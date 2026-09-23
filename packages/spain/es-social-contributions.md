---
name: es-social-contributions
description: Use this skill whenever asked about Spanish self-employed social contributions (cuota de autonomos / RETA). Trigger on phrases like "cuota autonomos", "RETA", "social contributions Spain", "autónomo contributions", "how much do I pay as autonomo", "tarifa plana", "cese de actividad", "regularizacion cuotas", "base de cotización", "TGSS direct debit", "cuota mensual", or any question about Spanish self-employed social security. Also trigger when classifying bank statement transactions showing TGSS direct debits, cuota autonomos debits, or Seguridad Social payments. ALWAYS read this skill before touching any Spanish social contributions work.
version: 2.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spanish self-employed social contributions (RETA)

Contributions to the Spanish regime for self-employed workers (RETA): the income bands that fix the monthly base, the rates, the yearly regularisation, and the IRPF deduction. Figures are for tax year 2026, from Orden PJC/297/2026, which applies them "desde el 1 de enero de 2026". There is no 2026 Budget Law. Two things carry another year, marked where used: the reduced starting fee in Rule 5 has a legal amount for 2023 to 2025 only, and the sick pay percentages in Section 10 come from the general Social Security page on temporary incapacity.

## Section 1: Quick reference

| Field | Value |
| --- | --- |
| Country | Spain |
| Regime | RETA, the special regime for self-employed workers |
| Primary legislation | Ley General de la Seguridad Social (RDLeg 8/2015); Real Decreto-ley 13/2022; Ley 20/2007 (article 38 ter) |
| Rules for this year | Orden PJC/297/2026 |
| Collecting body | Tesoreria General de la Seguridad Social (TGSS) |
| Currency | EUR only |
| Payment | Monthly, direct debit, last working day of the month |
| Contributor | Open Accountants |
| Validated by | Pending. Requires sign-off by a qualified asesor fiscal |
| Validation date | Pending |

**Read this section before computing or classifying anything.**

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown persona fisica vs societario | Ask. Minimum base rules differ. Rule 6 |
| Unknown net income estimate | STOP. An estimate is needed to pick a band |
| Unknown whether first-time autonomo | Ask. Reduced fee eligibility. Rule 5 |
| Unknown generic deduction | Ask which case in article 305.2 applies |

### Required inputs

**Minimum viable.** The case in article 305.2, the expected monthly average of annual net income, and whether this is a first registration.

**Recommended.** Bank statements with TGSS debits, date of alta, prior RETA history, the IRPF declaration.

**Ideal.** Full IRPF data, the Informe de bases de cotizacion, the alta and baja history.

### Refusal catalogue

- **R-ES-SC-1. Disability regimes.** A disability affecting contribution rules: "This needs a case-specific TGSS assessment. Escalate."
- **R-ES-SC-2. Cross-border posted workers.** Posted from another EU country: "EU social security coordination applies. Escalate."
- **R-ES-SC-3. Mutuas MATEPSS specifics.** A Mutua's own benefits or cover: "Out of scope. Contact the relevant Mutua."

## Section 3: Payment pattern library

### 3.1 TGSS direct debits (monthly cuota)

| Pattern | Treatment |
| --- | --- |
| TGSS, TESORERIA GENERAL | EXCLUDE. RETA cuota |
| SEGURIDAD SOCIAL, SS | EXCLUDE. RETA cuota |
| CUOTA AUTONOMOS | EXCLUDE. RETA cuota |
| RETA, REG ESP TRAB AUTONOMOS | EXCLUDE. RETA cuota |
| DOMICILIACION TGSS | EXCLUDE. RETA cuota |

### 3.2 Regularisation payments (TGSS demands additional cuotas)

| Pattern | Treatment |
| --- | --- |
| TGSS REGULARIZACION | EXCLUDE. RETA regularisation, Rule 9 |
| TGSS COMPLEMENTO | EXCLUDE. Adjustment to the provisional base |

