---
name: argentina-income-tax
description: >
  Use this Argentine income tax reference whenever asked about Impuesto a las
  Ganancias for self-employed individuals (autónomos, profesionales
  independientes) in the general regime. Match phrases like Ganancias, impuesto
  a las ganancias, autónomo Argentina, monotributo vs responsable inscripto,
  cuarta categoría, deducciones personales, ganancia no imponible, bienes
  personales, DDJJ Ganancias, ARCA, AFIP, CUIT, income tax Argentina, anticipos
  ganancias, or any question about filing or computing income tax for a
  self-employed client in Argentina. It gives the art. 94 scale (5% to 35%) and
  the art. 30 amounts ARCA publishes for periods 2025 and 2026, general
  deductions, anticipos, percepciones as credits, the Bienes Personales
  interaction and filing in Ganancias Personas Humanas - Portal Integrado. This
  Tier 2 draft supports source checking and reviewer questions; it does not
  authorise filing, payment or a tax position.
version: 2.5
jurisdiction: AR
tax_year: 2026
tax_year_notes: "Calendar tax year 2026, with separately labelled 2025 return material retained from Ryan Duguid's merged rewrite. The 2025 return remains open to 16 November 2026 under RG 5918. ARCA's annual tables for 2026 are also shown. Every indexed amount is the figure ARCA publishes for the named period, under arts 30 and 94 as amended by Ley 27.743."
last_updated: 2026-11-11
category: international
tier: 2
domain: income-tax
type: computation
---

# Argentine Income Tax: Autónomo / Profesional Independiente (Ganancias) v2.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers Impuesto a las Ganancias for individuals resident in Argentina who are self-employed and registered in the tax, in Argentine pesos. **Coverage label: calendar tax year 2026, retaining separately dated 2025 material because that return remains open to 16 November 2026.** The fiscal year for individuals is the calendar year (Ley de Impuesto a las Ganancias, texto ordenado 2019 (LIG), art. 24).

It covers income from a liberal profession or trade and the other functions in LIG art. 82 f), and from acting as corredor, viajante de comercio or despachante de aduana under art. 82 g). The wider art. 82 f) list is albacea, síndico, mandatario, gestor de negocios, director de sociedades anónimas and fiduciario. Where a profession or trade is complemented by a commercial business, or the reverse, the whole result is third category income (art. 53, last paragraph). Self-employed business income under art. 53 is touched only for the deducción especial.

Monotributo clients are outside this file: use `ar-monotributo`. Social security contribution amounts are in `ar-social-contributions`. Companies are in `ar-corporate-income-tax`. Those guides are not restated here.

### What this file is

This Guide is **Not yet approved**. Each figure carries its own citation and should be confirmed against it. It loads no workflow base, because the legacy file named none and none was qualified for this guide in this conversion; do not treat it as a complete operational workflow. Working paper only: nothing here is a filing position, and every output needs review by a Contador Público or equivalent before use.

### Refusals and boundaries

The codes are kept from the earlier version, and R-AR-7 is added. If a trigger fires, stop that work, give the message and do not produce a partial computation.

| Code | Trigger | Exact message |
| --- | --- | --- |
| R-AR-1 | Client is in Monotributo | 'Monotributo is a separate simplified regime. This file does not compute it; use ar-monotributo.' |
| R-AR-2 | Income category unknown: self-employed, relación de dependencia or both | 'The deducción especial differs by category under art. 30(c), so I cannot compute until the category of each income source is confirmed.' |
| R-AR-3 | A claimed expense has no document and no other proof | 'I cannot deduct this expense. Art. 40 denies it and charges 35% unless other evidence proves it was needed to earn taxable income. Even then, if the evidence shows a service, Decreto 862/2019 art. 106 may admit the deduction and keep the 35%. Art. 41 and art. 106 remove the charge only in their named cases.' This stops that line only. |
| R-AR-4 | Foreign-source income where a treaty or a foreign tax credit matters | 'Foreign-source income and foreign tax credits need treaty analysis by a reviewer. This file does not hold that analysis.' |
| R-AR-5 | Trust taxation or a corporate reorganisation | 'This is outside this file. Refer it to a reviewer.' |
| R-AR-6 | No CUIT provided | 'I need the CUIT: the ordinary filing schedule runs by its last digit and the return is filed under it.' |
| R-AR-7 | Art. 82 a), b) or c) income, such as employment or a pension, alongside art. 53 or other art. 82 income | 'Art. 30(c) and Decreto 862/2019 art. 98 set a separate limit on the deducción especial for mixed income. This file does not compute it, so a reviewer must.' |

A client who says they are an employee only is outside this file: art. 30(c) apartado 2 and RG 4003 retention then govern, and neither is computed here.

### Required inputs

1. Income category: art. 82 f) or g), art. 53, relación de dependencia, or a mix. A mix with art. 82 a), b) or c) income stops at R-AR-7.
2. Marital and family status, and each dependant's net income for the year.
3. Gross self-employment income for the calendar year.
4. Business expenses and their documents.
5. Mandatory autónomo contributions, paid month by month, and the category declared.
6. Health cover paid, split between obligatory obra social discounts and voluntary cover.
7. Other income: employment, rent, financial.
8. Assets at 31 December, for Bienes Personales.
9. CUIT.
10. Twelve months of bank statements.
11. Percepciones and retenciones suffered, with the documents that show them.
12. Anticipos paid.

### Conservative defaults

| Situation | Default |
| --- | --- |
| Self-employed or employee unclear | Stop (R-AR-2) |
| Period table uncertain | Use the annual table for the named period; never carry a table across periods |
| Undocumented expense | Not deducted until proved; art. 40 flagged, see The base |
| Spouse claimed, income unknown | Needs Input. The cónyuge amount needs net income at or below the art. 30(a) amount, confirmed |
| Percepciones | Credit only if a bank statement, card statement, invoice or equivalent document shows them, in the period they were charged. A document in an unregistered person's name is credited only under the RG 5617 art. 7 dependant condition |
| Monotributo or responsable inscripto unclear | Stop (R-AR-1 until settled) |
| Bienes Personales | Flag and check separately; it is not part of this computation |
| Contributions unpaid at the due date | Deducción especial not computed until art. 98 of the regulation is met |

### Red flags

| Flag | Treatment |
| --- | --- |
| No autónomo contributions shown | Art. 30(c) makes payment an indispensable condition of the deducción especial. Verify before computing it |
| Payments with no document | Art. 40 risk; test art. 41 and Decreto 862/2019 art. 106 |
| One client above about 80% of income | Reviewer heuristic carried from the earlier version. No statutory threshold was read. Ask whether the work is really employment |
| Large percepciones claimed | Match each to its document, and confirm the period |
| Assets near the Bienes Personales minimum | Flag for a separate return |

## Rates, bands and thresholds

Read each table for its named period. The scales and art. 30 amounts are ARCA's indexed figures under LIG arts 30 and 94, as substituted by Ley 27.743 arts 71 and 73. Both articles adjust semi-annually, in January and July, from fiscal year 2025 by the INDEC consumer price index for the semester just ended. Limit: ARCA's PDFs are titled for the retention regime on remuneration under RG 4003. ARCA's 'Determinación' page sends individual filers to the art. 94 scale and lists the art. 94 tables. Its personal deductions page lists the art. 30 tables, headed as values for remuneration. The controlling text is the unnumbered article after art. 102 of Decreto 862/2019 ('Mecanismo de actualización'): a person outside its second paragraph, which covers those with only art. 82 a), b), c) (except cooperative councillors) and e) income, uses at settlement the art. 30 amounts and art. 94 scale in effect from 1 July of the fiscal period. That ARCA's annual tables are those amounts is inferred; ARCA does not say so.

**Art. 94 scale, annual settlement, period 2025 (ARS)**

| Over | Up to | Fixed amount | Rate on excess | Source |
| --- | --- | --- | --- | --- |
| 0.00 | 1,749,901.45 | 0.00 | 5% | ARCA table, 2025: https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-liquidacion-anual-y-final-2025.pdf |
| 1,749,901.45 | 3,499,802.89 | 87,495.07 | 9% | same |
| 3,499,802.89 | 5,249,704.34 | 244,986.20 | 12% | same |
| 5,249,704.34 | 7,874,556.52 | 454,974.38 | 15% | same |
| 7,874,556.52 | 15,749,113.04 | 848,702.20 | 19% | same |
| 15,749,113.04 | 23,623,669.56 | 2,344,867.94 | 23% | same |
| 23,623,669.56 | 35,435,504.34 | 4,156,015.94 | 27% | same |
| 35,435,504.34 | 53,153,256.52 | 7,345,211.33 | 31% | same |
| 53,153,256.52 | and above | 12,837,714.51 | 35% | same |

**Art. 94 scale, annual settlement, period 2026 (ARS)**

