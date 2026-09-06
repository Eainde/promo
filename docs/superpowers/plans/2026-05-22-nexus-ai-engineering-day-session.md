# Nexus AI Engineering Day Session — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a full 45-min speech script and detailed slide-by-slide presentation outline for a Deutsche Bank Engineering Day session on Nexus AI & PromptLint.

**Architecture:** Two deliverables — a speech script (`RCP_session/speech.md`) and a presentation outline (`RCP_session/presentation_outline.md`). The presentation outline contains all slide content (text, tables, code snippets, diagram descriptions) ready to be turned into PowerPoint. The speech script contains the spoken narration for each slide. Both follow the same 37-slide, 8-block structure defined in the spec.

**Tech Stack:** Markdown files. Content references Nexus AI (Java/Spring Boot, LangGraph4j, LangChain4j), PromptLint (Java library), and CSM workflow.

**Source material:**
- Spec: `docs/superpowers/specs/2026-05-22-nexus-ai-engineering-day-session-design.md`
- Nexus AI details: `new_work_nexus_ai.md`
- PromptLint details: `new_work_prompt_lint.md`
- CSM workflow details: `new_work_csm_workflow.md`
- Screenshots: `framework/IMG_3485.jpg`–`IMG_3499.jpg` (Confluence docs), `framework/IMG_3956.HEIC`–`IMG_3964.HEIC` (DB tables, app config)

**Key context:**
- Audience already attended a Python LangChain/LangGraph session — frame Java/Nexus AI as the enterprise equivalent, don't re-teach basics
- Tone: technical depth for devs/architects, accessible framing for management
- Code snippets should be realistic Java (based on patterns from the docs), not pseudocode
- Reference actual DB table screenshots on observability and prompt slides

---

## File Structure

| File | Responsibility |
|---|---|
| `RCP_session/presentation_outline.md` | Slide-by-slide content: titles, bullet points, tables, code blocks, diagram descriptions, speaker notes. Everything needed to build the PPT. |
| `RCP_session/speech.md` | Full spoken narration keyed to each slide. ~45 min of content (~5400-6000 words). Conversational but technical tone. |

---

### Task 1: Create Presentation Outline — Opening & Platform Overview (Slides 1–8)

**Files:**
- Create: `RCP_session/presentation_outline.md`

- [ ] **Step 1: Write slides 1–4 (Title, Agenda, The Pain, What If)**

Write the opening block of `RCP_session/presentation_outline.md` with document header and slides 1–4.

```markdown
# Nexus AI & PromptLint — Engineering Day Presentation Outline

> 37 slides | ~45 min content + 15 min Q&A
> Presenter: Akshay Dipta | Forum: Deutsche Bank Engineering Day

---

## Opening — The Problem (3 min)

### Slide 1 — Title Slide

**Title:** Nexus AI & PromptLint
**Subtitle:** AI Engineering at dbCLM
**Presenter:** Akshay Dipta — Senior Engineer, CLM Tech
**Date:** [Engineering Day date]

---

### Slide 2 — Agenda

| # | Topic | Time |
|---|---|---|
| 1 | The Problem — Why We Built This | 3 min |
| 2 | Nexus AI — Platform Overview | 5 min |
| 3 | Tier 1 — Workflow Graph (LangGraph4j) | 8 min |
| 4 | Tier 2 — Agent Pipeline (Nexus AI) | 10 min |
| 5 | Platform Features — Auth, Prompts, Observability | 5 min |
| 6 | PromptLint — Static Quality Analyzer | 10 min |
| 7 | CSM Workflow — Production Case Study | 5 min |
| 8 | Getting Started + Q&A | 19 min |

---

### Slide 3 — The Pain

**Heading:** Building AI Agents Today

**Bullet points (large text, one per line):**
- 18–24 hours to build a single AI agent
- Every team re-implements orchestration, retry, guardrails from scratch
- No quality gates for prompts — silent degradation over time
- No observability — no audit trail for AI decisions
- No enterprise authentication abstraction
- Duplicated infrastructure across teams

**Visual:** Red/warning styling. Before-state emphasis.

---

### Slide 4 — What If

**Heading:** What If...

**Three bold statements (large text, staggered reveal):**
1. What if creating an AI agent took **1 hour** instead of 24?
2. What if you got **observability, enterprise auth, guardrails, and prompt quality testing** — for free?
3. What if a **12-agent pipeline** could be defined in **20 lines of code**?

**Visual:** Transition from red (pain) to green/blue (vision). Clean, minimal slide.

---
```

- [ ] **Step 2: Write slides 5–8 (Platform Overview)**

Append slides 5–8 to `RCP_session/presentation_outline.md`.

```markdown
## Nexus AI — Platform Overview (5 min)

### Slide 5 — What Nexus AI Gives You

**Heading:** Nexus AI — The Complete AI Engineering Platform

**Feature list (icons + short descriptions):**
- **Two-Tier Architecture** — Separate workflow orchestration from AI agent logic
- **Built-in Observability** — 3-table audit trail: every LLM call, every node outcome, every workflow run
- **Enterprise Authentication** — WIF → Azure → Gemini auth chain, configured via properties
- **Input/Output Guardrails** — Deterministic validation before and after every LLM call
- **Database-Driven Prompts** — Deploy prompt changes without code changes
- **Automatic Batch Scaling** — BatchAccumulatorTool handles output exceeding token limits
- **Full Reproducibility** — Same prompt + same input = same output. Debug any past execution.

**Footer stat:** 95% reduction in agent development time | Production-proven | dbCLM-wide adoption

---

### Slide 6 — Architecture Goals

**Heading:** Architecture Goals

| Goal | What It Means |
|---|---|
| **Reusability** | Core components shared across all workflows. New workflows compose existing pieces rather than building from scratch. |
| **Extensibility** | New node types, agent types, guardrails, and tools can be added without modifying the core framework. Plugin-based, open/closed principle. |
| **Modularity** | Tier 1 nodes and Tier 2 agents are self-contained units with declared inputs and outputs. Both can be composed without code changes. |
| **Scalability** | Automatic output pagination handles LLM token limits. Parallel execution at both tiers maximizes throughput. |
| **Maintainability** | Prompts stored in database. Guardrails are reusable Spring beans. Agent configuration is declarative via AgentSpec. |
| **Observability** | Every node execution and every agent execution tracked. Execution metadata, inputs, outputs, and timings persisted to database. Full audit trail for compliance. |

---

### Slide 7 — Two-Tier Architecture Diagram

**Heading:** Two-Tier Architecture

**Diagram description (for PPT creation):**

```
┌─────────────────────────────────────────────────────┐
│              TIER 1 — LangGraph4j                   │
│           (Workflow Orchestration)                   │
│                                                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐      │
│  │ Non-AI   │───>│ AI Node  │───>│ Non-AI   │      │
│  │ Node     │    │ (Bridge) │    │ Node     │      │
│  │          │    │          │    │          │      │
│  │ File I/O │    │  ┌─────┐ │    │ Store    │      │
│  │ API call │    │  │     │ │    │ Results  │      │
│  │ Routing  │    │  │ T2  │ │    │ Notify   │      │
│  └──────────┘    │  │     │ │    └──────────┘      │
│                  │  └──┬──┘ │                       │
│                  └─────┼────┘                       │
│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │
│                  ┌─────┴────┐                       │
│              TIER 2 — Nexus AI                      │
│           (Agent Pipeline)                          │
│                                                     │
│  AgentFactory | AgentSpec | AgenticScope            │
│  Guardrails | Tools | UntypedAgent                  │
│                                                     │
│  sequence() | parallel() | loopUntil()              │
└─────────────────────────────────────────────────────┘
```

**Callout:** "You've seen LangGraph in the Python session — this is the Java-native equivalent, with Nexus AI built on top"

**Key point:** Tier 1 answers "what steps does this workflow have?" — Tier 2 answers "how does this AI step work internally?"

---

### Slide 8 — Why Java-Native?

**Heading:** Why Java-Native? (Not Python)

**Three columns or comparison points:**

| Consideration | Python Approach | Our Java-Native Approach |
|---|---|---|
| **Ecosystem** | Separate Python microservice | Native Spring Boot integration |
| **Team Skills** | Java teams learning Python | Teams use existing Java expertise |
| **Enterprise Integration** | Custom bridges to DB auth, Spring beans | Direct access to dependency injection, WIF auth, Spring beans |
| **Production Readiness** | Additional deployment pipeline | Same deployment as existing services |

**Callout:** "I rejected the Python-based solution and convinced technical management to go Java-native"

---
```

