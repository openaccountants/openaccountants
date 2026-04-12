---
name: in-income-tax
description: >
  Use this skill whenever asked about Indian income tax for self-employed professionals, freelancers, or sole proprietors. Trigger on phrases like "how much tax do I pay in India", "ITR-4", "ITR-3", "Sugam", "Section 44ADA", "Section 44AD", "presumptive taxation", "new tax regime", "old tax regime", "advance tax India", "TDS credit", "PAN", "80C", "80D", "income tax return India", "surcharge", "health and education cess", "UPI income", "Razorpay payout", "Paytm business", or any question about filing or computing income tax for a self-employed individual in India. This skill covers new regime vs old regime rate tables, presumptive taxation (44ADA for professionals, 44AD for business), regular computation (ITR-3), surcharge, cess, standard deduction, Section 80C/80D deductions, advance tax schedule, TDS credits, PAN requirements, and ITR-4 (Sugam) structure. ALWAYS read this skill before touching any Indian income tax work.
version: 2.0
jurisdiction: IN
tax_year: 2025-26
category: international
depends_on:
  - income-tax-workflow-base
---

# India Income Tax (आयकर) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | India (भारत) |
| Tax | Income Tax + Health & Education Cess (4%) + Surcharge (if applicable) |
| Currency | INR only |
| Tax year | Financial Year (FY): 1 April -- 31 March |
| Current year | FY 2025-26 (Assessment Year 2026-27) |
| Primary legislation | Income Tax Act, 1961 (as amended by Finance Act, 2025) |
| Tax authority | Central Board of Direct Taxes (CBDT) / Income Tax Department |
| Filing portal | incometax.gov.in |
| Filing deadline | 31 July 2026 (non-audit cases) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Chartered Accountant (India) |
| Skill version | 2.0 |

### New Tax Regime Rate Table -- FY 2025-26 (Default) [T1]

| Total Income (INR) | Rate |
|---|---|
| 0 -- 4,00,000 | 0% |
| 4,00,001 -- 8,00,000 | 5% |
| 8,00,001 -- 12,00,000 | 10% |
| 12,00,001 -- 16,00,000 | 15% |
| 16,00,001 -- 20,00,000 | 20% |
| 20,00,001 -- 24,00,000 | 25% |
| Above 24,00,000 | 30% |

**Section 87A Rebate (New Regime):** If taxable income ≤ Rs. 12,00,000, tax is fully rebated (zero tax). For salaried persons with Rs. 75,000 standard deduction, effective zero-tax threshold is Rs. 12,75,000.

**Cess:** Add 4% Health & Education Cess on all income tax computed (after rebate).

### Old Tax Regime Rate Table (Below 60) [T1]

| Total Income (INR) | Rate |
|---|---|
| 0 -- 2,50,000 | 0% |
| 2,50,001 -- 5,00,000 | 5% |
| 5,00,001 -- 10,00,000 | 20% |
| Above 10,00,000 | 30% |

**Section 87A Rebate (Old Regime):** If taxable income ≤ Rs. 5,00,000, rebate up to Rs. 12,500 applies.

### Surcharge (Both Regimes) [T1]

| Total Income (INR) | Surcharge Rate |
|---|---|
| Up to 50,00,000 | Nil |
| 50,00,001 -- 1,00,00,000 | 10% of income tax |
| 1,00,00,001 -- 2,00,00,000 | 15% of income tax |
| 2,00,00,001 -- 5,00,00,000 | 25% of income tax (new regime only 25%) |
| Above 5,00,00,000 | 37% (old regime); 25% (new regime cap) |

### Presumptive Taxation Rates [T1]

