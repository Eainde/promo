# Nexus AI & PromptLint — Engineering Day Presentation Outline

> 16 slides | ~25 min content + ~19 min Q&A
> Presenter: Akshay Dipta — Senior Engineer, CLM Tech
> Forum: Deutsche Bank Engineering Day

---

## Section 1: Context (~3 min) — Slides 1-2

---

### Slide 1 — Title Slide

**Title:** Nexus AI & PromptLint
**Subtitle:** AI Engineering at dbCLM
**Tagline:** Java & Kotlin Native — Spring Boot Powered
**Presenter:** Akshay Dipta — Senior Engineer, CLM Tech
**Date:** [Engineering Day Date]

> **Verbal note:** No agenda slide — walk the audience through structure verbally as you open. "I'm going to show you the problem we had, the framework we built, the code that runs it, a real live run, and a tool that keeps prompt quality honest."

---

### Slide 2 — The Problem + Vision

**Split layout**

**Top half — Problem (red/warning tone):**

- Building a new AI agent took **18-24 hours** of boilerplate setup
- Every team was **reimplementing** the same infrastructure from scratch
- **No prompt quality gates** — bad prompts reached production silently
- **No observability** — no visibility into token usage, latency, or failures
- **Duplicated infra** — auth, model config, retry logic copy-pasted everywhere

**Bottom half — Vision (green/blue tone):**

- What if a new agent took **1 hour**, not 24?
- What if a 12-agent orchestration pipeline was expressible in **20 lines of code**?
- What if observability, auth, and database-driven prompts were **built in by default**?
- What if prompt quality was **enforced in CI**, like code linting?
- What if you could **see your agents execute live**, click any node, inspect state?

---

## Section 2: Architecture + Tier 1 Code (~3 min) — Slides 3-4

---

### Slide 3 — Two-Tier Architecture

**CRITICAL:** Nexus AI is the OUTER box containing both tiers.

```
┌──────────────────────────────────────────────────────────┐
│                        NEXUS AI                          │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │         TIER 1 — Workflow Orchestration             │  │
│  │              (built on LangGraph4j)                 │  │
│  │                                                    │  │
│  │  ┌──────────┐   ┌──────────┐   ┌──────────┐       │  │
│  │  │ Non-AI   │──>│ AI Node  │──>│ Non-AI   │       │  │
│  │  │ Node     │   │ (Bridge) │   │ Node     │       │  │
│  │  └──────────┘   │  ┌─────┐│   └──────────┘       │  │
│  │                 │  │ T2  ││                       │  │
│  │                 │  └──┬──┘│                       │  │
│  │                 └─────┼───┘                       │  │
│  │  Checkpoints | Graph State | Conditional Edges    │  │
│  └───────────────────────┼────────────────────────────┘  │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │
│  ┌───────────────────────┼────────────────────────────┐  │
│  │         TIER 2 — Agent Pipeline                    │  │
│  │              (built on LangChain4j)                │  │
│  │                                                    │  │
│  │  AgentFactory | AgentSpec | AgenticScope           │  │
│  │  Tools | UntypedAgent                               │  │
│  │  sequence() | parallel() | loopUntil()             │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  Enterprise Auth | DB-Driven Prompts | Observability     │
└──────────────────────────────────────────────────────────┘
```

> **Verbal additions:**
> - Why Java-native? We rejected a Python-based solution — CLM runs on Java, our team is Java, and we didn't want a polyglot ops burden.
> - LangGraph4j is integrated, not a separate deployment — it runs inside the same JVM.
> - Two node types in Tier 1: Non-AI nodes (pure Java logic — download, store, transform) and AI Nodes (bridges into Tier 2 agent pipeline).

---

### Slide 4 — Code: Tier 1 Graph Definition (Real CSM Workflow)

**Actual CsmWorkflowGraph code from production:**

