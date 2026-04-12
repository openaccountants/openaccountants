---
name: ireland-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Irish VAT return (VAT3 form) for a self-employed individual or small business in Ireland. Trigger on phrases like "prepare VAT return", "do the VAT", "Irish VAT", "VAT3", "ROS return", "Revenue Online", or any request involving Ireland VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Ireland only and only standard VAT-registered businesses. VAT groups, Capital Goods Scheme adjustments, and complex property transactions are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Irish VAT work.
version: 2.0
---

# Ireland VAT Return Skill (VAT3) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Ireland (Eire) |
| Standard rate | 23% |
| Reduced rates | 13.5% (construction, repair, cleaning, short-term car hire, certain fuels), 9% (newspapers, e-publications, sporting facilities, hairdressing), 4.8% (livestock, greyhounds) |
| Zero rate | 0% (exports, most food, children's clothing/footwear, books, oral medicines, medical devices, passenger transport) |
| Second reduced rate | 0% items listed in Schedule 2 VATCA 2010 |
| Flat-rate (farmers) | 5.5% flat-rate addition (farmer scheme — not covered, R-IE-6) |
| Return form | VAT3 (4 boxes: T1, T2, T3, T4) |
| Annual return | RTD (Return of Trading Details — 6 categories, annual) |
| Filing portal | https://www.ros.ie (Revenue Online Service — ROS) |
| Authority | Revenue Commissioners (Revenue) |
| Currency | EUR only |
| Filing frequencies | Bi-monthly (standard — 6 periods per year); Quarterly (by Revenue agreement); Monthly (by election); Annual (small traders with Revenue approval) |
| Deadline | 23rd of month following bi-monthly period end (extended to 23rd for ROS e-filers) |
| Two-thirds rule | If ≥2/3 of supply value is materials/goods, entire supply taxed as goods (Section 41 VATCA 2010) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants |
| Validated by | Pending — requires Irish CPA/CTA validation |
| Validation date | Pending |

**Key VAT3 boxes:**

| Box | Meaning |
|---|---|
| T1 | VAT charged on supplies (output VAT) — total of VAT charged on all sales, plus VAT self-accounted on reverse charge |
| T2 | VAT on intra-EU acquisitions — VAT self-accounted on goods acquired from other EU member states |
| T3 | VAT on imports — VAT on goods imported from outside EU (postponed accounting or paid at customs) |
| T4 | Total deductible VAT (input VAT) — total VAT on purchases and reverse charge input |
| E1 | Total sales (incl. zero-rated, exempt) |
| E2 | Total intra-EU acquisitions |

**Note:** Ireland's VAT3 is extremely simple — only 4 VAT boxes plus 2 statistical boxes. All the detail goes into the annual RTD and the underlying records.

**Conservative defaults — Ireland-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 23% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Ireland |
| Unknown B2B vs B2C status for EU customer | B2C, charge 23% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown two-thirds rule applicability | Treat as services |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 5,000 |
| HIGH tax-delta on a single conservative default | EUR 300 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | EUR 8,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Acceptable from: AIB (Allied Irish Banks), Bank of Ireland, PTSB (Permanent TSB), Ulster Bank, KBC Ireland (legacy), Revolut Business, Wise Business, N26, or any other.

**Recommended** — sales invoices, purchase invoices for input VAT claims above EUR 300, VAT number (IE format), prior VAT3.

**Ideal** — complete invoice register, prior RTD, carry-forward reconciliation, cash basis election confirmation if applicable.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement → hard stop. If bank statement only → reviewer brief warning.

### Ireland-specific refusal catalogue

On top of EU-wide refusals in `eu-vat-directive` Section 13.

**R-IE-1 — VAT group.** *Trigger:* client is part of a VAT group. *Message:* "VAT groups require consolidated filing. Out of scope."

**R-IE-2 — Capital Goods Scheme (Section 64 VATCA 2010).** *Trigger:* client has capital goods with adjustment intervals (20 years for developed property, other intervals for refurbishment). *Message:* "Capital Goods Scheme adjustments are too complex for this skill. Please use a chartered accountant."

**R-IE-3 — Complex property transactions.** *Trigger:* client buys/sells/develops property where the joint option to tax, the two-thirds rule on property, or CGS applies. *Message:* "Property VAT in Ireland requires specialist advice. Out of scope."

**R-IE-4 — Partial exemption.** *Trigger:* client makes both taxable and exempt supplies, exempt proportion non-de-minimis. *Message:* "You make both taxable and exempt supplies. Input VAT must be apportioned under Section 60 VATCA 2010. Please use a chartered tax adviser."

**R-IE-5 — Margin scheme.** *Trigger:* second-hand goods, art, antiques. *Message:* "Margin scheme requires transaction-level margin computation. Out of scope."

**R-IE-6 — Flat-rate farmer scheme.** *Trigger:* client is a flat-rate farmer adding 5.5%. *Message:* "Flat-rate farmer scheme has special obligations. Out of scope."

**R-IE-7 — RCT (Relevant Contracts Tax) / construction reverse charge.** *Trigger:* client is a principal contractor or subcontractor in construction. *Message:* "RCT reverse charge in construction requires determining whether the contract is a 'relevant contract' under Section 530A TCA 1997. [T2] — flag for review with details of the construction contract."

**R-IE-8 — Income tax instead of VAT.** *Trigger:* user asks about income tax. *Message:* "This skill handles VAT3 only."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Irish banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| AIB, ALLIED IRISH BANKS | EXCLUDE | Financial service, exempt Schedule 1 VATCA 2010 |
| BANK OF IRELAND, BOI | EXCLUDE | Same |
| PTSB, PERMANENT TSB | EXCLUDE | Same |
| ULSTER BANK | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| INTEREST, UILC | EXCLUDE | Interest, out of scope |
| LOAN, MORTGAGE | EXCLUDE | Loan principal, out of scope |

### 3.2 Irish government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| REVENUE, REVENUE COMMISSIONERS | EXCLUDE | Tax payment |
| ROS PAYMENT | EXCLUDE | Revenue Online Service payment |
| CRO, COMPANIES REGISTRATION OFFICE | EXCLUDE | Registry fee, sovereign acts |
| PRSI, DEPT OF SOCIAL PROTECTION | EXCLUDE | Social insurance |
| LOCAL PROPERTY TAX, LPT | EXCLUDE | Property tax |
| COMMERCIAL RATES | EXCLUDE | Local authority rates, not a supply |

### 3.3 Irish utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| ESB, ELECTRIC IRELAND | Domestic 23% or 13.5% | T4 (input) | Electricity — domestic energy at 23% (may have been temporarily reduced) |
| BORD GÁIS, BORD GÁIS ENERGY | Domestic 23% or 13.5% | T4 (input) | Gas supply |
| SSE AIRTRICITY | Domestic 23% or 13.5% | T4 (input) | Electricity/gas |
| ENERGIA, PANDA POWER, FLOGAS | Domestic 23% or 13.5% | T4 (input) | Energy suppliers |
| EIR, EIRCOM | Domestic 23% | T4 (input) | Telecoms |
| THREE IRELAND, 3 IRELAND, THREE | Domestic 23% | T4 (input) | Mobile telecoms |
| VODAFONE IE | Domestic 23% | T4 (input) | Mobile telecoms |
| VIRGIN MEDIA IE, SKY IRELAND | Domestic 23% | T4 (input) | Broadband/TV |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FBD, ZURICH IE, AVIVA IE | EXCLUDE | Insurance exempt, Schedule 1 |
| AXA IRELAND, ALLIANZ IRELAND | EXCLUDE | Same |
| INSURANCE, ÁRACHAS | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| AN POST | EXCLUDE for standard postage | | Universal postal service, exempt |
| AN POST | Domestic 23% for parcel/courier | T4 | Non-universal services taxable |
| DPD IRELAND, FASTWAY, NIGHTLINE | Domestic 23% | T4 | Courier, taxable |

### 3.6 Transport (Ireland domestic)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| IRISH RAIL, IARNRÓD ÉIREANN | Zero-rated | T4 | Domestic passenger transport is ZERO-RATED in Ireland |
| DUBLIN BUS, BUS ÉIREANN, GO-AHEAD IRELAND | Zero-rated | T4 | Same — passenger transport 0% |
| LUAS, TRANSPORT FOR IRELAND | Zero-rated | T4 | Same |
| TAXI | Domestic 13.5% | T4 | Taxis at 13.5% |
| RYANAIR, AER LINGUS (international) | EXCLUDE / 0% | | International flights zero rated |
| RYANAIR, AER LINGUS (domestic) | Zero-rated | T4 | Domestic flights also 0% |

**Note on Irish transport:** Most passenger transport in Ireland is zero-rated (0%), not reduced-rate. This is unusual in the EU. Taxis are the exception at 13.5%.

### 3.7 Food retail and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| TESCO IE, TESCO IRELAND | Zero-rated for most food | Food is zero-rated in Ireland (Schedule 2 VATCA 2010) |
| SUPERVALU, DUNNES STORES, ALDI IE, LIDL IE | Zero-rated for most food | Same — but confectionery, ice cream, soft drinks are at 23% |
| CENTRA, SPAR IE | Zero-rated / 23% mixed | Split between zero-rated food and standard-rate items |
| RESTAURANTS, PUB FOOD, CAFES | Domestic 13.5% | Restaurant/catering services at 13.5% |

**Note on Irish entertainment/meals:** Ireland has no hard block on business entertainment VAT. If the meal is a genuine business expense, input VAT at 13.5% is deductible. However, Section 59 VATCA 2010 blocks VAT on entertainment of any kind that is not part of a taxable supply. Default: block for non-hospitality businesses. [T2] flag if client claims business purpose.

### 3.8 SaaS — EU suppliers (reverse charge, T1/T4)

Since many tech companies bill from Ireland, check whether the supplier is actually Irish (domestic) or billing from Ireland to an Irish customer (domestic, NOT reverse charge).

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) — DOMESTIC | T4 only | Irish entity billing Irish customer = DOMESTIC 23%. NOT reverse charge. |
| MICROSOFT (365, Azure) | Microsoft Ireland (IE) — DOMESTIC | T4 only | Same — domestic 23% |
| ADOBE | Adobe Ireland (IE) — DOMESTIC | T4 only | Same — domestic 23% |
| META, FACEBOOK ADS | Meta Platforms Ireland (IE) — DOMESTIC | T4 only | Same — domestic 23% |
| LINKEDIN (paid) | LinkedIn Ireland (IE) — DOMESTIC | T4 only | Same |
| SPOTIFY | Spotify AB (SE) | T1/T4 | EU reverse charge (SE entity, not IE) |
| DROPBOX | Dropbox Ireland (IE) — DOMESTIC | T4 only | Domestic |
| SLACK | Slack Ireland (IE) — DOMESTIC | T4 only | Domestic |
| ATLASSIAN | Atlassian BV (NL) | T1/T4 | EU reverse charge |
| ZOOM | Zoom Ireland (IE) — DOMESTIC | T4 only | Domestic |
| STRIPE (subscription) | Stripe Ireland (IE) — DOMESTIC | T4 only | Domestic. Transaction fees are exempt. |

