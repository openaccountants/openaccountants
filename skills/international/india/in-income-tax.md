---
name: in-income-tax
description: >
  Use this skill whenever asked about Indian income tax for self-employed professionals, freelancers, or sole proprietors. Trigger on phrases like "how much tax do I pay in India", "ITR-4", "ITR-3", "Sugam", "Section 44ADA", "Section 44AD", "presumptive taxation", "new tax regime", "old tax regime", "advance tax India", "TDS credit", "PAN", "80C", "80D", "income tax return India", "surcharge", "health and education cess", or any question about filing or computing income tax for a self-employed individual in India. This skill covers new regime vs old regime rate tables, presumptive taxation (44ADA for professionals, 44AD for business), regular computation (ITR-3), surcharge, cess, standard deduction, Section 80C/80D deductions, advance tax schedule, TDS credits, PAN requirements, and ITR-4 (Sugam) structure. ALWAYS read this skill before touching any Indian income tax work.
version: 2.0
jurisdiction: IN
tax_year: 2025-26
category: international
depends_on:
  - income-tax-workflow-base
---

# India Income Tax — Self-Employed Skill v2.0

---

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Country | India (Republic of India) |
| Tax | Income Tax (Aaykar) |
| Currency | INR (Indian Rupee — ₹) |
| Tax year | Financial Year (FY) April 1 — March 31; Assessment Year (AY) = FY + 1 |
| Primary legislation | Income Tax Act 1961; Finance Act (annual) |
| Tax authority | Income Tax Department (ITD); CBDT |
| Filing portal | e-filing portal — https://www.incometax.gov.in |
| Filing deadline | 31 July (non-audit); 31 October (tax audit required); 31 March (belated) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a India-licensed Chartered Accountant (CA) |
| Skill version | 2.0 |

### New Tax Regime — Rate Brackets (FY 2025-26, default)

| Taxable Income (INR) | Rate |
|---|---|
| 0 — 4,00,000 | 0% |
| 4,00,001 — 8,00,000 | 5% |
| 8,00,001 — 12,00,000 | 10% |
| 12,00,001 — 16,00,000 | 15% |
| 16,00,001 — 20,00,000 | 20% |
| 20,00,001 — 24,00,000 | 25% |
| Above 24,00,000 | 30% |

**Rebate u/s 87A (new regime):** If total income ≤ ₹12,00,000: full tax rebate (effective zero tax). Rebate does not apply to special rate income (capital gains, etc.).

**Standard deduction (new regime, from AY 2025-26):** ₹75,000 for salaried/pension income. Not applicable to self-employment income directly.

### Old Tax Regime — Rate Brackets (opt-in)

| Taxable Income (INR) | Rate |
|---|---|
| 0 — 2,50,000 | 0% |
| 2,50,001 — 5,00,000 | 5% |
| 5,00,001 — 10,00,000 | 20% |
| Above 10,00,000 | 30% |

**Old regime allows:** Section 80C (up to ₹1,50,000), Section 80D (health insurance), HRA, LTA, home loan interest deduction, and other Chapter VI-A deductions. Self-employed typically compare regimes annually.

### Surcharge (on Income Tax — both regimes)

| Income Range | Surcharge Rate | New Regime Cap |
|---|---|---|
| Below ₹50,00,000 | Nil | — |
| ₹50,00,001 — ₹1,00,00,000 | 10% | — |
| ₹1,00,00,001 — ₹2,00,00,000 | 15% | — |
| ₹2,00,00,001 — ₹5,00,00,000 | 25% | 25% |
| Above ₹5,00,00,000 | 37% (old) | 25% |

**Health & Education Cess:** 4% on (Income Tax + Surcharge) — both regimes.

### Presumptive Taxation

| Scheme | Who | Threshold | Deemed Profit |
|---|---|---|---|
| Section 44ADA | Professionals (doctors, lawyers, CAs, architects, engineers, etc.) | Gross receipts ≤ ₹75,00,000 | 50% of gross receipts |
| Section 44AD | Business (not professionals) | Turnover ≤ ₹3,00,00,000 (if <5% cash) | 6% of digital receipts; 8% of cash |

**44ADA / 44AD:** No books of accounts required. File ITR-4 (Sugam). Cannot claim business expenses individually.

