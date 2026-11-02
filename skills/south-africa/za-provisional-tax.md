---
name: za-provisional-tax
description: Use this skill whenever asked about South African provisional tax (IRP6) for self-employed individuals. Trigger on phrases like "IRP6", "provisional tax", "SARS provisional", "estimated tax South Africa", "first provisional period", "second provisional period", "third provisional", "underestimation penalty", or any question about South African provisional tax obligations for self-employed persons. Covers first period (Aug 31), second period (Feb 28), voluntary third period (Sep 30), underestimation penalties, basic amount rules, and edge cases. ALWAYS read this skill before touching any South African provisional tax work.
version: 2.0
jurisdiction: ZA
tax_year: 2025
last_updated: 2026-07-13
authored_by: Werner Britz, CA(SA)
reviewed_by: Werner Britz
review_status: current
trust_label: Checked by Werner Britz
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ZA Provisional Tax

## South Africa Provisional Tax (IRP6) -- Self-Employed Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Werner Britz** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Provisional Tax

- **Country** — South Africa
- **Authority** — SARS
- **Primary legislation** — Income Tax Act 58 of 1962, Fourth Schedule
- **Supporting legislation** — Tax Administration Act 28 of 2011
- **Year of assessment** — 1 March to 28/29 February  _(Income Tax Act s 1, definition)_
- **First period due** — 31 August  _(Fourth Schedule para 21)_
- **Second period due** — 28/29 February  _(Fourth Schedule para 21)_
- **Third period (voluntary)** — 30 September  _(Fourth Schedule para 23A)_
- **Underestimation threshold (<= R1M)** — The AND logic in the skill is correct as a description of the penalty TRIGGER. Para 20(1)(b) imposes the penalty only where BOTH conditions are breached: estimate < 90% of actual AND estimate < basic amount. To AVOID penalty, the taxpayer needs EITHER condition met. In practice, paying at least the basic amount is the easy route and the 90% rule is largely irrelevant - it only matters where the taxpayer deliberately estimates BELOW the basic amount (for instance, a genuine drop in income from prior year) and needs a fallback. Two corrections remain: (1) threshold moves from R1m to R1.8m for years of assessment commencing on or after 1 March 2026 (Budget 2026); (2) the skill's phrasing "90% of actual AND >= basic amount" is ambiguous - it reads as a single composite test where the >= sign attaches to the basic amount. Clearer rewrite: "Penalty applies if estimate < 90% of actual income AND estimate < basic amount. To avoid penalty: estimate >= basic amount (safe harbour), or estimate >= 90% of actual."  _(Fourth Schedule para 20(1)(b); SARS Budget 2026 Tax Guide; SARS Guide to Provisional Tax; SARS IN 1 (Provisional Tax Estimates))_
- **Underestimation threshold (> R1M)** — Threshold raised to R1.8m for years of assessment commencing on or after 1 March 2026. Above the threshold, no basic-amount safe harbour: the estimate must be at least 80% of actual to avoid penalty. Para 20(1)(a) applies.  _(Fourth Schedule para 20(1)(a); SARS Budget 2026 Tax Guide)_
- **Penalty rate** — 20% of shortfall  _(Fourth Schedule para 20)_
- **Interest rate (s89quat)** — Current rate 10.25% p.a. from 2 March 2026 on late or underpaid tax. Rate on refund of overpayments is lower (6.25%). Rate is set quarterly by SARS by reference to repo rate plus a margin. Reference the SARS Interest Rates page rather than hardcoding.  _(TAA s 187; SARS Interest Rates page; SARS Budget 2026 Tax Guide)_
- **Tax threshold (under 65, 2025)** — 2026/27 (YOA 2027): R99,000. Below threshold, no income tax and not a provisional taxpayer.  _(Income Tax Act s 6; SARS Budget 2026 Tax Guide)_
- **Filing method** — SARS eFiling (IRP6)
- **Currency** — ZAR only

Update after sign-off.

- **Is client a provisional taxpayer?** — Receives income not subject to PAYE?  _(Fourth Schedule para 1)_

- **Prior year taxable income** — Basic amount is the taxable income reflected in the latest preceding ASSESSMENT, not just prior year. If the prior year is unassessed at the time of the IRP6, you go back to the most recent assessed year. Skill should be specific: "the taxable income per the most recent ASSESSED year of assessment, increased by 8% per annum if the assessment is more than 14 months old at the IRP6 due date (para 19(1)(d))".  _(Fourth Schedule para 19)_

