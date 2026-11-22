---
name: us-gaap-asc230-cash-flow-statement
description: "Draft US GAAP cash-flow working paper for operating/investing/financing classification, direct and indirect reconciliation, debt settlements, noncash transactions and restricted cash. Cites named FASB amendments and preserves current cash-equivalent and specialized classification source holds. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 230 Statement of Cash Flows (ASU 2016-15 and ASU 2016-18 amendment basis)"
effective_date: 2018-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP cash flow statement : ASC 230 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This job assembles a financial-statement working paper, not a cash forecast or bank reconciliation alone. The date key 2018-12-16 marks the first possible fiscal-year start after 15 December 2018 for ASU 2016-18's non-PBE annual transition; its non-PBE interims begin within fiscal years after 15 December 2019, and PBEs' annual/interim years begin after 15 December 2017. Application is retrospective; permitted early adoption has its annual-beginning condition. [ASU 2016-18, transition summary and 230-10-65-3](https://storage.fasb.org/ASU%202016-18.pdf).

## Ask the client first

- Comparative balance sheets, income statement, trial balances and complete cash/bank reconciliations.
- Definition/policy for cash equivalents and a line-by-line register of restricted balances and restrictions.
- Cash transaction detail, debt/lease/equity rollforwards, capital expenditure and disposal records.
- Acquisitions/disposals, foreign-currency movements, noncash transactions and changes in reporting perimeter.
- Taxes/interest paid, unpaid accruals, debt settlement fees/premiums and insurance/contingent receipts.
- Direct or indirect presentation, PBE status, reporting period and actual amendment adoption.

## The method, step by step

1. **Fix the cash perimeter.** Under the read amendment, the cash-flow reconciliation includes cash, cash equivalents and amounts generally described as restricted cash/equivalents. Reconcile the beginning/end totals to all relevant balance-sheet lines; where several lines hold these balances, supply the required face/note reconciliation and explain the restrictions. The amendment does not itself define every cash-equivalent or restricted-cash boundary. [ASU 2016-18, 230-10-45-4/-45-24 and -50-7/-50-8](https://storage.fasb.org/ASU%202016-18.pdf).
2. **Remove internal transfers and identify noncash activity.** Transfers within that cash perimeter are not operating, investing or financing flows. Keep noncash investing/financing activity outside cash totals and prepare its separate disclosure; examples in the read guidance include converting debt to equity and obtaining an asset through directly related debt. Do not create fictitious cash inflows/outflows to balance a journal. [ASU 2016-18, 230-10-45-5](https://storage.fasb.org/ASU%202016-18.pdf); [ASU 2016-15, 230-10-50-4](https://storage.fasb.org/ASU%202016-15.pdf).
3. **Classify by the actual transaction.** The read operating rules include payments to suppliers/employees, taxes and interest; the direct-method guidance includes customer receipts and ordinary interest/dividend receipts, with the stated special exceptions. Cash purchases of productive assets are investing, while principal repayment and qualifying debt issue/extinguishment costs are financing. Respect the seller-financing and capitalized-interest distinctions rather than classifying by ledger caption alone. [ASU 2016-15, 230-10-45-13, -45-15, -45-17 and -45-25](https://storage.fasb.org/ASU%202016-15.pdf).
4. **Prepare the chosen operating reconciliation.** For direct presentation, classify actual cash receipts/payments and total the operating classes. For indirect presentation, start from net income, adjust noncash and investing/financing income effects, and analyze operating-asset/liability movements net of acquisition/disposal/noncash/FX changes. The official example separately adjusts depreciation, gains and working-capital movements; a raw two-balance-sheet subtraction is not sufficient evidence of cash. Preserve the gain removal and full disposal proceeds in their separate places. [ASU 2016-18, 230-10-55-13 illustrative indirect statement](https://storage.fasb.org/ASU%202016-18.pdf).
5. **Split debt settlement correctly.** The read ASU 2016-15 treats directly related prepayment/extinguishment costs as financing, excluding accrued interest. For zero-coupon or insignificant-coupon debt, it separately treats accreted interest at settlement as operating and principal as financing. Do not apply that accreted-interest split to all debt instruments indiscriminately. [ASU 2016-15, 230-10-45-15(g), -45-15(b) and -45-17(d)](https://storage.fasb.org/ASU%202016-15.pdf).
6. **Reconcile and review.** Sum operating, investing and financing flows and separately supported exchange-rate effects to explain the cash-perimeter movement. Trace every line to transaction evidence and clear all differences. For mixed receipts/payments apply specific guidance first, then identifiable components by their underlying nature before a predominance analysis. Use a suspense list for unresolved classifications rather than an unexplained plug. [ASU 2016-18, 230-10-45-24 and illustrative statement](https://storage.fasb.org/ASU%202016-18.pdf); [ASU 2016-15, 230-10-45-22/-45-22A](https://storage.fasb.org/ASU%202016-15.pdf).

## Worked cases

All monetary values are hypothetical. Assume cleared scope/current rules, ordinary transactions without the special exceptions and no FX effect.

**Direct cash flow and restricted-cash bridge.** Customer receipts $120,000, supplier/employee payments $80,000, interest paid $5,000 and tax paid $10,000 give operating cash $25,000. Immediate cash equipment purchases are $20,000 investing outflow and principal repayment $3,000 financing outflow. Beginning unrestricted cash $7,000 plus restricted cash $3,000 totals $10,000; ending $7,000 plus $5,000 totals $12,000. The $2,000 net increase reconciles. A $2,000 internal transfer into the restricted account is not an additional outflow.

```oa-check
name: Direct statement reconciles total cash including restricted balances
inputs:
  customer_receipts: 120000
  suppliers_employees_paid: 80000
  interest_paid: 5000
  tax_paid: 10000
  cash_equipment_purchase: 20000
  principal_repaid: 3000
  opening_cash: 7000
  opening_restricted: 3000
  closing_cash: 7000
  closing_restricted: 5000
steps:
  - operating: customer_receipts - suppliers_employees_paid - interest_paid - tax_paid
  - investing: -cash_equipment_purchase
  - financing: -principal_repaid
  - net_cash_change: operating + investing + financing
  - opening_total: opening_cash + opening_restricted
  - closing_total: closing_cash + closing_restricted
  - reconciliation_difference: closing_total - opening_total - net_cash_change
expected:
  operating: 25000
  investing: -20000
  financing: -3000
  net_cash_change: 2000
  opening_total: 10000
  closing_total: 12000
  reconciliation_difference: 0
```

**Debt prepayment separates interest.** On ordinary debt, cash settlement is $50,000 principal, $3,000 directly related prepayment premium and $2,000 accrued interest, with no other component. Financing outflow is $53,000 and operating outflow $2,000, totaling $55,000. No $55,000 financing lump sum and no duplicate premium operating outflow is appropriate under this amendment-basis fact pattern. This case does not apply the different zero-/insignificant-coupon accretion rule.

```oa-check
name: Debt prepayment premium versus accrued interest classification
inputs:
  principal: 50000
  directly_related_premium: 3000
  accrued_interest: 2000
steps:
  - financing_outflow: principal + directly_related_premium
  - operating_outflow: accrued_interest
  - total_cash_paid: financing_outflow + operating_outflow
expected:
  financing_outflow: 53000
  operating_outflow: 2000
  total_cash_paid: 55000
```

## When to refuse or refer

Hold unreconciled cash, undefined cash equivalents, missing restriction evidence or unsupported noncash/FX/acquisition adjustments. Refer complex factoring/securitization, contingent consideration, derivatives, insurance receipts, leases and entity-specific exceptions before applying the ordinary classification rules. Cash-flow presentation does not repair a wrong recognition or measurement entry.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2016-18](https://storage.fasb.org/ASU%202016-18.pdf) | Summary/transition; 230-10-45-4/-45-5/-45-24; -50-7/-50-8; illustrative -55-12A/-55-13 cash bridge and indirect statement. | 2026-11-21 and 2026-11-22 (illustrative statement) |
| [ASU 2016-15](https://storage.fasb.org/ASU%202016-15.pdf) | Issues 1/2; 230-10-45-13/-45-15/-45-17/-45-25; -50-4; -45-22/-45-22A mixed classification. Scope limited to these passages. | 2026-11-21 and 2026-11-22 (noncash/mixed passages) |

**Not yet confirmed:** Complete current ASC 230, cash-equivalent/restricted-cash definitions and policies, netting/gross exceptions, complete specialized classifications, full direct/indirect disclosure requirements and intervening-amendment applicability. No proposed future cash-equivalent amendment is treated as enacted guidance. Official current ASC attempt on 2026-11-21 stopped at CAPTCHA/terms. These source gaps remain non-usable holds.
