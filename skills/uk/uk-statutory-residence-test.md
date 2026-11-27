---
name: uk-statutory-residence-test
description: "UK tax residence for 2026/27: automatic overseas and UK tests, sufficient ties, day counting and split-year cases. Includes historical worked cases and referrals for death, crew, treaty and related tax questions. Trigger on UK tax resident, SRT, 183 days, UK ties, leaving or arriving in the UK, split year and temporary non-residence."
version: 1.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# UK statutory residence test, 2026/27

The SRT determines individuals’ residence for income tax and capital gains tax, and for inheritance tax and corporation tax insofar as individuals’ residence is relevant. It concerns the UK as a whole, not residence in its constituent countries ([Sch 45 para 1](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/1)).

Check automatic overseas tests first, then automatic UK tests, then sufficient ties. Residence requires an automatic UK test with no automatic overseas test, or sufficient ties when neither automatic set is met. Otherwise the individual is non-resident ([Sch 45 para 5](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/5)).

The result is for the whole tax year; split-year treatment only relaxes this through particular charging rules. Test each year separately and obtain the residence history ([Sch 45 para 2](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/2)).

## Automatic tests

First overseas test: UK resident in at least one of the three preceding tax years, fewer than 16 UK days, and does not die in the year ([Sch 45 para 12](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/12)).

Second overseas test: UK resident in none of the three preceding tax years and fewer than 46 UK days ([Sch 45 para 13](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/13)).

Third overseas test: sufficient hours overseas over the tax year, no significant break, fewer than 31 days with more than 3 hours’ UK work, and fewer than 91 UK days excluding deemed days. Use the statutory hours calculation below ([Sch 45 para 14](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/14)).

First UK test: at least 183 UK days ([Sch 45 para 7](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/7)).

Second UK test: a UK home with presence on at least 30 days in the year, however briefly; a continuous 91-day period while it is a home, at least 30 days of that period in the year; throughout that period no overseas home, or each overseas home used on fewer than 30 days in the year. Count presence only while the property is a home. Test each UK home separately ([Sch 45 para 8](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/8)).

Third UK test: sufficient UK hours over a 365-day period, no significant break, some of the period in the tax year, more than 75% of days with more than 3 hours’ total work also having more than 3 hours’ UK work, and at least one such UK work day in both the period and the year ([Sch 45 para 9](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/9)).

Death in the year: the fourth UK test, fourth and fifth overseas tests and modified ties tables require separate conditions (paras 10, 15, 16, 20). Check this point with one of our partner accountants.

## Days, homes and work

A UK midnight counts as a day, subject to transit and exceptional circumstances. A day without a UK midnight does not count unless deemed ([Sch 45 para 22](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/22)).

Transit exception: arrival only as a passenger that day, departure the next day, and no activities substantially unrelated to the passage through the UK ([Sch 45 para 22](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/22)).

Exceptional circumstances: absent the circumstances the person would not be in the UK at midnight; circumstances beyond their control prevent leaving and they intend to leave as soon as permitted. Examples include war, civil unrest, natural disasters and sudden or life-threatening illness or injury. Exclude at most 60 days, counting forward from the start of the year; later days count. This is a days-spent rule, not a reduction of actual UK work days ([Sch 45 para 22](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/22)).

Deeming: at least three UK ties, more than 30 days present but not at midnight, and residence in at least one of the previous three tax years. Each qualifying day after the 30th counts. Do not use deeming to establish the three ties themselves, including the prior-year 90-day tie. Paragraph 14 excludes deemed days from its UK-day limit ([Sch 45 para 23](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/23)).

Home depends on permanence and stability, not ownership. A building, vehicle, vessel or other structure may qualify. A periodic holiday home or temporary retreat does not; continued ownership after moving out alone does not preserve a home ([Sch 45 para 25](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/25)).

Work means employment duties or trade activities. Travel counts where deductible or where work is actually done during it. Employment training must be provided or paid for by the employer and help with employment duties; trade training must be deductible. A voluntary post without a contract of service is not employment ([Sch 45 para 26](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/26)).

Work is located where actually done. Work during travel to or from the UK by air, sea or undersea tunnel is overseas from boarding the bound aircraft, ship or train until disembarkation, subject to special relevant-job rules ([Sch 45 para 27](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/27)).

Sufficient hours: disregard days with more than 3 hours’ work in the other territory. Exclude hours on those days from net hours in the territory tested. Start with 365 days for the UK test, or 365/366 for the overseas tax year, subtract disregarded days and permitted para 28 reductions. Divide the remaining reference period by 7, round down to whole weeks if above 1, or up to 1 if below 1. Net hours divided by this divisor must be at least 35. A simple contractual weekly average is insufficient ([Sch 45 para 14](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/14)).

