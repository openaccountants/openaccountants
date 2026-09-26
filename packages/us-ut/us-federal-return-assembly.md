---
name: us-federal-return-assembly
description: Tier 2 orchestrator skill that assembles the complete federal income tax return package for US freelance software developers filing as sole proprietors or single-member LLCs disregarded for federal tax. Sequences the upstream content skills (bookkeeping, SE computation, retirement, SE health insurance, QBI, estimated tax) in dependency order, resolves circular computations between SE health insurance and retirement contributions, produces Form 1040 with all required schedules (Schedule 1, Schedule 2, Schedule 3, Schedule C, Schedule SE, Schedule D if needed, Form 8829, Form 4562, Form 8995 or 8995-A, Form 8962 if marketplace coverage, Form 2210 if penalty, Form 7206), performs cross-form reconciliation checks, and produces the final reviewer package. Does not itself compute tax amounts — delegates to upstream content skills. MUST be loaded alongside us-tax-workflow-base v0.2 or later and all content skills it orchestrates. Federal only.
version: 0.2
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Federal Return Assembly

## Scope and who this is for

Figures are for tax year 2026, with a dated section for 2025 returns (due April 15, 2026, or October 15, 2026 on extension). This Guide sets the **order** for putting together a federal Form 1040 package for a US freelancer: a sole proprietor, or a single-member LLC that is disregarded for federal tax and reports on Schedule C. It covers how amounts flow between Schedule C, Schedule SE, Schedule 1, Schedule 1-A, Form 7206, Form 8995 or 8995-A, Schedules 2 and 3, and Form 2210. It also covers the ties to check before anyone signs.

It is an assembly method, not a substitute for the detailed rules. These related Guides go deeper and are optional to consult: `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-self-employed-retirement`, `us-self-employed-health-insurance`, `us-qbi-deduction`, `us-quarterly-estimated-tax`, `us-1099-k-and-payment-processors`, `us-capital-gains` and `us-form-1040-individual-return`. Federal only. For a California resident, see `ca-540-individual-return` for the state return.

Form line numbers below are from the **2025** forms. The 2026 forms may renumber lines, so check the 2026 form before relying on a line number.

## Ask the client first

- Filing status, and dates of birth for the taxpayer and spouse. The senior deduction and the additional standard deduction depend on age at year-end. Has anyone claimed the taxpayer as a dependent?
- Does every person on the return have a valid social security number? The tips, overtime and senior deductions need one, and married taxpayers must file jointly to claim them.
- Every source of self-employment income. More than one Schedule C, or a partnership, changes the Form 7206 and QBI work.
- Every Form 1099-NEC, 1099-MISC and 1099-K, reconciled to the books. Income is reportable whether or not a form arrived.
- Wages and Form W-2 box 12 codes. A W-2 matters for the social security wage base, for eligibility for an employer health plan, and for overtime or tips.
- Health coverage by month: who was covered, who paid, whether it was Marketplace coverage with advance premium tax credit (Form 1095-A), and any month when anyone was **eligible** for a subsidized plan through the taxpayer's employer, the spouse's employer, or the employer of a dependent or of a child under 27 at year-end, even if nobody took it.
- The retirement plan type (SEP, solo 401(k), SIMPLE, IRA), the date it was set up, and the amounts and dates contributed.
- Estimated payments made for the year (dates and amounts), any overpayment applied from the prior year, and the prior year's total tax and AGI (needed for the safe harbour).
- Capital gains, qualified dividends, rental income, K-1s, foreign income or accounts, and digital-asset activity. Each may take the return outside this Guide; see "When to refuse or refer".
- State residency for the year, for the state handoff.

## The method, step by step

