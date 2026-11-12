---
name: fk-payroll-social
description: Run ordinary Falkland Islands payroll withholding and Retirement Pension
  Contributions for 2026, with self-employed contribution coverage. Use for POAT,
  RPC, Medical Services Tax, new employee notification, EMP-02, E-POAT, monthly payment,
  certificates and employer year-end questions. Distinguishes resident main employment
  from secondary and non-resident employment and uses the official weekly or monthly
  payroll tables rather than simply dividing annual income tax. Includes pension earnings
  thresholds, multiple jobs, resident and overseas voluntary contributions and late-payment
  boundaries. Defence-related exemptions, unusual benefits, agency status and special
  pensions require the specific official determination rather than an assumed exemption.
jurisdiction: FK
category: payroll
type: situation-rules
domain: tax
tax_year: 2026
tier: 2
last_updated: '2026-11-11'
version: '0.1'
---

# Falkland Islands payroll and social contributions 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers paying remuneration to employees, former employees and directors must consider POAT; agencies and intermediaries may also be caught. RPC is a separate pension contribution, normally for resident people from age 17 until their applicable pensionable age, subject to earnings and other exemptions. Self-employed people register and pay their own RPC. Medical Services Tax currently has a zero rate; this does not cancel POAT or RPC. [FIGTO 2026 employer guide](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf); [Pensions Office](https://www.gov.fk/pensions/retirement-pension-scheme/).

Quick answer: determine employee status, residence, main employment, pay period, pension age and earnings before calculating. Use the actual 2026 pack tables; annual income-tax allowances are owned by [fk-income-tax](fk-income-tax.md).

## Rates, bands and thresholds

