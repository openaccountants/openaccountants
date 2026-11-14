---
name: sd-bank-franchise-tax
description: "Determine South Dakota 2026 financial-institution bank franchise tax, separate from the absence of ordinary corporate income tax. Compute graduated rates and minimum after state base and apportionment; identify state return and extension duties. Trigger on South Dakota bank franchise, financial institution income tax, lender and bank tax minimum."
version: "0.1"
jurisdiction: US-SD
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: income-tax
type: computation
---

# South Dakota bank franchise tax, 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** South Dakota has no ordinary corporate income tax, but covered financial institutions pay bank franchise tax on state-assignable net income. The ordinary schedule starts at 6% and declines marginally for very large income, subject to a USD 200 minimum. An S election or LLC form does not automatically exempt a financial institution. [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html); [10-43-10.1](https://sdlegislature.gov/api/Statutes/10-43-10.1.html).

## Scope

Ordinary financial-institution bank franchise tax under chapter 10-43, including definition, state adjustments, ordinary three-factor apportionment, rates/minimum and filing. This is not a general tax on all corporations' gross receipts. Trust-company and extended-term-trust special taxes, complicated related groups and specialized credit-card sourcing require separate analysis. Federal corporate computations belong to `us-form-1120-c-corp`.

## Ask the client first

1. Institution/legal classification, licenses, lending/deposit/trust activity, locations and exemptions.
2. Federal classification/year end, taxable income and detailed state adjustment records.
3. South Dakota/everywhere property, payroll and financial receipts with borrower and activity sourcing.
4. Related corporations, consolidation history and apportionment elections/determinations.
5. State loss vintages, federal taxes/imputed tax calculation, credits, payments and extension records.

## The method, step by step

### Rates, bands and thresholds

Rates are **marginal bands**, not a lower rate applied to the institution's entire income after crossing a threshold.

