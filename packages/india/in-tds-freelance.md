---
name: in-tds-freelance
description: >
  Use this skill whenever asked about Indian TDS (Tax Deducted at Source) on payments to freelancers, contractors, or professionals. Trigger on phrases like "TDS freelance India", "Section 194J", "Section 194C", "Section 194O", "TDS rate professional services", "Form 26Q", "Form 16A", "TDS certificate", "26AS", "AIS reconciliation", "TDS return India", "lower deduction certificate", "Section 197", "Section 206AA", "PAN not provided TDS", or any question about TDS obligations when paying or receiving freelance/contractor payments in India. Covers Section 194J (professional/technical services), 194C (contractor payments), 194O (e-commerce), TDS return filing (Form 26Q), TDS certificates (Form 16A), Form 26AS/AIS reconciliation, higher rate for missing PAN (Section 206AA), and lower deduction certificates (Section 197). ALWAYS read this skill before touching any India TDS work involving freelancers or contractors.
version: 1.0
jurisdiction: IN
tax_year: 2025-26
category: international
depends_on:
  - income-tax-workflow-base
---

# India TDS on Freelance & Contractor Payments Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | India |
| Jurisdiction Code | IN |
| Primary Legislation | Income Tax Act, 1961 -- Sections 194C, 194J, 194O, 197, 206AA |
| Supporting Legislation | Finance Act 2025; Income-tax Rules, 1962; CBDT Circulars and Notifications |
| Tax Authority | Central Board of Direct Taxes (CBDT) / Income Tax Department |
| Filing Portal | https://www.incometax.gov.in (TRACES for TDS: https://www.tdscpc.gov.in) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Chartered Accountant (India) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | FY 2025-26 (AY 2026-27) |
| Confidence Coverage | Tier 1: TDS rates per section, threshold amounts, Form 26Q due dates, Form 16A timelines, 206AA rates, PAN requirements. Tier 2: classification of payment as 194J vs 194C, mixed contracts, lower deduction certificate process. Tier 3: NRI payments (Section 195), transfer pricing, international services, DTAA treaty benefits. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Chartered Accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any TDS figure, you MUST know:

1. **Is the client the PAYER (deductor) or PAYEE (deductee)?** [T1] -- determines obligations (deduct & remit vs claim credit)
2. **Nature of payment** [T1] -- professional/technical service (194J), contract work (194C), or e-commerce (194O)
3. **PAN of the payee** [T1] -- if not provided, Section 206AA higher rate applies
4. **Legal status of payee** [T1] -- individual/HUF vs company/firm/AOP (affects 194C rate)
5. **Amount of payment** [T1] -- single payment and aggregate for the year (for threshold tests)
6. **Does the payee hold a lower deduction certificate (Section 197)?** [T2] -- reduces or eliminates TDS
7. **Is the payee a resident or non-resident?** [T1] -- non-resident payments fall under Section 195 (T3, out of scope)
8. **TAN (Tax Deduction Account Number) of the deductor** [T1] -- mandatory for TDS compliance

**If the payee is a non-resident, STOP. Section 195 applies, not 194C/194J. Escalate to [T3].**

---

## Step 1: Section 194J -- Professional / Technical Services [T1]

**Legislation:** Income Tax Act, 1961, Section 194J

| Item | Detail |
|------|--------|
| Applies to | Fees for professional services OR fees for technical services |
| TDS rate | 10% |
| Reduced rate | 2% for fees for technical services (NOT professional services) paid to a resident |
| Threshold | INR 30,000 per annum per payee |
| When to deduct | At the time of credit to payee's account OR at the time of payment, whichever is earlier |

### What Constitutes "Professional Services"

| Included | Excluded |
|----------|----------|
| Legal services | Salary payments (covered by Section 192) |
| Medical services | Goods purchases |
| Engineering services | Reimbursement of expenses (if separately billed and identifiable) |
| Architectural services | Payments to government bodies |
| Accountancy services | |
| Technical consultancy | |
| Interior decoration | |
| Advertising (certain) | |
| Sports commentary | |

### What Constitutes "Technical Services" (2% rate)

| Included |
|----------|
| Managerial services |
| Technical services |
| Consultancy services |
| Any service requiring technical expertise (call centre, data processing, etc.) |

