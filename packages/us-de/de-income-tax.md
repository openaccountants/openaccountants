---
name: de-income-tax
description: "Delaware Individual Income Tax Return (Form PIT-RES) for sole proprietors and single-member LLCs. Covers the seven-bracket graduated system (0%–6.6%), Delaware standard deduction, modifications to federal AGI, and personal credits. Trigger: taxpayer is a Delaware resident with gross income exceeding filing thresholds."
version: "0.1"
jurisdiction: US-DE
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Delaware individual income tax (Form PIT-RES / PIT-NON), tax year 2026

## Scope and who this is for

This Guide covers the Delaware personal income tax on individuals under Title 30, Chapter 11 of the Delaware Code:

- **Full-year residents** file Form PIT-RES.
- **Nonresidents** with Delaware-source income file Form PIT-NON.
- **Part-year residents** choose either form (see the method, step 2).

It is written for **tax year 2026** (returns due 30 April 2027). The section "Tax year 2025 returns" covers **2025 returns** that are still open on extension until 15 October 2026.

It does not cover:

- Delaware's gross receipts tax, corporate income tax, or fiduciary and partnership returns.
- City taxes. A city wage tax withheld from pay is not Delaware income tax, and the resident instructions say "DO NOT INCLUDE CITY WAGE TAX" in Delaware tax withheld. Handle any city tax separately.

Official sources used throughout:

- Delaware Code, Title 30, Chapter 11:
  - residency and rates: https://delcode.delaware.gov/title30/c011/sc01/index.html
  - residents' taxable income and credits: https://delcode.delaware.gov/title30/c011/sc02/index.html
  - nonresidents: https://delcode.delaware.gov/title30/c011/sc03/index.html
  - returns and estimated tax: https://delcode.delaware.gov/title30/c011/sc08/index.html
- Penalties and interest, Title 30, Chapter 5: https://delcode.delaware.gov/title30/c005/sc03/index.html
- 2025 PIT-RES instructions: https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-RES_Instructions_2025-01.pdf
- 2025 PIT-NON instructions: https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-NON_Instructions_2025-01.pdf
- 2026 estimated tax (PIT-EST) instructions: https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-EST_Instructions_2026-01.pdf

The Division of Revenue had not published 2026 return instructions when this Guide was written (25 September 2026). Where a 2026 figure comes from the statute rather than a 2026 form, this Guide says so.

## Ask the client first

1. **Residency.**
   - Where was the client domiciled during 2026, and did that change during the year?
   - Did they keep a place of abode in Delaware? How many days were they in Delaware?
   - Were they abroad for a long period (the foreign-presence exception)?
2. **Federal return.**
   - What is federal adjusted gross income (AGI), and which items make it up?
   - Did they itemize federally?
   - Did they claim the federal earned income credit?
   - Did they place business property in service in 2026 and take bonus depreciation?
3. **Filing status.** For a married couple: joint, separate, or combined separate? Is either spouse a nonresident?
4. **Age and status on 31 December 2026.**
   - Is either spouse 60 or over (pension exclusion, extra credit)?
   - Is either spouse 65 or over, or blind (extra standard deduction)?
   - Is the client someone else's dependent?
5. **Retirement income.**
   - What pensions, IRA/401(k) distributions, US military pension or Social Security did they receive?
   - How many years has each person aged 60 or over been domiciled in Delaware?
6. **Other-state income.** Did a Delaware resident pay income tax to another state (or DC) on the same income?
7. **Payments already made.** Delaware withholding (not city wage tax), 2026 estimated payments, and credit carried forward from 2025.
8. **Nonresident source income.** Which wages, business or rental income came from Delaware?

## Residency tests (30 Del. C. § 1103)

A **resident** is an individual who either:

- **(1)** is domiciled in Delaware, "to the extent of the period of such domicile"; or
- **(2)** "maintains a place of abode in this State and spends in the aggregate **more than 183 days** of the taxable year in this State."

