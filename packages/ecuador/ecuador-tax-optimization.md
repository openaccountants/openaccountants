---
name: ecuador-tax-optimization
description: "Lawful ways to pay the right amount of tax in Ecuador in 2026 for individuals, entrepreneurs and small businesses, with the decisions worked in figures. Covers the RIMPE regime (mandatory for those in scope, gross income up to USD 300,000, Negocio Popular up to USD 20,000, three years from the first return, no re-entry, and the activities it excludes), what happens when gross income passes USD 300,000, claiming the gastos personales rebate (18% of the lower of expenses and the canasta cap, only with the Anexo filed), the 3-SBU dividend exemption per company, and the red lines. Trigger on: reduce tax Ecuador, tax planning Ecuador, RIMPE negocio popular, RIMPE emprendedor 300,000, gastos personales rebaja, save tax Ecuador, should I stay in RIMPE. Figures belong to the sibling skills, which this one links: ecuador-income-tax (tables, rebate caps, RIMPE tables), ec-corporate-income-tax (dividends, reinvestment), ecuador-social-contributions (IESS)."
version: 0.2
jurisdiction: EC
tax_year: 2026
last_updated: 2026-11-11
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: decision
---

# Ecuador: tax planning decisions (2026) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill works through the planning choices an Ecuadorian individual or small business actually has in 2026, and the ones it does not have. It holds no rates of its own: the tables, caps and deadlines live in [ecuador-income-tax](ecuador-income-tax.md), [ec-corporate-income-tax](ec-corporate-income-tax.md), [ecuador-social-contributions](ecuador-social-contributions.md) and [ecuador-payroll](ecuador-payroll.md). Only lawful choices are covered. Anything that hides income, splits a business to stay under a threshold without substance, or misstates residence is out.

**Quick reference (2026).** RIMPE is not a choice: it applies by law to people and companies in scope (gross income up to USD 300,000, activity not excluded) for three years from the first return. Above USD 300,000 in a year, that year is taxed under the general regime and the taxpayer can never return to RIMPE. The gastos personales rebate is worth 18% of the lower of the expenses and the cap (USD 7,396.20 of expenses with one dependant in 2026), but only if the Anexo de Gastos Personales is filed in February. Dividends: the first 3 SBU (USD 1,446) a year from each company are exempt for a resident individual.

## Who this applies to

- **Individuals** (employees, the self-employed, landlords) taxed on the 2026 table, who can reduce tax through the gastos personales rebate and the exemptions in ecuador-income-tax.
- **People and companies in RIMPE**: gross annual income up to USD 300,000 (LRTI art. 97.3). Individuals with up to USD 20,000 are Negocios Populares; everyone else in the regime is an Emprendedor (art. 97.3).
- **Excluded from RIMPE whatever else they do** (art. 97.4): construction and land development (arts. 28, 29), professional services, mandates and representation, commission agents, transport except taxis, farming, fuel sales, employment, leasing of movable or immovable property, other special regimes, hydrocarbons, mining, petrochemicals, medical labs and pharmaceuticals, basic industries, finance, the popular and solidarity economy, insurance, and ICE goods and services; also artisans, recipients of foreign direct investment and public-private partnerships.
- **Owners of companies** deciding how to take profits: see ec-corporate-income-tax for the 12% dividend tax, the payment on undistributed profits and the reinvestment reduction.

## Rates, bands and thresholds

| Item | Rule or amount | Year | Source |
|---|---|---|---|
| RIMPE scope | individuals and companies with gross annual income up to USD 300,000 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 97.3) |
| Negocio Popular | individuals with gross income up to USD 20,000; fixed tax bands in ecuador-income-tax | 2026 | same (art. 97.3); https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf (Decreto Ley 742 art. 12) |
| Emprendedor band USD 200,000 to 300,000 | USD 2,797.52 plus 2.00% of the excess over USD 200,000, on gross income | 2026 | same (Decreto Ley 742 art. 12, table replacing LRTI art. 97.6); full table in ecuador-income-tax |
| RIMPE is mandatory | applies for three years from the first return while gross income stays at or below USD 300,000; Negocios Populares stay while they keep that status | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 97.5) |
| Gross income above USD 300,000 at year end | that year's tax is declared and paid under the general regime | 2026 | same (art. 97.6, last paragraph) |
| Once excluded | no re-entry into RIMPE | 2026 | same (art. 97.5) |
| General regime table, band USD 46,575 to 62,005 | USD 4,965 plus 25% of the excess | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf (Res. NAC-DGERCGC25-00000043 art. 2); full table in ecuador-income-tax |
| Gastos personales rebate | 18% of the lower of the expenses and the cap; canasta USD 821.80; cap 7 canastas with no dependants, 9 with one, up to 20 (100 for catastrophic illness or disability) | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ea002a89-17d8-4cdf-be42-affedbe3f8d8/BOLET%C3%8DN%20006%20-%20SRI%20HABILITA%20LA%20PROYECCI%C3%93N%20DE%20GASTOS%20PERSONALES%202026%20PARA%20REDUCIR%20EL%20IMPUESTO%20A%20LA%20RENTA.pdf (SRI Boletín NAC-COM-26-006); caps in ecuador-income-tax |
| Dividend exemption for a resident individual | 3 SBU (3 × USD 482 = USD 1,446) per distributing company per year | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 39.2(7)) |

