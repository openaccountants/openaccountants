---
name: in-advance-tax
description: Use this skill whenever asked about Indian advance tax for self-employed individuals, freelancers, or professionals. Trigger on phrases like "advance tax India", "advance tax instalments", "Section 234B", "Section 234C", "Challan 280", "advance tax due dates", "interest on late advance tax", "presumptive tax instalment", "estimated tax India", or any question about advance tax obligations under the Income-tax Act 1961. This skill covers the quarterly instalment schedule, presumptive taxation single instalment, threshold, interest for shortfall under s.234B and s.234C, senior citizen exemption, Challan 280 payment procedure, TDS credit interaction, and edge cases. ALWAYS read this skill before touching any advance tax-related work for India.
version: 2.0
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Advance Tax for Individuals and the Self-Employed

This Guide covers advance tax in India: who must pay it during the year, the instalment dates, how tax deducted or collected at source reduces it, the single instalment for presumptive taxpayers, the senior citizen exemption, the interest for paying late or too little, and how to pay on the e-Filing portal. Figures are for tax year 2026. This means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act, 2025, which replaced the Income-tax Act, 1961 from 1 April 2026. Section numbers below are those of the 2025 Act; the 1961 Act section numbers used in older material changed. Advance tax for the financial year 2025-26 (assessment year 2026-27) was due under the 1961 Act, and this Guide does not cover it.

## Section 1: Quick reference

Read this whole section before computing anything.

| Field | Value |
| --- | --- |
| Country | India |
| Jurisdiction code | IN |
| Tax | Advance tax on income tax (Income-tax Act, 2025, Chapter XIX-C) |
| Primary legislation | Income-tax Act, 2025 (30 of 2025): sections 403 to 410 (liability, computation, payment, instalments, credit); sections 423, 424 and 425 (interest) |
| Supporting legislation | Section 58 (presumptive income); section 266 (self-assessment tax); section 263 as substituted by the Finance Act, 2026 (return due dates); Income-tax Rules, 2026, rule 223 (Form No. 152) |
| Tax authority | Income Tax Department |
| Payment and filing portal | e-Filing portal, e-Pay Tax service |
| Tax year | Tax year 2026-27: 1 April 2026 to 31 March 2027 |
| Instalment dates for tax year 2026-27 | 15 June 2026, 15 September 2026, 15 December 2026, 15 March 2027 |
| Currency | INR only |

**Advance tax rules in the Income-tax Act, 2025**

| Item | Value | Note (verbatim from the Act) |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax is payable when the tax for the year, computed under section 405 (after tax deductible or collectible at source), is this amount or more (section 404) | INR 10,000 | "where the amount of such tax payable during that year, as computed under this Part, is ₹10000 or more" |
| Instalment 1: on or before 15 June, at least this share of the advance tax (section 408(1) Table) | 15% | "1. On or before Not less than 15% of such advance tax. the 15th June." |
| Instalment 2: on or before 15 September, at least this share, less what was paid earlier | 45% | "2. On or Not less than 45% of such advance tax" |
| Instalment 3: on or before 15 December, at least this share, less what was paid earlier | 75% | "3. On or Not less than 75% of such advance tax" |
| Instalment 4: on or before 15 March | the whole amount | "4. On or before The whole amount of such advance tax, as the 15th March." |
| Presumptive taxpayer under section 58(2) Table serial 1 or 3: one payment (section 408(2)) | whole amount by 15 March | "shall pay the whole amount of advance tax on the current income, calculated in the manner laid down in section 405 during each financial year, on or before the 15th March" |
| Payment on or before 31 March counts as advance tax for that financial year (section 408(3)) | 31 March | "Any amount paid by way of advance tax on or before the 31st March, shall be treated as advance tax paid during the financial year ending on that day" |
| Section 424 (default): interest applies where no advance tax is paid, or advance tax paid is less than this share of the assessed tax | 90% | "is less than 90% of the assessed tax" |
| Section 424 (default): simple interest for every month or part of a month, from 1 April after the tax year | 1% | "the assessee shall be liable to pay simple interest at the rate of 1% for every month or part of a month, for the period, beginning from the 1st April following" |
| Section 425 (deferment): interest on the shortfall at 15 June, 15 September and 15 December, each | 3% | "15% of the tax Shortfall till 15th day of 3% of June." |
| Section 425 (deferment): interest on the shortfall at 15 March | 1% | "100% of the Shortfall till 15th day of 1% of March." |
| Section 425(2)(a): the Act says no section 425(1) interest if the amount paid by 15 June is this share or more of the tax due on returned income. This Guide applies it to the June shortfall only (see 4.4). | 12% | "is 12% or more of the tax due on the returned income" |
| Section 425(2)(b): the Act says no section 425(1) interest if the amount paid by 15 September is this share or more of the tax due on returned income. This Guide applies it to the September shortfall only (see 4.4). | 36% | "is 36% or more of the tax due on the returned income" |
| Section 425(3): presumptive taxpayer (serial 1 or 3) short at 15 March | 1% | "simple interest at the rate of 1% on the amount of shortfall from the tax due on returned income" |
| Section 423: interest for a late or missing return, I = 1% x A x T (A = tax on which interest is payable, T = months) | 1% | "I = 1% x A x T" |
| Presumptive business, section 58(2) serial 1: turnover or gross receipts limit | two crore rupees | "(a) Does not" ... "exceed two" ... "crore rupees" (columns interleaved) |
| Presumptive business, serial 1: higher limit where cash receipts do not exceed 5% of the total | three crore rupees | "exceed three receipts which is against serial crore rupees" |
| Presumptive business, serial 1: cash receipts share for the higher limit | 5% | "in cash, does not respect of that tax exceed 5% of year; the total" |
| Presumptive business, serial 1: deemed profit on turnover received by bank or other specified non-cash mode | 6% | "(i) 6% of total business (b) does not turnover or gross" |
| Presumptive business, serial 1: deemed profit on the rest of the turnover | 8% | "(ii) 8% of total turnover or turnover or gross" |
| Presumptive profession, serial 3 (specified profession, section 62(4)): gross receipts limit | fifty lakh rupees | "not exceed fifty receipts or profit as referred lakh rupees;" |
| Presumptive profession, serial 3: higher limit where cash does not exceed 5% of gross receipts | seventy-five lakh rupees | "seventy-five higher. lakh rupees" |
| Presumptive profession, serial 3: deemed profit | 50% | "3. Specified Specified (a) Does 50% of the gross" |