On test (2):

- Exactly 183 days is not enough.
- The abode and the days must both be present.

**Foreign-presence exception to test (1).** A domiciliary is not treated as a resident for the period if all of these hold:

- they are present in a foreign country or countries for at least 495 full days in any consecutive 18-month period;
- during those 18 months they are in Delaware for not more than 45 days;
- they keep no permanent place of abode in Delaware where their spouse, children or parents are present for more than 45 days; and
- they are not a US government employee (including the Armed Forces).

Everyone who is not a resident is a **nonresident** (§ 1104).

## The method, step by step

### Step 1: Filing requirement (§ 1161; thresholds from the [2025 PIT-RES instructions](https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-RES_Instructions_2025-01.pdf))

**A resident must file if** they are required to file a federal return, or their Delaware-modified AGI is above the thresholds in the table below. The Division prints the thresholds in each year's instructions. The 2026 table is not yet published; the 2025 table is:

| 2025 threshold, by age/status (individual AGI) | Single / HoH / MFS | Joint | Claimed as a dependent |
|---|---|---|---|
| Under 60 | $9,400 | $15,450 | $5,250 |
| 60 to 64 | $12,200 | $17,950 | $5,250 |
| 65 and over, or blind | $14,700 | $20,450 | $7,750 |
| 65 and over and blind | $17,200 | $22,950 | $10,250 |

**A nonresident must file** if they had any gross income from Delaware sources.

**A part-year resident must file** if they had income from any source while a resident, or Delaware-source income while a nonresident.

### Step 2: Choose the return

- **Full-year resident:** PIT-RES.
- **Nonresident:** PIT-NON.
- **Part-year resident** (§ 1125) may choose either:
  - a **resident** return for the whole year, with the credit for tax paid to other states; or
  - a **nonresident** return, where the resident period's income counts as Delaware-source income.

  The instructions say you may prepare both and file the one that is more advantageous.

The Volunteer Firefighter, Child Care and Earned Income Tax Credits cannot be taken on PIT-NON.

**Spouses** (§ 1162):

- If they filed separate federal returns, they must file separate Delaware returns.
- If they filed a joint federal return, they may file joint, separate, or "combined separate" (filing status 4) in Delaware.
- If one spouse is a resident and the other is not, they file separately unless both elect to file jointly as residents.

Delaware applies **one rate schedule to every filing status.** For a two-earner couple, separate or combined separate filing is often cheaper; compare both.

If spouses file separately:

- both must use the same deduction method, standard or itemized; and
- each reports their own income plus half of jointly held investment income.

### Step 3: Start from federal AGI (§§ 1101, 1105)

Delaware taxable income starts from **federal adjusted gross income**. Delaware adopts the Internal Revenue Code "as the same may have been or shall become effective, for any taxable year." This is rolling conformity: federal changes, including P.L. 119-21 (the One Big Beautiful Bill Act, OBBBA), apply automatically unless Delaware decouples.

The Division states: "Delaware conforms with Federal Adjusted Gross Income (AGI) and with federal definition of Itemized Deductions." It also states that the OBBBA deductions for tips, overtime and car loan interest "are not defined federally as itemized deductions and will not flow through to the Delaware Personal Income Tax." Source: https://revenue.delaware.gov/tax-season-updates/

The Division's page does not address the federal additional deduction for seniors. Confirm with the Division before assuming it affects Delaware.

### Step 4: Additions ([§ 1106(a), (d)](https://delcode.delaware.gov/title30/c011/sc02/index.html))

