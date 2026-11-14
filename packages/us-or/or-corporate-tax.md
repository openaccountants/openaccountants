---
name: or-corporate-tax
description: "Oregon corporate excise versus income tax, C-corporation rates and Oregon-sales minimum, computation, group gate, estimates and published 2025-2026 filing-cycle return workflow."
jurisdiction: US-OR
category: state-tax
domain: tax
tax_year: 2026
tier: 2
type: computation
version: "0.1"
last_updated: 2026-11-13
---

# Oregon corporate excise and income tax, 2026

> **General reference only.** This skill provides working papers and a filing brief, not accountant approval. Apply cited law to verified facts, identify assumptions and unresolved issues, and obtain qualified professional review before filing or acting. Circular 230 section 10.37 requires reasonable factual and legal analysis.

## Scope

Oregon (US-OR) corporate excise or corporation income tax, ordinary C-corporation base/rate/minimum computation, estimated payments, group gate and filing. CAT is a separate tax owned by `or-cat`. The ongoing rate structure is stated on DOR's corporate requirements page and ORS 317.061/090. Final 2026 Form OR-20 instructions were not confirmed; return boxes, detailed procedure and examples use the **2025-2026 filing cycle** and must not be presented as final 2026 form fields.

Use `us-form-1120-c-corp` for federal taxable income and federal deductions/rates, `us-form-1120-s-s-corporation-return` for federal S reporting, `or-income-tax` for individual owners, and `or-payroll` for employee taxes. No federal numerical rate, credit or wage base is repeated. Partnerships, disregarded entities, S corporations, exempt entities and special industries are routed before ordinary Form OR-20 computation.

## Ask the client first

- What federal classification, legal entity, year-end, incorporation and Oregon-source/doing-business facts apply?
- What people, property, sales, services, inventory and solicitation activities determine nexus or a claimed federal limitation?
- What federal group, common ownership, unitary operations, foreign/insurance affiliates and intercompany items exist?
- What federal income before NOL/special deductions, Oregon adjustments, basis differences, losses and credit records are supported?
- What Oregon/total sales, allocated income, apportionment method and minimum-tax sales calculation apply?
- What prior/current liability, short-year dates, estimates, extensions, filing receipts and notices need reconciliation?

## The method, step by step

### 1. Choose excise versus income tax and the return