| Over | Up to | Fixed amount | Rate on excess | Source |
| --- | --- | --- | --- | --- |
| 0.00 | 2,336,953.69 | 0.00 | 5% | ARCA table, 2026: https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-liquidacion-anual-y-final-2026.pdf |
| 2,336,953.69 | 4,673,907.36 | 116,847.68 | 9% | same |
| 4,673,907.36 | 7,010,861.05 | 327,173.52 | 12% | same |
| 7,010,861.05 | 10,516,291.59 | 607,607.96 | 15% | same |
| 10,516,291.59 | 21,032,583.18 | 1,133,422.54 | 19% | same |
| 21,032,583.18 | 31,548,874.77 | 3,131,517.94 | 23% | same |
| 31,548,874.77 | 47,323,312.16 | 5,550,265.01 | 27% | same |
| 47,323,312.16 | 70,984,968.25 | 9,809,363.10 | 31% | same |
| 70,984,968.25 | and above | 17,144,476.49 | 35% | same |

Formula: tax = fixed amount + (ganancia neta imponible - lower limit) x rate. The statutory base scale printed in art. 94 is for fiscal year 2024: 9 steps, with 35% above ARS 36,450,000. It was adjusted exceptionally in September 2024 under Ley 27.743 art. 74. Use ARCA's table for a period, never that base scale. ARCA's January to June 2026 table (https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-per-ene-a-jun-2026.pdf) starts its second band at ARS 2,000,030.09 and is a retention table; the annual table above is the one for the 2026 settlement.

**Art. 30 amounts, annual (ARS)**

| Deduction | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Ganancia no imponible, art. 30(a) | 4,507,505.52 | 6,019,671.36 | ARCA tables, 2025: https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2025.pdf and 2026: https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |
| Cónyuge or registered unión convivencial partner, art. 30(b)1 | 4,245,166.13 | 5,669,323.06 | same |
| Each child under 18, art. 30(b)2 | 2,140,852.77 | 2,859,060.31 | same |
| Each child incapacitated for work, any age | 4,281,705.53 | 5,718,120.60 | same |
| Deducción especial, art. 30(c) apartado 1 | 15,776,269.32 | 21,068,849.78 | same |
| Deducción especial, apartado 1, nuevos profesionales or emprendedores | 18,030,022.08 | 24,078,685.46 | same |
| Deducción especial, apartado 2 (employees, not autónomos) | 21,636,026.50 | 28,894,422.56 | same |

Read the multiples exactly. Art. 30(c) **increases** the art. 30(a) amount by 2.5 times, so ARCA's apartado 1 figure is 3.5 times the GNI and already stands alone (15,776,269.32 = 4,507,505.52 x 3.5). Do not add GNI x 2.5 or subtract GNI from it. The increase is 3 times for nuevos profesionales and emprendedores (4 times the GNI), and 3.8 times under apartado 2 (4.8 times the GNI), which also adds the twelfth part for art. 82 a), b) and c) income. That twelfth part is not available to autónomos.

Art. 30 applies only where the persons named are resident in Argentina. See The base for the conditions.

ARCA's semester tables are retention tables for remuneration, not annual amounts. For January to June 2025 they show GNI 3,916,268.37, cónyuge 3,688,339.32, child 1,860,042.98, incapacitated child 3,720,085.95 and deducción especial 13,706,939.31. An autónomo's annual return uses the amounts in effect from 1 July of the period (Decreto 862/2019, unnumbered article after art. 102), taken here from ARCA's annual table, not a mix of 2 semesters. ARCA's note on caps set by the GNI takes the amounts updated from 1 July at annual settlement.

**General deductions, LIG art. 85**

| Item | Limit | Source |
| --- | --- | --- |
| Mortgage interest on a loan to buy or build the taxpayer's home, art. 85(a), third paragraph | ARS 20,000 a year; a co-owner takes their percentage of that limit | LIG art. 85: https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 and ARCA: https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/deducciones-generales.asp |
| Other debt interest and related costs, art. 85(a), first 2 paragraphs | Only where the debt bought goods or services used to earn taxed income, and never for income taxed by final withholding. Art. 85(a)'s cap on art. 53 subjects' related party interest is not restated | same |
| Death and mixed insurance, and retirement fund units, art. 85(b) | ARS 573,817.13 for 2025; ARS 753,472.14 for 2026. Excess carries to later years of the contract | same |
| Private retirement insurance plans, art. 85(i) | Same amounts, as a separate item | same |
| Donations to the State, political parties and art. 26(e) and (f) institutions, art. 85(c), on regulated conditions | 5% of the net income base below; party donations are limited separately. Art. 26(f) bodies qualify only for the four art. 85(c) purposes described below, not every exempt civil body | same |
| Retirement contributions to national, provincial or municipal cajas, art. 85(d) | Amount paid; the article sets no cap | same |
| Amortisation of intangibles with a limited life, art. 85(e) | No percentage cap in the article | same |
| Obligatory obra social discounts, art. 85(f), first paragraph | Amount paid; the paragraph sets no cap | same |
| Fees to medical cover institutions (prepaga), art. 85(f), second paragraph | 5% of the net income base below | same |
| Medical and paramedical fees for the taxpayer and cargas, art. 85(g) | 40% of the amount invoiced, to the extent not reimbursed, capped at 5% of the net income base | same |
| Home rent, art. 85(h) | 40% of rent, capped at the art. 30(a) amount; taxpayer owns no property in any percentage; invoice or equivalent from the landlord needed. Under decree art. 204, all co-tenants together share both the 40% rent limit and the GNI ceiling | same |
| Educational services and tools, art. 85(j) | For art. 30(b)2 children, and adult children to age 24 in regular study that stops them supporting themselves. ARCA adds that they must be resident with net income in the year not above the GNI. Capped at 40% of the art. 30(a) amount | same |
| 10% of annual rent on a dwelling, art. 85(k) | Art. 85(k) names tenant and landlord, subject to registration, but current Decreto 406 art. 3 excludes the deduction when the landlord/co-owner is an individual or estate in its attributable proportion. It does not expressly limit that exclusion to exempt rent. Do not automatically allow an individual landlord claim; the qualifying tenant's deduction remains separate | same |
| Casas Particulares staff | Pay and employer contributions, capped at the annual GNI amount. ARCA page; not in art. 85. Ley 26.063 art. 16 not read | same |

Under current Decreto 406 art. 3, the operative landlord wording is "La citada deducción no resultará de aplicación cuando el locador o condómino" and "revista la condición de persona humana o sucesión indivisa". Do not narrow it by adding an unstated exempt-income condition. Its historical application to a 2025 claim and any disputed scope require review; the former general landlord topic is preserved here as that explicit limitation. For the art. 85(k) tenant deduction, the unnumbered Decreto 862 provision after art. 204 caps all co-tenants together at 10% of the total qualifying rent, with contract registration where required; co-owner allocation follows its attributable share. Its individual/estate-landlord exclusion does not cancel a qualifying tenant claim. For art. 26(n) property disposals from 2026, the unnumbered provision after decree art. 83 follows the sale event in LIG art. 3; a rights transfer follows decree art. 254, including assignment of a purchase agreement or similar commitment before possession. Do not restrict that sale exemption to the seller's own dwelling. Both rules come from [Decreto 406/2026 arts. 1-3](https://www.argentina.gob.ar/normativa/nacional/decreto-406-2026-426274/texto), published/effective 1 June 2026. The old art. 99 baseline and own-home exemption remain historical classification questions for 2025.

For the art. 85(c) donation to an art. 26(f) body, its main object must be one of: nonprofit social/medical assistance including the listed vulnerable groups; scientific/technological research with the statutory programme/personnel certification; economic/political/social research oriented to political-party plans; or the specified officially recognised degree education or cultural promotion through free recognised courses. Confirm ARCA-recognised exemption and the required donation evidence; cash donations must be banked through the channels in the [official general-deductions instructions](https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/deducciones-generales.asp).

For art. 85(j), the first unnumbered decree provision after art. 204 covers officially recognised public/private education and postgraduate courses, directly supplied accessory food/accommodation/transport, private classes following official curricula, nurseries and kindergartens. Tools mean school supplies, smocks and uniforms. Apply the existing dependent/older-student tests and parental allocation rules; both parents together cannot exceed 40% of the GNI. A fee merely labelled education does not establish these conditions.

The 5% limits in art. 85(c), (f) and (g) apply to net income for the year before deducting the items in those paragraphs, prior year losses and, where relevant, the art. 30 amounts (art. 85, closing paragraphs).

**Cedular rates outside the art. 94 scale, and Bienes Personales**

