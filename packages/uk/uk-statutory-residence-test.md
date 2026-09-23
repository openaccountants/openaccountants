---
name: uk-statutory-residence-test
description: "Use this skill for any question about UK tax residency. Trigger on: \"UK tax resident\", \"statutory residence test\", \"SRT UK\", \"183 days UK\", \"leave UK tax\", \"UK ties test\", \"automatic overseas test UK\", \"split year UK\", \"ceasing UK residency\", \"UK non-resident\", \"UK resident abroad\", \"how many days UK tax\", \"UK day count rules\", \"UK resident status\". Covers the Statutory Residence Test (SRT) in full — automatic tests, sufficient ties, and split-year treatment."
version: 1.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# The UK statutory residence test

Whether an individual is resident in the UK for a tax year, worked out from counted days, counted hours and counted ties. Figures are for tax year 2026. In the UK that means the tax year from 6 April 2026 to 5 April 2027, which HMRC writes as 2026 to 2027. The test holds almost no money amounts: nearly every threshold in it is a number of days, a number of hours or a number of ties. Finance Act 2013, Schedule 45 is read here as it stood in force on 19 September 2026, and HMRC's guidance note RDR3 as last updated on 11 June 2026.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| What the test decides | Whether an individual is resident or not resident in the UK for income tax and capital gains tax, and for inheritance tax and corporation tax so far as an individual's residence matters to them (paragraph 1) |
| What it does not decide | Residence in England, Wales, Scotland or Northern Ireland specifically, rather than the UK as a whole (paragraph 1(3)) |
| In force from | 6 April 2013 |
| Tax year | 6 April to 5 April. Tax year 2026 runs from 6 April 2026 to 5 April 2027 |
| Primary legislation | Finance Act 2013, Schedule 45: https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| HMRC guidance | RDR3 Statutory Residence Test notes: https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3 |
| Tax authority | HM Revenue and Customs |
| Where status is reported | Supplementary pages SA109 of the Self Assessment return: https://www.gov.uk/government/publications/self-assessment-residence-remittance-basis-etc-sa109 |
| Verified by | Pending. A UK accountant's sign-off is required |

## Section 2: The SRT, three-part structure

Each tax year is looked at separately. A person can be resident in one year and not the next. A person who is resident for a year is treated as resident at all times in that year (paragraph 2(3)), unless the year is a split year (Section 6).

The statute sets the order, and the order matters:

1. **Automatic overseas tests** (Section 3). Meeting any one of them makes the person **not** UK resident for the year. Test these first: paragraph 5 says the automatic residence test is met only if the person meets at least one automatic UK test **and none** of the automatic overseas tests.
2. **Automatic UK tests** (Section 4). Meeting at least one of them, with no automatic overseas test met, makes the person UK resident for the year.
3. **Sufficient ties test** (Section 5). Reached only when none of the automatic UK tests and none of the automatic overseas tests is met (paragraph 17(1)).

If neither the automatic residence test nor the sufficient ties test is met, the person is not UK resident for that year (paragraph 4). RDR3 gives one shortcut: "If you’ve been in the UK for 183 or more days you’ll be a UK resident. There is no need to consider any other tests." One edge case: the third automatic overseas test counts UK days without the days added by the deeming rule (paragraph 14(2)), so a total that reaches 183 only through deemed days needs that test checked (our reading of para 14(2); confirm). https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3

## Section 3: Automatic overseas tests (not UK resident)

There are 5 automatic overseas tests (paragraph 11). The fourth and fifth apply only where the person dies in the year. Meeting any one of them makes the person not UK resident for the whole year.

| Test | Condition, in the statute's own terms | Where |
| --- | --- | --- |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| First automatic overseas test | P was resident in the UK for one or more of the 3 tax years preceding year X, the number of days in year X that P spends in the UK is **less than 16**, and P does not die in year X | Paragraph 12 |
| Second automatic overseas test | P was resident in the UK for **none** of the 3 tax years preceding year X, and the number of days that P spends in the UK in year X is **less than 46** | Paragraph 13 |
| Third automatic overseas test | P works sufficient hours overseas across year X, there are no significant breaks from overseas work, the number of days in year X on which P does more than 3 hours' work in the UK is **less than 31**, and the number of days spent in the UK (leaving out days treated as spent here only by the deeming rule) is **less than 91** | Paragraph 14 |
| Fourth automatic overseas test (death only) | P dies in year X, P was resident in the UK for neither of the 2 tax years preceding year X (or the alternative in paragraph 15(2) applies), and P spends **less than 46** days in the UK in year X | Paragraph 15 |
| Fifth automatic overseas test (death only) | P dies in year X, P was resident for neither of the 2 preceding tax years because the third automatic overseas test was met for each of them (or the alternative in paragraph 16(2) applies), and P would meet the third automatic overseas test for year X read with the modifications in paragraph 16(3) | Paragraph 16 |

