---
name: ke-income-tax
description: Use this skill whenever asked about Kenyan income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "KRA", "iTax", "income tax return", "personal relief", "insurance relief", "turnover tax", "presumptive tax", "self-employed tax Kenya", or any question about filing or computing income tax for a self-employed or sole proprietor client in Kenya. This skill covers progressive rates (10-35%), personal relief (KES 28,800), insurance relief, turnover tax, presumptive tax, instalment tax, penalties, and interaction with VAT. ALWAYS read this skill before touching any Kenyan income tax work.
---

# Kenya Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Kenya |
| Jurisdiction Code | KE |
| Primary Legislation | Income Tax Act, Chapter 470 (Laws of Kenya) |
| Supporting Legislation | Tax Procedures Act 2015; Finance Act 2023 (turnover tax amendments); Finance Act 2024 |
| Tax Authority | Kenya Revenue Authority (KRA) |
| Filing Portal | iTax (itax.kra.go.ke) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Kenyan CPA or registered tax agent |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, personal relief, insurance relief, turnover tax eligibility, instalment tax schedule. Tier 2: mixed-use expense apportionment, home office, capital allowances (industrial building, wear-and-tear). Tier 3: withholding tax on cross-border payments, transfer pricing, capital gains tax on property, extractive industry taxation. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified CPA must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Residency status** [T1] -- resident vs non-resident; this skill covers residents only
2. **Nature of trade** [T1] -- type of self-employment (determines whether turnover tax / presumptive tax is available)
3. **Gross annual income from self-employment** [T1] -- total receipts from trade
4. **Business expenses** [T1/T2] -- nature and amount (T2 for mixed-use items)
5. **Life / health / education insurance premiums paid** [T1] -- for insurance relief computation
6. **Instalment tax payments** [T1] -- amounts paid during the year
7. **Other income** [T1] -- employment (PAYE), rental, interest, dividends
8. **NSSF / SHIF contributions** [T1] -- mandatory social contributions
9. **PIN number** [T1] -- for iTax filing identification

**If residency status is unknown, STOP. Non-residents are taxed at flat 30% on Kenya-source income. Residency is mandatory.**

---

## Step 1: Determine Applicable Rate Table [T1]

**Legislation:** Income Tax Act, Cap 470, Third Schedule (as amended by Finance Act 2023)

### Resident Individual Progressive Tax Table (Annual)

| Taxable Income (KES/year) | Monthly Equivalent | Rate |
|--------------------------|-------------------|------|
| 0 -- 288,000 | 0 -- 24,000 | 10% |
| 288,001 -- 388,000 | 24,001 -- 32,333 | 25% |
| 388,001 -- 6,000,000 | 32,334 -- 500,000 | 30% |
| 6,000,001 -- 9,600,000 | 500,001 -- 800,000 | 32.5% |
| 9,600,001+ | 800,001+ | 35% |

### Non-Resident Rate [T1]

Non-residents: flat 30% on all Kenya-source income. No personal relief. This skill does not cover non-residents further.

### Personal Relief [T1]

| Relief | Amount (Annual) | Amount (Monthly) |
|--------|----------------|-----------------|
| Personal relief | KES 28,800 | KES 2,400 |

Personal relief is a credit against tax (not a deduction from income). Available to all resident individuals.

---

## Step 2: Self-Assessment Return Computation Structure [T1]

**Legislation:** Income Tax Act, s15-s16; Tax Procedures Act

| Step | Description | How to Populate |
|------|-------------|-----------------|
| A | Gross income from business/trade | Total self-employment receipts |
| B | Less: Allowable deductions | Expenses wholly and exclusively incurred in production of income |
| C | Net business income | A minus B |
| D | Add: Other income | Employment (net of PAYE), rental, interest, dividends |
| E | Total income | C plus D |
| F | Less: Allowable deductions from total income | Contributions to registered pension/provident, owner-occupied interest |
| G | Taxable income | E minus F |
| H | Tax per rate table | Apply progressive rates to G |
| I | Less: Personal relief | KES 28,800 |
| J | Less: Insurance relief | 15% of qualifying premiums (max KES 60,000/year) |
| K | Less: Instalment tax paid | Quarterly instalment payments |
| L | Less: Withholding tax credits | WHT deducted at source on payments received |
| M | Tax due / (refund) | H minus I minus J minus K minus L |

