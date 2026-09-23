---
name: uk-non-dom
description: "Use this skill for any question about UK non-dom rules. Trigger on: \"UK non-dom\", \"UK non-domiciled\", \"remittance basis UK\", \"FIG regime UK\", \"foreign income gains UK new resident\", \"UK domicile rules\", \"UK non-dom reform 2025\", \"arising basis UK\", \"4-year exemption UK tax\", \"UK overseas workday relief\", \"UK non-dom abolished\". Covers the new 4-year FIG regime (from April 2025), transitional provisions for existing non-doms, and remittance basis overview."
version: 1.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - uk-income-tax-sa100
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK non-dom rules: the 4-year foreign income and gains regime

How the UK taxes the foreign income and gains of someone who has recently become UK resident, and what a former remittance basis user does with foreign income and gains that arose before 6 April 2025. Figures are for tax year 2026. In the UK that means the tax year from 6 April 2026 to 5 April 2027, which HMRC writes as 2026 to 2027. Two sources carry a different year and are used anyway: helpsheet HS264 is written for the 2025 to 2026 tax year but states the temporary repatriation facility rate for 2026 to 2027 as well, and the remittance basis charge amounts in Section 4 come from a manual page that applies only to tax years up to and including 2024 to 2025.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Old regime | Remittance basis, based on domicile. Not available for tax years after 2024 to 2025 |
| New regime | The 4-year foreign income and gains regime, based on residence |
| First year of claims | The 2025 to 2026 tax year |
| Duration | A maximum of 4 consecutive tax years, beginning when UK tax residency started |
| Relief | No UK tax on the eligible foreign income and gains actually claimed. Nothing is automatic: a claim is needed for each year |
| Price of claiming | The personal allowance, the capital gains annual exempt amount and other allowances are lost for that year. See Section 2 |
| After the 4 years | Foreign income and gains are taxed as they arise, like any other UK resident |
| Former remittance basis users | Temporary repatriation facility and rebasing. See Section 3 |
| Inheritance tax | Long-term UK residence replaced domicile from 6 April 2025 |
| Primary legislation | Finance Act 2025, Part 2, and the Schedules it introduces |
| Tax authority | HM Revenue and Customs |
| Residence test | The statutory residence test. See `uk-statutory-residence-test` |

## Section 2: The New FIG Regime (From April 2025)

- **The remittance basis has ended.** On 6 April 2025 the 4-year foreign income and gains regime replaced the remittance basis. Domicile is no longer the connecting factor for foreign income and gains. From that date all UK residents are taxed on the arising basis on their worldwide income and gains; the regime is the only exception, and only for amounts claimed inside the window. https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime
- **Who can claim, first year.** An individual is a qualifying new resident for a tax year if they are UK resident in the tax year, have not been UK resident for at least 10 consecutive tax years immediately before the tax year, are not a member of the House of Commons or House of Lords for any part of the tax year, and are at least 10 years old at the start of the tax year. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000
- **Who can claim, later years.** For a later year the individual must be UK resident in the tax year, the tax year must be one of the 3 tax years immediately following the first tax year in which they were a qualifying new resident, and they must not be a member of either House for any part of the tax year. An individual can have been a qualifying new resident for 2022 to 2023, 2023 to 2024 or 2024 to 2025, which is how someone who arrived before the reform can still claim now. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000
- **The window does not stretch.** The regime is available for a maximum period of 4 consecutive years beginning when UK tax residency started, and unused years cannot be rolled over to a later year. If the first 4 years started before 6 April 2025, the regime can be used from the tax year 2025 to 2026 up to and including the last tax year of that 4-year period. https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime
- **Leaving the UK inside the window.** An individual who leaves temporarily and becomes non-UK resident cannot claim for the tax years they were away, but can claim for any qualifying tax years remaining when they return as a UK tax resident. https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime
- **What can be relieved.** Profits of a trade carried on wholly outside the UK, profits of an overseas property business, dividends from non-UK resident companies, interest such as interest paid on a foreign bank account, and foreign capital gains. https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime
- **What cannot.** UK source income and gains are taxed normally. Income from foreign earnings and foreign specific employment income is not eligible under this regime; the route for that income is Overseas Workday Relief in Section 5. Some foreign income is disqualified income, so check the manual for the source in question. No claim can be made for foreign income or gains that accrued before 6 April 2025. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100
- **A claim is compulsory, and it is annual.** There is no de minimis and no automatic application of the relief without a claim. The claim is made on the Self Assessment tax return for the tax year it applies to, and the income and gains to be relieved must be claimed source by source and quantified. A claim for year one does not carry into years two, three or four. An individual may claim for fewer than 4 years, and a year that is not claimed cannot be used later. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100
- **The deadline.** The time limit for a claim is the anniversary of 31 January following the end of the tax year, that is 12 months from the normal filing date. HMRC's own example: the normal filing date for a 2025 to 2026 return is 31 January 2027, so the claim deadline for that year is 31 January 2028. A claim can be amended or withdrawn within the same time limit. The regime gives no discretion to accept a late claim; one can only be allowed under HMRC's general late claims policy. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42300
- **What a claim costs.** An individual who makes a foreign income claim, a foreign gain claim or an Overseas Workday Relief election for a tax year loses, for that year, the personal allowance, blind person's allowance, the tax reductions for married couples and civil partners, the transferable tax allowance for married couples and civil partners, relief for payments for life insurance, and the capital gains annual exempt amount. Foreign qualifying losses accruing in that year cease to be allowable losses, and losses of a trade or property business carried on wholly outside the UK get no loss relief in that year or in any other year. These are lost even if the claim covers only foreign income, only foreign gains, or only the workday relief. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000
- **It does not cut adjusted net income.** Foreign income relief is disregarded when adjusted net income is worked out, so all of the foreign income still counts for tax-free childcare and for the High Income Child Benefit Charge. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000
- **Losses on UK assets are not touched.** Relief on foreign gains is applied before allowable losses are deducted, so losses on UK disposals in the year, and unused losses from years outside a claim, are used against UK gains or carried forward as normal. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000

