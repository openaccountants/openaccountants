---
name: eg-bookkeeping
description: Use this skill whenever asked about Egyptian record-keeping, bookkeeping, or the mandatory ETA digital systems for self-employed people, sole proprietors (منشأة فردية), and professionals (أصحاب المهن الحرة). Trigger on phrases like "Egypt e-invoicing", "الفاتورة الإلكترونية", "ETA e-receipt", "الإيصال الإلكتروني", "bookkeeping Egypt", "records sole proprietor Egypt", "EGS item coding", "digital signature ETA", "what books must I keep in Egypt", or any request to set up, review, or explain the books and records an Egyptian self-employed taxpayer must keep. ALWAYS read this skill before touching any Egyptian record-keeping or e-invoicing/e-receipt work.
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Bookkeeping

## Egypt Record-Keeping & Bookkeeping (مسك الدفاتر والسجلات) Skill v1.0

This skill explains the books, records, and **mandatory digital systems** an Egyptian self-employed person, sole proprietor (منشأة فردية), or professional (صاحب مهنة حرة) must maintain. Egypt has moved aggressively to a fully digital tax ecosystem: the **e-invoicing system (منظومة الفاتورة الإلكترونية)** for B2B/B2G, and the **e-receipt system (منظومة الإيصال الإلكتروني)** for B2C. Being inside these systems is now a precondition for deducting input VAT and for deducting costs. Reply to the user in their own language (English or Arabic).

## Section 1 — Quick reference & conservative defaults

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Egypt (جمهورية مصر العربية) |
| Scope | Self-employed individuals, sole proprietors (منشأة فردية), and professionals (مهن حرة). Not large corporates, banks, or regulated sectors. |
| Currency | EGP (Egyptian Pound — ج.م) |
| Mandatory digital systems | (1) e-invoicing — منظومة الفاتورة الإلكترونية (B2B/B2G); (2) e-receipt — منظومة الإيصال الإلكتروني (B2C) |
| Authority | Egyptian Tax Authority — ETA (مصلحة الضرائب المصرية) |
| Portal | eta.gov.eg (e-invoicing: invoicing.eta.gov.eg; e-receipt: e-receipt portal under ETA) |
| Legal backbone | Unified Tax Procedures Law No. 206 of 2020; Income Tax Law No. 91 of 2005; VAT Law No. 67 of 2016; SME Law No. 6 of 2025 |
| Item coding | GS1 (GTIN) **or** EGS (Egyptian Goods & Services) codes mapped to GPC |
| Digital signature | Required for e-invoices (HSM / USB token / approved cloud signing) |
| Record retention | **5 years** (per Unified Tax Procedures Law) — *verify current value; some advisers cite 7 years* |
| Quality tier | **Research-verified — pending sign-off by an Egyptian accountant (محاسب قانوني)** |
| Skill version | 1.0 |

- **Country** — Egypt (جمهورية مصر العربية)
- **Scope** — Self-employed individuals, sole proprietors (منشأة فردية), and professionals (مهن حرة). Not large corporates, banks, or regulated sectors.
- **Currency** — EGP (Egyptian Pound — ج.م)
- **Mandatory digital systems** — (1) e-invoicing — منظومة الفاتورة الإلكترونية (B2B/B2G); (2) e-receipt — منظومة الإيصال الإلكتروني (B2C)
- **Authority** — Egyptian Tax Authority — ETA (مصلحة الضرائب المصرية)
- **Portal** — eta.gov.eg (e-invoicing: invoicing.eta.gov.eg; e-receipt: e-receipt portal under ETA)
- **Legal backbone** — Unified Tax Procedures Law No. 206 of 2020; Income Tax Law No. 91 of 2005; VAT Law No. 67 of 2016; SME Law No. 6 of 2025  _(Unified Tax Procedures Law No. 206 of 2020; Income Tax Law No. 91 of 2005; VAT Law No. 67 of 2016; SME Law No. 6 of 2025)_
- **Item coding** — GS1 (GTIN) or EGS (Egyptian Goods & Services) codes mapped to GPC
- **Digital signature** — Required for e-invoices (HSM / USB token / approved cloud signing)
- **Record retention** — 5 years years (verify current value; some advisers cite 7 years)  _(Unified Tax Procedures Law)_
- **Quality tier** — Research-verified — pending sign-off by an Egyptian accountant (محاسب قانوني)
- **Skill version** — 1.0

