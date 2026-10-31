---
name: li-payroll-social
description: >
  Prepare 2026 Liechtenstein payroll and social contribution workpapers. Covers
  AHV, IV, FAK and administration contributions (employee 4.9%, employer
  7.385%), unemployment insurance ALV (0.5% each, capped at CHF 126,000 a year,
  CHF 350 a day for part years), the contribution wage and benefits in kind,
  self-employed contributions (12.285%, minimum CHF 368.55) and the 2026 table
  for non-employed persons, wage-tax withholding (the 4% to 19% maximum
  schedule, the CHF 25,200 student exemption), employer health-care contributions
  (CHF 180.50 a month), occupational pension entry (CHF 14,700, 8% minimum
  retirement contribution), accident premiums, remittance calendars, reminder
  fees and appeals. Trigger on: Liechtenstein payroll, AHV Liechtenstein, Lohnsteuer
  Liechtenstein, Quellensteuer, ALV, FAK, BPVG. Out of scope: disputed employment
  status, international insurance coordination and plan-specific premiums.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
version: 0.3
---

# Liechtenstein payroll and social contributions v0.3

## Who this applies to

Use this skill for 2026 for employees, self-employed and non-employed persons insured in Liechtenstein, and for employers running Liechtenstein payroll. It covers both payroll withholding (PR) and social contributions (SC). Confirm coverage separately for each employment and country. Liechtenstein has its own contribution rates; do not use Swiss rates. Residents are also subject to wage withholding; the annual assessment follows.

## Rates, bands and thresholds

The [AHV-IV-FAK bulletin effective 1 January 2026][contributions], sections 5–6, gives these percentages of the established contribution wage:

| Contribution | Employee | Employer | Tax year | Official source |
|---|---:|---:|---|---|
| AHV | 4.025% | 4.225% | 2026 | [AHV bulletin section 5][contributions] |
| IV | 0.675% | 0.675% | 2026 | [AHV bulletin section 5][contributions] |
| FAK | 0.200% | 1.900% | 2026 | [AHV bulletin section 5][contributions] |
| Administration, VK | none | 0.585% | 2026 | [AHV bulletin section 5][contributions] |
| Total above, excluding ALV | 4.900% | 7.385% | 2026 | [AHV bulletin section 5][contributions] |
| ALV | 0.500% | 0.500% | 2026 | [AHV bulletin section 6][contributions] |

ALV is capped at CHF 126,000 yearly **per employment**. For part-year employment, the bulletin uses CHF 350 per contribution day with its 30-day-month convention; do not use actual calendar days or an unadjusted annual cap. AHV/IV/FAK/VK and ALV do not necessarily share the same wage ceiling. The employer deducts employee contributions and remits both sides. [Bulletin, sections 5–6][contributions]

For working persons, contributions start on 1 January of the year they turn 18. The bulletin separately addresses apprentices/family members, remuneration in kind, pension age, self-employed persons and non-employed persons. A full-year adult employee example does not settle those cases. [Sections 1–4 and 7–14][contributions]

## The base

### Contribution status, wage items and benefits

For apprentices and family members working in the business, only cash remuneration is contributory through 31 December of the year they turn 20; from the following year, include remuneration in kind. For a spouse working in the business, the cash-only rule applies regardless of age. Non-employed persons and unpaid working family members enter contribution liability from 1 January of the year they turn 21. For persons born in 1958 or later, ordinary contribution liability ends at the end of the month they reach 65; for non-employed early pension recipients it ends on the last day of the month before pension payment starts. Determine continued-work treatment separately. [AHVG article 38(3)][ahvg]; [2026 bulletin, sections 2–4][contributions]

Build the contribution wage item by item. Section 8 includes overtime, bonuses, commissions, material tips, regular benefits in kind, directors' fees, employer wage continuation during sickness/accident, holiday pay and employer payment of an employee's contributions or tax. Section 9 separately excludes insurance sickness/accident daily allowances, maternity/paternity/parental replacement payments, family allowances, qualifying statutory/plan employer insurance contributions, natural gifts not exceeding CHF 1,000 a year and employer mobility contributions not exceeding CHF 600 a year. Those are contribution exclusions; do not copy them into the wage-tax base. Resolve the treatment when an exclusion's conditions or limit are not met before calculating. [2026 bulletin, sections 8–9][contributions]