**CRITICAL for Ireland:** Most major SaaS companies are billed from their IRISH entity. For an Irish customer, this means they are DOMESTIC supplies at 23%, NOT reverse charge. The invoice will show Irish VAT. Only non-IE EU entities (e.g. Spotify SE, Atlassian NL) trigger reverse charge. Verify the entity country on every invoice.

### 3.9 SaaS — non-EU suppliers (reverse charge, T1/T4)

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| NOTION | Notion Labs Inc (US) | T1/T4 | Non-EU reverse charge — self-account 23% |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | T1/T4 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | T1/T4 | Non-EU reverse charge |
| GITHUB | GitHub Inc (US) | T1/T4 | Check if billed by IE entity (then domestic) |
| FIGMA | Figma Inc (US) | T1/T4 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | T1/T4 | Non-EU reverse charge |
| HUBSPOT | HubSpot Ireland (IE) — likely DOMESTIC | T4 only | Check — may be billed from IE |
| TWILIO | Twilio Inc (US) or Twilio Ireland | Check | Could be domestic or non-EU |
| AWS | AWS EMEA SARL (LU) | T1/T4 | EU reverse charge (LU entity) |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing exempt — Stripe IE entity |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| SUMUP IE, SQUARE IE | Check invoice | Irish entity: fees may be exempt financial services |

