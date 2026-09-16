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
version: 0.1
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027), with 2025-26 differences noted"
last_updated: 2026-09-16
review_status: pending_review
depends_on:
  - au-individual-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Deductions, Offsets and Concessions v0.1

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

---

## Section 1 - The vocabulary map

| Mechanism | What it reduces | Typical value of $1 | Australian examples |
| --- | --- | --- | --- |
| **Deduction** | Assessable income, producing taxable income | The taxpayer's marginal rate, so worth more to higher earners | Work-related expenses, rental expenses, business expenses, personal super contributions, donations to deductible gift recipients |
| **Capital allowance** | Assessable income, spread over time or immediately | Marginal rate, but timing changes the value | Decline in value under Division 40, capital works under Division 43, instant asset write-off |
| **Tax offset (also called a rebate)** | Tax payable, after tax is calculated | $1 of tax, regardless of marginal rate | Low income tax offset, seniors and pensioners tax offset, foreign income tax offset, private health insurance rebate |
| **Concession or exemption** | The base itself, or the rules that apply to it | Varies | Small business CGT concessions, the 50% CGT discount, main residence exemption, small business entity concessions |

**Why the distinction matters.** A deduction of $1,000 saves $320 for someone on a 30% marginal
rate plus the 2% Medicare levy, and $470 for someone on the top rate. An offset of $1,000 saves
$1,000 for both, but only if there is $1,000 of tax to reduce.

**Refundable and non-refundable offsets.** Most offsets are non-refundable: they can reduce tax
payable to zero but no further, and the unused amount is lost. Some are refundable, so the excess
is paid out. Franking credits attached to franked dividends and the private health insurance
rebate are refundable. Check this before telling a taxpayer an offset is worth anything to them.
[ATO, About tax offsets](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets)

---

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

---

## Section 3 - The order of operations

Apply in this order. Reversing steps 4 and 5 is a common source of wrong answers.

1. Work out assessable income, including net capital gains.
2. Subtract allowable deductions to get taxable income.
3. Apply the rates for the income year to taxable income, giving gross tax.
4. Subtract non-refundable offsets, stopping at zero.
5. Subtract refundable offsets and credits, which can produce a refund.
6. Add the Medicare levy and any Medicare levy surcharge, which are separate from the offsets in
   step 4.
7. Subtract amounts already paid: PAYG withholding and PAYG instalments.

A tax loss arises where deductions exceed assessable income. A loss is carried forward, not
converted to a refund, and its use is restricted for individuals by the non-commercial loss rules
and for companies by the continuity of ownership and business continuity tests.

---

## Section 4 - Deductions: the decision steps

Run every proposed deduction through these steps in order. Stop at the first step that denies it.

### Step 1 - Is there a nexus with assessable income?

A loss or outgoing is deductible to the extent it is incurred in gaining or producing assessable
income, or necessarily incurred in carrying on a business for that purpose.
[ITAA 1997 s 8-1](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-1)

The ATO states the test for an employee as three conditions: the taxpayer spent the money and was
not reimbursed, the expense directly relates to earning income, and there is a record to prove it.
[ATO, Claiming deductions](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/how-to-claim-deductions)

An employer instruction to buy something does not by itself make it deductible.

### Step 2 - Is it private, domestic or capital in nature?

Section 8-1 denies a deduction to the extent the outgoing is private or domestic, or capital or of
a capital nature. Ordinary travel between home and work and daily lunches are private.

Capital expenditure is not lost, it moves to a different regime: Division 40 decline in value,
Division 43 capital works, the CGT cost base, or a specific write-off provision such as
Division 40-880 for certain business-related capital expenditure.

### Step 3 - Does a specific provision deny or limit it?

Deductibility can be denied even where the nexus exists. Examples include entertainment expenses,
penalties and fines, holding costs for vacant land held by most non-business taxpayers, and
general interest charge and shortfall interest charge incurred on or after 1 July 2025. Check the
specific provision before allowing an unusual item.

### Step 4 - Apportion

Where an expense serves both an income-producing and a private purpose, only the income-producing
share is deductible. The apportionment method must be reasonable and documented. A percentage
guessed at year end is not a method.

### Step 5 - Is it incurred in this income year?

"Incurred" is not the same as "paid". Prepayment rules can spread a deduction over the period the
benefit covers, with a 12 month exception available to individuals for non-business expenditure
and to small business entities.

