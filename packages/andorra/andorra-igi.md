---
name: andorra-igi
description: Use this skill whenever asked to prepare, review, or classify transactions for an Andorran IGI (Impost General Indirecte) return for any client. Trigger on phrases like "Andorra VAT", "Andorra IGI", "IGI return", "Andorran tax", or any request involving Andorran indirect tax filing. Andorra does NOT have VAT — it has the IGI at 4.5% standard rate. Andorra is NOT in the EU and is NOT harmonized with the EU VAT Directive. ALWAYS read this skill before touching any Andorran IGI work.
version: 2.0
---

# Andorra IGI Return Skill (Declaracio de l'IGI) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Principality of Andorra |
| Tax name | IGI (Impost General Indirecte) — NOT VAT |
| Standard rate | 4.5% |
| Reduced rate | 1% (food, water, books, cultural events) |
| Intermediate rate | 2.5% (transport, para-pharmaceutical, optical products) |
| Increased rate | 9.5% (banking and financial services) |
| Zero rate | 0% (exports, international transport, gold to Andorran financial institutions) |
| Exempt supplies | Medical, education, insurance, residential rental, social welfare, burial |
| Return form | Declaracio de l'IGI (quarterly) |
| Filing portal | https://www.e-govern.ad |
| Authority | Departament de Tributs i de Fronteres |
| Currency | EUR (used de facto, formal agreement since 2011) |
| Filing frequency | Quarterly (standard); annual summary by 31 March |
| Deadline | Last day of month following quarter end (Q1 by 30 Apr, Q2 by 31 Jul, Q3 by 31 Oct, Q4 by 31 Jan) |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending — requires validation by a licensed Andorran tax practitioner |
| Validation date | Pending |

**Key IGI return boxes:**

| Box | Meaning |
|---|---|
| A1 | Supplies at 4.5% — tax base |
| A2 | Output IGI at 4.5% |
| A3 | Supplies at 1% — tax base |
| A4 | Output IGI at 1% |
| A5 | Supplies at 2.5% — tax base |
| A6 | Output IGI at 2.5% |
| A7 | Supplies at 9.5% — tax base |
| A8 | Output IGI at 9.5% |
| A9 | Zero-rated supplies (exports) |
| A10 | Exempt supplies |
| A11 | Self-assessed IGI on imports of services (reverse charge base) |
| A12 | Output IGI on reverse charge |
| A13 | Total output IGI (A2+A4+A6+A8+A12) |
| B1 | Domestic purchases |
| B2 | Input IGI on domestic purchases |
| B3 | Imports of goods |
| B4 | IGI paid on imports |
| B5 | Fixed asset acquisitions |
| B6 | Input IGI on fixed assets |
| B7 | Input IGI on reverse charge (deductible) |
| B8 | Adjustments |
| B9 | Total input IGI (B2+B4+B6+B7+B8) |
| C1 | IGI payable (if A13 > B9) |
| C2 | IGI credit (if B9 > A13) |
| C3 | Credit from prior period |
| C5 | Net IGI payable |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 4.5% |
| Unknown IGI status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Andorra |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |
| Unknown SaaS billing entity | Reverse charge (Box A11/A12/B7) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 10,000 |
| HIGH tax-delta on a single conservative default | EUR 500 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net IGI position | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the quarter in CSV, PDF, or pasted text. Acceptable from any Andorran bank: Andbank, Creand (formerly Credi Andorra), MoraBanc, Vall Banc, or international banks.

**Recommended** — sales invoices, purchase invoices for claims above EUR 500, the client's NRT (Numero de Registre Tributari).

**Ideal** — complete invoice register, prior period return, reconciliation of prior credit (C3).

### Andorra-specific refusal catalogue

**R-AD-1 — Below registration threshold.** *Trigger:* client has turnover below EUR 40,000 and is not voluntarily registered. *Message:* "Below the mandatory IGI registration threshold. If not voluntarily registered, no IGI return is required."

**R-AD-2 — Financial services at 9.5%.** *Trigger:* complex financial services classification needed. *Message:* "Banking and financial services at 9.5% require specialist analysis to distinguish from exempt financial operations. Flag for reviewer."

**R-AD-3 — Partial exemption (proportional deduction).** *Trigger:* mixed taxable and exempt operations. *Message:* "Proportional deduction required. Annual adjustment needed. Flag for reviewer."

**R-AD-4 — Real property transactions.** *Trigger:* sale of real property. *Message:* "Sale of real property may be subject to IGI or to the Impost sobre les Transmissions Patrimonials. Specialist analysis required."

**R-AD-5 — Tourist IGI refund scheme.** *Trigger:* retail sales to tourists claiming refund. *Message:* "Tourist refund scheme has specific procedures and thresholds. Flag for reviewer."

---

## Section 3 — Supplier pattern library (the lookup table)

### 3.1 Andorran banks (fees at 9.5% or exempt)

