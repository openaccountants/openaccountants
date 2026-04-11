---
name: us-s-corp-election-decision
description: Tier 2 content skill for evaluating whether a US sole proprietor or single-member LLC should elect S-corporation status under IRC §1362 via Form 2553. Covers the SE tax savings analysis (salary subject to FICA, distributions not), the reasonable salary requirement under IRC §3121 and IRS audit scrutiny, the break-even analysis where SE tax savings exceed incremental costs, the QBI deduction interaction under §199A (W-2 wages increase QBI limitation room), state-specific disadvantages (California $800 franchise tax + 1.5% S-corp tax, New York City UBT elimination, etc.), the Form 2553 election deadline (March 15 or within 75 days of formation), late election relief under Rev. Proc. 2013-30, payroll processing and Form 1120-S filing costs, and the decision framework for when NOT to elect. Tax year 2025. MUST be loaded alongside us-tax-workflow-base v0.1+. Federal only; state issues flagged but not computed.
version: 0.2
---

# US S-Corp Election Decision Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides a structured decision framework for evaluating whether a sole proprietor or single-member LLC should elect S-corporation status for federal tax purposes. It does not file Form 2553, prepare Form 1120-S, or run payroll — those are execution tasks that follow after the decision is made.

**This is a decision skill, not a computation skill.** Unlike the bookkeeping and computation skills in the pipeline, this skill produces a decision brief for the reviewer, not a tax return position. The decision brief presents the SE tax savings estimate, the incremental costs, the QBI interaction, state-specific issues, and a recommendation with confidence level.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). It reflects the One Big Beautiful Bill Act (Public Law 119-21, signed July 4, 2025), including the permanent QBI deduction and the rate increase to 23% for 2026+.

**The reviewer is the customer of this output.** The skill produces a decision analysis, not a filing. The reviewing Enrolled Agent, CPA, or attorney makes the final recommendation to the client.

---

## Section 1 — Scope statement

This skill covers the S-corp election decision for tax year 2025 for taxpayers who are:

- US sole proprietors filing Schedule C, OR
- Single-member LLCs treated as disregarded entities for federal income tax purposes

Who are considering:

- Electing S-corporation status under IRC §1362 via Form 2553
- Evaluating whether an existing S-corp election should be maintained or revoked
- Comparing the tax cost of sole proprietorship vs S-corp structure

For the following kinds of work:

- Computing the SE tax savings from S-corp election at various salary levels
- Determining reasonable compensation under IRC §3121 and case law
- Running the break-even analysis (SE tax savings vs incremental costs)
- Evaluating the QBI deduction interaction (W-2 wages affect the QBI wage limitation)
- Identifying state-specific advantages and disadvantages
- Checking the Form 2553 election deadline and late election relief availability
- Producing a decision brief with recommendation and confidence level

This skill does NOT cover:

- Preparation of Form 2553 — execution task
- Preparation of Form 1120-S — execution task for a future tax year
- Payroll setup and processing — execution task
- Multi-member LLC to S-corp conversion — different considerations
- C-corp to S-corp conversion — built-in gains tax under §1374, different analysis
- Partnership to S-corp — different analysis
- S-corp vs C-corp comparison — this skill focuses on sole prop/SMLLC vs S-corp only

---

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (election effective for TY2025 if Form 2553 filed by March 17, 2025 — March 15 falls on Saturday — or within 75 days of formation if formed after January 1, 2025).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code as in force for tax year 2025
- One Big Beautiful Bill Act (OBBBA), Public Law 119-21, signed July 4, 2025
- IRC §199A as made permanent by OBBBA (20% for 2025, rising to 23% for 2026+)
- Rev. Proc. 2013-30 (late S-corp election relief)
- Rev. Proc. 2024-40 (2025 inflation adjustments)

---

## Section 3 — Year-specific figures table for tax year 2025

### Self-employment tax figures

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Social Security wage base | $176,100 | SSA annual announcement |
| OASDI rate (employee + employer combined) | 12.4% | IRC §1401(a) / §3101(a) + §3111(a) |
| Medicare rate (employee + employer combined) | 2.9% | IRC §1401(b) / §3101(b) + §3111(b) |
| Additional Medicare Tax (employee only, no employer match) | 0.9% above threshold | IRC §3101(b)(2) |
| Additional Medicare Tax threshold (single) | $200,000 | IRC §3101(b)(2)(C) |
| Additional Medicare Tax threshold (MFJ) | $250,000 | IRC §3101(b)(2)(A) |
| SE tax rate (OASDI + Medicare) | 15.3% (below SS wage base) | IRC §1401 |
| SE tax rate (Medicare only, above SS wage base) | 2.9% | IRC §1401(b) |
| Net SE earnings adjustment factor | 92.35% | IRC §1402(a)(12) |

