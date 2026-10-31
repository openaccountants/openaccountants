---
name: guatemala-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Guatemala IVA return (SAT-2237) for any client. Trigger on phrases like "prepare IVA return", "Guatemala VAT", "SAT return", "IVA Guatemala", or any request involving Guatemala value added tax filing. This skill covers Regimen General IVA filers only. Small taxpayer (Pequeno Contribuyente) regime and ZOLIC free-zone entities are in the refusal catalogue. ALWAYS read this skill before touching any Guatemala IVA work.
version: 2.0
jurisdiction: GT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guatemala IVA

## Section 1 — Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Guatemala |
| Standard rate | 12% |
| Small taxpayer rate | 5% flat (replaces IVA and income tax — separate regime) |
| Exempt supplies | Unprocessed agricultural products (first sale), generic medicines, agricultural inputs (artisanal), books, medical services, education, financial interest, insurance, residential rental, public transport, electricity/water (domestic) |
| Return form | SAT-2237 |
| Filing portal | https://portal.sat.gob.gt (Agencia Virtual) |
| Authority | SAT (Superintendencia de Administracion Tributaria) |
| Currency | GTQ (Guatemalan Quetzal) |
| Filing frequency | Monthly |
| Deadline | Last business day of month following period |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending |
| Validation date | Pending |

**Key SAT-2237 lines**

| Line | Meaning |
| --- | --- |
| 1 | Taxable sales and services (ventas y servicios gravados) |
| 2 | Output IVA (debito fiscal) = Line 1 x 12% |
| 3 | Exports at 0% |
| 4 | Exempt sales |
| 5 | Total sales (1+3+4) |
| 6 | Reverse charge on imports (auto-declared IVA) |
| 7 | Total output IVA (2+6) |
| 8 | Input IVA on local purchases |
| 9 | Input IVA on imports (customs) |
| 10 | Input IVA on expenses/services |
| 11 | Total input IVA (8+9+10) |
| 12 | Adjustments (blocked/apportioned) |
| 13 | Net input IVA (11-12) |
| 14 | IVA payable (7-13) |
| 15 | Prior credit balance |
| 16 | IVA retentions |
| 17 | Total payable / carry-forward |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 12% |
| Unknown IVA status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Guatemala |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |
| Unknown document type | No credit until valid FEL confirmed |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | GTQ 50,000 |
| HIGH tax-delta on a single conservative default | GTQ 5,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 |
| LOW absolute net IVA position | GTQ 100,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable input** — bank statement for the month. Acceptable from: Banco Industrial, Banrural, BAM, G&T Continental, Banco de los Trabajadores, or any other.
- **Recommended input** — FEL (Factura Electronica en Linea) documents, constancias de retencion.
- **Ideal input** — complete Libro de Compras y Ventas, prior SAT-2237, FEL register.

### Refusal catalogue

- **R-GT-1 — Pequeno Contribuyente** — Small taxpayers pay 5% flat tax and do NOT file IVA returns or claim input credits. (Trigger: client is under small taxpayer regime (income up to GTQ 150,000).)
- **R-GT-2 — ZOLIC free zone** — Free zone benefits require valid authorization. Escalate. (Trigger: client in ZOLIC.)
- **R-GT-3 — Partial exemption** — Proportional method required. Flag for reviewer. (Trigger: mixed taxable/exempt.)

### 3.1 Banks

**Banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BANCO INDUSTRIAL, BI | 12% for fees; EXCLUDE for interest |  |
| BANRURAL, BAM, G&T | Same |  |

### 3.2 Government (exclude)

**Government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SAT, SUPERINTENDENCIA | EXCLUDE | Tax payment |
| IGSS | EXCLUDE | Social security |

### 3.3 Utilities

**Utilities pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EEGSA, ENERGUATE | Domestic 12% | Electricity |
| TIGO, CLARO, MOVISTAR | Domestic 12% | Telecoms |
| EMPAGUA | Exempt (domestic water) |  |

### 3.4 SaaS non-resident (reverse charge)

**SaaS non-resident pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | Reverse charge 12% | Line 6 output, Line 10 input |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Reverse charge 12% | Same |

### 3.5 Food and entertainment (blocked)

**Food and entertainment pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAIZ, WALMART, LA TORRE | Default BLOCK | Personal provisioning |
| RESTAURANT, RESTAURANTE | Default BLOCK | Entertainment |

### 3.6 Professional services

**Professional services pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ABOGADO, NOTARIO, CONTADOR | Domestic 12% | Requires valid FEL |

### 3.7 Internal transfers

