---
name: dominican-republic-itbis
description: Use this skill whenever asked to prepare, review, or classify transactions for a Dominican Republic ITBIS return for any client. Trigger on phrases like "ITBIS", "Dominican Republic VAT", "DGII filing", or any request involving DR consumption tax. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any ITBIS work.
version: 2.0
jurisdiction: DO
tax_year: 2025
last_updated: 2026-07-13
authored_by: Miguel Lantigua, CPA
reviewed_by: Miguel Lantigua
review_status: current
trust_label: Checked by Miguel Lantigua
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Dominican Republic Itbis

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Dominican Republic (Republica Dominicana) |
| Standard rate | 18% (ITBIS) |
| Reduced rate | 16% (certain processed foods); 0% (exports, basic food basket) |
| Exempt | Education, healthcare, financial services, basic food items, fuel |
| Return form | Monthly ITBIS return (Form IT-1) |
| Filing portal | https://dgii.gov.do (Oficina Virtual DGII) |
| Authority | Direccion General de Impuestos Internos (DGII) |
| Currency | DOP (Dominican Peso) |
| Filing frequency | Monthly |
| Deadline | 20th of the month following the tax period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending — requires licensed DR tax practitioner |

- **Country** — Dominican Republic (Republica Dominicana)
- **Standard rate** — 18% (ITBIS)
- **Reduced rate** — 16% (certain processed foods); 0% (exports, basic food basket)
- **Exempt** — Education, healthcare, financial services, basic food items, fuel
- **Return form** — Monthly ITBIS return (Form IT-1)
- **Filing portal** — https://dgii.gov.do (Oficina Virtual DGII)
- **Authority** — Direccion General de Impuestos Internos (DGII)
- **Currency** — DOP (Dominican Peso)
- **Filing frequency** — Monthly
- **Deadline** — 20th of the month following the tax period
- **Companion skill** — vat-workflow-base v0.1 or later — MUST be loaded
- **Validated by** — Pending — requires licensed DR tax practitioner

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 18% |
| Unknown input credit status | Not creditable |
| Unknown counterparty location | Domestic DR |

- **Unknown rate on a sale** — 18%
- **Unknown input credit status** — Not creditable
- **Unknown counterparty location** — Domestic DR

## Section 2 — Required inputs and refusal catalogue

**Minimum viable** — bank statement. Acceptable from: Banreservas, Banco Popular Dominicano, Scotiabank DR, BHD Leon, Banco Santa Cruz, or any other.

- **R-DO-1 — Free trade zone entity** — FTZ entities have bespoke ITBIS exemptions. Please escalate.  _(R-DO-1)_
- **R-DO-2 — Withholding agent for ITBIS** — ITBIS withholding obligations require certificate tracking. Please escalate.  _(R-DO-2)_

### 3.1 Dominican banks (exclude)

**Dominican banks (exclude)**  _(Financial service)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BANRESERVAS, BANCO DE RESERVAS | EXCLUDE | Financial service |
| POPULAR, BANCO POPULAR | EXCLUDE | Same |
| BHD LEON, SCOTIABANK DR | EXCLUDE | Same |

- **BANRESERVAS, BANCO DE RESERVAS** — EXCLUDE  _(Financial service)_
- **POPULAR, BANCO POPULAR** — EXCLUDE  _(Same)_
- **BHD LEON, SCOTIABANK DR** — EXCLUDE  _(Same)_

### 3.2 Government (exclude)

**Government (exclude)**  _(Tax payment)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGII | EXCLUDE | Tax payment |
| DGA, ADUANAS | EXCLUDE | Customs |
| TSS, SOCIAL SECURITY | EXCLUDE | Social security |

- **DGII** — EXCLUDE  _(Tax payment)_
- **DGA, ADUANAS** — EXCLUDE  _(Customs)_
- **TSS, SOCIAL SECURITY** — EXCLUDE  _(Social security)_

### 3.3 Utilities

**Utilities**  _(Electricity)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EDENORTE, EDESUR, EDEESTE | Domestic 18% | Electricity |
| CAASD, INAPA | Domestic 18% | Water |
| CLARO DR, ALTICE, WIND TELECOM | Domestic 18% | Telecoms |

