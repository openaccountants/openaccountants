---
name: us-foreign-earned-income-2555
description: Work out a US citizen's or green card holder's 2026 foreign earned income exclusion and foreign housing exclusion or deduction on Form 2555, and decide between the exclusion, the foreign tax credit, or both. Covers the tax home test, the bona fide residence and physical presence (330 full days) tests, the 2026 maximum exclusion of USD 132,900, the housing base of USD 21,264 and the general housing limit of USD 39,870 with the Notice 2026-25 city limits, the stacking rule, the credits the election blocks, the revocation bar, self-employment tax and totalization, and the June 15 extension for people abroad. Trigger on "FEIE", "Form 2555", "foreign earned income exclusion", "housing exclusion", "physical presence test", "bona fide residence", "expat US tax", "FEIE or foreign tax credit". Load us-foreign-tax-credit-1116 for the credit itself. Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# US foreign earned income exclusion and housing (Form 2555), tax year 2026

> **Source-cited draft.** Built from the 2026 Form 2555 and its 2026 instructions, Rev. Proc. 2025-32, Notice 2026-25, IRS Pub. 54 (December 2025), 26 U.S.C. 911, 1402 and 1411, Treas. Reg. 1.911-7 and the SSA list of totalization agreements, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 a qualifying US citizen or resident alien working abroad can exclude up to **USD 132,900** of foreign earned income (Form 2555 line 37), plus a housing amount: qualified housing costs, capped at **USD 39,870** for most places or the higher city limit in Notice 2026-25 (London USD 68,600, Singapore USD 86,700, Geneva USD 116,900), minus a base of **USD 21,264**. To qualify, the person's tax home must be abroad and they must pass either the bona fide residence test (a full tax year of foreign residence) or the physical presence test (330 full days abroad in 12 consecutive months). The exclusion is an income tax exclusion only: self-employment tax is still due on all of the profit. Tax on income that is not excluded is worked out at the rates that would apply without the exclusion. Claiming it switches off the additional child tax credit and the earned income credit, and dropping it later locks the person out for 5 years.

## Scope and who this is for

In scope: one individual's 2026 Form 2555, filed with Form 1040, for:

- a US citizen of any age living and working outside the United States;
- a resident alien (for example a green card holder) who meets one of the tests. A green card holder stays a US tax resident while the green card is held, wherever they live; see `us-tax-residency`;
- employees of foreign employers, of US employers abroad, and of foreign subsidiaries of US groups;
- sole proprietors and single-member LLCs disregarded for federal tax who work abroad.

The skill covers: the tax home test, both presence tests and the 12-month window choice, what counts as foreign earned income, the housing exclusion and housing deduction, the exclusion computation, the stacking rule, the credits and deductions the election blocks, the election and its revocation, self-employment tax and totalization agreements, the choice between the exclusion and the foreign tax credit, and the filing extensions for people abroad.

