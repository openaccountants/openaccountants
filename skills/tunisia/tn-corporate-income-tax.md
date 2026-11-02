---
name: tn-corporate-income-tax
description: "Tunisia corporate income tax (IS) for tax year 2026: 20% standard rate, 10%, 35% and 40% sector rates, minimum tax, the new 4% contribution on banks, insurers, telecoms and car dealers from the 2026 finance law, withholding, 25 March return, audited company amendment rule and acomptes. Use for any question on Tunisian company tax, impot sur les societes, minimum tax, advance payments or sector rates. Items that could not be opened are marked unverified."
version: 1.1
jurisdiction: TN
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tunisia Corporate Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies and other legal persons in art. 45 of the Code IRPP-IS operating in Tunisia, and non-established foreign entities on Tunisian-source income. Profits taxed are those of establishments in Tunisia and those a treaty allocates to Tunisia (art. 47). Exempt bodies are listed in art. 46. Tax year 2026: the 2026 finance law items below apply to returns falling due in 2026 as stated.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Standard rate | 20% | 2026 | Taxable profit rounded down to the dinar. Art. 49 I | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Reduced rate | 10% | 2026 | Crafts, farming, fishing, listed cooperatives, post-relief regional or farm profits, support and anti-pollution activity, youth-employment projects. Art. 49 I(1) | same |
| Elevated rate | 35% | 2026 | Payment institutions, investment companies, debt collectors, telecom operators, hydrocarbon services and production, refining and wholesale, large retail, car dealers, foreign-brand franchisees with integration under 30%. Art. 49 I(3) | same |
| Financial rate | 40% | 2026 | Banks, financial institutions other than payment institutions, insurers and reinsurers. Art. 49 I(4) | same |
| Minimum tax | 0.2% of gross turnover, floor TND 500 | 2026 | Companies not at 10%; due with no turnover. Art. 49 II | same |
| Reduced minimum tax | 0.1%, floor TND 300 | 2026 | 10% companies, or price-controlled goods with gross margin up to 6%. Art. 49 II | same |
| New sector contribution | 4% of IS profit, minimum TND 10,000 | 2026 | Banks, financial institutions, insurers, telecom operators, car dealers; for returns due from 2026; not deductible; paid like IS. LF 2026 art. 20(7) | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf |
| Social Solidarity Contribution | unverified: 0.5% in the old file | 2026 | LF 2026 art. 87 extends the exceptional rule to profits whose return falls due in 2023 to 2026. Rate text not opened | unverified |
| Dividends withholding | 10% | 2026 | Art. 52 I(c bis); 25% to privileged-tax jurisdictions is for lines c, c bis, e | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Capital income withholding | 20% | 2026 | Art. 52 I(c) | same |
| Interest to foreign banks | 10% | 2026 | Art. 52 I(e) | same |
| Non-resident fees and income | 15% | 2026 | Art. 52 I(b); treaties prevail | same |
| Privileged-tax jurisdictions | 25% | 2026 | Art. 52 closing paragraph | same |
| Fees, commissions, rents, resident | 10% | 2026 | Art. 52 I(a) | same |
| Fees to IS or real-regime payees | 3%; hotel rents 5% | 2026 | Art. 52 I(a) | same |

## The base

Arts. 10 to 15 of the code apply (art. 48). Residents are taxed on Tunisian establishment profit, not on worldwide profit: the old file's worldwide statement does not match art. 47. Donations to the Union tunisienne de solidarite sociale and community companies join the art. 12(5) list (LF 2026 art. 38). The 4% contribution is not deductible.

Each year compare tax at the rate with minimum tax and pay the higher. New companies are free of minimum tax during project build-out, for three years at most; companies with full deduction are also out (art. 49 II).

## Deadlines and filing

Annual return: by 25 March, or the 25th of the third month after a non-December year end (art. 60 I(2)). Audited companies filing before the general meeting file provisionally and may amend within 15 days of approval, at the latest the 25th of the third month after that limit, which is 25 June for a December year end. So 25 June is the amendment limit, not a later filing date.

Acomptes: three, each 30% of prior-year tax, in the first 28 days of the sixth, ninth and twelfth months after year end (art. 51). Assets disposal gains are left out of the base, which cannot fall below minimum tax.

Steps: 1. Join online filing at the tax office with the adhesion form. 2. Get an ANCE certificate. 3. Complete the IS return (DGI form IS_2026) online and pay. Boxes: see Not yet confirmed.

## Penalties and interest

Minimum tax rises 50% if paid over one month late (art. 49 II). General penalties sit in the Tax Procedures Code, not opened.

## Cross-border points

Non-established entities: art. 45 II and III. Transfer pricing: [transfer pricing](tn-transfer-pricing.md). Withholding: [cross-border](tn-cross-border.md).

## Two worked examples that recompute

Simple: profit TND 100,000, turnover TND 5,000,000. Tax 20,000; minimum 10,000. Pay 20,000.

```oa-check
name: Standard company
inputs:
  profit: 100000
  turnover: 5000000
steps:
  - rate_tax: profit * 0.20
  - minimum: max(turnover * 0.002, 500)
  - tax: max(rate_tax, minimum)
expected:
  tax: 20000.00
```

Edge: bank with IS profit TND 1,000,000. IS at 40% is 400,000. The 4% contribution is 40,000 on top, not deductible. Total 440,000 before any solidarity contribution.

```oa-check
name: Bank with 4 percent contribution
inputs:
  profit: 1000000
steps:
  - is_tax: profit * 0.40
  - contribution: max(profit * 0.04, 10000)
  - total: is_tax + contribution
expected:
  total: 440000.00
```

## Ask the client first

1. Activity, and is it in a 10%, 35% or 40% list?
2. Turnover and profit for the year?
3. Year end, and is it legally audited?
4. Prior-year tax, and withholding certificates held?
5. Foreign related parties or payments abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code IRPP-IS, French text updated to LF 2025, archived copy of the DGI file; articles cited in this skill read. The 2026 edition page exists but its PDF could not be opened | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf | 2026-11-01 |
| Loi n° 2025-17 du 12 decembre 2025, loi de finances 2026, JORT n° 148, archived copy of the DGI file; tax articles read | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf | 2026-11-01 |
| DGI page on online filing, archived April 2025; steps read | https://web.archive.org/web/20250419084126/https://jibaya.tn/blog/la-tele-declaration-fiscale/ | 2026-11-01 |

Not yet confirmed: Social Solidarity Contribution rate and minimum. Exact 2026 scope of the 3% rate. The old 15% royalty line is covered only through art. 52 I(b). Tax-haven list. Return boxes. 2026 consolidated code not opened.

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
