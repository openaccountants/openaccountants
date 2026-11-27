---
name: portugal-payroll
description: "Portugal employee payroll for 2026: IRS withholding by region and payment date, November adjustments, Social Security, meal allowances, IRS Jovem, holiday and Christmas subsidies, filing and worked payroll cases. Trigger on Portuguese payroll, retenção na fonte, TSU, DMR, duodécimos and salário líquido. Establish residence, family situation, actual pay components, eligibility and reporting model before calculating. Specialist and unverified cases require the explicit partner referral in the body."
version: 1.4
jurisdiction: PT
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - payroll-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Portugal payroll (tax year 2026) v1.4

Prepare the payroll using the employee's residence, family declaration and actual payment date. Ordinary general-regime Social Security is employee 11% and employer 23.75% on the contributory base; IRS uses its own gross remuneration base. The November adjustment changes withholding, not the employee's contractual salary. See the cited rules below.

Related Guides: `payroll-workflow-base`; `pt-social-contributions` for contributions in depth; `pt-irs-employees-investment` for annual assessment; `pt-cross-border` for residence, treaties and postings; `pt-nhr-ifici` for special regimes; `portugal-bookkeeping` for payroll journals and subsidy accruals. These links do not resolve a hold below.

## Who this applies to

Employers paying Category A employment income. Withhold on payment or availability, subject to the statutory exceptions (CIRS art. 99). Ask for the personal/family declaration at the start or before first payment, and obtain later changes. Fixed pay plus other Category A amounts paid in the month form monthly remuneration; add payments for periods shorter than a month. Do not subtract employee Social Security before applying the withholding table. Benefits in kind and third-party tips have separate treatment; at the employee's request they can enter withholding (arts. 99 and 99-C). Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99.aspx and https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99c.aspx.

**Select the region and table.** Mainland residents use Despacho 233-A/2026; Azores residents Despacho 1179/2026 (AT Circular 3/2026); Madeira residents Despacho 19/2026, as rectified (AT Circular 2/2026). Table I is single without dependants or married two earners; II single with dependants; III married one earner; IV–VII employees with disability; VIII–XI pensions. The mainland Table I below must not be used for another table or region. Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular-3-2026.pdf; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular_2_2026.pdf.

For married one earner, spouses must not be judicially separated and either only one has aggregated income or one earns at least 95% of the couple's aggregated income. Qualifying unmarried partners use married tables. Without family details, assume no dependants (CIRS art. 99-B; despacho points 8–9). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99b.aspx and https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf.

| Payments in 2026 | Operative table rule | Official source |
|---|---|---|
| Mainland, January–October and from December | Ordinary 2026 tables | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12523-a-2026.pdf |
| Mainland, 1–30 November | Apply only 50% of the ordinary table withholding; retain the full amount if monthly income exceeds the upper limit of the penultimate row of the applicable table. This also applies where Christmas subsidy is paid alongside salary, retaining separate withholding. November errors can be rectified through December. | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12523-a-2026.pdf, points 1–9 |
| Azores, January–October and from December | Ordinary regional 2026 tables | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular-3-2026.pdf; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12610-a-2026.pdf |
| Azores, 1–30 November | Same 50% adjustment, penultimate-row exception, multiple-payment coverage and correction through December, using the Azores table | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12610-a-2026.pdf, points 1–9 |
| Madeira, January–October and from December | Ordinary regional 2026 tables | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular_2_2026.pdf; https://at.madeira.gov.pt/ficheiros/IISerie-196-2026-10-29Supl.pdf |
| Madeira, 1–30 November | Same 50% adjustment, penultimate-row exception, multiple-payment coverage and correction through December, using the Madeira table. The former statement that no Madeira order was found is superseded. | https://at.madeira.gov.pt/ficheiros/IISerie-196-2026-10-29Supl.pdf, Despacho 434/2026, points 1–9 |

## Rates, bands and thresholds

