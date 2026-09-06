# Nexus AI & PromptLint — Engineering Day Session Design

## Session Overview
- **Title:** Nexus AI & PromptLint — AI Engineering at dbCLM
- **Duration:** 1 hour (45 min content + 15 min Q&A)
- **Forum:** Deutsche Bank Engineering Day
- **Presenter:** Akshay Dipta
- **Format:** Slides + speech only (no live demo)
- **Audience:** Developers, testers, architects, tech management leaders
- **Prior context:** Audience already attended a Python LangChain/LangGraph session — no need to teach graph/agent basics from scratch

## Session Goals
1. **Knowledge sharing** — Deep-dive into Nexus AI architecture, platform features, and PromptLint
2. **Drive adoption** — Show teams how to onboard and build their own workflows
3. Frame LangGraph4j/LangChain4j through the Nexus AI lens — what Nexus AI adds on top, not re-teaching the underlying frameworks

## Approach: "The Builder's Journey" (Narrative-driven)
Problem → Solution → Architecture → Code → Impact → Adopt it.

## Time Allocation

| Block | Time | Slides |
|---|---|---|
| Opening — The Problem | 3 min | 3–4 |
| Nexus AI — Platform Overview | 5 min | 5–8 |
| Tier 1 — LangGraph Deep Dive | 8 min | 9–12 |
| Tier 2 — Agent Pipeline Deep Dive | 10 min | 13–19 |
| Platform Features | 5 min | 20–25 |
| PromptLint | 10 min | 26–31 |
| CSM Workflow — Proof It Works | 5 min | 32–34 |
| Getting Started | 4 min | 35–36 |
| Thank You + Q&A | ~15 min | 37 |

## Slide-by-Slide Spec

### Opening — The Problem (3 min)

**Slide 1 — Title**
"Nexus AI & PromptLint — AI Engineering at dbCLM" + presenter name, date, Engineering Day branding.

**Slide 2 — Agenda**
The 8 content blocks with time indicators. Sets expectations for the audience.

**Slide 3 — The Pain**
Before state:
- 18-24 hours to build a single AI agent
- No quality gates for prompts
- No standardisation — every team reimplements orchestration, retry, guardrails
- Duplicated infrastructure across teams
- No observability or audit trail for AI decisions
- No enterprise authentication abstraction

**Slide 4 — What If**
Vision statement:
- What if creating an AI agent took 1 hour instead of 24?
- What if you got observability, enterprise auth, guardrails, and prompt quality testing for free?
- What if a 12-agent pipeline could be defined in 20 lines of code?

### Nexus AI — Platform Overview (5 min)

**Slide 5 — What Nexus AI Gives You**
High-level feature list (not deep-dive yet):
- Two-tier architecture (workflow + agent orchestration)
- Built-in observability with 3-table audit trail
- Enterprise authentication (WIF → Azure → Gemini)
- Input/output guardrails
- Database-driven prompts (deploy without code changes)
- Automatic batch scaling (BatchAccumulatorTool)
- Full reproducibility and debugging support

**Slide 6 — Architecture Goals**
Table with 6 goals from the Confluence doc:
| Goal | Description |
|---|---|
| Reusability | Core components shared across all workflows. New workflows compose existing pieces. |
| Extensibility | New node types, agent types, guardrails, tools added without modifying core. Plugin-based / open-closed principle. |
| Modularity | Tier 1 nodes and Tier 2 agents are self-contained units with declared inputs/outputs. |
| Scalability | Automatic output pagination handles LLM token limits. Parallel execution at both tiers. |
| Maintainability | Prompts in database. Guardrails are reusable Spring beans. Agent config is declarative via AgentSpec. |
| Observability | Every node and agent execution tracked. Metadata, inputs, outputs, timings persisted to database. Full audit trail. |

**Slide 7 — Two-Tier Architecture Diagram**
Visual diagram:
- Tier 1 (LangGraph4j) on top — workflow orchestration layer
- Tier 2 (Nexus AI / LangChain4j) below — agent pipeline layer
- AI Node as the bridge between the two
- Reference: "You've seen LangGraph in the Python session — this is the Java-native equivalent, with Nexus AI on top"