**Regular taxation (ITR-3):** Maintain books per Section 44AA. Claim actual business expenses. Tax audit (u/s 44AB) required if gross receipts > ₹75L (professionals) or turnover > ₹3Cr (business with <5% cash).

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown regime choice | New regime (default) |
| Unknown whether 44ADA applies | Assume yes if a listed profession and receipts ≤ ₹75L |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown TDS amount | 0 credit until Form 26AS / AIS confirms |
| Unknown expense category | Not deductible |
| Unknown filing status | Individual, not company or LLP |

### Red Flag Thresholds

| Threshold | Value |
|---|---|
| HIGH single credit (possible undisclosed income) | ₹10,00,000 |
| HIGH cash transactions | ₹2,00,000 (Section 269ST limit) |
| MEDIUM TDS mismatch vs 26AS | Any difference |
| MEDIUM advance tax shortfall | If estimated tax > ₹10,000 and not paid |
| Tax audit trigger | Gross receipts > ₹75L (44ADA) or Turnover > ₹3Cr (44AD) |

---

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — full-year bank statements (Apr 1 — Mar 31), Form 26AS (TDS statement) or Annual Information Statement (AIS), PAN number, confirmation of profession type (doctor, CA, engineer, IT consultant, etc.).

**Recommended** — all invoices issued to clients, Form 16A from all payers (TDS certificates), GST returns (if GST-registered), prior year ITR and Acknowledgement.

**Ideal** — complete books of accounts (for ITR-3 clients), asset register, home loan certificate, Section 80C investment proofs, health insurance premium receipts (80D), foreign income details.

**Soft warn:** No Form 26AS / AIS = cannot verify TDS credits. Proceed but flag all TDS entries as unconfirmed.

### Refusal Catalogue

**R-IN-1 — Companies, LLPs, Partnerships.** "This skill covers income tax for individuals only. Corporate tax (Sections 115BA/115BAA) and partnership returns are out of scope."

**R-IN-2 — NRI taxation.** "Non-resident Indian taxation involves DTAA analysis, different rate schedules, and TRC requirements. Escalate to a CA with NRI expertise."

**R-IN-3 — Capital gains (beyond basic).** "Equity/MF capital gains (Section 111A/112A), property gains, and complex LTCG/STCG require separate computation. Escalate."

**R-IN-4 — International income / DTAA.** "Cross-border income requires Double Taxation Avoidance Agreement analysis. Out of scope."

**R-IN-5 — Tax audit (Section 44AB).** "Clients requiring a tax audit need a CA-certified audit report (Form 3CB/3CD) before filing. Out of scope for this skill."

---

## Section 3 — Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| NEFT CR / RTGS CR [client name] | Business receipts (Gross Receipts) | Revenue — include in gross receipts | Under 44ADA: 50% deemed profit. Under ITR-3: add to income |
| IMPS CR [client name] | Gross Receipts | Revenue | Same as NEFT/RTGS |
| RAZORPAY / STRIPE / PAYPAL [payout] | Gross Receipts | Revenue — platform payout | Match to underlying invoices; may be net of platform fees |
| UPI CR [client name] | Gross Receipts | Revenue | UPI receipts count as digital — favours 6% rate under 44AD |
| TDS REFUND / IT REFUND | EXCLUDE | Not income | Tax refund — not business revenue |
| INT CR / INTEREST | Income from Other Sources | Not business income | Separate schedule in ITR |
| DIVIDEND / DIV CR | Income from Other Sources | Not business income | Dividend income — separate schedule |
| RENT RECEIVED | Income from House Property | Not business income | Separate schedule |
| SALARY / PAYROLL | Income from Salaries | Not self-employment income | Report under salary schedule |
| GSTIN REFUND | EXCLUDE | Not income | GST refund — not taxable |

### 3.2 Expense Patterns (Debits on Bank Statement) — ITR-3 Only

*Note: Under 44ADA or 44AD presumptive schemes, individual expenses are NOT separately deductible. Patterns below apply to ITR-3 (regular accounts) clients only.*

