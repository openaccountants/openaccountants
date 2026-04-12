---
name: kosovo-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Kosovo VAT (TVSH) return for any client. Trigger on phrases like "Kosovo VAT", "Kosovo TVSH", "TAK filing", or any request involving Kosovo VAT. This skill covers standard TVSH payers filing monthly returns. Kosovo has 18% standard and 8% reduced rate. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Kosovo VAT work.
version: 2.0
---

# Kosovo VAT (TVSH) Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Kosovo (Republic of Kosovo) |
| Tax name | TVSH (Tatimi mbi Vleren e Shtuar) |
| Standard rate | 18% |
| Reduced rates | 8% (electricity, water, waste, heating, food, pharmaceutical, medical, IT equipment, agriculture, books) |
| Zero rate | 0% (exports, international transport, diplomatic) |
| Return form | Monthly TVSH declaration |
| Filing portal | https://etax.atk-ks.org (TAK e-portal) |
| Authority | Tax Administration of Kosovo (TAK — Administrata Tatimore e Kosoves) |
| Currency | EUR (Kosovo uses the euro) |
| Filing frequency | Monthly |
| Deadline | Last day of the month following the reporting month |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key TVSH return boxes:**

| Box | Meaning |
|---|---|
| 1 | Taxable supplies at 18% — base |
| 2 | Output TVSH at 18% |
| 3 | Taxable supplies at 8% — base |
| 4 | Output TVSH at 8% |
| 5 | Zero-rated supplies (exports) |
| 6 | Exempt supplies |
| 7 | Reverse charge on imported services — base |
| 8 | Output TVSH on reverse charge |
| 9 | Total output TVSH |
| 10 | Input TVSH on domestic purchases (18%) |
| 11 | Input TVSH on domestic purchases (8%) |
| 12 | Import TVSH |
| 13 | Input TVSH on reverse charge (creditable) |
| 14 | Total input TVSH |
| 15 | Net TVSH payable or credit |
| 16 | Credit brought forward |
| 17 | Net payable |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 18% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Kosovo |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (Box 7/8/13) |
| Unknown blocked-input status | Blocked |
| Unknown 8% vs 18% rate | 18% |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 3,000 |
| HIGH tax-delta on a single default | EUR 200 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net TVSH position | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: ProCredit Bank Kosovo, Raiffeisen Bank Kosovo, NLB Banka Kosovo, TEB, Banka Ekonomike, BKT Kosovo, or any other.

**Recommended** — invoices, fiscal receipts, client fiscal number.

**Ideal** — complete invoice register, prior TVSH declaration.

### Refusal catalogue

**R-XK-1 — Non-registered.** *Trigger:* client below EUR 30,000 threshold and not voluntarily registered. *Message:* "Non-registered entities cannot file TVSH. Out of scope."

**R-XK-2 — Partial exemption.** *Trigger:* mixed taxable and exempt. *Message:* "Input TVSH apportionment required."

**R-XK-3 — Income tax.** *Trigger:* user asks about income tax. *Message:* "This skill handles TVSH only."

---

## Section 3 — Supplier pattern library

### 3.1 Kosovo banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| PROCREDIT KOSOVO, PROCREDIT | EXCLUDE | Financial service, exempt |
| RAIFFEISEN KOSOVO, RAIFFEISEN | EXCLUDE | Same |
| NLB BANKA, TEB, BANKA EKONOMIKE | EXCLUDE | Same |
| BKT KOSOVO | EXCLUDE | Same |
| INTERES, INTEREST | EXCLUDE | Interest |
| KREDI, LOAN | EXCLUDE | Loan principal |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TAK, ATK, TAX ADMINISTRATION | EXCLUDE | Tax payment |
| DOGANA, CUSTOMS KOSOVO | EXCLUDE | Duty (import TVSH separate) |
| TRUST PENSIONAL, PENSION | EXCLUDE | Pension |
| MINISTRIA, GOVERNMENT | EXCLUDE | Government fee |

### 3.3 Utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| KESCO, KEK, KEDS | Domestic (8% electricity) | 11 | Electricity — reduced rate |
| RWC, UJËSJELLËSI | Domestic (8% water) | 11 | Water — reduced rate |
| IPKO, VALA, KUJTESA | Domestic 18% | 10 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SIGURIA, SIGAL KOSOVO, ILLYRIA | EXCLUDE | Exempt |
| SIGURIM, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| VIVA FRESH, ETC, INTEREX | Default BLOCK | Personal provisioning |
| RESTORANT, KAFENE, BAR | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

| Pattern | Box | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | 7/8/13 | Reverse charge at 18% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | 7/8/13 | Same |

