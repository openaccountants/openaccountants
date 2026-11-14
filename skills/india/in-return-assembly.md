---
name: in-return-assembly
description: Final orchestrator skill that assembles the complete India filing package for India-resident self-employed individuals and professionals. Consumes outputs from all India content skills (india-gst for GSTR-3B/GSTR-1, india-income-tax for ITR-3/ITR-4, in-advance-tax for quarterly instalments, in-tds-freelance for TDS reporting) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all India content skills listed above. India full-year residents only. Self-employed individuals and professionals only.
version: 0.2
type: filing-howto
jurisdiction: IN
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v 1.0 (content)
tier: 2
domain: income-tax
---

# India Return Package Assembly for Self-Employed Residents

This Guide assembles the complete India filing package for a resident individual who is self-employed or practises a profession as a sole proprietor: the income-tax return, the advance tax and TDS reconciliation and the GST position, checked against each other and handed to a Chartered Accountant for review. Figures are for tax year 2026. That means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. GST is not year-based: the GST operative texts here were read on 14 November 2026, with their start dates. Income of 1 April 2025 to 31 March 2026 (assessment year 2026-27) stays under the 1961 Act and its return is not covered by this Guide; use `india-income-tax` and `in-freelance-intake` for it.

This Guide runs last. It does not replace the computations of the content Guides; it orders them, checks that their outputs agree, and builds the reviewer package. A Chartered Accountant must review and sign off the package before anything is filed.

## Scope

The final capstone Guide for India self-employed returns. Every India content Guide feeds into this one. The output is the complete reviewer package that a Chartered Accountant can review, sign off and deliver to the client with filing instructions.

This Guide coordinates the content Guides, checks cross-Guide consistency and assembles the final deliverable. Run the content Guides in the order of Section 2. If a self-check fails, note it in the reviewer brief's open flags and continue with a clearly partial draft. Resolve blockers before stating a final filing amount or a filing-ready package. If the run is cut short, finish the computation work first (numbers, positions, flags), produce whatever formatted outputs you can, and state which deliverables were not produced and why.

Produces the complete India filing package for:

- Individuals resident in India for the whole tax year, not "not ordinarily resident" (use `in-tax-residency` if unsure). SUGAM (ITR-4) is for "a resident other than not ordinarily resident" under rule 164(5) of the [Income-tax Rules 2026](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
- Self-employed individuals and professionals working as sole proprietors under their own PAN.
- Tax year 2026-27 (1 April 2026 to 31 March 2027), Income-tax Act 2025. Returns for this year are filed in 2027 by the dates in the due-date table above.
- GST returns (GSTR-3B and GSTR-1, if registered) for the months of the same period, the income-tax return (ITR-3 or SUGAM ITR-4), the advance tax reconciliation and the TDS credit reconciliation.

Out of scope: income of 1 April 2025 to 31 March 2026 (1961 Act, assessment year 2026-27); HUFs, firms, LLPs and companies; non-residents; cases where section 172 (transfer pricing report) applies.

## Ask the client first

Ask only what the intake package and documents do not already answer.

- Is this for income of 1 April 2026 to 31 March 2027, or for the year before? The year decides the Act, the section numbers and the forms.
- Are your accounts required to be audited under the 2025 Act or any other law? This moves the return due date from 31 August to 31 October and adds the audit report.
- Have you ever opted out of the new regime, and have you already withdrawn that option once? Section 202(4) allows one withdrawal only.
- Did you use the presumptive business scheme (section 58(2) serial 1, or section 44AD before 1 April 2026) in any of the last five years and then declare a lower profit? Section 58(7) may bar the scheme.
- How much of your receipts, and of your payments, was in cash? The cash-share tests decide the presumptive limit and the audit limit.
- Do you supply services to clients outside India, and do you have a Letter of Undertaking for zero-rated supplies?

## The method, step by step

1. **Fix the year and the Act.** Tax year 2026-27, Income-tax Act 2025 ([new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq)). If the income is for the year to 31 March 2026, stop and use `india-income-tax`.
2. **Take the intake package** from `in-freelance-intake`: residence, structure, PAN, age, regime history, presumptive history, GST status, documents.
3. **Run `india-gst`** and fix GST turnover, output tax and input tax credit for the months of the year ([rule 61](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html), [rule 80](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html)).
4. **Choose the basis** under section 58 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf): serial 3 for a specified profession, serial 1 for an eligible business, or actual profit. Test receipts against the limits in the Act table, using the cash share to pick the limit.
5. **Test for tax audit** under section 63 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf): business turnover above INR 10,000,000 (INR 100,000,000 where cash receipts and cash payments each stay within 5%), professional gross receipts above INR 5,000,000 (all threshold amounts in words on the page), or presumptive cases claiming lower profit. A cheque or bank draft that is not account payee counts as cash for both cash tests (sections 58(9) and 63(5)(b)). Section 63(2): no audit where profit is declared under section 58(2). If an audit is required, the report (Form No. 26 under rule 47 of the [Income-tax Rules 2026](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf)) is due one month before the return due date (section 63(5)(a)), and the ordinary required-audit return is due 31October; s.172 cases follow 30November and are out of scope.
6. **Fix the regime** under section 202 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf). The new regime applies unless the client opts out under section 202(4). With business or profession income, the option must be exercised on or before the section 263(1) due date, carries to later years, and can be withdrawn only once; after withdrawal it cannot be exercised again unless the person stops having business or profession income. Only an old-Act option in force immediately before commencement is saved under s.536(2)(f). Rule 136 puts the current option/withdrawal in the s.263(1) return, not a replacement standalone Form 10-IEA. The FAQ summarizes savings: "An option exercised under a provision of the old Act ... is treated as if it was made under the equivalent provision of the new Act" ([new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq), questions 23 and 26).
7. **Run `india-income-tax`** for total income and tax: slabs, rebate, surcharge and cess from the tables above ([Finance Act 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf)).
8. **Pick the return form** under rule 164 of the [Income-tax Rules 2026](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf): SUGAM (ITR-4) for a resident (not RNOR) individual with section 58 income and, if it has capital gains, only long-term capital gains under section 198 within the limit in the Rules table (rule 164(5)(b)), and none of the rule 164(6) bars; otherwise ITR-3. The bars include foreign assets, signing authority or income, being a company director, holding unlisted equity shares at any time in the year, total income exceeding INR 5,000,000 (in words on the page), more than two house properties, agricultural income above INR 5,000, and any loss brought forward or to carry forward.
9. **Run `in-advance-tax`** and compute section 424 and 425 interest ([Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf)).
10. **Run `in-tds-freelance`** and match every credit to the tax credit statement and Form No. 168 ([tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)).
11. **Run the four cross-checks** in Section 3 and the self-checks in Section 6.
12. **Set the dates**: return due date from section 263(1)(c) as substituted by the [Finance Act 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf); belated return within 9 months (in words on the page) of the end of the tax year (section 263(4)); revised return within 12 months (in words on the page) (section 263(5)).
13. **Assemble the three output files** (Section 7) and state once that a Chartered Accountant must review and sign off before filing.

### Section numbers changed on 1 April 2026

The Income Tax Department states that "The 1961 Act stands repealed on the 01.04.2026" and that the law applicable to a tax payment "is determined by the year of income, not by the date of payment" ([new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq); [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)). For tax year 2026-27 use the 2025 Act numbers. The Department's own pages give these mappings:

| 1961 Act | Income-tax Act 2025 | Page that states it |
| --- | --- | --- |
| Section 115BAC (new tax regime) | Section 202 | [new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq), question 22 |
| Sections 44AD, 44ADA, 44AE (presumptive income) | Section 58, one table | [new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq) |
| Section 234B (interest for default in advance tax) | Section 424 | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq), question 20 |
| Section 234C (interest for deferment of advance tax) | Section 425 | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq), question 20 |
| TDS sections 192 to 194T | Sections 392 (salary) and 393 (other payments) | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq) |
| Annual Information Statement | Form No. 168 from tax year 2026-27 | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq) |

