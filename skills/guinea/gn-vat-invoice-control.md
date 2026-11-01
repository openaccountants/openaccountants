---
name: gn-vat-invoice-control
description: "Guinea VAT invoice-field and arithmetic control using the full March 2026 replacement of CGI article 383 VI. Use it to check the sixteen fields, their conditional branches, source identifiers and totals after independently establishing invoice duty and the governing version, including any October rectification effect. Registration, taxability, the correct rate and input-credit entitlement are separate jobs. The examples assume that the March version governs and use independently validated tax amounts rather than establishing a VAT rate. If currentness is unconfirmed, produce hypothetical March-text analysis only and stop before a live compliance conclusion or a legally required correction request. Filing, sanctions and wider VAT coverage remain partial."
jurisdiction: GN
category: international
tax_year: 2026
tax_year_notes: "Enacted 31 March 2026 replacement text; earlier periods and October rectification status unconfirmed."
tier: 2
last_updated: 2026-11-01
version: 1.1
---

# Guinea VAT invoice control v1.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Guinea.

## Who this applies to

**Governing-version prerequisite.** Before using this workflow for an actual period or invoice, establish that the March replacement text governs it, including the promulgation, effective date and effect of any October rectification. If that is not confirmed, label every result **hypothetical March-text analysis only** and stop before a live tax/compliance conclusion, filing/payment decision or legally required invoice-correction request. The source gap does not authorise assuming the March text remains unchanged.

Use to check a Guinea VAT invoice governed by CGI 383 VI after independently establishing that the invoicing duty applies. Article 13 of Law L/2026/010/CNT of 31 March 2026 replaces the full list of mandatory invoice fields. This Guide checks those fields and reconciles amounts; it does not determine VAT registration, taxability, the correct rate or input-credit entitlement. The official bundle contains the signed promulgation decree. Periods before the replacement and the final effect of the October rectifying bill remain unresolved. [Law art. 13, decree arts. 1–2, PDF pp. 20–21,27](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf).

## Rates, bands and thresholds

The list has sixteen numbered requirements, some conditional. There is no monetary exemption or tax-rate rule in the opened replacement paragraph. Mark each field **present**, **missing**, or **not applicable with documented reason**. Do not count a conditional field as mandatory for every invoice. [CGI 383 VI](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20).

