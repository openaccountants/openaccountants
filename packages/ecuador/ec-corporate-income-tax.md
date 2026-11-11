---
name: ec-corporate-income-tax
description: "Ecuador corporate income tax (impuesto a la renta de sociedades) for tax year 2026 under the Ley de Régimen Tributario Interno (LRTI) and its Reglamento. Covers who is a sociedad and resident, the 25% general rate and the 3-point surcharge when ownership is not reported or runs through a tax haven with an Ecuadorian beneficial owner (applied pro rata below 50%), the reductions (3 points for micro and small companies and habitual exporters, 3 points for new investment, up to 5 points under investment contracts, 8% or 10% for reinvestment in qualifying programmes), the 2-point tax stability option, RIMPE for companies, losses (5 years, 25% a year), the voluntary advance, the 12% single tax on dividends (10% to non-residents, 14% cases) and the new payment on undistributed profits, the 10% single tax on share sales, withholding at source, filing in April by ninth digit, penalties and interest. Trigger on: impuesto a la renta sociedades 2026, tarifa 25% Ecuador, 28% paraíso fiscal, reinversión de utilidades, pago a cuenta utilidades no distribuidas, dividendos 12%, RIMPE sociedad, retención en la fuente 2026, Ecuador corporate tax 2026."
version: 1.0
jurisdiction: EC
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Ecuador: corporate income tax (2026) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers the annual income tax of companies and other sociedades for the 2026 calendar year, the tax on the dividends they pay, and the payment on profits they keep. It links to the other Ecuador skills and does not repeat them:

- [ecuador-income-tax](ecuador-income-tax.md): individuals, including RIMPE individuals and how a resident shareholder reports dividends.
- [ecuador-iva](ecuador-iva.md): IVA.
- [ecuador-payroll](ecuador-payroll.md) and [ecuador-social-contributions](ecuador-social-contributions.md): employees and IESS.
- [ec-company-formation](ec-company-formation.md): setting up a company.

**Which text of the law.** The LRTI codification published by the SRI's Dirección Nacional Jurídica with last reform 1 April 2026, which includes the Ley Orgánica de Transparencia Social (Registro Oficial, third Suplemento 112, 28 August 2025) that replaced the dividend rules (art. 39.2) and added the payment on undistributed profits (art. 39.2.1), both applicable from 1 September 2025 (its first final provision). The Reglamento (RLRTI) used is the SRI codification with last reform 18 November 2025. Withholding percentages are in SRI Resolution NAC-DGERCGC26-00000009, applicable from 1 March 2026.

**Quick reference (2026).** Tax year: calendar year (LRTI art. 7). Rate: 25%; 28% where the surcharge applies; 22% for micro and small companies and habitual exporters. Return due: 10 to 28 April 2027 by the ninth digit of the RUC. Dividends: 12% single tax withheld by the company (10% to non-residents). Profits kept on 31 July: pago a cuenta from 0% to 2.50% of the whole balance, due in August.

## Who this applies to

