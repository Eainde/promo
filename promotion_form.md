# VP Promotion Form — Akshay Dipta

## Row 31: Repeat Candidate

**Previously nominated:** 2025 VP cycle. **Result:** Not selected.

**Feedback received:** Business impact was lost in technical language. Leadership and cooperation were not visible enough. Firmwide contribution was weak. No sponsors were listed. Individual design ownership was unclear. Presentation was too dense.

**Actions taken since:**

1. Delivered 3 platforms now adopted across the entire business unit, each solving a measurable business problem, pitched in plain business language.
2. Secured 3 sponsors: Lalitha Lalwani (CTO Platform Architect), Tong Su (Director, CTO Initiative Lead), Chris Ashley (Documents & Validity platform).
3. Built firmwide presence. Contributed to a major open-source AI project. Participated in the 2024 Deutsche Bank Hackathon and stepped up to lead a team in 2025. Built shared coding standards now used by every microservice in the unit. AI framework is being evaluated by DB Chief Strategy & Innovation Office as a potential bank-wide standard.
4. Single-handedly designed and built AI framework end to end, demonstrating clear individual design ownership.

---

## Section B: Scope of Role, Experience, Diversity and Inclusion

### Scope of Role

Senior Engineer and Component Guardian across three platforms in Client Life Cycle Management: the AI platform, the messaging infrastructure, and the Documents and Validity platform. I am the technical authority for all three. Every design change and code change goes through me for approval. Together, these platforms handle how client documents are stored, validated and linked to compliance requirements during onboarding. They are the foundation of regulatory compliance for the bank.

Technologies: Java, Spring Boot, Apache Kafka, AI frameworks, event-driven messaging.
Domain: Client onboarding automation, document management, compliance verification.

**Significant contributions:**

**AI Platform.** Our business unit had no AI capability. I single-handedly designed and built Nexus AI, a reusable framework that lets any team build an AI-powered workflow in about an hour instead of a full day. I also built PromptLint, a quality gate that catches bad AI instructions before they reach production. To prove it works, I delivered the first production AI workflow in the business unit. It automatically identifies senior managers from client documents, replacing a manual process. The bank's Chief Strategy and Innovation Office is now evaluating Nexus AI as a potential bank-wide standard.

**Messaging Infrastructure.** The system that moves data between our services was unreliable. Compliance analysts waited 30 to 60 minutes for results. Failed messages were lost permanently and no one could trace where work was stuck. I built a resilient processing engine that now handles half a million messages a day, an automatic failure recovery library, and full message traceability. Wait times dropped to seconds. Daily incidents stopped.

**Documents and Validity.** Client onboarding analysts were manually linking documents to compliance questions and checking whether answers were still valid. I designed automatic document linking and unlinking, and rebuilt the validity engine from a fragmented legacy system into a modular platform. This contributed to €5M in savings. Over 10,000 documents have been auto-linked and over 30,000 outdated links auto-removed without human intervention.

All three platforms are adopted across the business unit, not just my team.

### Engineering Experience

Over 13 years of engineering experience. I have consistently delivered robust, scalable solutions across leading financial and enterprise organisations, building strong technical, architectural and leadership capabilities.

At JP Morgan, I played a central role in building a strategic trading platform that supported complex financial products. I led the development of critical system components end to end and participated in migrating the platform from one cloud environment to another, improving performance, scalability and resilience.

At American Express, I specialised in building dynamic, high-performance user interfaces for the Corporate Purchasing Card portfolio. I developed complex front-end components and integrated them with back-end services over a period of three years.

At HSBC, I contributed to the development of front-office retail banking tools that streamlined banking operations for internal staff. I built both user-facing interfaces and back-end integrations.

At Sears, I designed and developed internet-based retail banking tools, integrating user interfaces with back-end systems.

At Herman Software, I gained foundational engineering experience by developing mobile applications early in my career.

I joined Deutsche Bank in March 2023. Since then I have built deep expertise in event-driven architecture, AI integration in enterprise environments, and engineering quality at scale.

Outside of my day to day role, I contributed to LangChain4j, a widely used open-source AI framework for Java, adding a new integration module for Google's AI models. This was merged into the public project as PR #4658. In 2024 I participated in the Deutsche Bank Hackathon where we developed a software solution to assist dementia patients. In 2025 I stepped up to lead a Hackathon team where we developed a solution for financial inclusion. I am also participating in the bank's environmental sustainability initiative in August 2026.

### Diversity and Inclusion

