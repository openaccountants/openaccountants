---
name: kh-income-tax
description: Use this skill whenever asked about Cambodia personal income tax, Tax on Salary (TOS), or Tax on Income (TOI) for individuals, sole proprietors, and employers. Trigger on phrases like "how much salary tax do I pay in Cambodia", "Tax on Salary", "TOS withholding", "Tax on Income Cambodia", "monthly salary tax bracket", "NSSF contribution", "tax on fringe benefits", "non-resident 20% salary tax", "dependent allowance Khmer", "sole proprietor tax Cambodia", "GDT e-filing", "20th of the month tax return", or any question about computing or filing employment-income tax, payroll withholding, or annual business-income tax for a Cambodian taxpayer. Also trigger when preparing or reviewing a monthly TOS return, computing NSSF (National Social Security Fund) contributions, applying dependent relief, or advising on annual TOI for a physical person. Cambodia has NO Western-style "personal income tax" — it runs Tax on Salary (monthly, progressive 0%–20%) and Tax on Income (annual, progressive 0%–20%) instead. This skill covers resident/non-resident TOS brackets, dependent allowances, fringe-benefit tax, NSSF schemes, annual TOI, GDT filing forms and deadlines, and penalties. ALWAYS read this skill before touching any Cambodian income-tax or payroll work.
jurisdiction: KH
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# cambodia-income-tax

## Cambodia Income Tax (Tax on Salary & Tax on Income) -- Skill v0.1

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Kingdom of Cambodia |
| Tax (employment) | Tax on Salary (TOS) -- monthly progressive withholding |
| Tax (business/professional) | Tax on Income (TOI) -- annual progressive tax on physical persons |
| Currency | Khmer Riel (KHR). Wages often quoted in USD (USD ≈ KHR 4,000–4,100); statutory tax tables are in KHR |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Law on Taxation; rate tables set by **Sub-Decree No. 196 ANKr.BK of 28 Sept 2022**, effective 1 Jan 2023 (current for 2025/2026) [PwC; DFDL] |
| Tax authority | General Department of Taxation (GDT), Ministry of Economy and Finance — www.tax.gov.kh [PwC; Acclime] |
| Social security | National Social Security Fund (NSSF) [NSSF; PwC] |
| Filing portal | GDT E-Filing / e-Tax system [PwC; Acclime] |
| Monthly TOS deadline | 20th day of the following month [PwC; Acclime] |
| Annual TOI deadline | 31 March (within 3 months of calendar year-end) [PwC; Acclime] |
| Validated by | Pending — requires sign-off by a qualified Cambodian tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

> **CONCEPTUAL NOTE — there is no "personal income tax" in the Western sense in Cambodia.** Individuals are taxed through two distinct progressive regimes that currently share the same 0%–20% rate ladder:
> 1. **Tax on Salary (TOS)** — a monthly progressive tax on employment income, withheld and remitted by the employer.
> 2. **Tax on Income (TOI)** — an annual progressive tax on the business/professional income of physical persons (sole proprietors, partnerships).
>
> This skill computes both. Always confirm which regime applies before producing any figure.

### 1.1 Tax on Salary (TOS) -- Monthly Brackets, RESIDENTS

**TOS monthly brackets, residents**  _([PwC; DFDL; MEF open data])_

| Monthly taxable salary (KHR) | Rate | Cumulative tax at top of band (KHR) |
| --- | --- | --- |
| 0 -- 1,500,000 | 0% | 0 |
| 1,500,001 -- 2,000,000 | 5% | 25,000 |
| 2,000,001 -- 8,500,000 | 10% | 675,000 |
| 8,500,001 -- 12,500,000 | 15% | 1,275,000 |
| Over 12,500,000 | 20% | -- |

*Cumulative-tax check: 0 + (5% × 500,000 = 25,000) → 25,000; + (10% × 6,500,000 = 650,000) → 675,000; + (15% × 4,000,000 = 600,000) → 1,275,000. Reconciled.*

- **GDT computation method** — The GDT publishes a "quick lump-sum deduction" per band so payroll can compute TOS = (monthly tax base × marginal rate) − quick deduction. The exact deduction column from the official Sub-Decree 196 table is [RESEARCH GAP — reviewer to confirm] (tax.gov.kh table is image-only / 403-blocked). This skill computes TOS directly by the marginal-band method above, which yields the same result; do not publish the lump-sum deduction figures until verified.  _([Acclime])_

### 1.2 Tax on Salary -- NON-RESIDENTS

**Non-resident TOS and fringe benefit rates**

