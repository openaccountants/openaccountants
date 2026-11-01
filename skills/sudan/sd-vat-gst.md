---
name: sd-vat-gst
description: >
  Prepare Sudan VAT registration and monthly return workpapers for 2026 intake using the official Arabic Act, the 2017 regulations and identified amendments actually opened. Covers ordinary traders, manufacturers, importers, exporters and service businesses, with invoices, input attribution, nil returns, adjustments and export refunds. Match Sudan VAT, value added tax, Form 1 registration, Form 3 return, import services and ضريبة القيمة المضافة requests. Historical rate cells and the unconfirmed current turnover threshold are explicitly separated from filing authority. Map source documents to the actual annexed form while checking current instructions before use. This Guide stops before submission where the enacted amendment chain or live procedure remains unresolved.
version: 0.3
jurisdiction: SD
tax_year: 2026
last_updated: 2026-11-01
authored_by: Ahmed Hassan
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
---

# Sudan VAT registration and monthly workpapers v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Taxable goods, services and works in Sudan, imports and exports, including free-zone domestic-entry questions. The Arabic statutory images/OCR were read because the English PDF text encoding is unusable. A downloaded file is not current consolidation proof. Do not use the old SDG 1,200,000 threshold without its actual operative instrument.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| General historical rate | 17% recorded by the principal s.14 amendment footnote for the 2012 decision; later enacted chain remains unresolved. | [s.14 and amendment footnote, PDF12](https://tax.gov.sd/wp-content/uploads/2025/02/vat2001.pdf) |
| Telecommunications | 40% under signed 2022 amendment; confirm category and operative period. | [VAT Amendment 2022 s.2(a), PDF1 and attestation PDF2](https://tax.gov.sd/wp-content/uploads/2025/02/law40-42.pdf) |
| Tobacco/cigarette category | 40% under 2018 amendment, not a general VAT rate. | [VAT Amendment 2018 s.2, PDF1–2](https://tax.gov.sd/wp-content/uploads/2025/02/law13_14.pdf) |
| Exports | Zero rate requires qualifying export and evidence; a foreign customer alone is insufficient. | [s.14 and amendment footnote, PDF12](https://tax.gov.sd/wp-content/uploads/2025/02/vat2001.pdf) |
| Registration amount | unverified: current numeric compulsory turnover threshold. Importer/exporter rule is independent of size under reg.5. | [reg.5, PDF4](https://tax.gov.sd/wp-content/uploads/2025/02/vat_list.pdf) |
| Monthly filing | Form 3 within 15 days of month end, including nil returns, under the opened 2017 regulation 11; extension requires approval. | [reg.11, PDF9](https://tax.gov.sd/wp-content/uploads/2025/02/vat_list.pdf) |
| Voluntary cancellation wait | 2 years under reg.6, not a universal permission to cancel all registrations. | [reg.6, PDF4–5](https://tax.gov.sd/wp-content/uploads/2025/02/vat_list.pdf) |
| VAT records | 5 years following the end of the financial year of the entries under reg.10(5), PDF 9; cancellation records also have reg.8 conditions. Income-tax records have a separate rule. | [reg.10, PDF8–9](https://tax.gov.sd/wp-content/uploads/2025/02/vat_list.pdf) |

## The base

1. Classify each supply, tax point and category before selecting a rate; continuous services have an invoice-event provision. Exempt and zero-rated supplies are different. The reg.32 list has defined food/agricultural, financial, educational, medical, diplomatic/treaty and other exclusions; later revocations and product facts need checking.
2. Reconcile sales and imported/customs/free-zone supplies to s.12–15 and valuation provisions. Do not infer a universal customs-value formula or apply the old category-specific valuation bases to every supply.
3. Require valid supplier invoices or customs proof. Directly attribute taxable input first, exclude personal/exempt input, then allocate genuine mixed inputs using the reg.29 proportion. Carry unused eligible credit forward; it is not automatically a cash refund.
4. For returned goods, obtain actual return/refund and the numbered dated adjustment evidence. Correct errors on the next monthly return with supporting documents under reg.31.
5. For export refunds assemble written claim, invoice and customs proof. Export services need the customer/use/contract/payment conditions in reg.30. The source provides a conditional three-month response and a 24 month written-claim limit, not automatic quarterly refund approval.
6. A Sudan resident paying taxable services/works to a nonresident without a registered Sudan legal entity has the s.28(5) add-and-remit rule. Establish supply category and actual rate before posting; this is separate from income-tax withholding.

## Deadlines and filing

1. Registration: submit regulation 7 Form 1 to the local office; resolve missing information, obtain Form 2 certificate and display it at head office and branches. Notify changes within 30 days. Cancellation needs a written decision and separate stock/records treatment under reg.8.
2. Build monthly sales/purchase registers from reg.9 invoices and reg.10 records. Obtain the CURRENT official Form 3/portal instructions before submission. The actual 2017 annex PDF 30 identifies taxpayer, registration/TIN, office and return month; PDF 31 gives instructions.
3. On the historical annex PDF 32, sales lines 1–6 distinguish taxable supplies, telecom, taxable fixed assets, special-basis supplies, exempt supplies and exports. Purchases lines 7–14 distinguish imported/local supplies, fixed assets, special-basis items, taxable services/telecom/other and exempt imported/local items. Use the form's labels, not invented 40/30/5% boxes: its printed telecom rate is historical.
4. Reconcile total collected tax and eligible input, prior credit line 15, credit carried line 16 and amount payable line 17; lines 18–19 concern refunds and petroleum-company certificates. Do not populate a claim without its evidence. PDF 33 contains completion material; no live filing tested.
5. Check period, currency and 2022 Arabic-translation/electronic-return powers. File/pay through the confirmed local route only after the current law/form/date gate clears; retain submission acknowledgement and payment receipt.

## Penalties and interest

The Act and regulation 11 permit assessment and enforcement for nonfiling/incorrect returns; the current penalty regulations and amended amounts are unresolved. A percentage inferred from a stale form or a universal late fee is not approved. Preserve assessment notices and service dates for the actual appeal/payment rules.

## Cross-border points

Keep customs entry evidence and actual export proof. Domestic free-zone withdrawals are not automatically exempt. Imported services can trigger s.28(5); [cross-border](sd-cross-border-residence.md) separately handles income-tax source and withholding. No digital-service threshold, foreign-supplier simplified regime or investment exemption is established here.

## Two worked examples that recompute

### Ordinary taxable month, historical general rate

Assume only qualifying general-rate supplies under the opened 17% source-period rate, net sales 100,000 and fully documented eligible net purchases 40,000. Output 17,000 less input 6,800 gives 10,200. No historic rate is thereby approved for 2026.

```oa-check
name: VAT historical general-rate month
inputs:
  sales: 100000
  purchases: 40000
steps:
  - output: sales*0.17
  - input: purchases*0.17
  - payable: output-input
expected:
  output: 17000
  input: 6800
  payable: 10200
```

### Mixed input attribution decision

Assume shared input tax10,000, taxable output60,000 and total output100,000 under the applicable reg.29 proportion. Shared eligible tax6,000, disallowed4,000. Direct attribution would instead permit a wholly taxable-use input in full; do not allocate directly exempt input as shared.

```oa-check
name: Mixed versus directly taxable input
inputs:
  shared_tax: 10000
  taxable_output: 60000
  total_output: 100000
steps:
  - shared_allowed: shared_tax*taxable_output/total_output
  - shared_disallowed: shared_tax-shared_allowed
  - directly_taxable_allowed: shared_tax
expected:
  shared_allowed: 6000
  shared_disallowed: 4000
  directly_taxable_allowed: 10000
```

## Ask the client first

- Activity, products, customers, legal entity and actual supply/tax-point dates.
- Registration certificate, importer/exporter status and turnover history.
- Tax invoices, customs entries, sales/purchase ledgers and prior credits.
- Private/exempt/taxable use allocation and returned-goods evidence.
- Export contract, destination/use, customs proof and receipt into Sudan.
- Notices, current form/currency, refund request and existing payment references.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| vat-ar; selected ss.12,15; PDF 11,13; s.14 and amendment footnote, PDF 12; s.28(5), PDF 20 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/vat2001.pdf | 2026-11-01 |
| law 40-42; selected VAT Amendment 2022 s.2(a), PDF 1 and attestation PDF 2; s.2(b)–(c), PDF 1–2 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law40-42.pdf | 2026-11-01 |
| law 13_14; selected VAT Amendment 2018 s.2, PDF 1–2 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law13_14.pdf | 2026-11-01 |
| vat-regs-2017; selected reg.5, PDF 4; reg.6, PDF 4–5; reg.7, PDF 5; reg.8, PDF 5–6; reg.9, PDF 6–7; reg.10, PDF 8–9; reg.11, PDF 9; reg.29, PDF 18–19; regs.29,31, PDF 18,21; reg.30, PDF 20; regs.32–33, PDF 21–23; annex Form 3, PDF 30–33 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/vat_list.pdf | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-vat-gst.md](../../evidence/ledgers/sd-vat-gst.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Legacy-topic controls below refer to the exact original material and line-independent destination records in [the complete old-topic map](../../evidence/ledgers/sd-old-topic-map.md). Each control retains its original rules, figures, groups, procedures and exceptions for source reconciliation. Supported content is replaced above with citations; any remaining original claim under that control is explicitly unconfirmed, not a usable default.

- SD-OLD-123: Sudan VAT (ضريبة القيمة المضافة) Skill v 0.1. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-124: Section 1 - Scope statement. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-125: Section 2 - Quick reference. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-126: Key return sections (Form 3). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-127: Conservative defaults. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-128: Section 3 - Rates and thresholds. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-129: Who must register. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-130: Registration procedure (Form 1, Form 2). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-131: Registration cancellation. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-132: Changes to registration data. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-133: Filing and payment. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-134: Filing and payment. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-135: Books and records. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-136: Step 1 - Compute output VAT. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-137: Step 2 - Compute input VAT (only recoverable if registered). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-138: Step 3 - Net VAT payable. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-139: Reverse-charge on imported services. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-140: Tax invoice requirements. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-141: Special-rate supplies. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-142: Voluntary registration. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-143: Sanctions for non-payment. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-144: Refunds for exporters. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-145: Imports. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-146: Example 1 - Standard domestic sale. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-147: Example 2 - Telecom sale (special rate). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-148: Example 3 - Export of goods (zero-rated). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-149: Example 4 - Reverse charge on foreign SaaS subscription. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-150: Example 5 - Import of goods (customs VAT). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-151: Example 6 - Monthly return summary. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-152: Section 8 - Self-checks. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-153: Section 9 - Reference material. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-154: PROHIBITIONS. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.

Not yet confirmed: Later enacted chain, numeric registration threshold and its current measurement, current live electronic Form 3 and all special valuation bases, exemption revocations including imported sugar and investment capital lists, imported-service rate/procedure, zero-rating evidence beyond the opened regulation, current sanctions and appeal conditions. Legacy cigarettes 30%, telecom 35%, a default 17% for unknown categories,5% special form line, fixed FIFO inventory rule, automatic quarterly refund and an unsupported 1.2 million threshold are not approved. Current input-credit exclusions and capital-equipment conditions require the full amended chain; no universal investment VAT exemption is certified. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