**Mainland Table I, ordinary 2026 withholding.** R is monthly gross remuneration subject to withholding. Select the first upper limit that contains R. Calculate R × marginal rate − deduction − (additional deduction × dependants); a negative result means no withholding. Round the final tax down to whole euros (CIRS art. 99-E). For November apply the dated rule above. Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf, point 3 and Table I; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99e.aspx.

| Monthly pay up to (EUR) | Marginal rate | Deduction (EUR) | Additional deduction per dependant (EUR) | Official source |
|---|---|---|---|---|
| 920.00 | 0% | 0 | 0 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf |
| 1,042.00 | 12.50% | 12.50% × 2.60 × (1,273.85 − R) | 21.43 | same |
| 1,108.00 | 15.70% | 15.70% × 1.35 × (1,554.83 − R) | 21.43 | same |
| 1,154.00 | 15.70% | 94.71 | 21.43 | same |
| 1,212.00 | 21.20% | 158.18 | 21.43 | same |
| 1,819.00 | 24.10% | 193.33 | 21.43 | same |
| 2,119.00 | 31.10% | 320.66 | 21.43 | same |
| 2,499.00 | 34.90% | 401.19 | 21.43 | same |
| 3,305.00 | 38.36% | 487.66 | 21.43 | same |
| 5,547.00 | 39.69% | 531.62 | 21.43 | same |
| 20,221.00 | 44.95% | 823.40 | 21.43 | same |
| Over 20,221.00 | 47.17% | 1,272.31 | 21.43 | same |

| Other item | 2026 rule and conditions | Official source |
|---|---|---|
| Mainland Table II | Same pay bands, rates and basic deductions as Table I; additional deduction EUR 34.29 per dependant except the zero row, where it is zero | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf, Table II |
| Mainland Table III | Zero withholding up to EUR 991; additional deduction EUR 42.86 on nonzero rows. Other bands differ: use the full Table III | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf, Table III |
| Azores Table I | Zero up to EUR 966; next row has marginal rate 8.75%. Use the complete regional row, including its deduction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular-3-2026.pdf, Table I |
| Madeira Table I | Zero up to EUR 980; next row has marginal rate 8.72%; over EUR 21,411 the rate is 32.78%, deduction EUR 1,275.30. Use the complete regional table | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular_2_2026.pdf, Table I |
| General-regime Social Security | Total 34.75%, employer 23.75%, employee 11%, subject to special-regime classification | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 53 |
| MOE | Management/administration duties: employer 23.75%, member 11%; other covered statutory-body members: employer 20.3%, member 9.3%. Confirm coverage, exclusions and the actual base; where classification is missing, Check this point with one of our partner accountants | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 61–69 |
| Domestic workers | Without unemployment protection: employer 18.9%, worker 9.4%; with it: 22.3% and 11%. Unemployment protection requires actual earnings under a full-time monthly contract; using actual rather than conventional earnings needs the statutory written agreement and eligibility. Without established coverage/base facts, Check this point with one of our partner accountants | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 116–121 |
| Meal allowance, cash | IRS and Social Security apply to the excess over EUR 6.15 per qualifying day, effective 1 January 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs2.aspx; https://files.diariodarepublica.pt/1s/2026/01/02103/0001100011.pdf, arts. 1 and 3; https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 46(2)(l), (3) |
| Meal vouchers/card | Statutory limit is 70% above cash: EUR 6.15 × 1.70 = EUR 10.455 per day (derived). Do not assume EUR 10.46 is fully exempt; cent rounding is held below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs2.aspx |
| IAS | EUR 537.13 for 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf, arts. 2 and 4 |
| Minimum wage, mainland | EUR 920 a month from 1 January 2026; special reductions/classifications require separate checking | https://diariodarepublica.pt/dr/detalhe/decreto-lei/139-2025-992879809, arts. 2, 3, 7 |
| Minimum wage, Azores | EUR 966, derived as national EUR 920 plus 5% | https://diariodarepublica.pt/dr/detalhe/decreto-legislativo-regional/8-2002-303252, art. 3; https://diariodarepublica.pt/dr/detalhe/decreto-lei/139-2025-992879809 |
| Minimum wage, Madeira | EUR 980 from 1 January 2026 | https://files.diariodarepublica.pt/1s/2026/02/02300/0001400015.pdf, arts. 2 and 4 |

