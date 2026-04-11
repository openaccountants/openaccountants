---
name: uk-income-tax-sa100
description: >
  Use this skill whenever asked about UK income tax for individuals filing SA100 Self Assessment. Trigger on phrases like "income tax UK", "SA100", "personal allowance", "tax bands", "tax computation", "marriage allowance", "savings allowance", "dividend allowance", "Scottish tax rates", "payments on account", "tax reducers", "tax relief", or any question about computing a UK individual's income tax liability. Covers personal allowance (including taper), income tax bands for rUK and Scotland, marriage allowance, savings and dividend allowances, tax reducers, the final tax computation, and payments on account. ALWAYS read this skill before touching any UK income tax return work.
version: 1.0
jurisdiction: GB
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
---

# UK Income Tax (SA100) -- Individual Tax Computation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Kingdom (England, Wales, Northern Ireland; Scottish rates for non-savings, non-dividend income of Scottish taxpayers) |
| Jurisdiction Code | GB |
| Primary Legislation | Income Tax Act 2007 (ITA 2007); Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003); Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005) |
| Supporting Legislation | Finance Act 2024; Finance Act 2025; Scotland Act 2016 (Scottish rate-setting power); Taxes Management Act 1970 (TMA 1970) |
| Tax Authority | HM Revenue & Customs (HMRC) |
| Filing Portal | HMRC Self Assessment Online |
| Contributor | Open Accountants Community |
| Validated By | [Pending -- requires sign-off by a UK-qualified accountant (ACA/ACCA/CTA)] |
| Validation Date | [Pending] |
| Skill Version | 1.0 |
| Tax Year | 2024/25 (6 April 2024 to 5 April 2025) |
| Confidence Coverage | Tier 1: personal allowance, income tax bands (rUK and Scotland), marriage allowance amount, savings allowance, dividend allowance, payment on account rules, filing deadlines, penalty structure. Tier 2: personal allowance taper computation at boundary, optimal marriage allowance election, interaction of multiple income sources, loss relief claims against total income. Tier 3: non-domiciled individuals, remittance basis, double taxation relief, trust income, complex pension relief. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Tax year** [T1] -- confirm 2024/25 (6 April 2024 to 5 April 2025)
2. **Residency status** [T1/T3] -- UK resident, non-resident, or split-year (T3 if non-resident or split-year)
3. **Scottish taxpayer** [T1] -- determines whether Scottish income tax rates apply to non-savings, non-dividend income
4. **Employment income** [T1] -- gross pay, benefits in kind (from P60/P45/P11D)
5. **Self-employment income** [T1] -- taxable trading profit from SA103 (see uk-self-employment-sa103 skill)
6. **Savings income** [T1] -- bank interest, building society interest, government bond interest
7. **Dividend income** [T1] -- dividends from UK and overseas companies
8. **Rental income** [T1] -- net property income from SA105
9. **Pension income** [T1] -- state pension, private pensions
10. **Other income** [T1] -- any other taxable income
11. **Pension contributions** [T1/T2] -- personal pension contributions (relief at source or net pay)
12. **Gift Aid donations** [T1] -- affects basic rate band extension
13. **Marriage allowance election** [T1] -- whether transferring or receiving GBP 1,260
14. **Tax already deducted at source** [T1] -- PAYE, tax deducted from savings, CIS deductions
15. **Payments on account already made** [T1] -- POA1 and POA2 for current year

**If residency status is unclear, STOP. Residency determines the entire tax computation basis.**

---

## Step 1: Income Categorisation [T1]

**Legislation:** ITA 2007, ss 6-22

Income must be classified into three categories. The order of taxation matters.

| Category | Priority | Examples | Taxed at |
|----------|----------|----------|----------|
| Non-savings income | First | Employment, self-employment, pensions, rental, trading | rUK rates or Scottish rates |
| Savings income | Second | Bank interest, building society interest, government bonds | UK savings rates |
| Dividend income | Third (top slice) | Company dividends (UK and overseas) | UK dividend rates |

**This ordering is mandatory.** Non-savings income fills the bands first, then savings income, then dividends sit on top.

---

## Step 2: Personal Allowance [T1]

**Legislation:** ITA 2007, s 35

### Standard Personal Allowance [T1]

