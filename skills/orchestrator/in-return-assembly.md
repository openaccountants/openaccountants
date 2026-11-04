---
name: in-return-assembly
description: Final orchestrator skill that assembles the complete India filing package for India-resident self-employed individuals and professionals. Consumes outputs from all India content skills (india-gst for GSTR-3B/GSTR-1, in-income-tax for ITR-3/ITR-4, in-advance-tax for quarterly instalments, in-tds-freelance for TDS reporting) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all India content skills listed above. India full-year residents only. Self-employed individuals and professionals only.
version: 0.1
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# India Return Package Assembly for Self-Employed Residents

This Guide assembles the complete India filing package for a resident individual who is self-employed or practises a profession as a sole proprietor: the income-tax return, the advance tax and TDS reconciliation and the GST position, checked against each other and handed to a Chartered Accountant for review. Figures are for tax year 2026. That means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. GST is not year-based: the GST rules here are those in force on 17 October 2026, with their start dates. Income of 1 April 2025 to 31 March 2026 (assessment year 2026-27) stays under the 1961 Act and its return is not covered by this Guide; use `in-income-tax` and `in-freelance-intake` for it.

This Guide runs last. It does not repeat the computations of the content Guides; it orders them, checks that their outputs agree, and builds the reviewer package. A Chartered Accountant must review and sign off the package before anything is filed.

## Section numbers changed on 1 April 2026

The Income Tax Department states that "The 1961 Act stands repealed on the 01.04.2026" and that the law applicable to a tax payment "is determined by the year of income, not by the date of payment" ([new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq); [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)). For tax year 2026-27 use the 2025 Act numbers. The Department's own pages give these mappings:

| 1961 Act | Income-tax Act 2025 | Page that states it |
| --- | --- | --- |
| Section 115BAC (new tax regime) | Section 202 | [new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq), question 22 |
| Sections 44AD, 44ADA, 44AE (presumptive income) | Section 58, one table | [new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq) |
| Section 234B (interest for default in advance tax) | Section 424 | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq), question 20 |
| Section 234C (interest for deferment of advance tax) | Section 425 | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq), question 20 |
| TDS sections 192 to 194T | Sections 392 (salary) and 393 (other payments) | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq) |
| Annual Information Statement | Form No. 168 from tax year 2026-27 | [tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq) |

Every other 2025 Act section named below is cited by its new number only. The pages this Guide can read do not map the rebate, the return due dates, the tax audit or the standard deduction to their old numbers, so none is given.

## Figures the cross-checks use

