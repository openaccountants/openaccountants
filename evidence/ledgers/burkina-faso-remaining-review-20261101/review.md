# Independent source review: initial frozen candidate

**Verdict: changes required.** The initial frozen follow-on is not accepted until D1–D3 below are repaired. This receipt remains bound to `26e1b85c0cbb72923709586bdaa76b694e9f6873` on `codex/burkina-faso-remaining-guides-2026`, baseline `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. Review date: 1 November 2026. Reviewer: independent Codex agent, not the writer. Applicable AGENTS.md, docs/OWNERS.md and docs/skill-template.md were read. The PDF skill was used for source extraction/layout inspection.

## Source identity and actual scope

Official source: https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf . Cached PDF SHA-256: `a8acc390c74bc605540ad493c09e6f9381b5a20148b8804810a164256f7f8c5c` (recomputed). The fresh web opening timed out; this review binds to the cached official 2026 edition, whose title page identifies the edition/year. It does not claim a fresh successful download.

All 130 ledger rows were checked against the relevant actual French passages, with adjacent taxpayer/expense/exception/payment conditions. `row-checks.json` records 125 PASS, 2 PASS_WITH_EXPLICIT_HOLD and 3 FAIL row verdicts. These are 130 rows, not 130 distinct figures. Each record binds the frozen ledger/row hashes to the relevant article span hash, physical page and raw-extraction line range. Exact quotation matching was checked separately for all 130 rows and passed; it does not replace legal review. Source files/extractions remain outside Git. The complete CGI was not read.

The source reading covered ledger-cited passages within CGI 1–21,23–35,39–56,61–62,71,74,79–82,85–95,97 and its reproduced 2025-0148 order,100,105–119,140–141,196–197,227–233,301,307(1),527–540,671,754–758,760–762 and769, limited to cited rules and neighbouring conditions. The full art. 536 table on rendered printed page 216 and the material art. 757 sanctions page 304 were also visually inspected. No repeated full-source dump is stored.

## Defects

| ID | Frozen location | Finding and required repair |
|---|---|---|
| D1 | corporate Penalties / ledger38; income Penalties / ledger53 | Art757(1)'s200k fine is not unconditional: adjacent757(2) raises it to 500k for loss-making taxpayers and1.5m for convention/temporary-exemption enterprises. Include those branches in both Guides and ledgers. Art757's distinct TP branches must not be conflated with ordinary attachments. Actual source: printed 304, raw 23222–23270. |
| D2 | corporate The base / ledger 13 | The specific art. 56 whole-payment deemed-distribution rule applies to managing associates **of capital companies** and spouses. Current wording drops the legal-form scope. Narrow Guide and ledger. Actual source: printed 35, raw 1990 onward. |
| D3 | corporate baseline 67 / old-topic row 41 | Specific IRCM scope for capital reimbursements and directors' tantièmes/jetons de présence is neither retained nor explicitly held. Generic distribution-filing hold does not cover substantive scope. Restore verified scope or explicitly hold these named topics and correct the destination disposition. |

## Independent checks and preservation

`independent-example-checks.json` contains separate Decimal recomputations of all six cases and their decision assumptions. All match. The supplemental repository checker also reports 3 files / 6 blocks / 0 failures. Payroll's result is illustrative before any unresolved final-tax rounding; it certifies no CNSS rate. Regime-election comparison is limited to the stated taxes.

`preservation-checks.json` records fresh Git reads and full SHA-256 values for all ten Guides, not copied writer booleans. Seven unedited Guides, including the two accepted drafts, are byte-identical to the pinned baseline. All eight legacy CTA suffixes and existing platform fields are unchanged; the accepted two had no CTA marker at baseline and still have none. All 16 prior accepted-review/ledger evidence Git blobs are byte-identical. No earlier review is replaced.

All 348 old-topic line records across eight legacy Guides were independently reconstructed and their baseline digests matched. `old-topic-spot-checks.md` records21 material checks plus the complete three-rewrite body comparison. D3 is the only substantive missing topic group found. Lost content restored by reviewer:0. The Guides grew, so no25% shrink condition is triggered.

The partnership default/election, advances on 15th, allowance 75k/50k/30k caps, IUTS 112 scale, TPA 5,000 acceleration, all CME classes/zones/tariffs, RSI normal SYSCOHADA, combined art. 62 cap, and stated rounding/art. 53-reference holds were checked. All seven domains remain partial. The five legacy 2025 jobs remain unchanged and unfinished. No attestation, full 2026 filing approval, authenticated portal workflow, issue closure or country-completion approval is given. Reviewer made no Guide edits, commit or push. A separate closure will bind any repairs to exact candidate hashes.
