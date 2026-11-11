---
name: cl-social-contributions
description: "Chile social contributions of independent workers (trabajadores independientes) for income of 2026, settled in Operación Renta, año tributario (AT) 2027. Covers who must contribute (DL 3.500 art. 89: art. 42 No. 2 honorarios and partners of societies of professionals) and who is exempt, the annual base of 80% of gross honorarios with its floor of four minimum monthly incomes and its ceiling of 12 x 90 UF, the pension contribution of 10% plus the AFP commission, the 7% health contribution, the SIS, work-accident insurance under Ley 16.744 (0.90% plus the activity rate) and the 0.03% SANNA contribution, the choice between total coverage and partial coverage at 90% for AT 2027 (Ley 21.133), the rule that limits the pension contribution to what the boleta withholding leaves, the order in which the withholding pays each item (art. 92 G), the coverage year from 1 July 2027 and the voluntary contributions of Ley 21.735. Trigger on: cotizaciones independientes, boleta de honorarios cotización, cobertura parcial o total, Operación Renta 2027, AFP independiente, Fonasa honorarios, SIS independientes. Out of scope: employees (cl-payroll), the income tax on honorarios (cl-income-tax)."
version: 2.2
jurisdiction: CL
tax_year: 2026
tax_year_notes: "income of calendar 2026, declared in Operación Renta AT 2027"
last_updated: 2026-11-11
category: payroll
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
---

# Chile: social contributions of independent workers (income 2026, AT 2027) v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill works out the pension, health and insurance contributions of an independent worker who earns honorarios in Chile in 2026. They are not paid monthly: the Servicio de Impuestos Internos (SII) computes them in the annual income tax return (Form F22) filed in April 2027 (año tributario, AT, 2027), and the Tesorería General de la República (TGR) pays them out of the boleta withholding before any income tax (DL 3.500 art. 92 F). Tax year: calendar 2026 income. Currency: Chilean peso (CLP); the ceiling is in Unidades de Fomento (UF).

Linked skills, not repeated here:

- [cl-income-tax](cl-income-tax.md): the boleta withholding rate for 2026 (15.25%) and the PPM of independents, the IGC on honorarios, gastos presuntos against gastos efectivos and the F22 codes, including the line where the cotizaciones are charged.
- [cl-payroll](cl-payroll.md): contributions of employees and employers, and the SIS paid by employers.
- [cl-cross-border](cl-cross-border.md): fees paid to people who are not resident in Chile.

**Which text of the law.** DL 3.500 as consolidated on LeyChile and read on 11 November 2026 in the version in force that day (it has deferred changes from 1 April 2027, not used here); Ley 21.133 (Diario Oficial 2 February 2019, single version, transitory articles); Ley 20.255 arts. 88 and 89 (version in force; deferred text from 1 April 2027 not used); Ley 16.744 art. 15; Ley 21.010 art. 3; Ley 21.063 art. 24; Ley 21.735 (Diario Oficial 26 March 2025) arts. 15, 16 and 46 transitorio. The ceiling, the AFP commissions and the SIS rate are set by the Superintendencia de Pensiones (SP) and read on spensiones.cl.

## Who this applies to

