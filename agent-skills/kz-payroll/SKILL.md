---
name: kz-payroll
description: "Kazakhstan 2026 employee withholding: statutory deductions, annual progressive PIT, monthly computation and employer reporting."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kz-payroll"
  jurisdiction: "KZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Kazakhstan payroll and salary withholding v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Employers computing resident ordinary salary payroll for 2026. Confirm the worker’s actual status, residence, tax-agent deduction application, contribution exemptions and employer regime first. A registered ИП invoice does not by itself resolve disguised-employment risk. Non-residents, exempt personnel, special unified-payment elections and treaty coverage require separate treatment. Use `kz-social-contributions` for contribution rates, caps and employer-type distinctions; use `kz-income-tax` for annual income schedules.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Resident salary ИПН | Cumulative annual taxable salary through 8,500 МРП at 10%, excess at 15%; deduct tax already calculated year-to-date (arts. 363 and 441) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Basic deduction | 30 МРП monthly, annual maximum 360 МРП; only at 1 tax agent on application (arts. 403 and 437) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Pension and health deductions | Actual qualifying employee contributions reduce the ИПН base before the basic deduction (arts. 401–402, 438–439) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Employer social tax | Use the legal-entity base/exclusions or fixed ИП-per-person method, as applicable; no СО offset in 2026 (arts. 555–558) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Computation order:

1. Reconcile contractual gross pay, taxable benefits, non-income items and exemptions. Preserve source documents and payroll period.
2. Calculate employee ОПВ and ВОСМС under their individual caps/exemptions using `kz-social-contributions`; these are withheld, not employer costs.
3. Subtract the qualifying social payments, other statutory reductions and the valid basic/social deductions to obtain taxable salary (arts. 438–439). Do not use the obsolete 14-МРП or 1-МЗП basic deduction. The basic deduction is not duplicated at a second employer. Unused monthly basic deduction does not carry to later payroll months; art. 409 self-assessment is a separate route.
4. Apply art. 441 to cumulative taxable salary since the start of the year. Subtract ИПН already calculated for earlier months. Do not treat each month as a fresh annual bracket or ignore the higher bracket late in the year.
5. Net salary is gross payable less employee deductions and ИПН. Separately compute employer-funded ОПВР, СО, employer ОСМС and any social tax due. General-regime legal-entity social tax uses statutory exclusions, not gross salary; an ИП uses the fixed method; special regimes can be social-tax exempt.
6. Reconcile gross-to-net, employer cost, payment instructions and contribution funds. A combined percentage cannot replace these components.

## Deadlines and filing

ИПН is calculated at accrual and withheld no later than payment; remit within 25 calendar days after the end of the payment month (art. 440). Monthly tax calculations and quarterly reporting are different: arts. 444–445 require the ordinary salary/social-tax declaration by the 15th of the second month following the quarter. Select the current Form 200.00 and employee appendix; populate individual income, qualifying reductions, deductions, calculated/withheld tax and contribution components from the reconciled ledger. Contribution due dates are in `kz-social-contributions`. File in the taxpayer cabinet, check acceptance rather than only upload success, retain the declaration receipt and reconcile payment/fund allocations. Do not rely on a historical form’s box labels.

## Penalties and interest

Late remittance, late declaration and inaccurate reporting require separate current-law assessment; no penalty is calculated from an approximate payroll load.

## Cross-border points

Do not apply resident deductions or contribution coverage automatically to non-residents/EAEU workers. Use arts. 682 and 692 and the applicable agreement after status review. A worker supplied by a foreign entity is a separate tax-agent case. Contractor-versus-employee classification follows actual facts, not a presumed exemption from registration alone.

## Two worked examples that recompute

Case 1: hypothetical eligible main-job salary is KZT 500,000, employee ОПВ KZT 50,000, ВОСМС KZT 10,000, and valid basic deduction KZT 129,750 derived from the index in `kz-tax-overview`. There are no additional deductions and cumulative taxable income stays in the lower bracket. Base is KZT 310,250, ИПН KZT 31,025 and net KZT 408,975. This corrects the old KZT 404,500 result based on a 1-МЗП deduction.

```oa-check
name: Resident salary gross to net
inputs:
  gross: 500000
  opv: 50000
  health: 10000
  basic: 129750
steps:
  - base: max(gross - opv - health - basic, 0)
  - pit: base * 0.10
  - net: gross - opv - health - pit
expected:
  base: 310250
  pit: 31025
  net: 408975
```

Case 2: cumulative taxable salary before this month is a hypothetical 8,400 МРП, previous ИПН 840 МРП, and this month taxable salary is 300 МРП. Cumulative tax at 8,700 МРП is 880 МРП, so this month’s tax is 40 МРП. Treating the month wholly at the lower rate would give 30 МРП and understate withholding by 10 МРП.

```oa-check
name: Annual salary bracket crossing
inputs:
  prior_taxable: 8400
  current_taxable: 300
  prior_tax: 840
steps:
  - cumulative: prior_taxable + current_taxable
  - cumulative_tax: min(cumulative, 8500) * 0.10 + max(cumulative - 8500, 0) * 0.15
  - current_tax: cumulative_tax - prior_tax
  - flat_month: current_taxable * 0.10
  - shortfall: current_tax - flat_month
expected:
  cumulative_tax: 880
  current_tax: 40
  shortfall: 10
```

## Ask the client first

- Employer form and regime, worker residence and actual employment relationship?
- Gross pay, benefits, exclusions, accrual/payment dates and year-to-date taxable salary/tax?
- Deduction application, other tax agent, prior-employer certificate and eligibility documents?
- Contribution exemptions, birth date, other payers and payment history?
- Current reporting form, accepted prior returns and payroll reconciliation?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 363, 401–403, 409, 437–445, 555–558, 682 and 692 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for KGD monthly basic-deduction no-carry clarification | https://www.gov.kz/org/kgd-sko/press/news/details/1323425?lang=ru | 2026-11-14 |

Not yet confirmed: Exact current electronic declaration boxes, special unified-payment and foreign-worker calculations, numeric penalties. The old approximate employer rates, 1-МЗП/14-МРП deduction and social-tax offset are superseded; all contribution components are now sourced in kz-social-contributions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kz-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kz-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
