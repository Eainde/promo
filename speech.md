# VP Promotion Speech

Good morning. I'm Akshay Dipta, Senior Engineer on the London Cadbury team in Client Life Cycle Management.

I have thirteen years of industry experience, and joined Deutsche Bank in March 2023. Today I lead AI capability for our business unit, and I am the technical authority for our messaging and AI infrastructure. Every design change and code approval goes through me.

Today I want to walk you through three real business problems I identified, designed solutions for, and delivered.


## SECTION ONE. AI PLATFORM.

The first is artificial intelligence.

When the bank started talking seriously about AI, our business unit had no capability of its own. Every team that wanted to build an AI agent was starting from a blank page. A single agent took eighteen to twenty-four hours to build, and every team rebuilt the same problems from scratch.

I saw this gap and took it on. The team was initially looking at a Python-based solution, but I steered us away from that direction. All of our microservices, infrastructure, and engineers are Java-based. Introducing Python would have created a parallel technology stack that's difficult to integrate and maintain. I presented the case for a Java-native solution to our technical management, and convinced them it was the right path.

From there, I single-handedly researched the problem, proved the concept, designed the architecture, and delivered the full solution.

The result is Nexus AI, our AI workflow framework. Any team in our business unit can now build a working AI agent in about an hour instead of a full day. Alongside it, I built PromptLint, a quality gate that catches bad AI instructions before they reach the model. The same way a spell-checker catches writing mistakes.

To prove it all works end to end, I delivered the first production AI workflow in our entire business unit. It is called the Client Senior Manager workflow. It automatically reads client documents to identify who the senior manager is for each client relationship. Analysts previously did this by hand, reading through pages of documentation. That means teams across the business unit can now automate manual processes that were previously too expensive to build.

But the impact has gone beyond my own team. I presented Nexus AI to the bank's Chief Strategy and Innovation Office, and they are now evaluating it as a potential standard AI framework for Deutsche Bank. I also demonstrated the framework to a team under Chris Dorr in CM Tech, and they are showing interest in onboarding it. Lalitha Lalwani, architect on the CTO platform, and Tong Su, Director and lead for the CTO initiative, have both worked with me on this AI initiative, and are sponsoring my promotion. What started as one engineer solving a local problem, is now being considered as infrastructure for the bank.


## SECTION TWO. KAFKA INFRASTRUCTURE.

The second is about the plumbing that holds everything together.

Our compliance platform handles thousands of client checks every day. But the messaging infrastructure underneath it was fundamentally broken. The system could not handle bursts of messages. When volume spiked, processing ground to a halt, and compliance analysts waited thirty to sixty minutes for results. When any part of the system had a brief outage, messages were lost permanently with no retry mechanism. And there was zero message traceability. When something failed, no one could see where work was stuck or why. This was not a theoretical risk. Users were reporting issues daily, incidents were being raised regularly, and the team was firefighting instead of building.

I built three things to fix this.

The first is a new processing engine built for resilience and scale. It handles high-volume message bursts without degradation. Wait time went from thirty to sixty minutes, down to seconds. The system now processes half a million messages a day.

The second is the Phoenix Retry Library. When part of the platform goes down briefly, messages now wait patiently and retry automatically once things recover, instead of failing permanently.

The third is full message traceability. End to end tracking of every message through every step in the system, from ingestion to completion. Production issues that used to take hours to diagnose are now resolved in minutes.

That means compliance analysts get results in real time, not next day, and fewer incidents disrupting the business.


## SECTION THREE. DOCUMENTS AND VALIDITY.

The third goes back to the heart of what our team does, handling client documents.

When I joined, our onboarding analysts had to verify every document by hand. Then they had to link each document to the right compliance questions, and check whether each answer was still valid. The whole process was largely manual. A new document arriving meant re-checking everything from scratch. It was slow, error-prone, and a bottleneck on every client onboarding.

I designed and built two things to solve this.

The first is Auto-Association and De-Association. When a document is uploaded, the system links it to the right questions automatically. When a newer document arrives, the old link is removed cleanly. There is no human in the loop.

The second is the Validity Framework. Once a document is linked, the framework calculates in real time whether the answer is still valid. I redesigned it from a fragmented legacy system into a modular, scalable architecture.

Together, this work contributed to five million euros in savings. The system has automatically linked over ten thousand documents, and removed over thirty thousand outdated links, all without human intervention. That means faster client onboarding, less manual handling time for analysts, and a better experience for our clients.

I don't just build. I continue to own this in production. Recently, I resolved critical issues in auto-association caused by Schufa-sourced documents and the Fulfillment UI. Chris Ashley, who I worked with on the initial development of this platform, is sponsoring my promotion.


## BEYOND MY TEAM.

My contribution doesn't stop at the boundary of my own team.

I also contribute to open-source beyond Deutsche Bank. I contributed to LangChain4j, the open-source Java AI framework that underpins our AI platform, adding a new integration module for Google's AI models. This is not just using open-source, it is giving back to the community that powers our work.

I also noticed our business unit had no shared coding standards. No formatting rules, no static analysis. I built common build configurations that enforce consistent code quality automatically, and today they are the standard across every microservice in the unit. Two of the platforms I have built, the messaging infrastructure and the AI framework, are now firmwide assets within Client Life Cycle Management, used every day by multiple teams beyond my own.

In 2024, I participated in the Deutsche Bank Hackathon. In 2025, I stepped up to lead a Hackathon team. And in August this year, I am contributing to the bank's environmental sustainability initiative.


## CLOSING.

I am an engineer. I don't just design solutions. I write the code, I build the systems, and I own them in production. When I see a problem no one is solving, I take it on. When I build something, I make it the standard. That is how three of my platforms became the foundation for an entire business unit, and that is why I am ready for Vice President.

Thank you.
