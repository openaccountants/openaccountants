---
name: rwanda-income-tax
description: "Rwanda personal income tax for 2026: PAYE bands, casual labour, micro and small business regimes, real regime, capital gains at 10%, the annual declaration by 31 March and how to file it in E-Tax. Use for employees and self-employed individuals in Rwanda."
version: 0.2
jurisdiction: RW
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda Income Tax: PAYE and self-employed

Tax year 2026: 1 January to 31 December 2026 (Law 027/2022 art 8). The law has not changed for 2026 rates; the 2026 changes are two ministerial orders (certification threshold, simplified accounting).

## Who this applies to

Individuals. A resident (permanent residence, habitual abode, 183 days in the tax period, or an average of more than 122 days in each of the two prior periods and present this period; art 4) pays on domestic and foreign income. A non-resident pays only on Rwanda-source income (art 12). Companies: see [rw-corporate-income-tax](rw-corporate-income-tax.md). Payroll mechanics: see [rwanda-payroll](rwanda-payroll.md).

KIFC: a new resident not resident in the prior 5 years, working as an expert or professional directly for an entity with Kigali International Financial Centre licensed activities, is exempt on foreign-source income for the first 5 years (art 12).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Annual band 0% | FRW 0 to 720,000 | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/calculate-paye |
| Annual band 10% | FRW 720,001 to 1,200,000 | 2026 | same |
| Annual band 20% | FRW 1,200,001 to 2,400,000 | 2026 | same |
| Annual band 30% | FRW 2,400,001 and above | 2026 | same |
| Monthly PAYE bands | 0% to 60,000; 10% to 100,000; 20% to 200,000; 30% above | 2026 | same |
| Casual labourer | 15%; first FRW 60,000 a month at 0% (art 56) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| Second employer | 30% (art 57; Handbook category S) | 2026 | same |
| Micro-enterprise, turnover FRW 2,000,000 to 4,000,000 | FRW 60,000 a year (art 14) | 2026 | same |
| Micro-enterprise, FRW 4,000,001 to 7,000,000 | FRW 120,000 | 2026 | same |
| Micro-enterprise, FRW 7,000,001 to 10,000,000 | FRW 210,000 | 2026 | same |
| Micro-enterprise, FRW 10,000,001 to 12,000,000 | FRW 300,000 | 2026 | same |
| Small business, turnover FRW 12,000,001 to 20,000,000 | 3% of turnover (arts 3, 14) | 2026 | same |
| Farming and livestock exemption | Turnover up to FRW 12,000,000 (art 21) | 2026 | same |
| No annual declaration | Turnover under FRW 2,000,000, employment income only, or investment income under withholding only (art 9 as amended) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf |
| Capital gains on shares, licences, debt instruments, options, guarantees | 10% (arts 36-37 as amended) | 2026 | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b |
| Certification of statements | Turnover of FRW 1,000,000,000 or more (Order 009, art 3) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Ministerial_orders-Financial_statements.pdf |

The first-year tables in arts 14 and 56 (0/20/30) applied only to the first year after the law; use the bands above.

## The base

Employment income covers wages, leave and sick pay, commissions, bonuses, allowances, reimbursed private expenses, redundancy pay and pensions (art 15). Not taxed: reimbursement wholly for the employer's business, employer contributions to RSSB, RSSB pensions (art 16). Employee RSSB contributions are not on that list, so PAYE is on gross; see the payroll skill. Benefits: car 10% of employment income, housing 20%, others at market value (art 18; Handbook PAYE chapter).

Real regime: income from all business activities less expenses that are wholly for the business, real, documented with invoices or receipts accepted by RRA, and of the period (arts 19, 24). Taxable income is rounded to the nearest FRW 1,000 (art 14). Not deductible: fines, income tax, entertainment except general sporting activity for staff, donations beyond 1% of turnover to non-profits, 20% of overheads with inseparable private use, and more (art 25). Losses carry forward 5 tax periods; RRA can authorise more (art 31; Order 003, art 33). Foreign losses do not offset. Depreciation: buildings and heavy machinery 5%, purchased intangibles 10%, information and communication systems with a life of 10 years or more 10%, computers and shorter-life systems 50% (pool), other assets 25% (pool) (art 27).

