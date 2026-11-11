---
name: cl-income-tax
description: "Chile individual income tax for tax year 2026 (año comercial 2026, declared in Operación Renta, año tributario 2027) under DL 824 (Ley sobre Impuesto a la Renta). Covers residence and the three-year rule for foreigners, the Impuesto Global Complementario (IGC) scale of 0% to 40% in UTA, the Impuesto Único de Segunda Categoría (IUSC) withheld monthly from wages in UTM, the December 2026 UTM of CLP 72,802 and UTA of CLP 873,624, self-employed honorarios (art. 42 No. 2) with the 15.25% boleta withholding for 2026, gastos presuntos (30% capped at 15 UTA) against gastos efectivos, the art. 47 reliquidation for two employers, mortgage interest (art. 55 bis), the education credit (art. 55 ter), APV under art. 42 bis, the IDPC credit and 35% restitution on dividends, Form F22 codes, the April 2027 deadline and Código Tributario penalties. Trigger on: impuesto global complementario 2026, segunda categoría, boleta de honorarios, gastos presuntos, Operación Renta 2027, F22, reliquidación, Chile i"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cl-income-tax"
  jurisdiction: "CL"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Chile: individual income tax, employees and honorarios (2026) v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers the annual income tax of an individual for the 2026 calendar year: employees taxed by monthly withholding (IUSC), independent workers who issue boletas de honorarios, and anyone who must file the annual Impuesto Global Complementario (IGC) return, Form F22, in April 2027. In Chile the income year is the "año comercial" 2026 and the filing year is the "año tributario" (AT) 2027.

Linked skills, not repeated here:

- [cl-social-contributions](cl-social-contributions.md): the pension, health and insurance contributions that the boleta withholding pays first, and their rates.
- [cl-corporate-income-tax](cl-corporate-income-tax.md): the first category tax (IDPC) of companies and the Pro Pyme regime.
- [cl-vat-return](cl-vat-return.md): IVA and Form F29.

**Which text of the law.** DL 824, Ley sobre Impuesto a la Renta (LIR), version of 17 October 2026 on LeyChile. Ley 21.850 (Reconstrucción Nacional, published 17 October 2026) changes the first category rate, the IDPC restitution and the art. 107 capital-gains tax, but its transitory articles keep the 2026 income year on the old rules (see Cross-border points and the corporate skill). Penalties and interest come from DL 830, Código Tributario (CT), version of 17 October 2026.

## Who this applies to

- **Residents.** A person domiciled or resident in Chile pays tax on income from any source, in Chile or abroad (LIR art. 3). A resident is anyone who stays in Chile more than 183 days, continuous or not, within any 12-month period (CT art. 8 No. 8).
- **Foreigners in their first three years.** A foreigner who becomes domiciled or resident is taxed only on Chilean-source income for the first three years from arrival; the Director Regional may extend this in qualified cases (LIR art. 3, second paragraph).
- **Non-residents.** Taxed only on Chilean-source income, through the Impuesto Adicional, not the IGC (LIR art. 3, arts. 58 to 60). Out of scope here.
- **Employees, pensioners (art. 42 No. 1).** Wages, salaries, bonuses and pensions pay the IUSC, withheld by the payer each month (arts. 43 No. 1 and 74 No. 1). The IUSC is final ("único") for that income (art. 43).
- **Independent workers (art. 42 No. 2).** Liberal professions and any "ocupación lucrativa" where personal work based on knowledge of a science, art, trade or technique predominates over the use of capital goods, plus societies of professionals (art. 42 No. 2). Honorarios are taxed in the IGC when received ("percibidas", art. 43 No. 2).
- **Who must file F22.** Every IGC taxpayer whose art. 54 income, before any deduction, exceeds the exempt band of 13.5 UTA (CLP 11,793,924 for 2026). An employee whose only income is wages from one payer, or other IGC-exempt income, does not file (art. 65 No. 3). An employee with two or more simultaneous employers must reliquidate (art. 47, art. 65 No. 5).
- **Out of scope.** Companies and individual entrepreneurs keeping accounts under the first category (see cl-corporate-income-tax), presumed-income farmers, transport and mining regimes, the art. 52 bis tax on senior public officials, and the Impuesto Adicional.
- **Chile has no "RIF" regime.** A request that names one (a Mexican regime) is about another country; ask which regime is meant.