- **Sociedades** (LRTI art. 98): legal persons, de facto companies, trusts (fideicomisos mercantiles), independent or autonomous estates with or without legal personality, consortia, holding companies that consolidate with subsidiaries, investment funds, and any entity that forms an economic unit or estate separate from its members. Exception: estates set up by state institutions where those institutions are the beneficiaries.
- **Resident company**: one constituted or created in Ecuador under Ecuadorian law (art. 4.2). It is taxed on worldwide income (art. 2).
- **Branches** of foreign companies domiciled in Ecuador, and **permanent establishments** of non-domiciled foreign companies, pay the same rate on their base (art. 37).
- **Must keep accounts**: every sociedad (art. 19; RLRTI art. 37), signed by an authorised accountant, with supporting documents kept at least 7 years.
- **RIMPE companies**: companies with gross annual income up to USD 300,000 and no excluded activity pay on gross income from the Emprendedor table (arts. 97.3, 97.6). See the RIMPE rows below. The exclusions and the 3-year term are in [ecuador-income-tax](ecuador-income-tax.md).
- **Business trusts and funds**: trusts that run a business or a going concern pay like companies. Trusts that do not, investment funds and complementary funds are exempt if they meet art. 9(15), but file an informative return (art. 42.1).
- **Out of scope**: hydrocarbon and mining contract regimes (they carry their own rules), transfer pricing detail, and treaty rates.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| General rate: resident companies, branches and permanent establishments | 25% of the base | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 37) |
| Surcharge: the company failed to report its shareholders, or a holder in the ownership chain is in a tax haven, lower-tax jurisdiction or preferential regime and the beneficial owner is an Ecuadorian tax resident | +3 points (28%) | 2026 | same (art. 37(a), (b)) |
| Surcharge where the affected holdings are 50% or more of capital | 28% on the whole base | 2026 | same (art. 37); https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 51) |
| Surcharge where the affected holdings are under 50% | rate + 3 points on the affected percentage of the base; normal rate on the rest; ownership read at 31 December | 2026 | same (RLRTI art. 51) |
| Micro and small companies, and habitual exporters (exporters only if employment is kept or increased in the year) | −3 points (22%) | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI, unnumbered article after art. 37.3) |
| Habitual exporter test | net exports at least 25% of net sales, and at least 6 exports in 6 different months (3 in 3 months for cyclical production; not needed for pure service exporters); not for crude oil or other non-renewable resources | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI, unnumbered article on exportador habitual) |
| New companies set up since the Ley Orgánica para el Desarrollo Económico y Sostenibilidad Fiscal (RO 587, 29 Nov 2021), and new investment by existing companies | −3 points on income from the new investment, up to 15 years from the first year of profit from it; total reduction capped at the amount invested; a separate cost centre is required | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 37.2) |
| Same, with an investment contract under the COPCI | up to −5 points, for the contract term; capped at the amount invested | 2026 | same (art. 37.3) |
| Reinvestment of profits in Ecuador in accredited disability, sports, culture, science or technology programmes | percentage reduction of 10% for programmes rated priority, 8% for the others, on the reinvested profit, under the Reglamento | 2026 | same (art. 37.1); computation in RLRTI art. 51 |
| Tax stability (estabilidad tributaria) | general-regime income tax frozen for 5 years in exchange for +2 points; the company must at least meet the SRI's effective tax rate for its sector; it may give it up, with no refund | 2026 | same (LRTI, unnumbered article after art. 37) |
| Loans by a company to its shareholders, or non-commercial loans to related parties | treated as advance dividends: withhold at the company rate on the amount; declare and pay the next month; credit against the company's own tax | 2026 | same (arts. 37, 39.2(6)) |

**Dividends (LRTI art. 39.2, as replaced from 1 September 2025).** A single income tax on the amount distributed, in the year of distribution. The distributing company withholds 100% of it when the shareholders' meeting resolves to distribute, whenever the dividend is actually paid.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Dividend to a resident individual, or to anyone other than the cases below | 12% single tax | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 39.2) |
| Dividend to a resident company or an Ecuadorian permanent establishment of a non-resident company | not taxed | 2026 | same (art. 39.2(1)); also exempt under art. 9(1) |
| Dividend to a non-resident | 10%; 12% where the distributing company's beneficial owner is an Ecuadorian tax resident | 2026 | same (art. 39.2(4)) |
| A tax-haven holder at any level of the chain and an Ecuadorian-resident beneficial owner | 14% | 2026 | same (art. 39.2(4)) |
| Company failed to report its ownership | 14% on the dividends linked to the failure | 2026 | same (art. 39.2(5)) |
| Resident individual's exempt band | 3 salarios básicos unificados per distributing company per year: 3 × USD 482 = USD 1,446 for 2026 | 2026 | same (art. 39.2(7)); SBU at https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf |
| Dividends received from abroad by a resident company or individual | added to taxable income at the normal rate or table, with credit for foreign tax up to the Ecuadorian tax | 2026 | same (art. 39.2(8)) |

