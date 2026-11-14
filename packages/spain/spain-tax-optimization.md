---
name: spain-tax-optimization
description: >
  Use this skill whenever asked about reducing tax in Spain, tax planning,
  saving tax, optimizing tax, allowances, deductions the client might be
  missing, or any question about legal strategies to minimize income tax
  liability for self-employed individuals (autónomos) in Spain. Trigger on
  phrases like "reduce tax", "tax planning", "save tax", "optimize",
  "allowances", "deductions I'm missing", "pagar menos impuestos",
  "optimización fiscal", "ahorrar en impuestos", "deducciones IRPF",
  "autónomo fiscal". It covers the common-regime IRPF, estimación directa and
  módulos, autónomo or SL, RETA, IVA, pensions and the LGT arts 15 and 16
  limits, with filing on the AEAT Sede and Import@ss. ALWAYS read this skill
  before advising on any Spanish tax optimization strategy. This Tier 2 draft
  supports source checking and reviewer questions; it does not authorise a
  tax position.
version: 1.4
jurisdiction: ES
tax_year: 2026
tax_year_notes: "Planning for income of 2026, declared in 2027; baseline reading 6 November 2026 and additional repair units read 7 November 2026. State IRPF rules and the 2026 RETA order are read as in force at that date. Autonomous scales are those of the AEAT Manual for 2025, because the 2026 scales were not read. No Budget Act for 2026 was found and that absence is held. País Vasco and Navarra are out of scope."
last_updated: 2026-11-14
depends_on: []
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: tax-optimization
type: situation-rules
---

# Spain Tax Optimization v1.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Spanish tax residents under the common regime who are self-employed (autónomos in estimación directa or estimación objetiva) or who own and run a sociedad limitada (SL), and their households. Tax residence is a fact to establish, not a default.

Out of scope: residents of País Vasco and Navarra, whose foral regimes LIRPF art. 4.2 leaves in place; none of the scales or deductions here apply to them. Canarias, Ceuta and Melilla have their own rules (LIRPF art. 4.3): this guide notes some of them and does not cover them. Non-residents are out of scope, apart from the art. 93 option below.

### What this file is

**Coverage label: planning for income of 2026, declared in 2027; baseline reading at 6 November 2026, with the additional repair units in Sources read at 7 November 2026.** The state scale, the savings scale and the IS, IVA and LGT rules are read in BOE consolidated text as updated to the dates on the Sources rows. Autonomous scales are those of the AEAT Manual for 2025, because the 2026 scales were not read. This file lists rules and the condition on which each one works. It does not say what a named client should do. Each comparison gives the arithmetic and leaves the choice to the client and a Spanish adviser.

This guide has no `depends_on` base. It leans on these siblings, which own their figures:

- [es-income-tax](es-income-tax.md): the IRPF computation and Modelo 100.
- [es-social-contributions](es-social-contributions.md) and [es-autonomous-worker](es-autonomous-worker.md): RETA in full. Both state the reduced cuota at EUR 80 with no hold for 2026, and the second says never to apply it to societarios; see 'Not yet confirmed'.
- [es-corporate-tax](es-corporate-tax.md): the IS computation.
- [es-beckham](es-beckham.md): the art. 93 option and its forms.
- [es-estimated-tax](es-estimated-tax.md): Modelo 130 and 131.
- [es-capital-gains](es-capital-gains.md): savings income.
- [spain-vat-return](spain-vat-return.md): Modelo 303 and 390 lines, rates and place of supply.
- [spain-transfer-pricing](spain-transfer-pricing.md): related-party documentation.
- [spain-formation](spain-formation.md): forming an SL.

### Refusals

Each refusal is a full stop. Give the message and do no partial planning.

| Trigger | Exact message |
| --- | --- |
| The client asks to design, paper over or defend a sham act, a false invoice, hidden income, or an arrangement that meets both limbs of LGT art. 15.1 | I cannot design or support this. It may fall within LGT art. 15 or 16 or Código Penal arts 305 to 310, and it needs a qualified Spanish adviser before anything is done. |
| Spanish tax residence is unknown or denied | I cannot apply these planning rules until Spanish tax residence is established. Please confirm it with a qualified Spanish adviser. |
| The client lives in País Vasco or Navarra | This guide covers the common regime only. The foral rules of your territory apply, and I cannot use these figures for them. |
| The client wants a final IRPF figure for income of 2026 | The autonomous scales for 2026 were not read for this guide, so any figure for income of 2026 is provisional. I can show that figure, labelled with the scale used, and nothing more. |
| The client wants the module limits for 2026 or 2027 stated as settled | The statute and the AEAT's stated criterion differ for 2026, and the limit for 2027 is unconfirmed. I can show both positions and the consequence of each. A Spanish adviser must decide which to rely on. |

### Rules for every answer

1. Questions come first. Ask the facts in 'Ask the client first' before any figure or comparison. Whatever stays unanswered is **Needs Input**: do not fill it with an assumed rate, status, community or election.
2. Give each strategy with its condition. A strategy with an unmet condition is not available, and an unknown condition is Needs Input.
3. A bill is not law. The draft módulos order for 2027 and any unpublished Budget Act figure are never used.
4. Every comparison states whether social contributions are in it. Where they are not, say so: the answer is an income tax comparison only.
5. A comparison is arithmetic on stated inputs. Do not name a turnover or profit at which a client should incorporate, and do not call either structure better. Legal liability, financing, costs and pension cover also bear on that choice and are outside this file.
6. A tax motive alone does not trigger the first refusal. LGT art. 15.1 needs both limbs: acts notoriously artificial or improper for the result, and no relevant legal or economic effects beyond the tax saving and the effects of the usual act. Art. 16 needs a sham. A choice the law offers, such as a pension contribution within its limit, stays available on its conditions. If the facts do not show whether a limb is met, that point is Needs Input and goes to a qualified Spanish adviser.

### Red flags

- A combined state and autonomous rate is quoted with no community named.
- A cost is called 'automatic': the provisión needs EDS, and the art. 30.2.5ª amounts each have conditions.
- A saving is claimed from prepaying a cost under the accrual rule.
- A dividend or salary from the client's own SL is left out of the RETA income test.
- Income or a person is moved into an SL with no activity or staff to match.

## Rates, bands and thresholds

Read each table for its named year. Figures a sibling owns are repeated only where a worked example needs them.

**State general scale, LIRPF art. 63, in force for income of 2026 (needs no annual law)**

| Over | Up to | Rate on the fraction | Cuota at the lower limit | Source |
| --- | --- | --- | --- | --- |
| 0 | 12,450 | 9.5% | 0 | LIRPF art. 63: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| 12,450 | 20,200 | 12% | 1,182.75 | same |
| 20,200 | 35,200 | 15% | 2,112.75 | same |
| 35,200 | 60,000 | 18.5% | 4,362.75 | same |
| 60,000 | 300,000 | 22.5% | 8,950.75 | same |
| 300,000 | and above | 24.5% | 62,950.75 | same |

The scale runs in 2 steps: the scale on the base liquidable general, less the scale on the personal and family minimum. EUR 5,550 is the basic taxpayer minimum only (art. 57), increased by EUR 1,150 when age is over 65 and a further EUR 1,400 when over 75. The complete personal and family minimum combines the applicable taxpayer, descendant, ascendant and disability components (arts 56 to 60). Apply art. 61's income, return-filing, sharing and assessment-date conditions before computing family components. Each community then applies its own scale (art. 74) in the same 2 steps and can set its own minimum. Autonomous amounts for 2026 remain unverified.

There is no single combined rate. The law gives no 'typical combined' figure, so none is given here.

**Autonomous scales, first and top rate, income of 2025 (2026 scales not read)**

| Community | First rate | Top rate | Top rate from | Source |
| --- | --- | --- | --- | --- |
| Andalucía | 9.5% | 22.5% | 60,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-andalucia.html |
| Aragón | 9.5% | 25.5% | 130,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-aragon.html |
| Asturias | 9% | 26% | 175,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-principado-asturias.html |
| Illes Balears | 9% | 24.75% | 175,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-illes-balears.html |
| Canarias | 9% | 26% | 123,745 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-canarias.html |
| Cantabria | 8.5% | 24.5% | 90,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-cantabria.html |
| Castilla-La Mancha | 9.5% | 22.5% | 60,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-castilla-mancha.html |
| Castilla y León | 9% | 21.5% | 53,407.20 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-castilla-leon.html |
| Cataluña | 9.5% | 25.5% | 175,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-cataluna.html |
| Comunitat Valenciana | 9% | 29.5% | 200,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunitat-valenciana.html |
| Extremadura | 8% | 25% | 120,200 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-extremadura.html |
| Galicia | 9% | 22.5% | 60,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-galicia.html |
| Comunidad de Madrid | 8.5% | 20.5% | 57,320.40 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-madrid.html |
| Región de Murcia | 9.5% | 22.5% | 60,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-region-murcia.html |
| La Rioja | 8% | 27% | 120,000 | AEAT Manual IRPF 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-rioja.html |

With the state's 24.5%, the top combined rates run from 45% (Madrid) to 54% (Comunitat Valenciana). Madrid has the lowest top rate of the 15, and La Rioja and Extremadura the lowest first band. Each community's bands differ, so compare whole scales and never these 2 rates alone. For habitual residents of Ceuta or Melilla, LIRPF DA 32ª imports the art. 65 scale for the autonomous component. It does not replace the state component. Territorial eligibility and calculations remain outside this guide's verified scope.

