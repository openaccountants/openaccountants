---
name: sweden-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Swedish VAT return (momsdeklaration) for a self-employed individual or small business in Sweden. Trigger on phrases like "prepare VAT return", "do the Swedish VAT", "momsdeklaration", "moms", "skattedeklaration", or any request involving Swedish VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Sweden only and only standard-registered businesses. VAT groups, fiscal representatives, and flat-rate schemes are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Swedish VAT work.
version: 2.0
---

# Sweden VAT Return Skill (Momsdeklaration) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Sweden (Konungariket Sverige) |
| Standard rate | 25% |
| Reduced rates | 12% (food, restaurant/catering, hotel accommodation), 6% (books, newspapers, cultural events, passenger transport, sporting events) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods, prescribed medicines, certain medical aids) |
| Return form | Skattedeklaration / Momsdeklaration (ruta 05–49) |
| Filing portal | https://www.skatteverket.se (Mina sidor) |
| Authority | Skatteverket (Swedish Tax Agency) |
| Currency | SEK only |
| Filing frequencies | Monthly (turnover > SEK 40M); Quarterly (SEK 1M–40M); Annual (< SEK 1M) |
| Deadline | Monthly: 12th of second month after period (26th for Dec); Quarterly: 12th of second month after quarter; Annual: part of the income tax return |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants |
| Validated by | Pending — requires auktoriserad revisor validation |
| Validation date | Pending |

**Key momsdeklaration ruta (boxes):**

| Ruta | Meaning |
|---|---|
| 05 | Taxable sales excl. VAT (momspliktig försäljning) — total |
| 06 | Taxable sales excl. VAT at 25% |
| 07 | Taxable sales excl. VAT at 12% |
| 08 | Taxable sales excl. VAT at 6% |
| 10 | Output VAT at 25% |
| 11 | Output VAT at 12% |
| 12 | Output VAT at 6% |
| 20 | EU goods acquisitions excl. VAT (gemenskapsinternt förvärv) |
| 21 | EU services purchased excl. VAT (where buyer accounts for VAT) |
| 22 | Purchases of goods from outside EU excl. VAT |
| 23 | Purchases of services from outside EU excl. VAT |
| 24 | Domestic purchases where buyer accounts for VAT (construction reverse charge) |
| 30 | Output VAT on acquisitions (ruta 20–24) at 25% |
| 31 | Output VAT on acquisitions at 12% |
| 32 | Output VAT on acquisitions at 6% |
| 35 | EU supplies of goods excl. VAT (gemenskapsintern leverans) |
| 36 | EU supplies of services excl. VAT (where buyer accounts for VAT) |
| 37 | Exports excl. VAT |
| 38 | Intermediary acquisitions (mellanman) |
| 39 | Other supplies exempt or outside scope |
| 40 | Exempt turnover (momsfri omsättning) |
| 48 | Input VAT (ingående moms) — total deductible |
| 49 | Net VAT payable / refundable (derived: output − input) |

**Conservative defaults — Sweden-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 25% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Sweden |
| Unknown B2B vs B2C status for EU customer | B2C, charge 25% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (ruta 23/30) |
| Unknown blocked-input status (representation, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | SEK 30,000 |
| HIGH tax-delta on a single conservative default | SEK 2,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | SEK 50,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Swedish or international business bank: Handelsbanken, SEB, Swedbank, Nordea SE, Danske Bank SE, Länsförsäkringar, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially intra-EU B2B supplies and exports), purchase invoices for any input VAT claim above SEK 2,000, the client's organisationsnummer and momsregistreringsnummer.

**Ideal** — complete invoice register, prior period momsdeklaration, reconciliation of any carry-forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available → hard stop. If bank statement only → proceed but record in the reviewer brief: "This momsdeklaration was produced from bank statement alone. The reviewer must verify input VAT claims above SEK 2,000 are supported by compliant invoices and reverse-charge classifications match."

### Sweden-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13. If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-SE-1 — VAT group (mervärdesskattegrupp).** *Trigger:* client is part of a VAT group. *Message:* "VAT groups require consolidation across all group members. Out of scope."

