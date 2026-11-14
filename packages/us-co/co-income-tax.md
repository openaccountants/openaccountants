---
name: co-income-tax
description: Colorado individual income tax in 2026 for residents, part-year residents, nonresidents and sole traders. Covers the published estimated rate, state modifications, retirement, credits, estimates and clearly labelled 2025 filing mechanics.
version: 0.2
jurisdiction: US-CO
category: state-tax
type: situation-rules
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Colorado individual income tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** 2026 estimated-tax worksheet uses 4.4%. The 2026 deduction-addback limits are lower, overtime deductions are added back, Colorado EITC is 25% of the allowable federal amount and the family affordability credit is unavailable. Final 2026 annual packet/rate and TABOR refund remain unconfirmed. Built from the law; Not yet approved.

## Who this applies to

Full-year residents, part-year residents and nonresidents with Colorado-source income, including sole traders and disregarded LLC owners. [DOR Part 1](https://tax.colorado.gov/individual-income-tax-guide) requires filing if a federal return is required or Colorado liability exists; a refund return can still be appropriate otherwise.

A resident is domiciled in Colorado or maintains a permanent abode there and spends, in aggregate, more than six months there. Domicile persists until changed; temporary absence does not decide it. A domicile move during the year creates part-year issues. Federal filing status carries through, including a joint return when spouses have different residence statuses. Complete federal income in `us-federal-income-tax-return-1040` and business income in `us-schedule-c-and-se-computation`; federal limits/rates remain there.

## Rates, bands and thresholds

| Item | Year and condition | Official source |
|---|---|---|
| Income-tax rate | Published 2026 estimates: 4.4%; final annual rate and any temporary adjustment need confirmation | [2026 DR 0104EP, worksheet](https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf) |
| Prior-year rates | 2024 4.25%; 2025 4.4%, retained for the 2025-2026 filing cycle | [DOR Part 2](https://tax.colorado.gov/individual-income-tax-guide) |
| Low-income tax table | Taxable income below $50,000 uses the year's published table; do not assume straight multiplication is the final return amount | [DOR Part 2](https://tax.colorado.gov/individual-income-tax-guide) |
| QBI add-back | Full deduction when AGI exceeds $500,000 single / $1,000,000 joint; Schedule F exception; SALT Parity owner rule separate | [DOR Part 3; §39-22-104](https://tax.colorado.gov/individual-income-tax-guide) |
| Federal deduction add-back | AGI exceeds $300,000 and deductions exceed the state limit; 2026 limits $1,000 single / $2,000 joint, compared with $12,000/$16,000 in 2023-2025 | [DOR Part 3](https://tax.colorado.gov/individual-income-tax-guide) |
| Overtime / tips | Full federal overtime deduction added back for 2026 and later; no add-back for qualified-tip deduction | [DOR Part 3](https://tax.colorado.gov/individual-income-tax-guide) |
| Colorado EITC | 25% in 2026 and later; 50% in 2025 | [EITC rules; §39-22-123.5](https://tax.colorado.gov/income-tax-topics-earned-income-tax-credit) |
| Family affordability credit | Unavailable for 2026; 2025 rules stay confined to that year | [DOR credit notice](https://tax.colorado.gov/income-tax-topics-family-affordability-tax-credit) |
| Estimated-tax trigger | Expected net tax after withholding/credits exceeds $1,000 | [2026 DR 0104EP](https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf) |
| Required annual estimates | Lesser of 70% current net tax and eligible 100% prior net tax; 110% prior tax when prior federal AGI exceeds $150,000, or $75,000 MFS | [2026 DR 0104EP](https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf) |
| Alternative minimum tax | Tentative Colorado minimum tax 3.47% on the appropriately modified base, then compare normal tax | [DOR Part 2](https://tax.colorado.gov/individual-income-tax-guide) |

## The base

Start with **federal taxable income**, not wages or AGI. Make Colorado additions, subtract permitted modifications, determine regular/alternative tax, allocate for a partial/nonresident year, then apply credits and payments. The [2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf) supplies the available annual mapping, labelled **2025-2026 filing cycle**: DR 0104 line 1 federal taxable income; lines 2-9 additions; line 10 subtotal; line 11 DR 0104AD subtractions; line 12 Colorado taxable income. Final 2026 fields, especially overtime, must be confirmed.

### State modifications

- **State income tax add-back.** [DOR's dedicated rules](https://tax.colorado.gov/income-tax-topics-state-income-tax-addback) cover Schedule A state income tax, including deductible FAMLI premiums, regardless of the state paid. General sales, local income/occupational, real estate and personal property taxes are not automatically added back. Apply both the limited-SALT and itemized-versus-available-standard-deduction limitations. The add-back is the smaller permitted amount, with floors at zero; MFS when either spouse itemizes uses zero available standard deduction for this calculation.
- **Entity-paid taxes.** Partnerships and resident S corporation shareholders add their distributed/pro rata deducted state income taxes without the personal Schedule A limitations. Nonresident S corporation shareholders have a Colorado-tax-specific rule. Reconcile DR 0106K separately; do not erase the personal add-back.
- **QBI.** Under [DOR Part 3](https://tax.colorado.gov/individual-income-tax-guide), the AGI test adds the full deduction, not merely the excess above the threshold. Exactly the threshold does not exceed it. The Schedule F exception is distinct from the SALT Parity rule: an owner of an electing entity adds the full allowed QBI deduction, not only the electing entity's share.
- **Deduction limit.** The high-AGI deduction add-back can apply to standard or itemized deductions. Reconcile the state income tax amount already added back so it is not counted twice; full final 2026 worksheet/field confirmation remains pending.
- **Overtime, tips and business meals.** Add back the claimed federal overtime deduction in 2026 and later, and the full covered federal business-meals deduction for the applicable state years. Tips have no corresponding add-back in DOR's current rules. Overtime remains subject to Colorado withholding; load `co-payroll`. Do not infer conformity of every other federal deduction from these examples.
- **Other additions/subtractions.** Retain non-Colorado state/local bond interest additions; state-tax refunds and eligible U.S. government interest subtractions only to the extent included federally; and the distinct CollegeInvest/ABLE recapture, K-1, conservation-easement and non-Colorado NOL topics. Fannie Mae/Ginnie Mae interest is not treated as a direct government obligation in the 2025 booklet. Charity for non-itemizers, other specialist adjustments and exact fields need the complete applicable-year instructions before use. Sources: [DOR Parts 3-4](https://tax.colorado.gov/individual-income-tax-guide), [Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf).

### Retirement subtractions

Compute each spouse separately; unused cap does not transfer. [DOR retirement rules](https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities) require amounts included in federal taxable income and allocate joint taxable Social Security in proportion to gross benefits.

| Age at year-end | Social Security boundary | Other qualifying pension/annuity cap | Source |
|---|---|---|---|
| 65 or older | Entire federally taxable Social Security | $24,000 reduced by Social Security subtracted, floored at zero | [DOR retirement rules](https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities) |
| 55-64, AGI no more than $75,000 single / $95,000 joint | Entire federally taxable Social Security for 2025 and later | $20,000 reduced by Social Security subtracted, floored at zero | [DOR retirement rules](https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities) |
| 55-64 above those limits | Shared $20,000 cap | Remaining part of the same cap | [DOR retirement rules](https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities) |
| Under 55 | Qualifying death-benefit limitation; no blanket ordinary-retirement exemption | Qualifying death benefits up to $20,000, shared with relevant Social Security | [DOR retirement rules](https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities) |

Qualifying categories include pensions, certain IRA distributions, fully matured purchased annuities and qualifying permanent-disability income. Premature IRA distributions and nonpermanent disability do not automatically qualify. Railroad, military-under-55 and historical PERA/DPS subtractions are separate topics and cannot duplicate the same income. The 2025 booklet has a $15,000 military-under-55 subtraction; final 2026 duration/eligibility and HOH/MFS treatment of the enhanced Social Security AGI test remain unconfirmed here.

### Credits and TABOR

[DOR EITC rules](https://tax.colorado.gov/income-tax-topics-earned-income-tax-credit) allow full-year/part-year residents, not nonresidents. The allowable federal credit normally comes first. DR 0104TN covers qualifying ITIN/no-work-valid-SSN cases and certain childless filers under 25: specified students age 24, ordinary qualifying nonstudents 19-24, qualifying former foster/homeless youth 18-24. All remaining conditions still apply. Claim through DR 0104CR. Part-year EITC uses the income-tax apportionment percentage capped at 100%; excess credit is refundable.

The [family affordability credit](https://tax.colorado.gov/income-tax-topics-family-affordability-tax-credit) is unavailable in 2026. Preserve its 2025 topic: residents, children under 17, income limits and DR 0104CN/CR. Published 2025 limits are $85,000 single and $96,000 joint, with maximum $3,273 under 6 / $2,455 ages 6-16; the full table controls rather than an invented straight-line phaseout. The separate child tax credit is not replaced by this credit's disappearance.

[TABOR mechanisms, SB24-228](https://leg.colorado.gov/bills/sb24-228) use property-tax reimbursement, conditional income-rate reductions, conditional sales/use-rate reductions and a remaining sales-tax refund. The old statutory income-cut schedule remains a topic, not a prediction of the final 2026 rate: remaining revenue >$300m through $500m gives a .04-percentage-point cut, then >$500m-.6bn .07, >$.6-.7bn .09, >$.7-.8bn .11, >$.8-1bn .12, >$1-1.5bn .13 and >$1.5bn .15. The separate sales/use reduction has its own adjusted trigger and .13-point mechanism. Apply the actual announced tax-year rate.

The [sales-tax refund rules](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund) require full-year domicile (or January 1 through death), the age/tax/withholding conditions and the incarceration exclusion. Modified AGI includes excluded Social Security and the applicable non-Colorado bond addition. File/elect the credit by October 15 after the year. A joint return with only one eligible spouse receives the single amount.

| 2025 modified AGI, 2025-2026 filing cycle only | Single refund | Joint refund | Source |
|---|---|---|---|
| $52,000 or less | $19 | $38 | [DOR 2025 table](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund) |
| $52,001-$105,000 | $25 | $50 | [DOR 2025 table](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund) |
| $105,001-$168,000 | $29 | $58 | [DOR 2025 table](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund) |
| $168,001-$233,000 | $35 | $70 | [DOR 2025 table](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund) |
| $233,001-$299,000 | $37 | $74 | [DOR 2025 table](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund) |
| $299,001 or more | $59 | $118 | [DOR 2025 table](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund) |

## Deadlines and filing

[DOR Parts 6-7](https://tax.colorado.gov/individual-income-tax-guide) and the [2026 DR 0104EP](https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf) provide these steps:

1. Select DR 0104 and required PN/AD/CR/TN/CN schedules by actual facts. Use Revenue Online, authorized e-filing or the allowed paper route. Preserve return acceptance and payment confirmation separately.
2. Annual calendar-year return/payment is due April 15 after year-end, with next-business-day adjustment. Automatic six-month filing extension does not extend payment. The 90% timely-payment/extended-filing/balance-with-return conditions govern the specified late-payment waiver.
3. For ordinary estimates, test the $1,000 trigger and eligible current/prior annual payment choices, then ordinarily divide into four quarters: April 15, June 15, September 15 and January 15 of the next year. Prior-tax choice requires a filed full 12-month Colorado year. Follow the required first-listed account and joint-payment identity.
4. Annualized installments require the corresponding federal method. Farmers/fishermen meeting the two-thirds-income test have a 50% current-tax rule, January 15 single installment and March 1 full-file/pay exception; do not apply ordinary-quarter assumptions.
5. Reconcile withholding, carryforwards and payments to the actual tax account. DR 0204 calculates estimate underpayments; the January 31 full-file/pay fourth-quarter exception is distinct from the annual deadline.
6. Federal changes generally require DR 0104X within 180 days of the specified finalization/amended-federal event. Retain the records for the required period; DOR Part 7 states four years after the latest specified return/due/payment event.

The available 2025 form assembly has PN tax carried to line 13 and AD subtotal to line 11; no final 2026 form mapping is represented. The actual 2025 form requires e-filing for more than five dependents. Overseas deadlines and full refund-claim limitation details remain unconfirmed.

## Penalties and interest

[DOR Parts 6-7](https://tax.colorado.gov/individual-income-tax-guide) publish calendar-2026 regular interest 11%, discounted interest 8%, and estimated-tax interest 11%. Discounting depends on payment before/within 30 days of deficiency or the specified timely installment agreement; it is not automatic.

Late payment is the greater of $5 or 5% unpaid tax, plus .5% per month up to 12%, subject to the stated waiver conditions. Count actual late periods and distinguish fraud, negligence, collection and information-return penalties; do not treat the ordinary formula as every assessment. The 2025-2026 filing cycle uses the calendar-year rate applicable while debt was outstanding, not a guessed constant for the return year.

## Cross-border points

[Part-year/nonresident rules](https://tax.colorado.gov/income-tax-topics-part-year-residents-nonresidents) first calculate tax as if full-year, then apply the modified-income apportionment percentage. The computation is not a simple fraction of residence days. Full allocation, ratios above 100%, excluded additions and exact PN lines require the current schedule.

Other-state credits, business apportionment, military elections/spouses/DR 1059, non-Colorado NOL, SALT Parity, AMT, capital gains, conservation easements, enterprise/CHIPS/strategic credits and city occupational privilege taxes remain separate fact-specific topics. City OPT is not a state-income-tax add-back merely because it was deductible federally.

## Two worked examples that recompute

Existing unnamed case topics are retained; all inputs are hypothetical.

**Case 1, 2026 single sole trader.** Federal taxable income $80,000, federal AGI $95,000 and state business-meals add-back $1,200 produce $81,200 Colorado income and $3,572.80 at the published estimated rate. Eligible prior tax is $3,000 on a filed 12-month year; prior AGI $90,000. The smaller annual estimate is $2,500.96, ordinarily $625.24 quarterly. A $750 prior-tax quarter is a different conservative payment choice, not the computed minimum.

```oa-check
name: Colorado sole trader current versus prior estimate
inputs:
  federal_taxable_income: 80000
  meals_addback: 1200
  eligible_prior_tax: 3000
steps:
  colorado_income: federal_taxable_income + meals_addback
  estimated_tax: colorado_income * 0.044
  required_annual: min(estimated_tax * 0.70, eligible_prior_tax)
  quarter: required_annual / 4
expected:
  colorado_income: 81200
  estimated_tax: 3572.80
  required_annual: 2500.96
  quarter: 625.24
```

**Case 2, 2026 joint high earners.** Federal taxable income $1,110,000, AGI $1.2m, QBI $40,000 and deductions $50,000 with no Schedule A state-tax adjustment. Add QBI $40,000 and deductions $48,000. Estimated tax is $52,712. Prior AGI was also above the high-income threshold and eligible prior tax was $45,000, so compare $36,898.40 current option with $49,500 prior option.

```oa-check
name: Colorado joint high income modifications and estimate
inputs:
  federal_taxable_income: 1110000
  qbi_addback: 40000
  federal_deductions: 50000
  eligible_prior_tax: 45000
steps:
  deduction_addback: max(0, federal_deductions - 2000)
  colorado_income: federal_taxable_income + qbi_addback + deduction_addback
  estimated_tax: colorado_income * 0.044
  current_option: estimated_tax * 0.70
  prior_option: eligible_prior_tax * 1.10
  required_annual: min(current_option, prior_option)
expected:
  deduction_addback: 48000
  colorado_income: 1198000
  estimated_tax: 52712
  current_option: 36898.40
  prior_option: 49500
  required_annual: 36898.40
```

**Case 3, 2025-2026 filing cycle, retirees 67 and 63.** Joint AGI $110,000, taxable income $80,000; spouse A taxable Social Security $18,000 and pension $30,000; B taxable Social Security $22,000; excluded Social Security $12,000. A subtracts $18,000 plus $6,000 pension; B is above the joint AGI limit and subtracts $20,000. Total $44,000 gives $36,000 taxable income. The verified [2025 Book 104 tax-table row](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf) uses an "Over / But not over" heading: exactly $36,000 belongs in the $35,900-$36,000 row, giving $1,582 (the old $1,586 used the next row); the 2025 modified-AGI refund table gives $58 jointly if both qualify. Neither table is labelled 2026.

```oa-check
name: Colorado legacy retirement case 2025 only
inputs:
  federal_taxable_income: 80000
  a_taxable_ss: 18000
  a_pension: 30000
  b_taxable_ss: 22000
steps:
  a_pension_subtraction: min(a_pension, max(0, 24000 - a_taxable_ss))
  b_ss_subtraction: min(b_taxable_ss, 20000)
  total_subtractions: a_taxable_ss + a_pension_subtraction + b_ss_subtraction
  colorado_income: federal_taxable_income - total_subtractions
  table_tax: 1582
  joint_sales_refund: 58
expected:
  a_pension_subtraction: 6000
  b_ss_subtraction: 20000
  total_subtractions: 44000
  colorado_income: 36000
  table_tax: 1582
  joint_sales_refund: 58
```

**Case 4, 2025-2026 filing cycle, July 1 arrival.** Reconciled taxable income $90,000, modified Colorado AGI $52,500 and modified federal AGI $105,000. Assumed correctly completed PN ratio is 50%; tax is $1,980. No full-year TABOR refund. This preserves the allocation example without assuming residence days alone create the ratio.

```oa-check
name: Colorado legacy part year income ratio
inputs:
  taxable_income: 90000
  modified_colorado_agi: 52500
  modified_federal_agi: 105000
steps:
  ratio: modified_colorado_agi / modified_federal_agi
  full_year_tax: taxable_income * 0.044
  apportioned_tax: full_year_tax * ratio
expected:
  ratio: 0.5
  full_year_tax: 3960
  apportioned_tax: 1980
```

**Case 5, credit year decision.** Head-of-household resident, child age 4, AGI $28,000 and allowable federal EITC $4,000. State EITC is $2,000 for 2025 versus $1,000 for 2026; 2026 FATC is unavailable. The actual 2025 DR 0104CN grid confirms $2,598 FATC for the $25,001-$30,000 HOH AGI band and a child under 6. Its separate regular child credit is $600 for this AGI, giving $3,198 combined Colorado child credits in 2025, distinct from EITC. Do not carry either 2025 child-credit grid into 2026 without its own form.

```oa-check
name: Colorado EITC credit year comparison
inputs:
  allowable_federal_eitc: 4000
steps:
  state_2025: allowable_federal_eitc * 0.50
  state_2026: allowable_federal_eitc * 0.25
  reduction: state_2025 - state_2026
  legacy_child_credits: 2598 + 600
expected:
  state_2025: 2000
  state_2026: 1000
  reduction: 1000
  legacy_child_credits: 3198
```

**Threshold decision.** Exactly $300,000 AGI does not trigger the deduction add-back; above it the full excess deduction over the applicable limit matters. Exactly the QBI AGI threshold does not trigger that test, while an electing SALT Parity entity can independently require it. A farmer's Schedule F exception does not erase a separate K-1 obligation.

## Ask the client first

- What tax year, federal status, domicile/move dates, abode and Colorado days apply to each spouse?
- What federal taxable income/AGI, deductions, Schedule C/F and DR 0106K facts exist?
- What ages, taxable/gross retirement benefits and distribution types apply separately?
- What children, allowable federal credits, SSN/ITIN and residency facts support credits?
- What prior filed-year tax/AGI, withholding, estimates, dates, carryforwards and notices exist?
- What other-state/local taxes, business allocation, military or specialist issues exist?

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| DOR individual rules | https://tax.colorado.gov/individual-income-tax-guide | Read for residence, rate/table boundary, additions, annual estimate rules, filing, amendments and calendar-year interest/penalties; not every specialist adjustment | 2026-11-13 |
| 2026 DR 0104EP | https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf | Read for 4.4% estimate worksheet, trigger, current/prior/farmer choices, payment dates, rounding and account identity | 2026-11-13 |
| 2025 Book 104 | https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf | Read for published year, actual 2025 form pages 1-8/base mapping, dependent e-filing, retirement instructions, exact $36,000 table boundary and discontinued use-tax form; final 2026 mapping not established | 2026-11-13 |
| State income tax add-back | https://tax.colorado.gov/income-tax-topics-state-income-tax-addback | Read for personal limitations, FAMLI treatment, K-1 taxes and resident/nonresident shareholder distinction | 2026-11-13 |
| Retirement rules | https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities | Read for ages/caps, joint allocation, enhanced Social Security test and pension interactions | 2026-11-13 |
| EITC rules | https://tax.colorado.gov/income-tax-topics-earned-income-tax-credit | Read for 2025/2026 percentages, resident/ITIN/younger-filer conditions, refundability and part-year cap | 2026-11-13 |
| Family affordability credit | https://tax.colorado.gov/income-tax-topics-family-affordability-tax-credit | Read for explicit 2026 unavailability and legacy 2025 eligibility/limits; phaseout grid separately read in DR 0104CN | 2026-11-13 |
| DOR 2025 DR 0104CN, 2025-2026 filing cycle | https://tax.colorado.gov/sites/default/files/documents/DR_0104CN_2025.pdf | Read for all eligibility, regular-child-credit and FATC grids, exact case band, zero boundary and PN cap on pages 1-4 | 2026-11-13 |
| TABOR | https://tax.colorado.gov/TABOR | Read for year-dependent refund/election; no final 2026 amount confirmed | 2026-11-13 |
| State sales-tax refund | https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund | Read for domicile, age/incarceration, modified AGI, all 2025 table rows and filing deadline | 2026-11-13 |
| SB24-228 enacted summary | https://leg.colorado.gov/bills/sb24-228 | Read for conditional mechanism order, rate-cut schedule and distinct sales-rate trigger | 2026-11-13 |
| Part-year/nonresident rules | https://tax.colorado.gov/income-tax-topics-part-year-residents-nonresidents | Read for residence, federal status, full-year-first computation and modified-income allocation; full final schedule pending | 2026-11-13 |

Not yet confirmed: final annual 2026 DR 0104/AD/PN/CR/CN fields, final rate/TABOR refund and any later change; complete deduction worksheet and other federal-conformity changes; HOH/MFS enhanced Social Security limits, military/PERA/DPS duration/details, charitable subtraction and specialist credits/adjustments; full PN ratios/line exclusions, overseas deadlines and refund-claim limitations. Existing bill-history claims, the 305-day military election and protest procedure require their specific current sources before use; they are not silently certified by this rebuild.
