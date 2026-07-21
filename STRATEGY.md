# The Content Machine Strategy

This is the strategy behind the software. The skills in this repo automate a content process, but the process only matters because of a thesis about where durable advantage comes from now. Source: Alex Lieberman's July 2026 appearance on Lenny's "How I AI" ([episode](https://www.lennysnewsletter.com/p/how-i-ai-how-the-founder-of-morning), [video](https://youtu.be/1_jlukb7gm4)), plus the implementation decisions made in this repo.

## The thesis: distribution is the moat

AI commoditizes technology. Whatever you build, a competitor can build faster next quarter. As product moats thin out, the moats that remain are the ones AI can't copy, and trusted distribution sits at the top of that list. An audience that reads you because they trust you compounds, and can't be cloned by a model.

The conclusion Lieberman draws: every company should build a media company on top of its business. Not a blog with a posting quota. An actual media operation, with the founder and employees as the talent.

Two problems block this in practice:

1. **The founder is capped.** Lieberman spends maybe 25% of his time on content and can't spend more. The question isn't "more hours." It's more output per hour without quality collapse.
2. **Employees don't create.** Not because they lack expertise. The activation energy is brutal on top of a full-time job, and the blank page is the moat around their expertise.

The machine attacks both. It makes the founder's content hours dramatically more productive, and it lowers the employee's cost of creating to roughly "answer five questions out loud."

## Climb Cringe Mountain

The cultural prerequisite. Posting about yourself and your work feels cringe, so most experts don't, so the people who do post own the conversation. Claire Vo's framing on the episode: as a bootstrapped founder you must climb Cringe Mountain. Post anyway, through the discomfort, until it stops being discomfort. Lieberman's position is the same but blunter: "if you build it, they will come" is dead now that distribution beats product. Shots on goal matter more than dignity.

If you're sharing this doc with a team: this section is the actual blocker. The software is easy. The willingness is the work.

## Why AI content usually fails, and the design answer

Out of the box, AI is a bad writer in a specific way: a model trained on the whole internet writes, by definition, the average of the internet. Lulu Meservey's line is that AI raises the floor of bad writers and caps the ceiling of great ones. She's right *if* you let the model draft from its own head.

The machine's answer is architectural, not prompt-engineering:

**Writing is a multi-step process, and AI belongs in different roles at different steps.** Map your workflow first, then decide per step whether AI drives, assists, or stays out. This generalizes: map any workflow before you automate it, and design for the ideal process with no constraints, not your current one.

**The model never generates substance.** Substance comes from you, extracted by interview. The drafting step may only use words from your interview transcript. The writer "shapes clay," it doesn't make clay. If the piece is thin, you were thin in the interview. Lieberman: AI slop is people pointing the finger at themselves.

**Quality is gated, not hoped for.** A six-persona council scores every draft. Below 9/10 aggregate, it revises. Personas exist because "make it better" is not a gradient. "Would Morgan Housel say the story carries the insight?" is.

**The system learns your taste, permanently.** Every edit you make becomes a candidate lesson, and approved lessons are checked on every future draft. This is the compounding asset. A generic model is everyone's writer. Your lessons file makes it yours.

## The machine, end to end

1. **The Oracle.** Scans the last 7 days of your systems of record (Slack, email, meeting notes, task trackers) plus an "internet reader" of accounts and sites you follow. Scores candidate "content spikes" on story, POV, specificity, novelty, and timeliness, then returns 10 to 15 a day, half internal, half internet. Every spike lands in a Spike Vault whether you use it or not: an idea inventory that means you never start from blank. Lieberman calls this step the most valuable thing in the system even if you never let AI draft a word.

2. **Research assistant** (optional). For spikes about external debates: what the principals said, the strongest version of each side, the contrarian angles still unclaimed, the open questions you could be the one to answer.

3. **The interview panel.** Six interviewer personas (Tim Ferriss, Joe Rogan, Michael Barbaro, Barbara Walters, Howard Stern, Larry King) question you one at a time, each with a different extraction job: mechanism, story, stakes, the unguarded quote, the compressed thesis. You answer by voice. Speed produces unguarded phrasing, and unguarded phrasing is where voice lives. The transcript becomes the piece's entire source corpus.

4. **Drafting in your codified voice.** Three personal files steer it: a profile (who you are, what you promote), a voice guide built by studying your ten best-performing posts (your hook formulas, your structures, your #1 rule; Lieberman's is "write like you're texting a friend"), and your accumulated content lessons. Output includes multiple hooks and closings to pick from.

5. **The writers council.** David Perell (structure), Shaan Puri (hook and momentum), Morgan Housel (story-to-insight ratio), an AI Slop Allergist (pattern contamination), plus two additions from this repo: Paul Graham (clarity) and Ann Handley (audience fit). Independent 1 to 10 scores, and an aggregate under 9.0 triggers a revision loop.

6. **The lessons loop.** After you finalize, the machine diffs its draft against what you actually published, abstracts generalizable rules from your edits, and asks permission to log them. On the episode, Lieberman catches a setup-punchline draft line ("they're both right, and that's exactly the problem"), calls the construction "the newest em-dash," and logs it. That's the loop working.

7. **Repurpose and distribute.** The anchor piece fans out into format-native derivatives (Gary Vaynerchuk's content pyramid), each derivative carrying one shard, matching how you historically write in that format, and passing the same council gate.

## The human layer: employees as the distribution channel

The machine scales one person. The strategy scales the company, and this part isn't software.

**Employee advocacy is the most underpriced channel available.** Most CEOs fear giving employees a megaphone because someone might get recruited. Lieberman's counter (and Claire's): suppressing your people's public profile is exactly what pushes them out. Enabling it is a retention benefit and a hiring magnet. Look at Anthropic. Engineers with public voices became extensions of the brand, and people trust the product more because individuals, not the logo, talk about it.

**The precedent.** At Storyarb, Lieberman ran "Own the Internet": a roughly 6-week campaign, everyone encouraged to post on LinkedIn, prize money for the winner, one rule that half your content stays within the company's domain. It drove 40% of all inbound leads that quarter, plus hiring top-of-funnel.

**The playbook (the "Creator Cup").** A month-long, points-based posting game:

- 10 points per post, 3 points for engaging with a colleague's post
- A shared channel ("Reply Guys") where everyone sees everyone's posts
- Weekly editor's pick: +50 points
- Weekly games. Example: "Full House," where if 70% of the company posts this week, a prize unlocks for a random participant
- Around $5,000 in monthly prizes, structured so playing at all can win, not just the impressions leader

The design principle: make participation feel winnable for non-creators, not a leaderboard for the one person who was already internet-famous. And the machine is what makes participation cheap. An employee's path to a post is: pick a spike the Oracle found, answer five interview questions out loud, approve a draft.

**The math for a bootstrapped company.** No lab-scale gravitas, no TechCrunch cycle, no VC signal boost? Your top talent showing their work in public is the substitute. If a $5,000 Creator Cup produces one engineering hire, it beat a recruiting agency by an order of magnitude. Leads are upside.

## Operating cadence

- **Daily:** run the Oracle. Two minutes to read 15 spikes. Even used purely as an idea feed, it kills the blank page.
- **2 to 3 times per week:** full pipeline on one spike, interview to published anchor.
- **Between:** repurpose. The Oracle also resurfaces old anchors whose topic reignited. An old piece plus a fresh hook is the cheapest good post you'll ever ship.
- **Always:** the lessons loop. Skipping it turns a compounding system back into a commodity one.

## When the machine fights you

From the episode, Lieberman's honest failure modes, worth adopting as policy:

- If a draft is taking longer to fix than to write, write it by hand. The machine is a tool, not a religion.
- If it repeats a mistake you already logged, stop and debug the lessons file. That's the one unforgivable error, because it means the compounding loop is broken.

## What to steal even if you build nothing

1. Map your content workflow before touching AI. Most of the waste is visible without any model.
2. Interview yourself instead of prompting a draft. The transcript-only rule is portable to any tool.
3. Codify your voice from your ten best posts, in a file. Aspirational self-description lies; the corpus doesn't.
4. Keep a lessons file and make every tool you use read it.
5. Run the employee campaign. It's a spreadsheet and prize money, and it built 40% of a quarter's pipeline at a real company.
