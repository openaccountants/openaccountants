---
name: ab-individual-return
description: "Alberta provincial personal income tax for an individual resident in Alberta on 31 December, worked through Form AB428 (Alberta Tax and Credits) on the T1 return. Primary tax year 2026, with a dated section carrying the full 2025 figures. Covers the six brackets (8%, 10%, 12%, 13%, 14%, 15%) including the 8% bracket added from 2025, the Alberta basic personal amount and the main non-refundable credits, the 8% credit rate, the Alberta supplemental tax credit, donations, medical expenses, the dividend tax credit, political contributions, minimum tax and indexing. Trigger on 'Alberta tax', 'AB428', 'Alberta tax brackets', 'Alberta 8% bracket', 'Alberta basic personal amount', 'Alberta supplemental tax credit', 'line 42800 Alberta'. Out of scope: federal tax (ca-fed-t1-return), CPP and EI (ca-fed-cpp-ei), instalments (ca-fed-instalments), self-employed expenses (ca-ab-deductions-for-self-employed-independent-contractor), emigrating (ca-ab-departure-tax-t1244-security-election-defer), companies (ab-corporate-tax)."
version: 1.2
jurisdiction: CA-AB
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Alberta personal income tax (Form AB428), tax year 2026, with 2025 figures

> **Built from the law.** Alberta provincial income tax, using the CRA annual forms, published 2026 parameters and the Alberta legislation identified below. Not yet approved by an accountant. The source table distinguishes the official material reread on 14 November 2026 from the historical statutory references whose current text could not be obtained in this audit.

Built by Michael Cutajar and the OpenAccountants team.

Tax year: the calendar year. Currency: Canadian dollars. Alberta sets the law. The Canada Revenue Agency (CRA) runs it on the federal T1 return. The ordinary result goes on line 42800 of the return (2025 Form AB428, line 75). If tax on split income applies, perform the final T1206 comparison before reporting that amount.

**Edition and completion gate.** The main income year is 2026, filed in 2027. The current CRA AB428 catalogue obtained on 14 November 2026 offers the 2025 annual form; no final 2026 AB428, annual worksheet, AB(S2), AB(S11) or T2203 was obtained. Numbered annual fields below belong to the actual 2025 editions. Published 2026 rates and TD1AB parameters support estimates, not a claim that the final 2026 fields have been checked. Three indexed parameters and unchanged provincial special-credit provisions still need the fresh statutory/actual-year check described in Sources. Keep those estimates and incomplete branches distinct from a completed filing.

**Evidence and attribution.** Record each required input as supplied, verified, not applicable or unresolved. Unknown is not zero. A conditional single-person illustration must not establish the client's marital status. Historical construction credit above is not an accountant approval; use only the actual per-skill approval record. A country-level reviewer name, a search result or another Canadian skill cannot establish approval of this Alberta method or the client's return.

Old figures to drop: Alberta no longer has a single flat 10% rate. From the 2025 tax year the first band is taxed at 8%, and credits are worked out at 8% (Act s.4).

See also: `ca-fed-t1-return` (federal tax and the federal credits), `ca-fed-cpp-ei`, `ca-fed-instalments`, `ca-capital-gains`, `ca-tax-residency`, `ca-ab-deductions-for-self-employed-independent-contractor`, `ca-ab-departure-tax-t1244-security-election-defer`, `ab-corporate-tax`.

## Who this applies to

**Residents on 31 December.** An individual who was resident in Alberta on the last day of the calendar year must pay Alberta tax (Act s.3(1)(a)). The tax is worked out on the whole year's taxable income (s.6.1(1)). So the province you live in on 31 December decides the provincial tax for the year, even if you moved in during the year. Use `ca-tax-residency` for the residential ties test.

**Alberta residents with business income outside Alberta.** The original statutory allocation summary is T x (C - D) / C, where T is the relevant Alberta tax, C is income for the year and D is business income earned outside Alberta (s.6.1(3), historical reference). It is not an instruction to multiply final ordinary AB428 tax by a percentage. CRA directs an Alberta resident with an outside-Alberta business permanent establishment to T2203 instead of ordinary AB428. Use the actual AB428MJ sequence below, including resident adjustments and the separate supplemental worksheet.

**Residents of another province with Alberta business income.** Screen Alberta business permanent establishments and allocate using T2203. The original statutory summary is T x C / D, where C is the Alberta business income and D is income for the year (ss.3(1)(b), 6.1(4), historical references). Establish the form's actual income allocation, credit population and Alberta-resident exclusions before applying its percentage. An employee working temporarily in another Canadian province does not acquire business permanent establishments solely from those wages.

**Part-year residents who leave Canada.** An individual resident in Alberta for part of the year, who did not live in another province after leaving Alberta, and who was resident outside Canada on the last day of the year, is taxed under s.6.1(5). Part-year credit limits are in s.36.1 and the emigrant proration in s.40. Use `ca-ab-departure-tax-t1244-security-election-defer` for departure tax.

**Non-residents of Canada with Canadian income** require a route and credit-restriction check. CRA's actual 2025 Alberta information directs a Canada-non-resident with employment only in Alberta, or a business permanent establishment only in Alberta, to ordinary AB428. Multiple provinces/territories or permanent establishments can require T2203. Establish Canadian taxable income and actual federal non-resident entitlements first. Do not claim resident-only adoption or pension amounts, full-year personal maxima or a foreign credit merely because Alberta-source income exists. The original statutory liability reference is s.3(1)(c); its precise current scope remains in the fresh-read queue in Sources.

**Not here:** the federal calculation (`ca-fed-t1-return`), companies (`ab-corporate-tax`), and trusts. A trust taxed under s.122 of the federal Act pays the top Alberta rate on all its taxable income (s.6.1(1)(b)).

## Rates, bands and thresholds

Alberta taxable income is the same as federal taxable income (s.5(1)), line 26000 of the return.

**Tax year 2026.** Bands from the CRA's 2026 rate page. Credit amounts from the CRA's 2026 TD1AB. Alberta says: "In 2026, thresholds and credit amounts will rise by 2%."

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income up to $61,200 | 8% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $61,200.01 to $154,259 | 10% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $154,259.01 to $185,111 | 12% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $185,111.01 to $246,813 | 13% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $246,813.01 to $370,220 | 14% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over $370,220 | 15% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Rate used for non-refundable credits ("specified percentage") | 8% | 2025 and later | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.4) |
| Alberta indexing factor | 2.0% | 2026 | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html (Table 8.2, index rate) |
| Basic personal amount | $22,769 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | $22,769 minus the spouse's or dependant's net income | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Age amount (65 or older on 31 December) | $6,345, reduced when net income is over $47,234, nil at $89,534 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Pension income amount | Up to $1,753 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Disability amount | $17,563 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Caregiver amount | Up to $13,180; full if the dependant's net income is $20,956 or less, nil at $34,136 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Amount for infirm dependants 18 or older | Up to $13,180; full if the dependant's net income is $8,707 or less, nil at $21,887 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Disability supplement for a person under 18 | Up to $13,180 | 2026 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (Tax Plan, Non-Refundable Tax Credits table, printed page 130) |
| Adoption expenses | Up to $19,741 | 2026 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (Tax Plan, Non-Refundable Tax Credits table, printed page 130) |
| Donations: first $200, then the rest | 60%, then 21% (not indexed) | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.11(1)) |
| Political contributions credit | 75% of the first $200, 50% of the next $900, 33.33% of the rest, at most $1,000 (fixed in the Act, not indexed) | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.24(2.1)) |
| Minimum tax carryover | 35% of the federal minimum tax carryover | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.27(1)) |

