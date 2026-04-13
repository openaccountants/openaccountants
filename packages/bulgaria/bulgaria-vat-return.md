---
name: bulgaria-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Bulgarian VAT return (Spravka-deklaratsiya po DDS) for any client. Trigger on phrases like "prepare VAT return", "do the DDS", "fill in DDS return", "create the return", "Bulgarian VAT", or any request involving Bulgaria VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Bulgaria only and standard DDS registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Bulgarian VAT work.
version: 2.0
---

# Bulgaria VAT Return Skill (Spravka-deklaratsiya po DDS) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Bulgaria (Republic of Bulgaria) |
| Standard rate | 20% |
| Reduced rates | 9% (accommodation/hotel services, printed/electronic books, baby food/hygiene products) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods, international transport) |
| Return form | Spravka-deklaratsiya po DDS (monthly summary return with purchase/sales ledgers) |
| Filing portal | https://portal.nra.bg (NRA e-services portal) |
| Authority | Natsionalna agentsiya za prihodite (NRA / NAP — National Revenue Agency) |
| Currency | BGN (Bulgarian Lev); EUR from 2026 target date — verify |
| Filing frequencies | Monthly only (no quarterly/annual option for VAT returns in Bulgaria) |
| Deadline | 14th of the month following the tax period |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key return structure — Bulgaria uses purchase/sales ledgers submitted with the return:**

The return (Spravka-deklaratsiya) summarizes ledger totals. Key rows:

| Row | Meaning |
|---|---|
| 01 | Total output DDS (danak za nachislyavane) |
| 11 | Output DDS on domestic supplies at 20% |
| 12 | Output DDS on domestic supplies at 9% |
| 13 | Output DDS on intra-EU acquisitions |
| 14 | Output DDS on services received from abroad (reverse charge) |
| 15 | Output DDS on import (deferred payment scheme if applicable) |
| 20 | Zero-rated supplies (exports) |
| 21 | Intra-EU supplies of goods |
| 22 | Services to EU (B2B, place of supply = customer) |
| 30 | Exempt supplies without credit |
| 31 | Total input DDS (danak za prispacane / tax credit) |
| 40 | Input DDS on domestic purchases |
| 41 | Input DDS on intra-EU acquisitions (reverse charge input side) |
| 42 | Input DDS on imports |
| 43 | Input DDS on services from abroad (reverse charge input side) |
| 50 | Net DDS position (Row 01 minus Row 31) |
| 60 | Excess credit (nadvishan danak za prispacane) — 3-period offset rule |
| 70 | DDS payable to budget |
| 80 | DDS refundable (after 3-period offset) |

**Conservative defaults — Bulgaria-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Bulgaria |
| Unknown B2B vs B2C status for EU customer | B2C, charge 20% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | BGN 5,000 |
| HIGH tax-delta on a single conservative default | BGN 400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net DDS position | BGN 10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Bulgarian or international business bank: UniCredit Bulbank, DSK Bank, Fibank (First Investment Bank), Postbank (Eurobank Bulgaria), UBB (United Bulgarian Bank), Raiffeisenbank Bulgaria, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for intra-EU B2B services and zero-rated supplies), purchase invoices for any input DDS claim above BGN 400, the client's DDS number in writing (BG + 9/10 digits).

**Ideal** — complete purchase/sales ledgers (dnevnik za pokupkite / dnevnik za prodazhbite), prior period return, reconciliation of excess credit brought forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This return was produced from bank statement alone. The reviewer must verify, before approval, that input DDS claims above BGN 400 are supported by compliant tax invoices and that all reverse-charge classifications match the supplier's invoice."

### Bulgaria-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-BG-1 — Non-registered entity attempting to file a DDS return.** *Trigger:* client is not registered for DDS and turnover is below the mandatory threshold (EUR 51,130 / BGN 100,000 from 2026). *Message:* "Non-registered entities do not file DDS returns. If you wish to register voluntarily, contact NRA first."

