---
name: ecuador-income-tax
description: "Ecuador personal income tax (impuesto a la renta de personas naturales) for tax year 2026 under the Ley de Régimen Tributario Interno (LRTI) and its Reglamento. Covers residence (183 days, centre of economic interests, temporary tax residence), the 2026 progressive table from SRI Resolution NAC-DGERCGC25-00000043 (0% to 37%, exempt band USD 12,208), the rebate for gastos personales (18% of the lower of expenses and 7 to 20 canastas, canasta USD 821.80), exempt income including the 13th and 14th salaries and the over-65 and disability exemptions, employment income and employer withholding, the RIMPE Negocio Popular and Emprendedor tables, non-residents at 25%, the inheritance and gift table, filing by ninth digit of the RUC or cédula, penalties and interest. Trigger on: impuesto a la renta personas naturales 2026, tabla impuesto a la renta 2026, gastos personales, rebaja gastos personales, cargas familiares, RIMPE negocio popular, RIMPE emprendedor, noveno dígito, SRI en línea, Ecuador "
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ecuador-income-tax"
  jurisdiction: "EC"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Ecuador: personal income tax for individuals and the self-employed (2026) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers the annual income tax of a natural person (persona natural) for the 2026 calendar year: employees, self-employed professionals and traders, people taxed under RIMPE, and non-residents with Ecuadorian-source income. It links to the other Ecuador skills and does not repeat them:

- [ec-corporate-income-tax](ec-corporate-income-tax.md): companies (sociedades), including RIMPE companies.
- [ecuador-iva](ecuador-iva.md): IVA, including how a RIMPE trader charges it.
- [ecuador-social-contributions](ecuador-social-contributions.md): IESS contribution rates (employee, employer, voluntary affiliate).
- [ecuador-payroll](ecuador-payroll.md): the employer's side of payroll, including the 13th and 14th salaries and fondos de reserva.

**Which text of the law.** The LRTI codification published by the SRI's Dirección Nacional Jurídica with last reform 1 April 2026, and the Reglamento para la Aplicación de la LRTI (RLRTI) with last reform 18 November 2025. Article 36(a) sets the table; under that article the table is indexed each year to the urban CPI at 30 November, and the 2026 table is SRI Resolution **NAC-DGERCGC25-00000043**, signed 29 December 2025, published in Registro Oficial Suplemento 194 of 30 December 2025 and applicable from 1 January 2026 (CPI variation 1.0534712934405%). Interest and the 20% surcharge come from the Código Tributario (CT).

**Quick reference (2026).** Tax year: calendar year 2026 (LRTI art. 7). Currency: US dollar. Exempt band: USD 12,208. Top rate: 37% above USD 109,956. Gastos personales rebate: 18% of the lower of expenses and canasta USD 821.80 times 7 (no dependants) up to 20. Return due: 10 to 28 March 2027 by the ninth digit of the RUC or cédula. RIMPE: due by the ninth digit in May 2027 under the SRI calendar, and by June at the latest under the law.

## Who this applies to

- **Tax residents** are taxed on worldwide income (LRTI art. 2). A natural person is resident for a tax year if any of these holds (LRTI art. 4.1):
  - (a) 183 calendar days or more in Ecuador, consecutive or not, in the same tax year, including sporadic absences;
  - (b) 183 days or more within a 12-month period spanning two tax years, unless they prove tax residence elsewhere for that period and that their main centre of activities or economic interests is there;
  - (c) their main centre of activities or economic interests is in Ecuador. That is so when Ecuador gave them the largest share of income in the last 12 months, or holds the largest share of their assets. It is presumed (rebuttable) when they hold assets in Ecuador worth over USD 1 million and have ever been an Ecuadorian tax resident, national or permanent resident, or legal representative of an Ecuadorian company or permanent establishment;
  - (d) they did not stay more than 183 days in any other country in the year.
- **Moving to a tax haven.** A resident who later claims residence in a tax haven, lower-tax jurisdiction or preferential regime stays resident in Ecuador for the next four tax years unless they prove 183 days there in one tax year and that their centre of interests is there (art. 4.1(b)).
- **Temporary tax residence** (residencia fiscal temporal, art. 4.1, unnumbered article). A person who has never been an Ecuadorian tax resident may opt for 5 years of tax on Ecuadorian-source income only, if they invest at least USD 150,000 in real estate or productive activities in Ecuador (kept for at least 5 years) or prove foreign-source income of at least USD 2,500 a month (and join social security while in the country). The conditions must be met between day 1 and day 120 after entering Ecuador.
- **Non-residents** are taxed only on Ecuadorian-source income (art. 4.1, last paragraphs of (c); art. 8), mostly by withholding. See Cross-border points.
- **Employees** (relación de dependencia): the employer withholds monthly (RLRTI art. 104).
- **Self-employed and others under the general regime**: professionals, commission agents, artisans, landlords and other independent workers file an annual return.
- **RIMPE individuals**: persons registered in the RUC under the Régimen Simplificado para Emprendedores y Negocios Populares pay on gross income from a separate table (LRTI arts. 97.1 to 97.10).
- **Spouses** are taxed separately. Income of the conjugal partnership (sociedad conyugal) is split equally, but employment income and professional income go to the spouse who earns it, and business income to the spouse who runs the business (art. 5).
- **Out of scope here**: companies and permanent establishments (ec-corporate-income-tax), IVA (ecuador-iva), IESS contributions (ecuador-social-contributions).

