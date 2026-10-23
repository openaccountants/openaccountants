---
name: de-employee-income-tax
description: "Use this skill for the annual German income tax return of an employee resident in Germany (Einkommensteuererklärung with Anlage N), tax year 2026, filed in 2027. Covers when an employee must file (§ 46 EStG: tax classes III/V or IV with factor, side income or wage replacement benefits over EUR 410, several employers) and when filing is voluntary (four years), the 2026 tariff, Arbeitnehmer-Pauschbetrag, Werbungskosten (commuting allowance at EUR 0.38 from the first km, home office day allowance, work equipment, training, union dues), Vorsorgeaufwendungen, Kinderfreibetrag against Kindergeld, Ehegattensplitting, single parent relief, household services (§ 35a), extraordinary burdens, solidarity surcharge, church tax, deadlines, late-filing surcharge and interest. Trigger on: Steuererklärung Arbeitnehmer, Anlage N, Werbungskosten, Pendlerpauschale, Homeoffice-Pauschale, Lohnsteuer Erstattung, tax refund Germany employee, Steuerklasse III V Pflichtveranlagung, Splittingtarif. Out of scope: payroll withholding (de-payroll, germany-payroll), self-employed income (de-income-tax), capital income (de-capital-gains), rent (de-rental-income), non-resident individuals."
jurisdiction: DE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Germany: income tax return for employees, tax year 2026 (Anlage N)

This skill works out the annual income tax of an employee who lives in Germany, from gross pay to the refund or extra payment against the wage tax (Lohnsteuer) the employer withheld. It is for the 2026 return, filed in 2027.

See also, and do not repeat here:

- **de-payroll** and **germany-payroll**: how the employer withholds Lohnsteuer, tax classes, the Vorsorgepauschale in payroll, social insurance rates and ceilings.
- **de-income-tax** and **de-einkommensteuer-freelancer**: self-employed and trade income (Anlage S, G, EÜR). de-income-tax is still on 2025 figures.
- **de-capital-gains**: investment income and the flat tax (Anlage KAP).
- **de-rental-income**: letting income (Anlage V).
- **de-social-contributions**: social insurance for the self-employed.
- **leaving-germany-exit-tax** and **germany-to-switzerland-cross-border-tax**: departures and the Swiss corridor.

## Who this applies to

- **In scope.** A person with a residence or habitual abode in Germany is fully liable to income tax on worldwide income (§ 1(1) EStG). This skill covers such a person whose income is mainly employment income (§ 19 EStG), with or without a spouse, with or without children.
- **Married couples and registered partners.** They may choose joint assessment (Zusammenveranlagung) if both are fully liable, not permanently separated, and met both conditions at some point in the year (§ 26(1) EStG). If neither chooses, joint assessment applies (§ 26(3) EStG).
- **Out of scope.** Non-residents with German wages (limited liability, § 1(4) EStG, or the § 1(3) election): no method here. Self-employed, trade, capital and rental income go to the sibling skills listed above, then the results come back into this return.

### When an employee must file (§ 46(2) EStG)

Where wage tax was withheld, the tax office assesses only in the listed cases. The common ones:

| Case | Rule |
|---|---|
| Side income | Income not subject to wage tax (for example rent or self-employment) over EUR 410 in total (no. 1) |
| Wage replacement benefits | Benefits under the progression rule (for example short-time work pay, parental allowance, unemployment benefit) over EUR 410 (no. 1) |
| Several employers at once | Wages from more than one employer at the same time, unless combined for wage tax (no. 2) |
| Health insurance refund | Refund of health and care insurance contributions over EUR 410, where wages exceed the basic allowance plus lump sums (no. 3, in this form from 1 January 2026 under § 52(36) EStG) |
| Married, both employed, class V, VI or IV with factor | Spouses assessed jointly, both had wages and one was taxed in class V or VI, or class IV with a factor (no. 3a) |
| Allowance on the wage tax card | A Freibetrag was entered in the wage tax data and wages exceed the basic allowance plus lump sums (no. 4) |
| One-time payments | Wage tax on a bonus computed without wages from earlier jobs in the year (code S) (no. 5a) |
| Marriage ended and remarried | In the same year (no. 6) |

