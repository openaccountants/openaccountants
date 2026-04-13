---
name: latvia-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Latvian VAT return (PVN deklaracija / PVN 1 form) for any client. Trigger on phrases like "prepare VAT return", "Latvian VAT", "PVN return", "PVN1", "pievienotas vertibas nodoklis", or any request involving Latvia VAT filing. This skill covers standard PVN-registered businesses only. MUST be loaded alongside BOTH vat-workflow-base and eu-vat-directive companion skills. ALWAYS read this skill before touching any Latvia VAT work.
version: 2.0
---

# Latvia PVN Return Skill (PVN 1) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1. The EU directive content is in `eu-vat-directive`.**

| Field | Value |
|---|---|
| Country | Latvia (Latvija) |
| Standard rate | 21% |
| Reduced rates | 12% (food, pharmaceuticals, hotel accommodation, domestic heating, passenger transport, books/periodicals), 5% (locally produced fruits/vegetables — seasonal) |
| Zero rate | Exports, intra-EU B2B supplies |
| Return form | PVN deklaracija (PVN 1) |
| Filing portal | https://eds.vid.gov.lv (EDS) |
| Authority | Valsts ienemumu dienests (VID) |
| Currency | EUR |
| Filing frequency | Monthly (intra-EU or turnover > EUR 50,000), quarterly (EUR 14,228-50,000), bi-annual (< EUR 14,228) |
| Deadline | 20th of month following period |
| Companion skill (workflow) | vat-workflow-base v0.1+ |
| Companion skill (EU directive) | eu-vat-directive v0.1+ |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending — requires validation by licensed Latvian accountant |
| Validation date | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 21% |
| Unknown PVN status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Latvia |
| Unknown B2B vs B2C for EU customer | B2C, charge 21% |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 3,000 |
| HIGH tax-delta on a single conservative default | EUR 200 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net PVN position | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: Swedbank Latvia, SEB banka, Citadele, Luminor, BlueOrange, or any other.

**Recommended** — sales/purchase invoices, VAT number (LV + 11 digits).

**Ideal** — complete invoice register, prior PVN 1.

### Latvia-specific refusal catalogue (supplements eu-vat-directive R-EU-1 through R-EU-12)

**R-LV-1 — Micro-enterprise tax regime.** *Trigger:* client is on micro-enterprise tax. *Message:* "Micro-enterprise taxpayers may have different PVN obligations. Flag for reviewer."

**R-LV-2 — Partial exemption.** *Trigger:* mixed taxable/exempt. *Message:* "Pro-rata required. Flag for reviewer."

**R-LV-3 — Timber/construction domestic reverse charge.** *Trigger:* timber or construction services. *Message:* "Domestic reverse charge applies for timber and construction. Specialist analysis required."

---

## Section 3 — Supplier pattern library

### 3.1 Latvian banks (fees exempt — exclude)
| Pattern | Treatment | Notes |
|---|---|---|
| SWEDBANK, SEB, CITADELE, LUMINOR | EXCLUDE for fees | Financial service exempt |
| PROCENTI, INTEREST | EXCLUDE | Interest exempt |

### 3.2 Government (exclude)
| Pattern | Treatment | Notes |
|---|---|---|
| VID, VALSTS IENEMUMU DIENESTS | EXCLUDE | Tax payment |
| VSAA | EXCLUDE | Social security |
| UZNEMUMU REGISTRS | EXCLUDE | Company registration |

### 3.3 Utilities
| Pattern | Treatment | Notes |
|---|---|---|
| LATVENERGO, SADALES TIKLS | Domestic 21% | Electricity |
| LATVIJAS GAZE, ENERĢIJAS PUBLISKAIS TIRGOTĀJS | Domestic 21% | Gas/heating — check 12% for domestic heating |
| LMT, TELE2, BITE | Domestic 21% | Telecoms |

### 3.4 SaaS — EU (reverse charge)
| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE IRELAND, MICROSOFT IRELAND, ADOBE IRELAND | EU reverse charge | Intra-EU services |
| SPOTIFY AB (SE), ATLASSIAN (NL) | EU reverse charge | Same |

### 3.5 SaaS — non-EU (reverse charge)
| Pattern | Treatment | Notes |
|---|---|---|
| NOTION, ANTHROPIC, OPENAI, FIGMA, CANVA | Non-EU reverse charge | |
| GITHUB (US) | Non-EU reverse charge | Check if billed by IE entity |

### 3.6 Food and entertainment (blocked)
| Pattern | Treatment | Notes |
|---|---|---|
| RIMI, MAXIMA, LIDL, TOP, MEGO | Default BLOCK | Personal provisioning |
| RESTORĀNS, KAFEJNĪCA | Default BLOCK | Entertainment — 60% cap on representation |

