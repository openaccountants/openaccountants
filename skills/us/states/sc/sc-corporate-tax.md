---
name: sc-corporate-tax
description: "South Carolina ordinary C corporation 5 percent income tax, federal/state reconciliation, allocation/apportionment, separate capital licence fee and minimum, SC1120 filing, estimates and entity boundaries."
version: "0.2"
jurisdiction: US-SC
category: state-tax
tax_year: 2026
last_updated: 2026-11-14
tier: 2
domain: income-tax
type: computation
---

# South Carolina corporate income tax and licence fee, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal figures and computations belong to the linked federal owner skills.

**Answer first.** An ordinary C corporation pays 5% on SC taxable income and a separate annual corporate licence fee based on capital stock and paid-in/capital surplus, with a USD 25 minimum. A loss for income-tax purposes does not automatically eliminate the licence fee. Source: [12-6-530](https://www.scstatehouse.gov/code/t12c006.php); [12-20-50](https://www.scstatehouse.gov/code/t12c020.php); [C corporation page](https://dor.sc.gov/business-income-taxes/corporate/c-corporation).

## Scope

Ordinary C corporations doing business or earning income in SC, including LLCs federally taxed as corporations. Federal corporate computations belong to `us-form-1120-c-corp`; individual/pass-through owner tax to `sc-income-tax`. This skill owns both corporate income and ordinary licence fee. S corporations useSC 1120 S and can still owe licence fees; banks, insurers, utilities, exempt entities, combined/consolidated groups and special elections need separate analysis.

## Ask the client first

1. Legal entity, federal election/classification, accounting year, FEIN and SC start/qualification/closing dates.
2. Federal taxable income/return and state additions, subtractions, depreciation and loss schedules.
3. SC and everywhere sales/receipts, allocated nonbusiness income and related-entity data.
4. First-day capital stock/paid-in surplus, applicable financial statement, earned surplus and special exclusions.
5. Approved income/licence credits, prior-year tax, estimates and extension payments.
6. SC1070 registration letter, CL-1 status and electronic-filing obligation.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate, amount and condition | Official source |
|---|---|---|
| Ordinary C corporation income | 5% of SC taxable income | [12-6-530](https://www.scstatehouse.gov/code/t12c006.php) |
| Annual licence fee | fifteen dollars plus one dollar for each thousand dollars, or fraction of a thousand dollars, of applicable capital stock and paid-in or capital surplus; minimum twenty-five dollars | [12-20-50(A)](https://www.scstatehouse.gov/code/t12c020.php) |
| Initial CL-1 licence fee | USD 25, within 60 days of doing business/using capital if not already filed/paid with Secretary of State | [account setup](https://dor.sc.gov/business-income-taxes/corporate/c-corporation) |
| Electronic filing/payment | Liability USD 15,000 or more per filing period | [filing mandate](https://dor.sc.gov/business-income-taxes/corporate/c-corporation) |
| Corporate estimated tax | Income tax less credits USD 100 or more under verified instructions | [Extensions and Estimated Payments](https://dor.sc.gov/sites/dor/files/forms/SC1120I.pdf) |

1. Establish nexus/classification and initial registration. Filing the first corporate return registers the business with SCDOR; mark Initial Return, reconcile CL-1/initial USD 25 fee and retain SC1070 requirements letter. Secretary-of-State qualification is separate. Do not file a sole proprietor as a corporation merely because it has an LLC name. Source: [account setup and return scope](https://dor.sc.gov/business-income-taxes/corporate/c-corporation).
2. Start with federal corporate taxable income, not the new individual AGI/SCIAD base. The verified **2025-2026 filing cycle** instructions use Schedule A/B adjustments: add qualifying other-state bond interest, state/local income or net-income-measured franchise taxes, federal NOL and other nonconforming items; subtract qualifying U. S. obligation interest and separately computed state adjustments. Maintain separate state basis/depreciation/loss workpapers. Source: [SC1120 lines 1/2 and Schedule A/B](https://dor.sc.gov/sites/dor/files/forms/SC1120I.pdf).
3. Directly allocate the applicable nonbusiness items and apportion remaining business income. SCDOR distinguishes sales-only apportionment for manufacturing/selling/dealing in tangible property from gross-receipts apportionment for most service/repair/financial businesses; special industries have separate methods. SC1120 SchedulesF/G/H andH-1/H-2/H-3 implement the classification. Final 2026 market sourcing/ratio exceptions remain Not yet confirmed. Source: [tax rates and apportionment](https://dor.sc.gov/business-income-taxes/corporate/c-corporation); [allocation/apportionment schedules](https://dor.sc.gov/sites/dor/files/forms/SC1120I.pdf).
4. Compute 5% of established SC taxable income and apply supported income-tax credits. Do not substitute the 25-dollar licence minimum for an income-tax minimum. Net-income tax and licence fee are separate computations/credit/payment streams. Source: [Part I and Part II](https://dor.sc.gov/sites/dor/files/forms/SC1120.pdf).
5. Compute licence fee on applicable capital stock and paid-in/capital surplus, not retained earnings. Current statute says USD 1 for each USD 1,000 **or fraction**, plus USD 15, minimum USD 25; use this statutory unit rule when a base is not an exact USD 1,000 multiple. The form's shorthand is 0.001 xbase +15 with minimum 25, so retain the reconciliation if form rounding differs. Multistate licence base/apportionment and each consolidated member's minimum are separate; minimum cannot be apportioned away. The fee generally applies to the licence year **following** the income-tax year. Sources: [12-20-50/60/70](https://www.scstatehouse.gov/code/t12c020.php); [licence period and Part II](https://dor.sc.gov/sites/dor/files/forms/SC1120I.pdf).
6. The 2026 amendment adds a certified qualifying-equity exclusion for some SC-headquartered corporations, first applying to a tax year beginning **after 1 July 2026**. Do not use that exclusion for every calendar 2026 base or without certificate/records; match the actual licence period. Holding-company, exempt-entity and final-return rules also need their own support. Source: [12-20-50(C/D),2026 Act 243 effective-date note](https://www.scstatehouse.gov/code/t12c020.php).
7. Reconcile credits, estimates and extension payments against the correct tax stream. S corporation status does not itself waive the corporate licence fee under the verified instructions. Partnerships/sole proprietors and elective 3% active-business entity/owner rules are different regimes; route individual-owner computation to `sc-income-tax`. Source: [SC1120S licence section](https://dor.sc.gov/sites/dor/files/forms/SC1120I.pdf); [12-6-545](https://www.scstatehouse.gov/code/t12c006.php).

## Boundary and exception table

| Situation | Action |
|---|---|
| Corporate loss | Income tax can be zero; licence fee/minimum still tested |
| Capital base not multiple USD 1,000 | Reconcile statutory fraction rule with form's 0.001 shorthand |
| Multistate service or goods business | Choose proper allocation/apportionment method, separate licence ratio |
| S corporation/qualified PTE | Separate return, licence fee and optional active-business election |
| Consolidated group | Member-by-member capital/minimum and state consolidation requirements |
| Bank/insurer/utility/cooperative/exempt entity | Refer separate tax/fee regime and exemptions |

## Worked cases

**Case 1, ordinary C corporation.** Invented SC taxable income USD 200,000 after federal/state reconciliation gives income tax USD 10,000. Established applicable licence base USD 1,000,000 gives USD 1,015 fee. With USD 8,000 income estimates and no licence payments/credits, remaining combined amount is USD 3,015. Capital is an exact USD 1,000 multiple, so statutory and form shorthand agree.

```oa-check
name: South Carolina corporate income and separate licence fee
inputs:
  sc_taxable_income: 200000
  applicable_capital: 1000000
  income_estimates: 8000
steps:
  - income_tax: sc_taxable_income * 0.05
  - licence_fee: max(15 + ceil(applicable_capital / 1000), 25)
  - total_balance: income_tax - income_estimates + licence_fee
expected:
  income_tax: 10000
  licence_fee: 1015
  total_balance: 3015
```

**Case 2, loss and capital boundary.** Invented corporation has zero SC taxable income after losses. At applicable capital USD 10,000, licence fee is USD 25. At USD 10,001, section 12-20-50's next USD 1,000 fraction gives USD 26. A zero income-tax result does not mean zero filing/payment; final-return/exemption exceptions must still be checked.

```oa-check
name: South Carolina licence minimum and fraction boundary
inputs:
  capital_at: 10000
  capital_over: 10001
steps:
  - fee_at: max(15 + ceil(capital_at / 1000), 25)
  - fee_over: max(15 + ceil(capital_over / 1000), 25)
expected:
  fee_at: 25
  fee_over: 26
```

## When to refuse or refer

Refer disputed nexus, combined/consolidated reporting, special industries, capital-reclassification/exclusion certificates, large losses, PTE elections and uncertain conformity. Obtain final 2026 instructions for any changed schedule before filing.

## Filing and payment

File **SC1120** through approved corporate e-file/vendor or permitted paper below electronic mandate; complete federal attachment, Part I income tax, Part II licence fee, SchedulesA/B and relevant allocation/apportionment, Schedule D annual report and credits. The website once labels paper returnSC 1120 C, but linked actual form isSC 1120; use the actual current form. Retain acceptance and separately reconcile income/licence payments. Due 15 thday of fourth month after close; calendar 2026 ordinarily 15 April 2027, subject to final calendar relief. Source: [filing/due-date requirements](https://dor.sc.gov/business-income-taxes/corporate/c-corporation); [actual return title/PartsI-II](https://dor.sc.gov/sites/dor/files/forms/SC1120.pdf).

Verified **2025-2026 filing cycle** instructions require estimates when expected income tax after credits is USD 100 or more, installments 15th of months 4,6,9,12 usingSC 1120-CDP or MyDORWAY Business Income Tax Payment. UseSC 2220 for underpayment. Extension payment through MyDORWAY submits an extension request; SC1120-T is the paper route. Filing extension does not extend payment of income tax or licence fee. Final 2026 safe-harbor/large-corporation and extension detail remain Not yet confirmed. Source: [Extensions and Estimated Payments](https://dor.sc.gov/sites/dor/files/forms/SC1120I.pdf).

## Completion checklist

- Entity/nexus/initial registration and correct income/licence periods identified.
- Federal reconciliation and allocation/apportionment supported; credits/losses documented.
- Separate licence base/minimum/fraction and member rules computed; payments matched by stream.
- Correct return and annual report filed, acceptance/payment saved, final 2026 gaps resolved.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for Current 12-6-530 ordinary corporate 5% and 12-6-545 pass-through boundaries; neighboring exemptions read. | https://www.scstatehouse.gov/code/t12c006.php | 2026-11-13 |
| Read for Current 12-20-50 fullA-D, financial-statement definitions, equity exclusion and 2026 effective date; 60 apportionment and 70 group minima. | https://www.scstatehouse.gov/code/t12c020.php | 2026-11-13 |
| Read for Current C corporation page:5%, registration/CL-1, licence fee, next-year period, apportionment types, filing/electronic mandate/due dates. | https://dor.sc.gov/business-income-taxes/corporate/c-corporation | 2026-11-13 |
| Read for SC1120I:2025 conformity context, federal adjustments, allocation/apportionment, licence period/Part II, S corporation boundary, estimates/extensions.2025-2026 filing cycle. | https://dor.sc.gov/sites/dor/files/forms/SC1120I.pdf | 2026-11-13 |
| Read for Current unyear-marked SC1120 revision 7/2/25, all 8 pages:Part I, Part II capital/licence, Schedule D annual report and allocation/apportionment schedules; 2025-2026 filing cycle. | https://dor.sc.gov/sites/dor/files/forms/SC1120.pdf | 2026-11-13 |

Not yet confirmed: final 2026 SC1120/SC1120S/instructions/credit schedules, conformity and depreciation/loss changes, current detailed sourcing/ratio elections, certified equity exclusion procedures, group/special-industry rules and final estimate/extension safe harbors. Ordinary statutory rate/licence calculation is confirmed; complete specialist return treatment is partial.
