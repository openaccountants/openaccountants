---
name: au-deductions-offsets
description: >
  Use this skill to work out what an Australian taxpayer can claim: deductions, tax offsets,
  rebates, credits, capital allowances and small business concessions, and how they interact. It
  maps the general "credits, reliefs, deductions and allowances" category onto Australian
  concepts, which behave differently from each other. Trigger on phrases like "what can I claim",
  "tax deductions Australia", "work-related expenses", "$1,000 standard deduction", "instant tax
  deduction", "tax offset", "rebate", "low income tax offset", "LITO", "refundable offset",
  "franking credits refund", "substantiation", "do I need a receipt", "capital or revenue",
  "apportion private use", "small business concessions". It routes to the specialist guides
  rather than restating their rules.
version: 0.5
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - au-individual-return
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Australia Deductions, Offsets and Concessions v0.4

## Australia Deductions, Offsets and Concessions v0.5

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## What this file is

**Obligation category:** Income tax
**Functional role:** Router and decision framework for everything that reduces Australian tax
**Status:** Source-cited draft, pending accountant review

Australia has no single "reliefs and allowances" concept. Four mechanisms sit behind that idea and
they behave differently, so getting the mechanism right matters more than finding the item.

## Section 1 - The vocabulary map

**The vocabulary map**

| Mechanism | What it reduces | Typical value of $1 | Australian examples |
| --- | --- | --- | --- |
| **Deduction** | Assessable income, producing taxable income | The taxpayer's marginal rate, so worth more to higher earners | Work-related expenses, rental expenses, business expenses, personal super contributions, donations to deductible gift recipients |
| **Capital allowance** | Assessable income, spread over time or immediately | Marginal rate, but timing changes the value | Decline in value under Division 40, capital works under Division 43, instant asset write-off |
| **Tax offset (also called a rebate)** | Tax payable, after tax is calculated | $1 of tax, regardless of marginal rate | Low income tax offset, seniors and pensioners tax offset, foreign income tax offset, private health insurance rebate |
| **Concession or exemption** | The base itself, or the rules that apply to it | Varies | Small business CGT concessions, the 50% CGT discount, main residence exemption, small business entity concessions |

**Why the distinction matters.** A $1,000 deduction saves $320 at a 30% marginal rate plus the
full 2% Medicare levy and $470 at a 45% marginal rate plus the same levy. These examples assume
the whole deduction falls within one tax band and does not affect any other calculation. A
$1,000 non-refundable offset saves up to $1,000 against the liabilities it can reduce. A
refundable offset can also pay out any excess.

**Refundable and non-refundable offsets.** Most offsets are non-refundable: they can reduce tax
payable to zero but do not pay out an unused offset. The treatment of any unused amount depends
on the offset: some can transfer, carry forward or reduce other liabilities. Some offsets are
refundable, so the excess is paid out. Franking credits attached to franked dividends and the private health insurance
rebate are refundable. Check this before telling a taxpayer an offset is worth anything to them.
[ATO, About tax offsets](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets)

## Section 2 - Scope statement

This skill covers:

- The order in which deductions, offsets and concessions are applied.
- The general deduction test, apportionment, the capital and revenue boundary, and the specific
  denial provisions.
- The standard deduction for work-related expenses that applies from the 2026-27 income year.
- Substantiation requirements and record retention.
- The main tax offsets and how refundability changes their value.
- Where each specialist rule set lives.

This skill does NOT cover:

- The detailed computation of any single item. Each has its own guide.
- GST credits. Those are not income tax deductions. See `australia-gst.md`.
- Fringe benefits tax. See `au-fbt-year.md`.
- State and territory concessions, including duty concessions and land tax exemptions. See
  `au-stamp-duty.md` and `au-land-tax.md`.

**Where the specialist rules live**

**Where the specialist rules live**

| Topic | Guide |
| --- | --- |
| Individual return items and work-related expense patterns | `au-individual-return.md` |
| Rental property income and expenses | `au-rental-property.md` |
| Small business CGT concessions | `au-small-business-cgt.md` |
| CGT discount, losses and cost base | `au-capital-gains.md` |
| Research and development tax incentive | `au-rd-incentive.md` |
| Personal services income restrictions | `au-psi.md` |
| Medicare levy and the surcharge | `au-medicare-levy.md` |
| Superannuation contribution deductions and caps | `au-super-guarantee.md` |
| Company losses, franking and Division 7A | `au-company-tax.md`, `au-div7a.md` |
| Foreign income tax offset | `au-foreign-income.md` |

