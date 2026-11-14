---
name: tn-corporate-tax
description: "Compute Tennessee 2026 franchise/excise and separate business gross-receipts taxes. Covers 0.25% net worth, $100 minimum,6.5% excise, $50,000 pre-apportionment deduction, standard single receipts apportionment, business classifications and TNTAP filing. Triggers on FAE 170, Tennessee franchise tax or business tax."
jurisdiction: US-TN
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
version: "1.0"
type: situation-rules
---

# Tennessee franchise, excise and business gross receipts taxes, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Tennessee entities can owe both 0.25% franchise tax (minimum $100) and 6.5% excise tax, plus a separate business tax on taxable gross receipts. A federal pass-through or disregarded classification does not establish a Tennessee exemption.

## Scope and who this is for

This is the one state owner for franchise/excise and gross-receipts business tax. The 2026 business-tax manual is published. Detailed FAE 170 form mechanics use verified **2025-2026 filing cycle** instructions;2026 FAE 170 line numbers remain unconfirmed. Federal C-corporate computation belongs in `us-form-1120-c-corp`; federal partnership and S-corporation owners are separate. No Tennessee individual income skill is required, but a sole proprietor may still owe business tax.

## Ask the client first

1. What legal and federal tax entity type, ownership, Tennessee registration, fiscal year and exemption approval apply?
2. What federal return and state modification schedules support pre-NOL net earnings, and what Tennessee NOL/credit vintages exist?
3. What year-end net worth, affiliate debt, property-measure/consolidated-net-worth elections and Tennessee/everywhere receipts apply?
4. What gross receipts, exemptions/deductions, dominant activity and wholesale/retail split exist separately at each business-tax location?
5. What prior/current franchise-excise tax after credits, estimates, extension payments and city/county registrations exist?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| Franchise tax ordinary base | 0.25% of apportioned net worth; minimum $100 | [TCA 67-4-2106 to 2109/2119](https://revenue.support.tn.gov/hc/en-us/articles/360058275991-FT-1-Franchise-Tax-Computation) |
| Excise tax | 6.5% of Tennessee net earnings | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058272391-ET-1-Excise-Tax-Computation) |
| Excise standard deduction | Lesser of positive adjusted pre-apportionment business income or $50,000; no loss creation | [2025-2026 filing cycle, Schedule J 32](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf) |
| General standard apportionment | Single receipts factor for years ending fromDecember 31,2025; special formula/election exceptions | [Schedule N/N 1](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf) |
| FAE estimates threshold | At least $5,000 after credits in both current and prior years; annualize short prior year | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057924052-F-E-11-Threshold-for-When-Estimated-Tax-Payments-are-Required) |
| Business tax standard filing threshold | $100,000 per applicable jurisdiction/location rules; test gross-sales schedule per manual | [pp.11-12,108-109](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf) |
| Business minimum, classes 1-4 and 5 B | $22 per location; out-of-state no-location minimum $22 for all Tennessee activity | [pp.65-66](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf) |
| Business class 5 A | 0.001 of applicable gross income; minimum $450, maximum $1,500 annually | [p.66](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf) |
| Business class 1 A/B/C retail; class 1 A wholesale | 0.001 /0.00025 | [pp.65-66](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf) |
| Business class 1 B/C wholesale; class 2/3 wholesale | 0.000375 | [pp.65-66](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf) |
| Business class 1 D retail; class 1 E wholesale | 0.0005 /0.0003125 | [pp.65-66](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf) |
| Business class 2 retail; class 3 retail; class 4; class 5 B | 0.0015 /0.001875 /0.001 /0.0002 respectively | [pp.65-66](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf) |

### Franchise and excise

1. Determine the taxable entity and exemption before computing. FAE 170 has separate Schedule J 1 for partnership entities, J 2 for individual-owned single-member LLCs, J 3 for S corporations andJ 4 for C corporations/other entities; the individual-owned disregarded LLC is therefore not automatically outside the tax. Source: [pp.5-7](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf).
2. Compute net worth as assets less liabilities, apply required affiliate-debt capitalization adjustments and the allowed apportionment factor, then the franchise rate/minimum. The mandatory property-minimum measure was removed; the 2025 instructions still permit an optional property-measure election. Do not silently reimpose that measure or deduct an invented $500,000 from net worth. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058275991-FT-1-Franchise-Tax-Computation), [Schedules A, F 1, F 2 and optionalG](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf).
3. Start excise with the entity's federal net earnings before federal NOL/special deductions. Reconcile all state additions/deductions, including state excise tax, affiliate intangibles/rent, exempt interest and depreciation/conformity differences as relevant. Do not copy the federal NOL. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058272391-ET-1-Excise-Tax-Computation), [Schedules J 1-J 4 andJ](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf).
4. From positive adjusted business earnings deduct up to $50,000 **before** apportionment. The deduction cannot create/increase a loss. Apply the appropriate receipts factor, add directly allocated nonbusiness earnings after any permitted unused deduction, then deduct separately tracked Tennessee loss carryover. The 2025-2026 filing cycle mapping is J 31 business income, J 32 standard deduction, J 34 subtotal, J 35 factor, J 36 apportioned, J 37 allocated, J 38 state NOL, J 39 excise base. Sources: [Schedule J 32-39, Schedule M, N/N 1](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf).
5. Apply 6.5%, add franchise tax, then properly supported credits and payments. Qualified state NOL carryforwards generally run no more than 15 years and have no carryback; verify the actual vintage/limitation. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058272391-ET-1-Excise-Tax-Computation).