| Item | Amount |
|------|--------|
| Personal allowance (2024/25) | GBP 12,570 |
| Frozen until | 2027/28 (confirmed) |

### Personal Allowance Taper [T1]

| Item | Value |
|------|-------|
| Taper threshold (adjusted net income) | GBP 100,000 |
| Taper rate | GBP 1 reduction for every GBP 2 of income above GBP 100,000 |
| Fully withdrawn at | GBP 125,140 |
| Effective marginal rate in taper zone | 60% (on income between GBP 100,000 and GBP 125,140) |

### Taper Calculation Formula [T1]

```
Adjusted net income = Total income - Gross pension contributions - Gross Gift Aid donations
If adjusted net income <= GBP 100,000: Personal allowance = GBP 12,570
If adjusted net income > GBP 100,000 and <= GBP 125,140:
    Reduction = (Adjusted net income - GBP 100,000) / 2
    Personal allowance = GBP 12,570 - Reduction
If adjusted net income > GBP 125,140: Personal allowance = GBP 0
```

### Adjusted Net Income [T1]

| Deduction from total income | Effect |
|---------------------------|--------|
| Gross personal pension contributions (relief at source) | Extend basic rate band AND reduce adjusted net income |
| Gift Aid donations (grossed up) | Extend basic rate band AND reduce adjusted net income |
| Trading losses (sideways relief, s 64 ITA 2007) | Reduce total income |

**Tax planning note [T2]:** Pension contributions and Gift Aid can be used to bring adjusted net income below GBP 100,000, restoring the personal allowance. This is a legitimate and common planning strategy. Flag for reviewer to confirm amounts.

---

## Step 3: Income Tax Rates -- England, Wales, Northern Ireland (rUK) [T1]

**Legislation:** ITA 2007, s 6; Finance Act 2024

### Non-Savings, Non-Dividend Income [T1]

| Band | Taxable income | Rate |
|------|---------------|------|
| Personal allowance | GBP 0 -- GBP 12,570 | 0% |
| Basic rate | GBP 12,571 -- GBP 50,270 | 20% |
| Higher rate | GBP 50,271 -- GBP 125,140 | 40% |
| Additional rate | Over GBP 125,140 | 45% |

The basic rate band is GBP 37,700 (i.e. GBP 50,270 minus GBP 12,570).

### Savings Income Rates [T1]

| Band | Rate |
|------|------|
| Savings within basic rate band | 20% |
| Savings within higher rate band | 40% |
| Savings within additional rate band | 45% |

But note: savings allowance and starting rate for savings may reduce effective rate to 0% (see Step 5).

### Dividend Income Rates [T1]

| Band | Rate |
|------|------|
| Dividends within basic rate band | 8.75% |
| Dividends within higher rate band | 33.75% |
| Dividends within additional rate band | 39.35% |

---

## Step 4: Income Tax Rates -- Scotland [T1]

**Legislation:** Scotland Act 2016; Scottish Rate Resolution 2024/25

Scottish rates apply ONLY to non-savings, non-dividend income of Scottish taxpayers. Savings and dividend income is taxed at the UK-wide rates in Step 3.

### Scottish Income Tax Bands (2024/25) [T1]

| Band | Taxable income (above personal allowance) | Rate |
|------|-------------------------------------------|------|
| Personal allowance | GBP 0 -- GBP 12,570 | 0% |
| Starter rate | GBP 12,571 -- GBP 14,876 | 19% |
| Basic rate | GBP 14,877 -- GBP 26,561 | 20% |
| Intermediate rate | GBP 26,562 -- GBP 43,662 | 21% |
| Higher rate | GBP 43,663 -- GBP 75,000 | 42% |
| Advanced rate | GBP 75,001 -- GBP 125,140 | 45% |
| Top rate | Over GBP 125,140 | 48% |

### Scottish Income Tax Bands (2025/26) [T1]

| Band | Taxable income (above personal allowance) | Rate |
|------|-------------------------------------------|------|
| Personal allowance | GBP 0 -- GBP 12,570 | 0% |
| Starter rate | GBP 12,571 -- GBP 15,397 | 19% |
| Basic rate | GBP 15,398 -- GBP 27,491 | 20% |
| Intermediate rate | GBP 27,492 -- GBP 43,662 | 21% |
| Higher rate | GBP 43,663 -- GBP 75,000 | 42% |
| Advanced rate | GBP 75,001 -- GBP 125,140 | 45% |
| Top rate | Over GBP 125,140 | 48% |

