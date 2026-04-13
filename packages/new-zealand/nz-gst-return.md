---
name: nz-gst-return
description: >
  Use this skill whenever asked about New Zealand GST returns for self-employed individuals. Trigger on phrases like "GST return", "GST101A", "GST rate NZ", "input tax", "output tax", "zero-rated", "GST registration", "taxable supply", "IRD GST", "myIR GST", or any question about GST filing for sole traders in New Zealand. Covers the 15% standard rate, zero-rated and exempt supplies, $60K registration threshold, invoice and payments basis, and GST101A return preparation. ALWAYS read this skill before touching any NZ GST work.
version: 2.0
jurisdiction: NZ
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# NZ GST Return -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | New Zealand |
| Tax | Goods and Services Tax (GST) at 15% |
| Currency | NZD only |
| Tax year basis | Balance date (typically 31 March) |
| Primary legislation | Goods and Services Tax Act 1985 (GSTA 1985) |
| Tax authority | Inland Revenue (IR / Te Tari Taake) |
| Filing portal | myIR (myir.ird.govt.nz) |
| Filing deadline | 28th of month after period end |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a New Zealand chartered accountant (CA) |
| Skill version | 2.0 |

### Rate Table

| Rate | Application |
|---|---|
| 15% | Standard rate on all taxable supplies |
| 0% | Zero-rated supplies (exports, going concerns, certain foodstuffs, fine metals) |
| Exempt | Financial services, residential rent, donated goods (certain conditions) |

### Tax Fraction

For GST-inclusive amounts at 15%: **3/23** (i.e. 15/115 = 3/23).

### Key Thresholds

| Item | Amount (NZD) |
|---|---|
| Mandatory GST registration | $60,000 taxable supplies in any 12-month period |
| Voluntary registration | Any person making taxable supplies |
| Payments basis eligibility | Taxable supplies < $2,000,000 |
| Six-monthly filing eligibility | Taxable supplies < $500,000 |
| Monthly filing required | Taxable supplies > $24,000,000 |
| Tax invoice required | Supplies over $50 |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| GST registration status unknown | STOP -- do not compute |
| Accounting basis unknown | Invoice basis (default) |
| Supply classification unknown | Standard-rated at 15% |
| Private use proportion unknown | 0% GST recovery |
| Going concern status unknown | Not a going concern (charge GST) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the GST period in CSV, PDF, or pasted text, plus confirmation of GST registration status and accounting basis.

**Recommended:** Sales invoices, purchase invoices for any input tax claim, GST registration number.

**Ideal:** Complete invoice register, prior period GST return, reconciliation of carried-forward amounts.

### Refusal Catalogue

**R-NZ-1 -- Not GST-registered.** "If turnover is below $60,000 and the client is not voluntarily registered, no GST filing is required. Stop."

**R-NZ-2 -- Companies and partnerships.** "This skill covers individual self-employed persons only. Company and partnership GST returns may have additional requirements."

**R-NZ-3 -- Financial services (complex).** "Complex financial services GST treatment requires specialist review. Escalate."

**R-NZ-4 -- Cross-border digital services (complex).** "Non-resident digital services GST has specific registration and collection rules. Escalate if amounts are material."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| DIRECT CREDIT [client] / DC [client] | Taxable supply | GST-inclusive revenue | Standard client payment |
| EFTPOS SETTLEMENT / EFTPOS CREDIT | Taxable supply | Revenue | Card terminal settlement |
| INTERNET BANKING CREDIT [client] | Taxable supply | Revenue | Online bank transfer |
| STRIPE NZ / STRIPE PAYOUT | Taxable supply | Revenue (net of fees) | Stripe payout -- gross up for fees |
| SHOPIFY PAYOUT / SHOPIFY SETTLEMENT | Taxable supply | Revenue | E-commerce platform settlement |
| XERO INVOICE PAYMENT | Taxable supply | Revenue | Xero-linked payment |
| INTEREST / INT EARNED [bank] | Exempt | NOT taxable supply | Bank interest -- exempt financial service |
| DIVIDEND [company] | Exempt | NOT taxable supply | Dividend |
| IRD REFUND / TAX REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

| Pattern | Expense Category | Treatment | Notes |
|---|---|---|---|
| SPARK / VODAFONE / 2DEGREES | Communications | Business portion deductible | Mixed use: apportion |
| VECTOR / MERCURY / GENESIS / CONTACT ENERGY | Utilities | Business portion deductible | Home office: apportion |
| COUNTDOWN / PAK'N SAVE / NEW WORLD | NOT business | Private | Unless entertainment or business meeting |
| BUNNINGS / MITRE 10 | Office supplies | Deductible if business | Keep receipts |
| GOOGLE ADS / META / LINKEDIN | Advertising | Fully deductible | |
| ADOBE / MICROSOFT / XERO / SLACK | Software | Fully deductible | Business subscription |
| AIR NEW ZEALAND / JETSTAR | Travel | Deductible if business | Keep itinerary |
| UBER NZ / TAXI | Travel | Deductible if business | Not commuting |
| ACC LEVY | EXCLUDE | Government levy | Not GST |
| IRD INCOME TAX / IRD PAYE | EXCLUDE | Tax payment | Not deductible |
| BANK FEE / ANZ FEE / ASB FEE / BNZ FEE / WESTPAC FEE | Exempt | No GST on bank fees | Financial service exempt |
| PERSONAL TRANSFER / OWN ACCOUNT | EXCLUDE | Drawings | Not business |

