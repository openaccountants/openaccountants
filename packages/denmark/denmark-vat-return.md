---
name: denmark-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Danish VAT return (Momsangivelse) for a self-employed individual or small business in Denmark. Trigger on phrases like "prepare VAT return", "do the VAT", "Danish VAT", "moms", "momsangivelse", or any request involving Denmark VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Denmark only and only standard-registered businesses. Loensumsafgift-only entities, VAT groups, and fiscal representatives are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Danish VAT work.
version: 2.0
---

# Denmark VAT Return Skill (Momsangivelse) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Denmark (Kongeriget Danmark) |
| Standard rate | 25% |
| Reduced rates | **None — Denmark is unique in the EU: no reduced rates** |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods, newspapers/periodicals from 2024, international transport) |
| Return form | Momsangivelse (rubrik 1–9) |
| Filing portal | https://skat.dk (TastSelv Erhverv) |
| Authority | Skattestyrelsen (Danish Tax Agency) |
| Currency | DKK only |
| Filing frequencies | Quarterly (turnover DKK 1–5M); Half-yearly (turnover < DKK 1M); Monthly (turnover > DKK 5M) |
| Deadline | Monthly/quarterly: 25th of month following period end; Half-yearly: 1 March / 1 September |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants |
| Validated by | Pending — requires statsautoriseret revisor validation |
| Validation date | Pending |

**CRITICAL: Denmark has NO reduced VAT rates.** Every taxable supply is at 25%. There is no 5%, 7%, 12%, or 13% rate. Any suggestion of a reduced rate is wrong.

**Key Momsangivelse rubrik (boxes):**

| Rubrik | Meaning |
|---|---|
| 1 | Output VAT (udgående moms) — total VAT charged on sales |
| 2 | VAT on EU acquisitions of goods (EU-varekøb) |
| 3 | VAT on services purchased abroad with reverse charge (ydelser købt i udlandet med omvendt betalingspligt) |
| 4 | Input VAT (indgående moms) — total deductible VAT on purchases |
| 5 | Derived: VAT payable / refundable (rubrik 1 + 2 + 3 − 4) |
| 6 | Sales excl. VAT (momspligtig omsætning) — value of taxable supplies |
| 7 | EU supplies of goods and services excl. VAT (EU-varesalg og ydelser) |
| 8 | Exports excl. VAT (eksport) |
| 9 | EU acquisitions of goods excl. VAT (EU-varekøb uden moms) |

**Conservative defaults — Denmark-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 25% (only rate available) |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Denmark |
| Unknown B2B vs B2C status for EU customer | B2C, charge 25% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (rubrik 3/4) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | DKK 25,000 |
| HIGH tax-delta on a single conservative default | DKK 1,500 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | DKK 40,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Danish or international business bank: Danske Bank, Nordea DK, Jyske Bank, Sydbank, Spar Nord, Arbejdernes Landsbank, Nykredit, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for intra-EU B2B supplies and exports), purchase invoices for any input VAT claim above DKK 1,500, the client's CVR/SE number and momsregistreringsnummer.

**Ideal** — complete invoice register, prior period momsangivelse, reconciliation of any carry-forward credit.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all → hard stop. If bank statement only without invoices → proceed but record in the reviewer brief: "This momsangivelse was produced from bank statement alone. The reviewer must verify, before approval, that input VAT claims above DKK 1,500 are supported by compliant tax invoices and that all reverse-charge classifications match the supplier's invoice."

### Denmark-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-DK-1 — Lønsumsafgift-only entity.** *Trigger:* client is not VAT-registered but subject to payroll tax on exempt activities. *Message:* "Lønsumsafgift (payroll tax on exempt activities) is a separate tax from moms. This skill covers momsangivelse only. Please consult a statsautoriseret revisor for lønsumsafgift obligations."

**R-DK-2 — VAT group (fællesregistrering).** *Trigger:* client is part of a VAT group under momsloven §47(4). *Message:* "VAT groups under fællesregistrering require consolidation across all group members. Out of scope for this skill."

