---
name: spain-tax-optimization
description: "Lawful tax planning for Spanish resident self-employed individuals (autónomos) in common territory for tax year 2026, read from the consolidated IRPF, IS, IVA, General Tax and Social Security laws on boe.es, the 2026 contribution order and AEAT pages. Covers the 2026 state and savings scales, autónomo versus SL (25%, 19%/21% micro, 23% small, 15% new), simplified direct assessment and its 5% / EUR 2,000 allowance, the 20% new-activity reduction, home supplies, meals, health insurance, depreciation, loss offsets, pension limits, the startup credit, IVA regimes, RETA bands and the starting reduced fee, timing, red lines and a filing calendar. Trigger on 'reduce tax', 'tax planning', 'save tax', 'deductions I'm missing', 'pagar menos impuestos', 'optimización fiscal', 'deducciones IRPF', 'autónomo fiscal'. Out of scope: Basque Country and Navarra (es-foral-income-tax), detailed computations (es-income-tax, es-autonomous-worker, es-social-contributions, es-corporate-tax, es-beckham)."
version: 1.1
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Tax Optimization

## Spain Tax Optimization -- Self-Employed (Autónomo) Skill v1.1

This skill lists the lawful levers. The pack's domain skills hold the full computations, and where a figure here and a domain skill ever differ, the domain skill wins: [es-income-tax](es-income-tax.md), [es-autonomous-worker](es-autonomous-worker.md), [es-social-contributions](es-social-contributions.md), [es-corporate-tax](es-corporate-tax.md), [es-beckham](es-beckham.md), [es-capital-gains](es-capital-gains.md), [es-irpf-deductions](es-irpf-deductions.md), [es-estimated-tax](es-estimated-tax.md), [es-vat-return](es-vat-return.md). It covers common territory only; the Basque Country and Navarra have their own laws ([es-foral-income-tax](es-foral-income-tax.md)).

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Key optimization legislation | Ley 35/2006 del IRPF (LIRPF); Real Decreto 439/2007 (RIRPF); Ley 27/2014 del Impuesto sobre Sociedades (LIS); Ley 37/1992 del IVA (LIVA) and its regulation (RIVA, RD 1624/1992); Ley 58/2003, General Tributaria (LGT); Real Decreto Legislativo 8/2015 (LGSS); Ley 20/2007 del Estatuto del trabajo autónomo; Orden PJC/297/2026 (2026 contributions) |
| Tax authority attitude to planning | Choosing between lawful options is allowed. The general anti-avoidance rule is the "conflicto en la aplicación de la norma tributaria" (LGT art 15): acts that are "notoriamente artificiosos o impropios" and have no relevant effect other than the tax saving are taxed as the usual act would be, with late-payment interest. Sham transactions (simulación) are taxed on what was really done, with interest and any penalty (LGT art 16). |
| Currency | EUR |
| Tax year | Calendar year: "El período impositivo será el año natural" (LIRPF art 12.1) |
| Filing deadline | Set each year by ministerial order (LIRPF art 97). For 2025 income the window was 8 April to 30 June 2026 (Orden HAC/277/2026). 2026 income is filed in the 2027 campaign. |

### IRPF Rates 2026 (State Scale)

**IRPF Rates 2026 (State Scale)** _(LIRPF art 63.1)_

| Taxable income (EUR) | State rate | Combined rate |
| --- | --- | --- |
| 0 -- 12,450 | 9.5% | State rate plus the community's own rate for the band |
| 12,450 -- 20,200 | 12% | same |
| 20,200 -- 35,200 | 15% | same |
| 35,200 -- 60,000 | 18.5% | same |
| 60,000 -- 300,000 | 22.5% | same |
| 300,000+ | 24.5% | same |

The general base is taxed twice: once on the state scale above and once on the scale of the taxpayer's autonomous community (CCAA). The combined rate therefore depends on the community. Use the community scales in [es-income-tax](es-income-tax.md).

## Section 2 -- Income Splitting & Structuring

