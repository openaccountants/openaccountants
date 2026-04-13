---
name: ecuador-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for an Ecuador IVA (Impuesto al Valor Agregado) return (Formulario 104) for any client. Trigger on phrases like "prepare IVA return", "Ecuador VAT", "Formulario 104", "SRI return", or any request involving Ecuador value added tax filing. This skill covers Regimen General taxpayers only. RIMPE Negocios Populares, oil-sector service contracts, and ZEDE entities are in the refusal catalogue. ALWAYS read this skill before touching any Ecuador IVA work.
version: 2.0
---

# Ecuador IVA Return Skill (Formulario 104) v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Ecuador |
| Standard rate | 15% (from 1 April 2024; confirmed through 2026) |
| Previous rate | 12% (periods before 1 April 2024) |
| Zero rate (tarifa 0%) | Unprocessed agricultural products, medicines, books, agricultural inputs, basic food basket (canasta basica), public transport, medical services, education, residential rental, financial interest |
| Return form | Formulario 104 |
| Filing portal | https://www.sri.gob.ec (SRI en Linea) |
| Authority | Servicio de Rentas Internas (SRI) |
| Currency | USD (Ecuador uses US dollar) |
| Filing frequency | Monthly (standard); semi-annual (RIMPE emprendedores) |
| Deadline | Depends on 9th digit of RUC (10th-28th of following month) |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending — requires validation by a licensed CPA in Ecuador |
| Validation date | Pending |

**Key Formulario 104 lines:**

| Line | Meaning |
|---|---|
| 401 | Taxable sales (excl. fixed assets) — tarifa diferente de 0% |
| 402 | Sales of fixed assets — taxable |
| 403 | Tarifa 0% sales (no credit right) |
| 404 | Tarifa 0% sales (with credit right) |
| 405 | Exports of goods |
| 406 | Exports of services |
| 409 | Total sales |
| 411 | Output IVA (IVA generado en ventas) |
| 500 | Taxable purchases (excl. fixed assets) |
| 501 | Fixed asset purchases — taxable |
| 502 | Non-taxable purchases |
| 503 | Taxable imports |
| 504 | Fixed asset imports — taxable |
| 510 | Input IVA on purchases |
| 511 | Input IVA on imports |
| 601 | IVA causado (output) |
| 602 | Credito tributario aplicable (input credit) |
| 605 | Factor de proporcionalidad |
| 699 | Tax payable / credit balance |
| 721 | IVA withholdings received |
| 902 | Total payable |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% |
| Unknown IVA status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Ecuador |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |
| Unknown SaaS billing entity | Reverse charge at 15% |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | USD 5,000 |
| HIGH tax-delta on a single conservative default | USD 500 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net IVA position | USD 10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. Acceptable from: Banco Pichincha, Banco del Pacifico, Produbanco, Banco Guayaquil, Banco Bolivariano, Cooperativa JEP, or any other.

**Recommended** — electronic invoices (facturas electronicas) for the period, comprobantes de retencion, RUC number.

**Ideal** — complete ATS (Anexo Transaccional Simplificado), prior Formulario 104, credit balance reconciliation.

### Ecuador-specific refusal catalogue

**R-EC-1 — RIMPE Negocio Popular.** *Trigger:* client is RIMPE Negocio Popular (income under USD 20,000). *Message:* "RIMPE Negocios Populares pay a fixed annual quota and do not charge IVA separately. No Formulario 104 is filed."

**R-EC-2 — Oil sector service contracts.** *Trigger:* client has service contracts with EPPETROECUADOR. *Message:* "Oil sector service contracts have specialized IVA treatment. Escalate to specialist."

**R-EC-3 — ZEDE / special economic zone.** *Trigger:* client operates in a ZEDE. *Message:* "ZEDE entities have special IVA rules. Flag for reviewer."

**R-EC-4 — Partial exemption (Factor de Proporcionalidad).** *Trigger:* client makes both tarifa 15% and tarifa 0% (no credit) sales. *Message:* "Mixed operations require the Factor de Proporcionalidad. Flag for reviewer to confirm calculation."

---

## Section 3 — Supplier pattern library

### 3.1 Ecuadorian banks (fees taxable, interest exempt)

| Pattern | Treatment | Notes |
|---|---|---|
| BANCO PICHINCHA, BP | 15% for fees; EXCLUDE for interest | Banking fees taxable; interest tarifa 0% |
| BANCO DEL PACIFICO, PRODUBANCO | Same | Same |
| BANCO GUAYAQUIL, BOLIVARIANO | Same | Same |
| COOPERATIVA JEP | Same | Same |
| INTERESES, INTERES | EXCLUDE | Interest, tarifa 0% |

