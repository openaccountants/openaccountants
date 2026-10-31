---
name: bd-einvoice
description: >
  Use this skill whenever asked about electronic invoicing, fiscal devices, and digital VAT compliance
  in Bangladesh. Trigger on phrases like "Bangladesh e-invoicing", "EFD SDC NBR", "electronic fiscal
  device Bangladesh", "Mushak invoice", "VAT software Bangladesh". Covers the NBR's electronic fiscal
  devices (EFD/SDC) for VAT, the Mushak invoice/return forms, and what small/non-VAT businesses must
  issue. ALWAYS read before any Bangladesh e-invoicing work.
version: 1.0
jurisdiction: BD
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Bangladesh E-Invoicing & Fiscal Compliance — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Country | Bangladesh |
| VAT fiscal devices | EFD (Electronic Fiscal Device) / SDC (Sales Data Controller) rolled out by the NBR for certain retail/service businesses to transmit sales data in real time |
| VAT invoice | Mushak-6.3 (tax invoice); VAT return Mushak-9.1 |
| Income tax | Filed via the NBR e-Return (etaxnbr.gov.bd) — no universal mandatory e-invoicing for income tax |
| Authority | National Board of Revenue (NBR) |
| Currency | BDT (৳) |
| Quality tier | Research-verified — pending sign-off by a Bangladeshi practitioner |
| Skill version | 1.0 |

## Section 2 — Key points (Tier 1)
- **VAT-registered businesses** issue the prescribed **Mushak-6.3** tax invoice and file **Mushak-9.1** returns. The NBR has been deploying **EFD/SDC** machines to specified retail and service categories to report sales to the NBR in real time — **scope is being expanded by SRO**; verify whether the business is in scope.
- A **non-VAT solo freelancer** is **not** within the EFD/Mushak regime — they simply issue a proper invoice showing their TIN and keep records (see bd-bookkeeping). Income tax is filed via the **e-Return**, not an e-invoicing system.
- Foreign-currency export receipts need the **bank encashment certificate** rather than a VAT invoice.

## Section 3 — Worked example
A VAT-registered IT services firm: issues Mushak-6.3 invoices, files Mushak-9.1 monthly, and uses an EFD/SDC if in a notified category. A non-registered freelancer just issues TIN invoices and keeps encashment certificates.

## Section 10 — Prohibitions
- NEVER tell a VAT-registered, in-scope business they can skip EFD/Mushak compliance.
- NEVER assume a universal income-tax e-invoicing mandate — there isn't one; income tax is the e-Return.
- NEVER state EFD scope/SRO dates without verifying current NBR notifications.

## Disclaimer
Informational only; not advice. Verify EFD/Mushak scope and dates with the NBR. All outputs must be reviewed and signed off by a qualified Bangladeshi practitioner. Maintained at [openaccountants.com](https://www.openaccountants.com).
