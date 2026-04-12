---
name: netherlands-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Netherlands VAT return (OB aangifte / btw-aangifte) for a self-employed individual or small business in the Netherlands. Trigger on phrases like "prepare OB aangifte", "Dutch VAT return", "BTW aangifte", "classify transactions for Dutch VAT", or any request involving Netherlands VAT filing. This skill covers the Netherlands only, standard BTW regime. Kleineondernemersregeling (KOR), partial exemption, margin scheme (margeregeling), and VAT groups (fiscale eenheid) are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Dutch VAT work.
version: 2.0
---

# Netherlands VAT Return Skill (OB Aangifte / BTW) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Standard rate | 21% |
| Reduced rate | 9% (food and drinks, books, medicines, hotels, cultural events, passenger transport, hairdressers, repairs of bicycles/shoes/clothing) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods) |
| Return form | OB aangifte (Omzetbelasting aangifte) — rubrieken 1 through 5 |
| Filing portal | https://www.belastingdienst.nl (Mijn Belastingdienst Zakelijk) |
| Authority | Belastingdienst |
| Currency | EUR only |
| Filing frequencies | Quarterly (standard); Monthly (if assigned by Belastingdienst or on request); Annual (if assigned) |
| Deadline | Last business day of the month following the period (e.g. Q1 due 30 April) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants contributors |
| Validation date | April 2026 |

**Key OB aangifte rubrieken (the boxes you will use most):**

| Rubriek | Meaning |
|---|---|
| 1a | Supplies/services taxed at 21% (omzet + BTW) |
| 1b | Supplies/services taxed at 9% (omzet + BTW) |
| 1c | Supplies/services taxed at other rates (omzet + BTW) |
| 1d | Private use (privégebruik) and other internal supplies (omzet + BTW) |
| 1e | Supplies/services taxed at 0% or not taxed (omzet only) |
| 2a | Supplies/services to EU countries (intracommunautaire leveringen/diensten, omzet only) |
| 3a | Acquisitions from EU countries (omzet + BTW) |
| 3b | Acquisitions from outside EU (omzet + BTW) |
| 4a | Supplies/services from EU countries — reverse charge received (omzet + BTW) |
| 4b | Supplies/services from outside EU — reverse charge received (omzet + BTW) |
| 5a | Total BTW due (verschuldigde omzetbelasting) |
| 5b | Total deductible BTW (voorbelasting) |
| 5c | Sub-total (5a minus 5b) |
| 5d | Reduction under KOR (only if KOR applies — we refuse this) |
| 5e | Estimated result from prior period |
| 5f | Total to pay / to receive |
| 5g | Total to pay / to receive |

**Conservative defaults — Netherlands-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 21% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Netherlands |
| Unknown B2B vs B2C status for EU customer | B2C, charge 21% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (rubriek 4b) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | €5,000 |
| HIGH tax-delta on a single conservative default | €400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | €10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Dutch or international business bank: ING, ABN AMRO, Rabobank, SNS Bank, ASN Bank, Triodos Bank, Bunq, Knab, Revolut Business, Wise Business, N26 Business, or any other.

**Recommended** — sales invoices for the period (especially for intra-EU B2B services and zero-rated supplies), purchase invoices for any input BTW claim above €400, the client's BTW-id in writing (NL + 9 digits + B + 2 digits).

**Ideal** — complete invoice register, prior period OB aangifte, reconciliation of any prior period credit.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement at all → hard stop. If bank statement only → proceed but record in reviewer brief: "This OB aangifte was produced from bank statement alone. Reviewer must verify input BTW claims above €400 are supported by compliant invoices and reverse-charge classifications match supplier invoices."

### Netherlands-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13.

**R-NL-1 — Kleineondernemersregeling (KOR).** *Trigger:* client is registered under the KOR (small business scheme, turnover below €20,000). *Message:* "KOR-registered businesses are exempt from charging BTW and cannot recover input BTW. They do not file OB aangiften. This skill covers the standard BTW regime only. If you have opted out of KOR, please confirm."

