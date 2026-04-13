---
name: el-salvador-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for an El Salvador IVA return (F-07) for any client. Trigger on phrases like "prepare IVA return", "El Salvador VAT", "F-07", "DGII return", or any request involving El Salvador value added tax filing. This skill covers standard IVA filers only. Free-zone (Zona Franca) and maquila entities are in the refusal catalogue. ALWAYS read this skill before touching any El Salvador IVA work.
version: 2.0
---

# El Salvador IVA Return Skill (F-07) v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | El Salvador |
| Standard rate | 13% |
| Exempt supplies | Unprocessed agricultural products, medicines, agricultural inputs, books, medical services, education, financial interest, insurance (life), residential rental, public transport, water, electricity (domestic first tier), fuel (subject to specific tax) |
| Return form | F-07 |
| Filing portal | https://portaldgii.mh.gob.sv |
| Authority | Ministerio de Hacienda / DGII |
| Currency | USD |
| Filing frequency | Monthly |
| Deadline | 10th business day of month following the period |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending |
| Validation date | Pending |

**Key F-07 lines:**

| Line | Meaning |
|---|---|
| 1 | Domestic taxable sales (ventas internas gravadas) |
| 2 | B2B taxable sales (ventas a contribuyentes) |
| 3 | B2C taxable sales (ventas a consumidor final) |
| 4 | Exports at 0% |
| 5 | Exempt sales |
| 6 | Total sales |
| 7 | Debito fiscal (output IVA at 13%) |
| 8 | Domestic taxable purchases |
| 9 | Taxable imports |
| 10 | Input IVA — local |
| 11 | Input IVA — imports |
| 12 | Total input IVA |
| 13 | Adjustments (blocked/apportioned) |
| 14 | Net input IVA |
| 15 | Tax determined (7 - 14) |
| 16 | Prior credit balance |
| 17 | Retentions and perceptions |
| 18 | Total payable / carry-forward |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 13% |
| Unknown IVA status of a purchase | Not deductible |
| Unknown counterparty country | Domestic El Salvador |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |
| Unknown document type | Factura (no credit) until CCF confirmed |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | USD 5,000 |
| HIGH tax-delta on a single conservative default | USD 300 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net IVA position | USD 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: Banco Agricola, Banco Cuscatlan, Davivienda, BAC Credomatic, Banco de America Central, or any other.

**Recommended** — Comprobantes de Credito Fiscal (CCF), Documentos Tributarios Electronicos (DTE), comprobantes de retencion.

**Ideal** — complete Libro de Compras y Ventas, prior F-07, DTE register.

### El Salvador-specific refusal catalogue

**R-SV-1 — Zona Franca entity.** *Trigger:* client operates in a free trade zone. *Message:* "Free zone companies have specific IVA exemptions under the Ley de Zonas Francas. Requires valid DPA authorization. Escalate to specialist."

**R-SV-2 — Maquila operations.** *Trigger:* client operates under maquila regime. *Message:* "Maquila operations have special IVA treatment. Maquila license must be current. Escalate."

**R-SV-3 — Partial exemption.** *Trigger:* mixed taxable and exempt supplies. *Message:* "Proportional method required for common costs. Flag for reviewer."

---

## Section 3 — Supplier pattern library

### 3.1 Banks (fees taxable, interest exempt)

| Pattern | Treatment | Notes |
|---|---|---|
| BANCO AGRICOLA, BAC | 13% for fees; EXCLUDE for interest | |
| BANCO CUSCATLAN, DAVIVIENDA | Same | |
| INTERESES | EXCLUDE | Interest exempt |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MINISTERIO DE HACIENDA, MH, DGII | EXCLUDE | Tax payment |
| ISSS | EXCLUDE | Social security |
| AFP | EXCLUDE | Pension |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| CAESS, CLESA, DELSUR, AES | Domestic 13% (commercial) | Electricity |
| ANDA | Exempt (domestic water) | |
| CTE, CLARO, TIGO, DIGICEL | Domestic 13% | Telecoms |

### 3.4 SaaS — non-resident (reverse charge)

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Reverse charge 13% | Self-assess output and input |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Reverse charge 13% | Same |

### 3.5 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| SUPER SELECTOS, WALMART, PRICESMART | Default BLOCK | Personal provisioning |
| RESTAURANT, RESTAURANTE | Default BLOCK | Entertainment blocked |

### 3.6 Fuel