Alberta's Budget 2026 Fiscal Plan says "Credit amounts have increased by 2% from 2025 due to the Alberta escalator." Three 2026 amounts are not printed by the CRA or Alberta yet, because the 2026 Form AB428 comes out with the 2026 tax package. The Act sets each one as the 2025 figure plus the Alberta escalator, rounded to the nearest dollar (s.44.2(1) and (4)). At 2% they work out as below. Check them against the 2026 AB428 when it is out:

- medical expense threshold: the lesser of $2,942 (2025: $2,884) and 3% of net income;
- supplemental tax credit base: $4,896 (2025: $4,800);
- child care and attendant care threshold for the under-18 disability supplement: $3,594 (2025: $3,524).

The method is backed up by the TD1AB: its 2026 basic personal amount ($22,769), age amount ($6,345 and $47,234) and pension amount ($1,753) are each the 2025 figure times 1.02, rounded.

**Tax year 2025.** From the CRA's 2025 rate page, 2025 Form AB428 and 2025 Worksheet AB428.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income up to $60,000 | 8% | 2025 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html |
| $60,000.01 to $151,234 | 10% (AB428 adds $4,800 for the first band) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| $151,234.01 to $181,481 | 12% (plus $13,923.40) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| $181,481.01 to $241,974 | 13% (plus $17,553.04) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| $241,974.01 to $362,961 | 14% (plus $25,417.13) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Over $362,961 | 15% (plus $42,355.31) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Non-refundable credit rate | 8% (AB428 line 53) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Basic personal amount | $22,323 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Spouse or common-law partner amount, and eligible dependant amount | $22,323 minus that person's net income | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Age amount (born in 1960 or earlier) | $6,221, reduced by 15% of net income over $46,308, nil at $87,782 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Pension income amount | Up to $1,719 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Disability amount for self | $17,219; under 18, a supplement of up to $12,922 less child and attendant care over $3,524, total at most $30,141 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Caregiver amount | $33,467 minus the dependant's net income, at most $12,922 per dependant | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Amount for infirm dependants 18 or older | $21,458 minus the dependant's net income, at most $12,922 per dependant | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Medical expenses | Expenses over the lesser of $2,884 and 3% of net income | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Adoption expenses | Up to $19,354 | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.13.1(2)) |
| Supplemental tax credit | 25% of (credits at 8%, leaving out unused tuition, minus $4,800) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Dividend tax credit | 8.12% of the taxable amount of eligible dividends; 2.18% of the taxable amount of other dividends | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Minimum tax: carryover and additional tax | 35% of the federal amount (AB428 lines 64 and 67) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |

**The supplemental tax credit.** Credits are worked out at 8%, but the 8% band only covers the first $60,000 of income (2025). The Act gives back a quarter of the credit value above $4,800: (A - $4,800) x 0.25, where A is the credits under ss.8 to 10, 12 to 13.1, 18, 19 and 20.1 (s.20.2). Donations (s.11) and unused tuition (s.17) are not in A. The AB428 worksheet takes line 58800 less line 58560, times 8%, less $4,800, times 25%. The effect is an extra 2% on credit amounts above $60,000 (2025) or $61,200 (2026). So a large credit claim is worth 10% on the part above that level, as it was before 2025.

**The dividend credit in 2026.** The Act sets the Alberta credit as a fraction of the federal gross-up, 149/890 and 227/770, "for the 2021 and subsequent taxation years" (s.21). The 2025 worksheet turns these into 2.18% and 8.12% of the taxable amount. Current federal Income Tax Act s.82(1)(b), reread on 14 November 2026, still specifies a 15% gross-up for other-than-eligible dividends and 38% for eligible dividends in 2026. This resolves the federal condition. Use taxable grossed-up amounts, not the cash dividend: actual 2025 Worksheet AB428 applies 2.18% to T1 line 12010 and 8.12% to line 12000 minus line 12010. Do not gross up an amount already reported grossed-up. The old provincial fractions remain historical statutory references pending a fresh s.21 read; rounded worksheet percentages are not exact fraction identities. Confirm the actual 2026 provincial worksheet before a final 2026 filing.

**Political contributions in 2026.** The dollar amounts are written into s.24(2.1) of the Act ($200, $1,100, $600, $1,000) and s.24 is not in the list of indexed provisions (s.44.2(1)), so the 2025 limits apply unchanged in 2026.

**Caregiver credits from 2027.** The Fiscal Measures Statutes Amendment Act, 2026 (SA 2026 c3, s.2) replaces the caregiver amount and the amount for infirm dependants 18 or older with one Alberta caregiver credit of $13,180 less the dependant's income over $20,956, which can also be claimed for an infirm spouse. It "comes into force on January 1, 2027", so it does not change 2026 returns; the 2027 amounts are indexed (new s.44.2(1.01)).

## The taxable base

1. **Start from line 26000.** Alberta uses federal taxable income (s.5(1)). Every federal deduction (RRSP, child care, business losses, the capital gains inclusion, the capital gains deduction) flows through. Federal rules live in `ca-fed-t1-return` and `ca-capital-gains`. Self-employed CPP is in `ca-fed-cpp-ei`. AB428 has no deductions of its own at this step.
2. **Part A: tax on taxable income.** Pick the band and apply the AB428 column: (taxable income - band floor) x band rate, plus the fixed amount for the bands below. For 2026 the fixed amounts are $4,896 at $61,200 (8% x $61,200), $14,201.90 at $154,259, $17,904.14 at $185,111, $25,925.40 at $246,813 and $43,202.38 at $370,220. These are worked from the CRA's 2026 bands. The July 2026 CRA payroll table separately prints KP 0, 1,224, 4,309, 6,160, 8,628 and 12,331. Those are rounded payroll deduction constants; they are not interchangeable with the cent-precision cumulative annual amounts above.
3. **Tax on split income.** Add Alberta tax on split income from Form T1206 (2025 AB428 line 60).
4. **Part B: non-refundable credits.** Add up the credit amounts: basic personal amount, age, spouse or eligible dependant, infirm dependants, CPP and EI (lines 30800, 31000, 31200 and 31217 of the return), adoption, pension, caregiver, disability for self and transferred from a dependant, student loan interest, unused tuition carried forward, transfers from a spouse, and medical expenses. Multiply the total by 8%. Then add donations: 60% of the first $200 and 21% of the rest. AB428 has no line for the Canada employment amount. Alberta's tuition line is only for unused amounts carried forward (line 58560, Schedule AB(S11)).
5. **Part C: reduce the tax.** From the Part A tax plus split-income tax, subtract the non-refundable credits, the dividend tax credit and the minimum tax carryover (35% of federal line 40427). The result cannot go below zero. Add Alberta additional tax for minimum tax purposes: actual 2025 AB428 line 67 uses 35% of **T691 Part 7 line 1 minus line 2**, not Part 7 line 14 and not a guessed total federal AMT. Subtract the provincial foreign tax credit (Form T2036), the political contributions credit and the supplemental tax credit, each step not going below zero. The result is ordinary Alberta tax at 2025 AB428 line 75. If TOSI applies, complete T1206 Part 3 and use the greater of its line 50 and the AB428 comparison amount at line 51, through T1206 line 52 to T1 line 42800. Use T1206 Part 4 for multiple jurisdictions; the ordinary comparison cannot replace that route.
6. **Other items.** An unused Alberta stock savings plan credit is claimed on Form T89. The Alberta child and family benefit (Act s.30.2) is a separate payment, not claimed on AB428. Alberta says it "is distributed quarterly with payments in August, November, February and May." The Fiscal Plan gives these yearly maximums (base component, then working component; the working component phases in on family working income, and both phase out on family net income above the threshold):

