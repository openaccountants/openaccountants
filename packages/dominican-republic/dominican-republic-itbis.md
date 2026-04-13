---
name: dominican-republic-itbis
description: Use this skill whenever asked to prepare, review, or classify transactions for a Dominican Republic ITBIS return for any client. Trigger on phrases like "ITBIS", "Dominican Republic VAT", "DGII filing", or any request involving DR consumption tax. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any ITBIS work.
version: 2.0
---

# Dominican Republic ITBIS Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
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

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 18% |
| Unknown input credit status | Not creditable |
| Unknown counterparty location | Domestic DR |

---

## Section 2 — Required inputs and refusal catalogue

**Minimum viable** — bank statement. Acceptable from: Banreservas, Banco Popular Dominicano, Scotiabank DR, BHD Leon, Banco Santa Cruz, or any other.

**R-DO-1 — Free trade zone entity.** Message: "FTZ entities have bespoke ITBIS exemptions. Please escalate."
**R-DO-2 — Withholding agent for ITBIS.** Message: "ITBIS withholding obligations require certificate tracking. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Dominican banks (exclude)
| Pattern | Treatment | Notes |
|---|---|---|
| BANRESERVAS, BANCO DE RESERVAS | EXCLUDE | Financial service |
| POPULAR, BANCO POPULAR | EXCLUDE | Same |
| BHD LEON, SCOTIABANK DR | EXCLUDE | Same |

### 3.2 Government (exclude)
| Pattern | Treatment | Notes |
|---|---|---|
| DGII | EXCLUDE | Tax payment |
| DGA, ADUANAS | EXCLUDE | Customs |
| TSS, SOCIAL SECURITY | EXCLUDE | Social security |

### 3.3 Utilities
| Pattern | Treatment | Notes |
|---|---|---|
| EDENORTE, EDESUR, EDEESTE | Domestic 18% | Electricity |
| CAASD, INAPA | Domestic 18% | Water |
| CLARO DR, ALTICE, WIND TELECOM | Domestic 18% | Telecoms |

### 3.4 SaaS and international
| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 18% | Non-resident |

### 3.5 Payroll/exclusions
| Pattern | Treatment | Notes |
|---|---|---|
| SALARIO, WAGES | EXCLUDE | Outside ITBIS scope |
| TRANSFERENCIA PROPIA | EXCLUDE | Internal |

---

## Section 4 — Worked examples

### Example 1 — Domestic sale at 18%
**Input:** `05.04.2026 ; CLIENTE DOMINICANO SRL ; CREDIT ; Factura DO-041 ; DOP 118,000`
Net = DOP 100,000, ITBIS = DOP 18,000.

| Date | Counterparty | Gross | Net | ITBIS | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | CLIENTE DOMINICANO | +118,000 | +100,000 | 18,000 | 18% | Output | N | — |

### Example 2 — Export, zero-rated
**Input:** `15.04.2026 ; US BUYER ; CREDIT ; Export ; DOP 500,000`

| Date | Counterparty | Gross | Net | ITBIS | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | US BUYER | +500,000 | +500,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Bank charges
**Input:** `30.04.2026 ; BANRESERVAS ; DEBIT ; Comision ; DOP -200`

| Date | Counterparty | Gross | Net | ITBIS | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | BANRESERVAS | -200 | — | — | — | — | N | "Financial" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 18%. 5.2 Reduced 16% (processed food). 5.3 Zero rate — exports. 5.4 Exempt — education, healthcare, basic food, fuel. 5.5 Input credit — NCF (comprobante fiscal) required. 5.6 Imports — 18% on CIF plus duty. 5.7 Reverse charge — non-resident services. 5.8 NCF system — all invoices must bear NCF number from DGII.

---

## Section 6 — Tier 2 catalogue
### 6.1 NCF validity. 6.2 ITBIS withholding. 6.3 SaaS — self-assess 18%. 6.4 Cash — exclude.

---

## Section 7 — Excel working paper template
Output 18%, 16%, Zero-rated, Exempt, Input, Net ITBIS.

## Section 8 — Bank statement reading guide
Banreservas/Popular exports CSV. DOP primary. Spanish descriptions.

## Section 9 — Onboarding fallback
### 9.1 RNC — "Registro Nacional del Contribuyente?" 9.2 Monthly filing. 9.3 Industry. 9.4 Exports. 9.5 Credit B/F.

## Section 10 — Reference material
Sources: 1. Codigo Tributario (Ley 11-92). 2. DGII normas. 3. NCF regulations.

Change log: v2.0 (April 2026): Full rewrite.

---

## Disclaimer
This skill is for informational purposes only. All outputs must be reviewed by a qualified professional before filing. Latest version at [openaccountants.com](https://openaccountants.com).
