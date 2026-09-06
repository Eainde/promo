# VP Promotion Speech & Presentation — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a 7-minute promotion speech and 8-slide PowerPoint presentation for VP/Senior Engineer promotion at Deutsche Bank TDI.

**Architecture:** "Three Big Bets" narrative — escalating from team impact (Document & Validity Platform) → business unit impact (Kafka Infrastructure) → innovation (AI Agentic Platform). Speech tells the story, slides provide visual anchors with before/after visuals and bold metrics.

**Tech Stack:** Markdown for speech draft, python-pptx for PowerPoint generation

---

### Task 1: Write the Speech — Opening Section

**Files:**
- Create: `speech.md`

**Reference files to read first:**
- `last_year_feedback.md` — panel feedback to address
- `last_year_work.md` — roles and background context
- `docs/superpowers/specs/2026-04-04-vp-promotion-speech-ppt-design.md` — approved spec

- [ ] **Step 1: Write the Opening section (~75 words, 30 seconds)**

Write to `speech.md`:

```markdown
# VP Promotion Speech — Akshay Dipta

## Opening (30 seconds)

Good morning everyone. My name is Akshay Dipta. I'm a Senior Engineer and Technical Lead on the Sieve team within Client Life Cycle Management — the platform that manages how Deutsche Bank onboards clients, verifies their documents, and ensures regulatory compliance.

I've spent 12 years building systems across major financial institutions — JP Morgan, HSBC, American Express — and joined Deutsche Bank in March 2023. Since then, I've taken on the role of Technical Lead, Component Guardian, and Scrum Master.

Today, I want to share three initiatives where I identified real business problems and built solutions that now operate across our entire business unit.
```

- [ ] **Step 2: Review word count**

Run: `wc -w speech.md`
Expected: ~75-90 words. Adjust if needed.

---

### Task 2: Write the Speech — Bet 1 (Intelligent Document & Validity Platform)

**Files:**
- Modify: `speech.md`

**Reference files to read first:**
- `last_year_work.md` — Auto-Association, Validity Framework details
- `new_work_kafka_library.md` — context on how validity calculation connects

- [ ] **Step 1: Write Bet 1 section (~250 words, 2 minutes)**

Append to `speech.md`:

```markdown
## Bet 1: Intelligent Document & Validity Platform (2 minutes)

When a client is onboarded at Deutsche Bank, analysts must verify documents — passports, proof of address, corporate filings — and link each document to the right compliance questions. Then they check whether each question has been answered correctly.

When I joined, this was largely manual. Analysts would read a document, decide which questions it relates to, and link them one by one. If a new document came in, they had to re-check everything. It was slow, error-prone, and created bottlenecks in client onboarding.

I designed and built two systems that work together to solve this.

The first is Auto-Association and De-Association. When a document is uploaded, the system automatically identifies which compliance questions it answers and links them. If a newer, more relevant document arrives, the old link is removed automatically. No manual intervention needed.

The second is the Validity Framework. Once a document is linked, this framework automatically calculates whether the answer is valid — checking rules, thresholds, and conditions in real time. I redesigned this from a fragmented legacy system into a modular, scalable architecture.

Together, these two systems form an intelligent pipeline: documents come in, get linked to the right questions, and their validity is calculated — all automatically.

The impact: this platform has contributed to saving the bank 25 million pounds through automation. Hundreds of analyst hours have been freed up. Client onboarding that used to stall on document verification now moves significantly faster.
```

- [ ] **Step 2: Review word count**

Run: `wc -w speech.md`
Expected: ~325-340 total words so far. Adjust if over.

---

### Task 3: Write the Speech — Bet 2 (Kafka Infrastructure Revolution)

**Files:**
- Modify: `speech.md`

**Reference files to read first:**
- `new_work_kafka_library.md` — Kafka Phoenix Retry Library, Spring Cloud Stream, observability details

- [ ] **Step 1: Write Bet 2 section (~250 words, 2 minutes)**

Append to `speech.md`:

```markdown
## Bet 2: Kafka Infrastructure Revolution (2 minutes)

Everything I just described — the auto-association, the validity calculations — runs on a messaging backbone. Thousands of events flow through our system every day. When a document is uploaded, a message triggers the association. When a question is linked, another message triggers the validity check.

But the messaging infrastructure had serious problems. Failed messages would sit in a database with no automated retry. Processing delays meant users were waiting 30 to 60 minutes for their compliance results to appear. And when something went wrong, there was no way to trace a message through the system to find where it failed.

I built three things to fix this.

First, I created the Kafka Phoenix Retry Library — a reusable library that automatically retries failed messages with intelligent backoff. It's cluster-safe, configurable, and teams can enable it with a single line of configuration.

Second, I introduced a new messaging library using Spring Cloud Stream that eliminated the daily processing lag. We went from 30 to 60 minute delays to processing everything within seconds — handling half a million messages per day.

Third, I built full message observability into both libraries. For the first time, teams can trace the complete lifecycle of any message from start to finish, which has been critical for finding and fixing production issues.

These libraries aren't just used by my team. They've been adopted across the entire Client Life Cycle Management business unit — multiple teams rely on them daily. I serve as the Component Guardian for this messaging infrastructure.
```

