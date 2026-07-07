---
name: ng-wht
description: "Use this skill whenever asked to compute, classify, or review Nigerian Withholding Tax (WHT) obligations payable by a business on its outgoing payments to suppliers, landlords, contractors, lenders, shareholders, professionals, or non-resident recipients. Trigger on phrases like \"Nigeria WHT\", \"Withholding Tax Nigeria\", \"FIRS WHT\", \"WHT rates Nigeria\", \"deduct WHT contract Nigeria\", \"PSC WHT\", \"NTA 2025 WHT\", \"WHT credit note\", \"WHT receipt FIRS\", \"WHT remittance Nigeria\", \"WHT on dividends Nigeria\", \"WHT on royalties Nigeria\", \"non-resident WHT Nigeria\", \"treaty WHT Nigeria\", \"petroleum WHT\", or any request involving the classification, deduction, or remittance of Nigerian withholding tax. This skill covers WHT under the Withholding Tax Regulations 1997 (as amended by S.I. 1997 No. 28 and subsequent FIRS notices) for both residents (companies and individuals) and non-residents, including the 2025 transitional regime ahead of the Nigeria Tax Act 2025 (NTA 2025) which will replace and consolidate WHT into a single \"tax-at-source\" Schedule from 1 January 2026. Out of scope: PAYE (Pay-As-You-Earn on employment income — see ng-paye); VAT withholding by listed government MDAs and oil & gas operators (separate from income-tax WHT — see ng-vat-return); Capital Gains Tax withholding on share disposals; specialist upstream petroleum royalty mechanics beyond standard PSC WHT; bespoke FIRS administrative arrangements for individual taxpayers under the SIRS (state) regime. ALWAYS read this skill before touching any Nigerian WHT work."
jurisdiction: NG
domain: international
tax_year: 2025
reviewed_by: Omolola Fasasi 
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# ng-wht

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Omolola Fasasi** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### ng-wht

- **Dividends — company recipient** — 10%  _(CITA s 78)_
- **Interest — company recipient** — 10%  _(CITA s 78)_
- **Royalties — company recipient** — 10%  _(CITA s 78)_
- **Rent — company recipient** — 10%  _(CITA s 78)_
- **Directors' fees — company recipient** — 10%  _(CITA s 78)_
- **Construction contracts — company recipient** — 2.5%  _(CITA s 78; Finance Act 2020)_
- **Consulting / professional fees — company recipient** — 5%  _(CITA s 78)_
- **Management services — company recipient** — 5% or 10%  _(CITA s 78)_
- **Commission / agency fees — company recipient** — 10%  _(CITA s 78)_
- **Dividends — individual recipient** — 10%  _(PITA s 69)_
- **Interest — individual recipient** — 10%  _(PITA s 69)_
- **Royalties — individual recipient** — 10%  _(PITA s 69)_
- **Construction contracts — individual recipient** — 5%  _(PITA s 69)_
- **Consulting / professional fees — company recipient** — 5%  _(CITA s 78)_
- **WHT remittance deadline** — 21st day of month following deduction  _(CITA s 78(3))_
- **WHT- small company exemption** — Small companies exempt from WHT deduction on transactions ≤₦2M/month and on payments to their suppliers. Must be added.

## Section 1 — Quick reference (rate table by transaction type)