**Payment on undistributed profits (pago a cuenta, LRTI art. 39.2.1).** Resident companies and permanent establishments that, by 31 July, have not distributed the profits accumulated from earlier years pay one rate on **100%** of that balance, chosen by the band the balance falls in. The first band is not deducted.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Undistributed balance up to USD 100,000 | 0% (no return needed) | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/8ef5341a-c40b-4ab5-a49d-fbd257d381d2/FORO_DIVIDENDOS.pdf (SRI, table under art. 39.2.1) |
| USD 100,000.01 to 1,000,000 | 0.75% | 2026 | same |
| USD 1,000,000.01 to 10,000,000 | 1.25% | 2026 | same |
| USD 10,000,000.01 to 100,000,000 | 1.75% | 2026 | same |
| USD 100,000,000.01 to 500,000,000 | 2.25% | 2026 | same |
| Above USD 500,000,000 | 2.50% | 2026 | same |

**Other company-level rates.**

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Gain on direct or indirect sale of shares or similar rights in Ecuadorian companies or permanent establishments, by residents or non-residents | single income tax 10%, at the time of sale; not triggered by restructurings, mergers or spin-offs where the beneficial owners and their proportions stay the same | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI, unnumbered article after art. 37 on enajenación de acciones) |
| Failure to report, or errors in reporting, a share sale (by the Ecuadorian company) | fine of 5% of the real value of the transaction | 2026 | same (unnumbered article after art. 40-A) |
| Payments abroad (services occasionally provided in Ecuador and other payments that are not dividends), no specific rate | withholding at the company rate, 25%; 37% to a recipient in a tax haven, lower-tax jurisdiction or preferential regime | 2026 | same (art. 39); https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/272ca6a9-d679-4b4e-8da0-fb4671cf5f8f/NAC-DGERCGC26-00000009_Ret_IR.pdf (art. 4) |
| Payments abroad by registered tourism providers for shows and cultural events held in Ecuador | 15% withholding; company rate if the recipient is in a tax haven | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (art. 39.3) |
| Voluntary advance (anticipo voluntario) | 50% of the prior year's tax due less that year's withholdings; credit against the year's tax | 2026 | same (art. 41) |
| RIMPE company, gross income up to USD 20,000 | USD 60 (the fracción básica of the first Emprendedor band) | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 229) |
| RIMPE company, gross income USD 20,000 to 300,000 | Emprendedor table: USD 60 + 1% over 20,000; USD 360 + 1.25% over 50,000; USD 672.50 + 1.50% over 75,000; USD 1,047.50 + 1.75% over 100,000; USD 2,797.52 + 2% over 200,000; no surcharge and no reduction | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf (Decreto Ley 742 art. 12, replacing LRTI art. 97.6); RLRTI art. 229 |

**Withholding at source on local payments (SRI Resolution NAC-DGERCGC26-00000009, from 1 March 2026).** The payer withholds when it pays or credits, whichever is first (art. 8). The withholding is a credit for the recipient. Selected rates:

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Interest paid to banks and supervised entities (other than interbank); purchases from RIMPE Negocios Populares with a pre-printed receipt | 0% | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/272ca6a9-d679-4b4e-8da0-fb4671cf5f8f/NAC-DGERCGC26-00000009_Ret_IR.pdf (art. 2(1)) |
| Passenger and cargo transport; farm produce bought from the producer; purchases from RIMPE Emprendedores | 1% | 2026 | same (art. 2(2)) |
| Farm produce bought from non-producer traders | 1.75% | 2026 | same (art. 2(3)) |
| Movable goods; electricity; insurance premiums; construction; leasing instalments; unlisted share sales; interbank interest; card payments to merchants | 2% | 2026 | same (art. 2(4)) |
| Labour-intensive services by individuals; interest and financial returns paid by Ecuadorian companies or individuals; media and advertising agencies; public-sector interest; purchase settlements (liquidaciones de compra) | 3% | 2026 | same (art. 2(5)) |
| Professional services and commissions of resident companies and permanent establishments | 5% | 2026 | same (art. 2(6)) |
| Fees of resident individuals for intellectual services, teaching and notarial work; image rights and influencers; royalties; listed share gains; rent of real estate | 10% | 2026 | same (art. 2(7)) |
| Any payment with no specific rate | 3% | 2026 | same (art. 3) |