## Rates, bands and thresholds

The IGC scale is in UTA; the IUSC scale is the same scale in UTM, applied each month. The UTA for the IGC is the UTM of the last month of the year, December 2026, times 12 (CT art. 8 No. 10). SII published December 2026 as UTM CLP 72,802 and UTA CLP 873,624. CLP amounts below are those multiples; the statute fixes the UTA multiple, the peso figure follows.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| UTM December 2026 (used for the December IUSC and the 2026 IGC) | CLP 72,802 | 2026 | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm |
| UTA December 2026 (UTM x 12) | CLP 873,624 | 2026 | same |
| UTM January to November 2026 (for the monthly IUSC of each month) | Jan 69,751; Feb 69,611; Mar 69,889; Apr 69,889; May 70,588; Jun 71,506; Jul 71,649; Aug 71,649; Sep 71,721; Oct 72,151; Nov 72,440 | 2026 | same |
| IGC band: up to 13.5 UTA (CLP 11,793,924) | Exempt; amount to deduct 0 | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 52) |
| IGC band: over 13.5 to 30 UTA (CLP 26,208,720) | 4%; deduct 0.54 UTA (CLP 471,756.96) | 2026 | same, art. 52 |
| IGC band: over 30 to 50 UTA (CLP 43,681,200) | 8%; deduct 1.74 UTA (CLP 1,520,105.76) | 2026 | same, art. 52 |
| IGC band: over 50 to 70 UTA (CLP 61,153,680) | 13.5%; deduct 4.49 UTA (CLP 3,922,571.76) | 2026 | same, art. 52 |
| IGC band: over 70 to 90 UTA (CLP 78,626,160) | 23%; deduct 11.14 UTA (CLP 9,732,171.36) | 2026 | same, art. 52 |
| IGC band: over 90 to 120 UTA (CLP 104,834,880) | 30.4%; deduct 17.80 UTA (CLP 15,550,507.20) | 2026 | same, art. 52 |
| IGC band: over 120 to 310 UTA (CLP 270,823,440) | 35%; deduct 23.32 UTA (CLP 20,372,911.68) | 2026 | same, art. 52 |
| IGC band: over 310 UTA | 40%; deduct 38.82 UTA (CLP 33,914,083.68) | 2026 | same, art. 52 |
| IUSC, monthly, same bands in UTM (art. 43 No. 1); December 2026 table | Exempt to CLP 982,827; 4% to 2,184,060 (deduct 39,313.08); 8% to 3,640,100 (126,675.48); 13.5% to 5,096,140 (326,880.98); 23% to 6,552,180 (811,014.28); 30.4% to 8,736,240 (1,295,875.60); 35% to 22,568,620 (1,697,742.64); 40% above (2,826,173.64) | Dec 2026 | https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2026.htm |
| Boleta de honorarios withholding (art. 74 No. 2) and PPM of independents (art. 84 b), services provided in 2026 | 15.25% of the gross fee | 2026 | https://www.sii.cl/destacados/boletas_honorarios/ ; Ley 21.133 art. 5 transitorio: https://www.bcn.cl/leychile/navegar?idNorma=1128420 |
| Same withholding, 2027 and 2028 onward | 16% (2027); 17% (2028, the permanent rate in art. 74 No. 2) | 2027-2028 | https://www.sii.cl/noticias/2025/261225noti01smn.htm |
| Gastos presuntos (art. 42 No. 2 workers acting individually) | 30% of gross annual honorarios, capped at 15 UTA (CLP 13,104,360) | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 50) |
| APV deduction (art. 42 bis, régimen of DL 3.500 art. 20 L letra b) | Up to 50 UF a month through the employer; up to 600 UF a year in total, UF at 31 December | 2026 | same, art. 42 bis Nos. 1, 2; art. 50 for independents |
| APV under DL 3.500 art. 20 L letra a) (no deduction) | State bonus of 15% of the saving on retirement, capped at 6 UTM a year | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=7147 (DL 3.500 art. 20 O) |
| Mortgage interest deduction (art. 55 bis) | Lower of interest paid and 8 UTA (CLP 6,988,992); full below 90 UTA of gross income; none above 150 UTA; between, interest x (250 - 1.667 x income in UTA)% | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 55 bis) |
| Education credit (art. 55 ter) | 4.4 UF per child a year, UF at year end; children up to 25, 85% attendance; parents' combined income up to 792 UF | 2026 | same, art. 55 ter |
| IGC exemption for small capital income (art. 57) | Art. 20 No. 2 income up to 20 UTM of December (CLP 1,456,040), fund-redemption gains up to 30 UTM (CLP 2,184,060), only where the other income is wages (art. 42 No. 1) or art. 22 income | 2026 | same, art. 57 |
| IGC rate cap where the art. 14 credit applies | Up to 44.45% | 2026 | same, art. 52 last paragraph |
| Restitution of IDPC credit from art. 14 A companies (SAC register) | 35% of the credit, a higher IGC (F22 code 1035) | Dividends and withdrawals of 2026 | same, art. 56 No. 3; Ley 21.850 art. 5 transitorio: https://www.bcn.cl/leychile/navegar?idNorma=1229250 |
| Credit on withdrawals and dividends with restitution above 310 UTA (art. 56 No. 4) | 5% of the part above 310 UTA (CLP 270,823,440), grossed up | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 56 No. 4) |
| Penal interest on late payment, 1 July to 31 December 2026 (CT art. 53) | 7.70% a year (CMF rate 4.20% plus 3.5%), 0.0213888889% a day | Jul-Dec 2026 | https://www.sii.cl/valores_y_fechas/otros_valores/tasa_interes_penal_diario.html |