Paragraph 28 reductions cover reasonable annual/parenting leave, illness or injury preventing reasonable work, and non-working days embedded between at least three consecutive leave days on each side. Do not subtract disregarded days twice. Fractional leave/sickness totals round down, without affecting the embedded-day rule ([Sch 45 para 28](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/28)).

An employment-change gap qualifies only if no work at all occurs between employments: maximum 15 days per gap and 30 in total in the ordinary hours calculation ([Sch 45 para 28](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/28)).

A significant break means at least 31 days with neither a day of more than 3 hours’ work in the tested territory nor a day that would have had that work but for annual, sick or parenting leave ([Sch 45 para 29](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/29)).

Cross-border vehicle, aircraft and ship crew: special relevant-job definitions, work-test exclusions and work-tie location rules apply (paras 9(3), 14(4), 30, 36). Check this point with one of our partner accountants.

## Sufficient ties

Each tie must be a different type. Prior UK residence in any of the three preceding tax years permits all five types; otherwise only family, accommodation, work and 90-day ties count ([Sch 45 para 31](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/31)).

Family: a UK-resident spouse/civil partner who is not separated, a person living together as married/civil partners, or a child under 18. Separation includes a court order, deed, or circumstances likely to be permanent. The relevant relationship must exist in the year ([Sch 45 para 32](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/32)).

No child tie if the parent sees the child in person in the UK on fewer than 61 days; if the child turns 18, use only the part before that birthday ([Sch 45 para 32](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/32)).

When deciding the family member’s residence, disregard a circular family tie back to the taxpayer. A child under 18 resident only because of full-time UK education is treated as non-resident if fewer than 21 UK days outside term-time. Half-term and other teaching breaks within a term count as term-time ([Sch 45 para 33](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/33)).

Accommodation: a UK place to live available continuously for at least 91 days in the year and at least one night there. Gaps shorter than 16 days are bridged. No ownership or legal occupation right is needed ([Sch 45 para 34](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/34)).

At a close relative’s home require at least 16 nights. Close relatives are parents, grandparents, siblings, children aged 18 or over and grandchildren aged 18 or over, including half-blood, marriage and civil partnership relationships ([Sch 45 para 34](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/34)).

Work tie: at least 40 days with more than 3 hours’ UK work ([Sch 45 para 35](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/35)).

90-day tie: more than 90 UK days in either of the two preceding tax years separately; do not add the years together ([Sch 45 para 37](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/37)).

Country tie, prior residents only: the UK has the greatest midnight count, including a tie for greatest with another country ([Sch 45 para 38](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/38)).

### Day thresholds (2026/27)

Only use these after all automatic tests fail; death cases are referred above.

Table A, resident in at least one of the preceding three years: 16–45 UK days needs at least 4 ties; 46–90 needs at least 3; 91–120 needs at least 2; more than 120 needs at least 1 ([Sch 45 para 18](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/18)).

Table B, resident in none of those years: 46–90 UK days needs all 4 ties; 91–120 needs at least 3; more than 120 needs at least 2 ([Sch 45 para 19](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/19)).

## Split-year treatment

First establish UK residence for the year. Split-year treatment requires a statutory case and changes only the relevant charging provisions; UK income can remain taxable during the overseas part. Test every potentially applicable case ([Sch 45 para 43](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/43)).

Case 1: starting full-time work overseas. These cases depend on period-specific work/day limits or partner and adjacent-year conditions. Check this point with one of our partner accountants.

Case 2: partner of someone starting full-time work overseas. These cases depend on period-specific work/day limits or partner and adjacent-year conditions. Check this point with one of our partner accountants.

Case 6: ceasing full-time work overseas. These cases depend on period-specific work/day limits or partner and adjacent-year conditions. Check this point with one of our partner accountants.

Case 7: partner of someone ceasing full-time work overseas. These cases depend on period-specific work/day limits or partner and adjacent-year conditions. Check this point with one of our partner accountants.

Case 3: resident the previous year; UK home at the start, then ceases all UK homes for the rest of the year; fewer than 16 UK days from that date; non-resident next year. At the end of six months from that date, sufficient overseas link means domestic tax residence there, presence there at every midnight throughout those six months, or all homes there. Overseas part starts the day the final UK home ceases ([Sch 45 para 46](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/46)).

Case 4: non-resident previous year; does not meet the UK-only-home test at the start, but begins meeting it and continues for the rest of the year; insufficient UK ties in the earlier part under the cut-back tables. Overseas part precedes that change. ([Sch 45 para 47](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/47)).

