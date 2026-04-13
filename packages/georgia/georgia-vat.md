---
name: georgia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Georgia VAT return for any client. Trigger on phrases like "Georgia VAT", "RS filing", "Revenue Service Georgia", or any request involving Georgian VAT. This skill covers standard VAT payers filing monthly returns. Small Business Status, Micro Business, Fixed Tax, and Virtual Zone IT regimes are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Georgian VAT work.
version: 2.0
---

# Georgia VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Georgia |
| Tax name | VAT (ghirebuleba damatebiti gadasakhadi) |
| Standard rate | 18% |
| Reduced rates | None (single standard rate) |
| Zero rate | 0% (exports, international transport, FIZ supplies, diplomatic) |
| Return form | Monthly VAT declaration (electronic via rs.ge) |
| Filing portal | https://rs.ge |
| Authority | Revenue Service (RS), Ministry of Finance |
| Currency | GEL (Georgian Lari) only |
| Filing frequency | Monthly |
| Deadline | 15th of the month following the reporting month |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key VAT return sections:**

| Section | Meaning |
|---|---|
| Part 1 | Taxpayer information (TIN, name, period) |
| Part 2 | Taxable supplies at 18% — base |
| Part 3 | Zero-rated supplies (exports) |
| Part 4 | Exempt supplies |
| Part 5 | Total supplies |
| Part 6 | Output VAT (18% of taxable) |
| Part 7 | Reverse charge VAT (imported services) |
| Part 8 | Total output VAT |
| Part 9 | Input VAT on domestic purchases |
| Part 10 | Input VAT on imports (customs) |
| Part 11 | Input VAT on reverse charge (creditable) |
| Part 12 | Total input VAT credit |
| Part 13 | Net VAT payable |
| Part 14 | Credit brought forward |
| Part 15 | Net payable or credit |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 18% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Georgia |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (Part 7/11) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | GEL 15,000 |
| HIGH tax-delta on a single default | GEL 1,000 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net VAT position | GEL 25,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: TBC Bank, Bank of Georgia, Liberty Bank, Basis Bank, Credo Bank, ProCredit Bank Georgia, or any other.

**Recommended** — invoices (especially e-invoices from rs.ge), client TIN (9 or 11 digits).

**Ideal** — complete e-invoice register from rs.ge, prior period declaration.

### Refusal catalogue

**R-GE-1 — Small Business Status.** *Trigger:* client on SBS (1% turnover tax, below GEL 500,000). *Message:* "Small Business Status entities do not file VAT returns. Out of scope."

**R-GE-2 — Micro Business.** *Trigger:* client is micro business (below GEL 30,000, exempt). *Message:* "Micro businesses are exempt from VAT. Out of scope."

**R-GE-3 — Fixed Tax.** *Trigger:* client on fixed tax regime. *Message:* "Fixed tax entities have separate obligations. Out of scope."

**R-GE-4 — Virtual Zone IT company.** *Trigger:* registered Virtual Zone IT entity. *Message:* "Virtual Zone IT companies have special tax treatment. Please use a qualified Georgian practitioner for confirmation of scope."

**R-GE-5 — Free Industrial Zone (FIZ).** *Trigger:* FIZ entity. *Message:* "FIZ entities have special VAT rules. Out of scope."

**R-GE-6 — Partial exemption.** *Trigger:* mixed taxable and exempt. *Message:* "Input VAT apportionment required. Use a qualified practitioner."

**R-GE-7 — Income tax.** *Trigger:* user asks about income/profit tax. *Message:* "This skill handles VAT only."

---

## Section 3 — Supplier pattern library

### 3.1 Georgian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TBC BANK, TBC | EXCLUDE | Financial service, exempt |
| BANK OF GEORGIA, BOG | EXCLUDE | Same |
| LIBERTY BANK, BASIS BANK, CREDO BANK | EXCLUDE | Same |
| PROCREDIT GEORGIA, TERABANK | EXCLUDE | Same |
| PROTSENTI, INTEREST | EXCLUDE | Interest, out of scope |
| SESXI, LOAN | EXCLUDE | Loan principal |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| REVENUE SERVICE, RS.GE | EXCLUDE | Tax payment |
| SABAZHOEBI, CUSTOMS | EXCLUDE | Duty (import VAT separate) |
| SAPENSIA, PENSION AGENCY | EXCLUDE | Pension contribution |
| IUSTITSII, JUSTICE HOUSE | EXCLUDE | Government fee |

### 3.3 Utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| TELASI, GWP, ENERGO-PRO | Domestic 18% | Part 9 | Electricity/water |
| SOCAR GEORGIA, GAZPROM GE | Domestic 18% | Part 9 | Gas |
| MAGTICOM, BEELINE GE, GEOCELL | Domestic 18% | Part 9 | Telecoms |
| SILKNET | Domestic 18% | Part 9 | Internet/TV |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ALDAGI, IC GROUP, TBC INSURANCE | EXCLUDE | Exempt |
| DAZGHVEVA, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| CARREFOUR GE, GOODWILL, NIKORA, FRESCO | Default BLOCK | Personal provisioning |
| RESTORAN, RESTORANI, KAFE, BAR | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

| Pattern | Box | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Part 7/11 | Reverse charge at 18% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | Part 7/11 | Same |

