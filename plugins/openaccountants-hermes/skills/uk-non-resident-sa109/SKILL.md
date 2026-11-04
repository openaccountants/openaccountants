---
name: uk-non-resident-sa109
description: "UK income tax and capital gains tax for individuals who are not UK resident but have UK income or sell UK land, for tax year 2026/27 (6 April 2026 to 5 April 2027) and 2025/26 returns due by 31 January 2027. Covers what a non-resident is taxed on, the default rates, the limit on liability for disregarded income (ITA 2007 s.811), who can claim a Personal Allowance, the SA109 pages, the Non-resident Landlord Scheme and NRL1, non-resident CGT on UK property with 2015 and 2019 rebasing and the 60-day return, UK work days and treaty relief, deadlines and penalties. Trigger phrases: non-resident, non-resident landlord, NRL1, SA109, live abroad UK rental, expat selling UK flat, UK income while living abroad, disregarded income, 60-day return non-resident. Out of scope: the residence test itself (uk-statutory-residence-test), the FIG regime (uk-non-dom), relocation plans (uk-to-uae-relocation-tax, uk-to-italy-flat-tax-relocation)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uk-non-resident-sa109"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# UK non-residents with UK income (SA109)

Tax year 2026/27 (6 April 2026 to 5 April 2027) is the year in force. The returns being filed now are for 2025/26. Both years use the same rates for non-residents, so one set of figures serves both unless a row says otherwise.

This skill is the cross-border hub for the UK pack. It holds the non-resident method. It links out for everything else:

- Whether someone is resident at all, split years and temporary non-residence: `uk-statutory-residence-test`.
- The FIG regime for new arrivals and the old remittance basis: `uk-non-dom`.
- The rental computation itself (expenses, finance costs, box map): `uk-rental-sa105`.
- CGT computation, reliefs and rates in general: `uk-capital-gains-sa108`.
- The standard income tax computation: `uk-income-tax-sa100`.
- UK dividends in general: `uk-dividends`.
- National Insurance when a non-resident works in the UK: `uk-national-insurance`.
- Planned moves out: `uk-to-uae-relocation-tax`, `uk-to-italy-flat-tax-relocation`.

## Who this applies to

- **Individuals who are not UK resident for the whole tax year** under the statutory residence test (FA 2013 Sch 45). The test, the day counts and the ties are in `uk-statutory-residence-test`. Do not restate them here.
- **Split years are different.** A person in a split year is UK resident for the year. The overseas part changes how some income is charged, but the s.811 limit below "only applies when an individual has been non-resident for the entire tax year. It does not apply, therefore, in the overseas part of a split year" (HMRC SAIM1170). HMRC's PAYE manual says s.810 "does not apply in the tax year of arrival in the UK or departure from the UK" (PAYE93066).
- **Scottish and Welsh taxpayer status does not apply to a non-resident.** Both definitions start with "resident in the UK for income tax purposes" (Scotland Act 1998 s.80D(1)(a); Government of Wales Act 2006 s.116E(1)(a)). A non-resident's non-savings income is charged at the UK "default" rates instead (ITA 2007 s.11C). In a split year the person is UK resident, so Scottish or Welsh status can apply.
- **Non-resident landlords for the NRL scheme** are a different population: people whose "usual place of abode" is outside the UK (ITA 2007 s.971(2); SI 1995/2902 reg 2). GOV.UK (Tax on your UK income if you live abroad: rent) says "If you live abroad for 6 months or more per year, you're classed as a 'non-resident landlord' ... even if you're a UK resident for tax purposes". Someone can be in the NRL scheme and still be UK resident under the SRT.
- **Companies and trusts** are out of scope. Non-resident companies pay corporation tax on UK property income and on gains from UK land (see `uk-corporation-tax`).

## Rates, bands and thresholds