Every other 2025 Act section named below is cited by its new number only. The cited primary provisions control; no old section number is assumed for an unmapped item.

### Figures the cross-checks use

#### Income-tax Act 2025 (Act 30 of 2025, as enacted)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| New regime (section 202(1), the default for individuals), any age: income taxed at nil up to | INR 400,000 | "1. Upto ₹400000 Nil"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: rate on the next slice | 5% | "2. From ₹400001 to ₹800000 5%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: top of the 5% slice | INR 800,000 | "2. From ₹400001 to ₹800000 5%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: rate on the next slice | 10% | "3. From ₹800001 to ₹1200000 10%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: top of the 10% slice | INR 1,200,000 | "3. From ₹800001 to ₹1200000 10%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: rate on the next slice | 15% | "4. From ₹1200001 to ₹1600000 15%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: top of the 15% slice | INR 1,600,000 | "4. From ₹1200001 to ₹1600000 15%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: rate on the next slice | 20% | "5. From ₹1600001 to ₹2000000 20%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: top of the 20% slice | INR 2,000,000 | "5. From ₹1600001 to ₹2000000 20%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: rate on the next slice | 25% | "6. From ₹2000001 to ₹2400000 25%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: income above which the top rate applies | INR 2,400,000 | "7. Above ₹2400000 30%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime: top rate | 30% | "7. Above ₹2400000 30%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, section 156(2), resident individual on the new regime: 100% of tax or this amount, whichever is less | INR 60,000 | "(a) the income does not exceed twelve lakh rupees, 100% of the income-tax payable or ₹ 60000, whichever is less"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, section 156(2): income limit (printed in words) | INR 1,200,000 (in words on the page) | "twelve lakh rupees"; resident individual, s.202(1), rebate capped to s.202(1) tax; marginal relief separately; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, section 156(1), resident individual on the old regime: 100% of tax or this amount, whichever is less | INR 12,500 | "deduction of 100% of income-tax payable or ₹ 12500, whichever is less"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, section 156(1): available only if total income does not exceed | INR 500,000 | "chargeable on the total income for any tax year if such total income does not exceed ₹ 500000"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Standard deduction from salary, section 19(1) Table serial 2(a), new regime: this amount or the salary, whichever is less | INR 75,000 | "(a) ₹ 75000 or the salary, whichever is less, where income-tax is computed under section 202(1)"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Standard deduction from salary, section 19(1) Table serial 2(b), any other case (old regime) | INR 50,000 | "(b) ₹ 50000 or the salary, whichever is less, in any other case"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive business, section 58(2) Table serial 1: turnover limit (words) | INR 20,000,000 (in words on the page) | s.58(2), serial 1: "two crore rupees"; eligible business only; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive business: higher limit where cash receipts do not exceed 5% (words) | INR 30,000,000 (in words on the page) | s.58(2), serial 1: "three crore rupees"; cash receipts no more than 5% of total turnover/gross receipts; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive business and profession: cash share for the higher limit, not more than | 5% | s.58(2), serial 1/3: "does not exceed 5%"; non-account-payee cheque/draft deemed cash under s.58(9); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive business: deemed profit on receipts by bank or other specified mode | 6% | s.58(2), serial 1: "6% of total turnover or gross receipts"; qualifying account-payee/electronic receipts during year or before s.263(1) due date; higher actually claimed profit prevails; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive business: deemed profit on the remaining turnover | 8% | s.58(2), serial 1: "8% of total turnover or gross receipts"; remaining turnover; higher actually claimed profit prevails; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive profession, section 58(2) Table serial 3: deemed profit share of gross receipts | 50% | s.58(2), serial 3: "50% of the gross receipts"; higher actually claimed profit prevails; specified resident assessee/profession only; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive profession: gross receipts limit (words) | INR 5,000,000 (in words on the page) | s.58(2), serial 3: "fifty lakh rupees"; specified resident assessee/profession; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Presumptive profession: higher limit where cash does not exceed 5% of gross receipts (words) | INR 7,500,000 (in words on the page) | s.58(2), serial 3: "seventy-five lakh rupees"; cash receipts no more than 5%, including deemed cash; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 58(7): period barred after leaving the business scheme (words) | 5 tax years (in words on the page) | "for five tax years"; serial 1 used then contrary declaration within succeeding 5 tax years; bar runs after departure year; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Tax audit, section 63(1) Table serial 1(a): business turnover above (words) | INR 10,000,000 (in words on the page) | "one crore rupees"; business turnover above limit; s.63(2) presumption exclusion and s.58(3)/(8) overrides apply; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Tax audit, serial 1(b): limit where cash receipts AND cash payments each do not exceed 5% (words) | INR 100,000,000 (in words on the page) | "ten crore rupees"; both cash receipts and cash payments separately no more than 5%; deemed cash included; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Tax audit, serial 1(b): cash share of receipts, and separately of payments, not more than | 5% | "in cash, does not exceed 5% of the said amount"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Tax audit, serial 1(c): profession gross receipts above (words) | INR 5,000,000 (in words on the page) | "fifty lakh rupees"; s.63(2) exclusion where income declared under s.58(2), subject to lower-profit/lockout rules; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax due (section 404) when the tax for the year is | INR 10,000 | "where the amount of such tax payable during that year, as computed under this Part, is ₹10000 or more"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax, section 408(1): by 15 June, not less than | 15% | "Not less than 15% of such advance tax"; cumulative, ordinary schedule; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax: by 15 September, cumulative, not less than | 45% | "Not less than 45% of such advance tax"; cumulative, ordinary schedule; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax: by 15 December, cumulative, not less than | 75% | "Not less than 75% of such advance tax"; cumulative, ordinary schedule; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest for default in advance tax, section 424(1): simple, per month or part of a month | 1% | "the assessee shall be liable to pay simple interest at the rate of 1% for every month or part of a month"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 424(1)(b): interest applies where advance tax paid is less than this share of assessed tax | 90% | "is less than 90% of the assessed tax"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest for deferment, section 425(1): flat, on the shortfall at 15 June, 15 September and 15 December | 3% | "3%" in columnE for each first 3 dates; conditional statutory table only: s.425(2)/(3) construction held below; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest for deferment, section 425(1) serial 4 and 425(3): on the shortfall at 15 March | 1% | "1%"; s.425(1) March columnE/s.425(3); ordinary-schedule interaction held below; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 425(2)(a): the Act says no section 425(1) interest if the amount paid by 15 June is this share or more of the tax due on the returned income. construction held; no final filing computation | 12% | "on or before the 15th day of June is 12% or more of the tax due on the returned income"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 425(2)(b): the Act says no section 425(1) interest if the amount paid by 15 September is this share or more of the tax due on the returned income. construction held; no final filing computation | 36% | "on or before the 15th day of September is 36% or more of the tax due on the returned income"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest for a late return, section 423(1): I = this rate x tax x months | 1% | "I = 1% x A x T"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Belated return, section 263(4): within this period from the end of the tax year (words) | 9 months (in words on the page) | "within nine months"; or before assessment, whichever earlier; no extension assumed; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Updated return, section 263(6)(a): within this period from the end of the financial year after the tax year (words) | 48 months (in words on the page) | "within forty-eight months"; eligibility/exclusions and additional tax require separate review; not an unconditional remedy; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### Finance Act 2026 (Act 4 of 2026, as enacted)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| Old regime (First Schedule Part I-B Paragraph A; only where the person opts out of section 202), under 60: nil band up to | INR 250,000 | First Schedule I-B Paragraph A, applicable age/residence row, quote "exceed ₹ 250000"; full age-specific bands below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, resident aged 60 to 79: nil band up to | INR 300,000 | First Schedule I-B Paragraph A, applicable age/residence row, quote "exceed ₹ 300000"; full age-specific bands below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, resident aged 80 or more: nil band up to (then 20%; no 5% slice) | INR 500,000 | First Schedule I-B Paragraph A, applicable age/residence row, quote "not exceed ₹ 500000"; full age-specific bands below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, under 60: rate on the slice above the nil band, up to INR 500,000 | 5% | First Schedule I-B Paragraph A, applicable age/residence row, quote "5% of the amount"; full age-specific bands below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime: rate on the slice above INR 500,000 | 20% | First Schedule I-B Paragraph A, applicable age/residence row, quote "20% of the amount"; full age-specific bands below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime: income above which the top rate applies, all ages | INR 1,000,000 | First Schedule I-B Paragraph A, applicable age/residence row, quote "exceeds ₹ 1000000"; full age-specific bands below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime: top rate | 30% | First Schedule I-B Paragraph A, applicable age/residence row, quote "30% of the amount"; full age-specific bands below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, section 3(4) Table serial 10 (new regime): applies where total income exceeds | INR 5,000,000 | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "exceeds ₹ 5000000"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, new regime: rate from that threshold up to INR 10,000,000 | 10% | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "rate of 10%"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, new regime: next threshold | INR 10,000,000 | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "rate of 15%"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, new regime: rate above INR 10,000,000 up to INR 20,000,000 | 15% | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "rate of 15%"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, new regime: threshold for the top rate (income excluding dividends and capital gains under sections 196 to 198) | INR 20,000,000 | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "exceeds ₹ 20000000, at the rate of 25%"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, new regime: top rate | 25% | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "exceeds ₹ 20000000, at the rate of 25%"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, old regime only (Table serial 1): rate where income excluding dividends and capital gains exceeds INR 50,000,000 | 37% | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "exceeds ₹ 50000000, at the rate of 37%"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, old regime only: threshold for 37% | INR 50,000,000 | s.3(4) table serial 10 (new) / First Schedule I-B Paragraph F (old), quote "exceeds ₹ 50000000, at the rate of 37%"; income-component caps and marginal relief apply; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge cap on the part of tax relating to dividends and capital gains (sections 196, 197, 198 under section 202; section 210(1) Table serial 2 to 5 for the old regime), both regimes | 15% | "the rate of surcharge on the income-tax in respect of that part of income shall not exceed 15%"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess on income-tax plus surcharge | 4% | "calculated at the rate of 4% of such income-tax and surcharge"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Fee for a return not filed by the due date, section 428(a): total income not more than INR 500,000 | INR 1,000 | "(i) a sum of ₹ 1000, if the total income of such person does not exceed ₹ 500000"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Section 428(a): total income limit for the lower fee | INR 500,000 | "(i) a sum of ₹ 1000, if the total income of such person does not exceed ₹ 500000"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Section 428(a): fee in any other case | INR 5,000 | "(ii) a sum of ₹ 5000, in any other case; (b) furnishes a return"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Fee for not furnishing the section 63 audit report, section 428(c): delay up to one month | INR 75,000 | "(i) a sum of ₹ 75000 for a delay up to one month"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Section 428(c): after the first month | INR 150,000 | "(ii) a sum of ₹ 150000 thereafter; (d) fails to furnish a report from an accountant"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Revised return, section 263(5) as substituted: within this period from the end of the tax year, or before assessment, whichever is earlier (words) | 12 months (in words on the page) | "within twelve months"; or before assessment, whichever earlier; s.428(b) fee after 9months; https://egazette.gov.in/WriteReadData/2026/271439.pdf |