| Benefit year | 1 child | 2 children | 3 children | 4 or more | Phase-out threshold | Source URL |
|---|---|---|---|---|---|---|
| July 2025 to June 2026 | $1,499 / $767 | $2,248 / $1,465 | $2,997 / $1,883 | $3,746 / $2,021 | $27,565 / $46,191 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (printed page 130) |
| July 2026 to June 2027 | $1,529 / $782 | $2,293 / $1,494 | $3,057 / $1,920 | $3,821 / $2,061 | $28,116 / $47,115 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (printed page 130) |

   Alberta has no provincial sales tax and no payroll tax in 2026: the Fiscal Plan's Major Provincial Tax Rates, 2026 table shows "-" for Alberta on both rows (https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf, printed page 132). GST is federal: see `canada-gst-hst`.


### Credit workpapers and conditions

Use the actual applicable-year AB428 and worksheet. The table of maxima does not establish entitlement. Unless a special provincial rule is identified, test the corresponding federal eligibility and the Alberta amount separately. Federal approval or a federal dollar amount does not itself set the Alberta dollar claim. The following line references are actual **2025** fields; use published 2026 parameters only for clearly labelled estimates.

1. **Basic, age, spouse and eligible dependant.** Resolve residence and any partial-year restrictions first. Age requires 65 or older at year end. The 2025 age base is `max(6221 - 0.15 * max(net_income - 46308, 0), 0)` with zero at $87,782; the 2026 published TD1AB maximum/thresholds are $6,345/$47,234/$89,534. For the ordinary eligible spouse or eligible dependant, reduce the applicable Alberta base by that person's actual net income with a zero floor. Establish the actual federal relationship, support, separate-living, household and support-payment conditions. Do not claim both spouse and eligible-dependant amounts merely because both income tests pass. Coordinate the actual persons and dates rather than assuming single from missing information.
2. **Infirm adult dependant, line 58200.** Establish the adult age, relationship, dependence because of impairment and any Canadian residence condition; a visitor alone does not qualify. The actual 2025 worksheet first takes the lesser of $12,922 and `$21,458 - dependant_net_income`, floored at zero, then subtracts the **same person's line 58160** claim with a further zero floor. Published 2026 TD1AB gives maximum $13,180, phase-out start $8,707 and nil at $21,887. Do not use the caregiver income threshold for this separate program. For a child subject to support payments, check the CRA's part-year separation and no-line-22000 conditions, and choose only the permitted better claim. Coordinate multiple supporters so their combined claim does not exceed the one-person maximum.
3. **Caregiver, line 58400, through 2026.** Establish a dwelling maintained alone or jointly where the claimant and adult dependant ordinarily lived, the qualifying relationship and any Canadian residence condition. The dependant must have been 18 or older while living there. An impaired qualifying relative can qualify; a parent or grandparent aged 65 or older can qualify without impairment under these existing rules. A person only visiting does not qualify. Actual 2025 worksheet base is `max(min(33467 - dependant_net_income, 12922) - same_person_58160, 0)`. Published 2026 TD1AB gives the corresponding $34,136/$13,180/$20,956 parameters. These are credit bases, multiplied by 8%, not refundable payments.
4. **Overlap and other claimants.** The actual worksheet subtracts the same person's eligible-dependant claim from both the infirm and caregiver calculations. If anyone claims the caregiver amount for that dependant, no one can also claim the infirm-dependant amount for the same person. If another person claims that dependant on line 58160, the caregiver claim is excluded. Coordinate actual permitted shares and support-payment restrictions; do not give each supporter the full maximum. Do not import BC's spouse-caregiver overlap rule into Alberta's current worksheet. The future 2027 spouse-inclusive consolidated credit does not apply to a 2026 return.
5. **Adoption and pension.** Actual 2025 adoption line 58330 follows federal qualifying expenses/period and caps the combined claim at $19,354 per child ($19,741 published for 2026), shared between adoptive parents without duplication. Actual pension line 58360 is the lesser of the eligible federal line 31400 amount and $1,719 ($1,753 in 2026). Both are Alberta-resident-only under the actual CRA instructions; an Alberta-source non-resident cannot claim them merely because an AB computation is needed. Do not treat all pension receipts as eligible pension income.
6. **CPP, QPP and EI.** Use the eligible base-contribution/premium amounts actually carried by T1 lines 30800, 31000, 31200 and 31217. Additional/enhanced CPP deductions already used in federal taxable income do not become another 8% base credit. Use `ca-fed-cpp-ei` for the contribution calculation, employee/self-employed mix, limits and overpayments. The fictional contributions in the original examples below are stipulated actual credit inputs, not legal annual maxima. Alberta Budget's comparison table prints a stale 2025 CPP number; it is not used here as contribution authority.
7. **Disability, line 58440.** Establish the actual federal DTC entitlement and approved period, using T2201/CRA determination where required. In 2025 the adult base is $17,219. For an eligible person under 18 at year end, add `max(12922 - max(relevant_care_expenses - 3524, 0), 0)`, capped with the base at $30,141. Relevant care is care claimed for that person by **any person**, not only by the claimant. Published 2026 base/supplement are $17,563/$13,180; the $3,594 care threshold is a provisional 2% derivation, not a read final 2026 annual field.
8. **Disability transferred from a dependant, line 58480.** Check actual federal transfer entitlement and the dependant's own return before computing unused entitlement. Actual 2025 Worksheet AB428 first computes the dependant's DTC base plus any eligible care-adjusted supplement, adds their AB428 line 36, subtracts their taxable income, floors at zero, and takes the lesser of that result and their disability amount. Keep each dependant separate and coordinate shares. A maximum is not automatically unused. Differing end-year provinces require the special CRA rules; do not copy Alberta's result into another province's transfer.
9. **Student-loan interest and unused tuition.** Establish qualifying student-loan interest and no double use. Alberta's tuition line 58560 is carryforward-only, using actual AB(S11), not a new credit for current fees. For 2025 obtain the unused Alberta amount from the 2024 assessment/reassessment. If prior 31 December residence was outside Alberta, the actual 2025 schedule says that unused amount cannot be claimed in 2025 or a future year. The student completes it. Its own-use base is taxable income if no more than $60,000; above that it is actual AB428 Part A tax divided by 8%. Subtract line 39, floor at zero and claim the lesser of the result and the available carryforward. Closing balance is opening less used. Do not import another province's tuition balance, create current-year Alberta fees, invent a new transfer or omit the student's own-use requirement. Obtain actual 2026 AB(S11) before finalizing that year's fields.
10. **Unused spouse amounts, line 58640.** Actual AB(S2) allows unused age, pension and disability amounts only where federal Schedule 2 eligibility is met. Establish the spouse's actual or hypothetical AB428 if they are not filing, with supporting slips and province facts. Above the $60,000 2025 boundary, its own-use measure is Part A tax divided by 8%, not raw taxable income. Subtract the spouse's basic amount, line 32 and used tuition, floor the adjusted taxable-income result at zero, then subtract it from the transferable age/pension/disability total with a zero floor. Do not transfer the full amounts by default. A spouse outside Alberta needs the special cross-province rules.
11. **Medical baskets.** Match actual federal eligible patients, expenses, periods, reimbursements and unclaimed balances. For self, spouse/common-law partner and minor children, use the same eligible basket as federal line 33099; subtract the lesser of 3% of the claimant's net income and $2,884 in 2025 ($2,942 provisionally derived for 2026), with a zero floor. For each other dependant, actual Worksheet AB428 subtracts **that dependant's AB428 line 48** from their eligible medical expenses, floors at zero and sums the separate results on 58729. Do not aggregate their net incomes or import Ontario's per-dependant cap. The ordinary federal period is an eligible 12 months ending in the tax year with no prior-year reuse. Federal s.118.2 also contains a special 24-month period including an eligible deceased patient's death day; verify the applicable provincial incorporation/special-return entitlement before using that exception, rather than automatically rejecting it or certifying it from the annual summary alone. Do not treat this method as a complete special-expense ceiling engine.
12. **Donations.** Establish eligible federal donation/gift amounts and carryforward limits before using AB428's separate gift lines. The Alberta calculation is 60% on the first $200 and 21% above $200 in the actual 2025 form. It is separate from the ordinary 8% base-credit sum and the supplemental calculation. Do not add the first $200 twice, use all cash payments without receipts/eligibility, or carry a non-refundable excess as a refund. Recheck the unchanged provincial provision and actual 2026 form for final 2026 work.

