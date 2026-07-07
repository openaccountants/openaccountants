---
name: zambia-income-tax
description: Use this skill whenever asked about Zambia personal income tax (PAYE) or self-employed / small-business income tax. Trigger on phrases like "how much PAYE do I pay", "Zambia income tax", "net pay Zambia", "PAYE bands", "NAPSA contributions", "NHIMA", "turnover tax", "presumptive tax", "rental income tax Zambia", "provisional tax", "ITF P16", "ZRA return", "tax-free threshold Zambia", or any question about computing or filing income tax for an employee, sole trader, or small business in Zambia. Also trigger when preparing or reviewing a PAYE computation, a turnover-tax return, or advising on NAPSA/NHIMA payroll deductions. This skill covers PAYE bands, NAPSA social security, NHIMA health insurance, turnover tax, rental income tax, presumptive tax, provisional income tax, VAT registration, filing deadlines, employer obligations, and penalties. ALWAYS read this skill before touching any Zambia income tax work.
jurisdiction: ZM
domain: income-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# zambia-income-tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Zambia (Republic of Zambia) |
| Tax | Income Tax (PAYE for employees; income/turnover/presumptive tax for self-employed) |
| Currency | Zambian Kwacha (ZMW / K) only |
| Tax year (charge year) | Calendar year (1 January -- 31 December) |
| Primary authority | Zambia Revenue Authority (ZRA) |
| Pension authority | National Pension Scheme Authority (NAPSA) |
| Health authority | National Health Insurance Management Authority (NHIMA) |
| Filing portal | ZRA TaxOnline (e-portal) |
| Annual return deadline | 21 June following the charge year (PwC, ZM individual tax administration) |
| Validated by | Pending -- requires sign-off by a Zambian-qualified accountant (ZICA member) |
| Validation date | Pending |
| Skill version | 0.1 |

