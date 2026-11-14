---
name: bd-bookkeeping
description: "Bangladesh 2026 records workflow for sole traders and small businesses: income, expenses, bank and remittance evidence, VAT registers, asset records and statutory retention by entity type."
version: 1.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: bookkeeping
type: situation-rules
---

# Bangladesh bookkeeping and evidence v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare accounting evidence and working papers for Bangladesh individuals and small businesses. Company statutory accounts and VAT returns are handled by their linked skills. Currency: BDT. A bank statement does not replace an invoice or establish tax relief.

## Ask the client first

- Legal entity and accounting/income period.
- All bank/platform accounts and domestic/export activities.
- VAT registration/enlistment and staff.
- Prior returns, asset register, invoices, remittance certificates and open disputes.

## The method, step by step

### Retention and evidence card

| Rule and condition | Retention period / amount | Official source |
|---|---|---|
| Non-company taxpayer records under new section 72A | Retain 6 years; analog, permitted digital form or both | Finance Act section 58: https://bdlaws.minlaw.gov.bd/act-1725/section-59432.html |
| Company books and related vouchers | At least 12 years before current year, or all earlier years if younger | Companies Act section 181(5): https://bdlaws.minlaw.gov.bd/act-788/section-33570.html |

1. Keep client invoices, platform statements (including Upwork/Fiverr), receipts, bank credits and the full statements for every BDT/foreign-currency account. Keep contracts and remittance/encashment certificates for foreign receipts; reconcile gross sales, platform charges, bank charges, exchange differences and net credits. Do not discard certificates or merge domestic/export records.
2. Record vendor bills, rent/utilities, internet, software subscriptions and other claimed business costs. Separate personal expenses, drawings and equipment/capital expenditure; maintain the asset/depreciation register. No fixed depreciation rate is supplied here.
3. Retain prior returns, TIN, trade licence, tax-payment records and withholding certificates. Relief/incentive evidence must match the actual scheme. A remittance certificate is evidence, not proof that an export incentive has been approved.
4. VAT-registered/enlisted persons maintain VAT-6.1 purchase and VAT-6.2 sale records, or VAT-6.2.1 for goods resold without processing, and issue the applicable invoice. Rule 40(1)(bbb) prescribes the ERP records; SRO 125 adds VAT-6.3 to the specified VAT-6.1/6.2/6.2.1 ERP records, distinct from device-notification scope. Read [VAT](bangladesh-vat.md) and [e-invoicing](bd-einvoice.md) for Mushak records, invoice content, software/device applicability and return handling. Do not use an ordinary invoice or bank statement as a substitute for compliant VAT evidence (https://nbr.gov.bd/uploads/rules/Authentic_English_Text_VAT_Rules_2016.pdf).
5. Tie each working-paper total to source documents and keep a list of unmatched receipts and unsupported expenses. Refer [financial statements](bd-financial-statements.md) for company accounts, audit and filing. Do not destroy records needed for an outstanding proceeding merely because a baseline period has elapsed.

## Worked cases

### Remittance reconciliation

Illustrative software invoices total 1,000,000; platform fees 50,000; bank credits 950,000. Difference is 0 after reconciling fees. This establishes document reconciliation, not automatic exemption or incentive entitlement.

```oa-check
name: Gross export invoices reconcile through platform fees
inputs:
  invoices: 1000000
  fees: 50000
  bank_credits: 950000
steps:
  - expected_bank: invoices - fees
  - unmatched: expected_bank - bank_credits
expected:
  expected_bank: 950000
  unmatched: 0
```

### Edge: equipment is separate from ordinary spending

Illustrative records contain cash receipts 600,000, ordinary supported costs 100,000, equipment 120,000 and proprietor drawings 80,000. Cash surplus is 300,000; profit before depreciation is 500,000. The equipment and drawings are not automatically deducted from profit. Depreciation and tax adjustments require the applicable rule.

```oa-check
name: Cash surplus is not profit after personal drawings and equipment
inputs:
  receipts: 600000
  ordinary_costs: 100000
  equipment: 120000
  drawings: 80000
steps:
  - cash_surplus: receipts - ordinary_costs - equipment - drawings
  - profit_before_depreciation: receipts - ordinary_costs
expected:
  cash_surplus: 300000
  profit_before_depreciation: 500000
```

## When to refuse or refer

Do not approve an unsupported deduction, credit or incentive. Refer disputed remittance/foreign-exchange treatment, missing invoices, destroyed records, mixed personal/business costs and unverified depreciation or retention exceptions.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for section 72A non-company retention and permitted storage forms | https://bdlaws.minlaw.gov.bd/act-1725/section-59432.html | 2026-11-14 |
| Read for Companies Act section 181 books, vouchers and company retention | https://bdlaws.minlaw.gov.bd/act-788/section-33570.html | 2026-11-14 |
| Read for VAT Rules 40-41 prescribed purchase/sale registers, ERP and invoices | https://nbr.gov.bd/uploads/rules/Authentic_English_Text_VAT_Rules_2016.pdf | 2026-11-14 |

| Read for SRO 125 item 10 adding VAT-6.3 to ERP records, effective 1 July 2026 | https://nbr.gov.bd/uploads/sros/VAT_SRO-125.pdf | 2026-11-14 |

Not yet confirmed: Any longer case-specific preservation order, asset-specific depreciation, export cash-incentive qualification, and current device-category notifications. The old unqualified retention estimate is replaced by entity-specific statutory rules.