**Slide 8 — Why Java-Native?**
- Rejected Python-based solution proposed by others
- Convinced technical management to go Java-native
- Reasoning: existing Spring Boot ecosystem, team Java expertise, production readiness, enterprise integration (DB auth, Spring beans, dependency injection)

### Tier 1 — LangGraph Deep Dive (8 min)

Frame as: "You know the graph concept from the Python session. Here's how it works in Java, and what Nexus AI adds."

**Slide 9 — Directed Graph Model**
- Nodes = processing steps (Java classes implementing AsyncNodeAction)
- Edges = execution order (sequential, conditional, parallel)
- Graph State = typed state object carrying data between nodes
- Visual: simple graph diagram with 3-4 nodes

**Slide 10 — Node Types**
Table with examples:
| Node Type | Description | Example |
|---|---|---|
| Non-AI Node | Standard Java logic — file I/O, API calls, data transformation, routing | Document Download, GCS Upload, Result Storage |
| AI Node | Delegates to Tier 2 — contains a full Nexus AI agent pipeline | CSM Extraction (12-agent pipeline), document classification |
| Decision Node | Evaluates condition, routes to different edges | Document size check → small doc vs large doc path |

**Slide 11 — Graph State**
- Typed state object — each node reads what it needs and writes what it produces
- Immutable at node boundaries — nodes receive a snapshot and return updates
- Spring-managed beans with full access to dependency injection

**Slide 12 — Code: Graph Definition**
Actual code snippet showing a real workflow graph wiring — registering nodes, defining edges, compiling the graph.

### Tier 2 — Agent Pipeline Deep Dive (10 min)

**Slide 13 — Agent Pipeline Components**
Component diagram showing:
- AgentFactory — creates/composes agents from declarative config
- AgentSpec — declarative config for each agent
- AgenticScope — shared state container within AI node
- UntypedAgent — standard interface for LLM-backed and pure Java agents
- Guardrails — input/output validation
- Tools — Java methods exposed to LLM via @Tool annotation

**Slide 14 — AgentSpec — Declarative Config**
All properties table:
| Property | Purpose |
|---|---|
| name | Unique agent identifier. Maps to prompt lookup in database. |
| inputs(...) | Declares which scope keys this agent reads. Framework resolves automatically from AgenticScope. |
| outputKey(...) | The scope key where this agent writes its result. Downstream agents read from this key. |
| tools(...) | Java objects with @Tool-annotated methods. LangChain4j discovers and exposes them to the LLM. |
| inputGuardrails(...) | Validation functions that run BEFORE the LLM call. Can block, rewrite, or pass through. |
| outputGuardrails(...) | Validation functions that run AFTER the LLM call. Can rewrite output, trigger retry, or reprompt. |
| maxSequentialToolExecutions | Maximum tool calls per LLM turn (critical for batch pagination). |
| listener(...) | AgentMonitor for execution observability — tracks timing, inputs, outputs, errors. |

**Slide 15 — Code: AgentSpec Example**
Real AgentSpec code snippet showing a fully configured agent.

**Slide 16 — Composition Patterns**
Diagrams for each pattern:
- `sequence(outputKey, agents...)` — agents execute one after another, each reads previous agent's output
- `parallel(outputKey, agents...)` — agents execute concurrently, all read from same scope state
- `loopUntil(max, predicate, agentA, agentB)` — loop until predicate true or max iterations
- These can be nested: a sequence can contain parallel groups, which can contain sub-sequences

**Slide 17 — Code: Agent Composition**
Code showing ~20 lines defining the CSM 12-agent pipeline using AgentFactory.sequence() with nested parallel() and loopAtEnd().

**Slide 18 — The Bridge — AI Node**
How Tier 1 connects to Tier 2:
1. AI Node reads from Graph State → seeds AgenticScope with initial inputs
2. Runs the Tier 2 agent pipeline (sequence/parallel/loop)
3. Reads final output from AgenticScope → writes back to Graph State for downstream Tier 1 nodes

