---
name: ng-vat-return
description: >
  Use this skill whenever asked about Nigerian VAT returns for self-employed individuals or small businesses. Trigger on phrases like "Nigeria VAT", "FIRS VAT", "7.5% VAT", "VAT return Nigeria", "value added tax Nigeria", "TaxPro Max", or any question about VAT computation or filing for businesses in Nigeria. Covers the 7.5% standard rate, exempt supplies, registration threshold (NGN 25M), monthly filing to FIRS, and input/output VAT computation. ALWAYS read this skill before touching any Nigerian VAT work.
version: 2.0
jurisdiction: NG
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Nigeria VAT Return -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Nigeria (Federal Republic of Nigeria) |
| Tax | Value Added Tax (VAT) at 7.5% |
| Currency | NGN only |
| Primary legislation | Value Added Tax Act (VATA), Cap V1 LFN 2004, as amended by Finance Act 2020 |
| Supporting legislation | Finance Act 2021, 2023; FIRS Regulations |
| Tax authority | Federal Inland Revenue Service (FIRS) |
| Filing portal | TaxPro Max (taxpromax.firs.gov.ng) |
| Filing frequency | Monthly |
| Filing deadline | 21st of the following month |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Nigerian chartered accountant |
| Skill version | 2.0 |

### Rate Table

| Rate | Application |
|---|---|
| 7.5% | Standard rate on all taxable supplies (effective 1 February 2020) |
| 0% | Exports, diplomatic supplies, humanitarian goods |
| Exempt | Basic food, medical, educational, agricultural, financial services, residential rent, public transport |

### Key Thresholds

| Item | Amount |
|---|---|
| VAT registration exemption | Annual turnover NGN 25,000,000 or less (Finance Act 2020) |
| Filing frequency | Monthly for all registered persons |
| Nil returns | Required even with no transactions |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Supply classification unknown | Standard-rated at 7.5% |
| Input VAT claim without invoice | Not claimable |
| Mixed supply apportionment unknown | No input credit on disputed portion |
| Non-resident service VAT | Self-account at 7.5% |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the month in CSV, PDF, or pasted text, plus confirmation of VAT registration status and TIN.

**Recommended:** Sales invoices, purchase invoices with VAT shown, prior period returns.

**Ideal:** Complete invoice register, TIN certificate, WHT-VAT documentation (for government supplies).

### Refusal Catalogue

**R-NG-1 -- Below threshold.** "Businesses with annual turnover of NGN 25,000,000 or less are exempt from VAT registration and filing. Stop."

**R-NG-2 -- International VAT recovery.** "Cross-border VAT recovery and transfer pricing implications are outside this skill scope. Escalate."

**R-NG-3 -- Corporate tax.** "Companies Income Tax (CIT) is a separate obligation outside this skill scope."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| TRANSFER FROM [client] / INWARD TRF | Taxable supply | Output VAT at 7.5% | Standard client payment |
| POS SETTLEMENT / POS CREDIT | Taxable supply | Revenue | Point-of-sale terminal settlement |
| PAYSTACK PAYOUT / PAYSTACK SETTLEMENT | Taxable supply | Revenue | Paystack payment gateway |
| FLUTTERWAVE PAYOUT / RAVE SETTLEMENT | Taxable supply | Revenue | Flutterwave (Rave) settlement |
| OPAY SETTLEMENT / OPAY PAYOUT | Taxable supply | Revenue | OPay business payout |
| MONNIFY PAYOUT | Taxable supply | Revenue | Monnify settlement |
| INTERSWITCH / QUICKTELLER | Taxable supply | Revenue | Interswitch settlement |
| FGN / STATE GOVT / LGA PAYMENT | Taxable supply | Revenue with WHT-VAT | Government contract -- check withholding |
| INTEREST EARNED / INT CREDIT | Exempt | NOT taxable supply | Bank interest |
| LOAN DISBURSEMENT | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

| Pattern | Expense Category | Treatment | Notes |
|---|---|---|---|
| OFFICE RENT / COMMERCIAL LEASE | Rent | Input VAT claimable at 7.5% | Dedicated business premises |
| IKEJA ELECTRIC / EKEDC / AEDC / BEDC | Utilities | Input VAT claimable | Electricity distribution companies |
| MTN / GLO / AIRTEL / 9MOBILE | Communications | Business portion input VAT | Mixed use: apportion |
| UBER / BOLT / TAXI | Travel | Input VAT if business | Keep receipts |
| GOOGLE ADS / META / LINKEDIN | Advertising | Input VAT claimable | Digital advertising |
| FIRS TAX PAYMENT / FIRS VAT | EXCLUDE | Tax payment | Not deductible |
| SALARY / PAYROLL | EXCLUDE | Not subject to VAT | Employment cost |
| PERSONAL WITHDRAWAL / SELF TRANSFER | EXCLUDE | Drawings | Not business |