| Section | Who | Presumptive Rate | Threshold |
|---|---|---|---|
| 44ADA | Specified professionals (doctors, lawyers, CAs, architects, consultants, etc.) | 50% of gross receipts = deemed profit | Gross receipts ≤ Rs. 75,00,000 |
| 44AD | Business owners (non-professionals) | 8% of turnover (6% if digital receipts) = deemed profit | Turnover ≤ Rs. 3,00,00,000 |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Regime not specified | New tax regime |
| Nature of income unclear (professional vs business) | Professional (44ADA) -- more conservative |
| Digital vs cash receipt mix unknown | 100% cash (8% rate under 44AD, not 6%) |
| Filing status unknown | Individual below 60 |
| TDS credits not confirmed | Exclude until Form 26AS verified |
| Advance tax paid unknown | Nil advance tax paid |

### Red Flag Thresholds [T1]

| Flag | Threshold |
|---|---|
| 44ADA limit exceeded | Gross receipts > Rs. 75,00,000 -- must file ITR-3 |
| 44AD limit exceeded | Turnover > Rs. 3,00,00,000 |
| Advance tax mandatory | Tax liability > Rs. 10,000 in the year |
| TAN required (deductor) | If the self-employed person pays salaries or contractor fees |
| Tax audit required (professional) | If gross receipts > Rs. 75,00,000 under 44ADA |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full financial year (1 April -- 31 March) in PDF, CSV, or pasted text. Confirmation of whether income is professional or business, and whether new or old regime applies.

**Recommended:** Form 26AS / Annual Information Statement (AIS) for TDS credits, advance tax challans (ITNS 280), all client invoices, Form 16A (TDS certificates from clients), PAN.

**Ideal:** Complete books of accounts (if not presumptive), all receipts for deductions under 80C/80D (old regime only), GST returns (if GST-registered).

### Refusal Catalogue

**R-IN-1 -- Non-Resident Indians (NRI) and RNOR.** "This skill covers Resident individuals only. NRI/RNOR taxation involves different income sourcing rules, DTAA analysis, and TRC requirements. Escalate."

**R-IN-2 -- Firms, Companies, LLPs.** "This skill covers individuals (sole proprietors/freelancers) only. Partnership firms, private limited companies, and LLPs file separate returns with different rates. Out of scope."

**R-IN-3 -- Capital Gains.** "Capital gains on shares, mutual funds, property, or other assets require detailed computation under Sections 111A, 112, and 112A. Escalate."

**R-IN-4 -- International Transactions / DTAA.** "Double taxation treaty analysis, foreign tax credits, and transfer pricing are out of scope. Escalate."

**R-IN-5 -- Tax Audit Cases (non-presumptive).** "If gross receipts exceed the presumptive threshold and a tax audit is required under Section 44AB, this skill cannot replace a statutory audit. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| NEFT CR / RTGS CR / IMPS CR [client name] | Gross receipts (44ADA/44AD) | Business income | Professional service fee received -- add to gross receipts |
| UPI [client name] / UPI CREDIT | Gross receipts | Business income | Digital receipt -- counts as electronic for 44AD 6% rate |
| RAZORPAY SETTLEMENT / RAZORPAY TRANSFER | Gross receipts | Business income | Payment gateway payout -- match to invoices |
| PAYTM PAYOUT / PAYTM SETTLEMENT | Gross receipts | Business income | Digital payment payout -- electronic for 44AD |
| CASHFREE SETTLEMENT / CASHFREE PAYOUT | Gross receipts | Business income | Payment aggregator payout |
| STRIPE PAYOUT INDIA / STRIPE TRANSFER | Gross receipts | Business income | International invoicing via Stripe India |
| PAYPAL TRANSFER / PAYPAL PAYOUT | Foreign income (Gross receipts) | Business income in INR | Convert at RBI reference rate on date received |
| SALARY CREDIT / SAL ADV [employer] | Salary income (Section 17) | NOT professional income | Employment income -- separate head, Form 16 required |
| INTEREST CREDIT / INT CREDIT / FD INTEREST | Income from Other Sources | NOT business income | Bank interest taxable; FD interest TDS may apply |
| DIVIDEND CREDIT / DIV [company] | Income from Other Sources | Taxable dividends | Domestic dividends taxable since FY 2020-21 |
| REFUND FROM INCOMETAX / IT REFUND | EXCLUDE | Not income | Tax refund is not taxable |
| LOAN DISBURSEMENT / LOAN CREDIT | EXCLUDE | Not income | Loan principal is liability, not income |
| GST REFUND / IGST REFUND | EXCLUDE | Not income | GST refund is not taxable income |