| Pattern | Tax Line | Tier | Treatment |
|---|---|---|---|
| OFFICE RENT / RENT [landlord] | Rent for premises | T1 | Fully deductible — business premises |
| HOME OFFICE [utility / landlord] | Office at home | T2 | Business portion only — % of home used for work |
| ELECTRICITY / BESCOM / TATA POWER / MSEDCL | Utilities | T2 | Business % only if home office; 100% if dedicated office |
| AIRTEL / JIO / BSNL / VI [mobile/internet] | Telephone/internet | T2 | Business % only — default 0% if mixed use |
| ZOMATO / SWIGGY / RESTAURANT | Business meals | T2 | Deductible only with business purpose documented; no flat rule |
| INDIGO / AIRINDIA / VISTARA / SPICEJET | Travel | T1 | Fully deductible if business travel — keep boarding pass |
| IRCTC / INDIAN RAILWAYS | Travel | T1 | Fully deductible if business |
| OLA / UBER / RAPIDO | Travel | T1 | Business trips — keep receipts |
| AMAZON [office supplies] / FLIPKART | Office supplies | T1 | Deductible if business purpose confirmed |
| SOFTWARE / SUBSCRIPTION [tech] | IT expenses | T1 | Deductible in year paid if revenue expense; capitalise if >3 years benefit |
| GOOGLE / MICROSOFT / ADOBE / ZOOM | IT/SaaS | T1 | Deductible — business software |
| PROFESSIONAL FEES / ADVOCATE / CA | Professional fees | T1 | Fully deductible |
| INSURANCE [professional indemnity] | Insurance | T1 | Professional indemnity: deductible |
| INSURANCE [health / life] | NOT a business expense | T1 | Health insurance: 80D deduction (max ₹25,000/₹50,000 senior); NOT business expense |
| BANK CHARGES / NEFT CHARGES | Bank charges | T1 | Fully deductible |
| GST PAYMENT TO GOVT | EXCLUDE from P&L | T1 | GST payments are not income tax deductible expenses |
| INCOME TAX / TDS / ADVANCE TAX | EXCLUDE | T1 | Income tax not deductible as business expense |
| LIC / PPFAC / ELSS | NOT business expense | T1 | Section 80C investment — deduction on personal return, not P&L |
| VEHICLE FUEL / PETROL / DIESEL | Vehicle expense | T2 | Business % only — logbook or reasonable estimate required |
| ATM CASH WITHDRAWAL | T2 — ask | T2 | Default exclude; ask what cash was used for |

### 3.3 TDS Credits

| Pattern | Treatment | Notes |
|---|---|---|
| TDS DEDUCTED BY [client] | Credit against tax liability | Verify in Form 26AS / AIS — must match |
| TDS u/s 194J (professional) | 10% TDS on professional fees | Most common for freelancers/consultants |
| TDS u/s 194C (contract) | 1% (individual) or 2% (firm) on contract payments | For project-based work |
| ADVANCE TAX PAID | Credit against tax liability | Verify challan reference |

### 3.4 Platform Payouts and Digital Receipts

| Pattern | Treatment | Notes |
|---|---|---|
| RAZORPAY SETTLEMENTS | Gross Receipts | Net of Razorpay fee — add back fee as expense |
| STRIPE [USD conversion] | Gross Receipts | Convert at RBI reference rate on receipt date |
| PAYPAL WITHDRAWAL | Gross Receipts | USD → INR conversion — FIFO or daily rate |
| UPWORK / FIVERR / TOPTAL | Gross Receipts | Platform earnings — net of platform fee |

### 3.5 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN ACCOUNT TRANSFER / SELF | EXCLUDE | Inter-account movement |
| LOAN CREDIT / BANK LOAN | EXCLUDE | Loan proceeds — not income |
| EMI / LOAN REPAYMENT | EXCLUDE (principal) | Principal repayment not deductible; interest on business loan: deductible |
| FD MATURITY | EXCLUDE (principal) | FD principal return not income; interest credited separately is income |

---

## Section 4 — Worked Examples

### Example 1 — 44ADA Professional (IT Consultant)

**Input line (HDFC Bank format):**
```
15/04/2025  NEFT-INFD12345678-ACME TECH SOLUTIONS-CONSULTING FEB25  CR  500,000.00  1,500,000.00
```

**Reasoning:**
NEFT credit from corporate client. Consulting income — IT consultant qualifies under Section 44ADA. Gross receipt: ₹5,00,000. Under 44ADA, deemed profit = 50% = ₹2,50,000. No further deductions available. File ITR-4 (Sugam).

**Classification:** Gross receipts ₹5,00,000 → Deemed profit ₹2,50,000 (44ADA).

---

### Example 2 — TDS Credit Reconciliation

**Input line (ICICI Bank format):**
```
30/04/2025  NEFT CR-TECHCORP LTD-INV 2025-001-LESS TDS 194J 50000  CR  450,000.00  2,250,000.00
```

**Reasoning:**
Client paid ₹4,50,000 (net of TDS u/s 194J). Gross invoice was ₹5,00,000. TDS deducted: ₹50,000 (10%). Gross receipt to include in return: ₹5,00,000. TDS credit ₹50,000 to claim in ITR against tax payable (verify in Form 26AS).