The Gazette prints two-column tables with the columns interleaved, so some quotes above read oddly. That is the page.

**Return due dates (section 263(1)(c) as substituted by the Finance Act, 2026)**

For tax year 2026-27 these dates fall in 2027. They matter here because section 266 self-assessment tax is paid before the return, and section 423 interest runs from the due date.

| Who | Due date | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Company; or an assessee whose accounts must be audited, where section 172 does not apply | 31 October | "2. (i) Company; Where the 31st October." |
| Business or profession income with accounts not required to be audited, and partners of such firms | 31 August | "3. (i) Assessee having income Where the 31st August." |
| Any other assessee (for example salary, rent, capital gains, no business income) | 31 July | "4. Any other assessee. 31st July." |
| Where section 172 (transfer pricing report) applies | 30 November | "Where the 30th November." |

**Paying on the e-Filing portal (e-Pay Tax)**

| Item | Value | Note (verbatim from the Income Tax Department FAQ) |
| --- | --- | --- |
| Source | all figures below | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax |
| A challan (CRN) must be generated on e-Pay Tax for every payment | CRN first | "it is mandatory to generate the Challan for the payment of direct taxes" |
| A CRN stays valid for 15 days after generation; a CRN for advance tax generated on or after 16 March is valid to 31 March | 31 March | "In case, Challan (CRN) is generated on or after 16th March for the payment of 'Advance Tax', then the valid till date is by default set as 31st March of that Financial Year." |
| Cash at a bank counter (Pay at Bank), maximum per CRN | INR 10,000 | "Rs 10,000 per Challan Form (CRN)" |
| Pay at Bank cannot be used by a company or by a person to whom section 63 of the 2025 Act (tax audit) applies (rule 333) | online only | "Note that Pay at Bank mode of tax payment cannot be used by a taxpayer being a company" |
| Proof of payment | Challan Receipt with CIN, BSR code and date | "The Challan Receipt contains Challan Identification Number (CIN), BSR Code and Date of Payment" |

## Section 2: Required inputs and refusal catalogue

### Required inputs

Before computing any advance tax figure, you must know:

1. Residence in India for tax year 2026-27 (resident or non-resident). The senior citizen exemption is for residents only.
2. Age: whether the person is sixty years or more at any time during the tax year (not on a fixed date).
3. Nature of income: business or profession, salary, house property, capital gains, dividends, winnings, other sources. Any business or profession income removes the senior citizen exemption.
4. Whether the person declares presumptive income under section 58(2) Table serial 1 (business) or serial 3 (profession). This changes the instalment schedule. Serial 2 (goods carriages) does not.
5. Estimated total income for the tax year and the regime (the default regime under section 202 or the old regime). The regime changes the tax, not the instalment dates. Rates, slabs and the rebate are in `in-income-tax`.
6. Tax deductible or collectible at source during the year on income included in the estimate (section 405(1), item C).
7. Any order from the Assessing Officer under section 407 to pay advance tax.