| Item | Figure | Tax year | Source |
|---|---|---|---|
| Default basic rate (non-resident's non-savings, non-dividend income up to the basic rate limit) | 20% | 2026/27 (also 2025/26) | https://www.legislation.gov.uk/ukpga/2026/11/section/3 ; https://www.legislation.gov.uk/ukpga/2025/8/section/3 |
| Default higher rate | 40% | 2026/27 (also 2025/26) | https://www.legislation.gov.uk/ukpga/2026/11/section/3 |
| Default additional rate | 45% | 2026/27 (also 2025/26) | https://www.legislation.gov.uk/ukpga/2026/11/section/3 |
| Savings basic, higher, additional rates | 20%, 40%, 45% | 2026/27 (also 2025/26) | https://www.legislation.gov.uk/ukpga/2026/11/section/3 |
| Property basic, higher, additional rates (apply to individuals, including non-residents, through ITA s.11CA) | 22%, 42%, 47% | 2027/28 onwards, enacted, not yet in force (s.11CA inserted by FA 2026 s.6, rates set by s.7) | https://www.legislation.gov.uk/ukpga/2026/11/section/6 ; https://www.legislation.gov.uk/ukpga/2026/11/section/7 |
| Dividend ordinary, upper, additional rates | 10.75%, 35.75%, 39.35% (2025/26: 8.75%, 33.75%, 39.35%) | 2026/27 | https://www.legislation.gov.uk/ukpga/2026/11/section/4 |
| Basic rate band on the HS300 limit working sheet | GBP 37,700, then 40% on the next GBP 87,440, 45% above | 2025/26 working sheet; the limits are frozen to 2030/31 (FA 2026 s.10) | https://assets.publishing.service.gov.uk/media/69bbb455bfd6895605dad865/HS300-WS-2026.pdf |
| Personal Allowance, if the claimant qualifies under ITA s.56 | GBP 12,570 | 2026/27 | https://www.gov.uk/income-tax-rates |
| Personal Savings Allowance (no residence condition in ITA s.12B) | GBP 1,000 basic rate; GBP 500 higher rate; nil additional rate | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/12B |
| NRL scheme deduction by agent or tenant | Basic rate (20%) on rent less deductible expenses paid | Each quarter | https://www.gov.uk/guidance/paying-tax-on-rent-to-landlords-abroad ; https://www.legislation.gov.uk/uksi/1995/2902/regulation/9 |
| NRL scheme: tenant with no agent must deduct if rent is | Over GBP 100 a week | Standing | https://www.gov.uk/guidance/paying-tax-on-rent-to-landlords-abroad |
| CGT rates on UK land (residential and non-residential) | 18% within the basic rate band, 24% above | Disposals from 6 April 2026 (same main rates since 30 October 2024) | https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances (rates table in `uk-capital-gains-sa108`) |
| CGT annual exempt amount (non-residents get it "in most cases") | GBP 3,000 | 2026/27 and 2025/26 | https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances |
| Rebasing date, residential UK property | Market value at 5 April 2015 | Disposals by non-residents of property held then | https://www.legislation.gov.uk/ukpga/1992/12/schedule/4AA |
| Rebasing date, non-residential land and indirect disposals | Market value at 5 April 2019 | Disposals by non-residents of assets held then | https://www.legislation.gov.uk/ukpga/1992/12/schedule/4AA |
| Indirect disposal threshold | Asset deriving at least 75% of its value from UK land, with at least a 25% interest | Since 6 April 2019 | https://www.legislation.gov.uk/ukpga/1992/12/section/1A ; https://www.gov.uk/guidance/capital-gains-tax-for-non-residents-uk-residential-property |
| UK property CGT return and payment | Within 60 days of completion | Completions on or after 27 October 2021 | https://www.gov.uk/guidance/capital-gains-tax-for-non-residents-uk-residential-property |
| Temporary non-residence window | 5 years or less, after sole UK residence in at least 4 of the 7 prior tax years | Standing | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |

## The taxable base

**What a non-resident is taxed on.** Only UK-source income. Savings and investment income of a non-resident is taxed "only on income arising from a UK source" (HMRC SAIM1170, citing ITTOIA 2005 s.368(2)). Employment income is taxed for duties performed in the UK (ITEPA 2003 s.27). UK property income is always within the charge. Gains are taxed only on UK land, on indirect disposals of UK property-rich entities, and on assets of a UK branch or agency (TCGA 1992 s.1A(3)).

**The limit on liability (ITA 2007 s.811).** For a non-resident individual, income tax for the year cannot exceed A + B (s.811(3)):

- **A** is the tax deducted at source, or treated as deducted, from "disregarded income" (s.811(4)).
- **B** is the tax that would be due if the disregarded income were left out **and** no Personal Allowance, married couple's reduction or treaty relief given through s.56(3) or a treaty were allowed (s.811(5) and (6)).

Disregarded income (s.813, s.814 and s.825) is:

- UK bank and building society interest, and other interest within ITTOIA Part 4 Chapter 2;
- dividends from UK resident companies;
- purchased life annuity payments, deeply discounted securities, transactions in deposits, unauthorised unit trust income;
- disregarded annual payments (s.826);
- disregarded transaction income (s.814: income from transactions carried out through a UK broker or investment manager where the independent broker or investment manager conditions are met);
- the UK State Pension and other ITEPA s.577 social security pensions, and the pension types listed in s.813(3);
- taxable social security benefits in ITEPA s.660 Table A, other than income support and jobseeker's allowance.

Income is not disregarded where the non-resident has a UK representative for it (s.813(2)). Property income, employment income, self-employment profits and most private pensions are never disregarded. Pensions under registered pension schemes are disregarded only where the scheme was a retirement annuity contract immediately before 6 April 2006 (s.813(4)). The limit is a ceiling, not a choice of method: work out the normal liability and the s.811 figure and pay the lower. HMRC's own staff "do two calculations for the year ... to determine the most beneficial one" (PAYE93066). On the return, HS300 and its working sheet do the comparison, and box 28 of the working sheet replaces box A297 of the Tax Calculation Summary working sheet "if smaller".

Since April 2016 banks do not deduct tax from interest ("Income Tax is no longer automatically taken from interest on savings and investments", GOV.UK). So A is usually nil, and the s.811 limit means a non-resident pays nothing on UK bank interest, dividends or the State Pension, at the cost of losing the Personal Allowance against everything else.

**Who gets a Personal Allowance.** A non-resident gets the Personal Allowance only if, at any time in the tax year, they meet one of the conditions in ITA 2007 s.56(3):

- a UK national or a national of an EEA state;
- resident in the Isle of Man or the Channel Islands;
- previously UK resident and now abroad for their own health or that of a family member living with them;
- in, or formerly in, Crown service; or employed in the service of a territory under His Majesty's protection; or employed by a missionary society;
- the widow, widower or surviving civil partner of someone in Crown service.

A treaty can also give the allowance. The SA109 notes list the treaty cases for box 15 (for example nationals and residents of Australia, Canada, India, Japan, New Zealand, South Africa or Switzerland, and residents of Ireland, the Netherlands or Portugal). The same notes exclude two cases where the income is only dividends, interest or royalties: a resident of Kenya or Mauritius, and a resident who is not a citizen of Belgium, Luxembourg, Portugal or Switzerland. A treaty claim needs a certificate of residence from the overseas authority. The allowance for 2026/27 is GBP 12,570, tapered above GBP 100,000 of adjusted net income as for residents. The claim is made each year on the return, or on form R43 for someone outside Self Assessment.

**Employment duties in the UK.** A non-resident employee is taxed on earnings for UK duties (ITEPA s.27). A treaty's dependent personal services article (Article 15 in the OECD model) exempts that pay only if all three conditions hold:

- the employee is present in the UK for not more than 183 days in the treaty's reference period;
- the pay is paid by, or on behalf of, an employer who is not UK resident;
- the pay is not borne by a UK permanent establishment.

HMRC will not accept a claim where a UK company "for practical purposes functions as his employer" and bears the cost through a recharge (DT1922). Whether the 183 days count per tax year or per 12-month period depends on the treaty. Read the treaty article. For employers, HMRC's short term business visitor arrangement lets PAYE be disregarded for treaty-resident visitors "expected to stay in the UK for 183 days or less in any twelve month period", with extra conditions at 60 days or more (PAYE82000).

**Gains on UK land.** For land held at the rebasing date, the default is rebasing (TCGA Sch 4AA):

- residential property held throughout from 6 April 2015 that was fully residential until 5 April 2019: market value at 5 April 2015 (para 7);
- non-residential land, indirect disposals, and property that was not fully residential before 6 April 2019: market value at 5 April 2019 (para 3).

Two elections are available against the default:

- **Retrospective computation** over the whole ownership period (paras 4 and 8). A loss on an indirect disposal computed this way is not allowable.
- **Straight-line time apportionment**, residential Part 3 cases only (para 9). The taxable share is the gain multiplied by the days from 6 April 2015 to the disposal, divided by the days from acquisition (or 31 March 1982 if later) to the disposal.

Mixed-use property splits: the residential part rebases to 2015, the rest to 2019 (HMRC guidance). Private residence relief can apply to a former home (see `uk-capital-gains-sa108`). The rate depends on the person's taxable UK income: "Add together all your taxable UK income and use this figure to work out your Capital Gains Tax rate" (HMRC). Losses on UK land offset UK land gains of the same year and carry forward against later UK land gains.

**Temporary non-residence.** Someone who returns within 5 years after at least 4 of the prior 7 years of sole UK residence is taxed in the year of return on gains (TCGA s.1M) and on some income (for example distributions from close companies and certain pension lump sums) received while away. "Nothing in any double taxation arrangements prevents a charge" under s.1M (s.1M(4)). The tests are in `uk-statutory-residence-test`.

## Deadlines and filing

- **The SA109 pages** ("Residence and foreign income and gains (FIG) regime etc") go with the SA100. Boxes 1 to 14 cover residence status and the split year. Boxes 15 to 17 cover the Personal Allowance claim and nationality codes. Boxes 18 to 22 cover other residence and treaty relief claims (HS302 for treaty residence, HS304 for other treaty provisions). The SA109 notes say the pages must not be sent "as an electronic attachment" to a return filed through HMRC's free online service. File on paper, or through commercial software or an agent.
- **2025/26 returns** (being filed now):
  - register by 5 October 2026 if no return was issued;
  - paper return by 31 October 2026;
  - online return through software by 31 January 2027;
  - pay by 31 January 2027.

  GOV.UK reminds non-resident landlords that the deadline "is earlier if you're sending your return by post (31 October)".
- **2026/27 returns**: the same pattern one year later (31 October 2027 paper, 31 January 2028 online). Confirm on the GOV.UK deadlines page once HMRC publishes them.
- **NRL scheme**:
  - letting agents register on NRL4 and tenants register with HMRC;
  - tax is paid within 30 days of each quarter ending 30 June, 30 September, 31 December and 31 March;
  - by 5 July each year the agent or tenant sends form NRLY to HMRC and gives the landlord certificate NRL6.

  The landlord applies on NRL1 (online or by post) to receive rent gross. HMRC approves it if satisfied the landlord "will follow all your UK tax obligations" and will not approve it if "you're late with your tax returns or payments". Approval does not remove the duty to file a return: "you'll need to declare your income in your Self Assessment tax return" (GOV.UK, Tax on your UK income if you live abroad: rent).
- **UK land disposals**: report every disposal of UK land within 60 days of completion through a Capital Gains Tax on UK property account, "even if you have no tax to pay ... have made a loss ... are registered for Self Assessment". Pay any tax due in the same 60 days. If the person files a Self Assessment return, the gain also goes on the SA108 (boxes 52.1 to 52.5, the non-resident CGT section) with credit for the tax already paid in box 52.4.
- **Treaty claims at source** (for example to receive a UK pension gross) use the country-specific DT form, sent to the tax authority of the country of residence first.

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| SA return late | GBP 100; after 3 months GBP 10 a day up to GBP 900; after 6 months the greater of 5% of the tax due or GBP 300; after 12 months another 5% or GBP 300 | https://www.gov.uk/self-assessment-tax-returns/penalties |
| SA tax paid late | 5% of the tax unpaid at 30 days, 6 months and 12 months | https://www.gov.uk/self-assessment-tax-returns/penalties |
| 60-day UK property return late | FA 2009 Sch 55 paras 3 to 6 apply (table item 2A, returns under FA 2019 Sch 2): GBP 100; GBP 10 a day for up to 90 days after 3 months if HMRC gives notice; then the greater of 5% of the tax or GBP 300 at 6 months and again at 12 months | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 |
| Late registration (failure to notify) | Based on the tax still unpaid at 31 January | https://www.gov.uk/self-assessment-tax-returns/penalties |
| Late payment interest | Bank of England base rate plus 4% (from 6 April 2025). 7.75% from 9 January 2026 on HMRC's page; Bank Rate has stayed at 3.75% since 18 December 2025, so 7.75% is the rate in force at 23 October 2026 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates ; https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp |
| NRL agent or tenant pays late | Interest on late quarterly payments; the agent or tenant is liable for tax it should have deducted | https://www.gov.uk/guidance/paying-tax-on-rent-to-landlords-abroad |

The HMRC interest page was last updated on 23 December 2025. The rate moves with Bank Rate, so check both pages on the day before quoting interest to a client.

## Cross-border points

- **Treaty tie-breaker.** A person resident in the UK under the SRT and also resident elsewhere may be treaty non-resident. That changes treaty relief, not SRT status. It also matters for temporary non-residence, since "sole UK residence" excludes any time as treaty non-resident (FA 2013 Sch 45 para 112). SA109 boxes 18 to 21 and HS302 handle the claim.
- **Relief for UK tax in the country of residence.** The UK taxes the UK-source income. The country of residence usually gives the credit or exemption. GOV.UK: "If the tax rates in the 2 countries are different, you'll pay the higher rate of tax."
- **Treaties and UK land.** HMRC says many treaties decide taxing rights on UK land disposals and a return is needed to claim treaty relief. Read the gains article of the relevant treaty. Most preserve the UK's right over immovable property in the UK.
- **Rates beyond 2026/27.** The NRL deduction rate for 2027/28 and the regulations that change it are covered in `uk-rental-sa105`. From 2027/28 the property rates of 22%, 42% and 47% apply to individuals' property income, and the savings rates rise to 22%, 42% and 47% (FA 2026 ss.5 and 7). Under s.811, UK interest of a non-resident stays disregarded. Under the normal computation it would be taxed at the new savings rates.
- **Social security.** A non-resident working in the UK can still owe Class 1 NIC; this depends on the social security agreement or the UK-EU Trade and Cooperation Agreement protocol, not the tax treaty. See `uk-national-insurance`.
- **Companies.** Non-resident companies with UK property income or UK land gains: see `uk-corporation-tax`.

## Worked examples

### Example 1: non-resident landlord, s.811 limit against full liability (2026/27)

Ana lives in Portugal all year and is not UK resident under the SRT. She lets a London flat through a UK agent. Net rent after allowable expenses, all paid through the agent, is GBP 18,000. She also has GBP 2,000 of UK bank interest, paid gross. She has no NRL1 approval, so the agent deducted 20% of the net rent: GBP 3,600.

**If she can claim a Personal Allowance** (for example as an EEA national under s.56(3)(za)):

- Normal liability: rent GBP 18,000 less the allowance GBP 12,570 leaves GBP 5,430 at the 20% default basic rate, which is GBP 1,086.
- Interest: her non-savings taxable income is above the GBP 5,000 starting rate limit, so there is no starting rate band. The first GBP 1,000 is covered by the Personal Savings Allowance. The other GBP 1,000 is taxed at 20%, which is GBP 200.
- Normal liability is GBP 1,286. The s.811 limit (tax on the rent with no allowance, interest left out) is GBP 3,600.
- She pays the lower, GBP 1,286. With GBP 3,600 already deducted, she is due a repayment of GBP 2,314.

**If she cannot claim an allowance** (for example a national of a country with no s.56 or treaty entitlement):

- Normal liability is GBP 18,000 at 20% (GBP 3,600) plus GBP 1,000 of interest at 20% (GBP 200), so GBP 3,800.
- The s.811 limit is still GBP 3,600, because the interest is disregarded and nothing was deducted from it.
- She pays GBP 3,600, which is covered exactly by the NRL deduction.

```oa-check
name: Non-resident landlord, net rent 18,000 and interest 2,000, s.811 limit against full liability (2026/27)
inputs:
  rent: 18000
  interest: 2000
  personal_allowance: 12570
  psa: 1000
  nrl_deducted: 3600
steps:
  - with_pa_rent_tax: (rent - personal_allowance) * 0.20
  - with_pa_interest_tax: max(interest - psa, 0) * 0.20
  - with_pa_full: with_pa_rent_tax + with_pa_interest_tax
  - s811_limit: rent * 0.20 + 0
  - with_pa_due: min(with_pa_full, s811_limit)
  - with_pa_repayment: nrl_deducted - with_pa_due
  - no_pa_full: rent * 0.20 + max(interest - psa, 0) * 0.20
  - no_pa_due: min(no_pa_full, s811_limit)
  - no_pa_balance: no_pa_due - nrl_deducted
expected:
  with_pa_full: 1286.00
  s811_limit: 3600.00
  with_pa_due: 1286.00
  with_pa_repayment: 2314.00
  no_pa_full: 3800.00
  no_pa_due: 3600.00
  no_pa_balance: 0.00
```

The `+ 0` in `s811_limit` is amount A: no tax was deducted from the interest. Both rent figures fall inside the GBP 37,700 basic rate band, so 20% is the only rate. Ana files SA100 with SA105 and SA109. On SA109 she puts X in box 1 and, if she claims the allowance, in box 16 with her nationality code in box 17. The GBP 3,600 goes in SA105 box 21.

### Example 2: non-resident sells a UK buy-to-let flat bought before April 2015 (2026/27)

Ben has lived in Dubai since 2012 and is not UK resident. He has no UK income. He bought a UK flat on 1 July 2010 for GBP 200,000 including costs and let it throughout. He never lived in it. Its market value at 5 April 2015 was GBP 260,000. He exchanged contracts on 2 September 2026 and completed on 30 September 2026. The sale price was GBP 340,000, with GBP 5,000 of selling costs.

**The three ways to compute the gain:**

- **Whole gain:** net proceeds GBP 335,000 less cost GBP 200,000 is GBP 135,000.
- **Rebasing (the default):** GBP 335,000 less GBP 260,000 is GBP 75,000. The GBP 60,000 of growth before 6 April 2015 is outside the charge.
- **Time apportionment:** the ownership period from 1 July 2010 to 2 September 2026 is 5,908 days, and 4,168 of them fall from 6 April 2015. GBP 135,000 × 4,168 / 5,908 is GBP 95,240.35.

He keeps the rebasing default, the lowest gain. Less the GBP 3,000 annual exempt amount, the taxable gain is GBP 72,000. With no UK income, the whole GBP 37,700 basic rate band is free. GBP 37,700 at 18% plus GBP 34,300 at 24% is GBP 15,018. He reports the disposal and pays within 60 days of completion, by 29 November 2026. The disposal date for the day count is the exchange date. The 60 days run from completion.

```oa-check
name: Non-resident sells UK flat, rebased gain against time apportionment (2026/27)
inputs:
  proceeds: 340000
  selling_costs: 5000
  cost: 200000
  mv_2015: 260000
  days_total: 5908
  days_post: 4168
  aea: 3000
  basic_band: 37700
  uk_taxable_income: 0
steps:
  - net_proceeds: proceeds - selling_costs
  - whole_gain: net_proceeds - cost
  - rebased_gain: net_proceeds - mv_2015
  - pre_2015_part: whole_gain - rebased_gain
  - time_apportioned: round(whole_gain * days_post / days_total, 2)
  - chosen_gain: min(rebased_gain, time_apportioned, whole_gain)
  - taxable_gain: chosen_gain - aea
  - band_left: max(basic_band - uk_taxable_income, 0)
  - at_18: min(taxable_gain, band_left) * 0.18
  - at_24: max(taxable_gain - band_left, 0) * 0.24
  - cgt: at_18 + at_24
expected:
  whole_gain: 135000.00
  rebased_gain: 75000.00
  pre_2015_part: 60000.00
  time_apportioned: 95240.35
  chosen_gain: 75000.00
  taxable_gain: 72000.00
  cgt: 15018.00
```

If Ben had UK income, his taxable UK income would use up the basic rate band first and more of the gain would fall at 24%. If he returns to the UK within 5 years of leaving, see temporary non-residence. He left in 2012 and has been away more than 5 years, so it does not apply here.

## Ask the client first

1. Were you non-resident for the **whole** tax year, or is it a split year? The s.811 limit and the default rates apply only to a full non-resident year. The SRT result comes from `uk-statutory-residence-test`.
2. What is your nationality, where are you resident, and have you ever been in Crown service? This decides the Personal Allowance under s.56 or a treaty, and so whether the s.811 limit or the normal computation is lower.
3. What UK income do you have, by type? Rent, interest, dividends, State Pension, private or workplace pensions, UK employment days. Has any UK tax been deducted, including by an NRL agent or tenant?
4. Do you have NRL1 approval to receive rent gross, and who collects the rent?
5. For a UK property sale: dates of purchase, exchange and completion; cost; any improvement costs and their dates; the value at 5 April 2015 (residential) or 5 April 2019 (other land); whether you ever lived there.
6. When did you leave the UK, and do you plan to come back within 5 years?

## Sources

| Source | URL | Read on |
|---|---|---|
| ITA 2007 s.811 (limit on liability of non-UK residents) | https://www.legislation.gov.uk/ukpga/2007/3/section/811 | 2026-10-23 |
| ITA 2007 s.812 (case where limit does not apply) | https://www.legislation.gov.uk/ukpga/2007/3/section/812 | 2026-10-23 |
| ITA 2007 s.813 (meaning of disregarded income) | https://www.legislation.gov.uk/ukpga/2007/3/section/813 | 2026-10-23 |
| ITA 2007 s.814 (disregarded transaction income) | https://www.legislation.gov.uk/ukpga/2007/3/section/814 | 2026-10-23 |
| ITA 2007 s.825 (disregarded savings and investment income) | https://www.legislation.gov.uk/ukpga/2007/3/section/825 | 2026-10-23 |
| ITA 2007 s.56 (residence etc of claimants for allowances) | https://www.legislation.gov.uk/ukpga/2007/3/section/56 | 2026-10-23 |
| ITA 2007 s.11C (default rates for non-UK resident individuals) | https://www.legislation.gov.uk/ukpga/2007/3/section/11C | 2026-10-23 |
| ITA 2007 s.12B (savings allowance) | https://www.legislation.gov.uk/ukpga/2007/3/section/12B | 2026-10-23 |
| ITA 2007 s.971 (non-resident landlords) | https://www.legislation.gov.uk/ukpga/2007/3/section/971 | 2026-10-23 |
| Finance Act 2026 s.3 (default and savings rates 2026-27) | https://www.legislation.gov.uk/ukpga/2026/11/section/3 | 2026-10-23 |
| Finance Act 2026 s.2 (main rates 2026-27) | https://www.legislation.gov.uk/ukpga/2026/11/section/2 | 2026-10-23 |
| Finance Act 2026 ss.6 and 7 (property rates from 2027-28) | https://www.legislation.gov.uk/ukpga/2026/11/section/6 | 2026-10-23 |
| Finance Act 2025 s.3 (default and savings rates 2025-26) | https://www.legislation.gov.uk/ukpga/2025/8/section/3 | 2026-10-23 |
| ITEPA 2003 s.27 (UK-based earnings of non-residents) | https://www.legislation.gov.uk/ukpga/2003/1/section/27 | 2026-10-23 |
| TCGA 1992 s.1A (territorial scope) | https://www.legislation.gov.uk/ukpga/1992/12/section/1A | 2026-10-23 |
| TCGA 1992 s.1M (temporary non-residents) | https://www.legislation.gov.uk/ukpga/1992/12/section/1M | 2026-10-23 |
| TCGA 1992 Sch 4AA (rebasing for non-residents) | https://www.legislation.gov.uk/ukpga/1992/12/schedule/4AA | 2026-10-23 |
| FA 2013 Sch 45 (statutory residence test, temporary non-residence) | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 | 2026-10-23 |
| FA 2009 Sch 55 (late filing penalties) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-10-23 |
| Scotland Act 1998 s.80D (Scottish taxpayers) | https://www.legislation.gov.uk/ukpga/1998/46/section/80D | 2026-10-23 |
| Government of Wales Act 2006 s.116E (Welsh taxpayers) | https://www.legislation.gov.uk/ukpga/2006/32/section/116E | 2026-10-23 |
| Taxation of Income from Land (Non-residents) Regulations 1995, SI 1995/2902, regs 2, 8, 9, 17 | https://www.legislation.gov.uk/uksi/1995/2902/regulation/9 | 2026-10-23 |
| HMRC, SA109 2026 form and notes | https://www.gov.uk/government/publications/self-assessment-residence-remittance-basis-etc-sa109 | 2026-10-23 |
| HMRC, HS300 Non-residents and investment income (2026) and working sheet | https://www.gov.uk/government/publications/non-residents-and-investment-income-hs300-self-assessment-helpsheet/hs300-non-residents-and-investment-income-2026 | 2026-10-23 |
| HMRC SAIM1170 (savings and investment income: non-residents) | https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim1170 | 2026-10-23 |
| HMRC PAYE93066 (s.810 and s.811 cases) | https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye93066 | 2026-10-23 |
| HMRC PAYE82000 (short term business visitors) | https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye82000 | 2026-10-23 |
| HMRC DT1922 (non-residents: employment, Article 15(2)) | https://www.gov.uk/hmrc-internal-manuals/double-taxation-relief/dt1922 | 2026-10-23 |
| GOV.UK, Tax on your UK income if you live abroad | https://www.gov.uk/tax-uk-income-live-abroad | 2026-10-23 |
| GOV.UK, Paying tax on rent to landlords abroad | https://www.gov.uk/guidance/paying-tax-on-rent-to-landlords-abroad | 2026-10-23 |
| GOV.UK, Apply as an individual to receive UK rental income without UK tax deducted (NRL1) | https://www.gov.uk/guidance/apply-as-an-individual-to-receive-uk-rental-income-without-uk-tax-deducted | 2026-10-23 |
| GOV.UK, Tell HMRC about CGT on UK property or land if you're not a UK resident | https://www.gov.uk/guidance/capital-gains-tax-for-non-residents-uk-residential-property | 2026-10-23 |
| GOV.UK, Work out your tax if you're a non-resident selling UK property or land | https://www.gov.uk/guidance/capital-gains-tax-for-non-residents-calculating-taxable-gain-or-loss | 2026-10-23 |
| GOV.UK, Capital Gains Tax rates and allowances | https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances | 2026-10-23 |
| GOV.UK, Income Tax rates and Personal Allowances | https://www.gov.uk/income-tax-rates | 2026-10-23 |
| GOV.UK, Self Assessment tax returns: deadlines and penalties | https://www.gov.uk/self-assessment-tax-returns | 2026-10-23 |
| Bank of England, Bank Rate history | https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp | 2026-10-23 |
| GOV.UK, Tax on your UK income if you live abroad: rent | https://www.gov.uk/tax-uk-income-live-abroad/rent | 2026-10-23 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-23 |

Not yet confirmed: the 2026/27 SA109 notes and HS300 working sheet (only the 2025/26 editions, published in 2026, were available); the legislation.gov.uk text of SI 1995/2902 is shown in its original form, so later amendments to the regulation wording were not checked (the current HMRC guidance was used for the 20% rate and the GBP 100 a week test).

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uk-non-resident-sa109` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uk-non-resident-sa109. If neither is available, confirm every figure against the official source pages cited above before relying on it.