### 3.3 Zero-Rated Supply Indicators

| Pattern | Treatment | Notes |
|---|---|---|
| EXPORT / INTERNATIONAL FREIGHT | Zero-rated output | Goods exported from NZ |
| GOING CONCERN SALE | Zero-rated output | Both parties must be GST-registered |
| FINE METALS / GOLD BULLION | Zero-rated | Gold, silver, platinum of certain fineness |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Two-Monthly Return

**Input:** Period Jan-Feb. Total sales (incl. GST) $23,000. Total purchases (incl. GST) $8,050. All standard-rated. No adjustments.

**Reasoning:**
Output tax: $23,000 x 3/23 = $3,000. Input tax: $8,050 x 3/23 = $1,050. Net GST payable: $3,000 - $1,050 = $1,950.

**Classification:** GST payable $1,950.

### Example 2 -- Exporter in Refund Position

**Input:** Total sales $50,000 (all zero-rated exports). Total purchases (incl. GST) $17,250.

**Reasoning:**
Output tax: $0 (zero-rated). Input tax: $17,250 x 3/23 = $2,250. GST refund: $2,250.

**Classification:** GST refund $2,250.

### Example 3 -- Entertainment Expense

**Input:** Business dinner $460 (incl. GST).

**Reasoning:**
GST content: $460 x 3/23 = $60. Entertainment 50% restriction applies. Claimable: 50% x $60 = $30. Non-claimable: $30.

**Classification:** Input tax claimable $30 only.

### Example 4 -- Private Use Apportionment

**Input:** Laptop purchased for $2,300 (incl. GST), used 70% business, 30% private.

**Reasoning:**
GST content: $2,300 x 3/23 = $300. Claim 70%: $300 x 70% = $210.

**Classification:** Input tax $210. Flag for reviewer on apportionment basis.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 GST101A Return Line-by-Line

| Box | Description | How to Populate |
|---|---|---|
| 5 | Total sales and income for the period | All income including GST-inclusive, zero-rated, and exempt |
| 6 | Zero-rated supplies | Exports and other 0% supplies (included in Box 5) |
| 7 | Total purchases and expenses | All purchases including GST-inclusive, zero-rated, and exempt |
| 8 | GST on sales (output tax) | (Box 5 - Box 6 - exempt supplies) x 3/23 |
| 9 | GST on purchases (input tax) | (Box 7 - exempt purchases - private) x 3/23 |
| 10 | Adjustments -- increase | Prior period corrections increasing GST payable |
| 11 | Adjustments -- decrease | Prior period corrections decreasing GST payable |
| 12 | GST to pay or refund | Box 8 + Box 10 - Box 9 - Box 11 |

### 5.2 Accounting Basis (s 19, 19A)

| Basis | Rule | Eligibility |
|---|---|---|
| Invoice basis | Account for GST when invoice is issued or received | Default for all |
| Payments basis | Account for GST when payment is made or received | Taxable supplies < $2M |
| Hybrid basis | Invoice for sales, payments for purchases (or vice versa) | By application to IR |

### 5.3 Filing Frequency and Deadlines (s 15, 16)

| Frequency | Eligibility | Deadline |
|---|---|---|
| Six-monthly | Taxable supplies < $500,000 | 28th of month after period end |
| Two-monthly | Default for most businesses | 28th of month after period end |
| Monthly | Taxable supplies > $24M or by election | 28th of month after period end |

### 5.4 Input Tax Rules (s 20, 21)

Claimable if: supply made by GST-registered person, valid tax invoice held (for supplies over $50), goods/services used in the taxable activity.

Not claimable: private or exempt use, entertainment (50% restriction), motor vehicles (private use portion must be apportioned).

### 5.5 Penalties

| Offence | Penalty |
|---|---|
| Late filing | $250 per return |
| Repeated late filing | Escalating penalties |
| Interest on unpaid GST | From original due date |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed-Use Assets

If the proportion of taxable use changes, adjustments may be required. Flag for reviewer if mixed-use assets exceed $5,000.

### 6.2 Bad Debts (s 26)

On invoice basis, if a debt is written off after 6 months, claim a bad debt adjustment (Box 11) for the GST component.

### 6.3 Second-Hand Goods Input Tax

A registered person can claim input tax on second-hand goods purchased from a non-registered person, subject to conditions.

### 6.4 Change of Use Adjustments

When the business/private use proportion of an asset changes, adjustments may be required in the GST return.

---

