# Independent review: monthly Prehľad sanction delta

**PASS for this frozen delta. No actionable substantive findings.**

Reviewed on 27 October 2026 by a separate AI reviewer who did not author this amendment. This is advisory source review, not accountant attestation and not a Slovakia country-pack PASS. No Guide, README or Git edits were made by this reviewer.

Frozen worktree HEAD: `1cbc9afd9e2e8d0a5a43d66637d2384ced589e69`.
Guide: `skills/international/slovakia/sk-payroll-social.md`, v0.5, **41,249 bytes**,
SHA-256 `8e4902cd4f0b56f2f1ee603ed1c037a7ac5b6b7e20e768a6debee5bada8a263d`.
Baseline v0.4: 36,653 bytes, SHA-256 `8268d19f9e76db76470ed913bb6c06b3766fed5e83319cf8595481d4e638da58`. Its entire bytes equal the committed HEAD Guide; the current amendment remains a working-tree delta at review time.

## Independent source conclusions

| Proposed method | Result and primary basis |
|---|---|
| Monthly filing versus annual return | Correct. ITA §39(9)(a), (11), (12), §49(2): the monthly summary has the end-of-next-month deadline and a no-employment-income-paid exception. The annual Hlásenie is expressly treated as a tax return; the monthly summary is not given that status. Employment income with no advance payable does not automatically erase monthly filing. A payout request can itself require the form; no-income status is not an instruction to ignore a requested payout. |
| Special five-day sanction gateway | Correct. ITA §39(11) requires an otherwise required summary, no filing within five calendar days after the ordinary deadline, and that month's advance-remittance obligation or request for the specified child bonus, interest-paid bonus or employment premium. An advance already remitted does not erase the statutory remittance obligation for the filing gateway. Absence of this financial/request gateway is not treated as proof that every separate filing duty disappears. |
| Current category and tariff | Correct. TC §154(1)(j) catches nonmonetary duties outside (a)–(i); §155(1)(e) gives €100–€10,000 in both independently compared January and September 2026 provisions. This is a range, not an automatic €100 assessment. The actual published historical decision expressly applies j/e to late Prehľad. |
| First breach and continuing breach | Correct. TC §155(4) suppresses the first relevant range fine and provides the assessment factors. FS's actual first-breach guidance identifies separate letter/subpoint categories and separate tax/customs-office assessment; a different form or next month is not a fresh first chance in the same category. TC §155(16) permits an equal repeat fine while the same unlawful state continues and the earlier fine did not remedy it. |
| July 2026 date | Correct. Ordinary due date 31 August 2026, fifth calendar day 5 September (Saturday), adjusted tolerance endpoint Monday 7 September. 8 September is outside tolerance. Independently recomputed with the date library and directly confirmed by FS's actual July example and FAQ13; TC §27(2), (4). |
| Payment interest independent of filing fine | Correct. ITA §35(6) establishes remittance time separately. The new paragraph says “ordinarily” for the five-day rule and cites the governing section; the section also contains its special foreign economic-employer/document branch. A timely remittance produces no payment interest merely because the form was late; tolerance/first-breach fine relief does not forgive an actual payment failure. |
| ECB date, duration, cutoff, rounding | Correct. TC §156(1)(d), (2): late/short collected wage advance, four times the ECB rate on the day after the advance should have been remitted, annual floor 15%, counting next day through payment inclusive. Section156(5) specifically cuts the wage-advance calculation off at payment or, if still unpaid, annual reconciliation, latest the applicable annual-return deadline. The general four-year maximum is retained. TC §161 rounds downward to €0.10; §156(6)(b) excludes interest of €5 or less per relevant tax/customs-office case. |
| Historical decision | Correctly limited. Decision104440104/2025 of 28 October 2025 supports classification, not the current tariff. Its historical €30–€3,000 range is superseded for the reviewed 2026 offence. Both PDF pages were read visually and as extracted text. The appeal notice gives no proof of finality; the Guide expressly leaves finality unverified. Taxpayer identity, address, tax IDs and payment details were not copied into the Guide. |

Actual current law was read from the retained section bodies, not inferred from source titles or another investigator's conclusions. Fresh live web opens independently confirmed the statute versions, FS pages and historical PDF. Full source hashes and exact paths are in [source-hashes.json](source-hashes.json); fresh tool receipts are retained beside this report.

Primary URLs:

- [ITA 2026, §§35,39,49](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html)
- [Tax Procedure Code, January 2026](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260101.html)
- [Tax Procedure Code, September 2026, §§27,154–156,161](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html)
- [FS monthly Prehľad guidance and FAQ13](https://podpora.financnasprava.sk/879943-Pod%C3%A1vanie-mesa%C4%8Dn%C3%BDch-preh%C4%BEadov)
- [FS first-breach category guidance](https://podpora.financnasprava.sk/989535-Druh%C3%A1-%C5%A1anca)
- [Published historical administrative decision](https://evo.isepvo.sk/evoportal/sk-sk/Public/DocumentSearch/GetAttachment?attId=1000515050&docId=1000295789)

## Full-content preservation and checks

The complete current Guide and complete original baseline were compared. All metadata except the intended version change is identical. Preamble, applicability, rates, bases, ordinary deadlines, cross-border/A1 material, both worked examples, six intake questions, byline and CTA are byte-identical. All original source URLs remain. The actual deletion inventory is version0.4, the two replaced penalty rows, one blank line, and the resolved “Not yet confirmed” fine-band sentence. Each substantive replacement preserves and refines its original topic; the general four-year interest maximum remains in the new paragraph. No old method/topic was silently removed.

- 30 independent boundary controls PASS, including July date, financial/request gateways, no-income versus required payout form, first/later category history, separate offices, payment timing, ECB reference date/rate floor, payment/reconciliation/annual-return cutoff and €5/rounding boundaries.
- Repository example runner: 1 file, **2 oa-check blocks, 0 failures, 0 missing**.
- Targeted repository Guide validator: **1 Guide checked, 0 errors, 0 warnings**. An initial absolute-path filter selected zero Guides; it was corrected to a proven repository-relative path before recording this verdict.
- `git diff --check`: PASS.
- Exact current Guide hash rechecked after controls.

The reviewer-written executable controls and JSON results are retained. They do not provide completeness merely from shape or a heading count: the substantive conclusion rests on the source review above, and the preservation conclusion includes an itemized review of every deletion.

## Boundaries remaining open

This closes only the defined monthly Prehľad sanction delta and its resolved fine-band reservation. The Slovakia pack remains partial, including the outstanding VAT issues and current PIT/CIT form work identified in the parent closeout. No country-wide completeness, new publication status or licensed-accountant signoff follows from this PASS. Individual remittance dates, payout facts, prior offence history and applicable annual reconciliation/return deadline remain factual inputs, not unresolved ordinary legal methods in this delta.
