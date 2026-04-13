---
name: liechtenstein-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Liechtenstein VAT (MWST) return for any client. Trigger on phrases like "Liechtenstein VAT", "MWST Liechtenstein", "Liechtenstein tax return", or any request involving Liechtenstein VAT. Liechtenstein forms a customs union with Switzerland and applies Swiss MWST law identically. Supplies between Liechtenstein and Switzerland are domestic. ALWAYS read this skill before touching any Liechtenstein MWST work.
version: 2.0
---

# Liechtenstein MWST Return Skill v2.0

## Section 1 — Quick reference

**Liechtenstein applies Swiss MWST law in full via the Customs Union Treaty of 1923. For all substantive rules, refer to the Switzerland VAT skill.**

| Field | Value |
|---|---|
| Country | Principality of Liechtenstein |
| Tax name | MWST (Mehrwertsteuer) — identical to Swiss MWST |
| Standard rate | 8.1% (from 1 Jan 2024) |
| Reduced rate | 2.6% (food, medicines, books, newspapers) |
| Special rate | 3.8% (accommodation) |
| Zero rate | Exports outside CH/LI customs territory |
| Exempt supplies | Medical, education, insurance, financial services, residential rental, cultural/sporting events (selected) |
| Return form | Swiss MWST return (filed through Swiss FTA system) |
| Filing portal | Liechtenstein registration: https://www.llv.li; returns via Swiss FTA |
| Authority | Steuerverwaltung Liechtenstein (registration); Swiss ESTV/AFC (substantive law) |
| Currency | CHF |
| Filing frequency | Quarterly (standard); semi-annual or monthly (by arrangement) |
| Deadline | 60 days after quarter end |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending |
| Validation date | Pending |

**Critical customs union rules:**

- Supplies between Liechtenstein and Switzerland are DOMESTIC — not imports/exports
- Supplies between Liechtenstein and the EU are treated as third-country trade (same as CH-EU)
- Liechtenstein is in the EEA but NOT in the EU VAT system
- No EU VIES for Liechtenstein entities

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 8.1% |
| Unknown MWST status of a purchase | Not deductible |
| Unknown counterparty country | Domestic LI/CH |
| Unknown business-use proportion | 0% recovery |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | CHF 5,000 |
| HIGH tax-delta | CHF 500 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net position | CHF 10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the quarter. Acceptable from: LGT, VP Bank, Liechtensteinische Landesbank, or Swiss/international banks.

### Refusal catalogue

**R-LI-1 — EEA vs customs union conflict.** *Trigger:* complex cross-border structure exploiting EEA membership for EU access while using customs union for MWST. *Message:* "Requires specialist analysis."

**R-LI-2 — Partial exemption.** *Trigger:* mixed supplies. *Message:* "Pro-rata required. Flag for reviewer."

---

## Section 3 — Supplier pattern library

### 3.1 Liechtenstein/Swiss banks
| Pattern | Treatment | Notes |
|---|---|---|
| LGT, VP BANK, LLB | EXCLUDE for interest/fees | Financial services exempt |
| UBS, CREDIT SUISSE, ZKB | EXCLUDE (Swiss domestic) | Same |

### 3.2 Government
| Pattern | Treatment | Notes |
|---|---|---|
| STEUERVERWALTUNG, AHV/IV | EXCLUDE | Tax/social security |
| HANDELSREGISTER | EXCLUDE | Registration fee |

### 3.3 Utilities
| Pattern | Treatment | Notes |
|---|---|---|
| LKW (Liechtensteinische Kraftwerke) | Domestic 8.1% | Electricity |
| TELECOM LIECHTENSTEIN, SALT, SWISSCOM | Domestic 8.1% | Telecoms |

### 3.4 SaaS — non-CH/LI suppliers (import of services)
| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Import tax at 8.1% | Self-assess (Bezugsteuer) |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Import tax at 8.1% | Same |