### Autónomo vs Sociedad Limitada (SL)

**Autónomo vs Sociedad Limitada (SL) table**  _(LIS art 29.1 and DT 44.2; LIRPF arts 63, 66, 76)_

| Factor | Autónomo (Persona Física) | Sociedad Limitada (SL) |
| --- | --- | --- |
| Top marginal rate | State 24.5% above EUR 300,000, plus the community's rate | General 25%. For periods starting in 2026: turnover in the previous period under EUR 1 million, 19% on the first EUR 50,000 and 21% on the rest; other small companies (turnover under EUR 10 million, LIS art 101) 23%; a new company with a real new activity 15% in its first profitable period and the next |
| Extraction | N/A | Salary (deductible for the company, taxed as employment income) + dividends (savings base 19% to 30%; 19% withholding on payment, RIRPF art 90) |
| When to incorporate | Compare the two after tax and social security on the client's own numbers | Requires notarial deed, compliance costs, annual accounts; see [spain-formation](spain-formation.md) |

- **Family members in the business** -- Wages paid to a spouse or minor children who live with the autónomo and really work in the business are deductible if there is a work contract and Social Security registration and the pay is not above market rates. The family member is taxed on them as employment income _(LIRPF art 30.2.2ª)_.

### Régimen de Estimación Directa

**Régimen de Estimación Directa table**  _(LIRPF arts 30-31; RIRPF arts 28 and 30)_

| Method | Detail |
| --- | --- |
| Estimación Directa Normal (EDN) | Actual income and expenses. Applies when the previous year's net turnover was over EUR 600,000, or when the taxpayer renounces the simplified method (then for at least three years). |
| Estimación Directa Simplificada (EDS) | Actual expenses, simplified depreciation table, plus a 5% allowance for provisions and hard-to-justify expenses, capped at EUR 2,000 a year. For prior-year net turnover up to EUR 600,000, unless renounced. |
| Estimación Objetiva (módulos) | Fixed yield from objective indicators for listed activities. Excluded where the previous year's receipts exceed EUR 150,000 (EUR 75,000 of it invoiced to businesses) or purchases exceed EUR 150,000. The higher 250,000 / 125,000 / 250,000 limits applied 2016 to 2024; the decree that would have extended them was revoked by Congress on 26 February 2026. See [es-autonomous-worker](es-autonomous-worker.md). |

The 5% allowance (up to EUR 2,000) is applied in EDS without receipts. It does not apply if the taxpayer takes the low-income reduction of RIRPF art 26.1 instead.

### Ley Beckham (Régimen de Impatriados)

**Ley Beckham table**  _(LIRPF art 93)_

| Feature | Detail | Legislation |
| --- | --- | --- |
| Flat rate | 24% on the base up to EUR 600,000; 47% above | LIRPF art 93.2 |
| Eligibility | Not resident in Spain in the five tax periods before the move | LIRPF art 93.1.a |
| Duration | The year residence changes and the next five | LIRPF art 93.1 |
| Who can use it | Employees (including remote workers), directors (with limits for holding companies), entrepreneurs with an approved "actividad emprendedora", and highly qualified professionals serving startups or doing R&D. The old "employment income only" rule no longer holds. Income through a Spanish permanent establishment excludes it, except for the last two groups. | LIRPF art 93.1.b-c |

Detail: [es-beckham](es-beckham.md).

## Section 3 -- Deductions Most People Miss

### Gastos Deducibles para Autónomos (IRPF Art. 28-30)