### 3.2 Expense Patterns (Debits -- for ITR-3 filers; ITR-4 presumptive filers do not itemise)

| Pattern | Schedule C Category | Treatment | Notes |
|---|---|---|---|
| OFFICE RENT / COMMERCIAL RENT [landlord] | Rent | Fully deductible | Deduct TDS at 10% if monthly rent > Rs. 50,000 |
| ELECTRICITY [BESCOM/MSEDCL/TATA POWER/TNEB] | Utilities | Deductible (business portion) | Home office: apportion by usage |
| BROADBAND / JIOFIBER / ACT / AIRTEL BROADBAND | Communication | Deductible (business portion) | Mixed use: apportion |
| MOBILE RECHARGE / AIRTEL / JIO / VI | Communication | Deductible (business portion) | Business calls only |
| SWIGGY BUSINESS / ZOMATO FOR BUSINESS | Meals/entertainment | Deductible if business | Document business purpose |
| AMAZON BUSINESS / FLIPKART BUSINESS | Office supplies | Fully deductible | Business account purchases |
| ZOHO SUBSCRIPTION / FRESHBOOKS / TALLY | Software | Fully deductible | Business software |
| GOOGLE ADS / META ADS / LINKEDIN ADS | Advertising | Fully deductible | Digital marketing |
| CA FEES / LEGAL FEES / CONSULTANT FEES | Professional charges | Fully deductible | TDS may be required (Section 194J) |
| LIC PREMIUM / TERM INSURANCE | NOT business expense | Section 80C deduction (old regime) | Personal insurance = not a business expense |
| HEALTH INSURANCE / MEDICLAIM [Star/HDFC Ergo/Bajaj] | NOT business expense | Section 80D deduction (old regime) | NOT deductible as business expense |
| PPF DEPOSIT / ELSS PURCHASE / NSC | NOT business expense | Section 80C deduction (old regime) | Investment deductions |
| ADVANCE TAX CHALLAN / ITNS 280 | EXCLUDE | Prepaid tax | Not a business expense; credit against liability |
| TDS DEDUCTED / TDS TO GOVT | EXCLUDE | Prepaid tax (credit) | Claim as credit on Form 26AS |
| GST PAYMENT / GST CHALLAN | EXCLUDE | Indirect tax | Not deductible as income tax expense |
| SWIPE / POS [vendor] | Mixed -- check | Identify payee | Could be office supply, travel, entertainment |
| PROFESSIONAL TAX [state] | Deductible | Fully deductible | State professional tax paid |
| BANK CHARGES / ACCOUNT MAINTENANCE / NEFT CHARGES | Bank charges | Fully deductible | Business account only |

### 3.3 UPI and Digital Platform Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| UPI/CR/[amount]/[client name] | Gross receipts | Electronic -- qualifies for 6% deemed profit under 44AD |
| PHONEPE CR / GPAY CREDIT / PAYTM CREDIT | Gross receipts | Digital receipt |
| BHIM UPI / BHIM CREDIT | Gross receipts | Digital receipt |
| NEFT/RTGS credits | Gross receipts | Electronic -- qualifies for 6% under 44AD |
| CHEQUE DEPOSIT / CHQ DEP | Gross receipts | Digital (account payee cheque) -- qualifies for 6% |
| CASH DEPOSIT / CASH / CDM | Gross receipts | CASH -- applies 8% under 44AD, not 6% |

### 3.4 TDS Deductions (Credits on Statement = Tax Credits)

