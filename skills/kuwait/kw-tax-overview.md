---
name: kw-tax-overview
description: "Overview of the Kuwait tax system for tax year 2026. Covers which regime applies: 15% income tax on corporate bodies, 1% Zakat and contribution, 2.5% NLST, the 15% DMTT for large multinational groups, no tax on individual income from work, and no VAT. Use as the first stop for what taxes apply in Kuwait, how a company is taxed in Kuwait, Kuwait tax year, tax authority, main deadlines and routing to the detailed Kuwait skills. Read from the Ministry of Finance texts. Not signed off by an accountant."
version: 0.2
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Tax Overview

Tax year 2026.

## Who this applies to

Anyone asking which Kuwait tax applies. Each figure's home is the linked skill.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Tax year | Calendar year of 12 months unless MOF approves otherwise, first period up to 18 months (reg. arts. 1 and 10) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Currency | Kuwaiti dinar: DMTT amounts convert to KWD at Central Bank rates (Decree-Law 157 art. 41) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf |
| Authority | Ministry of Finance tax administration | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Individuals | No tax on income from trade or work (reg. art. 8) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Corporate bodies | See [corporate income tax](kw-corporate-income-tax.md) | 2026 | same |
| Zakat, NLST, DMTT | See [corporate income tax](kw-corporate-income-tax.md) | 2026 | same |
| VAT or GST | None, see [VAT](kw-vat-gst.md) | 2026 | same |
| Social insurance | See [payroll](kw-payroll-social.md) | 2026 | same |

## The base

Kuwait taxes corporate bodies on Kuwait-source income, not worldwide income. Individuals have no residence test because they have no income tax.

## Deadlines and filing

The main return date for income tax is the 15th day of the 4th month after period end. DMTT is 15 months. Detail sits in the [corporate income tax](kw-corporate-income-tax.md) skill.

## Penalties and interest

See the [corporate income tax](kw-corporate-income-tax.md) skill.

## Cross-border points

Foreign companies are caught when trading in Kuwait, including through an agent. Large groups go to DMTT instead.

## Two worked examples that recompute

**Example 1.** A foreign branch earns KWD 200,000: 15% gives KWD 30,000.

```oa-check
name: Branch income tax
inputs:
  income: 200000
steps:
  - tax: income * 0.15
expected:
  tax: 30000.00
```

**Example 2 (decision).** A Kuwaiti listed company earns KWD 1,000,000 outside DMTT: Zakat KWD 10,000 and NLST KWD 25,000, against KWD 150,000 for a body under the income tax. The deciding fact is which regime applies, not the profit.

```oa-check
name: Listed company contributions
inputs:
  profit: 1000000
steps:
  - zakat: profit * 0.01
  - nlst: profit * 0.025
  - total: zakat + nlst
expected:
  total: 35000.00
```

## Ask the client first

- Individual or company?
- Foreign, Kuwaiti or Gulf owned?
- Listed or not?
- Group revenue over EUR 750m?

## Sources

| Source | URL | Read on |
|---|---|---|
| Executive Regulations of Law 2 of 2008, Ministerial Resolution 29 of 2008, arts. 1 to 3, 8 to 14, 19, 20, 24 to 28, 34, 37 to 39, 41, 42, 46; all 23 pages read in Arabic by OCR, art. 9 by page image | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |
| Decree-Law 157 of 2024, issuing articles and arts. 1, 16, 17, 19, 20, 22, 29 to 34, 36, 38; Kuwait Al-Youm supplement 1719, 31 Dec 2024; read in Arabic by OCR, pp. 10 and 11 by page image | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf | 2026-11-01 |

Not yet confirmed: Mixed ownership: how the 15% applies to a company part owned by Kuwaiti and part by foreign holders, and the Kuwaiti and Gulf exemption itself, including the earlier statements here that Gulf nationals are foreign and also exempt (the texts read define the taxpayer as any corporate body; Ministerial Decision 3 of 1989 on equal treatment of Gulf nationals is named in the NLST rule but the copy on the MOF site is a different document); KFAS 1% contribution; the 2.5% and 1% interaction with Free Trade Zone exemptions under Law 26 of 1995; the extension of the 5% retention rule beyond the FY 2026/2027 text for private payers; DMTT Executive Regulations detail (Ministerial Resolution 55 of 2025, not read beyond the title page); any business profits tax draft, for which no enacted text was found; the old cap of 50% on the late filing fine, which no text read supports

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