## Rates, bands and thresholds

**General regime, Tabla No. 1, tax year 2026.** Tax = tax on the fracción básica + (base − fracción básica) × rate on the excess (LRTI art. 36(a)).

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Base USD 0 to 12,208 | 0% | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf (Res. NAC-DGERCGC25-00000043 art. 2) |
| Base USD 12,208 to 15,549 | USD 0 + 5% of the excess over 12,208 | 2026 | same |
| Base USD 15,549 to 20,188 | USD 167 + 10% of the excess over 15,549 | 2026 | same |
| Base USD 20,188 to 26,700 | USD 631 + 12% of the excess over 20,188 | 2026 | same |
| Base USD 26,700 to 35,136 | USD 1,412 + 15% of the excess over 26,700 | 2026 | same |
| Base USD 35,136 to 46,575 | USD 2,678 + 20% of the excess over 35,136 | 2026 | same |
| Base USD 46,575 to 62,005 | USD 4,965 + 25% of the excess over 46,575 | 2026 | same |
| Base USD 62,005 to 82,679 | USD 8,823 + 30% of the excess over 62,005 | 2026 | same |
| Base USD 82,679 to 109,956 | USD 15,025 + 35% of the excess over 82,679 | 2026 | same |
| Base above USD 109,956 | USD 24,572 + 37% of the excess over 109,956 | 2026 | same |
| Same table as consolidated into LRTI art. 36(a) | as above | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 36(a)) |

**Gastos personales rebate.** Rebate = 18% × the lower of (a) personal expenses declared for the year and (b) the canasta familiar básica of January of the year times the number of canastas below (LRTI, unnumbered article on the rebate after art. 10; RLRTI art. 34). The rebate reduces the tax due (impuesto causado) before tax credits; any part above the tax due is lost and is not refunded.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Canasta familiar básica, January 2026 | USD 821.80 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ea002a89-17d8-4cdf-be42-affedbe3f8d8/BOLET%C3%8DN%20006%20-%20SRI%20HABILITA%20LA%20PROYECCI%C3%93N%20DE%20GASTOS%20PERSONALES%202026%20PARA%20REDUCIR%20EL%20IMPUESTO%20A%20LA%20RENTA.pdf (SRI Boletín NAC-COM-26-006) |
| Rebate rate | 18% of the lower value | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI, rebate article after art. 10, literals a and b) |
| No cargas familiares: 7 canastas | cap USD 5,752.60; maximum rebate USD 1,035.47 | 2026 | same (literal a); canasta from SRI Boletín NAC-COM-26-006 |
| 1 carga familiar: 9 canastas | cap USD 7,396.20; maximum rebate USD 1,331.32 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf (Decreto Ley 742, table in literal b) |
| 2 cargas: 11 canastas | cap USD 9,039.80; maximum rebate USD 1,627.16 | 2026 | same |
| 3 cargas: 14 canastas | cap USD 11,505.20; maximum rebate USD 2,070.94 | 2026 | same |
| 4 cargas: 17 canastas | cap USD 13,970.60; maximum rebate USD 2,514.71 | 2026 | same |
| 5 or more cargas: 20 canastas | cap USD 16,436.00; maximum rebate USD 2,958.48 | 2026 | same |
| Taxpayer with, or caring for, a person with a disability or a catastrophic, rare or orphan disease: 100 canastas | cap USD 82,180.00; maximum rebate USD 14,792.40 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (literal c, as replaced by the law in RO Suplemento 461 of 20 Dec 2023) |
| Galápagos | canasta multiplied by the Galápagos consumer price index (IPCEG); SRI gives 1.803 for 2026 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 34); index from SRI Boletín NAC-COM-26-006 |

The caps are the canasta times the multiple; the maximum rebate is 18% of the cap, rounded to the cent. Who counts as a carga familiar and which expenses qualify is under The base.

**Exempt amounts tied to the exempt band.**

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Person over 65: exempt income | one fracción básica, USD 12,208 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 9(12)) |
| Person with a certified disability (or their sole substitute, if the person does not use it): exempt income | up to two fracciones básicas, USD 24,416, scaled by degree of disability: 30-49% gives 60%, 50-74% 70%, 75-84% 80%, 85-100% 100% | 2026 | same (art. 9(12)); degree scale at https://www.sri.gob.ec/impuesto-renta |
| Over-65 and disability exemptions together | not cumulative; use the more favourable one | 2026 | same (art. 9(12)) |
| Who must file (general regime) | gross income above the fracción básica, USD 12,208 | 2026 | https://www.sri.gob.ec/impuesto-renta |