1. **Other states' bond interest.** Add interest on state and local bonds of states other than Delaware, and the matching mutual-fund dividends.
2. **Oil and gas percentage depletion.** Add it back to the extent it exceeds cost depletion.
3. **Net operating loss carryback.** Add the part of a federal carryback deduction above the $30,000 limit.
4. **OBBBA depreciation decoupling (new for 2026).** Under HB 255 (85 Del. Laws c. 231), for individuals from 1 January 2026:
   - Property acquired and placed in service after 31 December 2025 and before 1 January 2031, if it would otherwise get 100% expensing under OBBBA § 70301, is depreciated in Delaware under the Code "in effect immediately before the enactment of § 70301."
   - Qualified production property (OBBBA § 70307) placed in service in the same window follows the same rule.
   - The Division's Technical Information Memorandum 2025-2 says the TCJA schedule continues: "tax year 2026 bonus depreciation is permitted at 20%; and tax year 2027 and later bonus depreciation is 0%."
   - Keep a separate Delaware depreciation schedule for these assets. Their Delaware basis and later gain or loss will differ from federal.
   - The Act names only §§ 70301 and 70307. It does not decouple from the other OBBBA provisions.
   - The 2026 PIT-RES line for this adjustment is not yet published.

   Sources: https://delcode.delaware.gov/sessionlaws/ga153/chp231.shtml and https://revenuefiles.delaware.gov/2025/TIMs/HB_255_TIM.pdf

### Step 5: Subtractions ([§ 1106(b)](https://delcode.delaware.gov/title30/c011/sc02/index.html))

1. **US government interest.** Subtract interest on US obligations (and the matching mutual-fund dividends) that federal law exempts from state tax. Agency paper that is not a US obligation, such as Fannie Mae, is not exempt.
2. **Social Security and Railroad Retirement benefits.** Subtract the amount included in federal AGI.
3. **Pension exclusion, per person, for 2026** (§ 1106(b)(3)b, which applies to taxable years beginning on 1 January 2022 and ending before 1 January 2027):

   **Under age 60:** the greater of:
   - pensions received, up to **$2,000**; or
   - a US military pension, up to **$12,500**.

   **Age 60 or older:** pensions plus "eligible retirement income", up to **$12,500**. Eligible retirement income means:
   - qualified-plan, 401(k) and 457 distributions;
   - dividends, capital gains and interest;
   - rental income from real property, less deductible rental expenses.

   Income held by spouses as joint tenants with right of survivorship, or as tenants by the entirety, is treated as received half by each.

   **Each person gets one exclusion.** An early distribution (Form 1099-R code 1, or a distribution subject to the federal early-withdrawal penalty) does not qualify.

   **Domicile condition for age 60 or older.** A 2026 Act, SB 219 as amended by SA 1 (85 Del. Laws c. 426), added § 1106(b)(3)f.4. Under it, a person aged 60 or older gets this subtraction only if:
   - they were legally domiciled in Delaware before 1 January 2027 and have been domiciled there for **at least 3 years**; or
   - they became domiciled on or after 1 January 2027 and have been domiciled there for **at least 5 years**.

   For this rule, "legally domiciled" means being a "resident individual" under § 1103 (§ 1106(b)(3)f.4.B). That includes a statutory resident under test (2): a place of abode plus more than 183 days, even without domicile in the ordinary sense.

   The Act has no effective-date section, and the Code text gives no starting tax year. The 2025 instructions predate the Act, and no 2026 instructions exist yet. For a client aged 60 or over who has been domiciled in Delaware for less than 3 years, confirm with the Division before claiming the exclusion.

   **From 2027** (§ 1106(b)(3)c to e):
   - The US military pension cap rises to **$15,000** for 2027, **$20,000** for 2028, and **$25,000** for 2029 and later.
   - People aged 60 or over get the greater of the $12,500 exclusion or the military amount.
4. **Elderly or disabled low-income exclusion.** Available to a person over 60, or totally and permanently disabled, whose earned income is less than $2,500 **and** whose AGI does not exceed $10,000. The exclusion is $2,000.
   - On a joint return where both spouses qualify: $4,000, if combined earned income is less than $5,000 and AGI does not exceed $20,000.