1. **Close the books and finish Schedule C.** Reconcile gross receipts to bank deposits and to every 1099. Separate owner transfers, loans and personal items. Classify expenses and compute Schedule C line 31 net profit. Do Form 8829 (home office) and Form 4562 (depreciation) inside this step, because they change line 31.
2. **Compute Schedule SE.** Line 31 feeds Schedule SE line 2. Schedule SE line 12 goes to Schedule 2 line 4, and line 13 (half of SE tax) goes to Schedule 1 line 15. Do this before anything that depends on "net earnings".
3. **Compute the self-employed retirement deduction** (Schedule 1 line 16). The base for a SEP or the employer side of a solo 401(k) is net profit **minus the deductible half of SE tax minus the contribution itself**. Do not subtract the self-employed health insurance deduction.
4. **Compute the self-employed health insurance deduction** (Schedule 1 line 17). Its limit is net profit minus the deductible part of SE tax, minus the retirement deduction for the same business (Form 7206 lines 4 to 10). That is why step 3 must come first. If Marketplace coverage had advance premium tax credit, use the Pub. 974 method (step 5).
5. **Marketplace coverage only: resolve the premium tax credit.** The health insurance deduction and the premium tax credit depend on each other. This is the only true loop in the return. Use the Simplified Calculation Method or the Iterative Calculation Method in Pub. 974, then complete Form 8962.
6. **Finish Schedule 1** (HSA, IRA, student loan interest, other adjustments). Then Form 1040 line 11a (AGI) = line 9 total income − line 10 adjustments.
7. **Take the larger of the standard deduction or itemized deductions** (line 12e). If itemizing, apply the SALT limit on Schedule A.
8. **Complete Schedule 1-A** (tips, overtime, car loan interest, senior deduction) and enter it on line 13b. Its MAGI starts from line 11b.
9. **Compute the QBI deduction** (line 13a). "Taxable income before the QBI deduction" = line 11a − line 12e − line 13b. Use Form 8995 or Form 8995-A according to the threshold test below. QBI itself is net profit reduced by the deductible half of SE tax, the health insurance deduction and the retirement contribution attributable to the business.
10. **Taxable income** (line 15) = line 11b − line 14, where line 14 = 12e + 13a + 13b. It cannot go below zero.
11. **Compute the tax** (line 16): Tax Table if taxable income is under $100,000, Tax Computation Worksheet otherwise ([Form 1040 instructions](https://www.irs.gov/instructions/i1040gi)), or the capital gain worksheets if there are qualified dividends or net capital gain. Add Schedule 2 Part I (line 17) and subtract credits (lines 19 to 21).
12. **Schedule 2 Part II:** SE tax (line 4), Additional Medicare Tax (line 11, Form 8959) and net investment income tax (line 12, Form 8960). Schedule 2 line 21 goes to Form 1040 line 23. Line 24 is total tax.
13. **Payments:** withholding (line 25d), estimated payments and prior-year overpayment applied (line 26), and refundable credits (line 32). Line 33 is total payments.
14. **Estimated tax penalty.** Test the safe harbours below. File Form 2210 only if a Part II box (A to E) applies. Otherwise the taxpayer may leave line 38 blank and let the IRS bill any penalty.
15. **Run the tie-out checks** below. Then produce the package: the return, a working paper that recomputes each schedule, and a reviewer note listing every judgment call. Also include next year's estimated-tax schedule.

## Figures for tax year 2026 ([IRS inflation adjustments for 2026](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill); [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Pub. 505 (2026)](https://www.irs.gov/publications/p505))

| Item | 2026 amount |
|---|---|
| Standard deduction: single or married filing separately | $16,100 |
| Standard deduction: married filing jointly or qualifying surviving spouse | $32,200 |
| Standard deduction: head of household | $24,150 |
| 10% bracket ends (single / MFJ) | $12,400 / $24,800 |
| 12% bracket ends (single / MFJ) | $50,400 / $100,800 |
| 22% bracket ends (single / MFJ) | $105,700 / $211,400 |
| 24% bracket ends (single / MFJ) | $201,775 / $403,550 |
| 32% bracket ends (single / MFJ) | $256,225 / $512,450 |
| 35% bracket ends; 37% above (single / MFJ) | $640,600 / $768,700 |
| QBI threshold (MFJ / MFS / all others) | $403,500 / $201,775 / $201,750 |
| QBI phase-in ends (MFJ / MFS / all others) | $553,500 / $276,775 / $276,750 |
| Social security wage base (wages plus SE earnings) | $184,500 |
| SALT limit (MFS: $20,200), before the high-income reduction | $40,400 |
| SALT reduction starts above MAGI of (MFS: $252,500) | $505,000 |

For head-of-household brackets, see Rev. Proc. 2025-32. The personal exemption stays at zero.

### What changed for 2026 ([Pub. 505 (2026)](https://www.irs.gov/publications/p505); [26 U.S.C. 199A](https://www.law.cornell.edu/uscode/text/26/199A))

- **QBI deduction made permanent.** Starting in 2026, an "applicable taxpayer" gets a minimum QBI deduction of $400. An applicable taxpayer has at least $1,000 of qualified business income, in total, from active trades or businesses in which the taxpayer materially participates. The deduction is the larger of the normal computation and $400. The $400 and $1,000 amounts are indexed for inflation after 2026. Separately, the phase-in range widens to $75,000 ($150,000 on a joint return) above the threshold.
- **Premium tax credit.** From 2026 there is no limit on repaying excess advance credit, even with household income below 400% of the federal poverty line. Household income above 400% of the poverty line makes the taxpayer ineligible for the credit. For a freelancer with Marketplace coverage, get the income estimate right; an underestimate is now repaid in full.
- **Charitable giving.** Non-itemizers can deduct cash gifts to eligible charities up to $1,000 ($2,000 MFJ). Itemizers can deduct only gifts above 0.5% of AGI.
- **Itemized deduction limit.** Itemized deductions are reduced by 5.4% of the smaller of total itemized deductions or taxable income above $640,600 (single or head of household), $768,700 (MFJ or qualifying surviving spouse) or $384,350 (MFS). The QBI computation ignores this reduction.
- **Information returns.** For 2026, qualified tips are reported in dedicated boxes on Forms W-2, 1099-MISC, 1099-NEC and 1099-K, and qualified overtime in dedicated boxes on Forms W-2, 1099-MISC and 1099-NEC. Use these amounts for Schedule 1-A.

## Self-employment tax ([Schedule SE (2025)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf); [Pub. 505 (2026)](https://www.irs.gov/publications/p505))

| Item | Rule |
|---|---|
| Net earnings | Schedule C net profit × 92.35% |
| No SE tax | If net earnings (Schedule SE line 4c) are less than $400 |
| Social security part | 12.4% of net earnings, up to the wage base minus social security wages already taxed |
| Wage base | $176,100 for 2025; $184,500 for 2026 |
| Medicare part | 2.9% of all net earnings, with no cap |
| Deduction | Half of SE tax (Schedule SE line 13) goes to Schedule 1 line 15 |

The health insurance deduction does **not** reduce net earnings for SE tax ([Form 7206 instructions](https://www.irs.gov/instructions/i7206)).

## Additional taxes on higher income ([Pub. 505 (2026)](https://www.irs.gov/publications/p505))

| Tax | Rate | Applies above |
|---|---|---|
| Additional Medicare Tax (Form 8959) on wages plus SE income | 0.9% | $200,000 single, head of household or qualifying surviving spouse; $250,000 MFJ; $125,000 MFS |
| Net investment income tax (Form 8960) on the smaller of net investment income or the MAGI excess | 3.8% | $200,000 single or head of household; $250,000 MFJ or qualifying surviving spouse; $125,000 MFS |

These thresholds are not the same for a qualifying surviving spouse. Schedule C profit from an active business is not net investment income. The NIIT matters only when the freelancer also has interest, dividends, gains or rent.

## Deductions and credits added by the 2025 law ([Schedule 1-A (2025)](https://www.irs.gov/pub/irs-pdf/f1040s1a.pdf); [IRS fact sheet FS-2025-03](https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors); [Form 1040 instructions (2025)](https://www.irs.gov/instructions/i1040gi))

These apply for 2025 through 2028. Itemizers and non-itemizers can both claim them. They go on Schedule 1-A and flow to Form 1040 line 13b, so they lower taxable income but **not** AGI. Schedule 1-A MAGI is line 11b plus excluded Puerto Rico, foreign earned income and housing, and Form 4563 amounts.

| Deduction | Cap | Reduction | Who qualifies, and the traps |
|---|---|---|---|
| Qualified tips | $25,000 | $100 for each full $1,000 of MAGI above $150,000 ($300,000 MFJ) | The occupation must be on the IRS list of tipped occupations. The tips must be voluntary and reported on a W-2, a 1099 or Form 4137. A self-employed person in a specified service trade or business (SSTB) cannot claim it. Neither can an employee whose employer is in an SSTB. Transition relief under Notice 2025-69 treats someone working in a listed tipped occupation as not in an SSTB until final regulations are issued. For self-employed tips, the limit is the gross income of that business minus all deductions allocable to it, including the deductible part of SE tax, the SEP, SIMPLE and qualified plan deduction and the SE health insurance deduction. It is not simply net profit. Needs a valid SSN, and married taxpayers must file jointly. |
| Qualified overtime | $12,500 ($25,000 MFJ) | Same as tips | Only the premium part of overtime that the Fair Labor Standards Act requires, for example the "half" in time-and-a-half, as reported on a W-2 or the 1099 boxes on Schedule 1-A line 14b. Schedule C profit is never overtime. Needs a valid SSN, and married taxpayers must file jointly. |
| Car loan interest | $10,000 | $200 for each $1,000 (or part of $1,000) of MAGI above $100,000 ($200,000 MFJ) | The loan must be originated after December 31, 2024, and secured by a lien on the vehicle. The vehicle must be for personal use, have its final assembly in the US, and have its original use start with the taxpayer (used vehicles do not qualify). It must be a car, minivan, van, SUV, pickup truck or motorcycle with a gross vehicle weight rating under 14,000 pounds. Interest on a qualifying loan that is later refinanced generally still qualifies. Leases do not qualify, and the return must show the VIN. Interest already deducted on Schedule C is excluded. |
| Senior deduction | $6,000 per eligible person | 6% of MAGI above $75,000 ($150,000 MFJ) | The person must be 65 by the last day of the year (for 2025, born before January 2, 1961). It is in addition to the existing additional standard deduction for age. Needs a valid SSN, and married taxpayers must file jointly. |

## QBI deduction: which form, and the thresholds for 2025 ([Form 8995 (2025)](https://www.irs.gov/pub/irs-pdf/f8995.pdf); [Form 8995 instructions (2025)](https://www.irs.gov/instructions/i8995))

- **Form 8995** is allowed only if taxable income before the QBI deduction is **at or below** $197,300 ($394,600 MFJ) for 2025, and the taxpayer is not a patron of an agricultural or horticultural cooperative. Otherwise use **Form 8995-A**.
- At or below the threshold, a specified service business (for example consulting) is treated as a qualified business, and there is no limit based on W-2 wages or property. Above $197,300 but not above $247,300 ($394,600 to $494,600 MFJ), the SSTB exclusion and the wage and property limit phase in. Above that range, an SSTB gets no deduction. Deciding whether a freelancer is an SSTB is a judgment call for the reviewer note.
- Form 8995 computes 20% of QBI, then caps it at 20% of (taxable income before QBI − net capital gain, including qualified dividends).
- "Taxable income before QBI" for 2025 = Form 1040 line 11a − line 12e − line 13b. Leaving out 13b (Schedule 1-A) overstates the income limit.
- A QBI loss (including a carryforward) reduces QBI in later years.

For 2026 thresholds see the 2026 table above. Confirm the 2026 Form 8995 threshold on the form once it is released.

## Estimated tax and the Form 2210 penalty ([Pub. 505 (2026)](https://www.irs.gov/publications/p505); [Form 2210 instructions (2025)](https://www.irs.gov/instructions/i2210))

- Estimated tax is required for 2026 when **both** of these are true: (a) the taxpayer expects to owe at least $1,000 after withholding and credits, and (b) withholding and credits will be less than the smaller of 90% of the 2026 tax and 100% of the 2025 tax. The 2025 return must cover 12 months.
- Use 110% instead of 100% if 2025 AGI (line 11b) was more than $150,000 ($75,000 if filing separately for 2026). This does not apply if at least two-thirds of gross income is from farming or fishing.
- 2026 due dates: April 15, 2026; June 15, 2026; September 15, 2026; January 15, 2027. A due date that falls on a weekend or legal holiday moves to the next business day. The January payment is not needed if the 2026 return is filed by January 31, 2027 and the balance is paid then.
- File Form 2210 only if a box in Part II applies. Boxes B (waiver of part of the penalty), C (annualized income installment method) and D (withholding treated as paid on the actual dates) require the taxpayer to figure the penalty. Boxes A (waiver of the entire penalty) and E (joint return in only one of the two years, with the lower prior-year amount) require page 1 only. If no box applies, don't file Form 2210. The taxpayer may leave line 38 blank, and the IRS will figure any penalty and send a bill, or may figure the penalty and enter it on line 38 without attaching the form.

## Filing, extension and payment ([When to file](https://www.irs.gov/filing/individuals/when-to-file); [Form 4868 (2025)](https://www.irs.gov/pub/irs-pdf/f4868.pdf))

| Event | 2025 return | 2026 return |
|---|---|---|
| Return and payment due | April 15, 2026 | April 15, 2027, which is the 15th day of the fourth month after year-end, moved if it falls on a weekend or holiday |
| Extension | Form 4868 by April 15, 2026 gives six months, to October 15, 2026 | Form 4868 by the original due date |
| Payment | An extension to file is **not** an extension to pay. Tax unpaid after the original date bears interest | Same |

- **Late filing:** usually 5% of the unpaid tax for each month or part month, up to 25%. For a 2025 return more than 60 days late, the minimum is $525 (inflation-adjusted) or the tax due, whichever is smaller.
- **Late payment:** usually ½ of 1% of the unpaid tax for each month or part month, up to 25%.

## 2025 returns: what differs ([Form 1040 (2025)](https://www.irs.gov/pub/irs-pdf/f1040.pdf); [Schedule 2 (2025)](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf); [Schedule A instructions (2025)](https://www.irs.gov/instructions/i1040sca))

- The 2025 standard deduction is $15,750 (single or MFS), $31,500 (MFJ or qualifying surviving spouse) and $23,625 (head of household). If a box on line 12a to 12d is checked (dependent, spouse itemizes separately, dual-status alien, born before January 2, 1961, or blind), use the instructions instead of the flat amount.
- The 2025 Form 1040 splits AGI into lines 11a and 11b, puts the standard or itemized deduction on 12e, QBI on 13a and Schedule 1-A on 13b, and totals them on line 14.
- An excess advance premium tax credit repayment goes on Schedule 2 **line 1a**. Line 2 is the alternative minimum tax.
- Form 1040 line 26 is "2025 estimated tax payments and amount applied from 2024 return".
- **Rate brackets:** the 2026 brackets above do **not** apply to 2025 returns. For 2025, use the Tax Table in the 2025 Form 1040 instructions if taxable income is less than $100,000, or the Tax Computation Worksheet if it is $100,000 or more ([Form 1040 instructions (2025)](https://www.irs.gov/instructions/i1040gi)).
- The 2025 SALT limit on Schedule A is $40,000 ($20,000 MFS). It is reduced when MAGI is more than $500,000 ($250,000 MFS), but not below $10,000 ($5,000 MFS). For 2026 the limit is $40,400 and the reduction starts above $505,000; the reduction is 30% of the MAGI excess ([26 U.S.C. 164(b)(7)](https://www.law.cornell.edu/uscode/text/26/164)).

## Boundaries and exceptions ([Form 7206 instructions](https://www.irs.gov/instructions/i7206); [Form 1099-K](https://www.irs.gov/businesses/understanding-your-form-1099-k); [26 U.S.C. 199A](https://www.law.cornell.edu/uscode/text/26/199A))

| Situation | Treatment |
|---|---|
| Net earnings from self-employment are just under $400 | No SE tax. Schedule SE is not needed for the tax, but Schedule C is still filed |
| Eligible for a subsidized plan of the taxpayer's, spouse's, dependent's or child-under-27's employer for part of the year ([Form 7206 (2025) line 1](https://www.irs.gov/pub/irs-pdf/f7206.pdf)) | Premiums for those months don't count toward the health insurance deduction, even if the coverage was declined |
| Only one Schedule C, no Form 2555, no long-term care premiums | Use the Schedule 1 line 17 worksheet in the Form 1040 instructions. Form 7206 is optional |
| More than one source of SE income, Form 2555, or long-term care premiums | Form 7206 is required, one per business under which a plan is established |
| Marketplace plan with advance premium tax credit | Pub. 974 method. For 2026 there is no repayment cap |
| Taxable income before QBI exactly at the 2025 threshold ($197,300) | "At or below", so Form 8995 is allowed |
| QBI of $999 from an active business in 2026 | Not an "applicable taxpayer", so no $400 minimum. Compute normally |
| Taxpayer 65 but married filing separately | No senior deduction; a joint return is required |
| 1099-K from a payment app below the reporting threshold | Still report all business income. A payment app or marketplace must issue a 1099-K when payments total over $20,000 in more than 200 transactions. Card payments are reported whatever the amount |
| Personal payments from family or friends on a 1099-K | Not income. Document why they were excluded |

## Tie-out checks before sign-off

- Schedule C line 31 = Schedule SE line 2 (for a single business and no farm income).
- Schedule SE line 12 = Schedule 2 line 4, and Schedule SE line 13 = Schedule 1 line 15.
- Form 7206 line 14 (or the worksheet result) = Schedule 1 line 17. Form 7206 line 9 = the line 16 retirement amount for the same business.
- Schedule 1 line 26 = lines 11 through 23 plus line 25, and it equals Form 1040 line 10.
- Form 1040 line 9 = 1z + 2b + 3b + 4b + 5b + 6b + 7a + 8. Line 11a = 9 − 10, and line 11b = 11a.
- Form 8995 line 11 (or Form 8995-A line 33) = line 11a − 12e − 13b. The QBI deduction on the form = line 13a.
- Schedule 1-A line 38 = line 13b. Line 14 = 12e + 13a + 13b. Line 15 = 11b − 14, not below zero.
- Schedule 2 line 21 = Form 1040 line 23. Line 24 = 22 + 23.
- Line 33 = 25d + 26 + 32. Line 26 agrees with IRS payment records (use the taxpayer's IRS online account transcript).
- For Marketplace coverage, Form 8962: an excess advance credit repayment = Schedule 2 line 1a, and a net premium tax credit = Schedule 3 line 9.
- Only one of line 34 (overpaid) or line 37 (owed) is positive, and it equals the difference between lines 33 and 24.
- Every 1099 received is traced to a Schedule C line or an explained exclusion.

## Worked cases ([Schedule SE (2025)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf); [Pub. 560](https://www.irs.gov/publications/p560); [Form 7206 (2025)](https://www.irs.gov/pub/irs-pdf/f7206.pdf); [Form 8995 (2025)](https://www.irs.gov/pub/irs-pdf/f8995.pdf); [Form 1040 (2025)](https://www.irs.gov/pub/irs-pdf/f1040.pdf))

**Case A: ordinary 2025 return.** A single developer aged 40 has Schedule C net profit of $120,000 and no wages. She pays $9,600 of private (non-Marketplace) health premiums, with no employer plan available in any month. She contributes $15,000 to a SEP. She has no other income, no capital gains and no Schedule 1-A items.

- Net earnings: $120,000 × 92.35% = $110,820.00.
- SE tax: $110,820.00 × 12.4% = $13,741.68, plus $110,820.00 × 2.9% = $3,213.78, total $16,955.46. The deductible half is $8,477.73.
- SEP ceiling: 20% × ($120,000 − $8,477.73) = $22,304.45. The $15,000 contribution is within it.
- Health insurance limit: $120,000 − $8,477.73 − $15,000 = $96,522.27. That is more than $9,600, so she deducts $9,600.
- AGI: $120,000 − $8,477.73 − $15,000 − $9,600 = $86,922.27.
- Taxable income before QBI: $86,922.27 − $15,750 = $71,172.27. That is below $197,300, so she uses Form 8995.
- QBI: $120,000 − $8,477.73 − $15,000 − $9,600 = $86,922.27, and 20% of it is $17,384.45. The income limit is 20% × $71,172.27 = $14,234.45. The deduction is the smaller amount, $14,234.45.
- Taxable income: $71,172.27 − $14,234.45 = $56,937.82. Take the tax from the 2025 Tax Table (under $100,000). Total tax = that tax + $16,955.46 SE tax, less credits.

**Case B: senior deduction, 2025.** A single filer born in 1959 with a valid SSN has MAGI of $95,000. Deduction: $6,000 − 6% × ($95,000 − $75,000) = $4,800, entered on Schedule 1-A and line 13b, on top of the regular additional standard deduction for age.

**Case C: 2026 minimum QBI deduction.** A freelancer has $1,500 of QBI from a business she actively runs. The normal computation gives 20% × $1,500 = $300. She is an applicable taxpayer (at least $1,000 of QBI), so the deduction is $400. With $999 of QBI she would get $199.80 instead, because the $400 minimum does not apply.

**Case D: order error.** A preparer computes the health insurance limit before the SEP contribution. In Case A that would give a limit of $111,522.27 instead of $96,522.27. Here it makes no difference, but with premiums between those two amounts the deduction would be overstated. Always do the retirement step first.

## When to refuse or refer

- An S corporation, partnership or multi-member LLC, or a Schedule C loss that raises at-risk, passive-activity or excess-business-loss questions.
- Rental income (Schedule E), K-1s, material capital gains or crypto disposals beyond simple Schedule D reporting. See `us-capital-gains`.
- Foreign income, a foreign tax credit, Form 2555, FBAR or Form 8938 obligations, or a non-resident or dual-status filer.
- An SSTB above the QBI threshold, aggregation elections, or W-2 wage and property limits (Form 8995-A with Schedules A to D).
- A Marketplace plan with advance credit where the Pub. 974 iteration does not converge, or where household income is near 400% of the poverty line in 2026 ([Pub. 505 (2026)](https://www.irs.gov/publications/p505)).
- Tips in an occupation not clearly on the IRS list, overtime not reported on a W-2 or 1099, or tips earned in a possible SSTB.
- A tie-out check that fails and cannot be explained from the source documents.
- Amended returns (Form 1040-X), unfiled prior years, IRS notices, or a collection matter.
- Any figure that cannot be traced to a source document or an official IRS page. Flag it; do not guess.

## Completion checklist

- Intake answers recorded, including coverage by month and SSN status.
- Schedule C reconciled to the bank and to every 1099. Personal and transfer items excluded with notes.
- Schedule SE, then retirement, then health insurance (and Pub. 974 if Marketplace), computed in that order.
- Schedule 1-A tested for every person: age, SSN, tipped occupation, FLSA overtime, qualifying car loan.
- QBI computed from line 11a − 12e − 13b, and the correct form (8995 or 8995-A) chosen.
- Every tie-out check above passes, or the difference is explained in the reviewer note.
- Safe harbour tested, and Form 2210 filed only if a Part II box applies.
- Filing date, extension (Form 4868) and payment plan confirmed. Next year's estimated payments scheduled.
- State handoff prepared: federal AGI, taxable income, QBI deduction, depreciation detail, and the SE health insurance and retirement amounts.
- A credentialed preparer reviews and signs before filing.

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
