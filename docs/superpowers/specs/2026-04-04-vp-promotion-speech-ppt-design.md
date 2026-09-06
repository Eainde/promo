# VP Promotion Speech & Presentation — Design Spec

## Goal
Create a 7-minute promotion speech and accompanying PowerPoint presentation for Akshay Dipta's VP/Senior Engineer promotion at Deutsche Bank TDI.

## Context
- Second attempt — rejected in 2025
- Must directly address 8 critical feedback points from last year's panel
- Speech is delivered while presenting slides (slides = visual anchors, speech = narrative)
- No slide limit, 7-minute speech limit (~950 words)
- Sponsors slot reserved (confirmation pending)
- D4 involvement not included for now

## Strategy: "Three Big Bets"

Structure the entire pitch around 3 major achievements, each escalating in scope:

### Bet 1: Intelligent Document & Validity Platform (Team/Platform Impact)
- Auto-Association + De-Association + Validity Framework as one end-to-end system
- Document comes in → auto-linked to right questions → validity calculated automatically
- **Before:** Analysts manually linked documents to questions, manually checked validity — slow, error-prone
- **After:** Fully automated — contributed to 25M savings, hundreds of analyst hours saved, faster client onboarding
- Shows: Designs, Delivers, Achieves, Thinks

### Bet 2: Kafka Infrastructure Revolution (Business Unit Impact)
- Phoenix Retry Library + Spring Cloud Stream Library + Kafka Observability
- The backbone that makes everything work at scale
- **Before:** Daily processing delays, users waiting 30-60 mins for results, failed messages stuck in database, no visibility into message lifecycle
- **After:** Everything processed in seconds, 500K messages/day, full end-to-end message traceability
- Adopted across entire dbCLM business unit — not just team level
- Component Guardian of Kafka
- Shows: Designs, Delivers, Operates, Controls, Influences, Achieves

### Bet 3: AI Agentic Platform (Innovation & Future)
- Nexus AI framework + PromptLint quality tooling + CSM Workflow (first production use case)
- Three-part story: built the framework → built the quality tooling → delivered first production workflow
- **Before:** No AI capability in CLM, building an AI agent took 18-24 hours, no prompt quality assurance
- **After:** Agent creation in 1 hour (95% reduction), 8-dimension prompt quality analyzer, first agentic workflow in dbCLM (CSM identification & auto-answering)
- Single-handedly designed — all research, POC, design, and development
- Shows: Thinks, Designs, Delivers, Influences, Achieves, Controls

## Speech Structure (7 minutes, ~950 words)

| Section | Time | Content |
|---|---|---|
| **Opening** | 30s | Name, role, 12 years experience, joined DB March 2023, Technical Lead for Sieve team in Client Life Cycle Management. One line on what CLM does in plain English |
| **Bet 1** | 2 min | Before/after narrative. Manual → automated. 25M savings, analyst hours saved, faster onboarding |
| **Bet 2** | 2 min | Before/after narrative. 30-60 min delays → seconds. 500K msgs/day. dbCLM-wide adoption. Kafka observability |
| **Bet 3** | 2 min | Before/after narrative. No AI → full agentic platform. 18-24 hrs → 1 hr. First agentic workflow. Single-handedly designed |
| **Firmwide + Close** | 30s | Hackathon 2024 (participant) → 2025 (team lead), plastic cleaning initiative, sponsors, forward-looking close |

## Presentation Structure (8 slides)

| Slide | Title | Content |
|---|---|---|
| 1 | Title Slide | Name, role (AVP/Senior Engineer), team (Sieve, London), DB branding |
| 2 | About Me | 12 years, key orgs, joined DB March 2023, roles (Tech Lead, Component Guardian, Scrum Master, Kafka Guardian). Icons, no wall of text |
| 3 | My Platform | Plain English CLM explanation. Simple diagram: document → auto-association → validity → compliance |
| 4 | Bet 1: Intelligent Document & Validity Platform | Before/After visual. Metrics: 25M savings, 100s analyst hours. Architecture diagram showing auto-association triggering validity |
| 5 | Bet 2: Kafka Infrastructure Revolution | Before/After visual. Metrics: 30-60 min → seconds, 500K msgs/day. Diagram: retry library + observability. "Adopted across business unit" badge |
| 6 | Bet 3: AI Agentic Platform | Three-part visual: Framework → Quality → Production. Metrics: 18-24 hrs → 1 hr. "First agentic workflow in dbCLM". "Single-handedly designed" callout |
| 7 | Beyond My Team | Firmwide: Hackathon 2024 → team lead 2025, plastic cleaning. Division-wide: Kafka library + Nexus AI across dbCLM. Sponsors slot |
| 8 | Thank You | Forward-looking statement, contact details |

## Slide Design Principles
- Large readable text (min 18pt font)
- No acronyms without explanation
- Before/After visuals on Bets 1, 2, 3
- Max 5-6 bullet points per slide
- Every metric in large bold font
- Business language throughout — no jargon
- Clean, professional design with DB branding feel

## Panel Feedback Coverage

| Feedback Point | How Addressed |
|---|---|
| Business language | Every achievement explained in plain English, no jargon |
| Leadership & cooperation | Kafka library + Nexus AI adopted across dbCLM, Scrum Master, team lead in hackathon |
| Firmwide contribution | Hackathon (participant → leader), plastic cleaning, division-wide libraries |
| Sponsors | Slot reserved on slide 7 |
| Solution design ownership | Single-handedly designed Nexus AI, designed Validity Framework, designed Kafka Phoenix Library |
| D4 involvement | Not included for now |
| PPT readability | 8 slides, large text, before/after visuals, no wall-of-text |
| Business benefit | Every bet starts with business problem and ends with business impact |

## Speech Writing Guidelines
- Storytelling with before/after narratives, not bullet-point lists
- Plain English — explain like panel is non-technical
- Every technical example tied to business benefit
- Show growth trajectory: team impact → business unit impact → innovation
- Concise — sacrifice grammar for concision per user preference
- ~950 words total