| Item | Rate or amount | Source |
| --- | --- | --- |
| Interest and returns, art. 95 | Do not use the repealed art. 95's printed 5% and 15%. Ley 27.541 art. 32 repealed that provision from period 2020. Test the specific exemption first; ordinary non-exempt capital interest/returns fall under art. 48(a) and the art. 94 scale, with specific regimes tested separately | Ley 27.541 art. 32, seen with LIG art. 95: https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Dividends and distributions, art. 97 | 7%, withheld by the payer; the withholding is final for resident individuals not registered in the tax | same |
| Sale of securities, art. 98(a) | 5%: in pesos without adjustment clause | same |
| Sale of securities, art. 98(b) | 15%: with adjustment clause or in foreign currency, and digital currencies | same |
| Sale of shares, art. 98(c) | 15%: listed shares not meeting art. 26(u), and unlisted shares. Exemptions under art. 26(u) not tested here | same |
| Sale of real estate in Argentina, art. 99 | 15% is the art. 99 baseline, not a current blanket property-sale tax. Art. 26(n) and the unnumbered Decreto 862 article after art. 83 exempt art. 99 operations by resident/non-resident individuals and estates involving Argentine property sold or transferred from 1 January 2026 | same |
| Bienes Personales minimum, period 2025 | ARS 384,728,044.57 | ARCA: https://www.afip.gob.ar/gananciasYBienes/bienes-personales/conceptos-basicos/que-es.asp |
| Bienes Personales, dwelling, period 2025 | Not reached at or below ARS 1,346,548,155.99 | same |
| Bienes Personales general scale, period 2025 | 0.50% to ARS 52,664,283.73 of the excess; then ARS 263,321.42 plus 0.75% to ARS 114,105,948.16; then ARS 724,133.89 plus 1.00% | ARCA: https://www.afip.gob.ar/gananciasYBienes/bienes-personales/conceptos-basicos/alicuotas.asp |
| Bienes Personales law, later periods | Ley 23.966 art. 25 steps down: 2 bands to 0.75% for 2026. Indexed 2026 amounts held | Ley 23.966: https://www.argentina.gob.ar/normativa/nacional/norma-365/actualizacion |

### Enactment position

| Point | Status at 5 November 2026 | Source |
| --- | --- | --- |
| Art. 94 scale and art. 30 structure | Enacted: Ley 27.743 arts 71 and 73, B.O. 8 July 2024, read through Infoleg's notes | LIG notes: https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| 2025 and 2026 amounts | Administrative publication by ARCA of the statutory indexation; the regulation fixes which amounts apply at settlement | Decreto 862/2019, unnumbered article after art. 102: https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 |
| Plazo fijo exemption in any currency | Enacted: Ley 27.802 art. 191, for years from 1 January 2026 | Ley 27.802: https://biblioteca.arca.gob.ar/dcp/LEY_C_027802_2026_02_27 |
| Dwelling rent exemption, art. 26(n) | Enacted: Ley 27.802 art. 192, for years from 1 January 2026 | same |
| Loss indexation | Enacted: Ley 27.802 art. 190, for losses of years from 1 January 2025 | same |
| Simplified return | Enacted: Ley 27.799 Chapter III, amended by Ley 27.826 arts 3 to 11; RG 5820 and RG 5916 administer it | Ley 27.826: https://www.argentina.gob.ar/normativa/nacional/norma-431078/texto |
| Filing dates for period 2025 | Administrative: RG 5851 as last substituted by RG 5918 | RG 5918: https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5918%7Co:9%7Ca:2026%7Cf:29/10/2026 |

## The base

Tax is computed on each category's net income in pesos, then pooled.

```text
A  Gross income of each category
B  less expenses linked to taxed income (arts 23, 83, 86)
C  Net income = A - B, after current year losses (art. 25)
D  less general deductions not capped by income (art. 85)
E  less capped items at their limits, on the base in art. 85's closing paragraphs
F  less prior year losses (art. 25)
G  less art. 30 amounts: GNI + cargas de familia + deducción especial
H  Ganancia neta imponible = max(C - D - E - F - G, 0)
I  Tax on H under the art. 94 table for the period
J  less anticipos, retenciones and percepciones computable in the period
K  Balance due = max(I - J, 0); saldo a favor = max(J - I, 0)
```

**Timing.** Art. 24 charges first and third category income on the accrual basis and fourth category income when received. Expenses follow correlatively. Argentine self-employed fees under art. 82 f) are therefore counted when received.

**Expenses.** Art. 83 allows expenses made to obtain, keep and preserve taxed income, apportioned where they serve taxed and other income. Art. 84 presumes Argentine-incurred expenses relate to Argentine-source income and foreign-incurred expenses to foreign-source income, while allowing proof of Argentine-source linkage for foreign expenses, subject to art. 91(e). Art. 86 adds specific items; art. 87 covers building depreciation at 2% and art. 88 other depreciation. Art. 92 bars personal and family expenses (a), pay to a spouse or relative (c), unless an actual service is shown, and then only up to what third parties are usually paid and, unless ARCA says otherwise, not above the pay of the highest category non-relative employee, this tax (d) and capital (f). Cars are limited by art. 92(l) and art. 86(f): depreciation and rental are limited as if cost were ARS 20,000, net of IVA, and running costs cannot pass the amount ARCA sets each year for each unit. The current amount is held. The limit does not apply where running the car is the main object of the taxed activity; the article lists rental, taxis, remises and viajantes de comercio, and adds 'y similares'. Home office and car percentages stay with the reviewer (T2-AR-2 and T2-AR-3).

**Undocumented expenses, LIG arts 40 and 41.** Where a payment has no document or an apocryphal one, and it is not proved by other means that by its nature it must have been made to obtain, keep and preserve taxed income, it is not deductible and it bears a 35% rate. That rate is final and stands in place of the tax of the unknown or hidden recipient. The chargeable event is the date of the payment. Art. 41 removes the charge where ARCA presumes the payments (a) bought goods or (b) by their amount or otherwise are not taxable in the recipient's hands. Decreto 862/2019 art. 106 has 3 limbs. First, where the circumstances show the payment went on services to obtain, keep and preserve taxed income, the deduction may be admitted, without prejudice to the art. 40 tax. Second, where the way the business or activity works gives a founded presumption that the payments do not become taxable income for the recipient, they may be deducted and no tax is due; in doubt, ARCA must be consulted. Third, where there are sufficient signs that the payment bought goods, no tax is due, and the payment takes the treatment of that kind of goods. ARCA sets when the tax is paid. So a missing invoice alone is not the test, and proof of a service may save the deduction and still leave the 35%. Art. 40 reads as if other proof lifts both the denial and the charge, whilst art. 106 keeps the tax on services; that tension is held. The earlier version's 'art. 38' was the wrong article. Whether the 35% is computed on a grossed-up amount is held. Art. 40 does not state it and no provision was read that does.

**Deducción especial, autónomos.** All of these must hold under art. 30(c) and Decreto 862/2019 arts 98 and 99:

- The income is art. 82 income other than a), b) and c), or art. 53 income where the person works personally in the activity. The earlier version's 'art. 53' for professionals was incomplete.
- Mandatory contributions to SIPA, or the substitute caja, are paid. This is an indispensable condition. Art. 98 requires all contributions for January to December, or for the months owed, to be paid by the general due date of the return or to sit in a current payment plan. Each month's amount must match ARCA's published amount for the category declared. The current Decreto 862 art. 98 prints these as concurrent limbs a) and b); the former consolidation-display gap is resolved.
- The deduction cannot exceed the sum of the qualifying net income, nor what remains after compensating losses and general deductions, if lower. So: `deduccion_especial = min(table amount, qualifying net income, amount remaining)`. That formula is for a client with no art. 82 a), b) or c) income.
- Art. 30(c) leaves income in both apartados to the regulation. For mixed income, current art. 98 uses total qualifying art. 30(c) income up to the apartado 1 ceiling where art. 82 a), b) and c) income does not exceed that ceiling; otherwise it uses the total attributable to those latter employment/pension categories up to the apartado 2 ceiling. Apply art. 98's prior loss/general-deduction ordering and qualifying-net/remaining-income caps throughout; do not add two separate full special deductions. This file does not compute that case: R-AR-7.
- Nuevos profesionales are those with up to 3 years in the matrícula, and nuevos emprendedores are independent workers with up to 3 years since registering as such. The contribution condition applies to both (Decreto 862/2019 art. 99).

**Deduction residence:** LIG art. 33 requires living in Argentina for more than six months of the fiscal year for art. 30 deductions. Art. 33 also treats as resident persons abroad in the service of the Nation, provinces, CABA or municipalities and Argentine-national officials serving international bodies of which Argentina is a member. This test is distinct from general tax residence under arts. 116 onward; do not infer eligibility merely from worldwide-income residence.

**Cargas de familia, art. 30(b).** The person must be resident under that deduction-specific test, must be supported by the taxpayer, and must not have net income in the year above the art. 30(a) amount, whatever its origin and whether or not taxed. 'Ingresos' covers every kind of real or presumed gain, benefit and periodic or occasional receipt, unless it repays capital (Decreto 862/2019 art. 100). Only the nearest relative with taxable income may deduct. Where 2 parents hold parental responsibility and both have taxable income, the child amount goes in equal parts, or one may take 100% (art. 101). A unión convivencial is proved by its registration record and counts from the month of that record. Art. 31 counts cargas by month, including the whole month of the event.

**Losses, art. 25.** Compensate within the category, then against the second, first, third and fourth categories. A remaining loss carries forward 5 years. Art. 30 amounts never create a loss. Specific losses stay in their class, and foreign-source losses go only against foreign-source income (art. 131). Losses of years from 1 January 2025 are indexed by IPC (art. 25 as substituted by Ley 27.802 art. 190).

