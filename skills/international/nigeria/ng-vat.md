---
name: ng-vat
description: "Use this skill whenever asked to prepare, review, classify transactions for, or advise on Nigerian VAT (Value Added Tax) for self-employed individuals, sole traders, partnerships, or small companies operating in Nigeria. Trigger on phrases like \"Nigeria VAT\", \"FIRS VAT\", \"VAT Nigeria 7.5%\", \"VAT return Nigeria\", \"VAT Form 002\", \"TaxPro Max\", \"e-invoicing FIRS\", \"Merchant Buyer System\", \"MBS Nigeria\", \"VAT Act Nigeria\", \"NTA 2025 VAT\", \"Nigeria Tax Act 2025\", \"Section 10 VAT Act\", \"non-resident digital services Nigeria\", \"reverse charge Nigeria\", \"WHT-VAT Nigeria\", or any request involving Nigerian VAT registration, computation, classification, filing, or compliance. Covers the 7.5% standard rate under the VAT Act (as amended by Finance Acts 2019/2020/2021/2023) and the consolidation under the Nigeria Tax Act 2025 framework effective 1 January 2026, the NGN 25 million registration threshold, monthly Form VAT 002 filing to FIRS by the 21st of the following month via TaxPro Max, the FIRS Merchant Buyer Solution (MBS) phased e-invoicing mandate (large taxpayers from Q3 2024, medium taxpayers through 2025-2026), non-resident digital service registration under Section 10A, reverse-charge self-accounting on imported services, and WHT-VAT interaction on government and large-taxpayer contracts. Out of scope (refusal catalogue): excise duties, Petroleum Profit Tax, Companies Income Tax, transfer pricing, refund litigation, free trade zone (FTZ) treatment, state-level consumption taxes, real estate VAT, and VAT grouping. ALWAYS read this skill before touching any Nigerian VAT work."
jurisdiction: NG
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ng-vat

## Nigeria — VAT (Value Added Tax) — Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Omolola Fasasi** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### ng-vat

- **Standard VAT rate** — 7.5%  _(Finance Act 2019, effective 1 February 2020)_
- **Pre-2020 (superseded) VAT rate — no longer applicable** — 5%  _(Finance Act 2020)_
- **Zero rate — exports and specified supplies** — 0%  _(Finance Act 2021)_
- **Reverse-charge rate on imported services** — 7.5%  _(Section 10 VATA / NTA 2025)_
- **Compulsory VAT registration threshold (annual turnover)** — NGN 25,000,000  _(Finance Act 2019, effective 2020)_
- **Compulsory VAT registration threshold (annual turnover)** — NGN 100m  _(Nigeria Tax Act (NTA) 2025)_
- **Below-threshold exemption from VAT registration and filing** — Annual turnover ≤ NGN 25,000,000  _(Finance Act 2019, effective 2020)_
- **VAT return form** — VAT Form 002
- **Filing frequency** — Monthly (including nil returns)
- **VAT return filing and payment deadline** — 21st of the following month
- **TIN digit length** — 10 digits
- **Current unified statute** — Nigeria Tax Act (NTA) 2025, effective 1 January 2026  _(Nigeria Tax Act (NTA) 2025)_
- **Current unified statute** — Nigeria Tax Act (NTA) 2025, effective 1 January 2026  _(Nigeria Tax Act (NTA) 2025)_
- **VAT Form 002 Line 2 — Output VAT formula** — OUTPUT VAT =TOTAL(TAXABLE SALES * TAX RATE)
- **VAT Form 002 Line 6 — Net VAT payable formula** — NET VAT PAYABLE = TOTAL OUTPUT TAX -TOTAL INPUT TAX
- **Foreign currency invoice conversion rate** — CBN official rate on date of supply
- **HIGH single transaction** — NGN 10,000,000
- **Input VAT credit — unknown business-use portion (mixed personal/business)** — you can only claim input VAT credit for the business-use portion of mixed expense
- **Input VAT credit — supplier not displaying VRN on invoice** — No input credit (input claim not supported)
- **Zero-rate: exports of goods (documentation requirement — form)** — Form NXP, shipping documents and foreign exchange evidence required
- **Zero-rate: exported services — legislative basis** — Section 10A VATA; FIRS Information Circular 2021/02  _(Nigeria Tax Act (NTA) 2025)_
- **Zero-rate: humanitarian donor organisations — effective legislation** — All NGOs are expected to register for tax purposes, obtain tax identification number and file annual company income tax (CIT) with the nigerian revenue service (NRS)  _(Nigeria Tax Act (NTA) 2025)_
- **Reverse-charge: foreign digital services (B2B) — default classification** — 7.5% reverse-charge — buyer self-assesses under Section 10  _(Nigeria Tax Act (NTA) 2025)_
- **Reverse-charge: treatment for fully taxable business (net VAT effect)** — 0.075  _(Nigeria Tax Act (NTA) 2025)_
- **NRS cash refund processing time (in practice)** — 30 TO 90 DAYS  _(Nigeria Tax Act (NTA) 2025)_
- **VAT return excess input credit — treatment when refund not claimed** — Excess is automatically treated as an accumulated credit  _(Nigeria Tax Act (NTA) 2025)_
- **Processed/packaged food VAT treatment** — 7.5% (standard-rated)  _(Nigeria Tax Act (NTA) 2025)_
- **Stationery VAT treatment** — 7.5% (standard-rated)  _(Nigeria Tax Act (NTA) 2025)_
- **Commercial freight VAT treatment** — 7.5% (standard-rated)  _(Nigeria Tax Act (NTA) 2025)_
- **Pharmaceutical products — exemption condition** — Tax exempt  _(Nigeria Tax Act (NTA) 2025)_
- **Filing portal** — taxpayer self service (NSS) portal  _(Nigeria Tax Act (NTA) 2025)_
- **e-Invoice system** — Operated by the Nigeria Revenue Service (NRS)  _(Nigeria Tax Act (NTA) 2025)_

## Section 1 — Quick reference

