---
name: uk-statutory-residence-test
description: "Whether an individual is UK resident for tax year 2026/27 (6 April 2026 to 5 April 2027) under the statutory residence test in Finance Act 2013 Schedule 45. Covers the five automatic overseas tests, the four automatic UK tests, the sufficient ties test with the ties tables for leavers and arrivers, day counting (the midnight rule, transit days, exceptional circumstances, the deeming rule), split-year Cases 1 to 8 with their priority rules, and temporary non-residence. Trigger on: UK tax resident, statutory residence test, SRT, 183 days UK, UK ties test, automatic overseas test, split year UK, leaving the UK, arriving in the UK, UK day count, deeming rule, temporary non-residence. Out of scope: taxing foreign income under the 4-year FIG regime (uk-non-dom), what a non-resident pays on UK income (uk-non-resident-sa109), the return itself (uk-income-tax-sa100, uk-capital-gains-sa108)."
version: 1.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# The UK statutory residence test (SRT), tax year 2026/27

Tax year 2026/27 runs from 6 April 2026 to 5 April 2027. It has 365 days, because it holds no 29 February. The test is in Finance Act 2013, Schedule 45 ("Sch 45"), in force since 6 April 2013. The only amendments to the paragraphs used here are wording changes for opposite-sex civil partners (S.I. 2019/1458, from 2 December 2019). Finance Act 2020 s109 modified the test for coronavirus for 2019/20 and 2020/21 only; it matters for 2026/27 only through a look-back to those years (FIG, inheritance tax). HMRC's summary is guidance note RDR3 (updated 11 June 2026) and its manual is the Residence and FIG regime manual (RFIG20000 onwards). Where they simplify, the statute governs. The thresholds are counts of days, hours and ties. The law words them as "less than", "at least", "more than" or "not more than", and this skill keeps that wording, because one day either side changes the answer.

## Who this applies to

- **Individuals only.** The SRT decides whether an individual is resident or not resident in the UK for income tax and capital gains tax, and for inheritance tax and corporation tax "so far as the residence status of individuals is relevant to them" (Sch 45 para 1(4)).
- **The UK as a whole.** It does not decide residence in England, Wales, Scotland or Northern Ireland specifically (para 1(3)). Scottish taxpayer status is in `uk-scottish-income-tax`.
- **The basic rule** (paras 3-5). A person is UK resident for the year if the automatic residence test or the sufficient ties test is met. Otherwise they are not resident. The automatic residence test is met when the person meets at least one automatic UK test **and none** of the automatic overseas tests. So the overseas tests are checked first: one met overseas test ends the enquiry.
- **Whole-year result.** A person resident "for" a tax year is treated as resident at all times in it (para 2(3)). A split year relaxes that rule for the charging provisions only. It does not change the person's status for the year (para 40).
- **Personal representatives and trustees.** The split-year rules do not apply to personal representatives and apply only in part to trustees (para 41). Refer those cases.
- **Each year stands alone.** Test every tax year separately. The answer for a year depends on residence in the 3 years before it, so keep a residence history.

### Order of work

1. Fix the year and residence in each of the 3 previous tax years (decides which overseas test, which ties and which table apply).
2. Build a day log: each midnight, each day present but gone by midnight, each day with more than 3 hours' work in the UK or overseas, and each day at each home.
3. Automatic overseas tests. If one is met: not resident. Stop.
4. Automatic UK tests. If one is met: resident.
5. Otherwise, the sufficient ties test.
6. If resident and the person arrived or left in the year: test split-year Cases 1 to 8.
7. After-effects: temporary non-residence on return, and the 4-year FIG regime (`uk-non-dom`).

## Rates, bands and thresholds