In every other case filing is voluntary: an application for assessment, made by filing a return (§ 46(2) no. 8 EStG). The usual reason is a refund.

## Rates, bands and thresholds

All amounts are for tax year 2026.

| Item | Amount | Source |
|---|---|---|
| Basic allowance (Grundfreibetrag), zone 1 | EUR 0 to 12,348: no tax | https://www.gesetze-im-internet.de/estg/__32a.html |
| Zone 2 | EUR 12,349 to 17,799: (914.51 × y + 1,400) × y, y = (taxable income − 12,348) / 10,000 | Same |
| Zone 3 | EUR 17,800 to 69,878: (173.10 × z + 2,397) × z + 1,034.87, z = (taxable income − 17,799) / 10,000 | Same |
| Zone 4 (42%) | EUR 69,879 to 277,825: 0.42 × x − 11,135.63 | Same |
| Zone 5 (45%) | From EUR 277,826: 0.45 × x − 19,470.38 | Same |
| Rounding | Taxable income and tax both rounded down to whole euros | Same, § 32a(1) sentences 1 and 6 |
| Splitting for joint assessment | Twice the tax on half the joint taxable income | § 32a(5) EStG, same URL |
| Employee lump sum (Arbeitnehmer-Pauschbetrag) | EUR 1,230 unless higher costs are shown; union dues are deducted on top | https://www.gesetze-im-internet.de/estg/__9a.html |
| Commuting allowance (Entfernungspauschale) | EUR 0.38 per full km of one-way distance, from the first km, per day the first place of work is visited; cap EUR 4,500 a year unless an own or provided car is used | https://www.gesetze-im-internet.de/estg/__9.html (§ 9(1) sentence 3 no. 4); this text applies from 2026 under § 52(1) EStG |
| Home office day allowance (Tagespauschale) | EUR 6 per day worked mainly at home without visiting the first place of work; max EUR 1,260 a year | https://www.gesetze-im-internet.de/estg/__4.html (§ 4(5) sentence 1 no. 6c), applied to employees by § 9(5) EStG |
| Home office room (Arbeitszimmer), only if it is the centre of all work | Actual cost or EUR 1,260 a year flat | § 4(5) sentence 1 no. 6b EStG, same URL |
| Work equipment written off at once | Cost up to EUR 800 net of VAT per item | https://www.gesetze-im-internet.de/estg/__6.html (§ 6(2)), applied by § 9(1) sentence 3 no. 7 EStG |
| Second home for work (doppelte Haushaltsführung), rent | Up to EUR 1,000 a month in Germany | § 9(1) sentence 3 no. 5 EStG |
| First vocational training or study (no prior qualification, not within employment) | Special expense up to EUR 6,000 a year | https://www.gesetze-im-internet.de/estg/__10.html (§ 10(1) no. 7) |
| Pension contributions, cap | Up to the maximum contribution to the miners' pension scheme: EUR 124,800 × 24.7% = EUR 30,826 (rounded up); doubled for joint assessment. The tax-free employer share is then subtracted | § 10(3) EStG; ceiling: SVBezGrV 2026 § 4, https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf; rate: https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html |
| Other insurance (health, care, unemployment, liability, etc.), cap | EUR 1,900 for employees (employer pays towards health cover); EUR 2,800 otherwise; summed for spouses. Basic health and care cover is deductible in full even above the cap | § 10(4) EStG, same URL as § 10 |
| Statutory health contribution with sick-pay entitlement | Reduce by 4% before deducting | § 10(1) no. 3(a) sentence 4 EStG |
| Special expenses lump sum | EUR 36 (EUR 72 joint) | https://www.gesetze-im-internet.de/estg/__10c.html |
| Donations | Up to 20% of total income | https://www.gesetze-im-internet.de/estg/__10b.html |
| Child allowances (Freibeträge für Kinder) | EUR 3,414 plus EUR 1,464 per parent (EUR 4,878); EUR 9,756 per child for joint assessment | https://www.gesetze-im-internet.de/estg/__32.html (§ 32(6)); BMF monthly report Feb 2026 |
| Kindergeld | EUR 259 per child per month (EUR 3,108 a year) | https://www.gesetze-im-internet.de/estg/__66.html |
| Single parent relief (Entlastungsbetrag) | EUR 4,260 for one child, plus EUR 240 per further child; one twelfth less per month not met | https://www.gesetze-im-internet.de/estg/__24b.html |
| Household jobs: minijob in the household | Tax credit 20% of cost, max EUR 510 | https://www.gesetze-im-internet.de/estg/__35a.html |
| Household services and care | Tax credit 20% of cost, max EUR 4,000 | Same, § 35a(2) |
| Craftsmen's work at home | Tax credit 20% of labour cost, max EUR 1,200; invoice and bank transfer needed | Same, § 35a(3) and (5) |
| Extraordinary burdens: reasonable own share | Total income up to 15,340 / 15,341 to 51,130 / over 51,130: no children, basic tariff 5 / 6 / 7%; no children, splitting 4 / 5 / 6%; one or two children 2 / 3 / 4%; three or more 1 / 1 / 2% | https://www.gesetze-im-internet.de/estg/__33.html (§ 33(3)) |
| Maintenance of a dependant | Up to EUR 12,348 a year (the basic allowance), less the dependant's own income over EUR 624 | https://www.gesetze-im-internet.de/estg/__33a.html |
| Disability lump sum | EUR 384 (degree 20) up to EUR 2,840 (degree 100); EUR 7,400 if helpless or blind | https://www.gesetze-im-internet.de/estg/__33b.html |
| Solidarity surcharge | 5.5% of income tax; nothing while the tax (computed with child allowances) is at most EUR 20,350, or EUR 40,700 under splitting; above that, at most 11.9% of the excess | https://www.gesetze-im-internet.de/solzg_1995/__3.html and https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Church tax | 8% or 9% of income tax (computed with child allowances), by state | § 51a EStG https://www.gesetze-im-internet.de/estg/__51a.html; BMF booklet "Steuern von A bis Z" ("je nach Bundesland 8 oder 9 Prozent") |