- [ ] **Step 3: Review slides 1–8 for completeness against spec**

Read through the written slides and verify every spec requirement for slides 1–8 is covered.

---

### Task 2: Create Presentation Outline — Tier 1 Deep Dive (Slides 9–12)

**Files:**
- Modify: `RCP_session/presentation_outline.md`

- [ ] **Step 1: Write slides 9–12**

Append Tier 1 deep dive slides to `RCP_session/presentation_outline.md`.

```markdown
## Tier 1 — LangGraph Deep Dive (8 min)

### Slide 9 — Directed Graph Model

**Heading:** Tier 1 — Workflow as a Directed Graph

**Three core concepts (with visual):**

```
[Trigger] → [Node A] → [Node B] ──→ [Node C] → [End]
                          │                ↑
                          └── [Node D] ────┘
                         (conditional)
```

- **Nodes** = Processing steps — each is a Java class implementing `AsyncNodeAction`
- **Edges** = Execution order — sequential, conditional, or parallel
- **Graph State** = Typed state object that carries data between nodes (file paths, processing results, metadata)

**Callout:** "If you attended the Python LangGraph session, this is the same concept — directed graph, nodes, edges — but implemented in Java with full Spring Boot integration"

---

### Slide 10 — Node Types

**Heading:** Three Types of Nodes

| Node Type | What It Does | Real Examples |
|---|---|---|
| **Non-AI Node** | Standard Java logic — file I/O, API calls, data transformation, routing | Document Download, GCS Upload, Result Storage, Notification |
| **AI Node** | Delegates to Tier 2 — contains a full Nexus AI agent pipeline | CSM Extraction (12-agent pipeline), Document Classification, Entity Resolution |
| **Decision Node** | Evaluates a condition and routes to different edges | Document size check → small doc path vs. large doc path |

**Visual:** Three boxes with distinct colors/icons for each type.

---

### Slide 11 — Graph State

**Heading:** Graph State — How Data Flows

**Key points:**
- Typed state object — each node declares what it reads and what it writes
- **Immutable at node boundaries** — nodes receive a snapshot, return updates
- Nodes are **Spring-managed beans** — full access to dependency injection
- State carries: file paths, extracted text, processing results, metadata, error info

**Visual:** Diagram showing state flowing through 3 nodes, each adding/reading fields.

```
State: {docId, source}
    → [Download Node] →
State: {docId, source, filePath, rawText}
    → [AI Extraction Node] →
State: {docId, source, filePath, rawText, extractedEntities, score}
    → [Storage Node] →
State: {docId, ..., storageResult, status: COMPLETE}
```

---

### Slide 12 — Code: Graph Definition

**Heading:** Wiring a Workflow Graph

**Code block (Java):**

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

**Callout:** "This is a real workflow. Four nodes, linear flow. The CSM Extraction node is the AI Node — it contains the entire 12-agent Tier 2 pipeline inside it."

---
```

---

### Task 3: Create Presentation Outline — Tier 2 Deep Dive (Slides 13–19)

**Files:**
- Modify: `RCP_session/presentation_outline.md`

- [ ] **Step 1: Write slides 13–16**

Append slides 13–16 to `RCP_session/presentation_outline.md`.

```markdown
## Tier 2 — Agent Pipeline Deep Dive (10 min)

### Slide 13 — Agent Pipeline Components

**Heading:** Tier 2 — Inside the AI Node

**Component diagram (6 components with descriptions):**

```
┌────────────────────────────────────────────┐
│            AgentFactory                    │
│  Creates & composes agents from config     │
│                                            │
│  ┌──────────┐  ┌───────────────┐           │
│  │AgentSpec │  │AgenticScope   │           │
│  │(config)  │  │(shared state) │           │
│  └────┬─────┘  └───────┬───────┘           │
│       │                │                   │
│  ┌────┴────────────────┴────┐              │
│  │      UntypedAgent        │              │
│  │  (LLM-backed or Java)    │              │
│  └────┬─────────────┬───────┘              │
│       │             │                      │
│  ┌────┴────┐  ┌─────┴─────┐               │
│  │Guardrails│  │  Tools    │               │
│  │(in/out) │  │ (@Tool)   │               │
│  └─────────┘  └───────────┘               │
└────────────────────────────────────────────┘
```

**Key insight:** "LLM-powered agents and pure Java logic agents coexist using the same UntypedAgent interface. Teams add AI capabilities without learning new patterns."

---

### Slide 14 — AgentSpec — Declarative Config

**Heading:** AgentSpec — Everything to Define an Agent

| Property | Purpose |
|---|---|
| `name` | Unique agent identifier. Maps to prompt lookup in database. |
| `inputs(...)` | Declares which scope keys this agent reads. Framework resolves values from AgenticScope automatically. |
| `outputKey(...)` | The scope key where this agent writes its result. Downstream agents read from this key. |
| `tools(...)` | Java objects with `@Tool`-annotated methods. LangChain4j discovers and exposes them to the LLM. |
| `inputGuardrails(...)` | Validation functions that run BEFORE the LLM call. Can block, rewrite, or pass through. |
| `outputGuardrails(...)` | Validation functions that run AFTER the LLM call. Can rewrite output, trigger retry, or reprompt. |
| `maxSequentialToolExecutions` | Maximum tool calls per LLM turn (critical for batch pagination). |
| `listener(...)` | AgentMonitor for execution observability — tracks timing, inputs, outputs, errors. |

**Callout:** "This is purely declarative. You describe WHAT the agent needs — the framework handles HOW it runs."

---

### Slide 15 — Code: AgentSpec Example

**Heading:** Defining an Agent — Real Code

**Code block (Java):**

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

**Callout:** "The name maps to the database prompt table. Model parameters, system instructions, temperature — all loaded from DB at runtime. Change the prompt without changing code."

---

### Slide 16 — Composition Patterns

**Heading:** Composing Agents — sequence, parallel, loopUntil

**Three diagrams side by side:**

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
  All read from same scope state, execute concurrently
```

**loopUntil():**
```
[Agent A] → [Agent B] → predicate?
    ↑                      │ no
    └──────────────────────┘
                           │ yes → done
  Loop until quality threshold met or max iterations
```

**Key point:** "These patterns can be nested. A sequence can contain parallel groups, which can contain sub-sequences."

---
```

- [ ] **Step 2: Write slides 17–19**

Append slides 17–19 to `RCP_session/presentation_outline.md`.

```markdown
### Slide 17 — Code: Agent Composition (CSM Pipeline)

**Heading:** 12-Agent Pipeline in ~20 Lines

**Code block (Java):**

```java
return agentFactory.sequence(Workflow.class, "extractionReview",
    // Wave 1: Extract + classify in parallel
    agentFactory.parallel("wave1",
        candidateExtractor,
        sourceClassifier
    ),
    // Wave 2-4: Normalize, dedup, classify in sequence
    nameNormalizer,
    dedupLinker,
    csmClassifier,
    // Wave 5: Enrich in parallel
    agentFactory.parallel("wave5",
        countryOverride,
        titleExtractor,
        scoringEngine
    ),
    // Wave 5m: Merge parallel outputs (pure Java agent)
    waveMerger,
    // Wave 6-7: Assemble + format
    reasonAssembler,
    outputFormatter,
    // Wave 8+: Quality refinement loop
    agentFactory.loopUntil(3,
        scope -> scope.get("score") >= 0.85,
        critic,
        refiner
    )
);
```

**Callout:** "This is the entire CSM extraction pipeline. 12 agents. Parallel execution, sequential chaining, iterative refinement — all in ~20 lines of declarative code. The framework handles scope management, guardrails, batching, monitoring, and retry."

---

### Slide 18 — The Bridge — AI Node

**Heading:** How Tier 1 Connects to Tier 2

**Three-step flow diagram:**

