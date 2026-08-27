---
name: bc-pst
description: Use this skill for British Columbia Provincial Sales Tax — 7% non-harmonized retail sales tax separate from federal GST 5%. Triggers "BC PST", "British Columbia sales tax", "PST registration BC", "PST 7%", "FIN 400", "eTaxBC", "MRDT BC", "BC PST online sales". ALWAYS read this skill for BC sellers / online platforms with BC customers (NOT included in canada-gst-hst).
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BC PST

## British Columbia — Provincial Sales Tax (PST) — Skill v1.0

British Columbia did NOT harmonize with the federal Goods and Services Tax (GST). Instead, BC operates a stand-alone retail sales tax called the **Provincial Sales Tax (PST)** under the **Provincial Sales Tax Act, SBC 2012, c. 35**. Sellers with BC nexus must collect **both** 5% federal GST and 7% BC PST on most taxable sales — they are administered by two different governments on two different bases. This skill covers PST only; for the 5% GST overlay see `canada-gst-hst`.

## 1. Quick reference

- **Standard PST rate** — 7%
- **Registration threshold (BC sales)** — CAD 10,000 in a 12-month period
- **Foreign seller / marketplace economic nexus** — CAD 10,000 (in force since 1 April 2021)
- **Filing form** — FIN 400 — Provincial Sales Tax Return
- **Filing portal** — eTaxBC (https://etax.gov.bc.ca)
- **Filing frequency** — Monthly / quarterly / semi-annual / annual (set by Ministry based on tax collected)
- **Due date** — Last day of the month following the reporting period
- **Statutory basis** — Provincial Sales Tax Act, SBC 2012, c. 35
- **Administrator** — BC Ministry of Finance — Consumer Taxation Programs Branch
- **Companion federal tax** — GST 5% (charged separately, remitted to CRA)

**Quick reference table**

| Item | Value |
| --- | --- |
| Standard PST rate | **7%** |
| Registration threshold (BC sales) | **CAD 10,000** in a 12-month period |
| Foreign seller / marketplace economic nexus | **CAD 10,000** (in force since 1 April 2021) |
| Filing form | **FIN 400** — Provincial Sales Tax Return |
| Filing portal | **eTaxBC** (https://etax.gov.bc.ca) |
| Filing frequency | Monthly / quarterly / semi-annual / annual (set by Ministry based on tax collected) |
| Due date | Last day of the month following the reporting period |
| Statutory basis | Provincial Sales Tax Act, SBC 2012, c. 35 |
| Administrator | BC Ministry of Finance — Consumer Taxation Programs Branch |
| Companion federal tax | **GST 5%** (charged separately, remitted to CRA) |

> **Critical distinction from GST/HST.** PST is a **retail sales tax**, not a value-added tax. There are **no input tax credits**. A registered PST collector cannot recover PST paid on its own purchases — that PST becomes a cost of doing business unless a specific exemption certificate applies (e.g., goods purchased for resale).

## 2. Required inputs + refusal catalogue

### Required inputs before producing any return

- **Required inputs list** — 1. **Legal name + BC PST number** (format `PST-NNNN-NNNN`). 2. **Reporting period** start and end dates. 3. **Total BC sales** (taxable + exempt, broken out). 4. **PST collected** on sales. 5. **PST self-assessed** on taxable purchases brought into BC where no PST was charged at source (use tax / "self-assessment of PST"). 6. **MRDT amounts** (separate line) if collected on accommodation. 7. **Refunds/credits** issued to customers in the period. 8. **Exemption certificates on file** for any zero-rated B2B sales claimed. 9. **Indication whether seller is** (a) BC-located, (b) Canadian outside BC, or (c) foreign seller — affects the registration / collection rules.

### Refusal catalogue — STOP and refer to a BC-registered tax practitioner if:

- **Refusal catalogue** — - Real-property contractors (real-property contracts vs. retail sale of materials — special PST 168 rules). - Liquor licensees / cannabis retailers (separate liquor mark-up + cannabis-specific PST rules). - Motor vehicle dealers — passenger-vehicle luxury surtax bands require dealer-specific guidance. - Energy / natural gas / electricity producers (sector-specific PST treatment under PSTERR and the Carbon Tax Act). - Insurance / financial services (Insurance Premium Tax, not PST). - First Nations sales on reserve (s. 87 Indian Act interaction). - Bankruptcy / receivership returns. - Audit defence, voluntary disclosure submissions, appeals to the Minister. - Any return where the entity is also registered in Saskatchewan, Manitoba, or Quebec — multi-province PST/RST/QST coordination is out of scope here.

## 3. Rate schedule

- **Standard PST rate definition** — 7% on the purchase price of taxable goods, taxable software, and taxable services

**Rate schedule table**

| Category | Rate | Notes |
| --- | --- | --- |
| General tangible personal property | **7%** | Default rate |
| Liquor (sold by liquor retailer to consumer) | **10%** | Applied in addition to federal GST; replaces the former 10% Liquor Consumption Tax |
| Vapour products (e-cigarettes, vapour liquids) | **20%** | In force since 1 Jan 2020 |
| Accommodation (short-term) | **8%** | Separate accommodation rate; MRDT (Section 7) may add 2–3% on top |
| Passenger vehicles — < $55,000 | **7%** | Private sale of used vehicle also 7% (formerly 12% — equalised April 2022) |
| Passenger vehicles — $55,000 – $55,999.99 | **8%** |  |
| Passenger vehicles — $56,000 – $56,999.99 | **9%** |  |
| Passenger vehicles — $57,000 – $124,999.99 | **10%** |  |
| Passenger vehicles — $125,000 – $149,999.99 | **15%** |  |
| Passenger vehicles — ≥ $150,000 | **20%** |  |
| Boats, non-turbine aircraft | 7% / 8% / 10% / 12% banded similarly | Confirm latest bulletin |

- **Rate-determination rule** — > **Rate-determination rule.** The rate is set by the **purchase price including the federal GST** for accommodation and certain other categories, but for passenger vehicles the rate is determined on the price **before GST**. Always read the specific bulletin for the category.

## 4. Registration

### Who must register

- **Registration criteria** — A person must register to collect PST if they **make taxable sales, leases, or provide taxable services in BC** and either: 1. **Resident-in-BC seller** — sells, leases, or provides taxable goods/services in BC in the ordinary course of business (no de minimis — even a single taxable retail sale can trigger registration), OR 2. **Out-of-province Canadian seller or foreign seller** with **more than CAD 10,000 in gross revenue from BC retail sales in the previous 12 months** (or reasonable expectation of exceeding $10,000 in the next 12 months) — this is the economic nexus rule under s. 168.2 PSTA, in force since **1 April 2021**.  _(s. 168.2 PSTA)_

### Marketplace facilitators

- **Marketplace facilitator obligations** — Under amendments effective **1 July 2022**, an **online marketplace facilitator** (Amazon, Etsy, eBay, Shopify Markets, etc.) that facilitates **CAD 10,000+ of BC sales by marketplace sellers** in a 12-month period must: - Register for PST, - Collect and remit PST on facilitated sales on behalf of the underlying seller, - Issue compliant invoices showing PST collected, - Report on FIN 400 as a marketplace facilitator. The marketplace seller does **not** also collect PST on the same transaction — this is statutory single-point collection. The marketplace seller still must register if their **non-facilitated** BC sales (their own website, in-person, etc.) exceed $10,000.  _(Effective 1 July 2022)_

### How to register

- **Registration methods** — - Online via **eTaxBC** — preferred. - Form **FIN 418** (Application for Registration for PST) — paper alternative. - Foreign sellers do not need a BC business number or a Canadian bank account to register; remittance can be made by wire.

## 5. Taxable goods / services / software

- **Closed list rule** — PST applies to a **closed list** of taxable categories. If something is not in the list, it is exempt. This is the **opposite** of GST/HST, where everything is taxable unless specifically exempted or zero-rated.

### Taxable

- **Taxable categories** — - All **tangible personal property** (goods) unless specifically exempt. - **Software** — taxable when (a) delivered on tangible media, (b) downloaded to a BC device, OR (c) used on or with a BC device via a cloud / SaaS arrangement. The 2021 amendments confirmed cloud-based software is taxable under s. 105 PSTA. This is the broadest single PST/GST divergence for tech companies. - **Telecommunication services** — phone, internet, dedicated lines, paging, etc. (s. 130). - **Legal services** (s. 119). - **Related services** — services applied to or with respect to tangible personal property (repair, installation, maintenance, restoration). Note: services to **real property** (construction, painting a building, plumbing in a wall) are **not** PST-taxable as a service — the contractor pays PST on materials acquired and embeds it as cost. - **Short-term accommodation** under 27 days (s. 123). - **Liquor** (sold to consumer by a liquor retailer). - **Vapour products.**  _(s. 105 PSTA; s. 130; s. 119; s. 123)_

### Not taxable (NOT a complete list — see exemptions in Section 6)

- **Not taxable categories** — - Most personal services (haircuts, accounting, consulting, marketing, design). - Services to real property (other than the contractor's input PST). - Professional services other than legal services. - Online digital services other than software (e.g., a digital newspaper subscription is exempt; Netflix is generally subject only to GST, not PST — though always check current Ministry bulletins).

> **Software trap for SaaS sellers.** A US-based SaaS provider with > $10,000 BC subscribers must register, charge **7% BC PST + 5% GST**, and remit each to the respective tax authority. The BC PST registration is independent of GST/HST registration. Many foreign SaaS providers miss this and face retrospective assessment.

## 6. Exemptions

- **Exemption categories** — Statutory exemptions live in the PSTA, the **PST Exemption and Refund Regulation (BC Reg 97/2013)**, and Ministry bulletins. Headline categories: - **Basic groceries** (food for human consumption — same definition as GST Schedule VI). - **Prescription drugs** dispensed under a Health Professions Act prescription. - **Children's clothing and footwear** (specific size and price thresholds — see Bulletin PST 201). - **School supplies** purchased by a qualifying student (note: stricter than the federal GST exemption — confirm against Bulletin PST 202). - **Residential rent** (long-term, 27+ days) and most residential energy. - **Used goods sold in a private (non-business) sale** — except passenger vehicles, boats, and aircraft, where private-sale PST applies. - **Production machinery and equipment (PM&E)** used by qualifying manufacturers (Bulletin PST 110). - **Goods purchased for resale** — buyer provides a PST exemption certificate quoting their PST number; seller does not charge PST and keeps the certificate for audit. - **Sales to certain First Nations purchasers** on reserve (s. 87 Indian Act + Ministry policy). - **Sales to the federal government** (federal Crown immunity — but NOT provincial Crown or BC municipalities, which DO pay PST). A **bona-fide exemption certificate** must be obtained and retained for 5 years. Without one, audit will reassess PST plus penalties.  _(PST Exemption and Refund Regulation, BC Reg 97/2013; Bulletin PST 201; Bulletin PST 202; Bulletin PST 110; s. 87 Indian Act)_

## 7. MRDT — Municipal and Regional District Tax

- **MRDT rule** — The **Municipal and Regional District Tax** is an **additional 2% or 3%** levied on top of the 8% PST on short-term accommodation in designated areas. It is collected by the accommodation provider and remitted via the same FIN 400 return on a separate line.

### Designated areas (illustrative — confirm current Ministry list)

**Designated areas table**

| Area | MRDT rate |
| --- | --- |
| Vancouver | 3% |
| Victoria | 3% |
| Whistler | 3% |
| Tofino | 3% |
| Kelowna | 3% |
| Most other participating municipalities | 2% |

### Online accommodation platforms (Airbnb, Vrbo, Expedia)

- **Online platform registration threshold** — Effective **1 October 2018**, online accommodation platforms with > $2,500 of BC accommodation revenue must register for PST and MRDT and collect on host bookings. Hosts using a registered platform do not separately collect — single-point collection again.  _(Effective 1 October 2018)_

### Total tax on accommodation in Vancouver

- **Total tax on Vancouver accommodation** — 8% PST + 3% MRDT + 5% GST = 16% of the room rate. Some Vancouver accommodations additionally levy a 2.5% Destination Marketing Fee by industry agreement (not a tax — but customer-facing).

## 8. Filing — FIN 400 via eTaxBC

### Frequency

- **Frequency assignment rule** — Assigned by the Ministry based on **PST collectible per year**. A registrant may request more frequent filing.

**Filing frequency table**

| Annual PST collected | Assigned frequency |
| --- | --- |
| Over $11,940 | Monthly |
| $3,000 – $11,940 | Quarterly |
| $0 – $2,999 | Semi-annual |
| Below $0 (consistent net refund) | Annual |

### Due dates

- **Due date and penalties** — The return and payment are due on the **last day of the month following the reporting period**. Example: April PST is due 31 May. Late filing penalties begin at **10% of tax due** plus statutory interest (currently the prescribed rate under PSTA Reg).  _(PSTA Reg)_

### What goes on the return

- **Return boxes** — - **Box A** — Total sales (taxable + exempt). - **Box B** — Total taxable sales. - **Box C** — PST collected at 7% (and itemised lines for 8% accommodation, 10% liquor, 20% vapour, MRDT 2%/3%, vehicle bands). - **Box D** — PST self-assessed on purchases used in BC where no PST was charged. - **Box E** — Adjustments / refunds issued to customers. - **Box F** — **Commission** — registrants are entitled to retain a small commission for collecting PST: **the lesser of $198 per reporting period or 1.32% of PST collected**, but only if the return is filed and paid on time and PST collected is at least $22 (set under s. 50 PSTA Regulation). Note: commission is not available on MRDT or on self-assessed PST. - **Box G** — Net PST payable.  _(s. 50 PSTA Regulation)_

### Payment

- **Payment methods** — - eTaxBC pre-authorised debit (PAD). - Online banking via most Canadian financial institutions using PST account number as the bill-payee reference. - Wire transfer (foreign sellers).

### Records retention

- **Records retention period** — Five years from the end of the calendar year to which the records relate. Foreign-language records must be accompanied by an English translation if requested by an auditor.  _(s. 222 PSTA)_

## 9. Real estate / GST coordination

- **Real estate PST/GST treatment** — - **New residential housing (builder sale)** — **5% GST** applies; **no PST** on residential housing (PST is built into materials only via the contractor's input PST cost). - **Used residential housing (resale)** — **no GST, no PST**. Property Transfer Tax (PTT) under the Property Transfer Tax Act applies separately (out of scope here). - **Commercial real estate** — GST 5% applies; PST does not apply to real-property sales. - **Goodwill on the sale of a business** — **no PST** (goodwill is not tangible personal property). GST may apply unless the s. 167 election is made. - **Tangible assets included in a business sale** (equipment, FF&E, inventory) — **PST applies** unless the buyer is registered and acquiring for resale (resale exemption certificate) or the transaction qualifies for the bulk sale rules (s. 81 PSTA). The s. 167 GST election does NOT shelter PST — these are separate statutes.  _(Property Transfer Tax Act; s. 167; s. 81 PSTA)_

> **Asset purchase trap.** Buyers acquiring a BC business in an asset deal frequently overlook PST on FF&E, vehicles, and software licences. The PST liability survives closing under s. 230 PSTA (successor liability if a clearance certificate is not obtained). **Always obtain a PST clearance certificate from the Ministry before closing.**

## 10. Worked example — Vancouver SaaS / e-commerce business

**Facts.** "Cascadia Cloud Inc." is incorporated in BC, head-quartered in Vancouver. In Q2 2025 it has:

- **SaaS subscriptions** sold to BC customers — CAD 240,000.
- **SaaS subscriptions** sold to Ontario customers — CAD 360,000.
- **SaaS subscriptions** sold to US customers — CAD 500,000.
- **One-off hardware shipment** (network appliances) to a Burnaby BC customer — CAD 12,000, no resale certificate on file.
- **Short-term rental** of a Vancouver-owned condo via Airbnb — gross room revenue CAD 18,000. Airbnb is a registered platform.
- **Internal use of US cloud services** (AWS) — CAD 40,000 of which the BC consumption portion is reasonably allocated as CAD 30,000. AWS did not charge BC PST.

### Step 1 — Identify the PST-taxable BC sales

**Step 1 table**

| Item | Tax base | Rate | PST |
| --- | --- | --- | --- |
| SaaS to BC customers | $240,000 | 7% | **$16,800** |
| Hardware to Burnaby customer | $12,000 | 7% | **$840** |
| SaaS to Ontario customers | $360,000 | n/a (not BC-located use) | $0 |
| SaaS to US customers | $500,000 | n/a (not used in BC) | $0 |

Ontario and US customers are charged GST/HST as applicable (5% GST for US zero-rated export; 13% HST for Ontario) — see `canada-gst-hst`. They are NOT in scope for BC PST.

### Step 2 — Self-assessed PST (use tax) on AWS

- **Self-assessed PST calculation** — US cloud services used in BC are PST-taxable software/telecom services. AWS did not collect PST (assuming AWS is not registered for the in-scope service). Cascadia must self-assess: $30,000 × 7% = $2,100 self-assessed PST. This goes on FIN 400 Box D.

### Step 3 — Airbnb accommodation

- **Airbnb accommodation treatment** — Airbnb is a registered platform; it collects and remits **8% PST + 3% MRDT + 5% GST** on the host's behalf. Cascadia does NOT report this on its own FIN 400. The CAD 18,000 of room revenue is excluded from Cascadia's PST return entirely.

### Step 4 — Compile the FIN 400

**FIN 400 compilation table**

| Box | Amount |
| --- | --- |
| Box B — Taxable BC sales | $252,000 |
| Box C — PST collected (7%) | $17,640 |
| Box D — Self-assessed PST | $2,100 |
| Subtotal | $19,740 |
| Box F — Commission (1.32% × $17,640 = $232.85, capped at $198) | **($198.00)** |
| Box G — Net PST payable | **$19,542.00** |

> **Note on commission.** Commission applies only to PST collected (Box C), not to self-assessed PST (Box D), and is capped at $198 per reporting period.

### Step 5 — Pair with GST

- **GST filing pairing** — Separately, Cascadia files a GST/HST NETFILE return with CRA showing 5% GST on BC and US-zero-rated sales, 13% HST on Ontario sales, and claims Input Tax Credits on GST paid on Canadian purchases. The BC PST self-assessment does NOT generate an ITC — it is a cost.

## 11. Conservative defaults

- **Conservative default rules** — When the treatment is unclear: 1. **Default to charging PST.** Under-collection becomes a personal cost; over-collection can be refunded to the customer. Audit risk is asymmetric. 2. **Treat software / SaaS used in BC as taxable** unless a specific exemption applies and is documented. 3. **Obtain and retain exemption certificates** before zero-rating any B2B resale. No certificate = no exemption. 4. **Self-assess PST on out-of-province purchases of taxable goods and software** used in BC. This is the most common audit miss. 5. **For passenger vehicles, accommodation, liquor, and vapour products, apply the special rate**, not the 7% default. 6. **For mixed bundles** (taxable + exempt) where the price is single, the **entire bundle is taxable** unless the components are separately invoiced (s. 31 PSTA). 7. **For real-property contractors**, default to treating the contractor as the **end consumer** of materials — they pay PST on inputs and do NOT charge PST on the contract price. This is the opposite of the retail sale rule. 8. **When unsure whether a service is "related" to tangible personal property** (and therefore taxable) or is a service to real property (and therefore not), document the analysis and lean toward taxable. 9. **For marketplace facilitators**, confirm whether the platform is collecting PST before the seller separately remits — double collection is unrecoverable without a customer-facing refund.  _(s. 31 PSTA)_

## 12. Sources

- **Provincial Sales Tax Act, SBC 2012, c. 35** — primary legislation.
- **Provincial Sales Tax Exemption and Refund Regulation, BC Reg 97/2013** — exemption details and exemption certificate rules.
- **Provincial Sales Tax Regulation, BC Reg 96/2013** — registration, commission, returns.
- **eTaxBC** — https://www.etax.gov.bc.ca — registration, filing, payment.
- **BC Ministry of Finance Bulletins** (selected):
  - PST 001 — Registering to Collect PST.
  - PST 002 — Charging, Collecting and Remitting PST.
  - PST 105 — Software.
  - PST 107 — Telecommunication Services.
  - PST 110 — Production Machinery and Equipment Exemption.
  - PST 120 — Accommodation.
  - PST 124 — MRDT.
  - PST 130 — Lessors.
  - PST 201 — Children's Clothing and Footwear.
  - PST 202 — School Supplies.
  - PST 308 — PST on Vehicles.
  - PST 400 — PST and Real Property Contractors.
- **Notice 2020-001** — Economic nexus rules for out-of-province sellers (in force 1 April 2021).
- **Notice 2022-002** — Marketplace facilitator rules (in force 1 July 2022).
- **Form FIN 400** — Provincial Sales Tax Return.
- **Form FIN 418** — Application for Registration for Provincial Sales Tax.
- **Form FIN 490** — Certificate of Exemption — General.

> **Coordinate with:** `canada-gst-hst` (5% federal GST overlay on every BC taxable sale), `ca-bc-individual-return` (BC personal income tax — separate regime), and any sector-specific skill for liquor, cannabis, or fuel tax which fall outside this skill's scope.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
