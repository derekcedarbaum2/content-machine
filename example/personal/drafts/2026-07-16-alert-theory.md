---
transcript: transcripts/2026-07-16-alert-theory.md
format: long LinkedIn
council_aggregate: 9.2
revision_loops: 1
---

# Draft — "We turned off 1,000 alerts" (long LinkedIn)

<!-- WORKED EXAMPLE (fictional persona). Shows the artifact /draft produces:
     final draft, hook/closing options, council scorecard. Note every body
     sentence traces to the transcript; only hooks and closers are new. -->

## Final draft

We deleted 1,000 of our 1,400 alert rules. Incidents went down 40%.

In January we had a four-hour partial outage. On-call got 61 pages that night. The one that mattered — queue depth — was number 43. In the postmortem she said, totally flat: "I stopped reading them after twenty."

Nobody in the room was surprised. That was the moment. If nobody's surprised that on-call stopped reading pages, your alerting is already off. You just haven't admitted it.

The pruning took a spreadsheet, two engineers, and three afternoons. One rule: in the last 90 days, did a human take an action because of this page that they wouldn't have taken an hour later anyway? If no — deleted. Not snoozed. Deleted.

I kept a private list of the deleted alerts I was scared about. Checked it weekly. None of them ever mattered. The fear was inherited from the vendors, not from the data.

And yes, I sell a log tool, and no vendor is incentivized to tell you 71% of your alerts are garbage. More rules, more ingestion, bigger bill. I'd rather have a customer who trusts their pages than one who's numb. That numbness is the churn.

## Hook options offered

1. "We deleted 1,000 of our 1,400 alert rules. Incidents went down 40%." — *two-number collision* ✅ chosen
2. "On-call got 61 pages the night of our worst outage. The one that mattered was number 43." — *two-number collision, story-first*
3. "Your on-call didn't miss the page. Your on-call stopped reading pages months ago." — *reframe one-liner*

## Closing options offered

1. "That numbness is the churn." ✅ chosen (transcript-native)
2. "(The spreadsheet is still our most profitable piece of infrastructure.)" — *parenthetical joke*

## Council scorecard (final loop)

| Reviewer | Score | Note |
|---|---|---|
| Perell | 9 | One spine: noise → numbness → trust. Vendor turn earns its place. |
| Puri | 9 | Collision hook lands; no mid-piece sag. |
| Housel | 10 | Page #43 and the flat quote do all the persuading. |
| Slop Allergist | 9 | Loop 1 killed "the real ones drown in a sea of noise" (cliché) and an invented "here's the uncomfortable truth" lead-in. Clean now. |
| Graham | 9 | Fragments doing real work. "Not snoozed. Deleted." is the compression benchmark. |
| Handley | 9 | Staff-SRE reader leaves with a runnable rule (90-day test). Forwardable. |

**Aggregate: 9.2 — pass** (loop 1 aggregate was 8.5; fixed Allergist 6 + Puri 8, re-ran all six).