### 3.3 TGSS refunds (overpayment)

| Pattern | Treatment |
| --- | --- |
| TGSS DEVOLUCION | EXCLUDE. Refund of excess cuotas, Rule 9 |
| TGSS REINTEGRO | EXCLUDE. Same, and the pluriactividad refund, T2-1 |

### 3.4 Tarifa plana payments

| Pattern | Treatment |
| --- | --- |
| TGSS debit identical each month, far below any band cuota | EXCLUDE. Reduced starting fee. Do not assume an amount: read the TGSS award, Rule 5 |

### 3.5 Tax authority (NOT RETA)

| Pattern | Treatment |
| --- | --- |
| AEAT, AGENCIA TRIBUTARIA | EXCLUDE. Income tax or VAT, not social contributions |
| HACIENDA | EXCLUDE. Tax, not RETA |
| IVA, IRPF (tax reference) | EXCLUDE. Tax, not RETA |

### 3.6 Employee social security (employer obligations)

| Pattern | Treatment |
| --- | --- |
| TGSS REGIMEN GENERAL | EXCLUDE. Employer's duty for staff, not the autonomo's RETA. Section 10 |
| TC1, TC2 (payroll references) | EXCLUDE. Employer payroll obligations |

## Section 4: Worked examples

Amounts are blank: the cuota depends on the base chosen.

### Example 1: Standard monthly RETA cuota (TGSS direct debit)

`30.04.2026 ; TGSS TESORERIA GENERAL ; ADEUDO ; CUOTA AUTONOMOS ABRIL ; -[amount] ; EUR`

Pattern 3.1: the chosen base with each Rule 3 rate applied. EXCLUDE, deductible.

### Example 2: Tarifa plana cuota (new autonomo)

`31.03.2026 ; TGSS ; ADEUDO ; CUOTA TARIFA PLANA MARZO ; -[amount] ; EUR`

Pattern 3.1: a fixed fee instead of base times rate. Do not assume the amount, Rule 5. EXCLUDE, deductible.

### Example 3: Regularisation demand from TGSS

`25.09.2026 ; TGSS REGULARIZACION ; ADEUDO ; COMPLEMENTO CUOTAS ; -[amount] ; EUR`

Pattern 3.2: the final base exceeded the provisional one, Rule 9. EXCLUDE, a higher deductible expense of the year paid, Rule 10.

### Example 4: TGSS refund (overpaid cuotas)

`15.10.2026 ; TGSS DEVOLUCION ; ABONO ; DEVOLUCION CUOTAS ; +[amount] ; EUR`

Pattern 3.3: the final base was below the provisional one. EXCLUDE from VAT; for IRPF it is not simply income, Rule 10.

### Example 5: AEAT tax payment (NOT RETA)

`20.04.2026 ; AGENCIA TRIBUTARIA ; ADEUDO ; PAGO FRACCIONADO IRPF ; -[amount] ; EUR`

Pattern 3.5: a quarterly IRPF instalment. EXCLUDE, income tax.

### Example 6: Employer TGSS payment (not autonomo's own RETA)

`30.04.2026 ; TGSS REGIMEN GENERAL ; ADEUDO ; SS EMPLEADOS ; -[amount] ; EUR`

Pattern 3.6: employer social security for staff, not the autonomo's cuota. EXCLUDE.

### Rule 1: Net income formula for tranche determination

Article 308.1.c. Computable income is the net income of every economic activity under the IRPF rules; under direct estimation, that income increased by the owner's own social security cuotas and payments to alternative mutual societies. Where the activity uses the module method, the computable income is the prior net income, reduced for farming, forestry and livestock and unreduced otherwise. For a person under article 305.2.b the whole of the income from holdings in the company and the work income from it is counted as well. The deduction below is then applied and the result divided into months. Ninety days registered in the period regularised is enough for the lower rate.

