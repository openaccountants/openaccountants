---
name: il-income-tax-returns
description: "Use this skill when preparing, reviewing, or advising on Israeli annual income tax returns. Trigger on phrases like \"doch shnati\", \"Form 1301\", \"Form 1214\", \"דוח שנתי\", \"mas hachnasa\", \"income tax Israel\", \"nekudot zikui\", \"נקודות זיכוי\", \"tax brackets Israel\", \"mas yesafim\", \"מס יסף\", \"surtax Israel\", \"mikdamot\", \"מקדמות\", \"Mas Shevach\", \"מס שבח\", \"capital gains Israel\", \"Form 6111\", \"Form 856\", \"Form 126\", or any Israel income tax return query. ALWAYS read this skill before advising on Israeli income tax returns."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-income-tax-returns"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-03"
---

# IL Income Tax Returns

## Israel Income Tax Returns Skill v1.1

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1: Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Israel (מדינת ישראל) |
| Scope | Annual income tax returns for individuals and companies |
| Currency | NIS (Israeli New Shekel: ₪) |
| Tax authority | Israel Tax Authority (ITA: Reshut HaMisim: רשות המיסים) |
| Filing portal | Shaam Online: https://www.misim.gov.il |
| Individual return | Form 1301 (דוח שנתי ליחיד) |
| Short return (salaried refund) | Form 135 (דוח שנתי מקוצר) |
| Corporate return | Form 1214 (דוח שנתי לחברה) |
| Corporate tax rate | unverified: 23% flat |
| Surtax threshold | NIS 721,560 a year (NIS 60,130 a month) for 2026 (https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf, p.11); unverified: frozen 2025 to 2027 |
| Credit point value | NIS 242 a month, NIS 2,904 a year, for 2026 (https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf, p.12, s.33A); unverified: frozen 2025 to 2027 |
| Contributor | Open Accountants Community |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown filing obligation | Assume filing is required |
| Unknown bracket year | Use the most recent confirmed brackets |
| Unknown credit points | Apply base resident points only (2.25 male / 2.75 female) |
| Unknown rental income track | Apply marginal rate (most conservative; highest potential tax) |
| Unknown capital gains holding period | Apply 25% rate (no reduced rate exists in Israel regardless) |

## Section 2: Return types and deadlines

**Return types and deadlines table**

| Form | Hebrew | Who files | Deadline | Frequency |
| --- | --- | --- | --- | --- |
| 1301 | דוח שנתי ליחיד | Individuals, sole proprietors, freelancers | 30 June 2026 online; 29 May 2026 paper (tax year 2025) | Annual |
| 135 | דוח שנתי מקוצר | Salaried individuals claiming a refund | unverified: within 6 years of the tax year end (Section 160) | On demand |
| 1214 | דוח שנתי לחברה | Companies (Chevra Ba'am, Chevra Pratit) | unverified: May 31 (5 months after year end); extensions available | Annual |
| 126 | דוח מעסיק על משכורות | Employers reporting employee salaries | unverified: April 30 | Annual |
| 856 | דוח על תשלומים לספקים | Businesses reporting payments to suppliers | unverified: April 30 | Annual |
| 6111 | דוח כספי אחיד | unverified: businesses with turnover > NIS 300,000 (incl. VAT) | Submitted with 1301 or 1214 | Annual |
| Mikdamot | מקדמות מס הכנסה | Self-employed and businesses with advance assessments | unverified: 15th of the month after the period | Bi-monthly |
| Mas Shevach | הצהרת מס שבח | Anyone selling real estate in Israel | unverified: 30 days from sale (40 days if requesting exemption) | Per transaction |
| 1322/1325 | דוח רווח הון מניירות ערך | Anyone with securities capital gains | unverified: 30 days from sale (or annually with Form 1301) | Per transaction or annual |

**CPA-represented filers** (unverified) typically receive automatic extensions through the CPA association's quota arrangement with the ITA (often to September 30 or later).

## Section 3: Who must file Form 1301

- **Who must file Form 1301**: Self-employed individuals (Osek Murshe or Osek Patur); Individuals whose gross salary exceeded NIS 721,560 (surtax threshold); Individuals with income from multiple employers; Individuals with foreign income or assets abroad exceeding reporting thresholds; Anyone who received capital gains during the tax year; Individuals who received rental income exceeding the exempt threshold  _(Section 3: Who must file Form 1301)_

## Section 4: Income tax brackets (2026)

The Economic Efficiency Law 2026, chapter C, amended s.121 on 31.3.2026 with effect from 1 January 2026: 20% now runs from NIS 120,721 to 228,000, 31% from 228,001 to 301,200 and 35% from 301,201 to 560,280 (2026 deduction booklet p.4). The booklet's 2026 table (2026 deduction booklet p.10) gives the full set of bands. unverified: that the other bands are frozen at 2025 values:

**Income tax brackets (2026) table**  _(Section 4: Income tax brackets (2026))_

| Bracket | Annual income range (NIS) | Rate | Source |
| --- | --- | --- | --- |
| 1 | 0 – 84,120 | 10% | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.10) |
| 2 | 84,121 – 120,720 | 14% | same |
| 3 | 120,721 – 228,000 | 20% | same |
| 4 | 228,001 – 301,200 | 31% | same |
| 5 | 301,201 – 560,280 | 35% | same |
| 6 | 560,281 – 721,560 | 47% | same |
| Surtax | Above 721,560 | See Section 5 | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.11) |