The SRT holds no money amounts. These are its counts. All are in Sch 45 as in force for 2026/27 at https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 unless another source is named.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| First automatic overseas test: resident in 1 or more of the 3 previous years | Days in the UK less than 16, and P does not die in the year (para 12) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Second automatic overseas test: resident in none of the 3 previous years | Days in the UK less than 46 (para 13) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Third automatic overseas test: full-time work overseas | Average of 35 hours a week or more overseas; no significant break; UK work days (more than 3 hours) less than 31; UK days, leaving out deemed days, less than 91 (para 14) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Fourth and fifth automatic overseas tests (death in the year) | Less than 46 UK days with no residence in the 2 previous years, or full-time overseas work (paras 15-16) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| First automatic UK test | At least 183 days in the UK (para 7) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Second automatic UK test: UK home | Present at the UK home on at least 30 days in the year; a period of 91 consecutive days with that home, at least 30 of them in the year, with no overseas home or each overseas home used on fewer than 30 days (para 8) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Third automatic UK test: full-time work in the UK | 365-day period; average of 35 hours a week or more in the UK; no significant break; more than 75% of the work days (more than 3 hours) are UK work days (para 9) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Fourth automatic UK test (death in the year) | Resident in each of the 3 previous years by the automatic residence test, home in the UK at death (para 10) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| A work day | More than 3 hours' work on the day (paras 9, 14, 35) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Significant break from work | At least 31 days with no day of more than 3 hours' work, leave aside (para 29) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Gap between jobs taken out of the reference period | Up to 15 days per gap, 30 days in total (para 28(8)-(9)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Ties table for someone resident in 1 or more of the 3 previous years (Table A) | More than 15, not more than 45 days: at least 4 ties. More than 45, not more than 90: at least 3. More than 90, not more than 120: at least 2. More than 120: at least 1 (para 18) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Ties table for someone resident in none of the 3 previous years (Table B) | More than 45, not more than 90 days: all 4 ties. More than 90, not more than 120: at least 3. More than 120: at least 2 (para 19) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Work tie | At least 40 UK work days in the year (para 35) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| 90-day tie | More than 90 UK days in either or both of the 2 previous tax years (para 37) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Accommodation tie | Available for a continuous period of at least 91 days and at least 1 night spent there; a gap of fewer than 16 days does not break availability; at a close relative's home, at least 16 nights (para 34) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Family tie through a child under 18 | No tie if P sees the child in the UK on fewer than 61 days (para 32(3)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Child in UK full-time education | A child under 18 who is UK resident only because of UK full-time education is treated as not resident if fewer than 21 UK days outside term-time (para 33(3)-(4)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Deeming rule | Applies with at least 3 ties, more than 30 days present but not at midnight, and residence in 1 of the 3 previous years; days after the 30th count (para 23) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Exceptional circumstances | At most 60 days a year left out of the count (para 22(6)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Split year Case 3: leaving the UK home | Fewer than 16 UK days after the home ends; sufficient overseas link at the end of 6 months (para 46) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Split year Cases 1 and 6: permitted limits | 30 UK work days and 90 UK days, each reduced by the limit times whole months outside the period, divided by 12 (paras 44(8)-(9), 49(8)-(9)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Split year Cases 2 and 7: permitted limit | 90 UK days, reduced by 90 times whole months outside the part, divided by 12 (paras 45(9)-(10), 50(9)-(10)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Rounding the "appropriate number" | Round up if the first decimal is 5 or more, otherwise down (paras 20(4), 52(5)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| "Whole months" in the appropriate number | Calendar months wholly inside the part of the year (Interpretation Act 1978 s5 and Sch 1: "Month" means calendar month). HMRC, for the same words in para 20: "the whole of January, the whole of February and so on", with 6 to 30 April counting as the whole of April (RFIG20960) | 2026/27 | https://www.legislation.gov.uk/ukpga/1978/30/schedule/1 |
| Temporary non-residence | Sole UK residence in at least 4 of the 7 tax years before the year of departure; non-residence of 5 years or less (para 110) | 2026/27 | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| 4-year FIG regime entry | Not UK resident for each of the 10 tax years before the first qualifying year, and at least 10 years old at its start (ITTOIA 2005 s845B(1)(c)-(d)) | 2026/27 | https://www.legislation.gov.uk/ukpga/2005/5/section/845B |
| Inheritance tax: long-term UK resident | UK resident for at least 10 of the previous 20 tax years (IHTA 1984 s6A(1)) | 2026/27 | https://www.legislation.gov.uk/ukpga/1984/51/section/6A |

## The taxable base

The SRT does not tax anything. It decides whether the person's worldwide income and gains (resident) or only UK-source items (non-resident) are within UK tax. What it counts:

### Days spent in the UK (paras 22-24)

- **Midnight rule.** A day counts if the person is in the UK at the end of the day (para 22(1)). A day with no UK midnight does not count, subject to the deeming rule (para 23(1)-(2)).
- **Transit.** A day does not count if the person arrives as a passenger that day, leaves the next day, and in between does nothing "to a substantial extent unrelated" to passing through (para 22(3)).
- **Exceptional circumstances.** A day does not count if the person would have left but for exceptional circumstances beyond their control that stop them leaving, and they intend to leave as soon as those circumstances permit (para 22(4)). The statute's examples are national or local emergencies such as war, civil unrest or natural disasters, and a sudden or life-threatening illness or injury (para 22(5)). At most 60 such days a year. Counting forward from 6 April, the 61st and later such days count (para 22(6)). HMRC's guidance is at RFIG22210.
- **Deeming rule** (para 23(3)-(5)). If all three hold: at least 3 UK ties for the year; more than 30 "qualifying days" (in the UK during the day, gone by midnight); and UK residence in at least 1 of the 3 previous years. Then, counting forward from 6 April, every qualifying day after the 30th is treated as a UK day. In deciding whether the person has 3 ties for this purpose, deemed days are not used for the 90-day tie (para 23(5)). Deemed days are left out of the 91-day limit in the third automatic overseas test (para 14(2)) and the Case 1 and Case 6 overseas work criteria.
- **Order.** Apply transit, then exceptional circumstances, then the deeming rule, to build the count.

### Home (para 25)

A home can be a building, part of one, or "a vehicle, vessel or structure of any kind". It depends on how permanent or stable the arrangements are. A place used periodically as nothing more than a holiday home or temporary retreat is not a home. A former home is not still a home just because the person owns it after moving out, for example while selling or letting it. Ownership is not needed.

### Work (paras 26-30)

- Work is duties of an employment or activities of a trade. Deductible business travel and employer-paid training count as work time (para 26).
- Work is done where it is actually done. Work while travelling to or from the UK by air, sea or the Channel Tunnel is treated as done overseas, from boarding to leaving the craft (para 27).
- **Sufficient hours** (paras 9(2) and 14(3)). Step 1: take out "disregarded days", the days with more than 3 hours' work in the other country. Step 2: add up the hours worked in the country being tested on the remaining days ("net hours"). Step 3: start from 365 (or the period's days), subtract disregarded days and allowed leave, sick leave and job gaps (para 28): the "reference period". Step 4: divide by 7 and round down to a whole number (or up to 1 if below 1). Step 5: net hours divided by that number must be **35 or more**.
- Crew with a "relevant job" on a vehicle, aircraft or ship making at least 6 cross-border trips that begin or end in the UK cannot use the third automatic overseas test or the third automatic UK test (paras 9(3), 14(4), 30). Refer them.