## The taxable base

Work down this ladder. Each spouse computes their own employment income; the rest is joint under joint assessment (§ 26b EStG).

1. **Gross wages** from the wage tax certificate (Lohnsteuerbescheinigung), line 3. Tax-free items stay out.
2. **Less Werbungskosten**, or the EUR 1,230 lump sum if higher. Common items:
   - **Commuting:** full km of the shortest road distance × EUR 0.38 × days at the first place of work. Public transport costs above the allowance count instead (§ 9(2) EStG). Tax-free employer travel benefits reduce it.
   - **Home office:** EUR 6 for each day worked mainly at home where the employee did not go to the first place of work. A day is either a commuting day or a home office day, not both, unless no other workplace is available at all (§ 4(5) no. 6c sentence 2 EStG).
   - **Work equipment:** laptop, tools, typical work clothing; items over EUR 800 net are depreciated over their useful life.
   - **Training** for the current or a future job, after a first qualification (§ 9(6) EStG).
   - **Union dues:** from 2026 deducted in addition to the lump sum (§ 9a sentence 3 EStG).
   - Business travel, removal for work, second household, job application costs, account fees for salary.
   = **Income from employment.**
3. **Add other income** (from the sibling skills) to get total income (Gesamtbetrag der Einkünfte), less the single parent relief where it applies.
4. **Less special expenses (Sonderausgaben):**
   - Pension contributions: employee plus employer share to the statutory scheme, up to the cap, minus the tax-free employer share. In practice: the employee share.
   - Basic health and care insurance (employee share; statutory health reduced by 4% where sick pay is covered). Unemployment, disability and liability insurance count only while the EUR 1,900 cap is not already used by basic health and care (§ 10(4) sentence 4 EStG). For most employees it is.
   - Church tax paid, donations, first training up to EUR 6,000, childcare (§ 10(1) no. 5 EStG), or the EUR 36 lump sum.