| Pattern | Treatment | Notes |
|---|---|---|
| TDS BY [client name] / TDS DEDUCTED | Tax credit -- do NOT reduce income | Gross up income; claim TDS as credit on Form 26AS |
| 194J TDS / TDS 194J | Professional fee TDS at 10% | Client deducted TDS on professional fees |
| 194C TDS | Contractor TDS at 1%/2% | Contract payment TDS |

---

## Section 4 -- Worked Examples

### Example 1 -- UPI Payment from Client

**Input line (HDFC Bank statement):**
`15-Jun-2025 | UPI/CR/250615123456/ALPHA TECH SOLUTIONS | 85,000.00 CR | Bal 3,42,500.00`

**Reasoning:**
Credit via UPI from a business client. This is a professional fee receipt. Under Section 44ADA (professional), 50% of gross receipts = deemed profit. Under 44AD (business), 6% applies as UPI is digital/electronic. Confirm whether taxpayer is a specified professional. Receipt is electronic -- qualifies for the 6% rate if under 44AD.

**Classification:** Gross receipts Rs. 85,000. Add to annual total.

### Example 2 -- Razorpay Settlement

**Input line (ICICI Bank statement):**
`22-Aug-2025 | RAZORPAY SOFTWARE PVT LTD | 1,24,650.00 CR | Ref: RPY2025082211234`

**Reasoning:**
Razorpay collects payments on behalf of the seller, deducts their fee, and pays out net amount. The gross receipts (before Razorpay fees) are the taxable income. Razorpay fee of Rs. 350 (approx.) is a business expense. Gross receipts = Rs. 1,25,000; Razorpay fees = Rs. 350 deductible (ITR-3 filers). For presumptive filers (ITR-4), no itemisation -- deemed profit handles all expenses.

**Classification:** Gross receipts Rs. 1,25,000. Razorpay fee Rs. 350 is deductible for non-presumptive filers only.

### Example 3 -- LIC Premium Payment

**Input line (SBI Bank statement):**
`01-Apr-2025 | LIC PREMIUM/OTH/NEFT | 45,000.00 DR | Balance 2,85,000.00`

**Reasoning:**
Life insurance premium. This is NOT a business expense. Under the old regime, LIC premium qualifies for Section 80C deduction up to Rs. 1,50,000 combined limit. Under the new regime, 80C deductions are not available. Cannot be classified as a deductible business expense in either regime.

**Classification:** EXCLUDE from business expenses. Old regime: add to 80C pool (max Rs. 1,50,000 combined). New regime: no deduction.

### Example 4 -- TDS Deducted by Client

**Input line (Axis Bank statement):**
`10-Jul-2025 | NEFT CR/MNRVA CONSULTING/INV0042 LESS TDS | 90,000.00 CR`

**Reasoning:**
Client paid Rs. 90,000 after deducting 10% TDS on Rs. 1,00,000 invoice. The gross income is Rs. 1,00,000 (not Rs. 90,000). The TDS of Rs. 10,000 is a tax credit visible in Form 26AS. Report Rs. 1,00,000 as gross receipt and claim Rs. 10,000 TDS as credit.

**Classification:** Gross receipts Rs. 1,00,000. TDS credit Rs. 10,000 (verify in Form 26AS).

### Example 5 -- Cash Deposit

**Input line (Kotak Bank statement):**
`05-Sep-2025 | CASH DEPOSIT / CDM / BRANCH | 30,000.00 CR`

**Reasoning:**
Cash deposit. For 44AD taxpayers, cash receipts are taxed at 8% deemed profit (not the 6% digital rate). For 44ADA professionals, cash and digital are both 50% deemed -- no distinction. Cannot treat as digital receipt. Ask: was this cash collected from a client for a business service?

**Classification:** Gross receipts Rs. 30,000 (cash). For 44AD: counted toward 8% deemed profit pool (not 6%).

### Example 6 -- Advance Tax Challan Payment

**Input line (HDFC Bank statement):**
`14-Sep-2025 | INCOMETAX DEPT/ITNS 280/ADVANCE TAX | 25,000.00 DR`

