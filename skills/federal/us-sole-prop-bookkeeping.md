---
name: us-sole-prop-bookkeeping
description: Tier 2 content skill for classifying business transactions into US federal Schedule C (Form 1040) line items for sole proprietors and single-member LLCs disregarded for federal tax. Covers tax year 2025 under the One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) with post-OBBBA depreciation rules, permanent QBI framework, and new tip/overtime/auto loan interest deductions. Handles Schedule C Parts I-V, the §162 ordinary and necessary standard, §263 capitalization, §280A home office, §280F vehicle and listed property, §274 substantiation and meals, §168(k) bonus depreciation cutoff at January 19 2025, §179 expensing, §471(c) small business inventory exception, §183 hobby loss, and §6001 / §274(d) recordkeeping. Defers Schedule C net profit, Schedule SE, QBI, retirement contributions, and quarterly estimated tax to companion content skills. MUST be loaded alongside us-tax-workflow-base v0.1 or later. Federal only. No state tax.
version: 0.2
---

# US Sole Prop Bookkeeping Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides the actual federal income tax classification rules for transactions on a sole proprietor's books for tax year 2025. It does not provide workflow architecture — that comes from the base. It does not provide Schedule SE computation, QBI computation, retirement contribution computation, or quarterly estimated tax computation — those are separate content skills.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). It reflects the One Big Beautiful Bill Act (Public Law 119-21, signed July 4, 2025) and post-OBBBA guidance available as of the currency date. For tax years before 2025, the skill must not be used without explicit verification that the figures apply. For tax years after 2025, several figures will need updating (notably the QBI rate which rises to 23% in 2026, indexed §179 amounts, the standard mileage rate, retirement contribution limits, and the SS wage base).

**Scope.** This skill classifies transactions into the appropriate Schedule C (Form 1040) line item, identifies items that should be excluded (personal expenses, owner draws, transfers, capital items), flags items requiring documentation under §274(d), and produces a transaction-by-transaction working paper that the human reviewer can audit. It does not compute net profit, self-employment tax, or any 1040 position. Those are downstream and live in other skills.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers federal Schedule C (Form 1040) classification for tax year 2025 for taxpayers who are:

- US sole proprietors filing Schedule C, OR
- Single-member LLCs treated as disregarded entities for federal income tax purposes (the LLC's activity flows directly onto the owner's Schedule C)

For the following kinds of work:

- Classifying business income into Part I (gross receipts, returns, gross profit)
- Classifying business expenses into Part II (lines 8 through 27b)
- Identifying inventory and COGS items for Part III (lines 33 through 42)
- Capturing vehicle information for Part IV (lines 43 through 47b)
- Itemizing other expenses for Part V (line 48 detail flowing to Line 27b)
- Identifying capital items requiring depreciation treatment on Form 4562
- Identifying home office expenses requiring Form 8829 treatment
- Flagging the §274(d) substantiation status of travel, meals, gifts, and listed property
- Excluding non-business and non-deductible items with documented reasons

This skill does NOT cover:

- Computation of net profit (Schedule C line 31) — handled by `us-schedule-c-and-se-computation`
- Schedule SE — handled by `us-schedule-c-and-se-computation`
- The QBI deduction — handled by `us-form-1040-self-employed-positions`
- Self-employed retirement contribution computation — handled by `us-form-1040-self-employed-positions`
- Self-employed health insurance deduction — handled by `us-form-1040-self-employed-positions`
- Quarterly estimated tax — handled by `us-quarterly-estimated-tax`
- Any state tax — out of scope for the entire US tax stack
- The new OBBBA tip / overtime / auto loan interest / senior deductions — these flow through Schedule 1-A on the personal side, not Schedule C, and are handled by `us-form-1040-self-employed-positions`

---

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code as in force for tax year 2025
- One Big Beautiful Bill Act (OBBBA), Public Law 119-21, signed July 4, 2025, with provisions effective for 2025
- Tax Cuts and Jobs Act of 2017 provisions still in force in 2025 (those not superseded by OBBBA)
- Treasury Regulations as in force for tax year 2025
- IRS Publications updated for tax year 2025 (Pub 334, 463, 535 [discontinued — content moved to other Pubs], 587, 946)
- IRS Form Instructions for tax year 2025 (Schedule C, Form 4562, Form 8829, Form 1040)
- Rev. Proc. 2024-40 (2025 inflation adjustments, issued October 2024) where not superseded by OBBBA
- Rev. Proc. 2025-16 (2025 luxury auto depreciation caps and lease inclusion amounts)
- Notice 2025-5 (2025 standard mileage rates)

**Currency limitations:**
- Treasury and IRS guidance implementing OBBBA provisions was being issued throughout 2025 and into 2026. Where guidance is interpretive or where the OBBBA text and pre-OBBBA regulations are not yet harmonized, the skill flags the position for reviewer attention rather than asserting confidence.
- Some OBBBA provisions (notably the new tip, overtime, and auto loan interest deductions) operate through reporting mechanisms the IRS was still building out in late 2025. Form names and line references for those items may shift; the skill defers to current Form 1040 instructions at filing time.

---

## Section 3 — Year-specific figures table for tax year 2025

All dollar thresholds, rates, percentages, and indexed figures the skill relies on, in one place. Every figure has its primary source citation. Reviewers and future updaters can find every year-sensitive number here.

### Depreciation and capitalization

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| §179 expensing limit | $2,500,000 | OBBBA P.L. 119-21 §70306; IRC §179(b)(1) as amended |
| §179 phase-out threshold | $4,000,000 | OBBBA P.L. 119-21 §70306; IRC §179(b)(2) as amended |
| §179 heavy SUV cap | $31,300 | IRC §179(b)(5); inflation-adjusted |
| §168(k) bonus depreciation rate, property acquired ≤ Jan 19, 2025 | 40% | IRC §168(k) pre-OBBBA phase-down schedule |
| §168(k) bonus depreciation rate, property acquired > Jan 19, 2025 | 100% | OBBBA P.L. 119-21; IRC §168(k) as amended |
| §168(k) transitional election (in lieu of 100%) | 40% available | OBBBA P.L. 119-21 transitional rule |
| De minimis safe harbor, taxpayer with AFS | $5,000 per item | Treas. Reg. §1.263(a)-1(f)(1)(i)(D) |
| De minimis safe harbor, taxpayer without AFS | $2,500 per item | Treas. Reg. §1.263(a)-1(f)(1)(ii)(D) |

### Vehicle expenses

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Standard mileage rate (business) | 70 cents per mile | Notice 2025-5 |
| Standard mileage rate (medical/moving for armed forces) | 21 cents per mile | Notice 2025-5 |
| Standard mileage rate (charitable) | 14 cents per mile | IRC §170(i); statutory, not indexed |
| §280F first-year passenger auto depreciation cap, with bonus | $20,200 | Rev. Proc. 2025-16 Table 1 |
| §280F first-year passenger auto depreciation cap, without bonus | $12,200 | Rev. Proc. 2025-16 Table 2 |
| §280F second-year cap | $19,600 | Rev. Proc. 2025-16 |
| §280F third-year cap | $11,800 | Rev. Proc. 2025-16 |
| §280F succeeding years cap | $7,060 | Rev. Proc. 2025-16 |
| Heavy vehicle GVW threshold (escapes §280F caps) | > 6,000 lbs | IRC §280F(d)(5)(A) |

### Home office

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Simplified method rate | $5.00 per square foot | Rev. Proc. 2013-13; Pub 587 (2025) |
| Simplified method square footage cap | 300 sq ft | Rev. Proc. 2013-13; Pub 587 (2025) |
| Simplified method maximum deduction | $1,500 | $5 × 300, derived |

**Note:** OBBBA did NOT change the simplified home office rate. It remains at $5/sq ft, max $1,500, as set by Rev. Proc. 2013-13 and confirmed in IRS Publication 587 (2025). Any source claiming a 2025 increase to $6/sq ft or $1,800 max is wrong.

### Meals

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Business meals deductibility (general rule) | 50% | IRC §274(n)(1) |
| Entertainment deductibility | 0% | IRC §274(a)(1) post-TCJA |
| De minimis fringe (snacks, coffee) | 100% deductible | IRC §132(e); Treas. Reg. §1.132-6 |
| Employer-provided meals on premises for employer's convenience | varies, see §274(n)(2) and §119 | IRC §119; IRC §274(n)(2) |

**Note:** There is NO 100% deduction for restaurant meals in 2025. The temporary 100% deduction under CAA 2021 §210 expired after December 31, 2022. No subsequent legislation reinstated it. OBBBA did not contain a 100% restaurant meal provision. Any source claiming a 100% restaurant meal deduction for 2025 is wrong.

### Inventory and accounting method

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| §471(c) small business gross receipts threshold | $31,000,000 | IRC §471(c); IRC §448(c)(1); inflation-adjusted |
| §448(c) cash method gross receipts threshold | $31,000,000 | IRC §448(c)(1); inflation-adjusted |
| §163(j) small business interest exception threshold | $31,000,000 | IRC §163(j)(3); IRC §448(c) reference |

### 1099-NEC issuance

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| 1099-NEC filing threshold | $600 | IRC §6041A(a); §6041(a) |
| Backup withholding rate | 24% | IRC §3406(a)(1) |
| 1099-NEC due date to recipient and IRS | January 31, 2026 | IRC §6071(c) |

### Schedule SE figures (referenced for context, computed in companion skill)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Social Security wage base | $176,100 | SSA annual announcement; IRC §1402(b) |
| Net SE earnings adjustment factor | 92.35% | IRC §1402(a)(12) |
| OASDI rate | 12.4% | IRC §1401(a) |
| Medicare rate | 2.9% | IRC §1401(b) |
| Additional Medicare Tax rate | 0.9% | IRC §3101(b)(2) / §1401(b)(2) |
| Additional Medicare Tax threshold (single) | $200,000 | IRC §3101(b)(2)(C); statutory, not indexed |
| Additional Medicare Tax threshold (MFJ) | $250,000 | IRC §3101(b)(2)(A); statutory, not indexed |
| Minimum SE earnings to trigger SE tax | $400 | IRC §1402(b)(2) |

### QBI figures (referenced for context, computed in companion skill)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| QBI deduction rate (2025) | 20% | IRC §199A(a); OBBBA made permanent |
| QBI deduction rate (2026 onward) | 23% | OBBBA P.L. 119-21; IRC §199A as amended |
| QBI threshold (single, head of household, qualifying surviving spouse) | $197,300 | Rev. Proc. 2024-40; IRC §199A(e)(2) |
| QBI threshold (married filing jointly) | $394,600 | Rev. Proc. 2024-40 |
| QBI threshold (married filing separately) | $197,300 | Rev. Proc. 2024-40 |
| QBI phase-in range top (single) | $247,300 | $197,300 + $50,000; IRC §199A(e)(2)(B)(i) |
| QBI phase-in range top (MFJ) | $494,600 | $394,600 + $100,000; IRC §199A(e)(2)(B)(ii) |

### Retirement contribution figures (referenced for context, computed in companion skill)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| SEP-IRA / Solo 401(k) total employer cap | $70,000 | Notice 2024-80; IRC §415(c)(1)(A) |
| Solo 401(k) employee deferral | $23,500 | Notice 2024-80; IRC §402(g)(1) |
| Solo 401(k) catch-up (age 50-59, 64+) | $7,500 | Notice 2024-80; IRC §414(v) |
| Solo 401(k) super catch-up (age 60-63) | $11,250 | Notice 2024-80; IRC §414(v)(2)(E) under SECURE 2.0 |
| SIMPLE IRA employee deferral | $16,500 | Notice 2024-80; IRC §408(p)(2)(E) |
| Traditional/Roth IRA contribution | $7,000 | Notice 2024-80; IRC §219(b)(5) |
| IRA catch-up (age 50+) | $1,000 | IRC §219(b)(5)(B); statutory, not indexed |

---

## Section 4 — Primary source library

