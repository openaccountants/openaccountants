---
name: il-estimated-tax
description: "Illinois Estimated Income Tax (Form IL-1040-ES) for self-employed individuals. Covers quarterly payment requirements, 4.95% flat rate computation, safe harbour rules, underpayment penalty calculation, and payment schedule. Primary source: 35 ILCS 5/803; 86 Ill. Admin. Code 100.8010."
version: 1.0
jurisdiction: US-IL
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Amir Pelinkovic
review_status: current
depends_on:
  - us-tax-workflow-base
category: state
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Estimated Tax

## Illinois Estimated Tax (IL-1040-ES) v1.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **a licensed accountant** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### IL Estimated Tax

- **Threshold** — $1,000 of expected IL tax after withholding/credits (TY ending on/after 12/31/2019); $500 was the prior threshold and now applies only to the PTE-tax election context  _(35 ILCS 5/803; IDOR Pub-105; IL-1040-ES instr.)_
- **Safe harbor — current year** — 90% of current-year liability  _(35 ILCS 5/803; IL-2210.)_
- **Safe harbor — prior year** — 100% of prior-year liability; IL has no high-income 110% rule  _(35 ILCS 5/803; IL-2210; IL-1040-ES instr.)_
- **110% rule** — Confirmed - IL uses 100% prior-year regardless of income  _(IL-2210 instr.)_
- **IL flat rate** — 4.95%  _(35 ILCS 5/201.)_
- **Personal exemption — Single** — $2,850 for 2025 (the same exemption applies to IL-1040, estimated tax, and withholding)  _(IDOR FY2025-16; IL-1040-ES instr.)_
- **Personal exemption — MFJ** — $5,700 for 2025  _(IDOR FY2025-16.)_
- **Q1** — April 15, 2025  _(2025 IL-1040-ES.)_
- **Q2** — Statutory June 15; June 15, 2025 falls on a Sunday, so the effective due date is June 16, 2025  _(2025 IL-1040-ES; 5 ILCS 70/1.11.)_
- **Q3** — September 15, 2025  _(2025 IL-1040-ES.)_
- **Q4** — January 15, 2026  _(2025 IL-1040-ES.)_
- **Instalment split** — Four equal 25% installments  _(IL-1040-ES; IL-2210.)_
- **Underpayment rate** — IL interest tracks the IRC 6621 underpayment rate (federal short-term + 3 points for individuals) and is set SEMI-ANNUALLY (Jan 1 and Jul 1), not federal short-term + 2% quarterly.  _(35 ILCS 735/3-2; IDOR Pub-103.)_
- **Estimated tax exemption** — IL-1040-ES uses $2,850 (S) / $5,700 (MFJ) for 2025 - the same as IL-1040  _(IDOR FY2025-16; IL-1040-ES instr.)_
- **Income tax exemption** — $2,850 (S) / $5,700 (MFJ)  _(IDOR FY2025-16.)_
- **VERIFY** — They do NOT differ: both IL-1040 and IL-1040-ES use $2,850 (S) / $5,700 (MFJ) for 2025. The $2,625/$5,250 figures in rows 8-9 and 19 are erroneous (older amounts).  _(IDOR FY2025-16.)_

## What this file is

**Obligation category:** ET (Estimated Tax)
**Functional role:** Computation
**Status:** Complete

This is a Tier 2 content skill for computing quarterly estimated Illinois income tax payments for sole proprietors and single-member LLCs. Illinois imposes a flat 4.95% income tax rate with no brackets, which simplifies the estimated tax computation relative to graduated-rate states.

## Section 1 -- Scope statement

**In scope:**

- Form IL-1040-ES quarterly estimated tax payments
- Sole proprietors and single-member LLCs (disregarded entities)
- Safe harbour rules to avoid underpayment penalty
- Underpayment penalty computation (Form IL-2210)
- Interaction with federal estimated tax payments

**Out of scope (refused):**

- Partnerships, S-corps, C-corps
- Pass-through withholding (Form IL-1000)
- Composite returns
- Non-resident estimated tax
- Amended estimated payments after audit adjustments

## Section 2 -- Filing requirements

### Who must make estimated payments