- **Must contribute:** every individual who, without being subordinate to an employer, works on their own and earns income taxed under LIR art. 42 No. 2 (honorarios, boletas de honorarios, boletas de prestación de servicios de terceros), and partners of societies of professionals taxed under art. 42 No. 2 (DL 3.500 arts. 89 and 90, first paragraph). They must join an AFP; the first contribution makes them members (art. 89). A worker joining for the first time goes to the AFP with the lowest commission (SP).
- **Exempt from the AFP contribution** (SP, independent workers page): women aged 50 or more and men aged 55 or more on 1 January 2018 (Ley 21.133 art. 3 transitorio, which also lifts health, Ley 16.744 and SANNA); members of other pension systems (the old IPS, Dipreca and Capredena schemes keep their own rules, DL 3.500 art. 92 I); an annual taxable base below four minimum monthly incomes; people who contributed as employees in every month of the year at the ceiling; and old-age or total-invalidity pensioners.
- **Pension age, or pensioners who keep working:** a man over 65, a woman over 60, or an old-age or total-invalidity pensioner pays only health, Ley 16.744 and SANNA, and is exempt from the pension contributions of Title III (DL 3.500 art. 92, sixth paragraph). A partial-invalidity pensioner pays all of them except the SIS (art. 92, last paragraph).
- **Employees with honorarios on the side:** they contribute on the honorarios too, but wages and honorarios are added together for the annual ceiling (art. 90, second paragraph; see The base).
- **Not covered here:** independents with no art. 42 No. 2 income (they may contribute monthly, art. 90, third paragraph), people with no paid activity (voluntary members, art. 92 J), business owners taxed in the first category, and workers covered by a bilateral social-security agreement (refer).

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Year | Source URL |
|---|---|---|---|---|
| Annual taxable base (renta imponible anual) | 80% of gross art. 42 No. 2 income of the calendar year before the return | income of 2026, declared AT 2027 | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=7147 (DL 3.500 art. 90) |
| Floor of the base | 4 × CLP 553,553 = CLP 2,214,212; equivalent gross honorarios trigger 5 × IMM = CLP 2,767,765 | ordinary working-age IMM in force at 31 December of the income year, per current law; Ley 21.830 fixes CLP 553,553 from 1 May 2026 until the next adjustment from 1 January 2027. Check later enacted changes before filing | 2026 | https://www.suseso.gob.cl/613/w3-propertyvalue-136095.html ; https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1225354 |
| Monthly ceiling (límite máximo imponible, art. 16) | January provisional 89.9 UF; February-December definitive 90.0 UF | annual 2026 cap uses the December limit, hence 12 × 90 UF; distinguish monthly voluntary history | 2026 | https://www.spensiones.cl/portal/institucional/594/w3-article-16921.html |
| Annual ceiling of the base | 12 x 90.0 UF = 1,080 UF, at the UF of the last day of December | wages and honorarios together | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=7147 (DL 3.500 art. 90) |
| Partial coverage (cobertura parcial), AT 2027 | Pension and health on 90% of the base; SIS, Ley 16.744 and SANNA stay on 100% | only if the worker chooses it in the F22; 100% for everyone from AT 2028 | AT 2027 | https://www.bcn.cl/leychile/navegar?idNorma=1128420 (Ley 21.133 art. 2 transitorio) |
| Pension contribution | 10% of the base | under the statutory age exemption, excluding old-age/total-invalidity pensioners; partial-invalidity pensioners remain subject to pension contributions, except SIS under art. 92 | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=7147 (DL 3.500 art. 17) |
| AFP commission | The average of the commissions the worker's AFP charged in the year before payment (2026); current rates: Capital 1.44%, Cuprum 1.44%, Habitat 1.27%, Modelo 0.58%, PlanVital 1.16%, Provida 1.45%, Uno 0.46% | SP sets the method by general rule | 2026 | same, art. 92 C; https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9897.html |
| SIS (disability and survivors insurance) | 1.78% of taxable income from August 2026 for independents and voluntary members; for those paying through the withholding, the SP gave 1.49% for AT 2026 | the AT 2027 rate for retention payers is not yet published | 2026 | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9913.html |
| Health (Fonasa, or the chosen Isapre) | 7% of the base | an Isapre plan above 7% is paid directly by the worker, never out of the withholding | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=7147 (DL 3.500 art. 92) |
| Work-accident insurance (Ley 16.744), basic | 0.90% | on the same base (Ley 20.255 art. 88) | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=28650 (Ley 16.744 art. 15 a)) |
| Work-accident insurance, additional | activity schedule up to 3.4%, subject to the separate art. 16 surcharge of up to 100% | independents are excluded from ordinary DS 67 loss-ratio evaluation; their applicable rate can be retained, activity-based or subject to a safety-breach surcharge. Obtain the actual ISL/mutual rate, not a blanket 3.4% ceiling | 2026 | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=28650 (arts. 15-16); https://www.suseso.gob.cl/613/w3-propertyvalue-136095.html |
| SANNA (insurance for parents of seriously ill children) | 0.03% of the base | paid by the independent | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=1102293 (Ley 21.010 art. 3); https://www.bcn.cl/leychile/navegar?idNorma=1113014 (Ley 21.063 art. 24 a)) |
| Pension limited to what the withholding leaves (total coverage only) | During the first nine years from 2019 (AT 2019 to AT 2027), for those who do not choose partial coverage, the pension contribution (with the commission) is the withholding less SIS, Ley 16.744, SANNA and health | AT 2027 is the ninth year | AT 2027 | https://www.bcn.cl/leychile/navegar?idNorma=1128420 (Ley 21.133 art. 5 transitorio, second paragraph) |
| Boleta withholding 2026 | In [cl-income-tax](cl-income-tax.md) (one figure, one home) | services provided in 2026 | 2026 | https://www.sii.cl/destacados/boletas_honorarios/ |
| Ley 21.735 voluntary package for art. 42 No. 2 workers | gross phase-in schedule: 1% August 2025-July 2026; 3.5% August 2026-July 2027, before the applicable SIS offset. In the latter period: 0.1% individual, 0.9% protected return and 2.5% FAPP | all parts together; only until old-age/total-disability pension or age 65, whichever first; monthly declared base from 1 IMM to the DL 3.500 cap. Ultimate 6% plus 2.5% is the completed schedule, not the 2026 rate; no net early-period computation supplied | 2026 | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1212060 (arts. 15,16,4 and 46 transitorios) |

