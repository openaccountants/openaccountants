---
name: argentina-payroll
description: >
  Use this Guide for Argentine employee income-tax withholding in fiscal year
  2026: Ganancias cuarta categoria, relacion de dependencia, retenciones de
  sueldos, SiRADIG, F.572 Web and F.1359. It covers the withholding agent,
  cumulative computation, SAC, personal deductions, multiple employers,
  annual and final settlements, the ordinary withholding ceiling, reporting
  fields and refunds. It distinguishes January-June and July-December payroll
  tables from the annual settlement tables. It prepares working papers for a
  local professional to review. It does not calculate labour-law entitlements,
  employer social contributions, pensioner special deductions, executive
  termination packages or non-resident withholding.
version: 0.2
jurisdiction: AR
category: payroll
domain: tax
type: computation
tax_year: 2026
last_updated: 2026-11-11
tier: 2
---

# Argentina: payroll income-tax withholding 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Resident employees paid income within RG 4003 art. 1 and LIG art. 82(b). This Guide is **Not yet approved**. It produces a computation and reporting reconciliation, not an authorised filing. Currency is ARS and the coverage is calendar year 2026. RG 4003 also covers other fourth-category recipients; the pension-specific computation and actors' separate regime are outside this employee Guide.

**Quick answer:** use cumulative taxable remuneration and the table for the payment month. Deduct eligible expenses and personal deductions, apply the cumulative scale, then reconcile previous withholdings, refunds and permitted credits. The annual calculation uses different published parameters. Establish the payment date, settlement type, all employers, deductions and prior withholding before computing anything (RG 4003 arts. 3, 5, 7, 11 and 21; source below).

If several employers pay taxable income, only the largest payer acts as withholding agent. At a new employment relationship compare current payments; at the start of the fiscal year compare the prior year's payments. Exempt-only payers do not enter that selection. The employee reports other employment through SiRADIG (RG 4003 arts. 3 and 11).

**Out of scope:** gross-to-net labour entitlements, provincial payroll taxes, pension-specific and mixed self-employment deductions, executive severance, Tierra del Fuego and oilfield exemptions, expatriate equalisation and treaty exemptions. Route self-employed income to [argentina-income-tax](argentina-income-tax.md), autónomo contributions to [ar-social-contributions](ar-social-contributions.md), and residence/non-resident income to [argentina-cross-border](argentina-cross-border.md). Do not apply employee deductions to an autónomo.

## Rates, bands and thresholds

### Select the correct 2026 table

| Payment or settlement | Rule and condition | Official source |
|---|---|---|
| January-June ordinary payments | Use the payment month's accumulated columns in the first-semester deduction and scale PDFs. The first annualised GNI is 5,151,802.50, not a monthly allowance | RG 4003 art. 7(a); https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-ene-a-jun-2026.pdf |
| July-December ordinary payments | Use the payment month's columns in the second-semester PDFs. December cumulative GNI is 5,585,736.93. These blend the first-semester amounts with the updated second-semester amounts | RG 4003 art. 7(b); https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-jul-dic-2026.pdf |
| Annual settlement | Use the full annual amounts updated from July, including GNI 6,019,671.36; refund excess withholding where applicable | RG 4003 art. 7(c); https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |
| Final settlement | Annual parameters effective at the payment: first-semester annualised table for final settlement and payment in that semester; July-updated annual table for second-semester termination and/or instalment payment | RG 4003 art. 21(b); https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02 |
| Ordinary withholding limit | 35% of the gross remuneration for that payment. Annual/final settlement disregards the ceiling unless the beneficiary requests it by note | RG 4003 art. 7; LIG art. 94 maximum rate; https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02 |

The scale PDFs with every payment month's cumulative bands are [January-June](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-per-ene-a-jun-2026.pdf) and [July-December](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-per-jul-a-dic-2026.pdf). Read the month headed **MES DE PAGO**; do not divide the annual table to reconstruct rounded monthly figures.