### Exact ordinary 2025 Part C bridge

Keep every workpaper in cents, observe each printed floor and preserve the source edition. The actual 2025 AB428 page 3 gives this sequence; it is not a verified 2026 field map.

| Actual 2025 field | Calculation and required evidence |
|---|---|
| 59 | Part A progressive Alberta tax on actual federal taxable income |
| 60 / 61510 | Actual T1206 Alberta split-income result, if applicable; not an invented zero |
| 61 | 59 + 60 |
| 62 | Actual 8%-base credits plus the separately calculated donation credit, from 58 |
| 63 / 61520 | Actual Worksheet AB428 dividend credit, using the taxable dividend categories |
| 64 / 61540 | Actual federal 40427 minimum-tax carryover x 35%; keep separate from current AMT |
| 65 | Sum 62 through 64 |
| 66 | max(61 - 65, 0) |
| 67 | (T691 Part 7 line 1 - line 2) x 35%, using the completed actual federal form |
| 68 | 66 + 67 |
| 69 | Capped provincial foreign credit from actual T2036, including its AMT/country rules |
| 70 | max(68 - 69, 0) |
| 71 / 60030 | Eligible Alberta political contributions with dates/recipient/receipts |
| 72 | Actual political worksheet credit, maximum $1,000 |
| 73 | max(70 - 72, 0) |
| 74 / 61545 | Supplemental credit: `0.25 * max(0.08 * (58800 - 58560) - 4800, 0)` |
| 75 | max(73 - 74, 0); ordinary Alberta tax before any final T1206 comparison |

Actual 2025 T1206 Chart C supplies Alberta's 15% high rate, 8% low rate and 8.12%/2.18% dividend parameters; its Alberta input/comparison fields are AB428 60/69/75. Complete the federal split-income classification, adjusted-income, permitted-credit and foreign-credit work first. In ordinary Part 3, T1206 line 50 is compared with AB428 line 75 carried to line 51; the greater goes through 52 to T1 42800. Do not add the same TOSI twice or discard that final comparison because AB428 60 was already entered. TOSI-adjusted net/taxable income can also change spouse/dependant transfers, tuition own use and the ACFB. This method does not determine federal excluded-business/share/reasonable-return eligibility from the Alberta rate alone.

**Minimum tax.** Require the completed applicable-year federal T691 and actual 40427 carryover. The form's 35% current-amount input differs from the Part 7 line 14 additional-tax input used by BC's 2025 form. Do not substitute BC's field, divide provincial 8% by a federal rate, or set AMT to zero because ordinary tax is low. Specialized TOSI/foreign/AMT intersections and the final 2026 provincial fields remain open until their actual workpapers and authority are available.

**Political contribution workpaper.** The actual 2025 worksheet accepts registered provincial legislature/senatorial candidates, Alberta political parties, leadership contestants and constituency associations; prospective candidate associations qualify only for contributions on or after 4 July 2025. Verify registration, actual payment year and official receipt under the Election Finances and Contributions Disclosure Act. For eligible C no more than $200 use 0.75C; above $200 through $1,100 use $150 + 0.50(C - $200); above $1,100 through $2,300 use $600 + 0.3333(C - $1,100); if more than $2,300 enter $1,000. Exactly $2,300 produces $999.96 at the printed 33.33% rate. Preserve that actual form convention; do not invent an exact statutory one-third rate without reading the provision. CRA requires the claim on the return or within 90 days of the assessment/reassessment notice; paper returns attach the official receipt. An eligible calculated credit cannot reduce the ordinary tax below zero. Confirm the actual-year unchanged provision and filing instructions before finalizing 2026.

**Stock savings carryforward, T89.** Preserve the unused Alberta stock savings plan tax credit from the prior T89. Actual 2025 T89 takes the lesser of that balance and actual T1 line 42800, sends it to refundable-credit line 47900, and carries forward opening less used. It is a separate return item, not an extra AB428 Part B base or reduction of AB428 75. Establish Alberta residence and the actual prior balance; do not create a new investment entitlement. Attach T89 to a paper return.

### ACFB eligibility and income workpaper

The complete two-benefit-year maximum table above remains applicable to its stated periods. It is not a per-child payment table: the two-, three- and four-child entries are **family totals**, and each entry shows base / working components. The Alberta and CRA current program pages confirm the 2026–27 totals and thresholds. Do not confuse a July-to-June benefit period with the calendar income year used in the assessment.

- Establish an Alberta-resident parent with one or more children under 18, actual family/adjusted family net income, family working income, child count/ages and applicable CCB eligibility/household information. File the actual returns; CRA's Alberta information tells both spouses/partners to file by the ordinary April deadline for timely benefit processing. A zero-tax return can still matter.
- No separate ACFB application is ordinarily needed when the annual return is filed and the family qualifies for the federal CCB. Use RC66/actual CCB registration where required; this is not permission to submit a form from this method.
- The base component can be available without employment income. The working component grows at 15% of family employment income above $2,760 until the relevant family maximum. Both components then have their own family-income phase-out thresholds. Do not describe the working threshold as the net-income phase-out threshold, or calculate a final entitlement with an invented phase-out rate.
- Keep household status, shared custody, partner changes and residence changes current. The Alberta program says a family moving in becomes eligible in the month after becoming resident, while moving out can require repayment for ineligible months. Obtain actual base-year income/CRA assessment and custody/change-date rules before issuing a monthly final entitlement. TOSI-adjusted family income may be required.
- Payments are non-taxable, separate from the CCB and normally issued in August, November, February and May. Quarterly entitlements below $10 can be consolidated into less frequent payments. Do not post the annual maximum as an AB428 credit or guarantee receipt from an income-only calculation.
- The full statutory phase-out rates, income exclusions, base-year/change reassessments and special custody cases are not certified by this maximum table. Use the actual official calculator/assessment and operative rules before a final benefit calculation. No new rate is guessed here.

