---
name: on-individual-return
description: 'Ontario personal income tax on Form ON428 for an individual resident in Ontario on 31 December, for tax year 2026, with the full 2025 figures kept for 2025 returns still being filed or amended. Covers the five Ontario brackets, the basic personal amount and the main non-refundable credits at 5.05%, the Ontario surtax, the Ontario tax reduction, the LIFT credit for low earners, the dividend tax credit, and the Ontario Health Premium chart step by step. Applies to employees, the self-employed and retirees. Trigger on "Ontario tax", "ON428", "Ontario income tax", "Ontario surtax", "Ontario Health Premium", "OHP", "Ontario tax reduction", "LIFT credit", "Ontario basic personal amount", "Ontario tax brackets 2026". Out of scope: Ontario refundable credits and the Trillium Benefit (on-tax-credits), Employer Health Tax (on-eht), the federal T1 (ca-fed-t1-return), CPP and EI (ca-fed-cpp-ei), residency (ca-tax-residency), corporations and trusts.'
version: 2.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Ontario personal income tax (Form ON428), 2026 and 2025

Not yet approved. Built from the law. This source audit is not an accountant approval.

Use 2026 amounts for 2026 income and the actual 2025 forms for 2025 returns. As checked on 14 November 2026, the CRA ON428 catalogue offers the 2025 edition. Line numbers below are those printed on that edition, not confirmed 2026 form fields. The current 2026 rates, TD1ON and Ontario law support the 2026 calculation; recheck the actual 2026 package before filing. Record the year and edition beside each workpaper.

## Who this applies to

- An individual who is resident in Ontario on the last day of the tax year (31 December, or the date of death, or the date they left Canada). Ontario taxes their taxable income from line 26000 of the federal return. Taxation Act, 2007, s. 4(1), paragraphs 1 and 2.
- A non-resident of Canada for the year completes ON428 if they earned employment income only in Ontario, or business income from a permanent establishment only in Ontario (CRA, Ontario tax information 2025, "Who should complete Form ON428"). Their statutory tax base is taxable income earned in Canada, not unrestricted worldwide income (s. 3). Non-resident pension and adoption claims are prohibited by s. 8 paragraph 5; other credits have their own non-resident restrictions. Do not automatically give a non-resident the resident credit package.
- When income is allocated to more than one province or territory, use Form T2203 and the Ontario ON428MJ calculation, rather than completing ordinary ON428 and multiplying its final result. Ontario allocation affects basic tax, applicable credits, surtax, tax reduction and LIFT under ss. 6(2), 10, 16(3)-(4), 20(4)-(5) and 21.1(3.1). Keep the federal allocation calculation with the return.
- The tax is on the same T1 return as the federal tax, and CRA administers it. The result on ON428 line 90 goes on line 42800 of the return.
- It covers employees, the self-employed and retirees alike. The income type changes only the inputs: business income comes from ca-fed-t2125, CPP and EI amounts from ca-fed-cpp-ei.
- Not covered here:
  - Someone resident in another province on 31 December. Use that province's skill. The province on 31 December decides, even if the person lived in Ontario for most of the year.
  - Corporations and trusts. A trust pays no Ontario Health Premium (s. 24(3)) and has its own rates.
  - Ontario refundable credits on ON479, the Ontario Trillium Benefit (OEPTC, OSTC, NOEC) and the CARE credit. See on-tax-credits.
  - Employer Health Tax. See on-eht.
- Status Indians: Ontario says a person with a Certificate of Indian Status pays the health premium if their taxable income for the year was earned off-reserve and is more than $20,000. Refer any mix of on-reserve and off-reserve income to an accountant.

## Rates, bands and thresholds

Ontario tax on taxable income (ON428 Part A). Each rate applies only to the slice inside the band.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Band 1: taxable income up to $53,891 | 5.05% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 2: $53,891.01 to $107,785 | 9.15% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 3: $107,785.01 to $150,000 | 11.16% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 4: $150,000.01 to $220,000 | 12.16% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 5: over $220,000 | 13.16% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 1: taxable income up to $52,886 | 5.05% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 2: $52,886.01 to $105,775 (tax on lower bands $2,670.74) | 9.15% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 3: $105,775.01 to $150,000 (tax on lower bands $7,510.09) | 11.16% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 4: $150,000.01 to $220,000 (tax on lower bands $12,445.60) | 12.16% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 5: over $220,000 (tax on lower bands $20,957.60) | 13.16% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Indexation rate for Ontario amounts | 1.9% (2026), 2.8% (2025) | 2026, 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf |
| Ordinary non-refundable credit rate (CPP and EI included; donations calculated separately) | 5.05% | 2026, 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Basic personal amount | $12,989 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf |
| Basic personal amount | $12,747 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | base $12,132 less the other person's net income, maximum $11,029 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | base $11,905 less the other person's net income, maximum $10,823 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Age amount (65 or older on 31 December) | maximum $6,342, reduced by 15% of net income over $47,210, nil from $89,490 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf |
| Age amount (born in 1960 or earlier) | maximum $6,223, reduced by 15% of net income over $46,330, nil from $87,817 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Pension income amount | maximum $1,796 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf |
| Pension income amount | maximum $1,762 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Disability amount for self | $10,494 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf |
| Disability amount for self | $10,298 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Ontario caregiver amount, per dependant | base $27,066 less the dependant's net income, maximum $6,122 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf |
| Ontario caregiver amount, per dependant | base $26,562 less the dependant's net income, maximum $6,008 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Medical expenses: part not claimable | lesser of 3% of the relevant person's net income and $2,885 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Medical expenses: threshold and other-dependant limit | threshold is lesser of 3% of the relevant person's net income and $2,940; other-dependant eligible amount after their threshold is capped at $15,846 per dependant | 2026 | https://budget.ontario.ca/2026/fallstatement/provisions.html |
| Other-dependant medical expense limit after their threshold | $15,551 per dependant | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Disability supplement for a person under 18 at year-end | maximum $6,121, reduced by qualifying child/attendant care expenses above $3,585; added to the $10,494 basic disability amount | 2026 | https://budget.ontario.ca/2026/fallstatement/provisions.html |
| Disability supplement for a person under 18 at year-end | maximum $6,007, reduced by qualifying child/attendant care expenses above $3,518; added to the $10,298 basic disability amount | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Adoption expenses, eligible amount per child | $15,846 in 2026; $15,551 in 2025; shared parents cannot exceed one combined limit | 2026, 2025 | https://budget.ontario.ca/2026/fallstatement/provisions.html ; https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html |
| Donations and gifts credit | 5.05% on the first $200, 11.16% on the rest | 2026, 2025 | https://www.ontario.ca/laws/statute/07t11 |
| Dividend tax credit (share of the taxable amount of dividends) | eligible 10%, other than eligible 2.9863% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Dividend tax credit (share of the federal gross-up) | eligible 36.3158%; other than eligible 22.895% to 2026, 15.2283% from 2027 | 2026 | https://www.ontario.ca/laws/statute/07t11 |
| Ontario surtax | 20% of basic Ontario tax over $5,818, plus 36% of basic Ontario tax over $7,446 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf |
| Ontario surtax | 20% of basic Ontario tax over $5,710, plus 36% of basic Ontario tax over $7,307 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Ontario tax reduction | basic $300, plus $554 for each dependent child born in 2008 or later (under 18 at any time in 2026, s. 20(3)) and each dependant with an impairment; reduction is twice that total minus Ontario tax | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf |
| Ontario tax reduction | basic $294, plus $544 for each dependent child born in 2007 or later and each dependant with an impairment | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| LIFT credit | lesser of $875 and 5.05% of employment income, less 5% of the greater of adjusted net income over $32,500 and adjusted family net income over $65,000 | 2026, 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-a/5006-a-25e.pdf |
| LIFT credit: upper phase-out ceilings | no credit at individual adjusted net income $50,000 or family $82,500; a smaller employment-based maximum can reach zero earlier | 2026, 2025 | https://www.ontario.ca/page/low-income-individuals-and-families-tax-credit |
| Community food program donation credit for farmers | 25% of qualifying donations | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Ontario Health Premium | chart below; not indexed, same for 2025 and 2026 | 2026, 2025 | https://www.ontario.ca/laws/statute/07t11 |