**R-BG-2 — Partial exemption (mixed taxable and exempt supplies).** *Trigger:* client makes both taxable and exempt-without-credit supplies and the exempt proportion is not de minimis. *Message:* "You make both taxable and exempt supplies. Your input DDS must be apportioned using the partial credit coefficient (koefitsient) under ZDDS Art. 73. This requires an annual calculation. Please use a qualified accountant to determine the coefficient before input DDS is claimed."

**R-BG-3 — VAT group structure.** *Trigger:* client is part of a DDS group registration. *Message:* "DDS group registrations require consolidation across the group. Out of scope."

**R-BG-4 — Special schemes (margin, travel agent, investment gold).** *Trigger:* client deals in second-hand goods, travel packages, or investment gold under special schemes. *Message:* "Special DDS schemes require transaction-level margin or package computation. Out of scope for this skill."

**R-BG-5 — SAF-T filing complexity.** *Trigger:* client is a large enterprise required to file SAF-T alongside the DDS return with complex multi-branch reporting. *Message:* "SAF-T filing for large enterprises with multi-branch structures requires specialist IT and accounting setup. Out of scope."

**R-BG-6 — Fiscal representative.** *Trigger:* non-resident supplier with fiscal representative in Bulgaria. *Message:* "Non-resident registrations with fiscal representatives have specific obligations beyond this skill. Please use a qualified accountant."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules — the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Bulgarian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| UNICREDIT BULBANK, BULBANK | EXCLUDE for bank charges/fees | Financial service, exempt |
| DSK BANK, DSK | EXCLUDE for bank charges/fees | Same |
| FIBANK, FIRST INVESTMENT BANK | EXCLUDE for bank charges/fees | Same |
| POSTBANK, EUROBANK BULGARIA | EXCLUDE for bank charges/fees | Same |
| UBB, UNITED BULGARIAN BANK | EXCLUDE for bank charges/fees | Same |
| RAIFFEISENBANK BG, RAIFFEISEN | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| ЛИХВА, ЛИХВИ, INTEREST | EXCLUDE | Interest income/expense, out of scope |
| КРЕДИТ, ЗАЕМ, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Bulgarian government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| НАП, NRA, NAP, NATIONAL REVENUE | EXCLUDE | Tax payment, not a supply |
| ДДС ПЛАЩАНЕ, VAT PAYMENT | EXCLUDE | DDS payment |
| МИТНИЦА, CUSTOMS | EXCLUDE | Customs duty (but check for import VAT on customs declaration) |
| НОИ, NSSI, SOCIAL INSURANCE | EXCLUDE | Social security payment |
| ОБЩИНА, MUNICIPALITY | EXCLUDE | Municipal fees, sovereign acts |
| АГЕНЦИЯ ПО ВПИСВАНИЯТА, REGISTRY AGENCY | EXCLUDE | Company registration fees |
| ПАТЕНТНО ВЕДОМСТВО | EXCLUDE | Patent office fees |