| Item | Rate / Treatment |
| --- | --- |
| Cambodia-sourced salary | Flat **20%**, **final tax** — no brackets, no allowances [PwC] |
| Tax on Fringe Benefits (all employees) | Flat **20%** of the value of the benefit, **employer-borne**, monthly [PwC] |

### 1.3 Annual Tax on Income (TOI) -- Sole proprietors / individuals / partnerships

**Annual TOI brackets**  _([Orbitax; PwC])_

| Annual taxable income (KHR) | Rate | Cumulative tax at top of band (KHR) |
| --- | --- | --- |
| 0 -- 18,000,000 | 0% | 0 |
| 18,000,001 -- 24,000,000 | 5% | 300,000 |
| 24,000,001 -- 102,000,000 | 10% | 8,100,000 |
| 102,000,001 -- 150,000,000 | 15% | 15,300,000 |
| Over 150,000,000 | 20% | -- |

*Cumulative-tax check: 5% × 6,000,000 = 300,000 → 300,000; + 10% × 78,000,000 = 7,800,000 → 8,100,000; + 15% × 48,000,000 = 7,200,000 → 15,300,000. Reconciled.*

- **Sole proprietorship definition (for TOI)** — a business owned 100% by one physical person; husband, wife and dependent children are treated as one physical person.  _([PwC])_
- **Monthly TOI prepayment** — 1% of monthly turnover (inclusive of all taxes except VAT) under the self-assessment/real regime, creditable against annual TOI and minimum tax. (Micro/small simplified-regime taxpayers may differ — verify per turnover-based classification.)  _([PwC])_

### 1.4 Dependent Allowances (resident TOS only)

**Dependent allowances**

| Allowance | Monthly amount (KHR) | Condition |
| --- | --- | --- |
| Dependent child | 150,000 per child | Under 14, or under 25 if a full-time student [Acclime; DFDL] |
| Non-working dependent spouse | 150,000 | Spouse with no income [Acclime; DFDL] |

- **Allowance application scope** — Allowances reduce the monthly TOS tax base before applying the band table. They do not apply to non-resident flat-20% salary, fringe-benefit tax, or annual TOI.

### 1.5 Conservative Defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP — residency changes the entire computation (brackets vs flat 20%). Do not guess |
| Unknown regime (TOS vs TOI) | Treat employment income as TOS; business income as TOI; if mixed, STOP and ask |
| Unknown dependent eligibility | 0 allowances |
| Unknown whether a payment is a fringe benefit | Treat as a fringe benefit (20% employer-borne) |
| Unknown NSSF registration status | Assume employer is registered (≥8 employees) and apply NSSF; flag for reviewer |
| Currency of a USD-quoted wage | Convert to KHR at the documented monthly rate; flag the rate used |
| Unknown turnover-regime classification (sole proprietor) | STOP — affects prepayment and filing obligations |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable (TOS / payroll)** — gross monthly salary per employee, residency status of each employee, and dependent details (spouse, children) for residents.

**Minimum viable (TOI / sole proprietor)** — annual income and expense account or full-year bank statement, and confirmation of taxpayer classification (real/self-assessment regime).

**Recommended** — employment contracts, NSSF registration confirmation and employee count, fringe-benefit register, USD→KHR conversion rates used, prior-period TOS/TOI returns.

**Ideal** — full payroll register, NSSF contribution records, monthly TOI prepayment receipts, GDT e-filing acknowledgements.

**Refusal if minimum is missing — SOFT WARN.** No salary figure or no residency status = hard stop for TOS. For TOI, no income figure = hard stop. Bank statement without supporting invoices = proceed with reviewer warning: "This computation was produced from bank/payroll data alone. The reviewer must verify residency, dependent eligibility, and the deductibility of any business expenses."

### Refusal Catalogue

- **R-KH-1** — Residency status unknown. "Residency determines whether salary is taxed on the resident progressive brackets (0%–20% with allowances) or as a non-resident flat 20% final tax. This skill cannot compute Tax on Salary without it. Please confirm domicile, principal abode, or day-count (>182 days)."
- **R-KH-2** — Companies / corporate TOI. "This skill covers Tax on Salary and the Tax on Income of physical persons (sole proprietors/partnerships). Corporate income tax for legal persons, qualified investment projects, and minimum tax for companies are out of scope. Escalate to a Cambodian tax practitioner."
- **R-KH-3** — Cross-border / treaty / withholding on payments abroad. "Withholding tax on payments to non-residents, double-tax-treaty relief, and permanent-establishment questions require specialised analysis. Out of scope. Escalate."
- **R-KH-4** — Simplified / estimated-regime sole proprietor. "Micro and small simplified-regime taxpayers are taxed differently from the self-assessment/real regime modelled here. Confirm taxpayer classification before relying on these figures. [RESEARCH GAP — turnover thresholds not authoritatively captured]"
- **R-KH-5** — Tax arrears / GDT enforcement. "Client has outstanding tax or is under GDT reassessment. Penalties run 10%–40% plus 1.5%/month interest and are severe. Do not advise. Escalate immediately."
- **R-KH-6** — VAT requested. "This skill covers Tax on Salary and Tax on Income only. Cambodian VAT is a separate regime — out of scope here."