### Annual settlement: personal deductions

Amounts below are the annual/final July-updated table, subject to eligibility. They are not the December ordinary payroll table.

| Deduction | ARS, annual 2026 | Conditions and official source |
|---|---|---|
| Ganancia no imponible | 6,019,671.36 | Resident individual, LIG art. 30(a); https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |
| Spouse or qualifying cohabiting partner | 5,669,323.06 | Resident, dependent, net annual income no greater than GNI, relationship substantiated under art. 30(b); https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |
| Child or stepchild | 2,859,060.31 | Under 18, resident, dependent, income test met; closest qualifying relative; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |
| Child or stepchild incapacitated for work | 5,718,120.60 | No age restriction; other dependency conditions apply; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |
| Employee deducción especial, art. 30(c)(2) | 28,894,422.56 | Eligible art. 82(a)-(c) income, subject to the statutory exclusions; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |
| Additional special deduction | One twelfth of eligible GNI + family deductions + employee special deduction | Art. 30 and RG 4003 Annex II E; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf |

Family deductions also require residence and dependency. When both parents exercise parental responsibility and have taxable income, they may split the child deduction equally or one may take it all; never let both take the whole deduction (RG 4003 Annex II E). For art. 30 deductions, LIG art. 33 treats an individual living in Argentina for more than six months in the fiscal year as resident; this deduction test is distinct from general tax residence. Apply acquisition/cessation and partial-year facts under LIG art. 31, not an automatic full-year assumption. These rules and the income test come from [LIG arts. 30-33](https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05).

### Annual settlement: article 94 scale

Tax = fixed amount + (net taxable remuneration - lower band limit) × rate. These are ARCA's printed values; do not recompute the fixed amounts from rounded band widths.

| Over ARS | Up to ARS | Fixed ARS | Marginal rate | Official source |
|---|---|---|---|---|
| 0.00 | 2,336,953.69 | 0.00 | 5% | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-liquidacion-anual-y-final-2026.pdf |
| 2,336,953.69 | 4,673,907.36 | 116,847.68 | 9% | same |
| 4,673,907.36 | 7,010,861.05 | 327,173.52 | 12% | same |
| 7,010,861.05 | 10,516,291.59 | 607,607.96 | 15% | same |
| 10,516,291.59 | 21,032,583.18 | 1,133,422.54 | 19% | same |
| 21,032,583.18 | 31,548,874.77 | 3,131,517.94 | 23% | same |
| 31,548,874.77 | 47,323,312.16 | 5,550,265.01 | 27% | same |
| 47,323,312.16 | 70,984,968.25 | 9,809,363.10 | 31% | same |
| 70,984,968.25 | No upper limit | 17,144,476.49 | 35% | same |

## The base

Follow [RG 4003 Annex II, current text under RG 5683/2025](https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02), in this order:

1. Identify cash and non-cash remuneration paid, including other employers' reported taxable remuneration. Non-cash payments use current market value or, failing that, employer acquisition cost. Do not infer income-tax exemption from a labour-law description of a payment as non-remunerative.
2. Separate statutory exclusions in Annex II A: family allowances, specified termination compensation, death/disability compensation, documented indispensable training, and exclusively workplace clothing/equipment, among the listed cases. Stop and refer special territorial, industry and executive termination cases.
3. Allocate non-habitual pay under Annex II B across payment month and remaining months. Below 20% of habitual gross pay this allocation is optional. Do not spread ordinary variable sales commissions, amounts in a final settlement, or amounts whose spreading would make withholding impossible under the stated limitations. If a month has no payment, accumulate its deferred slice into the next paid month in that fiscal year; if no further payment occurs, include it at annual settlement. A final settlement also includes all prior deferred slices.
4. Add a twelfth of the relevant monthly gross amounts for SAC and deduct a twelfth of related deductible contributions under Annex II C. Choose and document one permitted reconciliation: replace twelfths with actual SAC and deductions when instalments are paid, or reconcile actual SAC at annual/final settlement. Do not count actual SAC and unreversed twelfths together.
5. Deduct eligible Annex II D expenses with evidence: mandatory retirement and health deductions, union dues and other mandatory discounts; permitted voluntary health cover, donations, rent, domestic staff, education, mortgage interest, insurance and retirement plans subject to their individual conditions. Mandatory contributions attributable to exempt income must be allocated out. The general deduction for insurance under D(d), medical fees under D(j) and retirement plans under D(p) is annual/final only. Indexed insurance caps are not reproduced here.
6. Accumulate the net remuneration for the fiscal year. Subtract eligible cumulative personal deductions including the additional twelfth, using the correct month or settlement table. Floor the taxable base at zero.
7. Apply the selected cumulative scale. Deduct permitted Annex II G credits only at annual/final settlement, then net previous withholdings/autorretenciones under H, accounting for refunds already made. Do not take Annex II G credits in an ordinary monthly calculation. Record a positive result as withholding and a negative result as refund, subject to the ordinary ceiling and the special settlement rules.

### Common general deductions: conditions before computing

These are Annex II D rules, not extra personal allowances. For the 5% caps, use net remuneration after the other admissible general deductions but before the three capped deductions (voluntary health cover, donations and medical fees), prior losses and art. 30 personal deductions; do not apply a percentage to gross salary.

| Claim | Limit and eligibility | Official source |
|---|---|---|
| Voluntary medical cover | Up to 5% of the specified cumulative net income, for employee and qualifying dependants; distinguish compulsory health discounts | RG 4003 Annex II D(c); https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02 |
| Donations | Up to 5% of the specified cumulative net income; only qualifying public bodies and exempt institutions; excess within the year can carry into later payroll calculations | Annex II D(g), same |
| Tenant's housing rent | 40% of invoiced rent, capped at GNI; taxpayer must own no property, even partly | Annex II D(h), same |
| Additional housing-rent deduction | 10% of monthly rent, with invoice and contract registered in RELI; can supplement D(h) where eligible; also available to a taxable landlord. Only the landlord deduction is excluded for exempt 2026 housing rent under LIG art. 26(n) and the unnumbered article after Decreto 862 art. 204; the tenant can remain eligible | Annex II D(s), same |
| Medical/paramedical fees | 40% of invoiced eligible services, capped at 5% of the specified annual net income; annual/final only | Annex II D(j), same |
| Domestic staff | Documented remuneration, employer contributions and mandatory work-risk insurance for staff under Ley 26.844, capped at GNI | Annex II D(m), same |
| Education/tools | Cap 40% of GNI; qualifying dependent children or children up to 24 inclusive who study regularly/professionally, cannot support themselves and meet the GNI net-income test; documented and entered in SiRADIG | Annex II D(r), same |
| Mortgage interest on own home | Up to ARS 20,000 annually for a qualifying purchase/construction mortgage; a co-owner is limited to their ownership share of that cap | LIG art. 85(a); https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Insurance/retirement, funeral costs | Apply the relevant statutory/annual cap before any claim; caps are not confirmed here, so stop these claim lines until read from the current official source | Annex II D(d),(e),(p); https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02 |

For rent accruing from 1 January 2026, current Decreto 862 art. 83 defines the qualifying individual/estate landlord exemption where the property is the tenant's unique family permanent home; LIG art. 26(n) and the unnumbered article after Decreto 862 art. 204 exclude the landlord's art. 85(k) deduction for that exempt income. Source: https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 . Do not apply a landlord deduction against exempt rent.

Do not confuse eligibility for education costs for a student over 18 with entitlement to the ordinary child personal deduction. Do not deduct unsupported expenditure merely because the payroll software offers a field.

**Exception table**

