---
name: us-self-employed-retirement
description: Tier 2 content skill for computing the self-employed retirement contribution deduction for US sole proprietors and single-member LLCs disregarded for federal tax purposes. Covers tax year 2025 SEP-IRA, Solo 401(k), SIMPLE IRA, and traditional/Roth IRA options with SECURE 2.0 super catch-up provisions. Handles the net SE earnings calculation, the 92.35% adjustment, the employer contribution formula (20% effective rate for sole props), employee deferral limits ($23,500), catch-up and super catch-up contributions, the SEP-IRA 25% limit ($70,000 cap), SIMPLE IRA rules, traditional and Roth IRA income limits and deductibility phase-outs, and establishment/contribution deadlines. Consumes Schedule C net profit and SE tax from us-schedule-c-and-se-computation. Feeds QBI computation in us-qbi-deduction. MUST be loaded alongside us-tax-workflow-base v0.1 or later. Federal only. No state tax.
version: 0.2
---

# US Self-Employed Retirement Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It computes the deductible retirement contributions available to a sole proprietor or single-member LLC owner for tax year 2025. It does not classify transactions (that is `us-sole-prop-bookkeeping`), compute Schedule C net profit or SE tax (that is `us-schedule-c-and-se-computation`), or compute the QBI deduction (that is `us-qbi-deduction`, which consumes this skill's output).

**Where this skill fits in the pipeline:**

```
Bank statement / source data
        ↓
us-sole-prop-bookkeeping (classifies every transaction into a Schedule C line)
        ↓
us-schedule-c-and-se-computation (aggregates, computes net profit, computes SE tax)
        ↓
us-self-employed-retirement (THIS SKILL — computes retirement contribution deduction)
  + us-self-employed-health-insurance (companion — computes SE health insurance deduction)
        ↓
us-qbi-deduction (QBI deduction, adjusted for retirement and SE health insurance)
        ↓
us-quarterly-estimated-tax (safe harbor for following year)
```

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). Contribution limits are from IRS Notice 2024-80 (November 2024). SECURE 2.0 Act provisions effective for 2025 are reflected, including the age 60-63 super catch-up.

**The reviewer is the customer of this output.** The skill produces a retirement contribution worksheet and a brief that the reviewing EA or CPA can audit and sign off on.

---

## Section 1 — Scope statement

This skill covers, for tax year 2025:

- **Solo 401(k)** — employee deferrals, employer (profit-sharing) contributions, catch-up and super catch-up contributions, Roth elective deferral option, establishment and contribution deadlines
- **SEP-IRA** — employer contribution formula (25% of compensation / 20% effective rate for sole props), maximum contribution, establishment and contribution deadlines
- **SIMPLE IRA** — employee deferrals, employer matching or non-elective contributions, catch-up and super catch-up, establishment deadlines
- **Traditional IRA** — $7,000 contribution limit, $8,000 catch-up (age 50+), deductibility rules when covered by an employer plan
- **Roth IRA** — income limits and phase-outs, contribution limits, backdoor Roth mechanics (flagged, not computed)
- **Net self-employment earnings calculation** — the base for employer contributions
- **Interaction with QBI** — deductible retirement contributions reduce QBI
- **Deadline matrix** — establishment vs. contribution deadlines for each plan type

This skill does NOT cover:

- Defined benefit plans (cash balance plans, etc.) — out of scope
- ESOP or stock-based plans — out of scope
- Employer plans with common-law employees (requires plan administration beyond sole-prop scope) — flagged for reviewer
- Roth conversion strategies or backdoor Roth execution — flagged for reviewer
- Plan administration, Form 5500-EZ filing, or DOL compliance — flagged for reviewer
- Excess contribution penalties (§4973) — flagged for reviewer
- Early withdrawal penalties (§72(t)) — out of scope
- Required minimum distributions (RMDs) — out of scope (relevant for taxpayers 73+)

---

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code §§401, 402, 404, 408, 408A, 408(p), 414, 415, 219 as in force for tax year 2025
- SECURE 2.0 Act of 2022 (Division T of the Consolidated Appropriations Act, 2023; P.L. 117-328) — provisions effective 2025: super catch-up for ages 60-63 under §414(v)(2)(E), mandatory Roth catch-up for high earners (delayed to 2026 per IRS Notice 2024-02), enhanced SIMPLE IRA limits
- One Big Beautiful Bill Act (OBBBA, P.L. 119-21) — OBBBA did NOT change retirement contribution limits for 2025. The limits were set by Notice 2024-80 before OBBBA's enactment.
- IRS Notice 2024-80 — 2025 retirement plan limits (issued November 2024)
- IRS Publication 560 (2025) — Retirement Plans for Small Business
- IRS Publication 590-A (2025) — Contributions to Individual Retirement Arrangements