- [ ] **Step 2: Review word count**

Run: `wc -w speech.md`
Expected: ~575-600 total words. Adjust if over.

---

### Task 4: Write the Speech — Bet 3 (AI Agentic Platform)

**Files:**
- Modify: `speech.md`

**Reference files to read first:**
- `new_work_nexus_ai.md` — Nexus AI architecture
- `new_work_prompt_lint.md` — PromptLint details
- `new_work_csm_workflow.md` — CSM workflow details

- [ ] **Step 1: Write Bet 3 section (~250 words, 2 minutes)**

Append to `speech.md`:

```markdown
## Bet 3: AI Agentic Platform (2 minutes)

Our business unit had no AI capability. When teams wanted to use AI to automate a task — like reading a document and extracting information — each team built everything from scratch. It took 18 to 24 hours to build a single AI agent, with no consistency, no quality controls, and no reusable patterns.

I saw an opportunity and took it on single-handedly. I did the research, built the proof of concept, designed the architecture, and developed the full framework.

The result is Nexus AI — an agentic workflow framework that lets any team build an AI-powered workflow in about one hour instead of a full day. It has a two-tier architecture: the first tier handles the business logic and orchestration, the second tier manages the AI agents, their quality guardrails, and their tools. Teams define what they want in a simple configuration, and the framework handles the rest.

Alongside this, I built PromptLint — a quality analyzer that tests AI prompts the same way we test code. It scores prompts across eight quality dimensions, catches regressions before they reach production, and runs in milliseconds with no AI calls needed. This brings engineering discipline to AI development.

To prove it works, I delivered the first production AI workflow in our entire business unit — a system that automatically reads client documents, identifies Client Senior Managers, and answers compliance questions that analysts previously handled manually.

This is now the foundation for how AI workflows are built across Client Life Cycle Management.
```

- [ ] **Step 2: Review word count**

Run: `wc -w speech.md`
Expected: ~825-850 total words. Adjust if over.

---

### Task 5: Write the Speech — Firmwide & Closing

**Files:**
- Modify: `speech.md`

- [ ] **Step 1: Write Firmwide + Closing section (~100 words, 30 seconds)**

Append to `speech.md`:

```markdown
## Firmwide & Closing (30 seconds)

Beyond my platform work, I've been growing my contribution to the wider firm. In 2024, I participated in the Deutsche Bank Hackathon. In 2025, I stepped up to lead a team. I'm also participating in the environmental sustainability initiative this August.

Two of the libraries I built — the messaging infrastructure and the AI framework — are now used across our entire business unit, not just my team.

I believe my work demonstrates impact at the level expected of a Vice President, and I'm excited to continue driving innovation and delivering value at Deutsche Bank.

Thank you.

---

**[Sponsors section — to be added upon confirmation]**
```

- [ ] **Step 2: Final word count check**

Run: `wc -w speech.md`
Expected: ~925-975 words total. Target is ~950. Adjust sections if significantly over/under.

- [ ] **Step 3: Review speech against panel feedback checklist**

Verify each feedback point from `last_year_feedback.md` is addressed:
1. Business language — no jargon? ✓
2. Leadership & cooperation — shown? ✓
3. Firmwide contribution — prominent? ✓
4. Sponsors — slot reserved? ✓
5. Solution design ownership — shown? ✓
6. PPT readability — (covered in PPT tasks) ✓
7. Business benefit — every bet ties back? ✓

---

### Task 6: Install python-pptx and Create PPT Generation Script

**Files:**
- Create: `generate_ppt.py`

- [ ] **Step 1: Install python-pptx**

Run: `pip3 install python-pptx`

- [ ] **Step 2: Create the PPT generation script — Slides 1-3**

Write to `generate_ppt.py` the beginning of the script that creates:
- **Slide 1 (Title):** "Akshay Dipta — VP Promotion", subtitle "Senior Engineer | Sieve Team | Client Life Cycle Management | London"
- **Slide 2 (About Me):** 12 years experience, key organisations, roles at DB (Tech Lead, Component Guardian, Scrum Master, Kafka Guardian), joined March 2023
- **Slide 3 (My Platform):** "Client Life Cycle Management" — plain English: "Manages how Deutsche Bank onboards clients, verifies documents, and ensures regulatory compliance". Visual flow: Document Upload → Auto-Association → Validity Check → Compliance Ready