**R-SE-2 — Fiscal representative.** *Trigger:* non-resident supplier with a fiscal representative in Sweden. *Message:* "Non-resident registrations with fiscal representatives have specific obligations beyond this skill."

**R-SE-3 — Partial exemption (proportionell avdragsrätt).** *Trigger:* client makes both taxable and exempt supplies (financial services, medical, education, residential rent) and exempt proportion is non-de-minimis. *Message:* "You make both taxable and exempt supplies. Input VAT must be apportioned under ML kapitel 13 §29-30. Please use an auktoriserad revisor to confirm the pro-rata rate."

**R-SE-4 — Flat-rate scheme (schablonavdrag).** *Trigger:* client uses a flat-rate deduction scheme (e.g. forestry/agriculture). *Message:* "Flat-rate schemes require sector-specific calculations beyond this skill."

**R-SE-5 — Real estate option to tax (frivillig skattskyldighet).** *Trigger:* client is a property owner transitioning into or out of the optional VAT registration for commercial property. *Message:* "Frivillig skattskyldighet transitions for real estate require complex capital goods scheme adjustments. Please use an auktoriserad revisor."

**R-SE-6 — Margin scheme (VMB vinstmarginalbeskattning).** *Trigger:* client deals in second-hand goods, art, antiques, or travel agent packages under the margin scheme. *Message:* "Margin scheme transactions require transaction-level margin computation. Out of scope."

**R-SE-7 — Income tax instead of moms.** *Trigger:* user asks about income tax return, not momsdeklaration. *Message:* "This skill handles momsdeklaration only. For Swedish income tax, use the appropriate income tax skill."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. Match by case-insensitive substring. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Swedish banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| HANDELSBANKEN, SHB | EXCLUDE for bank charges/fees | Financial service, exempt under ML kap 10 §33 |
| SEB, SKANDINAVISKA ENSKILDA | EXCLUDE for bank charges/fees | Same |
| SWEDBANK, SPARBANKEN | EXCLUDE for bank charges/fees | Same |
| NORDEA, NORDEA SE | EXCLUDE for bank charges/fees | Same |
| DANSKE BANK SE, LÄNSFÖRSÄKRINGAR BANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for fees | Check for separate taxable subscription invoices |
| RÄNTA, INTEREST | EXCLUDE | Interest income/expense, out of scope |
| LÅN, LOAN | EXCLUDE | Loan principal, out of scope |

### 3.2 Swedish government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SKATTEVERKET | EXCLUDE | Tax payment, not a supply |
| MOMS (as payment to Skatteverket) | EXCLUDE | VAT payment |
| TULLVERKET | EXCLUDE | Customs duty (but see import VAT on customs declaration) |
| BOLAGSVERKET | EXCLUDE | Company registry fees, sovereign acts |
| FÖRSÄKRINGSKASSAN | EXCLUDE | Social insurance payments |
| KRONOFOGDEMYNDIGHETEN | EXCLUDE | Enforcement authority |

### 3.3 Swedish utilities

| Pattern | Treatment | Ruta | Notes |
|---|---|---|---|
| VATTENFALL | Domestic 25% | 48 (input) | Electricity/gas — overhead |
| ELLEVIO, EON, FORTUM | Domestic 25% | 48 (input) | Regional electricity suppliers |
| TELIA, TELIA COMPANY | Domestic 25% | 48 (input) | Telecoms/broadband — overhead |
| TELENOR SE, TRE (3), COMVIQ | Domestic 25% | 48 (input) | Mobile telecoms |
| COMHEM, BREDBAND2 | Domestic 25% | 48 (input) | Broadband |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TRYGG-HANSA, IF, FOLKSAM | EXCLUDE | Insurance, exempt under ML kap 10 §35 |
| LÄNSFÖRSÄKRINGAR (insurance) | EXCLUDE | Same |
| FÖRSÄKRING, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Ruta | Notes |
|---|---|---|---|
| POSTNORD, POSTEN | EXCLUDE for standard postage | | Universal postal service, exempt |
| POSTNORD | Domestic 25% for parcel/courier | 48 | Non-universal services taxable |
| DHL, DB SCHENKER, BRING | Domestic 25% | 48 | Courier, taxable |

