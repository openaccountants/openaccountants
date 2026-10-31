---
name: kz-einvoice
description: >
  Use this skill whenever asked about electronic invoicing and digital fiscal compliance in Kazakhstan.
  Trigger on phrases like "Kazakhstan e-invoice", "ЭСФ", "электронный счёт-фактура", "IS ESF",
  "Kazakhstan online cash register", "ОФД", "ККМ Казахстан", "e-invoicing Kazakhstan". Covers the
  electronic invoice system (ИС ЭСФ), who must issue ЭСФ, online cash registers (ККМ) and fiscal data
  operators, and the e-waybill (СНТ). ALWAYS read this before any Kazakhstan e-invoicing work.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Kazakhstan E-Invoicing & Fiscal Compliance — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| E-invoice system | ИС ЭСФ (информационная система электронных счетов-фактур) — esf.gov.kz |
| Electronic invoice | ЭСФ (электронный счёт-фактура) |
| Online cash register | ККМ with fiscal data transmission to an ОФД (оператор фискальных данных) |
| E-waybill | СНТ (сопроводительная накладная на товары) for tracked goods |
| Who must issue ЭСФ | VAT-registered taxpayers; participants in goods-traceability; certain regimes — verify current scope |
| Tax authority | State Revenue Committee (КГД) |
| Currency | KZT |
| Quality tier | Research-verified — pending sign-off by a Kazakhstan accountant |
| Skill version | 1.0 |

### Conservative defaults
| Ambiguity | Default |
|---|---|
| Whether ЭСФ is mandatory | If VAT-registered or dealing in tracked/imported goods → assume mandatory |
| Cash/card retail sales | Assume an online ККМ + fiscal receipt is required (narrow exemptions) |

## Section 2 — Electronic invoices (ЭСФ)
- Issued and stored in the **ИС ЭСФ** portal; deadlines run from the date of turnover (commonly within 15 calendar days — verify).
- **Mandatory** for VAT payers, for traceable/imported goods, and for certain government-supply and traceability cases. A non-VAT small ИП on the simplified regime generally is **not** required to issue ЭСФ for ordinary services — verify against current КГД rules.
- A correctly issued ЭСФ is the basis for the buyer's VAT offset.

## Section 3 — Online cash registers (ККМ) & ОФД
- Businesses making cash/card sales to the public must use an **online ККМ** that transmits fiscal data to an **ОФД** in real time and issue a fiscal receipt (incl. QR).
- Narrow exemptions exist (e.g. certain remote-area or activity exemptions) — verify.

## Section 4 — E-waybill (СНТ)
For goods subject to traceability (imports, excisable, virtual-warehouse items), a **СНТ** must accompany movement and be registered electronically.

## Section 10 — Prohibitions
- NEVER tell a VAT payer they can skip ЭСФ.
- NEVER assume cash retail is exempt from online ККМ without checking the exemption list.
- NEVER state ЭСФ deadlines or scope without verifying current КГД rules.

## Disclaimer
Informational only; not advice. Verify ЭСФ scope, deadlines, and ККМ rules with the КГД. All outputs must be reviewed and signed off by a qualified Kazakhstan accountant before relying on them. Maintained at [openaccountants.com](https://www.openaccountants.com).
