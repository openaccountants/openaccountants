---
name: ab-individual-return
description: "Alberta provincial personal income tax for an individual resident in Alberta on 31 December, worked through Form AB428 (Alberta Tax and Credits) on the T1 return. Primary tax year 2026, with a dated section carrying the full 2025 figures and explicit holds for unresolved computations. Covers the six brackets (8%, 10%, 12%, 13%, 14%, 15%) including the 8% bracket added from 2025, the Alberta basic personal amount and the main non-refundable credits, the 8% credit rate, the Alberta supplemental tax credit, donations, medical expenses, the dividend tax credit, political contributions, minimum tax and indexing. Trigger on 'Alberta tax', 'AB428', 'Alberta tax brackets', 'Alberta 8% bracket', 'Alberta basic personal amount', 'Alberta supplemental tax credit', 'line 42800 Alberta'. Out of scope: federal tax (ca-fed-t1-return), CPP and EI (ca-fed-cpp-ei), instalments (ca-fed-instalments), self-employed expenses (ca-ab-deductions-for-self-employed-independent-contractor), emigrating (ca-ab-departure-tax-t1244-security-election-defer), companies (ab-corporate-tax)."
version: "1.2"
jurisdiction: CA-AB
tax_year: 2026
last_updated: 2026-11-28
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Alberta personal income tax (Form AB428), tax year 2026, with 2025 figures

> **Built from the law.** Drafted from the Alberta Personal Income Tax Act (RSA 2000 c A-30, consolidation current as of 11 December 2025), the CRA's 2025 Form AB428 and Worksheet AB428, the CRA's 2026 and 2025 tax rate pages, the CRA's 2026 TD1AB, the CRA's July 2026 payroll formulas (T4127), Alberta's Budget 2026 Fiscal Plan and the Fiscal Measures Statutes Amendment Act, 2026, all read on 2026-11-08. Not yet approved by an accountant. Do not file from it without review by a qualified Canadian professional.

Built by Michael Cutajar and the OpenAccountants team.

Tax year: the calendar year. Currency: Canadian dollars. Alberta sets the law. The Canada Revenue Agency (CRA) runs it on the federal T1 return. The result goes on line 42800 of the return (2025 Form AB428, line 75).

Old figures to drop: Alberta no longer has a single flat 10% rate. From the 2025 tax year the first band is taxed at 8%, and credits are worked out at 8% (Act s.4).

See also: `ca-fed-t1-return` (federal tax and the federal credits), `ca-fed-cpp-ei`, `ca-fed-instalments`, `ca-capital-gains`, `ca-tax-residency`, `ca-ab-deductions-for-self-employed-independent-contractor`, `ca-ab-departure-tax-t1244-security-election-defer`, `ab-corporate-tax`.

## Who this applies to

**Residents on 31 December.** An individual who was resident in Alberta on the last day of the calendar year must pay Alberta tax (Act s.3(1)(a)). The tax is worked out on the whole year's taxable income (s.6.1(1)). So the province you live in on 31 December decides the provincial tax for the year, even if you moved in during the year. Use `ca-tax-residency` for the residential ties test.

**Alberta residents with business income outside Alberta.** The pre-credit tax is T x (C - D) / C, where T is the normal Alberta tax, C is income for the year and D is the business income earned outside Alberta (s.6.1(3)).

**Residents of another province with Alberta business income.** An individual resident in another province or territory on 31 December who had business income in Alberta must also pay Alberta tax (s.3(1)(b)). The pre-credit tax is the full Alberta tax multiplied by the Alberta share: T x C / D, where C is the Alberta business income and D is income for the year (s.6.1(4)).

For these business allocations, the listed credits must also be restricted under ss.38-39; do not allocate the tax and then claim full unrestricted credits. Use the statutory income definitions in s.1(1)(j), not an assumed revenue share.

**Part-year residents who leave Canada.** An individual resident in Alberta for part of the year, who did not live in another province after leaving Alberta, and who was resident outside Canada on the last day of the year, is taxed under s.6.1(5). Part-year credit limits are in s.36.1 and the emigrant proration in s.40. Use `ca-ab-departure-tax-t1244-security-election-defer` for departure tax.