**Rental income.** Rent is first category income. Under LIG art. 26(n) and [current Decreto 862 art. 83](https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06), dwelling rent or subrent accrued from 1 January 2026 is exempt regardless of the contract date only where the property is exclusively the tenant's or subtenant's unique, family and permanent home. It covers all the individual/estate landlord's units meeting that condition, including amounts for the owner-supplied furniture, accessories and services. The exemption also reaches presumed rent on free or undetermined-price occupation where the occupier uses it as a home. A residential label alone is insufficient. The current decree also states the individual/estate-landlord exclusion from art. 85(k) without an express exempt-income qualifier; the tenant's own deduction has its separate conditions, as discussed above. A commercial let stays taxable, and so does a dwelling let in 2025. Expenses linked to exempt income are never deductible (art. 23). For urban property, maintenance expenses are either real, with vouchers, or a presumed 5% of gross rent. The method chosen applies to all the taxpayer's properties for 5 years. Persons who by nature must keep books, or have administrators who must account to them, and all rural property, use real expenses (art. 89).

**Financial income.** Art. 26(h) exempts interest on deposits with Ley 21.526 institutions: savings accounts, special savings accounts, fixed term deposits and third party deposits or other public funds as the Central Bank determines. Before 2026 the fixed term limb was for pesos; Ley 27.802 art. 191 removed that limit for years from 1 January 2026. It also covers returns on peso instruments for productive investment set by the Executive, if their rule says so and the first paragraph does not already cover them. Ley 27.541 art. 33 excluded interest on deposits with an adjustment clause, in a second paragraph of art. 26(h). Ley 27.638 art. 1 replaced that paragraph from period 2021 with the productive investment text, which has no such exclusion, and the consolidated art. 26(h) prints none. Classify contractual principal index adjustments separately from interest: LIG art. 26(t) exempts qualifying credit updates of any origin or nature, and [Decreto 862 art. 85](https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06) requires proof of the express agreement and an easily verifiable public index. This supplies the ordinary indexed-deposit principal-adjustment rule; it is not a claim that an adjustment is interest. Under LIG art. 26's penultimate paragraph, art. 183 and Decreto 862 art. 94, net eligible exempt active interest/updates against deductible art. 85(a) interest/updates with the required causal connection: only a positive balance is exempt; a negative balance follows the statutory deduction rules. These individual investment exemptions do not extend to a business applying inflation adjustment, for which art. 108(a) excludes arts. 26(h) and (t). Reading current arts. 48(a) and 94 together after the repeal of art. 95, ordinary non-exempt capital interest/returns enter second-category income and the progressive scale unless a named exemption or specific regime governs. Product, source and holder status still need evidence; an FCI distribution is not automatically a Ley 21.526 bank deposit. Dividends follow art. 97 and securities disposals follow their separate art. 98 rules.

**Percepciones, RG 5617 as amended.** RG 5617/2024 replaced RG 4815. It charges 30% only on the proportion of the covered operations paid in pesos that requires access to the foreign-exchange market (art. 1): card and equivalent payments for goods and services abroad, services by non-residents paid by card, foreign services through travel agencies, and passenger transport abroad. The base, in pesos, is the total amount of each operation (art. 6(a)), except passenger transport abroad, where it is the price net of taxes and charges (art. 6(b)). Art. 2 excludes health, medicines, books, educational platforms and software for educational purposes; research; firefighting; land transport to neighbouring countries; and listed portals, each in its stated terms. Since RG 5672/2025, buying banknotes and foreign currency as an individual is excluded (art. 2(e)). A bank's or card issuer's document is the proof (art. 5). Under art. 7 a registered taxpayer credits it against Ganancias in the period it was charged, as tax paid. On a card it is charged to the holder, user, additional holder or extension beneficiary, as the case may be. Where the document shows it in the name of a person not registered with ARCA, only the taxpayer who made the payment may credit it, in the annual Ganancias return, only if that person is declared as a carga de familia and only in the corresponding proportion. Otherwise 'este último', read here as the unregistered person, may claim a refund under Title II. RG 5617 does not define that proportion, so it is held. Any resulting saldo a favor counts as ingreso directo. Monotributo clients and non-taxpayers of Ganancias credit it against Bienes Personales. Someone not required to register in Ganancias may instead opt, by telling the collecting agent beforehand, to credit it there. Those who can credit it against neither tax may claim a refund under Title II once the calendar year ends. Impuesto PAIS applied up to 22 December 2024 (RG 5617 recitals); it is not a percepción and not a credit. The earlier version also named percepciones on imports. RG 2281 was not read, so that topic is held.

**Retenciones.** Tax withheld is a credit on the return. RG 830 governs retention on fees; it was not read, so no retention rate is given here.

### Transaction patterns

Working paper only. These narrations are illustrative, carried from the earlier version; no bank or ARCA source defines them. Confirm each from the document behind it.

| Code | Narration | Treatment |
| --- | --- | --- |
| I-01 | `TRANSFERENCIA DE [client]`, `TRF CR [client]` | Fee income, art. 82 f) if a profession |
| I-02 | `ACREDITACIÓN CVU [client]`, `CVU CRÉDITO` | Fee income |
| I-03 | `MERCADOPAGO COBRO`, `MP COBRO [client]` | Fee income at gross; fee is an expense if documented |
| I-04 | `DEBIN RECIBIDO [client]` | Fee income |
| I-05 | `PAYPAL RETIRO`, `PAYPAL TRANSFER` | Fee income. Source follows where the work is done (art. 5), not the platform. Rate: see Cross-border points |
| I-06 | `STRIPE PAYOUT`, `STRIPE AR` | As I-05; not by payer country |
| I-07 | `RAPIPAGO COBRO`, `PAGO FÁCIL COBRO` | Fee income |
| I-08 | `DEVOLUCIÓN GANANCIAS ARCA`, `REINTEGRO ARCA` | Not income |
| I-09 | `INTERESES PLAZO FIJO`, `RENDIMIENTO FCI` | Test the actual product and holder: qualifying bank interest art. 26(h), principal update art. 26(t), ordinary non-exempt capital return arts. 48(a)/94; an FCI label proves no bank exemption |
| I-10 | `DIVIDENDOS [company]` | Art. 97 |
| I-11 | `ALQUILER COBRADO`, `RENTA INMUEBLE` | First category; from 2026 apply the exclusive unique/family/permanent-home conditions in art. 26(n)/Decreto 862 art. 83 before treating rent as exempt |
| E-01 | `ALQUILER OFICINA`, `LOCACIÓN COMERCIAL` | Expense if linked to taxed income |
| E-02 | `EDESUR`, `EDENOR`, `EPEC`, `EPE` | Business share only |
| E-03 | `METROGAS`, `NATURGY`, `CAMUZZI` | Business share only |
| E-04 | `PERSONAL`, `CLARO`, `MOVISTAR`, `TELECOM` | Business share only |
| E-05 | `ADOBE`, `MICROSOFT 365`, `GOOGLE WORKSPACE` | Expense if linked to taxed income; percepción may be on the same line |
| E-06 | `CONTADOR`, `ESTUDIO CONTABLE`, `HONORARIOS CPN` | Expense if linked to taxed income |
| E-07 | `AEROLÍNEAS ARGENTINAS`, `FLYBONDI`, `JETSMART` | Expense with business purpose; personal travel barred by art. 92(a) |
| E-08 | `HOTEL`, `BOOKING.COM`, `AIRBNB` | As E-07 |
| E-09 | `JUBILACIÓN AUTÓNOMOS` | Art. 85(d), and evidence for the art. 98 test. Monotributo payments are not autónomo contributions: stop, R-AR-1 |
| E-10 | `OBRA SOCIAL`, `PREPAGA`, `OSDE`, `SWISS MEDICAL` | Art. 85(f): classify obligatory or voluntary first; the 5% cap applies to voluntary cover |
| E-11 | `SEGURO PROFESIONAL`, `RC PROFESIONAL` | Expense if linked to taxed income |
| E-12 | `COLEGIO PROFESIONAL`, `CPACF`, `MATRÍCULA` | Expense if linked to taxed income |
| E-13 | `PAGO GANANCIAS ARCA`, `VEP GANANCIAS` | Not deductible, art. 92(d); credit only if a payment on account of the period |
| E-14 | `ANTICIPO GANANCIAS`, `VEP ANTICIPO` | Not deductible; credit on the return |
| E-15 | `PERCEPCIÓN RG 5617`, `PERCEPCIÓN RG 4815`, `PERC. DÓLAR`, `IMP. PAÍS` | Percepción: credit, not a deduction. `IMP. PAÍS`: not a credit |
| E-16 | `MARKETING`, `PUBLICIDAD`, `GOOGLE ADS` | Expense if linked to taxed income |
| E-17 | `PAPELERÍA`, `INSUMOS OFICINA` | Expense if linked to taxed income |
| E-18 | `SERVICIO DOMÉSTICO` | Casas Particulares, capped at the annual GNI amount; not a business expense |
| E-19 | `ALQUILER VIVIENDA`, `INQUILINO` | Art. 85(h), personal, 40% capped; test the no property condition |

