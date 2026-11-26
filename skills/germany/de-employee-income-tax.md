---
name: de-employee-income-tax
description: "German resident employee income tax return for 2026 (Anlage N), filed in 2027: mandatory and voluntary assessment, tariff and splitting, employment expenses, statutory insurance deductions, child comparison, solidarity surcharge, deadlines and payment. Retains the original single and married cases as arithmetic audits with explicit holds for missing eligibility and payroll evidence. Refers specialist deductions, church tax and cross-border outcomes to a partner accountant. Trigger on Steuererklärung Arbeitnehmer, Anlage N, Werbungskosten, Pendlerpauschale, Homeoffice-Pauschale, Lohnsteuer Erstattung and Steuerklasse III/V. Payroll, freelance, investment, rental and non-resident computations use the related Guides."
version: 0.8
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-26
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Germany: income tax return for employees, tax year 2026 (Anlage N)

Use the annual taxable income and the 2026 tariff below, then reconcile the assessed tax with the wage tax actually withheld. Do not infer deductible insurance or a final refund from annual gross pay alone.

## Who this applies to

An employee resident or habitually resident in Germany is subject to unlimited income tax liability (§ 1(1) EStG). Employment receipts include salary, wages and employment benefits (§ 19(1) EStG). This Guide covers the resident employee's 2026 return, filed in 2027.

Spouses may choose joint assessment if both meet § 26(1)'s unlimited-liability condition and are not permanently separated, with these conditions present at the start of or arising during the year. Either spouse choosing individual assessment prevents joint assessment; without a valid election, joint assessment applies. The spouse rules also apply to registered civil partners (§§ 2(8), 26 EStG). Under joint assessment the spouses' separately determined income is combined (§ 26b).

Use `de-payroll` for withholding, `germany-income-tax` and `de-einkommensteuer-freelancer` for freelance/trade income, `de-capital-gains` for investments, `de-rental-income` for rent and `de-social-contributions` for self-employed social insurance. Non-residents use `de-non-resident-tax`; departures, part-year residence and Swiss commuters use `leaving-germany-exit-tax`, `de-partners-and-part-year` and `germany-to-switzerland-cross-border-tax`, within their own source limits.

### When an employee must file