## Section 3 -- Transaction / Payment Pattern Library

This is the deterministic pre-classifier for payroll registers and sole-proprietor bank statements. Match by case-insensitive substring on the counterparty/description as it appears. If multiple match, use the most specific. If none match, fall through to Tier 1 rules (Section 5).

Cambodian descriptions mix English, Khmer transliteration, and USD/KHR amounts. Terms below include common Khmer transliterations.

### 3.1 Income / Salary Patterns (Credits)

**Income/salary patterns table**

| Pattern | Regime / Line | Treatment | Notes |
| --- | --- | --- | --- |
| SALARY, PAYROLL, BROAS (ប្រាក់ខែ), WAGE, EMPLOYER [name] | TOS tax base | Employment income | Apply resident brackets or non-resident 20% per status |
| ALLOWANCE (cash, taxable), OVERTIME, BONUS (cash) | TOS tax base | Add to monthly taxable salary | Cash allowances/bonuses are part of the TOS base |
| FRINGE BENEFIT, HOUSING PROVIDED, CAR PROVIDED, SCHOOL FEES PAID | Fringe benefit | 20% employer-borne ToFB | NOT in employee TOS base; employer pays 20% of value |
| CLIENT PAYMENT, INVOICE, PROFESSIONAL FEES, CONSULTANCY (sole proprietor) | TOI turnover | Business income | Feeds annual TOI + 1% monthly prepayment base |
| STRIPE / PAYPAL / WISE PAYOUT (sole proprietor) | TOI turnover | Business income | Match to underlying invoices |
| TAX REFUND, GDT REFUND | EXCLUDE | Not income | Refund of prior tax |
| INTEREST RECEIVED, DIVIDEND | OUT OF SCOPE | Flag | Investment income — separate withholding rules; escalate |

### 3.2 Expense Patterns (Sole-Proprietor Debits) -- Deductible against TOI

**Expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, KIRI (ការជួល), SHOP RENT | Premises rent | Deductible | Business premises only |
| ACCOUNTANT, AUDITOR, BOOKKEEP, LEGAL (business) | Professional fees | Deductible | Business-related |
| SUPPLIES, STATIONERY, INVENTORY, STOCK PURCHASE | Cost of goods / supplies | Deductible | Trading inputs |
| MARKETING, FACEBOOK ADS, GOOGLE ADS | Advertising | Deductible |  |
| UTILITIES (business premises), EDC ELECTRICITY, WATER | Utilities | Deductible | Business premises; apportion if mixed |
| BANK FEE, ABA CHARGE, ACLEDA CHARGE, WING FEE | Bank/transfer charges | Deductible | Business account |
| SOFTWARE SUBSCRIPTION, SAAS | Software | Deductible | Recurring operating expense |

### 3.3 Statutory Withholdings / Contributions (Debits)

**Statutory withholdings table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| NSSF, SOCIAL SECURITY FUND | NSSF contribution | See Section 4 | Banded contributory wage, KHR 1,200,000 ceiling |
| TOS PAYMENT, SALARY TAX, GDT TOS | TOS remittance | Liability payment | Remitted by 20th of following month |
| TOI PREPAYMENT, 1% TURNOVER TAX | TOI monthly prepayment | Credit vs annual TOI | Not an expense — creditable |
| VAT PAYMENT, GDT VAT | EXCLUDE | Out of scope | Separate regime |

### 3.4 Not Deductible / Exclude

**Not deductible / exclude table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWNER DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | EXCLUDE | Not a business expense |
| FINE, PENALTY, GDT PENALTY | NOT deductible | Public policy |
| INCOME TAX, TOI PAYMENT (final) | NOT deductible | Tax on income |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Own-account movement |
| PERSONAL GROCERIES, RESTAURANT (personal) | NOT deductible | Private living cost |

### 3.5 Cambodian Banks / Wallets -- Statement Format Reference

**Banks/wallets statement format reference table**

