---
name: za-vat-return
description: >
  Use this skill whenever asked about South African VAT returns for self-employed individuals or small businesses. Trigger on phrases like "South Africa VAT", "VAT201", "SARS VAT", "15% VAT", "eFiling VAT", "zero-rated SA", "VAT vendor", or any question about VAT filing, computation, or registration for vendors in South Africa. Covers the 15% standard rate, zero-rated and exempt supplies, R1M registration threshold, VAT201 return, and bimonthly filing via SARS eFiling. ALWAYS read this skill before touching any South African VAT work.
version: 2.0
jurisdiction: ZA
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# South Africa VAT Return (VAT201) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | South Africa |
| Tax | Value-Added Tax (VAT) at 15% |
| Currency | ZAR only |
| Primary legislation | Value-Added Tax Act 89 of 1991 (VAT Act) |
| Supporting legislation | Tax Administration Act 28 of 2011 (TAA); SARS interpretation notes |
| Tax authority | South African Revenue Service (SARS) |
| Filing portal | SARS eFiling (efiling.sars.gov.za) |
| Default filing frequency | Bimonthly (Category A) |
| Filing deadline | Last business day of month following period end (eFiling) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a South African registered tax practitioner |
| Skill version | 2.0 |

### Rate Table

| Rate | Application |
|---|---|
| 15% | Standard rate (effective 1 April 2018) |
| 0% | Exports, basic foodstuffs, petrol/diesel, international transport, agricultural inputs |
| Exempt | Financial services, residential rental, public transport, educational services, childcare |

### Tax Fraction

For VAT-inclusive amounts at 15%: **15/115**.

### Key Thresholds

| Item | Amount (ZAR) |
|---|---|
| Compulsory registration | R1,000,000 taxable supplies in any 12-month period |
| Voluntary registration | R50,000 taxable supplies in any 12-month period |
| Payments basis eligibility | Taxable supplies < R2,500,000 |
| Full tax invoice threshold | R5,000 |
| No invoice required | Supplies under R50 |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Registration status unknown | STOP -- do not compute |
| Accounting basis unknown | Invoice basis (default) |
| Supply classification unknown | Standard-rated at 15% |
| Private use proportion unknown | 0% recovery |
| Second-hand goods claim | Not claimable until documentation confirmed |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the VAT period in CSV, PDF, or pasted text, plus confirmation of VAT registration status and vendor number.

**Recommended:** Sales invoices, purchase invoices with VAT shown, prior period VAT201.

**Ideal:** Complete invoice register, filing category confirmation, prior year VAT reconciliation.

### Refusal Catalogue

**R-ZA-1 -- Below threshold.** "If taxable supplies have not exceeded R1,000,000 in any 12-month period and client is not voluntarily registered, no VAT obligations. Stop."

**R-ZA-2 -- Cross-border services (complex).** "Complex cross-border service transactions and customs VAT require specialist review. Escalate."

**R-ZA-3 -- VAT grouping.** "VAT group registrations are outside this skill scope. Escalate."

**R-ZA-4 -- Large-value complex transactions.** "Transactions involving property, construction, or financial instruments require specialist review. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| EFT FROM [client] / EFT CREDIT | Taxable supply | Output VAT at 15% | Standard electronic transfer |
| INSTANT MONEY / CASH DEPOSIT | Taxable supply | Revenue | Cash receipt |
| PAYFAST PAYOUT / PAYFAST SETTLEMENT | Taxable supply | Revenue | PayFast payment gateway |
| YOCO SETTLEMENT / YOCO PAYOUT | Taxable supply | Revenue | Yoco card machine settlement |
| SNAPSCAN PAYOUT | Taxable supply | Revenue | SnapScan mobile payment |
| ZAPPER SETTLEMENT | Taxable supply | Revenue | Zapper payment |
| CAPITEC / FNB / ABSA / NEDBANK / STD BANK CREDIT | Taxable supply | Revenue | Bank transfer income |
| INTEREST / INT EARNED | Exempt | NOT taxable | Bank interest -- financial service |
| SARS REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

| Pattern | Expense Category | Treatment | Notes |
|---|---|---|---|
| OFFICE RENT / COMMERCIAL LEASE | Rent | Input VAT claimable | Business premises |
| ESKOM / CITY POWER / CITY OF CAPE TOWN | Utilities | Input VAT claimable | Electricity |
| TELKOM / VODACOM / MTN / CELL C / RAIN | Communications | Business portion claimable | Mixed use: apportion |
| ENGEN / SHELL / CALTEX / SASOL | Fuel | Input VAT claimable | Business use only |
| TAKEALOT / MAKRO / GAME | Office supplies | Input VAT claimable | Business purchases |
| GOOGLE ADS / META / LINKEDIN | Advertising | Input VAT claimable | Digital advertising |
| UBER SA / BOLT SA / TAXI | Travel | Input VAT if business | Keep receipts |
| SARS INCOME TAX / SARS PAYE | EXCLUDE | Tax payment | Not deductible |
| SARS VAT PAYMENT | EXCLUDE | VAT payment | Not input tax |
| BANK CHARGES / FNB FEE / ABSA FEE | Exempt | No input VAT | Financial service exempt |
| OWN TRANSFER / PERSONAL | EXCLUDE | Drawings | Not business |

