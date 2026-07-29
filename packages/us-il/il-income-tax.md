---
name: il-income-tax
description: >
  Illinois Individual Income Tax Return (Form IL-1040) for sole proprietors and single-member LLCs. Covers the flat 4.95% rate, Illinois base income computation from federal AGI, Schedule M addition and subtraction modifications, property tax credit (Schedule ICR), earned income credit, and the full return assembly. Primary source: 35 ILCS 5/.
jurisdiction: US-IL
tier: 2
category: state
tax_year: 2025
version: 0.1
verified_by: pending
last_updated: 2026-05-29
depends_on:
  - us-tax-workflow-base
---

# Illinois IL-1040 Individual Return v1.0

## Verified rates & thresholds (accountant-reviewed)

> This block is generated from the verified facts database at openaccountants.com —
> edit the facts there, not this prose. Items under clarification are excluded.

### IL Income Tax

- **IL flat rate** — 4.95% flat individual rate  _(35 ILCS 5/201(b)(5.4); 2025 IL-1040 instr.)_
- **Starting point** — Federal AGI (1040 Line 11) is the starting point (IL-1040 Line 1)  _(35 ILCS 5/203(a); 2025 IL-1040 instr.)_
- **Standard deduction** — IL allows no standard or itemized deduction; base income less subtractions/exemptions  _(86 Ill. Admin. Code 100.2410; IL-1040 instr.)_
- **Per person** — $2,850 per person for 2025  _(IDOR FY2025-16; 2025 IL-1040 instr.)_
- **MFJ (taxpayer + spouse)** — $5,700 MFJ (2 x $2,850)  _(IDOR FY2025-16.)_
- **Per dependent** — $2,850 per dependent  _(IDOR FY2025-16.)_
- **Age 65+ / legally blind** — Additional $1,000 per qualifying condition (65+/blind)  _(35 ILCS 5/204; IL-1040 instr.)_
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

---

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

---

## Section 2 -- Filing requirements

### Who must file

An Illinois resident must file Form IL-1040 if:

1. They are required to file a federal income tax return, OR
2. They want to claim a refund of Illinois income tax withheld, OR
3. They have Illinois base income exceeding the personal exemption amount.

**Source:** 35 ILCS 5/502(a).

### Due date

| Item | Date | Source |
|------|------|--------|
| Filing deadline | April 15, 2026 (for tax year 2025) | 35 ILCS 5/505 |
| Extension deadline | October 15, 2026 (automatic 6-month extension with federal extension) | 35 ILCS 5/505(b) |

Illinois automatically grants a 6-month extension if the taxpayer has a federal extension. No separate Illinois extension form is required. However, estimated tax payments are still due by April 15.

---

## Section 3 -- Rates and thresholds

| Item | Amount | Source |
|------|--------|--------|
| Illinois flat income tax rate | 4.95% | 35 ILCS 5/201(b)(5.4) |
| Personal exemption -- per person (2025) | $2,850 | 35 ILCS 5/204 (indexed annually) |
| Personal exemption -- MFJ (taxpayer + spouse) | $5,700 | 35 ILCS 5/204 |
| Personal exemption -- each dependent | $2,850 | 35 ILCS 5/204 |
| Additional exemption -- age 65+ and/or legally blind | $1,000 each | 35 ILCS 5/204 |
| Property tax credit rate | 5% of property taxes paid on principal residence | 35 ILCS 5/208 |
| Earned income credit | 20% of federal EIC (refundable) | 35 ILCS 5/212 (2025) |
| K-12 education expense credit | 25% of expenses over $250, max credit $750 | 35 ILCS 5/218 |

**Note on personal exemption:** Illinois does NOT have a standard deduction or itemized deductions at the state level. The personal exemption is the only below-the-line deduction.

**Exemption income phase-out (critical):** The personal exemption allowance is fully disallowed for higher-income taxpayers. If federal AGI exceeds **$250,000** (single, head of household, married filing separately, or qualifying surviving spouse) or **$500,000** (married filing jointly), the taxpayer is **not entitled to any personal exemption allowance**. There is no partial phase-out — it is a cliff. **Source:** 35 ILCS 5/204(g); 2025 IL-1040 Exemption Allowance Chart.

**Additional age/blind exemption:** A taxpayer (or spouse, if MFJ) who is 65 or older and/or legally blind receives an additional $1,000 exemption for each applicable condition. This additional amount is also subject to the same AGI phase-out above.

---

## Section 4 -- Computation rules (Step format)

### Step 1: Start with federal AGI (Line 1)

Enter federal adjusted gross income from federal Form 1040, Line 11. This is the starting point for Illinois.

### Step 2: Add Illinois addition modifications (Line 3, Schedule M)

Common additions for self-employed individuals:

