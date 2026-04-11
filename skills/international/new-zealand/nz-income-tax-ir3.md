---
name: nz-income-tax-ir3
description: >
  Use this skill whenever asked about New Zealand income tax for self-employed individuals filing an IR3 return. Trigger on phrases like "how much tax do I pay in NZ", "IR3", "income tax return New Zealand", "allowable deductions NZ", "provisional tax NZ", "schedular payments", "independent earner tax credit", "ACC levies", "Working for Families", "residual income tax", "self-employed tax NZ", or any question about filing or computing income tax for a self-employed individual in New Zealand. This skill covers NZ tax brackets (10.5%-39%), IR3 return structure, allowable deductions, ACC levies, provisional tax, IETC, penalties, and interaction with GST. ALWAYS read this skill before touching any NZ income tax work.
version: 1.0
jurisdiction: NZ
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# NZ Income Tax (IR3) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Income Tax Act 2007 (ITA 2007) |
| Supporting Legislation | Tax Administration Act 1994 (TAA 1994); Accident Compensation Act 2001 (ACC Act); Social Security Act 2018 (Working for Families) |
| Tax Authority | Inland Revenue Department (IRD) |
| Filing Portal | myIR (ird.govt.nz) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by a New Zealand Chartered Accountant |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, IETC eligibility, provisional tax threshold, filing deadlines, penalty rates. Tier 2: home office apportionment, motor vehicle business %, mixed-use expense allocation, bad debt write-off criteria. Tier 3: look-through companies, trusts, overseas income, complex capital gains (bright-line test). |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Tax residency status** [T1] -- NZ tax resident or non-resident. Non-residents have different rules. If non-resident, STOP and escalate [T3].
2. **Employment status** [T1] -- fully self-employed, or employed with side self-employment income.
3. **Gross self-employment income** [T1] -- total business income received or invoiced in the tax year (1 April to 31 March).
4. **GST registration status** [T1] -- registered (invoice basis or payments basis) or not registered. Affects how GST is treated in the P&L.
5. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items).
6. **Depreciation schedule** [T1] -- assets owned, cost, date acquired, depreciation method and rate.
7. **ACC levies paid** [T1] -- earner levy amount deducted or paid during the year.
8. **Prior year residual income tax (RIT)** [T1] -- for provisional tax determination. If RIT > $5,000, client is a provisional taxpayer.
9. **Other income** [T1] -- employment income (salary/wages), interest, dividends, rental, overseas income.
10. **Working for Families eligibility** [T2] -- number of dependent children, family income, hours worked (if applicable).

**If tax residency is unknown, STOP. Do not compute. NZ tax residency is mandatory.**

---

## Step 1: Determine Applicable Tax Rates [T1]

**Legislation:** Income Tax Act 2007, Schedule 1

### Individual Tax Rates (2025 tax year: 1 April 2024 -- 31 March 2025)

| Taxable Income (NZD) | Rate | Cumulative Tax at Top |
|----------------------|------|-----------------------|
| $0 -- $15,600 | 10.5% | $1,638 |
| $15,601 -- $53,500 | 17.5% | $8,020 |
| $53,501 -- $78,100 | 30% | $15,400 |
| $78,101 -- $180,000 | 33% | $49,027 |
| $180,001+ | 39% | -- |

**New Zealand has NO tax-free threshold. The first dollar of income is taxed at 10.5%.**

**Note:** These brackets were effective from 31 July 2024 (applied pro-rata for the 2024/25 year transitionally, but for the full 2025/26 year onward they apply in full). Confirm the applicable year before computing.

---

## Step 2: IR3 Return Structure [T1]

**Legislation:** Income Tax Act 2007; TAA 1994

The IR3 is the individual income tax return for persons with income not fully taxed at source (e.g., self-employed income, rental income, overseas income).

### Key Sections