If the tax for the year, after the tax deductible or collectible at source, is below the threshold in the Section 1 table, no advance tax is payable (section 404).

### Refusal catalogue

- **R-IN-AT-1: foreign tax relief in the estimate.** Trigger: the client has foreign income and wants to reduce advance tax for tax paid abroad (sections 157, 159 and 160 reliefs). Message: "Foreign tax relief in the advance tax estimate is outside this Guide. Please refer to a Chartered Accountant with international tax experience."
- **R-IN-AT-2: disputes about interest after assessment or reassessment.** Trigger: the client disputes interest under section 424 or 425 charged in an order, or interest recomputed after reassessment under section 279. Message: "Disputes about interest charged in an assessment need representation before the Assessing Officer. Please refer to a Chartered Accountant."
- **R-IN-AT-3: financial year 2025-26 and earlier.** Trigger: the client asks about advance tax or interest for income of the financial year 2025-26 (assessment year 2026-27) or earlier. Message: "Advance tax for 2025-26 and earlier years falls under the Income-tax Act, 1961. This Guide covers tax year 2026-27 under the Income-tax Act, 2025. Please refer to a Chartered Accountant."
- **R-IN-AT-4: companies and other non-individuals.** Trigger: the client is a company, firm, LLP or trust. The instalment table applies to all assessees, but the tax computation (rates, minimum alternate tax credit) is outside this Guide. Refer.
- **R-IN-AT-5: agricultural income taken into account.** Trigger: net agricultural income must be taken into account in the advance tax computation (section 405(2)). Refer.

## Section 3: Payment pattern library

This is a pre-classifier for bank statement lines about advance tax. Match by case-insensitive substring on the counterparty name or description. Narrations depend on the bank; confirm the payment type on the Challan Receipt before relying on a match.

### 3.1 Tax payments

| Pattern | Treatment | Notes |
| --- | --- | --- |
| E-PAY TAX, INCOMETAX.GOV, INCOME TAX, CBDT | TAX PAYMENT | Confirm on the Challan Receipt that the payment type was advance tax, not self-assessment tax, and which tax year it was for |
| CHALLAN 280, ITNS 280, OLTAS | TAX PAYMENT (older challan format) | Older narration. Payments are now made through e-Pay Tax with a CRN; confirm the type and year on the receipt |
| TIN-NSDL, PROTEAN | TAX PAYMENT (older portal) | The Department FAQ calls this the "OLTAS e-Payment of Taxes" on the Protean portal (previously NSDL), replaced by e-Pay Tax |
| SBI TAX, STATE BANK TAX, HDFC TAX, ICICI TAX, AXIS TAX | TAX PAYMENT | Net banking tax payment through an authorised bank; confirm type and year |
| NEFT/RTGS to the tax beneficiary account with a mandate form reference | TAX PAYMENT | e-Pay Tax RTGS/NEFT mode; the payment needs a CRN |

### 3.2 Tax deducted at source in the bank statement

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TDS, TAX DEDUCTED AT SOURCE | TDS CREDIT | Reduces advance tax only if the income is in the estimate (section 405(1)); check the credit on the e-Filing portal |
| TDS U/S 194J, TDS U/S 194C | TDS CREDIT | Bank and client narrations may still use 1961 Act labels. The 2025 Act renumbered the TDS provisions; see `in-tds-freelance` |
| TDS U/S 194N | TDS ON CASH WITHDRAWAL | May not relate to income in the estimate; check before counting it |

### 3.3 Self-assessment tax (separate from advance tax)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SELF ASSESSMENT TAX, SAT PAYMENT | SELF-ASSESSMENT TAX (NOT ADVANCE TAX) | Paid under section 266 before the return. It is not advance tax: only amounts paid as advance tax on or before 31 March count as advance tax for that financial year (section 408(3)). From the date it is paid, section 424 interest runs only on any shortfall that remains (section 424(4)) |

### 3.4 Refunds

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CPC REFUND, INCOME TAX REFUND, NEFT-CPC | TAX REFUND | Refund of excess advance tax or TDS; match it to the return |

## Section 4: Advance tax computation rules

### 4.1 Who must pay advance tax (Tier 1)

