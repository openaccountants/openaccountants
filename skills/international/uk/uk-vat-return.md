---
name: uk-vat-return
description: >
  Use this skill whenever asked to prepare, review, or classify transactions for a UK VAT return (VAT100) for a self-employed individual or small business. Trigger on phrases like "VAT return UK", "VAT100", "VAT registration", "VAT rates", "flat rate scheme", "FRS", "cash accounting VAT", "Making Tax Digital", "MTD", "input tax", "output tax", "partial exemption", "reverse charge construction", "bad debt relief", "VAT9 boxes", "Box 1 to Box 9", "reduced rate", "zero-rated", "exempt supply", "de minimis VAT", "annual accounting scheme", or any question about UK VAT obligations. Covers the VAT100 9-box structure, standard/reduced/zero rates, registration threshold (GBP 90,000), Flat Rate Scheme, cash accounting scheme, annual accounting scheme, MTD requirements, input tax blocked categories, partial exemption, bad debt relief, and reverse charge for construction (CIS). ALWAYS read this skill before touching any UK VAT work.
version: 1.0
jurisdiction: GB
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# UK VAT Return (VAT100) -- Comprehensive Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Kingdom |
| Jurisdiction Code | GB |
| Primary Legislation | Value Added Tax Act 1994 (VATA 1994) |
| Supporting Legislation | VAT Regulations 1995 (SI 1995/2518); Finance Act 2024; Finance Act 2025; The Value Added Tax (Flat Rate Scheme) Order 2004; The VAT (Input Tax) Order 1992 (SI 1992/3222); Making Tax Digital (VAT) Regulations 2018 |
| Tax Authority | HM Revenue & Customs (HMRC) |
| Filing Portal | HMRC VAT Online Services / MTD-compatible software |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a UK-qualified accountant (ACA/ACCA/CTA) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 (VAT periods within calendar year 2025) |
| Confidence Coverage | Tier 1: VAT rates, registration threshold, 9-box structure, FRS percentages, filing deadlines, MTD requirements, interest/penalty regime. Tier 2: partial exemption calculation, FRS limited cost trader test, bad debt relief conditions, reverse charge classification. Tier 3: international services (B2B/B2C place of supply), import VAT, Tour Operators' Margin Scheme, VAT groups, pension fund refunds. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before preparing any VAT return, you MUST know:

1. **Is the client VAT registered?** [T1] -- if not, determine whether registration is required or voluntary
2. **VAT registration number** [T1] -- 9-digit GB number
3. **VAT scheme** [T1] -- Standard accounting, Flat Rate Scheme, Cash Accounting, or Annual Accounting
4. **VAT period** [T1] -- monthly, quarterly, or annual (and specific dates)
5. **Nature of supplies** [T1] -- standard-rated, reduced-rated, zero-rated, exempt, outside scope
6. **Does the client make exempt supplies?** [T2] -- triggers partial exemption considerations
7. **Is the client in construction (CIS)?** [T2] -- reverse charge may apply
8. **MTD compliance** [T1] -- is the client using MTD-compatible software with digital links?
9. **Previous period's turnover** [T1] -- for scheme eligibility checks

---

## Step 1: VAT Rates [T1]

**Legislation:** VATA 1994, Schedule 7A (reduced), Schedule 8 (zero)

| Rate | Percentage | Examples |
|------|-----------|----------|
| Standard | 20% | Most goods and services, professional fees, software, electronics |
| Reduced | 5% | Domestic fuel and power, children's car seats, energy-saving materials (installed in residential property), smoking cessation products |
| Zero | 0% | Food (most, not catering/hot takeaway), children's clothing and footwear, books and newspapers (print), public transport, new residential construction, exports |
| Exempt | N/A (no VAT charged, no input VAT recovery) | Financial services, insurance, education, health services, burial and cremation, postal services (Royal Mail universal service), land and property (unless opted to tax) |
| Outside scope | N/A | Wages, dividends, donations, non-business activities, statutory fees |

### Key Rate Traps