For mainland employees with at least three dependants, reduce the marginal rate by one percentage point in employment Tables I–VII, leaving deductions unchanged (despacho point 5(h)). For a dependant with permanent disability of at least 60%, add EUR 84.82 (single or married one earner) or EUR 42.41 (married two earners). Before payment the employee may elect a multiplier up to three or six respectively (points 5(a), 6–7). A married sole earner whose spouse has no Category A/H income and permanent disability of at least 60% also adds EUR 135.71 (point 5(b)). Do not transfer these mainland procedures to a region without its own operative order. Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf.

## The base

**Separate the two bases.** General-regime contributions use remuneration within Contributions Code arts. 44–48. Base pay, seniority supplements, commissions, regular qualifying premiums, overtime, night pay, holiday pay and holiday/Christmas subsidies enter under art. 46. The ordinary employee calculation has no general wage ceiling; conventional or specially limited bases must be classified separately. Employer-canteen meals are excluded (art. 48(f)). Do not treat all profit shares, travel reimbursements or termination payments as automatically excluded: their classification is held below. Source: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575.

**Autonomous withholding.** Calculate holiday subsidy, Christmas subsidy, overtime and earlier-year remuneration separately from regular monthly pay (CIRS art. 99-C(5)). Subsidy instalments carry the proportional tax on the whole subsidy; earlier-year subsidies are separated by year. Earlier-year remuneration is divided by its covered months to find the rate, then that rate applies to the whole amount. Overtime uses 50% of the effective rate for that month's regular remuneration. Show effective rates separately for each remuneration on the payslip. Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99c.aspx; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf, points 5(f), 10. An exclusively variable remuneration package uses CIRS art. 100 and its annual estimate/cumulative adjustment rules, not Table I; because intermediate bands and estimation facts are not reproduced here, Check this point with one of our partner accountants.

**IRS Jovem.** Up to age 35, not a dependant, with an annual-return election: exemptions are 100% in income year 1, 75% in 2–4, 50% in 5–7, 25% in 8–10, capped annually at 55 × IAS. No-income years pause the count; earlier years as a dependant do not count under the transition. Current/past NHR or IFICI, an art. 12-A election, or an unregularised tax position exclude it. The employer needs the employee's invocation and income-year declaration. Calculate the effective rate on total pay including the exempt portion, then apply it only to the non-exempt part. The withholding exemption limit per payment is derived as 55 × EUR 537.13 / 14 = EUR 2,110.15 to cents; annual cap EUR 29,542.15. Apply the percentage and cap to the exempt portion, including separately calculated subsidies. Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99f.aspx; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf, point 5(g); https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_20274_2025.pdf (method, not its 2025 values).

**Subsidies and leave.** Christmas subsidy is one month's remuneration, by 15 December, pro rata in the admission/termination year and worker-related suspension. Holiday subsidy comprises base pay and payments for the specific mode of work, corresponding to minimum leave, normally paid before leave and proportionally for split leave unless agreed otherwise in writing. Minimum annual leave is 22 working days; admission and cessation rules differ. Thus budget salary plus both subsidies, but do not assume every subsidy equals every component of monthly pay, or that the employer can unilaterally choose twelfths. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475, arts. 238–239, 262–264. Termination entitlements and specialist leave are held below.

**Overtime and night work.** Under Labour Code art. 268, for the first 100 overtime hours annually: working-day first hour/fraction +25%, subsequent +37.5%, rest day/holiday +50%. Beyond 100 hours: +50%, +75%, +100% respectively. Payment is due where expressly ordered beforehand or performed when employer opposition was not foreseeable. Normal work is generally at most eight hours/day and forty/week (art. 203); special working-time arrangements require separate checking. For temporary workload overtime, annual limits are 175 hours at micro/small employers or 150 at medium/large, extendable to 200 by collective instrument; part-time uses its own proportionate/80-hour rule and statutory extensions. Daily limits also apply (art. 228); force-majeure/prevention of serious business harm follows arts. 227(2), 228(4), rather than those ordinary caps. Night pay is normally +25%, but art. 266 allows equivalent collectively agreed substitution and exceptions for predominantly nocturnal activity, public-facing night services or pay already set for night work. The default night interval is 22:00–07:00 only absent a collective definition satisfying art. 223. Source: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475.