**Classification:** Gross receipt ₹5,00,000; TDS credit ₹50,000 (verify 26AS).

---

### Example 3 — Foreign Currency Receipt (Export Service)

**Input line (SBI format):**
```
2025-06-20  INWARD REMITTANCE  STRIPE PAYMENTS  USD 5000 @ 83.45  CR  4,17,250.00  8,17,250.00
```

**Reasoning:**
USD 5,000 export payment. Convert at RBI reference rate on receipt date (₹83.45 = ₹4,17,250). Gross receipt for income tax. If GST-registered: export is zero-rated; LUT required. For 44ADA: deemed 50% profit = ₹2,08,625. Foreign inward remittance ≤ USD 10,000 typically exempt from FEMA declaration.

**Classification:** Gross receipts ₹4,17,250; check FEMA/RBI requirements.

---

### Example 4 — Platform Fee (Razorpay)

**Input line (HDFC format):**
```
01/05/2025  RAZORPAY SETTLEMENTS  SETTLEMENT 2025-04  CR  196,020.00  3,196,020.00
```

**Reasoning:**
Razorpay settles net of fees. If gross collections = ₹2,00,000 and Razorpay fee = ₹3,980 (≈2%): gross receipts = ₹2,00,000; Razorpay fee = ₹3,980 (deductible under ITR-3; not separately deductible under 44ADA). Under 44ADA: include ₹2,00,000 in gross receipts.

**Classification:** Gross receipts ₹2,00,000; payment gateway fee ₹3,980 (ITR-3 only).

---

### Example 5 — Health Insurance Premium (Not a Business Expense)

**Input line (Axis Bank format):**
```
15/06/2025  SI-HDFC ERGO HEALTH INS-POL 12345678  DR  25,000.00  5,75,000.00
```

**Reasoning:**
Health insurance premium ₹25,000. This is NOT a business expense deductible on P&L. It qualifies as a Section 80D deduction (max ₹25,000 for self/spouse/children if under 60; ₹50,000 for senior citizen). Under old regime: claim as 80D. Under new regime: 80D not available.

**Classification:** EXCLUDE from business P&L. Record as 80D deduction (old regime only).

---

### Example 6 — Advance Tax Payment

**Input line (Kotak Bank format):**
```
14/09/2025  NSDL-INCOME TAX-ADVANCE TAX-CHALLAN 280  DR  1,50,000.00  4,50,000.00
```

**Reasoning:**
Advance tax instalment. Not a business expense — do NOT include in P&L. Record as advance tax paid (credit against final tax liability). September instalment should cover 45% of estimated annual tax liability. Check if adequate.

**Classification:** EXCLUDE from P&L. Record advance tax credit ₹1,50,000.

---

## Section 5 — Tier 1 Rules (Compressed)

### 5.1 Regime Choice

**New regime (default from AY 2024-25):** Lower rates, minimal deductions (only 80CCD(2) NPS employer contribution). Standard deduction ₹75,000 for salary/pension. No 80C, 80D, HRA, home loan interest deduction.

**Old regime (opt-in, deadline: ITR filing date):** Higher rates but full deductions: 80C (₹1.5L), 80D (₹25K-₹50K), HRA, home loan interest, LTA, professional tax, etc.

**Decision rule for self-employed:** Compare (new regime tax on gross receipts less 44ADA deemed expenses) vs (old regime tax after all deductions). New regime usually wins above ₹15L income; old regime wins if 80C/80D/home loan add up to >₹3L deductions.

### 5.2 Presumptive Taxation (44ADA / 44AD)

- 44ADA available to: doctors, lawyers, CAs, architects, engineers, management consultants, interior decorators, film artists, authorised representatives, and "other notified professions"
- IT consultants / software developers: Generally covered under "technical consultancy" — confirm with CA
- 44ADA threshold: Gross receipts ≤ ₹75,00,000 (FY 2025-26)
- Deemed profit: 50% — client cannot separately claim any expense
- Cannot opt out of 44ADA for 5 years after opting in

### 5.3 Advance Tax Schedule

| Instalment | Deadline | Cumulative % |
|---|---|---|
| 1st | 15 June | 15% |
| 2nd | 15 September | 45% |
| 3rd | 15 December | 75% |
| 4th | 15 March | 100% |

**44ADA / 44AD clients:** Entire advance tax in single instalment by 15 March.
**Threshold:** If estimated tax liability > ₹10,000, advance tax mandatory.
**Interest for shortfall:** Section 234B (shortfall at filing) and 234C (per-quarter shortfall).

