---
name: uruguay-income-tax
description: "Uruguay personal income tax (IRPF, Impuesto a la Renta de las Personas Físicas) for tax year 2026 under Título 7 of the Texto Ordenado 2023 as amended by Ley 20.446 of 16 December 2025. Covers residence (183 days, centre of interests), the dual system, Categoría II labour income on the 0% to 36% scale in BPC (BPC 2026 UYU 6,864, Decreto 11/026), the aguinaldo and salario vacacional rate, the family-unit (núcleo familiar) scales, the deduction credit at 14% or 8%, the 20 BPC child deduction, the mortgage and rent credits, the 30% expense deduction for independent work, Categoría I capital income at 12%, 7% and the reduced interest rates, foreign capital income taxed from 1 January 2026, filing on forms 1101, 1102 and 1103, the five balance instalments and DGI penalties. Trigger on: IRPF 2026, franjas IRPF, deducciones IRPF, declaración jurada IRPF, núcleo familiar, rentas del exterior, Uruguay income tax. Out of scope: payroll withholding and BPS contributions, IRAE, IRNR, IASS."
version: 0.3
jurisdiction: UY
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Uruguay: personal income tax (IRPF) for 2026 v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill computes the annual IRPF of a resident individual (or a family unit that opts to file jointly) for the 2026 calendar year. It links to the other Uruguay skills and does not repeat them:

- [uruguay-payroll](uruguay-payroll.md): the employer's monthly IRPF withholding (anticipos).
- [uruguay-social-contributions](uruguay-social-contributions.md): BPS, FONASA and FRL contribution rates. Those contributions feed the deduction credit below, but their rates live there.
- [uy-corporate-income-tax](uy-corporate-income-tax.md): IRAE, including the option for independent workers to pay IRAE instead of IRPF.

**Which text of the law.** Título 7 (IRPF) of the Texto Ordenado 2023 approved by Decreto 101/024, as published by IMPO with the amendments of Ley 20.446 of 16 December 2025 (Budget Law, Diario Oficial 8 January 2026) already integrated. The regulation is Decreto 148/007, amended for foreign income by Decreto 95/026 of 6 May 2026. The law sets amounts in BPC (Base de Prestaciones y Contribuciones) or UI (Unidad Indexada); this skill converts BPC amounts at the 2026 value.

**Quick reference, 2026**

| Item | Figure |
|---|---|
| Tax year | Calendar year 2026; the tax arises on 31 December 2026 (T7 art. 7) |
| BPC 2026 | UYU 6,864 from 1 January 2026 (Decreto 11/026) |
| Labour income (Categoría II), individual | 0% up to 84 BPC (UYU 576,576), then 10%, 15%, 24%, 25%, 27%, 31%, and 36% above 1,380 BPC (UYU 9,472,320) |
| Deduction credit | 14% of allowable deductions if nominal income is 180 BPC (UYU 1,235,520) or less, otherwise 8% |
| Capital income (Categoría I) | 12% general; 7% on taxable dividends and author's rights; lower rates on some local interest |
| Annual return for 2025 income | Filed 29 June to 31 August 2026; balance in 5 instalments, the last on 30 December 2026 |

## Who this applies to

- **Residents.** An individual is resident in Uruguay for the calendar year if they stay more than 183 days in Uruguay (sporadic absences count, unless they prove tax residence in another country), or if the main core or base of their activities or of their economic or vital interests is in Uruguay. Vital interests are presumed, unless proven otherwise, when the spouse and dependent minor children habitually live in Uruguay (T7 art. 2). Uruguayan nationals on diplomatic, consular or official postings abroad are resident (same article).
- **Who pays.** Resident individuals, and family units (núcleos familiares) of resident spouses or judicially recognised cohabitants who opt to file jointly (T7 art. 8). The joint option covers only Categoría II, is made once a year, and is not available if either member pays IRAE, IRNR, IMEBA or IASS, or if the marriage or union starts or ends during the year. Spouses must be under the community property regime (sociedad conyugal).
- **What is taxed.** Uruguayan-source income: activities carried out, assets situated or rights used in Uruguay (T7 art. 6(1)). From 1 January 2026 also capital yields from non-resident entities and gains on those assets (T7 art. 6(2), as replaced by Ley 20.446 art. 653), except the rentals of movable and intangible property, image rights and derivative income listed in art. 18 A), C) and D). The DGI lists the new heads as foreign movable capital yields, foreign real-estate yields and gains on both. Derivative income is taxed under art. 6(3).
- **Two categories, taxed separately** (T7 art. 11). Categoría I: capital yields, capital gains and imputed income. Categoría II: labour income, inside or outside employment, and compensated inactivity subsidies. Losses stay in their own category and carry forward at most two years.
- **Out of scope.** Non-residents (IRNR), business income taxed under IRAE, pensions taxed under IASS, and the employer's monthly withholding. Clients in arrears or under DGI enforcement go to a contador público.

