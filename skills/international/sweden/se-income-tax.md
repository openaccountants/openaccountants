---
name: se-income-tax
description: "Use for Swedish personal income tax for income year 2026 (return filed in 2027), with the full computation for a sole trader (enskild firma, enskild näringsidkare). Covers municipal and regional tax (2026 average 32.38%), state tax of 20% above the SEK 643,000 skiktgräns, the basic deduction (grundavdrag) and the higher amount from 66, the job tax credit (jobbskatteavdrag), the 7% pension contribution and its credit, capital income at 30%, ISK and capital insurance standard income with the SEK 300,000 tax-free amount, ROT and RUT, business income on the NE form (schablonavdrag for egenavgifter, räntefördelning, expansionsfond, depreciation, home office, representation), F-tax instalments, the 2 May deadline (3 May 2027), final tax dates, late-filing fees, tax surcharge and cost interest. Trigger on: Swedish income tax, kommunalskatt, statlig inkomstskatt, grundavdrag, jobbskatteavdrag, NE-bilaga, enskild firma, F-skatt, ISK, rot, rut, kvarskatt. Out of scope: se-employee-income-tax, se-social-contributions, sweden-payroll, se-capital-gains, se-closely-held-company-312, se-corporate-tax, se-cross-border."
version: 2.1
jurisdiction: SE
category: international
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SE Income Tax

This skill sets out Swedish income tax for an individual for income year 2026 and works the full computation for a sole trader. The return of a person with only pay and pension is worked in [se-employee-income-tax](se-employee-income-tax.md). Self-employed contributions (egenavgifter) in detail are in [se-social-contributions](se-social-contributions.md). Monthly withholding is in [sweden-payroll](sweden-payroll.md). Gains on shares and homes are in [se-capital-gains](se-capital-gains.md). Dividends from a close company are in [se-closely-held-company-312](se-closely-held-company-312.md). Companies are in [se-corporate-tax](se-corporate-tax.md). Moving in or out is in [se-cross-border](se-cross-border.md).

## Who this applies to