Exclude as non-income and non-deductible until reviewed: `COMISIÓN BANCARIA` and `MANTENIMIENTO CTA` where personal, and bank names alone: `BANCO NACIÓN`, `BNA`, `BANCO GALICIA`, `GALICIA`, `SANTANDER ARGENTINA`, `BBVA ARGENTINA`, `MACRO`, `BANCO MACRO`, `BRUBANK`, `UALA`, `NARANJA X`. A fee on a business account may be an expense; check for a separate subscription on fintech accounts. `INTERESES` and `INTERÉS PRÉSTAMO`: ask the purpose, because art. 85(a) allows interest only on debt shown to have bought goods or services used to earn taxed income. Loans (`PRÉSTAMO PERSONAL`, `CUOTA PRÉSTAMO`): principal is neither income nor expense. `ARCA`, `AFIP`, `ANSES`: read the concept code, and see E-09, E-13 and E-14. `RENTAS [province]`, `ARBA`, `AGIP`, `DGIP`, `MUNICIPALIDAD`: provincial and municipal taxes such as Ingresos Brutos are not credits here; whether each is an expense is a reviewer question under arts 83 and 86(a). `TRANSFERENCIA PROPIA`, `CUENTA PROPIA`: internal, exclude. `EXTRACCIÓN ATM`, `RETIRO EFECTIVO`: exclude by default and ask the purpose.

### Bank exports

Not verified at any bank's site or against a real export; compare every row with the file received. Argentine exports usually show the period as thousands separator and the comma as decimal (`1.200.000,00`) and DD/MM/YYYY dates.

| Source | Expected columns, unverified | Narrations |
| --- | --- | --- |
| Banco de la Nación Argentina (PDF, CSV) | `Fecha;Concepto;Débito;Crédito;Saldo` | `TRANSFERENCIA CR [sender]`, `ACREDITACIÓN [sender]` |
| Banco Galicia (CSV, Excel) | `Fecha;Descripción;Débito;Crédito;Saldo` | `TRF CVU [sender]`, `TRANSFERENCIA [sender]` |
| Santander Argentina (CSV, PDF) | `Fecha;Concepto;Importe;Saldo`; positive is credit | |
| BBVA Argentina (CSV, PDF) | `Fecha;Detalle;Débito;Crédito;Saldo` | `TRF RECIBIDA DE [sender]` |
| Banco Macro (CSV) | `Fecha;Movimiento;Débito;Crédito;Saldo` | |
| Brubank, Ualá, Naranja X (CSV, PDF) | One signed column or 2 columns | `Transferencia recibida de [sender]`, `MP COBRO [amount]` |
| Mercado Pago | Settlements appear in the main bank statement | `MERCADOPAGO`, `MP COBRO`, `LIQUIDACIÓN MP`; gross up for fees |

CVU is the identifier for fintech wallets, and CBU for bank accounts. Both show as credits with the sender's identification. No bank source confirms the currency, so confirm it for each account and statement before treating amounts as pesos.

### Reviewer catalogue

| Code | Situation | Treatment |
| --- | --- | --- |
| T2-AR-1 | Monotributo or responsable inscripto choice | Depends on turnover, expenses and position. Contador Público decides; do not compute under the wrong regime |
| T2-AR-2 | Home office proportion | Reviewer confirms a documented proportion under art. 83 |
| T2-AR-3 | Car business use | Reviewer confirms the percentage and the arts 86(f) and 92(l) limits |
| T2-AR-4 | Which table applies | Reviewer confirms the annual table for the period |
| T2-AR-5 | Bienes Personales | Separate computation and return; verify assets and threshold |
| T2-AR-6 | Foreign-source income of a resident | Taxed worldwide; escalate, R-AR-4 |

### Working paper template

```text
ARGENTINE GANANCIAS WORKING PAPER (AUTÓNOMO / PROFESIONAL INDEPENDIENTE)
Working paper only. Not a filing position.
Taxpayer: _______________  CUIT: _______________  Fiscal period: ____

A  INCOME                                     ARS
4th category (fees, art. 82 f, g):      ___________
1st category (rent):                    ___________
2nd category (financial):               ___________
Foreign-source income (held, R-AR-4):   ___________
TOTAL GROSS                             ___________

B  EXPENSES (arts 83 to 88)
Office rent:                            ___________
Utilities (business share):             ___________
Phone and internet (business share):    ___________
Software:                               ___________
Accounting and legal fees:              ___________
Travel (business purpose):              ___________
Marketing and advertising:              ___________
Staff pay and contributions:            ___________
Office supplies:                        ___________
Professional insurance:                 ___________
Professional body fees:                 ___________
TOTAL EXPENSES                          ___________

C  NET INCOME
Gross - expenses:                       ___________
Current year losses (art. 25):         (___________)
NET INCOME AFTER LOSSES                 ___________

D  GENERAL DEDUCTIONS (art. 85)
Retirement contributions:               ___________
Health cover (obligatory; voluntary 5% cap): ______
Life insurance (period cap):            ___________
Casas Particulares (GNI cap):           ___________
Home rent (40%, GNI cap):               ___________
Donations (5% cap):                     ___________
TOTAL GENERAL DEDUCTIONS                ___________

PRIOR YEAR LOSSES (art. 25):            ___________

E  ART. 30 AMOUNTS (annual table for the period)
Ganancia no imponible:                  ___________
Deducción especial, min(table, qualifying net, amount remaining): ___
Cónyuge:                                ___________
Children (x ___):                       ___________
TOTAL ART. 30                           ___________

F  GANANCIA NETA IMPONIBLE, max(C - D - prior year losses - E, 0): ____
G  TAX ON THE ART. 94 TABLE:            ___________

H  CREDITS
Anticipos paid:                        (___________)
Retenciones:                           (___________)
Percepciones (RG 5617):                (___________)
BALANCE DUE / (SALDO A FAVOR)           ___________

I  REVIEWER FLAGS
[ ] Category confirmed (autónomo, not employee or Monotributo, no R-AR-7 mix)?
[ ] Annual table for the period used?
[ ] Every expense documented or otherwise proved?
[ ] Art. 40 tested against art. 41 and all 3 limbs of Decreto 862/2019 art. 106?
[ ] Each dependant's net income at or below the art. 30(a) amount?
[ ] Contributions paid and matching ARCA's amounts (art. 98)?
[ ] Percepción documents matched to the period and the name on them?
[ ] Bienes Personales assessed separately?
[ ] Foreign-currency receipts converted on a confirmed basis?
```

### Known gaps

Everything on the 'Not yet confirmed' line after Sources stays open. Client-facing wording for these gaps is in Ask the client first.

## Deadlines and filing

**Portal and form.** The return is prepared in the ARCA service 'Ganancias Personas Humanas - Portal Integrado', with Clave Fiscal at security level 2 or above (RG 5692 art. 2). The general regime uses form F. 711. The simplified regime uses form F. 2711. F. 711 is due where the person is registered, even with no taxable income, or where the tax is due even if not registered (art. 3). The balance is paid by VEP code 11-019-019 through 'Presentación de DDJJ y Pagos', by ARCA's electronic wallet or by a payment plan under RG 5321. A saldo a favor can be claimed through 'DEVOLUCIONES Y/O TRANSFERENCIAS - Versión 4.0'.

| Obligation | Date | Basis |
| --- | --- | --- |
| Ganancias return, period 2025, general or simplified | 16 November 2026, all CUIT | RG 5851 art. 1 as substituted by RG 5918 art. 1, and ARCA's 'Vencimientos' page. Replaced dates: RG 5876 (27 August), RG 5890 (22 September), RG 5898 (13 October), RG 5911 (30 October). Source conflict: Biblioteca's RG 5851 text labelled current under RG 5918 still prints 30 October 2026 |
| Ganancias balance, period 2025 | 27 July 2026, all CUIT. The later filing date does not move it | Same. Interest runs from the due date, Ley 11.683 art. 37 |
| Bienes Personales return and balance, period 2025 | 27 July 2026 | RG 5851 art. 1, second paragraph. Not the same date as Ganancias for this period |
| Ordinary rule, Ganancias | June of the following year on the schedule set each year by CUIT ending; balance on the next administrative business day | RG 5692 art. 5. Exact days are in the RG 4172 calendar, not read |
| Anticipos | 5 a year: August, October and December of the year after the base year, then February and April | ARCA anticipos page. Exact days held |
| First anticipo, period 2026 | 24 September 2026 | RG 5876 art. 2 as substituted by RG 5890 art. 2 |

**Anticipos.** Each is 20% of the base on ARCA's page, and they are due only if the amount is ARS 5,000 or more. The base takes the previous period's net result before art. 30, less the art. 30 amounts computed, both updated by IPC for July to December. It applies the updated art. 94 scale, then takes off promotional tax reductions, net computable retenciones and percepciones of the base period other than final ones, payments on account substituting retenciones, computable gasoil tax and computable analogous foreign tax. Those five deductible credits/reductions are themselves updated by the July-December IPC for the year before the anticipo period, under the same official instructions. Do not subtract retenciones/percepciones or gasoil credits attributable to the current anticipo year. The earlier version's 'bimonthly from June' was wrong. Where ARCA does not show the first or second anticipo for period 2026 because the 2025 return is unfiled, the taxpayer computes them from their own working papers (RG 5876 art. 2, second paragraph). Reduction goes through Cuentas Tributarias on the terms of ARCA's page and RG 5211, which was read only through that page.