**Read this section in full before classifying any transaction. Nigeria operates a single federal Value Added Tax administered by FIRS. State and local governments do NOT levy VAT (Lagos and Rivers have attempted but the federal position holds pending Supreme Court resolution). Excise duties, Petroleum Profit Tax, Companies Income Tax (CIT), Capital Gains Tax, Stamp Duty, Withholding Tax and Education Tax are all separate regimes and are out of scope.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Federal Republic of Nigeria |
| Tax | Value Added Tax (VAT) |
| Currency | NGN (Nigerian Naira — ₦) |
| Standard rate | **7.5%** (raised from 5% by Finance Act 2019, effective 1 February 2020) |
| Zero rate | 0% on exports of goods and services, supplies to diplomatic missions, goods purchased by humanitarian donor organisations (Finance Act 2021) |
| Exempt | Basic food items (unprocessed agricultural produce), medical/pharmaceutical products (NAFDAC-registered), pharmaceutical raw materials, baby products, newspapers and educational materials, financial services (banking fees, insurance premiums), natural gas (domestic), residential rent, public transport, locally-produced agricultural equipment, fertilizers, plant and machinery for use in EPZs |
| Registration threshold | **NGN 25,000,000** annual turnover (Finance Act 2019, effective 2020). Below threshold — no obligation to register. Voluntary registration permitted. |
| Tax authority | Federal Inland Revenue Service (FIRS) |
| Filing portal | FIRS TaxPro Max — https://taxpromax.firs.gov.ng |
| Return form | **VAT Form 002** (monthly return) |
| Filing frequency | **Monthly** for all registered persons (including nil returns) |
| Deadline | **21st of the following month** (filing AND payment) |
| e-Invoice | **FIRS Merchant Buyer Solution (MBS)** — phased real-time clearance mandate (see Section 6) |
| Primary legislation (legacy) | Value Added Tax Act (VATA), Cap V1 LFN 2004, as amended by Finance Acts 2019, 2020, 2021, 2023 |
| Primary legislation (current) | **Nigeria Tax Act (NTA) 2025** — unified statute consolidating VAT, CIT, CGT, PIT and other federal taxes; effective 1 January 2026 |
| Identifier | Taxpayer Identification Number (TIN, 10 digits) and VAT registration certificate (VRN) |
| Contributor | Open Accountants Community |
| Validated by | Verified by Omolola Fasasi (MB058950) on 2026-06-21 |
| Skill version | 2.0 |

### Rate table at a glance

**Rate table at a glance**

| Rate | Application |
| --- | --- |
| **7.5%** | Default standard rate on all taxable supplies (goods and services) not specifically exempt or zero-rated |
| **0%** | Exports of goods, exported services, supplies to diplomats, humanitarian goods (post-Finance Act 2021) |
| **Exempt** | Basic unprocessed food, medical/pharmaceutical (NAFDAC-registered), baby products, financial services, insurance, residential rent, public transport, educational materials, newspapers, natural gas, locally-produced agricultural equipment, fertilizers |
| **Out of scope** | Salaries/wages, dividends, interest, loan principal, share capital, drawings |

### Key VAT Form 002 lines

**Key VAT Form 002 lines**

| Line | Meaning |
| --- | --- |
| Line 1 | Total taxable sales (net of VAT) |
| Line 2 | Output VAT (Line 1 × 7.5%) |
| Line 3 | Zero-rated sales |
| Line 4 | Exempt sales |
| Line 5 | Total input VAT (on purchases for taxable activities, supported by valid VAT invoices) |
| Line 6 | Net VAT payable (Line 2 − Line 5) |
| Line 7 | Excess input VAT carried forward (or claim refund — see Tier 2) |

### Conservative defaults — specific to Nigeria

**Conservative defaults — specific to Nigeria**

| Ambiguity | Default |
| --- | --- |
| Unknown supply classification | Standard-rated at 7.5% |
| Unknown whether food is processed or unprocessed | Treat as processed — 7.5% until confirmed |
| Unknown pharmaceutical exemption | 7.5% until NAFDAC registration number confirmed |
| Unknown export documentation status (NXP form, shipping docs) | Treat as domestic 7.5% |
| Unknown business-use portion (mixed personal/business) | 0% input credit |
| Foreign digital service (B2B) | 7.5% reverse-charge — buyer self-assesses under Section 10 |
| Unknown whether NGN 25M turnover threshold met | Assume must file |
| Mixed taxable / exempt supplies, apportionment unknown | No input credit on disputed portion; flag for reviewer |
| Supplier not displaying VRN on invoice | No input credit (input claim not supported) |
| Government counterparty | Flag for WHT-VAT review |
| Foreign currency invoice | Convert at CBN official rate on date of supply |

### Red-flag thresholds

**Red-flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH — single transaction value | NGN 10,000,000 |
| HIGH — tax delta from a single conservative default | NGN 750,000 |
| MEDIUM — counterparty concentration | >40% of output OR input |
| MEDIUM — conservative default count | >4 per return |
| LOW — absolute net VAT position | NGN 5,000,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF or pasted text, plus confirmation of VAT registration status and TIN. Acceptable from any Nigerian bank: GTBank, First Bank, Access Bank, Zenith Bank, UBA, Fidelity Bank, Stanbic IBTC, Union Bank, Ecobank, Wema, FCMB, Sterling, Polaris, Keystone, Heritage, or any other.

**Recommended** — sales invoices showing the supplier's VRN, purchase invoices from VAT-registered suppliers with their VRN displayed, prior month VAT return (for excess input credit carried forward), export documentation (Form NXP and shipping documents) for zero-rated exports, and details of exempt supplies with product descriptions.

**Ideal** — complete invoice register, TIN certificate, VAT registration certificate, WHT-VAT credit notes (for government supplies and large-taxpayer counterparties), MBS-cleared e-invoice JSON/XML files for the period (once the taxpayer is in scope of the e-invoicing mandate), and ledger of input VAT carried forward.

**Refusal policy on missing minimum — SOFT WARN.** If no bank statement and no invoices are available: full stop. If only bank statement and no invoices: proceed but record in the reviewer brief that "this return was produced solely from bank statement narrations; the reviewer must verify that every input VAT claim is supported by a valid VAT invoice from a VAT-registered supplier showing the supplier's VRN, otherwise FIRS will disallow the credit."

