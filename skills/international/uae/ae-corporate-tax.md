---
name: ae-corporate-tax
description: >
  Use this skill whenever asked about UAE Corporate Tax for freelancers, sole establishments, or small businesses. Trigger on phrases like "how much tax do I pay in UAE", "corporate tax UAE", "CT return", "FTA", "small business relief", "free zone tax", "qualifying free zone person", "AED 375,000", "9% tax", "taxable income UAE", "corporate tax registration", "UAE tax return", "self-employed tax UAE", "freelancer tax Dubai", or any question about computing or filing UAE corporate tax. This skill covers the 0%/9% rate structure, small business relief (revenue under AED 3M), qualifying free zone person rules, deductible and non-deductible expenses, transfer pricing, registration requirements, and filing deadlines. Note: the UAE has NO personal income tax -- self-employed individuals and sole establishments are subject to corporate tax. ALWAYS read this skill before touching any UAE corporate tax work.
version: 1.0
jurisdiction: AE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# UAE Corporate Tax -- Freelancers and Sole Establishments Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Arab Emirates |
| Jurisdiction Code | AE |
| Primary Legislation | Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses |
| Supporting Legislation | Cabinet Decision No. 116 of 2022 (Small Business Relief); Cabinet Decision No. 37 of 2023 (Free Zone); Ministerial Decision No. 73 of 2023 (Non-Deductible Expenditure); Ministerial Decision No. 229 of 2025 (Qualifying Activities); Federal Decree-Law No. 28 of 2022 (Tax Procedures) |
| Tax Authority | Federal Tax Authority (FTA) |
| Filing Portal | EmaraTax (tax.gov.ae) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by a UAE-licensed tax agent |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, small business relief threshold, registration requirement, filing deadline calculation, non-deductible items list. Tier 2: qualifying free zone person determination, transfer pricing documentation, mixed-use expense apportionment, related party transactions. Tier 3: group relief, holding company structures, international tax treaties, permanent establishment determinations, withholding tax on cross-border payments. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed tax agent must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any corporate tax figure, you MUST know:

1. **Business structure** [T1] -- natural person conducting business (sole establishment / freelancer), civil company, or other entity. This skill covers natural persons and sole establishments only.
2. **Revenue in the tax period** [T1] -- total revenue (turnover) for the financial year. Determines small business relief eligibility.
3. **Free zone status** [T1] -- is the business registered in a UAE free zone? If yes, determine if it qualifies as a Qualifying Free Zone Person (QFZP).
4. **Financial year end** [T1] -- determines filing and payment deadlines.
5. **Gross income** [T1] -- total business income (revenue from services, goods, other sources).
6. **Business expenses** [T1/T2] -- nature and amount of each expense.
7. **Related party transactions** [T2] -- any transactions with connected persons (family, commonly-owned entities).
8. **Prior year losses** [T1] -- tax losses available for carry-forward.
9. **Registration status** [T1] -- whether the business is already registered for corporate tax with the FTA.
10. **Other UAE taxes** [T1] -- VAT registration status (affects expense treatment).

**If business structure is unknown, STOP. Do not compute. Business structure determines the applicable rules.**

---

## Step 1: No Personal Income Tax -- Confirm [T1]

**Legislation:** UAE Constitution; Federal Decree-Law No. 47 of 2022, Article 3

**The UAE does not impose personal income tax on individuals.** There is no tax on salary, wages, or personal investment income for individuals.

However, **natural persons conducting business activities** in the UAE are subject to corporate tax if their total turnover exceeds AED 1,000,000 in a calendar year. This means:

- A freelancer with annual revenue over AED 1,000,000 must register for and pay corporate tax.
- A sole establishment (sole proprietorship) is subject to corporate tax regardless of legal form.
- Investment income (interest, dividends, capital gains) earned by a natural person in a personal capacity (not through a licensed business) is generally NOT subject to corporate tax.

**Key threshold for natural persons:** Turnover of AED 1,000,000. Below this, a natural person conducting business is not subject to corporate tax (Ministerial Decision No. 73 of 2023).

---

## Step 2: Corporate Tax Rates [T1]

**Legislation:** Federal Decree-Law No. 47 of 2022, Article 3

### Standard Rates [T1]

| Taxable Income (AED) | Rate |
|----------------------|------|
| 0 -- 375,000 | 0% |
| 375,001+ | 9% |

### Qualifying Free Zone Person Rates [T1]

| Income Type | Rate |
|------------|------|
| Qualifying income | 0% |
| Non-qualifying income | 9% |

**There is no higher rate. The UAE corporate tax is a flat 9% above the threshold -- one of the lowest globally.**