A corporation doing business in Oregon generally files an excise return for that privilege, measured by net income and subject to the applicable minimum. A corporation not doing business but with Oregon-source income may instead file the corporation income return, generally with calculated tax and no excise minimum. Merely registering with the Secretary of State does not alone create a tax filing requirement when there is no Oregon business/source income. Conversely, being formed elsewhere does not remove Oregon nexus. [DOR filing requirements](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx); [2025 OR-20 pp.3-4](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

| Classification / facts | Return / boundary | Official source |
|---|---|---|
| Ordinary C corporation doing business | Form OR-20, excise tax and applicable minimum | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Corporation with Oregon-source income but not doing business | Form OR-20-INC, income tax; no ordinary excise minimum | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |
| Federal S corporation | Form OR-20-S; test entity-level taxable items and excise minimum, while owners report pass-through income separately | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |
| Federally corporate-classified LLC | Corporate return corresponding to business/source facts | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Disregarded entity | Include in owner's appropriate return; do not invent a separate corporate filing from an LLC name alone | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Insurance, cooperative, exempt UBTI, REIT/RIC or other specialized entity | Specific return or adjustments before ordinary computation | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |

Physical/economic nexus, nexus through interests/agents and P.L. 86-272 protection require their own facts. The CAT registration threshold is not a corporate income-tax nexus safe harbor. Qualifying tangible-goods solicitation protection does not automatically cover SaaS, services, intangible licensing or nonprotected in-state activities. Use `us-pl-86-272-income-tax-nexus` for the federal limitation without importing CAT conclusions. [OR-20 filing/group sections](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf); separate CAT [ORS 317A.116](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

### 2. Resolve consolidated reporting before the base

The cycle instructions require a consolidated Oregon return for corporations in a consolidated federal return that are also unitary for Oregon purposes, subject to exclusions and special entities. Remove nonunitary affiliates from the Oregon base/factors through supported additions/subtractions. Insurance affiliates filing separately have their own treatment. Federal consolidated membership alone is not the Oregon unitary decision, and the CAT more-than-50% grouping rule is not a replacement corporate rule. Retain federal-to-Oregon membership, intercompany and apportionment reconciliations. [OR-20 pp.3-4](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

For a consolidated excise return, determine minimum tax on Oregon sales of the filing group; it is one group minimum, not a separate minimum on each included affiliate. Mixed nexus, protected affiliates, foreign operations, ownership changes and insurer exceptions require the detailed schedules rather than a guessed separate-return calculation. [OR-20 pp.3-4,15](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

### 3. Reconcile income, allocation, losses and apportionment

In the **2025-2026 filing-cycle** map, Form OR-20 line 1 ordinarily starts from federal taxable income before federal NOL/special deductions, using federal Form 1120 line 28. Co-ops/other return types can have different starting lines. Reconcile the Oregon group first, then line 2 additions from Schedule OR-ASC-CORP, line 3 subtotal and line 4 subtractions. Do not begin at federal tax paid or after federal NOL and then deduct a state loss again. [OR-20 line instructions](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

State taxes measured by net income, federal/Oregon asset basis and depreciation, exempt income, dividend treatment, interest, foreign income, inventory and related-group items can require specific adjustments. Oregon minimum tax is not automatically added back for an ordinary OR-20/20-S filer just because paid; insurers have separate rules. The live requirements FAQ contains an older federal conformity-date statement, so it cannot resolve 2026 OBBBA/conformity without the applicable law and instructions. No automatic federal bonus/section 179/174A adjustment is invented. [DOR minimum-tax FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx); [OR-20 adjustment instructions](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

Ordinary multistate income generally uses the applicable single-sales-factor Oregon sourcing rules, with allocation of nonapportionable income and special industry methods where required. Schedule OR-AP supplies the percentage and Oregon taxable income; a customer billing ratio is not universally the correct sales factor. Use current goods/services/intangible sourcing, throwback/throwout and special-industry rules before calculating the factor. This skill does not provide a complete sourcing catalogue. [OR-20 Schedule OR-AP directions and Appendix C](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

Use Oregon loss records, not federal NOL automatically. The current requirements page describes corporate loss carryforward up to fifteen years and no carryback, with insurance-specific cross-reference. Vintage, ownership/group, allocation and allowable-loss amounts must be tested before using line 6; do not apply a single assumed percentage to every vintage. Capital loss line 7 has separate net-capital-gain and carryover rules. [DOR NOL section](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx); [OR-20 pp.14-15](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

### 4. Calculate ordinary tax and the excise minimum separately

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| Ordinary corporate Oregon taxable income up to $1 million | 6.6%, not below zero | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |
| Ordinary Oregon taxable income above $1 million | $66,000 + 7.6% of excess over $1 million | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |
| C corporation excise tax | Greater of calculated tax and Oregon-sales minimum, before applicable credit limitations | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |
| Corporation income tax filer not doing business | Calculated tax if any; no ordinary excise minimum | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |
| S corporation doing business | Ordinary $150 excise minimum; entity-level taxable items can require calculated tax and special rules | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |
| Estimated corporate tax trigger | Expected annual tax at least $500, including minimum | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx |

The following ordinary C-corporation minimum schedule is in ORS 317.090 and the published **2025-2026 filing-cycle** Appendix B. Oregon-sales measurement differs from CAT receipts and from Oregon taxable income; use the correct filing-group sales workpaper. Special entities can have different requirements. Do not apportion the resulting minimum by the income factor or reduce it with ordinary credits. [OR-20 pp.15-16,21](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| Ordinary C-corp Oregon sales Under $500,000 | $150 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $500,000-<1 million | $500 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $1 million-<2 million | $1,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $2 million-<3 million | $1,500 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $3 million-<5 million | $2,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $5 million-<7 million | $4,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $7 million-<10 million | $7,500 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $10 million-<25 million | $15,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $25 million-<50 million | $30,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $50 million-<75 million | $50,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales $75 million-<100 million | $75,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Ordinary C-corp Oregon sales At least $100 million | $100,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |

Ordinary calculation: taxable income T after state modifications/allocation/apportionment/losses; calculated tax = 6.6% x min(max(T,0),1 million) + 7.6% x max(T - 1 million,0). Determine minimum M from the correctly measured Oregon sales. Before special adjustments the excise tax is max(calculated tax,M). Apply only supported credits with the minimum preserved and each credit's own ordering/carryforward rules. A loss corporation doing business can still owe minimum tax. The S-corporation minimum does not flow through as an owner's credit. [DOR rate/minimum sections](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx); [OR-20 credit instructions](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

### 5. Form OR-20 workpaper map

| 2025-2026 filing-cycle field | Computation / support | Official source |
|---|---|---|
| Line 1 | Correct federal/group taxable income before NOL/special deductions | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Lines 2-5 | State additions/subtractions, then income before net loss deduction | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Lines 6-7 | Supported Oregon net loss and capital loss under their separate rules | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Line 8 / Schedule OR-AP | Supported apportionment percentage; 100.0000 for wholly Oregon nonapportioned business | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Line 9 | Oregon taxable income, or Schedule OR-AP part 2 line 12 for apportioning filer | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Lines 10-12 | Calculated excise tax and any eligible farm-capital-gain adjustment | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Line 13 | Minimum tax from correct Oregon/group sales | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Line 14 | Greater of line 12 and line 13 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Lines 15-16 | Applicable installment-sale/other adjustments and tax before credits | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Lines 17-20 | Standard/carryforward credits with minimum preserved | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Lines 21-22 | Applicable LIFO benefit recapture treatment and net excise tax | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |
| Payments/refund/balance fields | Reconcile estimates, prior credits, extension payment, adjustments and accepted payments | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf |

The printed instructions' line 20 minimum reference appears to point to line 15 even though the actual minimum is line 13; follow the actual form and substantive minimum rule, not that stray cross-reference. Special farm, LIFO, credit and allocation fields are gates to separate calculations, not assumed zeros. Final 2026 line numbers and conformity are unconfirmed. [OR-20 pp.15-16](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

### 6. Estimated tax and payment scheduling

Expected liability at least $500, including minimum, triggers corporate estimates. Ordinary calendar-year dates are April 15, June 15, September 15 and December 15, shifted to the next business day when applicable. Fiscal years use fifteenth days of months four, six, nine and twelve. For an ordinary full-year annual projection the source worksheet divides the required amount by the actual number of remaining required installments, usually four; changes in expected tax require catch-up as directed. Do not silently import CAT dates or individual January installment dates. [DOR estimates](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx); [OR-20 pp.2-3](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

Oregon corporate requirements expressly differ from federal estimates. Prior-year, large-corporation, annualized, seasonal and short-year exceptions require OR-37 and the applicable law. This skill's cases pay the full projected liability, not an unverified safe harbor. If federal EFT is mandatory for estimated payments, Oregon EFT is required absent approved waiver. Pay electronically through Revenue Online/financial institution or use OR-20-V under the paper-payment instructions. Do not send a paper voucher for an EFT payment. [OR-20 pp.2-3](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

## Boundary and exception table

| Facts | Treatment |
|---|---|
| Registered but no business/source income | Do not infer minimum filing solely from registration. |
| Oregon-source income without doing business | Test OR-20-INC and no excise minimum. |
| Operating loss but doing business | Test ordinary excise minimum independently of calculated tax. |
| Credit greater than calculated tax | Preserve minimum; determine actual allowable credit/carryforward. |
| Federal consolidated group | Determine Oregon unitary membership and special entities first. |
| C-corp and CAT obligations | Independent base, group, sales/nexus, filing and estimates. |
| Foreign/source, special industry or apportionment dispute | Require specific schedules/authority rather than a simple billing ratio. |
| Final 2026 return | Reconcile published 2025-cycle map and current law to final 2026 instructions. |

## Worked cases

### Case 1: credits cannot consume the minimum

An invented ordinary C corporation doing business in Oregon has $2 million reconciled Oregon taxable income, $3 million minimum-tax Oregon sales and $10,000 otherwise allowable nonrefundable credits. Calculated tax is $142,000, minimum $2,000 and tax after credits $132,000 before payments/special adjustments. An alternative operating-loss year with the same sales and credits has zero calculated tax but still $2,000 minimum. The credit is assumed substantively eligible; this example only checks the floor.

```oa-check
name: Oregon corporate excise minimum decision
inputs:
  taxable_income: 2000000
  minimum: 2000
  eligible_credit: 10000
  loss_year_income: -100000
steps:
  - calculated: min(max(taxable_income, 0), 1000000) * 0.066 + max(taxable_income - 1000000, 0) * 0.076
  - after_credit: max(calculated - eligible_credit, minimum)
  - loss_calculated: min(max(loss_year_income, 0), 1000000) * 0.066 + max(loss_year_income - 1000000, 0) * 0.076
  - loss_tax: max(loss_calculated - eligible_credit, minimum)
expected:
  calculated: 142000
  after_credit: 132000
  loss_calculated: 0
  loss_tax: 2000
```

### Case 2: annual projection and minimum estimate gate

An invented ordinary full-year excise filer has projected $1,000 minimum tax, no calculated tax above it, credits or prior payments, and is subject for all four installments. Paying full projected tax requires $250 each on the ordinary corporate dates. An alternative $150 minimum with no other liability falls below the $500 estimate trigger, although the annual return/payment obligation remains. Numeric flags record those established scenarios, not a complete estimate-exception classifier.

```oa-check
name: Oregon corporate minimum estimates
inputs:
  annual_projected_tax: 1000
  alternative_minimum: 150
  estimate_gate: 1
  alternative_gate: 0
steps:
  - ordinary_installment: annual_projected_tax * estimate_gate / 4
  - alternative_installment: alternative_minimum * alternative_gate / 4
  - ordinary_total: ordinary_installment * 4
expected:
  ordinary_installment: 250
  alternative_installment: 0
  ordinary_total: 1000
```

## When to refuse or refer

Refer P.L. 86-272/economic nexus disputes, consolidated/unitary exclusions, source/throwback disputes, special industries, foreign/insurance income, losses/ownership changes, pass-through withholding/composite/PTET, farm/LIFO adjustments, credit ordering and audits. Do not certify a final 2026 computation before resolving federal conformity and the year's forms. Incomplete records require a stated unresolved adjustment, not an assumed nil amount.

## Filing and payment

Oregon corporate returns are generally due the fifteenth day of the month following the federal corporation return due date: the current DOR page illustrates a calendar C return in May and S return in April. Weekend/state holidays move the date; the page says corporation due dates are not affected by Emancipation Day. This is a state rule referring to the federal deadline, not a restatement of federal filing law. Check the actual year/entity, including short or June year-end returns. [DOR due dates](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx).

Use federal Form 7004 for extension as instructed, retained/submitted with the Oregon return and marked in the extension box; for Oregon-only extension use the stated Oregon-only notation. The state extended due date is generally the fifteenth of the month following the federal extended date. A filing extension does not defer tax payment. Use the applicable return instructions/payment coupon and retain payment allocation. [DOR extensions](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx); [OR-20 due/extension instructions](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

Electronic return filing and EFT payment are separate. The 2025 instructions describe mandatory Oregon electronic filing when the corporation must e-file with the IRS, with an advance waiver process; obtain actual acceptance through approved software and preserve it. Revenue Online payment is not proof that an OR-20 was filed. Attach the required Oregon schedules/federal/group documents. Current electronic formats and final 2026 requirements remain to be confirmed. [OR-20 e-file and filing checklist](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf).

Amend using the correct year's form and amended indicator with full corrected amounts, detailed adjustments and support. A federal or other-state original/amended return changing relevant income generally requires Oregon amendment within ninety days; audit changes have their own reporting requirements. Use the instructions' specific amended-payment route, not ordinary EFT assumptions. Oregon NOL carryback is not created by filing a federal carryback. Protect a contingent refund with the stated protective-claim procedure, not an invented amended loss. [OR-20 pp.4-5](https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf); [DOR amendments](https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx).

Late-payment/filer penalties, underpayment interest and audit adjustments are distinct. Use dated payments/notices and current annual rates rather than CAT or UI penalties. Keep federal-to-Oregon basis, losses, credits and group records through their applicable use/assessment periods; a specific numeric retention period is not certified here.

## Completion checklist

- Establish classification, business/source facts, tax and correct return.
- Resolve federal/Oregon group membership before base and minimum sales.
- Support additions/subtractions, losses, allocation and factor.
- Calculate net-income tax and minimum separately; preserve the credit floor.
- Reconcile corporate estimates, extension, acceptance and payment dates.
- Report final-year/form/conformity gaps and special-regime referrals.

## Sources

| Official source / section read | URL | Read on |
|---|---|---|
| DOR Corporation filing requirements, tax/minimum, estimates, NOL, due/extension and amendments sections. Read for excise versus income tax, ongoing rates, entity routes, payment trigger and filing boundaries. | https://www.oregon.gov/dor/programs/businesses/Pages/corp-requirements.aspx | 2026-11-13 |
| DOR 2025 Form OR-20 instructions, pp.2-5, adjustment/line sections pp.10-16, Appendix B p.21 and Appendix C; 2025-2026 filing cycle. Read for group/base, minimum bands, form mapping, credit floor, estimates, amended workflow and apportionment boundaries. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-20-instructions_102-020-1_2025.pdf | 2026-11-13 |
| ORS chapter 317, sections 061/090 as cross-referenced by the return instructions. Read for statutory authority for the rate/minimum structure, read alongside operative-year instructions. | https://www.oregonlegislature.gov/bills_laws/ors/ors317.html | 2026-11-13 |
| ORS 317A.116. Read for CAT is independent and P.L. 86-272 does not protect that separate tax. | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html | 2026-11-13 |

Not yet confirmed: final 2026 OR-20/20-INC/20-S instructions/fields and full 2026 legislative/conformity audit, including OBBBA/bonus/179/174A; full nexus and receipts-sourcing/throwback catalogue; combined-group foreign/insurer/ownership details; complete NOL vintage/limitation and capital-loss schedules; special entity/PTET/composite/pass-through withholding calculations; all credit ordering/carryovers, OR-37 prior-year/large-corporation/annualized/seasonal/short-year exceptions; current e-file waiver thresholds/formats, complete penalty/interest and record retention periods. The live FAQ federal-conformity date is stale and is not treated as final 2026 law.