**The starting principle.** The United States taxes its citizens and resident aliens on worldwide income wherever they live. Living abroad does not stop the filing duty; the exclusion is claimed on a filed Form 1040 with Form 2555 attached, and without a valid election there is no exclusion. The question is never "do I file?" but "how much can be excluded or credited?". Source: [Instructions for Form 2555 (2026), General Information](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The foreign tax credit itself (Form 1116 categories, limit, carryovers, currency) | `us-foreign-tax-credit-1116` |
| The rest of Form 1040, the 2026 tax brackets and the standard deduction | `us-form-1040-individual-return` |
| Self-employment tax computation (Schedule SE) | `us-schedule-c-and-se-computation` |
| FBAR (FinCEN Form 114) and Form 8938 | `us-fbar-and-fatca-8938` |
| PFIC, CFC and GILTI or net CFC tested income, Form 5471 | `us-gilti-fdii-beat`, `us-form-5471-cfc-information` |
| Foreign trusts (Forms 3520 and 3520-A) | `us-foreign-trust-reporting` |
| Moving abroad: the wider checklist (state ties, pensions, PFIC funds) | `us-citizen-moving-abroad-tax` |
| Renouncing citizenship or giving up a long-held green card (section 877A, Form 8854) | `us-expatriation-exit-tax` |
| Who is a US tax resident (green card test, substantial presence) | `us-tax-residency` |
| Child tax credit and earned income credit rules | `us-child-tax-credit-and-eitc` |
| Quarterly estimated tax | `us-quarterly-estimated-tax` |
| Qualified business income deduction | `us-qbi-deduction` |
| State residency while abroad (California, New York, Virginia and others) | `us-multi-state-residency-and-allocation` |
| Nonresident aliens | `us-form-1040-nr-nonresident-return` |

## Ask the client first

1. **Status.** US citizen or green card holder? If a green card holder, of which country are you a citizen or national (the bona fide residence test needs a treaty country)? Have you filed Form I-407 or otherwise given up the green card?
2. **Who pays you.** If it is the US government or one of its agencies, that pay can never be excluded.
3. **Tax home and abode.** Where is your main place of work? Where do your family, home, bank accounts and personal ties sit? Do you keep a US home you return to between work periods (rotational work)?
4. **Exact travel dates** for the whole period abroad: every day in the US, every day in transit or over international waters, and any time in Cuba. Passport stamps, boarding passes and travel records are the evidence.
5. **Foreign residence.** Have you told the foreign tax authority that you are **not** a resident there? Did they accept that?
6. **Income.** Wages, self-employment profit, bonuses paid in a later year, employer-paid housing or allowances, meals and lodging on the employer's premises? Any pension, investment or rental income (never excludable)? Any work days in the US?
7. **Foreign tax.** How much foreign income tax did you pay or owe on the wages, for which period, and in which currency?
8. **Housing.** Rent, utilities, insurance, parking and repairs abroad, the city, and whether a spouse also qualifies or lives elsewhere.
9. **Election history.** Have you **ever** filed Form 2555? In which years? Have you ever revoked it, or claimed the foreign tax credit, the additional child tax credit or the earned income credit in a later year instead?
10. **Family credits and retirement.** Children for whom you want the child tax credit? Plans to contribute to an IRA?
11. **Self-employed clients.** Which country's social security system covers you, and do you hold a certificate of coverage?
12. **Spouse.** Does your spouse also qualify? Same household or a separate one? Joint or separate return?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Maximum foreign earned income exclusion, per qualifying individual (Form 2555 line 37) | USD 132,900 | [Rev. Proc. 2025-32, section 4.39](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Base housing amount, full year (16% of USD 132,900, line 32) | USD 21,264 | [Notice 2026-25, section 2](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| Base housing amount, per qualifying day (line 32) | USD 58.26 | [Form 2555 (2026), line 32](https://www.irs.gov/pub/irs-pdf/f2555.pdf) |
| General limit on housing expenses, full year (30% of USD 132,900) | USD 39,870 | [Notice 2026-25, section 2](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| General limit on housing expenses, per qualifying day | USD 109.23 | [Instructions for Form 2555 (2026), line 29b](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| City limit, London, United Kingdom (full year / daily) | USD 68,600 / 187.95 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Singapore (full year / daily) | USD 86,700 / 237.53 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Geneva, Switzerland (full year / daily) | USD 116,900 / 320.27 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Hong Kong, China (full year / daily) | USD 114,300 / 313.15 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Dubai, United Arab Emirates (full year / daily) | USD 57,174 / 156.64 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Tokyo City, Japan (full year / daily) | USD 67,300 / 184.38 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Paris area (Garches, Paris, Sevres, Suresnes, Versailles), France (full year / daily) | USD 73,600 / 201.64 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Alverca and Lisbon, Portugal (full year / daily) | USD 44,800 / 122.74 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Ingolstadt and Munich, Germany (full year / daily) | USD 51,500 / 141.10 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Sydney, Australia (full year / daily) | USD 65,600 / 179.73 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| City limit, Toronto, Canada (full year / daily) | USD 62,700 / 171.78 | [Notice 2026-25, section 3](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| Physical presence test: full days in a foreign country in any 12 consecutive months | 330 | [26 U.S.C. 911(d)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| Earned income cap where capital is material in an unincorporated business (share of net profits) | 30% | [26 U.S.C. 911(d)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| Revocation bar: no new election before this tax year after the revocation year, without IRS consent | 6th | [26 U.S.C. 911(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| Late election on an original return: filed within this time after the due date (without extensions) | 1 year | [Treas. Reg. 1.911-7(a)(2)(i)(C)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFRc52a9ea341d6d9f/section-1.911-7) |
| Housing deduction carryover | 1 year only (to 2027) | [Instructions for Form 2555 (2026), line 49](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Automatic extension to file and pay for people living abroad, 2026 return | 15 June 2027 | [Instructions for Form 2555 (2026), When To File](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Discretionary extra extension for taxpayers out of the country (by letter) | 15 December | [IRS Pub. 54, Additional extension of time](https://www.irs.gov/pub/irs-pdf/p54.pdf) |
| No self-employment tax below this net earnings amount | USD 400 | [26 U.S.C. 1402(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm) |
| US social security (totalization) agreements in force | 31 countries (Romania from 1 September 2026) | [SSA, U.S. International Social Security Agreements](https://www.ssa.gov/international/agreements_overview.html) |

The exclusion and both housing amounts are worked out on a daily basis and multiplied by the qualifying days in the tax year, so a part year gets a smaller exclusion, a smaller base and a smaller limit. A city limit applies only if the place is in the Notice 2026-25 table; anywhere else uses USD 39,870 (or USD 109.23 a day). The Notice lists many more places than the selection above; look the city up in the Notice itself.

### Step 1. Confirm the person and the income are in scope

The person is a US citizen or resident alien with pay for personal services performed abroad. Separate out at once the income the exclusion never covers: pensions and annuities (including social security), interest, dividends, capital gains, alimony, rents, and pay from the US government. Source: [Instructions for Form 2555 (2026), Part IV](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

### Step 2. The tax home test

The tax home must be in a foreign country throughout the period of bona fide residence or physical presence. Source: [Instructions for Form 2555 (2026), Tax home test](https://www.irs.gov/pub/irs-pdf/i2555.pdf); [26 U.S.C. 911(d)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm).

- The tax home is the regular or principal place of business, employment or post of duty, wherever the family lives. With no regular place of business, it is the regular place of abode.
- There is no foreign tax home for any period in which the **abode** is in the United States. Abode follows family, economic and personal ties. Keeping a US dwelling, or a temporary stay in the US, does not by itself put the abode there, but both count against the person.
- The IRS example: a worker on an offshore rig on a 28-day-on, 28-day-off rota who goes home to the US in the off weeks has a US abode and cannot claim either exclusion or the housing deduction.
- Exception: a person serving in a combat zone in support of the US Armed Forces can have a foreign tax home even with a US abode.
- A digital nomad with no fixed place of work may have no foreign tax home at all. Confirm it affirmatively: where are the home, family, bank accounts, driving licence and mailing address? If most are abroad, the tax home is likely abroad; if not, stop and refer (R-FEIE-13).

### Step 3. One presence test

Record which test is used, the dates and the day count. Form 2555 has Part II (bona fide residence) and Part III (physical presence): complete one, not both. A person can use one test in one year and the other in another. Source: [Instructions for Form 2555 (2026), Part I caution](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

**Bona fide residence test** ([26 U.S.C. 911(d)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm); [Instructions for Form 2555 (2026), Part II](https://www.irs.gov/pub/irs-pdf/i2555.pdf)):

- Open to a US citizen, and to a resident alien **only if** that person is a citizen or national of a country with which the US has an income tax treaty in effect (IRS Treaty Table 3).
- The person must be a bona fide resident of a foreign country for an uninterrupted period that includes an **entire tax year** (1 January to 31 December for a calendar-year filer). Once that full year is met, the residence period can run back into part of the year before and on into part of the year after, so a move-in year and a move-out year can also qualify for the days of residence.
- It turns on intention about the length and nature of the stay; acts outweigh words. A definite, temporary purpose followed by a return to the US is not residence; an extended, indefinite stay with a home made abroad may be. Factors: stated intention, length of stay and trips back, where the family lives, the type of housing (long lease or hotel), local integration (bank account, licence, local tax filings as a resident), and the nature of the job.
- Brief, temporary trips to the US do not break the residence.
- If the person gave the foreign authorities a statement that they are **not** resident there, and the authorities hold them not subject to tax for that reason, or have not ruled against that claim, they are **not** a bona fide resident of that country (Form 2555 lines 13a and 13b).
- Illustrations: a citizen who moved to London in March 2025 and has lived there since on a long lease, filing UK returns as a UK resident, with family in London and only occasional US trips, can meet the test for all of 2026 (and for the 2025 days after the move once 2026 is met). A citizen on a 9-month Tokyo assignment who returns each summer does not. A nomad moving between three countries every 3 months is not a bona fide resident anywhere and should look to the physical presence test.

**Physical presence test** ([26 U.S.C. 911(d)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm); [Instructions for Form 2555 (2026), Part III and line 16](https://www.irs.gov/pub/irs-pdf/i2555.pdf)):

- Open to US citizens and resident aliens.
- At least **330 full days** in a foreign country or countries during any 12 months in a row. A full day is the 24 hours starting at midnight, so the day of arrival or departure is usually not a full day.
- The days need not be consecutive: add up the separate periods abroad. The count may be interrupted by travel over international waters or other time not in a foreign country, but those days are not foreign days. "Foreign country" includes its territorial waters and airspace, and excludes international waters and the airspace above them, US territories and Antarctica.
- Holidays, sick days and other non-work days abroad count as foreign days.
- The 12-month period must include 365 days (366 in a leap year), part of which falls in 2026; it can begin or end in another calendar year. Both dates go on line 16; "Continues" is not allowed for the end date.
- **Choose the window.** The person picks the 12-month window, and different windows can be used for different tax years, even if they overlap. A first-year or final-year expat can often qualify for part of both years by choosing two windows that each hold 330 full days. Example: a citizen arrives in Dubai on 15 March 2025 and leaves on 31 August 2026, with few US trips. A window from 16 March 2025 to 15 March 2026 can support the 2025 return (16 March to 31 December 2025); a window from 1 September 2025 to 31 August 2026 can support 2026 (1 January to 31 August 2026, 243 days), if each window holds 330 full foreign days.
- Keep a trip-by-trip log of every US day in the window, a running 330-day tally, and the evidence (passport stamps, tickets, boarding passes). Form 2555 Part III asks for the US days in the window, and it must agree with the log. A wrong US day count is the most common way this claim fails.

**Cuba.** Days in Cuba in breach of US travel restrictions do not count for either test, income earned there is not foreign earned income, and housing costs there are not qualified housing expenses. Work at the US Naval Base at Guantanamo Bay is not a breach. Source: [Instructions for Form 2555 (2026), Travel to Cuba](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

**Waiver for war, civil unrest or similar adverse conditions.** If the person had to leave a country the IRS lists for the year, the minimum time can be waived for the days actually spent there, if they can show they would otherwise have met the test. Attach a statement and write "Claiming Waiver" in the top margin of page 1 of Form 2555. The IRS publishes the list of qualifying countries and dates for the previous year in the Internal Revenue Bulletin each year; check it before rejecting a person who is short of 330 days because of an evacuation. Source: [Instructions for Form 2555 (2026), Waiver of Time Requirements](https://www.irs.gov/pub/irs-pdf/i2555.pdf); [26 U.S.C. 911(d)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm).

### Step 4. Foreign earned income (Form 2555 Part IV, lines 19 to 26)

Foreign earned income is wages, salaries, professional fees and other pay for personal services performed in a foreign country during the qualifying period, including noncash pay (such as a home or car) and allowances or reimbursements (housing, education, cost of living, hardship). Source: [Instructions for Form 2555 (2026), Part IV](https://www.irs.gov/pub/irs-pdf/i2555.pdf); [26 U.S.C. 911(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm).

- **Source is where the work is done**, not where the money is paid. A citizen living in Lisbon who works there for a US client paid into a US account has foreign earned income. If the same person spends 60 working days in Boston, the pay for those days is US source and cannot be excluded.
- **Days split.** Where work is done partly in and partly outside the US, split the pay by working days.
- **Not foreign earned income:** pensions and annuities (including social security and railroad retirement benefits treated as social security); interest, ordinary dividends, capital gains, alimony and other investment income; pay as an employee of the US government or its agencies (including military pay; the separate combat zone exclusion is outside this skill); amounts received after the end of the tax year following the year the work was done; amounts included because of employer contributions to a nonexempt employees' trust or a nonqualified annuity; and amounts that are really a distribution of company profits rather than reasonable pay for the work.
- **Business with capital (line 20).** If both personal services and capital are material income-producing factors in an unincorporated business, only reasonable pay for the services is earned income, capped at **30%** of the person's share of net profits after the deduction for the employer-equivalent part of self-employment tax. If capital is not material, all of the gross income is earned income.
- **Timing.** Income is earned in the year the work is done. A cash-basis employee whose last 2025 salary payment arrived in 2026 because of payroll timing may treat it as 2026 income. Otherwise, 2026 pay for 2025 work is excluded only to the extent it would have been excludable in 2025: leave it out of Part IV, attach a statement, and enter it to the left of line 45 as "Exclusion of Income Earned in 2025". Pay received in 2025 for 2026 work is excluded by amending 2025 on Form 1040-X.
- **Meals and lodging (line 25).** Meals and lodging provided for the employer's convenience on the employer's business premises (lodging a condition of employment; a camp can count as business premises) are excluded under section 119 on line 25 and are not housing expenses.

### Step 5. Housing first (Form 2555 Part VI, lines 28 to 36)

The housing amount is worked out **before** the exclusion. Source: [Instructions for Form 2555 (2026), Part VI](https://www.irs.gov/pub/irs-pdf/i2555.pdf); [26 U.S.C. 911(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm).

1. **Line 28, qualified housing expenses.** Reasonable (not lavish or extravagant) costs for the person and, if they live with the person, the spouse and dependents: rent, utilities other than telephone, real and personal property insurance, nonrefundable fees to obtain a lease, furniture and accessories rental, residential parking, household repairs, and the fair rental value of employer-provided housing not excluded on line 25. Not included: deductible interest and taxes, amounts deductible by a cooperative housing tenant-stockholder, buying or improving a home, mortgage principal, depreciation, domestic labour, pay television, and buying furniture. Owners of a home abroad therefore have far less to claim than renters. Count expenses only for the qualifying period and only while section 119 is not already excluding the housing.
2. **Second foreign household.** Costs of a separate foreign home for the spouse and dependents count only if they live away from the tax home because conditions there are dangerous, unhealthful or otherwise adverse.
3. **Lines 29a and 29b, the limit.** Enter the location on line 29a only if it is in Notice 2026-25. Line 29b is USD 39,870 for an unlisted place and a full year; otherwise use the Limit on Housing Expenses Worksheet: qualifying days times the daily limit (USD 109.23 or the city's daily figure). A person who moved during 2026 runs the worksheet for each place by days lived there and adds the results; the total days cannot exceed line 31.
4. **Line 30** is the smaller of line 28 and line 29b. **Line 31** is the qualifying days in 2026. **Line 32**, the base, is USD 58.26 times line 31 (USD 21,264 for 365 days). **Line 33** is line 30 minus line 32; if zero or less, there is no housing exclusion or deduction.
5. **Lines 34 to 36, the exclusion.** Line 34 is employer-provided amounts: wages and salary from the employer (so an employee paying rent out of salary still has employer-provided amounts), in-kind pay, rent paid by the employer to the landlord, and reimbursements of housing, school fees or tax equalisation. Line 35 is line 34 divided by line 27 (at least three decimal places). Line 36, the housing exclusion, is line 33 times line 35, not more than line 34.
6. **Reduce** the housing amount by any nontaxable US government housing allowance received by the person or the spouse (see Pub. 54).

**Married couples, housing.** If both spouses qualify and share one foreign household on a joint return, they may figure housing jointly (either spouse, not both, claims it; that spouse may combine both spouses' expenses up to the limit and subtracts their own base; if the claiming spouse has the shorter qualifying period, only that period's expenses count) or separately (each uses their own base and they may allocate expenses between them with no duplication). Filing separately while sharing a household, they must figure it separately. Spouses with separate foreign households can each claim their own only if their tax homes are not within reasonable commuting distance of each other and neither household is within reasonable commuting distance of the other's tax home; otherwise only one can claim. Source: [Instructions for Form 2555 (2026), Married couples](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

**Election to use next year's city limit.** For 2025 returns, a person may use the 2026 limit in Notice 2026-25 where it is higher than the 2025 limit in Notice 2025-16. The IRS expects to allow the 2027 limits for 2026 returns in the next annual notice; that election is not yet available. Source: [Notice 2026-25, section 4](https://www.irs.gov/pub/irs-drop/n-26-25.pdf).

### Step 6. The exclusion (Part VII, lines 37 to 42) and the total (Part VIII, lines 43 to 45)

1. **Line 37:** USD 132,900. **Lines 38 and 39:** the qualifying days and the fraction of the year (1.000 for the full year). **Line 40:** line 37 times line 39.
2. **Line 41:** foreign earned income (line 27) minus the housing exclusion (line 36). **Line 42**, the exclusion, is the smaller of line 40 and line 41.
3. **Line 43:** housing exclusion plus the exclusion. The total can never exceed foreign earned income. Source: [Form 2555 (2026), Parts VII and VIII](https://www.irs.gov/pub/irs-pdf/f2555.pdf).
4. **Line 44, deductions related to excluded income.** No deduction, credit or exclusion definitely related to the excluded income is allowed. If only part of the foreign earned income is excluded, prorate by excludable over total foreign earned income. Examples: Schedule C expenses of the foreign business and the deductible half of self-employment tax. The section 119 exclusion and the housing deduction are not treated as related. Source: [Instructions for Form 2555 (2026), Part VIII and line 44](https://www.irs.gov/pub/irs-pdf/i2555.pdf); [26 U.S.C. 911(d)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm).
5. **Line 45** = line 43 minus line 44, entered on Schedule 1 (Form 1040), line 8d as a negative amount.
6. **Married couples, exclusion.** Each qualifying spouse figures their own exclusion on their own Form 2555, up to USD 132,900 each (USD 265,800 for two). Community property splitting does not change the amount. Each spouse's exclusion is limited to that spouse's own foreign earned income.

### Step 7. The housing deduction (Part IX, lines 46 to 50)

For the part of the housing amount not paid with employer-provided amounts, which in practice means self-employment income. If all foreign earned income is self-employment income, enter zero on line 36 and go to Part IX. Line 46 is line 33 minus line 36; line 47 is line 27 minus line 43; line 48 is the smaller. Line 49 adds the 2025 carryover from the Housing Deduction Carryover Worksheet. Line 50 goes to Schedule 1 (Form 1040), line 24j. An amount over the line 47 limit carries to 2027 only; if 2027 cannot use it, it is lost. A person claiming the housing deduction must use the Foreign Earned Income Tax Worksheet. Source: [Form 2555 (2026), Part IX](https://www.irs.gov/pub/irs-pdf/f2555.pdf); [Instructions for Form 2555 (2026), line 49](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

The housing exclusion and the earned income exclusion are separate elections. No election is needed for the housing deduction, but the person must give the IRS enough information to work it out. Source: [Treas. Reg. 1.911-7(a)(3)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFRc52a9ea341d6d9f/section-1.911-7).

### Step 8. Tax on what is left: the stacking rule

If any amount is excluded, the tax on the remaining taxable income is the tax on (taxable income plus the excluded amount) minus the tax on the excluded amount alone. The remaining income is therefore taxed at the rates it would have met without the exclusion; the low brackets are used up by the excluded amount. Use the Foreign Earned Income Tax Worksheet in the Form 1040 instructions for line 16, and the separate worksheet in the Form 6251 instructions for the alternative minimum tax. Source: [26 U.S.C. 911(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm); [Instructions for Form 2555 (2026), Figuring Tax on Income Not Excluded](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

- The 2026 brackets and standard deduction are in `us-form-1040-individual-return`.
- Section 911(f) covers the regular tax and the alternative minimum tax, including the capital gains rate computation within them. Software usually handles the worksheet; hand-prepared returns often miss it, so check the worksheet output, not only the bottom line.
- **Net investment income tax.** For the 3.8% tax, modified adjusted gross income adds back the excluded amount, net of the deductions disallowed under section 911(d)(6). Source: [26 U.S.C. 1411(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm). The Additional Medicare Tax on self-employment income is figured on Schedule SE earnings, which the exclusion never reduces.

### Step 9. What the election blocks

In any year the person claims either exclusion or the housing deduction:

- **No additional child tax credit** (the refundable part) and **no earned income credit**. The non-refundable child tax credit can still apply; modified adjusted gross income for its phase-out adds back the excluded income. See `us-child-tax-credit-and-eitc`.
- **No credit or deduction for foreign tax on excluded income.** If all the foreign earned income is excluded, none of the foreign tax on it can be credited. If part is excluded, the tax allocable to the excluded part is lost; the fraction is set out in `us-foreign-tax-credit-1116` (Form 1116 line 12).
- **IRA.** Special rules apply to the IRA deduction; excluded pay is not compensation for this purpose, so a person who excludes all of their pay may have no IRA room (see Pub. 590-A and `us-self-employed-retirement`).
- **Qualified business income.** Excluded income is not taken into account in figuring taxable income, so it is not qualified business income. See `us-qbi-deduction`.
- The exclusion lowers adjusted gross income, which can help with other phase-outs.

Source: [Instructions for Form 2555 (2026), Choosing the Exclusion(s)](https://www.irs.gov/pub/irs-pdf/i2555.pdf); [IRS Pub. 54, Effect of Choosing the Exclusions](https://www.irs.gov/pub/irs-pdf/p54.pdf).

### Step 10. The election, revocation and the 5-year bar

**Making the election.** File Form 2555 with Form 1040, 1040-SR or 1040-X. The election is valid only if made ([Treas. Reg. 1.911-7(a)(2)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFRc52a9ea341d6d9f/section-1.911-7)):

- (A) with a timely filed return, including extensions;
- (B) with an amended return that amends a timely filed return, filed within the section 6511(a) refund period;
- (C) with an original return filed within one year after the due date without extensions (this is not an extension for any other purpose); or
- (D) with a later return, if no tax is owed after the exclusion (before or after the IRS notices), or if tax is owed and the return is filed before the IRS discovers the failure to elect. Write "Filed Pursuant to Section 1.911-7(a)(2)(i)(D)" at the top of page 1 of Form 1040.

**Once made, it continues** for that year and every later year until revoked. It need not be revoked just because there is no foreign earned income in a year. Source: [Instructions for Form 2555 (2026), Choosing the Exclusion(s)](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

**Revoking.** Attach a statement to the return or amended return for the first year the person does not want the exclusion, naming which election (earned income, housing, or both) is revoked; each is revoked separately. Pub. 54 also says the person must make the same choice in a later year, otherwise it is treated as a revocation, and that taking the foreign tax credit or deduction, the additional child tax credit or the earned income credit in a later year counts as revoking. Taking the credit only on foreign tax on pay **above** the exclusion while still excluding is allowed. Source: [IRS Pub. 54, Effect of Revoking the Exclusions](https://www.irs.gov/pub/irs-pdf/p54.pdf).

**The bar.** After a revocation, the person cannot elect the same exclusion again before the **6th tax year after** the year the revocation took effect, unless the IRS consents through a letter ruling request (Pub. 54 names the address and the Rev. Proc. 2024-1 procedure). The IRS weighs things like a period of US residence, a move to a country with different tax rates, or a change of employer. Source: [26 U.S.C. 911(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm).

**The practical trap.** Year 1 the client excludes; year 2 they move to a high-tax country and file with the credit and no Form 2555; year 3 they move back to a low-tax country and file Form 2555 again. Year 2 is a revocation, so year 3 is inside the bar and the exclusion is disallowed. Where the client keeps an election in place but the exclusion would not help this year, the conservative course is to keep filing Form 2555 showing the election remains in effect, or attach a statement that the election under section 911 remains in effect and is not revoked, and model the year before choosing. Whether a zero-exclusion Form 2555 avoids the Pub. 54 deemed revocation once the credit is claimed on the same pay is a judgment call for the reviewer: say so to the client.

### Step 11. The choice: exclusion, credit, or both

Both reliefs answer double taxation; they cannot both apply to the same dollar. Compare, for each year and for the next five:

| Option | When it tends to win | What it costs |
| --- | --- | --- |
| Exclusion only | No or low foreign income tax (for example the UAE, many Gulf states, or a low effective rate) | Loses the additional child tax credit, the earned income credit and usually IRA room; tax on the rest is stacked; switching away later starts the 5-year bar |
| Credit only (Form 1116) | Foreign tax on the pay at or above US tax on it | Needs Form 1116; the credit cannot exceed the US tax on the foreign income; excess carries back 1 year and forward 10 in the same category |
| Exclusion up to the limit plus credit on the rest | Pay well above USD 132,900 in a country with some tax | Tax on the excluded part is lost; the credit only covers the tax allocable to the pay left in income |

- Model the tax under each, the refundable credits lost, IRA and QBI effects, and the carryover each creates (a carryover is worth more if the client expects US-source or lightly taxed foreign income later).
- Self-employment tax does not change between the options: neither the exclusion nor the credit reduces it.
- If one spouse uses the exclusion and the other the credit, model both returns together; the interactions are easy to get wrong.
- The mechanics of the credit are in `us-foreign-tax-credit-1116`. Document the options modelled and why one was chosen.

### Step 12. Self-employment tax and totalization

The exclusion is an income tax exclusion only. Self-employment tax is figured on **all** net earnings from self-employment, including excluded income, and is due once net earnings reach USD 400. Compute it with `us-schedule-c-and-se-computation`. Source: [IRS Pub. 54, Social Security and Medicare Taxes](https://www.irs.gov/pub/irs-pdf/p54.pdf); [26 U.S.C. 1402(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm).

Example: a freelancer in Dubai with USD 130,000 of Schedule C profit may owe no federal income tax after the exclusion but still owes self-employment tax on the whole profit (15.3% of 92.35% of it, with the Social Security part capped by the wage base); the UAE has no US agreement, so there is no relief. Set the expectation on intake: "The exclusion is income tax relief. Self-employment tax is separate and still due."

**Totalization agreements.** The US has social security agreements with 31 countries: Italy, Germany, Switzerland, Belgium, Norway, Canada, the United Kingdom, Sweden, Spain, France, Portugal, the Netherlands, Austria, Finland, Ireland, Luxembourg, Greece, South Korea, Chile, Australia, Japan, Denmark, the Czech Republic, Poland, the Slovak Republic, Hungary, Brazil, Uruguay, Slovenia, Iceland and Romania (in force from 1 September 2026). Source: [SSA, U.S. International Social Security Agreements](https://www.ssa.gov/international/agreements_overview.html).

- Self-employed people subject to both systems are generally covered only by the system of the country where they reside.
- **Covered by the foreign system only:** keep the foreign agency's certificate or statement that the earnings are covered there; it supports the exemption from US self-employment tax (attach it as the agreement requires and note the exemption on Schedule SE).
- **Covered by the US only:** request a certificate of coverage from the SSA Office of Earnings and International Operations (online at SSA.gov/international/CoC_link.html) to be exempt from the foreign tax.
- Only pay after the agreement's effective date can be exempt.
- Countries with no agreement (for example the UAE, Singapore, Hong Kong, Saudi Arabia, Mexico) give no exemption.
- Employees: US social security and Medicare tax generally do not apply to wages for work abroad unless an exception applies, such as an American employer; the exclusion does not change that answer.

Source: [IRS Pub. 54, Bilateral Social Security (Totalization) Agreements](https://www.irs.gov/pub/irs-pdf/p54.pdf).

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| US government employee abroad (civilian or military) | Pay is not foreign earned income; do not file Form 2555; use the credit if foreign tax applies | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Abode in the US (rotational work, family at home) | Fails the tax home test, unless serving in a combat zone in support of the Armed Forces | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Green card holder from a country with no US income tax treaty | Bona fide residence test not available; physical presence test still is | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Told the foreign country you are not resident | Not a bona fide resident of that country | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Fewer than 330 full days in every possible 12-month window | Physical presence test fails, unless the adverse-conditions waiver applies | [26 U.S.C. 911(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| Days in Cuba in breach of US travel rules | Do not count; income and housing there do not qualify | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Work in a US territory (for example Puerto Rico, Guam) | Not a foreign country for section 911; out of scope | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Housing costs at or below the base | No housing exclusion or deduction | [Form 2555 (2026), line 33](https://www.irs.gov/pub/irs-pdf/f2555.pdf) |
| City not in Notice 2026-25 | USD 39,870 full year, USD 109.23 a day | [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) |
| Pension, dividends, interest, capital gains, rents | Never excludable; credit only | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Pay received after the end of the year following the work year | Not excludable | [26 U.S.C. 911(b)(1)(B)(iv)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| Exclusion claimed, children in the family | No additional child tax credit, no earned income credit | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Self-employed abroad with the exclusion | Self-employment tax still due on the full net earnings unless a totalization agreement exempts them | [IRS Pub. 54](https://www.irs.gov/pub/irs-pdf/p54.pdf) |
| Revoked, wants it back within 5 years | Needs IRS consent by letter ruling | [26 U.S.C. 911(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| First year abroad, test not met by the due date | Form 2350 extension, or file without the exclusion and amend on Form 1040-X | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Net loss from the foreign business in the first eligible year | Probably do not elect; if an election is already in place, not claiming it is a revocation | [IRS Pub. 54, chapter 6, Example 4](https://www.irs.gov/pub/irs-pdf/p54.pdf) |
| Both spouses qualify | Each excludes up to USD 132,900 on their own Form 2555; housing by the joint or separate rules | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Which test applies | Physical presence, built from the travel log; bona fide residence only with evidence of an indefinite foreign home |
| Travel dates | No exclusion until a day log supports 330 full days or a full year of residence |
| Election history | Treat as a first election; ask for every return filed since leaving the US before relying on it |
| Whether the city is listed | Use USD 39,870 (USD 109.23 a day) until the Notice 2026-25 table is checked |
| Employer-provided share of housing (line 34) | All wages are employer-provided for an employee; zero for a self-employed person |
| Foreign tax paid | Zero for the comparison until the foreign return or payslips are seen |
| Totalization coverage | Self-employment tax due in full; no exemption without a certificate |
| Spouse's position | Ask; do not assume the spouse qualifies or files jointly |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| US days in the window close to the 35 allowed | One extra day fails the physical presence test |
| Family or home kept in the US, or rotational work | Tax home test may fail outright |
| A statement of nonresidence given to the foreign authority | Bona fide residence is barred in that country |
| Exclusion claimed in an earlier year, credit planned now | Revocation and the 5-year bar |
| Self-employed in a country with no US agreement | Self-employment tax on the whole profit |
| Children and low income | The lost additional child tax credit and earned income credit may outweigh the exclusion |
| Housing near or above the city limit | Check the Notice table and the qualified-expense list line by line |
| Pay from the US government mixed with private pay | The government part can never be excluded |
| Foreign tax at or above US rates | The credit alone may be better and keeps future options open |

## Worked cases

These use the 2026 figures above and, for the stacking, the 2026 single brackets and USD 16,100 standard deduction from Rev. Proc. 2025-32 (owned by `us-form-1040-individual-return`). Taxpayers are invented.

**Case 1, a decision: exclusion plus credit, or credit alone?** A single US citizen works all of 2026 abroad, meets the physical presence test, and earns USD 180,000 of foreign wages. No housing amount, no other income, standard deduction. Run it twice: in a low-tax country (foreign tax 10%, USD 18,000) and in a high-tax country (30%, USD 54,000).

Credit alone: taxable income USD 163,900; US tax USD 31,934. All income is foreign, so the Form 1116 limit is the whole USD 31,934. Exclusion route: exclude USD 132,900; taxable income USD 31,000; stacked tax is tax on USD 163,900 (USD 31,934) minus tax on USD 132,900 (USD 24,494) = USD 7,440. Foreign tax allocable to the excluded pay (132,900 / 180,000 of it) is lost.

- Low-tax country: credit alone leaves USD 31,934 minus USD 18,000 = **USD 13,934** of US tax. Exclusion route: creditable tax is USD 18,000 minus USD 13,290 = USD 4,710, so US tax is USD 7,440 minus USD 4,710 = **USD 2,730**. The exclusion route saves USD 11,204: **choose the exclusion** (then check the lost refundable credits and IRA room).
- High-tax country: both routes leave zero US tax. Credit alone carries forward USD 22,066 of unused credit; the exclusion route carries forward USD 6,690 (USD 14,130 available minus USD 7,440 used) and starts an election that would be costly to revoke. **Choose the credit alone** unless the client is likely to move to a low-tax country soon.

```oa-check
name: FEIE plus credit against credit alone, single, low-tax country (2026)
inputs:
  wages: 180000
  foreign_tax_rate: 0.10
  standard_deduction: 16100
  feie_limit: 132900
steps:
  - foreign_tax: wages * foreign_tax_rate
  - taxable_ftc_only: wages - standard_deduction
  - tax_ftc_only: 0.10 * min(taxable_ftc_only, 12400) + 0.12 * clamp(taxable_ftc_only - 12400, 0, 38000) + 0.22 * clamp(taxable_ftc_only - 50400, 0, 55300) + 0.24 * clamp(taxable_ftc_only - 105700, 0, 96075)
  - us_tax_ftc_only: tax_ftc_only - min(foreign_tax, tax_ftc_only)
  - excluded: min(feie_limit, wages)
  - stack_total: wages - excluded - standard_deduction + excluded
  - tax_on_total: 0.10 * min(stack_total, 12400) + 0.12 * clamp(stack_total - 12400, 0, 38000) + 0.22 * clamp(stack_total - 50400, 0, 55300) + 0.24 * clamp(stack_total - 105700, 0, 96075)
  - tax_on_excluded: 0.10 * min(excluded, 12400) + 0.12 * clamp(excluded - 12400, 0, 38000) + 0.22 * clamp(excluded - 50400, 0, 55300) + 0.24 * clamp(excluded - 105700, 0, 96075)
  - stacked_tax: tax_on_total - tax_on_excluded
  - creditable_tax: foreign_tax - foreign_tax * excluded / wages
  - us_tax_feie: stacked_tax - min(creditable_tax, stacked_tax)
  - feie_saving: us_tax_ftc_only - us_tax_feie
expected:
  tax_ftc_only: 31934.00
  us_tax_ftc_only: 13934.00
  stacked_tax: 7440.00
  creditable_tax: 4710.00
  us_tax_feie: 2730.00
  feie_saving: 11204.00
```

**Case 2, housing in a listed city.** A single employee lives in London for all of 2026 and meets the bona fide residence test. Wages USD 220,000, all foreign earned income; rent, utilities and insurance of USD 75,000, paid out of salary.

Line 30: the smaller of USD 75,000 and the London limit USD 68,600 = USD 68,600. Line 32: USD 21,264. Line 33: USD 47,336. All the income is from the employer, so line 35 is 1.000 and the housing exclusion (line 36) is USD 47,336. Line 41: USD 220,000 minus USD 47,336 = USD 172,664; line 42, the exclusion, is the smaller of USD 132,900 and USD 172,664 = USD 132,900. Line 43: USD 180,236 excluded. USD 39,764 of the wages stay in income, taxed at stacked rates, with a Form 1116 credit for the UK tax allocable to that part (see `us-foreign-tax-credit-1116`). Had London not been listed, line 29b would be USD 39,870 and the housing exclusion only USD 18,606.

```oa-check
name: Housing exclusion and FEIE, London, full year (2026)
inputs:
  wages: 220000
  housing_expenses: 75000
  city_limit: 68600
  general_limit: 39870
  base: 21264
  feie_limit: 132900
  employer_share: 1
steps:
  - line_30: min(housing_expenses, city_limit)
  - line_33: max(line_30 - base, 0)
  - line_36: line_33 * employer_share
  - line_41: wages - line_36
  - line_42: min(feie_limit, line_41)
  - line_43: line_36 + line_42
  - left_in_income: wages - line_43
  - housing_if_unlisted: max(min(housing_expenses, general_limit) - base, 0)
expected:
  line_33: 47336.00
  line_36: 47336.00
  line_42: 132900.00
  line_43: 180236.00
  left_in_income: 39764.00
  housing_if_unlisted: 18606.00
```

**Case 3, part year, by narrative.** A citizen moves abroad and meets the physical presence test with 200 qualifying days in 2026 in Dubai. Exclusion limit: USD 132,900 times 200 / 365 = USD 72,822 (rounded). Base: USD 58.26 times 200 = USD 11,652. Housing limit: Dubai's daily USD 156.64 times 200 = USD 31,328.

**Case 4, self-employed, by narrative (the Pub. 54 pattern).** A consultant abroad qualifies, with foreign earned income of USD 95,000, business expenses of USD 27,000 and net profit of USD 68,000. Self-employment tax is due on the full USD 68,000 even though all of it is excluded from income tax, unless a totalization certificate exempts it. The expenses allocable to the excluded income go on line 44.

**Case 5, the revocation bar, by narrative.** A client excluded for 2024 and claims the credit instead for 2025, so the election is treated as revoked for 2025. They cannot elect again before 2031 (the 6th tax year after 2025) without IRS consent; 2026 to 2030 are barred.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FEIE-1 | Bona fide resident of Puerto Rico or another US territory | Refer: section 933 or the territory's own rules, not section 911 |
| R-FEIE-2 | Has expatriated or plans to renounce or give up a long-held green card | Refer: `us-expatriation-exit-tax` |
| R-FEIE-3 | Holds PFIC funds or CFC shares | Refer: `us-gilti-fdii-beat`, `us-form-5471-cfc-information` and a PFIC (Form 8621) specialist |
| R-FEIE-4 | Foreign trust grantor or beneficiary | Refer: `us-foreign-trust-reporting` |
| R-FEIE-5 | FBAR or Form 8938 exposure | Note it; refer to `us-fbar-and-fatca-8938` |
| R-FEIE-6 | Unfiled returns for three or more years, or in the Streamlined procedures | Refer to a back-filing specialist; the late-election rules in Step 10 decide whether the exclusion survives |
| R-FEIE-7 | Dual residency decided by a treaty tie-breaker | Refer to international tax counsel |
| R-FEIE-8 | Wants to elect again within the 5-year bar | Refer: a letter ruling request is needed |
| R-FEIE-9 | US government or military employee abroad | Refer: section 911 does not apply to that pay; allowances need a specialist |
| R-FEIE-10 | Crypto mining or staking income abroad | Refer: `us-crypto-tax` |
| R-FEIE-11 | Contested state residency (for example California, New York, Virginia) | Refer: `us-multi-state-residency-and-allocation` |
| R-FEIE-12 | Totalization coverage in doubt or a certificate still to be obtained | Flag the exposure; refer the certificate process to a foreign payroll specialist |
| R-FEIE-13 | Tax home or bona fide residence weak (short or fixed posting, nonresident statement, family in the US) and physical presence not met | Do not claim the exclusion; use the credit or refer |
| R-FEIE-14 | Day counts cannot be evidenced from travel records | Do not claim until they can |
| R-FEIE-15 | Waiver for adverse conditions, a second foreign household, or spouses with separate foreign households | Refer unless the facts fit the instructions exactly |
| R-FEIE-16 | Unincorporated business where capital is material (the 30% rule), or pay for work spread over several years | Refer unless the allocation is documented |
| R-FEIE-17 | A late election under Treas. Reg. 1.911-7(a)(2)(i)(D) after the IRS has discovered the failure to elect and tax is owed | Refer: the election is not available |

## Filing and payment

For a 2026 calendar-year return. Sources: [Instructions for Form 2555 (2026), When To File and Where To File](https://www.irs.gov/pub/irs-pdf/i2555.pdf); [IRS Pub. 54](https://www.irs.gov/pub/irs-pdf/p54.pdf).

1. **Regular due date:** 15 April 2027.
2. **Automatic 2-month extension to 15 June 2027**, to file **and pay**, if on the regular due date the person lives outside the US and Puerto Rico and their tax home is outside them. Attach a statement saying both conditions are met. Interest still runs from 15 April. (The old version of this skill tied this extension to section 6072(c), which sets the due date for certain nonresident aliens; the extension comes from the regulations and the IRS instructions.)
3. **Form 4868** by the due date (or by 15 June when using the 2-month extension) extends filing, not payment, to 15 October 2027.
4. **Discretionary extra 2 months to 15 December 2027** for taxpayers out of the country: send the IRS a letter explaining why, by 15 October 2027. The IRS writes only if it refuses. Not available with an approved Form 2350.
5. **First year, test not yet met:** file Form 2350 with the IRS Service Center, Austin, TX 73301-0045, before the due date, for an extension to a date after the person expects to qualify; or file on time without the exclusion and amend on Form 1040-X within 3 years of filing or 2 years of paying, whichever is later.
6. **Where to file:** attach Form 2555 to Form 1040 or 1040-SR. On paper, mail to the special addresses for Form 2555 filers (IRS.gov international where-to-file page), not the address for the state. If the return is e-filed, still check the Foreign Earned Income Tax Worksheet output.
7. **Entries:** line 45 to Schedule 1, line 8d (negative); line 50 to Schedule 1, line 24j. Do not put foreign tax withheld by an employer and paid to the foreign country on Form 1040, line 25a or 25b.
8. **Estimated tax.** People abroad still owe quarterly estimated tax, including self-employment tax; the June extension does not move the 2026 instalments. Income the person reasonably expects to exclude can be left out of the estimate, allowing for the foreign tax credit lost on it. See `us-quarterly-estimated-tax`.

### 2025 returns still being filed on extension

| Item | 2025 | Source |
| --- | --- | --- |
| Maximum exclusion | USD 130,000 | [Rev. Proc. 2024-40, section 2.39](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Base housing amount, full year | USD 20,800 | [Notice 2025-16, section 2](https://www.irs.gov/pub/irs-drop/n-25-16.pdf) |
| General housing limit, full year | USD 39,000 | [Notice 2025-16, section 2](https://www.irs.gov/pub/irs-drop/n-25-16.pdf) |

City limits for 2025 are in Notice 2025-16; a 2025 filer may use the 2026 limit in Notice 2026-25 where higher. The tests, stacking, lost credits, revocation and self-employment rules are the same. The discretionary extension to 15 December 2026 had to be requested by 15 October 2026.

## Completion checklist

- [ ] Citizenship or green card status confirmed; treaty nationality checked for a resident alien using bona fide residence.
- [ ] Payer is not the US government.
- [ ] Tax home abroad and abode tested and documented.
- [ ] One presence test met, with dates and a day log from travel records; the 12-month window chosen to cover the most days.
- [ ] Qualifying days counted; exclusion, base and housing limit prorated.
- [ ] Only foreign earned income in Part IV; pensions, investment income, US-workday pay and late pay removed; prior-year pay handled by statement.
- [ ] Housing figured before the exclusion; the city limit taken from Notice 2026-25 only if listed; qualified expenses checked line by line.
- [ ] Spouse rules for the exclusion and for housing applied.
- [ ] Related deductions disallowed on line 44.
- [ ] Tax figured with the Foreign Earned Income Tax Worksheet (and the Form 6251 version).
- [ ] No credit on foreign tax allocable to excluded income; Form 1116 run for the rest.
- [ ] Additional child tax credit and earned income credit removed; IRA and QBI rechecked.
- [ ] Election history checked for every year abroad; any switch tested against the 5-year bar.
- [ ] Exclusion against credit modelled and the reason recorded.
- [ ] Self-employment tax on all net earnings, or a totalization certificate on file.
- [ ] Extension statement, Form 2350 or Form 4868 as needed; correct mailing address.
- [ ] FBAR and Form 8938 reviewed under `us-fbar-and-fatca-8938`.
- [ ] Reviewer has the day log, housing worksheet, the comparison and the stacking worksheet.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.39: 2026 foreign earned income exclusion USD 132,900. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Notice 2026-25. Read for section 2 (USD 21,264 base, USD 39,870 limit), section 3 (city table), section 4 (option for 2025) and section 6. | https://www.irs.gov/pub/irs-drop/n-26-25.pdf | 2026-11-13 |
| Form 2555 (2026). Read for Parts V to IX, lines 27 to 50, line 32 (USD 58.26, USD 21,264), line 37 (USD 132,900) and line 50 (Schedule 1, line 24j). | https://www.irs.gov/pub/irs-pdf/f2555.pdf | 2026-11-13 |
| Instructions for Form 2555 (2026). Read for What's New, Who Qualifies, Cuba, Waiver, When To File (15 June 2027), Form 2350, Choosing the Exclusion(s), Parts II to IX, line 29b (USD 109.23), married couples, line 44, line 45 and line 49. | https://www.irs.gov/pub/irs-pdf/i2555.pdf | 2026-11-13 |
| IRS Pub. 54 (Rev. December 2025). Read for the 15 December extension, totalization agreements, self-employment tax, Effect of Choosing and Revoking the Exclusions, and chapter 6 Example 4. | https://www.irs.gov/pub/irs-pdf/p54.pdf | 2026-11-13 |
| 26 U.S.C. 911 (govinfo, 2024 edition; not amended by Public Law 119-21). Read for (b)(1), (c), (d)(1) to (d)(6), (e) and (f). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm | 2026-11-13 |
| 26 U.S.C. 1411 (govinfo). Read for (d), modified adjusted gross income adding back the section 911 exclusion. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-13 |
| 26 U.S.C. 1402 (govinfo). Read for (b), the USD 400 floor. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm | 2026-11-13 |
| Treas. Reg. 1.911-7 (eCFR, current to 10 November 2026). Read for (a)(2)(i)(A) to (D), the late-election statement, and (a)(3). | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFRc52a9ea341d6d9f/section-1.911-7 | 2026-11-13 |
| SSA, U.S. International Social Security Agreements. Read for the table of 31 agreements and dates in force (Romania 1 September 2026). | https://www.ssa.gov/international/agreements_overview.html | 2026-11-13 |
| Rev. Proc. 2024-40. Read for section 2.39: the 2025 exclusion, USD 130,000. | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-13 |
| Notice 2025-16. Read for section 2: 2025 base USD 20,800 and limit USD 39,000. | https://www.irs.gov/pub/irs-drop/n-25-16.pdf | 2026-11-13 |

Not yet confirmed: the IRS list of countries qualifying for the adverse-conditions waiver for 2025 and 2026 was not opened, so no country is named; the 2026 Instructions for Form 1040 (Foreign Earned Income Tax Worksheet) and Form 6251 were not read, so their line numbers are not quoted; Pub. 54 for 2026 returns was not yet published (the December 2025 revision was read); the 2027 housing notice that would let 2026 filers use 2027 city limits has not been issued; the 2026 Form 1116 and its instructions were not yet published.
