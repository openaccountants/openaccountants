---
name: tanzania-income-tax
description: Use this skill whenever asked about Tanzania (Mainland) personal income tax, PAYE, or self-employed/sole-trader tax. Trigger on phrases like "how much PAYE do I pay", "Tanzania income tax", "TRA return", "ITX 201", "presumptive tax", "turnover tax Tanzania", "NSSF deduction", "SDL", "Skills Development Levy", "PSSSF", "WCF", "chargeable income TZS", "provisional tax Tanzania", "Return of Income individual", or any question about computing or filing personal income tax for an employee or self-employed individual in Tanzania. Also trigger when preparing or reviewing an ITX 201.01.E return, computing PAYE on a salary, applying the presumptive (turnover-based) regime, or advising on statutory contributions (NSSF/PSSSF/SDL/WCF). This skill covers the resident PAYE bands, non-resident flat rate, presumptive tax, social-security and statutory contributions, filing forms and deadlines, registration thresholds, and penalties. ALWAYS read this skill before touching any Tanzania income tax work.
jurisdiction: TZ
tax_year: 2025
last_updated: 2026-07-13
authored_by: Baraka Cassian, CPA, CA, CTA
reviewed_by: Baraka Cassian
review_status: current
trust_label: Checked by Baraka Cassian
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzania Income Tax -- Personal / Self-Employed

## Scope note

Tanzania **does** levy a personal income tax administered by the **Tanzania Revenue Authority (TRA)**. This skill covers **Tanzania Mainland**. The TRA also administers Zanzibar PAYE on the same income bands, but Zanzibar runs its own VAT/levy regime — treat Zanzibar-specific indirect taxes as out of scope and escalate. All figures are TZS (Tanzanian Shilling). Tax year = calendar year (1 January – 31 December).

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Baraka Cassian** on 2026-06-12.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### tanzania-income-tax