### 3.3 Bulgarian utilities

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| ЧЕЗ, CEZ RAZPREDELENIE, CEZ ELECTRO | Domestic 20% | 40 (input) | Electricity — overhead |
| ЕЛЕКТРОХОЛД, ELECTROHOLD | Domestic 20% | 40 (input) | Electricity distributor |
| EVN BULGARIA, EVN | Domestic 20% | 40 (input) | Electricity — overhead |
| ENERGO-PRO, ЕНЕРГО-ПРО | Domestic 20% | 40 (input) | Electricity — overhead |
| СОФИЙСКА ВОДА, SOFIYSKA VODA | Domestic 20% | 40 (input) | Water — overhead |
| VIVACOM, ВИВАКОМ | Domestic 20% | 40 (input) | Telecoms/broadband |
| A1 BULGARIA, А1 | Domestic 20% | 40 (input) | Telecoms |
| YETTEL, ТЕЛЕНОР | Domestic 20% | 40 (input) | Telecoms |
| БУЛГАРГАЗ, OVERGAS | Domestic 20% | 40 (input) | Gas supply |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DZI, ДЗИ | EXCLUDE | Insurance, exempt |
| BULSTRAD, БУЛСТРАД | EXCLUDE | Same |
| ALLIANZ BULGARIA, АЛИАНЦ | EXCLUDE | Same |
| GENERALI BULGARIA | EXCLUDE | Same |
| EUROINS, ЕВРОИНС | EXCLUDE | Same |
| UNIQA BULGARIA | EXCLUDE | Same |
| ЗАСТРАХОВКА, INSURANCE, ПРЕМИЯ | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| БЪЛГАРСКИ ПОЩИ, BULGARIAN POSTS | EXCLUDE for standard postal services | | Universal postal service, exempt |
| БЪЛГАРСКИ ПОЩИ (parcel/courier) | Domestic 20% | 40 | Non-universal services are taxable |
| SPEEDY, СПИДИ | Domestic 20% | 40 | Domestic courier |
| ECONT, ЕКОНТ | Domestic 20% | 40 | Domestic courier |
| DHL EXPRESS BG | Domestic 20% | 40 | Express courier |
| DHL INTERNATIONAL | EU reverse charge (DE/IE entity) | 41/43 | Check invoice — European billing entity |

### 3.6 Transport

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| БДЖ, BDZ, BULGARIAN RAILWAYS | Domestic 20% | 40 | Domestic rail |
| SOFIA METRO, МЕТРОПОЛИТЕН | EXCLUDE / 20% | | Public transport |
| TAXI, ТАКСИМЕТРОВ | Domestic 20% | 40 | Local taxi |
| RYANAIR, WIZZ AIR (international) | EXCLUDE / 0% | | International flights zero rated |
| BULGARIA AIR (domestic) | Domestic 20% | 40 | Domestic flight |
| BULGARIA AIR (international) | EXCLUDE / 0% | | International flight zero rated |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| KAUFLAND, LIDL, BILLA, FANTASTICO | Default BLOCK input DDS | Personal provisioning. Deductible only if hospitality/catering business. |
| CBA, METRO CASH & CARRY | Default BLOCK unless resale | If buying for resale, deductible |
| РЕСТОРАНТ, RESTAURANT, КАФЕ, CAFE | Default BLOCK | Entertainment/representation — see Section 5.12 |

### 3.8 SaaS — EU suppliers (reverse charge)

These are billed from EU entities and trigger reverse charge under ZDDS Art. 82(2).

| Pattern | Billing entity | Row | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 14/43 | Reverse charge services |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 14/43 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 14/43 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 14/43 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 14/43 | Reverse charge |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 14/43 | EU, reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 14/43 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 14/43 | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 14/43 | EU, reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 14/43 | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | 14/43 | Transaction fees may be exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge)

| Pattern | Billing entity | Row | Notes |
|---|---|---|---|
| AWS EMEA SARL | AWS EMEA SARL (LU) | 14/43 | LU entity = EU reverse charge |
| NOTION | Notion Labs Inc (US) | 14/43 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 14/43 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 14/43 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 14/43 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 14/43 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | 14/43 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or IE — check | 14/43 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 14/43 | Non-EU reverse charge |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU reverse charge | Stripe IE entity — separate from transaction fees |
| SUMUP, SQUARE, ZETTLE | Check invoice | If BG entity: domestic 20%; if IE/EU entity: reverse charge |

### 3.11 Professional services (Bulgaria)

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| НОТАРИУС, NOTARY | Domestic 20% | 40 | Deductible if business purpose |
| СЧЕТОВОДИТЕЛ, ACCOUNTANT, ОДИТОР, AUDITOR | Domestic 20% | 40 | Always deductible |
| АДВОКАТ, LAWYER, ATTORNEY | Domestic 20% | 40 | Deductible if business legal matter |
| ТЪРГОВСКИ РЕГИСТЪР, COMMERCIAL REGISTER | EXCLUDE | Government fee, not a supply |