| Addition | Description | Source |
|----------|-------------|--------|
| A-1 | Interest and dividends from state/local bonds of other states | 35 ILCS 5/203(a)(2)(F) |
| A-5 | Bonus depreciation add-back (IL does not conform to IRC §168(k)) | 35 ILCS 5/203(a)(2)(D-25) |
| A-18 | Net loss add-back (if federal AGI includes IL net loss deduction from prior years that IL has not allowed) | 35 ILCS 5/203(e) |
| A-24 | SALT deduction add-back -- Illinois requires add-back of any state income tax deducted federally (this is automatic since IL starts from AGI, not taxable income) | N/A -- structural |

**Key structural point:** Because Illinois starts from federal AGI (not federal taxable income), the federal standard deduction, itemized deductions, and QBI deduction do NOT flow into the Illinois computation. This means there is no SALT add-back issue -- it is handled structurally.

### Step 3: Subtract Illinois subtraction modifications (Line 7, Schedule M)

Common subtractions:

| Subtraction | Description | Source |
|-------------|-------------|--------|
| S-1 | U.S. government interest (Treasury bonds, savings bonds) | 35 ILCS 5/203(a)(2)(N) |
| S-2 | Illinois income tax refund included in federal AGI | Structural (IL tax is not deductible for IL) |
| S-7 | Social Security and railroad retirement income included in federal AGI | 35 ILCS 5/203(a)(2)(F) |
| S-8 | IL retirement income subtraction (contributions to qualified IL plans) | 35 ILCS 5/203(a)(2)(F) |
| S-19 | Illinois special depreciation (replace federal bonus with IL straight-line MACRS) | 35 ILCS 5/203(a)(2)(D-25) |

### Step 4: Compute Illinois base income (Line 9)

Federal AGI + additions - subtractions = Illinois base income.

### Step 5: Subtract personal exemptions (Line 10)

**First check the AGI phase-out.** If federal AGI exceeds $250,000 (single/HOH/MFS/QSS) or $500,000 (MFJ), the exemption is **$0** — skip the rest of this step.

Otherwise:

- $2,850 per taxpayer (single: $2,850; MFJ: $5,700)
- $2,850 per dependent claimed on the federal return
- + $1,000 for the taxpayer and/or spouse who is 65+ and/or legally blind (per condition)

### Step 6: Compute Illinois net income (Line 11)

Illinois base income - exemptions = Illinois net income. If negative, enter zero.

### Step 7: Compute Illinois tax (Line 12)

Illinois net income x 4.95% = Illinois income tax.

### Step 8: Apply tax credits (Lines 14-23)

Apply credits in this order:

> **Income cap on Schedule ICR credits:** The property tax credit and the K-12 education expense credit are **both disallowed** if federal AGI exceeds $250,000 (single/HOH/MFS/QSS) or $500,000 (MFJ) — the same thresholds as the exemption phase-out. The Illinois EIC is **not** subject to this cap. **Source:** 35 ILCS 5/208, 5/218; 2025 Schedule ICR instructions.

1. **Property tax credit (Schedule ICR):** 5% of property taxes paid on the principal residence. Non-refundable. Disallowed above the AGI cap.
2. **K-12 education expense credit (Schedule ICR):** 25% of qualifying expenses exceeding $250, max credit $750. Non-refundable. Disallowed above the AGI cap.
3. **Credit for taxes paid to other states:** If the taxpayer earned income in another state that was taxed by that state, Illinois allows a credit to prevent double taxation. Non-refundable.
4. **Illinois Earned Income Credit (Schedule IL-E/EIC):** 20% of federal EIC. Refundable.

### Step 9: Subtract withholding and estimated payments (Lines 24-27)

- Illinois withholding from W-2s and 1099s.
- Estimated tax payments made (Form IL-1040-ES).
- Overpayment from prior year applied.

### Step 10: Compute balance due or refund (Line 34/36)

Tax after credits - withholding - estimated payments = balance due (if positive) or refund (if negative).

---

## Section 5 -- Edge cases and special rules

### E-1: Bonus depreciation add-back and replacement

Illinois requires taxpayers to add back federal bonus depreciation (IRC §168(k)) and instead claim the standard MACRS depreciation that would have been allowable without bonus depreciation. This creates a timing difference, not a permanent one. Track the depreciation schedules carefully.

### E-2: Net loss limitation

Illinois limits the net loss deduction to $100,000 per year for individuals (enacted 2021, extended through 2027). Excess losses carry forward. **Source:** 35 ILCS 5/203(e)(2).

### E-2b: Exemption and credit phase-out cliff

For higher earners this is the single most consequential Illinois rule. Above federal AGI of $250,000 (single/HOH/MFS/QSS) or $500,000 (MFJ), the taxpayer loses the **entire** personal exemption allowance and the **entire** property tax credit and K-12 education expense credit. It is a cliff, not a gradual phase-out — one dollar of AGI over the threshold removes the full benefit. The Illinois EIC is unaffected. **Source:** 35 ILCS 5/204(g), 5/208, 5/218.