| Fact | Treatment | Source |
|---|---|---|
| Another employer becomes largest payer | Informative settlement by the old agent; new agent uses transferred year-to-date data | RG 4003 arts. 3, 11, 21(c), official RG link above |
| Employment ends, no replacement withholding agent | Final settlement using annual parameters effective at payment | RG 4003 art. 21(b), same |
| Employment ends but another taxable employer remains | Informative settlement with cumulative monthly parameters | RG 4003 art. 21(c), same |
| Termination paid in instalments within the same fiscal year | Calculate withholding/refund on the total taxable termination amounts and collect/refund proportionally with each instalment | RG 4003 art. 21(b), same |
| Termination paid in instalments across fiscal years | Defer final settlement until the last instalment; meanwhile follow art. 7 withholding. Refer the schedule rather than settling the whole amount in the first year | RG 4003 art. 21(b), same |
| Treaty or non-resident status asserted | Resolve residence and treaty before using resident payroll computation | RG 4003 art. 1, same |

## Deadlines and filing

Ordinary withholding occurs at each payment (RG 4003 art. 5). Obtain employee F.572 Web data through **SiRADIG - EMPLEADOR**, reconcile it to payroll, and retain the documents. Employees supply updates through **SiRADIG - TRABAJADOR**; the ordinary annual information cutoff is 31 March of the following year under art. 11. Employers communicate the art. 11/14 obligations within 30 calendar days of employment starting, retain the signed acknowledgement, and tell employees the monthly payroll cutoff (art. 19). Source: [RG 4003 arts. 11 and 19](https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02).

The ordinary annual settlement is made by the last business day of April following the fiscal year; collect/refund its balance on the first payment after settlement or subsequent payments if needed, up to the last business day of May. If departure or agent change intervenes, combine the prior annual settlement with the applicable final/informative settlement (RG 4003 art. 21; exceptional extensions must be checked for the settlement year).

Upload the annual/final/informative file through **Presentación de DDJJ y Pagos**. Annual electronic submission is mandatory if annual gross income, including exempt/non-taxable income, reaches the sum of the applicable GNI and employee special deduction, or if tax was not fully withheld. For other recipients who suffered withholding, the employer may upload or deliver the prescribed copy and retain a duplicate. Final/informative electronic files are due within five business days after the settlement (RG 4003 art. 22).

