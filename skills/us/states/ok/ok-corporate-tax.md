---
name: ok-corporate-tax
description: "Compute Oklahoma 2026 corporate income tax at 4%, recognizing franchise-tax repeal from 2024. Covers Form 512 federal starting point, state allocation/apportionment, Oklahoma accrued-tax deduction, NOL and depreciation controls, credits, estimates and electronic filing. Trigger on OK C corporation, Form 512 or franchise-tax questions."
jurisdiction: US-OK
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
version: "1.0"
type: situation-rules
---

# Oklahoma corporate income tax and franchise repeal, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Oklahoma corporate income tax remains 4% for 2026. The former annual franchise tax filing ended after tax year 2023; repeal of franchise tax does not remove the corporate income-tax return or other entity obligations.

## Scope and who this is for

Ordinary C corporations doing business in or deriving income from Oklahoma. Federal C-corporate income belongs in `us-form-1120-c-corp`. The 2026 OTC report confirms the state rate; detailed Form 512 mechanics use the verified **2025-2026 filing cycle** packet, with final 2026 instructions pending. S corporations, partnerships, electing pass-through entities, banks and exempt organizations use their own forms/rules and are not computed as ordinary C corporations here.

## Ask the client first

1. What legal/federal entity type, tax year, Oklahoma activity, source income, exemption or P.L.86-272 position applies?
2. What final federal return, Oklahoma modifications, depreciation elections, NOL vintages and credit approvals support the base?
3. What property, payroll and sales are in Oklahoma and everywhere, and what income must be directly allocated?
4. Is there a federal/state consolidated election, membership change, short year or liquidation?
5. What prior 12-month tax, current forecast, estimates, withholding and extension payments exist?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| 2026 ordinary corporate rate | 4% of Oklahoma taxable income | [2026 OTC report p.1](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/reports/annual-reports/otc/AR-2026.pdf) |
| Franchise tax / return | No filing requirement for tax year 2024 onward; 2023 and earlier obligations remain | [official text](https://oklahoma.gov/tax/businesses/other-taxes.html) |
| Ordinary unitary apportionment | Arithmetic average of property/payroll/sales factors present; only denominator-positive factors count | [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf) |
| Oklahoma accrued-tax deduction | Before-credit income divided by 26 when no credits; credit-covered income excluded; never below zero | [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf) |
| Estimates threshold | $500 or more reasonably expected current liability; smaller of 70% current tax or 100% prior 12-month tax | [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf) |
| Filing timing | 30 days after the applicable federal due date; special liquidation rule; next business day if OTC closed | [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf) |
| Extension payment tests | 90% paid to avoid delinquency penalty; 100% to avoid delinquent interest | [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf) |
| Delinquency | 5% late-payment penalty under packet conditions; 1.25% monthly interest | [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf) |

### Establish filing and the state base

1. A corporation doing business in or deriving Oklahoma-source income files even if no tax is due. Confirm the entity form: 512 for ordinary C corporations, 512-S for S corporations and separate pass-through/exempt rules. An inactive entity’s conclusion requires its own facts. Sources: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf), [official text](https://oklahoma.gov/tax/businesses/other-taxes.html).
2. Complete the federal computation first. Form 512 Part 1 Column A is the federal starting computation for all corporations. Domestic corporations deriving all income in Oklahoma use the applicable Column B method; corporations with a unitary multistate business generally use Part 2. Reconcile taxable interest from other states and U.S.-obligation exclusions, Oklahoma depreciation/expensing adjustments and all state additions/deductions. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf).
3. Keep depreciation elections asset by asset. The prior-cycle packet permits elected 100% Oklahoma bonus for qualified property and improvement property, but forbids duplicating a full federal deduction. It requires separate federal depreciation add-back and Oklahoma subtraction lines rather than a net entry, with continuing recovery-period tracking. Do not claim automatic conformity to every 2026 federal change. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf), pp.6-7, 68 O.S.2358.6a.
4. Calculate Oklahoma NOL independently, with detailed vintage, utilization and state apportionment schedules. The packet distinguishes ordinary carryforward treatment from special farming/insurance and other carryback exceptions, and provides an irrevocable election to forego an otherwise permitted carryback. Do not simply import a federal NOL amount or treat every loss as having identical vintage rules. The final 2026 limits require confirmation. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf), p.5.