### 3.11 Professional services (Ireland)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| SOLICITOR, & CO SOLICITORS | Domestic 23% | T4 | Legal — deductible if business |
| ACCOUNTANT, & ASSOCIATES, CPA, ACCA | Domestic 23% | T4 | Accountant — always deductible |
| CRO, COMPANIES REGISTRATION OFFICE | EXCLUDE | Registry fee |

### 3.12 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| PRSI, EMPLOYER PRSI | EXCLUDE | Social insurance |
| PAYE, PSWT | EXCLUDE | Payroll tax |
| SALARY, WAGES (outgoing) | EXCLUDE | Wages — outside VAT scope |
| USC | EXCLUDE | Universal Social Charge |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENT (commercial, with VAT) | Domestic 23% | Commercial lease where landlord opted to charge VAT |
| RENT (residential, no VAT) | EXCLUDE | Residential lease, exempt Schedule 1 |
| COMMERCIAL RATES | EXCLUDE | Local authority, not a supply |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER, INTERNAL, OWN ACCOUNT | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Out of scope |
| LOAN REPAYMENT | EXCLUDE | Loan principal |
| ATM, CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Irish self-employed IT consultant.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
US entity. Non-EU service — self-account VAT at 23%. Add EUR 3.38 (23% of EUR 14.68) to T1 (output VAT) and the same EUR 3.38 to T4 (input VAT). Net effect zero for fully taxable business.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (output) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.38 | 23% | T1 | T4 | N | — | — |