**Reasoning:**
Advance tax payment to the Income Tax Department. This is NOT a business expense -- it is a prepayment of income tax liability. Record as advance tax paid (to be credited against final liability). Self-employed persons must pay advance tax in four instalments if annual liability exceeds Rs. 10,000.

**Classification:** EXCLUDE from income/expenses. Record: Advance tax paid Rs. 25,000 (15 September instalment).

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Presumptive Taxation -- Section 44ADA (Professionals)

**Legislation:** Section 44ADA, Income Tax Act, 1961

Applicable to specified professionals: legal, medical, engineering, architecture, accountancy, technical consultancy, interior decoration, and any other profession notified by CBDT.

- Gross receipts ≤ Rs. 75,00,000: eligible for presumptive scheme
- Deemed profit = 50% of gross receipts (taxpayer may declare higher)
- No need to maintain books of accounts
- File ITR-4 (Sugam)
- No deduction for actual expenses allowed -- 50% covers all

### 5.2 Presumptive Taxation -- Section 44AD (Business)

**Legislation:** Section 44AD, Income Tax Act, 1961

Applicable to any business (non-professional) with turnover ≤ Rs. 3,00,00,000.

- Deemed profit = 8% of gross turnover (cash receipts)
- Deemed profit = 6% of gross turnover (digital receipts: NEFT, RTGS, UPI, cheque, electronic transfer)
- Mixed receipts: apply 6%/8% pro-rata
- File ITR-4 (Sugam)

### 5.3 Tax Computation Flow (New Regime)

```
Gross receipts / turnover
- Presumptive expenses (44ADA: 50% of gross; 44AD: 92-94% of gross)
= Presumptive profit (Business Income)
+ Other income (interest, dividends, salary)
= Gross Total Income
- Standard deduction for salaried component (if any)
= Total Income
Apply rate table (Section 1)
= Income Tax
x 1.04 (add 4% cess)
= Total Tax Payable
- TDS credits (from Form 26AS)
- Advance tax paid
= Tax due / refund
```

### 5.4 Advance Tax Schedule

**Legislation:** Sections 207-219, Income Tax Act

| Instalment | Due Date | Cumulative % of Liability |
|---|---|---|
| 1st | 15 June | 15% |
| 2nd | 15 September | 45% |
| 3rd | 15 December | 75% |
| 4th (final) | 15 March | 100% |

Advance tax is required when estimated tax liability for the year exceeds Rs. 10,000. Shortfall attracts interest under Sections 234B and 234C.

### 5.5 Interest for Late Payment / Default

| Situation | Interest | Section |
|---|---|---|
| Advance tax not paid / shortfall | 1% per month on shortfall | 234C |
| Tax not paid by March 31 | 1% per month from April 1 | 234B |
| Late filing after July 31 | 1% per month on tax due | 234A |

### 5.6 Filing Deadlines

| Scenario | Deadline |
|---|---|
| Non-audit cases (most freelancers) | 31 July 2026 (for FY 2025-26) |
| Tax audit cases (Section 44AB) | 31 October 2026 |
| Belated return | 31 December 2026 (with interest) |
| Revised return | 31 December 2026 |

### 5.7 Non-Deductible Items (Both Regimes)

| Item | Reason |
|---|---|
| Income tax itself (advance tax, self-assessment tax) | Not deductible |
| LIC premiums, PPF, ELSS | Personal investments (80C in old regime only) |
| Mediclaim/health insurance | Section 80D (old regime only) |
| Personal drawings / withdrawals | Not a business expense |
| GST paid on sales | Indirect tax, not income tax deduction |
| Fines and penalties | Not incurred for business |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime Selection Optimisation

Old regime is better only when total deductions (80C + 80D + HRA + home loan interest + other) exceed the tax saving from wider new regime slabs. Flag for reviewer to compute both and compare. Typical breakeven: substantial 80C investments + home loan interest + HRA.

### 6.2 Mixed Professional and Business Income

