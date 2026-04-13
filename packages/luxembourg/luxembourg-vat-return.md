---
name: luxembourg-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Luxembourg VAT return (TVA declaration) for any client. Trigger on phrases like "prepare VAT return", "Luxembourg VAT", "TVA Luxembourg", "AED return", or any request involving Luxembourg VAT filing. MUST be loaded alongside BOTH vat-workflow-base and eu-vat-directive. Holding company structures (SOPARFI/SIF/RAIF/SICAR) are in the refusal catalogue. ALWAYS read this skill before touching any Luxembourg VAT work.
version: 2.0
---

# Luxembourg TVA Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Luxembourg |
| Standard rate | 17% (lowest in the EU) |
| Reduced rates | 14% (wine, certain fuels, advertising printed matter), 8% (gas, electricity, cut flowers, hairdressing), 3% (food, books, medicines, children's clothing, accommodation, restaurants — from 2024) |
| Zero rate | Exports, intra-EU B2B supplies |
| Return form | TVA declaration |
| Filing portal | https://ecdf.b2g.etat.lu (eCDF) |
| Authority | AED (Administration de l'enregistrement, des domaines et de la TVA) |
| Currency | EUR |
| Filing frequency | Monthly (turnover > EUR 620,000), quarterly (EUR 112,000-620,000), annual (< EUR 112,000) |
| Deadline | Monthly/quarterly: 15th of month following; annual: 1 May |
| Small business exemption | EUR 50,000 (from 2025) |
| Companion skills | vat-workflow-base v0.1+, eu-vat-directive v0.1+ |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate | 17% |
| Unknown purchase status | Not deductible |
| Unknown counterparty country | Domestic Luxembourg |
| Unknown B2B/B2C for EU | B2C, charge 17% |
| Unknown business-use | 0% |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction | EUR 5,000 |
| HIGH tax-delta | EUR 300 |
| MEDIUM concentration | >40% |
| MEDIUM defaults | >4 |
| LOW net position | EUR 10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs
**Minimum viable** — bank statement. Banks: BCEE (Spuerkeess), BGL BNP Paribas, ING Luxembourg, Banque de Luxembourg, Raiffeisen.
**Recommended** — invoices, TVA number (LU + 8 digits).
**Ideal** — prior TVA declaration, eCDF submission data.

### Refusal catalogue (supplements eu-vat-directive)

**R-LU-1 — Holding company (SOPARFI/SIF/RAIF/SICAR).** *Trigger:* client is a holding or fund structure. *Message:* "Holding company and fund structures have extremely complex TVA positions (often fully exempt with partial recovery issues). Requires specialist adviser."

**R-LU-2 — Fund management.** *Trigger:* management company for investment funds. *Message:* "Fund management TVA is highly specialized. Escalate."

**R-LU-3 — Partial exemption.** *Trigger:* mixed supplies (extremely common in Luxembourg financial sector). *Message:* "Pro-rata required. Given Luxembourg's financial sector dominance, this is the norm rather than exception. Flag for reviewer."

---

## Section 3 — Supplier pattern library

### 3.1 Luxembourg banks
| Pattern | Treatment | Notes |
|---|---|---|
| BCEE, SPUERKEESS | EXCLUDE for fees/interest | Financial service exempt |
| BGL BNP PARIBAS, ING LUXEMBOURG | EXCLUDE | Same |
| BANQUE DE LUXEMBOURG, RAIFFEISEN | EXCLUDE | Same |

### 3.2 Government
| Pattern | Treatment | Notes |
|---|---|---|
| AED, ADMINISTRATION ENREGISTREMENT | EXCLUDE | Tax payment |
| CCSS (Centre Commun de la Securite Sociale) | EXCLUDE | Social security |
| REGISTRE DE COMMERCE | EXCLUDE | Registration |

### 3.3 Utilities
| Pattern | Treatment | Notes |
|---|---|---|
| CREOS, ENOVOS, SUDSTROUM | Domestic 8% | Gas/electricity (reduced) |
| POST LUXEMBOURG | Domestic 17% for non-universal services | Universal postal exempt |
| TANGO, POST TELECOM, ORANGE LU | Domestic 17% | Telecoms |

### 3.4 SaaS — EU (reverse charge)
| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE IRELAND, MICROSOFT IRELAND, ADOBE IRELAND | EU reverse charge | |
| Note: many SaaS companies bill FROM Luxembourg (Amazon, PayPal) — these are DOMESTIC | Domestic 17% | Check invoice |

### 3.5 SaaS — non-EU
| Pattern | Treatment | Notes |
|---|---|---|
| NOTION, ANTHROPIC, OPENAI, FIGMA | Non-EU reverse charge | |

### 3.6 Food and entertainment
| Pattern | Treatment | Notes |
|---|---|---|
| CACTUS, DELHAIZE, MATCH, AUCHAN | Default BLOCK | Personal provisioning |
| RESTAURANT | Domestic 3% (restaurant/catering) | If business entertainment, limited deductibility |

### 3.7 Insurance
| Pattern | Treatment | Notes |
|---|---|---|
| LA LUXEMBOURGEOISE, FOYER, LALUX | EXCLUDE | Insurance exempt |

### 3.8 Professional services
| Pattern | Treatment | Notes |
|---|---|---|
| EXPERT-COMPTABLE, REVISEUR | Domestic 17% | |
| AVOCAT, NOTAIRE | Domestic 17% | |

### 3.9 Internal transfers
| Pattern | Treatment | Notes |
|---|---|---|
| VIREMENT INTERNE | EXCLUDE | |
| SALAIRE | EXCLUDE | |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge
**Input:** `NOTION LABS INC ; DEBIT ; EUR 14.68`
**Treatment:** Non-EU reverse charge at 17%. Net zero.

### Example 2 — EU service reverse charge
**Input:** `GOOGLE IRELAND ; DEBIT ; EUR 850`
**Treatment:** EU reverse charge at 17%.

### Example 3 — Restaurant at super-reduced 3%
**Input:** `RESTAURANT CLAIREFONTAINE ; DEBIT ; EUR 206`
**Treatment:** Restaurant services at 3%. Net = 200. TVA = 6. If entertainment: limited deductibility. Flag.

### Example 4 — Electricity at 8%
**Input:** `ENOVOS ; DEBIT ; EUR 216`
**Treatment:** Domestic 8%. Net = 200. TVA = 16.

### Example 5 — EU B2B service sale
**Input:** `STUDIO KREBS GMBH (DE) ; CREDIT ; EUR 3,500`
**Treatment:** Zero-rated. Verify DE USt-IdNr.

### Example 6 — Amazon (billed from LU)
**Input:** `AMAZON EU SARL ; DEBIT ; EUR 50`
**Treatment:** Amazon EU SARL is a Luxembourg entity — DOMESTIC 17%, not reverse charge.

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 17%
### 5.2 Intermediate rate 14% — wine, certain fuels, advertising print
### 5.3 Reduced rate 8% — gas, electricity, cut flowers, hairdressing
### 5.4 Super-reduced rate 3% — food, books, medicines, children's clothing, accommodation, restaurants
### 5.5 Zero rate — exports, intra-EU B2B
### 5.6 Exempt — financial services, insurance, medical, education, residential rental
### 5.7 EU/non-EU reverse charge — per companion skills
### 5.8 Blocked input — entertainment (limited), personal use

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Financial sector TVA — nearly always partial exemption
### 6.2 Holding company input recovery — flag
### 6.3 Amazon/PayPal LU entities — domestic, not reverse charge
### 6.4 Restaurant entertainment — 3% but deductibility limited

---

## Section 7 — Excel working paper template
Standard layout. Column H accepts Luxembourg TVA box codes.

---

## Section 8 — Bank statement reading guide
**Format:** BCEE/BGL CSV, DD/MM/YYYY, EUR. **Language:** French, German, or Luxembourgish.
**Internal transfers:** "Virement interne". Exclude.

---

## Section 9 — Onboarding fallback
### 9.1 TVA number — "LU + 8 digits?"
### 9.2 Filing frequency — infer from turnover
### 9.3 Financial sector — "Are you in financial services?" (triggers partial exemption)
### 9.4 Prior credit — always ask

---

## Section 10 — Reference material

### Sources
1. Loi du 12 fevrier 1979 (TVA Law, as amended)
2. EU VAT Directive 2006/112/EC
3. AED/eCDF — https://ecdf.b2g.etat.lu

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
