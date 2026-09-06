# RCP Session — Nexus AI Studio Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Nexus AI Studio as Section 4.5 in the RCP presentation — two new slides + live demo section, with speech text and CLAUDE.md updates.

**Architecture:** Three markdown file edits. Insert new section content between existing Section 4 (Real Run) and Section 5 (PromptLint). Renumber all subsequent slides (+2). No code changes.

**Tech Stack:** Markdown content only.

---

## File Map

| File | Action | Purpose |
|------|--------|---------|
| `RCP_session/presentation_outline.md` | Modify (lines 293-399) | Insert slides 12-13 + live demo, renumber Section 5 → slides 14-16, Section 6 → slide 17 |
| `RCP_session/speech.md` | Modify (lines 141-186) | Insert Section 4.5 speech (~500 words), renumber Section 5 → slides 14-16, Section 6 → slide 17 |
| `RCP_session/CLAUDE.md` | Modify (lines 12-20) | Add Studio to session scope and note demo logistics |

---

### Task 1: Insert Studio slides into presentation_outline.md

**Files:**
- Modify: `RCP_session/presentation_outline.md:293-399`

- [ ] **Step 1: Insert Section 4.5 between Section 4 and Section 5**

Insert the following after line 293 (`> **Reference:** Screenshots IMG_3957-3959 show the real production table.` + `---`), before the current `## Section 5`:

```markdown
## Section 4.5: Nexus AI Studio (~5 min) — Slides 12-13 + Live Demo

---

### Slide 12 — Why a Visual Layer?

**Narrative bridge from Section 4:**

> "You just saw raw execution data — database tables with run IDs, agent traces, token counts. That's powerful for debugging and compliance. But when you're developing a 12-agent pipeline, you need to **see** it."

**Three developer needs:**

- **See topology while building** — which agents connect to which, where the parallel forks are, where the loops sit
- **Live execution feedback** — watch agents activate, complete, or fail as the workflow runs
- **State inspection at every checkpoint** — what went in, what came out, at every node

**Intro line:**
> "So I built Nexus AI Studio — a real-time graph visualization layer for the framework."

---

### Slide 13 — Tech & Integration

**Minimal text — setup for the live demo:**

- React + TypeScript SPA, packaged as a **Spring Boot JAR**
- "Add it as a Maven dependency — graph visualization built in, zero frontend setup"
- ELK.js for automatic hierarchical layout, D3 for pan/zoom, Server-Sent Events for real-time streaming
- API-compatible with the LangGraph Studio contract
- Dark theme, three-panel layout: thread list | graph visualization | state inspector

**Landing line:**
> "Backend framework, agent pipeline, AND the visualization — one platform."

---

### Live Demo (~3 min)

**Setup:** Nexus AI Studio running locally with CSM workflow loaded.

**Demo flow:**

1. **Show idle graph** — point out three-panel layout. Thread list on the left, graph in the centre, state panel on the right. Nodes show the full CSM pipeline topology — the same nodes from the code in slide 7.

2. **Trigger a run** — click Run in the thread panel with CSM input parameters.

3. **Watch execution animate:**
   - Nodes pulse amber as they activate
   - Parallel wave nodes activate simultaneously — visual proof of concurrency (same thing the database timestamps showed, but now you can see it)
   - Nodes turn green with checkmarks as they complete
   - State panel fills with checkpoint events in real-time

4. **Inspect state** — click a completed node. Show the JSON tree viewer with full state snapshot at that checkpoint. Show state diffs between consecutive checkpoints.

5. **Call out the loop** — if critic-refiner loop fires multiple times, point it out: "Watch — the critic scored below 0.85, so it loops back to the refiner. Second pass — score meets threshold, done."

**Key narration points:**
- "Every node you saw in the code — the sequence, parallel, loopUntil — you can see them executing live"
- "Click any node — full state at that checkpoint. What went in, what came out"
- "Same execution data from the database tables, rendered as a developer experience"

**Fallback:** If live demo fails, switch to pre-recorded screen capture: "Let me show you a recorded run."

**Verbal close:**
> "That's Nexus AI Studio. I built the orchestration framework, the agent pipeline, the observability layer, and the visual developer experience on top. Full stack, one platform."

---
```

- [ ] **Step 2: Renumber Section 5 header and slides**

Change:
- `## Section 5: PromptLint (~5 min) — Slides 12-14` → `## Section 5: PromptLint (~5 min) — Slides 14-16`
- `### Slide 12 — Prompts Are Code` → `### Slide 14 — Prompts Are Code`
- `### Slide 13 — 8 Quality Dimensions` → `### Slide 15 — 8 Quality Dimensions`
- `### Slide 14 — Code: JUnit API + CI Integration` → `### Slide 16 — Code: JUnit API + CI Integration`

- [ ] **Step 3: Renumber Section 6 header and slide**