**R-DK-3 — Fiscal representative.** *Trigger:* non-resident supplier with a fiscal representative in Denmark. *Message:* "Non-resident registrations with fiscal representatives have specific obligations beyond this skill. Please use a statsautoriseret revisor."

**R-DK-4 — Construction reverse charge (§46(1) nr. 3).** *Trigger:* client is a construction subcontractor where the reverse charge under §46(1) nr. 3 applies. *Message:* "Construction reverse charge under momsloven §46(1) nr. 3 requires transaction-level analysis of whether the customer is a registered builder. This is Tier 2 — flag for reviewer with specific construction details."

**R-DK-5 — Partial exemption (pro-rata).** *Trigger:* client makes both taxable and exempt-without-credit supplies and the exempt proportion is non-de-minimis. *Message:* "You make both taxable and exempt supplies. Input VAT must be apportioned under momsloven §38. Please use a statsautoriseret revisor to determine and confirm the pro-rata rate."

**R-DK-6 — Income tax return instead of moms.** *Trigger:* user asks about annual income tax return, not the momsangivelse. *Message:* "This skill only handles the momsangivelse. For Danish income tax, use the appropriate income tax skill."

**R-DK-7 — Used goods margin scheme (brugtmoms).** *Trigger:* client deals in second-hand goods under the brugtmoms scheme. *Message:* "Margin scheme (brugtmoms) transactions require transaction-level margin computation. Out of scope."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules — the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Danish banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DANSKE BANK | EXCLUDE for bank charges/fees | Financial service, exempt under momsloven §13(1) nr. 11 |
| NORDEA, NORDEA DK | EXCLUDE for bank charges/fees | Same |
| JYSKE BANK | EXCLUDE for bank charges/fees | Same |
| SYDBANK | EXCLUDE for bank charges/fees | Same |
| SPAR NORD, ARBEJDERNES LANDSBANK | EXCLUDE for bank charges/fees | Same |
| NYKREDIT | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| RENTE, INTEREST | EXCLUDE | Interest income/expense, out of scope |
| LÅN, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Danish government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SKAT, SKATTESTYRELSEN | EXCLUDE | Tax payment, not a supply |
| MOMS (as payment to Skat) | EXCLUDE | VAT payment to authority |
| TOLD, TOLDSTYRELSEN | EXCLUDE | Customs duty (but see import VAT on customs declaration) |
| ERHVERVSSTYRELSEN | EXCLUDE | Business registry fees, sovereign acts |
| KOMMUNESKAT, KOMMUNE | EXCLUDE | Municipal tax, not a supply |
| ARBEJDSMARKEDETS TILLÆGSPENSION, ATP | EXCLUDE | Statutory pension contribution |

### 3.3 Danish utilities

| Pattern | Treatment | Rubrik | Notes |
|---|---|---|---|
| ØRSTED, DONG ENERGY | Domestic 25% | 4 (input) | Electricity/gas — overhead |
| NORLYS, ANDEL ENERGI, EWII | Domestic 25% | 4 (input) | Regional energy suppliers |
| TDC, NUUDAY, YOUSEE | Domestic 25% | 4 (input) | Telecoms/broadband — overhead |
| TELIA DK, TELENOR DK, 3 (HI3G) | Domestic 25% | 4 (input) | Mobile telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TRYG, TOPDANMARK, CODAN | EXCLUDE | Insurance, exempt under §13(1) nr. 10 |
| ALKA, GF FORSIKRING, GJENSIDIGE | EXCLUDE | Same |
| FORSIKRING, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Rubrik | Notes |
|---|---|---|---|
| POSTNORD, POST DANMARK | EXCLUDE for standard postage | Universal postal service, exempt |
| POSTNORD | Domestic 25% for parcel/courier services | 4 (input) | Non-universal services are taxable |
| GLS, DAO, BRING | Domestic 25% | 4 (input) | Courier, taxable |
| DHL EXPRESS, TNT, FEDEX | Domestic 25% or EU reverse charge | 4 or 3/4 | Check invoice — billing entity |