### 3.7 Professional services

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NOTARIUSI, NOTARY | Domestic 18% | Part 9 | If business purpose |
| AUDITORI, BUKHGALTER | Domestic 18% | Part 9 | Deductible |
| ADVOKATI, LAWYER | Domestic 18% | Part 9 | If business matter |

### 3.8 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| KHELFASI, SALARY | EXCLUDE | Wages |
| DIVIDENDI | EXCLUDE | Out of scope |
| SHIDA, INTERNAL, OWN TRANSFER | EXCLUDE | Internal |
| ATM, NAGHDI | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00 ; GEL 43.20`

**Reasoning:** US entity. Reverse charge at 18%. Part 7 (output VAT), Part 11 (input credit). Net zero.

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -43.20 | -43.20 | 7.78 | 18% | Part 11 | Part 7 | N |

### Example 2 — Domestic purchase

**Input line:** `10.04.2026 ; MAGTICOM ; DEBIT ; Internet April ; -45.00 ; GEL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 10.04.2026 | MAGTICOM | -45.00 | -38.14 | -6.86 | 18% | Part 9 | N |

### Example 3 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTORAN SHEMOIKHEDE ; DEBIT ; Business dinner ; -250.00 ; GEL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORAN SHEMOIKHEDE | -250.00 | -250.00 | 0 | — | — | Y | "Entertainment: blocked" |

### Example 4 — Export of IT services (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT services ; +8,100.00 ; GEL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TECHCORP GMBH | +8,100 | +8,100 | 0 | 0% | Part 3 | Y | "Verify export docs" |

### Example 5 — Motor vehicle blocked

**Input line:** `28.04.2026 ; TEGETA MOTORS ; DEBIT ; Car lease ; -1,200.00 ; GEL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | TEGETA MOTORS | -1,200.00 | -1,200.00 | 0 | — | — | Y | "Vehicle: blocked" |

### Example 6 — Import of goods

**Input line:** `25.04.2026 ; CUSTOMS ; DEBIT ; Import VAT ; -5,400.00 ; GEL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 25.04.2026 | CUSTOMS | -5,400 | -4,576 | -824 | 18% | Part 10 | N |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 18% (Tax Code Article 164)
Single rate. Sales to Part 2/6. Purchases to Part 9.

### 5.2 Zero rate
Exports, international transport, FIZ supplies, diplomatic. Part 3.

### 5.3 Exempt supplies (Article 168)
Financial, insurance, medical, educational, residential rental, public transport, postal, cultural, agricultural land, government.

### 5.4 Reverse charge — non-resident services (Article 161)
Self-assess at 18%. Part 7 (output), Part 11 (input credit). Net zero.

### 5.5 Import VAT
At customs. Base = customs value + duties + excise. 18%. Part 10.

### 5.6 Blocked input VAT (Article 177)
Motor vehicles for personal use, entertainment/representation, personal consumption, no valid invoice, from non-VAT-registered supplier, for exempt supplies, fuel for non-commercial vehicles, gifts/donations.

### 5.7 Electronic invoicing
All VAT-registered taxpayers issue invoices via rs.ge. Input credit validated against system.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%. *Question:* "Car or commercial?"
### 6.2 Entertainment — *Default:* block.
### 6.3 SaaS entities — *Default:* reverse charge. *Question:* "Check invoice."
### 6.4 Virtual Zone IT — *Default:* R-GE-4 fires if suspected.
### 6.5 Owner transfers — *Default:* exclude.
### 6.6 Foreign incoming — *Default:* zero-rated. *Question:* "Export docs?"
### 6.7 Large purchases — *Question:* "Capital asset?"
### 6.8 Mixed-use phone — *Default:* 0%.
### 6.9 Cash withdrawals — *Default:* exclude.
### 6.10 Wine industry — *Default:* 18% domestic, 0% export. *Question:* "Confirm excise obligations."

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Georgia-specific box codes.

---

## Section 8 — Georgian bank statement reading guide

**CSV conventions.** TBC Bank and Bank of Georgia export in CSV with semicolons or commas. DD.MM.YYYY or ISO dates depending on setting.

**Georgian terms.** Khelfasi (salary), protsenti (interest), sesxi (loan), naghdi (cash), shida (internal), sabazhoebi (customs), dazghveva (insurance).

**Internal transfers.** Between client's TBC, BOG, Liberty accounts. Exclude.

**Foreign currency.** Convert to GEL at National Bank of Georgia rate.

**Wine exports.** Georgia is a major wine exporter. Wine export receipts are zero-rated. Excise is separate.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Fallback:* "Sole trader or company (LLC/JSC)?"
### 9.2 VAT registration — *Fallback:* "Standard VAT, Small Business, Micro, or Fixed Tax?"
### 9.3 TIN — *Fallback:* "What is your TIN?"
### 9.4 Period — *Inference:* statement dates.
### 9.5 Industry — *Inference:* wine, IT, tourism from counterparties. *Fallback:* "What does the business do?"
### 9.6 Virtual Zone — *Fallback:* "Are you a Virtual Zone IT company?"
### 9.7 Credit B/F — *Always ask.*
### 9.8 Cross-border — *Fallback:* "Customers outside Georgia?"

---

## Section 10 — Reference material

### Sources
1. Tax Code of Georgia — Articles 156-184
2. Revenue Service — https://rs.ge
3. National Bank of Georgia rates — https://www.nbg.gov.ge

### Known gaps
1. Virtual Zone IT regime not covered in detail. 2. FIZ rules not covered. 3. Wine excise not covered.

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Georgia VAT Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