**Madrid scale for 2025, used as a labelled stand-in in the examples**

| Over | Up to | Rate on the fraction | Cuota at the lower limit | Source |
| --- | --- | --- | --- | --- |
| 0 | 13,362.22 | 8.5% | 0 | AEAT Manual IRPF 2025, Comunidad de Madrid: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-madrid.html |
| 13,362.22 | 19,004.63 | 10.7% | 1,135.79 | same |
| 19,004.63 | 35,425.68 | 12.8% | 1,739.53 | same |
| 35,425.68 | 57,320.40 | 17.4% | 3,841.42 | same |
| 57,320.40 | and above | 20.5% | 7,651.10 | same |

Madrid's personal minimum for 2025 is EUR 5,956.65: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c14-adecuacion-impuesto-circunstancias-personales/minimo-autonomico-personal-familiar/comunidad-madrid-importes-minimo-personal-familiar.html

**Savings scale, LIRPF arts 66 and 76, state and autonomous halves together, from 1 January 2025**

| Over | Up to | Rate | Cuota at the lower limit | Source |
| --- | --- | --- | --- | --- |
| 0 | 6,000 | 19% | 0 | LIRPF arts 66 and 76: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| 6,000 | 50,000 | 21% | 1,140 | same |
| 50,000 | 200,000 | 23% | 10,380 | same |
| 200,000 | 300,000 | 27% | 44,880 | same |
| 300,000 | and above | 30% | 71,880 | same |

**Impuesto sobre Sociedades (IS), by the year the period starts**

| Entity | 2025 | 2026 | 2027 | Source |
| --- | --- | --- | --- | --- |
| General | 25% | 25% | 25% | LIS art. 29.1: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2014-12328/texto |
| Prior-period turnover (INCN) under EUR 1m, first EUR 50,000 of base | 21% | 19% | 17% | same, art. 29.1 and DT 44ª |
| Prior-period INCN under EUR 1m, rest of base | 22% | 21% | 20% | same |
| Entidad de reducida dimensión (art. 101, INCN under EUR 10m), not within the row above | 24% | 23% | 22% | same; 21% for periods starting in 2028 and art. 29.1's 20% after that |
| New entity, first period with a positive base and the next | 15% | 15% | 15% | same, art. 29.1 |

Both INCN thresholds use LIS art. 101.2-3's annualisation and aggregation tests. For a new entity, use its first period of actual activity. Annualise if the prior period or the activity lasted less than a year. Aggregate art. 42 groups regardless of residence or any consolidated-account duty, with the accounting eliminations and incorporations. The same rule covers art. 42 control of entities by an individual alone or with a spouse or relatives by blood or marriage through the second degree. Art. 101.4 continues reduced-size eligibility for the 3 periods after EUR 10m is reached if the entity or group qualified in that period and the 2 preceding periods. This also covers reaching EUR 10m through a qualifying Chapter VII, Title VII reorganisation if the participating entities meet that same 3-period eligibility test.

The micro rates apply 'unless a different rate from the general one applies'. The EUR 50,000 band is prorated by days for a period shorter than a year, or is the base if that is lower. An entity that is patrimonial under art. 5.2 is outside the micro, reduced-size and new-entity rates. The 15% does not apply where a related party carried on the activity and transferred it to the new entity, where in the year before formation an individual holding over 50% of the new entity carried it on, or where the entity belongs to a group under Código de Comercio art. 42.

**Activity income methods**

| Item | Amount | Source |
| --- | --- | --- |
| EDS: prior-year net turnover of all activities, annualised if an activity began in that year, at most | 600,000 | LIRPF art. 30.1 and RIRPF art. 28.2: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| EDS provisión: 5% of net income before this item, at most | 2,000 | RIRPF art. 30.2ª: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-6820/texto |
| Módulos limit, all activities, statute | 150,000 | LIRPF art. 31.1.1ª and 3ª b: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Módulos limit, of which to businesses and professionals, statute | 75,000 | same |
| Módulos limit, agriculture and forestry, statute | 250,000 | same |
| Módulos limit, purchases of goods and services excluding fixed assets, subcontracts counted, statute | 150,000 | same |
| Módulos reduction for 2026 | 5% | Orden HAC/1425/2025 DA 1ª: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2025-25272 |

The AEAT note of 1 April 2026 (https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html) applies higher 2026 limits by administrative criterion (250,000 all activities, 125,000 to businesses, 250,000 purchases). That conflicts with the statute above, so those figures are not usable guidance; see Not yet confirmed under Sources.

For the módulos income and purchase thresholds, annualise the prior-year volumes if an activity began during that year (LIRPF art. 31.1.3ª b and c). Apply the family and common-direction aggregation tests described below before comparing with any limit.

**Módulos limit conflict.** LIRPF DT 32ª and LIVA DT 13ª cover 2016 to 2024 only. RDL 16/2025 and RDL 2/2026 would have extended the higher limits, and Congress repealed both, so the consolidated statute reads 150,000, 75,000 and 150,000. The AEAT note of 1 April 2026 says the 2016 to 2024 limits stay for 2026 in IRPF and IVA, and that renuncias made under either decree stand. The AEAT's IRPF Manual for 2025 and IVA Manual for 2026 cite the repealed decrees for the same figures. So 250,000, 125,000 and 250,000 for 2026 is an administrative criterion with no consolidated text behind it. Show both and mark Needs Input. The limit for 2027 is unconfirmed, and the draft order for 2027 is silent on it.

**Reductions and caps on activity income**

| Item | Amount | Source |
| --- | --- | --- |
| Health insurance, each of the taxpayer, spouse and cohabiting children under 25 | 500 | LIRPF art. 30.2.5ª a: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Same, each person with a disability | 1,500 | same |
| Home supplies: share of cost × floor-area proportion | 30% | same, art. 30.2.5ª b |
| Own meals, Spain, no overnight stay, daily cap | 26.67 | RIRPF art. 9: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-6820/texto |
| Own meals, abroad, no overnight stay, daily cap | 48.08 | same |
| Own meals, Spain, overnight stay in another municipality, daily cap | 53.34 | same |
| Own meals, abroad, overnight stay, daily cap | 91.35 | same |
| Reduction on the art. 32.2.2º conditions, general | 2,000 | LIRPF art. 32.2.1º: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Further reduction, same conditions, net activity income up to 14,047.50, other income up to 6,500 | 6,498 | same; tapers by 1.14 times the excess to nil at 19,747.50 |
| Further reduction, same conditions, disability; 7,750 with a need for help, reduced mobility or 65% | 3,500 | same |
| Fallback if art. 32.2.2º conditions fail: non-exempt income including activity income below 12,000, subject to taper and combined cap below | 1,620 | same, art. 32.2.3º |
| New activity in estimación directa: positive net income after art. 32.1-2 reductions, first positive period and the next, annual eligible-income cap EUR 100,000; conditions below | 20% | same, art. 32.3 |

The art. 32.2.3º fallback is EUR 1,620 where non-exempt income is at most EUR 8,000; above that and below EUR 12,000 it is EUR 1,620 minus 0.405 times the excess over EUR 8,000. Together with the art. 20 reduction it cannot exceed EUR 3,700. No art. 32.2 reduction may make the resulting balance negative.

The art. 32.3 new-activity reduction requires no economic activity in the year before the start date, disregarding discontinued activities that never produced positive net income. Starting a later activity whilst continuing the first does not restart the first activity's first-positive-period-and-next-period window. The 20% applies to positive net income after art. 32.1-2 reductions, on at most EUR 100,000 annually. It is unavailable in a period when over 50% of income comes from a person or entity that paid the taxpayer employment income in the year before the activity began.

**Depreciation, EDS table, Orden of 27 March 1998**

| Group | Asset | Maximum linear rate | Maximum years | Source |
| --- | --- | --- | --- | --- |
| 1 | Buildings and other constructions | 3% | 68 | Orden of 27 March 1998, table: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1998-7200/texto |
| 2 | Installations, furniture, fittings, other tangible assets | 10% | 20 | same |
| 3 | Machinery | 12% | 18 | same |
| 4 | Transport elements | 16% | 14 | same |
| 5 | IT equipment, systems and software | 26% | 10 | same |
| 6 | Utensils and tools | 30% | 8 | same |
| 7 | Cattle, pigs, sheep and goats | 16% | 14 | same |
| 8 | Horses and non-citrus fruit trees | 8% | 25 | same |
| 9 | Citrus and vineyards | 4% | 50 | same |
| 10 | Olive groves | 2% | 100 | same |

**RETA 2026: 31.50% of the base (common 28.30, professional 1.30, MEI 0.90, cese 0.90, training 0.10)**