These bands apply to income from personal exertion (work and business). Income that is not from personal exertion is taxed at 31% up to NIS 25,100 a month and 35% up to NIS 46,690 a month, then 47% (2026 deduction booklet p.10).

### Monthly equivalent brackets

**Monthly equivalent brackets table**

| Monthly income (NIS) | Rate | Source |
| --- | --- | --- |
| Up to 7,010 | 10% | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.10) |
| 7,011 – 10,060 | 14% | same |
| 10,061 – 19,000 | 20% | same |
| 19,001 – 25,100 | 31% | same |
| 25,101 – 46,690 | 35% | same |
| 46,691 and above | 47% | same |

## Section 5: Surtax (Mas Yesafim: מס יסף)

Two separate charges, on two different bases (2026 deduction booklet p.11, Income Tax Ordinance s.121B):

**Surtax rates table**  _(Section 5: Surtax (Mas Yesafim: מס יסף))_

| Charge | Base | Rate | Source |
| --- | --- | --- | --- |
| Surtax, s.121B(a) | The part of an individual's total taxable income above NIS 721,560 a year (NIS 60,130 a month) | 3% | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.11) |
| Additional surtax on capital income | Taxable income from capital sources above the s.121B amount (added by the Economic Efficiency Law published 26 December 2024) | 2% more | same |
| Residential property sale, s.121B(e) | The real betterment (gain) on selling a right in a residential apartment, only if the sale value exceeds NIS 5,385,285 (2026) and the sale is not exempt under any law | Surtax as above | same |

- **Employment income**: only the 3% charge applies; top rate on employment income 50% (47% + 3%).
- **Capital income**: the 3% charge on the part of total taxable income above the threshold, and the 2% charge on capital-source taxable income above the threshold. Do not apply a blanket 5% to every capital item once total income passes the threshold; work out each base. unverified: which income types count as "capital sources" (dividends, interest, rent, capital gains), and the effective top rates.
- **Residential property**: the sale enters the surtax computation only if both conditions hold: sale value above NIS 5,385,285 (2026) and the sale is not exempt. unverified: the treatment of gains on non-residential real estate.
- **Surtax threshold**: NIS 721,560 for 2026 (2026 deduction booklet p.11). unverified: that it stays frozen through tax year 2027.

## Section 6: Nekudot Zikui (נקודות זיכוי: Tax credit points)