### 3.6 Transport (Denmark domestic)

| Pattern | Treatment | Rubrik | Notes |
|---|---|---|---|
| DSB | Domestic 25% | 4 (input) | Domestic rail, taxable (no reduced rate in DK) |
| REJSEKORT | Domestic 25% | 4 (input) | Public transport card top-up |
| MOVIA, MIDTTRAFIK, NORDJYLLANDS TRAFIKSELSKAB | Domestic 25% | 4 (input) | Regional transport |
| SAS, NORWEGIAN, RYANAIR (international) | EXCLUDE / 0% | | International flights zero rated |
| TAXI, TAXA, DANTAXI, 4X35 | Domestic 25% | 4 (input) | Local taxi |

### 3.7 Food retail and entertainment (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| NETTO, FØTEX, BILKA, FAKTA | Default BLOCK input VAT | Supermarket — personal provisioning. Only deductible if resale. |
| REMA 1000, ALDI DK, LIDL DK | Default BLOCK input VAT | Same |
| IRMA, MENY, SALLING | Default BLOCK input VAT | Same |
| RESTAURANTS, CAFES, BARS | Default BLOCK | Entertainment/representation — limited deductibility (25% of VAT on business entertainment per momsloven §42(2)) |

**Note on Danish representation (repræsentation):** Unlike Malta's hard block, Denmark allows 25% recovery of VAT on business entertainment (restauration) under momsloven §42(2). However, this requires proper documentation (business purpose, attendees). Default: block fully. [T2] flag if client claims business entertainment — reviewer must verify documentation meets §42(2).

### 3.8 SaaS — EU suppliers (reverse charge, rubrik 3/4)

These are billed from EU entities (typically Ireland or Luxembourg) and trigger reverse charge under momsloven §46(1) nr. 1.

| Pattern | Billing entity | Rubrik | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 3/4 | Reverse charge services |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 3/4 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 3/4 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 3/4 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 3/4 | Reverse charge |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 3/4 | EU, reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 3/4 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 3/4 | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 3/4 | EU, reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 3/4 | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | 3/4 | Transaction fees may be exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge, rubrik 3/4)

| Pattern | Billing entity | Rubrik | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 3/4 | LU entity → EU reverse charge |
| NOTION | Notion Labs Inc (US) | 3/4 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 3/4 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 3/4 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 3/4 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 3/4 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | 3/4 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE) — check | 3/4 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 3/4 | Non-EU reverse charge |

**Note:** Denmark's momsangivelse does not separate EU vs non-EU reverse charge on services into different boxes — both go through rubrik 3 (output) and rubrik 4 (input). The distinction matters for EU sales list (listesystem) reporting only.

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU reverse charge rubrik 3/4 | Stripe IE entity |
| MOBILEPAY, NETS, CLEARHAUS | Check invoice | If Danish entity: domestic 25%; acquirer fees may be exempt |

### 3.11 Professional services (Denmark)

| Pattern | Treatment | Rubrik | Notes |
|---|---|---|---|
| ADVOKAT, ADVOKATFIRMA | Domestic 25% | 4 (input) | Legal services, deductible if business purpose |
| REVISOR, REVISIONSSELSKAB, STATSAUTORISERET | Domestic 25% | 4 (input) | Accountant/auditor — always deductible |
| NOTAR | Domestic 25% | 4 (input) | Notary services |
| VIRK.DK, CVR | EXCLUDE | Government fee, not a supply |

