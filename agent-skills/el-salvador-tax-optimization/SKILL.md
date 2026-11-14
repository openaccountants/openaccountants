---
name: el-salvador-tax-optimization
description: "Use this skill when someone asks how to lawfully reduce tax in El Salvador in 2026. It works the main levers to the figure that decides them: operating as an individual on the art. 37 table or through a company at 25% (taxable income up to USD 150,000) or 30% plus the 5% final tax on distributed profits; holding an asset more than 12 months so the gain bears 10% instead of ordinary rates; documenting the USD 800 medical and USD 800 school deductions near the USD 6,600 step; and the red lines (source rules, 25% on payments to tax havens, incentive regimes needing certification). Trigger phrases include reduce tax El Salvador, planificacion fiscal, persona natural o sociedad, dividendos 5% and ganancia de capital 10%."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/el-salvador-tax-optimization"
  jurisdiction: "SV"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# El Salvador tax planning levers, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Salvadoran adviser. Aggressive positions are never advised; every suggestion needs review by a qualified professional in El Salvador.

## Who this applies to

Domiciled individuals and owner-managed businesses in El Salvador deciding how to structure income in 2026. The rates themselves are owned by [el-salvador-income-tax](el-salvador-income-tax.md); this skill compares options.

## Rates, bands and thresholds

| Item | Rate | Condition | Source |
| --- | --- | --- | --- |
| Individual top band (art. 37) | 30% above USD 22,857.14, plus USD 3,462.86 | Domiciled individuals | Asamblea Legislativa, Decreto 293 (2025): https://www.asamblea.gob.sv/sites/default/files/documents/decretos/E198E77D-2027-47AA-A8F6-1D70E2F46431.pdf |
| Company rate (art. 41) | 25% | Taxable income of USD 150,000 or less | Asamblea Legislativa, LISR consolidated: https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F326A5D9-F56E-4FCA-81D6-60088ABB52BF.pdf |
| Company rate (art. 41) | 30% | Above USD 150,000 | same |
| Profits distributed (art. 72) | 5% final | Domiciled or non-domiciled shareholders | same |
| Capital gains (art. 42) | 10% | Asset held more than 12 months | same |
| Payments to tax havens (CT art. 158-A) | 25% final retention | Payee in a preferential regime | Asamblea Legislativa, Codigo Tributario consolidated: https://www.asamblea.gob.sv/sites/default/files/documents/decretos/297557B6-E5FD-4A41-B734-089751C41FDA.pdf |

## The base

The comparisons use the definitions of the income tax skill: renta imponible after costs and art. 33 deductions for individuals; taxable income for companies; utilidades distributed (art. 72) are profit after the company's tax. A company also pays the 1.75% monthly pago a cuenta on gross income (CT art. 151), which is a credit, not an extra tax.

## Deadlines and filing

Individuals and companies file the annual return within four months of year end (LISR art. 48), by 30 April 2027 for 2026. Profit distributions bear the 5% retention when paid.

## Penalties and interest

A structure that relabels Salvadoran-source income as foreign, or disguises distributions, exposes the taxpayer to the Codigo Tributario fines for incorrect returns and to criminal tax fraud rules. Not filing: 40% of the tax (CT art. 238 a).

## Cross-border points

Income is taxed when obtained in El Salvador (LISR art. 16). Paying a related company in a tax haven costs 25% final retention (CT art. 158-A) and falls under transfer pricing (CT art. 62-A). Claims that foreign-source investment income is exempt after a 2024 reform, and any tech or free zone holiday, need the actual law and certification: see Not yet confirmed.

## Two worked examples that recompute

### Example 1: consultant with USD 100,000 profit, own name or company

As an individual: USD 3,462.86 + 30% of USD 77,142.86 = USD 26,605.72. Through a company (taxable income under USD 150,000, so 25%): USD 25,000, then 5% on distributing the remaining USD 75,000, USD 3,750: total USD 28,750. The individual route costs USD 2,144.28 less. A company only wins if profit is retained rather than distributed, or other non-tax reasons apply.

```oa-check
name: SV 2026 individual against company at USD 100,000
inputs:
  profit: 100000
steps:
  - individual: round(3462.86 + (profit - 22857.14) * 0.30, 2)
  - company_tax: profit * 0.25
  - distribution_tax: (profit - company_tax) * 0.05
  - company_route: company_tax + distribution_tax
  - difference: round(company_route - individual, 2)
expected:
  individual: 26605.72
  company_tax: 25000
  distribution_tax: 3750
  company_route: 28750
  difference: 2144.28
```

### Example 2: sell now or after 12 months

An individual with other income of USD 30,000 (already in band IV) sells shares at a USD 20,000 gain. Sold within 12 months of purchase, the gain joins ordinary income and adds USD 6,000 at 30%. Held more than 12 months, it bears 10%: USD 2,000. Waiting saves USD 4,000, if the price risk is acceptable.

```oa-check
name: SV 2026 capital gain timing
inputs:
  other_income: 30000
  gain: 20000
steps:
  - tax_with_gain: 3462.86 + (other_income + gain - 22857.14) * 0.30
  - tax_without: 3462.86 + (other_income - 22857.14) * 0.30
  - short_term_cost: round(tax_with_gain - tax_without, 2)
  - long_term_cost: gain * 0.10
  - saving: short_term_cost - long_term_cost
expected:
  short_term_cost: 6000
  long_term_cost: 2000
  saving: 4000
```

## Ask the client first

1. Expected profit and how much will be taken out each year.
2. Domicile of the owners.
3. Assets to be sold, purchase dates and costs.
4. Any related parties abroad, especially in low-tax places.
5. Any incentive regime (free zone, international services, technology) the business already holds, with its certificate.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Decreto Legislativo 293 (2025), art. 37 table | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/E198E77D-2027-47AA-A8F6-1D70E2F46431.pdf | 2026-11-14 |
| Read for LISR consolidated, arts. 16, 41, 42, 48 and 72 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F326A5D9-F56E-4FCA-81D6-60088ABB52BF.pdf | 2026-11-14 |
| Read for Codigo Tributario consolidated, arts. 62-A, 151, 158-A and 238 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/297557B6-E5FD-4A41-B734-089751C41FDA.pdf | 2026-11-14 |

Not yet confirmed: the 2024 exemption for foreign-source investment income (not in the consolidated LISR read); the 15-year income and municipal tax holiday for software, AI, cybersecurity and data businesses (innovation law not read); free zone dividend exemptions; the "10% on domestic investment income" figure of the old file (only the 10% capital gains rate of art. 42 was confirmed).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `el-salvador-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/el-salvador-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