**Non-residents of Canada.** Section3(1)(c) must be read with the applicable s.6.1 source/allocation rules and s.41 credit restrictions; Canadian income alone does not establish a particular Alberta liability. This Guide does not compute that case. **NON-USABLE HOLD: Check this point with one of our partner accountants.**

**Not here:** the federal calculation (`ca-fed-t1-return`), companies (`ab-corporate-tax`), and trusts. The separate trust formula and credit restrictions in ss.6.1(1)(b) and36 are not the ordinary individual calculation. **NON-USABLE HOLD: Check this point with one of our partner accountants.**

## Rates, bands and thresholds

Alberta taxable income is the same as federal taxable income (s.5(1)), line 26000 of the return.

**Tax year 2026.** Published bands are corroborated in Alberta's own current tax table. The 2026 TD1AB corroborates the listed credit inputs, but it is a payroll declaration, not a complete annual-return eligibility determination. Alberta says: "In 2026, thresholds and credit amounts will rise by 2%."

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income up to $61,200 | 8% | 2026 | https://www.alberta.ca/personal-income-tax |
| $61,200.01 to $154,259 | 10% | 2026 | https://www.alberta.ca/personal-income-tax |
| $154,259.01 to $185,111 | 12% | 2026 | https://www.alberta.ca/personal-income-tax |
| $185,111.01 to $246,813 | 13% | 2026 | https://www.alberta.ca/personal-income-tax |
| $246,813.01 to $370,220 | 14% | 2026 | https://www.alberta.ca/personal-income-tax |
| Over $370,220 | 15% | 2026 | https://www.alberta.ca/personal-income-tax |
| Rate used for non-refundable credits ("specified percentage") | 8% | 2025 and later | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.4) |
| Alberta indexing factor | 2.0% | 2026 | https://www.alberta.ca/personal-income-tax |
| Basic personal amount | $22,769 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | max(0, $22,769 minus the qualifying spouse's or dependant's income) | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Age amount (65 or older on 31 December) | $6,345, reduced when net income is over $47,234, nil at $89,534 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Pension income amount | Up to $1,753 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Disability amount | $17,563 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Caregiver amount | Up to $13,180; full if the dependant's net income is $20,956 or less, nil at $34,136 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Amount for infirm dependants 18 or older | Up to $13,180; full if the dependant's net income is $8,707 or less, nil at $21,887 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Disability supplement for a person under 18 | Up to $13,180 | 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (derived using ss.13/13.1 and44.2) |
| Adoption expenses | Up to $19,741 | 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (derived using ss.13/13.1 and44.2) |
| Donations: first $200, then the rest | 60%, then 21% on eligible gifts used for the federal claim; pre-2007 gift branch excluded (not indexed) | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.11(1)) |
| Political contributions credit | 75% up to $200; $150 plus 50% of the excess over $200 through $1,100; then $600 plus 33⅓% of the excess over $1,100, capped at $1,000 (fixed in the Act, not indexed) | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.24(2.1)) |
| Minimum tax carryover | 35% of the federal minimum tax carryover | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.27(1)) |

The Act indexes the specified dollar amounts using the Alberta escalator and nearest-dollar rounding (s.44.2). Alberta confirms2% for2026. The following are derived statutory inputs, not a claim to have read a2026 AB428 or its line numbers. Use the actual year's published return when filing:

- medical expense threshold: the lesser of $2,942 (2025: $2,884) and 3% of net income;
- supplemental tax credit base: $4,896 (2025: $4,800);
- child care and attendant care threshold for the under-18 disability supplement: $3,594 (2025: $3,524).

The method is backed up by the TD1AB: its 2026 basic personal amount ($22,769), age amount ($6,345 and $47,234) and pension amount ($1,753) are each the 2025 figure times 1.02, rounded.