### Step 6 - Is there evidence?

See Section 6. Substantiation is a condition of the deduction, not an audit formality.

---

## Section 5 - The standard deduction for work-related expenses, from 2026-27

A standard deduction of up to $1,000 for work-related expenses applies to Australian tax residents
who earn income from work. It commences on 1 July 2026 and first applies to the 2026-27 individual
tax return. It does not apply to the 2025-26 return.

According to the ATO's summary of the measure:

- Current arrangements continue for a taxpayer with more than $1,000 of work-related expenses, and
  for a taxpayer who earns only business or investment income.
- Some deductions remain claimable in addition to the standard deduction, including expenses that
  are not work-related such as investment expenses and charitable donations, union and professional
  association membership fees, and income protection insurance premiums.
- The measure prevents a double benefit where an expense covered by the standard deduction is
  salary packaged.
- Substantiation and capital allowance rules were updated to support the measure.

The measure is law, enacted by the Treasury Laws Amendment (Tax Reform No. 1) Act 2026 and the
Income Tax Rates Amendment (Tax Reform No. 1) Act 2026.
[ATO, Standard deduction for work-related expenses](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/standard-deduction-for-work-related-expenses);
[Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/latest);
[Income Tax Rates Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00050/latest)

**Practical effect.** For a work-only taxpayer whose substantiated work-related expenses are under
$1,000, the standard deduction is the better claim and removes the need to build a schedule of
small items. For a taxpayer above $1,000, nothing changes and the full substantiation rules
continue to apply to the actual claim.

**Confirm the detailed operation before applying it.** The mechanics that matter in practice, in
particular whether the standard deduction is applied automatically or elected, and exactly which
items sit outside it, must be checked against the ATO's 2026-27 return instructions when they are
published. This guide states the measure as the ATO summarised it on 26 June 2026.

---

## Section 6 - Substantiation

Substantiation is a statutory condition. Division 900 of the ITAA 1997 sets the written evidence
rules for work expenses, car expenses, travel expenses and business travel expenses.

| Requirement | Rule |
| --- | --- |
| General work expense evidence | Written evidence is required. The document must show the supplier, the amount, the nature of the goods or services, the date of the expense and the date of the document |
| The $300 total work expense rule | Where total work expense claims for the year are $300 or less, the written evidence rule is relaxed, but the expense must still have been incurred and the claim must still be reasonable. This is not a free $300 |
| Car expenses, cents per kilometre method | Up to 5,000 business kilometres per car per year. No written evidence of the kilometres is required, but the basis of the estimate must be able to be shown, for example diary records |
| Car expenses, logbook method | A logbook covering a continuous period of at least 12 weeks, valid for five years, plus odometer readings and expense records |
| Working from home, fixed rate method | A record of the total hours worked from home for the year, plus evidence that the expenses were incurred. The rate was 70 cents per hour for 2024-25 and 2025-26 |
| Travel with an allowance | Reasonable amounts determined annually by the Commissioner can remove the need to keep receipts, but not the requirement to have incurred the expense |
| Record retention | Generally five years from the date the return is lodged, and longer where a CGT asset or a carried-forward loss depends on the record |

[ATO, Fixed rate method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method);
[ATO, Cents per kilometre method](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-motor-vehicle-expenses/cents-per-kilometre-method)

The cents per kilometre rate and the working from home fixed rate are set per income year. Look up
the rate for the year being prepared rather than carrying last year's forward.

---

## Section 7 - Capital allowances and write-offs

| Mechanism | What it applies to | Key point |
| --- | --- | --- |
| Division 40 decline in value | Depreciating assets | Prime cost or diminishing value, over the asset's effective life. The Commissioner's effective life determination is a safe starting point |
| Immediate deduction for low cost items | Items costing $300 or less used mainly to produce non-business income | Does not apply to a set, or to substantially identical items, that together cost more than $300 |
| Instant asset write-off | Small business entities using the simplified depreciation rules | The limit is set per income year. It was $20,000 per asset for assets first used or installed ready for use between 1 July 2025 and 30 June 2026, for businesses with aggregated turnover under $10 million |
| Small business general pool | Assets costing at or above the instant asset write-off limit | 15% in the first year, 30% each year after |
| Division 43 capital works | Buildings and structural improvements | A fixed annual rate over a fixed period, claimed separately from Division 40 |
| Division 40-880 | Certain business-related capital expenditure not deductible elsewhere | Spread over five years |
| Car limit | Cars used for a business or income-producing purpose | Caps both the depreciation base and the GST credit. Look up the limit for the income year |