### Refusal catalogue — Nigeria-specific

- **R-NG-1 — Below registration threshold** — Businesses with annual turnover of NGN 25 million or less are exempt from VAT registration and filing obligations under Finance Act 2019 (effective 2020). Confirm turnover. If the business has voluntarily registered, treat as normal taxpayer; otherwise stop. (Trigger: business with annual turnover ≤ NGN 25,000,000 (Finance Act 2019/2020).)
- **R-NG-2 — VAT refund claims and litigation** — FIRS refund processes are lengthy (90+ days in practice), evidence-intensive, and frequently litigated. Out of scope. Escalate to a CITN-licensed tax practitioner; in the meantime carry the excess forward on Line 7. (Trigger: taxpayer asks for a cash refund from FIRS.)
- **R-NG-3 — Petroleum Profit Tax (PPT), Companies Income Tax (CIT), Education Tax** — This skill covers VAT only. PPT, CIT, EDT and other federal direct taxes are separate regimes under the Nigeria Tax Act 2025. Escalate. (Trigger: taxpayer asks about PPT, CIT, EDT, NITDA levy, NASENI levy, or police trust fund levy.)
- **R-NG-4 — Real estate VAT (land vs buildings)** — VAT on real estate involves complex exemption rules — land is exempt; buildings are taxable in some cases but exempt in others; commercial leases vs residential leases differ. Out of scope. Escalate to a CITN practitioner. (Trigger: taxpayer sells, buys or leases real estate.)
- **R-NG-5 — Free Trade Zone (FTZ) operations** — FTZ entities enjoy VAT exemptions on intra-zone and customs zone supplies but VAT applies on supplies into the customs territory. Specialised regime. Escalate. (Trigger: taxpayer operates in a Nigerian Export Processing Zone (NEPZA), Oil & Gas FTZ (OGFZA), Lekki FTZ, Calabar FTZ, etc.)
- **R-NG-6 — State-level consumption tax (Lagos / Rivers)** — The constitutional dispute between FIRS and certain states (Lagos, Rivers) over VAT collection remains pending Supreme Court resolution. For now, follow federal FIRS VAT. Escalate any state-level demand notices to a CITN-licensed tax practitioner. (Trigger: Lagos State Consumption Tax, Rivers State VAT, or any state-level VAT challenge to federal VAT.)
- **R-NG-7 — VAT grouping** — VAT grouping is not a recognised regime under the Nigerian VAT Act / NTA 2025. Each VAT-registered entity files separately. Escalate any group-structuring queries. (Trigger: request to treat related companies as a VAT group.)
- **R-NG-8 — ICMS-ST / margin schemes / second-hand goods** — Nigeria does not operate margin schemes or VAT substitution. All supplies are taxed on full consideration. Escalate any unusual valuation queries. (Trigger: request to apply a margin scheme or substitution regime.)
- **R-NG-9 — Tax tribunal defence or audit dispute** — Audit defence and tribunal representation are out of scope. Engage a CITN-licensed tax practitioner or a tax solicitor. (Trigger: taxpayer in active audit or before the Tax Appeal Tribunal.)
- **R-NG-10 — Excise duties on alcohol, tobacco, sugar-sweetened beverages, telecoms** — Excise duties (including the SSB sugar tax and telecoms excise reintroduced by Finance Act 2023 and amended under NTA 2025) are a separate regime administered partly by Customs and partly by FIRS. Out of scope. (Trigger: taxpayer manufactures or imports excisable goods.)

## Section 3 — Tier 1: taxable, exempt and zero-rated supplies

### 3.1 Standard-rated supplies (7.5%)

- **Standard-rated supplies (7.5%)** — Default treatment for any supply not specifically exempt or zero-rated. Examples include: - Consulting, IT, software (SaaS), engineering, advertising, marketing, legal, accounting, audit, architecture and other professional services rendered in Nigeria - Sale of finished goods (electronics, apparel, furniture, building materials, processed food, packaged consumer products) - Rental of commercial property and equipment - Telecommunications, broadband, cable TV, streaming subscriptions - Hospitality (hotels, restaurants — note: separate state consumption tax may also apply in Lagos/Rivers, see R-NG-6) - Domestic transportation of cargo and courier services - Repairs, maintenance, installation - Digital advertising (Google Ads, Meta Ads — also reverse-charge if billed from offshore entity)

### 3.2 Exempt supplies (no output VAT; no input credit recoverable on related purchases)

- **Exempt supplies list** — Listed in the First Schedule to the VAT Act and updated by Finance Acts. The non-exhaustive exempt list: - **Basic food items** — unprocessed agricultural produce (rice, beans, garri, yam, vegetables, cassava, maize, sorghum, millet). Processed/packaged food is 7.5%. - **Medical and pharmaceutical products** — NAFDAC-registered medicines, vaccines, medical consumables, hospital services - **Baby products** — diapers, infant formula, baby food - **Educational materials** — textbooks, school exercise books, educational journals, tuition fees (note: stationery is 7.5%) - **Newspapers and magazines** (print) - **Financial services** — banking fees, interbank charges, insurance premiums (note: IOF-style stamp duty applies separately) - **Insurance premiums** — life, general, motor, property - **Residential rent** — rental of residential accommodation - **Public transport** — passenger transport by road, rail, water (commercial freight is 7.5%) - **Plant and machinery imported for use in Export Processing Zones** - **Locally-produced agricultural equipment**, fertilizers, seedlings - **Natural gas** (domestic supply) - **Tractors, ploughs, and agricultural implements** - **Petroleum products** (subject to changes — verify under NTA 2025 implementing regulations)  _(First Schedule to the VAT Act)_

### 3.3 Zero-rated supplies (0% output VAT; input credit recoverable in full)