## Section 3: Transitional Provisions: Existing Non-Doms

For individuals who used the remittance basis before 6 April 2025: Both reliefs below can be used; they are not alternatives.

- **Relief 1: the temporary repatriation facility.** It is a temporary measure available from 6 April 2025 for 3 tax years: 2025 to 2026, 2026 to 2027 and 2027 to 2028. A former remittance basis user can elect to designate amounts of pre-6 April 2025 foreign income and gains, which are then taxed at the reduced rate in the table below. https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf
- **Who can use it.** The individual must be UK resident in the tax year of designation and must have previously used the remittance basis.
- **What can be designated.** Qualifying overseas capital: pre-6 April 2025 foreign income and gains, funds of uncertain origin, capital payments and income from non-UK trusts matched to pre-6 April 2025 foreign income or gains within the trust structure, and overseas assets such as property and investments. Partial designations are allowed; there is no obligation to designate everything.
- **How it is done.** The designation election goes on the "Residence and foreign income and gains (FIG) regime etc" pages, form SA109, of the Self Assessment return. For the 2025 to 2026 return HMRC directs box 50 for the election, box 51 for the total designated other than amounts relating to trusts, box 52 for designations relating to capital payments and benefits from trusts, and box 54 for how much was remitted in the year. Entries must be in sterling.
- **No need to remit in the same year.** The amount designated does not have to be brought to the UK during the facility period. Once designated, that capital can be remitted at any time in the future with no further tax charge, and inside a mixed fund the designated capital is treated as remitted in priority to everything else.
- **What the charge is and is not.** It is a flat charge on capital, not a tax on income or gains. No foreign tax credit is available against it. It does not enter total taxable income or gains, so it does not affect adjusted net income, bands and rates, pension thresholds, or payments on account for the next year. Paying the charge from undesignated pre-6 April 2025 foreign income or gains held offshore is itself an ordinary remittance, so designate the amount used to pay it. https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400
- **Not designated means taxed as before.** Pre-6 April 2025 foreign income and gains that are not designated are taxed at the usual rates when they are remitted to the UK.
- **Records.** The individual must keep their own records of the designated capital and the charge paid, so that later remittances can be shown to be of designated capital. HMRC does not ask for them unless it opens a compliance check.
- **Designation deadlines.** The election must be made in the Self Assessment return for the year, by the anniversary of 31 January following the end of that tax year: 31 January 2028 for 2025 to 2026, 31 January 2029 for 2026 to 2027, and 31 January 2030 for 2027 to 2028. Once the time to amend has passed, an election cannot be withdrawn, and the charge is not repaid if the designated amounts are no longer available. https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320
- **Business investment relief.** A claim for business investment relief on pre-6 April 2025 foreign income and gains invested in a UK company cannot be made after 5 April 2028.