**Other individual rates.**

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Non-resident individual, income from services occasionally provided in Ecuador | company rate on the whole income: 25% | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI arts. 36(b), 37) |
| Non-resident, other taxable income not attributable to a permanent establishment and with no specific withholding rate | 25%, withheld at source; recipient in a tax haven, lower-tax jurisdiction or preferential regime: the top individual rate, 37% | 2026 | same (art. 39) |
| Lottery, raffle, betting and sports-forecast prizes above one fracción básica (USD 12,208) per prize | single tax 15% of each prize, withheld by the organiser; prizes from Junta de Beneficencia de Guayaquil and Fe y Alegría exempt | 2026 | same (arts. 36(c), 9(10)) |
| Dividends from an Ecuadorian company to a resident individual | single income tax 12% on the amount distributed, withheld by the company; first 3 salarios básicos unificados (3 × USD 482 = USD 1,446) per company per year exempt; foreign dividends go into the general base with credit for foreign tax | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/c901c5dc-4f1f-411c-a02a-84432bfef788/Ley%20Org%C3%A1nica%20de%20Transparencia%20Social.pdf (LRTI art. 39.2(1), (2), (7), (8), as replaced from 1 Sep 2025); detail in ec-corporate-income-tax |
| Gain on shares sold on an Ecuadorian stock exchange | exempt up to 50 fracciones básicas a year (USD 610,400) if under 25% of the company's paid-in capital; above 25%, 5% single rate on the gain | 2026 | same (art. 9(24)) |

**Inheritances, legacies and gifts, Tabla No. 2, 2026** (LRTI art. 36(d); Res. NAC-DGERCGC25-00000043 art. 3). Rates are halved for heirs and legatees in the first degree of consanguinity with the deceased. Minor or disabled children of the deceased are exempt in the proportion the law sets.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Base USD 0 to 78,527 | 0% | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf (art. 3) |
| USD 78,527 to 157,053 | USD 0 + 5% of the excess | 2026 | same |
| USD 157,053 to 314,108 | USD 3,926 + 10% of the excess | 2026 | same |
| USD 314,108 to 471,193 | USD 19,632 + 15% of the excess | 2026 | same |
| USD 471,193 to 628,268 | USD 43,195 + 20% of the excess | 2026 | same |
| USD 628,268 to 785,321 | USD 74,609 + 25% of the excess | 2026 | same |
| USD 785,321 to 942,353 | USD 113,873 + 30% of the excess | 2026 | same |
| Above USD 942,353 | USD 160,982 + 35% of the excess | 2026 | same |

**RIMPE (LRTI art. 97.6; RLRTI art. 229).** Tax on **gross income** from the RIMPE activities, not on profit. No gastos personales rebate and no other reduction (RLRTI arts. 228, 229).

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| RIMPE scope | individuals and companies with gross annual income up to USD 300,000 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 97.3) |
| Negocio Popular: individual with gross income up to USD 20,000 | fixed tax by band: USD 0 to 2,500 pays USD 0; 2,500.01 to 5,000 pays USD 5; 5,000.01 to 10,000 pays USD 15; 10,000.01 to 15,000 pays USD 35; 15,000.01 to 20,000 pays USD 60 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf (Decreto Ley 742 art. 12, table replacing art. 97.6) |
| Emprendedor with gross income up to USD 20,000 | the same fixed bands, USD 0 / 5 / 15 / 35 / 60 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/bc4b9983-05f1-4a7a-a7c6-8a7cb2ec5572/LEY%20ORG%C3%81NICA%20DE%20EFICIENCIA%20ECON%C3%93MICA%20Y%20GENERACI%C3%93N%20DE%20EMPLEO.pdf (LOEEGE art. 23) |
| Emprendedor USD 20,000 to 50,000 | USD 60 + 1.00% of the excess over 20,000 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf (Decreto Ley 742 art. 12) |
| Emprendedor USD 50,000 to 75,000 | USD 360 + 1.25% of the excess over 50,000 | 2026 | same |
| Emprendedor USD 75,000 to 100,000 | USD 672.50 + 1.50% of the excess over 75,000 | 2026 | same |
| Emprendedor USD 100,000 to 200,000 | USD 1,047.50 + 1.75% of the excess over 100,000 | 2026 | same |
| Emprendedor USD 200,000 to 300,000 | USD 2,797.52 + 2.00% of the excess over 200,000 | 2026 | same |
| Gross income above USD 300,000 at year end | general regime and Tabla No. 1 for that year | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (art. 97.6, last paragraph) |
| Negocio Popular whose gross income exceeds USD 20,000 (up to 300,000) | taxed on the Emprendedor table for its band | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 230) |

