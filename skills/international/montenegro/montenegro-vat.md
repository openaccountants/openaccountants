---
name: montenegro-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Montenegro VAT (PDV) return for any client. Trigger on phrases like "Montenegro VAT", "Montenegrin PDV", "Montenegro tax return", or any request involving Montenegrin VAT. Montenegro has 21% standard, 15% intermediate, and 7% reduced rates. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Montenegrin VAT work.
version: 2.0
---

# Montenegro VAT (PDV) Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Montenegro (Crna Gora) |
| Tax name | PDV (Porez na Dodatu Vrijednost) |
| Standard rate | 21% |
| Intermediate rate | 15% (food for human consumption) |
| Reduced rate | 7% (bread, milk, textbooks, medicines, medical devices, accommodation, public transport) |
| Zero rate | 0% (exports, international transport) |
| Return form | Monthly PDV declaration |
| Filing portal | https://eprijava.tax.gov.me |
| Authority | Tax Administration of Montenegro (Poreska Uprava) |
| Currency | EUR (Montenegro uses the euro unilaterally) |
| Filing frequency | Monthly |
| Deadline | 15th of the month following the reporting month |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key PDV return boxes:**

| Box | Meaning |
|---|---|
| 1 | Taxable supplies at 21% — base |
| 2 | Output PDV at 21% |
| 3 | Taxable supplies at 15% — base |
| 4 | Output PDV at 15% |
| 5 | Taxable supplies at 7% — base |
| 6 | Output PDV at 7% |
| 7 | Zero-rated supplies |
| 8 | Exempt supplies |
| 9 | Reverse charge imported services — base |
| 10 | Output PDV on reverse charge |
| 11 | Total output PDV |
| 12 | Input PDV on domestic purchases (21%) |
| 13 | Input PDV on domestic purchases (15%) |
| 14 | Input PDV on domestic purchases (7%) |
| 15 | Import PDV |
| 16 | Input PDV reverse charge (creditable) |
| 17 | Total input PDV |
| 18 | Net payable or credit |
| 19 | Credit B/F |
| 20 | Net payable |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 21% |
| Unknown purchase status | Not deductible |
| Unknown counterparty country | Domestic Montenegro |
| Unknown SaaS billing entity | Reverse charge (Box 9/10/16) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 3,000 |
| HIGH tax-delta | EUR 200 |
| MEDIUM counterparty concentration | >40% |
| LOW absolute net PDV | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement. Acceptable from: CKB (Crnogorska Komercijalna Banka), NLB Montenegro, Erste Bank Montenegro, Hipotekarna Banka, Addiko Bank ME, or any other.

**Recommended** — invoices, client PIB (tax ID).

### Refusal catalogue

**R-ME-1 — Non-registered.** Below EUR 30,000 threshold. *Message:* "Not PDV registered. Out of scope."

**R-ME-2 — Partial exemption.** *Message:* "Apportionment required."

**R-ME-3 — Income tax.** *Message:* "This skill handles PDV only."

---

## Section 3 — Supplier pattern library

### 3.1 Montenegrin banks (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CKB, CRNOGORSKA KOMERCIJALNA | EXCLUDE | Financial service, exempt |
| NLB MONTENEGRO, NLB ME | EXCLUDE | Same |
| ERSTE MONTENEGRO, HIPOTEKARNA | EXCLUDE | Same |
| ADDIKO ME, LOVĆEN BANKA | EXCLUDE | Same |
| KAMATA, INTEREST | EXCLUDE | Interest |
| KREDIT, LOAN | EXCLUDE | Loan |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| PORESKA UPRAVA, TAX ADMIN | EXCLUDE | Tax payment |
| CARINA, CUSTOMS | EXCLUDE | Duty |
| FOND PIO, FOND ZDRAVSTVA | EXCLUDE | Social/health |

### 3.3 Utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| EPCG, ELEKTROPRIVREDA CG | Domestic 21% | 12 | Electricity |
| VODOVOD, VODOKANAL | Domestic 21% | 12 | Water |
| CRNOGORSKI TELEKOM, M:TEL ME, TELENOR ME | Domestic 21% | 12 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| LOVĆEN OSIGURANJE, UNIQA ME, SAVA ME | EXCLUDE | Exempt |
| OSIGURANJE, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| VOLI, IDEA ME, RODA | Default BLOCK | Personal provisioning |
| RESTORAN, KAFANA, BAR | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

| Pattern | Box | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | 9/10/16 | Reverse charge at 21% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | 9/10/16 | Same |

