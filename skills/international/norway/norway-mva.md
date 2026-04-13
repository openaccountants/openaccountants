---
name: norway-mva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Norway MVA return (MVA-melding) for any client. Trigger on phrases like "prepare MVA return", "Norwegian VAT", "MVA-melding", "merverdiavgift", or any request involving Norway VAT filing. Norway is NOT an EU member but IS in the EEA. There are NO intra-community supplies. All goods from EU are imports. ALWAYS read this skill before touching any Norway MVA work.
version: 2.0
---

# Norway MVA Return Skill (MVA-melding) v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Norway (Norge) |
| Tax name | MVA (Merverdiavgift) |
| Standard rate | 25% |
| Reduced rates | 15% (food and non-alcoholic beverages), 12% (passenger transport, accommodation, cinema, broadcasting, sports events, amusement parks) |
| Zero rate | Exports, international transport, newspapers, electric vehicles (until phase-out), certain services to foreign ships/aircraft |
| Exempt supplies | Financial services, insurance, medical, education, residential rental, cultural events (selected), immovable property (with option to tax) |
| Return form | MVA-melding |
| Filing portal | https://www.altinn.no |
| Authority | Skatteetaten (Norwegian Tax Administration) |
| Currency | NOK |
| Filing frequency | Bi-monthly (standard: Jan-Feb, Mar-Apr, etc.), annual (turnover < NOK 1M), weekly (primary industries) |
| Deadline | 1 month 10 days after period end (e.g., Jan-Feb due 10 April) |
| Registration threshold | NOK 50,000 in 12 months |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending |

**Key jurisdictional note:** Norway is NOT in the EU. No intra-community supplies. No VIES. All goods from EU/non-EU are imports. Services from abroad are reverse-charged.

**MVA-melding post codes:**

| Post | Meaning |
|---|---|
| 1 | Domestic sales and withdrawals at 25% |
| 2 | Domestic sales and withdrawals at 15% |
| 3 | Domestic sales and withdrawals at 12% |
| 4 | Zero-rated domestic sales |
| 5 | Exempt sales |
| 6 | Export sales |
| 7 | Purchases from abroad (reverse charge) — basis |
| 8 | Purchases from abroad (reverse charge) — MVA |
| 9 | Import of goods — basis |
| 10 | Import of goods — MVA |
| 11 | Domestic purchases at 25% — deductible input MVA |
| 12 | Domestic purchases at 15% — deductible input MVA |
| 13 | Domestic purchases at 12% — deductible input MVA |
| 14 | Input MVA on imports (post 10 deductible amount) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate | 25% |
| Unknown purchase status | Not deductible |
| Unknown counterparty | Domestic Norway |
| Unknown business-use | 0% |
| Unknown blocked status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction | NOK 50,000 |
| HIGH tax-delta | NOK 5,000 |
| MEDIUM concentration | >40% |
| MEDIUM defaults | >4 |
| LOW net position | NOK 100,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs
**Minimum viable** — bank statement. Banks: DNB, Nordea, SpareBank 1, Handelsbanken, Danske Bank.

### Refusal catalogue

**R-NO-1 — Below threshold.** *Trigger:* turnover < NOK 50,000. *Message:* "Below registration threshold."

**R-NO-2 — Partial deduction.** *Trigger:* mixed taxable/exempt. *Message:* "Apportionment required per mval. § 8-2. Flag."

**R-NO-3 — Fellesregistrering (group registration).** *Trigger:* VAT group. *Message:* "Group registration requires specialist. Escalate."

**R-NO-4 — Svalbard supplies.** *Trigger:* supplies to/from Svalbard. *Message:* "Svalbard is outside MVA territory. Specialist rules."

---

## Section 3 — Supplier pattern library

### 3.1 Banks
| Pattern | Treatment | Notes |
|---|---|---|
| DNB, NORDEA, SPAREBANK 1, HANDELSBANKEN | EXCLUDE | Financial service exempt |
| RENTER, GEBYRER | EXCLUDE | Interest/fees exempt |

### 3.2 Government
| Pattern | Treatment | Notes |
|---|---|---|
| SKATTEETATEN | EXCLUDE | Tax payment |
| NAV | EXCLUDE | Social security |
| BRØNNØYSUNDREGISTRENE | EXCLUDE | Company registry |