**Tax year 2025.** Published thresholds and rates below are corroborated by Alberta's current table and the2025 FormAB428. Amounts originally taken from its worksheet are also checked against the Act; derived endpoints are labelled below.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income up to $60,000 | 8% | 2025 | https://www.alberta.ca/personal-income-tax |
| $60,000.01 to $151,234 | 10% (AB428 adds $4,800 for the first band) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| $151,234.01 to $181,481 | 12% (published base $13,923.40; cumulative-base application on hold below) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| $181,481.01 to $241,974 | 13% (published base $17,553.04; cumulative-base application on hold below) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| $241,974.01 to $362,961 | 14% (published base $25,417.13; cumulative-base application on hold below) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| Over $362,961 | 15% (published base $42,355.31; cumulative-base application on hold below) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| Non-refundable credit rate | 8% (AB428 line 53) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| Basic personal amount | $22,323 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | max(0, $22,323 minus that qualifying person's income) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| Age amount (born in 1960 or earlier) | $6,221, reduced by 15% of net income over $46,308, nil by $87,782 (computed whole-dollar boundary) | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf |
| Pension income amount | Up to $1,719 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| Disability amount for self | $17,219; under 18, a supplement of up to $12,922 less child and attendant care over $3,524, computed total at most $30,141 | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf |
| Caregiver amount | $33,467 minus the dependant's net income, at most $12,922 per dependant | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf |
| Amount for infirm dependants 18 or older | $21,458 minus the dependant's net income, at most $12,922 per dependant | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf |
| Medical expenses | Expenses over the lesser of $2,884 and 3% of net income | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |
| Adoption expenses | Up to $19,354 | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.13.1(2)) |
| Supplemental tax credit | 25% of (credits at 8%, leaving out unused tuition, minus $4,800) | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf |
| Dividend tax credit | Statutory fractions:227/770 of the eligible-dividend gross-up;149/890 of the other-dividend gross-up; use the actual qualifying gross-up | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf |
| Minimum tax: carryover and additional tax | 35% of the federal amount (AB428 lines 64 and 67) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf |

### Credit eligibility and limits

Spouse/dependant formulas have a zero floor; do not manufacture a negative credit. The amounts above are ceilings or formula inputs, not automatic entitlements. Under Act s.8, the spouse claim requires support and the applicable relationship/separation conditions; the eligible-dependant claim requires the qualifying household, support, relationship, residence and age/infirmity conditions. Apply the one-person, no-double-claim and support-payment restrictions. Do not claim both spouse and eligible-dependant amounts for the same taxpayer.

Through2026, caregiver eligibility under s.8(1)(d) requires the shared home and qualifying relative: a parent/grandparent aged65 or older, or an adult relative dependent because of infirmity. The infirm-dependant branch s.8(1)(e) has its own support/relationship/residence conditions and coordination restrictions. Income in these formulas is the Act's defined/modified income; s.8(2)(g) disregards the federal20(1)(ww) deduction, so line23600 is not always an unadjusted substitute.

Pension amounts use eligible pension income under s.10 and its incorporated federal definitions, not ordinary CPP/QPP/OAS/GIS payments. Disability and transfers require the corresponding federal entitlement and statutory restrictions, not a diagnosis alone. Adoption is for eligible net expenses in the year the adoption period ends, subject to the per-child/shared cap. Medical expenses use the qualifying federal expense definitions with Alberta's separate thresholds for the claimant and other dependants. Apply the part-year and business-allocation restrictions where relevant. [Act ss.8-14,36.1,38-40](https://kings-printer.alberta.ca/documents/Acts/A30.pdf).

**The supplemental tax credit.** Credits are worked out at 8%, but the 8% band only covers the first $60,000 of income (2025). The Act gives back a quarter of the credit value above $4,800: (A - $4,800) x 0.25, where A is the total actually deducted under ss.8 to 10, 12 to 13.1, 18, 19 and 20.1 (s.20.2). Donations (s.11) and unused tuition (s.17) are not in A. The AB428 worksheet takes line 58800 less line 58560, times 8%, less $4,800, times 25%. Subject to actual eligibility/deduction and the non-refundable tax limit, the extra0.25×8%=2% applies to the included credit amounts above$60,000 (2025) or$61,200 (2026); it does not refund unused credits.