| Section | Description | How to Populate |
|---------|-------------|-----------------|
| Business income | Gross income from self-employment | Total business revenue for the year |
| Less: Business expenses | Allowable deductions | Expenses passing the nexus test (see Step 3) |
| Net profit/loss | Business income minus expenses | Carried to total income |
| Other income | Salary/wages, interest, dividends, rental | Amounts from employment, banks, companies |
| Total income | Sum of all income sources | All income aggregated |
| Less: Losses brought forward | Prior year losses | Carried from prior IR3 |
| Less: Independent earner tax credit | IETC (see Step 6) | Up to $520 per year |
| Taxable income | Total income minus deductions and losses | Apply rate table |
| Tax on taxable income | Computed from rate table | Progressive calculation |
| Less: Tax credits | PAYE deducted, RWT, withholding tax, IETC | Credits from certificates |
| Residual income tax (RIT) | Tax payable after credits | Determines provisional tax obligation |

---

## Step 3: Allowable Deductions -- The Nexus Test [T1/T2]

**Legislation:** Income Tax Act 2007, sections DA 1 and DA 2

### The Test [T1]
An expense is deductible if it has a **nexus** (connection) to deriving assessable income or carrying on a business for that purpose, AND is not of a capital, private, or domestic nature. This is the "general permission" in DA 1. Section DA 2 lists the "general limitations".

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated business premises) | T1 | Fully deductible |
| Professional indemnity insurance | T1 | Fully deductible |
| Accounting and tax agent fees | T1 | Fully deductible |
| Legal fees (business-related) | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions (operational) | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Professional development / CPD | T1 | Fully deductible if related to current business |
| Professional membership fees (CAANZ, NZICA) | T1 | Fully deductible |
| Bad debts (genuinely irrecoverable, previously returned as income) | T2 | Flag for reviewer -- confirm write-off criteria met |
| ACC levies (earner and work levies) | T1 | Deductible |
| Utilities (home office) | T2 | Proportional only -- see home office rules |
| Phone / mobile / internet | T2 | Business use portion only -- client to confirm % |
| Motor vehicle expenses | T2 | Business use portion only -- logbook required |
| Travel (flights, accommodation for business) | T1 | Fully deductible if wholly business purpose |
| Depreciation | T1 | Calculated per IRD rates (see Step 4) |
| Interest on business borrowings | T1 | Fully deductible if borrowed for business purposes |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Entertainment (50% deductible, 50% non-deductible) | ITA 2007 subpart DD -- 50% limitation on most entertainment |
| Personal living expenses | Private / domestic limitation (DA 2(2)) |
| Fines and penalties | Public policy (DA 2(3)) |
| Income tax itself | Cannot deduct income tax against income |
| Capital expenditure (unless depreciable) | Capital limitation (DA 2(1)) |
| Drawings / personal withdrawals | Not an expense |

**NZ Entertainment Rule:** Unlike Malta (which fully blocks entertainment), NZ allows a **50% deduction** for most business entertainment expenses (meals with clients, recreational activities). The remaining 50% is non-deductible. Some entertainment (e.g., entertainment provided to the general public as advertising) may be 100% deductible. [T2] Flag for reviewer to confirm the correct percentage.

### Home Office Rules [T2]

**Legislation:** ITA 2007, section DA 1; IRD operational guidance

- Calculate the proportion of home used for business: dedicated room(s) as a percentage of total floor area
- Apply that percentage to: rent/mortgage interest, rates, insurance, electricity, internet, maintenance
- An alternative simplified method allows a flat-rate deduction per hour worked from home (check current IRD guidance for the rate)
- Must be a dedicated workspace or have a reasonable basis for apportionment
- [T2] Flag for reviewer: confirm floor area basis and that workspace is genuinely used for business

### Motor Vehicle Rules [T2]

**Legislation:** ITA 2007, sections DE 2--DE 12

- Only the business-use percentage of fuel, insurance, registration, maintenance, and depreciation is deductible
- Client must maintain a logbook for a representative 90-day period (minimum) to establish business percentage
- The logbook is valid for 3 years, then must be renewed
- IRD may accept the kilometre rate method instead (check current rate -- typically around $0.99/km for petrol/diesel vehicles up to a mileage cap)
- [T2] Flag for reviewer: confirm business percentage claimed is reasonable and documented with a valid logbook

---

## Step 4: Depreciation [T1]

**Legislation:** Income Tax Act 2007, subpart EE; IRD Depreciation Determinations