### Allocate, apportion and deduct accrued tax

5. Separate directly allocable income, including situs-based oil/mining/property and other specified income, from net apportionable business income. Compute each ordinary factor as Oklahoma/everywhere property, payroll or sales. Average only the factors actually present. Apply the factor to apportionable income, then add directly allocated Oklahoma income and make other supported state adjustments. Special industry/election rules are not silently replaced by this ordinary formula. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf), Part 2 pp.8-9.
6. Calculate the **Oklahoma accrued-tax deduction**, not a federal-income-tax deduction. With positive pre-accrual income N and no credits, deduction = N/26; state taxable income = N - deduction, and tax = 4% of that result. With allowable credits C, the packet’s working formula is deduction = max((N - C/0.04)/26,0), then compute tax and apply the credit under its own limits. The deduction is denied on income covered by credits. Round final return entries as prescribed; do not apply 4% directly to a pre-accrual amount. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf), Part 2 line 9 and credit example p.9.
7. Reconcile tax, approved credits, estimates, withholding and prior payments. The prior-cycle map is taxable income to page 1 line 1; 4% tax line 2; credits line 3; liability after credits line 4; payments lines 5-11; refund/amount due in the remaining section. Attach the federal return, factor schedules and required balance-sheet/reconciliation information. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf).

### Repealed franchise tax and other obligations

Starting with tax year 2024 there is **no Oklahoma franchise-tax filing requirement**. FRX-200 expressly applies to 2023 and prior; do not create a 2026 franchise payment or carry the old capital rate into the new year. Outstanding old-year assessments, reinstatement and separate foreign-corporation/Secretary-of-State registration requirements can remain. Industry-specific gross-production and other taxes are separate from ordinary corporate income tax. Sources: [official text](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/general/FRX-200.pdf), [official text](https://oklahoma.gov/tax/businesses/other-taxes.html), [franchise-repeal FAQ](https://oklahoma.gov/tax/helpcenter/businesses.html).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| No 2026 franchise return | Still test ordinary corporate income filing and entity registration obligations. |
| Federal consolidated group | State election and separate member factors matter; the federal group result is not itself the state base. |
| One or two factors absent | Omit absent-denominator factors from the average; do not assign them a zero and divide by three. |
| Credit covers some income | Reduce the accrued-tax deduction for credit-covered income. |
| NOL, capital gain or separately allocated property | Use the appropriate state/vintage/source treatment before ordinary tax. |
| S corporation / electing PTE / bank / exempt entity | Refer to its own return and in-lieu/nonresident rules; do not apply this simplified 512 computation. |

Sources: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf), [official text](https://oklahoma.gov/tax/businesses/other-taxes.html).

## Worked cases

**Case 1.** A corporation has final Oklahoma pre-accrual income of $130,000 after all allocation, loss and state adjustments, with no credits. Accrued-tax deduction = $130,000/26 = **$5,000**; taxable income = **$125,000**; 4% tax = **$5,000**. Charging $5,200 on the pre-accrual income would skip the required computation. No 2026 franchise tax is added.

```oa-check
name: OK corporate accrued tax no credits
inputs:
  pre_accrual_income: 130000
steps:
- accrual: max(pre_accrual_income/26,0)
- taxable: pre_accrual_income-accrual
- tax: taxable*0.04
expected:
  accrual: 5000
  taxable: 125000
  tax: 5000
```

**Case 2, credit decision.** Assume final pre-accrual income $130,000 and a fully allowed $4,160 credit. Credit-covered income = $104,000; remaining $26,000 gives **$1,000** accrued-tax deduction, **$129,000** taxable income and **$5,160** gross tax; after credit, **$1,000** remains. Without the credit the first case gives $5,000 tax. The credit cannot be subtracted from that first case without recomputing the deduction.

```oa-check
name: OK credit decision changes accrued deduction
inputs:
  pre_accrual_income: 130000
  credit: 4160
  rate: 0.04
steps:
- credit_income: credit/rate
- accrual: max((pre_accrual_income-credit_income)/26,0)
- taxable: pre_accrual_income-accrual
- gross_tax: taxable*rate
- net_tax: max(gross_tax-credit,0)
expected:
  credit_income: 104000
  accrual: 1000
  taxable: 129000
  gross_tax: 5160
  net_tax: 1000
```


## When to refuse or refer

Refer uncertain nexus/P.L.86-272, consolidated elections, special industry apportionment, credit qualification, loss carrybacks, federal/state conformity, exempt entities and audit/reinstatement. The examples assume a final supported pre-accrual base, not raw federal income.

## Filing and payment

File electronically under the packet’s Rule 710:50-17-1 requirement using an approved corporate product. A generic FAQ still says paper is accepted; follow the specific current packet’s electronic rule, and resolve any required exception with OTC. Enter the correct year/fiscal/short-year information and all supporting schedules, transmit, then retain state acceptance and payment reference. Do not assume an individual OkTAP 511 screen prepares the corporate return. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf).