- **Zero-rated supplies list** — - **Exports of goods** — supported by Form NXP, shipping documents and foreign exchange evidence - **Exported services** — services rendered to a non-resident where the benefit accrues outside Nigeria (e.g., software development for an overseas client, consulting to a foreign company). Section 10A and FIRS Information Circular 2021/02. - **Diplomatic supplies** — goods and services to accredited diplomatic missions - **Humanitarian donor organisations** — Finance Act 2021 added this category **Documentation for zero-rate**: contract with non-resident; foreign currency invoice (raised in USD/EUR/GBP but VAT amount stated as zero); SWIFT/wire evidence of receipt; NXP form for goods; export bill of lading or airway bill.  _(Section 10A; FIRS Information Circular 2021/02; Finance Act 2021)_

### 3.4 Out of scope (not a supply at all)

- **Out of scope items** — - Salaries, wages, pensions - Dividends and distributions - Interest income (already exempt as financial service) - Loan principal and capital contributions - Penalty income (e.g., late-payment charges contractually agreed) - Donations and grants without supply of goods/services - Drawings by sole proprietors

## Section 4 — Tier 2: reviewer-judgement items

### 4.1 Reverse-charge on imported services (Section 10 VATA / NTA 2025)

- **Reverse-charge mechanics** — Services rendered by non-residents to Nigerian VAT-registered businesses trigger reverse-charge. The Nigerian recipient self-accounts for VAT at 7.5% on the consideration paid, declares it as **output VAT** on Line 2 and, where the service is used for fully taxable activities, simultaneously claims it as **input VAT** on Line 5 — netting to zero for fully taxable businesses. **Common scenarios:** - Software-as-a-Service from Microsoft Ireland, Google Cloud, AWS US, Adobe, Zoom, Slack, Notion, Figma, Canva, ChatGPT/Anthropic, Stripe (non-Nigerian entity), Salesforce - Foreign management fees, royalties, technical service fees - Foreign legal, consulting, marketing services - Digital advertising bought from Meta Ireland or Google Ireland **Practical computation example:** A Lagos consulting firm pays Microsoft Ireland NGN 11,200,000 for Azure services in April. The amount is gross of VAT. - Net (excluding VAT): 11,200,000 ÷ 1.075 = NGN 10,418,605 - Output VAT (self-assessed): 11,200,000 × 7.5/107.5 = NGN 781,395 - Input VAT (same amount, assuming fully taxable use): NGN 781,395 - Net VAT impact: zero - WHT (10% on royalty/technical service category, varies): typically separately remitted; consult WHT skill - IRRF-equivalent in Nigeria is WHT; not part of VAT  _(Section 10 VATA / NTA 2025)_

### 4.2 Non-resident digital service providers (Section 10A VATA / NTA 2025)

- **Non-resident digital service providers** — Non-resident suppliers of digital services to Nigerian consumers must register with FIRS, charge 7.5% VAT on B2C supplies, and remit monthly. The "VATGen" framework (FIRS Information Circular 2021/19) operationalises this. If the non-resident has not registered and has not charged VAT to a Nigerian VAT-registered business customer, the Nigerian recipient self-accounts under Section 10 (reverse-charge — see 4.1 above). **Practitioner checks:** - Does the supplier display a Nigerian VRN on their invoice? If yes, treat as ordinary domestic supply (no reverse-charge). - If the supplier has not registered and the customer is a Nigerian business, apply reverse-charge. - If the supplier has not registered and the customer is a Nigerian consumer, FIRS expects the supplier to register; reverse-charge does not apply to B2C.  _(Section 10A VATA / NTA 2025; FIRS Information Circular 2021/19)_

### 4.3 WHT-VAT interaction (government and large-taxpayer contracts)

- **WHT-VAT interaction** — Government MDAs (ministries, departments, agencies), oil & gas companies, and FIRS-designated "Large Taxpayers" are required to **withhold VAT at source** on payments to suppliers (typically the full 7.5%, treated as VAT remitted on behalf of the supplier). Some sectors also see a separate 5% WHT (income tax in nature, not VAT) deducted concurrently. **Practitioner treatment for the supplier:** - Output VAT is still declared on Line 2 in full - The amount withheld and remitted by the customer is treated as a credit and reduces the cash VAT to remit (claimed on Line 6 working) - Obtain a Withholding VAT Credit Note from the customer as evidence - File monthly even if WHT-VAT covers the entire month's output liability

### 4.4 Mixed taxable and exempt supplies — input apportionment

- **Mixed supplies apportionment** — When a business makes both taxable and exempt supplies: - Input VAT directly attributable to taxable supplies — fully recoverable - Input VAT directly attributable to exempt supplies — not recoverable - Residual input VAT (e.g., general overheads, rent, utilities of head office) — apportion by **revenue ratio**: (taxable revenue ÷ total revenue) × residual input VAT Flag for reviewer; document the apportionment method on the working paper.

### 4.5 Foreign currency invoicing

- **Foreign currency invoicing rule** — VAT must be reported in NGN. Use the **Central Bank of Nigeria (CBN) official exchange rate on the date of supply** (date of invoice). Where the invoice is in USD/EUR/GBP, convert the net consideration at the CBN rate, then apply 7.5%. Flag for reviewer on rate source and date.

### 4.6 Sector specials

**Sector specials**

| Sector | Treatment |
| --- | --- |
| **Oil & gas upstream** | Specialised regime; PPT applies on income, VAT applies on goods/services with restrictions. Escalate (R-NG-3 / R-NG-5). |
| **Telecommunications** | 7.5% VAT on services; **5% excise duty** (Finance Act 2023, amended under NTA 2025) also applies to telecom services in addition to VAT. Stack carefully. |
| **Banking and other financial services** | Exempt (no output VAT on interest, fees that are integral to the financial service). However, ancillary services (advisory, ATM card replacement fees in some readings) may attract VAT. |
| **Insurance** | Exempt (premiums). |
| **Hospitality (Lagos, Rivers)** | 7.5% federal VAT plus possible state consumption tax (Lagos 5%, Rivers VAT challenge). Tax stacking — coordinate with state advisor. |
| **Real estate** | Out of scope (R-NG-4). |
| **Export Processing Zones (EPZ)** | Out of scope (R-NG-5). |
| **e-Commerce platforms (Jumia, Konga, Shopee, Mercado Livre NG analogues)** | 7.5% on taxable goods; platforms generally collect and remit on behalf of marketplace sellers above threshold. |

## Section 5 — Worked examples

