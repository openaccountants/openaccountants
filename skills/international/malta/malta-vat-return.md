---
name: malta-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Malta VAT return (VAT3 form) or Article 11 annual declaration for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in VAT3", "create the return", "Article 11 declaration", or any request involving Malta VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Malta only and only Article 10 (standard) and Article 11 (small enterprise) registrations. Article 12, partial exemption, capital goods scheme adjustments, margin schemes, and VAT groups are all in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Malta VAT work.
version: 2.0
---

# Malta VAT Return Skill (VAT3 / Article 11 Declaration) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Malta (Republic of Malta) |
| Standard rate | 18% |
| Reduced rates | 7% (accommodation, minor repairs), 5% (food, pharmaceuticals, printed matter, medical devices), 12% (certain financial instruments, confectionery) |
| Zero rate | 0% (exports, intra-EU B2B supplies, certain foodstuffs, passenger transport by sea/air) |
| Return form | VAT3 (standard Article 10 periodic return); Article 11 Annual Declaration (4-box simplified form) |
| Filing portal | https://cfr.gov.mt (VAT Online) |
| Authority | Commissioner for Revenue (CFR), Malta |
| Currency | EUR only |
| Filing frequencies | Quarterly (Article 10, standard); Monthly (Article 12 only); Annual (Article 11 small enterprise) |
| Deadline | Article 10 e-filing: 21st of month after quarter end; Article 10 paper: 14th; Article 11 annual: 15 March following year |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
<<<<<<< HEAD
| Validated by | Michael Cutajar, Kevin Farrugia (warranted accountants) |
| Validation date | March 2026 |
=======
| Validated by | Pending — requires sign-off by a Maltese warranted accountant |
| Validation date | Pending |
>>>>>>> 70c2582 (Update accounting project files)

**Key VAT3 boxes (the boxes you will use most):**

| Box | Meaning |
|---|---|
| 1 | Intra-EU B2B supplies of services (net, 0% VAT) |
| 2 | Exports and supplies outside EU (net, 0% VAT) |
| 3 | Output base for reverse-charge acquisitions from EU |
| 4 | Output base for reverse-charge acquisitions from non-EU |
| 5 | Total output value (derived: 1+2+3+4) |
| 6 | Output VAT on EU reverse-charge acquisitions |
| 7 | Output VAT on non-EU reverse-charge acquisitions |
| 8 | Total output VAT (derived: 6+7) |
| 9 / 9a | EU goods / EU services acquisitions (net) |
| 10 | EU capital goods acquisitions (net) |
| 11 | Non-EU goods/services acquisitions (net) |
| 12 | Total acquisition values (derived: 9+9a+10+11) |
| 13 / 13a | Input VAT on EU goods / EU services |
| 14 | Input VAT on EU capital goods |
| 15 | Input VAT on non-EU acquisitions |
| 16 | Total input VAT on acquisitions (derived: 13+13a+14+15) |
| 17 | Net output VAT on acquisitions (derived: 8−16) |
| 18 / 18a / 18b | Local sales 18% / 7% / 12% (net) |
| 19 | Local sales 5% (net) |
| 20 | Zero-rated sales (net) |
| 21 | Exempt sales (net) |
| 22 | Total local sales (derived: 18+18a+18b+19+20+21) |
| 23 / 23a / 23b | Output VAT on local sales 18% / 7% / 12% |
| 24 | Output VAT on local sales 5% |
| 25 | Total output VAT on local sales (derived: 23+23a+23b+24) |
| 26 | Total output VAT (derived: 17+25) |
| 27 / 28 | Local purchases for resale 18% / 5% (net) |
| 29 | Zero-rated local purchases for resale (net) |
| 30 | Capital goods (net) |
| 31 / 31a / 31b | Local overhead purchases 18% / 7% / 12% (net) |
| 32 | Local overhead purchases 5% (net) |
| 33 | Total local purchase values (derived: 27+28+29+30+31+31a+31b+32) |
| 34 / 35 | Input VAT on local resale purchases 18% / 5% |
| 36 | Input VAT on capital goods |
| 37 / 37a / 37b | Input VAT on local overhead 18% / 7% / 12% |
| 38 | Input VAT on local overhead 5% |
| 39 | Total input VAT on local purchases (derived: 34+35+36+37+37a+37b+38) |
| 40 | Excess credit from prior adjustments |
| 41 | Other credits / adjustments |
| 42 | Excess credit carried forward (if 39 > 26) |
| 43 | VAT payable (if 26 > 39) |
| 44 | Credit brought forward from prior period |
| 45 | Net payable after B/F credit (43 − 44) |

**Conservative defaults — Malta-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 18% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Malta |
| Unknown B2B vs B2C status for EU customer | B2C, charge 18% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (Box 11/15) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | €3,000 |
| HIGH tax-delta on a single conservative default | €200 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | €5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the quarter in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Maltese or international business bank: BOV, HSBC Malta, APS, Lombard Bank, Banif, Revolut Business, Wise Business, N26 Business, or any other.

**Recommended** — sales invoices for the period (especially for intra-EU B2B services and zero-rated supplies), purchase invoices for any input VAT claim above €200, the client's VAT number in writing (MT + 8 digits).

**Ideal** — complete invoice register, Article 10/11 registration certificate, prior period VAT3, reconciliation of Box 44 credit brought forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all → hard stop. If bank statement only without invoices → proceed but record in the reviewer brief: "This VAT3 was produced from bank statement alone. The reviewer must verify, before approval, that input VAT claims above €200 are supported by compliant tax invoices and that all reverse-charge classifications match the supplier's invoice."

### Malta-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

