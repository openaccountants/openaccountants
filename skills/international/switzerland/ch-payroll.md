---
name: ch-payroll
description: "Swiss payroll for tax year 2026: what an employer deducts from wages and pays on top. Covers AHV/IV/EO (10.6%, split 5.3% each), unemployment insurance ALV (2.2%, split 1.1% each, on pay up to CHF 148,200; nothing above since 2023), accident insurance UVG (employer pays occupational, employee pays non-occupational, rates set by the insurer), occupational pension BVG (entry threshold CHF 22,680, coordination deduction CHF 26,460, coordinated pay CHF 3,780 to CHF 64,260, savings credits 7/10/15/18%), cantonal family allowance funds, the salary certificate (Lohnausweis), the annual AHV wage declaration due 30 January, and tax at source (Quellensteuer) for foreign employees without a C permit: tariff codes, the employer's commission and remittance. Trigger on: Swiss payroll, Lohnabrechnung, AHV Arbeitgeber, ALV Beitrag, BVG Koordinationsabzug, Quellensteuer Arbeitgeber, Lohnausweis, employer cost Switzerland. Out of scope: ch-ahv-iv (self-employed), ch-cross-border (residence, NOV, frontier workers), ch-federal-income-tax and ch-cantonal-tax (the employee's annual return)."
jurisdiction: CH
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Switzerland: payroll (social insurance deductions and tax at source)

This skill covers what a Swiss employer withholds from pay and what it pays on top in 2026. It links to the pack's other skills rather than repeating them:

- `ch-ahv-iv`: AHV/IV/EO for the self-employed (sliding scale, minimum contribution).
- `ch-cross-border`: residence, arrival and departure, the subsequent ordinary assessment (NOV) for source-taxed employees, non-residents and frontier workers.
- `ch-federal-income-tax` and `ch-cantonal-tax`: the employee's own tax return.
- `ch-taxation-employee-stock-options-and-employee`: employee shares and options.

## Who this applies to