```
TIER 1 (Graph State)                    TIER 2 (AgenticScope)
┌──────────────┐                        ┌──────────────────┐
│ Graph State  │                        │                  │
│ {docId,      │──── 1. Read ──────────>│  AgenticScope    │
│  filePath,   │     & Seed             │  {documentText,  │
│  rawText}    │                        │   documentSource}│
│              │                        │                  │
│              │                        │  ┌────────────┐  │
│              │                        │  │ 12-Agent   │  │
│              │                        │  │ Pipeline   │  │
│              │                        │  └────────────┘  │
│              │                        │                  │
│ {docId,      │<─── 3. Write ─────────│  {extractedCSMs, │
│  filePath,   │     Back               │   score,         │
│  rawText,    │                        │   reasons}       │
│  csmResults} │                        │                  │
└──────────────┘                        └──────────────────┘
```

**Three steps:**
1. **Scope Initialization** — AI Node reads from Graph State, seeds AgenticScope with initial inputs
2. **Pipeline Execution** — Runs the full Tier 2 agent pipeline (sequence/parallel/loop)
3. **Result Extraction** — AI Node reads final output from AgenticScope, writes back to Graph State

---

### Slide 19 — Tools & BatchAccumulatorTool

**Heading:** Tools — Java Methods as LLM Capabilities

**Left side — @Tool annotation:**

```java
@Tool("Submit a batch of extracted candidates")
public String submitBatch(String jsonBatch) {
    batches.get().add(jsonBatch);
    return "Batch received. Continue with next batch.";
}
```

**Right side — BatchAccumulatorTool flow:**

```
Agent produces 200+ records (exceeds token limit)
    │
    ├─ Small output (≤40 records) → return JSON directly
    │
    └─ Large output (>40 records):
         1. BatchResetInputGuardrail resets ThreadLocal
         2. LLM calls submit_batch(first 40 records)
         3. LLM calls submit_batch(next 40 records)
         4. ... continues until all records submitted
         5. BatchMergerOutputGuardrail merges all batches
         6. → Single complete JSON result
```

**Callout:** "This solved a critical production problem. When the LLM needs to output more data than its token limit allows, it paginates automatically using this tool. The developer doesn't need to handle this — it's built into the framework."

---
```

---

### Task 4: Create Presentation Outline — Platform Features (Slides 20–25)

**Files:**
- Modify: `RCP_session/presentation_outline.md`

- [ ] **Step 1: Write slides 20–25**

Append platform features slides to `RCP_session/presentation_outline.md`.

```markdown
## Platform Features (5 min)

### Slide 20 — Built-in Enterprise Auth

**Heading:** Enterprise Authentication — Built In

**Left side — Authentication flow diagram:**

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Certificate │────>│ Azure Token │────>│ Token        │────>│ Gemini      │
│ Signing     │     │ Generation  │     │ Signing      │     │ Auth        │
│ (Bank WIF)  │     │             │     │ (JWT)        │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

**Right side — What developers see:**

```properties
nexus:
  ai:
    enabled: true
    wif_provider: /path/to/provider.json
    wif_keystore: /path/to/keystore.json
    tenant_id: ENC(...)
  google:
    project_id: db-dev-daa2-dbclm
    location: europe-west4
    chat_model_name: gemini-2.0-flash-001
    temperature: 0.7
    topk: 40
    topp: 0.95
```

**Callout:** "The entire WIF → Azure → JWT → Gemini authentication chain is abstracted away. Teams set properties. That's it. All secrets encrypted with ENC()."

**Reference:** Screenshot IMG_3956

---

### Slide 21 — Database-Driven Prompts

**Heading:** Prompts Live in the Database

**Left side — profile_messages table structure:**

| Column | Example |
|---|---|
| AGENT_NAME | NAMED_ENTITY_EXTRACTION_V2 |
| TYPE | EXTRACTION_AGENTIC |
| SYSTEM_INSTRUCTION | "Your Goal: Extract named entities..." |
| USER_MESSAGE_TEMPLATE | "Analyze the following document: {documentText}" |
| MODEL_NAME | gemini-2.0-flash-001 |
| TEMPERATURE | 0.7 |
| TOP_P | 0.95 |
| TOP_K | 40 |
| OUTPUT_TOKENS | 2048 |
| THINKING_BUDGET | 1000000 |
| RESPONSE_SCHEMA | {"type":"object", "properties":{...}} |
| PROMPT_VERSION | 1 |

**Right side — Benefits:**
- Deploy prompt changes **without code changes**
- Prompt engineers iterate **independently** from developers
- **Versioned prompts** — track what changed and when
- **A/B testing** of prompt variants possible
- Model parameters (temperature, topK, thinking budget) tunable without redeployment

**Reference:** Screenshots IMG_3957–3959

---

### Slide 22 — Observability — 3-Table Data Model

**Heading:** Full Observability — Every Decision Tracked

**Three-table flow diagram:**

```
┌──────────────────────┐
│   Workflow Table      │
│                       │
│ RUN_ID (entry point)  │
│ STATUS: FINISHED      │
│ DATA_CONTENT          │
│ STARTED_AT            │
│ COMPLETED_AT          │
└──────────┬────────────┘
           │ RUN_ID
    ┌──────┴───────┐
    ▼              ▼
┌──────────────┐ ┌──────────────────┐
│ Agent        │ │ Checkpoint       │
│ Execution    │ │ Table            │
│ Table        │ │                  │
│              │ │ CHECKPOINT_ID    │
│ EXECUTION_ID │ │ RUN_ID           │
│ RUN_ID       │ │ AGENT_NAME       │
│ AGENT_NAME   │ │ STATUS           │
│ AGENT_TYPE   │ │ INPUT_SUMMARY    │
│ STATUS       │ │ OUTPUT_SUMMARY   │
│ PROMPT_VER   │ │ TOTAL_TOKENS     │
│ MODEL_NAME   │ │ PROMPT_TOKENS    │
│ TEMPERATURE  │ │ COMPLETION_TOKENS│
│ TOKENS_IN    │ │                  │
│ TOKENS_OUT   │ │                  │
│ TOTAL_TOKENS │ │                  │
│ STARTED_AT   │ │                  │
│ COMPLETED_AT │ │                  │
│ ERROR_MSG    │ │                  │
└──────────────┘ └──────────────────┘
```

**Callout:** "Every single LLM call is recorded — what prompt was sent, what model was used, what tokens it consumed, what it returned. Compliance teams can trace exactly how every AI decision was made."

**Reference:** Screenshots IMG_3960–3964

---

### Slide 23 — Reproducibility & Debugging

**Heading:** Reproduce Any Execution. Debug Any Failure.

**Four capabilities:**

| Capability | How It Works |
|---|---|
| **Full Audit Trail** | Every agent execution recorded: inputs, outputs, model parameters, timing. Compliance teams trace every decision. |
| **Reproducibility** | Same prompt version + same model parameters + same input = same output. Temperature(0) ensures deterministic results. |
| **Debugging** | Agent returns wrong output? Examine: exact prompt sent → scope state at that point → guardrail evaluation chain → model response. |
| **Performance Monitoring** | Execution times, token counts, error rates tracked per agent. Capacity planning and cost optimization. |

**Visual:** Timeline showing a failed execution with clickable inspection points at each agent.

---

### Slide 24 — Guardrails

**Heading:** Guardrails — Deterministic Validation at Every Step

**Two tables side by side:**

**Input Guardrails (before LLM call):**
| Outcome | Method | Effect |
|---|---|---|
| **Pass** | `success()` | Input valid. Proceed to LLM call. |
| **Rewrite** | `successWithText()` | Input modified (inject headers, transform). Proceed with modified input. |
| **Block** | `fatal(reason)` | Input invalid. LLM call blocked entirely. |

**Output Guardrails (after LLM call):**
| Outcome | Method | Effect |
|---|---|---|
| **Pass** | `success()` | Output valid. Continue pipeline. |
| **Retry** | `retry(reason)` | Output invalid. Re-invoke LLM with same prompt. |
| **Halt** | `fatal(reason)` | Unrecoverable error. Halt with exception. |

**Code example:**
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

**Callout:** "Guardrails are deterministic — they don't rely on the LLM. They're reusable Spring beans shared across agents."

---

### Slide 25 — Failure & Retry — 5 Layers

**Heading:** Five Layers of Failure Handling