### Income-tax Act 2025 (Act 30 of 2025, as enacted)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime (section 202(1), the default for individuals), any age: income taxed at nil up to | INR 400,000 | "1. Upto ₹400000 Nil" |
| New regime: rate on the next slice | 5% | "2. From ₹400001 to ₹800000 5%" |
| New regime: top of the 5% slice | INR 800,000 | "2. From ₹400001 to ₹800000 5%" |
| New regime: rate on the next slice | 10% | "3. From ₹800001 to ₹1200000 10%" |
| New regime: top of the 10% slice | INR 1,200,000 | "3. From ₹800001 to ₹1200000 10%" |
| New regime: rate on the next slice | 15% | "4. From ₹1200001 to ₹1600000 15%" |
| New regime: top of the 15% slice | INR 1,600,000 | "4. From ₹1200001 to ₹1600000 15%" |
| New regime: rate on the next slice | 20% | "5. From ₹1600001 to ₹2000000 20%" |
| New regime: top of the 20% slice | INR 2,000,000 | "5. From ₹1600001 to ₹2000000 20%" |
| New regime: rate on the next slice | 25% | "6. From ₹2000001 to ₹2400000 25%" |
| New regime: income above which the top rate applies | INR 2,400,000 | "7. Above ₹2400000 30%" |
| New regime: top rate | 30% | "7. Above ₹2400000 30%" |
| Rebate, section 156(2), resident individual on the new regime: 100% of tax or this amount, whichever is less | INR 60,000 | "(a) the income does not exceed twelve lakh rupees, 100% of the income-tax payable or ₹ 60000, whichever is less" |
| Rebate, section 156(2): income limit (printed in words) | twelve lakh rupees | "(a) the income does not exceed twelve lakh rupees" |
| Rebate, section 156(1), resident individual on the old regime: 100% of tax or this amount, whichever is less | INR 12,500 | "deduction of 100% of income-tax payable or ₹ 12500, whichever is less" |
| Rebate, section 156(1): available only if total income does not exceed | INR 500,000 | "chargeable on the total income for any tax year if such total income does not exceed ₹ 500000" |
| Standard deduction from salary, section 19(1) Table serial 2(a), new regime: this amount or the salary, whichever is less | INR 75,000 | "(a) ₹ 75000 or the salary, whichever is less, where income-tax is computed under section 202(1)" |
| Standard deduction from salary, section 19(1) Table serial 2(b), any other case (old regime) | INR 50,000 | "(b) ₹ 50000 or the salary, whichever is less, in any other case" |
| Presumptive business, section 58(2) Table serial 1: turnover limit (words) | two crore rupees | "(a) Does not (A) The aggregate business other assessee. exceed two" |
| Presumptive business: higher limit where cash receipts do not exceed 5% (words) | three crore rupees | "exceed three receipts which is against serial crore rupees" |
| Presumptive business and profession: cash share for the higher limit, not more than | 5% | "in cash, does not respect of that tax exceed 5% of year; the total" |
| Presumptive business: deemed profit on receipts by bank or other specified mode | 6% | "(i) 6% of total business (b) does not turnover or gross" |
| Presumptive business: deemed profit on the remaining turnover | 8% | "(ii) 8% of total turnover or turnover or gross" |
| Presumptive profession, section 58(2) Table serial 3: deemed profit share of gross receipts | 50% | "3. Specified Specified (a) Does 50% of the gross" |
| Presumptive profession: gross receipts limit (words) | fifty lakh rupees | "not exceed fifty receipts or profit as referred lakh rupees;" |
| Presumptive profession: higher limit where cash does not exceed 5% of gross receipts (words) | seventy-five lakh rupees | "seventy-five higher. lakh rupees" |
| Section 58(7): period barred after leaving the business scheme (words) | five tax years | "he shall not be eligible to claim the benefit of the provisions of this section for five tax years" |
| Tax audit, section 63(1) Table serial 1(a): business turnover above (words) | one crore rupees | "in business exceed or exceeds one crore rupees in any tax year" |
| Tax audit, serial 1(b): limit where cash receipts AND cash payments each do not exceed 5% (words) | ten crore rupees | "the words “ten crore rupees” had been substituted" |
| Tax audit, serial 1(b): cash share of receipts, and separately of payments, not more than | 5% | "in cash, does not exceed 5% of the said amount" |
| Tax audit, serial 1(c): profession gross receipts above (words) | fifty lakh rupees | "carrying on profession shall, if his gross receipts in profession exceed fifty lakh rupees" |
| Advance tax due (section 404) when the tax for the year is | INR 10,000 | "where the amount of such tax payable during that year, as computed under this Part, is ₹10000 or more" |
| Advance tax, section 408(1): by 15 June, not less than | 15% | "1. On or before Not less than 15% of such advance tax. the 15th June." |
| Advance tax: by 15 September, cumulative, not less than | 45% | "2. On or Not less than 45% of such advance tax" |
| Advance tax: by 15 December, cumulative, not less than | 75% | "3. On or Not less than 75% of such advance tax" |
| Interest for default in advance tax, section 424(1): simple, per month or part of a month | 1% | "the assessee shall be liable to pay simple interest at the rate of 1% for every month or part of a month" |
| Section 424(1)(b): interest applies where advance tax paid is less than this share of assessed tax | 90% | "is less than 90% of the assessed tax" |
| Interest for deferment, section 425(1): flat, on the shortfall at 15 June, 15 September and 15 December | 3% | "15% of the tax Shortfall till 15th day of 3% of June." |
| Interest for deferment, section 425(1) serial 4 and 425(3): on the shortfall at 15 March | 1% | "100% of the Shortfall till 15th day of 1% of March." |
| Section 425(2)(a): the Act says no section 425(1) interest if the amount paid by 15 June is this share or more of the tax due on the returned income. This Guide applies it to the June shortfall only; flag for the reviewer | 12% | "on or before the 15th day of June is 12% or more of the tax due on the returned income" |
| Section 425(2)(b): the Act says no section 425(1) interest if the amount paid by 15 September is this share or more of the tax due on the returned income. This Guide applies it to the September shortfall only; flag for the reviewer | 36% | "on or before the 15th day of September is 36% or more of the tax due on the returned income" |
| Interest for a late return, section 423(1): I = this rate x tax x months | 1% | "I = 1% x A x T" |
| Belated return, section 263(4): within this period from the end of the tax year (words) | nine months | "may furnish the return for any tax year at any time within nine months from the end of the relevant tax year" |
| Updated return, section 263(6)(a): within this period from the end of the financial year after the tax year (words) | forty-eight months | "at any time within forty-eight months from the end of the financial year succeeding the relevant tax year" |

