---
name: ms-corporate-tax
description: "Mississippi 2026 C-corporation income and franchise tax:0/4/5% income bands,0.50 per1000 franchise rate and25 minimum, capital/income reconciliation, estimates and83-105 filing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ms-corporate-tax"
  jurisdiction: "US-MS"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Mississippi corporate income and franchise tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Mississippi corporate income tax remains0% on the first $5,000,4% on the next $5,000 and5% above $10,000. The 2026 franchise rate is$0.50 per$1,000 or fraction of the statutory capital base above $100,000, with a $25 minimum. It is not repealed until 2028 under the cited phase-out. [DOR corporate tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions); [SB2858§§3-5](https://billstatus.ls.state.ms.us/documents/2016/html/SB/2800-2899/SB2858SG.htm).

## Scope

Ordinary domestic/foreign C corporations and federally corporate-classified entities with Mississippi obligations. This skill is the single state corporate/franchise owner, separate from individual phase-out rates. PTE/S corporations, insurance, combined groups, mineral producers, contractor direct accounting, NOLs and incentives need specialist work. Federal corporate input belongs to `us-form-1120-c-corp`.

## Ask the client first

1. Entity/federal classification, formation/qualification, Mississippi activity, accounting period and group/PTE relationships?
2. Separate federal ordinary income, state additions/deductions, asset basis, NOLs, credits and prior Mississippi returns?
3. All-source/Mississippi receipts, property, payroll, allocable income, industry and apportionment support?
4. Year-end capital accounts/reserves/debts, Mississippi assessed-property values and franchise allocation worksheet?
5. Estimates/payments, extensions, account notices, amendments and IRS audit changes?

## The method, step by step

1. **Determine both filing obligations.** Incorporated/qualified entities generally continue annual filing even if inactive. Ordinary corporate return is83-105;83-100 is the instructions, correcting the old README form label. Do not confuse corporate franchise with a franchised retail brand. [DOR filing/franchise FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions); [2025 booklet,2025-2026 filing cycle](https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf).
2. **Reconcile income independently.** Start with federal ordinary income and use83-122 state additions/deductions, not the individual AGI method. Retain a bridge for disallowed items, state income-tax deductions, related-party costs, asset differences and separately computed state NOLs. Apply state allocation/apportionment or prescribed direct accounting to the proper income, keeping the franchise factor separate. Do not invent a universal factor; obtain the industry-specific worksheet and support. [2025 instructions pp.7-9,2025-2026 filing cycle](https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf).
3. **Compute income tax.** On approved Mississippi taxable income T, tax=0.04xmin(max(T-5000,0),5000)+0.05xmax(T-10000,0). No minimum corporate income tax applies. Individual4% above $10,000 does not replace these corporate bands. [DOR income-tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions).
4. **Compute franchise separately.** Reconcile capital employed and the Mississippi allocation on83-110, including the statutory assessed-property floor and only allowable capital exclusions. Establish the authoritative final capital base before subtracting the$100,000 exemption. For2026 compute max(25,ceil(max(base-100000,0)/1000)x0.50). The fraction-of-$1,000 rule means round the units upward; do not use income apportionment automatically for capital. [SB2858§§3-4 amending27-13-5/7](https://billstatus.ls.state.ms.us/documents/2016/html/SB/2800-2899/SB2858SG.htm); [2025 instructions p.7](https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf); [DOR franchise computation FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions).
5. **Reconcile credits/payments and estimates.** Apply substantiated credits to the correct tax, then reconcile estimates separately by entity. Corporate income liability exceeding$200 triggers estimates. The opened2025-2026 filing cycle instructions require at least 90% of current income liability prepaid; verify final 2026 dates/installment procedure on the account before payment. Franchise tax is not automatically included in the income-estimate formula. [DOR estimates FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions); [2025 instructions pp.4-5](https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf).

### Rates, bands and thresholds

| 2026 item | Amount or rule | Authority |
| --- | --- | --- |
| Corporation first $5,000 taxable income | 0% | [DOR income-tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions) |
| Next$5,000 | 4% | [DOR income-tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions) |
| Above$10,000 | 5% | [DOR income-tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions) |
| Franchise rate | $0.50 per$1,000 or fraction over$100,000, minimum$25 | [DOR 2026 franchise paragraph](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions); [27-13-5/7 amendment](https://billstatus.ls.state.ms.us/documents/2016/html/SB/2800-2899/SB2858SG.htm) |
| Income estimate trigger | Annual liability exceeds $200 | [DOR estimates FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions) |

## Worked cases

### Ordinary taxable income and capital

Assume $100,000 approved Mississippi taxable income and $500,000 established Mississippi franchise capital after all capital allocation/floor work. Income tax=$200+$4,500=$4,700. Franchise units=400 and tax=$200. Total before credits/payments=$4,900. This does not assert that the two tax bases are interchangeable.

```oa-check
name: MS ordinary corporation income and franchise
inputs:
  taxable_income: 100000
  capital_base: 500000
steps:
  - income_tax: min(max(taxable_income - 5000, 0), 5000) * 0.04 + max(taxable_income - 10000, 0) * 0.05
  - franchise: max(25, ceil(max(capital_base - 100000, 0) / 1000) * 0.50)
  - combined: income_tax + franchise
expected:
  income_tax: 4700
  franchise: 200
  combined: 4900
```

### A fractional capital unit and minimum

Assume no taxable income, no exemption from franchise and established capital of$101,001. Two fractional/full units at$0.50 produce$1, so the$25 minimum controls. Inactive/loss status alone does not cancel the filing or minimum.

```oa-check
name: MS franchise fractional unit minimum
inputs:
  capital_base: 101001
steps:
  - units: ceil(max(capital_base - 100000, 0) / 1000)
  - franchise: max(25, units * 0.50)
expected:
  units: 2
  franchise: 25
```

## When to refuse or refer

Refer capital exclusions/assessed floor disputes, special industries, combined group, S/PTE, NOLs, asset basis and incentives. Do not apply the individual income rate, announce2026 franchise repeal, or compute a multistate base without the correct schedules.

## Filing and payment

C-corporation income/franchise return and payment are generally due the fifteenth day of the fourth month after year end. Extensions affect filing, not payment; DOR accepts federal extension in lieu where no tax liability exists at the original due date, otherwise use the proper Mississippi extension/payment process. Pay through TAP and retain proof. [DOR due-date/extension FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions).

The **2025-2026 filing cycle** booklet maps83-105 summary,83-110 franchise capital,83-122 income reconciliation,83-125 ordinary apportionment,83-150 nonbusiness allocation and83-155 NOL/capital-loss support. Final2026 form lines and precise estimate due-date interpretation are held pending; the booklet's phrase “after year end” in the estimate list should not be silently converted into a payment schedule without current clarification. [2025 instructions pp.4-9](https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf).

## Completion checklist

Confirm both taxes/period/entity, reconcile federal income, document the correct allocation/factor, establish capital and assessed floor, apply2026 franchise rate/minimum, reconcile credits/payments and verify the actual filing/estimate calendar.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DOR business FAQ; read for for all corporate income/franchise bands,2026 franchise paragraph, minimum, filing/extension/estimates. | https://www.dor.ms.gov/business/business-tax-frequently-asked-questions | 2026-11-13 |
| 2016 SB2858 final text; read for for complete27-13-5/7 capital/exemption/rate/minimum phase-out and repeal neighbours. | https://billstatus.ls.state.ms.us/documents/2016/html/SB/2800-2899/SB2858SG.htm | 2026-11-13 |
| 2025 Form 83-100 instructions; read for for pp.3-9 filing, current statutory phase-out, tax bases/factors and estimates;2025-2026 filing cycle. | https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf | 2026-11-13 |
| HB1§1; read for for corporate versus individual rate distinction in27-7-5 and neighbouring rate years. | https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm | 2026-11-13 |

Not yet confirmed: final 2026 return lines, exact current estimate installment schedule, specialized capital exclusions/assessed-value floor applications, state NOL/asset conformity and industry/group/election computations. Current DOR 2026 franchise paragraph and current corporate bands are verified; dated2025-2026 filing cycle form instructions are not represented as final 2026 forms.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ms-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ms-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
