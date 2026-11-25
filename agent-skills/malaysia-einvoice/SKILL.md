---
name: malaysia-einvoice
description: "Use this skill whenever asked about Malaysia e-invoicing in 2026, the MyInvois system, LHDN or IRBM e-invoice, UBL 2.1 for Malaysia, the e-invoice implementation timeline, the RM3 million exemption, the interim relaxation period, consolidated e-invoices, self-billed e-invoices, the 72-hour cancel or reject window, the MyInvois portal or API, or e-invoice penalties. Covers who must issue e-invoices and from when (phases from 1 August 2024 to 1 January 2026 and 1 July 2026 for new businesses), how turnover is measured (financial year 2022), the exemptions, the RM10,000 single-transaction rule, consolidation within 7 calendar days, the relaxation to 31 December 2027 for the last phase, the special voluntary disclosure programme and the filing steps. Based on IRBM e-Invoice Guideline version 4.8 and Specific Guideline version 4.9."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/malaysia-einvoice"
  jurisdiction: "MY"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Malaysia e-invoicing (MyInvois), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Malaysia.

## Scope

Malaysia's e-invoice is a continuous transaction control model run by the Inland Revenue Board (IRBM, LHDN) under section 82C of the Income Tax Act 1967: the supplier (or the buyer, for a self-billed e-invoice) submits each e-invoice to IRBM for validation through the MyInvois portal or the MyInvois API, and IRBM returns a unique identifier and validation link information. The portal’s visual representation includes a QR code. For an API-generated visual representation, the supplier embeds a QR code with the link. This skill says who must issue, from when, which transactions are covered, and how to issue, consolidate, cancel and correct. Portal: https://myinvois.hasil.gov.my. Developer documentation: https://sdk.myinvois.hasil.gov.my.

Out of scope: the SST due on the invoice (`malaysia-sst`); income tax treatment of the income or expense (`my-income-tax`, `my-corporate-income-tax`).

## Ask the client first

1. **Turnover or revenue for financial year 2022** from the audited accounts (statement of comprehensive income), or from the YA 2022 tax return if not audited; and the length of that financial year.
2. **When did the business start?** Before 2023, 2023 to 2025, or 2026 onwards.
3. **Group position.** Any non-individual shareholder or equivalent, holding company of which the client is a subsidiary, related company or joint venture with annual turnover or revenue of RM3 million or more.
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
| New business starting in 2026 or later that fails the exemption criteria | 1 July 2026 or the start of operations, whichever is later | Up to 31 December 2027 for an eligible taxpayer with a 1 July 2026 implementation date |
| New business starting in 2026 or later that meets the exemption criteria | 1 January of the second year after the YA in which annual turnover or revenue reaches RM3 million, including a threshold reached in the first YA | |
| Turnover or revenue under RM3 million | Exempt | |

