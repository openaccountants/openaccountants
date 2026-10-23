---
name: tax-research-with-your-ai-how-to-do-it-defensibly
description: The method for researching any tax question with the AI you already use, so the answer is citable and reviewable, not just plausible.
jurisdiction: general
category: cross-border
tax_year: 2025
last_updated: 2026-10-21
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tax research with your AI: how to do it defensibly

## Tax research with your AI: how to do it defensibly

This Guide is the method for researching any tax question with the AI you
already use, so the answer is citable and reviewable, not just plausible. It
is the same protocol Open Accountants serves automatically when it is added
to your AI; this is the standalone version anyone can use, on any platform.

## Who this is for

Anyone using AI for a real tax question: taxpayers checking their position,
accountants doing research faster. It does NOT replace advice on unsettled or
high-stakes positions; those end with a licensed professional.

## Before you start, pin down

- One question, one jurisdiction, one tax period. Broad questions produce mush.
- The taxpayer's basic facts: entity type, residency, dates, amounts.

## The method, step by step

1. Make your AI fetch the law, not remember it. Say: "Answer only from
   primary sources you fetch now. No figures from memory." Stale recall is
   the main failure mode; rates and thresholds change every year.
2. Identify the applicable hierarchy in the jurisdiction. Read legislation
   together with valid delegated legislation and binding judicial interpretation;
   do not assume every judgment ranks below every regulation. Separate these
   authorities from administrative guidance and commentary. Explain conflicts
   and seek professional review where their effect is unresolved.
3. Demand pinpoint citations: the section or article number, the official
   URL, and the effective date or tax year, for every figure.
4. Check the AI's homework. Open each cited page and confirm it actually
   says what is claimed. (With Open Accountants added to your AI, this check
   runs automatically against the live source.)
5. Make it state a confidence level per conclusion, and why it is not
   higher. "High, settled law" reads very differently from "Low, conflicting
   authority", and a reviewer needs to know which one they are holding.
6. Watch the calendar. If a budget, finance act, or reform sits between the
   source's date and today, re-pull the source and say so in the answer.
7. Finish with a scope note: what was assumed, what was not covered, and
   what needs professional confirmation before anyone relies on it.

## Australian supplement: a research file note

Use this supplement for Australian tax research. It records the work performed and its limits;
it does not decide the taxpayer's facts, make an election or authorise lodgement. The following
controls were checked against the linked official sources on 21 October 2026.

### Establish the period and authority

- Record transaction dates and the exact income year, entity, residency and question. Distinguish
  enacted law from a proposal and commencement from application to the taxpayer's period. Check
  relevant application, saving and transitional provisions, not only the operative section.
- Record the Federal Register compilation ID and effective period, not only a moving 'latest'
  link. Check for commenced amendments awaiting incorporation and inspect the amending law and
  relevant dates. The Register's latest-version warning can identify such amendments.
  See [Federal Register frequently asked questions](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/frequently-asked-questions).
- Identify each source's legal status. A public ruling binds the Commissioner where it applies
  to the entity and the entity relies on it; it does not bind the courts. A draft public ruling
  is not legally binding, but can provide written-guidance protection on its stated terms. Read
  its reliance notice rather than assuming either binding protection or no protection at all.
  See [TR 2006/10, paragraphs 30 and 39A-39B](https://www.ato.gov.au/law/view/document?DocID=TXR/TR200610/NAT/ATO/00001).
- A practical compliance guideline describes an administrative compliance approach and lacks the
  legally binding effect of a public ruling. Read its own reliance terms and eligibility criteria.
  See [PCG 2016/1, paragraphs 8 and 23-26](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20161/NAT/ATO/00001).
- Edited private advice is historical research material, not a ruling another taxpayer can rely
  on, and is not maintained for later changes. A decision impact statement records the ATO's
  response to a decision; separately read the judgment, appeal status and affected rulings.
  See [PS LA 2008/4, sections 2 and 7](https://www.ato.gov.au/law/view/document?DocID=PSR/PS20084/NAT/ATO/00001)
  and [PS LA 2009/9, paragraphs 187-200](https://www.ato.gov.au/law/view/document?DocID=PSR/PS20099/NAT/ATO/00001).

### File-note template

```markdown
# Australian tax research file note
Question and decision required:
Taxpayer facts and evidence supplied:
Period, transaction dates and relevant application provisions:
Missing facts and assumptions requiring confirmation:

## Source register
| Proposition | Source / pinpoint / official link | Version / effective period / date read | Status and reliance terms | Supports the proposition? |
| --- | --- | --- | --- | --- |

## Analysis
Apply each relevant condition to an evidenced fact. Identify conflicting authority,
alternative interpretations, adverse authority and unresolved factual conditions.

## Conditional position for review
Conclusion and supporting source references:
What changes the conclusion:
Unavailable sources, unperformed checks and unresolved issues:
Evidence or specialist review required, owner and next action:
Reviewer decision and date (leave pending until actually obtained):
```

### Fabricated acceptance cases

1. A proposition depends on a subsection that the researcher cannot retrieve. Record the exact
   unavailable authority, the access limitation and the next retrieval step. Do not invent its
   wording, cite a search snippet as a completed source check or label the position confirmed.
   Continue analysis that the available evidence supports, with the dependency unresolved.
2. An RCTI question concerns an invoice issued in August 2026, but the draft memo cites GSTR 2000/10
   as current law. The [withdrawal notice](https://www.ato.gov.au/law/view/document?DocID=GST/GSTR200010/NAT/ATO/00001)
   limits its continuing application to RCTIs issued on or before 14 June 2023. Retrieve the
   [2023 determination](https://www.legislation.gov.au/F2023L00785) for the later invoice and label
   [GSTR 2026/D2](https://www.ato.gov.au/law/view/document?DocID=DGS/GSTR2026D2/NAT/ATO/00001)
   as a draft with its own reliance terms. Leave unresolved factual eligibility for review.
3. A well-cited note has no recorded reviewer decision. Deliver it as a conditional position with
   review pending. Do not manufacture sign-off or call the taxpayer's treatment approved merely
   because all links resolved.

## The traps

- Confidently wrong, beautifully formatted: a perfect-looking memo citing
  law that no longer exists. This is the number one AI tax failure; steps 1
  and 6 are the defense. In our testing, an AI without these guardrails
  applied superseded law to a 2025 question while scoring near-perfect on
  citation formatting.
- Citations to real pages that do not say that. Step 4 catches these; a
  citation nobody checked is a liability wearing a suit.
- One uniform confident tone across settled and unsettled points. Step 5
  forces the honesty a professional reviewer expects.

## When to hand it to a human

Unsettled law, elections, filings, or anything you will rely on financially:
confirm with a licensed accountant before acting. Open Accountants routes
this to a named professional from inside your AI.

## Sources

- The method and its test results: https://www.openaccountants.com/blog/confidently-wrong-beautifully-formatted
- Add Open Accountants to your AI: https://www.openaccountants.com/connect

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