### 3.6 Transport (Sweden domestic)

| Pattern | Treatment | Ruta | Notes |
|---|---|---|---|
| SJ, SJ AB | Domestic 6% | 48 | Passenger rail at reduced rate |
| SL, SKÅNETRAFIKEN, VÄSTTRAFIK | Domestic 6% | 48 | Local/regional public transport at 6% |
| TAXI, TAXI STOCKHOLM, TAXI KURIR | Domestic 6% | 48 | Taxi at 6% (passenger transport) |
| SAS, NORWEGIAN, RYANAIR (international) | EXCLUDE / 0% | | International flights zero rated |
| SAS, NORWEGIAN (domestic) | Domestic 6% | 48 | Domestic flights at 6% |

### 3.7 Food retail and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| ICA, ICA MAXI, ICA KVANTUM | Default BLOCK input VAT | Supermarket — personal provisioning unless resale |
| COOP, COOP FORUM, STORA COOP | Default BLOCK input VAT | Same |
| HEMKÖP, WILLYS, LIDL SE | Default BLOCK input VAT | Same |
| RESTAURANTS, CAFES, BARS | Default BLOCK | Representation — limited deductibility |

**Note on Swedish representation (representationsavdrag):** Sweden allows VAT recovery on business entertainment up to a meal cost of SEK 300 per person excl. VAT (IL 16 kap. §2). The VAT on that amount is deductible. Above SEK 300/person, no additional VAT recovery. Alcohol is never deductible. Default: block fully. [T2] flag if client claims business entertainment with proper documentation.

### 3.8 SaaS — EU suppliers (reverse charge, ruta 21/30)

| Pattern | Billing entity | Ruta | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 21/30/48 | EU service reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 21/30/48 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 21/30/48 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 21/30/48 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 21/30/48 | Reverse charge |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) — DOMESTIC | 48 only | Swedish entity — domestic 25%, NOT reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 21/30/48 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 21/30/48 | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 21/30/48 | EU reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 21/30/48 | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | 21/30/48 | Transaction fees may be exempt — see 3.10 |

**Note on Spotify:** Spotify AB is a Swedish company. Purchases from Spotify are domestic Swedish transactions at 25%, NOT reverse charge. This is a common mistake.

### 3.9 SaaS — non-EU suppliers (reverse charge, ruta 23/30)

| Pattern | Billing entity | Ruta | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 21/30/48 | LU entity → EU reverse charge via ruta 21 |
| NOTION | Notion Labs Inc (US) | 23/30/48 | Non-EU service reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 23/30/48 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 23/30/48 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 23/30/48 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 23/30/48 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | 23/30/48 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or IE — check | 23/30/48 or 21/30/48 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 23/30/48 | Non-EU reverse charge |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU reverse charge ruta 21/30/48 | Stripe IE entity |
| KLARNA, SWISH (merchant fees) | Check invoice | Exempt financial service fees vs taxable platform fees |

### 3.11 Professional services (Sweden)

| Pattern | Treatment | Ruta | Notes |
|---|---|---|---|
| ADVOKAT, ADVOKATBYRÅ | Domestic 25% | 48 | Legal, deductible if business purpose |
| REVISOR, REVISIONSBOLAG, AUKTORISERAD | Domestic 25% | 48 | Accountant/auditor — always deductible |
| BOLAGSVERKET | EXCLUDE | Government fee, not a supply |