### 5.4 TDS Framework

| Section | Payer | Rate | Common for |
|---|---|---|---|
| 194J | Any person (>₹30,000/year) | 10% | Professional services, consulting |
| 194C | Any person (>₹30,000/year) | 1% (individual) / 2% (others) | Contract work |
| 194H | Any person | 5% | Commission |
| 194A | Banks, financial institutions | 10% | Interest on FD if > ₹40,000/year |

Always verify TDS in Form 26AS / AIS before claiming credit.

### 5.5 Filing Deadlines and Penalties

| Event | Date |
|---|---|
| ITR-4 (non-audit) | 31 July AY |
| ITR-3 (non-audit) | 31 July AY |
| ITR-3 (tax audit required) | 31 October AY |
| Belated return | 31 December AY (with penalty) |
| Revised return | 31 December AY |

| Penalty | Amount |
|---|---|
| Late filing (Section 234F) | ₹5,000 (income > ₹5L); ₹1,000 (income ≤ ₹5L) |
| Interest on unpaid tax (234A) | 1% per month |
| Interest on advance tax shortfall (234B/C) | 1% per month |

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office

Deductible under ITR-3 as actual expense apportioned by floor area. Under 44ADA/44AD: no separate home office deduction (embedded in 50%/6%/8% deemed profit).

**Flag for reviewer:** Is client filing ITR-3 or ITR-4? If ITR-3: what % of home used exclusively for business? Obtain landlord name and monthly rent.

### 6.2 Vehicle Expenses

Under ITR-3: Deductible business % only. Methods:
- **Logbook method:** Actual cost × (business km ÷ total km)
- **Reasonable estimate:** Client provides business-use % — document the basis

Under 44ADA/44AD: No separate vehicle deduction.

**Flag for reviewer:** ITR-3 or ITR-4? If ITR-3: logbook or estimate? What % business use?

### 6.3 Phone / Internet

Under ITR-3: Business % deductible. Flat estimate (e.g., 50% business) accepted if reasonable. Under 44ADA/44AD: embedded in deemed profit.

**Flag for reviewer:** ITR-3 only. Confirm business-use % or apply 50% default with reviewer note.

### 6.4 Old vs New Regime Choice

Cannot be determined without all deduction amounts. Compare after computing both.

**Flag for reviewer:** Compute both regimes. Confirm client's deduction proofs (80C investments, health insurance, home loan certificate).

### 6.5 Foreign Currency Income

Convert at RBI reference rate on the date of receipt. Check FEMA compliance if remittances exceed prescribed limits. May require FIRC (Foreign Inward Remittance Certificate) from bank.

**Flag for reviewer:** Confirm receipt date and RBI rate. Get FIRC if required.

---

## Section 7 — Excel Working Paper Template

```
INDIA INCOME TAX — WORKING PAPER
Financial Year: 2025-26 (AY 2026-27)
Client: ___________  PAN: ___________  Profession: ___________

A. GROSS RECEIPTS
  A1. Indian clients (NEFT/RTGS/UPI)              ___________
  A2. Foreign remittances (at INR equivalent)      ___________
  A3. Platform payouts (Razorpay/Stripe/PayPal)    ___________
  A4. Total Gross Receipts (A1+A2+A3)              ___________

B. REGIME COMPARISON
  B1. NEW REGIME: Tax on (A4 - standard deduction)  ___________
  B2. OLD REGIME: A4 less actual expenses less 80C/80D etc. ___________
  B3. Chosen regime:  [ ] New  [ ] Old

C. PRESUMPTIVE (44ADA) — if applicable
  C1. Gross Receipts (must be ≤ ₹75,00,000)        ___________
  C2. Deemed Income (50% of C1)                    ___________
  C3. Tax on C2 (per chosen regime slabs)          ___________
  C4. Surcharge (if applicable)                    ___________
  C5. H&E Cess (4% of C3+C4)                       ___________
  C6. Less: TDS Credits (per 26AS)                 ___________
  C7. Less: Advance Tax Paid                       ___________
  C8. Net Tax Payable / (Refund)                   ___________

D. TDS RECONCILIATION
  D1. TDS per 26AS/AIS                             ___________
  D2. TDS per invoices                             ___________
  D3. Difference (flag if >0)                      ___________

REVIEWER FLAGS:
  [ ] Regime choice confirmed?
  [ ] 44ADA eligibility confirmed (profession type)?
  [ ] All TDS credits verified in 26AS/AIS?
  [ ] Advance tax adequate (avoid 234B/234C)?
  [ ] Foreign income FIRC obtained?
  [ ] T2 items resolved?
```