### Example 2 — Domestic purchase from Irish-based SaaS (Google)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April ; -1,045.50 ; EUR`

**Reasoning:**
Google Ireland Ltd is an IRISH entity billing an IRISH customer. This is a DOMESTIC purchase at 23%. The invoice will include Irish VAT. EUR 1,045.50 incl. 23% VAT. Net = EUR 850. VAT = EUR 195.50. Input VAT goes to T4. No reverse charge — this is NOT a cross-border transaction.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -1,045.50 | -850.00 | -195.50 | 23% | T4 | N | — | — |

### Example 3 — Entertainment, blocked by default

**Input line:**
`15.04.2026 ; CHAPTER ONE RESTAURANT ; DEBIT ; Client dinner ; -280.00 ; EUR`

**Reasoning:**
Restaurant. Section 59 VATCA 2010 blocks input VAT on entertainment unless it forms part of a taxable supply. For an IT consultant, client entertainment is blocked. Default: block. [T2] flag.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | CHAPTER ONE RESTAURANT | -280.00 | -280.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked under Section 59 — recovery only if part of taxable supply" |

### Example 4 — Zero-rated food purchase (for hospitality business)

**Input line:**
`18.04.2026 ; MUSGRAVES WHOLESALE ; DEBIT ; Food supplies invoice ; -2,400.00 ; EUR`

