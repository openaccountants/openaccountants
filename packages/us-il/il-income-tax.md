---
name: il-income-tax
description: "Illinois Individual Income Tax Return (Form IL-1040) for sole proprietors and single-member LLCs. Covers the flat 4.95% rate, Illinois base income computation from federal AGI, Schedule M addition and subtraction modifications, property tax credit (Schedule ICR), earned income credit, and the full return assembly. Primary source: 35 ILCS 5/."
version: 1.0
jurisdiction: US-IL
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Amir Pelinkovic
review_status: current
depends_on: - us-tax-workflow-base
category: state
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Income Tax

## Illinois IL-1040 Individual Return v1.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **a licensed accountant** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### IL Income Tax

- **IL flat rate** — 4.95% flat individual rate  _(35 ILCS 5/201(b)(5.4); 2025 IL-1040 instr.)_
- **Starting point** — Federal AGI (1040 Line 11) is the starting point (IL-1040 Line 1)  _(35 ILCS 5/203(a); 2025 IL-1040 instr.)_
- **Standard deduction** — IL allows no standard or itemized deduction; base income less subtractions/exemptions  _(86 Ill. Admin. Code 100.2410; IL-1040 instr.)_
- **Per person exemption** — $2,850 per person for 2025  _(IDOR FY2025-16; 2025 IL-1040 instr.)_
- **MFJ exemption (taxpayer + spouse)** — $5,700 MFJ (2 x $2,850)  _(IDOR FY2025-16.)_
- **Per dependent exemption** — $2,850 per dependent  _(IDOR FY2025-16.)_
- **Age 65+ / legally blind additional exemption** — Additional $1,000 per qualifying condition (65+/blind)  _(35 ILCS 5/204; IL-1040 instr.)_
- **Exemption phase-out cliff — Single/HoH/MFS** — Exemption fully disallowed if federal AGI > $250,000 (Single/HoH/MFS)  _(35 ILCS 5/204(d); IL-1040 instr.)_
- **Exemption phase-out cliff — MFJ** — Fully disallowed if federal AGI > $500,000 (MFJ)  _(35 ILCS 5/204(d); IL-1040 instr.)_
- **Property tax credit** — 5% of IL property tax on principal residence, nonrefundable  _(35 ILCS 5/208; Schedule ICR.)_
- **Property tax credit — AGI cap** — Disallowed above $250K(S)/$500K(MFJ)  _(35 ILCS 5/208; Schedule ICR instr.)_
- **K-12 education expense credit** — 25% of qualified K-12 expenses over $250, max $750, nonrefundable  _(35 ILCS 5/201(m); Schedule ICR.)_
- **K-12 credit — AGI cap** — Disallowed above $250K(S)/$500K(MFJ)  _(Schedule ICR instr.)_
- **Illinois EIC** — 20% of federal EIC, refundable (2023+)  _(35 ILCS 5/212; Schedule IL-E/EIC.)_
- **EIC subject to AGI cap?** — IL EIC is not subject to the exemption cliff  _(35 ILCS 5/212.)_
- **§168(k) bonus depreciation** — IL decouples from federal bonus; add back on Schedule M / IL-4562  _(35 ILCS 5/203(b)(2)(E-10); IL-4562 instr.)_
- **Social Security** — Social Security taxed federally is fully subtracted  _(35 ILCS 5/203(a)(2); IL-1040 Line 5.)_
- **U.S. government bond interest** — Interest on U.S. obligations is subtracted  _(35 ILCS 5/203(a)(2)(N); Schedule M.)_
- **Net loss limitation** — This is a CORPORATE net loss deduction provision (IL-1120), not individual. The cap is $500,000/yr for tax years ending on/after 12/31/2024 and before 12/31/2027; the $100,000 cap applied only through tax years ending before 12/31/2024.  _(35 ILCS 5/207; 2025 IL-1120 instr. (R-12/25); PA 103-0592.)_
- **Deadline** — April 15, 2026 for TY2025  _(35 ILCS 5/505; IL-1040 instr.)_
- **Extension** — IL grants an automatic 6-month extension to ALL filers regardless of any federal extension (no IL form). A federal extension only matters if more than 6 months is needed. The 'with federal extension' condition is wrong.  _(2025 IL-1040 instr., 'When is my return due / Automatic extension.')_
- **Residency test** — IL determines residency by domicile and presence for other than a temporary or transitory purpose. IL has no 'place of abode + day-count' statutory-residency test (that is a NY/CA-style test).  _(35 ILCS 5/1501(a)(20); 86 Ill. Admin. Code 100.3020.)_