Every primary source the skill cites, in one place. Every position in the brief must cite from this library or a source explicitly added to it for that position.

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §61** — Gross income definition
- **IRC §62** — Adjusted gross income (above-the-line deductions including §62(a)(1) trade or business)
- **IRC §119** — Meals or lodging furnished for the convenience of the employer
- **IRC §132(e)** — De minimis fringe benefits
- **IRC §162(a)** — Trade or business expenses, "ordinary and necessary" standard
- **IRC §162(e)** — Lobbying and political expenditures (nondeductible)
- **IRC §162(l)** — Self-employed health insurance deduction (handled in companion skill)
- **IRC §163(j)** — Business interest expense limitation
- **IRC §164** — Deduction for taxes
- **IRC §168** — Accelerated cost recovery system (MACRS)
- **IRC §168(k)** — Bonus depreciation
- **IRC §168(k) as amended by OBBBA** — Permanent 100% bonus depreciation post-Jan 19, 2025
- **IRC §170** — Charitable contribution deduction (and §170(i) charitable mileage rate)
- **IRC §179** — Election to expense certain depreciable business assets
- **IRC §179 as amended by OBBBA** — $2.5M / $4M limits effective for property placed in service after Dec 31, 2024
- **IRC §183** — Activities not engaged in for profit (hobby loss)
- **IRC §195** — Start-up expenditures
- **IRC §197** — Amortization of intangibles
- **IRC §199A** — Qualified business income deduction (handled in companion skill)
- **IRC §212** — Expenses for production of income
- **IRC §262** — Personal, living, and family expenses (nondeductible)
- **IRC §263** — Capital expenditures
- **IRC §263A** — Uniform capitalization rules
- **IRC §274** — Disallowance of certain entertainment, etc., expenses
- **IRC §274(a)** — Entertainment disallowance
- **IRC §274(d)** — Substantiation requirements for travel, meals, gifts, listed property
- **IRC §274(n)** — 50% meals limitation
- **IRC §280A** — Disallowance of expenses in connection with business use of home
- **IRC §280F** — Limitation on depreciation for luxury automobiles and listed property
- **IRC §401(c)** — Self-employed retirement plans (handled in companion skill)
- **IRC §415** — Limitations on benefits and contributions under qualified plans
- **IRC §448** — Limitation on use of cash method of accounting
- **IRC §471** — General rule for inventories
- **IRC §471(c)** — Exemption from inventory accounting for small business taxpayers
- **IRC §1401, 1402** — Self-employment tax (handled in companion skill)
- **IRC §3406** — Backup withholding
- **IRC §6001** — Notice or regulations requiring records, statements, and special returns
- **IRC §6041, 6041A** — Information reporting (1099 framework)
- **IRC §6071(c)** — Time for filing information returns

### Treasury Regulations (26 CFR)

- **Treas. Reg. §1.61-1** through §1.61-22 — Gross income
- **Treas. Reg. §1.62-2** — Reimbursements and other expense allowance arrangements (accountable plans)
- **Treas. Reg. §1.132-6** — De minimis fringes
- **Treas. Reg. §1.162-1** — Business expenses
- **Treas. Reg. §1.162-2** — Traveling expenses (and §1.162-2(e) commuting nondeductible)
- **Treas. Reg. §1.162-3** — Materials and supplies
- **Treas. Reg. §1.162-4** — Repairs (vs capital improvements)
- **Treas. Reg. §1.162-5** — Education expenses
- **Treas. Reg. §1.179-1** through §1.179-6 — Section 179 elections
- **Treas. Reg. §1.183-1, 1.183-2** — Hobby loss factors
- **Treas. Reg. §1.199A-5** — Specified service trades or businesses
- **Treas. Reg. §1.262-1** — Personal expenses
- **Treas. Reg. §1.263(a)-1(f)** — De minimis safe harbor election
- **Treas. Reg. §1.263(a)-2** — Amounts paid to acquire or produce tangible property
- **Treas. Reg. §1.263(a)-3** — Amounts paid to improve tangible property (improvement standards: betterments, restorations, adaptations)
- **Treas. Reg. §1.263(a)-3(h)** — Small taxpayer safe harbor for buildings
- **Treas. Reg. §1.263(a)-3(i)** — Routine maintenance safe harbor
- **Treas. Reg. §1.263(a)-3(n)** — Election to capitalize repair and maintenance costs
- **Treas. Reg. §1.274-2** — Disallowance of deductions for entertainment, etc.
- **Treas. Reg. §1.274-5T** — Substantiation requirements (temporary, but operative)
- **Treas. Reg. §1.274-12** — Limitation on meals
- **Treas. Reg. §1.280A-1, 1.280A-2** — Business use of home
- **Treas. Reg. §1.280F-6** — Listed property
- **Treas. Reg. §1.471-1** — Need for inventories
- **Treas. Reg. §1.6001-1** — Records to be kept

### Revenue Procedures, Revenue Rulings, Notices

- **Rev. Proc. 2013-13** — Simplified method for home office deduction
- **Rev. Proc. 2024-40** — Inflation adjustments for 2025 (issued October 2024, in part superseded by OBBBA)
- **Rev. Proc. 2025-16** — Luxury auto depreciation caps and lease inclusion amounts for 2025
- **Notice 2024-80** — 2025 retirement plan limitations
- **Notice 2025-5** — 2025 standard mileage rates
- **Rev. Rul. 99-7** — Commuting expenses, deductibility of trips between home and work locations

### IRS Publications (current 2025 versions)