**Key distinction:** Professional services (listed in Explanation to 194J) = 10%. Technical/managerial services (not in that list) = 2%. [T2] flag for CA if the classification is ambiguous.

### Threshold Rule

```
if aggregate_payment_to_payee_in_FY <= INR 30,000: no TDS
if aggregate_payment_to_payee_in_FY > INR 30,000: TDS on entire amount (not just excess)
```

**WARNING:** Once the INR 30,000 threshold is crossed, TDS applies to the FULL amount (including the first INR 30,000), not just the excess.

---

## Step 2: Section 194C -- Contractor Payments [T1]

**Legislation:** Income Tax Act, 1961, Section 194C

| Item | Detail |
|------|--------|
| Applies to | Payments to contractors/sub-contractors for carrying out any work (including supply of labour) |
| TDS rate (individual/HUF) | 1% |
| TDS rate (others: company, firm, AOP, etc.) | 2% |
| Single payment threshold | INR 30,000 |
| Aggregate annual threshold | INR 1,00,000 |
| When to deduct | At the time of credit or payment, whichever is earlier |

### What Constitutes "Work" Under 194C

| Included | Excluded |
|----------|----------|
| Contract for manufacturing/supply of a product per buyer's specification | Purchase of goods from a seller's stock (not a contract) |
| Catering | Professional services (covered by 194J) |
| Transport/freight | Payments to employees |
| Printing | Personal purchases |
| Construction | |
| Software development (if contract for work, not professional service) | |
| Housekeeping, security services | |

### Threshold Rules

```
if single_payment <= INR 30,000 AND aggregate_in_FY <= INR 1,00,000: no TDS
if single_payment > INR 30,000: TDS on that payment
if aggregate_in_FY > INR 1,00,000: TDS on all payments from the date threshold is crossed
```

### 194C vs 194J -- Decision Matrix [T2]

| Nature of Service | Section | Rate |
|-------------------|---------|------|
| Freelance software developer writing custom code | 194J (professional/technical) | 10% or 2% |
| IT company providing manpower on contract | 194C | 1% / 2% |
| Architect designing a building | 194J (professional) | 10% |
| Construction contractor building the design | 194C | 1% / 2% |
| Chartered Accountant preparing accounts | 194J (professional) | 10% |
| Data entry operator on contract | 194C | 1% / 2% |

**[T2] If the contract involves both professional services and execution work (e.g., architect who also supervises construction), flag for CA to determine dominant nature of the contract.**

---

## Step 3: Section 194O -- E-Commerce Operator Payments [T1]

**Legislation:** Income Tax Act, 1961, Section 194O

| Item | Detail |
|------|--------|
| Applies to | E-commerce operators facilitating sale of goods/services by e-commerce participants |
| TDS rate | 1% |
| Threshold | INR 5,00,000 per annum per participant (for individuals/HUFs only) |
| Who deducts | The e-commerce OPERATOR (platform), not the buyer |
| Effective from | 1 October 2020 |

### Key Points

- 194O applies to the PLATFORM (Swiggy, Zomato, Amazon, Flipkart, Urban Company, etc.)
- The freelancer/seller sees TDS deducted from their payouts
- If 194O applies, 194C/194J do NOT apply to the same transaction (194O takes precedence for e-commerce transactions)
- Individual/HUF participants with gross amount <= INR 5,00,000 are exempt (threshold added by Finance Act 2023)

---

## Step 4: Section 206AA -- Higher Rate for Missing PAN [T1]

**Legislation:** Income Tax Act, 1961, Section 206AA

If the payee does not provide a valid PAN to the deductor:

| Normal Rate | 206AA Rate |
|-------------|-----------|
| Any rate under Chapter XVII-B | Higher of: (a) the rate specified in the section, (b) the rate in force, or (c) **20%** |

### Practical Application

| Section | Normal Rate | Rate Without PAN |
|---------|-------------|-----------------|
| 194J (professional) | 10% | 20% |
| 194J (technical) | 2% | 20% |
| 194C (individual/HUF) | 1% | 20% |
| 194C (others) | 2% | 20% |
| 194O | 1% | 20% (but 5% if 206AB applies) |