| Statutory item | Required information and condition | Official source |
|---|---|---|
| 1° | Supplier name and address | [CGI 383 VI 1°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 2° | Customer or recipient name and address | [CGI 383 VI 2°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 3° | Supplier NIF and VAT registration key | [CGI 383 VI 3°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 4° | For services where the recipient is liable under CGI 373 bis II: recipient NIF and VAT registration key | [CGI 383 VI 4°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 5° | Where the customer is liable: reference to CGI 373 bis stating that customer liability | [CGI 383 VI 5°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 6° | Where the liable person is a fiscal representative under CGI 373 quinquies: its NIF, VAT registration key, name and address | [CGI 383 VI 6°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 7° | Unique invoice number based on a chronological, continuous sequence | [CGI 383 VI 7°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 8° | Invoice date | [CGI 383 VI 8°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 9° | If different from invoice date: date of supply/service and date an advance is paid | [CGI 383 VI 9°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 10° | For each item/service: quantity, precise description, unit price excluding tax and legally applicable VAT rate, or the Code provision exempting the supply | [CGI 383 VI 10°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 11° | Discounts, rebates or cash discounts acquired and quantifiable at the transaction and directly linked to it | [CGI 383 VI 11°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 12° | Total VAT due on the transaction | [CGI 383 VI 12°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 13° | Total excluding tax | [CGI 383 VI 13°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20) |
| 14° | Total including all taxes | [CGI 383 VI 14°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| 15° | If the taxpayer elected VAT on debits: exact wording “TVA d’après les débits - article 366 bis du CGI” | [CGI 383 VI 15°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| 16° | If the margin regime applies: exact wording “TVA sur marge - article 410 bis du CGI” | [CGI 383 VI 16°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |

## The base

0. Establish the governing-version prerequisite above and record the evidence for the actual period or invoice, including any October effect. If unresolved, stop live use; the following steps may only illustrate the March text hypothetically.
1. Obtain the invoice, contract/order, supply or advance evidence, supplier registration details and independently established VAT treatment. Check invoice date and supply/advance dates against the source records.
2. Check items 1°–3° and 7°–14° line by line, applying the date and exemption conditions in the table. Match the unique number against the supplier's chronological sequence where the records are available; a number printed on one invoice cannot prove continuity.
3. Establish whether customer liability or a fiscal representative applies from a separately verified conclusion. Apply 4°–6° only when their stated conditions hold. The cross-referenced articles are not reproduced by this amendment, so this Guide cannot decide their scope.
4. If an evidenced debit-basis election or margin regime applies, check the exact respective wording in 15° or 16°. Do not elect a regime merely by printing its wording.
5. Reconcile quantities and unit prices to the net lines, directly related discounts to the transaction, the separately validated VAT amounts to total VAT, and net plus tax amounts to the printed tax-inclusive total. Use the statutory totals in 12°–14°; arithmetic agreement does not prove the rate or tax treatment is correct. [CGI 383 VI](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20).
6. Produce a discrepancy list with the field, evidence, invoice value, expected value and correction requested. Keep the original invoice and correction correspondence in the workpaper; no statutory retention duration is asserted here. An internally corrected spreadsheet does not correct the supplier's invoice.

## Deadlines and filing

This is an invoice-review job, not a VAT return submission. Route a missing mandatory field or arithmetic mismatch for correction before approving the document through this workflow. No statutory invoice-issue deadline, correction instrument, return due date, portal/form/box, submission receipt or payment reference has been verified from article 383 VI. Do not invent those details from the field list.

## Penalties and interest

The opened amendment sets invoice contents. It does not establish an invoice penalty, interest rate or automatic input-credit refusal. Record the defect without asserting an unverified sanction or deduction consequence.

## Cross-border points

Items 4°–6° expressly address recipient liability and fiscal representatives, with references to CGI 373 bis and 373 quinquies. Check the required identifiers and liability reference when a separately verified cross-border conclusion triggers them. This list alone does not prove that every imported service is reverse charged or every foreign supplier must appoint a representative. [CGI 383 VI 4°–6°](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=20).

## Two worked examples that recompute

Both cases assume the March version governs the relevant invoice. Without confirmed governing-version evidence, they are hypothetical arithmetic illustrations only and do not require a live invoice correction.

First, two lines have net amounts of GNF 20,000,000 and GNF 30,000,000. The independently validated tax amounts supplied to this control are GNF 3,600,000 and GNF 5,400,000. Net total is GNF 50,000,000, total VAT is GNF 9,000,000 and gross total is GNF 59,000,000. The example does not establish a statutory VAT rate.

```oa-check
name: Invoice totals reconcile from separately validated amounts
inputs:
  line_one_net: 20000000
  line_two_net: 30000000
  validated_line_one_vat: 3600000
  validated_line_two_vat: 5400000
steps:
  - total_net: line_one_net + line_two_net
  - total_vat: validated_line_one_vat + validated_line_two_vat
  - total_gross: total_net + total_vat
expected:
  total_net: 50000000
  total_vat: 9000000
  total_gross: 59000000
```

Second, a draft has independently validated net of GNF 40,000,000 and VAT of GNF 7,200,000, but printed gross of GNF 48,000,000. The correct arithmetic gross is GNF 47,200,000, leaving a GNF 800,000 discrepancy. The decision is to return the invoice for correction; it does not pass the control merely because all field labels are printed. The tax amounts are inputs, not a rate conclusion.

```oa-check
name: Return mismatched invoice for correction
inputs:
  validated_net: 40000000
  validated_vat: 7200000
  printed_gross: 48000000
steps:
  - expected_gross: validated_net + validated_vat
  - discrepancy: abs(printed_gross - expected_gross)
expected:
  expected_gross: 47200000
  discrepancy: 800000
```

## Ask the client first

Obtain evidence establishing the governing version for the invoice, including any October effect; the invoice and supporting supply/advance documents; supplier and customer identifiers; the separately verified registration/tax treatment and rate; any recipient-liability or representative conclusion; any debit-basis election or margin-regime evidence; and the invoice sequence and correction history.

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [DGB official enacted 2026 law bundle](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf), scanned law pp. 19–24, especially art. 13 replacing all sixteen items of CGI 383 VI on pp. 20–21; signed promulgation decree arts. 1–2 on p. 27, corroborated on p. 28. Invoice pages and signed decree visually inspected. | 2026-11-01 |

**Not yet confirmed:** underlying CGI 383 I–V and VII+, registration threshold, applicable VAT rates/exemptions/zero-rating and taxable base, scope of recipient liability and fiscal representation, debit/margin eligibility and elections, input deductions/refunds, issue/correction deadlines and instruments, retention duration, penalties/interest, return/payment portal/forms/boxes/deadlines/receipts, periods before the 31 March replacement and final promulgated status/effect of the October 2026 rectifying bill. The six legacy Guides remain historical and do not resolve these current-year gaps.
