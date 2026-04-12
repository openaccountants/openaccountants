---
name: azerbaijan-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Azerbaijan VAT (EDV) return for any client. Trigger on phrases like "Azerbaijan VAT", "EDV return", "Azerbaijani tax", or any request involving Azerbaijan VAT filing. This skill covers standard EDV payers filing monthly returns. Simplified tax regime and micro-enterprise exemptions are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Azerbaijan VAT work.
version: 2.0
---

# Azerbaijan VAT (EDV) Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Azerbaijan (Republic of Azerbaijan) |
| Tax name | EDV (Elave Deger Vergisi / Value Added Tax) |
| Standard rate | 18% |
| Reduced rates | None (single standard rate) |
| Zero rate | 0% (exports, international transport, diplomatic supplies, certain agricultural produce) |
| Return form | Monthly EDV declaration |
| Filing portal | https://www.taxes.gov.az |
| Authority | State Tax Service under the Ministry of Economy |
| Currency | AZN (Azerbaijani Manat) only |
| Filing frequency | Monthly |
| Deadline | 20th of the month following the reporting month |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key EDV return boxes:**

| Box | Meaning |
|---|---|
| 1 | Taxable supplies at 18% — base |
| 2 | Output EDV at 18% |
| 3 | Zero-rated supplies (exports) |
| 4 | Exempt supplies |
| 5 | Reverse charge on imported services — base |
| 6 | Output EDV on reverse charge |
| 7 | Total output EDV |
| 8 | Input EDV on domestic purchases |
| 9 | Import EDV (paid at customs) |
| 10 | Input EDV on reverse charge (creditable) |
| 11 | Total input EDV |
| 12 | Net EDV payable or credit |
| 13 | Credit brought forward |
| 14 | Net payable after credit |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 18% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Azerbaijan |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (Box 5/6/10) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | AZN 10,000 |
| HIGH tax-delta on a single default | AZN 500 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net EDV position | AZN 20,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: Kapital Bank, PASHA Bank, International Bank of Azerbaijan (IBA), AccessBank, Bank Respublika, Xalq Bank, or any other.

**Recommended** — invoices, e-invoice register from taxes.gov.az, client VOEN (TIN).

**Ideal** — complete e-invoice register, prior period declaration.

### Refusal catalogue

**R-AZ-1 — Simplified tax regime.** *Trigger:* client on simplified tax (turnover below AZN 200,000). *Message:* "Simplified tax payers do not file EDV returns. Out of scope."

**R-AZ-2 — Micro-enterprise.** *Trigger:* registered micro-enterprise. *Message:* "Micro-enterprises are exempt from EDV. Out of scope."

**R-AZ-3 — Partial exemption.** *Trigger:* mixed taxable and exempt supplies. *Message:* "Input EDV apportionment required. Use a qualified practitioner."

**R-AZ-4 — Free economic zone.** *Trigger:* Alat FEZ or other designated zone. *Message:* "FEZ entities have special EDV rules. Out of scope."

**R-AZ-5 — Income tax.** *Trigger:* user asks about income tax. *Message:* "This skill handles EDV returns only."

---

## Section 3 — Supplier pattern library

### 3.1 Azerbaijani banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| KAPITAL BANK, KAPITALBANK | EXCLUDE | Financial service, exempt |
| PASHA BANK, PASHABANK | EXCLUDE | Same |
| IBA, BEYNELXALQ BANK | EXCLUDE | Same |
| ACCESSBANK, BANK RESPUBLIKA, XALQ BANK | EXCLUDE | Same |
| FAIZ, INTEREST | EXCLUDE | Interest, out of scope |
| KREDIT, LOAN | EXCLUDE | Loan principal, out of scope |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| VERGI XIDMETI, STATE TAX | EXCLUDE | Tax payment |
| GOMRUK, CUSTOMS | EXCLUDE | Duty (import EDV separate) |
| DSMF, SOSIAL MUDAFIE | EXCLUDE | Social protection |
| ASAN XIDMET | EXCLUDE | Government service fee |

### 3.3 Utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| AZERIQAZ, AZERENERJI | Domestic 18% | 8 | Gas/electricity |
| AZERSU | Domestic 18% | 8 | Water |
| AZERCELL, BAKCELL, NAR MOBILE | Domestic 18% | 8 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| PASHA SIGORTA, AXA MBASK, ATESHGAH | EXCLUDE | Exempt |
| SIGORTA, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| BRAVO, BAZARSTORE, ARAZ SUPERMARKET | Default BLOCK | Personal provisioning |
| RESTAURANT, RESTORAN, KAFE | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

| Pattern | Box | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | 5/6/10 | Reverse charge at 18% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | 5/6/10 | Same |

### 3.7 Professional services

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NOTAR, NOTARY | Domestic 18% | 8 | If business purpose |
| AUDITOR, MUHASIB | Domestic 18% | 8 | Deductible |
| VEKIL, LAWYER | Domestic 18% | 8 | If business matter |

