---
name: malaysia-einvoice
description: Use this skill whenever asked about Malaysia e-invoicing in 2026, the MyInvois system, LHDN or IRBM e-invoice, UBL 2.1 for Malaysia, the e-invoice implementation timeline, the RM3 million exemption, the interim relaxation period, consolidated e-invoices, self-billed e-invoices, the 72-hour cancel or reject window, the MyInvois portal or API, or e-invoice penalties. Covers who must issue e-invoices and from when (phases from 1 August 2024 to 1 January 2026 and 1 July 2026 for new businesses), how turnover is measured (financial year 2022), the exemptions, the RM10,000 single-transaction rule, consolidation within 7 calendar days, the relaxation to 31 December 2027 for the last phase, the special voluntary disclosure programme and the filing steps. Based on IRBM e-Invoice Guideline version 4.8 and Specific Guideline version 4.9.
version: "2.0"
jurisdiction: MY
tax_year: 2026
tax_year_notes: "Rules in force in 2026, per the IRBM timeline page updated 30 August 2026, e-Invoice Guideline v4.8 and Specific Guideline v4.9."
last_updated: 2026-11-14
depends_on:
  - einvoice-workflow-base
category: invoicing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: e-invoicing
type: filing-howto
---

# Malaysia e-invoicing (MyInvois), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Malaysia.

## Scope

Malaysia's e-invoice is a continuous transaction control model run by the Inland Revenue Board (IRBM, LHDN) under the Income Tax Act 1967: the supplier (or the buyer, for a self-billed e-invoice) submits each e-invoice to IRBM for validation through the MyInvois portal or the MyInvois API, and IRBM returns a unique identifier and a QR code. This skill says who must issue, from when, which transactions are covered, and how to issue, consolidate, cancel and correct. Portal: https://myinvois.hasil.gov.my. Developer documentation: https://sdk.myinvois.hasil.gov.my.

Out of scope: the SST due on the invoice (`malaysia-sst`); income tax treatment of the income or expense (`my-income-tax`, `my-corporate-income-tax`).

## Ask the client first

1. **Turnover or revenue for financial year 2022** from the audited accounts (statement of comprehensive income), or from the YA 2022 tax return if not audited; and the length of that financial year.
2. **When did the business start?** Before 2023, 2023 to 2025, or 2026 onwards.
3. **Group position.** Any non-individual shareholder, holding company or related company with turnover of RM3 million or more.
4. **Customer mix.** B2B, B2G, B2C, exports; any single sale over RM10,000.
5. **Self-billed situations.** Payments to foreign suppliers, agents and dealers, individuals not in business, and similar.
6. **Channel.** MyInvois portal, API integration, or accounting software.

## The method, step by step

### Step 1: is the client in, and from when? (Guideline section 1.5 and 1.6)

| Group | Implementation date | Interim relaxation |
| --- | --- | --- |
| Turnover or revenue over RM100 million | 1 August 2024 | to 31 January 2025 |
| Over RM25 million up to RM100 million | 1 January 2025 | to 30 June 2025 |
| Over RM5 million up to RM25 million | 1 July 2025 | to 31 December 2025 |
| Up to RM5 million | 1 January 2026 | to 31 December 2027 |
| New business started 2023 to 2025 with turnover of at least RM3 million | 1 July 2026 | to 31 December 2027 |
| New business started 2026 onwards | 1 July 2026 or the start of operations; if first-year turnover is expected under RM3 million, 1 January of the second year after the year turnover reached RM3 million | |
| Turnover or revenue under RM3 million | Exempt | |

Rules for the test: turnover is from financial year 2022; a 2022 year longer or shorter than 12 months is pro-rated to 12 months; later changes in turnover do not change the date once set. The RM3 million exemption covers all kinds of taxpayer (individuals, partnerships, companies, co-operatives) but not a taxpayer with a non-individual shareholder, holding company or related company that has turnover of at least RM3 million. Voluntary early adoption is allowed.

