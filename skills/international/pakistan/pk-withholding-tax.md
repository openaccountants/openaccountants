---
name: pk-withholding-tax
description: "ALWAYS read this skill before touching any Pakistan Withholding Tax (WHT) work. Use this skill whenever asked to compute, classify, withhold, deposit, or reconcile Pakistan Withholding Tax obligations under the Income Tax Ordinance 2001 (ITO 2001) as amended by Finance Acts 2024 and 2025. Trigger on phrases like \"Pakistan WHT\", \"Pakistan withholding\", \"FBR WHT rates\", \"Section 153 Pakistan\", \"filer vs non-filer rates\", \"ATL rates\", \"advance tax Pakistan\", \"WHT services Pakistan\", \"Section 149 salary withholding\", \"Section 150 dividend WHT\", \"Section 151 profit on debt\", \"Section 152 non-resident WHT\", \"Section 153 services goods contracts\", \"Section 155 rent WHT\", \"Section 156 prizes winnings\", \"Section 165 statement\", \"PSID payment slip\", \"CPR Pakistan\", \"IRIS withholding\", \"WHT credit Pakistan\", \"exemption certificate Section 159\", \"reduced rate certificate Pakistan\", \"treaty WHT Pakistan\", \"DTA Pakistan withholding\". Pakistan WHT is the largest single source of federal tax revenue in Pakistan and operates across dozens of sections of the ITO 2001 covering imports, salary, dividends, profit on debt, payments to non-residents, payments for goods/services/contracts, rent, prizes, brokerage and commission, sale by auction, motor vehicles, electricity, telephone, banking transactions, and many sector-specific levies. Rates are published in the First Schedule and Division provisions of the ITO 2001 and are amended every year by the Finance Act — always verify against the current year text on the FBR website before relying on a figure. The Active Taxpayers List (ATL) regime under Tenth Schedule applies penal rates (typically 2x to 3x) to recipients not appearing on the weekly ATL published by FBR. ALWAYS read this skill before quoting a Pakistan WHT rate, drafting a withholding letter, computing a deposit, or advising on WHT credit claims. Out of scope: provincial sales tax on services WHT (separate from federal income WHT — covered by pakistan-sales-tax skill), Workers Welfare Fund and Workers Profit Participation Fund, Federal Excise Duty mechanics, customs duty on imports beyond Section 148, bespoke SRO-based exemptions (request the actual SRO before applying), and individual income tax return assembly (refer to a Pakistan tax practitioner)."
jurisdiction: PK
domain: international
tax_year: 2025
reviewed_by: Ibrar Ali
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# pk-withholding-tax

## Pakistan — Withholding Tax — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ibrar Ali** on 2026-06-12.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### pk-withholding-tax

- **§148 Imports — commercial** — Filer 5.5% / non-filer 11%  _(ITO 2001 §148)_
- **§148 Imports — industrial own-use raw materials** — 6% for Part III, 3.5% for Part II (double for non-filer)  _(ITO 2001 §148)_
- **§150 Dividends — general** — Filer 15% / non-filer 30%  _(ITO 2001 §150)_
- **§150 Dividends — IPP / mutual fund / REIT** — 7.5%–25% for filers (15%–50% for non-filers)  _(ITO 2001 §150)_
- **§151 Profit on debt** — Filer 20% for bank profit / 15% for others (double for non-filers)  _(ITO 2001 §151)_
- **§152(1) Royalty / fee for technical services** — 15% (treaty cap may apply) — final  _(ITO 2001 §152(1))_
- **§152(1A) Non-resident contract** — 7% (no non-filer surcharge applies)  _(ITO 2001 §152(1A))_
- **§152(1AA) Insurance / reinsurance premium** — 5% (no non-filer surcharge applies)  _(ITO 2001 §152(1AA))_
- **§152(2) Other payments to non-residents** — 10%–20% per nature (no non-filer surcharge applies)  _(ITO 2001 §152(2))_
- **§153(1)(a) Goods — to company** — Filer 5% / non-filer 10%  _(ITO 2001 §153)_
- **§153(1)(a) Goods — to individual / AOP** — Filer 5.5% / non-filer 11%  _(ITO 2001 §153)_
- **§153(1)(b) Services — general** — Filer 9% (company) / 11% (others) (2x for non-filers)  _(ITO 2001 §153)_
- **§153(1)(b) Services — low-margin sectors** — Filer 4% / non-filer 8%  _(ITO 2001 §153)_
- **§153(1)(c) Contracts** — Filer 7.5% (company) / 8% (others)  _(ITO 2001 §153)_
- **§153(2) Sportspersons** — 15% / 30% (final)  _(ITO 2001 §153(2))_
- **Prescribed-person threshold** — Companies; AOPs/individuals with turnover ≥ PKR 100M  _(ITO 2001 §153(7))_
- **§155 Rent — individuals / AOPs** — Slab: 0% to 300k; then 5% / 10% / 25%  _(ITO 2001 §155)_
- **§155 Rent — companies** — Filer 15% / non-filer 30% (flat)  _(ITO 2001 §155)_
- **§156 Prize bonds** — Filer 15% / non-filer 30% (final)  _(ITO 2001 §156)_
- **§156 Raffle / lottery / quiz** — Filer 20% / non-filer 40% (final)  _(ITO 2001 §156)_
- **§156A Petroleum commission** — 12% / 24% (final)  _(ITO 2001 §156A)_
- **§236C Sale of immovable property (seller)** — Slab based on value: Filer 4.5% to 5.5% / Non-filer 11.5%  _(ITO 2001 §236C)_
- **§236K Purchase of property (buyer)** — Slab based on value: Filer 1.5% to 2.5% / Non-filer 10.5% to 18.5%  _(ITO 2001 §236K)_
- **§231A Cash withdrawal (non-filer > 50k/day)** — 0.008  _(ITO 2001 §231A)_
- **§154 Export proceeds** — 1% filer / 2% non-filer (minimum tax)  _(ITO 2001 §154)_
- **Tax point §158** — Earlier of payment or credit; base includes sales tax  _(ITO 2001 §158)_
- **Deposit deadline (companies)** — Within 7 days of end of the week of deduction  _(Income Tax Rules 2002, Rule 43)_
- **Monthly §165 statement** — Quarterly, on or before the 20th day of the month following the end of each quarter  _(ITO 2001 §165)_
- **Annual reconciliation** — By the due date of filing the return of income  _(ITO 2001 §165)_
- **Late §165 statement penalty** — Rs 5,000 (if paid & filed within 90 days); otherwise PKR 2,500 per day (minimum PKR 10,000)  _(ITO 2001 §182)_
- **Failure to deduct** — Expense disallowed (§21(c)); recovery from payer (§161); plus default surcharge (§205) and penalties (§182)  _(ITO 2001 §21(c)/§161)_
- **§159 reduced-rate / exemption certificate** — Available on IRIS; must be held before payment  _(ITO 2001 §159)_

