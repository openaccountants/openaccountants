---
name: hungary-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Hungary VAT return (form 2565 / AFA bevallas) for any client. Trigger on phrases like "prepare VAT return", "do the AFA", "fill in 2565", "Hungarian VAT", or any request involving Hungary VAT filing. This skill covers Hungary only and standard AFA registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Hungarian VAT work.
version: 2.0
---

# Hungary VAT Return Skill (Form 2565 / AFA Bevallas) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.**

| Field | Value |
|---|---|
| Country | Hungary (Magyarorszag) |
| Standard rate | 27% (highest in the EU) |
| Reduced rates | 18% (accommodation, specified foodstuffs: milk, dairy, flour, bread, eggs, poultry), 5% (medicines, books, newspapers, internet access, restaurant/catering, district heating, live music/theatre, certain new residential property) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods) |
| Return form | Form 2565 (year-coded: 2465 for 2024, 2565 for 2025) |
| Filing portal | https://nav.gov.hu (eBEV / ANYK) |
| Authority | Nemzeti Ado- es Vamhivatal (NAV) |
| Currency | HUF (Hungarian Forint) |
| Filing frequencies | Monthly (default first 3 years + net AFA > HUF 1M); Quarterly (HUF 250K-1M); Annual (< HUF 250K, no EU trade) |
| Deadline | 20th of month following period |
| NAV Online Invoice | Mandatory for all domestic invoices |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key Form 2565 lines:**

| Line | Meaning |
|---|---|
| 01-02 | Domestic supplies at 27% — base / AFA |
| 03-04 | Domestic supplies at 18% — base / AFA |
| 05-06 | Domestic supplies at 5% — base / AFA |
| 07 | Exempt supplies |
| 08 | Intra-EU supplies of goods (0%) |
| 09 | Intra-EU B2B services (0%) |
| 10 | Exports (0%) |
| 11-12 | Intra-EU acquisition of goods — base / AFA |
| 13-14 | EU services received (reverse charge) — base / AFA |
| 15-16 | Non-EU services received (reverse charge) — base / AFA |
| 17-18 | Domestic reverse charge (construction, etc.) — base / AFA |
| 20 | Total output AFA |
| 30 | Total deductible input AFA |
| 31 | Input AFA on domestic purchases |
| 32 | Input AFA on EU acquisitions (reverse charge input) |
| 33 | Input AFA on imports |
| 34 | Input AFA on non-EU services (reverse charge input) |
| 35 | Adjustments |
| 40 | Net AFA payable (Line 20 minus Line 30) |
| 41 | Excess credit (visszaigenyelni hagyott) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 27% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Hungary |
| Unknown B2B vs B2C for EU customer | B2C, charge 27% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | HUF 1,000,000 |
| HIGH tax-delta on single default | HUF 70,000 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net AFA position | HUF 1,750,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: OTP Bank, K&H Bank, Erste Bank Hungary, MBH Bank (merged Magyar Bankholding), CIB Bank, UniCredit HU, Revolut Business, Wise Business.

**Recommended** — sales/purchase invoices, adoszam (tax number), prior form 2565.

**Ideal** — complete register, NAV Online Invoice records, prior period reconciliation.

### Hungary-specific refusal catalogue

**R-HU-1 — Alanyi mentes (exempt small enterprise).** *Trigger:* turnover < HUF 18M (2025) / HUF 20M (2026). *Message:* "Exempt small enterprises do not charge AFA and cannot recover input AFA."

**R-HU-2 — KATA subject.** *Trigger:* client is KATA taxpayer. *Message:* "KATA taxpayers have limited AFA implications. Specialist review required."

**R-HU-3 — Partial exemption.** *Message:* "Mixed supplies require aranyositas. Use an adotanacsado."

**R-HU-4 — VAT group.** *Message:* "Group registration out of scope."

**R-HU-5 — Special schemes.** *Message:* "Margin/travel agent out of scope."

---

## Section 3 — Supplier pattern library

### 3.1 Hungarian banks (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| OTP, OTP BANK | EXCLUDE | Financial service, exempt |
| K&H, K&H BANK | EXCLUDE | Same |
| ERSTE BANK HU, ERSTE | EXCLUDE | Same |
| MBH BANK, BUDAPEST BANK, TAKAREKBANK | EXCLUDE | Same (merged entity) |
| CIB BANK | EXCLUDE | Same |
| UNICREDIT HU | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check subscriptions |
| KAMAT, INTEREST | EXCLUDE | Interest |
| HITEL, KOLCSON, LOAN | EXCLUDE | Loan principal |