**Temporary repatriation facility charge**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf |
| Charge on amounts designated for the 2025 to 2026 and 2026 to 2027 tax years | 12% | HS264: "For the 2025 to 2026 and 2026 to 2027 tax years that rate is 12%." |
| Charge on amounts designated for the 2027 to 2028 tax year, the last year of the facility | 15% | HS264: "For the 2027 to 2028 tax year that rate is 15%." |

- **Relief 2: rebasing of foreign assets.** Paragraph 1 of Schedule 11 to the Finance Act 2025 applies to a disposal of an asset where all of these are true: the asset was held by the individual on 5 April 2017; the disposal is made on or after 6 April 2025; the asset was not situated in the United Kingdom at any time in the period beginning with 6 March 2024 and ending with 5 April 2025; the individual was not domiciled in the United Kingdom at any time in a tax year before tax year 2025 to 2026, deemed domicile included; and the individual made a remittance basis claim for at least one tax year from 2017 to 2018 up to 2024 to 2025 in which the remittance basis did not apply without a claim. Where it applies, the gain or loss is computed as if the asset had been acquired on 5 April 2017 for its market value on that date. https://www.legislation.gov.uk/ukpga/2025/8/schedule/11
- **Rebasing can be turned off, once.** The individual may elect for the rebasing paragraph not to apply to a disposal. The election is irrevocable and follows the claims procedure and time limit in the Taxes Management Act 1970. https://www.legislation.gov.uk/ukpga/2025/8/schedule/11

## Section 4: Before April 2025: Remittance Basis (History)

- **Old regime mechanics.** A UK resident who was not domiciled in the UK could claim the remittance basis, so that foreign income and gains were taxed only when remitted to the UK. From 6 April 2025 it is not possible to use the remittance basis. https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210
- **Old foreign income and gains are still live.** Foreign income or gains that arose to a former remittance basis user before 6 April 2025 continue to be taxed at the usual rates if they are remitted to the UK on or after that date, unless they are designated under the facility in Section 3. https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210
- **The remittance basis charge.** It was an annual charge payable by long-term UK residents aged 18 or over who claimed the remittance basis. The amounts are in the table below. HMRC states that this guidance applies only to tax years up to and including 2024 to 2025 and remains for reference purposes only, so no such charge arises for tax year 2026.
- **Deemed domicile.** Deemed domicile has two routes. Condition A covers someone born in the UK with a UK domicile of origin who is UK resident for the year. Condition B is that the individual has been UK resident for at least 15 of the 20 tax years immediately preceding the relevant tax year. It still matters for the rebasing test in Section 3. https://www.legislation.gov.uk/ukpga/2007/3/section/835BA

**Remittance basis charge, history only**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210 |
| Annual charge, tax resident in at least seven out of the nine preceding tax years | GBP 30,000 | RDRM32210: "an annual charge of either £30,000 for individuals who have been tax resident in at least seven out of the nine preceding tax" years |
| Annual charge, tax resident in at least twelve out of the fourteen preceding tax years | GBP 60,000 | RDRM32210: "£60,000 for individuals who have been tax resident in at least twelve out of the fourteen preceding tax years" |

This system is history for current years. The regime in Section 2 replaced it.

## Section 5: Overseas Workday Relief (OWR)