### Who Is a Scottish Taxpayer? [T1]

A Scottish taxpayer is someone whose closest connection (main place of residence) is in Scotland for the majority of the tax year. HMRC assigns an S tax code prefix.

---

## Step 5: Savings Allowance and Starting Rate for Savings [T1]

**Legislation:** ITA 2007, ss 12A, 12B (inserted by Finance Act 2016)

### Personal Savings Allowance (PSA) [T1]

| Taxpayer status | Savings allowance |
|----------------|------------------|
| Basic rate taxpayer | GBP 1,000 |
| Higher rate taxpayer | GBP 500 |
| Additional rate taxpayer | GBP 0 |

The PSA taxes savings income at 0% up to the allowance amount. It does NOT reduce taxable income -- it applies a 0% rate.

### Starting Rate for Savings [T1]

| Item | Value |
|------|-------|
| Starting rate band | GBP 5,000 |
| Starting rate | 0% |
| Availability | Only if non-savings income (after personal allowance) is below GBP 5,000 |

The starting rate band is reduced by GBP 1 for every GBP 1 of non-savings income above the personal allowance. If non-savings income exceeds GBP 17,570 (GBP 12,570 + GBP 5,000), the starting rate for savings is fully used up.

---

## Step 6: Dividend Allowance [T1]

**Legislation:** ITTOIA 2005, s 13A (as amended)

| Tax Year | Dividend Allowance |
|----------|-------------------|
| 2023/24 | GBP 1,000 |
| 2024/25 | GBP 500 |
| 2025/26 | GBP 500 |

The dividend allowance taxes the first GBP 500 of dividend income at 0%. It does NOT reduce taxable income -- it applies a 0% rate. Dividends above the allowance are taxed at 8.75% / 33.75% / 39.35% depending on the band they fall into.

**The dividend allowance still uses up the basic rate band.** A common misconception is that it sits outside the bands -- it does not.

---

## Step 7: Marriage Allowance [T1]

**Legislation:** ITA 2007, s 55B

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Relationship | Married or in a civil partnership |
| Transferor income | Must be below the personal allowance (GBP 12,570) |
| Recipient tax rate | Must be a basic rate taxpayer (not higher or additional) |
| Recipient jurisdiction | rUK or Scotland (starter, basic, or intermediate rate) |

### How It Works [T1]

| Item | Amount |
|------|--------|
| Amount transferable | GBP 1,260 (10% of personal allowance) |
| Tax saving for recipient | GBP 1,260 x 20% = GBP 252 |
| Effect on transferor | Personal allowance reduces to GBP 11,310 |
| Effect on recipient | Receives a tax reducer of GBP 252 |

### Rules [T1]

- The transfer is an election -- it must be claimed
- It can be backdated up to 4 years
- The recipient gets a tax REDUCER (reduces tax liability, not taxable income)
- If the recipient is a Scottish taxpayer, the reducer is still calculated at 20% (not the Scottish rate)
- If the recipient's income exceeds the basic rate band (GBP 50,270 for rUK), the marriage allowance is NOT available

---

## Step 8: Tax Reducers and Reliefs [T1/T2]

**Legislation:** ITA 2007, various sections

### Tax Reducers (reduce tax liability, not taxable income) [T1]

| Reducer | Amount | Legislation |
|---------|--------|-------------|
| Marriage allowance (recipient) | GBP 252 | ITA 2007, s 55B |
| Married couple's allowance (born before 6 April 1935) | Min GBP 4,280, max GBP 11,080 at 10% | ITA 2007, s 45 |
| EIS relief | 30% of investment (max GBP 1M or GBP 2M if at least GBP 1M in knowledge-intensive companies) | ITA 2007, s 158 |
| SEIS relief | 50% of investment (max GBP 200,000) | ITA 2007, s 257AB |
| VCT relief | 30% of investment (max GBP 200,000) | ITA 2007, s 261B |
| Social investment tax relief | 30% of investment | ITA 2007, s 257J |
| Maintenance payments relief (pre-March 1988 obligations) | 10% of GBP 4,280 max | ITA 2007, s 454 |