IRBM’s first rollout date was 1 August 2024. P.U. (A) 265/2024 prescribed 1 October 2024 for that cohort. IRBM distinguishes the statutory enforcement date from its rollout and interim relaxation. The amended rules set the underlying dates in rule 2(1), and IRBM applies the current RM3 million administrative exemption subject to its criteria. [Gazetted rules](https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/2384109/PUA%20265%20%282024%29.pdf#page=11), [2025 amendment](https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/2937538/P.U.%20%28A%29%20196_2025.pdf#page=4), [IRBM General FAQ, Q11–16](https://www.hasil.gov.my/wp-content/uploads/lhdnm-e-invoice-general-faqs.pdf#page=4).

For an established business use 2022 audited turnover or revenue, or the YA 2022 return if unaudited. If the 2022 accounting year-end changed, pro-rate to 12 months. Later turnover does not change a date already set. An eligible business below RM3 million is exempt whilst it meets the criteria. If it reached RM3 million in YA 2023, 2024 or 2025, the date is 1 July 2026. If it first reaches RM3 million in YA 2026 or later, the date is 1 January of the second year after that YA. An established taxpayer below RM3 million that fails the group test starts on 1 July 2026. Voluntary early adoption is allowed. [Guideline §§1.5–1.6](https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Guideline.pdf#page=13), [IRBM General FAQ, Q12–14](https://www.hasil.gov.my/wp-content/uploads/lhdnm-e-invoice-general-faqs.pdf#page=4).

Also exempt from issuing: foreign diplomatic offices; individuals not in business; statutory bodies, statutory authorities and local authorities for statutory collections and for goods sold or services performed before 1 July 2025; listed international organisations for transactions before 1 July 2025. No e-invoice is needed for employment income, pensions, alimony, certain dividends, zakat, listed securities and derivatives contracts, disposals of unlisted shares by individuals, and qualifying donations. Suppliers to exempt persons must still issue e-invoices.

### Step 2: which document

Invoice, credit note, debit note, refund note, and their self-billed versions (self-billed invoice, credit note, debit note, refund note). Self-billed e-invoices are issued by the buyer in the cases the Specific Guideline lists, for example payments to foreign suppliers and to agents, dealers and distributors.

### Step 3: individual or consolidated

- Issue an individual e-invoice when the buyer requests one or for an activity in the Specific Guideline §3.7, subject to the applicable relaxation below. For B2B, B2G and B2C transactions where the buyer does not request an e-invoice and §3.7 permits consolidation, aggregate monthly and submit within 7 calendar days after month end. [IRBM General FAQ, Q39](https://www.hasil.gov.my/wp-content/uploads/lhdnm-e-invoice-general-faqs.pdf#page=18), [Specific Guideline §§3.6–3.7](https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf#page=18).
- From 1 January 2026 the ordinary rules require an individual e-invoice for any single transaction over RM10,000 in every industry. First check whether the taxpayer is exempt or entitled to interim relaxation. [Specific Guideline Table 3.6 and §16.2](https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf#page=33).
- During the interim relaxation period the taxpayer may consolidate all transactions, including those normally needing an individual e-invoice, may put any description in the product field, and need not issue an individual e-invoice even if the buyer asks, provided it issues consolidated e-invoices. IRBM will not prosecute under section 120 of the ITA during the relaxation for non-compliance where those consolidated e-invoices are issued.

### Step 4: issue and validate

1. Create the e-invoice in UBL 2.1 (XML or JSON) with the supplier's and buyer's tax identification numbers, registration numbers, SST number where registered, MSIC code, line items, tax type and amount.
2. Submit through the MyInvois portal or API. API document v1.1 validates the digital signature. The SDK also permits v1.0 without signature validation pending an official retirement notice. [MyInvois SDK FAQ](https://sdk.myinvois.hasil.gov.my/faq/).
3. IRBM validates and returns the unique identifier, validation date and time and a link for the QR code. Share the validated e-invoice with the buyer.
4. The buyer may ask to reject, and the supplier may cancel, within 72 hours of validation. After 72 hours, corrections go through a credit note, debit note or refund note, not cancellation.

### Step 5: missed or wrong e-invoices

The e-Invoice Special Voluntary Disclosure Programme runs from 7 July 2026 to 31 December 2027 for taxpayers who missed submissions, submitted non-compliant e-invoices, or are under an e-invoice compliance review. Disclose accurately and in good faith using e-invoice version SVDP 1.2 without a digital signature or SVDP 1.3 with one. Submit missing consolidated invoices by their original transaction month. Enforcement relief depends on compliant disclosure and excludes fraud, wilful default and negligence. [Specific Guideline §§17.1–17.6](https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf#page=125).

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Exemption, turnover or revenue under | RM3,000,000 | https://www.hasil.gov.my/en/e-invois/pelaksanaan-e-invois-di-malaysia/garis-masa-pelaksanaan-e-invois/ |
| Last phase, annual turnover up to RM5 million, subject to exemption and concession dates | 1 January 2026 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Guideline.pdf#page=13 |
| New business started 2023 to 2025, turnover of at least RM3 million | 1 July 2026 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Guideline.pdf |
| Interim relaxation, last phase | to 31 December 2027 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf |
| Single transaction needing an individual e-invoice under ordinary rules, from 1 January 2026 | over RM10,000 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf#page=33 |
| Consolidated e-invoice deadline | 7 calendar days after month end | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf#page=18 |
| Cancel or reject window | 72 hours from validation | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Guideline.pdf |
| Special voluntary disclosure programme | 7 July 2026 to 31 December 2027 | https://www.hasil.gov.my/wp-content/uploads/IRBM-e-Invoice-Specific-Guideline.pdf |
| Failure to issue without reasonable excuse, on conviction under s. 120(1)(d) ITA | RM200 to RM20,000, imprisonment up to 6 months, or both | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf#page=392 |

### Technical notes

Kept from the earlier version for developers; check each against the SDK before building: UBL 2.1 namespaces for Invoice-2, CommonAggregateComponents-2 and CommonBasicComponents-2; ordinary e-invoice document versions 1.0 and 1.1; UTF-8; issue date and time in UTC; OAuth 2.0 client credentials with the client ID and secret from the MyInvois portal (taxpayer and intermediary logins), with an access token valid for 1 hour according to the [SDK login specification](https://sdk.myinvois.hasil.gov.my/api/07-login-as-taxpayer-system/); API paths for login, document submissions, document details, cancel, reject, search and QR code; sandbox at preprod-api.myinvois.hasil.gov.my. IRBM validation checks structure, mandatory fields, signature, TINs and registration numbers, code tables (MSIC, state, currency, tax type, classification), tax arithmetic, duplicates and dates; statuses are Submitted, Valid, Invalid, Cancelled and Rejected. Common rejections: invalid TIN, missing field, bad certificate, tax mismatch, invalid classification code, duplicate number. Follow the SDK mathematical mappings and field definitions for each tax type, including any rate or per-unit amount. A foreign-currency e-invoice carries the exchange rate. [MyInvois SDK mathematical mappings](https://sdk.myinvois.hasil.gov.my/mathematical-mappings/).

## Worked cases

Case, decision: must the client issue e-invoices in 2026? A trading company's audited financial year 2022 ran 18 months (1 July 2021 to 31 December 2022, after a change of year end) with revenue of RM4,200,000. Pro-rated to 12 months: RM4,200,000 / 18 x 12 = RM2,800,000. That is under RM3,000,000, so the company is exempt whilst the turnover and group tests pass. Check the effect of any later year reaching RM3 million. Had the 18-month revenue been RM4,800,000, the 12-month figure would be RM3,200,000, in the "up to RM5 million" phase from 1 January 2026 with relaxation to 31 December 2027.

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

```oa-check
name: Alternative annualised revenue above the e-invoice exemption
inputs:
  revenue_fy2022: 4800000
  months: 18
  exemption: 3000000
steps:
  - annualised: revenue_fy2022 / months * 12
  - excess: annualised - exemption
expected:
  annualised: 3200000
  excess: 200000
```

## When to refuse or refer

| Code | Trigger | Message |
| --- | --- | --- |
| R-EI-1 | Group structure unclear for the RM3 million test | "The exemption depends on the RM3 million annual turnover or revenue test for any non-individual shareholder or equivalent, holding company, related company and joint venture. I need the group facts before saying the client is exempt." |
| R-EI-2 | Building an API integration | "Use the MyInvois SDK specifications and test in the sandbox; this skill does not replace them." |
| R-EI-3 | Industry-specific rules (e-commerce, utilities, agents, foreign income) | "These have specific treatments in the Specific Guideline. Check the relevant section before advising." |
| R-EI-4 | Missed e-invoices from a past period | "Consider the special voluntary disclosure programme to 31 December 2027; refer to a tax agent." |

## Filing and payment

| Step | Where | When |
| --- | --- | --- |
| Register for MyInvois access | MyInvois portal (via MyTax roles) | Before the implementation date |
| Submit individual e-invoice | Portal or API | Follow ordinary invoicing arrangements and any specific deadline for the transaction. See [IRBM General FAQ, Q38](https://www.hasil.gov.my/wp-content/uploads/lhdnm-e-invoice-general-faqs.pdf#page=18). |
| Submit consolidated e-invoice | Portal or API | Within 7 calendar days after month end |
| Cancel or reject | Portal or API | Within 72 hours of validation |
| Correct after 72 hours | Credit, debit or refund note | When the error is found |
| Voluntary disclosure | IRBM, as prescribed | 7 July 2026 to 31 December 2027 |

Reconcile validated e-invoices with Form C or Form B and the relevant SST return and document timing, exemptions and other differences. Retain e-invoices used as business records for 7 years from the end of the year to which the income relates. For a late return, count from the end of the year in which the return is furnished. [Income Tax Act s. 82(1)(a), (1A) and (9)](https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf#page=297).

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
| Statutory duty, validation, consolidation and offence | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf#page=302 | 2026-11-22 |
| Original issuance rules and 2025 amendment | https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/2384109/PUA%20265%20%282024%29.pdf | 2026-11-22 |
| Amendment to the phasing under rule 2 | https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/2937538/P.U.%20%28A%29%20196_2025.pdf | 2026-11-22 |
| IRBM General FAQ on phase dates, exemption, consolidation and individual timing | https://www.hasil.gov.my/wp-content/uploads/lhdnm-e-invoice-general-faqs.pdf | 2026-11-22 |
| API v1.0 and v1.1 signature validation | https://sdk.myinvois.hasil.gov.my/faq/ | 2026-11-22 |

Not yet confirmed: a single fixed technical field count for all document types, a universal decimal-place requirement, or whether the client must collect tourism tax.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `malaysia-einvoice` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/malaysia-einvoice. If neither is available, confirm every figure against the official source pages cited above before relying on it.
