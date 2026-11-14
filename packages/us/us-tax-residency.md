---
name: us-tax-residency
description: Decide whether an individual is a US resident or nonresident for federal income tax in 2026, and from which date. Covers US citizens (always resident and taxed on worldwide income), the green card test, the substantial presence test under 26 U.S.C. 7701(b) (at least 31 days in 2026 and 183 weighted days counting all 2026 days, one-third of 2025 days and one-sixth of 2024 days), days that do not count, exempt individuals on F, J, M, Q, A and G visas and their year limits, the closer connection exception on Form 8840, the first-year choice, residency starting and termination dates with the 10-day rule, treaty tie-breakers on Form 8833, the spousal elections under section 6013(g) and (h), and dual-status returns. Trigger on "US tax resident", "substantial presence test", "183-day US test", "green card tax residency", "first year choice", "closer connection exception", "Form 8840", "Form 8843", "dual status return", "nonresident alien", "treaty tie-breaker US", "moving to the US taxes", "leaving the US taxes". Federal only.
version: "2.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# US federal tax residency for individuals, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 7701(b), 6013(g) and (h) and 6712 (govinfo), IRS Pub. 519 (2025 edition, the current one), the 2026 Forms 8840 and 8843, Form 8833, the 2025 Instructions for Form 1040-NR and IRS residency pages, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A US citizen is always a US resident for federal income tax and is taxed on worldwide income wherever they live. A non-citizen (an "alien") is a **resident** for 2026 if they held a green card at any time in 2026, or if they meet the **substantial presence test**: present on at least **31 days** in 2026, and 2026 days plus **one-third** of 2025 days plus **one-sixth** of 2024 days **equals or exceeds 183**. Otherwise they are a **nonresident**, unless they make the first-year choice. Someone who meets the test in their arrival year is resident only **from their first day of presence in 2026** (up to 10 days of earlier visits can be set aside with a signed statement), and was nonresident before that. Days as a student, teacher, trainee or diplomat, and some other days, do not count. With **fewer than 183 days** in 2026 and a foreign tax home all year, a timely **Form 8840** can still make the person a nonresident. A treaty tie-breaker (**Form 8833**) can do the same for tax purposes, with a serious trap for long-term green card holders.

## Scope and who this is for

In scope: one individual's federal income tax residency for calendar year 2026, the dates it starts and ends, and the statements and forms that make the position stick. The result decides which return is filed (Form 1040, Form 1040-NR or a dual-status return) and whether worldwide income is taxed.

