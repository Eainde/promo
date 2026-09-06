# Engineering Day 15-Slide Presentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite `RCP_session/presentation_outline.md` (15-slide content guide) and `RCP_session/speech.md` (~26 min speech script) from the condensed spec.

**Architecture:** Two markdown deliverables replacing the existing 37-slide versions. The presentation outline is the slide-by-slide content reference for building the PPT. The speech script is the word-for-word spoken content timed to ~26 min. Both follow the spec at `docs/superpowers/specs/2026-05-27-engineering-day-15-slide-design.md`.

**Tech Stack:** Markdown content files. No code dependencies.

**Key constraints:**
- 15 slides only, ~26 min spoken content
- Weight on the framework (Nexus AI + PromptLint), not on deliverables/impact
- Real DB execution screenshots replace live demo (slides 9-11)
- Nexus AI is the outer umbrella — LangGraph4j is inside it, not a separate layer
- Dropped topics (Java-native rationale, node types, graph state, bridge, enterprise auth, failure layers) covered verbally only — no slides
- Code on slides is real production code, not pseudocode

---

### Task 1: Write the presentation outline (RCP_session/presentation_outline.md)

**Files:**
- Overwrite: `RCP_session/presentation_outline.md`

**Reference:** Spec at `docs/superpowers/specs/2026-05-27-engineering-day-15-slide-design.md` — the slide-by-slide section is the primary source. The old 37-slide `RCP_session/presentation_outline.md` can be referenced for code snippets and diagrams that carry over unchanged.

- [ ] **Step 1: Write the header and Section 1 (slides 1-2)**

Replace all content in `RCP_session/presentation_outline.md` with:

```markdown
# Nexus AI & PromptLint — Engineering Day Presentation Outline

> 15 slides | ~26 min content + ~19 min Q&A
> Presenter: Akshay Dipta — Senior Engineer, CLM Tech
> Forum: Deutsche Bank Engineering Day

---

## Section 1: Context (~3 min)

### Slide 1 — Title Slide

**Title:** Nexus AI & PromptLint
**Subtitle:** AI Engineering at dbCLM
**Presenter:** Akshay Dipta — Senior Engineer, CLM Tech
**Date:** [Engineering Day date]

No agenda slide. Walk through the session structure verbally in opening remarks.

---

### Slide 2 — The Problem + Vision

**Split layout — two halves:**

**Top half — The Pain (red/warning styling):**
- 18–24 hours to build a single AI agent
- Every team re-implements orchestration, retry, guardrails from scratch
- No quality gates for prompts — silent degradation
- No observability — no audit trail for AI decisions
- Duplicated infrastructure across teams

**Bottom half — What If (green/blue transition, staggered reveal):**
1. What if creating an AI agent took **1 hour** instead of 24?
2. What if you got **observability, enterprise auth, guardrails, and prompt quality testing** — for free?
3. What if a **12-agent pipeline** could be defined in **20 lines of code**?

---
```

- [ ] **Step 2: Write Section 2 (slides 3-4)**

Append to the file:

```markdown
## Section 2: Architecture + Tier 1 Code (~3 min)

### Slide 3 — Two-Tier Architecture

**Heading:** Nexus AI — Two-Tier Architecture

**Diagram:**

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

**Key callouts on the diagram:**
- Nexus AI is the outer box — both tiers are inside it
- Tier 1 (Workflow Orchestration) built on LangGraph4j — includes checkpoints, graph state, conditional edges
- Tier 2 (Agent Pipeline) built on LangChain4j — AgentFactory, AgentSpec, guardrails, tools
- Cross-cutting: Enterprise Auth, DB-Driven Prompts, Observability span both tiers

**Verbal additions (no separate slides):**
- "You know graph concepts from the Python LangGraph session — LangGraph4j is the Java port, and Nexus AI wraps it with checkpoints, enterprise auth, and observability"
- Java-native rationale: "I rejected the Python proposal. Our ecosystem is Spring Boot, our teams are Java engineers. Direct access to DI, WIF auth, existing infrastructure."
- Node types: "Non-AI nodes handle file I/O, API calls, storage. AI nodes delegate to Tier 2. Decision nodes route conditionally."

---

### Slide 4 — Code: Tier 1 Graph Definition

**Heading:** Wiring a Workflow Graph

**Code block (Java) — real CSM workflow:**

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

**Callout:** "This is a real workflow. Four nodes, linear flow. The CSM Extraction node is the AI Node — it contains the entire 12-agent Tier 2 pipeline inside it."

**Verbal additions:** Graph state is typed object carrying data between nodes. Each node reads what it needs and writes what it produces. Nodes are Spring-managed beans with full DI access.

---
```

