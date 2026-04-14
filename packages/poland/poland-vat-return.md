---
name: poland-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Polish VAT return (JPK_V7M / JPK_V7K) for a self-employed individual or small business in Poland. Trigger on phrases like "prepare VAT return", "do the VAT", "Polish VAT", "JPK", "deklaracja VAT", "plik JPK", or any request involving Poland VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Poland only and only standard czynny podatnik VAT registrations. VAT groups (grupa VAT), special economic zones, and fiscal representatives are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Polish VAT work.
version: 2.0
---

# Poland VAT Return Skill (JPK_V7M / JPK_V7K) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Poland (Rzeczpospolita Polska) |
| Standard rate | 23% |
| Reduced rates | 8% (food, restaurant services, passenger transport, certain construction/renovation of residential buildings), 5% (basic foodstuffs, books, periodicals, hygiene products) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods, certain agricultural inputs) |
| Return form | JPK_V7M (monthly filers) or JPK_V7K (quarterly filers — deklaracja quarterly, ewidencja monthly) |
| Filing portal | e-Urząd Skarbowy (https://e-urzadskarbowy.podatki.gov.pl) |
| Authority | Krajowa Administracja Skarbowa (KAS — National Revenue Administration) |
| Currency | PLN only |
| Filing frequencies | Monthly (JPK_V7M — standard); Quarterly (JPK_V7K — available to "mały podatnik" with annual turnover ≤ EUR 2M equivalent) |
| Deadline | 25th of month following period end (both monthly and quarterly) |
| KSeF status | Krajowy System e-Faktur — mandatory structured e-invoicing phased in from 2026 |
| Split payment (MPP) | Mandatory for Annex 15 goods/services where invoice ≥ PLN 15,000 gross |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants |
| Validated by | Pending — requires doradca podatkowy validation |
| Validation date | Pending |

**Key JPK_V7 fields (deklaracja section):**

| Field | Meaning |
|---|---|
| K_10 | Net value of domestic sales at 23% |
| K_11 | Output VAT at 23% on domestic sales |
| K_12 | Net value of domestic sales at 8% |
| K_13 | Output VAT at 8% |
| K_14 | Net value of domestic sales at 5% |
| K_15 | Output VAT at 5% |
| K_16 | Net value of domestic sales at 0% |
| K_17 | Net value of intra-EU supplies of goods (WDT) |
| K_18 | Net value of exports |
| K_19 | Net value of intra-EU supplies of services (where buyer accounts for VAT) |
| K_20 | Net value of domestic supplies where buyer accounts for VAT (reverse charge) |
| K_21 | Net value of exempt supplies |
| K_22 | Net value of supplies not subject to VAT |
| K_23 | Net value of intra-EU acquisitions of goods (WNT) |
| K_24 | Output VAT on WNT |
| K_25 | Net value of import of goods (customs) |
| K_26 | Output VAT on import of goods |
| K_27 | Net value of import of services (Art. 28b) |
| K_28 | Output VAT on import of services |
| K_29 | Net value of domestic purchases where buyer accounts (Art. 17(1)(7-8)) |
| K_30 | Output VAT on domestic reverse charge |
| K_31 | Net value of intra-EU acquisitions of services |
| K_32 | Output VAT on EU service acquisitions |
| K_34 | Total output VAT (sum of K_11+K_13+K_15+K_24+K_26+K_28+K_30+K_32) |
| K_40 | Input VAT on domestic purchases |
| K_41 | Input VAT on intra-EU acquisitions |
| K_42 | Input VAT on imports |
| K_43 | Input VAT on domestic reverse charge |
| K_44 | Input VAT corrections (prior period) |
| K_45 | Total input VAT (K_40+K_41+K_42+K_43+K_44) |
| K_46 | Excess input over output (if K_45 > K_34) |
| K_47 | Excess output over input (if K_34 > K_45) — VAT payable |
| K_48 | Amount requested as refund |
| K_49 | Amount carried forward to next period |
| K_50 | VAT payable to the tax office |

**GTU codes (required in ewidencja section):**

| Code | Category |
|---|---|
| GTU_01 | Alcohol |
| GTU_02 | Fuel |
| GTU_03 | Heating oil |
| GTU_04 | Tobacco |
| GTU_05 | Waste |
| GTU_06 | Electronic devices |
| GTU_07 | Vehicles and parts |
| GTU_08 | Precious metals and scrap |
| GTU_09 | Pharmaceuticals |
| GTU_10 | Buildings and land |
| GTU_11 | Emission rights and similar |
| GTU_12 | Intangible services (advisory, legal, accounting, management) |
| GTU_13 | Transport and storage |

**Conservative defaults — Poland-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 23% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Poland |
| Unknown B2B vs B2C status for EU customer | B2C, charge 23% |
| Unknown business-use proportion (vehicle, phone) | 50% recovery (vehicle default per Art. 86a) |
| Unknown SaaS billing entity | Reverse charge from non-EU (K_27/K_28) |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown white list status of supplier | WARN — verify before payment |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | PLN 15,000 (also triggers split payment check) |
| HIGH tax-delta on a single conservative default | PLN 1,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | PLN 25,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from: PKO BP, mBank, ING Bank Śląski, Santander Bank Polska, Bank Pekao, Alior Bank, BNP Paribas PL, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices (faktury sprzedaży) for the period, purchase invoices (faktury zakupu) for input VAT claims above PLN 1,000, NIP number, white list verification for suppliers.

**Ideal** — complete invoice register, KSeF export (when available), prior period JPK_V7, white list verification log.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement → hard stop. If bank statement only → proceed with reviewer brief warning about invoice verification and white list checks.

### Poland-specific refusal catalogue

These apply on top of EU-wide refusals in `eu-vat-directive` Section 13.

**R-PL-1 — VAT-exempt entity (podatnik zwolniony).** *Trigger:* client is VAT-exempt (Art. 113 — turnover ≤ PLN 200,000). *Message:* "VAT-exempt entities do not file JPK_V7. They have no obligation to charge or recover VAT. This skill covers czynny podatnik VAT only."

**R-PL-2 — VAT group (grupa VAT).** *Trigger:* client is part of a VAT group under Art. 15a. *Message:* "VAT groups require consolidated filing. Out of scope."

**R-PL-3 — Fiscal representative.** *Trigger:* non-resident with fiscal representative. *Message:* "Fiscal representative obligations are beyond this skill."

**R-PL-4 — Partial exemption (proporcja/prewspółczynnik).** *Trigger:* client makes both taxable and exempt supplies, exempt proportion non-de-minimis. *Message:* "You make both taxable and exempt supplies. Input VAT must be apportioned under Art. 90 (proporcja) and/or Art. 86 ust. 2a (prewspółczynnik). Please use a doradca podatkowy."

**R-PL-5 — Special economic zone.** *Trigger:* client operates in a special economic zone with VAT exemptions. *Message:* "Special economic zone VAT rules require specialist advice. Out of scope."

**R-PL-6 — Margin scheme (VAT marża).** *Trigger:* client deals in second-hand goods, art, antiques, or travel agent packages under margin scheme. *Message:* "Margin scheme requires transaction-level margin computation. Out of scope."

**R-PL-7 — Income tax instead of VAT.** *Trigger:* user asks about PIT/CIT. *Message:* "This skill handles JPK_V7 (VAT) only. For Polish income tax, use the appropriate skill."

**R-PL-8 — KSeF mandatory e-invoicing dispute.** *Trigger:* client's invoices should be on KSeF but are not. *Message:* "If mandatory KSeF e-invoicing applies, invoices not submitted through KSeF may not be valid for input VAT deduction. Please verify KSeF compliance with a doradca podatkowy before claiming input VAT."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Polish banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| PKO BP, PKO BANK POLSKI | EXCLUDE for bank charges/fees | Financial service, exempt Art. 43 ust. 1 pkt 38-41 |
| MBANK, BRE BANK | EXCLUDE | Same |
| ING BANK ŚLĄSKI, ING PL | EXCLUDE | Same |
| SANTANDER BANK POLSKA, BZWBK | EXCLUDE | Same |
| BANK PEKAO, PEKAO SA | EXCLUDE | Same |
| ALIOR BANK, BNP PARIBAS PL | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for separate taxable subscriptions |
| ODSETKI, INTEREST | EXCLUDE | Interest, out of scope |
| KREDYT, POŻYCZKA, LOAN | EXCLUDE | Loan principal, out of scope |

### 3.2 Polish government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| URZĄD SKARBOWY, US | EXCLUDE | Tax office payment |
| E-DEKLARACJE, E-URZAD SKARBOWY | EXCLUDE | Tax filing system |
| ZUS, ZAKŁAD UBEZPIECZEŃ SPOŁECZNYCH | EXCLUDE | Social security contributions |
| KRUS | EXCLUDE | Agricultural social security |
| GUS, GŁÓWNY URZĄD STATYSTYCZNY | EXCLUDE | Statistical office fee |
| KRS, SĄD REJONOWY | EXCLUDE | Court/registry fee |
| KSeF (payment to system) | EXCLUDE | E-invoicing system |

### 3.3 Polish utilities

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| PGE, PGE OBRÓT | Domestic 23% | K_40 (input) | Electricity — overhead |
| TAURON, ENEA, ENERGA | Domestic 23% | K_40 (input) | Regional energy suppliers |
| PGNiG, POLSKIE GÓRNICTWO NAFTOWE | Domestic 23% | K_40 (input) | Gas supply |
| ORANGE POLSKA, ORANGE PL | Domestic 23% | K_40 (input) | Telecoms — overhead |
| PLAY, P4 | Domestic 23% | K_40 (input) | Mobile telecoms |
| T-MOBILE PL, PLUS, POLKOMTEL | Domestic 23% | K_40 (input) | Mobile telecoms |
| NETIA, UPC POLSKA | Domestic 23% | K_40 (input) | Broadband/telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| PZU, WARTA, ERGO HESTIA | EXCLUDE | Insurance, exempt Art. 43 ust. 1 pkt 37 |
| ALLIANZ PL, AXA PL, GENERALI PL | EXCLUDE | Same |
| UBEZPIECZENIE, POLISA | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| POCZTA POLSKA | EXCLUDE for standard postage | | Universal postal service, exempt |
| POCZTA POLSKA | Domestic 23% for courier/Pocztex | K_40 | Non-universal services taxable |
| INPOST, PACZKOMAT | Domestic 23% | K_40 | Parcel lockers, taxable |
| DPD PL, DHL PL, GLS PL | Domestic 23% | K_40 | Courier, taxable |

### 3.6 Transport (Poland domestic)

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| PKP, PKP INTERCITY | Domestic 8% | K_40 | Passenger rail at 8% |
| POLREGIO, KOLEJE MAZOWIECKIE | Domestic 8% | K_40 | Regional rail at 8% |
| ZTM, MPK, KOMUNIKACJA MIEJSKA | Domestic 8% | K_40 | Urban public transport at 8% |
| LOT, RYANAIR, WIZZ AIR (international) | EXCLUDE / 0% | | International flights zero rated |
| TAXI, BOLT PL, UBER PL | Domestic 8% | K_40 | Taxi/ride-hailing at 8% (passenger transport) |

### 3.7 Food retail (blocked unless resale)

| Pattern | Treatment | Notes |
|---|---|---|
| BIEDRONKA, JERONIMO MARTINS | Default BLOCK input VAT | Supermarket — personal provisioning |
| LIDL PL, ALDI PL, KAUFLAND | Default BLOCK | Same |
| ŻABKA, LEWIATAN, STOKROTKA | Default BLOCK | Same |
| RESTAURANTS, CAFES, BARS | Default BLOCK | Representation — see note below |

**Note on Polish representation:** Poland allows VAT recovery on business entertainment (usługi gastronomiczne) — but ONLY on catering services (usługi cateringowe). Restaurant services (eaten on premises) are NOT deductible under Art. 88 ust. 1 pkt 4. Catering (delivered food for business meetings) IS deductible. Default: block. [T2] flag if client claims catering.

### 3.8 SaaS — EU suppliers (reverse charge, K_31/K_32/K_41)

| Pattern | Billing entity | Field | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | K_31/K_32/K_41 | EU service reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | K_31/K_32/K_41 | Reverse charge |
| ADOBE | Adobe Ireland (IE) | K_31/K_32/K_41 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | K_31/K_32/K_41 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland (IE) | K_31/K_32/K_41 | Reverse charge |
| SPOTIFY | Spotify AB (SE) | K_31/K_32/K_41 | EU reverse charge |
| DROPBOX | Dropbox Ireland (IE) | K_31/K_32/K_41 | Reverse charge |
| SLACK | Slack Ireland (IE) | K_31/K_32/K_41 | Reverse charge |
| ATLASSIAN | Atlassian BV (NL) | K_31/K_32/K_41 | EU reverse charge |
| ZOOM | Zoom Ireland (IE) | K_31/K_32/K_41 | Reverse charge |
| STRIPE (subscription) | Stripe IE | K_31/K_32/K_41 | Transaction fees may be exempt |

### 3.9 SaaS — non-EU suppliers (reverse charge, K_27/K_28)

| Pattern | Billing entity | Field | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | K_31/K_32/K_41 | LU entity → EU reverse charge |
| NOTION | Notion Labs Inc (US) | K_27/K_28 | Non-EU import of services |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | K_27/K_28 | Non-EU |
| OPENAI, CHATGPT | OpenAI Inc (US) | K_27/K_28 | Non-EU |
| GITHUB | GitHub Inc (US) | K_27/K_28 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | K_27/K_28 | Non-EU |
| CANVA | Canva Pty Ltd (AU) | K_27/K_28 | Non-EU |
| HUBSPOT | US or IE — check | K_27/K_28 or K_31/K_32 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | K_27/K_28 | Non-EU |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing exempt |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| PRZELEWY24, PAYU, TPAY | Check invoice | Polish payment processors — fees may be exempt financial services |
| BLIK (merchant fees) | Check invoice | Exempt financial service |

### 3.11 Professional services (Poland)

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| KANCELARIA, ADWOKAT, RADCA PRAWNY | Domestic 23% | K_40 | Legal — deductible if business. GTU_12 for sales. |
| BIURO RACHUNKOWE, KSIĘGOWY, BIEGŁY REWIDENT | Domestic 23% | K_40 | Accountant — always deductible. GTU_12 for sales. |
| NOTARIUSZ | Domestic 23% | K_40 | Notary |
| DORADCA PODATKOWY | Domestic 23% | K_40 | Tax adviser |

### 3.12 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ZUS, SKŁADKI ZUS | EXCLUDE | Social security contributions |
| WYNAGRODZENIE, PENSJA, PŁACA (outgoing) | EXCLUDE | Wages — outside VAT scope |
| PIT-4R, ZALICZKA PIT | EXCLUDE | Employee income tax withholding |
| PFRON | EXCLUDE | Disability fund contribution |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| CZYNSZ, NAJEM (commercial, with VAT) | Domestic 23% | Commercial lease with VAT |
| CZYNSZ, NAJEM (residential, no VAT) | EXCLUDE | Residential lease, exempt Art. 43 ust. 1 pkt 36 |
| WSPÓLNOTA MIESZKANIOWA, SPÓŁDZIELNIA | EXCLUDE | Housing cooperative fees |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| PRZELEW WŁASNY, TRANSFER WEWNĘTRZNY | EXCLUDE | Internal movement |
| DYWIDENDA | EXCLUDE | Dividend, out of scope |
| SPŁATA KREDYTU, RATA | EXCLUDE | Loan repayment, out of scope |
| WYPŁATA GOTÓWKI, BANKOMAT, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |

### 3.15 White list and split payment checks

| Pattern | Treatment | Notes |
|---|---|---|
| Any purchase invoice ≥ PLN 15,000 gross | WARN: verify white list + split payment | Art. 108a — mandatory MPP for Annex 15 items |
| Supplier bank account not on white list | WARN: input VAT at risk | Art. 96b — verify at https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Polish self-employed IT consultant.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; PLN 64.32`

**Reasoning:**
Notion Labs Inc is US entity (Section 3.9). Import of services under Art. 28b. Report net PLN 64.32 in K_27, output VAT (23% = PLN 14.79) in K_28, input VAT PLN 14.79 in K_42 (or K_40 depending on form version). Net effect zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field (output) | Field (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -64.32 | -64.32 | 14.79 | 23% | K_27/K_28 | K_42 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -3,800.00 ; PLN`

**Reasoning:**
Google Ireland (IE). EU service acquisition. Net PLN 3,800 in K_31, output VAT (23% = PLN 874) in K_32, input VAT PLN 874 in K_41.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field (output) | Field (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -3,800.00 | -3,800.00 | 874.00 | 23% | K_31/K_32 | K_41 | N | — | — |

### Example 3 — Restaurant service, blocked

**Input line:**
`15.04.2026 ; RESTAURACJA POD SAMSONEM ; DEBIT ; Client dinner ; -450.00 ; PLN`

**Reasoning:**
Restaurant service (usługa gastronomiczna) — input VAT blocked under Art. 88 ust. 1 pkt 4. This is NOT catering (which would be deductible). Default: block. No input VAT.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURACJA POD SAMSONEM | -450.00 | -450.00 | 0 | — | — | Y | Q1 | "Restaurant: blocked — catering (delivered) would be deductible, restaurant (on-premises) is not" |

### Example 4 — Domestic purchase, split payment threshold

**Input line:**
`18.04.2026 ; DELL POLSKA ; DEBIT ; Invoice FV/2026/04/41 Laptop ; -7,995.00 ; PLN`

**Reasoning:**
Domestic purchase from Polish vendor. PLN 7,995 incl. 23% VAT. Net = PLN 6,500. VAT = PLN 1,495. Below PLN 15,000 gross threshold for mandatory split payment. Electronics (laptop) may trigger GTU_06 if client resells electronics — for purchases, no GTU required. Input VAT deductible in K_40. Check: is the supplier on the white list? Verify at wykaz podatników.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DELL POLSKA | -7,995.00 | -6,500.00 | -1,495.00 | 23% | K_40 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice PL-2026-018 IT consultancy ; +16,500.00 ; PLN`

**Reasoning:**
Incoming from German company. B2B IT consulting — place of supply is Germany. Invoice at 0% with reverse charge note. Report net in K_19 (EU services supplied). GTU_12 applies (intangible/advisory services). Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +16,500.00 | +16,500.00 | 0 | 0% | K_19 | Y | Q2 (HIGH) | "Verify German USt-IdNr; GTU_12 applies" |

### Example 6 — Vehicle, 50% restriction

**Input line:**
`28.04.2026 ; TOYOTA LEASING POLSKA ; DEBIT ; Car lease May ; -2,200.00 ; PLN`

**Reasoning:**
Car lease payment. Passenger vehicles used for mixed purposes: 50% input VAT deduction under Art. 86a. PLN 2,200 incl. 23% VAT. Net = PLN 1,788.62. Full VAT = PLN 411.38. Deductible = 50% = PLN 205.69. Full 100% deduction requires: ewidencja przebiegu pojazdu (mileage log), VAT-26 form filed, and documented exclusive business use. Default: 50%.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | TOYOTA LEASING POLSKA | -2,200.00 | -1,788.62 | -205.69 | 23% (50%) | K_40 | Y | Q3 | "Vehicle 50% deduction — 100% requires mileage log + VAT-26 form" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 23% (Art. 41 ust. 1)

Default rate. Sales → K_10/K_11. Purchases → K_40.

### 5.2 Reduced rate 8% (Art. 41 ust. 2, Annex 3)

Food (certain categories), restaurant/catering services, passenger transport, construction/renovation of residential buildings (social housing). Sales → K_12/K_13.

### 5.3 Reduced rate 5% (Art. 41 ust. 2a, Annex 10)

Basic foodstuffs (bread, milk, meat, vegetables, fruit), books, periodicals, certain hygiene products. Sales → K_14/K_15.

### 5.4 Zero rate (Art. 41 ust. 4-11)

Exports → K_18. Intra-EU B2B goods (WDT) → K_17 (requires VIES-verified VAT number, transport proof). Intra-EU B2B services → K_19.

### 5.5 Exempt without credit (Art. 43)

Financial services (pkt 38-41), insurance (pkt 37), medical (pkt 18-19), education (pkt 26-29), residential rent (pkt 36), postal universal service. Excluded from JPK_V7 output boxes. If significant → **R-PL-4 refuses**.

### 5.6 Reverse charge — EU services (Art. 28b)

EU supplier invoices at 0%: net → K_31, output VAT → K_32, input VAT → K_41.

### 5.7 Reverse charge — EU goods (WNT, Art. 9)

Physical goods from EU: net → K_23, output VAT → K_24, input VAT → K_41.

### 5.8 Reverse charge — non-EU services (import usług, Art. 28b)

Services from outside EU: net → K_27, output VAT → K_28, input VAT → K_42.

### 5.9 Import of goods

Goods from non-EU: import VAT on customs declaration or via simplified procedure. Net → K_25, output VAT → K_26, input VAT → K_42.

### 5.10 Blocked input VAT (Art. 88)

- Restaurant services (usługi gastronomiczne) — fully blocked Art. 88 ust. 1 pkt 4. Catering (usługi cateringowe) IS deductible — important distinction.
- Accommodation services (usługi hotelowe) — blocked Art. 88 ust. 1 pkt 4. Exception: if resold or part of tourism package.
- Passenger vehicles: 50% default (Art. 86a); 100% requires mileage log + VAT-26 form.
- Fuel for 50%-deduction vehicles: 50% deductible.
- Private use: fully blocked.

### 5.11 Split payment mechanism (MPP, Art. 108a)

Mandatory for invoices ≥ PLN 15,000 gross covering goods/services in Annex 15 (electronics, steel, fuel, construction, etc.). Payment must be split: net to supplier's regular account, VAT to supplier's VAT account. Non-compliance risks: loss of input VAT deduction, 30% sanction, joint liability.

### 5.12 White list verification (Art. 96b)

For payments > PLN 15,000 to VAT-registered suppliers: verify supplier's bank account is on the white list (wykaz podatników VAT). Payment to an unlisted account → input VAT deduction denied unless notified to tax office within 7 days (ZAW-NR form).

### 5.13 GTU codes (ewidencja section)

Sales of specific goods/services must be tagged with GTU codes (GTU_01–GTU_13) in the JPK_V7 ewidencja. For IT consultants, GTU_12 (intangible services) is the most common. GTU codes do not appear on the deklaracja section — only in ewidencja.

### 5.14 Sales — cross-border B2C

EU consumers above €10,000 threshold → **R-EU-5 (OSS refusal)**. Below threshold → Polish VAT.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* Orlen, BP PL, Shell PL, Circle K PL. *Default:* 50% recovery (passenger car default). *Question:* "Is this a passenger car (50%) or commercial vehicle (100%)? Do you keep a mileage log and have VAT-26 filed?"

### 6.2 Restaurant vs catering

*Pattern:* any restaurant name. *Default:* block. *Question:* "Was this eaten on premises (restaurant — blocked) or delivered catering for a business meeting (deductible)?"

### 6.3 Ambiguous SaaS billing entities

*Default:* non-EU reverse charge K_27/K_28. *Question:* "Check invoice for legal entity name and country."

### 6.4 Round-number owner transfers

*Default:* exclude as owner injection. *Question:* "Customer payment, capital injection, or loan?"

### 6.5 Incoming from individuals

*Default:* domestic B2C at 23%, K_10/K_11. *Question:* "Sale? Country?"

### 6.6 Foreign counterparty incoming

*Default:* domestic 23%. *Question:* "B2B with VAT number or B2C? Country?"

### 6.7 Large purchases (split payment check)

*Pattern:* invoice ≥ PLN 15,000 gross. *Default:* verify Annex 15, white list, and MPP compliance. *Question:* "Was this paid via split payment? Is the supplier on the white list?"

### 6.8 Mixed-use phone/internet

*Default:* 0% if mixed. *Question:* "Dedicated business line or mixed? Business percentage?"

### 6.9 Outgoing to individuals

*Default:* exclude as drawings. *Question:* "Contractor with invoice, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Default:* no VAT (residential). *Question:* "Commercial? Does landlord charge VAT?"

### 6.12 Foreign hotel

*Default:* exclude from input VAT. *Question:* "Business trip?"

### 6.13 KSeF invoice verification

*Pattern:* any purchase invoice from a Polish supplier. *Default:* accept. *Question:* "Is this invoice available in KSeF? (If KSeF is mandatory for this supplier and the invoice is not in KSeF, input VAT may be at risk.)"

---

## Section 7 — Excel working paper template (Poland-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Poland-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("JPK field") accepts valid K_ codes from Section 1. Additional column M for GTU code (GTU_01–GTU_13, sales only). Additional column N for split payment flag (MPP: Y/N).

### Sheet "Box Summary"

```
Output:
| K_10 | Domestic sales 23% net | =SUMIFS(...) |
| K_11 | Output VAT 23% | =C[K_10]*0.23 |
| K_12 | Domestic sales 8% net | =SUMIFS(...) |
| K_13 | Output VAT 8% | =C[K_12]*0.08 |
| K_14 | Domestic sales 5% net | =SUMIFS(...) |
| K_15 | Output VAT 5% | =C[K_14]*0.05 |
| K_17 | EU goods supplies (WDT) net | =SUMIFS(...) |
| K_18 | Exports net | =SUMIFS(...) |
| K_19 | EU services supplies net | =SUMIFS(...) |
| K_23 | EU goods acquisitions (WNT) net | =SUMIFS(...) |
| K_24 | Output VAT WNT | =C[K_23]*0.23 |
| K_27 | Import of services net | =SUMIFS(...) |
| K_28 | Output VAT import of services | =C[K_27]*0.23 |
| K_31 | EU services acquisitions net | =SUMIFS(...) |
| K_32 | Output VAT EU services | =C[K_31]*0.23 |
| K_34 | Total output VAT | =SUM of output VAT fields |

Input:
| K_40 | Input VAT domestic | =SUMIFS(...) |
| K_41 | Input VAT EU acquisitions | =SUMIFS(...) |
| K_42 | Input VAT imports | =SUMIFS(...) |
| K_45 | Total input VAT | =K_40+K_41+K_42+K_43+K_44 |

Bottom line:
| K_46 | Excess input | =IF(K_45>K_34, K_45-K_34, 0) |
| K_47 | Excess output (VAT payable) | =IF(K_34>K_45, K_34-K_45, 0) |
| K_50 | VAT payable to urzad skarbowy | =K_47 adjusted for carry-forward |
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/poland-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Poland bank statement reading guide

**CSV format conventions.** PKO BP exports semicolons with DD.MM.YYYY dates. mBank uses comma-separated with ISO dates. ING PL uses semicolons. Common columns: Data operacji, Opis, Kwota, Saldo.

**Polish language variants.** Czynsz (rent), wynagrodzenie/pensja (salary), odsetki (interest), przelew (transfer), wypłata (withdrawal), wpłata (deposit), faktura (invoice). Treat as English equivalents.

**Internal transfers.** Labelled "przelew własny", "transfer wewnętrzny". Always exclude.

**Owner draws.** Jednoosobowa działalność gospodarcza (sole trader) transfers to personal account are drawings — exclude.

**Refunds.** Identify by "zwrot", "korekta", "nota korygująca". Book as negative in same field.

**Foreign currency.** Convert to PLN at NBP (National Bank of Poland) mid-rate on the business day preceding the transaction. Art. 31a ust. 1.

**IBAN prefix.** PL = Poland. DE, IE, LU, NL, FR = EU. US, GB, CH = non-EU.

**White list check.** For all domestic purchase invoices > PLN 15,000: verify supplier NIP and bank account at https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka before processing.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* JDG (jednoosobowa działalność gospodarcza) vs sp. z o.o. vs S.A. *Fallback:* "Are you JDG (sole trader), spółka z o.o., or other?"

### 9.2 VAT registration status
*Inference rule:* if asking for JPK_V7, they are czynny podatnik VAT. *Fallback:* "Are you czynny podatnik VAT (active) or zwolniony (exempt)?"

### 9.3 NIP
*Fallback:* "What is your NIP? (10 digits, PL prefix for EU VIES)"

### 9.4 Filing period
*Inference rule:* transaction dates. *Fallback:* "Monthly (JPK_V7M) or quarterly (JPK_V7K)? Which period?"

### 9.5 Industry
*Inference rule:* counterparty mix. *Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* ZUS, wynagrodzenie outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Fallback:* "Do you make VAT-exempt sales?" *If yes → R-PL-4 may fire.*

### 9.8 Credit brought forward
*Always ask:* "Do you have excess credit (nadwyżka) from the previous period? (K_49)"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Poland? EU or non-EU? B2B or B2C?"

### 9.10 Vehicle type and mileage log
*Fallback:* "Do you use a vehicle for business? Passenger car or commercial? Do you keep a mileage log (ewidencja przebiegu pojazdu) and have VAT-26 filed?"

---

## Section 10 — Reference material

### Validation status

v2.0, rewritten April 2026. Awaiting validation by doradca podatkowy in Poland.

### Sources

1. Ustawa o VAT (11 March 2004, as amended) — https://isap.sejm.gov.pl
2. Ordynacja podatkowa (Tax Ordinance)
3. Rozporządzenie w sprawie JPK_V7M/V7K
4. KAS guidance — https://www.podatki.gov.pl
5. White list — https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka
6. Council Directive 2006/112/EC — via eu-vat-directive companion skill
7. VIES — https://ec.europa.eu/taxation_customs/vies/
8. NBP exchange rates — https://www.nbp.pl

### Known gaps

1. KSeF mandatory e-invoicing timeline is evolving — verify current mandatory dates.
2. Split payment (MPP) Annex 15 list may be updated — verify annually.
3. Restaurant vs catering distinction is a common audit issue — the skill defaults to block.
4. Vehicle 50%/100% distinction requires supporting documentation that cannot be verified from bank data.
5. GTU codes cover sales only — a future version should add detailed GTU classification guidance.
6. White list verification is flagged but cannot be performed programmatically — reviewer must verify.

### Change log

- **v2.0 (April 2026):** Full rewrite to three-tier Accora architecture.
- **v1.0 (April 2026):** Initial draft. Standalone monolithic document.

### Self-check (v2.0)

1. Quick reference with JPK field table and conservative defaults: yes (Section 1).
2. Supplier library as lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue: yes (Section 6, 13 items).
6. Excel template with recalc: yes (Section 7).
7. Onboarding as fallback: yes (Section 9, 10 items).
8. All 8 Poland-specific refusals: yes (R-PL-1 through R-PL-8).
9. Reference material at bottom: yes (Section 10).
10. Three rates (23%/8%/5%) mapped to K_ fields: yes.
11. Restaurant vs catering distinction: yes (Section 3.7, Example 3, Section 5.10).
12. Split payment (MPP) and white list documented: yes (Sections 5.11-5.12, 3.15).
13. Vehicle 50% default documented: yes (Section 5.10, Example 6).
14. GTU codes listed: yes (Section 1, Section 5.13).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