**Generic expenses deduction**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| Ordinary self-employed | 7% | "gastos genéricos del 7 por ciento" |
| Cases in article 305.2 b) and e) | 3% | "la deducción será del 3 por ciento" |

### Rule 2: Tranche table, 15 bands, tax year 2026

The bands are numbered as the order numbers them, each table from one. The 2025 edition of this Guide numbered the general table from four, so a band number taken from an older working paper must be re-read against the table below.

The reduced table applies when the monthly average is expected to fall below the lowest income in the general table. The law sets that floor as the general regime minimum contribution base, but the order fixes the 2026 tables at the figure in the table below, which is not the group 7 minimum in Rule 6. Use the table, not the general regime minimum. Every minimum base is unchanged from 2025; only the top two general maximum bases moved, to the new ceiling.

**Reduced table (bands 1 to 3), 2026**

| Band, by monthly net income in EUR | Minimum base | Maximum base |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| 1: 670 or less | EUR 653.59 | EUR 718.94 |
| 2: over 670 to 900 | EUR 718.95 | EUR 900.00 |
| 3: over 900, below 1,166.70 | EUR 849.67 | EUR 1,166.70 |

**General table (bands 1 to 12), 2026**

| Band, by monthly net income in EUR | Minimum base | Maximum base |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| 1: 1,166.70 or more, to 1,300.00 | EUR 950.98 | EUR 1,300.00 |
| 2: over 1,300.00 to 1,500.00 | EUR 960.78 | EUR 1,500.00 |
| 3: over 1,500.00 to 1,700.00 | EUR 960.78 | EUR 1,700.00 |
| 4: over 1,700.00 to 1,850.00 | EUR 1,143.79 | EUR 1,850.00 |
| 5: over 1,850.00 to 2,030.00 | EUR 1,209.15 | EUR 2,030.00 |
| 6: over 2,030.00 to 2,330.00 | EUR 1,274.51 | EUR 2,330.00 |
| 7: over 2,330.00 to 2,760.00 | EUR 1,356.21 | EUR 2,760.00 |
| 8: over 2,760.00 to 3,190.00 | EUR 1,437.91 | EUR 3,190.00 |
| 9: over 3,190.00 to 3,620.00 | EUR 1,519.61 | EUR 3,620.00 |
| 10: over 3,620.00 to 4,050.00 | EUR 1,601.31 | EUR 4,050.00 |
| 11: over 4,050.00 to 6,000.00 | EUR 1,732.03 | EUR 5,101.20 |
| 12: over 6,000.00 | EUR 1,928.10 | EUR 5,101.20 |

Inside the band the client chooses the base. Whatever the net income, no base may exceed EUR 5,101.20 a month, and the lowest base in either table is EUR 653.59.

### Rule 3: Contribution rate breakdown, tax year 2026

Each rate applies to the base. There is no employer half in RETA: the worker pays all of each.

**RETA rates 2026**

| Concept | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| Contingencias comunes | 28.30% | "28,30 por ciento" |
| Contingencias profesionales | 1.30% | "1,30 por ciento" |
| Of which temporary incapacity | 0.66% | "0,66 por ciento" |
| Of which permanent incapacity, death, survivors | 0.64% | "0,64 por ciento" |
| Cese de actividad | 0.90% | "0,90 por ciento" |
| Cese de actividad, agrarian special system inside this regime | 2.20% | "el 2,20 por ciento" |
| Formacion profesional | 0.10% | "0,10 por ciento" |
| Mecanismo de equidad intergeneracional | 0.90% | "tipo del 0,90 por ciento" |
| Extra charge where accident cover is not taken | 0.10% | "adicional equivalente al 0,10 por ciento" |

No official page prints a combined RETA percentage, so this Guide states none. Read the total from the TGSS receipt.

### Rule 4: Cuota formula

