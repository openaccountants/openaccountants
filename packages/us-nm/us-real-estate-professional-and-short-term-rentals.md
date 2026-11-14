---
name: us-real-estate-professional-and-short-term-rentals
description: US federal passive activity loss rules for rental property owners in tax year 2026 - why rental losses are passive, the $25,000 active participation allowance and its phase-out between $100,000 and $150,000 of modified AGI, real estate professional status (the more-than-half and more-than-750-hour tests, spouses, the election to treat all rentals as one activity and Rev. Proc. 2011-34 late relief), the seven material participation tests, the short-term rental rule (average stay of seven days or less, or 30 days or less with significant personal services), personal use under section 280A, the excess business loss limit ($256,000, $512,000 joint), Form 8582, records and when to refer. Trigger on "real estate professional", "REPS", "750 hours", "short-term rental loophole", "Airbnb loss", "passive loss", "Form 8582", "material participation". Federal only.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: situation-rules
---

# Rental losses, real estate professional status and the short-term rental rule, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 280A, 461 and 469, Treas. Reg. 1.469-1, 1.469-1T, 1.469-5T and 1.469-9, IRS Pub. 925, the Instructions for Forms 8582 and 461, Rev. Proc. 2011-34, Rev. Proc. 2025-32 and Public Law 119-21 section 70601, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A rental loss is **passive by default** and cannot offset wages or business profit; it carries forward until there is passive income or a full taxable sale. Three routes out, each tested every year: (1) the **USD 25,000 active participation allowance**, cut by 50% of modified AGI over **USD 100,000** and gone at **USD 150,000**; (2) **real estate professional status** (more than half of all personal services, and **more than 750 hours**, in real property businesses in which the taxpayer materially participates, one spouse alone meeting both) **plus material participation** in the rental; (3) a **short-term rental** with an **average stay of seven days or less** (or 30 days or less with significant personal services) is not a rental activity at all, so **material participation** alone (for example more than 100 hours and not less than anyone else) makes the loss non-passive. A full-time employee almost never meets the half test. Losses that clear these rules still meet the **excess business loss** limit of **USD 256,000 (USD 512,000 joint)** for 2026.

## Scope and who this is for

In scope: an individual who owns rental property, often a high-earning employee or business owner who owns or plans to buy rentals, and the adviser, for tax year 2026: section 469 as it applies to rentals, active participation, real estate professional status, material participation, the short-term rental rule, Form 8582 and the records.

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| Rental income and expenses on Schedule E | `us-schedule-e-rental-income` |
| Cost segregation studies, asset classes and methods | `us-federal-cost-segregation` |
| Bonus depreciation and section 179 | `us-section-179-and-bonus-depreciation` |
| Deferring gain by exchange | `us-section-1031-like-kind-exchange` |
| Renting your home to your own business for under 15 days | `us-augusta-rule-home-rental-to-your-business` |
| Net operating loss carryovers | `us-net-operating-loss-172` |
| State treatment | the state's own rules; states may not follow federal bonus depreciation or the passive rules |

## Ask the client first