Micro and small regimes tax turnover or a flat amount, with no expenses. A small business may opt for the real regime; the choice binds for 3 years, and simplified records (daily sales, daily purchases, money transactions) suffice (art 14; Order 003, art 32). Liberal professions cannot use the flat or lump-sum regimes (art 14). Road transport has its own flat table in the annex to the law.

### Decision table

| If | Then |
|---|---|
| Only salary | No annual return; PAYE is final, unless several employers and a refund is claimed (art 9(6)) |
| Turnover under FRW 2,000,000 | No declaration |
| Turnover up to FRW 12,000,000 | Flat amount |
| Turnover FRW 12,000,001 to 20,000,000 | 3%, or opt for the real regime for 3 years |
| Turnover over FRW 20,000,000, or a liberal profession | Real regime |

### Carried: Required Inputs and Refusal Catalogue

#### Required Inputs

**Minimum viable** : for an **employee**: monthly gross salary breakdown (basic + housing + transport + other allowances) and confirmation of resident/non-resident status. For a **self-employed individual**: bank statement for the full tax year (CSV, PDF, or pasted text) plus confirmation of annual turnover and chosen/eligible regime.

**Recommended** : payslips, RSSB contribution records, benefits-in-kind details (housing, vehicle), prior-year PIT declaration or RRA assessment, sales/purchase records (self-employed).

**Ideal** : complete income and expenditure account (real regime), asset register, RSSB statements for all schemes, casual-labour registers, KIFC expert status documentation (if applicable).

**Refusal if minimum is missing : SOFT WARN.** No salary breakdown or no bank statement at all = hard stop. Salary stated as a single gross figure with no allowance split = proceed with reviewer warning: "Benefit-in-kind and RSSB contribution bases depend on the allowance split (housing/transport). This computation assumed [stated assumption]. The reviewer must confirm the allowance breakdown."

#### Refusal Catalogue

- **R-RW-1 : Residence status unknown** : "Residence status affects the scope of taxable income (worldwide for residents vs Rwanda-source only for non-residents). This skill cannot compute tax without it. Please confirm before proceeding."
- **R-RW-2 : Companies, partnerships, group structures** : "This skill covers individual taxpayers (employees and sole-trader / turnover-regime self-employed). Companies file Corporate Income Tax (28%) separately. Escalate to a Rwanda-licensed practitioner."
- **R-RW-3 : KIFC expert exemption** : "New residents (not resident in the prior 5 years) working as experts for Kigali International Financial Centre (KIFC)-licensed entities may be exempt from PIT on foreign-source income for their first 5 years. This requires specialist confirmation of eligibility. Escalate."
- **R-RW-4 : Capital gains / share disposals** : "Capital gains on shares are taxed at 10% under separate rules. Out of scope for this PAYE/PIT skill. Escalate."
- **R-RW-5 : Arrears / RRA enforcement** : "Client has outstanding tax arrears or is subject to RRA enforcement. Administrative fines reach 60% of tax due and late-payment interest accrues monthly (capped at 100% of the tax). Do not advise. Escalate immediately."
- **R-RW-6 : VAT return requested** : "This skill covers income tax (PIT/PAYE) only. Rwanda VAT is standard-rated at 18% with a registration threshold of RWF 20,000,000/year (or RWF 5,000,000/quarter). Use a dedicated VAT skill."

### Carried: Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5. Patterns appear in English, Kinyarwanda, and French because Rwandan bank statements use all three.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

#### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MUSHAHARA, SALARY, SALAIRE, PAYE NET, EMPLOYER [name] | Employment income | PAYE should already be withheld at source by employer |
| Client name + TRANSFER, DEPOSIT, KWISHYURA, PAIEMENT | Business income (self-employed) | Turnover for regime test; if VAT-registered, extract net (excl. 18% VAT) |
| FEES, HONORARIES, HONORAIRES, CONSULTANCY, AMAFARANGA Y'AKAZI | Business income | Professional fees |
| MOMO PAYOUT, MTN MOMO, AIRTEL MONEY (business inflow) | Business income | Mobile-money inflow : match to invoices |
| STRIPE / PAYPAL / WISE / UPWORK / FIVERR PAYOUT | Business income | Platform payout : net of platform commission |
| RENT RECEIVED, UBUKODE, LOYER | Rental income | Separate income stream : not turnover for the trading regimes |
| INTEREST, INYUNGU, INTÉRÊTS | Investment income | May be subject to withholding tax |
| DIVIDEND, IMIGABANE, DIVIDENDE | Investment income | Subject to withholding tax |
| RRA REFUND, TAX REFUND | EXCLUDE | Refund of prior tax |
| AGRICULTURE, LIVESTOCK, UBUHINZI, UBWOROZI proceeds | Business income : but see exemption | Agriculture/livestock income exempt up to RWF 12,000,000/period; only excess taxed |

#### 3.2 Expense Patterns (Debits) : Deductible under the Real Regime Only

**3.2 Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, UBUKODE BW'IBIRO, LOYER BUREAU | Office rent | Deductible (real regime) | Dedicated business premises |
| ACCOUNTANT, AUDITOR, IBARURAMARI | Accountancy fees | Deductible |  |
| LAWYER, AVOCAT, LEGAL | Legal fees | Deductible | Must be business-related |
| OFFICE SUPPLIES, IBIKORESHO BY'IBIRO | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| BANK FEE, AMAFARANGA YA BANKI, FRAIS BANCAIRES | Bank charges | Deductible | Business account only |
| MOMO FEE, MTN/AIRTEL TRANSACTION FEE | Mobile-money fees | Deductible | Business transactions |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, ZOOM | Software subscription | Deductible | Recurring operating expense |

> Deductions are only relevant under the **real regime**. Micro-enterprise (flat) and lump-sum taxpayers pay on turnover and CANNOT deduct expenses.

#### 3.3 Expense Patterns (Debits) : Utilities (Real Regime, may need apportionment)

**3.3 Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| REG (Rwanda Energy Group), EUCL, ELECTRICITY, AMASHANYARAZI | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| WASAC, WATER, AMAZI | Water | T2 if home office |  |
| MTN, AIRTEL, INTERNET, CANALBOX | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |

#### 3.4 Expense Patterns (Debits) : Travel (Real Regime)

**3.4 Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RWANDAIR, FLIGHT, INDEGE | Flights | Deductible if business travel | Must be wholly business |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| YEGO MOVES, BOLT, TAXI, MOTO | Local transport | Deductible if business purpose |  |
| FUEL, LISANSI, CARBURANT, SP / ENGEN / KOBIL | Vehicle fuel | T2 : business % only | Requires mileage log |

#### 3.5 Expense Patterns (Debits) : NOT Deductible

**3.5 NOT Deductible table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RESTAURANT, ENTERTAINMENT, CLIENT MEAL | NOT deductible | Private/entertainment cost |
| GROCERIES, SUPERMARKET, SIMBA, NAKUMATT, PERSONAL | NOT deductible | Private living costs |
| FINE, PENALTY, IHAZABU, AMENDE | NOT deductible | Public policy |
| RRA PAYMENT, INCOME TAX, PAYE PAYMENT | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | NOT deductible | Not an expense |

#### 3.6 RSSB and Statutory Deductions (Special Handling)

**3.6 RSSB and Statutory Deductions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RSSB PENSION, PENSIYO | Statutory contribution | Employee 6% / Employer 6% of gross |
| RSSB OCCUPATIONAL, OCCUPATIONAL HAZARD | Statutory contribution | Employer 2% only (rate unverified) |
| RSSB MATERNITY | Statutory contribution | Employee 0.3% / Employer 0.3% |
| RSSB MEDICAL, RAMA | Statutory contribution | Employer 7.5% / Employee 7.5% of basic salary (public sector / opt-in) |
| CBHI, MUTUELLE, MUTUELLE DE SANTÉ | Statutory contribution | Employee 0.5% of net salary |