**How the IGC works.** Tax = base x rate of the band - amount to deduct of the band, all in the same unit. The "amount to deduct" turns the marginal scale into one multiplication: for a base of 24.04 UTA, 24.04 x 4% - 0.54 = 0.4216 UTA, which equals 4% of the 10.54 UTA above the exempt band.

## The base

The IGC base is built on F22 lines 1 to 24 (codes below from the F22 for AT 2026, the latest form SII has published; check the AT 2027 form when it appears).

**1. Gross income (renta bruta global, art. 54).** All IGC income of the year: honorarios received (line 7, code 110), wages and pensions (line 13, code 1098), withdrawals and dividends (lines 1 and 2), interest and other capital income under art. 20 No. 2 (line 8), gains under art. 17 No. 8 (line 8), rent determined by contract (line 5), foreign-source income (line 12). Wages enter only to set the rate: the IUSC already withheld is credited back (art. 54 No. 3, line 46, code 162). Amounts are updated by CPI from the month before receipt to 30 November 2026 (art. 54 No. 3, penultimate paragraph).

**2. Honorarios (Recuadro N° 1).** Gross fees with withholding (code 461, retention in code 492) plus fees without withholding (code 545) plus foreign fees and their gross-up (codes 1650, 856) give total gross income (code 547). Then deduct, in this order on the form: APV under art. 42 bis (code 770), qualifying social donations (code 872), and one of:

- **Gastos efectivos** (code 465): actual expenses necessary to produce the income, under the first category rules (art. 31) so far as they fit, with the documents to prove them. The independent's own pension contributions are deductible as an expense under this method (art. 50, first paragraph).
- **Gastos presuntos** (code 494): only for a worker who practises individually, not a society of professionals. 30% of gross annual income (code 547), capped at 15 UTA (CLP 13,104,360 for 2026). No receipts are needed, and the cotizaciones paid are **not** deductible on top (art. 50, last paragraph, added by Ley 21.133).

The result is total honorarios (code 467), carried to line 7. Honorarios are taxed when received, not when billed (art. 43 No. 2).