- [ ] **Step 3: Write Section 3 (slides 5-8)**

Append to the file:

```markdown
## Section 3: Agent Pipeline (~8 min)

### Slide 5 — Code: AgentSpec

**Heading:** Defining an Agent — Declarative Config

**Code block (Java):**

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

**Walk-through callouts (one per field):**
- `name` → maps to DB prompt table. Model params, system instructions, temperature loaded from DB at runtime
- `inputs` → declares which scope keys this agent reads. Framework resolves from AgenticScope automatically
- `outputKey` → where this agent writes its result. Downstream agents read from this key
- `tools` → Java objects with @Tool methods exposed to the LLM
- `inputGuardrails` → validation before LLM call (can block, rewrite, or pass)
- `outputGuardrails` → validation after LLM call (can retry, halt, or pass)
- `listener` → AgentMonitor for observability

**Key callout:** "Purely declarative. You describe WHAT the agent needs — the framework handles HOW it runs."

---

### Slide 6 — Composition Patterns

**Heading:** Composing Agents — sequence, parallel, loopUntil

**Three diagrams side by side:**

**sequence():**
[Agent A] → [Agent B] → [Agent C]
  Each reads previous agent's output

**parallel():**
         ┌→ [Agent A] ─┐
Input ───┤              ├──→ Merged Output
         └→ [Agent B] ─┘
  All read from same scope state, execute concurrently

**loopUntil():**
[Agent A] → [Agent B] → predicate?
    ↑                      │ no
    └──────────────────────┘
                           │ yes → done
  Loop until quality threshold met or max iterations

**Key point:** "These patterns can be nested. A sequence can contain parallel groups, which can contain sub-sequences."

---

### Slide 7 — Code: 12-Agent Pipeline

**Heading:** 12-Agent Pipeline in ~20 Lines

**Code block (Java) — the money slide:**

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

**Callout:** "12 agents. Parallel execution, sequential chaining, iterative refinement — all in ~20 lines. The framework handles scope management, guardrails, batching, monitoring, and retry."

---

### Slide 8 — Code: Guardrails

**Heading:** Guardrails — Deterministic Validation at Every Step

**Left side — Input/Output guardrail outcomes (compact table):**

|          | Pass         | Modify              | Stop            |
|----------|-------------|---------------------|-----------------|
| **Input**  | success()   | successWithText()   | fatal(reason)   |
| **Output** | success()   | retry(reason)       | fatal(reason)   |

**Right side — Code example:**

OutputGuardrail jsonGuardrail = (result) -> {
    try {
        objectMapper.readTree(result.text());
        return success();
    } catch (JsonProcessingException e) {
        return retry("Invalid JSON: " + e.getMessage());
    }
};

**Callout:** "Guardrails are deterministic — they don't rely on the LLM. Reusable Spring beans. Write a JSON guardrail once, use it across every agent."

---
```

- [ ] **Step 4: Write Section 4 (slides 9-11)**

Append to the file:

```markdown
## Section 4: Real Run — Proof (~6 min)

These slides replace the live demo. Show actual DB screenshots from a production CSM workflow run.

### Slide 9 — Real Run: Workflow Execution

**Heading:** Production Run — Workflow Execution

**Content:** Screenshot of the workflow table showing a completed run.
- RUN_ID, STATUS: FINISHED, timestamps (STARTED_AT, COMPLETED_AT)
- DATA_CONTENT field showing input parameters

**Verbal walk-through:** "This is a real workflow execution from production. You can see the run ID, when it started, when it completed, the status. Every workflow run gets tracked like this — full compliance traceability."

---

### Slide 10 — Real Run: Agent-by-Agent Trace

**Heading:** Production Run — Agent Execution Trace

**Content:** Screenshot of the agent execution table showing all 12 agents from a single run.
- Each row: AGENT_NAME, AGENT_TYPE, STATUS, MODEL_NAME, TOKENS_IN, TOKENS_OUT, TOTAL_TOKENS, STARTED_AT, COMPLETED_AT
- Shows data flowing agent by agent — which ran, in what order, how many tokens each consumed

**Verbal walk-through:** Walk through rows — candidate extractor consumed X tokens in Y seconds, source classifier ran in parallel (same start time), then sequential agents (normalizer, dedup, classifier), then parallel enrichment wave, then critic-refiner loop (ran twice before score threshold met).

**Key point:** "Every single LLM call is recorded. Compliance teams can trace exactly how every AI decision was made."

---

### Slide 11 — Real Run: DB-Driven Prompts

**Heading:** Production Run — Prompt Configuration

**Content:** Screenshot of the profile_messages table showing actual agent prompt configurations.
- Columns: AGENT_NAME, TYPE, SYSTEM_INSTRUCTION, MODEL_NAME, TEMPERATURE, TOP_P, TOP_K, OUTPUT_TOKENS, THINKING_BUDGET, RESPONSE_SCHEMA, PROMPT_VERSION

**Reference screenshots:** IMG_3957–3959

**Verbal walk-through:** "This is where all prompts live — in the database, not in code. Each agent has its own row. Change any of these and the next execution picks up the new config — no code change, no deployment, no PR."

**Verbal addition:** Briefly mention enterprise auth is also config-only — teams set application.properties, WIF→Azure→Gemini chain is abstracted.

---
```

- [ ] **Step 5: Write Section 5 (slides 12-14)**

Append to the file:

```markdown
## Section 5: PromptLint (~5 min)

### Slide 12 — Prompts Are Code

**Heading:** Prompts Are Code. Treat Them Like Code.

**Narrative build (large text, staggered):**
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

---

### Slide 13 — 8 Quality Dimensions

**Heading:** 8 Orthogonal Quality Dimensions

| Dimension | Code | What It Checks |
|---|---|---|
| **Clarity** | CLR | Role definition, task statement, imperative verbs, vague language |
| **Specificity** | SPC | Numbered rules, concrete examples, quantified thresholds |
| **Groundedness** | GND | Source-grounding phrases, anti-hallucination guards |
| **Output Contract** | OUT | JSON examples valid, field-level docs, schema completeness |
| **Constraint Coverage** | CON | Edge cases, null/empty handling, boundary conditions |
| **Consistency** | CST | Template variable alignment, contradictory instructions |
| **Token Efficiency** | TKN | Length vs complexity ratio, redundancy detection |
| **Injection Resistance** | INJ | System/user boundary, input sanitization, role-lock |

**Footer:** Each dimension scores 0.0–1.0. Overall = weighted average based on agent type profile.

**Verbal:** Mention agent type profiles — EXTRACTION weights groundedness highest, CLASSIFICATION weights specificity, etc. Custom profiles supported.

---

### Slide 14 — Code: JUnit API + CI Integration

**Heading:** Test Prompts Like You Test Code

**Left side — JUnit assertion API:**

@Test
void extractionPromptMeetsQualityBar() {
    PromptQualityAssert.assertThat(extractionPrompt)
        .hasOverallScoreAbove(0.75)
        .hasDimensionScoreAbove("GROUNDEDNESS", 0.80)
        .hasDimensionScoreAbove("OUTPUT_CONTRACT", 0.70)
        .hasNoFindingsWithSeverity(Severity.CRITICAL);
}

**Right side — CI pipeline diagram:**

[Code Change] → [Compile] → [Unit Tests] → [PromptLint] → [Integration Tests] → [Deploy]
                                               │
                                    Score < 0.75? → ❌ BUILD FAILS
                                    Score ≥ 0.75? → ✅ Continue

**Callout:** "Same JUnit runner. Same CI pipeline. Same quality bar. Runs in milliseconds, no network calls, fully deterministic."

---
```