- **Estimated payment requirement** — An individual must make estimated payments if: 1. The taxpayer expects to owe $500 or more in Illinois income tax after subtracting Illinois withholding and credits, AND 2. The taxpayer expects Illinois withholding and credits to be less than the smaller of: (a) 90% of the current year tax liability, or (b) 100% of the prior year tax liability.  _(35 ILCS 5/803(a); 86 Ill. Admin. Code 100.8010.)_

### Payment schedule

**Payment schedule**  _(35 ILCS 5/803(b))_

| Installment | Period covered | Due date | Source |
| --- | --- | --- | --- |
| 1st quarter | Jan 1 -- Mar 31 | April 15, 2025 | 35 ILCS 5/803(b) |
| 2nd quarter | Apr 1 -- May 31 | June 15, 2025 | 35 ILCS 5/803(b) |
| 3rd quarter | Jun 1 -- Aug 31 | September 15, 2025 | 35 ILCS 5/803(b) |
| 4th quarter | Sep 1 -- Dec 31 | January 15, 2026 | 35 ILCS 5/803(b) |

Illinois follows the same quarterly schedule as the IRS.

## Section 3 -- Rates and thresholds

**Rates and thresholds**  _(35 ILCS 5/201(b)(5.4); 35 ILCS 5/803(a); 35 ILCS 5/204 (2025); 35 ILCS 5/804; 35 ILCS 5/804(c))_

| Item | Amount | Source |
| --- | --- | --- |
| Illinois flat income tax rate | 4.95% | 35 ILCS 5/201(b)(5.4) |
| Estimated tax threshold | $500 | 35 ILCS 5/803(a) |
| Personal exemption | $2,625 (single); $5,250 (MFJ) | 35 ILCS 5/204 (2025) |
| Safe harbour -- current year | 90% of current year tax | 35 ILCS 5/804 |
| Safe harbour -- prior year | 100% of prior year tax | 35 ILCS 5/804 |
| Underpayment penalty rate | Varies (set by IDOR quarterly, tied to federal short-term rate + 2%) | 35 ILCS 5/804(c) |

**Note:** Illinois does NOT have a 110% prior-year safe harbour for high-income taxpayers as the IRS does. The prior-year safe harbour is always 100%.

## Section 4 -- Computation rules (Step format)

### Step 1: Estimate current year Illinois taxable income

0. **Step 1** — 1. Start with expected federal adjusted gross income (AGI). 2. Add Illinois addition modifications (Schedule M, Line 3): e.g., interest from non-Illinois state/local bonds, any bonus depreciation add-back per Illinois decoupling from IRC §168(k). 3. Subtract Illinois subtraction modifications (Schedule M, Line 16): e.g., U.S. government bond interest, Illinois income tax refunds included in federal AGI, Illinois retirement income subtraction (if applicable). 4. Result = Illinois base income.

### Step 2: Subtract personal exemption

0. **Step 2** — - Single/HoH: $2,625 - MFJ: $5,250 - MFS: $2,625 - Result = Illinois net income (equivalent to Illinois taxable income for individuals).

### Step 3: Compute estimated annual tax

- **Estimated annual tax formula** — Illinois net income x 4.95% = estimated annual Illinois income tax.  _(35 ILCS 5/201)_

### Step 4: Subtract credits and withholding

0. **Step 4** — - Subtract expected Illinois withholding (from W-2 jobs, if any). - Subtract the Illinois Property Tax Credit (5% of property taxes paid on principal residence). - Subtract the Illinois Earned Income Credit (20% of federal EIC for 2025). - Subtract any other applicable credits. - Result = net estimated tax liability.

### Step 5: Determine if estimated payments are required

0. **Step 5** — If the result from Step 4 is $500 or more, estimated payments are required.

### Step 6: Determine safe harbour amount

0. **Step 6** — The required annual payment is the lesser of: - 90% of the current year estimated tax (from Step 4), OR - 100% of the prior year Illinois tax liability (from the prior year IL-1040).

### Step 7: Compute quarterly payment

0. **Step 7** — Divide the required annual payment by 4. Each quarterly installment is 25% of the annual amount.

### Step 8: Adjust for annualized income (if applicable)

0. **Step 8** — If income is not earned evenly throughout the year, the taxpayer may use the annualized income installment method (Form IL-2210, Section B) to reduce early-quarter payments. This requires demonstrating that income was concentrated in later quarters.

## Section 5 -- Edge cases and special rules

### E-1: Part-year residents