## Rates, bands and thresholds

All BPC amounts are at UYU 6,864 for 2026. The annual scale applies to the annual renta computable.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| BPC value from 1 January 2026 | UYU 6,864 a month (UYU 6,576 in 2025 under Decreto 5/025; increase 4.38%) | 2026 | https://www.impo.com.uy/bases/decretos/11-2026 |
| Categoría II individual: up to 84 BPC (UYU 576,576, computed: 84 x the 2026 BPC of UYU 6,864), the mínimo no imponible general | Exempt | 2026 | https://www.impo.com.uy/bases/todgi-2023/7-2024 (T7 art. 48 A) |
| Over 84 BPC up to 120 BPC (UYU 823,680) | 10% | 2026 | same, art. 48 A |
| Over 120 BPC up to 180 BPC (UYU 1,235,520) | 15% | 2026 | same, art. 48 A |
| Over 180 BPC up to 360 BPC (UYU 2,471,040) | 24% | 2026 | same, art. 48 A |
| Over 360 BPC up to 600 BPC (UYU 4,118,400) | 25% | 2026 | same, art. 48 A |
| Over 600 BPC up to 900 BPC (UYU 6,177,600) | 27% | 2026 | same, art. 48 A |
| Over 900 BPC up to 1,380 BPC (UYU 9,472,320) | 31% | 2026 | same, art. 48 A |
| Over 1,380 BPC | 36% | 2026 | same, art. 48 A |
| Núcleo familiar where each member's Categoría II income exceeds 12 SMN: exempt up to 168 BPC (UYU 1,153,152); 15% to 180 BPC; then 24%, 25%, 27%, 31%, 36% at the individual band edges | as stated | 2026 | same, art. 48 B |
| Núcleo familiar where one member's Categoría II income does not exceed 12 SMN: exempt up to 96 BPC (UYU 658,944); 10% to 144 BPC (UYU 988,416); 15% to 180 BPC; then 24%, 25%, 27%, 31%, 36% at the individual band edges | as stated | 2026 | same, art. 48 C |
| National minimum wage (SMN), used for the 12 SMN test | UYU 24,572 a month from 1 January 2026; UYU 25,383 from 1 July 2026 | 2026 | https://www.impo.com.uy/bases/decretos/319-2025 |
| Aguinaldo (sueldo anual complementario) and salario vacacional required by law | Kept out of the scale; taxed at the rate of the highest band the other income reaches | 2026 | https://www.impo.com.uy/bases/todgi-2023/7-2024 (T7 art. 47, art. 48 last paragraph) |
| Deduction credit rate, nominal annual income (without aguinaldo and salario vacacional) up to 180 BPC (UYU 1,235,520) | 14% of the deductions in art. 49 A) to F) | 2026 | same, art. 49 |
| Deduction credit rate, nominal annual income above 180 BPC | 8% of the same deductions | 2026 | same, art. 49 |
| Child deduction (education, food, housing, health not covered by FONASA), per minor child in the taxpayer's care, including minors placed for adoption | 20 BPC a year (UYU 137,280) | 2026 | same, art. 49 D) |
| Child deduction, child legally declared incapable or with a severe disability (BPS criteria), any age | 40 BPC a year (UYU 274,560), double the above | 2026 | same, art. 49 D) |
| Mortgage instalments on the only permanent home, home cost not over UI 1,000,000 | Instalments paid, capped at 36 BPC a year (UYU 247,104) | 2026 | same, art. 49 E) |
| Rent credit, tenant of a permanent home, landlord identified | Up to 8% of the rent, credited against IRPF | 2026 | same, art. 51 |
| Independent work (servicios personales fuera de la relación de dependencia), not under IRAE | 30% of income deducted as expenses, plus bad debts | 2026 | same, art. 45 |
| Categoría I, restantes rentas (rents, most interest, foreign capital income, gains) | 12% | 2026 | same, art. 37 B) |
| Dividends and profits paid by IRAE taxpayers out of IRAE-taxed income, and deemed dividends (art. 19) | 7% | 2026 | same, art. 37 B) |
| Income from author's rights on literary, artistic or scientific works | 7% | 2026 | same, art. 37 B) |
| Foreign capital income of people resident from 2020 who opted under art. 24 second paragraph b) | 7% | 2026 | same, art. 37 B) |
| Interest on local bank deposits and on publicly issued, listed debt of resident issuers, in pesos at a fixed nominal rate: 1 year or less / over 1 to 3 years / over 3 years | 5.5% / 2.5% / 0.5% | 2026 | same, art. 37 A) |
| Same, pesos with an adjustment clause (for example UI): 1 year or less / over 1 to 3 years / over 3 years | 10% / 7% / 5% | 2026 | same, art. 37 A) |
| Same, foreign currency: 1 year or less / over 3 years (the over 1 to 3 years cell is blank in the IMPO consolidated text: see Not yet confirmed) | 12% / 7% | 2026 | same, art. 37 A) |
| Rental income exemption | Exempt if all rents are 40 BPC a year (UYU 274,560) or less and the owner lifts bank secrecy; lost if other capital yields exceed 3 BPC (UYU 20,592) | 2026 | same, art. 38 J) |
| Small disposals exemption | Each disposal UI 30,000 or less, and the year's total of such disposals under UI 90,000 | 2026 | same, art. 38 I) |
| Sale of permanent home exemption | Sale UI 1,200,000 or less, at least 50% reinvested in a new permanent home within 12 months, new home UI 1,800,000 or less | 2026 | same, art. 38 L) |
| Optional gain on property bought before 1 July 2007 (non-rural) and on property abroad | 15% of the sale price (never below the cadastral value for Uruguayan property) | 2026 | same, art. 29 |
| Other disposals without a provable cost, and the optional rule for foreign assets | Gain = 20% of the sale price | 2026 | same, art. 32 |
| Late filing of a return (contravención) | UYU 910 per return; UYU 2,730 maximum for several no-activity returns filed together | 2026 | https://www.impo.com.uy/bases/resoluciones-dgi/97-2026 |
| Late payment fine (mora) | 5% if paid within 5 working days; 10% up to 90 calendar days; 20% after that; plus a monthly surcharge (recargo) set by the Executive | 2026 | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 |