### S-corp payroll tax figures (employer side)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| FUTA tax rate | 6.0% (0.6% after state credit) | IRC §3301; most states qualify for 5.4% credit |
| FUTA wage base | $7,000 | IRC §3306(b)(1) |
| Effective FUTA cost per employee | $42 (0.6% x $7,000) | Derived |
| State unemployment insurance (SUI) | Varies by state; typically 1-5% on first $7K-$56K | State law |

### QBI deduction figures

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| QBI deduction rate (2025) | 20% | IRC §199A(a); OBBBA made permanent |
| QBI deduction rate (2026 onward) | 23% | OBBBA P.L. 119-21; IRC §199A as amended |
| QBI threshold (single) | $197,300 | Rev. Proc. 2024-40 |
| QBI threshold (MFJ) | $394,600 | Rev. Proc. 2024-40 |
| QBI phase-in range top (single) | $247,300 | $197,300 + $50,000 |
| QBI phase-in range top (MFJ) | $494,600 | $394,600 + $100,000 |
| W-2 wages limitation (above phase-in) | Greater of: 50% of W-2 wages, or 25% of W-2 wages + 2.5% of UBIA | IRC §199A(b)(2) |

### Form 2553 deadlines

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Election deadline for existing entity (calendar year) | March 17, 2025 (March 15 is Saturday) | IRC §1362(b)(1)(B); §7503 |
| Election deadline for newly formed entity | Within 75 days of formation | IRC §1362(b)(1)(C); Rev. Proc. 2013-30 |
| Late election relief | Available if requirements of Rev. Proc. 2013-30 are met | Rev. Proc. 2013-30 |

---

## Section 4 — Primary source library

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §1361** — S corporation defined; eligibility requirements
- **IRC §1361(b)(1)** — Requirements: domestic corporation, ≤ 100 shareholders, one class of stock, eligible shareholders only
- **IRC §1362** — Election; revocation; termination
- **IRC §1362(b)** — When election takes effect
- **IRC §1362(d)** — Termination of election
- **IRC §1363** — Effect of election on corporation (pass-through)
- **IRC §1366** — Pass-through of items to shareholders
- **IRC §1368** — Distributions (AAA, E&P, basis)
- **IRC §1374** — Built-in gains tax (not applicable to new elections from sole prop)
- **IRC §1375** — Excess net passive income tax
- **IRC §199A** — Qualified Business Income deduction
- **IRC §199A(b)(2)** — W-2 wages and UBIA limitations
- **IRC §3101, §3111** — FICA taxes (employee and employer shares)
- **IRC §3121** — Definitions (wages for FICA purposes — basis for reasonable salary)
- **IRC §3301, §3306** — FUTA tax
- **IRC §1401, §1402** — Self-employment tax (applies to sole props, NOT to S-corp shareholder-employees on wages)
- **IRC §162** — Trade or business expenses (S-corp deducts salary as business expense)

### Treasury Regulations

- **Treas. Reg. §1.1361-1** — S corporation defined
- **Treas. Reg. §1.1362-6** — Procedural requirements for Form 2553
- **Treas. Reg. §1.199A-1 through §1.199A-6** — QBI deduction regulations
- **Treas. Reg. §31.3121(a)-1** — Definition of wages for FICA

### Revenue Procedures and Rulings

- **Rev. Proc. 2013-30** — Late S-corp election relief (simplified method)
- **Rev. Proc. 2024-40** — 2025 inflation adjustments

### Key Court Cases and IRS Guidance

- **Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)** — $24K salary on $488K net income was unreasonably low; reasonable compensation required
- **Radtke v. United States, 712 F. Supp. 143 (E.D. Wis. 1989)** — Zero salary to S-corp shareholder-employee who performed services was unreasonable; all distributions recharacterized as wages
- **Joseph M. Grey Public Accountant, P.C. v. Commissioner, T.C. Memo 2002-34** — IRS successfully recharacterized distributions as wages when salary was unreasonably low
- **David E. Watson, P.C. v. United States, 757 F. Supp. 2d 877 (S.D. Iowa 2010)** — Detailed reasonable compensation analysis
- **IRS Fact Sheet FS-2008-25** — Reasonable compensation guidance for S-corp shareholders

### IRS Forms

- **Form 2553** — Election by a Small Business Corporation
- **Form 1120-S** — U.S. Income Tax Return for an S Corporation
- **Form 1120-S, Schedule K-1** — Shareholder's Share of Income, Deductions, Credits, etc.
- **Form 940** — Employer's Annual Federal Unemployment (FUTA) Tax Return

---

## Section 5 — The SE tax savings mechanism

### How a sole proprietor pays SE tax

As a sole proprietor, the taxpayer pays self-employment tax on **all** net SE earnings:

```
Net SE earnings = Schedule C net profit x 92.35%

SE tax = (Net SE earnings, up to SS wage base) x 15.3%
       + (Net SE earnings above SS wage base) x 2.9%
       + (Net SE earnings above $200K/$250K) x 0.9% (Additional Medicare Tax)

Deductible half of SE tax = 50% of the 15.3%/2.9% portion (NOT the 0.9%)
```

### How an S-corp shareholder-employee pays employment tax

As an S-corp shareholder-employee, the taxpayer pays FICA only on **salary (W-2 wages)**:

```
FICA on salary:
  Employee share: 7.65% (6.2% OASDI + 1.45% Medicare) up to SS wage base
                  1.45% Medicare on salary above SS wage base
                  Additional 0.9% Medicare on salary above $200K/$250K
  Employer share: 7.65% (6.2% OASDI + 1.45% Medicare) up to SS wage base
                  1.45% Medicare on salary above SS wage base

Distributions (K-1 income above salary): NO FICA, NO SE tax
```

### The savings calculation

```
Sole prop SE tax on $X of net income:
  = $X x 92.35% x 15.3% (up to SS wage base)
  = approximately 14.13% of net income (simplified)

S-corp FICA on salary of $Y (where Y < X):
  Employee + employer = $Y x 15.3% (up to SS wage base)

Savings = SE tax on $X - FICA on $Y - incremental S-corp costs

The savings come from the "distribution gap" ($X - $Y) that escapes FICA/SE tax.
```

### Why the savings are not unlimited: reasonable salary

The IRS requires that S-corp shareholder-employees who perform services receive **reasonable compensation** before taking distributions. IRC §3121; Watson v. United States; Radtke v. United States.

If the salary is set too low, the IRS can recharacterize distributions as wages, assess back FICA taxes (both shares), plus penalties and interest. This is a well-known audit target.

---

## Section 6 — Reasonable salary determination

### The IRS approach

There is no bright-line rule for reasonable compensation. The IRS and courts look at multiple factors:

1. **Training and experience** — what would a comparable employee earn?
2. **Duties and responsibilities** — the shareholder's role in generating revenue
3. **Time devoted** — hours per week/year
4. **Comparable wages** — what do similar positions pay in the same geographic area? (BLS data, salary surveys, industry benchmarks)
5. **Dividend history** — pattern of distributions vs salary
6. **Compensation agreements** — documented compensation arrangements
7. **Amounts paid to non-shareholder employees** — if they exist
8. **Timing and manner of paying dividends** — distributions that replace what would normally be salary

### Practical guidelines (not law, but widely used)

| Net SE income range | Reasonable salary range (rough guide) | Notes |
|---|---|---|
| < $50,000 | 80-100% of net income | Little room for meaningful split |
| $50,000 - $100,000 | 50-70% of net income | Moderate savings begin |
| $100,000 - $200,000 | 40-60% of net income | Sweet spot for savings |
| $200,000 - $400,000 | 35-50% of net income | Diminishing OASDI savings above SS wage base |
| > $400,000 | Comparable market salary (may be 20-40% of net) | Large distribution gap; ensure salary withstands scrutiny |

**Key principle:** The salary should reflect what the taxpayer would earn as an employee performing the same services for an unrelated employer. It should NOT be set to minimize FICA — it should reflect market value, with distributions representing the return on the business as an enterprise (similar to corporate dividends).

### Documentation requirements

The taxpayer should document the reasonable salary determination with:
- Job description listing duties performed
- Comparable salary data (BLS Occupational Employment Statistics, Glassdoor, industry surveys)
- Time log or estimate of hours worked
- Written board resolution or compensation memo (even for a single-shareholder S-corp)
- Consistent payment through payroll with proper withholding

---

## Section 7 — Break-even analysis

### Incremental costs of S-corp election

| Cost category | Typical annual cost | Notes |
|---|---|---|
| Form 1120-S preparation (tax return) | $1,000 - $3,000 | CPA or tax preparer; complexity varies |
| Payroll processing | $500 - $2,000/year | Provider fees (Gusto, ADP, manual); includes W-2, 940, 941 |
| State franchise/filing fees | $0 - $800+ | Varies by state; California is $800 minimum |
| State unemployment insurance (SUI) | $100 - $500+ | Varies by state and experience rating |
| FUTA tax | $42/year | 0.6% x $7,000 per employee (after state credit) |
| Workers' compensation (if required) | Varies | Some states require even for single-employee S-corps |
| Registered agent (if LLC) | $100 - $300 | If not already paying |
| Additional accounting/bookkeeping complexity | $500 - $1,500 | Payroll journal entries, K-1 reconciliation |
| **Total incremental cost** | **$2,000 - $6,000+** | |

### Break-even formula