### Finance Act 2026 (Act 4 of 2026, as enacted)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime (First Schedule Part I-B Paragraph A; only where the person opts out of section 202), under 60: nil band up to | INR 250,000 | "(1) where the total income does not Nil; exceed ₹ 250000" |
| Old regime, resident aged 60 to 79: nil band up to | INR 300,000 | "(1) where the total income does not Nil; exceed ₹ 300000" |
| Old regime, resident aged 80 or more: nil band up to (then 20%; no 5% slice) | INR 500,000 | "(1) where the total income does Nil; not exceed ₹ 500000 (2) where the total income 20%" |
| Old regime, under 60: rate on the slice above the nil band, up to INR 500,000 | 5% | "(2) where the total income exceeds 5% of the amount by which the total ₹ 250000" |
| Old regime: rate on the slice above INR 500,000 | 20% | "(3) where the total income exceeds ₹ 12500 plus 20% of the amount by ₹ 500000" |
| Old regime: income above which the top rate applies, all ages | INR 1,000,000 | "(4) where the total income exceeds ₹ 112500 plus 30% of the amount by ₹ 1000000" |
| Old regime: top rate | 30% | "(4) where the total income exceeds ₹ 112500 plus 30% of the amount by ₹ 1000000" |
| Surcharge, section 3(4) Table serial 10 (new regime): applies where total income exceeds | INR 5,000,000 | "exceeds ₹ 5000000 but does of an association of not exceed ₹ 10000000, at the" |
| Surcharge, new regime: rate from that threshold up to INR 10,000,000 | 10% | "not exceed ₹ 10000000, at the persons consisting of only rate of 10%;" |
| Surcharge, new regime: next threshold | INR 10,000,000 | "exceeds ₹ 10000000 but does not exceed ₹ 20000000, at the (v) every artificial rate of 15%;" |
| Surcharge, new regime: rate above INR 10,000,000 up to INR 20,000,000 | 15% | "exceeds ₹ 10000000 but does not exceed ₹ 20000000, at the (v) every artificial rate of 15%;" |
| Surcharge, new regime: threshold for the top rate (income excluding dividends and capital gains under sections 196 to 198) | INR 20,000,000 | "198 of the said Act) exceeds ₹ 20000000, at the rate of 25%;" |
| Surcharge, new regime: top rate | 25% | "198 of the said Act) exceeds ₹ 20000000, at the rate of 25%;" |
| Surcharge, old regime only (Table serial 1): rate where income excluding dividends and capital gains exceeds INR 50,000,000 | 37% | "exceeds ₹ 50000000, at the rate of 37%;" |
| Surcharge, old regime only: threshold for 37% | INR 50,000,000 | "exceeds ₹ 50000000, at the rate of 37%;" |
| Surcharge cap on the part of tax relating to dividends and capital gains (sections 196, 197, 198 under section 202; section 210(1) Table serial 2 to 5 for the old regime), both regimes | 15% | "the rate of surcharge on the income-tax in respect of that part of income shall not exceed 15%" |
| Health and Education Cess on income-tax plus surcharge | 4% | "calculated at the rate of 4% of such income-tax and surcharge" |
| Fee for a return not filed by the due date, section 428(a): total income not more than INR 500,000 | INR 1,000 | "(i) a sum of ₹ 1000, if the total income of such person does not exceed ₹ 500000" |
| Section 428(a): total income limit for the lower fee | INR 500,000 | "(i) a sum of ₹ 1000, if the total income of such person does not exceed ₹ 500000" |
| Section 428(a): fee in any other case | INR 5,000 | "(ii) a sum of ₹ 5000, in any other case; (b) furnishes a return" |
| Fee for not furnishing the section 63 audit report, section 428(c): delay up to one month | INR 75,000 | "(i) a sum of ₹ 75000 for a delay up to one month" |
| Section 428(c): after the first month | INR 150,000 | "(ii) a sum of ₹ 150000 thereafter; (d) fails to furnish a report from an accountant" |
| Revised return, section 263(5) as substituted: within this period from the end of the tax year, or before assessment, whichever is earlier (words) | twelve months | "furnish a revised return at any time within twelve months from the end of the relevant tax year" |

Return due dates, section 263(1)(c) as substituted by section 66 of the Finance Act 2026 (same page). The date falls in the financial year after the tax year, so tax year 2026-27 returns are due in 2027:

| Person | Due date | Note |
| --- | --- | --- |
| Source | all dates below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Business or profession whose accounts need no audit, where section 172 (transfer pricing report) does not apply | 31 August | "3. (i) Assessee having income Where the 31st August." |
| Accounts required to be audited under the 2025 Act or any other law, section 172 not applying | 31 October | "2. (i) Company; Where the 31st October." |
| Section 172 applies | 30 November | "Where the 30th November." |
| Any other assessee (no business or profession income) | 31 July | "4. Any other assessee. 31st July." |

### Income-tax Rules 2026 (notified 20 March 2026)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| SUGAM (ITR-4), rule 164(5)(b): long-term capital gains under section 198 allowed up to | INR 125,000 | "has only long-term capital gains under section 198 not exceeding ₹ 125000" |
| ITR-4 bar, rule 164(6)(h): total income exceeding (words) | fifty lakh rupees | "(h) has total income, exceeding fifty lakh rupees" |
| ITR-4 bar, rule 164(6)(m): agricultural income exceeding | INR 5,000 | "has agricultural income, exceeding ₹ 5000;" |

### GST: CGST Act 2017, section 22 (registration)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html |
| Registration needed when aggregate turnover in a financial year exceeds (words; statute figure, States other than special category States; suppliers of goods only may have a higher threshold, row below) | twenty lakh rupees | "if his aggregate turnover in a financial year exceeds twenty lakh rupees" |

### GST: CBIC "GST: An Update" (1 June 2019)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |
| Registration threshold for suppliers of services (other than Manipur, Mizoram, Nagaland and Tripura) | INR 20 lakh | "for suppliers of services would be Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and" |
| Registration threshold for suppliers engaged exclusively in goods, in States that adopted it | INR 40 lakh | "for the suppliers of goods would be Rs. 40 lakhs and Rs. 20 lakhs" |

### GST: Notification 83/2020-Central Tax (GSTR-1)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf |
| GSTR-1 due date, monthly filers | eleventh day of the following month | "till the eleventh day of the month succeeding such tax period" |
| GSTR-1 due date, quarterly (QRMP) filers | thirteenth day of the month after the quarter | "shall be extended till the thirteenth day of the month succeeding such tax period" |