**WARNING:** 20% is the MINIMUM rate when PAN is not provided. Always verify PAN before making any payment.

---

## Step 5: Section 206AB -- Higher Rate for Non-Filers [T1]

**Legislation:** Income Tax Act, 1961, Section 206AB

If the payee has NOT filed income tax returns for the two preceding years AND the aggregate TDS/TCS in each of those years exceeded INR 50,000:

| Rate | Detail |
|------|--------|
| Higher of | (a) twice the rate specified in the relevant section, OR (b) 5% |

### Verification

- Deductors can verify payee's filing status on the Income Tax portal's "Compliance Check for Section 206AB & 206CCA" utility
- If both 206AA (no PAN) and 206AB (non-filer) apply, the HIGHER rate applies

---

## Step 6: TDS Deposit (Remittance to Government) [T1]

**Legislation:** Rule 30 of Income-tax Rules, 1962

| Deductor Type | Due Date for Deposit |
|---------------|---------------------|
| Government deductors | Same day of deduction |
| Non-government deductors | 7th of the following month |
| March deductions | 30 April (extended deadline for March TDS) |

### Payment Method

- Challan No. ITNS 281 (available on TIN-NSDL or the Income Tax portal)
- Payment via net banking or authorised bank branch

---

## Step 7: TDS Return Filing -- Form 26Q [T1]

**Legislation:** Section 200(3); Rule 31A

Form 26Q is the quarterly TDS return for non-salary payments (including 194C, 194J, 194O).

| Quarter | Period | Filing Due Date |
|---------|--------|----------------|
| Q1 | 1 April -- 30 June | 31 July |
| Q2 | 1 July -- 30 September | 31 October |
| Q3 | 1 October -- 31 December | 31 January |
| Q4 | 1 January -- 31 March | 31 May |

### Filing Requirements

| Item | Detail |
|------|--------|
| Who must file | Any person who has deducted TDS under Chapter XVII-B |
| How | Online via TRACES (tdscpc.gov.in) using DSC or EVC |
| Software | Return Preparation Utility (RPU) from TRACES, or commercial TDS software |
| Nil return | NOT mandatory but recommended to avoid default notices |
| Corrections | Correction returns (C1/C2/C3/C4/C5) can be filed via TRACES |

### Late Filing Penalty

