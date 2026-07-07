---
name: pk-sales-tax-federal
description: ALWAYS read this skill before touching any Pakistan FEDERAL sales tax on goods work. Use whenever asked to prepare, review, classify transactions for, or advise on the federal Sales Tax Return (STR) administered by the Federal Board of Revenue (FBR) under the Sales Tax Act 1990 as amended by the Finance Acts 2024 and 2025. Trigger on phrases like "Pakistan sales tax", "FBR ST", "GST Pakistan", "sales tax return Pakistan", "STR Pakistan", "input tax credit Pakistan", "POS Tier-1 Pakistan", "Finance Act 2025 sales tax", "IRIS sales tax", "Annex-C", "STRN", "Fifth Schedule", "Sixth Schedule", "Eighth Schedule", "Ninth Schedule", "Tenth Schedule", or any request involving federal sales tax on goods in Pakistan. Federal scope only — provincial sales tax on services (SRB, PRA, KPRA, BRA) is handled by a separate skill (pk-sales-tax-services).
jurisdiction: PK
tax_year: 2025
reviewed_by: Ibrar Ali
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# pk-sales-tax-federal

## Pakistan — Federal Sales Tax on Goods (FBR) — Skill v2.0

> **Scope.** This skill covers the **federal sales tax on goods** administered by the Federal Board of Revenue (FBR) under the Sales Tax Act 1990 (STA 1990) as amended by the Finance Act 2024 and the Finance Act 2025. It applies to manufacturers, importers, wholesalers, distributors, retailers (including Tier-1 retailers with mandatory POS integration), and other persons making **taxable supplies of goods** in or to Pakistan.
>
> **Out of scope.** Provincial sales tax on **services** (Sindh Revenue Board / SRB, Punjab Revenue Authority / PRA, Khyber Pakhtunkhwa Revenue Authority / KPRA, Balochistan Revenue Authority / BRA, and Islamabad Capital Territory services tax administered by FBR) is handled by the companion skill `pk-sales-tax-services`. Federal Excise Duty (FED), customs duty, and income tax / withholding tax are also out of scope.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ibrar Ali** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### pk-sales-tax-federal

- **Standard rate** — 18% (raised from 17% on 1 Jul 2024; retained by FA 2025)  _(STA 1990 §3)_
- **Higher rate (luxury / specified)** — 25%  _(Eighth Schedule / SROs)_
- **Zero rate (exports, Fifth Schedule)** — 0% (full input recovery / refund)  _(STA 1990 §4; Fifth Schedule)_
- **Exempt (Sixth Schedule)** — No output tax; no input credit  _(STA 1990 §13; Sixth Schedule)_
- **Further tax (supplies to unregistered persons)** — 3% in addition to standard rate  _(STA 1990 §3(1A))_
- **Integrated Tier-1 retailer reduced rate (specified items)** — 15% for textile and leather goods / standard rates for other sectors  _(Eighth Schedule)_
- **Manufacturers** — Mandatory, except for "cottage industries" (turnover up to PKR 10M)  _(STA 1990 §14)_
- **Turnover registration threshold** — Annual turnover > PKR 10,000,000  _(STA 1990 §14 / SRO)_
- **Tier-1 retailer markers** — Electricity bill > PKR 1.2M/yr; national/international chain; A/C mall. (Shop area criteria removed).  _(STA 1990 §2(43A))_
- **Input credit cap §8B** — 90% of output tax (excess carried forward)  _(STA 1990 §8B)_
- **Input claim time limit** — Within 6 tax periods of the invoice  _(STA 1990 §7(1) proviso)_
- **Input credit conditions** — Supplier on ATL + invoice appears in buyer's Annex-A  _(STA 1990 §7 / §8(1)(ca))_
- **CNIC requirement** — Required on ALL invoices to unregistered buyers. (Exemption: retail sales to ordinary consumers ≤ PKR 100,000).  _(STA 1990 §23(1)(b))_
- **Return (STR) due** — 18th of following month (payment by 15th)  _(FBR SOP)_
- **Late filing penalty** — PKR 10,000 (Reduced to PKR 200/day if filed within 15 days of due date)  _(STA 1990 §33)_
- **Default surcharge** — KIBOR + 3% per annum on unpaid tax  _(STA 1990 §34)_
- **Fake / flying invoice** — PKR 25,000 or 100% of tax + criminal liability  _(STA 1990 §37A)_
- **Tier-1 retailer not POS-integrated** — 60% input-tax disallowance + monetary penalty  _(STA 1990 §33)_
- **Revised return** — Within 120 days with Commissioner's approval  _(STA 1990 §26(3))_
- **Refund claim time limit** — Within 1 year of date of payment  _(STA 1990 §66)_
- **ATL reinstatement surcharge** — N/A for Sales Tax (Move to Income Tax section)  _(STA 1990 (FA-set))_
- **Ninth Schedule** — 18% or 25% ad valorem on cellular mobile phones (based on import value)  _(STA 1990 Ninth Schedule)_
- **Tenth Schedule** — Fixed tax on bricks (PCT 6901.0000)  _(STA 1990 Tenth Schedule)_
- **Extra tax (consumer goods to unregistered retailers)** — 25% luxury rate (if referring to SRO 297) / Extra Tax is generally abolished  _(SRO 297(I)/2023 etc.)_

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Pakistan (Islamic Republic of Pakistan) |
| Tax | Federal Sales Tax on Goods (commonly called "GST" colloquially, though FBR uses "Sales Tax") |
| Statute | Sales Tax Act 1990 (STA 1990), as amended by Finance Act 2024 and Finance Act 2025 |
| Authority | Federal Board of Revenue (FBR) — Inland Revenue |
| Currency | PKR (Pakistani Rupee) |
| Tax year | Fiscal year 1 July – 30 June (return is filed monthly regardless) |
| Standard rate | **18%** (raised from 17% by Finance Act 2024, effective 1 July 2024; retained at 18% by Finance Act 2025) |
| Higher rate | **25%** on luxury / specified items per SROs and the Eighth Schedule |
| Reduced rates | Various rates per the Eighth Schedule (1%, 5%, 10%, 12%, 15%, etc., depending on item) |
| Zero rate | 0% — exports and items in the Fifth Schedule |
| Exempt | Items in the Sixth Schedule (basic foodstuffs, pharmaceuticals where listed, agricultural inputs, education, healthcare equipment, etc.) — no output, no input credit |
| Further tax | **3%** additional sales tax on supplies to **unregistered** persons (under §3(1A) STA 1990, rate set by SRO) |
| Extra tax | Generally abolished. SRO 297(I)/2023 imposed a 25% luxury rate on specified items — verify current applicability. |
| Registration threshold | Mandatory for: manufacturers (except cottage industries with turnover up to PKR 10M); importers; commercial wholesalers; Tier-1 retailers; persons with annual turnover **> PKR 10 million**; specified sectors notified by FBR |
| Registration ID | **NTN** (National Tax Number) and **STRN** (Sales Tax Registration Number) — issued on IRIS |
| Return form | **Sales Tax Return (STR)** — filed monthly via IRIS |
| Annexes | Annex-A (purchases), Annex-B (debit/credit notes), Annex-C (sales invoices), Annex-D (exports/imports), Annex-F (stock), Annex-H (refund), Annex-I (debit/credit adjustments), Annex-J (stock) — composition depends on taxpayer category |
| Filing portal | https://iris.fbr.gov.pk (IRIS) |
| Filing deadline | **18th of the month** following the tax period (some categories: 15th for payment, 18th for return — check current SOP) |
| Payment deadline | Typically **15th** of the following month (CPR — Computerised Payment Receipt — generated via IRIS, paid via authorised bank) |
| POS integration | **Tier-1 retailers** must be integrated with FBR's POS system (since 2019/2020). Real-time invoice transmission to FBR; QR-coded receipts |
| Tier-1 incentive | **15%** on textile and leather goods supplied by integrated Tier-1 retailers; standard rates for other sectors |
| Input credit | Allowed against valid registered-supplier invoices showing supplier STRN, within statutory time limits |
| Input credit cap | **90% of output tax** maximum credit per period (Sec 8B STA 1990); excess carries forward |
| Refund | Available primarily to exporters and zero-rated suppliers via Annex-H / FASTER / ERS systems |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Pakistan-registered Chartered Accountant or tax practitioner |
| Skill version | 2.0 |