### Example 1 — Resident-to-resident services with NFS-equivalent

**Scenario:** Lagos-based IT consultancy invoices an Abuja corporate client for software development.

**Bank statement line (GTBank format):**
```
Date        : 15/04/2025
Narration   : CREDIT TRANSFER — ACME CORP LTD — INV-2025-041 — IT CONSULTING
Amount      : +NGN 5,375,000.00
Balance     : NGN 25,375,000.00
```

**Working:**
- Net invoice (exclusive of VAT): NGN 5,000,000
- Output VAT 7.5%: NGN 375,000
- Total invoice: NGN 5,375,000

**Form 002 entries**

| Line | Value (NGN) |
| --- | --- |
| Line 1 (taxable sales net) | 5,000,000 |
| Line 2 (Output VAT) | 375,000 |

### Example 2 — B2B with WHT-VAT interaction (government contract)

**Scenario:** Manufacturing firm in Kano invoices Federal Ministry of Health for medical supplies. Government MDA withholds VAT at source.

**Invoice:**
- Net: NGN 20,000,000
- Output VAT 7.5%: NGN 1,500,000
- Gross: NGN 21,500,000

**Payment received in bank:**
- Net of WHT-VAT: NGN 20,000,000 (the Ministry remits the NGN 1,500,000 VAT directly to FIRS)
- Also potentially less a 5% income WHT: NGN 1,000,000 (income WHT, separate; treated as advance income tax, not VAT)
- Cash to supplier: NGN 19,000,000

**Required evidence:** Withholding VAT Credit Note from the Ministry of Health.

**Form 002 entries**

| Line | Value (NGN) |
| --- | --- |
| Line 1 (taxable sales net) | 20,000,000 |
| Line 2 (Output VAT) | 1,500,000 |
| Line 5 (Input VAT — if any input on these supplies) | (separate) |
| WHT-VAT credit (claimed against Line 2 in payment computation) | 1,500,000 |
| **Net cash VAT payable on this transaction** | **NGN 0** (already remitted by MDA) |

### Example 3 — Non-resident digital service (reverse charge under Section 10)

**Scenario:** Lagos law firm pays Microsoft Ireland for Azure cloud services in April.

**Bank statement line (First Bank format):**
```
Date        : 05/04/2025
Narration   : INTL PAYMENT — MICROSOFT IRELAND — AZURE SERVICES APR 2025
Amount      : -NGN 11,200,000.00
```

**Working:**
- Total paid (treated as VAT-inclusive for self-assessment): NGN 11,200,000
- Self-assessed output VAT: 11,200,000 × 7.5/107.5 = NGN 781,395
- Self-assessed input VAT (fully taxable activity — law firm): NGN 781,395
- Net VAT impact: zero
- Note: foreign currency conversion at CBN rate on date of invoice

**Form 002 entries**

| Line | Value (NGN) |
| --- | --- |
| Line 2 (Output VAT — reverse charge) | 781,395 |
| Line 5 (Input VAT — reverse charge) | 781,395 |
| **Net VAT on this transaction** | **NGN 0** |

### Example 4 — Export of software (zero-rated)

**Scenario:** Nigerian tech company exports a software licence to a UK client.

**Bank statement line (UBA format):**
```
Date        : 20/04/2025
Narration   : SWIFT CREDIT — UK TECH LTD — SOFTWARE LICENSE Q1 2025
Amount      : +NGN 15,000,000.00 (USD 9,000)
```

**Working:**
- Export of service to non-resident — zero-rated under Section 10A and FIRS Circular 2021/02
- Required: contract, foreign-bank transfer evidence (SWIFT advice), NXP form not required for services but FX evidence is required

**Form 002 entries**

| Line | Value (NGN) |
| --- | --- |
| Line 3 (Zero-rated sales) | 15,000,000 |
| Line 2 (Output VAT) | 0 |
| Related input VAT on production costs | claimable in full on Line 5 |

### Example 5 — Exempt basic food sale

**Scenario:** Agricultural trader in Ogun sells unprocessed yams to a market wholesaler.

**Bank statement line (Zenith Bank format):**
```
Date        : 10/04/2025
Description : PAYMENT — ALABA MARKET TRADERS — FARM PRODUCE SUPPLY
Reference   : INV-AGR-2025-010
Amount      : +NGN 2,000,000.00
```

**Working:**
- Unprocessed agricultural produce — exempt from VAT (First Schedule VATA)
- No output VAT; no input VAT credit on related purchases (apportion residual inputs)

**Form 002 entries**

| Line | Value (NGN) |
| --- | --- |
| Line 4 (Exempt sales) | 2,000,000 |
| Line 2 (Output VAT) | 0 |

### Example 6 — Standard monthly return (consolidated)

**Scenario:** Manufacturing company in Aba — April 2025.

**Consolidated return table**

| Item | Net (NGN) | VAT (NGN) |
| --- | --- | --- |
| Domestic taxable sales | 50,000,000 | 3,750,000 |
| Export sales (0%) | 20,000,000 | 0 |
| Exempt sales (basic food line) | 10,000,000 | 0 |
| **Total output** | **80,000,000** | **3,750,000** |
| Input on taxable purchases (with VRN invoices) | 30,000,000 | 2,250,000 |
| **Net VAT payable (Line 6)** |  | **1,500,000** |

**Apportionment of residual inputs:** taxable+zero-rated = 70,000,000; total = 80,000,000; recovery ratio = 87.5%. Residual inputs adjusted accordingly.

### Example 7 — Nil return

**Scenario:** Dormant VAT-registered company with no activity in April.

**Working:**
- No supplies, no inputs
- **Nil return must still be filed by 21 May** to avoid the NGN 50,000 + NGN 25,000/month penalty

**Form 002:** all lines zero, submitted via TaxPro Max.

### Example 8 — Mixed supplies with apportionment

**Scenario:** A pharmacy sells both NAFDAC-registered medicines (exempt) and over-the-counter cosmetic items (taxable).

- Taxable supplies: NGN 3,000,000 (cosmetics)
- Exempt supplies: NGN 2,000,000 (medicines)
- Total residual input VAT (rent, electricity, general overhead): NGN 200,000 — not directly attributable