**Important year note:** The PAYE bands below are identical for the 2025 and 2026 charge years (PwC's 2026 charge-year page shows the same figures, introduced effective 1 Jan 2025). NAPSA, NHIMA, and minimum-wage figures are the 2025 values; where 2026 figures were not officially confirmed they carry a [RESEARCH GAP] marker.

### PAYE Bands (2025, unchanged into 2026)

**PAYE Bands (2025, unchanged into 2026)**  _(PwC, ZM individual -- taxes on personal income)_

| Annual taxable income (ZMW) | Monthly equivalent (ZMW) | Rate | Cumulative tax at band top (annual) |
| --- | --- | --- | --- |
| 0 -- 61,200 | 0 -- 5,100 | 0% | K0 |
| 61,201 -- 85,200 | 5,101 -- 7,100 | 20% | K4,800 |
| 85,201 -- 110,400 | 7,101 -- 9,200 | 30% | K12,360 |
| Over 110,400 | Over 9,200 | 37% | -- |

- **PAYE band progressivity** — Progressive. Only income within each band is taxed at that band's rate. Residents and non-residents are charged the same income-tax rates in principle, though most non-resident income is instead subject to withholding tax.  _(PwC, ZM individual -- taxes on personal income)_
- **Tax-free threshold** — ZMW 5,100/month (K61,200/year)  _(PwC, ZM individual -- taxes on personal income; ZRA PAYE leaflet, Pay-As-You-Earn.pdf)_

**Cumulative tax arithmetic (annual):**
- Band 2 width K24,000 × 20% = K4,800 → cumulative K4,800 at K85,200
- Band 3 width K25,200 × 30% = K7,560 → cumulative K4,800 + K7,560 = K12,360 at K110,400

**Cumulative tax arithmetic (monthly):**
- Band 2 width K2,000 × 20% = K400 → cumulative K400 at K7,100
- Band 3 width K2,100 × 30% = K630 → cumulative K400 + K630 = K1,030 at K9,200

### NAPSA -- Pension Contributions (2025)

**NAPSA -- Pension Contributions (2025)**  _(NAPSA official; PwC ZM individual -- other issues)_

| Item | Value | Source |
| --- | --- | --- |
| Total contribution rate | 10% of gross monthly earnings | NAPSA official; PwC ZM individual -- other issues |
| Employee share | 5% | NAPSA official |
| Employer share | 5% | NAPSA official |
| Monthly insurable-earnings ceiling | ZMW 34,164.00 | NAPSA 2025 announcement |
| Max monthly contribution per party | ZMW 1,708.20 | NAPSA (34,164 × 5%) |
| Max combined monthly contribution | ZMW 3,416.40 | NAPSA (1,708.20 × 2) |
| National Average Earnings (NAE) 2025 | ZMW 8,541.00 | NAPSA 2025 announcement |

**Component check:** employee 5% + employer 5% = 10% total. Per-party cap 1,708.20 + 1,708.20 = 3,416.40 combined.
**[RESEARCH GAP — reviewer to confirm]** 2026 NAPSA ceiling and NAE — not officially confirmed; do not assume the 2025 ceiling carries into 2026.

### NHIMA -- National Health Insurance (2025)

**NHIMA -- National Health Insurance (2025)**  _(NHIMA (secondary); workforceafrica payroll guide)_

| Item | Value | Source |
| --- | --- | --- |
| Total rate | 1% of gross earnings | NHIMA (secondary); workforceafrica payroll guide |
| Employee share | 0.5% | NHIMA (secondary) |
| Employer share | 0.5% | NHIMA (secondary) |
| Monthly returns due | by the 10th | NHIMA (secondary) |

**Component check:** employee 0.5% + employer 0.5% = 1% total.
**[RESEARCH GAP — reviewer to confirm]** The 1% total / 0.5%+0.5% split is widely reported but the official NHIMA rate schedule could not be retrieved directly. Re-verify against the NHIMA Act/SI before publishing as authoritative.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether earner is employee or self-employed | STOP -- do not compute without status |
| Unknown gross vs net of allowances | Treat the figure as gross monthly earnings |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category (self-employed) | Not deductible |
| Unknown whether NAPSA ceiling applies | Apply the K34,164 ceiling |
| Unknown turnover-tax vs income-tax election | Turnover tax if turnover ≤ K5,000,000 (see R-ZM-2) |
| Unknown VAT registration | Not VAT-registered (use gross amounts) |
| Charge year not stated | Current charge year (2025/2026 bands are identical) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable (employee/PAYE):** gross monthly earnings (basic + allowances), and confirmation the person is an employee. Optionally: confirmation of NAPSA/NHIMA applicability.

**Minimum viable (self-employed):** bank statement for the charge year in CSV, PDF, or pasted text, plus the nature of the business and approximate annual turnover (to decide turnover tax vs income tax).

**Recommended:** payslips, NAPSA/NHIMA contribution records, sales invoices, purchase invoices/receipts, prior-year ZRA assessment, VAT registration status.

**Ideal:** complete income and expenditure account, asset register, provisional-tax payment confirmations, employment contract / minimum-wage order applicable to the sector.

**Refusal if minimum is missing -- SOFT WARN.** No earnings figure (employee) or no bank statement (self-employed) = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported and that the wholly-and-exclusively test is met."

### Refusal Catalogue

- **R-ZM-1** — Employment status unknown. "PAYE (employee) and turnover/income tax (self-employed) are entirely different regimes. This skill cannot compute tax without knowing the person's status. Please confirm before proceeding."  _(R-ZM-1)_
- **R-ZM-2** — Turnover near or above K5,000,000. "Turnover tax applies only to annual turnover up to ZMW 5,000,000 (PwC, ZM other taxes). Above this the business files under the standard income-tax regime, and VAT registration may be required. Escalate to a ZICA-qualified accountant."  _(R-ZM-2; PwC, ZM other taxes)_
- **R-ZM-3** — Companies, partnerships, group structures. "This skill covers individuals -- employees and sole traders only. Companies and partnerships file separate returns under different rules. Escalate to a ZICA-qualified accountant."  _(R-ZM-3)_
- **R-ZM-4** — Mining, farming, or special-sector income. "Mining and certain sector incomes are excluded from turnover tax and have bespoke regimes. Out of scope. Escalate to a ZICA-qualified accountant."  _(R-ZM-4)_
- **R-ZM-5** — Non-resident / withholding-tax matters. "Most non-resident income is taxed via withholding tax, not the PAYE/income-tax bands. Out of scope. Escalate to a ZICA-qualified accountant."  _(R-ZM-5)_
- **R-ZM-6** — Arrears / ZRA enforcement. "Client has outstanding tax arrears or is subject to ZRA enforcement. Late-payment penalties (5% plus BoZ discount rate + 2% interest) compound. Do not advise. Escalate immediately."  _(R-ZM-6)_
- **R-ZM-7** — VAT return requested. "This skill covers income tax / PAYE / turnover tax only. For Zambia VAT, use the zambia-vat skill (if available) or escalate."  _(R-ZM-7)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Amounts are in ZMW (K). Mobile-money references (MTN MoMo, Airtel Money, Zamtel Kwacha) are common in Zambian statements.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Line | Treatment | Notes |
| --- | --- | --- | --- |
| SALARY, STIPENDJU, NET PAY, EMPLOYER [name] | Employment income | PAYE income (employer-side) | Employee tax handled via PAYE, not self-employed return |
| Client name + PAYMENT, DEPOSIT, INVOICE, TRANSFER IN | Business turnover | Self-employed income | If turnover-tax taxpayer, this is turnover base |
| FEES, CONSULTANCY, PROFESSIONAL FEES | Business turnover | Self-employed income | NB: consultancy is EXCLUDED from turnover tax — taxed under income tax |
| MTN MOMO, AIRTEL MONEY, ZAMTEL KWACHA (received) | Business turnover | Self-employed income | Mobile-money receipt — match to invoices |
| STRIPE PAYOUT, PAYPAL PAYOUT, WISE PAYOUT, FLUTTERWAVE | Business turnover | Self-employed income | Platform payout — match to underlying invoices |
| RENT RECEIVED, RENTAL | Rental income | Rental income tax (own regime) | See Section 5.5 — not turnover tax |
| INTEREST, INTERESSI | Investment income | Excluded from turnover tax | Interest is excluded; may be subject to WHT |
| DIVIDEND | Investment income | Excluded from turnover tax | Dividends excluded; usually WHT |
| ZRA REFUND, TAX REFUND | EXCLUDE | Not income | Prior-year tax refund |
| GRANT, GOVERNMENT GRANT | Check nature | Capital grants EXCLUDE; revenue grants = turnover | Flag for reviewer |

### 3.2 Expense Patterns (Debits) -- Allowable (income-tax taxpayers only)

**3.2 Expense Patterns (Debits) -- Allowable (income-tax taxpayers only)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, RENT [commercial] | Office rent | Deductible | Dedicated business premises |
| INSURANCE (business) | Business insurance | Deductible | Must be business-related |
| ACCOUNTANT, AUDITOR, ZICA, BOOKKEEP | Accountancy fees | Deductible |  |
| LAWYER, LEGAL, ADVOCATE (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Advertising | Deductible |  |
| TRAINING, CPD, COURSE, SEMINAR | Training | Deductible | Must relate to current business |
| BANK CHARGE, MAINTENANCE FEE, LEDGER FEE | Bank charges | Deductible | Business account only |
| MOMO CHARGE, MOBILE MONEY FEE, AIRTEL MONEY FEE | Transaction fees | Deductible | Business transactions |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN | IT infrastructure | Deductible |  |

- **Turnover-tax note** — Note: a turnover-tax taxpayer pays 5% on turnover and does NOT deduct expenses. The deduction patterns below apply only to self-employed individuals taxed under the standard income-tax regime.

### 3.3 Expense Patterns (Debits) -- Software / SaaS

**3.3 Expense Patterns (Debits) -- Software / SaaS**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, DROPBOX | Software subscription | Deductible |  |

### 3.4 Expense Patterns (Debits) -- Utilities (apportion if mixed-use)

**3.4 Expense Patterns (Debits) -- Utilities (apportion if mixed-use)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ZESCO | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| LWSC, WATER UTILITY, NWSC | Water | T2 if home office | Proportional if home |
| MTN, AIRTEL, ZAMTEL (airtime/data) | Telecoms | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) -- Travel

**3.5 Expense Patterns (Debits) -- Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| PROFLIGHT, EMIRATES, KENYA AIRWAYS, ETHIOPIAN | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, LODGE | Accommodation | Deductible if business travel |  |
| YANGO, BOLT, ULENDO, TAXI | Local transport | Deductible if business purpose |  |
| FUEL, PETROL, DIESEL, PUMA, TOTAL ENERGIES | Vehicle fuel | T2 -- business % only | Requires mileage log |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, BAR, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private/entertainment in nature |
| GROCERIES, SHOPRITE, PICK N PAY, SPAR, PERSONAL | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, ZRA PENALTY | Fines/penalties | NOT deductible | Public policy |
| ZRA PAYMENT, INCOME TAX, PAYE PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Statutory Deductions / Liability Movements

**3.7 Statutory Deductions / Liability Movements**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NAPSA, PENSION CONTRIBUTION | Statutory deduction (payroll) | 5% employee / 5% employer; not a trading expense for the individual |
| NHIMA, HEALTH INSURANCE | Statutory deduction (payroll) | 0.5% employee / 0.5% employer |
| VAT PAYMENT, ZRA VAT | EXCLUDE | VAT liability payment, not expense |
| PROVISIONAL TAX, ZRA PROVISIONAL | Credit against liability | Not an expense |

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, LOAN PRINCIPAL | EXCLUDE | Loan principal movement |

### 3.9 Zambian Banks / Mobile Money -- Statement Format Reference

**3.9 Zambian Banks / Mobile Money -- Statement Format Reference**

| Provider | Common Patterns | Notes |
| --- | --- | --- |
| Zanaco | TRANSFER, DD, STANDING ORDER, CHARGES | PDF/CSV; date DD/MM/YYYY |
| Stanbic Bank Zambia | PAYMENT, TRF, FEE | PDF/CSV; counterparty in description |
| FNB Zambia | PAYMENT, DEBIT ORDER, FEE | PDF/CSV |
| Absa Zambia | TRANSFER, DEBIT ORDER, CHARGE | PDF |
| MTN MoMo | RECEIVED FROM, SENT TO, WITHDRAWAL, CHARGE | Mobile-money statement; very common |
| Airtel Money | RECEIVED, PAYMENT, CASH OUT, FEE | Mobile-money statement |

## Section 4 -- Worked Examples

All examples use the 2025 bands (identical for 2026). PAYE is computed on monthly gross taxable earnings.

### Example 1 -- Mid-range salary (K8,000/month employee)

**Input line:**
`31/03/2025 ; ZANACO ; EMPLOYER ACME LTD ; SALARY MAR ; +8,000.00 ; ZMW`

**Reasoning:**
Employee. PAYE on K8,000 monthly:
- Up to K7,100 cumulative = K400
- Excess K8,000 − K7,100 = K900 × 30% = K270
- PAYE = K400 + K270 = **K670**
NAPSA employee 5% × K8,000 = K400 (under K1,708.20 cap). NHIMA employee 0.5% × K8,000 = K40.
Net pay = 8,000 − 670 − 400 − 40 = **K6,890**.

**Classification:** PAYE K670; NAPSA (ee) K400; NHIMA (ee) K40; net K6,890.

### Example 2 -- Higher salary above NAPSA ceiling (K40,000/month)

**Input line:**
`30/04/2025 ; STANBIC ; EMPLOYER GLOBE LTD ; SALARY APR ; +40,000.00 ; ZMW`

**Reasoning:**
PAYE on K40,000:
- Up to K9,200 cumulative = K1,030
- Excess K40,000 − K9,200 = K30,800 × 37% = K11,396
- PAYE = K1,030 + K11,396 = **K12,426**
NAPSA employee capped: 5% × K34,164 ceiling = **K1,708.20** (gross exceeds ceiling). NHIMA employee 0.5% × K40,000 = K200.
Net pay = 40,000 − 12,426 − 1,708.20 − 200 = **K25,665.80**.

**Classification:** PAYE K12,426; NAPSA (ee) K1,708.20; NHIMA (ee) K200; net K25,665.80.

### Example 3 -- Below tax-free threshold (K4,500/month)

**Input line:**
`31/05/2025 ; FNB ; EMPLOYER SHOP CO ; WAGES MAY ; +4,500.00 ; ZMW`

**Reasoning:**
K4,500 is below the K5,100 monthly tax-free threshold. PAYE = **K0**.
NAPSA employee 5% × K4,500 = K225. NHIMA employee 0.5% × K4,500 = K22.50.
Net pay = 4,500 − 0 − 225 − 22.50 = **K4,252.50**.

**Classification:** PAYE K0; NAPSA (ee) K225; NHIMA (ee) K22.50; net K4,252.50.

### Example 4 -- Turnover-tax sole trader (mobile-money receipts)

**Input line:**
`12/06/2025 ; MTN MOMO ; RECEIVED FROM CUSTOMER ; SALE ; +3,000.00 ; ZMW`

**Reasoning:**
Sole trader with annual turnover under K5,000,000, taxed under turnover tax. Turnover tax is **5% on turnover above K12,000/year; 0% on the first K12,000** (PwC, ZM other taxes). No expense deductions. If monthly turnover is K3,000 (K36,000/year), tax = (36,000 − 12,000) × 5% = K24,000 × 5% = **K1,200/year** (≈ K100/month once the annual K12,000 is exhausted). Returns due by the 14th of the following month.

**Classification:** Turnover base K3,000 (this receipt); no deductions; 5% applies above the K12,000 annual exemption.

### Example 5 -- Non-deductible entertainment (income-tax trader)

**Input line:**
`22/04/2025 ; ABSA CARD ; CHRISMA RESTAURANT ; CLIENT DINNER ; -850.00 ; ZMW`

**Reasoning:**
Client entertainment is private/entertainment in nature and not wholly and exclusively for the production of income. Not deductible. No apportionment.

**Classification:** NOT deductible. Exclude from expenses.

### Example 6 -- Internal transfer (exclude)

**Input line:**
`15/05/2025 ; ZANACO ; OWN ACCOUNT - SAVINGS ; ; -5,000.00 ; ZMW`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Wholly and Exclusively Test (income-tax taxpayers)

- **Wholly and exclusively test** — An expense is deductible only if incurred wholly and exclusively in the production of income. Mixed-use expenses must be apportioned on a reasonable, documented basis. (General Zambian income-tax principle; verify exact section against the Income Tax Act before publishing — [RESEARCH GAP — reviewer to confirm statutory section].)  _(General Zambian income-tax principle [RESEARCH GAP])_

### 5.2 PAYE Computation (employees)

- **PAYE monthly band application** — Apply the progressive monthly bands (Section 1) to gross monthly taxable earnings: - 0 – K5,100: 0% - K5,101 – K7,100: 20% (cumulative K400 at top) - K7,101 – K9,200: 30% (cumulative K1,030 at top) - Over K9,200: 37% Employer deducts PAYE monthly and remits to ZRA by the 10th of the following month.  _(ZRA payment due dates)_

### 5.3 NAPSA (social security)

- **NAPSA contribution rule** — 10% total = 5% employee + 5% employer, on gross monthly earnings, capped at the K34,164 monthly insurable-earnings ceiling (max K1,708.20 per party). The earnings base includes basic salary, bonuses, commissions, severance, overtime, leave allowance, and acting allowance.  _(NAPSA 2025 announcement)_

### 5.4 NHIMA (health insurance)

- **NHIMA contribution rule** — 1% total = 0.5% employee + 0.5% employer, on gross earnings (basic plus all allowances/overtime/bonuses). Compulsory for all workers including casual, temporary, and contract. Monthly returns due by the 10th.  _(NHIMA — secondary sources; [RESEARCH GAP — reviewer to confirm against the NHIMA Act/SI])_

### 5.5 Self-Employed Regimes

**Self-Employed Regimes**  _(PwC, ZM other taxes; PKF Zambia 2025 Tax Alert; PwC, ZM individual)_

| Regime | Scope | Rate | Source |
| --- | --- | --- | --- |
| Turnover tax | Annual turnover ≤ K5,000,000 (excludes interest, dividends, royalties, consultancy, standard mining) | 0% on first K12,000; 5% above K12,000 | PwC, ZM other taxes; PKF Zambia 2025 Tax Alert |
| Rental income tax | Rental turnover | 0% ≤ K30,000; 4% K30,000–800,000; 16% > K800,000 | PwC, ZM other taxes |
| Presumptive (passenger transport) | Per vehicle, annual | See table below | PwC, ZM other taxes |
| Standard income tax | Turnover > K5,000,000 or excluded income | PAYE bands applied to taxable profit | PwC, ZM individual |

- **Turnover tax filing** — Turnover tax taxpayers pay 5% on turnover above K12,000/year and do NOT deduct expenses. Returns and payment due by the 14th of the following month.  _(PwC, ZM other taxes)_

**Presumptive tax — passenger transport (annual, per vehicle)**  _(PwC, ZM other taxes)_

| Vehicle seating | Annual presumptive tax (ZMW) |
| --- | --- |
| 36–49 seater | 10,368 |
| 22–35 seater | 7,776 |
| 18–21 seater | 5,184 |
| 12–17 seater | 2,592 |
| Below 12 seater (incl. taxis) | 1,296 |

### 5.6 Provisional (Advance) Income Tax — non-employment income

- **Provisional tax filing rule** — Individuals earning over K61,200/year from non-employment sources file quarterly provisional returns. Quarter deadlines: 31 Mar, 30 Jun, 30 Sep, 31 Dec (manual Q1 submission 5 Mar). New registrants after 31 Mar: within 90 days of registration.  _(PwC, ZM individual — tax administration)_

### 5.7 VAT Interaction (self-employed crossing the threshold)

**VAT Interaction**  _(PwC, ZM other taxes; ZRA tax information)_

| Item | Detail | Source |
| --- | --- | --- |
| Standard VAT rate | 16% | PwC, ZM other taxes; ZRA tax information |
| Registration threshold | Annual turnover > K800,000 (or > K200,000 in any consecutive 3-month period) | ZRA tax information; PwC |
| VAT returns | Monthly, due by the 18th (e-filing) | ZRA tax information |

- **K800,000 threshold note** — Note: the K800,000 threshold no longer governs turnover-tax eligibility (now K5m) but still governs VAT registration.  _(ZRA tax information; PwC)_

### 5.8 Non-Deductible Expenses (income-tax taxpayers)

**Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Entertainment (client meals, events) | Not wholly and exclusively for production of income |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax / PAYE itself | Tax on income |
| Capital expenditure | Relieved via capital allowances, not as expense [RESEARCH GAP — reviewer to confirm Zambian wear-and-tear rates] |
| Drawings / personal withdrawals | Not an expense |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (income-tax traders)

- **Home office deduction rule** — - Calculate the proportion of the home used for business (dedicated room as a percentage of total rooms or floor area) - Apply that percentage to: rent, ZESCO electricity, water, internet, maintenance - Must be a dedicated workspace; a dual-use room does NOT qualify **Conservative default:** 0% deduction until reviewer confirms the arrangement. **Flag for reviewer:** confirm room count / floor-area basis and that the workspace is genuinely dedicated.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use rule** — - Only the business-use percentage of fuel, insurance, maintenance, and capital allowances is deductible - Client must maintain a mileage log (business trips vs total) **Conservative default:** 0% business use until a mileage log is provided. **Flag for reviewer:** confirm the business percentage is documented and reasonable, and the applicable wear-and-tear rate. [RESEARCH GAP — reviewer to confirm Zambian capital-allowance rates.]

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rule** — - Business-use portion only (MTN/Airtel/Zamtel airtime and data) **Conservative default:** 0% deduction until the business percentage is confirmed.

### 6.4 Turnover-Tax vs Income-Tax Election

- **Election rule** — - Turnover tax (5%, no deductions) suits low-expense businesses; the standard income-tax regime suits high-expense businesses - The election interacts with the K5,000,000 turnover ceiling and excluded-income rules **Flag for reviewer:** confirm which regime minimises tax and is correctly registered with ZRA.

### 6.5 Rental Income Banding

- **Rental income banding rule** — - Rental turnover is taxed on its own scale (0% / 4% / 16%); confirm gross rental turnover and that no expenses are netted off before applying the rate **Flag for reviewer:** confirm the rental turnover figure and band.

### 6.6 Bad Debt Write-Off (income-tax traders)

- **Bad debt write-off rule** — - Deductible only if the income was previously declared, all reasonable recovery steps were taken, and the debt is genuinely irrecoverable **Flag for reviewer** to confirm all three conditions.

## Section 7 -- Excel Working Paper Template

```
ZAMBIA INCOME TAX -- WORKING PAPER
Charge Year: 2025
Client: ___________________________
Status: Employee (PAYE) / Sole trader (turnover tax) / Sole trader (income tax)

PART A -- EMPLOYEE (PAYE), MONTHLY
  A1. Gross monthly earnings (basic + allowances)   ___________
  A2. PAYE (apply monthly bands)                     ___________
  A3. NAPSA employee 5% (cap K1,708.20)              ___________
  A4. NHIMA employee 0.5%                            ___________
  A5. NET PAY (A1 - A2 - A3 - A4)                    ___________
  Memo: NAPSA employer 5% (cap K1,708.20)            ___________
  Memo: NHIMA employer 0.5%                          ___________

PART B -- SOLE TRADER, TURNOVER TAX
  B1. Annual turnover (excl. interest/dividends/
      royalties/consultancy/mining)                  ___________
  B2. Less exempt first K12,000                       ___________
  B3. Taxable turnover (B1 - B2, not below 0)        ___________
  B4. Turnover tax (B3 x 5%)                          ___________

PART C -- SOLE TRADER, STANDARD INCOME TAX
  C1. Gross business income                           ___________
  C2. Less allowable expenses                         ___________
  C3. Less capital allowances [GAP — rates TBC]       ___________
  C4. Taxable profit (C1 - C2 - C3)                   ___________
  C5. Income tax (apply annual bands)                 ___________
  C6. Less provisional tax paid                       ___________
  C7. Tax due / refund (C5 - C6)                      ___________

REVIEWER FLAGS:
  [ ] Employment status confirmed (PAYE vs self-employed)?
  [ ] Turnover-tax vs income-tax regime confirmed?
  [ ] Turnover below K5,000,000 ceiling confirmed?
  [ ] NAPSA ceiling applied correctly?
  [ ] NHIMA 0.5%/0.5% split confirmed (RESEARCH GAP)?
  [ ] Home office / vehicle / phone business % confirmed?
  [ ] Entertainment and personal expenses excluded?
  [ ] VAT registration status confirmed (> K800,000)?
```

## Section 8 -- Bank Statement Reading Guide

### Zambian Statement Formats

**Zambian Statement Formats**

| Provider | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Zanaco | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description holds counterparty + reference |
| Stanbic Zambia | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant |
| FNB Zambia | PDF, CSV | Date, Description, Amount, Balance | Debit orders for recurring expenses |
| Absa Zambia | PDF | Date, Particulars, Debit, Credit | Shorter descriptions |
| MTN MoMo | PDF/SMS export | Date, Type, Counterparty, Amount, Charge | "Received from" = income; "Sent to" = expense |
| Airtel Money | PDF/SMS export | Date, Type, Counterparty, Amount, Fee | "Cash out" = withdrawal |

### Key Terms

**Key Terms**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| MoMo / Mobile Money | Mobile-money transfer | Check direction for income/expense |
| Cash out / Withdrawal | Cash taken out | Ask what the cash was for |
| Standing order / Debit order | Recurring debit | Regular expense (rent, subscription) |
| Charge / Fee / Ledger fee | Bank or MoMo charge | Deductible (business account) |
| ZESCO | National electricity utility | Utility (T2 if home office) |
| NAPSA / NHIMA | Statutory payroll deductions | Not a trading expense for the individual |
| ZRA | Revenue authority | Tax payment — exclude / credit |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ZAMBIA INCOME TAX
1. Are you an employee (paid a salary) or self-employed (run your own business)?
2. If self-employed: what is your approximate annual turnover? (decides turnover tax vs income tax)
3. Does your income include interest, dividends, royalties, consultancy, or mining? (excluded from turnover tax)
4. Are you VAT-registered, or above K800,000 annual turnover?
5. Do you let property? If so, what is the gross annual rent?
6. Home office: dedicated room or shared space? If dedicated, what % of floor area?
7. Vehicle: used for business? If yes, what % business use, and do you keep a mileage log?
8. Phone/internet: what % is business use?
9. Are NAPSA and NHIMA deducted from your pay (employee) or do you pay them yourself?
10. Have you paid any provisional tax this charge year?
```

## Section 10 -- Reference Material

### Authority and Source References

**Authority and Source References**

| Topic | Reference |
| --- | --- |
| PAYE rates / tax-free threshold | PwC Worldwide Tax Summaries — ZM individual, taxes on personal income (taxsummaries.pwc.com/zambia/individual/taxes-on-personal-income); ZRA PAYE leaflet (zra.org.zm/wp-content/uploads/2025/08/Pay-As-You-Earn.pdf) |
| Filing deadline / provisional tax | PwC — ZM individual, tax administration (taxsummaries.pwc.com/zambia/individual/tax-administration) |
| Turnover / rental / presumptive tax / VAT | PwC — ZM other taxes (taxsummaries.pwc.com/zambia/corporate/other-taxes); PKF Zambia 2025 Tax Alert |
| NAPSA ceiling / rate / NAE | NAPSA 2025 announcement (napsa.co.zm); PwC — ZM individual, other issues |
| NHIMA rate | NHIMA (nhima.co.zm) — secondary; [RESEARCH GAP] |
| Penalties / due dates | ZRA penalties (zra.org.zm/penalties); ZRA payment due dates (zra.org.zm/payment-due-dates) |
| Minimum wage | Ministry of Labour & Social Security (mlss.gov.zm); SI No. 3 of 2025 |

### Filing, Forms & Employer Obligations

**Filing, Forms & Employer Obligations**

| Item | Detail | Source |
| --- | --- | --- |
| Annual individual return deadline | 21 June following the charge year | PwC, ZM individual — tax administration |
| Statute of limitations | 6 years from end of charge year (except fraud/wilful default) | PwC, ZM individual — tax administration |
| Monthly PAYE remittance | by the 10th of the following month | ZRA payment due dates |
| Monthly PAYE return form | ITF P16 (annual reconciliation: P18) | ZRA PAYE leaflet — [RESEARCH GAP: P16 vs P11 inconsistent across sources; confirm on ZRA portal] |
| Turnover-tax return / payment | by the 14th of the following month | PwC, ZM other taxes |
| VAT returns | monthly, by the 18th | ZRA tax information |

### Penalties & Interest

**Penalties & Interest**

| Breach | Charge | Source |
| --- | --- | --- |
| Late submission of return | 250 penalty units per month / part-month (≈ ZMW 75/month at ~K0.30/unit) | ZRA penalties page / penalties leaflet — [RESEARCH GAP: confirm current penalty-unit value] |
| Late payment of tax | 5% of the amount due, plus interest at Bank of Zambia discount rate + 2% | ZRA penalties page |

### Minimum Wage (2025)

No single national minimum wage; set by sector via Statutory Instruments under the Minimum Wages and Conditions of Employment Act (Cap 276).

**Minimum Wage (2025)**

| Order | Monthly (ZMW) | Source |
| --- | --- | --- |
| General Workers Order | 2,313.10 | MLSS / secondary aggregators — [RESEARCH GAP: confirm against SI] |
| Domestic Workers Order | 1,300.00 (incl. housing/transport/lunch allowances) | MLSS / secondary — [RESEARCH GAP] |
| Shop Workers Order | graded by job level | [RESEARCH GAP — specific grades not captured] |
| Transport (SI No. 3 of 2025) | bus drivers 3,000; truck drivers 4,000 | MLSS SI No. 3 of 2025 |

### Test Suite

Input: Employee, gross K4,500/month.
Expected: PAYE K0; NAPSA (ee) K225; NHIMA (ee) K22.50; net K4,252.50.

Input: Employee, gross K8,000/month.
Expected: PAYE K670 (K400 + K900×30%); NAPSA (ee) K400; NHIMA (ee) K40; net K6,890.

Input: Employee, gross K40,000/month.
Expected: PAYE K12,426 (K1,030 + K30,800×37%); NAPSA (ee) capped K1,708.20; NHIMA (ee) K200; net K25,665.80.

Input: Employee, gross K34,164/month.
Expected: NAPSA (ee) = K34,164 × 5% = K1,708.20 (exactly the cap). PAYE = K1,030 + (34,164 − 9,200)×37% = K1,030 + K9,236.68 = K10,266.68.

Input: Self-employed (standard regime), taxable profit K150,000/year.
Expected: Income tax = K12,360 + (150,000 − 110,400)×37% = K12,360 + K14,652 = K27,012.

Input: Sole trader, annual turnover K200,000 (no excluded income), under K5m ceiling.
Expected: Turnover tax = (200,000 − 12,000) × 5% = K188,000 × 5% = K9,400/year.

Input: Gross annual rent K500,000.
Expected: Rental income tax at 4% (band K30,000–800,000) = K500,000 × 4% = K20,000. [Confirm whether the first K30,000 is 0% before applying — PwC bands as stated; reviewer to confirm marginal vs flat application.]

Input: K850 client dinner claimed as expense (income-tax trader).
Expected: Remove — not deductible.

## PROHIBITIONS

- NEVER compute tax without confirming employee (PAYE) vs self-employed status
- NEVER apply turnover tax to interest, dividends, royalties, consultancy, or standard mining income
- NEVER allow expense deductions for a turnover-tax taxpayer (5% is on turnover)
- NEVER exceed the NAPSA insurable-earnings ceiling (K34,164/month → max K1,708.20 per party)
- NEVER treat NAPSA or NHIMA as a trading expense of the individual
- NEVER allow entertainment, personal, or fine/penalty expenses as deductions
- NEVER allow income tax / PAYE itself as a deduction
- NEVER assume the 2025 NAPSA ceiling, NHIMA split, or minimum wage carries into 2026 without confirmation
- NEVER treat a [RESEARCH GAP] figure as confirmed — flag it for the reviewer
- NEVER present tax calculations as definitive -- always label as estimated and pending professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, ZICA-qualified accountant, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
