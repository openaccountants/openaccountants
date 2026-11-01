---
name: kw-tax-overview
description: "Overview of the Kuwait tax system for tax year 2026. Covers which regime applies: 15% income tax on corporate bodies, 1% Zakat and contribution, 2.5% NLST, the 15% DMTT for large multinational groups, no tax on individual income from work, and the held VAT implementation question. Use as the first stop for what taxes apply in Kuwait, how a company is taxed in Kuwait, Kuwait tax year, tax authority, main deadlines and routing to the detailed Kuwait skills. Read from the Ministry of Finance texts. Not signed off by an accountant."
version: 0.3
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Tax Overview v0.3

Tax year 2026.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking which Kuwait tax applies. Each figure's home is the linked skill.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Tax year | Calendar year of 12 months unless MOF approves otherwise, first period up to 18 months (reg. arts. 1 and 10) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Currency | Kuwaiti dinar: DMTT amounts convert to KWD at Central Bank rates (Decree-Law 157 art. 41) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf |
| Authority | Ministry of Finance tax administration | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Individuals | Exempt on own income from trade or work, unless it represents a corporate body's share (reg. art. 8(2)) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Corporate bodies | See [corporate income tax](kw-corporate-income-tax.md) | 2026 | same |
| Zakat, NLST, DMTT | See corporate Guide for separate statutory scope and conditions | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf ; https://www.mof.gov.kw/Desicions/Decree/PDF/LawNo19Of2000NationalLabor.pdf ; https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf |
| VAT or GST | unverified: current implementation status is a NON-OPERATIVE HOLD, see [VAT](kw-vat-gst.md) | 2026 | https://www.mof.gov.kw/MOFDesicions/mofDesicions1.aspx |
| Social insurance | unverified: rates, coverage and due dates are held in [payroll](kw-payroll-social.md) | 2026 | unverified |

## The base

For ordinary income tax, source and corporate-body liability must be established under reg. arts. 1 to 3. Kuwaiti/Gulf and mixed-ownership liability is held. Art. 8(2) exempts a natural person's own work income subject to its corporate-share exception; it does not establish absence of residence concepts for treaties or foreign tax.

## Deadlines and filing

The main return date for income tax is the 15th day of the 4th month after period end. DMTT is 15 months. Detail sits in the [corporate income tax](kw-corporate-income-tax.md) skill.

## Penalties and interest

See the [corporate income tax](kw-corporate-income-tax.md) skill.

## Cross-border points

Foreign corporate-body Kuwait activity, including agency activity, requires an ordinary income-tax scope check. For multinational groups use the corporate Guide's DMTT revenue test, entity exclusions and commencement conditions before choosing the regime.

## Two worked examples that recompute

**Example 1.** A foreign branch outside DMTT has confirmed Kuwait income-tax liability, KWD 200,000 net taxable income and no exemption or unused losses. At the sourced corporate Guide rate, tax is KWD 30,000.

```oa-check
name: Branch income tax
inputs:
  income: 200000
steps:
  - tax: income * 0.15
expected:
  tax: 30000.00
```

**Example 2 (decision).** For an in-scope Kuwaiti listed shareholding company outside DMTT and all Law 46 art. 4 exclusions, assume KWD 1,000,000 is the confirmed annual net-profit base for both contributions. Zakat contribution is KWD 10,000 and NLST KWD 25,000, total KWD 35,000. Applying ordinary 15% income tax to that same number would give KWD 150,000, a difference of KWD 115,000. Choose the legally established regime, not the smaller number. The worked comparison does not resolve an ownership exemption or compute a DMTT top-up.

```oa-check
name: Listed company contributions
inputs:
  profit: 1000000
steps:
  - zakat: profit * 0.01
  - nlst: profit * 0.025
  - total: zakat + nlst
  - wrong_regime_comparator: profit * 0.15
  - difference: wrong_regime_comparator - total
expected:
  total: 35000.00
  wrong_regime_comparator: 150000.00
  difference: 115000.00
```

## Ask the client first

- Individual or company?
- Foreign, Kuwaiti or Gulf owned?
- Listed or not?
- Group revenue over EUR 750m?

## Sources

| Source | URL | Read on |
|---|---|---|
| Executive Regulations of Law 2 of 2008, Ministerial Resolution 29 of 2008, arts. 1 to 3, 8 to 14, 19, 20, 24 to 28, 34, 37 to 39, 41, 42, 46; prior writer read all 23 pages by OCR; closeout re-read cited articles and neighbouring clauses in Arabic OCR, PDF p. 8 visually checked | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |
| Decree-Law 157 of 2024, issuing articles and arts. 1 to 22, 29 to 34, 36, 38 and 41; Arabic OCR clauses and neighbours read; penalty PDF p. 10 visually checked; prior writer also checked p. 11 | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf | 2026-11-01 |

| Arabic Law 46/2006 arts. 1 to 5 and English official translation, annual contribution and exclusions read | https://www.mof.gov.kw/Desicions/Decree/PDF/Q46-2006.pdf | 2026-11-01 |
| Law 19/2000 art. 12 with neighbouring arts. 11 to 15, Arabic text read | https://www.mof.gov.kw/Desicions/Decree/PDF/LawNo19Of2000NationalLabor.pdf | 2026-11-01 |

Not yet confirmed: NON-OPERATIVE HOLDS. VAT/GST and excise implementation and all no-tax consequences (see VAT Guide); historical monthly PIFSS payment by the following month's 15th and all contribution rules (see payroll Guide); the old blanket statement that there is no individual residence concept. Mixed ownership: how the 15% applies to a company part owned by Kuwaiti and part by foreign holders, and the Kuwaiti and Gulf exemption itself, including the earlier statements here that Gulf nationals are foreign and also exempt (the texts read define the taxpayer as any corporate body; Ministerial Decision 3 of 1989 on equal treatment of Gulf nationals is named in the NLST rule but the copy on the MOF site is a different document); KFAS 1% contribution; the 2.5% and 1% interaction with Free Trade Zone exemptions under Law 26 of 1995; the extension of the FY 2026/2027 DMTT retention carve-out and five-year transfer direction to private payers; DMTT Executive Regulations detail (Ministerial Resolution 55 of 2025, not read beyond the title page); any business profits tax draft, for which no enacted text was found; the old cap of 50% on the late filing fine, which no text read supports

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