- **Credit point value**: NIS 242 a month for 2026 (2026 deduction booklet p.12, s.33A), so NIS 2,904 a year. unverified: frozen 2025 to 2027. unverified: every row of the table below; the point values per category were not checked against the law in this refresh.  _(Section 6: Nekudot Zikui (נקודות זיכוי: Tax credit points))_

**Nekudot Zikui table**  _(Section 6: Nekudot Zikui (נקודות זיכוי: Tax credit points))_

| Category | Points | Notes |
| --- | --- | --- |
| Israeli resident (male) | 2.25 | Base entitlement |
| Israeli resident (female) | 2.75 | Base (0.5 additional) |
| New immigrant (Oleh Chadash: עולה חדש) | 3.0 year 1, 2.0 year 2, 1.0 year 3 | For 3.5 years from Aliyah date (post-2022: 8.5 points over 54 months) |
| Returning resident (Toshav Chozer: תושב חוזר) | unverified: same as Oleh Chadash | unverified: the qualifying stay abroad; see il-new-immigrant for the official definitions of returning and veteran returning residents |
| Child born during tax year | 1.5 | Per child |
| Children aged 1–5 | 2.5 per child | Per child |
| Children aged 6–17 | 1.0 per child | Per child |
| Child aged 18 | 0.5 | Last year of child credit |
| Single parent | 1.0 | Divorced, widowed, or separated with custody |
| Academic degree (BA) | 1.0 | Per year, up to 3 years matching study duration (graduates 2023+) |
| Academic degree (MA) | 0.5 | For 2 years after completion (graduates 2023+) |
| Vocational certificate | 1.0 | Per year, up to 3 years matching study duration (graduates 2023+) |
| Disability (100% or blind) | 2.0 | Permanent |
| Combat reserve soldiers | unverified: 0.5 to 4.0 | Ordinance s.39B (Amendment 283, published 23.11.2025, credit points for reserve service as a combatant) exists (2026 deduction booklet p.7). unverified: the day bands (30 to 39 days 0.5; 40 to 49 days 0.75; 50 days 1.0; plus 0.25 per five further days) and the years they apply to; the directive that sets them was not opened |

### Worked example

Married woman (2.75 points) with two children aged 3 and 7 (2.5 + 1.0 = 3.5 points):
- Total: 6.25 points × NIS 2,904 = **NIS 18,150** annual tax reduction

### 7.1 Section 45א: 35% tax credit (Zikui)

- **Section 45א credit rules**: The 2026 booklet lists the s.45A(e)(2) ceiling ("ceiling of the amount for a credit for insurance and provident contributions") at **NIS 19,400 a month**, and the s.45A(d) and s.45A(e)(1) ceilings at NIS 189 a month (https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf, p.12). unverified: the 35% credit rate, the 7% employee contribution limit and how it applies to salary up to the NIS 19,400 ceiling, and the self-employed 5.5% limit. The NIS 23,232 a month in an earlier draft has no official support and is withdrawn.  _(7.1 Section 45א: 35% tax credit (Zikui))_

### 7.2 Section 47: Pension deduction (Nikui)

- **Section 47 deduction rules**: 2026 ceilings in the booklet (2026 deduction booklet p.12): qualifying income for a self-employed member s.47(a) NIS 9,700 a month; additional income s.47(a)(5) NIS 24,250 a month. unverified: Reduces taxable income by the contribution amount; Self-employed can deduct up to 11% of annual business income (capped at qualifying ceiling); Employee contributions above the 7% Section 45א threshold can qualify  _(7.2 Section 47: Pension deduction (Nikui))_

### 7.3 Combined rule

- **Combined 45א/47 rule**: unverified: The same shekel cannot double-count. Self-employed filers typically structure deposits so part qualifies for 45א (credit) and part for 47 (deduction) within the 16.5% combined ceiling.  _(7.3 Combined rule)_

