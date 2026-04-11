---
name: ca-540-individual-return
description: Tier 2 content skill for preparing California Form 540 (Resident Income Tax Return) for US sole proprietors and single-member LLCs who are California residents. Covers tax year 2025 California personal income tax including the Schedule CA (540) decoupling adjustments from federal AGI, California's non-conformity with OBBBA bonus depreciation and section 174 R&E expensing, the nine-bracket rate structure (1% through 12.3% plus the 1% Mental Health Services Tax surcharge above $1M), standard and itemized deductions, California tax credits (renter's credit, CalEITC, young child tax credit), SDI/VPDI deduction, and California's own AMT. Defers estimated tax to ca-estimated-tax-540es, SMLLC franchise tax to ca-smllc-form-568, and health coverage mandate to ca-form-3853-coverage. MUST be loaded alongside us-tax-workflow-base v0.1 or later and us-federal-return-assembly. California full-year residents only.
version: 0.2
---

# CA 540 Individual Return Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides the California personal income tax computation rules for a full-year California resident sole proprietor or single-member LLC owner for tax year 2025. It does not provide workflow architecture -- that comes from the base. It does not compute California estimated tax (ca-estimated-tax-540es), SMLLC franchise tax (ca-smllc-form-568), or the individual mandate penalty (ca-form-3853-coverage) -- those are separate content skills.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). California did NOT conform to the One Big Beautiful Bill Act (OBBBA, P.L. 119-21) for several key provisions. All OBBBA decoupling points are documented in Section 5. For tax years before 2025, the skill must not be used without explicit verification. For tax years after 2025, bracket thresholds and standard deduction amounts will need updating.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) reviews and signs the return.

---

## Section 1 -- Scope statement

This skill covers California Form 540 (Resident Income Tax Return) for tax year 2025 for taxpayers who are:

- Full-year California residents, AND
- Sole proprietors filing federal Schedule C, OR single-member LLCs disregarded for federal tax

For the following kinds of work:

- Computing California adjusted gross income (CA AGI) from federal AGI using Schedule CA (540)
- Identifying California additions (add-backs) and subtractions from federal AGI
- Applying the nine-bracket California tax rate schedule
- Applying the 1% Mental Health Services Tax (MHST) on taxable income above $1,000,000
- Determining standard deduction vs. itemized deductions (California-specific rules)
- Computing California tax credits (renter's credit, CalEITC, young child tax credit, and others)
- Computing California Alternative Minimum Tax (AMT) where applicable
- Producing the Form 540 worksheet for the reviewer

This skill does NOT cover:

- California estimated tax payments -- handled by `ca-estimated-tax-540es`
- Form 568 SMLLC return -- handled by `ca-smllc-form-568`
- Health coverage individual mandate -- handled by `ca-form-3853-coverage`
- Part-year residents or nonresidents (Form 540NR)
- Multi-state apportionment
- Community property adjustments for RDP/same-sex couples (flag for reviewer)
- Any federal computation -- those are upstream

---

## Section 2 -- Year coverage and currency

**Tax year covered:** 2025 (California returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** April 2026.

**Legislation reflected:**
- California Revenue and Taxation Code (R&TC) as in force for tax year 2025
- SB 78 (2019) -- California individual mandate (Form 3853, handled by companion skill)
- California's conformity position with the Internal Revenue Code as of January 1, 2015, with specified modifications (R&TC section 17024.5)
- FTB Publication 1001 (2025) -- Supplemental Guidelines to California Adjustments
- FTB Form 540 Instructions (2025)
- FTB Schedule CA (540) Instructions (2025)
- FTB Notice 2025-XX (2025 inflation adjustments) -- (verify exact notice number)

**Currency limitations:**
- California conformity to the IRC is generally fixed at January 1, 2015 with selective post-2015 conformity enacted by specific California legislation. OBBBA provisions (July 4, 2025) are NOT conformed to unless California enacts separate legislation. As of the currency date, no such legislation has been enacted.
- Some 2025 inflation-adjusted figures (brackets, standard deduction) are based on FTB announcements. Where the FTB has not yet published final figures, the skill uses projected amounts and flags them with "(verify 2025)".

---

## Section 3 -- Year-specific figures table for tax year 2025

All dollar thresholds, rates, and indexed figures in one place.

### Tax rate schedule -- Single, Head of Household, Married Filing Separately (verify 2025)

| Bracket | Taxable income range (Single) | Rate |
|---|---|---|
| 1 | $0 -- $10,756 | 1% |
| 2 | $10,757 -- $25,499 | 2% |
| 3 | $25,500 -- $40,245 | 4% |
| 4 | $40,246 -- $55,866 | 6% |
| 5 | $55,867 -- $70,612 | 8% |
| 6 | $70,613 -- $360,659 | 9.3% |
| 7 | $360,660 -- $432,791 | 10.3% |
| 8 | $432,792 -- $721,314 | 11.3% |
| 9 | $721,315 and above | 12.3% |
| MHST | Above $1,000,000 | +1% (13.3% effective marginal) |

**Note:** Married Filing Jointly brackets are double the single brackets. The $1,000,000 MHST threshold is statutory and NOT doubled for MFJ. (verify 2025 -- historically California has NOT doubled the MHST threshold for MFJ; confirm current status.)

### Standard deduction (verify 2025)

| Filing status | Standard deduction |
|---|---|
| Single / MFS | $5,540 |
| MFJ / QSS / HOH | $11,080 |

### California personal exemption credit (verify 2025)

| Filing status | Exemption credit |
|---|---|
| Single / MFS | $144 |
| MFJ / QSS | $288 |
| Each dependent | $433 |

### Renter's credit (verify 2025)

| Filing status | Credit amount | CA AGI limit |
|---|---|---|
| Single / HOH / MFS | $60 | $50,746 |
| MFJ / QSS | $120 | $101,492 |

### CalEITC (verify 2025)

| Figure | Value |
|---|---|
| Maximum earned income | $30,950 |
| Maximum credit (3+ children) | ~$3,529 |

### Young Child Tax Credit (YCTC) (verify 2025)

| Figure | Value |
|---|---|
| Maximum credit per qualifying child under 6 | $1,117 |
| Income phaseout | Tied to CalEITC eligibility |

### California AMT

| Figure | Value |
|---|---|
| AMT rate | 7% (flat rate on AMTI less exemption) |
| Exemption (single) | $93,666 (verify 2025) |
| Exemption (MFJ) | $124,876 (verify 2025) |
| Exemption phaseout rate | 25% of AMTI above threshold |

### SDI/VPDI (verify 2025)

| Figure | Value |
|---|---|
| SDI rate | 1.1% |
| SDI taxable wage ceiling | $153,164 (verify 2025) |
| Maximum SDI withholding | $1,684.80 (verify 2025) |
| SDI deductibility on CA return | Deductible as itemized deduction (not above-the-line) |

---

## Section 4 -- Primary source library

| Source | Use |
|---|---|
| R&TC section 17041 | Tax rate schedule |
| R&TC section 17043 | Mental Health Services Tax (1% above $1M) |
| R&TC section 17024.5 | IRC conformity date and modifications |
| R&TC section 17201 et seq. | Itemized deductions |
| R&TC section 17052 | CalEITC |
| R&TC section 17052.1 | Young Child Tax Credit |
| R&TC section 17053.5 | Renter's credit |
| R&TC sections 17062, 17063 | Standard deduction |
| R&TC section 17039 | Credit limitation (no credit reduces tax below tentative minimum tax) |
| R&TC sections 17061, 17062 | Personal exemption credits |
| R&TC section 17220 | SDI/VPDI deduction |
| R&TC sections 17750-17756 | California AMT |
| FTB Publication 1001 | Supplemental Guidelines to California Adjustments |
| FTB Publication 1005 | Pension and Annuity Guidelines |
| FTB Form 540 Booklet (2025) | Line-by-line instructions |
| Schedule CA (540) Instructions (2025) | Addition and subtraction adjustments |

---

## Section 5 -- Schedule CA (540): Federal-to-California adjustments

This is the critical section. California starts with federal AGI and adjusts it. Every OBBBA decoupling item must be identified and added back.

### 5.1 -- California non-conformity with OBBBA (critical)

California conforms to the IRC generally as of January 1, 2015, with selective updates. California has NOT enacted conformity legislation for OBBBA (P.L. 119-21). The following OBBBA provisions claimed on the federal return must be ADDED BACK on Schedule CA (540):

| Federal OBBBA provision | CA treatment | Schedule CA column |
|---|---|---|
| 100% bonus depreciation for property acquired after Jan 19, 2025 (OBBBA restored §168(k)) | CA does not conform. Use pre-OBBBA phase-down (40% for 2025). Add back the excess (60% of the bonus claimed federally). | Column B addition |
| §174 R&E expensing (if OBBBA modified the TCJA amortization requirement) | CA follows its own R&TC section 17024.5 conformity. If federal allows immediate expensing and CA requires 5-year amortization, add back the difference. | Column B addition |
| §179 expensing limit increase to $2,500,000 (OBBBA) | CA §179 limit is $25,000 with $200,000 phase-out (R&TC §17255). Add back excess over CA limit. | Column B addition |
| QBI deduction at 20% (§199A, made permanent by OBBBA) | CA does not allow the QBI deduction. Add back entire federal QBI deduction. | Column B addition |
| New tip income exclusion (OBBBA) | CA does not conform. Add back any excluded tip income. | Column B addition |
| New overtime income exclusion (OBBBA) | CA does not conform. Add back any excluded overtime income. | Column B addition |
| New auto loan interest deduction (OBBBA) | CA does not conform. Add back any deducted auto loan interest. | Column B addition |
| New senior standard deduction (OBBBA) | CA uses its own standard deduction. No adjustment needed if using CA standard deduction; if using federal itemized and the senior provision affected itemized amounts, reconcile. | Varies |

### 5.2 -- Pre-OBBBA non-conformity items (ongoing)

| Federal item | CA treatment |
|---|---|
| Federal QBI deduction (§199A) | Not allowed in CA. Full add-back. |
| HSA deduction (§223) | CA does not conform to federal HSA rules. Add back HSA deduction; HSA contributions and earnings are taxable in CA. |
| Federal bonus depreciation (§168(k)) at rates above CA allowance | Add back excess. CA allowed 0% bonus for many years; check CA conformity for 2025. |
| §179 excess over CA limit ($25,000) | Add back. |
| SALT deduction cap ($10,000 federal under TCJA, modified by OBBBA) | CA has NO SALT cap. If taxpayer itemizes on CA return, full state/local taxes (other than CA income tax) are deductible. But CA income tax is never deductible on the CA return. |
| Mortgage interest (federal $750K limit) | CA conforms to $1,000,000 limit (pre-TCJA). If mortgage exceeds $750K but is under $1M, the disallowed federal interest is a CA subtraction. |
| Net operating loss | CA has its own NOL rules. CA NOL may differ from federal NOL. |
| Educator expenses | CA conforms (verify 2025). |
| Student loan interest | CA conforms (verify 2025). |
| Moving expenses (military only federally) | CA allows moving expenses for all taxpayers (not just military). Subtraction for non-military movers. |

### 5.3 -- Common subtractions (federal income taxed, CA excludes)

| Item | CA treatment |
|---|---|
| Social Security benefits | Not taxable in CA. Subtract any amount included in federal AGI. |
| Railroad Retirement benefits (Tier 1) | Not taxable in CA. Subtract. |
| CA lottery winnings | Not taxable in CA. Subtract. |
| Military pay for active duty outside CA | Subtract under Servicemembers Civil Relief Act. |

---

## Section 6 -- Deduction computation

### 6.1 -- Standard vs. itemized

The taxpayer may choose independently for California. A taxpayer who itemizes federally may take the CA standard deduction, and vice versa. However:

- If MFS and spouse itemizes, the other spouse MUST also itemize on the CA return (R&TC section 17073.5).
- CA standard deduction is much lower than federal ($5,540 single vs. $15,000 federal for 2025). Most self-employed taxpayers with mortgage interest, property tax, or charitable contributions will benefit from itemizing on the CA return.

### 6.2 -- Itemized deduction differences from federal

| Deduction | Federal rule | CA rule |
|---|---|---|
| State and local income tax | $10,000 SALT cap (TCJA/OBBBA) | Not deductible (cannot deduct CA income tax on CA return). Other states' income tax IS deductible. |
| Property tax | Subject to $10,000 SALT cap | Fully deductible (no SALT cap in CA) |
| Mortgage interest | $750,000 acquisition debt limit | $1,000,000 acquisition debt limit (R&TC section 17220) |
| Home equity interest | Not deductible unless used for acquisition | Same as federal |
| Charitable contributions | Up to 60% AGI (cash to public charities) | Same as federal (CA conforms) |
| Medical expenses | Above 7.5% of AGI | Above 7.5% of AGI (CA conforms) |
| Casualty losses | Only federally declared disasters | CA allows CA-declared disaster losses too |
| Investment interest | Limited to net investment income | Same as federal |
| Gambling losses | Limited to gambling winnings | Same as federal |
| Miscellaneous itemized (2% floor) | Suspended by TCJA through 2025 | CA ALLOWS the 2% miscellaneous itemized deduction (CA did not conform to TCJA suspension). Employee business expenses, tax prep fees, etc. are deductible on the CA return subject to 2% AGI floor. |

---

## Section 7 -- Tax computation

### 7.1 -- Regular tax

1. Start with California taxable income (CA AGI minus deductions minus exemption credits basis).
2. Apply the nine-bracket rate schedule from Section 3.
3. Subtract personal exemption credits.
4. Result is regular tax before credits.

### 7.2 -- Mental Health Services Tax (MHST)

- 1% surcharge on California taxable income exceeding $1,000,000. (R&TC section 17043)
- The $1,000,000 threshold is NOT indexed for inflation.
- The $1,000,000 threshold is NOT doubled for MFJ. Each spouse's income is NOT measured separately -- it is based on the joint taxable income.
- MHST appears on Form 540 Line 62 (verify 2025 line reference).

### 7.3 -- California AMT

California has its own AMT computed on Schedule P (540):

1. Start with California taxable income.
2. Add back AMT preference items (accelerated depreciation, ISO exercises, tax-exempt interest from private activity bonds, etc.).
3. Subtract the AMT exemption (see Section 3).
4. Apply the flat 7% CA AMT rate.
5. AMT = excess of tentative minimum tax over regular tax.
6. AMT is in addition to regular tax and MHST.

**Key AMT triggers for sole proprietors:**
- Large §179 or depreciation differences (CA §179 limit is $25,000 vs. federal $2,500,000)
- ISO stock option exercises
- Tax-exempt interest from out-of-state private activity bonds

### 7.4 -- Tax credits

Apply credits in the following order (R&TC section 17039):

1. **Nonrefundable credits** (reduce tax to zero but not below):
   - Personal exemption credits ($144 single, $288 MFJ, $433 per dependent) -- (verify 2025)
   - Renter's credit ($60 single / $120 MFJ if CA AGI below threshold)
   - Child and dependent care credit (CA version)
   - Other nonrefundable credits

2. **Refundable credits** (can generate a refund):
   - CalEITC (California Earned Income Tax Credit)
   - Young Child Tax Credit (YCTC)
   - Foster Youth Tax Credit (FYTC)

**CalEITC notes:**
- Available to taxpayers with earned income from wages or self-employment.
- Self-employment income DOES qualify for CalEITC (unlike some state EITCs).
- Must file a CA return to claim even if no CA tax is owed.
- ITIN filers are eligible (CA allows CalEITC for ITIN filers).

---

## Section 8 -- SDI / VPDI deduction

- SDI (State Disability Insurance) or VPDI (Voluntary Plan Disability Insurance) withheld from wages is deductible as an itemized deduction on the CA return.
- SDI/VPDI is NOT deductible on the federal return (it is a state tax, subject to SALT cap federally, but on the CA return it gets its own treatment).
- If the taxpayer takes the CA standard deduction, SDI/VPDI is not separately deductible.
- For self-employed taxpayers who are also W-2 employees, SDI withheld from the W-2 job flows to Schedule CA as an itemized deduction.

---

## Section 9 -- PROHIBITIONS

**P-540-1.** NEVER apply the federal QBI deduction on the California return. California does not allow §199A. The full QBI amount must be added back on Schedule CA.

**P-540-2.** NEVER use federal bonus depreciation rates on the California return without adjustment. California's §179 limit is $25,000 (not $2,500,000), and bonus depreciation conformity must be verified against R&TC section 17250.

**P-540-3.** NEVER assume California conforms to OBBBA. As of the currency date, California has not enacted OBBBA conformity legislation. Every OBBBA-specific federal deduction or exclusion must be evaluated for CA add-back.

**P-540-4.** NEVER deduct California state income tax as an itemized deduction on the California return. Only other states' income taxes are deductible on Schedule CA.

**P-540-5.** NEVER double the $1,000,000 MHST threshold for MFJ filers. The threshold is $1,000,000 regardless of filing status.

**P-540-6.** NEVER exclude HSA contributions or earnings from California income. California does not conform to IRC section 223. HSA contributions are added back, and HSA earnings are taxable in California.

**P-540-7.** NEVER apply the federal $10,000 SALT cap on the California return. California has no SALT cap for its own itemized deduction computation.

**P-540-8.** NEVER skip the Schedule CA reconciliation. Every federal-to-California adjustment must be documented and traced.

**P-540-9.** NEVER compute AMT using the federal AMT rate (26%/28%). California AMT is a flat 7%.

**P-540-10.** NEVER exclude Social Security benefits from the CA subtraction analysis. Social Security is fully exempt from CA tax and must be subtracted from federal AGI on Schedule CA.

---

## Section 10 -- Edge Cases

### EC-540-1 -- Taxpayer with large OBBBA bonus depreciation claim

**Situation:** Sole proprietor purchased $200,000 of equipment on March 1, 2025 and claimed 100% bonus depreciation ($200,000) on the federal return under OBBBA-restored §168(k).

**Resolution:**
- Federal deduction: $200,000 (100% bonus).
- CA allowable: 40% bonus = $80,000 (pre-OBBBA phase-down schedule for 2025). (verify 2025 CA bonus rate)
- Schedule CA addition: $120,000.
- CA must also track the remaining $120,000 basis for future CA depreciation deductions (Schedule D-1 or equivalent).
- **Flag for reviewer:** Confirm CA bonus depreciation rate for assets placed in service in 2025.

### EC-540-2 -- High-income freelancer triggers MHST

**Situation:** Single filer with CA taxable income of $1,200,000.

**Resolution:**
- Regular tax computed on nine brackets through 12.3%.
- MHST: 1% x ($1,200,000 - $1,000,000) = $2,000.
- Total marginal rate on income above $1M = 13.3%.
- **Flag for reviewer:** Verify MHST threshold is still $1,000,000 for 2025 (statutory, not indexed).

### EC-540-3 -- MFJ couple with combined income just over $1M MHST threshold

**Situation:** MFJ with combined CA taxable income of $1,050,000. One spouse earns $900,000, the other $150,000.

**Resolution:**
- MHST applies based on JOINT taxable income, not per-spouse.
- MHST = 1% x ($1,050,000 - $1,000,000) = $500.
- The threshold is NOT doubled to $2,000,000 for MFJ.
- **Flag for reviewer:** Taxpayers near the $1M threshold should consider timing strategies (accelerate deductions, defer income).

### EC-540-4 -- HSA contributions add-back

**Situation:** Taxpayer contributed $4,300 to an HSA and deducted it on federal Form 1040 Line 13 (via Schedule 1).

**Resolution:**
- CA does not recognize HSAs. Add back $4,300 on Schedule CA Column B.
- HSA earnings (interest, dividends, capital gains inside the HSA) are also taxable in CA.
- Distributions for medical expenses: taxable in CA unless the expense was not already deducted.
- **Flag for reviewer:** Request HSA 1099-SA and 5498-SA to compute CA HSA income.

### EC-540-5 -- Mortgage interest difference ($750K vs $1M)

**Situation:** Taxpayer has a $900,000 mortgage (acquisition debt, pre-TCJA grandfathering does not apply). Federal deduction limited to interest on $750,000. CA allows interest on up to $1,000,000.

**Resolution:**
- Federal allowed: interest on $750,000 of the $900,000 mortgage.
- CA allowed: interest on $900,000 (under the $1M limit).
- Schedule CA subtraction: the disallowed federal interest (interest allocable to the $150,000 excess).
- **Flag for reviewer:** Calculate the exact pro-rata interest allocation.

### EC-540-6 -- Sole proprietor eligible for CalEITC

**Situation:** Low-income sole proprietor with $25,000 net self-employment income, no W-2 wages, single filer.

**Resolution:**
- CalEITC is available for self-employment income (net earnings from self-employment).
- Must have earned income within CalEITC range (up to $30,950 for 2025, verify).
- ITIN filers qualify.
- CalEITC is refundable -- taxpayer may owe zero CA tax and still receive the credit.
- Also check eligibility for Young Child Tax Credit if taxpayer has a child under 6.
- **Flag for reviewer:** Verify earned income computation for CalEITC matches Schedule C net profit.

### EC-540-7 -- 2% miscellaneous itemized deductions (CA allows, federal does not)

**Situation:** Taxpayer has $3,000 in unreimbursed employee business expenses (from a side W-2 job) and $1,500 in tax preparation fees. Federal AGI is $80,000.

**Resolution:**
- Federal: $0 deduction (TCJA suspended 2% miscellaneous itemized through 2025, and OBBBA did not restore).
- CA: 2% floor = $80,000 x 2% = $1,600. Total miscellaneous = $4,500. Deductible on CA = $4,500 - $1,600 = $2,900.
- Schedule CA subtraction: $2,900.
- **Flag for reviewer:** Verify that OBBBA did not change the federal suspension of 2% miscellaneous itemized deductions.

### EC-540-8 -- Social Security recipient with self-employment income

**Situation:** Taxpayer receives $18,000 in Social Security benefits (included in federal AGI per the 85% rule) and has $50,000 Schedule C net profit.

**Resolution:**
- Federal AGI includes up to 85% of Social Security = $15,300.
- CA: Social Security is 100% exempt. Subtract $15,300 on Schedule CA Column C.
- CA AGI = Federal AGI minus $15,300 (plus any other adjustments).
- **Flag for reviewer:** Confirm exact amount of Social Security included in federal AGI.

### EC-540-9 -- Taxpayer claims federal standard deduction but CA itemized is better

**Situation:** Single filer takes the federal standard deduction ($15,000) but has $8,000 in property taxes, $6,000 in mortgage interest, and $2,000 in charitable contributions.

**Resolution:**
- Federal: standard deduction is higher ($15,000 > $16,000 itemized less SALT cap complications).
- CA standard deduction: only $5,540.
- CA itemized: $8,000 property tax (fully deductible, no SALT cap) + $6,000 mortgage + $2,000 charitable = $16,000.
- Taxpayer should itemize on CA return ($16,000 > $5,540).
- The election is independent -- taxpayer CAN take federal standard and CA itemized.
- **Flag for reviewer:** Confirm independent election is optimal.

---

## Section 11 -- Test Suite

### Test 540-1 -- Basic single filer, no OBBBA complications

**Input:** Single, CA resident, federal AGI $85,000. No QBI. No bonus depreciation. No HSA. Standard deduction on CA return.
**Expected:** CA AGI = $85,000. CA taxable income = $85,000 - $5,540 = $79,460. Tax computed using brackets 1-6. Personal exemption credit of $144 applied. No MHST (under $1M).

### Test 540-2 -- QBI add-back

**Input:** Single, CA resident, federal AGI $120,000 after $20,000 QBI deduction. Actual Schedule C net profit = $100,000.
**Expected:** Federal AGI includes QBI deduction reducing taxable income, but CA AGI must add back the $20,000 QBI deduction on Schedule CA. CA AGI = federal AGI + $20,000 QBI add-back. (Note: QBI deduction is below-the-line federally on Line 13, so it does not affect federal AGI. The add-back occurs on the CA taxable income computation, not AGI.)

### Test 540-3 -- MHST computation

**Input:** Single, CA taxable income = $1,500,000.
**Expected:** Regular tax on $1,500,000 using nine brackets. MHST = 1% x ($1,500,000 - $1,000,000) = $5,000. Total tax = regular tax + $5,000 MHST.

### Test 540-4 -- HSA add-back plus SDI deduction

**Input:** Single, W-2 employee with side Schedule C. Federal AGI includes $4,300 HSA deduction. SDI withheld $1,684.80. Itemizing on CA return.
**Expected:** Add back $4,300 HSA on Schedule CA. SDI of $1,684.80 included in CA itemized deductions. Net CA AGI adjustment = +$4,300. Itemized deductions include SDI.

### Test 540-5 -- CalEITC with self-employment income

**Input:** Single, net self-employment income $22,000. One qualifying child age 4. No W-2 wages. ITIN filer.
**Expected:** Eligible for CalEITC based on $22,000 earned income. Eligible for Young Child Tax Credit (child under 6). Both credits are refundable. CA tax liability may be $0 with refundable credits generating a refund. ITIN status does not disqualify.

### Test 540-6 -- Independent deduction election (federal standard, CA itemized)

**Input:** Single, federal AGI $95,000. Takes federal standard deduction ($15,000). Has $9,000 property tax, $7,000 mortgage interest, $3,000 charitable.
**Expected:** CA standard deduction = $5,540. CA itemized = $9,000 + $7,000 + $3,000 = $19,000 (no SALT cap, no CA income tax deduction needed). Taxpayer should itemize on CA ($19,000 > $5,540). Federal and CA elections are independent.

### Test 540-7 -- Large §179 difference

**Input:** Single, claimed $500,000 §179 on federal return (within federal $2,500,000 limit). Equipment cost $500,000.
**Expected:** CA §179 limit = $25,000. Add back $475,000 on Schedule CA. CA must depreciate the remaining $475,000 using regular MACRS over the applicable recovery period. Track CA basis adjustment going forward.

---

## Section 12 -- Self-checks

**Check 200 -- Federal AGI flows to Schedule CA.** Verify that federal AGI on Schedule CA Line 37 matches the federal Form 1040 Line 11.

**Check 201 -- Every OBBBA add-back is documented.** For each OBBBA provision used on the federal return, verify a corresponding Schedule CA addition exists.

**Check 202 -- QBI deduction is added back.** If federal return claims QBI (Form 8995 or 8995-A), verify the full amount is added back on the CA return.

**Check 203 -- HSA add-back present if applicable.** If federal return includes an HSA deduction, verify it is added back on Schedule CA.

**Check 204 -- MHST computed if taxable income exceeds $1M.** If CA taxable income > $1,000,000, verify MHST of 1% on excess is included.

**Check 205 -- Standard vs. itemized deduction is optimal.** Verify the chosen deduction method produces the lower CA tax. Document if MFS forced itemization applies.

**Check 206 -- Social Security subtracted.** If federal AGI includes Social Security, verify it is subtracted on Schedule CA.

**Check 207 -- §179 and depreciation differences tracked.** If federal §179 or bonus depreciation exceeds CA limits, verify the add-back and the future-year CA depreciation schedule.

**Check 208 -- CalEITC and YCTC evaluated.** If CA earned income is within CalEITC range, verify credit was computed. If qualifying child under 6, verify YCTC.

**Check 209 -- CA AMT evaluated.** If large depreciation differences, ISO exercises, or private activity bond interest exist, verify Schedule P (540) was completed.

**Check 210 -- Filing status matches federal.** Verify CA filing status matches federal filing status (with limited exceptions for RDP).

---

## Section 13 -- Cross-skill references

**Inputs from:**
- `us-federal-return-assembly` -- federal AGI, federal tax, all federal positions
- `us-sole-prop-bookkeeping` -- Schedule C line items
- `us-schedule-c-and-se-computation` -- Schedule C net profit, depreciation details
- `us-qbi-deduction` -- QBI deduction amount for add-back
- `us-self-employed-health-insurance` -- SE health insurance deduction
- `us-self-employed-retirement` -- retirement contribution deduction

**Outputs to:**
- `ca-estimated-tax-540es` -- CA total tax for safe harbor computation
- `ca-form-3853-coverage` -- CA AGI for penalty computation
- `us-ca-return-assembly` -- Form 540 worksheet for final package

---

## Section 14 -- Known gaps

1. Part-year and nonresident returns (Form 540NR) are not supported.
2. Community property rules for RDP/same-sex couples require reviewer judgment.
3. California NOL carryforward/carryback rules are not fully detailed; flag for reviewer if taxpayer has prior-year CA NOLs.
4. Specific CA disaster loss rules beyond general casualty loss are not covered.
5. 2025 inflation-adjusted figures marked "(verify 2025)" must be confirmed against FTB final publications.
6. California legislative response to OBBBA may change before the filing deadline; monitor FTB announcements.

### Change log
- **v0.1 (April 2026):** Stub.
- **v0.2 (April 2026):** Full content skill with Schedule CA adjustments, OBBBA decoupling, brackets, credits, AMT, edge cases, and test suite.

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