| Pattern | Treatment | Notes |
|---|---|---|
| PUMA, SHELL, TEXACO, UNO | Exempt (fuel subject to specific tax) | No IVA component |

### 3.7 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| ABOGADO, CONTADOR, NOTARIO | Domestic 13% | Must have CCF for input credit |

### 3.8 Internal transfers

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERENCIA PROPIA | EXCLUDE | |
| SALARIO, PLANILLA | EXCLUDE | |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge
**Input:** `NOTION LABS INC ; DEBIT ; USD 16.00`
**Treatment:** Reverse charge at 13%. Output = USD 2.08. Input = USD 2.08. Net zero.

### Example 2 — B2B domestic sale
**Input:** `SA CLIENTE ; CREDIT ; Invoice SV-041 ; USD 5,650`
**Treatment:** Net = 5,000. IVA = 650. Line 2/7.

### Example 3 — Entertainment, blocked
**Input:** `RESTAURANTE LA PAMPA ; DEBIT ; USD 113`
**Treatment:** Blocked. No input credit.

### Example 4 — Export
**Input:** `US BUYER INC ; CREDIT ; USD 50,000`
**Treatment:** Line 4. Zero-rated. Full input credit.

### Example 5 — Motor vehicle, blocked
**Input:** `AUTOMOTRIZ SA ; DEBIT ; Sedan ; USD 20,000`
**Treatment:** Blocked. No input credit.

### Example 6 — Purchase with Factura (no CCF)
**Input:** `TIENDA X ; DEBIT ; Factura Consumidor Final ; IVA USD 65`
**Treatment:** IVA NOT deductible. No CCF = no credit. Request CCF from supplier.

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 13% (Ley del IVA Art. 54)
Default for all taxable supplies. B2B sales: Line 2/7. B2C sales: Line 3/7.

### 5.2 Exempt goods (Art. 44)
Unprocessed agricultural products, medicines, agricultural inputs, books, fuel.

### 5.3 Exempt services (Art. 46)
Medical, education, financial interest, insurance (life), residential rental, public transport, water, electricity (domestic).

### 5.4 Exports
Zero-rated with full input credit. Line 4.

### 5.5 Reverse charge (Art. 14-A)
Services from non-residents: self-assess at 13%.

### 5.6 Retention/perception system
Large taxpayer purchasing from small/medium: retain 1% of purchase price. Government: retain 1%.

### 5.7 Blocked input IVA (Art. 65)
Entertainment, motor vehicles, personal use, exempt operations, purchases without CCF.

### 5.8 Document requirements
B2B: CCF (supports input credit). B2C: Factura Consumidor Final (no credit for buyer). DTE replaces paper.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Agricultural first sale
*Default:* flag. *Question:* "Confirm first sale by producer — exempt."

### 6.2 Cross-border services
*Default:* flag. *Question:* "Consumed outside El Salvador? May qualify as export."

### 6.3 Bitcoin payment
*Default:* IVA applies on underlying supply. *Question:* "Value in USD at time of transaction."

### 6.4 Real estate
*Default:* flag. *Question:* "First transfer of new construction (13%) or subsequent (exempt)?"

### 6.5 DTE rollout
*Default:* flag. *Question:* "Is DTE mandatory for this taxpayer category yet?"

---

## Section 7 — Excel working paper template

### Sheet "Transactions"
Columns A-L. Column H accepts F-07 line numbers.

### Sheet "Return Summary"
```
Line 7 = Output IVA
Line 14 = Net input IVA
Line 15 = 7 - 14
Line 18 = 15 - 16 - 17
```

---

## Section 8 — Bank statement reading guide

**Format:** Banco Agricola CSV with DD/MM/YYYY. USD currency.
**Language:** Spanish.
**Internal transfers:** "Transferencia entre cuentas". Exclude.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
*Inference:* SA de CV, S de RL in name. *Fallback:* "Entity type?"

### 9.2 NIT and NRC
*Fallback:* "What is your 14-digit NIT and NRC?"

### 9.3 Period
*Inference:* from statement dates. *Fallback:* "Which month?"

### 9.4 Large taxpayer status
*Inference:* retention activity on statement. *Fallback:* "Are you designated as a large taxpayer by MH?"

### 9.5 Credit balance
Always ask: "Prior credit balance? (Line 16)"

---

## Section 10 — Reference material

### Sources
1. Ley del IVA, Decreto Legislativo 296 — Articles 4, 14-A, 44, 45, 46, 54, 65
2. Reglamento de la Ley del IVA
3. Codigo Tributario

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