**Gastos Deducibles para Autónomos table**  _(LIRPF arts 28-30; RIRPF arts 9 and 30)_

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Cuota de autónomos (RETA) | [es-autonomous-worker](es-autonomous-worker.md) | The autónomo's own RETA contributions are an expense of the activity. For 2026 the minimum monthly bases run from EUR 653.59 to EUR 1,928.10 by income band (Section 8). |
| Provisión gastos difícil justificación | RIRPF art 30.2ª; LIRPF art 30.2.4ª | 5% of net income before this item, max EUR 2,000/year. EDS only, no receipts needed. |
| New-activity reduction | LIRPF art 32.3 | Someone starting an activity in direct assessment reduces positive net income by 20% in the first profitable year and the next, on at most EUR 100,000 a year. Conditions on previous activity apply; see [es-autonomous-worker](es-autonomous-worker.md). |
| Suministros del hogar (home utilities) | LIRPF art 30.2.5ª.b) | Water, gas, electricity, phone and internet of the main home used partly for the business: 30% × (business m² ÷ total m²) × the cost, unless a higher or lower share is proved. |
| Gastos de manutención (own meals) | LIRPF art 30.2.5ª.c); RIRPF art 9 | Own meals while working, in restaurants or hotels, paid electronically, up to the per-day limits for employees: EUR 26.67 in Spain / EUR 48.08 abroad, or EUR 53.34 / EUR 91.35 with an overnight stay elsewhere. |
| Seguro de salud (private health insurance) | LIRPF art 30.2.5ª.a) | Deductible expense: up to EUR 500 a year per person (EUR 1,500 per person with a disability) for the autónomo, spouse and children under 25 who live with them. |
| Vehículo (IVA deductible 50%) | LIVA art 95.Tres.2ª | Cars and motorcycles are presumed 50% used in the business for IVA. A higher share must be proved. The IRPF rule is stricter: see [es-autonomous-worker](es-autonomous-worker.md). |
| Formación profesional | LIRPF art 28 | Courses, certifications and conferences needed for the activity, as an ordinary expense. |
| Cuotas colegiales | LIRPF art 28 | Professional body fees needed for the activity, as an ordinary expense. |
| Amortización | LIRPF art 29; RIRPF art 30.1ª | Depreciation of business assets; in EDS, by the simplified table (Section 4). |
| Reparaciones y conservación | LIRPF art 28 | Repairs and maintenance of business assets. |
| Primas de seguro | LIRPF art 28 | Professional liability, premises and the business part of vehicle insurance. |
| Reinvested profits (EDS small businesses) | LIRPF art 68.2.b | Net activity income reinvested in new business fixed assets in the same or next year: credit of 5% (2.5% if the new-activity reduction was used). |

## Section 4 -- Capital Allowances Optimization

**Legislation:** LIRPF art 29; RIRPF art 30.1ª; LIS art 12.3 (via LIRPF art 28)

### Simplified Depreciation Table (Estimación Directa Simplificada)

**Simplified Depreciation Table**  _(AEAT, Manual de actividades económicas 3.5.4)_

| Asset category | Maximum annual rate | Maximum years |
| --- | --- | --- |
| Buildings and other constructions | 3% | 68 |
| Installations, furniture, fittings and other fixed assets | 10% | 20 |
| Machinery | 12% | 18 |
| Vehicles (elementos de transporte) | 16% | 14 |
| IT equipment and software | 26% | 10 |
| Tools (útiles y herramientas) | 30% | 8 |

### Libertad de Amortización (Free Depreciation)

- **Free depreciation for low-value assets** -- New tangible fixed assets with a unit value of no more than EUR 300 may be written off at once, up to EUR 25,000 in total for the tax period (pro rata for a shorter period).  _(LIS art 12.3.e; applied to IRPF business income through LIRPF art 28.1)_

### Timing Strategy

Buying a depreciable asset early in the year gives a larger first-year charge than buying it in December, because depreciation runs from when the asset is in use.

## Section 5 -- Loss Utilization

- **Legislation** -- LIRPF arts 48-50  _(LIRPF arts 48-50)_

**Loss Utilization table**  _(LIRPF arts 48-50)_