## Deadlines and filing

These are ordinary statutory deadlines; use the actual 2026 AT calendar for extensions (for example, the DMR due in August is due on 31 August). Do not treat the AT declaration and the Social Security declaration as a single acceptance. Calendar: https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/calendario_fiscal/Pages/Quadro_res_Decl_2026.aspx.

| Obligation | Deadline / handling | Official source |
|---|---|---|
| AT DMR for ordinary resident employment | By the 10th after payment/availability; includes exempt/non-taxable employment income, withholding, mandatory social/health contributions and union dues | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx, art. 119(1)(c)(i) |
| Correct AT declaration | Within 30 days of an event changing declared income or creating a declaration obligation | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx, art. 119(1)(d) |
| Employee annual statement | By 20 January for prior year; changed facts also require a statement within 15 days | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx, art. 119(1)(b) |
| IRS payment | By the 20th of the month after deduction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs98.aspx, art. 98(3) |
| New SS reporting model | Confirm/correct by the 20th after the remuneration month; silence accepts the system values. The August acceptance/confirmation deadline is the 25th | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021, amended arts. 40(7)–(9), 23-B(2) |
| Transition | Voluntary during 2026 following SS confirmation; effective next month. Old-model submissions are then rejected. Compulsory for all employers from 1 January 2027. Check the employer's actual confirmed effective month | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021, art. 5 |
| Employee + employer SS payment | From the 1st to the 25th of the following month, based on SS data | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021, amended art. 43 |
| Payslip | By payment: employer identification; worker's full name, SS registration number and category; base and other pay; period; deductions; net. Also show effective IRS rates separately | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475, art. 276(3); https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99.aspx, art. 99(9); https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf, point 10 |

An employee may request a higher whole-number rate in writing; only the marginal rate changes, not deductions. Employer withholding errors can be corrected in the first subsequent withholding or following ones, within the year's last withholding period; November corrections also follow the dated orders above. Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs98.aspx, arts. 98(4), (6); https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf, point 5(e).

## Penalties and interest

Late/missing tax declarations fall under RGIT art. 117(1), base fine EUR 150–3,750; corporate/equivalent minimum and maximum limits double under art. 26(4), subject to its general limits. Non-delivery of tax withheld or required to be withheld falls under art. 114: for non-criminal intentional conduct, one to two times the shortfall; negligence 15%–50%, with statutory maximum limits and corporate rules. Do not use the old flat 10% surcharge. Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit26.aspx.

Compensatory tax interest depends on attributable delay (LGT art. 35), calculated daily with its statutory end points/limits, at the legal rate of 4%. General late-payment interest is 7.221% annually from 1 January 2026; LGT art. 44 has special judicial/enforcement rules. Social Security delay uses calendar months or parts under Contributions Code arts. 211–212, at the same general late-interest rate. Do not apply one day-count method to both. Sources: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx; https://diariodarepublica.pt/dr/detalhe/portaria/291-2003-223663; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx; https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668; https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575.

Failure to declare a worker is very serious; under the new model, a correction/declaration omission causing differences in amounts due to the worker is light if remedied within the next 60 days, serious otherwise (Contributions Code art. 40(10)–(11)). Missing statutory subsidy payments are very serious, overtime-premium breaches serious, deficient payslips light (Labour Code arts. 263–264, 268, 276). Sources: https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021; https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475. For an actual fine calculation, company adjustments to SS fines or possible criminal non-remittance under RGIT art. 105, Check this point with one of our partner accountants. Do not infer a criminal conclusion from an amount alone.

## Cross-border points

Foreign work, non-resident source/treaty classification, the non-resident single-payer minimum-wage exception and overtime treatment, EU posting/A1 coverage, IFICI and grandfathered NHR require case facts before a rate is applied. Check this point with one of our partner accountants. Route to `pt-cross-border`, `pt-social-contributions` or `pt-nhr-ifici`; no flat cross-border rate is authorised by this Guide alone.