## Section 1 — Quick reference (rate table by section)

**Section 1 — Quick reference field/value table**

| Field | Value |
| --- | --- |
| Country | Islamic Republic of Pakistan |
| Tax covered | Withholding Tax (WHT) under the Income Tax Ordinance 2001 — advance and final income tax collected at source on a very wide range of payments and transactions |
| Currency | Pakistani Rupee (PKR, Rs) — foreign-currency payments converted at the SBP interbank rate on the date of payment unless the contract specifies otherwise |
| Tax year | 1 July to 30 June (financial year) |
| Current tax year | **TY 2025-26 (Finance Act 2025)** — rates below reflect FA 2025 amendments; verify the current First Schedule and Division provisions on FBR website before relying |
| Federal tax authority | Federal Board of Revenue (FBR) — operates through Inland Revenue Field Offices (LTUs, MTUs, RTOs) |
| Filing portal | **IRIS** (https://iris.fbr.gov.pk) — for all WHT statements, returns, payment challans, and exemption certificate applications |
| Payment instrument | **CPR (Computerized Payment Receipt)** — generated by the bank upon deposit of WHT via a **PSID (Payment Slip ID)** created on IRIS |
| Monthly statement | **Section 165** withholding statement — filed monthly through IRIS by every withholding agent listing every deduction made in the month |
| Annual reconciliation | Annual Section 165 reconciliation statement |
| ATL impact | Recipients not on the Active Taxpayers List published weekly by FBR pay penal rates under the **Tenth Schedule** — typically 2x the standard rate, and up to 3x for certain categories |
| WHT credit | Tax deducted under most sections (Section 153 services, 153 goods adjustable, 155 rent, 148 imports adjustable, etc.) is creditable against the recipient's annual income tax liability; tax deducted under "final tax regime" (FTR) sections (e.g. 150 dividends, 151 profit on debt for individuals, 152(1) royalties/fees for technical services to non-residents, some 153 goods, 156 prizes) is **final** and not refundable |
| Governing law | **Income Tax Ordinance 2001** as amended by Finance Act 2024 and Finance Act 2025; Income Tax Rules 2002; **Tenth Schedule** (ATL/non-ATL rates); **First Schedule** (rates of tax) |
| Validated by | Pending — requires sign-off by a qualified Pakistan tax practitioner (ICAP-registered Chartered Accountant or ICMAP-registered Cost & Management Accountant or FBR-registered Income Tax Practitioner) |
| Skill version | 1.0 |

### Quick-look: section → payment type → rate (filer vs non-filer)

**Quick-look: section → payment type → rate table**

| Section | Payment type | Filer (ATL) rate | Non-filer (non-ATL) rate | Adjustable / Final |
| --- | --- | --- | --- | --- |
| **148** | Imports (commercial importer) | 5.5% (general goods, value-based) | 11% | Adjustable for most goods; minimum tax for some categories |
| **148** | Imports (industrial undertaking — raw materials for own use) | 6% (Part III) / 3.5% (Part II) | 2x | Adjustable |
| **149** | Salary | Progressive slab (0% to **35%** for income above Rs 4.1m for non-salaried; salaried slabs separate) | n/a (employer withholds per slabs) | Adjustable against annual tax |
| **150** | Dividends — general | **15%** | 30% | **Final** for most recipients |
| **150** | Dividends — IPP / mutual fund / REIT (special categories) | 7.5% – 25% (filers) | 15% – 50% (non-filers) | Final |
| **151** | Profit on debt (bank deposits, savings certificates, bonds) | **20% (bank profit) / 15% (others)** (where yield exceeds Rs 5m, higher rates apply) | 2x | **Final** for individuals up to threshold; adjustable for companies |
| **152(1)** | Royalty / fee for technical services to non-resident | 15% (treaty cap may apply) | 15% | Final (subject to treaty) |
| **152(1A)** | Non-resident contract execution (construction, assembly, services in PK) | 7% (PE-attributable) | no non-filer surcharge applies | Final / minimum tax depending on election |
| **152(2)** | Other payments to non-residents (general) | 10% – 20% per nature | no non-filer surcharge applies | Generally final |
| **152(2A)** | Payments to non-resident for services rendered to PE | 7% – 15% | 2x | Adjustable / final per election |
| **153(1)(a)** | Sale of **goods** — to company | **5%** | 10% | Adjustable (companies); minimum tax for many cases |
| **153(1)(a)** | Sale of **goods** — to individuals / AOPs | **5.5%** | 11% | Minimum tax for many categories |
| **153(1)(b)** | Rendering of **services** — general | **9% (company) / 11% (others)** | 2x | **Minimum tax** (effectively final at the rate but creditable beyond it) |
| **153(1)(b)** | Services — specified low-margin sectors (transport, freight forwarding, security, etc.) | 4% | 8% | Minimum tax |
| **153(1)(c)** | Execution of **contracts** (construction, supply contracts) | **7.5% (company) / 8% (others)** | 2x | Minimum tax / adjustable |
| **153(2)** | Sportspersons | 15% | 30% | Final |
| **155** | Rent of immovable property — individuals / AOPs | Slab: 0% up to Rs 300k, then 5% / 10% / 25% on higher slabs | 2x | Adjustable |
| **155** | Rent of immovable property — companies | 15% flat | 30% | Adjustable |
| **156** | Prizes and winnings — prize bonds | 15% | 30% | Final |
| **156** | Prizes and winnings — raffle, lottery, quiz | 20% | 40% | Final |
| **156A** | Petroleum products commission to petrol pump operators | 12% | 24% | Final |
| **156B** | Withdrawal of pension fund balance | Varies | 2x | Final |
| **231A** | Cash withdrawal from bank (non-ATL only, above Rs 50k/day) | n/a (filers exempt) | **0.008 (0.8%)** | Adjustable |
| **231B** | Purchase / transfer of motor vehicles | Slab by engine capacity / value | 2x – 3x | Adjustable |
| **234** | Motor vehicle tax (collected with token) | Slab | 2x | Adjustable |
| **235** | Electricity consumption — commercial / industrial | Slab on monthly bill | 2x for non-filers | Adjustable up to threshold; minimum tax above |
| **236** | Telephone and internet subscribers | Varies | n/a | Adjustable / final |
| **236A** | Sale by auction | 10% | 20% | Adjustable |
| **236C** | Sale / transfer of immovable property — seller | Slab: 4.5%–5.5% (filer) | 11.5% (non-filer) | Adjustable; final if holding period > 6 yr in some cases |
| **236K** | Purchase of immovable property — buyer | Slab: 1.5%–2.5% (filer) | 10.5%–18.5% (non-filer) | Adjustable |
| **236G/H** | Sales to distributors / retailers (specified sectors) | 0.1% – 2% | 2x | Minimum tax |

- **Critical rule (Section 158)** — WHT must be deducted **at the time the amount is actually paid** OR **when credited to the account of the recipient**, whichever is earlier. The base is the gross amount **including sales tax** (where Pakistan federal/provincial sales tax has been charged separately on the invoice).  _(Section 158)_
- **Critical rule (Tenth Schedule, ATL regime)** — Before applying any rate, the withholding agent must check the **weekly Active Taxpayers List (ATL)** published by FBR (and the provincial ATLs for sales tax purposes) on the FBR website. If the recipient's NTN/CNIC does not appear on the ATL on the date of payment, the higher non-filer rate applies. Print or screenshot the ATL check as part of the working paper.  _(Tenth Schedule)_
- **Critical rule (Section 159 exemption certificate)** — A recipient may apply on IRIS for a **reduced-rate** or **exemption** certificate. The certificate must be on hand at the date of payment — verbal claims do not suffice. The certificate is section-specific and time-bound.  _(Section 159)_

## Section 2 — Required inputs and refusal catalogue

### 2.1 Mandatory inputs before any WHT computation

**Mandatory inputs table**

| Input | Why it matters |
| --- | --- |
| Withholding agent identity, NTN (National Tax Number), entity type (company, AOP, individual, government department, PE of non-resident) | Determines whether obligation arises under Section 153 (only "prescribed persons" are agents under 153), and reporting cadence |
| Recipient legal name, CNIC (if individual) or NTN (if company/AOP), and tax residence | Determines resident-vs-non-resident regime and ATL status |
| **ATL status of recipient at the date of payment** — screenshot of FBR ATL search | Drives filer vs non-filer rate (typically 2x for non-ATL) |
| Nature of the payment (goods, services, contract, rent, dividend, profit on debt, royalty, FTS, prize, commission, brokerage, sale by auction, immovable property, vehicle, etc.) | Drives section and rate |
| Whether the recipient holds a Section 159 exemption / reduced-rate certificate, and certificate copy | Without certificate on hand, full rate applies even if recipient is eligible |
| Gross invoice amount, broken down between price and sales tax (federal STA 1990 or provincial SST) | WHT base excludes sales tax |
| Date of payment OR accrual, whichever is earlier | Tax point under Section 158 |
| For non-resident recipients claiming treaty relief: Tax Residence Certificate (TRC) and Form 10F-equivalent declaration | Treaty relief denied without TRC on hand at payment date |
| For Section 153 services to specified low-margin sectors (transport, freight forwarding, security, etc.): documentary evidence of sector classification | Drives the reduced 4% / 8% rate vs general 11% / 22% |
| For Section 148 imports: H.S. code, customs assessed value, and import status (commercial vs industrial own-use) | Drives rate band in the First Schedule |
| Bank account details for PSID generation (NTN of withholding agent and head of account) | Required to generate the PSID and obtain the CPR |

Refuse to compute Pakistan WHT without ALL of the following:

### 2.2 Refusal catalogue

**Refusal catalogue table**

| # | Situation | Reason |
| --- | --- | --- |
| R-PK-WHT-1 | Provincial sales tax on services WHT (Sindh SST, Punjab PST, KPK and Balochistan SST, Islamabad ICT-ST) | Distinct provincial regimes; route to pakistan-sales-tax. |
| R-PK-WHT-2 | Workers Welfare Fund (WWF) and Workers Profit Participation Fund (WPPF) | Separate labour-law levies; refer to a Pakistan tax practitioner. |
| R-PK-WHT-3 | Federal Excise Duty mechanics | Distinct regime under Federal Excise Act 2005. |
| R-PK-WHT-4 | Customs duty, regulatory duty, additional customs duty on imports beyond the Section 148 income-tax slice | Customs Act 1969 — refer to a licensed customs clearing agent. |
| R-PK-WHT-5 | Bespoke SRO (Statutory Regulatory Order) exemption claims without sight of the actual SRO | SROs are tightly drafted and time-bound; refuse without the document. |
| R-PK-WHT-6 | Treaty rate claim without a valid TRC dated on or before the payment date | Apply statutory non-resident rate. |
| R-PK-WHT-7 | Section 152(1A) PE-attribution and election questions for non-resident contractors | Requires PE analysis under Section 6 + treaty Article 5; refer to a Pakistan tax practitioner. |
| R-PK-WHT-8 | Final-Tax-Regime vs Normal-Tax-Regime classification dispute (whether a payment is FTR or NTR for the recipient's annual return) | Requires recipient-level analysis; refer to a Pakistan tax practitioner. |
| R-PK-WHT-9 | Petroleum, banking, insurance, power sector, IPP, REIT, mutual fund specials beyond the headline rate | Sector-specific Schedules to ITO 2001 (Second, Third, Fourth, Fifth, Seventh, Eighth Schedules) — refer to specialist. |
| R-PK-WHT-10 | Tax credit refund applications and IRIS dispute resolution beyond a routine reconciliation | Refer to a Pakistan tax practitioner / FTO. |
| R-PK-WHT-11 | Cross-jurisdictional WHT split where the same payment touches federal income WHT and provincial sales-tax WHT | Coordinate with pakistan-sales-tax skill but refuse to issue a combined determination without provincial confirmation. |

Refuse the engagement (explicit refusal, do not guess) in any of the following cases:

## Section 3 — Tier 1: common sections

### 3.1 Section 148 — Imports

- **Trigger** — Any import of goods into Pakistan cleared through Customs.  _(Section 148)_
- **Mechanics — collection point** — WHT is collected by the **Collector of Customs** at the time of clearance — the importer does not "withhold" in the usual sense; the duty/tax is paid at port via the customs assessment.  _(Section 148)_
- **Rate basis** — Rate is per the **First Schedule, Part II** — varies by H.S. code, commercial vs industrial-undertaking-for-own-use status, and ATL status.  _(First Schedule, Part II)_
- **General commercial import** — 5.5% (filer) / 11% (non-filer) on the customs-assessed value plus customs duty plus federal excise (the "import value" for tax purposes)  _(Section 148)_
- **Industrial undertaking raw materials for own use** — typically 6% for Part III / 3.5% for Part II depending on the item category (double for non-filers)  _(Section 148)_
- **Adjustable vs minimum tax** — WHT under 148 is **adjustable** against the importer's annual income tax for most categories, but is treated as **minimum tax** for certain finished-goods imports under SRO regimes — verify per current SRO.  _(Section 148)_
- **CPR for Section 148** — The CPR for Section 148 is the **Goods Declaration (GD)** assessment showing the WHT line item.  _(Section 148)_

Capture the GD number, the H.S. code, the assessed import value, customs duty, FED if any, ATL status of the importer, and the WHT line on the GD assessment.

### 3.2 Section 149 — Salary

- **Trigger** — Any payment of salary by an employer to an employee resident or non-resident, where the salary is sourced in Pakistan.  _(Section 149)_
- **Estimated annual liability withholding** — Employer must compute the **estimated annual tax liability** of the employee at the start of the tax year (or on joining), divide by 12, and withhold a 1/12 share each month.  _(Section 149)_
- **Salary slabs TY 2025-26** — Salaried slabs run from 0% (income up to Rs 600k) through progressive bands up to a top marginal rate of 35% (salaried) on income above the topmost threshold. (per FA 2025 — verify)  _(FA 2025)_
- **Non-salaried slabs** — Non-salaried (business / AOP / individual professional) slabs are different and reach 35% above the top threshold.  _(Section 149)_
- **In-year adjustment** — The employer adjusts during the year if salary, allowances, bonuses, or tax credits change.  _(Section 149)_
- **Tax credits against Section 149 withholding** — Section 60C — interest on house loan; Section 61 — donations to approved institutions; Section 63 — voluntary pension fund contributions; Section 62 — investment in shares / mutual funds / Sukuks (capped). Employee must inform employer in writing.  _(Sections 60C, 61, 62, 63)_
- **Adjustability** — Salary WHT is **adjustable** — credited against the employee's annual return liability.  _(Section 149)_
- **Annual salary certificate** — Section 149(1)(b) requires the employer to issue **annual salary certificate** to the employee on Form annexed to the rules.  _(Section 149(1)(b))_

### 3.3 Section 150 — Dividends

- **Trigger** — Distribution of dividends by a Pakistan-resident company (or a non-resident company on Pakistan-source profits subject to s.5).  _(Section 150)_
- **Standard rate** — 15% (filer) / 30% (non-filer) on the gross dividend  _(Section 150)_
- **Reduced rates for specified categories** — Reduced rates apply for specified categories (IPPs, mutual funds, REIT distributions, certain industries) per the First Schedule Part III.  _(First Schedule Part III)_
- **Deduction point** — WHT is deducted by the company paying the dividend at the time of payment / credit.  _(Section 150)_
- **Individuals / AOPs treatment** — For recipients who are individuals or AOPs, dividend WHT is final tax — no further income tax is payable and no expenses are deductible.  _(Section 150)_
- **Companies treatment** — For recipients who are companies, dividend WHT is adjustable against CIT, but inter-corporate dividend relief under Section 103 may apply.  _(Section 103)_
- **Bonus shares** — Bonus shares are subject to separate WHT regime where applicable (verify current FA).

### 3.4 Section 151 — Profit on debt

- **Trigger** — Payment of interest / profit on debt by a Pakistan-resident payer (bank, NBFC, government, company, individual) on bank deposits, savings certificates, government bonds, sukuks, term finance certificates, or general lending.  _(Section 151)_
- **Standard rate** — 20% for bank profit / 15% for others (filer); double for non-filers on the gross profit on debt  _(Section 151)_
- **Yield threshold** — For individual recipients where yield exceeds Rs 5m in a tax year, higher rates may apply per First Schedule.  _(First Schedule)_
- **Individual/AOP treatment** — For most individual / AOP recipients, profit on debt WHT is final tax on amounts up to the threshold; beyond it, treatment shifts to normal regime in some cases — confirm per current FA.  _(Section 151)_
- **Company treatment** — For company recipients, it is adjustable against CIT.  _(Section 151)_
- **Deduction point** — Banks withhold automatically at the time of credit to the depositor's account.  _(Section 151)_

### 3.5 Section 152 — Payments to non-residents

**Section 152 sub-section table**

| Sub-section | Payment type | Standard rate | ATL impact |
| --- | --- | --- | --- |
| 152(1) | Royalty | 15% | Treaty-capped (typically 10%-15%) |
| 152(1) | Fee for technical services (FTS) | 15% | Treaty-capped (typically 10%-15%) |
| 152(1AA) | Insurance / reinsurance premium | 5% | no non-filer surcharge applies |
| 152(1A) | Non-resident contract (construction, assembly, services with site presence) | 7% | no non-filer surcharge applies; election of FTR vs NTR available |
| 152(2) | Other payments to non-residents (general default) | 20% | no non-filer surcharge applies |
| 152(2A) | Payment to non-resident with PE in PK for services | 7% – 15% per nature | 2x non-filer |

- **Royalty** — 15%  _(152(1))_
- **Fee for technical services (FTS)** — 15%  _(152(1))_
- **Insurance / reinsurance premium** — 5%  _(152(1AA))_
- **Non-resident contract (construction, assembly, services with site presence)** — 7%  _(152(1A))_
- **Other payments to non-residents (general default)** — 20%  _(152(2))_
- **Payment to non-resident with PE in PK for services** — 7% – 15% per nature  _(152(2A))_
- **Treaty relief requirements** — Pakistan has DTAs with 60+ countries. To claim the reduced treaty rate at source, the withholding agent must hold: A valid Tax Residence Certificate (TRC) issued by the recipient's home tax authority covering the payment period; A declaration from the recipient that they are the beneficial owner and have no PE in Pakistan to which the income is attributable; A copy of the contract and invoice. Without the TRC at the payment date, apply the statutory rate; the recipient may later file a refund claim with FBR.  _(Section 152)_

### 3.6 Section 153 — Payments for services, goods, and contracts

**This is the largest and most-litigated WHT section in Pakistan. Read carefully.**

- **Trigger** — A "prescribed person" — defined in Section 153(7) — makes a payment for: (a) Sale of goods; (b) Rendering of services; (c) Execution of a contract (other than sale of goods or services).  _(Section 153(7))_
- **Prescribed persons** — Prescribed persons include: federal/provincial governments, local authorities, companies, AOPs with turnover ≥ Rs 100m, foreign contractors with PE, exporters of goods, and certain individuals with turnover ≥ Rs 100m. Individuals below the threshold and small AOPs are not prescribed persons and have no Section 153 obligation.  _(Section 153(7))_

**Rates (per FA 2025 — verify)**  _(FA 2025)_

| Limb | Recipient type | Filer rate | Non-filer rate | Status |
| --- | --- | --- | --- | --- |
| 153(1)(a) — goods | Company | **5%** | 10% | Adjustable for most; minimum tax for specified goods |
| 153(1)(a) — goods | Individual / AOP | **5.5%** | 11% | Generally minimum tax |
| 153(1)(b) — services — general | Any | **9% (company) / 11% (others)** | 2x | Minimum tax |
| 153(1)(b) — services — specified low-margin sectors | Any | **4%** | 8% | Minimum tax |
| 153(1)(c) — contracts | Company | **7.5%** | 2x | Minimum tax / adjustable |
| 153(1)(c) — contracts | Individual / AOP | **8%** | 2x | Generally minimum tax |
| 153(2) — sportspersons | Individual | 15% | 30% | Final |

- **Specified low-margin services (4%/8% rate)** — Specified low-margin services (4%/8% rate) include transport, freight forwarding, security guarding, advertising commission, software development services (subject to specific notification), and others — verify the current SRO notification listing eligible categories.
- **Goods vs services vs contract classification** — The classification drives the rate. A "supply of goods" with installation is typically a contract under 153(1)(c). A pure "service" with no goods component is 153(1)(b). A pure sale of inventory off-the-shelf is 153(1)(a).  _(Section 153)_
- **Sales tax exclusion** — Base is invoice value excluding federal STA 1990 sales tax and any provincial sales tax on services.  _(Section 153)_
- **Minimum tax** — For most 153 payments to individuals/AOPs, the WHT is minimum tax, meaning the recipient cannot get a refund below the WHT amount even if their normal computation would yield a lower tax.  _(Section 153)_
- **Reduced-rate certificate (Section 159)** — Common in 153(1)(b) services where recipient is a regular filer with documented losses or low-margin business; certificate is application-driven on IRIS.  _(Section 159)_

### 3.7 Section 155 — Rent of immovable property

- **Trigger** — Payment of rent for use of land, buildings, plant fitted to a building, or furniture by a "prescribed person" (Section 155 has its own definition, broadly mirroring 153).  _(Section 155)_
- **Individuals / AOPs rent slab** — Rs 0 – Rs 300,000 / year: 0%; Rs 300,001 – Rs 600,000: 5% on excess; Rs 600,001 – Rs 2,000,000: Rs 15,000 + 10% on excess; Rs 2,000,001 – Rs 4,100,000: Rs 155,000 + 25% on excess; Above Rs 4,100,000: Rs 470,000 + 25% on excess. (Verify current FA 2025 slabs.)  _(Section 155)_
- **Companies receiving rent** — 15% (filer) / 30% (non-filer) flat  _(Section 155)_
- **Non-filer rate** — Non-filer recipients: 2x the filer rate.  _(Section 155)_
- **Adjustability** — WHT under 155 is adjustable against the recipient's annual income tax.  _(Section 155)_

### 3.8 Section 156 — Prizes and winnings

- **Trigger** — Award of a prize, raffle, lottery, quiz, or winnings from a draw / promotional scheme.  _(Section 156)_
- **Prize bonds (SBP-issued)** — 15% (filer) / 30% (non-filer)  _(Section 156)_
- **Raffle / lottery / quiz prizes / promotional draws** — 20% (filer) / 40% (non-filer)  _(Section 156)_
- **Deduction point** — Tax is deducted before delivery of the prize by the prize-awarding entity.  _(Section 156)_
- **Final tax treatment** — WHT under 156 is final tax — the recipient does not include the winnings in normal income.  _(Section 156)_
- **Non-cash prizes** — Non-cash prizes: tax is computed on the fair market value of the prize and must be collected from the recipient before delivery (or grossed up in the prize design).  _(Section 156)_

### 3.9 Section 165 — Monthly and annual statements

- **Statement filing requirement** — Statement (Form prescribed) — through IRIS, quarterly, on or before the 20th day of the month following the end of each quarter, listing every WHT deduction made in the quarter with: recipient NTN/CNIC, recipient name, section, gross amount, WHT amount, CPR number, and date of deposit.  _(Section 165)_
- **Annual Reconciliation Statement** — Annual Reconciliation Statement — through IRIS, by the due date of filing the return of income, reconciling all quarterly statements.  _(Section 165)_
- **Consequences of non-filing — penalty** — Penalty under Section 182 — Rs 2,500 per day, minimum Rs 50,000 per default.  _(Section 182)_
- **Consequences of non-filing — disallowance** — Disallowance of expense under Section 21(c) — any payment from which WHT was not deducted (or not deposited) is disallowed for income tax purposes in the payer's own computation.  _(Section 21(c))_

## Section 4 — Tier 2: sector specials, treaty rates, tax credits, exemption certificates

### 4.1 Sector specials

**Sector specials table**

| Sector | Special regime |
| --- | --- |
| **Banking** | Seventh Schedule — banks taxed under separate computation; WHT on deposits per Section 151; banks also act as withholding agents on cash withdrawal (231A), banking transactions (236P, where in force), and customer transactions |
| **Insurance** | Fourth Schedule — insurance companies taxed under separate computation; premium WHT under Section 152(1AA) for reinsurance to non-residents |
| **Petroleum exploration & production** | Fifth Schedule — separate regime; royalty and PSC mechanics outside scope of this skill |
| **Petroleum products distribution** | Section 156A — 12% (filer) / 24% (non-filer) on commission to petrol pump operators, **final** |
| **Independent Power Producers (IPPs)** | Section 150 dividend WHT reduced to **7.5%** for specified IPP categories; separate corporate tax holiday under Second Schedule |
| **REITs / Mutual Funds** | Reduced dividend WHT (typically 7.5% for individuals, 25% for non-filers); pass-through treatment under Second Schedule |
| **Construction & developers** | Third Schedule — special tax regime under Section 100D; affects WHT treatment of progress payments |
| **Exporters** | Section 154 — export proceeds realized through banks subject to **1% WHT (filer) / 2% (non-filer)**, generally **minimum tax**; exporter's normal-regime election available subject to conditions |
| **Software & IT services exports** | Section 154A — **0.25%** on export proceeds realized through banks (concessional); subject to PSEB registration and other conditions |
| **Telecom** | Section 236 — subscriber WHT 15% on prepaid / postpaid bills |
| **Electricity** | Section 235 — commercial / industrial bills (slab); separate from domestic |
| **Stock market** | Section 233A — sale / purchase of shares through stock exchange — broker withholds at 0.02% (verify) |

### 4.2 Treaty rates (illustrative — verify the actual DTA before relying)

**Treaty rates table**

| Country | Dividend | Interest | Royalty | FTS |
| --- | --- | --- | --- | --- |
| United Kingdom | 15% / 20% | 15% | 12.5% | n/a (no FTS Article — falls under Other Income or Business Profits) |
| United States | 15% / 20% | n/a (US-PK DTA limited) | 0% (govt) / 15% | n/a |
| China | 10% | 10% | 12.5% | 12.5% |
| UAE | 10% / 15% | 10% | 12% | 12% (in some interpretations) |
| Saudi Arabia | 10% | 10% | 10% | 10% |
| Germany | 10% / 15% | 10% / 20% | 10% | 10% |
| Switzerland | 10% / 20% | 10% | 10% | 10% |
| Singapore | 10% / 12.5% | 12.5% | 10% | 10% |

Pakistan's standard DTA caps for major partners (top of the headline rate). The DTA rate caps the statutory rate only when: the recipient is the beneficial owner; the recipient is resident in the treaty partner state (TRC required); no LOB / PPT / anti-treaty-shopping provision is triggered; the income is not effectively connected to a PE in Pakistan (in which case Section 152(1A) PE-attribution rules apply).

### 4.3 Tax credits and refunds

- **Adjustable WHT** — Tax deducted under sections that are adjustable (e.g. 149 salary, 148 imports for most categories, 153 services to companies, 155 rent, 231A cash withdrawal, 231B vehicles, 236K property purchase) is credited against the recipient's annual income tax liability on the return.
- **Final tax WHT** — Tax deducted under final tax regime sections (150 dividends, 151 profit on debt for individuals, 152(1) royalty/FTS, 153 sportspersons, 154 exports, 156 prizes, 156A petroleum commission, etc.) is not refundable — it is the recipient's final liability on that income. The recipient does not include the gross income in normal taxable income.
- **Minimum tax** — Tax deducted as minimum tax (most 153 services and 153 goods to individuals/AOPs) is credited but only down to the minimum — if normal computation yields less than the WHT, the WHT amount stands as the floor.
- **Refund procedure** — Excess WHT (where annual tax liability is less than total adjustable WHT, including legitimate Section 159 over-deduction) is refunded on application via IRIS using the income tax return as the refund claim. Refund processing is slow in practice — set client expectations accordingly.

### 4.4 Section 159 — Exemption / reduced-rate certificates

- **When to apply** — A recipient should apply for a 159 certificate when: It is a regular filer with documented historical losses or low margins; The statutory WHT rate would exceed its expected annual tax liability (creating chronic refund position); It enjoys a sector-specific exemption / reduced rate that requires certification.  _(Section 159)_
- **Process** — Application on IRIS by the recipient (or its tax representative). Commissioner reviews and issues certificate specifying section, recipient, payer (or "all payers"), period, and rate (zero or reduced). Certificate is time-bound — typically valid for a tax year or shorter. Withholding agent must hold the certificate before the date of payment to apply the reduced rate.  _(Section 159)_

## Section 5 — Worked examples

### Example 5.1 — Section 153 services to a company (filer)

**Facts.** Karachi-based company A pays Karachi-based consulting firm B (private limited company, ATL filer) Rs 1,180,000 inclusive of 18% sales tax for advisory services.

**Computation.**
- Strip sales tax: gross fee = 1,180,000 / 1.18 = **Rs 1,000,000**.
- Section 153(1)(b) general services rate (filer): **11%**.
- WHT to deduct = 1,000,000 × 11% = **Rs 110,000**.
- Net paid to B = 1,000,000 (fee) − 110,000 (WHT) + 180,000 (sales tax payable to B who pays output sales tax) = **Rs 1,070,000**.
- Generate PSID on IRIS, deposit Rs 110,000 by next deposit deadline, obtain CPR, report on monthly 165 statement.

### Example 5.2 — Section 153 services (non-filer)

Same facts but B is **not on ATL** at the date of payment.

- Rate doubles to **22%**.
- WHT = 1,000,000 × 22% = **Rs 220,000**.
- Net paid = 1,000,000 − 220,000 + 180,000 = **Rs 960,000**.
- (Encourage B to file and appear on ATL to recover refund position via annual return.)

### Example 5.3 — Section 152 royalty to UK resident (with TRC)

**Facts.** Pakistan company pays £100,000 royalty to UK-resident IP owner. TRC and beneficial-ownership declaration on file. UK-PK DTA caps royalty at 12.5%.

**Computation.**
- Statutory rate (152(1)): 15%.
- Treaty-capped: **12.5%**.
- WHT = £100,000 × 12.5% = **£12,500**, converted to PKR at SBP interbank rate on payment date.
- Deposit via PSID; report on monthly 165 statement.
- Final tax — recipient has no further Pakistan tax obligation on this royalty.

### Example 5.4 — Section 148 commercial import

**Facts.** Importer X (filer) imports finished goods, customs assessed value PKR 10,000,000, customs duty 20% = 2,000,000, no FED.

**Computation.**
- Import value for income tax = 10,000,000 + 2,000,000 = **Rs 12,000,000**.
- Section 148 general commercial rate (filer): **5.5%**.
- WHT = 12,000,000 × 5.5% = **Rs 660,000**, collected by Customs at GD assessment.
- Adjustable against X's annual CIT.

### Example 5.5 — Section 155 rent to individual landlord (filer)

**Facts.** Company tenant pays individual landlord (ATL filer) Rs 2,400,000 annual rent.

**Computation (slab — verify FA 2025 figures).**
- First 300,000 — 0%
- Next 300,000 (to 600,000) — 5% on excess of 300,000 = 15,000
- Next 1,400,000 (to 2,000,000) — 10% on excess of 600,000 = 140,000
- Next 400,000 (to 2,400,000) — 15% on excess of 2,000,000 = 60,000
- Total annual WHT = **Rs 215,000**, deducted monthly as 17,917 per month from rent payments.

### Example 5.6 — Section 153 with Section 159 reduced certificate

**Facts.** Company X holds a Section 159 certificate from FBR reducing Section 153(1)(b) services WHT to **2%** for the period 1 July 2025 – 30 June 2026. Company Y (prescribed person) pays X Rs 500,000 for services.

**Computation.**
- Apply reduced certificate rate: **2%**.
- WHT = 500,000 × 2% = **Rs 10,000**.
- Y must attach the certificate reference (number + date) to the monthly 165 statement.

## Section 6 — Filing and payment

### 6.1 Payment workflow — PSID → CPR

- **PSID to CPR workflow** — 1. Log in to IRIS as the withholding agent (NTN-based credentials). 2. Navigate to e-Payments → Create PSID. 3. Select Tax Year, Section (148/149/150/151/152/153/155/156/etc.), Head of Account (income tax — corporate / non-corporate as applicable). 4. Enter recipient details (NTN/CNIC, name, section sub-clause), gross amount, rate applied, WHT amount. 5. Generate PSID — print or save the PDF (contains a unique PSID number and barcode). 6. Take PSID to any authorised branch of a scheduled bank (1Link member) or pay via internet banking linked to the bank's FBR module. 7. Bank issues CPR (Computerized Payment Receipt) with a unique CPR number, deposit date, and amount. 8. CPR is auto-reflected on IRIS within 24-48 hours; reconcile against the PSID before filing the monthly 165 statement.

### 6.2 Deposit deadlines

**Deposit deadlines table**

| Withholding agent type | Deposit deadline |
| --- | --- |
| Government departments | Same day / next working day after deduction |
| Companies | Within **7 days** of the end of the week in which deduction was made (per Rule 43 of Income Tax Rules) |
| Other withholding agents | Within **7 days** of the end of the fortnight in which deduction was made |
| Section 148 imports | Collected by Customs at GD assessment — no separate deposit by importer |

In practice, most withholding agents deposit weekly to stay current. The Section 165 statement is filed quarterly, on or before the 20th day of the month following the end of each quarter, listing all deposits made.

### 6.3 Monthly Section 165 statement (IRIS)

- **Due date** — 20th of the month following the end of each quarter (quarterly filing).  _(Section 165)_
- **Mode** — IRIS — upload of CSV / direct entry / API for ERP integrations.
- **Content** — Every deduction in the month, line by line — recipient NTN/CNIC, name, section, gross amount, WHT amount, CPR number, CPR date.
- **Validation** — IRIS auto-validates the CPR numbers against the bank deposit data; mismatches must be corrected before submission.
- **Penalty for late filing** — Section 182 — Rs 2,500 per day, minimum Rs 50,000.  _(Section 182)_

### 6.4 Annual reconciliation

- **Due date** — Due by the due date of filing the return of income.
- **Aggregation** — Aggregates all 12 monthly statements and reconciles to the audited financials (where the agent is a company).
- **Discrepancy resolution** — Discrepancies (deducted-not-deposited, deposited-not-statemented, statemented-not-deducted) must be resolved.

### 6.5 Penalties and consequences

**Penalties table**

| Default | Consequence |
| --- | --- |
| Failure to deduct WHT | Disallowance of the expense under **Section 21(c)** in the payer's own income tax computation; recovery of WHT from payer under Section 161; plus default surcharge (§205) and penalties (§182) |
| Failure to deposit deducted WHT | **0.1% per day default surcharge** on the unpaid amount + penalty under Section 182 |
| Failure to file Section 165 statement | Section 182 — **Rs 5,000** (if paid & filed within 90 days); otherwise **Rs 2,500 per day** (minimum Rs 10,000) per default |
| Late deposit but on time before notice | Default surcharge only; no penalty if voluntary |
| Use of incorrect (lower) rate without justification | Recovery of shortfall + default surcharge + penalty |
| Non-application of non-filer rate where recipient was non-ATL | Withholding agent personally liable for the shortfall under Section 161 |

## Section 7 — Conservative defaults

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| ATL status unverified at payment date | **Apply non-filer rate** (typically 2x) — flag to confirm |
| Treaty rate claim without TRC | **Apply statutory non-resident rate** — flag for refund claim path |
| Goods vs services vs contract classification unclear | **Apply contract rate (7%/15%)** as it is generally the highest of the 153 sub-limbs and avoids under-withholding |
| Sales tax inclusion in invoice ambiguous | **Strip sales tax conservatively** — base = invoice / (1 + applicable sales tax rate) |
| Section 159 certificate provided but expired / wrong section / wrong payer | **Disregard the certificate** and apply full rate — flag for renewal |
| Prescribed-person status of payer unclear (Section 153) | **Assume prescribed** and withhold — over-withholding can be recovered by recipient via refund |
| Sector classification for low-margin 153 services unclear | **Apply general rate (11%/22%)** rather than reduced (4%/8%) |
| Date of payment vs date of credit unclear | **Use the earlier date** as the tax point |
| Current-year rate ambiguity in user's mind | **Quote the FA 2025 rate** but ALWAYS flag "verify against current First Schedule on FBR website before depositing" |
| Multi-section overlap (e.g. payment that could be 153 services or 152 FTS to non-resident) | **Apply the more specific section** — for non-residents that means 152; for residents, 153 |
| Annual rent split across months for slab computation | **Annualise the rent** and apply slab to annual figure; deduct pro-rata monthly |

## Section 8 — Sources

**Sources table**

| # | Source | Use |
| --- | --- | --- |
| S-1 | **Income Tax Ordinance 2001** (consolidated up to Finance Act 2025) — published on FBR website (https://www.fbr.gov.pk) | Primary statute for all WHT sections |
| S-2 | **Income Tax Rules 2002** (consolidated) — FBR website | Procedural rules — Rule 43 (deposit deadlines), Rule 44 (statement forms), Rule 73-75 (159 certificates) |
| S-3 | **First Schedule** to ITO 2001 — Part II (rates), Part III (rate categories), Part IV (special rates) | All WHT rate figures |
| S-4 | **Tenth Schedule** to ITO 2001 — ATL / non-filer rate cascade | Filer vs non-filer 2x mechanics |
| S-5 | **Active Taxpayers List (ATL)** — FBR weekly publication on https://www.fbr.gov.pk/ATL | Real-time filer status check |
| S-6 | **Finance Act 2024** (Pakistan) and **Finance Act 2025** (Pakistan) — text published in Gazette of Pakistan | Current-year rate amendments |
| S-7 | **FBR Circulars and SROs** — current notifications on https://www.fbr.gov.pk | Sector-specific reduced rates, low-margin services classification, exemptions |
| S-8 | **IRIS portal** — https://iris.fbr.gov.pk | PSID generation, CPR reconciliation, 165 statements, 159 certificate applications |
| S-9 | **DTA texts** — published on FBR website under "International Taxation → Treaties" | Treaty rate caps for non-resident WHT |
| S-10 | **State Bank of Pakistan (SBP)** — https://www.sbp.org.pk | Interbank exchange rates for foreign-currency payment conversion |
| S-11 | **ICAP Tax Bulletins** and **ICMAP Tax Reviews** | Practitioner commentary on FA amendments |
| S-12 | **Pakistan Tax Bar Association** and case law — **Income Tax Appellate Tribunal (ITAT)** and **High Courts** reported decisions on FTR vs NTR, prescribed-person status, treaty interpretation, and Section 153 classification disputes | Interpretive guidance |

## End of skill v1.0 — pk-withholding-tax.

**Reviewer note.** Pakistan WHT rates change with every Finance Act and frequently within the year via SROs. Every figure in this skill is stated "as per FA 2025 — verify against current First Schedule" and must be confirmed against the live FBR text before any client-facing computation. Sign-off by an ICAP-registered Chartered Accountant or FBR-registered Income Tax Practitioner is required before reliance.

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
