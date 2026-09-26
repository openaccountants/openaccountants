---
name: au-payg-instalments
description: Use this skill whenever asked about Australian PAYG Instalments for sole traders. Trigger on phrases like "PAYG instalments", "BAS T1 T2 T7 T9", "instalment rate", "instalment amount", "ATO instalment", "GDP uplift", "GIC", "variation of instalments", or any question about income tax prepayments through the Business Activity Statement. Covers entry/exit thresholds, instalment rate method (T1/T2), instalment amount method (T7), GDP uplift factor, voluntary variation, GIC exposure on under-estimation, and quarterly/annual election. ALWAYS read this skill before touching any PAYG instalment work for Australia.
version: 2.2
jurisdiction: AU
tax_year: 2025
last_updated: 2026-09-26
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
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
| Portal | ATO Business Portal / myGov |
| Currency | AUD only |
| Entry thresholds | Instalment income >= $4,000 AND notional tax >= $1,000 |
| Exit threshold | Notional tax < $500 |
| Methods | Instalment rate (T1/T2/T11) or instalment amount (T7) |
| GDP uplift factor | 6% (2024-25, subject to annual determination) |
| Variation safe harbour | 85% of correct instalment amount |
| GIC rate | Base rate + 7% (updated quarterly) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Australian CPA/CA |
| Validation date | Pending |

**BAS label summary**

| Label | Description |
| --- | --- |
| T1 | Instalment income for the quarter |
| T2 | ATO-notified instalment rate |
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
| Method unclear | Check ATO notification -- they determine the method |
| Instalment income components uncertain | Include all business + investment income; exclude salary, CGT, exempt |
| Variation considered | Check 85% safe harbour before varying |
| First year of business | No instalments until first assessment |
| Annual election eligibility | Instalment income < $2M and GST turnover < $2M |

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

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a PAYG instalment payment.

### 3.1 ATO PAYG instalment debits

**ATO PAYG instalment debits pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO, AUSTRALIAN TAXATION OFFICE | PAYG instalment | Match with BAS quarterly timing |
| BAS PAYMENT, BAS DEBIT | PAYG instalment (combined with GST) | BAS payment includes both GST and PAYG |
| PAYG INSTALMENT, PAYG INST | PAYG instalment | Explicit description |
| ATO DIRECT DEBIT | PAYG instalment | Automatic payment |

### 3.2 Timing-based identification (quarterly BAS, standard)

**Timing-based identification table**

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
| ATO ACTIVITY STATEMENT | Combined payment | Includes GST + PAYG -- split for classification |

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

### Example 2 -- Instalment amount method

Input: ATO-notified instalment amount (T7) = $3,180 per quarter.

Output: Report T7 = $3,180 on BAS. Pay by BAS due date.

### Example 3 -- Variation of instalment rate

Input: ATO rate = 12%. Taxpayer estimates current year rate should be 8% (income dropped). Varied rate = 8%.

Computation: T11 = T1 x 8%, with the varied rate at T3 and the reason code at T4. Check: total varied instalments must be >= 85% of correct instalment (based on actual year-end assessment). If not, GIC applies.

### Example 4 -- Below entry threshold

Input: Instalment income = $3,500. Notional tax = $800.

Output: Instalment income < $4,000. Not entered into PAYG instalment system.

### Example 5 -- Bank statement classification

Input line: `28.10.2024 ; ATO ACTIVITY STATEMENT ; DEBIT ; BAS JUL-SEP 2024 ; -5,800.00 ; AUD`

Classification: Combined BAS payment (GST + PAYG). PAYG instalment component = T7, T9 or T11 from the BAS. Flag for reviewer to split.

## Section 5 -- Computation rules

### 5.1 Entry into PAYG instalment system

- **Automatic entry conditions** — Automatic entry if most recent assessment shows: Instalment income >= $4,000, AND Notional tax >= $1,000. Voluntary entry available below thresholds.
- **Method choice** — The ATO notifies an instalment amount, an instalment rate, or a choice between them. When a choice is offered, the method selected on the first activity statement applies for the rest of that income year. The notified figures come from the latest return with the ATO's adjustments; use the notice, not a historical uplift percentage.  _([ATO, Calculate your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments))_

### 5.2 Instalment rate method (T1/T2/T11)

- **Instalment rate method formula** — T1 = quarterly instalment income (business + investment, excl. salary/CGT/GST) T2 = ATO-notified rate (prior year notional tax / instalment income x GDP uplift) T11 = T1 x T2 (rounded to whole dollars)
- **What counts as instalment income** — Instalment income is gross business and investment income for the period, excluding GST. It is not net profit, so business deductions do not reduce T1. Salary subject to PAYG withholding and net capital gains are excluded, but a capital gain still creates a final income tax liability, so include it in the whole-year cash forecast. Review unusual receipts against the ATO definition.  _([ATO, Calculate your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments))_
- **Zero instalment rate** — If the notified rate is zero, still report instalment income at T1 and retain the statement and the reconciliation behind it.

### 5.3 Instalment amount method (T7)

- **Instalment amount method formula** — T7 = (prior year notional tax / 4) x GDP uplift factor

No income calculation needed. ATO pre-fills the amount.

### 5.4 GDP uplift factor

- **GDP uplift factor 2024-25** — 6%  _(Applied by ATO when calculating T2 and T7. Updated annually.)_

### 5.5 Variation

