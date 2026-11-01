---
name: bh-payroll-social
description: "Payroll and social insurance in Bahrain, tax year 2026: no income tax withholding on wages, SIO contributions for Bahraini, non-GCC and GCC workers, the expatriate end-of-service contribution of 4.2% and 8.4%, the payment date and late payment charges. Use for questions like SIO contribution rates, GOSI Bahrain, employer contribution Bahrain 2026, or end of service Bahrain."
jurisdiction: BH
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
category: payroll
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Payroll and Social Insurance v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Bahrain and their workers. There is no income tax to withhold from wages. Rates depend on nationality: Bahraini, non-GCC expatriate or GCC national. GCC nationals follow the rules of their home state under the unified extension scheme (Law No. 68 of 2006).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| EOSB, non-Bahraini, private sector, first three years | 4.2% of wages, employer alone | 2026 | https://web.archive.org/web/20250617002539/https://www.sio.gov.bh/en/end-of-service-benefits |
| EOSB, later years | 8.4% of wages, employer alone | 2026 | same |
| EOSB, employed over three years before 1 March 2024 | 8.4% from the start of the Regulation | 2026 | same |
| Payment date | Within the first 15 days of the following month (art. 27) | 2026 | https://web.archive.org/web/20250703061359/https://www.sio.gov.bh/en/law-no-24-of-1976 |
| Late payment interest | 5% of contributions due for each month or fraction | 2026 | same |
| Failure to insure or use real wages | Additional 20% of unpaid contributions (art. 29) | 2026 | same |
| unverified: employer, Bahraini nationals | 18% in 2026 per the prior version (17% in 2025, plus 1 point a year to 21% in 2028); no official text opened | 2026 | unverified |
| unverified: employee, Bahraini nationals | 8% (7% pension, 1% unemployment) per the prior version; art. 33 shows the 7% only | 2026 | unverified |
| unverified: non-GCC expatriate work injury | Employer 3%, employee 1% per the prior version; the law text shows employer 3% only | 2026 | unverified |
| unverified: insurable wage ceiling | BHD 4,000 a month per the prior version | 2026 | unverified |

The SIO English text is an older consolidation. Its art. 33 employer share of 11% is not the current rate.

## The base

Contributions are assessed on total monthly wages (art. 17) and may be fixed on the January wage for the year. Fractions: 50 fils or more round up to 100 fils, less is dropped (art. 26). The employer pays both shares and deducts the worker's share at wage payment; a missed deduction cannot be recovered later (art. 28). EOSB service before the Regulation stays under the Labour Law (Regulation art. 14).

## Deadlines and filing

The employer registers with the SIO on hiring and pays through the SIO employer e-services within the first 15 days of the following month.

## Penalties and interest

See the table. The EOSB Regulation points to arts. 148 and 149 of the Law.

## Cross-border points

GCC nationals: home state rules. A move in or out has no income tax effect (bh-cross-border-tax).

## Two worked examples that recompute

Non-Bahraini in year two on BHD 900: EOSB, employer only.

```oa-check
name: EOSB year two
inputs:
  wage: 900
steps:
  - eosb: wage * 0.042
expected:
  eosb: 37.80
```

Decision: keep or replace a non-Bahraini passing three years on BHD 900? The monthly EOSB cost doubles.

```oa-check
name: EOSB after year three
inputs:
  wage: 900
steps:
  - before: wage * 0.042
  - after: wage * 0.084
  - rise: after - before
expected:
  rise: 37.80
```

## Ask the client first

- Worker's nationality: Bahraini, non-GCC or GCC?
- Gross monthly wage?
- Service start date (before or after 1 March 2024)?
- Which payroll month?

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Insurance Law, Legislative Decree No. 24 of 1976, arts. 17, 26 to 29, 33 (SIO English text, archive copy of 3 Jul 2025; older consolidation, its rates are not current) | https://web.archive.org/web/20250703061359/https://www.sio.gov.bh/en/law-no-24-of-1976 | 2026-11-01 |
| Decision No. 109 of 2023, EOSB Regulation, arts. 5, 13, 14 (SIO, archive copy of 17 Jun 2025) | https://web.archive.org/web/20250617002539/https://www.sio.gov.bh/en/end-of-service-benefits | 2026-11-01 |

Not yet confirmed: every row marked unverified above. SIO returned 403 on 2026-11-01 and no decision setting current rates or the ceiling appeared on the archived SIO pages opened. Also the contribution floor.

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
