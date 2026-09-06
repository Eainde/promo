# VP Promotion Speech - Second Round

Target: 7 minutes. 1,198 spoken words. Round 1 delivered 1,191 words in the same slot, so this is the same length as a speech that already fitted, and it leaves room for questions.

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

I want to be precise about credit. I did not do this alone. Policy specialists defined what a senior manager is under the rules, and Operations, Data, Controls and Transformation all had a hand in it. We went from nothing to live in five months. What I brought was the framework it all runs on, and the first working version of it in our unit.

In June the bank held its annual technology showcase in India and demonstrated three artificial intelligence applications to the national press. This was one of the three, named in The Hindu.

Then in August the bank published an article about it on its own internal network, headlined, and I am quoting, how artificial intelligence cut a key client onboarding step from seventy seven minutes to ten. Sixty six people rated it four point six out of five. The Co-Head of Operations and Controls for the Corporate and Investment Bank called it the first production step towards a faster, more accurate and more scalable process that keeps a human accountable for every risk decision.

That is not me saying my work matters. That is the bank saying it.


## SECTION THREE. THE SECOND ONE, AND THE HARDER ONE.

The second one I own end to end, and it is a genuinely harder problem.

Regulation requires us to establish who ultimately owns and controls a corporate client. An analyst traces ownership upwards through layers of holding companies, funds and trusts, across documents in several languages, applying group policy and the rules of every country involved, and works out the percentages by hand.

That now runs automatically, and it has been live for a hundred users since August.

Two things about how I built it. One agent does the work, and a second checks it against seventeen acceptance criteria and sends it back if it fails. The interesting part is what happens when the checker is wrong. If the documents do not support what the reviewer says, the system has to disagree in writing and escalate to a human, rather than quietly changing its answer to make the complaint go away.

The second is that I treat these instructions as production code, not as prose. There are two hundred and sixty five automated tests on them. When users told me the same case was giving different answers on different days, I did not guess at a fix. I built a harness to measure it first.

And I did not just implement what the policy team handed me. I audited it clause by clause, put fifteen written questions back to them, and told them when their own worked examples were wrong. One had the ownership pointing the wrong way. Another had percentages that did not add up to a hundred. They corrected them.


## SECTION FOUR. THE FOUNDATIONS.

None of that runs without the plumbing underneath it, and I built a lot of that too.

Our messaging infrastructure could not handle load. Analysts waited up to an hour for results, and messages were lost permanently on any outage. I rebuilt it. Wait times went to seconds, it handles half a million messages a day, and every message is traceable end to end.

On the documents side, I built automatic linking of client documents to the compliance questions they answer, and rebuilt the engine that decides whether an answer is still valid. That contributed to five million euros in savings and over forty thousand document operations with no human involved. I still own it, and I was fixing production issues in it this month.


## SECTION FIVE. BEYOND MY TEAM.

Outside the bank, I contributed a new integration module to LangChain4j, the open source Java framework our AI platform is built on. That is giving back to the community we depend on.

I also taught it to the wider business unit. A hundred and forty people came to my session in June, it overran on questions, and it was recorded so it is still being used. And I built the shared coding standards that are now the default in every service in our unit. I took part in the bank's hackathon in 2024, led a team in 2025, and I am on the sustainability initiative this year.


## CLOSING.

I am an engineer. I write the code, I ship it, and I own it when it breaks at four in the afternoon on a Friday.

Two years ago our business unit had no AI capability at all. Today it has two workflows in production, both running on a platform I built, and one of them reached the national press. That is why I am ready for Vice President.

Thank you.