5. **Less extraordinary burdens** above the reasonable own share, maintenance payments, disability lump sums.
   = **Income (Einkommen).**
6. **Child allowances or Kindergeld (§ 31 EStG).** The tax office compares. If the tax saving from the allowances is greater than the year's Kindergeld, it deducts the allowances and adds the Kindergeld to the tax. Otherwise Kindergeld stands and no allowance is deducted. The allowances are always used for the solidarity surcharge and church tax base (§ 3(2) SolzG, § 51a(2) EStG).
   = **Taxable income (zu versteuerndes Einkommen)**, rounded down to euros.
7. **Tariff tax** (basic or splitting). Wage replacement benefits and treaty-exempt foreign pay raise the rate but are not taxed themselves (§ 32b EStG).
8. **Less tax credits:** § 35a household services and craftsmen.
9. **Plus solidarity surcharge and church tax.**
10. **Less wage tax, surcharge and church tax withheld** (certificate lines 4 to 7). The difference is the refund or extra payment.

**Losses.** A loss from another income type (for example rental) reduces employment income in the same year. A remaining loss can be carried back one year or forward without time limit under § 10d EStG; that mechanism is not set out here.

## Deadlines and filing

| Step | Rule |
|---|---|
| Form | Main form (Hauptvordruck) with Anlage N per employed spouse, Anlage Vorsorgeaufwand, Anlage Kind per child, Anlage Haushaltsnahe Aufwendungen, Anlage Sonderausgaben, Anlage Außergewöhnliche Belastungen, Anlage N-AUS for foreign pay. Form names from the ELSTER 2025 guide; the 2026 forms are not yet published |
| Channel | ELSTER (Mein ELSTER or third-party software). Paper is allowed for an employee with no business income, or with side income under EUR 410 (ELSTER 2025 guide) |
| Mandatory filers, own return | By 31 July 2027 (seven months after year end, § 149(2) AO). 31 July 2027 is a Saturday, so the deadline moves to Monday 2 August 2027 (§ 108(3) AO) |
| Mandatory filers, prepared by a tax adviser | By the last day of February of the second following year (§ 149(3) AO): 29 February 2028. Unlike 2020 to 2024, no special extension applies to 2026 (Art. 97 § 36 EGAO covers only up to 2024). The tax office can call for an earlier return (§ 149(4) AO) |
| Voluntary filers | Four-year assessment period (§ 169(2) no. 2 AO), starting at the end of 2026 because there is no duty to file (§ 170(1) AO): the 2026 return must reach the tax office by 31 December 2030. The ELSTER 2025 guide states the same rule for 2025 (31 December 2029) and says it cannot be extended |
| Payment | An extra payment is due one month after the notice (§ 36(4) EStG). The tax office may also set quarterly prepayments for later years |

## Penalties and interest

- **Late-filing surcharge (§ 152 AO).** Only for mandatory filers. The tax office may set it after a late return. It must set it if the return is not in within 14 months after year end (for 2026: by 29 February 2028) unless an extension was granted, the tax is nil, or the tax does not exceed the wage tax withheld and prepayments (§ 152(2) and (3) AO). Amount: 0.25% per month or part month of the tax less withheld tax and prepayments, at least EUR 25 per month, at most EUR 25,000 (§ 152(5) and (10) AO). An employee due a refund is not hit by the mandatory surcharge.
- **Interest on the balance (§ 233a AO).** Runs from 15 months after year end, so from 1 April 2028 for 2026, until the notice takes effect. 0.15% per full month, 1.8% a year (§ 238(1a) AO), on the balance rounded down to EUR 50. Refunds earn the same interest, at the earliest from the day the tax was paid.
- **Late payment (§ 240 AO).** 1% per started month on the overdue amount rounded down to EUR 50.