| South Dakota assignable net income, USD | Marginal rate / minimum | Official source |
| --- | --- | --- |
| First 400 million |6% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Over 400 million through 425 million |5% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Over 425 million through 450 million |4% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Over 450 million through 475 million |3% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Over 475 million through 500 million |2% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Over 500 million through 600 million |1% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Over 600 million through 1.2 billion |0.5% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Over 1.2 billion |0.25% | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| Minimum ordinary tax payable | USD 200 | [10-43-4](https://sdlegislature.gov/api/Statutes/10-43-4.html) |
| State NOL carryforward, losses incurred from 2015 | Seven following tax years; no carryback; statutory floor/adjustment order applies | [10-43-10.4](https://sdlegislature.gov/api/Statutes/10-43-10.4.html); [10.5](https://sdlegislature.gov/api/Statutes/10-43-10.5.html) |

1. Establish financial-institution status under 10-43-1 and the doing-business/license trigger in 10-43-2. The definition includes banks, savings/loan/trust companies, licensed lenders and specified loan/debt businesses, with material incidental seller/related-party exceptions. Money transmission alone does not prove bank franchise tax. Check explicit statutory exemptions rather than assuming every finance business qualifies.
2. Under 10-43-10.1, begin with federal-based net income as modified by state law. A financial institution electing S status computes as if the election had not been made; an LLC is treated as a separate corporation for this chapter. This differs from ordinary federal pass-through treatment.
3. Current 10-43-10.2 adds otherwise excluded state/local-obligation income, deducted state income-based taxes, qualifying federal-tax refunds, deducted dividends and specified liquidation losses. Current 10-43-10.3 subtracts qualifying taxed-financial-institution dividends, deductible federal taxes subject to exclusions, specified interest expense, liquidation gains and eligible imputed federal tax for S institutions/LLCs. Reconcile actual state-law categories; do not subtract a guessed federal amount.
4. The current codified text reflects 2026 chapter 51/SB 18 repealing special bad-debt modifications. Do not carry obsolete bad-debt addbacks/recoveries/method adjustments forward from an older form. Current 10-1-47 references the IRC as amended through January 1, 2026; SB 18's isolated act text still displayed January 1, 2025, but other 2026 enactments are reflected in the compiled statute. Use the complete current code and establish the effective-year treatment before filing a straddling period.
5. For multistate institutions, 10-43-22.1 uses the average of property, payroll and receipts factors. Financial receipt sourcing has detailed loan, fee, securities and affiliate rules in neighboring provisions; an ordinary retail destination rule is insufficient. Resolve the factor schedules before applying the rates. Related corporations may petition or be required to consolidate under 10-43-36.
6. Maintain state loss-vintage schedules under 10-43-10.4/.5, apply the state base/apportionment and deductions in the prescribed order, then calculate marginal band tax and compare to the minimum. Reconcile special trust/additional regimes before finalizing the ordinary result.

## Boundary and exception table

| Facts | Decision |
| --- | --- |
| Ordinary nonfinancial corporation | No general South Dakota corporate income tax; this bank skill does not create one |
| Financial institution elects S status or LLC form | State chapter retains a corporate computation; do not assume zero tax |
| Taxable institution with zero/low net income | USD 200 ordinary minimum can apply |
| Trust company/extended-term trust | Separate 10-43-88 through 92 rules; do not apply ordinary minimum automatically |
| Multistate lender/credit-card institution | Detailed statutory financial receipt sourcing and special classifications required |
| State/nonprofit development entity | Test 10-43-94 and other specific exemption conditions |

## Worked cases

**Case 1.** An invented ordinary covered institution has final South Dakota assignable net income USD 100,000 after all state adjustments/apportionment and no special credits. 6% gives USD 6,000, greater than USD 200 minimum.

```oa-check
name: South Dakota ordinary bank franchise tax
inputs:
  assignable_income: 100000
  minimum: 200
steps:
  - ordinary: assignable_income * 0.06
  - tax: max(ordinary, minimum)
expected:
  ordinary: 6000
  tax: 6000
```

**Case 2, minimum decision.** An invented ordinary taxable institution has final assignable income USD 1,000. Ordinary 6% tax is USD 60, so the USD 200 minimum controls. The example assumes no special trust regime/exemption.

```oa-check
name: South Dakota financial-institution minimum boundary
inputs:
  assignable_income: 1000
  minimum: 200
steps:
  - ordinary: assignable_income * 0.06
  - tax: max(ordinary, minimum)
expected:
  ordinary: 60
  tax: 200
```

## When to refuse or refer

Refer disputed institution status, statutory exemptions, trust/credit-card special rules, complex financial receipt sourcing, related consolidation, imputed federal tax, bad-debt transitions and historical losses. Do not mark a multistate return complete using an unsupported single percentage or treat the absence of ordinary corporate income tax as an exemption.

## Filing and payment

Use DOR's bank franchise tax Filing and Payment link, register/activate the institution account, select the tax year, reconcile the state return to federal income and adjustment/factor schedules, submit with required attachments, retain acceptance and separately verify payment posting. Final 2026 return field mapping has not been read, so no line-number filing instructions are claimed.

Under 10-43-30, annual return and tax are due **within 15 days after the federal income-tax return is due**. Under 10-43-30.1, an extension no later than six months from the original state date requires a federal extension, its copy filed with DOR by the original state date, and a reasonable estimated payment then. DOR requests a cover letter plus federal extension copy directly to its bank-franchise unit, not its tax portal. A qualifying reasonable estimate shortfall accrues interest under the statute; the filing extension is not permission to pay nothing.

Late return/payment invokes 10-59-6: ordinary late filing is 10% or USD 10 minimum after its statutory trigger, ordinary interest 1% per month/part with USD 5 first-month minimum; intentional delay has separate conditions/rate. Apply the full statute and current notice. Do not substitute unemployment contribution penalties.

## Completion checklist

- Covered financial institution and ordinary/special regime identified.
- Current state modifications and applicable 2026 timing reconciled.
- Federal/imputed tax, loss vintages and financial factors supported.
- Marginal schedule and minimum compared.
- Return/extension evidence, payment, portal acceptance and final-year form checked.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR bank franchise page. Read for institution filing, portal and direct extension workflow/minimum. | https://dor.sd.gov/businesses/taxes/bank-franchise-tax/ | 2026-11-13 |
| SDCL 10-43-1 and 2. Read for full definition, incidental-loan exceptions and business/license trigger. | https://sdlegislature.gov/api/Statutes/10-43-1.html and https://sdlegislature.gov/api/Statutes/10-43-2.html | 2026-11-13 |
| SDCL 10-43-4. Read for all marginal bands and USD 200 minimum. | https://sdlegislature.gov/api/Statutes/10-43-4.html | 2026-11-13 |
| SDCL 10-43-10.1. Read for federal-based net income and S/LLC treatment. | https://sdlegislature.gov/api/Statutes/10-43-10.1.html | 2026-11-13 |
| SDCL 10-43-10.2/.3. Read for current additions/subtractions after bad-debt repeal. | https://sdlegislature.gov/api/Statutes/10-43-10.2.html and https://sdlegislature.gov/api/Statutes/10-43-10.3.html | 2026-11-13 |
| SDCL 10-1-47. Read for compiled January 1, 2026 IRC conformity date. | https://sdlegislature.gov/api/Statutes/10-1-47.html | 2026-11-13 |
| 2026 chapter 51, SB 18. Read for repeal of special bank bad-debt modifications and source-text distinction. | https://mylrc.sdlegislature.gov/api/Documents/SessionLaw/301408.pdf?Year=2026 | 2026-11-13 |
| SDCL 10-43-10.4/.5. Read for no NOL carryback, seven-year carryforward and ordering restriction. | https://sdlegislature.gov/api/Statutes/10-43-10.4.html and https://sdlegislature.gov/api/Statutes/10-43-10.5.html | 2026-11-13 |
| SDCL 10-43-22.1 and 36. Read for three-factor apportionment and related consolidation. | https://sdlegislature.gov/api/Statutes/10-43-22.1.html and https://sdlegislature.gov/api/Statutes/10-43-36.html | 2026-11-13 |
| SDCL 10-43-30/.1. Read for fifteen-day-after-federal due date and extension/payment conditions. | https://sdlegislature.gov/api/Statutes/10-43-30.html and https://sdlegislature.gov/api/Statutes/10-43-30.1.html | 2026-11-13 |
| SDCL 10-43-94. Read for specific exempt development/public entities. | https://sdlegislature.gov/api/Statutes/10-43-94.html | 2026-11-13 |
| DOR financial institutions facts. Read for broad financial businesses, money transmitter distinction and sales/use overlap. | https://dor.sd.gov/media/q34fhrne/financial-institutions.pdf | 2026-11-13 |
| SDCL 10-59-6. Read for business tax late filing/interest trigger and minimums. | https://sdlegislature.gov/api/Statutes/10-59-6.html | 2026-11-13 |

Not yet confirmed: final 2026 state return fields; complete financial receipts sourcing and group schedules; effective-year bad-debt transition for pre-effective/straddling periods; specialized trust/credit-card regimes, imputed federal tax and detailed loss/credit computation. This partial ordinary bank-franchise skill is not a complete specialist financial-institution return.
