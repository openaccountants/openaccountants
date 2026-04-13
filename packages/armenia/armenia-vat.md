---
name: armenia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Armenian VAT (AVH) return for any client. Trigger on phrases like "Armenia VAT", "Armenian VAT", "AVH return", "SRC filing", or any request involving Armenian VAT filing. This skill covers standard VAT payers filing monthly returns. Turnover tax, micro-enterprise, and IT sector special regimes are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Armenian VAT work.
version: 2.0
---

# Armenia VAT Return Skill v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.**

| Field | Value |
|---|---|
| Country | Armenia (Republic of Armenia) |
| Tax name | AVH (Avelacvats Arzheki Hark) / VAT |
| Standard rate | 20% |
| Reduced rates | None (single standard rate) |
| Zero rate | 0% (exports, international transport, diplomatic supplies) |
| Return form | Monthly VAT declaration (electronic) |
| Filing portal | https://www.petakner.am |
| Authority | State Revenue Committee (SRC) |
| Currency | AMD (Armenian Dram) only |
| Filing frequency | Monthly |
| Deadline | 20th of the month following the reporting month |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key VAT return sections:**

| Section | Meaning |
|---|---|
| Part 1 | Taxable supplies at 20% — base |
| Part 2 | Output VAT at 20% |
| Part 3 | Zero-rated supplies (exports) |
| Part 4 | Exempt supplies |
| Part 5 | Reverse charge — services from non-residents — base |
| Part 6 | Output VAT on reverse charge |
| Part 7 | Total output VAT |
| Part 8 | Input VAT on domestic purchases |
| Part 9 | Input VAT on imports (paid at customs) |
| Part 10 | Input VAT on reverse charge (creditable) |
| Part 11 | Total input VAT |
| Part 12 | Net VAT payable or credit |
| Part 13 | Credit brought forward |
| Part 14 | Net payable after credit |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Armenia |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-resident (Part 5/6/10) |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | AMD 5,000,000 |
| HIGH tax-delta on a single conservative default | AMD 300,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | AMD 10,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. Acceptable from any Armenian bank: Ameriabank, ACBA Bank, Ardshinbank, Converse Bank, Evocabank, HSBC Armenia, or any other.

**Recommended** — sales invoices, purchase invoices for input VAT claims above AMD 300,000, the client's TIN (HVHH).

**Ideal** — complete e-invoice register from petakner.am, prior period declaration, reconciliation of credit brought forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement, hard stop. If bank statement only, proceed but record: "This VAT return was produced from bank statement alone. Reviewer must verify input VAT claims are supported by valid tax invoices."

### Armenia-specific refusal catalogue

**R-AM-1 — Turnover tax regime.** *Trigger:* client on turnover tax (below AMD 115,000,000 and opted for turnover tax). *Message:* "Turnover tax payers do not file VAT returns and cannot claim input VAT. Out of scope."

**R-AM-2 — Micro-enterprise.** *Trigger:* registered micro-enterprise. *Message:* "Micro-enterprises are exempt from VAT. Out of scope."

**R-AM-3 — IT sector special regime.** *Trigger:* certified IT company with special tax incentives. *Message:* "IT sector special regime entities may have modified VAT obligations. Please use a qualified Armenian practitioner."

**R-AM-4 — Partial exemption.** *Trigger:* mixed taxable and exempt supplies, non-de-minimis. *Message:* "Input VAT apportionment required. Use a qualified practitioner."

**R-AM-5 — Free economic zone.** *Trigger:* FEZ entity. *Message:* "FEZ entities have special VAT rules. Out of scope."

**R-AM-6 — Income tax.** *Trigger:* user asks about income tax. *Message:* "This skill handles VAT returns only."

---

## Section 3 — Supplier pattern library

### 3.1 Armenian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| AMERIABANK, AMERIA | EXCLUDE for bank charges/fees | Financial service, exempt |
| ACBA, ACBA BANK, ACBA-CREDIT AGRICOLE | EXCLUDE for bank charges/fees | Same |
| ARDSHINBANK, ARDSHIN | EXCLUDE for bank charges/fees | Same |
| CONVERSE BANK, EVOCABANK, ARARAT BANK | EXCLUDE for bank charges/fees | Same |
| HSBC ARMENIA, INECOBANK, ID BANK | EXCLUDE for bank charges/fees | Same |
| TOKOS, INTEREST | EXCLUDE | Interest, out of scope |
| VARK, LOAN | EXCLUDE | Loan principal, out of scope |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SRC, HARKAYIN KOMITE, STATE REVENUE | EXCLUDE | Tax payment |
| MAQSAYIN, CUSTOMS | EXCLUDE | Customs duty (see import VAT for Part 9) |
| SOTSIALAYIN, SOCIAL PAYMENT | EXCLUDE | Social payment |
| PETAKAN, STATE FEE | EXCLUDE | Government fee |