---

## Step 3: Allowable Deductions [T1/T2]

**Legislation:** Income Tax Act, s15 -- "wholly and exclusively incurred in the production of income"

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated business premises) | T1 | Fully deductible |
| Professional insurance | T1 | Fully deductible |
| Accounting / audit fees | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions (business) | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Staff salaries and wages | T1 | Fully deductible |
| Travel (business purpose) | T1 | Fully deductible if wholly business |
| Bad debts (previously included in income) | T2 | Flag for reviewer -- confirm irrecoverable |
| Motor vehicle expenses | T2 | Business portion only |
| Home office | T2 | Proportional -- dedicated space required |
| Repairs and maintenance (business assets) | T1 | Fully deductible |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal / domestic expenses | Not in production of income |
| Capital expenditure | Through capital deductions / wear-and-tear, not direct |
| Income tax | Tax on income not deductible |
| Entertainment (not wholly business) | Must prove wholly and exclusively for business |
| Provisions (general) | Only specific, quantified liabilities |

### Capital Deductions (Wear and Tear) [T1]

**Legislation:** Income Tax Act, Second Schedule

| Asset | Annual Rate |
|-------|------------|
| Heavy / self-propelling machinery | 37.5% (reducing balance) |
| Motor vehicles | 25% (reducing balance) |
| Computer and IT equipment | 30% (reducing balance) |
| Furniture and fittings | 12.5% (reducing balance) |
| Farm machinery | 100% (year of first use) |

Kenya uses the **reducing balance** method (not straight-line) for most assets.

---

## Step 4: Insurance Relief [T1]

**Legislation:** Income Tax Act, s31

| Rule | Detail |
|------|--------|
| Qualifying premiums | Life insurance, education policy, health/medical insurance |
| Relief rate | 15% of qualifying premiums paid |
| Annual cap | KES 60,000 per year (KES 5,000 per month) |
| Who qualifies | Resident individual paying premiums for self, spouse, or child |

**Insurance relief is a credit against tax, not a deduction from income.**

---

## Step 5: Instalment Tax [T1]

**Legislation:** Income Tax Act, s12

### Instalment Schedule

| Instalment | Deadline | Amount |
|-----------|----------|--------|
| 1st | 20th day of 4th month of accounting period | 25% of estimated tax |
| 2nd | 20th day of 6th month | 25% |
| 3rd | 20th day of 9th month | 25% |
| 4th | 20th day of 12th month | 25% |

For calendar year taxpayers: 20 April, 20 June, 20 September, 20 December.

### Rules [T1]

- Based on **estimated** current year tax liability (may also use prior year actual as safe harbour)
- If prior year tax < KES 40,000, instalment tax is not required
- Under-estimation penalty: 20% of the difference if estimate is less than 110% of actual
- Self-employed individuals must register as instalment taxpayers

---

## Step 6: Turnover Tax (TOT) Option [T1]

**Legislation:** Income Tax Act, s12C (as amended by Finance Act 2023)

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Annual gross turnover | Between KES 1,000,000 and KES 25,000,000 |
| Entity type | Resident person carrying on business |
| Exclusions | Management / professional services, rental income, employment income |

### Rate [T1]

| Detail | Value |
|--------|-------|
| TOT rate | 1.5% of gross turnover (Finance Act 2023 amendment from 1% effective 1 July 2023 -- verify current rate with KRA) |
| Filing | Monthly, by 20th of following month |
| Replaces | Income tax (but not VAT if VAT-registered) |

### Key Points [T1]

