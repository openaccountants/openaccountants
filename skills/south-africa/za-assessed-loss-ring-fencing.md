---
name: za-assessed-loss-ring-fencing
description: >
  South African section 20A ring-fencing of assessed losses for natural persons, and the section 20 carry-forward rules it sits on, for the 2027 year of assessment (1 March 2026 to 28 February 2027) and earlier years. Covers the income threshold that triggers ring-fencing and its move by the Taxation Laws Amendment Act 5 of 2026 from the 45% maximum marginal rate to the 39% marginal rate for years of assessment commencing on or after 1 March 2026, the listed suspect trades (including the 2026 wording for farming and animal breeding), the three-out-of-five-years test, the section 20A(3) escape and the residential letting exception, and the company 80% limitation under section 20. Use for questions about ring-fenced losses, suspect trades, hobby farming, rental losses, side businesses, or setting a trade loss off against salary.
version: 1.0
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "2026-27, the 2027 year of assessment (1 March 2026 to 28 February 2027), the first year of the 39% threshold"
last_updated: 2026-11-14
depends_on:
  - workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# South Africa: ring-fencing of assessed losses, s 20A

> **What changed.** For years of assessment commencing on or after **1 March 2026**, s 20A bites from the taxable income at which the **39%** marginal rate starts, not the 45% maximum marginal rate (Taxation Laws Amendment Act 5 of 2026, s 19). The threshold falls from about R1.8 million to under R700,000. Ring-fencing stops being a high-income edge case and becomes the default for a geared residential rental held by a reasonably paid employee. An accountant-approved file covers the same section: `ring-fencing-of-assessed-losses-under-section-20a`; it predates the 2026 Act's commencement, so check it against the threshold below.

## Scope

**s 20A ring-fencing for natural persons**, and enough of **s 20** to place it. A ring-fenced loss is quarantined, not lost.

Not covered: assessed losses of trusts; the s 20 company rules beyond the summary below; capital losses, which are an Eighth Schedule matter and not assessed losses at all; the First Schedule farming regime.

## Ask the client first

1. Taxable income for the year, **before** setting off any assessed loss or balance of assessed loss under s 20 (salary, other trades, interest, everything).
2. Which trade made the loss, and what it is (residential letting, sport, collectibles, farming, performing arts, vehicle or boat rental, and so on).
3. The trade's results for each of the last five years of assessment, including this one.
4. For a rental: who occupies the property, whether any occupant is a relative, and for how much of the year.
5. For farming or animal breeding: is it carried on full-time?
6. Evidence for a business with a reasonable prospect of profit: business plan, pricing, separate banking, hours spent, assets available for private use.

## The method, step by step

### Rates, bands and thresholds

The threshold is defined by reference to a marginal rate, so it moves with the bracket table. Read it as the floor of the band carrying that rate for the year (`za-income-tax-tables`).

| Year of assessment | Rate the threshold keys off | Taxable income at which that rate starts | Source |
| --- | --- | --- | --- |
| 2027 (2026/27) | 39% (s 20A(2) as amended by TLAA 5 of 2026, for years commencing on or after 1 March 2026) | Above R695,800 | https://www.sars.gov.za/legal-lprim-aa-2026-03-taxation-laws-amendment-act-5-of-2026-gg-54448-1-april-2026/ (rate); https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ (band floor) |
| 2026 (2025/26) | 45%, the maximum marginal rate | Above R 1,817,000 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| 2025 (2024/25) | 45%, the maximum marginal rate | Above R 1,817,000 | same |
| 2024 (2023/24) | 45%, the maximum marginal rate | Above R 1,817,000 | same |
| 2023 (2022/23) | 45%, the maximum marginal rate | Above R 1,731,600 | same |
| Company assessed loss set-off cap (s 20(1)(a)), years of assessment ending on or after 31 March 2023 | Higher of R1 million and 80% of taxable income before the set-off | Companies only | https://www.sars.gov.za/legal-intr-in-33-assessed-losses-companies-trade-and-income-from-trade-requirements/ |

A common error in commentary written during 2025 quotes the new threshold as R673,000. That was the 39% band floor for YoA **2026**, current when the amendment was proposed. The amendment applies from years of assessment commencing on or after 1 March 2026, so the first year is 2027, whose 39% band starts above **R695,800**.

### Step 1: the income test

s 20A applies only where the person's taxable income for the year, worked out **without** s 20A and **before** setting off any assessed loss or balance of assessed loss under s 20, **equals or exceeds** the amount at which the relevant marginal rate starts (table above). If this fails, s 20A does not apply, whatever the trade. Test this first.