## What this file is

**Obligation category:** IT (Income Tax)
**Functional role:** Return assembly
**Status:** Complete

This is a Tier 2 content skill for preparing the Illinois Form IL-1040 for a full-year Illinois resident who is a sole proprietor or single-member LLC owner. Illinois imposes a flat 4.95% income tax rate, starting from federal adjusted gross income (AGI) and applying Illinois-specific modifications.

## Section 1 -- Scope statement

**In scope:**

- Form IL-1040 (Individual Income Tax Return)
- Schedule M (Other Additions and Subtractions)
- Schedule ICR (Illinois Credits, including property tax credit and K-12 education expense credit)
- Schedule IL-E/EIC (Illinois Earned Income Credit)
- Full-year Illinois residents
- Filing status: single, MFJ, MFS, head of household, qualifying surviving spouse
- Self-employment income from Schedule C flowing through federal AGI

**Out of scope (refused):**

- Part-year and non-resident returns (Schedule NR)
- Business income apportionment for multi-state operations
- Partnership and S-corp pass-through (Schedule K-1-P)
- Illinois estate/trust income tax (Form IL-1041)
- Amended returns (Form IL-1040-X)
- Net loss carryforward computations beyond simple tracking
- Illinois corporate income tax (Form IL-1120)

## Section 2 -- Filing requirements

### Who must file

- **Filing requirement** — An Illinois resident must file Form IL-1040 if: 1. They are required to file a federal income tax return, OR 2. They want to claim a refund of Illinois income tax withheld, OR 3. They have Illinois base income exceeding the personal exemption amount.  _(35 ILCS 5/502(a).)_

### Due date

**Due date table**  _(35 ILCS 5/505)_

| Item | Date | Source |
| --- | --- | --- |
| Filing deadline | April 15, 2026 (for tax year 2025) | 35 ILCS 5/505 |
| Extension deadline | October 15, 2026 (automatic 6-month extension with federal extension) | 35 ILCS 5/505(b) |

- **Automatic extension detail** — Illinois automatically grants a 6-month extension if the taxpayer has a federal extension. No separate Illinois extension form is required. However, estimated tax payments are still due by April 15.  _(35 ILCS 5/505(b))_

## Section 3 -- Rates and thresholds

**Rates and thresholds table**  _(see rows)_

| Item | Amount | Source |
| --- | --- | --- |
| Illinois flat income tax rate | 4.95% | 35 ILCS 5/201(b)(5.4) |
| Personal exemption -- single | $2,625 | 35 ILCS 5/204 (2025 amount, indexed) |
| Personal exemption -- MFJ | $5,250 | 35 ILCS 5/204 |
| Personal exemption -- each dependent | $2,625 | 35 ILCS 5/204 |
| Property tax credit rate | 5% of property taxes paid on principal residence | 35 ILCS 5/208 |
| Earned income credit | 20% of federal EIC (refundable) | 35 ILCS 5/212 (2025) |
| K-12 education expense credit | 25% of expenses over $250, max credit $750 | 35 ILCS 5/218 |

- **Note on personal exemption** — Illinois does NOT have a standard deduction or itemized deductions at the state level. The personal exemption is the only below-the-line deduction.  _(35 ILCS 5/204)_

## Section 4 -- Computation rules (Step format)

### Step 1: Start with federal AGI (Line 1)

- **Federal AGI starting point** — Enter federal adjusted gross income from federal Form 1040, Line 11. This is the starting point for Illinois.  _(35 ILCS 5/203(a))_

### Step 2: Add Illinois addition modifications (Line 3, Schedule M)

Common additions for self-employed individuals:

**Addition modifications table**  _(see rows)_