### GST: CGST Rules, rule 61 (GSTR-3B)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html |
| GSTR-3B due date, monthly filers | twentieth day of the following month | "for each month, or part thereof, on or before the twentieth day of the month succeeding such month" |
| GSTR-3B due date, quarterly filers in the first State group named in rule 61 | twenty-second day of the month after the quarter | "Lakshadweep. twenty-second day of the month succeeding such quarter" |
| GSTR-3B due date, quarterly filers in the second State group named in rule 61 | twenty-fourth day of the month after the quarter | "Ladakh, Chandigarh or Delhi. twenty-fourth day of the month succeeding such quarter" |
| Quarterly provisos apply to aggregate turnover in the previous financial year up to (words) | five crore rupees | "for taxpayers having an aggregate turnover of up to five crore rupees in the previous financial year" |

### GST: CGST Rules, rule 80 (annual return)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html |
| GSTR-9 due date | thirty-first day of December | "electronically in FORM GSTR-9 on or before the thirty-first day of December following the end of such financial year" |
| GSTR-9C (self-certified reconciliation statement) needed when aggregate turnover exceeds (words) | five crore rupees | "whose aggregate turnover during a financial year exceeds five crore rupees, shall also furnish a self-certified" |

### GST: CGST Act, section 16 (input tax credit time limit)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html |
| Last date to take credit for an invoice of a financial year, or the annual return filing date if earlier | thirtieth day of November | "after the 6 [thirtieth day of November] following the end of financial year to which such invoice or" |

### GST: CGST Act, section 36 (keeping records)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter8/section36_v1.00.html |
| Retain GST books and records until this period after the due date of the annual return for the year (words) | seventy-two months | "shall retain them until the expiry of seventy-two months from the due date of furnishing of annual return" |

### GST: Notification 13/2017-Central Tax (interest)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-13-central-tax-english.pdf |
| Interest a year on tax paid late, section 50(1) | 18% | "Sub-section (1) of section 50 18" |

## What this file is

The final capstone Guide for India self-employed returns. Every India content Guide feeds into this one. The output is the complete reviewer package that a Chartered Accountant can review, sign off and deliver to the client with filing instructions.

This Guide coordinates the content Guides, checks cross-Guide consistency and assembles the final deliverable. Run the content Guides in the order of Section 2. If a self-check fails, note it in the reviewer brief's open flags and continue. If the run is cut short, finish the computation work first (numbers, positions, flags), produce whatever formatted outputs you can, and state which deliverables were not produced and why.

## Section 1: Scope

Produces the complete India filing package for:

- Individuals resident in India for the whole tax year, not "not ordinarily resident" (use `in-tax-residency` if unsure). SUGAM (ITR-4) is for "a resident other than not ordinarily resident" under rule 164(5) of the [Income-tax Rules 2026](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
- Self-employed individuals and professionals working as sole proprietors under their own PAN.
- Tax year 2026-27 (1 April 2026 to 31 March 2027), Income-tax Act 2025. Returns for this year are filed in 2027 by the dates in the due-date table above.
- GST returns (GSTR-3B and GSTR-1, if registered) for the months of the same period, the income-tax return (ITR-3 or SUGAM ITR-4), the advance tax reconciliation and the TDS credit reconciliation.

Out of scope: income of 1 April 2025 to 31 March 2026 (1961 Act, assessment year 2026-27); HUFs, firms, LLPs and companies; non-residents; cases where section 172 (transfer pricing report) applies.

## Section 2: Execution order and dependency chain

Run the content Guides in this order:

1. **`india-gst`**: GSTR-3B and GSTR-1 reconciliation. Runs first because GST turnover feeds the income-tax return. Reconcile GSTR-3B summaries with the books; check GSTR-1 outward supplies against invoices; reconcile input tax credit claimed with the auto-populated GSTR-2B. Output: GST turnover, output tax, input tax credit used, cash GST paid, reverse charge.
2. **`in-income-tax`**: the return (ITR-3, or SUGAM ITR-4 for presumptive income). Depends on the GST output: gross receipts must agree with GST turnover (excluding GST for a regular registrant). For presumptive income under section 58(2) Table serial 3 (specified profession), deemed profit is 50% of gross receipts, or a higher profit actually earned; no expense schedule. For actual profit: full profit and loss account, depreciation schedule and balance sheet. Output: total income, tax at the applicable rates, regime comparison if requested.
3. **`in-advance-tax`**: advance tax reconciliation. Depends on the return: final tax decides whether advance tax was enough. Reconcile advance tax paid against the liability, compute section 424 interest (default) and section 425 interest (deferment). Output: advance tax schedule, shortfalls, interest.
4. **`in-tds-freelance`**: TDS credit reconciliation. Depends on the return: TDS credits reduce final tax. Reconcile the tax credit statement and Form No. 168 (the Annual Information Statement from tax year 2026-27) with income declared; flag mismatches. If that Guide cannot produce output, compute the reconciliation from the tax credit statement collected at intake and flag in the reviewer brief that the dedicated Guide was not used. Output: TDS credit summary, mismatches.

- **Upstream failure.** If any content Guide fails to produce a validated output, note the failure in the reviewer brief and continue with the data available rather than halting.

## Section 3: Cross-Guide reconciliation

### Cross-check 1: GST turnover agrees with gross receipts in the return

| GST output | Return input | Rule |
| --- | --- | --- |
| GSTR-3B turnover (excluding GST) | Gross receipts from business or profession | Must agree; explain every difference in the reviewer brief |
| GSTR-1 outward supplies | Business schedule or presumptive turnover | Turnover excludes GST for regular registrants |
| Exports of services | Gross receipts | Included in gross receipts. An export of services is a "zero rated supply" under [section 16(1) of the IGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chaptervii/section16_v1.00.html); supply without payment of integrated tax is "under bond or Letter of Undertaking" (section 16(3)) |

**If they differ:** flag for the reviewer. Common causes: timing (invoice date versus receipt), reverse charge supplies, credit notes, advances received for services not yet supplied.

### Cross-check 2: presumptive income means no further deductions

The rules are in section 58 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

| Rule | Application |
| --- | --- |
| Section 58(2) Table serial 3: deemed profit is 50% of gross receipts or the profit claimed to have been actually earned, whichever is higher (the table text is interleaved on the page: "receipts or profit as referred lakh rupees; or claimed to have been to in section actually earned") | No deduction for actual expenses against that income. Section 58(4): "Any loss, allowance or deduction allowable under the provisions of this Act, shall not be allowed against the income computed" this way |
| Depreciation | Not claimed. Section 58(6): the written down value of an asset is computed as if depreciation had been claimed and allowed for each year |
| Who may use serial 3 | A "specified assessee": an individual or a firm, other than a limited liability partnership, resident in India. The profession must be a specified profession in section 62(4): legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration, information technology or company secretary, or one notified by the Board |
| Who may use serial 1 (business) | An "eligible assessee": resident individual, HUF or firm other than an LLP that does not carry on a specified profession, earns no commission or brokerage and carries on no agency business, and section 58(11)(a)(ii): no Chapter VIII-C deduction claimed for the year |
| Deductions from total income | Chapter VIII deductions where the old regime is chosen; on the new regime, section 202(2)(a)(xii) allows only sections 124(1), 124(2), 125(2) and 146 of Chapter VIII. These come off total income, not business income |

**If violated:** if the computation claims actual expenses AND declares presumptive profit, the check fails. It is one or the other.

**Lower profit than presumptive.** Section 58(3): a person who claims profit lower than the presumptive amount, and whose total income exceeds the maximum amount not chargeable to tax, must keep books under section 62 and get them audited under section 63.

**Leaving the business scheme.** Section 58(7): an eligible assessee who uses serial 1 for a tax year and, in any of the five tax years after it, declares profit otherwise, cannot use the section for the five tax years after the year of departure (figure in the Act table above). Section 58(8) then requires books and audit if total income exceeds the maximum amount not chargeable to tax.

### Cross-check 3: advance tax and TDS against the final liability

| Component | Source | Rule |
| --- | --- | --- |
| Advance tax paid | Tax credit statement and challans | Sum of all advance tax payments for tax year 2026-27 |
| TDS credits | Tax credit statement, Form No. 168, TDS certificates | Sum of TDS deducted and deposited |
| Self-assessment tax | Challans | Paid before filing |
| Total liability | Return computation | Tax on total income plus surcharge plus cess |
| Payable or refund | Liability minus (advance tax plus TDS plus self-assessment tax) | Positive = payable; negative = refund |

- **Section 424 (default).** A person liable to advance tax under section 404 who paid none, or paid less than 90% of "assessed tax", pays simple interest of 1% for every month or part of a month from 1 April following the tax year to the date total income is determined under section 270(1), or to the completion of regular assessment where one is made. Interest is on the assessed tax where nothing was paid, or on the shortfall. "Assessed tax" is tax on the total income as reduced by TDS and tax collected at source, among other credits listed in section 424(2). Rates in the Act table above.
- **Section 425 (deferment), four instalments.** On the shortfall against 15%, 45% and 75% of tax due on returned income at 15 June, 15 September and 15 December, flat interest of 3% each; on the shortfall against the whole amount at 15 March, 1%. Section 425(2): the Act says the assessee "shall not be liable to pay any interest under sub-section (1), if the advance tax paid by the assessee on the current income, [...] (a) on or before the 15th day of June is 12% or more of the tax due on the returned income; (b) on or before the 15th day of September is 36% or more of the tax due on the returned income." The Act prints no "and" or "or" between (a) and (b). This Guide applies (a) to the June shortfall only and (b) to the September shortfall only; where the interest turns on this reading, flag it for the reviewer.
- **Section 425(3), presumptive.** A person who declares profit under section 58(2) Table serial 1 or 3 pays simple interest of 1% on the shortfall if advance tax paid by 15 March is less than the tax due on returned income.
- Section 425(4): no interest under 425(1) or (3) on a shortfall caused by under-estimating capital gains, dividends, or business or profession income "accruing or arising for the first time", or winnings under section 2(49)(n), if the tax on it is paid in the remaining instalments or by 31 March.
- **Section 423 (late return).** Interest of 1% a month on the tax on total income as reduced by tax paid, for each month from the day after the due date (section 423(2) Table).

**Advance tax schedule, section 408**

| Instalment | Due date | Cumulative share required |
| --- | --- | --- |
| First | 15 June | 15% |
| Second | 15 September | 45% |
| Third | 15 December | 75% |
| Fourth | 15 March | The whole amount |

- **Presumptive single instalment.** Section 408(2): a person who declares profit under section 58(2) Table serial 1 or 3 pays the whole advance tax on or before 15 March. The Department confirms this "remains the same as under the old Act" ([tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq), question 19).
- **Threshold.** Advance tax applies only when the tax for the year is INR 10,000 or more (section 404). A resident aged 60 or more at any time in the tax year is not liable to advance tax under section 403(3) only if they have no income under "Profits and gains of business or profession"; a self-employed senior is liable.
- **Timing on 17 October 2026.** The June and September dates for tax year 2026-27 have passed. A presumptive client still has until 15 March 2027. A four-instalment client who missed them should pay now and expect section 425 interest.

### Cross-check 4: tax credit statement against income in the return

| Check | Rule |
| --- | --- |
| Every TDS entry on the tax credit statement and Form No. 168 | The matching income must appear in the return |
| TDS credit claimed in the return | Must equal the statement; explain every difference |
| Section of deduction | Payments from 1 April 2026 are deducted under a table item of section 393; the Department warns that quoting "old section numbers such as 194C, 194J, or 194H" for such transactions "may result in system -level validation errors" ([tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)) |
| Tax collected at source entries | Credit against the liability, if any |

**If they differ:** common causes are a deductor's late TDS statement, a wrong PAN quoted, or income booked in a different year. Flag for the reviewer with the specific entries. A missing entry is corrected by the deductor.

## Section 4: Final reviewer package contents

### Documents

1. **Executive summary**: one page: filing status, income, tax liability, GST position, advance tax, TDS credits, refund or balance due.
2. **GST reconciliation worksheet**: GSTR-3B against books, GSTR-1 against invoices, input tax credit reconciliation.
3. **Return computation worksheet**: ITR-3 or SUGAM (ITR-4), with all heads of income, deductions and the tax computation.
4. **Depreciation schedule**: asset register with block, cost, date, rate, allowance, written down value (actual-profit returns only).
5. **Advance tax reconciliation**: instalments against requirement, section 424 and 425 interest.
6. **TDS credit reconciliation**: tax credit statement against the return, mismatches flagged.
7. **Cross-Guide reconciliation summary**: all four cross-checks with pass or fail and notes.
8. **Reviewer brief**: narrative with positions, citations, flags and self-check results.
9. **Client action list**: what the client must do, with dates and amounts.

### Reviewer brief contents

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
[From in-income-tax output]
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
1. The audit report in Form No. 26 is due one month before the return due date
2. The return due date is 31 October 2027

### Advance tax for tax year 2027-28:
1. 15 June 2027: first instalment, the section 408 share of estimated tax = INR X
2. 15 September 2027: cumulative section 408 share = INR X
3. 15 December 2027: cumulative section 408 share = INR X
4. 15 March 2028: the whole amount = INR X
(If section 58(2) serial 1 or 3: the whole amount by 15 March 2028 in one instalment)

### GST calendar:
- GSTR-3B: twentieth day of the following month (quarterly filers: twenty-second or twenty-fourth day after the quarter, by State)
- GSTR-1: eleventh day of the following month (quarterly filers: thirteenth day after the quarter)
- GSTR-9 for 2026-27: thirty-first day of December after the end of the financial year

### Ongoing:
1. Issue GST tax invoices for all taxable supplies
2. Keep books of account (actual profit) or records of receipts (presumptive)
3. File GSTR-3B and GSTR-1 on time
4. Pay advance tax by each due date
5. Collect TDS certificates from clients
6. Monitor aggregate turnover against the GST registration threshold
7. Keep GST records for seventy-two months from the due date of the annual return; keep income-tax books for the period the Income-tax Rules 2026 prescribe under section 62
~~~

## Section 5: Refusals

- **R-IN-1**: upstream Guide did not run. Name it. This is a warning, not a hard stop. Continue with the data available and flag the gap.
- **R-IN-2**: upstream self-check failed. Name the check and note it in the reviewer brief. Continue.
- **R-IN-3**: cross-Guide reconciliation failed. Name it and describe the difference. Flag for the reviewer and continue.
- **R-IN-4**: intake incomplete. Specific missing items prevent computation. List them and ask the user for each.
- **R-IN-5**: out-of-scope item found during assembly, for example capital gains beyond what SUGAM (ITR-4) allows, rental income, foreign assets or income, or partnership income. Flag it and exclude it from the computation.
- **R-IN-6**: wrong year. The client's income is for 1 April 2025 to 31 March 2026. Stop: that return is under the 1961 Act; use `in-income-tax`.

## Section 6: Self-checks

- **Check IN-A1**: all upstream Guides ran. `india-gst`, `in-income-tax`, `in-advance-tax` produced output; `in-tds-freelance` produced output or the reconciliation was computed from the tax credit statement.
- **Check IN-A2**: GST turnover agrees with gross receipts in the return, or every difference is explained.
- **Check IN-A3**: if section 58(2) serial 3: profit declared is at least 50% of gross receipts, and no expenses are deducted.
- **Check IN-A4**: advance tax and TDS reconciled against the final liability. Credits (advance tax plus TDS plus self-assessment tax) match the payment or refund position.
- **Check IN-A5**: section 424 interest correct. Applies if advance tax paid is under 90% of assessed tax; 1% simple per month or part of a month from 1 April after the tax year.
- **Check IN-A6**: section 425 interest correct. 3% flat on the shortfall at each of the first three dates (subject to section 425(2), read as above), 1% on the shortfall at 15 March. Presumptive cases (section 58(2) serial 1 or 3): only section 425(3), 1% on the shortfall at 15 March.
- **Check IN-A7**: tax credit statement matches the return. Every TDS entry has income in the return; credits claimed equal the statement.
- **Check IN-A8**: regime applied correctly. New regime: section 202(1) rates, and only the deductions section 202(2) keeps. Old regime: rates in the Finance Act 2026 First Schedule Part I-B Paragraph A, and only if the opt-out was exercised by the section 263(1) due date (section 202(4)(a)(i)).
- **Check IN-A9**: rebate applied if eligible. New regime, resident individual: if income does not exceed twelve lakh rupees, rebate of 100% of tax or INR 60,000, whichever is less, with the marginal relief in section 156(2)(b) just above the limit. Old regime: INR 12,500 if total income does not exceed INR 500,000.
- **Check IN-A10**: surcharge and cess correct. Surcharge only above INR 5,000,000 of total income; cess at 4% on tax plus surcharge.
- **Check IN-A11**: filing calendar complete. Every deadline for the return, GST, advance tax and TDS is listed with its date and amount.
- **Check IN-A12**: every position cites its section of the Income-tax Act 2025, the CGST Act 2017, the IGST Act 2017 or the relevant rule.

## Section 7: Output files

The final output is **three files**:

1. **`[client_slug]_2026-27_india_master.xlsx`**: one workbook with every worksheet and computation. Sheets: Cover, GST Reconciliation (GSTR-3B against books), Return Computation (ITR-3 or ITR-4), Depreciation Schedule (actual profit only), Advance Tax Reconciliation, TDS Credit Reconciliation, Section 424 and 425 Interest, Cross-Check Summary. Use live formulas where possible: the gross receipts cell references the GST turnover cell; the advance tax shortfall references the final liability. Check there are no `#REF!` errors and that computed values agree before shipping.
2. **`reviewer_brief.md`**: one markdown file covering all of Section 4: executive summary, GST, return, advance tax, TDS, cross-Guide reconciliation, flags, positions, planning notes.
3. **`client_action_list.md`**: one markdown file with step-by-step actions: filings and payments, the next year's advance tax calendar, the GST calendar, ongoing compliance reminders.

If execution runs out of context mid-build, produce whatever is complete, then state at the end which of the three files were not produced or are partial.

Save the three files and present them to the user.

## Section 8: Cross-Guide references

**Inputs:**

- `in-freelance-intake`: structured intake package
- `india-gst`: GSTR-3B and GSTR-1 reconciliation output
- `in-income-tax`: return computation
- `in-advance-tax`: advance tax reconciliation and interest
- `in-tds-freelance`: TDS credit reconciliation (or the fallback computation from the tax credit statement)
- `in-tax-residency`: only if residence is in doubt

**Outputs:** the final reviewer package. No downstream Guide.

## Section 9: Known gaps

1. Filling the official return is not automated. The reviewer uses the worksheets to complete the return on the e-Filing portal.
2. Filing is done by the reviewer on the portal, not by this Guide.
3. Payment is the client's responsibility; this Guide gives instructions and amounts.
4. The tax audit report (Form No. 26) is not prepared here. If an audit is required, this Guide flags it and the Chartered Accountant prepares the report.
5. If `in-tds-freelance` cannot produce output, the TDS reconciliation is computed from the tax credit statement collected at intake.
6. Multi-year depreciation assumes the prior year schedule is provided. If not, only current-year additions are depreciated.
7. Capital gains computation is out of scope.
8. Foreign assets and foreign income reporting are out of scope.
9. Rental income is out of scope beyond noting it as other income.
10. The package covers tax year 2026-27 only; the next year appears only as planning.
11. State professional tax is taken from intake, not computed (see `in-professional-tax`).
12. The form numbers that replaced Form 16A and Form 10-IEA under the Income-tax Rules 2026 are not stated here; take them from the e-Filing portal.

## The method, step by step

1. **Fix the year and the Act.** Tax year 2026-27, Income-tax Act 2025 ([new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq)). If the income is for the year to 31 March 2026, stop and use `in-income-tax`.
2. **Take the intake package** from `in-freelance-intake`: residence, structure, PAN, age, regime history, presumptive history, GST status, documents.
3. **Run `india-gst`** and fix GST turnover, output tax and input tax credit for the months of the year ([rule 61](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html), [rule 80](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html)).
4. **Choose the basis** under section 58 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf): serial 3 for a specified profession, serial 1 for an eligible business, or actual profit. Test receipts against the limits in the Act table, using the cash share to pick the limit.
5. **Test for tax audit** under section 63 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf): business turnover above one crore rupees (ten crore rupees where cash receipts and cash payments each stay within the section 63 cash share), professional gross receipts above fifty lakh rupees, or presumptive cases claiming lower profit. A cheque or bank draft that is not account payee counts as cash for both cash tests (sections 58(9) and 63(5)(b)). Section 63(2): no audit where profit is declared under section 58(2). If an audit is required, the report (Form No. 26 under rule 47 of the [Income-tax Rules 2026](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf)) is due one month before the return due date (section 63(5)(a)), and the return is due 31 October.
6. **Fix the regime** under section 202 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf). The new regime applies unless the client opts out under section 202(4). With business or profession income, the option must be exercised on or before the section 263(1) due date, carries to later years, and can be withdrawn only once; after withdrawal it cannot be exercised again unless the person stops having business or profession income. An opt-out made under the 1961 Act carries over: "An option exercised under a provision of the old Act ... is treated as if it was made under the equivalent provision of the new Act" ([new Act FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq), questions 23 and 26).
7. **Run `in-income-tax`** for total income and tax: slabs, rebate, surcharge and cess from the tables above ([Finance Act 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf)).
8. **Pick the return form** under rule 164 of the [Income-tax Rules 2026](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf): SUGAM (ITR-4) for a resident (not RNOR) individual with section 58 income and, if it has capital gains, only long-term capital gains under section 198 within the limit in the Rules table (rule 164(5)(b)), and none of the rule 164(6) bars; otherwise ITR-3. The bars include foreign assets, signing authority or income, being a company director, holding unlisted equity shares at any time in the year, total income exceeding fifty lakh rupees, more than two house properties, agricultural income above INR 5,000, and any loss brought forward or to carry forward.
9. **Run `in-advance-tax`** and compute section 424 and 425 interest ([Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf)).
10. **Run `in-tds-freelance`** and match every credit to the tax credit statement and Form No. 168 ([tax payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)).
11. **Run the four cross-checks** in Section 3 and the self-checks in Section 6.
12. **Set the dates**: return due date from section 263(1)(c) as substituted by the [Finance Act 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf); belated return within nine months of the end of the tax year (section 263(4)); revised return within twelve months (section 263(5)).
13. **Assemble the three output files** (Section 7) and state once that a Chartered Accountant must review and sign off before filing.