What is indexed and what is not. Taxation Act s. 23(1) indexes the first two bracket limits, the third bracket limit except the $150,000, the credit amounts in s. 9, the surtax thresholds in s. 16 and the tax reduction amounts in s. 20(4) and (5). So $150,000 and $220,000 stay fixed and the surtax thresholds move every year. The LIFT figures (s. 21.1) and the Health Premium (s. 24) are not on the list and stay fixed.

Tax on the lower bands for 2026, computed from the CRA brackets the way ON428 line 7 shows it: $2,721.50 at $53,891, $7,652.80 at $107,785, $12,363.99 at $150,000, $20,875.99 at $220,000. The 2026 ON428 is not published yet, so check these against it when it comes out.

### Ontario Health Premium chart (ON428, line 89)

For an ordinary return without split income, use taxable income from line 26000. With split income, use combined income: line 26000 plus the split income taxed under s. 12.1, as required by s. 24(0.1) and the actual T1206 note. Use that combined income in every row of this chart. The 2025 ON428 prints these steps; s. 24(2) sets the same steps in law without indexing for 2026. Bankruptcy and optional death returns have separate rules below.

| Taxable income | Ontario Health Premium | Source URL |
|---|---|---|
| $20,000 or less | $0 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $20,000, not more than $25,000 | 6% of the amount over $20,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $25,000, not more than $36,000 | $300 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $36,000, not more than $38,500 | $300 plus 6% of the amount over $36,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $38,500, not more than $48,000 | $450 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $48,000, not more than $48,600 | $450 plus 25% of the amount over $48,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $48,600, not more than $72,000 | $600 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $72,000, not more than $72,600 | $600 plus 25% of the amount over $72,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $72,600, not more than $200,000 | $750 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $200,000, not more than $200,600 | $750 plus 25% of the amount over $200,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $200,600 | $900 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |

The same steps are in the law: https://www.ontario.ca/laws/statute/07t11 (s. 24(2)).

## The taxable base

Ontario starts from the finished federal return: complete steps 1 to 5 of the T1 first, then ON428 (CRA, Ontario tax information 2025). The order of ON428 is the method.

1. **Part A, tax on taxable income (line 8).** Take line 26000. Find the band, take the amount over the band floor, multiply by the band rate, round to the cent, add the tax on the lower bands.
2. **Part B, non-refundable credits (line 50).** Add the Ontario amounts that apply: basic personal amount, age, spouse or eligible dependant, caregiver, CPP or QPP contributions (lines 30800 and 31000), EI premiums (lines 31200 and 31217), adoption, pension, disability, interest on student loans, unused tuition and education amounts carried forward (Schedule ON(S11)), amounts transferred from a spouse (Schedule ON(S2)), and medical expenses over the threshold. Multiply the total by 5.05%. Add the donations credit: 5.05% on the first $200 and 11.16% on the rest.
   - Ontario amounts differ from the federal ones. Never copy a federal amount across. The eligibility rules are mostly the same as federal; the amounts are Ontario's (CRA, Ontario tax information 2025).
   - If a federal claim was reduced, for example for a newcomer or an emigrant, reduce the matching Ontario claim the same way.