**Currency limitations:**
- SECURE 2.0 §603 mandatory Roth catch-up for employees earning > $145,000 was delayed by IRS Notice 2024-02 to plan years beginning after December 31, 2025. This does NOT affect sole props for 2025 (no W-2 earnings threshold for sole props).
- The super catch-up for ages 60-63 under SECURE 2.0 §109 is effective for 2025 and is reflected in this skill.

---

## Section 3 — Year-specific figures table for tax year 2025

### Solo 401(k)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Employee elective deferral limit | $23,500 | Notice 2024-80; IRC §402(g)(1) |
| Catch-up contribution (age 50-59, 64+) | $7,500 | Notice 2024-80; IRC §414(v)(2)(B)(i) |
| Super catch-up contribution (age 60-63) | $11,250 | Notice 2024-80; IRC §414(v)(2)(E); SECURE 2.0 §109 |
| Total annual additions limit (§415(c)) | $70,000 | Notice 2024-80; IRC §415(c)(1)(A) |
| Total with catch-up (age 50-59, 64+) | $77,500 | $70,000 + $7,500 |
| Total with super catch-up (age 60-63) | $81,250 | $70,000 + $11,250 |
| Employer contribution rate (on compensation) | 25% of compensation | IRC §415(c)(1)(B); IRC §404(a)(8) |
| Effective employer rate for sole props | 20% of net SE earnings | See Section 5 derivation |

### SEP-IRA

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Maximum contribution | $70,000 | Notice 2024-80; IRC §415(c)(1)(A) |
| Contribution rate (on compensation) | 25% of compensation | IRC §404(h)(1)(C) |
| Effective rate for sole props | 20% of net SE earnings | See Section 5 derivation |
| Compensation cap | $350,000 | Notice 2024-80; IRC §401(a)(17) |

### SIMPLE IRA

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Employee deferral limit | $16,500 | Notice 2024-80; IRC §408(p)(2)(E) |
| Catch-up contribution (age 50-59, 64+) | $3,500 | Notice 2024-80; IRC §414(v)(2)(B)(ii) |
| Super catch-up contribution (age 60-63) | $5,250 | Notice 2024-80; IRC §414(v)(2)(E); SECURE 2.0 §109 |
| Employer match (dollar-for-dollar) | Up to 3% of compensation | IRC §408(p)(2)(A)(iii) |
| Employer non-elective alternative | 2% of compensation | IRC §408(p)(2)(B) |
| Compensation cap for 2% non-elective | $350,000 | Notice 2024-80; IRC §401(a)(17) |

### Traditional and Roth IRA

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| IRA contribution limit | $7,000 | Notice 2024-80; IRC §219(b)(5)(A) |
| IRA catch-up (age 50+) | $1,000 | IRC §219(b)(5)(B); statutory, NOT indexed |
| Traditional IRA deductibility phase-out (single, covered by employer plan) | MAGI $79,000-$89,000 | Notice 2024-80; IRC §219(g)(3)(B)(i) |
| Traditional IRA deductibility phase-out (MFJ, covered by employer plan) | MAGI $126,000-$146,000 | Notice 2024-80; IRC §219(g)(3)(B)(i) |
| Traditional IRA deductibility phase-out (MFJ, not covered but spouse is) | MAGI $236,000-$246,000 | Notice 2024-80; IRC §219(g)(7) |
| Roth IRA contribution phase-out (single / HoH) | MAGI $150,000-$165,000 | Notice 2024-80; IRC §408A(c)(3) |
| Roth IRA contribution phase-out (MFJ) | MAGI $236,000-$246,000 | Notice 2024-80; IRC §408A(c)(3) |
| Roth IRA contribution phase-out (MFS) | MAGI $0-$10,000 | IRC §408A(c)(3)(C)(iii); statutory, not indexed |

---

## Section 4 — Primary source library

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §219** — Retirement savings (traditional IRA deduction)
- **IRC §219(b)(5)** — IRA contribution limits
- **IRC §219(g)** — Deduction phase-out for active participants in employer plans
- **IRC §401(a)(17)** — Compensation cap for qualified plans
- **IRC §401(c)(2)** — Earned income of self-employed individual defined
- **IRC §402(g)** — Elective deferral limits
- **IRC §404(a)(8)** — Sole proprietor treated as own employer for contribution limits
- **IRC §404(h)** — SEP-IRA employer deduction limits
- **IRC §408** — Individual retirement accounts (traditional IRA)
- **IRC §408(p)** — SIMPLE IRA
- **IRC §408A** — Roth IRA
- **IRC §408A(c)(3)** — Roth IRA income limits
- **IRC §414(v)** — Catch-up contributions for individuals age 50+
- **IRC §414(v)(2)(E)** — Super catch-up contributions ages 60-63 (SECURE 2.0 §109)
- **IRC §415(c)** — Annual additions limit ($70,000 for 2025)
- **IRC §1402(a)** — Net earnings from self-employment
- **IRC §1402(a)(12)** — 92.35% adjustment
- **IRC §164(f)** — Deductible half of SE tax
- **IRC §4973** — Tax on excess contributions (penalty; flagged only)