- No deductions for expenses -- tax is on gross turnover
- Cannot claim capital allowances or other deductions
- Businesses below KES 1,000,000 may opt for presumptive tax instead
- [T2] Flag for reviewer: confirm whether TOT is more favourable than normal tax after deductions

---

## Step 7: Presumptive Tax [T1]

**Legislation:** Income Tax Act, s12D

| Condition | Requirement |
|-----------|-------------|
| Annual turnover | Below KES 1,000,000 |
| Eligible businesses | Specified in Third Schedule Part I (e.g., certain retail, transport) |
| Amount | KES 15,000 per year |

Presumptive tax is a final tax -- no further income tax obligation for qualifying income.

---

## Step 8: Filing and Deadlines [T1]

**Legislation:** Income Tax Act, s52B; Tax Procedures Act

| Filing / Payment | Deadline |
|-----------------|----------|
| Annual self-assessment return | 30 June of following year |
| Instalment tax (quarterly) | 20th day of 4th, 6th, 9th, 12th months |
| TOT monthly returns | 20th of following month |
| Amended return | Within 12 months of original filing |

All filing via **iTax** portal (itax.kra.go.ke).

---

## Step 9: Penalties [T1]

**Legislation:** Tax Procedures Act 2015, s72-s85

| Offence | Penalty |
|---------|---------|
| Late filing of return | 5% of tax due or KES 20,000, whichever is higher |
| Late payment of tax | 5% of tax due + 1% per month compound interest |
| Under-estimation of instalment tax | 20% of the shortfall |
| Failure to keep records | KES 100,000 per month (up to KES 1,000,000) |
| Fraudulent return | Double the tax evaded + criminal prosecution |

---

## Step 10: Record Keeping [T1]

**Legislation:** Tax Procedures Act, s23

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from end of the relevant year |
| What to keep | Invoices, receipts, bank statements, contracts, asset register |
| Format | Paper or electronic (KRA accepts both) |
| Language | English or Swahili |

---

## Step 11: Edge Case Registry

### EC1 -- Personal relief applied as deduction instead of credit [T1]
**Situation:** Client deducts KES 28,800 from taxable income before applying tax rates.
**Resolution:** INCORRECT. Personal relief is a credit against calculated tax, not a deduction from income. Apply tax rates first, then subtract KES 28,800 from the tax amount.

### EC2 -- Insurance relief exceeds cap [T1]
**Situation:** Client pays KES 500,000 in health insurance premiums. Claims 15% = KES 75,000 relief.
**Resolution:** Cap at KES 60,000. Relief = min(15% x KES 500,000, KES 60,000) = KES 60,000.

### EC3 -- Turnover tax elected by professional services provider [T1]
**Situation:** Freelance consultant with KES 5M turnover elects TOT.
**Resolution:** NOT eligible. Professional and management services are excluded from TOT. Must use normal income tax system.

### EC4 -- Below KES 1M turnover choosing between presumptive and normal tax [T2]
**Situation:** Small retail trader with KES 800,000 turnover and KES 600,000 expenses.
**Resolution:** Normal tax: (800,000 - 600,000) = 200,000 taxable. Tax = 10% x 200,000 = 20,000 - 28,800 relief = KES 0 (below relief). Presumptive tax: KES 15,000. Normal tax is more favourable. [T2] Flag for reviewer to confirm expense documentation.

### EC5 -- Withholding tax on professional fees not credited [T1]
**Situation:** Client received KES 1,000,000 for consultancy but only KES 950,000 was deposited (5% WHT deducted).
**Resolution:** Gross income = KES 1,000,000. WHT of KES 50,000 is a credit against final tax. Must be shown in Step L of computation. Client needs WHT certificates for iTax filing.

### EC6 -- SHIF and NSSF deductibility [T1]
**Situation:** Self-employed client pays SHIF (2.75% of income) and NSSF contributions. Wants to deduct both.
**Resolution:** NSSF contributions to registered provident fund are deductible (up to statutory limit). SHIF contributions are NOT deductible for income tax -- they are a separate health levy.