| Band | Monthly net income lower boundary | Upper boundary | Minimum base | Maximum base | Minimum monthly cuota | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Reduced 1 | No lower limit | 670 | 653.59 | 718.94 | 205.88 | Orden PJC/297/2026 art. 18: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2026-7296/texto |
| Reduced 2 | 670 | 900 | 718.95 | 900.00 | 226.47 | same |
| Reduced 3 | 900 | < 1,166.70 | 849.67 | 1,166.70 | 267.65 | same |
| General 1 | ≥ 1,166.70 | 1,300 | 950.98 | 1,300.00 | 299.56 | same |
| General 2 | 1,300 | 1,500 | 960.78 | 1,500.00 | 302.65 | same |
| General 3 | 1,500 | 1,700 | 960.78 | 1,700.00 | 302.65 | same |
| General 4 | 1,700 | 1,850 | 1,143.79 | 1,850.00 | 360.29 | same |
| General 5 | 1,850 | 2,030 | 1,209.15 | 2,030.00 | 380.88 | same |
| General 6 | 2,030 | 2,330 | 1,274.51 | 2,330.00 | 401.47 | same |
| General 7 | 2,330 | 2,760 | 1,356.21 | 2,760.00 | 427.21 | same |
| General 8 | 2,760 | 3,190 | 1,437.91 | 3,190.00 | 452.94 | same |
| General 9 | 3,190 | 3,620 | 1,519.61 | 3,620.00 | 478.68 | same |
| General 10 | 3,620 | 4,050 | 1,601.31 | 4,050.00 | 504.41 | same |
| General 11 | 4,050 | 6,000 | 1,732.03 | 5,101.20 | 545.59 | same |
| General 12 | 6,000 | and above | 1,928.10 | 5,101.20 | 607.35 | same |

Lower boundaries are exclusive and upper boundaries inclusive unless a different sign is shown. Reduced band 1 includes all income up to EUR 670. Exactly EUR 1,166.70 belongs to general band 1, with minimum base EUR 950.98 and minimum cuota EUR 299.56, not reduced band 3.

The bases and rates are in Orden PJC/297/2026 arts 18 and 37. The cuota column is the minimum base × 31.50%, computed here, not a published figure. The maximum base is EUR 5,101.20, a cuota of EUR 1,606.88.

**Reduced cuota (tarifa plana)**

The monthly reduced cuota for an alta in 2026 is held, not stated. LETA art. 38 ter.1 leaves the amount to the Budget Act (https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-13409/texto); RDL 13/2022 DT 5ª sets EUR 80 for 2023 to 2025 only (https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2022-12482/texto). It is listed under Not yet confirmed.

No amount for 2026 appears in RDL 3/2026 or Orden PJC/297/2026. EUR 80 is not stated here as the 2026 figure.

**Pension contributions, LIRPF arts 51 and 52**

| Item | Amount | Source |
| --- | --- | --- |
| Base limit, and never over 30% of net work and activity income, person by person | 1,500 | LIRPF art. 52.1: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Increase: employer contributions, or worker contributions on the art. 52 scale | up to 8,500 | same |
| Increase: self-employed limb (below) | up to 4,250 | same |
| Combined increase, the 2 limbs above | at most 8,500 | same |
| Employer contributions to a collective dependency insurance | up to 5,000 | same |
| Plan for a spouse whose net work and activity income is under EUR 8,000 | 1,000 | same, art. 51.7 |

The self-employed limb covers contributions to sector plans the autónomo adheres to, simplified employment plans for the self-employed, the entrepreneur's own contributions to an employment plan of which he is both promoter and participant, and mutualities, PPSE or dependency insurance on the same footing. EUR 5,750 is reached only where that limb applies and 30% of income allows it. Worker contributions on the art. 52 scale: up to EUR 500, up to 2.5 times the employer contribution; EUR 500.01 to 1,500, EUR 1,250 plus 0.25 times the excess; over EUR 1,500, 1 times it. The multiplier is 1 where work income from that firm exceeds EUR 60,000. TRLPFP art. 5.3 and art. 67 were additionally read for pension-plan contribution limits. Apply the separate contribution ceiling and qualifying-plan requirements before calculating the LIRPF reduction; the relief ceiling does not itself authorise a contribution.

**Deductions from cuota and other figures**

| Item | Amount | Source |
| --- | --- | --- |
| Investment in new companies: rate on a base of at most EUR 100,000 | 50% | LIRPF art. 68.1: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Qualifying donations: first EUR 250 | 80% | Ley 49/2002 art. 19: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2002-25039/texto |
| Qualifying donations: rest | 40% | same |
| Qualifying donations: rest, same entity 3 years running at no lower amount | 45% | same |
| Qualifying donations: base, at most 10% of base liquidable | 10% | LIRPF art. 69.1: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Joint return, marriage: reduction of the base | 3,400 | same, art. 84 |
| Joint return, art. 82.1.2ª parent-and-qualifying-children unit: reduction, unavailable when living with the other parent of any child in that unit | 2,150 | same |
| Withholding on professionals | 15% | LIRPF art. 101.5; RIRPF art. 95: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-6820/texto |
| Withholding on professionals, start year and next 2, no professional activity in the prior year | 7% | same |
| Withholding on dividends | 19% | LIRPF art. 101.4: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Modelo 130 instalment, EDS, cumulative net income | 20% | RIRPF art. 110: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-6820/texto |
| Art. 93 regime, work and activity income to EUR 600,000 | 24% | LIRPF art. 93.2.e: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto |
| Art. 93 regime, the excess | 47% | same |
| Criterio de caja, prior-year turnover annualised if activities began in that year, at most | 2,000,000 | LIVA art. 163 decies: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1992-28740/texto |
| Criterio de caja, cash receipts from one recipient at most | 100,000 | RIVA art. 61 nonies: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1992-28925/texto |
| Modelo 347, third-party operations over | 3,005.06 | RGAT art. 33: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-15984/texto |

Donation rows apply only when the recipient is eligible under Ley 49/2002 art. 16, the gift qualifies under art. 17 and its deductible base is valued under art. 18. A payment described as a donation is insufficient. Confirm the recipient's qualifying status, the gift and valuation evidence and the beneficiary certificate required by art. 24; unknown eligibility is Needs Input. Article 17 includes a bounded symbolic-return exception, so receipt of any benefit is not by itself a universal exclusion.

## The base

### Choosing the method

Estimación directa simplificada (EDS) applies where prior-year net turnover across all activities is at most EUR 600,000, unless renounced. If an activity started in that prior year, annualise turnover (RIRPF art. 28.2). Estimación directa normal (EDN) applies above that or on renuncia, which binds for 3 years (art. 30.1; RIRPF arts 28 and 29). The difference in records is by activity: a business keeps Código de Comercio accounts under EDN, and non-mercantile activities and EDS keep books only (RIRPF art. 68).

Módulos is not an option someone takes up: it applies, within its limits and to the activities listed in the annual order, unless renounced (art. 31.1.1ª). Limits aggregate activities of the spouse, descendants, ascendants and atribución entities where the activities are identical or similar and share a direction (art. 31.1.3ª). An activity done outside Spain, in whole or part, excludes it. The per-activity limits in the annual order were not read. Renuncia is made in December before the year, or by paying the first quarter's instalment in the direct method, and binds for at least 3 years (art. 31.1.5ª; RIRPF art. 33). So a move out of módulos starts with a calendar year and a 3-year commitment. For 2026, Orden HAC/1425/2025 keeps the modules. No text read supports saying they are being phased out.

Timing under módulos does not change the modules, but receipts and purchases count towards the limits. Annualise both prior-year income and prior-year purchases if an activity started during that year (LIRPF art. 31.1.3ª b and c); this does not resolve the 2026 limit conflict.

### Autónomo or SL

An autónomo pays IRPF on profit at the general scale. An SL pays IS on profit after pay, and its owner pays IRPF on pay and dividends. Retained profit bears no dividend tax until paid out, which defers the tax and does not remove it. Dividends carry 19% withholding (art. 101.4) and fall in the savings scale.

Conditions the comparison must carry:

- **Social contributions.** An administrator with effective control, or a controlling worker-socio, stays in RETA (LGSS art. 305.2 b and e). For art. 305.2 b, art. 308 counts all work income from, and the gross income from the equity of, an entity in which the person holds at least 33% at the IS accrual date, or at least 25% as an administrator. The deduction from income for the RETA bands is 3%, not the generic 7%, after 90 days in those cases, and the minimum base is that of group 7 of the Régimen General (art. 308.1.a 4ª).
- **Character of pay.** Pay for professional activities in Section 2 of the IAE from a company in which the socio is in RETA or a mutual is activity income, not work income (art. 27.1).
- **Market value.** Dealings between an SL and a socio holding at least 25% are related-party dealings at market value (LIS art. 18.2; LIRPF art. 41). The same shareholding threshold applies where linkage rests on that socio relationship, including its spouse and family limb. Administrators, whether formally appointed or acting in fact, and their spouse or relatives by blood or marriage to the third degree have a separate linkage rule; the administrator limb excepts pay for acting as such. LIS art. 18.6 lets a socio profesional treat the agreed pay as market value where all of these hold: over 75% of the entity's income is professional, with adequate staff and means; pay to all socios profesionales is at least 75% of the result before that pay; each socio's pay follows written criteria; and it is at least 1.5 times the average pay of employees doing similar work or, if none, 5 times the IPREM. Failing the last limb affects only that socio.
- **Substance.** Moving income into an SL with no activity of its own to match goes to LGT arts 15 and 16.
- **Costs.** Capital starts at EUR 1 (LSC art. 4), with reserve and liability rules below EUR 3,000. Formation and accounts belong to [spain-formation](spain-formation.md) and are outside the examples.

No income level decides this. See Example 1.

### Deductions most people miss