| Relief | Detail |
| --- | --- |
| Offset against general base | Negative business income offsets other general income (employment, rental) of the same year without limit (art 48.a). |
| Carry-forward | If the general base is still negative, it is carried forward against positive general bases of the next four years (art 50.3). |
| No carry-back | IRPF has no carry-back. Losses only go forward. |
| General-base gains and losses | A net loss from gains and losses not arising on a transfer (for example some prizes and grants) offsets up to 25% of the positive balance of income in the general base; any excess carries forward four years (art 48.b). |
| Base del ahorro offset | Within the savings base, a net loss on savings income (interest, dividends) offsets up to 25% of the net gain on transfers, and the other way round. Any excess carries forward four years in the same order (art 49). Savings losses do not reduce the general base. |

### Strategy

In the start-up phase, a loss in the business reduces employment or rental income of the same year. If the whole general base turns negative, use it in the next four years before it expires.

## Section 6 -- Timing Strategies

**Timing Strategies table**

| Strategy | Detail |
| --- | --- |
| Defer invoicing | Under estimación directa, income and expenses follow accrual. Cash timing matters for IVA and for the quarterly payments. For módulos the yield does not depend on invoice timing. |
| Accelerate expenses | Business income and expenses are allocated by the corporate tax rules, so by accrual (LIRPF art 14.1.b). Expenses that accrue before 31 December count in that year; paying in advance does not on its own move the expense. |
| Plan de pensiones contributions | Contributions reduce the general base. Make them before 31 December (Section 9). |
| Ganancias/pérdidas patrimoniales timing | Realise losses before year end to offset gains (Section 5). A loss on listed shares is not allowed while homogeneous shares bought within two months before or after the sale are still held; for unlisted shares the window is one year (LIRPF art 33.5.f-g). |
| Retenciones management | Professionals invoicing Spanish businesses suffer 15% withholding. A new professional can use 7% in the start year and the next two, if they had no professional activity in the year before (RIRPF art 95.1). |
| Matrimonial tax choice | A married couple (or a single parent family) can file jointly. The joint return reduces the base by EUR 3,400 a year for a married couple (LIRPF art 84.2.3º). Compare joint and separate returns each year. |
| Módulos exit timing | Leaving módulos for direct assessment is done by renunciation, which binds for at least three years (RIRPF art 33.3). Plan it for the start of a year. |
| Pago fraccionado (Modelo 130) | 20% of cumulative net income for the year to date, less withholding and earlier payments (RIRPF art 110). Professionals with at least 70% of income withheld in the previous year are exempt (RIRPF art 109). |

## Section 7 -- VAT Optimization (IVA)

- **Legislation** -- Ley 37/1992 del IVA and RD 1624/1992 (RIVA)  _(Ley 37/1992 del IVA)_

**VAT Optimization table**  _(LIVA; RIVA)_

| Strategy | Detail |
| --- | --- |
| Rates | General 21% (LIVA art 90); reduced 10% and 4% only for listed supplies (art 91). |
| Régimen General vs Simplificado | General: quarterly Modelo 303 by the 20th of April, July and October, and by 30 January for the last quarter (RIVA art 71.4). Simplificado: for módulos activities, with four returns a year (RIVA art 41). |
| Recargo de Equivalencia | Retailers buying from wholesalers pay the surcharge on purchases (5.2% general, 1.4% for 10% goods, 0.5% for 4% goods, 1.75% for tobacco, LIVA art 161) and file no IVA returns for that activity. It simplifies compliance but there is no input IVA recovery. |
| Criterio de Caja (cash basis IVA) | Output IVA falls due when the client pays (or on 31 December of the following year at the latest). Available if the previous year's volume of operations was no more than EUR 2,000,000. Must opt in (LIVA art 163 bis). |
| IVA deducible on vehicles | Cars and motorcycles are presumed 50% business use (LIVA art 95.Tres.2ª). A higher share needs proof. |
| Pro rata for mixed activities | With taxable and exempt activities, check the pro rata method each year to recover the right share of input IVA. |
| Modelo 390 (annual summary) | Filed in the first 30 days of January for the year before (RIVA art 71.7; AEAT). Review it for missed input IVA. |