| Provider | Common patterns | Notes |
| --- | --- | --- |
| ABA Bank | TRANSFER, PAYWAY, QR PAYMENT, CHARGE | App/CSV export; USD and KHR accounts common |
| ACLEDA Bank | TRANSFER, ACLEDA UNITY, FEE | PDF/CSV; dual-currency |
| Wing (WingMoney) | CASH IN, CASH OUT, TRANSFER | Mobile wallet; many micro-payments |
| Canadia / Vattanac | TRANSFER, STANDING ORDER, CHARGE | PDF statements |
| Bakong / KHQR | QR PAYMENT, BAKONG TRANSFER | National QR rail; counterparty in reference |

## Section 4 -- NSSF (National Social Security Fund) Contributions

**NSSF scheme rates table**  _([NSSF; PwC])_

| Scheme | Total rate | Employer share | Employee share | Contributory-wage band (KHR/month) |
| --- | --- | --- | --- | --- |
| Occupational Risk (ORC) | 0.8% | 0.8% | 0.0% | 400,000 floor – 1,200,000 ceiling [NSSF; PwC] |
| Health Care (HIP) | 2.6% | 2.6% (full burden since 1 Jan 2018) | 0.0% | 200,000 floor – 1,200,000 ceiling [NSSF; Aplus] |
| Pension (Old-Age), years 1–5 | 4.0% | 2.0% | 2.0% | 400,000 floor – 1,200,000 ceiling [PwC; NSSF] |
| **TOTAL (years 1–5)** | **7.4%** | **5.4%** | **2.0%** | ceiling KHR 1,200,000 |

NSSF is not a flat percentage of actual salary. It is calculated on a banded "contributory/assigned wage" with a ceiling of KHR 1,200,000/month. Three schemes apply. [NSSF; PwC]

*Column check: employer 0.8 + 2.6 + 2.0 = 5.4%; employee 0.0 + 0.0 + 2.0 = 2.0%; total 0.8 + 2.6 + 4.0 = 7.4%; and 5.4 + 2.0 = 7.4. Reconciled.*

> **Healthcare presentation flag.** The NSSF statute defines health care as 1.3% employer + 1.3% worker = 2.6%, but a decree requires the employer to bear 100% since 1 Jan 2018. Present it as employer-borne 2.6%, employee 0%. [NSSF; Aplus]

### 4.1 Pension escalation

- **Pension escalation** — Pension rises over time: 4% (years 1–5) → 8% (years 6–10) and then ~2.75% increases each subsequent 10-year period, split evenly employer/employee. Use 4% (2%/2%) for current-period computations unless the reviewer confirms a later phase.  _([PwC])_

### 4.2 Contribution ceilings (computed)

- **Maximum monthly employee NSSF** — pension 2% × KHR 1,200,000 = KHR 24,000. (2% × 1,200,000 = 24,000. Reconciled.)
- **Maximum monthly employer NSSF (years 1–5)** — 5.4% × KHR 1,200,000 = KHR 64,800. (0.054 × 1,200,000 = 64,800. Reconciled.)

### 4.3 Registration threshold

- **NSSF registration threshold** — 8 or more employees employees (must register with NSSF within 45 days and contribute to ORC, health care and pension. (Some practitioner sources note enforcement has effectively extended toward all employers/≥1 employee — verify current Prakas. [RESEARCH GAP — reviewer to confirm scope]))  _([PwC])_

## Section 5 -- Tier 1 Rules (When Data Is Clear)

- **section header** — 

### 5.1 Residency Test

- **Residency test** — A person is resident if ANY of: domiciled in Cambodia; principal place of abode in Cambodia; or present in Cambodia more than 182 days in any 12-month period ending in the tax year. Residents are taxed on worldwide salary; non-residents on Cambodia-sourced salary only. (Most sources say "more than 182 days" — treat as the >182-day test. [RESEARCH GAP — confirm exact wording vs 183 in Law on Taxation])  _([PwC; Acclime])_

### 5.2 Resident TOS Computation (monthly)

- **Resident TOS computation steps** — 1. Start with gross monthly salary (cash salary + taxable cash allowances/bonuses; exclude fringe benefits — those are taxed separately). 2. Subtract dependent allowances: KHR 150,000 per qualifying child + KHR 150,000 for a non-working spouse → monthly tax base. 3. Apply the resident band table (Section 1.1) by the marginal method. 4. Pass the result to the deterministic engine; do not hand-round intermediate bands.

### 5.3 Non-Resident TOS Computation

- **Non-resident TOS computation** — Flat 20% of Cambodia-sourced salary. Final tax. No allowances, no brackets.  _([PwC])_

### 5.4 Tax on Fringe Benefits

- **Tax on fringe benefits** — Flat 20% of the value of the benefit (housing, vehicle, school fees, low-interest loans, etc.), employer-borne, remitted monthly. Not added to the employee's TOS base.  _([PwC])_