| Item | Rule and condition |
| --- | --- |
| RETA cuotas | Deductible activity cost (art. 28.1); LGSS art. 308 adds them back for the RETA test. See the RETA table for amounts. |
| Provisión | EDS only: 5% of net income before this item, at most EUR 2,000 (art. 30.2.4ª; RIRPF art. 30.2ª). It needs no receipts. It is not available with the art. 32.2.1º reduction (art. 32.2.2º a), or where the taxpayer opts for the reduction in RIRPF art. 26.1 (RIRPF art. 30.2ª). |
| Home supplies | Art. 30.2.5ª b: where the taxpayer's main home is partly used for the activity, water, gas, electricity, telephone and Internet: 30% × (area used ÷ total area) × cost, unless a higher or lower proportion is proved. |
| Own meals | Art. 30.2.5ª c: incurred in the activity, in restaurants or hotels, paid electronically, up to the RIRPF art. 9 caps. The caps limit real spending; they are not a daily allowance. |
| Health insurance | Art. 30.2.5ª a: a deductible expense in estimación directa, EUR 500 per person (EUR 1,500 with a disability), for the taxpayer, spouse and children under 25 living with him. |
| Family pay and assets | Art. 30.2.2ª and 3ª: stipulated pay to a cohabiting spouse or minor child is deductible where habitual and continuous work is evidenced by an employment contract and affiliation to the relevant Social Security regime, up to the market rate for their qualifications and work. For assets or rights they provide to the activity, deduct stipulated consideration up to market value, or market value where none is stipulated. This asset rule excludes property or rights common to both spouses. The recipient treats the respective amounts as employment or capital income. |
| Art. 32.2.1º reduction | All of: a) net income in estimación directa; b) all supplies to one unrelated person, or TRADE status with an economically dependent client that is also unrelated under LIS art. 18; c) deductible costs at most 30% of gross income; d) the formal duties set by regulation; e) no employment income, except unemployment or art. 17.2 a benefits totalling no more than EUR 4,000 annually; f) at least 70% of income under withholding; g) no activity through an atribución entity. |
| Vehicle, IRPF | An ordinary car must be proved exclusively used for the activity; RIRPF art. 22.3 bars partial allocation of an indivisible asset. Art. 22.4 normally allows accessory, clearly insignificant private use of business fixed assets outside working hours, but excludes ordinary cars from that concession. Its exceptions are mixed goods vehicles, paid passenger transport, paid driver or pilot training, commercial representatives or agents and habitual paid hire. A listed exception concerns minor private use; it is not a prerequisite for proving genuinely exclusive business use. |
| Training, professional fees, repairs, insurance | Deductible on the general rule of art. 28.1 where linked to the activity, supported and recorded. No item-specific text was read. |

### IVA on vehicles

LIVA art. 95.Tres.2ª presumes 50% business use for cars, their trailers, mopeds and motorcycles. It presumes 100% for mixed goods vehicles, vehicles for paid passenger transport, driving schools, makers' testing, commercial agents' travel and surveillance. Art. 95.Tres.3ª adjusts the deduction to the proved actual use, which can be above or below 50%, so exclusive use is not needed. Art. 95.Tres.4ª allows any proof at law: the return and the books alone are not enough.

### Depreciation

The EDS table gives a maximum linear rate (RIRPF art. 30.1ª). Tools are group 6 at 30%, not machinery.

New tangible assets costing no more than EUR 300 each can be depreciated freely, subject to EUR 25,000 per tax period, prorated when the period is shorter than a year (LIS art. 12.3 e). The AEAT Manual applies this in IRPF estimación directa.

Under LIS art. 102, qualifying new tangible fixed assets and investment property used in economic activities and made available in an art. 101 period can receive free depreciation from entry into use. The eligible investment is EUR 120,000 times the average staff increase, calculated to 2 decimals using contracted hours relative to full-time hours. Compare the 24 months beginning at the start of the entry-into-use tax period with the preceding 12 months, then maintain the increase for another 24 months. Failure to increase or maintain staffing requires repayment of excess relief plus late interest with the return for the breach period. Art. 102 also covers qualifying construction contracts signed in that period with delivery within 12 months of completion, self-construction and new assets under finance leases where the purchase option is exercised.

LIS art. 103.1 separately permits twice the maximum official linear coefficient for qualifying new tangible fixed assets, investment property and intangibles used in economic activities and made available in an art. 101 period. Its construction-contract extension requires a contract signed in that period and delivery within 12 months of completion; it also extends to qualifying self-construction or self-production. The separate art. 103.5 intangible deduction is not modelled here and needs its referenced provision checked before use. The 2026 vehicle and renewable rules in LIS DA 17ª and 18ª were not read.

The rule on a part-year charge was not read, so a January purchase is not said to give a full 26%.

### Losses

| Item | Rule |
| --- | --- |
| Activity loss | Offsets other income in the general base without limit in the same year (art. 48 a). |
| General base still negative | Carries forward 4 years against positive general bases liquidables, of any category (art. 50.3). |
| Non-transmission gains and losses | Offset each other. A remaining loss offsets positive income in the general base up to 25%, and the rest carries 4 years (art. 48 b). |
| Savings base | Capital income and transmission gains each offset within their own group, then across groups up to 25% of the other's positive balance, each way, with a 4-year carry (art. 49). A capital loss does not reach the general base. |
| Securities repurchase | Art. 33.5 f: a loss on listed securities is not computed where homogeneous securities are bought within 2 months before or after the sale; 1 year for unlisted (g). The loss enters as those securities are sold. |
| Carry-back | The texts read provide only the forward carry. |

Only real costs make a loss. Spending to create one is still spending.

### Timing

- Income and cost follow accrual (art. 14.1 b; RIRPF art. 7.1). Prepaying insurance or subscriptions before 31 December brings forward the cash and not the deduction.
- The exception is the cash-basis option for those keeping books under RIRPF art. 68.3 to 6, stated in the return, for at least 3 years, and not available to anyone who keeps Código de Comercio accounts (RIRPF art. 7.2). Nothing can go uncounted or count twice (art. 7.4).
- Deferring an invoice does not move accrual. It also meets RD 1619/2012 art. 11: invoice at the time of the supply, or for a business client before the 16th of the next month.
- Pension contributions count in the year paid and are limited as above. The reduction comes off the general base and cannot make it negative (arts 50 and 51).
- Gains: realising a loss or spreading a gain across years changes the savings bands. See the repurchase rule first.
- Withholding is the payer's act, not the autónomo's. A new professional must tell the payer to get 7%, and the payer keeps the signed notice (RIRPF art. 95). RIRPF art. 95 lists other 7% cases, not covered here.
- Modelo 130 is arithmetic, at 20% of cumulative net income (4%, 3% or 2% in módulos on the art. 110 measures), so there is no election to cut it, and it falls by itself when cumulative income falls (RIRPF art. 110). A professional with at least 70% of prior-year income subject to withholding is exempt (RIRPF art. 109.2).
- Joint or individual: art. 84 gives a EUR 3,400 reduction for the spouses' unit or EUR 2,150 for the art. 82.1.2ª parent-and-qualifying-children unit. Apply it first to the general base, then any remainder to the savings base, making neither negative, before arts 51, 53 and 54 and DA 11ª. It is not a mínimo. The unit gets one basic personal minimum; relevant age and disability increments account for each spouse's circumstances, with separate descendant/disability rules for children. Under art. 83, the election covers every member and requires all to be IRPF taxpayers; one individual return requires the others to file individually. It does not bind later years. An exercised election cannot be changed for that year after the regulatory return deadline. If no return is filed, individual taxation applies unless a joint election is expressly made within 10 days of the administration's request. Membership is assessed at 31 December and no one can belong to 2 units (art. 82). An unmarried couple cannot form the spouses' unit, but a legally separated or unmarried parent may form the art. 82.1.2ª unit with all cohabiting children who meet art. 82.1's conditions. The EUR 2,150 reduction is unavailable if that taxpayer lives with the other parent of any child in the unit. Compute the permitted alternatives.

### IVA

- **Simplificado:** for the activities in the annual order, within the LIVA art. 122 limits (see the conflict note). [spain-vat-return](spain-vat-return.md) covers the general regime and explicitly refuses module-based returns. No verified companion computation is available here; obtain specialist input before applying simplificado.
- **Recargo de equivalencia:** applies by law to retailers who are individuals or atribución entities, under arts 148 and 149, and is not a choice. There is no return on those operations and no deduction of input IVA (art. 154), except on intra-EU acquisitions and art. 84.Uno.2º operations.
- **Criterio de caja:** the prior-year turnover ceiling is EUR 2,000,000, annualised if business or professional activities began in that year (LIVA art. 163 decies). For exclusion after an election, annualise current-year turnover if activities began during that year (RIVA art. 61 nonies); the separate EUR 100,000 cash-receipts test for one recipient also applies. Opt at alta or in December, for all operations outside the art. 163 duodecies.Dos list. The option rolls on until renuncia or exclusion, and a renuncia binds for at least 3 years. Output IVA falls due on collection or on 31 December of the next year, and input IVA is deductible on payment or on that same date (arts 163 decies to terdecies; RIVA arts 61 septies and 61 nonies). Excluded operations: the simplified, agricultural, recargo, gold, electronic services and group regimes; exempt exports and arts 21 to 25 supplies; intra-EU acquisitions; art. 84.Uno 2º to 4º reverse charges; imports; and arts 9.1º and 12 self-supplies.
- **Pro rata:** the general rule is the default. Special pro rata is by option in the last return of the year, binds for 3 years, and is compulsory where the general rule gives at least 10% more (LIVA art. 103; RIVA art. 28).

### Social contributions

RETA runs on real net income (LGSS art. 308) under RDL 13/2022. The transition did not end in 2025: DT 1ª.3 calls for a calendar over a further period of at most 6 years, and DA 1ª sets bases by annual net income from 1 January 2032, subject to DT 1ª.4 (not read). For 2026 the 2025 table continues under RDL 3/2026 art. 3.4 and Orden PJC/297/2026.