## Ask the client first

Ask only what the intake package and documents do not already answer.

- Is this for income of 1 April 2026 to 31 March 2027, or for the year before? The year decides the Act, the section numbers and the forms.
- Are your accounts required to be audited under the 2025 Act or any other law? This moves the return due date from 31 August to 31 October and adds the audit report.
- Have you ever opted out of the new regime, and have you already withdrawn that option once? Section 202(4) allows one withdrawal only.
- Did you use the presumptive business scheme (section 58(2) serial 1, or section 44AD before 1 April 2026) in any of the last five years and then declare a lower profit? Section 58(7) may bar the scheme.
- How much of your receipts, and of your payments, was in cash? The cash-share tests decide the presumptive limit and the audit limit.
- Do you supply services to clients outside India, and do you have a Letter of Undertaking for zero-rated supplies?

## When to refuse or refer

Refuse and refer to a Chartered Accountant:

- Income of 1 April 2025 to 31 March 2026 (1961 Act). Use `in-income-tax` or refer.
- Non-resident, not ordinarily resident, or residence in doubt: use `in-tax-residency` first.
- HUF, firm, LLP or company.
- Section 172 (transfer pricing report) applies.
- Tax audit required: this Guide flags it; the Chartered Accountant performs the audit and files Form No. 26.
- Foreign assets, foreign income or treaty relief; capital gains beyond SUGAM (ITR-4) limits; virtual digital assets (see `india-crypto-tax`).
- A pending notice, scrutiny or demand.