### The four automatic UK tests (paras 6-10)

- **First:** at least 183 days in the UK.
- **Second (home):** the person has a UK home, is there on at least 30 days in the year (any length of time counts), and there is a run of 91 consecutive days while they have it, at least 30 of them in the year, throughout which they have no overseas home or use each overseas home on fewer than 30 days in the year. Each UK home is tested separately (para 8(8)).
- **Third (full-time work in the UK):** sufficient hours in the UK over a 365-day period, part of it in the year; no significant break; more than 75% of work days are UK work days; at least one UK work day in both the period and the year.
- **Fourth (death):** see the table above. Refer.

### The five automatic overseas tests (paras 11-16)

- **First:** resident in 1 or more of the 3 previous years, fewer than 16 UK days, does not die in the year.
- **Second:** resident in none of the 3 previous years, fewer than 46 UK days.
- **Third (full-time work overseas):** sufficient hours overseas over the year; no significant break; fewer than 31 UK work days; fewer than 91 UK days, leaving out deemed days.
- **Fourth and fifth:** death cases. Refer.

### The sufficient ties test (paras 17-20, 31-38)

Used only when no automatic test decides the year. Each tie must be of a different type (para 31(4)).

| Tie | Who it counts for | Definition |
|---|---|---|
| Family (para 32) | Leavers and arrivers | A spouse or civil partner (not separated), a partner living with the person as if married, or a child under 18, who is UK resident for the year. No tie through a child seen in the UK on fewer than 61 days. A child under 18 who is UK resident only because of full-time education in the UK is treated as non-resident if in the UK fewer than 21 days outside term-time (para 33). |
| Accommodation (para 34) | Leavers and arrivers | A place to live in the UK, available for a continuous 91 days or more in the year, with at least 1 night spent there. Gaps under 16 days are bridged. At a close relative's home (parent, grandparent, sibling, adult child or grandchild), at least 16 nights. |
| Work (para 35) | Leavers and arrivers | At least 40 days with more than 3 hours' work in the UK. |
| 90-day (para 37) | Leavers and arrivers | More than 90 UK days in either or both of the 2 previous tax years. |
| Country (para 38) | Leavers only (resident in 1 or more of the 3 previous years) | The UK is the country where the person spends the most midnights in the year, or ties for most. |