### 3.3 Utilities
| Pattern | Treatment | Notes |
|---|---|---|
| HAFSLUND, STATKRAFT, FJORDKRAFT | Domestic 25% | Electricity |
| TELENOR, TELIA, ICE | Domestic 25% | Telecoms |

### 3.4 SaaS from abroad (reverse charge — all foreign suppliers, EU and non-EU alike)
| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Reverse charge 25% (post 7/8) | Norway treats EU same as non-EU |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Reverse charge 25% (post 7/8) | Same |
| AWS, STRIPE, ATLASSIAN | Reverse charge 25% (post 7/8) | Even if billed from EU |

### 3.5 Food
| Pattern | Treatment | Notes |
|---|---|---|
| REMA 1000, KIWI, MENY, COOP, BUNNPRIS | Domestic 15% for food | Default BLOCK as personal provisioning |
| RESTAURANT | Domestic 25% (restaurant service) | Entertainment: limited deductibility |

### 3.6 Internal transfers
| Pattern | Treatment | Notes |
|---|---|---|
| OVERFØRING EGEN KONTO | EXCLUDE | |
| LØNN, SALARY | EXCLUDE | |

---

## Section 4 — Worked examples

### Example 1 — Foreign SaaS reverse charge (treats EU and non-EU same)
**Input:** `GOOGLE IRELAND ; DEBIT ; NOK 8,500`
**Treatment:** Reverse charge at 25%. Post 7 = NOK 8,500. Post 8 = NOK 2,125. Input deductible. Net zero.

### Example 2 — Food purchase at 15%
**Input:** `REMA 1000 ; DEBIT ; NOK 1,150`
**Treatment:** Food at 15%. Default BLOCK as personal unless business (hospitality).

### Example 3 — Export
**Input:** `UK BUYER LTD ; CREDIT ; NOK 100,000`
**Treatment:** Post 6. Zero-rated. Full input recovery.

### Example 4 — Accommodation at 12%
**Input:** `HOTEL BRISTOL ; DEBIT ; NOK 2,240`
**Treatment:** Accommodation 12%. Net = 2,000. MVA = 240. Post 13 for input.

### Example 5 — Entertainment
**Input:** `RESTAURANT MAAEMO ; DEBIT ; NOK 5,000`
**Treatment:** Entertainment. Limited deductibility. Conservative default: 0%.

### Example 6 — Import of goods
**Input:** `CUSTOMS — import machinery ; DEBIT ; NOK 500,000 + MVA NOK 125,000`
**Treatment:** Post 9 = 500,000. Post 10 = 125,000. Post 14 = 125,000 (deductible).

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 25% (mval. § 5-1)
### 5.2 Reduced rate 15% — food and non-alcoholic beverages (§ 5-2)
### 5.3 Reduced rate 12% — transport, accommodation, cinema, broadcasting, sports (§ 5-3)
### 5.4 Zero rate — exports, international transport, newspapers, electric vehicles
### 5.5 Exempt — financial, insurance, medical, education, residential rental, cultural (selected)
### 5.6 Reverse charge — ALL services from abroad (EU and non-EU alike, mval. § 3-30, § 11-3)
### 5.7 Import of goods — MVA at customs or via postponed accounting
### 5.8 Blocked — entertainment, personal use, vehicle (limited)
### 5.9 Norway-EU: no intra-community. EU goods = imports.

---

## Section 6 — Tier 2 catalogue (compressed)
### 6.1 Vehicle costs — limited recovery, flag
### 6.2 Voluntary registration — for otherwise exempt activities (property), flag
### 6.3 Mixed-use — apportionment, flag
### 6.4 Primary industries — weekly filing, flag

---

## Section 7 — Excel working paper template
Standard layout. Column H accepts MVA-melding post codes.

---

## Section 8 — Bank statement reading guide
**Format:** DNB/Nordea CSV, DD.MM.YYYY, NOK. **Language:** Norwegian (Bokmal/Nynorsk).
**All foreign suppliers:** Reverse charge regardless of EU/non-EU origin.

---

## Section 9 — Onboarding fallback
### 9.1 MVA number — "Norwegian org.nr. + MVA suffix?"
### 9.2 Filing frequency — bi-monthly (standard)
### 9.3 Prior credit — always ask

---

## Section 10 — Reference material

### Sources
1. Merverdiavgiftsloven (mval.) LOV-2009-06-19-58
2. Merverdiavgiftsforskriften (fmva.)
3. Altinn — https://www.altinn.no

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