## The base

Work in this order for the 2026 income year.

1. **Gross honorarios.** All art. 42 No. 2 income received in 2026: boletas with withholding, boletas without withholding (where the worker paid PPM in F29), and partners' shares in a society of professionals (art. 90). The F22 codes are in [cl-income-tax](cl-income-tax.md).
2. **Annual base = 80% of gross**, subject to the 4-IMM eligibility threshold in the table (below it, no AFP duty) and at most 1,080 UF at the UF of 31 December 2026. SUSESO requires both IMM and cap in force at 31 December of the income year. Under law published at this read date, the base threshold is CLP 2,214,212 and gross trigger CLP 2,767,765; this is an eligibility test, not an automatic increase of an exempt below-threshold base.
3. **Employee with honorarios.** Add the year's taxable wages to the honorarios base for the annual ceiling. If the contributions go over the ceiling, the institutions re-settle and refund the excess (art. 90, second paragraph). A worker who contributed at the ceiling as an employee in every month owes nothing on the honorarios (SP).
4. **Coverage.** Total coverage: every item on 100% of the base. Partial coverage, chosen in the F22: pension (10% plus commission) and health (7%) on 90% of the base; SIS, Ley 16.744 and SANNA on 100% (Ley 21.133 art. 2 transitorio). The worker can switch between the two each year during the transition (Subsecretaría de Previsión Social FAQ).
5. **Compute each item** at the rates above. Old-age or total-invalidity pensioners and the statutory age-exempt categories pay health, Ley 16.744 and SANNA only. Partial-invalidity pensioners remain subject to the pension contribution but are exempt from SIS under art. 92.
6. **Apply the withholding** (and the PPM of art. 84 b)). TGR pays the items in this order until the money runs out: (1) SIS; (2) Ley 16.744; (3) SANNA; (4) health; (5) pension and AFP commission, pro rata; (6) pension balances left unpaid in earlier years, indexed (art. 92 G). Under total coverage in AT 2027, the pension item is limited to what is left after (1) to (4); the commission share of that amount is commission / (10% + commission) of it (Ley 21.133 art. 5 transitorio, second paragraph).
7. **What remains** of the withholding is then set against the income tax; any excess is refunded. For a genuine payable shortfall, art. 92 F(ii) provides direct payment under the Superintendencias' joint rule, whose actual deadline is unconfirmed here. This is separate from the total-coverage current-year pension limit in Ley 21.133 art. 5 transitorio: a difference removed by that limit is not automatically a new pension debt. Article 92 G's prior unpaid pension balances are a separate category.