3. **Basic Ontario tax (lines 53 to 61).** Line 53 is max(line 8 minus line 50, 0). Add the Ontario split-income amount on line 54 from the completed T1206, giving line 55. For an eligible 2025 minimum-tax carryover, calculate line 58 = max(line 53 minus the Ontario dividend credit on line 57, 0); line 59 = federal line 40427 x 24.63%; line 60 is the lesser of lines 58 and 59. Line 61 is max(line 55 minus line 60, 0). Do not deduct the whole federal carryover or deduct a dividend credit twice. Section 15(2) disallows the carryover when current-year minimum tax is payable. For a multiple-jurisdiction return, use the allocation-aware form instead. For 2026, s. 15(4) uses the Ontario lowest rate divided by the federal AMT rate, and the Ontario allocation factor; use the actual year's federal carryover and form instructions, not an assumed 2025 rounded factor.
4. **Surtax (lines 63 to 68).** Line 62 carries line 61. The surtax base on line 65 is max(line 62 minus the split-income tax on line 54, 0). Surtax S(B) = 20% x max(B minus the first threshold, 0) plus 36% x max(B minus the second threshold, 0), rounding each tax line to cents. Use $5,710/$7,307 for 2025 and $5,818/$7,446 for 2026. Add surtax to line 62 to get line 69. This is tax after non-refundable credits and any permitted minimum-tax carryover, before the dividend credit, reduction and LIFT. Do not apply surtax to taxable income or charge it again on the split-income tax.
5. **Dividend credit and current-year minimum tax (lines 70 to 73).** Line 70 is the dividend credit already calculated on line 57; line 71 = max(line 69 minus line 70, 0). In 2025, Worksheet ON428 line 72 starts with A = T691 Part 5 line 11 x 24.63%, then adds the incremental surtax S(A + line 65) minus existing line 68. Line 73 = line 71 plus line 72. Skipping line 72 understates tax. This is the Ontario bridge from a completed federal T691, not a replacement for the federal AMT computation. For 2026, s. 19.2(3.1), (4) and (5) require the actual statutory rate ratio and indexed surtax thresholds; obtain the correct-year T691 and Ontario instructions before finalizing. Do not treat a missing T691 as a zero. Sections 17 to 19 also require special calculations for qualifying retroactive lump sums, CPP/QPP benefit adjustments and section 40 ITAR amounts; obtain the applicable federal calculation and accountant review instead of treating these as ordinary income only.
6. **Ontario tax reduction (lines 74 to 80).** Personal amount = basic reduction plus the per-dependant amount for each qualifying dependent child under 18 at any time in the year (born in 2008 or later for 2026, 2007 or later for 2025) and each eligible dependant with an impairment. Line 80 = max(2 x personal amount minus line 73, 0); line 81 = max(line 73 minus line 80, 0). Check eligibility before using a count: an impairment alone does not establish an eligible dependant. See the dependency and residence rules below. The reduction is unavailable with current-year AMT, a bankruptcy in the calendar year, a trustee-filed bankruptcy return or ineligible residence. If line 73 is zero, line 80 is zero. A cohabiting spouse does not lose their own basic reduction merely because the other spouse has higher income; the higher-income rule governs the dependant additions.
7. **Provincial foreign tax credit (line 82)** from the actual Form T2036, after completing federal T2209. For each required country calculation, take the lesser of unused eligible foreign non-business tax and the Ontario-tax limit based on net foreign income/net income. T2036 note (4) requires a separate Ontario tax-otherwise-payable calculation with ON428 lines 70 and 72 set to zero and the calculation continued to line 81. It is not automatically all foreign tax left after the federal credit. Keep the normal return calculation intact. If total foreign non-business taxes exceed $200, T2036 requires a separate calculation per country; AMT and multiple-jurisdiction cases have additional notes. Do not substitute business-income tax or an invented allocation. Line 83 = max(line 81 minus line 82, 0).
8. **LIFT credit (line 85)** from Schedule ON428-A, subject to the detailed eligibility and adjusted-income steps below. Start with the lesser of $875 and 5.05% of employment income (lines 10100 and 10400). Reduce by 5% of the greater of adjusted individual net income over $32,500, adjusted family net income over $65,000, and zero; clamp the credit at zero. Single people use the individual test. A solely self-employed person with no employment income has a zero starting maximum. Line 86 = max(line 83 minus LIFT, 0). It never reduces the Health Premium, and unused credit is not refunded or carried forward.
9. **Community food program donation credit for farmers (line 87).** For qualifying Ontario agricultural-product donations to an eligible Ontario community food program, claim 25% of the eligible donation also claimed on federal Schedule 9 and Ontario line 58969. Check Ontario residence, farming income in the donation year, eligible product/recipient, receipts and no duplicate spousal claim. The 2025 instructions permit a five-year carryforward of the donations, even without farming income in the later claim year. Line 88 = max(line 86 minus line 87, 0), subject to the mandatory split-income comparison below.
10. **Ontario Health Premium (line 89)** from the chart, on taxable income plus applicable split income since 2024 (s. 24(0.1)). No credit, reduction or LIFT reduces the premium. For split income, complete T1206 Part 3's greater-of comparison and enter its Ontario result on line 88 before adding the premium; do not bypass that final minimum.
11. **Line 90** = the final line 88 plus line 89. Enter it on federal line 42800. This is only the Ontario component, not total federal/provincial tax or the amount payable after withholding and refundable credits. Preserve T1 reconciliation and refund/balance steps in ca-return-assembly.
Rounding: work each ON428 line to the cent. The surtax is worked on basic Ontario tax, not on taxable income. The premium is worked on taxable income, not on tax.

### Credit eligibility and supporting workpapers

Use the amounts for the return year, and record the original slip, receipt, certificate, assessment or supporting calculation. Non-refundable amounts reduce tax at 5.05%, not income dollar for dollar. Do not put enhanced CPP deductions into the base CPP credit again.