If a taxpayer has both professional income (44ADA) and business income (44AD), each must be computed separately using its own presumptive rate. Combined income is then aggregated. Flag for reviewer.

### 6.3 Home Office Deduction (ITR-3 filers only)

Self-employed persons maintaining regular books (ITR-3) may claim proportionate rent, electricity, and internet for a home office. Acceptable apportionment: floor area ratio or dedicated usage hours. 44ADA/44AD presumptive filers cannot claim this separately -- covered by deemed profit.

### 6.4 PayPal / Foreign Client Receipts

Foreign receipts converted to INR at SBI TT buying rate on date of receipt (or RBI reference rate). If annual foreign receipts exceed Rs. 20,00,000, the taxpayer may have GST implications. Flag for reviewer.

### 6.5 Clubbing of Income (Spouse / Minor)

If income earned by a spouse or minor child is attributable to the taxpayer's assets or business, it may be clubbed with the taxpayer's income. Flag for reviewer if transfers to spouse or minor detected.

---

## Section 7 -- Excel Working Paper Template

```
INDIA INCOME TAX WORKING PAPER -- FY 2025-26
Taxpayer name: _______________  PAN: ___________
Filing form: ITR-4 (Presumptive) / ITR-3 (Regular) [circle one]
Regime: New / Old [circle one]

A. GROSS RECEIPTS / TURNOVER
  A1. Digital receipts (UPI, NEFT, RTGS, cheque)   ___________
  A2. Cash receipts                                  ___________
  A3. Total gross receipts (A1 + A2)                ___________

B. PRESUMPTIVE PROFIT (ITR-4 only)
  B1. 44ADA: A3 x 50%                               ___________
  B2. 44AD digital: A1 x 6%                         ___________
  B3. 44AD cash: A2 x 8%                            ___________
  B4. Presumptive profit (B1 or B2+B3)              ___________

C. OTHER INCOME
  C1. Interest income                                ___________
  C2. Dividend income                                ___________
  C3. Salary / pension                               ___________
  C4. Total other income                             ___________

D. GROSS TOTAL INCOME (B4 + C4)                     ___________

E. DEDUCTIONS (Old Regime only)
  E1. Section 80C (LIC, PPF, ELSS, tuition, etc.)  ___________
  E2. Section 80D (health insurance)                ___________
  E3. Section 80G (donations)                       ___________
  E4. Total deductions (max 80C: 1,50,000)          ___________

F. TOTAL INCOME (D - E)                              ___________

G. TAX COMPUTATION
  G1. Income tax (per rate table)                    ___________
  G2. Less: Section 87A rebate                       ___________
  G3. Surcharge (if applicable)                      ___________
  G4. Health & Education Cess (4% of G1+G3-G2)     ___________
  G5. Total tax payable                              ___________

H. TAX CREDITS
  H1. TDS (from Form 26AS)                          ___________
  H2. Advance tax paid                               ___________
  H3. Total credits                                  ___________

I. NET TAX DUE / REFUND (G5 - H3)                  ___________

REVIEWER FLAGS:
  [ ] Form 26AS verified against bank statement?
  [ ] Regime choice confirmed?
  [ ] Cash vs digital receipt split confirmed?
  [ ] TDS certificates received for all credits?
  [ ] Advance tax interest computed (234B/234C)?
```

---

## Section 8 -- Bank Statement Reading Guide

### Indian Bank Statement Formats

| Bank | Key Format | Key Fields |
|---|---|---|
| HDFC Bank | CSV / PDF | Date, Narration, Value Date, Debit, Credit, Closing Balance |
| ICICI Bank | CSV / Excel | S.No, Value Date, Transaction Date, Cheque/Ref No, Transaction Remarks, Withdrawal (Dr), Deposit (Cr), Balance |
| SBI | CSV / PDF | Txn Date, Value Date, Description, Ref No/Cheque No, Debit, Credit, Balance |
| Axis Bank | CSV | Tran Date, CHQNO, Particulars, Debit, Credit, Balance |
| Kotak Mahindra | XLS | Date, Description, Chq/Ref No, Debit(INR), Credit(INR), Bal(INR) |