**Income tax.** Contributions paid under these rules count as social-security contributions for the LIR (Ley 20.255 art. 88, third paragraph; DL 3.500 art. 90). Whether they reduce the IGC base depends on gastos presuntos or efectivos (LIR art. 50): see [cl-income-tax](cl-income-tax.md).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Boleta withholding and PPM during 2026 | Monthly, by the client or by the worker in F29; dates in [cl-income-tax](cl-income-tax.md) | LIR arts. 74 No. 2, 84 b) |
| Choose total or partial coverage | In the AT 2027 F22, April 2027 | Ley 21.133 art. 2 transitorio |
| AFPs send members the certificate of contributions paid by employers, and report to the SII | By the last day of February 2027 | DL 3.500 art. 92 A |
| SII tells TGR, each AFP and each health institution what each worker owes | In the term of LIR art. 97 (refund timetable); SP says the first half of May | DL 3.500 arts. 92 D, 92 F; SP |
| Register with the ISL or a mutual before the first Ley 16.744 payment | Before the first annual payment (a worker not in a mutual is treated as in the ISL) | Ley 20.255 art. 88 |
| Coverage of SIS, Ley 16.744 and SANNA bought by the AT 2027 annual payment | 1 July 2027 to 30 June 2028, subject to each scheme's statutory benefit/payment conditions | DL 3.500 art. 92 E; Ley 20.255 art. 88; Ley 21.063 art. 5(b), amended by Ley 21.133 art. 4 |
| Ley 21.735 voluntary contributions | Monthly, by the last working day of the month after the income month | Ley 21.735 art. 16 |

**How it is filed.** There is no separate return. In the F22 on sii.cl the worker checks the honorarios the SII proposes, chooses total or partial coverage, and the SII computes the contributions in the cotizaciones line (see [cl-income-tax](cl-income-tax.md) for the codes). The AFP, Fonasa or the Isapre, the ISL or mutual, and the SANNA fund are paid by TGR from the withholding. A worker who starts honorarios in 2026 and wants cover before July 2027 has to pay monthly as a voluntary contributor (Subsecretaría de Previsión Social FAQ).

## Penalties and interest

- **Shortfall:** an actual prior unpaid pension balance, distinct from a current-year amount excluded by the total-coverage statutory limit, stays as an unpaid balance (saldo insoluto) and is paid, after the year's own contributions, out of the next years' withholdings, indexed under DL 3.500 art. 19 (art. 92 G, sixth place). The AFPs report these balances to the SII each February (art. 92 A).
- **Loss of cover:** Ley 16.744 benefits are paid only once the worker is up to date with the annual payment, with the registration rules of Ley 20.255 art. 88. Mandatory annual workers who are not attached to a mutual are deemed ISL-affiliated and registered for their July-June coverage period; absence of formal registration alone does not preclude occupational classification (current SUSESO Compendio D, chapter I §1). Do not apply a blanket pre-accident formal-registration denial to that deemed-registration case.
- **Withholding not paid by the client:** the client's penalty is under CT art. 97 No. 11, in [cl-income-tax](cl-income-tax.md).
- **Not issuing a boleta:** CT art. 97 No. 10, in [cl-income-tax](cl-income-tax.md).

## Cross-border points

- **A resident who bills foreign clients** has no withholding on those fees; the worker pays PPM (art. 84 b)), and the PPM funds the contributions the same way (art. 92 F i)).
- **Non-resident fee earners:** social-security treatment is outside this Guide's operative answer. Tax category, where work is performed, residence, foreign technical-professional exemption and treaty facts require separate research. The tax treatment is in [cl-cross-border](cl-cross-border.md); it does not establish a blanket social-security exemption.
- **Bilateral social-security agreements and the foreign-technician exemption** can change who contributes; neither was read for this skill. Refer.

## Two worked examples that recompute

Both examples are hypothetical formula illustrations using assumed SIS and commission inputs, not confirmed AT 2027 amounts payable or personal recommendations. Recompute when the annual parameters and filing instructions are published. Both use Valentina, a translator aged 34, resident in Santiago, with AFP Modelo (current commission 0.58%, used as a stand-in for its 2026 average) and Fonasa. In 2026 she received CLP 24,000,000 of gross honorarios, all from companies that withheld 15.25% (CLP 3,660,000). Her base is far below the ceiling (1,080 UF is about CLP 44.5 million at the UF of 31 October 2026, CLP 41,247.63). The SIS is taken at 1.78%, the SP rate in force from August 2026, because the SP's AT 2027 rate for retention payers is not yet published; the additional Ley 16.744 rate is taken as 0%. Rounding to whole pesos is left out.

### Example 1: hypothetical total coverage under assumed annual parameters