| Layer | Tier | Mechanism | What It Catches |
|---|---|---|---|
| **Graph Node Retry** | Tier 1 | Conditional edges + retry logic | Node failures, infrastructure errors, timeouts |
| **LLM Provider Retry** | Tier 2 | HTTP-level retry (built into client) | 429 rate limits, 500 errors, network timeouts |
| **Guardrail Retry** | Tier 2 | `reprompt()` / `retry()` | Invalid JSON, missing fields, quality violations |
| **Loop Pattern** | Tier 2 | `loopUntil(max, predicate)` | Iterative refinement until quality threshold met |
| **Batch Tool** | Tier 2 | `submit_batch()` tool | Output exceeds token limit — LLM paginates automatically |

**Callout:** "You don't implement any of this. It's all built into the framework. Your agent definition declares guardrails and limits — Nexus AI handles the rest."

---
```

---

### Task 5: Create Presentation Outline — PromptLint (Slides 26–31)

**Files:**
- Modify: `RCP_session/presentation_outline.md`

- [ ] **Step 1: Write slides 26–31**

Append PromptLint slides to `RCP_session/presentation_outline.md`.

```markdown
## PromptLint — Static Quality Analyzer (10 min)

### Slide 26 — Prompts Are Code

**Heading:** Prompts Are Code. Treat Them Like Code.

**Narrative build (staggered text):**
1. Prompts define how LLM agents behave — what they extract, classify, format, return
2. Unlike application code: **no linting, no static analysis, no automated quality gates**
3. Prompts silently degrade — someone adds vague language, removes the output schema, introduces contradictory rules
4. The LLM starts hallucinating or returning malformed output
5. Nobody can pinpoint **when** the regression happened — because nobody was testing the prompt

**Punchline (large text):**
> "PromptLint brings the discipline of static analysis to LLM prompts."

**Key stats:**
- Rule-based, deterministic — **no LLM calls**, no API keys, no latency
- Runs in **milliseconds**
- Same prompt → same score. Always. Fully deterministic.

---

### Slide 27 — All 8 Quality Dimensions

**Heading:** 8 Orthogonal Quality Dimensions

| Dimension | Code | What It Checks |
|---|---|---|
| **Clarity** | CLR | Role definition, task statement, imperative verbs, vague language detection, output format section, task-before-rules ordering |
| **Specificity** | SPC | Numbered rules, concrete examples, quantified thresholds, boundary conditions, enum constraints |
| **Groundedness** | GND | Source-grounding phrases, anti-hallucination guards, evidence requirements, citation instructions |
| **Output Contract** | OUT | JSON examples present and valid, field-level documentation, schema completeness |
| **Constraint Coverage** | CON | Edge case handling, null/empty handling, error handling, ordering rules, boundary conditions |
| **Consistency** | CST | Template variable alignment with declared inputs, contradictory instructions, terminology consistency |
| **Token Efficiency** | TKN | Prompt length vs complexity ratio, redundancy detection, filler removal |
| **Injection Resistance** | INJ | System/user boundary enforcement, input sanitization, refusal instructions, role-lock phrases |

**Footer:** Each dimension scores 0.0–1.0. Overall = weighted average based on agent type profile.

---

### Slide 28 — Agent Type Profiles

**Heading:** Weighted Scoring by Agent Type

| Profile | Top Weighted Dimensions | Use When |
|---|---|---|
| **EXTRACTION** | Groundedness (0.25), Specificity (0.15), Output Contract (0.15) | Extracting structured data from documents |
| **CLASSIFICATION** | Specificity (0.20), Constraint Coverage (0.20), Groundedness (0.15) | Categorizing inputs into defined classes |
| **FORMATTING** | Output Contract (0.30), Consistency (0.15), Constraint Coverage (0.15) | Transforming data into a specific output format |
| **REVIEW** | Groundedness (0.20), Specificity (0.15), Output Contract (0.15) | Reviewing and validating content |
| **DEFAULT** | Equal weights (0.125 each) | General-purpose agents or when unsure |

**Custom profiles supported:**
```java
var customProfile = new AgentTypeProfile("MY_AGENT", Map.of(
    "CLARITY",              0.20,
    "SPECIFICITY",          0.20,
    "GROUNDEDNESS",         0.20,
    "OUTPUT_CONTRACT",      0.20,
    "CONSTRAINT_COVERAGE",  0.10,
    "CONSISTENCY",          0.10,
    "TOKEN_EFFICIENCY",     0.00,
    "INJECTION_RESISTANCE", 0.00
));
```

---

### Slide 29 — Code: Analyzer + JUnit API

**Heading:** Test Prompts Like You Test Code

**Left side — Basic usage:**

```java
var analyzer = PromptQualityAnalyzer.create();

var prompt = PromptUnderTest.builder()
    .systemPrompt("You are a named entity extractor...")
    .userPrompt("Extract entities from: {documentText}")
    .agentType(AgentTypeProfile.EXTRACTION)
    .declaredInputs(Set.of("documentText"))
    .declaredOutputs(Set.of("entities"))
    .build();

PromptQualityReport report = analyzer.analyze(prompt);
System.out.println(renderer.renderSummary(report, 0.75));
```

**Right side — JUnit assertion API:**

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

**Callout:** "Test prompts the same way you test code. Same JUnit runner. Same CI pipeline. Same quality bar."

---

### Slide 30 — CI Integration

**Heading:** CI Integration — Fail the Build on Prompt Regression

**Pipeline diagram:**

```
[Code Change] → [Compile] → [Unit Tests] → [PromptLint] → [Integration Tests] → [Deploy]
                                               │
                                    Score < 0.75? → ❌ BUILD FAILS
                                    Score ≥ 0.75? → ✅ Continue
```

**Key points:**
- Set quality threshold (e.g., 0.75) — fail build if any prompt drops below
- Runs in **milliseconds** — no network calls, no API keys, no flaky tests
- **Fully deterministic** — same prompt always produces the same score
- Only runtime dependency: Jackson (jackson-databind) for JSON validation
- Java 17+

---

### Slide 31 — REST API

**Heading:** REST API — For Non-Java Teams

| Endpoint | Method | Description |
|---|---|---|
| `/prompt/quality/raw` | POST | Pass a raw prompt string. Returns quality report using DEFAULT profile. |
| `/prompt/quality` | POST | Pass a full PromptUnderTest (agent profile, declared inputs/outputs, system + user prompts). Returns detailed report. |

**Use cases:**
- Non-Java teams analyzing prompts via HTTP
- Integration with Confluence or documentation dashboards
- Automated quality reporting across all prompts in the organization

---
```

---

### Task 6: Create Presentation Outline — CSM Workflow & Getting Started (Slides 32–37)

**Files:**
- Modify: `RCP_session/presentation_outline.md`

- [ ] **Step 1: Write slides 32–37**

Append CSM workflow and closing slides to `RCP_session/presentation_outline.md`.

```markdown
## CSM Workflow — Proof It Works (5 min)

### Slide 32 — First Production Agentic Workflow

**Heading:** CSM Workflow — First Production AI Workflow in dbCLM

**Before / After:**

| | Before | After |
|---|---|---|
| **Process** | Analysts manually read financial and legal documents to identify Client Senior Managers | AI-powered workflow automatically reads documents, identifies CSMs, auto-answers CSM questions |
| **Effort** | Manual, time-consuming, error-prone for every document | Fully automated — triggered by event, results stored in compliance database |
| **Scale** | One analyst, one document at a time | Processes all documents as they arrive |

**Punchline:** "This isn't a proof-of-concept. This is the first production agentic workflow in the entire dbCLM business unit. Built on Nexus AI. Running in production."

---

### Slide 33 — CSM Architecture

**Heading:** CSM Workflow Architecture

**Top — Tier 1 (4 LangGraph nodes):**

```
[Document Download] → [GCS Upload] → [CSM Extraction] → [Result Storage]
     (Non-AI)           (Non-AI)         (AI Node)          (Non-AI)
```

| Node | Type | Responsibility |
|---|---|---|
| Document Download | Non-AI | Fetches KYC documents from source systems |
| GCS Upload | Non-AI | Uploads to Google Cloud Storage, extracts text |
| CSM Extraction | AI Node | 12-agent Tier 2 pipeline for person extraction and classification |
| Result Storage | Non-AI | Persists extraction results to compliance database |

**Bottom — Tier 2 (12 agents inside CSM Extraction):**