| Pattern | Treatment | Notes |
|---|---|---|
| ANDBANK | 9.5% for fee-based services; EXCLUDE for interest | Banking fees at increased rate; interest exempt |
| CREAND, CREDI ANDORRA | Same | Same |
| MORABANC | Same | Same |
| VALL BANC | Same | Same |
| INTERESSI, INTERES | EXCLUDE | Interest, exempt |

### 3.2 Andorran government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| GOVERN D'ANDORRA | EXCLUDE | Government fee, sovereign act |
| TRIBUTS I FRONTERES | EXCLUDE | Tax payment |
| DUANA, CUSTOMS | EXCLUDE for duty; check import IGI for Box B4 |
| CASS | EXCLUDE | Social security |

### 3.3 Andorran utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| FEDA, FORCES ELECTRIQUES D'ANDORRA | Domestic 4.5% | B1/B2 | Electricity |
| ANDORRA TELECOM, STA | Domestic 4.5% | B1/B2 | Telecoms |

### 3.4 Insurance (exempt)

| Pattern | Treatment | Notes |
|---|---|---|
| ASSEGURANCES, SEGUROS | EXCLUDE | Insurance, exempt |

### 3.5 Food retail

| Pattern | Treatment | Notes |
|---|---|---|
| PYRENEENNE, SUPERMERCAT | Domestic 1% for basic food | Reduced rate |
| RESTAURANT, CAFE | Default BLOCK input IGI | Entertainment blocked under Art. 60 |

### 3.6 SaaS — non-resident suppliers (reverse charge)

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Non-resident | A11/A12/B7 | Reverse charge at 4.5% |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Non-resident | A11/A12/B7 | Reverse charge at 4.5% |
| AWS, AMAZON WEB SERVICES | Non-resident | A11/A12/B7 | Reverse charge |

### 3.7 Spanish and French suppliers (imports)

| Pattern | Treatment | Notes |
|---|---|---|
| Spanish entity (ES-) | Import: industrial goods via customs agreement (no duty, IGI at applicable rate) | Agricultural goods: full duty + IGI |
| French entity (FR-) | Same as Spain | Same treatment at border |

### 3.8 Professional services (Andorra)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| ADVOCAT, NOTARI, ASSESSOR FISCAL | Domestic 4.5% | B1/B2 | Professional services |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERENCIA PROPIA, TRASPAS | EXCLUDE | Internal movement |
| DIVIDEND, PRESTEC | EXCLUDE | Out of scope |
| RETIRADA CAIXER | Ask | Default exclude; ask purpose |

---

## Section 4 — Worked examples

### Example 1 — Non-resident service reverse charge (Spanish consulting)

**Input line:**
`05.04.2026 ; CONSULTORIA BARCELONA SL ; DEBIT ; Consulting services ; EUR 5,000`