**Slide 19 — Tools & BatchAccumulatorTool**
- Tools: Java methods with @Tool annotation exposed to the LLM. Spring singleton with ThreadLocal state.
- BatchAccumulatorTool: Solves critical scaling problem when agent output exceeds LLM output token limit (e.g., 200+ records).
  1. BatchResetInputGuardrail resets ThreadLocal state
  2. LLM processes input — if small (≤40 records), returns JSON directly
  3. If large (>40), LLM calls submit_batch(first 40 records), continues for subsequent batches
  4. BatchMergerOutputGuardrail detects batch tool usage, merges all batches into single JSON result
- Code snippet showing @Tool annotation

### Platform Features (5 min)

**Slide 20 — Built-in Enterprise Auth**
WIF authentication flow diagram:
1. Certificate signing (standard bank WIF procedure)
2. Azure token generation
3. Token signing
4. Signed JWT used for Gemini authentication

Developer experience: teams just configure `application.properties`:
- `nexus.ai.wif_provider`, `nexus.ai.wif_keystore`, `nexus.ai.tenant_id`
- `nexus.google.project_id`, `nexus.google.chat_model_name`, `nexus.google.temperature`, etc.
- All secrets encrypted with ENC()
- Reference screenshot: IMG_3956

**Slide 21 — Database-Driven Prompts**
PromptStore system:
- `profile_messages` table stores all agent prompts
- Per-agent: name, type (EXTRACTION_AGENTIC), system instruction, user message template
- Model parameters in DB: model name, temperature, topP, topK, output tokens, thinking budget, response schema
- Prompt versions — versioned prompts for each agent
- Deploy prompt changes without code changes. Prompt engineers iterate independently from developers.
- A/B testing of prompt variants possible
- Reference screenshots: IMG_3957–3959

**Slide 22 — Observability — 3-Table Data Model**
Three interconnected tables forming the audit trail:

1. **Workflow table** (IMG_3964)
   - Creates RUN_ID for each workflow execution
   - Tracks overall status (FINISHED, CHECK), data content, timestamps
   - Top-level entry point

2. **Agent Execution table** (IMG_3960–3962)
   - EXECUTION_ID, RUN_ID, AGENT_NAME, AGENT_TYPE
   - STATUS, INPUT_SUMMARY, OUTPUT_SUMMARY
   - PROMPT_VERSION, MODEL_NAME, TEMPERATURE
   - TOKENS_IN, TOKENS_OUT, TOTAL_TOKENS
   - STARTED_AT, COMPLETED_AT, ERROR_MESSAGE

3. **Checkpoint table** (IMG_3963)
   - CHECKPOINT_ID, RUN_ID, AGENT_NAME, STATUS
   - INPUT_SUMMARY, OUTPUT_SUMMARY
   - total_tokens, total_prompt_tokens, total_completion_tokens

Flow: Workflow → Agent Executions → Checkpoints. Full compliance traceability.

**Slide 23 — Reproducibility & Debugging**
- Full audit trail: every agent execution recorded with inputs, outputs, model params, timing
- Reproducibility: same prompt version + model params + input = same output. Temperature(0) for deterministic results.
- Debugging: when agent produces wrong output, engineers examine exact prompt sent, scope state at that point, guardrail evaluation chain
- Performance monitoring: execution times, token counts, error rates for capacity planning

**Slide 24 — Guardrails**
Input Guardrails:
| Outcome | Method | Effect |
|---|---|---|
| Pass | success() | Input valid. Proceed to LLM call. |
| Rewrite | successWithText() | Input modified (e.g., inject guardrail headers). Proceed with modified input. |
| Block | fatal(reason) | Input invalid. LLM call blocked entirely. |

Output Guardrails:
| Outcome | Method | Effect |
|---|---|---|
| Pass | success() | Output valid. |
| Retry | retry(reason) | Output invalid. Re-invoke LLM with same prompt. |
| Halt | fatal(reason) | Unrecoverable error. Halt with exception. |

Code snippets for both.