### IRS Guidance and Publications

- **IRS Notice 2024-80** — 2025 retirement plan limits
- **IRS Publication 560 (2025)** — Retirement Plans for Small Business
- **IRS Publication 590-A (2025)** — Contributions to IRAs
- **IRS Publication 590-B (2025)** — Distributions from IRAs
- **SECURE 2.0 Act of 2022** — P.L. 117-328, Division T

---

## Section 5 — Net self-employment earnings for retirement purposes

### The base computation

For retirement contribution purposes, the sole proprietor's "compensation" is **net self-employment earnings**, defined as:

```
Net SE earnings = Schedule C net profit (Line 31)
                × 92.35%  [the §1402(a)(12) adjustment]
                − Deductible half of SE tax [§164(f)]
```

Wait — that is not quite right. The computation is actually:

```
Step 1: Net SE income = Schedule C net profit × 92.35%
Step 2: SE tax = Net SE income × 15.3% (up to SS wage base) + 2.9% (Medicare on excess)
Step 3: Deductible half of SE tax = SE tax × 50%
Step 4: Net SE earnings for retirement = Schedule C net profit − Deductible half of SE tax
```

**Why the difference matters:** For retirement contribution purposes under IRC §401(c)(2), "earned income" of a self-employed individual is net earnings from self-employment reduced by:
1. The deductible half of SE tax (§164(f)), AND
2. The retirement contribution itself (creating a circular formula)

### The 25% vs. 20% rate for sole props

When an employer contributes to an employee's SEP-IRA or 401(k) profit-sharing, the limit is 25% of the employee's compensation. But for a sole proprietor, the "compensation" is reduced by the contribution itself, creating circularity. The algebraic solution:

```
Contribution = Rate × (Net SE earnings − Contribution)
Contribution = Rate × Net SE earnings / (1 + Rate)
```

At a 25% rate: Contribution = 0.25 / 1.25 × Net SE earnings = **20% of net SE earnings**

This is why the effective employer contribution rate for sole props is **20%**, not 25%.

**Net SE earnings for this formula** = Schedule C net profit − deductible half of SE tax

### Worked derivation

```
Schedule C net profit:                    $100,000
× 92.35% (§1402(a)(12)):                  $92,350
SE tax (assuming all below SS wage base):
  OASDI: $92,350 × 12.4% =                $11,451
  Medicare: $92,350 × 2.9% =               $2,678
  Total SE tax:                            $14,129
Deductible half:                            $7,065

Net SE earnings for retirement:
  $100,000 − $7,065 =                     $92,935

Maximum employer contribution (SEP or Solo 401k profit-sharing):
  20% × $92,935 =                         $18,587

Solo 401(k) with employee deferral:
  Employee deferral (under age 50):        $23,500
  + Employer (20% × $92,935):             $18,587
  Total:                                   $42,087
  (Under §415(c) $70,000 limit — OK)
```

---

## Section 6 — Solo 401(k) computation

### Overview

The Solo 401(k) (also called individual 401(k) or one-participant 401(k)) is the most powerful retirement vehicle for sole props with no common-law employees. It combines:

1. **Employee elective deferrals** — up to $23,500 (2025), dollar-for-dollar from earnings
2. **Employer profit-sharing contributions** — up to 20% of net SE earnings (after deductible half of SE tax)
3. **Catch-up contributions** — additional amount for age 50+

### Contribution limits by age

| Age in 2025 | Employee deferral | Catch-up | Employer (max) | §415(c) cap | Maximum possible |
|---|---|---|---|---|---|
| Under 50 | $23,500 | $0 | 20% of net SE earnings, up to $46,500 | $70,000 | $70,000 |
| 50-59 | $23,500 | $7,500 | 20% of net SE earnings, up to $46,500 | $70,000 + $7,500 | $77,500 |
| 60-63 | $23,500 | $11,250 | 20% of net SE earnings, up to $46,500 | $70,000 + $11,250 | $81,250 |
| 64+ | $23,500 | $7,500 | 20% of net SE earnings, up to $46,500 | $70,000 + $7,500 | $77,500 |

**Note on the §415(c) cap:** The $70,000 limit applies to the sum of employee deferrals + employer contributions (NOT including catch-up). Catch-up contributions are above the §415(c) limit. So the true maximum is $70,000 + catch-up.

**Note on the employer side cap:** The employer contribution cannot exceed 20% of net SE earnings. The employee deferral + employer contribution (excluding catch-up) cannot exceed $70,000. These limits interact — whichever binds first controls.

### Roth elective deferral option

