# RCP Session — Nexus AI Studio Section Design

## Summary

Add Nexus AI Studio as a new section (Section 4.5) in the RCP presentation, placed between "Real Run — Proof" (Section 4) and "PromptLint" (Section 5). Two slides + a live demo. ~5 minutes total.

**Key message:** Full-stack ownership — "I built the backend framework, the agent pipeline, the observability layer, AND the visual developer experience."

## Context

- RCP session: 40 min content + 20 min Q&A
- Engineering Day version was ~26 min / 15 slides
- Audience saw a Python LangChain/LangGraph session — they know graph concepts
- Nexus AI Studio: React+TS SPA, real-time graph visualization, packaged as Spring Boot JAR

## What Nexus AI Studio Is

A web-based UI for visualizing AI agent workflow graphs in real-time:

- Three-panel layout: thread list (left), graph visualization (center), state inspector (right)
- SVG graph with D3 pan/zoom, ELK.js automatic hierarchical layout
- Live node status animations: pending → active (amber pulse) → completed (green check) / error (red)
- Parallel nodes animate simultaneously — visual proof of concurrency
- State snapshots at every checkpoint with JSON tree viewer and state diffs
- SSE streaming for real-time execution feedback
- Packaged as Maven JAR — any Java service adds it as a dependency, zero frontend setup
- API-compatible with LangGraph Studio contract

Tech: React 18, TypeScript, Vite, Tailwind (dark theme), D3.js, ELK.js, Zustand, Spring Boot auto-config.

## Section Design

### Placement

After Section 4 (Real Run — database tables), before Section 5 (PromptLint). Narrative bridge: "You saw the raw data. Now see what the developer sees."

### Slide 12 (new) — "Why a Visual Layer?"

Narrative transition slide. Brief — not a wall of text.

Content:
- Bridge: "Database tables are powerful for debugging and compliance. But when developing a 12-agent pipeline, you need to see the graph."
- Three needs: see topology while building, live execution feedback, state inspection at every checkpoint
- Intro line: "So I built Nexus AI Studio."

Verbal emphasis: this is about developer experience — the layer that makes the framework usable at scale, not just functional.

### Slide 13 (new) — Tech & Integration

Minimal text, visually light. Setup for the demo.

Content:
- React + TypeScript SPA, packaged as a Spring Boot JAR
- "Add it as a Maven dependency — graph visualization built in"
- ELK.js for automatic layout, D3 for interaction, SSE for real-time streaming
- Compatible with LangGraph Studio API contract
- Landing: "Backend framework, agent pipeline, AND the visualization — one platform."

### Live Demo (~3 min)

Immediately after slide 13. Show Nexus AI Studio with the CSM workflow.

Demo flow:
1. Show idle graph — point out three-panel layout, node topology
2. Trigger a run via the thread panel
3. Audience watches nodes animate: amber pulse → green checkmark
4. Call out parallel waves — same-time activation visible
5. State panel fills with checkpoint events in real-time
6. Click a completed node → show state snapshot in JSON tree viewer
7. Show state diffs between consecutive checkpoints
8. If critic-refiner loop fires multiple times — call it out

Key things to narrate during demo:
- "Every node you saw in the code — the sequence, parallel, loopUntil — you can see them executing live"
- "Click any node — full state at that checkpoint, what went in, what came out"
- "This is the same execution data from the database tables, but rendered as a developer experience"

### Verbal Close

"That's Nexus AI Studio. I built the orchestration framework, the agent pipeline, the observability layer, and the visual developer experience on top. Full stack, one platform."

## Updated Session Structure

| # | Section | Time | Slides |
|---|---------|------|--------|
| 1 | Context | ~3 min | 1-2 |
| 2 | Architecture + Tier 1 | ~3 min | 3-4 |
| 3 | Agent Pipeline | ~8 min | 5-8 |
| 4 | Real Run — Proof | ~6 min | 9-11 |
| **4.5** | **Nexus AI Studio** | **~5 min** | **12-13 + live demo** |
| 5 | PromptLint | ~5 min | 14-16 |
| 6 | Close | ~1 min | 17 |
| | **Total** | **~31 min** | **17 slides** |

## Demo Fallback

Pre-record a 2-min screen capture of a complete CSM workflow execution in Studio. If live demo fails (network, backend, timing), switch to recording: "Let me show you a recorded run." Visual impact preserved.

## Deliverables

1. Update `presentation_outline.md` — add slides 12-13 and live demo section, renumber subsequent slides
2. Update `speech.md` — add Section 4.5 speech text (~600 words covering slides + demo narration)
3. Update `RCP_session/CLAUDE.md` — note Studio section addition and demo logistics

## Out of Scope

- Changes to existing sections 1-4 or 5-6 (no modifications)
- Building or modifying the Studio application itself
- Creating the screen recording fallback (separate task)