**Confirm the instant asset write-off limit for the year being prepared.** The limit has changed
repeatedly. As at 16 September 2026 the ATO had published the $20,000 limit for 2025-26; the limit
for 2026-27 must be confirmed on the ATO instant asset write-off page before it is applied.
[ATO, Instant asset write-off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off)

---

## Section 8 - Tax offsets

### 8.1 The offsets most often in play

| Offset | Refundable | Summary |
| --- | --- | --- |
| Low income tax offset (LITO) | No | Up to $700 where taxable income is $37,500 or less. Between $37,501 and $45,000 the offset is $700 less 5 cents per dollar above $37,500. Between $45,001 and $66,667 it is $325 less 1.5 cents per dollar above $45,000. Nil above $66,667. Applied automatically |
| Seniors and pensioners tax offset (SAPTO) | No | Requires eligibility for a listed Australian Government pension or allowance, and income tests for the taxpayer and spouse. Unused amounts may be transferable between eligible spouses. Entitlement to at least $1 also raises the Medicare levy low income threshold |
| Private health insurance rebate | Yes | Income tested, and can be taken as a premium reduction or as an offset in the return |
| Franking credits on franked dividends | Yes | Included in assessable income first, then offset against tax, with the excess refundable to most resident individuals and complying super funds |
| Foreign income tax offset | No | Limited to the Australian tax on the doubly taxed income. See `au-foreign-income.md` |
| Small business income tax offset | No | For an individual with net small business income from a sole trader business or a share from a small business partnership or trust. Confirm the rate and cap for the income year |
| Zone and overseas forces offsets | No | Narrow eligibility rules |
| Beneficiary tax offset | No | For recipients of certain Commonwealth benefits and allowances |

[ATO, Low income tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset);
[ATO, Seniors and pensioners tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset)

### 8.2 What an offset cannot do

- A non-refundable offset cannot create or increase a refund.
- An offset does not reduce the Medicare levy, which is calculated separately. SAPTO affects the
  Medicare levy indirectly, through the low income threshold, not by reducing the levy directly.
- An offset does not reduce a HELP or other study and training support loan repayment, which is
  calculated on repayment income, not on tax payable.

---

## Section 9 - Concessions

Concessions change the base or the rules rather than reducing tax directly.

| Concession | Test | Guide |
| --- | --- | --- |
| Small business entity concessions | Aggregated turnover thresholds, which differ by concession | `australia-bookkeeping.md`, `au-individual-return.md` |
| Small business CGT concessions | $6 million maximum net asset value test or small business entity status, plus the active asset test | `au-small-business-cgt.md` |
| CGT discount | 12 months of ownership, and entity and residency tests | `au-capital-gains.md` |
| Main residence exemption | Dwelling used as the main residence, with partial and absence rules | `au-capital-gains.md`, `au-rental-property.md` |
| Research and development tax incentive | Registered eligible R&D activities | `au-rd-incentive.md` |
| Not-for-profit and DGR concessions | Endorsement and purpose tests | `au-not-for-profit.md` |

Do not treat a concession as available because the taxpayer is small. Each has its own test, and
the aggregated turnover threshold is not the same for every concession.

---

## Section 10 - Interactions and traps

- **Reimbursement removes the deduction.** An expense the employer pays or reimburses is not
  deductible to the employee. It may instead be a fringe benefit to the employer.
- **Salary packaging removes it too.** An expense met from pre-tax salary cannot also be deducted.
  The standard deduction measure includes a specific rule preventing that double benefit.
- **A GST credit is not a deduction.** Where a GST credit is claimable, the deductible amount is
  the GST-exclusive cost. Where it is not claimable, for example on an input taxed acquisition or
  by an unregistered taxpayer, the GST-inclusive amount is the cost.
- **Non-commercial losses.** An individual's loss from a business activity may be quarantined
  unless one of the statutory tests is met or the Commissioner exercises the discretion.
- **Personal services income.** PSI rules can deny deductions that would otherwise be available,
  particularly for rent, home office occupancy costs and payments to associates. See `au-psi.md`.
- **Capital allowance and CGT overlap.** Amounts deducted under Division 40 or Division 43 reduce
  the cost base of the underlying asset, so a deduction now can increase a capital gain later.
