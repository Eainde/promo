# New Work — Nexus AI Studio: The Visual Layer on the AI Platform

Source: `~/AD/GIT/nexus-ai-studio/` (57 commits, 31-May to 26-Aug-2026). Numbers verified 05-Sep-2026.

## Overview
The frontend companion to Nexus AI. A **UI-only Spring Boot JAR**: any Java service on the framework adds one Maven dependency, sets one property, and gets an interactive workflow UI at `/studio/`. Contains no business logic. A React SPA packaged as static assets, served by Spring auto-configuration.

Third product in the platform, after the Nexus AI framework and PromptLint. Its own repository, its own release.

## Why It Exists
The framework solved *how to build an agent*. It did not solve what happens once agents run.

- **Engineers could not see a workflow.** Read the raw mermaid graph or trace the code. To follow a run, tail logs and correlate timestamps.
- **Business users could not touch the prompts.** The instructions define what the system extracts and how it classifies, so the policy owners are the right people to change them. Every change went through an engineer.

Both problems have the same root: the platform was invisible.

## Two Capabilities

### 1. Workflow visualisation
- ELK.js auto-layout: subgraphs, conditional and parallel nodes, drag, zoom/pan, minimap, click-to-highlight adjacency, `/`-to-search nodes
- Live execution over server-sent events: node-by-node animation, LIVE banner (active node, n/N, elapsed), per-node timing tooltips
- Failed node highlighted where it failed
- Per-checkpoint state: Tree/JSON viewers, **changed-key badges** between consecutive checkpoints, in-data find, maximize overlay
- Multi-graph: each graph runs in its own execution slice, concurrently in the background. Switching the dropdown never stops a run
- Dark/light themes, three-panel layout (Threads · Graph · State)

### 2. Prompt management
- List every prompt bound to a workflow, view any version in full
- **Side-by-side version diff**, down to the parameters (`PromptDiff`, `SplitDiff`, `ParamsDiff`, `DiffRuler`)
- Save as new version, promote a version to default, run a prompt against the model from the screen
- Dirty-state bar so an unsaved draft is never silently lost

## Architecture
```
Browser → /studio/                        → React SPA (static assets from the Studio JAR)
        → /init, /workflows, /threads,
          /nexus/stream/*, /prompts/*      → implementing service (Nexus AI endpoints)
```
- **Stack:** Spring Boot 3.3 · React 18 · Vite · ELK.js · Zustand
- **Data flow:** mermaid string from `/init` → `mermaidParser.ts` → GraphModel → `elkLayout.ts` → SVG in GraphPanel
- **Execution flow:** Run → `useStreamExecution` → `POST /threads` → `POST /nexus/stream/{id}?thread={tid}` (SSE) → each checkpoint event updates the Zustand store
- **Auto-config:** `StudioWebConfig.java`. Disabled by default, needs `clm.nexus.ai.studio.enabled=true`. Base path via `clm.nexus.ai.studio.path`

## Design Decisions (the ones that matter for the pitch)

### API-compatible with LangGraph Studio ⭐
Same endpoint URLs, same response shapes. A service already exposing those endpoints gets this UI with zero frontend changes.

**Why this is the key point:** choosing Java over Python meant giving up the Python AI tooling. Rather than accept that as a permanent cost, Akshay rebuilt the missing tool and kept its contract. This is where the Java decision is vindicated rather than merely defended.

### A dependency, not a project
One Maven dependency plus one property. Nothing to build, nothing to deploy separately, no per-service UI to write. Off unless explicitly enabled. Same instinct as the Kafka retry library and the Maven mixins: a pattern in a document gets implemented five ways, a dependency with one switch gets used.

### Ship ahead of the backend, degrade honestly
Three prompt endpoints (save version, promote to default, run prompt) shipped before the server side existed. A `404`/`501` raises a friendly "coming soon" modal, so the feature lights up by itself when the backend lands, with no frontend release. Any other status is a real error, and the user's draft is preserved either way.

### Per-workflow prompt versions, and saving ≠ deploying
`AI_CHAT_PROMPT_FUNCTION.PROMPT_VERSION` (the binding row) is authoritative. `AI_CHAT_PROMPT.DEFAULT_PROMPT_VERSION` is vestigial and deliberately treated as dead, because two sources of truth for "which version is live" is how the wrong instruction reaches production. `UNIQUE (CW_PROMPT_CODE, FUNCTION_CODE)` means one prompt shared by two workflows can legitimately run a different version in each. Saving a version does not deploy it, promoting it does.

## Scale
| Measure | Value |
|---|---|
| Commits | 57 (31-May to 26-Aug-2026) |
| Frontend code | ~20,600 lines TypeScript/TSX |
| Components | 55 |
| Tests | **548 in 71 files** (545 pass locally, 3 fail on `ECONNREFUSED :3000`, environment not defect) |
| Artifact | `com.nexus:nexus-ai-studio:1.0.0-SNAPSHOT`, packaging `jar` |

## Docs
- `docs/nexus-studio-confluence.md` — Confluence wiki markup for the internal page, includes a recorded walkthrough
- `docs/prompt-api-contract.md` — the five prompt endpoints plus prerequisite
- `docs/prompt-db-schema.md` — prompt table contract

## ECDF Mapping
| Dimension | How This Maps |
|---|---|
| **Thinks** | Recognised the tooling gap the Java decision created, and closed it by rebuilding the tool rather than reversing the decision |
| **Designs** | Compatibility with an existing contract as a deliberate constraint. Zero-config adoption. Save separated from deploy |
| **Delivers** | A second shipped product on the platform, 548 tests |
| **Engages** | Puts prompts in front of the policy owners instead of routing every wording change through an engineer |
| **Operates** | Live execution visibility and per-checkpoint state, replacing log correlation |
| **Controls** | Versioned prompts, explicit promotion step, single source of truth for the live version |

## How To Use This In The Pitch
- It is the **answer to the obvious challenge** to the Java decision: "you gave up the tooling." He rebuilt it, to the same contract.
- "Nobody uses a platform they cannot see" is the one-line framing.
- The prompt screen is the **business-partnership** angle: policy owners change the rules, not engineers.
- Pairs with PromptLint: PromptLint checks prompt *quality*, Studio manages prompt *versions and deployment*.

## Screenshots
None yet. Worth capturing: a rendered workflow graph, a run mid-execution with the LIVE banner, the checkpoint state view with changed-key badges, and the prompt version diff.
