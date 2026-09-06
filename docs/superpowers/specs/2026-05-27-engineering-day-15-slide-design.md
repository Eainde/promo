# Nexus AI & PromptLint — Engineering Day Presentation (Condensed)

## Session Overview
- **Title:** Nexus AI & PromptLint — AI Engineering at dbCLM
- **Duration:** ~45 min total (26 min content + 19 min Q&A)
- **Slides:** 15
- **Forum:** Deutsche Bank Engineering Day
- **Presenter:** Akshay Dipta
- **Format:** Slides with code + real execution screenshots (no live demo)
- **Audience:** Developers, testers, architects, tech management
- **Prior context:** Audience attended a Python LangChain/LangGraph session

## Design Rationale
Condensed from 37-slide / 45-min version. Key changes:
- Cut from 37 → 15 slides, 45 min content → 26 min content
- Removed: separate agenda, architecture goals, node types, graph state, bridge/AI-node, BatchAccumulatorTool, enterprise auth, failure layers, agent type profiles, REST API, 7-steps, CSM before/after, adoption, open-source, separate close
- Added: 3 "real run" slides replacing demo — actual DB tables showing workflow execution, agent trace, prompt config
- Weight is on **the framework** (Nexus AI + PromptLint), not on what was delivered with it
- Dropped topics are covered verbally while showing code or not at all

## Slide-by-Slide Spec

---

### Section 1: Context (2 slides, ~3 min)

#### Slide 1 — Title
- **Nexus AI & PromptLint**
- Subtitle: AI Engineering at dbCLM
- Presenter: Akshay Dipta — Senior Engineer, CLM Tech
- Date, Engineering Day branding
- No agenda slide — walk through structure verbally in opening remarks

#### Slide 2 — The Problem + Vision
Merged from original slides 3-4. Split layout:

**Top half — The Pain (red/warning styling):**
- 18–24 hours to build a single AI agent
- Every team re-implements orchestration, retry, guardrails from scratch
- No quality gates for prompts — silent degradation
- No observability — no audit trail for AI decisions
- Duplicated infrastructure across teams

**Bottom half — What If (green/blue transition):**
1. What if creating an AI agent took **1 hour** instead of 24?
2. What if you got **observability, enterprise auth, guardrails, and prompt quality testing** — for free?
3. What if a **12-agent pipeline** could be defined in **20 lines of code**?

**Verbal:** "That's what Nexus AI and PromptLint deliver. Let me show you how."

---

### Section 2: Architecture + Tier 1 Code (2 slides, ~3 min)

#### Slide 3 — Two-Tier Architecture
The core architecture diagram:

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
│  │  Guardrails | Tools | UntypedAgent                 │  │
│  │  sequence() | parallel() | loopUntil()             │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  Enterprise Auth | DB-Driven Prompts | Observability     │
└──────────────────────────────────────────────────────────┘
```

**Key point spoken:** "Nexus AI is the complete platform. Both tiers live inside it. Tier 1 answers 'what steps does this workflow have?' — Tier 2 answers 'how does this AI step work internally?' We built checkpoints, graph state management, and observability on top of LangGraph4j — it's not a separate layer, it's integrated."

**Verbal additions (no separate slides):**
- "You know graph concepts from the Python LangGraph session — LangGraph4j is the Java port, and Nexus AI wraps it with checkpoints, enterprise auth, and observability"
- Why Java-native: "I rejected the Python proposal. Our ecosystem is Spring Boot, our teams are Java engineers. Java-native means direct access to DI, WIF auth, existing infrastructure."
- Node types: "Non-AI nodes handle file I/O, API calls, storage. AI nodes delegate to Tier 2. Decision nodes route conditionally."

#### Slide 4 — Code: Tier 1 Graph Definition

```java
var workflow = new StateGraph<>(CsmWorkflowState.class)

    // Register nodes
    .addNode("downloadDocuments", documentDownloadNode)
    .addNode("uploadToGcs",      gcsUploadNode)
    .addNode("csmExtraction",    csmExtractionAiNode)
    .addNode("storeResults",     resultStorageNode)

    // Define edges
    .addEdge(START,                "downloadDocuments")
    .addEdge("downloadDocuments",  "uploadToGcs")
    .addEdge("uploadToGcs",        "csmExtraction")
    .addEdge("csmExtraction",      "storeResults")
    .addEdge("storeResults",       END)

    .compile();
```

**Spoken:** "This is a real workflow. Four nodes, linear flow. The CSM Extraction node is the AI Node — it contains the entire 12-agent Tier 2 pipeline inside it. The graph doesn't need to know about that complexity."

**Verbal additions:** Graph state is a typed object carrying data between nodes — file paths, extracted text, results. Each node reads what it needs and writes what it produces. Nodes are Spring-managed beans with full DI access.

---

### Section 3: Agent Pipeline (4 slides, ~8 min)

#### Slide 5 — Code: AgentSpec

```java
AgentSpec candidateExtractor = AgentSpec.builder()
    .name("NAMED_ENTITY_EXTRACTION_V2")
    .inputs("documentText", "documentSource")
    .outputKey("extractedCandidates")
    .tools(batchAccumulatorTool)
    .inputGuardrails(batchResetInputGuardrail)
    .outputGuardrails(
        jsonSchemaOutputGuardrail,
        batchMergerOutputGuardrail
    )
    .maxSequentialToolExecutions(50)
    .listener(agentMonitor)
    .build();