### 3.7 Professional services

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NOTER, NOTAR | Domestic 18% | 10 | If business purpose |
| KONTABILIST, AUDITOR | Domestic 18% | 10 | Deductible |
| AVOKAT, LAWYER | Domestic 18% | 10 | If business matter |

### 3.8 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| PAGA, SALARY | EXCLUDE | Wages |
| DIVIDEND | EXCLUDE | Out of scope |
| TRANSFERE, INTERNAL | EXCLUDE | Internal |
| ATM, TERHEQJE | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; EUR 16.00`

**Reasoning:** US entity. Reverse charge at 18%. Box 7 (base), Box 8 (output), Box 13 (input credit). Net zero.

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -16.00 | -16.00 | 2.88 | 18% | 13 | 7/8 | N |

### Example 2 — Reduced rate utility (electricity at 8%)

**Input line:** `10.04.2026 ; KESCO ; DEBIT ; Electricity April ; -85.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 10.04.2026 | KESCO | -85.00 | -78.70 | -6.30 | 8% | 11 | N |

### Example 3 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTORANT LIBURNIA ; DEBIT ; Dinner ; -120.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORANT LIBURNIA | -120.00 | -120.00 | 0 | — | — | Y | "Entertainment: blocked" |

### Example 4 — Export (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT services ; +3,500.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TECHCORP GMBH | +3,500 | +3,500 | 0 | 0% | 5 | Y | "Verify export docs" |

### Example 5 — Motor vehicle blocked

**Input line:** `28.04.2026 ; AUTO PRISHTINA ; DEBIT ; Car lease ; -350.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | AUTO PRISHTINA | -350.00 | -350.00 | 0 | — | — | Y | "Vehicle: blocked" |

### Example 6 — Import of goods

**Input line:** `25.04.2026 ; DOGANA KOSOVES ; DEBIT ; Import TVSH ; -1,800 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 25.04.2026 | DOGANA KOSOVES | -1,800 | -1,525 | -275 | 18% | 12 | N |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 18%
Default rate. Sales to Box 1/2. Purchases to Box 10.

### 5.2 Reduced rate 8%
Electricity, water, waste, heating, food staples, pharmaceutical, medical equipment, IT equipment, agricultural inputs, books. Sales to Box 3/4. Purchases to Box 11.

### 5.3 Zero rate
Exports, international transport, diplomatic. Box 5.

### 5.4 Exempt
Financial, insurance, medical services, educational, residential rental, postal.

### 5.5 Reverse charge — non-resident services
Self-assess at 18%. Box 7/8 (output), Box 13 (input). Net zero.

### 5.6 Import TVSH
At customs. 18% (or 8% if applicable). Box 12.

### 5.7 Blocked input TVSH
Passenger vehicles, entertainment, personal consumption, no valid invoice.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%.
### 6.2 Entertainment — *Default:* block.
### 6.3 SaaS entities — *Default:* reverse charge at 18%.
### 6.4 8% vs 18% — *Default:* 18%. *Question:* "Confirm if reduced rate applies."
### 6.5 Owner transfers — *Default:* exclude.
### 6.6 Foreign incoming — *Default:* zero-rated. *Question:* "Export docs?"
### 6.7 Large purchases — *Question:* "Fixed asset?"
### 6.8 Cash withdrawals — *Default:* exclude.

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Kosovo-specific box codes. Note Kosovo uses EUR.

---

## Section 8 — Kosovo bank statement reading guide

**CSV conventions.** ProCredit Kosovo and Raiffeisen Kosovo use comma or semicolon delimiters, DD.MM.YYYY.

**Albanian terms.** Paga (salary), interes (interest), kredi (loan), terheqje (withdrawal), transfere (transfer). Same as Albania.

**Currency.** Kosovo uses EUR. No currency conversion needed for EUR transactions.

**Internal transfers.** Between client's accounts. Exclude.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Fallback:* "Sole trader or company (SHPK)?"
### 9.2 TVSH registration — *Fallback:* "TVSH registered?"
### 9.3 Fiscal number — *Fallback:* "What is your fiscal number?"
### 9.4 Period — *Inference:* statement dates.
### 9.5 Industry — *Fallback:* "What does the business do?"
### 9.6 Credit B/F — *Always ask.*
### 9.7 Cross-border — *Fallback:* "Customers outside Kosovo?"

---

## Section 10 — Reference material

### Sources
1. Law No. 05/L-037 on Value Added Tax (Kosovo)
2. TAK — https://etax.atk-ks.org
3. Central Bank of Kosovo — https://bqk-kos.org (no FX needed — EUR)

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Kosovo VAT (TVSH) Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