Return due dates, section 263(1)(c) as substituted by section 66 of the Finance Act 2026 (same page). The date falls in the financial year after the tax year, so tax year 2026-27 returns are due in 2027:

| Person | Due date | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| Business/profession, or partner in non-required-audit firm/spouse covered by s.10, excluding earlier company/required-audit/s.172 categories | 31 August | "31st August"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Company; required-audit person under this/other law; partner in required-audit firm or spouse covered by s.10, s.172 not applying | 31 October | "31st October"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Section 172 reporting person/partner/spouse covered by s.10 | 30 November | "30th November"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Any other assessee (no business or profession income) | 31 July | "31st July"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |

#### Income-tax Rules 2026 (notified 20 March 2026)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| SUGAM (ITR-4), rule 164(5)(b): long-term capital gains under section 198 allowed up to | INR 125,000 | "has only long-term capital gains under section 198 not exceeding ₹ 125000"; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| ITR-4 bar, rule 164(6)(h): total income exceeding (words) | INR 5,000,000 (in words on the page) | "exceeding fifty lakh rupees"; all other bars also apply; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| ITR-4 bar, rule 164(6)(m): agricultural income exceeding | INR 5,000 | "has agricultural income, exceeding ₹ 5000;"; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

#### GST: CGST Act 2017, section 22 (registration)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| Registration needed when aggregate turnover in a financial year exceeds (words; statute figure, States other than special category States; suppliers of goods only may have a higher threshold, row below) | INR 2,000,000 (in words on the page) | "if his aggregate turnover in a financial year exceeds twenty lakh rupees"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html |

#### GST: CBIC "GST: An Update" (1 June 2019)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| Services threshold, outside 4 named special-category States; compulsory-registration/exemption review still required | INR 2,000,000 | "for suppliers of services would be Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and"; https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |
| Historical 2019 overview: exclusive-goods threshold, subject to operative notification below | INR 4,000,000 | "for the suppliers of goods would be Rs. 40 lakhs and Rs. 20 lakhs"; https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |

#### GST: Notification 83/2020-Central Tax (GSTR-1)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| GSTR-1 due date, monthly filers | 11th of following month (in words on the page) | "till the eleventh day of the month succeeding such tax period"; https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf |
| GSTR-1 due date, quarterly (QRMP) filers | 13th of month after quarter (in words on the page) | "shall be extended till the thirteenth day of the month succeeding such tax period"; https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf |

#### GST: CGST Rules, rule 61 (GSTR-3B)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| GSTR-3B due date, monthly filers | 20th of following month (in words on the page) | "for each month, or part thereof, on or before the twentieth day of the month succeeding such month"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html |
| GSTR-3B due date, quarterly filers in the first State group named in rule 61 | 22nd of month after quarter (in words on the page) | "twenty-second day of the month succeeding such quarter"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html |
| GSTR-3B due date, quarterly filers in the second State group named in rule 61 | 24th of month after quarter (in words on the page) | "twenty-fourth day of the month succeeding such quarter"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html |
| QRMP option: preceding-year aggregate turnover not above | INR 50,000,000 (in words on the page) | Notification 84/2020: "up to five crore rupees"; preceding due return filed; opt under rule 61A; exclude IGST 14; if exceeded during quarter monthly from next quarter; https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-84-central-tax-english-2020.pdf |

#### GST: CGST Rules, rule 80 (annual return)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| GSTR-9 default due date, if annual return required; notified exemptions/extensions checked by year | 31 December following financial year (in words on the page) | "electronically in FORM GSTR-9 on or before the thirty-first day of December following the end of such financial year"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html |
| GSTR-9C (self-certified reconciliation statement) needed when aggregate turnover exceeds (words) | INR 50,000,000 (in words on the page) | "whose aggregate turnover during a financial year exceeds five crore rupees, shall also furnish a self-certified"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html |

#### GST: CGST Act, section 16 (input tax credit time limit)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| General s.16(4) last ITC date for invoice/debit note of FY, or annual-return filing if earlier; legacy s.16(5)/cancellation-revocation s.16(6) exceptions reviewed separately | 30 November following financial year (in words on the page) | "after the 6 [thirtieth day of November] following the end of financial year to which such invoice or"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html |