### 3.12 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ДОО, DOO, СОЦИАЛНО ОСИГУРЯВАНЕ | EXCLUDE | Social security contribution |
| ДЗПО, DZPO | EXCLUDE | Supplementary pension |
| ЗО, ЗДРАВНО ОСИГУРЯВАНЕ | EXCLUDE | Health insurance contribution |
| ЗАПЛАТА, SALARY, WAGES | EXCLUDE | Wages — outside DDS scope |
| ДАНЪК ВЪРХУ ДОХОДИТЕ | EXCLUDE | Income tax |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| НАЕМ, RENT (commercial, with DDS invoice) | Domestic 20% | Commercial lease where landlord charges DDS |
| НАЕМ, RENT (residential, no DDS) | EXCLUDE | Residential lease exempt (first letting) |
| ПРОМИШЛЕН ПАРК, INDUSTRIAL PARK | Domestic 20% | Industrial/commercial let |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| ВЪТРЕШЕН ПРЕВОД, OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| ДИВИДЕНТ, DIVIDEND | EXCLUDE | Dividend payment, out of scope |
| ПОГАСЯВАНЕ НА КРЕДИТ, LOAN REPAYMENT | EXCLUDE | Loan principal, out of scope |
| ТЕГЛЕНЕ, CASH WITHDRAWAL, ATM | Ask | Default exclude; ask what cash was spent on |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Bulgaria-based self-employed IT consultant. They illustrate the trickiest cases.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; BGN 28.70`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). No VAT on the invoice. Service received from non-EU supplier. Under ZDDS Art. 82(2), the Bulgarian recipient self-assesses output DDS at 20% and simultaneously claims input DDS. Both sides must appear: output in Row 14, input in Row 43. Net effect zero for fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | DDS | Rate | Row (input) | Row (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -28.70 | -28.70 | 5.74 | 20% | 43 | 14 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -1,660.00 ; BGN`