## Section 8 -- Social Security Optimization

- **Legislation** -- LGSS (Real Decreto Legislativo 8/2015); Ley 20/2007 art 38 ter; Orden PJC/297/2026  _(LGSS (Real Decreto Legislativo 8/2015); RD-Ley 13/2022 (progressive RETA system))_

### Progressive Cuota de Autónomos (2026 bands)

Since 2023 the autónomo chooses a monthly base from the band for the expected net income. The bands below are the 2026 bands. The monthly quota at the minimum base is computed at 31.50%: common contingencies 28.30% + occupational 1.30% + cessation 0.90% + training 0.10% + intergenerational equity (MEI) 0.90% _(Orden PJC/297/2026 arts 18.1-18.2 and 37.5-37.6)_.

**Progressive Cuota de Autónomos table**

| Net monthly income (EUR) | 2026 minimum base (EUR) | Monthly quota at the minimum base (EUR) |
| --- | --- | --- |
| ≤ 670 | 653.59 | 205.88 |
| > 670 -- 900 | 718.95 | 226.47 |
| > 900 -- < 1,166.70 | 849.67 | 267.65 |
| 1,166.70 -- 1,300 | 950.98 | 299.56 |
| > 1,300 -- 1,500 | 960.78 | 302.65 |
| > 1,500 -- 1,700 | 960.78 | 302.65 |
| > 1,700 -- 1,850 | 1,143.79 | 360.29 |
| > 1,850 -- 2,030 | 1,209.15 | 380.88 |
| > 2,030 -- 2,330 | 1,274.51 | 401.47 |
| > 2,330 -- 2,760 | 1,356.21 | 427.21 |
| > 2,760 -- 3,190 | 1,437.91 | 452.94 |
| > 3,190 -- 3,620 | 1,519.61 | 478.68 |
| > 3,620 -- 4,050 | 1,601.31 | 504.41 |
| > 4,050 -- 6,000 | 1,732.03 | 545.59 |
| > 6,000 | 1,928.10 | 607.35 |

The maximum base in every band from EUR 4,050 up is EUR 5,101.20 a month. Full table, bases and exceptions: [es-social-contributions](es-social-contributions.md).

### Optimization Strategies

**Optimization Strategies table**

| Strategy | Detail |
| --- | --- |
| Tarifa plana (reduced starting fee) | On first registration, or after two years out of RETA (three if the reduced fee was used before): a reduced fee for common and occupational contingencies for the first 12 full calendar months, with no cessation or training contribution. A further 12 months if expected net income is below the annual minimum wage. Must be requested at registration (Ley 20/2007 art 38 ter). The amount was EUR 80 a month in 2023 to 2025; from 2026 the State Budget Law sets it (RD-ley 13/2022, DT 5). |
| Income bracket management | A lower base means a lower quota, but also lower benefits. The chosen base is provisional. |
| Regularización anual | After the year, Social Security regularises the bases and quotas against the net income reported by the tax authority. Underpayments are charged and overpayments refunded (LGSS art 308.1.c). |
| Cese de actividad (unemployment) | Autónomos pay 0.90% for cessation cover. The benefit lasts from 4 months (12-17 months contributed) to 24 months (48 or more months contributed) (LGSS art 338.1). |
| Pluriactividad (dual activity) | Someone employed and self-employed at the same time gets back 50% of the amount by which total common-contingency contributions (both jobs, employer and employee) exceed EUR 17,323.68 in 2026, capped at 50% of the RETA common-contingency quotas. Social Security pays it within four months of the regularisation (Orden PJC/297/2026 art 18.8; LGSS art 313). |

## Section 9 -- Investment & Retirement

### Planes de Pensiones -- IRPF Art. 51-52

**Planes de Pensiones table**  _(LIRPF arts 51-52)_