**Ended programs.** The CRA's actual 2025 Alberta information says all entitlements under the former Alberta climate leadership adjustment rebate and Alberta family employment tax credit were eliminated after 31 December 2025. The original climate-rebate question therefore must not generate a 2026 claim from a historical transitional reference. Federal Canada Carbon Rebate eligibility/history is a separate federal question not determined here.

**No general Alberta payroll tax or PST.** Budget's 2026 Alberta comparison confirms those two entries, while federal GST, payroll withholding, CPP/EI and other actual employer obligations still need their own methods. Do not turn the absence of these two provincial taxes into a blanket absence of payroll or employment compliance.

## Deadlines and filing

AB428 is filed with the federal T1 return. There is no separate Alberta return and no separate Alberta deadline. The CRA dates for the 2025 return:

- **30 April 2026**: deadline to file and to pay.
- **15 June 2026**: deadline to file if you or your spouse or common-law partner are self-employed. Payment is still due 30 April 2026.

For the 2026 return, CRA's current tax-deadline fact sheet now publishes **30 April 2027** for ordinary filing/payment and **15 June 2027** for qualifying self-employed individuals or their spouse/common-law partner. Payment remains due 30 April. Those dates are published, not merely extrapolated. A tax-shelter business investment, death of the taxpayer or spouse, optional return or another special return needs the actual Income Tax Act s.150 rule and CRA instructions; the ordinary dates do not settle those branches. Instalments are federal rules covering federal and Alberta tax together: see `ca-fed-instalments`.

## Penalties and interest

Alberta tax is assessed and collected with federal tax, so the federal penalties apply to the combined balance (CRA, 2025 return):

- **Late filing:** 5% of the balance owing, plus 1% for each full month late, up to 12 months.
- **Repeated late filing:** for the 2025 return, a qualifying penalty in 2022, 2023 or 2024 **and** a demand to file can trigger 10% of the unpaid balance plus 2% for each full month late, up to 20 months. For the 2026 return, the corresponding three-year window is 2023 to 2025. Check both statutory conditions in federal s.162(2); a late filing alone does not automatically trigger the repeat rate.
- **Interest:** "the CRA charges compound daily interest starting the day after the due date." The rate can change every three months, so take it from the CRA's prescribed interest rate page.

## Cross-border points

- **Moving between provinces:** only the province of residence on 31 December taxes the year, apart from the business income split in s.6.1(3) and (4). Ask where the client lived on 31 December, not where the money was earned.
- **Foreign income of an Alberta resident:** taxed as part of taxable income. Foreign tax not used against federal tax can be claimed against Alberta tax as the provincial foreign tax credit on Form T2036 (s.23, 2025 AB428 line 69).
- **Historical overseas employment tax credit:** the original Alberta s.22 reference cannot establish a current credit. Federal s.122.3(1.01)(b) makes the specified amount nil, and s.122.3(1.02)(b) makes the percentage 0%, for 2016 and subsequent years. Do not claim an overseas-employment credit in 2025 or 2026 from this legacy reference. Section 122.3 still appears in the Act; do not falsely describe the section itself as repealed. Preserve the foreign-employment inquiry and consider actual foreign tax, treaty, deductions and residence in their own workpapers.
- **Leaving Canada:** Alberta tax still applies for the part of the year before departure (s.3(1), s.6.1(5)), with credits prorated for emigrants (s.40). The departure return and the T1244 deferral are in `ca-ab-departure-tax-t1244-security-election-defer`.
- **Arriving in Canada:** credits are restricted for part-year residents (s.36.1). Use `ca-tax-residency` for the arrival date.


### Foreign-credit workpaper: actual 2025 T2036

Complete federal T2209 first. If it absorbs all eligible foreign non-business tax, the provincial amount is zero. Otherwise preserve the actual country, Canadian-dollar conversion, eligible foreign non-business tax, federal credit used, net foreign income and net income. If total foreign non-business taxes paid to all countries exceed $200, complete a separate T2036 for each country; do not net unrelated countries into one uncapped credit.

Actual ordinary Alberta provincial tax otherwise payable is **AB428 line 63 plus line 68** under T2036 note (4), not line 68 alone and not BC's AMT exclusion. For multiple jurisdictions, the Alberta note uses **AB428MJ line 20 plus line 36**, and only the province of end-year residence obtains that provincial foreign-credit claim. T2036's allowed amount is the lesser of remaining eligible foreign non-business tax and the net-foreign-income / applicable-net-income share of provincial otherwise-payable tax, with its overall otherwise-payable ceiling. Apply its exact denominator and Part 1 allocation note rather than gross foreign receipts or total family income. Missing actual income or foreign tax is unresolved, not a full credit.

If minimum tax applies, Alberta follows T2036 note (1)'s other-province branch: line 2 uses the part of T691 Part 4 line 11 special foreign credit relating to the foreign non-business tax. Do not substitute the ordinary federal foreign credit or copy Ontario's apportionment formula. Partial-year Canadian residence also has a specific income denominator rule in note (3). Keep treaty/source/foreign-business-tax deductions in the federal workpaper; no blanket deduction of all overseas taxes is established here.

### Multiple jurisdictions: actual 2025 AB428MJ

1. Establish actual residence, business permanent establishments, income sources and T2203 Part 1 allocations. Part 2/Part 3 determine eligible and resident-only non-refundable-credit amounts. Ordinary interprovincial wages alone do not justify a business-allocation percentage.
2. AB428MJ 16 is tax on the relevant full taxable base; add actual unallocated TOSI at 17. Use actual Part 3 AB credit total at 19; Alberta residents alone have the dividend entry at 20 and the minimum-tax carryover at 21. That carryover uses federal 40427 x 35%. Subtract the actual sum at 22 from 18 with the floor at 23.
3. Add current AMT from `(T691 Part 7 line 1 - line 2) x 35%` at 24. Only then multiply 25 by the Part 1 Alberta allocation percentage at 26 to reach 27.
4. For an Alberta resident, complete the separate adjustment at 29–35: actual adoption plus pension bases x 8%, plus the dividend credit, multiplied by the percentage not allocated to Alberta. Subtract from 28 with a zero floor at 36. Do not perform this Alberta-resident adjustment for another province's resident.
5. Complete the residence-province foreign credit at 37 and the floor at 38. Non-Alberta residents follow the form's direct 27-to-38 instruction. Use actual political credit at 40, floor at 41, supplemental worksheet at 42 and floor at 43. Transfer actual 43 to T2203 Part 5 line 8, keeping the remaining provincial summary and T1206 Part 4 work separate.
6. The actual MJ supplemental worksheet is distinct: it adds its eighteen eligible base lines excluding unused tuition/donations, applies the Alberta allocation percentage, adds the resident-only adjustment for adoption/pension on the non-Alberta share, then applies 8%, the $4,800 base and 25% excess calculation. A nonresident has zero at its resident-adjustment line 28. Do not multiply an already completed ordinary supplemental credit by a guessed proportion.

These edition-specific steps preserve the original allocation purposes while correcting the final-tax shortcut. They are not a complete calculation without actual allocation/credit facts, applicable-year forms and any special-return restrictions.

### Arrival, departure and special returns

