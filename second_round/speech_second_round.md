# VP Promotion Speech - Second Round

Target: 7 minutes. 1,195 spoken words. Round 1 delivered 1,191 words in the same slot, so this is the same length as a speech that already fitted, and it leaves room for questions.

---

Good morning. I'm Akshay Dipta, a Senior Engineer in Client Life Cycle Management.

Before a bank can take on a client, it has to prove it knows who that client really is. Who owns them, who runs them, and whether the paperwork stands up. My team builds the platform that does that. I have thirteen years in the industry, and I joined Deutsche Bank in March 2023.

Today I want to tell you about two things that are now running in production, and how they got there.


## SECTION ONE. THE PLATFORM I BUILT.

Two years ago, when the bank started talking seriously about artificial intelligence, our business unit had no capability of its own. Every team started from a blank page, one agent took a full day to build, and everybody rebuilt the same problems from scratch.

I took that on. The team was leaning towards a Python-based solution. I steered us away. All our services, our infrastructure and our engineers are Java. A second language would have given us a parallel stack nobody could integrate or maintain. I made that case to technical management, and I convinced them.

Then I built it. I researched it, proved the concept, designed the architecture, and delivered it single-handedly. It is called Nexus AI. Any team in our unit can now build a working agent in about an hour instead of a full day. Alongside it I built a quality gate that catches badly written AI instructions before they ever reach the model, the way a spell checker catches a typo before you send the email.

Choosing Java had one cost. The ready made tooling for this work is all Python. So I built that too. It draws every workflow as a picture that lights up while it runs, and it lets the people who own the policy change the AI's instructions without waiting for a software release.

A framework nobody uses is worth nothing. So I went and used it.


## SECTION TWO. THE FIRST ONE, AND WHAT IT DID.

The first thing I built on it identifies the senior managers responsible for running a client's organisation. Analysts used to do that by hand, reading document after document and checking each name across several systems.

That work used to take seventy seven minutes per case. It now takes under ten. That is more than seven times faster, at over ninety nine and a half percent right first time, and an independent cost analysis put it at fifty seven percent cheaper per case.

I designed the whole thing. The multi agent design is mine, and I wrote every instruction that drives it, working through the rules with the policy specialists. Nothing to live in five months.

In June the bank held its annual technology showcase in India and demonstrated three artificial intelligence applications to the national press. This was one of the three, named in The Hindu.

Then in August the bank published an article about it on its own internal network, headlined, and I am quoting, how artificial intelligence cut a key client onboarding step from seventy seven minutes to ten. Sixty six people rated it four point six out of five. The Co-Head of Operations and Controls for the Corporate and Investment Bank called it the first production step towards a faster, more accurate and more scalable process that keeps a human accountable for every risk decision.

That is not me saying my work matters. That is the bank saying it.


## SECTION THREE. THE SECOND ONE, AND THE HARDER ONE.

The second one I own end to end, and it is a genuinely harder problem.

Regulation requires us to establish who ultimately owns and controls a corporate client. An analyst traces ownership upwards through layers of holding companies, funds and trusts, across documents in several languages, applying group policy and the rules of every country involved, and works out the percentages by hand.

> ⚠ **PLACEHOLDER NUMBERS — collect and replace before delivery.** Three to verify: (1) manual minutes per case, (2) minutes now, (3) accuracy measure. Everything else in this section is sourced.

One case took an analyst about two hours. It now takes under fifteen minutes, and it has been live for a hundred users since August. Over ninety five percent of cases come back right first time.

Getting an owner wrong on a client file is a regulatory problem, not an inconvenience, so speed on its own is worthless here. I designed it to mark its own homework against seventeen rules the policy team signed off before any person sees it, and to escalate to a human when the documents genuinely do not give an answer instead of inventing one. Two hundred and sixty five automated tests mean the same client case gives the same answer this month as it did last month. That is what makes the time saving safe to bank.

And I did not just implement what the policy team handed me. I audited it clause by clause, put fifteen written questions back to them, and told them when their own worked examples were wrong. One had the ownership pointing the wrong way. Another had percentages that did not add up to a hundred. They corrected them.


## SECTION FOUR. WHAT IT ALL STANDS ON.

Both of those workflows read documents. Neither works without the layer underneath, and that layer is mine.

At the centre is a state machine I built. It works out where every question and every document stands. A question's state decides what evidence we need, and when it is ready to be worked. A document's state decides whether it can be trusted.

On top of that, linking documents to questions was manual. I automated the linking, and the unlinking that everyone forgets, when a newer document supersedes an older one. A missing document is visible. A stale one still looks current, and an auditor cannot tell the difference.

So both workflows only see work my state machine released, and only act on documents it marked good.

That platform contributed five million euros in savings, and forty thousand document operations now run with no human. I still own it, and I was fixing production issues this month.

One layer down, all of it travels over messaging, which could not cope. Analysts waited half an hour for a result. I designed a new library with automatic retry, and the same work now takes seconds, at half a million messages a day.


## SECTION FIVE. BEYOND MY TEAM.

Outside the bank, I contributed a new integration module to LangChain4j, the open source Java framework our AI platform is built on. That is giving back to the community we depend on.

I also taught it to the wider business unit. A hundred and forty people came to my session in June, it overran on questions, and it was recorded so it is still being used. And I built the shared coding standards that are now the default in every service in our unit. I took part in the bank's hackathon in 2024, led a team in 2025, and I am on the sustainability initiative this year.


## CLOSING.

I am an engineer. I write the code, I ship it, and I own it when it breaks at four in the afternoon on a Friday.

Two years ago our business unit had no AI capability at all. Today it has two workflows in production, both running on a platform I built, and one of them reached the national press. That is why I am ready for Vice President.

Thank you.
