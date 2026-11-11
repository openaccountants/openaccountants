---
name: uruguay-social-contributions
description: "Uruguay social security contributions to BPS (Banco de Previsión Social) for tax year 2026. Covers dependent workers under Industria y Comercio (jubilatorio 15% personal and 7.5% employer, FONASA 3% to 8% personal by income and family and 5% employer plus the cuota mutual complement, FRL 0.10% each side, FGCL 0.025%), the 2026 ceilings and pension pillars under Ley 16.713 and the Ley 20.130 reform (tope C and nivel B UYU 288,836 from February 2026), the FONASA year-end refund, and owners without employees: the 2026 minimum contributions of unipersonales, SRL partners and sociedades de hecho on the BFC ficto scale (BFC UYU 1,847.96). Also BPS due dates and fines. Trigger on: aportes BPS, montepío, aporte patronal, FONASA, FRL, FGCL, tope de cotización, AFAP, unipersonal BPS, ficto BFC, Uruguay social security 2026. Out of scope: IRPF withholding (uruguay-payroll), monotributo, rural, construction, domestic work, professional funds (CJPPU)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uruguay-social-contributions"
  jurisdiction: "UY"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Uruguay social security contributions (BPS) for 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill computes the contributions BPS collects in 2026: for dependent workers, the personal and employer shares; for owners who work in their business without employees, the minimum monthly contribution. It does not compute income tax. It links to the other Uruguay skills and does not repeat them:

- [uruguay-payroll](uruguay-payroll.md): the full monthly payroll, including the IRPF the employer withholds, net pay, aguinaldo and salario vacacional, and the 2026 BPS due dates for employers.
- [uruguay-income-tax](uruguay-income-tax.md): IRPF, where the personal contributions below are deductible at 14% or 8%.
- [uy-cross-border](uy-cross-border.md): non-residents and foreign staff.

**IRPF is not a contribution.** IRPF is a DGI income tax. BPS collects it from employers alongside the nómina, but it is computed and owned by the payroll and income tax skills. "115 BPC" is an IRPF band edge, never a BPS threshold.

**Which text of the law.** Ley 16.713 (1995 pension system), Ley 20.130 (2023 pension reform, Sistema Previsional Común), Ley 18.211 (FONASA rates), as consolidated on IMPO; the 2026 values and minimums as BPS, which sets and collects them, publishes them.

**Quick reference, 2026**

| Item | Figure |
|---|---|
| BPC 2026 | UYU 6,864 (Decreto 11/026); FONASA band edge 2.5 BPC = UYU 17,160 |
| BFC (base ficta de contribución) | UYU 1,847.96 from January 2026 |
| Dependent worker, personal | Jubilatorio 15% + FONASA 3% to 8% + FRL 0.10% |
| Dependent worker, employer | Jubilatorio 7.5% + FONASA 5% (+ CCM) + FRL 0.10% + FGCL 0.025% |
| Jubilatorio ceiling (AFAP regimes) | UYU 288,836 a month from February 2026 (UYU 272,564 in January 2026) |
| Unipersonal without employees, category 1 (11 BFC) | UYU 8,833 a month if a FONASA beneficiary with no spouse or children |

## Who this applies to