**Reasoning:**
Spanish entity, no Andorran registration. Reverse charge at 4.5%. Box A11 = EUR 5,000, Box A12 = EUR 225, Box B7 = EUR 225. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | IGI | Rate | Box (input) | Box (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | CONSULTORIA BARCELONA SL | -5,000 | -5,000 | 225 | 4.5% | B7 | A11/A12 | N | — | — |

### Example 2 — Banking service at 9.5%

**Input line:**
`10.04.2026 ; ANDBANK ; DEBIT ; Account management fee Q1 ; -150`

**Reasoning:**
Banking fee at the 9.5% increased rate. Input IGI = 150 / 1.095 * 0.095 = 13.01. Deductible if for business use.

**Output:**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | ANDBANK | -150 | -136.99 | -13.01 | 9.5% | B1/B2 | N | — | — |

### Example 3 — Food sale at 1% reduced rate

**Input line:**
`12.04.2026 ; CASH SALE ; CREDIT ; Daily bakery sales ; +2,020`

**Reasoning:**
Bread and basic food at 1% reduced rate. Net = 2,020 / 1.01 = 2,000. IGI = 20.

**Output:**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 12.04.2026 | CASH SALE | +2,020 | +2,000 | 20 | 1% | A3/A4 | N | — | — |

### Example 4 — Import of industrial goods from Spain

**Input line:**
`18.04.2026 ; SPANISH MACHINERY SL ; DEBIT ; Customs entry — CNC machine ; -30,000`

**Reasoning:**
Industrial goods (HS 25-97) benefit from EU customs agreement: no duty. IGI at 4.5% on customs value. Import IGI = 30,000 * 0.045 = 1,350. Deductible as input IGI if for taxable activity.

**Output:**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | SPANISH MACHINERY SL | -30,000 | -30,000 | -1,350 | 4.5% | B3/B4 or B5/B6 | N | Q1 | "Confirm if capital good" |

### Example 5 — Entertainment, blocked

**Input line:**
`22.04.2026 ; RESTAURANT LA BORDA ; DEBIT ; Client dinner ; -209`

**Reasoning:**
Entertainment expenses are blocked under Art. 60. No input IGI recovery.

**Output:**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | RESTAURANT LA BORDA | -209 | -209 | 0 | — | — | Y | Q2 | "Entertainment: blocked" |

### Example 6 — Export of goods

**Input line:**
`28.04.2026 ; UK CUSTOMER LTD ; CREDIT ; Invoice AD-2026-012 electronics ; +12,000`

**Reasoning:**
Export of goods. Zero-rated under Art. 58. Requires customs export declaration. Input IGI fully deductible.

**Output:**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | UK CUSTOMER LTD | +12,000 | +12,000 | 0 | 0% | A9 | N | — | — |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 4.5% (Art. 57)
Default rate for most goods and services. Sales at Box A1/A2. Purchases at Box B1/B2.

### 5.2 Reduced rate 1% (Art. 57(2))
Basic food, water, books, cultural events. Sales at Box A3/A4.

### 5.3 Intermediate rate 2.5% (Art. 57(3))
Passenger transport, para-pharmaceutical, optical products. Sales at Box A5/A6.

### 5.4 Increased rate 9.5% (Art. 57(4))
Banking and financial services (not exempt). Sales at Box A7/A8. Unusual: most countries exempt financial services.

### 5.5 Zero rate (Art. 58)
Exports, international transport, gold to Andorran financial institutions. Box A9. Full input IGI recovery.

### 5.6 Exempt without credit (Art. 50)
Medical, education, insurance, residential rental, social welfare, burial. No output IGI, no input deduction.

### 5.7 Reverse charge — services from non-residents
Buyer self-assesses IGI at applicable rate. Box A11/A12 (output), Box B7 (input). Net zero for fully taxable.

### 5.8 Imports of goods
IGI collected at customs. Rate depends on goods classification. Box B3/B4. Deductible.

### 5.9 Fixed assets
Capital goods with useful life > 12 months. Box B5/B6 for input IGI.

### 5.10 Blocked input IGI (Art. 60)
No recovery: passenger vehicles for personal use, entertainment, personal consumption, tobacco, jewelry/art/luxury for personal use, without valid invoice.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs
*Default:* 0% recovery for passenger vehicles. *Question:* "Is this a personal or business-only vehicle?"

### 6.2 Entertainment
*Default:* block. *Question:* "Entertainment — blocked regardless."

### 6.3 Financial services classification
*Default:* 9.5% for banking fees; exempt for interest. *Question:* "Is this a fee-based service (9.5%) or interest/exempt operation?"

### 6.4 EU customs agreement classification
*Default:* flag for borderline products. *Question:* "Confirm HS code — industrial (chapters 25-97, no duty) or agricultural (chapters 1-24, full duty)?"

### 6.5 Tourist refund claims
*Default:* flag for reviewer. *Question:* "Are exports to tourists documented with refund scheme paperwork?"

### 6.6 Real property
*Default:* flag for reviewer. *Question:* "Is this subject to IGI or the property transfer tax (ITP)?"

### 6.7 Mixed-use expenses
*Default:* 0% if proportion unknown. *Question:* "What business percentage?"

---

## Section 7 — Excel working paper template (Andorra-specific)

### Sheet "Transactions"
Columns A-L per standard layout. Column H accepts valid Andorran IGI box codes.

### Sheet "Box Summary"
One row per box (A1 through C5). Values computed via SUMIFS from Transactions sheet.

### Sheet "Return Form"
```
A13 = Total output IGI
B9 = Total input IGI
IF B9 > A13: C2 = B9 - A13 (credit)
ELSE: C1 = A13 - B9 (payable)
C5 = C1 - C3 (net payable)
```

---

## Section 8 — Andorra bank statement reading guide

**Format conventions.** Andorran banks (Andbank, Creand, MoraBanc) typically export in CSV with DD/MM/YYYY dates. EUR currency only.

**Language.** Descriptions in Catalan (official), Spanish, or French. Treat equivalently.

**Internal transfers.** "Traspas entre comptes", "transferencia propia". Always exclude.

**Customs entries.** Goods arrive via Spanish (southern) or French (northern) border only. Look for "duana" entries.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference:* SL, SA in name = company. Individual name = sole trader. *Fallback:* "Entity type?"

### 9.2 IGI registration
*Inference:* if asking for IGI return, registered. *Fallback:* "Are you registered for IGI (above EUR 40,000 turnover)?"

### 9.3 NRT
*Fallback:* "What is your NRT?"

### 9.4 Period
*Inference:* from statement dates. *Fallback:* "Which quarter?"

### 9.5 Industry
*Inference:* counterparty mix. *Fallback:* "What does the business do?"

### 9.6 Prior credit
Always ask: "Do you have IGI credit from last quarter? (Box C3)"

---

## Section 10 — Reference material

### Sources
1. Llei 11/2012, del 21 de juny, de l'Impost General Indirecte — Articles 4, 50, 57, 58, 59, 60, 78, 85
2. Reglament de l'IGI
3. Llei 21/2014 and Llei 3/2019 (amendments)
4. EU Customs Agreement Decision 90/680/EEC

### Known gaps
1. Tourist IGI refund scheme procedures and current thresholds need practitioner verification.
2. Financial services IGI vs. exempt boundary requires specialist analysis.
3. EU customs agreement product classification for borderline goods.

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