- Base = 24,000,000 x 80% = CLP 19,200,000.
- SIS 1.78% = 341,760; Ley 16.744 0.90% = 172,800; SANNA 0.03% = 5,760; health 7% = 1,344,000. Together CLP 1,864,320.
- Full pension and commission would be 10.58% x 19,200,000 = CLP 2,031,360, more than the CLP 1,795,680 the withholding has left. Under Ley 21.133 art. 5 transitorio, for AT 2027 the pension item is the CLP 1,795,680 left: commission 0.58 / 10.58 of it = CLP 98,439.92; to her pension account CLP 1,697,240.08.
- Nothing is left for the income tax, which she pays in full in the F22 (see cl-income-tax). No pension balance is carried forward: in AT 2027 the law sets the pension contribution at what is left.

```oa-check
name: CL independent AT 2027, CLP 24m honorarios, total coverage
inputs:
  gross: 24000000
  withholding_rate: 0.1525
  commission: 0.0058
  sis: 0.0178
steps:
  - withheld: gross * withholding_rate
  - base: gross * 0.80
  - insurances_and_health: base * (sis + 0.009 + 0.0003 + 0.07)
  - full_pension: base * (0.10 + commission)
  - pension_paid: min(full_pension, withheld - insurances_and_health)
  - commission_paid: round(pension_paid * commission / (0.10 + commission), 2)
  - to_account: pension_paid - commission_paid
  - left_for_tax: withheld - insurances_and_health - pension_paid
expected:
  withheld: 3660000
  base: 19200000
  insurances_and_health: 1864320
  pension_paid: 1795680
  commission_paid: 98439.92
  to_account: 1697240.08
  left_for_tax: 0
```

### Example 2: conditional partial-versus-total comparison

Partial coverage for AT 2027 puts pension and health on 90% of the base (CLP 17,280,000); SIS, Ley 16.744 and SANNA stay on CLP 19,200,000.

- SIS, Ley 16.744 and SANNA (2.71%) = CLP 520,320; health 7% of 17,280,000 = CLP 1,209,600; pension and commission 10.58% of 17,280,000 = CLP 1,828,224. Total CLP 3,558,144.
- The withholding covers it all and leaves CLP 101,856 toward her income tax.

The figures that decide, partial against total: CLP 101,856 more withholding left for the tax; CLP 32,544 more into pension and commission (1,828,224 against 1,795,680), because under total coverage the pension takes only what the withholding leaves; and CLP 134,400 less health contribution (1,209,600 against 1,344,000), which lowers the base for sick-leave and maternity subsidies (Subsecretaría de Previsión Social FAQ). Under these assumed rates, partial coverage leaves more cash for tax and allocates more to pension/commission, while reducing the health/subsidy base. Actual annual rates and personal benefit eligibility can change the comparison; this arithmetic does not establish which election Valentina should make. From AT 2028 the choice ends and everyone contributes on 100%.

```oa-check
name: CL independent AT 2027, CLP 24m honorarios, partial against total coverage
inputs:
  gross: 24000000
  withholding_rate: 0.1525
  commission: 0.0058
  sis: 0.0178
steps:
  - withheld: gross * withholding_rate
  - base: gross * 0.80
  - base_partial: base * 0.90
  - insurances: base * (sis + 0.009 + 0.0003)
  - health_partial: base_partial * 0.07
  - pension_partial: base_partial * (0.10 + commission)
  - total_partial: insurances + health_partial + pension_partial
  - left_partial: withheld - total_partial
  - pension_total_cover: withheld - insurances - base * 0.07
  - extra_pension_partial: pension_partial - pension_total_cover
  - health_given_up: base * 0.07 - health_partial
expected:
  insurances: 520320
  health_partial: 1209600
  pension_partial: 1828224
  total_partial: 3558144
  left_partial: 101856
  extra_pension_partial: 32544
  health_given_up: 134400
```

## Ask the client first

1. Did the client issue boletas de honorarios (or receive boletas de terceros, or a share of a society of professionals) in 2026, and for how much gross? Was 15.25% withheld on all of it, or did they pay PPM themselves?
2. Age on 1 January 2018 and today, and whether they are a pensioner (old age, total or partial invalidity).
3. Which AFP (or an old-system scheme), and Fonasa or an Isapre at what plan price.
4. Did they also earn wages in 2026, and did any employer contribute at the ceiling every month?
5. Total or partial coverage in the AT 2027 F22, and any planned medical or maternity leave between July 2027 and June 2028.
6. Their activity (for the additional Ley 16.744 rate) and whether they are registered with the ISL or a mutual; any foreign clients or a bilateral social-security agreement.

