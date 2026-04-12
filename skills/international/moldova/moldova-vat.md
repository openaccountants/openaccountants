---
name: moldova-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Moldova VAT (TVA) return for any client. Trigger on phrases like "Moldova VAT", "TVA Moldova", "SFS filing", or any request involving Moldovan VAT. This skill covers standard TVA payers filing monthly returns. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Moldovan VAT work.
version: 2.0
---

# Moldova VAT (TVA) Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Moldova (Republic of Moldova) |
| Tax name | TVA (Taxa pe Valoarea Adaugata) |
| Standard rate | 20% |
| Reduced rates | 8% (bread, dairy, agricultural produce, medicines, natural gas, LPG) |
| Zero rate | 0% (exports, international transport) |
| Return form | Monthly TVA declaration |
| Filing portal | https://servicii.fisc.md (SFS portal) |
| Authority | State Fiscal Service (SFS — Serviciul Fiscal de Stat) |
| Currency | MDL (Moldovan Leu) only |
| Filing frequency | Monthly |
| Deadline | Last day of the month following the reporting month |
| DCFTA with EU | Deep and Comprehensive Free Trade Area — impacts customs treatment |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key TVA return boxes:**

| Box | Meaning |
|---|---|
| 1 | Taxable supplies at 20% — base |
| 2 | Output TVA at 20% |
| 3 | Taxable supplies at 8% — base |
| 4 | Output TVA at 8% |
| 5 | Zero-rated supplies |
| 6 | Exempt supplies |
| 7 | Reverse charge on imported services — base |
| 8 | Output TVA on reverse charge |
| 9 | Total output TVA |
| 10 | Input TVA domestic purchases (20%) |
| 11 | Input TVA domestic purchases (8%) |
| 12 | Import TVA (customs) |
| 13 | Input TVA reverse charge (creditable) |
| 14 | Total input TVA |
| 15 | Net payable or credit |
| 16 | Credit B/F |
| 17 | Net payable |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate | 20% |
| Unknown purchase status | Not deductible |
| Unknown counterparty country | Domestic Moldova |
| Unknown SaaS billing entity | Reverse charge (Box 7/8/13) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | MDL 100,000 |
| HIGH tax-delta | MDL 5,000 |
| MEDIUM counterparty concentration | >40% |
| LOW absolute net TVA | MDL 150,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement. Acceptable from: Moldova Agroindbank (MAIB), Victoriabank, Moldindconbank, Mobiasbanca, Eximbank, or any other.

**Recommended** — invoices (factura fiscala), client IDNO.

**Ideal** — complete e-invoice register, prior TVA declaration.

### Refusal catalogue

**R-MD-1 — Non-registered.** Below MDL 1,200,000 and not voluntarily registered. *Message:* "Not TVA registered. Out of scope."

**R-MD-2 — Partial exemption.** Mixed supplies. *Message:* "Apportionment required."

**R-MD-3 — Transnistria.** *Trigger:* entity in Transnistria. *Message:* "Transnistrian entities have separate fiscal administration. Out of scope."

**R-MD-4 — Income tax.** *Message:* "This skill handles TVA only."

---

## Section 3 — Supplier pattern library

### 3.1 Moldovan banks (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MAIB, MOLDOVA AGROINDBANK | EXCLUDE | Financial service, exempt |
| VICTORIABANK, VICTORIA | EXCLUDE | Same |
| MOLDINDCONBANK, MICB | EXCLUDE | Same |
| MOBIASBANCA, EXIMBANK | EXCLUDE | Same |
| DOBANDA, INTEREST | EXCLUDE | Interest |
| CREDIT, IMPRUMUT | EXCLUDE | Loan |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SFS, SERVICIUL FISCAL | EXCLUDE | Tax payment |
| VAMA, CUSTOMS | EXCLUDE | Duty (import TVA separate) |
| CNAS, SOCIAL INSURANCE | EXCLUDE | Social contributions |
| ASP, GOVERNMENT | EXCLUDE | Government fee |

### 3.3 Utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| MOLDOVAGAZ, MOLDELECTRICA | Domestic (8% gas / 20% electricity) | 11 or 10 | Gas at reduced rate; electricity at standard |
| APA-CANAL, REGIA APA | Domestic 20% | 10 | Water |
| MOLDTELECOM, ORANGE MD, MOLDCELL | Domestic 20% | 10 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MOLDASIG, GRAWE, DONARIS | EXCLUDE | Exempt |
| ASIGURARE, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| LINELLA, NR 1, METRO MD | Default BLOCK | Personal provisioning |
| RESTAURANT, CAFENEA, BAR | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

