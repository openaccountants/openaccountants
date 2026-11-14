---
name: me-corporate-tax
description: "Maine 2026 C-corporation income tax: nexus, adjusted federal income, graduated gross tax before apportionment, estimates and financial-institution franchise boundary."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/me-corporate-tax"
  jurisdiction: "US-ME"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Maine corporate and franchise tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Maine computes graduated corporate gross tax on adjusted federal taxable income **before** multiplying by the Maine apportionment factor. Financial institutions use a separate franchise regime; Maine does impose franchise tax on those institutions. [36 M.R.S.5200](https://legislature.maine.gov/statutes/36/title36sec5200.html); [2026 1120W-ME](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1120w.pdf); [5206](https://legislature.maine.gov/statutes/36/title36sec5206.html).

## Scope

Ordinary C-corporation income-tax computation and employer-level financial-institution routing. Federal corporate computation belongs to `us-form-1120-c-corp`; payroll to `me-payroll`; resident owners to `me-income-tax`. Combined/unitary groups, financial-institution asset/income bases, insurers, special factors, PTE elections and NOL/credit calculations are partial specialist areas.

## Ask the client first

1. Federal entity classification, formation/commercial domicile, tax-year dates and completed federal corporate taxable income?
2. Maine/everywhere property, payroll and sales, employee/agent activities, corporate partnership interests and solicitation facts?
3. Related entities, ownership/unitary activities, consolidated federal return and state filing history?
4. Maine additions/subtractions, depreciation/research basis, NOL history, special-industry status and credit evidence?
5. Maine/everywhere sales by destination/service receipt, nontaxable-state sales, estimates, prior-year liability and extensions?

## The method, step by step

1. **Determine tax and filing regime.** Nexus arises from Maine organization/commercial domicile or exceeding $250,000 Maine property, $250,000 payroll, $500,000 sales, or 25% of total property/payroll/sales. Partnership interests can create corporate nexus. Federal P.L.86-272 protection is preserved; use `us-pl-86-272-income-tax-nexus` for its actual limits. Nexus, Maine net income and federal corporate tax treatment determine the ordinary return obligation. S corporations with corporate-level federal taxable gains can be included; do not treat all pass-through income as C-corporation income. [5200-B](https://legislature.maine.gov/statutes/36/title36sec5200-B.html); [5102(6),(8),(10)](https://legislature.maine.gov/statutes/36/title36sec5102.html).
2. **Reconcile adjusted federal taxable income.** Start with the completed federal result, then Maine additions/subtractions and supported loss adjustments. Separate state depreciation/research/production-property schedules from federal deductions. The opened **2025-2026 filing cycle** booklet uses 1120ME, Schedule 1A additions and 1S subtractions; final 2026 line numbers remain unconfirmed. Current 2026 enacted modifications must be checked before importing the older line map. [2025 instructions, specific instructions](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/25_1120me_gen_instr_w_cover_pg.pdf); [2026 enacted changes](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/legischange26.pdf).
3. **Apply bands to the all-source adjusted income.** Use the table below. Do not first multiply income by Maine's factor: that incorrectly shifts income into lower bands. Unitary group income and band allocation require the combined-return rules. [5200(1-A),(3)-(5)](https://legislature.maine.gov/statutes/36/title36sec5200.html); [1120W-ME 2026 lines 1-2](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1120w.pdf).
4. **Apportion gross tax.** Ordinary Maine apportionment uses a sales factor, then gross tax x supported Maine factor. Tangible sales generally follow delivery, services where received; the statutory throwout of tangible sales into nontaxable states, unitary numerator/denominator and special-method exceptions must be tested. A raw Maine-sales/all-sales fraction is not always the final factor. [5211(8),(14)-(17)](https://legislature.maine.gov/statutes/36/title36sec5211.html).
5. **Apply supported credits and reconcile estimates.** Do not use a credit merely because the business is located in Maine. Reconcile current and prior-year tax, estimates and carryforward records. The 2026 estimate worksheet confirms ordinary prior-year 100% or current 90% safe harbor, with a large-corporation exception. [2026 worksheet instructions 1-4](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1120w.pdf).

## Rates, bands and thresholds

| Adjusted federal taxable income T | Gross corporate tax before apportionment | Authority |
| --- | --- | --- |
| Not over $350,000 | .035T | [5200](https://legislature.maine.gov/statutes/36/title36sec5200.html) |
| Over $350,000 through $1,050,000 | $12,250 + .0793(T-350,000) | [5200](https://legislature.maine.gov/statutes/36/title36sec5200.html) |
| Over $1,050,000 through $3,500,000 | $67,760 + .0833(T-1,050,000) | [5200](https://legislature.maine.gov/statutes/36/title36sec5200.html) |
| Over $3,500,000 | $271,845 + .0893(T-3,500,000) | [5200](https://legislature.maine.gov/statutes/36/title36sec5200.html) |

Current rates are stated in [5200(1-A)](https://legislature.maine.gov/statutes/36/title36sec5200.html) and [2026 1120W-ME](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1120w.pdf).

## Boundary table

| Fact | Treatment or stopping point |
| --- | --- |
| Financial institution | Section 5206 imposes franchise tax on institutions with Maine net income/assets and sufficient physical presence, including federal pass-through/disregarded entities. Option 1 is 1% Maine net income +0.008% Maine assets; option 2 is 0.039% Maine assets. Election is annual and irrevocable for that year; no election defaults to option 1. Bases, valuation and final 2026 form detail require specialist review. [5206](https://legislature.maine.gov/statutes/36/title36sec5206.html); [MRS franchise overview](https://www.maine.gov/revenue/taxes/income-estate-tax/franchise-tax-1120b-me). |
| Insurance / special financial business | Do not use ordinary corporate income bands for an excluded insurance-premium/franchise taxpayer. Confirm entity and industry definitions. |
| Group or nonstandard factor | Stop the stand-alone calculation for unitary/combined, partnership look-through, special sourcing or alternative factor. |
| PTE election | Separate 2026 elective regime; this skill does not prepare it. [2026 changes, PTE program](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/legischange26.pdf). |
| Federal depreciation/research | Federal owner supplies the federal calculation. Apply Maine modifications and recapture; do not import federal expensing unchanged. |

## Worked cases

### All-Maine corporation

Adjusted federal taxable income is $500,000, all taxable business activity is Maine, and there are no credits. Gross and apportioned tax are $24,145. This is corporate tax before estimates/payment reconciliation.

```oa-check
name: ME all-Maine corporate tax 2026
inputs:
  income: 500000
  factor: 1
steps:
  - gross: 12250 + (income - 350000) * 0.0793
  - tax: gross * factor
expected:
  gross: 24145
  tax: 24145
```

### Multistate corporation: tax then factor

Adjusted federal taxable income is $2 million and the correctly established Maine factor is 25%, with no credits. Gross tax is $146,895; Maine tax is $36,723.75. Applying bands to $500,000 apportioned income would produce the wrong answer. The example assumes factor work is already complete.

```oa-check
name: ME gross tax before apportionment 2026
inputs:
  income: 2000000
  factor: 0.25
steps:
  - gross: 67760 + (income - 1050000) * 0.0833
  - tax: gross * factor
expected:
  gross: 146895
  tax: 36723.75
```

## When to refuse or refer

Refer combined/unitary group determination, NOL/credit ordering, special sourcing/throwout, disputed nexus/P.L.86-272, insurers, franchise asset/income bases, PTE elections, short years and amended returns. Do not represent the financial-institution routing note as a complete 1120B-ME computation.

## Filing and payment

File 1120ME through the Maine Tax Portal/approved electronic route. The final 2026 return and general instructions were inactive labels when the 2026 form index was read. The **2025-2026 filing cycle** booklet says the ordinary return is due the 15th of the fourth month, with an automatic filing extension equal to federal extension plus 30 days or seven months, whichever expires later; filing extension does not extend payment. Its 90% original-date payment provision and final 2026 calendar/extension mechanics need reconfirmation. MRS's current FAQ contains a simpler six-month statement that conflicts with that detailed booklet; do not promise an extension date until reconciled against final 2026 instructions. [2025 instructions, general 1-4](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/25_1120me_gen_instr_w_cover_pg.pdf); [corporate FAQ](https://www.maine.gov/revenue/faq/corporate-income-tax); [2026 form index](https://www.maine.gov/revenue/tax-return-forms/corporate-income-tax-2026).

The actual 2026 worksheet requires estimates unless current **or** prior-year tax after credits is below $1,000. Ordinary installments are 15th of fourth, sixth, ninth and twelfth months: calendar-year April 15, June 15, September 15 and December 15, 2026, with weekend/holiday adjustment. Minimum annual target is smaller of prior-year tax for a 12-month year or 90% of current tax; large corporations and short years have special rules. [2026 1120W-ME instructions](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1120w.pdf).

## Completion checklist

Resolve regime/nexus; reconcile federal-to-Maine base; establish group and factor; apply gross bands before factor; support credits/estimates; resolve final 2026 return/extension and every specialist gap before filing.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| 36 M.R.S.5200; read for current bands and tax-before-apportionment rule, neighboring historical bands. | https://legislature.maine.gov/statutes/36/title36sec5200.html | 2026-11-13 |
| 36 M.R.S.5200-B; read for thresholds, partnership nexus and federal protection. | https://legislature.maine.gov/statutes/36/title36sec5200-B.html | 2026-11-13 |
| 36 M.R.S.5102; read for corporation, Maine net income and taxable corporation definitions. | https://legislature.maine.gov/statutes/36/title36sec5102.html | 2026-11-13 |
| 36 M.R.S.5211; read for single sales factor, sourcing, throwout and alternative methods. | https://legislature.maine.gov/statutes/36/title36sec5211.html | 2026-11-13 |
| 2026 1120W-ME; read for all rates, tax-then-factor, estimate trigger/safe harbor/dates and special cases. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1120w.pdf | 2026-11-13 |
| 2025 1120ME instructions, 2025-2026 filing cycle; read for federal starting point, schedules, filing/extension/electronic rules; not final 2026 line authority. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/25_1120me_gen_instr_w_cover_pg.pdf | 2026-11-13 |
| MRS corporate FAQ; read for current nexus/rates and conflicting simplified extension statement. | https://www.maine.gov/revenue/faq/corporate-income-tax | 2026-11-13 |
| 2026 corporate form index; read for active estimate worksheet and inactive final-return labels. | https://www.maine.gov/revenue/tax-return-forms/corporate-income-tax-2026 | 2026-11-13 |
| 36 M.R.S.5206; read for both methods, physical-presence condition and annual default election. | https://legislature.maine.gov/statutes/36/title36sec5206.html | 2026-11-13 |
| MRS franchise overview; read for 1120B-ME regime and current 2025-2026 filing-cycle form label. | https://www.maine.gov/revenue/taxes/income-estate-tax/franchise-tax-1120b-me | 2026-11-13 |
| MRS 2026 changes; read for state adjustment and elective PTE boundaries. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/legischange26.pdf | 2026-11-13 |

Not yet confirmed: final 2026 return/line map and extension conflict; full state asset/research/NOL/credit calculations; group/special sourcing; financial-institution income/assets bases and final 2026 franchise forms. Coverage is partial, not inferred from the 2026 tag.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `me-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/me-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
