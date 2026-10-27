# Year-End Self Evaluation 2026

Workday form, 3 boxes. Paste text below the `---` in each section. Items marked **[confirm]** need your check before pasting.

---

## WHAT - Overall Delivery

**Summary**
In 2026 I took two AI workflows into production on the AI platform I designed and built, while continuing to own our document and messaging core. Delivery covered all three priorities, target-state AI architecture, sprint delivery with AI tooling, and engineering quality with thought leadership across CLM tech.

**Priority 1. AI technical architecture, frameworks, data model, test strategy**
- **Nexus AI**. Designed and built the Java-native agentic framework used across CLM. Agent build time down from a full day to about one hour. Steered the programme away from a parallel Python stack so the AI layer fits our existing Java estate.
- **PromptLint**. Static quality gate for AI prompts, runs in CI with a JUnit API and catches weak instructions before they reach the model.
- **Nexus AI Studio**. Prompt management and live workflow visualisation (548 automated tests). Policy owners can manage prompts without a software release.
- Design artefacts, architecture decisions and test strategy documented on the team wiki **[confirm links]**.

**Priority 2. Feature delivery, dependencies, AI tooling**
- **Senior Manager identification (CSM)**. First agentic workflow in CLM, ten-agent architecture, taken from zero to production in five months (go-live Jul-2026). Case time 77 min to under 10 min, over 99.5% right first time, 57% cheaper per case (EUR 19.87 to EUR 8.51). Featured on the bank intranet (25-Aug-2026) and shown at Bank on Tech, Bengaluru, covered by national press.
- **Ownership and control extraction**. Second production AI workflow, owned end to end (rules, architecture, tests, deployment). Case time 198 min to 5-15 min, about 400 users from 5-Oct-2026, covers about 90% of clients checked, estimated 71 FTE of analyst time freed per year.
- Dependencies with Operations, Policy and partner teams tracked in Jira and raised in weekly SoS **[confirm]**.
- AI tooling used daily in development **[confirm tools, e.g. GitHub Copilot / Gemini / dbLumina, attach usage stats]**.

**Priority 3. Engineering quality and thought leadership**
- Test-first engineering across the AI platform, with over 2,100 automated tests, including 1,139 unit tests in Nexus AI, 418 in PromptLint and 548 in Nexus AI Studio. Every change is verified before release, so teams building on the platform can rely on it.
- Owned production for Documents & Validity and fixed live issues as they arose.
- Added multi-document support to Documents & Validity. Previously each question could hold only one document, now one question can be supported by multiple documents.
- Thought leadership. Led a 140-attendee RCP session (11-Jun-2026, recorded and still in use), shared coding standards now default across CLM services, Nexus AI under review as a bank-wide standard, open-source module contributed to LangChain4j.
- Bias for action. Made the Java-native platform call early and delivered both workflows on it.

---

## HOW - Overall Behaviour

I have acted in line with our four guiding principles and the Code of Conduct throughout the year.

**Client-centric**
Both AI workflows were built around the analyst's real pain, hours of manual document reading per case. The analyst stays the decision maker. The results show it, with CSM over 99.5% right first time and Ownership cases down from over three hours to 5-15 minutes.

**Innovative**
Brought AI capability to CLM where none existed. Designed Nexus AI, PromptLint and Nexus AI Studio, and contributed back to open source (LangChain4j). Challenged the default Python route with a Java-native design that the team could own long term.

**Disciplined**
Built control into the AI, not around it. Every extracted fact carries a document quote, conflicts and gaps are flagged and never guessed, checker agents review every step, and the platform underneath is protected by over 2,100 automated tests. I own what I ship in production and fix issues as they come up.

**Collaborative**
Worked clause by clause with the Policy team and closely with Operations on both workflows. Shared the platform openly. 140 colleagues attended my RCP session, multiple teams now build on Nexus AI, and I mentor engineers through pairing and code review.

**Code of Conduct**
Completed all mandatory training **[confirm]**. Handled client and colleague data with care, followed information security and AI usage policies, and credited programme and team contributions accurately.

---

## Supporting Documents (upload list)

Combine into one PDF if Workday allows. Use only the cropped images where noted.

| # | Document | Source file | Supports |
|---|---|---|---|
| 1 | Ross Mackenzie CSM go-live email, 10-Jul-2026 | `framework/IMG_4785_cropped.jpg` (**cropped only**) | Delivery, senior recognition |
| 2 | Bank intranet article, 25-Aug-2026 | `framework/IMG_4752-4754.jpg` | Delivery, visibility |
| 3 | CSM cost and savings slide | `framework/IMG_4751.jpg` | 57% cheaper per case |
| 4 | Board deck update, 22-Sep-2026 (Ownership) | `framework/IMG_4826-4829.jpg` | 198 to 5-15 min, 71 FTE, 400 users |
| 5 | The Hindu article, 19-Jun-2026 | `framework/IMG_4768-4770.jpg` | External visibility |
| 6 | RCP session attendance + chat feedback, 11-Jun-2026 | `framework/IMG_4771-4773.jpg` (4771 already cropped) | Collaboration, influence |
| 7 | Nexus AI Studio screenshot | `framework/nexus_studio_csm_workflow.png` | Architecture, delivery |
| 8 | Panellist brief (optional, full depth) | `second_round/Panellist_Brief_Akshay_Dipta.docx` | All priorities |
| 9 | **[add]** AI tooling usage stats, Sonar coverage, GitHub commit/PR stats | export from tools | Priorities 2d, 3a, 3b |

Items 1-7 credit the programme, not you by name. Fine as context next to the delivery text above.
