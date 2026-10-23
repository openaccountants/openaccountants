---
name: se-employee-income-tax
description: "Use for the Swedish personal income tax return (Inkomstdeklaration 1) of an employee or a pensioner for income year 2026, filed in 2027. Covers who must file and the pre-filled return, the 3 May 2027 deadline, municipal tax (2026 average 32.38%, set by each kommun), state tax of 20% above SEK 643,000, the basic deduction (grundavdrag) and the higher amount from age 66, the job tax credit (jobbskatteavdrag), the 7% general pension contribution and its full credit, commuting and other work expense deductions, ROT and RUT credits, capital income at 30% and the deficit credit, the ISK standard income with the new SEK 300,000 tax-free amount, late-filing fees and cost interest. Trigger on: Swedish tax return, deklaration, kvarskatt, grundavdrag, jobbskatteavdrag, allmän pensionsavgift, reseavdrag, ROT, RUT, ISK tax, Sweden pensioner tax. Out of scope: se-income-tax (sole traders), se-social-contributions, sweden-payroll, se-capital-gains, se-cross-border, se-corporate-tax."
jurisdiction: SE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Sweden: income tax for employees and pensioners (income year 2026)

This skill computes the final tax of a person whose income is pay, pension and savings. Business income of a sole trader is in [se-income-tax](se-income-tax.md). Self-employed contributions are in [se-social-contributions](se-social-contributions.md). Monthly withholding and employer contributions are in [sweden-payroll](sweden-payroll.md). Gains on shares and property are in [se-capital-gains](se-capital-gains.md). Moving in or out of Sweden is in [se-cross-border](se-cross-border.md).

## Who this applies to