```

**Spoken walk-through of each field:**
- `name` → maps to DB prompt table. Model params, system instructions, temperature — all loaded from DB at runtime
- `inputs` → declares which scope keys this agent reads. Framework resolves values from AgenticScope automatically
- `outputKey` → where this agent writes its result. Downstream agents read from this key
- `tools` → Java objects with @Tool methods exposed to the LLM
- `inputGuardrails` → validation before LLM call (can block, rewrite, or pass)
- `outputGuardrails` → validation after LLM call (can retry, halt, or pass)
- `listener` → AgentMonitor for observability

**Key point:** "This is purely declarative. You describe WHAT the agent needs — the framework handles HOW it runs."

#### Slide 6 — Composition Patterns
Three diagrams side by side:

**sequence():**
```
[Agent A] → [Agent B] → [Agent C]
  Each reads previous agent's output
```

**parallel():**
```
         ┌→ [Agent A] ─┐
Input ───┤              ├──→ Merged Output
         └→ [Agent B] ─┘
```

**loopUntil():**
```
[Agent A] → [Agent B] → predicate?
    ↑                      │ no
    └──────────────────────┘
                           │ yes → done
```

**Spoken:** "These can be nested. A sequence can contain parallel groups, which can contain sub-sequences. This nesting is how you build complex pipelines from simple patterns."

#### Slide 7 — Code: 12-Agent Pipeline
The money slide:

```java
return agentFactory.sequence(Workflow.class, "extractionReview",
    // Wave 1: Extract + classify in parallel
    agentFactory.parallel("wave1",
        candidateExtractor, sourceClassifier),
    // Wave 2-4: Sequential processing
    nameNormalizer,
    dedupLinker,
    csmClassifier,
    // Wave 5: Parallel enrichment
    agentFactory.parallel("wave5",
        countryOverride, titleExtractor, scoringEngine),
    // Wave 5m: Merge parallel outputs (pure Java agent)
    waveMerger,
    // Wave 6-7: Assemble + format
    reasonAssembler,
    outputFormatter,
    // Wave 8+: Quality refinement loop
    agentFactory.loopUntil(3,
        scope -> scope.get("score") >= 0.85,
        critic, refiner)
);
```

**Spoken:** Walk through each wave — what it does, which pattern it uses, why parallel vs sequential. Emphasize: "12 agents, ~20 lines. All execution, scope management, guardrails, batching, monitoring — handled by the framework."

#### Slide 8 — Code: Guardrails

**Left side — Input/Output guardrail outcomes (compact table):**

| | Pass | Modify | Stop |
|---|---|---|---|
| **Input** | `success()` | `successWithText()` | `fatal(reason)` |
| **Output** | `success()` | `retry(reason)` | `fatal(reason)` |

**Right side — Code example:**

```java
OutputGuardrail jsonGuardrail = (result) -> {
    try {
        objectMapper.readTree(result.text());
        return success();
    } catch (JsonProcessingException e) {
        return retry("Invalid JSON: " + e.getMessage());
    }
};
```

**Spoken:** "Guardrails are deterministic — they don't rely on the LLM. They're reusable Spring beans. Write a JSON guardrail once, use it across every agent. The framework handles the retry loop."

---

### Section 4: Real Run — Proof (3 slides, ~6 min)

These slides replace the live demo. Show actual DB screenshots from a production CSM workflow run.

#### Slide 9 — Real Run: Workflow Execution
**Content:** Screenshot of the workflow table showing a completed run.
- RUN_ID, STATUS: FINISHED, timestamps (STARTED_AT, COMPLETED_AT)
- DATA_CONTENT field showing input parameters

**Spoken:** "This is a real workflow execution from production. You can see the run ID, when it started, when it completed, the status. Every workflow run gets tracked like this — full compliance traceability."

#### Slide 10 — Real Run: Agent-by-Agent Trace
**Content:** Screenshot of the agent execution table showing all 12 agents from a single run.
- Each row: AGENT_NAME, AGENT_TYPE, STATUS, MODEL_NAME, TOKENS_IN, TOKENS_OUT, TOTAL_TOKENS, STARTED_AT, COMPLETED_AT
- Shows the data flowing agent by agent — which ran, in what order, how many tokens each consumed

**Spoken:** Walk through the rows: "Here's the candidate extractor — it consumed X tokens, took Y seconds. Here's the source classifier running in parallel — same start time. Then the sequential agents: normalizer, dedup, classifier. Then the parallel enrichment wave. And at the bottom, the critic-refiner loop — you can see it ran twice before the score threshold was met."

**Key point:** "Every single LLM call is recorded. Compliance teams can trace exactly how every AI decision was made. When an agent produces wrong output, you don't guess — you look up this table."

#### Slide 11 — Real Run: DB-Driven Prompts
**Content:** Screenshot of the `profile_messages` table showing actual agent prompt configurations.
- Columns: AGENT_NAME, TYPE, SYSTEM_INSTRUCTION, MODEL_NAME, TEMPERATURE, TOP_P, TOP_K, OUTPUT_TOKENS, THINKING_BUDGET, RESPONSE_SCHEMA, PROMPT_VERSION
- Reference screenshots: IMG_3957–3959

**Spoken:** "This is where all prompts live — in the database, not in code. Each agent has its own row. You can see the system instruction, the model parameters, the response schema. Change any of these and the next execution picks up the new config — no code change, no deployment, no PR. Prompt engineers iterate independently from developers."

**Verbal addition:** Briefly mention enterprise auth is also config-only — teams set application.properties and the WIF→Azure→Gemini chain is abstracted away.

---

### Section 5: PromptLint (3 slides, ~5 min)

#### Slide 12 — Prompts Are Code
**Large text / narrative build:**
1. Prompts define how LLM agents behave
2. Unlike application code: **no linting, no static analysis, no quality gates**
3. Prompts silently degrade — vague language, removed schemas, contradictory rules
4. Nobody can pinpoint **when** the regression happened

**Punchline (large text):**
> "PromptLint brings the discipline of static analysis to LLM prompts."

**Key stats:**
- Rule-based, deterministic — **no LLM calls**, no API keys
- Runs in **milliseconds**
- Fully deterministic: same prompt → same score

#### Slide 13 — 8 Quality Dimensions
| Dimension | Code | What It Checks |
|---|---|---|
| Clarity | CLR | Role definition, task statement, imperative verbs, vague language |
| Specificity | SPC | Numbered rules, concrete examples, quantified thresholds |
| Groundedness | GND | Source-grounding phrases, anti-hallucination guards |
| Output Contract | OUT | JSON examples valid, field-level docs, schema completeness |
| Constraint Coverage | CON | Edge cases, null/empty handling, boundary conditions |
| Consistency | CST | Template variable alignment, contradictory instructions |
| Token Efficiency | TKN | Length vs complexity ratio, redundancy detection |
| Injection Resistance | INJ | System/user boundary, input sanitization, role-lock |

Each dimension: score 0.0–1.0. Overall = weighted average based on agent type profile.

**Verbal:** Mention agent type profiles briefly — EXTRACTION weights groundedness highest, CLASSIFICATION weights specificity, etc. Custom profiles supported.

#### Slide 14 — Code: JUnit API + CI Integration
**Left side — JUnit assertion API:**

```java
@Test
void extractionPromptMeetsQualityBar() {
    PromptQualityAssert.assertThat(extractionPrompt)
        .hasOverallScoreAbove(0.75)
        .hasDimensionScoreAbove("GROUNDEDNESS", 0.80)
        .hasDimensionScoreAbove("OUTPUT_CONTRACT", 0.70)
        .hasNoFindingsWithSeverity(Severity.CRITICAL);
}
```

**Right side — CI pipeline diagram:**
```
[Code Change] → [Compile] → [Unit Tests] → [PromptLint] → [Integration Tests] → [Deploy]
                                               │
                                    Score < 0.75? → ❌ BUILD FAILS
                                    Score ≥ 0.75? → ✅ Continue