## Section 7 -- Working Paper Template

```
NZ GST WORKING PAPER
Taxpayer: _______________  IRD Number: ___________
GST Number: ___________
Period: ___________  Basis: Invoice / Payments
Filing Frequency: Monthly / 2-Monthly / 6-Monthly

A. TOTAL SALES (Box 5)
  A1. Standard-rated sales (incl. GST)           ___________
  A2. Zero-rated sales                           ___________
  A3. Exempt sales                               ___________
  A4. Total sales (A1 + A2 + A3)                 ___________

B. ZERO-RATED SUPPLIES (Box 6)                   ___________

C. TOTAL PURCHASES (Box 7)
  C1. Standard-rated purchases (incl. GST)       ___________
  C2. Zero-rated purchases                       ___________
  C3. Exempt purchases                           ___________
  C4. Total purchases                            ___________

D. OUTPUT TAX (Box 8)
  (A4 - B - exempt) x 3/23                      ___________

E. INPUT TAX (Box 9)
  (C4 - exempt - private) x 3/23                ___________

F. ADJUSTMENTS
  F1. Increase (Box 10)                          ___________
  F2. Decrease (Box 11)                          ___________

G. GST PAYABLE / REFUND (Box 12)
  D + F1 - E - F2                                ___________

REVIEWER FLAGS:
  [ ] Registration status confirmed?
  [ ] Accounting basis confirmed?
  [ ] Entertainment 50% restriction applied?
  [ ] Private use apportionment applied?
  [ ] Tax invoices held for all input claims?
```

---

## Section 8 -- Bank Statement Reading Guide

### NZ Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| ANZ NZ | CSV / PDF | Date, Description, Amount, Balance |
| ASB | CSV | Date, Unique Id, Tran Type, Cheque Number, Payee, Memo, Amount |
| BNZ | CSV | Date, Description, Debit, Credit, Balance |
| Westpac NZ | CSV | Date, Description, Debit, Credit, Balance |
| Kiwibank | CSV | Date, Description, Amount, Balance |
| TSB | CSV | Date, Details, Debit, Credit, Balance |

### Key NZ Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| D/C or DIRECT CREDIT | Bank transfer in | Potential income |
| AP or AUTOPAY | Automatic payment out | Regular expense |
| EFTPOS | Card terminal payment | Expense or income |
| TFR / TRANSFER | Internal transfer | Investigate -- may be drawings |
| DD / DIRECT DEBIT | Direct debit | Regular expense |
| IRD / INLAND REVENUE | Tax payment or refund | Exclude |
| ACC | ACC levy | Exclude from GST |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all business-name credits as potential taxable supplies
2. Classify all regular debits to known suppliers as potential input tax claims
3. Apply conservative defaults: invoice basis, 0% private use recovery
4. Flag all entertainment expenses for 50% restriction
5. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- NZ GST RETURN
1. Are you GST-registered? If so, what is your GST number?
2. What is your filing frequency (monthly, 2-monthly, 6-monthly)?
3. Are you on invoice basis or payments (cash) basis?
4. What is your balance date?
5. Do you make any zero-rated supplies (exports)?
6. Do you make any exempt supplies (financial services, residential rent)?
7. Do you use a vehicle for business? What percentage is business use?
8. Do you work from home? What percentage is business use?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Section |
|---|---|
| Imposition of GST | GSTA 1985, s 8 |
| Zero-rated supplies | GSTA 1985, s 11 |
| Exempt supplies | GSTA 1985, s 14 |
| Registration | GSTA 1985, s 51 |
| Accounting basis | GSTA 1985, s 19, 19A |
| Input tax | GSTA 1985, s 20, 21 |
| Filing periods | GSTA 1985, s 15, 16 |
| Bad debts | GSTA 1985, s 26 |

### Known Gaps / Out of Scope

- Company and partnership GST returns
- Complex financial services
- Cross-border digital services (non-resident supplier rules)
- Associated persons transactions
- GST grouping

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; NZ bank formats; local platform patterns; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration confirmed and GST number recorded?
- [ ] Accounting basis confirmed (invoice vs payments)?
- [ ] Tax fraction 3/23 used consistently?
- [ ] Entertainment 50% restriction applied?
- [ ] Exempt supplies included in Box 5 but excluded from GST calculation?
- [ ] Zero-rated supplies correctly reported in Box 6?

---

## PROHIBITIONS

- NEVER charge GST if the person is not GST-registered
- NEVER claim input tax on private expenditure
- NEVER claim full input tax on entertainment -- the 50% restriction applies
- NEVER use a tax fraction other than 3/23 for the 15% rate
- NEVER allow a going concern zero-rating unless both parties are registered
- NEVER ignore the accounting basis -- invoice vs payments basis changes when GST is accounted for
- NEVER omit exempt supplies from Box 5 (total sales) -- they are included in total but excluded from GST calculation
- NEVER present calculations as definitive -- always label as estimated and direct client to IR or a qualified NZ chartered accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