Solo 401(k) plans can be designed to accept Roth (after-tax) elective deferrals. Roth deferrals:
- Count against the $23,500 elective deferral limit (same as pre-tax)
- Do NOT reduce current-year taxable income (no deduction)
- Do NOT reduce QBI (since there is no deduction)
- Grow tax-free and are distributed tax-free in retirement (if qualified)

The skill computes Roth deferrals at $0 deduction but notes the total contributed for informational purposes. The employer profit-sharing portion is always pre-tax (traditional).

### Establishment and contribution deadlines

| Action | Deadline |
|---|---|
| Establish a new Solo 401(k) plan | December 31, 2025 (for 2025 contributions) |
| Make employee elective deferrals (2025) | December 31, 2025 (must be made by end of tax year) |
| Make employer profit-sharing contributions (2025) | Tax filing deadline including extensions (April 15, 2026, or October 15, 2026 with extension) |

**Critical:** A Solo 401(k) must be established (plan adoption agreement executed) by December 31 of the tax year. If the plan was not established by December 31, 2025, the sole prop CANNOT make 2025 Solo 401(k) contributions — even if they file an extension. This is different from a SEP-IRA.

### Form 5500-EZ filing requirement

If the Solo 401(k) plan assets exceed $250,000 at the end of the plan year, the sole prop must file Form 5500-EZ with the IRS. This is an annual filing, due by the last day of the 7th month after the plan year ends (July 31 for calendar-year plans). Failure to file triggers a $250/day penalty (up to $150,000). The skill flags this requirement when estimated plan assets exceed $200,000.

---

## Section 7 — SEP-IRA computation

### Overview

A SEP-IRA (Simplified Employee Pension) allows employer-only contributions. There is no employee deferral component. The maximum is 25% of compensation (20% effective for sole props), capped at $70,000 for 2025.

### Contribution formula for sole props

```
Maximum SEP contribution = lesser of:
  (a) 20% × (Schedule C net profit − deductible half of SE tax)
  (b) $70,000
```

### Advantages over Solo 401(k)

- Simpler to establish and administer (no plan document beyond IRS Form 5305-SEP)
- Can be established and funded up to the tax filing deadline including extensions (no December 31 establishment requirement)
- No Form 5500-EZ filing requirement

### Disadvantages vs. Solo 401(k)

- No employee deferral component — total contribution limited to 20% of net SE earnings
- For sole props with net SE earnings under ~$117,500, the SEP-IRA allows LESS total contribution than a Solo 401(k) with employee deferrals
- No catch-up contributions (the catch-up rules apply only to elective deferrals, not employer contributions)
- No Roth option (all SEP contributions are pre-tax)

### Establishment and contribution deadlines

| Action | Deadline |
|---|---|
| Establish SEP-IRA | Tax filing deadline including extensions (can establish and fund on same day) |
| Make 2025 contributions | Tax filing deadline including extensions (April 15, 2026, or October 15, 2026) |

**Key advantage:** A sole prop who did not plan ahead can establish a SEP-IRA and make 2025 contributions as late as October 15, 2026 (if they file an extension). This is NOT possible with a Solo 401(k).

---

## Section 8 — SIMPLE IRA computation

### Overview

A SIMPLE IRA (Savings Incentive Match Plan for Employees) is less common for solo practitioners but available. It allows both employee deferrals and employer contributions.

### Contribution formula for sole props

```
Employee deferral: up to $16,500 (2025)
Catch-up (age 50-59, 64+): additional $3,500
Super catch-up (age 60-63): additional $5,250

Employer match: dollar-for-dollar up to 3% of net SE earnings
  OR
Employer non-elective: 2% of net SE earnings (up to $350,000 comp cap = max $7,000)
```

### When SIMPLE IRA beats Solo 401(k)

Almost never for a sole prop. The SIMPLE IRA has lower deferral limits ($16,500 vs. $23,500) and lower employer contribution potential. It exists primarily for small businesses with employees who want a simpler alternative to a 401(k).

**The SIMPLE IRA has a critical restriction:** If a sole prop maintains a SIMPLE IRA, they generally cannot also maintain a Solo 401(k) or SEP-IRA for the same year. The SIMPLE IRA must be the only employer plan.

### Establishment deadline

A SIMPLE IRA must be established by October 1 of the tax year (e.g., October 1, 2025 for 2025 contributions). For a new business, it must be established as soon as administratively feasible but no later than October 1 if the business started before October 1.

---

## Section 9 — Traditional IRA

### Contribution limits (2025)

- Under age 50: $7,000
- Age 50+: $8,000 ($7,000 + $1,000 catch-up)

### Deductibility rules for self-employed individuals

A sole prop who participates in a Solo 401(k), SEP-IRA, or SIMPLE IRA is considered an "active participant" in an employer plan. This triggers the deductibility phase-out for traditional IRA contributions:

**Single / Head of Household (active participant):**
- MAGI ≤ $79,000: fully deductible
- $79,000 < MAGI < $89,000: partially deductible (pro-rata)
- MAGI ≥ $89,000: not deductible (but can still contribute — nondeductible contribution tracked on Form 8606)

**Married Filing Jointly (active participant):**
- MAGI ≤ $126,000: fully deductible
- $126,000 < MAGI < $146,000: partially deductible
- MAGI ≥ $146,000: not deductible

**MFJ (NOT active participant, but spouse IS):**
- MAGI ≤ $236,000: fully deductible
- $236,000 < MAGI < $246,000: partially deductible
- MAGI ≥ $246,000: not deductible

**If the sole prop does NOT have any employer plan (no SEP, no Solo 401(k), no SIMPLE):** The traditional IRA contribution is fully deductible regardless of income. However, this scenario is unlikely — the sole prop is leaving significant tax savings on the table by not having a plan.

### Contribution deadline

Traditional IRA contributions for 2025 are due by April 15, 2026 (the tax filing deadline WITHOUT extensions). Extensions do not extend the IRA contribution deadline.

### Interaction with other plans

A traditional IRA contribution is IN ADDITION to Solo 401(k) or SEP-IRA contributions. They use different limits and different IRC sections. But the deductibility phase-out kicks in when the taxpayer is an active participant in another plan.

---

## Section 10 — Roth IRA

### Contribution limits (2025)

Same as traditional IRA: $7,000 ($8,000 if age 50+). The combined traditional + Roth IRA contribution cannot exceed $7,000 ($8,000 if 50+).

### Income limits (2025)

**Single / Head of Household:**
- MAGI < $150,000: full contribution allowed
- $150,000 ≤ MAGI < $165,000: reduced contribution (pro-rata phase-out)
- MAGI ≥ $165,000: $0 direct Roth IRA contribution

**Married Filing Jointly:**
- MAGI < $236,000: full contribution allowed
- $236,000 ≤ MAGI < $246,000: reduced contribution
- MAGI ≥ $246,000: $0 direct Roth IRA contribution

**Married Filing Separately:**
- MAGI < $10,000: reduced contribution
- MAGI ≥ $10,000: $0

### Backdoor Roth IRA

High-income sole props who exceed the Roth IRA income limits can use the "backdoor" strategy:
1. Make a nondeductible traditional IRA contribution ($7,000/$8,000)
2. Convert to Roth IRA (Roth conversion — taxable on any pre-tax amounts)

**The skill flags this strategy when MAGI exceeds Roth limits but does NOT compute the conversion mechanics.** The pro-rata rule under §408(d)(2) (aggregation of all traditional IRA balances) makes backdoor Roth conversions complex when the taxpayer has existing pre-tax IRA balances. Refer to reviewer.

### Roth IRA does NOT reduce QBI

Roth IRA contributions are after-tax. They are not deductible and do not appear on Schedule 1. They do NOT reduce QBI.

### Contribution deadline

Same as traditional IRA: April 15, 2026 (no extension). This applies to both regular and catch-up contributions.

---

## Section 11 — Plan selection decision framework

For the typical sole prop with no employees, the decision tree is:

```
Is net SE earnings > $0?
├── NO → No SE retirement contributions possible (may still contribute to IRA from other income)
├── YES → Continue
    │
    Was a Solo 401(k) established by Dec 31, 2025?
    ├── YES → Solo 401(k) is almost always the best choice
    │         Employee deferral: up to $23,500
    │         + Employer: 20% of net SE earnings
    │         + Catch-up if applicable
    │         + Optional Roth IRA on top ($7,000/$8,000 if MAGI permits)
    │
    ├── NO → Can still establish a SEP-IRA by filing deadline
    │         SEP-IRA: 20% of net SE earnings (max $70,000)
    │         + Optional Roth IRA on top ($7,000/$8,000 if MAGI permits)
    │
    └── Income too low for meaningful employer contribution?
              Consider traditional IRA ($7,000/$8,000) or Roth IRA
              May be the only practical option if net SE earnings < $15,000
```

### The crossover point: when SEP-IRA equals Solo 401(k)

```
Solo 401(k) total = $23,500 (deferral) + 20% × net SE earnings (employer)
SEP-IRA total = 20% × net SE earnings

Solo 401(k) > SEP-IRA when net SE earnings < $117,500
  (because the $23,500 deferral advantage is only overcome when
   20% × net SE earnings exceeds the deferral limit, and the
   combined Solo 401(k) is capped at $70,000 anyway)
```

At net SE earnings of ~$232,500: both Solo 401(k) employer + deferral and SEP-IRA hit the $70,000 cap ($232,500 × 20% = $46,500 employer + $23,500 deferral = $70,000). Above that, the Solo 401(k) catch-up provides the only additional room.

---

## Section 12 — Conservative defaults table