- **EDENORTE, EDESUR, EDEESTE** — Domestic 18%  _(Electricity)_
- **CAASD, INAPA** — Domestic 18%  _(Water)_
- **CLARO DR, ALTICE, WIND TELECOM** — Domestic 18%  _(Telecoms)_

### 3.4 SaaS and international

**SaaS and international**  _(Non-resident)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, META, AWS | Self-assess 18% | Non-resident |

- **GOOGLE, MICROSOFT, META, AWS** — Self-assess 18%  _(Non-resident)_

### 3.5 Payroll/exclusions

**Payroll/exclusions**  _(Outside ITBIS scope)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, WAGES | EXCLUDE | Outside ITBIS scope |
| TRANSFERENCIA PROPIA | EXCLUDE | Internal |

- **SALARIO, WAGES** — EXCLUDE  _(Outside ITBIS scope)_
- **TRANSFERENCIA PROPIA** — EXCLUDE  _(Internal)_

### Example 1 — Domestic sale at 18%

**Input:** `05.04.2026 ; CLIENTE DOMINICANO SRL ; CREDIT ; Factura DO-041 ; DOP 118,000`
Net = DOP 100,000, ITBIS = DOP 18,000.

**Example 1 result table**  _(—)_

| Date | Counterparty | Gross | Net | ITBIS | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | CLIENTE DOMINICANO | +118,000 | +100,000 | 18,000 | 18% | Output | N | — |

- **Output** — 18%  _(—)_

### Example 2 — Export, zero-rated

**Input:** `15.04.2026 ; US BUYER ; CREDIT ; Export ; DOP 500,000`

**Example 2 result table**  _(—)_

| Date | Counterparty | Gross | Net | ITBIS | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | US BUYER | +500,000 | +500,000 | 0 | 0% | Zero-rated | N | — |

- **Zero-rated** — 0%  _(—)_

### Example 3 — Bank charges

**Input:** `30.04.2026 ; BANRESERVAS ; DEBIT ; Comision ; DOP -200`

**Example 3 result table**  _("Financial")_

| Date | Counterparty | Gross | Net | ITBIS | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30.04.2026 | BANRESERVAS | -200 | — | — | — | — | N | "Financial" |

- **—** — —  _("Financial")_

## Section 4 — Worked examples

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 18%. 5.2 Reduced 16% (processed food). 5.3 Zero rate — exports. 5.4 Exempt — education, healthcare, basic food, fuel. 5.5 Input credit — NCF (comprobante fiscal) required. 5.6 Imports — 18% on CIF plus duty. 5.7 Reverse charge — non-resident services. 5.8 NCF system — all invoices must bear NCF number from DGII.

- **5.1 Standard rate** — 18%
- **5.2 Reduced rate** — 16% (processed food)
- **5.3 Zero rate** — Exports
- **5.4 Exempt** — Education, healthcare, basic food, fuel
- **5.5 Input credit** — NCF (comprobante fiscal) required
- **5.6 Imports** — 18% on CIF plus duty
- **5.7 Reverse charge** — Non-resident services
- **5.8 NCF system** — All invoices must bear NCF number from DGII

## Section 6 — Tier 2 catalogue

### 6.1 NCF validity. 6.2 ITBIS withholding. 6.3 SaaS — self-assess 18%. 6.4 Cash — exclude.

- **6.1 NCF validity** — NCF validity
- **6.2 ITBIS withholding** — ITBIS withholding
- **6.3 SaaS** — Self-assess 18%
- **6.4 Cash** — Exclude

## Section 7 — Excel working paper template

Output 18%, 16%, Zero-rated, Exempt, Input, Net ITBIS.

## Section 8 — Bank statement reading guide

Banreservas/Popular exports CSV. DOP primary. Spanish descriptions.

## Section 9 — Onboarding fallback

### 9.1 RNC — "Registro Nacional del Contribuyente?" 9.2 Monthly filing. 9.3 Industry. 9.4 Exports. 9.5 Credit B/F.

## Section 10 — Reference material

Sources: 1. Codigo Tributario (Ley 11-92). 2. DGII normas. 3. NCF regulations.

Change log: v2.0 (April 2026): Full rewrite.

## Disclaimer

This skill is for informational purposes only. All outputs must be reviewed by a qualified professional before filing. Latest version at [openaccountants.com](https://openaccountants.com).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