Read the day count against Table A (resident in 1 or more of the 3 previous years) or Table B (resident in none) in the rates table. Below 16 days (Table A) or 46 days (Table B) the automatic overseas tests have already settled the year, except on death. On death, the tables are cut back (para 20). Refer.

### Split year: Cases 1 to 8 (paras 39-56)

A year can be split only if the person is UK resident for it (para 43). Test every Case that could apply; RDR3 says the same. The "overseas part" is taxed broadly as if non-resident under the special charging rules; the rest is the "UK part" (para 56).

| Case | Main conditions | Overseas part |
|---|---|---|
| 1. Starting full-time work overseas (para 44) | Resident last year. A period from a day of overseas work to 5 April meets the overseas work criteria (sufficient hours, no significant break, UK work days and UK days within the reduced 30 and 90 limits). Not resident next year **because** the third automatic overseas test is met. | From the start of that period (the longest, if several) |
| 2. Partner of a Case 1 person (para 45) | Resident last year. Moves overseas to live with a partner in Case 1 (this year or last). From the deemed departure day: no UK home, or more time in the overseas home; UK days within the reduced 90 limit. Not resident next year. | From the deemed departure day |
| 3. Ceasing to have a UK home (para 46) | Resident last year. Had a UK home on 6 April, stops having any UK home on a day in the year. From that day, fewer than 16 UK days. Not resident next year. At the end of 6 months from that day, a sufficient link overseas: tax resident there, present there at every midnight, or only home(s) there. | From the day the last UK home ends |
| 4. Starting to have a home in the UK only (para 47) | Not resident last year. From a day in the year, the person's only home or homes are in the UK for the rest of the year. Before that day, not sufficient ties (tables cut back pro rata). | Before that day |
| 5. Starting full-time work in the UK (para 48) | Not resident last year. A 365-day period starting with a UK work day in the year: sufficient UK hours, no significant break, **at least 75%** of work days in the UK. Before it, not sufficient ties (tables cut back). | Before the period starts (the first, if several) |
| 6. Ceasing full-time work overseas (para 49) | Not resident last year **because** of the third automatic overseas test, and resident in 1 or more of the 4 years before that. A period from 6 April to a day of overseas work meets the overseas work criteria. Resident next year. | To the end of that period (the longest, if several) |
| 7. Partner of a Case 6 person (para 50) | Not resident last year. Moves to the UK to live with a partner in Case 6 (this year or last). Before the deemed arrival day: no UK home, or more time overseas; UK days within the reduced 90 limit. Resident next year. | Before the deemed arrival day |
| 8. Starting to have a UK home (para 51) | Not resident last year. No UK home on 6 April; from a day in the year, a UK home for the rest of the year and all of next year. Before that day, not sufficient ties (tables cut back). Resident next year, and next year is not a split year. | Before the UK home starts |

- **Cutting the tables back** (Cases 4, 5, 8). Each day number in the first column of Table A or B is reduced by: that number times A, divided by 12, where A is the whole months in the part of the year beginning with the arrival day (paras 47(7), 48(6), 51(7)). A whole month is a calendar month (Interpretation Act 1978 Sch 1). Arriving on 15 May 2026, A is 10 (June to March); 1 to 5 April 2027 is not a whole month. The tie definitions themselves (40 work days, 91 days of availability, 61 days with a child) are not reduced. The family-member residence check still uses the whole year (paras 47(8), 48(7), 51(8)).
- **Priority.** Case 1 beats Cases 2 and 3; Case 2 beats Case 3 (para 54). Among arrival Cases: Case 6 wins unless Case 5 also applies with an earlier split year date; the same with Case 7 where Case 6 does not apply. Otherwise, among Cases 4, 5 and 8, the earliest split year date wins (para 55). The split year date is the last day of the overseas part (para 55(2)).
- **Partner** means a spouse, civil partner, or someone living with the person as if married (para 52(4)).