### 3.3 Zero-Rated Supply Indicators

| Pattern | Treatment | Notes |
|---|---|---|
| EXPORT / INTERNATIONAL SHIPMENT | Zero-rated output | Goods exported from SA |
| BROWN BREAD / MAIZE MEAL / RICE / EGGS / MILK | Zero-rated | Basic foodstuffs |
| FUEL LEVY / PETROL / DIESEL | Zero-rated | Fuel levy applies instead |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Bimonthly Return

**Input:** Standard-rated supplies R500,000. Purchases R200,000 (all standard-rated, valid invoices).

**Reasoning:**
Output VAT: R500,000 x 15% = R75,000. Input VAT: R200,000 x 15% = R30,000. VAT payable: R75,000 - R30,000 = R45,000.

**Classification:** VAT payable R45,000.

### Example 2 -- Exporter in Refund Position

**Input:** Zero-rated exports R800,000. Purchases R300,000 (standard-rated).

**Reasoning:**
Output VAT: R0. Input VAT: R300,000 x 15% = R45,000. Refund: R45,000.

**Classification:** VAT refund R45,000.

### Example 3 -- Second-Hand Goods Purchase

**Input:** Vendor buys used equipment from non-vendor for R50,000 (no VAT charged).

**Reasoning:**
Notional input tax: R50,000 x 15/115 = R6,521.74. Claimable if documentation requirements are met (declaration from seller, proof of payment).

**Classification:** Input tax R6,521.74. Flag for reviewer on documentation.

### Example 4 -- Bad Debt Relief

**Input:** Invoice for R23,000 (incl. VAT) written off after 14 months.

**Reasoning:**
Bad debt relief under s 22(1): debt outstanding over 12 months and written off. Relief: R23,000 x 15/115 = R3,000.

**Classification:** Input tax deduction R3,000.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 VAT201 Return Fields

| Field | Description |
|---|---|
| 1 / 1A | Standard-rated supplies / VAT thereon |
| 2 | Zero-rated supplies |
| 3 | Exempt supplies |
| 4 | Total supplies (1 + 2 + 3) |
| 5 / 5A | Capital goods purchased / VAT thereon |
| 6 / 6A | Other purchases / VAT thereon |
| 7 | Total input tax (5A + 6A + adjustments) |
| 8 | Output less input (1A - 7) |
| 9 | VAT payable / refundable |

### 5.2 Filing Categories

| Category | Frequency | Who |
|---|---|---|
| A | Bimonthly | Default for most vendors |
| B | Monthly | Taxable supplies > R30M/year |
| C | Six-monthly | Farming enterprises (by approval) |
| D | Annual | Small vendors (by approval) |

### 5.3 Filing Deadlines

| Method | Deadline |
|---|---|
| eFiling | Last business day of month following period end |
| Manual (branch) | 25th of month following period end |

### 5.4 Payments Basis (s 15)

Eligibility: taxable supplies < R2,500,000. Account for VAT when payment is made or received. Must apply to SARS.

### 5.5 Penalties (TAA Chapter 15)

| Offence | Penalty |
|---|---|
| Late filing | Fixed amount penalty (escalating scale) |
| Late payment | 10% of amount outstanding |
| Interest | Prescribed rate compounding monthly |
| Understatement | 10-200% depending on behaviour |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed Supplies Apportionment

Input tax must be apportioned when making both taxable and exempt supplies. Directly attributable input follows its supply. Residual input apportioned using revenue-based ratio. Flag for reviewer.

### 6.2 Imported Services (Reverse Charge, s 7(1)(c))

If foreign supplier is not VAT-registered in SA and service is consumed in SA, recipient must account for VAT. May claim corresponding input tax if for taxable supplies.

### 6.3 Second-Hand Goods Input Tax (s 16(3)(a)(ii))

Notional input tax: tax fraction (15/115) of consideration paid. Requires declaration from seller and proof of payment. Cannot exceed lesser of consideration paid or open market value. Flag for reviewer.

### 6.4 Change from Payments to Invoice Basis

When turnover exceeds R2,500,000. Transitional adjustments required. Flag for tax practitioner.

---