### 3.7 Tourism/accommodation

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| HOTEL (income from tourists) | 7% output PDV | 5/6 | Accommodation reduced rate |
| BOOKING.COM payout | Flag for rate determination | — | Accommodation vs platform fee |

### 3.8 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| PLATA, SALARY | EXCLUDE | Wages |
| DIVIDENDA | EXCLUDE | Out of scope |
| INTERNI, INTERNAL | EXCLUDE | Internal |
| BANKOMAT, ATM | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; EUR 16.00`

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -16.00 | -16.00 | 3.36 | 21% | 16 | 9/10 | N |

### Example 2 — Domestic utility

**Input line:** `10.04.2026 ; CRNOGORSKI TELEKOM ; DEBIT ; Internet April ; -35.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 10.04.2026 | CRNOGORSKI TELEKOM | -35.00 | -28.93 | -6.07 | 21% | 12 | N |

### Example 3 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTORAN KONOBA CATOVICA ; DEBIT ; Dinner ; -95.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORAN KONOBA CATOVICA | -95.00 | -95.00 | 0 | — | — | Y | "Entertainment: blocked" |

### Example 4 — Export (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT services ; +3,500.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TECHCORP GMBH | +3,500 | +3,500 | 0 | 0% | 7 | Y | "Verify export docs" |

### Example 5 — Accommodation income at 7%

**Input line:** `20.04.2026 ; BOOKING.COM ; CREDIT ; Guest payout April ; +2,800.00 ; EUR`

**Reasoning:** Short-term accommodation — 7% reduced rate. Platform fee from Booking.com (NL entity) is separate reverse charge.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 20.04.2026 | BOOKING.COM (accommodation) | +2,800 | +2,617 | +183 | 7% | 5/6 | Y | "Confirm duration, separate platform fee" |

### Example 6 — Motor vehicle blocked

**Input line:** `28.04.2026 ; DELTA MOTORS ME ; DEBIT ; Car lease ; -450.00 ; EUR`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | DELTA MOTORS ME | -450.00 | -450.00 | 0 | — | — | Y | "Vehicle: blocked" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 21%
Default. Sales to Box 1/2. Purchases to Box 12.

### 5.2 Intermediate rate 15%
Food for human consumption (not beverages, not restaurant meals). Sales to Box 3/4. Purchases to Box 13.

### 5.3 Reduced rate 7%
Bread, milk, textbooks, medicines, medical devices, accommodation (short-term), public transport. Sales to Box 5/6. Purchases to Box 14.

### 5.4 Zero rate
Exports, international transport. Box 7.

### 5.5 Exempt
Financial, insurance, medical services, education, residential rental, postal.

### 5.6 Reverse charge
Non-resident services. Self-assess at 21%. Box 9/10 (output), Box 16 (input).

### 5.7 Import PDV
At customs. Box 15.

### 5.8 Blocked
Passenger vehicles, entertainment, personal consumption, no valid invoice.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%.
### 6.2 Entertainment — *Default:* block.
### 6.3 SaaS entities — *Default:* reverse charge at 21%.
### 6.4 Rate determination (21%/15%/7%) — *Default:* 21%.
### 6.5 Tourism income — *Default:* flag for reviewer. *Question:* "Short-term accommodation?"
### 6.6 Owner transfers — *Default:* exclude.
### 6.7 Foreign incoming — *Default:* zero-rated.
### 6.8 Cash withdrawals — *Default:* exclude.

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Montenegro-specific box codes. Note EUR currency.

---

## Section 8 — Montenegrin bank statement reading guide

**CSV conventions.** CKB and NLB Montenegro use semicolons, DD.MM.YYYY.

**Montenegrin/Serbian terms.** Plata (salary), kamata (interest), kredit (loan), gotovina (cash), interni (internal), carina (customs), osiguranje (insurance).

**Currency.** Montenegro uses EUR unilaterally. No conversion needed.

**IBAN prefix.** ME = Montenegro.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Fallback:* "Sole trader or company (DOO/AD)?"
### 9.2 PDV registration — *Fallback:* "PDV payer?"
### 9.3 PIB — *Fallback:* "What is your PIB?"
### 9.4 Period — *Inference:* statement dates.
### 9.5 Industry — *Inference:* tourism/accommodation from Booking.com payouts. *Fallback:* "What does the business do?"
### 9.6 Credit B/F — *Always ask.*

---

## Section 10 — Reference material

### Sources
1. Law on Value Added Tax of Montenegro (Zakon o PDV-u)
2. Tax Administration — https://eprijava.tax.gov.me
3. Central Bank of Montenegro — https://www.cbcg.me

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Montenegro VAT (PDV) Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
