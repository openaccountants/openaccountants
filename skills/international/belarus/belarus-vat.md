---
name: belarus-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Belarus VAT (NDS) return for any client. Trigger on phrases like "Belarus VAT", "Belarusian NDS", "MNS filing", or any request involving Belarusian VAT. This skill covers standard NDS payers filing monthly/quarterly returns. Simplified taxation and individual entrepreneur special regimes are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Belarus VAT work.
version: 2.0
---

# Belarus VAT (NDS) Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Belarus (Republic of Belarus) |
| Tax name | NDS (Nalog na Dobavlennuyu Stoimost / VAT) |
| Standard rate | 20% |
| Reduced rates | 10% (certain food, children's goods, agricultural produce) |
| Zero rate | 0% (exports, international transport) |
| Return form | NDS declaration (electronic) |
| Filing portal | https://www.portal.nalog.gov.by |
| Authority | Ministry of Taxes and Duties (MNS) |
| Currency | BYN (Belarusian Ruble) only |
| Filing frequency | Monthly or quarterly (quarterly if revenue below threshold) |
| Deadline | 20th of the month following the reporting period |
| EAEU membership | Yes — special rules for intra-EAEU trade (Russia, Kazakhstan, Armenia, Kyrgyzstan) |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key NDS return boxes:**

| Box | Meaning |
|---|---|
| 1 | Taxable supplies at 20% — base |
| 2 | Output NDS at 20% |
| 3 | Taxable supplies at 10% — base |
| 4 | Output NDS at 10% |
| 5 | Zero-rated supplies (exports) |
| 6 | Exempt supplies |
| 7 | Reverse charge on imported services — base |
| 8 | Output NDS on reverse charge |
| 9 | EAEU goods imports — base |
| 10 | NDS on EAEU imports |
| 11 | Total output NDS |
| 12 | Input NDS on domestic purchases |
| 13 | Import NDS (customs or EAEU) |
| 14 | Input NDS on reverse charge (creditable) |
| 15 | Total input NDS |
| 16 | Net NDS payable or credit |
| 17 | Credit brought forward |
| 18 | Net payable |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Belarus |
| Unknown EAEU vs non-EAEU origin | Non-EAEU (customs import) |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (Box 7/8/14) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | BYN 15,000 |
| HIGH tax-delta on a single default | BYN 1,000 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net NDS position | BYN 30,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: Belarusbank, Belinvestbank, Priorbank, BPS-Sberbank, Alfa-Bank Belarus, MTBank, or any other.

**Recommended** — sales/purchase invoices, ESHF (electronic invoices) register, client UNP (TIN).

**Ideal** — complete ESHF register, EAEU trade documentation, prior period declaration.

### Refusal catalogue

**R-BY-1 — Simplified taxation.** *Trigger:* client on simplified regime. *Message:* "Simplified taxation payers have different NDS obligations. Out of scope."

**R-BY-2 — Individual entrepreneur special regime.** *Trigger:* IE on special regime without NDS obligations. *Message:* "IE special regimes may not require NDS returns. Out of scope."

**R-BY-3 — Partial exemption.** *Trigger:* mixed taxable and exempt. *Message:* "Input NDS apportionment required. Use a qualified practitioner."

**R-BY-4 — Free economic zone.** *Trigger:* FEZ entity. *Message:* "FEZ entities have special NDS rules. Out of scope."

**R-BY-5 — EAEU complex transactions.** *Trigger:* complex intra-EAEU supply chains (triangulation, tolling). *Message:* "Complex EAEU transactions require specialist analysis. Out of scope."

**R-BY-6 — Sanctions-related.** *Trigger:* transaction involves sanctioned entities or restricted goods. *Message:* "Sanctions compliance is outside this skill's scope. Seek legal advice."

---

## Section 3 — Supplier pattern library

### 3.1 Belarusian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BELARUSBANK | EXCLUDE | Financial service, exempt |
| BELINVESTBANK, BELINVEST | EXCLUDE | Same |
| PRIORBANK, PRIOR | EXCLUDE | Same |
| BPS-SBERBANK, ALFA-BANK BY | EXCLUDE | Same |
| MTBANK, BELGAZPROMBANK | EXCLUDE | Same |
| PROTSENTY, INTEREST | EXCLUDE | Interest, out of scope |
| KREDIT, LOAN | EXCLUDE | Loan principal |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MNS, NALOG, TAX INSPECTORATE | EXCLUDE | Tax payment |
| TAMOZHNYA, CUSTOMS | EXCLUDE | Duty (see import NDS separately) |
| FSZN, SOCIAL PROTECTION | EXCLUDE | Social contributions |
| BELGOSSTRAKH (mandatory insurance) | EXCLUDE | Statutory insurance |

### 3.3 Utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| ENERGOSBYT, ENERGO, MINSK ENERGIA | Domestic 20% | 12 | Electricity |
| MINSKVODOKANAL, VODOKANAL | Domestic 20% | 12 | Water |
| MINGAZ, GAZSNABZHENIE | Domestic 20% | 12 | Gas |
| A1, MTS BELARUS, LIFE:) | Domestic 20% | 12 | Telecoms |
| BELTELECOM | Domestic 20% | 12 | Fixed telecoms/internet |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BELGOSSTRAKH, BROSCO, PROMTRANSINVEST | EXCLUDE | Exempt |
| STRAKHOVANIE, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| EUROOPT, GREEN, KORONA, SANTA | Default BLOCK | Personal provisioning |
| RESTORAN, KAFE, BAR | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

