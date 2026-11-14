---
name: nm-corporate-tax
description: "New Mexico ordinary C-corporation income tax at the statutory 5.9% rate and USD 50 franchise tax, with state base adjustments, loss/group controls, CIT-1 filing, estimates and source-period limitations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nm-corporate-tax"
  jurisdiction: "US-NM"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# New Mexico corporate income and franchise tax, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal skills.

**Answer first.** New Mexico corporate income tax is **5.9% of taxable income** for tax years beginning on or after 1 January 2025. The separate **USD 50 corporate franchise tax** can remain due even when no income tax is due or the corporation is inactive. GRT is a different business liability in `nm-sales-tax`. Sources: [HB252 section 10 / NMSA 7-2A-5 and section 42 applicability](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf); [FYI-350, rates and franchise tax](https://realfile.tax.newmexico.gov/FYI-350.pdf).

## Scope

Ordinary C corporations with New Mexico business, property or income, including an LLC/partnership classified as a corporation federally. Franchise-tax scope also includes S corporations, but their return is the separate S-Corp form. Corporate status is not established by a GRT registration alone. Banks, insurers, exempt organizations, unitary groups and special entities require their actual statutory treatment. Source: [FYI-350, definitions, exemptions and filing](https://realfile.tax.newmexico.gov/FYI-350.pdf).

FYI-350 was revised 2 January 2025. Its ancillary mechanics are retained as the verified **2025-2026 filing cycle** and are not asserted to be final 2026 return instructions. Statutory flat rate is effective 2025 onward. Federal corporation computations and figures belong to `us-form-1120-c-corp`.

## Ask the client first

1. Federal classification, legal entities, state registration and tax-year start/end dates.
2. Federal taxable income, New Mexico modifications, exempt income and credits.
3. All-state business locations, property/payroll/sales and unitary-group ownership/transactions.
4. New Mexico loss carryforwards, prior filing method, elections and acquisitions.
5. Each entity exercising its franchise, including inactive entities and short periods.
6. Current/prior/two-years-prior liability and estimated/extension payments.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount and conditions | Official source |
|---|---|---|
| Corporate income tax | 5.9% taxable income for years beginning on/after 1 January 2025 | [HB252 section 10 / NMSA 7-2A-5; section 42](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Corporate franchise tax | USD 50 per year or partial year per corporation exercising corporate franchise; separate from income tax | [FYI-350, franchise tax](https://realfile.tax.newmexico.gov/FYI-350.pdf) |
| Estimated-tax floor | At least USD 5,000 annual tax after credits | [FYI-350, Estimated Payments](https://realfile.tax.newmexico.gov/FYI-350.pdf) |
| Verified estimated safe-harbor comparison | Smallest of 80% current year, 100% prior-year tax if at least USD 5,000, or 110% two-years-prior tax if at least USD 5,000 | [FYI-350, Estimated Payments](https://realfile.tax.newmexico.gov/FYI-350.pdf) |
| Late negligence penalty | 2% per month/part, maximum 20% unpaid tax under applicable conditions | [FYI-350, Interest and Penalties](https://realfile.tax.newmexico.gov/FYI-350.pdf) |

1. Determine the correct taxpayer and filing group. FYI-350 describes worldwide combined filing for unitary corporations with specified elections; do not assume separate filing simply because a corporation has its own federal EIN. Obtain prior elections and complete ownership chart. Source: [filing groups for 2020 onward](https://realfile.tax.newmexico.gov/FYI-350.pdf).
2. Reconcile federal taxable income to New Mexico base income with state adjustments and required exclusions/add-backs. Eliminate intercompany amounts under the applicable group rules. Federal figures, including federal rates and depreciation limits, are loaded from their owner skills rather than repeated here. Source: [Base Income and Net Income definitions](https://realfile.tax.newmexico.gov/FYI-350.pdf).
3. Allocate/apportion income only after the filing group and state modifications are established. The ordinary wholly-NM corporation has no out-of-state factor to assume; a multi-state corporation needs the actual UDITPA factors/elections and special-industry rules. Complete the current CIT schedules with reviewer support; this skill does not supply an unverified 2026 apportionment formula. Source: [Division of Income and filing-method sections](https://realfile.tax.newmexico.gov/FYI-350.pdf).
4. Reconcile the NM NOL schedule separately from the federal loss. FYI-350 defines the state deduction after apportionment, includes grandfathered carryovers and adjusts for entries/exits from a group. Do not deduct an unsupported federal carryover a second time or import federal amounts blindly. Source: [Net Operating Losses](https://realfile.tax.newmexico.gov/FYI-350.pdf).
5. Apply 5.9% to supported positive NM taxable income. Identify eligible credits and preserve certification/claim schedules. Then add **USD 50 per obligated corporation**, including each obligated entity in a combined return, even if taxable income is zero. Source: [NMSA 7-2A-5](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf); [Franchise Tax and group filing](https://realfile.tax.newmexico.gov/FYI-350.pdf).
6. Subtract properly credited estimates and other payments; retain tax-account reconciliation and refund/balance support. A franchise fee is not an income-tax credit and does not satisfy separate GRT or payroll returns.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Inactive corporation retains franchise | Test USD 50 tax despite zero income tax |
| Short tax year | Franchise tax is not automatically prorated; FYI-350 says USD 50 for a partial year |
| S corporation | Separate S-Corp return and franchise obligations, not ordinary CIT-1 income tax computation |
| Multi-state unitary group | Establish combined group/election and actual allocation/apportionment before tax |
| Partnership/disregarded entity | Usually PTE or owner return unless federally taxed as corporation |
| Premium-tax insurer or exempt trust/nonprofit | Specific statutory exemptions and unrelated-business exception require review |
| Seasonal income | Review annualization/penalty calculation on RPD-41287, not only equal payments |

## Worked cases

**Case 1: ordinary corporation.** Invented wholly-NM C corporation has supported taxable income USD 200,000, no credits and USD 10,000 estimates. Income tax USD 11,800 plus USD 50 franchise tax = USD 11,850; balance USD 1,850.

```oa-check
name: New Mexico corporation income and franchise tax
inputs:
  taxable: 200000
  estimates: 10000
steps:
  - income_tax: taxable * 0.059
  - total: income_tax + 50
  - balance: total - estimates
expected:
  income_tax: 11800
  total: 11850
  balance: 1850
```

**Case 2, payment decision under verified filing-cycle rules.** Invented corporation expects USD 20,000 current income tax, had USD 18,000 prior-year tax and USD 15,000 tax two years earlier, all eligible for the comparison. Current-year basis: USD 16,000; prior-year basis USD 18,000; two-year basis USD 16,500. The smallest safe-harbor amount is USD 16,000, or USD 4,000 each equal installment. This prepayment does not reduce final liability, and the franchise tax is still accounted for separately. Confirm final 2026 estimate instructions before relying on the ancillary safe harbor.

```oa-check
name: New Mexico corporate estimated payment comparison
inputs:
  current: 20000
  prior: 18000
  earlier: 15000
steps:
  - current_basis: current * 0.8
  - prior_basis: prior
  - earlier_basis: earlier * 1.1
  - annual_required: min(current_basis,prior_basis,earlier_basis)
  - installment: annual_required / 4
expected:
  current_basis: 16000
  prior_basis: 18000
  earlier_basis: 16500
  annual_required: 16000
  installment: 4000
```

## When to refuse or refer

Refer combined/unitary groups, apportionment, foreign-income adjustments, NOL disputes, specialist financial/insurance entities and credit certifications. Resolve final-year forms before entering line numbers. Old pre-2025 graduated corporation bands do not apply to years starting in 2026.

## Filing and payment

Use **TAP**, https://tap.state.nm.us, corporate account, correct year and **CIT-1**; confirm taxpayer/group identity, enter supported base, state adjustments and allocation, losses, tax, credits and franchise-tax count, then reconcile payments, submit and retain acceptance. Use **CIT-ES** for estimates and **CIT-EXT** for extension payments. Exact final 2026 line numbers are not supplied because the final form was not read. Source: [FYI-350, reporting, estimated and extension payments](https://realfile.tax.newmexico.gov/FYI-350.pdf).

The [current TRD corporate filing page](https://www.tax.newmexico.gov/businesses/corporate-income-franchise-tax-overview/filing-requirements/) says CIT-1 is due the fifteenth day of the fourth month after year end: ordinarily **15 April 2027** for calendar 2026. FYI-350 contains historical third-month language in its extension section alongside newer federal-aligned filing language; do not use the historical March date as the 2026 standard due date. Any electronic-filing timing concession and extension conditions require final-year confirmation. An extension to file does not remove interest on unpaid original-due-date tax.

Verified FYI-350 estimates are due in equal installments on the fifteenth day of the fourth, sixth, ninth and twelfth months: calendar-year 15 April, 15 June, 15 September and 15 December, with applicable nonbusiness-day adjustments. Compute negligence penalty at 2% monthly/part, maximum 20% under the stated conditions; interest is calculated daily at the applicable published quarterly rate. The publication's 2017 rate example is historical and is not a 2026 rate. Source: [FYI-350, Estimates, Extensions and Interest and Penalties](https://realfile.tax.newmexico.gov/FYI-350.pdf).

## Completion checklist

- Correct entity/group and each franchise-tax obligation documented.
- Federal/state base, loss schedule and any apportionment reviewed.
- 5.9% applied only to supported taxable base; franchise tax and credits kept separate.
- Final form, original payment date and estimate schedule verified; acceptance/payment records saved.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| HB252 enacted text. Read section 10 / NMSA 7-2A-5 and section 42 applicability from 2025; neighboring individual schedules also read. Official web PDF opened after direct connection refused. | https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf | 2026-11-13 |
| FYI-350 revised January 2, 2025. Read definitions, exemptions, rates/franchise tax, base, losses, filing groups and allocation, reporting, estimates, extensions and penalty/interest. Historical date/rate passages identified, not reused as current. | https://realfile.tax.newmexico.gov/FYI-350.pdf | 2026-11-13 |
| TRD corporate filing requirements. Read standard fourth-month due date and alternative entity-return routing. | https://www.tax.newmexico.gov/businesses/corporate-income-franchise-tax-overview/filing-requirements/ | 2026-11-13 |

Not yet confirmed: final 2026 CIT-1 form/line numbers and later conformity changes; complete 2026 apportionment factors, industry elections and sourcing; exact final NOL/credit schedules; electronic-filing deadline concession and final 2026 extension/estimate instructions; applicable 2026 quarterly interest rates. These ancillary instructions are the verified 2025-2026 filing cycle. No historical March extension-payment date or 2017 interest example is supplied as usable 2026 guidance.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nm-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nm-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