- **US citizens**, including dual citizens who hold US citizenship, are resident by citizenship. They are taxed on worldwide income from all sources whether they live in the US or abroad, and reliefs such as the foreign earned income exclusion and the foreign tax credit are only available by filing a return ([IRS: U.S. citizens and resident aliens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad)). A treaty does not change this: the saving clause lets the US tax its citizens as if the treaty had not come into effect (for example the [US-Germany treaty](https://www.irs.gov/pub/irs-trty/germany.pdf), Protocol paragraph 1(a)). The rest of this skill is about non-citizens.
- **Resident or nonresident matters because** a resident alien is taxed like a citizen, on worldwide income; a nonresident alien is taxed only on US-source income and on income effectively connected with a US trade or business ([Pub. 519](https://www.irs.gov/publications/p519), chapters 1 and 4).
- **Immigration status and tax status are separate.** A work visa does not by itself make someone a tax resident, and a student visa does not by itself make someone a nonresident.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Covered expatriate tests, the exit tax, Form 8854 figures and penalties | `us-expatriation-exit-tax` |
| Foreign earned income exclusion and housing amounts | `us-foreign-earned-income-2555` |
| Foreign tax credit | `us-foreign-tax-credit-1116` |
| FBAR and Form 8938 reporting by residents | `us-fbar-fatca-reporting` |
| Capital gains of nonresidents | `us-nonresident-cgt` |
| The Form 1040 computation once residency is fixed | `us-form-1040-individual-return` |
| State residency (each state applies its own law) | the state's residency skill, for example `ca-residency-leaving-california`, `ny-residency-leaving-new-york` |
| Social security and Medicare (FICA) status of nonresidents; estate and gift tax residence, which uses a different test ([Pub. 519, Reminders](https://www.irs.gov/publications/p519)) | not covered here |

## Ask the client first

1. **Citizenship and green card history.** Is the client a US citizen? Have they ever held a green card (Form I-551), and if so, from what date, and was it ever surrendered with Form I-407, revoked, or the subject of a removal order?
2. **Exact US entry and exit dates for 2026, 2025 and 2024** (I-94 travel history, passport stamps, boarding passes). Any part of a day counts as a full day. Estimates such as "about five months" are not enough.
3. **Visa class on each day** (F, J, M, Q, A, G, NATO, H, L, B and so on), the J-1 category (student, or researcher, professor or trainee), every earlier calendar year spent in F, J, M or Q status, and who paid any J or Q compensation (a foreign employer or a US payer).
4. **Days that may be excluded:** transit under 24 hours, foreign-vessel crew days, daily commuting from Canada or Mexico, or a medical condition that arose in the US and stopped them leaving.
5. **Where the tax home and personal life were:** main place of work, permanent home, family, belongings, driver's licence, voter registration; and whether the client applied for a green card, took other steps toward one, or had an adjustment-of-status application pending at any time in 2026.
6. **Treaty and family facts:** is the client also a tax resident of another country under its law, does that country have an income tax treaty with the US, what was their marital status on December 31, 2026, and the spouse's citizenship and residency. Will they meet the substantial presence test in 2027, or leave for good? For a departing green card holder, also the years the card was held, so `us-expatriation-exit-tax` can be run.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Substantial presence test: minimum days present in 2026 | at least 31 days | [26 U.S.C. 7701(b)(3)(A)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm) |
| Substantial presence test: weighted total that must be equalled or exceeded | 183 days | [26 U.S.C. 7701(b)(3)(A)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm) |
| Multiplier for 2026 (current year) days | 1 | same |
| Multiplier for 2025 (1st preceding year) days | 1/3 | same |
| Multiplier for 2024 (2nd preceding year) days | 1/6 | same |
| Closer connection exception: days in 2026 must be fewer than | 183 days | [26 U.S.C. 7701(b)(3)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Form 8840 (2026)](https://www.irs.gov/pub/irs-pdf/f8840.pdf) |
| Days of nominal presence that can be disregarded in fixing the residency starting or termination date (not in the day count) | not more than 10 days | [26 U.S.C. 7701(b)(2)(C)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm) |
| First-year choice: consecutive days present in the choice year | at least 31 consecutive days | [26 U.S.C. 7701(b)(4)(A)(iv)(I)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm) |
| First-year choice: share of the testing period present | equal to or exceeding 75 percent | [26 U.S.C. 7701(b)(4)(A)(iv)(II)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm) |
| First-year choice: days of absence that can be treated as presence for the 75% test only | not exceeding 5 days in the aggregate | same |
| Teacher or trainee (J or Q, not a student): not exempt in 2026 if exempt as teacher, trainee or student in any part of this many of the 6 preceding calendar years | 2 calendar years | [26 U.S.C. 7701(b)(5)(E)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf) |
| Teacher or trainee paid entirely by a foreign employer: stays exempt if exempt in any part of no more than this many of the 6 preceding years (the statute substitutes "4 calendar years") | 3 (or fewer) of the 6 prior calendar years | [26 U.S.C. 7701(b)(5)(E)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf) |
| Student (F, M, or J or Q as a student): exempt years before the student must show no intent to reside permanently | 5 calendar years | [26 U.S.C. 7701(b)(5)(E)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf) |
| Regular commuter from Canada or Mexico: share of workdays in the working period commuted to the US | more than 75% | [Pub. 519 (2025), ch. 1, "Regular commuters from Canada or Mexico"](https://www.irs.gov/pub/irs-pdf/p519.pdf) |
| Transit between two foreign points: days do not count if present less than | 24 hours | [26 U.S.C. 7701(b)(7)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm) |
| Return to residency within 3 years after a residency period of at least 3 consecutive calendar years: the gap may be taxed under section 877(b) | 3 consecutive calendar years | [26 U.S.C. 7701(b)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm) |
| Penalty per failure to disclose a treaty-based return position (individual), waivable for reasonable cause and good faith | USD 1,000 | [26 U.S.C. 6712(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6712.htm); [Form 8833](https://www.irs.gov/pub/irs-pdf/f8833.pdf) |
| Form 1040-NR due date if the client received wages subject to US income tax withholding | 15th day of the 4th month after the year ends (April 15, 2027 for 2026) | [Instructions for Form 1040-NR (2025), "When and Where Should You File?"](https://www.irs.gov/pub/irs-pdf/i1040nr.pdf) |
| Form 1040-NR due date with no such wages | 15th day of the 6th month after the year ends (June 15, 2027 for 2026) | same |

None of these figures is indexed. The tests in 26 U.S.C. 7701(b) were not amended by the One Big Beautiful Bill Act (Public Law 119-21), so the 2026 rules are the 2025 rules with the counting years moved on by one.

### Step 1: citizen or alien

If the client is a US citizen, stop: resident for the whole year by citizenship, taxed on worldwide income. Everything below applies only to non-citizens.

### Step 2: the green card test

- **Rule.** An alien is a resident for any calendar year in which they are a lawful permanent resident (LPR) at any time. LPR status continues until it is revoked or administratively or judicially determined to have been abandoned ([26 U.S.C. 7701(b)(1)(A)(i) and (b)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [IRS: green card test](https://www.irs.gov/individuals/international-taxpayers/alien-residency-green-card-test)). A green card holder does not need the day count to be resident. Do this test first.
- **Living abroad does not end it.** A green card holder who lives abroad stays a resident alien until the status formally ends, even if USCIS would no longer honour the card because it is more than 10 years old or the holder has been away ([Pub. 519, ch. 1, "Resident status abandoned"](https://www.irs.gov/publications/p519)).
- **When abandonment takes effect.** If the client starts it: when they file Form I-407, or a letter stating their intent to abandon, **with the green card attached**, with USCIS or a US consular officer. By mail, send by certified mail, return receipt requested (or the foreign equivalent), and keep a copy and proof of mailing and receipt; until the client has proof the letter was received, they remain a resident alien. If USCIS or a consular officer starts it: when the final administrative order of abandonment is issued (or a final judicial order, on appeal). Status is also taken away by a final administrative or judicial order of exclusion or deportation ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)).
- **Filing duty.** Under immigration law, an LPR who is required to file as a resident and does not may be regarded as having abandoned status and may lose it ([Pub. 519, ch. 1 and ch. 7](https://www.irs.gov/publications/p519)).
- **Long-term residents.** A green card holder whose LPR status ends (by I-407, an order, or a treaty tie-breaker, Step 8) may be a long-term resident who has expatriated. Run `us-expatriation-exit-tax` before advising on any of these steps.

### Step 3: count the days of presence

Count every day the client was physically present in the US at any time during the day, for 2026, 2025 and 2024 ([26 U.S.C. 7701(b)(7)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)). "United States" means the 50 states, the District of Columbia, US territorial waters and the adjacent seabed and subsoil; it does **not** include US territories or US airspace ([IRS: substantial presence test](https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test)). Then remove the days that do not count, recording each excluded day and the reason:

| Excluded days | Conditions | Form |
| --- | --- | --- |
| Regular commuters from Canada or Mexico | Commuted to work in the US from a residence in Canada or Mexico on more than 75% of the workdays in the working period. "Commute" means to travel to work and return to the residence within 24 hours. The working period runs from the first to the last day in the year present in the US to work (or by season or cycle for seasonal work) ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)) | none |
| Transit | Present less than 24 hours while in transit between two places outside the US. Changing planes counts as transit; attending a business meeting, even at the airport, does not ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)) | none |
| Foreign-vessel crew | Temporarily present as a regular crew member of a foreign vessel engaged in transportation between the US and a foreign country or a US territory; not on a day the client otherwise engages in a US trade or business ([26 U.S.C. 7701(b)(7)(D)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)) | none |
| Medical condition | Intended to leave but could not because of a medical condition that arose while in the US. Not available if the condition existed before arrival and the client knew of it, if the client returned for treatment of a condition from an earlier stay, or if they stayed beyond a reasonable period after they became able to leave ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519); [Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf)) | Form 8843 |
| NATO | Member of a force or civilian component to NATO present under a NATO visa. Immediate family members on a NATO visa are **not** covered and count every day ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)) | none |
| Exempt individual | See the next table | Form 8843, except foreign government-related individuals on A or G visas |

**Exempt individuals.** "Exempt" means the days do not count for the substantial presence test; it does **not** mean exempt from tax. The client must substantially comply with the visa, meaning no activity prohibited by immigration law that could cost the visa status. Immediate family members (a spouse, and unmarried children under 21 who live regularly in the household and are not members of another household, whose visas derive from the principal's) are included ([26 U.S.C. 7701(b)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Pub. 519, ch. 1](https://www.irs.gov/publications/p519)).

| Category | Who | Limit on exempt years |
| --- | --- | --- |
| Foreign government-related individual | Full-time diplomatic or consular status, or a full-time employee of an international organization designated under the International Organizations Immunities Act; generally A and G visas | No year limit. **A-3 and G-5** household staff (personal employees, attendants, domestic workers of officials) are not exempt and count every day. Other A and G visa holders need not file Form 8843 ([Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf)) |
| Teacher or trainee | J or Q visa, other than as a student (for example a J-1 researcher, professor or trainee) | Not exempt in 2026 if exempt as a teacher, trainee **or student** for any part of **2 of the 6** preceding calendar years (2020 to 2025). Exception: still exempt if **all four** hold: exempt for any part of 3 (or fewer) of the 6 prior years; a foreign employer paid all 2026 compensation; the client was present as a teacher or trainee in one of the 6 prior years; and a foreign employer paid all compensation in each of those prior years. A foreign employer includes a foreign office of a US entity. Attach evidence of the foreign payment to Form 8843 ([Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf)) |
| Student | F, M, or J or Q as a student | Not exempt after being exempt as a teacher, trainee or student for any part of **more than 5 calendar years** (part-years count as years), unless the client establishes that they do not intend to reside permanently in the US and has substantially complied with the visa. The facts include whether they kept a closer connection to a foreign country and whether they took steps toward a green card ([26 U.S.C. 7701(b)(5)(E)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf)) |
| Professional athlete | Temporarily present to compete in a charitable sports event (organized mainly to benefit a section 501(c)(3) charity, all net proceeds to it, volunteers doing substantially all the work) | Only the days actually competing; not practice, promotion or travel days ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)) |

Days as an exempt individual also do not count for the first-year choice, and an exempt individual's residency starting date can be later than their arrival date ([IRS: residency starting and ending dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)).

**Form 8843.** Required to exclude days as a teacher, trainee, student or professional athlete, or for a medical condition. Attach it to the 2026 Form 1040-NR; if no return is required, mail it to the Internal Revenue Service Center, Austin, TX 73301-0215 by the Form 1040-NR due date (including extensions). If it is not filed on time, Form 8843 (2026) and Pub. 519 say the athlete and medical-condition days cannot be excluded, unless the client shows by clear and convincing evidence that they took reasonable actions to learn of the requirement and significant steps to comply. The IRS substantial presence test page states the same consequence for exempt-individual days too, so treat a late Form 8843 as putting every excluded day at risk ([Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf); [IRS: substantial presence test](https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test)).

### Step 4: the substantial presence test

For 2026 the client is resident if **both** hold ([26 U.S.C. 7701(b)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Form 8840 (2026)](https://www.irs.gov/pub/irs-pdf/f8840.pdf)):

- present on **at least 31 days** in 2026, and
- 2026 days + 1/3 of 2025 days + 1/6 of 2024 days **equals or exceeds 183**.

Exactly 183 passes ("equals or exceeds") and exactly 31 passes ("at least"). The statute gives no rounding, so the fractions are used as they fall: 100 days in 2025 counts as 33.33. Because the total is weighted, a client with fewer than 183 days in 2026 can still pass, and a client with 183 or more days in 2026 passes on 2026 days alone. Do the test for each year separately: meeting it for 2026 says nothing about 2025.

### Step 5: if the test is met, try the closer connection exception (Form 8840)

A client who meets the substantial presence test is still a nonresident for 2026 if **all** of these hold ([26 U.S.C. 7701(b)(3)(B) and (C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Form 8840 (2026)](https://www.irs.gov/pub/irs-pdf/f8840.pdf); [IRS: closer connection exception](https://www.irs.gov/individuals/international-taxpayers/closer-connection-exception-to-the-substantial-presence-test)):

- present on **fewer than 183 days** in 2026 (182 or fewer; 183 or more rules it out);
- a **tax home in a foreign country for the whole of 2026**, in the same country to which the closer connection is claimed. The tax home is the general area of the main place of business, employment or post of duty, wherever the family home is; with no regular place of business, it is where the client regularly lives; an itinerant's tax home is wherever they work. A US tax home at any time in the year rules the exception out. For this purpose a "foreign country" includes US territories;
- a closer connection to that foreign country than to the US. Two countries (not more) are allowed only if the tax home was in one foreign country on January 1, moved to a second during the year and stayed there, the client had a closer connection to each for its period, and was taxed as a resident under the law of either country for the whole year or of each for its period;
- the client did **not** apply for, or take other affirmative steps toward, LPR status, and had **no** adjustment-of-status application pending, at any time in 2026; and
- a fully completed **Form 8840** is filed on time (see Filing and payment).

Closer connection means more significant contacts with the foreign country than with the US. The facts include where the permanent home is (a house, flat or furnished room, owned or rented, available at all times and not only for short stays), family, personal belongings, social, political, cultural, professional or religious affiliations, business activities, the driver's licence, where the client votes, charities supported, and the country of residence given on forms such as W-9, W-8BEN or W-8ECI ([Pub. 519, ch. 1, "Establishing a closer connection"](https://www.irs.gov/publications/p519)).

The exception is for the substantial presence test only. It is not available to a green card holder. A client with 183 or more days in 2026 must look instead to a treaty tie-breaker (Step 8). Students have a separate route under the 5-year rule above.

### Step 6: if both tests fail, consider the first-year choice

A client who arrives late in the year and will be resident next year can choose to be resident for part of the arrival year, for example to file jointly under section 6013(h) or to be taxed as a resident from arrival. Marriage is not required. Conditions for a choice for 2026 ([26 U.S.C. 7701(b)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Pub. 519, ch. 1, "First-Year Choice"](https://www.irs.gov/publications/p519)):

- **not** resident under the green card test or the substantial presence test for 2026;
- **not** resident at any time in 2025, and no first-year choice made for 2025;
- **resident under the substantial presence test** for 2027 (the green card test does not qualify);
- present in the US for **at least 31 consecutive days** in 2026; and
- present for at least 75% of the days from the first day of that 31-day period to December 31, 2026 (the "testing period"). Up to 5 days of absence in total can be treated as days of presence for this 75% test only.

Days excluded from the substantial presence test (exempt individual, transit, and so on) do not count as presence for either condition. Residency starts on the first day of the earliest 31-day period for which the 75% test is met; if only a later 31-day period meets it, residency starts on the first day of that later period. Once made, the choice cannot be revoked without IRS approval. How to make it is under Filing and payment.

### Step 7: fix the residency dates

**First year of residency.** If the client is resident for 2026 and was **not** resident at any time in 2025, they are resident only from the residency starting date and nonresident before it ([26 U.S.C. 7701(b)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)):

- **Substantial presence test:** the first day present in the US in 2026. Up to **10 days** of presence can be disregarded for this date (never for the day count) if on those days the client had a closer connection to, and a tax home in, a foreign country. Days may come from more than one visit as long as the total is 10 or fewer, but a run of consecutive days must be excluded whole or not at all. The client must file a signed statement, made under penalties of perjury, by the Form 1040-NR due date (contents under Filing and payment); without it the first day of residency is the first day of presence ([Pub. 519, ch. 1, "Residency starting date under substantial presence test"](https://www.irs.gov/publications/p519)).
- **Green card test only:** the first day in 2026 present in the US as an LPR. A card received abroad starts residency on the first day of presence after it is received ([IRS: residency starting and ending dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)).
- **Both tests:** the earlier of the two dates.
- **First-year choice:** the first day of the qualifying 31-day period (Step 6).
- **Resident at any time in 2025:** resident from January 1, 2026, whichever test applies ([Pub. 519, ch. 1, "Residency during the preceding year"](https://www.irs.gov/publications/p519)).

**Last year of residency.** If the client is resident for 2026 but **not** at any time in 2027, residency ends on **December 31, 2026**, unless an earlier date applies ([26 U.S.C. 7701(b)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm); [Pub. 519, ch. 1, "Last Year of Residency"](https://www.irs.gov/publications/p519)):

- The earlier date is the last day physically present in the US (substantial presence test), the first day no longer an LPR (green card test), or the later of the two if both tests were met.
- It is available **only if**, for the rest of 2026, the client had a tax home in a foreign country and a closer connection to it, **and** is not resident at any time in 2027.
- Up to **10 days** of later visits can be disregarded in fixing the termination date (not in the day count), on the same rules as on arrival.
- A signed statement (contents under Filing and payment) must be filed by the Form 1040-NR due date, or the earlier date cannot be claimed and residency runs to December 31.
- If the client is resident at any time in 2027, they are resident through December 31, 2026, whatever their closer connection ([IRS: residency starting and ending dates](https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates)).
- A treaty tie-breaker claim can also produce a termination date earlier than December 31 ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)).

A year with both a resident and a nonresident part is a **dual-status year**, unless a spousal election (Step 9) turns it into a full resident year.

### Step 8: consider a treaty tie-breaker (Form 8833)

The 7701(b) tests do not override treaty definitions of residence. If the client is a resident of the US under these rules and also a resident of a treaty country under that country's law, the treaty's tie-breaker may make them a resident of the other country only. Read the specific treaty. A common order, for example in the [US-Germany treaty](https://www.irs.gov/pub/irs-trty/germany.pdf), Article 4(2), is: permanent home available; if a home in both, centre of vital interests (closer personal and economic relations); then habitual abode; then nationality; then mutual agreement between the competent authorities.

- **Effect.** A client treated as a resident of the treaty country computes their US income tax as a nonresident alien. For purposes other than figuring the tax they are still treated as a US resident, and their residency time periods do not change ([Pub. 519, ch. 1, "Effect of Tax Treaties"](https://www.irs.gov/publications/p519)).
- **Filing.** File Form 1040-NR with Form 8833 attached and compute the tax as a nonresident ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519); [Form 8833](https://www.irs.gov/pub/irs-pdf/f8833.pdf)). A return must be filed to make the disclosure. A dual-resident taxpayer may also ask for US competent authority assistance under Rev. Proc. 2015-40.
- **Penalty.** Failure to disclose a treaty-based return position carries a penalty of USD 1,000 per failure for an individual, waivable for reasonable cause and good faith ([26 U.S.C. 6712](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6712.htm)).
- **Green card holders: the long-term resident trap.** A green card holder can claim a tie-breaker ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519), citing 7701(b)(6)(B)). But an LPR who starts to be treated as a resident of the treaty country, does not waive the treaty benefits and notifies the IRS **stops being an LPR for tax purposes** ([26 U.S.C. 7701(b)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)). Form 8833 warns that a dual-resident long-term resident who files it to be treated as a foreign resident is deemed to have terminated US residency and may be subject to tax under section 877A, with Form 8854 due ([Form 8833](https://www.irs.gov/pub/irs-pdf/f8833.pdf)). Filing Form 1040-NR as a nonresident can also put the green card itself at risk under immigration law. Run `us-expatriation-exit-tax` **before** the claim is made.
- **Barbados and Jamaica.** Certain nonresident students from Barbados and Jamaica, and trainees from Jamaica, may elect under those treaties to be treated as resident aliens, on Form 1040 with a signed election statement; it lasts while they remain eligible and ends only with competent authority permission ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)).

### Step 9: married clients, consider the spousal elections

Both elections treat the electing spouse as a resident for the **whole** year, so both spouses are taxed on worldwide income and the dual-status restrictions do not apply ([26 U.S.C. 6013(g) and (h)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartB-sec6013.htm); [Pub. 519, ch. 1](https://www.irs.gov/publications/p519)).

| | Section 6013(h), "Choosing resident alien status" | Section 6013(g), "Nonresident spouse treated as a resident" |
| --- | --- | --- |
| Who | Client was a nonresident alien at the start of the year and a resident at the end, and is married on December 31 to a citizen or resident. Includes both spouses arriving in the same year. Not available if single at year-end | On December 31 one spouse is a nonresident alien and the other is a citizen or resident |
| Duration | That year only. The couple can never make it again, even after separation, divorce or remarriage | That year and every later year until revoked, ended by death or legal separation, or terminated by the IRS for missing records; it does not apply in a year when neither spouse is a citizen or resident at any time. Once ended, never again for that couple |
| Treaty | Both taxed on worldwide income | Neither spouse can claim under a treaty not to be a US resident while it applies |
| Return | Joint Form 1040 for the year: checkbox in the Filing Status section, name of the dual-status spouse, statement signed by both | Joint Form 1040 for the first year with a statement signed by both; joint or separate returns in later years |

Either can be made on an amended joint return (Form 1040-X) generally within 3 years of filing the original return or 2 years of paying the tax, whichever is later; any later-year returns must then be amended too. A revocation of 6013(g) applies from the first year whose return due date has not yet passed ([26 U.S.C. 6013(g)(4)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartB-sec6013.htm); [IRS: nonresident spouse](https://www.irs.gov/individuals/international-taxpayers/nonresident-spouse)).

### Step 10: dual-status year, what is taxed and the restrictions

For the resident part of the year the client is taxed on income from all sources; foreign income received while resident is taxable even if earned while nonresident. For the nonresident part they are taxed on US-source income and effectively connected income; foreign income received while nonresident and not effectively connected is not taxable, even if earned while resident ([Pub. 519, ch. 6](https://www.irs.gov/publications/p519)). Restrictions on a dual-status return ([Pub. 519, ch. 6, "Restrictions for Dual-Status Taxpayers"](https://www.irs.gov/publications/p519); [IRS: taxation of dual-status individuals](https://www.irs.gov/individuals/international-taxpayers/taxation-of-dual-status-individuals)):

- no standard deduction; allowable itemized deductions only;
- no head of household rates;
- no joint return unless 6013(g) or (h) is elected;
- a married client who does not elect uses married-filing-separately rates for effectively connected income (some married residents of Canada, Mexico or South Korea, and married US nationals, who lived apart from their spouse for the last 6 months of the year may file as single);
- no education credits, earned income credit, or credit for the elderly or disabled unless married and electing full-year residence with a joint return;
- US-source income of the nonresident part that is not effectively connected is taxed at a flat 30% or a lower treaty rate, with no deductions against it.

The tax itself is computed in `us-form-1040-individual-return` (resident part) and under the nonresident rules in Pub. 519 chapter 4.

### Step 11: other timing rules

- **Fiscal-year taxpayers.** An alien who has not established a taxable year has the calendar year. A resident whose taxable year is not the calendar year is resident for the part of it within the calendar year of residence ([26 U.S.C. 7701(b)(9)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)).
- **Leaving and coming back.** An alien who was resident for a period including at least 3 consecutive calendar years, stops being resident and becomes resident again before the end of the 3rd calendar year after that period, is taxed for the gap under section 877(b) if that tax is more than the normal nonresident tax ([26 U.S.C. 7701(b)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)). Refer (R-RES-RETURN).

Order matters: counting days before removing exempt-individual days makes students and scholars wrongly resident, and a treaty tie-breaker claimed before the long-term resident check can make a green card holder an expatriate.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Weighted total exactly 183 | Test met ("equals or exceeds") |
| 30 days in 2026, weighted total over 183 | Test not met: the 31-day minimum fails |
| 183 or more days in 2026 | Test met on 2026 days alone; closer connection exception not available; only a treaty can help |
| Fewer than 183 days in 2026, test met, foreign tax home all year | Closer connection exception available with a timely Form 8840, unless green card steps were taken |
| Green card holder living abroad for years | Still resident until abandonment is formally effective; the closer connection exception does not apply |
| Green card holder claims a treaty tie-breaker | Nonresident for computing the tax, but may stop being an LPR and, if a long-term resident, expatriate: `us-expatriation-exit-tax` first |
| F-1 student in the 6th calendar year | Days count unless no intent to reside permanently is shown and Form 8843 is filed |
| J-1 researcher exempt in 2 of the last 6 years, US-paid | Not exempt; all 2026 days count |
| A-3 or G-5 household worker | Counts every day |
| NATO visa dependant | Counts every day |
| Arrival visit of 10 days or fewer before the real move | Can be disregarded for the starting date with a signed statement; still counted in the 183 |
| Arrival visit longer than 10 consecutive days | Cannot be split; the starting date is the first day of that visit |
| Leaves mid-2026 and returns at any time in 2027 | Resident through December 31, 2026 |
| Not resident in 2026, will be resident in 2027, arrived late in 2026 | First-year choice possible; return waits until the 2027 test is met |
| Married on December 31 to a citizen or resident | 6013(g) or (h) can replace dual status with a full-year joint return |
| Dual citizen holding US citizenship | Resident by citizenship; no treaty tie-breaker escapes it |

## Worked cases

**Case 1, a decision: an engineer moving to the US in 2026, resident from which date?** A German engineer visited the US on business for 60 days in 2024 and 120 days in 2025 (B-1 visits, German employer, home and tax home in Munich). In 2026 she attended a five-day meeting in New York from January 12 to 16 (5 days), went home, then transferred on an L-1 visa and lived in the US from May 1 to December 31 (245 days). She has no green card and was never an exempt individual.

2025 first: 120 + 60/3 = 140, below 183, so she was not resident in 2025 and the first-year rule applies to 2026. 2026: present 5 + 245 = 250 days, at least 31. Weighted total 250 + 120/3 + 60/6 = 250 + 40 + 10 = 300, which equals or exceeds 183: she meets the substantial presence test. With 250 days (183 or more) the closer connection exception is not available, so she is resident for 2026. The question is from when.

- **Without a statement:** her residency starting date is her first day of presence, **January 12, 2026**. Her German salary from January 17 to April 30 falls in the resident period and is taxed by the US (with a foreign tax credit, `us-foreign-tax-credit-1116`).
- **With the 10-day statement:** the January visit is one run of 5 consecutive days, 10 or fewer, and on those days she had a German tax home and a closer connection to Germany. She signs the statement under penalties of perjury and files it by the Form 1040-NR due date, and her residency starting date is **May 1, 2026**. The 5 days still count in the 300.

Recommend the statement: it moves about three and a half months of foreign salary out of the resident period. 2026 is a dual-status year (nonresident to April 30, resident from May 1): Form 1040 marked "Dual Status Return" with a Form 1040-NR statement for the nonresident part, due April 15, 2027, unless she is married on December 31 to a resident and both elect under 6013(h). Had the January trip lasted 12 consecutive days, no part of it could be disregarded (more than 10, and a run is excluded whole or not at all), and residency would start on the first day of that trip.

```oa-check
name: Arrival year 2026, substantial presence test and the 10-day rule
inputs:
  days_2024: 60
  days_2025: 120
  january_visit_days: 5
  main_stay_days: 245
steps:
  - weighted_2025: days_2025 + days_2024 / 3
  - resident_2025: min(floor(weighted_2025 / 183), 1)
  - days_2026: january_visit_days + main_stay_days
  - weighted_2026: days_2026 + days_2025 / 3 + days_2024 / 6
  - spt_met_2026: min(floor(weighted_2026 / 183), 1) * min(floor(days_2026 / 31), 1)
  - closer_connection_open: 1 - min(floor(days_2026 / 183), 1)
  - visit_can_be_disregarded: 1 - min(floor(january_visit_days / 11), 1)
expected:
  weighted_2025: 140
  resident_2025: 0
  days_2026: 250
  weighted_2026: 300
  spt_met_2026: 1
  closer_connection_open: 0
  visit_can_be_disregarded: 1
```

**Case 2: a consultant under 183 days who keeps a foreign home.** A Canadian consultant was in the US on 150 days in 2024, 120 days in 2025 and 122 days in 2026, working on projects for US clients. Her permanent home, family, car, bank and driver's licence are in Toronto, where her business is based all year, and she has never applied for a green card. Weighted total for 2026: 122 + 120/3 + 150/6 = 122 + 40 + 25 = 187: test met. She was present on fewer than 183 days in 2026 and her tax home was in Canada for the whole year, so she can be a nonresident for 2026 by filing Form 8840 (2026), naming Canada in Part II, by the Form 1040-NR due date: June 15, 2027 if she has no US wages subject to withholding, attached to her Form 1040-NR if she must file one for US-source income. If she misses it, she is resident for 2026 unless she can show by clear and convincing evidence that she took reasonable steps to learn of and comply with the requirement. Had she spent 183 days in 2026, Form 8840 would be closed and only the US-Canada treaty tie-breaker, on Form 1040-NR with Form 8833, could make her a nonresident for tax.

```oa-check
name: Closer connection exception available, 2026
inputs:
  days_2024: 150
  days_2025: 120
  days_2026: 122
steps:
  - weighted_2026: days_2026 + days_2025 / 3 + days_2024 / 6
  - spt_met_2026: min(floor(weighted_2026 / 183), 1) * min(floor(days_2026 / 31), 1)
  - under_183_days: 1 - min(floor(days_2026 / 183), 1)
expected:
  weighted_2026: 187
  spt_met_2026: 1
  under_183_days: 1
```

**Case 3: exactly 183, and one day short.** An H-1B worker was in the US on 150 days in 2026, 99 days in 2025 and none in 2024: 150 + 99/3 = 150 + 33 = 183. That equals 183, so the test is met. With 150 days the closer connection exception is open in principle, but it needs a foreign tax home all year, and a worker whose job is in the US normally has a US tax home, so it fails. With 96 days in 2025 instead, the total is 150 + 32 = 182: below 183, nonresident for 2026 unless she holds a green card or makes the first-year choice.

**Case 4: 183 days and a treaty.** A consultant spent 183 days in the US in 2026, keeping her home, family and employer in Germany with a German tax home all year. The test is met on 2026 days alone and the closer connection exception is closed (it needs fewer than 183 days). If she is resident in Germany under German law, the US-Germany Article 4(2) tie-breaker (permanent home first) may make her a German resident for the treaty. She then files Form 1040-NR with Form 8833 and computes US tax as a nonresident; leaving out Form 8833 risks the USD 1,000 penalty under 26 U.S.C. 6712.

**Case 5: F-1 student in her sixth year.** A student arrived in F-1 status in August 2021 and was exempt as a student in 2021, 2022, 2023, 2024 and 2025: 5 calendar years, because part-years count. In 2026 her days count unless she establishes that she does not intend to reside permanently in the US and has substantially complied with the visa. With 330 days in 2026 she meets the test on 2026 days alone. She was not resident in 2025, so she is resident from her first day of presence in 2026. If she qualifies to stay exempt, she files Form 8843 (2026) and remains a nonresident.

**Case 6: J-1 researcher, third year.** A J-1 researcher paid by a US university was exempt as a teacher or trainee in 2024 and 2025. For 2026 she was exempt in part of 2 of the 6 preceding years, so she is **not** an exempt individual, and all 2026 days count. If a foreign employer had paid all her compensation in 2026 and in each earlier year as a researcher, she would stay exempt, because she was exempt in no more than 3 of the 6 prior years.

**Case 7: first-year choice for 2026, filed in 2027.** A client arrives on November 3, 2026, stays to December 3 (31 consecutive days), is away December 4 to 10 (7 days) and is back from December 11 to 31 (21 days). He was not in the US in 2024 or 2025. For 2026 he is not resident (52 days, weighted 52). The testing period, November 3 to December 31, is 59 days; he was present 31 + 21 = 52 days; 75% of 59 is 44.25, and 52 exceeds it, so the 5-day allowance is not needed. If he meets the 2027 test (he needs at least 166 days in 2027, because 52/3 is 17.33 and 183 minus 17.33 is 165.67), he can choose residency from **November 3, 2026**. He cannot file the 2026 Form 1040 with the choice statement until the 2027 test is met, so he files Form 4868 by April 15, 2027, pays the tax figured as if nonresident all year, and files by October 15, 2027.

**Case 8: leaving mid-year.** A client present every day of 2024 and 2025 left for good on June 30, 2026 for a new job and home in Singapore. 181 days in 2026 plus one-third of the 2025 days and one-sixth of the 2024 days is far over 183: test met. With a Singapore tax home and closer connection from July 1, 2026 and no US residency in 2027, the termination date is June 30, 2026, if the signed statement is filed by the Form 1040-NR due date; otherwise December 31, 2026. 2026 is dual-status: Form 1040-NR marked "Dual Status Return" with a Form 1040 statement for the resident part, due April 15, 2027 if he received wages subject to US withholding, otherwise June 15, 2027 ([Instructions for Form 1040-NR](https://www.irs.gov/pub/irs-pdf/i1040nr.pdf)). If he comes back to live in the US before the end of 2029, check 7701(b)(10).

**Case 9: green card holder moving abroad.** A client who has held a green card since 2014 files Form I-407 with the card at a US consulate on March 31, 2026, with proof of filing. His LPR status ends that day. He is resident from January 1, 2026 (resident in 2025) to his termination date: March 31, 2026, if he has a foreign tax home and closer connection for the rest of 2026, files the statement with the abandonment evidence, and is not resident in 2027. He was an LPR in every year from 2014 to 2026, so he is a long-term resident whose expatriation date is March 31, 2026: run `us-expatriation-exit-tax` for the covered expatriate tests and Form 8854, which is due whether or not he is covered. Had he kept the card and claimed a treaty tie-breaker on a 2026 Form 1040-NR with Form 8833 instead, the result would also have been an expatriation date.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-RES-DAYS | No day count built from records for all three years | Refuse to state a conclusion until the schedule exists |
| R-RES-LTR | Green card holder considering a treaty tie-breaker or surrendering the card, or abroad for years without filing | Refer, and run `us-expatriation-exit-tax`: valuation and relief need a specialist |
| R-RES-LTRCOUNT | Long-term resident count close to the line, involves part-years, or includes years claimed as treaty-resident | Refer |
| R-RES-COVERED | Client may be a covered expatriate (net worth, five-year tax average, unfiled years) | Refer, via `us-expatriation-exit-tax` |
| R-RES-TREATY | Tie-breaker where the permanent home or centre of vital interests is genuinely unclear, or the treaty has special residence rules | Refer: the answer depends on that treaty's text, and competent authority may be needed |
| R-RES-DIPLOMAT | Diplomat or international organization staff where status or immunity is unclear | Refer |
| R-RES-LATE | Late Form 8840, Form 8843, residency-date statement or first-year choice | Refer: relief needs clear and convincing evidence and is fact-specific |
| R-RES-RETURN | Former long resident returning within 3 years (7701(b)(10)) | Refer: section 877(b) computation |
| R-RES-STATE | State residency | Federal status does not decide it: use the state skill |

## Filing and payment

- **Resident all year, or resident at year-end in a dual-status year:** Form 1040 for 2026, due April 15, 2027; an extension on Form 4868 by that date runs to October 15, 2027 and does not extend the time to pay. A dual-status client resident on December 31 checks "Other" at the top, writes "Dual Status Return", and attaches a statement for the nonresident part (Form 1040-NR can be used, marked "Dual Status Stmt") ([Pub. 519, ch. 6 "Forms To File" and ch. 7](https://www.irs.gov/publications/p519)).
- **Nonresident at year-end, including dual-status departures and treaty tie-breaker claims:** Form 1040-NR for 2026, due April 15, 2027 if the client received wages subject to US income tax withholding, otherwise June 15, 2027. Form 4868 extends an April 15 return to October 15, 2027 and a June 15 return to December 15, 2027. A departing dual-status client checks "Other", writes "Dual Status Return" and attaches a Form 1040 statement for the resident part. A due date on a Saturday, Sunday or legal holiday moves to the next business day ([Instructions for Form 1040-NR (2025)](https://www.irs.gov/pub/irs-pdf/i1040nr.pdf); [Pub. 519, ch. 7](https://www.irs.gov/publications/p519)).
- **E-filing dual-status returns:** for tax year 2025 dual-status taxpayers cannot e-file and paper-file at the address in the instructions ([Pub. 519 (2025), ch. 6](https://www.irs.gov/publications/p519)). Check the 2026 instructions before assuming the same for 2026.
- **Form 8840 and Form 8843:** attach to the 2026 Form 1040-NR. If no return is required, mail on its own to the Department of the Treasury, Internal Revenue Service Center, Austin, TX 73301-0215, by the Form 1040-NR due date including extensions. Each person files a separate form ([Form 8840 (2026)](https://www.irs.gov/pub/irs-pdf/f8840.pdf); [Form 8843 (2026)](https://www.irs.gov/pub/irs-pdf/f8843.pdf)).
- **Residency starting-date statement (10-day rule):** signed and dated under penalties of perjury; name, address, US TIN and visa number if any, passport number and issuing country, the tax year, the first and last days present in the year, the dates excluded, and facts showing the foreign tax home and closer connection for those days. Attach to the return or send to Austin by the Form 1040-NR due date ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)).
- **Residency termination-date statement:** signed and dated under penalties of perjury; the same identity details, the last day present, facts showing the foreign tax home and closer connection after it, the date LPR status was abandoned or rescinded with copies of the documents, and any de minimis days excluded. Same deadline ([Pub. 519, ch. 1](https://www.irs.gov/publications/p519)).
- **Form 8833:** attach to Form 1040-NR; a separate form for each treaty-based position ([Form 8833](https://www.irs.gov/pub/irs-pdf/f8833.pdf)).
- **First-year choice statement:** attach to the 2026 Form 1040: name and address; that the client makes the first-year choice for 2026; that they were not resident in 2025; that they are resident under the substantial presence test in 2027, with the number of 2027 days; the dates of the 31-day period and the period of continuous presence in 2026; and the dates of absence treated as presence. Neither return nor statement can be filed until the 2027 test is met. If that has not happened by April 15, 2027, file Form 4868 (to October 15, 2027) and pay with it the tax figured as if nonresident all of 2026 (Form 1040-NR can be used to figure it); interest and late-payment penalties run on tax not paid by April 15. Not following the procedure means nonresident for all of 2026, unless the clear-and-convincing-evidence relief applies ([Pub. 519, ch. 1, "First-Year Choice"](https://www.irs.gov/publications/p519)).
- **Spousal elections:** the Filing Status checkbox and signed statement on the joint Form 1040 (Step 9).
- **Form 8854** (long-term residents): with the return for the year that includes the expatriation date; figures and penalty in `us-expatriation-exit-tax`.

**2025 returns still open.** The same tests apply with 2025, 2024 and 2023 days, using the 2025 Pub. 519 and the 2025 Forms 8840 and 8843. The extended deadline for 2025 Forms 1040 and April-due Forms 1040-NR (October 15, 2026) has passed; a 2025 Form 1040-NR originally due June 15, 2026 and extended with Form 4868 is due **December 15, 2026** ([Pub. 519 (2025), ch. 7](https://www.irs.gov/publications/p519)). Late Form 8840 or Form 8843 for 2025: R-RES-LATE.

## Completion checklist

- Citizenship confirmed; green card history and any I-407 or orders recorded with dates and proof.
- Three-year day-count schedule (2024, 2025, 2026) tied to travel records, with each excluded day and its reason, and the exempt-year history for F, J, M and Q years.
- Test arithmetic shown, checking both "at least 31" and "equals or exceeds 183", for 2026 and, for an arrival year, for 2025.
- Closer connection, first-year choice and spousal elections each tested, with Forms 8840 and 8843 and the statements prepared by the due date.
- Residency starting and termination dates fixed, with any 10-day exclusion statement.
- Treaty position: the specific treaty article applied, Form 8833 attached, and the long-term resident check run **before** claiming.
- Correct return (Form 1040 or 1040-NR, "Dual Status Return" where applicable) and due date recorded.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 7701(b) (govinfo, 2024 edition). Read for (b)(1) the three routes to residence, (b)(2) first and last year and the 10-day rule, (b)(3) the 31-day and 183-day test, multipliers 1, 1/3, 1/6 and the closer connection exception, (b)(4) the first-year election (31 consecutive days, 75 percent, 5 days), (b)(5) exempt individuals and the 2-year, 4-year and 5-year limits, (b)(6) LPR and the treaty sentence, (b)(7) presence, commuters, transit, crew, (b)(9) taxable year and (b)(10) the 3-year rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm | 2026-11-13 |
| Public Law 119-21 (One Big Beautiful Bill Act), govinfo. Read (searched) for any amendment to 7701(b), 6013 or 877A; found only new 7701(a)(51) and (a)(52) definitions, none touching individual residence. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 6013 (govinfo). Read for (g) nonresident spouse election, duration, termination and one-election rule, and (h) the year-of-arrival joint return election. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartB-sec6013.htm | 2026-11-13 |
| 26 U.S.C. 6712 (govinfo). Read for the USD 1,000 penalty per failure to disclose a treaty-based position and the reasonable cause waiver. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6712.htm | 2026-11-13 |
| IRS Pub. 519 (2025), U.S. Tax Guide for Aliens, PDF. Read for Reminders, chapter 1 in full (green card test, abandonment, days of presence, commuters 75%, transit, exempt individuals, Form 8843, closer connection, treaties, dual status, first-year choice, 6013 choices, last year of residency, statements), chapter 6 (income subject to tax, restrictions, forms, e-file caution) and chapter 7 (due dates and extensions). | https://www.irs.gov/pub/irs-pdf/p519.pdf | 2026-11-13 |
| IRS Pub. 519 web edition (the same 2025 text), cited for section names. | https://www.irs.gov/publications/p519 | 2026-11-13 |
| Form 8840 (2026). Read for the eligibility notes, the 2026 test wording, two-country rule, tax home, permanent home, when and where to file and the penalty for not filing. | https://www.irs.gov/pub/irs-pdf/f8840.pdf | 2026-11-13 |
| Form 8843 (2026). Read for the A-3 and G-5 rule, teacher and trainee 2 of 6 years and the four-part exception, students over 5 calendar years, medical condition limits, where to file and the penalty for not filing. | https://www.irs.gov/pub/irs-pdf/f8843.pdf | 2026-11-13 |
| Form 8833 (Rev. December 2022). Read for the USD 1,000 penalty line, the dual-resident box and the long-term resident note on termination of residency and Form 8854. | https://www.irs.gov/pub/irs-pdf/f8833.pdf | 2026-11-13 |
| Instructions for Form 1040-NR (2025). Read for "When and Where Should You File?": 15th day of the 4th month with withheld wages, otherwise the 6th month, and the weekend rule. | https://www.irs.gov/pub/irs-pdf/i1040nr.pdf | 2026-11-13 |
| US-Germany income tax treaty (IRS copy). Read for Article 4(2) tie-breaker order and Protocol paragraph 1(a), the saving clause. | https://www.irs.gov/pub/irs-trty/germany.pdf | 2026-11-13 |
| IRS: Substantial presence test. Read for the test, excluded days, the definition of United States and the Form 8843 timing consequence. | https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test | 2026-11-13 |
| IRS: Residency starting and ending dates. Read for the green card date, a card received abroad, both tests, the exempt-individual note and residency in the next year. | https://www.irs.gov/individuals/international-taxpayers/residency-starting-and-ending-dates | 2026-11-13 |
| IRS: Closer connection exception to the substantial presence test. Read for the conditions and Form 8840. | https://www.irs.gov/individuals/international-taxpayers/closer-connection-exception-to-the-substantial-presence-test | 2026-11-13 |
| IRS: Green card test. Read for the test and when status ends. | https://www.irs.gov/individuals/international-taxpayers/alien-residency-green-card-test | 2026-11-13 |
| IRS: Taxation of dual-status individuals. Read for the dual-status restrictions. | https://www.irs.gov/individuals/international-taxpayers/taxation-of-dual-status-individuals | 2026-11-13 |
| IRS: Nonresident spouse. Read for the 6013(g) and (h) choices and amended-return timing. | https://www.irs.gov/individuals/international-taxpayers/nonresident-spouse | 2026-11-13 |
| IRS: U.S. citizens and resident aliens abroad. Read for worldwide taxation of citizens and residents wherever they live. | https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad | 2026-11-13 |
| Instructions for Form 8854 (2025). Read for the long-term resident definition and expatriation date, used here only to point to `us-expatriation-exit-tax`. | https://www.irs.gov/instructions/i8854 | 2026-11-13 |

Not yet confirmed: the 2026 edition of Pub. 519 and the 2026 Instructions for Form 1040-NR were not published when read (the rules above come from the statute, the 2026 Forms 8840 and 8843, and the 2025 Pub. 519 and 1040-NR instructions); the 2026 due dates (April 15, June 15, October 15 and December 15, 2027) are worked from the statutory "15th day of the 4th or 6th month" rule and the 6-month Form 4868 extension, not quoted from a 2026 page; whether dual-status 2026 returns can be e-filed is not yet stated by the IRS; the Treasury Regulations under 7701(b) (301.7701(b)-1 to -9) were not opened for this version, so points that rest only on them (for example the regulation's examples of other Code purposes for which a treaty-resident stays a US resident) are left out.