**Working:**
- Taxable ratio: 3,000,000 / 5,000,000 = 60%
- Recoverable residual input VAT: 200,000 × 60% = NGN 120,000
- Output VAT: 3,000,000 × 7.5% = NGN 225,000
- Net VAT payable: 225,000 − 120,000 = NGN 105,000

Flag for reviewer on apportionment method.

## Section 6 — e-Invoicing: FIRS Merchant Buyer Solution (MBS)

### 6.1 Overview

- **MBS overview** — The FIRS Merchant Buyer Solution (MBS) is Nigeria's national e-invoicing platform implementing **real-time invoice clearance** — every invoice issued by an in-scope taxpayer must be transmitted via API to FIRS, validated, assigned a unique invoice reference number (IRN) and a cryptographic signature, and only then is the invoice legally valid for VAT and CIT purposes. Each cleared invoice carries a **QR code** that customers and FIRS auditors can scan to verify authenticity. The MBS is mandated by FIRS regulations issued under the VAT Act and is being incorporated into the unified electronic compliance framework of the **Nigeria Tax Act 2025** (NTA 2025), which consolidates the legal basis for FIRS digitalisation from 1 January 2026.

### 6.2 Phased rollout timeline

**Phased rollout timeline**

| Phase | In-scope taxpayers | Effective from |
| --- | --- | --- |
| **Phase 1** | Large taxpayers (annual turnover > NGN 5 billion, FIRS Large Tax Office population) — pilot from late 2023, mandatory go-live | **Q3 2024** |
| **Phase 2** | Medium taxpayers (turnover NGN 1 billion to NGN 5 billion) | **2025** (rolling, by sector) |
| **Phase 3** | Smaller taxpayers above the VAT registration threshold (NGN 25M to NGN 1B) | **2026** (subject to FIRS notice; implementing regulations of NTA 2025 expected to confirm) |
| **Phase 4** | Voluntary registrants below threshold | TBC |

**Practitioner note:** at the date of this skill (2025/2026), large taxpayers are fully in-scope. Medium taxpayers should already be onboarding. Smaller VAT-registered businesses should expect mandatory adoption during 2026 once the NTA 2025 implementing regulations are gazetted.

### 6.3 Technical requirements

- **Technical requirements** — - **API integration** — taxpayer's billing/ERP system must integrate with the FIRS MBS API endpoint - **Real-time clearance** — invoice submitted to MBS before delivery to customer; FIRS validates and returns the IRN + signature - **Invoice format** — UBL-aligned XML/JSON (Universal Business Language) with mandatory fields including supplier TIN, buyer TIN, line items, NCM/HSN-equivalent product code, VAT amount, total - **QR code** — encoded with the IRN and key invoice data; printed on every customer-facing invoice (paper or PDF) - **Cryptographic signature** — FIRS-issued digital signature attached to the cleared invoice metadata - **Retention** — cleared invoices retained for 6 years (consistent with general FIRS record-keeping rules)

### 6.4 What changes for the practitioner

- **Changes for the practitioner** — 1. **Input VAT credit** — only invoices that have been MBS-cleared and carry a valid IRN + QR code support input VAT credit claims, once the supplier is in scope. Manual/PDF invoices from in-scope suppliers will not support input claims. 2. **VAT return data** — TaxPro Max will pre-populate sales figures from MBS-cleared invoices for in-scope taxpayers. Reconcile Form 002 sales to the MBS register. 3. **Penalties for non-clearance** — failure to clear an in-scope invoice through MBS attracts penalty equivalent to (or exceeding) the VAT on the invoice plus administrative fines (final amounts to be fixed by FIRS regulations). 4. **Reverse-charge** — self-assessed invoices for imported services should be raised through MBS once the taxpayer is in scope.

### 6.5 Out-of-scope (for now) — paper/PDF invoices

- **Out-of-scope paper/PDF invoices** — For taxpayers not yet in MBS scope, invoices must still meet Section 10 VATA requirements: supplier name and address, TIN/VRN, sequential invoice number, date, description of goods/services, quantity and unit price (exclusive of VAT), VAT amount, total. 6-year retention.  _(Section 10 VATA)_

## Section 7 — Filing and payment

### 7.1 Mechanics

**Filing and payment mechanics**

| Item | Detail |
| --- | --- |
| Form | **VAT Form 002** |
| Frequency | **Monthly** for all VAT-registered persons (including nil returns) |
| Filing deadline | **21st of the following month** |
| Payment deadline | **21st of the following month** (same as filing) |
| Filing portal | **FIRS TaxPro Max** — https://taxpromax.firs.gov.ng |
| Payment method | Pay-direct via TaxPro Max (linked to commercial banks); Remita; direct bank transfer with FIRS payment reference |
| Nil return | **Mandatory** even with zero activity |
| Amendment | Permitted via TaxPro Max amendment workflow; subject to FIRS review |
| Retention period | **6 years** for invoices, returns, and supporting records |

### 7.2 Penalties (VATA s 16-18 / NTA 2025 equivalent provisions)

**Penalties table**  _(VATA s 16-18 / NTA 2025 equivalent provisions)_

| Offence | Penalty |
| --- | --- |
| Failure to register | NGN 50,000 in the first month + NGN 25,000 for each subsequent month of default |
| Late filing of return | **NGN 50,000** in the first month + **NGN 25,000/month** thereafter |
| Late payment of VAT | **5% per month** of unpaid VAT + interest at CBN Monetary Policy Rate (MPR) plus a spread |
| Failure to issue VAT invoice | NGN 50,000 per offence |
| Failure to collect VAT (where required) | **150%** of the uncollected amount + 5% per annum interest |
| Failure to comply with MBS e-invoicing (in-scope taxpayers) | To be confirmed by FIRS regulations; expected to mirror or exceed the equivalent VAT |

### 7.3 Working paper template