## Two worked examples that recompute

### Example 1: October 2026, Lisbon, single without dependants

Original inputs: salary EUR 1,800, meal card EUR 9 × 22 days = EUR 198. The card is below the statutory limit. Ordinary Table I: 1,800 × 24.10% − 193.33 = 240.47, floor EUR 240; employee SS EUR 198, employer SS EUR 427.50; salary net EUR 1,362 plus the card. Salary + employer SS + card subtotal is EUR 2,425.50; insurance and other applicable costs are additional. An EUR 1,800 subsidy paid in June 2026 is withheld separately: another EUR 240, assuming unchanged table eligibility. Sources: Table I, meal allowance and subsidy rules above.

```oa-check
name: Portugal 2026 October original EUR 1800 and EUR 9 meal card
inputs:
  pay: 1800
  meal_days: 22
  meal_card_daily: 9
steps:
  - tax_raw: pay * 0.2410 - 193.33
  - withholding: floor(tax_raw)
  - ss_employee: pay * 0.11
  - ss_employer: pay * 0.2375
  - meal: meal_days * meal_card_daily
  - net_salary: pay - ss_employee - withholding
  - employer_cost: pay + ss_employer + meal
expected:
  tax_raw: 240.47
  withholding: 240
  ss_employee: 198
  ss_employer: 427.50
  meal: 198
  net_salary: 1362
  employer_cost: 2425.50
```

### Example 2: October 2026, IRS Jovem income year 3

Original inputs: age 26, mainland, single/no dependants, pay EUR 2,400, 75% exempt, IAS EUR 537.13; never NHR/IFICI. **Eligibility condition:** this result is usable only if not a dependant, no excluding art. 12-A election, regularised tax position and income-year count established. Without those facts, Check this point with one of our partner accountants.

Ordinary Table I produces EUR 436.41, effective rate 18.18375% before display rounding. Exemption EUR 1,800 is within the monthly cap EUR 2,110.15; non-exempt EUR 600 × that rate = EUR 109.1025, floor EUR 109. Employee SS EUR 264, employer SS EUR 570, net EUR 2,027. For the original November comparison, half the ordinary withholding result gives final floor EUR 54; net EUR 2,082. This is an eligibility-conditional comparison, not an assumption that the original sparse facts establish entitlement.

```oa-check
name: Portugal 2026 original IRS Jovem year 3 EUR 2400 including November comparison
inputs:
  pay: 2400
  exempt_share: 0.75
  ias: 537.13
steps:
  - tax_on_all: pay * 0.3490 - 401.19
  - effective_rate: tax_on_all / pay
  - monthly_cap: 55 * ias / 14
  - exempt: min(pay * exempt_share, monthly_cap)
  - taxable_part: pay - exempt
  - withholding: floor(taxable_part * effective_rate)
  - ss_employee: pay * 0.11
  - ss_employer: pay * 0.2375
  - net_pay: pay - ss_employee - withholding
  - november_withholding: floor(taxable_part * effective_rate * 0.5)
  - november_net: pay - ss_employee - november_withholding
expected:
  tax_on_all: 436.41
  effective_rate: 0.18183750
  monthly_cap: 2110.15
  exempt: 1800
  taxable_part: 600
  withholding: 109
  ss_employee: 264
  ss_employer: 570
  net_pay: 2027
  november_withholding: 54
  november_net: 2082
```

### Retained historical patterns (2026 inputs)

**Pattern 1, original EUR 1,800 and card EUR 7.63 × 22.** The old case supplied no payment month, so retain both period outcomes: ordinary withholding EUR 240, salary net EUR 1,362, card EUR 167.86, combined receipt EUR 1,529.86; November withholding EUR 120, combined receipt EUR 1,649.86. Salary + SS + card subtotal EUR 2,395.36. The previous method wrongly deducted SS before computing IRS. The historical 1% fund assumption is not a current cost input; see the fund hold below.