- **Choosing a band.** The autónomo chooses a provisional base by forecast, and can change it up to 6 times a year (RD 2064/1995 art. 45). A request in January or February takes effect on 1 March, March or April on 1 May, May or June on 1 July, July or August on 1 September, September or October on 1 November, and November or December on 1 January.
- **Regularisation.** After the AEAT passes income to the TGSS, the year is reset: see Example 2. A shortfall against the band's minimum base is due by the last day of the month after notice, with no interest or surcharge if paid within that period. An excess over the band's maximum base is refunded by the TGSS, with no interest, before 30 April of the year after the tax authority communicated computable income to the TGSS. That communication year need not be the contribution year. A provisional cuota between the 2 stays as paid. With no declaration, the group 7 base applies.
- **Lower income means a lower cuota and lower benefits.** Pension and other benefits follow the bases.
- **Reduced cuota.** For an alta after at least 2 years out of RETA, or 3 if the person had the reduction before, or an initial alta. It runs 12 full months and, if net income stays below the applicable annual minimum wage on a declaration, 12 more. If that second period spans 2 calendar years, the income test must be met separately in each year (LETA art. 38 ter.2). It is requested at alta and before the second period, and it ends on baja. Socios of capital companies and socios trabajadores of cooperatives are included (LETA art. 38 ter.9), and relatives to the second degree are excluded (38 ter.11). No cese or training contributions run during it. Benefits use the minimum base of the lowest general-table band (38 ter.5), EUR 950.98 for 2026, rather than the reduced table's EUR 653.59. With a disability of 33% or more, or for victims of gender violence or terrorism, the periods are 24 and 36 months. The actual reduced-cuota amount for 2026 remains held.
- **Cese de actividad.** Needs contributions in the prior 48 months, 12 of them in the last 24 (LGSS art. 338). Months contributed against months of benefit: 12 to 17, 4; 18 to 23, 6; 24 to 29, 8; 30 to 35, 10; 36 to 42, 12; 43 to 47, 16; 48 and over, 24.
- **Pluriactividad.** Orden PJC/297/2026 art. 18.8: refund of 50% of the excess of common-contingency contributions over EUR 17,323.68. Count RETA common-contingency contributions plus both employer and worker common-contingency contributions for simultaneous employment. The refund is capped at 50% of the RETA common-contingency cuotas paid, not all RETA contributions. The TGSS pays within 4 months of regularisation, except where contribution peculiarities prevent payment within that period or the person must provide additional data; payment then follows later (LGSS art. 313). No Modelo 190 is involved.

### Pensions

Benefits are work income in the year received (art. 17.2 a). DT 12ª preserves a transitional regime for qualifying contributions up to 31 December 2006, referring to the IRPF text in force on that date. The historical art. 17 was not retained or read: the claimed 40% reduction and capital-payment condition are held pending that source, rather than established by DT 12ª alone. The supported ordinary window is the contingency year or the next 2 years, with separate windows for earlier contingencies (DT 12ª.4). Article 52.2 allows eligible contributions unused because the taxable base was insufficient or its percentage limit applied to be reduced in the next 5 years, including attributed employer contributions. It excludes contributions exceeding the art. 51.6 maximum contribution limits; an over-limit contribution does not gain that carry-forward. Withdrawal outside the permitted cases means repaying the tax with interest (art. 51.8).

### New companies, donations and the savings base

The LIRPF art. 68.1 deduction needs all of these:

- The company is an SA, SL, SAL or SLL, unlisted on any organised market, including regulated markets and multilateral trading facilities, throughout all years of holding.
- It carries on a real economic activity with the required staff and material resources. It must not manage movable or immovable assets in any of its tax periods ending before the shares are transferred.
- Own funds at the start of the company's tax period of subscription are at most EUR 400,000. For an art. 42 group, aggregate all group entities regardless of residence or any duty to prepare consolidated accounts.
- Shares are subscribed at formation or in a capital increase within 5 years of formation, or 7 for qualifying empresas emergentes, and held for over 3 and under 12 years.
- On every day of each calendar year of holding, the investor's direct or indirect interest, together with the spouse and blood or marriage relatives to the second degree, must not exceed 40% of either capital or voting rights. That limit does not apply to founders of qualifying empresas emergentes named in the public incorporation deed.
- The entity must not carry on the same activity previously carried on under another ownership. Obtain its certificate that the art. 68.1.2º company conditions were met in the acquisition period.

Both the seven-year subscription window and founder holding-limit exception require qualifying empresa emergente status, not merely a newly formed company. Verify Ley 28/2022 art. 3's age, origin, distributions/listing, Spanish presence, workforce, innovation/scalability, group and disqualification conditions. Obtain the relevant ENISA certification and registered-status evidence under arts 4 and 5 and check art. 6's cessation/exclusion conditions. Do not self-certify that status from a business plan. If qualification is unconfirmed, both extensions are Needs Input and must not be applied. The detailed certification application procedure is outside this guide.

An autonomous deduction on the same subscription amounts excludes the state one. If an earlier disposal uses the art. 38.2 reinvestment exemption, only new subscription spending above the total sale proceeds enters this deduction's base; none does until the investment exceeds those proceeds (art. 68.1.4º). The result comes off the cuota íntegra estatal (art. 67.1 a), which cannot go negative (art. 67.2).

Savings: gains in separate years use the lower bands each year, where selling in that way has a reason of its own.

A new Cuenta de Ahorro e Inversión Financia Europa sits in LIRPF art. 95 ter (RDL 29/2026, BOE-A-2026-20823). It is not used in this guide: the validation of that decree was not read.

### Art. 93 regime (Ley Beckham)

Art. 93.1 needs all 3: no Spanish residence in the 5 prior periods; a move to Spain in the first year of the regime or the year before, caused by one of 4 events; and no income through a permanent establishment in Spain, except under events 3 and 4.

| Event | Rule |
| --- | --- |
| 1. Employment | A qualifying employment contract, excluding the special professional-athlete relationship. The statutory alternatives include starting an ordinary, qualifying special or statutory relationship with an employer in Spain; an employer-ordered move supported by a transfer letter; or employee remote work from Spain exclusively through computer, telematic and telecommunications means, without an employer-ordered move. The Spanish-employer test belongs to the first alternative. |
| 2. Administrator | Of an entity. If the entity is patrimonial, the administrator's holding cannot make it related under LIS art. 18. |
| 3. Entrepreneur | An activity qualified as entrepreneurial under Ley 14/2013 art. 70. |
| 4. Highly qualified professional or qualifying training/R+D/innovation | Meet RIRPF art. 113.2's applicable qualification or activity test. Remuneration for the qualifying startup services or training/R+D/innovation activities must together exceed 40% of all business, professional and employment income. Startup status is that defined by Ley 28/2022 art. 3. |

For event 3, RIRPF art. 113.2 and Ley 14/2013 arts 69 and 70 require an innovative activity and/or one of special economic interest for Spain, with a favourable ENISA report. The required business-residence authorisation must precede the move; EU/free-movement beneficiaries instead need the prescribed favourable report before moving. An existing regime user starting a different entrepreneurial activity also needs the specified report. Under art. 119.2(e), provide the report unless the supplied residence authorisation is the art. 69 entrepreneur authorisation.

For event 4, apply the qualification criteria cross-referenced to Ley 14/2013 art. 71, or the training/research categories in art. 72.1(a) to (d), as appropriate. Art. 119.2(f) requires qualification evidence, proof of the startup's registration and evidence of services: the stated residence-authorisation and online-register-check exceptions must be respected. Art. 119.2(g) requires evidence of qualifying training/R+D/innovation unless the supplied authorisation is the corresponding art. 72 authorisation. Confirm the applicable route, dates, qualifications, registered startup status and income denominator; missing evidence is Needs Input, with no election or eligibility conclusion. RIRPF art. 113.2 also restricts economic activities throughout the regime periods to the specified entrepreneurial activity, startup services and qualifying training/R+D/innovation activities. Screen every additional business activity against those permitted categories; unknown classification is Needs Input and no eligibility conclusion may be given for an activity outside them. This guide does not prepare an immigration or certification application.

So autónomos are not barred: events 3 and 4 reach them. The regime lasts for the year of the change and the next 5. It taxes work income, and activity income under event 3, at 24% to EUR 600,000 and 47% above, and all that income counts as Spanish wherever earned (art. 93.2 b). Savings income uses the 19% to 30% scale. Nothing offsets anything else (93.2 c). Family joining under art. 93.3 includes the spouse, children under 25 or of any age with a disability and, where there is no marriage, the children's other parent. LIRPF art. 93.3(a)'s statutory wording requires moving with the principal taxpayer or later, before the end of the first period in which the principal uses the regime. They must become Spanish tax residents and meet the prior-residence and permanent-establishment tests. Their combined bases liquidables must be below the principal's in each relevant period, and the regime continues only whilst the principal remains within it.

RIRPF art. 113.3 separately provides for family members arriving before the principal, provided they do not acquire Spanish tax residence before the principal's first regime period; it also permits later arrival before that period ends. Present both that regulation and LIRPF art. 93.3(a)'s statutory wording for an earlier-arrival case. Their application and eligibility remain Needs Input for a qualified Spanish adviser; this guide does not silently approve or exclude that case.

