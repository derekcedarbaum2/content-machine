# Interview transcript — spike: "We turned off 71% of alerts and incidents went down"

<!-- WORKED EXAMPLE (fictional persona). Shows the artifact /interview produces:
     verbatim Q&A, unpolished. This transcript is the ONLY source corpus /draft may use. -->

**Spike (from Oracle, score 9):** [9] SLACK #eng-postmortems — Quarterly review showed alert volume down 71% after the February pruning project, and Sev-2+ incidents *also* down 40%. why it scores: counterintuitive number pair + lived project + build-vs-buy adjacent.

**Research brief:** skipped — lived experience.

---

**Larry King:** Alerts down 71 percent, incidents down 40. In one or two sentences — why?

**Maya:** Because most of our alerts were about the monitoring system's feelings, not the customer's experience. When everything pages you, the real ones drown, and people learn to swipe pages away like spam. Turning off the noise meant the pages that fired actually got read.

**Michael Barbaro:** Take me to the moment this started. Where were you when you decided to prune 71% of them?

**Maya:** It was a postmortem in January. We'd had a four-hour partial outage and the on-call had gotten 61 pages that night. Sixty-one. And the one that mattered — the one about the queue depth — was number 43. She said in the postmortem, totally flat, "I stopped reading them after twenty." And nobody in the room was surprised. That was the moment. If nobody's surprised that on-call stopped reading pages, your alerting is already off, you just haven't admitted it.

**Tim Ferriss:** What was the actual mechanism of the pruning? Walk me through the process — how did you decide what died?

**Maya:** One rule. For every alert we asked: in the last 90 days, did a human take an action because of this page that they wouldn't have taken an hour later anyway? If no — deleted, not snoozed, deleted. We went from about 1,400 alert rules to a bit over 400. No fancy tooling. A spreadsheet, two engineers, three afternoons.

**Howard Stern:** Come on. You sell a log-analysis tool. Isn't "turn your alerts off" you telling people to use your product less? Say the thing you're dancing around.

**Maya:** The thing I'm dancing around is that most observability vendors get paid by the alert, basically. More rules, more ingestion, more dashboards, bigger bill. So no vendor is incentivized to tell you 71% of your alerts are garbage. I am telling you that, and yeah, it means customers might ingest less. Fine. I'd rather have a customer who trusts their pages than one who's numb and churns in a year. That numbness is the churn.

**Barbara Walters:** What were you afraid of when you deleted a thousand alerts?

**Maya:** Honestly? That we'd miss the big one and it'd be my name on the decision. The first month I kept a private list of deleted alerts I was scared about. Checked it weekly. None of them ever mattered. The fear was inherited from the vendors, not from the data.

---

*Stop-condition check: lived story (61 pages, page #43, the postmortem line) ✓ · falsifiable position (alert volume inversely related to incident response quality; vendors incentivized against pruning) ✓ · 2+ specifics (61 pages, #43, 1,400→400 rules, 90-day rule, 71%/40%) ✓*