```oa-check
name: Portugal original 2026 pattern 1 EUR 1800 and EUR 7.63 card
inputs:
  pay: 1800
  days: 22
  card_daily: 7.63
steps:
  - tax_raw: pay * 0.241 - 193.33
  - tax: floor(tax_raw)
  - meal: days * card_daily
  - employee_ss: pay * 0.11
  - employer_ss: pay * 0.2375
  - net: pay - employee_ss - tax
  - receipt: net + meal
  - cost_subtotal: pay + employer_ss + meal
  - november_tax: floor(tax_raw * 0.5)
  - november_receipt: pay - employee_ss - november_tax + meal
expected:
  tax_raw: 240.47
  tax: 240
  meal: 167.86
  employee_ss: 198
  employer_ss: 427.50
  net: 1362
  receipt: 1529.86
  cost_subtotal: 2395.36
  november_tax: 120
  november_receipt: 1649.86
```

**Pattern 2, original minimum wage EUR 920 and 14 full payments in 2026.** For mainland Table I eligibility and the general SS regime: employee SS EUR 101.20, withholding zero, net EUR 818.80 each payment; salary + employer SS annual subtotal EUR 15,939. The old summary EUR 14,094 and additional fund charge are not supported totals. Meals, insurance and any other applicable costs are outside this subtotal.

```oa-check
name: Portugal original 2026 minimum wage EUR 920 with fourteen payments
inputs:
  pay: 920
  payments: 14
steps:
  - employee_ss: pay * 0.11
  - net: pay - employee_ss
  - annual_salary: pay * payments
  - annual_employer_ss: annual_salary * 0.2375
  - annual_subtotal: annual_salary + annual_employer_ss
expected:
  employee_ss: 101.20
  net: 818.80
  annual_salary: 12880
  annual_employer_ss: 3059
  annual_subtotal: 15939
```

**Pattern 3, original June subsidy month.** No numeric pay was specified in the old pattern. Keep salary and holiday subsidy separate for IRS, using each one's own amount and table eligibility. It is not a universal rule that both get the same effective rate. The EUR 1,800 illustration remains in Example 1; no new original input is invented.

**Pattern 4, original termination settlement.** Preserve the components: unpaid salary, proportional holiday and Christmas subsidies, untaken current-year and carried-forward leave, and possible termination compensation. The original supplied no dates, service record, reason for departure or pay inputs. Its blanket /30 and months/12 formulas do not establish entitlements. This is a non-usable hold: Check this point with one of our partner accountants.

## Ask the client first

Obtain residence and payment dates; family/dependant/disability declarations; the spouse's aggregated income; itemised salary, overtime, benefits and subsidies; subsidy agreements; meal-payment medium and days; SS regime and confirmed transition month; and all IRS Jovem income-year and exclusion facts. For net-to-gross, preserve the agreed net and solve gross using the applicable table and SS base; no single gross-up percentage is authorised.

The following retained specialist topics are **non-usable holds** until the operative conditions and case facts are established:

- Old-model SS declaration timing and acceptance in the transition month: Check this point with one of our partner accountants.
- Meal-card cent rounding at the boundary: Check this point with one of our partner accountants.
- First-job and long-term-unemployed hiring reductions: Check this point with one of our partner accountants.
- FCT/FGCT: the FCT obligation to make deliveries ended permanently under the official fund FAQ 2. FGCT suspension is tied to the applicable medium-term agreement (FAQ 27); do not add the old combined 1% automatically or infer current liability/exemption without establishing that condition. For FGCT coverage, suspension duration, legacy debt and fund payment obligations, Check this point with one of our partner accountants. Source: https://www.fundoscompensacao.pt/pt/dl-115/2023-de-15-dez-faq.
- Travel/subsistence allowances, profit shares and termination-payment SS classification: Check this point with one of our partner accountants.
- Sick-pay waiting periods/rates and maternal/paternal leave benefits: Check this point with one of our partner accountants.
- Bereavement and marriage leave, accident-insurance terms and special working-time arrangements: Check this point with one of our partner accountants.
- General payroll record-retention periods and Relatório Único campaign deadline: Check this point with one of our partner accountants.
- Annual income-paid reporting outside ordinary employment DMR, non-resident reporting, annual IRS filing, deductions and mínimo de existência: Check this point with one of our partner accountants. Route to the relevant annual-return/cross-border Guide. The annual IRS schedule must never replace payroll withholding tables.