- **PAYE credits?** — Offset against provisional tax  _(Fourth Schedule para 21)_
- **Expected taxable income above R1,000,000?** — R1.8m from 1 March 2026.  _(Fourth Schedule para 20; SARS Budget 2026)_
- **R-ZA-PROV-1: Tax dispute / objection** — Objections to SARS penalties require qualified tax practitioner review. Escalate.  _(TAA Chapter 9; Dispute Resolution Rules)_
- **R-ZA-PROV-2: Company provisional tax** — This skill covers individuals only. Companies have different rules.  _(Fourth Schedule para 19 and para 20)_
- **NEVER estimate without asking about ALL income sources** — NEVER estimate without asking about ALL income sources
- **NEVER tell a client with income > R1M that basic amount protects them - it does not** — Substantively correct as a rule. Update threshold to R1.8m from 1 March 2026. Above the threshold, the basic-amount safe harbour does not apply; the only path is to estimate within 80% of actual.  _(Fourth Schedule para 20(1)(a); SARS Budget 2026)_
- **NEVER ignore PAYE credits** — NEVER ignore PAYE credits
- **NEVER confuse underestimation penalty with s89quat interest** — NEVER confuse underestimation penalty with s89quat interest  _(Fourth Schedule para 20; Income Tax Act s 89quat)_
- **NEVER assume third period is mandatory - it is voluntary** — NEVER assume third period is mandatory - it is voluntary  _(Fourth Schedule para 23A)_
- **NEVER present provisional tax as a separate tax - it is a prepayment** — NEVER present provisional tax as a separate tax - it is a prepayment
- **NEVER compute penalties without both estimate AND actual** — NEVER compute penalties without both estimate AND actual
- **NEVER use outdated SARS interest rates** — NEVER use outdated SARS interest rates  _(TAA s 187)_
- **MISSING prohibition: late payment** — Add: "Never advise that an estimate within tolerance protects against penalty if the payment is late." From 25 February 2026, the 20% underestimation penalty applies even where the estimate is correct but the payment is late (Budget 2026 amendment to para 20).  _(Fourth Schedule para 20 (amended); SARS Budget 2026)_
- **Self-employed / sole proprietor** — YES  _(Fourth Schedule para 1)_
- **Freelancer / contractor** — YES  _(Fourth Schedule para 1)_
- **Rental income recipient** — YES (if above threshold)  _(Fourth Schedule para 1)_
- **Director receiving director's fees** — Distinction needed. EXECUTIVE directors are common law employees with PAYE deducted from their remuneration - they would fall under the "salaried employee" row and are NOT provisional taxpayers solely on account of director's fees. NON-EXECUTIVE DIRECTORS (NEDs) are different: per BGR 40 (effective 1 June 2017), an NED is not a common law employee, no PAYE is to be deducted on NED fees, and the NED is a provisional taxpayer. Exception: non-resident NEDs - PAYE is compulsory for them under para 2(1A) of the Fourth Schedule. Cross-reference VAT angle: per BGR 41, an NED carrying on an enterprise must register for VAT if NED fees exceed the compulsory threshold (R2.3m from 1 April 2026; previously R1m); voluntary registration available above R120,000. This is an often-overlooked compliance trap - NEDs on multiple boards easily exceed the threshold without realising.  _(Fourth Schedule para 1 and para 2(1A); SARS BGR 40 (10 February 2017); SARS BGR 41 (Issue 2, 4 May 2017); SARS FAQs on BGRs 40 and 41)_
- **Salaried employee ONLY (all PAYE)** — Generally correct, but a salaried employee with significant taxable interest, dividends, or rental income may still be a provisional taxpayer. The exemption in para 18 covers this: a natural person is not a provisional taxpayer if their taxable income from non-remuneration sources, comprising interest, foreign dividends, rental, and remuneration NOT subject to PAYE, does not exceed R30,000.  _(Fourth Schedule para 18)_
- **Under 65, taxable income <= R95,750** — R99,000 for 2026/27. The threshold matches the income tax threshold.  _(Income Tax Act s 6)_
- **Exemption (additional)** — Restate per para 18: a natural person is not a provisional taxpayer if (a) they do not carry on a business, AND (b) their taxable income for the year will not exceed the tax threshold; OR they derive non-remuneration income (interest, foreign dividends, rental, remuneration not subject to PAYE) not exceeding R30,000.  _(Fourth Schedule para 18)_
- **First (IRP6): first 6 months, 31 Aug** — Refinement: pay half of (estimated annual tax LESS first PAYE less primary rebate). The formula on the IRP6 form: estimated annual taxable income -> estimated annual tax -> less rebates -> less medical credits -> less PAYE for the six months -> result x 50%. Skill should give the exact computation.  _(Fourth Schedule para 21(1))_
- **Second (IRP6): full year, 28 Feb** — Refinement: estimate annual taxable income; compute annual tax; less rebates and credits; less PAYE; less first provisional payment. The estimate at second period must comply with para 19 (basic amount or full-year estimate) to avoid penalty.  _(Fourth Schedule para 21(2) and para 19)_
- **Third (voluntary): top-up, 30 Sep** — Avoids interest on underpayment  _(Fourth Schedule para 23A)_
- **Basic amount = prior year's assessed taxable income. Safe harbour benchmark.** — Refinement: basic amount = taxable income per the latest preceding ASSESSMENT, EXCLUDING taxable capital gains and any retirement lump sum or severance benefit. If the latest assessment is older than 14 months at the start of the year being estimated, the basic amount is increased by 8% per annum for each year the assessment is "old". For example: estimating for YOA 2027 (year starting 1 March 2026), 14 months before that is 1 January 2025. If the latest assessment was issued before 1 January 2025, increase by 8%.  _(Fourth Schedule para 19(1)(d))_
- **Prior year assessed** — See above. Specifically taxable income EXCLUDING taxable capital gains, retirement lump sums, and severance benefits.  _(Fourth Schedule para 19(1)(d))_
- **No prior assessment** — Correct in practice but technically "basic amount is nil" - no safe harbour available. Taxpayer must estimate accurately (within 90% / 80% as applicable).  _(Fourth Schedule para 19)_
- **Prior year loss** — Zero  _(Fourth Schedule para 19)_