**R-MT-1 — Article 11 client attempting to claim input VAT.** *Trigger:* client is Article 11 registered, or turnover is below €35,000 and client has not opted into Article 10. *Message:* "Article 11 clients are exempt from charging VAT and cannot recover input VAT. They file a simplified annual declaration only, not a VAT3. This skill can help you with the Article 11 annual declaration but cannot prepare a VAT3 or calculate input VAT recovery for an Article 11 client."

**R-MT-2 — Article 12 registration (distance selling / EU goods acquisition threshold).** *Trigger:* client is Article 12 registered (goods acquirer from EU exceeding €10,000/year threshold, monthly filer). *Message:* "Article 12 registrations have different filing frequencies and obligations. This skill covers Article 10 and Article 11 only. Please escalate to a warranted accountant familiar with Article 12 obligations."

**R-MT-3 — Partial exemption (Article 22(4)).** *Trigger:* client makes both taxable supplies and exempt-without-credit supplies (financial services, residential rent, medical, education) and the exempt proportion is not de minimis. *Message:* "You make both taxable and exempt supplies. Your input VAT must be apportioned under Article 22(4), which requires a year-end pro-rata calculation that cannot be completed on a single-period basis without the annual ratio. Please use a warranted accountant to determine and confirm the pro-rata rate before input VAT is claimed."

**R-MT-4 — Capital goods scheme adjustment (Article 24).** *Trigger:* the period contains an adjustment to previously deducted input VAT on a capital good under Article 24 (5-year adjustment period for goods, 10-year for immovable property). *Message:* "Capital goods scheme adjustments under Article 24 are too fact-sensitive for this skill. They require tracking the original deduction, current and intended use, and computing the annual fraction. Please use a warranted accountant."

**R-MT-5 — Margin scheme.** *Trigger:* client deals in second-hand goods, art, antiques, or collectables under the margin scheme. *Message:* "Margin scheme transactions require transaction-level margin computation. Out of scope for this skill."

**R-MT-6 — VAT group (Article 5(2)).** *Trigger:* client is part of a VAT group or asks about group registration. *Message:* "VAT groups under Article 5(2) require consolidation across the group. Out of scope."

**R-MT-7 — Fiscal representative.** *Trigger:* non-resident supplier or client with a fiscal representative in Malta. *Message:* "Non-resident registrations with fiscal representatives have specific obligations beyond this skill. Please use a warranted accountant."

**R-MT-8 — Annual return (TA24 income tax) instead of VAT3.** *Trigger:* user asks about annual income tax return, not the VAT3. *Message:* "This skill only handles the VAT3 and Article 11 VAT declaration. For Malta income tax (TA24), use the malta-income-tax skill."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules — the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Maltese banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BOV, BANK OF VALLETTA | EXCLUDE for bank charges/fees | §4 Nr 8 equivalent: financial service, exempt |
| HSBC MALTA | EXCLUDE for bank charges/fees | Same |
| APS BANK, LOMBARD BANK, BANIF | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTERESSI, INTEREST, MGĦAX | EXCLUDE | Interest income/expense, out of scope |
| LOAN, SELF-EMPLOYED LOAN, PERSONAL LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Maltese government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| CFR, COMMISSIONER FOR REVENUE, INLAND REVENUE | EXCLUDE | Tax payment, not a supply |
| VAT DEPARTMENT | EXCLUDE | VAT payment |
| CUSTOMS, DIPARTIMENT TAD-DWANA | EXCLUDE | Customs duty (but see EC8 for import VAT C88) |
| MFSA, LOTTERIES AND GAMING, MGA | EXCLUDE | Licence fees, sovereign acts |
| MALTA ENTERPRISE, MCAST, UNIVERSITY OF MALTA | EXCLUDE | Government grants/fees, sovereign acts |
| PBS, TVM, NET TV | EXCLUDE | Broadcasting levy, not a VATable supply |
| ARMS (water/electricity bills from enemy.com.mt) | Domestic 18% | ARMS Ltd is taxable; electricity at 18% |
| ENEMALTA | Domestic 18% | Standard rated utility |

### 3.3 Maltese utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| ARMS LTD, ARMS LIMITED, ENEMY | Domestic 18% | 31/37 | Electricity, water, gas — overhead |
| ENEMALTA | Domestic 18% | 31/37 | Same |
| MELITA, GO PLC, EPIC | Domestic 18% | 31/37 | Telecoms/broadband — overhead |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MIDDLESEA, MSV, LAFERLA, GasanMamo | EXCLUDE | §4 Nr 10 equivalent, exempt |
| MAPFRE, AXA MALTA, GLOBALCAP | EXCLUDE | Same |
| INSURANCE, ASSIGURAZZJONI, INSURANCE PREMIUM | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| MALTA POST, MALTAPOST | EXCLUDE for standard postage stamps | | Universal service, exempt |
| MALTA POST | Domestic 18% for parcel services, tracked, courier | 31/37 | Non-universal services are taxable |
| DHL EXPRESS MALTA, TNT MALTA, FedEx Malta | Domestic 18% | 31/37 | Express courier, taxable |
| DHL INTERNATIONAL | EU reverse charge (IE entity) | 9a/13a | Check invoice — European billing entity |

