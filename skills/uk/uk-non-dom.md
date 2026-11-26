---
name: uk-non-dom
description: "UK foreign income and gains for new arrivals and former remittance basis users in 2026/27: FIG eligibility, claims and lost allowances, Overseas Workday Relief, Temporary Repatriation Facility, 2017 rebasing and the inheritance-tax residence outline. Trigger on UK non-dom, FIG, OWR, TRF, remittance basis abolished, rebasing or IHT tail. Residence determinations, trusts and specialist cases are referred."
version: 1.4
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - uk-income-tax-sa100
  - uk-statutory-residence-test
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# UK non-doms after April 2025: FIG, OWR, TRF, rebasing and IHT (2026/27)

## Who this applies to

The remittance basis ended from 6 April 2025; 2024/25 was its last tax year. UK residents now generally pay tax on worldwide income and gains as they arise, with relief for qualifying new residents requiring a claim. Old remittance-basis income and gains still need separate treatment ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf)). This Guide covers 2026/27, 6 April 2026 to 5 April 2027.

**Establish residence before applying relief.** Use `uk-statutory-residence-test`. For FIG, a year of SRT residence counts even if split-year treatment applies or a treaty treats the person as resident elsewhere. The first qualifying year fixes the window; it is not restarted by a later claim ([RFIG44000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000)).