| Ambiguity | Conservative default |
|---|---|
| Plan type not specified | Assume Solo 401(k) if established by Dec 31; otherwise SEP-IRA |
| Age not provided | Assume under 50 (lowest contribution limits); ask for age |
| Solo 401(k) establishment date unclear | Assume NOT established by Dec 31 (cannot use Solo 401(k)); default to SEP-IRA |
| Roth vs. traditional deferral preference not stated | Assume pre-tax (traditional) for maximum current-year deduction and QBI reduction |
| MAGI not computed for Roth eligibility | Compute MAGI from available data; if MAGI unclear, assume above Roth limits (no Roth recommendation) |
| Whether taxpayer has existing IRA balances (for backdoor Roth) | Assume yes (pro-rata rule applies); flag for reviewer |
| Plan contribution amount not specified | Compute maximum allowable; present maximum and let reviewer/taxpayer decide |
| SIMPLE IRA vs. other plans | Do NOT default to SIMPLE; it is inferior for most sole props without employees |

---

## Section 13 — Topical refusal catalogue

**R-RET-DB — Defined benefit plan inquiry.**
Trigger: Taxpayer asks about a defined benefit plan, cash balance plan, or pension.
Output: "Defined benefit plans require actuarial computation, Form 5500 filing, and ongoing plan administration that is beyond the scope of this skill. These plans can allow contributions substantially exceeding the §415(c) limit and are worth exploring for high-income sole props ($300K+ net SE earnings). Please consult an actuary or retirement plan specialist."

**R-RET-EMPLOYEES — Sole prop has common-law employees.**
Trigger: The taxpayer has employees (pays W-2 wages), which triggers nondiscrimination, top-heavy, and coverage rules for 401(k) and SEP plans.
Output: "When a sole prop has common-law employees, retirement plan contributions for the owner must satisfy nondiscrimination and coverage rules under §401(a)(4) and §410(b). This skill covers one-participant (solo) plans only. Please consult a retirement plan administrator or CPA."

**R-RET-EXCESS — Excess contributions.**
Trigger: Taxpayer may have contributed more than the limit.
Output: "Excess contributions to retirement plans are subject to a 6% excise tax under §4973 (IRAs) or must be corrected under the plan's terms (401(k)/SEP). This skill does not compute excess contribution penalties. Please consult a CPA or tax attorney."

**R-RET-RMD — Required minimum distributions.**
Trigger: Taxpayer is age 73+ and has retirement accounts.
Output: "Required minimum distributions under §401(a)(9) must begin by April 1 following the year the taxpayer turns 73 (under SECURE 2.0 schedule). RMD computation is out of scope. Please consult a CPA or financial advisor."

**R-RET-ROTHCONV — Roth conversion strategy.**
Trigger: Taxpayer asks about converting traditional IRA or 401(k) to Roth.
Output: "Roth conversions are taxable events with complex interactions (pro-rata rule, state tax, impact on ACA subsidies, Medicare IRMAA). This skill flags the backdoor Roth strategy but does not compute conversion mechanics. Please consult a CPA or financial advisor."

---

## Section 14 — Reviewer attention thresholds

| Threshold | Trigger | Rationale |
|---|---|---|
| Total retirement contributions > $50,000 | Always flag | Verify §415(c) limit compliance |
| Solo 401(k) established after Oct 1 | Always flag | Verify December 31 establishment was completed |
| Sole prop has employees | Always flag | Nondiscrimination and coverage rules apply |
| Net SE earnings < $23,500 | Always flag | Employee deferral limited to net SE earnings; verify computation |
| Taxpayer age 60-63 | Always flag | Super catch-up eligible — verify age documentation |
| Multiple retirement plans in same year | Always flag | Aggregation rules and limits coordination required |
| Backdoor Roth flagged | Always flag | Pro-rata rule; verify no existing pre-tax IRA balances |
| MAGI near Roth or IRA deductibility phase-out | Always flag | Small income changes could affect eligibility |
| Solo 401(k) assets > $200,000 | Always flag | Form 5500-EZ filing requirement approaching or triggered |

---

## Section 15 — Worked examples

### Example 1 — Solo 401(k), under 50, moderate income

**Taxpayer:** Maria Hernandez, single, age 34, freelance UX designer, net SE earnings = $62,644 (from Schedule C), deductible half of SE tax = $4,427. Solo 401(k) established December 2024.

```
Net SE earnings for retirement = $62,644 − $4,427 = $58,217

Employee deferral: $23,500 (under §402(g) limit)
Employer contribution: 20% × $58,217 = $11,643
Total: $35,143

§415(c) check: $23,500 + $11,643 = $35,143 ≤ $70,000 ✓

Deduction on Schedule 1: $35,143
```

### Example 2 — SEP-IRA, high income

**Taxpayer:** James Chen, single, age 42, freelance software developer, Schedule C net profit = $250,000, deductible half of SE tax = $16,583. No Solo 401(k) established (missed Dec 31 deadline).