### 3.12 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ARBETSGIVARAVGIFTER, SOCIALA AVGIFTER | EXCLUDE | Employer contributions |
| LÖN, SALARY, WAGES (outgoing) | EXCLUDE | Wages — outside VAT scope |
| PRELIMINÄRSKATT, F-SKATT | EXCLUDE | Preliminary tax payment |
| A-KASSA, FACKFÖRBUND | EXCLUDE | Unemployment insurance, union fees |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| HYRA, LOKALHYRA (commercial, with VAT) | Domestic 25% | Commercial lease where landlord has frivillig skattskyldighet |
| HYRA (residential, no VAT) | EXCLUDE | Residential lease, exempt |
| BOSTADSRÄTT | EXCLUDE | Housing cooperative fees, exempt |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| ÖVERFÖRING, INTERN, EGET KONTO | EXCLUDE | Internal movement |
| UTDELNING, DIVIDEND | EXCLUDE | Dividend, out of scope |
| LÅN, AMORTERING | EXCLUDE | Loan repayment, out of scope |
| UTTAG, BANKOMAT, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Swedish self-employed IT consultant.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; SEK 166.88`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). Non-EU service — reverse charge. Report net SEK 166.88 in ruta 23, output VAT (25% = SEK 41.72) in ruta 30, and same SEK 41.72 as input VAT in ruta 48. Net effect zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ruta (output) | Ruta (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -166.88 | -166.88 | 41.72 | 25% | 23/30 | 48 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April ; -9,500.00 ; SEK`