The ordinary due date is **30 days after the federal due date**, with next-business-day adjustment when OTC is closed. For a calendar-2026 corporation whose federal date is April 15, 2027, 30 days gives May 15, a Saturday, and therefore **May 17, 2027** under the packet rule; confirm the final 2026 filing notice. A no-liability return with an approved federal extension receives the stated automatic extension; otherwise request **504-C** by the original date. Pay the 90%/100% amounts needed for penalty/interest treatment. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf).

Estimated payments use **OW-8-ESC** and the 15th of the fourth, sixth, ninth and first succeeding months. Calendar dates are April 15, June 15, September 15, 2026 and January 15, 2027, subject to valid calendar adjustment. Use the published smaller-of-current/prior safe harbor and annualization where allowed. Save proof of timely payment; an extension does not eliminate unpaid-tax interest. Source: [Form 512 instructions, 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf), pp.3-4,10-11.

## Completion checklist

- Confirm entity, filing requirement and final 2026 instructions.
- Tie federal base, Oklahoma modifications, factors, allocated income and state loss vintages.
- Recompute accrued tax after credits and reconcile payments.
- Retain electronic acceptance, attached schedules and effective payment date.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| OTC FY2026 annual report. Read for p.1, 4% corporate rate explicitly for 2025 and 2026. | https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/reports/annual-reports/otc/AR-2026.pdf | 2026-11-13 |
| OTC current Form 512 packet. Read for 2025-2026 filing cycle pp.3-11 and return: filing, entity distinction, independent losses, depreciation, ordinary apportionment, accrued-tax deduction/credit example, estimates and due date. | https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/corporate-income-tax/current/512-Pkt.pdf | 2026-11-13 |
| OTC other taxes. Read for no franchise filing from 2024 and separate industry/entity obligations. | https://oklahoma.gov/tax/businesses/other-taxes.html | 2026-11-13 |
| OTC FRX-200. Read for express 2023-and-prior limitation and 2024 repeal notice. | https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/businesses/general/FRX-200.pdf | 2026-11-13 |
| OTC business FAQ. Read for franchise repeal and continuing old-year/foreign-corporation fee distinction; broad paper-filing FAQ reconciled with specific packet. | https://oklahoma.gov/tax/helpcenter/businesses.html | 2026-11-13 |

Not yet confirmed: Final 2026 Form 512 packet and calendar notice, changes to federal conformity/depreciation, detailed NOL vintage/carryback limits, special industry/elective factors, consolidated-group and PTE/nonresident mechanics, specific credits and foreign-corporation registration fee. Those areas remain partial; 2025-2026 filing cycle form mechanics are not represented as final 2026 instructions.