**Note:** A separate rate (15%) applies to large multinationals with consolidated global revenue exceeding EUR 750 million (Pillar Two / Global Minimum Tax -- effective for financial years starting on or after 1 January 2025). This is [T3] -- escalate if applicable.

---

## Step 3: Small Business Relief [T1]

**Legislation:** Federal Decree-Law No. 47 of 2022, Article 21; Cabinet Decision No. 116 of 2022; Ministerial Decision No. 73 of 2023

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Status | Must be a Resident Person (UAE-incorporated or effectively managed in the UAE) |
| Revenue threshold | Revenue must not exceed AED 3,000,000 in the relevant tax period |
| Not a member of a Multinational Enterprise Group | Global consolidated revenue must be below AED 3.15 billion |
| Not a Qualifying Free Zone Person | Cannot claim both SBR and QFZP benefits simultaneously |
| Valid period | Available for tax periods starting on or before 31 December 2026 |

### How It Works [T1]

- If eligible and the election is made, **taxable income is treated as nil** for the tax period. Effective tax = AED 0.
- The election must be **actively made** on the corporate tax return filed through EmaraTax. It is NOT automatic.
- The business must still **register for corporate tax** and **file a return** even if claiming SBR.

### Important Limitations [T1]

- Tax losses **cannot be created or carried forward** in a period where SBR is claimed.
- If the business exceeds AED 3,000,000 in a subsequent period, SBR is no longer available for that period.
- The AED 3,000,000 threshold is based on **revenue (turnover)**, not profit or taxable income.

---

## Step 4: Qualifying Free Zone Person (QFZP) [T1/T2]

**Legislation:** Federal Decree-Law No. 47 of 2022, Articles 18-19; Cabinet Decision No. 37 of 2023; Ministerial Decision No. 229 of 2025

### Eligibility Conditions [T1]

To qualify as a QFZP, ALL of the following must be met:

| Condition | Requirement |
|-----------|-------------|
| Maintain adequate substance | Have adequate employees, assets, and operating expenditure in the free zone |
| Derive qualifying income | Income must come from qualifying activities (see below) |
| Not elected out of free zone regime | Must not have elected to be treated as a standard taxpayer |
| Meet the de minimis requirement | Non-qualifying revenue must not exceed 5% of total revenue or AED 5,000,000, whichever is lower |
| Comply with transfer pricing rules | Maintain arm's length pricing for related party transactions |
| Prepare audited financial statements | Mandatory for all QFZPs (from 2025 onwards) |

### Qualifying Activities (Ministerial Decision No. 229 of 2025) [T1]

| Activity | Notes |
|----------|-------|
| Manufacturing of goods or materials | Processing or converting materials |
| Trading of qualifying commodities | As defined by ministerial decision |
| Holding of shares and other securities | Investment holding |
| Headquarter services to related parties | Group management functions |
| Treasury and financing services to related parties | Intra-group financing |
| Ship management | Maritime services |
| Fund management (regulated) | Licensed investment management |
| Wealth and investment management (regulated) | Licensed advisory |
| Logistics services | Warehousing, distribution |
| Distribution in/from a designated zone | Import/re-export |
| Reinsurance | Regulated reinsurance activities |
| Any other activity specified by Cabinet Decision | Check for updates |

### Non-Qualifying Activities (Excluded) [T1]

| Activity | Notes |
|----------|-------|
| Transactions with natural persons | Revenue from individual customers (not businesses) |
| Banking activities (regulated) | Unless specifically carved out |
| Insurance activities (regulated) | Unless reinsurance |
| Finance and leasing activities | Except intra-group as above |
| Ownership or exploitation of immovable property | Real estate income |
| Ownership or exploitation of intellectual property | Unless ancillary to a qualifying activity |
| Any activity not listed as qualifying | Default to non-qualifying |

[T2] Flag for reviewer: QFZP determination is complex. Confirm all conditions are met before advising 0% rate on qualifying income.

---

## Step 5: Taxable Income Computation [T1/T2]

**Legislation:** Federal Decree-Law No. 47 of 2022, Articles 20-33

### Computation Structure [T1]

```
  Accounting income per financial statements (IFRS or applicable standards)
+/- Adjustments required by the CT Law
- Exempt income (qualifying dividends, capital gains on qualifying participations)
+ Non-deductible expenditure (Step 6)
- Carry-forward tax losses utilised (up to 75% of taxable income)
= Taxable income
- AED 375,000 nil rate band
= Amount subject to 9%
x 9%
= Corporate tax payable
```

### Key Rules [T1]