**Bookkeeping thresholds (RLRTI art. 37; LRTI art. 19).** An individual must keep full accounts (signed by an authorised accountant) if, on 1 January or at the start of activity, own capital exceeds USD 180,000, or prior-year income exceeds USD 300,000, or prior-year costs and expenses exceed USD 240,000. Below these, an income and expense record (cuenta de ingresos y egresos) is enough. Employment income, pensions, inheritances, prizes, dividends, financial returns, occasional property sales and non-habitual home rental do not count toward the thresholds. Source: https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 37).

**Prior year, for returns filed in March 2026 (tax year 2025).** Res. NAC-DGERCGC24-00000041 (RO Suplemento 708 of 20 December 2024), as published by the SRI at https://www.sri.gob.ec/declaracion-impuesto-a-la-renta-2025: 0% to USD 12,081; 5% to 15,387 (USD 0 on the fracción); 10% to 19,978 (USD 165); 12% to 26,422 (USD 624); 15% to 34,770 (USD 1,398); 20% to 46,089 (USD 2,650); 25% to 61,359 (USD 4,914); 30% to 81,817 (USD 8,731); 35% to 108,810 (USD 14,869); 37% above (USD 24,316). The 2025 canasta was USD 798.31 (caps USD 5,588.17 for 7 canastas, maximum rebate USD 1,005.87). The same page prints the 5-or-more cap as USD 15,996.20. 20 × 798.31 is USD 15,966.20, which matches its rebate of USD 2,873.92, so USD 15,996.20 is a typo.

## The base

**General regime (LRTI art. 16).** Base = all taxable ordinary and extraordinary income, less returns, discounts, costs, expenses and deductions attributable to that income. Then apply Tabla No. 1 to get the tax due (impuesto causado), subtract the gastos personales rebate, then subtract tax credits (withholdings suffered, prior credits).

**Employment income (LRTI art. 17).** Base = taxable employment income less the employee's personal IESS contribution (unless the employer pays it). No other deduction or rebate reduces this base; gastos personales work as a rebate against the tax, not a deduction from income. Where the employer pays the tax for the employee (net-pay contract), add the tax the employer bears, once, to the base. The IESS rate is in [ecuador-social-contributions](ecuador-social-contributions.md).

**Employer withholding (RLRTI art. 104).** The employer adds up all pay projected for the year except the 13th and 14th salaries, subtracts the employee's IESS contribution (and the over-65 or disability exemptions), applies Tabla No. 1, subtracts the rebate on the employee's projected gastos personales, and divides by 11 to get the monthly withholding. Withholding starts with February pay; January pay is not withheld. The employee hands the employer a projection of gastos personales (with the number of cargas familiares) in February. The employer uses the January canasta, or the last known value until it is published, and adjusts later.

**Exempt income (LRTI art. 9), the items most individuals meet.**

- 13th and 14th salaries (décima tercera and décima cuarta remuneraciones).
- IESS benefits of every kind, employer retirement pensions under the Código del Trabajo, ISSFA and ISSPOL benefits and state pensions (art. 9(7)). The return of fondos de reserva by the IESS is not subject to withholding (RLRTI art. 105(2)).
- Interest on demand savings deposits paid by Ecuadorian financial institutions (art. 9(6)).
- Returns on fixed-term deposits and fixed-income securities issued for 180 days or more and held for at least 180 days without a break, unless the recipient is a debtor of that institution (credit-card debt does not count) or a related party (art. 9(15.1)).
- Severance (desahucio) and unfair-dismissal compensation up to the Código del Trabajo amounts; any excess is taxable (art. 9, unnumbered item).
- Scholarships for study at higher-education institutions and similar bodies (art. 9, unnumbered item).
- Travel, lodging and meal allowances of private-sector employees, supported by documents, for reasons inherent to the job (art. 9(11)).
- Gains from occasional sales of real estate, up to two sales a year; occasional means outside the taxpayer's ordinary business (art. 9(14)).
- Insurance indemnities, except for loss of profit (art. 9(16)).
- The over-65 and disability amounts in the rates section (art. 9(12)).

**Gastos personales (LRTI rebate article; RLRTI art. 34).**

- **What qualifies.** Expenses incurred in Ecuador on: housing (vivienda), health (salud), food (alimentación), clothing (vestimenta), national tourism in registered establishments with an annual operating licence, and education including art and culture. IVA and ICE are excluded from the amounts. Also:
  - child support (pensiones alimenticias) set in a mediation record or court ruling;
  - all interest on unsecured (quirografarios) and mortgage loans from the national financial system;
  - salaries and social benefits of workers affiliated to the IESS who are not linked to the taxpayer's business, if the IESS obligations are up to date when the return is filed;
  - vet and food costs of the taxpayer's pets (health and food headings).