Also exempt from issuing: foreign diplomatic offices; individuals not in business; statutory bodies and local authorities for statutory collections; international organisations for transactions before 1 July 2025. No e-invoice is needed for employment income, pensions, alimony, certain dividends, zakat, listed securities and derivatives contracts, disposals of unlisted shares by individuals, and qualifying donations. Suppliers to exempt persons must still issue e-invoices.

### Step 2: which document

Invoice, credit note, debit note, refund note, and their self-billed versions (self-billed invoice, credit note, debit note, refund note). Self-billed e-invoices are issued by the buyer in the cases the Specific Guideline lists, for example payments to foreign suppliers and to agents, dealers and distributors.

### Step 3: individual or consolidated

- B2B and B2G sales need an individual e-invoice.
- B2C sales where the buyer does not ask for an e-invoice may go on a monthly consolidated e-invoice, submitted within 7 calendar days after the month end.
- From 1 January 2026 any single transaction over RM10,000 needs an individual e-invoice, in every industry.
- During the interim relaxation period the taxpayer may consolidate all transactions, including those normally needing an individual e-invoice, may put any description in the product field, and need not issue an individual e-invoice even if the buyer asks, provided it issues consolidated e-invoices. IRBM will not prosecute under section 120 of the ITA during the relaxation for non-compliance where those consolidated e-invoices are issued.

### Step 4: issue and validate

1. Create the e-invoice in UBL 2.1 (XML or JSON) with the supplier's and buyer's tax identification numbers, registration numbers, SST number where registered, MSIC code, line items, tax type and amount.
2. Sign it with a digital certificate (API route) and submit through MyInvois portal or API.
3. IRBM validates and returns the unique identifier, validation date and time and a link for the QR code. Share the validated e-invoice with the buyer.
4. The buyer may ask to reject, and the supplier may cancel, within 72 hours of validation. After 72 hours, corrections go through a credit note, debit note or refund note, not cancellation.

### Step 5: missed or wrong e-invoices

The e-Invoice Special Voluntary Disclosure Programme runs from 7 July 2026 to 31 December 2027 for taxpayers who missed submissions, submitted non-compliant e-invoices, or are under an e-invoice compliance review. Disclosures must be in good faith and in the prescribed form.

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Exemption, turnover or revenue under | RM3,000,000 | https://www.hasil.gov.my/en/e-invois/pelaksanaan-e-invois-di-malaysia/garis-masa-pelaksanaan-e-invois/ |
| Last phase, turnover up to RM5 million, implementation | 1 January 2026 | same |
| New business started 2023 to 2025, turnover of at least RM3 million | 1 July 2026 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Guideline.pdf |
| Interim relaxation, last phase | to 31 December 2027 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf |
| Single transaction needing an individual e-invoice, from 1 January 2026 | over RM10,000 | same |
| Consolidated e-invoice deadline | 7 calendar days after month end | same |
| Cancel or reject window | 72 hours from validation | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Guideline.pdf |
| Special voluntary disclosure programme | 7 July 2026 to 31 December 2027 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf |
| Fine for failing to comply with a requirement, s. 120(1) ITA | RM200 to RM20,000, or up to 6 months, or both | https://www.hasil.gov.my/en/perundangan/kesalahan-denda-dan-penalti/ |

### Technical notes

Kept from the earlier version for developers; check each against the SDK before building: UBL 2.1 namespaces for Invoice-2, CommonAggregateComponents-2 and CommonBasicComponents-2; e-invoice document version 1.1; UTF-8; issue date and time in UTC; OAuth 2.0 client credentials with the client ID and secret from the MyInvois portal (taxpayer and intermediary logins); API paths for login, document submissions, document details, cancel, reject, search and QR code; sandbox at preprod-api.myinvois.hasil.gov.my. IRBM validation checks structure, mandatory fields, signature, TINs and registration numbers, code tables (MSIC, state, currency, tax type, classification), tax arithmetic, duplicates and dates; statuses are Submitted, Valid, Invalid, Cancelled and Rejected. Common rejections: invalid TIN, missing field, bad certificate, tax mismatch, invalid classification code, duplicate number. Line tax = taxable amount x rate, rounded to 2 decimals; each line carries its own tax type and rate; a foreign-currency e-invoice carries the exchange rate.