Change:
- `## Section 6: Close (~1 min) — Slide 15` → `## Section 6: Close (~1 min) — Slide 17`
- `### Slide 15 — Getting Started + Thank You` → `### Slide 17 — Getting Started + Thank You`

---

### Task 2: Insert Studio speech text into speech.md

**Files:**
- Modify: `RCP_session/speech.md:141-186`

- [ ] **Step 1: Insert Section 4.5 speech text**

Insert the following after line 141 (the `---` after Section 4's last paragraph), before the current `## Section 5`:

```markdown
## Section 4.5: Nexus AI Studio (Slides 12–13 + Live Demo, ~5 min)

**[Slide 12 — Why a Visual Layer?]**

You just saw the raw execution data — database tables, agent traces, token counts. That's powerful for auditing and debugging. But when you're developing a 12-agent pipeline with parallel waves and iterative loops, you need to see it. You need to see the graph topology while you're building. You need live feedback as agents execute. And you need to inspect the state at every checkpoint — what went in, what came out.

So I built Nexus AI Studio — a real-time graph visualization layer for the framework.

**[Slide 13 — Tech & Integration]**

It's a React and TypeScript single-page application, packaged as a Spring Boot JAR. Any Java service adds it as a Maven dependency and gets graph visualization built in — zero frontend setup required.

Under the hood, ELK.js computes the hierarchical graph layout automatically. D3 handles pan and zoom. And real-time execution updates stream via Server-Sent Events — the same technology your browser uses for live notifications.

The API is compatible with the LangGraph Studio contract — so if you've seen LangGraph Studio in the Python ecosystem, this is the Java-native equivalent, integrated directly into Nexus AI.

Backend framework, agent pipeline, and the visualization layer — one platform.

**[Live Demo]**

Let me show you. This is Nexus AI Studio running locally with the CSM workflow we've been discussing.

On the left, the thread panel — where you manage workflow runs. In the centre, the graph — every node from the code I showed you earlier. On the right, the state inspector.

I'll trigger a run now. Watch the graph.

[Trigger run]

See the first wave — the parallel extraction agents all light up at the same time. They're running concurrently, just like the database timestamps showed earlier. As each one finishes, it turns green. Now the sequential agents kick in — contextualiser, then the next wave.

Watch the state panel on the right — every checkpoint streams in live. Click any completed node and you get the full state snapshot. Here's the candidate extractor — you can see the JSON output, the extracted names, the confidence scores. And if I click the next node, I can see the diff — what changed between checkpoints.

And here's the critic-refiner loop. Watch — the critic scores the output. Below 0.85, so it loops back to the refiner. Second pass — meets the threshold. Done.

Every node you saw in the code, every parallel wave, every loop iteration — visible in real time. Same execution data from the database tables, but rendered as a developer experience.

That's Nexus AI Studio. I built the orchestration framework, the agent pipeline, the observability layer, and the visual developer experience on top. Full stack, one platform.
```

- [ ] **Step 2: Renumber Section 5 header and slide references**

Change:
- `## Section 5: PromptLint (Slides 12–14, ~5 min)` → `## Section 5: PromptLint (Slides 14–16, ~5 min)`
- `**[Slide 12 — Prompts Are Code]**` → `**[Slide 14 — Prompts Are Code]**`
- `**[Slide 13 — 8 Quality Dimensions]**` → `**[Slide 15 — 8 Quality Dimensions]**`
- `**[Slide 14 — Code: JUnit API + CI Integration]**` → `**[Slide 16 — Code: JUnit API + CI Integration]**`

- [ ] **Step 3: Renumber Section 6 header and slide reference**

Change:
- `## Section 6: Close (Slide 15, ~1 min)` → `## Section 6: Close (Slide 17, ~1 min)`
- `**[Slide 15 — Getting Started + Thank You]**` → `**[Slide 17 — Getting Started + Thank You]**`

---

### Task 3: Update RCP_session/CLAUDE.md

**Files:**
- Modify: `RCP_session/CLAUDE.md:12-20`

- [ ] **Step 1: Update session scope to include Studio**

Change line 13 from:
```
- **Goal:** Present Nexus AI + PromptLint, show the Java approach. Don't duplicate the Python session's LangChain/LangGraph deep-dive but show how it's done in Java
```
to:
```
- **Goal:** Present Nexus AI + Nexus AI Studio + PromptLint, show the Java approach. Don't duplicate the Python session's LangChain/LangGraph deep-dive but show how it's done in Java
```

- [ ] **Step 2: Add Studio constraint/note at end of file**

Append after line 20 (the last constraint):

```markdown

## Nexus AI Studio
- **Section 4.5** — new section between Real Run and PromptLint
- **Live demo** of CSM workflow execution in Studio (~3 min within the section)
- **Fallback:** pre-recorded screen capture if live demo fails
- **Key message:** full-stack ownership — backend framework + agent pipeline + visualization layer
- **Studio codebase:** `/Users/akshaydipta/AD/GIT/nexus-ai-studio`
```