### Common Depreciation Rates

| Asset Type | Diminishing Value Rate | Straight-Line Rate | Estimated Useful Life |
|-----------|----------------------|--------------------|-----------------------|
| Computer hardware (laptops, desktops) | 50% | 40% | 4 years |
| Computer software (purchased) | 50% | 40% | 4 years |
| Office furniture | 12% | 8% | 12.5 years |
| Office equipment (printers, scanners) | 30% | 21% | 5 years |
| Motor vehicles | 30% | 21% | 5 years |
| Mobile phones | 67% | 67% | 3 years |
| Buildings (residential) | 0% | 0% | No depreciation since 2011 |
| Buildings (commercial/industrial) | 2% | 1.5% | 50 years |

### Rules [T1]

- Taxpayer elects either **diminishing value** (DV) or **straight-line** (SL) method for each asset. Once elected, cannot switch for that asset.
- Low-value assets (cost $1,000 or less, or DV $1,000 or less): can be expensed immediately in the year of purchase.
- Depreciation starts in the year the asset is first used in the business.
- Pro-rata for part-year use (month of acquisition to end of income year).
- Motor vehicles: only the business-use proportion is claimable [T2].
- Cost threshold for immediate expensing increased to $1,000 (confirm current threshold with IRD).

### Asset Disposal [T2]

- If sale proceeds exceed adjusted tax value: depreciation recovery income (taxable).
- If sale proceeds are less than adjusted tax value: deduction allowed for the loss on disposal.
- Flag for reviewer: confirm disposal proceeds and tax book value before computing.

---

## Step 5: ACC Levies Interaction [T1]

**Legislation:** Accident Compensation Act 2001; ACC levy regulations

### ACC Levy Components for Self-Employed (2025/26)

| Levy | Rate | Basis |
|------|------|-------|
| Earner's levy | $1.67 per $100 liable income (1.67%) | All earners -- deducted from wages or invoiced to self-employed |
| Working Safer levy | $0.08 per $100 liable income | All businesses |
| Work levy | Varies by industry classification (CU code) | Self-employed -- based on industry risk |

### Key Rules [T1]

- **Minimum liable income:** $49,365 (2025/26). If actual income is below this, ACC levies are still calculated on the minimum.
- **Maximum liable income:** $152,790 (2025/26). Income above this is not subject to ACC levies.
- ACC levies paid are **deductible** for income tax purposes.
- The earner's levy for employees is deducted by the employer; for self-employed, it is invoiced directly by ACC or IRD.
- Work levy rates vary significantly by industry -- confirm the client's Classification Unit (CU) code.

---

## Step 6: Independent Earner Tax Credit (IETC) [T1]

**Legislation:** Income Tax Act 2007, section LB 1

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Tax residency | Must be a NZ tax resident for the full tax year |
| Income range | Annual income between $24,000 and $70,000 |
| Not receiving | Working for Families tax credits, NZ Superannuation, a student allowance, or income-tested benefit |
| Age | 18 years or older |

### Credit Amount [T1]

| Income Range (NZD) | IETC Amount |
|---------------------|-------------|
| $24,000 -- $66,000 | $520 per year (full credit) |
| $66,001 -- $70,000 | $520 minus 13 cents per dollar over $66,000 |
| Below $24,000 or above $70,000 | $0 |

**Note:** The upper threshold increased from $48,000 to $70,000 and the abatement start from $44,000 to $66,000 effective from the 2024/25 tax year (31 July 2024 change). For self-employed filing an IR3, claim the IETC by entering the number of eligible months on the return.

---

## Step 7: Working for Families (WFF) [T2]

**Legislation:** Income Tax Act 2007, subparts MD and MF; Social Security Act 2018

### Overview [T2]

Working for Families tax credits are available to families with dependent children. Self-employed individuals may be eligible but the interaction with fluctuating self-employment income makes this a T2 matter.

| Credit | Description |
|--------|-------------|
| Family Tax Credit (FTC) | Per-child credit based on family income. Abates as income rises. |
| In-Work Tax Credit (IWTC) | Additional credit for families where parent(s) work minimum hours (20 hrs/week for sole parent, 30 hrs/week combined for couples). |
| Best Start Tax Credit | For children born on or after 1 July 2018, up to age 3 (income-tested from age 1). |
| Minimum Family Tax Credit | Top-up to ensure minimum net income if working minimum hours. |