## Sources

| Source | URL | Read on |
|---|---|---|
| DL 3.500, LeyChile text in force on 11 Nov 2026 (JSON text service, version in force; deferred text from 1 Apr 2027 not used): arts. 16, 17, 89, 90, 91, 92, 92 A to 92 G, 92 I, 92 J | https://www.bcn.cl/leychile/navegar?idNorma=7147 | 2026-11-11 |
| Ley 21.133 (DO 2 Feb 2019, single version): arts. 2, 3 and 5 transitorios | https://www.bcn.cl/leychile/navegar?idNorma=1128420 | 2026-11-11 |
| Ley 20.255, version in force: arts. 88 and 89 | https://www.bcn.cl/leychile/navegar?idNorma=269892 | 2026-11-11 |
| Ley 16.744: arts. 2, 15 and 16 | https://www.bcn.cl/leychile/navegar?idNorma=28650 | 2026-11-11 |
| Ley 21.010: arts. 1 and 3 | https://www.bcn.cl/leychile/navegar?idNorma=1102293 | 2026-11-11 |
| Ley 21.063: arts. 5(b) and 24 | https://www.bcn.cl/leychile/navegar?idNorma=1113014 | 2026-11-11 |
| Ley 21.735 (DO 26 Mar 2025): arts. 15, 16, 4 and 46 transitorios | https://www.bcn.cl/leychile/navegar?idNorma=1212060 | 2026-11-11 |
| Read for the figures named: SP, independent workers page (who must contribute, exemptions, SIS 1.78% from Aug 2026 and 1.49% for AT 2026, May timetable, health 7%) | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9913.html | 2026-11-11 |
| Read for the figures named: SP, 2026 ceilings (90.0 UF; 87.8 UF in 2025) | https://www.spensiones.cl/portal/institucional/594/w3-article-16921.html | 2026-11-11 |
| Read for the figures named: SP, Sistema de AFP (commissions of the seven AFPs; new members go to the lowest commission) | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9897.html | 2026-11-11 |
| Read for the figure named: SII, Boleta de Honorarios 2026 (withholding 15.25%) | https://www.sii.cl/destacados/boletas_honorarios/ | 2026-11-11 |
| Read for the points named: Subsecretaría de Previsión Social, Ley de honorarios FAQ (switching coverage each year, effect of partial coverage on subsidies, voluntary cover for first-year workers) | https://previsionsocial.gob.cl/ley-honorarios/preguntas-frecuentes/ | 2026-11-11 |
| SUSESO current Compendio, Book II Title II D chapter I: registration, accident rates, annual base date, ended extraordinary levy | https://www.suseso.gob.cl/613/w3-propertyvalue-136095.html | 2026-11-11 |
| Ley 21.830 art. 1, IMM from 1 May 2026, current JSON | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1225354 | 2026-11-11 |
| DS 67 arts. 6 bis and 15, independent exclusion and safety surcharge | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=159800 | 2026-11-11 |
| SP provisional January 2026 ceiling, 89.9 UF | https://www71.spensiones.cl/portal/institucional/594/w3-article-16885.html | 2026-11-11 |
| SII 2026 UF table, 31 October CLP 41,247.63; illustration only, not December UF | https://www.sii.cl/valores_y_fechas/uf/uf2026.htm | 2026-11-11 |

Not yet confirmed: the SIS rate the SP will apply in AT 2027 to contributions paid through the withholding (the examples use 1.78%); each AFP's 2026 average commission under art. 92 C (the examples use the current rate); the UF of 31 December 2026 (sets the 1,080 UF ceiling in pesos); the joint rule of the Superintendencias setting the deadline for paying a shortfall directly; how the SII applies the Ley 21.133 art. 5 transitorio limit when the withholding exceeds the full contributions (read here as: the full 10% plus commission is charged and the rest goes to tax); the net early-phase Ley 21.735 voluntary payment after the applicable SIS offset and its operational implementation; bilateral social-security agreements and the foreign-technician exemption; the AT 2027 F22 codes for the cotizaciones.