For the contribution wage, the bulletin's section 10 values ordinary meals and accommodation as follows:

| Benefit | CHF per month | CHF per day | Official source |
|---|---:|---:|---|
| Breakfast | 120 | 4 | [2026 bulletin section 10][contributions] |
| Lunch | 300 | 10 | [2026 bulletin section 10][contributions] |
| Dinner | 240 | 8 | [2026 bulletin section 10][contributions] |
| Full meals | 660 | 22 | [2026 bulletin section 10][contributions] |
| Accommodation | 330 | 11 | [2026 bulletin section 10][contributions] |
| Full meals and accommodation | 990 | 33 | [2026 bulletin section 10][contributions] |

Other natural remuneration, including a family apartment or meals for relatives, is valued individually by the institution. If a working family member's cash and natural income cannot be established, section 11 supplies a monthly global wage: CHF 2,070 for single working family members and working spouses; CHF 3,060 for married working family members, with CHF 2,070 each if both spouses work fully in the business. Establish the actual category and the cash-only age/spouse rule before applying a figure. [Sections 10–11][contributions]

The wage-tax bulletin uses the same ordinary meal/accommodation amounts, but increases them by 20% for its listed senior staff, administrators, doctors, teachers and similar personnel. Hotel/restaurant directors or managers and employee couples have separate authority valuation routes. That wage-tax increase is not stated in the social bulletin's ordinary table: maintain separate benefit valuations and bases. [Wage bulletin I.2(a)][wage]

### Self-employed and non-employed contributions

#### Self-employed base and assessment

Establish social-insurance status from the actual independence and business-risk facts; a tax registration or invoice label alone does not establish self-employment. The institution decides the category. AHVG article 42 defines self-employed income and deducts income-earning expenses, justified depreciation/provisions and booked business losses. Its specified staff-welfare/public-benefit deductions exclude the person's own article 41 contributions and IV supplements; business-capital interest uses the government's applicable rate. Do not treat book profit after personal contribution deductions as the established contribution base or import a Swiss capital-interest rate. For 2026 the legal chain is AHVV article 16(2), which refers valuation to tax legislation, then SteG article 16(2)(b)(2), which links the eligible own-capital return to the article 5 Sollertrag of **4%**. Apply the linked valuation and modified-capital conditions, including the incorporated article 12(3)/54(2)–(6) rules. It is not 4% of every book-equity balance or a Swiss annual investment-interest figure. The actual capital reconciliation and special-case application still require evidence. [AHVV article 16(2)][ahvv]; [SteG articles 5 and 16(2)(b)(2)][law]; [AHVG articles 41–42][ahvg]

For an established ordinary annual self-employed contribution income of at least CHF 3,000, round income **down to the next CHF 100** before applying AHV 8.25%, IV 1.35%, FAK 2.10% and VK 0.585%, total 12.285%. There is no employee/employer split and no ALV for self-employment. Below CHF 3,000, the ordinary full-year minimum is CHF 368.55 including administration. For an activity established as **secondary self-employment**, AHVV article 17 requires contributions on calendar-year income **below CHF 1,000 only if the insured person requests them**. At CHF 1,000 that exception no longer applies. Establish that it is genuinely secondary activity; do not extend the exception to an ordinary main business or treat a receipt exactly at the limit as below it. Mixed employment/non-employment classification still needs its own assessment. [AHVV article 17][ahvv] [AHVG article 41][ahvg]; [2026 bulletin sections 5, 13 and 16][contributions]; [institution self-employed method][self-employed]

AHVV article 20 uses the result of the business year ending in the contribution year and invested equity at that business-year end. Do not split a non-calendar business year between contribution years. If there is no accounts closure in a contribution year, article 20(4) instead allocates income according to the business period's duration. Self-employed income is not annualised. Article 21 uses the final tax-assessment income without tax social deductions; article 16(4) limits the stated booked business-loss deduction to the current and immediately preceding contribution years. Reconcile these statutory adjustments before rounding or applying the percentage. [AHVV articles 16 and 20–21][ahvv]

Provisional contributions use expected income in the current contribution year. Report material changes; if year-end accounts show advances were too low, notify the institution immediately. Once final tax data are available, reconcile the definitive contribution decision with advances paid and record the balance. This is a contribution assessment, not a replacement for the income-tax computation. [2026 bulletin section 13][contributions]

#### Non-employed category and table lookup

