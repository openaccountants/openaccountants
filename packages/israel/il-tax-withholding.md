---
name: il-tax-withholding
description: Use this skill when advising on Israeli tax withholding at source (ניכוי מס במקור — Nikui Mas BeMakor). Trigger on phrases like "withholding tax Israel", "nikui mas", "ishur nikui", "withholding certificate", "Form 856", "Form 102", "tium mas", "tax coordination", "ניכוי מס במקור", "אישור ניכוי", or any Israeli withholding tax query. Covers payments to suppliers, freelancers, landlords, and non-residents. ALWAYS read this skill before advising on Israeli withholding tax.
version: 1.0
jurisdiction: IL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Tax Withholding

## Israel Tax Withholding (Nikui Mas BeMakor — ניכוי מס במקור) Skill v1.0

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 — Quick reference

**Quick reference**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Israel (מדינת ישראל) |
| Scope | Withholding tax at source on payments to suppliers, freelancers, landlords, and non-residents |
| Currency | NIS (Israeli New Shekel — ₪) |
| Governing law | Income Tax Ordinance — Sections 164 and 170 |
| Tax authority | Israel Tax Authority (ITA — רשות המיסים בישראל) |
| Periodic report | Form 102 (טופס 102) — monthly or bi-monthly |
| Annual reconciliation | Form 856 (טופס 856) — due April 30 |
| Certificate verification | gmishurim service — https://taxinfo.taxes.gov.il/gmishurim/firstPage.aspx |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Israel-licensed רואה חשבון or יועץ מס |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| No withholding certificate provided | Apply default rate for payment type |
| Certificate year not verified | Treat as expired — apply default rate |
| Unknown whether payee is resident or non-resident | Treat as non-resident (25% rate) |
| Payment type unclear | Apply 30% services default |
| Unknown whether payer exceeds mandatory withholder threshold | Withhold to be safe |

## Section 2 — Default withholding rates

### 2.1 Rates by payment type (no certificate)

**Rates by payment type (no certificate)**

| Payment type | Hebrew | Default rate | ITO Section |
| --- | --- | --- | --- |
| Services — individuals, no certificate | שלומים עבור שירותים | 30% (up to ~47% for unverified payees) | 164 |
| Services — companies, no certificate | שלומים עבור שירותים | 20–30% by ITA classification | 164 |
| Rent — business/commercial property | שכירות נכסי נדל"ן | 35% | 170 |
| Rent — residential property | שכר דירה למגורים | 30% | 170 |
| Royalties | תמלוגים | 23% | 170 |
| Interest | ריבית | 25% | 164 |
| Dividends | דיבידנדים | 25–30% | 164 |
| Payments to non-residents | תשלומים לתושבי חוץ | 25% | 170 |

- **Legacy 20% rate incorrect** — The "20% flat" figure from older guidance is incorrect. The ITA default for a service payment with no certificate is 30%, and the tax office can set it as high as ~47% for an unverified payee. A valid certificate is what brings the rate down (often to 0–5%).  _(164)_

### 2.2 De minimis threshold

- **De minimis threshold for single payment** — NIS 5,520 NIS (annually indexed; a single payment to a payee below this does not require withholding unless cumulative payments to that payee cross the threshold. Always verify the current-year threshold.)

## Section 3 — Withholding certificates

### 3.1 Certificate types

**Certificate types**

| Certificate | Hebrew | Purpose |
| --- | --- | --- |
| Ishur Nikui Mas BeMakor | אישור ניכוי מס במקור | Reduced or zero withholding on payments received |
| Ishur Tium Mas | אישור תיאום מס | Tax coordination for individuals with multiple payers/employers |
| Ishur Nikui Mas Rechisha | אישור ניכוי מס רכישה | Real estate purchase tax withholding |

### 3.2 Verifying a certificate

- **Steps to verify a certificate** — When a payee presents a withholding certificate: 1. Verify the year — certificates are valid for the current tax year (January–December) only. 2. Verify the payee's identity — business name, TIN (taxpayer identification number), and approved rate must match. 3. Verify online — use the ITA gmishurim service to confirm certificate status: https://taxinfo.taxes.gov.il/gmishurim/firstPage.aspx. 4. Check validity period — some certificates have shorter validity than the full year  _(https://taxinfo.taxes.gov.il/gmishurim/firstPage.aspx)_

### 3.3 Obtaining a certificate

- **Steps to obtain a certificate** — 1. Apply through the ITA online services (gmishurim system). 2. Provide: TIN, financial statements, tax returns. 3. Certificate valid for the current tax year. 4. Renewal required annually — certificates expire December 31

## Section 4 — Withholding calculation

### 4.1 Basic calculation

- **Basic withholding calculation** — Payment amount (before VAT): X NIS Withholding rate: Y% (from certificate, or default) Withholding amount: X × Y% Net payment to payee: X − Withholding amount VAT (if applicable): Calculated separately on the full pre-withholding amount

### 4.2 Worked example — Payment to freelancer

Scenario: Business pays NIS 10,000 to a freelancer (Osek Murshe) for consulting, no certificate.

**No certificate scenario**

| Line | Amount (NIS) |
| --- | --- |
| Gross payment (before VAT) | 10,000 |
| Withholding (30% default) | 3,000 |
| Net payment to freelancer | 7,000 |
| VAT (18% on gross) | 1,800 |
| Total paid by business | 8,800 (net 7,000 + VAT 1,800) |

If the freelancer provides a valid certificate showing 2% withholding:

**With certificate scenario**

| Line | Amount (NIS) |
| --- | --- |
| Gross payment (before VAT) | 10,000 |
| Withholding (2% per certificate) | 200 |
| Net payment to freelancer | 9,800 |
| VAT (18% on gross) | 1,800 |
| Total paid by business | 11,600 (net 9,800 + VAT 1,800) |

### 4.3 Cross-border payments

- **Cross-border payment rules** — For payments to non-residents: Default: 25% withholding. Tax treaty may reduce the rate — check the Israel–[country] treaty. Common treaties: US-Israel, UK-Israel, Germany-Israel, France-Israel. Treaty benefits require documentation and proper application. Treaty list: https://www.gov.il/he/departments/guides/taxation-agreements  _(https://www.gov.il/he/departments/guides/taxation-agreements)_

## Section 5 — Periodic reporting (Form 102)

### 5.1 Filing obligation

- **Filing obligation intro** — Amounts withheld must be reported and paid to the ITA periodically:

**Filing obligation table**

| Business size | Reporting frequency | Deadline |
| --- | --- | --- |
| Small businesses | Bi-monthly | 15th of the month after the period |
| Larger businesses / employers | Monthly | 15th of the following month |

- **Late reporting penalties** — Late reporting and late payment carry penalties and indexation (הצמדה + ריבית).

### 5.2 Mandatory withholder threshold

- **Mandatory withholding agent threshold** — Not every payer must withhold. A business becomes a mandatory withholding agent for service/asset payments once its turnover crosses the ITA's indexed turnover threshold. Below the threshold, withholding on service payments may not be required, but a business with employees still files Form 102 for payroll.

## Section 6 — Annual reconciliation (Form 856)

### 6.1 Purpose

- **Form 856 purpose** — Form 856 (טופס 856) is the annual withholding reconciliation for payments to suppliers and service providers. It is a detailed file listing every payee, the total paid, and the total withheld during the year, reconciled against the Form 102 deposits.

### 6.2 Requirements

**Form 856 requirements**

| Field | Description |
| --- | --- |
| Supplier details | ID/company number, name, address |
| Total payments | Gross amount paid during the year |
| Tax withheld | Amount withheld at source |
| Payment type | Services, goods, rent, commissions, etc. |

### 6.3 Deadline

- **Form 856 deadline** — April 30 date (of the year following the reporting year)

### 6.4 Workflow

- **Form 856 workflow steps** — 1. Deposit withheld amounts periodically via Form 102. 2. At year end, compile the per-payee detail file. 3. Submit Form 856 by April 30. 4. Form 856 is the PAYER's obligation as the withholding agent — separate from the payee's own annual return

## Section 7 — 2026 deduction-disallowance rule

- **2026 deduction disallowance rule** — Income Tax Circular 3/2026 (effective for payments made from 1.1.2026): An expense or input-VAT deduction is disallowed where the payer: Failed to withhold tax as required, OR Failed to report the withholding as required, OR Breached the Law for Reduction of the Use of Cash (cash over NIS 6,000 in a business-to-business transaction). Treat a missed withholding or a cash-law breach as a deduction risk, not just a reporting issue. The business loses the right to deduct the expense for income tax purposes AND loses the right to claim input VAT on the payment.  _(Income Tax Circular 3/2026)_

## Section 8 — Red flags and common errors

**Red flags and common errors**

| Error | Consequence |
| --- | --- |
| Using the legacy "20% for services" rate | Under-withholding; payer liable for the shortfall |
| Not checking certificate expiry | Applying a reduced rate when certificate has expired |
| Applying domestic rates to non-resident payments | Under-withholding; potential double taxation issues |
| Using residential rent rate (30%) for commercial property | Should be 35% for commercial |
| Cash payment over NIS 6,000 in B2B | Expense deduction disallowed under 2026 rules |
| Missing Form 102 deadline | Penalties and indexation on late payment |
| Not filing Form 856 by April 30 | Separate annual reconciliation penalty |

## Section 9 — Tier 2 items (require professional input)

**Tier 2 items**

| Item | Why it needs a professional | What to ask |
| --- | --- | --- |
| Tax treaty application | Treaty rates and documentation requirements vary by country | "Which country is the payee resident in? Provide the treaty article relied on." |
| Withholding on real estate transactions | Complex exemption rules under Mas Rechisha | "Is this a residential or commercial property purchase?" |
| Reclassification of payment type | ITA may challenge the classification | "Provide the service agreement or contract." |
| Exemption claims by non-residents | Requires ITA approval and specific documentation | "Does the non-resident have a permanent establishment in Israel?" |

## Section 10 — Reference material

**Reference material**

| Resource | Reference |
| --- | --- |
| Israel Tax Authority (ITA) | https://www.gov.il/he/departments/israel_tax_authority |
| Certificate lookup (gmishurim) | https://taxinfo.taxes.gov.il/gmishurim/firstPage.aspx |
| Form 856 filing | https://www.gov.il/he/service/form-856 |
| Income Tax Ordinance s.164/170 | https://www.nevo.co.il/law_html/law01/255_001.htm |
| Tax treaty list | https://www.gov.il/he/departments/guides/taxation-agreements |
| ITA filing portal (Shaam) | https://www.misim.gov.il |

## Disclaimer

> חשוב: כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional — such as a רואה חשבון (Ro'eh Cheshbon — CPA) or יועץ מס (Yo'etz Mas — tax advisor) licensed in Israel — before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