### 3.2 Hungarian government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| NAV, NEMZETI ADO | EXCLUDE | Tax payment |
| TB, TARSADALOMBIZTOSITAS | EXCLUDE | Social insurance |
| ONKORMANYZAT, MUNICIPALITY | EXCLUDE | Municipal fees |
| CEGJEGYZEK, COMPANY REGISTER | EXCLUDE | Registration |

### 3.3 Hungarian utilities

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| MVM, ELMÜ-ÉMÁSZ, E.ON HU | Domestic 27% | 31 | Electricity |
| FŐVÁROSI VÍZMŰVEK, VÍZMŰ | Domestic 27% | 31 | Water |
| FŐGÁZ, GÁZ | Domestic 27% | 31 | Gas |
| MAGYAR TELEKOM, T-MOBILE HU | Domestic 27% | 31 | Telecoms |
| VODAFONE HU, YETTEL HU | Domestic 27% | 31 | Telecoms |
| DIGI HU | Domestic 27% | 31 | Telecoms/broadband |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ALLIANZ HUNGARIA | EXCLUDE | Exempt |
| GENERALI BIZTOSITO | EXCLUDE | Same |
| GROUPAMA BIZTOSITO | EXCLUDE | Same |
| BIZTOSITAS, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
|---|---|---|
| MAGYAR POSTA | EXCLUDE for standard post; 27% for parcel | |
| GLS HU | Domestic 27% | Courier |
| MPL (Magyar Posta Logisztika) | Domestic 27% | Parcel |
| DHL INTERNATIONAL | EU reverse charge | Check entity |

### 3.6 SaaS — EU suppliers (reverse charge, Line 13-14 + 32)

| Pattern | Billing entity | Notes |
|---|---|---|
| GOOGLE | Google Ireland Ltd (IE) | EU RC |
| MICROSOFT | Microsoft Ireland (IE) | RC |
| ADOBE | Adobe Ireland (IE) | RC |
| META, FACEBOOK | Meta Ireland (IE) | RC |
| SPOTIFY | Spotify AB (SE) | EU RC |
| DROPBOX | Dropbox Ireland (IE) | RC |
| SLACK | Slack Ireland (IE) | RC |
| ATLASSIAN | Atlassian BV (NL) | EU RC |
| ZOOM | Zoom Ireland (IE) | RC |

### 3.7 SaaS — non-EU suppliers (reverse charge, Line 15-16 + 34)

| Pattern | Billing entity | Notes |
|---|---|---|
| AWS EMEA SARL | LU entity | EU RC (Line 13-14) |
| NOTION | Notion Labs Inc (US) | Non-EU RC |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Non-EU RC |
| OPENAI, CHATGPT | OpenAI Inc (US) | Non-EU RC |
| GITHUB | GitHub Inc (US) | Check if IE |
| FIGMA | Figma Inc (US) | Non-EU RC |
| CANVA | Canva Pty Ltd (AU) | Non-EU RC |

### 3.8 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.9 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| KÖZJEGYZŐ, NOTARY | Domestic 27% | Legal |
| KÖNYVELŐ, ACCOUNTANT | Domestic 27% | Accounting |
| ÜGYVÉD, LAWYER | Domestic 27% | Legal |

### 3.10 Payroll (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TB, JÁRULÉK | EXCLUDE | Social contributions |
| BÉR, FIZETÉS, SALARY | EXCLUDE | Wages |
| SZJA | EXCLUDE | Income tax |

### 3.11 Food retail

| Pattern | Treatment | Notes |
|---|---|---|
| TESCO HU, ALDI HU, LIDL HU, SPAR HU, PENNY | Default BLOCK | Personal provisioning |
| ÉTTEREM, RESTAURANT, VENDÉGLŐ | Default BLOCK | Entertainment |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SAJÁT ÁTUTALÁS, OWN TRANSFER | EXCLUDE | Internal |
| OSZTALÉK, DIVIDEND | EXCLUDE | Out of scope |
| HITELTÖRLESZTÉS, LOAN REPAYMENT | EXCLUDE | Loan principal |
| ATM, KÉSZPÉNZ | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge (Notion)
**Input:** `03.04.2026 ; NOTION LABS INC ; -5,870 HUF`
**Treatment:** Non-EU RC. Line 15 (base). Self-assessed AFA at 27%. Input in Line 34.

### Example 2 — EU service reverse charge (Google Ads)
**Input:** `10.04.2026 ; GOOGLE IRELAND LIMITED ; -340,000 HUF`
**Treatment:** EU RC. Line 13 (base). Line 14 (output AFA at 27%). Line 32 (input).