**3. Deductions from gross income (art. 55, lines 15 to 23).** Property tax paid in the year on property whose income is in the base (art. 55 a), code 166); the pension contributions of an individual entrepreneur or partner in a company with full accounts (art. 55 b), code 111); mortgage interest under art. 55 bis (line 21, code 750); APV under art. 42 bis for employees (line 23, code 765). The result is the annual base (line 24, code 170).

**4. Tax (line 25, code 157).** Apply the art. 52 scale at the December 2026 UTA. Add, where they arise, the restitution of IDPC credit (line 29, code 1035) and the tax on art. 21 items (line 30).

**5. Credits, in the order of art. 56.** First those that cannot be refunded (for example IDPC without refund right, code 608; the 5% credit of art. 56 No. 4, code 1636; the education credit, code 895), then the refundable ones: IUSC paid on wages (code 162), IDPC with refund right (code 610). A non-refundable credit larger than the tax is lost; only the excess of the art. 56 No. 3 credit (on income actually taxed at IDPC) and of the No. 2 credit is refunded (art. 56, last paragraphs).

**6. Payments on account (lines 85 and 91).** The boleta withholding of 15.25% (code 198) and any PPM the worker paid himself in Form F29 (code 1905). These are credits against the tax, never expenses.

**7. Cotizaciones charge (line 106, code 900).** The pension, health and insurance contributions of the independent worker are charged in the same F22 against the withholding and PPM. They are computed on 80% of gross honorarios (DL 3.500 art. 90); the rates and the opt-outs are in [cl-social-contributions](cl-social-contributions.md). What is left after tax and cotizaciones is refunded (code 87) or paid (code 91).

**Two employers (art. 47).** A worker paid by two or more employers at the same time in 2026 must reliquidate: add all taxable wages, updated by CPI, apply the annual scale at the December UTA, and credit the IUSC withheld. If the result is no higher tax, reliquidation is not compulsory. Any employee may reliquidate voluntarily, and must do so to claim art. 55 bis interest or the art. 55 ter credit (arts. 47, 55 bis, 55 ter).

**Capital gains in 2026.** The 10% single tax of art. 107 on listed shares and fund units still applies to 2026 sales: Ley 21.850 makes those gains "no renta" only from 1 January 2027 (art. 9 transitorio No. 3). Other share gains go to the IGC under art. 17 No. 8; a person not keeping accounts may offset losses on the same kind of investment in the year (art. 54 No. 1).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Employer withholds and pays IUSC; client company withholds 15.25% on boletas | Monthly, declared in F29 (codes 48 and 151) | LIR arts. 74 Nos. 1, 2 and 79 |
| Independent whose client did not withhold (a person, or no accounts) pays PPM of 15.25% itself | Monthly, F29 code 152 | LIR art. 84 b); SII honorarios help page |
| Annual return F22 for 2026, with payment of any balance | During April 2027, so by 30 April 2027 | LIR arts. 69 and 72 |
| Balance due is paid updated by CPI | From November 2026 to the month before the legal payment date | LIR art. 72 |
| Refund of an overpayment | Within 30 days after the normal deadline; a late return is refunded in the following month | LIR art. 97 |
| Sporadic income not fully withheld | Within the month after receipt | LIR art. 69 No. 3 |

**How to file.** On sii.cl, log in with RUT and Clave Tributaria (or ClaveÚnica), open Servicios Online, Declaración de Renta, and use the proposal SII builds from the sworn statements (declaraciones juradas) of employers, clients and banks. Check Recuadro N° 1 against your boletas (codes 461, 492, 545), choose gastos presuntos (494) or efectivos (465), check the lines 1 to 24 base, the credits and the cotizaciones charge in code 900, then submit. The result appears in code 305: a refund (code 87, with the bank account in codes 301, 306 and 780) or an amount to pay (code 91). Keep the F22 folio and the payment receipt. SII cross-checks codes 461 and 545 against the clients' returns and the F29 PPM, and lets you correct before it settles.

**Records.** Keep boletas, expense documents and certificates while SII can review the year: three years from the payment deadline, six years where no return was filed or it was maliciously false (CT art. 200).