## Cross-border points

- **Foreign pay of a resident.** Pay exempt in Germany under a tax treaty is still declared (Anlage N-AUS) and raises the rate on the rest (§ 32b EStG). Foreign tax credits under § 34c EStG are not covered here.
- **Moving in or out in 2026.** Months of limited liability and German-exempt foreign income are handled under § 2(7) and § 32b EStG; the pack has no method yet. For shares and departure rules see leaving-germany-exit-tax.
- **Spouse living abroad.** An EU/EEA national may get joint assessment with a spouse resident in the EU/EEA under § 1a EStG; filing is then mandatory (§ 46(2) no. 7 EStG). Not covered further.
- **Non-residents with German pay** (§ 1(3) election, § 46(2) no. 9 EStG) and Swiss cross-border commuters: refuse here. The commuter case belongs in germany-to-switzerland-cross-border-tax, which does not yet have its commuter part.

## Worked examples

### Example 1: single employee, EUR 55,000, commuter with home office days

Lena is 30, single, no children, not a church member, works in Hesse, statutory health insurance with a fund additional rate of 2.9%. Gross 2026 pay EUR 55,000, all under the health ceiling of EUR 69,750. She went to the office on 120 days (30 km one way) and worked from home on 100 days. Work equipment EUR 250. Her wage tax certificate shows Lohnsteuer withheld of EUR 8,060 and no solidarity surcharge. (Invented case; EUR 8,060 is what the 2026 payroll formula in de-payroll gives for class I with these facts.)

