---
name: croatia-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Croatian VAT return (Obrazac PDV) for any client. Trigger on phrases like "prepare VAT return", "do the PDV", "fill in PDV", "create the return", "Croatian VAT", or any request involving Croatia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Croatia only and standard PDV registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Croatian VAT work.
version: 2.0
---

# Croatia VAT Return Skill (Obrazac PDV) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Croatia (Republic of Croatia) |
| Standard rate | 25% |
| Reduced rates | 13% (accommodation, restaurant/catering food, newspapers, water, certain pharmaceuticals, cultural/sporting events, funeral services, firewood), 5% (basic foodstuffs, books, medical equipment, menstrual hygiene) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods) |
| Return form | Obrazac PDV (PDV-S for summary) |
| Filing portal | https://e-porezna.porezna-uprava.hr (ePorezna) |
| Authority | Porezna uprava (Tax Administration), Ministry of Finance |
| Currency | EUR (from 1 January 2023) |
| Filing frequencies | Monthly (default); Quarterly (turnover < EUR 110,000 prior year, no intra-EU acquisitions) |
| Deadline | Last day of the month following the period (from 2026) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key PDV return rows:**

| Row | Meaning |
|---|---|
| I.1 | Supplies outside Croatia (place of supply not HR) |
| I.2 | Exempt supplies without right of deduction |
| I.3 | Exempt supplies with right of deduction (exports, intra-EU) |
| I.4 | Intra-EU supplies of goods |
| I.5 | Intra-EU supplies of services (B2B) |
| II.1 | Domestic supplies at 25% — base |
| II.2 | Output PDV at 25% |
| II.3 | Domestic supplies at 13% — base |
| II.4 | Output PDV at 13% |
| II.5 | Domestic supplies at 5% — base |
| II.6 | Output PDV at 5% |
| II.7 | Self-assessed PDV on EU acquisitions — base |
| II.8 | Self-assessed PDV on EU acquisitions — tax |
| II.9 | Self-assessed PDV on EU services received — base |
| II.10 | Self-assessed PDV on EU services received — tax |
| II.11 | Self-assessed PDV on non-EU services — base |
| II.12 | Self-assessed PDV on non-EU services — tax |
| III.1 | Input PDV on domestic purchases |
| III.2 | Input PDV on EU acquisitions (reverse charge input) |
| III.3 | Input PDV on EU services (reverse charge input) |
| III.4 | Input PDV on non-EU services (reverse charge input) |
| III.5 | Input PDV on imports |
| IV | Total output PDV |
| V | Total input PDV |
| VI | Net PDV payable or refundable (IV minus V) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 25% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Croatia |
| Unknown B2B vs B2C status for EU customer | B2C, charge 25% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 3,000 |
| HIGH tax-delta on a single conservative default | EUR 200 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net PDV position | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Croatian or international bank: Zagrebacka banka (ZABA), PBZ (Privredna banka Zagreb), Erste & Steiermarkische Bank HR, OTP banka, Addiko Bank, RBA (Raiffeisenbank Austria d.d.), Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices (especially for intra-EU B2B and exports), purchase invoices for input PDV claims above EUR 200, client's OIB (11-digit Personal Identification Number).

**Ideal** — complete invoice register, prior period PDV return, fiscalization records (fiskalizacija), reconciliation of credit brought forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement, hard stop. If bank statement only, proceed but record in reviewer brief.

### Croatia-specific refusal catalogue

These apply on top of EU-wide refusals in `eu-vat-directive` Section 13.

**R-HR-1 — Small business exemption attempting PDV return.** *Trigger:* client is exempt (turnover < EUR 60,000) and not voluntarily registered. *Message:* "Exempt small businesses do not file PDV returns. Register voluntarily first if you wish to charge and recover PDV."

**R-HR-2 — Partial exemption.** *Trigger:* client makes both taxable and exempt-without-credit supplies, non-de-minimis. *Message:* "Mixed taxable/exempt supplies require pro-rata input PDV apportionment. Use a qualified accountant."