**The dividend credit in 2026.** The Act sets the Alberta credit as a fraction of the federal gross-up, 149/890 and 227/770, "for the 2021 and subsequent taxation years" (s.21). The historical2025 worksheet displays were2.18% and8.12% of the taxable amount; its current body was not recovered in this check. Keep those displays as non-usable historical references, rather than substituting rounded percentages for the exact statutory fractions. The federal15%/38% gross-ups are proven for2025/2026 in `ca-fed-t1-return`; the exact Alberta statutory fractions apply to the gross-up. The quoted2.18%/8.12% are the historical2025 worksheet rates, not an independently confirmed2026 worksheet instruction. **NON-USABLE HOLD for an unverified year-specific worksheet percentage calculation: Check this point with one of our partner accountants.**

**Political contributions in 2026.** The dollar amounts are written into s.24(2.1) of the Act ($200, $1,100, $600, $1,000) and s.24 is not in the list of indexed provisions (s.44.2(1)), so the 2025 limits apply unchanged in 2026.

**Caregiver credits from 2027.** The Fiscal Measures Statutes Amendment Act, 2026 (SA 2026 c3, s.2) replaces the caregiver amount and the amount for infirm dependants 18 or older with one Alberta caregiver credit of $13,180 less the dependant's income over $20,956, which can also be claimed for an infirm spouse. It "comes into force on January 1, 2027", so it does not change 2026 returns; the 2027 amounts are indexed (new s.44.2(1.01)).

Political contributions must be qualifying contributions by an individual other than a trust to the registered recipients listed in s.24, supported by the prescribed receipts/application. The statutory third-tier rate is exactly33⅓%, not a33.33% computational substitute; the credit is limited to tax payable.

[CRA published GST/HST and PST table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) separately corroborates Alberta's no-PST entry; it does not change the income-tax computation.

## The taxable base

1. **Start from line 26000.** Alberta uses federal taxable income (s.5(1)). Every federal deduction (RRSP, child care, business losses, the capital gains inclusion, the capital gains deduction) flows through. Federal rules live in `ca-fed-t1-return` and `ca-capital-gains`. Self-employed CPP is in `ca-fed-cpp-ei`. AB428 has no deductions of its own at this step.
2. **Part A: tax on taxable income.** Pick the band and apply the AB428 column: (taxable income - band floor) x band rate, plus the fixed amount for the bands below. For 2026 the fixed amounts are $4,896 at $61,200 (8% x $61,200), $14,201.90 at $154,259, $17,904.14 at $185,111, $25,925.40 at $246,813 and $43,202.38 at $370,220. These are arithmetic on the published bands. The historical payroll comparison constants (KP0,1,224,4,309,6,160,8,628,12,331) are retained only as an unverified comparison; they are not annual AB428 instructions. **NON-USABLE HOLD for the third and higher cumulative bases:** the read operative Act s.6.1(1)(a)(ii) refers to the highest amount under subclause(i), while the published2025 AB428 third-band base is$13,923.40. The year/commencement and2% indexing checks do not remove that reference anomaly. Section1(4) directs consistent interpretation with similar federal provisions; ITA117 and AB428 support the incremental method. An authoritative resolution of the printed reference has not been established here. Do not use the higher-band bases above, or their2025 counterparts, as a resolved filing computation here. Check this point with one of our partner accountants. The two examples below use the second band and do not depend on this discrepancy.
3. **Tax on split income.** Add Alberta tax on split income from Form T1206 (2025 AB428 line 60).
4. **Part B: non-refundable credits.** Add up the credit amounts: basic personal amount, age, spouse or eligible dependant, infirm dependants, CPP and EI (lines 30800, 31000, 31200 and 31217 of the return), adoption, pension, caregiver, disability for self and transferred from a dependant, student loan interest, unused tuition carried forward, transfers from a spouse, and medical expenses. Multiply the total by 8%. Then add donations: 60% of the first $200 and 21% of the rest. AB428 has no line for the Canada employment amount. Alberta's tuition line is only for unused amounts carried forward (2025 line58560, ScheduleAB(S11)), subject to s.17's remaining-tax limit and preceding-year Alberta residence condition; an unused other-province amount does not automatically transfer.
5. **Part C: reduce the tax.** From the Part A tax plus split-income tax, subtract the non-refundable credits, the dividend tax credit and the minimum tax carryover (35% of federal line 40427). The result cannot go below zero. Add Alberta additional tax for minimum tax purposes (35% of the federal amount from Form T691). Subtract the provincial foreign tax credit (Form T2036), the political contributions credit and the supplemental tax credit, each step not going below zero. The result is Alberta tax on line 42800.
6. **Other items.** If there is an unused Alberta stock savings plan tax credit,2025 AB428 directs completion of FormT89; its eligibility/carryover is not computed here. The Alberta child and family benefit (Act s.30.2) is a separate payment, not a deduction from AB428 tax. It requires the eligible-individual/qualified-child conditions, the relevant filed base-year return and Alberta residence at the beginning of the month and at the preceding month-end. The Alberta authority requires a parent of an under18 child, Alberta residence, a return and the income criteria; automatic consideration also requires qualification for the federalCCB. Alberta gives the usual payment months as August, November, February and May, with small quarterly entitlements below$10 potentially consolidated. The Fiscal Plan gives these yearly maximums (base component, then working component; the working component phases in at15% of qualifying family working income above$2,760 until its cap, and both components phase out on their separate family-income thresholds; these are maximums, not an actual benefit calculation):