| Wave | Agent(s) | Pattern | Purpose |
|---|---|---|---|
| 1 | Candidate Extractor + Source Classifier | `parallel()` | Extract names and classify document sources simultaneously |
| 2–4 | Name Normalizer → Dedup Linker → CSM Classifier | `sequence()` | Normalize, deduplicate, classify candidates |
| 5 | Country Override + Title Extractor + Scoring Engine | `parallel()` | Enrich with country rules, titles, scores in parallel |
| 5m | Wave Merger | `UntypedAgent` (Java) | Merge parallel outputs into single enriched record per candidate |
| 6–7 | Reason Assembler → Output Formatter | `sequence()` | Assemble compliance reasons, format final output |
| 8+ | Critic → Refiner | `loopAtEnd()` | Iterative quality refinement until score ≥ 0.85 |

---

### Slide 34 — ~20 Lines of Code

**Heading:** The Entire Pipeline — ~20 Lines of Code

**Same code as Slide 17 but now with full context:**

```java
// CSM Extraction — Tier 2 Agent Pipeline
// 12 agents, parallel + sequential + loop, ~20 lines

return agentFactory.sequence(Workflow.class, "extractionReview",
    agentFactory.parallel("wave1",
        candidateExtractor, sourceClassifier),
    nameNormalizer,
    dedupLinker,
    csmClassifier,
    agentFactory.parallel("wave5",
        countryOverride, titleExtractor, scoringEngine),
    waveMerger,
    reasonAssembler,
    outputFormatter,
    agentFactory.loopUntil(3,
        scope -> scope.get("score") >= 0.85,
        critic, refiner)
);
```

**Callout:** "All execution, scope management, guardrails, batching, and monitoring — handled by the framework. You define WHAT happens. Nexus AI handles HOW."

---

## Getting Started (4 min)

### Slide 35 — 7 Steps to a New Workflow

**Heading:** Build Your Own Workflow — 7 Steps

| Step | What You Do |
|---|---|
| **1. Design the Tier 1 Graph** | Identify high-level steps. Which are AI-powered? Which are standard Java? Define the graph topology. |
| **2. Create Tier 1 Nodes** | Implement `AsyncNodeAction<YourWorkflowState>` for each non-AI node. Register them in the StateGraph. |
| **3. Define Prompts in Database** | Insert prompt records into `profile_messages` table: agent name, system instruction, model parameters, response schema. |
| **4. Create AgentSpecs** | Define an AgentSpec for each AI processing step: name, inputs, outputKey, tools, guardrails, listener. |
| **5. Compose Tier 2 Pipeline** | Use AgentFactory to compose agents: `sequence()`, `parallel()`, `loopUntil()`. |
| **6. Create the AI Node (Bridge)** | Create the Tier 1 node that bridges to Tier 2. It reads from Graph State, seeds AgenticScope, invokes the pipeline, writes results back. |
| **7. Wire the Tier 1 Graph** | Register all nodes in the StateGraph, define edges, compile. Done. |

**Footer:** No changes to core framework required. A typical 3–5 agent workflow: **1–2 days**.

---

### Slide 36 — Quick Start

**Heading:** Quick Start

**Maven dependency (Nexus AI):**
```xml
<dependency>
    <groupId>com.db.clm.kyc</groupId>
    <artifactId>nexus-ai</artifactId>
    <version>${nexus-ai.version}</version>
</dependency>
```

**Maven dependency (PromptLint):**
```xml
<dependency>
    <groupId>com.db.clm.kyc</groupId>
    <artifactId>clm-prompt-lint</artifactId>
    <version>${prompt-lint.version}</version>
    <classifier>jdk17</classifier>
</dependency>
```

**Configuration:** Set `application.properties` (auth + model config)

**Documentation:** Confluence — Agentic AI Strategy space

**Contact:** Akshay Dipta — CLM Tech

---

### Slide 37 — Thank You + Q&A

**Heading:** Thank You

**Subheading:** Questions?

**Contact:** Akshay Dipta — Senior Engineer, CLM Tech

**Links:**
- Nexus AI Confluence: [Architecture Documentation]
- PromptLint Confluence: [Static Quality Analyzer]

---
```

---

### Task 7: Write Speech Script — Opening & Platform Overview (Slides 1–8)

**Files:**
- Create: `RCP_session/speech.md`

- [ ] **Step 1: Write speech for slides 1–8**

Create `RCP_session/speech.md` with the opening and platform overview narration.

The speech should be conversational, technical, and confident. ~1200 words for this block (covering ~8 min of spoken content). Each slide section should be marked with the slide number for easy reference.

Key tone notes:
- Frame through the builder's lens — "I built this because..."
- Reference the Python LangGraph session when introducing Tier 1/2
- Use concrete numbers (18-24hrs → 1hr, 12 agents, 20 lines of code)
- Speak to both devs ("here's the code") and management ("here's why it matters")

Content for the speech opening (~8 min worth):

```markdown
# Nexus AI & PromptLint — Engineering Day Speech

> ~45 min spoken content | 37 slides
> Tone: Technical, confident, conversational. Speaking to devs, architects, and tech management.

---

## Opening — The Problem (Slides 1–4, ~3 min)

**[Slide 1 — Title]**

Good morning everyone. I'm Akshay Dipta, Senior Engineer in CLM Tech. Today I'm going to take you inside Nexus AI and PromptLint — two tools I've built that are changing how we do AI engineering across dbCLM.

**[Slide 2 — Agenda]**

Here's what we'll cover in the next 45 minutes. We'll start with the problem — why we needed to build this. Then I'll walk you through the architecture, show you real code, and demonstrate the platform features that make it all work in an enterprise setting. We'll look at PromptLint — a static quality analyzer for LLM prompts — and then I'll show you a real production case study: a 12-agent workflow running in production today. And at the end, I'll show you how to get started building your own workflows. We'll have about 15 minutes for questions at the end.

**[Slide 3 — The Pain]**

So let's start with the problem. When we began exploring AI agents in dbCLM, building a single agent took 18 to 24 hours. Every team was writing their own orchestration logic, their own retry mechanisms, their own guardrails — all from scratch. There were no quality gates for prompts. Someone could change a prompt, and the agent would start hallucinating, and nobody could tell you when the regression happened or why. There was no observability — no audit trail showing what the AI decided and why. And there was no standard way to handle enterprise authentication to the LLM providers. Every team was solving the same problems independently, and duplicating infrastructure across the division.

**[Slide 4 — What If]**

So I asked three questions. What if creating an AI agent took one hour instead of 24? What if you got observability, enterprise authentication, guardrails, and prompt quality testing — built in, for free? And what if a 12-agent pipeline — something that sounds enormously complex — could be defined in 20 lines of code?

That's what Nexus AI and PromptLint deliver. Let me show you how.

---

## Nexus AI — Platform Overview (Slides 5–8, ~5 min)

**[Slide 5 — What Nexus AI Gives You]**

Nexus AI is a complete AI engineering platform. It's not just a framework for calling LLMs — it's the full stack you need to build, run, monitor, and maintain AI workflows in production.

Let me walk you through what you get. First, a two-tier architecture that cleanly separates workflow orchestration from AI agent logic. Built-in observability with a three-table audit trail — every LLM call, every node outcome, every workflow run is recorded. Enterprise authentication that abstracts the entire bank WIF to Gemini authentication chain. Input and output guardrails that validate data before and after every LLM call — deterministically, without relying on the LLM itself. Database-driven prompts — you can change a prompt, change model parameters, even change the model, without touching code. Automatic batch scaling for when an agent produces more output than the LLM's token limit allows. And full reproducibility — given the same prompt version and the same input, you get the same output. You can debug any past execution.

The bottom line: we went from 18 to 24 hours per agent to about 1 hour. That's a 95% reduction. And this isn't a prototype — it's running in production across the dbCLM business unit.

**[Slide 6 — Architecture Goals]**

Before I show you the architecture, let me tell you what we optimized for. Six goals drove every design decision.

Reusability — core components are shared across all workflows. You're composing existing pieces, not building from scratch. Extensibility — new node types, agent types, guardrails, and tools can be added without touching the core framework. It follows the open-closed principle. Modularity — both Tier 1 nodes and Tier 2 agents are self-contained units with declared inputs and outputs. Scalability — automatic output pagination handles LLM token limits, and parallel execution at both tiers maximizes throughput. Maintainability — prompts live in the database, guardrails are reusable Spring beans, and agent configuration is fully declarative. And observability — every node execution and every agent execution is tracked, with metadata, inputs, outputs, and timings all persisted to the database for compliance.