Add as a worked example: latest assessment for YOA 2024 (year ended Feb 2024), issued January 2025. Estimating for YOA 2026 first provisional (due Aug 2025). Period 14 months before 1 March 2025 is 1 January 2024. Assessment date Jan 2025 is after that benchmark, so no escalation. But for estimating YOA 2027 (Aug 2026 first prov), period 14 months before 1 March 2026 is 1 January 2025. Same assessment falls before this benchmark by less than a year - no escalation yet. If we get to YOA 2028 (Aug 2027 first prov) without a newer assessment, the basic amount escalates by 8%. (Fourth Schedule para 19(1)(d)(iii))

- **First period: no underestimation penalty** — Penalty applies only to second period  _(Fourth Schedule para 20)_

- **Threshold <= R1,000,000** — AND logic in skill is correct - both conditions must breach for penalty to trigger. Below R1.8m (new threshold from 1 March 2026), penalty applies under para 20(1)(b) where estimate < 90% of actual AND estimate < basic amount. To avoid penalty: estimate >= basic amount (the practical safe harbour) OR estimate >= 90% of actual. The basic amount route is so much easier that the 90% rule is in practice a fallback for cases where the taxpayer intentionally estimates below basic (genuine drop in income, business cessation, illness, etc.).  _(Fourth Schedule para 20(1)(b); SARS IN 1; SARS Budget 2026)_
- **Threshold > R1,000,000** — Threshold R1.8m from 1 March 2026. Para 20(1)(a): estimate must be at least 80% of actual to avoid penalty. No basic-amount safe harbour above the threshold.  _(Fourth Schedule para 20(1)(a); SARS Budget 2026)_
- **Safe harbour <= R1M** — Threshold R1.8m from 1 March 2026. Substantively correct: estimating at least the basic amount is sufficient to avoid the para 20 underestimation penalty regardless of how much the actual income exceeds the estimate. This is the standard practitioner approach. The 90% of actual fallback exists for cases where the taxpayer reasonably estimates below basic amount (genuine income decline) and needs a second protective threshold.  _(Fourth Schedule para 20(1)(b); SARS Budget 2026)_
- **Safe harbour > R1M** — Threshold R1.8m. Above this, no basic-amount safe harbour; estimate must be at least 80% of actual.  _(Fourth Schedule para 20(1)(a); SARS Budget 2026)_
- **Penalty calculation: 20% x (tax on 80% of actual - tax on estimated)** — Formula simplified. Correct para 20 penalty: where actual <= R1.8m and estimate < basic and < 90% of actual: 20% x (tax on lesser of basic amount and 90% of actual - tax on estimate). Where actual > R1.8m and estimate < 80% of actual: 20% x (tax on 80% of actual - tax on estimate). The skill's single formula is correct only for the over-R1m case.  _(Fourth Schedule para 20)_