## The base

**What can and cannot be chosen.**

1. **RIMPE or general regime is not an election.** If the gross income and the activities put a person in RIMPE, it applies for three years from the first return (art. 97.5). Earlier versions of this skill described Emprendedores being "moved to the general regime in 2025"; what the law says is that RIMPE ends after three years (or on passing USD 300,000), with no way back.
2. **RIMPE taxes gross income.** Costs do not reduce RIMPE tax (art. 97.3), so a low-margin business pays proportionally more than a high-margin one. A Negocio Popular subtracts wages of IESS-affiliated employees when its IESS obligations are up to date at the filing date (art. 97.3).
3. **Passing USD 300,000 changes the whole year.** The year is then taxed under the general regime on profit (art. 97.6), and the taxpayer stays out of RIMPE for good (art. 97.5). Whether that costs more depends on the margin: see Example 2.
4. **The gastos personales rebate is the main lever for individuals in the general regime and for employees.** It needs real, documented expenses in Ecuador (housing, health, food, clothing, education, national tourism) with receipts, and the Anexo de Gastos Personales filed in February; employees also give their employer a projection in February (ecuador-income-tax; RLRTI arts. 34, 104).
5. **Dividends**: each company's first 3 SBU a year to a resident individual is exempt (art. 39.2(7)). The timing and reinvestment choices are worked in ec-corporate-income-tax (Example 2 there decides distributing by 31 July or keeping the profits).
6. **IESS**: a voluntary or self-employed affiliate chooses the declared base above the SBU; the trade-off is in ecuador-social-contributions (Example 2 there).

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Anexo de Gastos Personales (needed to take the rebate) | February of the following year, by the ninth digit | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/a51f041a-d0b5-49d0-a2e0-7af11552f3c0/BOLETI%CC%81N%20004%20-%20EN%20FEBRERO%20LOS%20CONTRIBUYENTES%20DEBEN%20PRESENTAR%20EL%20ANEXO%20DE%20GASTOS%20PERSONALES%20DEL%20PER%C3%8DODO%20FISCAL%202025.pdf (SRI Boletín NAC-COM-26-004); detail in ecuador-income-tax |
| Employee's projection of gastos personales to the employer | February of the tax year | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 104) |
| Returns (general regime in March, RIMPE by June at the latest, companies in April) | by the ninth digit; dates in ecuador-income-tax and ec-corporate-income-tax | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 72) |

**Planning steps, in order.**

1. Read the RUC: which regime and activities are registered? An excluded activity on the RUC excludes RIMPE even if it is not the main one (art. 97.4).
2. Project gross income for the year against USD 20,000 and USD 300,000.
3. If close to USD 300,000, run Example 2 with the real margin before deciding when to invoice.
4. Collect receipts for gastos personales through the year, in the taxpayer's or a registered dependant's name; register dependants in SRI en línea.
5. File the Anexo in February and the return by the ninth-digit date.

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Late return | 3% of the tax a month, up to 100%; 0.1% of gross income a month, up to 5%, if no tax is due | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 100); detail in ecuador-income-tax |
| Tax assessed by the SRI | 20% surcharge on the principal, plus interest at 1.3 times the reference rate | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf (CT arts. 21, 90) |

## Cross-border points

- **Temporary tax residence** (5 years taxed on Ecuadorian-source income only, for people who were never resident and invest USD 150,000 or prove USD 2,500 a month of foreign income) is in ecuador-income-tax.
- **Moving to a tax haven** keeps a resident taxable in Ecuador for four more years unless they prove 183 days and their centre of interests there (LRTI art. 4.1(b)); see ecuador-income-tax.
- Payments abroad and the currency outflow tax are in ec-cross-border.

## Two worked examples that recompute

### Example 1: claim the gastos personales rebate or not

Ana is an employee. Her 2026 taxable base after IESS is USD 32,598 (USD 3,000 a month, as in ecuador-payroll). She has one dependant. She spends about USD 8,000 a year on housing, health, food, clothing and education in Ecuador and keeps the receipts.

- **No Anexo filed:** tax on the 2026 table 1,412 + 15% × (32,598 − 26,700) = **USD 2,296.70**; no rebate.
- **Anexo filed with USD 5,000 of receipts:** rebate 18% × 5,000 = **USD 900.00**; tax **USD 1,396.70**.
- **Anexo filed with all USD 8,000:** the one-dependant cap is 9 × 821.80 = USD 7,396.20, so the rebate is 18% × 7,396.20 = **USD 1,331.32**; tax **USD 965.38**.

What decides it: the rebate stops growing at the cap, so receipts above USD 7,396.20 add nothing; below it, each documented dollar is worth 18 cents. Filing the Anexo is the only way to get it.