**[Slide 7 — Two-Tier Architecture Diagram]**

Here's the high-level architecture. If you attended the Python LangGraph session, this will look familiar — but with an important difference.

Tier 1 is the workflow orchestration layer, built on LangGraph4j — the Java port of LangGraph. It defines the overall workflow as a directed graph. Nodes are processing steps, edges define the execution order. Some nodes are standard Java logic — downloading files, calling APIs, storing results. But one or more nodes are AI Nodes — and that's where Tier 2 comes in.

Tier 2 is the Nexus AI agent pipeline layer, built on LangChain4j. When an AI Node executes, it enters Tier 2. Inside, you have AgentFactory, AgentSpec, AgenticScope, guardrails, tools — everything needed to orchestrate multi-agent AI pipelines with parallel execution, sequential chaining, iterative loops, and quality enforcement.

The key insight is this: Tier 1 answers "what steps does this workflow have?" Tier 2 answers "how does this AI step work internally?" A workflow node can be as simple as a file download or as complex as a 12-agent extraction pipeline.

**[Slide 8 — Why Java-Native?]**

Now, a question I know some of you are thinking: why Java? Why not Python, which is the dominant language for AI?

When this initiative started, there was a proposal to build this in Python — a separate microservice that our Java services would call. I rejected that approach and convinced technical management to go Java-native.

Here's why. Our entire ecosystem is Spring Boot. Our teams are Java engineers. Going Python would mean a separate deployment pipeline, separate monitoring, separate expertise. With Java-native, we get direct access to Spring's dependency injection, the bank's WIF authentication libraries, our existing database infrastructure — all natively. No bridges, no adapters, no second deployment pipeline.

The result: teams use their existing Java skills, the framework integrates natively with our production infrastructure, and we deploy the same way we deploy everything else.
```

---

### Task 8: Write Speech Script — Tier 1 & Tier 2 Deep Dive (Slides 9–19)

**Files:**
- Modify: `RCP_session/speech.md`

- [ ] **Step 1: Write speech for slides 9–19**

Append the Tier 1 and Tier 2 deep dive narration to `RCP_session/speech.md`. ~2400 words covering ~18 min of spoken content.

```markdown
---

## Tier 1 — LangGraph Deep Dive (Slides 9–12, ~8 min)

**[Slide 9 — Directed Graph Model]**

Let's go deeper into each tier. Starting with Tier 1 — the workflow graph.

You know this concept from the Python LangGraph session. A workflow is a directed graph. Nodes are processing steps — in our case, each node is a Java class implementing AsyncNodeAction. Edges define the execution order — sequential, conditional, or parallel. And a typed Graph State object carries data between nodes: file paths, extracted text, processing results, metadata.

The Java version gives us one big advantage over the Python version: nodes are Spring-managed beans. That means full access to dependency injection — your repositories, your services, your configuration — all available inside every node.

**[Slide 10 — Node Types]**

There are three types of nodes. Non-AI Nodes are standard Java logic — downloading documents, uploading to cloud storage, storing results in a database, sending notifications. These are the infrastructure steps.

AI Nodes are where it gets interesting. An AI Node delegates to Tier 2 — it contains an entire Nexus AI agent pipeline. The CSM Extraction node, for example, contains a 12-agent pipeline that extracts, classifies, deduplicates, enriches, and quality-checks entities from documents.

And Decision Nodes evaluate a condition and route to different edges. For example, checking the document size to decide whether to use the small-document path or the large-document path.

**[Slide 11 — Graph State]**

The Graph State is how data flows through the workflow. It's a typed state object — each node declares what fields it reads and what fields it writes. At node boundaries, the state is immutable — nodes receive a snapshot and return updates. This makes the flow predictable and debuggable.

Here's a concrete example. The state starts with a document ID and source. After the Download node, it has a file path and raw text. After the AI Extraction node, it has extracted entities and a confidence score. After Storage, it has a completion status. Each node adds to the state without overwriting what came before.

**[Slide 12 — Code: Graph Definition]**

Here's what this looks like in code. This is a real workflow — the CSM extraction workflow.

Four nodes. Linear flow. We register each node, define the edges — start to download, download to upload, upload to extraction, extraction to storage, storage to end — and compile the graph. That's it.

The interesting part is that csm extraction AI node. It looks like just another node in the graph. But inside it, there's a full 12-agent Tier 2 pipeline. The graph doesn't need to know about that complexity — it just sees a node that takes input state and returns output state. Clean separation of concerns.

---

## Tier 2 — Agent Pipeline Deep Dive (Slides 13–19, ~10 min)

**[Slide 13 — Agent Pipeline Components]**

Now let's go inside that AI Node. This is Tier 2 — the Nexus AI agent pipeline.

Six core components. AgentFactory creates and composes agents from declarative configurations. AgentSpec is the declarative config that defines everything about an agent. AgenticScope is the shared state container — like Graph State but for agents within a single AI node. UntypedAgent is the standard interface that both LLM-backed agents and pure Java agents implement — the framework treats them identically. Guardrails provide input and output validation. And Tools are Java methods exposed to the LLM via the @Tool annotation.

The key design decision here: LLM-powered agents and pure Java logic agents use the same interface. That means you can mix AI agents with deterministic Java agents in the same pipeline, and the framework doesn't care which is which.

**[Slide 14 — AgentSpec — Declarative Config]**

Let me walk you through what goes into an AgentSpec. This is the heart of the framework — each agent is fully defined by its spec.

The name is the unique identifier — it maps directly to the prompt lookup in the database. Inputs declares which keys this agent reads from the AgenticScope — the framework resolves the values automatically. OutputKey is where this agent writes its result — downstream agents read from this key. Tools are Java objects with @Tool-annotated methods that get exposed to the LLM. InputGuardrails run before the LLM call — they can block invalid input, rewrite it, or pass it through. OutputGuardrails run after — they can retry on bad output or halt on unrecoverable errors. MaxSequentialToolExecutions controls how many tool calls the LLM can make per turn — critical for the batch pagination tool. And the listener is the AgentMonitor that tracks timing, inputs, outputs, and errors for observability.

This is purely declarative. You describe what the agent needs. The framework handles how it runs.

**[Slide 15 — Code: AgentSpec Example]**

Here's a real AgentSpec for the candidate extraction agent. The name maps to NAMED_ENTITY_EXTRACTION_V2 in the database prompt table. It reads documentText and documentSource from the scope. It writes to extractedCandidates. It uses the batch accumulator tool for handling large outputs. It has a batch reset input guardrail, a JSON schema output guardrail, and a batch merger output guardrail. Up to 50 sequential tool executions per turn. And the agent monitor listener tracks everything.

Notice what's not here — no prompt text, no model configuration, no temperature settings. All of that comes from the database at runtime. Change the prompt, change the model, change the temperature — without changing a single line of code.

**[Slide 16 — Composition Patterns]**

Now, how do you combine agents? Three composition patterns.

Sequence — agents execute one after another. Each agent reads the previous agent's output from the scope. This is your standard pipeline: extract, then normalize, then classify.

Parallel — agents execute concurrently. All of them read from the same scope state, and their results are written independently. Use this when agents are independent — extract names in parallel with classifying document sources.

LoopUntil — two agents execute in a loop until a predicate evaluates to true or you hit the maximum iterations. This is for iterative quality refinement — a critic evaluates the output, a refiner improves it, and you loop until the quality score meets your threshold.

And these can be nested. A sequence can contain parallel groups. A parallel group can contain sub-sequences. This nesting is how you build complex pipelines from simple patterns.

**[Slide 17 — Code: Agent Composition]**

And here's the payoff. This is the entire CSM extraction pipeline. 12 agents. About 20 lines of code.

Wave 1: candidate extractor and source classifier run in parallel — extracting names while simultaneously classifying document sources. Waves 2 through 4: name normalizer, dedup linker, and CSM classifier run in sequence — normalizing names, removing duplicates, and classifying each candidate. Wave 5: country override, title extractor, and scoring engine run in parallel — enriching each candidate with country rules, titles, and scores. Wave 5m: a pure Java agent that merges the parallel outputs into a single enriched record. Waves 6 and 7: reason assembler and output formatter run in sequence — assembling compliance reasons and formatting the final output. And wave 8 onward: a critic and refiner loop until the extraction score hits 0.85, with a maximum of 3 iterations.

