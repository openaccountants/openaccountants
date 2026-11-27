---
name: us-real-estate-professional-and-short-term-rentals
description: US federal passive activity loss rules for rental property owners in tax year 2026 - why rental losses are passive, the $25,000 active participation allowance and its phase-out between $100,000 and $150,000 of modified AGI, real estate professional status (the more-than-half and more-than-750-hour tests, spouses, the election to treat all rentals as one activity and Rev. Proc. 2011-34 late relief), the seven material participation tests, the short-term rental rule (average stay of seven days or less, or 30 days or less with significant personal services), personal use under section 280A, the excess business loss limit ($256,000, $512,000 joint), Form 8582, records and when to refer. Trigger on "real estate professional", "REPS", "750 hours", "short-term rental loophole", "Airbnb loss", "passive loss", "Form 8582", "material participation". Federal only.
version: "3.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: situation-rules
---

# Rental losses, real estate professional status and the short-term rental rule, tax year 2026

> **Built from the law. Not yet approved.** Built from 26 U.S.C. 280A, 461 and 469, Treas. Reg. 1.469-1, 1.469-1T, 1.469-5T and 1.469-9, the Instructions for Forms 8582 and 461, Rev. Proc. 2011-34, Rev. Proc. 2025-32 and Public Law 119-21 section 70601, read on 2026-11-27. No professional approval is claimed. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A rental loss is **passive by default** and generally cannot offset wages or nonpassive business profit except through an applicable allowance. Disallowed losses carry forward; apply the allowance again in a later eligible year, offset passive income, or test a qualifying entire disposition. Three routes out, each tested every year: (1) the **USD 25,000 active participation allowance**, cut by 50% of modified AGI over **USD 100,000** and gone at **USD 150,000**; (2) **real estate professional status** (more than half of personal services in trades or businesses, and **more than 750 hours**, in real property businesses in which the taxpayer materially participates, one spouse alone meeting both) **plus material participation** in the rental; (3) a **short-term rental** with an **average stay of seven days or less** (or 30 days or less with significant personal services) is not a rental activity at all, so, for a section 469 trade or business activity, **material participation** (for example more than 100 hours and not less than anyone else) makes the loss non-passive without REPS. After other loss limits, aggregate eligible business deductions exceeding business income/gains plus **USD 256,000 (USD 512,000 joint)** are excess business losses for 2026; employee wages do not increase that business-income base.

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
| Allowance fully gone at modified AGI of (USD 75,000 married filing separately) | USD 150,000 (derived from phase-out) | [Instructions for Form 8582](https://www.irs.gov/instructions/i8582) |
| Married filing separately, lived apart all year: maximum (phase-out start USD 50,000) | USD 12,500 | [26 U.S.C. 469(i)(5)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Active participation: minimum ownership by value with the spouse, whole period | 10 percent | [26 U.S.C. 469(i)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Real estate professional, test (i): share of all personal services in real property businesses with material participation | more than one-half | [26 U.S.C. 469(c)(7)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Real estate professional, test (ii): hours in those businesses | 750 hours (more than) | [26 U.S.C. 469(c)(7)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Employee work counts as real property work only for an owner of more than | 5 percent | [26 U.S.C. 469(c)(7)(D)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Short-term rental exception (A): average period of customer use | seven days or less | [Treas. Reg. 1.469-1T(e)(3)(ii)(A)](https://www.ecfr.gov/current/title-26/section-1.469-1T) |
| Short-term rental exception (B): average period, with significant personal services | 30 days or less | [Treas. Reg. 1.469-1T(e)(3)(ii)(B)](https://www.ecfr.gov/current/title-26/section-1.469-1T) |
| Material participation test (a)(1) | more than 500 hours | [Treas. Reg. 1.469-5T(a)(1)](https://www.ecfr.gov/current/title-26/section-1.469-5T) |
| Material participation test (a)(3), and the floor for (a)(7) | more than 100 hours | [Treas. Reg. 1.469-5T(a)(3), (b)(2)(iii)](https://www.ecfr.gov/current/title-26/section-1.469-5T) |
| Residence test for a dwelling: personal-use days must exceed the greater of 14 days or 10 percent of fair-rental days | 14 days | [26 U.S.C. 280A(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280A.htm) |
| Excess business loss threshold, taxable years beginning in 2026 | USD 256,000 | [Rev. Proc. 2025-32, section 4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess business loss threshold, joint returns | USD 512,000 | [Rev. Proc. 2025-32, section 4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

### Steps

1. **Classify each property for the year.** Work out the average period of customer use under [Treas. Reg. 1.469-1(e)(3)(iii)](https://www.ecfr.gov/current/title-26/section-1.469-1) and test the exceptions in Treas. Reg. 1.469-1T(e)(3)(ii). Note the result (rental activity, or not a rental activity) and go to step 2 either way.
2. **Personal use of any dwelling** under section 280A(d)(1), whether or not it is a rental activity. If the owner used it as a residence, section 280A(c)(5) caps the deductions from the rental use at gross rental income less deductions allowable anyway and business/rental deductions allocable to the activity but not to that use, and for a passive activity section 469(j)(10) leaves the items from that use out of section 469: stop here for that unit. Otherwise a rental activity goes to step 3, and a property that is not a rental activity goes to step 5.
3. **Real estate professional status** under section 469(c)(7)(B) and [Treas. Reg. 1.469-9(c)](https://www.ecfr.gov/current/title-26/section-1.469-9), one spouse at a time. If no one qualifies, every rental real estate activity is passive: go to step 4. If someone qualifies, test material participation in each rental real estate interest, or in the single combined activity if the section 1.469-9(g) election is in force or being made. If rental losses remain passive, including carried losses, test the allowance in step 4 as well.
4. **Passive rental real estate:** test active participation and apply the allowance and phase-out under section 469(i). Run Form 8582 ([Instructions for Form 8582](https://www.irs.gov/instructions/i8582)). Carry any disallowed loss forward under section 469(b).
5. **Not a rental activity:** decide whether it is a trade or business activity and whether the owner materially participated under Treas. Reg. 1.469-5T(a). With material participation, report on the usual forms, not Form 8582; without it, a trade or business activity is passive and enters the Form 8582 computation. If trade-or-business activity classification itself is unresolved: **HOLD: Check this point with one of our partner accountants.**
6. **Apply the limits in order:** basis and at-risk first, then the passive loss limits, then the excess business loss limit on Form 461.
7. **On a sale,** check whether it is a fully taxable disposition of the entire interest in the activity to an unrelated party under section 469(g); if so, suspended losses from that activity are released.
8. **Keep the hours records and the election statement** with the return.

## Boundary and exception table

### Why a rental loss is passive by default

Section 469(a) denies an individual, estate or trust a "passive activity loss". A passive activity is a trade or business without material participation, and also any rental activity, except as section 469(c)(7) provides (section 469(c)(1) and (2)). So a rental is passive even if the owner works hard on it, unless the owner is a real estate professional and materially participates (the Form 8582 instructions say the same).

- The net passive loss generally cannot offset wages, nonpassive business profit or portfolio interest/gains; it can offset passive income from other activities, subject to separate-activity rules such as publicly traded partnerships (PTPs).
- It is "treated as a deduction or credit allocable to such activity in the next taxable year" (section 469(b)), year after year.
- It comes free on a disposition of the entire interest in a transaction in which all gain or loss is recognized: the loss, to the extent it exceeds net passive income from all other passive activities, is then not passive. Not if the buyer is related under section 267(b) or 707(b)(1) (section 469(g)(1)).
- If an activity stops being passive (the owner becomes a real estate professional), old suspended losses first offset income from that same activity; any remainder stays passive and can offset other passive income or qualify for the section 469(i) allowance (section 469(f)(1); Treas. Reg. 1.469-9(j)).
- Form 8582 is where the computation is made, unless the instructions' exception for small rental losses with active participation applies.

### Active participation allowance

| Rule | Detail |
| --- | --- |
| Who | A natural person who actively participated in the rental real estate activity in the current year and, for a carried loss, also in the year it arose (section 469(i)(1)). Lower bar than material participation: significant and bona fide management decisions or arranging services can qualify; examples include approving new tenants, rental terms or expenditures (Form 8582 instructions) |
| Ownership | With the spouse, at least 10 percent by value for the whole period; a limited partner interest does not count (section 469(i)(6)) |
| Phase-out | A reduction, not a cliff: each dollar of modified AGI above USD 100,000 removes 50 cents of allowance |
| Modified AGI | AGI without taxable social security, without sections 219, 221 and 250 deductions, exclusions under sections 85(c), 135 and 137, and any passive activity loss or loss allowed by reason of section 469(c)(7) (section 469(i)(3)(E)) |
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
| Employee work | Counts in the total of personal services; counts as real property work only during periods as a 5-percent owner within section 416(i)(1)(B), meaning more than 5 percent with its ownership-attribution rules (section 469(c)(7)(D)(ii); Treas. Reg. 1.469-9(c)(5)). Do not assume employment hours or qualification |
| Investor-type work | Studying financial statements, preparing summaries for own use, monitoring finances in a non-managerial capacity: excluded investor work unless directly involved in day-to-day management or operations (Treas. Reg. 1.469-9(b)(4); 1.469-5T(f)(2)(ii)) |
| Joint return | Met "if and only if either spouse separately satisfies such requirements"; spouses' hours are not added for the two tests, but the other spouse's work counts in deciding which real property businesses a spouse materially participates in (Treas. Reg. 1.469-9(c)(4)) |
| Material participation once qualified | Tested with both spouses' participation combined, whether or not they file jointly (Treas. Reg. 1.469-5T(f)(3)) |

### The election to treat all rentals as one activity

| Point | Rule (Treas. Reg. 1.469-9(e), (f), (g)) |
| --- | --- |
| Without it | Each interest is separate and material participation must be shown in each. The election combines rental real estate interests, not unrelated development or construction work; PTPs remain separate |
| How | A statement with the original return for the year declaring the taxpayer is a qualifying taxpayer and is making the election under section 469(c)(7)(A) (paragraph (g)(3)) |
| When | Any year the taxpayer qualifies; not electing one year does not stop a later election |
| How long | Binding for that year and every later year the taxpayer qualifies, even after gaps; revocable only in a year of a material change in facts and circumstances (or later while it lasts), with a statement on the original return; being less advantageous is not a material change |
| Missed it | [Rev. Proc. 2011-34 §§4–5](https://www.irs.gov/pub/irs-drop/rp-11-34.pdf): the only failure must be timing, all affected returns for the effective year and later years must be consistent with aggregation (no inconsistent returns), each affected return must be filed within 6 months after its due date excluding extensions, and reasonable cause must exist. Attach the election statement to an amended return for the most recent year and mail to the IRS service center where the current return will be filed. State the intended effective year, reason for failure, qualifying-taxpayer/election declaration and all eligibility representations; put "FILED PURSUANT TO REV. PROC. 2011-34" at the top. Add the dated penalties-of-perjury declaration signed by the taxpayer(s) with personal knowledge, exactly as §4.02 requires. IRS notification is not a determination of eligibility, REPS or material participation. No unsigned AI declaration is usable |
| Limited partnership interests | If the combined activity includes any, the whole activity is a limited partnership interest for material participation (only Treas. Reg. 1.469-5T(e)(2) tests), unless the taxpayer's share of gross rental income from all limited partnership rental interests is less than ten percent of the taxpayer's share from all rental real estate interests (paragraph (f)) |
| Selling one property | Suspended losses are released only on a disposition of the entire interest in an activity (section 469(g)); the Form 8582 instructions let a disposition of substantially all of an activity be treated separately if the losses and income allocable to the part sold are proved with reasonable certainty. Decide before electing |

### Material participation: the seven tests (Treas. Reg. 1.469-5T(a), "if and only if" one is met)

| Test | Wording |
| --- | --- |
| (a)(1) | "participates in the activity for more than 500 hours during such year" |
| (a)(2) | participation "constitutes substantially all of the participation in such activity of all individuals (including individuals who are not owners of interests in the activity)" |
| (a)(3) | "participates in the activity for more than 100 hours during the taxable year, and such individual's participation in the activity for the taxable year is not less than the participation in the activity of any other individual (including individuals who are not owners of interests in the activity)" |
| (a)(4) | a significant participation activity (a trade or business with more than 100 hours, not materially participated in under another test) where aggregate participation in all such activities "exceeds 500 hours" |
| (a)(5) | "materially participated in the activity (determined without regard to this paragraph (a)(5)) for any five taxable years (whether or not consecutive) during the ten taxable years that immediately precede the taxable year" |
| (a)(6) | a personal service activity (specified professional fields or another business where capital is not a material income-producing factor), with material participation "for any three taxable years (whether or not consecutive) preceding the taxable year" |
| (a)(7) | "on a regular, continuous, and substantial basis during such year", on all facts and circumstances |

Limits that decide real cases: (a)(7) is closed to anyone with 100 hours or less (paragraph (b)(2)(iii)), and management time does not count for it if someone else is paid to manage or another individual spends more hours on management (paragraph (b)(2)(ii)); (a)(4) works only for trade or business activities, and a rental activity is not one (paragraph (c); Form 8582 instructions); (a)(2) and (a)(3) compare the owner with every other individual, so a manager, cleaner or contractor with more hours defeats (a)(3); work not customarily done by owners does not count if a principal purpose is to avoid the passive rules (paragraph (f)(2)(i)); investor-type work does not count unless directly involved in day-to-day management or operations (paragraph (f)(2)(ii)); a spouse's participation counts as the taxpayer's (paragraph (f)(3)); for a limited partnership interest within paragraph (e)(3), only (a)(1), (a)(5) or (a)(6) are available, subject to the general-partner exception in (e)(3)(ii). Do not classify an LLC member solely from the LLC label; Check this point with one of our partner accountants.

### The short-term rental rule

An activity involving the use of tangible property is not a rental activity for a year if (Treas. Reg. 1.469-1T(e)(3)(ii)): (A) "The average period of customer use for such property is seven days or less"; (B) "The average period of customer use for such property is 30 days or less, and significant personal services ... are provided by or on behalf of the owner of the property"; or (C) extraordinary personal services are provided, "without regard to the average period of customer use". For exceptions (C) to (F), including extraordinary services, incidental rentals, defined business hours and property supplied to an owned partnership or S corporation: **HOLD: no classification under these exceptions is usable from this Guide. Check this point with one of our partner accountants.**

- **Effect.** It is not a rental activity, so section 469(c)(2) does not make it passive. If it is a trade or business and the owner materially participated, the income or loss goes "on the forms or schedules normally used" and stays off Form 8582. Real estate professional status is not needed. Without material participation, a non-rental trade or business activity is passive, and the section 469(i) allowance does not help, because that allowance is for rental real estate activities.
- **Average period.** For one class of property, total days in all periods of customer use that end in the year (or include its last day), divided by the number of those periods; each continuous or recurring right to use counts as one period, even across renewals. With classes at significantly different daily rents, weight each class's average by its share of gross rental income (amounts paid for property use) (Treas. Reg. 1.469-1(e)(3)(iii)).
- **Significant personal services (B).** Only services by individuals; look at frequency, labour and value compared with the rent. Not counted: services needed for lawful use, construction of improvements and repairs extending useful life substantially beyond the average customer-use period, and services common with long-term rentals of high-grade property such as cleaning common areas, routine repairs, trash collection and security (Treas. Reg. 1.469-1T(e)(3)(iv)).

### Personal use and section 280A

- A dwelling is used as a residence if personal-use days exceed the greater of 14 days or 10 percent of days rented at a fair rental (section 280A(d)(1)). A day is personal use if, for any part of it, the unit is used by the owner, anyone else with an interest, a family member (section 267(c)(4)) of either, anyone under an arrangement letting the owner use another dwelling, or any individual not paying a fair rental (except an employee whose use falls under section 119) (section 280A(d)(2)). A personal day is not a fair-rental day for the 10 percent count. Apply section 280A(d)(3)'s fair-rent principal-residence exception (an interested occupant also needs a shared-equity financing agreement), section 280A(d)(2)'s substantially full-time repair/maintenance rule, and section 280A(d)(4)'s qualified rental-period rule when relevant. **HOLD: do not classify those special-use days without resolving the exception. Check this point with one of our partner accountants.**
- If so and section 280A(c)(5) applies, the items from that use are not taken into account for section 469 (section 469(j)(10)); section 280A(c)(5) caps rental deductions at gross rental income after deductions allowable anyway and business/rental deductions allocable to the activity but not to that use and carries the excess forward. This cap does not disallow deductions otherwise allowable without rental use; it prevents a rental-use loss against other income. Even below the residence threshold, allocate rental-use expenses under section 280A(e) when there are personal-use days.
- A residence rented for less than 15 days in the year: no rental deductions, rent not in income (section 280A(g); see `us-augusta-rule-home-rental-to-your-business`).

### Pairing with cost segregation and bonus depreciation

Depreciation does not bypass the passive-loss limits: a rental loss may be usable through the active-participation allowance, qualifying REPS plus material participation, or a non-rental trade or business with material participation. Otherwise apply section 469, including passive-income offsets and carryforwards. This Guide does not establish any asset's depreciation entitlement. Methods live in `us-federal-cost-segregation` and `us-section-179-and-bonus-depreciation`.

### The excess business loss limit

A loss that clears the passive rules can still be limited: after at-risk and passive limits, a non-corporate taxpayer's business losses "may be subject to the excess business loss limitation", figured on Form 461 (Form 8582 instructions). The Form 461 instructions treat an activity as a trade or business if the "primary purpose for engaging in the activity is for income or profit and you're involved in the activity with continuity and regularity" ([Instructions for Form 461](https://www.irs.gov/instructions/i461)); REPS or short customer use alone does not settle this separate determination. Compute excess over aggregate business income/gains plus the applicable threshold, excluding employee wages and the other items section 461(l)(3) specifies; the threshold is not a limit per property. The disallowed excess becomes a net operating loss carryover ([26 U.S.C. 461(l)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm)). Section 70601 of Public Law 119-21 struck "and before January 1, 2029" from section 461(l)(1) for taxable years beginning after 31 December 2026, so the limit no longer expires, and rebased its indexing to 2024 for years beginning after 31 December 2025 ([Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)).

### Records an examiner asks for

Participation may be shown "by any reasonable means"; contemporaneous daily logs are not required if participation can be shown by "appointment books, calendars, or narrative summaries" identifying the services and approximate hours (Treas. Reg. 1.469-5T(f)(4)). Prepare: a dated log of hours per property (or combined activity), per spouse, with the task, built during the year from calendars, emails, booking messages and invoices; for status, total hours in all trades or businesses including employment, with payroll or timesheets; hours of everyone else who worked on the property; for short-term rentals, the booking history and a record of personal-use days; the section 1.469-9(g) election statement and the year first made; ownership documents showing limited partnership interests and percentages; Form 8582 carryforward workpapers by activity.

### Defaults when a fact is missing

Do not invent hours, other workers' hours, an election or a passive-loss conclusion. Seek reasonable evidence under Treas. Reg. 1.469-5T(f)(4), including calendars or narrative summaries; a daily log is not compulsory. Until hours, booking history, personal-use allocation or election history are resolved, **HOLD: no deduction or classification dependent on that fact is usable. Check this point with one of our partner accountants.** Keep all original inputs on the workpaper.

### Red flags to raise

| Flag | Why it matters |
| --- | --- |
| Full-time W-2 employee claiming status | Compare actual qualifying real-property hours against all other personal-service hours |
| Short-term rental with a property manager doing most of the work | (a)(3) may fail; evaluate every applicable alternative test |
| Large first-year cost segregation loss | Check allowance, passive income, REPS/participation, depreciation entitlement and other loss limits |
| Sale of one property after the aggregation election | Suspended losses may not be released |
| Personal days exceed the greater of 14 or 10 percent of fair-rental days, after exceptions | Section 280A(c)(5) caps the loss |

## Worked cases

**Case 1, the allowance in the phase-out.** A married couple files jointly; neither is a real estate professional; they actively participate in one long-term rental. Modified AGI is USD 130,000 and the rental loss is USD 18,000. Assume their ownership is at least 10 percent throughout, the loss survives basis/at-risk limits, there is no other passive income/loss or credit using the allowance, and no special-activity rule applies. The excess over USD 100,000 is USD 30,000; half is USD 15,000; the allowance is USD 25,000 minus USD 15,000 = USD 10,000. They deduct USD 10,000 against other income and carry USD 8,000 forward as a suspended passive loss. At modified AGI of USD 400,000 the allowance is gone and the whole loss is suspended unless they have passive income or a qualifying disposition.

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

**Case 2, a decision: is the cabin loss passive?** An employee with high wages buys a cabin. In 2026 it has 40 guest stays totalling 160 nights, all ending in the year: an average of 4 days, seven or less, so it is not a rental activity. The owner logs 120 hours on listing, guest messages, restocking and turnovers; the cleaning contractor logs 90; no one else more. The owner is above 100 hours and not below anyone, so test (a)(3) is met. Assuming a section 469 trade or business activity with qualifying owner work and no special entity restriction, a first-year loss of USD 70,000 (largely depreciation after a cost segregation study) is not passive: it can offset wages, subject to basis, at-risk and the excess business loss limit. Personal use: 10 days, against the greater of 14 days and 10% of 160 rental days (16 days), so 16; 10 does not exceed 16, so the cabin is not a residence. The USD 70,000 is the original stated loss, not a proved deductible amount: with 10 personal-use days, the expense allocation under section 280A(e) must be checked before using it. **HOLD: do not claim a USD 70,000 wage offset from these inputs alone. Check this point with one of our partner accountants.** The trap: if the contractor logs 150 hours instead, the owner's 120 hours are less than another individual's, (a)(3) fails, (a)(1) fails (under 500), and (a)(7) rests on facts and circumstances with no hours figure above 100 in the regulation (the owner's management hours do count, since no one else is paid to manage or does more management). Failure of (a)(1) and (a)(3) does not by itself settle the other applicable tests, including significant-participation aggregation and prior participation. **HOLD: the USD 70,000 outcome in this variation is not usable until all applicable tests and loss limits are resolved. Check this point with one of our partner accountants.**

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
  - not_rental_activity: max(1 - ceil(max(average_stay - 7, 0)), 0)
  - meets_a3: min(ceil(max(owner_hours - 100, 0)), 1) * max(1 - ceil(max(cleaner_hours - owner_hours, 0)), 0)
  - meets_a3_trap: min(ceil(max(owner_hours - 100, 0)), 1) * max(1 - ceil(max(cleaner_hours_trap - owner_hours, 0)), 0)
  - residence_limit: max(14, 0.10 * nights)
  - used_as_residence: min(ceil(max(personal_days - residence_limit, 0)), 1)
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
| R-RE-EMPLOYEE | A real estate professional position for an employee | Use actual evidence; the half test needs qualifying real-property hours exceeding all other personal-service hours; the separate more-than-750-hour test also applies |
| R-RE-LOG | Unsupported reconstructed hours, or noncustomary owner work done principally to avoid the passive rules | Hold unsupported figures; reasonable reconstruction is permitted under (f)(4), but excluded work fails (f)(2)(i) |
| R-RE-ELECT | A late election outside Rev. Proc. 2011-34, a revocation, or a grouping question under Treas. Reg. 1.469-4 | HOLD: Check this point with one of our partner accountants. |
| R-RE-TIER | Interests held through tiered partnerships or S corporations | HOLD: Check this point with one of our partner accountants. |
| R-RE-OTHEREXC | Rental exceptions (C) to (F) | HOLD: Check this point with one of our partner accountants. |
| R-RE-SALE | A related-party sale or a 1031 exchange | HOLD: Check this point with one of our partner accountants. See `us-section-1031-like-kind-exchange`. |
| R-RE-STATE | State treatment | HOLD: Check this point with one of our partner accountants. |

## Filing and payment

Use the [Form 8582 instructions](https://www.irs.gov/instructions/i8582) to determine filing, including prior suspended losses; a passive loss is not the only filing trigger. The small-loss exception requires active-participation rental real estate to be the only passive activity, no prior unallowed passive losses or current/prior unallowed passive credits, total rental loss no more than USD 25,000 (USD 12,500 for married separate), modified AGI no more than USD 100,000 (USD 50,000 for married separate), separate filers apart all year, and no rental interest as a limited partner or estate/trust beneficiary. Non-rental activities use their usual schedule; short stays alone do not select Schedule C or settle self-employment tax. Attach Form 461 when its applicable-year filing instructions require it.

For a calendar-year individual subject to the ordinary deadline, the 2026 Form 1040 is due **15 April 2027** ([section 6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm)). A valid Form 4868 application made by the prescribed due date gives a six-month filing extension to **15 October 2027**; show estimated total tax and follow the filing instructions. It does not extend payment ([Treas. Reg. 1.6081-4](https://www.ecfr.gov/current/title-26/section-1.6081-4)). Disaster, overseas and other special deadlines: **HOLD: Check this point with one of our partner accountants.** Attach a timely section 1.469-9(g) election statement to the original return, including a valid extension; see the separate late-relief procedure above.

**2026 forms HOLD:** the linked Form 8582 and 461 instructions are 2025 editions, used here for unchanged principles only. Do not use their 2025 thresholds or box numbers for 2026. Before filing, obtain the final 2026 forms/instructions and resolve year-specific mechanics. Check this point with one of our partner accountants.

## Completion checklist

- Each property classified (rental activity or not) from the booking history.
- Personal-use days tested under section 280A(d)(1).
- Real estate professional tests run for one spouse at a time, with all employment hours in the total.
- Material participation tested per property or per combined activity, against every other individual's hours.
- Allowance phase-out applied on the right modified AGI.
- Limits applied in order: basis, at-risk, passive, excess business loss.
- Hours log, election statement and carryforward workpapers in the file.

> **Circular 230 §10.37:** apply these rules to the taxpayer's actual facts and reasonable assumptions; resolve missing information before using a deduction. This general reference is not a filing opinion.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 469 (govinfo). Read for (a), (b), (c)(1), (2) and (7), (f)(1), (g), (h), (i) USD 25,000, USD 100,000, 50 percent, USD 12,500, 10 percent, and (j)(10). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm | 2026-11-27 |
| 26 U.S.C. 280A (govinfo). Read for (c)(5), (d)(1)–(4), (e) and (g). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280A.htm | 2026-11-27 |
| 26 U.S.C. 461 (govinfo). Read (l)(2)–(3) for carryover and computation; archived sunset/indexing text is superseded by the law and revenue procedure below. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm | 2026-11-27 |
| Treas. Reg. 1.469-1 (eCFR). Read for (e)(3)(iii), average period of customer use. | https://www.ecfr.gov/current/title-26/section-1.469-1 | 2026-11-27 |
| Treas. Reg. 1.469-1T (eCFR). Read for (e)(3)(ii) exceptions (seven days or less, 30 days or less) and (e)(3)(iv). | https://www.ecfr.gov/current/title-26/section-1.469-1T | 2026-11-27 |
| Treas. Reg. 1.469-5T (eCFR). Read for (a) the seven tests, (b)(2), (c), (e)(2) and (f). | https://www.ecfr.gov/current/title-26/section-1.469-5T | 2026-11-27 |
| Treas. Reg. 1.469-9 (eCFR). Read for (b)(4), (c), (e), (f), (g), (h) and (j). | https://www.ecfr.gov/current/title-26/section-1.469-9 | 2026-11-27 |
| Instructions for Form 8582 (2025). Read for the small-loss exception, non-rental activities, order of limits and partial dispositions. | https://www.irs.gov/instructions/i8582 | 2026-11-27 |
| Instructions for Form 461 (2025). Read for the trade or business test. | https://www.irs.gov/instructions/i461 | 2026-11-27 |
| Rev. Proc. 2011-34. Read for late election relief. | https://www.irs.gov/pub/irs-drop/rp-11-34.pdf | 2026-11-27 |
| Rev. Proc. 2025-32. Read for section 4.31, USD 256,000 (USD 512,000 joint). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| Public Law 119-21, section 70601. Read for the permanent excess business loss limit and its effective dates. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-27 |
| 26 U.S.C. 416(i)(1)(B), owner definition and attribution. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartB-sec416.htm | 2026-11-27 |
| 26 U.S.C. 6072(a), ordinary individual deadline. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-27 |
| Treas. Reg. 1.6081-4, filing extension application and payment distinction. | https://www.ecfr.gov/current/title-26/section-1.6081-4 | 2026-11-27 |

Not yet confirmed: final 2026 Form 8582/461 filing mechanics, individual evidence-dependent outcomes, special personal-use days, LLC/limited-partner classification, special deadlines and referral cases are explicit non-usable HOLDs above. Check this point with one of our partner accountants.
