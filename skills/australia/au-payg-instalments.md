---
name: au-payg-instalments
description: Use this skill whenever asked about Australian PAYG Instalments for sole traders. Trigger on phrases like "PAYG instalments", "BAS T1 T2 T7 T9", "instalment rate", "instalment amount", "ATO instalment", "GDP uplift", "GIC", "variation of instalments", or any question about income tax prepayments through the Business Activity Statement. Covers entry/exit thresholds, instalment rate method (T1/T2), instalment amount method (T7), GDP uplift factor, voluntary variation, GIC exposure on under-estimation, and quarterly/annual election. ALWAYS read this skill before touching any PAYG instalment work for Australia.
version: 2.4
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-22
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
---

# AU Payg Instalments

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Tax | PAYG income tax instalments (via BAS) |
| Primary legislation | TAA 1953 Sch 1 Div 45 |
| Authority | Australian Taxation Office (ATO) |
| Portal | Online services for business, or ATO online services through myGov for sole traders |
| Currency | AUD only |
| Entry thresholds | Instalment income of $4,000 or more, tax payable on the latest assessment of $1,000 or more, and notional tax of $500 or more (individuals and trusts) |
| Exit thresholds | Common automatic exit triggers are notional tax under $500, business and investment income under $4,000 for residents or $1 for non-residents, assessed tax debt under $1,000 after adjustment for instalments and voluntary payments, or a rate of 0.0%. See Section 8 for other triggers ([ATO Stopping PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments)) |
| Methods | Instalment rate (T1/T2/T11) or instalment amount (T7) |
| GDP adjustment factor | 5% for 2026-27 (6% in 2024-25); set each year and applied to the instalment amount method only |
| Variation threshold | A varied rate below 85% of the benchmark rate or an estimated benchmark tax below 85% of the actual benchmark tax can trigger shortfall GIC ([ATO vary PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments); [TAA Sch 1 ss 45-230, 45-232](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)) |
| GIC rate | Annualised base rate plus 7 percentage points. Divide by the number of days in the calendar year for the daily rate ([TAA s 8AAD](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO GIC](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge)) |
| Contributor | Open Accountants Community |
| Validation date | Pending |

**BAS label summary**

| Label | Description |
| --- | --- |
| T1 | Instalment income for the quarter |
| T2 | ATO-notified instalment rate or the last varied rate for the same income year |
| T3 | Varied instalment rate (rate method) |
| T4 | Reason code for variation |
| T8 | Estimated tax for the year (amount method variation) |
| T7 | ATO-notified instalment amount |
| T9 | Varied instalment amount (amount method) |
| T11 | Instalment payable under the rate method (T1 x T2, or T1 x T3 when varied) |
| 5A | PAYG income tax instalment |
| 5B | Credit from PAYG income tax instalment variation |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Method unclear | Check the ATO notice for the available methods and the method elected |
| Instalment income components uncertain | Start with gross assessable business and investment income and check the inclusions and exclusions in Section 5.2 |
| Variation considered | Check 85% safe harbour before varying |
| First year of business | Check for an existing PAYG instalment rate and ask whether the taxpayer opted in |
| Annual election eligibility | Check the $8,000 notional tax test and the GST conditions in Section 7. Confirm the choice by the first instalment's ordinary due date |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — ATO notification of instalment rate (T2) or instalment amount (T7), quarterly instalment income figure.
- **Recommended inputs** — prior year income tax assessment, BAS due dates, current year income projections if varying.
- **Ideal inputs** — complete ATO notification, prior year assessment, quarterly P&L, BAS history.
- **Refusal policy if minimum is missing** — SOFT WARN. Without the ATO notification, the instalment rate or amount cannot be confirmed.

### Refusal catalogue

- **R-AU-PI-1 -- Companies/trusts/partnerships** — Trigger: client is not a sole trader. Message: "This skill covers sole trader PAYG instalments only."
- **R-AU-PI-2 -- PAYG withholding** — Trigger: client asks about PAYG withholding (W labels). Message: "PAYG withholding is a separate obligation. See au-gst-bas."
- **R-AU-PI-3 -- GST computation** — Trigger: client asks about GST. Message: "GST computation is handled by the GST skill. This skill covers PAYG instalments only."

## Section 3 -- Payment pattern library

Use these descriptions as matching clues. Reconcile a debit to label 5A on the BAS or to a PAYG instalment notice before classifying the PAYG component.

### 3.1 ATO PAYG instalment debits