All execution, scope management, guardrails, batching, and monitoring — handled by the framework. You define what happens. Nexus AI handles how.

**[Slide 18 — The Bridge — AI Node]**

Let me show you exactly how Tier 1 and Tier 2 connect. The AI Node is the bridge.

Step one: scope initialization. The AI Node reads the relevant fields from the Tier 1 Graph State — document text, document source — and seeds the Tier 2 AgenticScope with those values.

Step two: pipeline execution. The framework runs the full Tier 2 pipeline — all 12 agents with their sequence, parallel, and loop patterns.

Step three: result extraction. The AI Node reads the final output from the AgenticScope — the extracted CSMs, the confidence score, the compliance reasons — and writes them back to the Tier 1 Graph State. Downstream non-AI nodes can then store the results, send notifications, or trigger follow-up processes.

Clean handoff. Tier 1 doesn't know about agents. Tier 2 doesn't know about the workflow graph. The AI Node translates between the two.

**[Slide 19 — Tools & BatchAccumulatorTool]**

One more Tier 2 feature before we move on — tools and the BatchAccumulatorTool.

Tools are Java methods annotated with @Tool. The LLM sees these as callable functions. Spring singleton, ThreadLocal state for isolation. Standard LangChain4j pattern.

But the BatchAccumulatorTool solves a critical production problem. What happens when an agent needs to output 200 records, but the LLM's output token limit can only handle about 40 at a time? Without this tool, the entire call fails.

Here's how it works. The batch reset input guardrail clears the ThreadLocal state for this invocation. The LLM processes the input. If the output is small — 40 records or fewer — it returns the JSON directly, and the tool is never called. But if the output is large, the LLM calls submit_batch with the first 40 records, then the next 40, and so on — it paginates automatically. After all batches are submitted, the batch merger output guardrail detects that the tool was used, reads all accumulated batches, merges them into a single JSON result, and replaces the output.

The developer doesn't need to handle this. Declare the tool and guardrails in your AgentSpec, and the framework handles output scaling transparently.
```

---

### Task 9: Write Speech Script — Platform Features (Slides 20–25)

**Files:**
- Modify: `RCP_session/speech.md`

- [ ] **Step 1: Write speech for slides 20–25**

Append platform features narration. ~800 words covering ~5 min.

```markdown
---

## Platform Features (Slides 20–25, ~5 min)

**[Slide 20 — Built-in Enterprise Auth]**

Let's talk about the platform features that make this work in an enterprise setting. Starting with authentication.

Connecting to Gemini in the bank isn't just an API key. It's a multi-step process: you sign a certificate using the bank's Workload Identity Federation procedure, generate a token from Azure, sign that token to create a JWT, and use that JWT to authenticate with Gemini.

Nexus AI abstracts all of this. What developers see is an application.properties file. Set your WIF provider path, your keystore path, your tenant ID. Set your Google project, location, model name, temperature. All secrets encrypted with ENC. That's it. The framework handles the entire authentication chain internally.

No team should have to implement this themselves. It's built into the platform.

**[Slide 21 — Database-Driven Prompts]**

This is one of my favourite features. Prompts live in the database, not in code.

The profile_messages table stores everything about each agent's prompt: the agent name, the system instruction, the user message template, the model name, temperature, top P, top K, output tokens, thinking budget, and the response schema.

Why does this matter? Three reasons. First, you can deploy prompt changes without code changes. No pull request, no build, no deployment. Update the row in the database, and the next execution picks up the new prompt. Second, prompt engineers can iterate independently from developers. They don't need to understand the code — they work with the prompt in the database. And third, prompts are versioned. You know exactly which prompt version was used for every execution, and you can roll back if something goes wrong.

This is what the actual table looks like — you can see the agent names, system instructions, model parameters, everything configured per agent.

**[Slide 22 — Observability — 3-Table Data Model]**

Observability. This is critical for compliance and debugging.

Every workflow execution creates three interconnected records. The Workflow table creates a RUN_ID — this is the entry point. It tracks the overall status, timestamps, what triggered the workflow.

The Agent Execution table records every single LLM call within that run. For each agent: the execution ID, agent name, agent type, status, what prompt version was used, what model, what temperature, how many tokens went in, how many came out, the total token count, when it started, when it completed, and any error messages.

The Checkpoint table records every node outcome — what went in, what came out, token counts broken down by prompt tokens and completion tokens.

The flow is: Workflow creates the RUN_ID, Agent Executions and Checkpoints reference that RUN_ID. You can trace any workflow from trigger to final output, through every AI decision along the way. Compliance teams can audit exactly how every decision was made.

**[Slide 23 — Reproducibility & Debugging]**

Because we record everything, we get two powerful capabilities. Reproducibility — given the same prompt version, the same model parameters, and the same input, you get the same output. We use temperature zero for deterministic results.

And debugging. When an agent produces the wrong output, you don't guess. You look up the execution in the Agent Execution table, examine the exact prompt that was sent, the scope state at that point, the guardrail evaluation chain, and the model's response. You know exactly what happened and why.

We also track execution times and token counts per agent, which gives us performance monitoring for capacity planning and cost optimization.

**[Slide 24 — Guardrails]**

Guardrails provide deterministic validation at every step — independent of the LLM.

Input guardrails run before the LLM call. Three outcomes: pass — the input is valid, proceed. Rewrite — modify the input, for example injecting guardrail headers, then proceed with the modified version. Or block — the input is invalid, and the LLM call is blocked entirely.

Output guardrails run after the LLM call. Again three outcomes: pass — the output is valid. Retry — the output is invalid, re-invoke the LLM with the same prompt. Or halt — unrecoverable error, stop the pipeline.

These are reusable Spring beans. Write a JSON validation guardrail once, use it across every agent. The framework handles the retry loop — you just define the validation logic.

**[Slide 25 — Failure & Retry — 5 Layers]**

Finally, failure handling. The framework has five layers of retry and recovery.

At Tier 1, graph node retry uses conditional edges and retry logic to handle node-level failures, infrastructure errors, and timeouts. At Tier 2, the LLM provider's built-in HTTP retry handles rate limits, server errors, and network timeouts. Guardrail retry re-invokes the LLM when the output doesn't validate — invalid JSON, missing fields, quality violations. The loop pattern iterates until a quality threshold is met. And the batch tool handles output token limits by paginating automatically.

You don't implement any of this. It's all built into the framework. Your agent definition declares guardrails and limits — Nexus AI handles the rest.
```

---

### Task 10: Write Speech Script — PromptLint, CSM, & Closing (Slides 26–37)

**Files:**
- Modify: `RCP_session/speech.md`

- [ ] **Step 1: Write speech for slides 26–37**

Append PromptLint, CSM workflow, Getting Started, and closing narration. ~1800 words covering ~19 min.

```markdown
---

## PromptLint (Slides 26–31, ~10 min)

**[Slide 26 — Prompts Are Code]**

Now let's switch gears to PromptLint. And I want to start with a fundamental question: what happens when a prompt goes bad?

Prompts are code. They define how LLM agents behave — what they extract, how they classify, what format they return. But unlike application code, prompts have no linting. No static analysis. No automated quality gates. In practice, prompts silently degrade over time. Someone adds vague language. Someone removes the output schema. Someone introduces contradictory rules. The LLM starts hallucinating or returning malformed output. And nobody can pinpoint when the regression happened — because nobody was testing the prompt.

PromptLint changes that. It brings the discipline of static analysis to LLM prompts. Rule-based, deterministic analysis — no LLM calls, no API keys, no latency. It runs in milliseconds. And it's fully deterministic: the same prompt always produces the same score.

**[Slide 27 — All 8 Quality Dimensions]**

PromptLint evaluates prompts across eight independent quality dimensions.

Clarity checks whether the prompt has a clear role definition, a task statement, uses imperative verbs, and avoids vague language. Specificity looks for numbered rules, concrete examples, quantified thresholds, and boundary conditions. Groundedness checks for source-grounding phrases, anti-hallucination guards, and evidence requirements. Output Contract checks whether JSON examples are present and valid, with field-level documentation and schema completeness.