- **Housing** covers rent, condominium fees, mortgage interest for buying, building or improving the home, property tax and basic utilities, for one habitual home only.
- **Health** covers fees of doctors and other licensed health professionals, clinics, labs and pharmacies, medicines, lenses and prostheses, prepaid medicine and health insurance premiums, and the unreimbursed deductible.
- **Education** covers enrolment and fees at every level, school supplies and books, special education, childcare centres, uniforms, and art and culture as defined by the Ley Orgánica de Cultura.
- **Not reimbursed.** An expense reimbursed in any way does not count. The taxpayer picks which headings to use.
- **Receipts.** Supporting sales receipts (comprobantes de venta) may be in the name of the taxpayer or a registered carga familiar.
- **Cargas familiares** are parents, spouse or de facto partner, and children up to the year they turn 21 (or disabled children of any age), who depend on the taxpayer and have no taxed income. A dependant with taxed income up to one salario básico unificado (USD 482 for 2026) still counts. Parents must consent to being registered. Two taxpayers may share dependants, but no dependant may be counted by two taxpayers for the same year. Once an expense is incurred for a dependant, they count for the whole year for the cap, unless they had taxed income in the year.
- **Anexo.** To take the rebate the taxpayer must file the Anexo de Gastos Personales (RLRTI art. 34). Employees who want the rebate file it too.

**RIMPE base (RLRTI art. 228).** Gross taxed income from the RIMPE activities, operational and non-operational, less returns and discounts shown on the same receipt or credit note. A Negocio Popular also subtracts wages of its IESS-affiliated employees if the IESS obligations are met by the filing date (LRTI art. 97.3). Leave out lottery prizes, dividends, sales of shares, financial returns, inheritances and gifts, and pensions. These are declared under the general rules. Withholdings suffered are a credit against RIMPE tax (art. 97.10; RLRTI art. 232).

**Who cannot use RIMPE (LRTI art. 97.4).** Anyone whose RUC shows any of these, even alongside other activities:

- construction contracts and urbanisation or land-division activities (arts. 28 and 29);
- professional services, mandates and representation, commission agents;
- transport (except taxis), farming, fuel sales;
- employment, and renting out movable or immovable property;
- other special income tax regimes;
- hydrocarbons, mining, petrochemicals, medical labs and pharmaceuticals, basic industries, finance, the popular and solidarity economy, insurance;
- goods or services subject to ICE.

Artisans, recipients of foreign direct investment and public-private partnerships are also excluded. RIMPE lasts 3 years from the first return while gross income stays at or below USD 300,000. Negocios Populares stay while they keep that status. Once excluded, a taxpayer cannot re-enter (art. 97.5).

**Classifying receipts and payments.**

| Item | Treatment | Rule |
|---|---|---|
| Fees for professional services, platform payouts for services | General-regime business income (professionals cannot use RIMPE) | LRTI arts. 16, 97.4(b) |
| IVA charged on sales | Not income; owed to the SRI | see ecuador-iva |
| Input IVA that can be credited | Not a cost | see ecuador-iva |
| Input IVA that cannot be credited | Part of the cost | see ecuador-iva |
| Salary from an employer | Employment income, base under art. 17 | LRTI art. 17 |
| 13th and 14th salaries | Exempt | LRTI art. 9 |
| IESS benefits, return of fondos de reserva paid by IESS | Exempt / no withholding | LRTI art. 9(7); RLRTI art. 105 |
| Interest on a demand savings account | Exempt | LRTI art. 9(6) |
| Rent received | Taxable; if habitual, it excludes RIMPE | LRTI arts. 16, 97.4(b) |
| Housing, health, food, clothing, education, tourism spending | Feeds the gastos personales rebate, not a business deduction | LRTI rebate article; RLRTI art. 34 |
| Personal expenses above the cap, the taxpayer's own drawings | Not deductible | RLRTI art. 35(1) |
| Withholdings shown on comprobantes de retención | Tax credit, not an expense | RLRTI art. 232; LRTI art. 47 |
| Transfers between own accounts, loan principal | Neither income nor expense | LRTI art. 16 |

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Annual return and payment, general regime, tax year 2026 | window opens 1 February 2027; due by ninth digit of the RUC, cédula or passport: 1 = 10 March, 2 = 12, 3 = 14, 4 = 16, 5 = 18, 6 = 20, 7 = 22, 8 = 24, 9 = 26, 0 = 28 March 2027 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 72(2)) |
| Special taxpayers (contribuyentes especiales) | by the 9th of the month (March for individuals), whatever the ninth digit; moved to the previous business day if a holiday | https://www.sri.gob.ec/impuesto-renta |
| Taxpayers domiciled in Galápagos | up to the 28th of the following month, without regard to the ninth digit (RLRTI art. 72 wording) | RLRTI art. 72, same URL as the first row |
| Due date on a holiday or rest day | moves to the next business day, unless that falls in the next month; then it moves back to the last business day of the due month | same |
| RIMPE (Negocio Popular and Emprendedor individuals), tax year 2026 | the law: by June 2027 at the latest (LRTI art. 97.8; RLRTI art. 230). The SRI calendar for tax year 2025 set 10 to 28 May 2026 by ninth digit (1 = 10 May to 0 = 28 May). The return is due even with no income | https://www.sri.gob.ec/declaracion-impuesto-a-la-renta-2025 |
| Anexo de Gastos Personales, tax year 2026 | February 2027, by ninth digit, for everyone who takes the rebate, employees included | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/a51f041a-d0b5-49d0-a2e0-7af11552f3c0/BOLETI%CC%81N%20004%20-%20EN%20FEBRERO%20LOS%20CONTRIBUYENTES%20DEBEN%20PRESENTAR%20EL%20ANEXO%20DE%20GASTOS%20PERSONALES%20DEL%20PER%C3%8DODO%20FISCAL%202025.pdf (SRI Boletín NAC-COM-26-004, for tax year 2025) |
| Projection of gastos personales to the employer | February of the tax year (February 2026 for 2026) | RLRTI art. 104, same URL as the first row |
| Early return when activity stops during the year | within 30 days of ending the activity | RLRTI art. 74 |
| Amended return (declaración sustitutiva) | within one year where the error does not change the tax or overstated it; to raise the tax, any time before an SRI audit begins, with interest | RLRTI art. 73; LRTI art. 101 |