| Item | 2026 rule and condition | Official source |
|---|---|---|
| Secondary employer or non-resident employee | Subject to the low-hours exception below, POAT 21% of gross remuneration, without a second personal allowance | [Employer guide p1](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf#page=1) |
| Resident main employer, monthly table | GBP 1,405 monthly zero point; first GBP 1,500 above it at 21%, excess at 26%, as represented by the published monthly table | [Workbook, Monthly sheet A7/B7, G73/H73 and G74/H74](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2.-2026-Employer-Workbook.xlsx) |
| Resident main employer, weekly table | Published zero point GBP 325; use the Weekly sheet rather than annual allowance divided by weeks | [Workbook, Weekly sheet A6:B8](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2.-2026-Employer-Workbook.xlsx) |
| Medical Services Tax | 0% for individuals and employers | [2026 guide §5](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/General-Tax-Guide-Individuals-2026.pdf#page=2) |
| Employee RPC | GBP 23.90 per liable week | [2026 rate notice](https://www.gov.fk/pensions/wp-content/uploads/sites/36/2026/06/RPC_Rates_2026_for_Circulation.pdf) |
| Employer RPC | GBP 23.90 per liable week | [2026 rate notice](https://www.gov.fk/pensions/wp-content/uploads/sites/36/2026/06/RPC_Rates_2026_for_Circulation.pdf) |
| Self-employed RPC | GBP 47.80 per liable week | [2026 rate notice](https://www.gov.fk/pensions/wp-content/uploads/sites/36/2026/06/RPC_Rates_2026_for_Circulation.pdf) |
| Earnings limit | GBP 386.40 weekly; published monthly equivalent GBP 1,674.40; liability tested for weeks with earnings above the limit | [Rate notice](https://www.gov.fk/pensions/wp-content/uploads/sites/36/2026/06/RPC_Rates_2026_for_Circulation.pdf), [Pensions Office](https://www.gov.fk/pensions/retirement-pension-scheme/) |
| Voluntary resident / overseas contribution | GBP 47.80 / GBP 64.60 weekly, respectively, only where entitled to contribute | [2026 rate notice](https://www.gov.fk/pensions/wp-content/uploads/sites/36/2026/06/RPC_Rates_2026_for_Circulation.pdf) |

The RPC notice allocates liable weeks by Mondays: January 4, February 4, March 5, April 4, May 4, June 5, July 4, August 5, September 4, October 4, November 5, December 4. Never use four weeks for every month. These are week counts, not a rule that a worker is liable in every week. [2026 notice](https://www.gov.fk/pensions/wp-content/uploads/sites/36/2026/06/RPC_Rates_2026_for_Circulation.pdf).

## The base

Before selecting table or flat-rate POAT, apply regulations 3(2)-(3). For monthly-paid employees no income-tax POAT deduction is required or authorised below 60 paid hours in the period. Weekly-paid employees need both fewer than 15 paid hours in the current period and fewer than 60 across it and its three predecessors, taking all employers into account. Paid hours include paid non-working hours. This is a withholding exception, not an annual income exemption or cancellation of RPC. [POAT Regulations 3](https://www.legislation.gov.fk/download/pdf/e2e89312-74e1-4d82-8239-426a6f92b3a1/a821bb28-ccc1-4cc7-9fc1-7561f30e2046/fisl-1997-23_2022-01-01.pdf#page=3). Check the separate domestic short-visit exemption in [fk-income-tax](fk-income-tax.md#the-base) before assuming annual tax.

POAT starts from remuneration including relevant bonuses, directors' fees and taxable non-cash emoluments. The pack records salary in box 5, benefits in 6 and non-cash emoluments in 7; box 8 totals those fields, boxes 9 and 10 identify employee pension and RPC deductions, box 11 is net taxable pay, box 12 POAT and box 13 employer RPC. The guide says the BIK column need not legally be included for monthly POAT, but benefits remain relevant to annual tax. Maintain the annual benefit schedule and report it on leaving/year end; use [fk-income-tax, prescribed benefits](fk-income-tax.md#prescribed-employment-benefits) for housing, vehicle, travel and loan valuations. Monthly BIK inclusion is not legally compulsory, but annual benefit taxation remains. Distinguish remuneration/non-cash emoluments under §8(1)(b). [Employer guide pp1-3](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf); [Workbook EMP-02 and Import Info](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2.-2026-Employer-Workbook.xlsx).

Resident main employers use the supplied Weekly or Monthly table on the appropriate tax base. After the low-hours and exemption tests, other employers and non-resident cases use the flat-rate rule stated above. Do not award the same allowance at two jobs. A net-of-tax contract requires grossing up, not merely multiplying the promised net cash by the tax rate. Obtain FIGTO directions for unusual gross-ups. [Employer guide p1](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf).

RPC counts liable weeks rather than charging a percentage of the whole salary. With multiple jobs, aggregate weekly earnings: the employer who first employs the person in the week starting Monday operates both employee and employer contributions. Below-limit cases may qualify for contribution credits or voluntary contributions. Self-employed people pay the full weekly amount for qualifying weeks and use RPC-02, not the employee EMP-02. Overseas voluntary payment requires eligibility and registration; it cannot cover time before first entry into the Islands. [Pensions Office](https://www.gov.fk/pensions/retirement-pension-scheme/); [Workbook EMP-02](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2.-2026-Employer-Workbook.xlsx).

## Deadlines and filing

1. Follow FIGTO's request to register a new business with employees within seven working days using the New Business Enquiry form. Independently, regulation 11B requires a new-business return by the next month's 14th stating whether or not anyone is employed; no-staff businesses are included. Notify staffing/deduction changes under regulation 12(3) by the next month's 14th. [Regulations 11B-12](https://www.legislation.gov.fk/download/pdf/e2e89312-74e1-4d82-8239-426a6f92b3a1/a821bb28-ccc1-4cc7-9fc1-7561f30e2046/fisl-1997-23_2022-01-01.pdf#page=10). Register new pension contributors through the Pensions Office. [FIGTO employers](https://www.gov.fk/taxation/employers/), [Pensions Office](https://www.gov.fk/pensions/retirement-pension-scheme/).
2. Notify each new employee on EMP-03 by the 14th of the following month, using their TIN and pension number. Agency/intermediary workers require EMP-03a and contract information 21 days before commencement. [Employer guide p1](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf).
3. Complete EMP-02/E-POAT for each period, starting at the first employee row and avoiding blank rows. Report all remuneration, including amounts with no deduction. Use the Tax Office's current electronic form in Excel format and authorise electronic submission where required. Its 2026 guide directs returns to taxreception@taxation.gov.fk. Do not alter protected formulas. [Guide pp1-2](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf), [Workbook](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2.-2026-Employer-Workbook.xlsx).
4. Submit the monthly POAT/RPC return, including nil returns, and pay by the 14th of the next month. The guide expressly says a Saturday 14th remains the deadline. Send EMP-02a remittance advice with the employer reference and period so Treasury allocates tax, employee RPC and employer RPC correctly. [Guide p2](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf).
5. Give EMP-04 to a leaver and FIGTO within seven days of employment ending; keep a copy. For an employee still employed at year end, give the certificate by 31 January following the year. Submit the annual employer return by 2 February following the income year, using that year's issued workbook. [Guide p2](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf), [FIGTO employers](https://www.gov.fk/taxation/employers/).
6. Self-employed people register and settle their own annual contributions with the Pensions Office. Obtain the applicable RPC-02 and payment demand; no unsupported annual due date is asserted. Reconcile pension records and tax certificates to every monthly payment. Regulation 13(5) requires deduction/payment records and employee identity to be kept six years after the end of the relevant calendar year.

## Penalties and interest

Regulation 12A imposes GBP 50 for each failure to deliver the new-business or monthly return. [Regulation 12A](https://www.legislation.gov.fk/download/pdf/e2e89312-74e1-4d82-8239-426a6f92b3a1/a821bb28-ccc1-4cc7-9fc1-7561f30e2046/fisl-1997-23_2022-01-01.pdf#page=11). The 2026 employer guide confirms GBP 50 for late monthly returns. It warns that late POAT can attract interest and a penalty equal to the unpaid POAT; statutory assessment/remission and offence provisions still control. [Guide p2](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf); [Taxes Ordinance Part IV, especially §96](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf). POAT interest is three percentage points above base lending rate under §87(7), separate from the debt. [§87](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf). The Pensions Office states that §15 of the Retirement Pensions Ordinance allows 5% annual interest on contribution debts more than one year in arrears. [Pensions Office, late contributions](https://www.gov.fk/pensions/retirement-pension-scheme/). No invented universal cap or automatic RPC refund is assumed.

## Cross-border points

Non-resident POAT does not itself establish final treaty liability. Use [fk-cross-border-tax](fk-cross-border-tax.md) for UK arrangement screening. Non-resident annual assessment may refund tax or charge extra; see [fk-income-tax](fk-income-tax.md). Defence work or employment at MPA alone does not prove a designated-employer exemption. Obtain evidence before withholding ceases. [FIGTO guide §§6-7](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/General-Tax-Guide-Individuals-2026.pdf).

## Two worked examples that recompute

**Resident monthly payroll.** Assume GBP 2,495.60 gross cash pay, no benefit/other pension adjustment, four liable RPC weeks and main-resident monthly treatment. Employee RPC is GBP 95.60, box 11 is exactly GBP 2,400. Workbook Monthly A52/B52 gives GBP 208.95 POAT and cash GBP 2,191.05; employer RPC is GBP 95.60. This is an exact published row, not an assumed interpolation rule.
```oa-check
name: Main employer monthly payroll
inputs:
  gross: 2495.60
  liable_weeks: 4
steps:
  employee_rpc: liable_weeks*23.90
  base: gross-employee_rpc
  poat: round(max(0,min(base-1405,1500))*0.21+max(0,base-2905)*0.26,2)
  net: gross-employee_rpc-poat
  employer_rpc: liable_weeks*23.90
expected:
  employee_rpc: 95.60
  poat: 208.95
  net: 2191.05
```

**Worker-status decision.** For assumed GBP 1,500 paid in a month with no RPC liability and no other taxable pay adjustment, the main-resident Monthly table gives GBP 19.95 POAT. A secondary-employer or non-resident flat-rate case gives GBP 315. The difference GBP 295.05 is withholding, not necessarily a difference in annual final tax. Select by actual facts, not by whichever leaves more cash.

```oa-check
name: Main resident table versus flat-rate withholding
inputs:
  gross: 1500
steps:
  main_poat: (gross-1405)*0.21
  flat_poat: gross*0.21
  difference: flat_poat-main_poat
expected:
  main_poat: 19.95
  flat_poat: 315
  difference: 295.05
```

## Ask the client first

- Employee, director, agency worker or genuine self-employed status and contract.
- Residence, main/secondary job and any approved exemption.
- Pay frequency, paid hours across all jobs for the current and prior periods, gross/non-cash remuneration and employer-paid tax.
- Age, pension number, liable weeks and earnings from all jobs.
- Employee pension deductions, leavers and starts.
- Filing references, electronic authority, previous return and payment reconciliations.

## Sources

| Source and text actually read | URL | Read on |
|---|---|---|
| Read for pp. 1-3: FIGTO 2026 employer guide, all three pages including forms and sanctions. “an automatic penalty of £50”; “on or before the 14th of the next month” | https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf | 2026-11-11 |
| Read for sections EMP-02, EMP-02a and table sheets: 2026 employer workbook, EMP-02, EMP-02a, EMP-03, EMP-03a, EMP-04, Monthly/Weekly/Flat Rate tables; inspected labels, cached values and formula cells. “Net Taxable sum for the month (Box 8 less boxes 9 & 10)” | https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2.-2026-Employer-Workbook.xlsx | 2026-11-11 |
| Read for p. 1: Pensions Office 2026 rate notice, complete single page, weekly values and month allocation. “Employer Contribution £23.90”; “Earnings Limit (Weekly) £386.40” | https://www.gov.fk/pensions/wp-content/uploads/sites/36/2026/06/RPC_Rates_2026_for_Circulation.pdf | 2026-11-11 |
| Read for sections on contribution liability: Pensions Office, contribution liability, registration, multiple jobs, self-employed, voluntary and late interest paragraphs | https://www.gov.fk/pensions/retirement-pension-scheme/ | 2026-11-11 |
| Read for sections on business registration: FIGTO employer page, business registration and annual deadline | https://www.gov.fk/taxation/employers/ | 2026-11-11 |
| Read for sections 5-6: FIGTO 2026 individual guide, §5 zero MST and §6 POAT | https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/General-Tax-Guide-Individuals-2026.pdf | 2026-11-11 |
| Read for Part IV: Taxes Ordinance, Part IV deduction/enforcement provisions | https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf | 2026-11-11 |
| Read for POAT Regulations, read for regulations 2-13, low-hours withholding, directions, registration, returns and retention. Regulation 11B: “whether or not any person is employed”; regulation 13: “6 years after the end of the calendar year” | https://www.legislation.gov.fk/download/pdf/e2e89312-74e1-4d82-8239-426a6f92b3a1/a821bb28-ccc1-4cc7-9fc1-7561f30e2046/fisl-1997-23_2022-01-01.pdf | 2026-11-11 |

Not yet confirmed: FIGTO's operational instruction for remuneration between published table rows and any applicable POAT direction; live self-employed RPC annual due-date notice; comprehensive defence/approved-pension exceptions. Do not extrapolate weekly allowances from annual figures or invent interpolation.