## The base

1. **Start from accounting profit**, kept in US dollars by double entry under accepted accounting principles (LRTI art. 20). The financial statements filed with the Superintendencia are the same ones used for tax (art. 21).
2. **Base** = all taxable ordinary and extraordinary income, less returns, discounts, costs, expenses and deductions attributable to it (art. 16). Remove exempt income (art. 9). The main exemption for companies is dividends from resident companies (art. 9(1)); capitalising profits is not a distribution.
3. **Deductions**: costs and expenses made to obtain, maintain and improve taxable Ecuadorian-source income, with valid sales receipts (art. 10). Amortisation of assets that accounting spreads over more than one year is deductible on the terms of the Reglamento (art. 12). Where tax and accounting rules differ, tax rules prevail; deferred tax is recognised only where the Reglamento allows (art. 10, unnumbered article).
4. **Losses** (art. 11): set off against taxable profit of the next 5 years, at most 25% of each year's profit. On liquidation or end of activity in Ecuador, the loss of the last 5 years is deductible in full in the final year. Losses on sales of assets or shares between related parties, or with a shareholder and their close family, are not deductible. Shareholders cannot use the company's losses.
5. **Apply the rate.** Work out the rate from the rates table: 25%, adjusted by the surcharge or reductions. With a surcharge below 50%, split the base (RLRTI art. 51). With reinvestment, apply the reduced rate to the reinvested part and the normal rate to the rest. Where a reduction applies, the surcharge is computed on the reduced rate.
6. **Subtract credits**: withholdings suffered (comprobantes de retención), the voluntary advance, and any pago a cuenta that may be set off. The result is the tax payable or the credit balance (art. 47).

**Pago a cuenta base (RLRTI, unnumbered article after art. 126).** Start with the prior year's profit or loss (accounting result less employee profit share, income tax expense and the legal reserve). Add or subtract accumulated profits or losses of earlier years. Subtract dividends distributed between 1 January and 31 July. Subtract profits capitalised in that period. Add or subtract the equity-method valuation adjustment of the prior period. Financial and insurance institutions leave out profits their regulator bars them from distributing. Investment funds and trusts are outside it, and so is the State's share of state and mixed companies.

**What happens to the pago a cuenta.** It is a credit:

- against the withholding on a later dividend paid out of those profits;
- or against income tax from the year of distribution or capitalisation;
- in the same proportion as the profits distributed or capitalised.

Any part not set off can be refunded. If the company neither distributes nor capitalises in the next two tax years, the credit is lost and booked as a non-deductible expense (art. 39.2.1).

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Annual return and payment, tax year 2026 | window opens 1 February 2027; due by ninth digit of the RUC: 1 = 10 April, 2 = 12, 3 = 14, 4 = 16, 5 = 18, 6 = 20, 7 = 22, 8 = 24, 9 = 26, 0 = 28 April 2027 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 72(1)) |
| Special taxpayers (contribuyentes especiales) | by 9 April, whatever the ninth digit; moved to the previous business day if a holiday | https://www.sri.gob.ec/impuesto-renta |
| State institutions and public companies; Galápagos | up to the 20th of the following month; Galápagos up to the 28th of the following month | RLRTI art. 72, same URL as the first row |
| Due date on a holiday or rest day | moves to the next business day, unless that falls in the next month; then it moves back to the last business day of the due month | same |
| RIMPE company | the SRI calendar for tax year 2025 set 10 to 28 April 2026 by ninth digit | https://www.sri.gob.ec/declaracion-impuesto-a-la-renta-2025 |
| Pago a cuenta on undistributed profits | August, by ninth digit of the RUC (special taxpayers by the 11th); or 3 equal instalments in August, September and October; the choice cannot be changed by an amended return; no payment plan is granted | RLRTI, unnumbered article after art. 126; https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=57cb3aec-9834-4e68-8d44-c8ee1e422afa&nombre=NAC-DGERCGC26-00000026.pdf (Res. NAC-DGERCGC26-00000026) |
| Withholding on advance dividends (shareholder loans) | declared and paid the month after | LRTI art. 39.2(6) |
| Early return when activity ends during the year | within 30 days of ending the activity, then RUC cancellation | RLRTI art. 74; LRTI art. 40 |