- **Pub 334 (2025)** — Tax Guide for Small Business
- **Pub 463 (2025)** — Travel, Gift, and Car Expenses
- **Pub 535** — Business Expenses (DISCONTINUED; content migrated to other publications, primarily Pub 334 and Pub 535's chapters now in form instructions)
- **Pub 587 (2025)** — Business Use of Your Home
- **Pub 946 (2025)** — How to Depreciate Property

### Form instructions

- **Schedule C (Form 1040) Instructions (2025)**
- **Form 4562 Instructions (2025)** — Depreciation and Amortization
- **Form 8829 Instructions (2025)** — Expenses for Business Use of Your Home
- **Form 1040 and Schedules Instructions (2025)**
- **Form 1099-NEC Instructions (2025)**

### Court decisions

- **Welch v. Helvering, 290 U.S. 111 (1933)** — "Ordinary and necessary" standard
- **Cohan v. Commissioner, 39 F.2d 540 (2d Cir. 1930)** — Estimation of expenses where records exist but are imperfect (the "Cohan rule"; substantially limited by §274(d) for travel/meals/gifts/listed property)
- **Commissioner v. Soliman, 506 U.S. 168 (1993)** — Principal place of business test for home office (largely superseded by 1997 amendment to §280A allowing administrative or management activities to qualify)

### Authority NOT in the library (do not cite)

- Tax preparation software company blogs
- Tax newsletters
- Trade press commentary
- Anonymous "the IRS says" assertions

---

## Section 5 — Schedule C structure for tax year 2025

The 2025 Schedule C (Form 1040) has five parts. The skill classifies every transaction into a specific line within these parts, or excludes it with a documented reason.

### Part I — Income (Lines 1 through 7)

| Line | Content |
|---|---|
| 1 | Gross receipts or sales |
| 2 | Returns and allowances |
| 3 | Subtract line 2 from line 1 |
| 4 | Cost of goods sold (from line 42 in Part III) |
| 5 | Gross profit (line 3 minus line 4) |
| 6 | Other income (state fuel tax credits, etc.) |
| 7 | Gross income (line 5 plus line 6) |

### Part II — Expenses (Lines 8 through 27b)

| Line | Content | Primary source |
|---|---|---|
| 8 | Advertising | IRC §162; Schedule C Instructions (2025) |
| 9 | Car and truck expenses | IRC §162, §280F; Pub 463 (2025) |
| 10 | Commissions and fees | IRC §162 |
| 11 | Contract labor | IRC §162; 1099-NEC reportable |
| 12 | Depletion | IRC §611, §613 |
| 13 | Depreciation and §179 expense (from Form 4562) | IRC §167, §168, §168(k), §179 |
| 14 | Employee benefit programs (other than line 19) | IRC §162; excludes owner's own benefits |
| 15 | Insurance (other than health) | IRC §162 |
| 16a | Interest — mortgage (paid to banks, etc.) | IRC §163 |
| 16b | Interest — other | IRC §163; subject to §163(j) limit if applicable |
| 17 | Legal and professional services | IRC §162 |
| 18 | Office expense | IRC §162 |
| 19 | Pension and profit-sharing plans (for employees) | IRC §404; excludes owner's own contributions |
| 20a | Rent or lease — vehicles, machinery, equipment | IRC §162 |
| 20b | Rent or lease — other business property | IRC §162 |
| 21 | Repairs and maintenance | IRC §162; Treas. Reg. §1.162-4, §1.263(a)-3 |
| 22 | Supplies | IRC §162; Treas. Reg. §1.162-3 |
| 23 | Taxes and licenses | IRC §164; Pub 535 historical, now in form instructions |
| 24a | Travel | IRC §162, §274(d); Pub 463 (2025) |
| 24b | Meals (subject to 50% limit) | IRC §162, §274(n), §274(d); Pub 463 (2025) |
| 25 | Utilities | IRC §162 |
| 26 | Wages (less employment credits) | IRC §162; for employees, not owner |
| 27a | Energy efficient commercial buildings deduction (§179D) | IRC §179D; Form 7205 |
| 27b | Other expenses (from Part V line 48) | IRC §162; catch-all |

**Note on the structure for 2025:** Line 27a is designated for the §179D energy efficient commercial buildings deduction with Form 7205 attached. Line 27b is the catch-all "other expenses" total flowing from Part V. Schedule C-EZ remains discontinued (it was discontinued after tax year 2018).

### Part III — Cost of Goods Sold (Lines 33 through 42)

| Line | Content |
|---|---|
| 33 | Method used to value closing inventory (cost / lower of cost or market / other) |
| 34 | Was there any change in determining quantities, costs, or valuations? Y/N |
| 35 | Inventory at beginning of year |
| 36 | Purchases less cost of items withdrawn for personal use |
| 37 | Cost of labor (do not include any amounts paid to yourself) |
| 38 | Materials and supplies |
| 39 | Other costs |
| 40 | Add lines 35 through 39 |
| 41 | Inventory at end of year |
| 42 | Cost of goods sold (line 40 minus line 41); enter on line 4 |

### Part IV — Information on Your Vehicle (Lines 43 through 47b)

Required if claiming car or truck expenses on line 9 AND not required to file Form 4562. Captures: date placed in service, total miles, business miles, commuting miles, other personal miles, whether vehicle was available for personal use during off-duty hours, whether the taxpayer or spouse has another vehicle for personal use, whether evidence to support the deduction exists, and whether the evidence is written.

### Part V — Other Expenses (Line 48)

Itemized listing of "other expenses" that don't fit on lines 8-27a. Each item is described and totaled. The total flows to line 27b. Common items: bank fees, dues and subscriptions, education, postage and shipping (if not in office expense), software subscriptions (often), telephone (separated from utilities), uniforms, professional development.

---

## Section 6 — Position rules: classification by Schedule C line

For each Schedule C line, this section specifies: what belongs there, what does NOT belong there, the conservative default if data is ambiguous, the primary source citation, and edge cases the skill should flag for reviewer attention.

### Line 8 — Advertising

**What belongs:** Costs of promoting the business, including print and digital advertising, business cards, flyers, brochures, signage, website hosting and design, domain registration, SEO and content marketing services, social media advertising (Meta, LinkedIn, X, Google Ads, TikTok), trade show booth fees, sponsorship of events with a clear advertising connection, promotional merchandise distributed to prospects or customers (mugs, pens, t-shirts), email marketing services (Mailchimp, Constant Contact, ConvertKit), public relations services.

**What does NOT belong:**
- Political contributions and lobbying expenses (IRC §162(e); nondeductible)
- Personal social events with no business connection (§262)
- Sponsorships that are really charitable contributions (those go to Schedule A on the personal side, not Schedule C)
- Gifts to clients beyond $25 per recipient per year (excess is nondeductible under IRC §274(b)(1); the deductible portion is on line 27b "Other expenses" not line 8)

**Conservative default if ambiguous:** If the business purpose is unclear (e.g., a "sponsorship" of a community event that could be advertising or could be a charitable contribution), exclude from line 8 and flag for reviewer attention.

**Primary source:** IRC §162(a); Treas. Reg. §1.162-1; IRC §162(e) for political; IRC §274(b)(1) for gifts; Pub 334 (2025); Schedule C Instructions (2025) line 8.

**Edge cases to flag:**
- "Sponsorship" of a youth sports team or community event — may be advertising if the business name is prominently displayed and the audience is potential customers; otherwise charitable. Flag for reviewer.
- Goodwill advertising (institutional advertising designed to keep the business name before the public) — generally deductible if there's a reasonable expectation of future business benefit, per Reg. §1.162-20(a)(2). Flag if the dollar amount is material.

### Line 9 — Car and truck expenses

**What belongs:** Business use of vehicles, computed under either (a) the standard mileage method (70¢/mile for 2025, per Notice 2025-5) or (b) the actual expense method (gas, oil, repairs, insurance, registration, depreciation, lease payments, tires, washes — all multiplied by the business-use percentage).

**The method election rule (lock-in):**
- If the standard mileage method is elected in the FIRST year the vehicle is used for business, the taxpayer may switch to the actual method in a later year (subject to using straight-line depreciation for the remaining years).
- If the actual method (with MACRS depreciation) is elected in the first year, the taxpayer is **locked into the actual method** for the life of the vehicle.
- For LEASED vehicles, the method elected in the first year of the lease applies to the entire lease term.

**What does NOT belong on line 9:**
- Commuting from home to a regular place of business (Treas. Reg. §1.162-2(e); Rev. Rul. 99-7) — commuting is personal under §262.
- Personal-use portion of vehicle expenses (§262)
- Parking tickets and traffic fines (§162(f); nondeductible)
- Personal vehicle loan interest under the new OBBBA personal auto loan interest deduction — this flows to Schedule 1-A, not Schedule C. The business-use portion of vehicle loan interest belongs on line 16b.

**Conservative defaults:**
- If business-use percentage is not documented with a contemporaneous mileage log meeting §274(d), apply 0% business use (no deduction). The §274(d) substantiation requirement is strict; reconstructed estimates are not sufficient. Flag for reviewer with the §274(d) citation.
- If the taxpayer claims "100% business use" for a vehicle that is also their only personal vehicle, default to no deduction and flag — this is a known IRS audit trigger.
- If both standard mileage and actual expense data are available and the first-year election is unknown, apply the standard mileage method (the more conservative usually for typical use; reviewer can switch if actual is elected).
- If the vehicle was placed in service before 2025 and the prior method election is unknown, flag for reviewer.

**§280F luxury auto caps (2025):**
For passenger automobiles (≤6,000 lbs GVW) placed in service in 2025, the §280F first-year depreciation cap is:
- $20,200 with bonus depreciation (Rev. Proc. 2025-16 Table 1)
- $12,200 without bonus depreciation (Rev. Proc. 2025-16 Table 2)

Subsequent years: $19,600 (year 2), $11,800 (year 3), $7,060 (succeeding years).

**Heavy vehicles (>6,000 lbs GVW):** Not subject to §280F caps. Eligible for §179 expensing subject to the $31,300 SUV cap if classified as an SUV (IRC §179(b)(5)). Eligible for 100% bonus depreciation if acquired and placed in service after January 19, 2025 (OBBBA).

**Listed property recapture:** Vehicles are listed property under §280F(d)(4). If business use ever falls to 50% or below, the excess depreciation (over straight-line ADS) must be recaptured as ordinary income. Flag this for any vehicle where business use is between 50% and 100%.

**Primary source:** IRC §162; IRC §280F; Treas. Reg. §1.162-2(e); Treas. Reg. §1.274-5T; Treas. Reg. §1.280F-6; Rev. Rul. 99-7; Notice 2025-5; Rev. Proc. 2025-16; Pub 463 (2025); Schedule C Instructions (2025) line 9.

**Edge cases to flag:**
- Multiple vehicles in business use — each requires its own analysis.
- Home office establishes the home as a business location, which converts what would otherwise be commuting into deductible business mileage. Confirm home office qualification before treating any home-to-work miles as business.
- Lease inclusion amounts for leased luxury vehicles per Rev. Proc. 2025-16 Table 3 — must reduce the deduction.
- Vehicle acquired before Jan 19, 2025 → 40% bonus available; vehicle acquired after → 100% bonus available. The acquisition date matters.

### Line 10 — Commissions and fees

**What belongs:** Commissions paid to non-employees who are not contractors performing services. Examples: real estate broker commissions (when the taxpayer is a seller), sales commissions to independent reps, finder's fees, referral fees paid to third parties.

**What does NOT belong:**
- Commissions paid to employees (those are Line 26 wages)
- Commissions paid to independent contractors performing services (those are Line 11 contract labor)
- Commissions on the acquisition of capital assets (those are capitalized to the basis of the asset, not deducted)
- Bank fees, payment processor fees (those are typically Line 27b "Other expenses" — they're not commissions in the §162 sense)

**Conservative default:** If unclear whether a payment is a commission or contract labor, prefer Line 11 (contract labor), since contract labor has clearer 1099-NEC reporting consequences and the line items are interchangeable for tax effect (both are deductions).

**Primary source:** IRC §162; Schedule C Instructions (2025) line 10.

**Edge cases to flag:**
- Payment processor fees (Stripe, Square, PayPal merchant fees) — these go to Line 27b "Other expenses" or Line 17 "Legal and professional services" depending on classification preference; the skill defaults to Line 27b "Merchant processing fees" with a Part V description.

### Line 11 — Contract labor

**What belongs:** Payments to independent contractors (non-employees) for services performed for the business, including freelance designers, writers, virtual assistants, bookkeepers (if not on Line 17 as professional services — see below), photographers, video editors, software developers, consultants whose work is operational rather than advisory, cleaners and janitors who are not employees.

**What does NOT belong:**
- Payments to the owner or the owner's spouse (those are not deductible as contract labor; if the spouse is genuinely an employee, see Line 26)
- Payments to corporations for services (still belongs on Line 11 as contract labor; the corporate exception applies to 1099-NEC reporting, not to deductibility) — but flag if dollar amount is material
- Capitalized labor (labor costs that should be added to the basis of a capital asset under §263A)
- Inventory production labor (goes to Part III COGS line 37)

**The 1099-NEC obligation under §6041A:** Any contractor paid $600 or more in the calendar year for services in the course of the payor's trade or business must receive a Form 1099-NEC by January 31 of the following year, and a copy must be filed with the IRS by the same date (IRC §6041A; §6071(c)).

**Exceptions to the 1099-NEC obligation:**
- Payments to **C-corporations and S-corporations** are generally exempt from 1099-NEC reporting, EXCEPT payments to attorneys for legal services (IRC §6045(f) treatment) and payments to medical and health care providers, both of which require a 1099-NEC regardless of corporate status.
- Payments via **payment card** (credit card, debit card) are NOT reported on 1099-NEC by the payor; the payment card network reports them on 1099-K to the recipient.
- Payments via **third-party settlement organization (TPSO)** that meets the §6050W definition are NOT reported on 1099-NEC by the payor; the TPSO reports them on 1099-K.

**Critical: which payment methods qualify for the TPSO exception, and which DO NOT (NEW in v0.2):**

| Payment method | TPSO under §6050W? | 1099-NEC obligation falls on... | Working paper handling |
|---|---|---|---|
| Credit card / debit card | Yes (the card network) | Card network → 1099-K | No 1099-NEC obligation for taxpayer |
| PayPal Business | Yes | PayPal → 1099-K | No 1099-NEC obligation for taxpayer |
| Stripe | Yes | Stripe → 1099-K | No 1099-NEC obligation for taxpayer |
| Square | Yes | Square → 1099-K | No 1099-NEC obligation for taxpayer |
| Venmo Business profile | Yes | Venmo → 1099-K | No 1099-NEC obligation for taxpayer |
| **Venmo personal (Friends & Family)** | **No** | **Taxpayer → 1099-NEC** | Flag for taxpayer 1099-NEC obligation |
| **Zelle** | **No (bank-to-bank transfer)** | **Taxpayer → 1099-NEC** | Flag for taxpayer 1099-NEC obligation |
| **Personal check / cashier's check** | **No** | **Taxpayer → 1099-NEC** | Flag for taxpayer 1099-NEC obligation |
| **ACH transfer / wire transfer** | **No** | **Taxpayer → 1099-NEC** | Flag for taxpayer 1099-NEC obligation |
| **Cash** | **No** | **Taxpayer → 1099-NEC** | Flag for taxpayer 1099-NEC obligation |
| Cash App for Business | Yes | Cash App → 1099-K | No 1099-NEC obligation for taxpayer |
| **Cash App personal** | **No** | **Taxpayer → 1099-NEC** | Flag for taxpayer 1099-NEC obligation |

**Why Zelle is the most common trap:** Zelle is operated by a consortium of banks and does not act as a third-party settlement organization under §6050W. A Zelle payment is functionally a bank-to-bank transfer between the payor's account and the payee's account. The bank does not issue a 1099-K because the bank is not a TPSO. This means the §6041A 1099-NEC obligation falls fully on the payor — the same as if they had written a check.

**Why this matters:** The model must NOT apply the credit-card/PayPal exception to Zelle, Venmo personal, ACH, or check. Doing so would fail to flag the taxpayer's 1099-NEC obligation, which carries penalties under IRC §6721 (failure to file information returns) and §6722 (failure to furnish payee statements) ranging from $60 to $660 per return depending on lateness, plus a 24% backup withholding obligation under §3406 if the W-9 was never collected.

**Working paper rule:** For every Line 11 contractor with cumulative payments at or above $600 for the year, the working paper Column K reviewer attention reason must state the payment method and whether the 1099-NEC obligation falls on the taxpayer. If payment was via Zelle, Venmo personal, ACH, check, wire, or cash, the brief's "Items requiring documentation" section must list the W-9 status and note that the 1099-NEC must be filed by January 31 of the following year if not already filed.

**Conservative default:** If unclear whether a worker is a contractor or an employee, classify the payment as Line 11 contract labor with a reviewer-attention flag noting the worker classification risk. Misclassification of employees as contractors is a known IRS audit area and carries significant employment tax exposure. The skill does not adjudicate worker classification; it surfaces the risk.

**Primary source:** IRC §162; IRC §6041, §6041A, §6045(f), §6050W, §6071(c), §3406, §6721, §6722; Schedule C Instructions (2025) line 11; Form 1099-NEC Instructions (2025); Form 1099-K Instructions (2025).

**Edge cases to flag:**
- Workers paid $600+ where no W-9 was collected — flag for backup withholding obligation (24% under IRC §3406)
- Workers paid via Venmo personal / Zelle / personal check / ACH / wire / cash — these payments DO require 1099-NEC reporting at the $600 threshold; the payment processor exception does NOT apply (see table above).
- Workers who look like employees (regular hours, employer-provided tools, no business of their own) — flag for worker classification review.
- Payments that LOOK like they might be to corporations (e.g., "Acme Design LLC") — verify entity type via W-9. LLC may be disregarded (1099-NEC required), partnership (1099-NEC required), or corporation (1099-NEC NOT required, except attorneys / medical).

### Line 12 — Depletion

**What belongs:** Depletion deductions for taxpayers with an interest in natural resources (oil, gas, minerals, timber). Computed under IRC §611, §612 (cost depletion), or §613 (percentage depletion for some resources).

**Default position:** This skill defers to a specialist for any taxpayer with depletion. If a transaction would belong on Line 12, refuse the engagement and refer to a CPA or EA experienced in natural resource taxation.

**Primary source:** IRC §611, §612, §613; refer specialist.

**Refusal trigger:** Any depletion situation triggers refusal R-BOOK-DEPLETION (see Section 9).

### Line 13 — Depreciation and §179 expense (from Form 4562)

**What belongs:** Depreciation on tangible business property under MACRS, plus any §179 expensing election, plus any §168(k) bonus depreciation. The detail is computed on Form 4562 and the total flows to Line 13.

**The 2025 OBBBA depreciation framework:**

This is the single most consequential 2025 change for sole prop bookkeeping. The rules differ based on the **acquisition date** of the asset:

**Property acquired on or before January 19, 2025:**
- §168(k) bonus depreciation rate: **40%**
- Pre-OBBBA TCJA phase-down schedule applies (40% for property placed in service in 2025)
- §179 expensing available subject to pre-OBBBA limits *unless* the property is placed in service in a tax year beginning after Dec 31, 2024, in which case the OBBBA $2.5M / $4M limits apply

**Property acquired after January 19, 2025:**
- §168(k) bonus depreciation rate: **100%** (OBBBA P.L. 119-21)
- §179 expensing available with the OBBBA $2.5M cap and $4M phase-out

**The acquisition date matters more than the placed-in-service date for bonus depreciation under OBBBA.** The acquisition date is generally the date a binding written contract was entered into. For property under construction, the date construction began. For used property, the date of purchase. The Treasury and IRS have been issuing guidance on the acquisition-date determination throughout late 2025; flag any borderline case for reviewer.

**Transitional election:** For property placed in service during the first tax year ending after January 19, 2025, taxpayers may elect 40% bonus depreciation instead of 100%. Useful for taxpayers with limited income who don't want to generate large losses. Flag if the taxpayer's income suggests this might apply.

**§179 limits for 2025 (under OBBBA, IRC §179 as amended):**
- Maximum deduction: $2,500,000
- Phase-out threshold: $4,000,000 (dollar-for-dollar reduction above this)
- Heavy SUV cap (vehicles 6,001-14,000 lbs GVW): $31,300
- Subject to taxable income limitation — §179 cannot create or increase a net operating loss
- Election made on Form 4562

**§179 vs bonus depreciation decision framework:**
- §179 is income-limited and dollar-capped; bonus is not.
- §179 can be used on a per-asset basis; bonus applies to all qualified property in a class unless the taxpayer elects out of an entire class.
- For a profitable sole prop with capital purchases under $2.5M, §179 is often preferred for flexibility; for a sole prop with limited income, bonus depreciation is often better because it can create a loss.
- The skill does NOT optimize between §179 and bonus — that's a planning decision the reviewer makes. The skill captures the asset, the cost, the acquisition date, the placed-in-service date, the recovery period, and surfaces both options.

**De minimis safe harbor (Treas. Reg. §1.263(a)-1(f)):**
- Taxpayers with applicable financial statements (AFS): may expense items costing $5,000 or less per item (or per invoice line)
- Taxpayers without AFS: may expense items costing $2,500 or less per item
- Requires a written accounting policy in place at the start of the tax year
- Election is made annually on the return
- Items within the threshold are expensed (typically Line 18 office expense or Line 22 supplies, depending on use), not capitalized to Line 13

Most sole proprietors do not have AFS and use the $2,500 threshold. The skill defaults to $2,500 unless the user confirms AFS.

**What does NOT belong on Line 13:**
- Land (not depreciable)
- Inventory (goes to COGS, not depreciation)
- Property held for personal use (not deductible at all)
- Intangibles requiring §197 amortization (those go to Form 4562 different section, but flow to Line 13 via "amortization included in depreciation")
- Vehicles where the standard mileage method was elected (depreciation is built into the standard mileage rate)

**Conservative defaults:**
- If the acquisition date of an asset is unclear and could be either before or after January 19, 2025, default to the **before** date (40% bonus). Flag for reviewer.
- If the placed-in-service date is unclear, default to the later possible date (delays deduction).
- If the de minimis safe harbor election was made in a prior year is unknown, assume not made and require capitalization for items above threshold.
- If the recovery period of an asset is unclear, default to the longest plausible period.
- If the cost basis is undocumented, default to zero basis (no deduction).

**Primary source:** IRC §167, §168, §168(k), §179, §263; OBBBA P.L. 119-21 §70306 (Section 179) and the §168(k) amendment; Treas. Reg. §1.263(a)-1(f); Rev. Proc. 2025-16 (luxury auto caps); Pub 946 (2025); Form 4562 Instructions (2025); Schedule C Instructions (2025) line 13.

**Edge cases to flag:**
- Any asset with acquisition date within 30 days of January 19, 2025 — verify the binding contract date precisely (NEW in v0.2: dual treatment required, see below)
- Any asset where the §179 election would create an NOL — §179 cannot exceed taxable income from active trades or businesses
- Listed property with business use under 50% — use ADS straight-line, not MACRS GDS, and no §179
- Property converted from personal to business use — basis is the lesser of adjusted basis or FMV at conversion
- Heavy SUVs — distinguish from light trucks and confirm GVW
- Real property — different rules entirely (39-year nonresidential, 27.5-year residential rental, mid-month convention; rentals are out of scope per R-US-RENTAL)

**The 30-day OBBBA cutoff window — dual treatment requirement (NEW in v0.2):**

Any asset with an acquisition date in the window December 20, 2024 through February 18, 2025 (30 days on either side of January 19, 2025) is in the OBBBA cutoff danger zone. The bank/credit-card transaction date is NOT necessarily the acquisition date for §168(k) purposes — the acquisition date is the date a binding written contract was entered into, the date of order placement for retail purchases, or the date construction began for self-constructed property.

For any asset in the 30-day window:

1. **Capture both possible dates explicitly** in the asset detail on Form 4562: the bank transaction date, the order placement date if known, the binding contract date if known. State which date is being used and why.

2. **Prepare both treatments in the working paper:** the 40% bonus / pre-OBBBA treatment AND the 100% bonus / post-OBBBA treatment. The reviewer makes the final call based on documentation the user produces.

3. **Add a high-priority reviewer attention flag** with explicit language: "Asset acquired within 30 days of OBBBA cutoff (Jan 19, 2025). Reviewer must verify binding contract date or order placement date before finalizing the depreciation election. The bank transaction date alone is insufficient evidence of acquisition under IRC §168(k)."

4. **Add a documentation request to the structured question form:** purchase order, invoice, order confirmation email, or written contract showing the acquisition date.

5. **If the user cannot produce documentation**, the conservative default applies: use the date that produces less depreciation (the **earlier** date, which gives 40% bonus instead of 100%). State this in the brief.

This dual-treatment rule exists because the dollar swing on a single asset can be material — for a $5,000 computer, the difference between 40% and 100% bonus is $3,000 of current-year deduction, and the line between the two treatments may be a single business day on the calendar.

### Line 14 — Employee benefit programs

**What belongs:** Contributions to benefit plans for **employees** (not the owner): employer-paid health insurance for employees, group-term life insurance under §79, dependent care assistance under §129, educational assistance under §127, accident insurance, disability insurance, employer contributions to HSAs for employees.

**What does NOT belong:**
- The owner's own health insurance — that goes on Schedule 1 line 17 as the self-employed health insurance deduction (handled in companion skill `us-form-1040-self-employed-positions`)
- Pension and profit-sharing contributions for employees — those go on Line 19
- Owner's own retirement contributions — those go on Schedule 1 (handled in companion skill)

**Refusal note:** The base catalogue refusal R-US-EMPLOYEES fires if the business has any W-2 employees. A bare sole prop with no employees has nothing on Line 14. This line is effectively zero for in-scope clients. If transactions appear to belong here, the engagement should have been refused at Step 5 of the workflow.

**Primary source:** IRC §162, §79, §125, §127, §129; Schedule C Instructions (2025) line 14.

### Line 15 — Insurance (other than health)

**What belongs:** Business insurance premiums: general liability, professional liability / E&O / malpractice insurance, business property insurance, commercial auto insurance (if the standard mileage method is NOT being used; if standard mileage, the insurance is built into the rate and does NOT go here), business interruption insurance, cyber liability insurance, key person life insurance (in narrow cases), workers' compensation (if applicable), umbrella policies allocated to business use.

**What does NOT belong:**
- Owner's personal life insurance (§262; nondeductible)
- Owner's personal disability insurance (§262; nondeductible)
- Owner's health insurance (Schedule 1; companion skill)
- Insurance on personal property (§262)
- Self-insurance reserves (not deductible until paid out)
- The business-use portion of an insurance premium where the personal portion is on Schedule A — split the premium and put only the business portion on Line 15

**Conservative default:** If a premium covers both business and personal property and the allocation is undocumented, default to a 100% personal allocation (no business deduction). Flag for reviewer.

**Primary source:** IRC §162; Treas. Reg. §1.162-1; Schedule C Instructions (2025) line 15.

**Edge cases:**
- Term life insurance on the owner where the business is the beneficiary — generally not deductible (§264)
- Health insurance for the owner — never on Line 15; always Schedule 1 via §162(l)

### Line 16 — Interest

**Line 16a (mortgage interest paid to banks, etc.):** Mortgage interest on real property used in the business, paid to a financial institution. Most sole props will not have anything here unless they own commercial real estate.

**Line 16b (other business interest):** All other business interest — credit card interest on a business credit card (if the charges were business expenses), business loan interest, line of credit interest, business vehicle loan interest (the business-use portion), interest on equipment financing.

**The §163(j) limitation:** For 2025, taxpayers with average annual gross receipts ≤ $31M (the small business exception under §163(j)(3) referencing §448(c)) are exempt from the §163(j) interest limitation. Most sole props are well below this threshold and the limitation does not apply. Flag if the taxpayer's gross receipts approach the threshold.

**What does NOT belong:**
- Personal mortgage interest (Schedule A)
- Interest on personal credit cards even if some business charges are mixed in — split the interest, only the business portion is deductible, and substantiation is hard. Conservative default: exclude personal-card interest entirely unless cleanly separable.
- Personal auto loan interest (the new OBBBA deduction goes on Schedule 1-A, not Schedule C). The business-use portion of business auto loan interest belongs on Line 16b.
- Investment interest (Schedule A if applicable, subject to §163(d))
- Interest paid to the owner for loans from owner to business — generally a wash; not a real deduction

**Conservative defaults:**
- Mixed personal/business credit card → no deduction unless the business portion is cleanly identifiable and substantiated.
- Business-use percentage on a vehicle loan → use the same percentage as the vehicle expenses on Line 9.

**Primary source:** IRC §163, §163(j); Treas. Reg. §1.163-8T; Schedule C Instructions (2025) lines 16a and 16b.

### Line 17 — Legal and professional services

**What belongs:** Fees for tax preparation (the business portion only), legal fees for business matters (contracts, business formation, litigation defense for the business), accounting and bookkeeping services, business consulting, expert witness fees, patent and trademark filing fees, business advisory services, fractional CFO services.

**What does NOT belong:**
- Personal legal fees (§262) — divorce, personal injury, estate planning
- Capitalized legal fees (legal fees to acquire a capital asset are added to the asset's basis, not deducted; legal fees to defend title to property are also capitalized)
- Tax preparation fees for the personal portion of the return (not deductible post-TCJA for individuals; the business portion of tax prep is still deductible on Line 17)
- Fees to start up the business before it began operations (those are §195 start-up costs, subject to the $5,000 immediate deduction with phase-out and 15-year amortization for the rest)

**Conservative defaults:**
- If a legal fee could be capital or current, default to capital (no deduction in current year). Flag.
- If a legal fee is mixed personal/business and the allocation is undocumented, default to 100% personal (no deduction).

**Primary source:** IRC §162, §195, §263; Schedule C Instructions (2025) line 17.

**Edge cases to flag:**
- Pre-operating expenses → §195 start-up cost rules
- Legal fees in connection with the acquisition of a business or substantial asset → capitalize

### Line 18 — Office expense

**What belongs:** Day-to-day office consumables: paper, pens, printer ink and toner, postage (if not separately broken out), envelopes, file folders, paper clips, staplers, calculators, small office equipment under the de minimis threshold ($2,500 / $5,000), software subscriptions if not better classified elsewhere.

**What does NOT belong:**
- Computers, monitors, printers, furniture costing more than the de minimis threshold (those are capital, Line 13)
- Cleaning services (those are Line 27b "Other expenses")
- Telephone and internet (those are Line 25 utilities or Line 27b)
- Software subscriptions are sometimes here, sometimes Line 27b — the skill defaults Line 18 for productivity software (Microsoft 365, Google Workspace, basic accounting software) and Line 27b for industry-specific or specialized SaaS

**Conservative default:** Anything over $2,500 → Line 13 capitalization rather than Line 18, unless the de minimis safe harbor is elected and the item meets it.

**Primary source:** IRC §162; Treas. Reg. §1.263(a)-1(f); Schedule C Instructions (2025) line 18.

### Line 19 — Pension and profit-sharing plans (for employees)

**What belongs:** Employer contributions to retirement plans for **employees**: employer SEP contributions for employees, employer SIMPLE matches and contributions, employer 401(k) match and profit-sharing for employees.

**What does NOT belong:**
- Owner's own retirement contributions (those flow through the personal return; handled in companion skill `us-form-1040-self-employed-positions`)
- Plan administration fees paid by the business (those go to Line 17 legal and professional services if sufficiently itemized, or Line 27b)

**Refusal note:** Per R-US-EMPLOYEES, businesses with employees are out of scope. This line is effectively zero for in-scope clients. The owner's own SEP/Solo 401(k)/SIMPLE contributions never appear here.

**Primary source:** IRC §404; Schedule C Instructions (2025) line 19.

### Line 20a — Rent or lease, vehicles, machinery, and equipment

**What belongs:** Lease payments on business vehicles (if not using standard mileage), equipment leases (copiers, machinery, technology), short-term rentals of equipment for specific projects.

**Lease inclusion amount for luxury vehicle leases:** For leased passenger autos with FMV exceeding the inflation-adjusted threshold, an inclusion amount per Rev. Proc. 2025-16 Table 3 must reduce the deduction. The inclusion amount is added to gross income or netted against the lease deduction depending on the year. The skill flags any vehicle lease and prompts the reviewer to check for inclusion amount applicability.

**What does NOT belong:**
- Real property leases (those are Line 20b)
- Capitalized lease payments (true leases vs financing arrangements — financing arrangements are not deductible as rent; the asset is capitalized and depreciated and the interest is on Line 16)

**Conservative default:** If a "lease" might actually be a financing arrangement (lease-to-own with bargain purchase option, lease term exceeding 75% of useful life, etc.), flag for reviewer to determine substance over form.

**Primary source:** IRC §162; IRC §280F (lease inclusion); Rev. Proc. 2025-16 Table 3; Schedule C Instructions (2025) line 20a.

### Line 20b — Rent or lease, other business property

**What belongs:** Rent paid for office space, retail space, warehouse space, storage units used for business, coworking space memberships (WeWork, Industrious, Regus, Spaces, Switchyards, etc.), conference room rentals.

**What does NOT belong:**
- Home office expenses (those go through Form 8829 to Line 30, not Line 20b)
- Personal rent (§262)
- Equipment and vehicle leases (Line 20a)
- Lease-purchase arrangements that are really financings (capitalize)

**Coworking memberships:** Generally Line 20b. Some practitioners place coworking on Line 27b "Other expenses." Either is defensible; the skill defaults to Line 20b.

**Primary source:** IRC §162; Schedule C Instructions (2025) line 20b.

### Line 21 — Repairs and maintenance

**What belongs:** Costs to keep business property in ordinary operating condition: vehicle maintenance (oil changes, tire rotation, brake repairs — only if using actual expense method, not standard mileage), equipment repairs, building repair (paint touch-ups, fixing a broken window, plumbing repair), HVAC servicing, computer repairs, software bug fixes (paid to a developer).

**What does NOT belong (must be capitalized under §263 and the repair regulations):**
- **Betterments:** Costs that materially add to the value, substantially prolong the useful life, or adapt the property to a new or different use. Examples: a major engine rebuild that extends a vehicle's life, a building addition, replacing a roof entirely (vs patching).
- **Restorations:** Costs to restore property to its previously functional state after it has fallen into disrepair (rebuilding an asset that has been written off, replacing a major component).
- **Adaptations:** Costs to adapt property to a new or different use than originally intended.

**The repair regulations safe harbors:**

**Routine maintenance safe harbor (Treas. Reg. §1.263(a)-3(i)):** Activities the taxpayer reasonably expects to perform more than once during the property's class life (for non-buildings) or more than once during a 10-year period (for buildings) to keep the property in ordinarily efficient operating condition. If a maintenance activity meets this safe harbor, it's deductible regardless of dollar amount.

**Small taxpayer safe harbor for buildings (Treas. Reg. §1.263(a)-3(h)):** A taxpayer with average annual gross receipts ≤ $10M may elect to expense (rather than capitalize) repairs and improvements to a building with an unadjusted basis ≤ $1M, provided the total annual repair/improvement spend on that building is the lesser of $10,000 or 2% of the building's unadjusted basis.

**Conservative defaults:**
- If a "repair" could plausibly be a betterment, restoration, or adaptation, capitalize (Line 13). Flag.
- If the dollar amount is large (>$2,500 single invoice), default to capitalization unless the routine maintenance safe harbor clearly applies. Flag.
- The de minimis safe harbor under §1.263(a)-1(f) applies to acquisitions, not repairs — don't conflate the two.

**Primary source:** IRC §162, §263; Treas. Reg. §1.162-4; Treas. Reg. §1.263(a)-3 (improvement standards), §1.263(a)-3(h) (small taxpayer safe harbor), §1.263(a)-3(i) (routine maintenance safe harbor); Pub 535 historical content; Schedule C Instructions (2025) line 21.

### Line 22 — Supplies

**What belongs:** Materials and supplies consumed in the business that are not part of inventory or COGS. Per Treas. Reg. §1.162-3:
- **Incidental materials and supplies** (no inventory kept, no records of consumption): deductible when paid
- **Non-incidental materials and supplies** (records kept): deductible when used or consumed

Examples: cleaning supplies, small tools that don't meet capitalization, raw materials for projects that aren't part of formal inventory, packaging materials, shop consumables.

**What does NOT belong:**
- Inventory items (Part III COGS)
- Items above the de minimis safe harbor that should be capitalized
- Personal supplies (§262)

**Conservative default:** If a "supply" could really be inventory (the business sells the item to customers), flag for COGS classification.

**Primary source:** IRC §162; Treas. Reg. §1.162-3; Schedule C Instructions (2025) line 22.

### Line 23 — Taxes and licenses

**What belongs:**
- State and local real estate taxes on business property
- State and local personal property taxes on business assets
- State and local sales tax (when the business is the consumer, not when collected from customers)
- Payroll taxes (employer's share of FICA, FUTA, SUTA) — N/A for in-scope clients with no employees
- Business license fees, professional licensing, regulatory fees
- State franchise tax / state entity-level taxes for SMLLCs (e.g., California's $800 minimum franchise tax)
- Excise taxes paid as a cost of doing business
- State and local gross receipts taxes (e.g., Washington B&O tax, Oregon CAT)
- Federal highway use tax for heavy vehicles (Form 2290)

**What does NOT belong:**
- Federal income tax (never deductible against the business)
- State and local income tax (deductible on Schedule A, not Schedule C, subject to the $40K SALT cap under OBBBA — handled in companion skill)
- Self-employment tax (the deductible half goes on Schedule 1, not Schedule C)
- Sales tax collected from customers and remitted (this is a wash, not an expense — the customer paid it, the business is just a conduit)
- Penalties and fines (§162(f); nondeductible)
- Estate and gift taxes

**Conservative default:** If a "tax" payment is actually penalties or interest on late tax payment, exclude (penalties under §162(f), interest on tax deficiencies generally not deductible per §163(h)).

**Primary source:** IRC §162, §164; IRC §162(f) for penalties; Schedule C Instructions (2025) line 23.

### Line 24a — Travel

**What belongs:** Travel expenses while away from the tax home overnight on business: airfare, train, rental car (or actual vehicle expenses for personal vehicle on the trip), hotel/lodging, baggage fees, taxis/Uber/Lyft to/from airports and between business meetings, parking and tolls, business calls and internet during travel, laundry and dry cleaning during extended travel, tips related to business travel, conference fees (if separately tracked).

**The "tax home" concept:** The taxpayer's regular or principal place of business, regardless of where they live. Travel becomes deductible only when away from the tax home overnight. A taxpayer with no regular place of business may be considered an itinerant with no tax home, in which case nothing is deductible as travel — flag this for reviewer.

**What does NOT belong on Line 24a:**
- Meals during travel (those go to Line 24b at 50%)
- Entertainment during travel (§274(a); 0% deductible)
- Personal portion of mixed-purpose trips (split required)
- Travel for primarily personal purposes with incidental business (not deductible at all)
- Spousal travel (only deductible if the spouse is an employee with a bona fide business purpose for the trip — almost never the case for sole props)
- Commuting (not "travel" in the §162 sense)

**§274(d) substantiation requirement:** Travel is listed in §274(d), meaning the taxpayer must substantiate amount, time, place, business purpose, and (for entertainment, before its disallowance) attendees. The Cohan rule does NOT save undocumented travel. Receipts, calendars, and contemporaneous notes are required. Reconstructed estimates are not sufficient.

**Conservative defaults:**
- If documentation does not meet §274(d), exclude the deduction. Flag.
- If a trip was mixed business and personal and the allocation is undocumented, exclude entirely.
- If the trip was outside the US for more than 7 days and the business portion is less than 75%, special allocation rules apply per IRC §274(c) — flag for reviewer.

**Primary source:** IRC §162, §274(c), §274(d); Treas. Reg. §1.274-5T; Pub 463 (2025); Schedule C Instructions (2025) line 24a.

### Line 24b — Meals (50% deductible)

**What belongs:** Business meals subject to the 50% limitation under §274(n)(1):
- Meals with clients, prospects, or business associates where business is discussed
- Meals during overnight business travel (the 50% applies, not 100%)
- Meals at business conferences (when not included in the conference fee)
- Meals provided to employees (subject to specific rules) — N/A for in-scope clients with no employees

**The §274 rules in 2025:**
- General rule: business meals are 50% deductible (IRC §274(n)(1))
- **There is NO 100% deduction for restaurant meals in 2025.** The temporary 100% restaurant meal rule under CAA 2021 §210 expired after December 31, 2022 and was not extended.
- Entertainment is 0% deductible (§274(a)(1) post-TCJA)
- De minimis fringe benefits (office snacks, coffee, occasional pizza) are 100% deductible under §132(e)
- Meals provided for the convenience of the employer on business premises (§119) — narrow rule, mostly N/A for sole props

**The §274(d) substantiation requirement:** Same as travel — must document amount, date, place, business purpose, and business relationship of attendees. The Cohan rule does NOT save undocumented meals. The IRS audit standard is strict.

**Conservative defaults:**
- If §274(d) documentation is missing, exclude. Flag.
- If a meal could be entertainment in disguise (a "business dinner" that's really tickets to a sporting event with food included), check whether the meal was separately stated on the receipt — only the separately stated meal portion qualifies.
- "Lavish or extravagant" meals — partially nondeductible. The skill flags any meal > $200 per attendee for reviewer attention.
- Solo meals while not traveling overnight — generally not deductible (no business purpose distinct from personal sustenance). Exclude. Flag.

**Primary source:** IRC §162, §274(a), §274(d), §274(n); Treas. Reg. §1.274-12; Pub 463 (2025); Schedule C Instructions (2025) line 24b.

**Edge cases to flag:**
- Restaurant meals in 2025 are 50%, not 100%. Be alert for any source or workflow that asserts 100%.
- Per diem meals — if using the federal per diem rate for travel meals (Pub 463), the per diem amount is subject to the 50% limit.
- Meals provided to non-employees in exchange for services — could be compensation (1099-NEC) rather than meals.

### Line 25 — Utilities

**What belongs:** Utilities for business premises: electricity, gas, water, sewer, trash, internet (business portion if mixed-use), business phone lines.

**For home-based businesses:** Utilities for the home office are generally allocated through Form 8829 (actual expense method) and flow to Line 30 of Schedule C, NOT to Line 25. Do not double-count. Line 25 is only for utilities at a separate business premises.

**Phone-specific rule:** Per Pub 535 historical content and the IRS position, the basic local telephone service (the first landline) for a residence is treated as a personal expense (§262), even if the line is also used for business. Additional business lines, business-only lines, business cell phones, and long-distance charges for business purposes are deductible.

**What does NOT belong:**
- Personal utilities for the home not used in a qualifying home office
- Home office utilities (those go through Form 8829)

**Conservative default:** Mixed-use utility expenses without an allocation method → exclude or apply a very conservative business-use percentage (e.g., 10%) and flag.

**Primary source:** IRC §162, §262; Pub 587 (2025); Schedule C Instructions (2025) line 25.

### Line 26 — Wages (less employment credits)

**What belongs:** Gross wages paid to employees (excluding the owner and the owner's spouse unless the spouse is a bona fide employee with a separate business reason). Includes bonuses, commissions paid to employees, taxable fringe benefits already in W-2 wages.

**Refusal:** Per R-US-EMPLOYEES, businesses with W-2 employees are out of scope. Line 26 is effectively zero for in-scope clients.

**Primary source:** IRC §162, §3401; Schedule C Instructions (2025) line 26.

### Line 27a — Energy efficient commercial buildings deduction (§179D)

**What belongs:** Deduction under IRC §179D for energy-efficient improvements to commercial buildings, claimed via Form 7205. Generally rare for sole props.

**Refusal:** This skill refuses §179D positions. Refer to a specialist. Triggers refusal R-BOOK-179D.

**Primary source:** IRC §179D; Form 7205 Instructions (2025).

### Line 27b — Other expenses (from Part V, Line 48)

**What belongs:** Business expenses that don't fit cleanly on lines 8 through 27a. Itemized in Part V (Line 48) with descriptions, totaled and flowing to Line 27b.

Common items:
- Bank fees on business accounts
- Merchant processing fees (Stripe, Square, PayPal, Shopify Payments)
- Dues and subscriptions (professional associations, trade publications, online communities)
- Continuing education and training (if not capitalized as start-up; ongoing CE for an established business is deductible)
- Software subscriptions (industry-specific SaaS)
- Postage and shipping (if not in office expense)
- Cleaning services (if not in repairs)
- Uniforms and protective clothing (only if required as a condition of employment or unsuitable for general wear)
- Publications, books, research materials directly related to the business
- Business gifts (limited to $25 per recipient per year under §274(b)(1))
- Trade show fees
- Domain registration and web hosting (if not on Line 8 advertising)
- Tax research subscriptions, accounting CPE
- AI and ML services (Anthropic API, OpenAI API, etc.) — line 27b unless clearly advertising-related

**The §274(b)(1) gift limit:** Business gifts are deductible up to $25 per recipient per year. Anything above is nondeductible. Track per-recipient totals across the year.

**What does NOT belong on 27b:**
- Items that fit a specific line above (don't dump into 27b)
- Personal expenses (§262)
- Items already deducted elsewhere

**Conservative defaults:**
- Items that could fit a specific line should go on the specific line. Use 27b only as the catch-all.
- For ambiguous items, prefer 27b with a clear Part V description over forcing them onto a wrong specific line.

**Primary source:** IRC §162, §274(b)(1); Schedule C Instructions (2025) line 27b and Part V.

---

## Section 7 — Cross-cutting rules

These rules apply across multiple Schedule C lines and inform the classification of every transaction.

### The "ordinary and necessary" standard (IRC §162(a))

Every business expense must satisfy IRC §162(a): it must be "ordinary and necessary" for carrying on the trade or business. Per *Welch v. Helvering*, 290 U.S. 111 (1933):

- **Ordinary** means common and accepted in the taxpayer's particular trade or business. It does NOT mean "habitual" — a one-time expense can still be ordinary if it's the kind of expense someone in that trade would normally incur.
- **Necessary** means appropriate and helpful for the development of the business. It does NOT mean "indispensable."

The skill applies this as a sanity check on every classification: would a competent reviewer reading the same facts agree that this expense is ordinary and necessary for this taxpayer's specific trade or business? If the answer is uncertain, the expense is excluded with a flag.

Examples where ordinary-and-necessary fails:
- A graphic designer claiming a tractor (not ordinary for the trade)
- A consultant claiming a household-sized inventory of office supplies (not necessary)
- Any expense where the personal element is dominant (§262)

### Personal vs business expenses (IRC §262)

Per IRC §262(a), no deduction is allowed for personal, living, or family expenses. The skill enforces this strictly:

- Mixed-use items require allocation between business and personal portions, with substantiation for the business-use percentage.
- If the business-use percentage is undocumented, the conservative default is 0% business use (no deduction).
- Common mixed-use items: vehicles, phones, internet, computers, home utilities, home office space.
- The taxpayer's burden is to establish the business connection. Without contemporaneous records, the deduction fails.

### Owner contributions and owner draws (NEW in v0.2)

A sole proprietor and their business are the same legal and tax person. Money moving between the owner's personal accounts and the business accounts is NOT income, NOT an expense, NOT deductible, and NOT taxable. It is a balance-sheet movement only.

**Owner contributions (money flowing FROM personal TO business accounts):**
- Treatment: Excluded from gross receipts. Not on Schedule C.
- Working paper handling: Column N "Excluded? Reason if yes" → "Owner capital contribution from personal funds. Not income; sole prop and owner are same tax person."
- Common patterns: "DEPOSIT FROM PERSONAL CHASE", "TRANSFER FROM PERSONAL", "OWNER DEPOSIT", round-number deposits without an invoice reference, deposits matching the owner's personal account number prefix
- Citation: IRC §61 (gross income definition) — owner contributions are not gross income because there is no separate taxable entity. Treas. Reg. §1.61-1(a) limits gross income to amounts received from sources other than the taxpayer themselves.

**Owner draws (money flowing FROM business TO personal accounts):**
- Treatment: Excluded from expenses. Not on any Schedule C line. Not on Line 26 (wages — owner is not an employee). Not on Line 19 (pension — owner draws are not retirement contributions). Not on Line 14 (employee benefits — owner is not an employee). Specifically NOT on Line 30 (home office), NOT on Line 27a (other expenses), NOT anywhere on Schedule C.
- Working paper handling: Column N → "Owner draw to personal account. Not deductible; sole prop and owner are same tax person."
- Common patterns: "TRANSFER TO CHASE PERSONAL", "TRANSFER TO PERSONAL", "OWNER WITHDRAWAL", "DRAW", round-number transfers to the owner's personal account
- Citation: IRC §262(a) (personal living expenses not deductible); the foundational principle that a sole proprietor cannot deduct payments to themselves because there is no separate payer-payee relationship.

**Why this matters:** A sole proprietor on cash basis often runs significant cash through their business account that is properly excluded from both gross receipts and expenses. Misclassifying owner contributions as gross receipts inflates income and SE tax. Misclassifying owner draws as expenses inflates deductions and creates an audit-trigger pattern (deductions exceeding the §162 ordinary-and-necessary standard). Both are common errors and both must be caught by the classification.

**Edge cases:**
- A "deposit from personal" that is actually a customer payment routed through the wrong account first is gross receipts, not an owner contribution. Look for a customer name in the description or a matching invoice. If neither, default to owner contribution and flag for reviewer.
- A "transfer to personal" that is actually a payment to the owner's personal credit card on which business expenses were charged is NOT an owner draw — it is the settlement of an interaccount loan and the underlying business expenses on the personal card are still deductible if substantiated separately. Default to owner draw treatment unless the user provides credit card statements showing the underlying business expenses.
- An owner check to the business account for "loan from owner" is functionally the same as a contribution for sole prop purposes (no separate entity, no loan tracking required for federal income tax). Treat as owner contribution.
- Owner contributions and draws may be relevant for state income tax, business property tax, or local fee purposes, but not for federal Schedule C. State tax is out of scope.

### Capital vs current expenditure (IRC §263 and the repair regulations)

Per IRC §263 and the repair regulations under Treas. Reg. §1.263(a)-1 through §1.263(a)-3, expenditures that produce a long-term benefit must be capitalized rather than deducted in the current year. The framework:

1. **Acquisitions of new tangible property** — capitalize unless the de minimis safe harbor applies (§1.263(a)-1(f), $2,500 / $5,000 thresholds).
2. **Improvements to existing property** — capitalize if the expenditure is a betterment, restoration, or adaptation (§1.263(a)-3). Otherwise, treat as a deductible repair under §1.162-4.
3. **Routine maintenance** — deductible under the routine maintenance safe harbor (§1.263(a)-3(i)) regardless of dollar amount, if the maintenance is reasonably expected to be performed more than once during the property's class life (or more than once during a 10-year period for buildings).
4. **Small taxpayer safe harbor for buildings** — taxpayers with average annual gross receipts ≤ $10M may elect to expense building repairs and improvements up to the lesser of $10,000 or 2% of the building's unadjusted basis (§1.263(a)-3(h)).

### §274(d) substantiation for travel, meals, gifts, and listed property

IRC §274(d) imposes a heightened substantiation standard for four categories:

1. **Travel** away from home (Line 24a)
2. **Meals** (Line 24b) — but note that the §274(d) requirements still apply even though entertainment is now disallowed
3. **Business gifts** (Line 27b under §274(b)(1))
4. **Listed property** under §280F(d)(4) — vehicles, computers (in some cases), and other property used for personal purposes

For these four categories, the taxpayer must substantiate by adequate records or sufficient evidence: amount, time, place, business purpose, and business relationship of any other persons involved. The Cohan rule does NOT apply — undocumented amounts are disallowed in full, not estimated.

The skill applies the §274(d) standard rigorously. Any transaction in these four categories without contemporaneous documentation is flagged for either exclusion or reviewer attention.

### Hobby loss rules (IRC §183)

If an activity is not engaged in for profit, it is a hobby under §183. Post-TCJA, hobby expenses are NOT deductible at all (the prior 2% miscellaneous itemized deduction floor was eliminated). Hobby income remains fully taxable.

**The nine-factor test (Treas. Reg. §1.183-2(b)):**
1. Manner in which the taxpayer carries on the activity (businesslike or not)
2. Expertise of the taxpayer or advisors
3. Time and effort expended
4. Expectation that assets used in the activity may appreciate in value
5. Success in carrying on similar or dissimilar activities
6. History of income or losses
7. Amount of occasional profits, if any
8. Financial status of the taxpayer
9. Elements of personal pleasure or recreation

**The presumption of profit (§183(d)):** An activity is presumed to be for profit if it had a profit in 3 of the 5 most recent consecutive tax years (2 of 7 for activities consisting in major part of breeding, training, showing, or racing horses).

**Conservative default:** If the business has had losses for 3+ consecutive years and the §183 presumption is not met, flag for reviewer with a §183 risk note. The skill does not refuse the engagement, but the reviewer needs to assess hobby loss exposure.

**Primary source:** IRC §183; Treas. Reg. §1.183-1, §1.183-2.

---

## Section 8 — Conservative defaults table

Concrete defaults for each ambiguity type the skill encounters. Per Section 2 of the base, conservative means "the option that costs the taxpayer more tax." Every default applied must be flagged in the reviewer brief.

| Ambiguity | Conservative default | Citation rationale |
|---|---|---|
| Business-use percentage of an asset undocumented | 0% (no deduction) | §274(d) substantiation; §262 personal default |
| Mileage log not contemporaneous or missing | 0 business miles | §274(d); Treas. Reg. §1.274-5T |
| Acquisition date of asset on or near Jan 19, 2025 ambiguous | Before Jan 19, 2025 (40% bonus, not 100%) | OBBBA cutoff conservatism |
| §179 election in prior year unknown | Not made | No retroactive election permitted |
| De minimis safe harbor election in prior year unknown | Not made | Election is annual; no presumption |
| Asset basis undocumented | $0 | Taxpayer has burden to establish basis |
| Receipt for §274(d) item missing | Not deductible | Cohan rule does not apply post-1985 |
| Worker classification (employee vs contractor) unclear | Flag for reviewer; classify as contractor for line item only with risk note | Skill does not adjudicate; reviewer decides |
| Mixed-use credit card (personal and business) | Exclude entirely unless business portion cleanly separable | §262 default |
| Meal during business travel without purpose documentation | Not deductible | §274(d) |
| Solo meal (not while traveling overnight) | Not deductible | No business purpose distinct from personal |
| "Sponsorship" that could be advertising or charitable | Exclude from Line 8; flag | Conservative on character |
| "Repair" that could be a betterment | Capitalize (Line 13) | §263 / repair regs default |
| Pre-operating expense | §195 start-up cost treatment | $5,000 immediate, balance over 15 years |
| Depreciation method election in prior year unknown | Use ADS straight-line (most conservative) | No presumption of accelerated election |
| Hobby loss 3-year loss streak | Flag for reviewer; do not refuse | §183 risk note required |
| Personal vehicle loan interest | Schedule 1-A (OBBBA), not Schedule C | OBBBA personal deduction |
| Restaurant meal in 2025 | 50%, not 100% | §274(n)(1); no special rule for 2025 |
| Tip / overtime / senior deduction (OBBBA new) | Not on Schedule C | Companion skill / Schedule 1-A |
| Item over $2,500 without de minimis safe harbor election | Capitalize (Line 13) | Default capitalization rule |
| Asset placed in service date unknown | Latest plausible date | Defers deduction |
| Recovery period of asset unclear | Longest plausible | Defers deduction |
| Rental property activity | Refuse (R-US-RENTAL) | Out of scope |
| Cryptocurrency transaction | Refuse (R-US-CRYPTO) | Out of scope |
| Foreign currency transaction | Refuse (R-US-FOREIGN) | Out of scope |
| Cost segregation study question | Refuse (R-BOOK-COSTSEG) | Out of scope |
| §179D energy efficient buildings | Refuse (R-BOOK-179D) | Out of scope |
| Depletion | Refuse (R-BOOK-DEPLETION) | Out of scope |

---

## Section 9 — Topical refusal catalogue

Refusals on top of the global refusal catalogue in `us-tax-workflow-base` Section 6. Each refusal has a code (R-BOOK-XXX), a trigger condition, and an output message.

**R-BOOK-DEPLETION — Depletion (Line 12).**
Trigger: The taxpayer has any interest in natural resources requiring depletion under IRC §611 (oil, gas, minerals, timber).
Output: "Depletion deductions for natural resources require specialized analysis under IRC §611-§613, including the choice between cost depletion and percentage depletion, and the income limitation rules. This skill does not handle natural resource taxation. Please consult a CPA or Enrolled Agent who specializes in oil and gas, mining, or timber taxation."

**R-BOOK-179D — Energy efficient commercial buildings deduction (Line 27a).**
Trigger: The taxpayer is claiming or considering a §179D deduction for energy-efficient improvements to commercial buildings.
Output: "The §179D energy efficient commercial buildings deduction requires a certified engineering study and Form 7205. This skill does not handle §179D positions. Please consult a CPA or Enrolled Agent with §179D experience."

**R-BOOK-COSTSEG — Cost segregation study.**
Trigger: The taxpayer has had a cost segregation study performed on real property, or is considering one.
Output: "Cost segregation studies allocate real property costs across multiple depreciation classes and require specialized engineering analysis. This skill does not handle cost segregation. Please consult a CPA or specialist firm with cost segregation experience."

**R-BOOK-INVENTORY-LARGE — Inventory accounting above the §471(c) threshold.**
Trigger: The business has average annual gross receipts exceeding $31,000,000 over the prior three years (the §471(c) / §448(c) threshold for tax year 2025).
Output: "Businesses above the $31M small business threshold under IRC §471(c) and §448(c) must use accrual accounting and maintain inventory under the general rules of §471. This skill is scoped to small businesses below this threshold. Please consult a CPA experienced with mid-size business accounting and inventory."

**R-BOOK-UNICAP — UNICAP / §263A applicability.**
Trigger: The business is producing inventory or property and might be subject to UNICAP rules under §263A despite being below the §471(c) threshold (e.g., a manufacturer or builder).
Output: "Uniform capitalization rules under IRC §263A may require capitalization of indirect costs into inventory or property. The interaction with the §471(c) small business exception is nuanced. Please consult a CPA or Enrolled Agent for UNICAP analysis."

**R-BOOK-START-UP-LARGE — Large start-up costs.**
Trigger: The taxpayer has start-up expenditures under §195 exceeding $50,000 (the threshold at which the $5,000 immediate deduction phases out dollar-for-dollar).
Output: "Start-up costs above $50,000 trigger phase-out of the §195 immediate deduction and require careful tracking and amortization scheduling. Please consult a CPA or Enrolled Agent with experience in §195 start-up cost analysis."

**R-BOOK-CONVERSION — Personal-to-business conversion of an asset.**
Trigger: The taxpayer converted personal-use property to business use during the tax year (e.g., started using a personal vehicle for business, started using a personal computer for business at the level of a separate asset).
Output: "Personal-to-business conversion of an asset requires basis analysis (lesser of adjusted basis or fair market value at conversion) and prospective depreciation only. The interaction with §280F listed property rules can be complex. The skill flags this for reviewer attention rather than refusing, but the reviewer must verify the conversion treatment."

(Note: R-BOOK-CONVERSION is a flag, not a hard refusal — the skill will note the conversion and the conservative defaults but the reviewer makes the call.)

**R-BOOK-NOL — Schedule C generates a current-year NOL.**
Trigger: The current-year Schedule C produces a loss large enough to push the taxpayer's overall income negative, indicating an NOL.
Output: "A Schedule C loss large enough to create a net operating loss requires §172 analysis, including the 80% taxable income limitation and tracking for future years. The base catalogue refusal R-US-NOL applies. Please consult a CPA or Enrolled Agent with NOL experience."

(Note: this overlaps with R-US-NOL in the base; the skill defers to the base refusal and flags it explicitly.)

**R-BOOK-SECTION-179-IMPACT — §179 election approaching the income limitation.**
Trigger: The taxpayer's §179 election would approach or exceed the active trade or business income limitation, requiring careful coordination with bonus depreciation and timing decisions.
Output: "The §179 deduction is limited to taxable income from the active conduct of a trade or business. When the proposed §179 election approaches this limit, the choice between §179 and bonus depreciation becomes a planning question that affects multiple years. The skill captures the asset details and surfaces both §179 and bonus depreciation options, but the elections are made by the reviewer."

(Note: this is a flag, not a hard refusal — the skill captures the asset and presents options.)

---

## Section 10 — Reviewer attention thresholds

Dollar thresholds at which a position becomes a reviewer attention flag regardless of certainty. The reviewer reads attention flags top-down by dollar magnitude and stops when confident.

| Threshold | Trigger | Rationale |
|---|---|---|
| Single transaction ≥ $5,000 | Always flag, regardless of category | Material item; reviewer should verify substantiation |
| Single line item total ≥ $25,000 | Always flag, regardless of category | Material to overall return |
| Vehicle deduction (Line 9) ≥ $10,000 total | Always flag | Vehicle is a high-audit area |
| Home office deduction ≥ $3,000 (actual method) or any (simplified) | Always flag | Home office is a high-audit area |
| Meals (Line 24b) ≥ $5,000 | Always flag | Substantiation risk |
| Travel (Line 24a) ≥ $10,000 | Always flag | Substantiation risk |
| §179 election ≥ $50,000 | Always flag | Election affects multiple years |
| Bonus depreciation (any amount with acquisition date within 30 days of Jan 19, 2025) | Always flag | OBBBA cutoff sensitivity |
| Single contractor paid ≥ $10,000 (Line 11) | Always flag | Worker classification risk + 1099 obligation |
| Any Tier 2 default applied with cash impact ≥ $1,000 | Always flag | Material conservative position |
| Any §274(d) item with documentation gap ≥ $500 | Always flag | Substantiation risk |
| Any expense with personal-business split ≥ $2,000 | Always flag | Allocation risk |
| Schedule C net loss ≥ $10,000 | Always flag | Hobby loss / NOL exposure |
| Any expense in a refusal-flagged category that the skill didn't refuse | Always flag | Boundary check |

These thresholds are the floor — content skills may flag below these thresholds for category-specific reasons, but anything at or above always gets a flag.

---

## Section 11 — Worked examples

Six fully worked classification examples drawn from a hypothetical client (not from any real test data). Each shows input → reasoning with citations → output.

**Hypothetical client:** Maria Hernandez, freelance UX designer, single, sole proprietor (no LLC), based in Austin TX, calendar year 2025, no employees, no inventory, cash method, has a dedicated home office, uses her personal car for client meetings, has one significant equipment purchase in March 2025.

### Example 1 — Adobe Creative Cloud subscription

**Input:** "ADOBE *CC ALL APPS 03/15/2025 $59.99"

**Reasoning:**
- Adobe Creative Cloud is a productivity / design software subscription used in Maria's UX design business
- Ordinary and necessary for a UX designer (IRC §162(a))
- Recurring SaaS subscription, not a capital item
- Could fit Line 18 (office expense) or Line 27b (other expenses with description)
- Skill default: Line 27b "Software subscriptions — Adobe Creative Cloud" because it's industry-specific design software, not generic productivity

**Output:**
- Line: 27b (Other expenses, Part V description "Software subscriptions — Adobe Creative Cloud")
- Amount: $59.99
- Citation: IRC §162(a); Schedule C Instructions (2025) Part V
- Default applied: No
- Reviewer attention: No (below $5,000 threshold)

### Example 2 — Home Depot purchase: $1,847 standing desk

**Input:** "HOME DEPOT #6543 03/22/2025 $1,847.00"

**Reasoning:**
- A standing desk for the home office
- Tangible personal property with useful life > 1 year — would normally be capitalized under §263
- BUT: The cost ($1,847) is below the de minimis safe harbor threshold for taxpayers without applicable financial statements ($2,500 per item under Treas. Reg. §1.263(a)-1(f)(1)(ii)(D))
- Maria does not have AFS (sole prop with no audited financials)
- ASSUME the de minimis safe harbor election is made on the 2025 return (it's an annual election)
- If elected, the desk is expensed immediately rather than capitalized
- Where does it go? Office equipment used in the trade or business — Line 18 (office expense) is reasonable; Line 22 (supplies) less so since a standing desk is durable

**Output:**
- Line: 18 (Office expense) — assuming de minimis safe harbor election
- Amount: $1,847
- Citation: Treas. Reg. §1.263(a)-1(f)(1)(ii)(D); Schedule C Instructions (2025) line 18
- Default applied: Yes — assumed de minimis safe harbor election; flag for reviewer to confirm the election will be made on the return and that a written accounting policy was in place at the start of 2025
- Reviewer attention: Yes — single item over $1,000 and election confirmation needed

### Example 3 — Uber ride home from a client meeting at 8 PM

**Input:** "UBER 04/03/2025 $34.50"

**Reasoning:**
- Local transportation, not overnight travel — so it's NOT Line 24a (Travel)
- Could be Line 9 (Car and truck expenses) if Maria's standard car expense methodology covers this
- BUT Maria uses her personal car with the standard mileage method on Line 9. The standard mileage rate covers her own vehicle costs, not third-party transportation
- A business-purpose Uber to/from a client meeting is Line 24a-equivalent local transportation — but local transportation doesn't have its own line
- IRS practice: local business transportation that isn't overnight travel goes on Line 24a (Travel) per Pub 463 (the term "travel" in the §162 sense includes local business transportation)
- Alternative classification: Line 27b "Other expenses — Local business transportation"
- Skill default: Line 24a, with the understanding that "travel" here is local

**Output:**
- Line: 24a (Travel)
- Amount: $34.50
- Citation: IRC §162; Pub 463 (2025); Schedule C Instructions (2025) line 24a
- Default applied: No
- Reviewer attention: No
- Substantiation note: Per §274(d), the business purpose must be documented (which client, what meeting, what business reason). The receipt alone is insufficient. Flag if no contemporaneous record exists.

### Example 4 — March 2025 MacBook Pro purchase, $3,499

**Input:** "APPLE.COM/BILL 03/28/2025 $3,499.00 — MacBook Pro 16-inch"

**Reasoning:**
- Tangible personal property, useful life > 1 year
- Cost ($3,499) exceeds the de minimis safe harbor for taxpayers without AFS ($2,500)
- Therefore must be capitalized (Line 13) rather than expensed
- Computer is listed property under §280F(d)(4) historically; however, computers used exclusively at a regular business establishment (which a qualifying home office is) are NOT listed property under §280F(d)(4)(B)(i). Maria has a qualifying home office. Confirm exclusive business use.
- Acquisition date: March 28, 2025 — AFTER January 19, 2025 — so 100% bonus depreciation under OBBBA is available
- Recovery period: 5 years (computers and peripheral equipment under MACRS GDS)
- Eligible for §179 expensing (well under $2.5M cap), bonus depreciation (100% post-Jan 19), or regular MACRS
- Skill captures the asset and presents options; reviewer chooses the elections

**Output:**
- Line: 13 (Depreciation and §179 expense, via Form 4562)
- Amount: $3,499 (cost basis)
- Citation: IRC §168(k) as amended by OBBBA; IRC §179; IRC §280F(d)(4)(B)(i); Pub 946 (2025); Form 4562 Instructions (2025)
- Asset details captured for Form 4562: description (MacBook Pro 16"), date placed in service (assume March 28, 2025), cost basis ($3,499), recovery period (5 years), business-use percentage (assume 100% — confirm with reviewer that the computer is used exclusively in the qualifying home office)
- Available treatments:
  1. §179 expensing: Full $3,499 (well under $2.5M cap, and assuming Maria has at least $3,499 of taxable business income)
  2. 100% bonus depreciation: Full $3,499 (acquired after Jan 19, 2025; OBBBA)
  3. Regular MACRS: 5-year property, half-year convention, ~$700 first year
- Default for the working paper: capture the asset, surface the §179 / bonus options, flag for reviewer election
- Reviewer attention: Yes — election decision required; confirm exclusive business use

### Example 5 — Lunch with a prospective client at a restaurant

**Input:** "FRANKLIN BBQ 04/12/2025 $87.50"

**Reasoning:**
- Business meal at a restaurant
- §274(n)(1): 50% deductible
- IMPORTANT: Restaurant meals in 2025 are 50%, NOT 100%. The temporary 100% restaurant meal rule under CAA 2021 §210 expired after December 31, 2022 and has not been reinstated. OBBBA does not contain a 100% restaurant meal provision.
- §274(d) substantiation required: amount, date, place, business purpose, business relationship of attendees
- Maria must document who she met with and what business was discussed. The receipt alone is insufficient.

**Output:**
- Line: 24b (Meals subject to 50% limit)
- Amount entered: $87.50 (gross); the 50% reduction is applied at the form level, not at the transaction level — Line 24b shows the gross meal cost and the form mechanically applies the 50%
- Citation: IRC §274(n)(1); IRC §274(d); Treas. Reg. §1.274-12; Pub 463 (2025); Schedule C Instructions (2025) line 24b
- Default applied: No (assuming Maria provides substantiation)
- Reviewer attention: Flag for §274(d) substantiation confirmation — ask Maria for the prospect's name and the business discussed
- Substantiation status: Pending — flag for documentation collection

### Example 6 — A $4,200 round-trip flight to a UX conference in San Francisco, plus $850 hotel

**Input:**
- "DELTA AIR LINES 05/15/2025 $4,200.00"
- "MARRIOTT UNION SQ 05/18/2025 $850.00"

**Reasoning:**
- Both travel-related expenses for a business trip
- Conference in San Francisco — clearly business purpose if the conference is industry-relevant (UX design conference would be ordinary and necessary for Maria)
- Travel away from tax home (Austin) overnight
- Line 24a (Travel) for both
- §274(d) substantiation required: confirm the conference name, dates, business purpose
- Note: The $4,200 airfare is unusually high for a domestic round-trip from Austin to SFO. Flag — could be first/business class. First/business class is generally deductible if the taxpayer chooses it, but the high amount triggers the reviewer attention threshold.
- Note: Conference registration fee is separate from these line items — would be Line 27b "Conference fees" or Line 24a depending on practitioner preference; skill defaults to 24a if it's bundled with travel, otherwise 27b.

**Output:**
- Line: 24a (Travel) for both items
- Amount: $4,200 (flight) + $850 (hotel) = $5,050 total
- Citation: IRC §162; IRC §274(d); Pub 463 (2025); Schedule C Instructions (2025) line 24a
- Default applied: No
- Reviewer attention: Yes — total over $5,000 single-transaction threshold AND vehicle-class flag for the high airfare; AND §274(d) substantiation confirmation needed (conference name, dates, business purpose, attendance proof)

---

## Section 12 — Output format extensions

In addition to the base reviewer brief template (Section 3 of `us-tax-workflow-base`), this skill produces:

### Extension 1 — The classified transaction working paper (Excel)

A workbook with the following structure:

**Sheet "Transactions"** — one row per source transaction:

| Column | Content |
|---|---|
| A | Date |
| B | Payee / counterparty |
| C | Description (from source data) |
| D | Amount (gross) |
| E | Schedule C line (8 / 9 / 10 / ... / 27b / 33-42 for COGS / Excluded) |
| F | Part V description (if line is 27b) |
| G | Treatment label (e.g., "Office expense", "Vehicle - actual", "Capital - Form 4562") |
| H | Citation (IRC section / Reg / Pub) |
| I | Default applied? Y/N |
| J | Default reason if Y |
| K | Reviewer attention flag? Y/N |
| L | Reviewer attention reason if Y |
| M | §274(d) item? Y/N |
| N | Substantiation status (documented / pending / missing) |
| O | Excluded? Reason if yes |

**Sheet "Schedule C Summary"** — one row per Schedule C line, with the total via `=SUMIFS()` referencing Sheet "Transactions" column E.

**Sheet "Form 4562 Detail"** — for any capital items, listing description, date placed in service, cost basis, recovery period, business-use percentage, §179 election (if applicable), bonus depreciation (if applicable), method.

**Sheet "Form 8829 Detail"** — for home office expenses if the actual method is used: total home expenses by category, business-use percentage, allocated business amount.

**Sheet "Downstream Items"** (NEW in v0.2) — for transactions that are clearly business-related but belong to a downstream content skill's scope, not Schedule C. These are NOT excluded transactions (those go to the Excluded category in Sheet "Transactions"). They are handed off to the next skill in the stack with the recommended target line and the responsible skill named.

| Column | Content |
|---|---|
| A | Date |
| B | Payee / counterparty |
| C | Description |
| D | Amount |
| E | Recommended target form/line (e.g., "Schedule 1 Line 16", "Schedule 1 Line 17", "Form 8606", "Form 1040 Line 25c") |
| F | Responsible downstream skill (e.g., "us-form-1040-self-employed-positions", "us-quarterly-estimated-tax") |
| G | Brief note for the reviewer |

Common downstream items that go to this sheet, not to Schedule C:

- **Owner SEP-IRA, Solo 401(k), traditional IRA, Roth IRA contributions** → Schedule 1 Line 16 (deductible self-employed retirement contributions) or Form 8606 (nondeductible IRA basis tracking). Owned by `us-form-1040-self-employed-positions`. Never on Line 19 of Schedule C (Line 19 is employee plans only).
- **Owner self-employed health insurance premiums** (BCBS, ACA marketplace, COBRA, private insurer, dental, vision, long-term care if eligible) → Schedule 1 Line 17. Owned by `us-form-1040-self-employed-positions`. Never on Line 14 (employee benefits) or Line 15 (insurance other than health) of Schedule C.
- **Federal income tax payments** (estimated tax, prior-year balance due, extension payments) → Form 1040 Line 25c (estimated payments) or Line 31 (extension payment). Owned by `us-quarterly-estimated-tax` for 2025 estimateds; the prior-year balance due is a Form 1040 prior-year reconciliation item handled by the reviewer. Never deductible on any Schedule C line.
- **Federal self-employment tax payments** (already accounted for via Schedule SE; no separate line on Schedule C). Half of SE tax is a Schedule 1 Line 15 deduction owned by `us-schedule-c-and-se-computation`.
- **HSA contributions** (if the owner has an HSA-eligible high-deductible health plan) → Schedule 1 Line 13. Owned by `us-form-1040-self-employed-positions`.
- **Student loan interest payments** → Schedule 1 Line 21. Owned by the personal-side reviewer.
- **OBBBA-specific personal deductions** (qualified tips, qualified overtime, auto loan interest under the new OBBBA provision, additional senior deduction) → Schedule 1-A. Owned by `us-form-1040-self-employed-positions`.
- **Charitable contributions** → Schedule A (if itemizing) or no deduction (if taking standard deduction). Owned by the personal-side reviewer. Sponsorship that is genuinely promotional may be Line 8 advertising, not charitable — the test is whether the taxpayer received valuable advertising in return.

The Downstream Items sheet is required whenever any such transaction appears in the source data, even if the engagement scope (per the workflow base Section 4 intake) is Schedule C and SE only. The reviewer needs to know what was identified-but-deferred so the personal-side return is complete.

**Color conventions** (per the xlsx skill):
- Blue text: hardcoded inputs from source data
- Black text: formulas
- Green text: cross-sheet references
- Yellow background: rows with default applied OR reviewer attention flag

**File location:** `/mnt/user-data/outputs/<taxpayer-identifier>-schedule-c-2025-working-paper.xlsx`

**After building the workbook:** Run `python /mnt/skills/public/xlsx/scripts/recalc.py <filename>` to recalculate and check for errors. Verify zero formula errors before presenting via `present_files`.

### Extension 2 — Schedule C line summary in the reviewer brief

In addition to the base brief template, the reviewer brief for this skill includes a "Schedule C line summary" section:

```markdown
## Schedule C line summary

| Line | Description | Amount | Notes |
|---|---|---|---|
| 1 | Gross receipts | $X | |
| 2 | Returns and allowances | $X | |
| ... | ... | ... | ... |
| 28 | Total expenses (lines 8-27b) | $X | |
| 29 | Tentative profit | $X | |
| 30 | Home office (from Form 8829 or simplified) | $X | |
| 31 | Net profit (or loss) | $X | (DEFERRED — handled by Schedule C/SE skill) |

## Capital items captured for Form 4562

[List of capital items with cost basis, acquisition date, recovery period, and pending elections]

## §274(d) substantiation status

[List of items requiring substantiation, current status, and what's needed from the taxpayer]

## Excluded transactions

[List of all transactions excluded with reasons — personal expenses, owner draws, transfers, fines, etc.]

## Downstream items deferred to companion skills (NEW in v0.2)

[List of all transactions captured on Sheet "Downstream Items" with target form/line and responsible skill. Each entry: date, payee, amount, target line, responsible skill, brief note. Grouped by responsible skill.]

This section exists so the reviewer can see at a glance which downstream items were identified by the bookkeeping skill but deferred to other skills. If the engagement scope includes those skills, the reviewer can confirm they were also run. If the engagement scope does not include them, the reviewer knows what additional work the personal-side return requires.
```

---

## Section 13 — Intake form additions

Per slot 18 of the base intake form (Section 4 of `us-tax-workflow-base`), this skill adds the following questions to the standard intake. Ask only those not already answered by Step 3 inference:

**Bookkeeping-specific intake (slot 18 additions):**

18a. **Home office:** Do you have a dedicated home office used regularly and exclusively for business? If yes:
- Approximate square footage of the office
- Approximate total square footage of the home
- Did you use the simplified method or actual method last year? (Affects this year's election flexibility)

18b. **Vehicle:** Did you use a personal vehicle for business in 2025? If yes:
- Make, model, and year
- Date you started using it for business
- For 2025, do you have a contemporaneous mileage log? (Yes / Partial / No)
- Estimated business miles in 2025
- Estimated total miles in 2025
- Did you use the standard mileage method or actual method in the FIRST year you used this vehicle for business?

18c. **Capital purchases:** Did you purchase any equipment, computers, furniture, or other business property over $2,500 in 2025? If yes, list them with approximate dates and costs. (The Jan 19, 2025 OBBBA cutoff matters for bonus depreciation.)

18d. **De minimis safe harbor:** Do you have a written accounting policy electing the de minimis safe harbor under Treas. Reg. §1.263(a)-1(f)? If you don't know what this means, the answer is probably no.

18e. **Inventory:** Does your business carry inventory? If yes, what kind, and what was your beginning and ending inventory value for 2025?

18f. **Contractors:** Did you pay any individual contractor or unincorporated business $600 or more in 2025? If yes, did you collect a W-9 from each one before paying? (1099-NEC obligation.)

18g. **Business gifts:** Did you give any business gifts (to clients, prospects, referral sources) in 2025? Total approximate value? (§274(b)(1) $25 per recipient limit.)

18h. **Travel:** How many business trips away from your tax home overnight in 2025? Approximate total travel cost? Do you have receipts and a contemporaneous record of business purpose for each trip?

18i. **Meals:** Approximate total business meal spend in 2025? Do you have records of who you met with and what business was discussed for each meal? (§274(d) substantiation.)

18j. **Personal vs business cards:** Did you use a dedicated business credit card for business expenses, or did you mix business and personal on a single card? (Affects classification rigor.)

18k. **Prior-year carryovers:** Are there any depreciation carryovers, §179 carryovers, home office carryovers, or other carryforwards from prior years? If yes, attach the prior-year Form 4562 / Form 8829 / Schedule C.

18l. **Hobby loss exposure:** Has the business shown a profit in at least 3 of the last 5 years? (§183 presumption.)

---

## Section 14 — Self-check additions

In addition to the 15 base self-checks (Section 5 of `us-tax-workflow-base`), this skill adds:

**Check 16 — Schedule C line completeness.** The Schedule C line summary in the brief covers every line where a transaction was classified. Lines with no transactions show $0. The total of lines 8-27b equals the value on Line 28. The math is correct.

**Check 17 — Capital vs current consistency.** Every transaction over the de minimis safe harbor threshold ($2,500 without AFS, $5,000 with AFS) is either (a) capitalized to Line 13 with Form 4562 detail, or (b) flagged with a documented reason for current expensing (e.g., routine maintenance safe harbor, small taxpayer building safe harbor, or expense category that is by nature not capitalizable).

**Check 18 — §274(d) substantiation flagged.** Every transaction in a §274(d) category (travel, meals, gifts, listed property) has a substantiation status (documented / pending / missing) in column N of the working paper. None is silently absent.

**Check 19 — Vehicle method consistency.** If vehicle expenses appear on Line 9, the method (standard mileage or actual) is stated explicitly in the brief and applied consistently across all vehicle transactions. The first-year election rule is checked against any prior-year information available.

**Check 20 — Home office method consistency.** If a home office deduction is taken, exactly one method is used (simplified OR actual, never both for the same year). The deduction amount is computed correctly per the chosen method. If actual method, Form 8829 detail is captured.

**Check 21 — Acquisition date for OBBBA cutoff.** Every capital asset on Form 4562 has an acquisition date stated. Assets within 30 days of January 19, 2025 are flagged for reviewer verification of the precise acquisition date.

**Check 22 — Personal vs business consistency.** No transaction with personal-use elements appears in expenses without an allocation, OR the conservative default of 0% business use was applied and flagged.

**Check 23 — Refusal trace includes topical refusals.** The refusal trace in the brief lists every R-BOOK-XXX code from this skill in addition to the base R-US-XXX codes, with cleared/fired status.

**Check 24 — No 100% restaurant meals.** No transaction in Line 24b is treated as 100% deductible. All meal deductions are at 50% per §274(n)(1). (Defensive check against the common misconception that the 2021-2022 100% rule still applies.)

**Check 25 — No "Schedule 1-A" items on Schedule C.** New OBBBA personal deductions (qualified tips deduction, qualified overtime deduction, auto loan interest deduction, senior deduction) do not appear on Schedule C. They flow through the personal return via Schedule 1-A or its successor form per current 2025 instructions, handled by the companion skill `us-form-1040-self-employed-positions`.

---

## Section 15 — Cross-skill references

This skill produces outputs consumed by other content skills in the US tax stack:

**Output → `us-schedule-c-and-se-computation`:**
- The Schedule C line summary (lines 1 through 27b totals) feeds the Schedule C aggregation
- The home office deduction (Line 30) feeds the net profit computation
- The net profit on Line 31 is computed by the downstream skill, not here
- The net profit feeds Schedule SE for self-employment tax

**Output → `us-form-1040-self-employed-positions`:**
- The QBI deduction is computed downstream from Schedule C net profit
- Self-employed health insurance deduction is computed downstream (the skill flags any health insurance premium identified in the source data but does not compute the deduction)
- Retirement contribution computations happen downstream
- The new OBBBA personal deductions (tips, overtime, auto loan interest, senior) are entirely downstream

**Output → `us-quarterly-estimated-tax`:**
- The current-year Schedule C net profit (computed by the C/SE skill) feeds the current-year tax projection
- Prior-year tax (from the prior-year return) is needed for safe harbor

**Inputs from other skills:**
- This skill does not consume outputs from other content skills. It is upstream.

---

## Section 16 — Reference material

### Validation status

This file is v0.1 of `us-sole-prop-bookkeeping`, drafted in April 2026 as the first content skill on top of `us-tax-workflow-base` v0.1. Year-specific figures are verified against primary IRS sources (Publication 587, Notice 2025-5, Rev. Proc. 2024-40, Rev. Proc. 2025-16, Notice 2024-80, OBBBA P.L. 119-21 and IRS guidance summaries on irs.gov) as of April 2026.

### Origin

Drafted from a structured framework derived from a deep research report on Schedule C classification for tax year 2025, with year-specific figures and OBBBA provisions independently verified via direct primary source review on irs.gov and Big 4 / professional firm summaries. Where the deep research report contradicted primary sources (notably on the simplified home office rate and the restaurant meals deductibility), this skill follows the primary sources, not the report.

### Known gaps

1. The OBBBA implementing guidance was still being issued by Treasury and the IRS through late 2025 and into 2026. Some specific positions (notably around the §168(k) acquisition date determination, the §471(c) interaction with §263A, and the new tip/overtime reporting mechanisms) may be refined by guidance issued after this skill's currency date. The skill's citation discipline ensures positions are tied to identifiable sources, so updates can be applied surgically.
2. The skill does not optimize between §179 and bonus depreciation — it captures assets and surfaces both options for reviewer election. A future v0.2 could add optimization heuristics, but the reviewer is the decision-maker by design.
3. Worker classification (employee vs independent contractor) is flagged but not adjudicated. A future v0.2 could add the IRS 20-factor analysis or the more recent common law test, but the v0.1 position is to refer this question to the reviewer because the consequences are large and the analysis is fact-intensive.
4. The hobby loss flag uses the §183(d) presumption test only (3 of 5 years) and does not apply the nine-factor test of Reg. §1.183-2(b). Reviewer makes the call on borderline cases.
5. The Schedule 1-A reference for OBBBA personal deductions assumes the form name as commonly referenced in late 2025; the actual form name and line numbers should be confirmed against the final 2025 Form 1040 instructions when available.
6. The skill is silent on Section 199A aggregation for taxpayers with multiple businesses. This is handled in `us-form-1040-self-employed-positions`.
7. The de minimis safe harbor assumes the election is made; the skill does not verify that a written accounting policy was in place at the start of the year, which is a technical requirement. Reviewer must confirm.
8. The skill does not handle changes in accounting method (Form 3115). If a method change is needed, the engagement should be referred to a CPA with method change experience.

### Change log

- **v0.1 (April 2026):** Initial draft. Tax year 2025. Built on `us-tax-workflow-base` v0.1. Reflects OBBBA P.L. 119-21 as enacted July 4, 2025, and IRS implementing guidance available through April 2026.

### Self-check (v0.1 of this document, not the runtime self-check in Section 14)

1. Loads on top of `us-tax-workflow-base`: yes (stated in Section "What this file is").
2. Year-specific figures table provided: yes (Section 3).
3. Primary source library provided: yes (Section 4).
4. Position rules for every Schedule C line: yes (Section 6).
5. Conservative defaults table: yes (Section 8).
6. Topical refusal catalogue: yes (Section 9).
7. Reviewer attention thresholds: yes (Section 10).
8. Worked examples (minimum 5, hypothetical client): yes (Section 11, six examples drawn from hypothetical client Maria Hernandez).
9. Output format extensions: yes (Section 12).
10. Intake form additions: yes (Section 13).
11. Self-check additions: yes (Section 14).
12. Cross-skill references: yes (Section 15).
13. Reference material: yes (Section 16).
14. Citation discipline: every position rule cites a primary source. Verified.
15. OBBBA changes reflected: yes (§168(k) cutoff, §179 limits, QBI permanence, new personal deductions deferred to companion skill).
16. Simplified home office rate is correct ($5/sqft, $1,500 max), NOT the $6/sqft figure that appeared in some 2025 commentary. Verified directly from Pub 587 (2025).
17. Restaurant meals are 50%, not 100%. Verified — no 2025 legislation reinstated the 2021-2022 temporary rule.
18. §471(c) threshold is $31M for 2025. Verified.

## End of US Sole Prop Bookkeeping Skill v0.1

This skill is incomplete without `us-tax-workflow-base` v0.1 or later loaded alongside it. If you are reading this without the base loaded, ask the user to load it before proceeding.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