### Pension Tax Relief [T1]

| Method | How it works |
|--------|-------------|
| Relief at source | Pension provider claims basic rate relief. Higher/additional rate relief claimed via SA100. |
| Net pay | Full relief given through payroll. No further claim needed. |
| Annual allowance | GBP 60,000 (or tapering down to GBP 10,000 for high earners with adjusted income over GBP 260,000) |
| Carry forward | Unused annual allowance from previous 3 years can be carried forward |

### Gift Aid [T1]

| Item | Treatment |
|------|-----------|
| Gross up | Donation x 100/80 = gross amount |
| Basic rate relief | Given to charity at source |
| Higher/additional rate relief | Claimed via SA100 by extending the basic rate band |
| Basic rate band extension | Gross Gift Aid donation added to basic rate band limit |

---

## Step 9: Final Tax Computation [T1]

**Legislation:** ITA 2007, Part 2

### Computation Steps (in order) [T1]

| Step | Action |
|------|--------|
| 1 | Calculate total income (all sources) |
| 2 | Deduct reliefs from total income (e.g. trading losses, pension contributions for adjusted net income) to get net income |
| 3 | Deduct personal allowance from net income to get taxable income |
| 4 | Split taxable income into: non-savings, savings, dividends |
| 5 | Apply rates to non-savings income (rUK or Scottish rates) |
| 6 | Apply starting rate for savings (0% on up to GBP 5,000 if eligible) |
| 7 | Apply savings rates (with PSA at 0%) |
| 8 | Apply dividend rates (with dividend allowance at 0%) |
| 9 | Sum = income tax liability |
| 10 | Deduct tax reducers (marriage allowance, EIS, etc.) |
| 11 | Result = income tax charged |
| 12 | Deduct tax already deducted at source (PAYE, tax on savings, CIS) |
| 13 | Deduct payments on account already made |
| 14 | Deduct Class 4 NIC payments on account (if applicable) |
| 15 | Result = tax due (or refund) |

### Basic Rate Band Extension [T1]

The basic rate band (GBP 37,700) is extended by:
- Gross personal pension contributions (relief at source method)
- Gross Gift Aid donations

Example: GBP 4,000 gross pension contribution extends the basic rate band to GBP 41,700, meaning the higher rate threshold becomes GBP 54,270 (GBP 12,570 + GBP 41,700).

---

## Step 10: Payments on Account [T1]

**Legislation:** TMA 1970, ss 59A-59B

### When POAs Are Required [T1]

| Condition | POA required? |
|-----------|---------------|
| Previous year SA tax + Class 4 NIC > GBP 1,000 | YES |
| Previous year SA tax + Class 4 NIC <= GBP 1,000 | NO |
| 80% or more of tax deducted at source (PAYE) | NO |

### Payment Schedule [T1]

| Payment | Date | Amount |
|---------|------|--------|
| First payment on account (POA1) | 31 January in the tax year | 50% of prior year SA liability |
| Second payment on account (POA2) | 31 July after the tax year | 50% of prior year SA liability |
| Balancing payment | 31 January after the tax year | Remainder after POA1 + POA2 |

### Example for 2024/25 [T1]

| Payment | Date | Based on |
|---------|------|----------|
| POA1 for 2024/25 | 31 January 2025 | 50% of 2023/24 SA liability |
| POA2 for 2024/25 | 31 July 2025 | 50% of 2023/24 SA liability |
| Balancing payment for 2024/25 | 31 January 2026 | 2024/25 actual liability minus POA1 minus POA2 |
| POA1 for 2025/26 | 31 January 2026 | 50% of 2024/25 SA liability |

**Note:** The balancing payment for 2024/25 AND the first POA for 2025/26 are both due on 31 January 2026.

### Reducing Payments on Account [T2]

If the client expects their tax liability to be lower than the previous year, they can apply to reduce POAs using form SA303. If the estimate is too low, HMRC charges interest on the shortfall from the original due date. [T2] Flag for reviewer before reducing.

---

## Step 11: Filing Deadlines and Penalties [T1]