The 2026 total annual minimum is CHF 368.55 and maximum CHF 12,285, including administration; non-employed persons do not pay ALV. Minimum categories include non-employed spouses of working persons or pension recipients, qualifying non-employed recipients of a Liechtenstein IV or foreign state invalidity pension, persons maintained or permanently supported by public/third-party funds, and persons in education who paid no contributions or less than the minimum. Check age, contribution period and any employment contributions before selecting the category. Expenditure-taxed persons instead owe the statutory maximum. [AHVG article 43][ahvg]; [2026 bulletin sections 3–4 and 14][contributions]; [institution non-employed method][non-employed]

For a non-employed person outside a minimum category, establish domestic/foreign wealth and annual pension/replacement income from the assessment, then compute **wealth + 30 × relevant annual pension/replacement income**. The institution lists occupational pensions, maintenance and sickness/accident daily allowances as income examples. For married/registered partners outside a minimum category, it uses half the couple's combined wealth and pension income regardless of their property regime. For non-employed recipients of a Liechtenstein AHV or **foreign state** survivors' pension, AHVV article 25(3) supplies the wealth-only basis. Do not extend that exception to every private or occupational survivors' pension. The statute's state-pension qualification controls the institution page's broader summary. [Institution non-employed method, “Bemessung und Festsetzung” and “Hinterlassenenrente”][non-employed]

AHVV article 26 ordinarily uses wealth at the **start of the contribution year** and pension/replacement income actually received in that year, without annualising that pension income. For liability lasting less than a year, article 26(4) instead requires an annualised pension-income basis and the wealth assessed for that calendar year, with contributions proportionate to the liability duration. Establish the exact coverage period and the institution's duration/rounding method; do not multiply a short-period pension receipt by 30 and treat it as a full-year basis. Mixed-status transitions and fractional assessment-basis rounding remain unresolved here. [AHVV articles 25–26][ahvv]

Select the highest applicable lower-bound row of the official 2026 table below; **use the printed total annual contribution**. The table warns that the actual invoice can have rounding differences. It is not a flat percentage of wealth, and the AHV-only column is not the total bill. Its income-credit column is not the person's actual pension income. [2026 institution table][non-employed-table]

| Established assessment basis CHF | Total annual contribution CHF | Source |
|---|---:|---|
| Up to 199,999 | 368.55 | [2026 official table][non-employed-table] |
| From 200,000 | 464.55 | [2026 official table][non-employed-table] |
| From 400,000 | 607.55 | [2026 official table][non-employed-table] |
| From 600,000 | 768.40 | [2026 official table][non-employed-table] |
| From 800,000 | 982.80 | [2026 official table][non-employed-table] |
| From 1,000,000 | 1,411.65 | [2026 official table][non-employed-table] |
| From 1,100,000 | 1,840.50 | [2026 official table][non-employed-table] |
| From 1,200,000 | 2,269.40 | [2026 official table][non-employed-table] |
| From 1,300,000 | 2,698.25 | [2026 official table][non-employed-table] |
| From 1,400,000 | 3,127.10 | [2026 official table][non-employed-table] |
| From 1,500,000 | 3,555.95 | [2026 official table][non-employed-table] |
| From 1,600,000 | 3,984.80 | [2026 official table][non-employed-table] |
| From 1,700,000 | 4,413.60 | [2026 official table][non-employed-table] |
| From 1,800,000 | 4,842.55 | [2026 official table][non-employed-table] |
| From 1,900,000 | 5,271.35 | [2026 official table][non-employed-table] |
| From 2,000,000 | 5,700.25 | [2026 official table][non-employed-table] |
| From 2,100,000 | 6,129.10 | [2026 official table][non-employed-table] |
| From 2,200,000 | 6,557.95 | [2026 official table][non-employed-table] |
| From 2,300,000 | 6,986.85 | [2026 official table][non-employed-table] |
| From 2,400,000 | 7,415.70 | [2026 official table][non-employed-table] |
| From 2,500,000 | 7,844.55 | [2026 official table][non-employed-table] |
| From 2,600,000 | 8,273.35 | [2026 official table][non-employed-table] |
| From 2,700,000 | 8,702.25 | [2026 official table][non-employed-table] |
| From 2,800,000 | 9,131.05 | [2026 official table][non-employed-table] |
| From 2,900,000 | 9,560.00 | [2026 official table][non-employed-table] |
| From 3,000,000 | 9,988.80 | [2026 official table][non-employed-table] |
| From 3,100,000 | 10,417.70 | [2026 official table][non-employed-table] |
| From 3,200,000 | 10,846.55 | [2026 official table][non-employed-table] |
| From 3,300,000 | 11,275.35 | [2026 official table][non-employed-table] |
| From 3,400,000 | 11,704.30 | [2026 official table][non-employed-table] |
| From 3,500,000 | 12,133.10 | [2026 official table][non-employed-table] |
| From 3,600,000 | 12,285.00 | [2026 official table][non-employed-table] |