## The base

**Categoría II, labour income.**

- **Employment** (T7 art. 42): all regular or extraordinary pay in cash or kind, including allowances and per diems without accounts, the salario vacacional, and severance above the legal minimum (only the excess is taxed). FONASA and similar health benefits are not taxable (art. 40).
- **Independent work** (T7 art. 45): fees for personal services outside employment that are not under IRAE. Deduct a flat 30% for expenses plus bad debts; actual expenses are not deducted. An independent worker who opts into IRAE under T4 art. 14 leaves IRPF for that income (see the corporate skill).
- **Timing** (art. 41): accrual. Aguinaldo and salario vacacional count in the month they must be paid. Irregular income generated over more than two years can be spread over up to three years (independent) or taxed when paid at the rate of the spread amount (employed).
- **Computation, in order** (arts. 46 to 49 and 51):
  1. Add the year's renta computable, leaving out aguinaldo and salario vacacional.
  2. Apply the scale (individual art. 48 A, or the family scale B or C) band by band.
  3. Tax the aguinaldo and salario vacacional at the rate of the highest band reached in step 2.
  4. Add the deductions: BPS and other pension-fund contributions (art. 49 A), FONASA, FRL and similar health contributions (B), the Fondo de Solidaridad and its additional (C), child deductions (D), capped mortgage instalments (E) and CJPB items (F).
  5. Multiply the total by 14% or 8% (the 180 BPC test on nominal income without aguinaldo and salario vacacional) and subtract the result from the tax of steps 2 and 3.
  6. Subtract the rent credit (up to 8% of rent, art. 51) and the withholdings (anticipos) the employer or paying agent already made.
