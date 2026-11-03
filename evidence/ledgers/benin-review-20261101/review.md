# Independent Benin pack review, 1 November 2026

**Result: changes required within the requested preparation scope.** The frozen pack is not approved yet. All 113 ledger rows were checked against their actual official sources and all 16 examples recomputed. The disclosed partial scope is appropriate. Two operative trigger/condition omissions and eight short descriptions need correction. No comprehensive country coverage, authenticated filing or accountant attestation is approved.

Reviewed candidate: `a61fda399fa613455862d3cc72d5c403cd330ccc`. Pinned comparison base: `a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297`. The candidate hashes match the writer's initial `candidate-hashes.json`. I did not write the Guides, change their text, alter a ledger/topic map/writer record, change refs, commit, push, publish or attest. Only this new review-evidence directory was added. No moving `origin/main` comparison was used.

## Required repairs

| ID | Location at frozen candidate | Finding and concrete repair | Source |
|---|---|---|---|
| F1 | `skills/benin/bj-*.md:3`, every one of eight descriptions | The frontmatter specification requires 80–150 words. These descriptions contain 35–46 words. Expand each to 80–150 useful words covering its bounded job, taxpayer/period and search triggers. The passing validators do not establish compliance with this prose-length requirement. Counts: formation 38; corporate 37; cross-border 38; income 42; payroll 46; overview 45; TP 35; VAT 46. | `docs/skill-template.md`, Frontmatter spec, description row |
| F2 | `skills/benin/bj-cross-border-withholding.md:30`, `:37`, `:46`; corresponding ledger row 7 | The ordinary-interest workflow does not state the second statutory tax trigger. CGI 85(2) makes interest tax due from payment **or** a debit/credit accounting entry in the debtor's books or creditor's account, including amounts not yet paid. Merely asking for expense/payment dates, then describing putting products into payment in the deadline paragraph, leaves booked but unpaid interest untreated. Add the explicit accounting-entry trigger beside the interest/base rule and distinguish it from the distribution/meeting and service-expense rules. Read the tax trigger with article 91's remittance provision; do not replace it with a cash-only rule. The 15% rate itself is correct. | [CGI 2026 arts. 85(2), 88, 91](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=48). Article 85's decisive short text: « même si les sommes concernées ne sont pas encore payées ». |
| F3 | `skills/benin/bj-transfer-pricing.md:45`; corresponding ledger row 10 | The two/four-month audit rule omits the definition determining the FCFA 2bn limb. LFR 17 defines declared annual turnover using the amount declared for any tax in any year under audit, including the current year. State that definition beside the duration rule so the reader does not select only one favourable year or one return. The two/four-month limits, possible further four months, qualifying reasons and three-day reasoned notice are otherwise correct. | [Signed LFR 2026-10 art. 17, amended CGI 539(2), PDF p.5](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf#page=5). Its final sentence, including « l'une quelconque des années sous contrôle, y compris celle en cours », was visually checked. |

F2/F3 are narrow repairs to jobs the Guides actually describe. They do not require the author to turn these partial preparation Guides into a whole-law or authenticated-return manual. No further numeric-rate error was identified in the other ledger rows within the scope reviewed.

## Preservation and minor map corrections

The six legacy files remain. All six platform CTA tails are byte-identical to the pinned base. All existing platform/human fields checked, including absent/present `verified_by`, `reviewed_by`, `reviewed_on`, team attribution, licence and review-status fields, are unchanged. Both new Guides have no platform-owned fields. Eight current-year integer tax years and tier 2 values pass strict parsing. Every legacy candidate is longer than its baseline; the >25% shrink condition does not arise. **Lost content restored by reviewer: 0.** Unsupported legacy figures are kept as named unresolved topics or replaced from actual law, rather than silently passed off as current.

There are exactly 81 original heading/bold-topic map rows: income 15, VAT 12, corporate 16, formation 13, overview 13 and payroll 12. All original strings occur in the map. Semantic spot-checks covered the salary bands/residence/family quotient/CNSS deduction/annual IRPP, VAT threshold/reverse charge/digital services/inputs, corporate minimum/mining/hydrocarbons/dividend-listed/royalty/treaty/instalments, formation capital/audit/annual accounts, overview deadline/regional routing and the full legacy CNSS group. The replacement/deferred content is present in the corresponding Guide bodies/Sources.

Several map anchors land in a scope/rates section rather than the actual destination rule. These are navigation defects, not lost substantive content. Correct them while repairing the batch:

| Map line | Legacy topic | Correct target section |
|---:|---|---|
| 32 | Reverse charge on imported services | `bj-vat-gst.md#cross-border-points` |
| 33 | Foreign digital / e-services | `bj-vat-gst.md#cross-border-points` |
| 34 | Input VAT recovery | `bj-vat-gst.md#the-base` |
| 42 | Corporate tax base | `bj-corporate-income-tax.md#the-base` |
| 49 | Corporate advance payments | `bj-corporate-income-tax.md#deadlines-and-filing` |
| 72 | Overview corporate annual-return deadline | `bj-corporate-income-tax.md#deadlines-and-filing` |

## Independent source work

I read `CLAUDE.md`, `docs/skill-template.md`, `docs/OWNERS.md` and the supplied firm/project instructions. I independently fetched all ten source captures from their cited official public hosts and compared SHA-256 hashes. All ten fresh HTTP 200 bodies are byte-identical to the captured sources. The initial sandbox DNS failures and subsequent successful network fetches are separately recorded; the failures are not passed off as successful reads. No secondary summary was used as tax authority, and no credentials or authenticated portal were used.

- CGI 2026: every CGI article identified by the 90 CGI ledger excerpts was read with the operative surrounding text, plus directly linked adjacent provisions needed to assess conditions: arts. 1, 3–6, 8–9, 20, 30, 36, 43, 45–47, 49–52, 54, 85–86, 88–91, 101, 119–129, 141–143, 145–146, 191–195, 223–230, 233–238, 240–241, 243–245, 247–249, 252–254, 258–260, 262–263, 470–472, 485, 487–488, 492, 496 and 542–544. Fresh `pdftotext -layout` extraction is byte-identical to the private CGI text. Rendered PDF pages 62, 63, 203 and 239 were additionally visually checked. The cover consolidates the December 2025 original finance law, not the June law.
- Signed LFR 2026-10: tax articles 1–19 read in OCR with the corresponding signed scan pages 1–6, and final articles 48–49/signature on page 17 visually checked. Article 1's exercise-closed-31-December-2025 income rule and contrary-measure exception are correctly preserved. The distribution changes in arts. 3–7, gain/rent/platform changes in arts. 12–14 and audit-duration art. 17 were compared to the Guide text. No whole-budget-table review is claimed.
- Original signed LF 2025-22: relevant first-declaration relief, gas/cylinder and motorcycle/battery relief, preserved separate levies, BTP fuel deduction and refund provisions read in OCR, and tax scan pages 2–5 visually checked. The draft properly avoids the CGI's stale 2024 relief footnote. No other-year summary supplied the 2026 relief.
- National decree 2014-220: arts. 1–11 read from signed scan pages 2–4. Signature is 26 March 2014, and art. 11 commencement is 5 May 2014. Freely set capital, private statutes and deposit/receipt rules agree. Annex model statutes were not fully reviewed.
- OHADA AUSCGIE: arts. 140, 309–311-1, 376, 387–389 and 694 read in actual extracted text and surrounding paragraphs. Pages 77, 93 and 95 visually checked for half/quarter cash and two-of-three audit thresholds; fresh extraction is byte-identical. Article 389 continues onto the next page and gives three years from RCCM. The statute correctly takes priority over the conflicting portal comparisons.
- Five APIEx public HTML pages: company, prices, process, certificates and required pieces were independently fetched and the relevant public packet/fee/target/stages/identifier text read. No authenticated upload, checkout, completion or certificate was obtained.

The review's article/source scope is explicit; fetching an entire PDF did not mean reviewing every page. The 113 individual dispositions, including source URL/article and condition checks, are in `row-checks.md`. Two rows need the F2/F3 repairs; XB ordinary-deadline row 11 must also be read with F2. No new review against uncited secondary summaries was substituted for a ledger check.

## Arithmetic and mechanical checks

All **16** `oa-check` blocks were independently evaluated with Decimal arithmetic from their inputs/steps and matched all stated expected outputs. The repository example checker separately reports `checked 8 files, 16 oa-check blocks, 0 failures, 0 missing`. Key totals independently reproduced:

| Guide | Recomputed results |
|---|---|
| Salary | 16,500 ordinary ITS; 101,500 band tax + 3,000 June levy = 104,500 |
| Corporate | IS 3,000,000 / 250,000; separate-levy totals 3,004,000 / 254,000 |
| VAT | 1,800,000 output − 720,000 eligible input = 1,080,000; BTP 162,000 allowed / 18,000 excluded |
| VPS | 80,000; school 30,000 with evidence versus 40,000 without, difference 10,000 |
| Formation | SARL paid capital 1,000,000 + fee 22,000 = 1,022,000; SA 2,500,000 + 37,000 = 2,537,000 |
| Overview | Known DGI cash subtotal 1,204,500; supported VAT cash 350,000; unsupported deduction understates by 150,000 |
| TP | 12,000,000 versus 10,000,000 costs, candidate difference 2,000,000; threshold shortfall/excess 100,000,000 / 200,000,000 |
| Withholding | 50,000 / 100,000 ordinary dividend alternatives; 200,000 / 1,000,000 mixed-contract alternatives, difference 800,000 |

Scoped `skill_checks.py`: all 15 checks pass on all eight Guides. Pinned `validate-guides.py` adapter: 0 errors and one warning group, the known heuristic overlap between cross-border withholding and VPS payroll jobs. Both whitespace checks pass. These mechanical successes do not cure F1–F3. Full argv/stdout/stderr/exits, descriptions, metadata/CTA/base hashes and every executable expected-value comparison are in `mechanical-preservation.json`. The reviewer check script initially needed a local parser-shape correction before producing that receipt; no candidate content changed.

## Residual gaps and acceptance boundary

All seven README domains remain partial. The CNSS source/access problem is not a reason to reuse stale social rates: no current CNSS percentage/base/ceiling/deadline was verified or approved in this review. The VAT numerical threshold order, personal non-salary/benefit/exceptional-pay live calculations, complete corporate adjustments/incentives/sectors, actual treaty entitlements, retained-profit transitions, gain/rental-platform calculations, current TP forms/documentation order/CbCR exchange-secondary details and authenticated filing/registration remain expressly open. The ambiguous CGI 496(6) annual-TP versus article-471 reference was observed in the statute itself; withholding a fixed fine is appropriate.

After the author repairs F1–F3 and the map targets, an independent check of those deltas and a fresh scoped validation is required. Preserve this initial failed review and its source/mechanical receipts. The supported remainder does not need a whole-pack rewrite. No professional accountant review or attestation is represented by these findings.