Retain actual Canadian arrival/departure dates, residence ties, the relevant provincial date and the federal taxable-Canada/world-income work. Actual CRA Alberta instructions require corresponding reduced federal personal claims to reduce provincial 58040, 58080, 58120, 58160, 58200, 58400, 58440, 58480 and 58640 in the same way. Do not prorate every expense credit, every dollar of income or every full-year provincial tax by days as a universal shortcut. The original ss.36.1 and 40 references preserve the legal inquiry, but their exact current restricted-credit provisions remain unconfirmed in this fresh audit. A final immigrant, emigrant, nonresident, death or optional return needs its actual federal/provincial workpapers. Use `ca-tax-residency`, `ca-fed-t1-return` and the named departure/T1244 method for those jobs; holding a specific branch unresolved does not erase the valid ordinary 2025 computation above.

## Worked examples

**Example 1. Employee, single, 2026.** Priya lives in Calgary all year. Her taxable income (line 26000) is $75,000. Her return shows CPP of $3,400 on line 30800 and EI of $1,000 on line 31200. She claims no other credits. Part A: $75,000 is in the second band, so ($75,000 - $61,200) x 10% = $1,380, plus $4,896 for the first band, gives $6,276.00. Part B: $22,769 + $3,400 + $1,000 = $27,169, times 8% = $2,173.52. The supplemental credit is nil, because $2,173.52 is below the $4,896 base. Alberta tax on line 42800 is $6,276.00 - $2,173.52 = $4,102.48.

```oa-check
name: Alberta 2026, employee, taxable income 75,000
inputs:
  taxable_income: 75000
  cpp_30800: 3400
  ei_31200: 1000
  bpa: 22769
steps:
  - part_a_tax: (taxable_income - 61200) * 0.10 + 4896
  - credit_amounts: bpa + cpp_30800 + ei_31200
  - credits: round(credit_amounts * 0.08, 2)
  - supplemental: max((credits - 4896) * 0.25, 0)
  - alberta_tax: max(max(part_a_tax - credits, 0) - supplemental, 0)
expected:
  part_a_tax: 6276.00
  credit_amounts: 27169
  credits: 2173.52
  supplemental: 0
  alberta_tax: 4102.48
```

**Example 2. One earner with a spouse and a disability, 2025 (the supplemental credit applies).** Marc lived in Edmonton on 31 December 2025. His taxable income is $120,000. His spouse's net income (line 23600) is $3,000. Marc has an approved disability tax credit certificate. His return shows CPP of $3,100 on line 30800 and EI of $1,000 on line 31200. Part A: ($120,000 - $60,000) x 10% + $4,800 = $10,800.00. Part B: basic personal amount $22,323, spouse amount $22,323 - $3,000 = $19,323, CPP $3,100, EI $1,000, disability $17,219. The total on line 58800 is $62,965, times 8% = $5,037.20. Supplemental credit: ($5,037.20 - $4,800) x 25% = $59.30. That is 2% of the $2,965 by which his credit amounts exceed $60,000. Alberta tax: $10,800.00 - $5,037.20 - $59.30 = $5,703.50.

```oa-check
name: Alberta 2025, one earner, spouse amount, disability, supplemental credit
inputs:
  taxable_income: 120000
  spouse_net_income: 3000
  cpp_30800: 3100
  ei_31200: 1000
  bpa: 22323
  disability: 17219
steps:
  - part_a_tax: (taxable_income - 60000) * 0.10 + 4800
  - spouse_amount: max(bpa - spouse_net_income, 0)
  - line_58800: bpa + spouse_amount + cpp_30800 + ei_31200 + disability
  - credits: round(line_58800 * 0.08, 2)
  - supplemental: max((credits - 4800) * 0.25, 0)
  - check_two_percent: (line_58800 - 60000) * 0.02
  - alberta_tax: max(max(part_a_tax - credits, 0) - supplemental, 0)
expected:
  part_a_tax: 10800.00
  spouse_amount: 19323
  line_58800: 62965
  credits: 5037.20
  supplemental: 59.30
  check_two_percent: 59.30
  alberta_tax: 5703.50
```


**Example 3. Separate 2026 credit components, conditional estimates.** These are fictional, independent component workpapers, not a completed person's tax return. In the caregiver component, an Alberta parent and their impaired adult child ordinarily share a maintained dwelling, the federal eligible-dependant conditions are met, the child's net income is $15,000, there are no support-payment/other-claimant restrictions, and the same parent claims line 58160. The eligible-dependant base is $7,769; the caregiver maximum before overlap is $13,180, leaving only $5,411 on the caregiver workpaper and $432.88 of caregiver credit. The infirm-dependant credit cannot be stacked with that caregiver claim. This is not BC's spouse-overlap calculation. In a separate adult-medical component, eligible unreimbursed expenses of $20,000 for a dependant with $30,000 net income leave $19,100 after that dependant's own $900 threshold. A separate eligible under-18 disability component with relevant care claimed by any person of $20,000 eliminates the supplement. The medical and care thresholds below remain the stated provisional 2026 indexed estimates pending actual-year forms and the fresh statutory check.

```oa-check
name: Alberta 2026 conditional caregiver overlap, separate medical and care components
inputs:
  dependant_income: 15000
  eligible_dependant_base: 22769
  caregiver_maximum: 13180
  caregiver_income_base: 34136
  other_medical_expenses: 20000
  other_dependant_income: 30000
  medical_threshold: 2942
  disability_base: 17563
  child_supplement_maximum: 13180
  care_claimed_by_anyone: 20000
  care_threshold: 3594
steps:
  - eligible_dependant: max(eligible_dependant_base - dependant_income, 0)
  - caregiver_before_overlap: max(min(caregiver_income_base - dependant_income, caregiver_maximum), 0)
  - caregiver_after_overlap: max(caregiver_before_overlap - eligible_dependant, 0)
  - caregiver_credit: round(caregiver_after_overlap * 0.08, 2)
  - other_medical_threshold: min(medical_threshold, other_dependant_income * 0.03)
  - other_medical_base: max(other_medical_expenses - other_medical_threshold, 0)
  - other_medical_credit: round(other_medical_base * 0.08, 2)
  - care_excess: max(care_claimed_by_anyone - care_threshold, 0)
  - child_supplement: max(child_supplement_maximum - care_excess, 0)
  - disability_amount: disability_base + child_supplement
expected:
  eligible_dependant: 7769
  caregiver_before_overlap: 13180
  caregiver_after_overlap: 5411
  caregiver_credit: 432.88
  other_medical_threshold: 900
  other_medical_base: 19100
  other_medical_credit: 1528
  care_excess: 16406
  child_supplement: 0
  disability_amount: 17563
```

**Example 4. Fictional 2025 ordinary form bridge with supplied AMT/foreign workpapers.** Taxable income is $100,000, net income $100,000, eligible line 58800 bases total $25,000, there are no gifts/tuition/TOSI, and a completed federal return gives a $200 minimum-tax carryover. A completed T691 supplies Part 7 line 1 of $2,500 and line 2 of $500. It is specifically **their $2,000 difference**, not Part 7 line 14, that feeds the provincial additional tax. Cash dividends are $1,000 eligible and $1,000 other-than-eligible, giving taxable amounts $1,380/$1,150 and an Alberta worksheet dividend credit of $137.13 after cents rounding. Actual eligible foreign tax is $2,000, the supplied applicable T2036 AMT line-2 special-foreign-credit amount is $1,500, and its completed income workpaper supplies net foreign non-business income of $10,000 and the $100,000 denominator. Its Alberta otherwise-payable input includes line 63 plus line 68. An eligible registered political contribution of $1,000 has the required receipt/date and gives $550. These supplied federal classifications and foreign inputs are assumptions, not independently derived federal entitlements. The ordinary result is $6,242.87, with no final TOSI comparison needed on these facts.