### EC7 -- Capital gain on sale of business asset [T3]
**Situation:** Client sells business vehicle at a profit.
**Resolution:** ESCALATE. Kenya re-introduced capital gains tax at 15% on property transfers (effective 2023). Treatment of business asset disposal depends on whether it qualifies as a capital gain or trading income. Refer to tax practitioner.

### EC8 -- Non-resident earning Kenya-source consulting income [T1]
**Situation:** Non-resident consultant invoices Kenyan client KES 2,000,000.
**Resolution:** Subject to 20% withholding tax on management/professional fees (or treaty rate). The Kenyan payer must withhold and remit to KRA. This is a final tax for the non-resident. ESCALATE for treaty analysis if applicable [T3].

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
Action Required: Kenyan CPA or registered tax agent must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Kenyan CPA or tax agent. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** Resident, gross revenue KES 3,000,000, allowable expenses KES 1,200,000, insurance premiums KES 100,000, instalment tax paid KES 150,000.
**Expected output:** Taxable income = KES 1,800,000. Tax = 10% x 288,000 + 25% x 100,000 + 30% x (1,800,000 - 388,000) = 28,800 + 25,000 + 423,600 = KES 477,400. Less personal relief 28,800. Less insurance relief min(15,000, 60,000) = 15,000. Net tax = 477,400 - 28,800 - 15,000 = KES 433,600. Less instalment tax 150,000. Tax due = KES 283,600.

### Test 2 -- Below personal relief threshold
**Input:** Resident, taxable income KES 200,000, no insurance, no instalment tax.
**Expected output:** Tax = 10% x 200,000 = KES 20,000. Less personal relief KES 28,800. Tax payable = KES 0 (relief exceeds tax).

### Test 3 -- Turnover tax computation
**Input:** Resident trader (non-professional), gross turnover KES 8,000,000. Elected TOT.
**Expected output:** TOT = 1.5% x KES 8,000,000 = KES 120,000 per year (KES 10,000 per month).

### Test 4 -- Insurance relief at cap
**Input:** Client pays KES 600,000 in qualifying premiums.
**Expected output:** Relief = 15% x 600,000 = 90,000 but cap is KES 60,000. Insurance relief = KES 60,000.

### Test 5 -- High earner hitting top bracket
**Input:** Taxable income KES 12,000,000, instalment tax paid KES 2,500,000.
**Expected output:** Tax = 28,800 + 25,000 + (6,000,000 - 388,000) x 30% + (9,600,000 - 6,000,000) x 32.5% + (12,000,000 - 9,600,000) x 35% = 28,800 + 25,000 + 1,683,600 + 1,170,000 + 840,000 = KES 3,747,400. Less relief 28,800. Net tax = 3,718,600. Less instalment 2,500,000. Due = KES 1,218,600.

### Test 6 -- Presumptive tax vs normal tax
**Input:** Small trader, turnover KES 500,000, expenses KES 350,000.
**Expected output:** Normal tax: profit KES 150,000. Tax = 10% x 150,000 = 15,000 - 28,800 relief = KES 0. Presumptive: KES 15,000. Normal tax is more favourable (KES 0 vs KES 15,000).

---

## PROHIBITIONS

- NEVER apply personal relief as a deduction from income -- it is a credit against tax
- NEVER allow turnover tax for professional or management service providers
- NEVER allow insurance relief above KES 60,000 per year
- NEVER compute tax for non-residents using progressive rates -- non-residents pay flat 30%
- NEVER allow capital expenditure as a direct expense deduction -- use wear-and-tear (Second Schedule)
- NEVER ignore withholding tax certificates -- they are credits against final tax
- NEVER treat SHIF contributions as deductible for income tax purposes
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a Kenyan CPA for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA(K), registered tax agent, or equivalent licensed practitioner in Kenya) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