**Reasoning:**
Google Ireland Limited is an IE entity — standard EU reverse charge. Google Ads is a service. Output DDS self-assessed at 20% in Row 14, input DDS in Row 43. Both sides on the return. Net zero for fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | DDS | Rate | Row (input) | Row (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -1,660.00 | -1,660.00 | 332.00 | 20% | 43 | 14 | N | — | — |

### Example 3 — Entertainment/representation, limited deduction

**Input line:**
`15.04.2026 ; РЕСТОРАНТ ЩАСТЛИВЕЦА ; DEBIT ; Business dinner ; -430.00 ; BGN`

**Reasoning:**
Restaurant transaction. In Bulgaria, entertainment/representation expenses have deductible input DDS but the expense itself is subject to a 10% expense tax under the Corporate Income Tax Act (ZKPO Art. 204–207). The input DDS on the invoice IS deductible (unlike Malta where entertainment is hard-blocked). However, for a sole trader (ET), representation expenses may be challenged. Default: claim input DDS but flag for reviewer. Note the 10% expense tax obligation separately.

**Output:**

| Date | Counterparty | Gross | Net | DDS | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | РЕСТОРАНТ ЩАСТЛИВЕЦА | -430.00 | -358.33 | -71.67 | 20% | 40 | Y | Q1 | "Representation: confirm business purpose; 10% expense tax applies" |

### Example 4 — Capital goods (no statutory threshold)

**Input line:**
`18.04.2026 ; ТЕХНОПОЛИС ; DEBIT ; Laptop Lenovo ThinkPad ; -3,118.00 ; BGN`

**Reasoning:**
Bulgaria does not have a specific DDS monetary threshold for capital goods like Malta's EUR 1,160. However, assets used for business with a useful life > 1 year are subject to capital goods adjustment rules: 5-year for movables (ZDDS Art. 79(3)), 20-year for immovables (ZDDS Art. 79(7)). This laptop qualifies as a capital asset. Input DDS is deductible. Flag for capital goods tracking.

**Output:**

| Date | Counterparty | Gross | Net | DDS | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | ТЕХНОПОЛИС | -3,118.00 | -2,598.33 | -519.67 | 20% | 40 | N | — | "Capital goods — 5yr adjustment tracking" |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice BG-2026-018 IT consultancy March ; +6,850.00 ; BGN`

**Reasoning:**
Incoming from a German company. The client provides IT consulting services. B2B place of supply is the customer's country (Germany). The Bulgarian client invoices at 0%. Report in Row 22 (services to EU). Confirm: (a) customer has valid USt-IdNr; (b) invoice shows no Bulgarian DDS.

**Output:**

| Date | Counterparty | Gross | Net | DDS | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +6,850.00 | +6,850.00 | 0 | 0% | 22 | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, partial restriction

**Input line:**
`28.04.2026 ; OMV БЪЛГАРИЯ ; DEBIT ; Fuel ; -150.00 ; BGN`

**Reasoning:**
Fuel purchase. In Bulgaria, input DDS on passenger vehicles and their fuel/maintenance is deductible only if the vehicle is used exclusively for business, for taxi/rent-a-car, or if the vehicle has 6+1 seats. For a standard passenger car used partly for personal purposes, input DDS is restricted. Default: 0% recovery unless the client can demonstrate 100% business use or the vehicle qualifies under the exceptions (ZDDS Art. 70(1)(4-5)).

**Output:**

| Date | Counterparty | Gross | Net | DDS | Rate | Row | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | OMV БЪЛГАРИЯ | -150.00 | -150.00 | 0 | — | — | Y | Q3 | "Vehicle: confirm 100% business use or excluded vehicle type" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the row mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 20% (ZDDS Art. 66(1)(1))

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Sales: Row 11 (output base/DDS). Purchases: Row 40 (input DDS).

### 5.2 Reduced rate 9% (ZDDS Art. 66(2))

Applies to: accommodation/hotel services (tourist sector), printed and electronic books and publications, specific baby food and hygiene products. Sales: Row 12 (output base/DDS). Purchases: Row 40 at 9%.

**Note:** The temporary 9% rate on restaurant/catering and sports facilities expired 31 December 2024. From 1 January 2025 these are at 20%.

### 5.3 Zero rate and exempt with credit

Exports outside EU (ZDDS Art. 28): Row 20. Intra-EU B2B supplies of goods (ZDDS Art. 7): Row 21 (zero-rated, requires VIES-verified VAT number, transport proof). Intra-EU B2B services (ZDDS Art. 21(2)): Row 22 (place of supply is customer's country). International transport (ZDDS Art. 30-32): Row 20.

### 5.4 Exempt without credit

Financial services (Art. 46), insurance (Art. 47), healthcare (Art. 39), education (Art. 41), residential rental first letting (Art. 45), gambling (Art. 48), postal universal service (Art. 49). These are excluded from the return — no output DDS, no input deduction on related costs.

### 5.5 Local standard purchases

Input DDS on a compliant tax invoice (данъчна фактура) from a BG supplier is deductible for purchases used in taxable business activity. Subject to blocked-input rules (5.12). Map to Row 40.

### 5.6 Reverse charge — EU services received (ZDDS Art. 82(2))

Service from EU supplier invoiced at 0% with reverse-charge note: output DDS self-assessed at 20% in Row 14, input DDS in Row 43. Net zero for fully taxable client. If the EU supplier charged their local VAT, that is NOT reverse charge — treat as overhead with irrecoverable foreign VAT.

### 5.7 Reverse charge — EU goods received (ZDDS Art. 84)

Physical goods from EU supplier: output DDS self-assessed in Row 13, input DDS in Row 41.

### 5.8 Reverse charge — non-EU services received (ZDDS Art. 82(2))

Services from outside EU with no VAT charged: same treatment as EU reverse charge. Output in Row 14, input in Row 43.

### 5.9 Imports (ZDDS Art. 56)

Physical goods imported from non-EU: import DDS assessed by customs on the customs declaration. Input DDS on import in Row 42 if goods are for taxable business use.

### 5.10 Capital goods adjustments (ZDDS Art. 79)

Movable capital goods: 5-year adjustment period. Immovable property: 20-year adjustment period. No specific monetary threshold — asset classification based on accounting standards (useful life > 1 year). If client disposes of or changes use, adjustment may be required.

### 5.11 3-period excess credit offset (ZDDS Art. 92)

Bulgaria has a unique rule: if input DDS exceeds output DDS, the excess is NOT immediately refundable. It must be offset against output DDS due in the next 3 consecutive periods. Only if excess remains after 3 periods is it refundable. Exception: accelerated refund for businesses with >30% zero-rated supplies.

### 5.12 Blocked input DDS (ZDDS Art. 70)

The following have restricted or zero recovery:
- Passenger vehicles (up to 8+1 seats) and their fuel/maintenance — blocked unless used exclusively for taxable business, taxi/rent-a-car, 6+1 seat exception (Art. 70(1)(4-5))
- Goods/services for entertainment/representation — input DDS IS deductible, but subject to 10% expense tax under ZKPO
- Goods for personal use of staff/owners (Art. 70(1)(2))
- Goods/services not used for taxable supplies (Art. 70(1)(1))

### 5.13 Sales — local domestic (any rate)

Charge 20% or 9% as applicable. Report in sales ledger and Rows 11/12.

### 5.14 Sales — cross-border B2C

Services to EU consumers above EUR 10,000 threshold: R-EU-5 (OSS refusal) from eu-vat-directive fires. Below threshold: Bulgarian DDS at applicable rate.

### 5.15 Purchase/sales ledgers (ZDDS Art. 124-126)

Both the purchase ledger (dnevnik za pokupkite) and sales ledger (dnevnik za prodazhbite) MUST be submitted with the return. Each invoice must be individually recorded.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* OMV, Shell, Лукойл, Petrol, EKO, fuel receipts. *Why insufficient:* vehicle type and business-use unknown. Passenger car fuel blocked unless 100% business or qualifying vehicle. *Default:* 0% recovery. *Question:* "Is this a passenger car (restricted) or a commercial vehicle/qualifying vehicle used 100% for business?"

### 6.2 Restaurants and entertainment

*Pattern:* any restaurant, café, bar, catering name. *Why insufficient:* representation expenses deductible for DDS but trigger 10% expense tax. Business vs personal unknown. *Default:* block input DDS. *Question:* "Was this a business representation expense? (Note: if yes, input DDS deductible but 10% expense tax applies under ZKPO.)"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, Slack, Zoom, etc. *Why insufficient:* same brand bills from IE, US, or local entity. *Default:* non-EU reverse charge. *Question:* "Check the invoice for the legal entity name and billing country."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit matching client's name. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, your own money, or a loan?"

### 6.5 Incoming transfers from individual names

*Pattern:* incoming from private-looking counterparties. *Default:* domestic B2C sale at 20%. *Question:* "Was this a sale? Business or consumer? Country?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign IBAN or foreign currency. *Default:* domestic 20%. *Question:* "B2B with VAT number, B2C, goods or services, which country?"

### 6.7 Large one-off purchases (capital goods tracking)

*Pattern:* equipment, laptop, machinery. *Why insufficient:* no statutory DDS threshold but accounting classification determines adjustment period. *Default:* deductible; flag for capital goods register. *Question:* "Confirm useful life > 1 year for capital goods tracking."

### 6.8 Mixed-use phone, internet, home office

*Pattern:* Vivacom, A1, Yettel personal lines; home electricity. *Default:* 0% if mixed without declared %. *Question:* "Dedicated business line or mixed-use? Business percentage?"

### 6.9 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Default:* exclude as drawings. *Question:* "Contractor with invoice, wages, refund, or personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, теглене, cash withdrawal. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* наем, rent, lease. *Default:* no DDS (residential default). *Question:* "Commercial or residential? Does landlord charge DDS?"

### 6.12 Foreign hotel and accommodation

*Pattern:* hotel charged abroad. *Default:* exclude from input DDS. *Question:* "Was this a business trip?"

### 6.13 Credit brought forward and 3-period offset

*Pattern:* excess credit from prior periods. *Why insufficient:* must track the 3-period offset chain. *Default:* flag for reviewer. *Question:* "Which period did the excess credit originate? Has it been offset for 3 consecutive periods?"

---

## Section 7 — Excel working paper template (Bulgaria-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Bulgaria-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Row code") accepts only valid Bulgaria DDS row codes from Section 1 of this skill. Use blank for excluded transactions.

### Sheet "Row Summary"

One row per return row. Column A is the row number, column B is the description, column C is the value computed via formula. Key rows:

```
Output DDS:
| 11 | Output DDS domestic 20% | =SUMIFS(Transactions!F:F, Transactions!H:H, "11") |
| 12 | Output DDS domestic 9% | =SUMIFS(Transactions!F:F, Transactions!H:H, "12") |
| 13 | Output DDS intra-EU goods | =SUMIFS(Transactions!F:F, Transactions!H:H, "13") |
| 14 | Output DDS reverse charge services | =SUMIFS(Transactions!F:F, Transactions!H:H, "14") |
| 20 | Zero-rated exports | =SUMIFS(Transactions!E:E, Transactions!H:H, "20") |
| 21 | Intra-EU supplies goods | =SUMIFS(Transactions!E:E, Transactions!H:H, "21") |
| 22 | Intra-EU services | =SUMIFS(Transactions!E:E, Transactions!H:H, "22") |
| 01 | Total output DDS | =SUM(Row11..Row15) |

Input DDS:
| 40 | Input DDS domestic | =SUMIFS(Transactions!F:F, Transactions!H:H, "40") |
| 41 | Input DDS EU goods | =SUMIFS(Transactions!F:F, Transactions!H:H, "41") |
| 42 | Input DDS imports | =SUMIFS(Transactions!F:F, Transactions!H:H, "42") |
| 43 | Input DDS reverse charge services | =SUMIFS(Transactions!F:F, Transactions!H:H, "43") |
| 31 | Total input DDS | =SUM(Row40..Row43) |

Settlement:
| 50 | Net DDS (Row 01 - Row 31) | =Row01-Row31 |
| 70 | DDS payable (if 50 > 0) | =MAX(0, Row50) |
| 60 | Excess credit (if 50 < 0) | =ABS(MIN(0, Row50)) |
```

### Sheet "Return Form"

Final return-ready figures. Bottom-line: Row 70 (payable) or Row 60/80 (excess credit / refundable after 3-period offset).

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values, black for formulas, green for cross-sheet references, yellow background for any Default? = "Y" row.

---

## Section 8 — Bulgaria bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Bulgaria-specific patterns.

**CSV format conventions.** UniCredit Bulbank and DSK exports typically use semicolon delimiters with DD.MM.YYYY dates. Revolut Business exports use ISO dates. Common columns: Date, Description, Debit, Credit, Balance. Fibank may use Cyrillic headers.

**Bulgarian/Cyrillic variants.** Descriptions may be in Bulgarian Cyrillic: наем (rent), заплата (salary), лихва (interest), превод (transfer), теглене (withdrawal). Treat as English equivalent.

**Internal transfers.** Own-account transfers between client's banks. Labelled "вътрешен превод", "own transfer". Always exclude.

**Sole trader draws.** A self-employed person (ET — едноличен търговец) cannot pay themselves wages — transfers to personal account are drawings. Exclude.

**Refunds and reversals.** Identify by "възстановяване", "refund", "сторно", "reversal". Book as negative in same row as original.

**Foreign currency.** Convert to BGN at the BNB (Bulgarian National Bank) fixing rate for the transaction date. Note the rate in the Notes column.

**IBAN prefix.** BG = Bulgaria. IE, LU, NL, FR, DE = EU. US, GB, AU, CH = non-EU.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type and trading name
*Inference rule:* ET = sole trader; OOD/EOOD = limited company. *Fallback:* "Are you a sole trader (ET), limited company (OOD/EOOD), or other?"

### 9.2 DDS registration status
*Inference rule:* if filing a DDS return, they are registered. *Fallback:* "Are you DDS-registered (mandatory or voluntary)?"

### 9.3 DDS number
*Inference rule:* BG-format numbers may appear in EU customer payment descriptions. *Fallback:* "What is your DDS number? (BG + 9/10 digits)"

### 9.4 Filing period
*Inference rule:* first and last transaction dates. Bulgaria is always monthly. *Fallback:* "Which month does this cover?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix. *Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* DOO/ZO outgoing payments. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* medical/financial/educational income patterns. *Fallback:* "Do you make exempt supplies?" *If yes and non-de-minimis: R-BG-2 refuses.*

### 9.8 3-period excess credit status
*Inference rule:* not inferable from single period. *Fallback:* "Do you have excess DDS credit carried forward? From which period?"

### 9.9 Cross-border customers
*Inference rule:* foreign IBANs on incoming. *Fallback:* "Do you have customers outside Bulgaria? EU or non-EU? B2B or B2C?"

### 9.10 Vehicle ownership
*Inference rule:* fuel/vehicle-related debits. *Fallback:* "Do you own/lease a vehicle for business? Type (passenger car vs commercial)?"

---

## Section 10 — Reference material

### Sources

**Primary legislation:**
1. Zakon za danak varhu dobavenata stoynost (ZDDS — VAT Act) — Articles 2-12, 28-50, 56, 66, 70, 73, 79, 82, 84, 92, 124-126
2. Pravilnik za prilagane na ZDDS (PPZDDS — Implementing Regulations)

**NRA guidance:**
3. NRA DDS return form and instructions — https://portal.nra.bg
4. NRA guidance on reverse charge
5. NRA SAF-T implementation guidance

**EU directive (loaded via companion skill):**
6. Council Directive 2006/112/EC — via eu-vat-directive companion skill
7. Council Implementing Regulation 282/2011

**Other:**
8. VIES validation — https://ec.europa.eu/taxation_customs/vies/
9. BNB exchange rates — https://www.bnb.bg

### Known gaps

1. The supplier pattern library covers common Bulgarian counterparties but not every local SME.
2. The 3-period offset rule for excess credits requires period-by-period tracking beyond this skill's single-period scope.
3. SAF-T filing requirements (phased from 2026) are not fully detailed.
4. The 9% reduced rate scope should be verified annually.
5. BGN-to-EUR transition (target date) may affect currency handling.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. 10-section layout. Supplier pattern library with Bulgarian banks (UniCredit Bulbank, DSK, Fibank). No inline tier tags. Companion skill references added.
- **v1.0 (April 2026):** Initial skill with inline tier tags.

### Self-check (v2.0)

1. Quick reference at top with row table and conservative defaults: yes.
2. Supplier library as literal lookup tables: yes (14 sub-tables).
3. Worked examples (6): yes.
4. Tier 1 rules compressed without inline tags: yes (15 rules).
5. Tier 2 catalogue compressed: yes (13 items).
6. Excel template specification: yes.
7. Onboarding as fallback only: yes (10 items).
8. All Bulgaria-specific refusals present: yes (R-BG-1 through R-BG-6).
9. Reference material at bottom: yes.
10. No inline [T1]/[T2]/[T3] tags in body text: yes.

## End of Bulgaria VAT Return Skill v2.0

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.1 or later AND `eu-vat-directive` v0.1 or later.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