| Feature | Detail |
| --- | --- |
| Individual plan limit | Lower of EUR 1,500 a year and 30% of net employment plus business income (reduces base imponible general) |
| Employer plan (plan de empleo) | Up to EUR 8,500 more a year from employer contributions (and matching employee contributions within the art 52 table) |
| Autónomo plans | Up to EUR 4,250 more a year for contributions by autónomos to sector plans, simplified self-employed employment plans (PPES) and the other listed instruments |
| Combined autónomo limit | EUR 1,500 (individual) + EUR 4,250 (autónomo plans) = **EUR 5,750/year**, within the 30% limit |
| Tax saving | Contribution × marginal rate. Example 1 shows it. |
| Exit taxation | Taxed as employment income on withdrawal |
| Pre-2007 contributions | The reduction in force on 31 December 2006 can still apply to benefits from contributions made up to that date, if taken in the year of the event or the next two (LIRPF DT 12). |
| Unused contributions | Contributions not reduced for lack of base or because of the 30% limit can be used in the next five years (LIRPF art 52.2). |

### Inversión en Empresas de Nueva Creación -- IRPF Art. 68.1

**Inversión en Empresas de Nueva Creación table**  _(LIRPF art 68.1)_

| Feature | Detail |
| --- | --- |
| Deducción | 50% of the subscription for shares in a new or recent company, against the state share of tax |
| Base | At most EUR 100,000 a year |
| Requirements | SA, SL, SAL or SLL not listed; a real economic activity; own funds no more than EUR 400,000 when the shares are acquired; shares acquired at formation or in a capital increase within five years of formation (seven for startups under Ley 28/2022); held more than three and less than twelve years; the investor and family hold no more than 40% (except founders of a startup); a certificate from the company |
| Maximum deducción | EUR 50,000/year (50% of the EUR 100,000 base) |

Detail: [es-irpf-deductions](es-irpf-deductions.md).

### Base del Ahorro (Savings Tax)

**Base del Ahorro table**  _(LIRPF arts 66 and 76: state half plus community half)_

| Gains/income (EUR) | Rate |
| --- | --- |
| 0 -- 6,000 | 19% |
| 6,000 -- 50,000 | 21% |
| 50,000 -- 200,000 | 23% |
| 200,000 -- 300,000 | 27% |
| 300,000+ | 30% |

**Strategy:** Spreading gains over several years keeps more of them in the lower bands. The first EUR 6,000 of savings base each year is taxed at 19%.

## Section 10 -- Red Lines

**Red Lines table**

| Risk | Detail |
| --- | --- |
| Conflicto en la aplicación de la norma (Art. 15 LGT) | Artificial or improper acts whose only relevant effect is the saving are taxed as the usual act would be, plus late-payment interest (art 15.3). A penalty is possible where the arrangement matches one already published as a conflict case (art 206 bis). |
| Simulación (Art. 16 LGT) | Sham transactions: the real transaction is taxed, with interest and the penalty that applies (art 16.3). Unpaid tax penalties run 50% (minor), 50% to 100% (serious) and 100% to 150% (very serious) of the unpaid amount (LGT art 191). |
| Economía sumergida | Tax fraud of more than EUR 120,000 per tax and year is a crime: prison of one to five years and a fine of up to six times the amount (Código Penal art 305.1). |
| Factura falsa | Issuing invoices with false data is a very serious tax infringement: a fine of 75% of the operations involved (LGT art 201.3). Keeping false or double books is a crime with prison of five to seven months; for unrecorded or false entries the amount must exceed EUR 240,000 a year (Código Penal art 310). |
| Anti-wash rule | No loss on listed shares if homogeneous shares are bought within two months before or after; one year for unlisted (LIRPF art 33.5.f-g). |
| Tarifa plana abuse | The reduced fee needs two years out of RETA, or three if the reduced fee was used before (Ley 20/2007 art 38 ter). Re-registering early does not qualify. |
| Vinculación (related party transactions) | Transactions between an autónomo and their own SL (or a family SL) must be at market value (LIS art 18). |
| CCAA deduction eligibility | A person is resident in the community where they spend most days in the year, with a presumption for the main home (LIRPF art 72.1). A change of community whose main purpose is lower tax has no effect (LIRPF art 72.3). |