**Reasoning:**
Musgraves is a wholesale food distributor. Most food in Ireland is zero-rated (Schedule 2 VATCA 2010). If the client is in hospitality/catering, this is stock for resale and is zero-rated on purchase. VAT = EUR 0. But the purchase still goes into the records for the RTD. If the client is NOT in food business, this is personal provisioning — block.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | MUSGRAVES WHOLESALE | -2,400.00 | -2,400.00 | 0 | 0% | T4 | Y | Q2 | "Wholesale food — zero-rated. Is this for business (hospitality/resale) or personal?" |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice IE-2026-018 IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
Incoming from German company. B2B IT consulting — place of supply is Germany. Invoice at 0%, customer accounts for reverse charge. Report net in E1 (total sales) and underlying records. No output VAT in T1. Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | E1 (no T1) | Y | Q3 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, blocked (Section 59)

**Input line:**
`28.04.2026 ; BMW FINANCIAL SERVICES IE ; DEBIT ; Car lease May ; -650.00 ; EUR`

**Reasoning:**
Car lease. Section 59 VATCA 2010 blocks input VAT on motor vehicles (purchase, hire, or lease) unless the vehicle is stock-in-trade or qualifying for a short-term hire business. An IT consultant cannot recover VAT on car leases. Hard block. Exception: commercial vehicles (vans, trucks) used solely for business ARE deductible.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | BMW FINANCIAL SERVICES IE | -650.00 | -650.00 | 0 | — | — | Y | Q4 | "Motor vehicle: blocked under Section 59 — exception for commercial vehicles and stock-in-trade only" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 23% (Section 46(1)(a) VATCA 2010)

Default rate. Sales → T1 (output VAT). Purchases → T4 (input VAT).

### 5.2 Reduced rate 13.5% (Section 46(1)(c))

Construction, repair and maintenance of buildings, cleaning services, short-term car hire, restaurant/catering, waste collection, certain fuels (coal, peat, gas for residential). Sales → T1. Purchases → T4 (input VAT at 13.5%).

### 5.3 Second reduced rate 9% (Section 46(1)(ca))

Newspapers, electronic publications, sporting facilities, hairdressing, printed and digital periodicals.

### 5.4 Reduced rate 4.8% (Section 46(1)(cb))

Livestock (cattle, sheep), greyhounds. Very niche — unlikely for IT consultants.

### 5.5 Zero rate (Section 46(1)(b), Schedule 2)

Exports, most food and drink (but NOT alcohol, confectionery, soft drinks, restaurant meals, hot takeaway), children's clothing and footwear, books, oral medicines, medical aids and appliances, fertilisers, seeds, animal feeding stuffs, electricity (domestic — temporarily zero-rated), passenger transport.

### 5.6 Exempt without credit (Schedule 1)

Financial services, insurance, medical services, education, postal universal service, residential rent, certain sporting and cultural services. If significant → **R-IE-4 refuses**.

### 5.7 Reverse charge — EU services and goods

Self-account VAT at 23% on services received from EU suppliers (non-IE). Add to T1 and T4. For EU goods: add to T2 and T4. E2 captures EU acquisitions value.

### 5.8 Reverse charge — non-EU services

Self-account 23% on services from outside EU. Add to T1 and T4.

### 5.9 Import VAT (T3)

Goods from non-EU: import VAT at point of entry or via postponed accounting (if approved). Report in T3 (output) and T4 (input if deductible).

### 5.10 Blocked input VAT (Section 59 VATCA 2010)

- Motor vehicles: purchase, hire, lease of motor cars — hard block. Exception: stock-in-trade, short-term hire business, driving school.
- Petrol: fully blocked. Diesel for commercial vehicles: deductible.
- Entertainment: blocked unless part of a taxable supply.
- Food and drink: personal consumption blocked.
- Accommodation: blocked unless in the course of a taxable supply.

### 5.11 Two-thirds rule (Section 41)

If a composite supply consists of ≥2/3 goods (by value), the entire supply is taxed at the goods rate. If ≥2/3 services, entire supply at services rate. [T2] — requires analysis of the supply composition.

### 5.12 Cash basis (Moneys Received basis)

If turnover < EUR 2 million and approved by Revenue, VAT on sales can be accounted for when payment is received rather than when invoiced. Purchases are still accounted on invoice basis. [T2] — confirm with client.

### 5.13 RTD (Return of Trading Details)