```oa-check
name: EC 2026 planning, gastos personales rebate with one dependant
inputs:
  base: 32598
  canasta: 821.80
  canastas: 9
  gastos_low: 5000
  gastos_high: 8000
steps:
  - tax_table: 1412 + (base - 26700) * 0.15
  - cap: canastas * canasta
  - rebate_low: min(gastos_low, cap) * 0.18
  - rebate_high: round(min(gastos_high, cap) * 0.18, 2)
  - tax_low: tax_table - rebate_low
  - tax_high: tax_table - rebate_high
expected:
  tax_table: 2296.70
  cap: 7396.20
  rebate_low: 900.00
  rebate_high: 1331.32
  tax_low: 1396.70
  tax_high: 965.38
```

### Example 2: an Emprendedor close to USD 300,000 (a decision worked both ways)

Carlos runs a shop as a RIMPE Emprendedor (not an excluded activity). By December 2026 his gross income is USD 299,000. A customer wants a USD 2,000 invoice now or in January 2027. His profit margin is 20%. He is in his second RIMPE year.

- **Invoice in January (gross 2026 USD 299,000):** RIMPE tax 2,797.52 + 2% × (299,000 − 200,000) = **USD 4,777.52**.
- **Invoice in December (gross 2026 USD 301,000):** above USD 300,000, so 2026 is taxed in the general regime on profit, 20% × 301,000 = USD 60,200: 4,965 + 25% × (60,200 − 46,575) = **USD 8,371.25** before any rebate. He also leaves RIMPE for good.
- Difference: **USD 3,593.73** more tax for 2026.

What decides it is the margin. At a 20% margin the general regime costs more; at a low margin it could cost less, because RIMPE taxes gross income. Moving a genuine sale to the date it is really made is lawful; recording a December sale in January is not. Either way RIMPE ends after his third year (art. 97.5).

```oa-check
name: EC 2026 planning, Emprendedor at USD 299,000 or 301,000, 20% margin
inputs:
  gross_low: 299000
  gross_high: 301000
  margin: 0.20
steps:
  - rimpe_tax: 2797.52 + (gross_low - 200000) * 0.02
  - profit: gross_high * margin
  - general_tax: 4965 + (profit - 46575) * 0.25
  - extra_cost: general_tax - rimpe_tax
expected:
  rimpe_tax: 4777.52
  profit: 60200
  general_tax: 8371.25
  extra_cost: 3593.73
```

## Ask the client first

1. What does the RUC show: regime (general, RIMPE Negocio Popular, RIMPE Emprendedor) and every registered activity?
2. Gross income so far and projected for the year; profit margin; year of the first RIMPE return.
3. For individuals: number of dependants, receipts for gastos personales, and whether the Anexo was filed last year.
4. For company owners: dividends expected and from how many companies; whether profits will be kept past 31 July.
5. Residence: any plan to move abroad or recent arrival (temporary tax residence)?

## Sources

| Source | URL | Read on |
|---|---|---|
| LRTI, SRI codification (last reform 1 Apr 2026): arts. 4.1, 39.2, 97.1 to 97.7, 100 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| Decreto Ley 742 (RO Supl. 335, 20 Jun 2023), SRI copy: art. 12, RIMPE tables | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC25-00000043: 2026 table, art. 2 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf | 2026-11-11 |
| SRI Boletín NAC-COM-26-006: canasta USD 821.80 and the 18% rebate (as read for ecuador-income-tax the same day) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ea002a89-17d8-4cdf-be42-affedbe3f8d8/BOLET%C3%8DN%20006%20-%20SRI%20HABILITA%20LA%20PROYECCI%C3%93N%20DE%20GASTOS%20PERSONALES%202026%20PARA%20REDUCIR%20EL%20IMPUESTO%20A%20LA%20RENTA.pdf | 2026-11-11 |
| SRI Boletín NAC-COM-26-004: Anexo de Gastos Personales in February | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/a51f041a-d0b5-49d0-a2e0-7af11552f3c0/BOLETI%CC%81N%20004%20-%20EN%20FEBRERO%20LOS%20CONTRIBUYENTES%20DEBEN%20PRESENTAR%20EL%20ANEXO%20DE%20GASTOS%20PERSONALES%20DEL%20PER%C3%8DODO%20FISCAL%202025.pdf | 2026-11-11 |
| RLRTI, SRI codification (last reform 18 Nov 2025): arts. 34, 72, 104 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| Código Tributario, SRI codification (10 Aug 2023): arts. 21, 90 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf | 2026-11-11 |

Not yet confirmed: the old version's statement that RIMPE Emprendedores "are being moved to the general regime" in 2025 (it cited the SRI and a news site; no SRI resolution or law was read that does more than art. 97.5's three-year limit); the old "0% VAT for Negocio Popular sales" (see ecuador-iva for how a RIMPE trader charges IVA); the old "1% to 2% on gross income" summary (the Emprendedor table runs from 1.00% to 2.00% marginal rates on top of fixed amounts; see ecuador-income-tax); whether the three years count from the first RIMPE return for taxpayers moved in from the earlier RISE or microenterprise regimes.