**How to file, step by step.**

1. Close the books, prepare the financial statements and the tax reconciliation (conciliación tributaria): accounting profit, less employee profit share, plus non-deductible expenses, less exempt income, less loss carry-forward. The result is the base.
2. Check the ownership at 31 December and the shareholder report filed with the SRI. This decides the surcharge.
3. File the annual company return in SRI en línea by the ninth-digit date in April 2027: income, costs, reconciliation, rate applied, tax due, withholdings, advance and balance.
4. Pay the balance by the same date. A late return must include the interest and fine (RLRTI art. 72).
5. When the shareholders resolve a dividend, withhold the single tax on the date of the resolution and pay it with the monthly withholding return.
6. By 31 July, decide whether to distribute or capitalise. If profits from earlier years remain undistributed above USD 100,000, file and pay the pago a cuenta in August on the form "Formulario de Pago de Anticipo Mínimo de Impuesto a la Renta, Autorretenciones de Grandes Contribuyentes y Pago a Cuenta Sobre las Utilidades no Distribuidas". Use code 1077 to pay at once or 1078 for instalments (Res. NAC-DGERCGC26-00000026).

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Late filing with tax due | 3% of the tax due per month or part of a month late; cap 100% of the tax | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 100) |
| Late filing with no tax due | 0.1% of gross income per month or part of a month; cap 5% of that income | same |
| Fine not self-assessed and paid | collected by the SRI increased by 20% | same |
| Interest on late tax | Banco Central del Ecuador 90-day active reference rate, by quarter, per month (part month counts as a full month) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf (CT art. 21) |
| Interest on tax assessed by the SRI | 1.3 times that rate | same (CT art. 21) |
| Surcharge on tax assessed by the SRI | 20% of the principal | same (CT art. 90) |
| Share-sale reporting failure | 5% of the transaction's real value | LRTI, unnumbered article after art. 40-A |

## Cross-border points

- **Non-resident shareholders**: dividends at 10%, or 12% or 14% as in the dividend table (art. 39.2). Treaty rates may apply (art. 39.2, last paragraph). Before applying a treaty, the payer must check the recipient is resident in the other state (Res. NAC-DGERCGC26-00000009 art. 9).
- **Payments abroad** without a specific rate: 25% withholding, 37% to tax havens (art. 39).
- **Indirect sale** of an Ecuadorian company through a foreign parent is caught when, at any time in the year, the Ecuadorian company is worth 20% or more of the foreign company's real value, and the sales by the same seller and related parties in the year or the previous 12 months exceed 300 fracciones básicas (USD 3,662,400 for 2026), or 1,000 (USD 12,208,000) where the sale is no more than 10% of the capital. These thresholds do not apply where an Ecuadorian resident is the beneficial owner or the company sold is in a tax haven. The Ecuadorian company is the substitute taxpayer, except for stock-exchange sales (art. 39).
- **Foreign-source income** of a resident company is taxed with credit for foreign tax; foreign dividends as in the dividend table (art. 39.2(8)).
- **Transfer pricing** between related parties (the related-party definition follows art. 4): refer to a transfer pricing skill.

## Two worked examples that recompute

### Example 1: base split for a partial tax-haven holding, then a dividend