## Section 7 -- Working Paper Template

```
SOUTH AFRICA VAT WORKING PAPER (VAT201)
Vendor: _______________  VAT Number: ___________
Period: ___________  Category: A / B / C / D
Basis: Invoice / Payments

A. OUTPUT (SALES)
  A1. Standard-rated supplies (excl. VAT)        ___________
  A2. Output VAT (A1 x 15%)                     ___________
  A3. Zero-rated supplies                        ___________
  A4. Exempt supplies                            ___________

B. INPUT (PURCHASES)
  B1. Capital goods VAT                          ___________
  B2. Other purchases VAT                        ___________
  B3. Adjustments                                ___________
  B4. Total input VAT                            ___________

C. NET VAT
  C1. Output less input (A2 - B4)                ___________
  C2. VAT payable / refundable                   ___________

REVIEWER FLAGS:
  [ ] Registration and vendor number confirmed?
  [ ] Filing category confirmed?
  [ ] Accounting basis confirmed?
  [ ] Tax invoices held for all input claims?
  [ ] Second-hand goods documentation complete?
  [ ] Zero-rated vs exempt correctly distinguished?
```

---

## Section 8 -- Bank Statement Reading Guide

### South African Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| FNB | CSV / PDF | Date, Description, Amount, Balance |
| ABSA | CSV | Date, Description, Debit, Credit, Balance |
| Standard Bank | CSV | Date, Description, Debit, Credit, Balance |
| Nedbank | CSV | Date, Description, Debit, Credit, Balance |
| Capitec | CSV | Date, Description, Debit, Credit, Balance |
| Investec | CSV | Date, Description, Debit, Credit, Balance |

### Key SA Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| EFT CREDIT / INWARD PAYMENT | Bank transfer in | Potential income |
| DEBIT ORDER / DEBI CHECK | Direct debit | Regular expense |
| POS / CARD PURCHASE | Point of sale | Expense |
| CASH DEPOSIT | Cash received | Income |
| SARS / RECEIVER OF REVENUE | Tax payment or refund | Exclude |
| BANK CHARGES / SERVICE FEE | Bank fee | Exempt -- no VAT |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all EFT credits from business sources as potential taxable supplies
2. Apply conservative defaults: invoice basis, standard-rated, 0% private recovery
3. Only claim input VAT where VAT is clearly evident
4. Flag all large purchases for capital goods review

Present these questions:

```
ONBOARDING QUESTIONS -- SOUTH AFRICA VAT
1. Are you registered as a VAT vendor? What is your VAT number?
2. What filing category are you (A bimonthly, B monthly, C six-monthly, D annual)?
3. Are you on invoice basis or payments basis?
4. What types of goods or services do you sell?
5. Do you make any zero-rated supplies (exports, basic foodstuffs)?
6. Do you make any exempt supplies (financial, residential rent, education)?
7. Do you purchase second-hand goods from non-vendors?
8. Do you import services from non-resident suppliers?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Section |
|---|---|
| Imposition of VAT | VAT Act s 7 |
| Zero-rated supplies | VAT Act s 11 |
| Exempt supplies | VAT Act s 12 |
| Registration | VAT Act s 23 |
| Payments basis | VAT Act s 15 |
| Input tax | VAT Act s 16 |
| Tax invoices | VAT Act s 20 |
| Bad debts | VAT Act s 22 |
| Filing | VAT Act s 27, 28 |

### Known Gaps / Out of Scope

- Cross-border services (complex)
- Customs VAT on imports
- VAT grouping
- Large-value property transactions

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; SA bank formats; local payment patterns (PayFast, Yoco, SnapScan); worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration and vendor number confirmed?
- [ ] Filing category and accounting basis confirmed?
- [ ] Tax fraction 15/115 used consistently?
- [ ] Zero-rated vs exempt correctly distinguished?
- [ ] Second-hand goods claims properly documented?
- [ ] Bad debt relief only after 12 months?

---

## PROHIBITIONS

- NEVER claim input tax on exempt supplies -- only taxable (including zero-rated) supplies qualify
- NEVER charge VAT if not registered as a vendor
- NEVER use a rate other than 15% for standard-rated supplies
- NEVER confuse zero-rated (input tax claimable) with exempt (input tax NOT claimable)
- NEVER claim input tax without a valid tax invoice (for supplies over R50)
- NEVER ignore the bimonthly filing deadline -- penalties apply from the first day late
- NEVER apply payments basis without SARS approval
- NEVER claim notional input on second-hand goods without proper documentation and declarations
- NEVER present calculations as definitive -- always label as estimated and direct client to a SARS-registered tax practitioner

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, chartered accountant (CA(SA)), or equivalent licensed practitioner in South Africa) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