**R-HR-3 — VAT group.** *Trigger:* client is in a PDV group. *Message:* "PDV groups require consolidation. Out of scope."

**R-HR-4 — Special schemes (margin, travel agent).** *Trigger:* second-hand goods, travel packages. *Message:* "Special schemes require transaction-level computation. Out of scope."

**R-HR-5 — Real estate option to tax.** *Trigger:* client exercises option to tax immovable property (domestic reverse charge). *Message:* "Immovable property transactions with option to tax require specialist review. Out of scope."

**R-HR-6 — Fiscalization non-compliance.** *Trigger:* client has not fiscalized domestic invoices as required. *Message:* "All domestic invoices must be fiscalized (fiskalizacija). Ensure compliance before filing the PDV return."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. Most specific match wins. No match = fall through to Section 5.

### 3.1 Croatian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ZAGREBACKA BANKA, ZABA | EXCLUDE for bank charges/fees | Financial service, exempt |
| PBZ, PRIVREDNA BANKA ZAGREB | EXCLUDE for bank charges/fees | Same |
| ERSTE BANK HR, ERSTE & STEIERMARKISCHE | EXCLUDE for bank charges/fees | Same |
| OTP BANKA HR | EXCLUDE for bank charges/fees | Same |
| ADDIKO BANK | EXCLUDE for bank charges/fees | Same |
| RBA, RAIFFEISENBANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for taxable subscription invoices |
| KAMATA, INTEREST | EXCLUDE | Interest, out of scope |
| KREDIT, LOAN, ZAJAM | EXCLUDE | Loan principal, out of scope |

### 3.2 Croatian government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| POREZNA UPRAVA, TAX ADMINISTRATION | EXCLUDE | Tax payment |
| HZZO, CROATIAN HEALTH INSURANCE | EXCLUDE | Social security |
| HZMO, PENSION FUND | EXCLUDE | Pension contribution |
| HGK, CROATIAN CHAMBER OF COMMERCE | EXCLUDE | Membership (check if PDV applies) |
| FINA | EXCLUDE | Government agency fees |
| SUDSKI REGISTAR, COURT REGISTER | EXCLUDE | Registration fees |

### 3.3 Croatian utilities

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| HEP, HRVATSKA ELEKTROPRIVREDA | Domestic 25% | III.1 | Electricity |
| VODOVOD, VODOOPSKRBA | Domestic 13% | III.1 | Water supply at 13% |
| HRVATSKI TELEKOM, HT, T-COM | Domestic 25% | III.1 | Telecoms |
| A1 HRVATSKA, A1 HR | Domestic 25% | III.1 | Telecoms |
| TELEMACH | Domestic 25% | III.1 | Telecoms/broadband |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CROATIA OSIGURANJE | EXCLUDE | Insurance, exempt |
| ALLIANZ HRVATSKA | EXCLUDE | Same |
| GENERALI OSIGURANJE | EXCLUDE | Same |
| EUROHERC | EXCLUDE | Same |
| UNIQA HR | EXCLUDE | Same |
| OSIGURANJE, INSURANCE, POLICA | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| HRVATSKA POSTA, HP | EXCLUDE for standard post | | Universal service, exempt |
| HRVATSKA POSTA (parcel/courier) | Domestic 25% | III.1 | Non-universal services |
| OVERSEAS EXPRESS | Domestic 25% | III.1 | Courier |
| DPD HR | Domestic 25% | III.1 | Courier |
| DHL INTERNATIONAL | EU reverse charge (IE/DE entity) | III.3 | Check invoice |

### 3.6 Transport

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| HZ PUTNICKI PRIJEVOZ, CROATIAN RAILWAYS | Domestic 25% or 13% | III.1 | Domestic rail |
| ZET, ZAGREB TRAM | EXCLUDE / 13% | | Public transport |
| UBER, BOLT (platform fee) | EU reverse charge (IE entity) | III.3 | Platform fee; underlying ride domestic |
| CROATIA AIRLINES (international) | EXCLUDE / 0% | | International flight |