5. **Delaware income tax refunds** included in federal AGI.
6. **DE529 contributions**, up to $1,000 ($2,000 for a joint return).
   - Not allowed if federal AGI is greater than $100,000, or greater than $200,000 on a joint return.
   - Rollovers, beneficiary changes and K–12 tuition contributions do not count.
7. **Delaware ABLE contributions**, up to $5,000 ($10,000 for a joint return).
8. **Other items:** the work opportunity credit wage adjustment, Delaware NOL carryforwards blocked by the carryback limit, and fiduciary adjustments.

The result is **Delaware AGI**.

### Step 6: Deduction ([§§ 1107–1109](https://delcode.delaware.gov/title30/c011/sc02/index.html))

**Standard deduction.** It is fixed in the statute and not indexed, so the 2026 amounts are the § 1108 amounts:

| Filing status | Standard deduction |
|---|---|
| Single, head of household | $3,250 |
| Married filing jointly | $6,500 |
| Married filing separately (each) | $3,250 |

**Additional standard deduction.** Add $2,500 for each of:

- the taxpayer being 65 before the end of the year;
- the taxpayer being blind at year end;
- the same for a spouse, subject to the rules on a spouse's own filing.

This applies only if the standard deduction is used. The maximum is $5,000 per person.

**Itemized deductions.** The client may itemize in Delaware even if they took the federal standard deduction. Start from the federal itemized deductions, then:

- **remove** Delaware income tax;
- **remove** other states' income tax claimed as a credit under § 1111;
- **add** the self-employed health insurance not deducted federally, subject to the conditions in § 1109(a)(2)b;
- **add** union dues up to $500 where not deducted federally.

Spouses who both must file may itemize only if both elect to.

**Delaware AGI minus the deduction = Delaware taxable income.**

### Step 7: Tax ([§ 1102(a)(14)](https://delcode.delaware.gov/title30/c011/sc01/index.html): rates for taxable years beginning after 31 December 2013)

| Taxable income | Rate on the slice |
|---|---|
| $0 – $2,000 | 0% |
| over $2,000 – $5,000 | 2.2% |
| over $5,000 – $10,000 | 3.9% |
| over $10,000 – $20,000 | 4.8% |
| over $20,000 – $25,000 | 5.2% |
| over $25,000 – $60,000 | 5.55% |
| over $60,000 | 6.6% |

**Which method to use:**

- **Below $60,000:** use the Division's tax table (§ 1102(d)). It works in $50 bands, so it can differ by a few dollars from the formula.
- **$60,000 or more:** tax = **$2,943.50** plus 6.6% of the excess over $60,000. The $2,943.50 is the tax on the first $60,000 from the published tax schedule. Note that the 2026 PIT-EST worksheet prints this figure as $2,943.00; the statute and rate schedule give $2,943.50.

**Cumulative tax at each bracket top:**

| At | Tax |
|---|---|
| $5,000 | $66 |
| $10,000 | $261 |
| $20,000 | $741 |
| $25,000 | $1,001 |
| $60,000 | $2,943.50 |

**No 2026 rate change is in the Code.** Bills to add higher brackets were introduced in the 2025–2026 session, but § 1102 as published on delcode.delaware.gov still shows paragraph (a)(14) as the current schedule. Re-check § 1102 before filing if the client has income well above $60,000.

**Lump-sum distributions** have a separate tax (§ 1102(b), Form PIT-STC). Refer these (see "When to refuse or refer").

### Step 8: Credits ([§§ 1110–1117](https://delcode.delaware.gov/title30/c011/sc02/index.html))

- **Personal credit (§ 1110):**
  - $110 for each personal exemption the client would be entitled to federally: themselves, a spouse on a joint return, and each dependent.
  - The instructions confirm it is still allowed "even though you do not recognize personal exemptions on your federal return."
  - Add an extra $110 for each person aged 60 or over.
  - A person claimed as someone else's dependent gets no personal credit.
  - The credit cannot exceed the tax.