**Slide 25 — Failure & Retry — 5 Layers**
| Layer | Tier | Mechanism | Handles |
|---|---|---|---|
| Graph Node Retry | Tier 1 | LangGraph4j conditional edges + retry logic | Node-level failures, infra errors, timeout |
| LLM Provider | Tier 2 | HTTP-level retry (built into LLM client) | 429 rate limits, 500 errors, network timeouts |
| Input Guardrails | Tier 2 | reprompt()/retry() | Invalid JSON, missing fields, quality violations |
| Loop Pattern | Tier 2 | loopUntil(max, predicate) | Iterative refinement until quality threshold met |
| Batch Tool | Tier 2 | submit_batch() tool | Output token limit exceeded — LLM paginates automatically |

### PromptLint (10 min)

**Slide 26 — Prompts Are Code**
Philosophy:
- Prompts define how LLM agents behave, what they extract, what format they return
- Unlike application code: no linting, no static analysis, no automated quality gates
- Prompts silently degrade — someone adds vague language, removes output schema, introduces contradictory rules
- LLM starts hallucinating, nobody can pinpoint when the regression happened
- PromptLint brings static analysis discipline to LLM prompts

**Slide 27 — All 8 Quality Dimensions**
| Dimension | Code | What it Checks |
|---|---|---|
| Clarity | CLR | Role definition, task statement, imperative verbs, vague language detection, output format section, task-before-rules ordering |
| Specificity | SPC | Numbered rules, concrete examples, quantified thresholds, boundary conditions, enum constraints |
| Groundedness | GND | Source-grounding phrases, anti-hallucination guards, evidence requirements, citation instructions |
| Output Contract | OUT | JSON examples present and valid, field-level documentation, schema completeness |
| Constraint Coverage | CON | Edge case handling, null/empty handling, error handling, ordering rules, boundary conditions |
| Consistency | CST | Template variable alignment with declared inputs, contradictory instructions, terminology consistency |
| Token Efficiency | TKN | Prompt length vs complexity ratio, redundancy detection, filler removal |
| Injection Resistance | INJ | System/user boundary enforcement, input sanitization, refusal instructions, role-lock phrases |

Each dimension: score 0.0–1.0. Overall = weighted average based on agent type profile.

**Slide 28 — Agent Type Profiles**
| Profile | Top Weighted Dimensions | Use When |
|---|---|---|
| EXTRACTION | Groundedness (0.25), Specificity (0.15), Output Contract (0.15) | Extracting structured data from documents |
| CLASSIFICATION | Specificity (0.20), Constraint Coverage (0.20), Groundedness (0.15) | Categorizing inputs into defined classes |
| FORMATTING | Output Contract (0.30), Consistency (0.15), Constraint Coverage (0.15) | Transforming data into specific output format |
| REVIEW | Groundedness (0.20), Specificity (0.15), Output Contract (0.15) | Reviewing and validating content |
| DEFAULT | Equal weights (0.125 each) | General-purpose or when unsure |

Custom profiles supported — code snippet showing custom weight definition.

**Slide 29 — Code: Analyzer + JUnit API**
Two code snippets:
1. Basic usage: create PromptQualityAnalyzer, build PromptUnderTest, run analysis, get PromptQualityReport
2. JUnit: PromptQualityAssert fluent API — test prompts the same way you test code

**Slide 30 — CI Integration**
- Set quality threshold (e.g., 0.75)
- Run on every commit
- Fail the build on prompt regressions
- Runs in milliseconds — no network calls, no API keys, no flaky tests
- Fully deterministic: same prompt always produces same score
- Only runtime dependency: Jackson (jackson-databind) for JSON validation

**Slide 31 — REST API**
Two endpoints for non-Java teams:
| Endpoint | Method | Description |
|---|---|---|
| `/prompt/quality/raw` | POST | Simple analysis — pass raw prompt string, get report using DEFAULT profile |
| `/prompt/quality` | POST | Advanced analysis — pass PromptUnderTest with agent profile, declared inputs/outputs, system + user prompts |

Enables integration with Confluence, dashboards, or any HTTP client.