Article 308.1.b: the monthly cuota is the Rule 2 base with the Rule 3 rates applied. Where temporary incapacity is covered in another regime and the person does not opt in here, the order applies a reduction coefficient to the common contingencies cuota.

### Rule 5: Tarifa plana

A fixed monthly fee instead of base times rate, for a first registration or someone not in RETA in the two years before the date of effect (article 38 ter of Ley 20/2007). Nothing is contributed for cessation of activity or training during it, and benefits run on the general band 1 minimum.

**Reduced fee amounts set by law**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482 |
| Monthly reduced fee, 2023 to 2025 | EUR 80 | "será de 80 euros mensuales" |
| From month twenty-five in the article 38 ter(10) cases | EUR 160 | "de 160 euros a partir del mes vigesimoquinto" |

**The 2026 position.** Transitional provision five of Real Decreto-ley 13/2022 fixed the fee for 2023 to 2025 only and leaves later years to each State Budget Law; article 38 ter(1) says the same. No Budget Law has been approved for 2026, and neither Orden PJC/297/2026 nor Real Decreto-ley 3/2026 sets an amount: "cuota reducida", "tarifa plana" and "38 ter" appear in neither. TGSS guidance still shows EUR 80 a month plus the intergenerational equity contribution. Do not state a 2026 amount from memory: read it from the TGSS award and receipt, and name that document as the source.

**Duration and conditions** (article 38 ter): twelve complete calendar months from the date of effect, then a further twelve if net income in that second period is below the annual minimum wage, met in each calendar year it spans. Apply at registration, and again before the second period. Anyone who has used the fee before must have been out of RETA three years, not two. The first period is not regularised; the second only for a year in which income exceeded the annual minimum wage. Family members up to the second degree are excluded. For a recognised disability of at least 33 per cent, or a victim of gender violence or terrorism, the periods are twenty-four and thirty-six months. The right ends if the worker deregisters from this regime during either period.

### Rule 6: Autonomo societario minimum

Rule four of article 308.1.a: family members under article 305.2.k, and self-employed people under article 305.2 b) and e), where company directors and working members of companies sit, may not choose a monthly base below the general regime group 7 minimum, and the final base at regularisation may not be below it either. Ninety days registered in the period is enough for it to bite. Article 18.4 of the order also lets them keep the 2025 provisional base during 2026.

**Group 7 minimum base**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| Minimum monthly base, general regime group 7, 2026 | EUR 1,424.40 | "7 Auxiliares Administrativos. 1.424,40" |

### Rule 7: Payment schedule

Monthly, charged on the last working day of the month, by direct debit through a bank or collaborating institution. Paying late brings the surcharges below. Interest under article 31 is added where the debt is still unpaid fifteen days after the providencia de apremio is notified, or after the start of the deduction procedure.

**Surcharges for paying late (article 30)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| Duties met, paid in the first calendar month after the deadline | 10% | "Recargo del 10 por ciento" |
| Duties met, paid from the second calendar month | 20% | "a partir del segundo mes natural" |
| Duties not met, paid before the deadline in the demand | 20% | "antes de la terminación del plazo" |
| Duties not met, paid after that deadline | 35% | "Recargo del 35 por ciento" |

The duties are those in article 29: filing the contribution documents, with the data the regulations require, within the payment period.

### Rule 8: Base change windows (6 per year)

Six changes a year; the window decides when a change takes effect, per the TGSS base and income service listed in Sources. Asked 1 January to the last day of February, effective 1 March; 1 March to 30 April, effective 1 May; 1 May to 30 June, 1 July; 1 July to 31 August, 1 September; 1 September to 31 October, 1 November; 1 November to 31 December, 1 January next. A change during sick leave takes effect the day after the medical discharge.

### Rule 9: Annual regularisation (automatic)

Article 308.1.c. The TGSS compares the bases chosen with the income the tax administration sends it and regularises automatically. The result arrives as an electronic notification.