**Simplified return.** Individuals and undivided estates resident for the whole period may opt in, and for period 2025 being resident at any time in the year is enough. ARCA lists as requirements a CUIT not limited by an observed digital CUIT request, not being a subject under RG 3832 art. 3, and registration in Ganancias, which can be done when opting in. Ley 27.826 art. 3 replaced art. 38 of Ley 27.799 and dropped its ceilings of ARS 1,000,000,000 of income and ARS 10,000,000,000 of wealth, and ARCA's requirements page lists no income ceiling. Grandes Contribuyentes Nacionales and art. 38 bis officials may join only to file and pay. ARCA preloads the return, and the taxpayer may change, confirm and file it. Adhesion through 'Sistema Registral', option 'Ganancias Simplificada Ley 27.799', requires Clave Fiscal security level 3 or above under current RG 5820 art. 2; that is distinct from the Portal filing level 2 above. Annual ratification uses that option. Exercise adhesion from the first business day of the chosen period through its general return-filing deadline; annual ratification is possible with the prior simplified return or afterwards through the deadline of the period being ratified (RG 5820 arts. 2-3). Existing RG 5704 adopters for 2025 must convalidate by the 2025 filing deadline or the option is treated as withdrawn and the general regime applies. Under current art. 9, convalidation has effect only if the relevant balance was paid by the special balance deadline; a difference due to the fisc identified on filing must be paid by the special filing deadline with resarcitory interest. Do not confuse the later return date with a moved balance-payment deadline.

Ley 27.799 art. 39 requires acceptance and timely payment for the liberatory effect, with exceptions for omitted income, improper deductions and apocryphal documents. Art. 40 bis requires operations through authorised BCRA/CNV means in the formal financial system at origin or destination; its public-deed real-property cash exception is specific. Adherence does not cancel due-diligence duties. Whether this regime suits an autónomo remains a reviewer question: do not recommend its protection until those requirements and the current art. 40 significant-discrepancy tests are checked. The complete numeric protection tests and implementing-decree analysis remain explicitly unconfirmed here; absence of a discrepancy is not the only condition.

## Penalties and interest

| Item | Amount | Basis |
| --- | --- | --- |
| Late filing | ARS 220,000 for an individual, without prior demand. Halved by law, and not counted as a prior offence, if the return is filed and the fine paid between the general due date and 15 days after ARCA's notice | Ley 11.683 art. 38, amended by Ley 27.799 art. 15 |
| Automatic reduction | 25% off fines under arts 38 and 39 and the unnumbered articles after them, for individuals who are not Grandes Contribuyentes Nacionales | Art. 49 bis, added by Ley 27.826 art. 2, effective 9 October 2026 |
| One-off reduction | 50% off formal fines under arts 38 and 39 and the unnumbered articles after them, for infractions before Ley 27.826, not final or not paid, on obligations due from the start of Ley 27.799, for the same individuals, if the formal duty is met first or at the same time. Taking it means unconditional acceptance of the claim for the unreduced part, waiver of all actions and rights, and paying costs where due, even if the matter is in dispute. It gives no refund of amounts paid before the law | Ley 27.826 art. 17 |
| Formal breaches | Ordinary first-paragraph range ARS 150,000 to ARS 2,500,000. The specified fiscal-domicile, qualified repeated resistance, international-operation data and pricing-evidence breaches can reach ARS 35,000,000; test the actual paragraph and conditions | Art. 39 |
| Omission | 100% of the tax not paid, unless art. 46 applies or there is excusable error. Covers tax or anticipos unpaid through a missing or inexact return | Art. 45 |
| Omission linked to foreign parties | 200%. The text covers local companies, businesses, trusts or permanent establishments dealing abroad. Application to an individual autónomo is held | Art. 45 second paragraph |
| Repeat omission | 200%; 300% where the second paragraph applies | Art. 45 third paragraph |
| Fraud | 2 to 6 times the tax evaded | Art. 46. The earlier '200-1000%' was wrong |
| Voluntary correction, no repeat offence | Filing before an order of intervention: exempt. Before the prior view: 1/4 of the legal minimum. Before the art. 17 view: 1/2. Accepted within the first 15 days after the view: 3/4. Agreed assessment: legal minimum | Art. 49 |
| Resarcitory interest | 2.75% a month from 1 July 2025; 4% from 1 March to 30 June 2025 | Art. 37; Resolución MEC 3/2024, as amended by 199/2025 and 823/2025 |
| Punitive interest | 3.50% a month from 1 July 2025, once a claim is in court | Art. 52; same resolutions |
| Refund interest | 0.50% a month from 1 July 2025 | Same resolutions |
| Undocumented payments | 35% final charge on the conditions in The base | LIG arts 40 and 41. Not a penalty under Ley 11.683 |
| Prescription | 5 years if registered, if not registered with no duty to register, or if the duty was unmet and the position is regularised voluntarily; reduced to 3 for a registered taxpayer if the return was filed on time and any balance regularised and ARCA does not challenge it for a significant discrepancy; 10 years for other non-registered taxpayers | Art. 56 |

The earlier version's '1% per month' for late filing has no basis in Ley 11.683 and is removed. Criminal thresholds under the penal tax regime are not stated here; they were changed by Ley 27.799 and are to be read for any case that needs them.

## Cross-border points

Residents are taxed on worldwide income, with foreign taxes paid credited up to the limit in the law (LIG art. 1). Residence is in arts 116, 117 and 119.

Source is not set by who pays. Art. 5 treats as Argentine source income from any act or activity carried out in Argentine territory, whatever the nationality, domicile or residence of the parties or the place the contract was made. An autónomo working in Argentina for a foreign client therefore has Argentine-source income on that test, subject to the special rules in the following articles. The earlier version labelled PayPal and Stripe receipts 'foreign source'; that is withdrawn.

Foreign-source income under Title VIII is computed in pesos on the dates and rates the regulation sets (art. 129). Foreign tax credits are limited by arts 165 and 166. Foreign-source losses stay in that basket (art. 131). Any treaty question stops at R-AR-4.

The rate for converting Argentine-source fees received in foreign currency was not established. The earlier version's 'ARCA exchange rate' is held.

## Worked examples

All names are illustrative. Each block runs under the repository's example checker, and the drafter recomputed the outputs with a separate script from the tables above. Credits such as anticipos are left out unless shown.

### Example 1: Banco Nación, IT consultant, period 2025, is the client a nuevo profesional?

Martín López is an IT consultant in Buenos Aires, registered and paying his autónomo contributions in full and on time. Confirm that his work is a profession or trade under art. 82(f) and is not a commercial service. The statement lines below are a sample; annual totals are given facts and do not derive from them.

```text
Fecha;Concepto;Débito;Crédito;Saldo
05/01/2025;TRANSFERENCIA CR EMPRESA TECH SA;;1.200.000;
15/01/2025;COMISIÓN BANCARIA;1.500;;
10/02/2025;TRANSFERENCIA CR STARTUP DIGITAL SRL;;850.000;
28/02/2025;VEP JUBILACIÓN AUTÓNOMOS;180.000;;
15/03/2025;PAYPAL RETIRO;;420.000;
31/03/2025;ANTICIPO GANANCIAS VEP;250.000;;
20/04/2025;MERCADOPAGO COBRO;;380.000;
05/06/2025;TRANSFERENCIA CR GAMMA CONSULTING SA;;1.500.000;
10/07/2025;ESTUDIO CONTABLE PÉREZ;120.000;;
10/10/2025;AEROLÍNEAS ARGENTINAS;95.000;;
```

Patterns: I-01, I-03 and I-05 for credits, E-06, E-07, E-09 and E-14 for debits. Check retenciones on the domestic company payers. Annual gross income is ARS 28,000,000. Expenses are accounting 1,440,000, travel 1,140,000 and software 480,000, so 3,060,000. Contributions of 2,160,000 go once, as a general deduction. The earlier version counted them twice.

Case A is an established professional. Case B has 3 years or less in the matrícula or, for an independent worker with none, since registering as such (Decreto 862/2019 art. 99).

```oa-check
name: AR 2025 autonomo, standard and nuevo profesional deduccion especial
inputs:
  gross: 28000000
  expenses: 3060000
  contributions: 2160000
  gni: 4507505.52
  de_standard: 15776269.32
  de_nuevo: 18030022.08
steps:
  - net: gross - expenses - contributions
  - de_a: min(de_standard, net)
  - taxable_a: max(net - gni - de_a, 0)
  - tax_a: round(87495.07 + (taxable_a - 1749901.45) * 0.09, 2)
  - de_b: min(de_nuevo, net)
  - taxable_b: max(net - gni - de_b, 0)
  - tax_b: round(taxable_b * 0.05, 2)
  - difference: tax_a - tax_b
expected:
  net: 22780000
  taxable_a: 2496225.16
  tax_a: 154664.20
  taxable_b: 242472.40
  tax_b: 12123.62
  difference: 142540.58
```

Case A falls in the 9% band, Case B in the 5% band. So the date of registration or matriculation, as art. 99 applies, changes the tax by ARS 142,540.58. The earlier ARS 704,477.88 used the wrong personal figure.