ANOBAG employees have their own employee-without-contributing-employer category: the institution applies total AHV/IV/FAK/VK rates under the self-employed assessment process **plus ALV**. Do not infer the self-employed ALV exemption from the assessment route. AHVG article 39(2) also permits the agreed employer/employee collection route. Establish which route applies before charging the person or employer. [AHVG article 39][ahvg]; [2026 bulletin section 12][contributions]

### Wage withholding is a separate calculation

Source withholding applies to resident employment/replacement income too. Do not classify a resident wage as outside payroll withholding because an annual assessment follows. SteG articles 24–25 and the [February 2026 wage-tax bulletin][wage] govern the category and base. Its base is wage-certificate field 8 less field 6, not take-home pay; remuneration in kind and replacement income require their own treatment.

The bulletin's **maximum ordinary withholding schedule** uses expected annual gross remuneration, annualised for a part-year liability. These are whole-base withholding percentages, not the marginal bands of final individual tax. Obtain family status and any authority instruction before choosing a rate. The table's printed bands meet at their endpoints; confirm the assigned rate for an exact disputed boundary rather than rounding the income into a convenient band. [Section II.1][wage]

| Expected annual gross CHF | Single maximum | Expected annual gross CHF | Married maximum | Official source (2026) |
|---|---:|---|---:|---|
| Up to 40,000 | 4% | Up to 80,000 | 4% | [Wage bulletin II.1][wage] |
| 40,000–60,000 | 5% | 80,000–140,000 | 5% | [Wage bulletin II.1][wage] |
| 60,000–80,000 | 7% | 140,000–200,000 | 7% | [Wage bulletin II.1][wage] |
| 80,000–120,000 | 9% | 200,000–250,000 | 9% | [Wage bulletin II.1][wage] |
| 120,000–160,000 | 11% | 250,000–350,000 | 11% | [Wage bulletin II.1][wage] |
| 160,000–200,000 | 13% | 350,000–450,000 | 13% | [Wage bulletin II.1][wage] |
| 200,000–300,000 | 15% | 450,000–600,000 | 15% | [Wage bulletin II.1][wage] |
| 300,000–500,000 | 17% | 600,000–1,000,000 | 17% | [Wage bulletin II.1][wage] |
| Above 500,000 | 19% | Above 1,000,000 | 19% | [Wage bulletin II.1][wage] |

The current bulletin exempts qualifying resident pupils, apprentices and students from wage withholding up to CHF 25,200 from tax year 2025, while still requiring wage-list reporting. The still-linked 2019 orientation says CHF 24,000; use the February 2026 bulletin for this figure. Do not treat that exception as a general wage-tax or social-insurance exemption. [Section II.3 and footnote][wage]

### Other employer costs