RIRPF art. 116 requires a separate election for each taxpayer. The principal's maximum 6-month period runs from the activity start recorded in Spanish Social Security registration, documentation maintaining origin-country Social Security or, if registration is not compulsory, the supporting start-date document. Joining family have 6 months from entry to Spain or the principal's longer deadline. Relationship, age and disability are assessed when each family member elects. The prescribed communication model applies; someone who used the art. 89.B special withholding procedure cannot elect. Patrimonio applies on real obligation.

## Deadlines and filing

Filed online: AEAT Sede electrónica (https://sede.agenciatributaria.gob.es) for Modelos 100, 130, 303, 347 and 390, and the Import@ss portal of the TGSS (https://portal.seg-social.gob.es/wps/portal/importass/importass/) for RETA bases, alta and baja.

The calendar year is the tax year. Dates below are for 2026 as read. Filing dates for 2027, and the Renta campaign for income of 2026, were not published or not read when this file was written.

| Month | Action |
| --- | --- |
| January | By 30 January: Modelo 303 and 130 for the fourth quarter and Modelo 390 for the year. |
| February to 2 March | 1 February to 2 March: Modelo 347 for the prior year. Gather invoices and cuota records. |
| April | 8 April: Renta 2025 opens. By 20 April: Modelo 303 and 130 for the first quarter. Compare joint and individual. |
| May | Check the borrador for activity income, pension contributions and autonomous deductions. |
| June | Direct debit to 25 June, except that domiciling only the second IRPF instalment is allowed to 30 June (Orden HAC/277/2026 art. 12.3). 30 June: Renta 2025 closes. Modelo 390 is not due in June or December. |
| July | By 20 July: Modelo 303 and 130 for the second quarter. Review the RETA forecast. |
| August to September | Review purchases, input IVA and any pro rata. |
| October | By 20 October: Modelo 303 and 130 for the third quarter. Estimate the year's income and review the RETA band. |
| November | Review pension room against the art. 52 limit. Review gains and losses against the repurchase rule. |
| December | Renuncias and options for next year (módulos, EDS, criterio de caja). Pay pension contributions and donations. Buying an asset affects the charge only from entry into use. Invoicing stays on the art. 11 timing. |

## Penalties and interest

| Item | Rule | Source |
| --- | --- | --- |
| Conflicto, LGT art. 15 | Needs the Comisión consultiva's prior favourable report (art. 159). Tax on the usual act, or the advantage removed, with interest. | LGT art. 15 |
| Penalty in conflicto, art. 206 bis | Only with substantial equality to a published administrative criterion, public before the filing period. Serious. 50% of tax unpaid or of a refund wrongly obtained; 15% of a refund or benefit wrongly claimed; 15% of items set to offset in the base; 50% of items set against the cuota or apparent credits. It excludes penalties under arts 191, 193, 194 and 195. | LGT art. 206 bis |
| Simulación, LGT art. 16 | Tax on the act really done, interest and 'where applicable' the penalty. Under art. 191: minor 50%, serious 50% to 100%, very serious 100% to 150%. | LGT arts 16 and 191 |
| False invoices | Issuing them is very serious: 75% of the operations involved. | LGT art. 201.3 |
| Tax crime | Cuota defrauded, not income hidden, over EUR 120,000 in a period: prison of 1 to 5 years, a fine of 1 to 6 times and 3 to 6 years without public aid and tax benefits. Over EUR 600,000 and other aggravations: 2 to 6 years (art. 305 bis). Full regularisation under art. 305.4 removes criminal exposure on its conditions. | CP arts 305 and 305 bis |
| Books | CP art. 310: prison of 5 to 7 months for: a) no books at all under direct assessment; b) different accounts; c) unrecorded or misstated operations; d) fictitious entries. Limbs c and d need omitted or false returns and over EUR 240,000 a year. | CP art. 310 |
| Late without notice | Art. 27: 1%, plus 1% each full month; 15% after 12 months, with interest from then. | LGT art. 27 |
| Prescription | 4 years (art. 66). | LGT art. 66 |
| Certainty | Written binding consultation (arts 88 and 89). | LGT arts 88 and 89 |
| Reduced cuota | Not re-claimed within the 2 or 3-year gap. That is an entitlement test at the TGSS. | LETA art. 38 ter |

Late-payment interest follows LGT art. 26.6: the legal rate plus 25%, unless the Budget Act says otherwise. The rate for 2026 was not read.

## Cross-border points

- **Residence.** Art. 9.1: over 183 days in Spain in the year, counting sporadic absences unless residence elsewhere is proved, or the main core or base of the client's activities or economic interests in Spain. It is presumed, unless disproved, where the client's spouse and dependent minor children live in Spain on those tests. A refusal applies where this is unknown.
- **Community.** Residence in a community is most days there in the period (art. 72.1). A change whose main aim is lower tax has no effect (art. 72.3), and autonomous deductions need real residence.
- **Art. 93.** A choice to be taxed on the non-resident rules whilst remaining an IRPF taxpayer. See 'Art. 93 regime'.
- **Canarias, Ceuta, Melilla.** Outside the IVA territory (LIVA art. 3), with their own indirect taxes. LIRPF art. 68.4 contains the Ceuta and Melilla income deduction. Territorial eligibility and calculations remain outside this guide's verified scope. LIRPF DA 64ª has a 2026 activity measure for Ceuta, not used here.
- **Treaties.** No treaty or EU text was read. A client with foreign income or a move out of Spain is outside this file.
- **EU revenue.** CP art. 305.3 applies the art. 305 penalties to EU revenue at EUR 100,000.

## Two worked examples that recompute

The Madrid figures are the 2025 scale, a labelled stand-in. Examples 3 to 7 use a marginal rate of 35.9%: state 18.5% plus Madrid 17.4%, valid for a Madrid resident whose base stays between EUR 35,425.68 and EUR 57,320.40 on both sides of the change. Examples 5 to 7 assume a base of EUR 40,000 before the item. A taxpayer elsewhere has a different rate.

### Example 1: Which should I choose, autónomo or SL? Profit EUR 80,000, then EUR 45,000

Single, Madrid, under 65, no other income. Option A: an autónomo with the profit after every deductible cost. Option B: an existing SL (not new, not patrimonial, passing the aggregated and annualised INCN-under-EUR-1m test, full-year period starting in 2026), wholly owned and run by the client, paying a EUR 30,000 salary that stays work income (no Section 2 professional activity), and the rest of the profit after IS as a dividend. Corporate limits on distribution and SL costs are left out.

**Social contributions are left out of both sides: this is an income tax comparison only.** Under B, RETA still applies, and art. 308 counts the salary and dividends with a 3% deduction rather than 7%, so the RETA band need not fall.

A's tax is the 2 scales on the profit, each less the scale on the minimum (`5,550 × 9.5%` and `5,956.65 × 8.5%`). B's work income is `salary − 2,000` (art. 19.2 f, with own social contributions left out); it is over the art. 20 limit of EUR 19,747.50, so art. 20 gives nothing. IS is `min(profit − salary, 50,000) × 19% + max(profit − salary − 50,000, 0) × 21%`. The dividend is `profit − salary − IS`, taxed on the savings scale.

```oa-check
name: es-opt-sl-80000
inputs:
  profit: 80000
  salary: 30000
  min_state: 527.25
  min_madrid: 506.31525
steps:
  - a_state: 8950.75 + (profit - 60000) * 0.225 - min_state
  - a_madrid: 7651.10 + (profit - 57320.40) * 0.205 - min_madrid
  - a_total: a_state + a_madrid
  - work: salary - 2000
  - b_state: 2112.75 + (work - 20200) * 0.15 - min_state
  - b_madrid: 1739.53 + (work - 19004.63) * 0.128 - min_madrid
  - co_profit: profit - salary
  - is_tax: min(co_profit, 50000) * 0.19 + max(co_profit - 50000, 0) * 0.21
  - dividend: co_profit - is_tax
  - div_tax: 1140 + (dividend - 6000) * 0.21
  - b_retained: b_state + b_madrid + is_tax
  - b_paid_out: b_retained + div_tax
  - gap_paid_out: a_total - b_paid_out
expected:
  a_total: 24717.60
  b_state: 2755.50
  b_madrid: 2384.62
  is_tax: 9500.00
  dividend: 40500.00
  div_tax: 8385.00
  b_retained: 14640.12
  b_paid_out: 23025.12
  gap_paid_out: 1692.48
```

```oa-check
name: es-opt-sl-45000
inputs:
  profit: 45000
  salary: 30000
  min_state: 527.25
  min_madrid: 506.31525
steps:
  - a_state: 4362.75 + (profit - 35200) * 0.185 - min_state
  - a_madrid: 3841.42 + (profit - 35425.68) * 0.174 - min_madrid
  - a_total: a_state + a_madrid
  - work: salary - 2000
  - b_state: 2112.75 + (work - 20200) * 0.15 - min_state
  - b_madrid: 1739.53 + (work - 19004.63) * 0.128 - min_madrid
  - co_profit: profit - salary
  - is_tax: min(co_profit, 50000) * 0.19
  - dividend: co_profit - is_tax
  - div_tax: 1140 + (dividend - 6000) * 0.21
  - b_paid_out: b_state + b_madrid + is_tax + div_tax
  - gap_paid_out: a_total - b_paid_out
expected:
  a_total: 10649.54
  is_tax: 2850.00
  dividend: 12150.00
  div_tax: 2431.50
  b_paid_out: 10421.62
  gap_paid_out: 227.91
```