- **Effect: reduces interest, NOT the underestimation penalty** —   _(Fourth Schedule para 20)_
- **s89quat interest rate ~10.75% p.a. (verify current)** — Current 10.25% p.a. from 2 March 2026 on shortfall; 6.25% on refund of overpayment. Set quarterly by reference to repo rate plus margin.  _(TAA s 187; SARS Interest Rates page)_
- **Registration** — Registration is automatic once a taxpayer's circumstances meet the para 1 definition. Formal registration is not strictly required - SARS will issue an IRP6 if they detect provisional taxpayer characteristics. eFiling auto-creates the IRP6 line in the profile. Branch registration is largely obsolete.  _(Fourth Schedule para 1; SARS eFiling)_
- **Payment calculation formula** — Refinement: at each period the formula nets out rebates and medical credits before halving or topping up. First period: ((annual taxable income estimate -> tax per rates - rebates - medical credits) - PAYE for 6 months) / 2. Second period: (full-year annual tax less rebates less medical credits less PAYE) less first provisional. Third period: top-up to reach 100% of actual tax (less first, second, and PAYE).  _(Fourth Schedule para 21)_

Basic amount = zero. No safe harbour. Must estimate accurately. (Fourth Schedule para 19)

For YOA 2027 onwards: threshold is R1.8m. R1,050,000 is below the new threshold so the basic-amount safe harbour DOES apply (provided basic amount was used). Re-cast example for the new threshold: "Actual R1,900,000. Must estimate within 80% (R1,520,000+)". (Fourth Schedule para 20; SARS Budget 2026)

Prior loss. Current R500k. Basic amount = zero. No safe harbour. (Fourth Schedule para 19 and para 20)

R1.2m is below the new R1.8m threshold so basic amount safe harbour applies. Re-cast example. But note: even below R1.8m, mixed-income taxpayers often miss provisional tax because they think PAYE on salary is enough. (Fourth Schedule para 18 and para 20)

The conclusion is correct: estimating below basic amount triggers the penalty (assuming estimate is also < 90% of R700k = R630k, which R350k is). The "R450k (basic amount)" appears to be a typo - the basic amount per the setup is R400k. If the client had estimated at least R400k (the basic amount) the safe harbour would apply and no penalty. Note: in this example, EITHER threshold being met would protect: estimate of R400k+ (basic amount safe harbour) OR estimate of R630k+ (90% of actual). Either works in isolation. (Fourth Schedule para 20(1)(b))

Realises in August that second estimate too low. Third payment by Sep 30 reduces interest but not penalty. (Fourth Schedule para 20; Income Tax Act s 89quat)

Started business October 2024. Must file second provisional by Feb 28. Flag for reviewer on first period. (Fourth Schedule para 21)

Closes business November 2024. Still files second provisional by Feb 28. (Fourth Schedule para 21)

EC9 (suggested): client sells a property mid-year and realises a R500k capital gain. The taxable capital gain (40% inclusion = R200k) is income for the second provisional estimate but is EXCLUDED from the basic amount calculation. Practitioner must include the CGT effect in the estimate even though basic amount excludes it. (Fourth Schedule para 19(1)(d) and para 20)

EC10 (suggested): client receives a retirement lump sum mid-year. The lump sum is taxed separately under the retirement fund lump sum tables (not at marginal rates) and EXCLUDED from the basic amount and from the provisional tax estimate base. (Fourth Schedule para 19; Income Tax Act Second Schedule)

EC11 (suggested): from 25 February 2026, the 20% underestimation penalty applies even where estimate is within tolerance but payment is late. Critical change to highlight. (Fourth Schedule para 20 (amended); SARS Budget 2026)

Tier T2 format with client, situation, issue, options, recommended, action required

Tier T3 format for outside scope

Re-run on 2026/27 rates: R600k taxable -> annual tax R44,136 + 26%*(R600,000 - R245,200) = R44,136 + R92,248 = R136,384 - R17,820 rebate = R118,564 net of rebate. First period: R59,282. (SARS Budget 2026 Tax Guide)