- Starting point is the **accounting profit** per financial statements prepared under IFRS or other acceptable standards.
- Revenue recognition follows the applicable accounting standard, not cash receipts.
- Only **realised gains and losses** are generally included (unless election made for unrealised gains/losses).
- **Loss carry-forward:** Tax losses can be carried forward indefinitely, but offset is limited to **75% of taxable income** in any given period. The remaining 25% is taxed.
- **No loss carry-back** is permitted.

---

## Step 6: Non-Deductible Expenditure [T1]

**Legislation:** Federal Decree-Law No. 47 of 2022, Articles 28-33; Ministerial Decision No. 73 of 2023

### Specifically Non-Deductible [T1]

| Expense | Treatment |
|---------|-----------|
| Fines and penalties (government-imposed) | Fully non-deductible |
| Bribes and corrupt payments | Fully non-deductible |
| Donations and grants (non-qualifying) | Non-deductible unless to a qualifying public benefit entity listed by Cabinet Decision |
| Entertainment expenditure | 50% non-deductible (only 50% is allowed) |
| Personal expenses of the owner/shareholder | Fully non-deductible |
| Income tax or corporate tax payments | Non-deductible |
| Dividends or profit distributions | Not an expense |
| Provisions for doubtful debts (general) | Non-deductible until specifically written off |
| Related party payments without arm's length basis | Non-deductible to the extent exceeding arm's length amount |
| Interest exceeding the thin capitalisation limit | Non-deductible (net interest capped at 30% of EBITDA or AED 12M, whichever is higher) |

### Deductible Expenses [T1]

| Expense | Treatment |
|---------|-----------|
| Staff salaries and benefits | Fully deductible |
| Rent (business premises) | Fully deductible |
| Utilities (business) | Fully deductible |
| Professional fees (accounting, legal) | Fully deductible |
| Marketing and advertising | Fully deductible |
| Travel (business purpose) | Fully deductible |
| Insurance (business) | Fully deductible |
| Depreciation (per accounting standards) | Deductible (follows accounting treatment unless specified otherwise) |
| Bad debts (specifically written off) | Deductible when specifically identified and written off |
| Entertainment expenditure | 50% deductible |
| Qualifying donations | Deductible (to listed public benefit entities) |
| Interest (within thin capitalisation limits) | Deductible |

---

## Step 7: Transfer Pricing [T2]

**Legislation:** Federal Decree-Law No. 47 of 2022, Articles 34-36; Ministerial Decision No. 97 of 2023

### Arm's Length Principle [T2]

- All transactions with **Related Parties** and **Connected Persons** must be conducted at arm's length (i.e., as if between independent parties).
- Related parties include: family members (up to 4th degree), entities with 50%+ common ownership, directors, and their close relatives.
- If a transaction is not at arm's length, the FTA may adjust the taxable income accordingly.

### Documentation Requirements [T2]

| Requirement | Threshold | Details |
|------------|-----------|---------|
| Master File | Revenue > AED 3.15 billion (MNE group) | Group-wide transfer pricing information |
| Local File | Revenue > AED 200 million OR related party transactions > AED 40 million | Entity-specific transfer pricing documentation |
| Disclosure Form | All taxpayers with related party transactions | Filed with the CT return |
| Country-by-Country Report | Group revenue > AED 3.15 billion | Filed by the ultimate parent entity |

**For freelancers and sole establishments:** Transfer pricing is most relevant when transacting with family-owned entities or providing services to a company the freelancer also owns. [T2] Flag for reviewer if any related party transactions exist.

---

## Step 8: Registration Requirements [T1]

**Legislation:** Federal Decree-Law No. 47 of 2022; Federal Decree-Law No. 28 of 2022 (Tax Procedures)

### Who Must Register [T1]

| Entity Type | Must Register? |
|-------------|---------------|
| UAE-incorporated companies (mainland) | Yes -- regardless of revenue |
| Free zone companies | Yes -- regardless of revenue |
| Sole establishments / freelancers (licensed) | Yes -- if turnover exceeds AED 1,000,000 |
| Natural persons conducting business (unlicensed) | Yes -- if turnover exceeds AED 1,000,000 |
| Foreign companies with UAE permanent establishment | Yes |
| Individuals earning only employment income | No |

### Registration Process [T1]

- Register through the **EmaraTax portal** (tax.gov.ae).
- Obtain a **Tax Registration Number (TRN)**.
- Registration deadline: as per FTA timeline notices (staggered by licence issuance date). Check FTA announcements for applicable deadlines.
- Failure to register on time attracts a penalty of AED 10,000.

---