### 3.2 Government and regulators (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SRI, SERVICIO DE RENTAS INTERNAS | EXCLUDE | Tax payment |
| IESS, INSTITUTO ECUATORIANO DE SEGURIDAD SOCIAL | EXCLUDE | Social security |
| SENAE, ADUANA | EXCLUDE for duty; check import IVA |
| MUNICIPIO, GAD | EXCLUDE | Government fee |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| EMPRESA ELECTRICA, EEQ, CNEL | Domestic 15% | Commercial electricity |
| CNT, CORPORACION NACIONAL TELECOMUNICACIONES | Domestic 15% | Telecoms |
| CLARO, MOVISTAR, TUENTI | Domestic 15% | Mobile |
| EMPRESA DE AGUA, EMAAP | Tarifa 0% (domestic, up to threshold) | Water |

### 3.4 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| SEGUROS (general) | Domestic 15% | General insurance taxable |
| SEGURO DE VIDA, SEGURO MEDICO | Tarifa 0% | Life/health insurance exempt |

### 3.5 SaaS — non-resident (reverse charge)

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Reverse charge 15% | Self-assess output and input IVA |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Reverse charge 15% | Same |
| AWS, AMAZON WEB SERVICES | Reverse charge 15% | Same |

### 3.6 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| SUPERMAXI, MEGAMAXI, TIA, MI COMISARIATO | Default BLOCK input IVA | Personal provisioning |
| RESTAURANT, RESTAURANTE | Default BLOCK | Entertainment blocked |

### 3.7 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| ABOGADO, ESTUDIO JURIDICO | Domestic 15% | Withhold 70% or 100% of IVA |
| CONTADOR, CPA | Domestic 15% | Same |
| NOTARIA | Domestic 15% | Same |

### 3.8 Payroll and social security (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| IESS, FONDOS DE RESERVA | EXCLUDE | Social security |
| NOMINA, SUELDO, SALARIO | EXCLUDE | Wages |
| IMPUESTO A LA RENTA, IR | EXCLUDE | Income tax |

### 3.9 Internal transfers

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERENCIA PROPIA, TRASPASO | EXCLUDE | Internal movement |
| DIVIDENDO | EXCLUDE | Out of scope |
| RETIRO ATM, CAJERO | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:**
`05.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00`