### 5.5 Annual TOI (sole proprietor / physical person)

- **Annual TOI computation steps** — 1. Determine annual net business income (turnover less deductible business expenses incurred to earn it). 2. Apply the annual band table (Section 1.3) by the marginal method. 3. Credit the 1% monthly turnover prepayments paid during the year (and minimum tax, if applicable) against the annual liability. 4. Husband, wife and dependent children of a sole proprietor are treated as one physical person.  _([PwC])_

### 5.6 Non-Deductible Items (TOI)

**Non-deductible items table**

| Item | Reason |
| --- | --- |
| Owner drawings | Not a business expense |
| Fines and penalties | Public policy |
| Income tax itself (TOI) | Tax on income |
| Personal/private expenses | Not incurred to earn income |
| VAT remittances | Separate regime — exclude |

### 5.7 Filing & Deadlines

**Filing and deadlines table**

| Obligation | Deadline | Channel |
| --- | --- | --- |
| Monthly TOS return + payment | 20th of the following month | GDT e-filing [PwC; Acclime] |
| Monthly TOI prepayment (1% turnover) | 20th of the following month | GDT e-filing [PwC] |
| Annual TOI return | 31 March (within 3 months of year-end) | GDT e-Tax [PwC; Acclime] |
| NSSF contributions | Monthly per NSSF schedule | NSSF portal [NSSF] |

### 5.8 Penalties

**Penalties table**

| Trigger | Charge |
| --- | --- |
| Minor/negligent error or late payment | 10% additional tax [PwC; Acclime] |
| Unilateral reassessment / failure to file by deadline | 25% additional tax [PwC] |
| Repeat offense / obstruction (2nd notice within 3 years) | 40% additional tax [PwC] |
| Interest on unpaid tax | 1.5% per month (current statutory rate) [PwC; RUMAVI] |

*Some practitioner summaries cite "2% monthly interest"; the current statutory rate is 1.5%/month — treat 1.5% as authoritative. [RESEARCH GAP — reviewer to confirm against current Prakas]*

## Section 6 -- Worked Examples

All amounts in KHR. Computations use the marginal-band method.

### Example 1 -- Resident salary, no dependents

**Input line:**
`31/03/2025 ; ABA PAYROLL ; EMPLOYER SOKHA TRADING CO ; SALARY MAR ; +6,000,000 ; KHR`

**Reasoning:**
Resident, monthly tax base = KHR 6,000,000 (no allowances). Falls in the 2,000,001–8,500,000 band (10%).
TOS = 0 (first 1,500,000) + 5% × 500,000 (=25,000) + 10% × (6,000,000 − 2,000,000) (=400,000) = 425,000.
Employee NSSF = 2% × min(6,000,000, 1,200,000 ceiling) = 2% × 1,200,000 = 24,000.
Net pay = 6,000,000 − 425,000 − 24,000 = 5,551,000.

**Classification:** TOS withheld 425,000; employee NSSF 24,000; net 5,551,000.

### Example 2 -- Resident salary in the 0% band

**Input line:**
`31/04/2025 ; ACLEDA PAYROLL ; GARMENT FACTORY KH ; WAGE APR ; +1,200,000 ; KHR`

**Reasoning:**
Resident, tax base KHR 1,200,000 ≤ 1,500,000 → 0% band → TOS = 0.
Employee NSSF = 2% × min(1,200,000, 1,200,000) = 24,000.
Net pay = 1,200,000 − 0 − 24,000 = 1,176,000.

**Classification:** TOS 0; employee NSSF 24,000; net 1,176,000.

### Example 3 -- Resident salary, non-working spouse + 2 children

**Input line:**
`31/05/2025 ; ABA PAYROLL ; MEKONG LOGISTICS ; SALARY MAY ; +10,000,000 ; KHR`

**Reasoning:**
Dependent allowances = spouse 150,000 + 2 children × 150,000 = 450,000.
Tax base = 10,000,000 − 450,000 = 9,550,000 → falls in the 8,500,001–12,500,000 band (15%).
TOS = 675,000 (cumulative to 8,500,000) + 15% × (9,550,000 − 8,500,000) (=157,500) = 832,500.
Employee NSSF = 2% × 1,200,000 (ceiling) = 24,000.
Net pay = 10,000,000 − 832,500 − 24,000 = 9,143,500.

**Classification:** TOS 832,500; employee NSSF 24,000; net 9,143,500.

### Example 4 -- Non-resident salary (flat 20% final)

**Input line:**
`31/06/2025 ; CANADIA PAYROLL ; INTL CONSULTING SARL ; SALARY (NON-RESIDENT) ; +8,000,000 ; KHR`

