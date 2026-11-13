---
name: mt-corporate-tax
description: Prepare the Montana 2026 C-corporation income tax working paper and Form CIT filing. Covers ordinary tax, the minimum, single receipts factor, alternative gross sales eligibility and water's edge election boundaries. Trigger on Montana CIT or Montana corporate tax.
jurisdiction: US-MT
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
version: "1.1"
type: situation-rules
---

# Montana corporate income tax, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Montana taxes a C corporation's Montana taxable income at 6.75%, generally at least $50; a valid water's edge election uses 7%. The receipts-only alternative is 0.5% of Montana gross sales if all statutory conditions hold.

## Scope and who this is for

C corporations and LLCs taxed federally as C corporations doing business in Montana. S corporations use Form PTE; sole proprietors use `mt-income-tax`. Federal corporate tax belongs in `us-form-1120-c-corp`. 2026 rates are current DOR rules; detailed form references below use the verified **2025-2026 filing cycle** instructions and must be remapped to the eventual 2026 form.

## Ask the client first

1. What are the entity classification, fiscal-year dates, Montana activities and nexus/protection facts?
2. What is the federal corporate taxable income before federal NOL and special deductions, with a complete federal return?
3. What state modifications, separate Montana losses, credits and payment history exist?
4. What Montana and everywhere receipts, allocable income, affiliates and ownership changes must be analyzed?
5. Is there a valid water's edge election, or only sales activity with no Montana owned/rented real or tangible property and gross Montana sales at most $100,000?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| Ordinary corporate tax | 6.75% | [MCA 15-31-121, DOR](https://revenue.mt.gov/taxes/corporate-income-tax) |
| Minimum, ordinary return | $50 per corporation with Montana activity | [printed pp.1-2, 7](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf) |
| Valid water's edge election | 7% | [MCA 15-31-322, DOR](https://revenue.mt.gov/taxes/corporate-income-tax) |
| Alternative gross-sales election | 0.5%; only sales, no Montana real/tangible property owned or rented, Montana gross sales <= $100,000 | [MCA 15-31-122, DOR](https://revenue.mt.gov/taxes/corporate-income-tax) |
| Estimated payment threshold | Expected tax at least $5,000 | [official text](https://revenue.mt.gov/taxes/corporate-income-tax) |
| Automatic e-file exemption | Gross receipts <= $750,000; otherwise approved software or CWR waiver | [official text](https://revenue.mt.gov/taxes/corporate-income-tax) |
| Apportionment, tax years after 2024 | Single receipts factor | [official text](https://revenue.mt.gov/taxes/corporate-income-tax) |

1. Establish the federal filing classification and whether Montana business activity requires Form CIT. An LLC label does not decide the tax return. Montana tax exemption requires its own recognition; federal exemption alone is insufficient. Sources: [printed pp.1-2](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf).
2. Start with federal Form 1120 taxable income before federal NOL and special deductions (the verified 2025 CIT instructions identify federal line 28). Montana additions include deducted state/local/foreign income taxes, federal exempt interest and the appropriate combined-group adjustments. Reductions include Montana-permitted dividends, nonapportionable income removed before allocation and other state deductions. Keep a reconciliation by adjustment. Sources: [printed pp.5-6](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf).
3. For all-Montana activity, use the adjusted state base. For multistate income, separate directly allocable income and apply the current single receipts factor to apportionable income, then add Montana allocated income. The old double-weighted receipts formula ended for years beginning after 2024. Use Schedule K and the applicable sourcing rules, not the address of incorporation. Source: [apportionment section](https://revenue.mt.gov/taxes/corporate-income-tax), [What is new and Schedule K](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf).
4. Deduct the separately supported Montana NOL, then apply the appropriate rate and minimum. A federal NOL is not automatically the Montana NOL; groups require entity-level schedules. The 2025-2026 filing cycle instructions map adjusted income to line 4, apportioned income line 5, allocated income line 6, pre-NOL income line 7, Montana NOL line 8, taxable income line 9 and gross liability line 10. Confirm the 2026 form before transcribing. Source: [printed pp.5-7](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf).
5. Compare credits only after the gross liability/minimum calculation, then reconcile tentative and estimated payments and withholding. Use the actual credit form and minimum-tax limitation. The 0.5% alternative is an election, not an automatic substitute whenever turnover is low. Source: [printed pp.7-8](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Loss-making ordinary active corporation | File; ordinary $50 minimum still applies. |
| No Montana activity during a period | File the no-activity return or INA-CT affidavit through TAP, rather than silently stop filing. |
| Alternative sales-only election | All three conditions must hold; minimum-tax exception applies to the alternative tax. |
| Unitary affiliates | Combined reporting and Schedule K-Combined may be required; federal consolidated filing is not the state answer. |
| Water's edge | Form WE-ELECT within first 90 days, DOR approval, binding three periods; renew on time. |
| Claimed Public Law 86-272 protection | Document actual activities and still follow Schedule K filing instructions; group nexus requires separate analysis. |

Sources: [printed pp.1-4, 7](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf), [official text](https://revenue.mt.gov/taxes/corporate-income-tax).

## Worked cases

**Case 1.** A standalone all-Montana C corporation has $120,000 of final Montana taxable income and no credits: $120,000 x 6.75% = **$8,100**. A comparable corporation with a $2,000 loss still owes the ordinary **$50** minimum.

```oa-check
name: MT ordinary tax and minimum 2026
inputs:
  income: 120000
  loss: -2000
steps:
- tax: max(max(income, 0) * 0.0675, 50)
- loss_tax: max(max(loss, 0) * 0.0675, 50)
expected:
  tax: 8100
  loss_tax: 50
```

**Case 2, an election decision.** Assume a standalone sales-only corporation meets every alternative-election condition and has $80,000 Montana gross sales. The alternative is **$400**. If regular Montana taxable income is $20,000, ordinary tax is **$1,350**, so the alternative saves $950. At $4,000 of taxable income, ordinary tax is **$270**, so the alternative costs $130 more. Eligibility is assumed, and the comparison precedes credits.

```oa-check
name: MT alternative election comparison both margins
inputs:
  sales: 80000
  high_profit: 20000
  low_profit: 4000
steps:
- alternative: sales * 0.005
- ordinary_high: max(high_profit * 0.0675, 50)
- ordinary_low: max(low_profit * 0.0675, 50)
- saving_high: ordinary_high - alternative
- extra_low: alternative - ordinary_low
expected:
  alternative: 400
  ordinary_high: 1350
  ordinary_low: 270
  saving_high: 950
  extra_low: 130
```


## When to refuse or refer

Refer disputed nexus or protected solicitation, combined and international groups, water's edge elections, specialized industries, state NOL vintage/carryback elections, federal audit changes and credits without their supporting certificates. This skill does not replace the full sourcing rules.

## Filing and payment

File Form CIT using approved corporate tax software unless automatically exempt from e-filing or covered by CWR. TAP supports payments, account history, elections and inactivity filings; it is not described here as a general CIT return-entry substitute. Attach the federal return and required schedules; retain the accepted e-file acknowledgment and payment reference. Source: [official text](https://revenue.mt.gov/taxes/corporate-income-tax), [printed pp.1-2, 7](https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf).

Return and tax are due the 15th day of the fifth month after year-end, moved to the next business day: a calendar 2026 return is due **May 17, 2027**. The automatic six-month filing extension does not extend payment. Estimates, when required, fall on the 15th of months 4, 6, 9 and 12: April 15, June 15, September 15 and December 15, 2026 for a calendar year. Use Form CIT-UT for underpayment analysis. Source: [official text](https://revenue.mt.gov/taxes/corporate-income-tax).

Late filing: minimum $50 or 5% per month up to 25%. Ordinary late payment: 0.5% per month up to 12%; special estimated-tax rules must be distinguished. The 2026 interest rate for corporate tax is the **all-other-taxes** rate, 10.25%, computed daily, rather than the individual 7% rate. Source: [official text](https://revenue.mt.gov/taxes/penalty-and-interest). Recheck interest for days in 2027.

## Completion checklist

- Reconcile federal starting income and each Montana adjustment.
- Confirm correct receipts sourcing, group perimeter and election.
- Apply the minimum and substantiate each credit and Montana NOL.
- Save the return acceptance and payment confirmations.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR corporate income tax. Read for rates, eligibility, current receipts-only apportionment, filing, estimates and e-file waiver. | https://revenue.mt.gov/taxes/corporate-income-tax | 2026-11-13 |
| 2025 Form CIT instructions. Read for printed pp.1-8 and Schedule K: federal starting point, modifications, forms, minimum and election; 2025-2026 filing cycle mechanics. | https://revenue.mt.gov/files/Forms/Montana-Form-CIT-Instructions/2025_Montana_Form_CIT_Instructions.pdf | 2026-11-13 |
| DOR penalties and interest. Read for corporate late filing/payment rules and the 2026 all-other-taxes interest rate. | https://revenue.mt.gov/taxes/penalty-and-interest | 2026-11-13 |

Not yet confirmed: 2026 Form CIT and instructions, including changes to individual line numbers, were not confirmed. Detailed receipts sourcing, unitary-group computations, specialized industry formulae, credit computations and Montana NOL vintage/carryback calculations require their own primary-source working papers.

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.