## Step 9: Filing Deadlines [T1]

**Legislation:** Federal Decree-Law No. 47 of 2022, Article 48; Federal Decree-Law No. 28 of 2022

| Filing / Payment | Deadline |
|-----------------|----------|
| Corporate tax return | Within **9 months** after the end of the relevant tax period (financial year end) |
| Payment of corporate tax due | Same deadline as the return (within 9 months after FY end) |
| Tax registration | As per FTA schedule (check for entity-specific deadlines) |

### Examples [T1]

| Financial Year End | Filing & Payment Deadline |
|-------------------|--------------------------|
| 31 December 2024 | 30 September 2025 |
| 31 March 2025 | 31 December 2025 |
| 30 June 2025 | 31 March 2026 |
| 31 December 2025 | 30 September 2026 |

**No provisional tax / instalment system.** Tax is paid in full with the return.

---

## Step 10: Penalties [T1]

**Legislation:** Cabinet Decision No. 75 of 2023

| Offence | Penalty |
|---------|---------|
| Failure to register on time | AED 10,000 |
| Late filing of CT return | AED 500 per month (from the month following the due date), up to a maximum (check current FTA guidance) |
| Late payment of tax | Monthly penalty of 14% per annum on the outstanding amount (approximately 1.17% per month) |
| Failure to maintain records | AED 10,000 (first offence), AED 20,000 (repeat within 24 months) |
| Filing an incorrect return | Fixed penalty + percentage of the tax difference |
| Failure to notify FTA of changes | AED 1,000 -- AED 5,000 |
| Tax evasion | Criminal penalties under UAE law |

---

## Step 11: Record Keeping [T1]

**Legislation:** Federal Decree-Law No. 47 of 2022, Article 56

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 7 years from the end of the relevant tax period |
| What to keep | Financial statements, accounting records, supporting documents, contracts, invoices, bank statements, transfer pricing documentation |
| Format | Paper or digital (FTA accepts digital records) |
| Audited financial statements | Required for QFZPs; recommended for all taxpayers |
| Language | Arabic is required for official filings; supporting documents can be in English (FTA may request Arabic translations) |

---

## Step 12: Edge Case Registry

### EC1 -- Freelancer with revenue under AED 1,000,000 [T1]
**Situation:** Natural person freelancer earns AED 800,000 from freelance software development.
**Resolution:** Below the AED 1,000,000 threshold for natural persons. Not subject to corporate tax for this period. No registration required. However, if revenue is expected to exceed AED 1,000,000 in future periods, advise early registration.

### EC2 -- Small business relief not elected [T1]
**Situation:** Sole establishment has revenue of AED 2,500,000 and taxable income of AED 600,000. Files return but does not elect SBR.
**Resolution:** Without the election, tax is calculated normally: (600,000 - 375,000) x 9% = AED 20,250. The client should have elected SBR to pay AED 0. SBR is NOT automatic -- it must be actively elected on the CT return. Amend the return if within the allowed period.

### EC3 -- Entertainment expenses fully deducted [T1]
**Situation:** Business deducts AED 50,000 entertainment expenses in full.
**Resolution:** INCORRECT. Only 50% (AED 25,000) is deductible. Add back AED 25,000 to taxable income.

### EC4 -- Personal expenses included in business costs [T1]
**Situation:** Sole establishment owner includes personal car lease (AED 36,000/year), personal phone bill (AED 6,000/year), and family vacation (AED 15,000) in business expenses.
**Resolution:** All personal expenses are non-deductible. Remove AED 57,000 from deductions. If the car and phone are partially used for business, only the business portion is deductible [T2] -- flag for reviewer to determine reasonable business-use percentage.

### EC5 -- Free zone company earning revenue from mainland individuals [T2]
**Situation:** Free zone IT consultancy earns 40% of revenue from individual clients (natural persons) on the mainland.
**Resolution:** Revenue from transactions with natural persons is non-qualifying income. If non-qualifying revenue exceeds 5% of total revenue (or AED 5M, whichever is lower), the entire QFZP status is at risk. At 40%, the de minimis threshold is breached. The company likely cannot qualify as a QFZP. All income would be subject to the standard 0%/9% regime. [T2] Flag for reviewer.

### EC6 -- Loss carry-forward with SBR claim [T1]
**Situation:** Business had a tax loss in 2024 and claims SBR for 2025.
**Resolution:** Tax losses from a prior period CANNOT be utilised in a year where SBR is elected (because taxable income is deemed nil). Also, no new tax losses can arise in an SBR year. The prior losses remain available for use in future non-SBR periods.