#### 3.7 Exclusions (Neither Income nor Expense)

**3.7 Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, INGUZANYO, PRÊT | EXCLUDE | Loan principal movement |
| VAT PAYMENT, RRA VAT | EXCLUDE | VAT liability payment, not expense |

#### 3.8 Rwandan Banks / Channels : Statement Format Reference

**3.8 Rwandan Banks / Channels table**

| Channel | Common Patterns | Notes |
| --- | --- | --- |
| Bank of Kigali (BK) | TRANSFER, RTGS, CHARGES, MUSHAHARA | PDF/CSV; date format DD/MM/YYYY |
| I&M Bank Rwanda | PAYMENT, TRF, FEE | PDF/CSV; counterparty in description field |
| Equity Bank Rwanda | TRANSFER, DEBIT, CHARGE | PDF |
| MTN MoMo / Airtel Money | MOMO PAYMENT, CASH IN, CASH OUT, FEE | CSV/SMS export; very common for micro-enterprises |
| BPR / Cogebanque | TRANSFER, VIREMENT, FRAIS | PDF; French terms common |

### Carried: Tier 2 Catalogue (Reviewer Judgement Required)

#### 6.1 Home Office Deduction (Real Regime)

- **Home office deduction rule** : - Calculate proportion of home used for business (dedicated room/floor area as a percentage of the whole). - Apply that percentage to rent, electricity (REG/EUCL), water (WASAC), internet. - A dual-use room does NOT qualify. **Conservative default:** 0% deduction until reviewer confirms the arrangement.

#### 6.2 Motor Vehicle Business Use (Real Regime)

- **Motor vehicle business use rule** : - Only the business-use percentage of fuel, insurance, and maintenance is deductible. - Client must maintain a mileage log. **Conservative default:** 0% business use until a mileage log is provided.

#### 6.3 Phone / Internet Mixed Use (Real Regime)

- **Phone/internet mixed use rule** : - Business-use portion only; client must provide a reasonable estimate. **Conservative default:** 0% deduction until business percentage is confirmed.

#### 6.4 Benefit-in-Kind Edge Cases

- **Benefit-in-kind edge cases** : - Confirm whether housing/transport allowances are cash allowances (part of the RSSB pension base) or benefits in kind (statutory 20%/10% valuation). - **Flag for reviewer:** the allowance split materially affects both PAYE and RSSB.

#### 6.5 Regime Election

- **Regime election flag** : - Electing into the real regime is irrevocable for 3 years : flag the long-term consequences for reviewer sign-off.

#### 6.6 Agriculture / Livestock Threshold

- **Agriculture/livestock threshold flag** : - Confirm the split between exempt (first RWF 12,000,000) and taxable agricultural income.

#### 6.7 KIFC Expert Status

- **KIFC expert status flag** : - Confirm prior-5-year non-residence and KIFC-licensed employer before applying the foreign-source exemption.

### Carried: Excel Working Paper Template

```
RWANDA INCOME TAX: WORKING PAPER
Tax Year: 2026
Client: ___________________________
Residence: Resident / Non-resident
Taxpayer type: Employee (PAYE) / Self-employed (Micro / Lump-sum / Real)

A. EMPLOYMENT INCOME (PAYE PATH)
  A1. Basic salary (annual or monthly)           ___________
  A2. Housing allowance / benefit (20% if BIK)   ___________
  A3. Transport allowance                        ___________
  A4. Vehicle benefit (10% if BIK)               ___________
  A5. Other taxable allowances                   ___________
  A6. TOTAL taxable employment income            ___________
  A7. PAYE (apply bracket table)                 ___________

B. SELF-EMPLOYMENT : REGIME TEST
  B1. Annual turnover                            ___________
  B2. Regime (Exempt <2M / Micro / Lump-sum 3% / Real)  ______
  B3. Micro flat tax OR Lump-sum 3% OR Real-regime net profit  ______

C. REAL REGIME : NET PROFIT (if applicable)
  C1. Gross business income (net of 18% VAT if registered)  ____
  C2. Less: deductible business expenses          ___________
  C3. Net taxable profit (C1 - C2)                ___________
  C4. PIT (apply annual bracket table)            ___________

D. RSSB CONTRIBUTIONS (employee side)
  D1. Pension 6% of gross                         ___________
  D2. Maternity 0.3% of gross                     ___________
  D3. Medical 7.5% of basic (if applicable)       ___________
  D4. CBHI 0.5% of net salary                     ___________
  D5. TOTAL employee RSSB                         ___________

E. NET PAY (employee)
  E1. Gross - PAYE - employee RSSB                ___________

REVIEWER FLAGS:
  [ ] Residence status confirmed?
  [ ] Employee vs self-employed confirmed?
  [ ] Turnover band / regime confirmed?
  [ ] Allowance split (housing/transport) confirmed?
  [ ] Benefit-in-kind valuation confirmed (housing 20% / vehicle 10%)?
  [ ] Real-regime deductions supported by documents?
  [ ] Agriculture/livestock exemption applied correctly?
  [ ] KIFC expert status (if claimed) verified?
  [ ] Casual-labour 15% applied only where genuinely casual?
```


