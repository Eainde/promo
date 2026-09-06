# New Work — Ownership & Control Extraction (Second Production Agentic Workflow)

Source: `~/AD/GIT/ownership-prompts/` (87 commits, all Akshay). Status captured 31-Aug-2026.

## Overview
The second agentic workflow to reach production in the business unit, after the Client Senior Manager workflow. Akshay owns this one end to end. **Live in production for a controlled group of 100 users.**

## Business Problem (plain English)
When the bank takes on a corporate client, regulation requires it to establish who ultimately owns and controls that company. An analyst reads a pile of case documents, org charts, shareholder registers, certificates of incorporation, regulatory filings, client emails, often in several languages, and traces ownership upwards through layer after layer of holding companies, funds, trusts and partnerships. They apply group policy plus the rules of each country involved, and work out the percentages by hand.

This workflow replaces that manual trace. It reads the documents and returns the complete ownership and control structure: every shareholder, every layer, every percentage, voting and control rights, who the ultimate owners are, where documents conflict with each other, what is missing, and what needs to be requested from the client.

## Before & After

### Before
- Analyst manually reads and traces ownership across every document in the case.
- Slow, inconsistent between analysts, and hard to evidence to a regulator.
- An earlier attempt used a six-agent pipeline, which was complex and expensive to run.

### After
- One AI call returns the complete structure with the evidence attached to every claim.
- Collapsed the six-agent pipeline into a single call.
- Live for 100 users under controlled rollout.

## Design Principles (audit and regulator facing, not engineering preferences)
- **Evidence only.** No outside knowledge, no guessing. Every assertion carries a verbatim quote from a document.
- **Zero data loss.** Never drop a party for being below threshold, zero percent, or missing.
- **Deterministic.** The same case must produce the same answer every time.
- **Fail closed.** Record a gap and raise a flag rather than invent an answer.

## Scale
- 1,573-line rule set. 26 rules, 43 numbered sub-sections.
- 16 mandatory processing gates run in fixed order, from document inventory and translation through to completeness validation.
- 35 fields per ownership record. A 22-rung precedence ladder resolves what role each party holds, first match wins.
- Deployed prompt is 110,532 characters.

## Maker / Checker Built In
A second AI agent automatically reviews every output against **17 acceptance criteria** and returns a pass, accept-with-notes, or retry verdict. A retry sends the case back to be re-extracted.

The interesting engineering is in what happens when the reviewer is wrong. The rules require the extractor to re-extract rather than patch, to treat a review finding as a prompt to re-read a document rather than as evidence in itself, and to formally dispute a finding the documents do not support, raising it to a human instead of quietly complying. Without that, a reviewer that makes a mistake causes the exact fabrication the reviewer exists to catch.

## Engineering Rigour Applied To AI
This is the differentiator. AI instructions are usually treated as prose that nobody tests.

- **256 automated tests** pin the English rules to the output schema so the two cannot silently drift apart. Examples: `test_critic_criteria_names_match_schema_enum`, `test_every_record_property_is_named_in_the_system_prompt`, `test_direction_contract_is_consistent_across_prompts_and_schema` (guards against inverting every ownership relationship), `test_no_assertion_without_a_verbatim_quote`.
- **Run-to-run consistency harness.** Built after users reported that re-running the same case produced materially different results. It normalises away wording and ordering, then buckets remaining differences into parties, links, numbers, classification and derived values. Narrative drift is reported but never counted against agreement.
- **Regression discipline.** Every regression test was demonstrated failing against the pre-fix prompt before being accepted, then passing. This became policy after two earlier tests were found to be vacuous.
- **Determinism release.** One release resolved 3 critical and 10 important internal contradictions in the rules, added 7 new rules and corrected 9. Tests went from 25 to 82, then to 256.
- **Versioned deployment.** Prompts live as versioned rows in an Oracle table consumed by a Java service. A change is a new version, never an edit in place. The deployment SQL is generated and verified by decoding it back and comparing byte-for-byte against source, never hand-edited.
- Packaged the deployment tooling as a reusable, documented skill with a generate mode and a verify mode, so the next person does not rediscover the constraints.

## Partnership With The Business
The policy team supplied the requirements. Akshay did not just implement them.

- Ran a **clause-by-clause audit** of every supplied requirement, marking each as in, in-with-changes, or out, with the reason where wording was changed or rejected.
- Put **15 written questions** back to the business, each citing the line in their own document, and ran four rounds of response in a single day.
- **Rejected supplied examples that were wrong.** One worked example carried an inverted ownership relationship. Another's fund percentages did not total 100. Corrected figures were then supplied by the business.
- **Pushed open items back rather than guessing.** One rule was deliberately not implemented because the business could not supply a worked example, on the basis that a rule which cannot be applied identically twice is worse than no rule.
- Raised a documentation defect back to the business: their source document still carried withdrawn rules and would disagree with the deployed prompt unless corrected.
- Escalated three policy questions to the standards owner for confirmation before deployment.

## ECDF Mapping

| ECDF Dimension | How This Maps |
|---|---|
| **Thinks** | Collapsed a six-agent pipeline into one call. Recognised that non-determinism was the real defect behind user complaints, and built a measurement harness before attempting a fix |
| **Designs** | 16-gate processing order, 35-field output contract, 22-rung precedence ladder, maker/checker loop with explicit dispute semantics |
| **Delivers** | Second agentic workflow in the business unit to reach production, live for 100 users |
| **Operates** | Versioned deployment, generated-and-verified release artefacts, 10-point verification checklist where each item has caught a real bug |
| **Controls** | Evidence-only and fail-closed by design. 256 tests preventing rule drift. Every assertion traceable to a document quote for audit |
| **Engages** | Clause-by-clause partnership with the policy team, 15 questions raised, four rounds resolved in a day |
| **Influences** | Disputed incorrect business-supplied examples and had them corrected. Refused to implement an unspecifiable rule and said why |
| **Achieves** | Replaced manual ownership tracing. 3 critical and 10 important rule contradictions found and resolved |

## Known Gaps (be honest if asked in Q&A)
- No continuous integration. Tests run manually.
- The test suite is not in version control because the directory is ignored repo-wide.
- Deployment SQL is executed by hand.
- No published volume or service-level figures yet. Rollout is deliberately limited to 100 users.

## How To Use This In The Pitch
- Frame it as **the second one, and the harder one**. The first workflow proved the framework works. This proves it scales to a genuinely difficult regulatory problem.
- The maker/checker story lands with a non-technical panel: one AI does the work, another checks it, and there are rules for when the checker is wrong.
- The testing story is the strongest differentiator. Most people treat AI instructions as prose. Akshay treats them as production code with a test suite.
- The business partnership answers the 2025 feedback on cooperation directly, with specifics rather than an assertion.