### 3.7 Food retail (blocked unless hospitality)

| Pattern | Treatment | Notes |
|---|---|---|
| KONZUM, KAUFLAND, LIDL HR, SPAR HR, PLODINE | Default BLOCK input PDV | Personal provisioning |
| RESTAURANT, RESTORAN, KAFIC | Default BLOCK | Entertainment |

### 3.8 SaaS — EU suppliers (reverse charge, Row II.9/II.10 + III.3)

| Pattern | Billing entity | Row | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | II.9/II.10 + III.3 | Reverse charge services |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | II.9/II.10 + III.3 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | II.9/II.10 + III.3 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | II.9/II.10 + III.3 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | II.9/II.10 + III.3 | Reverse charge |
| SPOTIFY | Spotify AB (SE) | II.9/II.10 + III.3 | EU reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | II.9/II.10 + III.3 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | II.9/II.10 + III.3 | Reverse charge |
| ATLASSIAN | Atlassian Network Services BV (NL) | II.9/II.10 + III.3 | EU reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | II.9/II.10 + III.3 | Reverse charge |
| STRIPE (subscription) | Stripe Technology Europe Ltd (IE) | II.9/II.10 + III.3 | Transaction fees exempt |

### 3.9 SaaS — non-EU suppliers (reverse charge, Row II.11/II.12 + III.4)

| Pattern | Billing entity | Row | Notes |
|---|---|---|---|
| AWS EMEA SARL | AWS EMEA SARL (LU) | II.9/II.10 + III.3 | LU = EU reverse charge |
| NOTION | Notion Labs Inc (US) | II.11/II.12 + III.4 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | II.11/II.12 + III.4 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | II.11/II.12 + III.4 | Non-EU reverse charge |
| GITHUB | GitHub Inc (US) | II.11/II.12 + III.4 | Check if billed by IE |
| FIGMA | Figma Inc (US) | II.11/II.12 + III.4 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | II.11/II.12 + III.4 | Non-EU reverse charge |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.11 Professional services (Croatia)

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| JAVNI BILJEZNIK, NOTAR | Domestic 25% | III.1 | Notary |
| RACUNOVODSTVO, ACCOUNTANT | Domestic 25% | III.1 | Accounting |
| ODVJETNIK, LAWYER | Domestic 25% | III.1 | Legal |