- **Resident individual rates (annual)** — 0% to TZS 3,240,000; 8% 3,240,001-6,240,000; 20% 6,240,001-9,120,000; 25% 9,120,001-12,000,000; 30% above 12,000,000  _(Income Tax Act, Cap 332, First Schedule)_
- **Non-resident individual - employment income** — 15% flat, final  _(Income Tax Act, Cap 332)_
- **CIT standard rate** — 30% (resident corporations and PEs of non-residents)  _(Income Tax Act, Cap 332, First Schedule)_
- **CIT - newly DSE-listed companies** — 25% for three consecutive years from listing; minimum 25% of shares issued to the public  _(Income Tax Act, Cap 332, First Schedule)_
- **CIT - new assemblers of vehicles/tractors/fishing boats** — 10% for first five years from commencement  _(Income Tax Act, Cap 332, First Schedule)_
- **CIT - new manufacturers of pharmaceuticals or leather products** — 20% for first five years (performance agreement with Government required)  _(Income Tax Act, Cap 332, First Schedule)_
- **Alternative minimum tax (AMT)** — 1% of turnover for entities with perpetual unrelieved tax losses for the current and preceding two income years  _(Income Tax Act, Cap 332 (AMT provisions, as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Extractive-sector service fees (residents)** — 10% FINAL withholding on technical and management services provided to mining, oil and gas entities by residents (increased from 5%)  _(Income Tax Act, Cap 332 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Presumptive regime eligibility** — Resident individuals with business turnover not exceeding TZS 100,000,000 per annum (no presumptive for entities)  _(Income Tax Act, Cap 332, First Schedule para 2)_
- **Presumptive band 1** — Turnover below TZS 4,000,000: NIL tax  _(Income Tax Act, Cap 332, First Schedule para 2)_
- **Presumptive band 2** — TZS 4m-7m: TZS 100,000 (no records) OR 3% of turnover above TZS 4m (records kept)  _(Income Tax Act, Cap 332, First Schedule para 2)_
- **Presumptive band 3** — TZS 7m-11m: TZS 250,000 (no records) OR TZS 90,000 + 3% of turnover above TZS 7m (records kept)  _(Income Tax Act, Cap 332, First Schedule para 2)_
- **Presumptive band 4** — TZS 11m-100m: 3.5% of turnover (records required)  _(Income Tax Act, Cap 332, First Schedule para 2)_
- **Presumptive tax - transporters (selected)** — Vehicle-based annual amounts, e.g. passenger vehicles up to 5 seats TZS 120,000 up to TZS 2,200,000 (>65 seats); taxis TZS 180,000; ride-hailing TZS 350,000; ride-sharing TZS 450,000; special hire TZS 750,000; goods vehicles TZS 120,000-2,200,000 by tonnage  _(Income Tax Act, Cap 332, First Schedule (transport presumptive schedule))_
- **CGT - disposal of investment (individuals)** — Tanzanian-source investment: 10% resident / 30% non-resident (single instalment basis)  _(Income Tax Act, Cap 332, s.90)_
- **CGT - corporations** — Gains on realisation of investments included in income and taxed at 30%  _(Income Tax Act, Cap 332)_
- **Realisation of land/buildings - compliance** — Single instalment payable within 30 days of realisation; notify Commissioner within 14 days  _(Income Tax Act, Cap 332, s.90; Tax Administration Act, Cap 438)_
- **Realisation without cost records (resident individuals)** — 3% of the GREATER of incomings or the approved asset value (instead of 10% of gain) for land/buildings  _(Income Tax Act, Cap 332, s.90 (as amended))_
- **CGT exemptions (selected)** — Private residence where gain <= TZS 15m; agricultural land with market value <= TZS 10m; DSE-listed shares held by a resident; DSE-listed shares of a non-resident holding <25%  _(Income Tax Act, Cap 332, s.9 / Second Schedule exemptions)_
- **Taxation of undistributed profits (deemed distribution)** — CG may treat 30% of after-tax profits as distributed where not distributed within 12 months after year-end; 10% dividend WHT applies on the deemed distribution  _(Income Tax Act, Cap 332 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Tax loss carryforward** — Indefinite carryforward; BUT brought-forward losses may shelter only 60% of taxable profits in a year (excess carried forward). 60% cap does not apply to agriculture, health and education businesses  _(Income Tax Act, Cap 332, s.19 (as amended))_
- **Loss ring-fencing** — Agricultural, mining-licence-area, petroleum-licence-area, foreign-source, investment and speculative losses offset only against income of the same category/area  _(Income Tax Act, Cap 332, s.19)_
- **Depreciation - Class 1 (37.5% reducing balance)** — Computers and data handling equipment; automobiles/buses/minibuses <30 passengers; goods vehicles <7 tonnes; construction and earth-moving equipment  _(Income Tax Act, Cap 332, Third Schedule)_
- **Depreciation - Class 2 (25% reducing balance)** — Buses >=30 passengers; heavy/specialised trucks and trailers; rail, vessels, aircraft; plant and machinery used in agriculture or manufacturing; public utility plant  _(Income Tax Act, Cap 332, Third Schedule)_
- **Depreciation - Class 3 (12.5% reducing balance)** — Office furniture, fixtures and equipment; any asset not in another class  _(Income Tax Act, Cap 332, Third Schedule)_
- **Depreciation - buildings** — Class 6: 5% straight line (general buildings/structures); Class 5: 20% straight line (agriculture/livestock/fish-farming buildings, dams, fences)  _(Income Tax Act, Cap 332, Third Schedule)_
- **Depreciation - intangibles (Class 7)** — Straight line over useful life of the asset  _(Income Tax Act, Cap 332, Third Schedule)_
- **Depreciation - Class 8 (100%)** — Plant and machinery used in agriculture; electronic fiscal devices purchased by non-VAT-registered traders  _(Income Tax Act, Cap 332, Third Schedule)_
- **Enhanced allowance - manufacturing/fish farming/tourist hotels** — 50% allowance on qualifying plant and machinery enjoyed equally in the first and second years; normal rates on the remaining balance thereafter  _(Income Tax Act, Cap 332, Third Schedule)_
- **Mineral/petroleum operations expenditure** — 20% per year straight line  _(Income Tax Act, Cap 332, Third Schedule)_
- **Charitable contributions deduction** — Approved charitable/social development contributions deductible up to 2% of taxable income (before the deduction); Education Fund, LGA statutory community obligations and AIDS Trust Fund contributions also deductible  _(Income Tax Act, Cap 332, s.16)_
- **Statement of estimated tax** — Due within 3 months from start of the accounting period; instalments payable by end of months 3, 6, 9 and 12  _(Income Tax Act, Cap 332, ss.88-89)_
- **Final income tax return** — Within 6 months after accounting period end (public sector entities: within 9 months)  _(Income Tax Act, Cap 332, s.91; Tax Administration Act, Cap 438)_
- **Late filing penalty** — Per month or part-month, the HIGHER of 2.5% of unpaid tax or 15 currency points (TZS 300,000) for entities; 5 currency points (TZS 100,000) for individuals  _(Tax Administration Act, Cap 438, s.78)_
- **Interest on late payment** — Statutory rate (Bank of Tanzania discount rate), compounded monthly  _(Tax Administration Act, Cap 438, s.76)_
- **Statute of limitations** — TRA may adjust a return within 5 years of the final-return due date; NO limit for fraud, wilful neglect or serious omission  _(Tax Administration Act, Cap 438, s.48)_
- **Objection deposit** — Higher of tax not in dispute or one-third of assessed tax; FA2025 adds CG power to demand 100% deposit where objector is a flight risk  _(Tax Administration Act, Cap 438, s.51 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Objection determination time limit** — If TRA issues no determination within 6 months of admitting an objection, the assessment/decision is treated as confirmed and taxpayer may appeal to the Board  _(Tax Administration Act, Cap 438, s.52 (as amended))_
- **Appeal route** — TRA objection -> Tax Revenue Appeals Board (TRAB) -> Tax Revenue Appeals Tribunal (TRAT) -> Court of Appeal  _(Tax Revenue Appeals Act, Cap 408)_
- **CPA certification of returns** — Returns of corporations with gross income above TZS 100m and individuals with turnover above TZS 500m must be prepared or certified by a CPA in public practice  _(Tax Administration Act, Cap 438 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Audited financial statements (sole traders)** — Required where annual turnover is TZS 100m or more  _(Tax Administration Act, Cap 438)_
- **Digital service tax (non-residents)** — 2% of turnover (excl. VAT) for non-resident providers of electronic services; monthly return and payment by the 20th of the following month  _(Income Tax Act, Cap 332; Income Tax (Registration of Non-Resident Electronic Service Suppliers) Regulations 2022)_
- **Digital asset withholding tax** — 3% on payments to residents for exchange/transfer of digital assets; withheld by platform owners/facilitators including non-residents (simplified registration required)  _(Income Tax Act, Cap 332 (as amended by Finance Act 2024))_
- **Forest produce single instalment** — 2% of gross payment remitted before transporting forest produce (timber, logs, mirunda, poles); base = greatest of farm-gate price, purchase price or TFS-determined value  _(Income Tax Act, Cap 332 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Functional currency** — TZS; Commissioner may permit quantification in convertible foreign currency on written application  _(Income Tax Act, Cap 332; Tax Administration Act, Cap 438)_
- **Tax year** — Calendar year default; entities may apply to use their own accounting period  _(Income Tax Act, Cap 332, s.20-21)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Republic of Tanzania (Mainland) |
| Tax | Personal Income Tax / PAYE |
| Currency | TZS (Tanzanian Shilling) only |
| Tax year | Calendar year (1 January – 31 December) |
| Primary legislation | Income Tax Act, Cap. 332; Tax Administration Act, Cap. 438 |
| Tax authority | Tanzania Revenue Authority (TRA) |
| Filing portal | TRA online services (PAYE/SDL/WHT monthly); IDRAS for SDL |
| PAYE deadline | 7th day of the month following the payroll month (TRA) |
| Annual individual return | Form ITX 201.01.E — due within 6 months of year-end (by 30 June) (TRA / PwC) |
| Tax-free threshold | First TZS 270,000/month (TZS 3,240,000/year) (TRA) |
| Top marginal rate | 30% (TRA) |
| Validated by | Pending — requires sign-off by a Tanzanian tax practitioner |
| Validation date | Verified by Baraka Cassian (ACPA 3158) on 2026-06-12 |
| Skill version | 0.1 |

### Resident PAYE Bands — Monthly (TRA)

**Resident PAYE Bands — Monthly**  _(TRA, "Income Tax for Individuals" (https://www.tra.go.tz/page/income-tax-for-individuals); confirmed by PwC Tax Summaries, last reviewed 14 Jan 2026 (https://taxsummaries.pwc.com/tanzania/individual/taxes-on-personal-income))_

| Monthly taxable income (TZS) | Rate | Tax on band | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 – 270,000 | 0% (NIL) | 0 | 0 |
| 270,001 – 520,000 | 8% of excess over 270,000 | 20,000 | 20,000 |
| 520,001 – 760,000 | 20,000 + 20% of excess over 520,000 | 48,000 | 68,000 |
| 760,001 – 1,000,000 | 68,000 + 25% of excess over 760,000 | 60,000 | 128,000 |
| Above 1,000,000 | 128,000 + 30% of excess over 1,000,000 | — | — |

**Arithmetic check (do not alter without re-deriving):** band 2 cap 250,000 × 8% = 20,000; band 3 cap 240,000 × 20% = 48,000 → 68,000 cumulative; band 4 cap 240,000 × 25% = 60,000 → 128,000 cumulative. Tax-free first TZS 270,000/month = TZS 3,240,000/year, stated explicitly by TRA.

### Other Income-Tax Rates on Individuals

**Other Income-Tax Rates on Individuals**

| Item | Rate | Source |
| --- | --- | --- |
| Non-resident employment income | 15% flat, FINAL tax | PwC (Big-4) — TRA rate page does not restate it [RESEARCH GAP — reviewer to confirm against ITA Cap. 332] |
| Secondary employment (second employer) | 30% flat, withheld at source | TRA individual guidance / Big-4 guides |
| Capital gains — resident, Tanzanian-source investment | 10% | PwC |
| Capital gains — non-resident, Tanzanian-source investment | 30% | PwC |
| Capital gains — resident, overseas-source investment | 30% | PwC |

### Presumptive (Turnover-Based) Tax — Individual Traders (TRA)

**Presumptive (Turnover-Based) Tax — Individual Traders**  _(TRA, https://www.tra.go.tz/page/income-tax-for-individuals)_

| Annual turnover (TZS) | Tax — incomplete records | Tax — complete records |
| --- | --- | --- |
| 0 – 4,000,000 | NIL | NIL |
| 4,000,001 – 7,000,000 | 100,000 | 3% of excess over 4,000,000 |
| 7,000,001 – 11,000,000 | 250,000 | 90,000 + 3% of excess over 7,000,000 |
| 11,000,001 – 100,000,000 | 3.5% of turnover | 3.5% of turnover |

Applies to **resident individuals** with annual business turnover **not exceeding TZS 100,000,000** who are **not VAT-registered**. **Arithmetic check:** complete-records band 2 at TZS 7,000,000 = 3% × 3,000,000 = 90,000, which is the base of band 3 — consistent. Turnover **above TZS 100,000,000**: taxed on net profit under the standard regime (full accounts required), NOT presumptive (TRA).

### Statutory Contributions (Quick View)

**Statutory Contributions (Quick View)**

| Contribution | Total | Employee | Employer | Source |
| --- | --- | --- | --- | --- |
| NSSF (private sector) | 20% of gross | up to 10% | balance (min 10%) | NSSF / PwC |
| PSSSF (public sector) | 20% of gross | up to 5% | ~15% | PwC |
| SDL (Skills Development Levy) | 3.5% of gross emoluments | 0% | 3.5% (employer-only) | TRA / PwC |
| WCF (Workers' Compensation Fund, private) | 0.5% of cash sums | 0% | 0.5% (employer-only) | PwC |

**Arithmetic check:** NSSF employee (10%) + employer (10%) = 20% total. PSSSF employee (5%) + employer (15%) = 20% total. SDL and WCF are employer-only — employee column is 0.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP — do not apply a rate table without residency |
| Unknown whether second employer exists | Treat as primary employment (progressive bands), flag for reviewer |
| Unknown record quality (presumptive) | Use **incomplete-records** column (higher) |
| Unknown VAT-registration status of trader | Assume VAT-registered → presumptive NOT available; flag |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown sector (public vs private) | Assume private sector (NSSF, not PSSSF) |
| Number of employees unknown (SDL) | Flag — SDL applies only at 10+ employees |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — payroll details (gross monthly salary) for an employee, OR a bank statement for the full tax year plus confirmation of business turnover for a self-employed trader; plus confirmation of **residency** (resident / non-resident) and **employment status** (single employer / second employer / self-employed).
- **Recommended** — all sales invoices/receipts, purchase invoices, NSSF/PSSSF contribution records, SDL/WCF records (if employer), prior-year ITX 201 or assessment, VAT-registration confirmation, statement of whether business records are "complete" or "incomplete".
- **Ideal** — complete income and expenditure account, asset register, provisional-tax (statement of estimated tax) payment confirmations, all employer P9/PAYE schedules, sector confirmation (public/private).
- **Refusal if minimum is missing** — SOFT WARN. No payroll or bank data at all = hard stop. Data without supporting invoices = proceed with reviewer warning: "This computation was produced from bank/payroll data alone. The reviewer must verify that every deduction is supported and that turnover/record-completeness drives the correct presumptive column."

### Refusal Catalogue

- **R-TZ-1** — Residency unknown. "Residency determines whether progressive resident bands or the 15% non-resident flat (final) rate applies. This skill cannot compute tax without confirming residency. Please confirm before proceeding."
- **R-TZ-2** — Companies, partnerships, group structures. "This skill covers resident individuals (employees and sole traders) only. Companies, partnerships, and groups file separately. Escalate to a Tanzanian tax practitioner."
- **R-TZ-3** — Zanzibar indirect taxes. "Zanzibar runs its own VAT/levy regime. PAYE bands are shared, but Zanzibar VAT and levies are out of scope. Escalate."
- **R-TZ-4** — Capital gains / property disposals. "Capital gains on investments and property require specialised analysis (resident 10%, non-resident 30%, overseas-source 30%). Out of scope for routine computation. Escalate."
- **R-TZ-5** — Arrears / enforcement. "Client has outstanding tax arrears or is subject to TRA enforcement. Statutory interest (BoT discount rate + 5%, compounded monthly) and penalties are severe. Do not advise — escalate to a Tanzanian tax practitioner immediately."
- **R-TZ-6** — VAT return requested. "This skill covers income tax/PAYE and presumptive tax only. Tanzania VAT (standard rate 18%, registration threshold TZS 200,000,000 Mainland) is a separate workflow."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5. Match by case-insensitive substring on the counterparty/description. Most specific match wins. Swahili terms are included because Tanzanian statements frequently mix English and Swahili.

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + MALIPO, PAYMENT, DEPOSIT, AMANA | Business income | Sole-trader turnover / revenue | If VAT-registered (Art.), extract net (excl. 18% VAT) |
| ADA, FEES, USHAURI, CONSULTANCY, PROFESSIONAL FEES | Business income | Professional fees | Typical self-employed income |
| MSHAHARA, SALARY, MISHAHARA, EMPLOYER [name] | Employment income | PAYE income | Goes to employment computation, not turnover |
| STRIPE PAYOUT, PAYPAL, WISE, FLUTTERWAVE, DPO | Business income | Platform payout | Match to underlying invoices |
| M-PESA, TIGO PESA, AIRTEL MONEY, HALOPESA (received) | Business income (if trade) | Mobile-money receipt | Verify business vs personal; mobile money is ubiquitous |
| KODI / RENT RECEIVED | Other income | Rental income | Not trading turnover |
| RIBA, INTEREST RECEIVED | Other income | Investment income |  |
| GAWIO, DIVIDEND | Other income | Investment income |  |
| TRA REFUND, MAREJESHO YA KODI | EXCLUDE | Tax refund | Prior-year refund, not income |
| RUZUKU, GOVERNMENT GRANT | Check nature | Capital grant EXCLUDE; revenue grant = income | Flag for reviewer |

### 3.2 Expense Patterns (Debits) — Fully Deductible (Self-Employed)

**Expense Patterns (Debits) — Fully Deductible (Self-Employed)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| KODI YA OFISI, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| BIMA, INSURANCE (business), PROFESSIONAL INDEMNITY | Business insurance | Deductible |  |
| MHASIBU, ACCOUNTANT, AUDIT, BOOKKEEP | Accountancy fees | Deductible |  |
| WAKILI, LAWYER, LEGAL (business) | Legal fees | Deductible | Must be business-related |
| VIFAA VYA OFISI, STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MATANGAZO, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| MAFUNZO, TRAINING, SEMINAR, WARSHA | Training | Deductible | Must relate to current business |
| ADA YA BENKI, BANK CHARGE, CRDB CHARGE, NMB FEE | Bank charges | Deductible | Business account only |
| STRIPE FEE, M-PESA FEE, MAKATO | Transaction/processing fees | Deductible |  |

### 3.3 Expense Patterns (Debits) — Software / SaaS

**Expense Patterns (Debits) — Software / SaaS**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, ZOOM, ADOBE | Software subscription | Deductible | Recurring = operating expense |
| ANTHROPIC, OPENAI, GITHUB, CANVA, NOTION | Software subscription | Deductible |  |
| PERPETUAL SOFTWARE LICENCE (high value) | Capital item | Capitalise — capital allowances | Flag for reviewer; depreciation per ITA schedule [RESEARCH GAP — reviewer to confirm Tanzanian depreciation class/rate] |

### 3.4 Expense Patterns (Debits) — Utilities (apportion)

**Expense Patterns (Debits) — Utilities (apportion)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| LUKU, TANESCO, UMEME, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated premises; apportion if home |
| MAJI, DAWASA, WATER | Water | T2 if home office | Apportion if home |
| VODACOM, AIRTEL, TIGO, HALOTEL, TTCL, INTERNET | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) — Travel

**Expense Patterns (Debits) — Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| PRECISION AIR, AIR TANZANIA, FLIGHT, NDEGE | Flights | Deductible if business travel | Must be wholly business |
| HOTEL, BOOKING.COM, GUEST HOUSE, NYUMBA YA WAGENI | Accommodation | Deductible if business travel |  |
| BOLT, UBER, TAXI, BAJAJI, DALADALA | Local transport | Deductible if business purpose |  |
| MAFUTA, PETROL, FUEL, ORYX, PUMA, TOTAL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKING, MAEGESHO | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) — NOT Deductible

**Expense Patterns (Debits) — NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| MGAHAWA, RESTAURANT, CHAKULA, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private/entertainment — flag, no partial deduction by default |
| BINAFSI, PERSONAL, GROCERIES, DUKA, SUPERMARKET | Personal expenses | NOT deductible | Private living costs |
| FAINI, FINE, PENALTY, ADHABU | Fines/penalties | NOT deductible | Public policy |
| TRA PAYMENT, INCOME TAX, KODI YA MAPATO | Tax payments | NOT deductible | Income tax cannot reduce income |
| MATUMIZI BINAFSI, DRAWINGS, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Statutory / Exclusion Patterns

**Statutory / Exclusion Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NSSF, MFUKO WA HIFADHI | Social-security contribution | Employee NSSF (10%) deducted from gross before PAYE? — flag for reviewer [RESEARCH GAP — confirm PAYE base treatment of employee NSSF] |
| PSSSF | Social-security contribution (public) | Public-sector only |
| SDL, SKILLS DEVELOPMENT LEVY | Employer levy | Employer-only (3.5%); not an employee deduction |
| WCF, WORKERS COMPENSATION | Employer levy | Employer-only (0.5%) |
| VAT PAYMENT, TRA VAT, KODI YA ONGEZEKO | EXCLUDE | VAT liability, not expense |
| PROVISIONAL TAX, STATEMENT OF ESTIMATED TAX | Credit against liability | Not an expense |
| TRANSFER KWENDA ACCOUNT YANGU, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| LOAN, MKOPO (principal) | EXCLUDE | Loan principal movement |

### 3.8 Tanzanian Banks / Payment Rails — Statement Format Reference

**Tanzanian Banks / Payment Rails — Statement Format Reference**

| Provider | Common Patterns | Notes |
| --- | --- | --- |
| CRDB Bank | TRANSFER, MALIPO, CHARGE, FT | PDF/CSV; description holds counterparty + reference |
| NMB Bank | PAYMENT, DEPOSIT, WITHDRAWAL, FEE | PDF; common nationwide |
| NBC (National Bank of Commerce) | TRF, DD, CHARGES | PDF |
| M-Pesa / Tigo Pesa / Airtel Money | C2B, B2C, PAYBILL, LIPA, MAKATO | Mobile-money statements; very common for SMEs |
| Equity / Stanbic / Absa | PAYMENT, TRANSFER, CARD | PDF/CSV |

## Section 4 -- Worked Examples

### Example 1 — Employee PAYE, gross TZS 1,500,000/month (resident)

**Input line:**
`28/03/2025 ; CRDB ; MSHAHARA MACHI 2025 ; EMPLOYER ACME LTD ; +1,500,000 ; TZS`

**Reasoning:**
Resident employee, single employer. Monthly gross TZS 1,500,000 falls in the top band (above 1,000,000).
PAYE = 128,000 + 30% × (1,500,000 − 1,000,000) = 128,000 + 30% × 500,000 = 128,000 + 150,000 = **278,000**.
Employee NSSF = 10% × 1,500,000 = **150,000**.
Net pay = 1,500,000 − 278,000 − 150,000 = **1,072,000**.

**Classification:** PAYE = TZS 278,000; employee NSSF = TZS 150,000; net = TZS 1,072,000.

### Example 2 — Employee PAYE, gross TZS 600,000/month (resident)

**Input line:**
`28/04/2025 ; NMB ; MSHAHARA ; EMPLOYER BLUE LTD ; +600,000 ; TZS`

**Reasoning:**
Gross 600,000 falls in band 520,001–760,000.
PAYE = 20,000 + 20% × (600,000 − 520,000) = 20,000 + 20% × 80,000 = 20,000 + 16,000 = **36,000**.
Employee NSSF = 10% × 600,000 = **60,000**.
Net pay = 600,000 − 36,000 − 60,000 = **504,000**.

**Classification:** PAYE = TZS 36,000; employee NSSF = TZS 60,000; net = TZS 504,000.

### Example 3 — Self-employed presumptive, turnover TZS 9,000,000, complete records

**Input:**
Resident trader, not VAT-registered, annual turnover TZS 9,000,000, maintains complete records.

**Reasoning:**
Turnover in band 7,000,001–11,000,000 (complete records).
Tax = 90,000 + 3% × (9,000,000 − 7,000,000) = 90,000 + 3% × 2,000,000 = 90,000 + 60,000 = **150,000**.

**Classification:** Presumptive tax = TZS 150,000.

### Example 4 — Self-employed presumptive, turnover TZS 9,000,000, incomplete records

**Input:**
Same trader, but records are incomplete.

**Reasoning:**
Turnover in band 7,000,001–11,000,000 (incomplete records) → flat **250,000**.

**Classification:** Presumptive tax = TZS 250,000. (Note the penalty for poor records: TZS 100,000 higher than the complete-records case in Example 3.)

### Example 5 — Self-employed presumptive, turnover TZS 50,000,000

**Input:**
Resident trader, not VAT-registered, turnover TZS 50,000,000 (records complete or incomplete — same column above 11m).

**Reasoning:**
Band 11,000,001–100,000,000 → 3.5% of turnover regardless of records.
Tax = 3.5% × 50,000,000 = **1,750,000**.

**Classification:** Presumptive tax = TZS 1,750,000.

### Example 6 — Non-resident employee, gross TZS 4,000,000/month

**Input line:**
`28/05/2025 ; STANBIC ; SALARY ; EMPLOYER GLOBAL LTD ; +4,000,000 ; TZS`

**Reasoning:**
Non-resident employment income → flat **15% FINAL** tax (PwC; [RESEARCH GAP — reviewer to confirm against ITA Cap. 332]). Progressive bands do NOT apply.
Tax = 15% × 4,000,000 = **600,000**. This is final — no annual reconciliation on this employment income.

**Classification:** PAYE (final) = TZS 600,000.

### Example 7 — Mobile-money receipt (M-Pesa) for a trader

**Input line:**
`12/06/2025 ; M-PESA ; LIPA NA M-PESA / TILL ; CUSTOMER SALE ; +85,000 ; TZS`

**Reasoning:**
Till receipt = trading turnover. Include in annual turnover for presumptive/standard determination. If VAT-registered, extract net of 18% VAT.

**Classification:** Business income (turnover).

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency Drives Everything

- **Residency determines rate regime** — **Resident individual:** progressive monthly PAYE bands (Section 1). **Non-resident individual:** 15% flat, FINAL tax on employment income (PwC; [RESEARCH GAP — reviewer to confirm]). Confirm residency before any computation.

### 5.2 PAYE Computation (Resident)

- **PAYE computation** — Apply the monthly bands to taxable employment income. Tax-free threshold = first TZS 270,000/month. Top marginal rate 30% above TZS 1,000,000/month. PAYE is withheld by the employer and remitted by the 7th of the following month (TRA).

### 5.3 Secondary Employment

- **Secondary employment withholding** — An employee with a **second source of employment** is withheld at a flat **30%** at source on that second employment (TRA individual guidance / Big-4). Do not run the progressive bands on second-employer income.

### 5.4 Presumptive vs Standard (Self-Employed)

**Presumptive vs Standard (Self-Employed)**

| Condition | Regime |
| --- | --- |
| Resident individual, turnover ≤ TZS 100,000,000, NOT VAT-registered | Presumptive (Section 1 turnover table) |
| Turnover > TZS 100,000,000, or VAT-registered | Standard net-profit regime; full accounts required |

Records "complete" → use the lower complete-records column; "incomplete" → higher fixed amounts (TRA). Above TZS 11,000,000 turnover, both columns are identical at 3.5% of turnover.

### 5.5 Capital Gains

**Capital Gains**

| Disposer / source | Rate |
| --- | --- |
| Resident — Tanzanian-source investment | 10% (PwC) |
| Non-resident — Tanzanian-source investment | 30% (PwC) |
| Resident — overseas-source investment | 30% (PwC) |

Out of scope for routine PAYE/turnover work — flag for specialist.

### 5.6 The Wholly-and-Exclusively Principle (Standard Regime)

- **Wholly-and-exclusively principle** — Under the standard net-profit regime, an expense is deductible only if incurred wholly and exclusively in the production of income (Income Tax Act, Cap. 332). Mixed-use expenses must be apportioned on a reasonable, documented basis. Entertainment, private living costs, fines/penalties, income tax itself, and drawings are not deductible.  _(Income Tax Act, Cap. 332)_

### 5.7 Statutory Contributions

**Statutory Contributions**

| Contribution | Rate | Who pays | Source |
| --- | --- | --- | --- |
| NSSF (private) | 20% of gross | Employer ≥10% + Employee ≤10% (legal splits 10/10 or 15/5; employer may pay all 20%) | NSSF / PwC |
| PSSSF (public) | 20% of gross | Employer recovers up to 5% from employee → ~15%/5% | PwC |
| SDL | 3.5% of gross monthly emoluments | Employer-only; applies to employers with **10+ employees**; filed monthly on form ITX 300.01.E via IDRAS, due by the 7th | TRA / PwC |
| WCF (private) | 0.5% of cash sums to employees | Employer-only; filed/paid monthly | PwC |

**NSSF basis:** straight percentage of gross — NSSF publishes **no statutory ceiling or floor** on contributory wage. SDL exemptions: schools, universities, religious-run health institutions (PwC). WCF: 0.5% is the current private-sector tariff; [RESEARCH GAP — distinct public-sector WCF rate for 2025/26 not separately confirmed; use 0.5% as headline].

### 5.8 Filing Forms and Deadlines (TRA / PwC)

**Filing Forms and Deadlines**

| Item | Detail |
| --- | --- |
| PAYE monthly remittance + return | Due by the 7th of the following month (online) |
| SDL / WHT monthly returns | Same 7th-day deadline |
| Individual annual return | Form **ITX 201.01.E** ("Return of Income — Individual"); due within 6 months of year-end → file between 1 January and **30 June** |
| Who must file the annual return | Individuals with income beyond a single resident employer (business/self-employed income, multiple employers, investment income). Pure single-employer PAYE employees need not file. |
| Statement of estimated tax (provisional) | Due within 3 months of the start of the year of income (by **31 March**); provisional tax paid in 4 quarterly instalments (end of months 3, 6, 9, 12) |

### 5.9 Registration Thresholds

**Registration Thresholds**

| Item | Threshold | Source |
| --- | --- | --- |
| TIN | Required for all taxpayers / anyone in business (obtain before trading) | TRA |
| Presumptive eligibility | Turnover ≤ TZS 100,000,000 and not VAT-registered | TRA |
| VAT registration (Mainland) | TZS 200,000,000 annual taxable turnover (raised from 100m effective July 2024) | PwC / TRA |
| VAT registration (Zanzibar) | TZS 100,000,000 | PwC / TRA |
| VAT — professional service providers (accountants, lawyers, engineers) | Must register regardless of turnover | PwC / TRA |
| VAT standard rate | 18% | TRA |

### 5.10 Penalties and Interest (TRA)

**Penalties and Interest**  _(TRA, https://www.tra.go.tz/page/interest-penalties-offences)_

| Default | Charge |
| --- | --- |
| Late filing (per month / part-month) | HIGHER of 2.5% of (tax assessed − tax paid), OR 5 currency points (TZS 100,000) for an individual / 15 currency points (TZS 300,000) for a body corporate |
| Underestimation / late payment | Interest at statutory rate = Bank of Tanzania discount rate + 5%, compounded monthly [RESEARCH GAP — exact % depends on current BoT discount rate; reviewer to compute] |
| Failure to maintain documents | 1 currency point (TZS 20,000) individual / 10 currency points (TZS 200,000) corporate |
| False or misleading statement | 50% of the tax shortfall (no intent) up to 100% (intent/recklessness) |

- **Currency point** — TZS 20,000  _(TRA, https://www.tra.go.tz/page/interest-penalties-offences)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (Standard Regime)

- **Home office deduction** — Apportion rent, electricity (LUKU/TANESCO), water, internet by the proportion of the dwelling genuinely used for business. Dual-use space does not qualify. **Conservative default:** 0% until reviewer confirms a dedicated workspace and basis.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible; requires a mileage log. **Conservative default:** 0% business use until log provided.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use** — Business-use portion only; reasonable documented estimate required. **Conservative default:** 0% until business percentage confirmed.

### 6.4 Records Completeness (Presumptive)

- **Records completeness** — Whether a trader's records are "complete" determines the column used (Examples 3 vs 4 — a TZS 100,000 swing on TZS 9,000,000 turnover). Reviewer must judge whether records genuinely support the complete-records column.

### 6.5 Employee NSSF Treatment in PAYE Base

- **Employee NSSF treatment** — Whether employee NSSF (10%) is deducted from gross **before** computing PAYE materially changes the tax. [RESEARCH GAP — reviewer to confirm the statutory PAYE base treatment of employee social-security contributions.] Until confirmed, compute PAYE on gross and flag.

### 6.6 SDL Headcount Threshold

- **SDL headcount threshold** — SDL applies only to employers with **10 or more** employees. Reviewer must confirm headcount before applying or omitting the 3.5% levy. Confirm exemption status (schools/universities/religious-run health).

### 6.7 Capital Allowances / Depreciation (Standard Regime)

- **Capital allowances / depreciation** — Depreciation classes and rates under the ITA Cap. 332 Third Schedule are not enumerated in this skill. [RESEARCH GAP — reviewer to apply the correct Tanzanian depreciation class and rate for each asset.]

## Section 7 -- Excel Working Paper Template

```
TANZANIA INCOME TAX -- WORKING PAPER
Tax Year: 2025 (calendar)
Client: ___________________________
Residency: Resident / Non-resident
Type: Employee / Self-employed (presumptive) / Self-employed (standard)
Sector (if employee): Private (NSSF) / Public (PSSSF)

=== A. EMPLOYEE PAYE (monthly) ===
  A1. Gross monthly emoluments                 ___________
  A2. Band applied (per Section 1)             ___________
  A3. PAYE (resident bands OR 15% non-res)     ___________
  A4. Employee NSSF (10% of A1) [confirm base] ___________
  A5. Net pay (A1 - A3 - A4)                   ___________

=== B. EMPLOYER LEVIES (employer-only) ===
  B1. Employer NSSF (10% of gross)             ___________
  B2. SDL (3.5% of gross; 10+ employees)       ___________
  B3. WCF (0.5% of cash sums, private)         ___________

=== C. SELF-EMPLOYED PRESUMPTIVE ===
  C1. Annual turnover                          ___________
  C2. VAT-registered? (Y → not presumptive)    ___________
  C3. Records complete? (Y/N)                  ___________
  C4. Presumptive tax (per turnover table)     ___________

=== D. SELF-EMPLOYED STANDARD (turnover > 100m or VAT-reg) ===
  D1. Turnover (net of VAT if registered)      ___________
  D2. Allowable expenses (wholly & exclusively)___________
  D3. Capital allowances [class/rate – review] ___________
  D4. Net profit (D1 - D2 - D3)                ___________
  D5. Tax (pass to deterministic engine)       ___________

=== E. FILING ===
  E1. Annual return ITX 201.01.E required?     ___________
  E2. Provisional tax (statement of est. tax)  ___________
  E3. Deadline annual return: 30 June          ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Second employer? (30% flat at source)
  [ ] Sector confirmed (NSSF vs PSSSF)?
  [ ] Employee NSSF PAYE-base treatment confirmed? [RESEARCH GAP]
  [ ] SDL headcount (10+) confirmed?
  [ ] Records completeness confirmed (presumptive)?
  [ ] VAT-registration status confirmed?
  [ ] Capital allowance classes/rates confirmed? [RESEARCH GAP]
  [ ] Entertainment / personal / fines excluded?
```

## Section 8 -- Bank Statement Reading Guide

### Tanzanian Statement Formats

**Tanzanian Statement Formats**

| Provider | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| CRDB Bank | PDF, CSV | Date, Description, Debit, Credit, Balance | Description holds counterparty + reference |
| NMB Bank | PDF | Date, Particulars, Withdrawal, Deposit, Balance | Nationwide; shorter descriptions |
| NBC | PDF | Date, Narrative, Debit, Credit |  |
| M-Pesa / Tigo Pesa / Airtel Money | PDF, CSV | Date, Details, Paid In, Withdrawn, Balance | Mobile-money — critical for SMEs; includes MAKATO (fees) |
| Stanbic / Absa / Equity | PDF, CSV | Date, Description, Amount, Balance | Card transactions show merchant |

### Key Swahili / Local Banking Terms

**Key Swahili / Local Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| MSHAHARA | Salary | Employment income (PAYE) |
| MALIPO | Payment | Check direction (income / expense) |
| AMANA / HLAS | Deposit | Potential income |
| MAKATO | Charges / deduction | Bank/transaction fee (deductible if business) |
| KODI | Tax OR rent | Disambiguate: "kodi ya mapato" = income tax; "kodi ya nyumba" = rent |
| RIBA | Interest | Interest income / charge |
| GAWIO | Dividend | Investment income |
| MKOPO | Loan | Exclude principal |
| FAINI / ADHABU | Fine / penalty | NOT deductible |
| LUKU | Prepaid electricity token | Utility (apportion) |
| LIPA NA M-PESA / TILL | Merchant till receipt | Trading turnover |
| MAREJESHO | Refund | Check nature (tax refund = exclude) |

## Section 9 -- Onboarding Fallback

If the client provides data but cannot answer all onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present these questions:

```
ONBOARDING QUESTIONS -- TANZANIA INCOME TAX
1. Are you resident or non-resident in Tanzania for tax?
2. Are you an employee, self-employed, or both?
3. (Employee) Do you have a second employer? (second job = 30% flat at source)
4. (Employee) Private or public sector? (NSSF vs PSSSF)
5. (Self-employed) What is your annual turnover?
6. (Self-employed) Are you VAT-registered? Are your records complete?
7. (Employer) Do you have 10 or more employees? (SDL applies at 10+)
8. Did you pay any provisional tax (statement of estimated tax)?
9. Any other income (rental, interest, dividends, second employment)?
10. Any capital assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| PAYE bands, presumptive tax | TRA, "Income Tax for Individuals" — https://www.tra.go.tz/page/income-tax-for-individuals |
| Personal income tax (confirmation) | PwC Tax Summaries — https://taxsummaries.pwc.com/tanzania/individual/taxes-on-personal-income |
| NSSF/PSSSF/SDL/WCF | PwC "Other taxes" — https://taxsummaries.pwc.com/tanzania/individual/other-taxes |
| NSSF contribution rates | NSSF — https://www.nssf.go.tz/pages/rate-of-contributions |
| SDL | TRA — https://www.tra.go.tz/page/skills-development-levy-sdl |
| VAT | TRA — https://www.tra.go.tz/page/value-added-tax-vat |
| Filing / deadlines | PwC tax administration — https://taxsummaries.pwc.com/tanzania/individual/tax-administration |
| Penalties / interest | TRA — https://www.tra.go.tz/page/interest-penalties-offences |
| Primary law | Income Tax Act, Cap. 332; Tax Administration Act, Cap. 438 |

### Minimum Wage (Employment-Law Context — NOT a Tax Figure)

Source: Labour Institutions (Minimum Wage for Private Sector) Order, 2025 — https://tanzlii.org/en/akn/tz/act/gn/2025/605a/eng@2025-10-13.

- New private-sector wage order in force from **1 January 2026** (replaces the 2022 order); average increase ~33.4%.
- Lowest sectoral minimum: **TZS 175,000/month** (e.g. agriculture). Sector rates range up to ~TZS 644,000 (telecoms) and higher (~765,900 for international mining/energy).
- Prior 2022 benchmark (through end of 2025): ~TZS 275,060/month.
- Public-sector minimum wage raised to TZS 500,000/month in 2025 (TanzaniaInvest) [RESEARCH GAP — reviewer to confirm against gazette].

### Test Suite

Input: resident employee, gross TZS 1,500,000/month.
Expected: PAYE = 128,000 + 30%×(1,500,000−1,000,000) = **278,000**; employee NSSF 10% = 150,000; net = **1,072,000**.

Input: resident employee, gross TZS 600,000/month.
Expected: PAYE = 20,000 + 20%×(600,000−520,000) = **36,000**; employee NSSF = 60,000; net = **504,000**.

Input: resident employee, gross TZS 300,000/month.
Expected: PAYE = 8%×(300,000−270,000) = 8%×30,000 = **2,400**.

Input: resident employee, gross TZS 270,000/month.
Expected: PAYE = **0** (NIL band).

Input: trader, turnover TZS 9,000,000, complete records, not VAT-registered.
Expected: 90,000 + 3%×(9,000,000−7,000,000) = **150,000**.

Input: same trader, incomplete records.
Expected: flat **250,000**.

Input: trader, turnover TZS 50,000,000.
Expected: 3.5%×50,000,000 = **1,750,000**.

Input: non-resident, gross TZS 4,000,000/month.
Expected: 15%×4,000,000 = **600,000** (final tax). [RESEARCH GAP — confirm 15% against ITA Cap. 332.]

Expected: NSSF employee 10% + employer 10% = **20%**; PSSSF employee 5% + employer 15% = **20%**.

Input: trader, turnover TZS 120,000,000.
Expected: presumptive NOT available; standard net-profit regime, full accounts required.

## PROHIBITIONS

- NEVER apply a rate table without confirming residency.
- NEVER run progressive bands on non-resident employment income (15% flat, final) or on second-employer income (30% flat at source).
- NEVER use the complete-records presumptive column without confirming records are genuinely complete — default to the higher incomplete-records column.
- NEVER treat a VAT-registered trader, or turnover above TZS 100,000,000, as eligible for presumptive tax.
- NEVER deduct an employee's PAYE, fines/penalties, entertainment, private living costs, or drawings as a business expense.
- NEVER treat SDL or WCF as an employee deduction — they are employer-only levies.
- NEVER apply SDL without confirming the employer has 10 or more employees.
- NEVER state the statutory interest rate as a fixed number — it tracks BoT discount rate + 5%, compounded monthly.
- NEVER include VAT collected on sales in turnover/income for a VAT-registered trader.
- NEVER present tax calculations as definitive — always label as estimated and flag all [RESEARCH GAP] items for the reviewer.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