**R-NL-2 — Partial exemption (pro rata / BUA).** *Trigger:* client makes both taxable and exempt-without-credit supplies and the exempt proportion is not de minimis. *Message:* "You make both taxable and exempt supplies. Input BTW must be apportioned under the pro rata (Art. 11 Wet OB 1968) or BUA (Besluit Uitsluiting Aftrek) rules. Please use a belastingadviseur."

**R-NL-3 — Margin scheme (margeregeling).** *Trigger:* client deals in second-hand goods, art, antiques, or collectables. *Message:* "Margeregeling transactions require transaction-level margin computation. Out of scope."

**R-NL-4 — Fiscal unity (fiscale eenheid).** *Trigger:* client is part of a fiscale eenheid BTW. *Message:* "Fiscale eenheden require consolidation. Out of scope."

**R-NL-5 — Fiscal representative.** *Trigger:* non-resident with a fiscal representative in the Netherlands. *Message:* "Non-resident registrations with fiscal representatives have specific obligations beyond this skill."

**R-NL-6 — BES islands filing.** *Trigger:* client is based in Bonaire, Sint Eustatius, or Saba. *Message:* "The BES islands have a separate ABB (Algemene Bestedingsbelasting) system, not BTW. This skill covers European Netherlands only."

**R-NL-7 — Real estate (BTW on onroerend goed).** *Trigger:* client deals in new property or opted for BTW on property lease. *Message:* "BTW on real estate is complex. Please use a belastingadviseur."

**R-NL-8 — Income tax instead of BTW.** *Trigger:* user asks about inkomstenbelasting or vennootschapsbelasting instead of BTW. *Message:* "This skill only handles Dutch BTW returns. For income tax, use a dedicated Dutch income tax skill."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. Match by case-insensitive substring. If none match, fall through to Section 5.

### 3.1 Dutch banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ING, ING BANK | EXCLUDE for bank charges/fees | Financial service, exempt |
| ABN AMRO, ABN | EXCLUDE for bank charges/fees | Same |
| RABOBANK, RABO | EXCLUDE for bank charges/fees | Same |
| SNS BANK, ASN BANK | EXCLUDE for bank charges/fees | Same |
| TRIODOS, BUNQ, KNAB | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| RENTE, INTEREST | EXCLUDE | Interest income/expense, out of scope |
| LENING, HYPOTHEEK | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Dutch government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| BELASTINGDIENST | EXCLUDE | Tax payment (BTW, IB, Vpb), not a supply |
| RIJKSOVERHEID | EXCLUDE | Government |
| GEMEENTE | EXCLUDE | Municipal fees/taxes |
| UWV | EXCLUDE | Employee insurance, social security |
| SVB | EXCLUDE | Social insurance bank |
| KVK, KAMER VAN KOOPHANDEL | EXCLUDE | Chamber of Commerce fees |
| RVO, RIJKSDIENST VOOR ONDERNEMEND | EXCLUDE | Government agency |
| DOUANE | EXCLUDE | Customs (but check for import BTW) |
| CBS, CENTRAAL BUREAU STATISTIEK | EXCLUDE | Government statistics |

### 3.3 Dutch utilities

| Pattern | Treatment | Rubriek | Notes |
|---|---|---|---|
| VATTENFALL | Domestic 21% | 5b (input) | Electricity/gas — standard rate |
| ENECO | Domestic 21% | 5b (input) | Energy |
| ESSENT | Domestic 21% | 5b (input) | Energy |
| GREENCHOICE | Domestic 21% | 5b (input) | Energy |
| NUON (now Vattenfall) | Domestic 21% | 5b (input) | Energy |
| KPN, KPN BV | Domestic 21% | 5b (input) | Telecoms/broadband — overhead |
| T-MOBILE NL, T-MOBILE NETHERLANDS | Domestic 21% | 5b (input) | Telecoms |
| VODAFONE NL, VODAFONE NETHERLANDS | Domestic 21% | 5b (input) | Telecoms |
| ZIGGO | Domestic 21% | 5b (input) | Cable/broadband |
| VITENS, DUNEA, EVIDES | Domestic 9% | 5b (input) | Water supply at reduced rate |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ACHMEA, CENTRAAL BEHEER, INTERPOLIS | EXCLUDE | Insurance, exempt |
| NATIONALE NEDERLANDEN, NN | EXCLUDE | Same |
| AEGON, ASR | EXCLUDE | Same |
| UNIVÉ, CZ, MENZIS, VGZ, ZILVEREN KRUIS | EXCLUDE | Health insurance, exempt |
| VERZEKERING, PREMIE | EXCLUDE | All insurance exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Rubriek | Notes |
|---|---|---|---|
| POSTNL (standard mail) | EXCLUDE for standard postage | | Universal postal service, exempt |
| POSTNL (parcels) | Domestic 21% | 5b | Non-universal services taxable |
| DHL EXPRESS NL, DHL PARCEL | Domestic 21% | 5b | Express courier |
| DPD, GLS NETHERLANDS | Domestic 21% | 5b | Courier |
| UPS NEDERLAND | Domestic 21% | 5b | Courier |