### 3.12 Payroll and social security (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| HZZO, HZMO | EXCLUDE | Social contributions |
| PLACA, SALARY, WAGES | EXCLUDE | Wages |
| POREZ NA DOHODAK | EXCLUDE | Income tax |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| NAJAM, RENT (commercial with PDV) | Domestic 25% | Commercial lease |
| NAJAM, RENT (residential) | EXCLUDE | Residential exempt |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| INTERNI PRIJENOS, OWN TRANSFER | EXCLUDE | Internal movement |
| DIVIDENDA, DIVIDEND | EXCLUDE | Out of scope |
| OTPLATA KREDITA, LOAN REPAYMENT | EXCLUDE | Loan principal |
| BANKOMAT, ATM, CASH WITHDRAWAL | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
US entity. Reverse charge under VAT Act Art. 17(1). Self-assess output PDV at 25% in Row II.11/II.12, input PDV in Row III.4. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | PDV | Rate | Row (input) | Row (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.67 | 25% | III.4 | II.11/II.12 | N | — | — |

### Example 2 — EU service reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads ; -850.00 ; EUR`

**Reasoning:**
IE entity. EU reverse charge. Output in Row II.9/II.10, input in Row III.3.

**Output:**

| Date | Counterparty | Gross | Net | PDV | Rate | Row (input) | Row (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 212.50 | 25% | III.3 | II.9/II.10 | N | — | — |

### Example 3 — Entertainment, blocked

**Input line:**
`15.04.2026 ; RESTORAN DUBRAVKIN PUT ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant. Entertainment/representation in Croatia: input PDV is NOT deductible for entertainment (VAT Act Art. 61). Block.

**Output:**

| Date | Counterparty | Gross | Net | PDV | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORAN DUBRAVKIN PUT | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked" |

### Example 4 — Capital goods

**Input line:**
`18.04.2026 ; LINKS D.O.O. ; DEBIT ; Laptop Dell ; -1,595.00 ; EUR`

**Reasoning:**
Movable capital goods above the threshold (EUR 6,636 for 5-year adjustment). This laptop at EUR 1,595 is below the adjustment threshold — treat as overhead. Input PDV deductible at 25%.

**Output:**

| Date | Counterparty | Gross | Net | PDV | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | LINKS D.O.O. | -1,595.00 | -1,276.00 | -319.00 | 25% | III.1 | N | — | — |

### Example 5 — EU B2B service sale

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
B2B service to Germany. Place of supply = Germany. Report in Row I.5 at 0%. Verify customer's USt-IdNr.

**Output:**

| Date | Counterparty | Gross | Net | PDV | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | I.5 | Y | Q2 (HIGH) | "Verify German USt-IdNr" |

### Example 6 — Motor vehicle, restricted

**Input line:**
`28.04.2026 ; INA D.D. ; DEBIT ; Fuel ; -80.00 ; EUR`

**Reasoning:**
Fuel for passenger vehicle. In Croatia, input PDV on passenger vehicles and related costs (fuel, maintenance) is deductible only for vehicles used exclusively for business (taxi, driving school, rental, delivery). Default: 0% recovery.

**Output:**

| Date | Counterparty | Gross | Net | PDV | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | INA D.D. | -80.00 | -80.00 | 0 | — | — | Y | Q3 | "Vehicle: confirm exclusive business use" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 25% (VAT Act Art. 38(1))
Default rate. Sales: Row II.1/II.2. Purchases: Row III.1.

### 5.2 Reduced rate 13% (VAT Act Art. 38(2))
Accommodation, restaurant/catering (food and non-alcoholic beverages), newspapers, water supply, certain pharmaceuticals, cultural/sporting events, funeral services, firewood.

### 5.3 Super-reduced rate 5% (VAT Act Art. 38(3))
Basic foodstuffs (bread, milk, eggs, cooking oil, baby food), books (printed/electronic), medical equipment, menstrual hygiene products.

### 5.4 Zero rate and exempt with credit
Exports: Row I.3. Intra-EU B2B goods: Row I.4. Intra-EU B2B services: Row I.5. International transport: Row I.3.

### 5.5 Exempt without credit
Financial services, insurance, healthcare, education, postal universal service, residential rental (>2 years), gambling, transfer of going concern.

### 5.6 Reverse charge — EU services received (VAT Act Art. 17(1))
Output PDV self-assessed at 25% in Row II.9/II.10, input PDV in Row III.3.

### 5.7 Reverse charge — EU goods received
Output in Row II.7/II.8, input in Row III.2.

### 5.8 Reverse charge — non-EU services received
Output in Row II.11/II.12, input in Row III.4.

### 5.9 Imports
Import PDV on customs declaration. Input in Row III.5.

### 5.10 Capital goods (VAT Act Art. 64-65)
Immovable property: 10-year adjustment. Movable capital goods (> EUR 6,636): 5-year adjustment.

### 5.11 Blocked input PDV (VAT Act Art. 61)
- Entertainment/representation: fully blocked (no exceptions)
- Passenger vehicles and related costs (fuel, maintenance): blocked unless exclusively for taxable business (taxi, driving school, rental, delivery)
- Personal use items: blocked
- Goods/services for exempt supplies: blocked

### 5.12 Fiscalization (Zakon o fiskalizaciji)
All domestic invoices must be fiscalized. Non-compliance is a separate obligation — does not affect PDV classification but must be flagged.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs
*Default:* 0% recovery. *Question:* "Passenger car or commercial? Exclusive business use?"

### 6.2 Restaurants and entertainment
*Default:* block. *Question:* "Entertainment meal? (Note: blocked regardless of purpose in Croatia.)"

### 6.3 Ambiguous SaaS billing entities
*Default:* non-EU reverse charge. *Question:* "Check invoice for legal entity and billing country."

### 6.4 Round-number incoming transfers
*Default:* exclude as owner injection. *Question:* "Customer payment, own money, or loan?"

### 6.5 Incoming from individuals
*Default:* domestic B2C at 25%. *Question:* "Sale? B2B or B2C? Country?"

### 6.6 Foreign counterparty incoming
*Default:* domestic 25%. *Question:* "B2B with VAT number? Country?"

### 6.7 Large purchases (capital goods)
*Default:* if > EUR 6,636 gross, flag for adjustment tracking. *Question:* "Confirm total invoice amount."

### 6.8 Mixed-use phone/internet/home office
*Default:* 0%. *Question:* "Dedicated business or mixed-use?"

### 6.9 Outgoing to individuals
*Default:* exclude as drawings. *Question:* "Contractor, wages, or personal?"

### 6.10 Cash withdrawals
*Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments
*Default:* no PDV (residential). *Question:* "Commercial or residential?"

### 6.12 Water supply rate
*Default:* 13%. *Question:* "Confirm water supply invoice (13% reduced rate)."

---

## Section 7 — Excel working paper template (Croatia-specific)

Per `vat-workflow-base` Section 3 base. Column H accepts Croatia PDV row codes. Sheet "Row Summary" maps to Obrazac PDV rows I.1 through VI. Bottom-line: Row VI (net payable/refundable).

---

## Section 8 — Croatia bank statement reading guide

**CSV conventions.** ZABA and PBZ use semicolons with DD.MM.YYYY. Revolut uses ISO dates.

**Croatian language.** najam (rent), placa (salary), kamata (interest), prijenos (transfer), gotovina (cash).

**Internal transfers.** "Interni prijenos", "vlastiti racun". Exclude.

**Sole trader draws.** Self-employed (obrt) cannot pay themselves wages. Exclude.

**HRK legacy.** Croatia adopted EUR on 1 January 2023. Any pre-2023 HRK amounts must be converted at the fixed rate 7.53450 HRK = 1 EUR.

**IBAN prefix.** HR = Croatia. IE, DE, NL = EU. US, GB = non-EU.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference:* d.o.o. = limited, obrt = sole trader. *Fallback:* "Are you obrt (sole trader) or d.o.o. (company)?"

### 9.2 PDV registration
*Fallback:* "Are you PDV-registered (mandatory or voluntary)?"

### 9.3 OIB
*Fallback:* "What is your OIB? (11 digits)"

### 9.4 Filing period
*Inference:* transaction dates; monthly or quarterly. *Fallback:* "Which period?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Fallback:* "Do you make exempt supplies?" *If yes: R-HR-2 may fire.*

### 9.8 Credit brought forward
*Fallback:* "Excess PDV credit from prior period?"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Croatia? EU or non-EU? B2B or B2C?"

### 9.10 Fiscalization status
*Fallback:* "Are your invoices fiscalized?"

---

## Section 10 — Reference material

### Sources
1. Zakon o porezu na dodanu vrijednost (VAT Act, OG 73/13, as amended)
2. Pravilnik o PDV-u (VAT Regulation)
3. Zakon o fiskalizaciji (Fiscalization Act)
4. EU VAT Directive 2006/112/EC — via eu-vat-directive companion skill
5. VIES — https://ec.europa.eu/taxation_customs/vies/

### Known gaps
1. Supplier library does not cover every Croatian SME.
2. Fiscalization technical compliance not detailed.
3. Construction domestic reverse charge not covered in depth.

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. Croatian banks (ZABA, PBZ, Erste HR).
- **v1.0 (April 2026):** Initial skill.

### Self-check
1. Quick reference with row table and conservative defaults: yes.
2. Supplier library: yes (14 sub-tables).
3. Worked examples (6): yes.
4. No inline [T1]/[T2]/[T3] tags: yes.
5. 10-section structure: yes.

## End of Croatia VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