### 3.7 Insurance (exempt)
| Pattern | Treatment | Notes |
|---|---|---|
| BALTA, BTA, IF APDROŠINĀŠANA | EXCLUDE | Insurance exempt |

### 3.8 Professional services
| Pattern | Treatment | Notes |
|---|---|---|
| ZVĒRINĀTAIS REVIDENTS, AUDITORS | Domestic 21% | |
| ADVOKĀTS, JURISTA BIROJS | Domestic 21% | |
| NOTĀRS | Domestic 21% | |

### 3.9 Internal transfers
| Pattern | Treatment | Notes |
|---|---|---|
| IEKŠĒJAIS PĀRSKAITĪJUMS | EXCLUDE | |
| ALGA, DARBA SAMAKSA | EXCLUDE | Salary |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge
**Input:** `NOTION LABS INC ; DEBIT ; EUR 14.68`
**Treatment:** Non-EU reverse charge. Output and input PVN at 21%. Net zero.

### Example 2 — EU service reverse charge (Google Ads)
**Input:** `GOOGLE IRELAND LIMITED ; DEBIT ; EUR 850.00`
**Treatment:** EU reverse charge. Intra-EU services. Output and input PVN at 21%.

### Example 3 — Entertainment (representation — 60% cap)
**Input:** `RESTORĀNS VINCENTS ; DEBIT ; EUR 220`
**Treatment:** Representation expenses have 60% PVN recovery cap in Latvia. Flag for reviewer. Conservative default: 0%.

### Example 4 — Capital goods
**Input:** `DELL TECHNOLOGIES ; DEBIT ; EUR 1,595`
**Treatment:** Capital goods. Input PVN at 21%.

### Example 5 — EU B2B service sale
**Input:** `STUDIO KREBS GMBH (DE) ; CREDIT ; EUR 3,500`
**Treatment:** B2B service to EU customer. Zero-rated. Verify DE USt-IdNr via VIES.

### Example 6 — Motor vehicle, partial block
**Input:** `SIA AUTOCENTRS ; DEBIT ; car lease ; EUR 650`
**Treatment:** Latvia limits PVN recovery on passenger vehicles. Conservative default: 0%. Flag for reviewer.

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 21%
Default. Most goods and services.

### 5.2 Reduced rate 12%
Food products, pharmaceuticals, hotel accommodation, domestic heating, passenger transport, books/periodicals.

### 5.3 Reduced rate 5%
Locally produced seasonal fruits and vegetables.

### 5.4 Zero rate
Exports, intra-EU B2B supplies (goods and services).

### 5.5 Exempt without credit
Financial services, insurance, medical, education, residential rental, postal universal service.

### 5.6 Reverse charge — EU services
Standard EU reverse charge per eu-vat-directive.

### 5.7 Reverse charge — non-EU services
Self-assess at 21%.

### 5.8 Domestic reverse charge
Timber, scrap metal, construction services — domestic reverse charge.

### 5.9 Blocked input PVN
Entertainment (above 60% representation cap), passenger vehicles (limited recovery), personal use.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs
*Default:* 0%. *Question:* "Confirm vehicle type and business-use proportion."

### 6.2 Representation expenses
*Default:* 0%. *Question:* "60% cap applies for documented business representation. Confirm."

### 6.3 Timber/construction reverse charge
*Default:* flag. *Question:* "Confirm if domestic reverse charge applies."

### 6.4 Mixed-use expenses
*Default:* 0%. *Question:* "Business proportion?"

---

## Section 7 — Excel working paper template
Standard layout. Column H accepts PVN 1 row codes.

---

## Section 8 — Bank statement reading guide
**Format:** Swedbank/SEB CSV, DD.MM.YYYY, EUR. **Language:** Latvian or English.
**Internal transfers:** "Iekšējais pārskaitījums". Exclude.

---

## Section 9 — Onboarding fallback

### 9.1 PVN number
*Fallback:* "What is your PVN number? (LV + 11 digits)"

### 9.2 Filing frequency
*Inference:* from turnover. *Fallback:* "Monthly, quarterly, or bi-annual?"

### 9.3 Credit brought forward
Always ask.

---

## Section 10 — Reference material

### Sources
1. Pievienotas vertibas nodokla likums (PVN likums) — Latvian VAT Act
2. EU VAT Directive 2006/112/EC
3. VID EDS portal — https://eds.vid.gov.lv

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture with companion skill references.
- **v1.0-draft:** Initial skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