- **Part-year residents** — Part-year residents must estimate tax only on income earned during the period of Illinois residency plus Illinois-source income earned while a non-resident. Use Schedule NR to allocate.  _(unsure)_

### E-2: Bonus depreciation add-back

- **Bonus depreciation add-back** — Illinois does not conform to federal IRC §168(k) bonus depreciation. Illinois requires an add-back of the bonus depreciation amount and allows the standard MACRS depreciation instead. This affects the estimated tax base.  _(35 ILCS 5/203(a)(2)(D-25).)_

### E-3: No estimated payment vouchers needed for e-pay

- **E-pay vouchers** — Illinois allows estimated payments via MyTax Illinois (mytax.illinois.gov) without submitting Form IL-1040-ES vouchers. If paying electronically, retain confirmation numbers.  _(unsure)_

### E-4: Prior year had no tax liability

- **Prior year zero liability** — If the taxpayer's prior year Illinois tax liability was zero (e.g., first year of self-employment with no IL-1040 filed), the prior-year safe harbour is $0. The taxpayer must pay 90% of the current year tax to avoid penalties.  _(unsure)_

### E-5: Fiscal year taxpayers

- **Fiscal year taxpayers** — Fiscal year taxpayers follow the same quarterly pattern but shifted to match their fiscal year. Payments are due on the 15th day of the 4th, 6th, 9th, and 1st months of the following fiscal year.  _(unsure)_

### E-6: Overpayment from prior year applied

- **Overpayment applied** — If an overpayment from the prior year IL-1040 was applied to estimated taxes, this amount reduces the first quarter estimated payment. Document the amount applied.  _(unsure)_

## Section 6 -- Test suite

### Test 1: Standard freelancer

- **Input:** Single filer, IL resident all year. Expected net income from Schedule C: $100,000. No withholding. No credits other than personal exemption.
- **Expected:** IL taxable income: $100,000 - $2,625 = $97,375. Tax: $97,375 x 4.95% = $4,820.06. Quarterly payment: $4,820.06 / 4 = $1,205.02 per quarter.

### Test 2: Below threshold

- **Input:** Part-year freelancer. Expected IL taxable income: $8,000. Tax: $8,000 x 4.95% = $396. With withholding of $0.
- **Expected:** $396 < $500 threshold. No estimated payments required.

### Test 3: Safe harbour using prior year

- **Input:** Current year estimated tax: $6,000. Prior year IL tax: $4,000.
- **Expected:** Safe harbour = lesser of ($6,000 x 90% = $5,400) or ($4,000 x 100% = $4,000). Required annual payment: $4,000. Quarterly: $1,000.

### Test 4: MFJ with W-2 withholding

- **Input:** MFJ. Combined income: $150,000. W-2 withholding (spouse): $3,200. Estimated tax: ($150,000 - $5,250) x 4.95% = $7,170.23. Net after withholding: $7,170.23 - $3,200 = $3,970.23.
- **Expected:** $3,970.23 > $500. Quarterly: $3,970.23 / 4 = $992.56.

### Test 5: Property tax credit

- **Input:** Single filer, IL taxable income $80,000. Property taxes paid: $6,000.
- **Expected:** Tax: ($80,000 - $2,625) x 4.95% = $3,830.06. Property tax credit: $6,000 x 5% = $300. Net: $3,530.06. Quarterly: $882.52.

## Section 7 -- Prohibitions

- **P-1:** Do NOT apply the federal 110% safe harbour for high-income taxpayers. Illinois uses 100% for all taxpayers.
- **P-2:** Do NOT include bonus depreciation in the Illinois income estimate without adding it back.
- **P-3:** Do NOT skip estimated payments because the taxpayer expects a large 4th quarter adjustment. Each quarter's payment is independently required.
- **P-4:** Do NOT advise on penalty abatement requests. That is a procedural matter outside this skill's scope.

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Federal AGI correctly adjusted for Illinois modifications (Schedule M)
- [ ] Flat rate of 4.95% applied (not a graduated rate)
- [ ] Personal exemption of $2,625 (single) or $5,250 (MFJ) deducted
- [ ] $500 threshold applied to determine filing requirement
- [ ] Safe harbour computed using the lesser of 90% current / 100% prior
- [ ] 100% prior year rule used (not 110%)
- [ ] Bonus depreciation add-back included if applicable
- [ ] Property tax credit at 5% included if applicable
- [ ] Quarterly payments divided evenly (25% each)

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