### 3.3 Utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| ENA, ELECTRIC NETWORKS ARMENIA | Domestic 20% | Part 8 | Electricity |
| VEOLIA JRMUGK, YEREVAN JRMUGK | Domestic 20% | Part 8 | Water |
| GAZPROM ARMENIA, HAYRUSGAZARD | Domestic 20% | Part 8 | Gas |
| VEON ARMENIA, TEAM TELECOM, UCOM | Domestic 20% | Part 8 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ROSGOSSTRAKH, INGO ARMENIA, NAIRI INSURANCE | EXCLUDE | Exempt |
| APAHOV, INSURANCE | EXCLUDE | Same |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
|---|---|---|
| HAYPOST | EXCLUDE for standard mail | Universal service, exempt |
| DHL, FEDEX, TNT | Domestic 20% or reverse charge | Check billing entity |

### 3.6 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| SUPERMARKET, YEREVAN CITY, SAS | Default BLOCK | Personal provisioning |
| RESTAURANT, RESTORAN, CAFE, BAR | Default BLOCK | Entertainment blocked |

### 3.7 SaaS — non-resident suppliers (reverse charge)

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Various non-resident | Part 5/6/10 | Reverse charge at 20% |
| SLACK, ZOOM, DROPBOX, NOTION | Various non-resident | Part 5/6/10 | Reverse charge |
| AWS, ANTHROPIC, OPENAI, GITHUB, FIGMA, CANVA | US entities | Part 5/6/10 | Reverse charge |

### 3.8 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE, PAYPAL (transaction fees) | EXCLUDE (exempt) | Financial service |

### 3.9 Professional services

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NOTAR, NOTARY | Domestic 20% | Part 8 | If business purpose |
| HASHVAPAH, AUDITOR | Domestic 20% | Part 8 | Deductible |
| PASHTPAN, LAWYER | Domestic 20% | Part 8 | If business matter |

### 3.10 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| ASHKHATAVARDZ, SALARY | EXCLUDE | Wages, out of scope |
| DIVIDEND | EXCLUDE | Out of scope |
| INTERNAL, OWN TRANSFER | EXCLUDE | Internal movement |
| ATM, KANKHIK, CASH | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge (Notion)

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00 ; AMD 6,240`

**Reasoning:** US entity, non-resident. Reverse charge at 20%. Part 5 (base), Part 6 (output VAT), Part 10 (input credit). Net zero.

| Date | Counterparty | Gross | Net | VAT | Rate | Box (input) | Box (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -6,240 | -6,240 | 1,248 | 20% | Part 10 | Part 5/6 | N | — | — |

### Example 2 — Domestic purchase with input VAT

**Input line:** `10.04.2026 ; UCOM ; DEBIT ; Business internet April ; -15,000 ; AMD`

**Reasoning:** Domestic Armenian telecoms. Standard 20%. Input VAT deductible.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | UCOM | -15,000 | -12,500 | -2,500 | 20% | Part 8 | N | — | — |

### Example 3 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTORAN DOLMAMA ; DEBIT ; Business dinner ; -45,000 ; AMD`

**Reasoning:** Entertainment blocked. No input VAT recovery.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORAN DOLMAMA | -45,000 | -45,000 | 0 | — | — | Y | Q1 | "Entertainment: blocked" |

### Example 4 — Export of IT services (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT consultancy ; +1,950,000 ; AMD`

**Reasoning:** Export of services. Zero-rated. Part 3. Requires export documentation.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TECHCORP GMBH | +1,950,000 | +1,950,000 | 0 | 0% | Part 3 | Y | Q2 (HIGH) | "Verify export docs" |

### Example 5 — Motor vehicle blocked

**Input line:** `28.04.2026 ; ZANGAK AUTO ; DEBIT ; Car lease ; -120,000 ; AMD`

**Reasoning:** Passenger vehicle input VAT blocked. Default: full block.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | ZANGAK AUTO | -120,000 | -120,000 | 0 | — | — | Y | Q3 | "Motor vehicle: blocked" |

### Example 6 — Import of goods

**Input line:** `25.04.2026 ; CUSTOMS ; DEBIT ; Import VAT machinery ; -480,000 ; AMD`

**Reasoning:** Import VAT at customs. Recoverable. Part 9.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 25.04.2026 | CUSTOMS | -480,000 | -400,000 | -80,000 | 20% | Part 9 | N | — | — |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 20% (Tax Code Article 64)
Single rate, no reduced rates. Sales to Part 1/2. Purchases to Part 8.