**Legislation:** TMA 1970, ss 8-12, 93, 97

### Filing Deadlines [T1]

| Item | Deadline |
|------|----------|
| Paper SA100 return | 31 October following the tax year |
| Online SA100 return | 31 January following the tax year |
| For 2024/25: paper | 31 October 2025 |
| For 2024/25: online | 31 January 2026 |

### Late Filing Penalties [T1]

| Delay | Penalty |
|-------|---------|
| 1 day late | GBP 100 (even if no tax owed) |
| 3 months late | GBP 10 per day for up to 90 days (max GBP 900) |
| 6 months late | Greater of GBP 300 or 5% of tax due |
| 12 months late | Greater of GBP 300 or 5% of tax due (additional) |

### Late Payment Penalties [T1]

| Delay from 31 January | Penalty |
|----------------------|---------|
| 30 days late | 5% of tax unpaid |
| 6 months late | Additional 5% of tax still unpaid |
| 12 months late | Additional 5% of tax still unpaid |

Interest is charged on all late payments from the due date at the HMRC interest rate.

---

## Step 12: SA100 Key Boxes -- Quick Reference [T1]

| Box / Section | Description |
|--------------|-------------|
| TR1-TR2 | Personal details, UTR, NI number |
| TR3 | Employment income (from P60) |
| TR4 | Self-employment (attach SA103) |
| TR5 | Partnerships (attach SA104) |
| TR6 | Property income (attach SA105) |
| TR7 | Foreign income (attach SA106) |
| SA101 | Additional information (EIS, VCT, Gift Aid, etc.) |
| Tax calculation summary | Total income, deductions, personal allowance, tax charged, tax paid, balance due/refund |

---

## PROHIBITIONS

- NEVER compute income tax without first categorising income as non-savings, savings, or dividends
- NEVER apply Scottish rates to savings or dividend income -- Scottish rates apply ONLY to non-savings, non-dividend income
- NEVER apply marriage allowance if the recipient is a higher or additional rate taxpayer
- NEVER ignore the personal allowance taper for adjusted net income above GBP 100,000
- NEVER apply the personal savings allowance to additional rate taxpayers (it is GBP 0)
- NEVER treat the dividend allowance as a deduction from income -- it is a 0% rate band
- NEVER apply the starting rate for savings if non-savings income exceeds GBP 17,570
- NEVER compute payments on account based on the current year -- always use the prior year SA liability
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their accountant for confirmation
- NEVER advise on non-domiciled or remittance basis issues -- escalate as T3

---

## Step 13: Edge Case Registry

### EC1 -- Personal allowance taper at boundary [T1]
**Situation:** Taxpayer has adjusted net income of GBP 110,000.
**Resolution:** Reduction = (GBP 110,000 - GBP 100,000) / 2 = GBP 5,000. Personal allowance = GBP 12,570 - GBP 5,000 = GBP 7,570. Effective marginal rate on income GBP 100,000-GBP 110,000 = 60%.

### EC2 -- Pension contribution restoring personal allowance [T2]
**Situation:** Taxpayer earns GBP 115,000. Makes GBP 15,000 gross pension contribution (relief at source).
**Resolution:** Adjusted net income = GBP 115,000 - GBP 15,000 = GBP 100,000. Personal allowance fully restored to GBP 12,570. Tax saving: GBP 15,000 x 40% higher rate relief + GBP 12,570 x 40% restored allowance = significant benefit. [T2] Flag for reviewer to confirm contribution is within annual allowance.

### EC3 -- Scottish taxpayer with dividends [T1]
**Situation:** Scottish taxpayer earns GBP 40,000 salary and GBP 5,000 dividends.
**Resolution:** Salary taxed at Scottish rates (starter 19%, basic 20%, intermediate 21%). Dividends taxed at UK dividend rates (8.75% basic rate). The Scottish rates do NOT apply to dividends.

### EC4 -- Marriage allowance and Scottish taxpayer [T1]
**Situation:** Scottish basic rate taxpayer is recipient of marriage allowance transfer.
**Resolution:** Tax reducer = GBP 252 (calculated at 20%, not Scottish rates). The marriage allowance reducer is always at the UK basic rate of 20%.