| Pattern | Box | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | 7/8/13 | Reverse charge at 20% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | 7/8/13 | Same |

### 3.7 Professional services

| Pattern | Treatment | Box |
|---|---|---|
| NOTAR, NOTARY | Domestic 20% | 10 |
| AUDITOR, CONTABIL | Domestic 20% | 10 |
| AVOCAT, LAWYER | Domestic 20% | 10 |

### 3.8 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARIU, SALARY | EXCLUDE | Wages |
| DIVIDEND | EXCLUDE | Out of scope |
| INTERN, TRANSFER INTERN | EXCLUDE | Internal |
| ATM, NUMERAR | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00 ; MDL 288`

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -288 | -288 | 58 | 20% | 13 | 7/8 | N |

### Example 2 — Domestic utility at standard rate

**Input line:** `10.04.2026 ; MOLDTELECOM ; DEBIT ; Internet April ; -450 ; MDL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 10.04.2026 | MOLDTELECOM | -450 | -375 | -75 | 20% | 10 | N |

### Example 3 — Reduced rate purchase (gas at 8%)

**Input line:** `12.04.2026 ; MOLDOVAGAZ ; DEBIT ; Natural gas ; -1,620 ; MDL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 12.04.2026 | MOLDOVAGAZ | -1,620 | -1,500 | -120 | 8% | 11 | N |

### Example 4 — Export (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT services ; +18,000 ; MDL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TECHCORP GMBH | +18,000 | +18,000 | 0 | 0% | 5 | Y | "Verify export docs" |

### Example 5 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTAURANT LA PLACINTE ; DEBIT ; Dinner ; -800 ; MDL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANT LA PLACINTE | -800 | -800 | 0 | — | — | Y | "Entertainment: blocked" |

### Example 6 — Import of goods

**Input line:** `25.04.2026 ; VAMA ; DEBIT ; Import TVA ; -12,000 ; MDL`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 25.04.2026 | VAMA | -12,000 | -10,000 | -2,000 | 20% | 12 | N |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 20% (Fiscal Code Article 96)
Default rate. Sales to Box 1/2. Purchases to Box 10.

### 5.2 Reduced rate 8%
Bread, dairy, agricultural produce, medicines, natural gas, LPG. Sales to Box 3/4. Purchases to Box 11.

### 5.3 Zero rate
Exports, international transport. Box 5.

### 5.4 Exempt
Financial, insurance, medical, educational, residential rental, postal.

### 5.5 Reverse charge (Article 109)
Non-resident services. Self-assess at 20%. Box 7/8 (output), Box 13 (input).

### 5.6 Import TVA
At customs. Box 12.

### 5.7 Blocked input
Passenger vehicles, entertainment, personal consumption, no valid invoice.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%.
### 6.2 Entertainment — *Default:* block.
### 6.3 SaaS entities — *Default:* reverse charge at 20%.
### 6.4 8% vs 20% — *Default:* 20%.
### 6.5 Owner transfers — *Default:* exclude.
### 6.6 Foreign incoming — *Default:* zero-rated.
### 6.7 Cash withdrawals — *Default:* exclude.
### 6.8 Rent — *Default:* no TVA.

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Moldova-specific box codes.

---

## Section 8 — Moldovan bank statement reading guide

**CSV conventions.** MAIB and Victoriabank use semicolons, DD.MM.YYYY.

**Romanian terms.** Salariu (salary), dobanda (interest), credit/imprumut (loan), numerar (cash), intern (internal), vama (customs), asigurare (insurance), contabil (accountant).

**Foreign currency.** Convert to MDL at National Bank of Moldova rate.

**IBAN prefix.** MD = Moldova.

**Transnistria note.** Transactions with Transnistrian counterparties require special handling — R-MD-3 fires.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Fallback:* "SRL, SA, or sole trader (II)?"
### 9.2 TVA registration — *Fallback:* "TVA payer?"
### 9.3 IDNO — *Fallback:* "What is your IDNO?"
### 9.4 Period — *Inference:* statement dates.
### 9.5 Industry — *Fallback:* "What does the business do?"
### 9.6 Credit B/F — *Always ask.*
### 9.7 Transnistria — *Fallback:* "Any transactions with Transnistria?"

---

## Section 10 — Reference material

### Sources
1. Fiscal Code of Moldova — Title III (TVA)
2. SFS — https://servicii.fisc.md
3. National Bank of Moldova — https://www.bnm.md

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Moldova VAT (TVA) Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