1. **Hours in 2026 for each spouse** in every job and business, including employment, and in real estate work, and who can show it.
2. **For each property:** the average guest stay, the personal-use days, and who else (manager, cleaner, contractor) worked on it and for how many hours.
3. **Ownership:** is any rental held through a limited partnership, an LLC taxed as a partnership or an S corporation, and what percentage does the client own?
4. **Has the client ever filed a section 1.469-9(g) election** to treat all rentals as one activity, and in which year?
5. **Expected modified AGI,** and suspended passive losses carried in from earlier years, by property.
6. **Is a sale, exchange or transfer to a family member planned?**

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Active participation allowance, maximum per year (single or joint; not indexed) | USD 25,000 | [26 U.S.C. 469(i)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Allowance phase-out starts at modified AGI above | USD 100,000 | [26 U.S.C. 469(i)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Reduction per dollar of modified AGI above the start | 50 percent | [26 U.S.C. 469(i)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Allowance fully gone at modified AGI of (USD 75,000 married filing separately) | USD 150,000 | [IRS Pub. 925](https://www.irs.gov/pub/irs-pdf/p925.pdf) |
| Married filing separately, lived apart all year: maximum (phase-out start USD 50,000) | USD 12,500 | [26 U.S.C. 469(i)(5)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Active participation: minimum ownership by value with the spouse, whole period | 10 percent | [26 U.S.C. 469(i)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Real estate professional, test (i): share of all personal services in real property businesses with material participation | more than one-half | [26 U.S.C. 469(c)(7)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Real estate professional, test (ii): hours in those businesses | 750 hours (more than) | [26 U.S.C. 469(c)(7)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Employee work counts as real property work only for an owner of more than | 5 percent | [26 U.S.C. 469(c)(7)(D)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Short-term rental exception (A): average period of customer use | seven days or less | [Treas. Reg. 1.469-1T(e)(3)(ii)(A)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-1T) |
| Short-term rental exception (B): average period, with significant personal services | 30 days or less | [Treas. Reg. 1.469-1T(e)(3)(ii)(B)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-1T) |
| Material participation test (a)(1) | more than 500 hours | [Treas. Reg. 1.469-5T(a)(1)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-5T) |
| Material participation test (a)(3), and the floor for (a)(7) | more than 100 hours | [Treas. Reg. 1.469-5T(a)(3), (b)(2)(iii)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-5T) |
| Residence test for a dwelling: personal-use days must exceed the greater of 14 days or 10 percent of fair-rental days | 14 days | [26 U.S.C. 280A(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280A.htm) |
| Excess business loss threshold, taxable years beginning in 2026 | USD 256,000 | [Rev. Proc. 2025-32, section 4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess business loss threshold, joint returns | USD 512,000 | [Rev. Proc. 2025-32, section 4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

### Steps

1. **Classify each property for the year.** Work out the average period of customer use under [Treas. Reg. 1.469-1(e)(3)(iii)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-1) and test the exceptions in Treas. Reg. 1.469-1T(e)(3)(ii). Note the result (rental activity, or not a rental activity) and go to step 2 either way.
2. **Personal use of any dwelling** under section 280A(d)(1), whether or not it is a rental activity. If the owner used it as a residence, section 280A(c)(5) caps the deductions from the rental use at the gross rental income less the deductions allowable anyway, and for a passive activity section 469(j)(10) leaves the items from that use out of section 469: stop here for that unit. Otherwise a rental activity goes to step 3, and a property that is not a rental activity goes to step 5.
3. **Real estate professional status** under section 469(c)(7)(B) and [Treas. Reg. 1.469-9(c)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-9), one spouse at a time. If no one qualifies, every rental real estate activity is passive: go to step 4. If someone qualifies, test material participation in each rental real estate interest, or in the single combined activity if the section 1.469-9(g) election is in force or being made.
4. **Passive rental real estate:** test active participation and apply the allowance and phase-out under section 469(i). Run Form 8582 ([Instructions for Form 8582](https://www.irs.gov/pub/irs-pdf/i8582.pdf)). Carry any disallowed loss forward under section 469(b).
5. **Not a rental activity:** decide whether it is a trade or business activity and whether the owner materially participated under Treas. Reg. 1.469-5T(a). With material participation, report on the usual forms, not Form 8582; without it, the activity is passive and goes on Form 8582.
6. **Apply the limits in order:** basis and at-risk first, then the passive loss limits, then the excess business loss limit on Form 461.
7. **On a sale,** check whether it is a fully taxable disposition of the entire interest in the activity to an unrelated party under section 469(g); if so, suspended losses from that activity are released.
8. **Keep the hours records and the election statement** with the return.

## Boundary and exception table

### Why a rental loss is passive by default

Section 469(a) denies an individual, estate or trust a "passive activity loss". A passive activity is a trade or business without material participation, and also any rental activity, except as section 469(c)(7) provides (section 469(c)(1) and (2)). So a rental is passive even if the owner works hard on it, unless the owner is a real estate professional and materially participates (Pub. 925 says the same).

- The net passive loss cannot offset wages, business profit, interest or gains; it can offset passive income from other activities.
- It is "treated as a deduction or credit allocable to such activity in the next taxable year" (section 469(b)), year after year.
- It comes free on a disposition of the entire interest in a transaction in which all gain or loss is recognized: the loss, to the extent it exceeds net passive income from all other passive activities, is then not passive. Not if the buyer is related under section 267(b) or 707(b)(1) (section 469(g)(1)).
- If an activity stops being passive (the owner becomes a real estate professional), old suspended losses offset only income from that same activity, and any remainder stays passive (section 469(f)(1)).
- Form 8582 is where the computation is made, unless the instructions' exception for small rental losses with active participation applies.

### Active participation allowance

| Rule | Detail |
| --- | --- |
| Who | A natural person who actively participated in a rental real estate activity (section 469(i)(1)). Lower bar than material participation: approving new tenants, deciding rental terms and approving expenditures count (Pub. 925) |
| Ownership | With the spouse, at least 10 percent by value for the whole period; a limited partner interest does not count (section 469(i)(6)) |
| Phase-out | A reduction, not a cliff: each dollar of modified AGI above USD 100,000 removes 50 cents of allowance |
| Modified AGI | AGI without taxable social security, without sections 219, 221 and 250 deductions, certain exclusions, and any passive activity loss or loss allowed by reason of section 469(c)(7) (section 469(i)(3)(E)) |
| Married filing separately, lived together at any time | No allowance at all (section 469(i)(5)(B)); the USD 12,500 and USD 50,000 apply only if they lived apart all year |
| Short-term rental outside the rental definition | Not rental real estate, so the allowance is not the route |

### Real estate professional status

If section 469(c)(7) applies, the rule that every rental is passive does not apply, and each interest in rental real estate is a separate activity unless the taxpayer elects to combine them (section 469(c)(7)(A)). Status alone is no deduction: a qualifying taxpayer's rental "is a passive activity under section 469 for the taxable year unless the taxpayer materially participates in the activity" (Treas. Reg. 1.469-9(e)(1)). Two gates every year: qualify, then materially participate.

| Point | Rule |
| --- | --- |
| Half test wording | "more than one-half of the personal services performed in trades or businesses by the taxpayer during such taxable year are performed in real property trades or businesses in which the taxpayer materially participates" |
| Hours test wording | "such taxpayer performs more than 750 hours of services during the taxable year in real property trades or businesses in which the taxpayer materially participates" |
| Real property businesses | "any real property development, redevelopment, construction, reconstruction, acquisition, conversion, rental, operation, management, leasing, or brokerage trade or business" (section 469(c)(7)(C)) |
| Which hours count | Only from real property businesses in which the taxpayer materially participates (Treas. Reg. 1.469-9(c)(3)) |
| Employee work | Counts in the total of personal services; counts as real property work only for a 5-percent owner of the employer (section 469(c)(7)(D)(ii); Treas. Reg. 1.469-9(c)(5)). A full-time W-2 employee almost never meets the half test |
| Investor-type work | Studying financial statements, preparing summaries for own use, monitoring finances in a non-managerial capacity: not personal services (Treas. Reg. 1.469-9(b)(4); 1.469-5T(f)(2)(ii)) |
| Joint return | Met "if and only if either spouse separately satisfies such requirements"; spouses' hours are not added for the two tests, but the other spouse's work counts in deciding which real property businesses a spouse materially participates in (Treas. Reg. 1.469-9(c)(4)) |
| Material participation once qualified | Tested with both spouses' participation combined, whether or not they file jointly (Treas. Reg. 1.469-5T(f)(3)) |

### The election to treat all rentals as one activity

| Point | Rule (Treas. Reg. 1.469-9(e), (f), (g)) |
| --- | --- |
| Without it | Each interest is separate and material participation must be shown in each; an owner of several properties rarely meets an hours test property by property |
| How | A statement with the original return for the year declaring the taxpayer is a qualifying taxpayer and is making the election under section 469(c)(7)(A) (paragraph (g)(3)) |
| When | Any year the taxpayer qualifies; not electing one year does not stop a later election |
| How long | Binding for that year and every later year the taxpayer qualifies, even after gaps; revocable only in a year of a material change in facts and circumstances (or later while it lasts), with a statement on the original return; being less advantageous is not a material change |
| Missed it | [Rev. Proc. 2011-34](https://www.irs.gov/pub/irs-drop/rp-11-34.pdf): attach the statement to an amended return for the most recent year, marked "FILED PURSUANT TO REV. PROC. 2011-34", if the only failure was timing, every affected return was filed consistently with aggregation and on time (within 6 months of the due date, excluding extensions), and there is reasonable cause. Relief does not decide qualification or material participation |
| Limited partnership interests | If the combined activity includes any, the whole activity is a limited partnership interest for material participation (only Treas. Reg. 1.469-5T(e)(2) tests), unless their gross rental income is less than ten percent of gross rental income from all rental real estate interests (paragraph (f)) |
| Selling one property | Suspended losses are released only on a disposition of the entire interest in an activity (section 469(g)); the Form 8582 instructions let a disposition of substantially all of an activity be treated separately if the losses and income allocable to the part sold are proved with reasonable certainty. Decide before electing |

### Material participation: the seven tests (Treas. Reg. 1.469-5T(a), "if and only if" one is met)

| Test | Wording |
| --- | --- |
| (a)(1) | "participates in the activity for more than 500 hours during such year" |
| (a)(2) | participation "constitutes substantially all of the participation in such activity of all individuals (including individuals who are not owners of interests in the activity)" |
| (a)(3) | "participates in the activity for more than 100 hours during the taxable year, and such individual's participation in the activity for the taxable year is not less than the participation in the activity of any other individual (including individuals who are not owners of interests in the activity)" |
| (a)(4) | a significant participation activity (a trade or business with more than 100 hours) where aggregate participation in all such activities "exceeds 500 hours" |
| (a)(5) | "materially participated in the activity ... for any five taxable years (whether or not consecutive) during the ten taxable years that immediately precede the taxable year" |
| (a)(6) | a personal service activity with material participation "for any three taxable years (whether or not consecutive) preceding the taxable year" |
| (a)(7) | "on a regular, continuous, and substantial basis during such year", on all facts and circumstances |

Limits that decide real cases: (a)(7) is closed to anyone with 100 hours or less (paragraph (b)(2)(iii)), and management time does not count for it if someone else is paid to manage or another individual spends more hours on management (paragraph (b)(2)(ii)); (a)(4) works only for trade or business activities, and a rental activity is not one (paragraph (c); Form 8582 instructions); (a)(2) and (a)(3) compare the owner with every other individual, so a manager, cleaner or contractor with more hours defeats (a)(3); work not customarily done by owners does not count if a principal purpose is to avoid the passive rules (paragraph (f)(2)(i)); investor-type work does not count unless directly involved in day-to-day management or operations (paragraph (f)(2)(ii)); a spouse's participation counts as the taxpayer's (paragraph (f)(3)); a limited partner materially participates only under (a)(1), (a)(5) or (a)(6) (section 469(h)(2)).

### The short-term rental rule

An activity involving the use of tangible property is not a rental activity for a year if (Treas. Reg. 1.469-1T(e)(3)(ii)): (A) "The average period of customer use for such property is seven days or less"; (B) "The average period of customer use for such property is 30 days or less, and significant personal services ... are provided by or on behalf of the owner of the property"; or (C) extraordinary personal services are provided, "without regard to the average period of customer use". Exceptions (D) to (F) (incidental rentals, defined business hours, property provided to the owner's own partnership or S corporation) are outside this skill.

- **Effect.** It is not a rental activity, so section 469(c)(2) does not make it passive. If it is a trade or business and the owner materially participated, the income or loss goes "on the forms or schedules normally used" and stays off Form 8582. Real estate professional status is not needed. Without material participation it is passive, and the section 469(i) allowance does not help, because that allowance is for rental real estate activities.
- **Average period.** For one class of property, total days in all periods of customer use that end in the year (or include its last day), divided by the number of those periods; each continuous or recurring right to use counts as one period, even across renewals. With classes at significantly different daily rents, weight each class's average by its share of gross rental income (Treas. Reg. 1.469-1(e)(3)(iii)).
- **Significant personal services (B).** Only services by individuals; look at frequency, labour and value compared with the rent. Not counted: services needed for lawful use, construction and major repairs, and services common with long-term rentals of high-grade property such as cleaning common areas, routine repairs, trash collection and security (Treas. Reg. 1.469-1T(e)(3)(iv)).

### Personal use and section 280A

- A dwelling is used as a residence if personal-use days exceed the greater of 14 days or 10 percent of days rented at a fair rental (section 280A(d)(1)). A day is personal use if, for any part of it, the unit is used by the owner, anyone else with an interest, a family member (section 267(c)(4)) of either, anyone under an arrangement letting the owner use another dwelling, or any individual not paying a fair rental (section 280A(d)(2)). A personal day is not a fair-rental day for the 10 percent count.
- If so and section 280A(c)(5) applies, the items from that use are not taken into account for section 469 (section 469(j)(10)); section 280A(c)(5) caps rental deductions at gross rental income after deductions allowable anyway and carries the excess forward. No loss against other income that year.
- A residence rented for less than 15 days in the year: no rental deductions, rent not in income (section 280A(g); see `us-augusta-rule-home-rental-to-your-business`).

### Pairing with cost segregation and bonus depreciation

A cost segregation study can create a large first-year loss through bonus depreciation. It reduces tax on other income only if this skill's tests are met for that year: status plus material participation for a long-term rental, or material participation in a short-term rental that is not a rental activity. Otherwise it is suspended under section 469(b). Methods live in `us-federal-cost-segregation` and `us-section-179-and-bonus-depreciation`.

### The excess business loss limit

A loss that clears the passive rules can still be limited: after at-risk and passive limits, a non-corporate taxpayer's business losses "may be subject to the excess business loss limitation", figured on Form 461 (Form 8582 instructions). The Form 461 instructions treat an activity as a trade or business if the "primary purpose for engaging in the activity is for income or profit and you're involved in the activity with continuity and regularity" ([Instructions for Form 461](https://www.irs.gov/pub/irs-pdf/i461.pdf)); no IRS page says a real estate professional's rental or a short-term rental is one automatically. The disallowed excess becomes a net operating loss carryover ([26 U.S.C. 461(l)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm)). Section 70601 of Public Law 119-21 struck "and before January 1, 2029" from section 461(l)(1) for taxable years beginning after 31 December 2026, so the limit no longer expires, and rebased its indexing to 2024 for years beginning after 31 December 2025 ([Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)).

### Records an examiner asks for

Participation may be shown "by any reasonable means"; contemporaneous daily logs are not required if participation can be shown by "appointment books, calendars, or narrative summaries" identifying the services and approximate hours (Treas. Reg. 1.469-5T(f)(4)). Prepare: a dated log of hours per property (or combined activity), per spouse, with the task, built during the year from calendars, emails, booking messages and invoices; for status, total hours in all trades or businesses including employment, with payroll or timesheets; hours of everyone else who worked on the property; for short-term rentals, the booking history and a record of personal-use days; the section 1.469-9(g) election statement and the year first made; ownership documents showing limited partnership interests and percentages; Form 8582 carryforward workpapers by activity.

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Hours log | Treat the loss as passive until a log exists |
| Employment hours of the claimed professional | Assume full-time (about 2,000 hours): half test fails |
| Hours of cleaners and managers | Assume they exceed the owner's: test (a)(3) fails |
| Average stay | Treat as a rental activity until the booking history is produced |
| Election history | Assume no election; each property tested separately |

### Red flags to raise

| Flag | Why it matters |
| --- | --- |
| Full-time W-2 employee claiming status | Half test almost never met |
| Short-term rental with a property manager doing most of the work | (a)(3) fails; likely passive |
| Large first-year cost segregation loss | Only usable if the tests are met that year; excess business loss limit next |
| Sale of one property after the aggregation election | Suspended losses may not be released |
| More than 14 personal days at a vacation home | Section 280A(c)(5) caps the loss |

## Worked cases

**Case 1, the allowance in the phase-out.** A married couple files jointly; neither is a real estate professional; they actively participate in one long-term rental. Modified AGI is USD 130,000 and the rental loss is USD 18,000. The excess over USD 100,000 is USD 30,000; half is USD 15,000; the allowance is USD 25,000 minus USD 15,000 = USD 10,000. They deduct USD 10,000 against other income and carry USD 8,000 forward as a suspended passive loss. At modified AGI of USD 400,000 the allowance is gone and the whole loss is suspended unless they have passive income: the usual position of the high earner, and the reason the other two routes matter.

```oa-check
name: Active participation allowance phase-out (2026)
inputs:
  magi: 130000
  rental_loss: 18000
  high_magi: 400000
steps:
  - allowance: max(25000 - 0.5 * max(magi - 100000, 0), 0)
  - deducted: min(rental_loss, allowance)
  - suspended: rental_loss - deducted
  - allowance_high: max(25000 - 0.5 * max(high_magi - 100000, 0), 0)
expected:
  allowance: 10000
  deducted: 10000
  suspended: 8000
  allowance_high: 0
```

**Case 2, a decision: is the cabin loss passive?** An employee with high wages buys a cabin. In 2026 it has 40 guest stays totalling 160 nights, all ending in the year: an average of 4 days, seven or less, so it is not a rental activity. The owner logs 120 hours on listing, guest messages, restocking and turnovers; the cleaning contractor logs 90; no one else more. The owner is above 100 hours and not below anyone, so test (a)(3) is met and a first-year loss of USD 70,000 (largely depreciation after a cost segregation study) is not passive: it can offset wages, subject to basis, at-risk and the excess business loss limit. Personal use: 10 days, against the greater of 14 days and 10% of 160 rental days (16 days), so 16; 10 does not exceed 16, so the cabin is not a residence. The trap: if the contractor logs 150 hours instead, the owner's 120 hours are less than another individual's, (a)(3) fails, (a)(1) fails (under 500), and (a)(7) rests on facts and circumstances with no hours figure above 100 in the regulation (the owner's management hours do count, since no one else is paid to manage or does more management). Treat the USD 70,000 as passive and suspended unless the (a)(7) case is written up.

```oa-check
name: Short-term rental classification and personal use (2026)
inputs:
  nights: 160
  stays: 40
  owner_hours: 120
  cleaner_hours: 90
  cleaner_hours_trap: 150
  personal_days: 10
steps:
  - average_stay: nights / stays
  - not_rental_activity: 1 - min(floor(average_stay / 7.01), 1)
  - meets_a3: min(floor(owner_hours / 100.01), 1) * (1 - min(floor(cleaner_hours / (owner_hours + 0.01)), 1))
  - meets_a3_trap: min(floor(owner_hours / 100.01), 1) * (1 - min(floor(cleaner_hours_trap / (owner_hours + 0.01)), 1))
  - residence_limit: max(14, 0.10 * nights)
  - used_as_residence: min(floor(personal_days / (residence_limit + 0.01)), 1)
expected:
  average_stay: 4
  not_rental_activity: 1
  meets_a3: 1
  meets_a3_trap: 0
  residence_limit: 16
  used_as_residence: 0
```

**Case 3, one spouse qualifies.** Spouse A is a full-time employed engineer with about 2,000 hours at work. Spouse B has no other job and logs 900 hours finding, renovating, leasing and managing the couple's rentals through a property business in which B materially participates. All B's working hours are real property hours, so B passes the half test, and 900 is more than 750. The joint return qualifies through B alone; A's 2,000 hours neither stop it nor count. The couple must still show material participation in each rental, or in the combined activity if they elect, counting both spouses' hours.

**Case 4, the half test fails.** A self-employed consultant works 2,000 hours consulting and 800 on rentals. Total personal services are 2,800 hours, so more than half means more than 1,400. 800 hours passes the 750-hour test but fails the half test: no status.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-RE-EMPLOYEE | A real estate professional position for a full-time employee who is not a 5-percent owner of the employer | Refuse unless the log shows real property hours in businesses with material participation exceeding all employee hours |
| R-RE-LOG | Hours built after the year from memory alone, or hours of work whose purpose is to avoid the passive rules | Refuse (Treas. Reg. 1.469-5T(f)(2)(i)) |
| R-RE-ELECT | A late election outside Rev. Proc. 2011-34, a revocation, or a grouping question under Treas. Reg. 1.469-4 | Refer |
| R-RE-TIER | Interests held through tiered partnerships or S corporations | Refer |
| R-RE-OTHEREXC | Rental exceptions (C) to (F) | Refer |
| R-RE-SALE | A related-party sale or a 1031 exchange | Refer; `us-section-1031-like-kind-exchange` |
| R-RE-STATE | State treatment | Refer |

## Filing and payment

Form 8582 goes with the 2026 Form 1040 when there is a passive loss (unless the small-loss exception applies), with rental activity on Schedule E and a non-rental short-term rental with material participation on the schedule normally used. The section 1.469-9(g) election statement is attached to the original 2026 return. Form 461 goes with the return when the excess business loss limit applies. The return is due **15 April 2027**, or 15 October 2027 on extension; the election must be on the original return, extension included.

## Completion checklist

- Each property classified (rental activity or not) from the booking history.
- Personal-use days tested under section 280A(d)(1).
- Real estate professional tests run for one spouse at a time, with all employment hours in the total.
- Material participation tested per property or per combined activity, against every other individual's hours.
- Allowance phase-out applied on the right modified AGI.
- Limits applied in order: basis, at-risk, passive, excess business loss.
- Hours log, election statement and carryforward workpapers in the file.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 469 (govinfo). Read for (a), (b), (c)(1), (2) and (7), (f)(1), (g), (h), (i) USD 25,000, USD 100,000, 50 percent, USD 12,500, 10 percent, and (j)(10). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm | 2026-11-13 |
| 26 U.S.C. 280A (govinfo). Read for (c)(5), (d)(1) and (2), and (g). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280A.htm | 2026-11-13 |
| 26 U.S.C. 461 (govinfo). Read for (l)(2), the net operating loss carryover. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm | 2026-11-13 |
| Treas. Reg. 1.469-1 (eCFR). Read for (e)(3)(iii), average period of customer use. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-1 | 2026-11-13 |
| Treas. Reg. 1.469-1T (eCFR). Read for (e)(3)(ii) exceptions (seven days or less, 30 days or less) and (e)(3)(iv). | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-1T | 2026-11-13 |
| Treas. Reg. 1.469-5T (eCFR). Read for (a) the seven tests, (b)(2), (c), (e)(2) and (f). | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-5T | 2026-11-13 |
| Treas. Reg. 1.469-9 (eCFR). Read for (b)(4), (c), (e)(1), (f) and (g). | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR3dff4ee5ffb0ae6/section-1.469-9 | 2026-11-13 |
| IRS Pub. 925 (2025). Read for rentals as passive, active participation examples and USD 150,000 / USD 75,000. | https://www.irs.gov/pub/irs-pdf/p925.pdf | 2026-11-13 |
| Instructions for Form 8582 (2025). Read for the small-loss exception, non-rental activities, order of limits and partial dispositions. | https://www.irs.gov/pub/irs-pdf/i8582.pdf | 2026-11-13 |
| Instructions for Form 461 (2025). Read for the trade or business test. | https://www.irs.gov/pub/irs-pdf/i461.pdf | 2026-11-13 |
| Rev. Proc. 2011-34. Read for late election relief. | https://www.irs.gov/pub/irs-drop/rp-11-34.pdf | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.31, USD 256,000 (USD 512,000 joint). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21, section 70601. Read for the permanent excess business loss limit and its effective dates. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |

Not yet confirmed: the 2026 Pub. 925 and the 2026 Instructions for Forms 8582 and 461 were not yet published when read; the statutory rules are not indexed and did not change for 2026, so the 2025 editions are used.