## Deadlines and filing

- **Where residence is reported.** On the SA109 pages ("Residence and foreign income and gains (FIG) regime etc") filed with the SA100 Self Assessment return. Split-year claims and FIG claims go there too. The latest SA109 on GOV.UK is the 2026 edition, for 2025/26 (page updated 28 September 2026). The 2026/27 edition is not yet published.
- **Notify chargeability.** A person with no return notice must tell HMRC within 6 months from the end of the tax year (TMA 1970 s7). For 2026/27 that is 5 October 2027.
- **2026/27 return** (TMA 1970 s8(1D)): paper by 31 October 2027; online by 31 January 2028. A later notice from HMRC gives 3 months (s8(1F)-(1G)).
- **Balancing payment** for 2026/27: 31 January 2028 (TMA 1970 s59B(4)).
- **2025/26 returns, due now** (GOV.UK deadlines page): paper by 31 October 2026, online by 31 January 2027, pay by 31 January 2027.
- **Records.** Keep the day log with evidence for each midnight (travel tickets, passport stamps, card statements), work diaries with hours, and evidence about each home. HMRC can ask for them in an enquiry.

## Penalties and interest

There is no SRT-specific penalty. A wrong residence answer leads to a wrong or late return, and the return penalties apply.

- **Late filing** (FA 2009 Sch 55): £100 (para 3); after 3 months, £10 a day for up to 90 days (para 4); after 6 months, the greater of 5% of the tax and £300 (para 5); after 12 months, another 5% or £300, or more where information was withheld deliberately (para 6).
- **Late payment** (GOV.UK penalties page): 5% of the tax unpaid at 30 days, 6 months and 12 months.
- **Errors** (FA 2007 Sch 24 para 4): for a UK-only (category 1) inaccuracy, 30% of the potential lost revenue if careless, 70% if deliberate, 100% if deliberate and concealed. Category 2 and 3 inaccuracies, which involve offshore matters, run higher: 45%/105%/150% and 60%/140%/200%.
- **Making Tax Digital for Income Tax.** A person who must use MTD for Income Tax from 6 April 2026 gets the new penalties for the 2026/27 return instead: penalty points for late submission, and late payment penalties of 3% of the tax owed at day 15 and 3% more at day 30, plus 10% a year from day 31 for up to 2 years (no penalty up to 15 days late, and none at day 15 in the first year). The current penalties still apply to their 2025/26 return (GOV.UK, Penalties for Making Tax Digital for Income Tax).
- **Late payment interest:** 7.75% from 9 January 2026 (Bank Rate plus 4% from 6 April 2025), per HMRC's interest rates page.

## Cross-border points

- **Treaties.** The SRT decides UK residence only. If another country also treats the person as resident, the tie-breaker in the double taxation agreement decides treaty residence. Split-year treatment does not affect treaty residence (para 42). Refer dual-resident cases.
- **Temporary non-residence** (paras 109-115). A person is temporarily non-resident if: they had sole UK residence for a residence period; the next period or periods are not sole UK residence; at least 4 of the 7 tax years before the year of departure were years (or split years with a UK part) of sole UK residence; and the temporary period of non-residence is 5 years or less (para 110). "Sole UK residence" means UK resident with no time as treaty non-resident (para 112). A residence period is a whole non-split year, or the UK or overseas part of a split year (para 111). The period runs from the end of the last sole-residence period to the start of the next one (para 113).
  - **Effect.** Gains on disposals in the temporary period of non-residence are treated as accruing in the period of return, unless the asset is excluded by TCGA 1992 s1N (TCGA 1992 s1M(1)). Treaties do not stop that charge (s1M(4)). RDR3 lists other income caught in the year of return, such as some pension payments, close company distributions and chargeable event gains. Detail is at RFIG21500.
  - RDR3 adds that the period must be longer than 5 years, "that is 5 years plus one day", to escape these rules.