## Section 3 - The order of operations

- **Order of operations** -- Apply the statutory offset priorities, including the rules for any unused amount. 1. Work out assessable income, including net capital gains. 2. Subtract allowable deductions to get taxable income. 3. Apply the rates for the income year to taxable income, giving basic income tax liability. 4. Calculate the Medicare levy and any Medicare levy surcharge separately. 5. Apply offsets to basic income tax liability in the order in section 63-10. For each unused amount, follow its statutory treatment: application to another liability, transfer, carry-forward, refund or loss. See Section 8.2 for the Medicare levy exceptions. 6. Add the remaining income tax and levy liabilities, then subtract any refundable excess offsets. 7. Apply PAYG withholding credits and the credit for PAYG instalments payable, including instalments still unpaid and adjusted for any instalment credits already claimed. Unpaid instalments remain separate liabilities. _([ITAA 1997 s 63-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10), [TAA 1953 Schedule 1 s 45-30](https://www.legislation.gov.au/C1953A00001/2026-05-21/2026-05-21/text/original/epub/OEBPS/document_2/document_2.html))_
- **Tax losses** -- A tax loss generally arises when deductions other than prior-year tax losses exceed the sum of assessable income and net exempt income. Division 35 can defer individual business losses before this calculation. Company losses carried forward are subject to the applicable ownership and business continuity rules. From 2026-27 qualifying corporate tax entities can choose to carry a current-year loss back to either of the 2 preceding years and claim a refundable offset, subject to Division 160. _([ITAA 1997 s 36-10](https://www.legislation.gov.au/C2004A05138/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html), [Tax Reform No. 2 Act 2026 Schedule 1](https://www.legislation.gov.au/C2026A00071/asmade/text))_

## Section 4 - Deductions: the decision steps

- **Deductions decision steps overview** -- Identify the provision that allows the deduction before applying these steps. Steps 1 and 2 test general deductions under section 8-1. A specific deduction, such as a qualifying gift under Division 30, follows its own eligibility rules; failure of the section 8-1 test does not decide that claim. For specific deductions, apply steps 3 to 6 using the relevant provision's limits, apportionment, timing and evidence requirements.  _([ITAA 1997 (Cth) s 8-5](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-5))_

### Step 1 - Is there a nexus with assessable income?

- **Nexus test** -- A loss or outgoing is deductible to the extent it is incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business for that purpose.  _([ITAA 1997 s 8-1](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-1))_
- **ATO three conditions for employees** -- The ATO states the test for an employee as three conditions: the taxpayer spent the money and was not reimbursed, the expense directly relates to earning income, and there is a record to prove it. An employer instruction to buy something does not by itself make it deductible.  _([ATO, Claiming deductions](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/how-to-claim-deductions))_

### Step 2 - Is it private, domestic or capital in nature?

- **Private, domestic or capital exclusion** -- Section 8-1 denies a deduction to the extent the outgoing is private or domestic, or capital or of a capital nature. Ordinary travel between home and work and daily lunches are private. If section 8-1 excludes capital expenditure, check whether it qualifies under another regime: Division 40 decline in value, Division 43 capital works, the CGT cost base, or a specific write-off provision such as section 40-880 for certain business-related capital expenditure.

### Step 3 - Does a specific provision deny or limit it?

- **Specific denial or limit provisions** -- Deductibility can be denied even where the nexus exists. Examples include entertainment expenses, penalties and fines, holding costs for vacant land held by most non-business taxpayers, and general interest charge and shortfall interest charge incurred on or after 1 July 2025. Check the specific provision before allowing an unusual item.

### Step 4 - Apportion

- **Apportionment** -- Where an expense serves both an income-producing and a private purpose, only the income-producing share is deductible. The apportionment method must be reasonable and documented. A percentage guessed at year end is not a method.

### Step 5 - Is it incurred in this income year?

- **Timing / incurred** -- The timing of the liability can differ from the payment date. An individual incurring non-business expenditure or an eligible business with aggregated turnover of less than $50 million can use the 12-month rule if the eligible service period is 12 months or less and ends by the last day of the following income year. For a specific deduction, use its own timing rule. For example, a qualifying gift of money under Division 30 is generally deducted in the income year the gift is made. _([ATO, Deductions for prepaid expenses 2026](https://www.ato.gov.au/law/view/print?DocID=SAV%2FDPE%2F00001))_

### Step 6 - Is there evidence?

- **Evidence** -- See Section 6. Substantiation is a condition of the deduction, not an audit formality.

## Section 5 - The standard deduction for work-related expenses, from 2026-27

From 2026-27, an individual who is an Australian tax resident at any time in the year and derives
assessable labour income under section 25-130 qualifies. This includes salary, director fees and
other amounts in section 25-130(4). Business or investment income alone is insufficient. The ATO
applies the deduction automatically. The starting amount is the smaller of $1,000 and the year's
assessable labour income. No expense or record is required for the standard deduction itself.

Covered expenses actually claimed reduce the standard deduction dollar for dollar, to a minimum
of zero. Compare those expenses with the taxpayer's starting amount. If they are below it, the
taxpayer can leave the covered expenses off the return and receive the full standard deduction.
If they claim them, substantiate the claim and allow for the automatic reduction. Record and
claim eligible expenses outside this calculation separately. These include union fees, eligible
trade, business and professional association memberships, deductible income protection, personal
sickness and accident insurance premiums, investment expenses and eligible gifts.

From 2026-27, check section 40-425(9) before allocating assets to a low-value pool. It bars
allocation if, at first use or installation ready for use, the taxpayer reasonably expected
to use the asset mainly to earn assessable labour income. Assets already allocated by 2025-26
keep their pool treatment. Under section 40-291A the taxpayer can elect to reduce an assessable
or deductible balancing adjustment by 50% instead of using the ordinary reductions under
sections 40-290 and 40-291. The asset must have been used to earn assessable labour income and
its effective life must overlap a year in which the taxpayer used the standard deduction.

The deduction was enacted by Schedule 4 of the Treasury Laws Amendment (Tax Reform No. 1)
Act 2026. The related employer FBT restrictions start on 1 April 2027. [ATO, Standard deduction
for work-related expenses](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses)
and [Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/pdf).

## Section 6 - Substantiation

Substantiation is a statutory condition. Division 900 of the ITAA 1997 sets the written evidence
rules for work expenses, car expenses, travel expenses and business travel expenses.

**Substantiation requirements**  _([ATO, Fixed rate method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method); [ATO, Cents per kilometre method](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-motor-vehicle-expenses/cents-per-kilometre-method))_

| Requirement | Rule |
| --- | --- |
| General work expense evidence | Keep written evidence for actual expenses unless a statutory exception applies. The general particulars are the supplier, amount, nature of the goods or services, date of the expense and date of the document |
| Former $300 work expense rule | For 2025-26 and earlier years, section 900-35 relaxed the written evidence requirement for eligible claims up to $300. The exception was repealed from 2026-27. Substantiate actual amounts under the remaining rules |
| Car expenses, cents per kilometre method | Up to 5,000 business kilometres per car per year. No written evidence of the kilometres is required, but the basis of the estimate must be able to be shown, for example diary records |
| Car expenses, logbook method | Keep a continuous logbook for at least 12 weeks or for the whole period you held the car if shorter. Keep odometer readings and expense records. The logbook can ordinarily be used for up to five income years. Update it if usage changes materially |
| Working from home, fixed rate method | Record actual hours as you work from home and keep evidence of each type of additional expense incurred. The rate was 70 cents per hour for 2024-25 and 2025-26 |
| Travel with an allowance | A qualifying employer travel allowance can relieve written evidence requirements for deductible covered expenses within the Commissioner's reasonable amounts. Keep evidence that you incurred the expenses and written evidence for all overseas accommodation. [ATO, Travel allowance record keeping exceptions](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/cars-transport-and-travel/overnight-travel-expenses-and-allowances/travel-allowances-for-overnight-travel/record-keeping-exceptions-for-travel-allowance-expenses) |
| Record retention | Generally five years after lodging for employee work expense records. Business, CGT and carried-forward loss records have their own retention periods |

The cents per kilometre rate and the working from home fixed rate are set per income year. Look up
the rate for the year being prepared rather than carrying last year's forward.

## Section 7 - Capital allowances and write-offs

**Capital allowances and write-offs**  _([ATO, Instant asset write-off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off))_

| Mechanism | What it applies to | Key point |
| --- | --- | --- |
| Division 40 decline in value | Depreciating assets | Prime cost or diminishing value, over the asset's effective life. The Commissioner's effective life determination is a safe starting point |
| Immediate deduction for low cost items | Items costing $300 or less used mainly to produce non-business income | Does not apply to a set, or to substantially identical items, that together cost more than $300 |
| Instant asset write-off | Eligible small business entities choosing simplified depreciation, subject to exclusions and prior claims | Full statutory asset cost, adjusted for GST entitlements before private-use apportionment, must be strictly less than $20,000. Deduct only the taxable-use amount. Temporary threshold covers first taxable use or installation in 2025-26; the permanent threshold applies to specified first use or installation from 1 July 2026. [ITAA 1997 ss 328-175 and 328-180](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html), [ITTPA s 328-180(4)(d)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [No. 2 Act schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text) |
| Small business general pool | Covered assets not individually deductible, including exactly $20,000, and continuing pools | Ordinary deduction: 30% of the opening pool balance plus 15% of taxable-purpose adjustable values for assets first used or installed ready for taxable use during the year, with separate rules for second-element costs. If the statutory amount before ordinary depreciation is positive and less than $20,000, deduct it instead and close the pool at zero. [ITAA 1997 ss 328-185, 328-190, 328-210 and 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) and [ITTPA s 328-180(6)(e)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Division 43 capital works | Buildings and structural improvements | A fixed annual rate over a fixed period, claimed separately from Division 40 |
| Section 40-880 | Certain business-related capital expenditure not deductible elsewhere | Normally 20% per year over five income years starting in the year incurred. Certain start-up costs can be deducted immediately |
| Car limit | Cars designed mainly to carry passengers, subject to exceptions | Check both the depreciation cost limit for the year you start to hold the car and the separate GST credit limit if claiming a credit |

**Check eligibility and the first taxable-use year.** For an individual asset deduction, small business entity status and the required simplified-depreciation choice must apply in both the year you started to hold the asset and the first taxable-use year (s 328-180(1)(a) and (ab)). The temporary 2025-26 asset threshold additionally requires you to have first acquired the asset at or after 7.30 pm ACT time on 12 May 2015. The 2026 permanent threshold was enacted on 26 August 2026. Schedule 2 commenced on 1 October 2026 and item 15 applies to specified assets first used or installed ready for use from 1 July 2026; an acquisition date alone does not establish the year or permit a second deduction. The temporary 2025-26 provisions remain relevant to that year. Existing pools continue under section 328-220 after small business entity status or a later simplified-depreciation choice ceases; new assets cannot enter the pool until an eligible choosing year. See `au-individual-return.md` for the detailed cost, use, allocation and pool calculation. [No. 2 Act schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text), [ITAA 1997 ss 328-175 to 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) and [ITTPA s 328-180](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

**Worked example: strict cost boundary.** Assume eligible assets, the required simplified-depreciation choice, first taxable use in 2026-27, 100% taxable use and no other pool amounts. A $19,999 asset can qualify for the individual write-off. An asset costing exactly $20,000 enters the pool. Its pre-depreciation pool amount is not less than $20,000, so its 15% deduction is $3,000 and closing balance is $17,000. Do not write off that closing balance again in the same year.

```oa-check
name: Deductions guide distinguishes below and exactly 20000
inputs:
  below_cost: 19999
  exact_cost: 20000
  taxable_use_percent: 100
  first_use_rate: 15
steps:
  - individual_deduction: pct(below_cost, taxable_use_percent)
  - pre_depreciation_pool: pct(exact_cost, taxable_use_percent)
  - pool_deduction: pct(pre_depreciation_pool, first_use_rate)
  - closing_pool: pre_depreciation_pool - pool_deduction
expected:
  individual_deduction: 19999
  pre_depreciation_pool: 20000
  pool_deduction: 3000
  closing_pool: 17000
```

**Worked example: full cost and low pool.** Assume the same eligibility and timing, no other pool amounts and a $30,000 asset used 60% for taxable purposes. Its full cost fails the individual less-than-$20,000 test. Its taxable-purpose amount of $18,000 enters the pool. The statutory pre-depreciation pool amount is positive and less than $20,000, so the pool deduction is $18,000 and closing balance is zero, instead of an ordinary 15% pool deduction.

```oa-check
name: Deductions guide keeps full cost separate from low pool value
inputs:
  full_cost: 30000
  taxable_use_percent: 60
steps:
  - taxable_amount: pct(full_cost, taxable_use_percent)
  - pre_depreciation_pool: taxable_amount
  - low_pool_deduction: pre_depreciation_pool
  - closing_pool: pre_depreciation_pool - low_pool_deduction
expected:
  taxable_amount: 18000
  pre_depreciation_pool: 18000
  low_pool_deduction: 18000
  closing_pool: 0
```

## Section 8 - Tax offsets

### 8.1 The offsets most often in play

**The offsets most often in play**  _([ATO, Low income tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset); [ATO, Seniors and pensioners tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset))_

| Offset | Refundable | Summary |
| --- | --- | --- |
| Low income tax offset (LITO) | No | For eligible Australian tax residents, up to $700 where taxable income is $37,500 or less. Between $37,501 and $45,000 the offset is $700 less 5 cents per dollar above $37,500. Between $45,001 and $66,667 it is $325 less 1.5 cents per dollar above $45,000. Nil above $66,667. Applied automatically |
| Seniors and pensioners tax offset (SAPTO) | No | Requires eligibility for a listed Australian Government pension or allowance, and income tests for the taxpayer and spouse. Unused amounts may be transferable between eligible spouses. Entitlement to at least $1 also raises the Medicare levy low income threshold |
| Private health insurance rebate | Yes | Income tested, and can be taken as a premium reduction or as an offset in the return |
| Franking credits on franked dividends | Yes | Eligible resident individuals and complying super funds include the credit in assessable income and claim the offset. Check the qualified person rules, including the holding period and related payments, and the dividend washing rules. [ATO, You and your shares 2026](https://www.ato.gov.au/law/view/document?docid=SAV%2FYAYS%2F00001) |
| Foreign income tax offset | No | Generally limited to the greater of $1,000 and the amount calculated under section 770-75, and cannot exceed qualifying foreign tax paid. See `au-foreign-income.md` |
| Small business income tax offset | No | For eligible net small business income from a sole trader business or a share from a small business partnership or trust. The business must have aggregated turnover of less than $5 million. [ATO, Small business income tax offset](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/concessions-offsets-and-rebates/small-business-income-tax-offset) |
| Zone and overseas forces offsets | No | Narrow eligibility rules |
| Beneficiary tax offset | No | For recipients of certain Commonwealth benefits and allowances |

### 8.2 Unused offsets and other liabilities

- **Unused offsets and other liabilities** -- - An unused non-refundable offset is not paid out as an offset refund. Reducing income tax can still create or increase a credit after PAYG withholding and instalment credits are applied. - Most offsets do not reduce Medicare levy. However, section 63-10 table items 21 and 22 apply remaining veterans' superannuation (invalidity pension) tax offset and foreign income tax offset to Medicare levy, then Medicare levy (fringe benefits) surcharge. The remaining excess cannot be refunded, transferred or carried forward. See `au-foreign-income.md` for FITO limits. - SAPTO affects the Medicare levy indirectly through the low income threshold; it does not reduce the levy directly. - An offset does not reduce a HELP or other study and training support loan repayment, which is calculated on repayment income, not on tax payable.  _([ITAA 1997 s 63-10(1), table items 21 and 22](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10), [ATO, About tax offsets](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets))_

## Section 9 - Concessions

Concessions change the base or the rules rather than reducing tax directly.

**Concessions**

| Concession | Test | Guide |
| --- | --- | --- |
| Small business entity concessions | Aggregated turnover thresholds, which differ by concession | `australia-bookkeeping.md`, `au-individual-return.md` |
| Small business CGT concessions | $6 million maximum net asset value test, CGT small business entity with aggregated turnover below $2 million, or an eligible partnership or passively held asset route. Apply the active asset test and check the other basic and concession-specific conditions | `au-small-business-cgt.md` |
| CGT discount | 12 months of ownership, and entity and residency tests | `au-capital-gains.md` |
| Main residence exemption | Dwelling used as the main residence, with partial and absence rules. Check the foreign-resident life events test if the taxpayer is a foreign resident at the CGT event. [ATO, Main residence exemption for foreign residents](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents) | `au-capital-gains.md`, `au-rental-property.md` |
| Research and development tax incentive | Registered eligible R&D activities | `au-rd-incentive.md` |
| Not-for-profit and DGR concessions | Endorsement and purpose tests | `au-not-for-profit.md` |

Do not treat a concession as available because the taxpayer is small. Each has its own test, and
the aggregated turnover threshold is not the same for every concession.

## Section 10 - Interactions and traps

- **Reimbursement removes the deduction.** An expense the employer pays or reimburses is not
  deductible to the employee. It may instead be a fringe benefit to the employer.
- **Salary packaging.** An expense met by the employer under a salary packaging arrangement is
  generally excluded from the employee's actual expense deductions. From 1 April 2027 the
  standard deduction legislation also restricts the employer's FBT treatment of certain packaged
  work expenses and items. [ATO, Reducing your FBT liability](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/exemptions-concessions-and-other-ways-to-reduce-fbt/reducing-your-fbt-liability).
- **GST credits reduce deductions.** Reduce the otherwise deductible expense by the input tax
  credit to which the taxpayer is entitled. Any GST included in the expense for which there is no
  credit entitlement remains part of the cost.
- **Non-commercial losses.** An individual's loss from a business activity may be deferred. Check
  the primary production and professional arts exception, the income requirement and statutory
  tests, and any applicable exercise of the Commissioner's discretion.
- **Personal services income.** PSI rules can deny deductions that would otherwise be available,
  particularly for rent, home office occupancy costs and payments to associates. See `au-psi.md`.
- **Capital allowance and CGT overlap.** Check what Division 43 capital works deductions must be
  excluded from the property's cost base or reduced cost base, including amounts still claimable.
  For Division 40 depreciating assets, apply the balancing adjustment rules and check whether
  CGT event K7 applies to non-taxable use. [ATO, Cost base adjustments for capital works](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-adjustments-for-capital-works) and [ITAA 1997 ss 104-235 and 118-24](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).
- **Deduction timing versus payment.** Superannuation contributions are deductible in the year the
  fund receives them, not the year they are journalised.

## Section 11 - Worked example

**Facts.** The employee is an Australian tax resident for the whole of the 2026-27 income year,
with salary of $92,000 and $19,000 of PAYG withheld. Assume no other income, spouse, dependants,
private health insurance rebate, Medicare levy exemption, Medicare levy surcharge or HELP debt.
All figures are synthetic.

**Substantiated amounts for the year**

| Item | Synthetic cost | Treatment |
| --- | --- | --- |
| Tools, work-related journal, work-related phone use | $780 total | Work-related expenses |
| Union fees for current employment | $620 | Claimable in addition to the standard deduction |
| Income protection insurance premiums covering loss of employment income | $540 | Claimable in addition to the standard deduction |
| Qualifying monetary gift to a deductible gift recipient | $200 | Claimable in addition to the standard deduction |
| Interest on a margin loan on income-producing shares | $1,300 | Investment expense, claimable in addition |

**Step 1, work out the standard deduction.** The maximum is $1,000 because salary is $92,000.
Leave the $780 of covered expenses off the return to receive the full $1,000 automatically.

**Step 2, total deductions.**

```
Standard deduction for work-related expenses      1,000
Union fees                                          620
Income protection premiums                          540
DGR donation                                        200
Margin loan interest                              1,300
Total deductions                                  3,660
```

**Step 3, taxable income.**

```
Salary                                           92,000
Less deductions                                   3,660
Taxable income                                   88,340
```

**Step 4, tax at 2026-27 resident rates.**

```
0 to 18,200                                         nil
18,201 to 45,000 at 15c      26,800 x 0.15      = 4,020
45,001 to 88,340 at 30c      43,340 x 0.30      = 13,002
Gross tax                                       = 17,022
```

**Step 5, offsets.** Taxable income of $88,340 exceeds $66,667, so LITO is nil.

**Step 6, Medicare levy and the result.**

```
Medicare levy   88,340 x 2%                     =  1,766.80
Total tax and levy                              = 18,788.80
Less PAYG withheld                              = 19,000.00
Refund                                          =    211.20
```

**Step 7, compare with claiming actual work-related expenses.** If the employee claims the $780,
the ATO applies a reduced standard deduction of $1,000 less $780, or $220. The 2 amounts add to
$1,000. Taxable income remains $88,340, tax $17,022, Medicare levy $1,766.80 and the refund $211.20.

**What the example shows.** The 4 other expenses reduce taxable income by $2,660. At a 30%
marginal tax rate and the full 2% Medicare levy, they reduce the tax and levy by $851.20.

```oa-check
name: Claimed labour expenses reduce the automatic standard deduction
inputs:
  salary: 92000
  standard_limit: 1000
  covered_expenses_claimed: 780
  other_deductions: 2660
  payg_withheld: 19000
steps:
  - standard_deduction: max(0, min(standard_limit, salary) - covered_expenses_claimed)
  - taxable_income: salary - standard_deduction - covered_expenses_claimed - other_deductions
  - income_tax: pct(45000 - 18200, 15) + pct(taxable_income - 45000, 30)
  - medicare_levy: pct(taxable_income, 2)
  - refund: payg_withheld - income_tax - medicare_levy
expected:
  standard_deduction: 220
  taxable_income: 88340
  income_tax: 17022
  medicare_levy: 1766.80
  refund: 211.20
```

## Section 12 - Common errors

- Treating an offset as a deduction, or the reverse, and overstating the benefit by a factor of
  three or more.
- Assuming a non-refundable offset produces a refund where there is no tax to reduce.
- Applying the 2025-26 rules to a 2026-27 return, or the reverse, now that the standard deduction
  and the 15% second bracket apply from 1 July 2026.
- Applying the former $300 written-evidence exception to actual work expenses claimed for 2026-27.
- Carrying forward last year's cents per kilometre rate or working from home rate.
- Claiming a deduction for an expense the employer reimbursed, or that was salary packaged.
- Claiming the GST-inclusive cost where a GST credit was also claimed.
- Claiming a capital item as an immediate deduction because it is small, without checking the
  instant asset write-off limit and eligibility for the year.
- Ignoring the non-commercial loss rules for an individual's side business.
- Claiming both Division 40 and Division 43 on the same expenditure.

## Section 13 - Self-checks

- [ ] The income year is identified, and the rules used are those for that year.
- [ ] Each item is classified as a deduction, capital allowance, offset or concession.
- [ ] Each offset is identified as refundable or non-refundable.
- [ ] Every deduction meets its governing provision's eligibility rules, limits and apportionment requirements; section 8-1 claims pass the nexus test.
- [ ] Each claim meets its applicable evidence requirements, and any apportionment method is documented.
- [ ] Capital items use the correct regime, including the eligibility rules for any immediate write-off.
- [ ] Amounts reimbursed or salary packaged are excluded.
- [ ] The offsets are applied to tax payable, not to taxable income.
- [ ] Offsets follow section 63-10 priorities, including any application to Medicare levy or surcharge and the treatment of unused amounts.
- [ ] Refunds of excess PAYG payments are distinguished from refunds of unused offsets.
- [ ] Rates, thresholds and limits are confirmed against the ATO page for the income year.

## Sources

- Income Tax Assessment Act 1997, s 8-1 (general deductions), s 8-5 (specific deductions),
  Division 25 (specific deductions), Division 26 (denials), Division 40 (capital allowances),
  Division 43 (capital works), Division 900 (substantiation).
- Treasury Laws Amendment (Tax Reform No. 1) Act 2026,
  https://www.legislation.gov.au/C2026A00049/latest
- ATO, Standard deduction for work-related expenses,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses
- ATO, Claiming deductions,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/how-to-claim-deductions
- ATO, About tax offsets,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets
- ATO, Low income tax offset,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset
- ATO, Seniors and pensioners tax offset,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset
- ATO, Fixed rate method for working from home,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method
- ATO, Instant asset write-off,
  https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off
- ATO, Tax rates: Australian resident,
  https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents

Sources for the 2026-27 standard deduction, offsets and worked example were checked as at
22 November 2026. The working from home table gives historical rates through 2025-26.

Not yet confirmed: the working from home fixed rate for 2026-27.

Check this point with one of our partner accountants.

Selected simplified-depreciation rules read 2026-11-12:

- [ITAA 1997 ss 328-175, 328-180, 328-185, 328-190, 328-210 and 328-220](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html): eligibility, cost, allocation, ordinary rates, low-pool value and continuing pools. Read 2026-11-12.
- [ITTPA 1997 s 328-180(4)(d) and (6)(e)](https://www.legislation.gov.au/C2004A05128/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html): temporary 2025-26 asset and pool thresholds. Read 2026-11-12.
- [Tax Reform No. 2 Act 2026 schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text): application of the permanent threshold. Read 2026-11-12.

## Section 15 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

The most up-to-date version of this skill is maintained at
[openaccountants.com](https://www.openaccountants.com).

> [Contributor history](https://github.com/openaccountants/openaccountants/commits/main/skills/australia/au-deductions-offsets.md).
