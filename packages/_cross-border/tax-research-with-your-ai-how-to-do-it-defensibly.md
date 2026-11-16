---
name: tax-research-with-your-ai-how-to-do-it-defensibly
description: The method for researching any tax question with the AI you already use, so the answer is citable and reviewable, not just plausible.
jurisdiction: general
tax_year: 2026
last_updated: 2026-11-15
source_checked: 2026-11-15
version: 1.0
type: router
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Tax research with your AI: how to do it defensibly

## Scope

Use this research protocol with the AI you already use to produce a citable,
reviewable tax working paper. It serves taxpayers and accountants. It routes
research, source checks and professional review; it supplies no tax rate,
computation, election or filing authorisation. Unsettled or high-stakes positions
need a qualified professional in the relevant jurisdiction.

The standalone method can be followed on any platform. Actual source access and
tool availability must be checked in the session. Connecting OpenAccountants does
not prove that every assertion was automatically compared with live law or assign
a professional to the case. See the source/version boundaries below.

## Ask the client first

- Pin down one question, jurisdiction and tax period; split a broad question into
  explicit issues. Cross-border questions need the relevant jurisdictions and
  separate domestic/treaty interactions.
- Establish entity type, residency, transaction dates and amounts from the actual
  evidence. Identify missing facts and conclusions that depend on them. Do not
  ask again for facts already available in the case record.

## The method, step by step

1. Make your AI fetch the law, not remember it. Say: "Answer only from
   primary sources you fetch now. No figures from memory." Record the text actually obtained, its applicable version and the date read.
   Rates, thresholds and other rules can change; a familiar citation is not proof
   that its current or historical wording applies to this period.
2. Identify the applicable hierarchy in the jurisdiction. Read legislation
   together with valid delegated legislation and binding judicial interpretation;
   do not assume every judgment ranks below every regulation. Separate these
   authorities from administrative guidance and commentary. Explain conflicts
   and seek professional review where their effect is unresolved.
3. Demand pinpoint citations: the section or article number, the official
   URL, and the applicable effective date or tax year, for every rule, figure,
   exception and deadline. Read operative paragraphs and adjacent exceptions;
   distinguish a proposal, commencement and the period to which a rule applies.
4. Check the AI's homework. Open each cited page and confirm it actually
   says what is claimed for these facts and this period. Record actual access
   failures and unperformed checks; a search snippet, error or challenge page is not
   a completed source read. Ask the AI to do the checking it can perform, then have
   the reviewer inspect the evidence. Never describe an unavailable check as run.
5. Make it state a confidence level per conclusion, and why it is not
   higher. "High, settled law" reads very differently from "Low, conflicting
   authority", and a reviewer needs to know which one they are holding. Explain
   source and factual gaps as well as legal uncertainty; confidence is not an
   independent accuracy score or a legal penalty/reliance standard.
6. Watch the calendar. If a budget, finance act, or reform sits between the
   source's date and today, re-pull the source and say so in the answer.
7. Finish with a scope note: what was assumed, what was not covered, unavailable
   sources, unresolved conflicts and what needs professional confirmation before
   reliance. Keep source verification and any actual professional sign-off separate.

## Australian supplement: a research file note

Use this supplement for Australian tax research. It records the work performed and its limits;
it does not decide the taxpayer's facts, make an election or authorise lodgement. The original supplement recorded a 21 October 2026 source check. This revision
reads the specific sources/scopes listed below on 2026-11-15; that read date does
not assert that every underlying Australian tax rule or taxpayer treatment was checked.

### Establish the period and authority

- Record transaction dates and the exact income year, entity, residency and question. Distinguish
  enacted law from a proposal and commencement from application to the taxpayer's period. Check
  relevant application, saving and transitional provisions, not only the operative section.
- Record the Federal Register compilation ID and effective period, not only a moving 'latest'
  link. Check for commenced amendments awaiting incorporation and inspect the amending law and
  relevant dates. The Register's latest-version warning can identify such amendments.
  See [Federal Register frequently asked questions](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/frequently-asked-questions).
- Identify each source's legal status. A public ruling binds the Commissioner where it applies
  to the entity and the entity relies on it. Keep that administrative binding effect
  separate from binding judicial interpretation; do not treat a public ruling as a
  court judgment. A draft public ruling
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

### Research route checks (fabricated scenarios)

1. A proposition depends on a subsection that the researcher cannot retrieve. Record the exact
   unavailable authority, the access limitation and the next retrieval step. Do not invent its
   wording, cite a search snippet as a completed source check or label the position confirmed.
   Continue analysis that the available evidence supports, with the dependency unresolved.