- **Variation rule** — A taxpayer varies the rate by entering the new rate at T3, or the amount by entering estimated annual tax at T8 and the varied amount at T9, with a reason code at T4 in either case. If total varied instalments < 85% of the benchmark (correct instalment based on actual assessment), GIC applies from each instalment due date.
- **Varied rate formula** — Varied rate = estimated annual tax on instalment income divided by estimated annual instalment income, multiplied by 100. Apply the varied percentage to actual instalment income for the period. If estimated annual instalment income is zero, the rate or amount can be varied to zero without estimating tax. Select the reason code that matches the circumstances.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Varying the instalment amount** — For quarterly amount instalments the cumulative targets are 25%, 50%, 75% and 100% of estimated annual tax: work out the target for the quarter, deduct earlier instalments and add back any earlier variation credits. A taxpayer who enters the system part-way through the year treats their first instalment quarter as the first quarter. If the result is negative, report zero at T9 and 5A and claim any credit for earlier instalments as a positive amount at 5B; claiming it is optional because instalments are reconciled through the annual assessment. Twice-yearly payers pay 75% in April and the balance in July.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Estimate the whole year, not turnover times a rate** — A variation changes prepayments without changing the final liability. Estimate the tax attributable to instalment income from a current full-year forecast that includes other income, deductions and offsets. Under the rate method the instalment already rises and falls with income; a changed profit margin can justify a variation, a temporary cash shortage does not. If payment is difficult, lodge the statement and discuss a payment arrangement with the ATO.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Timing and records** — Lodge the variation on or before the instalment due date and before the income tax return for that year is lodged; it applies to the remaining instalments until another variation or the end of the year. Keep the forecast, assumptions, calculation, reason code and lodged statement, review the forecast when conditions change, and match instalment credits on the assessment to the instalment account before treating an expected credit as cash.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

### 5.6 Year-end credit

- **Year-end credit rule** — Total PAYG instalments credited against annual income tax assessment. Overpayment: refund or offset. Underpayment: balance due with assessment.

## Section 6 -- Penalties and interest

### 6.1 General Interest Charge (GIC)

- **GIC rate** — base rate (90-day bank bill rate) + 7%  _(Updated quarterly. Applies from instalment due date if variation results in < 85% of correct amount.)_

### 6.2 Late BAS lodgement penalty

- **Late BAS lodgement penalty** — $313 per 28-day period, up to 5 periods ($1,565 max for small entities)  _(Failure to lodge BAS)_

### 6.3 Safe harbour

- **Safe harbour rule** — If varied instalments total >= 85% of the benchmark instalment, no GIC.
- **85% is a floor, not a target** — Where varied instalments fall below 85% of the tax payable on instalment income, general interest charge applies to the difference and penalties can follow. The figure is not licence to understate tax deliberately, and it does not remove other interest charges.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

## Section 7 -- Annual instalment election

- **Annual election eligibility and effect** — Taxpayers with instalment income < $2M and GST turnover < $2M may elect to lodge and pay annually instead of quarterly. This aligns the PAYG instalment with the annual income tax assessment.

## Section 8 -- Edge cases

Not entered into PAYG system until after first assessment. No instalments in Year 1. Tax shock in Year 2. Flag for reviewer.

Instalment rate method auto-adjusts. If using amount method, consider variation in low-income quarters.

Instalment income = total across all activities. Single rate applies to aggregate.

Interest, dividends, rent are instalment income. Employees with significant investment income may enter PAYG system.

ATO-notified rate already includes Medicare levy (2%) and any surcharge. No separate adjustment needed.

Apply if notional tax drops below $500 or instalment income ceases.

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Entry thresholds checked ($4,000 instalment income + $1,000 notional tax)
- [ ] Correct method identified (rate vs amount)
- [ ] T1 includes only correct components (no salary, no CGT, no GST)
- [ ] T2 matches ATO notification or is validly varied
- [ ] 85% safe harbour checked if variation applied
- [ ] GDP uplift factor current
- [ ] BAS due dates correct
- [ ] Year-end credit against annual assessment noted
- [ ] First-year exception flagged if applicable
- [ ] Output labelled as estimated until Australian CPA/CA confirms

### Test 1 -- Instalment rate method

Input: T1 = $42,800. T2 = 8.50%.
Expected: T11 = $3,638.

### Test 2 -- Instalment amount method

Input: Prior year notional tax = $12,000. GDP uplift = 6%.
Expected: Annual = $12,720. T7 = $3,180/quarter.

### Test 3 -- Below entry threshold

Input: Instalment income = $3,500.
Expected: Not entered into system.

### Test 4 -- Variation with safe harbour check

Input: ATO rate 12%. Varied to 8%. Actual correct rate = 10%.
Expected: Varied total = 80% of correct. Below 85%. GIC applies.

### Test 5 -- First year

Input: New sole trader, no prior assessment.
Expected: No instalments. Flag Year 2 tax shock risk.

### Test 6 -- Year-end credit (overpayment)

Input: Total instalments paid = $15,000. Actual tax = $12,000.
Expected: $3,000 overpayment refunded or offset.

## Prohibitions

- NEVER include salary, net capital gains, or GST in instalment income (T1)
- NEVER vary the instalment rate or amount without checking the 85% safe harbour
- NEVER assume the first year of business requires PAYG instalments
- NEVER ignore the GDP uplift factor when computing T7 or verifying T2
- NEVER conflate PAYG instalments (T labels) with PAYG withholding (W labels)
- NEVER present instalment figures as definitive -- the ATO notification is authoritative

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
