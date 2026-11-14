---
name: bd-einvoice
description: "Bangladesh 2026 prescribed VAT invoice evidence and EFD/SDC scope triage; distinguish Mushak documents from income-tax e-Return and retain bank remittance evidence separately."
version: 1.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: e-invoicing
type: filing-howto
---

# Bangladesh VAT invoices and fiscal-device scope v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Registered/enlisted businesses preparing invoice evidence and small operators checking whether the VAT/device regime applies. This is not a universal income-tax e-invoicing mandate or an exemption for every unregistered freelancer.

## Ask the client first

- Activity, legal form, BIN/enlistment certificate and actual registration duty.
- Invoice/supply date, customer/supplier identity, taxable value and applicable rate source.
- Any EFD/SDC notification covering the activity/location.
- Export/remittance and bank evidence, adjustments and prior invoice references.

## The method, step by step

1. Use [VAT](bangladesh-vat.md) to establish registration and supply treatment first. Section 51 requires the registered/enlisted person to issue the prescribed invoice by the relevant tax time; do not presume a non-registered operator has no duty if it should have registered (https://bdlaws.minlaw.gov.bd/act-1106/section-42347.html).
2. VAT Rules 40 prescribes Mushak/VAT-6.3 for a registered person's supply. Retain the date/time, supplier identity/address/BIN, applicable purchaser information, description, value excluding VAT, rate/tax and supporting references. The old Mushak-11 references in the VAT workflow are not the current form identified by these Rules (https://nbr.gov.bd/uploads/rules/Authentic_English_Text_VAT_Rules_2016.pdf).
3. Link credit/debit notes to the original invoice under section 52 and the prescribed adjustment documents in Rule 40. Keep purchase/sale registers and return reconciliation; a bank transfer alone does not establish eligible input credit (https://bdlaws.minlaw.gov.bd/act-1106/section-42348.html).
4. Check the actual current EFD/SDC category/location notification before deciding whether a fiscal device, sales-data controller or approved software is required. Do not tell a notified in-scope business to skip it, or claim a universal mandate without the notification.
5. A non-VAT operator must keep a proper commercial invoice and tax records appropriate to its activity. Check registration independently; an ordinary commercial invoice must not impersonate a VAT invoice or claim a BIN that does not exist. Foreign receipts also need remittance/encashment evidence; a certificate does not replace the applicable invoice.
6. Income-tax filing uses the NBR e-Return workflow, separate from fiscal invoicing. VAT Rules 47 identifies 9.1 and 9.2 return forms; the current [VAT](bangladesh-vat.md) skill owns periods/deadlines. Retain invoices, device records where applicable, adjustment references and filing acknowledgements.

## Worked cases

### Invoice total agrees with its tax breakdown

Illustrative correctly classified invoice net 100,000 plus evidenced VAT 15,000 equals gross 115,000. These are example inputs from the assumed invoice, not a rate determination from this file.

```oa-check
name: Invoice total reconciliation
inputs:
  net: 100000
  invoice_vat: 15000
steps:
  - gross: net + invoice_vat
expected:
  gross: 115000
```

### Credit-note reconciliation

Illustrative original invoice gross 115,000; matched credit note net 10,000 and VAT 1,500 totals 11,500, leaving 103,500 gross after adjustment. Legal entitlement, note fields and tax period must also be established; do not net an unrelated payment against the invoice.

```oa-check
name: Matched invoice and credit note
inputs:
  original_gross: 115000
  credit_net: 10000
  credit_vat: 1500
steps:
  - credit_gross: credit_net + credit_vat
  - adjusted_gross: original_gross - credit_gross
expected:
  credit_gross: 11500
  adjusted_gross: 103500
```

## When to refuse or refer

Refer missing BIN/registration duty, unresolved rate/supply, EFD/SDC scope, nonstandard credit/debit notes and unverified software requirements. Do not promise input credit or treat the income-tax e-Return as an invoice.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for VAT Act section 51 invoice obligation | https://bdlaws.minlaw.gov.bd/act-1106/section-42347.html | 2026-11-14 |
| Read for VAT Rules 40 invoice information and adjustment documents; 47 return forms | https://nbr.gov.bd/uploads/rules/Authentic_English_Text_VAT_Rules_2016.pdf | 2026-11-14 |
| Read for VAT Act section 52 credit/debit notes | https://bdlaws.minlaw.gov.bd/act-1106/section-42348.html | 2026-11-14 |
| Read for VAT Act section 46 documentary and other input-credit conditions | https://bdlaws.minlaw.gov.bd/act-1106/section-42342.html | 2026-11-14 |

Not yet confirmed: Current EFD/SDC category/location notifications, device/software approvals, any activity-specific commercial invoice/TIN mandate and live return fields. No universal income-tax e-invoicing duty or blanket freelancer exemption is asserted.