**Self-employment interaction:** Self-employed income counts toward family income for WFF abatement. Business losses may reduce family income. [T2] Flag for reviewer: confirm hours worked meet the IWTC threshold and that family income estimate is reasonable.

---

## Step 8: Provisional Tax [T1]

**Legislation:** Income Tax Act 2007, subpart RC; TAA 1994

### Threshold [T1]

You are a **provisional taxpayer** if your residual income tax (RIT) exceeds **$5,000** in the prior income year.

### Payment Options [T1]

| Method | How It Works | Instalments |
|--------|--------------|-------------|
| Standard option | Prior year RIT + 5% (if prior year return filed) or RIT from 2 years ago + 10% (if not filed), divided equally across instalments | 3 instalments: 28 Aug, 15 Jan, 7 May |
| Estimation option | Taxpayer estimates current year tax liability | 3 instalments: same dates |
| Accounting Income Method (AIM) | Pay provisional tax based on actual year-to-date accounting income, using approved software | 6 payments (every 2 months) |

### Instalment Dates (Standard, Non-GST aligned) [T1]

| Instalment | Due Date |
|-----------|----------|
| 1st | 28 August |
| 2nd | 15 January |
| 3rd | 7 May |

**Note:** Different dates apply if the taxpayer is GST-registered and files GST returns 6-monthly or 2-monthly (instalments align with GST due dates). Confirm the client's GST filing frequency.

### Use-of-Money Interest (UOMI) [T1]

- IRD charges interest on underpayments and pays interest on overpayments of provisional tax.
- UOMI does not apply to the first provisional tax instalment if using the standard method and the taxpayer's RIT is under $60,000.
- Check current UOMI rates with IRD (rates change periodically).

---

## Step 9: Filing Deadlines [T1]

**Legislation:** TAA 1994

| Filing / Payment | Deadline |
|-----------------|----------|
| IR3 return (individual, no tax agent) | 7 July following the end of the tax year |
| IR3 return (linked to a tax agent) | 31 March of the following year (extension of time) |
| Terminal tax (balance of tax due) | 7 February following the end of the tax year (if no tax agent); 7 April (with tax agent) |
| Provisional tax instalments | See Step 8 |

**Tax year:** 1 April to 31 March (standard balance date).

---

## Step 10: Penalties and Interest [T1]

**Legislation:** TAA 1994, Part 9

| Offence | Penalty |
|---------|---------|
| Late filing of IR3 | Late filing penalty: $50 initial + $250 if still not filed after further notification |
| Late payment | 1% initial late payment penalty on the day after due date + 4% incremental penalty if still unpaid after 7 days + 1% monthly thereafter |
| Use-of-money interest (underpayment) | Variable rate (check current IRD rate -- typically around 7-8%) |
| Shortfall penalty -- lack of reasonable care | 20% of the tax shortfall |
| Shortfall penalty -- unacceptable tax position | 20% of the tax shortfall |
| Shortfall penalty -- gross carelessness | 40% of the tax shortfall |
| Shortfall penalty -- abusive tax position | 100% of the tax shortfall |
| Shortfall penalty -- evasion | 150% of the tax shortfall |

**WARNING:** Shortfall penalties are severe and cumulative with UOMI. Any shortfall situation must be escalated to a qualified accountant immediately.

---

## Step 11: Interaction with GST [T1]

**Legislation:** Goods and Services Tax Act 1985

| Scenario | Income Tax Treatment |
|----------|---------------------|
| GST-registered (invoice basis): GST collected on sales | NOT income -- exclude from gross business income. Report net (GST-exclusive) amounts. |
| GST-registered: input GST claimed on expenses | NOT an expense -- exclude from deductions. Report net (GST-exclusive) expense amounts. |
| GST-registered: input GST that cannot be claimed (exempt supplies, entertainment 50%) | IS an expense -- include the non-claimable GST in the cost. |
| Not GST-registered | All amounts are GST-inclusive. Full gross amount is income/expense. |