### 3.6 Transport (Netherlands domestic)

| Pattern | Treatment | Rubriek | Notes |
|---|---|---|---|
| NS, NEDERLANDSE SPOORWEGEN | Domestic 9% | 5b (input) | Rail transport at reduced rate |
| GVB, RET, HTM, CONNEXXION, ARRIVA | Domestic 9% | 5b (input) | Public transport, reduced rate |
| OV-CHIPKAART | Domestic 9% | 5b (input) | Public transport card top-up |
| UBER NL, UBER NETHERLANDS | Domestic 9% (transport) | 5b | Ride-hailing |
| BOLT NL | Domestic 9% | 5b | Ride-hailing |
| KLM (domestic) | Domestic 21% | 5b | Domestic flights at standard rate |
| KLM, TRANSAVIA, EASYJET (international) | EXCLUDE / 0% | | International flights exempt |
| TAXI | Domestic 9% | 5b | Local taxi, reduced rate |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| ALBERT HEIJN, AH | Default BLOCK input BTW | Personal provisioning. |
| JUMBO, LIDL, ALDI, PLUS | Default BLOCK | Same |
| DIRK, DEKAMARKT, HOOGVLIET | Default BLOCK | Same |
| RESTAURANT, EETCAFE, CAFE | Default BLOCK | Entertainment — see Section 5.12 |

### 3.8 SaaS — EU suppliers (reverse charge, rubriek 4a)

| Pattern | Billing entity | Rubriek | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 4a + 5b | Reverse charge: output in 5a via 4a, input in 5b |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 4a + 5b | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 4a + 5b | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 4a + 5b | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 4a + 5b | Reverse charge |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 4a + 5b | EU reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 4a + 5b | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 4a + 5b | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 1a (domestic!) | NL entity — domestic 21%, NOT reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 4a + 5b | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | 4a + 5b | Transaction fees may be exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge, rubriek 4b)

| Pattern | Billing entity | Rubriek | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 4a + 5b | LU entity → EU reverse charge |
| NOTION | Notion Labs Inc (US) | 4b + 5b | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 4b + 5b | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 4b + 5b | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 4b + 5b | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 4b + 5b | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | 4b + 5b | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or IE — check | 4b or 4a | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 4b + 5b | Non-EU reverse charge |

### 3.10 SaaS — the exception (NOT reverse charge)

| Pattern | Treatment | Why |
|---|---|---|
| ATLASSIAN (NL entity) | Domestic 21% rubriek 1a / 5b | Atlassian Network Services BV is a Dutch entity — domestic purchase, not reverse charge. |
| AWS EMEA SARL | EU reverse charge rubriek 4a + 5b (LU entity) | Standard EU reverse charge. If invoice shows Dutch BTW, treat as domestic 21%. |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU reverse charge 4a + 5b | Stripe IE entity |
| MOLLIE | Domestic 21% or EXCLUDE | Check — Mollie BV is Dutch; transaction fees exempt, subscription fees taxable |
| ADYEN | Domestic 21% or EXCLUDE | Adyen NV is Dutch; same distinction |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Dutch: domestic; if IE: reverse charge |

### 3.12 Professional services (Netherlands)