- Individuals who are unlimited taxable in Sweden (living here, or staying here six months in a row). They pay municipal and regional tax and state tax on earned income, and state tax on capital income. The residence tests are in [se-cross-border](se-cross-border.md).
- Sole traders (enskild näringsidkare). The business surplus from the NE form is earned income. It carries egenavgifter, the pension contribution and the job tax credit.
- A person must file if earned income was SEK 25,042 or more in 2026 (Skatteverket, skattefri årsinkomst SEK 25,041). Every sole trader files an NE form with Inkomstdeklaration 1.
- Out of scope here: aktiebolag (the owner's dividends and salary go to se-closely-held-company-312 and sweden-payroll), partnerships (handelsbolag, kommanditbolag), which allocate income between partners under their own rules, and SINK taxpayers.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Price base amount (prisbasbelopp, PBB) | SEK 59,200 | 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Income base amount (inkomstbasbelopp) | SEK 83,400 | 2026 | same page |
| Municipal plus regional tax | Rate of the kommun where the person was registered on 1 November 2025 (IL 65 kap. 3 §). Average 32.38%; lowest Österåker 28.93%; highest Dorotea 35.65%; Stockholm 30.55% (18.22% + 12.33%) | 2026 | same page; https://skatteverket.entryscape.net/rowstore/dataset/c67b320b-ffee-4876-b073-dd9236cd2a99 |
| State tax on earned income | 20% of taxable earned income above SEK 643,000 (skiktgräns), every age | 2026 | IL 65 kap. 5 §; same page |
| Brytpunkt (income before the basic deduction where state tax starts) | SEK 660,400 under 66; SEK 760,500 from 66 | 2026 | same page |
| Basic deduction, under 66 at 1 January 2026 | SEK 25,100 at low income, at most SEK 45,600, at least SEK 17,400; band formula in IL 63 kap. 3 § | 2026 | IL 63 kap. 3 §; same page |
| Basic deduction, 66 or over at 1 January 2026 (born 1959 or earlier) | 3 § amount plus the special amount in IL 63 kap. 3 a §: SEK 65,800 at low income, at most SEK 179,100, at least SEK 117,500 | 2026 | IL 63 kap. 3 a § (Lag 2025:1376); same page |
| Job tax credit, under 66 | Four-band formula, flat above 8.08 PBB; set against municipal tax only | 2026 | IL 67 kap. 2 and 7 §§ (Lag 2025:1376) |
| Job tax credit, 66 or over | 22% of work income up to 1.75 PBB; 0.2635 PBB plus 7% of work income up to 5.24 PBB; 0.6293 PBB above | 2026 | IL 67 kap. 8 § |
| Earned income credit | SEK 1,500; 0.75% of taxable earned income above SEK 40,000 when it is between SEK 40,000 and 240,000 | 2026 | IL 67 kap. 46-47 §§ |
| General pension contribution | 7% of employment and business income, at most SEK 47,100; credited back 100% | 2026 | Lag (1994:1744) 2-4 §§; IL 67 kap. 4 §; same page |
| Egenavgifter (sole trader) | 28.97% born 1959 or later; 10.21% born 1938-1958; none born 1937 or earlier | 2026 | same page; detail in se-social-contributions |
| Egenavgift reduction | 7.5% of the business base, at most SEK 15,000, if the business base is above SEK 40,000 and the person was not 67 at 1 January | 2026 | Lag (2023:748) 3 § (as amended by 2023:754, in force 1 January 2026) |
| Schablonavdrag for egenavgifter | 25% of the surplus (born 1959 or later); 10% (born 1938-1958, or full old-age pension all year) | 2026 | IL 16 kap. 29-30 §§; same page |
| Tax on capital income | 30% of the surplus | 2026 | IL 65 kap. 7 § |
| Capital deficit credit | 30% of a deficit up to SEK 100,000; 21% of the rest | 2026 | IL 67 kap. 10 § |
| ISK standard income | Capital base × (government borrowing rate 30 November 2025 of 2.55% + 1 point) = 3.55%; floor 1.25% | 2026 | IL 42 kap. 36-37 §§; same page |
| Capital insurance (kapitalförsäkring) yield tax | 30% of capital base × 3.55%, charged on the insurer | 2026 | Lag (1990:661) 3 d and 9 §§ |
| Tax-free amount for ISK, capital insurance and PEPP | Standard income on the first SEK 300,000 of combined savings, ISK first | 2026 | IL 42 kap. 48 § (Lag 2024:1132, from 1 January 2026) |
| RUT credit (household services) | 50% of the labour cost | 2026 | IL 67 kap. 19 § (Lag 2025:322) |
| ROT credit (repair and extension of own home) | 30% of the labour cost | 2026 | IL 67 kap. 19 § (Lag 2025:322); Lag (2009:194) 7 § |
| ROT and RUT cap | SEK 75,000 a person a year in total, ROT at most SEK 50,000 | 2026 | IL 67 kap. 19 § |
| Positive räntefördelning | 8.55% of a positive capital base (2.55% + 6 points); optional | 2026 | IL 33 kap. 2-3 §§; same page |
| Negative räntefördelning | 3.55% of the capital base; required only below minus SEK 500,000 | 2026 | IL 33 kap. 3-4 §§; same page |
| Expansionsfond | Tax 20.6% on the allocation, credited back on reversal; ceiling = net assets at year end ÷ 0.794 | 2026 | IL 65 kap. 8 §; same page |
| Low-value equipment (expense at once) | Cost excluding VAT below half a PBB, SEK 29,600 | 2026 | IL 18 kap. 4 § |
| Equipment depreciation | Up to 30% a year (book depreciation) or 25% (reducing balance); 20% straight-line backstop | 2026 | IL 18 kap. 13 and 17 §§ |
| Own car used in the business | SEK 2.50 per km (SEK 25 per mil) if the car is not a business asset | 2026 | IL 16 kap. 27 § |
| Home office without a fitted-out room (at least 800 hours) | SEK 2,000 a year on own or spouse's property; SEK 4,000 otherwise | 2026 | IL 16 kap. 35 § |
| Representation | Meals SEK 0; simple refreshments SEK 60 per person; theatre, golf and similar SEK 180 per person; all excluding VAT | 2026 | IL 16 kap. 2 §; same page |
| VAT exemption for small turnover | Turnover in Sweden not above SEK 120,000 this year or either of the two before | 2026 | ML (2023:200) 18 kap. 4 § |
| Burial fee | 0.292%; Stockholm 0.07%; Tranås 0.285% | 2026 | same page |
| Late filing fee | SEK 1,250; again after three months; again after two more months | 2026 | SFL 48 kap. 6-7 §§ |
| Tax surcharge | 40% of the final tax that would have been lost; 10% for a timing error | 2026 | SFL 49 kap. 11 §; same page |
| Cost interest | Base rate 2.5% since 1 December 2024; late payment base rate + 15 points = 17.5% | 2026 | SFL 65 kap. 3-4, 13 §§; https://www.skatteverket.se/rantapaskattekontot |

## The taxable base

**Three income types.** Employment (tjänst), business (näringsverksamhet) and capital (kapital). Employment and business together are earned income (förvärvsinkomst). Capital is taxed on its own at 30%.

**Earned income to taxable income.** Add the employment surplus and the business surplus to get assessed earned income. Deduct the basic deduction to get taxable earned income (beskattningsbar förvärvsinkomst). Municipal tax is that amount times the kommun's total rate. State tax is 20% of the part above SEK 643,000.

**Basic deduction.** Skatteverket computes it from assessed earned income and rounds it up to the next SEK 100 (IL 63 kap. 2 §). Under 66 (IL 63 kap. 3 §): up to 0.99 PBB, 0.423 PBB; 0.99 to 2.72 PBB, 0.423 PBB plus 20% of the excess over 0.99 PBB; 2.72 to 3.11 PBB, 0.77 PBB; 3.11 to 7.88 PBB, 0.77 PBB less 10% of the excess over 3.11 PBB; above 7.88 PBB, 0.293 PBB. From 66 at 1 January 2026, add the special amount from the twelve-band table in IL 63 kap. 3 a § (for example 35.6% of income less 0.073 PBB between 3.24 and 5.00 PBB). From 2027 the age in 3 a § becomes 67 (Lag 2025:1374).

**Credits.** Credits come off in this order (IL 67 kap. 2 §): pension contribution, job tax credit, sickness and activity compensation, earned income credit, regional credit, capital deficit, household work, green technology, gifts, unemployment fund fee. The job tax credit and the earned income credit come off municipal tax only. Credits are in whole kronor (IL 67 kap. 1 §). A credit larger than the tax it can be set against is lost. Credits never reduce the pension contribution itself.

**Job tax credit.** Work income is the employment surplus plus the active business surplus, less general deductions, rounded down to SEK 100 (IL 67 kap. 6 §). Under 66 (IL 67 kap. 7 §), with GA the basic deduction and K the municipal rate: up to 0.91 PBB, (W − GA) × K; 0.91 to 3.24 PBB, (0.91 PBB + 38.74% of W between 0.91 and 3.24 PBB − GA) × K; 3.24 to 8.08 PBB, (1.813 PBB + 25.1% of W between 3.24 and 8.08 PBB − GA) × K; above 8.08 PBB, (3.027 PBB − GA) × K. From 66, use IL 67 kap. 8 § from the table above.

**Pension contribution.** 7% of employment and business income, each rounded down to SEK 100, ignoring income above 8.07 income base amounts, nothing if income is below 42.3% of a PBB; the contribution is rounded to the nearest SEK 100 (Lag 1994:1744 3-4 §§). A sole trader gets the credit only if the contribution was paid on time (IL 67 kap. 4 §).

**Business income (NE form).** Book income and costs net of VAT if the business is VAT-registered. Tax payments, VAT payments, owner drawings and deposits, loan principal and transfers between own accounts are not income or costs. Interest received goes to capital, not business. Then:
- Schablonavdrag: deduct 25% of the surplus (10% where only the 10.21% rate applies) to cover this year's egenavgifter; it is reversed next year and replaced by the egenavgifter actually charged (IL 16 kap. 29-30 §§). Egenavgifter are then computed on the surplus after this deduction.
- Equipment: a purchase below SEK 29,600 excluding VAT, or with a life of three years or less, is deducted at once. Items with a natural link are tested on their combined cost (IL 18 kap. 4 §). Others go into the equipment pool (IL 18 kap. 13 §).
- Own car: SEK 2.50 per km for business trips in a car that is not a business asset (IL 16 kap. 27 §). A business car is deducted at actual cost.
- Home office: either a reasonable share of rent and heating for a part of the home fitted out for the business (IL 16 kap. 34 §), or the flat SEK 2,000 or SEK 4,000 if the person worked at least 800 hours at home (IL 16 kap. 35 §). Not both.
- Representation: deductible only if directly linked to the business; meals SEK 0 (IL 16 kap. 2 §).
- Räntefördelning: a positive capital base allows 8.55% of it to move from business income to capital income (30%). A capital base below minus SEK 500,000 forces 3.55% the other way (IL 33 kap.).
- Periodiseringsfond: a sole trader may set aside up to 30% of the surplus, to be reversed within six years (Skatteverket, belopp och procent 2026).
- Expansionsfond: an allocation is taxed at 20.6% now and the 20.6% is credited back when it is reversed; the fund must be reversed when the business stops (IL 34 kap. 16 §, 65 kap. 8 §).
- Losses: a business deficit carries forward to the next year with no time limit, against the same business (IL 40 kap. 2 §).
- Records: books and vouchers are kept until the end of the seventh year after the year the financial year ended (BFL 7 kap. 2 §).

**Capital income.** Interest, dividends and gains outside an ISK, less deductible interest. From 2026 interest is deductible only on loans with qualifying security or lender (IL 42 kap. 6 a-6 g §§). A surplus is taxed at 30%. A deficit gives the 30% or 21% credit.

**ISK and capital insurance.** For an ISK, the capital base is a quarter of the sum of the value at the start of each quarter plus deposits in the year (IL 42 kap. 37 §). Standard income is the base times 3.55% and is taxed at 30% as capital income. Gains and dividends inside the ISK are not taxed. Capital insurance is taxed through a 30% yield tax charged on the insurer (Lag 1990:661 9 §). From 2026 the standard income on the first SEK 300,000 of combined ISK, capital insurance and PEPP savings comes back as a capital deduction, ISK first (IL 42 kap. 48 §). Skatteverket gives it automatically.

**ROT and RUT.** The buyer must be 18 or over at year end, the work must be for their own household or that of a parent living in Sweden, in a home within the EEA, and the contractor must hold F-tax (IL 67 kap. 11, 14-16 §§). Payment must be electronic (IL 67 kap. 15 a §). Only labour counts, not materials or travel (IL 67 kap. 18 §). The contractor normally takes the credit off the invoice and claims it from Skatteverket; the credit belongs to the year the work was paid (IL 67 kap. 12 §).

## Deadlines and filing

- Inkomstdeklaration 1 is due 2 May the year after the income year (SFL 32 kap. 1 §). 2 May 2027 is a Sunday, so the return for 2026 is on time on Monday 3 May 2027 (Lag 1930:173 2 §). For the 2025 return Skatteverket used 4 May 2026 for the same reason.
- Filing is digital in the e-service with BankID or the codes on the paper return, or on paper. A sole trader adds the NE form.
- An accounting firm can get an extension for its clients. In 2026 the extended date was 15 June (Skatteverket, få skatteåterbäring).
- F-tax: a sole trader applies to be approved for F-tax (SFL 9 kap.) and pays preliminary tax in equal monthly amounts from February to January, due on the 12th, and on the 17th in January and August (SFL 62 kap. 4 §).
- Final tax (slutlig skatt): Skatteverket must send the final tax notice to individuals by 15 December of the year after the income year (SFL 56 kap. 10 §). In the 2026 round notices went out 6-10 April for returns approved digitally without changes by 31 March, 8-12 June for returns filed by 4 May, 3-7 August for extended or later returns, and 7-11 December for the rest. Refunds are paid with the notice. Skatteverket has not yet published the 2027 dates.
- Residual tax (kvarskatt) is due on the first due date after 90 days from the final tax decision (SFL 62 kap. 8-9 §§). In 2026, a notice in June was due 14 September 2026 and one in August on 12 November 2026.

## Penalties and interest

- Late filing: SEK 1,250; a second SEK 1,250 if still not filed three months after the deadline; a third SEK 1,250 after two more months (SFL 48 kap. 6-7 §§). A person living abroad on the deadline pays no fee if they file by 31 May (SFL 48 kap. 3 §).
- Tax surcharge (skattetillägg): 40% of the final tax that would have been lost through an incorrect statement, 20% for other taxes (SFL 49 kap. 11 §). For a wrong deficit in business or employment, 40% of a quarter of the reduction. For a timing error, 10% (Skatteverket, belopp och procent 2026).
- Cost interest on residual tax runs from 13 February the year after the income year at the base rate (SFL 65 kap. 4 and 6 §§). On residual tax up to SEK 30,000 there is no interest up to 3 May (the 3rd of the fifth month). In 2026 Skatteverket started it on 5 May 2026. To avoid interest on residual tax above SEK 30,000, pay the excess by 12 February 2027.
- Unpaid tax after the due date carries the base rate plus 15 points (17.5% at the current base rate) until it goes to the Enforcement Authority (SFL 65 kap. 13 §). Cost interest is not deductible.

## Cross-border points

- A person limited taxable for all of 2026 who did not choose resident taxation pays a flat 25% municipal tax on earned income (IL 65 kap. 4 §). One who chose to be taxed as a resident under IL 3 kap. 18 § pays the average rate, 32.38% (Skatteverket, belopp och procent 2026).
- A non-resident who chose resident taxation under IL 3 kap. 18 § gets the basic deduction, job tax credit and earned income credit only if all or almost all earned income is Swedish (IL 63 kap. 2 §, 67 kap. 5 and 46 §§).
- Someone resident for part of the year gets the basic deduction and credits pro rata by month, unless almost all earned income is Swedish (IL 63 kap. 4 §, 67 kap. 9 and 48 §§).
- Self-employment carried on abroad counts as work income for the job tax credit if the person worked in it to a real extent (IL 67 kap. 6 §).
- ROT and RUT can cover a home anywhere in the EEA; work for a parent needs the parent to live in Sweden; a foreign contractor with no Swedish business needs a home-country certificate equal to F-tax (IL 67 kap. 14-15 and 17 §§).
- SINK, the expert tax relief and treaty relief are in [se-cross-border](se-cross-border.md).

## Worked examples

### Example 1: sole trader in Stockholm, profit SEK 600,000

Born 1985, registered in Stockholm on 1 November 2025 (30.55%). Booked net profit SEK 600,000. No räntefördelning, periodiseringsfond or expansionsfond. No other income.

- Schablonavdrag 25%: SEK 150,000. Assessed earned income SEK 450,000.
- Basic deduction: 450,000 is between 3.11 and 7.88 PBB, so 0.77 × 59,200 − 10% × (450,000 − 3.11 × 59,200) = 18,995.20, rounded up to SEK 19,000.
- Taxable earned income SEK 431,000. Below SEK 643,000, so no state tax.
- Municipal tax: 431,000 × 30.55% = SEK 131,670.50.
- Pension contribution 7% × 450,000 = SEK 31,500, credited back if paid on time.
- Job tax credit: (1.813 × 59,200 + 25.1% × (450,000 − 3.24 × 59,200) − 19,000) × 30.55% = 46,782.98, given as SEK 46,782.
- Earned income credit SEK 1,500.
- Income tax before burial fee: 131,670.50 + 31,500 − 31,500 − 46,782 − 1,500 = SEK 83,388.50.
- Egenavgifter: 28.97% × 450,000 = 130,365, less the reduction of 7.5% × 450,000 capped at SEK 15,000, so SEK 115,365.

```oa-check
name: Sole trader born 1985, Stockholm, net profit SEK 600,000 (2026)
inputs:
  net_profit: 600000
  pbb: 59200
  municipal_rate: 0.3055
  skiktgrans: 643000
steps:
  - schablonavdrag: net_profit * 0.25
  - earned_income: net_profit - schablonavdrag
  - basic_deduction: ceil((0.77 * pbb - 0.10 * (earned_income - 3.11 * pbb)) / 100) * 100
  - taxable_earned: earned_income - basic_deduction
  - municipal_tax: taxable_earned * municipal_rate
  - state_tax: max(taxable_earned - skiktgrans, 0) * 0.20
  - pension_contribution: round(earned_income * 0.07 / 100) * 100
  - work_income: floor(earned_income / 100) * 100
  - job_credit: floor((1.813 * pbb + 0.251 * (work_income - 3.24 * pbb) - basic_deduction) * municipal_rate)
  - earned_income_credit: 1500
  - income_tax: municipal_tax + state_tax + pension_contribution - pension_contribution - job_credit - earned_income_credit
  - egenavgifter: earned_income * 0.2897 - min(earned_income * 0.075, 15000)
expected:
  schablonavdrag: 150000.00
  earned_income: 450000.00
  basic_deduction: 19000.00
  taxable_earned: 431000.00
  municipal_tax: 131670.50
  state_tax: 0.00
  pension_contribution: 31500.00
  job_credit: 46782.00
  income_tax: 83388.50
  egenavgifter: 115365.00
```

### Example 2: sole trader born 1958, credits capped by the tax

Born 1958, so 66 or over at 1 January 2026 and in the 1938-1958 group for egenavgifter. Average municipal rate 32.38%. Net profit SEK 300,000. No other income.

- Schablonavdrag 10%: SEK 30,000. Assessed earned income SEK 270,000 (4.56 PBB).
- Basic deduction: 3 § part 0.77 × 59,200 − 10% × (270,000 − 3.11 × 59,200) = 36,995.20; 3 a § special amount, band 3.24 to 5.00 PBB, 35.6% × 270,000 − 0.073 × 59,200 = 91,798.40. Total 128,793.60, rounded up to SEK 128,800.
- Taxable earned income SEK 141,200. Municipal tax 141,200 × 32.38% = SEK 45,720.56. No state tax.
- Pension contribution 7% × 270,000 = SEK 18,900. Its credit comes first and uses SEK 18,900 of the municipal tax.
- Job tax credit from 66 (IL 67 kap. 8 §), work income between 1.75 and 5.24 PBB: 0.2635 × 59,200 + 7% × 270,000 = SEK 34,499. Only SEK 26,820 of municipal tax is left, so the credit is cut to SEK 26,820. The earned income credit finds no tax left.
- Final income tax: 45,720.56 + 18,900 − 18,900 − 26,820 = SEK 18,900.56, which is in effect the pension contribution.
- Egenavgifter: only the old-age pension contribution, 10.21% × 270,000 = SEK 27,567, with no 7.5% reduction (the person was 67 or over at the start of the year, Lag 2023:748 3 §).

```oa-check
name: Sole trader born 1958, average rate, net profit SEK 300,000 (2026)
inputs:
  net_profit: 300000
  pbb: 59200
  municipal_rate: 0.3238
steps:
  - schablonavdrag: net_profit * 0.10
  - earned_income: net_profit - schablonavdrag
  - ga_main: 0.77 * pbb - 0.10 * (earned_income - 3.11 * pbb)
  - ga_extra: 0.356 * earned_income - 0.073 * pbb
  - basic_deduction: ceil((ga_main + ga_extra) / 100) * 100
  - taxable_earned: earned_income - basic_deduction
  - municipal_tax: taxable_earned * municipal_rate
  - pension_contribution: round(earned_income * 0.07 / 100) * 100
  - pension_credit: min(pension_contribution, municipal_tax)
  - work_income: floor(earned_income / 100) * 100
  - job_credit_formula: floor(0.2635 * pbb + 0.07 * work_income)
  - job_credit: min(job_credit_formula, floor(municipal_tax - pension_credit))
  - earned_income_credit: min(1500, floor(municipal_tax - pension_credit - job_credit))
  - final_tax: municipal_tax + pension_contribution - pension_credit - job_credit - earned_income_credit
  - egenavgifter: earned_income * 0.1021
expected:
  earned_income: 270000.00
  basic_deduction: 128800.00
  taxable_earned: 141200.00
  municipal_tax: 45720.56
  pension_contribution: 18900.00
  job_credit_formula: 34499.00
  job_credit: 26820.00
  earned_income_credit: 0.00
  final_tax: 18900.56
  egenavgifter: 27567.00
```

## Ask the client first

1. Year of birth. It sets the basic deduction table, the job tax credit table, the egenavgift rate and the schablonavdrag.
2. The kommun where they were registered on 1 November 2025, and whether they belong to the Church of Sweden.
3. Did they live in Sweden all of 2026? If not, what share of earned income was Swedish.
4. For a sole trader: the booked result, whether VAT-registered, the net business assets at the start and end of the year (räntefördelning, expansionsfond), prior-year deficits, home office hours and whether they own or rent, and whether F-tax was paid on time.
5. Savings: ISK, capital insurance and PEPP balances, sales outside an ISK, loan interest and the security behind each loan.
6. ROT or RUT work paid in 2026, with the invoices showing the credit already given.

## Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), as amended to SFS 2026:1393: 16 kap. 2, 27, 29-30, 34-35 §§; 18 kap. 4, 13, 17 §§; 33 kap. 2-4 §§; 34 kap. 16 §; 40 kap. 2 §; 42 kap. 6 a, 36-37, 48 §§; 63 kap. 2-3 a §§; 65 kap. 3-8 §§; 67 kap. 1-12, 14-19, 46-48 §§; transitional rules 2024:1132, 2025:322, 2025:1374, 2025:1376 | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-24 |
| Skatteförfarandelag (2011:1244), as amended to SFS 2026:1305: 32 kap. 1 §; 48 kap. 3, 6-7 §§; 49 kap. 11 §; 56 kap. 10 §; 62 kap. 4, 8-9 §§; 65 kap. 3-6, 13 §§ | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-24 |
| Lag (1994:1744) om allmän pensionsavgift, 2-4 §§ | https://data.riksdagen.se/dokument/sfs-1994-1744.text | 2026-10-24 |
| Lag (2023:748) om särskilt avdrag vid beräkning av egenavgifter, 3 § (as amended by 2023:754) | https://data.riksdagen.se/dokument/sfs-2023-748.text | 2026-10-24 |
| Lag (2009:194) om förfarandet vid skattereduktion för hushållsarbete, 7 § | https://data.riksdagen.se/dokument/sfs-2009-194.text | 2026-10-24 |
| Lag (1990:661) om avkastningsskatt på pensionsmedel, 3 d and 9 §§ | https://data.riksdagen.se/dokument/sfs-1990-661.text | 2026-10-24 |
| Mervärdesskattelag (2023:200), 18 kap. 4 § | https://data.riksdagen.se/dokument/sfs-2023-200.text | 2026-10-24 |
| Bokföringslag (1999:1078), 7 kap. 2 § | https://data.riksdagen.se/dokument/sfs-1999-1078.text | 2026-10-24 |
| Lag (1930:173) om beräkning av lagstadgad tid, 2 § | https://data.riksdagen.se/dokument/sfs-1930-173.text | 2026-10-24 |
| Skatteverket, belopp och procent inkomstår 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-24 |
| Skatteverket, skattesatser per kommun 2026 (open data) | https://skatteverket.entryscape.net/rowstore/dataset/c67b320b-ffee-4876-b073-dd9236cd2a99 | 2026-10-24 |
| Skatteverket, ränta på skattekontot | https://www.skatteverket.se/rantapaskattekontot | 2026-10-24 |
| Skatteverket, deklaration | https://www.skatteverket.se/privat/deklaration | 2026-10-24 |
| Skatteverket, få skatteåterbäring (2026 notice and refund dates) | https://www.skatteverket.se/privat/deklaration/faskatteaterbaring.4.12815e4f14a62bc048f10101.html | 2026-10-24 |
| Skatteverket, betala kvarskatt | https://www.skatteverket.se/privat/deklaration/betalakvarskatt.4.12815e4f14a62bc048f106ca.html | 2026-10-24 |

Not yet confirmed: the 2027 notice, refund and extension dates (Skatteverket has published only the 2026 round); the base interest rate in force when 2026 residual tax is charged; whether Skatteverket rounds the 66-plus basic deduction once on the total, as Example 2 does, or on each part; the regional reduction of egenavgifter (Lag 2001:1170) and the egenavgift waiting-period options, left to se-social-contributions; the NE form line for each income and cost type (R1-R47) and the bank-statement classification library of the old version, which are working practice rather than law and were not re-read on an official page; the church fee rate for a given parish.

> Contributed by Ryan Duguid.

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