```
NIGERIA VAT — MONTHLY WORKING PAPER (Form 002)
Taxpayer: _______________  TIN: ___________  VRN: ___________
Period (Month / Year): ___________

A. OUTPUT (SALES)
  A1. Standard-rated supplies (excl. VAT) — Line 1     ___________
  A2. Output VAT (A1 × 7.5%)             — Line 2     ___________
  A3. Zero-rated supplies                — Line 3     ___________
  A4. Exempt supplies                    — Line 4     ___________
  A5. Reverse-charge output (Sec. 10)                ___________
  A6. Total supplies                                  ___________

B. INPUT (PURCHASES with valid VRN/MBS invoices)
  B1. Input VAT on taxable purchases     — Line 5     ___________
  B2. Reverse-charge input (matches A5)               ___________
  B3. Apportionment factor (if mixed)    ___ %         ___________
  B4. Less: input on exempt supplies                  ___________
  B5. Net allowable input VAT                         ___________

C. NET VAT
  C1. Subtotal (A2 + A5 - B5 - B2)                    ___________
  C2. Less: WHT-VAT credit notes from MDAs            ___________
  C3. Less: prior month excess input c/f (Line 7)     ___________
  C4. VAT payable (or excess to c/f)                  ___________

REVIEWER FLAGS:
  [ ] VAT registration and TIN/VRN confirmed?
  [ ] All input claims supported by VAT invoices showing supplier VRN?
  [ ] In-scope for MBS? All input invoices MBS-cleared with IRN/QR?
  [ ] Mixed-supply apportionment applied where relevant?
  [ ] Nil return filed if no activity?
  [ ] WHT-VAT credit notes obtained for government contracts?
  [ ] Reverse-charge applied to imported services?
  [ ] Zero-rate supported by NXP form / FX evidence?
  [ ] Foreign currency converted at CBN rate on date of supply?
```

## Section 8 — Nigeria Tax Act 2025 (NTA 2025) — changes and transitional context

### 8.1 Background

The **Nigeria Tax Act 2025** consolidates Nigeria's federal tax statutes — Value Added Tax Act, Companies Income Tax Act, Personal Income Tax Act, Capital Gains Tax Act, Stamp Duties Act, Petroleum Profits Tax provisions, and the various Finance Act amendments — into a single unified statute. Companion legislation includes the Nigeria Revenue Service Act (renaming FIRS to NRS in some drafts) and the Joint Revenue Board Act.

The NTA 2025 is **effective 1 January 2026**. Implementing regulations and FIRS information circulars are being published throughout 2025-2026 to operationalise the consolidated framework.

### 8.2 VAT-specific changes under NTA 2025

**VAT-specific changes under NTA 2025**

| Topic | Position under VAT Act (legacy) | Position under NTA 2025 |
| --- | --- | --- |
| Standard rate | 7.5% (Finance Act 2019) | **7.5% retained** (no rate change in the consolidated text as enacted; future rate changes can be made by regulation) |
| Registration threshold | NGN 25M (Finance Act 2019) | **NGN 25M retained**; specific transitional provisions for entities crossing the threshold mid-year clarified |
| Exempt list | First Schedule VATA + Finance Act amendments | **Consolidated and clarified** in the NTA Schedules; basic food, NAFDAC medicines, baby products, education, residential rent, financial services, public transport, agricultural inputs all retained |
| Zero-rated list | Exports + humanitarian (Finance Act 2021) | **Retained and expanded** to clarify exported services criteria |
| Non-resident digital services | Section 10A (Finance Act 2020/2021) + VATGen circular | **Consolidated**; explicit framework for marketplace facilitators to collect and remit |
| Reverse-charge | Section 10 (Finance Act 2020) | **Retained**, mechanics clarified for service importation |
| Input VAT scope | VATA s 17 (restrictions on capital items historically; some loosened by Finance Acts) | **Broadened** under NTA 2025 to align more closely with full-credit IVA models — practitioner should verify under implementing regulations |
| e-Invoicing (MBS) | FIRS regulations under VATA | **Codified** as a statutory requirement in NTA 2025 with the phased timeline confirmed |
| Penalties | VATA s 16-18 | **Recalibrated and standardised** across the consolidated tax types |
| Tax authority name | Federal Inland Revenue Service (FIRS) | **Nigeria Revenue Service (NRS)** — in some draft versions; FIRS brand may persist administratively during transition |

### 8.3 Transitional issues to watch

- **Transitional issues to watch** — - **Returns straddling 1 January 2026**: December 2025 return filed in January 2026 still uses the legacy VATA framework; January 2026 returns onward use NTA 2025 references. Verify with FIRS guidance. - **Input VAT carried forward** from December 2025: should be recognised under NTA 2025 c/f provisions; no expiry expected but confirm. - **MBS scope expansion**: confirm via FIRS gazette which taxpayer tiers come into scope during 2026. - **State VAT challenges**: NTA 2025 reaffirms federal VAT competence pending Supreme Court resolution of Lagos/Rivers cases. - **Sectoral excises** (telecoms, SSB, gaming) — separately codified under NTA 2025; do not stack into VAT lines but coordinate at the invoice level. All NTA 2025 transitional questions should be flagged for reviewer.

## Section 9 — Conservative defaults (compressed)

When the practitioner cannot determine the correct treatment with confidence from the available data, apply the most cautious treatment and flag for reviewer:

1. **Unknown supply nature** → 7.5% standard
2. **Unknown food classification** → processed/taxable until proven exempt
3. **Unknown pharmaceutical exemption** → 7.5% until NAFDAC number produced
4. **Unknown export documentation** → domestic 7.5%
5. **Unknown business-use proportion** → 0% input credit
6. **Unknown foreign supplier registration status** → reverse-charge by Nigerian recipient
7. **Unknown turnover relative to threshold** → assume must file
8. **Unknown apportionment** → no credit on disputed portion
9. **Supplier invoice lacking VRN** → no input credit
10. **Government counterparty** → flag for WHT-VAT review
11. **Foreign currency invoice** → CBN official rate on date of supply
12. **Invoice from suspected in-scope MBS taxpayer without IRN/QR** → no input credit, request MBS-cleared invoice
13. **Period straddling 1 January 2026** → flag for NTA 2025 transitional review
14. **State-level demand notice (Lagos/Rivers)** → escalate to CITN practitioner

## Section 10 — Sources and reference material

### Primary legislation