```java
StateGraph<CsmState> workflow = new StateGraph<>(CsmState::new);

workflow.addNode("document_aggregation",            documentAggregatorNode);
workflow.addNode("document_classification_node",    documentClassificationNode);
workflow.addNode("named_entity_extraction_node",    namedEntityExtractionNode);
workflow.addNode("csm_classification",              csmClassificationNode);
workflow.addNode("csm_comparison",                  csmComparisonNode);
workflow.addNode("de_duplication_node",             deDuplicationNode);
workflow.addNode("person_name_normalization_node",  personNameNormalizationNode);
workflow.addNode("auto_answer_trigger",             autoAnswerTriggeringNode);
workflow.addNode("csm_persistence",                 csmPersistenceNode);
workflow.addNode("persistence_complete_or_skipped", noOpNode);
workflow.addNode("party_search_complete_or_skipped", noOpNode);

workflow.addEdge(START, "document_aggregation");
workflow.addEdge("document_aggregation", "document_classification_node");
workflow.addConditionalEdges("document_classification_node",
    documentAggregationEdge,
    Map.of("named_entity_extraction_node", "named_entity_extraction_node", END, END));
workflow.addEdge("named_entity_extraction_node", "person_name_normalization_node");
workflow.addEdge("person_name_normalization_node", "de_duplication_node");
workflow.addEdge("de_duplication_node", "csm_classification");
workflow.addEdge("csm_classification", "csm_comparison");
workflow.addConditionalEdges("csm_comparison", csmPersistenceTriggeringEdge,
    Map.of("csm_persistence", "csm_persistence",
           "persistence_complete_or_skipped", "persistence_complete_or_skipped"));
workflow.addEdge("csm_persistence", "persistence_complete_or_skipped");
workflow.addConditionalEdges("persistence_complete_or_skipped",
    partySearchAssociationAndCreationEdge, ...);
workflow.addConditionalEdges("party_search_complete_or_skipped",
    autoAnswerTriggeringEdge,
    Map.of("auto_answer_trigger", "auto_answer_trigger", END, END));
workflow.addEdge("auto_answer_trigger", END);

return workflow.compile(
    CompileConfig.builder().checkpointSaver(checkpointSaver).build());
```

> **Verbal:** 11 nodes, 3 conditional edges, a sub-graph call, and checkpoint persistence — all expressed as a directed graph. This is the real production code.

---

## Section 3: Agent Pipeline (~7 min) — Slides 5-7

---

### Slide 5 — Code: AgentSpec

**The candidateExtractor AgentSpec:**

```java
AgentSpec candidateExtractor = AgentSpec.builder()
    .name("candidateExtractor")
    .inputs(List.of("documentText", "clientProfile"))
    .outputKey("extractedCandidates")
    .tools(List.of(documentSearchTool, entityResolutionTool))
    .maxSequentialToolExecutions(5)
    .listener(auditLogListener)
    .build();
```

> **Walk-through callouts:**
> - `inputs` — named bindings from graph state; no magic string passing
> - `outputKey` — result is written back to state under this key, available to downstream agents
> - `tools` — pluggable; any LangChain4j-compatible tool
> - `maxSequentialToolExecutions` — prevents runaway tool loops
> - `listener` — audit, metrics, tracing hook

---

### Slide 6 — Code: 12-Agent Pipeline

**~20 lines expressing the full CSM extraction pipeline:**

```java
AgentPipeline pipeline = agentFactory.sequence(
    agentFactory.parallel("wave1",
        nameExtractor,
        roleExtractor,
        organisationExtractor
    ),
    contextualiser,
    agentFactory.parallel("wave5",
        evidenceLinker,
        conflictDetector,
        confidenceScorer
    ),
    waveMerger,
    reasonAssembler,
    outputFormatter,
    agentFactory.loopUntil(
        3,
        result -> result.getScore() >= 0.85,
        critic,
        refiner
    )
);
```

> Three parallel waves reduce latency. Sequential agents depend on prior outputs. `loopUntil` drives quality — up to 3 critic/refiner iterations until score ≥ 0.85, then stops.

---

## Section 4: Real Run — Proof (~6 min) — Slides 8-10

---

### Slide 9 — Real Run: Workflow Execution

**Screenshot:** workflow execution table

| Column | Example Value |
|--------|---------------|
| RUN_ID | `csm-wf-20240518-0042` |
| STATUS | `FINISHED` |
| STARTED_AT | `2024-05-18 09:14:02.341` |
| FINISHED_AT | `2024-05-18 09:14:47.882` |
| DATA_CONTENT | `{ "csmCandidates": [...] }` |