### E-3: No standard deduction

Illinois has NO standard deduction and NO itemized deductions at the state level. The only below-the-line deduction is the personal exemption. This catches taxpayers who expect a state deduction mirroring the federal one.

### E-4: Social Security subtraction

All Social Security benefits included in federal AGI are subtracted for Illinois purposes. Illinois does not tax Social Security income. **Source:** 35 ILCS 5/203(a)(2)(F).

### E-5: Illinois residency determination

Illinois uses a "place of abode" test, not a day-count test. If a taxpayer maintains a place of abode in Illinois and is present in Illinois for more than an aggregate of 12 months during a three-year period, they are presumed to be an Illinois resident. **Source:** 35 ILCS 5/1501(a)(20).

### E-6: Gambling winnings

Illinois does not allow a subtraction for gambling losses. If federal AGI includes net gambling winnings (after losses are deducted as federal itemized deductions), the Illinois computation starts from AGI which includes gross gambling winnings. The losses deducted federally as itemized deductions do not reduce IL base income.

---

## Section 6 -- Test suite

### Test 1: Standard freelancer, single

- **Input:** Federal AGI: $100,000 (all Schedule C). No additions. Social Security subtraction: $0. No property tax. Single, no dependents.
- **Expected:** Base income: $100,000. Exemption: $2,850. Net income: $97,150. Tax: $97,150 x 4.95% = $4,808.93.

### Test 2: MFJ with property tax credit

- **Input:** Federal AGI: $150,000. No modifications. MFJ, 2 dependents. Property taxes paid: $8,000.
- **Expected:** Exemptions: $5,700 + (2 x $2,850) = $11,400. Net income: $138,600. Tax: $138,600 x 4.95% = $6,860.70. Property tax credit: $8,000 x 5% = $400. Net tax: $6,460.70.

### Test 2b: High-income exemption + credit phase-out (cliff)

- **Input:** Federal AGI: $520,000. MFJ, 2 dependents. Property taxes paid: $12,000.
- **Expected:** AGI exceeds the $500,000 MFJ threshold, so exemption = $0 AND the property tax credit is disallowed. Net income: $520,000. Tax: $520,000 x 4.95% = $25,740.00. No property tax credit. (If AGI were $499,000 the full $11,400 exemption and $600 property tax credit would apply.)

### Test 3: Bonus depreciation add-back

- **Input:** Federal AGI includes $50,000 of bonus depreciation on a $50,000 asset (5-year MACRS). Year 1.
- **Expected:** Addition: $50,000. Subtraction: $10,000 (year 1 standard MACRS on 5-year property). Net addition: $40,000. Track remaining $40,000 as future IL subtractions.

### Test 4: Social Security subtraction

- **Input:** Federal AGI: $60,000 including $12,000 of Social Security benefits taxed federally.
- **Expected:** Subtraction: $12,000. IL base income: $48,000.

### Test 5: Earned income credit

- **Input:** Federal EIC: $2,000. Single, 1 child.
- **Expected:** IL EIC: $2,000 x 20% = $400 (refundable).

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT apply a standard deduction or itemized deductions to Illinois income. Only the personal exemption applies.
- **P-2:** Do NOT carry forward federal NOLs into Illinois without checking the $100,000 IL net loss limitation.
- **P-3:** Do NOT assume bonus depreciation flows through. Illinois requires the add-back.
- **P-4:** Do NOT tax Social Security benefits for Illinois purposes.
- **P-5:** Do NOT file a separate Illinois extension form if the taxpayer has a federal extension.
- **P-6:** Do NOT use graduated brackets. Illinois has a flat 4.95% rate.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Federal AGI correctly transcribed from Form 1040, Line 11
- [ ] All Schedule M additions identified (especially bonus depreciation)
- [ ] All Schedule M subtractions identified (especially Social Security, gov't bond interest)
- [ ] AGI phase-out checked FIRST — exemption and ICR credits zeroed if AGI > $250k/$500k
- [ ] Personal exemptions correctly computed ($2,850 x number of exemptions, + $1,000 age/blind)
- [ ] Flat rate of 4.95% applied
- [ ] Property tax credit at 5% (non-refundable, disallowed above AGI cap)
- [ ] EIC at 20% of federal EIC (refundable)
- [ ] No standard deduction applied
- [ ] Net loss limitation of $100,000 checked
- [ ] Reviewer brief includes all positions and flags

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

---

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://www.openaccountants.com/network).

<!-- openaccountants-mcp-cta -->

## The accountant-verified version lives in the connector

This file is the open, **research-grade draft**. The **accountant-verified**
version of this skill is **not published to GitHub** — it is delivered free
through the OpenAccountants MCP connector, where your AI agent loads the
verified rules together with the name of the accountant who signed them off.

**→ Install the free connector:** <https://www.openaccountants.com/connect>
**MCP endpoint:** `https://www.openaccountants.com/api/mcp`