```
SE tax savings = (Net SE income - Reasonable salary) x effective SE tax rate on the gap
Incremental costs = sum of costs above

Break-even: SE tax savings > Incremental costs

Simplified: Break-even typically occurs when net SE income > $50,000 - $60,000
(assuming reasonable salary is ~60% of net income and incremental costs are ~$3,000-4,000)
```

### Worked break-even example

**Scenario:** Freelance software developer, single filer, net SE income = $120,000.

**As sole proprietor:**
```
Net SE earnings: $120,000 x 92.35% = $110,820
OASDI: $110,820 x 12.4% = $13,742 (all below $176,100 SS wage base)
Medicare: $110,820 x 2.9% = $3,214
Total SE tax: $16,956
Deductible half: $8,478
```

**As S-corp with $65,000 salary:**
```
Employee FICA: $65,000 x 7.65% = $4,973
Employer FICA: $65,000 x 7.65% = $4,973
Total FICA: $9,945
FUTA: $42
Distribution: $120,000 - $65,000 = $55,000 (no FICA)
```

**Savings calculation:**
```
SE tax avoided: $16,956 - $9,945 = $7,011
Less FUTA: -$42
Less incremental costs (est.): -$3,500 (payroll, 1120-S, etc.)
Net annual savings: approximately $3,469
```

**Conclusion:** At $120K net SE income with a $65K salary, the S-corp saves roughly $3,400-3,500/year after costs. The savings increase as income rises above the salary level.

---

## Section 8 — QBI deduction interaction

### The basic QBI framework (2025)

Under IRC §199A, sole proprietors and S-corp shareholders can deduct 20% of qualified business income (rising to 23% for 2026+ under OBBBA). For taxpayers below the income threshold ($197,300 single / $394,600 MFJ for 2025), the deduction is simply 20% of QBI with no limitations.

### When QBI interacts with the S-corp decision

For taxpayers **above the QBI threshold** (in the phase-in range or above), the QBI deduction is limited to the greater of:

- **50% of W-2 wages** paid by the business, OR
- **25% of W-2 wages + 2.5% of unadjusted basis immediately after acquisition (UBIA)** of qualified property