- Paid below the cuota for the band's minimum base: the difference is payable up to the last day of the month after notification, without interest or surcharge.
- Paid above the cuota for the band's maximum base: the TGSS refunds the difference of its own motion, without interest, before 30 April of the year after the income was sent.
- Surcharges and interest are never refunded; debts already run up on provisional bases stand.
- No IRPF return, or one with no income declared under direct estimation: the final base is the group 7 minimum in Rule 6.
- Excluded: months already used for a benefit granted, the reduced fee period, and the T2-4 late registration period.

### Rule 10: Tax deductibility

The Agencia Tributaria states that cuotas paid to RETA for the activity are a deductible expense of it. The regularisation is picked up in the year it is settled, not the year regularised: an amount to pay is a higher deductible social security expense of that year (box 0196); an amount returned reduces that year's expense (box 0197); any part of the refund above the cuotas paid that year is higher income (box 0178). The page is in Sources. Keep principal, surcharge and interest apart. No page read for this refresh says whether a late surcharge is deductible, so leave it out of the expense until an accountant rules on it.

### T2-1: Pluriactividad (simultaneous employment + RETA)

**Trigger:** employee under the general regime and in RETA at the same time.
**Issue:** contributions are due in both. Where the two together pass the threshold below, part of the excess is refunded.
**Action:** flag for the reviewer. The TGSS pays the refund within four months of the regularisation, later where the contribution has particular features or the worker has to supply data.

**Pluriactividad refund 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537 |
| Combined common contingencies contributions above which a refund arises | EUR 17,323.68 | "superen la cuantía de 17.323,68 euros" |
| Share of the excess refunded, capped at that share of the RETA cuotas paid | 50% | "del 50 por ciento del exceso" |

### T2-2: Autonomo over age 47

**Trigger:** someone aged 47 or over asks whether age restricts the base they may elect.
**Issue:** it does not. Neither the LGSS nor Orden PJC/297/2026 carries an age restriction: "cuarenta y siete" and "47 años" appear in neither. That rule belonged to the system replaced on 1 January 2023. What survives is article 18.5 of the order, on transitional provision six of Real Decreto-ley 13/2022: someone contributing before 1 January 2023 on a base higher than their income would give, unchanged since, may keep it during 2026, or choose a lower base than that one.
**Action:** check the history before moving a long-standing high base; the right is lost once it changes.

### T2-3: Large regularisation demand

**Trigger:** a large additional amount because the estimated band was far below the final one.
**Issue:** payable up to the last day of the month after notification, without interest or surcharge. A deferral (aplazamiento) can be applied for.
**Action:** flag for the reviewer.

### T2-4: Mid-year alta (pro-rata)

**Trigger:** registration part way through a month.
**Issue:** the start date can be chosen only three times a year, and only if applied for in time; those registrations run from the day of alta. Any other registration that year takes effect on the first day of the month work starts, and the whole month is contributed for. Deregistrations work the same way. Where registration was reported late, the base from the day activity started to the last day of the month it was reported is the general band 1 minimum, and that period is left out of the regularisation. A late alta also loses the right to reductions in the cuota, and carries a penalty.
**Action:** confirm the date of alta and whether it was reported in time.

**Late registration base**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo+autonomo/guia |
| Base for the late registration period, 2026 | EUR 950.98 | "que en 2026 son 950,98 €/mes" |

### T2-5: Tarifa plana extension rejected

**Trigger:** income in the first period reached the annual minimum wage.
**Issue:** the second twelve months are not available. Contribution for all protected contingencies starts on the first day of the month after the first period ends.
**Action:** confirm the income and the date the ordinary cuota starts.

### T2-6: Ceuta and Melilla

**Trigger:** the client lives and works in Ceuta or Melilla.
**Issue:** a self-employed worker resident and active there in the listed sectors pays a reduced share of the common contingencies cuota on the provisional or final base. The share changed during 2026, so a full year needs both rows below. The sector list also changed: the earlier wording named building construction inside the exception clause, so a builder was OUT, and the wording in force from 1 October 2026 does not name it at all, so a builder is IN. That one sentence carries its exceptions inside it, so read article 36 for the period in question before deciding a sector is in or out.
**Action:** confirm the sector and split the year at the boundary date before quoting a cuota.