### Worked example (self-employed, NIS 300,000 annual income)

**Worked example (self-employed, NIS 300,000 annual income) table**

unverified: this example uses the unconfirmed 5.5% and 11% bases and ignores the 2026 ceilings above.

| Benefit | Calculation |
| --- | --- |
| Pension deposit | NIS 33,000 (11% of income) |
| Section 47 deduction | Reduces taxable income by up to NIS 33,000 |
| Section 45א credit | 35% of up to 5.5% of income = up to NIS 16,500 eligible → NIS 5,775 direct tax reduction |

## Section 8: Rental income tax tracks

Israeli law offers three options for taxing residential rental income:

**Rental income tax tracks table**  _(Section 8: Rental income tax tracks)_

| Track | Rate | Conditions |
| --- | --- | --- |
| Exempt | 0% | unverified: monthly rent below NIS 5,654/month (2025–2027, frozen, no longer CPI-indexed) |
| Flat rate | 10% | unverified: on gross rent, no deductions allowed. Payment by January 31 of following year |
| Marginal | Progressive rates (10%–50%) | unverified: full deduction of expenses (depreciation, mortgage interest, maintenance). Filed with Form 1301 |

### 9.1 Real estate (Mas Shevach: מס שבח)

- **Filing deadline**: unverified: Filing: Within 30 days of sale (40 days if requesting exemption).  _(9.1 Real estate (Mas Shevach: מס שבח))_
- **Mas Shevach calculation**: unverified: Sale price − Original purchase price (adjusted for CPI) − Allowable deductions (purchase tax paid, legal fees, agent commission, renovation costs with receipts) = Real capital gain (Shevach Re'ali: שבח ריאלי) × 25% tax rate = Mas Shevach payable  _(9.1 Real estate (Mas Shevach: מס שבח))_
- **Single apartment exemption (Ptur Dira Yechida: פטור דירה יחידה)**: unverified: Seller's only residential property in Israel; Owned for at least 18 months; Sale price below NIS 5,008,000 (2024–2027, frozen); Seller is an Israeli resident; Partial exemption applies proportionally above the ceiling  _(9.1 Real estate (Mas Shevach: מס שבח))_
- **Linear method (Shita Liniarit: שיטה ליניארית)**: unverified: For properties purchased before January 7, 2014, only the portion of gain attributable to the period after that date is taxed at 25%. The pre-2014 portion may be exempt or taxed at a lower historical rate.  _(9.1 Real estate (Mas Shevach: מס שבח))_

### 9.2 Securities (Forms 1322/1325)

- **Securities capital gains rules**: unverified: 25% tax rate for individuals on traded securities; 30% if seller holds 10%+ of the company; Losses can offset gains within the same category in the same tax year; Capital losses carry forward to offset future capital gains (but not ordinary income)  _(9.2 Securities (Forms 1322/1325))_

### 10.1 How they work

- **Mikdamot mechanics**: The ITA sets a percentage rate based on prior year returns; Applied to bi-monthly turnover (total revenue excluding VAT); New businesses receive a percentage based on industry statistics  _(10.1 How they work)_

### 10.2 Payment schedule

**Payment schedule table**  _(10.2 Payment schedule)_

| Period | Months | Payment due |
| --- | --- | --- |
| 1 | January – February | March 15 |
| 2 | March – April | May 15 |
| 3 | May – June | July 15 |
| 4 | July – August | September 15 |
| 5 | September – October | November 15 |
| 6 | November – December | January 15 |

### 10.3 Year-end reconciliation

- **Year-end reconciliation rules**: Mikdamot paid > actual tax → refund (Hechzer Mas: החזר מס); Mikdamot paid < actual tax → difference owed (plus possible interest); Rate adjustment available mid-year if income changes significantly (Shinui Shiur Mikdamot: שינוי שיעור מקדמות)  _(10.3 Year-end reconciliation)_

## Section 11: Corporate tax

**Corporate tax table**  _(Section 11: Corporate tax)_

| Item | Rate / rule |
| --- | --- |
| Corporate tax rate | unverified: 23% flat on taxable profits |
| Closely held company (Chevra Me'atim: חברה מעטים) | unverified: 2% annual tax on accumulated undistributed profits unless 6%+ distributed as dividends |
| Form 6111 | unverified: required for turnover > NIS 300,000 (including VAT) |
| Deadline | unverified: May 31 (extensions available) |

## Section 12: Form 6111 (standardized financial statements)

- **Form 6111 requirement**: unverified: Required for any business with annual turnover exceeding NIS 300,000 (including VAT).  _(Section 12: Form 6111 (standardized financial statements))_
- **Section A: Profit and Loss Statement**: Revenue by source, COGS, operating expenses, financial income/expenses, depreciation, net profit, tax adjustments  _(Section 12: Form 6111 (standardized financial statements))_
- **Section B: Balance Sheet**: Current assets, fixed assets, current liabilities, long-term liabilities, equity  _(Section 12: Form 6111 (standardized financial statements))_
- **Submission requirement**: All amounts in NIS. Must match audited financial statements exactly. Submitted electronically via Shaam.  _(Section 12: Form 6111 (standardized financial statements))_

## Section 13: Filing via Shaam online portal

1. Register at misim.gov.il with Teudat Zehut (תעודת זהות) or company number
2. Set up digital credentials (username + password + 2FA)
3. Select the relevant form and tax year
4. Enter data or upload from accounting software
5. System validates data and flags errors
6. Review calculated tax liability
7. Submit electronically (receive confirmation number)
8. Pay any tax owed via the payment portal

- **CPA authorization (Yipui Koach: ייפוי כוח)**: Granted per-client, per-year via the Shaam portal. Allows CPA to submit returns and communicate with the ITA on behalf of the client.  _(Section 13: Filing via Shaam online portal)_

### Example 1: Freelancer annual return (Form 1301)

**Scenario:** Male freelance developer (Osek Murshe), annual business revenue NIS 450,000, business expenses NIS 80,000, two children aged 4 and 8.

**Working:**
- Net business income: NIS 450,000 − NIS 80,000 = NIS 370,000
- Credit points: 2.25 (resident) + 2.5 (child age 4) + 1.0 (child age 8) = 5.75 points
- Tax credit: 5.75 × NIS 2,904 = NIS 16,698
- Income tax (applying 2026 brackets to NIS 370,000):
  - 10% on 84,120 = NIS 8,412
  - 14% on 36,600 = NIS 5,124
  - 20% on 107,280 = NIS 21,456
  - 31% on 73,200 = NIS 22,692
  - 35% on 68,800 = NIS 24,080
  - **Gross tax: NIS 81,764**
- Less credit points: NIS 81,764 − NIS 16,698 = **NIS 65,066 income tax**
- Less mikdamot paid during year → net tax due or refund

### Example 2: Real estate capital gains (Mas Shevach)

**Scenario:** Investment apartment sold for NIS 2,800,000, purchased in 2018 for NIS 1,600,000.

**Working:**
- Gross gain: NIS 2,800,000 − NIS 1,600,000 = NIS 1,200,000
- Adjust for CPI change from 2018 to sale date
- Deduct allowable expenses (purchase tax, legal fees, agent commission, documented renovation)
- Real gain × 25% = Mas Shevach payable
- unverified: file within 30 days of sale
- Surtax: an investment apartment is a residential apartment, so the gain enters the surtax only if the sale value exceeds NIS 5,385,285 (2026) and the sale is not exempt (2026 deduction booklet p.11, s.121B(e)). The sale value here is NIS 2,800,000, below the ceiling: no surtax on this gain. Had it been above the ceiling, the 3% charge would apply to the part of total taxable income above NIS 721,560 and the 2% capital-income charge to the part of capital-source income above it; they are two bases, not a single 5% on the gain.

## Section 15: Common errors

**Common errors table**  _(Section 15: Common errors)_

| Error | Why it matters |
| --- | --- |
| Using US form numbers (1040) | Israel uses Form 1301 for individuals |
| Wrong deadline (April 30 for Form 1301) | April 30 is the legacy paper baseline; current online deadline is June 30 |
| Single capital gains rate for everything | unverified: securities 25%; significant shareholders 30%; real estate varies |
| Default credit point value without checking eligibility | Points vary by personal status; must calculate per individual |
| Adding every residential sale to surtax income | A residential-apartment gain counts only if the sale value exceeds NIS 5,385,285 (2026) and the sale is not exempt (2026 deduction booklet p.11) |
| Forgetting Section 45א/47 pension credits | One of the most common filing errors for self-employed |

## Section 16: Reference material

**Reference material table**  _(Section 16: Reference material)_

| Resource | Reference |
| --- | --- |
| Tax Authority: Form 1301 service | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals |
| Shaam filing portal | https://www.misim.gov.il |
| Kol Zchut: income tax brackets | https://www.kolzchut.org.il/he/מדרגות_מס_הכנסה |
| Kol Zchut: tax credit points | https://www.kolzchut.org.il/he/נקודות_זיכוי |
| Kol Zchut: Mas Shevach | https://www.kolzchut.org.il/he/חישוב_מס_שבח |
| Real estate taxation office | https://www.gov.il/he/departments/topics/land_taxation |
| Income Tax Ordinance | https://www.nevo.co.il/law/70264 |

## Recomputed checks (2026)

```oa-check
name: Freelancer, net NIS 370,000, 5.75 points (2026)
inputs:
  p: 370000
  pts: 5.75
steps:
  - tax: 84120*0.10+36600*0.14+107280*0.20+73200*0.31+(p-301200)*0.35
  - net: tax-pts*2904
expected:
  net: 65066
```

```oa-check
name: Surtax on employment income NIS 800,000
inputs:
  p: 800000
steps:
  - s: (p-721560)*0.03
expected:
  s: 2353.2
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Israel Tax Authority, salary-deduction booklet from January 2026 (updated April 2026), read p.4 (Economic Efficiency Law 2026 bracket change from 1 January 2026), p.7 (s.39B, Amendment 283), p.10 (2026 annual and monthly bands after the bracket-widening law, s.121), p.11 (s.121B surtax 3% above NIS 721,560, extra 2% on capital-source income, residential sale ceiling NIS 5,385,285), p.12 (credit point NIS 242, s.45A(d), (e)(1), (e)(2) ceilings NIS 189, 189, 19,400; s.47(a) ceilings NIS 9,700 and 24,250) | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf | 2026-11-03 |
| Israel Tax Authority, Form 1301 service page, tax year 2025 | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals | 2026-11-01 |

Not yet confirmed: the tax year 2026 return deadlines (the Authority has published only tax year 2025 dates); Forms 126, 856, 1214 deadlines and representative extensions; Form 6111 NIS 300,000 trigger; Mas Shevach filing window, calculation, single-apartment exemption and the linear method; Form 135 six-year window; securities rates and loss rules; closely held company 2% tax; corporate rate 23%; the 2025 to 2027 freezes; the credit-point table by category and the reserve-duty day bands; the s.45A 35%, 7% and 5.5% rules and the s.47 11% rule; the rental tracks; which income counts as capital-source for the 2% surtax; non-residential real estate in the surtax. No official consolidated text of the Income Tax Ordinance was opened; sections are cited as the Authority's booklet states them.

## Disclaimer

> **חשוב:** כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional: such as a רואה חשבון (Ro'eh Cheshbon: CPA) or יועץ מס (Yo'etz Mas: tax advisor) licensed in Israel: before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-03. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-income-tax-returns` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-income-tax-returns. If neither is available, confirm every figure against the official source pages cited above before relying on it.