- **Age, pension and family amounts.** Age amount = max(year's age maximum minus 15% x max(relevant net income minus year's age threshold, 0), 0), subject to age eligibility. Pension amount is eligible pension income, limited to the Ontario maximum and federal eligibility, not all CPP, OAS or investment income. Spouse/eligible-dependant amount = min(year's maximum, max(year's base minus the other person's relevant net income, 0)), subject to the federal relationship, support and competing-claim rules. Get worldwide net income where required, even if that person files no return. Use TOSI-adjusted inputs when T1206 requires them.
- **Caregiver overlap.** First establish an eligible adult relative with an impairment and the support/residence conditions. For each dependant, compute the preliminary amount min(max(year's caregiver base minus their net income, 0), year's caregiver maximum), then subtract the Ontario eligible-dependant amount actually claimed for that same person on line 58160, flooring the result at zero. Worksheet ON428 2025 and TD1ON-WS 2026 both contain this subtraction. Do not add the full eligible-dependant and caregiver maxima for the same person. A parent without an impairment does not qualify merely because of age. The relative need not live with the claimant in every eligible caregiver case.
- **Disability and transfers.** Confirm eligibility under the federal disability rules and T2201. For an eligible person under 18 at year-end, supplement = max(supplement maximum minus max(qualifying child/attendant care expenses claimed by anyone minus the year's expense threshold, 0), 0). Add the supplement to the basic disability amount. A transfer from a dependant is only the unused amount calculated after their own tax and credits, not the whole disability maximum by default; use Worksheet ON428 and coordinate all supporting claimants. Different year-end provinces need the applicable special rules. Spousal age, pension and disability transfers use Schedule ON(S2) and the amount the spouse cannot use, not a duplicate full claim.
- **Medical expenses.** The self/spouse/minor-child basket uses the claimant's threshold; the other-dependant basket uses each other dependant's net income and per-dependant cap. Use eligible unreimbursed expenses for the same eligible claim period as the federal medical claim: ordinarily a 12-month period ending in the tax year; where the patient died during that year, federal Income Tax Act s. 118.2(1), descriptions B(d) and E(d), permits an eligible 24-month period including the day of death. Do not reuse expenses claimed for an earlier year or by another person. In 2025, the Ontario exceptions include attendant care limited federally to $10,000/$20,000 in a death year becoming $17,627/$35,253 for Ontario, adapted-van maximum $8,813, and accessible-dwelling moving expenses maximum $3,525. Those are 2025 figures only. The 2026 medical threshold and other-dependant cap above are confirmed; do not silently copy the 2025 special expense maxima into 2026. Establish disability/attendant-care interaction and reimbursements before claiming both.
- **Unused tuition and student-loan interest.** Ontario no longer accrues new tuition/education amounts after the 2017 phase-out. Use an actual Ontario assessment balance and Schedule ON(S11), not the federal balance or current tuition bill. The 2025 schedule says no claim if not resident in Ontario on 31 December 2017, and zero balance if resident then but not resident in Ontario on the last day of any year since 2021. Calculate current mandatory usage and remaining carryforward on the schedule; attach it to a paper return. Eligible student-loan interest follows federal qualifying-loan rules and can use the payment year or subsequent five years, without using the same payment twice.
- **Donations and dividends.** Ontario donations are limited to gifts actually used in the federal donation claim; ordinary individuals use 5.05% on the first $200 and 11.16% above it. On the actual 2025 Worksheet ON428, dividend credit = 2.9863% x line 12010 plus 10% x (line 12000 minus line 12010). These are taxable, grossed-up dividend amounts, not cash dividends. Section 19.1 preserves through 2026 the 22.895% share of the non-eligible federal gross-up and 36.3158% share of the eligible gross-up. Its enacted non-eligible change to 15.2283% starts in 2027, not 2026. Do not apply the future rate early or give a non-resident the resident dividend credit.

### Tax reduction: dependency, residence and unusual returns

Use the actual return-year ON428 and ss. 20(2)-(10). A qualifying child can generate the child addition and, where eligible, the impairment addition. Confirm the child lived with the claimant, the eligible-individual/Canada Child Benefit position and whether someone else became the child's eligible individual before year-end. The rule is not simply a count of every child financially supported. A spouse/partner claiming the child as their spouse, a Children's Special Allowances case, disputed support or shared custody needs its specific rules. Do not duplicate the same addition across claimants. For a cohabiting couple, only the higher-net-income person claims the dependant additions; bankruptcy has special deemed-income rules. Non-cohabiting shared impairment claims have their own majority/equal-share rule in s. 20(8).

For an ordinary year, confirm Canadian residence at the start and throughout the year, Ontario residence at year-end and all other eligibility. A person who left and returned during the year cannot rely only on two residence snapshots. The law excludes periods of non-residence in Canada, subject to its death-year wording. CRA explicitly permits a newcomer arriving on 1 January or emigrant leaving on 31 December where all conditions hold; it also allows the qualifying deceased resident's final return using the single-person rules. Do not extend these exceptions to an arbitrary midyear arrival or departure. A missing residence history is not a zero-tax conclusion.

### LIFT: adjusted income, eligibility and family facts

Use actual ON428-A Parts A/B and s. 21.1. For each required person, calculate adjusted net income as max(net income on line 23600, including a negative amount, plus UCCB repayment on line 21300 plus the RDSP repayment included on line 23200, minus UCCB income on line 11700 minus RDSP income on line 12500, 0). If T1206 applies, use its TOSI-adjusted net-income input where instructed. Family adjusted income is the sum of each person's separately calculated amount. Do not use the same net income for employment income, taxable income and adjusted family income.

For an ordinary return, confirm Canadian residence at the start and throughout the year and Ontario residence at year-end. LIFT is unavailable in a current-year AMT case, a bankruptcy year, a trustee-filed bankruptcy return, a trust, or where confinement includes 31 December of the previous year and the first 179 days of the current year. Apply the law and CRA death/first-day-arrival/last-day-departure exceptions only to their actual facts. For a spouse who died during the year, the actual 2025 schedule and instructions use Part A as single; the qualifying deceased person's final return also uses the single calculation. Otherwise obtain the actual year-end spouse information and their adjusted net income. Each eligible employed spouse calculates their own credit using their own employment income and the family test. The $50,000/$82,500 figures are upper ceilings for the maximum $875, not promised exact phase-out points for every employee.

### Mandatory split-income and minimum-tax handoff

Do not set T1206 or T691 to zero because their inputs are absent. Identify the applicable federal treatment first. For split income, the actual 2025 T1206 requires TOSI-adjusted net-income and, for specified credits, taxable-income inputs; Part 3 applies Ontario's 20.53% high rate and 5.05% low rate, credits against split income, and a greater-of calculation at lines 50 to 52. Its Ontario footnote directs the result back to ON428 line 88, then the Health Premium is added on lines 89/90. Complete Part 4 instead for a multiple-jurisdiction T2203 case. Preserve the completed form and all exclusions/allocations. A provisional ordinary ON428 total is not the final answer when TOSI is unresolved.

Minimum tax carryover and current-year AMT are different adjustments. Keep the actual federal carryover, current-year T691, Ontario carryover limit, incremental surtax and any foreign-credit adjustment as separate workpapers. The 2025 numerical bridges above are sourced to actual 2025 forms. For 2026 special AMT/TOSI returns, verify the year's federal/ provincial package, rate ratios and inputs before signing off. This skill does not replace the federal T691/T1206 computations.

For bankruptcy, do not charge a full Health Premium independently on every return. Section 24(4) aggregates combined income for the calendar year: the pre-bankruptcy premium is calculated first; the post-bankruptcy amount is the annual aggregate premium less the pre-bankruptcy amount. Section 24(4.1) deems the premium zero on the specified trustee in-bankruptcy return. Section 24(5) excludes income on the named optional death returns from the combined-income test; a qualifying final return still bears the appropriate premium. Keep all affected returns together for accountant review.

## Deadlines and filing

- Ontario tax is filed on the federal T1 return to CRA, with Form ON428 (and Schedule ON428-A for LIFT). There is no separate Ontario return. Ontario's own page tells the self-employed to pay the health premium as part of the return by completing ON428.
- 2025 return: file by April 30, 2026, or by June 15, 2026 if the person or their spouse or common-law partner is self-employed. Any balance owing was due April 30, 2026 in both cases.
- 2026 income, filed in 2027: most individual returns and payment are due 30 April 2027. The ordinary self-employed person/spouse filing deadline is 15 June 2027, but payment remains 30 April 2027. CRA's current 2027 fact sheet and Income Tax Act s. 150(1)(d) retain the exception for a business whose expenditures are primarily tax-shelter investment costs. Death returns and other special extensions use their own rules in ca-fed-t1-return; do not blindly apply the ordinary calendar.
- Employers deduct Ontario tax and the Health Premium from pay (T4127, Form TD1ON). For self-employed instalments see ca-fed-instalments. For filing channels and the federal return itself see ca-fed-t1-return.

## Penalties and interest

These are federal rules. CRA applies them to the whole balance owing on the T1, Ontario tax included.

- Late filing with a balance owing: 5% of the balance owing, plus 1% of the balance for each full month late, up to 12 months.
- Repeat late filing: 10% of the balance owing, plus 2% for each full month late, up to 20 months, if a late-filing penalty was charged in any of the three previous years and CRA sent a demand to file.
- Interest: compound daily interest on any unpaid amount from the day after the due date, reassessed amounts included, at CRA's prescribed rate, which can change every three months.

## Cross-border points

- **Interprovincial residence.** For an ordinary Canadian-resident return, the province of residence at year-end determines the provincial package, subject to multi-jurisdiction business allocation. This does not mean an immigrant is taxed on unrestricted worldwide income for a pre-residence period, or that a departure/death return uses a fictional 31 December residence. Use ca-tax-residency and the actual residence/departure/death date.
- **Newcomers and emigrants.** A person who arrived in or left Canada during the year may have to reduce some Ontario credits, the same way as the federal claims. A newcomer arriving on January 1, or an emigrant leaving on December 31, may still claim the tax reduction and LIFT if resident in Ontario on December 31 and the other conditions are met (CRA, Ontario tax information 2025). Departure tax: see leaving-canada-departure-tax.
- **Business in more than one province.** An Ontario resident with business income from a permanent establishment outside Ontario pays Ontario tax only on the Ontario share, using the Ontario allocation factor from Form T2203 (Taxation Act s. 6(2)). The surtax and the basic tax reduction are scaled by the same factor (s. 16(4), s. 20(4)). Flag for an accountant.
- **Non-residents with Ontario income.** A non-resident of Canada with employment income only in Ontario, or business income from a permanent establishment only in Ontario, uses ON428 (s. 4(1) para. 3). The Health Premium applies only to Ontario residents: s. 24(1) charges it on the people in paragraphs 1 and 2 of s. 4(1), not paragraph 3.
- **Foreign tax.** Foreign non-business income tax not fully credited against federal tax may give a provincial foreign tax credit on Form T2036 (s. 21).

## Worked examples

### Example 1: 2026, single employee on a low income (tax reduction, LIFT and the Health Premium)

Amira is 30, single, with no dependants, and lives in Toronto all of 2026. Her only income is employment income of $34,000. Her T4 shows base CPP contributions of $1,509.75 (line 30800) and EI premiums of $554.20 (line 31200). After the enhanced CPP deduction of $305 on line 22215, her net income (line 23600) and taxable income (line 26000) are both $33,695.

- Part A: $33,695 is in band 1. $33,695 x 5.05% = $1,701.60 (line 8).
- Part B: $12,989 + $1,509.75 + $554.20 = $15,052.95. Times 5.05% = $760.17 (line 50).
- Basic Ontario tax: $1,701.60 - $760.17 = $941.43. That is below $5,818, so no surtax. Line 73 is $941.43.
- Tax reduction: 2 x $300 = $600, minus $941.43, is negative, so the reduction is nil.
- LIFT: the lesser of $875 and 5.05% x $34,000 ($1,717.00) is $875. Her adjusted net income of $33,695 is $1,195 over $32,500, and 5% of that is $59.75. LIFT = $875 - $59.75 = $815.25. Ontario tax after LIFT: $941.43 - $815.25 = $126.18.
- Health Premium: taxable income of $33,695 is in the $25,000 to $36,000 step, so $300.
- Ontario tax, line 90 (to line 42800): $126.18 + $300 = $426.18. Most of what she pays is the premium, which LIFT cannot reduce.

```oa-check
name: Ontario 2026, single employee, taxable income 33,695
inputs:
  taxable_income: 33695
  employment_income: 34000
  adjusted_net_income: 33695
  cpp_30800: 1509.75
  ei_31200: 554.20
  bpa: 12989
  reduction_basic: 300
steps:
  - line8: round(taxable_income * 0.0505, 2)
  - line50: round((bpa + cpp_30800 + ei_31200) * 0.0505, 2)
  - line53: max(line8 - line50, 0)
  - surtax: round(max(line53 - 5818, 0) * 0.20, 2) + round(max(line53 - 7446, 0) * 0.36, 2)
  - line73: line53 + surtax
  - reduction: max(2 * reduction_basic - line73, 0)
  - line83: max(line73 - reduction, 0)
  - lift_max: min(875, round(employment_income * 0.0505, 2))
  - lift: max(lift_max - round(max(adjusted_net_income - 32500, 0) * 0.05, 2), 0)
  - line86: max(line83 - lift, 0)
  - ohp: 300
  - ontario_tax: line86 + ohp
expected:
  line8: 1701.60
  line50: 760.17
  line53: 941.43
  reduction: 0
  lift: 815.25
  ontario_tax: 426.18
```

### Example 2: 2025, married high earner with surtax and donations

Daniel lives in Ottawa all of 2025. He is 45 and married, and his spouse had no income in 2025. His taxable income (line 26000) is $180,000, all from employment. He paid base CPP of $3,356.10 (line 30800) and EI of $1,077.48 (line 31200), and gave $1,000 to registered charities. He has no children.

- Part A: $180,000 is in band 4. ($180,000 - $150,000) x 12.16% = $3,648.00, plus $12,445.60 = $16,093.60 (line 8).
- Part B: $12,747 basic, plus the spouse amount ($11,905 - $0 = $11,905, capped at $10,823), plus $3,356.10 and $1,077.48, makes $28,003.58. Times 5.05% = $1,414.18. Donations: $200 x 5.05% = $10.10, plus $800 x 11.16% = $89.28, total $99.38. Line 50 = $1,513.56.
- Basic Ontario tax: $16,093.60 - $1,513.56 = $14,580.04.
- Surtax: ($14,580.04 - $5,710) x 20% = $1,774.01, plus ($14,580.04 - $7,307) x 36% = $2,618.29. Surtax $4,392.30. Line 69 = $18,972.34.
- Tax reduction: 2 x $294 = $588 is far below his tax, so nil. LIFT is nil at his income.
- Health Premium: $180,000 is in the $72,600 to $200,000 step, so $750.
- Ontario tax, line 90: $18,972.34 + $750 = $19,722.34. The surtax adds about 30% to his basic Ontario tax.

```oa-check
name: Ontario 2025, married, taxable income 180,000, donations 1,000
inputs:
  taxable_income: 180000
  bpa: 12747
  spouse_base: 11905
  spouse_net_income: 0
  spouse_max: 10823
  cpp_30800: 3356.10
  ei_31200: 1077.48
  donations: 1000
  reduction_basic: 294
steps:
  - line8: round((taxable_income - 150000) * 0.1216, 2) + 12445.60
  - spouse_amount: min(max(spouse_base - spouse_net_income, 0), spouse_max)
  - line46: round((bpa + spouse_amount + cpp_30800 + ei_31200) * 0.0505, 2)
  - line49: round(min(donations, 200) * 0.0505, 2) + round(max(donations - 200, 0) * 0.1116, 2)
  - line50: line46 + line49
  - line53: max(line8 - line50, 0)
  - surtax: round(max(line53 - 5710, 0) * 0.20, 2) + round(max(line53 - 7307, 0) * 0.36, 2)
  - line69: line53 + surtax
  - reduction: max(2 * reduction_basic - line69, 0)
  - ohp: 750
  - ontario_tax: line69 - reduction + ohp
expected:
  line8: 16093.60
  line50: 1513.56
  line53: 14580.04
  surtax: 4392.30
  line69: 18972.34
  ontario_tax: 19722.34
```

### Example 3: 2026 caregiver and eligible-dependant overlap

A claimant has established that an adult dependant with an impairment qualifies, including all support and residence tests. The dependant's net income is $10,000; the claimant's eligible-dependant amount for this person is $2,132. The caregiver preliminary amount is $6,122, but the same-person subtraction leaves $3,990, giving $201.50 of caregiver tax credit. It is not a second full $6,122 claim. With zero dependant income and the full $11,029 eligible-dependant amount, this caregiver amount is zero. These component results assume the claimant has enough Ontario tax to use the credit.

```oa-check
name: Ontario 2026 caregiver same-person overlap
inputs:
  dependant_net_income: 10000
  eligible_dependant_amount: 2132
steps:
  - preliminary: min(max(27066 - dependant_net_income, 0), 6122)
  - caregiver_amount: max(preliminary - eligible_dependant_amount, 0)
  - caregiver_credit: round(caregiver_amount * 0.0505, 2)
  - no_income_caregiver: max(6122 - 11029, 0)
expected:
  preliminary: 6122
  caregiver_amount: 3990
  caregiver_credit: 201.50
  no_income_caregiver: 0
```

### Example 4: 2026 separate medical baskets and the child disability supplement

Assume eligible unreimbursed expenses and valid disability/support facts. A claimant with net income $100,000 has $5,000 in the self/spouse/minor-child medical basket. The threshold is $2,940, leaving $2,060. Separately, eligible expenses for an adult dependant are $20,000 and that person's net income is $30,000. Their own threshold is $900; the $19,100 excess is capped at $15,846. Total eligible Ontario medical amount is $17,906, yielding $904.25 of credit before non-refundable limits. Do not use the claimant's net income for the adult dependant.

Separately, an eligible disabled child under 18 at year-end has qualifying child/attendant care expenses of $5,000 claimed by the family. The 2026 supplement is $6,121 minus ($5,000 minus $3,585) = $4,706; with the basic disability amount, the child's disability amount is $15,200. This is not automatically the parent's transferred amount; calculate what the child needs first and check the medical/disability interaction.

```oa-check
name: Ontario 2026 medical baskets and disability supplement
inputs:
  claimant_net: 100000
  self_expenses: 5000
  other_net: 30000
  other_expenses: 20000
  care_expenses: 5000
steps:
  - self_threshold: min(round(claimant_net * 0.03, 2), 2940)
  - self_allowable: max(self_expenses - self_threshold, 0)
  - other_threshold: min(round(other_net * 0.03, 2), 2940)
  - other_allowable: min(max(other_expenses - other_threshold, 0), 15846)
  - medical_amount: self_allowable + other_allowable
  - medical_credit: round(medical_amount * 0.0505, 2)
  - supplement: max(6121 - max(care_expenses - 3585, 0), 0)
  - disability_amount: 10494 + supplement
expected:
  self_threshold: 2940
  self_allowable: 2060
  other_threshold: 900
  other_allowable: 15846
  medical_amount: 17906
  medical_credit: 904.25
  supplement: 4706
  disability_amount: 15200
```

### Example 5: LIFT adjusted income, family phase-out and an early zero

An otherwise eligible employee has $5,000 employment income and $40,000 adjusted individual net income from all sources. The starting maximum is only $252.50; the $375 reduction makes LIFT zero before the $50,000 upper ceiling. Sole-proprietor profit alone would not create an employment-based maximum.

For a different eligible employee, net income is $31,000, UCCB repayments are $1,200, RDSP repayments are $800, UCCB income is $1,000 and RDSP income is $500. Adjusted individual net income is $31,500. If their spouse's separately calculated adjusted net income is $40,000, family income is $71,500. With $30,000 employment income, the maximum $875 is reduced by $325 under the family test, leaving $550 before the available-tax limit. The repayment/income amounts here are stipulated verified inputs, not a claim that everyone receives those payments.

```oa-check
name: Ontario LIFT smaller maximum and adjusted family income
inputs:
  low_employment: 5000
  low_adjusted_net: 40000
  employment: 30000
  net_income: 31000
  uccb_repayment: 1200
  rdsp_repayment: 800
  uccb_income: 1000
  rdsp_income: 500
  spouse_adjusted: 40000
steps:
  - low_maximum: min(875, round(low_employment * 0.0505, 2))
  - low_reduction: round(max(low_adjusted_net - 32500, 0) * 0.05, 2)
  - early_zero: max(low_maximum - low_reduction, 0)
  - adjusted_individual: max(net_income + uccb_repayment + rdsp_repayment - uccb_income - rdsp_income, 0)
  - adjusted_family: adjusted_individual + spouse_adjusted
  - maximum: min(875, round(employment * 0.0505, 2))
  - reduction: round(max(adjusted_individual - 32500, adjusted_family - 65000, 0) * 0.05, 2)
  - credit: max(maximum - reduction, 0)
expected:
  low_maximum: 252.50
  low_reduction: 375
  early_zero: 0
  adjusted_individual: 31500
  adjusted_family: 71500
  maximum: 875
  reduction: 325
  credit: 550
```

### Example 6: actual 2025 AMT and carryover bridges

These are two independent component checks, not a fabricated complete federal T691. In the current-year AMT case, a completed T691 Part 5 line 11 supplies $10,000 and ON428 line 65 is $7,000. Ontario basic additional tax is $2,463. Existing surtax is $258; surtax on $9,463 is $1,526.76, so incremental surtax is $1,268.76. Line 72 must be $3,731.76, not just $2,463. Tax reduction and LIFT are unavailable in this AMT case.

In a separate year/case without current-year AMT, assume line 53 $1,000, Ontario dividend credit $200 and a valid federal minimum-tax carryover claim on line 40427 of $10,000. The 2025 percentage calculation is $2,463 but the Ontario ordinary-tax limit is $800, so line 60 is $800. That case does not simultaneously claim current-year AMT and its carryover credit.

```oa-check
name: Ontario 2025 current AMT incremental surtax and separate carryover limit
inputs:
  federal_amt_excess: 10000
  line65: 7000
  ordinary_tax: 1000
  dividend_credit: 200
  federal_carryover: 10000
steps:
  - basic_additional: round(federal_amt_excess * 0.2463, 2)
  - existing_surtax: round(max(line65 - 5710, 0) * 0.20, 2) + round(max(line65 - 7307, 0) * 0.36, 2)
  - augmented_base: line65 + basic_additional
  - augmented_surtax: round(max(augmented_base - 5710, 0) * 0.20, 2) + round(max(augmented_base - 7307, 0) * 0.36, 2)
  - incremental_surtax: augmented_surtax - existing_surtax
  - line72: basic_additional + incremental_surtax
  - carryover_tax_limit: max(ordinary_tax - dividend_credit, 0)
  - percentage_limit: round(federal_carryover * 0.2463, 2)
  - line60: min(carryover_tax_limit, percentage_limit)
expected:
  basic_additional: 2463
  existing_surtax: 258
  augmented_base: 9463
  augmented_surtax: 1526.76
  incremental_surtax: 1268.76
  line72: 3731.76
  carryover_tax_limit: 800
  percentage_limit: 2463
  line60: 800
```

### Example 7: 2025 TOSI final minimum and premium base

For this handoff check, assume a completed T1206, not an unresolved split-income classification. Its Part 3 line 50 is $2,000, while the ordinary Ontario result supplied to its line 51 is $1,500. Line 52 is the greater amount, $2,000; the Ontario footnote returns that amount to ON428 line 88. With taxable income $19,000 and split income $10,000, combined income for the Health Premium is $29,000 and the premium is $300. Ontario line 90 is $2,300. Taking the ordinary result and testing only $19,000 would incorrectly omit both the floor and premium. The stipulated completed-form floor includes all relevant credits; this example does not derive a full T1206 from gross split income alone.

```oa-check
name: Ontario 2025 TOSI greater-of handoff before Health Premium
inputs:
  tosi_line50: 2000
  ordinary_line51: 1500
  taxable_income: 19000
  split_income: 10000
steps:
  - line88: max(tosi_line50, ordinary_line51)
  - combined_income: taxable_income + split_income
  - premium: min(round(max(combined_income - 20000, 0) * 0.06, 2), 300)
  - line90: line88 + premium
expected:
  line88: 2000
  combined_income: 29000
  premium: 300
  line90: 2300
```

### Example 8: dividend bases and a capped foreign-tax credit

For 2025, a taxable eligible-dividend amount of $13,800 and taxable non-eligible amount of $11,500 produce Ontario credits $1,380 and $343.42, total $1,723.42. Use taxable slip amounts, not the original cash dividend or a second gross-up.

In a separate ordinary 2025 foreign-credit case, eligible non-business foreign tax is $800 and the completed federal credit is $500, leaving $300. The Ontario tax-otherwise-payable workpaper required by T2036 note (4) gives $2,000, net foreign income is $5,000 and net income is $50,000. The Ontario limit is $200, so the credit is $200, not the full $300 left federally. All amounts are Canadian dollars and the example assumes one country and no AMT/TOSI or allocation issues.

```oa-check
name: Ontario 2025 taxable dividend bases and T2036 limit
inputs:
  eligible_taxable: 13800
  noneligible_taxable: 11500
  foreign_tax: 800
  federal_credit: 500
  ontario_otherwise_payable: 2000
  foreign_net: 5000
  net_income: 50000
steps:
  - eligible_credit: round(eligible_taxable * 0.10, 2)
  - noneligible_credit: round(noneligible_taxable * 0.029863, 2)
  - dividend_credit: eligible_credit + noneligible_credit
  - unused_foreign_tax: max(foreign_tax - federal_credit, 0)
  - ontario_limit: round(ontario_otherwise_payable * foreign_net / net_income, 2)
  - provincial_credit: min(unused_foreign_tax, ontario_limit)
expected:
  eligible_credit: 1380
  noneligible_credit: 343.42
  dividend_credit: 1723.42
  unused_foreign_tax: 300
  ontario_limit: 200
  provincial_credit: 200
```

## Ask the client first

1. Which province did you live in on 31 December (or on the date you left Canada)? Were you resident in Canada on 1 January?
2. Your federal figures once the T1 is done: taxable income (line 26000), net income (line 23600), employment income (lines 10100 and 10400), CPP and EI amounts (lines 30800, 31000, 31200, 31217), dividends (lines 12000 and 12010), and any split income on Form T1206.
3. Did you have a spouse or common-law partner on 31 December, and what was their net income? This decides the spouse amount, the LIFT family test and who claims the tax reduction for dependants.
4. Which children born in 2008 or later (2007 or later for a 2025 return), or dependants with an impairment, qualify under the actual support/residence rules? Obtain their net incomes, who claims eligible-dependant/caregiver/disability amounts, shared custody/CCB facts and amounts already claimed by anyone.
5. Your age on 31 December, pension income, disability tax credit certificate, medical expenses, donations, and unused tuition carried forward.
6. Any business with a place of business outside Ontario, foreign tax paid by country, bankruptcy or trustee-filed return, confinement spanning the prior 31 December and first 179 days, death, minimum tax (T691), minimum-tax carryover or tax on split income (T1206)? Get the complete forms and residence history. Each changes the method; refer unresolved cases to an accountant.
7. For LIFT, obtain employment income separately from business income, each required person's UCCB/RDSP income and repayments, the actual spouse/death dates and the final adjusted-income calculation. For Ontario tuition, obtain the Ontario assessment balance and year-end residence history since 2017.

## Sources

| Source | URL | Read on |
|---|---|---|
| CRA, Form ON428 Ontario Tax 2025 (5006-C), read for Parts A, B and C and the line 89 chart | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf | 2026-11-14 |
| CRA, Worksheet ON428 2025 (5006-D), read for the age amount, caregiver amount and dividend tax credit lines | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf | 2026-11-14 |
| CRA, Schedule ON428-A, LIFT credit 2025 (5006-A), read for Parts A and B | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-a/5006-a-25e.pdf | 2026-11-14 |
| CRA, Ontario tax information 2025 (5006-PC), read for who completes ON428, newcomers and emigrants, tax reduction, line 89 | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html | 2026-11-14 |
| CRA, Tax rates and brackets, current year (2026), read for the Ontario rate table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-14 |
| CRA, Tax rates and brackets, last year (2025), read for the Ontario rate table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html | 2026-11-14 |
| CRA, T4127 Payroll Deductions Formulas, 122nd edition, effective January 1, 2026, read for the Ontario factors V1, V2, S and Tables 8.2 and 8.23 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf | 2026-11-14 |
| CRA, Form TD1ON 2026, Ontario Personal Tax Credits Return, read for lines 1 to 6 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf | 2026-11-14 |
| CRA, Worksheet TD1ON-WS 2026, read for the age, spouse, eligible dependant and caregiver parts | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf | 2026-11-14 |
| CRA, Due dates and payment dates, personal income tax, read for the filing and payment due dates | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-14 |
| CRA, Interest and penalties on late taxes, read for the late-filing penalty and interest | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | 2026-11-14 |
| CRA, CPP contribution rates, maximums and exemptions, read for the 2025 row (example 2 input) | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html | 2026-11-14 |
| CRA, EI premium rates and maximums, read for the 2025 row (example 2 input) | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html | 2026-11-14 |
| Ontario, Taxation Act, 2007, S.O. 2007, c. 11, Sch. A consolidation from July 1, 2026, read for ss. 3, 4, 6, 9, 16, 19.1, 20, 21, 21.1, 23 and 24 | https://www.ontario.ca/laws/statute/07t11 | 2026-11-14 |
| Ontario, Low-income Individuals and Families Tax (LIFT) Credit, read for eligibility and the 2022 onward calculation | https://www.ontario.ca/page/low-income-individuals-and-families-tax-credit | 2026-11-14 |
| Ontario, Ontario Tax Reduction, read for eligibility and the spouse rule | https://www.ontario.ca/page/ontario-tax-reduction | 2026-11-14 |
| Ontario, Health premium, read for who pays and Status card holders | https://www.ontario.ca/page/health-premium | 2026-11-14 |
| Ontario, actual official Word consolidation of Taxation Act, 2007, from 1 July 2026; relevant ss. 3 to 24, read in the downloaded law rather than the JavaScript shell | https://www.ontario.ca/laws/docs/07t11_e.doc | 2026-11-14 |
| Ontario, 2026 Fall Statement tax provisions, personal-income-tax indexed credits and reduction/LIFT descriptions, read with the law | https://budget.ontario.ca/2026/fallstatement/provisions.html | 2026-11-14 |
| CRA, current ON428 catalogue, actual available edition check | https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5006-c.html | 2026-11-14 |
| CRA, actual 2025 T1206, Ontario notes, Chart C and Part 3/Part 4 handoff | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1206/t1206-25e.pdf | 2026-11-14 |
| CRA, actual 2025 T2036, both pages including Ontario AMT and tax-otherwise-payable notes | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2036/t2036-25e.pdf | 2026-11-14 |
| CRA, actual 2025 Schedule ON(S11), assessment balance, claim and carryforward/residence restrictions | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-s11/5006-s11-25e.pdf | 2026-11-14 |
| CRA, current 2027 filing/payment fact sheet for 2026 self-employed income | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html | 2026-11-14 |
| Federal Income Tax Act, s. 150(1)(d), ordinary and special filing dates | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Federal Income Tax Act, s. 118.2(1) descriptions B(d)/E(d), ordinary and eligible death-year medical claim periods, read with Ontario s. 9(20) | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.2.html | 2026-11-14 |
| Federal Income Tax Act, ss. 162(1)-(2) and 161(1), late-filing conditions and unpaid-tax interest | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html ; https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html | 2026-11-14 |
| Federal Income Tax Act, ss. 127.51 and 82(1)(b), AMT statutory rate denominator and dividend gross-up branches | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-127.51.html ; https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html | 2026-11-14 |

Not yet confirmed and remaining limits, as checked on 14 November 2026: the CRA ON428 catalogue still offers the 2025 edition; 2026 lower-band constants remain derived from current rates, not confirmed 2026 printed fields. Current Ontario publications now confirm the 2026 medical threshold, other-dependant cap and under-18 disability supplement above. The specific 2026 attendant-care, adapted-van and accessible-dwelling moving expense maxima have not been confirmed in the sources read; do not roll forward 2025 limits. The 2026 dividend rule is supported in law as a share of the federal gross-up, not a read-off of a 2026 Worksheet ON428. Filing channels remain in ca-fed-t1-return. Actual 2025 T691/T1206 bridges are described, but full federal AMT and TOSI engines, cross-province allocation, disputed dependency and complex bankruptcy/death returns require the completed source forms and an accountant. No approval is inferred from a directory name or a source audit.