## Worked cases

Case, decision: must the client issue e-invoices in 2026? A trading company's audited financial year 2022 ran 18 months (1 July 2021 to 31 December 2022, after a change of year end) with revenue of RM4,200,000. Pro-rated to 12 months: RM4,200,000 / 18 x 12 = RM2,800,000. That is under RM3,000,000, so the company is exempt, provided no non-individual shareholder, holding company or related company has turnover of RM3 million or more. Had the 18-month revenue been RM4,800,000, the 12-month figure would be RM3,200,000, in the "up to RM5 million" phase from 1 January 2026 with relaxation to 31 December 2027.

```oa-check
name: e-invoice exemption test with an 18-month FY2022
inputs:
  revenue_fy2022: 4200000
  months: 18
  exemption: 3000000
steps:
  - annualised: revenue_fy2022 / months * 12
  - headroom: exemption - annualised
expected:
  annualised: 2800000
  headroom: 200000
```

## When to refuse or refer

| Code | Trigger | Message |
| --- | --- | --- |
| R-EI-1 | Group structure unclear for the RM3 million test | "The exemption does not apply if a corporate shareholder, holding company or related company has turnover of RM3 million or more. I need the group facts before saying the client is exempt." |
| R-EI-2 | Building an API integration | "Use the MyInvois SDK specifications and test in the sandbox; this skill does not replace them." |
| R-EI-3 | Industry-specific rules (e-commerce, utilities, agents, foreign income) | "These have specific treatments in the Specific Guideline. Check the relevant section before advising." |
| R-EI-4 | Missed e-invoices from a past period | "Consider the special voluntary disclosure programme to 31 December 2027; refer to a tax agent." |

## Filing and payment

| Step | Where | When |
| --- | --- | --- |
| Register for MyInvois access | MyInvois portal (via MyTax roles) | Before the implementation date |
| Submit individual e-invoice | Portal or API | At the transaction |
| Submit consolidated e-invoice | Portal or API | Within 7 calendar days after month end |
| Cancel or reject | Portal or API | Within 72 hours of validation |
| Correct after 72 hours | Credit, debit or refund note | When the error is found |
| Voluntary disclosure | IRBM, as prescribed | 7 July 2026 to 31 December 2027 |

Effects elsewhere: revenue in Form C and Form B should agree with validated e-invoices; SST returns are compared with e-invoice tax totals; deductions should be supported by e-invoices received or self-billed.

## Completion checklist

- FY2022 turnover found, pro-rated if needed, and the group test done.
- Implementation date and relaxation end stated.
- Each customer stream classified as individual or consolidated, including the RM10,000 rule.
- Self-billed cases listed.
- 72-hour and 7-day timings set in the process.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the implementation timeline and the RM3,000,000 exemption (page updated 30 August 2026) | https://www.hasil.gov.my/en/e-invois/pelaksanaan-e-invois-di-malaysia/garis-masa-pelaksanaan-e-invois/ | 2026-11-14 |
| Read for e-Invoice Guideline v4.8: Table 1.1, turnover basis, new businesses, exemptions in 1.6, the 72-hour window | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Guideline.pdf | 2026-11-14 |
| Read for e-Invoice Specific Guideline v4.9: consolidation within 7 days, the RM10,000 rule, Table 16.1 relaxation periods, section 16.3 on prosecution, section 17 voluntary disclosure | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf | 2026-11-14 |
| Read for the s. 120(1) fine | https://www.hasil.gov.my/en/perundangan/kesalahan-denda-dan-penalti/ | 2026-11-14 |

Not yet confirmed: the technical notes (namespaces, document version 1.1, API paths, token life of 1 hour, 55 fields in 8 groups, tax type codes) were not checked against the SDK site today; the retention period for e-invoices (old file: 7 years); the tourism tax figure in the old file (RM10 a room a night); the legal basis named in the old file (section 82C and P.U. (A) 265, not opened).
