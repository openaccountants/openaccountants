---
name: cw-corporate-income-tax
description: "Curacao profit tax (winstbelasting) for companies, tax year 2026. Covers who pays (N.V., B.V., cooperatives, foundations and associations running a business, SPF), the 15% rate on the first 500,000 of taxable profit and 22% above, the 0% Curacao investment company, the 10/T rate for doelvermogens, the 3% rate for low-taxed activities and the expired 2% E-zone rate, the optional territoriality rule, rulings, the provisional return within three months and the final return within six, extensions and penalties. Trigger phrases include Curacao corporate tax, winstbelasting Curacao, profit tax Curacao, voorlopige aangifte, Curacao investment company, territoriality Curacao."
version: "1.0"
jurisdiction: CW
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: computation
---

# Curacao profit tax (winstbelasting) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: the calendar year 2026, or a financial year that differs from it. Authority: Belastingdienst Curacao (belastingdienst.cw). Amounts are Curacao guilders (ANG or NAf on older pages, XCG or Cg on newer ones).

## Who this applies to

Legal persons pay profit tax; a sole trader pays income tax on business profit instead ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)). Taxpayers include (same page):
- naamloze vennootschappen (N.V.) and besloten vennootschappen (B.V.);
- open limited partnerships, cooperatives and mutual insurers;
- doelvermogens (special-purpose funds);
- associations and foundations, if they run a business (a foundation only if it does not serve the general public interest alone);
- the stichting particulier fonds (SPF);
- other bodies with share capital.

Out of scope: income tax for sole traders and partners (`cw-income-tax`), turnover tax (`cw-vat-gst`), wage tax (`cw-payroll-social`), forming the company (`cw-company-formation`), the Pillar Two minimum tax (see "Not yet confirmed").

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| General rate, first band | 15% | On the first 500,000 of taxable profit | 2026 | [Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/) |
| General rate, above the band | 22% | On taxable profit above 500,000 | 2026 | same |
| Curacao investment company (Curacaose Beleggingsvennootschap) | 0% | The exempt company was converted into this form from 1 July 2018 | 2026 | same |
| Doelvermogen | 10/T, where T is the general rate | Bodies designated as doelvermogens | 2026 | same |
| Low-taxed activities | 3% | Building, repair and maintenance of ships and aircraft; support services; storage and logistics; services to investment funds. Not for notaries, lawyers, public accountants, tax advisers or management services | 2026 | same |
| E-zone company | 2% | Applied up to and including the year 2022 only | 2022 and earlier | same |
| Late or missing return | penalty ANG 250 to ANG 2,500 | Rises with the number of defaults | 2026 | same |
| Late or missing payment | penalty ANG 250 to ANG 10,000 | Rises with the number of defaults | 2026 | same |
| Fault penalty | 25% (gross negligence), 50% (intent), 100% (serious fraud); repeat: 50% or 100% | Of the tax concerned | 2026 | same |
| Ruling validity | at most 3 years | Lapses if facts change | 2026 | same |

The 2026 Belastingdienst handbook repeats the 15% and 22% rates with the band printed as Cg. 500,000, and the penalty range Cg. 250 to Cg. 10,000 ([Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf)).

## The base

1. **Profit tax is self-assessed.** You compute and pay it; the Belastingdienst checks later ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)).
2. **Commercial to tax profit.** Proper books are compulsory. The handbook notes the gap between commercial and tax profit, usually worked out by an accountant from the annual accounts ([Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf)).
3. **Territoriality (optional).** A company with Curacao and foreign results may include only the result from activities in Curacao and assets connected to Curacao. Look at where the causal costs are incurred. All profit counts as domestic unless you show which part is foreign, so the rule is not compulsory: you choose it on the return. Finance and non-finance businesses are treated differently, and it applies only to income from a material business (a lasting organisation of capital and labour). Passive income (interest, royalties, rent, dividends) is always domestic and taxed in Curacao, including for a foreign company with a Curacao permanent establishment and for banks and insurers ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)).
4. **Rulings.** An advance ruling gives certainty on, for example, the Curacao investment company, the fiscal unity, transparent status and doelvermogens. Send a written request to rulingverzoeken@gobiernu.cw or through the contact form with: name, address and CRIB number; any representative's authority; a full description of the facts and proposed transactions; their purpose; transfer pricing reports where relevant; for cross-border transactions, the countries the ruling will be exchanged with and the effects there; the organisation chart; answers to the "Template and instruction sheet for information exchange". Not in person (same page).
5. **Participation exemption, loss carry-forward, depreciation and interest limits** are not on the pages read: see "Not yet confirmed".

## Deadlines and filing

Two returns a year, both online through the portal with a user account; payment by bank only, not cash ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)):

