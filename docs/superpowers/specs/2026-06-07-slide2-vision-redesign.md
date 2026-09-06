# Slide 2 Vision Redesign — Remove Duplication with Slide 3

**Date:** 2026-06-07
**Scope:** RCP session presentation, Slide 2 vision section + corresponding speech text

## Problem

All 6 vision points in Slide 2 (custom chat models, custom serialization, bank auth, auto-persisted checkpoints, pluggable listeners, rate limiting) are repeated in Slide 3 "What's Inside Nexus AI." PromptLint and Nexus AI Studio have no presence in the vision.

## Decision

Reframe Slide 2 vision as **outcome-focused "what if" questions**. Slide 3 stays unchanged and answers the "how." Zero duplication.

## Slide 2 — Vision Section (Replaces All 6 Current Points)

1. What if a new agent took **1 hour**, not 24?
2. What if a 12-agent orchestration pipeline was expressible in **20 lines of code**?
3. What if observability, auth, and database-driven prompts were **built in by default**?
4. What if prompt quality was **enforced in CI**, like code linting?
5. What if you could **see your agents execute live**, click any node, inspect state?

Points 1-3 set up Slide 3 (framework internals) and Slides 5-12 (code, DB schema).
Point 4 sets up Slides 16-18 (PromptLint).
Point 5 sets up Slides 14-15 (Nexus AI Studio).

## Slide 2 — Problem Section (Unchanged)

- Building a new AI agent took **18-24 hours** of boilerplate setup
- Every team was **reimplementing** the same infrastructure from scratch
- **No prompt quality gates** — bad prompts reached production silently
- **No observability** — no visibility into token usage, latency, or failures
- **Duplicated infra** — auth, model config, retry logic copy-pasted everywhere

## Speech Text (Vision Portion Only)

So the vision was clear. What if building a new agent took one hour, not twenty-four? What if a twelve-agent orchestration pipeline with parallel execution and iterative loops was expressible in twenty lines of code? What if observability, authentication, and database-driven prompts were all built in by default, zero developer code? What if prompt quality was enforced in CI, the same way we enforce code quality, deterministic, no LLM calls, fail the build if a prompt drops below threshold? And what if you could see your agents execute live, click any node, inspect the full state at that checkpoint?

That's what I built. Let me show you what's inside.

## Files to Update

1. `RCP_session/presentation_outline.md` — Slide 2 vision section
2. `RCP_session/speech.md` — Section 1, Slide 2 speech text
