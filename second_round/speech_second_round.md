# VP Promotion Speech - Second Round

Target: 7 minutes. 1,181 spoken words. Round 1 delivered 1,191 words in the same slot, so this is close to the length of a speech that already fitted.

Teleprompter format. One breath per line. Blank line = short beat. *(pause)* = full pause, look up at the panel. **Bold** = stress the word. `▶ SLIDE` headings = click to that slide. Word count excludes headings and *(pause)* lines.

---

## ▶ SLIDE 1. Title

Good morning.  
I'm **Akshay Dipta**,  
a Senior Engineer in Client Life Cycle Management.

## ▶ SLIDE 2. About me and my platform

I have **thirteen years** in the industry,  
and I joined Deutsche Bank in March 2023.  
I lead AI for our business unit,  
and I am the technical authority for our messaging and AI infrastructure.

*(pause)*

Before a bank can take on a client,  
it has to prove it knows who that client really is.

**Who runs them.**  
**Who owns them.**  
**And whether the paperwork stands up.**

My team builds the platform that answers those three questions.  
I built its core, and I will come back to that.

*(pause)*

But first, how artificial intelligence arrived.


## ▶ SLIDE 3. The AI platform I built

Two years ago, our business unit had **no AI capability** of its own.  
One agent took a full day to build,  
and everybody rebuilt the same problems from scratch.

I took that on.

The team was leaning towards a Python-based solution.  
I steered us away.  
Everything we run is Java,  
and a second language would have meant a parallel stack nobody could maintain.  
I made the case for Java, and that is the direction we took.

*(pause)*

Then I built it.  
I researched it, proved the concept, designed the architecture,  
and delivered it **single-handedly**.  
It is called **Nexus AI**.  
Any team in our unit can now build a working agent  
in **about an hour**, instead of a full day.

Alongside it I built **PromptLint**.  
A quality gate that catches badly written AI instructions  
before they ever reach the model.  
The way a spell checker catches a typo before you send the email.

On top of it I built **Nexus AI Studio**.  
It is a prompt management system,  
so the people who own the policy can manage the AI's instructions directly,  
without waiting for a software release.  
And it draws every workflow as a picture that lights up while it runs.

*(pause)*

A framework nobody uses is worth nothing.  
So I used it, on the first of those three questions.

**Who runs the client.**


## ▶ SLIDE 4. Who runs the client

Every client has senior managers who run it,  
and the bank has to identify them.

Analysts did that by hand.  
Reading every document, one at a time.  
Checking each name across several systems.  
Sorting out duplicates and country rules themselves.  
Cases went back and forth between preparer and reviewer.  
It took **seventy seven minutes** per case.

*(pause)*

So I built the first AI workflow on my framework to do it.  
I designed the multi agent architecture, a team of **ten AI agents**,  
and I wrote every instruction that drives them.

They read every document in parallel.  
They find the senior managers, merge duplicates and apply country-specific rules.  
Checker agents review every step,  
and the results are matched to the client's existing records.  
The analyst reviews it and makes the final decision.

I took it from nothing to production in **five months**.

*(pause)*

A case now takes **under ten minutes**.  
That is more than **seven times faster**,  
at over **ninety nine and a half percent** right first time,  
and **fifty seven percent cheaper** per case.

In June the bank showcased it to the national media in India,  
and it was covered by multiple news outlets.  
In August the bank featured it on its internal network.


## ▶ SLIDE 5. Who owns the client

That answered who runs a client.  
The harder question is **who owns them**.  
And this workflow I own **end to end**.

*(pause)*

Regulation requires the bank to know who ultimately owns every corporate client.

An analyst read documents in several languages.  
Traced ownership upwards, layer by layer,  
through holding companies, funds and trusts.  
And worked out the percentages by hand, country by country.

Documents conflicted. Evidence was missing.  
One case took **over three hours**.  
And a wrong owner is a regulatory problem.

*(pause)*

So I designed the rules, the architecture, the tests and the deployment.

The AI reads every document, in any language.  
It maps the ownership chart, layer by layer.  
It works out the percentages,  
and identifies the ultimate owners under each country's rules.

Conflicts and gaps are flagged, **never guessed**.  
Every claim carries a quote from a document.  
It checks its own work before any person sees it,  
and automated tests make sure the same case gives the same answer every time.

That is what makes the speed safe.

*(pause)*

A case now takes **five to fifteen minutes**, instead of over three hours.  
At least **thirteen times faster**.  
About **four hundred users** work with it today.  
It covers about **ninety percent** of the clients we check,  
and it frees an estimated **seventy one people's** worth of work every year.


## ▶ SLIDE 6. Whether the paperwork stands up

Both workflows read documents.  
Which brings me to the third question, **the paperwork**,  
and to the core I promised to come back to.

*(pause)*

At the centre is a **state machine** I built.  
It works out where every question and every document stands.  
A question's state decides what evidence we need,  
and when it is ready to be worked.  
A document's state decides whether it can be trusted.

Linking documents to questions was manual.  
I automated the linking,  
and the unlinking that everyone forgets,  
when a newer document supersedes an older one.

A missing document is visible.  
A stale one still looks current,  
and an auditor cannot tell the difference.

So both AI workflows only see work my state machine released,  
and only act on documents it marked good.

*(pause)*

That platform contributed **five million euros** in savings,  
and **forty thousand** document operations now run with no human.  
I still own it in production,  
and when an issue comes up, I am the one who fixes it.

One layer down, all of it travels over messaging, which could not cope.  
Analysts waited **thirty to sixty minutes** for a result.  
I designed a new library with automatic retry.  
The same work now takes **seconds**,  
at **a million messages a day**.


## ▶ SLIDE 7. Beyond my team

All of that sits inside my business unit.

*(pause)*

Beyond it, I contributed a new integration module to **LangChain4j**,  
the open source Java framework our AI platform is built on.  
Giving back to the community we depend on.

Inside the bank, I drive **re-use**.  
My messaging and retry libraries are used across the business unit.  
Nexus AI is now being reviewed **bank-wide**.  
And the shared coding standards I built are the default in every service in our unit.

I taught Nexus AI and PromptLint to the wider organisation.  
**A hundred and forty people** came to my session in June,  
and the recording is still being used.

I mentor engineers through pairing and code review.  
I took part in the bank's hackathon in 2024,  
led a team in 2025,  
and joined the sustainability initiative in 2026.


## ▶ SLIDE 8. Closing

*(pause)*

**I am an engineer.**  
I write the code, I ship it,  
and I own it when it breaks at four in the afternoon on a Friday.

*(pause)*

Who runs a client.  
Who owns them.  
And whether the paperwork stands up.

Two years ago our business unit answered all three by hand,  
and had no AI capability at all.  
Today two AI workflows answer the first two in production,  
and all three stand on the core I built.  
One of them reached the national press.

*(pause)*

That is why I am ready for **Vice President**.

Thank you.