Constraint Coverage looks at edge case handling — what happens with null values, empty inputs, error conditions. Consistency checks that template variables align with declared inputs and that instructions don't contradict each other. Token Efficiency analyzes the prompt length versus complexity ratio and detects redundancy. And Injection Resistance checks for system/user boundary enforcement, input sanitization, and refusal instructions.

Each dimension produces a score from 0 to 1. The overall score is a weighted average — and the weights depend on the type of agent.

**[Slide 28 — Agent Type Profiles]**

That's where agent type profiles come in. Different agent types have different quality priorities.

An extraction agent — one that pulls structured data from documents — needs strong groundedness and output contracts. So the EXTRACTION profile weights groundedness at 0.25 and output contract at 0.15. A classification agent needs precise rules, so the CLASSIFICATION profile weights specificity and constraint coverage highest. A formatting agent's most critical dimension is the output contract — weighted at 0.30.

We provide five built-in profiles: extraction, classification, formatting, review, and a default with equal weights. And you can define custom profiles if your agent type doesn't fit the built-in ones — just specify the dimension weights as a map.

**[Slide 29 — Code: Analyzer + JUnit API]**

Let me show you how simple it is to use.

On the left: basic usage. Create the analyzer — one line. Build a PromptUnderTest with your system prompt, user prompt, agent type, declared inputs and outputs. Run the analysis. Get the report. Print a summary with your quality threshold. That's it.

On the right: the JUnit assertion API. This is where it gets powerful. You write a test — a standard JUnit test — that asserts your prompt has an overall score above 0.75, that groundedness is above 0.80, that output contract is above 0.70, and that there are no critical-severity findings.

Test prompts the same way you test code. Same JUnit runner. Same CI pipeline. Same quality bar.

**[Slide 30 — CI Integration]**

And because it's a JUnit test, it slots right into your CI pipeline. After compilation and unit tests, PromptLint runs. If any prompt drops below your quality threshold — build fails. Red. Fix the prompt before it reaches production.

The key properties that make this practical for CI: it runs in milliseconds — no network calls, no API keys, no flaky tests. It's fully deterministic — no randomness, no model variance. The same prompt always produces the same score. And the only runtime dependency is Jackson for JSON validation. That's it.

**[Slide 31 — REST API]**

For teams that don't use Java, PromptLint also exposes two REST endpoints. A simple analysis endpoint — post a raw prompt string, get a quality report using the default profile. And an advanced endpoint — post a full PromptUnderTest with agent profile, declared inputs and outputs, and both system and user prompts.

This enables integration with Confluence, quality dashboards, or any HTTP client. Any team, any language, can analyze their prompts.

---

## CSM Workflow — Proof It Works (Slides 32–34, ~5 min)

**[Slide 32 — First Production Agentic Workflow]**

So let me bring this all together with a real production case study. The CSM workflow — the first production agentic workflow in the entire dbCLM business unit.

Before Nexus AI: analysts manually read financial and legal documents to identify Client Senior Managers for KYC compliance. Document by document. Time-consuming. Error-prone.

After: an AI-powered workflow automatically reads documents, identifies CSMs, classifies them, and auto-answers CSM questions. Triggered by events, results stored in the compliance database. Fully automated.

This isn't a proof of concept. This is production. Running today.

**[Slide 33 — CSM Architecture]**

Here's the architecture. At Tier 1, four LangGraph nodes. Document Download fetches the KYC documents. GCS Upload pushes them to Google Cloud Storage and extracts the text. CSM Extraction is the AI Node — it contains the entire 12-agent Tier 2 pipeline. And Result Storage persists the extraction results to the compliance database.

Inside that CSM Extraction node — the Tier 2 pipeline. Wave 1: candidate extractor and source classifier run in parallel — extracting names while classifying document sources. Waves 2 through 4: normalize names, remove duplicates, classify candidates — in sequence. Wave 5: country override, title extractor, and scoring engine run in parallel — enriching candidates. Wave 5m: a pure Java agent merges the parallel outputs. Waves 6 and 7: assemble compliance reasons and format the final output. And wave 8 onward: a critic-refiner loop that iterates until the extraction quality score hits 0.85.

12 agents. A mix of LLM-powered and pure Java. Parallel, sequential, and iterative patterns. All orchestrated by Nexus AI.

**[Slide 34 — ~20 Lines of Code]**

And here's the entire pipeline definition. About 20 lines of code. Every agent is already configured via its AgentSpec and its database prompt. This code just composes them — parallel here, sequence there, loop at the end.

All execution, scope management, guardrails, batching, monitoring, retry — handled by the framework. You define what happens. Nexus AI handles how.

---

## Getting Started (Slides 35–36, ~4 min)

**[Slide 35 — 7 Steps to a New Workflow]**

If you want to build your own workflow, here are the seven steps. And I want to emphasize — none of these require changes to the core framework.

Step one: design your Tier 1 graph. What are the high-level steps? Which are AI-powered, which are standard Java? Define the topology.

Step two: create your Tier 1 nodes. Implement AsyncNodeAction for each non-AI node — these are your file downloads, API calls, storage operations.

Step three: define your agent prompts in the database. Insert records into the profile_messages table with the agent name, system instruction, model parameters, and response schema.

Step four: create your AgentSpecs. Declarative config for each AI agent — name, inputs, output key, tools, guardrails, listener.

Step five: compose your Tier 2 pipeline using AgentFactory. Use sequence, parallel, loopUntil — however your agents need to interact.

Step six: create the AI Node bridge. It reads from Graph State, seeds the AgenticScope, invokes the pipeline, and writes results back.

Step seven: wire the Tier 1 graph. Register all nodes, define edges, compile. Done.

A typical workflow with 3 to 5 agents can be built in 1 to 2 days. Half a day for prompts and AgentSpecs, half a day for Tier 2 composition, and half a day for Tier 1 graph wiring and testing.

**[Slide 36 — Quick Start]**

To get started, add the Maven dependencies for Nexus AI and PromptLint. Configure your application.properties with the authentication and model settings. The documentation is on Confluence in the Agentic AI Strategy space. And if you have questions or want help building your first workflow, reach out to me directly.

---

## Closing (Slide 37, ~30 sec)

**[Slide 37 — Thank You]**

That's Nexus AI and PromptLint. A complete AI engineering platform — from workflow orchestration to agent pipelines, from enterprise authentication to prompt quality gates. Built in Java, running in production, available for your team to adopt.

Thank you. I'm happy to take questions.
```

---

### Task 11: Review & Finalize Both Deliverables

**Files:**
- Review: `RCP_session/presentation_outline.md`
- Review: `RCP_session/speech.md`

- [ ] **Step 1: Cross-check speech against presentation outline**

Verify every slide in the presentation outline has a corresponding speech section and vice versa. Check that:
- Slide numbers match between both files
- All code snippets referenced in the speech appear in the outline
- All tables and diagrams referenced in the speech appear in the outline
- Time allocations are consistent

- [ ] **Step 2: Word count check on speech**

Run: `wc -w RCP_session/speech.md`

Expected: ~5400–6000 words (targeting ~130 words per minute × 45 minutes). If significantly over or under, adjust.

- [ ] **Step 3: Verify spec coverage**

Check every section of the design spec is covered:
- [ ] Opening (slides 1–4): problem statement, vision
- [ ] Platform Overview (slides 5–8): features, goals, architecture, Java-native
- [ ] Tier 1 (slides 9–12): graph model, node types, state, code
- [ ] Tier 2 (slides 13–19): components, AgentSpec, code, composition, bridge, tools
- [ ] Platform Features (slides 20–25): auth, DB prompts, observability, reproducibility, guardrails, retry
- [ ] PromptLint (slides 26–31): philosophy, dimensions, profiles, code, CI, REST API
- [ ] CSM Workflow (slides 32–34): before/after, architecture, code
- [ ] Getting Started (slides 35–37): 7 steps, quick start, closing

- [ ] **Step 4: Final read-through for tone**

Check that the speech:
- Frames through the Nexus AI lens (not re-teaching LangGraph/LangChain basics)
- References the Python session where appropriate
- Uses concrete numbers throughout
- Speaks to both devs and management
- Is conversational but confident