**Reduction of the common contingencies cuota, Ceuta and Melilla**

| Cuotas accrued | Value | Note |
| --- | --- | --- |
| Source, first row | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2023-625 |
| Before 1 October 2026 | 50% | "bonificación del 50 por ciento de la cuota por contingencias comunes" |
| Source, second row | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |
| From 1 October 2026 | 75% | "bonificación del 75 por ciento de la cuota por contingencias comunes" |

## Section 7: Excel working paper template

~~~
SPAIN RETA CONTRIBUTIONS. WORKING PAPER
Client: [name]  Tax Year: [year]  Prepared: [date]

INPUT
  Case in article 305.2:  [individual / letter b) or e)]
  Revenue, expenses:      EUR [__] / EUR [__]
  Net income, deduction:  EUR [__] / EUR [__]
  Net for RETA, monthly:  EUR [__] / EUR [__]
  Band, date of alta:     [__] / [__]
  Reduced fee eligible:   [YES / NO]

CUOTA
  Chosen base in band:    EUR [__]
  Rates applied (Rule 3): [each concept and its rate]
  Monthly, annual cuota:  EUR [__] / EUR [__]
  Or reduced fee awarded: EUR [__] for [__] months

REGULARISATION
  Final band, min base:   [__] / EUR [__]
  Monthly difference:     EUR [__]
  Annual adjustment:      EUR [__] / [DEMAND / REFUND]

IRPF
  Total cuotas paid:      EUR [__]
  Box (Rule 10):          [0196 / 0197 / 0178]

REVIEWER FLAGS
  [List any Tier 2 flags]
~~~

## Section 8: Bank statement reading guide

### How RETA payments appear on Spanish bank statements

**Debits:** "TGSS", "TESORERIA GENERAL", "SEGURIDAD SOCIAL", "CUOTA AUTONOMOS", on the last working day of each month, a consistent amount unless the base changed in a Rule 8 window. **Regularisation:** "TGSS REGULARIZACION", "COMPLEMENTO CUOTAS". **Refunds:** "TGSS DEVOLUCION", "TGSS REINTEGRO", a CREDIT due before 30 April, Rule 9.

**Key identification tips:**
1. RETA is monthly, not quarterly: look for a consistent end-of-month debit.
2. Do not read the band off the debit. Different bases give similar cuotas, and a reduced fee, a bonificacion or a mid-month alta break the pattern. Take the base from the Informe de bases de cotizacion.
3. AEAT debits are tax.

## Section 9: Onboarding fallback

If the client provides only a bank statement:

1. **Scan for TGSS debits** and identify the monthly pattern and amount.
2. **Do not infer the band.** Ask for the TGSS Informe de bases de cotizacion.
3. **Spot a possible reduced fee:** a small identical monthly debit, confirmed on the award.
4. **Look for a regularisation:** a large debit or credit outside the pattern.
5. **Flag:** "The RETA base was not read from a TGSS document. The reviewer must confirm before the IRPF filing."

## Section 10: Reference material

### Net income example

Work it out in this order, with the client's own amounts. Do not carry an example number into a client file.

1. Computable income: net income under the IRPF rules, increased by the owner's own social security cuotas (article 308.1.c).
2. Apply the Rule 1 deduction, then divide by the months in the period for the monthly average.
3. Find the band in Rule 2 whose income range contains that average, and choose a base between its minimum and maximum. The cuota follows from Rule 3.

### Employee and employer contributions in the general regime, 2026

