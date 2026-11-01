---
name: kw-company-formation
description: "Company formation and entity choice in Kuwait for tax year 2026, with the tax consequences. Covers WLL, closed and public shareholding companies, direct investment licences under Law 116 of 2013, tax exemption up to ten years, tax card and first registrations. Use for questions on setting up in Kuwait, foreign ownership, KDIPA licence, 100% ownership, which entity pays Zakat or NLST, or tax steps after incorporation. Company-law figures that could not be read at source are marked unverified. Not signed off by an accountant."
version: 0.2
jurisdiction: KW
category: formation
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Company Formation and Entity Choice

Tax year 2026.

## Who this applies to

Founders and foreign investors choosing a vehicle in Kuwait.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Direct investment ownership | Up to 100% of the capital of the company under a Law 116 of 2013 licence | 2026 | https://kdipa.gov.kw/wp-content/uploads/2021/08/law1162013.pdf |
| Licensed investment exemption | Income tax or other taxes exempted for up to ten years from actual start of operations (art. 27) | 2026 | same |
| Expansion | Exempt for no less than the original exemption period (art. 27) | 2026 | same |
| Imports for the investment | Machinery, tools and equipment wholly or partly exempt from duties (art. 27) | 2026 | same |
| WLL | unverified: most common small vehicle, one shareholder allowed, no fixed statutory minimum capital | 2026 | unverified |
| Closed KSC and public KSCP | unverified: minimum capital set by the Companies Law and regulations | 2026 | unverified |
| Kuwaiti partner | unverified: at least 51% outside a direct investment licence | 2026 | unverified |
| Incorporation time | unverified: 2 to 6 weeks for a WLL | 2026 | unverified |

## The base

Entity choice sets the tax regime. Public and closed shareholding companies pay the Zakat contribution, and listed companies pay NLST, see [corporate income tax](kw-corporate-income-tax.md). A WLL is outside Law 46 of 2006 by its terms.

## Deadlines and filing

1. Reserve the name, notarise the articles, deposit capital, obtain the commercial licence and Chamber membership, and enter the commercial register through the Kuwait Business Center at https://kbc.moci.gov.kw. This order is carried from the earlier version and is unverified.
2. For a licence under Law 116 of 2013, follow the KDIPA procedures at https://kdipa.gov.kw/investors-service-center/investment-licensing-procedures/.
3. A foreign corporate body registers with the tax administration within 30 days and applies for a tax card.
4. Each year: audited statements, licence renewal, tax or Zakat returns, and PIFSS registration.

## Penalties and interest

See the [corporate income tax](kw-corporate-income-tax.md) skill.

## Cross-border points

A foreign company can also work through an agent, and is still taxed on that activity. Agency contracts go with the tax card application (reg. art. 12).

## Two worked examples that recompute

**Example 1.** A licensed entity with income of KWD 500,000 and a full exemption saves KWD 75,000 at 15%.

```oa-check
name: Value of exemption
inputs:
  income: 500000
steps:
  - saved: income * 0.15
expected:
  saved: 75000.00
```

**Example 2 (decision).** Closed KSC or WLL, profit KWD 100,000, neither listed. The KSC bears 1%, KWD 1,000. A WLL does not fall under Law 46 of 2006.

```oa-check
name: KSC contribution
inputs:
  profit: 100000
steps:
  - zakat: profit * 0.01
expected:
  zakat: 1000.00
```

## Ask the client first

- Who are the shareholders and their nationalities?
- What activity, and is it on the excluded list under Council of Ministers Decision 75 of 2015?
- Will it seek a KDIPA licence?
- Will it list?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 116 of 2013, English text, arts. 25 to 27 read | https://kdipa.gov.kw/wp-content/uploads/2021/08/law1162013.pdf | 2026-11-01 |
| Law 46 of 2006, English text, arts. 1 to 5 read | https://www.mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf | 2026-11-01 |
| Executive Regulations of Law 2 of 2008, Ministerial Resolution 29 of 2008, arts. 1, 2, 8 to 10, 11 to 16, 24, 26 to 28, 34, 36 to 39, 41, 42, 46, 47; all 23 pages read in Arabic by OCR, art. 9 by page image | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |

Not yet confirmed: Companies Law 1 of 2016 text: moci.gov.kw law pages gave no document link. Minimum capital for WLL, KSC and KSCP. The 51% partner rule. Timeline and step order. Chamber membership and licence renewal details. Whether the KFAS contribution falls on closed KSCs.

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