### EC5 -- Savings income only, below personal allowance [T1]
**Situation:** Retired person with no employment or pension income. Bank interest GBP 18,000 only.
**Resolution:** Personal allowance GBP 12,570 applied. Remaining GBP 5,430. Starting rate for savings: GBP 5,000 at 0% (available because non-savings income is nil). PSA: GBP 430 within GBP 1,000 allowance at 0%. Tax = GBP 0.

### EC6 -- Dividend allowance uses up basic rate band [T1]
**Situation:** Taxpayer has GBP 49,770 salary and GBP 2,000 dividends. Total income GBP 51,770.
**Resolution:** Salary uses GBP 37,200 of basic rate band (GBP 49,770 - GBP 12,570). Remaining basic rate band = GBP 500. Dividends: first GBP 500 covered by dividend allowance at 0% (but still uses basic rate band). Next GBP 500 in basic rate band at 8.75%. Remaining GBP 1,000 in higher rate band at 33.75%.

### EC7 -- Multiple income sources and band allocation [T2]
**Situation:** Employment GBP 30,000, self-employment GBP 15,000, savings GBP 3,000, dividends GBP 8,000. Total GBP 56,000.
**Resolution:** Order: non-savings first (GBP 45,000), then savings (GBP 3,000), then dividends (GBP 8,000). Personal allowance against non-savings: GBP 45,000 - GBP 12,570 = GBP 32,430 taxable non-savings. All within basic rate band (GBP 37,700). Remaining basic rate band: GBP 5,270. Savings: GBP 1,000 PSA at 0%, GBP 2,000 at 20%. Remaining basic rate band: GBP 3,270. Dividends: GBP 500 at 0% (dividend allowance), GBP 2,770 at 8.75% (remaining basic rate band), GBP 4,730 at 33.75% (higher rate band).

### EC8 -- Payments on account not required [T1]
**Situation:** Taxpayer has PAYE employment income GBP 45,000. Self-employment profit GBP 3,000 (first year). Tax deducted via PAYE = GBP 6,486. SA liability on self-employment = GBP 600.
**Resolution:** SA liability GBP 600 is below GBP 1,000 threshold. No payments on account required. Pay GBP 600 with the return by 31 January.

### EC9 -- High income child benefit charge [T2]
**Situation:** Taxpayer earns GBP 70,000 and receives child benefit for 2 children.
**Resolution:** High Income Child Benefit Charge applies where adjusted net income exceeds GBP 60,000 (from 2024/25, threshold raised from GBP 50,000). At GBP 70,000, the charge is 100% of child benefit received. Charge is 1% of benefit for every GBP 200 of income between GBP 60,000 and GBP 80,000. At GBP 70,000: 50% x annual child benefit. [T2] Flag for reviewer to confirm exact child benefit amount received.

### EC10 -- Gift Aid extending basic rate band [T1]
**Situation:** Taxpayer earns GBP 55,000. Makes GBP 2,000 net Gift Aid donations (GBP 2,500 gross).
**Resolution:** Basic rate band extended by GBP 2,500: from GBP 37,700 to GBP 40,200. Higher rate threshold becomes GBP 52,770 (GBP 12,570 + GBP 40,200). Income GBP 50,270-GBP 52,770 now taxed at 20% instead of 40%. Higher rate relief on donation: GBP 2,500 x 20% = GBP 500 (the difference between 40% and 20% on the amount pulled into basic rate).

---

## Step 14: Test Suite

### Test 1 -- Basic rate taxpayer, employment only
**Input:** Employment income GBP 35,000. No other income. PAYE deducted GBP 4,486.
**Expected output:** Personal allowance GBP 12,570. Taxable income GBP 22,430. Tax: GBP 22,430 x 20% = GBP 4,486. Tax deducted GBP 4,486. Balance due = GBP 0.

### Test 2 -- Higher rate taxpayer with self-employment
**Input:** Employment income GBP 40,000. Self-employment profit GBP 25,000. PAYE deducted GBP 5,486.
**Expected output:** Total non-savings income GBP 65,000. Personal allowance GBP 12,570. Taxable GBP 52,430. Tax: GBP 37,700 x 20% = GBP 7,540. GBP 14,730 x 40% = GBP 5,892. Total tax = GBP 13,432. Less PAYE GBP 5,486. Balance via SA = GBP 7,946.

