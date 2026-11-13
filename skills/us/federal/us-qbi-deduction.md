---
name: us-qbi-deduction
description: Compute the 2026 section 199A qualified business income (QBI) deduction for a US sole proprietor or single-member LLC disregarded for federal tax, on Form 8995 or Form 8995-A. The rate stays 20% (the One Big Beautiful Bill Act did not adopt 23%). 2026 figures from Rev. Proc. 2025-32 and Public Law 119-21 section 70105, with thresholds of $201,750 (single and head of household), $201,775 (married filing separately) and $403,500 (joint), phase-in ranges widened to $75,000 and $150,000, and the new $400 minimum deduction for at least $1,000 of QBI from a business the taxpayer materially participates in. Covers QBI after the deductible half of self-employment tax, self-employed health insurance and retirement contributions, the specified service trade or business (SSTB) rules and de minimis test, the W-2 wage and UBIA limit, the phase-in, the 20% of taxable income cap and loss carryforwards. Trigger on "QBI", "199A", "pass-through deduction", "Form 8995", "Form 8995-A", "SSTB", "20% deduction". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US qualified business income deduction (section 199A), tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 199A, Public Law 119-21 section 70105 (the One Big Beautiful Bill Act), Rev. Proc. 2025-32, Treas. Reg. 1.199A-1, 1.199A-2, 1.199A-3 and 1.199A-5 (eCFR), and the 2026 draft Forms 8995 and 8995-A and draft Instructions for Form 8995, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 the deduction is **20%** of qualified business income, never 23%. The final One Big Beautiful Bill Act (Public Law 119-21, section 70105) kept the 20% rate, removed the end-2025 expiry, widened the phase-in ranges to **USD 75,000** (USD 150,000 joint) and added a **USD 400** minimum deduction for a taxpayer with at least **USD 1,000** of QBI from businesses they materially participate in. At or below taxable income of **USD 201,750** (single, head of household), **USD 201,775** (married filing separately) or **USD 403,500** (joint), the deduction is 20% of QBI, capped at 20% of taxable income less net capital gain, whatever the business is. Above that, a specified service business (law, health, accounting, consulting, financial services and the rest) phases out, and every business meets the W-2 wage and property limit, both fully by **USD 276,750**, **USD 276,775** or **USD 553,500**. A specified service business just above the threshold still gets a partial deduction (see Case 1).

## Scope and who this is for

In scope: one individual (or a married couple filing jointly) with QBI from one or more Schedules C for tax year 2026: a sole proprietorship or a single-member LLC treated as disregarded. The skill works out QBI, the threshold position, SSTB status, the W-2 wage and UBIA limit, the phase-in, the taxable income cap and the minimum deduction, and fills Form 8995 or Form 8995-A. The result goes on Form 1040, line 13a (2026 draft instructions).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Classifying transactions into Schedule C lines | `us-sole-prop-bookkeeping` |
| Schedule C net profit, self-employment tax and its deductible half | `us-schedule-c-and-se-computation` |
| Self-employed health insurance deduction (section 162(l)) | `us-self-employed-health-insurance` |
| SEP, SIMPLE and solo 401(k) contributions and their limits | `us-self-employed-retirement` |
| Standard deduction and the rest of taxable income | `us-federal-income-tax-return-1040` |
| No tax on tips (section 224) and the other 2026 changes | `us-2026-federal-tax-changes` |
| Whether to elect S corporation status to create W-2 wages | `us-s-corp-election-decision` |
| Rental real estate as a trade or business, material participation | `us-real-estate-professional-and-short-term-rentals` |
| QBI from partnerships and S corporations (Schedule K-1) | `us-form-1065-partnership`; refer (R-QBI-K1) |
| Paying the tax during the year | `us-quarterly-estimated-tax` |
| Putting the return together | `us-federal-return-assembly` |
| State QBI conformity or add-backs | the state's income tax skill (for California, `us-ca-return-assembly`) |

This skill loads on top of `us-tax-workflow-base`.

## Ask the client first