| Penalty | Amount |
|---------|--------|
| Section 234E | INR 200 per day of delay (maximum = total TDS deductible) |
| Section 271H | INR 10,000 to INR 1,00,000 (at AO's discretion for delay > 1 year or incorrect information) |

---

## Step 8: TDS Certificates -- Form 16A [T1]

**Legislation:** Section 203; Rule 31

| Item | Detail |
|------|--------|
| Form | Form 16A (certificate for non-salary TDS) |
| Issued by | Deductor to deductee |
| Frequency | Quarterly (one per quarter of deduction) |
| Due date | Within 15 days from the due date of filing Form 26Q |
| Generation | Download from TRACES after filing Form 26Q (auto-generated with digital signature) |

### Form 16A Due Dates

| Quarter | 26Q Due | 16A Due |
|---------|---------|---------|
| Q1 (Apr-Jun) | 31 July | 15 August |
| Q2 (Jul-Sep) | 31 October | 15 November |
| Q3 (Oct-Dec) | 31 January | 15 February |
| Q4 (Jan-Mar) | 31 May | 15 June |

---

## Step 9: Form 26AS and AIS Reconciliation [T1]

**Legislation:** Section 203AA; Rule 31AB

| Form | Purpose |
|------|---------|
| Form 26AS | Annual Tax Statement -- shows all TDS/TCS credited against the taxpayer's PAN |
| AIS (Annual Information Statement) | Extended version showing financial transactions (SFT data, interest, dividends, purchases, etc.) |
| TIS (Taxpayer Information Summary) | Aggregated and categorised summary of AIS data |

### Reconciliation Steps (for Payee/Deductee)

1. Download Form 26AS from TRACES or the Income Tax portal
2. Download AIS from the Income Tax portal
3. Match TDS credits in 26AS against TDS deducted by each deductor
4. Verify amounts match invoices raised and payments received
5. If mismatch: contact the deductor to correct Form 26Q or file a correction return
6. Claim TDS credit in ITR only for amounts reflected in Form 26AS

**WARNING:** TDS credit is allowed ONLY if reflected in Form 26AS. If the deductor has deducted TDS but not deposited or filed 26Q, the DEDUCTEE cannot claim credit. The deductee should pursue the deductor.

---

## Step 10: Lower Deduction Certificate -- Section 197 [T2]

**Legislation:** Income Tax Act, 1961, Section 197

If the payee's total income is below the taxable threshold or the effective tax rate is lower than TDS rates:

| Item | Detail |
|------|--------|
| Application | Form 13 filed online on the Income Tax portal |
| Issued by | Assessing Officer (AO) |
| Certificate specifies | NIL rate or a reduced rate |
| Validity | Typically for one financial year |
| Deductor obligation | Must apply the rate specified in the certificate (not the statutory rate) |

### When to Recommend

| Scenario | Action |
|----------|--------|
| Freelancer with income below basic exemption limit | Recommend applying for NIL certificate |
| Professional with high expenses and low taxable income | Recommend applying for reduced rate certificate |
| Multiple deductors deducting at full rate causing cash flow issues | Recommend lower deduction certificate |

**[T2] Always flag for CA before advising on Section 197. The application requires projected income computation and supporting documentation.**

---

## Step 11: Edge Case Registry

### EC1 -- Payment is mix of goods and services [T2]
**Situation:** Invoice includes INR 2,00,000 for software development (service) and INR 50,000 for hardware (goods purchase).
**Resolution:** If amounts are separately identifiable in the invoice, TDS applies only to the service component (194J on INR 2,00,000). If not separately stated, TDS on the entire amount. [T2] flag for CA.

### EC2 -- Reimbursement of expenses included in invoice [T2]
**Situation:** Freelancer invoices INR 1,00,000 for consulting + INR 20,000 for travel reimbursement.
**Resolution:** If reimbursement is separately billed and supported by actual receipts, TDS may not apply to the reimbursement component (per CBDT Circular 715/1995 and subsequent judicial decisions). However, this is frequently disputed. [T2] flag for CA.

### EC3 -- Payee is a partnership firm -- which rate? [T1]
**Situation:** Payment under 194C to a partnership firm.
**Resolution:** Partnership firm is NOT an individual/HUF. Rate = 2% (not 1%).

### EC4 -- Aggregate threshold crossed mid-year (194C) [T1]
**Situation:** Four payments of INR 28,000 each to the same contractor. Total = INR 1,12,000. No single payment exceeded INR 30,000.
**Resolution:** Aggregate exceeded INR 1,00,000. TDS should have been deducted from the 4th payment onward (when the aggregate crossed INR 1,00,000). If not deducted on earlier payments, the deductor is treated as an assessee in default. Deduct TDS on subsequent payments and consider depositing shortfall with interest.

### EC5 -- Freelancer on e-commerce platform (194O vs 194J) [T2]
**Situation:** Graphic designer sells services via an e-commerce platform like Fiverr or Urban Company.
**Resolution:** 194O applies (1% TDS by the e-commerce operator). The hiring client does NOT additionally deduct 194J. 194O takes precedence for transactions facilitated through the platform. If the client hires the freelancer directly (off-platform), 194J applies.

### EC6 -- TDS deducted but not deposited by deductor [T1]
**Situation:** Deductor deducted TDS of INR 50,000 from the freelancer's payment but has not deposited to the government. 26AS shows no credit.
**Resolution:** The DEDUCTEE cannot claim credit until it appears in 26AS. The deductee should: (1) demand Form 16A from the deductor, (2) report to the Income Tax Department if deductor refuses, (3) file ITR without the credit and claim it via rectification once 26AS is updated.

### EC7 -- Section 194J threshold: multiple professional services [T1]
**Situation:** Client pays a freelancer INR 15,000 for accounting and INR 20,000 for tax advisory in the same FY. Total = INR 35,000.
**Resolution:** Aggregate exceeds INR 30,000. TDS applies to the entire INR 35,000 (not just the excess). The deductor should have started deducting from the payment that pushed the aggregate over INR 30,000.

### EC8 -- GST component in the invoice and TDS [T1]
**Situation:** Invoice: Base fee INR 1,00,000 + GST 18% = INR 18,000. Total invoice INR 1,18,000.
**Resolution:** Per CBDT Circular 23/2017, TDS is to be deducted on the base amount EXCLUDING GST, provided GST is separately shown in the invoice. TDS = 10% of INR 1,00,000 = INR 10,000 (not INR 11,800).

### EC9 -- Presumptive taxation payee and TDS credit [T1]
**Situation:** Freelancer files under Section 44ADA (presumptive). Has TDS of INR 80,000 deducted. Presumptive tax liability = INR 50,000.
**Resolution:** TDS credit (INR 80,000) exceeds tax liability (INR 50,000). Excess INR 30,000 is refundable via ITR filing. The freelancer MUST file ITR to claim the refund.

### EC10 -- Section 194R -- benefits or perquisites in kind [T2]
**Situation:** Company provides a freelancer with a laptop worth INR 50,000 as part of the engagement.
**Resolution:** Section 194R (introduced in 2022) requires TDS at 10% on benefits/perquisites exceeding INR 20,000 provided to resident contractors/professionals. TDS = 10% x INR 50,000 = INR 5,000. The deductor may provide cash to cover the TDS. [T2] flag for CA.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Chartered Accountant must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Chartered Accountant. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard 194J deduction
**Input:** Payment of INR 1,50,000 to a freelance chartered accountant for audit services. PAN provided.
**Expected output:** Section 194J applies. TDS = 10% x INR 1,50,000 = INR 15,000. Deposit by 7th of the following month.

### Test 2 -- 194C to individual contractor
**Input:** Single payment of INR 45,000 to an individual contractor for office renovation. PAN provided.
**Expected output:** Section 194C. Single payment exceeds INR 30,000 threshold. TDS = 1% x INR 45,000 = INR 450.

### Test 3 -- No TDS below threshold (194J)
**Input:** Two payments of INR 12,000 each to a freelance designer in the same FY. Total = INR 24,000. PAN provided.
**Expected output:** Aggregate INR 24,000 < INR 30,000 threshold. No TDS required.

### Test 4 -- Missing PAN (Section 206AA)
**Input:** Payment of INR 60,000 for professional services. Payee has NOT provided PAN.
**Expected output:** Section 206AA applies. TDS = 20% x INR 60,000 = INR 12,000 (instead of normal 10% = INR 6,000).

### Test 5 -- GST excluded from TDS base
**Input:** Invoice: Professional fees INR 2,00,000 + GST 18% = INR 36,000. Total = INR 2,36,000. GST shown separately. PAN provided.
**Expected output:** TDS on base amount only. TDS = 10% x INR 2,00,000 = INR 20,000.

### Test 6 -- 194C aggregate threshold crossed
**Input:** Q1: INR 25,000. Q2: INR 25,000. Q3: INR 25,000. Q4: INR 30,000. All to same individual contractor. PAN provided.
**Expected output:** No single payment > INR 30,000. But aggregate = INR 1,05,000 > INR 1,00,000. TDS obligation arose when aggregate crossed INR 1,00,000 (during Q4 payment). TDS = 1% on the Q4 payment = INR 300. Future payments also subject to TDS.

### Test 7 -- Form 26Q filing timeline
**Input:** TDS deducted in July, August, September (Q2).
**Expected output:** Form 26Q for Q2 due by 31 October. Form 16A due by 15 November.

---

## PROHIBITIONS

- NEVER apply Section 194J/194C to payments to non-residents -- Section 195 applies (out of scope, T3)
- NEVER deduct TDS below the applicable threshold -- verify both single-payment and aggregate thresholds
- NEVER ignore Section 206AA -- always verify PAN before applying the standard rate
- NEVER include GST in the TDS base when GST is separately stated in the invoice
- NEVER issue Form 16A without first filing Form 26Q for the relevant quarter
- NEVER advise a deductee to claim TDS credit not reflected in Form 26AS
- NEVER apply 194C rates (1%/2%) to professional services that fall under 194J
- NEVER assume e-commerce payments are exempt -- verify 194O applicability
- NEVER estimate Section 197 lower deduction certificate outcomes without CA review
- NEVER ignore late filing penalties under Section 234E -- INR 200/day accrues quickly

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