Every employer with staff working in Switzerland. Employees are insured in Swiss social insurance from 1 January after their 17th birthday and pay AHV/IV/EO on their wages ([AHV/IV sheet 2.01](https://www.ahv-iv.ch/p/2.01.d), no. 1). The employer deducts the employee's share from each wage and settles both shares with its compensation fund (Ausgleichskasse) (AHVG art. 51).

Out or partly out:

- **Small wages.** On wages of up to CHF 2,500 a year per employer, AHV/IV/EO is only levied if the employee asks. This does not apply to household employees or to staff of the cultural and media employers listed in sheet 2.01, who always pay ([sheet 2.01](https://www.ahv-iv.ch/p/2.01.d), no. 19). From 1 January 2026 the old exemption for short, low-paid engagements in culture and media (AHVV art. 34d para. 2 let. b) no longer exists.
- **Employees past reference age (65).** They still pay AHV/IV/EO, but only on pay above an allowance of CHF 16,800 a year per employer (CHF 1,400 per month for part years), unless they waive it. They pay no ALV from the end of the month in which they reach reference age ([sheet 2.01](https://www.ahv-iv.ch/p/2.01.d), no. 14 to 17; [sheet 2.08](https://www.ahv-iv.ch/p/2.08.d)).
- **BVG.** Only employees earning more than CHF 22,680 a year from one employer are compulsorily insured: from 1 January after their 17th birthday for death and disability, and from 1 January after their 24th birthday for retirement savings (BVG art. 7).
- **UVG non-occupational cover.** Only for employees working at least 8 hours a week for one employer. Below that, accidents on the way to work count as occupational (UVV art. 13).
- **Tax at source.** Foreign employees resident in Switzerland without a settlement permit (C permit) are taxed at source by the employer (DBG art. 83). Not if the spouse, living together, is Swiss or holds a C permit (DBG art. 83 para. 2). Non-residents working for a Swiss employer are taxed at source under DBG art. 91 (see `ch-cross-border`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| AHV/IV/EO total on wages | 10.6% (AHV 8.7%, IV 1.4%, EO 0.5%), no ceiling | 2026 | [AHV/IV sheet 2.01, Stand 1.1.2026, no. 3](https://www.ahv-iv.ch/p/2.01.d) |
| AHV/IV/EO employee share / employer share | 5.3% / 5.3% | 2026 | [sheet 2.01, no. 3](https://www.ahv-iv.ch/p/2.01.d) |
| AHV component, employee / employer | 4.35% / 4.35% | 2026 | [AHVG art. 5 and 13](https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de) |
| ALV total | 2.2% up to CHF 148,200 a year per employment; 0% above (no solidarity contribution since 1 January 2023) | 2026 | [AVIG art. 3](https://www.fedlex.admin.ch/eli/cc/1982/2184_2184_2184/de); [sheet 2.08](https://www.ahv-iv.ch/p/2.08.d) |
| ALV employee share / employer share | 1.1% / 1.1% | 2026 | [AVIG art. 3 para. 3](https://www.fedlex.admin.ch/eli/cc/1982/2184_2184_2184/de) |
| ALV monthly ceiling (provisional, monthly payroll) | CHF 12,350 | 2026 | [sheet 2.08, no. 5](https://www.ahv-iv.ch/p/2.08.d) |
| UVG maximum insured earnings | CHF 148,200 a year (CHF 406 a day) | 2026 | [UVV art. 22 para. 1](https://www.fedlex.admin.ch/eli/cc/1983/38_38_38/de) |
| UVG occupational accident premium | Employer pays; rate set by the insurer (Suva or private) in per mille of insured earnings | 2026 | [UVG art. 91 and 92](https://www.fedlex.admin.ch/eli/cc/1982/1676_1676_1676/de) |
| UVG non-occupational accident premium | Employee pays unless the employer agrees to carry it; rate set by the insurer | 2026 | [UVG art. 91 para. 2](https://www.fedlex.admin.ch/eli/cc/1982/1676_1676_1676/de) |
| BVG entry threshold | Annual pay above CHF 22,680 | 2026 | [BVG art. 7](https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de); [BSV Masszahlen 2025/2026](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf) |
| BVG coordination deduction | CHF 26,460 | 2026 | [BVG art. 8](https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de); [BSV Masszahlen](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf) |
| BVG maximum insured annual pay | CHF 90,720 | 2026 | same |
| BVG coordinated pay, minimum / maximum | CHF 3,780 / CHF 64,260 | 2026 | same |
| BVG minimum savings credits (% of coordinated pay) | Age 25-34: 7%; 35-44: 10%; 45-54: 15%; 55 to reference age: 18% | 2026 | [BVG art. 16](https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de) |
| BVG minimum interest rate | 1.25% | 2026 | [BSV Masszahlen](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf) |
| BVG split | Employer pays at least as much as all its employees together | 2026 | [BVG art. 66 para. 1](https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de) |
| Family allowance fund (FAK) contribution | Set by each canton and fund, as % of AHV wages | 2026 | [FamZG art. 16](https://www.fedlex.admin.ch/eli/cc/2008/51/de) |
| AHV allowance for employees past reference age | CHF 16,800 a year per employer (CHF 1,400 a month) | 2026 | [sheet 2.01, no. 15 and 17](https://www.ahv-iv.ch/p/2.01.d) |
| Small-wage limit (AHV only on request) | CHF 2,500 a year per employer | 2026 | [sheet 2.01, no. 19](https://www.ahv-iv.ch/p/2.01.d) |
| AHV payment frequency | Quarterly if annual payroll is up to CHF 200,000; monthly above | 2026 | [AHVV art. 34](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| AHV late payment interest | 5% a year, day by day (30-day month, 360-day year) | 2026 | [AHVV art. 41bis and 42](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Tax at source tariff codes | A single, not living with children; B married, one earner; C married, two earners; H single living with and mainly supporting children; D AHV refunds under AHVG art. 18 para. 3; E simplified procedure; G replacement income not paid through the employer; L to Q German frontier workers; R to V Italian frontier workers | 2026 | [QStV art. 1](https://www.fedlex.admin.ch/eli/cc/2018/274/de) |
| Employer's commission on tax at source (federal range) | 1% to 2% of the tax, set by the canton | 2026 | [DBG art. 88 para. 4](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Zurich commission on tax at source | 2% of the tax (1% on pension lump sums, max CHF 50 each) | 2026 | [Kantonales Steueramt Zürich](https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/quellensteuer-abrechnen.html) |
| Zurich tariff A0, no church tax, gross CHF 6,951 to 7,000 a month | 7.75% | 2026 | [Zurich Tarif A ohne Kirchensteuer, Ausgabe 2026](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/quellensteuer/quellensteuertarif/2026/p208840_QuellensteuerTarif_A_ohne_KS_ENT1.pdf) |
| Mandatory NOV threshold for source-taxed residents | Gross employment income of CHF 120,000 or more | 2026 | [QStV art. 9](https://www.fedlex.admin.ch/eli/cc/2018/274/de) |

The 13th AHV old-age pension is paid for the first time in December 2026. It does not change the 2026 contribution rate: the 1 January 2026 edition of sheet 2.01 keeps 10.6%.

## The taxable base

**AHV wages (massgebender Lohn).** Every payment for work as an employee: salary, 13th salary, bonuses, commissions, overtime and holiday pay, board fees, regular benefits in kind (meals, housing, private use of a company car), and employee share benefits (valued and timed under the federal tax rules). Not included: family allowances within the usual local amounts, the employer's regulatory pension contributions, accident and sickness insurance premiums paid directly for all staff equally, gifts in kind up to CHF 600 a year, and work-related training ([sheet 2.01](https://www.ahv-iv.ch/p/2.01.d), no. 10 and 11). Meals and lodging are valued at fixed amounts: full board and lodging CHF 33 a day or CHF 990 a month (no. 12).

**ALV** uses the same AHV wage, capped at CHF 148,200 per employment. For part-year employment the cap is CHF 148,200 / 360 times days employed, counting 30 days a month ([sheet 2.08](https://www.ahv-iv.ch/p/2.08.d), no. 3).

**UVG** uses the AHV wage up to CHF 148,200, with small differences: wages of employees past reference age and usual family allowances count (UVV art. 22 para. 2).

**BVG** uses the annual AHV wage (BVG art. 7 para. 2). Coordinated pay = annual pay up to CHF 90,720, minus CHF 26,460, and never less than CHF 3,780 (BVG art. 8). The age credits in the table are the legal minimum savings. The pension fund's own rules set the actual contributions, which add risk premiums and costs and are usually higher. Use the fund's rules, not the minimum, for real payroll.

**Tax at source** is computed on gross pay before social deductions, including benefits in kind and replacement income (DBG art. 84). The ESTV builds flat allowances for work costs, insurance premiums and children into the tariffs (DBG art. 85). The employer applies the tariff of the employee's canton of residence (DBG art. 107 para. 1 let. a) as a percentage of the month's gross pay. The ESTV and the cantons fix how a 13th salary, bonuses, hourly pay, part-time work and several jobs are handled (DBG art. 85 para. 4; ESTV circular 45).

**Order of a monthly payslip.** Gross pay, less employee AHV/IV/EO 5.3%, ALV 1.1%, UVG non-occupational premium, BVG employee contribution, and, where it applies, tax at source on the gross.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Register a new source-taxed employee with the tax office | Within 8 days of starting work (or in the monthly electronic return) | [QStV art. 5](https://www.fedlex.admin.ch/eli/cc/2018/274/de) |
| AHV/IV/EO and ALV advance payments (Akontobeiträge) | Within 10 days after each quarter end (payroll up to CHF 200,000) or month end | [AHVV art. 34 and 35](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Annual wage declaration to the compensation fund | By 30 January after the year (within 30 days of year end); for 2026, by 30 January 2027 | [AHVV art. 36](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de); [sheet 2.01, no. 4](https://www.ahv-iv.ch/p/2.01.d) |
| Balance after the declaration | Within 30 days of the invoice | [AHVV art. 36 para. 4](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| BVG contributions to the pension fund | By the end of the first month after the year at the latest; the fund's rules usually ask for more frequent payment | [BVG art. 66 para. 4](https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de) |
| Tax at source return, Zurich | Monthly; quarterly if fewer than 10 source-taxed employees; within 30 days after the period ends | [Kantonales Steueramt Zürich](https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/quellensteuer-abrechnen.html) |
| Tax at source corrections, Zurich | Until 31 March of the following year, on a later return | same |
| Salary certificate (Lohnausweis, form 11) | To every employee for each year. Basel-Stadt, Bern, Fribourg, Jura, Neuchâtel, Solothurn, Vaud and Valais also require a copy sent directly to the cantonal tax office | [DBG art. 127](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de); [ESTV Wegleitung Lohnausweis 2026](https://www.estv.admin.ch/dam/de/sd-web/afP1GDFr8gE3/dbst-form-lohna-wegleitung-2026-de.pdf), no. 2 and 74 |
| Source-tax certificate to the employee | For the tax deducted | [DBG art. 88 para. 1 let. b](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |

The DBG and the Wegleitung set no calendar date for handing over the Lohnausweis. Give it early enough for the employee's return (Zurich: due 31 March of the following year, see `ch-cross-border`).

The tax at source goes to the canton of residence of each employee, even where the employer sits in another canton (DBG art. 88 para. 2 and art. 107 para. 3). An employer with staff living in several cantons files in each.

Small employers can use the simplified procedure (BGSA): one annual settlement of AHV/IV/EO, ALV, family allowances and a flat source tax with the compensation fund. For 2026 each wage must not exceed CHF 22,680 and total payroll CHF 60,480 (twice the maximum AHV old-age pension), all staff must be settled this way, and it is not open to companies (AG, GmbH) or cooperatives ([AHV/IV sheet 2.07, Stand 1.1.2026](https://www.ahv-iv.ch/p/2.07.d), no. 2; AHVV art. 34 para. 1 let. c). The flat source tax is 5% of the AHV wage: 0.5% federal (DBG art. 37a) and 4.5% cantonal and communal (sheet 2.07, no. 5).

## Penalties and interest

- **AHV/IV/EO and ALV.** Late interest of 5% a year, whether or not the employer is at fault. It runs from the end of the payment period on advances not paid within 30 days; from 1 January after the year when the declaration is late; and from the invoice date on a balance not paid within 30 days (AHVV art. 41bis and 42; sheet 2.01 no. 7 to 9).
- **Employer liability.** An employer that harms the AHV by wilful or grossly negligent breach of the rules must make good the loss. For a company, board members and managers are liable in second rank, jointly (AHVG art. 52).
- **Missed deduction.** An employer that fails to deduct the employee's ALV share pays both shares ([sheet 2.08](https://www.ahv-iv.ch/p/2.08.d), no. 9). The UVG employee premium may only be deducted from the pay of the same or the next pay period (UVG art. 91 para. 3).
- **Tax at source.** The employer is liable for the tax whether or not it deducted it (DBG art. 88 para. 3). Failing to deduct is tax evasion: a fine normally equal to the tax, from one third to three times (DBG art. 175). Using deducted tax for other purposes is a crime: up to three years' imprisonment or a monetary penalty (DBG art. 187). Breach of reporting duties after a reminder: fine up to CHF 1,000, up to CHF 10,000 in serious cases (DBG art. 174). The canton can cut or cancel the commission (QStV art. 6 para. 2). Zurich charges interest on late returns even where an extension was granted.
- **BVG.** The pension fund may charge late interest (BVG art. 66 para. 2); the rate is in its rules.

## Cross-border points

- **Which country insures.** With EU/EFTA states, Switzerland applies EU coordination: an employee is normally insured where they work. A posted worker keeps home cover with an A1 certificate. See `ch-cross-border` and [BSV](https://www.bsv.admin.ch/en/social-security-agreements).
- **Frontier workers.** German frontier workers use tariff codes L, M, N, P and Q, with a federal share of 10% of the tax (QStV art. 1 and 8). Italian frontier workers under the 2020 agreement use codes R to V at 80% of the ordinary tariff (QStV art. 1 para. 3). Detail and the NOV rules: `ch-cross-border` and `germany-to-switzerland-cross-border-tax`.
- **Non-resident employees** (DBG art. 91): source tax under the employer's canton, final unless an NOV on request applies. Since 2025 an employer must, on request, certify telework and days abroad for an employee who leaves during the year (DBG art. 127 para. 3; QStV art. 5a for France).
- **Foreign employer.** A foreign employer without a Swiss establishment does not withhold source tax; the employee is assessed ordinarily, unless a Swiss establishment or the Swiss group company as de facto employer bears the pay (QStV art. 4).
- **Settlement permit during the year.** An employee who gets a C permit or marries a Swiss or C-permit holder leaves source tax from the following month (QStV art. 12; see `ch-cross-border`).

## Worked examples

### Example 1: employee aged 40 on CHF 90,000, no source tax

A Swiss employee aged 40 earns CHF 90,000 a year, paid monthly, no bonus. AHV/IV/EO is 5.3% each side: CHF 4,770 for the employee and CHF 4,770 for the employer. The salary is below CHF 148,200, so ALV is 1.1% each side on all of it: CHF 990 each.

BVG: the salary is above CHF 22,680, so she is insured. Coordinated pay is 90,000 - 26,460 = CHF 63,540, below the CHF 64,260 maximum. At 40 the minimum savings credit is 10%: CHF 6,354. We assume the fund splits it equally, which is the least the employer may pay (BVG art. 66): CHF 3,177 each.

Employee deductions: 4,770 + 990 + 3,177 = CHF 8,937, leaving CHF 81,063 before the UVG non-occupational premium and her income tax (she files a normal return). Employer cost: 90,000 + 4,770 + 990 + 3,177 = CHF 98,937, plus the UVG occupational premium, the FAK contribution, the compensation fund's administration fee and the BVG risk and cost premiums, which depend on the insurer, canton and fund and are not computed here.

```oa-check
name: Employee aged 40, CHF 90,000, AHV/IV/EO, ALV and BVG minimum (2026)
inputs:
  gross: 90000
  ahv_iv_eo_share_pct: 5.3
  alv_share_pct: 1.1
  alv_ceiling: 148200
  bvg_coordination_deduction: 26460
  bvg_max_insured: 90720
  bvg_min_coordinated: 3780
  bvg_credit_pct_age_35_44: 10
steps:
  - ahv_employee: gross * ahv_iv_eo_share_pct / 100
  - ahv_employer: ahv_employee
  - alv_employee: min(gross, alv_ceiling) * alv_share_pct / 100
  - alv_employer: alv_employee
  - coordinated_pay: max(min(gross, bvg_max_insured) - bvg_coordination_deduction, bvg_min_coordinated)
  - bvg_credit: coordinated_pay * bvg_credit_pct_age_35_44 / 100
  - bvg_employee: bvg_credit / 2
  - bvg_employer: bvg_credit - bvg_employee
  - employee_deductions: ahv_employee + alv_employee + bvg_employee
  - net_before_uvg_and_tax: gross - employee_deductions
  - employer_cost: gross + ahv_employer + alv_employer + bvg_employer
expected:
  ahv_employee: 4770.00
  alv_employee: 990.00
  coordinated_pay: 63540.00
  bvg_credit: 6354.00
  bvg_employee: 3177.00
  employee_deductions: 8937.00
  net_before_uvg_and_tax: 81063.00
  employer_cost: 98937.00
```

### Example 2: B-permit employee taxed at source in Zurich, CHF 7,000 a month

A single Portuguese citizen with a B permit lives in the canton of Zurich, has no children, belongs to no church and earns CHF 7,000 a month (12 payments, no 13th salary). She has no C permit and is not married, so the employer deducts tax at source under the Zurich tariff (DBG art. 83, art. 107). Her code is A0, no church tax (A0N). On the 2026 Zurich tariff A without church tax, CHF 7,000 falls in the band CHF 6,951 to 7,000, rate 7.75%. Tax at source is 7,000 x 7.75% = CHF 542.50 a month, computed on gross pay before social deductions.

Social deductions: AHV/IV/EO 5.3% = CHF 371 and ALV 1.1% = CHF 77 (below the CHF 12,350 monthly ceiling). The BVG and UVG employee contributions depend on her fund and insurer and are left out here.

The employer keeps a 2% commission on the tax, CHF 10.85, so CHF 531.65 is owed to the Kantonales Steueramt Zürich. The employer files the monthly return within 30 days after the month ends; the tax office then invoices the amount.

The edge case: her annual gross is 12 x 7,000 = CHF 84,000, which is CHF 36,000 under the CHF 120,000 NOV threshold. So tax at source is final for her salary unless she asks for an NOV by 31 March 2027 (DBG art. 89a). If she had a 13th salary or bonus, the month's rate would be set under ESTV circular 45, not simply read from the monthly table.

```oa-check
name: B permit, Zurich tariff A0N 2026, CHF 7,000 a month, tax at source and commission
inputs:
  monthly_gross: 7000
  zh_a0n_rate_pct: 7.75
  ahv_iv_eo_share_pct: 5.3
  alv_share_pct: 1.1
  alv_monthly_ceiling: 12350
  zh_commission_pct: 2
  nov_threshold: 120000
  months: 12
steps:
  - source_tax: monthly_gross * zh_a0n_rate_pct / 100
  - ahv_employee: monthly_gross * ahv_iv_eo_share_pct / 100
  - alv_employee: min(monthly_gross, alv_monthly_ceiling) * alv_share_pct / 100
  - net_before_bvg_uvg: monthly_gross - source_tax - ahv_employee - alv_employee
  - commission: round(source_tax * zh_commission_pct / 100, 2)
  - remitted_to_canton: source_tax - commission
  - annual_gross: monthly_gross * months
  - below_nov_threshold_by: nov_threshold - annual_gross
expected:
  source_tax: 542.50
  ahv_employee: 371.00
  alv_employee: 77.00
  net_before_bvg_uvg: 6009.50
  commission: 10.85
  remitted_to_canton: 531.65
  annual_gross: 84000.00
  below_nov_threshold_by: 36000.00
```

## Ask the client first

1. Each employee's age, annual salary (with 13th salary and bonuses) and weekly hours. These set BVG entry and the savings credit band, the UVG non-occupational cover and the ALV ceiling.
2. Nationality and permit (B, C, L, G), canton of residence, marital status, the spouse's job and permit, number of children and church membership. These decide whether tax is taken at source and which code and canton apply.
3. Which compensation fund, UVG insurer, pension fund and family allowance fund the company uses, and their rates and rules.
4. Whether anyone works abroad, lives abroad or is posted to Switzerland (A1 certificate), and whether anyone is past reference age.
5. Annual payroll total: above CHF 200,000 means monthly AHV payments.

## Sources

| Source | URL | Read on |
|---|---|---|
| Informationsstelle AHV/IV, Merkblatt 2.01 Lohnbeiträge an die AHV, IV und EO, Stand 1. Januar 2026 | https://www.ahv-iv.ch/p/2.01.d | 2026-10-23 |
| Informationsstelle AHV/IV, Merkblatt 2.07 Vereinfachtes Abrechnungsverfahren für Arbeitgebende, Stand 1. Januar 2026 | https://www.ahv-iv.ch/p/2.07.d | 2026-10-23 |
| Informationsstelle AHV/IV, Merkblatt 2.08 Beiträge an die Arbeitslosenversicherung, Stand 1. Januar 2025 | https://www.ahv-iv.ch/p/2.08.d | 2026-10-23 |
| Informationsstelle AHV/IV, Update Sozialversicherungen in der Schweiz, Änderungen 2026 | https://www.shop.ahv-iv.ch/data/docs/de/82816/Update-%C2%ABSozialversicherungen-in-der-Schweiz%C2%BB-Stand-1.-Januar-2026.pdf | 2026-10-23 |
| AHVG, SR 831.10, version of 1 January 2026, art. 5, 13, 51, 52 | https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de | 2026-10-23 |
| AHVV, SR 831.101, version of 1 January 2026, art. 34, 35, 36, 41bis, 42 | https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de | 2026-10-23 |
| AVIG, SR 837.0, version of 1 January 2026, art. 3 | https://www.fedlex.admin.ch/eli/cc/1982/2184_2184_2184/de | 2026-10-23 |
| UVG, SR 832.20, version of 1 January 2026, art. 1a, 91, 92 | https://www.fedlex.admin.ch/eli/cc/1982/1676_1676_1676/de | 2026-10-23 |
| UVV, SR 832.202, version of 1 January 2026, art. 13, 22 | https://www.fedlex.admin.ch/eli/cc/1983/38_38_38/de | 2026-10-23 |
| BVG, SR 831.40, version of 1 January 2025 (current), art. 7, 8, 16, 66 | https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de | 2026-10-23 |
| BSV, Wichtige Masszahlen im Bereich der beruflichen Vorsorge 2025 und 2026 | https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf | 2026-10-23 |
| FamZG, SR 836.2, version of 1 January 2026, art. 16 | https://www.fedlex.admin.ch/eli/cc/2008/51/de | 2026-10-23 |
| DBG, SR 642.11, version of 2 September 2026, art. 37a, 83 to 89a, 91, 107, 127, 174, 175, 187 | https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de | 2026-10-23 |
| QStV, SR 642.118.2, version of 10 January 2025 (current), art. 1 to 9, 12 | https://www.fedlex.admin.ch/eli/cc/2018/274/de | 2026-10-23 |
| ESTV, Wegleitung zum Ausfüllen des Lohnausweises, gültig ab 1. Januar 2026 | https://www.estv.admin.ch/dam/de/sd-web/afP1GDFr8gE3/dbst-form-lohna-wegleitung-2026-de.pdf | 2026-10-23 |
| Kantonales Steueramt Zürich, Quellensteuer abrechnen | https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/quellensteuer-abrechnen.html | 2026-10-23 |
| Kantonales Steueramt Zürich, Quellensteuer-Tarife | https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/quellensteuer-tarife.html | 2026-10-23 |
| Kantonales Steueramt Zürich, Quellensteuertarif A ohne Kirchensteuer, Ausgabe 2026 | https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/quellensteuer/quellensteuertarif/2026/p208840_QuellensteuerTarif_A_ohne_KS_ENT1.pdf | 2026-10-23 |

Not yet confirmed: a 2026 edition of AHV/IV sheet 2.08 (the 2025 edition was read; AVIG art. 3 and UVV art. 22 as in force on 1 January 2026 give the same 2.2% and CHF 148,200); a fixed calendar deadline for the Lohnausweis (none in the DBG or the 2026 Wegleitung; any cantonal deadline is not checked); cantonal FAK rates, who bears them in each canton, and the compensation funds' administration fees; UVG premium rates (insurer-specific); the commission rate and return frequency in cantons other than Zurich.