- **The 4-year FIG regime.** From 6 April 2025 the remittance basis was replaced by a residence-based regime (GOV.UK). A person is a "qualifying new resident" for a year if UK resident for it and not UK resident for each of the 10 tax years before it, and is at least 10 years old at its start (ITTOIA 2005 s845B(1)). They also qualify for the next 3 tax years in which they are UK resident (s845B(2)-(3)). Every one of those residence answers is an SRT answer. The age-10 condition was inserted by Finance Act 2026 Sch 3 para 3, in force from Royal Assent on 18 March 2026 with no separate commencement rule, so it applies to 2026/27. HMRC: "You cannot roll any unused years over to a later year." The claim, its effect and the allowances it costs are in `uk-non-dom`. The SRT applies from 2013/14. A 10-year look-back that reaches 2012/13 or earlier uses the old residence rules, which this skill does not cover. Refer those cases.
- **Inheritance tax.** From 6 April 2025 worldwide assets are within inheritance tax for a "long-term UK resident": UK resident for at least 10 of the previous 20 tax years (IHTA 1984 s6A(1)), with exits after 10 consecutive non-resident years or a shorter tail (s6A(2)-(3)). Residence for 2013/14 onward is the SRT answer (s6A(5)), and the SRT applies to inheritance tax so far as individuals' residence is relevant (Sch 45 para 1(4)). The test and its tail are in `uk-non-dom`.
- **What non-residents still pay** on UK income and UK land: `uk-non-resident-sa109`. Planned moves: `uk-to-uae-relocation-tax`, `uk-to-italy-flat-tax-relocation`. Foreign tax credit relief for residents: `uk-foreign-tax-and-withholding`.

## Worked examples

### Example 1: a leaver, the deeming rule and Table A

Anna was UK resident in each of 2023/24, 2024/25 and 2025/26, and spent 150 days in the UK in 2025/26. In 2026/27 her only home is in Spain and she is not full-time anywhere. She spends 40 midnights in the UK. She is also in the UK on 35 days on which she leaves before midnight. She stays 20 nights at her brother's London flat, which is available to her all year. She does more than 3 hours' UK work on 40 days. Her partner and children live in Spain. Spain has most of her midnights.

- **Ties.** Work: 40 days is at least 40, so yes. Accommodation: available all year (at least 91 days) and 20 nights at a close relative's home is at least 16, so yes. 90-day: 150 days in 2025/26 is more than 90, so yes. Family: no. Country: no. That is 3 ties.
- **Deeming rule.** She has at least 3 ties, more than 30 qualifying days, and was resident in the 3 previous years. So qualifying days 31 to 35 are deemed: 5 days. Her count is 40 + 5 = 45.
- **Automatic tests.** First overseas test: 45 is not less than 16, so it fails. The third overseas test fails (not full-time). First UK test: 45 is below 183. She has no UK home and no full-time UK work. No automatic test decides the year.
- **Table A.** 45 days is "more than 15 but not more than 45": at least 4 ties needed. She has 3. She is **not UK resident** for 2026/27. One more day in the UK (46) would drop the requirement to 3 ties and make her resident.

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

Raj was not UK resident in any of the 10 years to 2025/26. On 1 October 2026 he takes a 2-year lease on a London flat and lives there; it stays his UK home for the rest of 2026/27 and all of 2027/28. He keeps his family home in Singapore, so Case 4 (UK-only home) does not apply, and he is not full-time in the UK, so Case 5 does not. Over the whole year he spends 190 days in the UK (50 before 1 October and 140 after), so he is resident for 2026/27 under the first automatic UK test (at least 183 days). He is resident for 2027/28 and that year is not split.

- **Before the home: 6 April to 30 September 2026.** That is 25 + 31 + 30 + 31 + 31 + 30 = 178 days. He spends 50 midnights in the UK in that part, on work trips. He does more than 3 hours' UK work on 45 days (work tie). On those trips he stays in a serviced flat that is available to him from 1 June to 30 September (122 days, accommodation tie). It is a place to stay, not a home: his home is in Singapore, so on 6 April he has no UK home, as Case 8 requires. No family tie, no 90-day tie. That is 2 ties. The country tie does not count: he was resident in none of the 3 previous years, so Table B applies.
- **Cutting Table B back** (para 51(6)-(7)). A is the whole months from 1 October 2026 to 5 April 2027: October to March, 6. Each day number is reduced by the number times 6/12, rounded half up (para 52(5)). 45 × 6 / 12 = 22.5, which rounds to 23, so 45 becomes 22. 90 becomes 45. 120 becomes 60.
- **Result.** 50 days is "more than 45 but not more than 60" in the cut-back table: at least 3 ties needed. He has 2. (The uncut Table B would ask for all 4 at 50 days.) He does not have sufficient UK ties before 1 October, so **Case 8 applies**. The overseas part is 6 April to 30 September 2026; the UK part starts 1 October 2026.
- **Watch the rounding.** A plain half-even rounding would give 22 and a first band edge of 23. The statute rounds 0.5 up, so the edge is 22. That does not change Raj's result, but it decides a case with exactly 23 days.

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

