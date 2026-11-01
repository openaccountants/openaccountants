---
name: lb-tax-overview
description: "Tax overview for Lebanon, tax year 2026: main taxes and where each is covered. Sources and unverified rows are marked per row."
version: 1.1
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lebanon Tax Overview

Lebanon operates a schedular tax system administered by the Ministry of Finance, with separate taxes on corporate profits, employment income, business income, and movable capital. Taxation rests on a principle of territoriality: profit is taxable if it arises from an effort or activity exerted in Lebanon.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard corporate tax | 17% | 2026 | https://www.investinlebanon.gov.lb/en/doing_business/tax_system |
| Withholding on dividends | 10% | 2026 | same |
| VAT return deadline | one month instead of 20 days | 2026 | https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf |
| Tax year | Calendar year (1 January to 31 December) (Companies may request approval to use a different accounting year) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959) |
| Currency | Lebanese pound (LBP / LL) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened |
| Tax authority | Ministry of Finance : Directorate General of Taxation (approx : confirm exact directorate name) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Ministry of Finance |
| Basis of taxation | Territorial : income taxed if generated through activity exerted in Lebanon | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959) |
| Standard corporate income tax rate | 17% | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959) |
| Top personal/payroll tax rate | 25% (Progressive payroll rates run 2% to 25%; business income 4% to 25%) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959) |
| Does VAT exist? / Standard VAT rate | Yes : standard VAT rate 11% | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; VAT Law (Law No. 379 of 2001) |
| Withholding tax on dividends | 10% | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Tax on Movable Capital (Decree-Law No. 146 of 1959) |
| Corporate tax return filing deadline | 31 March (entities) / 31 May (capital companies) of the following year | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959) |
| Structure of income taxation | Schedular : separate taxes on business profits, salaries, and movable capital income | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959) |

## Two worked examples that recompute

Corporate tax at 17% on LL 500,000,000, then 10% withholding on a full distribution of the balance. VAT on a sale uses the [VAT skill](lebanon-vat.md).

```oa-check
name: Corporate tax
inputs:
  profit: 500000000
steps:
  - tax: profit * 0.17
expected:
  tax: 85000000
```

```oa-check
name: Dividend withholding
inputs:
  net: 415000000
steps:
  - wht: net * 0.10
expected:
  wht: 41500000
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Ministry of Finance Citizen Budget 2026, measures list, all pages (hosted by Institut des Finances, a Ministry body) | https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf | 2026-11-01 |
| IDAL, Doing Business, Tax System (whole page) | https://www.investinlebanon.gov.lb/en/doing_business/tax_system | 2026-11-01 |
| Ministry of Finance, finance.gov.lb tax pages | unverified: CAPTCHA, not read | not read |

Not yet confirmed: every row marked unverified. finance.gov.lb returned a CAPTCHA during this refresh, which we did not solve; only archive indexes of it were read, and the text of 2026 Budget Law No. 40 of 10 Feb 2026 was not opened (the law number comes from a search summary, not an official page). Citizen Budget wording covers measures only, so anything else in that law is unread.

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