**First qualifying year.** Under [ITTOIA 2005 s845B(1)](https://www.legislation.gov.uk/ukpga/2005/5/section/845B), in 2026/27 the individual must be UK resident, at least 10 at the start of the tax year, not a member of either House of Parliament for any part of it, and non-UK resident in each of the preceding 10 tax years. Nationality and domicile do not decide eligibility: returning UK nationals can qualify. Parliamentary membership in the look-back needs specialist review.

**Subsequent years.** Section 845B(2)-(3) permits claims in the next three tax years if UK resident and not disqualified. A qualifying first year in 2022/23, 2023/24 or 2024/25 counts towards the window, although FIG claims cannot relieve income or gains from those pre-reform years. In 2026/27 a qualifying 2024/25 arrival is in year 3, a 2023/24 arrival in year 4, and a 2022/23 arrival has no year left.

| Boundary | Result | Source |
|---|---|---|
| Exactly 10 non-resident tax years before the first qualifying year | Enough; nine is insufficient for that stay | https://www.legislation.gov.uk/ukpga/2005/5/section/845B |
| Non-resident year inside the four-year window, or year for which no claim is made | No replacement year; remaining eligible years can still be claimed | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000 |
| Split year or treaty non-residence while SRT-resident | Counts as a full resident year for FIG eligibility | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000 |

## Rates, bands and thresholds

| Item | Rule and period | Source |
|---|---|---|
| FIG window | First qualifying year plus next 3 tax years; first-year conditions above | https://www.legislation.gov.uk/ukpga/2005/5/section/845B |
| OWR financial limit | Lower of 30% of relevant qualifying employment income or £300,000 per qualifying year; cumulative across receipt years; transitional exception below | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600 |
| TRF designation | 12% for 2025/26 or 2026/27; 15% for 2027/28; no later designation year | https://www.legislation.gov.uk/ukpga/2025/8/schedule/10 |
| Rebasing | Market value at 5 April 2017, on disposals from 6 April 2025, only if all five conditions below are met | https://www.legislation.gov.uk/ukpga/2025/8/schedule/11 |
| IHT ordinary long-term residence test | At least 10 of previous 20 tax years, subject to the exclusions and special cases below | https://www.legislation.gov.uk/ukpga/1984/51/section/6A |
| Example 1 income-tax assumptions, England 2026/27 | Standard personal allowance £12,570; basic taxable band £37,700 (computed: £50,270 less £12,570) at 20%, then 40% within the stated income; allowance tapers £1 per £2 of adjusted net income above £100,000 | https://www.gov.uk/income-tax-rates |

## The taxable base

**FIG income.** A foreign income claim covers income arising from 6 April 2025 which meets [s845H](https://www.legislation.gov.uk/ukpga/2005/5/section/845H) and is not disqualified by [s845I](https://www.legislation.gov.uk/ukpga/2005/5/section/845I). Ordinary wholly overseas trading profits, overseas property profits, foreign interest and dividends from non-UK resident companies can qualify. Foreign pensions, royalties and offshore income gains also have specific statutory categories; do not assume every foreign receipt qualifies. Employment income uses OWR. Specialist pension, performance-income, securities, settlements and investment-management classifications: **Check this point with one of our partner accountants.**

**FIG gains.** A separate foreign gain claim is required under TCGA 1992 Schedule D1. For an ordinary foreign asset gain, the asset must be outside the UK and must not derive at least 75% of its value from UK land. Old remittance-basis gains are excluded. Attributed company/trust gains and special asset classifications: **Check this point with one of our partner accountants.** ([RFIG45500](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig45500)).

**Claim mechanics.** Claim in the individual's Self Assessment return each year, identify each source of income or each gain, and quantify the relief. There is no automatic relief, de minimis or monetary cap. A smaller claim relieves only the amount claimed; an incorrect quantification does not invalidate the claim but no quantification does. Income relief is deducted at Step 2 in calculating net income, only from qualifying foreign income. Relieved amounts can be brought to the UK later without further UK tax ([s845A](https://www.legislation.gov.uk/ukpga/2005/5/section/845A); [RFIG42100](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100)).

**Costs of a foreign income claim, foreign gain claim or OWR election.** These apply for the year even if only one small source is claimed ([RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000)):

- Lose the personal allowance, blind person's allowance, married-couple/civil-partner tax reductions, transferable marriage allowance and life-insurance payment relief.
- Lose the CGT annual exempt amount. Foreign qualifying capital losses accruing in that year cease to be allowable; UK asset losses and unused losses from years outside a claim are unaffected. Foreign-gain relief is applied before allowable losses.
- A loss of a business carried on wholly outside the UK in that year gets no relief then or later, if its profits would have been qualifying foreign income. This includes qualifying overseas trade, profession, vocation and property businesses ([s845C](https://www.legislation.gov.uk/ukpga/2005/5/section/845C)). Brought-forward overseas trade/property losses are used against that business's profits before FIG relief.
- Lose the overseas-property dwelling-loan finance-cost reduction under s274A for the year; the brought-forward amount for the following year is nil ([s845D](https://www.legislation.gov.uk/ukpga/2005/5/section/845D)).

Foreign income relief is disregarded for adjusted net income: the foreign income still counts for tax-free childcare and the High Income Child Benefit Charge. A foreign income claim can reduce the earnings-based pension-contribution relief ceiling by the relieved relevant UK earnings, but not below the £3,600 basic amount ([s845F](https://www.legislation.gov.uk/ukpga/2005/5/section/845F); RFIG43000). Pension relief and adjusted-net-income consequences of OWR: **Check this point with one of our partner accountants.** Compare the benefit of a claim with the allowances/losses given up and the alternative foreign-tax-credit position.

**Overseas Workday Relief.** A qualifying new resident employee can make a foreign employment election and a separate claim on qualifying employment income for overseas duties. No FIG claim is needed; the new relief does not require payment offshore. General-earnings apportionment must be just and reasonable; a simple UK-workdays ratio is not a universal calculation. Split-year UK-part restrictions, Crown employment, share awards, multiple/associated employments, deductions and unusual workday allocations: **Check this point with one of our partner accountants.** ([EIM43555](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43555); [EIM43565](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43565)).

For the financial limit, use relevant net taxable qualifying employment income from the employment(s) to which the claim relates, not a separate wholly UK employment's salary. Apply the limit for each qualifying year cumulatively across tax years when that year's earnings are taxed, deducting relief already claimed. Earnings taxed before the elected qualifying year cannot use that year's relief ([EIM43600](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600)). Eligibility can recur after another qualifying period of non-residence ([EIM43560](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43560)).

**OWR transition.** Employees who became resident in 2023/24 or 2024/25, qualified for OWR and elected the remittance basis for at least one of those years retain three residence years of OWR if not a qualifying new resident in 2025/26, or four if they are. They still need a new OWR election and claim. Their relief for tax years starting from 6 April 2025 and ending before 6 April 2028 is uncapped. A qualifying 2024/25 arrival can therefore use year 3 in 2026/27; a 2023/24 arrival gets year 4 only if qualifying for the four-year treatment. A 2022/23 arrival who qualified for and elected remittance-basis OWR in a year from 2022/23 to 2024/25 gets no OWR for 2025/26. Earnings for duties in a pre-2025 remittance-basis year retain the old rules; qualifying late receipts before 6 April 2028 may be designated under TRF. Do not treat all late-paid earnings as qualifying ([EIM43605](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43605)).

**Old money.** Pre-6 April 2025 FIG from remittance-basis years remains taxable at usual rates on remittance unless validly designated under TRF; a new FIG claim cannot relieve it. Money, assets derived from it, UK services/debts and benefits to relevant persons can create remittances without a simple bank transfer. Mixed funds, relevant-person attribution, remitted-dividend reporting and rates, proportionate foreign tax credit, business investment relief (including its 5 April 2028 claim cutoff), exempt property, Gift Aid and remittance-basis-charge offsets: **Check this point with one of our partner accountants.** ([HS264](https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf)).

**TRF eligibility and timing.** A person must have used the remittance basis in at least one year before 2025/26 and be UK resident in the designation year. Make the election in the 2025/26, 2026/27 or 2027/28 return. For ordinary old FIG, the capital must satisfy Schedule 10 paragraph 2: it arose as income/gain by 2024/25 and its remittance would attract the specified remittance-basis charge. It can remain offshore, or be remitted during the TRF period. If already remitted and not previously designated, designate it for the year of remittance, not a later year. Partial designation is allowed; designated qualifying capital can be remitted later without a further remittance charge ([Schedule 10 paras 1-2, 10 and 12](https://www.legislation.gov.uk/ukpga/2025/8/schedule/10)).

**TRF amount.** Under paragraph 8(2A), ordinary old-FIG capital is valued when it first arose. Relevant foreign income/CGT paid or payable is normally deducted from the amount that can be designated, except to the extent the tax is paid or will be paid from other funds (paras 8(3)-(4A)). State the total and the designation basis for each amount, including which remittance-basis amounts were remitted that year. Foreign-currency conversions, uncertain-origin funds, valuation questions and trust/settlements/ToAA amounts: **Check this point with one of our partner accountants.** A designation alone does not prove entitlement to every exemption.

**TRF charge.** It is a charge on capital, collected like income tax; it is separate from taxable income/gains, adjusted net income and tax bands. No foreign tax credit offsets the charge, and it does not create payments on account. If undesignated old FIG pays the charge from offshore, that payment is itself an ordinary remittance; use designated funds or clean capital ([RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400); HS264). Keep records identifying each designated amount, charge paid and later remittances (Schedule 10 paras 8(8), 9(7)).

**Rebasing.** [FA 2025 Schedule 11 paragraph 1](https://www.legislation.gov.uk/ukpga/2025/8/schedule/11) uses 5 April 2017 market value for the gain or loss only if all five conditions hold:

1. The individual held the asset on 5 April 2017.
2. Disposal is on or after 6 April 2025.
3. It was not UK-situated at any time from 6 March 2024 to 5 April 2025, subject to paragraph 2 exceptions.
4. The individual was not UK domiciled in any tax year before 2025/26, including deemed domicile under s835BA.
5. They made a s809B remittance-basis claim in at least one year from 2017/18 to 2024/25 in which neither automatic route, s809D nor s809E, applied.

The gain is still considered in the disposal year; rebasing does not itself exempt it. A separate qualifying foreign gain claim may relieve it. An election out for a particular disposal is irrevocable and follows TMA ss42-43; compare original cost with the 2017 value rather than automatically electing out. Spouse transfers, share reorganisations, paragraph 2 location exceptions (public access, repair, sale, personal items, small notional remittances or temporary importation), the separate deemed-domiciliary rebasing, valuations and election procedure: **Check this point with one of our partner accountants.**

**Inheritance tax outline.** From 6 April 2025 long-term UK residence replaces domicile/deemed domicile for the ordinary overseas-asset scope. Overseas assets may be within IHT on transfer or death; an actual charge needs a separate computation ([HMRC guidance](https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident)). Under [s6A](https://www.legislation.gov.uk/ukpga/1984/51/section/6A), the ordinary test is 10 resident years in the previous 20, but not after any 10 consecutive non-resident years in the previous 19. There is also an exit after the required consecutive non-resident years ending with the preceding year. Count resident years in the 20 years ending with the last resident year: 13 or fewer requires 3 non-resident years; 14 requires 4; 15 requires 5; 16 requires 6; 17 requires 7; 18 requires 8; 19 requires 9; 20 requires 10. Pre-2013/14 residence uses the income-tax rules for that earlier year. Transitional exits tied to domicile on 30 October 2024 and non-residence in 2025/26, young persons, elections under ss267ZC-267ZE, trust assets (including the 30 October 2024 protection), trustee notifications, pre-6 April 2025 transfers/deaths and all IHT computations/planning: **Check this point with one of our partner accountants.**

## Deadlines and filing

Use the year's Self Assessment return with SA109 residence/FIG pages and the supplementary pages for the income or gains, ordinarily SA106/SA108. Declare the income/gains and claim the relief; eligibility alone is insufficient. MTD users make relevant claims and adjustments through compatible software. The 2026/27 form and box-level submission, including the TRF boxes numbered 50/51/52/54 in 2025/26: **Check this point with one of our partner accountants.** Do not reuse old box numbers for a later return ([RFIG42100](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100); HS264).

- **Ordinary annual return:** 2025/26 paper received by 31 October 2026 and online by 31 January 2027; 2026/27 paper by 31 October 2027 and online by 31 January 2028. Late notices and registration/notification, balancing payment and payments-on-account dates: **Check this point with one of our partner accountants.** Use `uk-income-tax-sa100` and `uk-payments-on-account` for their conditions ([TMA s8](https://www.legislation.gov.uk/ukpga/1970/9/section/8)).
- **FIG income and gain claims:** 31 January 2028 for 2025/26 and 31 January 2029 for 2026/27. Claims are in the return, including amendments ([s845A](https://www.legislation.gov.uk/ukpga/2005/5/section/845A); [RFIG42300](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42300)).
- **OWR:** the election deadline follows the qualifying employment year; the separate claim deadline follows the tax year for which relief is claimed. Each is the anniversary of 31 January following its relevant year's end: for 2026/27, 31 January 2029 ([ITEPA ss41M and 41P](https://www.legislation.gov.uk/ukpga/2003/1/section/41M); [EIM43585](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43585)).
- **TRF designation:** 31 January 2028 for 2025/26, 31 January 2029 for 2026/27, 31 January 2030 for 2027/28 ([RDRM73320](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320)).

Ordinary amendments/withdrawals follow the claim/election time limit. Where the initial claim/election was made by its ordinary deadline, a late notice can extend its amendment window; it does not extend that initial deadline. Late claims, consequential claims, withdrawals, HMRC-assessment/TRF offsets and repayments: **Check this point with one of our partner accountants.** In particular, do not promise a TRF refund when designated money is spent abroad or invoke overpayment relief for a designation election (RDRM73320).

## Penalties and interest

TRF administration, penalties and unpaid-tax interest follow income-tax collection rules (Schedule 10 paragraph 9); that does not make the charge income tax or subject it to payments on account. Ordinary HMRC late-payment interest is **8.00% from 24 November 2026**; apply the rates for the actual overdue period, not a projected future rate ([HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)). Filing/payment/inaccuracy penalties, MTD differences, reasonable excuse, appeals and interest computations: **Check this point with one of our partner accountants.**

## Cross-border points

A FIG claim does not determine treaty residence. A treaty-non-resident year can still count as UK resident for FIG as above. The TRF charge is outside a treaty that covers income/gains but not capital; do not assume every treaty has the same scope ([RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000); RDRM73400). Treaty residence, foreign tax credit, double taxation when OWR is capped, temporary non-residence on departure and the IHT tail in an actual case: **Check this point with one of our partner accountants.** Use `uk-foreign-tax-and-withholding` for the separate credit-relief topic.

## Worked examples

### Example 1: a new arrival, FIG claim or not

Leila was not UK resident in any of the 10 tax years to 2025/26 and is UK resident from 6 April 2026, outside Scotland. In 2026/27 she has a UK salary of £60,000 and overseas rental profit of £40,000, with no foreign tax. Assume she is at least 10 on 6 April 2026, is not disqualified, has no other income, losses, deductions or reliefs, and is otherwise entitled to the full personal allowance without a claim. She is a qualifying new resident for 2026/27. The calculation compares income tax only, excluding NIC.

- **No claim.** Total income £100,000; her personal allowance is not tapered (income is not above £100,000). Taxable £87,430. Tax: £37,700 at 20% = £7,540; £49,730 at 40% = £19,892. Total £27,432.
- **FIG claim on the £40,000.** The qualifying rental profit is deducted. She loses the personal allowance. Taxable £60,000: £7,540 + (£22,300 at 40% = £8,920). Total £16,460.
- **Saving £10,972.** She also loses the CGT annual exempt amount for the year; if she has UK gains, add that cost. Claim by 31 January 2029.

```oa-check
name: Qualifying new resident, salary 60,000 and foreign rent 40,000, claim vs no claim (2026/27)
inputs:
  uk_salary: 60000
  foreign_rent: 40000
  personal_allowance: 12570
  basic_band: 37700
steps:
  - taxable_no_claim: uk_salary + foreign_rent - personal_allowance
  - tax_no_claim: min(taxable_no_claim, basic_band) * 0.20 + max(taxable_no_claim - basic_band, 0) * 0.40
  - taxable_claim: uk_salary
  - tax_claim: min(taxable_claim, basic_band) * 0.20 + max(taxable_claim - basic_band, 0) * 0.40
  - saving: tax_no_claim - tax_claim
expected:
  taxable_no_claim: 87430
  tax_no_claim: 27432
  tax_claim: 16460
  saving: 10972
```

### Example 2: TRF timing, 2026/27 against 2027/28 against no designation

Nida used the remittance basis up to 2024/25. She holds £30,000 of 2022/23 foreign income offshore and is UK resident in 2026/27. Assume she is an additional rate taxpayer in England, the £30,000 is entirely untaxed remittance-basis income qualifying under Schedule 10 paragraph 2, with no foreign tax, other relief or trust involvement. The 2027/28 comparison assumes she remains UK resident and leaves this income offshore until that year.

- **Designate in the 2026/27 return:** 12% of £30,000 = £3,600 ([RDRM73400](https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400)). Election by 31 January 2029.
- **Wait for 2027/28:** 15% = £4,500. The delay costs £900.
- **Bring it in in 2026/27 with no designation:** taxed at her usual rate, 45% = £13,500. Remitting it in 2026/27 prevents waiting until a 2027/28 designation for that remittance.
- **Edge.** If she pays the charge from the same offshore account, that payment is a remittance. Designating the full £30,000 covers it; paying from undesignated old FIG would be taxed at 45%.

```oa-check
name: TRF on 30,000 of pre-2025 foreign income, 12% vs 15% vs remitted at 45%
inputs:
  old_fig: 30000
steps:
  - trf_2026_27: old_fig * 0.12
  - trf_2027_28: old_fig * 0.15
  - cost_of_waiting: trf_2027_28 - trf_2026_27
  - undesignated_tax: old_fig * 0.45
  - saving_vs_undesignated: undesignated_tax - trf_2026_27
expected:
  trf_2026_27: 3600
  trf_2027_28: 4500
  cost_of_waiting: 900
  undesignated_tax: 13500
  saving_vs_undesignated: 9900
```

### Example 3: OWR financial limit with a later bonus

Historical Case 7, matching [EIM43600 Example 4](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600). Assume one employment performed in and outside the UK, no deductions or other OWR claims, no transitional exemption from the cap, and 40% overseas duties for both salary and bonus. Sergei is a qualifying new resident for 2025/26 and makes an OWR election. He earns £500,000 for 2025/26 and 40% of his duties are outside the UK: £200,000 of qualifying foreign employment income. Relief is the lower of £300,000 and 30% of £500,000 (£150,000), so £150,000. In 2026/27 he receives a £100,000 bonus for 2025/26 duties. His 2025/26 qualifying employment income charged to tax is now £600,000; the limit is the lower of £300,000 and £180,000, less £150,000 already claimed. He claims £30,000 in his 2026/27 return.

```oa-check
name: OWR limit across two tax years for one qualifying year (EIM43600 Example 4)
inputs:
  earnings_y1: 500000
  bonus_y2: 100000
  overseas_share: 0.40
  cap: 300000
steps:
  - qfei_y1: earnings_y1 * overseas_share
  - relief_y1: min(qfei_y1, min(cap, earnings_y1 * 0.30))
  - limit_total: min(cap, (earnings_y1 + bonus_y2) * 0.30)
  - relief_y2: min(bonus_y2 * overseas_share, limit_total - relief_y1)
expected:
  qfei_y1: 200000
  relief_y1: 150000
  limit_total: 180000
  relief_y2: 30000
```

### Historical cases 1-8 retained

Assume each person described as qualifying meets the age and parliamentary restrictions; establish all residence years rather than inferring them from arrival dates.

1. **Bassim:** non-resident for all years 2013/14 to 2025/26, resident from 6 April 2026. His four-year window is 2026/27 to 2029/30. If non-resident in 2027/28 that year is lost; 2030/31 cannot replace it. His 2026/27 claim deadline is 31 January 2029 (s845B; RFIG44000; RFIG42300).
2. **Marie:** non-resident 2013/14 to 2023/24, resident from 2024/25. The first qualifying year is 2024/25; claim years are 2025/26, 2026/27 and 2027/28 if resident and not disqualified. No FIG relief for 2024/25 or 2028/29. The relevant ten-year look-back is 2014/15 to 2023/24 (s845B).
3. **Allegra:** SRT-resident in 2017/18 but treaty-resident in Italy, then permanent arrival in 2025/26. The treaty year breaks the non-resident run; no FIG relief for 2025/26 or later years of that stay (RFIG44000).
4. **Yan:** qualifying in 2026/27, wholly overseas trade profit £20,000, FIG claim £15,000. £5,000 remains taxable; personal allowance and CGT annual exempt amount are lost (RFIG42100; RFIG43000).
5. **Ayaan:** in 2026/27, wholly overseas consultancy profit £200,000, wholly overseas software loss £25,000 and UK profit £50,000. Assume both overseas trades' profits meet s845H/I. Claiming £200,000 FIG relief leaves £50,000 UK profit taxable and permanently denies the £25,000 loss, including carry-forward (s845C; RFIG43000).
6. **Nida:** the original £30,000 of 2022/23 foreign income and 2026/27 designation are preserved in Example 2; the 12% charge is £3,600, deadline 31 January 2029. The 2027/28 comparison at 15% is conditional on continued UK residence and the money remaining unremitted until that year.
7. **Sergei:** the original £500,000 salary for 2025/26, 40% overseas duties, £100,000 later bonus in 2026/27 and £300,000 cap are preserved in Example 3. Relief is £150,000 then £30,000.
8. **Rebasing:** a former remittance-basis user claimed under s809B in 2019/20, was never UK domiciled/deemed domiciled and sells in 2026/27 a foreign share portfolio held on 5 April 2017 which never came to the UK. Assume neither automatic remittance route applied in 2019/20. It is rebased to 5 April 2017 market value; compare original cost before electing out. A holding UK-situated between 6 March 2024 and 5 April 2025 needs a paragraph 2 exception. Valuation, share reorganisation or election details: **Check this point with one of our partner accountants.** (Schedule 11).

```oa-check
name: Historical partial claim and overseas loss cases, 2026/27
inputs:
  yan_profit: 20000
  yan_claim: 15000
  ayaan_overseas_profit: 200000
  ayaan_overseas_loss: 25000
  ayaan_uk_profit: 50000
steps:
  - yan_unrelieved: yan_profit - yan_claim
  - ayaan_fig_relief: ayaan_overseas_profit
  - ayaan_profit_remaining: ayaan_overseas_profit + ayaan_uk_profit - ayaan_fig_relief
  - ayaan_disallowed_loss: ayaan_overseas_loss
expected:
  yan_unrelieved: 5000
  ayaan_fig_relief: 200000
  ayaan_profit_remaining: 50000
  ayaan_disallowed_loss: 25000
```

## When to refuse or refer

Every referral above means **Check this point with one of our partner accountants.** Also use that referral for residence doubts, pre-SRT look-backs, coronavirus residence modifications, parliamentary membership, a child's first qualifying year/2025-26 age-condition commencement, trusts and transfer of assets abroad, pre-2025 domicile and remittance-basis charges, and any unverified classification or election. Do not confirm eligibility without the full residence history.

## Ask the client first

Read existing records before requesting missing facts:

1. Residence by tax year, age at the first qualifying year's start, first UK residence after the non-resident run, split/treaty years and any parliamentary membership.
2. Remittance-basis years and s809B claims versus automatic application; domicile/deemed-domicile history.
3. Old FIG by year/source/account/asset; remittance dates; foreign tax and which funds paid it; any planned designation or remittance.
4. Current foreign income/gains/losses, UK gains, property finance costs, pension contributions and competing reliefs.
5. Employment years versus receipt years, locations/workdays, deductions, bonuses and pre-2025 OWR history.
6. Assets held on 5 April 2017, original costs/values and UK presence from 6 March 2024 to 5 April 2025.
7. Residence over 20 years, planned departure, domicile on 30 October 2024 and any trust relationship.

## Sources

| Source and passage read | URL | Read on |
|---|---|---|
| Read for ITTOIA s845A, claims and restricted deduction | https://www.legislation.gov.uk/ukpga/2005/5/section/845A | 2026-11-26 |
| Read for ITTOIA s845B, complete eligibility test | https://www.legislation.gov.uk/ukpga/2005/5/section/845B | 2026-11-26 |
| Read for FA 2026 Sch 3, Parts 1-2 amendments and commencement | https://www.legislation.gov.uk/ukpga/2026/11/schedule/3 | 2026-11-26 |
| Read for RFIG44000, residence criteria, split/treaty years and unused years | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig44000 | 2026-11-26 |
| Read for ITTOIA s845H, qualifying categories | https://www.legislation.gov.uk/ukpga/2005/5/section/845H | 2026-11-26 |
| Read for ITTOIA s845I, disqualified categories | https://www.legislation.gov.uk/ukpga/2005/5/section/845I | 2026-11-26 |
| Read for RFIG45500, ordinary foreign asset gains and exclusions | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig45500 | 2026-11-26 |
| Read for RFIG42100, claim mechanics and quantification | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42100 | 2026-11-26 |
| Read for RFIG43000, allowances, losses, ANI and pensions; examples | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000 | 2026-11-26 |
| Read for ITTOIA s845C, loss conditions | https://www.legislation.gov.uk/ukpga/2005/5/section/845C | 2026-11-26 |
| Read for ITTOIA s845D, property finance costs | https://www.legislation.gov.uk/ukpga/2005/5/section/845D | 2026-11-26 |
| Read for ITTOIA s845F, pension-contribution relief ceiling | https://www.legislation.gov.uk/ukpga/2005/5/section/845F | 2026-11-26 |
| Read for EIM43555, new OWR scope, election/claim and offshore payment | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43555 | 2026-11-26 |
| Read for EIM43565, just/reasonable general-earnings apportionment | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43565 | 2026-11-26 |
| Read for EIM43560, eligibility and repeat periods | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43560 | 2026-11-26 |
| Read for EIM43600, relevant income, cumulative cap and Example 4 | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600 | 2026-11-26 |
| Read for EIM43605, transitional conditions and trailing earnings | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43605 | 2026-11-26 |
| Read for FA 2025 Sch 10, paras 1-2, 8-10, 12; special cases inspected and referred | https://www.legislation.gov.uk/ukpga/2025/8/schedule/10 | 2026-11-26 |
| Read for HS264, old FIG, TRF and filing routes | https://www.gov.uk/government/publications/remittance-basis-hs264-self-assessment-helpsheet/hs264-remittance-of-pre-6-april-2025-foreign-income-and-gains-and-the-temporary-repatriation-facility-trf | 2026-11-26 |
| Read for RDRM73400, charge, funding and Nida example | https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73400 | 2026-11-26 |
| Read for FA 2025 Sch 11, all five conditions, exceptions and election | https://www.legislation.gov.uk/ukpga/2025/8/schedule/11 | 2026-11-26 |
| Read for IHTA s6A, ordinary test and exclusions/tail | https://www.legislation.gov.uk/ukpga/1984/51/section/6A | 2026-11-26 |
| Read for HMRC IHT guidance, overseas-asset scope; special cases referred | https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident | 2026-11-26 |
| Read for RFIG42300, initial claim and amendment time limits | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig42300 | 2026-11-26 |
| Read for ITEPA s41M, election and qualifying-year deadline | https://www.legislation.gov.uk/ukpga/2003/1/section/41M | 2026-11-26 |
| Read for ITEPA s41P, claim and receipt-year deadline | https://www.legislation.gov.uk/ukpga/2003/1/section/41P | 2026-11-26 |
| Read for EIM43585, OWR time limits | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43585 | 2026-11-26 |
| Read for RDRM73320, TRF time limits, withdrawals and repayment exclusions | https://www.gov.uk/hmrc-internal-manuals/residence-domicile-and-remittance-basis/rdrm73320 | 2026-11-26 |
| Read for TMA s8, ordinary return dates; completed SA100-38 exact statutory read reused | https://www.legislation.gov.uk/ukpga/1970/9/section/8 | 2026-11-26 |
| Read for HMRC income-tax rates/allowance; completed SA100-09 and UKSA103 TAX-PA reads reused for unchanged England example | https://www.gov.uk/income-tax-rates | 2026-11-26 |
| Read for Ordinary HMRC late-payment interest; completed UKVAT114/SA100-47 read reused, effective date checked | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-22; applicability 2026-11-26 |

Not yet confirmed: no unresolved tax rule is offered for use. The specialist points explicitly referred above, including 2026/27 boxes and child commencement, are outside usable instructions in this Guide.