A client with staff pays these as an employer; one in pluriactividad pays them as an employee. No official page prints a combined employer percentage, so the parts are given as the order prints them. The accident and occupational disease premium is the tariff by activity in additional provision 61. The maximum base is the Rule 2 ceiling and the group 7 minimum is in Rule 6; other group minimums are in article 3 of the order.

**General regime rates 2026**

| Concept | Total | Employer and employee shares |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| Contingencias comunes | 28.30% | employer 23.60%, employee 4.70% |
| Unemployment, permanent contract | 7.05% | employer 5.5%, employee 1.55% |
| Unemployment, fixed-term contract | 8.30% | employer 6.70%, employee 1.60% |
| FOGASA | 0.20% | employer only |
| Formacion profesional | 0.70% | employer 0.60%, employee 0.10% |
| Mecanismo de equidad intergeneracional | 0.90% | employer 0.75%, employee 0.15% |

**Solidarity contribution 2026**, on the part of pay above the maximum base. For artists and for bullfighting professionals the order makes this contribution definitive for the employer and provisional for the worker, regularised at the end of the year; for everyone else it says nothing of the kind.

| Part of pay | Rate | Employer and employee shares |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| From EUR 5,101.21 to EUR 5,611.32 | 1.15% | employer 0.96%, employee 0.19% |
| From EUR 5,611.33 to EUR 7,651.80 | 1.25% | employer 1.04%, employee 0.21% |
| Above EUR 7,651.80 | 1.46% | employer 1.22%, employee 0.24% |

### Cese de actividad (cessation benefit)

The regulatory base is the average of the bases contributed over the twelve continuous months before the legal cessation. Duration depends on the months contributed for cessation of activity in the forty-eight before it, at least twelve in the last twenty-four: four months of benefit for twelve to seventeen contributed, up to twenty-four months for forty-eight or more. A new award needs eighteen months since the last. Voluntary cessation that is not a legal cessation does not qualify. Maximum and minimum amounts are percentages of the IPREM in article 339.3.

**Rate applied to the regulatory base**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| General rate, whole period of the benefit | 70% | "la base reguladora el 70 por ciento" |
| Article 331.1.a) points four and five, and partial suspension for force majeure | 50% | "será del 50 por ciento" |

### IT (sick leave) coverage

A self-employed worker gets the subsidy from the fourth day of a sick leave that is not work related, must be registered and up to date with the cuotas, and must have contributed at least 180 days in the five years before. The percentages below are what Social Security publishes for temporary incapacity, on the general page for the benefit, not a RETA page. A higher base gives a higher daily benefit: the regulatory base is the common contingencies base of the month before the leave started. For a self-employed worker the subsidy for a work accident or an occupational disease runs from the day after the sick note, and no minimum contribution period is required. Once sixty days of the sick leave have passed from the medical sign off, the mutua, or where relevant the state employment service, pays the cuotas for every contingency.

**Percentage of the regulatory base**

| Case | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365 |
| Common illness or non-work accident, day 4 to day 20 | 60% | "60% desde el día 4 hasta el 20" |
| Common illness or non-work accident, from day 21 | 75% | "75% desde el día 21 en adelante" |
| Accident at work or occupational disease, from the day the right arises | 75% | "75% desde el día en que se produzca" |

### Test suite

None states a cuota: that depends on the base chosen inside the band and on which rates apply.

- Monthly average EUR 2,330.00: general band 6, which runs up to and including its top figure.
- Monthly average exactly EUR 1,166.70: general band 1, not reduced band 3, which stops below it.
- Monthly average at the 6,000.00 boundary in Rule 2: general band 11, not band 12, which begins above it.
- Company member under article 305.2.b, average EUR 900.00: the base may not be below the group 7 minimum.
- Chose the minimum of general band 2, final income in general band 10: the difference is payable up to the last day of the month after notification.
- No IRPF return filed: final base is the group 7 minimum.
- New registration with the reduced fee: twelve complete calendar months from the date of effect, no cessation or training contribution in them, and no amount stated for this year.
- Regularisation settled this year for last year's cuotas: an amount to pay goes in box 0196, an amount returned in box 0197, and any excess over the cuotas paid in box 0178.