- **It survives, on new terms.** Overseas Workday Relief lets a UK resident employee keep out of UK tax the part of the employment income that relates to duties performed outside the UK. The relief period was extended to 4 years to align with the 4-year foreign income and gains regime, and because the remittance basis has gone it is no longer necessary to keep part of the employment income offshore and in an offshore bank account to get the relief. That statement comes from the policy paper published on 30 October 2024. https://www.gov.uk/government/publications/tax-changes-for-non-uk-domiciled-individuals/reforming-the-taxation-of-non-uk-domiciled-individuals
- **Who can elect.** Eligibility for the new relief in a tax year depends on being a qualifying new resident for that year, the same test as in Section 2, subject to the transitional rules below. A claim under the 4-year regime is not needed. Domicile plays no part. https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43560
- **How it is claimed now.** For income earned on or after 6 April 2025 the relief is claimed on the "Residence and foreign income and gains (FIG) regime etc" pages of the Self Assessment return, not on the employment pages. Income earned before 6 April 2025 stays under the rules in force when it was earned. https://www.gov.uk/government/publications/employment-residence-and-domicile-issues-hs211-self-assessment-helpsheet/hs211-employment-residence-and-domicile-issues-2026
- **Apportionment.** The starting point is still the split between UK and non-UK duties: UK-taxable employment income = total employment income multiplied by UK workdays divided by total workdays. This is a common method, not printed on an HMRC page read for this Guide; confirm. Then the financial limit in the table below is applied.
- **The limit is new, but not for everyone yet.** From 6 April 2025 the relief for a qualifying year is capped, and the cap is cumulative across tax returns where earnings for one qualifying year are taxed in more than one year. https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600 An employee who became UK resident in 2023 to 2024 or 2024 to 2025, qualified for Overseas Workday Relief, and elected the remittance basis for at least one of those years is not subject to the limit for any tax year beginning on or after 6 April 2025 and ending before 6 April 2028. Such an employee keeps the relief for their first three years of UK residence, or four if they are a qualifying new resident in 2025 to 2026. An employee who became UK resident in 2022 to 2023 and elected the remittance basis is not eligible for the relief for 2025 to 2026. https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43605
- **Electing costs the same allowances.** An Overseas Workday Relief election costs the personal allowance, the capital gains annual exempt amount and the other items listed in Section 2, even if no foreign income or gain is claimed. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000
- **Recordkeeping.** Keep a day-by-day record of where the duties were performed, with travel evidence. The pages read for this Guide do not set a format for that record.

**Overseas Workday Relief financial limit, per qualifying year**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600 |
| Cash cap. The relief is the lower of this and the percentage below | GBP 300,000 | EIM43600: "30% of the relevant qualifying employment income for the qualifying year arising out of the employment(s) to which the claim relates and which is charged to tax, or £300,000." |
| Percentage cap, taken on the relevant qualifying employment income for the qualifying year | 30% | EIM43600: "will be the lower of : 30% of the relevant qualifying employment income" |

## Inheritance tax: long-term UK residence

From 6 April 2025 the domicile and deemed domicile rules were replaced for inheritance tax by long-term UK residence. An individual is a long-term UK resident in a tax year if they are tax resident in the UK for either the previous 10 consecutive years or a total of 10 years or more within the previous 20 years, and then their non-UK assets can be in scope of inheritance tax on a transfer or on death. Long-term UK residence can be kept for up to 10 tax years after leaving the UK, and for a shorter tail where there were fewer years of residence: HMRC's own examples are 10 to 13 years of residence giving 3 years after leaving, 14 years giving 4 years, and 15 years giving 5 years. Returning after 10 consecutive years of non-residence resets the test. HMRC states that inheritance tax will be charged on any overseas assets in a trust the individual set up or added to, even when they were not a long-term UK resident at that time. There is no inheritance tax on death on trust assets that were placed in the trust while the individual was non-UK domiciled and that were overseas on 30 October 2024 and overseas at death or when the individual's rights to the trust ended. An individual who did not have UK domicile or deemed domicile on 30 October 2024, is non-resident for 2025 to 2026 and does not return is not a long-term UK resident. One who had deemed domicile on 30 October 2024 and meets the same two conditions stops being a long-term UK resident after 3 years of non-residence. Inheritance tax is a refer case in this Guide. https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident

## The method, step by step

1. Settle UK residence for each tax year under the statutory residence test first; nothing below works without it. Residence for the regime is determined by that test. See `uk-statutory-residence-test`. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000
2. Test the qualifying new resident conditions in Section 2 for the year in question, including the 10 consecutive tax years of non-residence and the position in the 4-year window. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000
3. Weigh the claim. Compare the tax saved on the foreign income and gains against the personal allowance, the capital gains annual exempt amount, the other allowances and the foreign loss relief that the claim gives up for that year. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000
4. Make the claim on the Self Assessment return for that year, source by source and quantified, by the anniversary of 31 January following the end of the tax year. Repeat it every year the relief is wanted. See `uk-income-tax-sa100` for the return itself. https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100
5. For pre-6 April 2025 foreign income and gains, decide whether to designate under the temporary repatriation facility on form SA109, and pay the charge in Section 3. https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf
6. On a disposal of a foreign asset held on 5 April 2017, run the rebasing conditions in Schedule 11 to the Finance Act 2025 before computing the gain, and consider whether to elect out. See `uk-capital-gains-sa108`. https://www.legislation.gov.uk/ukpga/2025/8/schedule/11
7. For an employee with non-UK duties, consider the Overseas Workday Relief election and apply the financial limit in Section 5. https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600
8. Check inheritance tax separately against the long-term UK residence test, because the year counts there are different from the income tax ones. https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident

## Ask the client first

- In which tax years were you UK resident over the last 20 years, and when did the current period of residence start? This drives the 4-year window and the inheritance tax test.
- Have you ever claimed the remittance basis, and for which tax years? Both the temporary repatriation facility and rebasing turn on this.
- What foreign income and foreign gains do you expect this year, and are they worth more to you than the personal allowance and the capital gains annual exempt amount you would give up?
- Do you have employment duties performed outside the UK, and who is the employer?
- Do you still hold foreign assets that you held on 5 April 2017, and was any of them situated in the UK at any time between 6 March 2024 and 5 April 2025?
- Are you the settlor or a beneficiary of a non-UK trust, or have you received anything from one?

## When to refuse or refer

- Any non-UK trust: settlor-interested structures, capital payments, matching to trust income and gains, and trust inheritance tax charges. Refer to a UK tax adviser.
- Inheritance tax exposure of any kind, including the tail after leaving the UK, transfers into settlements, and the position of trustees.
- Mixed funds: working out what has actually been remitted from an account holding more than one type of income, capital or year.
- Treaty residence, double taxation agreements and foreign tax credits. A claim under the regime does not change treaty residence, and no foreign tax credit is available against the repatriation facility charge.
- Transfer of assets abroad and settlements legislation cases.
- Domicile questions for tax years before 2025 to 2026, which still decide rebasing and the treatment of old foreign income and gains. Domicile does not decide who can claim the 4-year regime or Overseas Workday Relief: a returning UK national who meets the 10 year non-residence test can claim.
- Valuing an asset at 5 April 2017 for rebasing, and deciding whether to elect out of rebasing.
- Working out the statutory residence test itself, including split years. See `uk-statutory-residence-test`.
- Business investment relief, exempt property and other pre-6 April 2025 remittance history.

## Section 6: Sources

- Check if you can claim the 4-year foreign income and gains regime: https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime
- Qualifying new resident: https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000
- Making a claim: https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100
- Claim time limits: https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42300
- Effects of a claim on allowances and losses: https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000
- Helpsheet HS264, remittance of pre-6 April 2025 foreign income and gains and the temporary repatriation facility: https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf
- Helpsheet HS211, employment, residence and domicile issues: https://www.gov.uk/government/publications/employment-residence-and-domicile-issues-hs211-self-assessment-helpsheet/hs211-employment-residence-and-domicile-issues-2026
- Overseas Workday Relief financial limit: https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600
- Overseas Workday Relief eligibility: https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43560
- Overseas Workday Relief transitional provisions: https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43605
- Temporary repatriation facility, designation time limits: https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320
- Temporary repatriation facility, the TRF charge: https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400
- Remittance basis charge, history: https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210
- Rebasing of assets, Schedule 11 to the Finance Act 2025: https://www.legislation.gov.uk/ukpga/2025/8/schedule/11
- Deemed domicile, section 835BA of the Income Tax Act 2007: https://www.legislation.gov.uk/ukpga/2007/3/section/835BA
- Inheritance tax if you are a long-term UK resident: https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident
- Policy paper, reforming the taxation of non-UK domiciled individuals, published 30 October 2024: https://www.gov.uk/government/publications/tax-changes-for-non-uk-domiciled-individuals/reforming-the-taxation-of-non-uk-domiciled-individuals

> **Working paper only.** This Guide states the rules as the official pages print them. Trusts, inheritance tax, mixed funds and treaty questions are outside it. Engage a UK tax adviser for any individual relying on the 4-year regime, for any designation under the temporary repatriation facility, and before any disposal where rebasing may apply.

> Contributed by OpenAccountants.

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