```
Net SE earnings for retirement = $250,000 − $16,583 = $233,417

SEP-IRA: 20% × $233,417 = $46,683
§415(c) check: $46,683 ≤ $70,000 ✓

Deduction on Schedule 1: $46,683

Had he established a Solo 401(k):
  Employee deferral: $23,500
  Employer: $46,683 (same as SEP)
  Total: $70,000 (hits §415(c) cap, so capped at $70,000)
  Additional savings: $70,000 − $46,683 = $23,317 more in retirement
```

### Example 3 — Solo 401(k) with super catch-up

**Taxpayer:** Lisa Park, MFJ, age 61, freelance accountant, Schedule C net profit = $180,000, deductible half of SE tax = $12,717. Solo 401(k) established 2020.

```
Net SE earnings = $180,000 − $12,717 = $167,283

Employee deferral: $23,500
Super catch-up (age 60-63): $11,250
Employer: 20% × $167,283 = $33,457
Total: $68,207

§415(c) check: $23,500 + $33,457 = $56,957 ≤ $70,000 ✓
  (catch-up is excluded from §415(c))
Total with catch-up: $56,957 + $11,250 = $68,207

Deduction on Schedule 1: $68,207
```

### Example 4 — Low income, IRA only

**Taxpayer:** Alex Rivera, single, age 28, freelance graphic designer, Schedule C net profit = $18,000, deductible half of SE tax = $1,272. No employer plan established.

```
Net SE earnings = $18,000 − $1,272 = $16,728

Could establish SEP-IRA by filing deadline:
  20% × $16,728 = $3,346

Could establish Solo 401(k) by Dec 31:
  Employee deferral: $16,728 (limited to net SE earnings)
  Employer: $3,346
  Total: limited by net SE earnings interaction
  In practice: can defer up to $16,728 (less than $23,500 limit)
  + employer: 20% × $16,728 = $3,346
  Total: up to ~$16,728 (deferral cannot exceed earned income)

Traditional IRA (no employer plan, fully deductible): $7,000
Roth IRA: $7,000 (MAGI well below $150,000)
```

---

## Section 16 — Edge cases

1. **Net SE earnings are negative (Schedule C loss).** No SE retirement contributions allowed. May still contribute to a traditional or Roth IRA using earned income from other sources (W-2 wages).

2. **Employee deferral exceeds net SE earnings.** The elective deferral cannot exceed net SE earnings from the business. If net SE earnings are $15,000, the maximum deferral is $15,000, not $23,500.

3. **Multiple self-employment activities.** If the taxpayer has multiple Schedule Cs, net SE earnings are aggregated. A loss from one business reduces net SE earnings available for retirement contributions from another.

4. **Part-year self-employment.** No pro-ration of limits. If the taxpayer was self-employed for 3 months and earned $20,000, the full $23,500 deferral limit applies (subject to net SE earnings limitation).

5. **Taxpayer also has W-2 income with employer 401(k).** The $23,500 elective deferral limit is SHARED across all 401(k) plans (including employer 401(k) and Solo 401(k)). If the taxpayer deferred $20,000 at their employer, only $3,500 remains for Solo 401(k) deferral. Employer contributions are NOT shared — each plan has its own §415(c) limit.

6. **Age 60-63 super catch-up is NOT available for SEP-IRA.** The super catch-up applies to elective deferrals only (401(k), SIMPLE). SEP-IRA has no deferral component and therefore no catch-up.

7. **SIMPLE IRA 2-year rule.** If the taxpayer previously had a SIMPLE IRA and is within the 2-year period from the first SIMPLE contribution, rollovers to a traditional IRA or 401(k) are restricted. The 25% early withdrawal penalty (instead of the normal 10%) applies during this period.

8. **Spousal IRA.** A self-employed taxpayer filing MFJ can fund a spousal IRA ($7,000/$8,000) for a non-working or low-earning spouse, even though the spouse has no earned income of their own, as long as the combined earned income exceeds the total IRA contributions.

9. **Contribution deadline with extension.** Solo 401(k) employer contributions and SEP-IRA contributions can be made up to October 15, 2026 if the taxpayer files an extension. The extension must actually be filed — the contribution deadline is the actual filing deadline, not an automatic grace period.

10. **Roth Solo 401(k) deferrals do not reduce QBI.** Pre-tax (traditional) Solo 401(k) deferrals reduce QBI via the Schedule 1 deduction. Roth deferrals do not reduce QBI because they are not deductible. This affects the downstream QBI computation.

---

## Section 17 — Test suite

### Test 1 — Basic Solo 401(k), under 50
**Input:** Schedule C net profit $100,000; deductible half SE tax $7,065; age 40; Solo 401(k) established.
**Expected:** Net SE earnings for retirement = $92,935. Employee deferral = $23,500. Employer = 20% × $92,935 = $18,587. Total = $42,087. §415(c) check: $42,087 ≤ $70,000. **Deduction = $42,087.**