### Example 3 — Entertainment
**Input:** `15.04.2026 ; BORKONYHA ÉTTEREM ; -88,000 HUF`
**Treatment:** Restaurant. In Hungary, entertainment/representation: input AFA is deductible IF business purpose documented AND invoice compliant. Unlike Malta's hard block. Default: block (purpose unknown).

### Example 4 — EU B2B service sale
**Input:** `22.04.2026 ; STUDIO KREBS GMBH ; +1,400,000 HUF`
**Treatment:** B2B to DE. Line 09. 0%. Verify USt-IdNr.

### Example 5 — Capital goods
**Input:** `18.04.2026 ; MEDIAMARKT HU ; Laptop ; -638,000 HUF`
**Treatment:** Above HUF 200,000: capital goods. 5-year adjustment. Input AFA at 27% in Line 31.

### Example 6 — Motor vehicle
**Input:** `28.04.2026 ; MOL NYRT ; Fuel ; -32,000 HUF`
**Treatment:** In Hungary, passenger car fuel: input AFA deductible if used for business. Default: 0%.

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard 27% (Sec. 82)
Default. Sales: Line 01-02. Input: Line 31.

### 5.2 Reduced 18% (Sec. 82(2))
Accommodation, specified foodstuffs.

### 5.3 Reduced 5% (Sec. 82(2))
Medicines, books, newspapers, internet, restaurant/catering, district heating, performances, certain new residential.

### 5.4 Zero rate / exports
Exports: Line 10. Intra-EU goods: Line 08. Intra-EU services: Line 09.

### 5.5 Exempt (Sec. 85-86)
Financial, insurance, healthcare, education, postal, residential rental, gambling.

### 5.6 Reverse charge — EU (Sec. 140-142)
Goods: Line 11-12. Services: Line 13-14.

### 5.7 Reverse charge — non-EU
Services: Line 15-16.

### 5.8 Capital goods (Sec. 135-136)
> HUF 200,000 net, life > 1 year: 5-year adjustment (movable), 20-year (immovable).

### 5.9 NAV Online Invoice
Mandatory for ALL domestic invoices. Real-time reporting to NAV system.

### 5.10 Blocked input
- Personal use: blocked
- Entertainment: deductible if business purpose (no hard block like Malta)
- Vehicle: no hard block; deductible if business use

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — *Default:* 0%. *Question:* "Business use?"
### 6.2 Entertainment — *Default:* block. *Question:* "Business purpose documented?"
### 6.3 SaaS entity — *Default:* non-EU RC.
### 6.4 Owner transfers — *Default:* exclude.
### 6.5 Large purchases (> HUF 200,000) — *Default:* capital goods register.
### 6.6 Mixed-use telecom — *Default:* 0%.
### 6.7 Cash withdrawals — *Default:* exclude.
### 6.8 KATA status — *Default:* flag reviewer.

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3. Column H accepts Hungarian form 2565 line codes. Bottom-line: Line 40 (payable) or Line 41 (excess credit).

---

## Section 8 — Hungary bank statement reading guide

**CSV conventions.** OTP and K&H use semicolons, YYYY.MM.DD (Hungarian date format).

**Hungarian language.** berleti dij (rent), ber/fizetes (salary), kamat (interest), atutalas (transfer), keszpenz (cash).

**Currency.** HUF. Convert foreign at MNB (Magyar Nemzeti Bank) rate.

**IBAN prefix.** HU = Hungary.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Inference:* Kft. = company; egyeni vallalkozo = sole trader.
### 9.2 AFA registration — *Fallback:* "Standard AFA payer or alanyi mentes?"
### 9.3 Adoszam — *Fallback:* "Tax number? (11 digits)"
### 9.4 Filing frequency — *Fallback:* "Monthly, quarterly, or annual?"
### 9.5 NAV Online Invoice — *Fallback:* "Using NAV Online Invoice system?"
### 9.6 Exempt supplies — *Fallback:* "Any exempt supplies?"
### 9.7 Credit brought forward — *Fallback:* "Excess AFA credit from prior period?"

---

## Section 10 — Reference material

### Sources
1. VAT Act (Act CXXVII of 2007, as amended)
2. NAV Online Invoice Regulation
3. EU VAT Directive 2006/112/EC — via companion skill
4. VIES — https://ec.europa.eu/taxation_customs/vies/

### Change log
- **v2.0 (April 2026):** Full rewrite. Hungarian banks (OTP, K&H, Erste HU).
- **v1.0 (April 2026):** Initial skill.

## End of Hungary VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