- **"Sufficient hours overseas" is a calculation, not a 35-hour week.** Paragraph 14(3): identify disregarded days (days with more than 3 hours' work in the UK); add the hours worked overseas, ignoring hours worked on disregarded days, to get net overseas hours; subtract from 365 (366 if the year includes 29 February) the disregarded days and the leave and gap days allowed by paragraph 28, to get the reference period; divide the reference period by 7 and round (down if the answer is more than 1 and not whole, up to 1 if it is less than 1); then divide net overseas hours by that number. If the answer is 35 or more, P works sufficient hours overseas. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Significant break from overseas work** (paragraph 29(2)): at least 31 days go by and not one of them is a day on which P does more than 3 hours' work overseas, or would have done so but for annual leave, sick leave or parenting leave. A significant break means the test fails. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Who it does not cover** (paragraph 14(4)): the third automatic overseas test does not apply to a person who has a relevant job on board a vehicle, aircraft or ship at any time in year X and makes at least 6 cross-border trips in that job in the year that begin in the UK, end in the UK, or both. RDR3 adds that the test does not apply to voluntary workers. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Day in the UK**: present in the UK at the end of the day. See Section 7.

## Section 4: Automatic UK tests (UK resident)

There are 4 automatic UK tests (paragraph 6). Meeting one makes the person UK resident, unless an automatic overseas test is also met, in which case the automatic overseas test wins (paragraph 5).

| Test | Condition, in the statute's own terms | Where |
| --- | --- | --- |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| First automatic UK test | P spends **at least 183 days** in the UK in year X | Paragraph 7 |
| Second automatic UK test (the home test) | P has a home in the UK during all or part of year X; P spends a sufficient amount of time in that home, meaning at least 30 days in the year when P is present there for at least some of the time; and there is at least one period of 91 consecutive days, occurring while P has that home and with at least 30 of those days falling in year X, throughout which either P has no home overseas or P is present in each overseas home on fewer than 30 days in year X | Paragraph 8 |
| Third automatic UK test (the work test) | P works sufficient hours in the UK over a period of 365 days with no significant breaks from UK work; all or part of that period falls in year X; more than 75% of the total number of days in the 365-day period on which P does more than 3 hours' work are days on which P does more than 3 hours' work in the UK; and at least one day falling in both that period and year X is a day on which P does more than 3 hours' work in the UK | Paragraph 9 |
| Fourth automatic UK test (death only) | P dies in year X; P was resident in the UK by virtue of meeting the automatic residence test for each of the previous 3 tax years; the tax year before year X would not be a split year; when P died, either P's home was in the UK or P had more than one home and at least one of them was in the UK; and P did not spend a sufficient amount of time in any overseas home in year X | Paragraph 10 |

- The second automatic UK test is applied to each UK home separately, and is met if it is met for at least one of them (paragraph 8(8)). The 30 days can be in aggregate, consecutive or intermittent, and presence for any length of time on a day counts (paragraph 8(4) to (6)). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- "Sufficient hours in the UK" uses the same five steps as the overseas calculation, applied to UK hours over the 365-day period, and again needs an answer of 35 or more (paragraph 9(2)). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- Significant break from UK work (paragraph 29(1)): at least 31 days go by and not one of them is a day on which P does more than 3 hours' work in the UK, or would have done so but for annual leave, sick leave or parenting leave. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- The third automatic UK test does not apply to a person with a relevant job on board a vehicle, aircraft or ship who makes at least 6 qualifying cross-border trips in year X (paragraph 9(3)). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- The fourth automatic UK test is a home test for a deceased person. It carries no day count of its own.

## Section 5: Sufficient ties test

Reached only when no automatic test decides the year. Count the ties, then read the number of days spent in the UK against the table for the person's prior residence history.

**Which ties count** (paragraph 31). If P was resident in the UK for one or more of the 3 tax years preceding year X, all five ties count. Otherwise only the first four count, and there is no country tie. Each tie counted must be of a different type. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45

| Tie | Condition, in the statute's own terms | Where |
| --- | --- | --- |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Family tie | At any time in year X a relevant relationship exists between P and someone who is UK resident for year X: husband and wife or civil partners and not separated; a couple living together as if they were a married couple or civil partners; or a child of P's under the age of 18. There is no family tie through a child if P sees the child in the UK on fewer than 61 days in year X, or, if the child turns 18 during year X, in the part of the year before that day | Paragraph 32 |
| Family tie, the schoolchild rule | A child of P's under 18 who is in full-time education in the UK, and who is resident in the UK for year X but would not be so resident if the time spent in full-time education in the UK (meaning term-time) were disregarded, is treated as not resident if the number of days that child spends in the UK in the part of year X outside term-time is less than 21. Half-term and other breaks within a term count as term-time. A family tie the family member has with P only because of their relationship with P is also disregarded when deciding whether that family member is UK resident (paragraph 33(2)) | Paragraph 33 |
| Accommodation tie | P has a place to live in the UK, it is available to P during year X for a continuous period of at least 91 days, and P spends at least one night there in that year. A gap of fewer than 16 days between periods of availability is treated as continued availability. If the place is the home of a close relative, P must spend a total of at least 16 nights there. A close relative is a parent or grandparent, a brother or sister, or a child or grandchild aged 18 or over, including by half blood, marriage or civil partnership. Accommodation can be available to P even if P holds no interest in it and has no legal right to occupy it | Paragraph 34 |
| Work tie | P works in the UK for at least 40 days in year X, continuously or intermittently. A day counts if P does more than 3 hours' work in the UK on that day | Paragraph 35 |
| 90-day tie | P has spent more than 90 days in the UK in the tax year preceding year X, in the tax year before that one, or in each of those tax years separately | Paragraph 37 |
| Country tie | The country in which P meets the midnight test for the greatest number of days in year X is the UK. If two or more countries tie for the greatest number and one of them is the UK, P has the tie. It counts only for a person resident in the UK in one or more of the 3 preceding tax years | Paragraph 38 |

**Table A: P was resident in the UK for one or more of the 3 tax years preceding year X** (paragraph 18).

| Days spent by P in the UK in year X | Number of ties that are sufficient | Where |
| --- | --- | --- |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| More than 15 but not more than 45 | At least 4 | Paragraph 18 |
| More than 45 but not more than 90 | At least 3 | Paragraph 18 |
| More than 90 but not more than 120 | At least 2 | Paragraph 18 |
| More than 120 | At least 1 | Paragraph 18 |

**Table B: P was resident in the UK for none of the 3 tax years preceding year X** (paragraph 19).

| Days spent by P in the UK in year X | Number of ties that are sufficient | Where |
| --- | --- | --- |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| More than 45 but not more than 90 | All 4 | Paragraph 19 |
| More than 90 but not more than 120 | At least 3 | Paragraph 19 |
| More than 120 | At least 2 | Paragraph 19 |

- RDR3 prints the same two tables and writes the bands as "16 to 45", "46 to 90", "91 to 120" and "Over 120". The wording above is the statute's. https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3
- Neither table has a top row for 183 days or more, and neither has a bottom row below the first band. Those cases never reach this test: 183 days meets the first automatic UK test, and a low day count meets the first or second automatic overseas test. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- Where P dies in year X, paragraph 18 is read without the words "More than 15 but", and if the death is before 1 March in year X each day number in the first column of both tables is reduced by an appropriate number worked out from the number of whole months in year X after the month in which P dies, rounded to the nearest whole number (paragraph 20; the page does not print the formula itself). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45

## Section 6: Split year treatment

A split year does **not** change residence status. The person is UK resident for the whole year. The split only relaxes the rule that treats them as resident at all times in it, and when and how that rule is relaxed is set by the special charging rules; subject to those rules, nothing in the split year rules alters residence status or tax liability (paragraph 40). A year can only be a split year if the person is UK resident for it (paragraph 43). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45

There are 8 cases. Cases 1 to 3 involve an actual or deemed departure from the UK. Cases 4 to 8 involve an actual or deemed arrival (paragraph 43).

| Case | What it covers, in the statute's own words | Where |
| --- | --- | --- |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/2013/29/schedule/45 |
| Case 1 | Starting full-time work overseas | Paragraph 44 |
| Case 2 | The partner of someone starting full-time work overseas | Paragraph 45 |
| Case 3 | Ceasing to have a home in the UK | Paragraph 46 |
| Case 4 | Starting to have a home in the UK only | Paragraph 47 |
| Case 5 | Starting full-time work in the UK | Paragraph 48 |
| Case 6 | Ceasing full-time work overseas | Paragraph 49 |
| Case 7 | The partner of someone ceasing full-time work overseas | Paragraph 50 |
| Case 8 | Starting to have a home in the UK | Paragraph 51 |

- Every case has its own full set of conditions and all of them must be met. Cases 1, 2 and 3 also require the person to be not resident for the **next** tax year. Cases 4 to 8 require the person to have been not resident for the **previous** tax year. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- Case 3 needs the person to spend fewer than 16 days in the UK in the part of the year beginning with the day they cease to have a UK home, and to have a sufficient link with a country overseas at the end of the 6 months beginning with that day (paragraph 46). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- Case 1 uses "permitted limits" for UK days (90 reduced) and UK work days (30 reduced), and Case 2 uses a permitted limit for UK days only (90 reduced). The reduction grows with the whole months of the year before the departure day, so the limits are smaller the later in the year the person leaves (paragraphs 44(8) and (9), 45(9) and (10)): https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Priority.** Where more than one case applies, one case decides the split date. Case 1 has priority over Cases 2 and 3, and Case 2 over Case 3 (paragraph 54). Among Cases 4 to 8, Case 6 or Case 7 takes priority over Cases 4, 5 and 8 unless Case 5 has an earlier split year date, and where only Cases 4, 5 and 8 apply the earliest split year date wins (paragraph 55). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Temporary non-residence.** Leaving is not the end of it. RDR3 treats a person as temporarily non-resident where, after a residence period of sole UK residence, in 4 or more of the 7 tax years immediately preceding the year of departure they either had sole UK residence for the tax year or the year was a split year that included a residence period of sole UK residence and the period of non-residence lasts 5 years or less. Certain income and gains of that period are then taxed in the year of return. If the period of non-residence is more than 5 years, that is 5 years plus one day, the rules do not apply. https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3

## Section 7: Counting days

- **The midnight rule** (paragraph 22(1)). If P is present in the UK at the end of a day, that day counts as a day spent by P in the UK. If P is not present at the end of the day, it does not count (paragraph 23(1)), subject to the deeming rule below. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Transit** (paragraph 22(3)). A day does not count where P arrives in the UK only as a passenger, leaves the next day, and between arrival and departure does not engage in activities that are to a substantial extent unrelated to P's passage through the UK. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Exceptional circumstances** (paragraph 22(4) to (6)). A day does not count where P would not have been present at the end of it but for exceptional circumstances beyond P's control that prevent P from leaving, and P intends to leave as soon as they permit. The statute's examples are national or local emergencies such as war, civil unrest or natural disasters, and a sudden or life-threatening illness or injury. **The maximum is 60 days in a tax year**, counted forward from the start of the year; every later day within the exception counts as a day spent in the UK, whether or not the circumstances are the same ones. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **The deeming rule** (paragraph 23(3) and (4)). All three conditions must hold: P has at least 3 UK ties for the year; the number of qualifying days, meaning days when P is present in the UK at some point but not at the end of the day, is more than 30; and P was resident in the UK for at least one of the 3 preceding tax years. Once the qualifying days reach 30, counting forward from the start of the year, every later qualifying day is treated as a day spent in the UK. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **The deeming rule does not feed itself** (paragraph 23(5)). It is ignored when deciding whether P has 3 UK ties, so qualifying days above 30 are not used to create the 90-day tie. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Aggregate, not consecutive** (paragraph 24). A number of days spent in the UK "in" a period is the total for that period, whether continuous or intermittent. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **A work day is not a day spent in the UK.** Paragraph 22 decides whether a day counts as a day spent in the UK. It says nothing about days on which P does more than 3 hours' work, which are counted by their own rules (paragraphs 9, 14 and 35). Work is doing something in the performance of duties of an employment or in the course of a trade, and qualifying travelling time counts as work (paragraph 26). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45

## The method, step by step

1. Fix the year and the history. Confirm the tax year under test and whether the person was UK resident in each of the 3 tax years before it, since that choice decides which automatic overseas test, which tie list and which ties table applies. Finance Act 2013, Schedule 45, paragraphs 12, 13, 31, 18 and 19: https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
2. Build the day log before applying any test. For every day record whether the person was in the UK at the end of the day, whether they were present at some point but not at midnight, whether they did more than 3 hours' work in the UK or overseas, and which country they were in at midnight. Apply transit, exceptional circumstances up to the 60-day maximum, and then the deeming rule, in that order. Paragraphs 22 to 24: https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
3. Apply the automatic overseas tests (paragraphs 12 to 16). If any one is met, stop: the person is not UK resident for the year. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
4. Apply the automatic UK tests (paragraphs 7 to 10). If any one is met and no automatic overseas test is, the person is UK resident for the whole year. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
5. If nothing is decided, count the ties in Section 5 and read the day count against Table A or Table B (paragraphs 17 to 19 and 31 to 38). https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
6. If the person is resident and arrived or left during the year, test every split year case that could apply and then apply the priority rules to pick one split date (paragraphs 43 to 55). Also test temporary non-residence for anyone who left within the last 5 years: https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3
7. Report the result on supplementary pages SA109 of the Self Assessment return, filed with the SA100: https://www.gov.uk/government/publications/self-assessment-residence-remittance-basis-etc-sa109

## Ask the client first

- Were you UK resident in any of the 3 tax years before this one, and which ones? This changes the day thresholds, the tie list and the table used.
- Can you give a dated log of every arrival and departure, including where you were at midnight each night and days you were in the UK without staying the night?
- Did you have a home available to you in the UK at any point, for how long, how many days were you in it, and did you also have a home overseas and how many days were you in that?
- On how many days did you do more than 3 hours' work in the UK, and on how many overseas? Were there gaps of 31 days or more with no such work? https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- Is your spouse, civil partner, cohabiting partner or any child of yours under 18 UK resident for the year, and if a child, on how many days did you see that child in the UK?
- Did you arrive in or leave the UK during the year, on what date, and were you resident for the year before and the year after?

## When to refuse or refer

- **Anyone within a few days of any threshold.** One day changes the answer at 15 and 16 days, 45 and 46 days, 90 and 91 days, 120 days, 182 and 183 days, 40 UK work days, 30 or 31 UK work days, 30 qualifying days and 60 exceptional days. Do not answer from an approximate day count. Refer for a day-by-day reconstruction. https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- **Treaty residence.** The statutory residence test decides UK residence only. Where another country also claims the person, the tie-breaker sits in the double taxation agreement, not in Schedule 45, and paragraph 42 says split year treatment is not intended to affect that question. Refer.
- **Any split year.** The cases overlap, the priority rules decide the split date, and Cases 1 and 2 have permitted limits that shrink the later the departure. Refer rather than pick a case.
- **Exceptional circumstances.** Whether a circumstance is exceptional, beyond the person's control and preventing departure is a judgement on facts. The statute gives examples, not a list.
- **Temporary non-residence**, and anyone returning to the UK whose period of non-residence is 5 years or less. RDR3 says the period must be longer than 5 years, that is 5 years plus one day, for the rules not to apply. https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3
- **Deceased persons.** The fourth and fifth automatic overseas tests, the fourth automatic UK test and the pro-rated ties tables all apply only on death.
- **A relevant job on board a vehicle, aircraft or ship**, where the third automatic overseas test and the third automatic UK test may be switched off.
- **Trustees and personal representatives.** Split year treatment does not apply to personal representatives and applies only to a limited extent to trustees (paragraph 41).
- **Residence within the UK.** This test does not decide whether someone is resident in Scotland, Wales, Northern Ireland or England for the purposes of a rate set there (paragraph 1(3)).
- What follows from the answer is a different question: how a UK resident is taxed on foreign income and gains is in `uk-non-dom`; the return itself is in `uk-income-tax-sa100`, `uk-capital-gains-sa108` and `uk-return-assembly`; a planned move is in `uk-to-italy-flat-tax-relocation` or `uk-to-uae-relocation-tax`.

## Section 8: Sources

- Finance Act 2013, Schedule 45 (the statutory residence test): https://www.legislation.gov.uk/ukpga/2013/29/schedule/45
- HMRC, RDR3 Statutory Residence Test notes: https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3
- HMRC, Residence and foreign income and gains regime etc, Self Assessment SA109: https://www.gov.uk/government/publications/self-assessment-residence-remittance-basis-etc-sa109

> **Working paper only.** This Guide states the test; it does not apply it. The statutory residence test turns on a day-by-day and hour-by-hour record, and a single day can reverse the answer. Keep a contemporaneous travel and work log with dates, midnights and hours. Where the status is close to a threshold, or a treaty, a split year or a death is involved, have a UK accountant settle it before the return is filed.

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