**Reasoning:** US entity. Self-assess IVA at 15%. Output = USD 2.40. Input = USD 2.40. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line (input) | Line (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | NOTION LABS INC | -16.00 | -16.00 | 2.40 | 15% | 510 | 411 | N | — | — |

### Example 2 — Standard domestic sale

**Input line:**
`10.04.2026 ; CIA TECHSOLUTION SA ; CREDIT ; Invoice 2026-041 consulting ; +5,750`

**Reasoning:** Domestic taxable sale at 15%. Net = 5,750 / 1.15 = 5,000. IVA = 750.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | CIA TECHSOLUTION SA | +5,750 | +5,000 | 750 | 15% | 401/411 | N | — | — |

### Example 3 — Entertainment, blocked

**Input line:**
`15.04.2026 ; RESTAURANTE EL MESON ; DEBIT ; Business dinner ; -115`

**Reasoning:** Entertainment blocked. No input IVA recovery.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANTE EL MESON | -115 | -115 | 0 | — | — | Y | Q1 | "Entertainment: blocked" |

### Example 4 — Export of goods (bananas)

**Input line:**
`18.04.2026 ; FRUIT IMPORT GMBH ; CREDIT ; Invoice EC-2026-088 bananas ; +100,000`

**Reasoning:** Export of goods. Tarifa 0% with full input credit recovery. Line 405.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | FRUIT IMPORT GMBH | +100,000 | +100,000 | 0 | 0% | 405 | N | — | — |

### Example 5 — Motor vehicle, blocked

**Input line:**
`22.04.2026 ; AUTOMOTORES SA ; DEBIT ; Sedan purchase ; -25,000`

**Reasoning:** Passenger vehicle. Input IVA blocked.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | AUTOMOTORES SA | -25,000 | -25,000 | 0 | — | — | Y | Q2 | "Motor vehicle: blocked" |

### Example 6 — Professional services with IVA withholding

**Input line:**
`28.04.2026 ; ING. PEDRO GARCIA ; DEBIT ; Consulting fee ; -2,300`

**Reasoning:** Professional service from individual. IVA = 2,300 / 1.15 * 0.15 = 300. Must withhold 100% of IVA = 300. Issue comprobante de retencion within 5 days.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | ING. PEDRO GARCIA | -2,300 | -2,000 | -300 | 15% | 500/510 | N | Q3 | "Withhold 100% IVA" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 15% (LRTI Art. 65)
Default rate for all taxable transfers. Sales at Line 401/411. Purchases at Line 500/510.

### 5.2 Tarifa 0% goods (LRTI Art. 55)
Unprocessed agricultural products, medicines, agricultural inputs, books, infant formula, feminine hygiene, seeds.

### 5.3 Tarifa 0% services (LRTI Art. 56)
Medical, education, public transport, residential rental, financial interest, insurance (life/health), electricity/water (domestic thresholds), funerals.

### 5.4 Exports (LRTI Art. 55-56)
Zero-rated with full input credit. Goods at Line 405. Services at Line 406.

### 5.5 Reverse charge — imported services
Self-assess at 15%. Report output and input. Net zero for fully taxable.

### 5.6 IVA withholding (LRTI Art. 63)
Goods from general taxpayer: 30%. Services from general: 70%. Professional individuals: 100%. Government: 100%. Exporters: 100%.

### 5.7 Blocked input IVA (LRTI Art. 66)
Personal use, entertainment, motor vehicles (except rental/taxi/transport), purchases without valid electronic comprobante.

### 5.8 Factor de Proporcionalidad
Mixed operations: Factor = (Taxable + Exports) / Total Sales. Apply to common input IVA.

### 5.9 Electronic invoicing
Mandatory for all taxpayers. Input IVA only deductible with SRI-authorized electronic documents.

### 5.10 ICE interaction (LRTI Art. 75-89)
ICE is separate. IVA is calculated on price inclusive of ICE.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Rate change transition
*Default:* 15% for all current periods. 12% only for pre-April 2024. *Question:* "Confirm transaction date for rate determination."

### 6.2 Exporter IVA recovery
*Default:* full recovery for exporters. *Question:* "Are all costs attributable to exports?"

### 6.3 CAN country services
*Default:* reverse charge. *Question:* "Confirm CAN Decision 599 implications."

### 6.4 Artisan sector
*Default:* flag for reviewer. *Question:* "Is JNDA registration current?"

### 6.5 Tourism packages
*Default:* flag. *Question:* "Incoming foreign tourist package — confirm tarifa 0% eligibility."

### 6.6 Mixed operations proportionality
*Default:* flag for reviewer. *Question:* "Confirm factor calculation."

---

## Section 7 — Excel working paper template

### Sheet "Transactions"
Columns A-L. Column H accepts Formulario 104 line numbers.

### Sheet "Return Summary"
```
Line 601 = Output IVA
Line 602 = Input credit (after factor)
Line 699 = 601 - 602
Line 902 = 699 - 721 (withholdings)
```

---

## Section 8 — Ecuador bank statement reading guide

**Format:** Banco Pichincha exports CSV with DD/MM/YYYY. USD currency.

**Language:** Spanish. "Transferencia", "deposito", "retiro".

**Internal transfers:** "Traspaso entre cuentas". Always exclude.

**RUC-based deadline:** Filing date depends on 9th digit of RUC (10th-28th).

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
*Inference:* SA, CIA LTDA = company. *Fallback:* "Entity type?"

### 9.2 Tax regime
*Inference:* if filing F104, Regimen General. *Fallback:* "Regimen General or RIMPE?"

### 9.3 RUC
*Fallback:* "What is your 13-digit RUC?"

### 9.4 Period
*Inference:* from statement dates. *Fallback:* "Which month?"

### 9.5 Industry
*Inference:* counterparty mix. *Fallback:* "What does the business do?"

### 9.6 Credit balance
Always ask: "Credit balance from prior period?"

---

## Section 10 — Reference material

### Sources
1. Ley de Regimen Tributario Interno (LRTI) — Articles 53-73
2. Reglamento LRTI — Article 193
3. Codigo Tributario
4. Executive Decree 198 (March 2024, rate increase)
5. SRI en Linea — https://www.sri.gob.ec

### Known gaps
1. ZEDE-specific IVA rules need specialist verification.
2. Artisan sector JNDA registration status must be current.
3. Digital services taxation from non-residents is evolving.

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