### Prohibitions

- NEVER compute without knowing which case in article 305.2 applies
- NEVER use gross income for the band. Apply the Rule 1 deduction first
- NEVER say a registered client can avoid RETA
- NEVER present the reduced fee as automatic. It is applied for at registration
- NEVER state a 2026 reduced fee from memory. No Budget Law has set one
- NEVER add the Rule 3 rates together and call the sum an official rate
- NEVER ignore the regularisation
- NEVER advise on pluriactividad without the reviewer
- NEVER present a cuota as exact without naming the base
- NEVER confuse the monthly payment with a quarterly one
- NEVER deduct a late surcharge. The live Guide treated surcharges and penalties as not deductible, and no page read for this refresh confirms or denies it. Keep it out and ask the accountant
- NEVER compute sick pay without the base of the month before the leave

## The method, step by step

1. Confirm which case in article 305.2 applies: it decides the Rule 1 deduction and the Rule 6 floor. See the [LGSS](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724).
2. Estimate the monthly average of annual net income under article 308.1.c, apply the Rule 1 deduction, and find the band in [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296).
3. Choose a base inside that band, subject to the Rule 6 floor, through the TGSS base and income service in Sources, in one of the Rule 8 windows.
4. For someone starting out, apply for the reduced fee at registration under article 38 ter of [Ley 20/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409) and record the amount the TGSS awards, since the law sets none for 2026.
5. Pay by direct debit on the last working day of each month, per the TGSS guide linked in T2-4. Late payment brings the Rule 7 surcharges.
6. Re-estimate income in the year and move the base in the next window if it changed (article 308.1.a).
7. File the IRPF return. The TGSS regularises automatically: read the notification, settle or expect the refund on the Rule 9 timetable, and book it as Rule 10 directs.

## Ask the client first

- Are you registered as an individual, or as a company director or working member? It decides the generic deduction and the group 7 floor.
- Have you been in RETA in the last two years, and ever used the reduced fee? It sets eligibility and whether the wait is two years or three.
- What do you expect to earn this year, and has that changed since you chose your base?
- Are you also an employee under the general regime? That opens the T2-1 refund.
- Were you registered late, or did you pick the start date? It changes the opening period's base and whether it is regularised.
- Have you had a regularisation notification, and did you pay or receive on it?
- Do you live and work in Ceuta or Melilla? It reduces the common contingencies cuota, and the reduction changed during the year.

## When to refuse or refer

- Anyone asking the exact reduced fee. The periods are in Rule 5; the 2026 amount is not set in law.
- Anyone posted to or from another EU country, or contributing in two member states.
- A specific Mutua's benefits, cover or payment of a claim.
- The employer's accident and occupational disease premium: the tariff by activity in additional provision 61 of the LGSS.
- Autonomous community and foral questions. Alava, Bizkaia, Gipuzkoa and Navarra run their own tax administrations.
- Whether a late surcharge is deductible for IRPF. No page read here answers it.
- Any request for a combined RETA percentage, an effective rate, or a cuota without a named base.

## Sources

- [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296)
- [Ley General de la Seguridad Social](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724)
- [Real Decreto-ley 13/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482)
- [Ley 20/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409)
- [Bases and rates of contribution](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537)
- [Temporary incapacity benefit](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365)
- [TGSS Importass, guide for the self-employed](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo+autonomo/guia)
- [TGSS Importass, base and income service](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos)
- [Agencia Tributaria, regularisation of RETA cuotas](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/7-cumplimentacion-irpf/7_4-rendimientos-actividades-economicas/7_4_2-regimen-estimacion-directa/7_4_2_3-gastos-fiscalmente-deducibles/cotizaciones-reta.html)

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in Spain) before filing or acting upon.

> Contributed by OpenAccountants.

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