### Separate business tax

Business tax is a distinct privilege tax on taxable **gross sales**, including many services and wholesale activity. It can apply to an individual sole proprietor who owes no FAE tax. Identify both state-level (county) and any adopted municipal-level tax. Choose one dominant business classification per location and retailer/wholesaler treatment; apply that rate to the relevant taxable receipts after specific exemptions and deductions. A sales-tax exemption does not automatically establish a business-tax exemption. Sources: [pp.11-16,47-66](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf).

The $100,000 test is not a deductible allowance. The 2026 manual instructs use of Schedule Aline 1 total gross sales for the threshold, with location/jurisdiction rules. Retail versus wholesale status depends on the sales mix; do not elect the cheaper rate without facts. Minimal-activity licenses may be required where gross sales exceed $3,000 but remain below $100,000, with a $15 local fee. Ordinary standard-license holders keep minimum-return obligations until properly closed. Sources: [pp.11-12,28-32,60-66,75-76](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| FAE entity with no positive earnings | Excise may be zero; franchise minimum generally remains. |
| Federal consolidated group | Usually derive a separate-entity pro forma state income base; consolidated net worth is a separate election. |
| P.L.86-272 claimed |2025 instructions expressly distinguish franchise schedules; do not infer complete state-tax exemption. |
| Nonbusiness income | Allocate separately; do not force it through the receipts factor. |
| Business-tax exempt professional service | Specific exempt-service definition controls; taxable goods/other services can still produce tax. |
| Municipal business-tax rate | Current manual allows certain pre 2014 municipal rates to continue; do not assume every municipality uses an identical current table. |
| Contractor deemed locations/class 5 A/coin-operated operator | Special sourcing/minimum rules need the full 2026 manual and actual locations. |

Sources: [official text](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058272391-ET-1-Excise-Tax-Computation), [pp.65-66,85-88,91-108 and 144-152](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf).

## Worked cases

**Case 1.** A hypothetical all-Tennessee C corporation has final adjusted pre-deduction business earnings $200,000, net worth $400,000, no losses/credits and no property election. Excise base after $50,000 deduction=$150,000; excise **$9,750**. Franchise=$400,000 x 0.25%=**$1,000**, total **$10,750**. This illustrates the verified 2025-2026 filing cycle mechanics; confirm 2026 form/conformity before filing.

```oa-check
name: TN ordinary FAE2026 computation with cycle mechanics
inputs:
  adjusted_income: 200000
  net_worth: 400000
steps:
- excise_base: max(adjusted_income-min(max(adjusted_income,0),50000),0)
- excise: excise_base*0.065
- franchise: max(net_worth*0.0025,100)
- total: excise+franchise
expected:
  excise_base: 150000
  excise: 9750
  franchise: 1000
  total: 10750
```

**Case 2, classification decision.** Assume a class 2 location with $200,000 taxable receipts in one jurisdiction and no credits. If 60% of its receipts are retail, the retail 0.0015 rate produces **$300**. If 60% are wholesale instead, the 0.000375 wholesale rate produces **$75**, still above the $22 minimum. The sales mix decides the classification treatment; it is not a free election. A separate city return component, if applicable, would be computed independently.

```oa-check
name: TN business tax classification decision both mixes
inputs:
  sales: 200000
  minimum: 22
steps:
- retail_tax: max(sales*0.0015,minimum)
- wholesale_tax: max(sales*0.000375,minimum)
- difference: retail_tax-wholesale_tax
expected:
  retail_tax: 300
  wholesale_tax: 75
  difference: 225
```


## When to refuse or refer

Refer exemption applications/annual renewals, qualified telecom and financial groups, consolidated net worth, special sourcing, loss vintages, affiliate adjustments, federal 2025/2026 conformity questions and uncertain business classifications. Do not issue a final return from the simplified examples.

## Filing and payment

FAE 170 is filed and paid electronically through [TNTAP](https://tntap.tn.gov/eservices/). Register/add the tax account, select the fiscal period and entity method, complete the applicable J, F, N, M and loss/credit schedules, reconcile Schedule A/BtoC, then submit and save return acceptance/payment reference. The original due date is the 15 thof the fourth month after year-end:April 15,2027 for calendar 2026. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057843932-F-E-5-Due-Date-for-Filing-Form-FAE170-and-Online-Filing-Requirement), [official text](https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf).

A seven-month filing extension requires the payment/credit/refund conditions in F&E 9. If owing tax, pay the lesser of 90% current liability or 100% prior annualized liability by the original date; if prior liability zero, the required extension payment is $100. Extension is not permission to defer tax free of interest. Estimated installments, if both-year $5,000 test met, are April 15, June 15, September 15,2026 and January 15,2027. Estimated-payment penalty is 2% per month/part, capped 24%, plus interest. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058324951-F-E-9-Extension-for-Filing-the-Franchise-and-Excise-Tax-Return), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057924052-F-E-11-Threshold-for-When-Estimated-Tax-Payments-are-Required), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057954352-F-E-13-Estimated-Tax-Payments-Due-Dates-and-Penalty).