Legislation: Income-tax Act, 2025, sections 403, 404 and 405 (https://egazette.gov.in/WriteReadData/2025/265620.pdf).

Advance tax is payable during the financial year on the "current income" of that tax year (section 403). The test is the tax for the year computed under section 405, compared with the threshold in the Section 1 table: at that amount or more, advance tax is payable (section 404). Exactly at the threshold, advance tax IS payable: the Act says "or more".

| Category | Advance tax payable? |
| --- | --- |
| Self-employed or professional, tax for the year after TDS/TCS at or above the threshold | YES, four instalments |
| Salaried person with other income, tax for the year after TDS/TCS at or above the threshold | YES, four instalments |
| Presumptive taxpayer under section 58(2) Table serial 1 or 3, at or above the threshold | YES, one payment by 15 March (section 408(2)) |
| Goods carriage owner under section 58(2) Table serial 2, at or above the threshold | YES, four instalments (section 408(2) names only serial 1 and 3) |
| Resident individual, sixty or more at any time in the tax year, with NO business or profession income | NO (section 403(3)) |
| Resident individual, sixty or more, WITH any business or profession income | YES |
| Non-resident individual of any age | YES if at or above the threshold (section 403(3) covers residents only) |
| Anyone whose tax for the year after TDS/TCS is below the threshold | NO |

How the amount is computed (section 405(1)): A = B - C, where B is income tax on the estimated current income at the rates in force, and C is the tax deductible or collectible at source during the financial year on income that is included in the estimate (and has actually been paid or credited after deduction, or received or debited after collection). So the threshold test is on the NET figure after TDS and TCS, not on gross tax.

The person estimates the current income (section 406(3)) and may increase or reduce the remaining instalments as the estimate changes (section 406(2)).

### 4.2 Assessing Officer's order (Tier 2)

Where a person has already been assessed by regular assessment, the Assessing Officer may order advance tax on a "specified sum" (section 407(1)). The order may be passed no later than the last day of February of the financial year (section 407(2)). If the person estimates a lower figure, they send an intimation in Form No. 152 (section 407(8); Income-tax Rules, 2026, rule 223) and pay on their own estimate. If they estimate a higher figure, they pay the higher amount (section 407(9)). Failing to pay under the order, or failing to send Form No. 152 before an unpaid instalment falls due, makes the person an "assessee in default" (section 409), with penalty exposure under section 412. Flag for the reviewer.

### 4.3 Interest under section 424: default in payment (Tier 1)

Legislation: Income-tax Act, 2025, section 424 (https://egazette.gov.in/WriteReadData/2025/265620.pdf).

- Who: an assessee liable to pay advance tax under section 404 who paid none, or paid less than the share of "assessed tax" in the Section 1 table.
- Base: the whole assessed tax if nothing was paid; otherwise the amount by which advance tax paid falls short of assessed tax. "Assessed tax" is the tax on the total income determined under section 270(1) or on regular assessment, reduced by TDS/TCS on income included, by relief under sections 157, 159(1), 159(2) and 160, and by the tax credits in section 424(2)(f) (section 424(2)).
- Rate and period: the monthly rate in the Section 1 table, simple, for every month or part of a month, from 1 April after the tax year (1 April 2027 for tax year 2026-27) to the date total income is determined under section 270(1) or, where a regular assessment is made, the date it is completed.
- Self-assessment tax: where tax is paid under section 266 before then, interest is computed up to the date of that payment, and after it only on the remaining shortfall (section 424(4)).
- Advance tax counts if paid on or before 31 March (section 408(3)).

### 4.4 Interest under section 425: deferment of instalments (Tier 1)

Legislation: Income-tax Act, 2025, section 425 (https://egazette.gov.in/WriteReadData/2025/265620.pdf).

| Due date | Tax due on returned income that should be paid by then | Interest on the shortfall |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| 15 June | 15% | 3% |
| 15 September | 45% | 3% |
| 15 December | 75% | 3% |
| 15 March | 100% | 1% |

- Base: "tax due on returned income", which is the tax on the total income declared in the return, reduced by TDS/TCS on income included, by the same reliefs and by the tax credits in section 425(5)(f) (section 425(5)). It is NOT the assessed tax used in section 424.
- Shortfall: the amount due at that date (column 2) less the advance tax already paid by that date.
- The interest in the table is a flat charge on each shortfall, not a monthly rate.
- Section 425(2): "The assessee shall not be liable to pay any interest under sub-section (1), if the advance tax paid by the assessee on the current income, [...] (a) on or before the 15th day of June is 12% or more of the tax due on the returned income; (b) on or before the 15th day of September is 36% or more of the tax due on the returned income." The shares are in the Section 1 table. The text does not join (a) and (b) with "and" or "or". This Guide applies (a) to the June shortfall only and (b) to the September shortfall only. A case that turns on this reading is Tier 2.
- Presumptive taxpayers (section 58(2) Table serial 1 or 3): the June, September and December rows do not apply. Section 425(1) applies to an assessee liable under section 404 "other than the assessee mentioned in sub-section (3)". This Guide reads sub-section (3) as covering only section 58(2) serial 1 or 3 taxpayers, because on the wider reading section 425(1) would apply to no one. A case that turns on this is Tier 2. Section 425(3) charges simple interest at the March rate in the table on the shortfall from the tax due on returned income at 15 March.
- Income that is hard to foresee (section 425(4)): no interest under section 425(1) or (3) on a shortfall caused by underestimating, or failing to estimate, (i) capital gains, (ii) winnings from lotteries, crossword puzzles, races, card games, gambling or betting (section 2(49)(n)), (iii) business or profession income arising for the first time, or (iv) dividend income (not a dividend under section 2(40)(e), section 425(6)). BOTH conditions apply: the shortfall comes from that income AND the person paid the full tax on that income in any of the remaining instalments of advance tax, if any, or by 31 March of the tax year.
- Sections 424 and 425 are separate. Both can apply to the same person for the same year.
- Both sections say the assessee "shall be liable to pay" the interest. Neither section contains a power to reduce or waive it. (Section 411(7) allows a reduction or waiver only of interest on unpaid demands under section 411(3).)

### 4.5 Presumptive taxpayers (Tier 1)

Legislation: section 58(2) and section 408(2) of the 2025 Act (https://egazette.gov.in/WriteReadData/2025/265620.pdf).

A person who declares profits under section 58(2) Table serial 1 (eligible business) or serial 3 (specified profession) pays the whole advance tax by 15 March (section 408(2)). The limits and deemed profit rates are in the Section 1 table. The higher turnover limits apply only where cash receipts are not more than the cash share in that table. Who qualifies, and what counts as a specified profession, is in `in-income-tax`. A goods carriage owner under serial 2 is not covered by section 408(2) and pays four instalments.

### 4.6 Regime choice (Tier 1)

The choice between the default regime in section 202 and the old regime changes the tax for the year and so the advance tax amount. It does not change the instalment dates, the threshold or the interest rules. Rates, slabs and the rebate: see `in-income-tax`.

### 4.7 Worked examples (hypothetical amounts)

All amounts in these examples are hypothetical and in INR. The resident individual is under sixty, has no presumptive income, and has no TDS or TCS, so the advance tax, the tax due on returned income and the assessed tax are the same figure. Interest is computed with the rates in the Section 1 table.

| Example | Hypothetical amount (INR) | How it is computed |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| A. Advance tax for tax year 2026-27 (assumed) | 240,000 | Assumed |
| A. Paid by 15 June 2026, at least | 36,000 | 15% of 240,000 |
| A. Paid by 15 September 2026, at least (cumulative) | 108,000 | 45% of 240,000 |
| A. Paid by 15 December 2026, at least (cumulative) | 180,000 | 75% of 240,000 |
| A. Paid by 15 March 2027 | 240,000 | The whole amount |
| B. Nothing paid before 15 March 2027; 240,000 paid on 15 March 2027: section 425 interest for June | 1,080 | 3% of 36,000 |
| B. Section 425 interest for September | 3,240 | 3% of 108,000 |
| B. Section 425 interest for December | 5,400 | 3% of 180,000 |
| B. Section 425 interest in total (no March shortfall; section 424 does not apply because the whole amount was paid by 31 March) | 9,720 | 1,080 + 3,240 + 5,400 |
| C. Instalments A paid on time to 15 December 2026, nothing more by 31 March 2027: section 424 share test | 216,000 | 90% of 240,000; 180,000 paid is less, so section 424 applies |
| C. Section 424 shortfall | 60,000 | 240,000 - 180,000 |
| C. Section 424 interest if the 60,000 is paid as self-assessment tax on 20 July 2027 | 2,400 | 1% x 60,000 x 4 months (April, May, June, July 2027; part of a month counts) |
| C. Section 425 interest for March | 600 | 1% of 60,000 |
| D. As C, but 216,000 paid by 15 March 2027: section 424 | nil | 216,000 is not less than 90% of 240,000 |
| D. Section 425 interest for March | 240 | 1% of 24,000 (240,000 - 216,000) |

If the extra amount in Example D is paid between 16 and 31 March instead, section 424 still does not apply (section 408(3)), but the 15 March shortfall is the same as in Example C, and so is the March interest under section 425.

## Section 5: Payment procedure (e-Pay Tax)

Source: Income Tax Department e-Pay Tax FAQ (https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax). The e-Filing portal home page states that payments under the Income-tax Act, 1961 are for dues up to FY 2025-26 and payments under the Income-tax Act, 2025 are for Tax Year 2026-27 onwards (https://www.incometax.gov.in/iec/foportal/).

### Online payment steps (Tier 1)

1. Open e-Pay Tax on the e-Filing portal, before login (Quick Links) or after login with the PAN.
2. Make sure the challan is for the Income-tax Act, 2025, tax year 2026-27, and advance tax. The portal takes payments under both Acts from a single interface (home page), so check the Act, the year and the payment type before paying. A payment made under the wrong one cannot be reversed on the portal (FAQ question 8).
3. Choose the mode of payment when generating the challan: net banking or debit card of an authorised bank, payment gateway (net banking, debit card, credit card, UPI), RTGS/NEFT, or Pay at Bank counter. The mode cannot be changed after the CRN is generated.
4. Generate the challan (CRN). It is valid for 15 days; a CRN for advance tax generated on or after 16 March is valid to 31 March.
5. Pay. Cash at a bank counter is limited per CRN to the amount in the Section 1 table. A company, and a person to whom section 63 (tax audit) applies, must pay online (rule 333 as stated in the FAQ).
6. Download the Challan Receipt from Payment History. It shows the CIN, BSR code and date of payment. Keep it for the return.

### What the receipt must show

| Field | What to check |
| --- | --- |
| Act and year | Income-tax Act, 2025, tax year 2026-27 |
| Payment type | Advance tax (not self-assessment tax) |
| PAN | The taxpayer's own PAN |
| Proof | CIN, BSR code and date of payment |

A payment made under the wrong head or year cannot be refunded or reversed on the portal. The FAQ tells the taxpayer to claim it as a credit in the return for the relevant year or ask the jurisdictional Assessing Officer for refund or adjustment.

## Section 6: Senior citizen exemption and penalties

### 6.1 Senior citizen exemption (Tier 1)

Legislation: section 403(3) of the 2025 Act (https://egazette.gov.in/WriteReadData/2025/265620.pdf). Section 403(1) does not apply to an individual resident in India who (a) does not have any income chargeable under the head "Profits and gains of business or profession" AND (b) is of the age of sixty years or more at any time during the tax year. Both conditions must hold.

| Condition | Advance tax |
| --- | --- |
| Resident, sixty or more at any time in tax year 2026-27, no business or profession income | Not payable |
| Resident, sixty or more, with any business or profession income | Payable if at or above the threshold |
| Non-resident, any age | Payable if at or above the threshold |
| Resident who turns sixty on any day up to 31 March 2027 | Meets the age condition for tax year 2026-27 |

Interest: sections 424 and 425 charge interest on an assessee "liable to pay advance tax under section 404". Section 403(3) switches off section 403(1) for this group, so no instalments are due. If an exempt person is nonetheless charged interest, treat it as Tier 2.

### 6.2 Interest and penalties (Tier 1)

| Charge | Rate or limit | Legislation |
| --- | --- | --- |
| Default in advance tax | Section 1 table, section 424 rows | Section 424 |
| Deferment of instalments | Section 1 table, section 425 rows | Section 425 |
| Late or missing return | Section 1 table, section 423 row | Section 423 |
| Penalty where in default on a demand, or deemed in default under section 409 | Directed by the Assessing Officer; total not more than the tax in arrears; not levied without a hearing, or where the default was for good and sufficient reasons | Section 412 |

## Section 7: Edge case registry

### EC1: Income mainly from capital gains realised late in the year (Tier 1)

Situation: the client's main income for tax year 2026-27 is a capital gain realised in January 2027. Nothing was paid in June or September 2026.
Resolution: section 425(4) removes section 425 interest on the shortfall caused by the capital gain, provided the full tax on that gain is paid in the remaining instalments (here, by 15 March 2027) or by 31 March 2027. Tax on other income still follows the normal schedule. Section 424 can still apply if total advance tax paid by 31 March is below the share of assessed tax in the Section 1 table.

### EC2: TDS covers most of the liability (Tier 1)

Situation: a consultant's fees suffer TDS. The tax for the year less the TDS deductible on the fees included in the estimate is the net figure.
Resolution: compare the NET figure with the threshold (section 405(1), item C). If it is at or above the threshold, the net amount is paid in four instalments. TDS also reduces the base for interest (sections 424(2) and 425(5)).

### EC3: Presumptive taxpayer who also has capital gains (Tier 2)

Situation: the client declares business income under section 58(2) Table serial 1 and also has a capital gain.
Resolution: section 408(2) puts the WHOLE advance tax on the current income of a serial 1 or 3 presumptive taxpayer on one date, 15 March. The capital gain is part of that current income. Section 425(4) still protects a shortfall caused by the gain if its tax is paid in full by 31 March. Flag for the reviewer.

### EC4: Senior citizen with rent and freelance income (Tier 1)

Situation: client aged sixty-five, resident, with rent and some freelance consulting fees.
Resolution: the freelance fees are profession income, so section 403(3)(a) fails and the exemption does NOT apply. If the tax for the year after TDS is at or above the threshold, the four-instalment schedule applies to all income.

### EC5: Estimate rises during the year (Tier 1)

Situation: the client's income estimate rises after September.
Resolution: section 406(2) lets the client increase the remaining instalments. Section 425 interest is computed at each date on the shortfall against the share of the tax due on returned income, so a later top-up does not remove interest already incurred at an earlier date. Pay the shortfall by the next date.

### EC6: Advance tax paid in full, return filed late (Tier 2)

Situation: the client paid all instalments on time but filed the return after the section 263 due date.
Resolution: section 424 does not apply (advance tax paid). Section 423 interest (formula in the Section 1 table) applies on the tax on which interest is payable, which section 423(2) defines after deducting "tax paid", including advance tax and TDS. A late filing fee under section 428 may also apply. Flag for the reviewer.

### EC7: Non-resident with Indian business income (Tier 2)

Situation: a non-resident individual has business income from India.
Resolution: advance tax applies on the same threshold and dates. The senior citizen exemption does NOT apply (it is for residents only). Treaty relief is outside this Guide (R-IN-AT-1). Flag for the reviewer.

### EC8: Questions about the 1961 Act (Tier 2)

Situation: the client quotes 1961 Act sections or asks about the instalments for 2025-26.
Resolution: for tax year 2026-27 apply the 2025 Act sections in this Guide. For 2025-26 and earlier, refuse under R-IN-AT-3.

### EC9: Client reading this after 15 September 2026 (Tier 1)

Situation: in October 2026 the client realises no advance tax has been paid for tax year 2026-27.
Resolution: the June and September shortfalls have already arisen and attract section 425 interest unless section 425(4) applies. Pay enough by 15 December 2026 to reach the December share in the Section 1 table, and the rest by 15 March 2027, to avoid further section 425 interest and any section 424 interest.

## Section 8: Reviewer escalation protocol

When a Tier 2 situation is identified:

~~~
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: a Chartered Accountant must confirm before advising the client.
~~~

When a Tier 3 situation is identified:

~~~
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside the scope of this Guide]
Action Required: do not advise. Refer to a Chartered Accountant. Document the gap.
~~~

## Section 9: Test suite

### Test 1: Standard self-employed, four instalments

Input: resident, age forty, business income, no presumptive scheme, no TDS, advance tax for the year as in Example A in Section 4.7.
Expected: the four cumulative amounts in Example A, due 15 June 2026, 15 September 2026, 15 December 2026 and 15 March 2027.

### Test 2: Exactly at the threshold

Input: tax for the year after TDS and TCS equals the threshold in the Section 1 table.
Expected: advance tax IS payable. Section 404 says "or more".

### Test 3: Below the threshold

Input: tax for the year after TDS and TCS is below the threshold.
Expected: no advance tax payable; no section 424 or 425 interest.

### Test 4: Presumptive taxpayer (section 58(2) serial 1)

Input: age forty-five, eligible business declaring presumptive income, advance tax above the threshold, no TDS.
Expected: one payment of the whole advance tax by 15 March 2027. No June, September or December amounts. If short at 15 March, section 425(3) interest at the March rate.

### Test 5: Senior citizen exempt

Input: resident, turns sixty in February 2027, income only from house property and bank interest.
Expected: section 403(3) applies (sixty at any time during the tax year, no business or profession income). No advance tax.

### Test 6: Senior citizen not exempt

Input: resident, age sixty-five, freelance fees, tax after TDS above the threshold.
Expected: exemption does not apply. Four instalments.

### Test 7: Section 424 interest

Input: Example C in Section 4.7.
Expected: section 424 interest as in Example C, plus section 425 March interest as in Example C.

### Test 8: Section 425 interest when nothing is paid until 15 March

Input: Example B in Section 4.7.
Expected: section 425 interest for June, September and December as in Example B; no section 424 interest.

## Section 10: Prohibitions

- Never compute advance tax without the estimated total income, the regime and the TDS/TCS on income in the estimate.
- Never skip the threshold test, and never test gross tax: the test is on tax after TDS/TCS (section 405(1)).
- Never treat a person exactly at the threshold as exempt: section 404 says "or more".
- Never apply the senior citizen exemption to a person with any business or profession income, or to a non-resident.
- Never test age on a fixed date: the condition is sixty or more at ANY time during the tax year.
- Never tell a section 58(2) serial 1 or 3 presumptive taxpayer to pay four instalments; never tell a serial 2 goods carriage owner to pay only once.
- Never compute section 425 interest on assessed tax: its base is the tax due on returned income.
- Never treat self-assessment tax under section 266 as advance tax.
- Never tell a client that section 424 or 425 interest will be waived.
- Never quote 1961 Act section numbers as the law for tax year 2026-27.
- Never present an advance tax figure as final: it rests on an estimate, and the return decides the tax.

## The method, step by step

1. Fix the year and the law: tax year 2026-27 (1 April 2026 to 31 March 2027), Income-tax Act, 2025 (https://egazette.gov.in/WriteReadData/2025/265620.pdf). For 2025-26 or earlier, refer (R-IN-AT-3).
2. Check the senior citizen exemption under section 403(3): resident, sixty or more at any time in the tax year, AND no business or profession income. If both hold, stop: no advance tax (https://egazette.gov.in/WriteReadData/2025/265620.pdf).
3. Estimate current income and compute the tax for the year under the chosen regime (rates in `in-income-tax`). Deduct the tax deductible or collectible at source on income in the estimate (section 405(1)) (https://egazette.gov.in/WriteReadData/2025/265620.pdf).
4. Compare the net figure with the section 404 threshold in the Section 1 table. At or above it, advance tax is payable (https://egazette.gov.in/WriteReadData/2025/265620.pdf).
5. Pick the schedule under section 408: four instalments, or one payment by 15 March for a section 58(2) serial 1 or 3 presumptive taxpayer. Set the cumulative amounts from the Section 1 table (https://egazette.gov.in/WriteReadData/2025/265620.pdf).
6. Pay each instalment through e-Pay Tax with a CRN under the 2025 Act, tax year 2026-27, advance tax; keep the Challan Receipt (https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax).
7. Re-estimate before each date and adjust the remaining instalments (section 406(2)). If an Assessing Officer's order arrives, follow section 407 and use Form No. 152 for a lower estimate (https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
8. After the year: compute section 425 interest on the tax due on returned income, then section 424 interest on assessed tax if advance tax paid by 31 March is below the share in the Section 1 table. Pay any balance with interest as self-assessment tax under section 266 before filing (https://egazette.gov.in/WriteReadData/2025/265620.pdf).
9. File by the section 263(1)(c) due date that fits the client, or section 423 interest runs (https://egazette.gov.in/WriteReadData/2026/271439.pdf).

## Ask the client first

- Were you resident in India for tax year 2026-27, and what is your date of birth?
- Do you have any business or profession income, including freelance or consulting fees?
- Do you declare presumptive income under section 58(2), and under which serial (business, goods carriages or profession)?
- What income do you expect for the whole year, and how much tax will be deducted or collected at source on it?
- Do you expect capital gains, dividends, winnings or a new business during the year?
- What have you already paid for tax year 2026-27, on which dates, and under which payment type?

## When to refuse or refer

- Advance tax or interest for 2025-26 or earlier (1961 Act): refer.
- Foreign tax relief in the estimate (sections 157, 159, 160): refer.
- Disputes about interest charged in an assessment or reassessment: refer.
- Companies, firms, LLPs and trusts: refer for the tax computation.
- An Assessing Officer's order under section 407, or a notice treating the person as in default under section 409: refer.
- Net agricultural income in the computation (section 405(2)): refer.
- A payment made under the wrong head or year: the client must claim it in the return or ask the Assessing Officer; refer if the amounts are material.

## Sources

- Income-tax Act, 2025 (30 of 2025), Gazette of India, 22 August 2025: https://egazette.gov.in/WriteReadData/2025/265620.pdf
- Finance Act, 2026 (4 of 2026), Gazette of India, 30 March 2026 (section 263 due dates as substituted): https://egazette.gov.in/WriteReadData/2026/271439.pdf
- Income-tax Rules, 2026, notified 20 March 2026 (rule 223, Form No. 152): https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
- Income Tax Department, e-Pay Tax FAQ: https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax
- Income Tax Department, e-Filing portal home page (payments under each Act): https://www.incometax.gov.in/iec/foportal/

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
