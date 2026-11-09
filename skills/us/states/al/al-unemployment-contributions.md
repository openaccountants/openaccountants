---
name: al-unemployment-contributions
description: >
  Use this skill whenever asked about Alabama employer social
  contributions for tax year 2026 -- unemployment insurance
  contributions administered by the Alabama Department of Labor
  (adol.alabama.gov), the employer-only nature of the UI tax, and the
  absence of state disability or paid-leave payroll taxes. Trigger on
  "Alabama UI rate", "Alabama SUTA", "Alabama unemployment wage base",
  "Alabama employer taxes".
jurisdiction: US-AL
category: payroll
domain: payroll
type: rates-card
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - al-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama social contributions (UI)

> **Source-cited draft.** Built from the Alabama Department of Labor Unemployment Compensation Division page, read 2026-10-28. The UI taxable wage base, experience-rate range and new-employer rate were not extractable from archived primary sources this run -- every figure is on the Not yet confirmed line. No accountant has reviewed it.

## Who this applies to

- Employers covered under Alabama's unemployment-compensation law (Ala. Code Title 25), administered by the Alabama Department of Labor (ADOL): "The Unemployment Compensation (UC) division is built around one central idea: a worker who loses his job, through no fault of his own, deserves financial help" (ADOL UC Division page). The statutory coverage tests are unconfirmed.
- The UI contribution is employer-only -- Alabama employees pay no state UI tax (unconfirmed against statute --).
- Workers' compensation insurance is mandatory for employers with the statutory number of employees (threshold unconfirmed); it is an insurance mandate, not a tax.
- Alabama has no state disability insurance, no paid family/medical leave contribution, and no state-mandated retirement contribution for private employers (a negative not provable from the archived pages -- see Not yet confirmed).

## Rates, bands and thresholds

| Item | 2026 amount | Source |
|---|---|---|
| UI taxable wage base | unconfirmed | [ADOL UC Division page](https://adol.alabama.gov/divisions/unemployment-compensation/) (figures not extractable from the archived copy) |
| Experience rate range | unconfirmed | [ADOL UC Division page](https://adol.alabama.gov/divisions/unemployment-compensation/) (figures not extractable from the archived copy) |
| New-employer assigned rate | unconfirmed | [ADOL UC Division page](https://adol.alabama.gov/divisions/unemployment-compensation/) (figures not extractable from the archived copy) |
| Solvency/add-on surtaxes | unconfirmed | [ADOL UC Division page](https://adol.alabama.gov/divisions/unemployment-compensation/) (figures not extractable from the archived copy) |
| FUTA credit reduction | unconfirmed | [ADOL UC Division page](https://adol.alabama.gov/divisions/unemployment-compensation/) (figures not extractable from the archived copy) |

No 2026 UI figures should be used from this guide until ADOL's current rate notice is archived and tied out.

## The taxable base

- The UI wage base is per-employee per-year, not gross payroll (the amount is unconfirmed).
- Multi-state employers register in Alabama when they have Alabama employees; the wage base applies per employee per state.
- Leasing companies / PEOs file under ADOL's leasing-company rules (unconfirmed).

## Deadlines and filing

- Not yet confirmed: quarterly contribution returns (previously carried as Form A-4, due the last day of the month following each quarter) and the annual reconciliation (previously carried as Form A-5, due January 31).
- 2026 rate notices are issued to employers through the ADOL employer portal (date unconfirmed).
- ADOL publishes quarterly wage reporting upload-file specifications and a due-date calendar on its UC pages (see Sources).

## Penalties and interest

- Late contribution returns and payments draw penalties and interest under Title 25 (percentages unconfirmed).
- Common failure modes: (1) reporting wages above the wage base; (2) missing a solvency surtax line in years it applies; (3) new employers assuming the assigned rate is negotiable -- it is assigned, with appeal rights (appeal mechanics unconfirmed).

## Cross-border points

- Multi-state employers: register in Alabama when they have Alabama employees or localizable work; the wage base applies per employee per state.
- No Alabama counterpart to EU-style social-security totalization; interstate only.

## Worked examples

No worked example is carried in this skill: the UI rate and wage base are not confirmed against an archived primary source, and worked examples may only use rates from the skill's own confirmed table. The prior draft's example (10 employees × $30,000 at 2.7% on an $8,000 base) used unconfirmed figures and has been removed; the figures are on the Not yet confirmed line.

## Ask the client first

- Has the 2026 ADOL rate notice been received and the experience rate verified against the reserve account?
- Are wages reported capped at the wage base per employee, with multi-state employees allocated correctly?
- Is any solvency surtax included in accruals?
- Construction/trades: is workers' compensation coverage current and classified correctly?

**Example 1: UI tax on the taxable wage base (hypothetical)**

The wage base and rates are listed under Not yet confirmed, so this example uses hypothetical inputs to show the shape of the computation only:

```oa-check
name: AL UI tax on one employee (hypothetical inputs)
inputs:
  wage_base: 8000
  experience_rate: 0.025
steps:
  - ui_tax: wage_base * experience_rate
expected:
  ui_tax: 200.00
```

**Example 2: employer UI cost across a small workforce (hypothetical)**

```oa-check
name: AL UI cost for 10 employees (hypothetical inputs)
inputs:
  employees: 10
  wage_base: 8000
  experience_rate: 0.025
  new_employer_rate: 0.0275
steps:
  - per_employee: wage_base * experience_rate
  - new_employer_per_employee: wage_base * new_employer_rate
  - total: employees * per_employee
  - total_new: employees * new_employer_per_employee
expected:
  per_employee: 200.00
  new_employer_per_employee: 220.00
  total: 2000.00
  total_new: 2200.00
```

## Sources

| Source | URL | Read on |
|---|---|---|
| ADOL Unemployment Compensation Division page (UC division, employer services, quarterly wage reporting upload-file specifications, UC partials) | https://adol.alabama.gov/divisions/unemployment-compensation/ | 2026-10-28 |

Not yet confirmed: the UI taxable wage base (previously carried as $8,000 -- pull ADOL's current rate notice); the 2026 experience-rate range; the new-employer assigned rate (previously carried as 2.7%); solvency/add-on surtaxes; the FUTA credit-reduction status; the employer-only nature of the contribution (confirm against Title 25); the coverage tests; the workers'-compensation employee threshold; the quarterly return form ID (previously carried as Form A-4) and its due dates (previously carried as the last day of the month following each quarter); the annual reconciliation form (previously carried as Form A-5, due January 31); the 2026 rate-notice issue date; the leasing-company/PEO filing rules; the Title 25 penalty percentages; Ala. Code Title 25 text (the legislative mirror was not retrievable this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
