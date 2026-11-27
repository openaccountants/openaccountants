---
name: us-federal-income-tax-return-1040
description: Prepare the tax year 2026 US federal individual return working papers, ordinary rate schedules and standard-versus-itemized decision. Covers filing and payment workflow with explicit holds for draft 2026 form fields and specialist computations.
version: "2.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US federal income tax return, Form 1040

Use the 2026 figures below for 2026 working papers, ordinarily filed in 2027. **Filing hold:** the IRS current final Form 1040 is still headed 2025; its 2026 Form 1040 and instructions are drafts marked “DRAFT—NOT FOR FILING.” No 2026 box or line mapping is certified here. Check this point with one of our partner accountants. ([Current form](https://www.irs.gov/pub/irs-pdf/f1040.pdf); [2026 draft form](https://www.irs.gov/pub/irs-dft/f1040--dft.pdf); [draft instructions](https://www.irs.gov/pub/irs-dft/i1040gi--dft.pdf), covers only.)

## Scope and who this is for

Federal individual Form 1040 working papers for US citizens and resident taxpayers. Form 1040-SR is an optional alternative for taxpayers age 65 or older and uses the same schedules and instructions ([IRS](https://www.irs.gov/forms-pubs/about-form-1040)). Nonresident/dual-status, entity and state returns, decedents, gift tax and expatriation filings are specialist referrals below.

## Ask the client first

Record the return year and accounting period; citizenship/residence; filing status and marital/household changes; ages, blindness and dependency; all earned/unearned income, business records, foreign income/accounts, withholding and payments. Obtain W-2/1099/corrected forms, last return/AGI, any current IP PIN and bank details. For deductions obtain payment evidence, mortgage debt/use records, eligible SALT, charity recipient/receipt details and carryovers; identify tips, overtime, vehicle financing/VIN and senior claims. Screen relief for taxpayers abroad, military/combat-zone service and disasters, unfiled returns, notices and inability to pay. These are preparation inputs, not findings of eligibility.

## The method, step by step

### Rates, bands and thresholds

#### Tax year 2026 rate schedules

Apply the marginal schedule to **taxable income**, using the established filing status. “Up to” includes the endpoint; “over” excludes it. These ordinary schedules do not calculate preferential gains/dividends, AMT, special taxes or credits. Those computations remain referred below; do not use a single marginal rate on all income. [Rev. Proc. 2025-32 §4.01, Tables 1–4](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).

| What | Value | Note |
|---|---|---|
| Married filing jointly and surviving spouses, up to USD 24,800 | 10% of taxable income | Table 1: "Not over $24,800 10% of the taxable income" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing jointly, over USD 24,800 up to USD 100,800 | USD 2,480 plus 12% of the excess over USD 24,800 | Table 1: "Over $24,800 but not over $2,480 plus 12% of the excess $100,800 over $24,800" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing jointly, over USD 100,800 up to USD 211,400 | USD 11,600 plus 22% of the excess over USD 100,800 | Table 1: "Over $100,800 but not over $11,600 plus 22% of the excess $211,400" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing jointly, over USD 211,400 up to USD 403,550 | USD 35,932 plus 24% of the excess over USD 211,400 | Table 1: "Over $211,400 but not over $35,932 plus 24% of the excess $403,550" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing jointly, over USD 403,550 up to USD 512,450 | USD 82,048 plus 32% of the excess over USD 403,550 | Table 1: "Over $403,550 but not over $82,048 plus 32% of the excess $512,450" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing jointly, over USD 512,450 up to USD 768,700 | USD 116,896 plus 35% of the excess over USD 512,450 | Table 1: "Over $512,450 but not over $116,896 plus 35% of the $768,700" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing jointly, over USD 768,700 | USD 206,583.50 plus 37% of the excess over USD 768,700 | Table 1: "Over $768,700 $206,583.50 plus 37% of the excess over $768,700" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Head of household, up to USD 17,700 | 10% of taxable income | Table 2: "Not over $17,700 10% of the taxable income" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Head of household, over USD 17,700 up to USD 67,450 | USD 1,770 plus 12% of the excess over USD 17,700 | Table 2: "Over $17,700 but $1,770 plus 12% of not over $67,450" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Head of household, over USD 67,450 up to USD 105,700 | USD 7,740 plus 22% of the excess over USD 67,450 | Table 2: "Over $67,450 but $7,740 plus 22% of not over $105,700" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Head of household, over USD 105,700 up to USD 201,750 | USD 16,155 plus 24% of the excess over USD 105,700 | Table 2: "Over $105,700 but $16,155 plus 24% of not over $201,750" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Head of household, over USD 201,750 up to USD 256,200 | USD 39,207 plus 32% of the excess over USD 201,750 | Table 2: "Over $201,750 but $39,207 plus 32% of not over $256,200" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Head of household, over USD 256,200 up to USD 640,600 | USD 56,631 plus 35% of the excess over USD 256,200 | Table 2: "Over $256,200 but $56,631 plus 35% of not over $640,600" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Head of household, over USD 640,600 | USD 191,171 plus 37% of the excess over USD 640,600 | Table 2: "Over $640,600 $191,171 plus 37% of the excess over $640,600" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Single, and married filing separately, up to USD 12,400 | 10% of taxable income | Tables 3 and 4: "Not over $12,400 10% of the taxable income" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Single, and married filing separately, over USD 12,400 up to USD 50,400 | USD 1,240 plus 12% of the excess over USD 12,400 | Tables 3 and 4: "Over $12,400 but $1,240 plus 12% of not over $50,400" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Single, and married filing separately, over USD 50,400 up to USD 105,700 | USD 5,800 plus 22% of the excess over USD 50,400 | Tables 3 and 4: "Over $50,400 but $5,800 plus 22% of not over $105,700" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Single, and married filing separately, over USD 105,700 up to USD 201,775 | USD 17,966 plus 24% of the excess over USD 105,700 | Tables 3 and 4: "Over $105,700 but $17,966 plus 24% of not over $201,775" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Single, and married filing separately, over USD 201,775 up to USD 256,225 | USD 41,024 plus 32% of the excess over USD 201,775 | Tables 3 and 4: "Over $201,775 but $41,024 plus 32% of not over $256,225" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Single only, over USD 256,225 up to USD 640,600 | USD 58,448 plus 35% of the excess over USD 256,225 | Table 3: "Over $256,225 but $58,448 plus 35% of not over $640,600" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Single only, over USD 640,600 | USD 192,979.25 plus 37% of the excess over USD 640,600 | Table 3: "Over $640,600 $192,979.25 plus 37% of the excess over $640,600" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing separately only, over USD 256,225 up to USD 384,350 | USD 58,448 plus 35% of the excess over USD 256,225 | Table 4: "Over $256,225 but $58,448 plus 35% of not over $384,350" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Married filing separately only, over USD 384,350 | USD 103,291.75 plus 37% of the excess over USD 384,350 | Table 4: "Over $384,350 $103,291.75 plus 37% of the excess over $384,350" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |


#### Tax year 2026 deductions, credits and other amounts

The normal basic standard deduction requires eligibility: it is zero for a separate married filer if either spouse itemizes, and for specified short-period returns caused by a change of accounting period. Nonresident cases remain referred. Age/blindness amounts require age 65 before year-end or statutory blindness at year-end (corrected central vision no better than 20/200, or a visual field no wider than 20 degrees). A spouse addition requires the applicable §151(b) conditions; on a separate return the spouse must have no gross income and not be another taxpayer's dependent. These are additional amounts for each eligible condition, not part of the separate senior deduction ([§63(c)(6), (f)](https://uscode.house.gov/us/usc/t26/s63/)).

| What | Value | Note |
|---|---|---|
| Standard deduction, married filing jointly and surviving spouses | USD 32,200 | "Married Individuals Filing Joint Returns and Surviving Spouses $32,200" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Standard deduction, head of household | USD 24,150 | "Heads of Households (§ 1(j)(2)(B)) $24,150" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Standard deduction, single and married filing separately | USD 16,100 | "Unmarried Individuals (other than Surviving Spouses and Heads of $16,100"; married filing separately is also printed at $16,100 ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Additional standard deduction for age 65 or blindness, per condition, married person or surviving spouse | USD 1,650 | "the additional standard deduction amount under § 63(f) for the aged or the blind is $1,650" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Additional standard deduction for age 65 or blindness, unmarried and not a surviving spouse | USD 2,050 | "increased to $2,050 if the individual is also unmarried and not a surviving spouse" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Child tax credit, maximum per qualifying child | USD 2,200 | "the maximum amount of the credit allowed under § 24(a) is $2,200" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Child tax credit, refundable amount per child | USD 1,700 | "the amount used in § 24(d)(1)(A) to determine the amount of the credit under § 24 that may be refundable is $1,700" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Alternative minimum tax exemption, married filing jointly and surviving spouses | USD 140,200 | "Joint Returns or Surviving Spouses $140,200" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Alternative minimum tax exemption, unmarried (not surviving spouse) | USD 90,100 | "Unmarried Individuals (other than Surviving Spouses) $90,100" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Alternative minimum tax exemption, married filing separately | USD 70,100 | "Married Individuals Filing Separate Returns $70,100" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Alternative minimum tax exemption, phase-out starts and ends, joint returns | USD 1,000,000; USD 1,280,400 | "Joint Returns or Surviving Spouses $1,000,000 $1,280,400" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Alternative minimum tax exemption, phase-out starts and ends, unmarried | USD 500,000; USD 680,200 | "Unmarried Individuals (other than $500,000 $680,200" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Alternative minimum tax exemption, phase-out starts and ends, married filing separately | USD 500,000; USD 640,200 | "Married Individuals Filing Separate $500,000 $640,200" ([source](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Standard deduction, tax year 2025 only (the return filed in 2026) | USD 15,750 single and married filing separately; USD 31,500 married filing jointly; USD 23,625 head of household | "the standard deduction for 2025 is $15,750, and for heads of households, the standard deduction is $23,625" ; "for tax year 2025, the OBBB raises the standard deduction amount to $31,500 for married couples filing jointly" ([source](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill)) |
| Dependent basic standard deduction | smaller of the normal basic amount for the status and the greater of USD 1,350 or earned income plus USD 450; then add eligible age/blindness amounts | [Rev. Proc. 2025-32 §4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [§63(c)(5), (f)](https://uscode.house.gov/us/usc/t26/s63/) |

The personal exemption amount is zero for 2026 under [§151(d)(5)(A)](https://uscode.house.gov/us/usc/t26/s151/); the separate senior deduction remains referred below.

The child-credit rows are **maximum parameters only**, not an award or refundable payment. Full dependency/age/residence, SSN/TIN, MAGI, earned-income and tax-liability tests and the final return computation: Check this point with one of our partner accountants. The AMT rows likewise give statutory parameters, with phaseout measured by AMTI, not regular taxable income; child exemptions and MFS special adjustments require the full computation. Check this point with one of our partner accountants. Do not use these tables alone to certify either liability or eligibility.

#### Changes made by Public Law 119-21 that apply to a tax year 2026 return

| What | Value | Note |
|---|---|---|
| State and local tax deduction cap, taxable years beginning in 2026 | USD 40,400 before MAGI reduction; final limit halved for married filing separately | Eligible personal state/local real-property, personal-property and income taxes (or elected general sales taxes, not both income and sales). Personal-property tax must be annual and based on value; exclude nondeductible improvement assessments. Reduce 40,400 by 30% of positive MAGI excess over 505,000 (half that threshold for MFS), floor 10,000; then halve the resulting limit for MFS, giving a 5,000 floor. MAGI = AGI plus exclusions under §§911, 931, 933. Business/income-producing taxes and foreign-tax treatment require separate classification. [§164(a), (b)(5)–(7)](https://uscode.house.gov/us/usc/t26/s164/) |
| Charitable deduction for a taxpayer who does not itemize, taxable years beginning after 31 December 2025 | up to USD 1,000 (USD 2,000 joint) | Cash paid during the year to §170(b)(1)(A) organizations, excluding §509(a)(3) supporting organizations and donor advised funds. Required substantiation and other applicable limits still apply; the itemizer 0.5% floor and specified carryover rules do not apply. This reduces taxable income, not AGI. [§170(p)](https://uscode.house.gov/us/usc/t26/s170/); [§63(b)(4)](https://uscode.house.gov/us/usc/t26/s63/); [P.L.119-21 §70424](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Itemized charitable contributions, taxable years beginning after 31 December 2025 | otherwise allowable gifts only above 0.5% of contribution base | Contribution base = AGI without a net-operating-loss carryback. Other recipient/property/percentage/substantiation limits still apply. The floor applies in the statutory order, not separately to each gift. Carryover and mixed-category cases: Check this point with one of our partner accountants. [§170(b)(1)(G)–(I), (d)(1)(C)](https://uscode.house.gov/us/usc/t26/s170/); [P.L.119-21 §70425](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Limit on itemized deductions in the 37% bracket, taxable years beginning after 31 December 2025 | itemized deductions reduced by 2/37 of the lesser of (1) the itemized deductions, or (2) taxable income, computed before this reduction and increased by those itemized deductions, above the dollar amount at which the 37% bracket begins for the taxpayer | Apply after all other itemized-deduction limitations; use only positive excess above that threshold. The threshold test uses taxable income **increased by** the otherwise allowable itemized deductions, not taxable income alone. [§68](https://uscode.house.gov/us/usc/t26/s68/); [P.L.119-21 §70111](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

### Steps

1. Establish the taxpayer's year, status and filing duty. A TIN is required ([IRS](https://www.irs.gov/individual-tax-filing)). Under [§6017](https://uscode.house.gov/us/usc/t26/s6017/), a non-nonresident individual with net earnings from self-employment of **USD 400 or more** must file a self-employment tax return; exactly 400 is included. This does **not** itself require quarterly estimates: withholding, expected tax and the separate estimate rules matter ([IRS estimated taxes](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes)); use `us-quarterly-estimated-tax` for that job. Other 2026 filing/dependent thresholds and all no-filing conclusions remain held below. A possible withholding refund or refundable credit should still be screened.
2. Reconcile income and adjustments from documents into a working paper. Classify each business/investment/foreign/other receipt before choosing schedules; do not send every side receipt automatically to Schedule C. Use `us-schedule-c-and-se-computation` for the relevant business computation. [IRS schedule selector](https://www.irs.gov/forms-pubs/about-form-1040): Schedule 1 addresses additional income/adjustments; Schedule 1-A the four additional-deduction topics; Schedule 2 additional taxes; Schedule 3 additional credits/payments. These are navigation labels, not 2026 field mappings or entitlement to a deduction/credit.
3. Compute standard and itemized alternatives only after all applicable limits. Add eligible non-itemizer cash charity to that alternative; it is not an increase in the basic standard deduction. Compare actual federal tax benefit, including preferential-rate and other affected computations. State tax can change an election; separate-filing spouse constraints matter. [§63](https://uscode.house.gov/us/usc/t26/s63/), [§170](https://uscode.house.gov/us/usc/t26/s170/). Mortgage interest in the worked case is expressly an already-eligible input; the debt-qualification computation is not supplied here.
4. Compute tax, credits, additional taxes and payments in working papers; hold any affected amount when a specialist computation is outstanding. Reconcile total tax less total payments to refund/balance, with both zero possible. Record tax year, sources, assumptions, unresolved issues, reviewer and evidence of filing/payment. **Do not transmit a draft form or transpose 2025 line numbers into 2026.** Final 2026 field placement and final instruction-dependent computation remain a partner referral.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Dependency or age/blindness | Apply the basic cap before eligible additions; distinguish filing thresholds from deduction eligibility and from senior relief |
| MFS or high-income itemizer | Own rate schedule; spouse-itemization restriction; SALT halving after phase-down; §68 increased-income test |
| Qualified dividends or long-term gains | The ordinary schedule alone is insufficient; capital-gains computation below remains a specialist route |
| Abroad, military/combat zone, disaster, fiscal year or unusual signing | Identify actual facts and relief before treating an ordinary filing/payment date as applicable; exceptions below remain referred |
| 2025 form/table or a 2026 draft | Not a final 2026 filing instruction; preserve the year label and stop affected filing work |

## Worked cases

**Original Case 1: standard or itemized, tax year 2026.** Preserve MFJ, both under 65, AGI USD 200,000, eligible mortgage interest USD 14,000 (alternative USD 20,000), eligible SALT USD 11,000 and cash gifts USD 6,000. This is conditional arithmetic: assume standard-deduction eligibility, no blindness/dependency, no additional adjustments/deductions, no NOL carryback or charity carryovers, and documented cash gifts to an eligible §170(b)(1)(A) recipient other than a supporting organization or donor advised fund. No preferential income, AMT, credits, extra taxes or state-tax effect is included. Real eligibility is not established by these input amounts.

The charity floor is 200,000 × 0.5% = 1,000; eligible itemized charity = 5,000. Itemized total = 14,000 + 11,000 + 5,000 = **30,000**. Standard route = 32,200 + 2,000 = **34,200**, a 4,200 deduction advantage and **924** ordinary-schedule tax saving. At mortgage interest 20,000, itemized = **36,000**, exceeding the standard route by **1,800**; its ordinary tax is 25,504, saving 396 against the standard route. The decision crosses at mortgage interest 18,200. [2026 amounts](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [charity rule](https://uscode.house.gov/us/usc/t26/s170/). These are working-paper comparisons, not final return certification.

```oa-check
name: Standard or itemized, married filing jointly, 2026
inputs:
  agi: 200000
  mortgage: 14000
  salt: 11000
  cash_gifts: 6000
steps:
  - floor: agi * 0.005
  - itemized: mortgage + min(salt, 40400) + cash_gifts - floor
  - standard_route: 32200 + min(cash_gifts, 2000)
  - gap: standard_route - itemized
  - itemized_higher_mortgage: itemized + 6000
  - itemizing_wins_by: itemized_higher_mortgage - standard_route
expected:
  itemized: 30000
  standard_route: 34200
  gap: 4200
  itemized_higher_mortgage: 36000
  itemizing_wins_by: 1800
```

```oa-check
name: Tax on each route, married filing jointly, 2026 Table 1
inputs:
  agi: 200000
  standard_route: 34200
  itemized: 30000
  band_base: 11600
  band_start: 100800
  band_rate: 0.22
steps:
  - taxable_standard: agi - standard_route
  - taxable_itemized: agi - itemized
  - tax_standard: band_base + (taxable_standard - band_start) * band_rate
  - tax_itemized: band_base + (taxable_itemized - band_start) * band_rate
  - standard_saves: tax_itemized - tax_standard
expected:
  taxable_standard: 165800
  taxable_itemized: 170000
  tax_standard: 25900
  tax_itemized: 26824
  standard_saves: 924
```


## When to refuse or refer

Each affected result below is **non-usable until resolved**. For each: **Check this point with one of our partner accountants.**

- Final 2026 Form 1040/1040-SR, Schedule 1/1-A/2/3/A/C fields, final tax-table/worksheet selection, e-file validation and any return dependent on those instructions. Do not substitute the 2025 line map or a draft.
- 2026 general and dependent filing thresholds, earned/unearned/gross-income tests, qualifying-relative income tests and special filing triggers beyond the §6017 rule above. The current IRS filing table is explicitly 2025; its older single age-65 amount is not certified here. No no-filing decision follows from this Guide's basic standard-deduction amounts.
- Senior deduction; qualified tips, occupation/SSTB/business-net-income restrictions; qualified FLSA overtime; new personal vehicle loan interest, lien/assembly/VIN/lease restrictions; each SSN, filing-status, MAGI, phaseout and effective-period test. Schedule 1-A remains the topic route, not a complete claim method.
- Child tax credit/refundable portion, EITC (including investment-income exclusion), Lifetime Learning Credit and other education/general-business/foreign credits. The child maxima above do not prove entitlement.
- Capital gains/qualified dividends and special rate categories: route to `us-capital-gains`; AMT adjustments, exemption phaseout/MFS/child exceptions and complete computation; excess business losses, QBI and passive/at-risk losses. No computed liability is supplied by the parameter tables.
- Foreign earned income exclusion and residence/presence tests, foreign tax credit, foreign accounts, nonresident/dual-status and treaty issues. Foreign income relief does not establish deadline relief.
- Nonresident returns, partnership/corporation/trust/estate returns, decedents' final returns, gift tax Form 709, expatriation Form 8854 and state/local returns.
- Taxpayer-abroad automatic/further extensions, military/combat/contingency/hospitalization relief, IRS notification and disaster-specific postponements; penalties and interest calculations, inability-to-sign/representative exceptions.
- Charity carryovers, multiple contribution categories, noncash gifts, recipient/substantiation disputes, mortgage-debt qualification or disputed tax classifications; do not turn the worked assumptions into findings.
- Amended/prior-year returns, refund-claim limitations, special electronic/paper routes and state amendments: `us-amended-return-form-1040-including-capital`. Use the actual year's law and instructions; no historical threshold or processing-time promise is carried forward.
- An IRS notice, collection issue, disputed refund, missing records or unreconciled total; stop the affected filing rather than guessing.

## Filing and payment

These are ordinary workflow steps; the final 2026 filing hold above still controls.

1. Use [IRS filing options](https://www.irs.gov/filing/individuals/how-to-file) to choose current supported tax software, professional preparation or paper. Free File/Fillable Forms and volunteer programs remain routes; 2027-season income limits, opening date and provider eligibility are **not certified here**. Check this point with one of our partner accountants.
2. Use the **current calendar year's issued IP PIN**, including for prior-year returns if filing during that year ([IRS](https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin)). Obtain actual final forms and instructions from [IRS Form 1040](https://www.irs.gov/forms-pubs/about-form-1040) before completing fields or signing/transmitting.
3. For an ordinary calendar-year 2026 filer, file and pay by **15 April 2027** ([IRS](https://www.irs.gov/individual-tax-filing)). A timely ordinary extension gives **15 October 2027 to file**, not extra time to pay. Request by the April deadline: pay online designating an extension (retain confirmation), request through Free File, or submit Form 4868 by the supported mail/e-file/professional route ([IRS extension methods](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)). Exceptional relief is referred above. Fiscal-year baseline is the fifteenth day of the fourth month after year-end, shifted for weekends/legal holidays ([Topic 301](https://www.irs.gov/taxtopics/tc301)); special cases remain held.
4. Paper: attach all W-2s, income documents such as W-2G/1099-R when federal tax was withheld, other required front attachments such as Form 2439, and schedules in sequence order behind the return. Attach original W-2 and corrected W-2c copies when received. Both spouses ordinarily sign a joint paper return; signature exceptions are referred. Use the applicable form-instruction address; properly address/pay postage, postmark and deposit by the deadline. E-file timing is transmission in the taxpayer's time zone; retain the subsequent IRS acceptance acknowledgement. [Topic 301](https://www.irs.gov/taxtopics/tc301).
5. Pay through [IRS payments](https://www.irs.gov/payments), choosing the correct year/type; retain confirmation. Bank-account Direct Pay is available without signing in; Individual Account shows payment history and payment-plan options. Card/digital-wallet, wire, check/money-order/1040-V and cash are alternative routes whose current requirements/fees must be established before use. Check this point with one of our partner accountants. If unable to pay, use the IRS debt/payment-plan route; no plan acceptance or penalty waiver is promised.
6. Retain exact refund amount and AGI for later checks ([IRS filing page](https://www.irs.gov/filing/individuals/how-to-file)). Use [Where's My Refund](https://www.irs.gov/refunds) and [Individual Account](https://www.irs.gov/payments/online-account-for-individuals) for status, records, balances, notices and payments. Old estimated refund/processing times are not a guarantee. Rejected filings or missing acceptance require resolution, not an assumption that submission succeeded.

## Completion checklist

Return year/status and original inputs documented; each operative computation sourced and reconciled; specialist and draft-form holds visible; actual final forms and supported filing route established; reviewer and acceptance/payment evidence recorded. Do not mark a held return complete.

Circular 230 §10.37: this general working-paper reference depends on stated facts and assumptions; resolve missing facts and affected legal issues before relying on it for a taxpayer's return.

## Sources

| Source and sections actually read | URL | Read on |
|---|---|---|
| Rev. Proc. 2025-32 §4.01 Tables 1–4, §4.05 child maxima, §4.10 AMT parameters, §4.14 standard deductions; exact completed 26 November reads reused where unchanged | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-26; applicable sections checked 2026-11-27 |
| §63(b), (c)(5)–(7), (f): taxable-income placement, standard eligibility, dependent cap/additions | https://uscode.house.gov/us/usc/t26/s63/ | 2026-11-27 |
| §164(a), (b)(5)–(7): eligible SALT, 2026 cap, MAGI reduction and MFS order | https://uscode.house.gov/us/usc/t26/s164/ | 2026-11-27 |
| §170(a), (b)(1)(G)–(I), (d)(1)(C), (p): cash limits, contribution base, floor and non-itemizer conditions | https://uscode.house.gov/us/usc/t26/s170/ | 2026-11-27 |
| §68(a)–(b): increased-income test and limitation order | https://uscode.house.gov/us/usc/t26/s68/ | 2026-11-27 |
| P.L.119-21 §§70111, 70120, 70424–70425: effective dates; completed exact unchanged reads reused, charity/non-itemizer amendments checked | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-26; charity amendments 2026-11-27 |
| §151(d)(5)(A): zero personal exemption amount; (b) spouse condition | https://uscode.house.gov/us/usc/t26/s151/ | 2026-11-27 |
| §6017: exact 400 boundary, spouses' separate SE bases | https://uscode.house.gov/us/usc/t26/s6017/ | 2026-11-27 |
| About Form 1040: SR age/schedules and schedule navigation | https://www.irs.gov/forms-pubs/about-form-1040 | 2026-11-27 |
| Current Form 1040 cover: final version is 2025; not a 2026 mapping | https://www.irs.gov/pub/irs-pdf/f1040.pdf | 2026-11-27 |
| 2026 draft Form 1040 cover: do not file drafts | https://www.irs.gov/pub/irs-dft/f1040--dft.pdf | 2026-11-27 |
| 2026 draft instructions cover: final approval/change warning only, not operative filing instructions | https://www.irs.gov/pub/irs-dft/i1040gi--dft.pdf | 2026-11-27 |
| Filing-requirement page: 2025 labels and conflicting over-400 wording; not used as 2026 threshold authority | https://www.irs.gov/individuals/check-if-you-need-to-file-a-tax-return | 2026-11-27 |
| Estimated taxes: withholding/estimated-tax distinction and separate payment conditions, not automatic at SE 400 | https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes | 2026-11-27 |
| Individual filing: TIN and ordinary April 2027 filing/payment date | https://www.irs.gov/individual-tax-filing | 2026-11-27 |
| Filing options: ordinary deadline, methods and record AGI/refund; season eligibility not certified | https://www.irs.gov/filing/individuals/how-to-file | 2026-11-27 |
| Extension: ordinary filing-only date and three request routes | https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-27 |
| Topic 301: dates, timeliness, acceptance, paper assembly and ordinary signature/address rules | https://www.irs.gov/taxtopics/tc301 | 2026-11-27 |
| IP PIN: current-year use, including prior-year returns | https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin | 2026-11-27 |
| Payments: guest Direct Pay, Individual Account and payment-plan navigation | https://www.irs.gov/payments | 2026-11-27 |
| Individual Account: records, AGI, refund status, notices, balances and payment-plan navigation | https://www.irs.gov/payments/online-account-for-individuals | 2026-11-27 |
| Refunds: tracking route only, no processing-time promise | https://www.irs.gov/refunds | 2026-11-27 |

Not yet confirmed: final 2026 form fields, final instruction-dependent worksheets and all no-filing decisions; full CTC/AMT eligibility/computations despite retained parameters; EITC/education/foreign credits, FEIE, Schedule 1-A claims, preferential gains and loss/QBI rules; unusual deadlines/signatures, penalties, charity complexity, mortgage qualification, amended/prior-year outcomes, Free File/volunteer season criteria, alternative payment requirements and individual disputes. Each affected result is non-usable under the explicit partner referral above. No accountant approval is created or withdrawn by this working-paper text.