Conceptually right: estimate equals basic amount, safe harbour applies. Under the new R1.8m threshold, same conclusion for these numbers. (Fourth Schedule para 20)

The under-threshold formula is not "tax on 80% of actual - tax on estimate"; that is the OVER-threshold formula. Per para 20(1)(b), where both legs are breached for an under-threshold taxpayer: penalty = 20% x [tax on 90% of actual taxable income - tax on basic amount]. For this example: 90% of R800k = R720k. Tax on R720k less tax on R400k (basic amount), multiplied by 20%. The estimate amount (R350k) does NOT feature in the under-threshold penalty calculation - SARS uses the basic amount as the floor because that is where the safe harbour was. (Fourth Schedule para 20(1)(b); SARS Guide to Provisional Tax; SARS IN 1)

R1.5m is below the new R1.8m threshold so basic amount safe harbour applies. Re-cast for new threshold: actual R2m, estimate R1.5m, basic R1.6m. 80% of actual = R1.6m. Estimate < R1.6m. Penalty 20% x (tax on R1.6m - tax on R1.5m). (Fourth Schedule para 20; SARS Budget 2026)

Second R500k. Actual R800k. Third R100k by Sep 30. Reduces interest, not penalty.

R1.2m below new R1.8m threshold. Basic amount safe harbour available. Recast example. (Fourth Schedule para 20; SARS Budget 2026)

First year. No prior. Estimated R400k. Basic amount = zero. No safe harbour. (Fourth Schedule para 19)

Add a test: estimate equals 90% of actual (timely compliant) but payment made one day late. Under amended para 20 (from 25 Feb 2026), the 20% underestimation penalty applies. (Fourth Schedule para 20 (amended))

The disclaimer template references "CPA, EA, tax attorney" - these are US/general qualifications. For a SA skill, the wording should be "registered tax practitioner (SAIT/SAICA), CA(SA), or registered legal practitioner".

## Section 1 -- Quick reference

**Section 1 -- Quick reference table**

| Field | Value |
| --- | --- |
| Country | South Africa |
| Authority | SARS (South African Revenue Service) |
| Primary legislation | Income Tax Act 58 of 1962, Fourth Schedule |
| Supporting legislation | Tax Administration Act 28 of 2011 |
| Year of assessment | 1 March to 28/29 February |
| First period due | 31 August |
| Second period due | 28/29 February |
| Third period (voluntary) | 30 September |
| Underestimation threshold (<= R1,800,000) | 90% of actual AND >= basic amount |
| Underestimation threshold (> R1,800,000) | 80% of actual (no safe harbour) |
| Penalty rate | 20% of shortfall |
| Interest rate (s89quat) | 10.25% p.a. from 2 March 2026 (on underpayment); 6.25% on overpayment refunds. Set quarterly by SARS by reference to repo rate. |
| Tax threshold (under 65, 2026) | R99,000 |
| Filing method | SARS eFiling (IRP6) |
| Currency | ZAR only |
| Contributor | Open Accountants |
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Required inputs list** — Before computing, you MUST obtain: 1. Is client a provisional taxpayer? -- receives income not subject to PAYE? 2. Year of assessment 3. Prior year taxable income -- determines "basic amount" 4. Estimated current year taxable income 5. PAYE credits? -- offset against provisional tax 6. Expected taxable income above R1,800,000? -- different threshold

### Refusal catalogue

- **R-ZA-PROV-1 -- Tax dispute / objection** — Trigger: client wants to object to SARS penalty. Message: "Objections to SARS penalties require qualified tax practitioner review. Escalate."
- **R-ZA-PROV-2 -- Company provisional tax** — Trigger: question about company (not individual) provisional tax. Message: "This skill covers individuals only. Companies have different rules."

### Prohibitions

- **Prohibitions list** — - NEVER estimate without asking about ALL income sources - NEVER tell a client with income > R1.8M that basic amount protects them -- it does not - NEVER advise that an estimate within tolerance protects against penalty if the payment is late. From 25 February 2026, the 20% underestimation penalty applies even where the estimate is correct but the payment is late. - NEVER ignore PAYE credits - NEVER confuse underestimation penalty (locked at second period) with s89quat interest (reducible via third period) - NEVER assume third period is mandatory -- it is voluntary - NEVER present provisional tax as a separate tax -- it is a prepayment - NEVER compute penalties without both estimate AND actual - NEVER use outdated SARS interest rates