**Primary legislation table**

| Topic | Reference |
| --- | --- |
| VAT imposition (legacy) | Value Added Tax Act (VATA), Cap V1 LFN 2004, s 2 |
| Registration threshold | VATA s 8, as amended by Finance Act 2019 |
| Exempt supplies | VATA First Schedule (as amended) |
| Zero-rated supplies | VATA Second Schedule + Finance Act 2021 |
| VAT invoice requirements | VATA s 10 |
| Reverse-charge on imported services | VATA s 10 (Finance Act 2020) |
| Non-resident digital services | VATA s 10A (Finance Acts 2020/2021) |
| Filing and payment | VATA s 15 |
| Penalties | VATA s 16, 17, 18 |
| Consolidated framework | **Nigeria Tax Act 2025** (effective 1 January 2026) |
| Tax authority | **Nigeria Revenue Service Act 2025** (renaming/restructuring FIRS) |
| Joint board | **Joint Revenue Board Act 2025** |
| Finance Act amendments | Finance Acts 2019, 2020, 2021, 2023 |

### Regulations, circulars and portals

**Regulations, circulars and portals table**

| Resource | Reference |
| --- | --- |
| FIRS TaxPro Max (filing portal) | https://taxpromax.firs.gov.ng |
| FIRS main portal | https://www.firs.gov.ng |
| FIRS Information Circular 2021/02 — exported services | FIRS website |
| FIRS Information Circular 2021/19 — VATGen for non-resident digital services | FIRS website |
| FIRS Merchant Buyer Solution (MBS) — e-invoicing guidance | FIRS e-Invoicing portal |
| NAFDAC registration database (for pharmaceutical exemption verification) | https://www.nafdac.gov.ng |
| Central Bank of Nigeria FX rates (for foreign currency invoicing) | https://www.cbn.gov.ng |

### Standards bodies

**Standards bodies table**

| Body | Role |
| --- | --- |
| ICAN (Institute of Chartered Accountants of Nigeria) | Chartered accountancy body |
| ANAN (Association of National Accountants of Nigeria) | Recognised accountancy body |
| CITN (Chartered Institute of Taxation of Nigeria) | Recognised tax practitioner body — required for representation before FIRS in tax matters |
| FIRS Large Tax Office (LTO) | Administers Tier-1 large taxpayers |

### Out of scope (cross-reference)

- Petroleum Profit Tax (PPT) / Hydrocarbon Tax under NTA 2025
- Companies Income Tax (CIT)
- Personal Income Tax (PIT)
- Capital Gains Tax (CGT)
- Withholding Tax (income WHT — separate from WHT-VAT)
- Education Tax (EDT), NITDA Levy, NASENI Levy, Police Trust Fund Levy
- Excise duties (alcohol, tobacco, sugar-sweetened beverages, telecoms excise)
- Stamp Duty
- Customs duties / Import duty
- State-level consumption taxes (Lagos, Rivers — pending Supreme Court resolution)
- Free Trade Zone (FTZ) regime
- VAT refund litigation
- Transfer pricing

### Changelog

**Changelog table**

| Version | Date | Change |
| --- | --- | --- |
| 2.0 | 2026 | Consolidated rewrite merging ng-vat-return.md (filing mechanics) and nigeria-vat.md (supplier libraries and worked examples); refreshed for the Nigeria Tax Act 2025 framework effective 1 January 2026 and the FIRS Merchant Buyer Solution e-invoicing phased mandate |
| 1.0 | 2025 | Initial versions (ng-vat-return.md and nigeria-vat.md) |

### Self-check

- [ ] VAT registration and TIN/VRN confirmed
- [ ] Turnover above NGN 25M registration threshold (or voluntary registration in place)
- [ ] Standard 7.5% applied to all unclassified taxable supplies
- [ ] Exempt supplies correctly identified (basic food, NAFDAC medicines, education, financial, residential rent, public transport, agricultural)
- [ ] Zero-rate supported by export documentation (NXP form for goods; FX evidence for services)
- [ ] Reverse-charge applied to imported services under Section 10
- [ ] WHT-VAT credit notes collected for government and large-taxpayer contracts
- [ ] Input claims supported by valid VAT invoices showing supplier VRN
- [ ] In-scope MBS invoices carry IRN, QR code and cryptographic signature
- [ ] Mixed taxable/exempt supplies apportioned correctly
- [ ] Foreign currency converted at CBN rate on date of supply
- [ ] Nil return filed if no activity
- [ ] Form 002 filed and VAT paid via TaxPro Max by 21st of the following month
- [ ] Records retained for 6 years
- [ ] NTA 2025 transitional implications flagged for reviewer

## Prohibitions

- NEVER charge VAT on exempt supplies (basic food, NAFDAC-registered medicines, baby products, education, residential rent, public transport, financial services, insurance)
- NEVER claim input VAT without a valid VAT invoice displaying the supplier's VRN
- NEVER claim input VAT from an in-scope MBS supplier without a cleared invoice carrying IRN, QR code and FIRS signature
- NEVER require VAT registration for businesses below NGN 25,000,000 annual turnover (Finance Act 2019)
- NEVER apply a VAT rate other than 7.5% (the pre-2020 rate of 5% is no longer applicable)
- NEVER miss the 21st monthly filing deadline — nil returns are still required and attract penalties for non-filing
- NEVER claim input VAT on purchases used to make exempt supplies (apportion if mixed)
- NEVER ignore the Section 10 reverse-charge obligation on imported services from non-residents
- NEVER apply state-level VAT alongside federal VAT without explicit reviewer escalation (Lagos / Rivers position disputed)
- NEVER provide VAT refund advice without escalating to a CITN-licensed practitioner
- NEVER advise on FTZ, oil & gas upstream, or real estate VAT without escalation
- NEVER present calculations as definitive — always label as estimated and direct the client to an ICAN/ANAN chartered accountant or a CITN-registered tax practitioner

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional — a chartered accountant (FCA/ACA, ICAN or ANAN) or a CITN-registered tax practitioner in Nigeria — before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as Nigerian tax law evolves under the Nigeria Tax Act 2025 and subsequent FIRS regulations.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