### Key STR sections (federal sales tax return on IRIS)

**Key STR sections table**

| Section | Meaning |
| --- | --- |
| Annex-C | Output — domestic taxable supplies invoice-wise |
| Annex-D | Exports and zero-rated supplies |
| Annex-A | Input — purchases invoice-wise (auto-populated from suppliers' Annex-C) |
| Annex-B | Debit/credit notes |
| Annex-F | Stock statement (manufacturers) |
| Annex-H | Refund claim (exporters / zero-rated) |
| Annex-I | Adjustment of debit/credit notes |
| Annex-J | Stock summary (where required) |
| Main return | Tax due, input tax, adjustable input, further tax, extra tax, withholding, net payable / carry forward |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale of goods | 18% standard |
| Unknown counterparty registration | **Unregistered** — apply **further tax 3%** on output side; **no input credit** on input side |
| Unknown counterparty country | Domestic Pakistan |
| Unknown export qualification | Domestic 18% until shipping bill / GD / BL evidence confirmed |
| Unknown business-use proportion | 0% input credit |
| Unknown whether supplier invoice is on IRIS | No input credit (must be reflected in Annex-A from supplier's Annex-C) |
| Unknown Tier-1 status of retailer | Treat as Tier-1 if turnover > PKR 100M, has ≥10 retail outlets, has air-conditioning, or other Tier-1 markers per §2(43A) STA 1990 |
| Unknown Eighth Schedule applicability | Apply standard 18% (do not assume reduced rate) |
| Unknown reverse-charge treatment for imported services | Federal sales tax does NOT apply to services — refer to provincial skill |

### Red flag thresholds

**Red flag thresholds table**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | PKR 5,000,000 |
| HIGH tax delta on single default | PKR 900,000 (i.e. 18% of HIGH) |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >5 per period |
| LOW absolute net ST position | PKR 500,000 |
| AUDIT trigger — input/output ratio | Input tax > 90% of output for 3+ consecutive months |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the tax period (HBL, UBL, MCB, Allied, Bank Alfalah, Meezan, Standard Chartered Pakistan, Bank Al-Habib, Faysal, JS, Soneri, Askari, Habib Metro, Silk Bank, Summit; mobile wallets JazzCash, Easypaisa, NayaPay, SadaPay also acceptable). Client's NTN and STRN. Confirmation of registration status (manufacturer, importer, wholesaler, retailer Tier-1 / Tier-2, distributor, exporter).

**Recommended** — sales invoices (issued and received) showing supplier STRN, IRIS Annex-A pre-filled by FBR (the "purchase data" auto-loaded from counterparties' Annex-C), GDs (Goods Declarations) for imports/exports, POS data extract for Tier-1 retailers, prior period credit carry-forward statement, withholding sales tax certificates received.

**Ideal** — full sales/purchase ledgers in IRIS-ready format (CSV), bonded warehouse / EOU documentation if applicable, SROs being relied upon (with reference number and date), stock movement records, customs documents (Goods Declaration, Bill of Lading, Mate Receipt) for imports/exports, copies of withholding tax challans, debit/credit note register.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Federal sales tax input credit requires the supplier invoice to appear in your Annex-A (auto-populated from the supplier's Annex-C filed on IRIS). Until verified on IRIS, all input credits in this working paper are provisional. Output tax must be reported regardless of supplier behaviour."

### Refusal catalogue

- **R-PK-F-1 — Multiple tax authorities / split goods–services business** — "Federal sales tax (this skill) covers goods only. If the same business also supplies services in Sindh / Punjab / KP / Balochistan / ICT, those services require provincial filing via the companion skill `pk-sales-tax-services`. This skill will compute the federal portion only and flag service items for the provincial workflow."
- **R-PK-F-2 — SRO-based manufacturing exemption / concessionary regime** — "Reduced rates and exemptions under SROs (Statutory Regulatory Orders) — e.g., textile zero-rating SROs, dairy SROs, pharma SROs, mobile phone CKD SROs — require gazette-level verification with the current text of the SRO at the date of supply. The skill will flag and compute under standard 18% unless the user provides the active SRO reference. Escalate to a Pakistani Chartered Accountant for definitive SRO interpretation."
- **R-PK-F-3 — Withholding sales tax agent obligations** — "Designated withholding agents (federal/provincial government departments, autonomous bodies, public-sector companies, listed companies, distributors of specified sectors) must withhold sales tax at prescribed rates under the Sales Tax Special Procedure (Withholding) Rules 2007 and the Eleventh Schedule. Out of scope unless you provide the withholding register, SRO 660(I)/2007 applicability confirmation, and the list of suppliers from whom withholding has been deducted. Escalate."
- **R-PK-F-4 — Export refund (Annex-H / FASTER / ERS)** — "Export refund claims via Annex-H, FASTER (Fully Automated Sales Tax e-Refund), or the older Expeditious Refund System (ERS) require complete shipping documentation (GD, BL, mate receipt, e-form, foreign inward remittance), input invoice matching with Annex-A, and stock reconciliation. Refund computation and claim submission is out of scope — escalate. The skill can report zero-rated turnover in Annex-D and flag pending refund."
- **R-PK-F-5 — Partial exemption / mixed taxable + exempt supplies** — "Where a person makes both taxable and exempt supplies (e.g., a manufacturer producing both pharma-exempt and taxable medical devices), input tax must be apportioned per §8(2) and the Apportionment of Input Tax Rules 1996. Requires full-year data to compute the residual input ratio. Out of scope — escalate."
- **R-PK-F-6 — Tier-1 POS non-integration / penalty assessment** — "Persons meeting Tier-1 retailer thresholds (§2(43A) STA 1990) who are not integrated with FBR's POS system face turnover-based penalties and disallowance of input tax. Assessment of penalty exposure and remediation is out of scope. Escalate."
- **R-PK-F-7 — Imported services reverse charge / digital services** — "Federal sales tax under STA 1990 is on **goods only**. Imported services (Google Ads, AWS, Meta, etc.) attract **provincial** sales tax on services (e.g., SRB has a reverse-charge rule) or federal **withholding tax on payments to non-residents** under the Income Tax Ordinance 2001. Neither is covered by this skill. Refer to `pk-sales-tax-services` and the income tax skill."
- **R-PK-F-8 — Federal Excise Duty (FED) overlap** — "Certain goods (cement, sugar, aerated waters, tobacco, services in 'FED in VAT mode' regime) attract Federal Excise Duty in addition to or instead of sales tax. FED is out of scope — escalate to FED specialist."
- **R-PK-F-9 — Combined / aggregated audits, scrutiny notices, show-cause notices** — "Responding to FBR audit / scrutiny / show-cause notices, RAU (Risk-Based Audit Unit) selections, post-refund audits, or DRAP-related inspections is professional advisory work — out of scope. Provide the client's correspondence to a licensed tax practitioner."

## Section 3 — Tier 1 — Registered persons, taxable supplies, input/output

### 3.1 Who must register

- **Mandatory registration categories** — Mandatory registration under §14 STA 1990 and the Sales Tax Rules 2006: - **Manufacturers** — mandatory, except for - **Importers** — any person importing goods (registered automatically via WeBOC / PSW for customs purposes; STA registration also required for input/output reporting). - **Wholesalers, dealers, distributors** — of taxable goods. - **Tier-1 retailers** — see §2(43A): retailer falling in any of these categories: operating as a national/international chain ≥ specified outlets; located in air-conditioned mall, plaza or centre (excluding kiosks); electricity bill > PKR 1.2M / year in last 12 months; wholesaler-cum-retailer engaged in bulk import and supply of consumer goods; or any other category notified by FBR. (Shop area criteria removed.) - **Persons with annual turnover > PKR 10 million** (small retailers below this and below the Tier-1 thresholds may qualify for the Final Tax Regime via electricity bill — verify applicable SRO/schedule). - **Persons engaged in zero-rated supplies / exports** (registration enables refund). - **Persons specifically notified by FBR** under SROs. Voluntary registration is permitted for businesses below threshold who want to claim input credit on inputs sold onward to registered customers.  _(STA 1990 §14, Sales Tax Rules 2006, §2(43A))_

### 3.2 Taxable supply — what is in scope

- **Taxable supply / goods definition** — Per §2(33) and §2(41) STA 1990, a "taxable supply" is a supply of taxable goods made by an importer, manufacturer, wholesaler, distributor, or retailer (other than a supply of goods exempt under §13 / Sixth Schedule) in the course or furtherance of any taxable activity. "Goods" include every kind of movable property other than actionable claims, money, stocks, shares and securities (§2(12)). It does **not** include services (covered by the provincial regime).  _(STA 1990 §2(33), §2(41), §2(12), §13)_

### 3.3 Time and value of supply

- **Time of supply and value of supply** — - **Time of supply** (§2(44)): the earlier of (a) delivery of goods; (b) issuance of invoice; (c) receipt of payment. For continuous supplies (e.g., electricity, gas), the time is the date specified on the bill. - **Value of supply** (§2(46)): consideration in money received, including all federal/provincial duties and taxes excluding sales tax itself. Where consideration is non-monetary, the open-market value. For supplies between associated persons, the open-market value. Trade discounts allowed if shown on the invoice and in line with normal business practice.  _(STA 1990 §2(44), §2(46))_

### 3.4 Standard rate — 18%

- **Standard rate applicability** — Applies to all taxable supplies not falling under a reduced rate (Eighth Schedule), zero rate (Fifth Schedule), or exemption (Sixth Schedule). Increased from 17% to 18% by Finance Act 2024 effective 1 July 2024; retained at 18% by Finance Act 2025.  _(Finance Act 2024; Finance Act 2025)_

### 3.5 Output tax

- **Output tax formula** — Tax charged on outward supplies. Computed as: `Output tax = Value of supply (excluding ST) × applicable rate` If price is "inclusive of sales tax": `Net value = Gross / (1 + rate)` `Output tax = Gross − Net` Output tax is reported invoice-wise in **Annex-C** of the STR.  _(Annex-C)_

### 3.6 Input tax and credit eligibility

- **Input tax credit conditions and §8B cap** — Input tax under §7 STA 1990 may be deducted from output tax in the same tax period if **all** the following are met: 1. Purchase is for **taxable activity** (or zero-rated activity). 2. Invoice is from a **registered** supplier showing the supplier's **STRN**, the buyer's STRN, invoice serial, date, description, quantity, value, rate, and tax amount. 3. Invoice appears in the buyer's **Annex-A** as auto-populated from the supplier's filed Annex-C (or where Annex-A pre-population is overridden, the supplier's CPR is verifiable on IRIS). 4. Claim is made within **six (6) tax periods** from the issuance of the tax invoice (§7(1) proviso — limit may change by Finance Act; verify before each filing). 5. Input is **not blocked** (see §3.7 below). 6. For imports, the **Goods Declaration** is filed and customs duty + ST paid via PSW. **Section 8B cap.** Adjustable input tax is capped at **90% of output tax** in any tax period (§8B STA 1990). Any excess input tax is carried forward to the next period. Specified sectors (e.g., certain registered manufacturers under SRO 1190(I)/2019) are exempt from §8B — check current SRO list.  _(STA 1990 §7, §8B, §7(1) proviso)_

### 3.7 Blocked input — non-creditable

- **Blocked input categories** — Per §8 STA 1990, input tax is NOT allowed on: - Goods used or consumed for **non-taxable** activities (private, exempt, etc.). - Goods on which **extra tax** or **further tax** is paid (cannot be cascaded as input). - **Passenger road vehicles** (except commercial vehicles for hire / transport of goods). - **Building materials** used in immovable property construction (other than for sale of the building as a taxable supply by a registered builder). - **Fake invoices** or invoices issued by **suspended / blacklisted** suppliers (Active Taxpayer List — ATL — check on IRIS before claiming). - **Entertainment, food, beverages** consumed by employees / management (not for resale). - Goods purchased from **unregistered persons** (no STRN, no invoice on IRIS). - Goods not deposited in the **declared business premises** / stock register mismatched.  _(STA 1990 §8)_

### 3.8 Invoice requirements (§23 STA 1990)

- **Tax invoice content requirements** — A "tax invoice" must show: - Name, address, STRN of the supplier - Name, address, STRN (if registered) of the buyer - Date of issue - Serial number (chronological, sequential) - Description of goods, quantity, unit - Value exclusive of tax - Rate of tax (18%, 15%, 5%, etc.) - Amount of tax - Total invoice value - For supplies to unregistered persons: the name and CNIC of the buyer is required on ALL invoices (per §23(1)(b)); exemption applies only for retail sales to ordinary consumers ≤ PKR 100,000 Tier-1 retailers must issue **POS-integrated invoices** with QR code linking to FBR (real-time transmission).  _(STA 1990 §23)_

### 3.9 Filing — monthly Sales Tax Return (STR)

- **Filing timing and nil return requirement** — Filed via IRIS by the **18th of the month** following the tax period (calendar month). Payment via CPR (Computerised Payment Receipt) typically by the **15th**, with the return filed by the 18th. Exact deadlines for any given period are published by FBR via SOP / circular — verify before each filing. A nil return is required even if there are no transactions in the period (failure to file penalises the taxpayer and moves them off the Active Taxpayer List).  _(FBR SOP)_

### 3.10 Penalties (Section 33 STA 1990 — summary)

**Penalties table**  _(STA 1990 §33)_

| Default | Penalty |
| --- | --- |
| Failure to file return on time | PKR 10,000 (reduced to PKR 200/day if filed within 15 days of due date) |
| Failure to issue tax invoice | PKR 10,000 or 5% of value, whichever higher |
| Failure to deposit tax due | PKR 10,000 or 5% of tax, whichever higher, + default surcharge |
| Default surcharge (interest) | **KIBOR + 3%** per annum on unpaid tax (§34) |
| Issuance of fake/flying invoice | PKR 25,000 or 100% of tax, + criminal liability (§37A) |
| Tier-1 retailer not POS-integrated | Disallowance of 60% input tax + monetary penalty |
| Failure to register | PKR 10,000 + 100% of tax sought to be evaded |
| Failure to file refund claim correctly | Refund delayed; no specific monetary penalty |

## Section 4 — Tier 2 — Tier-1 POS integration, Schedules, further/extra tax

### 4.1 Tier-1 retailers and POS integration

- **Tier-1 retailer definition and POS integration requirements** — Since 2019/2020 (notified by FBR via SROs and Chapter XIV-AA of the Sales Tax Rules 2006), **Tier-1 retailers** as defined in §2(43A) STA 1990 must integrate their point-of-sale (POS) systems with FBR's real-time invoicing system. **Definition of Tier-1 retailer (§2(43A))** — meets any one: - Part of a national or international chain. - Operates in air-conditioned mall, plaza, or centre (excluding kiosks). - Cumulative electricity bill > **PKR 1.2 million / year**. - Wholesaler-cum-retailer engaged in bulk import. - Other categories notified by FBR. **Integration requirements:** - Each sales invoice issued by a Tier-1 retailer must be transmitted in real time to FBR's POS server. - Invoice must carry a **QR code** and **invoice number** generated by FBR. - Customer can verify the invoice at FBR's "Tax Asaan" app or the FBR website. - Customers receive a **5% prize / discount** under FBR's Prize Scheme on POS-verified invoices (subject to ongoing notification). **Reduced rate for integrated Tier-1 retailers (selected items).** Per the Eighth Schedule and successive SROs, certain finished goods (e.g., specified textiles, leather articles) supplied by integrated Tier-1 retailers carry a reduced rate (historically **12%**, then **15%**; the rate has fluctuated — verify the current SRO at the date of supply). Non-integrated Tier-1 retailers do NOT qualify for the reduced rate and face input tax disallowance of **60%** of admissible input.  _(STA 1990 §2(43A); Sales Tax Rules 2006 Chapter XIV-AA)_

### 4.2 Fifth Schedule — Zero-rated supplies

- **Zero-rated supply categories** — Per §4 STA 1990 read with the **Fifth Schedule**, the following are charged at **0%** (allowing full input tax recovery / refund): - Exports of goods (with shipping bill / GD evidence). - Supplies to diplomats, diplomatic missions, privileged persons. - Supplies of stores / provisions for consumption aboard conveyances proceeding outside Pakistan. - Locally manufactured plant and machinery (where notified). - Supplies to duty-free shops. - Other items as listed and amended periodically by Finance Acts and SROs (e.g., previously included raw materials for export-oriented sectors — textile, leather, carpets, surgical, sports goods — this "zero-rating" was withdrawn in 2019 for domestic sales and is now confined to actual exports). Zero-rating means the supplier charges 0% output tax, claims input credit on related purchases, and is entitled to a **refund** of net input tax via Annex-H / FASTER / ERS.  _(STA 1990 §4; Fifth Schedule)_

### 4.3 Sixth Schedule — Exempt supplies

- **Exempt supply categories and mixed supply apportionment** — Per §13 STA 1990 read with the **Sixth Schedule**, exempt items include: - **Basic foodstuffs**: unprocessed wheat, rice, pulses, vegetables, fruits, fresh meat, fish, eggs, milk, edible oils where specified. - **Pharmaceuticals**: many active pharmaceutical ingredients and finished medicines (subject to changes by Finance Acts; from 2024 some pharma went from zero-rated to exempt, restricting input credit recovery). - **Agricultural inputs**: certain pesticides, seeds, tractors (where notified). - **Educational items**: textbooks, exercise books, stationery (specified). - **Health equipment**: certain medical devices, supplies for charitable hospitals. - **Newsprint**: as notified. - **Goods imported by international organisations** and diplomatic missions (Table-2). - **Renewable energy items** (solar panels, wind turbines, batteries — coverage has varied; Finance Act 2024 brought some solar items back into the tax net; Finance Act 2025 again altered the position — verify current law before classification). **Effect of exemption.** No output tax. **No input credit** on inputs attributable to exempt supplies. Where a person makes mixed taxable + exempt supplies, input is apportioned per the Apportionment of Input Tax Rules 1996.  _(STA 1990 §13; Sixth Schedule; Apportionment of Input Tax Rules 1996)_

### 4.4 Eighth Schedule — Reduced and concessionary rates

- **Reduced-rate items under Eighth Schedule** — Per §3(2)(aa) STA 1990, the **Eighth Schedule** lists items taxed at rates other than 18%. Common reduced-rate items (rates change frequently — verify): - **Mobile phones** — 18% or 25% ad valorem depending on import value (Ninth Schedule). - **Sugar (industrial use)** — 8% or other reduced rate. - **Soybean meal, oilcake** — 10% or other. - **Re-meltable iron / steel scrap** — fixed PKR / metric ton. - **Locally manufactured electric vehicles** — concessionary rate. - **Specified pharma raw materials** where re-classified out of exempt. - **Certain dairy and milk products** — variable. The Eighth Schedule is amended **every Finance Act**. Always consult the current consolidated Schedule on FBR's website before applying a reduced rate.  _(STA 1990 §3(2)(aa); Eighth Schedule)_

### 4.5 Ninth Schedule — Specified electronics / mobile phones (fixed tax)

- **Mobile phones ad valorem tax** — The **Ninth Schedule** prescribes **18% or 25% ad valorem** on imports / supplies of cellular mobile phones, based on import value. Tax is collected at import (by Customs) and at registration (by PTA / cellular operator).  _(Ninth Schedule)_

### 4.6 Tenth Schedule — Retailer regime (small retailers)

- **Fixed tax on bricks** — The **Tenth Schedule** prescribes fixed tax on bricks (PCT 6901.0000).  _(Tenth Schedule)_

### 4.7 Further tax — 4% on supplies to unregistered persons (§3(1A))

- **Further tax mechanics** — Where a registered person makes a taxable supply to an **unregistered person**, the registered person must charge **further tax at 3%** in addition to the standard 18% (so effective 21% on the supply). Purpose: incentivise the buyer to register. - **Not creditable** by anyone — it is a final tax on the supply chain. - Shown on invoice as a separate line. - Reported in the STR main return under "further tax payable". - Not applicable to supplies to: government departments, exempt entities, end consumers below specified thresholds (verify current SRO exclusions).  _(STA 1990 §3(1A))_

### 4.8 Extra tax — Specified consumer goods to unregistered retailers

- **Extra tax status** — Extra tax under SRO 297(I)/2023 (luxury rate 25%) has largely been abolished. Verify current applicability before applying any extra tax.  _(SRO 297(I)/2023)_

### 4.9 Withholding sales tax (Eleventh Schedule)

- **Withholding sales tax mechanics** — Designated withholding agents (federal/provincial government, autonomous bodies, public-sector companies, listed companies, and others notified) must withhold a portion of sales tax on payments to suppliers under the Sales Tax Special Procedure (Withholding) Rules 2007. Withheld amounts are deposited via CPR and credited to the supplier's STRN. The supplier accounts for full output tax and offsets the withheld amount in the STR. Rates of withholding vary by category of supplier and goods (commonly 1/5th of the tax, 1/10th, or 100% — verify the Eleventh Schedule and current SRO).  _(Sales Tax Special Procedure (Withholding) Rules 2007; Eleventh Schedule)_

### 4.10 Refund mechanisms (exporters and zero-rated)

- **Refund mechanisms and time limits** — - **FASTER** (Fully Automated Sales Tax e-Refund) — for **textile, leather, carpets, sports goods, surgical goods** — the "Five Zero-Rated Sectors". Refund processed automatically based on Annex-H data and Annex-A matching with suppliers' Annex-C. - **ERS** — older system, still used for non-FASTER claims. - **Annex-H** — refund claim filed monthly alongside the STR. - **Time limit** — refund claim must be filed within **one year** of the date of payment of tax (§66 STA 1990). - **Conditions** — input invoices verified, GD / BL / e-form confirmed, foreign inward remittance encashed, stock reconciliation OK.  _(STA 1990 §66)_

### 4.11 Active Taxpayer List (ATL)

- **ATL verification and reinstatement** — FBR publishes a weekly **Active Taxpayer List** (sales tax). Buying from a supplier **not on the ATL** disallows input credit. Always verify supplier ATL status before claiming input. Re-instatement on the ATL requires filing all overdue returns and payment of the "Surcharge for ATL" (a fixed amount currently PKR 20,000 for companies, PKR 10,000 for AOPs, PKR 1,000 for individuals — verify current Finance Act).

## Section 5 — Worked example

**Scenario.** A registered manufacturer of cotton garments in Karachi (Sindh) makes the following supplies in May 2026. Federal sales tax on goods is being computed (the business does not provide services, so no provincial filing is needed). The manufacturer is on the ATL and has been since 2022. Not a Tier-1 retailer (sells B2B and B2 manufactured-export).

### 5.1 Transactions for May 2026

**Transactions table for May 2026**

| # | Date | Description | Counterparty | Counterparty status | Gross (PKR) | Direction |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 03/05/2026 | Sale of cotton T-shirts | RETAILER A (Tier-1, registered, STRN 1234567-8) | Registered | 5,900,000 | Outflow → them |
| 2 | 07/05/2026 | Sale of cotton T-shirts | KIRYANA STORE B | Unregistered | 1,100,000 | Outflow → them |
| 3 | 12/05/2026 | Export of T-shirts to US importer (GD #KHI-EXP-2026-3344) | ACME USA INC | Foreign | 8,000,000 (USD inward) | Outflow → them |
| 4 | 15/05/2026 | Purchase of cotton yarn | YARN MILLS LTD (registered, STRN 7654321-2) | Registered | 4,720,000 | Inflow ← them |
| 5 | 18/05/2026 | Purchase of dyes & chemicals (imported) | Customs GD #KHI-IMP-2026-9988 | Customs | 1,180,000 ST paid at import | Inflow ← them |
| 6 | 20/05/2026 | Electricity bill (K-Electric) | K-ELECTRIC | Registered | 590,000 | Inflow ← them |
| 7 | 22/05/2026 | Purchase from a supplier later found suspended on ATL | XYZ TRADERS | Suspended | 944,000 | Inflow ← them |
| 8 | 28/05/2026 | Sale of fabric scrap | UNREGISTERED RECYCLER | Unregistered | 220,000 | Outflow → them |

### 5.2 Reasoning — line by line

**1. Sale to RETAILER A (registered):** Standard 18%. Gross PKR 5,900,000 includes ST. Net DPP = 5,900,000 / 1.18 = **5,000,000**. Output ST = **900,000**. No further tax (buyer registered). Reported in Annex-C with buyer's STRN.

**2. Sale to KIRYANA STORE B (unregistered):** Standard 18% + **further tax 4%** (total 22%). Gross PKR 1,100,000 includes both ST + further tax. Net DPP = 1,100,000 / 1.22 = **901,639.34**. Output ST (18%) = **162,295.08**. Further tax (4%) = **36,065.57**. Reported in Annex-C with buyer's CNIC (since gross > PKR 100,000); further tax shown separately in the main return. CNIC of buyer is mandatory on ALL invoices to unregistered persons (§23(1)(b)); exemption: retail sales to ordinary consumers ≤ PKR 100,000.

**3. Export to ACME USA INC:** Zero-rated under Fifth Schedule. Output ST = **0**. Reported in Annex-D with GD reference, BL, and inward remittance details. Input tax attributable to this supply is refundable via FASTER (textile is one of the five zero-rated sectors).

**4. Purchase of cotton yarn from YARN MILLS LTD (registered):** Standard 18%. Gross PKR 4,720,000 includes ST. Net = 4,720,000 / 1.18 = **4,000,000**. Input ST = **720,000**. Provided YARN MILLS LTD is on ATL and the invoice appears in Annex-A (pulled from YARN's Annex-C), input is claimable. Reported in Annex-A.

**5. Import of dyes & chemicals (PSW / Customs GD):** Sales tax paid at import via PSW. ST paid PKR 1,180,000. Net DPP at import = 1,180,000 / 0.18 = 6,555,556 (i.e., the DPP on which 18% gives 1,180,000 — but in this scenario the PKR 1,180,000 IS the ST paid, not the invoice gross; clarifying assumption: customs valuation gross PKR 6,555,556 + 18% ST PKR 1,180,000). Input ST = **1,180,000**. Provided GD is reflected in PSW/IRIS, fully claimable. Reported in Annex-A (imports section).

**6. Electricity bill (K-Electric, registered):** Standard 18%. Gross PKR 590,000 includes ST. Net = 590,000 / 1.18 = **500,000**. Input ST = **90,000**. K-Electric is registered (utility) and issues a tax invoice via the bill; appears in Annex-A. Reported in Annex-A.

**7. Purchase from XYZ TRADERS (later suspended on ATL):** Although an invoice was received, XYZ TRADERS is suspended on the ATL. Input tax of PKR 944,000 × 18/118 = PKR 144,000 is **disallowed** under §8(1)(ca) STA 1990 (purchase from non-active supplier). Treat as input = **0**. Flag the line in the working paper for the client to follow up with the supplier or the FBR.

**8. Sale of fabric scrap to UNREGISTERED RECYCLER:** Standard 18% + further tax 4%. Gross PKR 220,000 includes ST + further tax. Net = 220,000 / 1.22 = **180,327.87**. Output ST = **32,459.02**. Further tax = **7,213.11**. CNIC of buyer mandatory if gross > PKR 100,000 → mandatory here. Reported in Annex-C.

### 5.3 Working paper — STR for May 2026

```
PAKISTAN — FEDERAL SALES TAX WORKING PAPER (STR May 2026)
NTN: __________  STRN: __________
Taxpayer category: Manufacturer (textiles)  ATL status: Active

A. OUTPUT (Annex-C + Annex-D)
  A1. Domestic taxable supplies — registered buyers
      DPP                                          5,000,000.00
      Output ST @ 18%                                900,000.00
  A2. Domestic taxable supplies — unregistered buyers
      DPP                                          1,081,967.21
      Output ST @ 18%                                194,754.10
      Further tax @ 4%                                43,278.69
  A3. Exports (zero-rated, Fifth Schedule)
      Value                                        8,000,000.00
      Output ST @ 0%                                       0.00
  A4. Total output ST (A1 + A2)                  1,094,754.10
  A5. Total further tax (A2 further only)            43,278.69

B. INPUT (Annex-A)
  B1. Domestic purchases — registered, ATL active
      DPP                                          4,500,000.00
      Input ST                                       810,000.00
      (yarn 720,000 + electricity 90,000)
  B2. Imports (PSW / Customs)
      DPP                                          6,555,556.00
      Input ST                                     1,180,000.00
  B3. Purchases from suspended / non-ATL suppliers
      DPP                                            800,000.00
      Input ST DISALLOWED                            144,000.00
  B4. Admissible input ST (B1 + B2)              1,990,000.00

C. §8B 90% CAP
  C1. 90% of output ST (A4 × 90%)                   985,278.69
  C2. Lesser of B4 and C1                           985,278.69
  C3. Excess input carried forward (B4 − C2)      1,004,721.31

D. NET PAYABLE / REFUNDABLE
  D1. Output ST (A4)                              1,094,754.10
  D2. Less: Admissible input (C2)                   985,278.69
  D3. Plus: Further tax (A5)                         43,278.69
  D4. Net ST payable                                152,754.10
  D5. Refund claim (Annex-H, exports portion)
      → Excess input attributable to exports
        to be claimed via FASTER; the C3 carry-forward
        of 1,004,721.31 will be partially refunded via
        Annex-H based on the export turnover ratio:
        8,000,000 / (8,000,000 + 5,000,000 + 1,081,967.21)
        = 8,000,000 / 14,081,967.21 = 56.81%
      → Provisional refund claim
        1,004,721.31 × 56.81% =                    570,782.30

E. PAYMENT
  E1. CPR amount (D4)                               152,754.10
  E2. Due date — 15 June 2026 (payment)
  E3. Return due 18 June 2026 (IRIS submission)

REVIEWER FLAGS:
  [ ] All counterparty STRNs verified on IRIS ATL?
  [ ] Annex-A pre-populated; differences reconciled with supplier Annex-C?
  [ ] XYZ TRADERS suspension confirmed; input PKR 144,000 disallowed?
  [ ] Further tax 4% applied to all unregistered sales > 0?
  [ ] CNIC obtained for all unregistered sales > PKR 100,000?
  [ ] GD #KHI-EXP-2026-3344 evidence (BL, e-form, FIR) in file?
  [ ] Annex-H refund claim filed concurrently?
  [ ] §8B 90% cap applied; excess carry forward recorded?
  [ ] Stock movement matched to declared output (Annex-F)?
```

## Section 6 — Filing and payment

### 6.1 Filing channel — IRIS

- **IRIS monthly STR flow** — All federal sales tax returns are filed via **IRIS** at https://iris.fbr.gov.pk. IRIS is FBR's integrated e-filing system (replaced earlier eFBR and standalone Sales Tax e-Filing portals). Login is via the registered NTN/STRN and IRIS password (with 2FA via SMS on the registered mobile number / iris-token app). The monthly STR flow: 1. **Open Sales Tax Return → New return → Period (May 2026).** 2. **Annex-A** is auto-pre-populated with purchase invoices uploaded by the user's suppliers in their Annex-C. Reconcile differences (missing invoices, mismatched amounts, suspended suppliers). 3. **Annex-C** — upload sales invoices (manually, via CSV/Excel template, or via API for ERP-integrated taxpayers). Tier-1 retailers' POS-integrated invoices flow automatically into Annex-C. 4. **Annex-D** — exports (with GD details). 5. **Annex-B / Annex-I** — debit and credit notes. 6. **Annex-F** — stock statement (manufacturers — if FBR requires it for the period). 7. **Annex-H** — refund claim (zero-rated suppliers). 8. **Main return** — system computes output, input, §8B cap, further tax, extra tax, withholding adjustments, payable / carry-forward. 9. **Generate CPR** (Computerised Payment Receipt) for the net payable amount. 10. **Pay** via authorised bank (1-Link / over-the-counter / online banking) by the payment deadline. 11. **Submit return** via IRIS by the **18th of the following month**.  _(https://iris.fbr.gov.pk)_

### 6.2 Payment instruments

- **Payment channels** — - Online banking (1-Link member banks: HBL, UBL, MCB, Allied, Alfalah, Meezan, etc.) — generate CPR on IRIS, pay via Internet banking using the PSID (Payment Slip ID). - ATM (1-Link enabled). - Mobile banking apps (JazzCash, Easypaisa now also offer FBR payment for retail amounts). - Over-the-counter at any authorised branch.

### 6.3 Late filing / late payment

- **Late filing and payment consequences** — - **Late filing penalty**: PKR 10,000 (reduced to PKR 200/day if filed within 15 days of due date). - **Default surcharge** on unpaid tax: **KIBOR + 3%** per annum (§34 STA 1990). - **Removal from ATL**: failure to file the STR by the due date moves the taxpayer off the next weekly ATL — buyers will lose input credit on purchases from this taxpayer until they re-register. - **Re-instatement on ATL**: file all overdue returns + pay surcharge + ATL re-activation fee.  _(STA 1990 §34)_

### 6.4 Revised returns

- **Revised return conditions** — A revised return can be filed within **120 days** of the original filing date with **Commissioner Inland Revenue's approval** (§26(3) STA 1990). After 120 days, only the Commissioner can authorise revisions on application.  _(STA 1990 §26(3))_

### 6.5 Coordination with provincial filings

If the taxpayer also supplies services (a separate business activity from goods), monthly provincial returns are filed in parallel:

- **Sindh**: SRB e-portal — by 15th–18th (varies).
- **Punjab**: PRA e-portal.
- **KP**: KPRA e-portal.
- **Balochistan**: BRA e-portal.
- **ICT (Islamabad)**: Federal — services tax in ICT is administered by FBR via a separate return (the ICT (Tax on Services) Ordinance 2001 read with Finance Act). Sometimes filed alongside the federal goods STR.

See companion skill `pk-sales-tax-services` for provincial workflows.

## Section 7 — Conservative defaults

**Conservative defaults table with rationale**

| Ambiguity | Default | Rationale |
| --- | --- | --- |
| Counterparty registration unknown | Treat buyer as **unregistered** (apply further tax 4%); treat supplier as **unregistered** (no input credit) | Aligns with FBR's penal stance on input claims from unverified suppliers |
| Goods vs services unclear | Federal goods if tangible and movable; flag to `pk-sales-tax-services` if intangible / labour-based | Federal scope is strictly goods (§2(12)) |
| Rate unclear (could be Eighth Schedule reduced) | Apply **18%** standard | Eighth Schedule reductions require SRO confirmation; conservative is higher rate |
| Zero-rate (export) unconfirmed | Apply **18%** domestic | Export requires GD + BL + foreign inward remittance evidence |
| Exempt (Sixth Schedule) unconfirmed | Apply **18%** taxable | Sixth Schedule item lists are detailed and change; default to taxable |
| Tier-1 retailer status unclear | Treat as **Tier-1** if any §2(43A) marker present | Penalty for missed Tier-1 obligations (60% input disallowance) is severe |
| Eighth Schedule reduced-rate item not explicitly listed | Apply **18%** | Reduced rates are exhaustive per item |
| Further tax applicability unclear (buyer registration unknown) | Apply **further tax 3%** | Conservative; better to over-collect and refund than under-collect and face audit |
| Input invoice not visible on Annex-A | **No input credit** this period; claim only when invoice appears in Annex-A | §7 STA 1990 + IRIS protocol |
| Supplier ATL status unverified | **No input credit** | §8(1)(ca) blocks input from non-ATL suppliers |
| §8B 90% cap — sector exemption unclear | Apply the cap (deduct only 90%) | Sector-specific SRO exemptions are narrow; default to general rule |
| Refund eligibility unclear | Do not claim refund; carry input forward | Refund claims trigger audit; only claim with full documentation |
| Withholding sales tax — agent status unclear | Treat as non-withholding agent | Wrong withholding triggers default surcharge |
| Reverse-charge for imported services | Out of scope — refer to provincial / income tax | Federal STA 1990 does not have a reverse charge mechanism for services |

- **Default count limit** — If more than **5 conservative defaults** are applied in a single STR working paper, flag the whole filing as MEDIUM risk and obtain explicit client confirmation before submission.

## Section 8 — Sources

### 8.1 Primary legislation

**Primary legislation table**

| Statute | Reference |
| --- | --- |
| Sales Tax Act 1990 | Act No. III of 1951, as amended (consolidated by FBR) — https://download1.fbr.gov.pk/Docs/2025/Sales%20Tax%20Act%201990.pdf |
| Sales Tax Rules 2006 | SRO 555(I)/2006, as amended |
| Finance Act 2024 | Act No. XIII of 2024 — raised standard rate from 17% to 18%; revised Eighth and Sixth Schedules |
| Finance Act 2025 | Act of 2025 — further amendments to Schedules, further tax mechanics, POS regime (verify text on FBR website) |
| Sales Tax Special Procedure (Withholding) Rules 2007 | SRO 660(I)/2007, as amended |
| Apportionment of Input Tax Rules 1996 | SRO 698(I)/96 |
| ICT (Tax on Services) Ordinance 2001 | For services rendered in Islamabad Capital Territory |

### 8.2 Schedules (current consolidated text on FBR portal)

- **Third Schedule** — items taxable on retail price (manufacturer charges ST on printed retail price, not factory price).
- **Fifth Schedule** — zero-rated.
- **Sixth Schedule** — exempt.
- **Seventh Schedule** — (historically) zero-rated five sectors; largely subsumed into Fifth Schedule.
- **Eighth Schedule** — reduced rates.
- **Ninth Schedule** — 18% or 25% ad valorem on cellular mobile phones (based on import value).
- **Tenth Schedule** — fixed tax on bricks (PCT 6901.0000).
- **Eleventh Schedule** — withholding sales tax rates and categories.
- **Twelfth Schedule** — minimum value addition tax on commercial imports.

### 8.3 Key SROs (verify current text — SROs change frequently)

- SRO 297(I)/2023 — extra tax on consumer goods.
- SRO 1190(I)/2019 — sectors exempt from §8B 90% cap.
- SRO 660(I)/2007 — withholding sales tax procedure.
- SRO on Tier-1 POS integration — successive (verify the consolidated SRO at filing date).

### 8.4 Operational guidance

- FBR IRIS portal: https://iris.fbr.gov.pk
- FBR official website: https://www.fbr.gov.pk
- FBR Tax Asaan app — for taxpayer verification.
- FBR Active Taxpayer List (Sales Tax) — published every Monday.
- FBR Knowledge Base / Helpline 051-111-772-772.

### 8.5 Companion skills

- `vat-workflow-base` — generic VAT/sales tax workflow scaffolding (MUST load).
- `pk-sales-tax-services` — provincial sales tax on services (SRB, PRA, KPRA, BRA, ICT).
- (forthcoming) `pk-income-tax` — Income Tax Ordinance 2001 / withholding tax.
- (forthcoming) `pk-customs-fed` — customs duty and FED.

## Section 9 — Note on provincial sales tax on services (separate skill)

Sales tax on **services** in Pakistan is **NOT** within federal jurisdiction. Following the 18th Constitutional Amendment (2010), the power to tax services devolved to the provinces. Each province has its own legislation, authority, portal, rates, and return:

**Provincial sales tax on services table**

| Jurisdiction | Authority | Statute | Standard rate | Portal |
| --- | --- | --- | --- | --- |
| Sindh | SRB (Sindh Revenue Board) | Sindh Sales Tax on Services Act 2011 | 13% (some categories 8%, 10%, 15%) | https://e.srb.gos.pk |
| Punjab | PRA (Punjab Revenue Authority) | Punjab Sales Tax on Services Act 2012 | 16% (with reduced rates for some categories) | https://e.pra.punjab.gov.pk |
| KP | KPRA (Khyber Pakhtunkhwa Revenue Authority) | KP Finance Act 2013, Second Schedule | 15% (varies) | https://kpra.kp.gov.pk |
| Balochistan | BRA (Balochistan Revenue Authority) | Balochistan Sales Tax on Services Act 2015 | 15% | https://bra.gob.pk |
| Islamabad Capital Territory | FBR (federal as agent for ICT) | ICT (Tax on Services) Ordinance 2001 | 16% (varies — aligned with PRA in practice) | IRIS (FBR portal) |

If a single business supplies **both goods and services**, it must file:
- The **federal STR** (this skill, `pk-sales-tax-federal`) for the goods leg, **and**
- The **applicable provincial return(s)** for the services leg (handled by `pk-sales-tax-services`).

Input tax cross-credit between federal goods ST and provincial services ST is **available** under various bilateral arrangements (FBR-SRB, FBR-PRA, etc.) but the mechanics differ by jurisdiction and require careful tracking. The companion skill covers this.

## Prohibitions

- **Prohibitions list** — - NEVER claim input credit from a supplier whose STRN is **not on the ATL** at the date of supply (§8(1)(ca) STA 1990). - NEVER apply the **17% rate** — current standard rate is **18%** since 1 July 2024. - NEVER skip the **further tax 4%** when supplying to unregistered buyers (§3(1A) STA 1990). - NEVER claim input credit without the invoice appearing in the buyer's **Annex-A** (auto-populated from supplier's Annex-C on IRIS). - NEVER apply a **reduced rate** without confirming the current Eighth Schedule entry and any active SRO at the date of supply. - NEVER treat a Tier-1 retailer's supplies as eligible for the integrated-retailer reduced rate **unless** POS integration is verified with FBR. - NEVER assume **export zero-rating** without GD, BL, e-form, and foreign inward remittance evidence. - NEVER ignore the **§8B 90% input cap** unless the taxpayer is in a sector specifically exempted by an active SRO. - NEVER mix **federal goods ST** computations with **provincial services ST** — they are distinct returns to distinct authorities. - NEVER present this skill's output as definitive — all returns must be reviewed and signed off by a Pakistan-registered Chartered Accountant or licensed tax practitioner before filing.  _(STA 1990 §8(1)(ca), §3(1A), §8B)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Pakistan-registered Chartered Accountant (ICAP / ICMAP), licensed tax practitioner, or equivalent) before filing with FBR or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes (Finance Acts, SROs, and FBR notifications are issued frequently).

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