Annual return with 6 categories: (1) goods at standard rate, (2) goods at reduced/zero rate, (3) services at standard rate, (4) services at reduced/zero rate, (5) exempt supplies, (6) non-deductible purchases. Not due with every VAT3 but must be prepared at year end.

### 5.14 Sales — cross-border B2C

EU consumers above €10,000 threshold → **R-EU-5 (OSS refusal)**. Below threshold → Irish VAT.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* Topaz, Circle K IE, Applegreen, Maxol. *Default:* block (petrol always blocked; diesel for commercial vehicles only). *Question:* "Is this petrol (blocked) or diesel for a commercial vehicle?"

### 6.2 Entertainment

*Pattern:* restaurant, pub, hotel meal. *Default:* block under Section 59. *Question:* "Is this entertainment part of a taxable supply? (If not, VAT is blocked.)"

### 6.3 Ambiguous SaaS billing entities

*Default:* check if IE entity (then domestic 23%, not reverse charge). *Question:* "Check invoice — is this billed from an Irish entity or foreign?"

### 6.4 Round-number owner transfers

*Default:* exclude as owner injection. *Question:* "Customer payment, capital, or loan?"

### 6.5 Incoming from individuals

*Default:* domestic sale — determine rate based on goods/services. *Question:* "Was this a sale? What was supplied?"

### 6.6 Foreign counterparty incoming

*Default:* check if EU B2B or B2C. *Question:* "B2B with VAT number or B2C? Country?"

### 6.7 Large one-off purchases

*Default:* normal input VAT in T4. *Question:* "Confirm invoice amount and what was purchased."

### 6.8 Mixed-use phone/internet

*Pattern:* Eir, Three, Vodafone personal lines. *Default:* 0% if mixed. *Question:* "Dedicated business line? Business percentage?"

### 6.9 Outgoing to individuals

*Default:* exclude as drawings. *Question:* "Contractor, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Default:* exclude. *Question:* "What was cash used for?"

### 6.11 Rent payments

*Default:* no VAT (residential). *Question:* "Commercial property? Does landlord charge VAT?"

### 6.12 Foreign hotel

*Default:* exclude from input VAT. *Question:* "Business trip?"

### 6.13 Construction services (RCT)

*Pattern:* builder, contractor, plumber, electrician. *Default:* domestic 13.5% in T4. *Question:* "Are you a principal contractor? Is this a relevant contract under RCT?" *If yes → R-IE-7 fires.*

### 6.14 Two-thirds rule composite supplies

*Pattern:* single invoice combining goods and services. *Default:* treat as services at applicable rate. *Question:* "What proportion of this supply is goods vs services?"

---

## Section 7 — Excel working paper template (Ireland-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Ireland-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("VAT3 box") accepts: T1, T2, T3, T4, E1, E2. For reverse charge, enter "T1/T4" (both output and input). Column M for RTD category (1–6, for annual RTD preparation).

### Sheet "Box Summary"

Ireland's VAT3 is very simple:

```
| T1 | Output VAT (incl. reverse charge output) | =SUMIFS(Transactions!F:F, ..., "T1") |
| T2 | VAT on intra-EU acquisitions | =SUMIFS(Transactions!F:F, ..., "T2") |
| T3 | VAT on imports | =SUMIFS(Transactions!F:F, ..., "T3") |
| T4 | Deductible input VAT | =SUMIFS(Transactions!F:F, ..., "T4") |
| NET | VAT payable / refundable | =C[T1]+C[T2]+C[T3]-C[T4] |
| E1 | Total sales value | =SUMIFS(Transactions!E:E, ..., sales rows) |
| E2 | EU acquisitions value | =SUMIFS(Transactions!E:E, ..., EU acq rows) |
```

### Sheet "Return Form"

