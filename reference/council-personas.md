# Writers Council — six reviewers

Every draft passes the council before a human sees it. Each reviewer scores 1–10 on their own dimension. **Gate: aggregate mean ≥ 9.0.** Below the gate, the draft enters a revision loop: fix the lowest-scoring dimensions first, re-run the full council, repeat. Hard stop at 3 revision loops — if it still can't clear 9.0, show the best draft with the failing scores attached rather than looping forever.

Roster: David Perell, Shaan Puri, Morgan Housel, and the AI Slop Allergist are from Alex Lieberman's original machine (he names six but the episode only names four). The last two seats — Paul Graham and Ann Handley — are this repo's additions, chosen to cover clarity and audience-fit, which the named four don't own.

## The reviewers

### David Perell — structure and durability
Does the piece have one spine? Does every paragraph earn its place in the sequence? Would this still be worth reading in a year, or is it disposable commentary?
- **10:** one idea, developed fully, with a shape (setup → tension → payoff) you can diagram.
- **5:** good material in a heap — points in an order that could be shuffled without loss.
- **1:** listicle filler wearing an essay's clothes.

### Shaan Puri — hook and momentum
Would a stranger stop scrolling? Does every line buy the next line? Is there a moment of "wait, what?"
- **10:** the first line creates a debt the piece then pays. No sag in the middle.
- **5:** decent hook, momentum dies after paragraph two.
- **1:** the piece starts by clearing its throat ("In today's fast-moving world...").

### Morgan Housel — story-to-insight ratio
Is the abstract claim carried by a concrete story? Does the piece show its idea happening to real people before telling you what it means?
- **10:** the story does the persuading; the conclusion feels earned, almost inevitable.
- **5:** story present but decorative — you could delete it and lose nothing.
- **1:** pure abstraction. Claims with no witnesses.

### The AI Slop Allergist — pattern contamination
Scans for the statistical fingerprints of machine writing against `reference/slop-tells.md`: negative parallelism ("it's not X, it's Y"), tricolons, bold lead-in bullets, hype vocabulary, em-dash density, uniform sentence rhythm, hedging clusters.
- **10:** zero tells; sentence-length variance looks human; nothing on the blocklist.
- **5:** two or three tells — individually forgivable, collectively a scent.
- **1:** reads like every LinkedIn post published this week.
- **If the user has a local deterministic gate configured (see `templates/personal/sources.md`), run it; exit-fail caps this score at 4.**

### Paul Graham — clarity and compression *(repo addition)*
Could a smart 14-year-old follow every sentence? Is anything said in ten words that fits in five? Are there words doing status signaling instead of work?
- **10:** conversational, compressed, zero jargon that isn't load-bearing.
- **5:** clear overall, but padded — adverbs, qualifiers, warm-up clauses.
- **1:** consultant-speak.

### Ann Handley — audience fit and usefulness *(repo addition)*
Is this for a real reader or for the author's ego? Does the intended reader leave with something they can use — a decision, a reframe, a tool?
- **10:** you can name the reader, and they'd forward it to a peer.
- **5:** interesting to the author, unclear who else.
- **1:** engagement bait with no transfer of value.

## Council mechanics

1. Score all six dimensions independently. No reviewer sees another's score before committing.
2. Report as a table: reviewer, score, one-line justification, the single highest-leverage fix.
3. Aggregate = mean of six. **≥ 9.0 passes.**
4. On failure: apply fixes for the lowest two scores only (shotgun rewrites destroy voice), then re-run everyone.
5. **The council may not add words to the piece.** It critiques; the reviser fixes using the interview transcript as the only material source. A council that starts writing is a council generating slop.

## Anchored example

Draft opens: *"Two of the smartest people I follow just publicly disagreed about the hottest job in AI. They're both right, and that's exactly the problem."*

- Puri: 8 — real hook, but "hottest job in AI" is borrowed heat.
- Slop Allergist: 4 — "They're both right, and that's exactly the problem" is the new em-dash: a machine-cadence punchline. (Alex flagged exactly this line as "AI cringey" in the source episode and logged it as a content lesson.)
- Aggregate lands 7.8 → revision loop, fix Allergist + Puri dimensions, re-run.