> The entire 4-node workflow — download, GCS upload, 12-agent AI extraction, store — completes end-to-end. STATUS = FINISHED. Data is persisted.

---

### Slide 10 — Real Run: Agent-by-Agent Trace

**Screenshot:** agent execution table — all 12 agents visible

| AGENT_NAME | AGENT_TYPE | STATUS | MODEL_NAME | TOKENS_IN | TOKENS_OUT | STARTED_AT | FINISHED_AT |
|------------|------------|--------|------------|-----------|------------|------------|-------------|
| nameExtractor | PARALLEL | FINISHED | gemini-1.5-pro | 1240 | 380 | 09:14:18.001 | 09:14:21.443 |
| roleExtractor | PARALLEL | FINISHED | gemini-1.5-pro | 1198 | 290 | 09:14:18.001 | 09:14:22.107 |
| organisationExtractor | PARALLEL | FINISHED | gemini-1.5-pro | 1310 | 410 | 09:14:18.003 | 09:14:23.650 |
| contextualiser | SEQUENTIAL | FINISHED | gemini-1.5-pro | 2100 | 540 | 09:14:23.651 | 09:14:27.002 |
| ... | ... | ... | ... | ... | ... | ... | ... |

> **Walk-through:**
> - Wave 1 agents share the same STARTED_AT — proof of true parallelism
> - Sequential agents start only after their predecessor finishes
> - Loop iterations show as separate rows with incrementing attempt number
> - Every token is counted — cost visibility out of the box

---

### Slide 11 — Real Run: DB-Driven Prompts

**Screenshot:** `profile_messages` table

| AGENT_NAME | TYPE | SYSTEM_INSTRUCTION | MODEL_NAME | TEMPERATURE |
|------------|------|-------------------|------------|-------------|
| nameExtractor | SYSTEM | You are a precise entity extractor... | gemini-1.5-pro | 0.1 |
| critic | SYSTEM | You are a strict quality evaluator... | gemini-1.5-pro | 0.0 |

> Prompts live in the database — not in code, not in config files. Change a prompt without a deployment. A/B test model versions by updating a row. Full audit trail of who changed what and when.

> **Reference:** Screenshots IMG_3957-3959 show the real production table.

---

## Section 4.5: Nexus AI Studio (~5 min) — Slides 12-13

---

### Slide 12 — Nexus AI Studio (Info)

**Split layout:**

**Left — Today:**
- **Graph Visualization** — renders workflow graph as interactive UI
- **Run Workflows from UI** — trigger and monitor executions in the browser
- **Live Execution Tracking** — agents light up, complete, or fail in real time
- **State Inspection** — click any node for full input/output at that checkpoint

**Right — Vision (Swagger for AI):**
- **Auto-Discover Agents** — scans app context, lists every registered agent
- **Run Individual Agents** — test any agent in isolation, pass input, see output
- **Run Full Workflows** — end-to-end pipelines with live graph feedback
- **One UI for Everything** — like Swagger gave APIs a face, Studio gives agents a face

**Footer:** React + TypeScript SPA, packaged as a Spring Boot JAR. Add one Maven dependency, get the full UI.

---

### Slide 13 — Nexus AI Studio (Live Demo)

**Screenshot of Studio UI** with CSM workflow loaded, showing:
- Three-panel layout: threads/input (left), graph visualization (centre), state inspector (right)
- All nodes completed with green checkmarks
- Sub-graph (party-search-graph) visible
- State panel showing checkpoint data

**Demo flow:** Talk over screenshot, then switch to live app.

**Fallback:** If live demo fails, stay on screenshot.

---

## Section 5: PromptLint (~5 min) — Slides 14-16

---

### Slide 14 — Prompts Are Code

**Narrative build — 4 points:**

1. A prompt that degrades model output doesn't throw an exception — it just silently returns worse results.
2. You won't catch it in unit tests. You may not catch it in integration tests. You catch it when a business user files a ticket.
3. We treat configuration as code, infrastructure as code — why not prompts as code?
4. PromptLint brings static analysis to prompt engineering: the same discipline we apply to Java, applied to the strings we send to models.

**Punchline quote:**
> *"A bad prompt is a bug. PromptLint finds it before it ships."*