**Key rule:** For GST-registered taxpayers, the IR3 business income and expenses should be reported GST-exclusive. For non-registered taxpayers, report GST-inclusive amounts.

---

## Step 12: Record Keeping [T1]

**Legislation:** TAA 1994, section 22

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 7 years from the end of the income year |
| What to keep | All sales invoices, purchase invoices, bank statements, receipts, contracts, depreciation schedule, motor vehicle logbook |
| Format | Paper or digital (IRD accepts digital records) |
| Motor vehicle logbook | Must be maintained for a 90-day representative period, valid for 3 years |

---

## Step 13: Edge Case Registry

### EC1 -- GST collected included in income [T1]
**Situation:** GST-registered client reports gross receipts of $115,000 (includes 15% GST). Client includes full $115,000 as business income.
**Resolution:** Business income must be $100,000 (GST-exclusive). The $15,000 GST collected is a liability to IRD, not income. Correct before filing.

### EC2 -- Non-GST-registered client expense treatment [T1]
**Situation:** Non-GST-registered client purchases office supplies for $115 (including 15% GST).
**Resolution:** Full $115 is the deductible expense. Non-registered clients cannot claim input GST, so the gross amount is the cost.

### EC3 -- Entertainment expenses, 50% rule [T1]
**Situation:** Client takes a client to dinner ($200) and wants to deduct the full amount.
**Resolution:** Only 50% ($100) is deductible under the entertainment limitation (subpart DD). The other 50% is non-deductible. Unlike Malta, NZ does not fully block entertainment -- it allows half.

### EC4 -- Motor vehicle, no logbook [T2]
**Situation:** Client claims 70% business use of their vehicle but has never maintained a logbook.
**Resolution:** Without a valid 90-day logbook, the business percentage cannot be substantiated. [T2] Flag for reviewer: client must complete a logbook before the claim can be accepted. IRD may disallow the deduction on audit without logbook evidence.

### EC5 -- Low-value asset incorrectly capitalised [T1]
**Situation:** Client buys a $500 printer and adds it to the depreciation schedule.
**Resolution:** Assets costing $1,000 or less can be immediately expensed in the year of purchase. The $500 printer can be fully deducted as an expense rather than depreciated over multiple years.

### EC6 -- Provisional tax, first year [T1]
**Situation:** Client started self-employment on 1 July 2024. Now filing the first IR3 for the year ending 31 March 2025.
**Resolution:** No provisional tax was required during the first year (no prior year RIT). If the RIT for 2025 exceeds $5,000, the client becomes a provisional taxpayer for the 2026 year.

### EC7 -- IETC claimed while receiving Working for Families [T1]
**Situation:** Client earns $40,000 from self-employment and receives WFF tax credits. Client also claims the IETC.
**Resolution:** INCORRECT. A person receiving WFF tax credits is not eligible for the IETC. Remove the IETC claim. The two credits are mutually exclusive.

### EC8 -- ACC minimum income threshold [T1]
**Situation:** Self-employed client earns only $20,000 but receives an ACC invoice calculated on $49,365.
**Resolution:** CORRECT. ACC levies for self-employed are calculated on a minimum liable income of $49,365 (2025/26), regardless of actual earnings. The full levy amount is deductible for income tax.

### EC9 -- Overseas income not declared [T3]
**Situation:** NZ tax resident client has overseas freelance income of $15,000 USD not included in their IR3.
**Resolution:** NZ tax residents are taxed on worldwide income. The overseas income must be converted to NZD and included. Foreign tax credits may be available. [T3] Escalate to a qualified accountant for foreign tax credit computation and any applicable DTA (Double Tax Agreement) analysis.

### EC10 -- Loss carried forward [T1]
**Situation:** Client had a business loss of $8,000 in 2024 and a profit of $30,000 in 2025.
**Resolution:** The $8,000 loss can be carried forward and offset against the $30,000 profit in 2025, reducing taxable business income to $22,000. Losses can be carried forward indefinitely in NZ (subject to the continuity rules for companies -- not applicable to sole traders).