Continue but flag for the reviewer:

- Profit declared below the presumptive rate, or a move off section 58(2) serial 1 (section 58(7) and 58(8)).
- Work whose place in the section 62(4) list of specified professions is unclear.
- Any GST point that `india-gst` flagged.
- Proposals that are not law: the 57th GST Council meeting of 8 October 2026 recommended changes, including to late fees and penalties ([press release](https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf)). The release describes them as recommendations, for example "The GST Council recommended an amendment to rule 19 of the CGST Rules, 2017". Do not apply them until the amended law is notified.

## Sources

- Income-tax Act 2025 (Act 30 of 2025), Gazette of India: https://egazette.gov.in/WriteReadData/2025/265620.pdf
- Finance Act 2026 (Act 4 of 2026), Gazette of India: https://egazette.gov.in/WriteReadData/2026/271439.pdf
- Income-tax Rules 2026: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
- Income Tax Department, new Act FAQs: https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq
- Income Tax Department, tax payments FAQs: https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq
- CGST Act section 16: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html
- CGST Act section 22: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html
- CGST Act section 36: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter8/section36_v1.00.html
- IGST Act section 16: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chaptervii/section16_v1.00.html
- CGST Rules rule 61: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html
- CGST Rules rule 80: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html
- Notification 83/2020-Central Tax: https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf
- Notification 13/2017-Central Tax: https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-13-central-tax-english.pdf
- CBIC, GST: An Update (1 June 2019): https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf
- GST Council, 57th meeting press release (recommendations only): https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant, tax practitioner, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