### Example 2: Banco Galicia, architect, period 2025, spouse and children

Lucía Fernández is an architect in Córdoba, married with 2 children under 18, contributions in order. Gross income 35,000,000; expenses 8,000,000; contributions 2,400,000; voluntary prepaga 600,000. Test the 5% cap first: the base is 24,600,000, so the limit is 1,230,000 and all 600,000 passes.

Case A: her spouse has net income at or below ARS 4,507,505.52, and she takes the cónyuge amount and both children. Case B: her spouse has net income of ARS 5,000,000, above that limit, and taxable income, so no cónyuge amount, and the parents split each child equally. Case C: as B, but Lucía takes 100% of the child amounts under Decreto 862/2019 art. 101.

```oa-check
name: AR 2025 architect, spouse income and child split decide the tax
inputs:
  gross: 35000000
  expenses: 8000000
  contributions: 2400000
  prepaga: 600000
  gni: 4507505.52
  de: 15776269.32
  conyuge: 4245166.13
  child: 2140852.77
  children: 2
steps:
  - base_5pct: gross - expenses - contributions
  - prepaga_allowed: min(prepaga, pct(base_5pct, 5))
  - net: base_5pct - prepaga_allowed
  - de_used: min(de, net)
  - taxable_a: max(net - gni - de_used - conyuge - child * children, 0)
  - taxable_b: max(net - gni - de_used - child * children / 2, 0)
  - tax_b: round(taxable_b * 0.05, 2)
  - taxable_c: max(net - gni - de_used - child * children, 0)
expected:
  prepaga_allowed: 600000
  net: 24000000
  taxable_a: 0
  taxable_b: 1575372.39
  tax_b: 78768.62
  taxable_c: 0
```

Result: nil in Cases A and C, ARS 78,768.62 in Case B. The earlier ARS 189,621.18 was wrong. If the spouse's net income is unknown, Cases A and B differ, so this is Needs Input. Check Bienes Personales separately.

### Example 3: BBVA Argentina, consultant with rent, period 2026, kind of let and the art. 98 cap

Patricia Vega is a consultant in Mendoza, contributions in order, with net self-employment income of ARS 22,000,000 and gross rent of ARS 6,000,000 under the presumed 5% method of art. 89. Case A: a commercial let, taxable. Case B: a dwelling let that is exclusively the tenant's unique, family and permanent home, meeting Decreto 862 art. 83 and exempt under art. 26(n) from 2026, so it stays out. Case C changes the facts to test the cap: self-employment net 10,000,000 and commercial rent 10,000,000 gross. The deducción especial stops at the qualifying income and does not shelter rent.

```oa-check
name: AR 2026 consultant, dwelling let exempt and deduccion especial cap
inputs:
  self_net: 22000000
  rent_gross: 6000000
  self_net_c: 10000000
  rent_gross_c: 10000000
  gni: 6019671.36
  de: 21068849.78
steps:
  - rent_net: rent_gross - pct(rent_gross, 5)
  - de_a: min(de, self_net)
  - taxable_a: max(self_net + rent_net - gni - de_a, 0)
  - tax_a: round(taxable_a * 0.05, 2)
  - taxable_b: max(self_net - gni - de_a, 0)
  - rent_net_c: rent_gross_c - pct(rent_gross_c, 5)
  - de_c: min(de, self_net_c)
  - taxable_c: max(self_net_c + rent_net_c - gni - de_c, 0)
  - tax_c: round(116847.68 + (taxable_c - 2336953.69) * 0.09, 2)
expected:
  rent_net: 5700000
  taxable_a: 611478.86
  tax_a: 30573.94
  taxable_b: 0
  de_c: 10000000
  taxable_c: 3480328.64
  tax_c: 219751.43
```

For period 2025 the same dwelling let would still be taxable, because the exemption starts with years from 1 January 2026. Flag Bienes Personales for the property.

### Example 4: Santander Argentina, percepciones above the tax

Diego Ruiz is a digital creator with gross income of ARS 18,000,000. His computed tax of ARS 1,200,000 is a given fact here, not derived. Percepciones under RG 5617 are ARS 3,500,000.

```oa-check
name: AR percepciones as credit produce a saldo a favor
inputs:
  tax: 1200000
  percepciones: 3500000
steps:
  - balance_due: max(tax - percepciones, 0)
  - saldo_a_favor: max(percepciones - tax, 0)
expected:
  balance_due: 0
  saldo_a_favor: 2300000
```

Match every percepción to its document and period first. Any charge for buying dollars as an individual after RG 5672 took effect should not exist, and an `RG 4815` label alone does not prove the period: RG 5617 art. 19 allowed agents to keep older labels until 31 March 2025. Test the actual operation/perception date and applicable regime. The balance is ingreso directo under RG 5617 art. 7.

### Other legacy examples

**Brubank, low income, period 2025.** Ana García is single, with gross 15,000,000, expenses 4,000,000 and contributions 1,800,000, so net 9,200,000. The deducción especial stops at 9,200,000 under art. 98, so ganancia neta imponible is max(9,200,000 - 4,507,505.52 - 9,200,000, 0) = 0. Tax nil. If the contributions were paid, so still deductible, but late and outside a payment plan, the art. 98 test fails. The deducción especial then falls away and the result is max(9,200,000 - 4,507,505.52, 0) = 4,692,494.48, on which tax would be ARS 244,986.20 + (4,692,494.48 - 3,499,802.89) x 12% = ARS 388,109.19.

**Banco Macro, undocumented expenses.** Dr Carlos Méndez, a physician in Tucumán, claims ARS 2,000,000 with no invoices. Test other evidence, art. 41 and Decreto 862/2019 art. 106 first. Signs of goods, or a founded presumption that the payment is not taxable in the recipient's hands, remove the tax. Proof of a service may save the deduction and still leave the 35%. If none helps, art. 40 denies the deduction and charges 35%, which on the ARS 2,000,000 paid would be ARS 700,000; any gross-up is held. Art. 83 is not the article that denies it.

## Ask the client first

1. **Status.** Is the client a resident responsable inscripto in Ganancias, in Monotributo or an employee? What activities produce income, is any a commercial business combined with a profession, and is any from employment or a pension? Say: 'Please confirm your status with your Clave Fiscal at www.arca.gob.ar. If you are in Monotributo, this file does not apply.'
2. **Identity and period.** What are the CUIT, the fiscal period, and for a nuevo profesional or emprendedor the date of matriculation or registration?
3. **Contributions.** Which autónomo category was declared, and was every month paid by the due date or put in a payment plan? Are there other cajas?
4. **Family.** Is there a spouse or registered partner? What was the net income in the year of each dependant, from any source? Who has parental responsibility, and how is each child's amount split?
5. **Income, expenses and credits.** What are the 12 months of statements, the invoices or other proof of expenses, health cover by type, rent paid or received and the kind of let, foreign receipts and anticipos? What documents show percepciones and retenciones? Say: 'Argentine law denies an undocumented expense unless other evidence proves it, and art. 40 may charge 35%. Even with that evidence, if it shows a service, the expense may be allowed and the 35% may still apply.' The ARCA services the earlier version named for this ('Mis Comprobantes', 'Mis Retenciones') were not confirmed at ARCA; the bank or card document is what RG 5617 art. 5 names.
6. **Wealth.** What real estate, vehicles, investments and bank balances were held at 31 December, in Argentina and abroad? Say: 'Bienes Personales is a separate tax on assets above a threshold ARCA publishes. For period 2025 it fell due on 27 July 2026, not with Ganancias.'

Before any output, check the items in the Reviewer flags block.

## Sources

Read on means the date read for this conversion. Limits follow each source. Current official ARCA and Argentina.gob consolidations were read for the portions stated below. Original Infoleg links returned access errors in this pass and are replaced with substantive official alternatives. Embedded earlier versions are distinguished from current law. Amending laws were read only for their named scopes; Ley 27.743 remains sourced through the consolidated notes. The source-read date below does not claim a review of every historic provision in each long text. Amounts come from ARCA's own PDFs, and the operative pages of both annual art. 30 tables were checked visually because text extraction scrambled them.