**As a sole proprietor:** There are no W-2 wages (the sole proprietor's own earnings are SE income, not wages). The W-2 wages component is zero unless the sole proprietor has employees. The QBI limitation therefore depends entirely on the UBIA of qualified property (25% of W-2 wages is zero, so only 2.5% of UBIA applies in the second prong, and the first prong is $0).

**As an S-corp:** The shareholder-employee's salary IS W-2 wages for QBI purposes. This increases the W-2 wages component, potentially increasing the QBI deduction limitation.

### When this matters

| Taxpayer situation | QBI impact of S-corp | Notes |
|---|---|---|
| Income below QBI threshold | No impact — QBI is 20% of QBI regardless | S-corp decision driven purely by SE tax savings |
| Income in phase-in range | S-corp W-2 wages may increase QBI deduction | Run both scenarios; net tax impact may favor S-corp |
| Income above phase-in range | S-corp W-2 wages are critical for QBI deduction | Without W-2 wages, QBI deduction may be zero for service businesses (SSTBs) |
| Specified Service Trade or Business (SSTB) above threshold | QBI deduction phases out entirely | S-corp W-2 wages do not help once fully phased out |

### The SSTB factor

For specified service trades or businesses (legal, health, consulting, financial services, performing arts, athletics, etc. under §199A(d)(2)), the QBI deduction phases out entirely above the threshold. Once fully phased out, the W-2 wages from S-corp salary provide no QBI benefit. The S-corp decision for SSTBs above the threshold is driven purely by SE tax savings.

**Note:** Software development is generally NOT an SSTB (consulting may be, depending on facts). The reviewer must classify the business.

---

## Section 9 — Form 2553 election mechanics

### Filing deadline

| Scenario | Deadline | Primary source |
|---|---|---|
| Existing entity, calendar year, electing for TY2025 | March 17, 2025 (March 15 is Saturday) | IRC §1362(b)(1)(B); §7503 |
| Entity formed on or after Jan 1, 2025 | Within 75 days of formation | IRC §1362(b)(1)(C) |
| Fiscal year entity | By the 15th day of the 3rd month of the fiscal year | IRC §1362(b)(1)(B) |

### Late election relief under Rev. Proc. 2013-30

If the Form 2553 deadline was missed, relief is available under Rev. Proc. 2013-30 if ALL of the following are met:

1. The entity is an eligible entity (meets all §1361(b) requirements)
2. The entity intended to be classified as an S-corp as of the intended effective date
3. The entity failed to qualify solely because the election was not timely filed
4. The entity has reasonable cause for the late filing
5. No more than **3 years and 75 days** have passed since the intended effective date
6. No inconsistent returns were filed (i.e., the entity and all shareholders filed as if the S election were in effect)

**How to file:** Attach a statement to Form 2553 explaining the reasonable cause, and write "FILED PURSUANT TO REV. PROC. 2013-30" at the top. File with the IRS service center.

### Other late election methods

- **PLR (Private Letter Ruling):** If Rev. Proc. 2013-30 does not apply (e.g., more than 3 years and 75 days have passed, or inconsistent returns were filed), the entity can request a PLR from the IRS. Cost: $3,000 - $35,000+ user fee plus professional fees. Generally not cost-effective for sole props.
- **Rev. Proc. 2022-19:** Provides additional simplified relief for certain late elections when filed within 3 years and 75 days.

### Eligibility requirements for S-corp status

The entity must meet ALL of the following (IRC §1361(b)(1)):

1. Domestic corporation (or LLC electing corporate treatment)
2. No more than 100 shareholders
3. Only eligible shareholders (individuals, certain trusts, estates — no partnerships, corporations, or nonresident aliens)
4. Only one class of stock (differences in voting rights are OK; differences in distribution/liquidation rights are not)
5. Not an ineligible corporation (certain financial institutions, insurance companies, DISCs)

For a single-member LLC, the LLC must first elect to be treated as a corporation (Form 8832) or simultaneously elect S-corp status (Form 2553 with the LLC's EIN triggers the entity classification election automatically under Treas. Reg. §301.7701-3(c)(1)(v)(C)).

---

## Section 10 — State-specific considerations

### States with significant S-corp disadvantages

| State | Issue | Impact |
|---|---|---|
| **California** | $800 annual franchise tax (LLC or S-corp) + 1.5% S-corp tax on net income | S-corp pays 1.5% income tax at entity level (franchise tax); sole prop does not. At $100K net income, this is $1,500 additional state tax. Break-even analysis must account for this. |
| **New York City** | S-corps are subject to NYC General Corporation Tax (GCT) or UBT | Sole props pay NYC UBT; S-corps may pay GCT. The rates and structures differ. Detailed NYC analysis needed. |
| **New Hampshire** | Business Profits Tax (BPT) at 7.5% applies to S-corp income | NH has no personal income tax but taxes business income at entity level. S-corps pay BPT. |
| **Tennessee** | No state income tax on earned income | S-corp provides no state tax savings; sole prop is equally advantaged. |
| **Texas** | Franchise (margin) tax applies to S-corps with revenue > $2.47M | Small S-corps below the no-tax-due threshold are unaffected. Above threshold, 0.375% to 0.75% on margin. |

### States with S-corp advantages

| State | Issue | Impact |
|---|---|---|
| **New Jersey** | S-corp income taxed at reduced rates at entity level; shareholder may benefit from pass-through structure | Complex; run both scenarios |
| **Most states** | S-corp income passes through to shareholder's personal return | No entity-level tax in most states (CA, NH, NYC are exceptions) |

### General guidance

The state analysis is fact-intensive and varies by state. The skill flags state issues and provides the California example in detail (because it is the most common disadvantage case), but the reviewer must analyze the taxpayer's specific state situation.

---

## Section 11 — When NOT to elect S-corp

### Decision matrix: situations where S-corp is typically NOT advantageous

| Situation | Why S-corp is typically NOT advantageous |
|---|---|
| **Net SE income < $50,000** | SE tax savings are too small to justify incremental costs ($2K-6K/year). The break-even is not met. |
| **Taxpayer values simplicity** | S-corp adds payroll, 1120-S filing, K-1, and ongoing compliance. Sole prop is simpler. |
| **California resident with income < $150K** | California's 1.5% S-corp tax + $800 franchise tax may offset or exceed SE tax savings. |
| **Taxpayer has significant losses** | S-corp losses are limited by basis, at-risk, and passive activity rules. Sole prop losses flow directly to Schedule C. S-corp basis rules are more restrictive (shareholder loans must be direct loans, not from third parties). |
| **Taxpayer plans to sell the business** | S-corp sale mechanics (asset sale vs stock sale) are more complex and may have less favorable tax treatment than sole prop goodwill sale. |
| **Taxpayer has multiple businesses** | Each S-corp requires its own 1120-S, payroll, etc. Multiple Schedule C sole proprietorships are simpler. |
| **Taxpayer is near retirement** | S-corp salary (lower than SE income) reduces Social Security benefit computation. For taxpayers near 62, this may not matter, but for younger taxpayers it reduces future benefits. |
| **Income is highly variable** | In low-income years, the S-corp's fixed costs (payroll, 1120-S) remain even when there is no SE tax savings. |
| **Taxpayer has no employees and does all work personally** | The "reasonable salary = all income" argument is strongest here. If the IRS determines that 100% of income is reasonable compensation, there are zero SE tax savings but full S-corp costs. |
| **SSTB above QBI threshold** | No QBI benefit from W-2 wages (QBI deduction fully phased out). Decision rests on SE tax savings alone. |

---

## Section 12 — Conservative defaults table

| Situation | Conservative default | Rationale |
|---|---|---|
| Reasonable salary percentage unknown | Use 60% of net SE income as starting point | Provides moderate savings while leaving room for IRS scrutiny |
| Comparable salary data unavailable | Use BLS median for the taxpayer's SOC code + 10% | Conservative buffer against IRS challenge |
| State S-corp tax unknown | Flag for reviewer; do not assume zero | Many states have entity-level taxes on S-corps |
| QBI impact unclear | Run both scenarios (sole prop and S-corp); present both | Reviewer decides which is better |
| Late election feasibility uncertain | Assume Rev. Proc. 2013-30 relief is available if within 3 years 75 days and returns were filed consistently | Conservative but optimistic; flag for reviewer confirmation |
| Incremental cost estimate unavailable | Use $3,500 as default incremental cost | Covers payroll ($1,000), 1120-S prep ($1,500), miscellaneous ($1,000) |
| Social Security benefit impact | Flag but do not compute | SSA benefit computation is complex and fact-specific |

---

## Section 13 — PROHIBITIONS

The skill MUST NOT:

1. **Recommend a specific salary amount as "the" reasonable salary** — the skill presents a range and factors; the reviewer and client determine the actual salary with professional judgment
2. **Prepare or file Form 2553** — the skill produces a decision brief, not a filing
3. **Advise setting salary to zero or near-zero** — this is the single most audited S-corp position; cases like Radtke and Watson demonstrate the consequences
4. **Guarantee SE tax savings** — savings depend on facts (income level, reasonable salary, state taxes, costs) that vary by taxpayer
5. **Ignore state-level S-corp taxes** — state taxes can eliminate or reverse federal savings; always flag
6. **Treat the QBI interaction as always favoring S-corp** — for many taxpayers (below the threshold, SSTBs above the threshold), QBI is neutral or irrelevant to the S-corp decision
7. **Advise revocation of an existing S-corp election without full analysis** — revocation has its own consequences (including the 5-year prohibition on re-election under §1362(g))
8. **Compute Social Security benefit reductions** — SSA benefit calculations are out of scope; flag the issue for the reviewer
9. **Apply the analysis to multi-member LLCs or partnerships** — different rules apply
10. **Recommend S-corp election solely to avoid Additional Medicare Tax** — the 0.9% Additional Medicare Tax applies to wages above $200K/$250K regardless of entity structure; S-corp salary above the threshold still pays it

---

## Section 14 — Edge cases

**Edge Case 1 — Net SE income fluctuates widely year to year.**
A freelancer earned $150K in TY2024 but expects only $40K in TY2025 due to a career change. The S-corp election made sense at $150K but may not at $40K. The incremental costs ($3K-5K) may exceed SE tax savings at $40K. The skill should present both years' analysis and note that S-corp elections are ongoing — the taxpayer must pay the incremental costs even in low-income years unless they revoke the election.

**Edge Case 2 — Taxpayer's only income source is this business.**
When the taxpayer's entire livelihood comes from the business and they perform all services personally, the IRS's argument that "reasonable salary = most of the income" is strongest. The Watson case involved a CPA whose firm earned $488K; the court found $93K was reasonable (about 19%), but the taxpayer had other partners. A solo operator has a weaker position. Conservative approach: set salary at 60-70% of net income for solo operators.

**Edge Case 3 — S-corp election mid-year.**
An S-corp election effective mid-year (e.g., LLC formed July 1, 2025, with Form 2553 filed within 75 days) creates a short S-corp year. The taxpayer files Schedule C for Jan 1 - Jun 30 and Form 1120-S for Jul 1 - Dec 31. Both SE tax and FICA apply to their respective periods. The break-even analysis should pro-rate costs and savings.

**Edge Case 4 — Husband and wife qualified joint venture converting to S-corp.**
A married couple filing jointly who operate a qualified joint venture (§761(f)) must restructure to a single-member entity before electing S-corp status. The QJV files two Schedule Cs; the S-corp files one 1120-S. Both spouses must be employees if both perform services. This doubles the payroll cost and FUTA. Flag for reviewer.

**Edge Case 5 — Taxpayer has substantial depreciable property (high UBIA).**
When the business has significant qualified property (equipment, vehicles, etc.), the UBIA component of the QBI limitation may provide adequate QBI deduction room without W-2 wages. In this case, the S-corp's W-2 wages provide less QBI benefit, and the decision tilts toward sole proprietorship. Run both QBI scenarios.

**Edge Case 6 — California resident with high income.**
At $300K net SE income in California: SE tax savings from S-corp might be $10K-15K, but California imposes a 1.5% S-corp tax ($4,500) plus the $800 franchise tax. Net California cost: $5,300. Federal savings must exceed this state cost plus other incremental costs ($3K-5K). Total break-even: federal savings must exceed ~$8K-10K. This typically works at $300K but is marginal at $150K.

**Edge Case 7 — Taxpayer also has W-2 income from another employer.**
If the taxpayer's W-2 wages from another employer exceed the Social Security wage base ($176,100 for 2025), then ALL of the sole prop's SE income is subject to only the 2.9% Medicare rate (not the 12.4% OASDI rate). The S-corp savings are dramatically reduced because the OASDI savings disappear. The S-corp only saves the 2.9% Medicare rate on the distribution gap, which at a $3K-5K cost may not break even.

**Edge Case 8 — Taxpayer plans to contribute to a Solo 401(k).**
The Solo 401(k) employer contribution for an S-corp shareholder-employee is based on W-2 salary (25% of salary, up to the §415 limit of $70,000 for 2025). Lower salary = lower employer contribution limit. For a sole proprietor, the contribution is based on net SE earnings (20% of net SE earnings after the SE tax deduction). The skill must compare retirement contribution room under both structures and flag if the S-corp salary would reduce maximum retirement contributions.

**Edge Case 9 — Entity already has an S-corp election in place but income has dropped.**
The taxpayer elected S-corp when income was $200K but now earns $50K. The incremental costs ($3K-5K) may exceed the SE tax savings. The skill should analyze whether revoking the election makes sense, noting the 5-year prohibition on re-election under §1362(g). This creates an asymmetric decision: revoking is easy but re-electing requires waiting 5 years.

**Edge Case 10 — Taxpayer is a nonresident alien's spouse filing MFJ.**
An S-corp cannot have a nonresident alien as a shareholder (§1361(b)(1)(C)). If the taxpayer's spouse is a nonresident alien, the taxpayer can still elect S-corp status (the spouse is not a shareholder), but the MFJ filing status and its interaction with Additional Medicare Tax thresholds ($250K MFJ) should be analyzed. Flag for reviewer.

---

## Section 15 — Test suite

### Test 1 — Clear S-corp advantage

**Input:** Freelance developer, single filer, net SE income = $150,000. No employees. No state income tax (TX resident). No W-2 income from other sources.
**Expected output:**
- Sole prop SE tax: $150,000 x 92.35% x 15.3% = approximately $21,194
- S-corp with $80,000 salary: FICA = $80,000 x 15.3% = $12,240 + FUTA $42 = $12,282
- SE tax savings: $21,194 - $12,282 = $8,912
- Incremental costs (estimated): $3,500
- Net savings: approximately $5,412
- Recommendation: S-corp election likely advantageous. Flag reasonable salary determination for reviewer.

### Test 2 — Below break-even

**Input:** Freelance writer, single filer, net SE income = $35,000. No employees. No state income tax.
**Expected output:**
- Sole prop SE tax: $35,000 x 92.35% x 15.3% = approximately $4,945
- S-corp with $25,000 salary: FICA = $25,000 x 15.3% = $3,825 + FUTA $42 = $3,867
- SE tax savings: $4,945 - $3,867 = $1,078
- Incremental costs (estimated): $3,500
- Net savings: -$2,422 (NET LOSS)
- Recommendation: S-corp election NOT advantageous at this income level. The incremental costs exceed the SE tax savings.

### Test 3 — California resident with 1.5% S-corp tax

**Input:** Freelance consultant, single filer, CA resident, net SE income = $120,000. No employees.
**Expected output:**
- Sole prop SE tax: $120,000 x 92.35% x 15.3% = approximately $16,956
- S-corp with $65,000 salary: FICA = $65,000 x 15.3% = $9,945 + FUTA $42 = $9,987
- SE tax savings: $16,956 - $9,987 = $6,969
- California S-corp tax: $120,000 x 1.5% = $1,800 + $800 franchise tax = $2,600
- Incremental costs (federal): $3,500
- Total incremental costs: $3,500 + $2,600 = $6,100
- Net savings: $6,969 - $6,100 = $869
- Recommendation: Marginal. Savings are under $1,000. The complexity and audit risk may not justify the election. Flag for reviewer — might be worth it if income is expected to grow.

### Test 4 — High income with W-2 from another employer

**Input:** Freelance consultant, MFJ, net SE income = $80,000. Spouse has W-2 income of $200,000 (exceeds SS wage base).
**Expected output:**
- The taxpayer's W-2 spouse already exceeds the SS wage base. The taxpayer's SE income is also subject to employer OASDI (because SE tax is separate from the spouse's FICA).
- Wait — SE tax applies to the individual, not the household. The taxpayer's own SE earnings below the SS wage base are still subject to full 15.3% SE tax.
- Sole prop SE tax: $80,000 x 92.35% x 15.3% = approximately $11,300
- S-corp with $50,000 salary: FICA = $50,000 x 15.3% = $7,650 + $42 = $7,692
- SE tax savings: $11,300 - $7,692 = $3,608
- Incremental costs: $3,500
- Net savings: approximately $108
- Recommendation: Barely break-even. S-corp election provides negligible savings. Not recommended given the added complexity.
- **However:** If the taxpayer's OWN wages + SE earnings exceed the SS wage base, the savings picture changes. Recalculate with combined income analysis.

### Test 5 — Late election with Rev. Proc. 2013-30 relief

**Input:** Freelance designer, single filer, formed LLC on January 15, 2025. Intended to elect S-corp effective January 15, 2025. Missed the 75-day deadline (April 1, 2025). Now filing Form 2553 on July 15, 2025. Net SE income expected: $100,000. Filed TY2025 returns as S-corp.
**Expected output:**
- 75-day deadline: April 1, 2025 (75 days from Jan 15)
- Filing date: July 15, 2025 (105 days late)
- Rev. Proc. 2013-30 requirements:
  - Eligible entity: YES (assumed)
  - Intended S-corp effective date: January 15, 2025
  - Within 3 years and 75 days: YES (well within)
  - Filed consistently as S-corp: YES (stated)
  - Reasonable cause: must be documented on Form 2553
- Relief likely available. File Form 2553 with "FILED PURSUANT TO REV. PROC. 2013-30" notation.
- Recommendation: Proceed with late filing. Flag for reviewer to verify all Rev. Proc. 2013-30 requirements.

### Test 6 — QBI interaction for high-income non-SSTB

**Input:** Freelance app developer (NOT an SSTB), single filer, net SE income = $280,000. No employees, no depreciable property (UBIA = $0). Considering S-corp with $140,000 salary.
**Expected output:**
- Taxable income above QBI threshold ($197,300 single): YES, in phase-in range
- As sole proprietor: W-2 wages = $0, UBIA = $0. QBI limitation = greater of (50% x $0) or (25% x $0 + 2.5% x $0) = $0. QBI deduction is limited to $0 once fully phased in (at $247,300 for single). Since income is $280K (above $247,300), full limitation applies: QBI deduction = $0 as sole prop.
- As S-corp: W-2 wages = $140,000. QBI limitation = greater of (50% x $140,000 = $70,000) or (25% x $140,000 + 2.5% x $0 = $35,000) = $70,000. QBI = $280,000 - $140,000 = $140,000 (K-1 income). QBI deduction = 20% x $140,000 = $28,000, limited to $70,000 → deduction = $28,000.
- QBI tax savings: $28,000 x marginal tax rate (est. 32%) = approximately $8,960
- SE tax savings from S-corp: additional savings on top
- Recommendation: S-corp is strongly advantageous due to BOTH SE tax savings and QBI deduction recovery. Flag for reviewer.

---

## Section 16 — Cross-skill references

**Inputs from upstream skills:**

- **From `us-schedule-c-and-se-computation`:** Schedule C net profit (the starting point for SE income and the income base for break-even analysis)
- **From `us-form-1040-self-employed-positions`:** QBI deduction computation under both scenarios (sole prop vs S-corp); total tax liability

**Outputs:**

- This skill produces a decision brief, not a tax return position. If the decision is to elect S-corp, the taxpayer begins using the S-corp pipeline (Form 1120-S, payroll, K-1) for the current or future tax year, which is outside the scope of the sole-prop skill stack.

---

## Section 17 — Reference material

### Validation status

This file is v0.2 of `us-s-corp-election-decision`, drafted in April 2026. SE tax rates, QBI thresholds, and SS wage base verified against IRC, SSA announcements, and Rev. Proc. 2024-40. Case law citations verified. California S-corp tax rate verified against Cal. Rev. & Tax. Code §23802(b).

### Known gaps

1. The reasonable salary analysis is inherently fact-intensive. The skill provides a framework and rough guidelines but cannot substitute for a formal compensation study. For taxpayers above $200K net SE income, a formal study may be warranted.
2. State-specific analysis is provided only for California in detail. Other states with entity-level S-corp taxes (NH, NYC, etc.) are flagged but not computed.
3. The skill does not compute Social Security benefit reductions from lower W-2 wages. This is a long-term planning consideration that requires SSA benefit projection tools.
4. The QBI interaction analysis assumes the taxpayer has only one business. Multi-business QBI aggregation under §199A(b)(3) is handled by the QBI companion skill.
5. The skill does not address the built-in gains tax (§1374), which applies to C-corp to S-corp conversions. This is out of scope (sole prop to S-corp does not trigger §1374).
6. Workers' compensation insurance requirements for single-shareholder S-corps vary by state and are not tracked.

### Change log

- **v0.1 (April 2026):** Stub.
- **v0.2 (April 2026):** Full skill. Tax year 2025. Built on `us-tax-workflow-base` v0.1.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