## Deadlines and filing

| Item | Deadline | Source |
|---|---|---|
| Annual declaration and payment | 31 March 2027 for 2026 (arts 9, 10) | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf |
| Quarterly prepayments | 30 June, 30 September, 31 December (art 33) | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| Capital gains tax | 15 days after the month of sale (art 37) | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b |
| Provisional filing, certified taxpayers | On approval, certified statements within 3 months of the provisional declaration (art 9(3)) | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf |

Prepayment = tax of the prior year / turnover of the prior year x turnover of the quarter, less tax withheld that quarter.

### How to file a real regime declaration

1. Log in at https://etax.rra.gov.rw with TIN and password. Real regime is E-Tax only; flat and lump-sum may also use M-Declaration (https://www.rra.gov.rw/en/taxes-fees/domestic-taxes/income-tax/declare-income-tax-1).
2. Annexure Downloads, choose the PIT annexure. Enable content, complete each relevant tab, validate and save.
3. Prepare the Profit and Loss Account and Balance Sheet annexures and the Representative annexure. Certified statements are uploaded by the approved firm where turnover reaches the threshold.
4. Fill the declaration; enter Quarterly Prepayments and withholdings as credits. Declaration and annexures must agree or it will not submit.
5. Tick the certifying box and submit. Keep the acknowledgement receipt: its RRA Reference Number (doc ID) and amount are what you pay against.
6. Pay by e-banking, mobile money, MobiCash or at a bank by 31 March.

Steps from the RRA Tax Handbook 2025 (https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf). The Handbook and the RRA income tax page still state FRW 600,000,000 for certification; Order 009 of 24/09/2026 sets FRW 1,000,000,000 and wins.

## Penalties and interest

| Fault | Consequence | Source |
|---|---|---|
| Late declaration, fixed fine (Law 020/2023 art 81) | FRW 50,000 for a non-commercial person or turnover over FRW 2,000,000 up to FRW 20,000,000; FRW 300,000 for a public institution or non-profit with turnover over FRW 20,000,000; FRW 500,000 for a notified large taxpayer | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf |
| Repeat fault within 2 years | Fine doubled; third time, four times | same |
| Certified statements not filed when required | FRW 500,000 every month until filed | same |
| Late declaration and payment (art 82) | 20% of tax up to 30 days, 40% from day 31 to 60, 60% after 60 days | same |
| Declared on time, paid late (art 82) | 5% up to 30 days, 10% from day 31 to 60, 30% after 60 days | same |
| Understatement of 10% to 20% (art 83) | 10% of the understatement; doubles above 20%; none if corrected and paid before notice of audit, but art 82 fines apply | same |
| Late-payment interest (art 80) | 0.5% a month up to 6 months, 1% from 6 to 12 months, 1.5% after 12 months; not compounded; every started month counts; capped at 100% of the tax | same |
| Tax evasion (art 81) | Fine equal to the evaded tax, plus criminal penalties | same |