| Pattern | Box | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | 7/8/14 | Reverse charge at 20% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | 7/8/14 | Same |

### 3.7 EAEU suppliers (special treatment)

| Pattern | Treatment | Notes |
|---|---|---|
| Russian, Kazakh, Armenian, Kyrgyz suppliers | EAEU import — Box 9/10 | NDS paid via EAEU protocol, not customs |

### 3.8 Professional services

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NOTAR, NOTARIUS | Domestic 20% | 12 | If business purpose |
| AUDITOR, BUKHGALTER | Domestic 20% | 12 | Deductible |
| ADVOKAT, LAWYER | Domestic 20% | 12 | If business matter |

### 3.9 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| ZARPLATA, SALARY | EXCLUDE | Wages |
| DIVIDEND | EXCLUDE | Out of scope |
| VNUTRENNIY, INTERNAL | EXCLUDE | Internal transfer |
| BANKOMAT, ATM | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00 ; BYN 52.80`

**Reasoning:** US entity. Reverse charge at 20%. Box 7 (base), Box 8 (output NDS), Box 14 (input credit). Net zero.

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -52.80 | -52.80 | 10.56 | 20% | 14 | 7/8 | N |

### Example 2 — EAEU import (from Russia)

**Input line:** `10.04.2026 ; OOO TECHNOPARK MOSCOW ; DEBIT ; Server equipment ; -8,500.00 ; BYN`

**Reasoning:** Russian supplier (EAEU). EAEU import protocol — NDS self-assessed, not at customs. Box 9 (base), Box 10 (NDS). Input credit if for taxable supplies.

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | OOO TECHNOPARK | -8,500 | -8,500 | 1,700 | 20% | 13 | 9/10 | N |

### Example 3 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTORAN VASILKI ; DEBIT ; Business dinner ; -350.00 ; BYN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORAN VASILKI | -350.00 | -350.00 | 0 | — | — | Y | "Entertainment: blocked" |

### Example 4 — Export (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT services ; +12,000.00 ; BYN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TECHCORP GMBH | +12,000 | +12,000 | 0 | 0% | 5 | Y | "Verify export docs" |

### Example 5 — Motor vehicle blocked

**Input line:** `28.04.2026 ; ATLANT-M ; DEBIT ; Car lease ; -1,800.00 ; BYN`

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | ATLANT-M | -1,800.00 | -1,800.00 | 0 | — | — | Y | "Vehicle: blocked" |

### Example 6 — Reduced rate purchase (10%)

**Input line:** `20.04.2026 ; AGROKOMBINAT ; DEBIT ; Agricultural produce ; -2,200.00 ; BYN`

**Reasoning:** Agricultural produce at 10% reduced rate. Input NDS deductible.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
|---|---|---|---|---|---|---|---|
| 20.04.2026 | AGROKOMBINAT | -2,200 | -2,000 | -200 | 10% | 12 | N |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 20% (Tax Code Article 122)
Default rate. Sales to Box 1/2. Purchases to Box 12.

### 5.2 Reduced rate 10%
Certain food products, children's goods, agricultural produce (listed in Tax Code). Sales to Box 3/4.

### 5.3 Zero rate
Exports, international transport. Box 5. Requires customs/export documentation.

### 5.4 Exempt supplies
Financial services, insurance, medical, educational, residential rental, postal, cultural.

### 5.5 Reverse charge — non-resident services
Self-assess at 20%. Box 7/8 (output), Box 14 (input credit). Net zero.

### 5.6 EAEU imports
Goods from Russia, Kazakhstan, Armenia, Kyrgyzstan: NDS self-assessed under EAEU protocol (not at customs). Box 9/10. Separate EAEU import declaration required by 20th of month following import.

### 5.7 Non-EAEU imports
At customs. Base = customs value + duties. Box 13. Recoverable.

### 5.8 Blocked input NDS
Passenger vehicles, entertainment, personal consumption, no valid invoice/ESHF.

### 5.9 Electronic invoicing (ESHF)
Mandatory electronic invoicing system. All VAT invoices must be issued via ESHF portal. Input NDS credit requires ESHF-registered invoice.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%. *Question:* "Car or commercial?"
### 6.2 Entertainment — *Default:* block.
### 6.3 SaaS entities — *Default:* reverse charge. *Question:* "Check invoice."
### 6.4 EAEU vs non-EAEU supplier — *Default:* non-EAEU. *Question:* "Is supplier from EAEU country?"
### 6.5 Owner transfers — *Default:* exclude.
### 6.6 Foreign incoming — *Default:* zero-rated. *Question:* "Export docs?"
### 6.7 Large purchases — *Question:* "Fixed asset?"
### 6.8 Mixed-use phone — *Default:* 0%.
### 6.9 Cash withdrawals — *Default:* exclude.
### 6.10 Rent — *Default:* no NDS. *Question:* "Commercial with NDS?"

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Belarus-specific box codes.

---

## Section 8 — Belarusian bank statement reading guide

**CSV conventions.** Belarusbank and Belinvestbank exports use semicolon delimiters, DD.MM.YYYY dates. Priorbank may use comma delimiters.

**Russian/Belarusian terms.** Zarplata (salary), protsenty (interest), kredit (loan), nalichnye (cash), vnutrenniy (internal), tamozhnya (customs), strakhovanie (insurance), bukhgalter (accountant).

**Internal transfers.** Between client's accounts. Always exclude.

**Foreign currency.** Convert to BYN at the National Bank of Belarus rate.

**IBAN prefix.** BY = Belarus.

**EAEU trade indicators.** Payments to/from Russian, Kazakh, Armenian, Kyrgyz counterparties or IBANs (RU, KZ, AM, KG) indicate potential EAEU protocol treatment.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Fallback:* "Sole trader (IE) or company (OOO/OAO)?"
### 9.2 NDS registration — *Fallback:* "Standard NDS payer?"
### 9.3 UNP — *Fallback:* "What is your UNP?"
### 9.4 Period — *Inference:* statement dates. *Fallback:* "Monthly or quarterly? Which period?"
### 9.5 Industry — *Fallback:* "What does the business do?"
### 9.6 EAEU trade — *Inference:* RU/KZ/AM/KG counterparties. *Fallback:* "Do you trade with EAEU countries?"
### 9.7 Exempt supplies — *If yes, R-BY-3 fires.*
### 9.8 Credit B/F — *Always ask.*

---

## Section 10 — Reference material

### Sources
1. Tax Code of Belarus — Chapter 14 (NDS)
2. EAEU Treaty, Annex on Indirect Taxes
3. MNS portal — https://www.portal.nalog.gov.by
4. National Bank of Belarus rates — https://www.nbrb.by

### Known gaps
1. EAEU triangulation/tolling not covered. 2. Simplified regime not covered. 3. Sanctions impact on cross-border classification not analyzed.

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Belarus VAT (NDS) Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