Case 5: non-resident previous year; a 365-day period starts on a day of more than 3 hours’ UK work in the year, sufficient UK hours, no significant break, at least 75% of days with more than 3 hours’ total work also having more than 3 hours’ UK work, and insufficient ties in the earlier part. Use the first qualifying period; unlike the third automatic UK test, exactly 75% qualifies ([Sch 45 para 48](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/48)).

Case 8: non-resident previous year; no UK home at the start; first UK home in the year continues for the rest of that year and all the next; insufficient ties in the earlier part; resident next year and next year not split. Overseas part precedes the first UK-home day ([Sch 45 para 51](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/51)).

Cases 4, 5 and 8: reduce each table day threshold by threshold × A / 12, with A the whole calendar months in the part beginning with the relevant start day. Do not reduce tie definitions; measure ties over the earlier part, but family-member residence remains a whole-year question. For arrival on 15 May 2026, June–March gives A = 10; 1–5 April 2027 is not a whole calendar month. Calendar month follows [Interpretation Act 1978 Schedule 1](https://www.legislation.gov.uk/ukpga/1978/30/schedule/1) ([Sch 45 para 51](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/51)).

Round the reduction, not the resulting threshold: first decimal 5 or more rounds up; otherwise down ([Sch 45 para 52](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/52)).

Priority: Case 1 over 2 over 3. For arrivals, Case 6 prevails unless Case 5 has an earlier split-year date; absent 6, the same applies to Case 7. Otherwise earliest date among 4, 5 and 8 wins; cases sharing that earliest date share priority. The split-year date is the final overseas day, not the first UK day ([Sch 45 para 55](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45/paragraph/55)).

## Related questions and referrals

Temporary non-residence and the tax charged on return: Check this point with one of our partner accountants.

Dual residence, treaty tie-breakers, personal representatives and trustees: Check this point with one of our partner accountants.

SA109 reporting, notification, filing and payment deadlines: Check this point with one of our partner accountants.

Late-filing, late-payment, inaccuracy and Making Tax Digital penalties and current interest: Check this point with one of our partner accountants.

Four-year FIG eligibility, age conditions, pre-2013 residence and claims: Check this point with one of our partner accountants.

Inheritance tax long-term residence, worldwide assets and departure tails: Check this point with one of our partner accountants.

For associated Guides use `uk-income-tax-sa100`, `uk-non-dom`, `uk-non-resident-sa109`, `uk-capital-gains-sa108`, `uk-scottish-income-tax`, `uk-foreign-tax-and-withholding`, `uk-to-uae-relocation-tax` and `uk-to-italy-flat-tax-relocation`.

## Worked examples

### Example 1: a leaver, the deeming rule and Table A

Anna was UK resident in each of 2023/24, 2024/25 and 2025/26, and spent 150 days in the UK in 2025/26. In 2026/27 her only home is in Spain and she is not full-time anywhere. She spends 40 midnights in the UK. She is also in the UK on 35 days on which she leaves before midnight. She stays 20 nights at her brother's London flat, which is available to her all year. She does more than 3 hours' UK work on 40 days. Her partner and children live in Spain. Assume none is UK resident, she survives the year, the brother’s flat is accommodation rather than her home, and no transit/exceptional-day adjustment applies. Assume ordinary work rather than a relevant crew job, and no qualifying 365-day UK work period overlapping the year. Spain has most of her midnights.

- **Ties.** Work: 40 days is at least 40, so yes. Accommodation: available all year (at least 91 days) and 20 nights at a close relative's home is at least 16, so yes. 90-day: 150 days in 2025/26 is more than 90, so yes. Family: no. Country: no. That is 3 ties.
- **Deeming rule.** She has at least 3 ties, more than 30 qualifying days, and was resident in the 3 previous years. So qualifying days 31 to 35 are deemed: 5 days. Her count is 40 + 5 = 45.
- **Automatic tests.** First overseas test: 45 is not less than 16, so it fails. The third overseas test fails (not full-time). First UK test: 45 is below 183. She has no UK home and no full-time UK work. No automatic test decides the year.
- **Table A.** 45 days is "more than 15 but not more than 45": at least 4 ties needed. She has 3. She is **not UK resident** for 2026/27. One additional countable midnight, with the 35 day visits and ties unchanged, gives 46 and would drop the requirement to 3 ties and make her resident.

```oa-check
name: Leaver with 40 midnights and 35 day visits, deeming rule and Table A (2026/27)
inputs:
  midnights: 40
  qualifying_days: 35
  uk_work_days: 40
  relative_flat_nights: 20
  days_prior_year: 150
  family_tie: 0
  country_tie: 0
steps:
  - work_tie: clamp(uk_work_days - 39, 0, 1)
  - accommodation_tie: clamp(relative_flat_nights - 15, 0, 1)
  - ninety_day_tie: clamp(days_prior_year - 90, 0, 1)
  - ties: work_tie + accommodation_tie + ninety_day_tie + family_tie + country_tie
  - deeming_applies: clamp(ties - 2, 0, 1) * clamp(qualifying_days - 30, 0, 1)
  - deemed_days: deeming_applies * max(qualifying_days - 30, 0)
  - uk_days: midnights + deemed_days
  - first_overseas_test_met: clamp(16 - uk_days, 0, 1)
  - first_uk_test_met: clamp(uk_days - 182, 0, 1)
  - ties_needed: 4 - clamp(uk_days - 45, 0, 1) - clamp(uk_days - 90, 0, 1) - clamp(uk_days - 120, 0, 1)
  - resident: clamp(ties - ties_needed + 1, 0, 1)
  - ties_needed_at_46: 4 - clamp(uk_days + 1 - 45, 0, 1) - clamp(uk_days + 1 - 90, 0, 1) - clamp(uk_days + 1 - 120, 0, 1)
  - resident_at_46: clamp(ties - ties_needed_at_46 + 1, 0, 1)
expected:
  ties: 3
  deemed_days: 5
  uk_days: 45
  first_overseas_test_met: 0
  first_uk_test_met: 0
  ties_needed: 4
  resident: 0
  resident_at_46: 1
```

### Example 2: an arriver, split year Case 8 and the cut-back Table B

Raj was not UK resident in any of the 10 years to 2025/26. On 1 October 2026 he takes a 2-year lease on a London flat and lives there; it stays his UK home for the rest of 2026/27 and all of 2027/28. He keeps his family home in Singapore, so Case 4 (UK-only home) does not apply, and he is not full-time in the UK, so Case 5 does not. Assume he survives the year, has no qualifying overseas work period or Case 6/7 partner circumstances, and no other split-year case applies. Over the whole year he spends 190 days in the UK (50 before 1 October and 140 after), so he is resident for 2026/27 under the first automatic UK test (at least 183 days). He is resident for 2027/28 and that year is not split.

- **Before the home: 6 April to 30 September 2026.** That is 25 + 31 + 30 + 31 + 31 + 30 = 178 days. He spends 50 midnights in the UK in that part, on work trips. He does more than 3 hours' UK work on 45 days (work tie). On those trips he stays in a serviced flat that is available to him from 1 June to 30 September (122 days, accommodation tie). It is a place to stay, not a home: assume its temporary arrangements lack the permanence/stability of a home and no UK home exists before 1 October; having a Singapore home alone does not prove that. On 6 April he has no UK home, as Case 8 requires. Assume no UK-resident family member and no more than 90 UK days in either 2024/25 or 2025/26: non-residence alone does not establish the latter. No family tie, no 90-day tie. That is 2 ties. The country tie does not count: he was resident in none of the 3 previous years, so Table B applies.
- **Cutting Table B back** (para 51(6)-(7)). A is the whole months from 1 October 2026 to 5 April 2027: October to March, 6. Each day number is reduced by the number times 6/12, rounded half up (para 52(5)). 45 × 6 / 12 = 22.5, which rounds to 23, so 45 becomes 22. 90 becomes 45. 120 becomes 60.
- **Result.** 50 days is "more than 45 but not more than 60" in the cut-back table: at least 3 ties needed. He has 2. (The uncut Table B would ask for all 4 at 50 days.) He does not have sufficient UK ties before 1 October, so **Case 8 applies**. The overseas part is 6 April to 30 September 2026; the UK part starts 1 October 2026.
- **Watch the rounding.** A plain half-even rounding would give 22 and a first band edge of 23. The statute rounds 0.5 up, so the edge is 22. At 23 days the statutory first band can be reached with all four ties; the half-even calculation would incorrectly place that day below the first band. This arithmetic alone does not decide every 23-day case.

```oa-check
name: Arriver, Case 8 split year, Table B cut back for 6 whole months (2026/27)
inputs:
  whole_months_from_arrival: 6
  days_before_home: 50
  ties_before_home: 2
steps:
  - overseas_part_days: 25 + 31 + 30 + 31 + 31 + 30
  - cut_45: floor(45 * whole_months_from_arrival / 12 + 0.5)
  - cut_90: floor(90 * whole_months_from_arrival / 12 + 0.5)
  - cut_120: floor(120 * whole_months_from_arrival / 12 + 0.5)
  - band_1: 45 - cut_45
  - band_2: 90 - cut_90
  - band_3: 120 - cut_120
  - ties_needed: 5 - clamp(days_before_home - band_1, 0, 1) - clamp(days_before_home - band_2, 0, 1) - clamp(days_before_home - band_3, 0, 1)
  - sufficient_ties: clamp(ties_before_home - ties_needed + 1, 0, 1)
  - case_8_ties_condition_met: 1 - sufficient_ties
expected:
  overseas_part_days: 178
  cut_45: 23
  band_1: 22
  band_2: 45
  band_3: 60
  ties_needed: 3
  sufficient_ties: 0
  case_8_ties_condition_met: 1
```

In the check, a `ties_needed` of 5 would mean no number of ties is enough (22 days or fewer under the cut-back Table B).

### Historical Case A: Anna before the additional day visits

In 2026/27 Anna has the same 2023/24, 2024/25 and 2025/26 residence history, 150 prior-year days, sole Spanish home, part-time consulting, 40 UK midnights, 20 nights in her brother’s flat available all year, and 40 days of more than 3 hours’ UK work. Assume no qualifying day visits, family tie or country tie, and the same no-home/no-full-time-work assumptions as Example 1. Three ties at 40 days fall short of four, so non-resident. At 46 midnights three ties suffice. At 39 UK work days the work tie disappears. Historical Case B adds the original 35 day visits and is Example 1 above. [Sch 45 paras 18, 23, 34–38](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45).

### Historical Case C: Raj’s 100-day alternative

Raj is non-resident in every year 2016/17–2025/26. In 2026/27 he has 100 UK midnights, a London flat rented all year, his Singapore family home used on more than 30 days, and 45 days of more than 3 hours’ UK work, part time and not full-time anywhere. His wife and children remain in Singapore. Assume they are not UK resident, the Singapore home is retained throughout, no more than 90 UK days in either 2024/25 or 2025/26, survival, no day adjustments, and at least one night in the available London flat. Automatic tests fail; accommodation and work give two ties, below Table B’s three at 100 days: non-resident. If his wife becomes UK resident and they are not separated, three ties make him resident. The original proposed FIG claim years 2026/27–2029/30 are preserved as a question, not a confirmed entitlement: Check this point with one of our partner accountants. [Sch 45 paras 8, 19, 32, 34, 35, 37](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45).

### Historical Case D: Tom leaves his final UK home

Tom has been UK resident for many years. His sole London home is used on far more than 30 days and retained until 30 September 2026, when he sells it and acquires and moves into his Dubai home. The April 91-day UK-home period with no overseas home establishes 2026/27 UK residence. Assume no automatic overseas test, no later UK home, no full-time overseas work or qualifying Case 1 partner, and no higher-priority case. From 30 September he has 10 UK days; Dubai is his only home at the end of six months; he is non-resident for 2027/28 on a separate assessment. Case 3 gives an overseas part starting 30 September 2026. [Sch 45 paras 8, 46, 53–54](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45).

### Historical Case E: Tom returns

Tom had sole UK residence in each of the seven tax years before 2026/27. Using Case D, his last sole-residence period ends 29 September 2026. Assume each intervening residence period lacks sole UK residence. He returns resident for all 2031/32, not split, with no treaty residence elsewhere. The temporary period is 30 September 2026–5 April 2031 inclusive: 1,649 days, less than five years, so the statutory temporary-non-residence definition applies. The original potential return-year charge on gains from pre-departure assets sold in Dubai requires asset-specific exclusions and current charging law: Check this point with one of our partner accountants. [Sch 45 paras 110–115](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45).

## Ask the client first

Obtain the full residence history; midnight and daytime travel log; work hours by location, leave and employment gaps; every home and place to stay with dates and nights; family members’ residence and days seeing minor children; previous and next-year circumstances; and treaty residence. Keep supporting travel, work and housing records. These are intake requests, not assumptions about a particular client.

## Sources

| Source and scope | URL | Read on |
|---|---|---|
| Finance Act 2013 Schedule 45, paras 1–56 and 110–115: tests, ties, counting, split years and residence periods | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 | 2026-11-27 |
| HMRC RDR3: order of tests, tables and split-year overview | https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3 | 2026-11-27 |
| Interpretation Act 1978 Schedule 1: calendar month | https://www.legislation.gov.uk/ukpga/1978/30/schedule/1 | 2026-11-27 |