```oa-check
name: Alberta actual 2025 ordinary AMT foreign dividend political bridge
inputs:
  taxable_income: 100000
  credit_bases: 25000
  eligible_cash_dividend: 1000
  other_cash_dividend: 1000
  federal_carryover: 200
  t691_part7_line1: 2500
  t691_part7_line2: 500
  eligible_foreign_tax: 2000
  applicable_t2036_line2: 1500
  net_foreign_income: 10000
  t2036_net_income: 100000
  political_contribution: 1000
steps:
  - part_a_tax: (taxable_income - 60000) * 0.10 + 4800
  - ordinary_credits: round(credit_bases * 0.08, 2)
  - eligible_taxable_dividend: eligible_cash_dividend * 1.38
  - other_taxable_dividend: other_cash_dividend * 1.15
  - dividend_credit: round(eligible_taxable_dividend * 0.0812 + other_taxable_dividend * 0.0218, 2)
  - provincial_carryover: federal_carryover * 0.35
  - line66: max(part_a_tax - ordinary_credits - dividend_credit - provincial_carryover, 0)
  - additional_amt: (t691_part7_line1 - t691_part7_line2) * 0.35
  - line68: line66 + additional_amt
  - foreign_otherwise_payable: dividend_credit + line68
  - foreign_remaining: max(eligible_foreign_tax - applicable_t2036_line2, 0)
  - foreign_ratio_limit: round(net_foreign_income / t2036_net_income * foreign_otherwise_payable, 2)
  - provincial_foreign_credit: min(foreign_remaining, foreign_ratio_limit, foreign_otherwise_payable)
  - line70: max(line68 - provincial_foreign_credit, 0)
  - political_credit: 150 + (political_contribution - 200) * 0.50
  - supplemental: max(ordinary_credits - 4800, 0) * 0.25
  - alberta_tax: max(max(line70 - political_credit, 0) - supplemental, 0)
expected:
  part_a_tax: 8800
  ordinary_credits: 2000
  eligible_taxable_dividend: 1380
  other_taxable_dividend: 1150
  dividend_credit: 137.13
  provincial_carryover: 70
  line66: 6592.87
  additional_amt: 700
  line68: 7292.87
  foreign_otherwise_payable: 7430
  foreign_remaining: 500
  foreign_ratio_limit: 743
  provincial_foreign_credit: 500
  line70: 6792.87
  political_credit: 550
  supplemental: 0
  alberta_tax: 6242.87
```

**Example 5. Independent 2025 boundary components, not one client's return.** A $2,300 eligible political contribution gives $999.96 under the actual printed decimal rate. A separate supplemental workpaper with line 58800 of $80,000 including $20,000 unused tuition has no supplemental credit after excluding tuition. A supplied ordinary AB428 amount of $1,200 and completed T1206 line 50 of $1,700 produce final 42800 of $1,700, not $1,200. A separate T89 balance of $5,000 then permits at most $1,700 on 47900, leaving $3,300. A separate eligible AB(S11) student's $100,000 taxable income, actual Part A tax of $8,800, line 39 of $25,000 and actual available carryforward of $20,000 use the tax/8% own-use measure of $110,000, use $20,000 tuition and leave zero. These calculations do not establish relationship, custody, support, carryforward, contribution or federal TOSI eligibility.

```oa-check
name: Alberta actual 2025 political boundary tuition exclusion and supplied final comparisons
inputs:
  contribution_at_boundary: 2300
  supplemental_line58800: 80000
  supplemental_unused_tuition: 20000
  ordinary_ab428: 1200
  supplied_t1206_line50: 1700
  stock_opening_balance: 5000
  tuition_part_a_tax: 8800
  tuition_prior_credits: 25000
  tuition_opening_balance: 20000
steps:
  - political_printed_credit: round(600 + (contribution_at_boundary - 1100) * 0.3333, 2)
  - supplemental_eligible_bases: supplemental_line58800 - supplemental_unused_tuition
  - supplemental_credit: max(supplemental_eligible_bases * 0.08 - 4800, 0) * 0.25
  - final_42800: max(ordinary_ab428, supplied_t1206_line50)
  - stock_credit_47900: min(stock_opening_balance, final_42800)
  - stock_closing_balance: stock_opening_balance - stock_credit_47900
  - tuition_equivalent_income: tuition_part_a_tax / 0.08
  - tuition_own_use_requirement: max(tuition_equivalent_income - tuition_prior_credits, 0)
  - tuition_used: min(tuition_opening_balance, tuition_own_use_requirement)
  - tuition_closing_balance: tuition_opening_balance - tuition_used
expected:
  political_printed_credit: 999.96
  supplemental_eligible_bases: 60000
  supplemental_credit: 0
  final_42800: 1700
  stock_credit_47900: 1700
  stock_closing_balance: 3300
  tuition_equivalent_income: 110000
  tuition_own_use_requirement: 85000
  tuition_used: 20000
  tuition_closing_balance: 0
```

## Ask the client first

1. Where did you live on 31 December of the year? If you moved during the year, when and from where? If unknown, do not work out provincial tax.
2. Did you have business income earned outside Alberta (or, if you live in another province, inside Alberta)?
3. Your taxable income (line 26000), net income (line 23600), actual marital/common-law status and relevant change dates, plus each spouse/dependant income and support record. If status or a required income is unknown, leave the affected credit, transfer and family benefit unresolved. Do not assume single. A no-spouse-credit conditional illustration must be labelled as such and must not become the final return.
4. Your age on 31 December, any pension income, and whether a T2201 disability certificate is approved for you or a dependant.
5. Medical expenses, donations, Alberta political contributions, and any unused Alberta tuition carried forward (Schedule AB(S11)).
6. Did you leave or enter Canada in the year, and did you pay foreign tax? Obtain actual dates, Canadian and foreign income, federal T2209/T691 outputs, source-country tax/receipts and any T2203 permanent-establishment allocations.
7. Does federal TOSI apply? Obtain completed T1206 classification, adjusted incomes, provincial inputs and the final comparison, rather than assuming an Alberta progressive calculation is final.
8. Who else claims the same dependant, caregiver, support, medical, adoption or disability amount? Obtain permitted shares, relationship/household evidence and actual care expenses claimed by anyone. Obtain spouse/dependant returns or the actual equivalent inputs before unused transfers.
9. For ACFB, obtain actual family/adjusted incomes and base year, child/custody/status/residence change dates and the CRA benefit assessment. For T89/tuition, obtain the actual prior assessment/form balance and prior province. Do not infer a carryforward from an old maximum.

## Sources