- People who are unlimited taxable in Sweden for the whole of 2026 (living in Sweden, or staying here six months in a row) and whose income is employment income (tjänst), pension and capital income. The residence tests are in [se-cross-border](se-cross-border.md).
- A person must file if their income from employment and business together was at least 42.3% of the price base amount (SEK 25,042 or more for 2026, as Skatteverket rounds it), if their capital income without a third-party statement was at least SEK 200, or if they are limited taxable with taxable income of at least SEK 100 (SFL 30 kap. 1 §).
- Skatteverket sends each such person a return already filled in from employers', banks' and fund managers' statements. If every figure is right, the person approves it in the e-service or by logging in with their codes. If anything is missing (commuting, a sale of shares, ROT paid outside the invoice model), they change or add it before approving.
- Out of scope: active business income, partnership income, close-company (fåmansföretag) dividends under 57 kap. IL, and SINK taxpayers.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Price base amount (prisbasbelopp) | SEK 59,200 | 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Income base amount (inkomstbasbelopp) | SEK 83,400 | 2026 | same page |
| Average municipal tax rate (kommun plus region) | 32.38%; each kommun and region sets its own rate | 2026 | same page; IL 65 kap. 3 § |
| State tax on earned income | 20% of taxable earned income above SEK 643,000 (skiktgräns) | 2026 | same page; IL 65 kap. 5 § |
| Point where state tax starts (brytpunkt), before credits | SEK 660,400 under 66; SEK 760,500 from 66 | 2026 | same page |
| Basic deduction, under 66 | SEK 25,100 at low income, at most SEK 45,600, at least SEK 17,400 at high income | 2026 | same page; IL 63 kap. 3 § |
| Basic deduction, 66 or over at 1 January 2026 | SEK 65,800 at low income, at most SEK 179,100, at least SEK 117,500 at high income | 2026 | same page; IL 63 kap. 3 a § |
| General pension contribution (allmän pensionsavgift) | 7% of employment and business income, income capped at 8.07 income base amounts; at most SEK 47,100 | 2026 | same page; Lag (1994:1744) 2-3 §§ |
| Credit for the pension contribution | 100% of the contribution | 2026 | IL 67 kap. 4 § |
| Job tax credit (jobbskatteavdrag), under 66 | Formula in IL 67 kap. 7 §; flat above 8.08 price base amounts (SEK 478,336); no phase-out | 2026 | IL 67 kap. 7 § (Lag 2025:1376) |
| Earned income credit (skattereduktion för förvärvsinkomst) | SEK 1,500 when taxable earned income is SEK 240,000 or more; 0.75% of the excess over SEK 40,000 between SEK 40,000 and 240,000 | 2026 | IL 67 kap. 46-47 §§ |
| Commuting to work | SEK 25 per mil (SEK 2.50 per km) by own car; only the part of the year's costs above SEK 15,000 | 2026 | same page; IL 12 kap. 2 and 27 §§ |
| Other work expenses | Only the part above SEK 5,000 | 2026 | IL 12 kap. 2 § |
| Tax on capital income | 30% | 2026 | IL 65 kap. 7 § |
| Capital deficit credit | 30% of a deficit up to SEK 100,000; 21% of the rest | 2026 | same page; IL 67 kap. 10 § |
| ISK standard income | Government borrowing rate at 30 November 2025 (2.55%) plus 1 point = 3.55%, floor 1.25% | 2026 | same page; IL 42 kap. 36 § |
| ISK, capital insurance and PEPP tax-free amount | First SEK 300,000 of the combined capital base | 2026 | same page; IL 42 kap. 48 § (Lag 2024:1132) |
| RUT credit (household services) | 50% of the labour cost | 2026 | IL 67 kap. 19 § (Lag 2025:322) |
| ROT credit (repair, maintenance, extension of own home) | 30% of the labour cost | 2026 | IL 67 kap. 19 § (Lag 2025:322) |
| ROT and RUT cap | SEK 75,000 per person a year in total, of which ROT at most SEK 50,000 | 2026 | IL 67 kap. 19 § |
| Unemployment fund fee credit | 25% of fees paid to an a-kassa | 2026 | IL 67 kap. 51 § |
| Burial fee (begravningsavgift) | 0.292% of taxable earned income; Stockholm 0.07%, Tranås 0.285% | 2026 | same page |
| Public service fee | At most SEK 1,184 per person a year | 2026 | same page |
| Late filing fee (individual) | SEK 1,250 at the deadline, a second SEK 1,250 after three months, a third after two more months | 2026 | SFL 48 kap. 6-7 §§ |
| Base interest rate on the tax account | 2.5% since 1 December 2024 (cost interest); 17.5% high rate | 2026 | https://www.skatteverket.se/rantapaskattekontot |

## The taxable base

**Earned income (förvärvsinkomst).** Add salary, taxable benefits, sick pay, parental benefit and pension. Deduct work expenses (only the excess over the SEK 15,000 or SEK 5,000 thresholds) to get the surplus of employment income. This is the assessed earned income (fastställd förvärvsinkomst).

**Commuting.** Reasonable costs of travel between home and work are deductible (IL 12 kap. 26 §). Car costs count only if the distance is at least 5 km and the car regularly saves a total of at least two hours compared with public transport, or if there is no public transport, or the car is used in the job on enough days (IL 12 kap. 27-28 §§). An own car is deducted at SEK 2.50 per km plus road, bridge, ferry and congestion charges. Add up the year's travel, then deduct SEK 15,000.

**Basic deduction.** Skatteverket computes it from the assessed earned income and the price base amount (IL 63 kap. 3 §), then rounds it up to the next SEK 100:

- up to 0.99 price base amounts: 0.423 PBB;
- 0.99 to 2.72 PBB: 0.423 PBB plus 20% of income above 0.99 PBB;
- 2.72 to 3.11 PBB: 0.77 PBB;
- 3.11 to 7.88 PBB: 0.77 PBB less 10% of income above 3.11 PBB;
- above 7.88 PBB (SEK 466,496): 0.293 PBB, which is SEK 17,400 after rounding.