### CSM Workflow — Proof It Works (5 min)

**Slide 32 — First Production Agentic Workflow**
- First ever agentic workflow in the entire dbCLM business unit
- Before: analysts manually read documents to find and identify Client Senior Managers
- After: AI-powered workflow automatically reads documents, identifies CSMs, auto-answers CSM questions
- Proves Nexus AI works in production — not just a framework, a real business solution

**Slide 33 — CSM Architecture**
Tier 1 — 4 LangGraph Nodes:
| Node | Type | Responsibility |
|---|---|---|
| Document Download | Non-AI | Fetches KYC documents from source systems |
| GCS Upload | Non-AI | Uploads documents to Google Cloud Storage, extracts text |
| CSM Extraction | AI Node | 12-agent Tier 2 pipeline for person extraction and classification |
| Result Storage | Non-AI | Persists extraction results to the compliance database |

Tier 2 — 12-Agent Pipeline (inside CSM Extraction Node):
| Wave | Agent(s) | Pattern | Purpose |
|---|---|---|---|
| 1 | Candidate Extractor + Source Classifier | parallel() | Extract names and classify document sources simultaneously |
| 2-4 | Name Normalizer + Dedup Linker + CSM Classifier | sequence() | Normalize, deduplicate, and classify candidates |
| 5 | Country Override + Title Extractor + Scoring Engine | parallel() | Enrich with country rules, titles, and scores in parallel |
| 5m | WaveS Merger | UntypedAgent (Java) | Merge parallel outputs into single enriched record per candidate |
| 6-7 | Reason Assembler + Output Formatter | sequence() | Assemble compliance reasons and format final output |
| 8+ | Critic + Refiner | loopAtEnd() | Iterative quality refinement until extraction score ≥ 0.85 |

**Slide 34 — ~20 Lines of Code**
Show the actual workflow definition code. The entire 12-agent pipeline defined in ~20 lines of declarative configuration. All execution, scope management, guardrails, batching, and monitoring handled by the framework.

### Getting Started (4 min)

**Slide 35 — 7 Steps to a New Workflow**
1. Design the Tier 1 Graph — identify high-level steps, which are AI-powered vs standard Java
2. Create Tier 1 Nodes — implement AsyncNodeAction for each non-AI node
3. Define Agent Prompts in Database — insert into PromptStore (profile_messages table)
4. Create AgentSpecs — declarative config for each AI processing step
5. Compose the Tier 2 Pipeline — use AgentFactory (sequence/parallel/loopUntil)
6. Create the AI Node (Bridge) — reads from Graph State, seeds AgenticScope, invokes pipeline, writes back
7. Wire the Tier 1 Graph — register all nodes, define edges, compile

No changes to core framework required. A typical 3-5 agent workflow built in 1-2 days.

**Slide 36 — Quick Start**
- Maven dependency for Nexus AI
- Maven dependency for PromptLint
- `application.properties` config (auth, model, project)
- PromptLint setup (analyzer + CI threshold)
- Where to find documentation (Confluence links)
- Who to contact (Akshay Dipta)

**Slide 37 — Thank You + Q&A**
- Contact information
- Open floor for questions

## Speech Design Notes
- ~45 min of spoken content across 37 slides
- Narrative arc: Problem → Vision → Architecture → Deep Dive → Platform Features → Quality → Proof → Adopt
- Frame LangGraph/LangChain through Nexus AI lens — audience already knows the Python version
- Code snippets on slides should be real, not pseudocode
- Reference actual DB screenshots on observability/prompt slides for credibility
- Tone: technical but accessible — architects and management are in the room alongside devs

## Deliverables
- `RCP_session/speech.md` — full speech script (~45 min spoken)
- `RCP_session/presentation_outline.md` — detailed slide-by-slide content guide for PPT creation

## Key Decisions
- No live demo — slides + speech only
- Audience already knows LangChain/LangGraph from Python session — don't re-teach basics
- Include "How to Get Started" section to drive adoption
- Reference actual DB table screenshots for observability credibility
- CSM workflow shown as full 12-agent production example, not a toy demo