### 3.8 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| EMEK HAQQI, SALARY | EXCLUDE | Wages |
| DIVIDEND | EXCLUDE | Out of scope |
| DAXILI, INTERNAL, OWN TRANSFER | EXCLUDE | Internal |
| ATM, NAGD, CASH | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00 ; AZN 27.20`

**Reasoning:** US entity. Reverse charge at 18%. Box 5/6 (output), Box 10 (input credit). Net zero.

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -27.20 | -27.20 | 4.90 | 18% | 10 | 5/6 | N |

### Example 2 — Domestic utility

**Input line:** `10.04.2026 ; AZERCELL ; DEBIT ; Mobile April ; -35.00 ; AZN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 10.04.2026 | AZERCELL | -35.00 | -29.66 | -5.34 | 18% | 8 | N |

### Example 3 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTORAN SHIRVANSHAH ; DEBIT ; Dinner ; -180.00 ; AZN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORAN SHIRVANSHAH | -180.00 | -180.00 | 0 | — | — | Y | "Entertainment: blocked" |

### Example 4 — Export (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP LLC ; CREDIT ; IT services ; +8,500.00 ; AZN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TECHCORP LLC | +8,500 | +8,500 | 0 | 0% | 3 | Y | "Verify export docs" |

### Example 5 — Motor vehicle blocked

**Input line:** `28.04.2026 ; BAKU AUTO ; DEBIT ; Car lease ; -850.00 ; AZN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | BAKU AUTO | -850.00 | -850.00 | 0 | — | — | Y | "Vehicle: blocked" |

### Example 6 — Import of goods

**Input line:** `25.04.2026 ; CUSTOMS ; DEBIT ; Import EDV machinery ; -3,600 ; AZN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 25.04.2026 | CUSTOMS | -3,600 | -3,051 | -549 | 18% | 9 | N |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 18% (Tax Code Article 175)
Single rate. Sales to Box 1/2. Purchases to Box 8.

### 5.2 Zero rate
Exports, international transport, diplomatic supplies, certain agricultural produce. Box 3.

### 5.3 Exempt supplies
Financial services, insurance, medical, educational, residential rental, public transport, postal.

### 5.4 Reverse charge — non-resident services (Article 169)
Self-assess at 18%. Box 5/6 (output), Box 10 (input credit). Net zero for fully taxable.

### 5.5 Import EDV
At customs. Base = customs value + duties. 18%. Box 9. Recoverable.

### 5.6 Blocked input EDV
Passenger vehicles, entertainment, personal consumption, no valid invoice, for exempt supplies.

### 5.7 Credit notes
Both parties adjust in current period.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%. *Question:* "Car or commercial?"
### 6.2 Entertainment — *Default:* block.
### 6.3 SaaS entities — *Default:* reverse charge. *Question:* "Check invoice."
### 6.4 Owner transfers — *Default:* exclude. *Question:* "Sale or own money?"
### 6.5 Foreign incoming — *Default:* zero-rated. *Question:* "Export docs?"
### 6.6 Large purchases — *Question:* "Fixed asset?"
### 6.7 Mixed-use phone — *Default:* 0%. *Question:* "Business line?"
### 6.8 Cash withdrawals — *Default:* exclude.
### 6.9 Rent — *Default:* no EDV. *Question:* "Commercial with EDV?"

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Azerbaijan-specific box codes.

---

## Section 8 — Azerbaijani bank statement reading guide

**CSV conventions.** Kapital Bank and PASHA Bank exports use semicolon delimiters, DD.MM.YYYY dates.

**Azerbaijani terms.** Emek haqqi (salary), faiz (interest), kredit (loan), nagd (cash), daxili (internal), gomruk (customs), sigorta (insurance).

**Internal transfers.** Between client's Kapital, PASHA, IBA accounts. Always exclude.

**Foreign currency.** Convert to AZN at the Central Bank of Azerbaijan rate.

**IBAN prefix.** AZ = Azerbaijan.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Fallback:* "Sole trader or company?"
### 9.2 EDV registration — *Fallback:* "VAT payer or simplified regime?"
### 9.3 VOEN — *Fallback:* "What is your VOEN?"
### 9.4 Period — *Inference:* statement dates.
### 9.5 Industry — *Fallback:* "What does the business do?"
### 9.6 Exempt supplies — *If yes, R-AZ-3 fires.*
### 9.7 Credit B/F — *Always ask.*
### 9.8 Cross-border — *Fallback:* "Customers outside Azerbaijan?"

---

## Section 10 — Reference material

### Sources
1. Tax Code of Azerbaijan — Articles 159-184
2. State Tax Service — https://www.taxes.gov.az
3. Central Bank of Azerbaijan — https://www.cbar.az

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Azerbaijan VAT (EDV) Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