On these inputs, income tax on full payout under B is EUR 1,692.48 lower at EUR 80,000 and EUR 227.91 lower at EUR 45,000. If the EUR 80,000 company keeps the EUR 40,500 instead, B's tax so far is EUR 14,640.12, and the EUR 10,077.48 gap is deferred, not saved. These gaps exclude social contributions and every SL cost, and they move with the salary chosen, so they do not show that either option is cheaper overall. Which to choose is for the client and a Spanish adviser, on the art. 308, art. 27.1 and art. 18 conditions above.

### Example 2: RETA regularisation, computable income EUR 36,000

Income for the RETA test, after adding back cuotas, is EUR 36,000. The generic 7% applies. The provisional base was the minimum of general band 5, EUR 1,209.15. The whole of 2026 was at the 31.50% rate, and no reduced cuota applied.

`36,000 × 93% ÷ 12 = 2,790`, which is in general band 8, with a minimum base of EUR 1,437.91. The provisional base is below that, so `(1,437.91 − 1,209.15) × 31.50% × 12` is due. Had the provisional base been between EUR 1,437.91 and EUR 3,190, nothing would be due or refunded.

```oa-check
name: es-opt-reta-regularisation
inputs:
  income: 36000
  rate: 0.315
  base_provisional: 1209.15
  base_tramo_min: 1437.91
steps:
  - monthly: income * 0.93 / 12
  - shortfall: (base_tramo_min - base_provisional) * rate * 12
expected:
  monthly: 2790.00
  shortfall: 864.71
```

### Example 3: Pension contribution, autónomo, net income EUR 45,000

Assume EUR 1,500 of general contributions and EUR 4,250 to a qualifying simplified employment pension plan for autónomos under TRLPFP arts 5.3(a)(2) and 67.1(c), with no other annual contributions. The art. 52 relief ceiling on these assumptions is `min(30% × 45,000, 1,500 + 4,250)`, or EUR 5,750. Confirm the actual plan's eligibility and the separate aggregate contribution cap before using this result; this is a conditional illustration. The saving uses the stipulated 35.9% marginal rate above.

```oa-check
name: es-opt-pension
inputs:
  income: 45000
  contribution: 5750
  marginal: 0.359
steps:
  - limit: min(0.30 * income, 1500 + 4250)
  - allowed: min(contribution, limit)
  - saving: allowed * marginal
expected:
  limit: 5750.00
  saving: 2064.25
```

It defers rather than removes tax: benefits are work income later.

### Example 4: Provisión, EDS, net income EUR 40,000

`min(5% × 40,000, 2,000)`.

```oa-check
name: es-opt-provision
inputs:
  net: 40000
  marginal: 0.359
steps:
  - provision: min(0.05 * net, 2000)
  - saving: provision * marginal
expected:
  provision: 2000.00
  saving: 718.00
```

### Example 5: Home supplies, 15 m² in a 90 m² main home, EUR 3,600

`3,600 × (15 ÷ 90) × 30%`, on no other proportion proved.

```oa-check
name: es-opt-supplies
inputs:
  cost: 3600
  used: 15
  total: 90
  marginal: 0.359
steps:
  - deductible: cost * used / total * 0.30
  - saving: deductible * marginal
expected:
  deductible: 180.00
  saving: 64.62
```

### Example 6: Own meals, 100 travel days in Spain, no overnight stay

The cap is `100 × 26.67`. That needs at least that much real spending, on the conditions above.

```oa-check
name: es-opt-meals
inputs:
  days: 100
  cap: 26.67
  marginal: 0.359
steps:
  - maximum: days * cap
  - saving: maximum * marginal
expected:
  maximum: 2667.00
  saving: 957.45
```

### Example 7: Health insurance, family of 4, EDS or EDN

Assume the taxpayer pays EUR 500 each for their own cover, their spouse and 2 cohabiting children under 25, all eligible under LIRPF art. 30.2.5ª(a). All 4 premiums and the stipulated marginal rate are hypothetical inputs, not verified client entitlements.

```oa-check
name: es-opt-health
inputs:
  persons: 4
  premium_each: 500
  marginal: 0.359
steps:
  - deductible: persons * premium_each
  - saving: deductible * marginal
expected:
  deductible: 2000.00
  saving: 718.00
```

### Example 8: Reduced cuota, income about EUR 1,300 a month

**Conditional example. EUR 80 is the 2023 to 2025 amount and is an assumed input here, held for 2026.** Compared with the minimum of general band 1: `(950.98 × 31.50% − 80) × 12`.

```oa-check
name: es-opt-reduced-cuota
inputs:
  assumed_reduced: 80
  base_tramo_min: 950.98
  rate: 0.315
steps:
  - standard: base_tramo_min * rate
  - saving: (standard - assumed_reduced) * 12
expected:
  standard: 299.56
  saving: 2634.70
```

### Example 9: New company investment, EUR 20,000, conditions met

Assume every art. 68.1 eligibility condition above is met for its required period, including group own funds, qualifying activity and the daily capital/voting-rights test. No autonomous deduction uses these amounts and no earlier art. 38.2 reinvestment exemption restricts the new deduction base.

`min(50% × min(20,000, 100,000), cuota íntegra estatal)`. Base liquidable general EUR 70,000 gives a state cuota of `8,950.75 + 10,000 × 22.5% − 527.25`. Base EUR 40,000 gives `4,362.75 + 4,800 × 18.5% − 527.25`. The result cannot go negative, so the lower base uses only part of the deduction. No carry-forward rule was found for the rest.

```oa-check
name: es-opt-new-company
inputs:
  investment: 20000
steps:
  - deduction: 0.50 * min(investment, 100000)
  - state_high: 8950.75 + (70000 - 60000) * 0.225 - 527.25
  - state_low: 4362.75 + (40000 - 35200) * 0.185 - 527.25
  - used_high: min(deduction, state_high)
  - used_low: min(deduction, state_low)
expected:
  deduction: 10000.00
  state_high: 10673.50
  state_low: 4723.50
  used_high: 10000.00
  used_low: 4723.50
```

## Ask the client first

1. Residence: where the client lives, the community, days in Spain, any move between communities or into Spain in the last 6 years, and whether art. 93 applies.
2. Activity: what it is and its IAE section, start date, prior-year turnover, EDS, EDN or módulos, any renuncia in force, and the share of income under withholding.
3. RETA: alta date, chosen base, forecast net income, any earlier reduced cuota, any other employment, and relatives who are also autónomos.
4. Company: any SL held, share held, administrator status, INCN, pay, dividends planned, and related persons who deal with it.
5. Household: marital status, spouse's income, children and ages, disability, and joint or individual filing.
6. Investments: pension contributions so far and which plan type, contributions before 2007, recent sales and repurchases of securities, new company investments, and donations.

## Sources

Each row says what was read. BOE rows state the update date of the consolidated text. Autonomous pages are from the Manual for 2025.