### Step 2: the trade test

If the income test is met, the loss from a trade is ring-fenced where either:
- the trade made an assessed loss in **at least three of the last five years** of assessment, counting the current year; or
- the trade is a **listed suspect trade** (s 20A(2)(b)), which is caught on the income test alone, with no three-in-five count:
  - any sport practised by the person or a relative;
  - any dealing in collectibles;
  - the rental of residential accommodation, unless the letting exception applies;
  - the rental of vehicles, aircraft or boats as defined in the Eighth Schedule, unless at least 80% of the asset is used by persons who are not relatives for at least half the year;
  - animal showing by the person or a relative;
  - farming or animal breeding, unless carried on full-time (from 1 March 2026 the words "or activities of a similar nature" were removed from this item);
  - any form of performing or creative arts practised by the person or a relative;
  - any form of gambling or betting practised by the person or a relative;
  - any trade in respect of which a tax benefit scheme applies (as the earlier version of this file listed; see Not yet confirmed).

### Step 3: the escapes

- **Residential letting exception.** Residential accommodation is not a suspect trade where **at least 80%** of it is used by persons who are **not relatives** of the person for **at least half** of the year of assessment. Both limbs must hold.
- **Reasonable prospect of profit (s 20A(3)).** The trade escapes if it is a business with a reasonable prospect of deriving taxable income (other than taxable capital gains) within a reasonable period, having regard to: the proportion of gross income to allowable deductions; the level of activity and whether it is carried on in a commercial manner (hours, separate premises, staff, a business plan, advertising); the number of years of losses compared with the start-up period; the changes made to the business to make it profitable; whether assets are available for private use or for the use of relatives. This is a facts and evidence test. It is not available where the trade has made losses in **six or more of the last ten** years (s 20A(4)), other than farming, where the ten-year count does not apply.

### Step 4: what ring-fencing does

A ring-fenced loss is carried forward and may be set off only against income from **that same trade** in later years, not against salary or other trades. The cash effect is deferral, sometimes for ever: a rental that never makes a taxable profit carries its ring-fenced loss without ever relieving anything.

### Step 5: section 20 for context

- An assessed loss carries forward and may be set off against income from any trade, subject to s 20(2A), which requires the person to have carried on a trade in the year of set-off.
- Companies are separately limited, for years of assessment ending on or after 31 March 2023: the balance of assessed loss set off is capped at the **higher of R1 million and 80%** of taxable income before the set-off. From years ending on or after 31 December 2024 the cap does not apply to a company that has taken steps to liquidate, wind up or deregister under s 41(4) and not withdrawn them. This cap does not apply to natural persons.

## Boundary and exception table

| Situation | Result |
| --- | --- |
| Taxable income before the loss below the threshold | s 20A does not apply at all |
| Listed suspect trade, income test met, no escape | Ring-fenced at once; three-in-five is irrelevant |
| Not listed, losses in 2 of the last 5 years | Not ring-fenced |
| Not listed, losses in 3 of the last 5 years, no escape | Ring-fenced |
| Bonded rental let at market rent to the person's child | Fails the letting exception: a relative occupies it |
| Rental, 80% non-relative tenants for 5 months of 12 | Fails: the half-year limb is not met |
| Full-time farming | Outside the list; First Schedule applies |
| Losses in 6 or more of the last 10 years, not farming | s 20A(3) escape not available |
| Applying the 39% threshold to a 2026 return, or 45% to a 2027 return | Both wrong: the year of assessment decides |

### Red flags

- A salaried taxpayer above the 2027 threshold claiming a residential rental loss against salary: ring-fenced by default from 2026/27 unless an escape is proven.
- "Taxable income" taken after the loss, or remuneration taken instead of taxable income.
- A prior-year rand threshold carried forward.

## Worked cases

### Case 1: geared rental, YoA 2027, caught

An employee has taxable income of R780,000 before any loss. A bonded flat let to an unrelated tenant for the whole year makes a loss of R60,000 after interest. It made losses in 2023, 2024, 2026 and 2027.

- Income test: R780,000 equals or exceeds the 2027 39% band floor of R695,800, so the test is met. (Under the old 45% rule, R780,000 is far below R1,817,000 and s 20A would not have applied.)
- Residential letting: 100% non-relative occupation for the whole year, so the letting exception applies and the rental is **not** a listed suspect trade. Three-in-five test: losses in 4 of the last 5 years, so it is caught on that test, unless s 20A(3) applies.
- With no proof of a reasonable prospect of profit, the R60,000 is ring-fenced: taxable income stays R780,000 and the loss carries forward against future rental profit.