## Section 3 -- Who is a provisional taxpayer

- **Legislation** — ITA Fourth Schedule, paragraph 1  _(ITA Fourth Schedule, paragraph 1)_

**Who is a provisional taxpayer table**

| Category | Provisional taxpayer? |
| --- | --- |
| Self-employed / sole proprietor | YES |
| Freelancer / contractor | YES |
| Rental income recipient | YES (if above threshold) |
| Non-executive director (NED fees, per BGR 40) | YES -- no PAYE on NED fees |
| Executive director (salary + director fees, PAYE deducted) | NO (not solely on account of director fees) |
| Salaried employee ONLY (all PAYE) | NO |
| Under 65, taxable income <= R99,000 | NO |

- **Exemption (para 18)** — A person is not a provisional taxpayer if they have no business income AND the total taxable income from interest, foreign dividends, rental, and remuneration from an unregistered employer does not exceed R30,000 for the year of assessment.  _(para 18)_

## Section 4 -- Payment periods, basic amount, and estimation

### Payment periods

**Payment periods table**

| Period | Covers | Due date | Requirement |
| --- | --- | --- | --- |
| First (IRP6) | First 6 months | 31 August | Estimate full year; pay half of estimated tax |
| Second (IRP6) | Full year | 28 February | Estimate full year; pay balance |
| Third (voluntary) | Top-up | 30 September | Avoids interest on underpayment |

### Basic amount

- **Basic amount definition** — The "basic amount" = taxable income per the latest preceding ASSESSMENT, EXCLUDING taxable capital gains, retirement lump sums, and severance benefits. Safe harbour benchmark for underestimation.
- **14-month escalation rule** — If the latest assessment is more than 14 months old at the IRP6 due date, increase the basic amount by 8% per annum (compounded) for each complete year beyond 14 months.

**Basic amount table**

| Situation | Basic amount |
| --- | --- |
| Prior year assessed | Prior year taxable income (excl. capital gains, retirement lump sums, severance) |
| No prior assessment | Zero |
| Prior year loss | Zero |
| Latest assessment > 14 months old | Increase by 8% p.a. |

### Estimation rules

- **First period penalty rule** — First period: no underestimation penalty (penalty applies only to second period).
- **Second period accuracy thresholds** — Second period: accuracy thresholds apply (see Section 5).

## Section 5 -- Underestimation penalties

- **Legislation** — ITA Fourth Schedule, paragraph 20  _(ITA Fourth Schedule, paragraph 20)_

### Thresholds

**Thresholds table**

| Taxable income | Penalty trigger |
| --- | --- |
| <= R1,800,000 | If estimate < 90% of actual AND estimate < basic amount |
| > R1,800,000 | If estimate < 80% of actual |

### Safe harbour

**Safe harbour table**

| Income | Safe harbour |
| --- | --- |
| <= R1.8M | Use basic amount as estimate -- NO penalty even if actual is higher |
| > R1.8M | No safe harbour -- must estimate within 80% |

### Penalty calculation

- **Penalty calculation <= R1.8M** — penalty = 20% x (tax on LESSER of [basic amount] and [90% of actual] - tax on estimate) The estimate amount does NOT feature directly -- SARS uses the basic amount as the floor.
- **Penalty calculation > R1.8M** — penalty = 20% x (tax on 80% of actual - tax on estimate)
- **Late payment note** — From 25 February 2026, the 20% underestimation penalty also applies where the estimate is within tolerance but payment is late.

## Section 6 -- Third period and interest

### Third provisional payment (voluntary)

**Third provisional payment table**

| Item | Detail |
| --- | --- |
| Due | 30 September |
| Purpose | Reduce s89quat interest |
| Mandatory? | NO |
| Effect | Reduces interest, NOT the underestimation penalty |

### Interest on underpayment (s89quat)

- **Interest rate on underpayment** — Rate 10.25% p.a. from 2 March 2026 (on underpayment); 6.25% on overpayment refunds. Set quarterly by SARS by reference to repo rate. Runs from period due date to payment date.

## Section 7 -- Registration, filing, and payment calculation

### Registration

- **Registration rule** — Register as provisional taxpayer on eFiling or at SARS branch.

### Payment calculation

- **Payment calculation formula** — first_period = ((estimated_annual_tax - rebates - medical_credits) - PAYE_for_6_months) / 2 second_period = (full_year_tax - rebates - medical_credits - PAYE_full_year) - first_provisional_payment third_period = actual_tax - first_provisional - second_provisional - PAYE_full_year