| Source | URL | Read on |
| --- | --- | --- |
| LIRPF, BOE-A-2006-20764: additional complete article versions read, arts 56 to 61 and 82 to 84 and 93; retained consolidated text updated 2026-10-07 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto | 2026-11-07 |
| RIRPF, BOE-A-2007-6820: additional complete article versions read, arts 113 and 119; retained consolidated text updated 2026-11-05 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-6820/texto | 2026-11-07 |
| Ley 49/2002, BOE-A-2002-25039: additional complete article versions read, arts 16 to 19 and 24; retained consolidated text updated 2026-10-19 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2002-25039/texto | 2026-11-07 |
| Ley 28/2022, BOE-A-2022-21739, consolidated text updated 2026-07-16: complete article versions read, arts 3 to 6; other units and detailed implementing procedures not read | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2022-21739/texto | 2026-11-07 |
| Ley 14/2013, BOE-A-2013-10074, consolidated text updated 2026-01-30: complete article versions read, arts 69 to 72; no immigration application or actual qualification assessed | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2013-10074/texto | 2026-11-07 |
| TRLPFP, RDL 1/2002, BOE-A-2002-24252, consolidated text updated 2026-09-18: complete article versions read, arts 5 and 67; hypothetical qualifying-plan facts only | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2002-24252/texto | 2026-11-07 |
| LIRPF, Ley 35/2006, BOE-A-2006-20764, consolidated text updated 2026-10-07: read in part, arts 4, 9, 14, 17, 19, 20, 27 to 33, 41, 48 to 52, 57, 63, 65, 66 to 69, 72, 74, 76, 82, 84, 93, 95 ter and 101, DA 64ª, DT 12ª and DT 32ª, in the parts cited | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2006-20764/texto | 2026-11-06 |
| RIRPF, Real Decreto 439/2007, BOE-A-2007-6820, consolidated text updated 2026-11-05: read in part, arts 7, 9, 22, 28 to 30, 33, 68, 95, 109 to 111, 116 and 119, in the parts cited | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-6820/texto | 2026-11-06 |
| LIS, Ley 27/2014, BOE-A-2014-12328, consolidated text updated 2026-09-03: read in part, arts 12.3 e, 18, 29, 101 to 103 and DT 44ª, in the parts cited; DA 17ª and 18ª not read | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2014-12328/texto | 2026-11-06 |
| LIVA, Ley 37/1992, BOE-A-1992-28740, consolidated text updated 2026-10-07: read in part, arts 3, 95, 103, 122, 148, 149, 154, 163 decies to terdecies and DT 13ª, in the parts cited | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1992-28740/texto | 2026-11-06 |
| RIVA, Real Decreto 1624/1992, BOE-A-1992-28925, consolidated text updated 2026-11-05: read in part, arts 28.1.1º, 61 septies, 61 nonies and 71.4 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1992-28925/texto | 2026-11-06 |
| LGT, Ley 58/2003, BOE-A-2003-23186, consolidated text updated 2026-10-09: read in part, arts 15, 16, 26.6, 27, 66, 88, 89, 159, 179.2 d, 191, 201 and 206 bis, in the parts cited | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2003-23186/texto | 2026-11-06 |
| LGSS, Real Decreto Legislativo 8/2015, BOE-A-2015-11724, consolidated text updated 2026-11-05: read in part, arts 305.2 b and e, 308, 313 and 338, in the parts cited | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-11724/texto | 2026-11-06 |
| LETA, Ley 20/2007, BOE-A-2007-13409, consolidated text updated 2026-09-02: read in part, art. 38 ter, whole article | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-13409/texto | 2026-11-06 |
| Código Penal, Ley Orgánica 10/1995, BOE-A-1995-25444, consolidated text updated 2026-04-09: read in part, arts 305, 305 bis and 310 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1995-25444/texto | 2026-11-06 |
| Ley 49/2002, BOE-A-2002-25039, consolidated text updated 2026-10-19: read in part, art. 19 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2002-25039/texto | 2026-11-06 |
| RGAT, Real Decreto 1065/2007, BOE-A-2007-15984, consolidated text updated 2026-10-28: read in part, arts 32 c and 33 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2007-15984/texto | 2026-11-06 |
| Reglamento de facturación, Real Decreto 1619/2012, BOE-A-2012-14696, consolidated text updated 2026-03-31: read in part, art. 11 only; arts 8 to 10 not read | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2012-14696/texto | 2026-11-06 |
| RDL 13/2022, BOE-A-2022-12482, consolidated text updated 2026-10-07: read in part, DA 1ª and DT 1ª.1 to 3 and DT 5ª | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2022-12482/texto | 2026-11-06 |
| Real Decreto 2064/1995, BOE-A-1996-1579, consolidated text updated 2026-07-15: read in part, art. 45.1 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1996-1579/texto | 2026-11-06 |
| LSC, Real Decreto Legislativo 1/2010, BOE-A-2010-10544, consolidated text updated 2025-12-19: read in part, art. 4 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2010-10544/texto | 2026-11-06 |
| Orden PJC/297/2026, BOE-A-2026-7296, consolidated text updated 2026-07-16: read in part, preamble, arts 18 and 37 | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2026-7296/texto | 2026-11-06 |
| Orden of 27 March 1998, BOE-A-1998-7200, consolidated text updated 2025-12-18: read in part, operative text and the table | https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1998-7200/texto | 2026-11-06 |
| RDL 3/2026 as published, BOE-A-2026-2548: read in part, art. 3.4 and a search for the reduced cuota | https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-2548 | 2026-11-06 |
| Resolución of 26 February 2026 (repeal of RDL 2/2026), BOE-A-2026-4667: read in part, whole resolution | https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-4667 | 2026-11-06 |
| Resolución of 27 January 2026 (repeal of RDL 16/2025), BOE-A-2026-2024: read in part, whole resolution | https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-2024 | 2026-11-06 |
| Orden HAC/1425/2025, BOE-A-2025-25272: read in part, arts 1 to 6 and DA 1ª | https://www.boe.es/diario_boe/xml.php?id=BOE-A-2025-25272 | 2026-11-06 |
| Orden HAC/277/2026, BOE-A-2026-7041: read in part, arts 7, 11 and 12, Renta dates and payment in 2026 | https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-7041 | 2026-11-07 |
| AEAT Manual IRPF 2025, Andalucía scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-andalucia.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Aragón scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-aragon.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Asturias scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-principado-asturias.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Illes Balears scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-illes-balears.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Canarias scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-canarias.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Cantabria scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-cantabria.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Castilla-La Mancha scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-castilla-mancha.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Castilla y León scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-castilla-leon.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Cataluña scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-cataluna.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Comunitat Valenciana scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunitat-valenciana.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Extremadura scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-extremadura.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Galicia scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-galicia.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Comunidad de Madrid scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-madrid.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Región de Murcia scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-region-murcia.html | 2026-11-06 |
| AEAT Manual IRPF 2025, La Rioja scale: read in part, the scale | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/comunidad-autonoma-rioja.html | 2026-11-06 |
| LIRPF DA 32ª: additionally read in full for the Ceuta/Melilla autonomous-scale import | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 | 2026-11-07 |
| AEAT Manual IRPF 2025, Ceuta and Melilla: read in part, the art. 65 reference | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico/especialidad-escala-autonomica-contribuyentes.html | 2026-11-06 |
| AEAT Manual IRPF 2025, autonomous scales, index: read in part, the list of scales | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico.html | 2026-11-06 |
| AEAT Manual IRPF 2025, autonomous minimum: read in part, general rule | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c14-adecuacion-impuesto-circunstancias-personales/minimo-autonomico-personal-familiar.html | 2026-11-06 |
| AEAT Manual IRPF 2025, Madrid minimum: read in part, personal minimum | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c14-adecuacion-impuesto-circunstancias-personales/minimo-autonomico-personal-familiar/comunidad-madrid-importes-minimo-personal-familiar.html | 2026-11-06 |
| AEAT Manual IRPF 2025, EDS depreciation: read in part, the table, against the Orden | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c07-rendimientos-actividades-economicas-estimacion-directa/fase-1-determinacion-rendimiento-neto/amortizaciones-dotaciones-ejercicio-fiscalmente-deducibles/especialidades-fiscales-amortizaciones-modalidad-simplificada.html | 2026-11-06 |
| AEAT Manual IRPF 2025, LIS art. 12.3: read in part, the EUR 300 limb in IRPF | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c07-rendimientos-actividades-economicas-estimacion-directa/fase-1-determinacion-rendimiento-neto/amortizaciones-dotaciones-ejercicio-fiscalmente-deducibles/supuestos-libertad-amortizacion/libertad-amortizacion-supuestos-contemplados-articulo-12_3.html | 2026-11-06 |
| AEAT Manual IRPF 2025, module limits: read in part, limits for 2025 and 2026 | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c08-rendimientos-actividades-economicas-eo-fores/concepto-ambito-aplicacion/actividades-economicas-desarrolladas-directamente-personas-fisicas/causas-exclusion-metodo-estimacion-objetiva/limites-cuantiativos-excluyentes-reglas-determinacion-rendimientos.html | 2026-11-06 |
| AEAT Manual IVA 2026, simplified regime: read in part, limits for 2026 | https://www3.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2026/capitulo-01-novedades-destacar-2026/regimenes-especiales-simplificado-agricultura-ganaderia-pesca.html | 2026-11-06 |
| AEAT note on RDL 2/2026: read in part, module limits | https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2026/principales-novedades-tributarias-introducidas-real-2-febrero.html | 2026-11-06 |
| AEAT note of 1 April 2026: read in full, the note | https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html | 2026-11-06 |
| AEAT calendar 2026, to 30 January: read in part, Modelos 130, 303 and 390 | https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/enero/hasta-30-enero.html | 2026-11-06 |
| AEAT calendar 2026, to 2 March: read in part, Modelo 347 | https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html | 2026-11-06 |
| AEAT, Modelo 347 dates: read in part, the filing period | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/plazos-presentacion.html | 2026-11-06 |
| AEAT calendar 2026, 8 April to 30 June: read in part, Renta 2025 | https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/abril/8-abril-hasta-30-junio.html | 2026-11-06 |
| AEAT calendar 2026, to 20 April: read in part, Modelos 130 and 303 | https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/abril/hasta-20-abril.html | 2026-11-06 |
| AEAT calendar 2026, to 20 July: read in part, Modelos 130 and 303 | https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/julio/hasta-20-julio.html | 2026-11-06 |
| AEAT calendar 2026, to 20 October: read in part, Modelos 130 and 303 | https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/octubre/hasta-20-octubre.html | 2026-11-06 |
| Seguridad Social, RETA bases page: read in part, a search for the 2026 reduced cuota | https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/10721/10724/1320/1322 | 2026-11-06 |
| TGSS, Import@ss portal: read in part, the portal home page, for its name and purpose | https://portal.seg-social.gob.es/wps/portal/importass/importass/ | 2026-11-06 |
| Hacienda, memoria of the draft módulos order for 2027: read in part, a search for the limits | https://www.hacienda.gob.es/sgt/normativadoctrina/proyectos/22102026-main-om-modulos-2027.pdf | 2026-11-06 |

Not yet confirmed: the historical IRPF art. 17 in force on 31 December 2006, including the claimed 40% capital pension reduction; module limits for 2026 (statute against AEAT criterion; see the conflict note) and for 2027; IVA simplificado limits on the same basis; the reduced cuota amount for an alta in 2026; whether a Budget Act for 2026 exists at this date (none found; RDL 3/2026 art. 3.4 and Orden PJC/297/2026 read); autonomous scales and minimums for 2026; RETA bands for 2027; the Renta campaign and Modelo dates for 2027, including 30 January 2027, a Saturday; actual pension-plan eligibility and all annual contributions; the late-payment interest rate for 2026; LIS DA 17ª and 18ª; the part-year depreciation rule; RD 1619/2012 arts 8 to 10 as changed on 20 April 2026, which [spain-einvoice](spain-einvoice.md) owns; the status of RDL 29/2026; any tax treaty; siblings es-social-contributions and es-autonomous-worker on the EUR 80 amount, and es-autonomous-worker on societarios, against LETA art. 38 ter.9.