Andes S.A. is resident in Ecuador and is not a micro or small company. Its 2026 base after the tax reconciliation is USD 400,000. At 31 December 2026, 40% of its shares are held through a company in a tax haven whose beneficial owner is an Ecuadorian resident. The other 60% is held by Ecuadorian residents directly. Withholdings suffered in 2026 were USD 30,000.

- Affected part: 40% × 400,000 = 160,000 at 28% = **USD 44,800**. Rest: 60% × 400,000 = 240,000 at 25% = **USD 60,000** (RLRTI art. 51).
- Tax due: **USD 104,800**. Less withholdings: **USD 74,800 payable** by the ninth-digit date in April 2027.
- In May 2027 it distributes USD 100,000 to a resident individual holding directly. The company withholds 12% × (100,000 − 1,446) = **USD 11,826.48**, using the 2026 band for illustration; the band for the year of distribution is 3 times that year's SBU. Because the 40% chain has a tax-haven holder and an Ecuadorian beneficial owner, the dividends paid along that chain bear 14% (art. 39.2(4)).

```oa-check
name: EC CIT 2026, 40% tax-haven chain, base USD 400,000, dividend withholding
inputs:
  base: 400000
  affected_share: 0.40
  withheld: 30000
  dividend: 100000
  sbu: 482
steps:
  - affected_tax: base * affected_share * 0.28
  - normal_tax: base * (1 - affected_share) * 0.25
  - tax_due: affected_tax + normal_tax
  - payable: tax_due - withheld
  - exempt_band: 3 * sbu
  - dividend_tax: round((dividend - exempt_band) * 0.12, 2)
expected:
  affected_tax: 44800
  normal_tax: 60000
  tax_due: 104800
  payable: 74800
  exempt_band: 1446
  dividend_tax: 11826.48
```

### Example 2: distribute by 31 July or keep the profits? (a decision worked both ways)

Pacífico Cía. Ltda. is resident. On 31 July 2026 it has USD 2,000,000 of profits from earlier years, worked out as in The base, not yet distributed. Its sole shareholder is a resident individual.

- **Keep the profits.** The balance is in the USD 1,000,000.01 to 10,000,000 band, so the pago a cuenta is 1.25% × 2,000,000 = **USD 25,000**, on the whole balance with no first-band deduction. It is due in August 2026, or in 3 instalments of USD 8,333.33 (August to October). If the company distributes or capitalises within the next two tax years, the USD 25,000 is a credit against the dividend withholding or the company's income tax. If it does neither, the USD 25,000 is lost and becomes a non-deductible expense.
- **Distribute all of it before 31 July.** No pago a cuenta. The company withholds the single dividend tax: 12% × (2,000,000 − 1,446) = **USD 239,826.48**, final for the shareholder.
- **The figure that decides** is when the shareholder needs the cash. Keeping costs USD 25,000 now. That is recovered in full if the profits are paid out within two years, because the dividend tax then falls by the same amount. It is lost if they are not. Paying out now costs the full USD 239,826.48 at once. Distributing USD 1,900,001 or more by 31 July would leave at most USD 99,999 undistributed, in the 0% band, so no pago a cuenta at all.

```oa-check
name: EC 2026, undistributed profits USD 2,000,000, keep or distribute
inputs:
  undistributed: 2000000
  sbu: 482
steps:
  - pago_a_cuenta: undistributed * 0.0125
  - instalment: round(pago_a_cuenta / 3, 2)
  - dividend_tax: round((undistributed - 3 * sbu) * 0.12, 2)
  - dividend_tax_after_credit: dividend_tax - pago_a_cuenta
  - max_kept_for_zero_band: 100000 - 1
expected:
  pago_a_cuenta: 25000
  instalment: 8333.33
  dividend_tax: 239826.48
  dividend_tax_after_credit: 214826.48
  max_kept_for_zero_band: 99999
```

## Ask the client first