### 3.12 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ATP, AM-BIDRAG, A-SKAT | EXCLUDE | Statutory payroll taxes/contributions |
| LØN, SALARY, WAGES (outgoing) | EXCLUDE | Wages — outside VAT scope |
| FERIEKONTO | EXCLUDE | Holiday fund, statutory |
| DA-BARSEL | EXCLUDE | Parental leave fund |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| HUSLEJE, LEJE (commercial, invoiced with VAT) | Domestic 25% | Commercial lease where landlord opted to charge VAT (frivillig registrering) |
| HUSLEJE, LEJE (residential, no VAT) | EXCLUDE | Residential lease, exempt §13(1) nr. 8 |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OVERFØRSEL, INTERN, EGNE KONTI | EXCLUDE | Internal movement |
| UDBYTTE, DIVIDEND | EXCLUDE | Dividend payment, out of scope |
| LÅN, AFDRAG | EXCLUDE | Loan repayment, out of scope |
| HÆVNING, KONTANTHÆVNING, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Denmark-based self-employed IT consultant. They illustrate the trickiest cases.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; DKK 109.52`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). No VAT on the invoice. Services received from abroad — reverse charge under momsloven §46(1) nr. 1. Both output VAT (rubrik 3) and input VAT (rubrik 4) must be reported. Net effect zero for a fully taxable business. The 25% VAT on DKK 109.52 = DKK 27.38.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubrik (output) | Rubrik (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -109.52 | -109.52 | 27.38 | 25% | 3 | 4 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -6,350.00 ; DKK`