**Who must file.** Every individual with gross income above USD 12,208 in 2026 must file, even if the rebate brings the tax to zero. Not required: a non-resident with no representative in Ecuador whose only income was withheld at source (SRI, https://www.sri.gob.ec/impuesto-renta).

**How to file, step by step.**

1. Get the SRI en línea password (clave) and check the RUC shows the right regime (general, RIMPE Negocio Popular or RIMPE Emprendedor).
2. Register cargas familiares in SRI en línea, then file the Anexo de Gastos Personales in February.
3. From 1 February, file the annual income tax return in SRI en línea. Under the general regime, enter income, costs and expenses, exempt income, the over-65 or disability exemption, the rebate, and withholdings from comprobantes de retención. RIMPE uses the simplified return the SRI generates.
4. The system works out the tax due, the rebate and the balance. A late return must include the interest and fine in the same return (RLRTI art. 72).
5. Pay the balance by the ninth-digit date through the means the SRI accepts. A credit balance can be claimed as a refund, as a pago indebido, or carried as a credit to later years (LRTI art. 47; RLRTI art. 232).
6. Keep comprobantes de venta and comprobantes de retención for at least 7 years (RLRTI arts. 37, 232).

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Late filing with tax due | 3% of the tax due per month or part of a month late; cap 100% of the tax; self-assessed without any resolution | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 100) |
| Late filing with no tax due | 0.1% of gross income for the period per month or part of a month; cap 5% of that income | same |
| Fine not self-assessed and paid | the SRI collects it increased by 20% | same |
| Interest on late tax | annual interest at the Banco Central del Ecuador's 90-day active reference rate, for each quarter of delay, per month (a part month counts as a full month), from the due date to payment | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf (CT art. 21) |
| Interest on tax assessed by the SRI | 1.3 times that rate | same (CT art. 21) |
| Surcharge on tax assessed by the SRI | 20% of the principal, after credit for earlier payments | same (CT art. 90) |
| An all-zero return later replaced with real figures | the zero return counts as not filed; the fine is computed on the replacement | RLRTI art. 72 |

The interest rate itself changes each quarter; take it from the Banco Central del Ecuador for the quarter concerned.

## Cross-border points

- **Residents** are taxed on worldwide income (LRTI art. 2(2)). Ecuadorian-source income stays taxable in Ecuador even if the person is resident elsewhere. Tax paid abroad can be credited under double tax agreements ratified by Ecuador. Where the foreign tax is lower than the Ecuadorian table would give, the person pays the difference in Ecuador (art. 4.1(c)).
- **Non-residents**: 25% (the company rate) on the whole income from services occasionally provided in Ecuador (art. 36(b)). 25% withheld on other Ecuadorian-source income with no specific withholding rate. 37% if the recipient is in a tax haven, lower-tax jurisdiction or preferential regime (art. 39).
- **Sale of Ecuadorian shares by a resident or non-resident**: single income tax of 10% on the gain (LRTI, unnumbered article after art. 37), with the stock-exchange exemption in art. 9(24). The Ecuadorian company is the substitute taxpayer except for stock-exchange sales (art. 39). Detail in ec-corporate-income-tax.
- **Foreign inheritances and gifts received by a resident** are taxed under Tabla No. 2. Tax paid abroad on the same event is a credit, up to the Ecuadorian tax (art. 36(d)).
- **Temporary tax residence**: Ecuadorian-source income only, for 5 years (art. 4.1, unnumbered article).
- Treaty rates and withholding on payments abroad: refer to a cross-border skill or a licensed Ecuadorian adviser.