| Benefit year | 1 child | 2 children | 3 children | 4 or more | Phase-out threshold | Source URL |
|---|---|---|---|---|---|---|
| July 2025 to June 2026 | $1,499 / $767 | $2,248 / $1,465 | $2,997 / $1,883 | $3,746 / $2,021 | $27,565 / $46,191 | [Alberta maximums](https://www.alberta.ca/alberta-child-and-family-benefit); [Act30.2 thresholds](https://kings-printer.alberta.ca/documents/Acts/A30.pdf) |
| July 2026 to June 2027 | $1,529 / $782 | $2,293 / $1,494 | $3,057 / $1,920 | $3,821 / $2,061 | $28,116 / $47,115 | https://www.alberta.ca/alberta-child-and-family-benefit |

   Alberta has no provincial sales tax, as corroborated by the CRA GST/HST and PST table. The old Budget2026 provincial payroll-tax assertion was not reconfirmed and is a **NON-USABLE HOLD: Check this point with one of our partner accountants.** The original fiscal-plan comparison source is retained for that research (https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf, printed page 132). GST is federal: see `canada-gst-hst`.

## Deadlines and filing

AB428 is filed with the federal T1 return. There is no separate Alberta return and no separate Alberta deadline. The CRA dates for the 2025 return:

- **30 April 2026**: deadline to file and to pay.
- **15 June 2026**: deadline to file for a qualifying business taxpayer or their cohabiting spouse/common-law partner, subject to the tax-shelter-cost exception. Payment is still due 30 April 2026.

For an ordinary2026 individual return, ITA150(1)(d) gives30April2027, or15June2027 for the qualifying business/spouse branch; the extension does not apply to a business whose expenditures were primarily tax-shelter-investment costs. The ordinary balance-due date is30April2027 under ITA248(1), even with the June filing extension. Death, bankruptcy or another special extension is not decided here. [ITA150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html); [balance-due day, ITA248](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html). Instalments are federal rules covering federal and Alberta tax together: see `ca-fed-instalments`.

## Penalties and interest

Alberta tax is assessed and collected with federal tax, so the federal penalties apply to the combined balance (CRA, 2025 return):

- **Late filing:** 5% of tax unpaid when the return was required to be filed, plus1% of that base per complete month late, up to12months.
- **Repeated late filing:** both a current demand to file and a qualifying penalty payable before this failure for a return in any of the three preceding taxation years are required. For2025 those years are2022-2024; for2026 they are2023-2025. The rate is10% plus2% per complete month, at most20months, on the statutory unpaid-tax base.
- **Interest:** "the CRA charges compound daily interest starting the day after the due date." Obtain the applicable prescribed rate for each outstanding period; no actual interest-rate figure is supplied here.

## Cross-border points

- **Moving between provinces:** only the province of residence on 31 December taxes the year, apart from the business income split in s.6.1(3) and (4). Ask where the client lived on 31 December, not where the money was earned.
- **Foreign income of an Alberta resident:** included through the correctly determined federal taxable base. The provincial foreign tax credit is a per-country, non-business-income-tax calculation under s.23, limited by both the excess over amounts that COULD have been claimed federally (not merely what was claimed) and the Alberta tax attributable under its statutory fraction. FormT2036 feeds2025 AB428 line69; a foreign business tax, exempt income or unused federal tax is not automatically an Alberta credit. Actual foreign-tax computation: **NON-USABLE HOLD: Check this point with one of our partner accountants.**
- **Overseas employment tax credit:** Alberta s.22 refers to35% of a federal s.122.3 deduction, but the federal specified amount is nil and specified percentage0% for2016 and subsequent years. It does not produce a2025 or2026 credit. [Federal s.122.3(1.01)-(1.02)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-122.3.html).
- **Leaving Canada:** Alberta tax still applies for the part of the year before departure (s.3(1), s.6.1(5)), with the category-specific part-year and applicable income-allocation credit restrictions (ss.36.1,40), not an automatic day-count proration of every credit. The departure return and the T1244 deferral are in `ca-ab-departure-tax-t1244-security-election-defer`.
- **Arriving in Canada:** credits are restricted for part-year residents (s.36.1). Use `ca-tax-residency` for the arrival date.

## Worked examples

Both examples are conditional calculations using the stated allowable T1 credit inputs, ordinary full-year individual treatment, no multi-jurisdiction allocation, and no unlisted tax adjustments. They do not establish credit eligibility from income alone; apply the statutory conditions above.

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

## When to refuse or refer

For nonresident/trust, actual foreign-tax, unresolved higher-band statutory-base interpretation, or another item expressly marked unverified, the outcome is a **NON-USABLE HOLD. Check this point with one of our partner accountants.** The published thresholds, properly conditioned credits and both original worked cases remain usable within their stated scope. The old AFETC, climate/federal carbon-rebate and resource/farm/SR&ED references do not create an AB428 claim.

## Ask the client first

1. Where did you live on 31 December of the year? If you moved during the year, when and from where? If unknown, do not work out provincial tax.
2. Did you have business income earned outside Alberta (or, if you live in another province, inside Alberta)?
3. Your taxable income (line 26000) and net income (line 23600), and your spouse's or dependant's net income. If marital status is unknown, assume single and claim no spouse amount.
4. Your age on 31 December, any pension income, and whether a T2201 disability certificate is approved for you or a dependant.
5. Medical expenses, donations, Alberta political contributions, and any unused Alberta tuition carried forward (Schedule AB(S11)).
6. Did you leave or enter Canada in the year, and did you pay foreign tax?

## Sources

| New bounded reading / reuse | Official URL | Actual read date |
|---|---|---|
| Selected operative ss.1(4),3-13.1,17-24,27,28-30.2,35.4,36-41,44.2; cover still states11December2025, with2026c3 listed not in force. Exact private quotations distinguish the higher-band reference anomaly | https://kings-printer.alberta.ca/documents/Acts/A30.pdf | 2026-11-28 |
| Alberta published2025/2026 bracket table and2026 escalator; ACFB eligibility, separate maxima and usual payments | https://www.alberta.ca/personal-income-tax; https://www.alberta.ca/alberta-child-and-family-benefit | 2026-11-28 |
| Native2025 AB428 PDF, all three pages of extracted clauses/fields;2026 TD1AB native two-page text, payroll-purpose and qualification boundaries | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.pdf; https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf | 2026-11-28 |
| Federal annual filing/balance-due definitions; overseas credit nil/zero from2016;2026 caregiver amendment2 and commencement/indexation | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html; https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html; https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-122.3.html; https://kings-printer.alberta.ca/documents/Acts/2026ch03_unpr.pdf | 2026-11-28 |


The original8November inventory below is retained as historical source provenance. Selected operative Act provisions and the2026 amendment, Alberta's current bracket/ACFB pages, the native2025 AB428 PDF,2026 TD1AB and federal deadline/OETC clauses were checked on28November2026. The old worksheet/e-text, payroll page and Budget PDF were not recovered in that check; a failed link or download is not treated as a source read.


| Source | URL | Read on |
|---|---|---|
| Alberta Personal Income Tax Act, RSA 2000 c A-30, consolidation current as of 11 December 2025 (Alberta King's Printer): ss.3, 4, 5, 6.1, 11, 12, 13.1, 20.2, 21, 22, 23, 24, 27, 30.2, 36.1, 40, 44.2 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf | 2026-11-08 |
| CRA, 2025 Form AB428 Alberta Tax and Credits (5009-C), e-text, Parts A, B and C read for bands, credit lines and the 8% rate | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt | 2026-11-08 |
| CRA, 2025 Worksheet AB428 (5009-D), e-text, read for age, caregiver, infirm dependant, disability, dividend, political contribution and supplemental credit lines | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt | 2026-11-08 |
| CRA, Current year tax rates and income brackets (2026), read for the Alberta rate table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-08 |
| CRA, Last year tax rates and income brackets (2025), read for the Alberta rate table and footnote 2 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html | 2026-11-08 |
| CRA, TD1AB 2026 Alberta Personal Tax Credits Return, lines 1 to 8 read for 2026 credit amounts | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf | 2026-11-08 |
| CRA, T4127 Payroll Deductions Formulas, 123rd edition, effective 1 July 2026, read for Tables 8.1 and 8.2 (Alberta) | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html | 2026-11-08 |
| Government of Alberta, Personal income tax, read for the overview, Table 1 and the child and family benefit | https://www.alberta.ca/personal-income-tax | 2026-11-08 |
| CRA, Due dates and payment dates (individuals), read for the 2025 filing and payment dates | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-08 |
| CRA, Interest and penalties on late taxes, read for the late-filing penalty and interest | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | 2026-11-08 |
| Government of Alberta, Budget 2026 Fiscal Plan 2026-29, Tax Plan, read for the Non-Refundable Tax Credits and Alberta Child and Family Benefit tables (printed page 130), the Major Provincial Tax Rates, 2026 table (page 132) and the new Alberta caregiver credit (page 123) | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf | 2026-11-08 |
| Fiscal Measures Statutes Amendment Act, 2026, SA 2026 c3, s.2 (not in force provisions, current as of 30 June 2026) | https://kings-printer.alberta.ca/documents/Acts/2026ch03_unpr.pdf | 2026-11-08 |

The derived2026 medical threshold$2,942, supplemental base$4,896 and under18 care threshold$3,594 follow the read Act and2% indexing, not newly read2026 form boxes. The annual2026 filing/payment dates are now statutory calendar derivations. Historical Alberta Climate Leadership Adjustment entitlement was extinguished at the end of31December2025, with no refund after that date (s.35.4).

Not yet confirmed: **NON-USABLE HOLD: Check this point with one of our partner accountants.** The2026 AB428/worksheet fields have not been verified here; the third-and-higher cumulative-base cross-reference remains unresolved as explained above; the historical payroll constants and unverified annual worksheet dividend percentages are not filing instructions. The actual prescribed interest rate, a complete ACFB phase-out/payment calculation, any current federal Canada Carbon Rebate, the old Alberta royalty/small-farm/SR&ED-top-up references, the provincial payroll-tax assertion and combined federal/Alberta marginal rates remain unverified or outside this computation. Their historical topics are retained as research/referral destinations; no current individual entitlement follows from them.