```

**Spoken:** "Test prompts the same way you test code. Same JUnit runner, same CI pipeline, same quality bar. Runs in milliseconds, no network calls, fully deterministic. Only runtime dependency is Jackson."

---

### Section 6: Close (1 slide, ~1 min)

#### Slide 15 — Getting Started + Thank You

**Top half — How to adopt:**
```xml
<dependency>
    <groupId>com.db.clm.kyc</groupId>
    <artifactId>nexus-ai</artifactId>
</dependency>

<dependency>
    <groupId>com.db.clm.kyc</groupId>
    <artifactId>clm-prompt-lint</artifactId>
</dependency>
```
- Documentation: Confluence — Agentic AI Strategy space
- Contact: Akshay Dipta — CLM Tech

**Bottom half:**
"Thank You — Questions?"

---

## Speech Design Notes
- ~26 min spoken content across 15 slides
- Narrative: Problem → Architecture → Code → Real Proof → Quality → Adopt
- Many topics from the 37-slide version are covered **verbally** while showing code slides — Java-native rationale, node types, graph state, bridge concept, enterprise auth, failure layers
- Code on slides is real production code, not pseudocode
- "Real Run" section (slides 9-11) replaces the demo with actual DB screenshots — more credible than a live demo that could fail
- Tone: technical, confident, conversational

## Deliverables
- Updated `RCP_session/presentation_outline.md` — 15-slide content guide
- Updated `RCP_session/speech.md` — ~26 min speech script
- PPT file generation (if requested)