1. What is the entity (company, branch, permanent establishment, trust, fund), and is it registered as RIMPE with gross income up to USD 300,000?
2. Who holds the shares at 31 December, at every level up to the beneficial owner, was the ownership report filed, and is any holder in a tax haven, lower-tax jurisdiction or preferential regime?
3. Is it a micro or small company or a habitual exporter, does it have new investments, an investment contract or a tax-stability election, or reinvestment in accredited programmes?
4. The accounting result, employee profit share, non-deductible items, exempt income and losses of the last 5 years.
5. Accumulated undistributed profits on 31 July and any distributions or capitalisations planned; any loans to shareholders or related parties.
6. Withholdings suffered in the year, any voluntary advance, and payments made abroad.

## Sources

| Source | URL | Read on |
|---|---|---|
| LRTI, SRI codification, last reform 2026-04-01: arts. 2, 4.2, 9(1), 9(15), 10, 11, 12, 16, 19-21, 37 with its unnumbered articles, 37.1-37.3, 39, 39.2, 39.2.1, 39.3, 40, 40-A and the next article, 41, 42.1, 47, 97.3, 97.6, 98, 100 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| RLRTI, SRI codification, last reform 2025-11-18: arts. 37, 51, 72, 74, 229, the exportador habitual article and the pago a cuenta articles after art. 126 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| Ley Orgánica de Transparencia Social (RO third Supl. 112, 28 Aug 2025), SRI copy: new arts. 39.2 and 39.2.1 and the final provisions (application from the first day of the month after publication) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/c901c5dc-4f1f-411c-a02a-84432bfef788/Ley%20Org%C3%A1nica%20de%20Transparencia%20Social.pdf | 2026-11-11 |
| SRI, presentation on the dividend rules and the pago a cuenta table (the table in the law is printed as an image in RO Supl. 112, page 50) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/8ef5341a-c40b-4ab5-a49d-fbd257d381d2/FORO_DIVIDENDOS.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC26-00000026 (14 Jul 2026): form, codes 1077 and 1078, single payment or 3 instalments | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=57cb3aec-9834-4e68-8d44-c8ee1e422afa&nombre=NAC-DGERCGC26-00000026.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC26-00000009 (27 Feb 2026): withholding percentages from 1 Mar 2026, arts. 2-4, 8, 9; repeals NAC-DGERCGC24-00000008 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/272ca6a9-d679-4b4e-8da0-fb4671cf5f8f/NAC-DGERCGC26-00000009_Ret_IR.pdf | 2026-11-11 |
| Decreto Ley 742 (RO Supl. 335, 20 Jun 2023), SRI copy: art. 12, RIMPE tables | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf | 2026-11-11 |
| Código Tributario, SRI codification, last modification RO 372 of 10 Aug 2023: arts. 21 and 90 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf | 2026-11-11 |
| SRI, Impuesto a la Renta page: company rate and its adjustments, deadlines, special taxpayers | https://www.sri.gob.ec/impuesto-renta | 2026-11-11 |
| SRI, Declaración Impuesto a la Renta 2025 page: RIMPE company calendar (April) | https://www.sri.gob.ec/declaracion-impuesto-a-la-renta-2025 | 2026-11-11 |
| Ministerio del Trabajo, Acuerdo Ministerial MDT-2025-195: SBU USD 482 from 1 Jan 2026 | https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf | 2026-11-11 |

Not yet confirmed:
- the pago a cuenta table was read from the SRI presentation, not from the image in RO Supl. 112 page 50;
- the August day-by-digit table for the pago a cuenta (an image in RO Supl. 153 of 28 Oct 2025, page 54);
- whether the art. 37.1 reinvestment reduction of 10% or 8% means points or a share of the rate (the SRI page says "10% de la tarifa");
- the size thresholds that make a company micro or small (set outside the LRTI);
- the exemption for new microenterprises in the Reglamento;
- whether any constitutional challenge to the Ley Orgánica de Transparencia Social is pending;
- whether art. 39's reference to a progressive table for non-residents' share gains still applies next to the 10% single tax;
- the employee profit share percentage (Código del Trabajo, not read);
- treaty and Andean Community Decision 578 rates;
- form numbers for the 2026 company return.