- [ ] **Step 6: Write Section 6 (slide 15)**

Append to the file:

```markdown
## Section 6: Close (~1 min)

### Slide 15 — Getting Started + Thank You

**Top half — How to adopt:**

Maven dependencies:
  com.db.clm.kyc : nexus-ai
  com.db.clm.kyc : clm-prompt-lint

- Documentation: Confluence — Agentic AI Strategy space
- Contact: Akshay Dipta — CLM Tech

**Bottom half:**
"Thank You — Questions?"
```

- [ ] **Step 7: Review outline against spec**

Read through the completed `RCP_session/presentation_outline.md` and verify:
- Exactly 15 slides numbered 1-15
- All 6 sections present with correct slide ranges
- All code snippets match the spec exactly
- Diagram on slide 3 shows Nexus AI as outer box with both tiers inside
- Slides 9-11 reference real DB screenshots (no conceptual diagrams)
- No impact/adoption/open-source slides exist
- No dropped topics appear as slides (they appear only as "verbal" notes)

---

### Task 2: Write the speech script (RCP_session/speech.md)

**Files:**
- Overwrite: `RCP_session/speech.md`

**Reference:** The spec's "Spoken" and "Verbal additions" notes for each slide. The old 37-slide `RCP_session/speech.md` can be referenced for phrasing and flow — reuse good spoken language where the content carries over.

**Target:** ~26 min spoken = ~2,600-3,000 words (at ~110 words/min conversational pace).

**Per-section word targets:**
- Section 1 (Context): ~330 words / ~3 min
- Section 2 (Architecture + Tier 1 Code): ~330 words / ~3 min
- Section 3 (Agent Pipeline): ~880 words / ~8 min
- Section 4 (Real Run): ~660 words / ~6 min
- Section 5 (PromptLint): ~550 words / ~5 min
- Section 6 (Close): ~110 words / ~1 min

- [ ] **Step 1: Write the header and Section 1 speech (slides 1-2)**

Replace all content in `RCP_session/speech.md` with:

```markdown
# Nexus AI & PromptLint — Engineering Day Speech

> ~26 min spoken content | 15 slides
> Tone: Technical, confident, conversational. Speaking to devs, architects, and tech management.
> Audience has attended a Python LangChain/LangGraph session — they know graph/agent basics.

---

## Section 1: Context (Slides 1–2, ~3 min)

**[Slide 1 — Title]**

Good morning everyone. I'm Akshay Dipta, Senior Engineer in CLM Tech. Today I'm going to take you inside Nexus AI and PromptLint — two things I've built that are changing how we do AI engineering across dbCLM.

Here's what we'll cover in about 25 minutes. I'll start with the problem — why we needed to build this. Then I'll show you the architecture and walk through real code — how you define a workflow graph, how you define agents, how you compose a 12-agent pipeline in 20 lines of code. Then I'll show you real production execution data — actual database records from a live run, so you can see how data flows through the system. After that, PromptLint — a static quality analyzer for LLM prompts. And we'll wrap up with how to get started. We'll have plenty of time for questions.

**[Slide 2 — The Problem + Vision]**

So let's start with the problem. When we began exploring AI agents in dbCLM, building a single agent took 18 to 24 hours. Every team was writing their own orchestration logic, their own retry mechanisms, their own guardrails — all from scratch. There were no quality gates for prompts. Someone could change a prompt, the agent would start hallucinating, and nobody could tell you when the regression happened. There was no observability — no audit trail showing what the AI decided and why. And every team was duplicating the same infrastructure independently.

So I asked three questions. What if creating an AI agent took one hour instead of 24? What if you got observability, enterprise authentication, guardrails, and prompt quality testing — built in, for free? And what if a 12-agent pipeline could be defined in 20 lines of code?

That's what Nexus AI and PromptLint deliver. Let me show you how.

---
```

- [ ] **Step 2: Write Section 2 speech (slides 3-4)**

Append to the file:

```markdown
## Section 2: Architecture + Tier 1 Code (Slides 3–4, ~3 min)

**[Slide 3 — Two-Tier Architecture]**

Here's the high-level architecture. Nexus AI is the complete platform — everything you see on this slide lives inside it.

There are two tiers. Tier 1 is the workflow orchestration layer, built on LangGraph4j — the Java port of LangGraph that you saw in the Python session. But we've added checkpoints, graph state management, and observability on top. It's not just LangGraph in Java — it's LangGraph integrated into the Nexus AI platform.

Tier 1 defines the overall workflow as a directed graph. Nodes are processing steps — some are standard Java logic like downloading files, calling APIs, storing results. But one or more nodes are AI Nodes, and that's where Tier 2 comes in.

Tier 2 is the agent pipeline layer, built on LangChain4j. AgentFactory, AgentSpec, guardrails, tools — everything needed to orchestrate multi-agent AI pipelines with parallel execution, sequential chaining, and iterative loops.

And spanning both tiers — enterprise authentication, database-driven prompts, and full observability. These aren't bolted on — they're built into the platform.

Now, why Java and not Python? When this initiative started, there was a proposal to build it in Python. I rejected that. Our ecosystem is Spring Boot. Our teams are Java engineers. Java-native means direct access to dependency injection, the bank's WIF authentication libraries, our existing database infrastructure — all natively. No bridges, no adapters, no second deployment pipeline.

**[Slide 4 — Code: Tier 1 Graph Definition]**

Here's what a workflow looks like in code. This is real — the CSM extraction workflow.

Four nodes. We register each node — download documents, upload to cloud storage, CSM extraction, and store results. Then we define the edges — start to download, download to upload, upload to extraction, extraction to storage, storage to end. Compile. That's it.

The interesting part is that CSM Extraction AI Node. It looks like just another node in the graph. But inside it, there's a full 12-agent Tier 2 pipeline. The graph doesn't need to know about that complexity — it just sees a node that takes input state and returns output state.

The graph state is a typed object that carries data between nodes — file paths, extracted text, processing results. Each node reads what it needs and writes what it produces. And because nodes are Spring-managed beans, they have full access to dependency injection — your repositories, your services, your configuration.

---
```

- [ ] **Step 3: Write Section 3 speech (slides 5-8)**

Append to the file:

```markdown
## Section 3: Agent Pipeline (Slides 5–8, ~8 min)

**[Slide 5 — Code: AgentSpec]**

Now let's go inside that AI Node. This is Tier 2.

Every agent in Nexus AI is defined by an AgentSpec. This is the heart of the framework — purely declarative configuration.

Let me walk you through this real example. The name — NAMED_ENTITY_EXTRACTION_V2 — maps directly to the prompt lookup in the database. All model parameters, system instructions, temperature — loaded from the database at runtime. You change the prompt without changing code.

Inputs declares which keys this agent reads from the shared scope. The framework resolves the values automatically — you just declare what you need. OutputKey is where this agent writes its result. Downstream agents read from this key.

Tools are Java objects with @Tool-annotated methods. The LLM sees these as callable functions. In this case, the batch accumulator tool handles cases where the output exceeds the LLM's token limit — it paginates automatically.

Input guardrails run before the LLM call — they can block invalid input, rewrite it, or pass it through. Output guardrails run after — they can retry on bad output, validate JSON schema, merge batches. The listener is the AgentMonitor that tracks timing, inputs, outputs, and errors for observability.

This is purely declarative. You describe what the agent needs. The framework handles how it runs.

**[Slide 6 — Composition Patterns]**

Now, how do you combine agents? Three composition patterns.

Sequence — agents execute one after another. Each agent reads the previous agent's output from the scope. This is your standard pipeline: extract, then normalize, then classify.

Parallel — agents execute concurrently. All of them read from the same scope state, and their results are written to separate output keys. Use this when agents are independent — extract names in parallel with classifying document sources.

LoopUntil — two agents execute in a loop until a predicate evaluates to true or you hit the maximum iterations. This is for iterative quality refinement — a critic evaluates the output, a refiner improves it, and you loop until the quality score meets your threshold.

And critically — these can be nested. A sequence can contain parallel groups. A parallel group can contain sub-sequences. This nesting is how you build complex pipelines from simple patterns.

**[Slide 7 — Code: 12-Agent Pipeline]**

And here's the payoff. This is the entire CSM extraction pipeline. 12 agents. About 20 lines of code.

Wave 1: candidate extractor and source classifier run in parallel — extracting names while simultaneously classifying document sources. Waves 2 through 4: name normalizer, dedup linker, and CSM classifier run in sequence — normalizing names, removing duplicates, classifying each candidate. Wave 5: country override, title extractor, and scoring engine run in parallel — enriching each candidate with country rules, titles, and scores. Wave 5m: a pure Java agent — not an LLM agent — that merges the parallel outputs into a single enriched record. Waves 6 and 7: reason assembler and output formatter run in sequence. And wave 8 onward: a critic and refiner loop until the extraction score hits 0.85, with a maximum of 3 iterations.

All execution, scope management, guardrails, batching, monitoring — handled by the framework. You define what happens. Nexus AI handles how.

**[Slide 8 — Code: Guardrails]**

Guardrails provide deterministic validation at every step — independent of the LLM.

Input guardrails run before the LLM call. Three outcomes: pass — proceed. Rewrite — modify the input, then proceed. Or block — the input is invalid, the LLM call is blocked entirely.

Output guardrails run after. Pass — the output is valid. Retry — re-invoke the LLM. Or halt — unrecoverable error.

Here's a real example — a JSON validation guardrail. It tries to parse the LLM's output as JSON. If it succeeds, pass. If it fails, retry with the error message. The framework handles the retry loop — you just define the validation logic.

These are reusable Spring beans. Write a guardrail once, use it across every agent in the platform.

---
```