## Penalties and interest

All under the Código Tributario (DL 830).

- **Late return that is the basis of a tax** (CT art. 97 No. 2): 10% of the tax resulting, if the delay is up to 5 months; then 2% more for each month or part of a month, up to 30% of the tax owed.
- **Late return with no immediate payment** (for example a refund return): 1 UTM to 1 UTA (art. 97 No. 2, last paragraph).
- **Incomplete or wrong return** that could lead to lower tax, unless due diligence is shown: 5% to 20% of the tax difference (art. 97 No. 3).
- **Maliciously false or incomplete return:** 100% to 300% of the tax evaded, and imprisonment (art. 97 No. 4).
- **Late payment of a tax withheld** (the employer's IUSC, the client's boleta withholding): 10% of the tax, plus 2% a month, up to 30%; 20% and 60% where SII detects the omission in an audit (art. 97 No. 11).
- **Not issuing a boleta de honorarios** when required: 50% to 500% of the operation, at least 2 UTM and at most 40 UTA, plus closure of up to 20 days (art. 97 No. 10).
- **Late payment:** the tax is updated by CPI (CT art. 53, first paragraph) and bears a daily penal interest equal to the CMF one-year rate plus 3.5%, fixed by SII each semester: 7.70% a year, 0.0213888889% a day, for 1 July to 31 December 2026 (art. 53).

## Cross-border points

- **Foreign income of a resident** is declared (line 12, honorarios codes 1650 and 856). Tax paid abroad gives the credit of art. 41 A (codes 1018, 746); a treaty may change the result. Treaty analysis is not covered here; refer.
- **First three years** after a foreigner arrives: Chilean-source income only (art. 3).
- **Dividends and withdrawals from Chilean companies** carry the IDPC credit (art. 56 No. 3). For a company under art. 14 A, 35% of that credit is restituted (paid back) for withdrawals and dividends of 2026. Ley 21.850 reduces the restitution to 30% for credits of AT 2028, 20% for AT 2029 and nothing after (art. 5 transitorio), and cuts the first category rate from 27% (income of 2026) to 23% (from 2029) (art. 6 transitorio). Neither change touches the 2026 income year.
- **Non-residents** pay Impuesto Adicional, withheld at source (arts. 58 to 60, 74 No. 4). Out of scope.

## Two worked examples that recompute

All amounts are assumed already updated by CPI to the form's values. UTA = CLP 873,624 (December 2026).

### Example 1: IT consultant on gastos presuntos

Pablo, resident in Santiago, works alone and issued boletas for CLP 30,000,000 gross in 2026, all to companies, which withheld 15.25% (CLP 4,575,000). He has no other income and chooses gastos presuntos.

Gastos presuntos are 30% of CLP 30,000,000 = CLP 9,000,000, under the 15 UTA cap of CLP 13,104,360. Total honorarios (code 467) are CLP 21,000,000, which is 24.04 UTA: the 4% band. IGC = 21,000,000 x 4% - 0.54 x 873,624 = 840,000 - 471,756.96 = CLP 368,243.04 (code 157).

Credits: the withholding of CLP 4,575,000 (code 198). Before the cotizaciones charge, the balance is a CLP 4,206,756.96 credit. The cotizaciones on 80% of CLP 30,000,000 are then charged in code 900 (rates in cl-social-contributions); what remains is refunded. His own cotizaciones are not deducted from the base, because he chose gastos presuntos (art. 50).

The same check proves the band arithmetic on two further cases: an employee's December 2026 monthly IUSC on CLP 3,000,000 of taxable pay (8% band: CLP 113,324.52, matching SII's table), and an IGC base of 400 UTA in the 40% band (121.18 UTA).

