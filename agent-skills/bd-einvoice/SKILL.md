---
name: bd-einvoice
description: "Bangladesh 2026 prescribed VAT invoice evidence and EFD/SDC scope triage; distinguish Mushak documents from income-tax e-Return and retain bank remittance evidence separately."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bd-einvoice"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
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
2. Registered persons issue Mushak/VAT-6.3 under Rule 40(1)(c), electronically or in hard copy after the 2026 amendment. Keep actual issue date/time; supplier name/address/BIN; purchaser name/address/BIN where applicable when the supply value exceeds BDT 25,000; description, quantity, supply date/time and transport nature/number; value excluding VAT, rate, VAT and gross amount. The purchaser-information threshold does not waive separate section 46 input-credit evidence requirements. Use fiscal-year consecutive serials and place-specific serials where required, at least 2 copies with the original to the purchaser (accompanying transported goods) and retained copy, plus any Board-required information. Rule 40(1)(c)(i), as amended in 2026, allows the specified MFS online notification/statement as invoice in its covered case; it does not turn every bank credit into a VAT invoice. Sources: Rule 40(1)(c), https://nbr.gov.bd/uploads/rules/Authentic_English_Text_VAT_Rules_2016.pdf; SRO 125 item 10, https://nbr.gov.bd/uploads/sros/VAT_SRO-125.pdf.
3. Keep VAT-6.1 purchase and VAT-6.2 sale registers; VAT-6.2.1 is the combined purchase/sale record for goods resold without processing. Rule 40(1)(bbb) requires the specified records through ERP software; the 2026 amendment adds VAT-6.3 to VAT-6.1, 6.2 and 6.2.1. This sourced ERP obligation is distinct from EFD/SDC device-category notifications. The old Mushak-11 reference is not the current prescribed invoice. Rules 40-41 also prescribe an enlisted turnover-tax person's VAT-6.9 invoice and purchase/sale records, with serial/copy requirements (same Rules and SRO).
4. Link VAT-6.7 credit and VAT-6.8 debit notes to the original invoice and section 52's contents; incomplete/defective evidence does not support credit under Rule 40(3). VAT-6.4 records contractual manufacturing, with a separate VAT-6.3 for the manufacturing fee; VAT-6.5 covers branch/warehouse transfers. VAT-6.6 is the withholding certificate; VAT-6.10 is purchase/sale information under Rule 42, not that certificate. Refer substantive transfer/VDS liabilities to a specialist, while retaining these correct document jobs (https://bdlaws.minlaw.gov.bd/act-1106/section-42348.html; Rules 40-42 above).
5. Check the actual current EFD/SDC category/location notification before deciding whether a fiscal device or sales-data controller is required. Keep this device check separate from the confirmed ERP records above. Do not tell a notified in-scope business to skip it, or claim a universal device mandate without the notification.
6. A non-VAT operator must keep a proper commercial invoice and tax records appropriate to its activity. Check registration independently; an ordinary commercial invoice must not impersonate a VAT invoice or claim a BIN that does not exist. Foreign receipts also need remittance/encashment evidence; a certificate does not replace the applicable invoice.
7. Income-tax filing uses the NBR e-Return workflow, separate from fiscal invoicing. Current Rule 47, replaced by SRO 125 item 11 effective 1 July 2026, uses VAT-9.1 for registered manufacturers/service providers, VAT-9.1.1 for registered traders and VAT-9.2 for enlisted turnover-tax persons. The current [VAT](bangladesh-vat.md) skill owns periods/deadlines and the later statute/form-period inconsistency. Retain invoices, ERP/device records as applicable, adjustments and filing acknowledgements.

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

Refer missing BIN/registration duty, unresolved rate/supply, EFD/SDC scope, nonstandard credit/debit notes and unverified device approvals. Do not promise input credit or treat the income-tax e-Return as an invoice.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for VAT Act section 51 invoice obligation | https://bdlaws.minlaw.gov.bd/act-1106/section-42347.html | 2026-11-14 |
| Read for VAT Rules 40-42 invoice particulars, registers/ERP, copies and document jobs; old Rule 47 read with its 2026 replacement | https://nbr.gov.bd/uploads/rules/Authentic_English_Text_VAT_Rules_2016.pdf | 2026-11-14 |
| Read for SRO 125 items 10-11: ERP, electronic/hard-copy/MFS invoice amendments, current return populations and commencement | https://nbr.gov.bd/uploads/sros/VAT_SRO-125.pdf | 2026-11-14 |
| Read for VAT Act section 52 credit/debit notes | https://bdlaws.minlaw.gov.bd/act-1106/section-42348.html | 2026-11-14 |
| Read for VAT Act section 46 documentary and other input-credit conditions | https://bdlaws.minlaw.gov.bd/act-1106/section-42342.html | 2026-11-14 |

Not yet confirmed: Current EFD/SDC category/location notifications, device approvals, any activity-specific commercial invoice/TIN mandate and live return fields. No universal income-tax e-invoicing duty or blanket freelancer exemption is asserted.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bd-einvoice` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bd-einvoice. If neither is available, confirm every figure against the official source pages cited above before relying on it.