| Addition | Description | Source |
| --- | --- | --- |
| A-1 | Interest and dividends from state/local bonds of other states | 35 ILCS 5/203(a)(2)(F) |
| A-5 | Bonus depreciation add-back (IL does not conform to IRC §168(k)) | 35 ILCS 5/203(a)(2)(D-25) |
| A-18 | Net loss add-back (if federal AGI includes IL net loss deduction from prior years that IL has not allowed) | 35 ILCS 5/203(e) |
| A-24 | SALT deduction add-back -- Illinois requires add-back of any state income tax deducted federally (this is automatic since IL starts from AGI, not taxable income) | N/A -- structural |

- **Key structural point** — Because Illinois starts from federal AGI (not federal taxable income), the federal standard deduction, itemized deductions, and QBI deduction do NOT flow into the Illinois computation. This means there is no SALT add-back issue -- it is handled structurally.  _(N/A -- structural)_

### Step 3: Subtract Illinois subtraction modifications (Line 7, Schedule M)

Common subtractions:

**Subtraction modifications table**  _(see rows)_

| Subtraction | Description | Source |
| --- | --- | --- |
| S-1 | U.S. government interest (Treasury bonds, savings bonds) | 35 ILCS 5/203(a)(2)(N) |
| S-2 | Illinois income tax refund included in federal AGI | Structural (IL tax is not deductible for IL) |
| S-7 | Social Security and railroad retirement income included in federal AGI | 35 ILCS 5/203(a)(2)(F) |
| S-8 | IL retirement income subtraction (contributions to qualified IL plans) | 35 ILCS 5/203(a)(2)(F) |
| S-19 | Illinois special depreciation (replace federal bonus with IL straight-line MACRS) | 35 ILCS 5/203(a)(2)(D-25) |

### Step 4: Compute Illinois base income (Line 9)

- **Illinois base income formula** — Federal AGI + additions - subtractions = Illinois base income.  _(35 ILCS 5/203)_

### Step 5: Subtract personal exemptions (Line 10)

- **Personal exemptions** — $2,625 per taxpayer (single: $2,625; MFJ: $5,250); $2,625 per dependent claimed on the federal return  _(35 ILCS 5/204)_

### Step 6: Compute Illinois net income (Line 11)

- **Illinois net income formula** — Illinois base income - exemptions = Illinois net income. If negative, enter zero.  _(35 ILCS 5/204)_

### Step 7: Compute Illinois tax (Line 12)

- **Illinois tax formula** — Illinois net income x 4.95% = Illinois income tax.  _(35 ILCS 5/201(b)(5.4))_

### Step 8: Apply tax credits (Lines 14-23)

- **Credit order** — Apply credits in this order: 1. Property tax credit (Schedule ICR): 5% of property taxes paid on the principal residence. Non-refundable. 2. K-12 education expense credit (Schedule ICR): 25% of qualifying expenses exceeding $250, max credit $750. Non-refundable. 3. Credit for taxes paid to other states: If the taxpayer earned income in another state that was taxed by that state, Illinois allows a credit to prevent double taxation. Non-refundable. 4. Illinois Earned Income Credit (Schedule IL-E/EIC): 20% of federal EIC. Refundable.  _(35 ILCS 5/208; 35 ILCS 5/201(m); 35 ILCS 5/212)_

### Step 9: Subtract withholding and estimated payments (Lines 24-27)

- **Withholding and payments** — Illinois withholding from W-2s and 1099s. Estimated tax payments made (Form IL-1040-ES). Overpayment from prior year applied.  _(35 ILCS 5/803)_

### Step 10: Compute balance due or refund (Line 34/36)

- **Balance due/refund formula** — Tax after credits - withholding - estimated payments = balance due (if positive) or refund (if negative).  _(IL-1040 instr.)_

## Section 5 -- Edge cases and special rules

### E-1: Bonus depreciation add-back and replacement

- **Bonus depreciation add-back and replacement** — Illinois requires taxpayers to add back federal bonus depreciation (IRC §168(k)) and instead claim the standard MACRS depreciation that would have been allowable without bonus depreciation. This creates a timing difference, not a permanent one. Track the depreciation schedules carefully.  _(35 ILCS 5/203(a)(2)(D-25))_

### E-2: Net loss limitation