```oa-check
name: YoA 2027 rental loss, taxable income R780,000, loss R60,000, ring-fenced
inputs:
  taxable_income_before_loss: 780000
  threshold_2027: 695800
  rental_loss: 60000
  loss_years_in_last_five: 4
steps:
  - margin_over_threshold: taxable_income_before_loss - threshold_2027
  - taxable_income_if_ring_fenced: taxable_income_before_loss
  - taxable_income_if_not_ring_fenced: taxable_income_before_loss - rental_loss
  - extra_income_taxed: taxable_income_if_ring_fenced - taxable_income_if_not_ring_fenced
expected:
  margin_over_threshold: 84200.00
  taxable_income_if_ring_fenced: 780000.00
  extra_income_taxed: 60000.00
```

### Case 2: decision, sell the loss-making side business before the third loss year or keep it

A person with taxable income of R900,000 before losses runs a photography side business (performing or creative arts is a listed trade, so it would be caught at once if it is "creative arts"; assume instead it is commercial event photography and not listed). It made losses in YoA 2026 and 2027 of R50,000 each. A third loss in YoA 2028 would bring it to 3 of the last 5 years.

- Keep and lose again in 2028: the 2028 loss is ring-fenced (income test met, 3 of 5). Value of the set-off lost against salary at the 41% marginal rate on R50,000: R20,500 of tax deferred, possibly for ever.
- Restructure to profit (or prove s 20A(3) prospects with a business plan and commercial pricing): the 2028 loss stays deductible against salary, saving R20,500 in that year.
- The figure that decides is the expected 2028 loss times the marginal rate, against the cost of the restructuring.

```oa-check
name: Value of keeping a side-business loss outside s 20A, R50,000 at 41%
inputs:
  loss_2028: 50000
  marginal_rate: 0.41
  loss_years_if_lose_again: 3
steps:
  - tax_value_of_set_off: loss_2028 * marginal_rate
expected:
  tax_value_of_set_off: 20500.00
```

## When to refuse or refer

- Trusts and companies: different rules (see `za-corporate-income-tax` for companies).
- A taxpayer relying on s 20A(3) with no records: refer; the escape is evidence-led.
- Farming: whether it is full-time, and the First Schedule, need a farming specialist.
- Losses involving a tax benefit scheme or an avoidance arrangement: refer.

## Filing and payment

The ring-fenced loss is shown on the ITR12 against the trade concerned and carried forward to the same trade's later results. Provisional taxpayers must reflect the ring-fencing in their IRP6 estimates, since a loss that cannot reduce salary-based taxable income does not reduce the provisional tax due (`za-provisional-tax`).

## Completion checklist

- [ ] Income test done on taxable income before any s 20 set-off, using the threshold for the year.
- [ ] Trade classified: listed or not; three-in-five count done for unlisted trades.
- [ ] Letting exception tested on both limbs.
- [ ] s 20A(3) evidence collected, and the six-in-ten bar checked.
- [ ] Ring-fenced loss carried forward against the same trade only.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Taxation Laws Amendment Act 5 of 2026 (GG 54448, 1 April 2026), s 19: read for the amended s 20A(2) opening words (39% marginal rate, before setting off any assessed loss) and s 20A(2)(b)(vi) (farming or animal breeding), effective for years of assessment commencing on or after 1 March 2026 | https://www.sars.gov.za/legal-lprim-aa-2026-03-taxation-laws-amendment-act-5-of-2026-gg-54448-1-april-2026/ | 2026-11-14 |
| SARS, Rates of Tax for Individuals: read for the 39% and 45% band floors for YoA 2023 to 2027 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ | 2026-11-14 |
| SARS Interpretation Note 33 (Issue 6), 4 July 2025: read for para 4.1.1 (company assessed loss limitation, higher of R1 million and 80%, years ending on or after 31 March 2023, and the s 41(4) liquidation carve-out) and s 20(2A) | https://www.sars.gov.za/legal-intr-in-33-assessed-losses-companies-trade-and-income-from-trade-requirements/ | 2026-11-14 |

Not yet confirmed: the s 20A(2)(b) list other than item (vi), the vehicle, aircraft and boat 80% condition, the s 20A(3) factors and the s 20A(4) six-in-ten bar were not reread in the consolidated Income Tax Act today (the Act text did not open by script); they are carried from the earlier version of this file and the general wording of s 20A.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

> Contributed by Brandon Iverach.