- **Deduction timing versus payment.** Superannuation contributions are deductible in the year the
  fund receives them, not the year they are journalised.

---

## Section 11 - Worked example

**Facts.** Nadia is an Australian tax resident for the whole of the 2026-27 income year. She is an
employee with salary of $92,000 and $19,000 of PAYG withheld. She has no spouse, no private health
insurance obligations in issue, and no HELP debt. All figures are synthetic.

Her substantiated amounts for the year:

| Item | Amount | Treatment |
| --- | --- | --- |
| Tools, work-related journal, work-related phone use | $780 total | Work-related expenses |
| Union fees | $620 | Claimable in addition to the standard deduction |
| Income protection insurance premiums | $540 | Claimable in addition to the standard deduction |
| Donation to a deductible gift recipient | $200 | Not work-related, claimable in addition |
| Interest on a margin loan on income-producing shares | $1,300 | Investment expense, claimable in addition |

**Step 1, choose the work-related expense basis.** Her work-related expenses of $780 are less than
$1,000, so the standard deduction of $1,000 produces the larger claim.

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

**Step 7, compare with claiming actual work-related expenses.** Claiming the actual $780 instead
of the $1,000 standard deduction would give taxable income of $88,560, tax of $17,088, a Medicare
levy of $1,771.20 and a refund of $140.80. The standard deduction is worth $70.40 more, being the
$220 difference in deductions at her 30% marginal rate plus the 2% Medicare levy.

**What the example shows.** The value of a deduction is the deduction multiplied by the marginal
rate and the levy, not the deduction itself. It also shows why the four extra items matter: each
is outside the standard deduction, so each still reduces tax in full.

---

## Section 12 - Common errors

- Treating an offset as a deduction, or the reverse, and overstating the benefit by a factor of
  three or more.
- Assuming a non-refundable offset produces a refund where there is no tax to reduce.
- Applying the 2025-26 rules to a 2026-27 return, or the reverse, now that the standard deduction
  and the 15% second bracket apply from 1 July 2026.
- Claiming $300 of work expenses with no expense actually incurred. The relaxation is of the
  written evidence rule, not of the requirement to have spent the money.
- Carrying forward last year's cents per kilometre rate or working from home rate.
- Claiming a deduction for an expense the employer reimbursed, or that was salary packaged.
- Claiming the GST-inclusive cost where a GST credit was also claimed.
- Claiming a capital item as an immediate deduction because it is small, without checking the
  instant asset write-off limit and eligibility for the year.
- Ignoring the non-commercial loss rules for an individual's side business.
- Claiming both Division 40 and Division 43 on the same expenditure.

---

## Section 13 - Self-checks

- [ ] The income year is identified, and the rules used are those for that year.
- [ ] Each item is classified as a deduction, capital allowance, offset or concession.
- [ ] Each offset is identified as refundable or non-refundable.
- [ ] Every deduction passes the nexus test, is not denied by a specific provision, and is
      apportioned where private use exists.
- [ ] Substantiation exists for every claim, and the method of apportionment is documented.
- [ ] Capital items are in the correct regime rather than claimed outright.
- [ ] Amounts reimbursed or salary packaged are excluded.
- [ ] The offsets are applied to tax payable, not to taxable income.
- [ ] The Medicare levy is calculated separately from the offsets.
- [ ] Rates, thresholds and limits are confirmed against the ATO page for the income year.

---

## Section 14 - Sources

- Income Tax Assessment Act 1997, s 8-1 (general deductions), s 8-5 (specific deductions),
  Division 25 (specific deductions), Division 26 (denials), Division 40 (capital allowances),
  Division 43 (capital works), Division 900 (substantiation).
- Treasury Laws Amendment (Tax Reform No. 1) Act 2026,
  https://www.legislation.gov.au/C2026A00049/latest
- Income Tax Rates Amendment (Tax Reform No. 1) Act 2026,
  https://www.legislation.gov.au/C2026A00050/latest
- ATO, Standard deduction for work-related expenses,
  https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/standard-deduction-for-work-related-expenses
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

Sources were checked on 16 September 2026. The working from home fixed rate and the instant asset
write-off limit for 2026-27 had not been published at that date.

---

## Section 15 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

The most up-to-date version of this skill is maintained at
[openaccountants.com](https://www.openaccountants.com).

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