```oa-check
name: CL IGC 2026, honorarios with gastos presuntos, 4% band
inputs:
  uta: 873624
  utm_dec: 72802
  gross: 30000000
  withholding_rate: 0.1525
  monthly_pay: 3000000
  high_base_uta: 400
steps:
  - presuntos: min(gross * 0.30, 15 * uta)
  - base: gross - presuntos
  - base_uta: round(base / uta, 2)
  - igc: round(base * 0.04 - 0.54 * uta, 2)
  - withheld: gross * withholding_rate
  - balance_before_cotizaciones: igc - withheld
  - iusc_december: round(monthly_pay * 0.08 - 1.74 * utm_dec, 2)
  - igc_top_band_uta: high_base_uta * 0.40 - 38.82
expected:
  presuntos: 9000000
  base: 21000000
  base_uta: 24.04
  igc: 368243.04
  withheld: 4575000
  balance_before_cotizaciones: -4206756.96
  iusc_december: 113324.52
  igc_top_band_uta: 121.18
```

### Example 2: architect deciding between gastos presuntos and gastos efectivos

Sofía, an architect working alone in Valparaíso, received CLP 45,000,000 of honorarios in 2026. She can prove CLP 19,400,000 of necessary expenses (studio rent, software, subcontractors, travel), not counting her own cotizaciones. Which method should she declare?

- **Gastos presuntos:** 30% of 45,000,000 is CLP 13,500,000, above the cap, so CLP 13,104,360. Base CLP 31,895,640 = 36.51 UTA, the 8% band. IGC = 31,895,640 x 8% - 1.74 x 873,624 = CLP 1,031,545.44.
- **Gastos efectivos:** base CLP 25,600,000 = 29.30 UTA, the 4% band. IGC = 25,600,000 x 4% - 0.54 x 873,624 = CLP 552,243.04.

The figure that decides is whether provable expenses exceed the presuntos deduction, here CLP 19,400,000 against CLP 13,104,360. Efectivos save CLP 479,302.40, and under efectivos her own pension contributions would also be deductible (art. 50). Had she proved only CLP 10,000,000, presuntos (CLP 13,104,360) would win. Efectivos need every expense documented; an expense she cannot prove comes out.

```oa-check
name: CL IGC 2026, presuntos against efectivos, architect CLP 45m
inputs:
  uta: 873624
  gross: 45000000
  efectivos: 19400000
  low_efectivos: 10000000
steps:
  - presuntos: min(gross * 0.30, 15 * uta)
  - base_presuntos: gross - presuntos
  - base_efectivos: gross - efectivos
  - igc_presuntos: round(base_presuntos * 0.08 - 1.74 * uta, 2)
  - igc_efectivos: round(base_efectivos * 0.04 - 0.54 * uta, 2)
  - saving_efectivos: igc_presuntos - igc_efectivos
  - low_case_better_deduction: max(presuntos, low_efectivos)
expected:
  presuntos: 13104360
  base_presuntos: 31895640
  base_efectivos: 25600000
  igc_presuntos: 1031545.44
  igc_efectivos: 552243.04
  saving_efectivos: 479302.40
  low_case_better_deduction: 13104360
```

## Ask the client first