| Pattern | Treatment | Rubriek | Notes |
|---|---|---|---|
| ACCOUNTANT, BELASTINGADVISEUR | Domestic 21% | 5b | Always deductible |
| ADVOCAAT, ADVOCATENKANTOOR | Domestic 21% | 5b | Deductible if business legal matter |
| NOTARIS, NOTARISKANTOOR | Domestic 21% | 5b | Deductible if business |
| ADMINISTRATIEKANTOOR | Domestic 21% | 5b | Bookkeeper |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| UWV, WERKNEMERSVERZEKERINGEN | EXCLUDE | Employee insurance contributions |
| LOONHEFFING, LOONBELASTING | EXCLUDE | Payroll tax remittance |
| SALARIS, LOON | EXCLUDE | Wages — outside BTW scope |
| PENSIOEN, ABP, PFZW | EXCLUDE | Pension contributions |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| HUUR BEDRIJFSPAND, KANTOORHUUR | Domestic 21% | Commercial lease where landlord opted for BTW (optie belaste verhuur) |
| HUUR, HUURPRIJS (residential) | EXCLUDE | Residential lease exempt |
| OZB, ONROERENDEZAAKBELASTING | EXCLUDE | Property tax, not a supply |
| WOZ | EXCLUDE | Property valuation, not a supply |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OVERBOEKING EIGEN REKENING | EXCLUDE | Internal movement |
| SPAARREKENING, NAAR SPAREN | EXCLUDE | Own savings transfer |
| DIVIDEND | EXCLUDE | Dividend payment, out of scope |
| AFLOSSING, AFLOSSING LENING | EXCLUDE | Loan repayment |
| GELDOPNAME, PINOPNAME | TIER 2 — ask | Default exclude; ask what cash was spent on |
| STORTING, PRIVÉSTORTING | EXCLUDE | Owner injection |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Netherlands-based self-employed IT consultant (zzp'er, standard BTW regime).

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). No BTW on the invoice. This is a service from a non-EU supplier. The Dutch client must self-assess BTW (verlegging) under Art. 12 lid 2 Wet OB. Output BTW on rubriek 4b, input BTW on rubriek 5b. Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubriek (input) | Rubriek (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.08 | 21% | 5b | 4b | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
Google Ireland Limited is an IE entity — EU reverse charge (verlegging). Output BTW on rubriek 4a, input BTW on rubriek 5b. Net effect zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubriek (input) | Rubriek (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 178.50 | 21% | 5b | 4a | N | — | — |

### Example 3 — Entertainment, BUA blocked

**Input line:**
`15.04.2026 ; RESTAURANT DE KAS AMSTERDAM ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant transaction. In the Netherlands, the Besluit Uitsluiting Aftrek (BUA) blocks deduction of BTW on business entertainment (relatiegeschenken, spijzen en dranken) unless it relates to staff meals in specific circumstances. Business meals with external relations (zakenrelaties) have blocked BTW under Art. 1 lid 1 sub c BUA. Default: block. If this is a staff canteen or company event → may be deductible.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubriek | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANT DE KAS AMSTERDAM | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Restaurant: BUA blocks BTW on business entertainment. Staff event or external?" |

### Example 4 — Capital goods (bedrijfsmiddel)

**Input line:**
`18.04.2026 ; DELL NETHERLANDS BV ; DEBIT ; Invoice DEL2026-0041 Laptop XPS 15 ; -1,595.00 ; EUR`

**Reasoning:**
The gross amount is €1,595. In the Netherlands, capital goods (bedrijfsmiddelen) used for business are subject to BTW correction over the herzieningsperiode (5 years movable, 10 years immovable). There is no minimum threshold for capitalisation for BTW purposes — the herzieningsregeling applies to goods used for more than one year. Input BTW is deductible in full on rubriek 5b at time of purchase (for fully taxable businesses). The distinction matters for BUA and herzieningsregeling tracking.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubriek | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DELL NETHERLANDS BV | -1,595.00 | -1,318.18 | -276.82 | 21% | 5b | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice NL-2026-018 IT consultancy March ; +3,500.00 ; EUR`

**Reasoning:**
Incoming €3,500 from a German company. B2B services: place of supply is customer's country (Germany) under Art. 6 lid 1 Wet OB / Art. 44 VAT Directive. Client invoices at 0% with "BTW verlegd" (reverse charge). Report on rubriek 2a (intracommunautaire diensten). No output BTW. Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubriek | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 2a | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, BUA correction

**Input line:**
`28.04.2026 ; LEASE PLAN NEDERLAND ; DEBIT ; Lease payment VW Golf ; -550.00 ; EUR`

**Reasoning:**
Car lease payment. In the Netherlands, BTW on car leases IS deductible at the time of purchase/lease (unlike Malta's hard block). However, the BUA requires a correction at year-end for private use (privégebruik). The correction is 2.7% of the catalogue value (cataloguswaarde) of the car per year, or actual private use percentage. For a zzp'er with mixed use: deduct BTW fully now, correct at year-end via rubriek 1d (privégebruik). Default: deduct in full, flag for year-end BUA correction.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Rubriek | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | LEASE PLAN NEDERLAND | -550.00 | -454.55 | -95.45 | 21% | 5b | Y | Q3 | "Car: BTW deductible now, year-end BUA privégebruik correction needed. What is the cataloguswaarde?" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 21% (Art. 9 lid 1 Wet OB)

Default rate. Sales → rubriek 1a. Purchases → rubriek 5b.

### 5.2 Reduced rate 9% (Tabel I bij Wet OB)

Applies to: food and non-alcoholic drinks (on-premises and takeaway), books (print and digital), medicines, hotels, camping, cultural events (museums, cinema, theatre), passenger transport, hairdressers, repairs of bicycles/shoes/clothing/household linen. Sales → rubriek 1b. Purchases → rubriek 5b.

### 5.3 Zero rate and exempt with credit

Exports outside EU → rubriek 1e (zero-rated). Intra-EU B2B supplies of goods → rubriek 2a (intracommunautaire levering, zero-rated with VIES verification). Intra-EU B2B services → rubriek 2a (diensten, place of supply customer's country).

### 5.4 Exempt without credit (Art. 11 Wet OB)

Medical/paramedical, education, insurance, financial services, residential rent, postal universal service, cultural/sporting (in some cases), child care. No output BTW, no input deduction. If significant → **R-NL-2 refuses**.

### 5.5 Local standard purchases

Input BTW on a compliant invoice from a Dutch supplier is deductible. Map to rubriek 5b.

### 5.6 Reverse charge — EU services received (verlegging, Art. 12 lid 2)

EU supplier invoices at 0% with reverse charge: output BTW on rubriek 4a, input BTW on rubriek 5b. Net effect zero.

### 5.7 Reverse charge — EU goods received (intracommunautaire verwerving)

Goods from EU: output BTW on rubriek 3a, input BTW on rubriek 5b.

### 5.8 Reverse charge — non-EU

Non-EU services and goods: output BTW on rubriek 4b, input BTW on rubriek 5b.

### 5.9 Capital goods (bedrijfsmiddelen / herzieningsregeling)

No minimum threshold for BTW capitalisation. Herzieningsperiode: 5 years movable, 10 years immovable (Art. 13 Uitvoeringsbeschikking OB). Input BTW deductible in full at purchase for fully taxable businesses. Corrections for change of use over the herzieningsperiode.

### 5.10 BUA — Besluit Uitsluiting Aftrek (blocked deductions)

The BUA blocks deduction of BTW on:
- Business gifts (relatiegeschenken) to external parties if total per recipient > €227 per year. Below → deductible.
- Food, drink, tobacco provided in connection with external business relations (entertainment).
- Private use of company car (privégebruik auto): correct at year-end via rubriek 1d. Correction = 2.7% of cataloguswaarde per year (or actual private use %).
- Staff provisions: meals at workplace, canteen → partially blocked if below cost.
- Accommodation for external relations → blocked.
- NOTE: unlike Malta's hard block on entertainment, the Netherlands blocks via BUA year-end correction mechanism. BTW is initially deductible, then corrected.

### 5.11 Private use correction (rubriek 1d)

At year-end (or in Q4 / last period), the client must declare output BTW on private use of business goods via rubriek 1d. Most common: car (2.7% cataloguswaarde), phone, home office.

### 5.12 Intracommunautaire opgave (ICP — Listing)

In addition to the OB aangifte, if the client makes intra-EU supplies, they must file an ICP (Intracommunautaire opgave) listing the EU customers and amounts. This is separate from the OB aangifte but the data comes from the same rubriek 2a transactions. Flag for reviewer.

### 5.13 Sales — local domestic

Charge 21% or 9% as applicable. Map to rubriek 1a or 1b.

### 5.14 Sales — cross-border B2C

Above €10,000 EU-wide → **R-EU-5 OSS refusal fires**. Below → Dutch BTW.

### 5.15 Import BTW

Since 2023, businesses with an Art. 23 licence (vergunning) can defer import BTW to the OB aangifte instead of paying at customs. Output on rubriek 3b or 4b, input on 5b.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* SHELL, BP, ESSO, TANGO, TINQ. *Default:* deductible in full, flag for BUA year-end correction. *Question:* "What is the cataloguswaarde of the car? What % private use?"

### 6.2 Restaurants and entertainment

*Pattern:* restaurant, eetcafe, hotel. *Default:* block (BUA). *Question:* "Staff event or external business entertainment?"

### 6.3 Ambiguous SaaS billing entities

*Default:* non-EU reverse charge rubriek 4b. *Question:* "Check invoice for legal entity and country."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Default:* exclude as owner injection. *Question:* "Customer payment, own money, or loan?"

### 6.5 Incoming transfers from individual names

*Default:* domestic B2C 21%. *Question:* "Sale? Business or consumer?"

### 6.6 Incoming transfers from foreign counterparties

*Default:* domestic 21%. *Question:* "B2B with BTW-id, B2C, goods or services, which country?"

### 6.7 Large one-off purchases

*Default:* deductible, flag for herzieningsregeling tracking. *Question:* "Confirm invoice amount."

### 6.8 Mixed-use phone, internet, home office

*Default:* 0% if mixed. *Question:* "Dedicated business line or mixed-use? Business %?"

### 6.9 Outgoing transfers to individuals

*Default:* exclude. *Question:* "Contractor, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Pattern:* geldopname, pinopname. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Default:* no BTW (residential). *Question:* "Commercial property with BTW option (optie belaste verhuur)?"

### 6.12 Foreign hotel and accommodation

*Default:* exclude from input BTW. *Question:* "Business trip?"

### 6.13 Airbnb income

*Default:* [T2] flag. *Question:* "Short-stay rental? Duration? Tourist tax (toeristenbelasting)?"

### 6.14 Domestic reverse charge (construction)

*Pattern:* aanneming, onderaanneming, construction. *Why insufficient:* the Netherlands has domestic verlegging for construction subcontracting (Art. 12 lid 5 Wet OB). *Default:* [T2] flag. *Question:* "Construction subcontractor with verlegging?"

### 6.15 Platform sales

*Default:* if EU cross-border above €10,000 → R-EU-5. Otherwise: domestic 21% for sales; platform fees as EU reverse charge. *Question:* "Sell outside Netherlands?"

---

## Section 7 — Excel working paper template (Netherlands-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Netherlands overlay.

### Sheet "Transactions"

Column H accepts rubriek codes from Section 1. For reverse charge, enter both (e.g. "4a/5b").

### Sheet "Rubriek Summary"

```
| 1a | Omzet 21% + BTW | =SUMIFS(...) |
| 1b | Omzet 9% + BTW | =SUMIFS(...) |
| 1e | 0% / niet belast | =SUMIFS(...) |
| 2a | Intracommunautaire prestaties | =SUMIFS(...) |
| 3a | Verwervingen uit EU | =SUMIFS(...) |
| 4a | Verlegging EU | =SUMIFS(...) |
| 4b | Verlegging niet-EU | =SUMIFS(...) |
| 5a | Verschuldigde BTW | =SUM(BTW on 1a,1b,1d,3a,4a,4b) |
| 5b | Voorbelasting | =SUM(deductible input BTW) |
| 5c | Subtotaal | =5a - 5b |
| 5g | Te betalen / te ontvangen | =5c + 5e |
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/netherlands-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Dutch bank statement reading guide

**CSV format conventions.** Dutch banks export in CSV with comma or semicolon delimiters and DD-MM-YYYY dates. Common columns: Datum, Naam/Omschrijving, Rekening, Tegenrekening, Bedrag, Mutatiesoort, Mededelingen. ING uses YYYYMMDD in their CSV.

**Dutch language variants.** Huur (rent), salaris/loon (salary), rente (interest), overboeking (transfer), factuur (invoice), terugbetaling (refund), storting (deposit), opname (withdrawal). Treat as English equivalents.

**Mutatiesoort codes.** BA = betaalautomaat (card payment), GT = girale telebankieropdracht (bank transfer), IC = incasso (direct debit), OV = overboeking (internal transfer), ST = storting (deposit). These help classify.

**Internal transfers.** "Overboeking eigen rekening", "naar spaarrekening". Always exclude.

**Belastingdienst payments.** Tax payments appear as "BELASTINGDIENST" with a specific aanslagnummer. Always exclude.

**Foreign currency.** Convert to EUR at transaction date ECB rate.

**IBAN prefix.** NL = Netherlands. IE, LU, FR, DE = EU. US, GB, AU, CH = non-EU.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* BV = company; eenmanszaak = sole trader; VOF = partnership; zzp'er = freelancer. *Fallback:* "Eenmanszaak, BV, VOF, or zzp'er?"

### 9.2 BTW regime
*Inference rule:* if filing OB aangifte, they are standard regime. *Fallback:* "Standard BTW regime or KOR?"

### 9.3 BTW-id
*Fallback:* "What is your BTW-id? (NL + 9 digits + B + 2 digits)"

### 9.4 Filing period
*Fallback:* "Which quarter/month?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* UWV, loonheffing outgoing. *Fallback:* "Employees?"

### 9.7 Exempt supplies
*Fallback:* "Any exempt sales?" *If yes → R-NL-2.*

### 9.8 Credit carried forward
*Always ask.* "BTW credit from prior period?"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Netherlands? EU/non-EU? B2B/B2C?"

### 9.10 Art. 23 import licence
*Conditional fallback:* "Do you have an Art. 23 vergunning for deferred import BTW?"

---

## Section 10 — Reference material

### Validation status

v2.0, April 2026, three-tier Accora architecture.

### Sources

1. Wet op de omzetbelasting 1968 (Wet OB) — https://wetten.overheid.nl
2. Uitvoeringsbeschikking OB 1968 — herzieningsregeling
3. Besluit Uitsluiting Aftrek omzetbelasting 1968 (BUA)
4. Belastingdienst OB aangifte guidance — https://www.belastingdienst.nl
5. Council Directive 2006/112/EC — via eu-vat-directive companion skill
6. VIES — https://ec.europa.eu/taxation_customs/vies/

### Known gaps

1. KOR details not covered (R-NL-1 refuses).
2. BUA year-end correction calculation is simplified (2.7% cataloguswaarde).
3. Art. 23 import deferral details are flagged T2 only.
4. Herzieningsregeling tracking requires multi-year data.
5. ICP listing is flagged but not generated.
6. Domestic construction verlegging flagged T2 only.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. 10 sections.
- **v1.0/1.1:** Initial skill.

### Self-check (v2.0)

1. Quick reference with rubrieken table: yes.
2. Supplier library (15 sub-tables): yes.
3. Worked examples (6): yes.
4. Tier 1 rules (15): yes.
5. Tier 2 catalogue (15): yes.
6. Excel template: yes.
7. Onboarding fallback (10): yes.
8. 8 refusals: yes.
9. Reference material: yes.
10. BUA mechanism (key NL difference from Malta hard block): yes.
11. Privégebruik auto correction via rubriek 1d: yes.
12. Atlassian NL entity exception: yes.
13. EU B2B services on rubriek 2a: yes.
14. Non-EU SaaS reverse charge rubriek 4b: yes.
15. Art. 23 import deferral mentioned: yes.

## End of Netherlands VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a belastingadviseur, registeraccountant, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