| Return | Deadline | Payment | Extension | Source |
|---|---|---|---|---|
| Provisional (voorlopige aangifte) | Within 3 months after the end of the calendar or financial year | With the return; at least the tax on the last final return filed | None | [Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/) |
| Final (definitieve aangifte) | Within 6 months after the year end | With the return | Reasoned request; if the Inspector does not refuse within 15 days, the deadline moves by 3 months | same |

- **Lower provisional amount.** If your provisional figure is below the last final return, send a reasoned written request on the prescribed form through the contact form before paying the lower amount. The Inspector needs two weeks, so ask at least a month before the provisional deadline (same page).
- **Income statement for a company** (inkomensverklaring): only after the profit tax return is filed and processed; request it through the contact form with the company details, CRIB number and the reason (same page).
- For a 31 December 2026 year end: provisional return and payment by 31 March 2027, final by 30 June 2027.

## Penalties and interest

- Late or missing return: ANG 250 to ANG 2,500; late or missing payment: ANG 250 to ANG 10,000, each depending on how often the taxpayer has defaulted ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)).
- Gross negligence 25%, intent 50%, serious fraud 100%; on repeat, 50% for gross negligence and 100% for intent (same page).
- Interest on late tax is not on the pages read.

## Cross-border points

- Passive income stays taxable in Curacao even under territoriality, including for a Curacao permanent establishment of a foreign company (see "The base").
- Rulings with a cross-border element are exchanged with the other countries concerned and need transfer pricing reports where relevant ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)).
- Withholding taxes on dividends, interest and royalties, and the Pillar Two minimum tax, are not confirmed on an official page: refer.

## Two worked examples that recompute

**Case 1: ordinary B.V., calendar 2026.** Taxable profit 800,000. 15% of 500,000 = 75,000; 22% of 300,000 = 66,000. Profit tax 141,000; effective rate 17.625%. Provisional return and payment by 31 March 2027 for at least the 2025 final-return tax; final return by 30 June 2027.

```oa-check
name: Curacao profit tax, taxable profit 800000
inputs:
  profit: 800000
  band: 500000
  low_rate: 0.15
  high_rate: 0.22
steps:
  - low_part: min(profit, band) * low_rate
  - high_part: max(profit - band, 0) * high_rate
  - tax: low_part + high_part
  - effective_pct: tax / profit * 100
expected:
  low_part: 75000.00
  high_part: 66000.00
  tax: 141000.00
  effective_pct: 17.625
```

**Case 2: decision, claim territoriality or not.** A company has total profit of 1,000,000, of which it can document 400,000 as foreign result of a material business (no passive income). Without territoriality: 75,000 + 22% of 500,000 = 185,000. With it: taxable 600,000, so 75,000 + 22% of 100,000 = 97,000. Claiming saves 88,000, but only if the company can show which part is foreign; otherwise all profit is domestic.

```oa-check
name: Territoriality claimed or not
inputs:
  total_profit: 1000000
  foreign_profit: 400000
  band: 500000
  low_rate: 0.15
  high_rate: 0.22
steps:
  - tax_without: min(total_profit, band) * low_rate + max(total_profit - band, 0) * high_rate
  - domestic_profit: total_profit - foreign_profit
  - tax_with: min(domestic_profit, band) * low_rate + max(domestic_profit - band, 0) * high_rate
  - saving: tax_without - tax_with
expected:
  tax_without: 185000.00
  tax_with: 97000.00
  saving: 88000.00
```

## Ask the client first

1. Legal form, CRIB number and financial year end.
2. Taxable profit, and the tax on the last final return filed (the provisional minimum).
3. Activities: any low-taxed activity (ships, aircraft, support services, logistics, fund services), investment company or doelvermogen status, or a pre-2023 E-zone history?
4. Any foreign activities or assets, and passive income (interest, royalties, rent, dividends)?
5. Any ruling in force, and when it was issued?
6. Late returns or payments in earlier years?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Office Curacao, Winstbelasting (theme page): read for taxpayers, the 15% and 22% rates, the 0%, 10/T, 2% and 3% rates, territoriality, rulings, both returns, extensions and penalties | https://belastingdienst.cw/ondernemer/themas/winstbelasting/ | 2026-11-14 |
| Tax Office Curacao handbook "De basis van succesvol ondernemen" (2026): read for the rates in Cg, the commercial to tax profit step and the penalty range | https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf | 2026-11-14 |

Not yet confirmed: the participation exemption conditions; loss carry-forward, depreciation and interest limits; withholding tax on dividends, interest and royalties (the old file said 0%, citing a law firm); the Pillar Two minimum tax (Landsverordening minimumbelasting), its start date and filing duties (only secondary sources found); interest on late profit tax; the current Economic Zones rules after 2022.