- **Child deduction sharing** (art. 49): parents who agree give it in full to one of them or split it equally; otherwise the regulation sets an order.

**Categoría I, capital income.**

- **Real-estate rents** (T7 arts. 15, 16): gross rent accrued minus bad debts, the agency commission, the fees for drawing up or renewing the lease and their IVA, Contribución Inmobiliaria and Impuesto de Enseñanza Primaria. A sub-landlord also deducts the rent paid. Leases under 12 months take the property taxes pro rata.
- **Movable capital** (art. 18): interest on deposits and loans, rent of movables and intangibles, royalties, image rights, trust distributions, and profits withdrawn by owners of sole-trader businesses under IRAE for years from 2017. Taxable dividends are those paid out of IRAE-taxed income (art. 38 C).
- **Capital gains** (arts. 26 to 34): sale price minus the UI-indexed cost, with the 15% and 20% options above. Losses offset only gains, and only if provable (art. 34).
- **Exempt** (art. 38) include public debt interest and gains, exchange differences, inflation adjustments, dividends from listed companies and from profits not taxed by IRAE, the small-disposal, rental and home-sale exemptions in the table, and transfers of shares into a resident holding company that the seller keeps owning at least 95% of for four years (art. 38 Q).
- **Foreign capital income from 1 January 2026** (arts. 6(2), 21, 25, 32; Decreto 95/026). Taxed at 12%. Income earned through a non-resident entity (or a resident entity listed in T4 art. 12 A 1 to 8) is imputed directly to a resident individual who is its beneficial owner, with a 5% minimum holding (art. 21). Foreign tax paid on the same income is a credit, capped at the Uruguayan tax on it (art. 25). For listed securities held at 31 December 2025, the cost is their quoted value on that date (art. 32). Foreign property gains may use 15% of the price, other foreign assets 20% of the price, as an annual option (arts. 29, 32). The DGI collects this income on form 1146.
- **Impatriates** (arts. 24, 24 bis). People who become resident from 1 January 2026 may opt to pay IRNR instead of IRPF on foreign capital income in the year of arrival and the next ten years. They qualify through one of three routes: property investment over UI 12,500,000, capitalising investment funds with at least UI 625,000 a year, or staying more than 183 days in each year. They must not have been resident in the two previous years. Afterwards they may pay IRPF at half the rate for five years, or a fixed annual amount of UI 1,875,000 (UI 1,250,000 in years with more than 183 days' stay). Other residents may elect the same fixed UI 1,875,000 under art. 39 bis. These are elections; refer the client before relying on one.

## Deadlines and filing

| Step | What and where | Source |
|---|---|---|
| Who must file | Employees with more than one employer, or who exceeded the annual threshold and had no December income, or who exceeded the mínimo no imponible with several simultaneous payers without form 3100, or who took the 5% family-unit reduction in withholding. For 2025 income the thresholds were UYU 963,510 nominal and UYU 552,384. Also all independent workers not under IRAE, and anyone with capital income that was not withheld. Most employees do not file | [DGI, obligados](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/estan-obligados-presentar-declaracion-irpf) |
| Forms | 1102 individual, 1103 family unit (Categoría II); 1101 capital income (Categoría I); independent workers also file 1302 (IVA servicios personales) | same |
| Portal | DGI Servicios en Línea or the DGI app, signed in with a digital identity; the return comes pre-filled; a third party can file through Asignación de roles | [DGI, calendario campaña 2026](https://www.gub.uy/direccion-general-impositiva/comunicacion/noticias/calendario-campana-2026-irpf) |
| Filing window, 2025 income | 29 June to 31 August 2026 (pre-filled form from 26 June). Refunds paid from 28 July 2026; a return filed by the 15th is paid within that month | same |
| Payment of the balance, 2025 income | Five equal instalments: 31 August, 30 September, 30 October, 30 November and 30 December 2026. Tax codes 101 (Cat. I), 109 (Cat. II), 117 (family unit); month charged December 2025; boleto 2908 at Abitab, Red Pagos or online banking | [DGI, saldo a pagar](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/declaracion-irpf-surge-saldo-pagar-se-efectua-pago-del-saldo) |
| Foreign income payments on account | Half-yearly: January to June paid in August, July to December paid in February of the next year | [Res. DGI 1517/026, num. 21, 22](https://www.impo.com.uy/bases/resoluciones-dgi/1517-2026) |
| 2026 income | Return due in the 2027 campaign; the DGI has not yet published that calendar | not yet published |

## Penalties and interest

- **Late filing.** Fixed fine of UYU 910 per return in 2026 (Res. DGI 97/026), within the contravención range of UYU 680 to UYU 13,220 set for 2026 by [Decreto 344/025](https://www.impo.com.uy/bases/decretos/344-2025) under Código Tributario art. 95. It applies even if no tax is due.
- **Late payment** (Código Tributario art. 94). Fine of 5%, 10% or 20% of the tax paid late depending on the delay, plus a monthly surcharge calculated day by day at the rate the Executive sets. Asking for a payment plan within the payment term costs 10%.

## Cross-border points

- **Non-residents** pay IRNR, not IRPF. The IRNR option for employment income of foreign free-zone workers and incoming IT professionals (art. 43) applies to IT contracts started up to 28 February 2025 only.
- **Residents with foreign capital income** are taxed from 1 January 2026, with the foreign tax credit and imputation rules above.
- **Uruguayan-source by rule** (art. 6): pay from the Uruguayan State to officials posted abroad; employment services performed abroad for IRAE or IRPF taxpayers; technical and advertising services from abroad to IRAE taxpayers.

## Two worked examples that recompute

### Example 1: employee with one child and rental income

Lucía is resident and employed all of 2026. Her salary, without aguinaldo and salario vacacional, is UYU 1,200,000; aguinaldo and salario vacacional together are UYU 100,000. Her payslips show UYU 180,000 of BPS pension contributions and UYU 54,000 of FONASA and FRL. She has one child aged 8. She also rents out a flat for UYU 300,000 a year and pays UYU 20,000 of Contribución Inmobiliaria on it.

Categoría II. UYU 1,200,000 is in the 15% band: 24,710.40 on the 10% band plus 15% of (1,200,000 - 823,680) = 56,448, so UYU 81,158.40. The highest band reached is 15%, so aguinaldo and salario vacacional pay 15%: UYU 15,000. Deductions are 180,000 + 54,000 + 137,280 (20 BPC for the child) = UYU 371,280. Her nominal income without aguinaldo is under 180 BPC (UYU 1,235,520), so the rate is 14%: credit UYU 51,979.20. Categoría II tax: 81,158.40 + 15,000 - 51,979.20 = UYU 44,179.20, before her employer's withholdings.

Categoría I. Her rents exceed 40 BPC, so the exemption does not apply. The base is 300,000 - 20,000 = UYU 280,000; at 12% the tax is UYU 33,600, taxed separately, on form 1101 if not withheld.

```oa-check
name: UY IRPF 2026, employee, one child, rental income
inputs:
  bpc: 6864
  salary: 1200000
  aguinaldo_vacacional: 100000
  bps_contributions: 180000
  fonasa_frl: 54000
  children: 1
  rent: 300000
  property_tax: 20000
steps:
  - edge_84: 84 * bpc
  - edge_120: 120 * bpc
  - edge_180: 180 * bpc
  - band_10: (min(salary, edge_120) - edge_84) * 0.10
  - band_15: (min(salary, edge_180) - edge_120) * 0.15
  - scale_tax: band_10 + band_15
  - sac_tax: aguinaldo_vacacional * 0.15
  - deductions: bps_contributions + fonasa_frl + children * 20 * bpc
  - credit: deductions * 0.14
  - cat2_tax: scale_tax + sac_tax - credit
  - rent_exempt_limit: 40 * bpc
  - cat1_tax: (rent - property_tax) * 0.12
expected:
  edge_84: 576576
  edge_120: 823680
  edge_180: 1235520
  band_10: 24710.40
  band_15: 56448.00
  scale_tax: 81158.40
  sac_tax: 15000.00
  deductions: 371280
  credit: 51979.20
  cat2_tax: 44179.20
  rent_exempt_limit: 274560
  cat1_tax: 33600.00
```

### Example 2: should the couple file as a núcleo familiar?

Martín has Categoría II renta computable of UYU 1,500,000 and his wife Ana UYU 400,000 in 2026. They are married under sociedad conyugal, both resident, and neither pays IRAE, IRNR, IMEBA or IASS. Ana's income exceeds 12 SMN, so if they opt to file jointly, scale B applies.

Filed separately (scale A): Martín pays 86,486.40 up to 180 BPC plus 24% of (1,500,000 - 1,235,520), so UYU 149,961.60; Ana is under 84 BPC and pays nothing. Total UYU 149,961.60.

Filed jointly (scale B) on UYU 1,900,000: exempt to UYU 1,153,152; 15% from there to UYU 1,235,520 = 12,355.20; 24% on the rest = 159,475.20. Total UYU 171,830.40.

The decision: filing separately saves UYU 21,868.80 before deductions, so they file separately. The joint option pays when one spouse has little or no labour income: if Ana earned nothing (scale C), joint tax on Martín's UYU 1,500,000 would be UYU 133,488, which is UYU 16,473.60 less than filing separately. If Ana earned UYU 200,000 (still under 12 SMN, scale C), joint tax on UYU 1,700,000 would be UYU 181,488, more than the UYU 149,961.60 separately. Recompute the deduction credit under each option before electing (see Not yet confirmed).

```oa-check
name: UY IRPF 2026, individual vs núcleo familiar decision
inputs:
  bpc: 6864
  martin: 1500000
  ana: 400000
  ana_low: 200000
steps:
  - e84: 84 * bpc
  - e96: 96 * bpc
  - e120: 120 * bpc
  - e144: 144 * bpc
  - e168: 168 * bpc
  - e180: 180 * bpc
  - tax_to_180: (e120 - e84) * 0.10 + (e180 - e120) * 0.15
  - martin_tax: tax_to_180 + (martin - e180) * 0.24
  - ana_tax: max(0, min(ana, e120) - e84) * 0.10
  - separate_total: martin_tax + ana_tax
  - joint_b: (e180 - e168) * 0.15 + (martin + ana - e180) * 0.24
  - saving_separate: joint_b - separate_total
  - joint_c_zero: (e144 - e96) * 0.10 + (e180 - e144) * 0.15 + (martin - e180) * 0.24
  - saving_joint_zero: separate_total - joint_c_zero
  - joint_c_low: (e144 - e96) * 0.10 + (e180 - e144) * 0.15 + (martin + ana_low - e180) * 0.24
expected:
  tax_to_180: 86486.40
  martin_tax: 149961.60
  ana_tax: 0
  separate_total: 149961.60
  joint_b: 171830.40
  saving_separate: 21868.80
  joint_c_zero: 133488.00
  saving_joint_zero: 16473.60
  joint_c_low: 181488.00
```

## Ask the client first

1. Residence in 2026: days in Uruguay, where the spouse and minor children live, any certificate of residence elsewhere. Did they become resident in 2026, or earlier under an impatriate or IRNR option?
2. Labour income: each employer and paying institution, pay by month, aguinaldo and salario vacacional separately, and any independent fees. Has an independent worker opted into IRAE?
3. Deductions: BPS (or other fund), FONASA, FRL and Fondo de Solidaridad paid; children (dates of birth, disability, which parent claims); mortgage on the only home (home cost in UI, instalments paid); rent paid and the landlord's identity.
4. Spouse or cohabitant: the marriage regime, each one's Categoría II income (12 SMN test), and whether either pays IRAE, IRNR, IMEBA or IASS. If unknown, compute individually.
5. Capital income: rents and their costs; interest by instrument, currency and term; dividends and their source; sales of property or shares with dates and costs; every foreign account, fund, company or property held from 1 January 2026, with foreign tax paid.
6. Withholdings and payments already made, including foreign-income payments on account.

## Sources

| Source | URL | Read on |
|---|---|---|
| Texto Ordenado 2023 (Decreto 101/024), Título 7 IRPF, IMPO consolidated text with Ley 20.446 integrated: arts. 1 to 52 read in full | https://www.impo.com.uy/bases/todgi-2023/7-2024 | 2026-11-11 |
| Decreto 11/026 of 20 January 2026, art. 1: BPC UYU 6,864 from 1 January 2026 | https://www.impo.com.uy/bases/decretos/11-2026 | 2026-11-11 |
| Decreto 319/025, arts. 1 and 2: salario mínimo nacional from 1 January and 1 July 2026 | https://www.impo.com.uy/bases/decretos/319-2025 | 2026-11-11 |
| Decreto 95/026 of 6 May 2026, foreign capital income regulation (arts. 1 to 18 read) | https://www.impo.com.uy/bases/decretos-originales/95-2026 | 2026-11-11 |
| Resolución DGI 1517/026, numerals 20 to 25 (payments on account, simplified regime) | https://www.impo.com.uy/bases/resoluciones-dgi/1517-2026 | 2026-11-11 |
| Resolución DGI 2294/026, numeral 7 read for the transitional fixed-amount payment for 2026 | https://www.impo.com.uy/bases/resoluciones-dgi/2294-2026 | 2026-11-11 |
| BPS ATYR, Comunicado R 5/2026, parts 1 to 4 read for the IRPF 2026 monthly values (monthly scale 7 to 115 BPC, the 14% / 8% test at 15 BPC a month, child 20 and 40 BPC): cross-check of the BPC conversions | https://www.bps.gub.uy/23860/2026---comunicado-r-5---valores-escalas-irpf-2026.html | 2026-11-11 |
| DGI, who must file the IRPF return (guide of 12 May 2026), read for the filing tests and forms | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/estan-obligados-presentar-declaracion-irpf | 2026-11-11 |
| DGI, 2026 IRPF campaign calendar (news of 1 June 2026), read for the filing window and refunds | https://www.gub.uy/direccion-general-impositiva/comunicacion/noticias/calendario-campana-2026-irpf | 2026-11-11 |
| DGI, payment of the IRPF balance (guide of 25 May 2026), read for the instalment dates and tax codes | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/declaracion-irpf-surge-saldo-pagar-se-efectua-pago-del-saldo | 2026-11-11 |
| DGI, new categories of foreign income and form 1146 (news of 24 July 2026), read in full | https://www.gub.uy/direccion-general-impositiva/comunicacion/noticias/irpf-nuevas-categorias-rentas-obtenidas-exterior-personas-fisicas-residentes | 2026-11-11 |
| Código Tributario (Decreto-Ley 14.306), arts. 94 and 95 | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 | 2026-11-11 |
| Decreto 344/025, arts. 1 and 2: contravención minimum and maximum for 2026 | https://www.impo.com.uy/bases/decretos/344-2025 | 2026-11-11 |
| Resolución DGI 97/026, numeral 1 read for the late-return fine for 2026 | https://www.impo.com.uy/bases/resoluciones-dgi/97-2026 | 2026-11-11 |

Not yet confirmed: the art. 37 A) rate for foreign-currency interest over one and up to three years (blank in the consolidated text); the monthly recargo rate for 2026; how the 180 BPC deduction-rate test and the deductions apply to a núcleo familiar return; whether a deduction credit larger than the tax is lost; which SMN figure (January or July) the 12 SMN test uses in a year with two values; the filing calendar for 2026 income (2027 campaign); monotributo and the unipersonal minimum base, which sit in BPS rules not read for this skill; the employer withholding mechanics in Decreto 148/007, left to uruguay-payroll.

> Contributed by Michael Cutajar.