I bring a diverse cultural background and global perspective to a London-based team working across geographies and time zones. I built shared coding standards and tooling that lower the barrier to entry for all developers. New joiners get consistent guardrails from their first day, regardless of experience level.

I actively mentor junior and mid-level engineers on engineering best practices, AI technologies and modern architecture through hands-on pairing sessions and code review coaching. I have participated in two Deutsche Bank Hackathons, leading a cross-functional team in 2025, bringing together colleagues from different disciplines and backgrounds and fostering collaboration beyond normal team boundaries.

I champion inclusive sprint practices. I encourage contributions from all team members in design discussions, retrospectives and technical decisions, ensuring diverse viewpoints shape our solutions.

By building the AI framework as a reusable, open platform and sharing it across the business unit, I ensured that every team has equal access to AI capability regardless of their size or expertise. Teams that previously could not build AI solutions can now do so, levelling the playing field across the organisation.

---

## Section C: Engineering Behaviours and Capabilities

### Thinks — Level 4

1. Identified that the business unit had no AI capability. Every team wanting to use AI was starting from scratch. I saw the gap, took ownership, and single-handedly researched, designed and built the solution.

2. Rejected the team's proposed approach of using a different programming language for AI. All our engineers and systems use Java. I presented the case for a Java-native solution to technical management and convinced them. This decision has now been validated by bank-wide interest.

3. Independently identified that AI instructions had no quality controls. Nobody was testing them. I created PromptLint, bringing the discipline of automated quality checking to AI instructions for the first time in the organisation.

4. Identified fundamental problems in our messaging infrastructure. There was no automatic recovery from failures, no way to trace where work was stuck, and performance collapsed under load. I designed solutions that transformed it from daily incidents to a resilient platform processing half a million messages a day.

5. Consistently apply the latest industry thinking in AI orchestration patterns, event-driven architecture and automated quality enforcement.

### Engages — Level 3

1. Built professional relationships with senior stakeholders across the organisation to drive AI adoption beyond my immediate team.

2. Worked directly with Lalitha Lalwani (CTO Platform Architect) and Tong Su (Director, CTO Initiative Lead) on the AI initiative. Both are sponsoring my promotion based on this collaboration.

3. Demonstrated the AI framework to Chris Dorr's team (Managing Director, CM Tech). They are now evaluating it for their own use.

4. Presented to the bank's Chief Strategy and Innovation Office (Keith Finnerty, Director and Lead Data Scientist). They are evaluating it as a potential bank-wide standard.

5. As Component Guardian, I coach and mentor developers through code reviews, hands-on pairing and best-practice guidance, building engineering capability across the team.

6. Built shared automated coding standards now adopted by every microservice in the business unit, lowering the barrier for all engineers and ensuring consistent quality.

7. Participated in the 2024 Deutsche Bank Hackathon, developing a software solution for dementia patients. In 2025 I stepped up to lead a cross-functional Hackathon team, developing a solution for financial inclusion.

### Influences — Level 3

1. AI direction. Convinced technical management to adopt a Java-native AI approach instead of introducing a second programming language. Delivered the framework that validated this decision. The bank's Chief Strategy and Innovation Office is now evaluating it as a potential bank-wide standard. Influence that started with a single technical argument is now shaping strategy.

2. Messaging reliability. Drove adoption of my failure-recovery library and new messaging engine across multiple teams in the business unit, establishing the standard for how we handle message reliability.

3. Code quality culture. Built automated coding standards and drove their adoption across every microservice in the business unit. Engineers no longer debate formatting in reviews. The tooling enforces it.

4. Open-source community. Contributed to LangChain4j, a widely used open-source AI framework, adding a new integration module. This gives back to the community that powers our AI platform and raises Deutsche Bank's visibility in the open-source ecosystem.

5. I communicate complex technical decisions in clear business terms, adjusting my message for audiences from engineers to Directors to the Innovation Office.

### Achieves — Level 3

1. AI. Reduced time to build an AI-powered workflow from a full day to about one hour, a 95% reduction. Delivered the first production AI workflow in the business unit, proving the approach works.

2. Messaging. Compliance analysts waited 30 to 60 minutes for results. Now they get them in seconds. The platform processes half a million messages a day. Daily messaging incidents have been eliminated.

3. Documents and Validity. Contributed to €5M in savings. Over 10,000 documents automatically linked to the right compliance questions. Over 30,000 outdated links automatically removed, all without human intervention.

4. Planned and phased the rollout of each platform sequentially. Validity framework first, then messaging, then AI. This managed risk while delivering continuous business value.

5. Every platform solves a real user problem. Faster client onboarding, fewer incidents, less manual effort for compliance analysts.