### 5.2 Zero rate
Exports (customs declaration required), international transport, diplomatic supplies. Part 3.

### 5.3 Exempt supplies
Financial services, insurance, medical, educational, residential rental, public transport, postal universal service, agricultural land.

### 5.4 Input VAT on domestic purchases
Deductible if: for taxable supplies, valid tax invoice, supplier is VAT registered. Part 8.

### 5.5 Reverse charge — non-resident services (Tax Code Article 40)
Self-assess at 20%. Part 5 (base), Part 6 (output), Part 10 (input credit). Net zero for fully taxable.

### 5.6 Import VAT
At customs. Base = customs value + duties. 20%. Part 9. Recoverable.

### 5.7 Blocked input VAT
- Passenger vehicles (unless taxi/rental/driving school)
- Entertainment and representation
- Personal consumption
- Without valid tax invoice
- For exempt supplies

### 5.8 Credit notes
Both parties adjust in current period.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%. *Question:* "Car or commercial vehicle?"
### 6.2 Entertainment — *Default:* block.
### 6.3 SaaS entities — *Default:* reverse charge. *Question:* "Check invoice for entity."
### 6.4 Owner transfers — *Default:* exclude. *Question:* "Customer payment or own money?"
### 6.5 Incoming from individuals — *Default:* domestic 20%. *Question:* "Was this a sale?"
### 6.6 Foreign incoming — *Default:* zero-rated export. *Question:* "Export documentation?"
### 6.7 Large purchases — *Question:* "Fixed asset (>12 months life)?"
### 6.8 Mixed-use phone — *Default:* 0%. *Question:* "Business line?"
### 6.9 Cash withdrawals — *Default:* exclude. *Question:* "What for?"
### 6.10 Rent — *Default:* no VAT (residential). *Question:* "Commercial with VAT invoice?"

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Armenia-specific box codes from Section 1.

```
| Part 1  | Taxable supplies 20% | =SUMIFS(...) |
| Part 2  | Output VAT 20% | =Part1*0.20 |
| Part 3  | Zero-rated | =SUMIFS(...) |
| Part 5  | Reverse charge base | =SUMIFS(...) |
| Part 6  | Output VAT reverse charge | =Part5*0.20 |
| Part 7  | Total output VAT | =Part2+Part6 |
| Part 8  | Input VAT domestic | =SUMIFS(...) |
| Part 9  | Input VAT imports | =SUMIFS(...) |
| Part 10 | Input VAT reverse charge | =Part5*0.20 |
| Part 11 | Total input VAT | =Part8+Part9+Part10 |
| Part 12 | Net payable/credit | =Part7-Part11 |
| Part 13 | Credit B/F | [manual] |
| Part 14 | Net after credit | =Part12-Part13 |
```

---

## Section 8 — Armenian bank statement reading guide

**CSV format conventions.** Ameriabank and ACBA exports typically use semicolon or comma delimiters with DD.MM.YYYY dates. Ardshinbank exports may use ISO dates.

**Armenian language variants.** ashkhatavardz (salary), tokos (interest), vark (loan), kankhik (cash), gnumner (purchases), vacharqner (sales), pashtpan (lawyer), hashvapah (accountant).

**Internal transfers.** Own-account transfers between client's Ameriabank, ACBA, Ardshinbank accounts. Always exclude.

**Foreign currency.** Convert to AMD at the Central Bank of Armenia rate on the transaction date.

**IBAN prefix.** AM = Armenia.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Inference:* "LLC"/"SRL" endings. *Fallback:* "Sole trader or company?"
### 9.2 VAT registration — *Inference:* asking for VAT return = registered. *Fallback:* "VAT payer or turnover tax?"
### 9.3 TIN (HVHH) — *Fallback:* "What is your tax ID?"
### 9.4 Filing period — *Inference:* statement dates. *Fallback:* "Which month?"
### 9.5 Industry — *Inference:* counterparty mix. *Fallback:* "What does the business do?"
### 9.6 Exempt supplies — *Fallback:* "Do you make exempt sales?" *If yes, R-AM-4 fires.*
### 9.7 Credit B/F — *Always ask:* "VAT credit from previous month?"
### 9.8 Cross-border — *Inference:* foreign IBANs. *Fallback:* "Customers outside Armenia?"

---

## Section 10 — Reference material

### Sources
1. Tax Code of Armenia (as amended) — Articles 40, 64, et seq.
2. SRC e-filing — https://www.petakner.am
3. Central Bank of Armenia rates — https://www.cba.am

### Known gaps
1. IT sector special regime not covered. 2. Turnover tax regime not covered. 3. FEZ rules not covered.

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.
- **v1.x:** Initial skill.

## End of Armenia VAT Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
