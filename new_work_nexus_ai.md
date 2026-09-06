# New Work — Nexus AI: Agentic Workflow Framework for dbCLM

## Overview
A reusable, AI-driven workflow framework designed to orchestrate complex multi-step business processes. Combines standard Java logic with AI-powered agents in a single, declarative pipeline. Led end-to-end — all initial research, POC, design and development driven by Akshay.

## Business Impact
- **Before:** Creating an AI agent took 18-24 hours
- **After:** An agent can be created in 1 hour using Nexus AI
- **95% reduction** in agent development time
- Business unit level initiative — framework for all of dbCLM, not just one team
- Projects as AI adoption and new innovation for the division

## Architecture — Two-Tier Design

### Tier 1 — LangGraph (Workflow Graph)
- Workflow defined as a **directed graph**
- **Nodes** = processing steps (Java classes implementing AsyncNodeAction)
- **Edges** = execution order (sequential, conditional, parallel)
- **Graph State** = carries data between nodes (file paths, processing results, metadata)
- Node types:
  - **Non-AI Node** — standard Java logic (file I/O, API calls, data transformation, routing)
  - **AI Node** — delegates to Tier 2 (Nexus AI agent pipeline)
  - **Decision Node** — evaluates a condition and routes to different edges

### Tier 2 — Nexus AI (Agent Pipeline)
- **AgentFactory** — creates/composes AI agents from declarative AgentSpec configurations
  - `sequence(outputKey, agents...)` — agents execute one after another, each reads previous agent's output
  - `parallel(outputKey, agents...)` — agents execute concurrently, all read from same scope state
  - `loopUntil(max, predicate, agentA, agentB)` — loop until predicate evaluates to true or max iterations
- **AgentSpec** — declarative config defining everything needed to create an agent:
  - name, inputs(), outputKey, tools, inputGuardrail, outputGuardrail, maxSequentialToolExecutions, listeners
- **AgenticScope** — shared state container within AI node's agent pipeline. Automatic wiring — each agent reads inputs from scope and writes outputs to scope
- **UntypedAgent** — standard interface for both LLM-backed and custom Java agents
- **Guardrails** — input/output validation with retry, reprompt, and rewrite capabilities
- **Tools** — Java methods with @Tool annotation exposed to the LLM
- **BatchAccumulatorTool** — solves critical scaling problem when agent produces output exceeding LLM's output token limit (e.g., 200+ records). Provides LLM-driven output pagination

### How the Tiers Connect
The AI node acts as the bridge between the two tiers. It translates Graph State into AgenticScope inputs, runs the Tier 2 pipeline, and writes the result back to Graph State for downstream Tier 1 nodes.

## Guardrail System

### Input Guardrails
| Outcome | Method | Effect |
|---|---|---|
| Pass | success() | Input is valid. Proceed to LLM call |
| Rewrite | successWithText() | Input modified. Proceed with modified input |
| Block | fatal(reason) | Input invalid. LLM call is blocked entirely |

### Output Guardrails
| Outcome | Method | Effect |
|---|---|---|
| Pass | success() | Output valid |
| Retry | retry(reason) | Output invalid. Re-invoke LLM with same prompt |
| Halt | fatal(reason) | Unrecoverable error. Halt with exception |

## Failure and Retry Handling

| Layer | Tier | Mechanism | Handles |
|---|---|---|---|
| Graph Node Retry | Tier 1 | LangGraph4j conditional edges + retry logic | Node-level failures, infrastructure errors, timeout |
| LLM Provider | Tier 2 | HTTP-level retry (built into LLM client) | 429 rate limits, 500 errors, network timeouts |
| Input Guardrails | Tier 2 | reprompt()/retry() | Invalid JSON, missing fields, quality violations |
| Loop Pattern | Tier 2 | loopUntil(max, predicate) | Iterative refinement until quality threshold met |
| Batch Tool | Tier 2 | submit_batch() tool | Output token limit exceeded — LLM paginates automatically |

## AI Agent Integration Flow
1. **PromptStore Lookup** — agent name used to look up prompt configuration from database
2. **ChatModel Construction** — built with provider-specific factory. All LLM parameters configured from database
3. **Agent Builder Assembly** — AgentFactory.createAgent(Spec) is called, registers tools and guardrails
4. **Agent Build** — builder produces a configured LangChain4j record ready for invocation

## How to Add a New Workflow (7 Steps)
1. Design the Tier 1 Graph
2. Create Tier 1 Nodes
3. Define Agent Prompts in Database
4. Create AgentSpecs
5. Compose the Tier 2 Pipeline
6. Create the AI Node (Bridge)
7. Wire the Tier 1 Graph

**A typical new workflow with 3-5 agents can be built in 1-2 days** (half a day for AgentSpecs + Tier 2 composition, half a day for Tier 1 graph wiring and testing)

## Benefits

| Benefit | Impact |
|---|---|
| **Faster Development** | New workflows assembled from existing components. A 5-agent workflow = ~30 lines of config code |
| **Clear Separation of Concerns** | Tier 1 handles infra (file I/O, storage, APIs), Tier 2 handles AI orchestration (LLM calls, guardrails, tools) |
| **Standardized Execution** | Every workflow follows: trigger → graph traversal → node execution → AI pipeline → result storage. Consistent behavior across all workflows |
| **Seamless AI Integration** | LLM-based agents and Java logic coexist using same UntypedAgent interface. Teams add AI capabilities without learning new patterns |
| **Quality Enforcement** | Guardrails provide deterministic validation independent of the LLM. Input validation, output schema checking, and automatic reprompt are built in |
| **Automatic Scaling** | BatchAccumulatorTool handles output token limits transparently. System produces correct results whether output is 10 records or 500 |
| **Full Observability** | Both tiers provide execution tracking. Tier 1 tracks node-level execution, Tier 2 tracks conversations with prompt details. End-to-end traceability for compliance |
| **Database-Driven Prompts** | Prompts deploy without code changes. Prompt engineers iterate independently from developers. All keying of configuration centrally managed |
| **Reduced Duplication** | Shared guardrails, tools, orchestration patterns, and Tier 1 nodes eliminate copy-paste across workflows. Bug fixes propagate to all workflows automatically |

## ECDF Mapping

| ECDF Dimension | How This Maps |
|---|---|
| **Thinks** | Identified the need for agentic architecture, researched and designed innovative solution |
| **Designs** | Led end-to-end design of entire two-tier architecture from scratch |
| **Delivers** | Built and shipped the complete framework used across dbCLM |
| **Influences** | Drove AI adoption and set architectural direction for the entire business unit |
| **Achieves** | 18-24 hours → 1 hour for agent creation (95% reduction) |
| **Engages** | Framework enables all teams across dbCLM to build AI agents |
| **Controls** | Built-in guardrails, quality enforcement, observability |
| **Operates** | Full execution tracking, retry handling, failure recovery across both tiers |

## Screenshots Reference
- Nexus AI architecture documentation: framework/IMG_3485.jpg through IMG_3495.jpg