**ATO PAYG instalment debits pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO, AUSTRALIAN TAXATION OFFICE | Unallocated ATO payment | Match against the activity statement or instalment account |
| BAS PAYMENT, BAS DEBIT | Activity statement payment | Check which labels apply and split the payment |
| PAYG INSTALMENT, PAYG INST | Likely PAYG instalment | Reconcile to the relevant statement or notice |
| ATO DIRECT DEBIT | Unallocated ATO payment | Reconcile to the account before classifying |

### 3.2 Timing-based identification (quarterly BAS, standard)

**Timing-based identification table**

These are matching windows. The dates in the second column are ordinary deadlines for deferred BAS payers. Other quarterly payers generally use the 21st of the following month. Check the notice and any weekend, public holiday or deferral. For example, 28 February 2027 is a Sunday, so the ordinary deferred date moves to Monday 1 March if that day is a business day at the place of lodgment. [TAA Schedule 1 s 45-61](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) · [Acts Interpretation Act s 36(2)](https://www.legislation.gov.au/C1901A00002/2026-03-28/2026-03-28/text/original/epub/OEBPS/document_1/document_1.html)

| Debit date range | BAS quarter | Confidence |
| --- | --- | --- |
| 20 October -- 5 November | Q1 (Jul-Sep) due 28 Oct | High |
| 20 February -- 10 March | Q2 (Oct-Dec) due 28 Feb | High |
| 20 April -- 10 May | Q3 (Jan-Mar) due 28 Apr | High |
| 20 July -- 10 August | Q4 (Apr-Jun) due 28 Jul | High |

Note: BAS payments typically combine GST and PAYG amounts. The PAYG component is the T11, T9 or T7 figure within the BAS.

### 3.3 Related but NOT PAYG instalments

**Related but not PAYG instalments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO PAYG WITHHOLDING, W1-W5 | EXCLUDE | Employer withholding (separate) |
| ATO GST ONLY | EXCLUDE | GST-only payment |
| ATO SUPER, SUPER GUARANTEE | EXCLUDE | Superannuation guarantee |
| ATO PENALTY, ATO GIC | EXCLUDE | Penalty/interest |
| ATO REFUND | Flag for reviewer | Tax refund |
| ATO ACTIVITY STATEMENT | Activity statement payment | Check the BAS for the components actually reported |

### 3.4 BAS combined payment identification

A single BAS payment typically includes GST payable/refundable + PAYG instalment + PAYG withholding. To isolate the PAYG instalment component, the BAS form values (T7, T9 or T11) are needed.

## Section 4 -- Worked examples

### Example 1 -- Instalment rate method

Q1 business income = $42,000. Interest income = $800. ATO rate (T2) = 8.50%.

**BAS label value table**

| BAS label | Value |
| --- | --- |
| T1 (instalment income) | $42,800 |
| T2 (instalment rate) | 8.50% |
| T11 (instalment payable) | $3,638 |

```oa-check
name: AU PAYG instalment rate method Q1 calculation
inputs:
  business_income: 42000
  interest_income: 800
  rate_pct: 8.50
steps:
  - instalment_income: business_income + interest_income
  - instalment_payable: pct(instalment_income, rate_pct)
expected:
  instalment_income: 42800
  instalment_payable: 3638
```

### Example 2 -- Instalment amount method

Input: ATO-notified instalment amount (T7) = $3,150 per quarter.

Output: Report T7 = $3,150/quarter on BAS. Pay by BAS due date.

### Example 3 -- Variation of instalment rate

Input: ATO rate = 12%. A new forecast shows a lower profit margin and supports a varied rate of 8%.

Computation: T11 = T1 × 8%, dropping cents. Put the varied rate at T3 and the reason code at T4. The shortfall test compares 8% with 85% of the eventual benchmark instalment rate. The example needs that benchmark to determine exposure.

### Example 4 -- Below entry threshold

Input: Instalment income = $3,500. Notional tax = $800.

Output: Instalment income < $4,000, so these facts do not trigger automatic entry. Voluntary entry is available.

### Example 5 -- Bank statement classification

Input line: `28.10.2026 ; ATO ACTIVITY STATEMENT ; DEBIT ; BAS JUL-SEP 2026 ; -5,800.00 ; AUD`

Classification: $5,800 activity statement payment. Obtain the BAS and reconcile its 5A instalment and any 5B variation credit before allocating the payment.

## Section 5 -- Computation rules

### 5.1 Entry into PAYG instalment system

- **Automatic entry conditions** — An individual or trust enters automatically when the latest return shows instalment income of $4,000 or more, the notice of assessment shows tax payable of $1,000 or more, and notional tax is $500 or more. Voluntary entry is available below the thresholds. Instalment income is gross business and investment income excluding GST and capital gains.  _([ATO, Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments))_
- **Method choice** — The ATO notifies an instalment amount, an instalment rate, or a choice between them. When a choice is offered, the method selected on the first activity statement applies for the rest of that income year. The notified figures come from the latest return with the ATO's adjustments; use the notice, not a historical uplift percentage.  _([ATO, Calculate your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments))_

### 5.2 Instalment rate method (T1/T2/T11)

- **Instalment rate method formula**. T1 is quarterly instalment income. T2 is the notified rate or the last variation for the year. The statutory rate starts with notional tax ÷ base assessment instalment income × 100, rounded to 2 decimal places. The ATO publishes 55% as its reasonable rate for affected individuals. Multiply T1 by T2, or by T3 if varying in this period, and drop cents when reporting T11 and 5A. The GDP adjustment applies only to the amount method. [TAA Schedule 1 ss 45-110, 45-320](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) · [ATO activity statement instructions](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement)
- **What counts as instalment income**. Use gross assessable business and investment income for the period, excluding GST collected, exempt income and net capital gains for a sole trader. Ordinary business deductions do not reduce T1. Exclude PAYG withholding payments, with an exception for payments withheld for failure to quote a TFN or ABN. Apply any farm management deposit adjustment and account for qualifying partnership or trust instalment income. Include any taxable net capital gain in the final income tax cash forecast. [TAA Schedule 1 s 45-120 and Subdivisions 45-H and 45-I](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) · [ATO instalment income](https://www.ato.gov.au/Business/PAYG-instalments/Calculate-your-PAYG-instalments/Instalment-income/)
- **Zero instalment rate** — If the notified rate is zero, still report instalment income at T1 and retain the statement and the reconciliation behind it.

### 5.3 Instalment amount method (T7)

- **Instalment amount method**. Use the amount notified at T7. Under s 45-405 the ATO increases base-year adjusted taxable income and adjusted withholding income, if any, by the GDP factor before recalculating notional tax. Under s 45-400 the four-instalment method uses cumulative targets of 25%, 50%, 75% and 100% of that recalculated tax, less earlier instalments as applicable. The taxpayer can use the prefilled amount without calculating quarterly instalment income. [TAA Schedule 1 ss 45-112, 45-400 and 45-405](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)

### 5.4 GDP adjustment factor

- **GDP adjustment factor 2026-27**. The factor is 5%, with application from 1 July for a standard income year and for substituted income years starting from 1 April 2026. Substituted years beginning January through March 2026 keep the 2025-26 factor of 4%. The 2024-25 factor was 6%. The factor derives from ABS data or a statutory override. It applies to the quarterly and twice-yearly amount methods. [ATO 2026-27 GDP adjustment](https://softwaredevelopers.ato.gov.au/GDPupliftfactor) · [ATO 2024-25 GDP adjustment](https://softwaredevelopers.ato.gov.au/gdp-adjustment-2024-25-gst-and-payg-instalments)

### 5.5 Variation

- **Variation rule**. Enter the varied rate at T3, or the estimated tax at T8 and varied amount at T9. Use a reason code at T4 for either method. For the rate method, compare the varied rate with 85% of the year's benchmark instalment rate under s 45-230. For the amount method, compare the estimated benchmark tax with 85% of the year's benchmark tax under s 45-232. Work out GIC on the statutory shortfall for the relevant period. [TAA Schedule 1 ss 45-230 and 45-232](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)
- **Varied rate formula** — Varied rate = estimated annual tax on instalment income divided by estimated annual instalment income, multiplied by 100. Apply the varied percentage to actual instalment income for the period. If estimated annual instalment income is zero, the rate or amount can be varied to zero without estimating tax. Select the reason code that matches the circumstances.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Varying the instalment amount**. The targets under s 45-410 are 25%, 50%, 75% and 100% of estimated benchmark tax. Count from the first quarter for which an instalment is owing that year. Subtract the earlier instalments and, for the third and fourth quarters, add the earlier s 45-420 credits to which the taxpayer was entitled. A negative result gives a nil instalment at T9 and 5A. Claim the resulting credit as a positive amount at 5B by the instalment due date if choosing to claim it. For an established twice-yearly payer with a standard income year, the first instalment is generally 75% in April with the balance in July. Apply the separate part-year entry rules in ss 45-402 and 45-412 if the taxpayer first receives a rate later in the year. [TAA Schedule 1 ss 45-402, 45-410, 45-412 and 45-420](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)
- **Estimate the whole year, not turnover times a rate** — A variation changes prepayments without changing the final liability. Estimate the tax attributable to instalment income from a current full-year forecast that includes other income, deductions and offsets. Under the rate method the instalment already rises and falls with income; a changed profit margin can justify a variation, a temporary cash shortage does not. If payment is difficult, lodge the statement and discuss a payment arrangement with the ATO.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Timing and records** — Lodge the variation on or before the instalment due date and before the income tax return for that year is lodged; it applies to the remaining instalments until another variation or the end of the year. Keep the forecast, assumptions, calculation, reason code and lodged statement, review the forecast when conditions change, and match instalment credits on the assessment to the instalment account before treating an expected credit as cash.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

### 5.6 Year-end credit

- **Year-end credit rule**. The assessment credit is the total instalments payable for the year, including unpaid instalments, less variation credits claimed. Unpaid instalments remain payable. Any resulting overpayment is refunded or offset, and any remaining assessed tax is payable. [TAA Schedule 1 s 45-30](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)

## Section 6 -- Penalties and interest

### 6.1 General Interest Charge (GIC)

- **GIC rate**. Add 7 percentage points to the quarterly base rate using the relevant monthly average yield of 90-day Bank Accepted Bills. Divide by the calendar year's number of days for the daily rate. Shortfall GIC under ss 45-230 and 45-232 generally runs from the variation instalment's due day through the assessed tax due day. [TAA s 8AAD](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [TAA Schedule 1 ss 45-230 and 45-232](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)
- **GIC and SIC deductions**. Deduction denial applies to assessments for income years starting on or after 1 July 2025, including where the underlying debt is older. Apply the start date to any substituted accounting period. A later remission of non-deductible interest is excluded from assessable recoupments. [Treasury Laws Amendment (Tax Incentives and Integrity) Act 2025 Schedule 2](https://www.legislation.gov.au/C2025A00029/asmade/2025-03-27/text/original/pdf) · [ATO interest deductions](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/deny-deductions-for-ato-interest-charges)

### 6.2 Late BAS lodgement penalty

- **Late BAS lodgment penalty**. The base penalty is 1 unit for each 28-day period or part, up to 5 units. The penalty unit is $364 a unit from 1 July 2026, giving a base maximum of $1,820. It was $330 from 7 November 2024 to 30 June 2026. Multipliers of 2 or 5 can apply under the medium or large withholder, assessable income or GST turnover tests. Check the registered-agent exception where applicable. [ATO penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) · [ATO failure to lodge penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty)

### 6.3 Safe harbour

- Meeting the relevant 85% threshold in Section 5.5 avoids GIC on that variation shortfall. Other charges can still apply.
- If the rate fails the test, s 45-230 uses the difference between the varied rate and the lower of the ATO rate and benchmark rate, multiplied by the quarter's instalment income, plus any statutory credit adjustment. For the amount method, s 45-232 uses the positive difference between the statutory acceptable amount and the actual amount. Section 45-240 provides for remission in special circumstances. [TAA Schedule 1 ss 45-230, 45-232 and 45-240](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)

## Section 7 -- Annual instalment election

- **Annual election eligibility and effect**. The latest notified notional tax must be under $8,000. Check the individual's and any partnership's GST registration and annual tax period elections under s 45-140. Make the election in approved form by the first instalment's ordinary due date. For a deferred BAS payer that usually means the 28th of the following month, or 28 February where December is in the last month of that quarter. The ATO requests the choice before lodging the first quarterly statement. For a standard year, a self-preparer following the ATO annual process lodges the return by 31 October without a separate instalment. An agent client generally pays by 21 October before the return is lodged. If the return goes in first, the ATO instructs the client to pay the notice by 21 October and leave it unlodged and unvaried. [TAA Schedule 1 ss 45-61, 45-70 and 45-140](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) · [ATO PAYG due dates](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due)

## Section 8 -- Edge cases

A new sole trader may already be in PAYG instalments through earlier investment income or may opt in before their first business assessment. Check for an instalment rate that remains in force. [TAA Schedule 1 s 45-50(4)](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) · [ATO, Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments)

Instalment rate method auto-adjusts. If using amount method, consider variation in low-income quarters.

Instalment income = total across all activities. Single rate applies to aggregate.

Interest, dividends, rent are instalment income. Employees with significant investment income may enter PAYG system.

The ATO-notified rate accounts for Medicare levy where payable. The ordinary levy rate is 2%, subject to reductions and exemptions. The calculation excludes Medicare levy surcharge. Use the notified rate for the instalment and forecast any applicable surcharge separately for the income tax assessment. [TAA Schedule 1 s 45-340 step 2](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) · [Medicare Levy Act s 6](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html)

The ATO removes individuals automatically under the triggers in Section 1 and in some other cases, including eligibility for the seniors and pensioners tax offset, Division 6AA income below the threshold for a person under 18, or a final return or non-lodgment notice. A taxpayer who has stopped earning business or investment income can also ask to exit. Check the rate withdrawal and the date the ATO gives. [ATO, Stopping PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments)

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Entry thresholds checked ($4,000 instalment income, $1,000 tax payable, $500 notional tax)
- [ ] Correct method identified (rate vs amount)
- [ ] T1 includes only correct components (no salary, no CGT, no GST)
- [ ] T2 matches ATO notification or is validly varied
- [ ] 85% safe harbour checked if variation applied
- [ ] GDP adjustment factor current (5% for 2026-27)
- [ ] BAS due dates correct
- [ ] Year-end credit against annual assessment noted
- [ ] First-year exception flagged if applicable
- [ ] Output labelled as estimated until Australian CPA/CA confirms

### Test 1 -- Instalment rate method

Input: T1 = $42,800. T2 = 8.50%.
Expected: T11 = $3,638.

### Test 2 -- Instalment amount method

Input: 2025-26 base-year adjusted taxable income is $60,000 for a full-year resident with no withholding income, education debt or applicable offsets. Full Medicare levy applies. The first 2026-27 instalment uses a 5% GDP adjustment.

Expected: Adjusted income is $60,000 × 1.05 = $63,000. Using the 2025-26 base-year rates, income tax is $4,288 + 30% × ($63,000 − $45,000) = $9,688. The 2% Medicare levy is $1,260. GDP-adjusted notional tax is $10,948 and the first instalment is 25% × $10,948 = $2,737. [ATO resident rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents) · [TAA Schedule 1 ss 45-340, 45-400 and 45-405](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html)

### Test 3 -- Below entry threshold

Input: Instalment income = $3,500.
Expected: No automatic entry. Check any earlier rate or voluntary registration.

### Test 4 -- Variation with safe harbour check

Input: ATO rate 12%. Varied to 8%. Benchmark rate 10%. Instalment income for this quarter is $10,000. No variation credit was claimed.

Expected: The threshold is 85% × 10% = 8.5%. The varied rate of 8% falls below it. The lower of 12% and 10% is 10%, so the discrepancy is 2 percentage points. GIC applies to $10,000 × 2% = $200 before any remission.

```oa-check
name: AU PAYG instalment variation safe harbour 85% check
inputs:
  ato_rate_pct: 12
  varied_rate_pct: 8
  benchmark_rate_pct: 10
  instalment_income: 10000
steps:
  - safe_harbour_pct: pct(benchmark_rate_pct, 85)
  - comparison_rate_pct: min(ato_rate_pct, benchmark_rate_pct)
  - discrepancy_pct: comparison_rate_pct - varied_rate_pct
  - gic_base_amount: pct(instalment_income, discrepancy_pct)
expected:
  safe_harbour_pct: 8.5
  comparison_rate_pct: 10
  discrepancy_pct: 2
  gic_base_amount: 200
```

### Test 5 -- First year

Input: New sole trader with no instalment rate in force and no voluntary registration.
Expected: No PAYG instalments until the Commissioner gives an instalment rate. Allow for the final income tax liability in the cash forecast.

### Test 6 -- Year-end credit (overpayment)

Input: Instalments totalling $15,000 became payable and were paid. No variation credits were claimed. The assessed tax is $12,000.
Expected: $15,000 credit less $12,000 assessed tax gives $3,000 refunded or offset.

## Prohibitions

- Apply the instalment income inclusions and exclusions in Section 5.2
- NEVER vary the instalment rate or amount without checking the 85% safe harbour
- NEVER assume the first year of business requires PAYG instalments
- Apply the GDP adjustment to the statutory base-year income figures when checking T7
- NEVER conflate PAYG instalments (T labels) with PAYG withholding (W labels)
- NEVER present instalment figures as definitive -- the ATO notification is authoritative

## Sources

- [ATO, Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments) and [Stopping PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments) (read 2026-11-22)
- [ATO, Calculate your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments) and [How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments) (read 2026-11-22)
- [ATO, 2026-27 GDP adjustment](https://softwaredevelopers.ato.gov.au/GDPupliftfactor) and [2024-25 GDP adjustment](https://softwaredevelopers.ato.gov.au/gdp-adjustment-2024-25-gst-and-payg-instalments) (read 2026-11-22)
- [TAA 1953 Schedule 1, Division 45](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) and [s 8AAD GIC](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) (read 2026-11-22)
- [ATO penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units), [failure to lodge penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty) and [general interest charge](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge) (read 2026-11-22)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