### Test 2 — SEP-IRA, high income hitting cap
**Input:** Schedule C net profit $400,000; deductible half SE tax $23,886; age 55; no Solo 401(k).
**Expected:** Net SE earnings = $376,114. SEP = 20% × $376,114 = $75,223, CAPPED at $70,000. **SEP deduction = $70,000.**

### Test 3 — Solo 401(k) with super catch-up
**Input:** Schedule C net profit $200,000; deductible half SE tax $14,130; age 62; Solo 401(k) established.
**Expected:** Net SE earnings = $185,870. Employee deferral = $23,500. Employer = 20% × $185,870 = $37,174. Subtotal = $60,674 ≤ $70,000 §415(c). Super catch-up = $11,250. **Total deduction = $71,924.**

### Test 4 — Low income, deferral limited by earnings
**Input:** Schedule C net profit $20,000; deductible half SE tax $1,413; age 30; Solo 401(k) established.
**Expected:** Net SE earnings = $18,587. Employee deferral = $18,587 (limited by net SE earnings, not $23,500). Employer = 20% × $18,587 = $3,717. Total = $22,304. But total cannot exceed net SE earnings in a meaningful way — verify: $23,500 deferral limit > $18,587 net SE earnings, so deferral capped at $18,587. **Total deduction = $22,304.**

### Test 5 — Shared 401(k) deferral with employer plan
**Input:** Schedule C net profit $80,000; deductible half SE tax $5,652; age 45; Solo 401(k) established; also has W-2 job where deferred $15,000 in employer 401(k).
**Expected:** Remaining Solo 401(k) deferral = $23,500 − $15,000 = $8,500. Net SE earnings = $74,348. Employer = 20% × $74,348 = $14,870. **Solo 401(k) total = $8,500 + $14,870 = $23,370.** (Employer contributions are separate from the shared deferral limit.)

### Test 6 — Traditional IRA deductibility phase-out
**Input:** Schedule C net profit $120,000; SEP-IRA contribution $20,000; single; MAGI = $100,000 (after SE tax deduction); age 35.
**Expected:** Active participant in SEP-IRA. Single phase-out: $79,000-$89,000. MAGI $100,000 > $89,000. **Traditional IRA contribution is NOT deductible** (but can still contribute nondeductibly or to Roth if MAGI < $150,000).

---

## Section 18 — PROHIBITIONS

1. **NEVER use the 25% rate directly for a sole prop's employer contribution.** The effective rate is 20% (25% / 1.25) because the contribution reduces the base. Using 25% overstates the maximum contribution.

2. **NEVER allow a Solo 401(k) for 2025 if the plan was not established by December 31, 2025.** Default to SEP-IRA if the establishment date is unknown or after December 31.

3. **NEVER ignore the §415(c) $70,000 cap.** Employee deferrals + employer contributions (excluding catch-up) cannot exceed $70,000. Catch-up is on top.

4. **NEVER apply the super catch-up to ages outside 60-63.** Ages 50-59 and 64+ get the regular $7,500 catch-up. Only ages 60-63 get the $11,250 super catch-up.

5. **NEVER recommend a SIMPLE IRA over a Solo 401(k) for a sole prop without employees.** SIMPLE IRA has lower limits and more restrictions. It is virtually always inferior for the target demographic.

6. **NEVER forget that the $23,500 deferral limit is SHARED across all 401(k) plans.** A taxpayer with both an employer 401(k) and a Solo 401(k) shares the limit.

7. **NEVER allow employee deferrals to exceed net SE earnings.** The deferral is capped at the lesser of $23,500 or net SE earnings.

8. **NEVER compute retirement contributions without first computing the deductible half of SE tax.** The deductible half of SE tax reduces net SE earnings, which is the base for employer contributions.

9. **NEVER extend the IRA contribution deadline beyond April 15.** Filing extensions do NOT extend the IRA contribution deadline. Only Solo 401(k) employer contributions and SEP-IRA contributions get the extension benefit.

10. **NEVER treat Roth contributions (IRA or Solo 401(k) Roth deferral) as reducing QBI.** Only deductible (pre-tax) contributions reduce QBI.

---

## Section 19 — Cross-skill references

| Upstream skill | Data consumed |
|---|---|
| `us-schedule-c-and-se-computation` | Schedule C net profit (Line 31), deductible half of SE tax |

| Downstream skill | Data provided |
|---|---|
| `us-qbi-deduction` | Deductible retirement contribution amount (reduces QBI) |
| `us-quarterly-estimated-tax` | Retirement deduction amount (reduces estimated tax liability) |
| `us-federal-return-assembly` | Retirement deduction for Schedule 1 Line 16 |
| `us-ca-return-assembly` | Retirement deduction for federal return portion |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