### EC7 -- Related party payment without arm's length pricing [T2]
**Situation:** Freelancer pays AED 120,000 annual "management fee" to a company owned by their spouse for unspecified services.
**Resolution:** Related party transaction. Must be at arm's length. If the fee exceeds what an independent third party would charge for the same services (or no genuine services are provided), the FTA may disallow the deduction. [T2] Flag for reviewer: confirm the nature and market rate of the services.

### EC8 -- Registration not done despite being required [T1]
**Situation:** Sole establishment has been operating since 2023 with revenue over AED 2,000,000. Never registered for corporate tax.
**Resolution:** The business is required to register. Failure to register on time incurs a penalty of AED 10,000. Advise immediate registration through EmaraTax. Past-due returns must be filed. Late filing and payment penalties will also apply. Escalate to a licensed tax agent for remediation.

### EC9 -- Net interest exceeding thin capitalisation limit [T2]
**Situation:** Business has net interest expense of AED 15,000,000. EBITDA is AED 30,000,000.
**Resolution:** Net interest deduction is capped at the greater of 30% of EBITDA (AED 9,000,000) or AED 12,000,000. Cap = AED 12,000,000. Disallow AED 3,000,000 (15M - 12M). The disallowed interest can be carried forward for up to 10 years. [T2] Flag for reviewer.

### EC10 -- No personal income tax confirmation [T1]
**Situation:** Employee earning AED 500,000 salary asks if they need to pay income tax.
**Resolution:** NO. The UAE does not impose personal income tax on employment income, investment income, or other personal income. Corporate tax only applies to business activities. Salary and wages are not subject to any income tax in the UAE.

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: UAE-licensed tax agent must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to UAE-licensed tax agent. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard sole establishment, above threshold
**Input:** Mainland sole establishment, revenue AED 2,000,000, allowable expenses AED 1,200,000 (all qualifying), no entertainment, no related party transactions. Does not elect SBR.
**Expected output:** Taxable income = 2,000,000 - 1,200,000 = 800,000. Tax = (800,000 - 375,000) x 9% = AED 38,250.

### Test 2 -- Small business relief elected
**Input:** Sole establishment, revenue AED 2,500,000, taxable income AED 500,000. Elects SBR.
**Expected output:** Taxable income deemed nil. Corporate tax = AED 0. No losses created or carried forward.

### Test 3 -- Revenue exceeds SBR threshold
**Input:** Freelancer, revenue AED 3,500,000, expenses AED 2,000,000.
**Expected output:** Revenue exceeds AED 3,000,000. SBR not available. Taxable income = 1,500,000. Tax = (1,500,000 - 375,000) x 9% = AED 101,250.

### Test 4 -- Entertainment expense partially disallowed
**Input:** Business expenses include AED 40,000 entertainment.
**Expected output:** Only AED 20,000 deductible. AED 20,000 added back to taxable income.

### Test 5 -- Loss carry-forward with 75% cap
**Input:** Prior year tax loss of AED 500,000. Current year taxable income (before loss offset) = AED 400,000.
**Expected output:** Maximum loss offset = 75% of 400,000 = AED 300,000. Taxable income after offset = 100,000. Tax = (100,000 - 375,000) = negative, so within 0% band. Tax = AED 0. Remaining loss to carry forward = 500,000 - 300,000 = AED 200,000.

### Test 6 -- Freelancer below AED 1,000,000 threshold
**Input:** Natural person freelancer, revenue AED 750,000.
**Expected output:** Below AED 1,000,000 threshold for natural persons. Not subject to corporate tax. No registration required.

### Test 7 -- Filing deadline calculation
**Input:** Financial year ends 31 December 2025.
**Expected output:** CT return and payment due by 30 September 2026 (9 months after FY end).

---

## PROHIBITIONS

- NEVER state that the UAE has personal income tax -- it does not
- NEVER apply corporate tax to natural persons with turnover below AED 1,000,000
- NEVER assume small business relief is automatic -- the election must be actively made on the return
- NEVER allow SBR and QFZP benefits simultaneously for the same entity
- NEVER allow entertainment expenses to be deducted at more than 50%
- NEVER allow personal expenses as business deductions
- NEVER allow fines, penalties, or bribes as deductions
- NEVER allow related party payments without confirming arm's length pricing
- NEVER offset more than 75% of taxable income with carried-forward losses
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their tax agent for confirmation
- NEVER advise on group structures, permanent establishment, or multinational Pillar Two rules without escalating [T3]
- NEVER forget that filing and registration are mandatory even if no tax is due

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a UAE-licensed tax agent or equivalent practitioner) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