**Reasoning:**
Non-resident → flat 20% final tax on Cambodia-sourced salary, no allowances, no brackets.
TOS = 20% × 8,000,000 = 1,600,000 (final).
Net pay (before any NSSF, if the employer is NSSF-registered) = 8,000,000 − 1,600,000 = 6,400,000.

**Classification:** TOS 1,600,000 (final tax). No brackets, no dependent relief.

### Example 5 -- Tax on Fringe Benefits (employer-borne)

**Input line:**
`30/06/2025 ; ABA TRANSFER ; LANDLORD — STAFF HOUSING ; HOUSING PROVIDED TO MANAGER ; -2,000,000 ; KHR`

**Reasoning:**
Employer provides housing valued at KHR 2,000,000/month. Tax on Fringe Benefits = 20% × 2,000,000 = 400,000, paid by the employer monthly. Not added to the employee's TOS base.

**Classification:** ToFB 400,000 (employer-borne). Excluded from employee TOS computation.

### Example 6 -- Annual TOI, sole proprietor

**Input summary:**
`FY2025 ; sole proprietor (real regime) ; annual net business income +60,000,000 ; KHR`

**Reasoning:**
Annual taxable income 60,000,000 → falls in the 24,000,001–102,000,000 band (10%).
TOI = 300,000 (cumulative to 24,000,000) + 10% × (60,000,000 − 24,000,000) (=3,600,000) = 3,900,000.
Less 1% monthly turnover prepayments already paid (creditable). If prepayments during the year totalled, say, 1,500,000, then balance due = 3,900,000 − 1,500,000 = 2,400,000.

**Classification:** Annual TOI 3,900,000; less prepayment credits; balance due to GDT by 31 March.

## Section 7 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 7.1 Residency determination at the margin

- Day-count near the >182-day threshold, dual residence, or mid-year arrival/departure changes the whole computation.
- **Flag for reviewer:** confirm domicile, principal abode, and day-count evidence. Do not auto-classify near the boundary.

### 7.2 Fringe-benefit valuation

- Housing, vehicles, low-interest loans, school fees, and meals each have specific valuation rules.
- **Conservative default:** treat unexplained employer-paid personal benefits as taxable fringe benefits at 20%.
- **Flag for reviewer:** confirm the assessed value of each benefit.

### 7.3 USD-quoted wages → KHR

- Many contracts state salary in USD; the statutory tables are in KHR.
- **Flag for reviewer:** confirm the conversion rate applied (document the date and source; USD ≈ KHR 4,000–4,100). [RESEARCH GAP — confirm whether GDT-published rate or contractual rate applies]

### 7.4 Sole-proprietor expense deductibility

- Mixed personal/business expenses (home premises, vehicle, phone) must be apportioned on a reasonable, documented basis.
- **Conservative default:** 0% deduction for mixed-use items until apportionment is evidenced.

### 7.5 Taxpayer-classification (turnover regime)

- Real/self-assessment vs simplified/estimated regime affects prepayment, VAT, and filing.
- **Flag for reviewer:** confirm turnover-band classification against the GDT Prakas. [RESEARCH GAP — thresholds not authoritatively captured]

### 7.6 NSSF pension phase

- Pension rate escalates (4% → 8% → +~2.75% per decade). The applicable phase depends on scheme tenure.
- **Flag for reviewer:** confirm whether years 1–5 (4%) or a later phase applies.

## Section 8 -- Excel Working Paper Template

```
CAMBODIA TAX ON SALARY (TOS) -- MONTHLY WORKING PAPER (KHR)
Tax Year: 2025   Month: ____________
Employee: ___________________________
Residency: Resident / Non-resident
Currency of contract: KHR / USD   (rate used if USD: __________)

A. GROSS MONTHLY SALARY (cash)
  A1. Base salary                                ___________
  A2. Taxable cash allowances / bonuses          ___________
  A3. TOTAL gross (A1 + A2)                       ___________

B. DEPENDENT ALLOWANCES (residents only)
  B1. Non-working spouse (150,000)               ___________
  B2. Children (150,000 each × ___)              ___________
  B3. TOTAL allowances                           ___________

C. MONTHLY TAX BASE (A3 - B3)                    ___________

D. TOS (pass to deterministic engine)
  D1. Resident: marginal-band table              ___________
      OR Non-resident: 20% × A3 (final)          ___________

E. NSSF (banded, ceiling 1,200,000)
  E1. Employee pension (2% × min(A3,1,200,000))  ___________
  E2. Employer ORC 0.8% + HIP 2.6% + Pension 2%  ___________

F. NET PAY (A3 - D - E1)                          ___________

----------------------------------------------------------
ANNUAL TAX ON INCOME (TOI) -- SOLE PROPRIETOR (KHR)
  G1. Annual turnover                            ___________
  G2. Deductible business expenses               ___________
  G3. Net taxable income (G1 - G2)               ___________
  G4. Annual TOI (marginal-band table)           ___________
  G5. Less: 1% monthly prepayments credited      ___________
  G6. Balance due / (refund) (G4 - G5)           ___________

REVIEWER FLAGS:
  [ ] Residency status confirmed?
  [ ] USD→KHR conversion rate documented?
  [ ] Dependent eligibility evidenced?
  [ ] Fringe benefits valued & taxed at 20% (employer)?
  [ ] NSSF registration & pension phase confirmed?
  [ ] Sole-proprietor turnover-regime classification confirmed?
  [ ] Prepayment credits reconciled to receipts?
```