| Source | URL | Read on |
| --- | --- | --- |
| Read for LIG t.o. 2019, Decreto 824/2019, updated: read for arts 1, 5, 23 to 26, 29 to 31, 40, 41, 53, 82 to 89, 92, 94 to 99, 116 to 119, 129, 131, 132, 155, 165, 166 | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for Decreto 862/2019, updated: read for arts 98 to 101, art. 106 and the unnumbered article after art. 102 | https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 | 2026-11-11 |
| Read for indexed principal, interest exemption/netting, ordinary non-exempt capital returns and business exclusion: LIG arts. 26(h), (t) and penultimate paragraph, 48(a), 94, 108(a), 183; quotations: "Los montos provenientes de actualizaciones de créditos de cualquier origen o naturaleza.", "la exención estará limitada al saldo positivo" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for donation purposes and deduction residence: LIG arts. 33, 85(c); quotations: "más de SEIS (6) meses", "cuyo objetivo principal sea" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for index proof and causal interest netting: Decreto 862 arts. 85, 94; quotations: "índices fácilmente verificables y de público y notorio conocimiento", "Si de tal compensación surgiera un saldo negativo" | https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 | 2026-11-11 |
| Read for all current housing/rental/sale implementing changes: Decreto 406/2026 arts. 1-5; quotation: "a partir del 1° de enero de 2026" | https://www.argentina.gob.ar/normativa/nacional/decreto-406-2026-426274/texto | 2026-11-11 |
| Read for current housing-rent and property-sale conditions, landlord deduction exclusion and concurrent contribution tests: Decreto 862 arts. 83 and following unnumbered article, 98, 204 and both unnumbered articles after 204; quotations: "vivienda única, familiar y de ocupación permanente", "se devenguen a partir del 1° de enero de 2026", "en forma concurrente" | https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 | 2026-11-11 |
| Read for Ley 11.683 t.o. 1998, updated: read for arts 37 to 39, 45, 46, 49, 49 bis, 52, 56 | https://www.argentina.gob.ar/normativa/nacional/norma-18771/actualizacion | 2026-11-11 |
| Read for Ley 23.966 Bienes Personales, updated: read for arts 24 and 25 | https://www.argentina.gob.ar/normativa/nacional/norma-365/actualizacion | 2026-11-11 |
| Read for Ley 27.638: read in full | https://www.argentina.gob.ar/normativa/nacional/norma-352586/texto | 2026-11-11 |
| Read for Ley 27.541: read for arts 32 and 33 | https://www.argentina.gob.ar/normativa/nacional/norma-333564/texto | 2026-11-11 |
| Read for Ley 27.799: read for current Chapter III arts. 38-42 ter including payment/protection/formal-finance conditions, and art. 15 | https://www.argentina.gob.ar/normativa/nacional/norma-422008/actualizacion | 2026-11-11 |
| Read for Ley 27.802: read for arts 190 to 192 | https://biblioteca.arca.gob.ar/dcp/LEY_C_027802_2026_02_27 | 2026-11-11 |
| Read for Ley 27.826: read for arts 2 to 11 and 17 | https://www.argentina.gob.ar/normativa/nacional/norma-431078/texto | 2026-11-11 |
| Read for ARCA art. 94 table, annual 2025: read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-liquidacion-anual-y-final-2025.pdf | 2026-11-11 |
| Read for ARCA art. 94 table, annual 2026: read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-liquidacion-anual-y-final-2026.pdf | 2026-11-11 |
| Read for ARCA art. 94 table, January to June 2026: read in part, for the second band | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-per-ene-a-jun-2026.pdf | 2026-11-11 |
| Read for ARCA art. 30 table, annual 2025: read in full, checked visually | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2025.pdf | 2026-11-11 |
| Read for ARCA art. 30 table, annual 2026: read in full, checked visually | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf | 2026-11-11 |
| Read for ARCA art. 30 table, January to June 2025: read for the row values | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-enero-junio-2025.pdf | 2026-11-11 |
| Read for ARCA note on caps set by the GNI: read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/documentos/Deducciones-generales-tope-GNI-desde-2024.pdf | 2026-11-11 |
| Read for ARCA general deductions page: read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/deducciones-generales.asp | 2026-11-11 |
| Read for ARCA personal deductions page: read in full, a list of art. 30 tables | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/deducciones-personales.asp | 2026-11-11 |
| Read for ARCA page 'Determinación': read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/determinativa/determinacion.asp | 2026-11-11 |
| Read for ARCA page 'Presentación': read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/determinativa/presentacion.asp | 2026-11-11 |
| Read for ARCA page 'Saldos': read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/determinativa/saldos.asp | 2026-11-11 |
| Read for ARCA page 'Vencimientos': read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/determinativa/vencimientos.asp | 2026-11-11 |
| Read for ARCA page 'Anticipos': read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/determinativa/anticipos.asp | 2026-11-11 |
| Read for ARCA simplified return, requirements page: read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/simplificada/requisitos.asp | 2026-11-11 |
| Read for ARCA simplified return page: read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/simplificada/declaracion-jurada.asp | 2026-11-11 |
| Read for ARCA simplified return, ratification page: read in full | https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/simplificada/ratificacion.asp | 2026-11-11 |
| Read for RG 5692 ARCA, consolidated: read for arts 1 to 7 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5692%7Co:9%7Ca:2025%7Cf:07/05/2025 | 2026-11-11 |
| Read for RG 5851 ARCA, consolidated: read for art. 1. Its text labelled current under RG 5918 still prints 30 October 2026; RG 5918 art. 1 and ARCA's 'Vencimientos' page show 16 November 2026 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5851%7Co:9%7Ca:2026%7Cf:21/05/2026 | 2026-11-11 |
| Read for RG 5918 ARCA: read in full | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5918%7Co:9%7Ca:2026%7Cf:29/10/2026 | 2026-11-11 |
| Read for RG 5876 ARCA, consolidated: read for arts 1 and 2 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5876%7Co:9%7Ca:2026%7Cf:17/07/2026 | 2026-11-11 |
| Read for RG 5890 ARCA: read for arts 1 and 2 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5890%7Co:9%7Ca:2026%7Cf:24/08/2026 | 2026-11-11 |
| Read for RG 5898 ARCA: read for arts 1 and 2 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5898%7Co:9%7Ca:2026%7Cf:18/09/2026 | 2026-11-11 |
| Read for RG 5911 ARCA: read for art. 1 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5911%7Co:9%7Ca:2026%7Cf:07/10/2026 | 2026-11-11 |
| Read for RG 5820 ARCA current arts. 2-5 and 9, adoption/ratification timing, credential and convalidation/payment conditions; quotation: "Clave Fiscal con nivel de seguridad 3 o superior" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5820%7Co:9%7Ca:2026%7Cf:08/02/2026 | 2026-11-11 |
| Read for RG 5916 ARCA: read in part for the simplified regime | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5916%7Co:9%7Ca:2026%7Cf:23/10/2026 | 2026-11-11 |
| Read for RG 5617 ARCA, consolidated arts. 1-14 and 19 including pesos/FX scope and educational-software exclusion; quotations: "en la medida y la proporción que se abonen en pesos las operaciones alcanzadas", "software con fines educativos" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5617%7Co:9%7Ca:2024%7Cf:18/12/2024 | 2026-11-11 |
| Read for Resolución MEC 3/2024, consolidated: read for arts 1, 2 and 4 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RES%7Cn:3%7Co:6%7Ca:2024%7Cf:19/01/2024 | 2026-11-11 |
| Read for Resolución MEC 199/2025: read in full | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RES%7Cn:199%7Co:6%7Ca:2025%7Cf:27/02/2025 | 2026-11-11 |
| Read for Resolución MEC 823/2025: read in full | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RES%7Cn:823%7Co:6%7Ca:2025%7Cf:23/06/2025 | 2026-11-11 |
| Read for ARCA Bienes Personales rates page: read for the period 2025 scale | https://www.afip.gob.ar/gananciasYBienes/bienes-personales/conceptos-basicos/alicuotas.asp | 2026-11-11 |
| Read for ARCA Bienes Personales concepts page: read for the minimum and dwelling limit | https://www.afip.gob.ar/gananciasYBienes/bienes-personales/conceptos-basicos/que-es.asp | 2026-11-11 |

Not yet confirmed: historical 2025 application and any disputed scope of the current Decreto 406 art. 3 landlord exclusion; complete current simplified-return significant-discrepancy/protection numeric tests; whether proof that a payment was for a service lifts the art. 40 tax, given Decreto 862/2019 art. 106; that ARCA's annual tables are the amounts in effect from 1 July, which is inferred; the proportion in RG 5617 art. 7 for a dependant's percepciones; exact days for the ordinary return and for anticipos 2 to 5 of period 2026 (RG 4172 calendar not read); RG 5211 itself; Decreto 93/2026, Decreto 1160/2026 and Decreto 1253/2026; import percepciones under RG 2281; whether the 35% in art. 40 is grossed up; the rate for converting Argentine-source fees received in foreign currency; retention rates under RG 830; the current running cost cap for cars under art. 92(l); treaty treatment of foreign income; whether art. 45's 200% limb reaches an individual; Ley 26.063 art. 16; the penal tax thresholds; indexed Bienes Personales amounts for 2026 and the conditions for its contribuyentes cumplidores scale; the ARCA service names 'Mis Comprobantes' and 'Mis Retenciones'; bank export formats; any later change after this 11 November 2026 read. The RG 5851 display conflict is reconciled above in favour of direct RG 5918; it is a publication defect, not a choice between equal due dates.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.4 | 2026-11-11 | Advanced to 2026 from Ryan Duguid's merged v2.3; retained the full dated 2025 material and old topics. Added current housing/sale conditions, indexed-principal and interest netting/classification rules, and corrected the contribution/mixed-income explanation. |
| 2.3 | 2026-11-05 | Converted to the upstream template. Added 2026 tables and the 2026 reforms. Corrected the deducción especial multiple and its conditions, art. 40, categories, percepciones, anticipos, filing dates, Bienes Personales and penalties. All computed examples replaced. |
| 2.2 | 2026-11-01 | Legacy version. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