**Reasoning:**
Google Ireland Limited is an IE entity — EU reverse charge. Services purchased abroad, rubrik 3 for the output VAT amount (DKK 1,587.50) and rubrik 4 for the input VAT. Also report the net in rubrik 7 for EU sales list purposes if this is the reporting entity (but for the momsangivelse, rubrik 3/4 is sufficient). Net cash effect zero for a fully taxable business.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubrik (output) | Rubrik (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -6,350.00 | -6,350.00 | 1,587.50 | 25% | 3 | 4 | N | — | — |

### Example 3 — Entertainment, limited deduction

**Input line:**
`15.04.2026 ; RESTAURANT MARCHAL ; DEBIT ; Client dinner ; -1,800.00 ; DKK`

**Reasoning:**
Restaurant transaction. Business entertainment (repræsentation) under momsloven §42(2) allows recovery of 25% of the VAT amount. The full invoice is DKK 1,800 incl. 25% VAT. Net = DKK 1,440. VAT = DKK 360. Recoverable = 25% of DKK 360 = DKK 90. However, this requires documented business purpose and attendee list. Default: block fully. [T2] flag — reviewer must verify documentation.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubrik | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANT MARCHAL | -1,800.00 | -1,800.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked — 25% partial recovery possible under §42(2) if documented" |

### Example 4 — Capital goods (high-value purchase)

**Input line:**
`18.04.2026 ; DUSTIN A/S ; DEBIT ; Invoice DK2026-441 Dell XPS 15 ; -12,495.00 ; DKK`

**Reasoning:**
Domestic purchase from a Danish vendor. DKK 12,495 incl. 25% VAT. Net = DKK 9,996. VAT = DKK 2,499. This exceeds the capital goods threshold and will be subject to the 5-year adjustment period (investeringsgoder) under momsloven §43-44 if it qualifies as a capital good (purchase price excl. VAT > DKK 100,000 for goods). At DKK 9,996 net, this is below the DKK 100,000 capital goods scheme threshold — treat as normal overhead input VAT in rubrik 4.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubrik | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DUSTIN A/S | -12,495.00 | -9,996.00 | -2,499.00 | 25% | 4 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice DK-2026-018 IT consultancy March ; +26,250.00 ; DKK`

**Reasoning:**
Incoming DKK 26,250 from a German company. The client provides IT consulting services to a German B2B customer. Place of supply for services is Germany (customer's country) under the general rule. The client invoices at 0%, the German customer accounts for reverse charge. Report net in rubrik 7 (EU supplies). No output VAT in rubrik 1. Confirm: (a) customer is VAT-registered — verify German USt-IdNr on VIES; (b) the invoice shows no Danish moms.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubrik | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +26,250.00 | +26,250.00 | 0 | 0% | 7 | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, partial deduction

**Input line:**
`28.04.2026 ; JYSK BILCENTER ; DEBIT ; Car lease payment April ; -4,500.00 ; DKK`

**Reasoning:**
Car lease payment. Denmark allows partial VAT recovery on vehicles used for business — but only for commercial vehicles (varebiler/lastbiler). For passenger cars used for mixed business/private purposes, VAT deduction is generally not available unless the car is leased and used for business, in which case partial deduction may apply under momsloven §41(1) for leased passenger cars (1/3 of lease VAT deductible if car cost > DKK 160,000). Default: block fully. [T2] flag — reviewer must determine vehicle type and applicable deduction rule.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubrik | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | JYSK BILCENTER | -4,500.00 | -4,500.00 | 0 | — | — | Y | Q3 | "Vehicle: blocked — partial recovery may apply under §41 for leased passenger cars" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the rubrik mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 25% (momsloven §33)

The ONLY rate for all taxable supplies in Denmark. There are no reduced rates. Sales → rubrik 1 (VAT), rubrik 6 (net). Purchases → rubrik 4 (input VAT).

### 5.2 Zero rate (momsloven §34)

Exports outside EU → rubrik 8 (net, requires export evidence). Intra-EU B2B supplies of goods → rubrik 7 (net, requires customer VAT number verified on VIES, transport proof). Intra-EU B2B services → rubrik 7 (place of supply is customer's country, no Danish VAT). Newspapers and periodicals → 0% from 2024.

### 5.3 Exempt without credit (momsloven §13)

Medical services, dental care, social services, education, financial services, insurance, postal universal service, certain cultural/sporting events, residential rent, passenger transport. These supplies are excluded from the momsangivelse — no output VAT, no input VAT deduction on related costs. If exempt supplies are significant → **R-DK-5 refuses**.

### 5.4 Local standard purchases

Input VAT on a compliant tax invoice (faktura) from a Danish supplier is deductible at 25%. Rubrik 4 (input VAT). Subject to blocked-input rules (5.8).

### 5.5 Reverse charge — services received from abroad (momsloven §46(1) nr. 1)

When the client receives a service from an EU or non-EU supplier: compute 25% VAT on the net amount. Report output VAT in rubrik 3. Report same amount as input VAT in rubrik 4. Net cash effect zero for a fully taxable business. If the foreign supplier incorrectly charged their local VAT, that foreign VAT is NOT recoverable through the Danish return — must be reclaimed via EU refund procedure.

### 5.6 Reverse charge — EU goods acquisitions (momsloven §46(1) nr. 4)

Physical goods from an EU supplier: compute 25% VAT. Report output VAT in rubrik 2. Report input VAT in rubrik 4. Net value in rubrik 9.

### 5.7 Import VAT — goods from outside EU

Goods imported from non-EU countries: import VAT is settled on the momsangivelse (importmomsordningen — Denmark shifted import VAT reporting to the VAT return from 2015). Report in rubrik 4 as input VAT when the import VAT has been charged. The customs declaration (enhedsdokument) is the supporting document.

### 5.8 Blocked input VAT (momsloven §42)

The following categories have restricted or zero VAT recovery:
- Entertainment/representation: 25% of VAT recoverable under §42(2), requires documentation of business purpose and attendees
- Hotel accommodation for business: 100% deductible (changed from 75% — now fully deductible)
- Motor vehicles: passenger cars generally blocked; vans/trucks used for business fully deductible; leased passenger cars partial deduction under §41
- Tobacco and spirits: blocked §42(1) nr. 5-6
- Private use: fully blocked §42(1) nr. 1
- Natural gas, electricity for non-business purposes: blocked

### 5.9 Capital goods scheme (momsloven §43-44)

Capital goods with acquisition cost excl. VAT ≥ DKK 100,000 are subject to the capital goods adjustment scheme. Adjustment period: 5 years for movable goods, 10 years for immovable property (real estate). Below DKK 100,000: treat as normal overhead in rubrik 4.

### 5.10 Sales — local domestic

Charge 25%. Report VAT in rubrik 1, net in rubrik 6. No B2B/B2C distinction for domestic supplies.

### 5.11 Sales — cross-border B2C

Goods to EU consumers above €10,000 EU-wide threshold → **R-EU-5 (OSS refusal) from eu-vat-directive fires**. Digital services to EU consumers above €10,000 → same. Below threshold → Danish VAT at 25%, rubrik 1/6.

### 5.12 Lønsumsafgift interaction

Businesses making exempt supplies under §13 may be subject to lønsumsafgift (payroll tax on exempt activities). This is a separate return filed separately. If the client makes only taxable supplies, lønsumsafgift does not apply. If the client makes exempt supplies, **R-DK-1** or **R-DK-5** may fire.

---

## Section 6 — Tier 2 catalogue (compressed)

For each ambiguity type: pattern, why the bank statement is insufficient, conservative default, question for the structured form.

### 6.1 Fuel and vehicle costs

*Pattern:* Q8, Circle K, Shell DK, OK Benzin, fuel receipts. *Why insufficient:* vehicle type and use unknown. Passenger car → generally blocked; van/truck → deductible. *Default:* 0% recovery. *Question:* "Is this a commercial vehicle (varebil/lastbil) used exclusively for business, or a passenger car (personbil)?"

### 6.2 Restaurants and entertainment (repræsentation)

*Pattern:* any restaurant, café, bar, catering. *Why insufficient:* 25% partial recovery available but requires documentation. *Default:* block. *Question:* "Was this business entertainment with documented purpose and attendees? (If yes, 25% of VAT may be recoverable under §42(2).)"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, Slack, Zoom, etc. where the legal entity is not visible. *Why insufficient:* same brand can bill from IE (EU), US (non-EU), or DK (domestic). *Default:* reverse charge rubrik 3/4 (non-EU). *Question:* "Could you check the invoice for the legal entity name and country?"

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, your own capital injection, or a loan?"

### 6.5 Incoming transfers from individual names

*Pattern:* incoming from private-looking counterparties. *Default:* domestic B2C sale at 25%, rubrik 1/6. *Question:* "Was this a sale? Business or consumer? Country?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign IBAN or foreign currency. *Default:* domestic 25%. *Question:* "What was this — B2B with a VAT number, B2C, goods or services, and which country?"

### 6.7 Large one-off purchases

*Pattern:* single invoice near or above DKK 100,000 net. *Why insufficient:* capital goods threshold test applies. *Default:* if net ≥ DKK 100,000 → capital goods scheme; if net < DKK 100,000 → normal overhead in rubrik 4. *Question:* "Could you confirm the total invoice amount excluding VAT?"

### 6.8 Mixed-use phone, internet, home office

*Pattern:* TDC, Nuuday, YouSee personal lines; home electricity. *Default:* 0% if mixed without declared %, 100% if confirmed pure business. *Question:* "Is this a dedicated business line or mixed-use? What business percentage would you estimate?"

### 6.9 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Default:* exclude as drawings. *Question:* "Was this a contractor with an invoice, wages, a refund, or a personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* HÆVNING, ATM, KONTANT. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly HUSLEJE, LEJE to a landlord name. *Default:* no VAT (residential default). *Question:* "Is this a commercial property? Does the landlord charge moms on the rent (frivillig registrering)?"

### 6.12 Foreign hotel and accommodation

*Pattern:* hotel charged abroad. *Default:* exclude from input VAT (foreign VAT not recoverable through momsangivelse). *Question:* "Was this a business trip?" (For income tax records.)

### 6.13 Construction services received

*Pattern:* builder, contractor, craftsman (håndværker, murer, tømrer). *Why insufficient:* construction reverse charge may apply under §46(1) nr. 3 if the supplier is a subcontractor and the client is also in construction. *Default:* domestic 25% in rubrik 4 (normal purchase). *Question:* "Are you in the construction sector? Is this supplier a subcontractor to you?"

### 6.14 Platform sales (Amazon, eBay, Etsy)

*Pattern:* incoming from Amazon Payments EU, Etsy, PayPal, Stripe. *Default:* if client sells to EU consumers across countries above €10,000, R-EU-5 OSS refusal fires. For Denmark-only or below threshold: rubrik 1/6 at 25%; platform fees as separate reverse charge rubrik 3/4. *Question:* "Do you sell to buyers outside Denmark? Total EU cross-border sales for the year?"

---

## Section 7 — Excel working paper template (Denmark-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Denmark-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Rubrik code") accepts only valid momsangivelse rubrik codes from Section 1 of this skill (1–9). Use blank for excluded transactions. For reverse-charge transactions, enter both the output rubrik (e.g. 3) and input rubrik (e.g. 4) separated by a slash in column H.

### Sheet "Box Summary"

One row per rubrik. Denmark's form is simpler than most EU countries — only 9 boxes.

```
| 1  | Output VAT (udgående moms) | =SUMIFS(Transactions!F:F, Transactions!H:H, "1") |
| 2  | VAT on EU goods acquisitions | =SUMIFS(Transactions!F:F, Transactions!H:H, "2") |
| 3  | VAT on services from abroad (reverse charge) | =SUMIFS(Transactions!F:F, Transactions!H:H, "3") |
| 4  | Input VAT (indgående moms) | =SUMIFS(Transactions!F:F, Transactions!H:H, "4") |
| 5  | VAT payable/refundable | =C[1]+C[2]+C[3]-C[4] |
| 6  | Taxable sales excl. VAT | =SUMIFS(Transactions!E:E, Transactions!H:H, "6") |
| 7  | EU supplies excl. VAT | =SUMIFS(Transactions!E:E, Transactions!H:H, "7") |
| 8  | Exports excl. VAT | =SUMIFS(Transactions!E:E, Transactions!H:H, "8") |
| 9  | EU goods acquisitions excl. VAT | =SUMIFS(Transactions!E:E, Transactions!H:H, "9") |
```

### Sheet "Return Form"

Final momsangivelse-ready figures. The bottom-line cell is rubrik 5:

```
Rubrik 5 = Rubrik 1 + Rubrik 2 + Rubrik 3 − Rubrik 4

Positive rubrik 5 → payable to Skattestyrelsen.
Negative rubrik 5 → refund to the business.
```

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values from the bank statement, black for formulas, green for cross-sheet references, yellow background for any row where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/denmark-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Denmark bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Denmark-specific patterns.

**CSV format conventions.** Danske Bank exports use semicolon delimiters with DD.MM.YYYY dates. Nordea DK exports use comma delimiters. Common columns: Dato, Tekst, Beløb, Saldo. Jyske Bank includes a Posteringstype column. Always confirm date format and delimiter before parsing.

**Danish language variants.** Some descriptions appear in Danish: husleje (rent), løn/gage (salary), rente (interest), overførsel (transfer), hævning (withdrawal), indbetaling (deposit). Treat as English equivalents.

**Internal transfers and exclusions.** Own-account transfers between the client's Danske Bank, Nordea, Revolut accounts. Labelled "overførsel", "intern overførsel", "egne konti". Always exclude.

**Owner draws.** A self-employed sole trader (enkeltmandsvirksomhed) cannot pay themselves a salary — any transfer to their personal account is a drawing. Exclude.

**Refunds and reversals.** Identify by "refundering", "tilbageførsel", "kreditnota". Book as negative in the same rubrik as the original transaction.

**Foreign currency transactions.** Convert to DKK at the transaction date rate. Use the Danmarks Nationalbank rate or the rate shown on the bank statement.

**IBAN country prefix.** DK = Denmark. IE, LU, NL, FR, DE = EU. US, GB, AU, CH = non-EU.

---

## Section 9 — Onboarding fallback (only when inference fails)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first (Step 3) and only confirming with the client in Step 4. The questionnaire below is a fallback.

### 9.1 Entity type and trading name
*Inference rule:* sole traders (enkeltmandsvirksomhed) often match account holder name; company names end in "ApS", "A/S", "I/S", "K/S". *Fallback:* "Are you a sole trader (enkeltmandsvirksomhed), ApS, A/S, or partnership?"

### 9.2 VAT registration status
*Inference rule:* if asking for a momsangivelse, they are VAT-registered. *Fallback:* "Are you momsregistreret (VAT-registered)?"

### 9.3 CVR/SE number and VAT number
*Inference rule:* CVR numbers sometimes appear in payment descriptions. *Fallback:* "What is your CVR/SE number and momsregistreringsnummer? (DK + 8 digits)"

### 9.4 Filing period and frequency
*Inference rule:* first and last transaction dates. *Fallback:* "Which period does this cover? Monthly, quarterly, or half-yearly?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, sales descriptions. *Fallback:* "In one sentence, what does the business do?"

### 9.6 Employees
*Inference rule:* ATP, A-skat, løn outgoing transfers. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* medical/financial/educational income patterns. *Fallback:* "Do you make any VAT-exempt sales?" *If yes and non-de-minimis → R-DK-5 refuses.*

### 9.8 Credit brought forward
*Inference rule:* not inferable from single period. Always ask. *Question:* "Do you have any excess credit (tilgodehavende) from the previous period?"

### 9.9 Cross-border customers
*Inference rule:* foreign IBANs on incoming. *Fallback:* "Do you have customers outside Denmark? EU or non-EU? B2B or B2C?"

### 9.10 Vehicle type
*Inference rule:* not inferable from bank data. *Fallback:* "Do you use a vehicle for business? Is it a passenger car (personbil) or commercial vehicle (varebil/lastbil)?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the three-tier Accora architecture (vat-workflow-base + eu-vat-directive + country skill). Awaiting validation by a statsautoriseret revisor or registreret revisor in Denmark.

### Sources

**Primary legislation:**
1. Momsloven (Consolidated VAT Act) — https://www.retsinformation.dk
2. Momsbekendtgørelsen (VAT Executive Order)
3. Opkrævningsloven (Collection Act)

**Skattestyrelsen guidance:**
4. TastSelv Erhverv momsangivelse form — https://skat.dk
5. Skattestyrelsen guidance on reverse charge (omvendt betalingspligt)
6. Skattestyrelsen VAT registration thresholds

**EU directive (loaded via companion skill):**
7. Council Directive 2006/112/EC — implemented via eu-vat-directive companion skill
8. Council Implementing Regulation 282/2011

**Other:**
9. VIES validation — https://ec.europa.eu/taxation_customs/vies/
10. Danmarks Nationalbank exchange rates

### Known gaps

1. The supplier pattern library covers the most common Danish and international counterparties but not every local business.
2. Construction reverse charge (§46(1) nr. 3) is flagged as Tier 2 — a future version should add detailed construction classification rules.
3. Lønsumsafgift interaction is mentioned but not fully specified — out of scope for this VAT-only skill.
4. The capital goods threshold (DKK 100,000 excl. VAT) is the statutory amount as of April 2026. Verify annually.
5. Hotel accommodation VAT recovery (100% deductible) should be verified against current legislation.
6. The 25% entertainment recovery rule under §42(2) requires careful documentation — the skill defaults to block.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with three-tier Accora architecture. Quick reference moved to top (Section 1). Supplier pattern library restructured as literal lookup tables (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue restructured (Section 6). Excel working paper specification added (Section 7). Bank statement reading guide added (Section 8). Onboarding moved to fallback role (Section 9). Reference material moved to bottom (Section 10).
- **v1.0 (April 2026):** Initial skill. Standalone monolithic document. Awaiting validation.

### Self-check (v2.0)

1. Quick reference at top with rubrik table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 14 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 12 rules).
5. Tier 2 catalogue compressed with inference rules: yes (Section 6, 14 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only: yes (Section 9, 10 items).
8. All 7 Denmark-specific refusals present: yes (Section 2, R-DK-1 through R-DK-7).
9. Reference material at bottom: yes (Section 10).
10. No reduced rates — 25% only: explicitly stated in Section 1 and Section 5.1.
11. Entertainment partial recovery (25% under §42(2)) documented: yes (Section 3.7, Example 3, Section 5.8).
12. Vehicle rules documented: yes (Section 5.8, Example 6).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
