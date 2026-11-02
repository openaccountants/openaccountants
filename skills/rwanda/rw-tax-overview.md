---
name: rw-tax-overview
description: "Rwanda tax system at a glance for 2026: RRA, the income tax, VAT and procedure laws, headline rates and deadlines, and what changed in 2025 and 2026."
version: 0.2
jurisdiction: RW
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda Tax Overview

## Who this applies to

Anyone needing the map. Details sit in the linked skills.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Top personal rate | 30% | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/calculate-paye |
| Corporate rate | 28% | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf |
| VAT | 18% | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/value-added-tax/penalties-and-interest |
| Capital gains | 10% | 2026 | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b |
| Digital services tax | 1.5%, needs a ministerial order | 2026 | same |
| Tax period | Calendar year | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| Environmental levy on imports in plastic | 0.2% of customs value basis, from 1 July 2025 | 2026 | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b |

## The base

Residents on worldwide income, non-residents on Rwanda source (art 12). Authority: Rwanda Revenue Authority. Currency: Rwandan franc. Laws: 027/2022 (income), 049/2023 (VAT), 020/2023 (procedures), and amendments of 2023 and 2025. 2026 additions: Orders 003 and 004 of April, 006 to 009 of September. Skills: [income tax](rwanda-income-tax.md), [company tax](rw-corporate-income-tax.md), [VAT](rwanda-vat.md), [payroll](rwanda-payroll.md), [RSSB](rwanda-social-contributions.md), [formation](rw-company-formation.md).

## Deadlines and filing

Annual income tax: 31 March. PAYE, VAT, withholding: 15 days after the period. Portals: https://etax.rra.gov.rw and www.ishema.rssb.rw.

## Penalties and interest

See [rw-corporate-income-tax](rw-corporate-income-tax.md).

## Cross-border points

See [rw-corporate-income-tax](rw-corporate-income-tax.md).

## Two worked examples that recompute

```oa-check
name: Company tax on FRW 10,000,000
inputs:
  profit: 10000000
steps:
  - tax: profit * 0.28
expected:
  tax: 2800000.00
```

**Decision.** Same profit through a company then a 15% dividend to a resident individual, against the real regime, is worked from the two skills.

```oa-check
name: VAT on FRW 1,000,000
inputs:
  price: 1000000
steps:
  - vat: price * 0.18
expected:
  vat: 180000.00
```

## Ask the client first

1. Individual or company?
2. Resident?
3. Turnover?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 027/2022 establishing taxes on income (read: arts 3-5, 8-10, 12-21, 24-33, 36-38, 44-50, 56-69) | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf | 2026-11-01 |
| Law 051/2023 amending the income tax law (whole) | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf | 2026-11-01 |
| Official Gazette Special of 29/05/2025: Law 009/2025 (VAT), Law 014/2025 (income tax) (whole of both) | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b | 2026-11-01 |
| RRA, Declare VAT page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/value-added-tax/penalties-and-interest | 2026-11-01 |
| RRA, Calculate PAYE page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/calculate-paye | 2026-11-01 |

Not yet confirmed: the old note of a medium-term 20% corporate target and the "2025-2030 reform package" had no official source and were removed from the body.

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