Business tax: register the tax account and each location, obtain required city/county license, and use the TNTAP business tax return with separate jurisdiction/location receipts and deductions. The annual due date is the 15 thof the fourth month after fiscal year-end; close the business with a final return within 15 days, or close just the location in TNTAP if other locations remain. Sources: [pp.28-32,68-76](https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf).

General DOR delinquency penalty is 5% monthly/part, maximum 25%, plus applicable interest. The opened GEN 16 page confirms 11.50% only through June 30,2026; the later 2026 rate must be confirmed and is not guessed. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057121372-GEN-16-Penalties-and-Interest).

## Completion checklist

- Establish entity/exemption and separate all three state-tax bases.
- Substantiate pre-apportionment deduction, state NOL, net worth and receipts.
- Reconcile business receipts and classification by jurisdiction.
- Save electronic acknowledgments and payment effective dates.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR 2025 FAE 170 instructions. Read for pp.1-11 and standardN/N 1 apportionment section:rates, entity schedules, standard deduction, state NOL and form mapping;2025-2026 filing cycle. | https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae170instructions2025.pdf | 2026-11-13 |
| DORFT 1. Read for net worth basis,0.25% and $100 minimum. | https://revenue.support.tn.gov/hc/en-us/articles/360058275991-FT-1-Franchise-Tax-Computation | 2026-11-13 |
| DORET 1. Read for federal starting point, stateadjustments,6.5% andloss carryforward. | https://revenue.support.tn.gov/hc/en-us/articles/360058272391-ET-1-Excise-Tax-Computation | 2026-11-13 |
| DOR 2026 business-tax manual. Read for pp.11-16,28-32,60-76,85-88 and 108-109:threshold, licenses, rates, returns and sourcing distinctions. | https://www.tn.gov/content/dam/tn/revenue/documents/tax_manuals/june-2026/business-tax.pdf | 2026-11-13 |
| DORFAE 5. Read for original due date, TNTAPandmandatory electronic filing. | https://revenue.support.tn.gov/hc/en-us/articles/360057843932-F-E-5-Due-Date-for-Filing-Form-FAE170-and-Online-Filing-Requirement | 2026-11-13 |
| DORFAE 9. Read for seven-month extension and payment conditions. | https://revenue.support.tn.gov/hc/en-us/articles/360058324951-F-E-9-Extension-for-Filing-the-Franchise-and-Excise-Tax-Return | 2026-11-13 |
| DORFAE 11. Read for both-year $5,000 threshold and short-year annualization. | https://revenue.support.tn.gov/hc/en-us/articles/360057924052-F-E-11-Threshold-for-When-Estimated-Tax-Payments-are-Required | 2026-11-13 |
| DORFAE 13. Read for estimate dates and 2% monthly 24% penalty. | https://revenue.support.tn.gov/hc/en-us/articles/360057954352-F-E-13-Estimated-Tax-Payments-Due-Dates-and-Penalty | 2026-11-13 |
| DORGEN 16. Read for general penalty and interest effective only throughJune 30,2026. | https://revenue.support.tn.gov/hc/en-us/articles/360057121372-GEN-16-Penalties-and-Interest | 2026-11-13 |

Not yet confirmed: 2026 FAE 170 and June 2026 FAEmanual could not be read;2026 line numbers and later conformity changes require confirmation. Detailed credits, special entity exemptions, industry/group apportionment, loss-vintage limits and business-tax exemptions/deductions are not fully computed. Current municipal business-tax rates and postJune 2026 interest rate remain unconfirmed. The 2026 businessmanual is current; FAEmechanics are explicitly 2025-2026 filing cycle.