- **Net loss deduction limitation** — Illinois limits the net loss deduction to $100,000 per year for individuals (enacted 2021, extended through 2027). Excess losses carry forward.  _(35 ILCS 5/203(e)(2).)_

### E-3: No standard deduction

- **No standard deduction** — Illinois has NO standard deduction and NO itemized deductions at the state level. The only below-the-line deduction is the personal exemption. This catches taxpayers who expect a state deduction mirroring the federal one.  _(86 Ill. Admin. Code 100.2410)_

### E-4: Social Security subtraction

- **Social Security subtraction** — All Social Security benefits included in federal AGI are subtracted for Illinois purposes. Illinois does not tax Social Security income.  _(35 ILCS 5/203(a)(2)(F).)_

### E-5: Illinois residency determination

- **Residency determination** — Illinois uses a "place of abode" test, not a day-count test. If a taxpayer maintains a place of abode in Illinois and is present in Illinois for more than an aggregate of 12 months during a three-year period, they are presumed to be an Illinois resident.  _(35 ILCS 5/1501(a)(20).)_

### E-6: Gambling winnings

- **Gambling winnings** — Illinois does not allow a subtraction for gambling losses. If federal AGI includes net gambling winnings (after losses are deducted as federal itemized deductions), the Illinois computation starts from AGI which includes gross gambling winnings. The losses deducted federally as itemized deductions do not reduce IL base income.  _(unsure)_

## Section 6 -- Test suite

### Test 1: Standard freelancer, single

**Input:** Federal AGI: $100,000 (all Schedule C). No additions. Social Security subtraction: $0. No property tax. Single, no dependents.
**Expected:** Base income: $100,000. Exemption: $2,625. Net income: $97,375. Tax: $97,375 x 4.95% = $4,820.06.

### Test 2: MFJ with property tax credit

**Input:** Federal AGI: $150,000. No modifications. MFJ, 2 dependents. Property taxes paid: $8,000.
**Expected:** Exemptions: $5,250 + (2 x $2,625) = $10,500. Net income: $139,500. Tax: $139,500 x 4.95% = $6,905.25. Property tax credit: $8,000 x 5% = $400. Net tax: $6,505.25.

### Test 3: Bonus depreciation add-back

**Input:** Federal AGI includes $50,000 of bonus depreciation on a $50,000 asset (5-year MACRS). Year 1.
**Expected:** Addition: $50,000. Subtraction: $10,000 (year 1 standard MACRS on 5-year property). Net addition: $40,000. Track remaining $40,000 as future IL subtractions.

### Test 4: Social Security subtraction

**Input:** Federal AGI: $60,000 including $12,000 of Social Security benefits taxed federally.
**Expected:** Subtraction: $12,000. IL base income: $48,000.

### Test 5: Earned income credit

**Input:** Federal EIC: $2,000. Single, 1 child.
**Expected:** IL EIC: $2,000 x 20% = $400 (refundable).

## Section 7 -- Prohibitions

- **P-1:** Do NOT apply a standard deduction or itemized deductions to Illinois income. Only the personal exemption applies.
- **P-2:** Do NOT carry forward federal NOLs into Illinois without checking the $100,000 IL net loss limitation.
- **P-3:** Do NOT assume bonus depreciation flows through. Illinois requires the add-back.
- **P-4:** Do NOT tax Social Security benefits for Illinois purposes.
- **P-5:** Do NOT file a separate Illinois extension form if the taxpayer has a federal extension.
- **P-6:** Do NOT use graduated brackets. Illinois has a flat 4.95% rate.

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Federal AGI correctly transcribed from Form 1040, Line 11
- [ ] All Schedule M additions identified (especially bonus depreciation)
- [ ] All Schedule M subtractions identified (especially Social Security, gov't bond interest)
- [ ] Personal exemptions correctly computed ($2,625 x number of exemptions)
- [ ] Flat rate of 4.95% applied
- [ ] Property tax credit at 5% (non-refundable)
- [ ] EIC at 20% of federal EIC (refundable)
- [ ] No standard deduction applied
- [ ] Net loss limitation of $100,000 checked
- [ ] Reviewer brief includes all positions and flags

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