A person who was 66 at 1 January 2026 (born 1959 or earlier) adds a special amount from the 12-band table in IL 63 kap. 3 a §. For 2027 the age moves to 67 (the version of 3 a § in force from 1 January 2027). The deduction cannot exceed the earned income (IL 63 kap. 5 §).

**Taxable earned income** is earned income less the basic deduction. Municipal tax is that amount times the rate of the kommun where the person was registered on 1 November 2025 (IL 65 kap. 3 §). State tax is 20% of the part above SEK 643,000.

**Pension contribution.** The employee pays 7% of pay, rounded to the nearest SEK 100. Income above 8.07 income base amounts (SEK 673,038) is ignored. No contribution is due if income is below 42.3% of the price base amount. Pension is not income from employment, so it carries no contribution, and neither does income-related sickness or activity compensation (Lag (1994:1744) 3-4 §§). The same amount comes back as a credit, so for an employee the net cost is nil. A self-employed person gets the credit only if the contribution was paid on time (IL 67 kap. 4 §).

**Job tax credit, under 66.** Credits count against municipal tax only (IL 67 kap. 2 §). With work income W (the surplus of employment income and of active business income, less general deductions, rounded down to SEK 100; IL 67 kap. 6 §), GA the basic deduction and K the municipal rate (IL 67 kap. 7 §):

- W up to 0.91 PBB: (W − GA) × K;
- 0.91 to 3.24 PBB: (0.91 PBB + 38.74% of W between 0.91 and 3.24 PBB − GA) × K;
- 3.24 to 8.08 PBB: (1.813 PBB + 25.1% of W between 3.24 and 8.08 PBB − GA) × K;
- above 8.08 PBB: (3.027 PBB − GA) × K.

The credit does not fall at high incomes. Pension is not work income, so a pensioner with no pay gets no job tax credit.

**Job tax credit, 66 or over.** 22% of work income up to 1.75 PBB; 0.2635 PBB plus 7% of work income from 1.75 to 5.24 PBB; 0.6293 PBB above 5.24 PBB (IL 67 kap. 8 §).

**Capital income.** Interest, dividends and gains outside an ISK, less deductible interest. Since 2026 interest is deductible only on loans with qualifying security or lender: a bank or mortgage-lender loan secured on property or a tenant-owner flat, a bank or securities-firm loan secured on listed securities or fund units, a pawnbroker loan, or a loan secured on the vehicle or boat it financed (IL 42 kap. 6 a-6 g §§; 2025 was a transition year at 50% for other loans). Interest on unsecured consumer loans and credit cards is not deductible. A surplus is taxed at 30%. A deficit gives the credit in the table above, which is set against tax on earned income and property fee.

**ISK.** Each quarter, add the value of the account on the first day and the deposits made in that quarter; the capital base is one quarter of the sum of the four (IL 42 kap. 37 §). Standard income is the base times 3.55%. A deduction removes the standard income on the first SEK 300,000 (SEK 150,000 in 2025) of combined ISK, capital insurance and PEPP savings, ISK first (IL 42 kap. 48 §). The rest is capital income at 30%. Gains and dividends inside the ISK are not taxed (IL 42 kap. 42 §).

**Order of credits** (IL 67 kap. 2 §): pension contribution, job tax credit, sickness and activity compensation, earned income credit, regional credit, capital deficit, household work (ROT and RUT), green technology, gifts, a-kassa fee. Credits are given in whole kronor (IL 67 kap. 1 §). A credit beyond the tax it can be set against is lost; it is not paid out.

**On top of income tax** the final tax includes the burial fee (0.292% of taxable earned income in most kommuner), the church fee for members of the Church of Sweden (set by each parish), and the public service fee (at most SEK 1,184). They are left out of the examples.

## Deadlines and filing