## Section 11 -- Annual Tax Planning Calendar

**Annual Tax Planning Calendar table**

| Month | Action |
| --- | --- |
| January | By 30 January: Modelo 303 (Q4 IVA), Modelo 130 (Q4 IRPF payment) and Modelo 390 (annual IVA summary). Review the prior year's income and expenses. Ask for the reduced starting fee at registration if new. |
| February | Modelo 347 (annual third-party operations over EUR 3,005.06; for 2025 operations the window was 1 February to 2 March 2026). Gather invoices, bank statements and RETA receipts. |
| March | Review plan de pensiones capacity and unused contributions from earlier years. |
| April | Renta campaign opens (8 April in 2026). File Modelo 303 + Modelo 130 for Q1 by the 20th. Compare a joint and an individual return if married. |
| May | Complete the Renta return. Check the AEAT draft for missing business expenses, pension contributions and community deductions. |
| June | Renta deadline (30 June in 2026, set by the year's order). |
| July | File Modelo 303 + Modelo 130 for Q2 by the 20th. Mid-year income review; change the RETA base if income has moved bands (LGSS art 308.1.a.3ª). |
| August | Plan second-half purchases: equipment, training. |
| September | Review the IVA position: missed input IVA, pro rata. |
| October | File Modelo 303 + Modelo 130 for Q3 by the 20th. Estimate full-year income. |
| November | Use the pension limits (EUR 1,500 + EUR 4,250 for autónomo plans). Realise capital losses to offset gains, watching the anti-wash rule. |
| December | Bring forward deductible expenses that will accrue this year. Make charitable donations. Buy and bring into use assets to depreciate. |

## Section 12 -- Cash Impact Examples

The examples use a combined marginal rate of 37% as an assumption. The real marginal rate depends on the client's base and community scale ([es-income-tax](es-income-tax.md)).

### Example 1 -- Plan de Pensiones (Autónomo, Net Income EUR 45,000)

**Example 1 table**

| Contribution (individual EUR 1,500 + autónomo plan EUR 4,250) | EUR 5,750 (below 30% × 45,000 = EUR 13,500) |
| --- | --- |
| Tax saving at an assumed 37% marginal rate | **EUR 2,127.50/year** |

### Example 2 -- Provisión de Gastos de Difícil Justificación (EDS)

**Example 2 table**

| Net rendimientos before provisión | EUR 40,000 |
| --- | --- |
| 5% provisión = EUR 2,000 (cap EUR 2,000) | EUR 2,000 |
| Tax saving at 37% | **EUR 740/year** |

### Example 3 -- Suministros del Hogar (15m² office in 90m² home)

**Example 3 table**

| Annual home costs (electricity + water + gas + internet) | EUR 3,600 |
| --- | --- |
| Workspace proportion (15/90) | 16.67% |
| Deductible (30% of proportion) | EUR 3,600 × 15/90 × 30% = EUR 180 |
| Tax saving at 37% | **EUR 66.60/year** |

### Example 4 -- Gastos de Manutención (100 Travel Days/Year)

**Example 4 table**

| Deductible meals (100 days in Spain, no overnight, actual spend at least the limit) | 100 × EUR 26.67 = EUR 2,667 |
| --- | --- |
| Tax saving at 37% | **EUR 986.79/year** |

### Example 5 -- Seguro de Salud (Family of 4)

**Example 5 table**

| Premium (autónomo, spouse, two children under 25 living at home: 4 × EUR 500) | EUR 2,000 |
| --- | --- |
| Tax saving at 37% | **EUR 740/year** |

### Example 6 -- Tarifa Plana (First 12 Months)

**Example 6 table**

| Ordinary quota at the minimum base for income of EUR 1,166.70 to 1,300 a month | EUR 950.98 × 31.50% = EUR 299.56/month |
| --- | --- |
| Ordinary quota for 12 months | EUR 3,594.72 |
| Reduced starting fee | EUR 80/month in 2023 to 2025; the 2026 amount is set by the State Budget Law (not yet confirmed) |
| **Annual saving** | EUR 3,594.72 minus 12 × the reduced fee. At EUR 80 it would be EUR 2,634.72. |

### Example 7 -- Startup Investment (EUR 20,000 in Nueva Creación)

**Example 7 table**

| Deducción (50% of EUR 20,000) | **EUR 10,000** |
| --- | --- |
| Direct reduction of the state share of tax (cuota íntegra estatal) | **EUR 10,000** |

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Ley 35/2006 del IRPF, consolidated text (last update 07/10/2026), arts 12, 28-33, 48-52, 63, 66, 68, 72, 76, 84, 93, 97, DT 12, DT 32 | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 | 2026-10-30 |
| Real Decreto 439/2007 (RIRPF), consolidated text, arts 9, 28, 30, 90, 95, 109-111 | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 | 2026-10-30 |
| Ley 27/2014 del Impuesto sobre Sociedades, consolidated text, arts 12.3, 18, 29, 101, DT 44 | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 | 2026-10-30 |
| Ley 37/1992 del IVA, consolidated text, arts 90, 91, 95, 161, 163 bis | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 | 2026-10-30 |
| Real Decreto 1624/1992 (RIVA), consolidated text, arts 41, 71 | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 | 2026-10-30 |
| Ley 58/2003 General Tributaria, consolidated text, arts 15, 16, 191, 201, 206 bis | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 | 2026-10-30 |
| Real Decreto 1065/2007 (Reglamento general de gestión e inspección), art 33 (Modelo 347 threshold) | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 | 2026-10-30 |
| Código Penal, consolidated text, arts 305, 310 | https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444 | 2026-10-30 |
| Real Decreto Legislativo 8/2015 (LGSS), consolidated text, arts 308, 313, 338 | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 | 2026-10-30 |
| Ley 20/2007 del Estatuto del trabajo autónomo, consolidated text, art 38 ter | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 | 2026-10-30 |
| Real Decreto-ley 13/2022, preamble on DT 5 (reduced fee 2023-2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482 | 2026-10-30 |
| Orden PJC/297/2026, 2026 contribution rules, arts 18 and 37 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 | 2026-10-30 |
| Orden HAC/277/2026, IRPF 2025 return models and filing window | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7041 | 2026-10-30 |
| AEAT, Manual de actividades económicas 3.5.4, simplified depreciation table | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html | 2026-10-30 |
| AEAT, Modelo 347 filing period | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/plazos-presentacion.html | 2026-10-30 |
| AEAT, Modelo 390 filing period | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-390-iva-declaracion-resumen-anual_/plazos-presentacion.html | 2026-10-30 |
| AEAT, Renta 2025 campaign page | https://sede.agenciatributaria.gob.es/Sede/Renta.html | 2026-10-30 |

Not yet confirmed: (1) the amount of the reduced starting fee (tarifa plana) for new registrations in 2026; the law leaves it to the State Budget Law, and no 2026 amount was found (es-social-contributions and es-autonomous-worker say the same). (2) No statutory sentence was quoted for the deduction of the autónomo's own RETA contributions; it rests on the pack's es-autonomous-worker skill. (3) The old file's "typical combined rate" column (about 19% to 54%) and its ranking of communities (Madrid lowest; Cataluña, Valencia and Extremadura among the highest) have no single official source and were removed; use the community scales in es-income-tax. (4) The old rule of thumb to incorporate once profits pass about EUR 40,000 to 50,000 has no official source. (5) The old file's "AEAT monitors gaps under 2-3 years" for the reduced fee is not an official statement; only the statutory two-year and three-year rules are given. (6) The 2027 dates for the Renta campaign, Modelo 347 and Modelo 390 are not yet published. (7) The day-count rule for first-year depreciation was not read in the IS regulation.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
