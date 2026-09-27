# VP Promotion Speech - Second Round

Target: 7 minutes. 1,154 spoken words. Round 1 delivered 1,191 words in the same slot, so this is close to the length of a speech that already fitted.

---

Good morning. I'm Akshay Dipta, a Senior Engineer in Client Life Cycle Management.

Before a bank can take on a client, it has to prove it knows who that client really is. Who owns them, who runs them, and whether the paperwork stands up. My team builds the platform that does that. I have thirteen years in the industry, and I joined Deutsche Bank in March 2023.

Today I want to tell you about two things that are now running in production, and how they got there.


## SECTION ONE. THE PLATFORM I BUILT.

Two years ago, when the bank started talking seriously about artificial intelligence, our business unit had no capability of its own. Every team started from a blank page, one agent took a full day to build, and everybody rebuilt the same problems from scratch.

I took that on. The team was leaning towards a Python-based solution. I steered us away. All our services, our infrastructure and our engineers are Java. A second language would have given us a parallel stack nobody could integrate or maintain. I made the case for Java, and that is the direction we took.

Then I built it. I researched it, proved the concept, designed the architecture, and delivered it single-handedly. It is called Nexus AI. Any team in our unit can now build a working agent in about an hour instead of a full day. Alongside it I built a quality gate that catches badly written AI instructions before they ever reach the model, the way a spell checker catches a typo before you send the email.

Choosing Java had one cost. The ready made tooling for this work is all Python. So I built that too. It draws every workflow as a picture that lights up while it runs, and it lets the people who own the policy change the AI's instructions without waiting for a software release.

A framework nobody uses is worth nothing. So I went and used it.


## SECTION TWO. THE FIRST ONE, AND WHAT IT DID.

Every client has senior managers who run it, and the bank has to identify them. Analysts did that by hand, reading every document one at a time, checking each name across several systems, and sorting out duplicates and country rules themselves. Cases went back and forth between preparer and reviewer. It took seventy seven minutes per case.

So I built the first AI workflow on my framework to do it. I designed the multi agent architecture, a team of ten AI agents, and I wrote every instruction that drives them. They read every document in parallel, find the senior managers, merge duplicates and apply country-specific rules. Checker agents review every step, and the results are matched to the client's existing records. The analyst reviews it and makes the final decision. I took it from nothing to production in five months.

A case now takes under ten minutes. That is more than seven times faster, at over ninety nine and a half percent right first time, and fifty seven percent cheaper per case. In June it was one of only three AI applications the bank showed the national press in India, and it was named in The Hindu. In August the bank featured it on its own internal network, and readers rated it four point six out of five.


## SECTION THREE. THE SECOND ONE, AND THE HARDER ONE.

The second one I own end to end, and it is a much harder problem.

Regulation requires the bank to know who ultimately owns and controls every corporate client. An analyst read documents in several languages, traced ownership upwards layer by layer through holding companies, funds and trusts, and worked out the percentages by hand against group policy and the rules of every country involved. Documents conflicted, evidence was missing, and one case took over three hours. And getting an owner wrong is a regulatory problem, not an inconvenience.

So I designed the rules, the architecture, the tests and the deployment. The AI reads every document, in any language, maps the ownership chart layer by layer, works out the percentages and identifies the ultimate owners under each country's rules. Conflicts and gaps are flagged, never guessed, and every claim carries a quote from a document. It checks its own work against seventeen rules before any person sees it. Two hundred and sixty five automated tests make sure the same case gives the same answer this month as last month. That is what makes the speed safe.

A case now takes five to fifteen minutes instead of over three hours. About four hundred users work with it today. It handles about ninety percent of the clients we check, and it frees an estimated seventy one people's worth of work every year.


## SECTION FOUR. WHAT IT ALL STANDS ON.

Both of those workflows read documents. Neither works without the layer underneath, and that layer is mine.

At the centre is a state machine I built. It works out where every question and every document stands. A question's state decides what evidence we need, and when it is ready to be worked. A document's state decides whether it can be trusted.

On top of that, linking documents to questions was manual. I automated the linking, and the unlinking that everyone forgets, when a newer document supersedes an older one. A missing document is visible. A stale one still looks current, and an auditor cannot tell the difference.

So both workflows only see work my state machine released, and only act on documents it marked good.

That platform contributed five million euros in savings, and forty thousand document operations now run with no human. I still own it in production, and when an issue comes up, I am the one who fixes it.

One layer down, all of it travels over messaging, which could not cope. Analysts waited half an hour for a result. I designed a new library with automatic retry, and the same work now takes seconds, at a million messages a day.


## SECTION FIVE. BEYOND MY TEAM.

Outside the bank, I contributed a new integration module to LangChain4j, the open source Java framework our AI platform is built on. That is giving back to the community we depend on.

I also taught it to the wider business unit. A hundred and forty people came to my session in June, it overran on questions, and it was recorded so it is still being used. And I built the shared coding standards that are now the default in every service in our unit. I took part in the bank's hackathon in 2024, led a team in 2025, and I am on the sustainability initiative this year.


## CLOSING.

I am an engineer. I write the code, I ship it, and I own it when it breaks at four in the afternoon on a Friday.

Two years ago our business unit had no AI capability at all. Today it has two workflows in production, both running on a platform I built, and one of them reached the national press. That is why I am ready for Vice President.

Thank you.
