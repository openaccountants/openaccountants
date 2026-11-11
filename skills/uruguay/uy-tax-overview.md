---
name: uy-tax-overview
description: "Uruguay tax overview and router for 2026: which Uruguay skill to load for a question and in what order, with the few facts that apply across all of them. Covers the calendar tax year, the peso, the two collectors (DGI for taxes, BPS for social security and wage IRPF), the source principle and the 2026 change for residents' foreign capital income, the BPC of UYU 6,864, and the wealth tax (Impuesto al Patrimonio: 1.5% for companies, 2.8% for banks, 3% for low-tax entities without a permanent establishment), which has no separate skill. Routes to IRPF, IRAE, IVA, IRNR and treaties, transfer pricing, payroll, BPS contributions and company formation. Trigger on: Uruguay taxes, sistema tributario uruguayo, which taxes in Uruguay, DGI BPS, Impuesto al Patrimonio, Uruguay tax overview 2026."
version: 0.1
jurisdiction: UY
tax_year: 2026
last_updated: 2026-11-11
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Uruguay tax overview and router, 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill sends a Uruguay question to the right skill. The rates live in those skills; this page keeps only the facts every Uruguay answer needs and the wealth tax, which no other skill covers.

**Facts that apply to every Uruguay skill, 2026**

| Item | Figure | Source URL |
|---|---|---|
| Tax year | Calendar year for individuals; IRPF and IRNR arise on 31 December | https://www.impo.com.uy/bases/todgi-2023/8-2024 (T8 art. 8); see uruguay-income-tax for T7 |
| Currency | Uruguayan peso (UYU); SA capital must be stated in pesos | https://www.impo.com.uy/bases/leyes/16060-1989 (art. 279) |
| BPC (Base de Prestaciones y Contribuciones), the unit most thresholds use | UYU 6,864 a month from 1 January 2026 | https://www.impo.com.uy/bases/decretos/11-2026 (art. 1) |
| Tax collector | Dirección General Impositiva (DGI) | https://www.impo.com.uy/bases/todgi-2023/7-2024 (T7 art. 1, for IRPF); T8 art. 20 and T14 for IRNR and the wealth tax |
| Social security collector, also collects IRPF withheld from wages for DGI | Banco de Previsión Social (BPS) | https://www.impo.com.uy/bases/todgi-2023/7-2024 (T7 art. 1); https://www.bps.gub.uy/10323/impuesto-a-la-renta-de-las-personas-fisicas-irpf.html |
| Wealth tax (Impuesto al Patrimonio), entities taxed under IRAE rules | 1.5% of taxable net worth | https://www.impo.com.uy/bases/todgi-2023/14-2024 (T14 art. 53 D) |
| Wealth tax, banks, financial houses and art. 62 entities | 2.8% | same (art. 53 C) |
| Wealth tax, entities resident or located in low or no-tax jurisdictions without a permanent establishment in Uruguay | 3% | same (art. 53 E) |
| Wealth tax, bearer bonds and similar securities | 3.5% | same (art. 53 B) |

## The method, step by step

1. **Who is asking, and are they resident?** Residence rules for individuals (more than 183 days, or centre of interests) and entities (formed under Uruguayan law) are in [uy-cross-border](uy-cross-border.md) and [uruguay-income-tax](uruguay-income-tax.md). A non-resident without a permanent establishment goes to step 6.
2. **Source.** Uruguay taxes income from activities, assets or rights used in Uruguay. From 1 January 2026 a resident individual is also taxed on foreign capital yields and gains (see [uruguay-income-tax](uruguay-income-tax.md)). Companies' foreign income is in [uy-corporate-income-tax](uy-corporate-income-tax.md).
3. **Pick the tax and load its skill:**

| Question | Skill |
|---|---|
| Individual's income tax (IRPF): wages, fees, rents, interest, dividends, annual return | [uruguay-income-tax](uruguay-income-tax.md) |
| Company or business income tax (IRAE), payments on account, IMCD | [uy-corporate-income-tax](uy-corporate-income-tax.md) |
| VAT (IVA): rates, registration, returns | [uruguay-iva](uruguay-iva.md) |
| Running payroll: gross to net, IRPF withholding, BPS nómina | [uruguay-payroll](uruguay-payroll.md) |
| BPS contributions alone, including owners without employees | [uruguay-social-contributions](uruguay-social-contributions.md) |
| Non-residents (IRNR), withholding on payments abroad, treaties | [uy-cross-border](uy-cross-border.md) |
| Related-party pricing, form 3001 | [uy-transfer-pricing](uy-transfer-pricing.md) |
| Choosing and forming an SAS, SRL or SA, beneficial owners, annual accounts | [uy-company-formation](uy-company-formation.md) |
| Wealth tax of a company | This page, step 4 |

