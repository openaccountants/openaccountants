---
name: ng-income-tax
description: Use this skill whenever asked about Nigerian personal income tax for self-employed individuals. Trigger on phrases like "Nigeria income tax", "PITA", "FIRS", "self-assessment Nigeria", "progressive tax Nigeria", "minimum tax Nigeria", "consolidated relief", or any question about computing or filing income tax for sole proprietors in Nigeria. Covers progressive rates (7-24%), minimum tax (1% of gross income), consolidated relief allowance, and self-assessment filing. ALWAYS read this skill before touching any Nigerian income tax work.
---

# Nigeria Personal Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Nigeria |
| Jurisdiction Code | NG |
| Primary Legislation | Personal Income Tax Act (PITA), Cap P8 LFN 2004, as amended by Finance Act 2020, 2021, 2023 |
| Supporting Legislation | Federal Inland Revenue Service (Establishment) Act; Companies Income Tax Act (CITA) for companies |
| Tax Authority | Federal Inland Revenue Service (FIRS) -- for FCT residents; State Internal Revenue Service (SIRS) -- for state residents |
| Filing Portal | TaxPro Max (taxpromax.firs.gov.ng) for FIRS; state portals vary |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Nigerian chartered accountant (ICAN fellow or ANAN member) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: progressive rate table, consolidated relief, minimum tax, filing deadlines. Tier 2: business expense deductions, capital allowances. Tier 3: transfer pricing, petroleum profits tax, international tax treaties. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Residency status** [T1] -- resident vs non-resident (this skill covers residents only)
2. **State of residence** [T1] -- determines whether to file with FIRS (FCT) or state IRS
3. **Gross income from self-employment** [T1] -- total business receipts
4. **Business expenses** [T1/T2] -- nature and amount
5. **Other income** [T1] -- employment, investment, rental
6. **Life insurance premiums and pension contributions** [T1] -- for relief computation
7. **National Housing Fund contributions** [T1]
8. **Tax Identification Number (TIN)** [T1]

**If residency status is unknown, STOP. Non-residents are taxed differently under PITA.**

---

## Step 1: Progressive Tax Rates [T1]

**Legislation:** PITA, Sixth Schedule (as amended by Finance Act 2020)

### Resident Individual Tax Table [T1]

| Taxable Income (NGN) | Rate |
|----------------------|------|
| First 300,000 | 7% |
| Next 300,000 (300,001 -- 600,000) | 11% |
| Next 500,000 (600,001 -- 1,100,000) | 15% |
| Next 500,000 (1,100,001 -- 1,600,000) | 19% |
| Next 1,600,000 (1,600,001 -- 3,200,000) | 21% |
| Above 3,200,000 | 24% |

---

## Step 2: Consolidated Relief Allowance (CRA) [T1]

**Legislation:** PITA, s 33(1), as amended by Finance Act 2020

| Component | Amount |
|-----------|--------|
| Higher of: NGN 200,000 or 1% of gross income | Base relief |
| Plus: 20% of gross income | Additional relief |
| **CRA Total** | **Higher of (200,000 or 1% of GI) + 20% of GI** |

### CRA Calculation [T1]

CRA = max(NGN 200,000, 1% x Gross Income) + 20% x Gross Income

The CRA replaced the previous system of personal allowance + children's allowance + dependent relative allowance.

---

## Step 3: Other Reliefs and Deductions [T1]

**Legislation:** PITA, s 33

| Relief | Amount / Rule |
|--------|--------------|
| Pension contribution (employee/self-employed) | Actual contribution to approved pension scheme (min 8% of basic + housing + transport per PRA 2014) |
| National Housing Fund | 2.5% of basic salary (for employees; self-employed may contribute voluntarily) |
| Life insurance premium | Actual premium paid on own life |
| National Health Insurance | Actual premium paid |
| Gratuities | Tax-exempt if from approved scheme |

### Business Expense Deductions [T1/T2]

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent | T1 | Fully deductible |
| Professional fees | T1 | Fully deductible |
| Staff salaries | T1 | Fully deductible |
| Depreciation (capital allowances) | T1 | Per Fifth Schedule |
| Marketing and advertising | T1 | Fully deductible |
| Motor vehicle (business use) | T2 | Business portion only; flag mixed use |
| Home office | T2 | Proportional; flag for reviewer |

---