**Internal transfers pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA | EXCLUDE |  |
| PLANILLA, SALARIO | EXCLUDE |  |

### Example 1 — Non-resident reverse charge

**Input:** `NOTION LABS INC ; DEBIT ; GTQ 245`
**Treatment:** Reverse charge 12%. Output Line 6. Input Line 10. Net zero.

### Example 2 — Standard domestic sale

**Input:** `SA CLIENTE ; CREDIT ; GTQ 112,000`
**Treatment:** Net = 100,000. IVA = 12,000. Line 1/2.

### Example 3 — Entertainment, blocked

**Input:** `RESTAURANTE KACAO ; DEBIT ; GTQ 2,240`
**Treatment:** Blocked. No input credit.

### Example 4 — Coffee export

**Input:** `US ROASTER INC ; CREDIT ; GTQ 200,000`
**Treatment:** Line 3. Zero-rated. Full input credit.

### Example 5 — Motor vehicle, blocked

**Input:** `AUTOMOTRIZ GT ; DEBIT ; Sedan GTQ 150,000`
**Treatment:** Blocked. No input credit.

### Example 6 — Purchase without FEL

**Input:** `VENDEDOR X ; handwritten receipt ; IVA GTQ 600`
**Treatment:** NOT deductible. No valid FEL = no credit.

### 5.1 Standard rate 12% (Decreto 27-92 Art. 10)

- **Standard rate default** — Default for all taxable supplies.  _(Decreto 27-92 Art. 10)_

### 5.2 Small taxpayer 5% (Decreto 27-92 Art. 45)

- **Small taxpayer flat tax** — Flat tax. No IVA charged, no input credits. Buyers get no IVA credit from pequeno contribuyente.  _(Decreto 27-92 Art. 45)_

### 5.3 Exempt goods (Art. 7)

- **Exempt goods** — Unprocessed agricultural (first sale), generic medicines, artisanal agricultural inputs, books, live animals (production).  _(Art. 7)_

### 5.4 Exempt services

- **Exempt services** — Education, medical, financial interest, insurance, residential rental, public transport, domestic electricity/water.

### 5.5 Exports

- **Exports treatment** — Zero-rated. Line 3. Full input credit.

### 5.6 Reverse charge — non-resident services

- **Reverse charge non-resident services** — Self-assess 12%. Line 6 output, Line 10 input.

### 5.7 FEL mandatory electronic invoicing

- **FEL mandatory invoicing** — All invoices must be FEL-certified. Input IVA only valid with FEL.

### 5.8 Blocked input IVA (Art. 16, 18)

- **Blocked input IVA** — Entertainment, motor vehicles, personal use, exempt operations, without valid FEL.  _(Art. 16, 18)_

### 5.9 Factura Especial (Art. 52)

- **Factura Especial** — Purchase from unregistered person: buyer issues Factura Especial, self-assesses IVA 12% and ISR 5%.  _(Art. 52)_

### 5.10 IVA retention regime

- **IVA retention regime** — Designated agents retain varying percentages of IVA. Credit card processors: 15%. Government: 25%. Exporters: 65%.

### 6.1 Agricultural first sale

- **Agricultural first sale default/question** — Default: flag. Question: "Confirm qualifying first sale."

### 6.2 Real estate

- **Real estate default/question** — Default: flag. Question: "First sale new construction (12%) or subsequent/bare land (exempt)?"

### 6.3 Cross-border Central American services

- **Cross-border Central American services default/question** — Default: flag. Question: "Consumed outside Guatemala? Export?"

### 6.4 Transport vehicle

- **Transport vehicle default/question** — Default: flag. Question: "Exclusively for goods/passenger transport business?"

## Section 7 — Excel working paper template

Standard layout. Column H accepts SAT-2237 line numbers.

## Section 8 — Bank statement reading guide

**Format:** Banco Industrial CSV, DD/MM/YYYY, GTQ. **Language:** Spanish.

### 9.1 Tax regime

- **Tax regime inference/fallback** — Inference: if filing SAT-2237, Regimen General. Fallback: "Regimen General or Pequeno Contribuyente?"

### 9.2 NIT

- **NIT fallback** — Fallback: "What is your NIT?"

### 9.3 Prior credit

- **Prior credit always ask** — Always ask: "Prior credit balance? (Line 15)"

### Sources

1. Decreto 27-92, Ley del IVA — Articles 3, 7, 10, 16, 18, 37, 45, 48, 52
2. Decreto 10-2012, Ley de Actualizacion Tributaria
3. SAT FEL regulations

### Change log

- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

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