#### GST: CGST Act, section 36 (keeping records)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| General GST retention from annual-return due date; proceedings/investigation require later of this and 1 year after final disposal (1 year in words on page) | 72 months (in words on the page) | "shall retain them until the expiry of seventy-two months from the due date of furnishing of annual return"; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter8/section36_v1.00.html |

#### GST: Notification 13/2017-Central Tax (interest)

| Item | Value | Conditions, exact source excerpt and official URL |
| --- | --- | --- |
| Delayed-tax interest per year, s.50(1); cash-ledger proviso/proceedings exception reviewed; wrong-ITC s.50(3) separate | 18% | "Sub-section (1) of section 50 18"; https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-13-central-tax-english.pdf |


##### Conditions controlling the reference tables

- New-regime s.156 rebate is for a resident individual and cannot exceed tax calculated at s.202(1) rates; s.156(2)(b) marginal relief just above INR 1,200,000 and s.156(3) cap must both be applied. Salary deductions are min(salary, INR 75,000) under s.202(1), min(salary, INR 50,000) otherwise; neither is a deduction against freelance receipts. [ss.19,156,202](https://egazette.gov.in/WriteReadData/2025/265620.pdf).
- Old-regime bands: under 60 uses nil to INR 250,000, 5% to INR 500,000, 20% to INR 1,000,000 and 30% above; resident 60-79 uses nil to INR 300,000 then 5%,20%,30% at the same upper bounds; resident 80+ uses nil to INR 500,000,20% to INR 1,000,000,30% above. Age is at any time in the tax year. New-regime rates are independent of age. [First Schedule I-B Paragraph A](https://egazette.gov.in/WriteReadData/2026/271439.pdf).
- For ordinary slab income, surcharge is 10% above INR 5,000,000 to INR 10,000,000;15% above INR 10,000,000 to INR 20,000,000;25% above INR 20,000,000. Old regime continues 25% to INR 50,000,000 and 37% above. Dividends/capital-gain component exclusions and 15% caps in the cited tables must be applied, not a single percentage on every component. Apply marginal relief at each applicable threshold: tax plus surcharge cannot exceed threshold tax plus surcharge plus the excess income; cess follows. Special-rate/mixed-income cases are referred. [s.3(4)-(5), First Schedule I-B Paragraph F](https://egazette.gov.in/WriteReadData/2026/271439.pdf).
- Presumption requires the complete s.58 eligibility, receipt-timing and higher-actual-profit tests. Profession under s.62(4) is not automatically any freelance activity. Serial 1 excludes specified professions, commission/brokerage and agency business and requires no Chapter VIII-C deduction; resident individual/HUF/non-LLP firm only. Serial 3 covers specified resident individual/non-LLP firm; this package remains individual-only. Non-account-payee cheque/draft counts as cash. Lower-profit and serial 1 lockout books/audit conditions remain operative. [ss.58,62,63; Finance Act 2026s.40](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [amendment](https://egazette.gov.in/WriteReadData/2026/271439.pdf).
- Rule 164(6) has 15 ITR 4 bars: foreign assets/signing authority/income; s.10 apportionment; nonpermitted s.93 deduction; director; unlisted equity; income above INR 5,000,000; more than 2 chargeable house properties; brought-forward/carryforward loss; income with TDS in another person's hands; relief/deduction condition in(6)(l); agriculture above INR 5,000; deferred-ESOP tax; Part A of Chapter XIII special-rate income. The incomplete cross-reference in(6)(l) is not silently repaired: hold such a case. Rule 164(5) capital-gain permission and(6)(o) special-rate bar also require resolution before using ITR 4 for gains; do not assume a final utility will accept it. [entire rule 164](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
- Form 26 under rule 47 uses Part A if audited under another law, Part B otherwise, with particulars in Part C/D. Section 63 audit report is due 1 month before applicable return due date (period in words on the page); required-audit status governs even if the audit has not actually been performed. Final TY 2026-27 utility fields are unconfirmed. [rule 47](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf); [s.63](https://egazette.gov.in/WriteReadData/2025/265620.pdf).
- GST registration: s.22 general threshold is INR 2,000,000; the 4 special-category States Manipur, Mizoram, Nagaland and Tripura use INR 1,000,000, subject to any applicable notified enhancement/exemption. Exclusive-goods INR 4,000,000 exemption under Notification 10/2019 excludes compulsory s.24 registration, the 10 named States/UT, voluntary/continuing registrants and specified goods. The excluded States/UT are Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Puducherry, Sikkim, Telangana, Tripura and Uttarakhand. Goods excluded: ice cream/other edible ice; pan masala; tobacco/manufactured substitutes; from 1April 2022 specified fly-ash bricks/aggregate/blocks, fossil-meal/siliceous-earth bricks, building bricks and earthen/roofing tiles with the notification's tariff headings. Do not turn INR 4,000,000 into a universal threshold. [Notification 10/2019](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-10-central-tax-english-2019.pdf); [2022amendment](https://gstcouncil.gov.in/sites/default/files/2024-05/03_2022_ct_eng_0.pdf); [s.22](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html). Thresholds in words on the respective pages; classification/compulsory-registration exceptions go to `india-gst`.
- QRMP requires option under rule 61A, preceding-FY aggregate turnover up to INR 50,000,000 and prior due return filed; option continues until revised. Crossing the limit during a quarter means monthly filing from the first month of the succeeding quarter. First 2months' PMT 06 deposit is generally due 25th of next month; quarterly 3B is 22nd/24th after quarter by full State group in rule 61. Recover the exact group for the GSTIN, and check period-specific extensions. [Notification 84/2020](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-84-central-tax-english-2020.pdf); [rule 61](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html).
- ITC requires invoice/document, communicated supplier details, receipt, tax paid and return; the 180 day nonpayment rule (except reverse charge), repayment/interest and later reavailment must be reviewed. GST component depreciated for income tax cannot also be credited. General 30November/earlier annual-return cutoff has the s.16(5) legacy-year and s.16(6) revoked-cancellation exceptions; refer those rather than applying the ordinary cutoff mechanically. [s.16](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html).
- Annual return depends on s.44 exclusions/notified exemptions for the actual FY; no old small-taxpayer exemption is projected into 2026-27. Default 31December 2027 is derived from rule 80 if required, subject to extensions. Delayed s.50(1) tax interest generally follows the cash-ledger portion for late s.39 returns, with the proceedings exception in the statute; wrong ITC availed AND utilized is a separate s.50(3) issue whose rate/computation is not supplied by the old Notification 13/2017 alone. [s.44](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section44_v1.00.html); [s.50](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section50_v1.00.html).

### Section 2: Execution order and dependency chain

Run the content Guides in this order:

1. **`india-gst`**: GSTR-3B and GSTR-1 reconciliation. Runs first because GST turnover feeds the income-tax return. Reconcile GSTR-3B summaries with the books; check GSTR-1 outward supplies against invoices; reconcile input tax credit claimed with the auto-populated GSTR-2B. Output: GST turnover, output tax, input tax credit used, cash GST paid, reverse charge.
2. **`india-income-tax`**: the return (ITR-3, or SUGAM ITR-4 for presumptive income). Depends on the GST output: gross receipts must agree with GST turnover (excluding GST for a regular registrant). For presumptive income under section 58(2) Table serial 3 (specified profession), deemed profit is 50% of gross receipts, or a higher profit actually earned; no expense schedule. For actual profit: full profit and loss account, depreciation schedule and balance sheet. Output: total income, tax at the applicable rates, regime comparison if requested.
3. **`in-advance-tax`**: advance tax reconciliation. Depends on the return: final tax decides whether advance tax was enough. Reconcile advance tax paid against the liability, compute section 424 interest (default) and section 425 interest (deferment). Output: advance tax schedule, shortfalls, interest.
4. **`in-tds-freelance`**: TDS credit reconciliation. Depends on the return: TDS credits reduce final tax. Reconcile the tax credit statement and Form No. 168 (the Annual Information Statement from tax year 2026-27) with income declared; flag mismatches. If that Guide cannot produce output, compute the reconciliation from the tax credit statement collected at intake and flag in the reviewer brief that the dedicated Guide was not used. Output: TDS credit summary, mismatches.

- **Upstream failure.** If any content Guide fails to produce a validated output, note the failure in the reviewer brief and continue with available data as a partial draft. Do not substitute 0 for an unknown or present incomplete output as ready to file.

### Section 3: Cross-Guide reconciliation

#### Cross-check 1: GST turnover agrees with gross receipts in the return

| GST output | Return input | Rule |
| --- | --- | --- |
| GSTR-3B turnover (excluding GST) | Gross receipts from business or profession | Must agree; explain every difference in the reviewer brief |
| GSTR-1 outward supplies | Business schedule or presumptive turnover | Turnover excludes GST for regular registrants |
| Exports of services | Gross receipts | Included in gross receipts. A transaction verified to qualify as an export of services is a "zero rated supply" under [section 16(1) of the IGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chaptervii/section16_v1.00.html); supply without payment of integrated tax is "under bond or Letter of Undertaking" (section 16(3)) |

**If they differ:** flag for the reviewer; do not force totals to match. A foreign customer alone does not prove an export; verify the export/place-of-supply conditions in `india-gst`, otherwise hold GST treatment. Common causes: timing (invoice date versus receipt), reverse charge supplies, credit notes, advances received for services not yet supplied.

#### Cross-check 2: presumptive income means no further deductions

The rules are in section 58 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

| Rule | Application |
| --- | --- |
| Section 58(2) Table serial 3: deemed profit is 50% of gross receipts or the profit claimed to have been actually earned, whichever is higher (separate table cells read together, not interleaved PDF extraction) | No deduction for actual expenses against that income. Section 58(4): "Any loss, allowance or deduction allowable under the provisions of this Act, shall not be allowed against the income computed" this way |
| Depreciation | Not claimed. Section 58(6): the written down value of an asset is computed as if depreciation had been claimed and allowed for each year |
| Who may use serial 3 | A "specified assessee": an individual or a firm, other than a limited liability partnership, resident in India. The profession must be a specified profession in section 62(4): legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration, information technology or company secretary, or one notified by the Board |
| Who may use serial 1 (business) | An "eligible assessee": resident individual, HUF or firm other than an LLP that does not carry on a specified profession, earns no commission or brokerage and carries on no agency business, and section 58(11)(a)(ii): no Chapter VIII-C deduction claimed for the year |
| Deductions from total income | Only otherwise eligible Chapter VIII deductions where the old regime is chosen; on the new regime, section 202(2)(a)(xii) allows only sections 124(1), 124(2), 125(2) and 146 of Chapter VIII. These come off total income, not business income |

**If violated:** if the computation claims actual expenses AND declares presumptive profit, the check fails. It is one or the other.

**Lower profit than presumptive.** Section 58(3): a person who claims profit lower than the presumptive amount, and whose total income exceeds the maximum amount not chargeable to tax, must keep books under section 62 and get them audited under section 63.

**Leaving the business scheme.** Section 58(7): an eligible assessee who uses serial 1 for a tax year and, in any of the 5 tax years after it, declares profit otherwise, cannot use the section for the 5 tax years after the year of departure (figure in the Act table above). Section 58(8) then requires books and audit if total income exceeds the maximum amount not chargeable to tax.

#### Cross-check 3: advance tax and TDS against the final liability

| Component | Source | Rule |
| --- | --- | --- |
| Advance tax paid | Tax credit statement and challans | Sum of all advance tax payments for tax year 2026-27 |
| TDS credits | Tax credit statement, Form No. 168, TDS certificates | Sum of TDS deducted and deposited |
| Self-assessment tax | Challans | Paid before filing |
| Total liability | Return computation | Tax on total income plus surcharge plus cess; show s.423/424/425 interest and s.428 fees separately, then add for total cash payable |
| Payable or refund | Liability minus (advance tax plus TDS plus self-assessment tax) | Derived tax balance only: positive = tax payable; negative = provisional refund. Add separately computed interest/fees; allocate s.266(3) payments to fees first, then interest, then tax; unresolved credits are not a final refund |

- **Section 424 (default).** A person liable to advance tax under section 404 who paid none, or paid less than 90% of "assessed tax", pays simple interest of 1% for every month or part of a month from 1 April following the tax year to the date total income is determined under section 270(1), or to the completion of regular assessment where one is made. Interest is on the assessed tax where nothing was paid, or on the shortfall. "Assessed tax" is tax on the total income as reduced by TDS and tax collected at source, among other credits listed in section 424(2). Rates in the Act table above.
- **Section 425 construction hold.** The s.425(1) table shows ordinary cumulative shortfalls at 15%,45%,75%,100% and 3%,3%,3%,1% interest respectively. Section 425(2) says no subsection 1 interest if June paid at least 12% or September at least 36%, but prints no connector between clauses. Section 425(3) includes both serial 1/3 presumptive assessees and the further phrase "or, who is liable to pay advance tax under section 404". The latter wording creates a material interaction with the ordinary schedule. Preserve these statutory provisions and the conventional June/September-only interpretation as a conditional working, not a resolved rule. Use `in-advance-tax`'s explicit hold; do not deliver a final ordinary-case s.425 amount until the construction is resolved against authoritative text/guidance. No generic software assumption settles it. [s.425(1)-(6)](https://egazette.gov.in/WriteReadData/2025/265620.pdf).
- **Section 425(3), presumptive.** For a serial 1/3 case with a March shortfall the provision states 1% on the shortfall; complete payment by 15March avoids that shortfall. The ordinary-case scope remains held as above.
- Section 425(4): no interest under 425(1) or (3) on a shortfall caused by under-estimating capital gains, dividends, or business or profession income "accruing or arising for the first time", or winnings under section 2(49)(n), if the tax on it is paid in the remaining instalments or by 31 March.
- **Section 423 (late return).** Interest of 1% a month on the tax on total income as reduced by tax paid, for each month from the day after the due date (section 423(2) Table).

**Advance tax schedule, section 408**

| Instalment | Due date | Cumulative share required |
| --- | --- | --- |
| First | 15 June | 15%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Second | 15 September | 45%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Third | 15 December | 75%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Fourth | 15 March | 100% (whole amount); https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- **Presumptive single instalment.** Section 408(2): a person who declares profit under section 58(2) Table serial 1 or 3 pays the whole advance tax on or before 15 March. The Department confirms this "remains the same as under the old Act" ([tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq), question 19).
- **Threshold.** Advance tax applies only when the tax for the year is INR 10,000 or more (section 404). A resident aged 60 or more at any time in the tax year is not liable to advance tax under section 403(3) only if they have no income under "Profits and gains of business or profession"; a self-employed senior gets no age exemption but is liable only if the net s.404 computation reaches INR 10,000.
- **Timing on 14 November 2026.** The June and September dates for tax year 2026-27 have passed. A presumptive client still has until 15 March 2027. A four-instalment client who missed them should pay the supported tax shortfall now; show s.425 only as a conditional working under the construction hold.

#### Cross-check 4: tax credit statement against income in the return

| Check | Rule |
| --- | --- |
| Every TDS entry on the tax credit statement and Form No. 168 | The matching income must appear in the return |
| TDS credit claimed in the return | Must equal the statement; explain every difference |
| Section of deduction | Payments from 1 April 2026 are deducted under a table item of section 393; the Department warns that quoting "old section numbers such as 194C, 194J, or 194H" for such transactions "may result in system -level validation errors" ([tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)) |
| Tax collected at source entries | Credit against the liability, if any |

**If they differ:** common causes are a deductor's late TDS statement, a wrong PAN quoted, or income booked in a different year. Flag for the reviewer with the specific entries. A missing entry is corrected by the deductor.

### Section 4: Final reviewer package contents

#### Documents

1. **Executive summary**: one page: filing status, income, tax liability, GST position, advance tax, TDS credits, refund or balance due.
2. **GST reconciliation worksheet**: GSTR-3B against books, GSTR-1 against invoices, input tax credit reconciliation.
3. **Return computation worksheet**: ITR-3 or SUGAM (ITR-4), with all heads of income, deductions and the tax computation.
4. **Depreciation schedule**: asset register with block, cost, date, rate, allowance, written down value (actual-profit returns only).
5. **Advance tax reconciliation**: instalments against requirement, section 424 and 425 interest.
6. **TDS credit reconciliation**: tax credit statement against the return, mismatches flagged.
7. **Cross-Guide reconciliation summary**: all four cross-checks with pass or fail and notes.
8. **Reviewer brief**: narrative with positions, citations, flags and self-check results.
9. **Client action list**: what the client must do, with dates and amounts.

#### Reviewer brief contents

~~~markdown
# Complete Return Package: [Client Name], tax year 2026-27 (Income-tax Act 2025)

## Executive Summary
- Filing status: [Individual, resident (not RNOR)]
- Age at any time in the tax year: [below 60 / 60 to 79 / 80 or more]
- Business: self-employed professional / sole proprietor
- Tax regime: [new regime, section 202 / old regime, opted out under section 202(4)]
- Basis: [section 58(2) serial 3 profession / section 58(2) serial 1 business / actual profit]
- Return form: [ITR-3 / SUGAM (ITR-4)]
- Return due date: [31 August 2027 (no audit) / 31 October 2027 (audit)]
- GST registration: [regular / composition / unregistered]
- Gross receipts: INR X
- Deemed profit (section 58) / net profit (actual): INR X
- Total income: INR X
- Tax liability (including surcharge and cess): INR X
- Advance tax paid: INR X
- TDS credits: INR X
- Self-assessment tax paid: INR X
- Balance due / refund: INR X
- Section 424 interest (if any): INR X
- Section 425 interest (if any): INR X
- GST annual position: output INR X, input tax credit INR X, cash paid INR X

## GST Returns
[From india-gst output]
- Registration type and State
- GSTR-3B summary, monthly or quarterly
- GSTR-1 outward supply reconciliation
- Input tax credit claimed against GSTR-2B
- Reverse charge liability
- Zero-rated exports and Letter of Undertaking status
- Aggregate turnover for the year

## Income-tax Return (ITR-3 / SUGAM ITR-4)
[From india-income-tax output]
- Gross receipts from business or profession
- Deemed profit (section 58) or actual profit and loss
- Depreciation schedule (actual profit only)
- Income under other heads
- Deductions: Chapter VIII (old regime) or those section 202(2) keeps (new regime); standard deduction under section 19(1) if there is salary
- Total income
- Tax at the applicable rates
- Surcharge (only if total income exceeds the first surcharge threshold)
- Health and Education Cess
- Rebate under section 156 (resident individuals, if within the limit)
- Total tax liability

## Advance Tax Reconciliation
[From in-advance-tax output]
- Payments made (dates and amounts)
- Required cumulative shares at each date (section 408)
- Shortfall at each date
- Section 424 interest (advance tax under the section 424(1)(b) share of assessed tax)
- Section 425 interest (deferment)
- Total interest

## TDS Credit Reconciliation
[From in-tds-freelance output or computed from the tax credit statement]
- Deductor-wise summary
- Section 393 table item for each deduction (payments from 1 April 2026)
- Tax credit statement against the return
- Mismatches and resolution notes
- Tax collected at source (if any)

## Cross-Guide Reconciliation
- GST turnover against gross receipts: [pass/fail]
- Presumptive income with no expense deduction: [pass/fail or N/A]
- Advance tax plus TDS against final liability: [pass/fail]
- Tax credit statement against income: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream Guides]
- Regime choice; whether an opt-out was exercised by the section 263(1) due date
- Presumptive lock-out under section 58(7) if moving off serial 1
- Mixed-use expense percentages (phone, internet), actual profit only
- Home office claim, actual profit only
- Zero-rated exports: Letter of Undertaking and receipt of export proceeds
- PAN-Aadhaar link status
- Section 424 and 425 interest exposure
- GST registration threshold, if turnover is approaching it
- Unexplained items in Form No. 168

## Positions Taken
[List with legislation citations]
- e.g. "Presumptive income under section 58(2) Table serial 3 of the Income-tax Act 2025: specified profession under section 62(4); gross receipts within the higher limit because cash received is within the section 58(2) cash share"
- e.g. "New tax regime under section 202(1); no opt-out under section 202(4)"
- e.g. "Export of services: zero rated supply under section 16(1)(a) of the IGST Act, supplied under a Letter of Undertaking"
- e.g. "Laptop capitalised and depreciated in the computers block" (actual profit only; the reviewer confirms the rate)

## Planning Notes for Tax Year 2027-28
Planning only under currently enacted law; recheck Finance Act 2027 and notifications before using these dates/amounts.
- Advance tax schedule (instalments with amounts and dates)
- GST calendar (monthly GSTR-3B, or quarterly with GSTR-1 under QRMP)
- Presumptive lock-out tracking under section 58(7), if relevant
- Depreciation carried forward (written down value)
- Regime review for the next year
- Changes made by the next Finance Act

## Client Action List

### Before the return due date (31 August 2027, or 31 October 2027 if the accounts must be audited):
1. Review this package with your Chartered Accountant
2. Pay self-assessment tax of INR X (if a balance is due)
3. File the return on the Income Tax Department's e-Filing portal
4. Verify the return after filing, as the portal requires

### If a tax audit is required (section 63):
1. The audit report in Form No. 26 is due 1 month (in words on the page) before the return due date
2. The return due date is 31 October 2027

### Advance tax for tax year 2027-28:
1. 15 June 2027: first instalment, the section 408 share of estimated tax = INR X
2. 15 September 2027: cumulative section 408 share = INR X
3. 15 December 2027: cumulative section 408 share = INR X
4. 15 March 2028: the whole amount = INR X
(If section 58(2) serial 1 or 3: the whole amount by 15 March 2028 in one instalment)

### GST calendar:
- GSTR-3B: 20th of following month (in words on the page) (quarterly filers: 22nd or 24th (in words on the page) after the quarter, by State)
- GSTR-1: 11th of following month (in words on the page) (quarterly filers:13th of month after quarter (in words on the page))
- GSTR-9 for 2026-27: default 31December 2027 (derived), if required and no notified exemption/extension; GSTR 9C if aggregate turnover exceedsINR 50,000,000

### Ongoing:
1. Issue GST tax invoices for all taxable supplies
2. Keep books of account (actual profit) or records of receipts (presumptive)
3. File GSTR-3B and GSTR-1 on time
4. Pay advance tax by each due date
5. Collect TDS certificates from clients
6. Monitor aggregate turnover against the GST registration threshold
7. Keep GST records for 72months (in words on the page) from the due date of the annual return, or 1 year after final disposal of the relevant appeal/revision/proceeding/investigation if later; keep income-tax books for the period the Income-tax Rules 2026 prescribe under section 62
~~~

### Section 7: Output files

The final output is **three files**:

1. **`[client_slug]_2026-27_india_master.xlsx`**: one workbook with every worksheet and computation. Sheets: Cover, GST Reconciliation (GSTR-3B against books), Return Computation (ITR-3 or ITR-4), Depreciation Schedule (actual profit only), Advance Tax Reconciliation, TDS Credit Reconciliation, Section 424 and 425 Interest, Cross-Check Summary. Use live formulas where possible: the gross receipts cell references the GST turnover cell; the advance tax shortfall references the final liability. Check there are no `#REF!` errors and that computed values agree before shipping.
2. **`reviewer_brief.md`**: one markdown file covering all of Section 4: executive summary, GST, return, advance tax, TDS, cross-Guide reconciliation, flags, positions, planning notes.
3. **`client_action_list.md`**: one markdown file with step-by-step actions: filings and payments, the next year's advance tax calendar, the GST calendar, ongoing compliance reminders.

If execution runs out of context mid-build, produce whatever is complete, then state at the end which of the three files were not produced or are partial.

Save the three files and present them to the user.

### Section 8: Cross-Guide references

**Inputs:**

- `in-freelance-intake`: structured intake package
- `india-gst`: GSTR-3B and GSTR-1 reconciliation output
- `india-income-tax`: return computation
- `in-advance-tax`: advance tax reconciliation and interest
- `in-tds-freelance`: TDS credit reconciliation (or the fallback computation from the tax credit statement)
- `in-tax-residency`: only if residence is in doubt

**Outputs:** the final reviewer package. No downstream Guide.

### Section 9: Known gaps

1. Filling the official return is not automated. The reviewer uses the worksheets to complete the return on the e-Filing portal.
2. Filing is done by the reviewer on the portal, not by this Guide.
3. Payment is the client's responsibility; this Guide gives instructions and amounts.
4. The tax audit report (Form No. 26) is not prepared here. If an audit is required, this Guide flags it and the Chartered Accountant prepares the report.
5. If `in-tds-freelance` cannot produce output, the TDS reconciliation is computed from the tax credit statement collected at intake.
6. Multi-year depreciation assumes the prior year schedule is provided. If not, show current-year additions separately, flag missing opening written-down values and block final depreciation/return totals; never assume earlier assets have a 0 allowance.
7. Capital gains computation is out of scope.
8. Foreign assets and foreign income reporting are out of scope.
9. Rental income is out of scope beyond noting it as other income.
10. The package covers tax year 2026-27 only; the next year appears only as planning.
11. State professional tax is taken from intake, not computed (see `in-professional-tax`).
12. The precise current non-salary TDS certificate/portal fields need the period-specific `in-tds-freelance` mapping. Current rule 136 is confirmed: regime option/withdrawal goes in the timely return itself, not an assumed replacement standalone Form 10-IEA. Final current-year utility fields remain unconfirmed.

## Worked cases

All figures below are hypothetical inputs or derived outputs. Assume resident individual, eligible income classification, new regime, no special-rate income, surcharge, loss, other deductions or unverified GST export status. Use confirmed sibling output for any omitted issue; neither example proves final portal acceptance.

### Case 1: professional presumption and matched credits

Eligible professional receipts INR 4,000,000, all banked and within s.58 serial 3 conditions; no higher actual profit claimed. Profit is 50%=INR 2,000,000. New-regime slab tax is INR 200,000, cess INR 8,000, total INR 208,000. Matched TDS INR 150,000 leaves advance-tax target INR 58,000; INR 60,000 paid by 15March 2027 fully covers it. With no late filing/fees and no March advance shortfall, provisional refund is INR 2,000. Match GST/books receipts separately; no GST rate is invented here. [s.58/202/408/425](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [cess s.3(15)](https://egazette.gov.in/WriteReadData/2026/271439.pdf).

```oa-check
name: India return assembly professional presumption and matched credits
inputs:
  receipts: 4000000
  tds: 150000
  advance: 60000
steps:
  profit: receipts * 0.50
  slab_tax: 400000 * 0.05 + 400000 * 0.10 + 400000 * 0.15 + (profit - 1600000) * 0.20
  cess: slab_tax * 0.04
  total_tax: slab_tax + cess
  advance_target: max(0, total_tax - tds)
  refund: tds + advance - total_tax
expected:
  profit: 2000000
  slab_tax: 200000
  cess: 8000
  total_tax: 208000
  advance_target: 58000
  refund: 2000
```

### Case 2: a missing TDS credit changes the handover decision

Actual-profit receipts INR 3,000,000 less supported expenses INR 1,000,000 and separately verified depreciation INR 200,000 gives INR 1,800,000 income; depreciation is a supplied verified input, not a rate calculation. Slab tax is INR 160,000 and cess INR 6,400, total INR 166,400. Claimed TDS INR 170,000 would suggest INR 3,600 refund, but the statement supports only INR 150,000, leaving INR 16,400 tax before interest/fees. The INR 20,000 discrepancy is sent for deductor/reviewer correction; do not release the apparent refund or invent an interest amount without dated payments and the s.425 resolution. [s.202](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [cess](https://egazette.gov.in/WriteReadData/2026/271439.pdf); [credit mismatch FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/Tax%20Credit%20Mismatch%20-FAQ).

```oa-check
name: India return assembly actual profit TDS discrepancy decision
inputs:
  receipts: 3000000
  expenses: 1000000
  depreciation: 200000
  claimed_tds: 170000
  statement_tds: 150000
steps:
  profit: receipts - expenses - depreciation
  slab_tax: 400000 * 0.05 + 400000 * 0.10 + 400000 * 0.15 + (profit - 1600000) * 0.20
  cess: slab_tax * 0.04
  total_tax: slab_tax + cess
  claimed_refund: claimed_tds - total_tax
  supported_balance: total_tax - statement_tds
  discrepancy: claimed_tds - statement_tds
expected:
  profit: 1800000
  slab_tax: 160000
  cess: 6400
  total_tax: 166400
  claimed_refund: 3600
  supported_balance: 16400
  discrepancy: 20000
```

## When to refuse or refer

Refuse and refer to a Chartered Accountant:

- Income of 1 April 2025 to 31 March 2026 (1961 Act). Use `india-income-tax` or refer.
- Non-resident, not ordinarily resident, or residence in doubt: use `in-tax-residency` first.
- HUF, firm, LLP or company.
- Section 172 (transfer pricing report) applies.
- Tax audit required: this Guide flags it; the Chartered Accountant performs the audit and files Form No. 26.
- Foreign assets, foreign income or treaty relief; capital gains beyond SUGAM (ITR-4) limits; virtual digital assets (see `india-crypto-tax`).
- A pending notice, scrutiny or demand.

Continue with a partial draft but flag for the reviewer; do not release an unresolved filing figure:

- Profit declared below the presumptive rate, or a move off section 58(2) serial 1 (section 58(7) and 58(8)).
- Work whose place in the section 62(4) list of specified professions is unclear.
- Any GST point that `india-gst` flagged.
- Proposals that are not law: the 57th GST Council meeting of 8 October 2026 recommended changes, including to late fees and penalties ([press release](https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf)). The release is evidence of recommendations, not proof that no later implementing notification exists. Recover any operative amendment before using a waiver. It describes them as recommendations, for example "The GST Council recommended an amendment to rule 19 of the CGST Rules, 2017". Do not apply them until the amended law is notified.

### Assembly failure codes

- **R-IN-1**: upstream Guide did not run. Name it. This is a warning, not a hard stop. Continue with the data available and flag the gap; the affected package remains partial until resolved.
- **R-IN-2**: upstream self-check failed. Name the check and note it in the reviewer brief. Continue.
- **R-IN-3**: cross-Guide reconciliation failed. Name it and describe the difference. Flag for the reviewer and continue.
- **R-IN-4**: intake incomplete. Specific missing items prevent computation. List them and ask the user for each.
- **R-IN-5**: out-of-scope item found during assembly, for example capital gains beyond what SUGAM (ITR-4) allows, rental income, foreign assets or income, or partnership income. Flag it and exclude it from this limited working only. State that the working omits income/assets and is not a complete return; obtain the separate computation before final totals or filing.
- **R-IN-6**: wrong year. The client's income is for 1 April 2025 to 31 March 2026. Stop: that return is under the 1961 Act; use `india-income-tax`.

## Filing and payment

Prepare the 3 files and dated instructions specified above; the reviewer completes and verifies the period-specific return through the official e-Filing portal. Follow the actual rule 164 verification mode (DSC/EVC/ITR-V as applicable); do not assume an electronic upload alone completes filing. Separate payment receipt from return acknowledgement, and confirm the selected tax year. Rule 164(11) makes the return annexure-less: retain supporting computations/certificates for review rather than attaching them indiscriminately. Final portal boxes/deadlines for verification must be confirmed when the TY 2026-27 utility is released. [rule 164](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

For payment, use the official [e-Pay Tax workflow](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax), retain challan/receipt and reconcile to the statement; distinguish old-year payment from current-year payment. No filing/payment is made by this assembly instruction.

## Completion checklist

- **Check IN-A 1**: all upstream Guides ran. `india-gst`, `india-income-tax`, `in-advance-tax` produced output; `in-tds-freelance` produced output or the reconciliation was computed from the tax credit statement.
- **Check IN-A 2**: GST turnover agrees with gross receipts in the return, or every difference is explained.
- **Check IN-A 3**: if section 58(2) serial 3: profit declared is at least 50% of gross receipts, and no expenses are deducted.
- **Check IN-A 4**: advance tax and TDS reconciled against the final liability. Credits (advance tax plus TDS plus self-assessment tax) match the payment or refund position.
- **Check IN-A 5**: section 424 interest correct. Applies if advance tax paid is under 90% of assessed tax; 1% simple per month or part of a month from 1 April after the tax year.
- **Check IN-A 6**: section 425 construction hold explicitly retained; any conditional ordinary-case working labelled, no final filing amount until resolved. Original conventional schedule, retained conditionally: 3% flat on the shortfall at each of the first three dates (subject to section 425(2), read as above), 1% on the shortfall at 15 March. Presumptive cases (section 58(2) serial 1 or 3): section 425(3) provides 1% on the shortfall at 15 March.
- **Check IN-A 7**: tax credit statement matches the return. Every TDS entry has income in the return; credits claimed equal the statement.
- **Check IN-A 8**: regime applied correctly. New regime: section 202(1) rates, and only the deductions section 202(2) keeps. Old regime: rates in the Finance Act 2026 First Schedule Part I-B Paragraph A, and only if a valid saved prior option continues or the current option was exercised in the timely return by the section 263(1) due date (section 202(4)(a)(i)).
- **Check IN-A 9**: rebate applied if eligible. New regime, resident individual: if income does not exceed INR 1,200,000 (in words on the page), rebate of 100% of eligible tax or INR 60,000, whichever is less, capped to s.202(1) slab tax under s.156(3), with the marginal relief in section 156(2)(b) just above the limit. Old regime: INR 12,500 if total income does not exceed INR 500,000.
- **Check IN-A 10**: surcharge and cess correct. Surcharge only above INR 5,000,000 of total income; cess at 4% on tax plus surcharge.
- **Check IN-A 11**: filing calendar complete. Every deadline for the return, GST, advance tax and TDS is listed with its date and amount.
- **Check IN-A 12**: every position cites its section of the Income-tax Act 2025, the CGST Act 2017, the IGST Act 2017 or the relevant rule.

## Sources

| Official source | Read for | Actual read date |
|---|---|---|
| https://egazette.gov.in/WriteReadData/2025/265620.pdf | Read for complete ss.19 salary table,58,62(4),63,156,202,263,266,403-410,423-425,536(2)(f); operative conditions and neighboring exceptions | 2026-11-14 |
| https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read for ss.3(1)-(5),(15),40,56,66,93-96 and First Schedule I-B Paragraph A/F: annual rates, surcharges, marginal relief, cess, due dates and fees | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | Read for rules 47,136 and entire 164, plus rules 75-76/neighboring context; audit, regime and return eligibility/verification | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq | Read for FAQ 2,21-26: repeal, period, presumption, regime and savings | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq | Read for FAQ 3-6,14-23: year selection, TDS transition, advance schedules and Form 168; statute controls over broad FAQ wording | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html | Read for entire operative CGSTs.16 and neighboring amendments: ITC conditions,180days, depreciation restriction, cutoff and legacy/revocation exceptions | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html | Read for entire CGSTs.22, explanations and amendments: registration thresholds, special States and enabling enhancement | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter8/section36_v1.00.html | Read for entire CGSTs.36 including proceedings/investigation longer-retention proviso | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chaptervii/section16_v1.00.html | Read for entire operative IGSTs.16 and adjacent amendments: exports/authorized SEZ zero rating, LUT/bond/refund conditions | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html | Read for entire current rule 61 including both State groups, PMT 06 monthly deposit and extension/refund conditions; historical footnote not used as current QRMP threshold | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html | Read for entire current rule 80 and historical amendments: annual return/GSTR 9C, default date/exclusions; no old exemption projected | 2026-11-14 |
| https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf | Read for whole 1 page notification: monthly 11th/quarterly 13th GSTR 1 and commencement | 2026-11-14 |
| https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-13-central-tax-english.pdf | Read for whole 1 page notification: s.50(1)18% delayed tax; old s.50(3)entry not used as current wrong-ITC rate | 2026-11-14 |
| https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf | Read for PDFpp.12-13 and 32 registration overview/neighboring paragraph; historical 2019 educational threshold account, not all 44pages | 2026-11-14 |
| https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf | Read for 57th meeting press-release introduction and late-fee/penalty/registration/export recommendations on PDFpp.9-11; recommendations require operative notification, not all 15pages | 2026-11-14 |
| https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-10-central-tax-english-2019.pdf | Read for whole 1 page: exclusive-goods INR 4 million exemption and all goods/State/compulsory/voluntary exclusions | 2026-11-14 |
| https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-10-central-tax-english-2019_corrgndm.pdf | Read for whole 1 page: numbering corrections from(iii)/(iv)to(c)/(d) | 2026-11-14 |
| https://gstcouncil.gov.in/sites/default/files/2024-05/03_2022_ct_eng_0.pdf | Read for whole 1 page: four added goods/tariff exclusions and 1April 2022 commencement | 2026-11-14 |
| https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-84-central-tax-english-2020.pdf | Read for whole 2pages: QRMP election, preceding return condition, continuing option and threshold-crossing consequence; historical default options not projected | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section44_v1.00.html | Read for entire operative section 44 and neighboring amendments: annual-return exclusions, notified exemptions and late window | 2026-11-14 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section50_v1.00.html | Read for entire operative section 50 and neighboring amendments: delayed-tax cash-ledger proviso/proceedings exception and separate wrong-ITC utilization rule | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/Tax%20Credit%20Mismatch%20-FAQ | Read for all 4questions: statement mismatch, deductor/challan corrections and credit reconciliation | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax | Read for FAQ 4-15 and 38: CRN, modes, receipts and erroneous payment handling | 2026-11-14 |

**Not yet confirmed:** final TY 2026-27 return utility/box fields and verification deadlines; defective rule 164(6)(l) cross-reference and rule 164(5)/(6)(o) capital-gain interaction before ITR 4 use; section 425(2)/(3) ordinary-case construction; case-specific GST classification/export/place-of-supply/compulsory-registration exceptions, annual-return exemptions and deadline extensions; current wrong-ITC interest rate/computation; specific special-rate/rebate/marginal-relief computations; prior depreciation values without opening schedules; final next-year law for 2027-28. Missing/upstream-failed/out-of-scope matters stay visible as partial-package blockers, never usable unsupported amounts. Current non-salary TDS certificate fields are taken only after the sibling period mapping is verified.

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant, tax practitioner, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