1. Where did the client live in 2026, and for how many days was he in Chile in any 12-month period? If a foreigner, when did he arrive (the three-year rule)?
2. What income did he have: wages (how many employers at the same time), boletas de honorarios (gross, and whether each client withheld), dividends or withdrawals (and the company's regime, 14 A or Pro Pyme), interest, rent, share or property sales, foreign income?
3. For honorarios: does he work alone or through a society of professionals, and can he document actual expenses? (This decides gastos presuntos against gastos efectivos; never assume one.)
4. Did he pay his own PPM in F29, and which cotizaciones apply to him (age, opt-out, coverage through employment)? See cl-social-contributions.
5. Does he have APV, and under which DL 3.500 art. 20 L regime (letra a, bonus; letra b, deduction); a mortgage loan with interest paid in 2026; children in school, and both parents' combined income for the art. 55 ter test?
6. If the answer turns on a treaty, foreign tax paid, or company withdrawals with credits, collect the certificates (the company's dividend certificate, foreign tax receipts) or refer.

## Sources

| Source | URL | Read on |
|---|---|---|
| DL 824, Ley sobre Impuesto a la Renta, LeyChile version of 17 Oct 2026 (read in the LeyChile XML export): arts. 3, 20, 42, 42 bis, 43, 47, 50, 52, 54, 55, 55 bis, 55 ter, 56, 57, 65, 69, 72, 74, 84, 97 | https://www.bcn.cl/leychile/navegar?idNorma=6368 | 2026-11-11 |
| Ley 21.850, Reconstrucción Nacional (DO 17 Oct 2026): arts. 8 and 9 (LIR changes) and transitory arts. 5, 6 and 9 (IDPC rate 27% for 2026, restitution phase-out, art. 107 from 1 Jan 2027) | https://www.bcn.cl/leychile/navegar?idNorma=1229250 | 2026-11-11 |
| Ley 21.133 (2019): art. 5 (art. 50 change, 17% rate) and art. 5 transitorio (0.75 point yearly increase of the withholding) | https://www.bcn.cl/leychile/navegar?idNorma=1128420 | 2026-11-11 |
| DL 3.500: art. 20 L (APV regimes a and b), art. 20 O (15% bonus, 6 UTM cap), art. 90 (80% base for independents) | https://www.bcn.cl/leychile/navegar?idNorma=7147 | 2026-11-11 |
| DL 830, Código Tributario, LeyChile version of 17 Oct 2026: art. 8 Nos. 8 and 10, art. 53, art. 97 Nos. 2, 3, 4, 10, 11, art. 200 | https://www.bcn.cl/leychile/navegar?idNorma=6374 | 2026-11-11 |
| Read for the figures named: SII, UTM, UTA and IPC 2026 table (December 2026 UTM 72,802, UTA 873,624, and each month) | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm | 2026-11-11 |
| Read for the figures named: SII, Impuesto Único de Segunda Categoría 2026, monthly tables (December and November read in full) | https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2026.htm | 2026-11-11 |
| Read for the figures named: SII, Boleta de Honorarios 2026 page: withholding 15.25% from 1 Jan 2026; 16% in 2027 | https://www.sii.cl/destacados/boletas_honorarios/ | 2026-11-11 |
| Read for the figures named: SII news of 26 Dec 2025: 15.25% for 2026, 16% for 2027, 17% for 2028 | https://www.sii.cl/noticias/2025/261225noti01smn.htm | 2026-11-11 |
| Read for the figures named: SII FAQ 001.140.8398.009 (updated 3 Aug 2026): 2026 withholding 15.25% with the CLP 100,000 example | https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_8398.htm | 2026-11-11 |
| Read for the figures named: SII, Formulario 22 for AT 2026 (codes of Recuadro N° 1, lines 1 to 118) | https://www.sii.cl/ayudas/formularios/f22_at2026.pdf | 2026-11-11 |
| Read for the figures named: SII, Formulario 29 (codes 48, 151, 152 for withholding and PPM) | https://www.sii.cl/formularios/imagen/F29.pdf | 2026-11-11 |
| Read for the figures named: SII, daily penal interest table (certificate 06/2026: 4.20% + 3.5% = 7.70%, 1 Jul to 31 Dec 2026) | https://www.sii.cl/valores_y_fechas/otros_valores/tasa_interes_penal_diario.html | 2026-11-11 |
| Read for the figures named: SII news of 19 Oct 2026 on Ley 21.850 (calendar of the measures, IDPC 25.5% / 24% / 23% for AT 2028 to 2030) | https://www.sii.cl/noticias/2026/191026noti01pcr.htm | 2026-11-11 |

Not yet confirmed: the exact AT 2027 Operación Renta calendar (SII sets by resolution the days within April, and any later date for returns without payment; not yet published); the AT 2027 F22 codes (the codes above are from the AT 2026 form); the UF at 31 December 2026, which sets the peso value of the 600 UF APV cap, the 4.4 UF education credit and the 792 UF income test; whether SII's circular on Ley 21.850 changes the 35% restitution for credits allocated in April 2027 (the transitory article keeps the rules in force to 31 December 2026 for credits accumulated to that date); whether gastos efectivos require the independent to keep a full accounting record (SII practice, not read in the law).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cl-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cl-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