## Section 9 -- Bank Statement / Payroll Reading Guide

### Cambodian Statement Formats

**Cambodian statement formats table**

| Provider | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| ABA Bank | App export / CSV / PDF | Date, Description, Amount, Currency, Balance | USD and KHR accounts; PayWay & KHQR references |
| ACLEDA Bank | PDF / CSV | Date, Particulars, Debit, Credit, Balance | Dual-currency; bilingual descriptions |
| Wing (WingMoney) | App / CSV | Date, Type (Cash In/Out), Amount | Mobile wallet; many micro-payments |
| Canadia / Vattanac | PDF | Date, Description, Withdrawal, Deposit | Standing orders for rent/payroll |
| Bakong / KHQR | App | Date, Counterparty, Amount, Reference | National QR rail |

### Key Khmer Terms / Transliterations

**Key Khmer terms table**

| Term (Khmer / translit) | English | Classification hint |
| --- | --- | --- |
| ប្រាក់ខែ / BROAS KHE | Monthly salary | TOS tax base |
| ការជួល / KIRI | Rent | Business expense (premises) or personal |
| ពន្ធ / PUNH | Tax | TOS/TOI remittance — not an expense |
| ផ្ទេរ / PHTOR / TRANSFER | Transfer | Check direction for income/expense |
| សោហ៊ុយ / SOHUY / CHARGE | Fee / charge | Bank charge (deductible if business) |
| NSSF / បេឡាជាតិ | Social security | NSSF contribution (Section 4) |
| ប្រាក់រង្វាន់ / BONUS | Bonus | Cash bonus → TOS base |

## Section 10 -- Onboarding Fallback

If the client provides payroll or bank data but cannot answer onboarding questions immediately:

1. Classify all lines using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm."
3. Apply conservative defaults (Section 1.5).
4. Generate the working paper (Section 8) with clear flags.
5. Present the following questions:

```
ONBOARDING QUESTIONS -- CAMBODIA INCOME TAX
1. For each employee: resident or non-resident? (domicile / principal abode / >182 days?)
2. Is salary quoted in KHR or USD? If USD, what conversion rate should apply?
3. For residents: non-working spouse? How many qualifying children (under 14, or under 25 if full-time student)?
4. Any non-cash benefits provided (housing, car, school fees, loans)? Values?
5. Is the employer NSSF-registered? How many employees? Which pension phase?
6. Sole proprietor? If so, what is the annual turnover and taxpayer-regime classification?
7. Were 1% monthly TOI prepayments made? Totals and receipts?
8. Any GDT arrears, reassessments, or penalties outstanding?
```

## Section 11 -- Reference Material

### Key Legislation / Authority References

**Key legislation table**

| Topic | Reference |
| --- | --- |
| TOS & TOI rate tables (2023→) | Sub-Decree No. 196 ANKr.BK of 28 Sept 2022, effective 1 Jan 2023 [PwC; DFDL; Orbitax] |
| Residency & sourcing | Law on Taxation; PwC "Taxes on personal income" [PwC] |
| Dependent allowances | KHR 150,000/month per child and per non-working spouse [Acclime; DFDL] |
| Non-resident salary / fringe benefits | Flat 20% [PwC] |
| NSSF schemes, rates, ceiling | NSSF Contribution Payment; PwC "Other taxes" [NSSF; PwC; Aplus] |
| Filing deadlines (TOS 20th; TOI 31 March) | PwC "Corporate tax administration"; Acclime [PwC; Acclime] |
| Penalties (10/25/40%; 1.5%/month) | PwC; Acclime; RUMAVI [PwC; Acclime; RUMAVI] |
| Tax authority | General Department of Taxation (GDT), www.tax.gov.kh |

### Minimum Wage (context — sector-specific, not economy-wide)