- **Credit for tax paid to another state (§ 1111).** Residents only; covers income taxed by another state or DC.
  - It is limited to Delaware tax × (income from that state ÷ total taxable income).
  - Attach a signed copy of the other state's return.
- **Earned income tax credit (§ 1117).** Residents may choose either:
  - a non-refundable credit of **20%** of the federal credit; or
  - a refundable credit of **4.5%** of the federal credit.
- **Volunteer firefighter credit, child and dependent care credit, and business credits (Form PIT-CRS).** These are outside the core method. Check each one's conditions in the instructions.

### Step 9: Nonresidents (§§ 1121–1124)

1. Compute Delaware AGI on **all** income, as if the client were a resident (PIT-NON Column A).
2. Compute Delaware-source income (Column B):
   - employee pay for services **(a)** rendered in Delaware, or **(b)** "attributable to employment in this State and not required to be performed elsewhere" (§ 1124(b)(1));
   - Delaware real or tangible property;
   - a business carried on in Delaware.

   **Days worked outside Delaware for a Delaware job.** Pay for these days can be excluded only if the employer required the work to be done outside Delaware.
   - Claim the exclusion on Form PIT-SCW: https://revenuefiles.delaware.gov/2025/PITForms_Instructions/PIT-SCW_2025-01_PaperInteractiveIPM.pdf
   - The form apportions by days: Delaware-source wages = wages × (days worked in Delaware ÷ total days worked).
   - The allowance "must be based on necessity of work outside the State of Delaware in performance of duties for the employer, as opposed to solely for the convenience of the employee."
   - The PIT-NON instructions say: "Working from home does not qualify for an exclusion on Form PIT-SCW."
   - The form adds one exception: a home office counts only if "working from home is a requirement of employment with your employer."
   - Days worked from home by choice stay Delaware days.

   Intangible income (interest, dividends, gains) is Delaware-source only if the property is used in a Delaware business. Military pay of a nonresident servicemember is not Delaware-source income.
3. Compute the tax on the full taxable income with the full rate schedule. Subtract the personal credits.
4. Multiply by the **proration decimal**: Delaware-source income ÷ Delaware AGI. The instructions say to round it to four decimal places; it cannot exceed 1.0000 or be below zero.

## Figures and years at a glance ([Title 30, Chapter 11](https://delcode.delaware.gov/title30/c011/sc02/index.html))

| Item | 2026 | 2025 | Source |
|---|---|---|---|
| Top rate | 6.6% over $60,000 | same | § 1102(a)(14) |
| Standard deduction (single / joint) | $3,250 / $6,500 | same | § 1108 |
| Additional standard deduction (65+ or blind) | $2,500 each | same | § 1108(b) |
| Personal credit | $110 per exemption, plus $110 for 60+ | same | § 1110 |
| Pension exclusion, under 60 | $2,000 (US military pension: $12,500) | same | § 1106(b)(3)b |
| Pension exclusion, 60+ | $12,500 (domicile condition, see step 5) | $12,500 | § 1106(b)(3)b, f.4 |
| Bonus depreciation, individuals | 20% (TCJA schedule), not OBBBA 100% | follows federal | HB 255; Technical Information Memorandum 2025-2 |
| Estimated tax required if tax less credits exceeds | $800 | same | § 1169 |
| Interest on late payment | 0.5% per month | same | § 533 |

## Boundary and exception table ([§ 1103](https://delcode.delaware.gov/title30/c011/sc01/index.html))