## Step 4: Capital Allowances [T1]

**Legislation:** PITA, Fifth Schedule

| Asset | Initial Allowance | Annual Allowance |
|-------|-------------------|-----------------|
| Building (industrial) | 15% | 10% |
| Motor vehicles | 50% | 25% |
| Plant and machinery | 50% | 25% |
| Furniture and fittings | 25% | 20% |
| Computer equipment | 50% | 25% |

Capital allowances are claimed in lieu of depreciation. Initial allowance is claimed in the year of first use. Annual allowance is on a straight-line basis on the residual value.

---

## Step 5: Computation Structure [T1]

| Step | Description | How to Populate |
|------|-------------|-----------------|
| A | Gross income from business | Total self-employment receipts |
| B | Less: Allowable business deductions | Expenses wholly, reasonably, exclusively, and necessarily incurred |
| C | Assessable income | A minus B |
| D | Add: Other income | Investment income, rental, etc. |
| E | Gross total income | C plus D |
| F | Less: Consolidated Relief Allowance | max(200,000, 1% x E) + 20% x E |
| G | Less: Other reliefs | Pension, NHF, life insurance |
| H | Taxable income | E minus F minus G |
| I | Tax per rate table | Apply progressive rates to H |
| J | Compare with minimum tax | 1% of gross income |
| K | Tax payable | Higher of I and J |
| L | Less: WHT credits | Withholding tax deducted at source |
| M | Tax due / (refund) | K minus L |

---

## Step 6: Minimum Tax [T1]

**Legislation:** PITA, s 37, as amended by Finance Act 2020

| Rule | Detail |
|------|--------|
| Minimum tax rate | **1% of gross income** |
| When it applies | When computed tax (per progressive rates) is LESS than minimum tax |
| Exemption | Employers with less than NGN 30M turnover (for CIT); for PITA, minimum tax applies to all |
| Effect | Taxpayer pays the HIGHER of computed tax or minimum tax |

**Note:** Finance Act 2020 simplified minimum tax from the previous complex formula to a flat 1% of gross income.

---

## Step 7: Filing and Payment [T1]

**Legislation:** PITA, s 41-44; Tax Procedures Act

| Item | Detail |
|------|--------|
| Filing deadline | **31 March** of the following year (self-assessment) |
| Payment deadline | Same as filing deadline |
| Method | TaxPro Max (FIRS) or state portal |
| Self-assessment | Self-employed persons file self-assessment returns |
| Withholding tax | 10% WHT on professional fees, 5% on contracts |

---

## Step 8: Penalties [T1]

**Legislation:** PITA, s 94-100

| Offence | Penalty |
|---------|---------|
| Late filing | NGN 50,000 for first month + NGN 25,000 per subsequent month |
| Late payment | 10% of tax due + interest at CBN MPR + spread |
| Failure to keep records | NGN 50,000 fine |
| Wilful tax evasion | NGN 20,000 fine or 3 years imprisonment or both |
| Incorrect return (without fraud) | Penalty of twice the difference |

---

## Step 9: Edge Case Registry

### EC1 -- Minimum tax exceeds computed tax [T1]
**Situation:** Freelancer with NGN 15,000,000 gross income but NGN 13,000,000 expenses. Taxable income = NGN 2,000,000 after CRA.
**Resolution:** Computed tax on NGN 2,000,000 ~ NGN 259,000. Minimum tax = 1% x 15,000,000 = NGN 150,000. Computed tax is higher, so pay computed tax. If expenses were higher and taxable income lower, minimum tax would apply.

### EC2 -- Multiple sources of income [T1]
**Situation:** Client has self-employment income and rental income.
**Resolution:** Aggregate all income. Apply CRA and reliefs to total gross income. Apply progressive rates to final taxable income.

### EC3 -- Withholding tax on professional fees [T1]
**Situation:** Consultant receives NGN 5,000,000 payment, client withholds 10% (NGN 500,000).
**Resolution:** Gross income = NGN 5,000,000. WHT of NGN 500,000 is a credit against final tax liability. Must obtain WHT certificate (credit note) for filing.

### EC4 -- Non-resident earning Nigeria-source income [T1]
**Situation:** Non-resident freelancer invoices Nigerian client.
**Resolution:** Subject to WHT as final tax (10% on professional/technical services). Payer must withhold and remit. This skill does not cover non-resident taxation further. [T3] for treaty analysis.