Payments offset principal tax first, then the fine, then interest (art 80). The Law's art 82 text reads "twenty percent (10%)" for the middle band; we follow the figure 10%, as the numeric text and the 5/10/30 scale show.

Records are kept 10 years (Law 020/2023 art 15). The audit power lapses after 5 years, 10 if information was concealed to evade tax (art 35).

## Cross-border points

Residents are taxed on foreign income; foreign tax on business profit is not a deduction (art 25) and is entered as a Foreign Tax Credit in the declaration (Handbook). Withholding on payments to non-residents, and treaties: see [rw-corporate-income-tax](rw-corporate-income-tax.md). Foreign employer paying a non-resident for services in Rwanda with no permanent establishment: exempt (art 16). Employer with no withholding duty under a treaty: employee self-declares within 15 days of the month end (art 58).

## Two worked examples that recompute

**Example 1. Monthly PAYE on FRW 500,000.** 4,000 at 10%, 20,000 at 20%, 90,000 at 30%.

```oa-check
name: Monthly PAYE, gross FRW 500,000
inputs:
  gross: 500000
steps:
  - band_10: (min(gross, 100000) - 60000) * 0.10
  - band_20: (min(gross, 200000) - 100000) * 0.20
  - band_30: (gross - 200000) * 0.30
  - paye: band_10 + band_20 + band_30
expected:
  paye: 114000.00
```

**Example 2. Decision: stay on 3% or opt for the real regime.** Turnover FRW 18,000,000, profit FRW 3,000,000. Lump sum: 540,000. Real regime: 468,000. The real regime saves FRW 72,000 this year, but binds for 3 years and needs records. Opt only if profit stays below the point where tax equals 3% of turnover.

```oa-check
name: Small business, 3% or real regime
inputs:
  turnover: 18000000
  profit: 3000000
steps:
  - lump: turnover * 0.03
  - real: 48000 + 240000 + (profit - 2400000) * 0.30
  - saving: lump - real
expected:
  lump: 540000.00
  real: 468000.00
  saving: 72000.00
```

## Ask the client first

1. Resident in Rwanda in 2026? On which test?
2. Salary only, or business income? Which turnover?
3. Liberal profession or road transport?
4. Records good enough for the real regime?
5. Any share sale, and were the shares listed in Rwanda?
6. Any foreign income or foreign tax paid?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 027/2022 establishing taxes on income (read: arts 3-5, 8-10, 12-21, 24-33, 36-38, 44-50, 56-69) | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf | 2026-11-01 |
| Law 051/2023 amending the income tax law (whole) | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf | 2026-11-01 |
| Official Gazette Special of 29/05/2025: Law 009/2025 (VAT), Law 014/2025 (income tax) (whole of both) | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b | 2026-11-01 |
| Law 020/2023 on tax procedures (read: arts 15, 35, 78, 80-88) | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf | 2026-11-01 |
| Ministerial Order 003/26/10/TC of 29/04/2026 (read: arts 17, 19, 32-33) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/Ministerial_Order_on_Simplified_Accounting_Method_April_2026.pdf | 2026-11-01 |
| Ministerial Order 009/26/10/TC of 24/09/2026 (whole) | https://www.rra.gov.rw/fileadmin/user_upload/Ministerial_orders-Financial_statements.pdf | 2026-11-01 |
| RRA Tax Handbook 2025 (read: E-Tax steps, real regime, PAYE, VAT declaration chapters) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf | 2026-11-01 |
| RRA, Calculate PAYE page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/calculate-paye | 2026-11-01 |
| RRA, Declare Income Tax page (whole page) | https://www.rra.gov.rw/en/taxes-fees/domestic-taxes/income-tax/declare-income-tax-1 | 2026-11-01 |

Not yet confirmed: the 10% and 20% benefit rules for housing rest on the Handbook, as art 18 was read only in part; the road transport annex amounts were not captured from the PDF table, so use the annex directly; trading licence declaration by 31 January is carried from the old file and was not re-read; treatment of a home office, vehicle and phone in the real regime is our working practice and not a rule in the law; RRA rounding of monthly PAYE is not stated in the pages read.

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