```
Positive NET → payable to Revenue.
Negative NET → refund from Revenue.
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/ireland-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Ireland bank statement reading guide

**CSV format conventions.** AIB exports use comma-separated with DD/MM/YYYY dates. Bank of Ireland uses similar format. PTSB may use semicolons. Common columns: Date, Description, Debit, Credit, Balance.

**Irish language variants.** Most descriptions are in English. Occasional Irish: cíos (rent), tuarastal (salary), ús (interest). Treat as English equivalents.

**Internal transfers.** Labelled "transfer", "own account", "internal". Always exclude.

**Owner draws.** Sole trader transfers to personal account are drawings — exclude.

**Refunds.** Identify by "refund", "credit note", "reversal". Book as negative.

**Currency.** EUR only for domestic. Foreign currency → convert at ECB rate.

**IBAN prefix.** IE = Ireland. GB = UK (non-EU post-Brexit). DE, FR, NL = EU. US, AU, CH = non-EU.

**Important post-Brexit note:** UK (GB) is non-EU. Supplies to/from UK are treated as non-EU (imports/exports), NOT intra-EU. Northern Ireland has special protocol for goods.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* sole trader vs Ltd vs DAC vs LLP. *Fallback:* "Are you a sole trader, company limited by shares (Ltd), DAC, or partnership?"

### 9.2 VAT registration status and basis
*Fallback:* "Invoice basis or Moneys Received (cash) basis?"

### 9.3 VAT number
*Fallback:* "What is your VAT number? (IE + 7 digits + 1-2 letters)"

### 9.4 Filing period
*Fallback:* "Bi-monthly, quarterly, monthly, or annual? Which period?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* PRSI, PAYE, salary outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Fallback:* "Do you make VAT-exempt sales?" *If yes → R-IE-4 may fire.*

### 9.8 Credit brought forward
*Always ask:* "Excess credit from previous period?"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Ireland? EU or non-EU? B2B or B2C?"

### 9.10 Property / construction
*Fallback:* "Do you deal in property or construction?" *If yes → R-IE-2/R-IE-3/R-IE-7 may fire.*

---

## Section 10 — Reference material

### Validation status

v2.0, rewritten April 2026. Awaiting validation by Irish chartered accountant or chartered tax adviser.

### Sources

1. VATCA 2010 (Value-Added Tax Consolidation Act 2010) — https://www.irishstatutebook.ie
2. Revenue guidance — https://www.revenue.ie
3. ROS — https://www.ros.ie
4. Council Directive 2006/112/EC — via eu-vat-directive companion skill
5. VIES — https://ec.europa.eu/taxation_customs/vies/
6. ECB exchange rates

### Known gaps

1. The SaaS pattern library is critical for Ireland — most major tech companies bill from IE entities, making them domestic rather than reverse charge. Verify each supplier.
2. Capital Goods Scheme (Section 64) is entirely excluded.
3. Two-thirds rule (Section 41) is flagged as Tier 2 but not fully worked.
4. Northern Ireland Protocol for goods is not fully addressed.
5. Cash basis eligibility and mechanics are noted but not detailed.
6. Energy VAT rates may have temporary changes — verify current rates.

### Change log

- **v2.0 (April 2026):** Full rewrite to three-tier Accora architecture.
- **v1.0 (April 2026):** Initial draft. Standalone document.

### Self-check (v2.0)

1. Quick reference with VAT3 box table and conservative defaults: yes (Section 1).
2. Supplier library with Irish patterns: yes (Section 3, 14 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue: yes (Section 6, 14 items).
6. Excel template with recalc: yes (Section 7).
7. Onboarding as fallback: yes (Section 9, 10 items).
8. All 8 Ireland-specific refusals: yes (R-IE-1 through R-IE-8).
9. Reference material at bottom: yes (Section 10).
10. Multiple rates (23%/13.5%/9%/4.8%/0%) documented: yes.
11. Irish SaaS domestic exception (IE entities = domestic, NOT reverse charge): yes (Section 3.8, Example 2).
12. Motor vehicle hard block (Section 59): yes (Section 5.10, Example 6).
13. Zero-rated food documented: yes (Section 5.5).
14. Passenger transport zero-rated: yes (Section 3.6).