- Return for income year 2026: due 2 May 2027 (SFL 32 kap. 1 §). 2 May 2027 is a Sunday, so filing on Monday 3 May 2027 is on time (Lag (1930:173) 2 §).
- Residual tax (kvarskatt) up to SEK 30,000: no cost interest if it is on the tax account by 3 May 2027 (SFL 65 kap. 4 §). Above SEK 30,000: pay the excess by 12 February 2027 to avoid interest from 13 February 2027.
- Final tax due: the due date that falls first once 90 days have passed from the final tax decision (SFL 62 kap. 8 §).
- ROT and RUT: the contractor deducts the credit on the invoice. The person must pay the invoice electronically (IL 67 kap. 15 a §), and the credit belongs to the year the work was paid for, so payment by 31 December 2026 counts in 2026 (IL 67 kap. 12 §), and the contractor applies to Skatteverket. Confirm in the return that the amounts match.

## Penalties and interest

- Late filing fee: SEK 1,250; a second SEK 1,250 if still not filed three months after the deadline; a third after a further two months (SFL 48 kap. 6-7 §§). A person living abroad on the deadline pays no fee if they file by 31 May (SFL 48 kap. 3 §).
- Tax surcharge (skattetillägg) on an incorrect statement: 40% of the tax that would have been lost (SFL 49 kap. 11 §).
- Cost interest on residual tax: the base rate (SFL 65 kap. 4 §), which Skatteverket shows as 2.5% since 1 December 2024. Unpaid tax after the due date: base rate plus 15 points (17.5%) until handed to the Enforcement Authority (SFL 65 kap. 13 §).

## Cross-border points

- A person resident for only part of 2026 gets the basic deduction and job tax credit pro rata by month, unless almost all their earned income is Swedish (IL 63 kap. 4 §, 67 kap. 9 §).
- A non-resident who chose to be taxed as a resident under IL 3 kap. 18 § gets the basic deduction and credits only if almost all earned income is Swedish (IL 63 kap. 2 §).
- ISK value counts only for quarters in which the holder was unlimited taxable (IL 42 kap. 41 §).
- SINK, the expert relief and treaty relief are in [se-cross-border](se-cross-border.md).

## Worked examples

### Example 1: employee on SEK 600,000, average municipal rate

Anna is 40, works in Sweden all year for SEK 600,000 and has no other income or deductions. Her kommun charges the 2026 average of 32.38%.

- Basic deduction: income is above 7.88 PBB, so 0.293 × 59,200 = 17,345.60, rounded up to SEK 17,400.
- Taxable earned income: 600,000 − 17,400 = SEK 582,600. It is below SEK 643,000, so no state tax.
- Municipal tax: 582,600 × 32.38% = SEK 188,645.88.
- Pension contribution: 7% × 600,000 = SEK 42,000, credited back in full.
- Job tax credit: income is above 8.08 PBB, so (3.027 × 59,200 − 17,400) × 32.38% = 52,390.32, given as SEK 52,390.
- Earned income credit: SEK 1,500.
- Final income tax before burial, church and public service fees: 188,645.88 + 42,000 − 42,000 − 52,390 − 1,500 = SEK 134,755.88.

```oa-check
name: Employee, SEK 600,000 pay, average municipal rate 2026
inputs:
  pay: 600000
  pbb: 59200
  municipal_rate: 0.3238
  skiktgrans: 643000
steps:
  - basic_deduction: ceil(0.293 * pbb / 100) * 100
  - taxable_earned: pay - basic_deduction
  - municipal_tax: taxable_earned * municipal_rate
  - state_tax: max(taxable_earned - skiktgrans, 0) * 0.20
  - pension_contribution: pay * 0.07
  - pension_credit: pension_contribution
  - job_credit: floor((3.027 * pbb - basic_deduction) * municipal_rate)
  - earned_income_credit: 1500
  - final_tax: municipal_tax + state_tax + pension_contribution - pension_credit - job_credit - earned_income_credit
expected:
  basic_deduction: 17400.00
  taxable_earned: 582600.00
  municipal_tax: 188645.88
  state_tax: 0.00
  pension_contribution: 42000.00
  job_credit: 52390.00
  final_tax: 134755.88
```