### 3.5 Food and entertainment
| Pattern | Treatment | Notes |
|---|---|---|
| COOP, MIGROS, DENNER, ALDI, LIDL | Domestic 2.6% for food | Check for mixed items |
| RESTAURANT | Domestic 8.1% for service; food component may be 2.6% | Complex split |

### 3.6 Internal transfers
| Pattern | Treatment | Notes |
|---|---|---|
| EIGENÜBERWEISUNG, INTERNER TRANSFER | EXCLUDE | |
| GEHALT, LOHN | EXCLUDE | Salary |

---

## Section 4 — Worked examples

### Example 1 — Import of services (US SaaS)
**Input:** `NOTION LABS INC ; DEBIT ; CHF 15.00`
**Treatment:** Bezugsteuer (import tax) at 8.1%. Self-assess output and input. Net zero.

### Example 2 — Swiss domestic sale
**Input:** `SWISS CLIENT AG ; CREDIT ; CHF 10,810`
**Treatment:** Domestic (CH/LI customs union). Net = 10,000. MWST = 810. Standard 8.1%.

### Example 3 — Entertainment
**Input:** `RESTAURANT TORKEL ; DEBIT ; CHF 350`
**Treatment:** Business entertainment. MWST may be partially recoverable under Swiss rules (not hard-blocked like EU). Flag for reviewer if personal element.

### Example 4 — Export to EU
**Input:** `GERMAN COMPANY GMBH ; CREDIT ; CHF 5,000`
**Treatment:** Export from customs territory. Zero-rated. Requires export documentation.

### Example 5 — Accommodation at 3.8%
**Input:** `HOTEL MALBUN ; DEBIT ; CHF 207.60`
**Treatment:** Accommodation at 3.8%. Net = 200. MWST = 7.60. Deductible if business.

### Example 6 — Food purchase at 2.6%
**Input:** `COOP VADUZ ; DEBIT ; CHF 51.30`
**Treatment:** Food at reduced rate 2.6%. Default BLOCK as personal provisioning unless hospitality.

---

## Section 5 — Tier 1 classification rules (compressed)

All rules follow Swiss MWSTG. See Switzerland VAT skill for complete details.

### 5.1 Standard rate 8.1% — most goods and services
### 5.2 Reduced rate 2.6% — food, medicines, books, newspapers
### 5.3 Accommodation rate 3.8% — hotel/accommodation
### 5.4 Zero rate — exports outside CH/LI customs territory
### 5.5 Exempt — medical, education, insurance, financial, residential rental
### 5.6 Import tax (Bezugsteuer) — services from non-CH/LI suppliers
### 5.7 Import of goods — MWST at customs
### 5.8 CH-LI supplies are domestic — never export/import

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 EEA implications
*Default:* flag. *Question:* "Does EEA membership affect this transaction?"

### 6.2 Mixed-use expenses
*Default:* 0%. *Question:* "Business proportion?"

### 6.3 Vehicle costs
Swiss rules on vehicle MWST recovery. *Default:* flag.

---

## Section 7 — Excel working paper template
Standard layout per Swiss MWST return structure.

---

## Section 8 — Bank statement reading guide
**Format:** LGT/VP Bank CSV, DD.MM.YYYY, CHF. **Language:** German.
**CH/LI distinction:** Supplies between LI and CH are domestic.

---

## Section 9 — Onboarding fallback

### 9.1 MWST number
*Fallback:* "What is your MWST number?"

### 9.2 CH or LI registration
*Fallback:* "Registered through Liechtenstein Steuerverwaltung?"

### 9.3 Prior credit
Always ask.

---

## Section 10 — Reference material

### Sources
1. Swiss MWSTG (Mehrwertsteuergesetz) — applied in Liechtenstein via Customs Union Treaty
2. Customs Union Treaty (1923, as amended)
3. Liechtenstein MWST Ordinance
4. Steuerverwaltung — https://www.llv.li

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial wrapper skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