Cambodia has no economy-wide statutory minimum wage; the statutory minimum applies only to the textile, garment, footwear, travel-goods and bag sectors. [ASEAN Briefing; KPMG; DFDL]

**Minimum wage table**

| Year | Minimum wage | Probationary |
| --- | --- | --- |
| 2025 | USD 208/month (effective 1 Jan 2025) | USD 206/month [ASEAN Briefing; KPMG] |
| 2026 | USD 210/month (effective 1 Jan 2026) | rises to 210 post-probation [Xinhua; DFDL] |

Mandatory additional garment-sector benefits: transport/accommodation USD 7/month; attendance bonus USD 10/month; seniority bonus USD 2–11/month; OT meal allowance USD 0.5/day. [ASEAN Briefing]

### Sources

- PwC Tax Summaries — Cambodia, Individual: taxes on personal income; Individual: other taxes; Corporate: tax administration. https://taxsummaries.pwc.com/cambodia
- DFDL — "Changes to Tax on Income and Tax on Salary tables"; "Increase in minimum wage for 2026." https://www.dfdl.com
- Orbitax — "Cambodia Sets New Individual Income Tax Brackets from 2023." https://orbitax.com/news/archive.php/Cambodia-Sets-New-Individual-I-51045
- MEF Open Data — Monthly salary tax brackets. https://data.mef.gov.kh
- Acclime Cambodia — Personal Income Tax; Taxation introduction; Annual filing requirements. https://cambodia.acclime.com
- NSSF — Contribution Payment. https://www.nssf.gov.kh
- Aplus Consulting — NSSF / Cambodia labour law. https://www.aplusconsulting.com.kh
- ASEAN Briefing — 2025 minimum wage. https://www.aseanbriefing.com
- KPMG Cambodia — Technical update (2025 minimum wage). https://assets.kpmg.com
- Xinhua — 2026 USD 210 minimum wage. https://english.news.cn
- RUMAVI — Cambodia tax guide 2026. https://rumavi.com

*Note: tax.gov.kh returns HTTP 403 to automated fetches; the official Sub-Decree 196 PDF could not be retrieved directly. All figures above are cross-confirmed via the national authority (NSSF, MEF open data) and Big-4/established practitioner guides (PwC, DFDL, KPMG, Acclime, Orbitax).*

### Test Suite

**Test 1 — Resident, no dependents, KHR 6,000,000.**
Expected: TOS = 25,000 + 400,000 = 425,000; employee NSSF = 24,000; net = 5,551,000.

**Test 2 — Resident, 0% band, KHR 1,200,000.**
Expected: TOS = 0; employee NSSF = 24,000; net = 1,176,000.

**Test 3 — Resident, spouse + 2 children, KHR 10,000,000.**
Expected: allowances 450,000; base 9,550,000; TOS = 675,000 + 157,500 = 832,500; NSSF 24,000; net = 9,143,500.

**Test 4 — Non-resident, KHR 8,000,000.**
Expected: TOS = 20% × 8,000,000 = 1,600,000 (final); no allowances.

**Test 5 — Fringe benefit, KHR 2,000,000 housing.**
Expected: ToFB = 20% × 2,000,000 = 400,000 (employer-borne); excluded from employee TOS base.

**Test 6 — Annual TOI, net income KHR 60,000,000.**
Expected: TOI = 300,000 + 3,600,000 = 3,900,000; less 1% prepayment credits = balance due.

**Test 7 — NSSF ceiling.**
Expected: salary KHR 5,000,000 → contributory wage capped at 1,200,000 → employee NSSF = 24,000; employer NSSF = 5.4% × 1,200,000 = 64,800.

## PROHIBITIONS

- NEVER apply the resident progressive brackets without confirming residency — non-residents pay a flat 20% final tax.
- NEVER add dependent allowances or brackets to a non-resident salary computation.
- NEVER include fringe benefits in the employee's TOS base — they are taxed at 20%, employer-borne.
- NEVER charge employees the health-care (HIP) contribution — the employer bears the full 2.6% since 1 Jan 2018.
- NEVER compute NSSF on actual salary above the KHR 1,200,000 contributory-wage ceiling.
- NEVER publish the GDT "quick lump-sum deduction" figures — they are an unconfirmed RESEARCH GAP; compute TOS by the marginal-band method.
- NEVER treat the 1% monthly TOI turnover prepayment as a deductible expense — it is a creditable prepayment.
- NEVER allow income tax, fines, penalties, or owner drawings as deductions against TOI.
- NEVER apply a USD-quoted wage to the KHR statutory table without documenting the conversion rate.
- NEVER present tax calculations as definitive — always label as estimated, pending professional review.

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
