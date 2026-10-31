---
name: belgium-payroll
description: "Belgian payroll for 2026 from the employer side: employee social security of 13.07% (RSZ / ONSS), the private-sector employer rate of 24.92% (19.88% plus wage moderation for most workers), the social and fiscal work bonus (werkbonus), the structural reduction, the exemption above the quarterly pay ceiling, first-hire reductions, the company car solidarity contribution and the 2026 reference CO2 for the benefit in kind, meal vouchers and eco-cheques, how withholding (bedrijfsvoorheffing) fits in, DmfA and monthly advance dates, and RSZ surcharges, interest and late-filing charges. Trigger on: Belgian payroll, RSZ bijdragen, ONSS cotisations, werkbonus, structurele vermindering, solidariteitsbijdrage bedrijfswagen, employer cost Belgium, DmfA, maaltijdcheques. Out of scope: be-payroll-withholding (the Annex III key formula), be-employee-income-tax, be-social-contributions (self-employed), be-cross-border (posted and frontier workers)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/belgium-payroll"
  jurisdiction: "BE"
  tax_year: "2026"
  last_updated: "2026-10-26"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Belgium Payroll (2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to run a payroll, file or pay without review by a qualified professional in Belgium.

## Who this applies to

Employers who employ workers under the social security law of 27 June 1969 in Belgium, for pay in calendar year 2026 (income 2026, assessment year 2027). It covers private-sector white-collar (bedienden) and blue-collar (arbeiders) workers. Public-sector rates are listed but not worked through.

Out: the self-employed (`be-social-contributions`); the employee's own annual return (`be-employee-income-tax`); the step-by-step withholding computation (`be-payroll-withholding`); posted and frontier workers (`be-cross-border`).

Always identify the joint committee (paritair comite / commission paritaire) first. Over 100 joint committees set sector minimum pay, indexation timing, end-of-year premiums and other benefits.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employee social security | 13.07% of gross pay (pensions 7.50, health care 3.55, benefits 1.15, unemployment 0.87); blue-collar pay declared at 108%; no ceiling | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Employer basic contribution, private sector | 24.92% total rate | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Employer rate, structural reduction category 1 or 3 | 19.88% plus wage moderation of at most 5.12% (4.27% + 4.27% of 19.88%), 25.00% in all | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Employer branch shares | Pensions 8.86; health care 3.80; benefits 2.35; unemployment 1.46; occupational diseases 1.00; accidents at work 0.30 | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Public sector basic rates | Contract staff 24.82%; statutory staff and apprentices 17.82%; provincial and local authorities 23.07% | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| 1.60% contribution | 1.60% (1.69% with wage moderation); employers with on average 10 or more workers | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Asbestos fund; special accidents at work | 0.01% (quarters 1 to 3 of 2026); 0.02% | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Blue-collar annual holiday contribution | 5.57% quarterly plus 10.27% once a year, on pay at 108% | 2026 | [RSZ 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Exemption above the pay ceiling | No basic employer contribution or wage moderation on pay codes 1 and 61 above EUR 86,700 a quarter (January to June 2026) and EUR 88,434 (from 1 July 2026) | 2026 | [RSZ 2026/3, high pay](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/otheremployersreductions/partial_exemption_very_high_salaries.html) |
| Structural reduction, category 1, from Q3 2026 | R = 0.14 x (11,687.74 - S) + 0.16 x (9,738.14 - S), each part nil if negative | Q3 2026 | [RSZ 2026/3, structural reduction](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/structuralreduction.html) |
| Social work bonus, white-collar, from 1 September 2026 | Part A EUR 127.54 to S of EUR 2,937.93, tapering by 0.2739 x (S - 2,937.93), nil above EUR 3,403.62; part B EUR 171.99 to S of EUR 2,300.62, tapering by 0.2699 x (S - 2,300.62), nil above EUR 2,937.93 | 2026 | [RSZ 2026/3, work bonus](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html) |
| Social work bonus, white-collar, July and August 2026 | Part A tapers by 0.3196, nil above EUR 3,336.98; part B as above | 2026 | [RSZ 2026/3, work bonus](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html) |
| Social work bonus, blue-collar | Part A EUR 137.74 (taper 0.3452 in July and August, 0.2958 from September); part B EUR 185.75 (taper 0.2915) | 2026 | [RSZ 2026/3, work bonus](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html) |
| Work bonus annual cap | EUR 3,594.36 per worker per calendar year, from 1 July 2026 | 2026 | [RSZ 2026/3, work bonus](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html) |
| Fiscal work bonus | 33.14% of part A and 63% of part B of the social bonus granted, at most EUR 2,000 a year | Income 2026 | [Art. 289ter/1 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5403364d-120e-4c43-8945-ac770f1228f6) |
| First hires | First employee: up to EUR 2,000 a quarter (G21), unlimited period, from 1 July 2026 (EUR 3,100 before); reductions again up to the 5th employee from 1 July 2026, each 12 quarters within 20 | 2026 | [RSZ 2026/3, first hires](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/firstengagments.html) |
| Company car solidarity contribution, formula | Monthly: petrol [(CO2 x 9) - 768] / 12; diesel [(CO2 x 9) - 600] / 12; LPG, CNG [(CO2 x 9) - 990] / 12; electric EUR 20.83; times 185.85 / 114.08 for 2026 | 2026 | [RSZ 2026/3, company cars](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/special_contributions/companycar.html) |
| Company car, multiplication factor | For cars ordered from 1 July 2023 that emit CO2: 2.25 (from 1 July 2023), 2.75 (2025), 4.00 (from 1 January 2026), 5.50 (from 1 January 2027) | 2026 | [RSZ 2026/3, company cars](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/special_contributions/companycar.html) |
| Company car, monthly minimum | EUR 33.93 (cars from before 1 July 2023); EUR 42.34 (cars from 1 July 2023; base EUR 25.99 indexed); no factor on the minimum | 2026 | [RSZ 2026/3, company cars](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/special_contributions/companycar.html) |
| Company car benefit in kind, reference CO2 | 70 g/km petrol, LPG and natural gas; 58 g/km diesel; for benefits granted from 1 January 2026 | 2026 | [KB 17 December 2025, BS 24 December 2025](https://www.ejustice.just.fgov.be/eli/besluit/2025/12/17/2025009788/staatsblad) |
| Meal vouchers | Electronic vouchers granted from 1 January 2026: employer share at most EUR 8.91, employee share at least EUR 1.09, one per day worked | 2026 | [Art. 38/1, par. 2 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796974b3-6cc3-458b-bd22-a129b359909b) |
| Eco-cheques | At most EUR 250 per worker a year, EUR 10 per cheque | 2026 | [Art. 38/1, par. 4 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796974b3-6cc3-458b-bd22-a129b359909b) |
| Annual tax scale behind withholding | 25% to EUR 16,720; 40% to EUR 29,510; 45% to EUR 51,070; 50% above | Income 2026 | [Art. 130 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96) |
| Tax-free amount; employee lump-sum expenses | EUR 11,550; 30% capped at EUR 6,070 | Income 2026 | [Art. 131](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751); [art. 51 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c) |

## The taxable base

**Social security base.** Employee and employer contributions apply to all pay, including bonuses and benefits in kind. Blue-collar pay is declared at 108%. There is no ceiling on the employee contribution. The employer exemption above the quarterly ceiling applies only to the basic employer contribution and wage moderation on pay codes 1 and 61; special contributions and employee contributions stay due on all pay. The ceiling is an absolute amount per employer, not prorated for part-time work, split by employment line where there are several (reduction code 1360).

**Work bonus.** The social work bonus cuts the 13.07% employee contribution for low pay. It is computed on the monthly reference pay S (gross at 100%, full-time equivalent; part-time S = W / J x D or W / H x U). The bonus is part A plus part B. It never exceeds the employee contribution; a shortfall is cut from part B first. The fiscal work bonus then reduces withholding.

**Structural reduction.** Ps = R x µ x ßs per quarter and employment line. For a full-time worker with a full quarter, S is the quarter's pay and µ = ßs = 1. Category 2 (social maribel) and category 3 (sheltered workshops) have their own formulas. Older, younger and long-term unemployed worker reductions are regional and not covered here.

**Withholding base.** Taxable pay is gross pay less employee social security (after the work bonus). Withholding is not the annual scale applied to one month: Annex III of the KB/WIB 92 sets a key formula that annualises pay, deducts the lump sum, applies the scale and the tax-free amount, then family reductions. Two rule sets apply in 2026 (to 31 October and from 1 November). Compute it with `be-payroll-withholding`. Holiday pay, end-of-year premiums and arrears use the special rates for exceptional pay.

**Company car.** The employer owes a monthly solidarity contribution per car made available for private use or commuting, from the formula in the table, with the multiplication factor for cars ordered from 1 July 2023 and the monthly minimum as a floor. Utility vehicles only: declare EUR 0.00. The employee's benefit in kind is added to taxable pay for withholding; it is built on the reference CO2 of 70 g/km (petrol) and 58 g/km (diesel) for 2026. The full benefit formula and the employer's 2026 tax deductibility are on the "Not yet confirmed" line and are not given here.

**Meal vouchers and eco-cheques.** Within the art. 38/1 limits (EUR 8.91 employer share, EUR 1.09 minimum employee share, one per day actually worked; eco-cheques EUR 250 a year), they are exempt from income tax.

**Benefits and pay rules (labour law).** Double holiday pay for white-collar workers is 92% of monthly pay, paid by the employer and carrying employee social security and exceptional-pay withholding; blue-collar holiday pay comes from the holiday fund. Standard week 38 hours; overtime supplement 50% (100% on Sundays and holidays); voluntary overtime up to 120 hours a year (extendable to 360); the minimum wage (GGMMI) is set by collective agreement no. 43 and indexed. Guaranteed pay in illness, the 20 days of holiday and the 10 public holidays apply. These points were carried from the earlier version and were not re-read against 2026 sources; see "Not yet confirmed".

**Payslip.** Each pay run needs a payslip showing employer and employee identification (RSZ number, INSZ), period, gross pay and every component (including benefits in kind), employee RSZ, work bonus, taxable pay, withholding, special social security contribution, net pay, meal vouchers and holiday pay where paid.

## Deadlines and filing

| Obligation | When | Where |
|---|---|---|
| Dimona (start and end of employment) | By the start or end of the employment | RSZ |
| Monthly RSZ advances | By the 5th of each month, when contributions for the quarter before last (k-2) were above EUR 4,000. Each advance is a share of the contributions for the same quarter last year (k-4): Q1 to Q3, 30% by the 5th of the 2nd and 3rd month of the quarter and 25% by the 5th of the month after it; Q4, 30% by 5 November, 35% by 5 December and 15% by 5 January. Flat-rate advances (EUR 450 per worker from the 3rd, EUR 700 per construction blue-collar worker) apply in the cases the RSZ sets | RSZ ([advances](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/contributionpayment_obligations_periodicity/provisions.html)) |
| DmfA and balance of contributions | Quarterly, by the last day of the month after the quarter: 30 April, 31 July, 31 October, 31 January | RSZ ([payment dates](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/contributionpayment_obligations_periodicity/generalrule.html)) |
| Blue-collar yearly holiday contribution (10.27%) | Declared by 31 March, paid by 30 April | RSZ |
| Withholding return and payment | Monthly payers within 15 days after the month the pay was paid; quarterly if the previous year's withholding was under EUR 51,480 (art. 412 WIB 92); 2026 calendar dates in `be-payroll-withholding` | FOD Financien (Finprof) |
| Tax certificates 281.10 / 281.20 | By 28 February of the following year (Belcotax) | FOD Financien |
| Work accident declaration | Within 8 calendar days | Insurer / Fedris |

A DmfA can be corrected within the limitation period.

## Penalties and interest

- **Late payment of RSZ contributions:** a surcharge of 10% of the amount not paid on time, plus late interest of 7% a year from the due date to payment. On the employer's request, the RSZ can waive these when the contributions are paid before the end of the second month after the quarter and earlier quarters were usually paid on time. In exceptional circumstances the employer can get up to 50% off the surcharges and up to 25% off the interest, once all contributions are paid ([RSZ, consequences](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/contributionpayment_obligations_periodicity/omissionconsequences.html)).
- **Late DmfA:** a flat charge of EUR 495.79, plus EUR 247.89 per tranche of EUR 24,789.35 of contributions above EUR 49,578.70. Not charged when the return is filed before the end of the second month after the quarter and earlier returns were usually on time. The same amounts apply for habitually incomplete or incorrect returns ([RSZ, DmfA omission](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/dmfa/omission.html)).
- **DmfA drawn up or corrected by the RSZ:** EUR 50.00 plus EUR 4.00 per missing or changed employment line. A return is incomplete or incorrect when, six months after the quarter, missing lines or pay reach 5% of the persons or pay declared.
- **Withholding paid late:** late interest at 4% a year under art. 414 WIB 92, with administrative fines of EUR 50 to EUR 1,250 per infringement under art. 445; detail in `be-payroll-withholding`.

## Cross-border points

- An employer without a Belgian establishment that employs workers subject to Belgian social security still files DmfA and pays RSZ.
- Workers sent to Belgium from another EU state with an A1 certificate stay in their home scheme; Limosa notification applies to posted workers. See `be-cross-border`.
- Withholding applies to pay for work done in Belgium by non-residents under the Income Tax Code and the treaty; frontier workers and treaty splits are in `be-cross-border`.

## Worked examples

### Example 1: white-collar EUR 3,500 a month, third quarter of 2026

A full-time white-collar worker in the private sector, category 1 of the structural reduction, earns EUR 3,500 a month in July, August and September 2026. Employee social security is 13.07% of 3,500, EUR 457.45. There is no work bonus: EUR 3,500 is above EUR 3,336.98 (July and August) and EUR 3,403.62 (September). Taxable pay for withholding is EUR 3,042.55 a month; the withholding itself comes from `be-payroll-withholding`. The employer pays 25.00% of the quarter's EUR 10,500, EUR 2,625.00. The structural reduction low-pay part is 0.14 x (11,687.74 - 10,500) = EUR 166.28; the very-low-pay part is negative, so nil. Net basic employer contributions are EUR 2,458.72 for the quarter, before special contributions.

```oa-check
name: White-collar EUR 3,500 a month, Q3 2026, employee RSZ and structural reduction
inputs:
  monthly_gross: 3500
  employee_rate: 0.1307
  employer_rate: 0.25
steps:
  - employee_ss: round(monthly_gross * employee_rate, 2)
  - taxable_pay: monthly_gross - employee_ss
  - quarter_pay: monthly_gross * 3
  - employer_quarter: quarter_pay * employer_rate
  - low_pay_part: max(round(0.14 * (11687.74 - quarter_pay), 2), 0)
  - very_low_pay_part: max(round(0.16 * (9738.14 - quarter_pay), 2), 0)
  - structural_reduction: low_pay_part + very_low_pay_part
  - employer_net: employer_quarter - structural_reduction
expected:
  employee_ss: 457.45
  taxable_pay: 3042.55
  employer_quarter: 2625.00
  structural_reduction: 166.28
  employer_net: 2458.72
```

### Example 2: low-paid white-collar worker with a petrol company car, September 2026

A full-time white-collar worker earns EUR 2,500 a month and has a petrol company car ordered in 2024, CO2 120 g/km, used privately. Work bonus part A is the full EUR 127.54 (S is below EUR 2,937.93). Part B is 171.99 - 0.2699 x (2,500 - 2,300.62) = EUR 118.18. The social bonus is EUR 245.72, so the employee pays 326.75 - 245.72 = EUR 81.03 of RSZ. The fiscal work bonus earned is 33.14% x 127.54 + 63% x 118.18 = EUR 116.72. The employer's solidarity contribution is [(120 x 9) - 768] / 12 = 26.00, indexed by 185.85 / 114.08 and multiplied by 4.00 for a car ordered after 30 June 2023: EUR 169.43 a month. That is above the EUR 42.34 minimum, so EUR 169.43 is due. Edge case: the RSZ page does not say at which step to round; this example rounds once, at the end.

```oa-check
name: White-collar EUR 2,500, September 2026, work bonus and company car solidarity contribution
inputs:
  monthly_gross: 2500
  employee_rate: 0.1307
  co2: 120
steps:
  - part_a: 127.54
  - part_b: round(max(min(171.99 - 0.2699 * (monthly_gross - 2300.62), 171.99), 0), 2)
  - work_bonus: part_a + part_b
  - employee_ss_gross: round(monthly_gross * employee_rate, 2)
  - employee_ss_net: employee_ss_gross - work_bonus
  - fiscal_bonus: round(part_a * 0.3314, 2) + round(part_b * 0.63, 2)
  - car_base: ((co2 * 9) - 768) / 12
  - car_contribution: max(round(car_base * 185.85 / 114.08 * 4, 2), 42.34)
expected:
  part_b: 118.18
  work_bonus: 245.72
  employee_ss_net: 81.03
  fiscal_bonus: 116.72
  car_base: 26.00
  car_contribution: 169.43
```

## Ask the client first

1. Joint committee number, and whether each worker is white-collar or blue-collar.
2. Gross pay per month and per quarter, work fraction, and any bonuses, holiday pay or arrears.
3. Company cars: fuel type, WLTP CO2, catalogue value, and the date the car was ordered or the lease signed (before or after 1 July 2023).
4. Average headcount (10 or more triggers the 1.60% contribution) and whether this is a first hire.
5. Meal voucher face value and employee share, and eco-cheques granted.
6. Contributions paid for the same quarter last year (sets the monthly advances).

## Sources

| Source | URL | Read on |
|---|---|---|
| RSZ, administrative instructions 2026/3, contributions | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, company cars (solidarity contribution) | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/special_contributions/companycar.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, work bonus | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, structural reduction | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/structuralreduction.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, payment dates | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/contributionpayment_obligations_periodicity/generalrule.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, monthly advances | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/contributionpayment_obligations_periodicity/provisions.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, late payment sanctions | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/contributionpayment_obligations_periodicity/omissionconsequences.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, DmfA late or missing | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/obligations/obligations_nsso/dmfa/omission.html | 2026-10-26 |
| RSZ, administrative instructions 2026/3, exemption above the pay ceiling | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/otheremployersreductions/partial_exemption_very_high_salaries.html | 2026-10-23 |
| RSZ, administrative instructions 2026/3, first hires | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/firstengagments.html | 2026-10-23 |
| KB 17 December 2025, reference CO2 2026 (KB/WIB 92 art. 18, par. 3, 9), Belgisch Staatsblad 24 December 2025 | https://www.ejustice.just.fgov.be/eli/besluit/2025/12/17/2025009788/staatsblad | 2026-10-26 |
| Fisconetplus, art. 38/1 WIB 92, meal vouchers and eco-cheques | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796974b3-6cc3-458b-bd22-a129b359909b | 2026-10-23 |
| Fisconetplus, art. 289ter/1 WIB 92, fiscal work bonus | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5403364d-120e-4c43-8945-ac770f1228f6 | 2026-10-23 |
| Fisconetplus, art. 130 WIB 92, tax scale | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96 | 2026-10-23 |
| Fisconetplus, art. 131 WIB 92, tax-free amount | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751 | 2026-10-23 |
| Fisconetplus, art. 51 WIB 92, lump-sum expenses | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c | 2026-10-23 |
| Fisconetplus, art. 412 WIB 92, withholding payment dates and quarterly threshold | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/473ac660-d80e-4181-ab8e-e3544b57ffa8 | 2026-10-23 |

Not yet confirmed: the company car benefit in kind formula of art. 36, par. 2 WIB 92 (6/7 of catalogue value, CO2 percentage from 5.5% moving 0.1 point per gram, 4% to 18%, age reduction) and its 2026 indexed minimum, because Fisconetplus could not be read today; the employer's 2026 tax deductibility of company cars (art. 198bis and 66 WIB 92); the rounding step in the solidarity contribution; the special social security contribution scale for 2026; work bonus amounts for January to June 2026; the 2026 minimum wage (GGMMI, CAO 43); the labour-law points (holiday pay, overtime, guaranteed pay, holidays, payslip contents, Dimona, 281.10 and work accident deadlines) carried from the earlier version without a 2026 re-read; the FOD withholding calendar page, which blocked automated reading today (dates kept in `be-payroll-withholding`).

> Contributed by Ryan Duguid.

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-26. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `belgium-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/belgium-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