**Key stats:**
- No LLM calls — fully deterministic, rule-based analysis
- Runs in milliseconds — fast enough for pre-commit hooks and CI gates
- Deterministic — same prompt always produces the same score

---

### Slide 15 — 8 Quality Dimensions

| Dimension | Code | What It Checks |
|-----------|------|----------------|
| Clarity | CLR | Sentence structure, ambiguous pronouns, vague quantifiers |
| Specificity | SPC | Under-constrained instructions, missing format requirements |
| Groundedness | GND | Hallucination risk — claims without context anchoring |
| Output Format | OUT | Missing output schema, ambiguous response format |
| Conciseness | CON | Redundancy, repetition, padding |
| Consistency | CST | Contradictory instructions within the same prompt |
| Token Efficiency | TKN | Unnecessary verbosity relative to instruction density |
| Injection Risk | INJ | Prompt injection surface area, missing delimiters |

> **Footer:** Each dimension scores 0-1. Weighted composite score 0-1. Configurable thresholds per dimension or aggregate.

> **Verbal mention:** Agent type profiles — a `critic` agent prompt is scored against a different profile than a `data extractor` prompt. Strictness weights differ by role.

---

### Slide 16 — JUnit API + CI Integration

**Left — Real JUnit test (production code):**

```java
@Test
@DisplayName("Fetch CSM_CLASSIFIER prompt from H2
  and validate quality report meets threshold
  and has no critical issues")
void shouldFetchAndValidateCsmClassifierPromptQuality() {
    String agentName = CSM_CLASSIFIER.getValue();
    Prompt prompt = nexusStoreProvider
        .prompts().lookup(agentName).get();
    assertNotNull(prompt, "Prompt should not be null.");

    PromptUnderTest promptUnderTest = new PromptUnderTest(
        agentName,
        prompt.getSystemInstruction(),
        prompt.getPromptText(),
        Set.of("gcsFilePath", "sourceClassification",
               "extractedCandidates"),
        "output",
        AgentTypeProfile.CLASSIFICATION,
        prompt.getResponseSchema());

    PromptQualityReport report =
        analyzer.analyze(promptUnderTest);

    assertThat(report)
        .printReport(0.75)
        .passesThreshold(0.75)
        .hasNoCriticalIssues();
}
```

**Right — Test execution output:**

```
PROMPT QUALITY REPORT: document-summarizer
Profile: EXTRACTION

Overall Score: 0.75 / 1.00  PASS (threshold: 0.50)

Dimension            Score  Weight  Contrib
CLARITY               1.00   0.10    0.100
SPECIFICITY           0.58   0.15    0.088
GROUNDEDNESS          0.92   0.25    0.229
OUTPUT_CONTRACT       0.83   0.15    0.125
CONSTRAINT_COVERAGE   0.20   0.15    0.030
CONSISTENCY           1.00   0.10    0.100
TOKEN_EFFICIENCY      1.00   0.05    0.050
INJECTION_RESISTANCE  0.63   0.05    0.031

Weakest: CONSTRAINT_COVERAGE (0.20)

Issues: 9 total (0 critical, 3 warning, 6 info)
WARN [SPC-004] No positive examples found
WARN [CON-001] No instructions for empty input
WARN [INJ-001] No defence against embedded prompts

Suggestions:
1. Add 2+ positive examples
2. Use proper JSON types
3. Show nullable fields as null in example
4. Add empty input handling instruction
5. Add ambiguous case guidance
6. Add prompt injection defence
```

> No extra service, no API key, no network call. Just a dependency on the classpath. Runs in milliseconds.

---

## Section 6: Close (~1 min) — Slide 17

---

### Slide 17 — Getting Started + Thank You

**Maven dependencies:**

```xml
<!-- Nexus AI framework -->
<dependency>
    <groupId>com.db.clm</groupId>
    <artifactId>nexus-ai</artifactId>
    <version>LATEST</version>
</dependency>

<!-- PromptLint static analyser -->
<dependency>
    <groupId>com.db.clm</groupId>
    <artifactId>clm-prompt-lint</artifactId>
    <version>LATEST</version>
</dependency>
```

**Resources:**
- Confluence: `CLM Tech / Nexus AI / Getting Started`
- Contact: Akshay Dipta — CLM Tech, Senior Engineer

---

## **Thank You — Questions?**