6. I continue to own all platforms in production, actively resolving issues. Not build and walk away.

### Designs — Level 3

1. AI Framework. Designed to separate business logic from AI orchestration. Teams wire together business steps without needing to understand how the AI models work underneath. Key design decision: built-in quality gates that validate AI inputs and outputs automatically, so bad data never reaches the model and bad results never reach the user. AI instructions are managed centrally and can be updated without code changes. Business teams iterate independently from engineers.

2. Messaging Library. Designed for safe failure recovery. When part of the system goes down, messages wait and retry automatically with increasing delays instead of failing permanently. Only one instance handles retries at a time, preventing duplicate processing. Each team configures their own recovery rules without writing custom code.

3. Validity Framework. Redesigned from fragmented legacy logic scattered across the codebase into a modular system where each validation rule is independent and testable. Added parallel processing so the system handles high volumes without slowing down.

4. All three designs prioritise reliability under failure, scalability under load, observability for diagnosis, and security by default.

5. All three are used across the business unit by multiple teams. Designed for reuse from the start, not retrofitted.

### Delivers — Level 4

1. Subject matter expert and go-to person across three domains: AI workflows, messaging infrastructure, and document validity processing. I am recognised as the technical authority. Every design change and code approval in these areas goes through me.

2. AI Platform. Delivered the complete AI framework, the quality gate for AI instructions, and the first production AI workflow, from concept through to live business use.

3. Messaging. Delivered the new processing engine, the failure recovery library, and full message traceability, transforming an unreliable system into the unit's most stable platform.

4. Documents and Validity. Delivered automatic document linking, automatic unlinking, and the rebuilt validity engine, removing manual steps from every client onboarding.

5. Contributed to LangChain4j, a major open-source AI project, adding a new integration module. This demonstrates engineering capability beyond the bank.

6. Built shared automated coding standards that enable other teams to deliver higher-quality software faster. Now the default for every microservice in the business unit.

### Operates — Level 3

1. Actively resolves production issues. Recently fixed critical bugs in document auto-linking caused by a specific third-party data source and by the client-facing interface. This is ongoing ownership, not build and walk away.

2. Built full message lifecycle tracking for the messaging platform. Production issues that previously took hours to diagnose are now resolved in minutes because every message can be traced end to end.

3. All platforms designed with operational health from the start. Performance monitoring, system health dashboards and scalability are built in, not bolted on after problems emerge.

4. Led a critical client data migration from a legacy database to the new structure. Zero data loss. Zero downtime. Coordinated across teams including late-night production support.

5. Regular participant in production support rotations, incident triage and resolution. I feed insights from production back into engineering improvements.

### Controls — Level 4

Elevated from Level 3 because my scope of control now extends across the entire business unit, not just my own components.

1. Built automated code quality enforcement that is now the mandatory standard across every microservice in the business unit. It prevents poorly-formatted or non-compliant code from reaching production. No manual enforcement is needed. The tooling catches issues at build time.

2. Built PromptLint, automated quality gates for AI instructions. It checks 8 quality dimensions and blocks regressions before they reach production. The same philosophy as code quality enforcement, applied to AI.

3. Built safety controls into the AI framework. Every AI agent has input validation that blocks bad data before it reaches the model, and output validation that catches bad results before they reach the user, with automatic correction.

4. Built safe failure handling into the messaging library. It ensures only one process retries failed messages at a time, preventing duplicates, with a full audit trail of every retry.

5. As Component Guardian, I rigorously review code for all guarded components, enforcing quality and security standards and coaching developers on best practices.

---

## Section D: Endorsers

**Endorser 1:** Lalitha Lalwani, CTO Platform Architect.
Relationship: Worked directly with Akshay on the AI initiative. Observed his end-to-end ownership of the AI framework, from research through design to production delivery.
Statement: [REQUEST FROM LALITHA. Ask her to write 2 to 3 sentences on your AI design ownership and initiative.]

**Endorser 2:** Tong Su, Director, CTO Initiative Lead.
Relationship: Worked directly with Akshay on the AI initiative as the Director-level lead. Observed his ability to influence technical direction and deliver at business-unit scale.
Statement: [REQUEST FROM TONG. Ask him to write 2 to 3 sentences on your influence and delivery.]

**Endorser 3:** Chris Ashley.
Relationship: Worked with Akshay on the initial development of the Documents and Validity platform. Observed his engineering ownership and production commitment.
Statement: [REQUEST FROM CHRIS. Ask him to write 2 to 3 sentences on your engineering impact and ownership.]
