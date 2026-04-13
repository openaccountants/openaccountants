---
name: monaco-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Monaco TVA (VAT) return for any client. Trigger on phrases like "Monaco VAT", "Monaco TVA", "Monaco tax return", or any request involving Monaco VAT. Monaco is within the French VAT territory and applies French TVA rules identically. Supplies between Monaco and France are domestic. For all substantive rules, refer to the France VAT skill. ALWAYS read this skill before touching any Monaco TVA work.
version: 2.0
---

# Monaco TVA Return Skill v2.0

## Section 1 — Quick reference

**Monaco applies French TVA law in full under the Franco-Monegasque Customs Convention of 1963. For all substantive rules, refer to the France VAT skill (france-vat-return).**

| Field | Value |
|---|---|
| Country | Principality of Monaco |
| Tax name | TVA (Taxe sur la Valeur Ajoutee) — identical to French TVA |
| Standard rate | 20% |
| Reduced rates | 10% (restaurants, prepared food, accommodation, passenger transport), 5.5% (food, books, energy, adapted housing), 2.1% (medicines, press, cultural events) |
| Zero rate | Exports outside EU |
| Return form | French CA3 declaration |
| Filing portal | Monaco: https://service-public-entreprises.gouv.mc; filed via Nice tax office |
| Authority | Direction des Services Fiscaux de Monaco (registration); DGFiP France (substantive law) |
| Currency | EUR |
| Filing frequency | Monthly (turnover > EUR 4M HT or TVA > EUR 15,000), quarterly (otherwise), annual (< EUR 1,000 TVA) |
| Deadline | Monthly: 15th-24th of following month; quarterly: within month after quarter |
| Companion skills | vat-workflow-base v0.1+, eu-vat-directive v0.1+ |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending |

**Critical rules:**

- Monaco-France supplies are DOMESTIC (not intra-EU)
- Monaco-EU (non-France) supplies follow France-EU intra-community rules
- Monaco-non-EU supplies follow French export/import rules
- Monaco IS part of the EU VAT territory

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate | 20% |
| Unknown purchase status | Not deductible |
| Unknown counterparty | Domestic Monaco/France |
| Unknown B2B/B2C for EU | B2C, charge 20% |
| Unknown business-use | 0% |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs
**Minimum viable** — bank statement. Banks: CMB (Compagnie Monegasque de Banque), CFM (Credit Foncier de Monaco), Barclays Monaco, HSBC Private Bank Monaco.

### Refusal catalogue
**R-MC-1 — Complex cross-border structures.** *Trigger:* Monaco corporate structures with non-French elements. *Message:* "Requires specialist analysis."
**R-MC-2 — Partial exemption.** *Trigger:* mixed supplies. *Message:* "Pro-rata per French rules. Flag for reviewer."

---

## Section 3 — Supplier pattern library

### 3.1 Monaco/French banks
| Pattern | Treatment | Notes |
|---|---|---|
| CMB, CFM, BARCLAYS MONACO, HSBC MONACO | EXCLUDE | Financial service exempt |
| BNP, SOCIETE GENERALE, CREDIT AGRICOLE | EXCLUDE (French domestic) | Same |

### 3.2 Government
| Pattern | Treatment | Notes |
|---|---|---|
| DIRECTION DES SERVICES FISCAUX | EXCLUDE | Tax payment |
| CCSS MONACO, CAISSES SOCIALES | EXCLUDE | Social security |

### 3.3 Utilities
| Pattern | Treatment | Notes |
|---|---|---|
| SMEG (Societe Monegasque de l'Electricite et du Gaz) | Domestic 20% | Electricity/gas |
| MONACO TELECOM | Domestic 20% | Telecoms |

### 3.4 SaaS — EU/non-EU
Follow French TVA rules exactly. EU suppliers: intra-community reverse charge. Non-EU: import of services.

### 3.5 Food and entertainment
| Pattern | Treatment | Notes |
|---|---|---|
| CARREFOUR, CASINO | Default BLOCK | Personal provisioning |
| RESTAURANT | Domestic 10% (restaurant) | Entertainment: limited deductibility |

### 3.6 Internal transfers
| Pattern | Treatment | Notes |
|---|---|---|
| VIREMENT INTERNE | EXCLUDE | |
| SALAIRE | EXCLUDE | |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge
**Input:** `NOTION LABS INC ; DEBIT ; EUR 14.68`
**Treatment:** Import of services. Self-assess TVA at 20%. Net zero.

### Example 2 — French domestic sale
**Input:** `SA NICE CLIENT ; CREDIT ; EUR 12,000`
**Treatment:** DOMESTIC (Monaco-France). 20%. Net = 10,000. TVA = 2,000.

### Example 3 — Restaurant at 10%
**Input:** `LE LOUIS XV ; DEBIT ; EUR 440`
**Treatment:** Restaurant 10%. Net = 400. TVA = 40. Entertainment: limited deductibility.

### Example 4 — Intra-EU supply to Germany
**Input:** `GERMAN GMBH (DE) ; CREDIT ; EUR 5,000`
**Treatment:** Intra-EU B2B. Zero-rated. Same as France-EU supply.

### Example 5 — Electricity
**Input:** `SMEG ; DEBIT ; EUR 240`
**Treatment:** Domestic 20%. Net = 200. TVA = 40.

### Example 6 — Export outside EU
**Input:** `US BUYER INC ; CREDIT ; EUR 10,000`
**Treatment:** Export. Zero-rated. Customs documentation required.

---

## Section 5 — Tier 1 classification rules (compressed)

All rules follow French CGI Articles 256-298. See France VAT skill for complete details.

### 5.1 Standard 20% — most goods/services
### 5.2 Intermediate 10% — restaurants, accommodation, transport
### 5.3 Reduced 5.5% — food, books, energy
### 5.4 Super-reduced 2.1% — medicines, press
### 5.5 Zero — exports outside EU
### 5.6 Exempt — financial, insurance, medical, education, residential rental
### 5.7 Monaco-France = domestic
### 5.8 Monaco-EU = intra-community (same as France)
### 5.9 Blocked — entertainment (limited), personal use

---

## Section 6 — Tier 2 catalogue (compressed)
### 6.1 Monaco-specific administrative differences — flag
### 6.2 Mixed-use — 0% default
### 6.3 Complex corporate — escalate

---

## Section 7 — Excel working paper template
Standard layout per French CA3 structure.

---

## Section 8 — Bank statement reading guide
**Format:** CMB/CFM CSV, DD/MM/YYYY, EUR. **Language:** French.

---

## Section 9 — Onboarding fallback
### 9.1 TVA number — French-format TVA number (FR + 11 digits)?
### 9.2 Monaco or Nice registration
### 9.3 Prior credit — always ask

---

## Section 10 — Reference material

### Sources
1. French CGI Articles 256-298 (TVA)
2. Franco-Monegasque Customs Convention (1963)
3. EU VAT Directive 2006/112/EC Art. 6-7

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial wrapper skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