2. An RCTI question concerns an invoice issued in August 2026, but the draft memo cites GSTR 2000/10
   as current law. The [withdrawal notice](https://www.ato.gov.au/law/view/document?DocID=GST/GSTR200010/NAT/ATO/00001)
   withdraws it from 29 July 2026 and limits its continuing application to RCTIs
   issued on or before 14 June 2023. It does not apply from 15 June 2023 onward. Retrieve the
   [2023 determination](https://www.legislation.gov.au/F2023L00785) for the later invoice and label
   [GSTR 2026/D2](https://www.ato.gov.au/law/view/document?DocID=DGS/GSTR2026D2/NAT/ATO/00001)
   as a draft with its own reliance terms. Its current notice conditions interest/penalty
   protection on applicability and reasonable good-faith reliance; the correct tax may
   still be payable. Read the determination and every relevant condition before deciding
   eligibility; this research example does not approve an RCTI or input tax credit.
3. A well-cited note has no recorded reviewer decision. Deliver it as a conditional position with
   review pending. Do not manufacture sign-off or call the taxpayer's treatment approved merely
   because all links resolved.

## The traps

- Confidently wrong, beautifully formatted: a perfect-looking memo citing
  a superseded version of law. Steps 1 and 6 address that risk. The original
  historical testing example is retained in the source note below; it does not
  establish a current model error rate or guarantee that following the protocol
  makes a position correct.
- Citations to real pages that do not say that. Step 4 catches these; a
  citation nobody checked is a liability wearing a suit.
- One uniform confident tone across settled and unsettled points. Step 5
  forces the honesty a professional reviewer expects.

## When to refuse or refer

Unsettled law, elections, filings, or anything you will rely on financially:
obtain review by a suitably qualified licensed professional before acting. Record
review as pending until actually obtained. A user can request professional help;
availability, scope and responsibility require a separate engagement. An AI answer,
resolved links or a connected skill is not an engagement or approval.

## Sources

| Source | Read for | Actual read date and boundary |
|---|---|---|
| [Federal Register FAQ](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/frequently-asked-questions) | Read for: Register/title/compilation IDs, latest versus historical versions, unincorporated commenced amendments and effective/commencement distinction | 2026-11-15, relevant FAQ entries and adjacent explanations. Registry method, not approval of a taxpayer's substantive law. |
| [TR 2006/10](https://www.ato.gov.au/law/view/document?DocID=TXR/TR200610/NAT/ATO/00001) | Read for: Public-ruling status/reliance and applicable class/period, paragraphs 28–39C including draft protections; current version history | 2026-11-15, ordinary browser recovered the 25 February 2026 version after direct fetches failed. An older PDF was rejected as evidence of the new draft paragraphs. |
| [PCG 2016/1](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20161/NAT/ATO/00001) | Read for: Nature of compliance guidance, status and reliance; paragraphs 8 and 20–27, including eligibility/good faith and change-of-view terms | 2026-11-15, ordinary browser and official five-page PDF read. Not a statement that a particular taxpayer qualifies for a safe harbour. |
| [PS LA 2008/4, official PDF](https://www.ato.gov.au/law/view/pdf?DocId=PSR%2FPS20084%2FNAT%2FATO%2F00001&PiT=99991231235958&filename=law%2Fview%2Fpdf%2Fpsr%2Fps2008-004c10.pdf) | Read for: Sections 1–2 and 7: edited advice as historical record, nonreliance and no update for later law/application | 2026-11-15, actual official PDF identifies version published 22 May 2025. Direct HTML/browser access denied; no claim to have opened a later version. |
| [PS LA 2009/9](https://www.ato.gov.au/law/view/document?DocID=PSR/PS20099/NAT/ATO/00001) | Read for: Paragraphs 187–200: DIS purpose, final/interim context, affected views and limits, including not a public ruling or proxy amendment | 2026-11-15, ordinary browser read after direct fetch failed. Other litigation procedures are outside this skill. |
| [GSTR 2000/10 withdrawal](https://www.ato.gov.au/law/view/document?DocID=GST/GSTR200010/NAT/ATO/00001) | Read for: Whole withdrawal notice, paragraphs 1–4: withdrawal and invoice-date boundary | 2026-11-15, ordinary browser. Date example only; no substantive RCTI eligibility clearance. |
| [2023 RCTI determination](https://www.legislation.gov.au/F2023L00785/asmade/2023-06-14/text/original/epub/OEBPS/document_1/document_1.html) | Read for: Sections 1–9: identity, commencement, authority, definitions, eligibility, agreement and compliance conditions; repeal schedule identified | 2026-11-15, actual instrument text and Register in-force/version identification. Eligibility must be tested on the real facts. |
| [GSTR 2026/D2](https://www.ato.gov.au/law/view/document?DocID=DGS/GSTR2026D2/NAT/ATO/00001) | Read for: Reliance notice, paragraphs 1–9, date-of-effect and draft/final distinction | 2026-11-15, ordinary browser. Preliminary view; detailed RCTI transaction treatment is outside this protocol. |
| [Original method/testing account](https://www.openaccountants.com/blog/confidently-wrong-beautifully-formatted) | Read for: Historical source-check protocol, outdated-law failure, benchmark limits and separate professional-engagement note | 2026-11-15. Publisher's own small experiment, not independent proof of accuracy. No tax treatment from that blog is used here. |
| [Add OpenAccountants to your AI](https://www.openaccountants.com/connect) | Read for: Connection page and separate-engagement/general-reference boundary | 2026-11-15. Setup details depend on the actual host application; no live execution of a source check was tested here. |

The original testing anecdote concerned an AI applying superseded law to a 2025
question while scoring well on citation formatting. The linked publisher report
describes a small, selected, internally judged experiment. Treat it as a historical
illustration of why version checks matter, not evidence that a model or this protocol
is universally accurate. Its generic ordering of statute, regulations and case law
does not override the jurisdiction-specific hierarchy required above.

Not yet confirmed: no specific taxpayer conclusion, election, filing, penalty protection or professional sign-off is established by this research protocol. Current source access must be demonstrated on each actual question. The former claims that adding OpenAccountants always performs automatic live verification, that the standalone text exactly matches the current served protocol and that an accountant is automatically assigned are not established here and are not usable assurances. No live public tool catalogue or current AI model performance was tested; historical experimental observations do not establish a general error ranking. The PS LA 2008/4 PDF was read in its identified 22 May 2025 version; a later revision, if any, was not independently recovered. Any source or fact missing in the actual matter remains an explicit dependency, not a reason to invent wording or sign-off.

> Contributed by Ryan Duguid.