### Example 2: ISK with a capital base of SEK 800,000

Erik has one ISK. The four quarterly values plus deposits average SEK 800,000. He has no capital insurance or PEPP, and no other capital income.

- Standard income: 800,000 × 3.55% = SEK 28,400.
- Tax-free deduction: at most 300,000 × 3.55% = SEK 10,650.
- Taxable capital income: 28,400 − 10,650 = SEK 17,750.
- Tax at 30%: SEK 5,325. That is 1.065% of the SEK 500,000 above the tax-free amount.
- The edge case: had the base been SEK 300,000 or less, the deduction would equal the standard income and no tax would be due.

```oa-check
name: ISK capital base SEK 800,000, income year 2026
inputs:
  capital_base: 800000
  borrowing_rate: 0.0255
  tax_free_base: 300000
steps:
  - schablon_rate: max(borrowing_rate + 0.01, 0.0125)
  - standard_income: capital_base * schablon_rate
  - deduction: min(standard_income, tax_free_base * schablon_rate)
  - taxable_capital: standard_income - deduction
  - tax: taxable_capital * 0.30
expected:
  standard_income: 28400.00
  deduction: 10650.00
  taxable_capital: 17750.00
  tax: 5325.00
```

## Ask the client first

1. Date of birth. At 66 by 1 January 2026 (born 1959 or earlier), the higher basic deduction and the older job tax credit apply.
2. The kommun where they were registered on 1 November 2025, and whether they belong to the Church of Sweden.
3. Did they live in Sweden all of 2026? If not, how much of their earned income was Swedish.
4. Commuting: distance, days, car or public transport, and the time saved by car.
5. Savings: ISK, capital insurance and PEPP balances; sales of shares or funds outside an ISK; loan interest paid.
6. ROT or RUT work paid in 2026, with invoices showing the credit already given.

## Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), as amended to SFS 2026:1393: 12 kap. 2, 26-27 §§; 42 kap. 6 a-6 g, 36-48 §§; 63 kap. 2-5 §§; 65 kap. 3-7 §§; 67 kap. 1-10, 11-19, 46-51 §§; transitional rules 2024:1132, 2024:1177, 2025:322, 2025:1376 | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-23 |
| Lag (1994:1744) om allmän pensionsavgift, 2-4 §§ | https://data.riksdagen.se/dokument/sfs-1994-1744.text | 2026-10-23 |
| Skatteförfarandelag (2011:1244): 30 kap. 1 §; 32 kap. 1 §; 48 kap. 3, 6-7 §§; 49 kap. 11 §; 62 kap. 8 §; 65 kap. 3-6, 13 §§ | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-23 |
| Lag (1930:173) om beräkning av lagstadgad tid, 2 § | https://data.riksdagen.se/dokument/sfs-1930-173.text | 2026-10-23 |
| Skatteverket, belopp och procent inkomstår 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-23 |
| Skatteverket, ränta på skattekontot | https://www.skatteverket.se/rantapaskattekontot | 2026-10-23 |
| Skatteverket, deklaration | https://www.skatteverket.se/privat/deklaration | 2026-10-23 |
| Skatteverket, rot- och rutarbete | https://www.skatteverket.se/privat/fastigheterochbostad/rotochrutarbete.4.2e56d4ba1202f95012080002966.html | 2026-10-23 |

Not yet confirmed: the average church fee rate (not on the page read); the base interest rate in force in 2027 when residual tax for 2026 is charged (Skatteverket shows 2.5% from 1 December 2024 and the rate can change); whether the job tax credit uses the price base amount multiple rounded before the municipal rate is applied (the example uses the unrounded product and drops öre as 67 kap. 1 § requires); the date Skatteverket will publish for the 2027 filing round (the law gives 3 May 2027).