## Sources

Read on 27 November 2026; the scope below identifies what was actually read. No download status is treated as source proof.

| Source and read scope | Official URL | Read on |
|---|---|---|
| CIRS arts. 2, 12-B, 98, 99, 99-B, 99-C, 99-E, 99-F: remuneration, meal comparison, youth conditions and transition, timing, family, subsidies, rounding | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs2.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs98.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99b.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99c.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99e.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99f.aspx | 2026-11-27 |
| CIRS art. 119: DMR, changed declarations and employee statements; non-resident/annual reporting read but held as a specialist filing route | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx | 2026-11-27 |
| Mainland order: points 1–15; Tables I–III; disability, three-dependant and optional-rate conditions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf | 2026-11-27 |
| Regional circulars: territorial/date scope, table families, retained Table I zero/first/top rows | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular-3-2026.pdf ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular_2_2026.pdf | 2026-11-27 |
| Mainland and Azores November orders: operative points 1–10 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12523-a-2026.pdf ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12610-a-2026.pdf | 2026-11-27 |
| Madeira Despacho 434/2026: operative points 1–10, JORAM pages 2–3 | https://at.madeira.gov.pt/ficheiros/IISerie-196-2026-10-29Supl.pdf | 2026-11-27 |
| Meal allowance Portaria: arts. 1 and 3 | https://files.diariodarepublica.pt/1s/2026/01/02103/0001100011.pdf | 2026-11-27 |
| IAS Portaria: arts. 2 and 4 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf | 2026-11-27 |
| IRS Jovem circular: full calculation method and monthly limit; 2025 monetary example is not reused as a 2026 rate | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_20274_2025.pdf | 2026-11-27 |
| Contributions Code: arts. 40, 42–48, 53, 61–69, 116–121, 211–212; base, rate-classification dependencies and interest | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 | 2026-11-27 |
| DL 127/2025: amended arts. 23-B, 40, 43, transition art. 5 and commencement | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021 | 2026-11-27 |
| Labour Code: arts. 203–205, 210–211, 223, 227–228, 238–239, 262–268, 276; hours, leave/subsidies, night/overtime exceptions and payslip | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475 | 2026-11-27 |
| Mainland minimum wage: arts. 2, 3, 7; Azores art. 3 regional increment; Madeira arts. 2, 4 | https://diariodarepublica.pt/dr/detalhe/decreto-lei/139-2025-992879809 ; https://diariodarepublica.pt/dr/detalhe/decreto-legislativo-regional/8-2002-303252 ; https://files.diariodarepublica.pt/1s/2026/02/02300/0001400015.pdf | 2026-11-27 |
| RGIT arts. 26, 114, 117: penalty framework; art. 105 read but criminal outcome held | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit26.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit105.aspx | 2026-11-27 |
| LGT arts. 35, 44; legal and late-interest rates and scope | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx ; https://diariodarepublica.pt/dr/detalhe/portaria/291-2003-223663 ; https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-11-27 |
| Fund authority FAQ 2 and 27: end of FCT deliveries and conditional FGCT suspension; actual current FGCT liability remains held | https://www.fundoscompensacao.pt/pt/dl-115/2023-de-15-dez-faq | 2026-11-27 |
| AT 2026 calendar: DMR row including August extension | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/calendario_fiscal/Pages/Quadro_res_Decl_2026.aspx | 2026-11-27 |

Not yet confirmed: the specialist holds listed above, including SS old-model timing (the current portal did not expose the operative text and the practical-guide route failed), card-boundary cent rounding, employment incentives, specialist benefits/leave, record retention, Relatório Único, FGCT liability and case-specific criminal/penalty outcomes. Check this point with one of our partner accountants. Do not use historical unsupported rates or amounts for those topics.

> Contributed by OpenAccountants.