### Key Narration Patterns

| Narration | Meaning | Tax Action |
|---|---|---|
| NEFT/CR/[ref]/[sender] | Electronic credit via NEFT | Business income |
| UPI/CR/[date]/[ref]/[sender] | UPI credit | Business income (digital) |
| CASH DEP / CDM | Cash deposit | Business income (cash) |
| TRF TO [own account] | Internal transfer | Exclude |
| IMPS/[ref]/[name] | IMPS credit | Business income (digital) |
| ATW/[ATM ref]/[branch] | ATM withdrawal | Investigate -- personal or business? |
| INT PD / INTEREST CREDIT | Bank interest | Other income |
| SALARY/SAL | Salary credit | Employment income |
| ADVNC TAX / ITNS 280 | Advance tax payment | Tax prepayment (credit) |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all UPI/NEFT/RTGS/cheque credits as potential gross receipts (digital)
2. Classify all CDM/cash deposits as potential gross receipts (cash)
3. Apply conservative defaults: new regime, professional (44ADA), 50% presumptive profit
4. Mark all salary credits and interest separately
5. Flag advance tax challans as prepaid tax credits
6. Generate working paper with clear PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- INDIA INCOME TAX
1. Are you a specified professional (doctor, CA, lawyer, architect, etc.) or a general business?
2. New or old tax regime? (Default: new)
3. Total gross receipts for FY 2025-26?
4. What % of receipts were received via UPI/NEFT/RTGS/cheque (vs cash)?
5. TDS deducted by clients -- do you have Form 26AS / AIS downloaded?
6. Advance tax paid -- any ITNS 280 challans this year?
7. Old regime only: any LIC, PPF, ELSS, health insurance, home loan repayments?
8. Is your PAN linked to your bank account?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Section |
|---|---|
| Presumptive taxation (professionals) | Section 44ADA |
| Presumptive taxation (business) | Section 44AD |
| New tax regime | Section 115BAC |
| Advance tax | Sections 207-219 |
| Interest for default | Sections 234A, 234B, 234C |
| TDS on professional fees | Section 194J |
| TDS on rent | Section 194I |
| Section 80C deductions | Section 80C |
| Health insurance deduction | Section 80D |

### ITR Form Guide

| Form | Who Uses It |
|---|---|
| ITR-4 (Sugam) | Presumptive income (44ADA/44AD), total income ≤ Rs. 50,00,000 |
| ITR-3 | Business/professional income NOT under presumptive scheme |
| ITR-1 (Sahaj) | Salaried individuals only, no business income |

### Known Gaps / Out of Scope

- Capital gains (Sections 111A, 112, 112A)
- NRI / RNOR taxation
- Partnership firms, companies, LLPs
- DTAA / double taxation relief
- Cryptocurrency taxation (VDA -- Section 115BBH)

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; transaction pattern library; local bank formats; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] New regime applied by default unless old regime confirmed?
- [ ] 4% cess applied after rebate?
- [ ] Surcharge checked for income > Rs. 50,00,000?
- [ ] Cash vs digital receipts split verified for 44AD?
- [ ] TDS credits verified against Form 26AS, not just bank statement?
- [ ] Advance tax interest computed if shortfall > Rs. 10,000?

---

## PROHIBITIONS

- NEVER apply old regime without explicit confirmation from client
- NEVER allow LIC/PPF/health insurance premiums as business expenses (they are 80C/80D items in old regime only)
- NEVER use net bank receipt as gross income when TDS was deducted -- always gross up
- NEVER allow income tax (advance tax, self-assessment tax) as a business deduction
- NEVER apply the 6% deemed profit rate to cash receipts under 44AD (8% applies)
- NEVER advise NRI clients using this skill -- escalate
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Chartered Accountant for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant or equivalent licensed practitioner in India) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