- Commuting: 120 × 30 × 0.38 = EUR 1,368. Home office: 100 × 6 = EUR 600. Equipment EUR 250. Werbungskosten EUR 2,218, above the EUR 1,230 lump sum.
- Employment income: 55,000 − 2,218 = EUR 52,782.
- Pension: employee share 9.3% = EUR 5,115 (total contributions 10,230, under the EUR 30,826 cap, minus the employer's 5,115).
- Health: (7.3% + 1.45%) × 55,000 = 4,812.50, less 4% = EUR 4,620. Care, childless over 23: 2.4% = EUR 1,320. Basic health and care EUR 5,940 already exceed the EUR 1,900 cap, so unemployment insurance adds nothing.
- Special expenses lump sum EUR 36.
- Taxable income: 52,782 − 11,055 − 36 = EUR 41,691, zone 3.
- Tax: z = 2.3892; (173.10 × 2.3892 + 2,397) × 2.3892 + 1,034.87 = 7,749.88, rounded down EUR 7,749. Below EUR 20,350, so no solidarity surcharge.
- Refund: 8,060 − 7,749 = EUR 311. She is not obliged to file (no § 46(2) case) and can claim it until 31 December 2030.

```oa-check
name: DE employee 2026, single, EUR 55,000, 30 km commute, 100 home office days
inputs:
  gross: 55000
  office_days: 120
  km: 30
  home_days: 100
  equipment: 250
  lohnsteuer_withheld: 8060
steps:
  - commuting: office_days * km * 0.38
  - home_office: min(home_days * 6, 1260)
  - werbungskosten: max(commuting + home_office + equipment, 1230)
  - employment_income: gross - werbungskosten
  - pension: gross * 0.093
  - health: gross * (0.073 + 0.0145) * 0.96
  - care: gross * 0.024
  - vorsorge: pension + health + care
  - taxable: floor(employment_income - vorsorge - 36)
  - z: (taxable - 17799) / 10000
  - tax: floor((173.10 * z + 2397) * z + 1034.87)
  - soli: 0
  - refund: lohnsteuer_withheld - tax - soli
expected:
  werbungskosten: 2218
  vorsorge: 11055
  taxable: 41691
  tax: 7749
  refund: 311
```

### Example 2: married couple, classes III and V, one child, splitting

Jonas earns EUR 72,000 (class III, 15 km on 200 days, so commuting is EUR 1,140 and the EUR 1,230 lump sum is higher). Mia earns EUR 18,000 (class V) and pays EUR 200 union dues; she has no other job costs. One child, Kindergeld EUR 3,108 for the year. Both in statutory health insurance at a 2.9% additional rate, no church. Because one spouse was in class V, they must file (§ 46(2) no. 3a EStG). Wage tax withheld on both certificates together: EUR 11,900 (invented).

- Jonas: 72,000 − 1,230 = EUR 70,770. Mia: 18,000 − 1,230 − 200 = EUR 16,570 (union dues on top of the lump sum, new for 2026). Total EUR 87,340.
- Pension, employee shares: 6,696 + 1,674 = EUR 8,370.
- Health: Jonas on the ceiling, 69,750 × 8.75% × 0.96 = 5,859; Mia 18,000 × 8.75% × 0.96 = 1,512. Care with a child, 1.8%: 1,255.50 and 324. Basic cover EUR 8,950.50 is above the joint cap of EUR 3,800, so it counts in full and unemployment insurance drops out.
- Taxable income before child allowances: 87,340 − 17,320.50 − 72 = 69,947.50, rounded down EUR 69,947.
- Splitting: tax on 34,973 = 5,662, doubled EUR 11,324.
- With child allowances (EUR 9,756): taxable EUR 60,191, splitting tax 2 × 4,243 = EUR 8,486. Saving EUR 2,838 is less than Kindergeld of EUR 3,108, so Kindergeld stands and the income tax is EUR 11,324.
- Surcharge base is EUR 8,486 (with allowances), below EUR 40,700: no surcharge.
- Refund: 11,900 − 11,324 = EUR 576.

```oa-check
name: DE married couple 2026, splitting, one child, Kindergeld check
inputs:
  gross_a: 72000
  gross_b: 18000
  union_dues_b: 200
  health_ceiling: 69750
  kindergeld_year: 3108
  withheld: 11900
steps:
  - income_a: gross_a - 1230
  - income_b: gross_b - 1230 - union_dues_b
  - pension: (gross_a + gross_b) * 0.093
  - health: (min(gross_a, health_ceiling) + gross_b) * 0.0875 * 0.96
  - care: (min(gross_a, health_ceiling) + gross_b) * 0.018
  - vorsorge: pension + health + care
  - taxable: floor(income_a + income_b - vorsorge - 72)
  - half: floor(taxable / 2)
  - z: (half - 17799) / 10000
  - tax_split: 2 * floor((173.10 * z + 2397) * z + 1034.87)
  - taxable_kfb: floor(income_a + income_b - vorsorge - 72 - 9756)
  - half_kfb: floor(taxable_kfb / 2)
  - zk: (half_kfb - 17799) / 10000
  - tax_kfb: 2 * floor((173.10 * zk + 2397) * zk + 1034.87)
  - allowance_saving: tax_split - tax_kfb
  - income_tax: min(tax_split, tax_kfb + kindergeld_year)
  - refund: withheld - income_tax
expected:
  vorsorge: 17320.50
  taxable: 69947
  tax_split: 11324
  tax_kfb: 8486
  allowance_saving: 2838
  income_tax: 11324
  refund: 576
```

`income_tax` takes the lower of the two routes: with allowances the tax is 8,486 plus the Kindergeld added back, 3,108, which is 11,594; without them it is 11,324, so the allowance route is not used. Both examples use only zone 3 of the tariff because the taxable amounts fall in it; a different case must pick its zone first.

## Ask the client first

1. Tax class in 2026, and for a couple, both wage tax certificates. A class III/V or IV-with-factor couple must file.
2. Any income without wage tax (rent, freelance, foreign pay) or wage replacement benefits (parental allowance, short-time work pay). Over EUR 410 makes filing mandatory and brings in other forms.
3. Office days and home office days, and the one-way road distance. These decide the Werbungskosten and whether they beat EUR 1,230.
4. Health insurance: statutory or private, the fund's additional rate, and any refunds received.
5. Children: dates of birth, Kindergeld received, whether they live in the household, and for a single parent whether another adult lives there.
6. Church membership and state of residence (8% or 9%).

## Sources

| Source | URL | Read on |
|---|---|---|
| EStG § 4 (home office allowances) | https://www.gesetze-im-internet.de/estg/__4.html | 2026-10-23 |
| EStG § 6 (low-value assets, EUR 800) | https://www.gesetze-im-internet.de/estg/__6.html | 2026-10-23 |
| EStG § 9 (Werbungskosten, commuting EUR 0.38) | https://www.gesetze-im-internet.de/estg/__9.html | 2026-10-23 |
| EStG § 9a (lump sum EUR 1,230, union dues) | https://www.gesetze-im-internet.de/estg/__9a.html | 2026-10-23 |
| EStG § 10 (special expenses, caps) | https://www.gesetze-im-internet.de/estg/__10.html | 2026-10-23 |
| EStG § 10b (donations) | https://www.gesetze-im-internet.de/estg/__10b.html | 2026-10-23 |
| EStG § 10c (lump sum EUR 36) | https://www.gesetze-im-internet.de/estg/__10c.html | 2026-10-23 |
| EStG § 24b (single parent relief) | https://www.gesetze-im-internet.de/estg/__24b.html | 2026-10-23 |
| EStG §§ 26, 26b (joint assessment) | https://www.gesetze-im-internet.de/estg/__26.html | 2026-10-23 |
| EStG § 31 (Kindergeld comparison) | https://www.gesetze-im-internet.de/estg/__31.html | 2026-10-23 |
| EStG § 32 (child allowances) | https://www.gesetze-im-internet.de/estg/__32.html | 2026-10-23 |
| EStG § 32a (2026 tariff, splitting) | https://www.gesetze-im-internet.de/estg/__32a.html | 2026-10-23 |
| EStG §§ 33, 33a, 33b (extraordinary burdens) | https://www.gesetze-im-internet.de/estg/__33.html | 2026-10-23 |
| EStG § 35a (household services) | https://www.gesetze-im-internet.de/estg/__35a.html | 2026-10-23 |
| EStG § 36 (payment of balance) | https://www.gesetze-im-internet.de/estg/__36.html | 2026-10-23 |
| EStG § 46 (when employees are assessed) | https://www.gesetze-im-internet.de/estg/__46.html | 2026-10-23 |
| EStG § 51a (church tax base) | https://www.gesetze-im-internet.de/estg/__51a.html | 2026-10-23 |
| EStG § 52 (this version applies from 2026) | https://www.gesetze-im-internet.de/estg/__52.html | 2026-10-23 |
| EStG § 66 (Kindergeld EUR 259) | https://www.gesetze-im-internet.de/estg/__66.html | 2026-10-23 |
| SolzG §§ 3, 4 | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-10-23 |
| AO §§ 108, 149, 152, 169, 170, 233a, 238, 240 | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-10-23 |
| EGAO Art. 97 § 36 (extensions end with 2024) | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-10-23 |
| SVBezGrV 2026 (miners' pension ceiling EUR 124,800) | https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf | 2026-10-23 |
| RVBeitrSBek 2026 (pension rates 18.6% and 24.7%) | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html | 2026-10-23 |
| BMF monthly report Feb 2026, main tax changes 2026 | https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2026/02/Inhalte/Kapitel-2-Analysen/2-5-wichtigste-steuerliche-aenderungen-2026.html | 2026-10-23 |
| BMF booklet "Steuern von A bis Z" (church tax 8 or 9%) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf | 2026-10-23 |
| ELSTER, guide to the 2025 income tax return (forms, filing duty, voluntary deadline) | https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025 | 2026-10-23 |

Not yet confirmed: the 2026 form set and line numbers (ELSTER has not published the 2026 guide; the form names above are from 2025); which states charge 8% and which 9% church tax (state law, not on a federal page); the employee rates in the examples (health additional rate 2.9% and care 2.4% / 1.8%) are taken from de-payroll, not re-read today.