For income including wages from which tax was deducted, these are common assessment triggers under [§ 46(2) EStG](https://www.gesetze-im-internet.de/estg/__46.html), not an exhaustive list. An individual tax-office demand also creates a filing duty ([§ 149(1) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html)).

| Case | Condition |
|---|---|
| Side income or progression income | Positive taxable income not subject to wage withholding, reduced by the attributable § 13(3) and § 24a amounts, exceeds EUR 410; separately, a positive total of progression income and benefits exceeds EUR 410 (no. 1). This is income, not gross turnover. |
| Concurrent employers | Wages from several employers at the same time, except wages combined under § 38(3a) sentence 7 for withholding (no. 2). |
| Health/care refund | Refund of § 10(1) no. 3 contributions exceeds EUR 410 and annual wages exceed basic allowance + employee lump sum + special-expense lump sum. For spouses satisfying § 26(1), use double the basic allowance and special-expense lump sum, but one employee lump sum (no. 3; applies from 2026 under § 52(36)). |
| Both spouses earned wages | Spouses within §§ 26, 26b; one had class V or VI, or class IV with a factor, for all or part of the year (no. 3a). Class III alone does not settle the duty. |
| Entered wage-tax allowance | Only a Freibetrag under § 39a(1) sentence 1 nos. 1–3, 5 or 6; the same wage thresholds as the refund row apply (no. 4). |
| Bonus code S | Earlier employment wages were left out of the bonus withholding computation (no. 5a). |
| Marriage ended and remarriage | The marriage ended by death, divorce or annulment in the year and either former spouse remarried that year (no. 6). |

Only after excluding all applicable mandatory cases and a tax-office demand use voluntary assessment, requested by filing the return (§ 46(2) no. 8).

## Rates, bands and thresholds

The tariff applies to **taxable income**, not gross salary. Select the zone first. Special tariffs and progression cases require the referral below.

| Item | 2026 rule | Official source |
|---|---|---|
| Basic allowance, zone 1 | EUR 0–12,348: tax EUR 0 | https://www.gesetze-im-internet.de/estg/__32a.html § 32a(1) |
| Zone 2 | EUR 12,349–17,799: (914.51 × y + 1,400) × y; y is one ten-thousandth of x − 12,348 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Zone 3 | EUR 17,800–69,878: (173.10 × z + 2,397) × z + 1,034.87; z is one ten-thousandth of x − 17,799 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Zone 4 | EUR 69,879–277,825: 0.42 × x − 11,135.63 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Zone 5 | From EUR 277,826: 0.45 × x − 19,470.38 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Rounding | x is taxable income rounded down to whole euros; round the resulting tax down to whole euros | https://www.gesetze-im-internet.de/estg/__32a.html § 32a(1) |
| Joint splitting | Twice the § 32a(1) tax on half the joint taxable income, with that paragraph's rounding | https://www.gesetze-im-internet.de/estg/__32a.html § 32a(5) |
| Employee lump sum | EUR 1,230 if higher employment expenses are not proved; limited to receipts. Qualifying union dues are additional to the lump sum, but do not deduct them twice when using actual expenses | https://www.gesetze-im-internet.de/estg/__9a.html |
| Commuting | EUR 0.38 per full one-way km for each day attending the first workplace; EUR 4,500 annual cap unless an own/provided car is used. No flight routes or tax-free collective transport. Shortest road route, or an obviously more convenient route used regularly; eligible excess annual public-transport cost may replace the allowance. For employer benefits, multiple homes or disability-related special travel rules: Check this point with one of our partner accountants. | https://www.gesetze-im-internet.de/estg/__9.html § 9(1) no. 4 and (2) |
| Home working day | EUR 6, maximum EUR 1,260 per year across all work, when work is predominantly at home and no first workplace is visited. If permanently no other workplace is available, the day allowance may also apply on external/office days. No deduction insofar as accommodation costs can be deducted under § 4(5) no. 6a/§ 9(1) no. 5 or a room deduction is taken under no. 6b | https://www.gesetze-im-internet.de/estg/__4.html § 4(5) no. 6c; employee bridge https://www.gesetze-im-internet.de/estg/__9.html § 9(5) |
| Work equipment | Immediate deduction election for qualifying depreciable movable equipment capable of independent use, with cost excluding VAT not exceeding EUR 800 per item (the deductible cost includes VAT under R 9.12); otherwise establish the applicable depreciation treatment, rather than automatically expensing it | https://www.gesetze-im-internet.de/estg/__6.html § 6(2) sentences 1–3; employee bridge https://www.gesetze-im-internet.de/estg/__9.html § 9(1) nos. 6–7; https://ao.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/II-Einkommen-2-24b/4-Ueberschuss-d-Einnahmen-ueber-die-Werbungsk-8-9a/Paragraf-9/r-9-12.html R 9.12 |
| Statutory pension deduction | Add the tax-free employer share, apply the cap, then subtract that share. General cap (computed): ceil(EUR 124,800 × 24.7%) = EUR 30,826, doubled jointly; § 10(3) sentence 3 requires reductions for the specified pension-exempt/other pension-entitlement groups. Do not assume every employee has the unreduced cap | https://www.gesetze-im-internet.de/estg/__10.html § 10(1) no. 2 and (3); https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html; https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html |
| Basic health and compulsory care | Deduct qualifying actual contributions; statutory health contributions giving sick-pay entitlement are reduced by 4%. Account for refunds and tax-free subsidies; foreign-tax-free-income and provider conditions are in § 10(2) | https://www.gesetze-im-internet.de/estg/__10.html § 10(1) no. 3, (2), (4b) |
| Other insurance cap | EUR 2,800, reduced to EUR 1,900 for the groups in § 10(4) sentence 2, including employer-subsidised health cover; spouses add their individual caps. If deductible basic health/care exceeds the cap, deduct that basic cover and no additional no. 3a insurance | https://www.gesetze-im-internet.de/estg/__10.html § 10(4) |
| Special-expense lump sum | EUR 36, EUR 72 jointly, if no higher expenses in the categories listed in § 10c are proved; insurance deductions are separate | https://www.gesetze-im-internet.de/estg/__10c.html |
| Child allowances | EUR 3,414 + EUR 1,464 per eligible child per parent; doubled to a derived EUR 9,756 jointly only where the child has the required relationship to both spouses. Reduce by 1/12 per ineligible month; residence reductions, transfers and identification requirements also apply | https://www.gesetze-im-internet.de/estg/__32.html § 32(6) |
| Kindergeld | EUR 259 per eligible month; EUR 3,108 (computed: 259 × 12) only for twelve eligible months | https://www.gesetze-im-internet.de/estg/__66.html |
| Solidarity surcharge | Recompute income tax with eligible child allowances in every § 32 case, without the Kindergeld add-back (§ 3(2) deviates from § 2(6) EStG). For 2026, no surcharge on the non-§ 32d(3)/(4) base up to EUR 20,350, or EUR 40,700 under § 32a(5)/(6). Above it take the lesser of 5.5% of that base and 11.9% of its excess over the limit; § 32d(3)/(4) tax separately bears 5.5%. Drop fractions of a cent | https://www.gesetze-im-internet.de/solzg_1995/__3.html §§ 3(2)–(3); https://www.gesetze-im-internet.de/solzg_1995/__4.html |

## The taxable base

1. Reconcile gross taxable employment receipts to the actual wage certificates. Determine each spouse's employment expenses or lump sum separately, then combine income for a valid joint assessment (§§ 9, 9a, 26b).
2. Include other assessed income only after the relevant Guide has established it. The sum of income less the applicable § 2(3) reliefs is total income; less special expenses and extraordinary burdens is income (§ 2(2)–(4)). Use actual deductible insurance amounts supported by the certificates and insurer data, not assumed percentages of annual salary.
3. Apply child allowances only after establishing § 32 eligibility. The tax office compares the allowance route with the Kindergeld **entitlement**, not simply the cash received. If allowances are needed for the statutory tax exemption, add the corresponding entitlement to the tariff tax; § 31 excludes months covered by its § 70(1) sentence 2 non-payment exception. Otherwise the Kindergeld route stands (§ 31).
4. Apply the appropriate tariff to taxable income, then applicable credits, the correct surcharge and church-tax calculations, and finally credit the attributable withholding and prepayments (§§ 2(5)–(6), 36). A referred item below is a hold on the completed return, not permission to treat that item as zero.

## Deadlines and filing

| Step | Rule and source |
|---|---|
| Form and channel | Form topics retained: Hauptvordruck, Anlage N for each employed spouse, Vorsorgeaufwand, Kind, Haushaltsnahe Aufwendungen, Sonderausgaben, Außergewöhnliche Belastungen and N-AUS. Use Mein ELSTER or appropriate software only after establishing the correct 2026 form/field mapping; 2025 guidance does not prove it. For this mapping: Check this point with one of our partner accountants. https://www.elster.de/elsterweb/helpGlobal?themaGlobal=help_est_ufa_10_2025 |
| Electronic filing | Required by § 25(4) where agricultural, trade or self-employed income is earned and the assessment is not a § 46(2) nos. 2–8 case; hardship waiver on application. This provision does not compel an ordinary wages-only filer to file electronically. https://www.gesetze-im-internet.de/estg/__25.html |
| Mandatory, own return | General seven-month deadline: 31 July 2027 is Saturday, moving it to Monday 2 August 2027. An individual demand/extension must be checked. https://www.gesetze-im-internet.de/ao_1977/__149.html § 149(1)–(2); https://www.gesetze-im-internet.de/ao_1977/__108.html § 108(3) |
| Mandatory, authorised adviser | Normally 29 February 2028 under § 149(3), subject to an earlier § 149(4) demand. This extension excludes § 46(2) no. 8 voluntary returns. Pandemic extensions cover earlier periods, not 2026. https://www.gesetze-im-internet.de/ao_1977/__149.html; https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html |
| Voluntary | Ordinary four-year assessment period, starting at the end of 2026: submit by 31 December 2030, provided there is no mandatory duty. https://www.gesetze-im-internet.de/ao_1977/__169.html § 169(2) no. 2; https://www.gesetze-im-internet.de/ao_1977/__170.html § 170(1) |
| Reconciliation/payment | Credit applicable withholding and paid prepayments. An assessed balance is generally payable within one month after notification; already-due unpaid prepayments are immediately payable. A refund is paid after notification. https://www.gesetze-im-internet.de/estg/__36.html §§ 36(2)–(4) |

## Penalties and interest

- **Late filing:** discretionary surcharge under § 152(1), with excuse protection; ordinarily mandatory after 14 months (29 February 2028 for 2026), or an earlier § 149(4) demand deadline. Extensions, nil/negative tax and tax not exceeding prepayments plus creditable withholding exclude the automatic rule, but do not abolish discretion. For an annual return: 0.25% per started late month of assessed tax less those credits, minimum EUR 25 monthly, rounded down to euros, maximum EUR 25,000. The special first-demand rule in § 152(5) sentence 3 can shorten the chargeable period. [AO § 152(1)–(5), (10)](https://www.gesetze-im-internet.de/ao_1977/__152.html).
- **Assessment interest:** ordinary 2026 employee balances run from 1 April 2028, fifteen months after year-end, until assessment takes effect. Under §§ 233a/238 it is 0.15% per full month (1.8% annually), on the prescribed difference rounded down to EUR 50; refund interest is limited to the refundable amount and starts no earlier than payment, with separate periods for multiple payments. Retrospective events/loss carrybacks have a different start under § 233a(2a): refer these. [AO § 233a(1)–(3)](https://www.gesetze-im-internet.de/ao_1977/__233a.html), [§ 238](https://www.gesetze-im-internet.de/ao_1977/__238.html).
- **Late payment:** 1% per started month on assessed/declared overdue tax rounded down to EUR 50. No surcharge for delay up to three days, except payments within § 224(2) no. 1; no surcharge on ancillary tax charges. [AO § 240(1)–(3)](https://www.gesetze-im-internet.de/ao_1977/__240.html).

## Cross-border points

These topics remain within the intake. The abbreviated old rules do not establish an outcome; do not calculate them from the former headline rate/cap alone.

| Topic | Final action |
|---|---|
| Home-office room and annual room allowance | Check this point with one of our partner accountants. |
| Second household, business travel, work-related moving, applications and salary-account costs | Check this point with one of our partner accountants. |
| First education and later vocational training | Check this point with one of our partner accountants. |
| Donations, deductible church tax paid and childcare | Check this point with one of our partner accountants. |
| Single-parent relief and household/adult eligibility | Check this point with one of our partner accountants. |
| Household minijob, household/care services and craftsmen credits | Check this point with one of our partner accountants. |
| Extraordinary burdens and the progressive reasonable-own-share calculation | Check this point with one of our partner accountants. |
| Dependant maintenance | Check this point with one of our partner accountants. |
| Disability and related lump sums | Check this point with one of our partner accountants. |
| Loss offset, carryback/forward and retrospective-event interest | Check this point with one of our partner accountants. |
| Church membership/state rates, child-adjusted base, partial-income method, trade-tax-credit adjustment, mixed-faith couples, special Kirchgeld, caps and rounding | Check this point with one of our partner accountants. |
| Foreign pay, wage replacement benefits/progression, foreign tax credit, part-year residence, spouse abroad and Swiss commuter treatment | Check this point with one of our partner accountants. |
| Later-year quarterly prepayments | Check this point with one of our partner accountants. |

## Worked examples

Both original 2026 cases are retained below. **These are audits of the former numerical model, not filing results.** Recomputing arithmetic cannot supply missing legal or factual eligibility. Do not use the historical checkpoint deductions or the final balances as deductible amounts/refunds until supported by the actual records.

### Example 1: original single-employee case, on hold

Lena, 30, single, no children, no church membership, Hesse; 2026 gross pay EUR 55,000; statutory health cover with an assumed fund additional rate of 2.9%; 120 office days, 30 km one way, 100 days working from home; equipment EUR 250; stipulated certificate wage tax EUR 8,060, no solidarity withholding. The EUR 8,060 is retained as the original input, not as a verified output of a payroll formula.

The old expense model recomputes to 120 × 30 × 0.38 + 100 × 6 + 250 = EUR 2,218. It requires the actual first-workplace/route/employer-benefit facts, qualifying home days and deductible equipment use. The record does not establish them. The former insurance model was EUR 5,115 pension + EUR 4,620 health + EUR 1,320 care = EUR 11,055; annual gross and the assumed fund rate do not establish those actual deductible contributions.

Auditing that former model only: 55,000 − 2,218 = 52,782; 52,782 − 11,055 − 36 = 41,691. At this checkpoint, z = 2.3892 and raw tariff tax is EUR 7,749.885086384, floored to EUR 7,749. The arithmetic difference from EUR 8,060 is EUR 311, with a zero surcharge at this checkpoint base. **The EUR 311 refund conclusion is withdrawn pending evidence.** For the missing expense/insurance conditions and final return: Check this point with one of our partner accountants.

```oa-check
name: Original DE single 2026 arithmetic audit only, outcome on hold
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
  - historical_balance: lohnsteuer_withheld - tax - soli
expected:
  werbungskosten: 2218
  vorsorge: 11055
  taxable: 41691
  tax: 7749
  historical_balance: 311
```

### Example 2: original married case, on hold

Jonas earns EUR 72,000, class III, 15 km on 200 days. Mia earns EUR 18,000, class V, pays EUR 200 union dues and has no other job costs. The original record says one child and EUR 3,108 annual Kindergeld; both have statutory health cover at an assumed 2.9% additional rate, work outside Saxony and have no church membership. Stipulated fictional withholding inputs remain EUR 7,564 and EUR 1,850, total EUR 9,414, not computed payroll outputs.

Expense arithmetic: commuting 200 × 15 × 0.38 = EUR 1,140; the EUR 1,230 lump sum is higher for Jonas. Mia's lump sum plus qualifying union dues gives 18,000 − 1,230 − 200 = EUR 16,570; Jonas has EUR 70,770; total EUR 87,340.

The old contribution model recomputes pension EUR 6,696 + 1,674 = 8,370; health EUR 5,859 + 1,512 = 7,371; care EUR 1,255.50 + 324 = 1,579.50, using the old EUR 69,750 ceiling input. Total EUR 17,320.50. **These are not established employee deductions.** Mia's annual EUR 18,000 does not establish regular monthly remuneration, employment duration or transition-range treatment. [SGB IV § 20(2)–(2a)](https://www.gesetze-im-internet.de/sgb_4/__20.html) provides a transition range up to regular monthly EUR 2,000 and a separate employee-contribution basis, with an occupational-training exception. Do not invent a monthly pay pattern. The child's age, eligible months, residence and relationship to both spouses are also unstated.

The old model's checkpoint is 87,340 − 17,320.50 − 72 = EUR 69,947.50, floored to 69,947. Splitting gives 2 × tax(34,973) = EUR 11,324. Applying the old full-child-allowance input EUR 9,756 gives taxable 60,191 and 2 × tax(30,095) = EUR 8,486. The arithmetic saving is EUR 2,838, below the EUR 3,108 input; the allowance route plus that input is EUR 11,594 versus EUR 11,324. The child-adjusted checkpoint surcharge is zero. 11,324 − 9,414 = EUR 1,910. **The EUR 1,910 extra-payment conclusion is withdrawn.** For verified contributions, child eligibility, joint-assessment conditions and the final return: Check this point with one of our partner accountants.

```oa-check
name: Original DE married 2026 arithmetic audit only, outcome on hold
inputs:
  gross_a: 72000
  gross_b: 18000
  union_dues_b: 200
  health_ceiling: 69750
  kindergeld_year: 3108
  withheld: 9414
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
  - historical_tax: min(tax_split, tax_kfb + kindergeld_year)
  - historical_balance: historical_tax - withheld
expected:
  vorsorge: 17320.50
  taxable: 69947
  tax_split: 11324
  tax_kfb: 8486
  allowance_saving: 2838
  historical_tax: 11324
  historical_balance: 1910
```

## Ask the client first

Obtain the actual 2026 wage/insurance records and refunds, tax-office demands, both spouses' assessment choices and tax classes, other income/benefits, verified workplace/route/day records, work-equipment use, child eligibility/entitlement records, church membership and state. For any referred item obtain the relevant records before completing the return. Annual salary and a tax class do not establish the remaining facts.

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| EStG § 1(1), residence | https://www.gesetze-im-internet.de/estg/__1.html | 2026-11-26 |
| EStG § 19(1), employment receipts | https://www.gesetze-im-internet.de/estg/__19.html | 2026-11-26 |
| EStG § 2(2)–(8), base and partners | https://www.gesetze-im-internet.de/estg/__2.html | 2026-11-26 |
| EStG § 26, election/conditions/default | https://www.gesetze-im-internet.de/estg/__26.html | 2026-11-26 |
| EStG § 26b, combined income | https://www.gesetze-im-internet.de/estg/__26b.html | 2026-11-26 |
| EStG § 46(2), assessment cases | https://www.gesetze-im-internet.de/estg/__46.html | 2026-11-26 |
| EStG § 52(1), (36), 2026 application | https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-26 |
| EStG § 32a(1), (5), complete tariff and rounding | https://www.gesetze-im-internet.de/estg/__32a.html | 2026-11-26 |
| EStG § 9a, lump sum/union/receipt limit | https://www.gesetze-im-internet.de/estg/__9a.html | 2026-11-26 |
| EStG § 9(1) nos. 4, 6–7, (2), (4)–(6), expenses and bridges | https://www.gesetze-im-internet.de/estg/__9.html | 2026-11-26 |
| EStG § 4(5) nos. 6b–6c, home-work exclusions | https://www.gesetze-im-internet.de/estg/__4.html | 2026-11-26 |
| EStG § 6(2) sentences 1–3, low-value assets | https://www.gesetze-im-internet.de/estg/__6.html | 2026-11-26 |
| LStH 2026 R 9.12, employee equipment cost/VAT | https://ao.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/II-Einkommen-2-24b/4-Ueberschuss-d-Einnahmen-ueber-die-Werbungsk-8-9a/Paragraf-9/r-9-12.html | 2026-11-26 |
| EStG § 10(1) nos. 2–3, (2)–(4), (4b), insurance deduction | https://www.gesetze-im-internet.de/estg/__10.html | 2026-11-26 |
| SVBezGrV 2026 § 4(1), pension ceilings | https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html | 2026-11-26 |
| RVBeitrSBek 2026, pension contribution rates | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html | 2026-11-26 |
| EStG § 10c, scope of lump sum | https://www.gesetze-im-internet.de/estg/__10c.html | 2026-11-26 |
| EStG § 32, child conditions and allowances | https://www.gesetze-im-internet.de/estg/__32.html | 2026-11-26 |
| EStG § 66, monthly amount and eligible months | https://www.gesetze-im-internet.de/estg/__66.html | 2026-11-26 |
| EStG § 31, entitlement comparison and exception | https://www.gesetze-im-internet.de/estg/__31.html | 2026-11-26 |
| SolzG § 3(2)–(3), assessment base and limits | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-11-26 |
| SolzG § 4, rate, mitigation, rounding | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-11-26 |
| EStG § 25(3)–(4), return/channel | https://www.gesetze-im-internet.de/estg/__25.html | 2026-11-26 |
| ELSTER 2025 form selection; reused exact completed read, not 2026 form proof | https://www.elster.de/elsterweb/helpGlobal?themaGlobal=help_est_ufa_10_2025 | 2026-10-29 |
| AO § 149(1)–(4), duty/deadlines | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-11-26 |
| AO § 108(3), weekend rule; reused exact completed read | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-10-29 |
| EGAO Art. 97 § 36, transitional periods | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-11-26 |
| AO § 169(2) no. 2, ordinary assessment period | https://www.gesetze-im-internet.de/ao_1977/__169.html | 2026-11-26 |
| AO § 170(1)–(2), start of assessment period | https://www.gesetze-im-internet.de/ao_1977/__170.html | 2026-11-26 |
| EStG § 36(2)–(4), credit/payment/refund | https://www.gesetze-im-internet.de/estg/__36.html | 2026-11-26 |
| AO § 152(1)–(5), (10), late filing | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-11-26 |
| AO § 233a(1)–(3), assessment interest | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-11-26 |
| AO § 238(1)–(2), interest rate/full months/base rounding | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-11-26 |
| AO § 240(1)–(3), late-payment charge/grace | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-11-26 |
| SGB IV § 20(2)–(2a), transition range/employee basis/training exception | https://www.gesetze-im-internet.de/sgb_4/__20.html | 2026-11-26 |

Not yet confirmed: 2026 form/field mapping; each named referral outcome; both examples' actual deductible contributions, expense eligibility and complete family/assessment facts. These are explicit holds requiring a partner accountant, not usable estimates. The 2.9% fund rate and wage-withholding amounts remain original fictional inputs, not statutory general rates or verified payroll calculations.