4. **Wealth tax (Impuesto al Patrimonio) of a company.** Entities listed in Título 4 art. 12 (the IRAE taxpayers, with exceptions such as monotributo contributors) pay an annual tax on their taxable net worth (T14 art. 4 B). Multiply the taxable net worth by the rate for its class in the table above; the Executive may cut the rates by up to 50% (art. 54). Valuation rules and the individuals' scale, which has been reduced each year since 2008 under art. 53 A, are not covered here.
5. **Several taxes at once.** A company with staff needs, in order: [uy-company-formation](uy-company-formation.md), [uruguay-payroll](uruguay-payroll.md), [uruguay-iva](uruguay-iva.md), [uy-corporate-income-tax](uy-corporate-income-tax.md), and [uy-transfer-pricing](uy-transfer-pricing.md) if it deals with related parties. A non-resident investor needs [uy-cross-border](uy-cross-border.md) first, then the skill for the income type.
6. **Non-resident without a permanent establishment**: load [uy-cross-border](uy-cross-border.md); it routes back to IRAE if there is a permanent establishment.

## Worked cases

### Case 1: a company's wealth tax for 2026

An SA (an IRAE taxpayer, not a bank, not in a low-tax jurisdiction) closes 2026 with taxable net worth of UYU 10,000,000 after the T14 valuation rules. Its wealth tax is 1.5% x 10,000,000 = UYU 150,000. If the same net worth belonged to a bank, the rate would be 2.8% (UYU 280,000); an entity of a low-tax jurisdiction with no permanent establishment would pay 3% (UYU 300,000).

```oa-check
name: Impuesto al Patrimonio on UYU 10,000,000 of taxable net worth, three classes
inputs:
  net_worth: 10000000
steps:
  - company: net_worth * 0.015
  - bank: net_worth * 0.028
  - low_tax_no_pe: net_worth * 0.03
expected:
  company: 150000.00
  bank: 280000.00
  low_tax_no_pe: 300000.00
```

## When to refuse or refer

- **Individuals' wealth tax**: the 2026 rates and the mínimo no imponible are not in any Uruguay skill yet; refer to DGI or a contador público.
- **Free-zone users, rural (IMEBA), monotributo, IMESI, IASS (pensions)**: no Uruguay skill covers them; say so and refer.
- **Disputes, DGI audits, payment plans or arrears**: refer to a contador público.
- **Sanctions or embargo screening**: not covered.

## Sources

| Source | URL | Read on |
|---|---|---|
| Decreto 11/026, art. 1 read: BPC UYU 6,864 from 1 January 2026 | https://www.impo.com.uy/bases/decretos/11-2026 | 2026-11-11 |
| Texto Ordenado 2023, Título 14 Impuesto al Patrimonio, IMPO text: arts. 1 to 4, 53, 54 and 57 read | https://www.impo.com.uy/bases/todgi-2023/14-2024 | 2026-11-11 |
| Texto Ordenado 2023, Título 7 IRPF, IMPO text: art. 1 (DGI and BPS roles) read | https://www.impo.com.uy/bases/todgi-2023/7-2024 | 2026-11-11 |
| Texto Ordenado 2023, Título 8 IRNR, IMPO text: arts. 3, 4 and 8 read (residence, tax year) | https://www.impo.com.uy/bases/todgi-2023/8-2024 | 2026-11-11 |
| Ley 16.060, art. 279 read (capital in pesos) | https://www.impo.com.uy/bases/leyes/16060-1989 | 2026-11-11 |
| BPS, IRPF page read (BPS collects wage IRPF for DGI) | https://www.bps.gub.uy/10323/impuesto-a-la-renta-de-las-personas-fisicas-irpf.html | 2026-11-11 |
| DGI, Estado de los Convenios para evitar la Doble Imposición, read as the DGI page for treaties | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/convenios-para-evitar-doble-imposicion | 2026-11-11 |

Not yet confirmed: the 2026 individuals' wealth tax rates after the yearly reductions, and the mínimo no imponible; whether the Executive has used art. 54 to cut any wealth tax rate for 2026; the wealth tax return form and due dates; company fiscal years other than the calendar year (in uy-corporate-income-tax).

> Contributed by Michael Cutajar.