### 3.3 Exempt Supply Indicators

| Pattern | Treatment | Notes |
|---|---|---|
| RICE / BEANS / GARRI / YAMS / VEGETABLES | Exempt | Basic food items |
| PHARMACY / HOSPITAL / CLINIC | Exempt | Medical and pharmaceutical |
| SCHOOL FEES / UNIVERSITY / COLLEGE | Exempt | Educational |
| RESIDENTIAL RENT / HOUSE RENT | Exempt | Residential accommodation |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Monthly Return

**Input:** Taxable supplies NGN 5,000,000. Input VAT from purchases NGN 150,000.

**Reasoning:**
Output VAT: 5,000,000 x 7.5% = NGN 375,000. Input VAT: NGN 150,000 (with valid VAT invoices). VAT payable: 375,000 - 150,000 = NGN 225,000.

**Classification:** VAT payable NGN 225,000.

### Example 2 -- Exporter in Refund Position

**Input:** Zero-rated exports NGN 10,000,000. Input VAT NGN 300,000.

**Reasoning:**
Output VAT: NGN 0 (zero-rated). Input VAT: NGN 300,000. Excess input: carry forward or claim refund from FIRS.

**Classification:** Refund/carry forward NGN 300,000.

### Example 3 -- Mixed Supplies (Taxable and Exempt)

**Input:** Taxable supplies NGN 3,000,000, exempt supplies NGN 2,000,000. Total input VAT NGN 200,000 (none directly attributable).

**Reasoning:**
Taxable ratio: 3,000,000 / 5,000,000 = 60%. Claimable input: 200,000 x 60% = NGN 120,000. Output VAT: 3,000,000 x 7.5% = NGN 225,000. VAT payable: 225,000 - 120,000 = NGN 105,000.

**Classification:** VAT payable NGN 105,000. Flag for reviewer on apportionment.

### Example 4 -- Nil Return

**Input:** No supplies or purchases in the month.

**Reasoning:**
Nil return must still be filed by the 21st. VAT payable = NGN 0.

**Classification:** File nil return.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 VAT Return Computation

| Step | Action |
|---|---|
| 1 | Total standard-rated output supplies (exclusive of VAT) |
| 2 | Output VAT = Standard-rated supplies x 7.5% |
| 3 | Total exempt supplies (reported, no VAT) |
| 4 | Total zero-rated supplies (reported, 0% VAT) |
| 5 | Total input VAT on purchases (from valid VAT invoices) |
| 6 | Input VAT restriction: no credit for input on exempt supplies |
| 7 | Net VAT = Output VAT - Allowable input VAT |
| 8 | VAT payable to FIRS |

### 5.2 VAT Invoice Requirements (VATA s 10)

Must show: supplier name, TIN, description of goods/services, quantity, price exclusive of VAT, VAT amount, total, date, sequential number. Retention: 5 years minimum.

### 5.3 Filing and Payment

| Item | Detail |
|---|---|
| Filing frequency | Monthly |
| Filing deadline | 21st of the following month |
| Payment deadline | Same as filing deadline |
| Filing method | TaxPro Max |
| Nil returns | Must be filed even if no transactions |

### 5.4 Non-Resident Digital Services (VATA s 10A)

Non-resident suppliers of digital services to Nigerian consumers must register and charge VAT. If they do not, the Nigerian recipient may self-account.

### 5.5 Penalties (VATA s 16-18)

| Offence | Penalty |
|---|---|
| Failure to register | NGN 50,000 first month + NGN 25,000 per subsequent month |
| Late filing | 5% of tax due per month + NGN 50,000 |
| Late payment | 5% of amount due + interest at CBN MPR |
| Failure to issue VAT invoice | NGN 50,000 per offence |
| Failure to collect VAT | 150% of uncollected amount + 5% interest per annum |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed Taxable and Exempt Supplies

When a business makes both taxable and exempt supplies, input VAT must be apportioned. Directly attributable input follows its supply; residual input is apportioned by revenue ratio. Flag for reviewer.

### 6.2 Non-Resident Services

If a non-resident does not charge VAT, the Nigerian recipient may need to self-account. Flag for reviewer when client purchases services from non-residents.

### 6.3 Foreign Currency Invoicing

VAT must be computed in NGN. Use CBN exchange rate on the date of supply. Flag for reviewer on exchange rate source and date.