1. **Filing status for 2026.** It sets the threshold and phase-in range. Married filing separately has its own threshold (USD 201,775), not half the joint one.
2. **What the business does, in the client's words**, with a split of 2026 gross receipts by type of work if it does more than one thing (advice against deliverables, services against product sales). This decides SSTB status and the de minimis test.
3. **Did the client materially participate** in each business in 2026 (section 469(h), for example more than 500 hours)? Only then does its QBI count toward the USD 1,000 needed for the USD 400 minimum.
4. **Employees.** Did the business pay common-law employees on Forms W-2 in 2026? The total of the section 6051(a)(3) and (8) amounts for those employees, and whether the Forms W-2 were filed with the Social Security Administration on time. The owner's own draw is never W-2 wages.
5. **Depreciable property** still in use at 31 December 2026: each item's cost and placed-in-service date (Form 4562 and the asset register). Fully expensed items still count.
6. **Prior-year carryforwards:** the 2025 Form 8995 line 16 or Form 8995-A Schedule C qualified business loss carryforward, and any REIT or PTP loss carryforward.
7. **Upstream figures:** Schedule C line 31 for each business, the deductible half of self-employment tax, the self-employed health insurance deduction and the retirement plan deduction, each from its own skill.
8. **Other income:** net capital gain and qualified dividends (they reduce the cap), W-2 wages from a job, and whether the client was an employee of the same customer in the last three years.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Deduction rate on QBI | 20% (the 23% in the House-passed bill was not enacted) | [26 U.S.C. 199A(b)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm); [Public Law 119-21, section 70105](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Overall cap | 20% of (taxable income before the QBI deduction minus net capital gain, with qualified dividends added to net capital gain) | [26 U.S.C. 199A(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm); [Form 8995 (2026 draft), lines 11 to 14](https://www.irs.gov/pub/irs-dft/f8995--dft.pdf) |
| Threshold amount, all other returns (single, head of household, qualifying surviving spouse) | USD 201,750 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Threshold amount, married filing separately | USD 201,775 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Threshold amount, married filing jointly | USD 403,500 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| End of phase-in range, all other returns | USD 276,750 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| End of phase-in range, married filing separately | USD 276,775 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| End of phase-in range, married filing jointly | USD 553,500 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-in range width, every return except joint (was USD 50,000 to 2025) | USD 75,000 | [Public Law 119-21, section 70105(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Phase-in range width, joint return (was USD 100,000 to 2025) | USD 150,000 | [Public Law 119-21, section 70105(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Wage limit, first alternative | 50% of W-2 wages | [26 U.S.C. 199A(b)(2)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| Wage limit, second alternative | 25% of W-2 wages plus 2.5% of UBIA of qualified property | [26 U.S.C. 199A(b)(2)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| Depreciable period for UBIA | later of 10 years from placed in service or the last full year of the section 168 recovery period (ignoring 168(g)) | [26 U.S.C. 199A(b)(6)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| W-2 wages count only if filed with SSA within | 60 days after the due date (with extensions) | [26 U.S.C. 199A(b)(4)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| Minimum deduction, taxable years beginning after 31 December 2025 | USD 400 | [Rev. Proc. 2025-32, section 2.12](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Public Law 119-21, section 70105(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| QBI needed for the minimum, from active businesses (material participation, section 469(h)) | USD 1,000 | [Rev. Proc. 2025-32, section 2.12](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Public Law 119-21, section 70105(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| SSTB de minimis, gross receipts USD 25 million or less | not an SSTB if under 10% of gross receipts are from the specified service | [Treas. Reg. 1.199A-5(c)(1)(i)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-5) |
| SSTB de minimis, gross receipts over USD 25 million | under 5% | [Treas. Reg. 1.199A-5(c)(1)(ii)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-5) |
| Former employee presumed still an employee for the same services | 3 years | [Treas. Reg. 1.199A-5(d)(3)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-5) |

The rate, the 50%, 25% and 2.5% factors and the phase-in widths are statutory and not indexed. The thresholds are indexed every year. The USD 400 and USD 1,000 are indexed only for taxable years beginning after 2026, in multiples of USD 5 (Public Law 119-21, section 70105(b), new section 199A(i)(3)).

### Step 1: qualified business income for each business

QBI is the net amount of qualified items of income, gain, deduction and loss from the trade or business, included in taxable income for 2026 (section 199A(c)(1), (c)(3)). For a sole proprietor:

**QBI = Schedule C line 31 minus the deductible half of self-employment tax (Schedule 1) minus the self-employed health insurance deduction minus the deduction for contributions to SEP, SIMPLE or solo 401(k) plans for the owner.**

The three subtractions are required: Treas. Reg. 1.199A-3(b)(1)(vi) treats the section 164(f), 162(l) and 404 deductions as attributable to the business to the extent the business's gross income was used to work them out, in proportion where there are several businesses. The Form 8995 instructions repeat it. If the client has two Schedules C, split each of the three deductions between them in proportion to the income each contributed.

Not in QBI:

- Capital gains and losses (including section 1231 gain treated as capital), dividends, interest not properly allocable to the business, and annuities not received in connection with the business (section 199A(c)(3)(B)).
- Wages as an employee (except a statutory employee, Form W-2 box 13 checked), and the owner's own draw (section 199A(c)(4), (d)(1)(B)).
- From 2026, any tip amount deductible under section 224(a), and section 224 tip income excluded from the business's net profit (2026 draft Instructions for Form 8995). The tip deduction itself is in `us-2026-federal-tax-changes`.
- Losses and deductions suspended in 2026 by other rules (sections 163(j), 179, 461(l), 465 and 469); they enter QBI in the year they are allowed (2026 draft Instructions for Form 8995).
- A traditional IRA deduction (section 219), Roth contributions, the standard or itemized deductions, estimated tax payments and the QBI deduction itself.

### Step 2: taxable income before the QBI deduction

Taxable income for every section 199A test is computed without the QBI deduction (section 199A(e)(1)). Use Form 1040 line 11a (adjusted gross income) minus the standard or itemized deduction and the other deductions the 2026 draft Form 8995 instructions list for line 11; the standard deduction amounts are in `us-federal-income-tax-return-1040`. Because the QBI deduction is left out, there is no loop: work out the self-employment tax, health insurance and retirement deductions first (they depend on net earnings from self-employment, not on QBI), then QBI, then taxable income, then the deduction, once.

### Step 3: where taxable income sits

| Taxable income before the QBI deduction | What applies | Form |
| --- | --- | --- |
| At or below the threshold (USD 201,750 / 201,775 / 403,500) | 20% of QBI for every business, SSTB or not; no wage or UBIA limit | Form 8995 (unless a cooperative patron) |
| Above the threshold, up to the end of the range (USD 276,750 / 276,775 / 553,500) | SSTB items cut to the applicable percentage; wage and UBIA limit phased in | Form 8995-A with Part III, and Schedule A for an SSTB |
| Above the end of the range | SSTB: no deduction. Other businesses: the smaller of 20% of QBI and the wage and UBIA limit | Form 8995-A |

The phase-in fraction is (taxable income minus the threshold) divided by USD 75,000 (USD 150,000 joint) (Form 8995-A (2026 draft), lines 20 to 24). The applicable percentage for an SSTB is 100% minus that fraction, not below zero (section 199A(d)(3)(B)).

### Step 4: SSTB status

A specified service trade or business is one involving services in health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage services, investing and investment management, trading, or dealing in securities, partnership interests or commodities, or one whose principal asset is the reputation or skill of its employees or owners (section 199A(d)(2), which takes the section 1202(e)(3)(A) list without "engineering, architecture"). Treas. Reg. 1.199A-5(b) defines each field narrowly:

| Activity | SSTB? | Reason |
| --- | --- | --- |
| Physician, dentist, nurse, pharmacist, physical therapist, psychologist, veterinarian | Yes | Health, 1.199A-5(b)(2)(ii) |
| Health club, spa, payment processing, selling drugs or medical devices | No | Excluded from health, 1.199A-5(b)(2)(ii) |
| Lawyer | Yes | Law |
| Accountant, enrolled agent, return preparer, financial auditor | Yes | Accounting, 1.199A-5(b)(2)(iv) |
| Bookkeeper | Not named in the regulation; treat as accounting (conservative) and flag | "similar professionals", 1.199A-5(b)(2)(iv) |
| Financial adviser, wealth or retirement planner, valuations and M&A advice | Yes | Financial services, 1.199A-5(b)(2)(ix) |
| Taking deposits or making loans | No | Excluded from financial services, 1.199A-5(b)(2)(ix) |
| Stockbroker | Yes | Brokerage, 1.199A-5(b)(2)(x) |
| Real estate agent or broker, insurance agent or broker | No | Excluded from brokerage, 1.199A-5(b)(2)(x) |
| Advice and counsel to clients, lobbying | Yes | Consulting, 1.199A-5(b)(2)(vii) |
| Sales, training and educational courses, consulting embedded in a non-SSTB sale with no separate fee | No | Excluded from consulting, 1.199A-5(b)(2)(vii) |
| Engineer, architect | No | Struck from the list by section 199A(d)(2)(A) |
| Software development, web development, UX and graphic design, data analytics delivered as a work product | Not a listed field; no SSTB unless the work is really advice and counsel | Not named in 1.199A-5(b); judge on the facts |
| "IT consultant" or "marketing consultant" | Depends: advice only is consulting; delivering code, systems or campaigns is not | 1.199A-5(b)(2)(vii) |
| Endorsement, licensing of name or likeness, appearance fees | Yes | Reputation or skill, 1.199A-5(b)(2)(xiv), narrowed to these three |

**De minimis.** A business with gross receipts of USD 25 million or less is not an SSTB if under 10% of its gross receipts come from a specified service (5% above USD 25 million); activity incident to the service counts as the service (Treas. Reg. 1.199A-5(c)(1)).

**Former employees.** A person treated as an employee who then provides substantially the same services to the same business (or a related person) as a contractor is presumed for three years to still be performing services as an employee, which is not a qualified business, unless records rebut it on IRS notice (Treas. Reg. 1.199A-5(d)(3)).

### Step 5: W-2 wages and UBIA

- **W-2 wages** are the section 6051(a)(3) and (8) amounts the business paid its common-law employees for 2026, allocable to QBI, and on Forms W-2 filed with the SSA within 60 days of the due date (section 199A(b)(4)). Wages paid through a payroll provider count if paid to the business's own common-law employees (Treas. Reg. 1.199A-2(b)(2)(ii)). The owner's draw and wages the client earns as someone else's employee never count.
- **UBIA** is the original basis of tangible depreciable property held and available for use at year end, used during the year to produce QBI, and still in its depreciable period: the later of 10 years after placed in service or the last full year of the regular MACRS recovery period (section 199A(b)(6)). Depreciation, section 179 and bonus depreciation do not reduce it (Treas. Reg. 1.199A-2(c)(3)(i): no section 1016(a)(2) or (3) adjustments). A laptop costing USD 3,499 placed in service in 2025 (5-year property) keeps a UBIA of USD 3,499 through 2034, even if it was fully expensed in 2025. Land is not depreciable and has no UBIA.

### Step 6: the deduction for each business

Per business, before the cap (section 199A(b)(2) and (3); Form 8995-A (2026 draft), Parts II and III):

1. **At or below the threshold:** 20% x QBI.
2. **SSTB above the threshold:** first multiply QBI, W-2 wages and UBIA by the applicable percentage (Schedule A, Form 8995-A). Above the end of the range the applicable percentage is zero and so is the deduction.
3. **Tentative amount** (line 3): 20% x QBI (after step 2 for an SSTB).
4. **Wage and UBIA limit** (line 10): the greater of 50% x W-2 wages, or 25% x W-2 wages plus 2.5% x UBIA.
5. **Above the end of the range:** the smaller of line 3 and line 10 (line 11).
6. **Inside the range, where line 10 is less than line 3:** reduction = (line 3 minus line 10) x phase-in fraction; the deduction is line 3 minus that reduction (lines 17 to 26). For a sole proprietor with no employees and no property, line 10 is zero, so the deduction is 20% x QBI x (1 minus the fraction), and for an SSTB that is applied to QBI already cut to the applicable percentage.

### Step 7: combine, cap, then the minimum

1. Add the amounts for every business (Form 8995-A line 16; Form 8995 line 4 times 20%). Negative QBI in one business is first netted against the positive businesses in proportion to their positive QBI, and the loss business's W-2 wages and UBIA are not carried with it (Treas. Reg. 1.199A-1(d)(2)(iii)(A)).
2. Add 20% of qualified REIT dividends and PTP income (refer: R-QBI-REIT).
3. **Cap:** the smaller of that total and 20% x (taxable income before the QBI deduction minus net capital gain plus qualified dividends) (section 199A(a); Form 8995 (2026 draft) lines 11 to 15; Form 8995-A (2026 draft) lines 33 to 37).
4. **Minimum (new for 2026):** if aggregate QBI from all businesses the taxpayer materially participated in is at least USD 1,000, the deduction is the greater of the step 3 result and USD 400 (section 199A(i) as rewritten by Public Law 119-21 section 70105(b); Form 8995 (2026 draft) lines 16 and 17; Form 8995-A (2026 draft) lines 40 and 41). The minimum is compared after the taxable income cap. QBI from a business the taxpayer does not materially participate in is passive and does not count toward the USD 1,000.

### Step 8: losses carried forward

If total QBI for 2026 (including a 2025 carryforward) is below zero, the QBI part of the deduction is zero and the negative amount is carried to 2027 as negative QBI from a separate trade or business, offsetting QBI from all businesses in later years whether or not the loss business still exists (section 199A(c)(2); Treas. Reg. 1.199A-1(d)(2)(iii)(B); 2026 draft Instructions for Form 8995, line 18). A loss suspended under another rule (at-risk, passive, excess business loss) enters QBI only in the year it is allowed. An SSTB loss carried forward keeps the applicable percentage of the year it arose.

### Form 8995 (simplified), 2026 draft line by line

Use it when taxable income before the QBI deduction is at or below USD 201,750 (USD 201,775 married filing separately, USD 403,500 joint) and the client is not a cooperative patron. Up to five businesses or aggregations go on line 1; an aggregation needs Schedule B (Form 8995-A) attached.

| Line | Entry |
| --- | --- |
| 1i to 1v | Business name, TIN (the LLC's EIN, or the owner's SSN if none), QBI or loss |
| 2 | Total QBI |
| 3 | Qualified business loss carryforward from 2025 (negative) |
| 4 | Lines 2 plus 3; zero if negative |
| 5 | Line 4 x 20% |
| 6 to 9 | REIT and PTP amounts and the 20% component |
| 10 | Lines 5 plus 9 |
| 11 | Taxable income before the QBI deduction |
| 12 | Net capital gain plus qualified dividends |
| 13 | Line 11 minus line 12, not below zero |
| 14 | Line 13 x 20% |
| 15 | Smaller of line 10 or line 14 (new label: before the minimum deduction) |
| 16 | Minimum deduction for active QBI (new for 2026): USD 400 if active QBI on line 1 is at least USD 1,000 |
| 17 | Greater of line 15 or line 16; to Form 1040 line 13a |
| 18 | QBI loss carryforward to 2027 (lines 2 plus 3, if negative) |
| 19 | REIT and PTP loss carryforward |
| 20 | Box for an electing small business trust (new) |

### Form 8995-A (detailed), 2026 draft

Use it when taxable income before the QBI deduction is above the threshold, or the client is a cooperative patron. An SSTB below the threshold, or several businesses below the threshold, do not on their own require Form 8995-A. Schedule A carries the SSTB applicable percentage, Schedule B the aggregation, Schedule C loss netting and carryforwards, Schedule D the patron reduction. Part II lines 2 to 16 run Step 6 per business, Part III lines 17 to 26 the phase-in, Part IV lines 27 to 41 the cap, the section 199A(g) amount and the minimum (lines 39 to 41).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Taxable income exactly at the threshold (USD 201,750) | Below-threshold rules; Form 8995. The phase-in starts with the first dollar above |
| Taxable income exactly at the end of the range (USD 276,750) | An SSTB gets nothing (applicable percentage zero); others take the full wage and UBIA limit |
| Married filing separately | Threshold USD 201,775 and range USD 75,000 (end USD 276,775): not half the joint figures, so a couple filing separately reaches the limits at about half the joint income |
| SSTB with taxable income inside the range | Partial deduction, shrinking on two counts (applicable percentage and phase-in); not zero until the end of the range |
| Non-SSTB above the range, no employees, no property | Deduction zero: line 10 is zero. Flag; see `us-s-corp-election-decision` |
| Non-SSTB above the range with equipment but no employees | Limit is 2.5% x UBIA: ask for the asset register before assuming zero |
| QBI negative for the year | Deduction from QBI zero; carry the loss to 2027 (Step 8). The USD 400 minimum does not apply because aggregate active QBI is below USD 1,000 |
| Active QBI between USD 1,000 and USD 2,000 | 20% is under USD 400, so the minimum lifts the deduction to USD 400 (Case 2) |
| QBI only from a business the client does not materially participate in | Normal 20% rules apply; no USD 400 minimum |
| Taxable income below QBI | The cap binds: 20% x (taxable income minus net capital gain) |
| Taxable income zero or negative | Cap is zero. Whether and how the USD 400 minimum then applies is not settled by final instructions: flag for the reviewer |
| Two Schedules C, one a loss | Net the loss against the profitable business in proportion (Treas. Reg. 1.199A-1(d)(2)(iii)); never take 20% of the profitable one alone |
| Mixed SSTB and non-SSTB work in one business | Apply the 10% (or 5%) de minimis test on gross receipts; if it fails, refer (R-QBI-SSTB-MIXED) |
| Client was the customer's employee in the last 3 years, same work | Presumed employee; no QBI from that work unless rebutted (Treas. Reg. 1.199A-5(d)(3)) |
| Business changes character during the year | One trade or business for the year; judge SSTB status on the whole year's receipts with the de minimis test |
| Community property state, married filing jointly | Schedule C income split between spouses follows state law; QBI follows that split. Flag; this skill does not do the split |
| Statutory employee (W-2 box 13) | The income is QBI (Schedule C); not W-2 wages for the limit |

Conservative defaults where facts are missing:

| Missing fact | Default |
| --- | --- |
| SSTB status unclear | Treat as SSTB above the threshold; flag |
| Taxable income within USD 10,000 of the threshold or the end of the range | Work it both ways and show both |
| W-2 wages not documented | Assume zero; ask for Forms W-2 and W-3 |
| UBIA not documented | Assume zero above the threshold only after asking for Form 4562 or the asset list |
| 2025 carryforward not provided | Assume none; ask for the 2025 Form 8995 line 16 or Form 8995-A Schedule C |
| Material participation not confirmed | Do not apply the USD 400 minimum; ask |
| Health insurance or retirement deduction not yet worked out | Work them out first; never skip the QBI reduction |

## Worked cases

**Case 1, a decision: does a financial planner just above the threshold get a partial deduction, and is an extra USD 5,100 SEP contribution worth making?** A single financial planner (financial services, an SSTB) has 2026 Schedule C net profit of USD 270,000, no employees and no qualifying property. From the upstream skills: deductible half of self-employment tax USD 15,054.50, self-employed health insurance USD 12,000, SEP contribution USD 20,000 (option A). No other income; standard deduction USD 16,100 (2026, from `us-federal-income-tax-return-1040`). Option B raises the SEP contribution by USD 5,100 to USD 25,100, within the plan limit worked out in `us-self-employed-retirement`.

Option A: QBI = 270,000 minus 15,054.50 minus 12,000 minus 20,000 = USD 222,945.50. Taxable income before the QBI deduction = USD 206,845.50, which is USD 5,095.50 above the USD 201,750 threshold. Phase-in fraction = 5,095.50 / 75,000 = 6.794%; applicable percentage = 93.206%. The SSTB is still a qualified business, cut to 93.206%: 20% x 222,945.50 x 93.206% = USD 41,559.72 (Form 8995-A line 3). Line 10 is zero, so the phase-in reduction is 41,559.72 x 6.794% = USD 2,823.57, leaving USD 38,736.15. The cap is 20% x 206,845.50 = USD 41,369.10, not binding. **Deduction USD 38,736.15**, a partial deduction, not zero. Taxable income after it: USD 168,109.35.

Option B: QBI = USD 217,845.50 and taxable income before the QBI deduction = USD 201,745.50, at or below the threshold, so SSTB status no longer matters and Form 8995 applies. 20% of QBI is USD 43,569.10, but the cap is 20% x 201,745.50 = USD 40,349.10, which binds. **Deduction USD 40,349.10.** Taxable income after it: USD 161,396.40.

The figure that decides: the extra USD 5,100 contribution cuts taxable income by USD 6,712.95 (USD 1,612.95 more QBI deduction on top of the USD 5,100). Recommend option B if the client can fund the extra contribution and is content to defer the money; a reviewer confirms the SEP limit. Either way, a planner USD 5,095.50 over the threshold keeps most of the deduction.

```oa-check
name: SSTB just above the 2026 threshold, with and without an extra SEP contribution (single)
inputs:
  schedule_c_profit: 270000
  half_se_tax: 15054.50
  se_health: 12000
  sep_a: 20000
  sep_b: 25100
  std_deduction: 16100
  threshold: 201750
  phase_range: 75000
steps:
  - qbi_a: schedule_c_profit - half_se_tax - se_health - sep_a
  - ti_a: qbi_a - std_deduction
  - phase_a: clamp((ti_a - threshold) / phase_range, 0, 1)
  - applicable_a: 1 - phase_a
  - line3_a: 0.20 * qbi_a * applicable_a
  - after_phase_a: line3_a - (line3_a - 0) * phase_a
  - deduction_a: min(after_phase_a, 0.20 * ti_a)
  - qbi_b: schedule_c_profit - half_se_tax - se_health - sep_b
  - ti_b: qbi_b - std_deduction
  - deduction_b: min(0.20 * qbi_b, 0.20 * ti_b)
  - taxable_after_a: ti_a - deduction_a
  - taxable_after_b: ti_b - deduction_b
  - saving_in_taxable_income: taxable_after_a - taxable_after_b
expected:
  qbi_a: 222945.50
  ti_a: 206845.50
  line3_a: 41559.72
  deduction_a: 38736.15
  ti_b: 201745.50
  deduction_b: 40349.10
  taxable_after_a: 168109.35
  taxable_after_b: 161396.40
  saving_in_taxable_income: 6712.95
```

**Case 2, the new USD 400 minimum.** A single employee earns USD 30,000 of wages and runs a small weekend photography business she works in herself for more than 500 hours a year (material participation). Schedule C net profit is USD 1,500; the deductible half of self-employment tax is USD 105.97 (from `us-schedule-c-and-se-computation`); no health insurance or retirement deduction. Standard deduction USD 16,100.

QBI = 1,500 minus 105.97 = USD 1,394.03. Taxable income before the QBI deduction = 30,000 plus 1,394.03 minus 16,100 = USD 15,294.03, below the threshold, so Form 8995. Line 5: 20% x 1,394.03 = USD 278.81. Line 14: 20% x 15,294.03 = USD 3,058.81. Line 15: USD 278.81. Active QBI of USD 1,394.03 is at least USD 1,000, so line 16 is USD 400 and line 17 is **USD 400**. Under 2025 rules the deduction would have been USD 278.81. Had she not materially participated, or had QBI been under USD 1,000, it would stay at line 15.

```oa-check
name: Minimum deduction for active QBI (2026, single)
inputs:
  wages: 30000
  schedule_c_profit: 1500
  half_se_tax: 105.97
  std_deduction: 16100
  minimum: 400
  minimum_qbi: 1000
steps:
  - qbi: schedule_c_profit - half_se_tax
  - taxable_income: wages + qbi - std_deduction
  - line_5: 0.20 * qbi
  - line_14: 0.20 * taxable_income
  - line_15: min(line_5, line_14)
  - line_16: minimum * clamp(floor(qbi / minimum_qbi), 0, 1)
  - line_17: max(line_15, line_16)
expected:
  qbi: 1394.03
  taxable_income: 15294.03
  line_5: 278.81
  line_14: 3058.81
  line_15: 278.81
  line_16: 400.00
  line_17: 400.00
```

**Case 3, the wage limit above the range (no check block).** A married couple filing jointly have taxable income before the QBI deduction of USD 600,000, above the USD 553,500 end of the range. Her landscaping business (not an SSTB) has QBI of USD 300,000, paid USD 60,000 of W-2 wages to two employees and holds equipment with UBIA of USD 200,000. 20% of QBI is USD 60,000. The limit is the greater of 50% x 60,000 = USD 30,000 and 25% x 60,000 plus 2.5% x 200,000 = USD 20,000, so USD 30,000. The deduction is the smaller of USD 60,000 and USD 30,000: **USD 30,000**; the cap (20% x 600,000 = USD 120,000) does not bind. Were it an SSTB, the deduction would be zero.

## When to refuse or refer

On top of the global catalogue in `us-tax-workflow-base` and the upstream skills' catalogues.

| Code | Situation | Action |
| --- | --- | --- |
| R-QBI-MULTI | Several businesses where aggregation under Treas. Reg. 1.199A-4 is in question (50% common ownership, same year end, no SSTB, and two of: same products or services, shared facilities or staff, operated in coordination) | Refer: aggregation is an election that must be reported consistently in later years |
| R-QBI-K1 | QBI from a partnership or S corporation (Schedule K-1) | Refer: entity-level W-2 wages, UBIA and reasonable compensation |
| R-QBI-REIT | Qualified REIT dividends or PTP income or loss | Refer: separate 20% component and its own carryforward |
| R-QBI-NOL | A net operating loss carryforward changes taxable income | Refer: ordering with the threshold and the cap |
| R-QBI-SSTB-MIXED | A business with both SSTB and non-SSTB receipts that fails the 10% (or 5%) de minimis test | Refer: Treas. Reg. 1.199A-5(c) |
| R-QBI-COOP | Patron of an agricultural or horticultural cooperative, or a section 199A(g) amount | Refer: Form 8995-A Schedule D |
| R-QBI-RENTAL | Rental real estate claimed as a trade or business (Rev. Proc. 2019-38 safe harbor) | Use `us-real-estate-professional-and-short-term-rentals`, then refer if unclear |
| R-QBI-EMPLOYEE | Client reclassified from employee to contractor for the same customer within 3 years | Flag: presumption of employee status; reviewer decides whether records rebut it |
| R-QBI-TRUST | Estate, trust or electing small business trust | Refer: Form 1041 and the DNI allocation |

Always flag for the reviewer: taxable income within USD 10,000 of the threshold or the end of the range; above the range with no W-2 wages; a deduction over USD 15,000; an unclear SSTB classification or mixed advice and deliverable work; any QBI loss or carryforward; a missing retirement or health insurance reduction; more than one business; the USD 400 minimum claimed (material participation evidence).

Never:

- Apply a 23% rate, for any year. It was in the House-passed bill only; Public Law 119-21 kept 20%.
- Compute QBI without subtracting the deductible half of self-employment tax, self-employed health insurance and retirement plan contributions.
- Say SSTB status does not matter without checking taxable income.
- Treat the owner's draw or someone else's W-2 wages as W-2 wages for the limit.
- Use Form 8995 when taxable income is above the threshold.
- Let the QBI deduction reduce self-employment tax or adjusted gross income; it is allowed for income tax only (section 199A(f)(3)) and is taken after adjusted gross income.
- Apply the 2025 figures (USD 197,300 / 394,600 thresholds, USD 50,000 / 100,000 ranges) or leave out the USD 400 minimum on a 2026 return.

## Filing and payment

Form 8995 or Form 8995-A (with Schedules A to D as needed) is attached to the 2026 Form 1040, due **15 April 2027**; the deduction goes on Form 1040 line 13a (2026 draft Instructions for Form 8995). An extension to 15 October 2027 extends filing, not payment. The QBI deduction lowers income tax only, so it lowers the 2026 estimated payments; see `us-quarterly-estimated-tax`. Keep the SSTB analysis, the de minimis receipts split, material participation evidence, Forms W-2 and W-3 and the asset register with the working papers.

## Completion checklist

- Year figures are 2026: thresholds USD 201,750 / 201,775 / 403,500, ranges USD 75,000 / 150,000, rate 20%.
- QBI reduced by the deductible half of self-employment tax, self-employed health insurance and retirement contributions, split in proportion across businesses.
- Section 224 tips, capital items, interest not allocable to the business and suspended losses kept out of QBI.
- Taxable income measured before the QBI deduction.
- SSTB status decided field by field, with the de minimis test and the former-employee presumption checked.
- W-2 wages limited to common-law employees on timely filed Forms W-2; UBIA from the asset register at unadjusted cost, within the depreciable period.
- Phase-in fraction and applicable percentage computed with the 2026 range.
- Cap applied, then the USD 400 minimum (with USD 1,000 of active QBI and material participation confirmed).
- 2025 carryforward brought in; 2027 carryforward recorded.
- Right form: Form 8995 at or below the threshold, Form 8995-A above.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 199A (govinfo, 2024 edition, before Public Law 119-21). Read for (a) the cap, (b)(2) 20%, 50%, 25% and 2.5%, (b)(3) and (d)(3) the phase-in, (b)(4) W-2 wages and the 60-day rule, (b)(6) UBIA and the depreciable period, (c) QBI and loss carryover, (d)(2) SSTB, (e)(1) and (e)(2) taxable income and threshold, (f)(3), and the old (i) termination after 2025. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm | 2026-11-13 |
| Public Law 119-21 (One Big Beautiful Bill Act), section 70105. Read for (a) the USD 75,000 (USD 150,000 joint) ranges, (b) the rewritten section 199A(i) minimum deduction of USD 400 with USD 1,000 of active QBI, material participation under 469(h), indexing after 2026, and (c) taxable years beginning after 31 December 2025. No change to the 20% rate. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.26 (2026 thresholds USD 201,750, 201,775, 403,500 and phase-in amounts USD 276,750, 276,775, 553,500) and section 2.12 (USD 400 minimum, USD 1,000 QBI, indexed after 2026). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Form 8995 (2026), IRS early release draft created 5/1/26. Read for the 2026 threshold line and lines 1 to 20, including new lines 15, 16 (minimum deduction) and 20. | https://www.irs.gov/pub/irs-dft/f8995--dft.pdf | 2026-11-13 |
| Form 8995-A (2026), IRS early release draft created 5/26/26. Read for Parts I to IV, lines 2 to 26 (wage and UBIA limit, phase-in with USD 75,000 / 150,000) and lines 39 to 41 (minimum deduction). | https://www.irs.gov/pub/irs-dft/f8995a--dft.pdf | 2026-11-13 |
| Instructions for Form 8995 (2026), IRS draft dated 17 June 2026. Read for the minimum deduction and material participation, section 224 tips out of QBI, suspended losses, the SSTB exceptions with 2026 amounts, aggregation conditions, line 11, line 17 and Form 1040 line 13a. | https://www.irs.gov/pub/irs-dft/i8995--dft.pdf | 2026-11-13 |
| Instructions for Form 8995 (2025), final. Read for the QBI items list (deductible part of self-employment tax, self-employed health insurance, retirement contributions) and the QBI flow chart, repeated in the 2026 draft. | https://www.irs.gov/pub/irs-pdf/i8995.pdf | 2026-11-13 |
| Treas. Reg. 1.199A-1 (eCFR). Read for (d)(2)(iii) netting of negative QBI in proportion and the separate-business carryover. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-1 | 2026-11-13 |
| Treas. Reg. 1.199A-2 (eCFR). Read for (b)(2) W-2 wages, including wages paid by another person for the business's common-law employees, and (c)(3) UBIA without depreciation adjustments. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-2 | 2026-11-13 |
| Treas. Reg. 1.199A-3 (eCFR). Read for (b)(1)(vi): the section 164(f), 162(l) and 404 deductions reduce QBI in proportion to the business's gross income. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-3 | 2026-11-13 |
| Treas. Reg. 1.199A-5 (eCFR). Read for (b) the field definitions (health, accounting, consulting, financial services, brokerage, reputation or skill), (c)(1) the 10% and 5% de minimis rule at USD 25 million, and (d)(3) the three-year employee presumption. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-5 | 2026-11-13 |

Not yet confirmed: the final 2026 Forms 8995 and 8995-A and their instructions were not yet released when read; line numbers above are from the IRS early release drafts and may change. The draft Instructions for Form 8995-A (2026) were downloaded but not relied on. How the USD 400 minimum applies when taxable income before it is below USD 400 or zero is not addressed in the law or the draft instructions read. The 2027 indexed amounts of the USD 400 and USD 1,000 are not yet published. Treas. Reg. 1.199A-4 (aggregation) was not opened; the aggregation conditions above are from the 2026 draft Instructions for Form 8995.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