- **Everyone doing paid work in Uruguay** is included in BPS, dependent or not, unless another fund (military, police, bank, notarial, professional) covers the activity; one activity cannot be affiliated to two funds (Ley 20.130 art. 3(1) to (4)).
- **Dependent workers and their employers**, private sector, "Industria y Comercio" affiliation. The employer withholds the personal share and pays both ([BPS, pago de aportes](https://www.bps.gub.uy/10357/pago-de-aportes.html)).
- **Owners without employees**: titulares of empresas unipersonales, partners of SRL and sociedades de hecho who work in the business, who pay on a ficto base in BFC and not on real pay ([BPS, Industria y Comercio](https://www.bps.gub.uy/6665/industria-y-comercio.html)). From the reform, a non-dependent's jubilatorio rate above 15% counts as the employer part (Ley 20.130 art. 21(2)).
- **Foreign employers.** A person working in Uruguay for a foreign entity without a permanent establishment is covered as non-dependent, on the pay actually received, unless a dependent worker proves cover in the employer's country under an agreement in force (Ley 20.130 art. 3(7)).
- **Out of scope.** Monotributo, the régimen de aportación gradual, rural, construction (aporte unificado), domestic work, public bodies (their employer rates vary), servicios bonificados, the professional fund (CJPPU) and the other parallel funds.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| BPC from 1 January 2026 | UYU 6,864 a month | 2026 | https://www.impo.com.uy/bases/decretos/11-2026 (art. 1) |
| BFC (base ficta de contribución) | UYU 1,847.96 (in force from January 2026) | 2026 | https://www.bps.gub.uy/5478/valores-actuales.html; https://www.bps.gub.uy/5479/valores-historicos.html |
| Jubilatorio personal (montepío), dependent workers | 15% | 2026 | https://www.bps.gub.uy/835/tasas.html; Ley 16.713 art. 181, https://www.impo.com.uy/bases/leyes/16713-1995 |
| Jubilatorio employer (patronal), Industria y Comercio, since 1 July 2007 | 7.5% | 2026 | https://www.bps.gub.uy/835/tasas.html |
| Jubilatorio, new entrants from the Sistema Previsional Común: personal rate | 15%, split 10% BPS up to nivel A, 5% AFAP up to nivel A and 15% AFAP between nivel A and nivel B | 2026 | https://www.impo.com.uy/bases/leyes/20130-2023 (arts. 21 and 22) |
| Ley 16.713 mixed regime topes A, B and C | UYU 96,279 / 144,418 / 288,836 a month (A and B from January 2026, C from February 2026) | 2026 | https://www.bps.gub.uy/5478/valores-actuales.html |
| Tope C in January 2026 | UYU 272,564 (in force from February 2025) | 2026 | https://www.bps.gub.uy/5479/valores-historicos.html |
| Ley 20.130 niveles A and B | UYU 144,418 (from January 2026) and UYU 288,836 (from February 2026) | 2026 | https://www.bps.gub.uy/5478/valores-actuales.html |
| FONASA personal, pay up to 2.5 BPC (UYU 17,160): no spouse / spouse without own SNIS cover | 3% / 5% | 2026 | https://www.bps.gub.uy/10314/tasas-fonasa.html |
| FONASA personal, pay over 2.5 BPC: no spouse, no children / no spouse, children / spouse, no children / spouse and children | 4.5% / 6% / 6.5% / 8% | 2026 | same; Ley 18.211 art. 61, https://www.impo.com.uy/bases/leyes/18211-2007 |
| FONASA employer | 5% of pay subject to montepío, plus the Complemento de Cuota Mutual (CCM) | 2026 | https://www.bps.gub.uy/10314/tasas-fonasa.html |
| CCM formula | (number of beneficiaries x cuota mutual) minus (3% basic personal + 5% employer contributions of all staff) | 2026 | same |
| Cuota mutual | UYU 1,820 (January to June 2026); UYU 1,880 from July 2026 | 2026 | https://www.bps.gub.uy/5479/valores-historicos.html |
| FRL personal (dependent and non-dependent) and employer, since 1 January 2019 | 0.10% each (0.125% to 31 December 2018) | 2026 | https://www.bps.gub.uy/10322/fondo-reconversion-laboral-frl.html |
| FGCL, employer, private-sector dependants, since 1 January 2019 | 0.025% | 2026 | https://www.bps.gub.uy/15668/fondo-de-garantia-de-creditos-laborales.html |
| FONASA year-end refund: personal contributions above 1.25 times the CPE of the worker, spouse and children covered | CPE UYU 6,858 a month (October and November 2026) | 2026 | Ley 18.211 art. 61; https://www.bps.gub.uy/5478/valores-actuales.html |
| Unipersonal without employees, minimum by category (BFC): 1 (11), 2 (15), 3 (20), 4 (25), 5 (30) | Base UYU 20,328 / 27,719 / 36,959 / 46,199 / 55,439 | 2026 | https://www.bps.gub.uy/6665/industria-y-comercio.html (vigencia enero 2026) |
| Same, categories 6 (36), 7 (42), 8 (48), 9 (54), 10 (60 BFC) | Base UYU 66,527 / 77,614 / 88,702 / 99,790 / 110,878 | 2026 | same |
| Unipersonal, FONASA beneficiary, no spouse, no children (code SS 15): total monthly payment, categories 1 to 10 | UYU 8,833 / 10,504 / 12,592 / 14,680 / 16,768 / 19,275 / 21,780 / 24,286 / 26,792 / 29,298 | 2026 | same |
| Same, no spouse, with children (SS 1) | UYU 9,502 / 11,173 / 13,261 / 15,349 / 17,437 / 19,944 / 22,449 / 24,955 / 27,461 / 29,967 | 2026 | same |
| Same, spouse, with children (SS 16) | UYU 10,394 / 12,065 / 14,153 / 16,241 / 18,329 / 20,836 / 23,341 / 25,847 / 28,353 / 30,859 | 2026 | same |
| Same, spouse, no children (SS 17) | UYU 9,725 / 11,396 / 13,484 / 15,572 / 17,660 / 20,167 / 22,672 / 25,178 / 27,684 / 30,190 | 2026 | same |
| Same, already covered for health through a dependent job (SS 2, 28, 29, 30) | UYU 5,143 / 6,814 / 8,902 / 10,990 / 13,078 / 15,585 / 18,090 / 20,596 / 23,102 / 25,608 | 2026 | same |
| Unipersonal titular not a FONASA beneficiary (SS 9 or 99), jubilatorio and FRL only; BPS notes this column is for a titular who employs more than five dependants paid below the employer ficto, and category 1 only where FONASA cover comes through servicios personales | UYU 4,594 / 6,265 / 8,353 / 10,441 / 12,529 / 15,036 / 17,541 / 20,047 / 22,553 / 25,059 | 2026 | same |
| SRL partner, minimum per partner | 15 BFC (UYU 27,719 base): UYU 6,265; or 20 BFC (UYU 36,959): UYU 8,353 | 2026 | same |
| Sociedad de hecho without employees, minimum per partner | 11 BFC (UYU 20,328): UYU 4,594; or 15 BFC (UYU 27,719): UYU 6,265 | 2026 | same |

## The base

**Dependent workers.**

1. The base is pay subject to contributions ("materia gravada"). Aguinaldo pays contributions; the salario vacacional does not (see [uruguay-payroll](uruguay-payroll.md) for both).
2. **Jubilatorio** on pay up to the ceiling of the worker's regime: Sistema Previsional Común (first job from 1 December 2023) up to nivel B; Ley 16.713 mixed regime up to tope C; above it, contributions are voluntary (Ley 16.713 art. 7; Ley 20.130 art. 22). BPS publishes the ceiling only for workers in the AFAP regime ([BPS, topes](https://www.bps.gub.uy/10306/topes-de-cotizacion.html)).
3. **Which pillar.** The 15% is not changed by the split; only where it goes. In the reform regime 10 points up to nivel A fund BPS and the rest goes to the AFAP. In the 1995 regime pay up to tope A is in the solidarity pillar and A to C in the individual savings pillar; a worker who used the art. 8 option sends 50% of the first-level pay to the AFAP. Under Ley 20.130 the aguinaldo is a separate income for this split (art. 24).
4. **FONASA personal** on all pay: band chosen by all the month's taxed pay without aguinaldo, then the family line. Spouse lines only where the spouse or partner has no SNIS cover of their own; a child is under 18 or of any age with a disability, including the spouse's (Ley 18.211 art. 61). A worker is a FONASA user from 13 days worked in the month or pay of 1.25 BPC, and an employer that takes on the complement may give user status regardless (art. 62).
5. **FRL** 0.10% personal and 0.10% employer on all pay; **FGCL** 0.025% employer on all pay.
6. **Employer FONASA** 5% plus the CCM where the cuota mutual for the covered workers exceeds the 3% basic personal plus 5% employer contributions of the whole staff.
7. **Year end.** Personal FONASA contributions for the year above 1.25 times the CPE of the worker and the family covered are refunded (Ley 18.211 art. 61).

**Owners without employees (Industria y Comercio).**

1. Pick the category (1 to 10, 11 to 60 BFC); the BFC base for January 2026 onward is UYU 1,847.96 per BFC.
2. Pick the health code: FONASA beneficiary by family situation (SS 1, 15, 16, 17), already covered through a dependent job (SS 2, 28, 29, 30), or not a beneficiary (SS 9 or 99).
3. The monthly payment is the BPS table amount. The non-beneficiary amount equals 22.6% of the base (for example 4,594 / 20,328), which is the 15% personal and 7.5% employer jubilatorio plus 0.10% FRL; the BPS note says that column is "aporte jubilatorio y FRL".
4. An SRL partner's minimum is 15 or 20 BFC and a sociedad de hecho partner's 11 or 15 BFC, as in the table.

## Deadlines and filing

| Step | What | When | Where |
|---|---|---|---|
| Registration | Register the business with BPS before starting; register each dependent worker (alta) and leaver (baja) | Alta from 10 days before the start date up to the start date itself | BPS online services, GAFI ([BPS](https://www.bps.gub.uy/818/declarar-al-personal.html)) |
| Monthly, employers | Nómina (declaración nominada) and payment of personal and employer contributions | Month after the work month, on the date for the last digit of the company number in the [2026 BPS calendar](https://www.bps.gub.uy/bps/file/23709/1/calendario-de-vencimientos-2026.pdf) (dates listed in [uruguay-payroll](uruguay-payroll.md)) | BPS online services |
| Monthly, owners without employees | Payment of the minimum contribution; BPS generates the monthly bill automatically and emails it. After three consecutive months unpaid, the automatic bill stops until the owner asks for it again | Month after, on the "Cobranza descentralizada" column of the 2026 calendar: January 23, February 24, March 20, April 24, May 25, June 22, July 21, August 21, September 21, October 22, November 23, December 21 | BPS "Emitir facturas" service, BPS Empresas app, collection network, bank debit ([BPS guide, Industria y Comercio](https://www.bps.gub.uy/bps/file/10291/13/guia---industria-y-comercio.pdf)) |
| Cannot pay | Nómina with a declaración jurada de no pago (DJNP); the minimum payment is the personal contributions (jubilatorio, FONASA, FRL) | By the due date | [BPS, pago de aportes](https://www.bps.gub.uy/10357/pago-de-aportes.html) |
| FONASA annual return, servicios personales | Annual declaration | 16 April (digits 0 to 2), 23 April (3 to 5), 30 April (6 to 9), 2026, available from 9 February | 2026 BPS calendar |

The monthly nómina is a BPS declaration; it is not DGI form 1102, which is the IRPF annual return.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late-payment fine, nómina on time with DJNP | 2.5% (up to 5 working days late) / 5% (up to 90 days) / 10% (after) | [BPS, multas y recargos](https://www.bps.gub.uy/18132/multas-y-recargos-por-mora.html) |
| Late-payment fine, no nómina on time | 5% / 10% / 20% | same |
| Recargo, monthly, capitalised every four months | 0.90% from January 2026; 0.80% from May 2026 | [BPS, valores históricos](https://www.bps.gub.uy/5479/valores-historicos.html) |
| Nómina late | 0.1 or 0.25 UR per worker (0.2 or 0.5 UR on repeat), capped at 5 UR where only the payment or DJNP was late | [BPS, multa por nómina](https://www.bps.gub.uy/10366/multa-por-nomina.html) |
| Personal contributions withheld and not paid | Criminal complaint for apropiación indebida | [BPS, pago de aportes](https://www.bps.gub.uy/10357/pago-de-aportes.html) |

## Cross-border points

- **Posting abroad**: under 183 days the worker stays in BPS unless an agreement's posting rule applies; longer, worker and employer may agree to stay for up to five years (Ley 20.130 art. 3(6)).
- **Foreign employer without a permanent establishment**: the worker contributes as non-dependent on real pay, unless covered in the employer's country under an agreement (Ley 20.130 art. 3(7)).
- **Free-zone foreign staff** who stay outside BPS: see [uy-cross-border](uy-cross-border.md) for their IRNR option.

## Two worked examples that recompute

### Example 1: part-time employee on UYU 15,000, spouse without own health cover

Lucía works part time in a shop for UYU 15,000 a month in 2026. Her husband has no SNIS cover of his own; they have no children.

Her pay is up to 2.5 BPC (UYU 17,160), so FONASA is the lower band, and the spouse line applies: 5%. Personal contributions: jubilatorio 15% = 2,250; FONASA 5% = 750; FRL 0.10% = 15; total UYU 3,015. Employer: jubilatorio 7.5% = 1,125; FONASA 5% = 750; FRL 15; FGCL 3.75; total UYU 1,893.75. BPS receives UYU 4,908.75 for the month. Her pay is below 7 BPC, so no IRPF is withheld (see [uruguay-payroll](uruguay-payroll.md)).

```oa-check
name: Lucía, UYU 15,000, spouse without SNIS, below 2.5 BPC
inputs:
  gross: 15000
  bpc: 6864
steps:
  - band_edge: 2.5 * bpc
  - fonasa_rate: 0.05
  - ee_total: gross * 0.15 + gross * fonasa_rate + gross * 0.001
  - er_total: gross * 0.075 + gross * 0.05 + gross * 0.001 + gross * 0.00025
  - to_bps: ee_total + er_total
expected:
  band_edge: 17160.00
  ee_total: 3015.00
  er_total: 1893.75
  to_bps: 4908.75
```

### Example 2: sole trader without employees, category 1, and the effect of health cover through a job

Pablo runs an empresa unipersonal (Industria y Comercio) with no employees, in category 1 (11 BFC). He has no spouse and no children.

The base is 11 x 1,847.96 = UYU 20,328 (rounded as in the BPS table). Jubilatorio and FRL are 22.6% of it, UYU 4,594. As a FONASA beneficiary (SS 15) his total is UYU 8,833 a month, so the health part is UYU 4,239; for 2026 he pays UYU 105,996.

If he also took a dependent job that gives him SNIS cover (SS 2), his business minimum drops to UYU 5,143 a month: UYU 44,280 less over the year. The jubilatorio and FRL part stays the same; only the health part changes.

```oa-check
name: Pablo, unipersonal category 1, SS 15 against SS 2, 2026
inputs:
  bfc: 1847.96
  categories_bfc: 11
  total_ss15: 8833
  total_ss2: 5143
steps:
  - base: round(categories_bfc * bfc, 0)
  - pension_frl: round(base * 0.226, 0)
  - health_ss15: total_ss15 - pension_frl
  - annual_ss15: total_ss15 * 12
  - annual_saving_with_job_cover: (total_ss15 - total_ss2) * 12
expected:
  base: 20328
  pension_frl: 4594
  health_ss15: 4239
  annual_ss15: 105996
  annual_saving_with_job_cover: 44280
```

## Ask the client first

1. Dependent or owner: employee, unipersonal titular, SRL partner or sociedad de hecho partner, and whether there are employees.
2. Month of the contribution: the ceiling changed in February 2026 and the cuota mutual in July 2026.
3. Pension regime: first job before or after 1 December 2023; AFAP mixed regime; any art. 8 option.
4. Family and health cover: spouse or partner and whether they have their own SNIS cover; children under 18 or with a disability; for owners, whether a dependent job already gives SNIS cover.
5. Pay for the month without aguinaldo (for the FONASA band), and the aguinaldo separately.
6. BPS affiliation (Industria y Comercio or another fund) and the category of an owner.

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 16.713, IMPO consolidated text: arts. 7 and 8 (levels, option) and 181 to 183 (rates) read | https://www.impo.com.uy/bases/leyes/16713-1995 | 2026-11-11 |
| Ley 20.130, IMPO consolidated text: arts. 1 to 9 and 18 to 28 read (inclusion, posting, foreign employers, new entrants' rates, pillar split) | https://www.impo.com.uy/bases/leyes/20130-2023 | 2026-11-11 |
| Ley 18.211, IMPO consolidated text: arts. 61 to 63 read (FONASA rates, user threshold, refund) | https://www.impo.com.uy/bases/leyes/18211-2007 | 2026-11-11 |
| Decreto 11/026, art. 1 read: BPC 2026 | https://www.impo.com.uy/bases/decretos/11-2026 | 2026-11-11 |
| BPS, tasas de aporte jubilatorio page, read in full | https://www.bps.gub.uy/835/tasas.html | 2026-11-11 |
| BPS, tasas FONASA page (updated 23 October 2026), read in full including the CCM formula | https://www.bps.gub.uy/10314/tasas-fonasa.html | 2026-11-11 |
| BPS, FRL page (updated 21 October 2026), read in full | https://www.bps.gub.uy/10322/fondo-reconversion-laboral-frl.html | 2026-11-11 |
| BPS, FGCL page, read in full | https://www.bps.gub.uy/15668/fondo-de-garantia-de-creditos-laborales.html | 2026-11-11 |
| BPS, topes de cotización page, read in full | https://www.bps.gub.uy/10306/topes-de-cotizacion.html | 2026-11-11 |
| BPS, valores actuales, October and November 2026 columns read (BFC, BPC, cuota mutual, CPE, topes, niveles, UR, recargo) | https://www.bps.gub.uy/5478/valores-actuales.html | 2026-11-11 |
| BPS, valores históricos, 2025 and 2026 entries read for tope C, nivel B, BFC, cuota mutual and recargo | https://www.bps.gub.uy/5479/valores-historicos.html | 2026-11-11 |
| BPS, aportes mínimos Industria y Comercio (vigencia enero 2026), all tables read: unipersonales, SRL, sociedad de hecho | https://www.bps.gub.uy/6665/industria-y-comercio.html | 2026-11-11 |
| BPS, pago de aportes page read (what the payment covers, minimum payment, DJNP) | https://www.bps.gub.uy/10357/pago-de-aportes.html | 2026-11-11 |
| BPS, declarar al personal page read | https://www.bps.gub.uy/818/declarar-al-personal.html | 2026-11-11 |
| BPS, Guía de obligaciones Industria y Comercio (January 2025 edition, page updated 21 May 2026), all pages read: companies with and without employees, alta deadline, billing | https://www.bps.gub.uy/bps/file/10291/13/guia---industria-y-comercio.pdf | 2026-11-11 |
| BPS, calendario de vencimientos 2026 (Resolución de Directorio 37-15/2025), full table and FONASA annual return note read | https://www.bps.gub.uy/bps/file/23709/1/calendario-de-vencimientos-2026.pdf | 2026-11-11 |
| BPS, multas y recargos por mora page read | https://www.bps.gub.uy/18132/multas-y-recargos-por-mora.html | 2026-11-11 |
| BPS, multa por nómina page read | https://www.bps.gub.uy/10366/multa-por-nomina.html | 2026-11-11 |

Not yet confirmed: the CCM per worker in practice; the BSE work-accident premium (not a BPS contribution; varies by risk); socio vitalicio FONASA rates (one row of the BPS table is inconsistent); employer rates of public bodies; the rules for moving between ficto categories over time; monotributo, the régimen de aportación gradual and rural minimums; the AFAP-side split for workers who used the art. 8 option in the reform regime; whether workers outside the AFAP regime have any ceiling; how FONASA applies to an owner who also has employees.

> Contributed by Michael Cutajar.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uruguay-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uruguay-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