Design specs for all slides:
- White/light background, DB blue (#001E96) for headers
- Minimum 18pt font for body text
- Metrics in 28pt+ bold
- Clean, professional layout
- No acronyms without explanation

- [ ] **Step 3: Run and verify slides 1-3 generate correctly**

Run: `python3 generate_ppt.py`
Expected: `promotion_presentation.pptx` created, openable, 3 slides visible

---

### Task 7: Add Bet Slides to PPT Script (Slides 4-6)

**Files:**
- Modify: `generate_ppt.py`

**Reference files to read:**
- `new_work_kafka_library.md`
- `new_work_nexus_ai.md`
- `new_work_prompt_lint.md`
- `new_work_csm_workflow.md`

- [ ] **Step 1: Add Slide 4 — Bet 1: Intelligent Document & Validity Platform**

Before/After layout:
- Left column "BEFORE": Analysts manually link documents, manual validity checks, slow onboarding
- Right column "AFTER": Auto-association & de-association, automated validity calculation, intelligent document pipeline
- Bottom metrics bar: "£25M saved" | "100s of analyst hours freed" | "Faster client onboarding"

- [ ] **Step 2: Add Slide 5 — Bet 2: Kafka Infrastructure Revolution**

Before/After layout:
- Left column "BEFORE": 30-60 min delays, failed messages stuck, no message tracing
- Right column "AFTER": Processing in seconds, 500K messages/day, full lifecycle observability
- Bottom metrics bar: "30-60 min → Seconds" | "500,000 msgs/day" | "Adopted across business unit"

- [ ] **Step 3: Add Slide 6 — Bet 3: AI Agentic Platform**

Three-part flow visual:
- Box 1: "Nexus AI Framework" — "Build AI agents in 1 hour (was 18-24 hrs)"
- Box 2: "PromptLint" — "8-dimension quality analyzer, no AI calls, CI integrated"
- Box 3: "CSM Workflow" — "First production AI workflow in the business unit"
- Callout: "Single-handedly designed — research, POC, architecture, development"
- Bottom metric: "18-24 hours → 1 hour | First agentic workflow in dbCLM"

- [ ] **Step 4: Run and verify slides 4-6**

Run: `python3 generate_ppt.py`
Expected: 6 slides, all readable, metrics prominent, before/after layout clear

---

### Task 8: Add Final Slides to PPT Script (Slides 7-8)

**Files:**
- Modify: `generate_ppt.py`

- [ ] **Step 1: Add Slide 7 — Beyond My Team**

Two sections:
- "Firmwide": Hackathon 2024 (participant) → 2025 (team lead), Environmental sustainability initiative (Aug 2026)
- "Division-Wide Impact": Kafka Phoenix Library → adopted across dbCLM, Nexus AI Framework → adopted across dbCLM
- Sponsors section: "[Sponsor names — to be confirmed]"

- [ ] **Step 2: Add Slide 8 — Thank You**

- "Thank You" in large text
- "Akshay Dipta | Senior Engineer | Sieve Team, London"
- Forward-looking: "Excited to continue driving innovation and delivering value at Deutsche Bank"

- [ ] **Step 3: Run final PPT generation**

Run: `python3 generate_ppt.py`
Expected: `promotion_presentation.pptx` with 8 slides, all readable and professional

- [ ] **Step 4: Verify complete PPT against spec**

Open and check:
1. All 8 slides present ✓
2. No acronyms without explanation ✓
3. All metrics in large bold font ✓
4. Before/after visuals on slides 4, 5, 6 ✓
5. No wall-of-text on any slide ✓
6. Business language throughout ✓
7. Sponsors slot on slide 7 ✓

---

### Task 9: Final Review — Speech + PPT Alignment

**Files:**
- Review: `speech.md`, `promotion_presentation.pptx`

- [ ] **Step 1: Verify speech-to-slide alignment**

Check that each speech section maps to corresponding slide:
- Opening → Slides 1-3
- Bet 1 → Slide 4
- Bet 2 → Slide 5
- Bet 3 → Slide 6
- Firmwide + Close → Slides 7-8

- [ ] **Step 2: Verify panel feedback coverage**

Cross-reference against all 8 feedback points from `last_year_feedback.md`:
1. Business language ✓
2. Leadership & cooperation ✓
3. Firmwide contribution ✓
4. Sponsors slot ✓
5. Solution design ownership ✓
6. D4 involvement — excluded by design
7. PPT readability ✓
8. Business benefit ✓

- [ ] **Step 3: Time the speech**

Read `speech.md` aloud at speaking pace. Target: 6.5-7.5 minutes.
If too long: trim Bet sections proportionally.
If too short: add one more impact detail to each Bet.