---

## Section 8 — Bank Statement Reading Guide

### Common Indian Bank Formats

| Bank | Date Format | Key Fields |
|---|---|---|
| HDFC Bank | DD/MM/YYYY | Date \| Narration \| Chq./Ref.No. \| Value Dt \| Withdrawal Amt \| Deposit Amt \| Closing Balance |
| ICICI Bank | DD/MM/YYYY | Transaction Date \| Value Date \| Reference No \| Description \| Debit \| Credit \| Balance |
| SBI | DD/MM/YYYY | Txn Date \| Value Date \| Description \| Ref No \| Debit \| Credit \| Balance |
| Axis Bank | DD-MM-YYYY | Date \| Transaction Details \| Chq No \| Debit \| Credit \| Balance |
| Kotak Mahindra | DD/MM/YYYY | Date \| Description \| Chq No \| Debit \| Credit \| Balance |

### Key Banking Terms

| Term | Classification Hint |
|---|---|
| NEFT CR / RTGS CR | Incoming wire — potential client payment |
| IMPS CR / UPI CR | Instant payment — client receipt |
| NEFT DR / RTGS DR | Outgoing wire — supplier payment |
| SI- / ECS DR | Standing instruction / auto-debit — subscription or EMI |
| ATM WDL / ATM DR | Cash withdrawal — ask purpose |
| INT CR | Interest income — other sources, not business |
| TDS | TDS deducted — cross-check with 26AS |
| RETURN / BOUNCE | Failed transaction — ignore |
| ADVANCE TAX / CHALLAN 280 | Tax payment — not an expense |

### Number Format

INR amounts use Indian numbering: ₹10,00,000 = ₹10 lakh = INR 1,000,000. Statements typically omit the ₹ symbol. Comma = thousands/lakh/crore separator; no decimal for whole rupees.

---

## Section 9 — Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all credits as Gross Receipts and all debits as potential expenses
2. Mark all T2 items "PENDING — reviewer must confirm"
3. Apply conservative defaults (new regime; 44ADA if profession type plausible)
4. Generate working paper with flags

**Onboarding questions:**
```
ONBOARDING QUESTIONS — INDIA INCOME TAX
1. What is your profession? (IT consultant, doctor, CA, lawyer, architect, etc.)
2. Are you filing under 44ADA (presumptive) or maintaining full books (ITR-3)?
3. New tax regime or old tax regime — any preference / prior-year choice?
4. Total gross receipts for FY 2025-26 (approximate)?
5. Have you paid advance tax? If yes, how much and when?
6. Any foreign clients / remittances from abroad?
7. Do you have any 80C investments (LIC, ELSS, PPF, etc.)?
8. Health insurance? Home loan? (Relevant only if old regime)
9. TDS deducted by clients — do you have Form 16A / Form 26AS access?
10. GST registered? If yes, gross receipts for GST and income tax may differ.
```

---

## Section 10 — Reference Material

| Topic | Reference |
|---|---|
| Income computation | Income Tax Act 1961, Sections 28-44 |
| Presumptive taxation | Section 44ADA, 44AD |
| Tax rates (new regime) | Finance Act 2025 — First Schedule |
| Advance tax | Section 208-219 |
| TDS | Chapter XVII-B (Sections 192-206AA) |
| Section 80C deductions | Chapter VI-A |
| Section 80D health insurance | Section 80D |
| Tax filing portal | https://www.incometax.gov.in |
| Form 26AS / AIS | e-filing portal — My Account |
| TDS rate chart | CBDT circular (annual) |

---

## PROHIBITIONS

- NEVER compute tax using simple multiplication on a single slab — Indian rates are progressive.
- NEVER allow health insurance premiums, LIC, PPF, or ELSS as business (P&L) deductions — they are 80C/80D personal deductions.
- NEVER allow income tax payments or GST payments as business expenses.
- NEVER apply 44ADA to businesses (retail, manufacturing) — only listed professions qualify.
- NEVER allow 44ADA deemed profit below 50% — the 50% floor is mandatory.
- NEVER skip TDS reconciliation with Form 26AS — mismatch causes demand notice.
- NEVER advise on regime choice without computing both regimes.
- NEVER present tax calculations as definitive — always label as estimated and direct client to their CA.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Chartered Accountant (CA) before filing. Tax laws in India change annually with each Finance Act — verify rates and thresholds for the applicable assessment year.
