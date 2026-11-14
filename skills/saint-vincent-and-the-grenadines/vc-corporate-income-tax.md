---
name: vc-corporate-income-tax
description: >
  Saint Vincent and the Grenadines company income tax for 2026. Covers the 28% rate on
  chargeable income set by the Finance Act 10 of 2023, the return and final tax three
  months after the financial year end, estimated tax in four instalments (one quarter
  each by the end of months six, nine and twelve, the balance three months after year
  end), the EC$600 instalment exemption, the short-year rule, 1.5% monthly interest, and
  the withholding rates on payments to nonresidents. Trigger phrases include SVG
  corporate tax, St Vincent company tax 28%, SVG estimated tax instalments.
version: 1.0
jurisdiction: VC
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: corporate-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Vincent and the Grenadines company income tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Company income tax in Saint Vincent and the Grenadines (SVG) for years of assessment in 2026, under the Income Tax Act, Cap. 435, as amended by the Finance Act 10 of 2023, and the Inland Revenue Department (IRD) guidance. Covers the rate, return, estimated tax and interest once chargeable income is known. Amounts are EC$. Residence, deductions, capital allowances, losses, incentives, special sectors and treaties are outside it. VAT: [vc-vat](vc-vat.md).

## Ask the client first

1. Financial year end; whether the company was assessed for the preceding year, and that year's length.
2. Chargeable income for the preceding assessed year and the expected chargeable income now.
3. Accounting profit and the adjustments to reach chargeable income, each with its authority.
4. Instalments paid, withholding credits, and any payments to nonresidents.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Company rate | 28% on every dollar of chargeable income (Fifth Schedule item 2, replacing 30%) | [Finance Act 10 of 2023, Schedule item 8(b)](https://finance.gov.vc/finance/images/PDF/Acts/Finance_Act_No_10_of_2023_30_to_28_tax_rate_001.pdf) |
| Return and final tax | Three months after the financial year ends | [IRD taxes page](https://ird.gov.vc/index.php/taxes) |
| Estimated tax base, s.70(2) | Tax at current rates on the preceding (or latest assessed) year's chargeable income; expected income if never assessed; a short preceding year is grossed up by 365 / days | [Income Tax Act Cap. 435, s.70](https://ird.gov.vc/images/pdf/Cap435.pdf) |
| Instalments 1 to 3, s.71 | One quarter of estimated tax each, by the end of the 6th, 9th and 12th months of the year | [Income Tax Act Cap. 435, s.71](https://ird.gov.vc/images/pdf/Cap435.pdf) |
| Instalment 4, s.71 | The balance of tax for the year, by the end of the 3rd month after year end | same |
| Instalment exemption, s.72 | None required where tax chargeable, after tax deducted at source, is EC$600 or less | [Income Tax Act Cap. 435, s.72](https://ird.gov.vc/images/pdf/Cap435.pdf) |
| Revision of the estimate, s.73 | Application by 30 November in the income year | same |
| Interest | 1.5% a month | [IRD taxes page](https://ird.gov.vc/index.php/taxes) |
| Withholding on services by nonresidents | 20%; rental 10%; CARICOM royalties, interest and management fees 15%; remit by the 15th of the next month | same |

### Steps

1. **Bridge** accounting profit to chargeable income; record the authority for each adjustment.
2. **Tax:** chargeable income x 28%.
3. **Estimated tax:** prior-year chargeable income x 28% (grossed up for a short year), or expected income if never assessed. If the tax is EC$600 or less, no instalments.
4. **Pay** a quarter of the estimate by the end of months 6, 9 and 12, and the balance with the return three months after year end.
5. **Credits:** subtract instalments and tax withheld at source.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Final tax above the estimate | The fourth payment is the balance, not a fourth quarter | [Cap. 435, s.71(2)(b)](https://ird.gov.vc/images/pdf/Cap435.pdf) |
| Preceding year of 200 days | Gross up: chargeable income x 365 / 200 | [Cap. 435, s.70(2)(c)](https://ird.gov.vc/images/pdf/Cap435.pdf) |
| Old 30% rate in the consolidated Act | Replaced by 28% (Finance Act 2023, embodying the Provisional Collection of Taxes Order 8 of 2023) | [Finance Act 10 of 2023](https://finance.gov.vc/finance/images/PDF/Acts/Finance_Act_No_10_of_2023_30_to_28_tax_rate_001.pdf) |
| Paying a nonresident for services | Withhold 20% and remit by the 15th | [IRD taxes page](https://ird.gov.vc/index.php/taxes) |

## Worked cases

### Case 1: calendar-year company

Last year's chargeable income gives an estimate of 28,000; this year's chargeable income is 125,000, tax 35,000. Instalments of 7,000 are due at the end of June, September and December, and the balance of 14,000 by the end of March 2027.

```oa-check
name: SVG company tax and instalments, estimate 28,000, final 35,000
inputs:
  chargeable: 125000
  estimate: 28000
steps:
  - tax: chargeable * 0.28
  - quarter: estimate / 4
  - paid_in_year: quarter * 3
  - balance: tax - paid_in_year
expected:
  tax: 35000
  quarter: 7000
  paid_in_year: 21000
  balance: 14000
```

### Case 2 (decision): short preceding year, what estimate?

The company's first year was 200 days with chargeable income of 50,000. The statutory estimate grosses up: 50,000 x 365 / 200 = 91,250, tax 25,550, instalments 6,387.50. Using the unadjusted 50,000 would give 14,000 and instalments of 3,500, short by 2,887.50 each. If a lower expected income is real, apply for revision by 30 November.

```oa-check
name: SVG estimated tax after a 200-day first year
inputs:
  prior_income: 50000
  days: 200
steps:
  - grossed: prior_income * 365 / days
  - estimate: grossed * 0.28
  - quarter: estimate / 4
  - wrong_quarter: prior_income * 0.28 / 4
  - shortfall: quarter - wrong_quarter
expected:
  grossed: 91250
  estimate: 25550
  quarter: 6387.5
  wrong_quarter: 3500
  shortfall: 2887.5
```

## When to refuse or refer

- Residence and source, special sectors, incentives, losses, capital allowances.
- Treaties and cross-border structuring beyond the IRD withholding rates.
- Penalty amounts: the IRD page names penalties without amounts.

## Filing and payment

1. File the company return with the final tax three months after year end ([IRD taxes page](https://ird.gov.vc/index.php/taxes)).
2. Pay estimated tax under ss.70 and 71; apply by 30 November to revise the estimate.
3. Reconcile the computation to the accounts and the payment ledger; list withholding credits separately.

## Completion checklist

- Chargeable income bridged; 28% applied.
- Estimate on the s.70(2) basis; EC$600 exemption checked.
- Quarters by months 6, 9, 12; balance three months after year end.

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 10 of 2023 (scanned, OCR): read for Schedule item 8(b), the Fifth Schedule company rate 30% to 28% and the individual band change, and the Provisional Collection of Taxes Order 8 of 2023 | https://finance.gov.vc/finance/images/PDF/Acts/Finance_Act_No_10_of_2023_30_to_28_tax_rate_001.pdf | 2026-11-14 |
| IRD taxes page: read for the 28% rate, the return and payment three months after year end, 1.5% monthly interest and the withholding tax rates | https://ird.gov.vc/index.php/taxes | 2026-11-14 |
| Income Tax Act Cap. 435 (IRD PDF): read for ss.70 to 73, estimated tax, instalments, the EC$600 exemption and revision | https://ird.gov.vc/images/pdf/Cap435.pdf | 2026-11-14 |

Not yet confirmed: amendments to ss.70 to 73 after the consolidation; penalty amounts; the Tax Administration Act rules on interest and penalties (not opened).