| Source | URL | Read on |
|---|---|---|
| Alberta Personal Income Tax Act, RSA 2000 c A-30, consolidation current as of 11 December 2025 (Alberta King's Printer): ss.3, 4, 5, 6.1, 11, 12, 13.1, 20.2, 21, 22, 23, 24, 27, 30.2, 36.1, 40, 44.2 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf | 2026-11-08 |
| CRA, 2025 Form AB428 Alberta Tax and Credits (5009-C), e-text, Parts A, B and C read for bands, credit lines and the 8% rate | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt | 2026-11-14 |
| CRA, 2025 Worksheet AB428 (5009-D), e-text, read for age, caregiver, infirm dependant, disability, dividend, political contribution and supplemental credit lines | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt | 2026-11-14 |
| CRA, Current year tax rates and income brackets (2026), read for the Alberta rate table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-14 |
| CRA, Last year tax rates and income brackets (2025), read for the Alberta rate table and footnote 2 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html | 2026-11-14 |
| CRA, TD1AB 2026 Alberta Personal Tax Credits Return, lines 1 to 8 read for 2026 credit amounts | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf | 2026-11-14 |
| CRA, T4127 Payroll Deductions Formulas, 123rd edition, effective 1 July 2026, read for Tables 8.1 and 8.2 (Alberta) | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html | 2026-11-14 |
| Government of Alberta, Personal income tax, read for the overview, Table 1 and the child and family benefit | https://www.alberta.ca/personal-income-tax | 2026-11-14 |
| CRA, Due dates and payment dates (individuals), read for the 2025 filing and payment dates | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-14 |
| CRA, Interest and penalties on late taxes, read for the late-filing penalty and interest | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | 2026-11-14 |
| Government of Alberta, Budget 2026 Fiscal Plan 2026-29, Tax Plan, read for the Non-Refundable Tax Credits and Alberta Child and Family Benefit tables (printed page 130), the Major Provincial Tax Rates, 2026 table (page 132) and the new Alberta caregiver credit (page 123) | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf | 2026-11-08 |
| Fiscal Measures Statutes Amendment Act, 2026, SA 2026 c3, s.2 (not in force provisions, current as of 30 June 2026) | https://kings-printer.alberta.ca/documents/Acts/2026ch03_unpr.pdf | 2026-11-08 |
| CRA, actual 2025 AB428 standard PDF, all three pages; page 3 visually checked for exact AMT/order/TOSI bridge | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf | 2026-11-14 |
| CRA, actual 2025 Worksheet AB428 PDF, all three pages; page 3 visually checked for dividend/political/supplemental fields | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.pdf | 2026-11-14 |
| CRA, 2025 Alberta information, all operative credit/scope/foreign/political/benefit/ended-program paragraphs | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/alberta/5009-pc.html | 2026-11-14 |
| CRA, 2026 TD1AB, both pages; published credit parameters/conditions, a payroll form rather than final annual AB428 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf | 2026-11-14 |
| CRA, actual 2025 AB(S2), complete one-page spouse own-use/transfer workpaper | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-s2/5009-s2-25e.pdf | 2026-11-14 |
| CRA, actual 2025 AB(S11), complete one-page prior-province/own-use/carryforward workpaper | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-s11/5009-s11-25e.pdf | 2026-11-14 |
| CRA, actual 2025 T89, complete one-page separate 47900 credit/carryforward | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t89/t89-25e.pdf | 2026-11-14 |
| CRA, actual 2025 T1206, Alberta Chart C, adjusted-income notes, Part 3 final comparison and Part 4 route; page 10 visually checked | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1206/t1206-25e.pdf | 2026-11-14 |
| CRA, actual 2025 T2036, both pages, especially Alberta notes (1), (3) and (4) | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2036/t2036-25e.pdf | 2026-11-14 |
| CRA, actual 2025 T691, Part 7; not a complete federal AMT audit | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t691/t691-25e.pdf | 2026-11-14 |
| CRA, actual 2025 T2203, Alberta AB428MJ and Alberta worksheet, relevant Part 1/3/5 routes; not every province's calculation | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2203/t2203-25e.pdf | 2026-11-14 |
| Government of Alberta, current ACFB eligibility, two benefit-year tables, phase-in and household-change body | https://www.alberta.ca/alberta-child-and-family-benefit | 2026-11-14 |
| CRA, current Alberta benefit page, 2026–27 component amounts/thresholds | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-alberta.html | 2026-11-14 |
| Government of Alberta, Budget 2026 Fiscal Plan, actual indexed official read of printed pages 123, 130 and Alberta-only 132 rows; not a successful direct PDF download | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf | 2026-11-14 |
| Government of Alberta, implementation page, Royal Assent and 2027 caregiver start | https://www.alberta.ca/implementing-budget-2026 | 2026-11-14 |
| Legislative Assembly, Bill 17 s.2 and explanatory notes, printed pages 3–8; Bill text, not the final assented Act PDF | https://docs.assembly.ab.ca/LADDAR_files/docs/bills/bill/legislature_31/session_2/20251023_bill-017.pdf | 2026-11-14 |
| Federal Income Tax Act s.82(1), actual gross-up branches | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html | 2026-11-14 |
| Federal Income Tax Act s.122.3(1.01)/(1.02), post-2015 zero/nil branches | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-122.3.html | 2026-11-14 |
| Federal Income Tax Act s.118.2(1), eligible medical periods/no reuse; provincial incorporation remains open | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.2.html | 2026-11-14 |
| Federal Income Tax Act s.150, individual ordinary/self-employed/death deadline branches | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Federal Income Tax Act s.162(1)/(2), ordinary/repeat late-filing conditions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html | 2026-11-14 |
| CRA, current deadline fact-sheet body publishes 2027 dates despite historical URL slug | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html | 2026-11-14 |

Not yet confirmed: the remaining checks below are open except where expressly resolved.

### Remaining checks and resolved historical questions

- **Still open for final 2026 filing:** actual annual AB428/worksheet/S2/S11/T2203 field maps; final printed medical/supplemental/under-18-care amounts and cumulative band constants. The original 2% arithmetic gives $2,942/$4,896/$3,594 and the constants above, but arithmetic alone is not a fresh read of the indexing/rounding clause.
- **Fresh statutory access still open:** the King's Printer consolidated Alberta Act and unproclaimed 2026 amendment PDFs could not be obtained on 14 November. The original 8 November citations are retained with their historical date, not relabelled as independently reread. This affects certification of exact ss.3/6.1 scope, fixed special-credit provisions, s.12 medical incorporation, s.21 fractions, s.23 limits, s.24 non-indexing, ss.36.1/40 restricted credits and s.44.2 rounding. The actual CRA forms/guidance support the practical 2025 steps, and actual government 2026 pages support published parameters. A final full-law certification still needs the operative sections; a successful PDF download of a different source is not that check.
- **Caregiver transition:** the actual Alberta implementation page confirms Royal Assent on 26 March 2026 and a 1 January 2027 start. The actual Assembly Bill 17 s.2 text and its explanatory notes preserve the two current programs and the future consolidated rule; it is identified as Bill text, not falsely described as the assented Act PDF. Obtain the final operative amendment and indexed 2027 parameters before applying 2027.
- **Resolved:** current federal s.82 confirms the 15%/38% gross-ups; current CRA body publishes 30 April/15 June 2027; current federal s.122.3 gives no 2025/2026 overseas-employment credit; actual CRA Alberta instructions end the two former climate/family-employment programs after 2025. These do not resolve an unrelated final provincial form or a federal carbon-rebate question.
- **Not supplied as engines:** ACFB full statutory phase-out/base-year/shared-custody rules; current/future quarterly prescribed interest rates; special medical ceilings or special death/cross-province entitlements; final federal-plus-Alberta marginal/dividend rates. Use the actual named federal/program authority and complete inputs, not invented zeroes or a maximum table.
- **Old unsupported business items:** the original royalty tax credit, small farm tax credit and Alberta SR&ED top-up had no individual AB428 line established. Do not invent personal credits. Preserve the inquiry and check the actual business/program eligibility in `ab-corporate-tax` or the relevant authority. An absent annual form line alone is not proof that every business program is repealed.
- **Approval:** no new accountant approval or `reviewed_by` record is created by this audit, its arithmetic checks or an AI source review. Any live route claiming otherwise needs a separate app correction.
