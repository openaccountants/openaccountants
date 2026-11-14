---
name: ia-corporate-tax
description: "Compute ordinary Iowa C corporation income tax for tax years beginning in 2026, using the certified 5.5% and 7.1% bands. Identifies the separate financial-institution franchise tax, federal taxable-income base, state adjustments, apportionment, estimates and filing workflow. Trigger on Iowa corporation tax, IA 1120 and Iowa franchise tax."
version: "0.1"
jurisdiction: US-IA
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: income-tax
type: computation
---

# Iowa corporate income and financial-institution franchise tax, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers; a qualified professional must review the facts, computations and filings. Circular 230 section 10.37: apply the law to established facts, consider relevant circumstances and do not rely on audit risk or assume facts that have not been supplied.

**Answer first.** For a tax year beginning in 2026, ordinary corporation tax is 5.5% on the first USD 100,000 of Iowa taxable income and 7.1% above it. This is a graduated tax, not a flat rate on all income. Financial institutions use a separate franchise-tax base and return, with a 3.8% rate for years beginning in 2026. [2026 corporate order](https://revenue.iowa.gov/media/4303/download); [422.63](https://www.legis.iowa.gov/docs/code/2026/422.63.pdf).

## Scope

Ordinary C corporations doing business in Iowa or deriving Iowa-source income, including LLCs taxed as corporations federally. Financial institutions are identified and routed to their separate franchise return. S corporations, partnership returns and PTET elections are outside the computation. Sole proprietors/disregarded individual owners use `ia-income-tax`; federal corporate deductions belong to `us-form-1120-c-corp` and related federal skills.

## Ask the client first

1. Federal entity classification, financial-institution status, tax-year start/end and prior Iowa returns.
2. Iowa operations, property, payroll, customers and out-of-state activities, including solicitation-only claims.
3. Federal taxable income, current/historical NOL detail, tax-exempt interest and state adjustments.
4. Iowa and everywhere receipts, allocable nonbusiness income and related-party transactions.
5. Credits, estimates, withholding, prior overpayment and any federal consolidated group.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount, tax year beginning in 2026 | Official source |
| --- | --- | --- |
| Ordinary corporate band through USD 100,000 | 5.5% | [Order 2025-02, certified 2026 bands](https://revenue.iowa.gov/media/4303/download) |
| Ordinary corporate income above USD 100,000 | 7.1% on excess, plus USD 5,500 on lower band | [Order 2025-02](https://revenue.iowa.gov/media/4303/download) |
| Financial institution subject to franchise tax | 3.8% of the separate franchise-tax base; not the ordinary C-corp rate | [422.60 and 422.63(2)(e)](https://www.legis.iowa.gov/docs/code/2026/422.63.pdf) |
| Corporate estimate screen | Expected tax at least USD 1,000; check exceptions and required installments | [422.38 incorporating 422.16(12)](https://www.legis.iowa.gov/docs/code/2026/422.38.pdf) |

The statute contains unreduced legacy corporate rates but expressly gives the annual certification priority under 422.33(1)(b). The order states the threshold was not met for another reduction, so 2026 stays at the effective bands above. Do not substitute a hoped-for flat 5.5% rate.

### Compute the ordinary IA 1120 liability

1. Determine the correct return and Iowa nexus. An S corporation files IA 1120S, a partnership IA 1065, and a disregarded LLC reports with its owner plus the required disregarded-entity schedule. Financial institutions fall under 422.60, not this ordinary computation. A Public Law 86-272 claim needs a factual review and the IA 1120 claim/attachments; it is not automatic exemption for all remote businesses.
2. Start with federal taxable income **after** the federal NOL deduction, then reconcile modifications under [422.35](https://www.legis.iowa.gov/docs/code/2026/422.35.pdf). Subtract included federal-securities interest; add federally exempt nonqualifying state/foreign securities interest. Add back federal pre-2023 NOL carryovers and use IA 124 for eligible pre-2023 Iowa losses. Do not assume all current NOLs are separately recomputed for Iowa.
3. Separate allocable nonbusiness income from business income. Apply the business activity ratio to business income using Iowa-receipts and everywhere-receipts rules under [422.33(2)](https://www.legis.iowa.gov/docs/code/2026/422.33.pdf), then add Iowa-allocable nonbusiness income and apply remaining allowed loss adjustments in the required order. The receipt ratio is not a payroll/property average. All filers complete Schedule E, even wholly Iowa businesses.
4. Apply the graduated bands to the final Iowa taxable income; subtract supported credits and reconcile estimates and prior credits to balance/refund. Document any special credit or related-party adjustment separately rather than inventing an amount.
5. For the **2025-2026 filing cycle**, the read IA 1120 instructions map reductions through Schedule A, business activity ratio from Schedule E line 13 to IA 1120 line 8, and historical Iowa NOL from IA 124 to line 12. These are reference locations pending final 2026 form confirmation.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Financial institution | Separate IA 1120F and franchise base; 2026 statutory rate shown above, full bank computation needs specialist review |
| Multistate corporation | Allocation and receipt apportionment needed before bands |
| Exempt entity with UBIT/cooperative/short year | Different return deadlines; confirm applicable entity instructions |
| Consolidated group or PL 86-272 | Required elections, exclusions and schedules need specific review |
| Pre-2023 loss | Retain origin-year schedules; distinguish federal addition from Iowa carryover deduction |

## Worked cases

**Case 1.** An invented wholly Iowa C corporation has final Iowa taxable income of USD 80,000 after all modifications. Tax is 80,000 x 5.5% = USD 4,400 before credits/payments. Applying 7.1% to the whole base would overstate liability.

```oa-check
name: Iowa lower-band corporate tax
inputs:
  iowa_taxable: 80000
steps:
  - lower: min(iowa_taxable, 100000) * 0.055
  - upper: max(iowa_taxable - 100000, 0) * 0.071
  - tax: lower + upper
expected:
  tax: 4400
```

**Case 2.** An invented corporation has USD 500,000 of business income after Iowa modifications and removing nonbusiness income, USD 200,000 Iowa receipts, USD 1,000,000 total receipts and no allocable income, credits or losses. The ratio is 20%, giving USD 100,000 Iowa taxable income and USD 5,500 tax. If all those receipts instead belong to Iowa, the base is USD 500,000 and tax USD 33,900. Source-location evidence determines which computation applies.

```oa-check
name: Iowa receipts-apportionment boundary
inputs:
  modified_business_income: 500000
  iowa_receipts: 200000
  total_receipts: 1000000
steps:
  - ratio: iowa_receipts / total_receipts
  - apportioned: modified_business_income * ratio
  - apportioned_tax: min(apportioned, 100000) * 0.055 + max(apportioned - 100000, 0) * 0.071
  - wholly_iowa_tax: min(modified_business_income, 100000) * 0.055 + max(modified_business_income - 100000, 0) * 0.071
expected:
  ratio: 0.20
  apportioned: 100000
  apportioned_tax: 5500
  wholly_iowa_tax: 33900
```

## When to refuse or refer

Refer financial-institution base/apportionment, consolidated elections, pass-through/PTET returns, unusual receipt sourcing, nexus defenses, related-party adjustments, historical NOL disputes and incentive credits. Do not infer professional approval from the commit author's identity.

## Filing and payment

Ordinary calendar-year 2026 IA 1120 is due April 30, 2027 under [422.21 and 422.38](https://www.legis.iowa.gov/docs/code/2026/422.21.pdf). Fiscal-year ordinary filers use the last day of the fourth following month. Co-operatives, UBIT and short years have special deadlines. Check current e-filing requirements and approved Modernized eFile software; payments use GovConnectIowa. For the **2025-2026 filing cycle**, instructions require electronic filing when gross receipts are at least USD 250,000, credits at least USD 25,000, or an Iowa consolidated return is filed; check final 2026 instructions for any revised scope.

Prepare IA 1120, Schedule A, Schedule E and relevant IA 124/group schedules, reconcile the electronic result, submit, save acceptance and separately schedule payment with the correct period/FEIN. Estimates are due the last days of the fourth, sixth, ninth and twelfth months of the tax year, adjusted for weekends/holidays, under [the state estimate instructions](https://revenue.iowa.gov/media/2358/download).

The read **2025-2026 filing-cycle** instructions grant six extra filing months when at least 90% of correct tax was timely paid; interest still runs on any balance. [421.27](https://www.legis.iowa.gov/docs/code/2026/421.27.pdf) provides late-filing/payment penalties, including a no-tax-due specified-business filing penalty based on imputed liability. Confirm the final 2026 extension and penalty calculation before filing; do not treat an extension as permission to pay late.

## Completion checklist

- Ordinary corporation versus franchise/pass-through return established.
- Federal base, historical NOL and state adjustments reconciled.
- Business/nonbusiness division and receipt sourcing supported.
- Certified 2026 bands applied; credits and payments reconciled.
- Current entity-specific forms/e-filing, deadline, acceptance and payment confirmed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IDR Order 2025-02. Read for certified 2026 ordinary corporate bands and failed rate-reduction trigger; document heading governs its 2026 coverage despite inconsistent footer date. | https://revenue.iowa.gov/media/4303/download | 2026-11-13 |
| Iowa Code 422.33. Read for ordinary corporation scope, annual rate certification and business/nonbusiness allocation. | https://www.legis.iowa.gov/docs/code/2026/422.33.pdf | 2026-11-13 |
| Iowa Code 422.35. Read for federal base, securities adjustments and historical NOL treatment. | https://www.legis.iowa.gov/docs/code/2026/422.35.pdf | 2026-11-13 |
| Iowa Code 422.60. Read for financial-institution franchise-tax scope. | https://www.legis.iowa.gov/docs/code/2026/422.60.pdf | 2026-11-13 |
| Iowa Code 422.63. Read for 2026 franchise rate and separate apportionment. | https://www.legis.iowa.gov/docs/code/2026/422.63.pdf | 2026-11-13 |
| Iowa Code 422.21. Read for ordinary and special-entity due dates. | https://www.legis.iowa.gov/docs/code/2026/422.21.pdf | 2026-11-13 |
| Iowa Code 422.38. Read for corporate application of filing provisions. | https://www.legis.iowa.gov/docs/code/2026/422.38.pdf | 2026-11-13 |
| IDR 2025 IA 1120 instructions, 2025-2026 filing cycle. Read for entity return selection, federal taxable income, Schedule A/E, IA 124, electronic thresholds and extension. | https://revenue.iowa.gov/media/4372/download?inline= | 2026-11-13 |
| IDR IA 1120 estimated-tax instructions. Read for estimate liability trigger and fourth/sixth/ninth/twelfth-month due dates. | https://revenue.iowa.gov/media/2358/download | 2026-11-13 |
| Iowa Code 421.27. Read for late filing/payment and no-tax-due business filing penalties. | https://www.legis.iowa.gov/docs/code/2026/421.27.pdf | 2026-11-13 |

Not yet confirmed: final 2026 IA 1120/IA 1120F line mappings and filing-method thresholds; full financial-institution franchise base, bank apportionment and IA 1120F workflow; special credits, consolidated elections, PL 86-272 facts and pass-through/PTET computations. The README marks corporate coverage partial for the financial-institution computation.