## Two worked examples that recompute

### Example 1: self-employed consultant, general regime, no dependants

María is resident in Ecuador and works as an independent IT consultant (professional services, so RIMPE is excluded). In 2026 her taxable fees net of IVA are USD 42,000 and her deductible business costs are USD 12,000. Her base is USD 30,000. She has no cargas familiares. She has receipts for USD 6,000 of gastos personales (rent and food). Clients withheld USD 800 of income tax.

- USD 30,000 falls in the USD 26,700 to 35,136 band: tax due = 1,412 + (30,000 − 26,700) × 15% = 1,412 + 495 = **USD 1,907.00**.
- Rebate: 18% × min(6,000, 7 × 821.80 = 5,752.60) = **USD 1,035.47**.
- Tax after rebate: USD 871.53. Less withholdings USD 800: **USD 71.53 payable** by her ninth-digit date in March 2027.
- Her gross income is above USD 12,208, so she must file whatever the result. She files the Anexo de Gastos Personales in February 2027.

```oa-check
name: EC PIT 2026, resident consultant, base USD 30,000, no dependants
inputs:
  fees: 42000
  costs: 12000
  gastos: 6000
  canasta: 821.80
  withheld: 800
steps:
  - base: fees - costs
  - tax_due: 1412 + (base - 26700) * 0.15
  - cap: canasta * 7
  - rebate: round(0.18 * min(gastos, cap), 2)
  - after_rebate: max(0, tax_due - rebate)
  - payable: after_rebate - withheld
expected:
  base: 30000
  tax_due: 1907.00
  cap: 5752.60
  rebate: 1035.47
  after_rebate: 871.53
  payable: 71.53
```

### Example 2: shopkeeper, does RIMPE apply? (a decision worked both ways)

Luis is resident and runs a small shop. In 2026 his gross sales net of IVA are USD 60,000, costs USD 40,000, profit USD 20,000. He has 2 cargas familiares and USD 9,000 of gastos personales. Which regime applies decides his tax. RIMPE is not a choice: it follows the RUC (LRTI arts. 97.3 to 97.5).

- **If his RUC shows only the shop (RIMPE Emprendedor):** tax on gross income = 360 + (60,000 − 50,000) × 1.25% = **USD 485.00**. There is no rebate under RIMPE (RLRTI art. 228). Due by his ninth-digit date in May 2027 under the SRI calendar.
- **If his RUC also shows an excluded activity, such as renting out a flat:** RIMPE is closed to him (art. 97.4) and he is under the general regime on profit. Base USD 20,000 falls in the USD 15,549 to 20,188 band: 167 + (20,000 − 15,549) × 10% = **USD 612.10**. Rebate: 18% × min(9,000, 11 × 821.80 = 9,039.80) = USD 1,620.00, which is more than the tax, so the tax is **USD 0**. The unused USD 1,007.90 is lost, not refunded.
- **The figure that decides** is the activity list on the RUC. With these numbers the general regime gives less tax (USD 0 against USD 485), but he cannot pick it while he is RIMPE-eligible. If profit were USD 30,000 on the same sales, the general regime would give 1,412 + 495 = 1,907 less the 1,620 rebate = USD 287, still below RIMPE's USD 485.

```oa-check
name: EC 2026, RIMPE Emprendedor against the general regime for the same shop
inputs:
  gross: 60000
  costs: 40000
  gastos: 9000
  canasta: 821.80
steps:
  - rimpe_tax: 360 + (gross - 50000) * 0.0125
  - profit: gross - costs
  - general_tax_due: 167 + (profit - 15549) * 0.10
  - cap: canasta * 11
  - rebate: round(0.18 * min(gastos, cap), 2)
  - general_tax: max(0, general_tax_due - rebate)
  - rebate_lost: rebate - general_tax_due
  - alt_profit_tax: max(0, 1412 + (30000 - 26700) * 0.15 - rebate)
expected:
  rimpe_tax: 485.00
  profit: 20000
  general_tax_due: 612.10
  cap: 9039.80
  rebate: 1620.00
  general_tax: 0
  rebate_lost: 1007.90
  alt_profit_tax: 287.00
```

## Ask the client first

1. Residence in 2026: days in Ecuador and abroad (including across two tax years), where most income and assets are, and whether temporary tax residence was taken on arrival.
2. What the RUC shows: general regime, RIMPE Negocio Popular or RIMPE Emprendedor, and every activity registered (one excluded activity closes RIMPE).
3. Kinds of income: employment, professional fees, business, rent, interest and deposits (term and holding period), dividends, share sales, prizes, inheritances or gifts, foreign income.
4. Gross income, costs and own capital, for the filing duty and the USD 180,000 / 300,000 / 240,000 bookkeeping tests.
5. Cargas familiares: who, their ages and income, and whether any are registered by another taxpayer; any disability or catastrophic illness; whether the client is over 65.
6. Gastos personales receipts by heading, and withholdings suffered (comprobantes de retención); for employees, the projection given to the employer.