Use the [2026 F.1359 version 2 manual](https://www.arca.gob.ar/572web/documentos/F1359-Version-00200-Manual-001-a%C3%B1o2026.pdf), not an older F.1357 layout. It identifies remuneration in records 03/04, general deductions in 05, personal deductions in 06, payments on account in 07 and computation in 08. In record 06, field 12 is employee special deduction, field 13 the additional twelfth and field 15 total art. 30 deductions. Record 08 field 3 is taxable remuneration, field 5 determined tax, field 6 withholding, field 8 self-withholding and field 9 final balance. Cross-check the manual's field formulas. After upload retain the acknowledgement, check subsequent consistency notices and rectify errors. F.1359 is made available to the employee through SiRADIG.

Report and deposit payroll withholding under **SICORE**, RG 2233, as required by RG 4003 art. 24; F.931 social-security filing does not replace this. Where withholding is incomplete, art. 23 requires the May SICORE entry under **Detalle de Retenciones**, **Recibo de Sueldo**, number zero, and **Imposibilidad de Retención**. Current CUIT-specific deposit dates and SICORE payment codes are not confirmed in this Guide; obtain the official calendar before payment.

**Unrecovered withholding and employee payment:** under RG 4003 art. 13, incomplete withholding normally brings annual assessment/payment and, where necessary, registration. If the employer determines the tax and makes F.1359 available, the employee may instead pay the reported shortfall by VEP through **Presentación de DDJJ y Pagos**, Clave Fiscal level 2 or above, tax 11 / concept 708 / subconcept 708. Pay by the ordinary individual income-tax payment deadline and report payment through SiRADIG. The same mechanism permits payment of a current-year amount reported unwithheld on a payslip. Meeting this alternative's conditions removes the registration/annual assessment obligation arising from that shortfall; it does not exempt unrelated income. Keep the VEP receipt and reconcile the employer's balance.

**Arrears:** RG 4003 art. 9 separates current-year adjustments from earlier-year amounts. Current-year adjustments enter the current agent's calculation using other-payer data where relevant. LIG art. 24(b) permits prior-year attribution for the specified retroactive causes: collective agreement, statute or pay-scale amendment, judgment, admission of the claim or competent administrative appeal resolution. The election waives any accrued limitation defence. It is not an election for every late salary payment. For that qualifying election, an employer that was the original withholding agent rectifies its own historic calculation by adding the adjustment. If a different agent acted in that period, the payer applies that historic period's rules using the original agent's certificate supplied by the employee. Only if the original agent ceased activities may the specified F.572/F.572 Web or historic system information and withholding documents substitute. Without those required documents the latter election procedure is unavailable. Do not silently apply the 2026 scale. Without that election, apply the perception-period treatment and art. 9 procedure. Obtain professional review before restating a prior settlement.

## Penalties and interest

[RG 4003 art. 25](https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02) refers breaches to Ley 11.683 and, where applicable, the criminal tax regime. Declaration content is the declarant's responsibility. This Guide does not supply a fixed penalty or interest percentage: current penalty amounts, the offence classification, interest periods and any criminal threshold need a separate current-law check before assessment. Do not treat the withholding ceiling as permission to leave a balance unreported.

## Cross-border points

RG 4003 art. 1 distinguishes residents from foreign beneficiaries. Apply [argentina-cross-border](argentina-cross-border.md) to residence, foreign work locations and treaties. Do not use days abroad alone to conclude that Argentine residence ended. Employee income and foreign income may require an individual return beyond payroll; the payroll settlement does not certify that all income has been taxed. Foreign secondments and tax borne by an employer require separate review; RG 4003 art. 8 refers gross-up to the implementing regulation.

## Two worked examples that recompute

### 1. Annual settlement with one employee, no dependants

Assume a full-year resident employee, ordinary employee deductions, ARS 45,000,000 taxable gross including actual SAC after reversing estimated twelfths, and ARS 5,000,000 properly substantiated general deductions. There are no other deductions, credits, other employers or previous refunds. Annual personal deductions are GNI 6,019,671.36 + employee special deduction 28,894,422.56 + their twelfth 2,909,507.83 = 37,823,601.75. Taxable remuneration is 2,176,398.25, wholly within the first annual band. Determined tax is 108,819.91. Previous withholding 100,000 leaves 8,819.91 to collect. Sources: annual PDFs above and F.1359 record 08.

```oa-check
name: Annual employee settlement 2026
inputs:
  taxable_gross: 45000000
  general_deductions: 5000000
  gni: 6019671.36
  employee_special: 28894422.56
  previously_withheld: 100000
steps:
  - additional_twelfth: round((gni + employee_special) / 12, 2)
  - personal: gni + employee_special + additional_twelfth
  - taxable_base: max(0, taxable_gross - general_deductions - personal)
  - determined_tax: round(taxable_base * 0.05, 2)
  - balance: determined_tax - previously_withheld
expected:
  additional_twelfth: 2909507.83
  taxable_base: 2176398.25
  determined_tax: 108819.91
  balance: 8819.91
```

### 2. Withholding ceiling: ordinary payment or annual settlement?

Assume the correct cumulative calculation already gives ARS 900,000 additional tax, and the current gross payment is ARS 2,000,000. For an ordinary payment, the ceiling is 700,000, leaving 200,000 unrecovered. If this is an annual/final settlement, collect 900,000 unless the employee supplies the art. 7 note requesting the ceiling. With that note, collect 700,000 and track/report the unrecovered balance. These are alternative legal classifications, not an employer election. The example isolates the ceiling after the scale calculation; all figures except the sourced 35% ceiling are assumed inputs.

```oa-check
name: Ordinary versus annual withholding ceiling
inputs:
  current_gross: 2000000
  calculated_balance: 900000
steps:
  - ceiling: current_gross * 0.35
  - ordinary_withheld: min(calculated_balance, ceiling)
  - ordinary_unrecovered: calculated_balance - ordinary_withheld
  - annual_without_note: calculated_balance
  - annual_with_note: min(calculated_balance, ceiling)
expected:
  ceiling: 700000
  ordinary_withheld: 700000
  ordinary_unrecovered: 200000
  annual_without_note: 900000
  annual_with_note: 700000
```

## Ask the client first

1. Payment dates and whether each calculation is ordinary, annual, final or informative; any instalments or agent change.
2. Tax residence, work locations and any treaty claim or special territorial/industry status.
3. All employers' remuneration, SAC, benefits in kind, cumulative withholding, refunds and self-withholding.
4. F.572 Web and evidence for family status, dependants' residence/income, deduction sharing and changes during the year.
5. Evidence for general deductions and credits, distinguishing monthly from annual-only items.
6. Any written withholding-ceiling request, uncollected tax, prior F.1359 and filing/payment acknowledgements.

## Sources

Read on means the specified text was extracted and read, not merely that its URL responded. Original PDFs were cached outside git.

| Source and text read | Official URL | Read on |
|---|---|---|
| Read for RG 4003 consolidated, arts. 1-13, 19, 21-25 and current Annex II A-H; quotation: "en el segundo semestre del año fiscal: acumulados mensualmente en ese período semestral" | https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02 | 2026-11-11 |
| Read for Decreto 862 art. 83 and unnumbered article after art. 204, qualifying 2026 housing-rent exemption and landlord deduction exclusion; quotation: "única, familiar y de ocupación permanente" | https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 | 2026-11-11 |
| Read for LIG arts. 24, 30-33 and 85(a), arrears, family and employee eligibility, mortgage cap; quotation: "se añadirá como deducción especial la doceava parte" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for ARCA first-semester 2026 deductions, title and monthly/annualised tables; quotation: "5.151.802,50" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-ene-a-jun-2026.pdf | 2026-11-11 |
| Read for ARCA second-semester 2026 deductions, title and cumulative table; quotation: "5.585.736,93" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-jul-dic-2026.pdf | 2026-11-11 |
| Read for ARCA annual 2026 deductions, whole one-page table; quotations: "6.019.671,36", "28.894.422,56" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/deducciones/documentos/Deducciones-personales-art-30-liq-anual-2026.pdf | 2026-11-11 |
| Read for ARCA annual/final 2026 scale, all nine rows and scope note; quotation: "liquidación final y anual" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-liquidacion-anual-y-final-2026.pdf | 2026-11-11 |
| Read for ARCA first-semester 2026 scale, title and monthly table layout; quotation: "MES DE PAGO" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-per-ene-a-jun-2026.pdf | 2026-11-11 |
| Read for ARCA second-semester 2026 scale, title and monthly table layout; quotation: "MES DE PAGO" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-humanas-sucesiones-indivisas/declaracion-jurada/documentos/Tabla-Art-94-LIG-per-jul-a-dic-2026.pdf | 2026-11-11 |
| Read for ARCA F.1359 v2 manual for 2026, record index, sections 4.6, 4.8 and 5; quotation: "Si el archivo remitido ingresa correctamente, el sistema emitirá un Acuse de Recibo" | https://www.arca.gob.ar/572web/documentos/F1359-Version-00200-Manual-001-a%C3%B1o2026.pdf | 2026-11-11 |

Not yet confirmed: current SICORE deposit calendar and payment codes; 2026 indexed insurance/retirement and funeral-cost deduction caps; current penalty amounts and interest rates; exceptional extensions applicable to settlements made in 2027. Special pension, executive, territorial and industry computations are out of scope.