**Reasoning:**
Google Ireland Limited (IE). EU service reverse charge. Net SEK 9,500 in ruta 21, output VAT (25% = SEK 2,375) in ruta 30, input VAT SEK 2,375 in ruta 48.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ruta (output) | Ruta (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -9,500.00 | -9,500.00 | 2,375.00 | 25% | 21/30 | 48 | N | — | — |

### Example 3 — Entertainment, limited deduction

**Input line:**
`15.04.2026 ; RESTAURANG OPERAKÄLLAREN ; DEBIT ; Client dinner 4 persons ; -4,800.00 ; SEK`

**Reasoning:**
Restaurant transaction. Business entertainment (representation) with 4 persons. Swedish rule: VAT deductible on meal cost up to SEK 300/person excl. VAT. Maximum deductible base = 4 x SEK 300 = SEK 1,200 excl. VAT. VAT on that = SEK 300. But documentation is required (business purpose, attendees, date). Default: block fully. [T2] flag.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ruta | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANG OPERAKÄLLAREN | -4,800.00 | -4,800.00 | 0 | — | — | Y | Q1 | "Representation: blocked — partial recovery possible up to SEK 300/person excl. VAT if documented" |

### Example 4 — Domestic purchase at reduced rate (passenger rail)

**Input line:**
`18.04.2026 ; SJ AB ; DEBIT ; Stockholm–Gothenburg return ; -1,200.00 ; SEK`

**Reasoning:**
SJ AB is the Swedish state railway. Domestic passenger transport is at 6% VAT. Net = SEK 1,200 / 1.06 = SEK 1,132.08. VAT = SEK 67.92. Input VAT deductible in ruta 48 if business travel.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ruta | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | SJ AB | -1,200.00 | -1,132.08 | -67.92 | 6% | 48 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice SE-2026-018 IT consultancy March ; +35,000.00 ; SEK`

**Reasoning:**
Incoming from a German company. B2B IT consulting services — place of supply is Germany. Invoice at 0%, German customer accounts for reverse charge. Report net in ruta 36 (EU services supplied). No output VAT. Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ruta | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +35,000.00 | +35,000.00 | 0 | 0% | 36 | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Vehicle, mixed-use passenger car

**Input line:**
`28.04.2026 ; VOLVO FINANS ; DEBIT ; Car lease May ; -5,500.00 ; SEK`

**Reasoning:**
Car lease payment. In Sweden, passenger cars used for mixed business/private purposes have limited VAT recovery. If the car is used exclusively for business (not available for private use), 100% recovery. For mixed use, recovery is restricted. Default: block fully. [T2] flag — reviewer must determine vehicle classification and business-use proportion.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ruta | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | VOLVO FINANS | -5,500.00 | -5,500.00 | 0 | — | — | Y | Q3 | "Vehicle: blocked — full recovery requires exclusive business use" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 25% (ML kap 9 §2)

Default rate for any taxable supply unless reduced rate, zero rate, or exemption applies. Sales → ruta 06 (net), ruta 10 (output VAT). Purchases → ruta 48 (input VAT).

### 5.2 Reduced rate 12% (ML kap 9 §3)

Applies to: food and non-alcoholic beverages, restaurant and catering services (excl. alcohol), hotel accommodation (from 2024). Sales → ruta 07 (net), ruta 11 (output VAT). Purchases → ruta 48 (input VAT at 12%).

### 5.3 Reduced rate 6% (ML kap 9 §4)

Applies to: books, newspapers, periodicals, cultural events (cinema, theatre, concerts), sporting events (spectator), domestic passenger transport (bus, rail, taxi, domestic flights). Sales → ruta 08 (net), ruta 12 (output VAT). Purchases → ruta 48 (input VAT at 6%).

### 5.4 Zero rate / exempt with credit

Exports → ruta 37 (net). Intra-EU B2B goods → ruta 35 (net, requires VIES-verified VAT number, transport proof). Intra-EU B2B services → ruta 36 (net). Prescribed medicines, certain medical aids → zero rated.

### 5.5 Exempt without credit (ML kap 10)

Medical/dental care, social services, education, financial services, insurance, postal universal service, residential rent. Excluded from the momsdeklaration. If significant → **R-SE-3 refuses**.

### 5.6 Local standard purchases

Input VAT at applicable rate from a Swedish supplier. Deductible in ruta 48. Subject to blocked-input rules (5.10).

### 5.7 Reverse charge — EU services received (ML kap 6 §33-34)

EU supplier invoices at 0%: net → ruta 21, output VAT → ruta 30 (at applicable rate, usually 25%), input VAT → ruta 48. Net cash effect zero.

### 5.8 Reverse charge — EU goods acquisitions

Physical goods from EU supplier: net → ruta 20, output VAT → ruta 30, input VAT → ruta 48.

### 5.9 Reverse charge — non-EU services (ML kap 6 §34)

Services from outside EU: net → ruta 23, output VAT → ruta 30, input VAT → ruta 48.

### 5.10 Blocked input VAT

- Entertainment/representation: VAT deductible only up to SEK 300/person excl. VAT on meals; alcohol never deductible (IL 16 kap §2)
- Passenger cars: mixed-use → restricted; exclusive business use → full deduction; requires evidence
- Private use: fully blocked
- Staff gifts above SEK 500 excl. VAT: blocked (trivial gifts up to SEK 500 deductible)
- Real property for residential use: blocked

### 5.11 Capital goods scheme (ML kap 15)

Capital goods with acquisition cost excl. VAT ≥ SEK 200,000 for movable property (machinery, equipment) are subject to 5-year adjustment. Immovable property (real estate): 10-year adjustment with threshold SEK 100,000 per cost item. Below thresholds: treat as normal overhead in ruta 48.

### 5.12 Construction reverse charge (ML kap 6 §34a)

Construction and building services between VAT-registered businesses in the construction sector: the buyer accounts for VAT. Net → ruta 24, output VAT → ruta 30, input VAT → ruta 48. [T2] — requires determining both parties are in construction.

### 5.13 Sales — local domestic

Charge 25%, 12%, or 6% as applicable. Map to ruta 06/07/08 (net) and ruta 10/11/12 (output VAT). Ruta 05 = total = sum of 06+07+08.

### 5.14 Sales — cross-border B2C

EU consumers above €10,000 threshold → **R-EU-5 (OSS refusal)**. Below threshold → Swedish VAT at applicable rate.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* OKQ8, Circle K, Preem, Shell SE, Ingo. *Default:* 0% recovery. *Question:* "Is this a passenger car for mixed use, or a commercial vehicle used exclusively for business?"

### 6.2 Restaurants and entertainment (representation)

*Pattern:* any restaurant, café, bar. *Default:* block. *Question:* "Was this business representation with documented purpose and attendees? How many persons? (VAT deductible up to SEK 300/person excl. VAT.)"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, etc. where legal entity not visible. *Default:* non-EU reverse charge ruta 23/30/48. *Question:* "Could you check the invoice for the legal entity name and country?"

### 6.4 Round-number incoming transfers from owner-named counterparties

*Default:* exclude as owner injection. *Question:* "Is this a customer payment, capital injection, or loan?"

### 6.5 Incoming transfers from individual names

*Default:* domestic B2C sale at 25%, ruta 06/10. *Question:* "Was this a sale? Country?"

### 6.6 Incoming transfers from foreign counterparties

*Default:* domestic 25%. *Question:* "B2B with VAT number, B2C, goods or services, which country?"

### 6.7 Large one-off purchases (capital goods threshold)

*Default:* if net ≥ SEK 200,000 → capital goods scheme; otherwise normal overhead. *Question:* "Confirm total invoice amount excluding VAT."

### 6.8 Mixed-use phone, internet, home office

*Pattern:* Telia, Telenor personal lines; home electricity. *Default:* 0% if mixed. *Question:* "Dedicated business line or mixed-use? Business percentage?"

### 6.9 Outgoing transfers to individuals

*Default:* exclude as drawings. *Question:* "Contractor with invoice, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Pattern:* UTTAG, BANKOMAT, ATM. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* HYRA, LOKALHYRA. *Default:* no VAT (residential). *Question:* "Commercial property? Does landlord charge moms (frivillig skattskyldighet)?"

### 6.12 Foreign hotel and accommodation

*Default:* exclude from input VAT. *Question:* "Was this a business trip?"

### 6.13 Construction services received

*Pattern:* byggtjänster, snickare, målare, VVS. *Default:* domestic 25% ruta 48. *Question:* "Are you in the construction sector? Is this a subcontractor?"

### 6.14 ROT/RUT deductions

*Pattern:* ROT-avdrag, RUT-avdrag on invoices. *Why insufficient:* ROT/RUT is an income tax deduction, not a VAT concept. The VAT on the full invoice is still applicable. *Default:* treat as normal domestic purchase at 25% for VAT. *Question:* "Confirm the total invoice amount including VAT (before ROT/RUT reduction)."

---

## Section 7 — Excel working paper template (Sweden-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Sweden-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Ruta code") accepts only valid momsdeklaration ruta codes from Section 1. For reverse-charge transactions, enter output ruta and input ruta separated by a slash (e.g. "21/30/48").

### Sheet "Box Summary"

```
Output:
| 05 | Total taxable sales excl. VAT | =C[06]+C[07]+C[08] |
| 06 | Sales 25% excl. VAT | =SUMIFS(Transactions!E:E, Transactions!H:H, "06") |
| 07 | Sales 12% excl. VAT | =SUMIFS(Transactions!E:E, Transactions!H:H, "07") |
| 08 | Sales 6% excl. VAT | =SUMIFS(Transactions!E:E, Transactions!H:H, "08") |
| 10 | Output VAT 25% | =C[06]*0.25 |
| 11 | Output VAT 12% | =C[07]*0.12 |
| 12 | Output VAT 6% | =C[08]*0.06 |

Acquisitions (reverse charge):
| 20 | EU goods acquisitions | =SUMIFS(...) |
| 21 | EU services acquisitions | =SUMIFS(...) |
| 22 | Non-EU goods acquisitions | =SUMIFS(...) |
| 23 | Non-EU services acquisitions | =SUMIFS(...) |
| 24 | Domestic reverse charge (construction) | =SUMIFS(...) |
| 30 | Output VAT on acquisitions 25% | =(C[20]+C[21]+C[22]+C[23]+C[24])*0.25 |
| 31 | Output VAT on acquisitions 12% | ... |
| 32 | Output VAT on acquisitions 6% | ... |

Exempt/zero-rated supplies:
| 35 | EU goods supplies | =SUMIFS(...) |
| 36 | EU services supplies | =SUMIFS(...) |
| 37 | Exports | =SUMIFS(...) |

Input:
| 48 | Total input VAT | =SUMIFS(Transactions!F:F, Transactions!H:H, "48") |
| 49 | Net VAT payable/refundable | =(C[10]+C[11]+C[12]+C[30]+C[31]+C[32])-C[48] |
```

### Sheet "Return Form"

```
Positive ruta 49 → payable to Skatteverket.
Negative ruta 49 → refund to the business.
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/sweden-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Sweden bank statement reading guide

**CSV format conventions.** Handelsbanken exports use semicolon delimiters with YYYY-MM-DD dates. SEB uses tab-separated. Swedbank typically semicolons. Common columns: Datum, Text, Belopp, Saldo.

**Swedish language variants.** Hyra (rent), lön (salary), ränta (interest), överföring (transfer), uttag (withdrawal), insättning (deposit). Treat as English equivalents.

**Internal transfers.** Own-account transfers labelled "överföring", "eget konto", "intern". Always exclude.

**Owner draws.** Enskild firma (sole trader) transfers to personal account are drawings — exclude.

**Refunds.** Identify by "återbetalning", "kreditnota", "retur". Book as negative in same ruta.

**Foreign currency.** Convert to SEK at transaction date rate. Use Riksbanken cross rates.

**IBAN prefix.** SE = Sweden. DK, FI, NO = Nordic (EU/EEA). IE, DE, FR = EU. US, GB, CH = non-EU.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* enskild firma (sole trader) vs AB (aktiebolag) vs HB (handelsbolag). *Fallback:* "Are you enskild firma, AB, HB, or other?"

### 9.2 VAT registration status
*Inference rule:* if asking for momsdeklaration, they are momsregistrerad. *Fallback:* "Are you momsregistrerad?"

### 9.3 Organisationsnummer and VAT number
*Fallback:* "What is your organisationsnummer and momsregistreringsnummer? (SE + 12 digits)"

### 9.4 Filing period
*Inference rule:* transaction dates. *Fallback:* "Monthly, quarterly, or annual filing? Which period?"

### 9.5 Industry
*Inference rule:* counterparty mix. *Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* arbetsgivaravgifter, lön outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Fallback:* "Do you make VAT-exempt sales?" *If yes → R-SE-3 may fire.*

### 9.8 Credit brought forward
*Always ask:* "Do you have any excess credit from the previous period?"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Sweden? EU or non-EU? B2B or B2C?"

### 9.10 Vehicle type
*Fallback:* "Do you use a vehicle for business? Passenger car or commercial vehicle? Mixed or exclusive business use?"

---

## Section 10 — Reference material

### Validation status

v2.0, rewritten April 2026. Awaiting validation by auktoriserad revisor or godkänd revisor in Sweden.

### Sources

1. Mervärdesskattelagen (ML) 2023:200 — https://www.riksdagen.se
2. Skatteförfarandelagen (SFL) 2011:1244
3. Inkomstskattelagen (IL) 1999:1229 (representation limits)
4. Skatteverket guidance — https://www.skatteverket.se
5. Council Directive 2006/112/EC — via eu-vat-directive companion skill
6. VIES — https://ec.europa.eu/taxation_customs/vies/
7. Riksbanken exchange rates

### Known gaps

1. Supplier pattern library does not cover every Swedish business.
2. Construction reverse charge (ruta 24) is Tier 2 — future version should add detailed rules.
3. ROT/RUT interaction is noted but not fully specified for VAT purposes.
4. Capital goods thresholds (SEK 200,000 movable / SEK 100,000 immovable) to be verified annually.
5. Representation limits (SEK 300/person) to be verified against current IL 16 kap.
6. Spotify domestic treatment must be verified — entity may change billing country.

### Change log

- **v2.0 (April 2026):** Full rewrite to three-tier Accora architecture.
- **v1.0 (April 2026):** Initial draft. Standalone monolithic document.

### Self-check (v2.0)

1. Quick reference with ruta table and conservative defaults: yes (Section 1).
2. Supplier library as lookup tables: yes (Section 3, 14 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue: yes (Section 6, 14 items).
6. Excel template with recalc: yes (Section 7).
7. Onboarding as fallback: yes (Section 9, 10 items).
8. All 7 Sweden-specific refusals: yes (Section 2, R-SE-1 through R-SE-7).
9. Reference material at bottom: yes (Section 10).
10. Three rates (25%/12%/6%) correctly mapped to ruta 06-08/10-12: yes.
11. Spotify domestic exception documented: yes (Section 3.8).
12. Representation limits (SEK 300/person) documented: yes.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