| Item | Rate | Note |
|------|------|------|
| Hot takeaway food | 20% | NOT zero-rated like cold food |
| Biscuits (plain) | 0% | Zero-rated |
| Biscuits (chocolate-covered) | 20% | Standard-rated (McVitie's Jaffa Cakes = cakes = 0%) |
| E-books / digital publications | 0% | Zero-rated since 1 May 2020 |
| PPE / safety equipment | 20% | Standard-rated |
| Catering | 20% | Standard-rated (even if the food itself would be zero-rated) |

---

## Step 2: VAT Registration [T1]

**Legislation:** VATA 1994, Schedule 1

### Compulsory Registration

| Threshold | Amount | Basis |
|-----------|--------|-------|
| Registration threshold | GBP 90,000 | Taxable turnover in the previous 12 months (rolling) |
| Forward-looking test | GBP 90,000 | Expected taxable turnover in the next 30 days alone |
| Notification deadline | 30 days from end of the month the threshold is exceeded |
| Effective date | First day of the second month after the threshold is exceeded |

### Voluntary Registration

Any person making taxable supplies (even below the threshold) may register voluntarily. Benefits: recover input VAT on purchases. Cost: must charge VAT on sales and comply with MTD.

### Deregistration Threshold

| Threshold | Amount |
|-----------|--------|
| Deregistration threshold | GBP 88,000 (taxable turnover expected to fall below this in next 12 months) |

---

## Step 3: VAT100 -- The 9-Box Structure [T1]

**Legislation:** VAT Regulations 1995, Regulation 25

| Box | Description | What Goes In |
|-----|-------------|-------------|
| Box 1 | VAT due on sales and other outputs | Output VAT charged to customers on standard and reduced-rate supplies; VAT on imports (postponed VAT accounting); reverse charge VAT due |
| Box 2 | VAT due on acquisitions from EU (legacy) | VAT on goods acquired from EU member states (post-Brexit: generally postponed import VAT in Box 1 instead) |
| Box 3 | Total VAT due (Box 1 + Box 2) | Automatic sum |
| Box 4 | VAT reclaimed on purchases and other inputs | Input VAT on allowable business purchases; import VAT recoverable; reverse charge VAT recoverable |
| Box 5 | Net VAT to pay or reclaim (Box 3 - Box 4) | If positive: amount to pay HMRC. If negative: refund due from HMRC |
| Box 6 | Total value of sales and all other outputs (excl. VAT) | Net value of ALL outputs (standard, reduced, zero, exempt) |
| Box 7 | Total value of purchases and all other inputs (excl. VAT) | Net value of ALL inputs (including exempt and zero-rated purchases) |
| Box 8 | Total value of supplies to EU (excl. VAT) | Post-Brexit: supplies of goods to EU customers (exports) |
| Box 9 | Total value of acquisitions from EU (excl. VAT) | Post-Brexit: goods acquired from EU (imports) |

### Box 5 Interpretation

```
if Box_5 > 0: taxpayer PAYS this amount to HMRC
if Box_5 < 0: HMRC REFUNDS this amount to the taxpayer
```

---

## Step 4: Flat Rate Scheme (FRS) [T2]

**Legislation:** VATA 1994, s26B; The Value Added Tax (Flat Rate Scheme) Order 2004

### Eligibility

| Criterion | Threshold |
|-----------|-----------|
| Estimated taxable turnover (next 12 months) | <= GBP 150,000 (excl. VAT) |
| Exit threshold | GBP 230,000 (incl. VAT) total business income |

### How FRS Works

Instead of computing output VAT minus input VAT, the business:
1. Charges VAT at the standard rate (20%) on invoices to customers
2. Pays HMRC a FLAT PERCENTAGE of gross (VAT-inclusive) turnover
3. Keeps the difference

### FRS Percentages -- Selected Sectors (2025)

| Sector | FRS % |
|--------|-------|
| Accountancy or bookkeeping | 14.5% |
| Advertising | 11.0% |
| Computer and IT consultancy | 14.5% |
| Computer repair | 10.5% |
| Estate agency or property management | 12.0% |
| Journalism or photography | 11.0% |
| Management consultancy | 14.0% |
| Publishing | 11.0% |
| Real estate | 14.0% |
| Secretarial services | 13.0% |
| Social worker | 11.0% |
| Transport or storage | 10.0% |
| Any other activity not listed | 12.0% |

### First-Year Discount

New VAT registrations get a 1% reduction in the FRS percentage for the first year of registration.

### Limited Cost Trader (LCT) [T2]

**Legislation:** Finance Act 2017

If the business spends less than 2% of gross turnover (or less than GBP 1,000 per year if greater) on "relevant goods," it is classified as a Limited Cost Trader.

| LCT Status | FRS Rate |
|------------|----------|
| Limited Cost Trader | 16.5% (regardless of sector) |
| NOT Limited Cost Trader | Sector rate from table above |

"Relevant goods" = goods used exclusively for the business. EXCLUDES: capital goods over GBP 2,000, food and drink consumed by the business or staff, vehicles/fuel/vehicle parts.

**[T2] Always compute the LCT test before applying the sector rate. Many service businesses (consultants, IT, accountants) with minimal goods purchases will be LCT at 16.5%, making FRS unattractive.**

---

## Step 5: Cash Accounting Scheme [T1]

**Legislation:** VAT Regulations 1995, Regulations 56-65

| Criterion | Detail |
|-----------|--------|
| Eligibility | Estimated taxable turnover <= GBP 1,350,000 |
| Exit threshold | GBP 1,600,000 |
| How it works | Account for VAT based on date of PAYMENT (not invoice date) |
| Benefit | Automatic bad debt relief -- no VAT due on unpaid invoices |
| Restriction | Cannot reclaim input VAT until payment is made |

### When Cash Accounting is Beneficial

| Scenario | Cash Accounting? |
|----------|-----------------|
| Client has slow-paying customers | YES -- defers output VAT until cash received |
| Client pays suppliers promptly | MAYBE -- delays input VAT recovery |
| Client has significant bad debts | YES -- automatic relief |
| Client is cash-flow positive with fast collections | NO -- standard accrual is simpler |

---

## Step 6: Annual Accounting Scheme [T1]

**Legislation:** VAT Regulations 1995, Regulations 49-55

| Criterion | Detail |
|-----------|--------|
| Eligibility | Estimated taxable turnover <= GBP 1,350,000 |
| Exit threshold | GBP 1,600,000 |
| How it works | One VAT return per year (instead of quarterly) |
| Interim payments | 9 monthly or 3 quarterly interim payments based on prior year's liability |
| Final payment | Balancing payment with the annual return (due 2 months after the year-end) |
| Benefit | Reduces admin burden; only one return per year |
| Restriction | Cannot combine with FRS |

---

## Step 7: Making Tax Digital (MTD) [T1]

**Legislation:** The VAT (Amendment) Regulations 2018 (SI 2018/261); Finance (No. 2) Act 2017

### Who Must Comply

| Requirement | Detail |
|-------------|--------|
| Mandatory for | ALL VAT-registered businesses (since April 2022) |
| Digital records | Must keep digital records of supplies made and received |
| Digital links | Data must flow digitally between software systems (no manual re-keying between spreadsheets) |
| Filing | VAT returns must be filed via MTD-compatible software (NOT via HMRC's online portal) |

### Digital Record-Keeping Requirements

| Must Record Digitally | Detail |
|----------------------|--------|
| Business name, address, VAT number | Identifying information |
| Each supply made (date, net value, VAT rate) | Output records |
| Each supply received (date, net value, VAT rate) | Input records |
| Time of supply (tax point) | For accrual accounting |
| Rate of VAT | Standard, reduced, zero, exempt |
| Reverse charge transactions | Must be separately identifiable |

### Compatible Software

HMRC maintains a list of MTD-compatible software. Examples include Xero, QuickBooks, FreeAgent, Sage, Kashflow. Bridging software (connecting spreadsheets to HMRC API) is also acceptable.

---

## Step 8: Input Tax -- Blocked Categories [T1]

**Legislation:** VATA 1994, s25; The VAT (Input Tax) Order 1992

The following input VAT CANNOT be reclaimed:

| Blocked Category | Detail |
|-----------------|--------|
| Business entertainment | Entertaining UK customers, suppliers, or other business contacts. Exception: entertaining overseas customers IS recoverable. |
| Motor cars | VAT on purchase or lease of cars NOT exclusively for business use. Exception: 100% business use (pool car, driving instructor car, taxi) = fully recoverable. |
| Car fuel (private element) | If car has any private use, full input VAT on fuel is blocked UNLESS the fuel scale charge is applied |
| Domestic accommodation for directors | Non-business use property |
| Non-business expenditure | Expenditure not wholly for business purposes |

### Partially Recoverable Items

| Item | Treatment |
|------|-----------|
| Mobile phones | Fully recoverable if business contract (even if some private use) |
| Home office costs | Apportion business vs private -- recover business element only |
| Mixed-use equipment | Apportion on reasonable basis |

---

## Step 9: Partial Exemption [T2]

**Legislation:** VATA 1994, s26; VAT Regulations 1995, Regulations 99-107

If the business makes BOTH taxable supplies (standard, reduced, zero) AND exempt supplies:

### Standard Method

| Category | Input VAT Treatment |
|----------|-------------------|
| Directly attributable to taxable supplies | Fully recoverable |
| Directly attributable to exempt supplies | NOT recoverable |
| Residual (not directly attributable to either) | Recoverable in proportion: taxable supplies / total supplies |

### De Minimis Test

| Test | Threshold |
|------|-----------|
| Monthly average | Exempt input VAT <= GBP 625 per month on average |
| Annual limit | Exempt input VAT <= GBP 7,500 per year |
| AND | Exempt input VAT <= 50% of total input VAT |

**If the de minimis test is met, ALL input VAT (including that attributable to exempt supplies) is recoverable.**

### Annual Adjustment

A partial exemption annual adjustment must be done at the end of the VAT year (the "longer period"). This compares the actual annual proportion against the proportions used in each quarter.

**[T2] Partial exemption is complex. Always flag for reviewer when a client makes any exempt supplies.**

---

## Step 10: Bad Debt Relief [T1]

**Legislation:** VATA 1994, s36; VAT Regulations 1995, Regulation 168-172

If a customer does not pay, the supplier can reclaim the output VAT already paid to HMRC.

### Conditions

| Condition | Requirement |
|-----------|-------------|
| Age of debt | At least 6 months old (from the later of the due date or the date of supply) |
| Written off | The debt must be written off in the accounts |
| VAT return | Claim on the VAT return for the period in which conditions are met |
| Record | Must keep a record of the bad debt relief claim |
| Time limit | Claim must be made within 4 years and 6 months of the date of supply |

### Mechanism

```
bad_debt_relief = (outstanding_amount × VAT_rate) / (1 + VAT_rate)
```

Add the relief amount to Box 4 (input tax) on the VAT return.

**If the customer later pays (wholly or partially), the relief must be reversed in the period of payment.**

---

## Step 11: Reverse Charge -- Construction Industry (CIS) [T2]

**Legislation:** VATA 1994, s55A; The Value Added Tax (Section 55A) (Specified Services and Excepted Supplies) Order 2020

### What It Is

For certain construction services between VAT-registered businesses within the Construction Industry Scheme (CIS), the CUSTOMER (not the supplier) accounts for the VAT.

### When It Applies

| Condition | Detail |
|-----------|--------|
| Supply | Specified construction services (building, civil engineering, installation, completion, repair, decoration, demolition) |
| Supplier | VAT-registered, CIS-registered |
| Customer | VAT-registered, CIS-registered, AND makes onward supplies of construction services |
| End user exemption | Does NOT apply if the customer is an "end user" or "intermediary supplier" |

### Supplier's Invoice

| Item | Detail |
|------|--------|
| VAT rate shown | Reverse charge -- customer to account for VAT |
| Net amount | Shown as normal |
| VAT amount | NOT charged by supplier |
| Invoice annotation | Must state "Reverse charge: Customer to account to HMRC for VAT on this supply" |

### Customer's VAT Return

| Box | Entry |
|-----|-------|
| Box 1 | Include the VAT amount (output tax -- as if the customer supplied to itself) |
| Box 4 | Include the same VAT amount (input tax recovery -- subject to normal rules) |
| Box 6 | Do NOT include (this is the customer's input, not output) |
| Box 7 | Include the net value |

**[T2] Reverse charge classification is fact-specific. Always flag for reviewer when construction services are involved between CIS-registered parties.**

---

## Step 12: Filing Deadlines and Penalties [T1]

**Legislation:** Finance Act 2021 (new penalty regime from Jan 2023); VAT Regulations 1995

### Filing Deadline

| Return Frequency | Deadline |
|-----------------|----------|
| Quarterly | 1 month and 7 days after the end of the VAT period |
| Monthly | 1 month and 7 days after the end of the month |
| Annual | 2 months after the end of the annual period |

### New Penalty Regime (from January 2023)

#### Late Submission Penalties (Points-Based)

| Points | Annual filers: penalty at | Quarterly filers: penalty at | Monthly filers: penalty at |
|--------|---------------------------|-----------------------------|-----------------------------|
| Threshold | 2 points | 4 points | 5 points |
| Penalty per late return (once threshold reached) | GBP 200 | GBP 200 | GBP 200 |

Points expire after a period of compliance (24 months for annual, 12 months for quarterly, 6 months for monthly).

#### Late Payment Penalties

| Days Late | Penalty |
|-----------|---------|
| 1-15 days | No penalty |
| 16-30 days | 2% of outstanding VAT at day 15 |
| 31+ days | Additional 2% of outstanding VAT at day 30, plus daily rate of 4% per annum |

#### Late Payment Interest

- Runs from the due date until payment
- Rate: Bank of England base rate + 2.5%

---

## Step 13: Edge Case Registry

### EC1 -- Voluntary registration below threshold [T1]
**Situation:** Freelancer with GBP 40,000 turnover wants to register for VAT to recover input VAT on a GBP 10,000 computer purchase.
**Resolution:** Voluntary registration is permitted. Client must then charge 20% on all standard-rated supplies and comply with MTD. Consider whether the input VAT benefit outweighs the admin burden and potential price impact on price-sensitive B2C customers.

### EC2 -- FRS limited cost trader trap [T2]
**Situation:** IT consultant on FRS (sector rate 14.5%). Annual turnover GBP 80,000 (gross GBP 96,000). Goods purchased: GBP 500.
**Resolution:** Goods < 2% of GBP 96,000 (GBP 1,920) and < GBP 1,000. Client IS a Limited Cost Trader. Rate = 16.5%, not 14.5%. VAT due = GBP 96,000 x 16.5% = GBP 15,840. Under standard accounting: output = GBP 16,000, input ~GBP 2,000 (if any), net = ~GBP 14,000. FRS at 16.5% is WORSE than standard accounting. [T2] recommend leaving FRS.

### EC3 -- Mixed standard and exempt supplies [T2]
**Situation:** Accountant provides standard-rated accounting services and exempt financial intermediary services.
**Resolution:** Partial exemption applies. Identify directly attributable input VAT for each stream. Apportion residual input VAT. Apply de minimis test (GBP 625/month average AND <= 50% of total input VAT). [T2] flag for reviewer.

### EC4 -- Bad debt relief timing [T1]
**Situation:** Invoice issued 1 March, payment due 31 March. Customer has not paid. Today is 15 October (6.5 months from due date).
**Resolution:** Debt is 6 months old from the due date (31 March + 6 months = 30 September). Conditions met from 1 October. If written off in accounts, claim relief on the VAT return covering October.

### EC5 -- Reverse charge supply incorrectly treated as normal [T2]
**Situation:** Sub-contractor invoiced GBP 50,000 + GBP 10,000 VAT for plastering services to a main contractor (both CIS-registered). Main contractor paid GBP 60,000.
**Resolution:** This should have been reverse charge. Supplier should not have charged VAT. Main contractor should not have paid VAT to the supplier. Supplier must issue a credit note and re-invoice without VAT (stating reverse charge). Main contractor self-accounts for VAT in Boxes 1 and 4. [T2] flag for reviewer.

### EC6 -- Tourist departing UK, retail export scheme [T2]
**Situation:** Overseas customer buys goods from UK shop, wants VAT refund.
**Resolution:** The UK VAT Retail Export Scheme (VAT 407) was ABOLISHED from 1 January 2021 (post-Brexit). No VAT refund for personal exports by non-EU visitors. B2B exports remain zero-rated with evidence of export.

### EC7 -- Place of supply for digital services to EU consumer [T3]
**Situation:** UK freelancer sells software subscription to an individual in France.
**Resolution:** This is a B2C supply of digital services. Post-Brexit, the UK supplier may need to register for EU VAT (OSS) in one EU member state. This is outside the scope of the UK VAT return. [T3] escalate.

### EC8 -- Flat Rate Scheme and capital goods over GBP 2,000 [T1]
**Situation:** FRS business buys a GBP 5,000 laptop (GBP 6,000 inc. VAT).
**Resolution:** Under FRS, input VAT on capital goods costing GBP 2,000 or more (inc. VAT) CAN be reclaimed separately on the VAT return. Claim GBP 1,000 in Box 4. This is a one-off exception to the general FRS rule.

### EC9 -- Cash accounting and bad debt [T1]
**Situation:** Client uses cash accounting scheme. Customer has not paid a GBP 12,000 invoice for 8 months.
**Resolution:** Under cash accounting, the client has NOT yet accounted for output VAT on this supply (because payment has not been received). No bad debt relief claim is needed -- the VAT was never charged. This is the built-in benefit of cash accounting.

### EC10 -- Threshold approached: rolling 12-month test [T1]
**Situation:** Month-by-month turnover: each month GBP 7,000. After 13 months, rolling 12-month total = GBP 84,000. In month 14, a GBP 10,000 contract brings rolling 12-month total to GBP 87,000. Month 15: GBP 8,000, rolling total = GBP 88,000. Month 16: GBP 9,000, rolling total = GBP 90,000.
**Resolution:** The rolling 12-month total reaches GBP 90,000 at the end of month 16. Client must notify HMRC within 30 days of the end of that month. Registration effective from the 1st of the month following the 30-day notification period. Monitor monthly.

### EC11 -- Annual accounting scheme interim payments [T1]
**Situation:** Client on annual scheme. Prior year VAT liability = GBP 12,000.
**Resolution:** 9 monthly interim payments of GBP 1,200 each (10% of prior year liability), starting in month 4 of the VAT year. Balancing payment with the annual return.

---

## Step 14: Full VAT Return Walkthrough -- Standard Accounting [T1]

### Example: Quarterly Return, Standard-Rated Business

```
Sales for the quarter:
  Standard-rated sales (net):          GBP 45,000
  Zero-rated sales (exports):         GBP 5,000
  Total sales:                         GBP 50,000
  Output VAT (20% x GBP 45,000):      GBP 9,000

Purchases for the quarter:
  Standard-rated purchases (net):      GBP 12,000
  Input VAT (20% x GBP 12,000):       GBP 2,400
  Blocked entertainment VAT:           GBP 200 (not recoverable)
  Recoverable input VAT:              GBP 2,200

VAT100:
  Box 1: GBP 9,000          (output VAT)
  Box 2: GBP 0              (EU acquisitions)
  Box 3: GBP 9,000          (Box 1 + Box 2)
  Box 4: GBP 2,200          (input VAT, net of blocked)
  Box 5: GBP 6,800          (pay to HMRC)
  Box 6: GBP 50,000         (total outputs ex VAT)
  Box 7: GBP 12,000         (total inputs ex VAT)
  Box 8: GBP 5,000          (supplies to EU)
  Box 9: GBP 0              (acquisitions from EU)
```

---

## Step 15: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified accountant must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified accountant. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard quarterly return
**Input:** Standard-rated sales GBP 30,000. Standard-rated purchases GBP 8,000. No exempt supplies. No blocked items.
**Expected output:** Box 1 = GBP 6,000. Box 4 = GBP 1,600. Box 5 = GBP 4,400 (pay to HMRC). Box 6 = GBP 30,000. Box 7 = GBP 8,000.

### Test 2 -- Refund return (zero-rated exports exceed inputs)
**Input:** Zero-rated export sales GBP 50,000. Standard-rated purchases GBP 20,000.
**Expected output:** Box 1 = GBP 0 (zero-rated outputs). Box 4 = GBP 4,000. Box 5 = -GBP 4,000 (HMRC refunds). Box 6 = GBP 50,000. Box 7 = GBP 20,000. Box 8 = GBP 50,000 (if EU).

### Test 3 -- FRS computation
**Input:** FRS business, sector rate 14.5% (not LCT). Gross turnover (inc. VAT) GBP 60,000.
**Expected output:** VAT payable = GBP 60,000 x 14.5% = GBP 8,700. Box 1 = GBP 8,700. Box 6 = GBP 50,000 (net). Capital goods claim in Box 4 if applicable.

### Test 4 -- Blocked entertainment
**Input:** Client spent GBP 2,000 on client entertainment (GBP 400 VAT). Also GBP 1,000 on staff Christmas party (GBP 200 VAT).
**Expected output:** Client entertainment VAT (GBP 400) = blocked, not recoverable. Staff entertainment (GBP 200) = recoverable (staff entertainment is NOT blocked). Box 4 includes GBP 200 only.

### Test 5 -- Bad debt relief
**Input:** Invoice for GBP 12,000 + GBP 2,400 VAT = GBP 14,400. Issued 1 January. Due 31 January. Unpaid. Today = 15 August. Debt written off in accounts.
**Expected output:** 6 months from due date (31 Jan) = 31 July. Conditions met. Relief = GBP 2,400. Claim in Box 4 of the VAT return covering August.

### Test 6 -- Registration threshold test
**Input:** Rolling 12-month taxable turnover: GBP 89,500 at end of March. April sales = GBP 3,000. Rolling total = GBP 91,000.
**Expected output:** Threshold GBP 90,000 exceeded at end of April. Notify HMRC by 30 May. Registration effective from 1 June (or 1 July if HMRC applies standard timeline).

### Test 7 -- Partial exemption de minimis
**Input:** Total input VAT = GBP 8,000. Directly attributable to taxable supplies = GBP 5,000. Directly attributable to exempt = GBP 500. Residual = GBP 2,500. Taxable proportion = 90%. Exempt input VAT = GBP 500 + (GBP 2,500 x 10%) = GBP 750. Monthly average = GBP 250 (for 3-month period).
**Expected output:** Exempt input VAT GBP 750/quarter = GBP 250/month. Below GBP 625/month AND below 50% of total input VAT. De minimis met. Recover ALL GBP 8,000.

---

## PROHIBITIONS

- NEVER prepare a VAT return without confirming the client's VAT scheme (standard, FRS, cash, annual)
- NEVER apply FRS sector rates without checking the Limited Cost Trader test first
- NEVER reclaim input VAT on blocked categories (business entertainment, non-pool cars)
- NEVER confuse zero-rated (VAT recoverable) with exempt (VAT not recoverable)
- NEVER file a VAT return outside MTD-compatible software for a VAT-registered business
- NEVER claim bad debt relief before 6 months have elapsed from the later of due date or supply date
- NEVER apply the reverse charge without verifying both parties are CIS-registered and the customer makes onward construction supplies
- NEVER include items outside the scope of VAT (wages, dividends) in Box 6 or Box 7
- NEVER ignore the registration threshold -- monitor rolling 12-month turnover continuously
- NEVER claim input VAT on exempt supplies unless the partial exemption de minimis test is met
- NEVER present FRS as always beneficial -- the LCT test at 16.5% makes it worse than standard accounting for most service businesses with low goods expenditure

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
