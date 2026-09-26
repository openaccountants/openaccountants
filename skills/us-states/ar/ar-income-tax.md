---
name: ar-income-tax
description: Use this skill whenever asked about Arkansas individual income tax for self-employed individuals or sole proprietors — filing Form AR1000F, AR estimated tax, Arkansas tax brackets, Arkansas deductions, or any query involving Arkansas state income tax compliance. Trigger on phrases like "Arkansas income tax", "AR income tax", "Form AR1000F", "Arkansas estimated tax", "Arkansas self-employed tax", "DFA income tax", or "Ark. Code Ann. §26-51".
version: "0.1"
jurisdiction: US-AR
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Arkansas individual income tax (Form AR1000F and AR1000NR): 2026 method, with 2025 return notes

Figures are for tax year 2026 unless a line says 2025. The 2026 rates come from Act 2 of the First Extraordinary Session of 2026, which cut the top rate to 3.7% ([Act 2](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf)). The 2025 figures come from the Arkansas Department of Finance and Administration (DFA) 2025 instructions and tax tables. A separate section covers 2025 returns, which are still being filed on extension.

## Scope

- **Covers:** individuals who file an Arkansas return: full-year residents (Form AR1000F), and part-year residents and nonresidents (Form AR1000NR). It covers wage earners, retirees, and self-employed people and sole proprietors who report a federal Schedule C.
- **Covers these topics:** filing thresholds, income and exempt income, the Arkansas adjustments on Form AR1000ADJ, the standard deduction, the tax tables and rates, personal tax credits, capital gains (Form AR1000D), the retirement exemption, military pay, part-year proration, estimated tax, the extension, and penalties.
- **Does not cover:** fiduciary returns (AR1002), corporations, the electing pass-through entity tax (PET) return itself, composite returns, business incentive credits, or a multistate business's apportionment. See "When to refuse or refer".
- **Arkansas does not start from the federal return's AGI.** The AR1000F lists each type of income on its own line (wages on line 8, Schedule C on line 13, capital gains on line 14, and so on), subtracts only the adjustments printed on Form AR1000ADJ, and reaches its own Arkansas AGI on line 25. Federal amounts feed in line by line, often with Arkansas changes ([2025 AR1000F/AR1000NR instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).

## Ask the client first