**Section 1 Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Federal Republic of Nigeria |
| Tax covered | Withholding Tax (WHT) — advance income tax collected at source on specified payments |
| Currency | Nigerian Naira (NGN, ₦) — foreign-currency payments converted at the CBN official rate on the date of payment |
| Tax year | Calendar year (1 Jan – 31 Dec) for corporate WHT; assessment year aligned with FIRS practice |
| Current tax year | 2025 (transitional — NTA 2025 takes effect 1 January 2026) |
| Federal tax authority | Federal Inland Revenue Service (FIRS) — for companies, non-residents, and Abuja FCT residents |
| State tax authorities | State Internal Revenue Services (SIRS, e.g. LIRS in Lagos) — for individuals, partnerships, and unincorporated entities resident in the State |
| Filing portal | TaxPro-Max (https://taxpromax.firs.gov.ng) for FIRS WHT; State portals for SIRS WHT (e.g. LIRS eTax) |
| Remittance receipt | FIRS WHT Credit Note (electronic) — issued upon successful remittance and reconciliation |
| Company-payer deadline | **21st** day of the month following the month of deduction |
| Individual-payer deadline (where applicable) | **10th** day of the month following the month of deduction |
| Governing law (current) | Companies Income Tax Act (CITA) Cap C21 LFN 2004 (as amended), Personal Income Tax Act (PITA) Cap P8 LFN 2004 (as amended), Petroleum Profits Tax Act (PPTA), Capital Gains Tax Act, plus the **Withholding Tax (Companies and Persons other than Companies) Regulations 1997 (S.I. No. 28 of 1997)** as amended by FIRS Information Circulars (most recently the 2024 update) |
| Governing law (from 1 Jan 2026) | **Nigeria Tax Act 2025 (NTA 2025)** — consolidates WHT into a single tax-at-source Schedule (implementing regulations TBC) |
| Validated by | Verified by Omolola Fasasi (MB058950) on 2026-06-21 |
| Skill version | 1.0 |

### Quick-look: payment type → WHT rate (residents vs non-residents)

**Quick-look payment type to WHT rate table**

| Payment type | Resident — individuals (PITA) | Resident — companies (CITA) | Non-resident (CITA, treaty-cap may apply) | Credit / Final? |
| --- | --- | --- | --- | --- |
| Dividends | 10% | 10% | 10% | **Final** for residents (franked investment income); creditable / final for non-residents per treaty |
| Interest | 10% | 10% | 10% | **Final** for residents on bank/govt interest; otherwise creditable |
| Rent (land, building, equipment hire) | 10% | 10% | 10% | Creditable |
| Royalties | 5% | 5% | 10% | Creditable / final depending on category |
| Technical / professional services fees | 5% | 5% (10% if also a consultant fee) | 10% | Creditable |
| Management fees | 5% | 5% | 10% | Creditable |
| Consultancy fees | 5% | 5% | 10% | Creditable |
| Commissions | 5% | 5% | 10% | Creditable |
| All types of contracts (supply, construction) other than sales in the ordinary course of business | 5% | 5% | 5% (PSC: 10% per FIRS practice) | Creditable |
| Directors' fees | 10% | n/a (companies are not directors) | 10% | Creditable / final |
| Building, construction, and related activities | 2.5% (NEW rate per 2015 amendment) | 2.5% | 5% / 10% non-resident | Creditable |
| Hire of equipment (other than land/building) | 10% | 10% | 10% | Creditable |
| Charter — aircraft, ship, etc. | 10% | 10% | 10% | Creditable |
| Petroleum (PSC and JV operator payments to contractors) | n/a | 5% / 10% per PSC | 5% / 10% per PSC | Creditable against CIT / PPT |

- **Critical rule (Regulation 4, WHT Regulations 1997)** — WHT must be deducted by the payer at the time of payment OR when the liability is credited in the books — whichever comes first. The base is the gross amount excluding VAT. Where VAT applies (currently 7.5%), strip it before computing WHT.  _(Regulation 4, WHT Regulations 1997)_
- **Critical rule (2024 FIRS Information Circular)** — Small companies (turnover ≤ ₦25m) and individuals making payments below specified de-minimis thresholds (typically ₦10,000 per transaction or ₦25,000 in a month to the same recipient for services) are NOT required to deduct WHT on those payments. Verify the current threshold before applying.  _(2024 FIRS Information Circular)_

## Section 2 — Required inputs and refusal catalogue

### 2.1 Mandatory inputs before any WHT computation

- **intro** — Refuse to compute WHT without ALL of the following:

**Mandatory inputs table**

| Input | Why it matters |
| --- | --- |
| Payer identity, TIN, and entity type (company, partnership, individual, government MDA) | Determines whether obligation arises, deadline (21st company / 10th individual), and remitting agency (FIRS vs SIRS) |
| Recipient legal name and tax residence | Determines resident (CITA/PITA) vs non-resident (CITA + treaty) rate |
| Recipient TIN (Tax Identification Number) | Required on the WHT Credit Note; without TIN the recipient cannot claim the credit |
| Nature of the payment (dividend, interest, rent, royalty, services, contract, commission, professional fees, directors' fees, etc.) | Determines applicable rate band |
| Whether payment is in the ordinary course of business (sales of goods) | Sales of goods in the ordinary course are EXEMPT from WHT; only services/contracts and passive income attract WHT |
| Gross contract value, **VAT-exclusive** | Base excludes VAT; strip 7.5% PPN-equivalent first if invoiced gross |
| Date of payment OR accrual, whichever is earlier | Tax point under Regulation 4 |
| For non-resident treaty rate: tax-residence certificate (TRC) from the recipient's home tax authority | Treaty relief denied if TRC not held at tax point |
| For PSC payments: whether payer is Operator, NNPC, or contractor; whether the contract is upstream or midstream | Determines 5% vs 10% PSC WHT under FIRS practice |
| For 2024 Circular de-minimis: payer turnover and per-transaction value | Determines whether small-company / small-payment exemption applies |

### 2.2 Refusal catalogue

Refuse the engagement (explicit refusal, do not guess) in any of the following cases:

- **R-NG-WHT-1** — PAYE on employment income  _(Out of scope — route to ng-paye.)_
- **R-NG-WHT-2** — VAT withholding by listed government MDAs or oil & gas operators (7.5% VAT WHT)  _(Distinct from income-tax WHT; route to ng-vat-return.)_
- **R-NG-WHT-3** — Capital Gains Tax withholding on share disposals (10% CGT, S.I. 2022 No. 6)  _(Separate CGT regime; refer to a Nigerian tax practitioner.)_
- **R-NG-WHT-4** — Upstream petroleum royalty mechanics (NUPRC royalty, gas flare penalty, signature bonus)  _(Specialist domain — refer to a petroleum tax specialist.)_
- **R-NG-WHT-5** — Treaty rate claim without a valid TRC dated before the tax point  _(Default to non-resident statutory rate (10% etc.); treaty relief denied.)_
- **R-NG-WHT-6** — Sales of goods in the ordinary course of business  _(NOT subject to WHT under WHT Regs 1997 — confirm with payer and refuse to over-withhold.)_
- **R-NG-WHT-7** — Bespoke FIRS / SIRS administrative concessions or rulings  _(Cannot rely on private rulings without sight of the actual letter — refuse and request the document.)_
- **R-NG-WHT-8** — NTA 2025 transitional questions covering periods straddling 31 Dec 2025 / 1 Jan 2026  _(Implementing regulations TBC; refuse to commit to post-1-Jan-2026 mechanics until FIRS publishes the WHT Schedule.)_
- **R-NG-WHT-9** — Multi-jurisdictional split between FCT (FIRS) and a State (SIRS) for the same payer  _(Each agency claims residency on different tests — refer to a Nigerian practitioner.)_
- **R-NG-WHT-10** — WHT on intra-group reimbursements without supporting invoices  _(Likely re-characterisable as service fee — refuse and request the underlying contracts.)_

## Section 3 — Tier 1 — common rates (residents and non-residents)

### 3.1 Statutory basis

- **Statutory basis** — WHT is imposed by section 78 (and ss. 79–82) CITA (companies) and section 69 (and ss. 70–74) PITA (individuals and unincorporated bodies). Specific rates and procedures are prescribed by the Withholding Tax (Companies and Persons other than Companies) Regulations 1997 (S.I. No. 28 of 1997) as amended, supplemented by FIRS Information Circulars (most recently the 2024 update consolidating earlier practice).  _(CITA s 78-82; PITA s 69-74; Withholding Tax (Companies and Persons other than Companies) Regulations 1997 (S.I. No. 28 of 1997))_

### 3.2 Resident rates (current — 2025)

The current rate table for payments to Nigerian residents (both companies under CITA and individuals/partnerships under PITA) is:

**Resident rates table**

| Payment type | Rate |
| --- | --- |
| Dividends | 10% |
| Interest | 10% |
| Rent (land, building, plant, machinery, equipment) | 10% |
| Royalties | 5% |
| Technical service fees | 5% |
| Management fees | 5% |
| Consultancy fees | 5% |
| Professional fees (legal, accounting, engineering, etc.) | 5% |
| Commissions | 5% |
| Building, construction, and related activities | 2.5% (reduced from 5% under the 2015 amendment) |
| All contracts other than sales in the ordinary course of business | 5% |
| Hire of equipment (movables) | 10% |
| Charter (aircraft, ship, etc.) | 10% |
| Directors' fees (paid to non-employee directors) | 10% |

### 3.3 Non-resident rates (current — 2025)

For payments to non-residents without a Nigerian permanent establishment, the default statutory rate is generally 10%, often capped or reduced by a Double Tax Treaty (DTT) with the recipient's country. The default non-resident table is:

**Non-resident rates table**

| Payment type | Default rate | Common treaty cap |
| --- | --- | --- |
| Dividends | 10% | 7.5% (UK, Netherlands, Canada, China, Belgium, South Africa, etc.) |
| Interest | 10% | 7.5% (most treaties) |
| Royalties | 10% | 7.5% (most treaties) |
| Technical/management/consultancy service fees | 10% | 7.5% in some treaties; not specifically capped in others — default applies |
| All contracts (other than ordinary sales) | 5% | Per treaty — typically not capped (services article) |
| Directors' fees | 10% | Per treaty |

Nigeria has DTTs in force with: United Kingdom, Belgium, Canada, China, Czech Republic, France, Netherlands, Pakistan, Philippines, Romania, Singapore, Slovakia, South Africa, South Korea, Spain, Sweden, United Arab Emirates. Treaties signed but not yet ratified at the time of writing (e.g. Sweden 2021 protocol, UAE 2016, Cameroon) — verify status at FIRS before applying.

### 3.4 Tax base — gross excluding VAT

- **Tax base excluding VAT** — WHT is computed on the gross contract value or invoice amount excluding VAT. If the invoice is gross-of-VAT at 7.5%, strip VAT first: base = invoice / 1.075. Reimbursements of third-party expenses are excluded from the base only if the supporting invoices are in the name of the payer; otherwise included.

### 3.5 De minimis (2024 Circular)

- **De minimis exemption** — Per the 2024 FIRS Information Circular, small companies (turnover ≤ ₦25m) are not required to deduct WHT on their outgoing payments. Additionally, individual payers and small businesses are not required to deduct WHT on payments below the de minimis (typically ₦10,000 per transaction, or aggregate ₦25,000/month per recipient for services). The recipient remains liable for income tax on the gross amount — the exemption is from the withholding obligation, not the underlying tax.  _(2024 FIRS Information Circular)_

### 3.6 WHT credits

- **WHT credit against liability** — WHT deducted from a resident is generally a credit against the recipient's CIT or PIT liability in the year of assessment in which the income arose. The recipient claims the credit by presenting the FIRS WHT Credit Note (electronic, issued via TaxPro-Max). Excess credits may be carried forward indefinitely or refunded in narrow circumstances.
- **Dividends final for residents** — For dividends, WHT at 10% is final for resident shareholders — the dividend constitutes "franked investment income" and is not aggregated with other taxable income (CITA s. 80(3)). The same applies to bank/government interest earned by resident individuals (PITA s. 70(2)).  _(CITA s. 80(3); PITA s. 70(2))_
- **Final for non-residents passive income** — For non-residents, WHT is final for passive income (dividends, interest, royalties) — the non-resident has no further Nigerian tax obligation on that stream. For active services and contracts, the non-resident may still need to file a Nigerian return if a PE exists.

## Section 4 — Tier 2 — sector specials, treaty rates, transitional under NTA 2025

### 4.1 Petroleum (PSC and JV WHT) — special rates

- **intro** — Payments by Production Sharing Contract (PSC) Operators and Joint Venture partners to contractors and sub-contractors attract WHT at FIRS-prescribed rates that differ from the general 5%:

**PSC WHT rates table**

| Payment | Rate (PSC) |
| --- | --- |
| Service contracts to non-resident contractors (upstream PSC) | **10%** (per FIRS Information Circular and PPTA practice) |
| Service contracts to resident contractors (upstream PSC) | **5%** |
| Management / technical fees in PSC chain | 5% resident / 10% non-resident |
| Royalties paid by Operator to licensor | 5% resident / 10% non-resident |

- **PSC creditability and documentation** — PSC WHT is creditable against the recipient's CIT or PPT (Petroleum Profits Tax) liability. Documentation must reference the specific PSC contract number and FIRS PSC reference.

### 4.2 Building and construction — 2.5% reduced rate

- **2.5% reduced rate scope** — The 2015 amendment to the WHT Regulations reduced the rate on building, construction, and related activities from 5% to 2.5% for residents, in response to industry representations on cash-flow pressure. The reduced rate covers civil engineering, construction works, painting, plumbing, and electrical installation when integral to building works. Pure consultancy on a construction project (architects, quantity surveyors as standalone fees) remains at 5% professional fees, NOT 2.5%.  _(2015 amendment)_

### 4.3 Treaty rates — common matrix

**Treaty rates common matrix**

| Country | Dividends | Interest | Royalties |
| --- | --- | --- | --- |
| United Kingdom | 7.5% | 7.5% | 7.5% |
| Netherlands | 7.5% | 7.5% | 7.5% |
| Canada | 7.5% | 7.5% | 7.5% |
| France | 7.5% / 12.5% | 12.5% | 12.5% |
| China | 7.5% | 7.5% | 7.5% |
| South Africa | 7.5% / 10% | 7.5% | 7.5% |
| Singapore | 7.5% | 7.5% | 7.5% |
| Belgium | 7.5% / 12.5% | 12.5% | 12.5% |
| UAE (signed; verify ratification) | 7.5% | 7.5% | 7.5% |

- **Treaty relief requirements** — Treaty relief requires: A valid Tax Residence Certificate (TRC) from the recipient's home tax authority, dated before the tax point. The recipient must be the beneficial owner of the income (not a conduit). The TRC must be submitted to FIRS via TaxPro-Max when remitting WHT. Without a valid TRC at the tax point, the default statutory rate applies. The non-resident may in theory claim a refund post-payment, but this is administratively difficult.

### 4.4 Transitional under Nigeria Tax Act 2025 (NTA 2025)

The Nigeria Tax Act 2025 (assented June 2025) consolidates Federal tax laws into a single statute and replaces CITA, PITA, PPTA, VAT Act, and the WHT Regulations 1997 from 1 January 2026. Key WHT-related changes flagged for 2026 (subject to implementing regulations):

- Consolidation of WHT into a single "Tax at Source" Schedule, replacing the 1997 Regulations.
- Indications of revised rate ranges — possible reductions for technical/professional services to align with regional practice (Kenya 5%, Ghana 7.5%).
- Express recognition of digital and cross-border services as a WHT category (currently grey under SEP — Significant Economic Presence Order 2020).
- Streamlined single electronic WHT credit note via the consolidated FIRS portal.
- Potential harmonisation of company-payer and individual-payer remittance deadlines (likely to consolidate to 21st of the following month for all payers).

- **TBC under NTA 2025 implementing regulations** — Until FIRS publishes the WHT Schedule and the implementing regulations under NTA 2025, do NOT commit to post-1-January-2026 mechanics. Flag transitional issues and refer.

### 4.5 Digital and cross-border services — Significant Economic Presence (SEP)

- **SEP digital services WHT** — The Companies Income Tax (Significant Economic Presence) Order 2020 brought non-resident digital service providers into the Nigerian tax net where they have SEP (turnover ≥ ₦25m from Nigerian customers, or use of a .ng domain, or local payment infrastructure). For B2B digital service payments to non-residents under SEP, the Nigerian payer must withhold at 10% unless reduced by treaty. NTA 2025 is expected to formalise this regime.  _(Companies Income Tax (Significant Economic Presence) Order 2020)_

## Section 5 — Worked examples

### 5.1 Resident services (professional fees, 5%)

ABC Nigeria Ltd. engages XYZ Consulting Ltd. (resident, valid TIN) for management consultancy. Invoice ₦5,000,000 plus VAT 7.5% ₦375,000, total ₦5,375,000.

- Tax base: ₦5,000,000 (excluding VAT)
- Rate: 5% (management/consultancy fees, resident company)
- WHT to deduct: **₦250,000**
- Net payment to XYZ Consulting: ₦4,750,000 (net of WHT) + ₦375,000 VAT = ₦5,125,000
- ABC Nigeria remits ₦250,000 to FIRS by the **21st of the following month** via TaxPro-Max and obtains a WHT Credit Note in the name of XYZ Consulting Ltd. (with XYZ's TIN).
- XYZ Consulting claims ₦250,000 as a credit against its CIT in its 2025 annual return.

### 5.2 Non-resident services (treaty cap, royalty)

ABC Nigeria Ltd. pays a UK-resident company £100,000 for a software licence (treated as royalty). CBN rate on payment date: ₦1,950/£.

**Scenario A — no TRC on file.**

- Gross NGN equivalent: £100,000 × ₦1,950 = ₦195,000,000
- WHT at 10% (statutory non-resident royalty rate): **₦19,500,000**
- Net remitted to UK: ₦175,500,000 (£90,000)
- ABC issues WHT Credit Note and remits ₦19,500,000 to FIRS by the 21st of the following month.

**Scenario B — valid UK HMRC TRC dated before payment.**

- Nigeria–UK DTT royalty rate (Article 12): **7.5%**
- WHT: ₦195,000,000 × 7.5% = **₦14,625,000**
- Net remitted: ₦180,375,000 (£92,500)
- TRC reference recorded on the WHT Credit Note and uploaded to TaxPro-Max.

> **Software-as-royalty caveat.** Nigeria's FIRS practice generally treats software licence and SaaS subscriptions as royalty (NTA 2025 expected to codify). Default to royalty treatment unless a robust legal opinion supports business-profits classification under Article 7.

### 5.3 Dividends — resident corporate shareholder (final)

NewCo Nigeria Ltd. declares ₦100,000,000 dividend to its parent OldCo Nigeria Ltd. (resident company, valid TIN).

- Tax base: ₦100,000,000
- Rate: 10% (dividend, resident corporate shareholder)
- WHT: **₦10,000,000**
- Net dividend received by OldCo: ₦90,000,000
- The ₦100,000,000 gross dividend is franked investment income in OldCo's hands per CITA s. 80(3) — it is NOT aggregated with OldCo's other taxable income and the 10% WHT is the final Nigerian tax burden on this dividend.
- NewCo remits ₦10,000,000 to FIRS by the 21st of the following month and issues a WHT Credit Note (which OldCo retains as evidence of the franked status).

## Section 6 — Filing and payment

### 6.1 Tax point

- **Tax point trigger** — The WHT obligation arises at the earlier of (Regulation 4, WHT Regulations 1997): Date of payment to the recipient, or Date the cost is accrued / liability credited in the payer's books, or Date of the supplier's invoice (where the payer recognises the liability on receipt). For accrual-basis companies, the tax point is typically the invoice date or the date the liability is booked in payables.  _(Regulation 4, WHT Regulations 1997)_

### 6.2 Remittance deadline — 21st (companies) / 10th (individuals)

- **Companies remittance deadline** — Companies and corporate payers (CITA s. 78): remit by the 21st day of the month following the month of deduction, to FIRS via TaxPro-Max.  _(CITA s. 78)_
- **Individual payers remittance deadline** — Individual payers and unincorporated bodies (PITA s. 69): remit by the 10th day of the month following the month of deduction, to the relevant State Internal Revenue Service (SIRS, e.g. LIRS for Lagos) where the payer is resident, OR to FIRS where the payer is in the FCT (Abuja) or is a federal-charge entity.  _(PITA s. 69)_
- **Remittance schedule details** — The remittance is made via TaxPro-Max (FIRS) or the State portal (LIRS eTax for Lagos, etc.) with a schedule of deductees listing for each: recipient TIN, recipient name, invoice number, gross amount, WHT rate, WHT amount, and nature of payment.

### 6.3 FIRS WHT Credit Note

- **WHT Credit Note issuance** — Upon successful remittance and reconciliation, FIRS issues an electronic WHT Credit Note to each recipient, in PDF format, downloadable from TaxPro-Max. The Credit Note shows the recipient's TIN, the payer's TIN, the period, the gross amount, the WHT rate, the WHT amount, and a unique reference number. The recipient attaches the Credit Note(s) to its annual CIT/PIT return as evidence of the tax credit.

### 6.4 Penalties for non-compliance

- **Late remittance penalty** — Late remittance: penalty of 10% of the tax due plus interest at the CBN Monetary Policy Rate (MPR) plus a spread, per CITA s. 82.  _(CITA s. 82)_
- **Failure to deduct penalty** — Failure to deduct: the payer becomes personally liable for the unpaid WHT plus penalty and interest — the recipient is not pursued.
- **Failure to file return penalty** — Failure to file the WHT return / schedule of deductees: administrative penalty of ₦25,000 (companies) per month or ₦5,000 (individuals) per month.
- **Failure to issue credit notes** — Failure to issue WHT Credit Notes: recipient may claim against the payer directly under common-law breach of regulatory duty.

### 6.5 Annual reconciliation

- **Annual reconciliation process** — There is no separate annual WHT return for the payer beyond the monthly schedules. The annual CIT return (Form CIT) and the annual PIT return (Form A) of the recipient reconciles WHT credits claimed against gross income reported. FIRS automatically cross-matches credits claimed against credits issued via TaxPro-Max — mismatches trigger audit queries.

## Section 7 — Conservative defaults

When any input is ambiguous, missing, or contested, default to the conservative position that minimises the risk of under-withholding — under-withholding makes the payer personally liable (CITA s. 81/PITA s. 73), whereas over-withholding allows the recipient to claim a refund or credit.

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Recipient TIN not provided | Withhold at full statutory rate; do NOT issue Credit Note until TIN provided (recipient cannot claim credit without TIN, but obligation to remit remains) |
| Resident vs non-resident unclear | Treat as non-resident → apply non-resident rate (10% / 5% as applicable) |
| Service vs goods classification ambiguous | Treat as service → WHT applies; goods sales in ordinary course are exempt |
| Building/construction vs general contract | Apply 2.5% only with clear evidence of qualifying building/construction activity; otherwise 5% contracts |
| Treaty rate claim without original TRC | Apply default statutory non-resident rate (no treaty relief) |
| Royalty vs business profits (software/SaaS) | Treat as royalty → withhold per non-resident rate (10% / treaty) |
| Reimbursement of expenses unclear | Include in WHT base unless supporting invoices are in the payer's name |
| Mixed contract (goods + services) | Split if separately invoiced; if bundled, withhold on the full amount as services |
| Small-company de minimis status unverified | Apply WHT (do not assume exemption); the recipient can claim a refund if the exemption is later substantiated |
| CBN exchange rate not yet published | Use the most recent published CBN rate; do NOT use the parallel/black-market rate |
| Period straddles 31 Dec 2025 / 1 Jan 2026 | Apply 1997 Regulations to invoices dated up to 31 Dec 2025; flag post-1-Jan-2026 mechanics as TBC under NTA 2025 |
| Multiple object classifications possible | Pick the higher-rate code |

The general principle: withhold the higher rate when in doubt and let the recipient claim a refund or credit. A refund claim from FIRS is administratively heavy but available; making good an under-withholding from the payer's own pocket months after the supplier has been paid is much worse.

## Section 8 — Sources

**Primary legislation (current — 2025).**
- Companies Income Tax Act (CITA) Cap C21 LFN 2004, as amended by the Finance Acts 2019, 2020, 2021, 2023 — sections 78–82 (WHT on companies).
- Personal Income Tax Act (PITA) Cap P8 LFN 2004, as amended by the Finance Acts — sections 69–74 (WHT on individuals).
- Petroleum Profits Tax Act (PPTA) Cap P13 LFN 2004 (PSC WHT mechanics).
- Capital Gains Tax Act Cap C1 LFN 2004 (CGT — out of scope here).
- Value Added Tax Act Cap V1 LFN 2004 (VAT — distinct from income-tax WHT).

**Future legislation (from 1 January 2026).**
- Nigeria Tax Act 2025 (NTA 2025) — assented June 2025; replaces CITA, PITA, PPTA, VAT Act, WHT Regulations 1997 from 1 January 2026; consolidates WHT into a single "Tax at Source" Schedule (implementing regulations TBC).

**Subsidiary legislation.**
- Withholding Tax (Companies and Persons other than Companies) Regulations 1997 (S.I. No. 28 of 1997), as amended (including the 2015 amendment reducing building/construction WHT to 2.5%).
- Companies Income Tax (Significant Economic Presence) Order 2020 — SEP for non-resident digital services.

**FIRS Information Circulars.**
- 2024 FIRS Information Circular on WHT — consolidates and clarifies WHT rates, de minimis thresholds, and small-company exemption.
- Earlier FIRS circulars on PSC WHT, treaty relief procedure (TRC requirements), and reimbursable expenses.

**Treaty network (as at 2025).** Nigeria has DTTs in force with the United Kingdom, Belgium, Canada, China, Czech Republic, France, Netherlands, Pakistan, Philippines, Romania, Singapore, Slovakia, South Africa, South Korea, Spain, Sweden, and the United Arab Emirates. Always verify the specific treaty article text and ratification status before applying.

**Portals.**
- **FIRS TaxPro-Max** — https://taxpromax.firs.gov.ng — federal WHT remittance, returns, and Credit Notes.
- **LIRS eTax** — https://etax.lirs.net — Lagos State WHT for individuals/partnerships resident in Lagos.
- State Internal Revenue Service portals for other States.

## Section 9 — Cross-references

- For Nigerian PAYE (employment income withholding) → see `ng-paye.md`.
- For Nigerian VAT (including the distinct VAT withholding by listed MDAs and oil & gas operators) → see `ng-vat-return.md` and `nigeria-vat.md`.
- For Nigerian income tax (CIT and PIT) → see `ng-income-tax.md`.
- For Nigerian client intake and identity verification → see `intake.md`.
- For Nigeria foundation (currency, calendar, authority, general principles) → see `foundation.md`.

## Nigeria — Withholding Tax (WHT) — Skill v1.0

*Skill version 1.0. Tax year 2025. Pending sign-off by a qualified Nigerian tax practitioner (CITN-registered or ICAN with tax practice licence). NTA 2025 implementing regulations TBC — do not file WHT returns or commit to post-1-January-2026 mechanics based solely on this skill without credentialed local review.*

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