## Ask the client first

1. Were you UK resident in each of the 3 tax years before 2026/27? If you arrived recently, were you non-resident in each of the 10 years before your first UK year? (Decides the overseas test, the ties, the table and FIG.)
2. A dated log of every arrival and departure: where were you at midnight each night, and on which days were you in the UK only during the day? Were any UK nights caused by an emergency or sudden illness?
3. Which days did you work more than 3 hours in the UK, and overseas? Weekly hours, leave and any 31-day gap without work.
4. Every home you had in the year, UK and overseas, with dates and days present. Any other UK place you could stay (a relative's home, a flat kept for you), how long it was available and how many nights you spent there.
5. Is your spouse, civil partner or partner UK resident for the year? Any child under 18 in the UK, and on how many days did you see them there?
6. Did you arrive or leave during the year, on what date, and why (job, partner's job, home)? Were you UK resident for most of the 7 years before an earlier departure, and are you treaty-resident anywhere else?

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2013, Schedule 45 (paras 1-56, 109-115) | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 | 2026-10-24 |
| HMRC, RDR3 Statutory Residence Test guidance note (updated 11 June 2026) | https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3 | 2026-10-24 |
| HMRC Residence and FIG regime manual, RFIG20720 (deeming rule) | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig20720 | 2026-10-24 |
| HMRC Residence and FIG regime manual, RFIG21500 (temporary non-residence) | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig21500 | 2026-10-24 |
| Taxation of Chargeable Gains Act 1992, s1M (temporary non-residents) | https://www.legislation.gov.uk/ukpga/1992/12/section/1M | 2026-10-24 |
| ITTOIA 2005, s845A and s845B (FIG regime claim and qualifying new resident) | https://www.legislation.gov.uk/ukpga/2005/5/section/845B | 2026-10-24 |
| GOV.UK, Check if you can claim the 4-year foreign income and gains regime | https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime | 2026-10-24 |
| Taxes Management Act 1970, s7, s8 and s59B | https://www.legislation.gov.uk/ukpga/1970/9/section/8 | 2026-10-24 |
| Finance Act 2009, Schedule 55, paras 3-6 (late filing penalties) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-10-24 |
| Finance Act 2007, Schedule 24, para 4 (inaccuracy penalties) | https://www.legislation.gov.uk/ukpga/2007/11/schedule/24/paragraph/4 | 2026-10-24 |
| GOV.UK, Self Assessment tax returns: deadlines | https://www.gov.uk/self-assessment-tax-returns/deadlines | 2026-10-24 |
| GOV.UK, Self Assessment tax returns: penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-10-24 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |
| Interpretation Act 1978, s5 and Schedule 1 ("Month" means calendar month) | https://www.legislation.gov.uk/ukpga/1978/30/schedule/1 | 2026-10-24 |
| HMRC Residence and FIG regime manual, RFIG20960 (whole months) | https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig20960 | 2026-10-24 |
| Finance Act 2026, Schedule 3 para 3 (age-10 condition in s845B) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/3 | 2026-10-24 |
| Finance Act 2020, s109 (coronavirus modifications, 2019/20 and 2020/21) | https://www.legislation.gov.uk/ukpga/2020/14/section/109 | 2026-10-24 |
| Inheritance Tax Act 1984, s6A (long-term UK resident) | https://www.legislation.gov.uk/ukpga/1984/51/section/6A | 2026-10-24 |
| GOV.UK, Penalties for Making Tax Digital for Income Tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-10-24 |
| GOV.UK, SA109 Residence and FIG regime etc (page updated 28 September 2026) | https://www.gov.uk/government/publications/self-assessment-residence-remittance-basis-etc-sa109 | 2026-10-24 |

Not yet confirmed: whether the age-10 condition in ITTOIA 2005 s845B(1)(d), in force from 18 March 2026, also governs claims for 2025/26 (FA 2026 Sch 3 para 3 has no commencement rule of its own; 2026/27 is covered either way).

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