## Sources

| Source | URL | Read on |
|---|---|---|
| SRI Resolution NAC-DGERCGC25-00000043 (29 Dec 2025), 2026 tables for individuals (art. 2) and inheritances and gifts (art. 3), applicable from 1 Jan 2026; whole document read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf | 2026-11-11 |
| LRTI, SRI codification, last reform 2026-04-01: arts. 1-8, 9, 10 (rebate article), 16-19, 36, 37, 39, 47, 97.1-97.10, 100, 101 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| RLRTI, SRI codification, last reform 2025-11-18: arts. 34, 35, 37, 72-74, 104, 105, 228-232 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| Decreto Ley 742, Ley Orgánica para el Fortalecimiento de la Economía Familiar (RO Supl. 335, 20 Jun 2023), SRI copy: canasta multiples table (art. 3) and RIMPE tables (art. 12) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/de132165-dc5e-4267-a8a8-b9368be697f9/Ley_Organica_Fortalecimiento_Econ_Familiar_20_jun_2023.pdf | 2026-11-11 |
| Ley Orgánica de Eficiencia Económica y Generación de Empleo (RO Supl. 461, 20 Dec 2023), SRI copy: art. 23 (Emprendedores up to USD 20,000 table) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/bc4b9983-05f1-4a7a-a7c6-8a7cb2ec5572/LEY%20ORG%C3%81NICA%20DE%20EFICIENCIA%20ECON%C3%93MICA%20Y%20GENERACI%C3%93N%20DE%20EMPLEO.pdf | 2026-11-11 |
| Código Tributario, SRI codification, last modification RO 372 of 10 Aug 2023: arts. 21 and 90 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf | 2026-11-11 |
| SRI Boletín NAC-COM-26-006 (6 Feb 2026): canasta USD 821.80, 18%, Galápagos IPCEG 1.803, February projection | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ea002a89-17d8-4cdf-be42-affedbe3f8d8/BOLET%C3%8DN%20006%20-%20SRI%20HABILITA%20LA%20PROYECCI%C3%93N%20DE%20GASTOS%20PERSONALES%202026%20PARA%20REDUCIR%20EL%20IMPUESTO%20A%20LA%20RENTA.pdf | 2026-11-11 |
| SRI Boletín NAC-COM-26-004 (30 Jan 2026): Anexo de Gastos Personales due in February by ninth digit, employees included | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/a51f041a-d0b5-49d0-a2e0-7af11552f3c0/BOLETI%CC%81N%20004%20-%20EN%20FEBRERO%20LOS%20CONTRIBUYENTES%20DEBEN%20PRESENTAR%20EL%20ANEXO%20DE%20GASTOS%20PERSONALES%20DEL%20PER%C3%8DODO%20FISCAL%202025.pdf | 2026-11-11 |
| SRI, Impuesto a la Renta page: who must file, bookkeeping thresholds, disability scale, deadlines and special taxpayers | https://www.sri.gob.ec/impuesto-renta | 2026-11-11 |
| SRI, Declaración Impuesto a la Renta 2025 page: 2025 table, 2025 canasta caps, RIMPE May calendar | https://www.sri.gob.ec/declaracion-impuesto-a-la-renta-2025 | 2026-11-11 |
| Ley Orgánica de Transparencia Social (RO third Supl. 112, 28 Aug 2025), SRI copy: new art. 39.2 and final provisions | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/c901c5dc-4f1f-411c-a02a-84432bfef788/Ley%20Org%C3%A1nica%20de%20Transparencia%20Social.pdf | 2026-11-11 |
| Ministerio del Trabajo, Acuerdo Ministerial MDT-2025-195: salario básico unificado USD 482 from 1 Jan 2026 | https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf | 2026-11-11 |

Not yet confirmed: whether art. 39's reference to a progressive table for non-residents' share gains still applies next to the 10% single tax; dividends received by resident individuals between 1 Jan 2025 and 31 Aug 2025 went into the progressive table (Ley Orgánica de Transparencia Social, second final provision), not the 12% single tax; the RIMPE calendar for tax year 2026 (May 2027 dates assumed from the 2025 calendar; the law sets June as the outer limit); the Anexo de Gastos Personales calendar dates by digit for tax year 2026 and whether the SRI keeps any income threshold for it; the form numbers for the annual return (Formulario 102 or 102A) in SRI en línea for 2026; whether the Código Tributario arts. 21 and 90 were amended after 10 Aug 2023 (the SRI copy read is dated then); the treatment of Andean Community Decision 578 for residents of CAN countries; the meaning of "the following month" for Galápagos taxpayers in RLRTI art. 72.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ecuador-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ecuador-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