- Which tax year is this: a 2026 estimate, or a 2025 return that is still open? The top rates differ between the two years.
- Where was the client domiciled during the year? Did they move into or out of Arkansas during the year? Did they live inside the city limits of Texarkana, Arkansas or Texarkana, Texas, at a street address (not a PO box)?
- Filing status. If married, do both spouses have income? Arkansas lets married couples file jointly, separately on the same return (status 4), or separately on different returns (status 5). If one spouse had a negative total income, they must file jointly.
- For each income type: wages (and Arkansas withholding), Schedule C net profit, Schedule E and K-1 income, farm income, interest and dividends, capital gains and holding periods, retirement distributions (employer plan or traditional IRA, the client's age, and whether it was a rollover), Social Security, unemployment, gambling winnings.
- Is either spouse on active duty in the armed forces, National Guard or Reserves, or receiving military retirement? What is the Home of Record?
- For the self-employed: federal Schedule C, any bonus depreciation or section 179 deduction claimed federally, health insurance paid through the business, and SEP, SIMPLE or Keogh contributions.
- Is the client a member of an entity that elected the Arkansas pass-through entity tax?
- Income taxed by another state (the client will need a signed copy of that state's return), and income from Arkansas sources for a nonresident.
- Estimated tax paid for the year, the prior year's Arkansas tax liability, and any overpayment carried forward.
- Did the client file a federal extension (Form 4868) or an Arkansas extension (Form AR1055-IT)?

## The method, step by step

1. **Decide whether a return is needed and which form.** Full-year residents use AR1000F. Part-year residents and nonresidents use AR1000NR. A nonresident with any Arkansas-source gross income must file, whatever the amount; a part-year resident must file if they had any gross income while an Arkansas resident. A full-year resident files if gross income is at least the threshold for their status (see the 2025 section), or to claim a refund or the military pay exemption ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).
2. **List income line by line**, using Arkansas rules. Leave out exempt income (Social Security, VA benefits, child support, gifts and inheritances, interest on US and Arkansas government obligations, active-duty military pay). Enter Schedule C net profit on line 13. Run capital gains through Form AR1000D before they reach line 14. Put federal/state depreciation differences on line 22 through Form AR-OI.
3. **Apply the retirement and military exemptions.** Military retirement pay is fully exempt. Part of an employer-plan distribution, or of a traditional IRA distribution taken at age 59½ or later, is exempt, with one cap per taxpayer across all plans (see the figures and the boundary table).
4. **Subtract only the adjustments printed on Form AR1000ADJ** (line 24). These include IRA, HSA, self-employed health insurance, Keogh/SEP/SIMPLE contributions, student loan interest, alimony paid under a court order, and the Texarkana exemption. The form says: "Do not enter amounts from categories that are not printed on this form." So do not carry across other federal adjustments, such as the deductible part of self-employment tax ([AR1000ADJ](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000ADJ_AdjustmentsSchedule.pdf)). The result is Arkansas AGI (line 25).
5. **Choose the tax table.** If the client qualifies for a Low Income Tax Table, the standard deduction is already built in: enter zero deduction and read the tax from Arkansas AGI. Otherwise use the Regular Tax Table and deduct the larger of the standard deduction or Arkansas itemized deductions (Form AR3). Net taxable income is line 28.
6. **Compute the tax** from the Regular Tax Table. The same table applies to every filing status. Married couples filing status 4 compute each spouse's tax separately on the same return. For 2026, see the rate tables below.
7. **Subtract credits:** personal tax credits (line 34), the child care credit (AR2441), and the credits on Form AR1000TC (credit for tax paid to another state, the additional credit for qualified individuals, and others). Credits beyond the total tax are not refundable.
8. **Part-year residents and nonresidents only:** prorate the net tax by Arkansas AGI (column C) divided by total AGI (columns A and B), as a decimal rounded to six places and capped at 100% ([DFA Subject 802](https://www.dfa.arkansas.gov/wp-content/uploads/802-HowToApportionTaxLiability.pdf)).
9. **Subtract payments** (withholding, estimated tax, extension payment), then work out the underestimate penalty on Form AR2210 or AR2210A.

## Figures with years

### 2026 rates: Act 2 of the First Extraordinary Session of 2026 ([Act 2](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf))

The Act applies "for tax years beginning on or after January 1, 2026". It was approved on 6 May 2026.

| Net taxable income of $94,700 or less: from | to | rate |
| --- | --- | --- |
| $0 | $5,599 | 0% |
| $5,600 | $11,199 | 2% |
| $11,200 | $15,999 | 3% |
| $16,000 | $26,399 | 3.4% |
| $26,400 | $94,700 | 3.7% |

| Net taxable income over $94,700: from | to | rate |
| --- | --- | --- |
| $0 | $4,700 | 2% |
| $4,701 | and above | 3.7% |

- If net taxable income is from $94,701 to $97,600, the tax from the upper table is reduced by a "bracket adjustment amount". This starts at $290 at $94,701–$94,800 and falls by $10 for each $100 band, down to $10 at $97,501–$97,600 and $0 from $97,601.
- DFA's fiscal impact statement confirms these as the tables for "the 2026 and following tax years" ([DFA fiscal impact, SB1](https://arkleg.state.ar.us/Home/FTPDocument?path=%2FAssembly%2F2025%2F2026S1%2FFiscal+Impacts%2FSB1-DFA1.pdf)).
- The same Act says the tables "shall be adjusted annually". DFA's 2026 withholding formula and 2026 estimated-tax worksheet use the unadjusted amounts above. **The 2026 AR1000F tax table is not published yet.** Treat 2026 computations as estimates until it is.
- DFA's 2026 bracket formula ([2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf)): for income of $26,400 to $94,700, tax = income × 3.7% minus $367.16. For income of $97,601 and over, tax = income × 3.7% minus $79.90. The return's table is worked at the midpoint of each $100 band, so a table figure can differ from the formula by a few dollars.

### 2026 deduction and credits ([2026 AR1000ES](https://www.dfa.arkansas.gov/wp-content/uploads/2026_Final_AR1000ES_2.pdf))

- Standard deduction on DFA's 2026 estimated-tax worksheet: $2,470 per taxpayer. Confirm it against the 2026 AR1000F instructions when they are published.
- Personal tax credits on the 2026 worksheet: $29 for single or married filing on separate forms. $58 for a joint return, head of household, married filing separately on the same return, or a qualifying widow(er). Add $29 for each dependent, and $29 each for blind, deaf, over 65 and "65 Special".
- Declaration threshold: file a Declaration of Estimated Tax if the estimated tax after withholding and credits is $1,000 or more.

### Figures that stay the same in both years

- **Retirement exemption:** $6,000 per taxpayer, across all employer plans and traditional IRAs combined ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).
- **Capital gains:** 50% of the net capital gain is taxed (net long-term gain less net short-term loss). Net capital gain above $10,000,000 is exempt. Net short-term gain is taxed in full ([AR1000D](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000D_CapitalGains.pdf); [DFA Subject 502](https://www.dfa.arkansas.gov/wp-content/uploads/502-CapitalGainsTax.pdf)).
- **Capital loss limit:** $3,000 a year, or $1,500 per taxpayer for filing status 4 or 5. The unused loss carries forward ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).
- **Home sale:** gain on a main home is exempt up to $250,000 per taxpayer, or $500,000 for a married couple filing on the same return, if it was owned and used as the main home for 2 of the 5 years before the sale ([DFA Subject 502](https://www.dfa.arkansas.gov/wp-content/uploads/502-CapitalGainsTax.pdf)).

## Boundary and exception table

| Rule | Who / when | Boundary and conditions | Source |
| --- | --- | --- | --- |
| Regular vs upper rate table | Tax year 2026 | Upper table only if net taxable income is **more than** $94,700; bracket adjustment for $94,701–$97,600 | [Act 2](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf) |
| Retirement exemption: employer-sponsored plan | Any age; "The recipient does not have to be retired" | First $6,000 of the taxable amount, after recovering after-tax contributions under IRC §72. Caveat: the line 16 instructions treat withdrawals from deferred compensation or thrift savings plans before age 59½ (or disability) as premature distributions; check those before applying the exemption | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Retirement exemption: traditional IRA | Only after reaching age 59½, or an early distribution because of the participant's death or disability | Other early withdrawals do not qualify, even for medical costs, education or a first home; one $6,000 cap across all plans per taxpayer; a surviving spouse gets a single $6,000 | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Military retirement | Uniformed services retirement pay | Fully exempt. If it exceeds $6,000, no exemption for other plans; if less, the rest of the $6,000 can be used on employer-sponsored plans. For traditional IRAs DFA contradicts itself: the exempt-income list allows the remainder for "traditional or employer-sponsored distributions", but the line 17 text says "Retirees cannot claim both the military retirement exemption and the $6,000 exemption for traditional IRA distributions (A.C.A 26-51-307(f))". Confirm with DFA or refer before using the remainder on an IRA | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Active-duty military pay | Tax years from 2014; includes National Guard and Reserves | Fully exempt, but the resident must still file and report it (line 9); nonresidents stationed in Arkansas are not taxed on it | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Low Income Tax Table | Total income from all sources within the table limit | Married couples must file jointly; not available if the client uses the exclusion for active-duty military pay, military retirement, employer-sponsored pension income or a qualified traditional IRA distribution. The client "may elect NOT TO USE the exclusion(s)" and use the Low Income Table if within its limits; not with itemizing | [2025 tax tables](https://www.dfa.arkansas.gov/wp-content/uploads/TaxTables_FI_2025.pdf); [instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Itemizing, status 4 or 5 | Married filing separately | If one spouse itemizes, both must itemize | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Texarkana exemption | Residents inside Texarkana, AR city limits: all income exempt. Residents inside Texarkana, TX: only income earned in Texarkana, AR | Must use a street address in the city limits (a PO box or rural route is disallowed); attach Form AR-TX for W-2 income; file and report all income, then claim it on AR1000ADJ | [DFA Subject 302](https://www.dfa.arkansas.gov/wp-content/uploads/302-BorderCityExemption.pdf) |
| Capital gain over $10,000,000 | Gain realized on or after 1 January 2014 | Line 7b of AR1000D caps net capital gain at $10,000,000 before the 50% | [AR1000D](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000D_CapitalGains.pdf) |
| Bonus depreciation | Federal §168(k) | Arkansas did not adopt it; report the depreciation difference on AR-OI and AR1000D | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Section 179 | Purchases after 2022 | Arkansas adopted IRC §179 "as in effect on January 1, 2022"; the 2025 instructions give a $1,250,000 deduction limit and a $3,130,000 cost-of-property limit | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| Credit for tax paid to another state | Arkansas residents only | Nonresidents cannot claim it; attach a signed copy of the other state's return | [AR1000TC instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000TC_Instructions.pdf) |
| Net operating loss | Arkansas NOL | Carry forward only ("NOL carrybacks not allowed"); attach AR1000-NOL | [Instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |

### Federal conformity and P.L. 119-21 (OBBBA)

- Arkansas adopts selected Internal Revenue Code sections as of fixed dates, not the current Code. Two examples from the 2025 instructions: it did not adopt federal bonus depreciation, and it adopted IRC §179 as in effect on 1 January 2022 ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).
- The 2025 instructions and DFA's 2026 estimated-tax forms do not add any line for the 2025 federal changes in P.L. 119-21. Form AR1000ADJ accepts only the adjustments printed on it, and tips are reported as wages on line 8. So do not assume any new federal deduction (for tips, overtime, car-loan interest or seniors) reduces Arkansas income. Check DFA's What's New page and the 2026 instructions before filing a 2026 return.
- The federal qualified business income deduction (§199A) has no Arkansas equivalent and no line on the AR1000F.

## Worked cases

Each case is an illustration with hypothetical inputs. 2026 amounts use DFA's 2026 bracket formula and may differ by a few dollars from the 2026 tax table once it is published.

**C1: 2026, single, self-employed ([2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf); [2026 AR1000ES](https://www.dfa.arkansas.gov/wp-content/uploads/2026_Final_AR1000ES_2.pdf)).** Schedule C net profit $60,000, no other income, standard deduction. Arkansas has no line for the deductible part of self-employment tax, so net taxable income = $60,000 − $2,470 = $57,530. Tax ≈ $57,530 × 3.7% − $367.16 = $1,761.45. Less the $29 personal credit = $1,732.45. That is $1,000 or more, so a declaration is due. Four vouchers of about $433 each (15 April, 15 June, 15 September 2026 and 15 January 2027).

**C2: 2025 return, single, table lookup ([2025 brackets](https://www.dfa.arkansas.gov/wp-content/uploads/2025_TaxBrackets.pdf)).** Net taxable income on line 28 is $75,950, in the $75,900–$76,000 band. DFA's own example gives the table tax as $2,542 ($75,950 × .039 = $2,962.05, less $419.96, rounded). Less the $29 personal credit = $2,513.

**C3: 2026, married filing jointly, high income ([Act 2](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf); [2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf)).** Net taxable income is $150,000, which is more than $94,700, so the upper table applies: 2% on the first $4,700 and 3.7% above it. Tax = $150,000 × 3.7% − $79.90 = $5,470.10. Less personal credits of $58 = $5,412.10.

**C4: 2026, capital gains ([AR1000D](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000D_CapitalGains.pdf)).** A resident has net long-term gain of $40,000 (no losses) and net short-term gain of $5,000. Arkansas taxable amount = $40,000 × 50% + $5,000 = $25,000. That goes on line 14.

**C5: gain over $10,000,000 ([AR1000D](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000D_CapitalGains.pdf)).** Net long-term capital gain of $12,000,000 from a sale in 2026. Line 7b caps it at $10,000,000. Line 8 = $10,000,000 × 50% = $5,000,000 taxable. The other $7,000,000 is not taxed.

**C6: 2026, retiree aged 66 ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).** Taxable employer pension $20,000 and a traditional IRA distribution of $8,000. Social Security is exempt and is left out. There is one $6,000 cap across both plans, so taxable retirement income = $20,000 + $8,000 − $6,000 = $22,000. Because the client uses the pension and IRA exclusions, the Low Income Tax Table is not available unless they elect not to use them.

**C7: 2026, part-year resident ([DFA Subject 802](https://www.dfa.arkansas.gov/wp-content/uploads/802-HowToApportionTaxLiability.pdf); [2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf)).** A single person moved to Arkansas on 1 July. Total AGI for the year from all sources is $90,000, and Arkansas AGI (column C: income received as a resident plus Arkansas-source income) is $36,000. Compute tax on the full-year figure: net taxable income $90,000 − $2,470 = $87,530. Tax ≈ $87,530 × 3.7% − $367.16 = $2,871.45. Less the $29 credit = $2,842.45. The ratio is $36,000 ÷ $90,000 = 0.400000. Arkansas tax ≈ $2,842.45 × 0.400000 = $1,136.98.

**C8: estimated tax safe harbor ([AR2210 instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR2210_Instructions.pdf)).** The C1 client expects 2026 tax of $1,732.45 and had a 2025 Arkansas liability of $1,200. The required annual payment is the lesser of 90% of this year's tax ($1,559.21) or last year's liability ($1,200). So the required payment is $1,200, or $300 a quarter. If less is paid, a penalty of 10% a year runs on each quarter's shortfall, day by day.

## When to refuse or refer

- A multistate business that must apportion income. Act 719 of 2025 rewrote Arkansas apportionment and sourcing (market-based sourcing) "for tax years beginning on and after January 1, 2026" ([Act 719](https://arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf)). Refer it.
- A member of an entity that elected the pass-through entity tax. The income is reported and then backed out on AR-OI, and the entity's tax is not withholding. Refer it unless you have the AR-K1 and the PET return.
- Residency disputes: a claim of a new domicile while the client keeps an Arkansas home, and military spouses who claim a non-Arkansas domicile (Form AR-MS is needed).
- Arkansas NOL carryforwards, business incentive credits (Form AR1000TC business credits), and lump-sum distribution averaging (AR1000TD).
- A final 2026 return figure that depends on the 2026 AR1000F tax table, standard deduction or filing thresholds: refer it until DFA publishes them. Estimates for 2026 planning, labelled as estimates, are fine.
- Any claim that a federal 2025 or 2026 deduction from P.L. 119-21 reduces Arkansas income. We found no Arkansas authority for it.
- Audits, notices of proposed assessment, offers in compromise, and anything that looks like evasion.

## Filing and payment

- **Due date:** 15 April for calendar-year filers. A return mailed on a Saturday, Sunday or legal holiday due date is timely if it is postmarked the next business day ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).
- **Extension:** an accepted federal extension (Form 4868) also extends the Arkansas return, and so does Form AR1055-IT filed by 15 April. The maximum is 210 days, which extends the due date to 15 November. Check the extension box on the return. An extension to file is not an extension to pay. Tax due still has to be paid by 15 April, or the failure-to-pay penalty and interest run.
- **Penalties on an original return ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)):** failure to pay, 1% a month; failure to file, 5% a month; up to a maximum of 35% of the tax due. Interest is 10% a year from the original due date. A $500 penalty applies to a frivolous return.
- **Estimated tax ([2026 AR1000ES](https://www.dfa.arkansas.gov/wp-content/uploads/2026_Final_AR1000ES_2.pdf)):** a declaration is due by 15 April if the estimated tax is expected to be $1,000 or more. Later installments are due 15 June, 15 September and 15 January. Someone who first becomes liable later in the year pays in fewer, larger installments. Farmers whose farm income is expected to be at least two-thirds of gross income may pay by the 15th day of the second month after the year ends.
- **No underestimate penalty ([AR2210 instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR2210_Instructions.pdf))** if the tax shown on the return is less than $1,000. None either if the client had no tax liability in a preceding 12-month tax year and was an Arkansas resident all of that year. The Commissioner can also waive it for casualty, disaster or other unusual circumstances, or where the client retired after age 62 or became disabled and the underpayment had reasonable cause.
- **Payment:** online through ATAP (atap.arkansas.gov), or by check with voucher AR1000V.
- **Federal changes:** if the IRS changes net taxable income, file an amended Arkansas return within 180 days of the IRS notice and demand. If you do not, the statute of limitations stays open for three years on that year.
- **Refund claims:** within three years of filing or two years of payment, whichever is later.

### 2025 returns (tax year 2025, being filed now) ([2025 brackets](https://www.dfa.arkansas.gov/wp-content/uploads/2025_TaxBrackets.pdf))

- **Rates:** Act 1 of the Second Extraordinary Session of 2024 set the top rate at 3.9%. The 2025 indexed brackets are 0% to $5,599; 2% from $5,600; 3% from $11,200; 3.4% from $16,000; and 3.9% from $26,400 to $94,700. Above $94,700, the upper table is 2% on the first $4,700 and 3.9% above, with bracket adjustments up to $97,800. For $100,001 and over: $3,809 + 3.9% of the excess over $100,000.
- **Use the table.** DFA says a formula result "must match the table exactly", and the table is worked at the midpoint of each $100 band.
- **Standard deduction 2025 ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)):** $2,470 (single, head of household, surviving spouse, and each spouse filing separately); $4,940 married filing jointly.
- **Additional tax credit for qualified individuals, 2025 ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)):** up to $60 per person if net income on line 28 is $26,500 or less, stepping down to $0 above $27,600. The return must be timely filed.
- **Dependents 2025 ([instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)):** a dependent's gross income must be under $5,200. This limit does not apply to a child under 19, or to a full-time student under 24.
- **Due dates for 2025 returns:** the original due date was 15 April 2026. Extended returns are due 15 November 2026. That date is a Sunday, so a return postmarked on Monday 16 November 2026 is timely under DFA's weekend rule.

| 2025 filing threshold (full-year resident): must file if gross income is at least | Amount |
| --- | --- |
| Single | $14,644 |
| Head of household or surviving spouse, 1 or no dependents | $20,821 |
| Head of household or surviving spouse, 2 or more dependents | $24,819 |
| Married filing jointly, 1 or no dependents | $24,696 |
| Married filing jointly, 2 or more dependents | $28,723 |
| Married filing separately | $9,470 |
| Source | [2025 instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |

## Completion checklist

- [ ] Right form (AR1000F or AR1000NR) and the right year's table (the 2025 table or the 2026 table).
- [ ] Income entered line by line. Exempt income left out (Social Security, active-duty pay), but active-duty pay shown on line 9.
- [ ] Capital gains run through AR1000D: the exclusion applies to net long-term gain only, short-term gain is taxed in full, and the cap is applied.
- [ ] Retirement exemption: one cap per taxpayer across plans, IRA only from age 59½, early deferred-comp/thrift withdrawals checked, military retirement handled first (remainder to employer plans; remainder to an IRA only after confirming with DFA).
- [ ] Only AR1000ADJ adjustments; no deductible self-employment tax, no QBI.
- [ ] Depreciation differences (bonus, section 179) reported on AR-OI and AR1000D.
- [ ] Low Income Table vs Regular Table chosen correctly, and both spouses on the same method.
- [ ] Personal credits counted: taxpayer, spouse, dependents, 65+, blind, deaf, and HOH or surviving spouse.
- [ ] Part-year or nonresident: tax computed on full-year income, then prorated by the column C ratio, with a copy of federal Form 1040 pages 1 and 2 attached.
- [ ] Other-state credit only for residents, with a signed copy of the other state's return.
- [ ] Estimated tax paid against the lesser of this year's percentage test or last year's liability; AR2210 or AR2210A attached if a penalty or exception applies.
- [ ] Extension box checked if extended. Balance paid by 15 April.
- [ ] Before filing a 2026 return: check DFA's 2026 instructions for the final tax table, standard deduction, filing thresholds and any P.L. 119-21 changes.

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