| Situation | Rule | Result |
|---|---|---|
| Abode in Delaware, domiciled elsewhere, exactly 183 days in Delaware | Statutory residency needs **more than 183 days** | Nonresident |
| Same, 184 days | More than 183 days, with an abode | Resident for the whole year |
| Domiciliary abroad 495+ days in 18 months, 45 or fewer days in Delaware, no family abode in use over 45 days, not a US employee | § 1103(1) exception | Not a resident for that period |
| Taxable income exactly $60,000 | Instructions: "$60,000 or greater, use the tax schedule" | $2,943.50 |
| Expected tax after withholding and credits exactly $800 | A declaration is required only if it "can reasonably be expected to exceed $800" | No estimated tax declaration required |
| Turns 60 on 31 December 2026 | Age is tested at year end ("60 years of age or over on December 31") | 60+ exclusion and extra $110 credit apply, if the domicile condition is met |
| Turns 65 on 31 December 2026 | § 1108(b): "attained the age of 65 before the close of the taxable year" | Extra $2,500, standard deduction only |
| Under 60 with an early IRA distribution (1099-R code 1) | Not a qualifying pension | No exclusion for that distribution |
| DE529 contribution, single filer with federal AGI just over $100,000 | Denied if AGI is "greater than $100,000" | No subtraction |
| Nonresident spouse of a resident | § 1162(a)(4) | Separate returns unless both elect to file jointly as residents |
| 2026 equipment, 100% bonus depreciation federally | HB 255, § 1106(d) | Delaware allows 20% bonus plus regular depreciation; add back the difference |
| Nonresident with a Delaware job, working some days at home by choice | § 1124(b)(1)b; the PIT-NON instructions say "Working from home does not qualify for an exclusion on Form PIT-SCW" ([instructions](https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-NON_Instructions_2025-01.pdf)) | Home days remain Delaware-source wages |
| Same, but the employer requires out-of-state client work on some days | [Form PIT-SCW](https://revenuefiles.delaware.gov/2025/PITForms_Instructions/PIT-SCW_2025-01_PaperInteractiveIPM.pdf): allowance for days worked outside Delaware out of necessity | Exclude wages × (required days outside ÷ total days worked) |
| City wage tax withheld | Not Delaware tax | Leave it out of Delaware tax withheld |

## Worked cases (tax year 2026; rates from [§ 1102](https://delcode.delaware.gov/title30/c011/sc01/index.html))

**Case A: single resident, wages only.**
- Federal AGI = wages $85,000; no modifications. Delaware AGI = $85,000.
- Standard deduction $3,250, so taxable income = $81,750.
- Tax = $2,943.50 + ($81,750 − $60,000) × 6.6% = $2,943.50 + $1,435.50 = $4,379.00.
- Personal credit $110.
- **Delaware tax = $4,269.00.**

**Case B: married couple, both 67, joint return.** Both have been domiciled in Delaware for more than 3 years.
- Federal AGI $130,000, made up of:
  - taxable Social Security $20,000;
  - two employer pensions of $15,000 each;
  - jointly held interest and dividends of $80,000.
- **Subtractions:**
  - Social Security: $20,000.
  - Pension exclusion: each spouse has $15,000 of pension plus $40,000 of eligible retirement income, so each is capped at $12,500. Together $25,000.
- Delaware AGI = $130,000 − $20,000 − $25,000 = $85,000.
- **Deduction:** $6,500 + 2 × $2,500 = $11,500. Taxable income = $73,500.
- **Tax** = $2,943.50 + $13,500 × 6.6% = $2,943.50 + $891.00 = $3,834.50.
- **Credits:** two personal credits plus two 60+ credits, 4 × $110 = $440.
- **Tax = $3,394.50.**
- Also compute combined separate (filing status 4). With one rate schedule, splitting income can lower the total.

**Case C: nonresident.** Lives in Pennsylvania, works in Delaware, single, age 45.
- Delaware wages $70,000 plus Pennsylvania-source interest $10,000, so federal AGI and Delaware AGI (Column A) = $80,000.
- Taxable income as if resident = $80,000 − $3,250 = $76,750.
- Tax = $2,943.50 + $16,750 × 6.6% = $2,943.50 + $1,105.50 = $4,049.00. Less the personal credit $110 = $3,939.00.
- Proration = $70,000 ÷ $80,000 = 0.8750.
- **Delaware tax = $3,939.00 × 0.8750 = $3,446.63.**
- The interest is not Delaware-source because it is investment income, not income from property used in a Delaware business.

**Case D: sole proprietor, 2026 equipment.**
- The client buys a $100,000 machine and places it in service in June 2026. They take 100% bonus depreciation federally, deducting $100,000.
- **Delaware:** bonus depreciation is 20%, which is $20,000. The remaining $80,000 is depreciated under the pre-OBBBA rules (regular MACRS) from 2026.
- **Addition for 2026** = $100,000 minus the Delaware-allowed depreciation.
- **Later years:** subtract the Delaware depreciation claimed each year until the Delaware basis is used up.
- **On sale:** compute gain on the Delaware basis.

**Case E: nonresident, some work outside Delaware** ([Form PIT-SCW](https://revenuefiles.delaware.gov/2025/PITForms_Instructions/PIT-SCW_2025-01_PaperInteractiveIPM.pdf)).
- Lives in Maryland and works for a Delaware employer. Wages $90,000; 240 days worked in 2026.
- The employer required 40 days of client work in other states. The employee also worked 20 days from home by choice.
- Only the 40 required days are excluded. The 20 home days stay Delaware days.
- Delaware days = 240 − 40 = 200.
- **Delaware-source wages** = $90,000 × 200 ÷ 240 = $75,000. Exclusion = $15,000.
- If the home days were wrongly excluded too, Delaware wages would be understated by $7,500.

## When to refuse or refer

Refer to a Delaware-experienced professional, or the Division of Revenue (302-577-8200), for:

- **Residency disputes:** domicile changes, the foreign-presence exception, or dual-resident situations.
- **Military cases** involving the Servicemembers Civil Relief Act or the military spouse exemption (Form WTH-EXM).
- **Lump-sum distribution tax** (Form PIT-STC).
- **Business credits** (Form PIT-CRS), historic rehabilitation credits, and S corporation composite or nonresident-shareholder issues.
- **Allocation for a business carried on inside and outside Delaware** (§ 1124(f)).
- **Pension exclusion for a person aged 60 or over domiciled in Delaware for less than 3 years** (see step 5).
- **The 2026 depreciation adjustment** before the 2026 PIT-RES instructions are published, if the amounts are large.
- **City taxes**, including a city wage tax.
- **Fiduciary returns, estates and trusts.**

## Tax year 2025 returns (still open on extension to 15 October 2026; [2025 PIT-RES instructions](https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-RES_Instructions_2025-01.pdf))

- **Rates, standard deduction, credits and pension exclusion amounts are the same as 2026.**
  - The 60-or-over domicile condition in step 5 was enacted after the 2025 instructions were issued.
  - The Act does not say whether it reaches a 2025 return. For a recent arrival aged 60 or over, confirm with the Division before claiming the exclusion.
- **Bonus depreciation.** For individuals, Delaware's decoupling applies only to property placed in service after 31 December 2025. So 2025 PIT-RES follows the federal depreciation taken.
- **SALT cap.** The 2025 itemized deductions follow the federal cap of $40,000 ($20,000 married filing separately). It is reduced for federal modified AGI over $500,000 ($250,000 married filing separately). Delaware income tax must still be removed from itemized deductions.
- **Tips, overtime and car loan interest** deductions do not reduce Delaware income.
- **Extension.** It runs to 15 October 2026 only if Form PIT-EXT was filed by 30 April 2026. "THERE IS NO EXTENSION OF TIME FOR PAYMENT OF TAX." Interest has run at 0.5% per month from 30 April 2026 on any unpaid balance.
- **Penalty exceptions for 2025 estimated tax.** The prior-year safe harbour uses the 2024 tax, at 110% if 2024 Delaware AGI was over $150,000 ($75,000 married filing separately).

## Filing and payment steps with deadlines (2026 tax year; [PIT-EST instructions](https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-EST_Instructions_2026-01.pdf))

1. **Estimated tax (§§ 1169–1170; PIT-EST).**
   - Required if 2026 tax, less withholding and credits, can reasonably be expected to exceed $800.
   - Due dates: 30 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027. Pay online at tax.delaware.gov or by paper voucher.
   - **Underpayment penalty:** 1.5% per month on each late or short instalment.
   - **No penalty if each instalment is paid on time and totals at least:**
     - 90% of the 2026 tax; or
     - 100% of the 2025 tax, or 110% if 2025 AGI exceeded $150,000 ($75,000 married filing separately).

     The PIT-EST instructions test federal AGI for the previous year; the PIT-RES and PIT-UND instructions test Delaware AGI. If only one of the two is over the limit, use 110% to be safe.
   - **No payment is required** if there was no tax liability for a full 12-month prior year.
   - **Farmers and fishermen** have their own rule.
   - Compute the penalty on Form PIT-UND, not federal Form 2210.
2. **Return due 30 April 2027** (§ 1168: the 30th day of the fourth month after year end). Pay any balance by the same date.
3. **Extension.** File PIT-EXT, with the estimated balance, by 30 April 2027. This moves the filing date, but not the payment date.
   - The 2025 form extended filing to 15 October.
   - Confirm the 2026 date on the 2026 PIT-EXT when it is published.
4. **Attachments:**
   - pages 1 and 2 of federal Form 1040 and its schedules;
   - W-2 and 1099-R forms;
   - the signed other-state return if claiming § 1111;
   - Form PIT-RSA if itemizing;
   - Form PIT-UND if a penalty is computed.
5. **Federal changes (§ 514).** Report an IRS change, or file an amended Delaware return, within 90 days of the final federal determination or amended federal return.

**Penalties and interest (Title 30, Chapter 5):**

- **Late filing** (§ 534(a)): 5% of the net tax due per month or part month, up to 50%.
- **Late payment** (§ 534(b)): 1% per month, up to 25%.
- **Interest** (§ 533): 0.5% per month or fraction, from the original due date regardless of any extension.
- **Accuracy-related penalty** (§ 536): 20% of the underpayment for negligence or a substantial understatement, 40% for a gross valuation misstatement.
- Fraud penalties are separate (§ 535).

## Completion checklist ([2025 PIT-RES instructions](https://revenuefiles.delaware.gov/2025/PITForms_Instructions/Instructions/PIT-RES_Instructions_2025-01.pdf))

- [ ] Residency tested under both § 1103 tests, (1) and (2), with the day count recorded.
- [ ] Correct form (PIT-RES / PIT-NON). For a part-year resident, both options compared.
- [ ] Federal AGI taken from the final federal return. OBBBA below-the-line deductions not carried into Delaware.
- [ ] Additions made: non-Delaware municipal interest, and the 2026 depreciation adjustment for post-2025 property.
- [ ] Subtractions made: US interest, Social Security, the pension exclusion (per person, age and domicile checked), DE529 and ABLE within their limits.
- [ ] Standard or itemized deduction chosen; both spouses consistent if filing separately.
- [ ] Tax from the table (below $60,000) or the schedule ($60,000 and above).
- [ ] Personal credits ($110 each, plus the 60+ credit). Other-state credit limited by the ratio. EITC option chosen.
- [ ] For a married couple, joint versus combined separate compared.
- [ ] Withholding excludes city wage tax. Estimated payments and carryforward matched to Division records.
- [ ] PIT-UND checked if the balance due is more than 10% of the tax: the client "may owe" the penalty. Attach PIT-UND if the computed penalty is greater than zero, or if Part 3 (annualised method) is used.
- [ ] Filed and paid by 30 April 2027, or PIT-EXT filed with payment.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