### 3.6 Transport (Malta domestic)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| TALLINJA, MALTA PUBLIC TRANSPORT | EXCLUDE or 0% | | Public bus — zero rated passenger transport |
| BOLT MALTA, UBER MALTA | Domestic 18% (platform fee reverse charge EU) | 31/37 or 9a/13a | Underlying ride 18%; platform fee via IE — check |
| TRANSFER, TAXI | Domestic 18% | 31/37 | Local taxi |
| AIR MALTA, RYANAIR, WIZZ AIR (international) | EXCLUDE / 0% | | International flights zero rated |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| LIDL MALTA, PAVI, ARKADIA, PARK TOWERS, SCOTTS | Default BLOCK input VAT | Personal provisioning. Deductible only if hospitality/catering business. |
| SUPERMARKET, ĦANUT | Default BLOCK | Same |
| RESTAURANTS, CAFES, BARS (any named restaurant) | Default BLOCK | Entertainment blocked under 10th Schedule Item 3(1)(b) — see EC4 |

### 3.8 SaaS — EU suppliers (reverse charge, Box 9a / 13a)

These are billed from EU entities (typically Ireland or Luxembourg) and trigger §13b equivalent reverse charge.

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 9a/13a | Reverse charge services |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 9a/13a | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 9a/13a | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 9a/13a | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 9a/13a | Reverse charge |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 9a/13a | EU, reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 9a/13a | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 9a/13a | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 9a/13a | EU, reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 9a/13a | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | 9a/13a | Transaction fees may be exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge, Box 11 / 15)

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — BUT check | 9a/13a | LU entity → EU reverse charge. Unlike Germany, no domestic branch exception in Malta |
| NOTION | Notion Labs Inc (US) | 11/15 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 11/15 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 11/15 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 11/15 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 11/15 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | 11/15 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE) — check invoice | 11/15 or 9a/13a | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 11/15 | Non-EU reverse charge |

### 3.10 SaaS — the exception (NOT reverse charge)

| Pattern | Treatment | Why |
|---|---|---|
| AWS EMEA SARL | EU reverse charge Box 9a/13a (Luxembourg entity) | Malta has no AWS domestic branch equivalent to the German exception. Standard EU reverse charge applies. If invoice shows MT VAT charged, treat as local 18%. |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU reverse charge Box 9a/13a | Stripe IE entity — separate line item from transaction fees |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Maltese entity: domestic 18%; if IE/EU entity: reverse charge |