The [health authority's 2026 contribution page][health] sets the monthly employer health-care amount at CHF 180.50 for adults and CHF 90.25 for the stated youth category, reduced for part-time work; age-group changes apply from the following 1 January. Its separately displayed 2027 amounts are not 2026 rates. Daily sickness insurance, accident cover and occupational pensions require applicable eligibility and provider/plan terms. Do not advertise one all-in employer percentage.

### Occupational pension and accident premium allocation

For an employee within compulsory BPVG coverage, first establish AHV liability, article 3 exclusions, the article 4 annual wage gate and the relevant risk/savings start dates. The annual wage entry threshold is the annual amount of the minimum AHV old-age pension (BPVG article 4(1)): CHF 1,225 a month from 1 January 2025 (AHVG article 68(3bis), note 209), so **CHF 14,700** a year. BPVV article 3(3) annualises pay for a part-year employment; this is separate from actual-period contributions. Under BPVG article 4(2), risk cover begins on 1 January after the 17th birthday and retirement saving on 1 January after the 19th birthday on the stated qualifying employment terms. A term longer than three months is treated as indefinite; a shorter term extended beyond three months is treated as indefinite from extension. [BPVG article 4][bpvg]; [BPVV article 3][bpvv]; [AHVG article 68][ahvg] Do not assume the AHV contribution base alone establishes compulsory pension membership. Under article 7, the pension institution fixes contributions; the ordinary minimum retirement contribution is 8% of insured wage under article 6. The employer supplies at least half the contributions for each employee. This is a minimum retirement contribution, not an all-in pension/risk/administration percentage. Article 7(5) requires employee deductions and the corresponding employer contribution to reach the pension institution no later than the end of the relevant calendar quarter. Special voluntary/continued-insurance and parental-leave cases require their separate rules. [BPVG articles 3–4 and 6–7][bpvg]

For compulsory accident insurance, UVersG article 79 allocates occupational-accident and occupational-disease premiums to the employer. Non-occupational premiums fall on the insured person, subject to a more favourable agreement. The employer owes the full premium to the insurer and deducts the employee share from the current or immediately following wage period; a less favourable agreement is invalid. Confirm actual insured coverage and the insurer's premium tariff; these payer rules do not establish an invented flat premium rate. [UVersG article 79][uversg]

### Further checks

#### Part-year ALV cap

This reproduces the institution's section 6 example: 15 April–28 December gives 254 contribution days under its stated convention and CHF 96,200 pay. The cap is CHF 88,900 (254 x CHF 350), giving CHF 889 at the combined 1% (CHF 444.50 each side). This is not 254 ordinary actual-calendar days.


#### Assumed established wage-withholding instruction

Assume a single resident employee with CHF 90,000 expected full-year gross, no special category/treaty or revised authority instruction, and a confirmed 9% withholding rate. CHF 7,500 current gross gives CHF 675 withholding, before other deductions. This does not calculate final individual tax.


## Deadlines and filing

1. Retain contracts, residence/treaty evidence, birth date, employment dates, work countries, status and insurance decisions, family status, expected annual remuneration and any authority rate direction.
2. Build separate social-contribution and wage-tax bases from pay, benefits, reimbursements and replacement income. The bulletin lists the contribution-wage items; the wage-tax bulletin supplies its own base. Resolve disputed classification before calculation.
3. Calculate employee AHV/IV/FAK and capped ALV; record employer AHV/IV/FAK/VK and ALV separately. Reconcile to the provider's account and actual contribution period.
4. Calculate wage withholding under the applicable instruction, issue the wage certificate, and retain the employee/employer liability reconciliation. Benefits-only payments still require collection of the tax from the recipient under SteG article 27; do not invent a universal cash-only cap.
5. Remit ordinary wage withholding quarterly. The authority's demand letter fixes the quarterly due dates. The February 2026 bulletin states wage lists and the annual balancing payment by 31 January of the next year, with separate lists by resident municipality and foreign-residence categories. For 2026 payroll, verify the actual 2027 calendar/holiday and authority notice before assigning a final date. [SteG, articles 27–28][law]; [section III][wage]
6. Keep the AHV contribution calendar separate. Under AHVV article 30, employer annual wage sums **over CHF 200,000** pay monthly; **CHF 12,000–200,000** pay quarterly; **below CHF 12,000** pay annually. Contributions are payable within 20 days after that payment period ends. Self-employed persons, ANOBAG and non-employed persons ordinarily pay quarterly; the institution can allow longer periods up to annual in justified cases. Monthly election and an imposed monthly schedule for late payers are separate routes. Preserve the actual institution's schedule. [AHVV article 30][ahvv]
7. Employer wage reconciliations cover the calendar year and are due 31 January of the following year. Employer final contribution balances and self-employed definitive shortfalls are payable within 20 days of invoicing; excess is refunded or credited. Report employer expected annual wage-sum changes of at least 10%; changes **below CHF 20,000** need not be reported under article 34(2). The threshold tests concern the wage sum, not headcount or individual salary. [AHVV articles 23 and 34–35][ahvv]

## Penalties and interest

SteG article 27 makes the payer liable for underwithholding and requires corrected certification; article 28 addresses interest on a late annual difference. Do not calculate a fine from a statutory maximum or describe withholding as the employee's final assessed tax. [SteG, articles 27–28][law]

Under AHVV article 31, a missed contribution payment or required return information triggers a written reminder with a 10–20-day grace period. If that period expires unused, a further reminder must include a CHF 20–200 reminder fee and notice of consequences. It is not an automatic fee on the first late day. Article 37 permits assessment of unpaid/unreported contributions and charges the late party the costs of the assessment/local examination. [AHVV articles 31 and 37][ahvv]

A contribution decision must contain appeal instructions. AHVG article 84 permits **Vorstellung within four weeks** to the institution, with a fresh decision and a cost/fee-free initial procedure. Under article 86, appeal from that decision goes to the Obergericht within a separate **four-week, non-extendable period**, filed at that court. Keep the decision, proof of service and applicable procedural start/date rules; the later court route is not the initial administrative objection. [AHVG articles 83quinquies and 84–86][ahvg]

## Cross-border points

For foreign residents, inspect the January 2026 treaty annex and the actual treaty, residence, workdays and public/private employment facts. Austrian or Swiss commuter treatment is not determined by a postal address alone. For 2026, Austrian cross-border commuters (Grenzgänger) under article 15(4) of the Liechtenstein-Austria treaty bear a 4% source tax on employment income ([Finance Act 2026, article 3][finance]); the commuter conditions must be met. SteG article 26 provides authority confirmation for exemption/reduction and a separate excess-withholding refund route. Specified board/pension payments under article 25(3) have a separate 12% rule; do not apply the ordinary wage table automatically. Treaty analysis and all exceptional payment categories remain open. [SteG, articles 24–26][law]

For a dispute over the existence or extent of source-tax liability, article 25(4) permits the taxpayer or payer to request an authority decision by the end of March of the calendar year following the payment's maturity; the payer must continue withholding until the final decision. For treaty overwithholding, article 26(3) separately sets a refund-application period of two years from maturity of the withheld tax amounts. Preserve the actual maturity dates, authority certificate, proof of excess and correct route; these are different procedures. [SteG articles 25(4) and 26(3), read 30 October 2026][law]

## Two worked examples that recompute

These are assumed ordinary covered adult employees; rates and bases must apply before the arithmetic is used. No occupational-pension, accident/sickness premium, health contribution or wage tax is included in the first two controls.

### Full-year employee contributions

```oa-check
name: Liechtenstein 2026 assumed employee contribution split
inputs:
  established_annual_wage: 60000
  employee_ahv_iv_fak: 0.049
  annual_alv_cap: 126000
  employee_alv: 0.005
steps:
  ahv_iv_fak_deduction: established_annual_wage * employee_ahv_iv_fak
  alv_base: min(established_annual_wage, annual_alv_cap)
  alv_deduction: alv_base * employee_alv
  specified_employee_deductions: ahv_iv_fak_deduction + alv_deduction
expected:
  ahv_iv_fak_deduction: 2940
  alv_base: 60000
  alv_deduction: 300
  specified_employee_deductions: 3240
```

### Full-year employer contributions with ALV cap

Assume CHF 150,000 established annual wage, all subject to AHV/IV/FAK/VK, and full-year ALV coverage in this employment.

```oa-check
name: Liechtenstein 2026 assumed employer contribution and ALV ceiling
inputs:
  established_annual_wage: 150000
  employer_ahv_iv_fak_vk: 0.07385
  annual_alv_cap: 126000
  employer_alv: 0.005
steps:
  ahv_iv_fak_vk_charge: established_annual_wage * employer_ahv_iv_fak_vk
  alv_base: min(established_annual_wage, annual_alv_cap)
  alv_charge: alv_base * employer_alv
  specified_employer_charges: ahv_iv_fak_vk_charge + alv_charge
expected:
  ahv_iv_fak_vk_charge: 11077.50
  alv_base: 126000
  alv_charge: 630
  specified_employer_charges: 11707.50
```

## Ask the client first

Establish coverage, contribution dates/wages, residence and treaty status, public/private employment, family status and the authority instruction. Ask for the pension/insurance plan, benefit details, current remittance notices and prior corrections. Refer disputed status, multi-country insurance/telework, every treaty entitlement, family/retirement exceptions, specialist benefits and plan pricing.

## Sources

| Source | URL | Read on |
|---|---|---|
| AHV-IV-FAK, bulletin 1.01 contributions to AHV/IV/FAK/ALV, as of 1 January 2026 | https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf | 2026-10-30 |
| AHV-IV-FAK, self-employed persons | https://www.ahv.li/beitraege/selbstaendigerwerbende/ | 2026-10-30 |
| AHV-IV-FAK, non-employed persons | https://www.ahv.li/beitraege/nichterwerbstaetige/ | 2026-10-30 |
| AHV-IV-FAK, contribution table for non-employed persons 2026 | https://www.ahv.li/fileadmin/user_upload/Dokumente/Beitraege/Nichterwerbst%C3%A4tige/Beitragstabelle_Nichterwerbst%C3%A4tige_2026.pdf | 2026-10-30 |
| AHVG (Act on old-age and survivors' insurance), consolidated 1 January 2026, articles 38-43, 68, 83quinquies-86 | https://www.gesetze.li/konso/pdf/1952029000 | 2026-10-30 |
| AHVV (Ordinance), consolidated 1 January 2026, articles 16-17, 20-26, 30-31, 34-39 | https://www.gesetze.li/konso/pdf/1982035000 | 2026-10-30 |
| BPVG (Occupational Pensions Act), consolidated 1 January 2026, articles 3-4, 6-7 | https://www.gesetze.li/konso/pdf/1988012000 | 2026-10-30 |
| BPVV (Occupational Pensions Ordinance), consolidated 16 April 2026, article 3 | https://www.gesetze.li/konso/pdf/2005288000 | 2026-10-30 |
| UVersG (Accident Insurance Act), consolidated 1 January 2026, article 79 | https://www.gesetze.li/konso/pdf/1990046000 | 2026-10-30 |
| Steuergesetz (SteG), consolidated 1 July 2026, articles 5, 16, 24-29 | https://www.gesetze.li/konso/pdf/2010340000 | 2026-10-30 |
| Steuerverwaltung, bulletin on source tax / wage tax, February 2026, with treaty annex January 2026 | https://www.llv.li/servicekonto/steuerverwaltung/quellensteuer-lohnsteuer-unselbstaendige-taetigkeit-und-ersatzeinkuenfte-merkblatt.pdf | 2026-10-30 |
| Finanzgesetz für das Jahr 2026, article 3 (Austrian commuters) | https://www.gesetze.li/konso/pdf/2025556000 | 2026-10-31 |
| Steuerverwaltung, wage and source tax | https://www.llv.li/de/landesverwaltung/steuerverwaltung/lohn-quellensteuer-personalvorsorge/lohn-quellensteuer | 2026-10-24 |
| Landesverwaltung, health insurance premiums and employer contributions | https://www.llv.li/de/privatpersonen/gesundheit-vorsorge-und-pflege/krankenversicherung/praemien-beitraege | 2026-10-30 |

Not yet confirmed: interest on late social contributions; the eligible-capital reconciliation for self-employed contributions; mixed-status and part-year rounding for non-employed persons; continued work after pension age; accident, sickness and pension plan premium rates; treaty entitlements of individual cross-border workers; the 2027 calendar dates for 2026 wage lists.

[bpvv]: https://www.gesetze.li/konso/pdf/2005288000
[ahvv]: https://www.gesetze.li/konso/pdf/1982035000
[bpvg]: https://www.gesetze.li/konso/pdf/1988012000
[uversg]: https://www.gesetze.li/konso/pdf/1990046000
[ahvg]: https://www.gesetze.li/konso/pdf/1952029000
[self-employed]: https://www.ahv.li/beitraege/selbstaendigerwerbende/
[non-employed]: https://www.ahv.li/beitraege/nichterwerbstaetige/
[non-employed-table]: https://www.ahv.li/fileadmin/user_upload/Dokumente/Beitraege/Nichterwerbst%C3%A4tige/Beitragstabelle_Nichterwerbst%C3%A4tige_2026.pdf
[contributions]: https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf
[law]: https://www.gesetze.li/konso/pdf/2010340000
[wage]: https://www.llv.li/servicekonto/steuerverwaltung/quellensteuer-lohnsteuer-unselbstaendige-taetigkeit-und-ersatzeinkuenfte-merkblatt.pdf
[wage-page]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/lohn-quellensteuer-personalvorsorge/lohn-quellensteuer
[health]: https://www.llv.li/de/privatpersonen/gesundheit-vorsorge-und-pflege/krankenversicherung/praemien-beitraege

[finance]: https://www.gesetze.li/konso/pdf/2025556000

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
