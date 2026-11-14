---
name: us-de-corporate-tax
description: "Delaware corporate income tax, 2026, tax year 2026: applicability, state computations, exceptions, registration, returns, payment and source-backed worked cases."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-de-corporate-tax"
  jurisdiction: "US-DE"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Delaware corporate income tax, 2026

## Scope

Delaware corporate income tax is 8.7% on the modified federal base allocated/apportioned to Delaware. This is distinct from entity franchise/annual tax (`de-franchise-tax-and-llc`) and seller GRT (`de-gross-receipts-tax`). The 2026 law and indexed estimate threshold are confirmed; form-line mechanics use the **2025-2026 filing cycle** CIT-TAX instructions pending the final 2026 annual form. Federal computation belongs to `us-form-1120-c-corp`. [State source](https://delcode.delaware.gov/title30/c019/index.html); [State source](https://revenue.delaware.gov/frequently-asked-questions/corporate-income-tax-faqs/).

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

## Ask the client first

1. Federal classification, taxable year, Delaware business activities, property/staff and claimed statutory exemption?
2. Separate-company federal taxable income, federal consolidated workpapers and any disregarded subsidiaries?
3. Allocable income and related expenses; Delaware and everywhere receipts by source/type, commercial domicile and partnership interests?
4. Research/depreciation history, acquisition/service dates, state/federal basis, losses and credits?
5. Gross receipts in each of the preceding three years for the small-corporation estimate test?
6. Prior/current tax, dated estimates, extensions, federal adjustments and nexus notices?

## The method, step by step

1. **Test liability.** Every domestic/foreign corporation doing business in Delaware and not §1902(b)-exempt files CIT-TAX even with zero income or a loss. A statutory registered office alone without Delaware business is exempt; formation alone does not create income tax. Federal S status follows through to the corporate exemption, but separate S/nonresident-owner filing under Chapter 11 remains a different job. Holding/investment-company and specialist exemptions require the exact activities, not the label on the entity. [State source](https://delcode.delaware.gov/title30/c019/index.html); [State source](https://revenue.delaware.gov/frequently-asked-questions/corporate-income-tax-faqs/).
2. **Start with separate-company federal taxable income.** Delaware prohibits consolidated income tax returns. Reconstruct each member as if separately filed. Disregarded corporate-owned LLC operations enter the corporate owner's return. Reconcile additions/subtractions under §1903(a), including income taxes, exempt/nonbusiness items, federal/state depreciation differences and credit-related expenses. [State source](https://revenuefiles.delaware.gov/2025/BusinessTaxForms_Instructions/CIT-TAX_2025-01_Instructions.pdf).
3. **Apply HB 255, not an assumption of full OBBBA conformity.** For corporations, property acquired/placed in service after January 19, 2025 and before January 1, 2031 continues pre-OBBBA bonus rules: generally 20% bonus in 2026, plus regular depreciation on the remainder; special production-property expensing is decoupled in its statutory window. Preserve separate basis and reversal/disposal adjustments. For 2022-2024 domestic research, retroactive federal expensing does not flow into Delaware; continue prior amortization. For 2025 onward current research expensing conforms. Individuals have a different start date; see `de-income-tax`. [State source](https://revenuefiles.delaware.gov/2025/TIMs/HB_255_TIM.pdf); [State source](https://delcode.delaware.gov/sessionlaws/ga153/chp231.shtml).
4. **Allocate first, then apportion the remainder.** Section 1903(b) assigns specified rents/royalties, gains and interest under their own property/transaction/commercial-domicile rules. Post 2020 ordinary interstate corporations use a single gross-receipts factor for remaining income, with statutory Delaware-source numerator and everywhere denominator. Do not import another state's market-sourcing or throwback rule. Telecommunications/worldwide-headquarters corporations have special treatment; request relief under §1903(c) if the statutory result is inequitable. [State source](https://delcode.delaware.gov/title30/c019/index.html); [State source](https://revenuefiles.delaware.gov/2025/BusinessTaxForms_Instructions/CIT-TAX_2025-01_Instructions.pdf).
5. **Compute** Delaware allocated income plus apportioned remainder, apply the statutory state NOL treatment and 8.7%, then only substantiated credits/payments. Delaware generally follows federal NOL rules but caps any carryback at $30,000 in a preceding year under §1903(a)(2)g; do not invent a separate state 80% rule. Complex loss years/retroactive federal changes need a full CIT-NOL workpaper. [State source](https://delcode.delaware.gov/title30/c019/index.html); [State source](https://revenue.delaware.gov/frequently-asked-questions/corporate-income-tax-faqs/).

### Rates, bands and thresholds

| Item | Amount or rule | Official source |
| --- | --- | --- |
| Corporate income tax | 8.7% | [§1902](https://delcode.delaware.gov/title30/c019/index.html) |
| Ordinary apportionment from 2020 | Single receipts factor; separately allocate designated income | [§1903](https://delcode.delaware.gov/title30/c019/index.html) |
| 2026 small corporation | Receipts not exceeding $26,767,000 in any 2 of preceding 3 taxable years | [State source](https://revenuefiles.delaware.gov/2025/Annual_Threshold_Adjustment_Factor_for_CY26.pdf) |
| Regular estimates | 50%/20%/20%/10% in months 4/6/9/12 | [§1905](https://delcode.delaware.gov/title30/c019/index.html) |
| Small-corporation estimates | 25%/25%/25%/25% | [§1905](https://delcode.delaware.gov/title30/c019/index.html) |
| State NOL carryback limit | $30,000 per preceding year | [§1903(a)(2)g](https://delcode.delaware.gov/title30/c019/index.html) |
| 2026 bonus generally | 20%, plus regular depreciation, under HB 255 windows | [State source](https://revenuefiles.delaware.gov/2025/TIMs/HB_255_TIM.pdf) |
| Late filing/payment/interest | 5% monthly maximum 50%; 1% monthly maximum 25%; 0.5% interest monthly or part | [State source](https://delcode.delaware.gov/title30/c005/sc03/index.html) |

## Worked cases

**Case 1:** Hypothetical modified income $1,000,000 includes $100,000 separately allocated entirely outside Delaware. Remaining $900,000 has a verified Delaware receipts factor 25%; Delaware taxable income $225,000 and tax $19,575. Assume no losses/credits and ordinary corporation sourcing.

```oa-check
name: DE corporate allocated apportioned
inputs:
  modified: 1000000
  allocated_out: 100000
  factor: 0.25
steps:
- remainder: modified - allocated_out
- de_income: remainder * factor
- tax: de_income * 0.087
expected:
  remainder: 900000
  de_income: 225000
  tax: 19575
```

**Case 2:** Receipts in two prior years are $26 m and $26.5 m, within 2026 threshold, so a $40,000 current-year estimate is paid $10,000 each instalment. If only one of three prior years met the threshold, regular instalments would be $20,000/$8,000/$8,000/$4,000. This is a classification test; it is not an optional deferral election.

```oa-check
name: DE small corporation estimate decision
inputs:
  tax: 40000
steps:
- small: tax * 0.25
- regular_first: tax * 0.5
- regular_middle: tax * 0.2
- regular_last: tax * 0.1
expected:
  small: 10000
  regular_first: 20000
  regular_middle: 8000
  regular_last: 4000
```

## When to refuse or refer

Refer P.L.86-272/economic-nexus disputes, holding/investment and nonprofit exemptions, S/composite returns, financial/insurance/telecommunications/headquarters regimes, apportionment relief, foreign income, research transition, acquisitions, complex NOLs and incentive credits. No exemption follows just from having an out-of-state customer.

## Filing and payment

Calendar 2026 CIT-TAX and balance are due April 15, 2027; fiscal years use day 15 of month 4 after year-end. A timely federal extension automatically extends filing; otherwise request CIT-EXT by the original due date. Payment remains due then. File the initial CIT-EST declaration even if the estimate is zero; later zero vouchers need not be filed. Regular 2026 estimates are April 15, June 15, September 15, December 15; small corporations use equal 25% instalments. No tentative return for a period shorter than 92 days. Underpayment additions/safe harbours and annualization are governed by §535; do not equate paying last year's tax with a universal safe harbour. Report final federal changes within 90 days under §514. Retain separate federal reconciliation, source schedules, state basis, loss/credit history and payment confirmations. [State source](https://delcode.delaware.gov/title30/c019/index.html); [State source](https://revenuefiles.delaware.gov/2025/BusinessTaxForms_Instructions/CIT-TAX_2025-01_Instructions.pdf); [State source](https://delcode.delaware.gov/title30/c005/sc03/index.html).

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| Chapter 19. Read for liability, exemptions, modifications, allocation, estimates and 92 day exception. | https://delcode.delaware.gov/title30/c019/index.html | 2026-11-13 |
| Corporate FAQ. Read for rate, separate return, filing date and NOL. | https://revenue.delaware.gov/frequently-asked-questions/corporate-income-tax-faqs/ | 2026-11-13 |
| 2025 CIT-TAX instructions. Read for 2025-2026 filing cycle computation, schedules and filing procedures. | https://revenuefiles.delaware.gov/2025/BusinessTaxForms_Instructions/CIT-TAX_2025-01_Instructions.pdf | 2026-11-13 |
| 2026 threshold table. Read for small-corporation indexed receipts limit. | https://revenuefiles.delaware.gov/2025/Annual_Threshold_Adjustment_Factor_for_CY26.pdf | 2026-11-13 |
| HB 255. Read for corporate/individual conformity dates. | https://delcode.delaware.gov/sessionlaws/ga153/chp231.shtml | 2026-11-13 |
| TIM 2025-2. Read for research, bonus and production-property adjustments. | https://revenuefiles.delaware.gov/2025/TIMs/HB_255_TIM.pdf | 2026-11-13 |
| Chapter 5. Read for penalties, estimate additions and interest. | https://delcode.delaware.gov/title30/c005/sc03/index.html | 2026-11-13 |

Not yet confirmed: final 2026 CIT-TAX form/line numbers; taxpayer-specific source/nexus determinations, credits, complex NOL and research transition schedules. These are not computed by this ordinary corporate method.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-de-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-de-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