### 3.12 Professional services (Malta)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| Notary names (NUTAR, DR [name] NOTARY) | Domestic 18% | 31/37 | Deductible if business purpose |
| Accountant / auditor names (CPA, ACCA, AUDIT) | Domestic 18% | 31/37 | Always deductible |
| Solicitor / advocate (ADV, AVV, LAWYER) | Domestic 18% | 31/37 | Deductible if business legal matter |
| Malta Business Registry, MBR | EXCLUDE | Government fee, not a supply |
| MFSA fees | EXCLUDE | Regulatory fee, not a supply |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ĊESOP, SSC, SOCIAL SECURITY | EXCLUDE | Statutory SSC payment |
| FSS, INCOME TAX, PAYER TAX | EXCLUDE | PAYE/FSS tax remittance |
| SALARY, PAGA, WAGES (outgoing) | EXCLUDE | Wages — outside VAT scope |
| NI, NATIONAL INSURANCE | EXCLUDE | If referencing UK obligations |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| KIRJA, RENT (commercial, invoiced with VAT) | Domestic 18% | Commercial lease where landlord opted to charge VAT |
| KIRJA, RENT (residential, no VAT) | EXCLUDE | Residential lease exempt without credit |
| GROUND RENT, ĊENS | EXCLUDE | Ground rent, sovereign/feudal in nature, out of scope |
| MALTA FREEPORT, MALTA ENTERPRISE PARK | Domestic 18% | Industrial/commercial let, usually taxable |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL, ACCOUNT TRANSFER | EXCLUDE | Internal movement |
| DIVIDEND, DIVIDENT | EXCLUDE | Dividend payment, out of scope |
| LOAN REPAYMENT, REPAYMENT | EXCLUDE | Loan principal, out of scope |
| CASH WITHDRAWAL, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |
| DIRECTOR FEE (received) | EXCLUDE | Director fees are outside VAT scope in Malta — see EC10 |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Malta-based self-employed IT consultant. They illustrate the trickiest cases. Pattern-match against these when you encounter similar lines in any real statement.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). No VAT on the invoice. This is a service received from a non-EU supplier. Article 10 client applies reverse charge under the equivalent of Article 19/20 of the Malta VAT Act. Both sides of the reverse charge must be reported: output VAT in Box 4/7, input VAT in Box 11/15. Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (input) | Box (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 2.64 | 18% | 11 / 15 | 4 / 7 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
Google Ireland Limited is an IE entity — standard EU reverse charge. Google Ads is a service (not physical goods). Box 9a for the net, Box 13a for input VAT, Box 3 for output base, Box 6 for output VAT. The gross amount is treated as the net (Google invoices net of VAT to VAT-registered EU clients). Both sides must appear on the return.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (input) | Box (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 153.00 | 18% | 9a / 13a | 3 / 6 | N | — | — |

### Example 3 — Entertainment, fully blocked

**Input line:**
`15.04.2026 ; SCIORTINO'S RESTAURANT VALLETTA ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant transaction. Entertainment is fully blocked under the Malta VAT Act 10th Schedule Item 3(1)(b). Unlike Germany (where Bewirtung can be recovered with the right documentation), Malta has a hard block on entertainment — no exceptions for business purpose, no partial recovery, no receipt exception. The input VAT is irrecoverable regardless of whether the dinner was a genuine client meeting. Default: full block. No input VAT entry.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | SCIORTINO'S RESTAURANT | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked" |

### Example 4 — Capital goods threshold

**Input line:**
`18.04.2026 ; DELL TECHNOLOGIES MALTA ; DEBIT ; Invoice DEL2026-0041 Laptop XPS 15 ; -1,595.00 ; EUR`

**Reasoning:**
The gross amount is €1,595. The Article 24 capital goods threshold is €1,160 gross. €1,595 ≥ €1,160, so this is a capital goods purchase. It goes to Box 30 (net) and Box 36 (input VAT), not Box 31/37. If the gross had been €980, it would go to Box 31/37 as an overhead. The gross test applies — do not net out the VAT first before testing against the threshold.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DELL TECHNOLOGIES MALTA | -1,595.00 | -1,351.69 | -243.31 | 18% | 30 / 36 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice MT-2026-018 IT consultancy March ; +3,500.00 ; EUR`

**Reasoning:**
Incoming €3,500 from a German company (DE IBAN). The client is providing IT consulting services. B2B place of supply for services is the customer's country (Germany) under the general rule. The client invoices at 0%, the German customer accounts for reverse charge in Germany. Report net amount in Box 1 (EU B2B services). No output VAT. Confirm: (a) customer is a VAT-registered business — ask for the German USt-IdNr; (b) the invoice shows no Maltese VAT with a note that the customer accounts for VAT. If the customer cannot provide a valid USt-IdNr, reclassify as B2C and charge Maltese 18%.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 1 | Y | Q2 (HIGH) | "Verify German USt-IdNr" |

### Example 6 — Motor vehicle, hard block

**Input line:**
`28.04.2026 ; AUTOSALES MALTA LTD ; DEBIT ; Invoice AUT-1189 Hyundai Tucson lease payment ; -650.00 ; EUR`

**Reasoning:**
Car lease payment. Input VAT on motor vehicles (and therefore leased vehicles) is hard-blocked under the Malta VAT Act 10th Schedule Item 3(1)(a)(iv-v). This block applies regardless of whether the vehicle is used exclusively for business. The only exceptions are: taxi services, driving instruction, car rental as the primary business activity, or hearse services. An IT consultant does not fall within any exception. Default: full block, no input VAT recovery. If client later claims this is a qualifying business vehicle, [T2] flag for reviewer — do not unblock without warranted accountant sign-off.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | AUTOSALES MALTA LTD | -650.00 | -650.00 | 0 | — | — | Y | Q3 | "Motor vehicle: blocked" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the box mapping. Apply silently if the data is unambiguous. For full doctrinal context, see the source citations in Section 10.

### 5.1 Standard rate 18% (VAT Act Cap. 406, 5th Schedule Part 1)

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Sales → Box 18 / Box 23. Purchases → Box 31 / Box 37.

### 5.2 Reduced rate 7% (5th Schedule Part 2)

Applies to: short-term accommodation (hotels, guesthouses under 3 months), minor repairs to bicycles, shoes, leather goods, clothing, domestic appliances. Sales → Box 18a / Box 23a. Purchases → Box 31a / Box 37a.

### 5.3 Reduced rate 12% (5th Schedule Part 3)

Applies to: certain financial instruments and related services, confectionery in specific circumstances. Sales → Box 18b / Box 23b. Purchases → Box 31b / Box 37b.

### 5.4 Reduced rate 5% (5th Schedule Part 4)

Applies to: food (with exceptions for confectionery, ice cream, alcohol), non-prescription medicines and pharmaceutical products, medical devices for disabled persons, printed books and newspapers, children's car seats, certain seeds and plants. Sales → Box 19 / Box 24. Purchases → Box 28 / Box 35 (resale) or Box 32 / Box 38 (overhead).

### 5.5 Zero rate and exempt with credit

Exports outside EU → Box 2 (zero-rated, requires export evidence). Intra-EU B2B supplies of goods → Box 2 (zero-rated, requires customer VAT number verified on VIES, transport proof, compliant invoice). Intra-EU B2B services → Box 1 (place of supply is customer's country, no Maltese VAT, requires customer VAT number). International passenger transport (sea/air) → Box 20.

### 5.6 Exempt without credit

Residential rent, certain medical services, insurance, financial services, postal universal service, education. These supplies are excluded from the VAT return — no output VAT, no input VAT deduction on related costs. If these are significant, partial exemption rules apply — **R-MT-3 refuses** if non-de-minimis.

### 5.7 Local standard purchases

Input VAT on a compliant tax invoice from a Malta supplier is deductible for purchases used in taxable business activity. Subject to blocked-input rules (5.12) and the capital goods threshold (5.9). Map overhead to Box 31/37. Map resale goods to Box 27/34.

### 5.8 Reverse charge — EU services received (VAT Act Art. 19 equivalent)

When the client receives a service from an EU supplier and the supplier invoices at 0% with a reverse-charge note: net → Box 9a, input VAT → Box 13a, output base → Box 3, output VAT → Box 6. Net cash effect zero for a fully taxable Article 10 client. If the EU supplier charged their local VAT (e.g. Irish 23%), that is NOT reverse charge — treat as an overhead expense with irrecoverable foreign VAT.

### 5.9 Reverse charge — EU goods received

Physical goods from an EU supplier: net → Box 9, input VAT → Box 13, output base → Box 3, output VAT → Box 6.

### 5.10 Reverse charge — non-EU services and goods received

For all services and goods received from outside the EU where no VAT was charged: net → Box 11, input VAT → Box 15, output base → Box 4, output VAT → Box 7. Net cash effect zero for a fully taxable client.

### 5.11 Capital goods (Article 24)

If gross invoice amount ≥ €1,160: Box 30 (net) / Box 36 (input VAT). If gross < €1,160: Box 31/37 (overhead). The gross test applies — test the invoice total before subtracting VAT. Capital goods are subject to a 5-year (or 10-year for immovable property) adjustment period. Note for §15a-equivalent tracking: if client later disposes of or changes use of the asset, an adjustment may be required — document the original classification.

### 5.12 Blocked input VAT (10th Schedule)

The following categories have zero VAT recovery with no exceptions unless specifically noted:
- Entertainment of any kind (Item 3(1)(b)) — hard block, no Bewirtungsbeleg equivalent in Malta
- Motor vehicles: purchase, lease, or fuel for cars not used exclusively for taxi/driving school/car rental/hearse (Item 3(1)(a)(iv-v))
- Tobacco products (Item 3(1)(a)(i))
- Alcohol (Item 3(1)(a)(ii)) — note: deductible for hospitality businesses where alcohol is stock in trade
- Art, antiques, and collectables (Item 3(1)(a)(iii))
- Pleasure craft (Item 3(1)(a)(iv))
- Personal use items (Item 3(1)(c))

Blocked categories override partial exemption. Check blocked status before applying any recovery.

### 5.13 Article 11 annual declaration (4-box simplified form)

Article 11 clients do not file VAT3. They file a 4-box annual declaration:
- Box 1: Sales of goods
- Box 2: Provision of services
- Box 3: Purchases of stock for resale
- Box 4: Purchases of capital assets

General overhead expenses do not appear on the declaration. No input VAT recovery. No reverse-charge boxes. This skill processes Article 11 declarations in simplified mode — Steps 5.7 through 5.12 do not apply.

### 5.14 Sales — local domestic (any rate)

Charge 18%, 7%, 12%, or 5% as applicable. No B2B/B2C distinction for domestic Malta supplies. Map to Box 18/18a/18b/19 as appropriate.

### 5.15 Sales — cross-border B2C

Goods to EU consumers above €10,000 EU-wide threshold → **R-EU-5 (OSS refusal) from eu-vat-directive fires**. Digital services to EU consumers above €10,000 → same. Below threshold → Maltese VAT at applicable rate, Box 18.

---

## Section 6 — Tier 2 catalogue (compressed)

For each ambiguity type: pattern, why the bank statement is insufficient, conservative default, question for the structured form.

### 6.1 Fuel and vehicle costs

*Pattern:* Agip, Enemed, Shell Malta, BP Malta, fuel receipts. *Why insufficient:* vehicle type and business-use proportion unknown. If vehicle is a car → blocked regardless of use. If van, truck, motorbike for business delivery → deductible. *Default:* 0% recovery. *Question:* "Is this a car (blocked) or a commercial vehicle used exclusively for business?"

### 6.2 Restaurants and entertainment

*Pattern:* any named restaurant, café, bar, catering. *Why insufficient:* entertainment is hard blocked under 10th Schedule. Business meals do not have a recoverable exception in Malta. *Default:* block. *Question:* "Was this a client entertainment meal or a staff meal? (Note: both are blocked — this is for income tax records only.)"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, Slack, Zoom, LinkedIn, Apple, Amazon, Dropbox, Atlassian, Stripe, PayPal where the legal entity is not visible. *Why insufficient:* same brand can bill from Ireland (EU reverse charge Box 9a/13a), US (non-EU reverse charge Box 11/15), or Malta (domestic 18%). *Default:* non-EU reverse charge Box 11/15 (most conservative — if the supplier is EU and the client provided their VAT number, the invoice will show 0% anyway). *Question:* "Could you check the most recent invoice from each? I need the legal entity name and whether it shows a reverse-charge note or Maltese VAT."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Why insufficient:* could be a customer sale, owner injection, or family loan. *Default:* exclude as owner injection. *Question:* "The €X transfer from [name] — is this a customer payment, your own money going in, or a loan?"

### 6.5 Incoming transfers from individual names (not owner)

*Pattern:* incoming from private-looking counterparties. *Why insufficient:* could be B2C sale, B2B sale paid from personal account, refund. *Default:* domestic B2C sale at 18%, Box 18/23. *Question:* "For each: was it a sale? Business or consumer customer? Country?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign IBAN or foreign currency. *Why insufficient:* could be B2B (zero-rated with VAT number), B2C (potentially OSS), goods, services, refund. *Default:* domestic 18%. *Question:* "What was this — B2B with a VAT number, B2C, goods or services, and which country?"

### 6.7 Large one-off purchases (potential capital goods)

*Pattern:* single invoice €800–€1,160 range (near threshold), or labelled "laptop", "equipment", "machinery". *Why insufficient:* gross amount determines classification, and €1,160 gross is the threshold. *Default:* if gross ≥ €1,160 → Box 30/36; if gross < €1,160 → Box 31/37. *Question:* "Could you confirm the total invoice amount including VAT?" (Needed to apply the gross test correctly.)

### 6.8 Mixed-use phone, internet, home office

*Pattern:* Melita, GO, EPIC personal lines; home electricity. *Why insufficient:* business proportion unknown. *Default:* 0% if mixed without declared %, 100% if confirmed pure business. *Question:* "Is this a dedicated business line or mixed-use? What business percentage would you estimate?"

### 6.9 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Why insufficient:* could be contractor with invoice, wages, refund, drawings. *Default:* exclude as drawings. *Question:* "Was this a contractor you paid with an invoice, wages, a refund to a customer, or a personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, cash withdrawal, BOV cash. *Why insufficient:* unknown what cash was spent on. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly "kirja", "rent", "lease" to a landlord-sounding counterparty. *Why insufficient:* commercial vs residential, whether landlord opted to charge VAT. *Default:* no VAT, no deduction (residential default). *Question:* "Is this a commercial property? Does the landlord charge VAT on the rent?"

### 6.12 Foreign hotel and accommodation (non-Malta)

*Pattern:* hotel or accommodation charged abroad. *Why insufficient:* place of supply is the location of the property — non-Malta VAT paid at source, not recoverable. *Default:* exclude from input VAT. *Question:* "Was this a business trip?" (For income tax records, the expense may still be deductible.)

### 6.13 Airbnb income

*Pattern:* Airbnb payouts, short-term rental income. *Why insufficient:* duration determines VAT treatment; below-threshold Article 11 status affects whether output VAT is due. *Default:* [T2] flag for reviewer — confirm rental duration and Article registration. *Question:* "Is this rental for under 3 months (short-term, 7% output VAT if Article 10) or over 3 months (long-term, exempt)? Confirm with reviewer."

### 6.14 Director fee payments (outgoing)

*Pattern:* monthly payment to a director name, described as "director fee" or "management fee". *Why insufficient:* payments to a director as a director are outside VAT scope; but if the director also provides separate consultancy services with an invoice, that is a VATable supply. *Default:* exclude as out-of-scope. *Question:* "Is this a director fee (out of scope) or a consultancy invoice from the director for separately agreed professional services?"

### 6.15 Platform sales (Amazon, eBay, Etsy)

*Pattern:* incoming from Amazon Payments EU, Etsy Payments, PayPal, Stripe. *Why insufficient:* aggregated settlement may include multi-country buyer mix. *Default:* if client sells to EU consumers across multiple countries above €10,000, R-EU-5 OSS refusal fires. For Malta-only or below-threshold: treat gross as Box 18/23 base at 18%; platform fees as separate reverse charge Box 9a/13a (IE entity). *Question:* "Do you sell to buyers outside Malta? Total EU cross-border sales for the year?"

---

## Section 7 — Excel working paper template (Malta-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Malta-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Box code") accepts only valid Malta VAT3 box codes from Section 1 of this skill. Use blank for excluded transactions. For reverse-charge transactions, enter both the input box (e.g. 9a) and the output box (e.g. 3) separated by a slash in column H.

### Sheet "Box Summary"

One row per box. Column A is the box number, column B is the description, column C is the value computed via formula. Mandatory rows in this exact order:

```
Output (acquisitions):
| 3  | Output base EU reverse charge | =SUMIFS(Transactions!E:E, Transactions!H:H, "3") |
| 4  | Output base non-EU reverse charge | =SUMIFS(Transactions!E:E, Transactions!H:H, "4") |
| 6  | Output VAT EU reverse charge | =Box_Summary!C[3_row]*0.18 |
| 7  | Output VAT non-EU reverse charge | =Box_Summary!C[4_row]*0.18 |
| 8  | Total output VAT on acquisitions | =Box_Summary!C[6_row]+Box_Summary!C[7_row] |

Acquisitions (input):
| 9  | EU goods acquisitions net | =SUMIFS(Transactions!E:E, Transactions!H:H, "9") |
| 9a | EU services acquisitions net | =SUMIFS(Transactions!E:E, Transactions!H:H, "9a") |
| 10 | EU capital goods acquisitions net | =SUMIFS(Transactions!E:E, Transactions!H:H, "10") |
| 11 | Non-EU acquisitions net | =SUMIFS(Transactions!E:E, Transactions!H:H, "11") |
| 13 | Input VAT EU goods | =Box_Summary!C[9_row]*0.18 |
| 13a| Input VAT EU services | =Box_Summary!C[9a_row]*0.18 |
| 14 | Input VAT EU capital goods | =Box_Summary!C[10_row]*0.18 |
| 15 | Input VAT non-EU | =Box_Summary!C[11_row]*0.18 |
| 16 | Total input VAT acquisitions | =SUM(C[13_row]:C[15_row]) |
| 17 | Net output VAT acquisitions | =C[8_row]-C[16_row] |

Local sales:
| 18 | Local sales 18% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "18") |
| 18a| Local sales 7% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "18a") |
| 18b| Local sales 12% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "18b") |
| 19 | Local sales 5% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "19") |
| 23 | Output VAT 18% | =C[18_row]*0.18 |
| 23a| Output VAT 7% | =C[18a_row]*0.07 |
| 23b| Output VAT 12% | =C[18b_row]*0.12 |
| 24 | Output VAT 5% | =C[19_row]*0.05 |
| 25 | Total local output VAT | =SUM(C[23_row]:C[24_row]) |
| 26 | Grand total output VAT | =C[17_row]+C[25_row] |

Local purchases:
| 27 | Resale 18% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "27") |
| 28 | Resale 5% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "28") |
| 30 | Capital goods net | =SUMIFS(Transactions!E:E, Transactions!H:H, "30") |
| 31 | Overhead 18% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "31") |
| 31a| Overhead 7% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "31a") |
| 31b| Overhead 12% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "31b") |
| 32 | Overhead 5% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "32") |
| 34 | Input VAT resale 18% | =C[27_row]*0.18 |
| 35 | Input VAT resale 5% | =C[28_row]*0.05 |
| 36 | Input VAT capital goods | =C[30_row]*0.18 |
| 37 | Input VAT overhead 18% | =C[31_row]*0.18 |
| 37a| Input VAT overhead 7% | =C[31a_row]*0.07 |
| 37b| Input VAT overhead 12% | =C[31b_row]*0.12 |
| 38 | Input VAT overhead 5% | =C[32_row]*0.05 |
| 39 | Total local input VAT | =SUM(C[34_row]:C[38_row]) |
```

### Sheet "Return Form"

Final VAT3-ready figures. The bottom-line cell is Box 43 (payable) or Box 42 (excess credit):

```
Box 26 = Grand total output VAT
Box 39 = Total local input VAT

IF Box 39 > Box 26:
  Box 42 = (Box 39 - Box 26) + (Box 41 - Box 40)   [excess credit]
  Box 43 = 0
ELSE:
  Box 42 = 0
  Box 43 = (Box 26 - Box 39) + (Box 40 - Box 41)   [tax payable]

Box 45 = Box 43 - Box 44   [net after B/F credit]
```

Positive Box 45 → payable to CFR. Negative → request refund or carry forward as Box 44 in next period.

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values from the bank statement (column D of Transactions), black for formulas (everything in Box Summary and Return Form), green for cross-sheet references (Return Form referencing Box Summary), yellow background for any row in Sheet "Transactions" where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/malta-vat-<period>-working-paper.xlsx
```

Check the JSON output. If `status` is `errors_found`, fix the formulas and re-run. If `status` is `success`, present via `present_files`.

---

## Section 8 — Malta bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Malta-specific patterns.

**CSV format conventions.** BOV and HSBC Malta exports typically use comma delimiters with DD/MM/YYYY dates. Revolut Business exports use ISO dates. Common columns: Date, Description, Debit, Credit, Balance. Wise exports include currency columns. Always confirm which account currency applies before converting.

**Maltese language variants.** Some descriptions appear in Maltese: kirja (rent), paga/salarju (salary), interessi (interest), ħanut (shop), flus kontanti (cash), ittrasferit (transferred). Treat as the English equivalent.

**Internal transfers and exclusions.** Own-account transfers between the client's BOV, HSBC, Revolut accounts. Labelled "own transfer", "transfer to savings", "internal". Always exclude.

**Director draws.** A self-employed sole trader cannot pay themselves wages — any transfer to their personal account is a drawing. Exclude. A single-director company paying a director fee: exclude from VAT (out of scope) but flag for income tax records.

**Refunds and reversals.** Identify by "refund", "reversal", "chargeback", "storno". Book as a negative in the same box as the original transaction. Correction is in the period the refund is booked, not by amending the original period.

**Airbnb and short-term rental income.** Airbnb Malta payouts appear as "AIRBNB PAYMENTS", "AIRBNB *, AIRBNB IRELAND" from an IE IBAN. These are an aggregated settlement of rental income. The rental income itself is a Maltese 7% output VAT supply (if Article 10, short-term under 3 months). The Airbnb platform service fee is an EU reverse charge (Box 9a/13a). Both must be separated. [T2] flag: confirm duration and Article registration.

**Foreign currency transactions.** Convert to EUR at the transaction date rate. Use the ECB reference rate for non-USD/GBP currencies, or the rate shown on the bank statement. Note the rate used in the Transactions sheet column L (Notes).

**IBAN country prefix.** MT = Malta. IE, LU, NL, FR, DE = EU (relevant for EU reverse charge). US, GB, AU, CH = non-EU. A Maltese IBAN from the counterparty does not automatically mean a Maltese VAT registration — always cross-check the supplier name against Section 3.

**Cryptic descriptions.** Card purchases with only a merchant terminal code; SEPA direct debits with only a mandate reference. If the counterparty cannot be identified from the description, ask the client. Do not classify unidentified transactions.

---

## Section 9 — Onboarding fallback (only when inference fails)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first (Step 3) and only confirming with the client in Step 4. The questionnaire below is a fallback — ask only the questions the data could not answer.

For each question, the inference rule comes first. Only ask if inference fails.

### 9.1 Entity type and trading name
*Inference rule:* sole trader names often match the account holder name; company names end in "Ltd", "Limited", "Co. Ltd". *Fallback question:* "Are you a self-employed sole trader, a limited company, or a partnership?"

### 9.2 VAT registration type
*Inference rule:* if the client is asking for a VAT3, they are Article 10. If they mention no VAT on sales and annual filing, they are Article 11. *Fallback question:* "Are you Article 10 (standard VAT, charging 18%) or Article 11 (small enterprise exemption, turnover below €35,000)?"

### 9.3 VAT number
*Inference rule:* MT-format VAT numbers sometimes appear in payment descriptions from EU customers. Search statement descriptions first. *Fallback question:* "What is your Maltese VAT number? (MT + 8 digits)"

### 9.4 Filing period
*Inference rule:* first and last transaction dates on the bank statement. Article 10 is quarterly. *Fallback question:* "Which quarter does this cover? Q1 (Jan–Mar), Q2 (Apr–Jun), Q3 (Jul–Sep), or Q4 (Oct–Dec)?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, sales description patterns, invoice descriptions. IT, consultancy, hospitality, retail, construction are recognisable. *Fallback question:* "In one sentence, what does the business do?"

### 9.6 Employees
*Inference rule:* SSC, FS3, PAYE outgoing transfers to non-owner names. *Fallback question:* "Do you have employees? If so, how many?"

### 9.7 Exempt supplies
*Inference rule:* presence of medical/financial/educational/residential rental income. *Fallback question:* "Do you make any VAT-exempt sales (medical, education, insurance, financial services, residential lettings)?" *If yes and non-de-minimis → R-MT-3 refuses.*

### 9.8 Rental income
*Inference rule:* Airbnb payouts, "kirja" credits, property management names. *Conditional fallback — only if rental income is suspected:* "Is this short-term rental (under 3 months) or long-term? Is the property used for Airbnb?"

### 9.9 Credit brought forward
*Inference rule:* not inferable from a single period statement. Always ask. *Question:* "Do you have any excess credit from the previous quarter carried forward? (Box 44)"

### 9.10 Cross-border customers
*Inference rule:* foreign IBANs on incoming, foreign currency, foreign-name customers. *Fallback question:* "Do you have customers outside Malta? In EU countries or outside the EU? Are they businesses (B2B with VAT numbers) or consumers?"

---

## Section 10 — Reference material

### Validation status

<<<<<<< HEAD
This skill is v2.0, rewritten in April 2026 to align with the three-tier Accora architecture (vat-workflow-base + eu-vat-directive + country skill). It supersedes v1.0 (March 2026, standalone monolithic skill). The Malta-specific content (box mappings, rates, thresholds, blocked categories) has been validated against the VAT Act Chapter 406 and CFR guidance by Michael Cutajar (CPA Warrant No. 125122) and Kevin Farrugia (warranted accountant), both in Malta.
=======
This skill is v2.0, rewritten in April 2026 to align with the three-tier Accora architecture (vat-workflow-base + eu-vat-directive + country skill). It supersedes v1.0 (March 2026, standalone monolithic skill). The Malta-specific content (box mappings, rates, thresholds, blocked categories) is drawn from the VAT Act Chapter 406 and CFR guidance. Independent sign-off by a Maltese warranted accountant is pending and is a prerequisite to any reliance.
>>>>>>> 70c2582 (Update accounting project files)

### Sources

**Primary legislation:**
1. VAT Act, Chapter 406, Laws of Malta — https://legislation.mt — Articles 2, 5, 10, 11, 12, 19, 20, 21, 22, 24, 10th Schedule, 5th Schedule
2. Value Added Tax (Amendment) Acts (subsequent amendments incorporated in consolidated text)

**CFR guidance:**
3. CFR VAT3 form and completion notes — https://cfr.gov.mt
4. CFR Article 11 Annual Declaration form — https://cfr.gov.mt
5. CFR guidance on reverse charge (intra-EU and non-EU services)
6. CFR VAT registration thresholds notice (Article 10/11/12 boundaries)

**EU directive (loaded via companion skill):**
7. Council Directive 2006/112/EC (Principal VAT Directive) — implemented via eu-vat-directive companion skill
8. Council Implementing Regulation 282/2011

**Other:**
9. VIES validation — https://ec.europa.eu/taxation_customs/vies/
10. ECB euro reference rates — https://www.ecb.europa.eu/stats/eurofxref/

### Known gaps

1. The supplier pattern library in Section 3 covers the most common Maltese and international counterparties but does not cover every local SME or regional brand. Add patterns as they emerge.
2. The worked examples are drawn from a hypothetical IT consultant in Malta. They do not cover hospitality, retail, e-commerce, or construction specifically. A v2.1 should add sector-specific worked examples.
3. The reduced rate table (7%, 12%, 5%) covers the most common items but the 5th Schedule is detailed — edge cases (e.g. specific food items near the confectionery boundary) should be flagged [T2] for reviewer.
4. The capital goods threshold (€1,160 gross) is the statutory amount as of March 2026. Verify this has not been amended by Ministerial notice before each tax year.
5. The Article 11 threshold (€35,000) is as of the current year. Verify annually.
6. Red flag thresholds (€3,000 single transaction, €200 tax-delta, €5,000 absolute position) are conservative starting values for Malta's typical self-employed client profile — not empirically calibrated.
7. Airbnb and short-term rental classification (EC5 in v1.0) is Tier 2 in all cases due to duration uncertainty. A future version should add an inference rule based on payment frequency patterns.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with three-tier Accora architecture. Quick reference moved to top (Section 1). Supplier pattern library restructured as literal lookup tables (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue restructured to compressed format (Section 6). Excel working paper specification added (Section 7). Bank statement reading guide added (Section 8). Onboarding moved to fallback role with inference rules (Section 9). Reference material moved to bottom (Section 10). Companion skill references updated to vat-workflow-base v0.1 and eu-vat-directive v0.1.
<<<<<<< HEAD
- **v1.0 (March 2026):** Initial skill. Standalone monolithic document covering Malta VAT Act Chapter 406, box mappings, reverse charge mechanics, blocked categories, edge case registry, and test suite. Validated by Michael Cutajar and Kevin Farrugia.
=======
- **v1.0 (March 2026):** Initial skill. Standalone monolithic document covering Malta VAT Act Chapter 406, box mappings, reverse charge mechanics, blocked categories, edge case registry, and test suite.
>>>>>>> 70c2582 (Update accounting project files)

### Self-check (v2.0 of this document)

1. Quick reference at top with box table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples drawn from non-test data (hypothetical IT consultant): yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 15 rules).
5. Tier 2 catalogue compressed with inference rules: yes (Section 6, 15 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only, inference rules first: yes (Section 9, 10 items).
8. All 8 Malta-specific refusals present: yes (Section 2, R-MT-1 through R-MT-8).
9. Reference material at bottom: yes (Section 10).
10. Entertainment hard-block (no Bewirtung exception) explicit: yes (Section 5.12 + Example 3).
11. Motor vehicle hard-block explicit: yes (Section 5.12 + Example 6).
12. Capital goods gross threshold test explicit: yes (Section 5.11 + Example 4).
13. EU B2B service sale (Box 1) and USt-IdNr verification explicit: yes (Example 5).
14. Non-EU SaaS reverse charge (Box 11/15) explicit: yes (Example 1 + Section 3.9).
15. Article 11 simplified mode explicit: yes (Section 5.13).

## End of Malta VAT Return Skill v2.0

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture) AND `eu-vat-directive` v0.1 or later (Tier 2, EU directive content). Do not attempt to produce a VAT3 without all three files loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