### Test 3 -- Personal allowance taper
**Input:** Total income GBP 120,000. No pension contributions, no Gift Aid.
**Expected output:** Adjusted net income GBP 120,000. Reduction = (GBP 120,000 - GBP 100,000) / 2 = GBP 10,000. Personal allowance = GBP 12,570 - GBP 10,000 = GBP 2,570. Taxable income = GBP 117,430. Tax: GBP 37,700 x 20% = GBP 7,540. GBP 79,730 x 40% = GBP 31,892. Total = GBP 39,432.

### Test 4 -- Scottish taxpayer with savings and dividends
**Input:** Scottish taxpayer. Employment income GBP 30,000. Savings GBP 2,000. Dividends GBP 3,000.
**Expected output:** Non-savings (Scottish rates): Personal allowance GBP 12,570. Taxable non-savings GBP 17,430. Tax: GBP 2,306 at 19% = GBP 438.14. GBP 12,094 at 20% (note: Scottish basic rate band to GBP 14,876 above PA, leaving GBP 12,094 after starter band filled) -- wait, let me recalculate. Using 2024/25 Scottish bands: Starter (GBP 12,571-GBP 14,876) = GBP 2,306 x 19% = GBP 438.14. Basic (GBP 14,877-GBP 26,561) = GBP 11,685 x 20% = GBP 2,337. Intermediate (GBP 26,562-GBP 30,000) = GBP 3,439 x 21% = GBP 722.19. Non-savings tax = GBP 3,497.33. Savings (UK rates): GBP 1,000 PSA at 0%. GBP 1,000 at 20% = GBP 200. Dividends (UK rates): GBP 500 allowance at 0%. GBP 2,500 at 8.75% = GBP 218.75. Total tax = GBP 3,916.08.

### Test 5 -- Marriage allowance
**Input:** Spouse A earns GBP 10,000 (below personal allowance). Spouse B earns GBP 28,000 (basic rate). Marriage allowance elected.
**Expected output:** Spouse A transfers GBP 1,260. Spouse A personal allowance = GBP 11,310. Spouse A tax = GBP 0 (income below reduced PA). Spouse B tax reducer = GBP 252. Spouse B tax without MA: (GBP 28,000 - GBP 12,570) x 20% = GBP 3,086. Spouse B tax with MA: GBP 3,086 - GBP 252 = GBP 2,834.

### Test 6 -- Payments on account
**Input:** 2023/24 SA liability (tax + Class 4 NIC via SA) = GBP 8,000. 2024/25 actual SA liability = GBP 10,000.
**Expected output:** POA1 (31 Jan 2025) = GBP 4,000. POA2 (31 Jul 2025) = GBP 4,000. Balancing payment (31 Jan 2026) = GBP 10,000 - GBP 4,000 - GBP 4,000 = GBP 2,000. Plus POA1 for 2025/26 (31 Jan 2026) = GBP 5,000. Total due 31 Jan 2026 = GBP 7,000.

### Test 7 -- Savings income, starting rate available
**Input:** Part-time employment GBP 14,000. Bank interest GBP 6,000. No dividends.
**Expected output:** Non-savings: GBP 14,000 - GBP 12,570 PA = GBP 1,430 at 20% = GBP 286. Starting rate for savings: GBP 5,000 - GBP 1,430 = GBP 3,570 of starting rate remaining. Savings: GBP 3,570 at 0% (starting rate). Then PSA GBP 1,000 at 0%. Then GBP 1,430 at 20% = GBP 286. Total tax = GBP 572.

### Test 8 -- Additional rate taxpayer, no personal allowance
**Input:** Total income GBP 200,000. All employment. PAYE deducted GBP 72,000.
**Expected output:** Personal allowance = GBP 0 (income > GBP 125,140). Taxable income = GBP 200,000. Tax: GBP 37,700 x 20% = GBP 7,540. GBP 87,440 x 40% (GBP 37,701 to GBP 125,140) = GBP 34,976. GBP 74,860 x 45% = GBP 33,687. Total tax = GBP 76,203. Less PAYE GBP 72,000. Balance = GBP 4,203.

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
Action Required: Qualified accountant must confirm before filing.
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

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