### Conservative defaults

When a fact is uncertain, the AI must take the **safer, more compliant** path and tell the user it is doing so:

- **Assume the taxpayer is in scope.** The B2C e-receipt mandate and the e-invoicing mandate have rolled out in waves and the registration threshold was lowered (reported as EGP 500,000 → EGP 250,000 of annual revenue for late 2025 / 2026). If turnover is near or above the threshold, assume the taxpayer **must** join. *Verify the exact threshold and the taxpayer's specific phase on eta.gov.eg.*
- **Assume an undocumented expense is non-deductible.** From the relevant phase onward, costs and input VAT not supported by a valid e-invoice / e-receipt are treated as **not deductible**.
- **Default retention is 5 years; if in doubt keep records longer** (7 years is a safe over-retention buffer some advisers recommend).
- **Never invent a deadline, threshold, rate, or phase date.** If you cannot confirm it, say "verify current value on eta.gov.eg or with an Egyptian accountant."

## Section 2 — The e-invoicing system (منظومة الفاتورة الإلكترونية)

The e-invoicing system handles **B2B and B2G** transactions. A registered seller must generate a structured electronic invoice, sign it digitally, and submit it to the ETA for **clearance/validation** before it is a legally valid invoice.

### 2.1 Who must register

- **Small-business exemption threshold / registration deadline** — EGP 500,000 → EGP 250,000 annual revenue; registration deadline cited as 31 March 2026 EGP (cited, reported in late 2025 — verify the threshold and the taxpayer's exact registration deadline on eta.gov.eg)  _(eta.gov.eg)_

E-invoicing rolled out in waves from 2020 and is now mandatory for essentially all VAT-registered businesses and professionals doing B2B/B2G work. Reporting in late 2025 indicates the small-business exemption threshold was lowered (cited as EGP 500,000 → **EGP 250,000** annual revenue), with newly-in-scope taxpayers required to register by an early-2026 deadline (cited as **31 March 2026**). *Verify the threshold and the taxpayer's exact registration deadline on eta.gov.eg — these figures changed recently.*

### 2.2 Registration steps (high level)

- **Registration steps** — 1. **Create the ETA digital profile** — register the business/professional on the ETA e-invoicing portal and set up authorised representatives. 2. **Obtain a digital signature (التوقيع الإلكتروني).** Egypt recognises electronic signatures with the same legal weight as handwritten ones (Unified Tax Procedures Law No. 206/2020; Digital Signature Law No. 15/2004). Get an AES certificate from an ETA-approved provider (e.g., Egypt Trust, Misr for Central Clearing). Form factors: - **USB token** — manual signing, suitable for very low invoice volume. - **HSM (Hardware Security Module) or approved cloud signing** — for automated / higher-volume issuance from an ERP. 3. **Code your items.** Every good or service must carry a code before it can be invoiced — see 2.3. 4. **Connect.** Low-volume issuers (commonly cited as **under ~200 invoices**) can issue directly on the ETA portal; higher volumes integrate an ERP via the ETA API. *Verify the current portal-vs-API threshold.*  _(Unified Tax Procedures Law No. 206/2020; Digital Signature Law No. 15/2004)_

### 2.3 Item coding — GS1 (GTIN) or EGS

- **Item coding schemes** — Each item must be uniquely coded using one of two ETA-recognised schemes: - **GS1 / GTIN** — register product data on MyGS1; barcodes propagate to the ETA platform (commonly cited as within ~24 hours). - **EGS (Egyptian Goods & Services code)** — for items without a GS1 code; the internal code is linked to the **GPC (Global Product Classification)** category and submitted to the ETA for **review and approval** before use. Approval is not instant, so code your catalogue early.

### 2.4 Format & submission

- **Format and submission requirements** — - Invoices are submitted to the ETA in the **ETA structured format (JSON or XML)** conforming to the ETA schema. - B2B/B2G invoices follow a **clearance model**: the invoice must be validated by the ETA (effectively real-time / same-day) — an unvalidated invoice is not a valid tax invoice. - The buyer's **Tax Registration Number (TRN)** (or UIN for foreign entities) must be present and valid; an invalid TRN can block the buyer's VAT deduction.

### 2.5 Consequences of non-compliance

- **Consequences of non-compliance** — - **No input-VAT deduction and no cost deductibility.** Invoices not issued through the e-invoicing system are **not accepted for VAT input credit, VAT refunds, or income-tax cost deduction.** This is the single most important point for a self-employed client: an expense without a compliant e-invoice effectively costs more. - **Penalties** under the Unified Tax Procedures Law for failure to issue/submit electronic documents, plus reported escalating/tiered penalties for repeated late submission (introduced for 2026). *Verify current penalty amounts.* - **Loss of access to the SME simplified regime** — ETA has stated that e-invoice/e-receipt compliance is required to benefit from the simplified tax system (Law No. 6 of 2025). See Section 4.5.  _(Unified Tax Procedures Law; SME Law No. 6 of 2025)_

## Section 3 — The e-receipt system (منظومة الإيصال الإلكتروني)

The e-receipt system handles **B2C** sales to final consumers (retail, services to individuals). The seller issues the customer a receipt at the point of sale and transmits the receipt data to the ETA.

### 3.1 Rollout status (2025 → 2026)

- **Rollout phases** — The e-receipt mandate has expanded in phases by ETA decision: - Earlier 2025 phases brought specified groups in on **1 July 2025** (Decision 123/2025) and **15 July 2025** (Decision 225/2025). - **Decision No. 281 of 2025** extended the mandate to retail/consumer transactions, with a wave from **15 September 2025**, and (as reported) lowered the in-scope revenue threshold and tightened penalties for 2026. By 2026 the system is described as fully operational, with enforcement focused on bringing each remaining group into its assigned phase. **A taxpayer must check the ETA website to confirm which phase applies to them.** *Verify the exact phase, threshold, and date for the specific taxpayer.*  _(ETA Decisions 123/2025, 225/2025, 281/2025)_

### 3.2 How it works

- **e-receipt operational requirements** — - **Integrate the POS / cash register or ERP** with the ETA central e-receipt system; receipts are transmitted with the seller's data and item codes. - **Submission timing:** sources commonly cite real-time or **within ~24 hours** of issuance; one source cites a 72-hour window. *Verify the current permitted window on eta.gov.eg — do not promise a specific window to the client without confirming.* - **QR code** must appear on the printed receipt linking to the validated e-receipt for consumer verification. - The same **item coding (GS1 / EGS)** and **digital identity** requirements apply as for e-invoicing.

### 3.3 e-invoice vs e-receipt — which applies

**e-invoice vs e-receipt applicability table**

| Sale | System | Model |
| --- | --- | --- |
| To a business or government (B2B / B2G) | e-invoice (الفاتورة الإلكترونية) | Pre-clearance / validation, structured JSON/XML, buyer TRN required |
| To a final consumer (B2C) | e-receipt (الإيصال الإلكتروني) | Transmit receipt data to ETA (real-time / short window), QR code on receipt |

A self-employed person who serves **both** business clients and individual consumers will typically need **both** systems.

## Section 4 — Books & records required

### 4.1 The general obligation to keep regular accounts

- **General obligation to keep regular accounts** — Under the Income Tax Law No. 91 of 2005 and the Unified Tax Procedures Law No. 206 of 2020, a taxpayer carrying on a commercial, industrial, or professional activity must keep **regular, accurate accounts and records** that allow the ETA to determine taxable profit. Keeping regular accounts is also what lets the taxpayer be taxed on **actual net profit** (revenue minus deductible costs) rather than on an estimated/deemed basis.  _(Income Tax Law No. 91 of 2005; Unified Tax Procedures Law No. 206 of 2020)_

### 4.2 Core books and records (typical self-employed / sole proprietor set)

- **Core books and records** — - **Cash / bank book** — receipts and payments (دفتر الصندوق/البنك). - **Sales / revenue register** — every e-invoice and e-receipt issued. - **Purchases / expenses register** — every supplier e-invoice received. - **Fixed-asset register** — assets and depreciation, supporting capital allowances. - **Inventory records** — where the activity holds stock. - **Wages / payroll records** — if the taxpayer has employees. - **Supporting documents** — contracts, bank statements, supplier e-invoices, customer e-receipts, import documents. For **professionals (مهن حرة)** (e.g., doctors, lawyers, engineers, consultants, freelance developers), keep a fee/revenue register and an expense register that tie to issued e-invoices/e-receipts and to bank deposits.

### 4.3 Link to deductibility

- **Link to deductibility** — Costs and input VAT are deductible **only if** supported by valid documentation that, from the relevant mandate phase, means a **compliant e-invoice / e-receipt** inside the ETA systems. Cash expenses with no compliant document should be treated as non-deductible by default.

### 4.4 Retention period

- **Record retention** — 5 years years (verify current value; some advisers cite 7 years)  _(Unified Tax Procedures Law)_

Electronic documents should be kept in their electronic form (XML/JSON plus the ETA validation and any human-readable PDF).

### 4.5 Simplified-regime taxpayers (SME Law No. 6 of 2025)

- **Simplified regime turnover eligibility** — annual turnover not exceeding EGP 20 million EGP  _(SME Law No. 6 of 2025, effective 1 March 2025)_

**Turnover-banded tax rates (reported, verify)**  _(SME Law No. 6 of 2025 (reported, verify))_

| Turnover band | Rate |
| --- | --- |
| under EGP 500k | ~0.4% |
| EGP 500k–2m | ~0.5% |
| EGP 2m–3m | ~0.75% |
| EGP 3m–10m | ~1% |
| EGP 10m–20m | ~1.5% |

- **Simplified regime record and filing requirements** — - Taxpayers are **not required to keep the full complex books** of the Unified Tax Procedures Law — a **simplified records system** and stand-alone simplified forms apply (annual income/payroll return; **quarterly** VAT returns). - **But** e-invoicing / e-receipt compliance is still required — ETA has stated the simplified-regime benefits depend on being inside the digital systems. - The election is **locked in for 5 years** (cannot be withdrawn early). Even simplified-regime taxpayers should keep revenue records, expense records, bank statements, and all e-invoices/e-receipts for the **5-year** retention period.  _(SME Law No. 6 of 2025)_

## Section 5 — Worked examples

### Example 1 — Freelance software developer, B2B clients only

A Cairo developer invoices three Egyptian companies. **System:** e-invoicing (B2B). Steps: register the digital profile on the ETA portal → obtain a USB-token digital signature (low volume) → create EGS codes for "software development services" linked to GPC → issue each invoice in ETA JSON/XML with the client's valid TRN → submit for clearance. Keep all issued e-invoices and supplier e-invoices for **5 years**. Without these, the developer cannot deduct input VAT on their laptop/software purchases.

### Example 2 — Beauty salon selling to individuals

A salon serves walk-in consumers. **System:** e-receipt (B2C). Personal-care centres were brought into the e-receipt mandate during the 2025 phases. Integrate the POS with the ETA e-receipt system, code services with EGS, transmit each receipt within the permitted window, and print a **QR code** on the receipt. *Confirm the salon's exact phase date on eta.gov.eg.*

### Example 3 — Consultant serving both companies and individuals

A consultant advises corporate clients (B2B) and also coaches private individuals (B2C). They need **both** systems: e-invoices for the company engagements and e-receipts for the individual sessions, sharing the same digital identity and item codes.

### Example 4 — Small trader under the SME simplified regime

A retailer with EGP 4 million annual turnover opts into Law No. 6 of 2025 (turnover band ~1%). They keep a **simplified records system** rather than full double-entry books and file **quarterly** VAT and an annual return — **but** must still issue e-receipts (B2C) and any B2B e-invoices, and retain those documents for **5 years**. Missing e-receipt compliance can disqualify them from the simplified-regime benefits.

## Section 6 — Tier 2 escalation, references & checklist

### Tier 2 — escalate / refuse and route to a human

- **Escalation triggers** — Hand off to a qualified Egyptian accountant (محاسب قانوني) or tax adviser when: - The taxpayer is **not** a self-employed individual / sole proprietor / professional (companies, partnerships, banks, regulated sectors). - There is a dispute, audit, assessment, or penalty notice from the ETA. - The taxpayer needs the **exact** phase date / threshold / penalty figure — these change by ETA decision and must be confirmed on eta.gov.eg. - ERP-to-ETA technical integration, HSM setup, or bulk EGS catalogue coding. - Cross-border / non-resident, withholding tax, or transfer-pricing issues.

### References (verify against primary sources)

- **Egyptian Tax Authority — eta.gov.eg** (e-invoicing portal: invoicing.eta.gov.eg; SDK: sdk.invoicing.eta.gov.eg; e-receipt portal).
- Unified Tax Procedures Law **No. 206 of 2020** (electronic documents; retention).
- Income Tax Law **No. 91 of 2005** and Executive Regulations (Decree 991/2005).
- VAT Law **No. 67 of 2016** and amendments (input-VAT conditions).
- SME tax incentives **Law No. 6 of 2025** (simplified regime).
- ETA Decisions **123/2025, 225/2025, 281/2025** (e-receipt phases / threshold).
- GS1 Egypt (gs1eg.org) — GTIN/EGS/GPC item coding.
- PwC *Worldwide Tax Summaries — Egypt*; KPMG / EY / Grant Thornton tax alerts (2025–2026).

### Checklist for the AI before answering

- [ ] Identified whether sales are B2B/B2G (e-invoice) or B2C (e-receipt) or both.
- [ ] Confirmed the taxpayer is in scope / which phase, or told them to verify on eta.gov.eg.
- [ ] Covered digital signature + item coding (GS1/EGS).
- [ ] Stated the input-VAT / cost-deduction precondition.
- [ ] Stated the 5-year retention (flagged as "verify"; advised longer if unsure).
- [ ] Checked whether the SME simplified regime (Law 6/2025) applies.
- [ ] Hedged every threshold/date/penalty with "verify current value".
- [ ] Replied in the user's language.

## PROHIBITIONS

- **Do NOT** state a registration threshold, phase date, submission window, penalty amount, or retention period as settled fact without flagging it for verification — these have changed recently (e.g., threshold reportedly lowered to EGP 250,000; e-receipt window cited as both 24h and 72h; retention cited as both 5 and 7 years).
- **Do NOT** advise a client to deduct input VAT or costs that are **not** supported by a compliant e-invoice / e-receipt.
- **Do NOT** tell a taxpayer they are exempt from e-invoicing / e-receipt — direct them to confirm their phase on eta.gov.eg.
- **Do NOT** invent EGS/GS1 item codes; codes must be registered and (for EGS) ETA-approved.
- **Do NOT** advise corporates, partnerships, banks, or regulated entities — this skill is scoped to self-employed individuals, sole proprietors, and professionals.
- **Do NOT** provide a digital-signature certificate, set up an HSM, or perform ETA portal registration on the user's behalf — guide them to ETA-approved providers.
- **Do NOT** present this output as filed advice — it requires human sign-off.

## Disclaimer

This skill is **research-verified** against public Egyptian Tax Authority material and reputable secondary sources (PwC, KPMG, EY, Grant Thornton, GS1 Egypt) as of **May 2026**, but it has **not yet been signed off by a qualified Egyptian accountant (محاسب قانوني)**. Egypt's e-invoicing and e-receipt rules, thresholds, phase dates, penalties, and retention periods change frequently by ETA decision. Treat every figure marked "verify" as provisional and confirm it on **eta.gov.eg** or with a licensed Egyptian tax professional before relying on it. This is general information, not tax advice, and must be reviewed by a qualified human before filing or acting. Part of **openaccountants.com** — an open-source library of tax skills for AI agents serving self-employed people.

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