### EC5 -- CRA calculation with very low income [T1]
**Situation:** Gross income = NGN 500,000.
**Resolution:** CRA = max(200,000, 1% x 500,000 = 5,000) + 20% x 500,000 = 200,000 + 100,000 = NGN 300,000. Taxable income = 500,000 - 300,000 = NGN 200,000. Tax = 7% x 200,000 = NGN 14,000. Minimum tax = 1% x 500,000 = NGN 5,000. Pay NGN 14,000 (higher).

### EC6 -- Dual filing obligation (FIRS and state) [T2]
**Situation:** Client lives in Lagos but has business in FCT.
**Resolution:** PITA filing is based on residence. File with Lagos State IRS. [T2] Flag for reviewer if multiple states are involved or if the client has businesses in multiple jurisdictions.

---

## Step 10: Test Suite

### Test 1 -- Standard mid-range income
**Input:** Gross income NGN 8,000,000, allowable expenses NGN 3,000,000, pension contribution NGN 400,000, no WHT.
**Expected output:**
- Assessable income: NGN 5,000,000
- CRA: max(200,000, 80,000) + 20% x 8,000,000 = 200,000 + 1,600,000 = NGN 1,800,000
- Taxable income: 8,000,000 - 3,000,000 - 1,800,000 - 400,000 = NGN 2,800,000
- Tax: 7% x 300,000 + 11% x 300,000 + 15% x 500,000 + 19% x 500,000 + 21% x 1,200,000 = 21,000 + 33,000 + 75,000 + 95,000 + 252,000 = NGN 476,000
- Minimum tax: 1% x 8,000,000 = NGN 80,000
- Tax payable: NGN 476,000 (higher)

### Test 2 -- Low income, CRA wipes out tax
**Input:** Gross income NGN 600,000, expenses NGN 100,000, no pension.
**Expected output:**
- CRA: max(200,000, 6,000) + 20% x 600,000 = 200,000 + 120,000 = NGN 320,000
- Taxable income: 600,000 - 100,000 - 320,000 = NGN 180,000
- Tax: 7% x 180,000 = NGN 12,600
- Minimum tax: 1% x 600,000 = NGN 6,000
- Tax payable: NGN 12,600 (higher)

### Test 3 -- High earner, top bracket
**Input:** Gross income NGN 20,000,000, expenses NGN 5,000,000, pension NGN 800,000.
**Expected output:**
- CRA: max(200,000, 200,000) + 20% x 20,000,000 = 200,000 + 4,000,000 = NGN 4,200,000
- Taxable income: 20,000,000 - 5,000,000 - 4,200,000 - 800,000 = NGN 10,000,000
- Tax: 21,000 + 33,000 + 75,000 + 95,000 + 336,000 + (10,000,000 - 3,200,000) x 24% = 560,000 + 1,632,000 = NGN 2,192,000
- Minimum tax: 1% x 20,000,000 = NGN 200,000
- Tax payable: NGN 2,192,000

### Test 4 -- Minimum tax applicable
**Input:** Gross income NGN 10,000,000, expenses NGN 9,000,000, pension NGN 500,000.
**Expected output:**
- CRA: 200,000 + 2,000,000 = NGN 2,200,000
- Taxable income: 10,000,000 - 9,000,000 - 2,200,000 - 500,000 = max(0, -1,700,000) = NGN 0
- Computed tax: NGN 0
- Minimum tax: 1% x 10,000,000 = NGN 100,000
- Tax payable: NGN 100,000 (minimum tax)

---

## PROHIBITIONS

- NEVER apply the old personal allowance / children's allowance system -- CRA replaced it from 2020
- NEVER ignore minimum tax -- it is a floor; always compare computed tax vs 1% of gross income
- NEVER deduct capital expenditure directly -- use capital allowances (Fifth Schedule)
- NEVER file with the wrong authority -- FIRS for FCT residents, state IRS for all others
- NEVER compute CRA on net income -- it is based on GROSS income
- NEVER ignore withholding tax certificates -- they are credits against final tax
- NEVER treat non-resident income under progressive rates -- different rules apply
- NEVER present calculations as definitive -- always label as estimated and direct client to an ICAN/ANAN member

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant (FCA/ACA) or accredited tax practitioner in Nigeria) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