### 6.4 WHT-VAT on Government Contracts

Government entities may withhold VAT at source. Verify withholding documentation.

---

## Section 7 -- Working Paper Template

```
NIGERIA VAT WORKING PAPER
Taxpayer: _______________  TIN: ___________
Period: ___________  Month: ___________

A. OUTPUT (SALES)
  A1. Standard-rated supplies (excl. VAT)        ___________
  A2. Output VAT (A1 x 7.5%)                    ___________
  A3. Zero-rated supplies                        ___________
  A4. Exempt supplies                            ___________
  A5. Total supplies                             ___________

B. INPUT (PURCHASES)
  B1. Input VAT on taxable purchases             ___________
  B2. Less: input on exempt supplies             ___________
  B3. Net allowable input VAT                    ___________

C. NET VAT
  C1. VAT payable (A2 - B3)                     ___________
  C2. Or excess credit                           ___________

REVIEWER FLAGS:
  [ ] VAT registration confirmed?
  [ ] All input claims supported by valid VAT invoices?
  [ ] Mixed supply apportionment applied?
  [ ] Nil return filed if no activity?
  [ ] WHT-VAT from government contracts accounted for?
```

---

## Section 8 -- Bank Statement Reading Guide

### Nigerian Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| GTBank | CSV / PDF | Date, Description, Debit, Credit, Balance |
| First Bank | CSV | Transaction Date, Narration, Debit, Credit, Balance |
| Access Bank | CSV | Date, Description, Debit Amount, Credit Amount, Balance |
| UBA | CSV | Date, Narration, Debit, Credit, Balance |
| Zenith Bank | CSV | Date, Description, Debit, Credit, Balance |
| Fidelity Bank | CSV | Trans Date, Narration, Debit, Credit, Balance |

### Key Nigerian Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| NIP / NIBSS / INWARD TRF | Interbank transfer in | Potential income |
| POS / SETTLEMENT | POS terminal | Income or expense |
| USSD / MOBILE BANKING | Mobile transfer | Income or expense |
| FGN / MDAs | Government payment | Income with WHT-VAT |
| STAMP DUTY | Stamp duty charge | Exclude |
| VAT / FIRS | Tax payment | Exclude |
| SMS ALERT | Bank charge | Exempt (financial service) |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all NIP/NIBSS credits from non-personal sources as potential taxable supplies
2. Apply 7.5% output VAT to all unclassified business income
3. Only claim input VAT where description clearly indicates business purchase
4. Flag all government payments for WHT-VAT review
5. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- NIGERIA VAT
1. Are you registered for VAT with FIRS? What is your TIN?
2. What is your annual turnover (above or below NGN 25 million)?
3. What types of goods or services do you sell?
4. Do you make any exempt supplies (basic food, medical, education)?
5. Do you sell to government entities?
6. Do you import goods or services?
7. Do you have valid VAT invoices for all purchase claims?
8. Any excess credit carried forward from prior period?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| VAT imposition | VATA s 2 |
| Registration threshold | VATA s 8 (Finance Act 2020) |
| Exempt supplies | VATA First Schedule |
| VAT invoice | VATA s 10 |
| Non-resident digital services | VATA s 10A |
| Filing and payment | VATA s 15 |
| Penalties | VATA s 16-18 |

### Known Gaps / Out of Scope

- International VAT recovery
- Transfer pricing implications
- Companies Income Tax (CIT)
- Withholding tax on contracts (separate from VAT)

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Nigerian bank formats; local payment patterns (Paystack, Flutterwave, OPay); worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration and TIN confirmed?
- [ ] Turnover above NGN 25M threshold?
- [ ] All input claims supported by valid VAT invoices?
- [ ] Exempt supplies identified and excluded from output VAT?
- [ ] Nil return filed if no activity?
- [ ] Filing by 21st of following month?

---

## PROHIBITIONS

- NEVER charge VAT on exempt supplies (basic food, medical, education, residential rent)
- NEVER claim input VAT without a valid VAT invoice
- NEVER require VAT registration for businesses below NGN 25,000,000 annual turnover
- NEVER apply a VAT rate other than 7.5% (the pre-2020 rate of 5% is no longer applicable)
- NEVER miss the 21st monthly filing deadline -- nil returns are still required
- NEVER claim input VAT on purchases used for exempt supplies
- NEVER ignore self-accounting obligations on imported services from non-residents
- NEVER present calculations as definitive -- always label as estimated and direct client to ICAN/ANAN member

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant (FCA/ACA) or accredited tax practitioner in Nigeria) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
