# RCP Session — CLAUDE.md

## Context
- RCP = broader business unit in Deutsche Bank
- Akshay already delivered one session (Engineering Day) — earlier version of these materials
- RCP session: 19 slides, ~38 min content + ~20 min Q&A
- Materials: `presentation_outline.md`, `speech.md`, `create_presentation.py`, `Nexus_AI_PromptLint_RCP.pptx`

## Session Details
- **Audience:** RCP-wide, same people who attended a separate Python LangChain/LangGraph session
- **Audience knowledge:** They know LangGraph/LangChain concepts from the Python session. They do NOT know Nexus AI or PromptLint
- **Time:** 1 hour total — ~38 min content + ~20 min Q&A
- **Goal:** Present Nexus AI + Nexus AI Studio + PromptLint, show the Java approach
- **Focus:** Nexus AI framework + PromptLint — not a LangChain/LangGraph tutorial

## Key Constraints
- Don't go deep into LangChain4j/LangGraph4j basics (audience already got that in Python)
- Show how Nexus AI builds ON TOP of those — the value-add, not the underlying library
- PromptLint is a key differentiator — no Python equivalent shown in other session

## Current Slide Structure (19 slides)
1. Title
2. Problem + Vision (outcome-focused "what if" points, no overlap with slide 3)
3. What's Inside Nexus AI (9-capability grid)
4. Two-Tier Architecture
5. AgentSpec
6. Spring Boot Agent Configuration
7. Workflow Graph Definition
8. DB Schema ER Diagram
9. Prompt Table
10. Workflow Run Table
11. Agent Execution Table
12. Checkpoints Table
13. Nexus AI Studio (info — Today + Vision split)
14. Nexus AI Studio (live demo — screenshot + switch to live app)
15. Prompts Are Code
16. 8 Quality Dimensions
17. JUnit API + CI Integration (real test code + real execution output)
18. Getting Started
19. Thank You & Q&A

## Key Design Decisions
- Slide 2 vision uses "what if" outcomes, slide 3 shows "how" — no duplication
- Composition Patterns slide removed (covered verbally in other slides)
- Studio split into info slide + screenshot/live demo slide
- PromptLint slide 17 uses real production test code and actual test execution output
- Studio screenshot: `studio_screenshot.png`

## Nexus AI Studio
- **Live demo** of CSM workflow execution in Studio
- **Fallback:** screenshot on slide 14 serves as fallback if live demo fails
- **Key message:** full-stack ownership — backend framework + agent pipeline + visualization layer
- **Studio codebase:** `/Users/akshaydipta/AD/GIT/nexus-ai-studio`

## File Relationships
- `create_presentation.py` generates `Nexus_AI_PromptLint_RCP.pptx`
- User may manually edit PPTX after generation — always check PPTX state before assuming script output is current
- All three files (outline, speech, PPTX/script) must stay in sync