- [ ] **Step 4: Write Section 4 speech (slides 9-11)**

Append to the file:

```markdown
## Section 4: Real Run — Proof (Slides 9–11, ~6 min)

**[Slide 9 — Real Run: Workflow Execution]**

Now let me show you this running in production. No demo — something better. Actual database records from a real CSM workflow execution.

This is the workflow table. You can see the run ID, the status — finished. The timestamps showing when it started and when it completed. The data content field showing the input parameters that triggered this run.

Every single workflow execution creates a record like this. You can query any run, see its status, see how long it took. Full compliance traceability — you know exactly what ran, when, and what triggered it.

**[Slide 10 — Real Run: Agent-by-Agent Trace]**

This is where it gets interesting. The agent execution table — every LLM call within that workflow run.

Look at the rows. Here's the candidate extractor — you can see the agent name, the model it used, how many tokens went in, how many came out, when it started, when it completed. And here's the source classifier — notice it has the same start time as the candidate extractor. That's because they ran in parallel — wave 1 of our pipeline.

Then the sequential agents — name normalizer, dedup linker, CSM classifier. Each starts after the previous one completes. Then the parallel enrichment wave — country override, title extractor, scoring engine — again, same start times.

And down at the bottom, the critic-refiner loop. You can see it executed twice — the first iteration didn't meet the 0.85 score threshold, so it looped. The second iteration passed.

This is the power of the observability layer. Every single LLM call is recorded — what prompt was sent, what model was used, what tokens it consumed, what it returned. When an agent produces the wrong output, you don't guess. You look up this table and see exactly what happened.

**[Slide 11 — Real Run: DB-Driven Prompts]**

And this is where the prompts live. The profile_messages table.

Each row is one agent's complete prompt configuration. You can see the agent name, the system instruction, the model name, temperature, top P, top K, output tokens, thinking budget, the response schema, and the prompt version.

This is one of my favourite design decisions. Prompts live in the database, not in code. You want to change how the candidate extractor behaves? Update this row. The next execution picks up the new prompt — no code change, no pull request, no deployment. Prompt engineers iterate independently from developers.

And the prompt version field means you always know which version of the prompt produced a given result. Combined with the agent execution table, you have full traceability from trigger to output.

One more thing I'll mention briefly — enterprise authentication is also purely configuration. Teams set their WIF provider and keystore paths in application.properties, and the entire authentication chain — WIF to Azure to JWT to Gemini — is handled internally by the platform.

---
```

