# Nigeria pack: independent review (rule 9)

- Date: 2026-10-29
- Reviewer: independent AI review agent (no shared context with the writer)
- Branch: pack/ng
- Files reviewed: `skills/international/nigeria/ng-pension-nhf-social-contributions.md`, `skills/international/nigeria/ng-non-resident-cross-border.md`, `skills/international/nigeria/README.md`
- Writer's notes (`evidence/research/nigeria-2026/2026-10-29-ng-pack-source-notes.md`) were treated as claims and re-checked against the sources below.

## Sources re-read

| Source | URL | Read on | How |
|---|---|---|---|
| Nigeria Tax Act 2025 (Act No. 7), Official Gazette No. 117, 26 June 2025 | https://nass.gov.ng/documents/download/11249 | 2026-10-29 | curl + pdftotext |
| Nigeria Tax Administration Act 2025 (Act No. 5), Official Gazette No. 117, 26 June 2025 | https://nass.gov.ng/documents/download/11250 | 2026-10-29 | curl + pdftotext |
| Pension Reform Act 2014, PenCom copy | https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf (linked from https://www.pencom.gov.ng/pra2014/) | 2026-10-29 | curl; text layer garbled, pages 7, 8, 9, 11, 12 rendered and read as images |
| PenCom FAQ on the CPS (2020) | https://pencom.gov.ng/wp-content/uploads/2020/06/FREQUENTLY-ASK-QUESTION-2020-ENGLISH-MAIN-VISUAL.pdf | 2026-10-29 | curl + pdftotext |
| National Housing Fund Act, Cap. N45 (FMBN copy) | https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf | 2026-10-29 | curl + pdftotext |
| FMBN NHF legal framework | https://fmbn.gov.ng/products/nhf-scheme/legal-framework | 2026-10-29 | curl |
| NSITF services | https://nsitf.gov.ng/services/ | 2026-10-29 | curl and built-in browser |
| ITF Revenue department | https://itf.gov.ng/departments/revenue.html | 2026-10-29 | built-in browser (curl got HTTP 406) |
| NRS Nigeria Tax Act page | https://www.nrs.gov.ng/tax-laws/nigerian-administration-act | 2026-10-29 | built-in browser (curl got a bot-check page; not solved) |

## Figures checked

| Item | Skill value (as submitted) | Source value | Source | Result |
|---|---|---|---|---|
| "Resident individual": alternatives or cumulative? | any of (a)–(f) | limbs (a)–(f), "(e) ... or (f)"; non-resident = all six negated, joined by "and". Alternatives | NTA s201 | match; wording made explicit, cite changed from "interpretation" to s201 |
| 183-day test | 183 days in 12 months | "not less than 183 days in a 12-month period inclusive of annual leave or temporary period of absence" | NTA s201 | match |
| "Nigerian company" | incorporated, or central or effective management/control in Nigeria | same, three limbs | NTA s201 | match |
| Small company | turnover <= NGN 100m and fixed assets <= NGN 250m | same | NTA s201 | match |
| Worldwide taxation of residents | s12 | s12 | NTA s12 | match |
| Employment income source | s13(1)(a)/(b) | same | NTA s13(1) | match |
| Non-resident charge and gains | s17(1), (2) | same | NTA s17(1)–(2) | match |
| s17(3)(a)–(c) and exceptions (i)–(iii) | as stated | same | NTA s17(3) | match |
| s17(4) final tax | final unless attributable to PE/SEP | same; cross-refers to "section 50 of NTAA" | NTA s17(4) | match; cross-ref error noted (see fixes) |
| s17(5)(a)–(e) PE profit rules | as stated | same | NTA s17(5) | match |
| s17(6)–(7) profit-margin fallback | as stated | same | NTA s17(6)–(7) | match |
| s17(8) minimum | "not subject to deduction at source" → 4% of Nigerian income | "not less than the tax withheld at source under NTAA, and where the income is not liable to a deduction of tax under NTAA, 4%" | NTA s17(8) | fixed (wording "not liable") |
| s17(9)(a)–(e) PE, SEP, employment carve-out, "place", profit margin | as stated | same; "place" list is (9)(d) | NTA s17(9) | match; (9)(d) cite added |
| s18 shipping/air, 2% minimum monthly | 2% of gross revenue, monthly | same, "computed, assessed and paid on monthly basis" | NTA s18(6) | match |
| Shipping monthly return due date | "monthly" | 21st day of the following month, with evidence of payment | NTAA s21(1)–(3) | fixed (added) |
| s19 dividends to non-residents | no further tax, no refund | same; s19(2) cross-refers to NTAA s50 | NTA s19 | match; cross-ref noted |
| Company rate | 30%, small 0%, 25% by Presidential order | same | NTA s56 | match |
| 15% minimum ETR | out of scope, s57 | s57 | NTA s57 | match |
| Development levy | 4%, not small or non-resident companies | same | NTA s59(1) | match |
| Unilateral credit | lower of attributable Nigerian tax (excl. Chapter Three taxes) and foreign tax; proportion formula | same | NTA s119(2)–(3) | match |
| DTA effect, extant DTAs from 1 Jan after entry into force, anti-treaty-shopping, beneficial owner, GMT carve-out | as stated | same | NTA s120(1), (5)–(8) | match |
| Treaty credit, no credit to non-resident, no deduction, 2-year claim | as stated | same | NTA s121(3)–(7) | match |
| "Excess unilateral foreign tax neither credited nor deductible" (Example 2 edge) | stated as rule | s119 caps the credit; the no-deduction rule s121(6)(a) applies to treaty "foreign tax" (s122 definition) only | NTA ss119, 121, 122 | fixed (moved to Not yet confirmed) |
| Non-resident company return contents | "group audited accounts" ... | "the company's full audited financial statements and the financial statement of the Nigerian operations, attested to by an independent, qualified or certified accountant in Nigeria" ... | NTAA s11(2) | fixed |
| No return where only final-tax income | s11(3) | same | NTAA s11(3) | match |
| Filing deadlines | 6 months; new company 18 months / 6 months; cessation 6 months | same | NTAA s11(5) | match |
| Artificial transactions appeal | s46(2)–(3) | same | NTAA s46 | match |
| Late return penalty | not confirmed | NGN 100 000 first month + NGN 50 000 each later month | NTAA s101 | added |
| Late payment | not confirmed | 10% + interest at CBN MPR + spread (naira) or SOFR + spread (FX) | NTAA s65(1) | added |
| Failure to deduct | not confirmed | 40% of amount not deducted | NTAA s105 | added |
| Failure to remit deductions | not confirmed | amount + 10% a year + interest at MPR; due by 21st of next month; conviction up to 3 years or fine | NTAA s107 | added |
| NTA commencement | 1 January 2026 | "[1st January, 2026] Commencement" | NTA gazette, p. A395 | match; now cited to the gazette (NRS page does not state the date) |
| Individual bands | 0/15/18/21/23/25% on 800k / 2.2m / 9m / 13m / 25m / above 50m | same | NTA s58, Fourth Schedule | match; Minimum Wage exclusion added |
| Eligible deductions incl. rent relief 20% max NGN 500 000 | as stated | same | NTA s30(2)(a) | match |
| Deductions claimed in writing | s31 | same | NTA s31 | match |
| Pension rates | 10% employer, 8% employee | minimum 10% and 8% | PRA s4(1) | match; now cites the Act |
| Employer bearing whole contribution | "full 18%+" | not less than 20% of monthly emoluments | PRA s4(4)(b) | fixed (FAQ says 18%; statute wins) |
| Monthly emoluments floor | basic + housing + transport | same | PRA s120 definition | match |
| Private-sector coverage threshold | 3 or more employees | **15 or more** employees (s2(2)); fewer than 3 may join voluntarily (s2(3)); PenCom FAQ Q16 says 3 or more | PRA s2(2)–(3); PenCom FAQ | fixed: statute stated, conflict flagged, README SC partial |
| Exemptions | judicial officers, armed forces, intelligence; pre-2004 retirees; those with <= 3 years to retire at 30 June 2004 | s5(1)(a) persons in Constitution s291 incl. armed forces, intelligence and secret services; (b) employees under a scheme existing before **25 June 2004** with 3 or less years to retire at that date | PRA s5(1) | fixed |
| Remittance deadline | 7 working days from payday | same; remitted to the Pension Fund Custodian | PRA s11(3)(b) | match; cite and payee fixed |
| Late-remittance penalty | at least 2% of total unpaid contributions | at least 2% of the unpaid contribution **for each month or part of a month** the default continues | PRA s11(6)–(7) | fixed |
| Tax treatment of contributions | "not taxed" (FAQ) | tax-deductible expenses (s10(1)); voluntary-contribution income taxed if withdrawn within 5 years (s10(4)) | PRA s10 | refined |
| Group Life | at least 3 x annual total emolument | same; premium paid not later than start of cover | PRA s4(5); FAQ Q28–29 | match |
| Voluntary contributions, one-third cap | FAQ Q7 | FAQ Q7 (not found in PRA text) | PenCom FAQ | match (official FAQ) |
| Employer code at 3+ employees | FAQ | FAQ (registration section Q8) | PenCom FAQ | match |
| Foreigners not mandated | FAQ | FAQ Q19 | PenCom FAQ | match |
| Contract/casual staff use salary payable | FAQ | FAQ, service-delivery Q5 | PenCom FAQ | match |
| NHF rate and threshold | 2.5% of basic monthly salary, NGN 3 000+ a year | same | NHF Act s4(a), s9(1) | match |
| NHF remittance | within one month | same | NHF Act s9(2), s10 | match |
| NHF penalties | NGN 50 000; NGN 20 000 "up to" 5 years; NGN 5 000 "up to" 1 year | fine NGN 50 000; NGN 20 000 or imprisonment **for a term of five years** or both; NGN 5 000 or one year or both | NHF Act s20(2)–(3) | fixed wording; s20(5) added |
| NHF Act being amended | FMBN note | "Act 3 is being amended" | FMBN legal framework | match |
| NSITF | 1% of total monthly payroll, employer-funded, via ecsonline | same | NSITF services | match |
| ITF | 1% of annual payroll; 50% reimbursable | same | ITF Revenue page | match |

Total items checked: 58 rows above (several rows cover more than one figure).

## Fixes made (with sources)

Pension skill:
1. Coverage threshold: statute PRA s2(2) says 15 or more employees; PenCom FAQ Q16 says 3. Body now states the statute (rule 2) and flags the conflict; Example 2 and the Ask-first list updated; Not yet confirmed lists the conflict. Description updated.
2. Employer bearing whole contribution: at least 20% (PRA s4(4)(b)), not 18%.
3. Exemptions rewritten per PRA s5(1): one pre-2004 category, date 25 June 2004 (not 30 June).
4. Late-remittance penalty: at least 2% per month or part month (PRA s11(7)).
5. Remittance payee: the Pension Fund Custodian (PRA s11(3)(b)).
6. Rates now cite the PRA (ss4, 10, 11, 120) as well as the FAQ; PRA added to Sources; "PRA text not reachable" removed from Not yet confirmed.
7. NHF penalties: fixed terms of imprisonment, not "up to"; s20(5) continuing liability added.
8. NTA s58 Minimum Wage exclusion noted; NTA commencement cited to the gazette.

Cross-border skill:
1. Residence limbs stated as alternatives; definitions cited to NTA s201.
2. s17(8): "not liable to deduction" wording in table, body and Example 1 (assumption stated).
3. Added NTAA s51(2) final tax for non-resident recipients of dividends, interest, rent, royalties, directors' fees and entertainer/sportsperson payments.
4. Noted that NTA s17(4) and s19(2) cross-refer to "section 50 of NTAA", but deduction at source is NTAA s51 (s50 is upstream petroleum instalments).
5. Non-resident return contents corrected to NTAA s11(2)(a) wording.
6. Shipping/airline monthly return due by the 21st of the following month (NTAA s21).
7. Penalties section filled from NTAA ss65, 66, 101, 105, 107 (were "not confirmed").
8. Example 2 edge: removed the unsourced claim that excess unilateral foreign tax is not deductible; s121(6)(a) applies to treaty cases; question moved to Not yet confirmed. Development levy noted as outside the example. Summary "never by deduction" limited to treaties.
9. NRS source row description corrected (the page does not state the commencement date; the gazette does).

README:
1. "single substantive federal tax law" → "principal substantive tax law" (NRS page wording).
2. `partial` entries added for SC (threshold conflict; ITF/NSITF gaps) and XB (deduction-at-source rates in unread regulations; ng-wht is tax_year 2025). Coverage report now shows NG present: none.
3. SC row no longer says "3+ staff"; PRA added to Official sources.

## Examples recomputed by hand

- Pension Ex. 1: emoluments 600 000; employee 8% = 48 000; employer 10% = 60 000; NHF 2.5% x 400 000 = 10 000; NSITF 6 000; ITF 72 000/yr; annual pay 7 200 000; deductions (48 000 + 10 000) x 12 = 696 000; chargeable 6 504 000; 15% x 2 200 000 = 330 000; 18% x 3 504 000 = 630 720; tax 960 720; monthly 80 060. Correct.
- Pension Ex. 2: 2 employees; pension mandatory 0 under both the statute (15) and PenCom (3) thresholds; NHF 2 x 3 750 = 7 500; NSITF 1% x 400 000 = 4 000; per head if covered 18% x 200 000 = 36 000. Correct. oa-check formula changed to the statute threshold (employees - 14); outputs unchanged.
- XB Ex. 1: 12% x 500m = 60m > 10m; 30% x 60m = 18m; 4% x 500m = 20m; payable 20m. Correct, on the stated assumption that the income is not liable to deduction at source.
- XB Ex. 2: 30% x 200m = 60m; 50/200 x 60m = 15m; credit min(15m, 12m) = 12m; net 48m; edge credit capped at 15m. Correct.
- `python3 scripts/check-examples.py` on both files: 2 blocks each, 0 failures. `validate-guides.py --no-index-check`: passed. `coverage-report.py --json`: NG has README, partial entries as above.

## Still not confirmed

- Private-sector pension threshold (PRA s2(2) "15" in PenCom's copy vs PenCom FAQ "3"); PenCom's copy is headed "A Bill" with a blank commencement date, so whether the gazetted Act or a later amendment reads differently was not confirmed.
- ITF liability threshold, due date, "payroll" definition and penalties (no ITF Act text found on itf.gov.ng).
- NSITF penalty rates and payment due date (services and FAQ pages give none).
- NHIS/NHIA rates; NHF for foreign nationals; status of the NHF Act amendment.
- Deduction-at-source regulations and rates (NTAA s51(1) leaves rates to regulations).
- Minister's spread over MPR/SOFR for late-payment interest (NTAA s65).
- Whether excess non-treaty foreign tax is deductible.
- Presidential order for the 25% company rate; SEP regulations; ratified treaty list; Transfer Pricing Regulations (old.firs.gov.ng not checked again).

## Other observations (not changed)

- The NTAA gazette prints its commencement as 26 June 2025, not 1 January 2026. The skills only date the NTA to 1 January 2026, so nothing was changed.
- NTA s57(2)(a) prints the MNE threshold as "£750 million" in the gazette; the skill does not state the figure.
- NTAA s51(8) sets a 5% final deduction on non-resident technical/consulting/professional/management services to a labelled startup; not added (rates are out of scope for this skill).

## Unreachable or blocked

- nrs.gov.ng: curl returned a Radware bot-check page; read in the built-in browser instead (no CAPTCHA solved).
- itf.gov.ng: curl HTTP 406; read in the built-in browser.
- PenCom PRA PDF: text layer is font-shifted; relevant pages read as rendered images.
