# CSM Workflow — Post Go-Live Results (Aug 2026)

Evidence captured 31-Aug-2026. Source images: `framework/IMG_4751.jpg` (cost slide), `framework/IMG_4752-4754.jpg` (bank-wide intranet article).

This file supersedes the "metrics expected in ~1 month" note in `new_work_csm_workflow.md`.

## Headline Numbers

| Measure | Before | After |
|---|---|---|
| Average processing time per file | ~77 minutes | Under 10 minutes |
| Speed | baseline | More than 7x faster |
| Right-first-time accuracy | n/a | Over 99.5% |
| Cost per file | €19.87 (manual effort) | €8.51 (AI run) |
| Saving per file | | **€11.36, 57% lower** |

Supporting detail from the cost slide:
- Average 16 documents per file. Maximum single file: 87 documents, €42.80.
- Total spend to date: €12.6k across 1,485 executions (live plus back-testing, 7-26 June).
- 74% of cost is driven by document processing (input tokens), not model reasoning or output.

## Bank-Wide Recognition

Intranet article on dbnetwork, Technology & Innovation section, published **25-Aug-2026** (updated 26-Aug):

> **"How AI cut a key KYC client onboarding step from 77 minutes to 10"**

- 66 ratings, **4.6 out of 5**. 5 comments.
- Author: Amir Sadiq.

Quoted in the article, **Ross Mackenzie, Co-Head of Operations & Controls for the Corporate Bank and Investment Bank**:

> "This is the first production step towards a much more ambitious goal: an AI-augmented, end-to-end KYC process that is faster, more accurate and more scalable, while preserving clear human accountability for every risk decision. We are not simply automating individual tasks. We are redesigning how KYC is performed, using AI to remove manual work, strengthen data quality and allow our team to focus on the judgement that protects our clients and the bank."

Article also states:
- The solution is the **first live use case** from the Corporate Bank and Investment Bank KYC Operations AI Accelerator programme.
- **Built and deployed in five months.** KYC specialists defined the business and policy logic, technology teams built and integrated the capability. Live-case testing and user feedback shaped the final version.
- Cross-functional by design: KYC Operations, Technology, Data, Policy, Controls and Transformation.
- Analysts still review the evidence and make the final decision. Human accountability preserved.
- Less rework between colleagues preparing KYC cases and those validating them before approval.
- "The CSM solution lays the foundation for future innovation across the KYC lifecycle."

## Management Visibility

- Cost and savings analysis presented by **Marco Luebbers (Managing Director)** and **Tim Ryan**. Marco is a listed sponsor.
- Quoted at Co-Head level by Ross Mackenzie in a bank-wide publication.

## Agent Inventory (from cost slide)

Ten agents across five waves, each paired with a critic agent. Model: Gemini 2.5 Pro.

| Wave | Agent | Internal name |
|---|---|---|
| 1 | AutoClassifyDoc (+ critic) | DOCUMENT_SOURCE_CLASSIFIER_V2 |
| 1 | NamedEntityExtractor (+ deep critic) | NAMED_ENTITY_EXTRACTOR_V2 |
| 1 | CsmMandateCheck | CSM_MANDATE_EXTRACTOR |
| 2 | NameNormalizer | CSM_NAME_NORMALIZER_V2 |
| 2 | DeDuplication (+ critic) | CSM_DEDUP_LINKER_V2 |
| 3 | CSMClassifier (+ critic) | CSM_CLASSIFIER_V2 |
| 4 | Compare CSM against dbCLM | CSM_AGENTIC_COMPARISON (now a Java tool) |
| 5 | Auto Answer CSM Related Questions | DOCUMENTS_ANSWER_EXTRACTOR |

## Optimisation Levers In Flight

| Lever | Approach | Expected impact |
|---|---|---|
| Model optimisation | Move specific agents from Gemini Pro to Flash 2.5 (de-duplication agent/critic, name normaliser) | €8.51 → €5.61 per run, **-34%** |
| Document input reduction | Link documents to data points via document journey stream so only relevant documents reach agents | Reduces document volume from avg 16 per file. Targets the largest cost driver (74%) |
| AI-based Java code | Use AI to generate Java code and replace agents with Java-based tools (Agent 7 already converted) | Eliminates token usage long-term |

All levers to be validated and tested ensuring no degradation in performance or accuracy.

## How To Use This In The Pitch

- Lead with **77 minutes to under 10** and **57% cheaper per file**. Both are plain business language and need no explanation.
- **99.5% right-first-time** answers the "does AI actually work in a controlled process" question before it is asked.
- The article plus the Ross Mackenzie quote is independent, senior, bank-wide validation. It answers the 2025 feedback on Director-level engagement and firmwide visibility without self-assertion.
- The five-month cross-functional delivery is the cooperation evidence the 2025 panel asked for. Name the disciplines involved.
- The optimisation levers show ongoing ownership, not build-and-walk-away.

## Attribution Guardrail

The article credits the programme and "technology teams", not Akshay by name. Claim only what is defensible in the pitch: he built the framework these agents run on (Nexus AI), and delivered the first agentic workflow in the business unit. Do not claim sole authorship of the headline result.
