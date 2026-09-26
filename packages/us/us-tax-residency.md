---
name: us-tax-residency
description: "US tax residency for non-US-citizens: substantial presence test, green card test, first-year election, closer connection exception, treaty tie-breaker, dual-status returns. Trigger on: \"US tax resident alien\", \"substantial presence test\", \"183-day US test\", \"green card tax residency\", \"first year election US\", \"closer connection exception\", \"US dual status return\", \"non-resident alien US\", \"treaty tie-breaker US\", \"moving to US taxes\", \"leaving US taxes\". US citizens are always resident — this skill covers non-citizens only."
version: 1.0
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US tax residency for non-citizens: green card test, substantial presence test, elections and dual-status years

Figures are for tax year 2026, with a dated section for 2025 returns (extended 2025 returns are due October 15, 2026). This Guide decides whether a non-US-citizen ("alien") is a **resident alien** or a **nonresident alien** for federal income tax, from what date, and what must be filed to make that position stick. The residency tests are statutory (IRC §7701(b)) and work the same way in 2026 as in 2025; only the years in the count shift. The core IRS source is [Publication 519, U.S. Tax Guide for Aliens](https://www.irs.gov/publications/p519) (2025 edition, for 2025 returns; use the 2026 edition for 2026 returns once it is published).

## Scope and who it is for

- **Covered:** any individual who is not a US citizen: visa holders, green card holders, visitors, and people arriving in or leaving the US.
- **Why it matters:** a resident alien is generally taxed on worldwide income, like a citizen. A nonresident alien is taxed only on US-source income and on income effectively connected with a US trade or business. [Pub 519, Introduction](https://www.irs.gov/publications/p519)
- **Not covered here:** US citizens; state residency, which each state decides under its own law; FICA status; estate and gift tax residence, which uses a different test ([Pub 519, Reminders](https://www.irs.gov/publications/p519)); and computing a nonresident's tax once status is known.
- **Immigration status and tax status are separate.** A work visa does not by itself make someone a tax resident.

## Ask the client first

- Citizenship(s), and whether the client has ever held a green card (Form I-551), with the date it was granted and whether it was ever surrendered, revoked or the subject of an I-407.
- Exact US entry and exit dates for the current year and the **two** previous calendar years (passport stamps, I-94 travel history, boarding passes). Partial days count as full days.
- Visa class on each day of presence (F, J, M, Q, A, G, NATO and so on), the J-1 category (student vs researcher/teacher/trainee), and every earlier calendar year spent in F, J, M or Q status.
- For J/Q teachers and trainees: who paid the compensation in each year (a foreign employer or a US payer).
- Whether any days were spent in transit (under 24 hours), as a foreign-vessel crew member, commuting daily from Canada or Mexico, or stuck in the US by a medical condition that arose there.
- Where the client's main place of work (tax home), permanent home, family, belongings, driver's licence and voter registration were during the year.
- Whether the client applied for a green card, took other steps toward one, or had an adjustment-of-status application pending at any time in the year.
- Whether the client is also a tax resident of another country under that country's law, and whether it has an income tax treaty with the US.
- Marital status on December 31 and the spouse's citizenship and residency.
- Plans for next year: will the client meet the substantial presence test in the following year, or leave for good?
- For departing green card holders: the years in which they held the card, net worth, the average annual net income tax for the last five years, and whether all five years of US returns were filed.

## The method, step by step

1. **Confirm the person is an alien.** Citizens are outside this Guide. Dual citizens who hold US citizenship are citizens.
2. **Green card test.** If the client was a lawful permanent resident (LPR) at any time in the calendar year, they are a resident for that year, subject to the residency starting date, a treaty tie-breaker and the expatriation rules below. Do this first; a green card holder never needs the day count to become resident.
3. **Count days of presence.** Count every day the client was physically in the US at any time of day for the current year and the two previous years, then remove excluded days (exempt individual, transit, crew, commuters, medical, NATO). Record each excluded day and why.
4. **Substantial presence test (SPT).** Resident if at least 31 days in the current year **and** current days + 1/3 of first-previous-year days + 1/6 of second-previous-year days is at least 183.
5. **If the SPT is met, test the closer connection exception.** Available only with **fewer than 183** days in the current year, a foreign tax home for the whole year, a closer connection to that country, no green card steps, and a timely Form 8840.
6. **If both tests fail, test the first-year choice** (arriving clients who will meet the SPT next year), and check whether the client wants it.
7. **Fix the residency dates.** Find the residency starting date (arrival year) and residency termination date (departure year). A year with both a resident and a nonresident part is a **dual-status year** unless an election converts it.
8. **Consider a treaty tie-breaker** if the client is also resident in a treaty country. For a green card holder, check the long-term resident expatriation trap **before** claiming it.
9. **Consider the spousal elections** (§6013(g) and §6013(h)) for married clients. They replace dual-status treatment with a full-year resident joint return.
10. **Departing green card holders:** decide whether the client is a long-term resident, whether they become a covered expatriate, and file Form 8854.
11. **File the right return and statements by the right date** (see the filing section), and keep the day-count schedule and evidence with the file.

Order matters: counting days before removing exempt-individual days makes students and scholars wrongly resident, and a treaty tie-breaker claimed before step 10 can make a long-term green card holder an expatriate.

## Test 1: the green card test

- **Rule.** An alien is a resident for any calendar year in which they are an LPR at any time. LPR status continues until it is taken away or is administratively or judicially determined to have been abandoned. [§7701(b)(1)(A)(i) and (b)(6)](https://www.law.cornell.edu/uscode/text/26/7701); [IRS: green card test](https://www.irs.gov/individuals/international-taxpayers/alien-residency-green-card-test)
- **Living abroad does not end it.** A green card holder who lives abroad remains a resident alien until the status formally ends, even if USCIS would no longer honour an old card or the holder has been away a long time. [Pub 519, ch. 1, "Resident status abandoned"](https://www.irs.gov/publications/p519)
- **When abandonment takes effect.** If the client starts it, when they file Form I-407 (or a letter of intent to abandon) **with the green card attached** with USCIS or a US consular officer. By mail, use certified mail with return receipt and keep proof of mailing and receipt; until that proof exists the client stays a resident alien. If USCIS or a consular officer starts it, when the final administrative order (or, on appeal, final judicial order) is issued. Status is also taken away by a final order of exclusion or deportation. [Pub 519, ch. 1](https://www.irs.gov/publications/p519)
- **Residency starting date (green card only).** If the client meets the green card test but not the SPT, residency starts on the first day in the year they are present in the US as an LPR. A card issued abroad starts residency on the first day of presence after it is received. If the client meets both tests, use the earlier of the two starting dates. [IRS: residency starting and ending dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)
- **Resident in the previous year?** If the client was resident at any time in the previous calendar year and is resident at any time this year, they are resident from January 1. [Pub 519, ch. 1, "Residency during the preceding year"](https://www.irs.gov/publications/p519)
- **Filing duty.** Pub 519 warns that an LPR who is required to file as a resident and does not may be regarded under immigration law as having abandoned status. [Pub 519, ch. 7](https://www.irs.gov/publications/p519)

## Test 2: the substantial presence test

**Rule** ([§7701(b)(3)](https://www.law.cornell.edu/uscode/text/26/7701); [IRS: substantial presence test](https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test)). For tax year 2026 the client is resident if both are true:

- present on **at least 31 days** in 2026, and
- days in 2026 + 1/3 of days in 2025 + 1/6 of days in 2024 **equals or exceeds 183**.

Exactly 183 passes ("equals or exceeds"); exactly 31 days passes ("at least"). The weighted total is not a count of days in any one year, so a client with fewer than 183 days in the current year can still pass. For 2025 returns, the years are 2025, 2024 and 2023.

**What counts as the United States.** The 50 states, DC, US territorial waters and the adjacent seabed and subsoil. It does **not** include US territories or US airspace. [Pub 519, ch. 1](https://www.irs.gov/publications/p519)

**A day of presence** is any day the client is physically present at any time during the day. [§7701(b)(7)(A)](https://www.law.cornell.edu/uscode/text/26/7701)

### Days that do not count

| Excluded days | Conditions | Form |
|---|---|---|
| Regular commuters from Canada or Mexico | Commute to work in the US from a home in Canada or Mexico on more than 75% of workdays in the working period; "commute" means out and back within 24 hours. [Pub 519, ch. 1, "Days of Presence"](https://www.irs.gov/publications/p519) | - |
| Transit | In the US for under 24 hours while travelling between two places outside the US. Attending a business meeting, even at the airport, breaks transit | - |
| Crew of a foreign vessel | Regular crew member of a foreign vessel between the US and a foreign country or US territory; not if the client does other US business that day | - |
| Medical condition | Intended to leave but could not because of a condition that arose while in the US. Not available if the condition existed before arrival and was known, if the client returns for treatment of an earlier condition, or if they stay beyond a reasonable time after they could leave | Form 8843 |
| NATO | Member of a force or civilian component to NATO under a NATO visa; **not** dependants, who count every day | - |
| Exempt individual | See the next table | Form 8843, except foreign government-related individuals [Form 8843](https://www.irs.gov/pub/irs-pdf/f8843.pdf) |

### Exempt individuals, and the year limits

"Exempt" means the days do not count for the SPT; it does **not** mean exempt from tax. The client must substantially comply with the visa (no activity prohibited by immigration law that could cost the visa status). Immediate family (spouse and unmarried children under 21 in the household whose visas derive from the principal's) are included. [§7701(b)(5)](https://www.law.cornell.edu/uscode/text/26/7701); [Pub 519, ch. 1, "Exempt individual"](https://www.irs.gov/publications/p519)

| Category | Who | Limit on exempt years |
|---|---|---|
| Foreign government-related individual | Diplomatic/consular status or full-time employee of an international organization; generally A and G visas | No year limit. **A-3 and G-5** household staff are not exempt and count every day |
| Teacher or trainee | J or Q visa, other than as a student (for example J-1 researcher, professor, trainee) | Not exempt in the current year if exempt as a teacher, trainee **or student** for any part of **2 of the 6** preceding calendar years. Exception: still exempt if exempt in 3 or fewer of the 6 preceding years and a foreign employer paid all compensation this year and in each earlier year as a teacher or trainee (the statute's "4 calendar years" rule) |
| Student | F, M, or J/Q as a student | Exempt for **5 calendar years** (any part of a year counts as a year, and years as a teacher or trainee count). After that the student is **not** exempt unless they show they do not intend to reside permanently in the US and have substantially complied with the visa |
| Professional athlete | Competing in a charitable sports event | Only the days actually competing |

Days as an exempt individual also do not count for the first-year choice, and an exempt individual's residency starting date can be later than their arrival date. [IRS: residency starting and ending dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)

**Form 8843.** Required to exclude days as a student, teacher or trainee, professional athlete, or for a medical condition; due with the return, or on its own by the Form 1040-NR due date. If it is not filed on time, the athlete and medical-condition days **cannot be excluded**, unless the client shows by clear and convincing evidence that they took reasonable steps to comply. [Pub 519, ch. 1, "Form 8843"](https://www.irs.gov/publications/p519)

## Closer connection exception (Form 8840)

A client who meets the SPT is still treated as a nonresident if **all** of these hold for the year ([§7701(b)(3)(B)-(C)](https://www.law.cornell.edu/uscode/text/26/7701); [IRS: closer connection exception](https://www.irs.gov/individuals/international-taxpayers/closer-connection-exception-to-the-substantial-presence-test)):

- present in the US on **fewer than 183 days** in the current year (182 or fewer; 183 or more rules it out);
- a **tax home** in a foreign country for the **entire** year, in the same country to which the closer connection is claimed. The tax home is the general area of the main place of business, employment or post of duty, not the family home; with no regular place of business, it is where the client regularly lives;
- a closer connection to that foreign country than to the US (or to two countries, if the tax home moved from one to the other during the year and the client was taxed as a resident in the way Pub 519 describes);
- the client did **not** apply for, or take other steps toward, LPR status, and had **no** adjustment-of-status application pending, at any time in the year; and
- a fully completed **Form 8840** is filed on time.

Closer connection is judged on facts such as the permanent home (available at all times, not only for short stays), family, belongings, affiliations, business activities, driver's licence, where the client votes, and the residence country given on forms such as W-9 or W-8BEN. [Pub 519, ch. 1, "Establishing a closer connection"](https://www.irs.gov/publications/p519)

**Deadline and consequence.** Form 8840 is due by the due date of Form 1040-NR, including extensions. Attach it to the Form 1040-NR, or, if no return is required, send it on its own to the IRS Austin centre by that date. Without a timely Form 8840 the exception cannot be claimed, unless the client shows by clear and convincing evidence that they took reasonable steps to learn of the requirement and significant steps to comply. [Form 8840 (2025)](https://www.irs.gov/pub/irs-pdf/f8840.pdf); [Pub 519, ch. 1](https://www.irs.gov/publications/p519)

The exception is for the SPT only. It does not apply to a green card holder. A client with 183 or more days in the current year must look instead to a treaty tie-breaker.

## First-year choice (§7701(b)(4))

A client who arrives late in a year and will be resident next year can choose to be resident for part of the arrival year (useful, for example, to file jointly under §6013(h) or to be taxed as a resident from arrival). Conditions for a choice for year X ([§7701(b)(4)](https://www.law.cornell.edu/uscode/text/26/7701); [Pub 519, ch. 1, "First-Year Choice"](https://www.irs.gov/publications/p519)):

- **not** resident under the green card test or the SPT for year X;
- **not** resident at any time in year X-1, and no first-year choice made for year X-1;
- **resident under the SPT** in year X+1 (the green card test does not qualify);
- present in the US for **at least 31 consecutive days** in year X; and
- present for at least 75% of the days from the first day of that 31-day period to December 31 of year X (the "testing period"). Up to 5 days of absence in total can be treated as days of presence for this 75% test only. [§7701(b)(4)(A)](https://www.law.cornell.edu/uscode/text/26/7701)

Days excluded from the SPT (exempt individual, transit, and so on) are not counted as presence for either condition. Residency starts on the first day of the earliest 31-day period that satisfies both conditions.

**How and when.** Attach the statement Pub 519 describes (the choice, non-residence in year X-1, SPT residence and day count in year X+1, the 31-day and continuous-presence periods, and absence days treated as presence) to Form 1040 for year X. The return and statement **cannot be filed until the SPT has been met for year X+1**. If that has not happened by April 15, extend with Form 4868 (to October 15) and pay with the extension the tax figured as if the client were a nonresident all year; interest and late-payment penalties run on tax not paid by April 15. Once made, the choice cannot be revoked without IRS approval. Not following the procedure means nonresident for all of year X, unless the clear-and-convincing-evidence relief applies. [Pub 519, ch. 1, "Statement required to make the first-year choice"](https://www.irs.gov/publications/p519)

Marriage is not required to make the choice.

## Residency starting and ending dates

**Arrival year.** If the client is resident this year and was **not** resident at any time last year, they are resident only from the residency starting date. [§7701(b)(2)(A)](https://www.law.cornell.edu/uscode/text/26/7701)

- SPT: the first day present in the year. Up to **10 days** of presence can be disregarded for this date (not for the day count) if, on those days, the client had a closer connection to, and a tax home in, a foreign country. Periods of consecutive days must be excluded whole or not at all. A signed statement under penalties of perjury must be filed by the Form 1040-NR due date, or the client's first day of residency is their first day of presence. [Pub 519, ch. 1, "Residency starting date under substantial presence test"](https://www.irs.gov/publications/p519)
- Green card: see Test 1. First-year choice: the first day of the qualifying 31-day period.

**Departure year.** If the client was resident this year but is **not** resident at any time next year, the residency termination date is **December 31**, unless an earlier date applies. [Pub 519, ch. 1, "Last Year of Residency"](https://www.irs.gov/publications/p519)

- The earlier date is: the last day physically present in the US (SPT); the first day no longer an LPR (green card test); or the later of the two if both tests were met.
- It is available **only if**, for the rest of the year, the client had a tax home in a foreign country and a closer connection to it, **and** is not resident at any time in the following year. [§7701(b)(2)(B)](https://www.law.cornell.edu/uscode/text/26/7701)
- Up to **10 days** of later visits can be disregarded in fixing the termination date (not in the SPT count), on the same rules as on arrival.
- A signed statement (last day of presence, facts showing the foreign tax home and closer connection, and the date and evidence of LPR abandonment where relevant) must be filed by the Form 1040-NR due date, or the closer connection cannot be claimed and residency runs to December 31. [Pub 519, ch. 1, "Statement required to establish your residency termination date"](https://www.irs.gov/publications/p519)
- If the client is resident at any time in the **next** year, they are treated as resident through December 31 of this year, whatever their closer connection. [IRS: residency starting and ending dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)

A client who leaves mid-year after meeting the SPT is therefore resident to December 31 unless every condition above is met and documented.

## Treaty tie-breaker (Form 8833)

If the client is a resident of the US under §7701(b) and also a resident of a treaty country under that country's law, the treaty's residence article may assign residence to one country. Read the specific treaty. A common order, for example US-Germany Article 4(2), is permanent home, centre of vital interests, habitual abode, nationality, then mutual agreement. [US-Germany treaty](https://www.irs.gov/pub/irs-trty/germany.pdf)

- **Effect.** A client who is resident in the treaty country under the tie-breaker and claims treaty benefits as a nonresident computes their US income tax as a nonresident alien for the dual-resident period. They are still treated as a US resident for other Code purposes (for example, whether a foreign company is a CFC), and their residency time periods are unchanged. [Treas. Reg. §301.7701(b)-7(a)](https://www.law.cornell.edu/cfr/text/26/301.7701%28b%29-7)
- **Filing.** File Form 1040-NR by its due date (including extensions) with a fully completed Form 8833 attached. [Treas. Reg. §301.7701(b)-7(b)-(c)](https://www.law.cornell.edu/cfr/text/26/301.7701%28b%29-7); [Pub 519, ch. 1, "Effect of Tax Treaties"](https://www.irs.gov/publications/p519)
- **Penalty.** Failure to disclose a treaty-based return position carries a penalty of $1,000 per failure for an individual, waivable for reasonable cause and good faith. [§6712](https://www.law.cornell.edu/uscode/text/26/6712); [Form 8833](https://www.irs.gov/pub/irs-pdf/f8833.pdf)
- **Green card holders: the long-term resident trap.** A green card holder can claim a tie-breaker (Pub 519 cites §7701(b)(6)(B)). But an LPR who starts to be treated as a resident of the treaty country, does not waive the treaty benefits, and notifies the IRS **stops being an LPR for tax purposes**. For a long-term resident that date is an **expatriation date** under §877A, and Form 8854 is due. [§7701(b)(6)](https://www.law.cornell.edu/uscode/text/26/7701); [Form 8854 instructions](https://www.irs.gov/instructions/i8854); [Form 8833 note on long-term residents](https://www.irs.gov/pub/irs-pdf/f8833.pdf) Filing Form 1040-NR can also affect whether the client keeps the residency permit. [Treas. Reg. §301.7701(b)-7(b)](https://www.law.cornell.edu/cfr/text/26/301.7701%28b%29-7)

## Expatriation of long-term residents (§877A)

- **Long-term resident (LTR).** An LPR in at least **8 of the last 15 tax years** ending with the year LPR status ends. Do not count a year in which the client was treated as resident in a treaty country and did not waive the treaty benefits. [Form 8854 instructions, "Long-term resident (LTR) defined"](https://www.irs.gov/instructions/i8854)
- **Expatriation date** for an LTR is the earliest of: filing Form I-407 with a US consular or immigration officer; a final administrative order of abandonment (or a final judicial order if appealed); a final order of removal; or the date a dual resident starts to be treated as a treaty-country resident, does not waive the benefits and notifies the IRS. [Form 8854 instructions](https://www.irs.gov/instructions/i8854)
- **Covered expatriate** if any one applies: average annual net income tax for the 5 tax years before the expatriation date is **more than** $211,000 for expatriation in 2026 ([Rev. Proc. 2025-32, §4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) or more than $206,000 for 2025 ([Form 8854 instructions](https://www.irs.gov/instructions/i8854)); net worth of $2 million or more on the expatriation date ([IRS: expatriation tax](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax)); or failure to certify on Form 8854 five years of federal tax compliance.
- **Consequence.** A covered expatriate is taxed on the net unrealized gain in their property as if sold at fair market value on the day before the expatriation date. The gain otherwise included is reduced (not below zero) by $910,000 for 2026 ([Rev. Proc. 2025-32, §4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) and by $890,000 for 2025 ([Form 8854 instructions](https://www.irs.gov/instructions/i8854)). Deferred compensation, specified tax-deferred accounts and non-grantor trust interests follow separate rules. Gifts and bequests from a covered expatriate to US persons can trigger the §2801 tax on the recipient.
- **Form 8854.** Every LTR who ends residency files an initial Form 8854 with the return for the year that includes the expatriation date, **whether or not** they are a covered expatriate. If no return is required, file it by the date the return would have been due (including extensions). The penalty for not filing, or for filing incomplete or incorrect information, is $10,000 unless due to reasonable cause and not wilful neglect. [Form 8854 instructions, "Penalties"](https://www.irs.gov/instructions/i8854)

## Spousal elections: joint return instead of dual status

Both elections treat the electing spouse as a resident for the **whole** year, so both spouses are taxed on worldwide income and the dual-status restrictions do not apply. [§6013(g)-(h)](https://www.law.cornell.edu/uscode/text/26/6013); [Pub 519, ch. 1](https://www.irs.gov/publications/p519)

| | §6013(h) "Choosing resident alien status" | §6013(g) "Nonresident spouse treated as a resident" |
|---|---|---|
| Who | Client was a nonresident at the start of the year and resident at the end, and is married on December 31 to a citizen or resident (both spouses may be arriving) | On December 31 one spouse is a citizen or resident and the other is a nonresident alien |
| Duration | That year only. The couple can never make it again, even after divorce and remarriage | That year and every later year until revoked, ended by death, legal separation or the IRS, or suspended for a year in which neither spouse is a citizen or resident. Once ended, never again for the couple |
| Treaty | Taxed on worldwide income | Neither spouse can claim under a treaty not to be a US resident while it applies |
| Return | Joint Form 1040 for the year, checkbox in Filing Status, statement signed by both spouses | Joint Form 1040 for the first year, statement signed by both; joint or separate returns later |

Either can be made on an amended joint return within 3 years of filing the original return or 2 years of paying the tax, whichever is later; any later-year returns must then be amended too. Revocation of §6013(g) is due by the return due date for the year it takes effect. [IRS: nonresident spouse](https://www.irs.gov/individuals/international-taxpayers/nonresident-spouse); [Pub 519, ch. 1](https://www.irs.gov/publications/p519)

## Dual-status years

For the resident part of the year the client is taxed on worldwide income. For the nonresident part they are taxed on US-source income and effectively connected income. Foreign income received while nonresident and not effectively connected is not taxable, even if earned while resident. [Pub 519, ch. 6](https://www.irs.gov/publications/p519)

Restrictions on a dual-status return ([Pub 519, ch. 6, "Restrictions for Dual-Status Taxpayers"](https://www.irs.gov/publications/p519); [IRS: taxation of dual-status individuals](https://www.irs.gov/individuals/international-taxpayers/taxation-of-dual-status-individuals)):

- no standard deduction (allowable itemized deductions only);
- no head of household rates;
- no joint return unless §6013(g) or (h) is elected;
- a married client who does not elect must use married-filing-separately rates for effectively connected income (limited exceptions for certain married residents of Canada, Mexico or South Korea and US nationals living apart from their spouse for the last 6 months of the year);
- no education credits, earned income credit or credit for the elderly or disabled unless married and electing full-year residence with a joint return;
- non-effectively-connected US income of the nonresident period is taxed at a flat 30% or a lower treaty rate, with no deductions against it. [Pub 519, ch. 6, "How To Figure Your Tax"](https://www.irs.gov/publications/p519)


## Worked cases (tax year 2026 unless stated)

**Case 1: plain SPT.** An H-1B worker was in the US on 150 days in 2026, 99 days in 2025 and none in 2024. Weighted total: 150 + 99/3 + 0 = 150 + 33 = 183. That equals 183, so the SPT is met ("equals or exceeds"). With 150 days the closer connection exception is open in principle, but it needs a foreign tax home all year, and a worker whose job is in the US will normally have a US tax home. [§7701(b)(3)](https://www.law.cornell.edu/uscode/text/26/7701)

**Case 2: just under.** Same client, but 96 days in 2025: 150 + 32 = 182. Below 183, so no SPT; nonresident for 2026 unless they hold a green card or make a first-year choice.

**Case 3: 183 days blocks closer connection.** A consultant spent 183 days in the US in 2026, keeps her home, family and employer in Germany and has a German tax home all year. The SPT is met on 2026 days alone. Closer connection is **not** available (it needs fewer than 183 days). If she is resident in Germany under German law, the US-Germany treaty tie-breaker (permanent home first) may make her a German resident: she files Form 1040-NR with Form 8833, or risks the $1,000 penalty for not disclosing the position. [§6712](https://www.law.cornell.edu/uscode/text/26/6712)

**Case 4: F-1 student, sixth year.** A student arrived in F-1 status in August 2021 and has been exempt as a student in 2021, 2022, 2023, 2024 and 2025. That is 5 calendar years, because part-years count. In 2026 her days count unless she establishes that she does not intend to reside permanently in the US and has substantially complied with the visa. With 330 days in 2026, she meets the SPT on 2026 days alone and is a resident from her first day of presence in 2026 (she was not resident in 2025). If she qualifies to stay exempt, she files Form 8843 and remains a nonresident. [Pub 519, ch. 1, "Students"](https://www.irs.gov/publications/p519)

**Case 5: J-1 researcher, third year.** A US-paid J-1 researcher was exempt as a teacher/trainee in 2024 and 2025. For 2026 they were exempt for part of 2 of the 6 preceding years, so they are **not** an exempt individual in 2026, and all 2026 days count. (If a foreign employer had paid all their compensation in every year, the 4-of-6 rule would keep them exempt.) [§7701(b)(5)(E)(i)](https://www.law.cornell.edu/uscode/text/26/7701)

**Case 6: first-year choice for 2025, filed by October 15, 2026.** A client arrived on November 3, 2025, stayed to December 3 (31 consecutive days), was away December 4-10 (7 days) and was back from December 11 to 31 (21 days). They were not in the US in 2023 or 2024, so they are not resident for 2025 under the SPT (52 days) and were not resident in 2024. They meet the SPT for 2026. Testing period November 3 to December 31 = 59 days. Present 31 + 21 = 52 days. Three-quarters of 59 is 44.25, and 52 is more than that, so the choice is available (the 5-day allowance is not needed). Residency starts on November 3, 2025. The 2025 Form 1040 with the choice statement could not be filed until the client met the 2026 SPT; with a Form 4868 filed by April 15, 2026 the return is due by October 15, 2026. [Pub 519, ch. 1, "First-Year Choice"](https://www.irs.gov/publications/p519)

**Case 7: leaving mid-year.** A client present every day of 2024 and 2025 left for good on June 30, 2026 for a new job and home in Singapore. 181 days in 2026 plus one-third of the 2025 days and one-sixth of the 2024 days is well over 183: SPT met. With a Singapore tax home and closer connection from July 1 and no US residency in 2027, the termination date is June 30, 2026, if the statement is filed by the Form 1040-NR due date; otherwise December 31. 2026 is dual-status: Form 1040-NR marked "Dual Status Return", with a Form 1040 statement for the resident period. [Pub 519, ch. 1 and ch. 6](https://www.irs.gov/publications/p519)

**Case 8: green card holder moving abroad.** A client who has held a green card since 2014 files Form I-407 with the card at a US consulate on March 31, 2026. An LPR in every year 2014-2026, he is a long-term resident, and March 31, 2026 is his expatriation date. He is a covered expatriate if his net worth is $2 million or more ([IRS: expatriation tax](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax)), or his average annual net income tax for 2021-2025 is more than $211,000 ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)), or he cannot certify five years of compliance. Either way he files an initial Form 8854 with his 2026 return, or faces a $10,000 penalty. [Form 8854 instructions](https://www.irs.gov/instructions/i8854) Had he instead claimed a treaty tie-breaker on a 2026 Form 1040-NR with Form 8833, the result would have been the same: an expatriation date.

## When to refuse or refer

- Refer any green card holder who is considering a treaty tie-breaker, surrendering the card, or has lived abroad for years without filing: the §877A analysis, valuation and relief procedures need a specialist.
- Refer if the long-term resident count is close to 8 years, involves part-years, or includes years claimed as treaty-resident.
- Refer if the client may be a covered expatriate (net worth, five-year tax average, or unfiled years).
- Refer treaty tie-breakers where the permanent home or centre of vital interests is genuinely unclear, or where the specific treaty has special residence rules; the answer depends on that treaty's text.
- Refuse to state a residency conclusion without a day count built from records for all three years. Do not accept estimates such as "about 5 months".
- Refer diplomats and international-organization staff where status or immunity is unclear.
- Refer late Form 8840, 8843 or residency-date statements: relief needs clear and convincing evidence and is fact-specific.
- Refer state residency: federal status does not decide it.

## Filing steps and deadlines

- **Resident all year, or resident at year-end (dual status):** Form 1040, due April 15 of the following year (April 15, 2027 for tax year 2026). A dual-status client resident on December 31 marks the Form 1040 "Dual Status Return" and attaches a Form 1040-NR statement for the nonresident period. [Pub 519, ch. 6 and ch. 7](https://www.irs.gov/publications/p519)
- **Nonresident at year-end (including dual-status departures and treaty tie-breaker claims):** Form 1040-NR. It is due April 15 of the following year if the client received wages subject to withholding, otherwise June 15. A departing dual-status client marks it "Dual Status Return" with a Form 1040 statement. [Pub 519, ch. 6](https://www.irs.gov/publications/p519)
- **Extensions:** Form 4868 filed by the original due date gives an automatic 6-month extension (October 15 for calendar-year Form 1040 filers). It does not extend the time to pay. A due date on a weekend or legal holiday moves to the next day that is not one. [Pub 519, ch. 7](https://www.irs.gov/publications/p519)
- **Form 8840, Form 8843 and the residency start/termination statements:** attach to the return, or file separately with the IRS Austin centre if no return is required, by the Form 1040-NR due date. [Pub 519, ch. 1](https://www.irs.gov/publications/p519)
- **Form 8833:** attach to the Form 1040-NR (a return must be filed to make the disclosure even if not otherwise required). [Form 8833](https://www.irs.gov/pub/irs-pdf/f8833.pdf)
- **First-year choice statement:** with the Form 1040 for the choice year, filed only after the SPT is met for the next year.
- **Form 8854:** with the return for the year that includes the expatriation date.

### 2025 returns (filing in 2026)

- The same tests apply, with the SPT counting 2025, 2024 and 2023 days. Use the 2025 Pub 519 and the 2025 Forms 8840, 8843 and 8854.
- Extended 2025 returns are due **October 15, 2026**. That includes first-year choices for 2025 that waited for the 2026 SPT. [Pub 519, ch. 1](https://www.irs.gov/publications/p519)
- For expatriation in 2025, the covered-expatriate tax threshold is $206,000 and the exclusion is $890,000. [Form 8854 instructions (2025)](https://www.irs.gov/instructions/i8854)
- Dual-status taxpayers **cannot e-file** their 2025 return. Paper-file at the dual-status address in the Form 1040 or 1040-NR instructions. [Pub 519, ch. 6, "Forms To File"](https://www.irs.gov/publications/p519) Check the 2026 instructions before assuming the same for 2026.

## Completion checklist

- Three-year day-count schedule tied to travel records, with each excluded day and its reason; green card and exempt-year history.
- SPT arithmetic shown, testing both "at least 31" and "equals or exceeds 183".
- Closer connection, first-year choice and spousal elections each tested, with Forms 8840/8843 and statements prepared on time.
- Residency starting and termination dates fixed, with any 10-day exclusion statement.
- Treaty position: specific treaty article applied, Form 8833 attached, long-term resident check done **before** claiming.
- Form 8854 prepared where a long-term resident's LPR status ended.
- Correct return (1040 or 1040-NR, "Dual Status Return" where applicable) and due date recorded.

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