## Section 8 -- Edge case registry

### EC1 -- New self-employed, no prior assessment

Situation: First year, no basic amount.
Resolution: Basic amount = zero. No safe harbour. Must estimate accurately.

### EC2 -- Just above R1.8M

Situation: Actual R1,900,000.
Resolution: Above R1.8M threshold. Must estimate within 80% (R1,520,000+). No basic amount safe harbour.

### EC3 -- Loss year followed by profit

Situation: Prior year loss, current R500,000.
Resolution: Basic amount = zero. No safe harbour.

### EC4 -- Employee with side income (below R1.8M)

Situation: Salary R800,000 + freelance R400,000 = R1,200,000.
Resolution: Provisional taxpayer. Below R1.8M threshold, so basic amount safe harbour applies. 90% of actual AND >= basic amount test. PAYE credited.

### EC5 -- Underestimation below R1.8M

Situation: Basic amount R400,000, estimate R350,000, actual R700,000.
Resolution: Estimate < basic amount, so penalty applies. Had client used R400,000 (the basic amount), no penalty.

### EC6 -- Third period timing

Situation: Realizes in August that second estimate too low.
Resolution: Third payment by Sep 30 reduces interest but not penalty.

### EC7 -- Mid-year commencement

Situation: Started business October 2024.
Resolution: Still must file second provisional by February 28. Flag for reviewer on first period.

### EC8 -- Cessation mid-year

Situation: Closes business November 2024.
Resolution: Still files second provisional by February 28.

### EC9 -- Capital gain in current year

Situation: Client sells property mid-year with R500,000 capital gain. Taxable capital gain (40% inclusion = R200,000).
Resolution: The R200,000 taxable capital gain must be included in the provisional tax estimate. However, it is EXCLUDED from the basic amount calculation (basic amount excludes taxable capital gains, retirement lump sums, and severance benefits).

### EC10 -- Late payment penalty

Situation: Estimate within 90% of actual (compliant) but payment one day late.
Resolution: Under amended paragraph 20 (effective 25 February 2026), the 20% underestimation penalty applies even where the estimate is correct but payment is late.

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified tax practitioner must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified tax practitioner. Document gap.
```

## Section 10 -- Test suite

### Test 1 -- Standard first period (2026/27 rates)

Input: Estimated annual taxable income R600,000. No PAYE.
Expected output: Tax = R44,136 + 26% x (R600,000 - R245,200) = R136,384 - R17,820 rebate = R118,564. First period = ~R59,282.

### Test 2 -- Second period, basic amount safe harbour

Input: Prior year R500,000. Actual R700,000. Estimate = R500,000.
Expected output: No penalty. Safe harbour applies (<= R1.8M, estimate >= basic amount).

### Test 3 -- Second period penalty (below R1.8M)

Input: Basic amount R400,000. Estimate R350,000. Actual R800,000.
Expected output: Estimate < basic amount. Penalty = 20% x (tax on LESSER of [basic amount R400,000] and [90% of actual R720,000] - tax on R350,000) = 20% x (tax on R400,000 - tax on R350,000).

### Test 4 -- Above R1.8M, no safe harbour

Input: Actual R2,000,000. Estimate R1,500,000. Basic amount R1,200,000.
Expected output: Above R1.8M. 80% of actual = R1,600,000. Estimate R1,500,000 < R1,600,000. Penalty = 20% x (tax on R1,600,000 - tax on R1,500,000).

### Test 5 -- Third period reducing interest

Input: Second estimate R500,000. Actual R800,000. Third payment R100,000 by Sep 30.
Expected output: Third reduces interest, not penalty.

### Test 6 -- Employee with side income (below R1.8M)

Input: Salary R900,000 (PAYE) + freelance R300,000 = R1,200,000.
Expected output: Below R1.8M. Basic amount safe harbour available. 90% of actual AND >= basic amount test. PAYE credited.

### Test 7 -- New taxpayer

Input: First year. No prior. Estimated R400,000.
Expected output: Basic amount = zero. No safe harbour.

### Test 8 -- Late payment penalty

Input: Estimate R700,000. Actual R750,000 (estimate within 90%). Payment submitted one day after due date.
Expected output: Under amended para 20 (effective 25 Feb 2026), 20% penalty applies despite estimate being within tolerance, because payment was late.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CA(SA), or registered legal practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