- [ ] **Step 5: Write Section 5 speech (slides 12-14)**

Append to the file:

```markdown
## Section 5: PromptLint (Slides 12–14, ~5 min)

**[Slide 12 — Prompts Are Code]**

Now let's switch to PromptLint. And I want to start with a fundamental question: what happens when a prompt goes bad?

Prompts are code. They define how LLM agents behave — what they extract, how they classify, what format they return. But unlike application code, prompts have no linting. No static analysis. No automated quality gates.

In practice, prompts silently degrade. Someone adds vague language. Someone removes the output schema. Someone introduces contradictory rules. The LLM starts hallucinating or returning malformed output. And nobody can pinpoint when the regression happened — because nobody was testing the prompt.

PromptLint changes that. It brings the discipline of static analysis to LLM prompts. Rule-based, deterministic — no LLM calls, no API keys, no latency. Runs in milliseconds. And it's fully deterministic: the same prompt always produces the same score.

**[Slide 13 — 8 Quality Dimensions]**

PromptLint evaluates prompts across eight independent dimensions.

Clarity — does the prompt have a clear role and task definition? Specificity — are there numbered rules, concrete examples, quantified thresholds? Groundedness — does it instruct the LLM to ground answers in source material and avoid hallucination? Output Contract — is the expected JSON schema documented with examples?

Constraint Coverage — what happens with edge cases, null values, empty inputs? Consistency — do template variables match declared inputs, are there contradictory instructions? Token Efficiency — is the prompt concise relative to its complexity? And Injection Resistance — is there system/user boundary enforcement, input sanitization?

Each dimension scores 0 to 1. The overall score is a weighted average — and the weights depend on the agent type. An extraction agent weights groundedness highest. A classification agent weights specificity. You can also define custom profiles with your own weights.

**[Slide 14 — Code: JUnit API + CI Integration]**

Here's how you use it. On the left — the JUnit assertion API.

A standard JUnit test that asserts your prompt has an overall score above 0.75, groundedness above 0.80, output contract above 0.70, and no critical-severity findings. Test prompts the same way you test code. Same JUnit runner. Same CI pipeline. Same quality bar.

On the right — how it fits into CI. After compilation and unit tests, PromptLint runs. If any prompt drops below your threshold — build fails. Fix the prompt before it reaches production.

The key properties that make this practical: it runs in milliseconds — no network calls. Fully deterministic — no randomness. And the only runtime dependency is Jackson for JSON validation.

---
```

- [ ] **Step 6: Write Section 6 speech (slide 15)**

Append to the file:

```markdown
## Section 6: Close (Slide 15, ~1 min)

**[Slide 15 — Getting Started + Thank You]**

To get started, add the Maven dependencies for Nexus AI and PromptLint. Configure your application.properties for authentication and model settings. The documentation is on Confluence in the Agentic AI Strategy space. And if you have questions or want help building your first workflow, reach out to me directly.

That's Nexus AI and PromptLint. A complete AI engineering platform — workflow orchestration, agent pipelines, enterprise authentication, prompt quality gates. Built in Java, running in production, available for your team to adopt.

Thank you. Happy to take questions.
```

- [ ] **Step 7: Review speech against spec and word count**

Verify:
- Speech references all 15 slides and only 15 slides
- Verbal additions from spec are woven into the speech at correct slide locations:
  - Slide 3: Java-native rationale, node types, LangGraph4j as integrated (not separate)
  - Slide 4: Graph state, Spring-managed beans
  - Slide 11: Enterprise auth mention
  - Slide 13: Agent type profiles
- No mentions of dropped content (CSM before/after, adoption, CSIO, open-source, 7-steps)
- Total word count is between 2,600-3,000 words (~26 min)
- Tone is technical, confident, conversational

---

### Task 3: Commit both files

**Files:**
- `RCP_session/presentation_outline.md`
- `RCP_session/speech.md`

- [ ] **Step 1: Commit**

```bash
git add RCP_session/presentation_outline.md RCP_session/speech.md
git commit -m "rewrite eng day presentation: 37 slides → 15, code + real run focus"
```
