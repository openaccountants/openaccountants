---
name: uk-non-dom
description: "Use this skill for any question about UK non-dom rules. Trigger on: \"UK non-dom\", \"UK non-domiciled\", \"remittance basis UK\", \"FIG regime UK\", \"foreign income gains UK new resident\", \"UK domicile rules\", \"UK non-dom reform 2025\", \"arising basis UK\", \"4-year exemption UK tax\", \"UK overseas workday relief\", \"UK non-dom abolished\". Covers the new 4-year FIG regime (from April 2025), transitional provisions for existing non-doms, and remittance basis overview."
version: 1.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-26
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - uk-income-tax-sa100
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK non-dom rules after April 2025: the 4-year FIG regime, the TRF, rebasing, OWR and IHT

## Scope

This Guide covers how the UK taxes the foreign income and gains (FIG) of people who used to rely on the remittance basis, and of people who have recently arrived in the UK. The primary year is the UK tax year 2026/27 (6 April 2026 to 5 April 2027), which HMRC writes as "2026 to 2027" or "2026-27". A short dated section covers the 2025/26 returns being filed now, and a separate dated section covers people with remittance basis history before 6 April 2025.

- **What ended.** "On 6 April 2025 the 4-year foreign income and gains regime replaced the remittance basis." Domicile is no longer the connecting factor for income tax and capital gains tax. From that date "all UK residents are taxed on the arising basis of assessment on their worldwide income and gains", and "the 2024 to 2025 tax year was the last year for which the remittance basis could be claimed, or could apply automatically" ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf), updated 6 April 2026).
- **What replaced it (Finance Act 2025 and Finance Act 2026 amendments):**
  1. the 4-year FIG regime for qualifying new residents (ITTOIA 2005 [s845A](https://www.legislation.gov.uk/ukpga/2005/5/section/845A) and [s845B](https://www.legislation.gov.uk/ukpga/2005/5/section/845B));
  2. the temporary repatriation facility (TRF) for former remittance basis users' pre-6 April 2025 FIG;
  3. rebasing to 5 April 2017 for certain former remittance basis users ([Finance Act 2025 Schedule 11](https://www.legislation.gov.uk/ukpga/2025/8/schedule/11));
  4. a new Overseas Workday Relief (OWR) tied to the FIG regime;
  5. residence-based inheritance tax: the long-term UK resident test ([IHTA 1984 s6A](https://www.legislation.gov.uk/ukpga/1984/51/section/6A)).
- **Who this Guide is for.** Individuals who are UK resident under the statutory residence test (SRT) in 2026/27, or who were resident in earlier years and used the remittance basis. It covers income tax and capital gains tax in full and inheritance tax in outline only.
- **What it does not cover.** Working out residence itself (see `uk-statutory-residence-test`, which carries the same FIG look-back rules), non-UK trusts, the settlements and transfer of assets abroad rules, mixed fund identification, treaty relief, and the IHT charge itself. These are refer cases below.
- **Every step depends on residence.** HMRC: "UK residence is determined by the statutory residence test (SRT) for tax years 2013-14 onwards" ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000)). Settle residence for every year in the look-back before anything else.

## Ask the client first

- **Residence history.** For each tax year back to 2006/07 at least: were you UK resident under the SRT? Split years and years when a treaty made you resident elsewhere still count as UK resident years for the FIG test. When did your current period of UK residence begin?
- **The first qualifying year.** In which tax year did you first become UK resident after 10 or more consecutive non-resident years? That year, not 2026/27, fixes the 4-year window and the 10-year look-back.
- **Parliament.** Were you a member of the House of Commons or House of Lords at any time in the claim year or in the 10 years before the first qualifying year? Members are deemed UK resident and cannot be qualifying new residents.
- **Age.** For a child: were they at least 10 years old on 6 April of the year?
- **Remittance basis history.** Did you claim the remittance basis, or have it apply automatically, in any year up to 2024/25? Which years? Did you pay the remittance basis charge? Were you ever domiciled or deemed domiciled in the UK before 2025/26?
- **Pre-6 April 2025 FIG still offshore.** How much unremitted foreign income and gains from remittance basis years do you hold, in which accounts or assets, and do you plan to bring any to the UK? Do you have records that show which year and type each amount came from?
- **Foreign income and gains in 2026/27.** What foreign income (by source) and foreign gains (by disposal) do you expect? Do you also have foreign losses, overseas property finance costs, or pension contributions that depend on UK earnings?
- **Employment.** Do you work for an employer both in and outside the UK? What share of your workdays are overseas? Did you use OWR on the remittance basis in 2022/23, 2023/24 or 2024/25? Do you receive bonuses that relate to earlier years?
- **Assets held on 5 April 2017.** Do you still own foreign assets you held on that date? Was any of them in the UK at any time from 6 March 2024 to 5 April 2025, and if so why?
- **Trusts.** Are you a settlor or beneficiary of a non-UK trust, or have you received a capital payment or benefit from one?
- **Inheritance tax.** How many of the last 20 tax years were you UK resident? Did you have UK domicile or deemed domicile on 30 October 2024? Are you planning to leave the UK?

## The method, step by step

1. **Fix residence for every relevant year.** Use the SRT for 2013/14 onward. For the FIG regime and OWR, treaty non-residence and split year treatment are ignored: "Any year in which split year treatment applies will be a full year of UK residence for the purposes of the residence criteria" ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000)). A look-back reaching 2012/13 or earlier uses the pre-SRT rules; refer it.
2. **Find the first qualifying year.** It is the first year of UK residence after 10 consecutive non-resident tax years, where the person is not a member of either House of Parliament and (from Finance Act 2026) is at least 10 years old at the start of the year ([s845B(1)](https://www.legislation.gov.uk/ukpga/2005/5/section/845B)). The years 2022/23, 2023/24 and 2024/25 count as qualifying years if the test would have been met in them (s845B(3)(c)).
3. **Check 2026/27 is inside the window.** 2026/27 qualifies if it is the first qualifying year, or "one of the next three tax years after a qualifying tax year" and the person is UK resident and not disqualified in 2026/27 (s845B(2)). Unused years do not roll forward. A non-resident year inside the window is lost, but the remaining years can still be used on return.
4. **Decide whether a FIG claim is worth it.** Weigh the tax saved on qualifying foreign income and gains against everything the claim costs for that year (see "What a claim costs" below). The cost applies even if the claim is small. Compare with simply paying tax on the arising basis with foreign tax credit relief.
5. **Make the claim in the 2026/27 return, source by source, quantified,** by 31 January 2029 ([s845A(5)](https://www.legislation.gov.uk/ukpga/2005/5/section/845A); [RFIG42300](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42300)). Repeat each year the relief is wanted.
6. **For employees, consider OWR** separately. Eligibility follows qualifying new resident status; a FIG claim is not needed. Apply the financial limit and the transitional rules ([EIM43560](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43560)).
7. **For former remittance basis users, deal with old FIG.** Pre-6 April 2025 FIG remitted in 2026/27 is taxed at the usual rates unless designated under the TRF. Decide what to designate for 2026/27 (the last 12% year) and make the election on the SA109 pages by 31 January 2029 ([RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320)).
8. **On any disposal of a foreign asset held on 5 April 2017,** test the rebasing conditions in Schedule 11 before computing the gain, and consider the irrevocable election out.
9. **Check inheritance tax separately** against the long-term UK resident test. Its year counts differ from the FIG test. Refer any IHT computation.
10. **File and keep records:** SA100 plus SA109 (residence and FIG regime pages), SA106 for foreign income, and a record of designated TRF capital and workday evidence.

## The rules and figures for 2026/27

### 1. The 4-year FIG regime (qualifying new residents)

**Who qualifies** ([s845B](https://www.legislation.gov.uk/ukpga/2005/5/section/845B); [RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000); [HMRC guidance](https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime)):

- **First year (s845B(1)).** All of: UK resident for the year; not disqualified (not a member of the House of Commons or House of Lords for any part of the year); "for each of the 10 tax years before that tax year, the individual was not UK resident"; and "at least 10 years old at the commencement of that tax year". The age condition was inserted by Finance Act 2026 on 18 March 2026; check commencement if a young child's 2025/26 position matters.
- **Next three years (s845B(2)).** UK resident, not disqualified, and the year "is one of the next three tax years after a qualifying tax year". The 10 non-resident years are counted back from the first qualifying year, not from the year of claim. This matches the `uk-statutory-residence-test` Guide.
- **Arrivals before the reform (s845B(3)(c)).** 2022/23, 2023/24 or 2024/25 is a qualifying tax year if the test would have been met in it. No claim can be made for those years themselves. HMRC: "you'll only have one year of eligibility — the tax year 2025 to 2026" for someone whose residence began in 2022/23.
- **Look-back for 2026/27, by first qualifying year:** arrival in 2026/27 needs non-residence 2016/17 to 2025/26; arrival in 2025/26 needs 2015/16 to 2024/25; arrival in 2024/25 needs 2014/15 to 2023/24; arrival in 2023/24 needs 2013/14 to 2022/23. An arrival in 2022/23 has no FIG year left in 2026/27 (its window ended with 2025/26).
- **Nationality and domicile do not matter.** A returning UK national with a UK domicile of origin qualifies if the 10-year test is met ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000), Example 2).
- **Parliament.** Members of either House are deemed UK resident under the Constitutional Reform and Governance Act 2010, so a year as a member breaks the 10-year run even if the SRT says non-resident.
- **Leaving inside the window.** A non-resident year cannot be claimed and is not replaced. HMRC: "You cannot roll any unused years over to a later year." The temporary non-residence rules do not bite on someone leaving within their first 4 years, because they "will not meet the requirement that an individual was UK resident for at least 4 out of the 7 tax years preceding the year of departure" ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000)).

**What can be relieved** ([RFIG45100](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig45100); [HMRC guidance](https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime)):

- Qualifying foreign income under ITTOIA 2005 s845H, which is not "disqualified income" under s845I. It includes profits of a trade carried on wholly outside the UK, profits of an overseas property business, interest such as interest on a foreign bank account, dividends from non-UK resident companies, foreign pension income (except disqualified types), royalties and offshore income gains. Check the manual for the specific source.
- Qualifying foreign gains under TCGA 1992 Schedule D1 (a "foreign gain claim").
- **Not covered:** UK income and gains; relevant foreign earnings and foreign specific employment income (use OWR instead); and any foreign income or gains that arose before 6 April 2025. RFIG45100: qualifying foreign income "can only be income which arises on or after 6 April 2025".

**How the claim works** ([s845A](https://www.legislation.gov.uk/ukpga/2005/5/section/845A); [RFIG42100](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100)):

- A claim "must be made in a return" (s845A(4)). There is "no de minimis or automatic application of the relief without a claim".
- Income and gains must be claimed "on a source-by-source basis" and quantified. "Incorrectly quantifying a claim does not invalidate it", but "not quantifying a claim at all does invalidate the claim". Claiming less than the full amount relieves only the amount claimed.
- The relief is deducted at Step 2 of the income tax calculation (ITA 2007 s23), and since Finance Act 2026 "a deduction for that purpose is to be made only from qualifying foreign income" (s845A(3A), for 2025/26 onward).
- A claim for year one does not carry forward. A year not claimed cannot be used later. There is no cap on the amount relieved.
- Relieved amounts can be brought to the UK at any time without further UK tax.

**Deadline, amendment and late claims** ([RFIG42300](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42300)):

- The claim must be made "before the end of the period of 12 months beginning with 31 January after the end of that tax year" (s845A(5)). For 2026/27 that is **31 January 2029**; for 2025/26 it is 31 January 2028 (HMRC's own example).
- Claims can be amended or withdrawn within the same time limit. If the notice to file was issued after 31 October following the tax year, and the claim was made in time, it can be amended up to 3 months after the date of the notice.
- "There is no provision within the FIG regime legislation that allows Commissioners to exercise their discretion to accept late claims." A late claim can only be allowed under HMRC's general late claims policy.
- A consequential claim after an HMRC assessment is barred where the loss of tax was brought about carelessly or deliberately (s845A(6)).

**What a claim costs** ([RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000); ITTOIA 2005 ss845C to 845G; TCGA 1992 [s1K(6)](https://www.legislation.gov.uk/ukpga/1992/12/section/1K)). A foreign income claim, a foreign gain claim or an OWR election for a year removes, for that year:

- the personal allowance, blind person's allowance, the married couple's and civil partner tax reductions, the transferable tax allowance (marriage allowance), and relief for life insurance payments under ITA 2007 ss457 and 458;
- the capital gains tax annual exempt amount (s1K(6)(b): not entitled "if ... the individual makes a foreign gain claim, a foreign income claim or a foreign employment election for that tax year");
- foreign losses accruing in that year, which "cease to be allowable losses";
- relief for losses of a trade, profession, vocation or property business carried on wholly outside the UK, for that year's losses, in that year "or in any other tax year" (s845C);
- relief under ITTOIA 2005 s274A for finance costs on dwelling-related loans of an overseas property business, and the brought-forward amount for the next year becomes nil (s845D).

These are lost "regardless of whether a claim or election is made for only foreign income, only foreign gains, or only OWR". Three further effects:

- **Brought-forward overseas losses are used up first.** Carried-forward overseas trade or property losses are deducted from that business's profits before the FIG relief, so they "may be used up even though a foreign income claim is made" ([RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000), Example 2).
- **Pension contributions.** Relief on registered pension contributions can be cut by the amount of FIG relief claimed on "relevant UK earnings", but not below the basic amount, "currently £3,600" (s845F, [RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000)).
- **Adjusted net income ignores the relief.** "All of an individual's foreign income will be taken into account" for tax-free childcare and the High Income Child Benefit Charge.

Losses on UK assets are not affected: "losses arising in respect of the in-year disposal of UK assets as well as unused losses from years outside of a relevant claim are unaffected." A FIG claim does not change treaty residence under Article 4(1) of a double taxation agreement.

### 2. Overseas Workday Relief (OWR) from 6 April 2025

- **Eligibility** ([EIM43560](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43560)). "It will be sufficient that the employee is eligible for the FIG regime for a tax year, they do not need to make a claim for relief under this regime in order to be eligible for OWR." "Domicile is no longer a factor." An employee can use OWR more than once in a lifetime if the 10-year non-residence rule is met again.
- **Election and claim.** The employee makes a foreign employment election for the qualifying year, then an OWR claim in the return for each tax year in which earnings for that qualifying year are charged (ITEPA 2003 Part 2 Chapter 5C). For income earned from 6 April 2025, OWR "must be claimed on the 'residence and foreign income and gains (FIG) regime etc' pages of the Self Assessment return"; income earned before that date stays under the rules in force when earned ([HS211](https://www.gov.uk/government/publications/employment-residence-and-domicile-issues-hs211-self-assessment-helpsheet/hs211-employment-residence-and-domicile-issues-2026)). Keeping earnings offshore is no longer required.
- **What is relieved.** Qualifying foreign employment income: the part of the employment income that relates to duties performed outside the UK, net of the matching share of deductions ([EIM43600](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600), Examples 4 and 5).
- **Financial limit (ITEPA 2003 s41R).** Relief for a qualifying year is "the lower of : 30% of the relevant qualifying employment income for the qualifying year ... or £300,000" ([EIM43600](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600)). The limit counts only employments performed both in and outside the UK. It applies to each qualifying year separately and is cumulative across the tax years in which that year's earnings are taxed (for example a later bonus).
- **Timing trap.** Earnings are claimed in the year they are taxed. An inducement paid in 2025/26 for an employment that starts in 2026/27 is "for" 2026/27 but taxed in 2025/26, so no OWR claim can be made for it ([EIM43600](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600), Example 3).
- **Cost.** An OWR election alone costs the personal allowance, the CGT annual exempt amount and the other items in "What a claim costs".

**OWR transitional rules for remittance basis users who arrived in 2022/23 to 2024/25** ([EIM43605](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43605)):

| Arrived (first UK resident year) | Used OWR on the remittance basis? | Position |
| --- | --- | --- |
| 2023/24 or 2024/25, not a qualifying new resident in 2025/26 | Yes, for at least one of those years | OWR for the first three years of UK residence |
| 2023/24 or 2024/25, and a qualifying new resident in 2025/26 | Yes | OWR for the first four years of UK residence |
| 2023/24 or 2024/25 (either row above) | Yes | No financial limit for any tax year starting on or after 6 April 2025 and ending before 6 April 2028 |
| 2022/23 | Yes, for a year from 6 April 2022 | "not be eligible for OWR for 2025-26, even if they are a qualifying new resident"; a FIG claim is still possible |

For 2026/27, this means: a 2024/25 arrival in this group is in year 3 and gets OWR without the limit; a 2023/24 arrival gets 2026/27 (year 4) only if they were also a qualifying new resident in 2025/26, and then without the limit. Earnings for pre-6 April 2025 remittance basis years received later stay on the remittance basis and, if received before 6 April 2028, can be designated under the TRF.

### 3. The temporary repatriation facility (TRF)

**Rates** ([RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400); [HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf)):

| Tax year of designation | TRF charge on designated amount | Designation election deadline | Source |
| --- | --- | --- | --- |
| 2025/26 | 12% | 31 January 2028 | [RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400), [RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320) |
| 2026/27 (current year) | 12% | 31 January 2029 | [RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400), [RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320) |
| 2027/28 (last year) | 15% | 31 January 2030 | [RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400), [RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320) |

- **Who can use it.** "You must: be UK resident in the tax year of designation" and "have previously used the remittance basis" ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf)). A non-resident year cannot carry a designation.
- **What can be designated ("qualifying overseas capital").** Pre-6 April 2025 foreign income and gains; funds of uncertain origin (for example in a mixed fund at 6 April 2025); capital payments and income from non-UK trusts matched to pre-6 April 2025 FIG within the trust structure; overseas assets such as property and investments that derive from such FIG. Amounts in exempt property or business investment relief investments can be designated without disposing of them.
- **Partial designation** is allowed. Nothing must be remitted in the TRF period. Once designated and the charge paid, the capital "will be available for remittance at any time in the future without incurring any further tax charges". In a mixed fund, designated "TRF capital" is remitted in priority to everything else.
- **How.** Make the election and quantify the amounts on the SA109 "Residence and foreign income and gains (FIG) regime etc" pages. HS264 lists boxes 50 (election), 51 (total designated, excluding trust amounts), 52 (trust capital payments and benefits) and 54 (amount remitted) for the 2025 to 2026 return; check the 2026/27 SA109 notes for the box numbers before filing. Entries are in sterling.
- **Exchange rates.** "As a designation is treated as having taken place at the beginning of the tax year", foreign income and amounts of uncertain source are converted at the rate on 6 April of the designation year (6 April 2026 for 2026/27). Foreign gains are converted at the rate when the asset was disposed of.
- **Nature of the charge** ([RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400)). "The TRF charge is a charge on capital. It is not a tax on income or capital gains." So: no foreign tax credit; outside any double taxation convention that covers only income and gains; it cannot frank Gift Aid; it does not enter adjusted net income, bands, pension thresholds, or next year's payments on account. Returns, records, appeals, penalties and interest apply as for income tax.
- **Paying the charge from offshore.** "There is no exemption in the TRF legislation that would prevent money paid to HMRC to pay the TRF charge being remitted and taxed at the usual tax rates." Designate the money used to pay, or pay from clean capital. Remittance basis charges paid in earlier years "cannot be offset against an amount of TRF charge".
- **Amending and withdrawing** ([RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320)). An election can be amended within the same time limit (or up to 3 months after a notice to file issued after 31 October). "Outside of the timeframe to amend an election, a designation election cannot be withdrawn", and there is no repayment if the designated funds are later spent offshore. Overpayment relief is not available, because the charge is not income tax or CGT. Late elections only under HMRC's late claims policy; no consequential election after careless or deliberate behaviour.
- **Records.** Keep your own records of designated capital and the charge paid. HMRC does not ask for them unless it opens a compliance check.
- **Not designated means taxed as before.** Undesignated pre-6 April 2025 FIG remitted in 2026/27 is taxed at the usual rates; remitted foreign dividends are taxed at the normal rates, not the dividend rates, and the dividend allowance does not apply ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf)). Foreign tax credit is available on the proportion remitted.
- **Business investment relief.** "You will not be able to make a business investment relief claim after 5 April 2028."

### 4. Rebasing to 5 April 2017 for former remittance basis users

[Finance Act 2025 Schedule 11](https://www.legislation.gov.uk/ukpga/2025/8/schedule/11), paragraph 1, applies to a disposal by an individual where all five conditions are met:

- (a) the asset was held on 5 April 2017;
- (b) the disposal is on or after 6 April 2025;
- (c) the asset "was not situated in the United Kingdom at any time in the period beginning with 6 March 2024 and ending with 5 April 2025";
- (d) the individual "was not domiciled in the United Kingdom at any time in a tax year before tax year 2025-26", with deemed domicile under ITA 2007 [s835BA](https://www.legislation.gov.uk/ukpga/2007/3/section/835BA) counting as domicile (para 1(5));
- (e) the individual made a remittance basis claim under ITA 2007 s809B for at least one tax year from 2017/18 to 2024/25 in which the remittance basis did not apply automatically (s809D or s809E).

Effect: the gain or loss is computed as if the asset was acquired on 5 April 2017 "for a consideration equal to its market value on that date". Further rules:

- It applies notwithstanding the no-gain/no-loss rule for spouses (para 1(3)).
- After a share reorganisation treated as the same asset under TCGA 1992 s127, the location test in (c) applies to both the original and the new holding (para 1(4)).
- **Carve-outs for (c)** ([Sch 11 para 2](https://www.legislation.gov.uk/ukpga/2025/8/schedule/11)): an asset brought into the UK is still treated as not situated there if it met the public access or repairs conditions, was in the UK solely or mainly for sale, is clothing, footwear, jewellery or a watch for the personal use of the individual, a spouse or civil partner, or their children or grandchildren under 18, fell within the notional remitted amount under £1000 exemption, or had not failed the temporary importation rule by 5 April 2025.
- **Election out** (para 3): the individual may elect for paragraph 1 not to apply to a disposal. It follows the claims procedure and time limit in sections 42 and 43 of the Taxes Management Act 1970 and "is irrevocable". Elect out where the original cost is higher than the 5 April 2017 value.
- Para 4 amends the separate 2017 rebasing for deemed domiciliaries (Finance (No. 2) Act 2017 Schedule 8, paragraph 41) with effect from 2025/26. Refer those cases.
- Rebasing only changes the base cost. A gain on a disposal on or after 6 April 2025 is taxed on the arising basis in the year of disposal ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf), Example 2), unless the person is a qualifying new resident and makes a foreign gain claim.

### 5. Inheritance tax: long-term UK residence (outline only)

From 6 April 2025 "the domicile and deemed domicile rules were replaced by new long-term UK resident rules" ([HMRC](https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident)). The test is in [IHTA 1984 s6A](https://www.legislation.gov.uk/ukpga/1984/51/section/6A):

- **In.** An individual is a long-term UK resident "at all times in a tax year if they were UK resident for at least 10 of the previous 20 tax years" (s6A(1)). HMRC's summary puts it as either the previous 10 consecutive years or a total of 10 years or more within the previous 20.
- **Out after 10 years away.** Not long-term UK resident if non-UK resident "for any 10 consecutive tax years during the 19 tax years before the current tax year" (s6A(2)(a)). HMRC: after 10 consecutive years of non-residence the test is reset, and only the year of return and later years count.
- **The tail.** Also out after non-residence for the "required number" of consecutive tax years ending with the previous tax year (s6A(2)(b)). Count the resident years in the 20 tax years ending with the last resident year:

| Resident years in that 20-year period | Consecutive non-resident years needed to fall out |
| --- | --- |
| 13 or less | 3 |
| 14 | 4 |
| 15 | 5 |
| 16 | 6 |
| 17 | 7 |
| 18 | 8 |
| 19 | 9 |
| 20 | 10 |

- **Transitional exits** ([HMRC](https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident)). A person who did not have UK domicile or deemed domicile on 30 October 2024, is non-resident for 2025/26 and does not return, is not a long-term UK resident. A person who had deemed domicile on 30 October 2024, is non-resident for 2025/26 and does not return, stops being a long-term UK resident after 3 years of non-residence.
- **Residence** is the SRT for 2013/14 onward, and the old income tax rules for 2012/13 and earlier (s6A(5)). Section 6B modifies the test for young persons, and ss267ZC to 267ZE allow an election to be treated as long-term resident.
- **Trusts.** Inheritance tax is charged on overseas assets in a trust the individual set up or added to, "even when you were not a long-term UK resident". There is no IHT on death on trust assets placed in trust while non-UK domiciled, overseas on 30 October 2024, and overseas at death or when the individual's rights ended. Tell trustees when long-term UK residence status changes.
- Transfers or deaths before 6 April 2025 follow the old domicile rules. Any IHT computation, trust charge or planning is a refer case.

### 6. Before 6 April 2025: the remittance basis (history, for old years and old money)

This section is dated. It applies to tax years up to and including 2024/25 and to pre-6 April 2025 FIG that is still offshore.

- **The old rule.** A UK resident who was not domiciled in the UK could claim the remittance basis, paying UK tax on foreign income and gains only when remitted to the UK ([RDRM32210](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210)). "From 6 April 2025 it is not possible to use the remittance basis of taxation."
- **Old FIG stays taxable on remittance.** FIG that arose to a former remittance basis user before 6 April 2025 "will continue to be taxed at the usual tax rates if they are remitted to the UK on or after 6 April 2025", unless designated under the TRF. The remittance rules still decide what counts as a remittance: bringing money or assets derived from old FIG to the UK, using them for UK services or relevant debts, or benefits to "relevant persons" such as a spouse, minor children or grandchildren, and close companies ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf)). Mixed fund ordering rules still apply.
- **No FIG relief for old money.** Even a qualifying new resident cannot claim FIG relief on pre-6 April 2025 FIG, "whether or not he remits them during a period when he is a qualifying new resident or after" ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000), Example 3).
- **Remittance basis charge (reference only).** HMRC: "The guidance in this section only applies to tax years up to and including the 2024-25 tax year and remains for reference purposes only." The charge was paid by long-term residents aged 18 or over who claimed the remittance basis:

| Years (up to 2024/25 only) | Condition | Annual remittance basis charge | Source |
| --- | --- | --- | --- |
| 2017/18 to 2024/25 | UK resident in at least 7 of the 9 preceding tax years | £30,000 | [RDRM32210](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210) |
| 2017/18 to 2024/25 | UK resident in at least 12 of the 14 preceding tax years | £60,000 | [RDRM32210](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210) |
| 2026/27 | Any | No charge: the remittance basis no longer exists | [RDRM32210](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm32210) |

- **Deemed domicile (still relevant to rebasing and old years).** Under ITA 2007 [s835BA](https://www.legislation.gov.uk/ukpga/2007/3/section/835BA), Condition A is: born in the UK, domicile of origin in the UK, and UK resident for the year. Condition B is UK residence "for at least 15 of the 20 tax years immediately preceding the relevant tax year".
- **OWR on pre-2025 earnings.** Earnings for remittance basis years keep the old OWR rules ([HS211](https://www.gov.uk/government/publications/employment-residence-and-domicile-issues-hs211-self-assessment-helpsheet/hs211-employment-residence-and-domicile-issues-2026)).

## Boundaries and exceptions

| Situation | Result | Source |
| --- | --- | --- |
| Treaty-resident elsewhere in a year when SRT-resident in the UK | Counts as a UK resident year; it breaks the 10-year run | [RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000) |
| Exactly 10 non-resident years, then arrival | Qualifies: s845B(1)(c) needs each of the 10 years before to be non-resident, not more than 10 | [s845B](https://www.legislation.gov.uk/ukpga/2005/5/section/845B) |
| 9 non-resident years, then arrival | Does not qualify in any year of that stay | [s845B](https://www.legislation.gov.uk/ukpga/2005/5/section/845B) |
| Non-resident in year 2 of the window, back in year 3 | Year 2 lost; years 3 and 4 claimable; no fifth year | [RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000) |
| Member of the House of Commons or Lords for part of a year | Disqualified for that year; membership years count as UK resident | [RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000) |
| Child under 10 at 6 April | Not a qualifying new resident under s845B(1) for that year (Finance Act 2026 condition) | [s845B](https://www.legislation.gov.uk/ukpga/2005/5/section/845B) |
| Claim covers one small foreign source only | Full cost still applies: personal allowance, CGT annual exempt amount, foreign losses | [RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000) |
| Pre-6 April 2025 FIG of a new qualifying resident who used the remittance basis earlier | No FIG relief; taxed on remittance unless designated under the TRF | [RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000) |
| Designated funds later spent abroad | No repayment of the TRF charge once the amendment window has passed | [RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320) |
| Asset in the UK for a day between 6 March 2024 and 5 April 2025 | No rebasing unless a Schedule 11 para 2 carve-out applies | [Sch 11](https://www.legislation.gov.uk/ukpga/2025/8/schedule/11) |
| Only ever taxed on the remittance basis automatically (no s809B claim) | No rebasing: condition (e) needs a claim in 2017/18 to 2024/25 | [Sch 11](https://www.legislation.gov.uk/ukpga/2025/8/schedule/11) |

## Worked cases (2026/27)

**Case 1: arrival in 2026/27 after 10+ years away.** Bassim was non-UK resident for all tax years 2013/14 to 2025/26 and became UK resident on 6 April 2026. He is a qualifying new resident for 2026/27 and can claim for 2026/27, 2027/28, 2028/29 and 2029/30 in each year he is UK resident. If he is non-resident in 2027/28 he loses that year and cannot claim in 2030/31 ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000), Example 6). His 2026/27 claim is due by 31 January 2029.

**Case 2: arrival in 2024/25, before the reform.** Marie was non-resident 2013/14 to 2023/24 and resident from 2024/25. 2024/25 is her first qualifying year, but no claim is possible for it. She can claim for 2025/26, 2026/27 and 2027/28 if resident, and not for 2028/29 ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000), Example 2). For 2026/27 the look-back is 2014/15 to 2023/24, not 2016/17 to 2025/26.

**Case 3: treaty year breaks the run.** Allegra was UK resident under the SRT in 2017/18 but treaty-resident in Italy. She arrives permanently in 2025/26. 2017/18 counts as a UK resident year, so she has no 10-year run and cannot claim in 2025/26 or later years of this stay ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000), Example 4).

**Case 4: partial claim.** Yan is a qualifying new resident for 2026/27 with profits of £20,000 from a trade carried on wholly outside the UK. If she claims relief of £15,000, "£15,000 of her £20,000 profits will be relieved from tax, and she will pay tax at the usual rates on the remaining £5,000" ([RFIG42100](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100), Example 1). She also loses her personal allowance and CGT annual exempt amount for 2026/27.

**Case 5: foreign loss lost for good.** Ayaan, a qualifying new resident, has in 2026/27 overseas consultancy profits of £200,000, an overseas software business loss of £25,000 and UK profits of £50,000. She claims relief on the £200,000. The £25,000 loss cannot be set against either profit, "in any future years" ([RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000), Example 1). The £50,000 UK profit is taxed at the usual rates.

**Case 6: TRF in 2026/27.** Nida, a former remittance basis user, holds £30,000 of 2022/23 foreign income in an overseas account and designates all of it in her 2026/27 return. The TRF charge is "£3,600 (12% of £30,000)" ([RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400)). She can pay TRF charges from that account without an income tax remittance charge, because the money is designated. The election deadline is 31 January 2029. If she waits and designates in 2027/28, the rate is 15%.

**Case 7: OWR and the financial limit.** Sergei is a qualifying new resident for 2025/26 and makes an OWR election. He earns £500,000 for 2025/26 and 40% of his duties are outside the UK, giving £200,000 of qualifying foreign employment income. Relief is the lower of £300,000 and £150,000, so £150,000. In 2026/27 he receives a £100,000 bonus for 2025/26 duties. His 2025/26 qualifying employment income charged to tax is now £600,000; the cap is the lower of £300,000 and £180,000, less £150,000 already claimed, so he can claim £30,000 in his 2026/27 return ([EIM43600](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600), Example 4).

**Case 8: rebasing decision.** A former remittance basis user who claimed the remittance basis under s809B in 2019/20, was never domiciled or deemed domiciled in the UK, and sells in 2026/27 a foreign share portfolio held on 5 April 2017 that never came to the UK, computes the gain from its 5 April 2017 market value. If the original cost was higher than that value, they should consider the irrevocable election out. If any holding was situated in the UK at any time between 6 March 2024 and 5 April 2025 and no carve-out applies, that holding is not rebased ([Sch 11](https://www.legislation.gov.uk/ukpga/2025/8/schedule/11)).

## When to refuse or refer

- **Non-UK trusts** of any kind: settlor or beneficiary positions, capital payments, matching to trust income and gains, TRF designations of trust amounts, and trust IHT charges.
- **Inheritance tax**: any computation, lifetime transfers, the tail after leaving, trusts, elections under ss267ZC to 267ZE, and the young persons rule.
- **Mixed funds**: identifying what was remitted from an account holding more than one type or year of income, gains or capital, and choosing what to designate.
- **Residence doubt**: any SRT question, split years, the Finance Act 2020 coronavirus modifications, and look-backs reaching 2012/13 or earlier. Use `uk-statutory-residence-test` or refer.
- **Treaties and foreign tax credits**: treaty residence, double taxation relief where the OWR limit bites, and whether a treaty reaches the TRF charge.
- **Transfer of assets abroad and settlements legislation.**
- **Domicile before 2025/26**, where rebasing or old years turn on it.
- **Valuations** at 5 April 2017 and the decision to elect out of rebasing.
- **Business investment relief**, exempt property and other remittance basis history.
- **Members of Parliament** and anyone who held a seat in the look-back period.
- **Late claims or elections**: only HMRC's late claims policy can help; refer before promising anything.
- Refuse to confirm that a client "qualifies" until residence for every year in the look-back is established.

## Filing and payment

**2026/27 (current year).**

- Return: SA100 with SA109 "Residence and foreign income and gains (FIG) regime etc" pages for the FIG claim, OWR election and claim, and TRF election; SA106 for foreign income; SA108 for gains. Register for Self Assessment by 5 October 2027 if not already in it.
- Online return and payment of the balance: 31 January 2028. Paper return: 31 October 2027. Second payment on account: 31 July. These follow the pattern shown on [GOV.UK deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines), which currently shows the 2025/26 dates; confirm the 2026/27 dates there.
- FIG claim and TRF designation: both are made in the return (including by amendment), and the statutory window runs to 31 January 2029. Check the OWR claim time limit in the SA109 notes ([s845A](https://www.legislation.gov.uk/ukpga/2005/5/section/845A); [RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320)).
- The TRF charge is collected through Self Assessment like income tax, with the same penalties and interest, but does not change next year's payments on account ([RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400)).
- MTD for Income Tax users make claims through their software instead of the SA boxes ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf)).

**2025/26 returns being filed now (dated 25 September 2026).**

- Online return and payment: 31 January 2027. Paper return: 31 October 2026. Registration for someone new to Self Assessment: 5 October 2026 ([GOV.UK deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)).
- 2025/26 was the first FIG claim year and the first TRF year (charge 12%). The FIG claim and TRF election for 2025/26 can be made or amended until 31 January 2028 ([RFIG42300](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42300); [RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320)).
- HS264 box numbers 50, 51, 52 and 54 apply to the 2025/26 SA109.

## Completion checklist

- [ ] Tax year stated as 2026/27 (6 April 2026 to 5 April 2027).
- [ ] SRT residence established for every year in the look-back (10 years before the first qualifying year; 20 years for IHT). Split and treaty years counted as UK resident.
- [ ] First qualifying year identified; 2026/27 confirmed inside the 4-year window; not disqualified; age condition met.
- [ ] Each foreign source checked as qualifying foreign income or gain, arising on or after 6 April 2025.
- [ ] Cost of claiming weighed: allowances, CGT annual exempt amount, foreign losses, overseas property finance costs, pension relief, child benefit charge.
- [ ] Claim made source by source and quantified in the 2026/27 return, by 31 January 2029 at the latest.
- [ ] OWR: eligibility, transitional row, election, financial limit per qualifying year.
- [ ] Former remittance basis user: TRF designation considered for 2026/27 at 12% ([RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400)), exchange rates at 6 April 2026, records kept, charge funded from designated or clean money.
- [ ] Rebasing conditions tested on any disposal of an asset held on 5 April 2017; election out considered.
- [ ] Long-term UK residence status noted for IHT; referred where relevant.
- [ ] Refer items above referred.

## Sources and currency

This Guide states the rules as the official pages print them on 25 September 2026. HMRC manuals are updated often; check the "Updated" date on each page before relying on it.

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