### EC11 -- Schedular payments received with withholding tax deducted [T1]
**Situation:** Client is a contractor who received schedular payments of $50,000 with $10,000 withholding tax already deducted (20% rate).
**Resolution:** Gross income = $50,000 (report the full gross amount as business income). The $10,000 withholding tax is a tax credit, not a reduction of income. Claim it as a credit against the final tax liability in the IR3. If more tax was withheld than the final liability, client receives a refund.

---

## Step 14: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified NZ accountant must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified NZ accountant. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** NZ tax resident, gross business revenue $85,000, allowable expenses $25,000, depreciation $2,000, ACC levies paid $3,500, no other income, no PAYE credits, not GST-registered.
**Expected output:** Net business income = $60,000 - $2,000 depreciation = $58,000. Deduct ACC $3,500. Taxable income = $54,500. Tax: $1,638 + ($53,500 - $15,600) x 17.5% + ($54,500 - $53,500) x 30% = $1,638 + $6,632.50 + $300 = $8,570.50. IETC: $0 (income above $70,000 gross... but taxable income is $54,500, so check: IETC is based on net income $54,500 -- within range). IETC = $520. Final tax = $8,050.50. RIT = $8,050.50. Provisional tax required next year (RIT > $5,000).

### Test 2 -- Contractor with schedular payments
**Input:** NZ tax resident, gross schedular payments $70,000, withholding tax deducted $14,000 (20%), allowable expenses $15,000, depreciation $1,500.
**Expected output:** Net income = $70,000 - $15,000 - $1,500 = $53,500. Tax on $53,500: $1,638 + ($53,500 - $15,600) x 17.5% = $1,638 + $6,632.50 = $8,270.50. IETC: $520 (income $53,500 is in range). Tax = $7,750.50. Less withholding tax credit $14,000. RIT = -$6,249.50 (refund of $6,249.50).

### Test 3 -- IETC ineligible due to WFF
**Input:** NZ tax resident, self-employed, taxable income $40,000, receives Working for Families tax credits.
**Expected output:** IETC = $0. Cannot claim IETC while receiving WFF. Tax on $40,000: $1,638 + ($40,000 - $15,600) x 17.5% = $1,638 + $4,270 = $5,908.

### Test 4 -- Entertainment expense, 50% rule
**Input:** Client includes $4,000 business entertainment in expenses.
**Expected output:** Only $2,000 is deductible (50%). Remove $2,000 from allowable deductions.

### Test 5 -- Low-value asset expensed
**Input:** Client buys a monitor for $800 and adds it to the depreciation schedule at 50% DV.
**Expected output:** Asset cost is $1,000 or less. Can be immediately expensed. Remove from depreciation schedule and deduct $800 fully in the current year.

### Test 6 -- Provisional tax calculation
**Input:** 2025 IR3 shows RIT of $12,000. Client asks for 2026 provisional tax schedule (standard method, non-GST-aligned).
**Expected output:** 2026 provisional tax = $12,000 + 5% = $12,600. Three equal instalments of $4,200 each: 28 August 2025, 15 January 2026, 7 May 2026.

### Test 7 -- First year, no provisional tax
**Input:** Client started business in October 2024. First IR3 for year ending 31 March 2025. RIT = $7,500.
**Expected output:** No provisional tax was due during 2024/25 (no prior year). Full RIT of $7,500 payable as terminal tax. Client becomes a provisional taxpayer for 2025/26 (RIT > $5,000).

---

## PROHIBITIONS

- NEVER compute tax without confirming NZ tax residency
- NEVER apply tax rates to gross income without first deducting allowable expenses
- NEVER allow the IETC and Working for Families to be claimed simultaneously
- NEVER allow entertainment to be deducted at more than 50% (unless it qualifies as an exception under subpart DD)
- NEVER allow income tax itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER include GST collected in business income for GST-registered clients
- NEVER accept a motor vehicle business-use claim without a valid logbook
- NEVER use current year income estimates for the standard provisional tax method -- always prior year RIT + 5%
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their accountant for confirmation
- NEVER advise on trusts, look-through companies, or overseas income without escalating to a qualified accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant or equivalent licensed practitioner in New Zealand) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
