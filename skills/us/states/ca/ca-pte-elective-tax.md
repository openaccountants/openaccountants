---
name: ca-pte-elective-tax
description: Compute California's 2026 pass-through entity elective tax and each owner's credit. Covers who can elect (partnerships, LLCs taxed as partnerships and S corporations, not disregarded LLCs), who can consent, the 9.3% rate on qualified net income, the June 15 payment of the greater of USD 1,000 or 50% of last year's PTE tax, the SB 132 rule for 2026 to 2030 that a short June 15 payment cuts each owner's credit by 12.5% of their share of the shortfall instead of blocking the election, Form 3804, Form 3893 and Form 3804-CR, credit ordering after the Other State Tax Credit, the 5-year carryover and the federal deduction under IRS Notice 2020-75. Trigger on "California PTE tax", "PTET", "AB 150", "SB 132", "Form 3804", "SALT workaround California".
version: "2.1"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# California pass-through entity (PTE) elective tax

For tax year 2026, an eligible partnership or S corporation doing business in California can elect to pay **9.3% of qualified net income (QNI)**; eligible consenting owners claim a California credit, subject to the payment-shortfall and owner-level limits below. [R&TC §19910(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.); [§17052.11](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.).

## Scope and who this is for

Use this Guide for the 2026 entity computation, election, payments and owner credit, with the separately identified original 2025 cases. It covers LLCs taxed as partnerships or S corporations. A sole proprietor or disregarded LLC cannot elect at its own level. A disregarded LLC can instead be an eligible owner in another electing entity under the owner test below. [FTB qualifications](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html).

This Guide is maintained by the Open Accountants project. It provides information and computations for professional review before filing. Under [Circular 230 §10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37), federal written advice must consider the taxpayer's actual facts; do not assume a return will escape examination. No professional approval is asserted here.

## Ask the client first

Obtain the entity classification, California business/filing status, all direct owners and any disregarded owner chain, resident/part-year/nonresident status, all income/deduction and guaranteed-payment details, annual consents, prior-year PTE tax paid, dated payment confirmations, first/original/superseding return dates, calendar or fiscal year, owner credit carryovers and other credits. Obtain the California-taxable share from the residency/source workpapers; do not infer it from an ownership percentage alone.

## Rates, bands and thresholds

| Item | Amount and operative condition | Official source |
|---|---|---|
| Entity PTE rate | 9.3% of QNI for taxable years beginning in 2026–2030; see eligibility and conditional operation below | [R&TC §19910(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.) |
| First payment | Greater of USD 1,000 or 50% of the elective tax paid for the prior taxable year, by June 15 during the election year | [R&TC §19914(a)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19914.) |
| June shortfall reduction | 12.5% of each qualified taxpayer's pro rata share of the amount due but not paid by June 15, for 2026–2030 | [R&TC §17052.11(b)(2)(B)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.) |
| Owner carryover | Following taxable year and succeeding four years, until exhausted; nonrefundable | [R&TC §17052.11(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.); [FTB credit](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |

## The method, step by step

### 1. Test the entity and each owner

The electing entity must do business in California under §23101 and be required to file under §18633, §18633.5 or §18601(a). It must be taxed as a partnership or S corporation, with owners exclusively corporations under §23038 or taxpayers under §17004 (which includes partnerships). Publicly traded partnerships and entities permitted or required to be in a combined reporting group are excluded. [§19910(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.); [§19912](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19912.); [§17004](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17004.).

An individual, fiduciary, estate or trust subject to California personal income tax may qualify; a corporation or partnership cannot claim this owner credit. The disregarded-entity exclusion has an exception for a disregarded LLC owned by a qualifying taxpayer other than a partnership, where that owner consents and the LLC is a partner, shareholder or member of the electing entity. A disregarded LLC owned by a partnership or corporation does not qualify. A partnership or disregarded entity as an owner does not by itself prevent the lower-tier entity electing for its other qualifying owners. [§17052.11(b)(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.); [FTB owner FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

Collect and retain written annual consent as a workpaper policy. Consent includes all of the owner's pro rata/distributive share and guaranteed payments subject to California personal income tax, not a chosen fraction. Nonconsenting owners are excluded from QNI but bound by the entity election. [§19910(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.); [FTB consent](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html).

### 2. Build QNI owner by owner

Include the consenting qualified owner's share of income and IRC §707(c) guaranteed payments **subject to California personal income tax**, using California determinations rather than unadjusted federal ordinary income. Resident owners use their entire California-taxable share, regardless of source; nonresidents use only the California-taxable sourced share. Part-year residents include worldwide items during residence and California-source items during nonresidence. [§19910(a)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.); [§17041(a), (i)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17041.); [FTB QNI](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

The FTB's general K-1 starting points are S corporation income lines 1–10 less deductions 11–12, or partnership income lines 1, 2, 3, 4c–11 less deductions 12–13. Include relevant items omitted from these lines, including §179 recapture and entity-level gain on §179-expensed property. These are starting points, not a substitute for the California-taxable QNI test. [FTB QNI FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

Exclude an owner's net negative share; do not net it against another owner's positive share. An entity-wide loss alone does not establish zero QNI for every owner. Entity asset-sale gain enters the owners' shares; an owner's sale of their partnership/LLC interest or S corporation stock is owner-level income outside entity QNI. Tax-exempt items stay outside the California-taxable base. [FTB QNI FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html); [§19910(a)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.).

Entity tax = sum of included owner QNI × 0.093. Keep separate owner computations for residency differences. Do not deduct the PTE payment in calculating California QNI: any PTE tax deducted federally is added back in computing California entity net income. [FTB California add-back](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

### 3. Compute payments and the credit reduction

Required first payment = max(USD 1,000, 50% × prior-taxable-year elective tax paid). No prior-year tax means the floor applies; a one-off prior-year gain does not create an exception. For 2026 the ordinary first-payment date is June 15, 2026; balance = total PTE tax less payments, due March 15, 2027 for a calendar-year entity. Extensions to file do not extend this payment date. [§19914(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19914.); [2026 voucher instructions](https://www.ftb.ca.gov/forms/2026/2026-3893-instructions.pdf); [FTB payment FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

**2026–2030:** a missed or short payment at **either** deadline does not itself bar the election under §19914(b). The separate reduction in §17052.11(b)(2)(B) concerns the June 15 shortfall only. Do not treat a later payment as curing that shortfall. Underpaid tax remains payable with applicable penalties and interest. [§19914(b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19914.); [§17052.11(b)(2)(B)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.); [FTB underpayments](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

For the ordinary positive-QNI case illustrated by the FTB: owner credit before owner-use limits = 9.3% × owner QNI − 12.5% × June shortfall × owner QNI / total QNI; June shortfall = max(0, required first payment − timely first payment). Follow the FTB's whole-dollar example below. Do not divide by zero or assume an unused or negative computed credit becomes a cash refund. A zero/negative-QNI allocation or a reduction exceeding the preliminary credit needs specialist resolution: **Check this point with one of our partner accountants.** [FTB credit-reduction example](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

| Boundary | Treatment | Source |
|---|---|---|
| 2021 election | Original timely return; tax payable by original return due date, no June installment | [§19904(a)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19904.) |
| 2022–2025 election | Missed/short required June payment bars election, subject to applicable disaster relief/short-year rule | [§19904(a)(2), (b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19904.); [FTB FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Short taxable year with no June 15 | No June 15 payment requirement for that year | [FTB short-period FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Weekend/legal holiday | Next business day is timely; 2025 June installment was due June 16, 2025 | [FTB payment dates](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| Disaster | Additional time only if applicable relief covers the entity's principal place of business and the relevant payment/return | [FTB disaster FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| PTE overpayment | Applied to other liabilities or refunded after return; cannot be earmarked as next year's PTE/June installment; may elect next-year LLC annual tax/fee or S corporation estimated tax | [FTB overpayments FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

### 4. Elect on the return and keep payment evidence

Make the annual election on the timely filed original Form 100S, 565 or 568 by attaching Form 3804 and entering the elective tax on the designated entity-return line. An amended return cannot first elect or change the consenting owners. The election is irrevocable, subject to the FTB's replacement-original treatment for a qualifying superseding return. [§19910(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.); [FTB election FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

A superseding return may make or revoke the election if both returns are filed by the original due date, or both are filed after that date but by the extended deadline. A first return filed by the original deadline followed by a second after it is an amended return, even if the second is within the extension. A return after the extended deadline cannot elect. [FTB superseding-return scenarios](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

| Calendar-year return | Original 2026 return / PTE balance | Extended filing deadline | Source |
|---|---|---|---|
| Form 100S | March 15, 2027 (third month) | September 15, 2027 (ninth month) | [FTB business dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html); [2026 voucher](https://www.ftb.ca.gov/forms/2026/2026-3893-instructions.pdf) |
| Form 565 / partnership Form 568 | March 15, 2027 (third month) | October 15, 2027 (tenth month) | [FTB business dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html); [2026 voucher](https://www.ftb.ca.gov/forms/2026/2026-3893-instructions.pdf) |

For 2025 calendar-year cases the original deadline was March 16, 2026, with September 15, 2026 for Form 100S or October 15, 2026 for Form 565/partnership Form 568 if extended. Use the entity's actual year for fiscal-year dates; use the next-business-day rule. [FTB dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html).

Pay through FTB Web Pay for Businesses, supported software EFW, or the applicable Form 3893 voucher. An S corporation subject to mandatory electronic payment must pay PTE electronically too. Designate electronic payments as PTE payments, use separate tax-year transactions, and do not combine them with other entity tax. For a voucher select Form 100S/565/568, supply the corporation/SOS/FEIN identifiers and amount, and mail with the check to Franchise Tax Board, PO Box 942857, Sacramento CA 94257-0531. Retain confirmation and reconcile the entity account. [2026 voucher instructions](https://www.ftb.ca.gov/forms/2026/2026-3893-instructions.pdf); [FTB payment method](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

For **2025 only**, Form 3804 Part I combines owner QNI at line 1, rate at line 2 and tax at line 3, carried to Form 100S line 29, Form 565 line 25 or Form 568 line 4. Identify consenting owners in its official Part II schedules, using additional official pages rather than a substitute schedule. For an eligible disregarded SMLLC enter the underlying owner's name and ID on Form 3804 and Form 3804-CR. Explain the credit on the K-1 Other Credits statement. [2025 Form 3804 instructions](https://www.ftb.ca.gov/forms/2025/2025-3804-instructions.pdf); [2025 Form 3804-CR instructions](https://www.ftb.ca.gov/forms/2025/2025-3804-cr-instructions.html).

The read FTB index lists 2026 Form 3893 but 2025 Form 3804/3804-CR. **2026 calculation-form line numbers and reduced-credit boxes are on a non-usable hold**; do not reuse the 2025 box numbers for 2026 or sign off a 2026 completed form from this Guide. Check this point with one of our partner accountants. The computation, deadlines and 2026 payment instructions above remain usable. [FTB form list](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html).

If taxable income changes after a valid election, revise QNI and tax, pay additional tax or claim the overpayment, and have owners amend their returns with revised Form 3804-CR and Schedule P Part III. This can change next year's required June payment. [FTB QNI adjustments](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

### 5. Apply the owner's credit and limits

Claim the applicable credit using Form 3804-CR on the qualified taxpayer's personal return (Form 540, 540NR or 541 as appropriate). It is nonrefundable; carry unused amounts to the following year and four succeeding years, using the earliest possible year, with no carryback or assignment. An owner who consented to a valid election but omitted the credit may amend their own return with Form 3804-CR to claim it. [FTB owner-amendment FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html). Keep the origin year and expiry in the workpapers; the original carryover can survive repeal while its own period remains open. [§17052.11(a), (c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.); [§17039(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.); [FTB credit](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html); [2025 credit instructions](https://www.ftb.ca.gov/forms/2025/2025-3804-cr-instructions.html).

Apply the PTE credit **after** the Other State Tax Credit (OSTC): §17039(a)(6), then (a)(7) for §17052.10, then (a)(8) for §17052.11. In the OSTC net-tax-payable calculation, add back the PTE credit that reduced net tax for that year. [§17039(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.); [§17052.11(f)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.); [§17052.10(f)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.10.).

The PTE credit can reduce regular tax below tentative minimum tax; it does not eliminate alternative minimum tax. It is excluded from the business-credit limitation in §17039.4(c)(5). [§17039(c)(1)(AD), (AH)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.); [§17039.4(c)(5)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.4.); [FTB credit instructions](https://www.ftb.ca.gov/forms/2025/2025-3804-cr-instructions.html).

For an owner receiving credit through a disregarded entity, the annual amount usable is additionally limited under §17039(g) to regular tax including that entity's income less regular tax excluding it; excess follows the credit's carryover rules. Do not automatically label all of Erin's calculated credit currently usable. [§17039(g)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.).

The credit cannot reduce the 1% behavioral health services tax on taxable income over USD 1,000,000; keep that tax in owner estimates. The PTE tax itself is excluded from the entity's estimated-tax calculation under §19136, while the PTE credit reduces qualified taxpayers' estimated payments. [§17043(a), (c)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043.); [FTB estimated-tax FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

A nonresident group return cannot claim the credit; claim it on the qualified taxpayer's own return. The PTE election does not change the separate 7% nonresident withholding requirement or create an automatic waiver. [FTB group-return and withholding FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

A qualified grantor trust may consent and its grantor may generally claim the received credit on their return. A qualified trust may pass all or part of its credit to beneficiaries; the retaining trust and each recipient file their own Form 3804-CR. Do not assert that it must always stay with the trust. Complex estate/trust distributions and grantor attribution: Check this point with one of our partner accountants. [FTB trust FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html); [2025 credit instructions](https://www.ftb.ca.gov/forms/2025/2025-3804-cr-instructions.html).

### 6. Federal deduction and separate California taxes

Under IRS Notice 2020-75 §3.02, state income tax imposed directly on and paid by the partnership or S corporation is deducted in computing its non-separately stated income/loss in the payment year, even where imposed by election or offset by an owner state credit. It reduces federal K-1 income; do not separately deduct the same payment again on the owner's Schedule A. On a calendar-year payment-year computation, June/December 2026 payments fall in 2026; a March 2027 payment falls in 2027. Do not assert a blanket accrual-year exception from the accounting-method label alone. [IRS Notice, §§3.02–4](https://www.irs.gov/pub/irs-drop/n-20-75.pdf).

California adds back the entity's federally deducted PTE payment. PTE tax is in addition to other taxes/fees: it does not replace LLC annual tax/fee or S corporation tax, and the owner PTE credit is for PTE tax, not those other amounts. [§19910(b)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.); [FTB add-back](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

| Separate tax in the original cases | Rule and condition | Source |
|---|---|---|
| LLC annual tax | Generally USD 800 for an ordinary taxable LLC in 2025/2026; statutory exemptions remain; payment by fourth month's 15th day (calendar-year April 15), separate from March PTE balance | [§17941(a), (c), (f), (g)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.); [§23153(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.) |
| LLC fee | Based on California **total income**, not net ordinary income: USD 900 at USD 250,000–<500,000; USD 2,500 at USD 500,000–<1,000,000; USD 6,000 at USD 1,000,000–<5,000,000; USD 11,790 at USD 5,000,000+ | [§17942(a), (b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| LLC fee dates | Estimate by sixth month's 15th day; final fee by return due date | [§17942(c), (d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| Ordinary nonfinancial S corporation | 1.5% net-income tax and generally USD 800 minimum if subject to franchise tax; first-year incorporated/qualified corporations are exempt from the minimum (not income tax); financial corporation rate differs | [§23802(b), (c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23802.); [§23153(d), (f)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.) |

Do not infer the LLC fee, a full federal benefit, or a marginal-rate recommendation solely from PTE QNI. The original federal illustrative saving of USD 23,250 × 37% = USD 8,602.50 per equal owner is arithmetic only: it assumes the whole deduction is incremental, immediately usable and valued at that marginal rate. It is a reduction in tax, not a reduction of AGI by that product. Model the owner's actual SALT itemization, QBI, losses and credits before advising consent. Notice §3.02(4) excludes the specified payment from the owner SALT limit; it does not guarantee that illustrative saving. [IRS Notice](https://www.irs.gov/pub/irs-drop/n-20-75.pdf).

SB 132's new part is conditional on extension of IRC §164(b)(6). Public Law 119-21 §70120(a)(1) removed that provision's January 1, 2026 end date; the operative condition is met. Taxable years beginning in 2026–2030 are covered. If §164(b)(6) is repealed before December 1, 2031, §19916(c) makes the part inoperative for years starting on or after the next January 1. [§19916](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19916.); [Public Law §70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

For fiscal-year endings at the boundary, §17052.10(d) allows the qualified taxpayer's 2026 credit for an electing entity year beginning in 2025; §17052.11(d) similarly allows the taxpayer's 2031 credit for an electing entity year beginning in 2030. Do not treat a calendar-year sunset label as cancelling these express credits. [§17052.10(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.10.); [§17052.11(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.).

Federal SALT phase-down calculations and §461(l) excess-business-loss thresholds are outside this computation; no old fixed cap or loss threshold is usable here. For accrual acceleration, combined QBI/loss planning or a quantified net saving: Check this point with one of our partner accountants. Companion: us-2026-federal-tax-changes and us-tax-workflow-base.

### 7. Late payment, filing and interest

Under §19132(a), unless the failure is due to reasonable cause and not willful neglect, the ordinary late-payment penalty is 5% of total tax unpaid plus 0.5% per month or fraction on remaining tax, for at most 40 months; aggregate maximum 25%. Compute the unpaid base after timely payments and allowable credits, and reduce it for later payments. Apply §19132(b)'s coordination with late-filing/demand penalties; do not stack their full totals. [R&TC §19132(a)–(e)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19132.).

The ordinary late-filing rule in §19131(a) is 5% per month or fraction, capped at 25%, with the statutory reasonable-cause condition and paid-tax/credit reductions. This is not a complete penalty quote for fraud, demand, or entity per-owner filing penalties. Interest on unpaid tax runs from the prescribed payment date at the adjusted rate, without filing-extension relief. [§19131(a), (c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19131.); [§19101(a), (b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19101.). A live interest computation or those exceptional penalties: Check this point with one of our partner accountants. No approximate historical interest percentage is usable.

## Worked cases

Amounts below are USD. Cases B–D preserve both their original **2025** versions and the later **2026** versions with the same inputs; neither year is substituted for the other. Unless A2 says otherwise, assume valid timely elections, full required payments and no June reduction. Credit outputs are generated amounts before owner-use limits. Income inputs mean California-determined income before the PTE deduction, with no omitted adjustment. [FTB QNI and credit method](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html); [2025 §19900](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19900.); [2026 §19910](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.).
### Example A: FTB Partnership A, 2025 election

Partnership A has four equal partners, W, X, Y and Z. All four consent for 2025 ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

| Step | Amount | Source |
| --- | --- | --- |
| 2025 QNI | USD 500,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| 2025 PTE elective tax (QNI × the rate) | USD 46,500 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Required June 15, 2026 payment (the greater of the floor and half of the 2025 tax) | USD 23,250 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

### Example A2: FTB Partnership A, 2026 election with a short June 15 payment

Partnership A pays only part of the required amount on June 15, 2026. Only X, Y and Z consent for 2026, each with a share of income and guaranteed payments as below. The partnership elects on its timely filed original return and pays the balance ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

| Step | Amount | Source |
| --- | --- | --- |
| June 15, 2026 payment made | USD 10,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Share of each of X, Y and Z | USD 100,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| 2026 QNI | USD 300,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| 2026 PTE elective tax | USD 27,900 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Credit per partner before reduction | USD 9,300 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Reduction per partner: 12.5% × (USD 23,250 minus USD 10,000) × USD 100,000 / USD 300,000 | USD 552 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Credit allowed to each of X, Y and Z for 2026 | USD 8,748 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

The FTB rounds the reduction to whole dollars (the unrounded figure is a little above it). W did not consent for 2026 and gets no 2026 credit, but is bound by the election.

```oa-check
name: CA PTE 2026, FTB Partnership A, short June 15 payment and reduced credit
inputs:
  tax_2025: 46500
  paid_june_15: 10000
  partner_share: 100000
  qni_2026: 300000
steps:
  - required_june_15: max(1000, tax_2025 * 0.5)
  - pte_tax_2026: qni_2026 * 0.093
  - credit_before: partner_share * 0.093
  - reduction: round(0.125 * (required_june_15 - paid_june_15) * partner_share / qni_2026, 0)
  - credit_allowed: credit_before - reduction
expected:
  required_june_15: 23250
  pte_tax_2026: 27900
  credit_before: 9300
  reduction: 552
  credit_allowed: 8748
```


### Example B: XYZ Consulting Inc., Chris and Dana, 2025 and 2026 versions

Original facts in each separate year: ordinary income USD 400,000; 75% California source; Chris is a California resident owning 60%; Dana is a Nevada resident owning 40%; both consent. Chris's full share is USD 240,000 (his California-source component is USD 180,000). Dana's full share is USD 160,000, of which USD 120,000 is California-source QNI. Combined QNI is USD 360,000; tax is USD 33,480; generated credits are Chris USD 22,320 and Dana USD 11,160. [FTB residency/QNI](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html); [§17041(a), (i)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17041.).

Dana claims on her own Form 540NR. Calculate her actual regular tax using all relevant income and return facts before deciding how much credit is usable; the old USD 7,000–8,000 tax / USD 3,000–4,000 carryforward estimates are **not usable outputs** from these incomplete facts. Consent may still have a net benefit despite a carryover, so do not recommend against it solely because current-year tax is below USD 11,160. A quantified consent recommendation for Dana: Check this point with one of our partner accountants.

```oa-check
name: CA PTE 2026, S corporation with a resident and a nonresident shareholder
inputs:
  ordinary_income: 400000
  ca_source_share: 0.75
  chris_pct: 0.60
  dana_pct: 0.40
steps:
  - chris_qni: ordinary_income * chris_pct
  - dana_qni: ordinary_income * ca_source_share * dana_pct
  - qni: chris_qni + dana_qni
  - pte_tax: qni * 0.093
  - chris_credit: chris_qni * 0.093
  - dana_credit: dana_qni * 0.093
expected:
  chris_qni: 240000
  dana_qni: 120000
  qni: 360000
  pte_tax: 33480
  chris_credit: 22320
  dana_credit: 11160
```

### Example C: DEF Holdings LLC and Upper Tier Capital LLC, 2025 and 2026 versions

Each year's original ordinary-income input is USD 1,000,000, all California source. Upper Tier Capital LLC, taxed as a partnership, owns 30%; seven California-resident individuals own 10% each and all seven consent. Exclude the upper tier's USD 300,000; included QNI is USD 700,000, PTE tax USD 65,100, and generated credit USD 9,300 for each individual. No lower-tier PTE credit passes to the upper-tier partnership. [FTB tiered-owner FAQ](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html); [§17052.11(b)(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.); [2025 §17052.10(b)(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.10.). Restructuring is not automatically solved by converting the upper tier to an S corporation, which also is not a qualified taxpayer: Check this point with one of our partner accountants.

### Example D: GHI Partners and Erin Single LLC, 2025 and 2026 versions

Each year's California-source income is USD 800,000. Erin Single LLC is a disregarded SMLLC wholly owned by California resident Erin, owns 25% of GHI Partners, and consents through its qualifying owner. QNI attributable to it is USD 200,000 and generated PTE tax/credit USD 18,600. The statutory disregarded-LLC exception permits eligibility, but §17039(g) limits Erin's current use to the incremental regular tax from the disregarded entity's income; unused eligible credit follows the carryover rule. The generated credit is not a promise of a USD 18,600 current reduction. [§17052.11(b)(3)(C)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.); [2025 §17052.10(b)(3)(C)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.10.); [§17039(g)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.). The 2025 forms identify Erin by name and ID; 2026 boxes remain under the stated form hold. [2025 Form 3804](https://www.ftb.ca.gov/forms/2025/2025-3804-instructions.pdf).

### Original Example A: ABC Software LLC, Alex and Brooke, 2025

Alex and Brooke are California residents, each owns 50%, both consent, and original 2025 California-source ordinary income is USD 500,000. With that income as QNI, each has USD 250,000 and a generated credit of USD 23,250; total PTE tax is USD 46,500. No prior-year PTE tax was paid, so the first-payment floor is USD 1,000, timely by **June 16, 2025** under the weekend rule. The USD 45,500 balance could be paid December 31, 2025 for payment-year federal treatment, otherwise by **March 16, 2026**. The ordinary LLC annual-tax payment is separate, ordinarily April 15 during the taxable year; the old March 15 LLC annual-tax date is wrong. [§19900](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19900.); [§19904](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19904.); [FTB next-business-day rule](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html); [§17941(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.); [Notice timing](https://www.irs.gov/pub/irs-drop/n-20-75.pdf).

The original USD 800 LLC tax input is retained separately. The fee cannot be determined from USD 500,000 **net ordinary income** alone; §17942 uses defined total income. The historical suggested USD 2,500 fee at USD 250,000–499,999 and USD 6,000 at USD 500,000–999,999 are superseded, non-usable figures; the correct bands are in the separate-tax table. The old USD 23,650 per-owner federal reduction equals half of USD 46,500 + USD 800 only, excludes any fee and assumes those amounts have not already been deducted; it is not a completed federal-return result. For that final fee/base reconciliation: Check this point with one of our partner accountants.

### Original Example E: JKL Studios LLC and Fei, 2025

Fei moves from California to Washington on July 1, 2025 after six months' residence. Original annual share USD 300,000: USD 180,000 belongs to the residence period and USD 120,000 to the nonresident period, with 100% California-source income. **Given those period allocations as established inputs**, QNI is USD 300,000 and generated PTE tax/credit USD 27,900; the part-year owner uses Form 540NR. The alternative original facts expressly change to ratable income and 70% California source: USD 150,000 resident share plus USD 150,000 × 70% = USD 105,000 nonresident share gives QNI USD 255,000 and generated credit USD 23,715. [§17041(i)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17041.); [§19900(a)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19900.).

These arithmetic results do not prove a ratable or closing-of-books allocation for an actual partnership year. If Fei's USD 180,000/120,000 or USD 150,000/150,000 period allocation is disputed, those outputs are non-usable until the allocation is established: Check this point with one of our partner accountants.

```oa-check
name: Original 2025 cases and historical inputs
inputs:
  abc_income: 500000
  abc_paid: 1000
  xyz_income: 400000
  ca_fraction: 0.75
  def_income: 1000000
  upper_pct: 0.30
  ghi_income: 800000
  erin_pct: 0.25
  fei_resident: 180000
  fei_nonresident: 120000
  fei_alt_half: 150000
steps:
  - abc_tax: abc_income * 0.093
  - abc_owner_credit: abc_tax / 2
  - abc_balance: abc_tax - abc_paid
  - xyz_qni: xyz_income * 0.60 + xyz_income * ca_fraction * 0.40
  - xyz_tax: xyz_qni * 0.093
  - def_excluded: def_income * upper_pct
  - def_qni: def_income - def_excluded
  - def_tax: def_qni * 0.093
  - def_owner_credit: def_tax / 7
  - erin_qni: ghi_income * erin_pct
  - erin_generated_credit: erin_qni * 0.093
  - fei_qni: fei_resident + fei_nonresident
  - fei_generated_credit: fei_qni * 0.093
  - fei_alt_qni: fei_alt_half + fei_alt_half * 0.70
  - fei_alt_credit: fei_alt_qni * 0.093
expected:
  abc_tax: 46500
  abc_owner_credit: 23250
  abc_balance: 45500
  xyz_qni: 360000
  xyz_tax: 33480
  def_excluded: 300000
  def_qni: 700000
  def_tax: 65100
  def_owner_credit: 9300
  erin_qni: 200000
  erin_generated_credit: 18600
  fei_qni: 300000
  fei_generated_credit: 27900
  fei_alt_qni: 255000
  fei_alt_credit: 23715
```

### Original stacking and marginal-rate illustrations

The historical S corporation has USD 500,000 California net income: the ordinary nonfinancial 1.5% tax is USD 7,500. If the separately established PTE QNI is also USD 500,000, PTE tax is USD 46,500 and the two taxes total USD 54,000 before any other obligations. Only USD 46,500 generates the PTE credit. The USD 800 minimum is a floor where applicable, not an additional USD 800 above the USD 7,500. [§23802(b), (c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23802.); [§19900(b)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19900.); [§17052.10(b)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.10.).

The old illustrative equal-ownership comparison (California-resident 50% partner, Nevada-resident 50% partner, 60% California source) is preserved as a formula: for California-determined entity income I, QNI is 0.50I + 0.50 × 0.60I = 0.80I. Do not invent an income amount. The earlier short-payment story of USD 800 paid against an imagined USD 500 floor never established the required USD 1,000 minimum: for a 2025 first election it fails absent applicable relief; for a 2026 first election the June shortfall is USD 200 and ordinary aggregate reduction USD 25, allocated to qualified owners. [§19904](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19904.); [§19914](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19914.); [§17052.11(b)(2)(B)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.).

## When to refuse or refer

Do not elect for an excluded entity or excluded owner, first elect on an amended/late return, waive withholding just because PTE was paid, treat a nonrefundable credit as a refund, or use a held calculation as a filing output. Retain the bounded partner-accountant holds above for reduction edge cases, missing 2026 form boxes, complex fiduciaries, restructuring, disputed Fei allocations, incomplete LLC fee bases and quantified federal/owner savings.

## Completion checklist

Reconcile entity/owner eligibility and annual consents; each California QNI share and excluded negative share; prior-year paid tax and dated installments; June shortfall and generated versus usable owner credit; timely original/superseding election; Form 3804 entity total versus return; owner Form 3804-CR and K-1 statements; federal deduction versus California add-back; OSTC order, TMT/AMT, disregarded-owner limit, carryover expiry, estimates and withholding; other entity taxes; and all non-usable holds. These checks replace the repeated historical reviewer checks 301–328, without an assertion of an independent pass.

Output: eligibility memo; consent register; QNI/tax and reduced-credit computation; payment/account reconciliation; applicable election and owner-credit form workpapers; federal timing/add-back memo; owner-use/carryover schedule; reviewer brief with unresolved **case-specific** held outputs. Final form filing/sign-off awaits professional review and the stated 2026 form hold.

Inputs/handoffs: us-tax-workflow-base; entity bookkeeping; ca-residency-leaving-california; ca-540-individual-return; ca-estimated-tax-540es; ca-smllc-form-568 (SMLLC matters only); ca-llc-fee-and-tax; us-form-1065-partnership; us-federal-return-assembly; us-ca-return-assembly; us-s-corp-election-decision; us-2026-federal-tax-changes; us-pte-state-matrix.

## Sources

Read on 2026-11-27. California LegInfo direct readers returned 403; the cited substantive statute text was then read successfully in the official site through the browser. No failed retrieval is treated as proof.

| Official source | Sections read and applicability | Date read |
|---|---|---|
| [19910](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19910.), [19912](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19912.), [19914](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19914.), [19916](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19916.) | Read for 2026–2030 entity eligibility, QNI/rate, consent/election, both payment deadlines and SALT operative/repeal conditions| 2026-11-27 |
| [19900](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19900.), [19904](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19904.) | Read for Original 2021–2025 regime, QNI and installment condition| 2026-11-27 |
| [17052.10](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.10.), [17052.11](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17052.11.) | Read for 2025/2026 owner definitions, generated credit, reduction, carryover, fiscal-year boundary, OSTC and mathematical disallowance| 2026-11-27 |
| [17004](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17004.), [17041](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17041.), [17043](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043.) | Read for Taxpayer definition; resident and part-year base in §17041(a),(i), not its unindexed printed bands; behavioral health tax and credit exclusion| 2026-11-27 |
| [17039](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.), [17039.4](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17039.4.) | Read for Credit order, below-TMT exceptions, disregarded-entity use restriction, carryover survival and PTE exclusion from business-credit limit| 2026-11-27 |
| [17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.), [17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.), [23802](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23802.), [23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.) | Read for LLC taxes/fee definition, bands and dates; S corporation rate, financial exception, minimum and first-year exemption, limited to relevant 2025/2026 conditions| 2026-11-27 |
| [19131](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19131.), [19132](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19132.), [19101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19101.) | Read for Ordinary filing/payment penalties, base/coordination, reasonable cause and interest timing; no current interest percentage asserted| 2026-11-27 |
| [18633](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.), [18633.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.) | Read for Partnership/partnership-LLC third-month filing dates and filing-status dependency| 2026-11-27 |
| [Official text](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) | Read for FTB PTE index: qualifications, computation, dates, add-back, credit, form list| 2026-11-27 |
| [Official text](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) | Read for FTB help: all PTE FAQ substantive sections, including QNI, superseding returns, shortfall example, owner limits, payment/short-year/disaster| 2026-11-27 |
| [Official text](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html) | Read for FTB business dates: partnership, partnership LLC and S corporation return/extension dates| 2026-11-27 |
| [Official text](https://www.ftb.ca.gov/forms/2026/2026-3893-instructions.pdf) | Read for 2026 Form 3893: complete payment instructions, electronic requirement and calendar-year balance date| 2026-11-27 |
| [Official text](https://www.ftb.ca.gov/forms/2025/2025-3804-instructions.pdf) | Read for 2025 Form 3804: complete computation, official owner schedules, underlying-owner identification and entity return lines; not evidence of 2026 boxes| 2026-11-27 |
| [Official text](https://www.ftb.ca.gov/forms/2025/2025-3804-cr-instructions.html) | Read for 2025 Form 3804-CR: definitions, trust pass-through, limitations, carryover and owner identification; not evidence of 2026 boxes| 2026-11-27 |
| [Official text](https://www.irs.gov/pub/irs-drop/n-20-75.pdf) | Read for IRS Notice 2020-75 §§2–4: specified payments, non-separate deduction, payment year, SALT exclusion and reliance| 2026-11-27 |
| [Official text](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | Read for Public Law 119-21 §70120: continued operation of §164(b)(6); no owner-specific savings computation| 2026-11-27 |

| [31 CFR §10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37) | Read for Federal written-advice facts and audit-risk requirements, (a)(2)| 2026-11-27 |

Not yet confirmed: 2026 Form 3804/3804-CR final boxes; a live interest-rate computation; edge-case zero/negative credit allocation, complex fiduciary attribution, actual disputed part-year allocation, missing fee-base facts, and quantified federal net savings. Each is explicitly held above; none is a usable conclusion.
