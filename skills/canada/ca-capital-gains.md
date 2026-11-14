---
name: ca-capital-gains
description: "Canadian resident individuals: calculate capital gains and losses, reconstruct adjusted cost base, test principal residence and flipping rules, calculate eligible LCGE deductions and reserves, and prepare Schedule 3. Ordinary inclusion is one-half under enacted law. For non-residents use ca-nonresident-cgt."
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
depends_on:
  - income-tax-workflow-base
---

# Canada: capital gains for individuals (inclusion rate, ACB, principal residence, lifetime exemption, losses, Schedule 3)

## Scope

This skill covers **federal** income tax on capital gains and capital losses of an **individual resident in Canada** who sells, or is considered to have sold, capital property: shares and fund units, real estate, a home or cottage, personal-use property and qualifying small business or farm and fishing property.

Primary year: **tax year 2026** (calendar year, 1 January to 31 December 2026). A short section near the end covers the **2025** returns that were due in 2026. Where a rule is unchanged between 2025 and 2026 the skill says so.

It covers:

- the inclusion rate (the share of a gain that is taxed) and the enacted rule and the historical proposed increase;
- proceeds, adjusted cost base (ACB), outlays and expenses, and average cost for identical shares;
- the principal residence exemption, the designation, the "plus 1" year and reporting on Form T2091(IND);
- the residential property flipping rule (homes held for less than 365 days);
- the lifetime capital gains exemption (LCGE) for qualified small business corporation shares and qualified farm or fishing property, claimed as the capital gains deduction;
- capital losses, net capital losses, superficial losses, personal-use and listed personal property;
- the capital gains reserve;
- reporting on Schedule 3, line 12700, line 25300 and line 25400, and the filing dates.

**Not covered here:** non-residents selling Canadian property (see the **ca-nonresident-cgt** skill), departure tax on leaving Canada and residency questions (see **ca-tax-residency**), corporations and trusts, provincial and territorial tax rates, Quebec's separate provincial return, and whether a sale is business income rather than a capital gain outside the flipping rule. Provincial and territorial tax also applies to the same taxable capital gain, but the rates are outside this skill.

Law: the *Income Tax Act* (ITA), mainly [s.38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) (taxable capital gain), [s.40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) (gains, losses, reserve, principal residence formula), [s.54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) (definitions), [s.110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html) (capital gains deduction) and [s.111](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html) (loss carryovers). The Justice Laws consolidation read on 14 November 2026 is current to 19 October 2026. The ordinary inclusion rule comes from the enacted Act; historical announcements are not an alternative rate. [G01][G02][G03][G04][G05]

## Ask the client first

- **Were you resident in Canada for the whole year of sale?** The LCGE needs residence throughout the claim year, including the statutory deeming rule for residence during part of that year and throughout the preceding or following year (ITA110.6(5)). A non-resident needs a different Guide.
- **What did you sell, when, and for how much?** Get the T5008 slip or broker statement, the sale contract, and the closing statement for real estate.
- **What did it cost you, including purchase costs and improvements?** For shares or fund units bought over time, get every purchase, reinvested distribution and T3 box 42 amount so the average cost can be rebuilt.
- **What did the sale cost you?** Commissions, legal fees, real estate commission.
- **Was any amount in a foreign currency?** Get the dates of purchase, sale and each expense.
- **For a home or cottage:** when bought, who lived in it in each year, whether any part was rented or used for business, whether capital cost allowance was ever claimed, and which other homes the family unit owned in the same years.
- **Did you own the home for less than 365 consecutive days?** If yes, ask why you sold (death, illness, separation, a job move, and the other listed life events).
- **For private company shares or a farm or fishing property:** who owned the shares in the last 24 months, what the company's assets were over that time, how much LCGE was used before, and any past business investment losses. Get the investment income and carrying charges for Form T936.
- **Did you, your spouse or common-law partner, or a company you control, buy the same property back within 30 days before or after a loss sale?**
- **Were you paid in full at closing, or over several years?**
- **Do you have unused net capital losses from earlier years** (see the last notice of assessment)?
- **Are you or your spouse or common-law partner self-employed?** That changes the filing date, not the payment date.

## The method, step by step

1. **Confirm it is a capital disposition.** A sale, a gift, or a deemed sale all count. Check the flipping rule first for any Canadian housing unit held for less than 365 days; if it applies, the gain is business income and this skill stops for that property.
2. **Find the year.** Report the disposition in the calendar year you sold or were considered to have sold the property, even if your business has a different fiscal year end.
3. **Work out proceeds, ACB and outlays in Canadian dollars.** Capital gain or loss = proceeds − (ACB + outlays and expenses).
4. **Apply special rules to the gain or loss:** principal residence exemption, personal-use property floor, listed personal property, superficial loss, and the reserve if you are paid over time.
5. **Apply the correct inclusion rule.** Ordinary 2026 and 2025 capital gains and allowable capital losses use one-half under ITA38. Test specified charitable-gift exceptions separately. Do not halve an already-taxable slip amount or the special partnership amount shown at line19890 on the actual2025 Schedule3. [G01][G26][G45][G47]
6. **Net the year.** Allowable capital losses of the year offset taxable capital gains of the year. A positive balance goes on **line 12700**. A negative balance becomes part of the net capital loss: keep it for later years or carry it back on Form T1A.
7. **Apply losses from other years** on **line 25300**, generally against taxable capital gains, oldest loss first and adjusted for historical inclusion rates. Check the pre-1986 and death-year exceptions separately; an ABIL is a different loss category. [G05][G21][G22]
8. **Claim the capital gains deduction** on **line 25400** for eligible QSBC shares or qualified farm or fishing property, using Form T657 (and Form T936 for the cumulative net investment loss, CNIL).
9. **Report** on Schedule 3 (and Form T2091(IND) for a home), file by the deadline and pay any balance by 30 April of the next year.

## Key figures, with the year each applies to

| Item | Tax year 2026 | Tax year 2025 | Source |
| --- | --- | --- | --- |
| Inclusion rate (individuals) | one-half of the gain (ITA s.38(a), current enacted ordinary rule) | 50% ("The inclusion rate for 2025 is 50%") | [ITA s.38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html); [CRA capital losses](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| LCGE (QSBC shares, qualified farm or fishing property) | $1,275,000 of gains | $1,250,000 of gains | [CRA indexation table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| Capital gains deduction limit (derived: one-half of the LCGE, line 25400), before personal eligibility/history limits | $637,500 | $625,000 | [ITA110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html), [117.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.1.html), [CRA indexation table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| Personal-use property: minimum ACB and minimum proceeds | $1,000 | $1,000 | [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html) |
| Flipping rule holding period | less than 365 consecutive days | same | [ITA s.12(13)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html) |
| Superficial loss window | 30 days before to 30 days after the sale | same | [ITA s.54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) |
| Net capital loss carryback / carryforward | 3 years back, no limit forward | same | [CRA capital losses](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Listed personal property loss | 3 years back, 7 years forward, LPP gains only | same | [ITA41](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-41.html); [CRA capital losses](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Reserve (proceeds paid over time) | gain spread over up to 5 years; up to 10 years for certain transfers to a child | same | [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA s.40(1.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Late principal residence designation penalty | lesser of $8,000 and $100 per complete month late | same | [ITA s.220(3.5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html) |

### The inclusion rate: current law and historical proposals

- **Ordinary capital gains and allowable capital losses use one-half** under enacted ITA38(a),(b). There is no enacted general two-thirds rate above $250,000 for the individual dispositions covered here. The January2025 announcement concerned a proposed change; it does not override the current Act. [G01][G34]
- The previously cited corporate What's New page no longer contains the quoted cancellation sentence. Do not use that missing quotation to establish the law. Read ITA38. A historical split date may still matter for the **LCGE**, not an ordinary 2024 capital-gain inclusion-rate split. [G01][G04][G29]
- Specified gifts can have a zero-inclusion portion under38(a.1),(a.2), with advantage adjustments under38.2. Flow-through-share and partnership-exchange rules can produce additional amounts. Use the actual gift calculation, not a universal exemption. [G01][G45][G47]
- Older net capital losses were incurred at other rates: 1988–1989 two-thirds;1990–1999 three-quarters;2000 the taxpayer's actual Schedule3 inclusion rate;2001–2025 one-half. Preserve the originating-year allowable-loss balance and adjust to the claim-year rate under111(1.1). A historical three-quarter allowable loss of7,500 corresponds to5,000 at one-half, not7,500. [G05][G21][G22]

## Proceeds, ACB and outlays ([T4037, Chapter 1 and Chapter 3](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html))

- **Proceeds of disposition** are usually the sale price; they can also be compensation for property destroyed, expropriated or stolen.
- **Adjusted cost base (ACB)** is usually the cost of the property plus expenses to acquire it (commissions, legal fees) and capital expenditures such as additions and improvements. Current expenses such as maintenance and repairs are **not** added.
- **Outlays and expenses** are the costs of selling: fixing-up expenses, finders' fees, commissions, brokers' fees, surveyors' fees, legal fees, transfer taxes and advertising. They reduce the gain only; they cannot be deducted from other income.
- **Capital gain = proceeds − ACB − outlays and expenses.** A negative result is a capital loss.
- **Identical properties** (shares of the same class of one company, units of one mutual fund trust): use the **average cost**. Recalculate after a purchase using the remaining pool ACB immediately before it plus the new acquisition cost, divided by the total units now held; do not restore costs of previously sold units. A sale does not change the average cost of the units left.
- **Mutual fund trust units:** T3 box 42 changes the ACB. The magnitude of a negative box42 amount is added to ACB; a positive amount is subtracted. If the ACB would go below zero, the excess is a deemed capital gain at that time and the ACB is reset to zero. A negative box42 amount increases ACB by its absolute amount, not by subtracting a negative number twice. [G02(3)][G08(1)(a),(2)(h)][G19]
- **Stock splits and consolidations** do not change the total ACB; they change the ACB per share.
- **Foreign currency:** convert proceeds at the exchange rate at the time of sale, the ACB at the rate when the property was acquired, and each expense at the rate when it was incurred.
- **Gifted property:** you are generally considered to have acquired it at its fair market value (FMV) on the date you received it. **Inherited property:** your cost is generally the deceased person's deemed proceeds, usually the FMV right before death; property from a deceased spouse or common-law partner, and farm property or a woodlot passing to a child, may be treated differently.
- **Records:** keep purchase and sale records, and a record of the FMV on the date you inherit property, receive it as a gift, or change its use.
- **Slips:** brokers issue a T5008 slip or an account statement for securities sold. Rebuild the ACB from the client's own purchase records rather than relying on a slip alone.

## Principal residence exemption ([Folio S1-F3-C2](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html))

**What can qualify.** A house, cottage, condominium, apartment, duplex unit, trailer, mobile home or houseboat, a leasehold interest in one, or a co-operative housing share bought only to get the right to live in a unit. It qualifies for a year only if **all** of these hold:

- you own it, alone or jointly;
- you, your current or former spouse or common-law partner, or one of your children **ordinarily inhabited** it at some time in the year;
- you **designate** it as your principal residence for that year.

**Land.** The land under and around the home can be included, usually up to **half a hectare**. More land counts only if you can show it is needed for the use and enjoyment of the home (for example, a municipal minimum lot size).

**One home per family unit per year (1982 and later).** For 1993 and later years the family unit is: you; a person who was your spouse or common-law partner throughout the year (unless you were separated all year under a court order or written agreement); and your children, other than a child who had a spouse or common-law partner during the year or was 18 or older during the year. If you had no spouse or partner and were under 18 all year, your parents and unmarried siblings under 18 are also in the unit. So a couple with a house and a cottage can shelter only one of them for any given year.

**The exemption formula (ITA40(2)(b)).** Remaining capital gain = **A − (A × B ÷ C) − D**, with a negative algebraic result treated as zero under257. A is the otherwise determined gain; B is the count of eligible designated years ending after acquisition during which the taxpayer was resident in Canada, plus one only if resident during the acquisition year; C is all tax years ending after acquisition during which the property was owned. D is the statutory adjustment for certain pre-23February1994 acquisitions with a1994 capital-gains election, otherwise zero. Only when D=0 can the ordinary exemption be described simply as gain×B/C. Do not omit D from an old-property case or create a capital loss from an overlarge fraction. [G02(2)(b)][G39]

- The **"plus 1"** lets you treat both the old and the new home as sheltered in the year you sell one and buy the other, even though only one can be designated for that year.
- The "plus 1" is **only available if you were resident in Canada in the year you acquired the home.** If you were non-resident throughout that year, you do not get the extra year.
- The exemption is also limited to years you were **resident in Canada**. If the client was non-resident for any part of the ownership, refer or see the ca-nonresident-cgt skill.

**You must report the sale.** For 2016 and later years, CRA only allows the principal residence exemption if you **report the disposition and the designation** on your return.

- Report on **Schedule 3** (actual2025 edition: **Part2**, line17900 designation box) and **Form T2091(IND)**, *Designation of a Property as a Principal Residence by an Individual (Other Than a Personal Trust)*.
- On the actual **2025 T2091(IND)**, Schedule3 line17900 **box1** leads to **Section1 on page2**, not page1. Boxes2or3 also require Section2 beginning on page3, completed for the applicable situation. A1994 election can require T2091(IND)-WS. The box choice never waives residence, capital-character or family-year requirements. [G26][G30]
- Sold more than one former home in the same year: a separate T2091(IND) for each.
- **Forgot to designate?** Ask CRA to amend the return. CRA can accept a late designation, but a principal residence designation is treated as an election (ITA s.220(3.21)(a.1)), and the late-election penalty is the **lesser of $8,000 and $100 for each complete month** from the original due date to the date the request is made (ITA s.220(3.5)).

**A loss on a home is not deductible.** A home is personal-use property, so a loss on its sale cannot be claimed.

**Partly used to earn income.** If only part of the home qualifies, split the selling price and ACB between the home part and the income part on a reasonable basis (square metres or number of rooms), and report the gain on the income part. The whole property keeps its principal residence status if the income use is ancillary to the home use, there is no structural change, and no capital cost allowance is claimed (for example, a home day care).

**Change of use.** Converting a home to income-producing use normally creates an FMV deemed disposition/reacquisition under45(1). A45(2) election is a signed letter filed with the return for the change year; it defers that change, but rental income remains reportable and CCA must not be claimed while the election operates. Up to four non-occupied tax years can qualify for designation, subject to Canadian-residence and family-year limits. A45(3) election for rental-to-home use is due by the earlier of90days after a Ministerial demand and the filing deadline for the year of the actual disposition. It can allow up to four earlier designated years, subject to the same restrictions. Under45(4), CCA allowed for a tax year ending after1984 and on or before the change to the taxpayer, their spouse/common-law partner or a relevant trust defeats45(3). Partial changes from19March2019 can also qualify for these elections; do not assume only a complete conversion is covered. [G14][G20¶2.48–2.60.2]

**Employer relocation and ancillary use.** Lifting the45(2) four-year limit under54.1 requires employment relocation, an unrelated employer, the old home at least40km farther from the new work than the subsequent residence, and return to ordinary habitation while employed by the same employer or by the end of the year after that employment ends, or death during that employment. It is not a general extension for every job move or every45(3) election. CRA's ancillary-use treatment requires all three conditions already listed above; structural conversion or CCA can change the result. Refer with the FMV, rental/CCA history, election letters and exact occupancy dates. [G15][G20¶2.48–2.64]

## Flipped homes: the 365-day rule ([ITA s.12(12)–(14)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html))

- A **housing unit in Canada** (including a rental property), or a right to acquire one, that you owned or held for **less than 365 consecutive days** before selling it is a **flipped property**. The gain is **business income**, not a capital gain. It is fully taxed, the principal residence exemption does not apply, and a business loss on a flipped property is **deemed nil**.
- The rule applies to residential properties sold on or after 1 January 2023 (Folio S1-F3-C2, ¶2.6.1). It does not apply to property that is already inventory (that is business income anyway).
- **Exception: life events.** The rule does not apply if the sale can reasonably be considered to occur because of, or in anticipation of:
  - the death of the taxpayer or a related person;
  - a related person joining the household, or the taxpayer joining a related person's household (marriage or partnership, birth, adoption, care of an elderly parent);
  - breakdown of a marriage or common-law partnership, where the couple had lived separate and apart for **at least 90 days** before the sale;
  - a threat to the personal safety of the taxpayer or a related person;
  - a serious disability or illness of the taxpayer or a related person;
  - an eligible relocation of the taxpayer or spouse/common-law partner: the new home is **at least40km** closer to the new business/employment or full-time post-secondary education location, with the rest of the248(1) definition tested;12(13)(b)(vi) removes its requirements for the new work location and new residence to be in Canada;
  - involuntary termination of employment of the taxpayer or spouse or common-law partner;
  - insolvency of the taxpayer;
  - destruction or expropriation of the property.
- If the home is **not** a flipped property, it can still be business income on general principles (for example, a pattern of buying to resell). If treated as business income, report on Form T2125; if a capital gain, on Schedule 3. That judgment is outside this skill: refer when facts point to trading.

## Lifetime capital gains exemption and the capital gains deduction ([CRA line 25400](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25400-capital-gains-deduction.html); [ITA s.110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html))

The LCGE is a limit on **gains**; the deduction on line 25400 is the matching limit on **taxable** gains (half, because only half of a gain is taxable).

| Year | LCGE (gains) | Deduction limit (line 25400) | Source |
| --- | --- | --- | --- |
| 2026 | $1,275,000 | $637,500 | [CRA indexation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| 2025 | $1,250,000 | $625,000 | [CRA indexation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |

- **2026 is the first indexed year after2025.** ITA117.1(2)(c) expressly indexes the625,000 amount in110.6(2)(a) for tax years after2025, using117.1(1),(3). The2026 published result is637,500 of deduction and1,275,000 of eligible gains. The625,000 base in110.6 is not an unindexed2026 ceiling. [G04][G06][G18]
- The same limit covers **qualified small business corporation (QSBC) shares** and **qualified farm or fishing property (QFFP)**. It is one **cumulative lifetime** limit shared across both: deductions already claimed in earlier years reduce what is left.

**Who can claim.** An individual (not a trust) who:

- was **resident in Canada throughout the year** of the claim (CRA also treats you as resident throughout the year if you were resident for part of it and throughout the year before or the year after; factual and deemed residents count);
- has gains that qualify; and
- has deduction room left.

**What gains qualify.** Taxable capital gains from dispositions of QSBC shares or QFFP; a reserve brought into income from such a disposition; and such gains allocated and designated to you by a trust.

**QSBC share: all three tests** ([T4037, Definitions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)):

1. **At the time of sale** it is a share of a **small business corporation** (ITA248(1); CRA generally describes all or substantially all as90%or more, but this is not a statutory percentage safe harbour): a Canadian-controlled private corporation (CCPC) where **all or substantially all** of the fair market value of the assets are used mainly in an active business carried on primarily in Canada (by it or a related corporation), or are shares or debts of connected small business corporations, or a mix.
2. **Holding period:** throughout the **24 months** immediately before the sale, no one owned the share other than you, a partnership of which you were a member, or a person related to you. Shares issued after13June1988 are generally deemed previously owned by an unrelated person under110.6(14)(f), subject to its specific exceptions. Substituted-share and connected-corporation tracing under110.6(1) can add conditions; a newly issued or reorganized share needs a full eligibility review.
3. **Asset test over the 24 months:** throughout that period, while owned by you, your partnership or a related person, it was a share of a CCPC with **more than 50%** of the fair market value of its assets used mainly in an active business carried on primarily in Canada, or in qualifying shares or debts of connected corporations, or a mix.

**How to claim.**

- Complete **Form T657**, *Calculation of Capital Gains Deduction*, and claim on **line 25400**. You may claim any amount up to the maximum you calculate.
- If you had investment income or investment expenses in any year from 1988 on, complete **Form T936** for the **cumulative net investment loss (CNIL)**. A CNIL balance reduces the deduction available in the year.
- **ABIL and old net capital losses need the actual annual-gains-limit calculation.** The old-loss adjustment is not automatically the whole line25300 deduction:110.6(1) first offsets it by net non-eligible taxable capital gains. Use T657 Step1 with T936 ChartA; the detailed form workflow below preserves the current-year and cumulative limits. [G04][G28][G29]
- Report QSBC share dispositions on **line 1** of Part 3 of Schedule 3 and QFFP on **line 2**.
- A reserve brought into income later requires the original disposition date/year and the relevant T657 historical chart, including the2024 date split. Do not automatically use the claim-year headline LCGE for every old reserve. [G29][G44]
- Large gains, deductions and gifts require a separate **alternative minimum tax** calculation on the correct-year T691. Read its adjustments, credits and carryover rules; a large deduction does not establish either a zero AMT result or an AMT bill by itself. The2025 form expressly excludes a person who died in2025 and specified special returns. No complete2026 AMT engine is supplied here. [G46]

Related reliefs **not** covered here, refer instead: the capital gains deduction for a qualifying business transfer to an employee ownership trust (line 25395), qualifying cooperative conversions, intergenerational business transfers (Form T2066), and the capital gains deferral for eligible small business investments.

## Capital losses ([CRA: Capital losses](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html); [line 25300](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25300-net-capital-losses-other-years.html))

- An **allowable capital loss** is the capital loss × the inclusion rate (one-half).
- Allowable capital losses of the year **must** first be applied against taxable capital gains of the same year. They generally **cannot** reduce other income. Pre-1986 balances, qualifying ABIL and the special death-year/preceding-year rule in111(2) require separate treatment; do not classify every investment loss as an ABIL. [G05][G12][G21]
- Any excess becomes part of the **net capital loss** for the year. It can be carried **back to any of the three previous years** or **forward to any future year**, but only against taxable capital gains.
- **Carryback:** complete Part 5 of **Form T1A**, *Request for Loss Carryback*, with the current return. Do **not** file an amended return for the earlier year. A 2026 net capital loss can go back to 2023, 2024 and 2025. A carryback can reduce a capital gains deduction claimed in that year or a later year.
- **Carryforward:** claim on **line 25300**. Apply older losses before newer ones and keep separate balances by year. Losses from years with a different inclusion rate must be adjusted to the current rate (CRA worksheet charts).
- Applying a net capital loss reduces **taxable income**, not **net income**, so income-tested credits and benefits do not change.
- **Pre-1986 loss balance:** the special rule includes losses before23May1985 and qualifying later dispositions under a sale agreement entered before that date. After gains, other-income relief is limited to the least of excess,2,000 and the available pre-1986 balance, adjusted for earlier use/deductions. Obtain the historical worksheet; do not substitute all pre-1986 losses indiscriminately. [G05][G21][G22]
- **Business investment loss:** test39(1)(c) for a qualifying SBC share or qualifying CCPC debt and the actual disposition/deemed-disposition conditions. Only the eligible amount after the reduction rules becomes an ABIL under38(c), with gross21699/allowable21700 reporting as directed. An ordinary unpaid personal debt or any failed-company investment is not automatically an ABIL. Refer for the reduction rules, evidence and LCGE effect. [G01][G12][G21]

### Superficial loss ([ITA s.54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html); [s.40(2)(g)(i)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html))

A loss is **superficial**, and is **denied**, when **both** of these hold:

1. you, or a person **affiliated** with you, buys (or gets a right to buy) the same or an **identical** property during the period that starts **30 days before** and ends **30 days after** the sale; and
2. at the **end** of that period, you or the affiliated person still owns (or has a right to buy) that substituted property.

- Affiliated persons include you and your spouse or common-law partner; you and a corporation controlled by you or your spouse or partner; a partnership and its majority-interest partner; a trust and its majority-interest beneficiary.
- **Same taxpayer buys substituted property in a taxable account:**53(1)(f) generally adds the denied superficial loss to its ACB, subject to the statutory adjustments. This is not a guarantee of eventual deductibility. An affiliated buyer needs their own eligible basis analysis; never add another buyer's loss to the seller's remaining holdings without tracing. Partial repurchases, rights, different quantities and registered plans require a separate allocation/stop-loss review. [G08][G21]
- **Common exceptions** (not superficial): deemed sales on becoming or ceasing to be resident, on a change of use, or on death; the expiry of an option; property appropriated by a shareholder on a winding-up; becoming or ceasing to be tax-exempt within 30 days after the sale.
- Buying back inside the taxpayer's RRSP, TFSA or other registered plan: refer. The registered-plan loss-denial rules in40(2)(g)(iv) can deny a loss without recoverable taxable-account basis. A54 superficial-loss exception does not switch off other stop-loss rules. [G02][G03][G08]

### Personal-use and listed personal property ([T4037, lines 9 and 10](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html))

- **Personal-use property** (car, boat, furniture, a cottage used by the family): if the ACB is under $1,000, use $1,000; if the proceeds are under $1,000, use $1,000. If both are $1,000 or less, there is no gain or loss and nothing to report. **Losses on personal-use property are not deductible** (other than listed personal property).
- **Listed personal property (LPP)** is personal-use property within the statutory list: prints, etchings, drawings, paintings, sculptures or similar works of art, jewellery, rare folios, manuscripts or books, stamps and coins (including interests in them). LPP losses offset only LPP gains, in the year or the **three years before or seven years after**. Carry back on Form T1A.

## Capital gains reserve: paid over several years ([T4037, Claiming a reserve](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA s.40(1)(a)(iii), (1.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html))

- If part of the sale price is payable after the end of the year, you may deduct a **reserve** so the gain is taxed as the money comes in. Calculate the full gain first, then deduct the reserve.
- The ordinary reserve remaining is capped at **80%,60%,40%,20%,0% of the original gain** in the sale year and following four years, and also by the reasonable gain portion of proceeds payable after year-end. A later year includes **the prior reserve less the new reserve**, not the full original gain less another reserve. Earlier recognition can make a later increment less than one-fifth; there is no universal fixed20% annual inclusion. [G02(1)(a)][G44]
- The special **ten-year** route has its own90%,80%,70%,60%,50%,40%,30%,20%,10%,0% remaining caps. For40(1.1), the child must be resident in Canada immediately before the disposition and the property must meet the actual family farm/fishing or small-business-share conditions. Intergenerational, qualifying-business-transfer and qualifying-cooperative-conversion routes have separate40(1.2)–(1.4) tests. Do not give every child sale or related transfer a ten-year reserve. [G02]
- Claim on **Form T2017**, *Summary of Reserves on Dispositions of Capital Property*, each year.
- **No reserve** under40(2)(a) if the taxpayer was non-resident or exempt at year-end or at any time in the immediately following year, or sold to a corporation they controlled directly or indirectly in any manner immediately after the sale, or a partnership in which they were immediately after disposition a majority-interest partner. Check later-year status before treating a provisional claim as final. [G02(2)(a)]
- For QSBC shares or QFFP, retain the original sale year and applicable T657 chart; the headline current-year cap is not a substitute. For2025, T2017 separates prior-year reserves and current claims across QFFP,QSBC,child,QBT,QCC and other property, with the signed net adjustment at line67060 transferred to Schedule3 line19200. [G29][G44]

## Boundaries and exceptions ([T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html))

| Situation | Treatment | Source |
| --- | --- | --- |
| Home owned less than 365 consecutive days, no listed life event | Business income, fully taxed; no principal residence exemption; loss deemed nil | ITA s.12(12)–(14); [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Home owned365days or more, or listed life event applies | Statutory flipping rule may not apply; separately determine business versus capital. PRE only after capital/property/residence/designation tests | [ITA12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html), [39](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html), [54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) |
| Home was principal residence every year owned (resident throughout) | Subject to the complete formula and capital-property gate, gain sheltered; actual2025 Schedule3 Part2 and T2091(IND) Section1 page2 still required | CRA principal residence page; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Two homes in the family unit | Only one can be designated per year for the whole family unit; choose the years per property | ITA s.54 "principal residence" (c); [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Owner non-resident throughout the acquisition year | No "plus 1" year | ITA s.40(2)(b), variable B; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Loss on a home, car, boat or other personal-use property | Not deductible | T4037; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Personal-use item with ACB and proceeds both $1,000 or less | No gain or loss; do not report | T4037; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Loss on shares, same shares bought back within 30 days before or after and still held 30 days after | Superficial loss denied; add to ACB of the new shares | ITA s.54; CRA capital losses; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Repurchase31or more days after sale, with no taxpayer/affiliated acquisition or right in the61-day window | Superficial-loss test not met; check all other loss restrictions before allowing | [ITA54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html), [40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Loss sale then acquisition or right by spouse or an affiliated corporation | Test both acquisition/right in the30day-before/after window and ownership/right at its end; only then superficial, subject to other stop-loss rules; trace the correct substituted owner for ACB | [ITA54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html), [40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html), [53](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-53.html) |
| Eligible listed securities/fund gift to qualified donee | Zero inclusion only for eligible portion; advantage, flow-through shares and partnership exchanges need adjustments; T1170 | [ITA38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html), [38.2](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.2.html), [T1170](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1170/t1170-25e.pdf) |
| QSBC shares held less than 24 months by you or related persons (including new treasury shares) | Generally fails the holding-period test; no LCGE | T4037 definition; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| CCPC asset mix at sale does not meet all-or-substantially-all test | No automatic QSBC entitlement; trace qualifying connected-company assets and obtain eligibility/purification review before sale | [ITA248](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html), [110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html) |
| Seller not resident throughout year | Test110.6(5) residence deeming for deduction; independently test reserve year-end/following-year conditions | [ITA110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html), [40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Net capital loss vs employment or business income | Generally unavailable; pre-1986 balance,111(2) death-year rules and qualifying ABIL require their separate calculations | CRA capital losses; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Sale proceeds received over time | Reserve over up to five years (ten for certain transfers to a child) | T4037; ITA s.40; [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |

## Worked cases

All cases: individual resident in Canada throughout 2026, amounts in Canadian dollars, federal treatment only. The amounts are illustrations, not official figures.

**C1. Shares bought twice, part sold (average cost).**
Bought 100 shares of one public company at $20 each plus $10 commission (cost $2,010), later 100 more at $30 each plus $10 commission (cost $3,010). Total cost $5,020 for 200 shares, so the average cost is $25.10 a share. In June 2026 sold 150 shares at $40 each: proceeds $6,000, commission $10.
- ACB of the shares sold: 150 × $25.10 = $3,765.
- Capital gain: $6,000 − $3,765 − $10 = $2,225.
- Taxable capital gain (one-half): $1,112.50, reported through Schedule 3 (line 4, publicly traded shares) to line 12700.
- The 50 shares left keep the average cost: ACB $1,255.

**C2. Loss sale and buy-back (superficial loss).**
100 shares with an ACB of $5,000 sold on 10 March 2026 for $3,000 (a $2,000 loss). On 25 March 2026 the client buys 100 identical shares for $3,100 and still holds them on 9 April 2026 (30 days after the sale).
- Both tests are met, so the $2,000 loss is a superficial loss and is denied for 2026.
- The client bought the substituted shares, so the new ACB is $3,100 + $2,000 = $5,100.
- If instead the client bought back on15April2026,36days after sale, with no taxpayer/affiliated acquisition or right in the window8February–9April, the superficial-loss rule would not deny the loss. Assuming no other restriction, allowable capital loss is1,000.

**C3. Cottage and city home in one family (principal residence formula).**
A couple owns a city home (bought 2008) and a cottage the husband bought in 2017 for $300,000. The cottage is sold in 2026 for $700,000 with $20,000 of selling costs. Both were ordinarily inhabited by the family every year; both spouses were resident in Canada throughout. They decide to designate the cottage for4years(2023–2026) and keep the other years for the city home. Assume capital property, no change-of-use/CCA issue, all designated years eligible, D=0 and no1994 election adjustment.
- Gain: $700,000 − $300,000 − $20,000 = $380,000.
- Years owned ending after acquisition: 2017 to 2026 = 10. Years designated = 4, plus 1 = 5.
- Exempt part: $380,000 × 5 ÷ 10 = $190,000. Remaining gain: $190,000.
- Taxable capital gain: $95,000.
- Report on Schedule 3 and the full Form T2091(IND) (the cottage was not the principal residence for all years or all years but one). The city home cannot be designated for 2023 to 2026 when it is sold later. Compare gain per year on each property before choosing the years.

**C4. Selling qualified small business shares (LCGE 2026).**
A founder sells all her shares of a CCPC in August 2026 for a capital gain of $1,500,000. She and related persons held the shares for more than 24 months, the more-than-50% asset test was met throughout, and at the time of sale 90% or more of the assets were used in an active business carried on primarily in Canada. No LCGE used before, no CNIL, no ABIL, no net capital losses claimed.
- Taxable capital gain: $750,000 (line 12700).
- Capital gains deduction (2026 limit): $637,500 on line 25400, supported by Form T657 and Form T936.
- Taxable capital gain left in taxable income: $112,500.
- This leaves112,500 of this gain in ordinary taxable income before any other taxpayer items. It is not112,500 of tax payable. Obtain the correct-year T691 AMT calculation before finalising; no AMT dollar amount is established here.

**C5. Condo sold after nine months (flipping rule).**
Bought 1 February 2026 for $500,000, sold 1 November 2026 for $560,000, selling costs $10,000. No listed life event.
- Owned less than 365 consecutive days, so it is a flipped property.
- Profit $50,000 is **business income** (Form T2125), fully included; no inclusion rate, no principal residence exemption.
- If the move satisfies the complete eligible-relocation exception, including the40km comparison and causal link, the statutory flipping deeming does not apply. Reassess business versus capital on general principles, then PRE separately if capital. A job move or273-day holding period alone does not establish an exemption.

**C6. Personal-use property floor.**
A boat bought for $800 is sold for $1,500.
- ACB is under $1,000, so ACB is treated as $1,000. Gain: $1,500 − $1,000 = $500; taxable capital gain $250, reported on Schedule 3 line 9.
- Had it sold for $900, both ACB and proceeds would be $1,000 or less: no gain, nothing to report. Had it sold at a loss, the loss would not be deductible.

**C7. Net capital loss carried back.**
In 2026 the client has capital losses of $10,000 and capital gains of $4,000.
- Allowable capital loss $5,000; taxable capital gain $2,000. Net: $3,000 of unapplied allowable loss, which is the 2026 net capital loss.
- Nothing goes on line 12700 for 2026, and the loss cannot reduce 2026 employment income.
- Carry it back against taxable capital gains of 2023, 2024 or 2025 on Part 5 of Form T1A filed with the 2026 return, or keep it for line 25300 in a later year.

## When to refuse or refer

Refer to a Canadian tax professional (CPA) when:

- the client was **not resident in Canada** for the whole year, arrived or left in the year, or was non-resident while owning a home (departure tax, part-year rules and the acquisition-year plus-one test);
- a home was **rented, used for business, or had CCA claimed**, or a s.45(2) or s.45(3) election is in play or was missed;
- a home sale may be **business income** on general principles (repeat buying and selling, building to sell), even if held 365 days or more;
- an **LCGE claim** on private company shares or farm or fishing property: the 24-month and asset tests, purification, CNIL, ABIL history, and **alternative minimum tax** all need a full calculation;
- a **qualifying business transfer**, **intergenerational business transfer**, cooperative conversion or small business investment deferral is contemplated; obtain the current enacted conditions and actual forms rather than carrying forward an old proposal label;
- a **superficial loss** involving a spouse, corporation, trust or registered plan;
- **trusts, estates, partnerships** or corporations are the seller, or a sale or rollover to a related or controlled corporation;
- **crypto-assets**, options, short sales or frequent trading where the income may be business income;
- a **late principal residence designation** or amended return is needed and the penalty may apply;
- a sale by a **non-resident** of Canadian property: use the ca-nonresident-cgt skill.

Refuse to give a figure when the purchase cost, dates or ownership history cannot be established; ask for the records instead of estimating.

## Returns being filed now: tax year 2025 (dated section) ([CRA line 25400](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25400-capital-gains-deduction.html))

- 2025 returns were due **30 April 2026**, or **15 June 2026** if the individual or their spouse or common-law partner was self-employed; any balance was payable by **30 April 2026** in both cases ([CRA important dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html)). Late 2025 returns and adjustments still use these rules.
- Inclusion rate for 2025: one-half ("The inclusion rate for 2025 is 50%").
- LCGE for 2025: $1,250,000, deduction limit $625,000 (not indexed for 2025). For 2024 the limit changed mid-year (a lower limit before 25 June 2024 and $1,250,000 from 25 June 2024); Form T657 has separate charts. Refer if a 2024 reserve, partnership or trust allocation straddles that date.
- A 2025 net capital loss can be carried back to 2022, 2023 and 2024 on Form T1A.
- Some CRA landing-page wording still calls the LCGE increase proposed and contains inconsistent historical amounts. For2025 use the actual T657 edition; for current entitlement use enacted110.6 and117.1 plus the indexation table. Do not copy the landing page's historical typos into a2024 reserve or2023 cap. [G04][G06][G18][G23][G29]

## Filing and payment

- **Report taxable/reportable capital dispositions in the sale/deemed-sale calendar year** through the correct-year Schedule3 and T1. Preserve the specific no-report rule for personal-use property with both cost and proceeds at/below1,000, and the special reporting route for fully designated homes. Positive taxable capital gains reach line12700; a net capital loss is recorded rather than entered as negative employment-offsetting income. [G17][G19][G26]
- Home sales: **Schedule 3** designation (line 17900) and **Form T2091(IND)**.
- Capital gains deduction: **Form T657**, **Form T936**, **line 25400**.
- Net capital losses of other years: **line 25300**. Carryback: **Form T1A**.
- Reserve: **Form T2017**. Gifts of securities: **Form T1170**.
- **2026 ordinary T1:**30April2027. Qualifying business filers and their cohabiting spouse/common-law partner generally have15June2027, but the tax-shelter-expenditure exception in150(1)(d)(ii) restores30April; ordinary balance payment remains30April2027. CRA's published2027 business deadline page confirms these dates. Death/special returns need their actual rules. [G17][G38]

## Rebuild the transaction file before completing the return

Create a disposition schedule with one row per asset/pool: owner and percentage, capital/business conclusion, acquisition/disposition dates, currency and actual exchange-rate evidence, gross proceeds, acquisition cost, acquisition expenses, improvements/other ACB changes, selling outlays, raw gain/loss, special-rule adjustment, reserve, inclusion and form destination. Keep the evidence and unresolved items next to that row. An amount computed from assumed cost or undocumented ownership is not a final filing number. [G02][G09][G19][G26]

**Remaining identical-property pool.** On a new purchase, pool ACB becomes the **remaining pre-purchase adjusted pool plus the new acquisition cost**, then divide by total remaining units. Do not add the cost of shares already sold back into the pool. A sale removes units×average ACB and leaves the average unchanged. Reinvested distributions add the cost of actual additional units; T3 box42 and corporate actions require their own adjustments. Employee-option securities and certain other statutory exclusions under47 need separate treatment rather than unconditional averaging. [G08][G09][G19]

**T3 box42 and below-zero control.** A positive box42 amount reduces the relevant trust-unit pool; a negative amount increases it by its magnitude. If100 of pool ACB is reduced by a150 capital adjustment, recognize50 of deemed capital gain and set ACB to zero. Do not carry negative50 forward and tax it again on a later sale. Conversely a negative box42 amount of50 increases100 to150. Link each adjustment to the actual trust and units. [G02(3)][G08(1)(a),(2)(h)][G19]

**Use a T5008 as reconciliation evidence, not an automatic return.** The actual2026 slip is available. It shows currency13, transaction date14, security type15, quantity16, description17, ISIN/CUSIP18, cost/book value20 and proceeds21. The preparer's guide uses settlement date in14 and permits1231 for aggregated transactions, so do not infer an individual trade's acquisition date from that field. Box20 may not equal tax ACB; reconstruct transfers between brokers, prior purchases/sales, reinvestments and adjustments. Box21 is gross proceeds under the guide: do not deduct selling commission again if a statement separately shows only net cash. Reconcile any mismatch to original confirmations and prevent duplicate reporting of the same transaction from imported slips and the broker schedule. Foreign-currency slip amounts require CAD conversion before the gain calculation. [G40][G41][G42][G43]

**Gifts and inheritances.** General69(1)/70(5) FMV rules do not override express rollovers, spouse/farm exceptions or deemed-disposition rules. Keep donor/deceased date and valuation evidence, original transfer treatment and any relevant election. An unknown inherited basis cannot be replaced by current market value. Depreciable property needs a separate CCA/recapture analysis; a depreciable-property loss is not an ordinary capital loss. [G12][G36][G37][G19]

## Complete the actual annual forms in order

The following field map is for **actual2025 forms**, used for the dated2025 bridge and to check the method. Use enacted2026 rules for2026 working papers, then verify the final2026 annual form editions and approved software before filing. **Do not silently carry these2025 field numbers into a final2026 return.** This edition limit does not mean all2026 forms are unavailable: T5008(26) is published. [G26][G27][G28][G29][G30][G41][G44][G45][G46]

### Schedule3 and principal residence: actual2025 editions

1. **Part1** asks about Canadian housing/right dispositions held less than365days at17905 and records any life-event category at17906. Keep the acquisition/sale dates and supporting event. The form's shorthand about life events does not replace the ordinary business-versus-capital decision under the Act. Business income goes through the applicable business schedule, not half inclusion simply because one box was ticked. [G12][G13][G26]
2. **Part2,17900** is the principal-residence designation: box1 all years/all but one; box2 some years; box3 multiple properties. Choose from the complete family/residence/designation history, not solely years owned. Actual T2091(IND) Section1 onpage2 records address, acquisition year9955, relevant proceeds9954, designated years9956 and the taxpayer's designation, signature, SIN and date. Use only the taxpayer's share, and the residence portion if mixed use. For box1, Section1 alone is the stated shortcut; box2or3 also needs applicable Section2 beginningpage3. A separate form is required for each property. [G26][G30]
3. On a paper return attach the required signed form; for electronic filing follow the form/software instructions and retain the signed designation and source records. Do not put SINs or completed client forms in public GitHub. Pre1982 ownership,1994 elections, T2091(IND)-WS and special mixed-use/estate situations need their actual historical calculations. A simple current example does not certify those engines. [G20][G30]
4. **Part3** separates QSBC(line1,10699/10700), QFFP(line2,10999/11000), qualifying foreclosure/repossessions(line3,12399/12400), public/other shares(line4,13199/13200), real/depreciable/other property(line5,13599/13800), debt(line6,15199/15300), crypto capital dispositions(line7,15200/15301), other foreclosures(line8,15499/15500), PUP(line9,15800) and LPP(line10,15900). Use property character first; an actual principal-residence result can have its own directed destination, so don't use the real-estate row for every fully exempt home. [G26][G30]
5. **Part4** reconciles directed deferrals/slips/other adjustments, including T3 amounts17600 and reserve adjustment19200 from T2017; total19700 flows to Part5. Avoid reporting both underlying transactions and an already included allocation a second time. **Part5** applies the ordinary50% fraction and separately adds specific partnership amount19890 at100%, producing19900. A positive19900 goes to T1 12700; a negative result is used for the loss records/T1A, not a negative wage deduction. The special19890 amount is not an instruction to apply a general two-thirds inclusion rate. [G26]

**Late PRE designation.** Keep the original return, actual disposition/designation facts, reason for delay and complete request.220(3.2),(3.21) permit discretionary acceptance, subject to the ten-calendar-year application rule; acceptance is not automatic. The220(3.5) penalty is the lesser of8,000 and100×complete months from the required date to a satisfactory application. A12-complete-month illustration is1,200;100months is capped at8,000. Do not describe late acceptance as a no-penalty guarantee. [G16][G20]

### T657 and T936: establish entitlement, not just the headline LCGE

**Qualification file first.** Prove residency/deeming, exact asset and original disposition date, qualifying property, current-year and prior-year deductions, losses, investment income/expenses and any trust/partnership allocation. The at-sale SBC standard is all-or-substantially-all qualifying asset value; the24-month QSBC test is **more than50%**, not at least50%. Connected chains, substitutions, new issues and the deemed relationship of partnerships under110.6(14) require actual tracing. QFFP has its own ownership/use and historical tests; a QSBC checklist cannot certify a farm. Keep the specialist eligibility review with this computation. [G04][G48]

**Actual2025 T657 Step1, page3.** Reconcile qualifying Schedule3 amounts10700/11000/12400 plus eligible reserve amounts from T2017line13, apply the half fraction and the directed qualifying-transfer deductions to obtain the eligible amount. Compare with the form's overall taxable-gain amount after its T3 and directed transfer adjustments. At lines14–16, subtract **T936 ChartA line14 net non-eligible taxable gains** from old losses deducted at25300, floored at zero. Adjust qualifying ABIL separately at17–19. The eligible amount less those adjusted losses, floored at zero, is the annual gains limit21. This is why subtracting every25300dollar from eligible gains gives the wrong result. Keep all T2048 and trust-specific directed adjustments if present rather than using the simplified example below. [G04][G28][G29]

**Cumulative limit and remaining lifetime room.** T657 Step2, page4, brings forward eligible taxable gains after1984 and subtracts the directed prior losses, current adjusted losses, CNIL and prior capital-gains deductions. Claiming the2026 headline637,500 is possible only to the extent the actual annual limit, cumulative limit, eligible current gain and remaining lifetime limit all allow it. Do not subtract CNIL or a prior deduction twice by mixing simplified remaining-room arithmetic with a form total that already includes it. Use the claim-year form and historic chart/inclusion-rate adjustments for each prior balance. [G04][G06][G18][G29]

**Actual2025 T936.** Parts1and2 separate investment expenses from investment income, including their specified property/partnership items and adjusted capital-loss amounts. Part3 combines current amounts with reconciled opening totals, then computes nonnegative CNIL for T657 Step2line16. ChartA computes net non-eligible taxable gains for the T657 old-loss adjustment. Do not place an ABIL, already-counted reserve or every business expense in the investment columns by default. If prior forms are missing, reconstruct the1988onward history with the form's stated pre1992 exceptions. The2025 form's line20 references the **2024** T936 line19; do not read the same line number from the2025 form as though the editions were interchangeable. Fetch the actual prior edition and reconcile opening balances before finalizing. This method does not certify an unexamined2024 field map. [G28][G29]

**Historical charts and allocations.** Actual2025 T657 Step3 asks both original disposition year and reserve/trust/partnership category. Its2024 Period1 reserve chart uses508,418;Period2 uses625,000. Its2025 Part1 chart for certain2025 allocations of a Period1-of2024 disposition uses522,145;Part2 for current/post24June2024 dispositions uses625,000. These are **deduction** amounts with their chart-specific predicates, not interchangeable gain caps or a universal2025 limit. The2026 current eligible-gain limit does not overwrite them. The actual2025 T657 historical table gives2023gain limit971,190 and2024Period1gain limit1,016,836; don't copy inconsistent figures from the line25400 landing page. Refer with the original-year forms, T3/T5013 detail and previous claims when a historical chart is required. [G23][G29]

### Capital-loss carryback and carryforward controls

Keep separate schedules for ordinary net capital losses and LPP losses. Ordinary loss records show origin year, gross capital loss, original inclusion rate, original allowable-loss balance, prior use, claim-year adjustment, current use and remaining original-year balance. For example a1995 allowable-loss balance7,500 at75% yields5,000 deductible at50%; using3,000 of that adjusted balance consumes4,500 of the original allowable-loss balance and leaves3,000 of the original balance, equivalent to2,000 at50%. Do not subtract a claim-year amount from an unadjusted origin-year balance. [G05][G21][G22]

For an ordinary **2025** carryback, actual T1A **Part5** allocates the available amount to2022/2023/2024 at66360/66370/66380 and totals the request, with the remaining balance retained. Part6 uses the separate LPP2022/2023/2024 fields66420/66430/66440. Complete the certification/signature/date and representative details required by the actual form. Filing a T1A request does not prove CRA has processed it; retain the submitted request and reassessment before marking the prior-year result settled. Do not amend the earlier return simply to make this carryback. **2026** carrybacks reach2023–2025, but require that year's actual form. [G21][G27]

Ordinary loss deductions reduce taxable income rather than net income; they don't retrospectively change the net-income base for income-tested benefits. A carryback can nevertheless change an earlier LCGE deduction, requiring a linked recomputation. Death-year111(2), pre1986 other-income use, ABIL and loss-restriction/affiliated/registered-plan cases remain separate, evidence-led computations. [G04][G05][G21][G22]

For LPP, apply the statutory list, not a prediction that an asset appreciates. Apply the1,000floor subject to46's partial-interest and set rules; a collection/set cannot be sliced into artificial1,000allowances. LPP losses offset LPP gains only, oldest eligible losses first, within three preceding/seven following years. A2026 LPP loss can potentially apply to2023–2025 or2027–2033, subject to actual LPP gains and prior use. A PUP loss is otherwise denied; absence of a superficial loss alone does not create a deduction. [G02][G03][G10][G11][G21]

### Reserve schedule and gift schedule

For each reserve property retain original proceeds, original gain, sale year, property/transfer category, balance **payable after year-end**, prior claimed reserve, current reasonable maximum, elapsed-year cap, any prior-reserve ceiling, chosen current reserve and the resulting current gain. Ordinary reserve is no more than the lesser of gain×deferred proceeds/proceeds and the applicable80/60/40/20/0% remaining cap. Later-year reserve cannot exceed the prior claimed reserve; include prior reserve less current, with the complete40(2)(a) prohibitions tested. Do not use a repayment of principal as the taxable gain or recognize the original gain afresh every year. [G02][G44]

Actual2025 T2017 uses categoriesA(QFFP),B(QSBC),C(other specified child transfers),D(QBT),E(QCC),F(other), preserving original disposition-year information. It includes separate old pre13November1981 and non-qualifying-security gift instructions, which are not the ordinary five-year engine. Its net reserve adjustment67060 feeds Schedule3 19200. For an eligible-gain deduction, carry the appropriate qualifying amount and historical year into T657 as directed. A negative reserve adjustment can be legitimate where a new sale-year reserve is claimed; do not force every reserve line positive. [G29][G44]

**Eligible gifts:** use the actual T1170 for qualifying property and donee. Without an advantage, the otherwise eligible specified gain may have zero inclusion. With an advantage, zero-inclusion gain is prorated by eligible gift amount/proceeds; the remaining gain has ordinary half inclusion under38.2. For proceeds10,000, ACB6,000 and eligible gift8,000, gain4,000 splits3,200zero-inclusion and800ordinary, producing400taxable capital gain before any separate flow-through/AMT adjustment. Report ordinary share gains as directed to actual2025 Schedule3 13200, debt15300 or ecological land13800; keep the charitable receipt/credit calculation separate. Special exchangeable securities, partnership interests and flow-through-share deemed gains need their full conditions; no universal zero-gain promise. [G01][G45][G47]

## Extra worked checks and decision cases

These synthetic examples preserve all seven original families and add cases for the identified weaknesses. They calculate specified capital amounts, not a client's final federal/provincial tax or AMT. Inputs assume ordinary taxable-account capital property unless a different treatment is stated.

### Check1: original average-cost partial sale and a later purchase

C1's remaining50shares have1,255ACB. If another50shares are acquired for2,000all-in, the new100-share pool has3,255ACB and32.55average, not the original5,020plus2,000. [G09][G19]

```oa-check
name: Canadian capital shares partial sale preserves remaining pool
inputs:
  first_cost: 2010
  second_cost: 3010
  initial_units: 200
  sold_units: 150
  proceeds: 6000
  sale_cost: 10
  later_cost: 2000
  later_units: 50
steps:
  initial_pool: first_cost + second_cost
  average: initial_pool / initial_units
  sold_acb: average * sold_units
  gain: proceeds - sold_acb - sale_cost
  taxable_gain: gain * 0.5
  remaining_pool: initial_pool - sold_acb
  remaining_units: initial_units - sold_units
  new_pool: remaining_pool + later_cost
  new_average: new_pool / (remaining_units + later_units)
expected:
  initial_pool: 5020
  average: 25.1
  sold_acb: 3765
  gain: 2225
  taxable_gain: 1112.5
  remaining_pool: 1255
  new_pool: 3255
  new_average: 32.55
```

### Check2: original loss repurchase and original annual net loss

For C2 the full100-share self-repurchase is within8February–9April2026 and still held at the end; all2,000 is denied and substituted ACB becomes5,100. The15April alternative is36days after sale, with no other in-window acquisition/right and no other restriction. For C7 assume ordinary losses, no LPP/ABIL/stop-loss complications. [G02][G03][G08][G21]

```oa-check
name: Canadian ordinary and superficial losses use distinct balances
inputs:
  old_acb: 5000
  sale_proceeds: 3000
  repurchase_cost: 3100
  year_gross_losses: 10000
  year_gross_gains: 4000
steps:
  denied_loss: old_acb - sale_proceeds
  substituted_acb: repurchase_cost + denied_loss
  alternative_allowable_loss: denied_loss * 0.5
  year_allowable_losses: year_gross_losses * 0.5
  year_taxable_gains: year_gross_gains * 0.5
  net_capital_loss: max(0, year_allowable_losses - year_taxable_gains)
  positive_12700: max(0, year_taxable_gains - year_allowable_losses)
expected:
  denied_loss: 2000
  substituted_acb: 5100
  alternative_allowable_loss: 1000
  year_allowable_losses: 5000
  year_taxable_gains: 2000
  net_capital_loss: 3000
  positive_12700: 0
```

### Check3: cottage formula, full designation and no manufactured PRE loss

C3 assumes acquisition-year residence, all four eligible designations, capital character and D=0. The second subcase uses10designated years and10owned years with plus-one: the negative algebraic result is nil under257. D must be calculated separately in a relevant1994-election case. [G02][G30][G39]

```oa-check
name: Canadian principal residence formula preserves D and floors at nil
inputs:
  proceeds: 700000
  acb: 300000
  costs: 20000
  designated_years: 4
  owned_years: 10
  d_adjustment: 0
steps:
  gain: proceeds - acb - costs
  exempt_ratio_amount: gain * (designated_years + 1) / owned_years
  remaining_gain: max(0, gain - exempt_ratio_amount - d_adjustment)
  taxable_gain: remaining_gain * 0.5
  all_designated_result: max(0, gain - gain * (owned_years + 1) / owned_years - d_adjustment)
expected:
  gain: 380000
  exempt_ratio_amount: 190000
  remaining_gain: 190000
  taxable_gain: 95000
  all_designated_result: 0
```

### Check4: eligible QSBC headline limit is not a tax bill

C4 assumes all actual QSBC tests, residence and unused limits proved, no CNIL/ABIL/loss/prior-deduction reduction. The indexed2026 result637,500 remains conditional; taxable amount112,500 is not tax payable. [G04][G06][G18]

```oa-check
name: Canadian eligible 2026 gain and indexed deduction are different units
inputs:
  gross_gain: 1500000
  eligible_gain_limit: 1275000
steps:
  taxable_gain: gross_gain * 0.5
  deduction_cap: eligible_gain_limit * 0.5
  deduction: min(taxable_gain, deduction_cap)
  remaining_taxable_amount: taxable_gain - deduction
expected:
  taxable_gain: 750000
  deduction_cap: 637500
  deduction: 637500
  remaining_taxable_amount: 112500
```

### Check5: flipping and personal-use floors

C5 is273days from1February to1November2026, no qualifying life event and already-established Canadian housing facts. Its50,000profit is business income, with no half inclusion/PRE. C6 is an ordinary whole boat, not a partial-interest/set/gifting-arrangement case. [G10][G13]

```oa-check
name: Canadian flipped profit and personal use floor are separate treatments
inputs:
  condo_proceeds: 560000
  condo_cost: 500000
  condo_sale_cost: 10000
  boat_acb: 800
  boat_proceeds: 1500
  alternative_proceeds: 900
steps:
  business_profit: condo_proceeds - condo_cost - condo_sale_cost
  pup_acb: max(1000, boat_acb)
  pup_gain: max(1000, boat_proceeds) - pup_acb
  pup_taxable: pup_gain * 0.5
  alternative_gain: max(1000, alternative_proceeds) - pup_acb
expected:
  business_profit: 50000
  pup_acb: 1000
  pup_gain: 500
  pup_taxable: 250
  alternative_gain: 0
```

### Check6: reserve can produce no additional gain in a later year

Original gain100,000/proceeds200,000/deferred60,000. Choose the maximum ordinary permissible reserve30,000 in year1, recognizing70,000. If60,000remains payable after year2, the still-permitted30,000reserve leaves **zero** further reserve-related gain that year, not a compulsory20,000. Full gain remains recognized by the final deadline. This assumes no prohibition and no other sale-year amounts. [G02][G44]

```oa-check
name: Canadian reserve uses remaining reserve and prior year reconciliation
inputs:
  original_gain: 100000
  proceeds: 200000
  deferred_year1: 60000
  deferred_year2: 60000
steps:
  reasonable_year1: original_gain * deferred_year1 / proceeds
  cap_year1: original_gain * 0.8
  reserve_year1: min(reasonable_year1, cap_year1)
  recognized_year1: original_gain - reserve_year1
  reasonable_year2: original_gain * deferred_year2 / proceeds
  cap_year2: original_gain * 0.6
  reserve_year2: min(reasonable_year2, cap_year2, reserve_year1)
  recognized_year2: reserve_year1 - reserve_year2
  reserve_final_year: original_gain * 0
expected:
  reserve_year1: 30000
  recognized_year1: 70000
  reserve_year2: 30000
  recognized_year2: 0
  reserve_final_year: 0
```

### Check7: non-eligible gains absorb old losses before the LCGE adjustment

Synthetic all-capital case with no T2048/trust adjustments, current loss or ABIL: eligible taxable gains30,000, non-eligible taxable gains20,000. An old-loss deduction15,000is fully absorbed by non-eligible gains for this limit;35,000leaves15,000adjusted loss reducing the eligible annual limit to15,000. CNIL/cumulative/lifetime constraints still require their own steps. [G04][G28][G29]

```oa-check
name: Canadian annual gains limit adjusts old losses for non eligible gains
inputs:
  eligible_taxable_gain: 30000
  other_taxable_gain: 20000
  old_loss_a: 15000
  old_loss_b: 35000
steps:
  total_taxable_gains: eligible_taxable_gain + other_taxable_gain
  a_limit: min(total_taxable_gains, eligible_taxable_gain)
  non_eligible_excess: max(0, total_taxable_gains - a_limit)
  adjusted_loss_a: max(0, old_loss_a - non_eligible_excess)
  annual_limit_a: max(0, a_limit - adjusted_loss_a)
  adjusted_loss_b: max(0, old_loss_b - non_eligible_excess)
  annual_limit_b: max(0, a_limit - adjusted_loss_b)
expected:
  total_taxable_gains: 50000
  non_eligible_excess: 20000
  adjusted_loss_a: 0
  annual_limit_a: 30000
  adjusted_loss_b: 15000
  annual_limit_b: 15000
```

### Check8: historical allowable-loss balance is not a current-rate balance

Origin1995rate75%, remaining allowable balance7,500; current ordinary rate50%. Current deduction3,000consumes4,500origin-year allowable-loss units and leaves3,000origin units, equivalent to2,000current-rate deduction. Keep rates and units on both sides of the ledger. [G05][G21][G22]

```oa-check
name: Canadian capital loss rate conversion preserves origin balance units
inputs:
  origin_allowable_balance: 7500
  origin_rate: 0.75
  current_rate: 0.5
  current_deduction: 3000
steps:
  current_equivalent: origin_allowable_balance * current_rate / origin_rate
  origin_consumed: current_deduction * origin_rate / current_rate
  origin_remaining: origin_allowable_balance - origin_consumed
  current_remaining_equivalent: origin_remaining * current_rate / origin_rate
expected:
  current_equivalent: 5000
  origin_consumed: 4500
  origin_remaining: 3000
  current_remaining_equivalent: 2000
```

### Check9: gift advantage and T3 capital adjustment

Gift example assumes qualifying listed securities, eligible donee/receipt and no flow-through/partnership special gain. Ordinary taxable400does not settle AMT or the charitable credit. The separate T3example proves below-zero reset and the negative-box magnitude. [G02][G08][G19][G45][G47]

```oa-check
name: Canadian gift advantage and trust unit adjustments avoid blanket zero rates
inputs:
  gift_proceeds: 10000
  gift_acb: 6000
  eligible_gift: 8000
  pool_acb: 100
  positive_box42: 150
  negative_box42_magnitude: 50
steps:
  gift_gain: gift_proceeds - gift_acb
  zero_inclusion_gain: gift_gain * eligible_gift / gift_proceeds
  ordinary_gain: gift_gain - zero_inclusion_gain
  ordinary_taxable: ordinary_gain * 0.5
  deemed_gain: max(0, positive_box42 - pool_acb)
  reset_acb: max(0, pool_acb - positive_box42)
  increased_acb: pool_acb + negative_box42_magnitude
expected:
  gift_gain: 4000
  zero_inclusion_gain: 3200
  ordinary_gain: 800
  ordinary_taxable: 400
  deemed_gain: 50
  reset_acb: 0
  increased_acb: 150
```

**Non-numeric decision controls:** exactly365days is outside the statutory less-than365test but may still be a business sale;89days separation fails the90day branch; at exactly50% qualifying asset value the QSBC more-than50% history test fails; buying onday31does not cure an earlier affiliated in-window purchase/right; disposing of the replacement before the window ends can change the superficial test but leaves other loss restrictions; missing original ownership/basis/designation/transfer eligibility holds that result; a45(3) election cannot undo prohibited post1984CCA. A child not resident immediately before transfer does not qualify for40(1.1) just because the seller is resident; partnership majority interest can prohibit even an ordinary reserve. An unapproved source method does not inherit a named accountant's approval from a country directory. [G02][G03][G04][G07][G13][G14]

## Required handoff and unresolved work

Return a calculation file, source records, completed draft schedules/forms or the exact missing fields, loss/reserve history, election/designation decisions, year/form editions and dates, and the unresolved specialist work. Keep **prepared**, **reviewed**, **submitted** and **CRA processed/paid** distinct. A successful plugin call or a structurally valid file does not prove legal correctness, accountant approval, return acceptance or payment. No real account, signature, submission, designation, election or payment is made by this method alone.

Use ca-tax-residency for part-year/residency decisions, ca-nonresident-cgt for non-resident Canadian dispositions and ca-return-assembly for the wider T1. Quebec's separate provincial return is not the default federal companion for an Ontario employee. If the live start tool recommends Quebec or credits an accountant for a different retrieved method, preserve that response and the actual method-level approval label rather than manufacturing approval here. The present source remains tier2 with no named approval; a reviewer of tax sources is not automatically the approving accountant.

## Completion checklist

- [ ] Residence in Canada confirmed for the whole year (and for the LCGE test and the "plus 1" year).
- [ ] Each disposition: date, proceeds, ACB (rebuilt from records, average cost for identical property), outlays, currency conversion.
- [ ] Flipping rule checked for every Canadian housing unit held less than 365 days; life event documented if relied on.
- [ ] Principal residence: years owned, years designated, family unit's other homes, Schedule 3 designation box and T2091(IND) completed.
- [ ] Superficial loss window (30 days before and after) checked for every loss, including spouse and own corporation.
- [ ] Personal-use property floor and LPP rules applied; no personal-use losses claimed.
- [ ] Ordinary one-half inclusion applied once; specified gifts, already-taxable slip amounts and special partnership amounts treated correctly. No proposed two-thirds threshold used.
- [ ] LCGE: QSBC or QFFP tests documented; prior deductions, CNIL (T936), ABIL and line 25300 claims taken into account; 2026 limit used; AMT checked (T691).
- [ ] Net capital loss balances by year updated; carryback on T1A if chosen.
- [ ] Reserve eligibility, unpaid-proceeds fraction, remaining caps, prior reserve, later-year recognition and T2017 reconciliation checked if proceeds are paid over time.
- [ ] Return filed and balance paid by the dates above.

## Sources

- [G01] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html). Read for ITA38(a)–(c), ordinary half, gifts/exchange and allowable loss exceptions. Read 2026-11-14.
- [G02] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html). Read for ITA40(1),(1.01),(1.1)–(1.4),(2)(a),(b),(g),(3), gain/loss/reserves, denials, PRE includingD and negativeACB. Read 2026-11-14.
- [G03] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html). Read for ITA54 relevant ACB/capital/PUP/LPP/principal-residence/family/land and full superficial-loss definition; not all definitions. Read 2026-11-14.
- [G04] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html). Read for ITA110.6 annual/cumulative/CNIL, QSBC full definition, deductions(2)–(2.3), residence(5), new-share/tracing(14) and valuation opening; not fullQFFP/transfer engine. Read 2026-11-14.
- [G05] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html). Read for ITA111 relevant(1)(b),(1.1),(2),(3), and(8) loss definitions, old-rate/oldest/death/pre1986 scope; not a fullcorporate loss engine. Read 2026-11-14.
- [G06] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.1.html). Read for ITA117.1 all operative(1)–(4), particularly(2)(c)625000after2025 indexing and rounding. Read 2026-11-14.
- [G07] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-251.1.html). Read for ITA251.1(1)–(3) affiliation/control and opening(4); not every trust interpretation. Read 2026-11-14.
- [G08] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-53.html). Read for ITA53(1)(a),(f), relevant(2)(h) trust-unit adjustments and neighbors; not wholeACB statute. Read 2026-11-14.
- [G09] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html). Read for ITA47 all operative(1)–(3), identical property averaging, debt and employee exceptions. Read 2026-11-14.
- [G10] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-46.html). Read for ITA46 all operative(1)–(5),1000floor/partial/set/gifting qualifications. Read 2026-11-14.
- [G11] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-41.html). Read for ITA41 all operative(1)–(3), LPP-only net gain and3/7year ordering. Read 2026-11-14.
- [G12] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-39.html). Read for ITA39(1)(a)–(c) capital/business exclusions, depreciable loss and ABIL predicates; no fullABIL reductions. Read 2026-11-14.
- [G13] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html). Read for ITA12(12)–(14), full flipping housing/right definition, all9events and nil business loss. Read 2026-11-14.
- [G14] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-45.html). Read for ITA45 all operative(1)–(4), full/partial use and elections/deadline/CCA. Read 2026-11-14.
- [G15] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.1.html). Read for ITA54.1 all operative(1)–(2), specific employer-relocation four-year relief. Read 2026-11-14.
- [G16] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html). Read for ITA220(3.2),(3.21),(3.3)–(3.7), late designation/application period and lesser-of penalty. Read 2026-11-14.
- [G17] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html). Read for ITA150(1) deadlines and relevant(1.1) resident disposition filing; not complete estate return engine. Read 2026-11-14.
- [G18] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html). Read for CRAindexation table LCGE/deduction2026/2025 and relevant2024/2023 historical rows; not unrelated credits. Read 2026-11-14.
- [G19] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html). Read for T4037 actual2025 bounded gain/outlay/CAD FX, gifts, calendar-year, identical property/T3/splits, inheritance, reserves, ordinary/LPP/superficial losses and relevant QSBC/PRE; not whole guide. Read 2026-11-14.
- [G20] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html). Read for PRE folio relevant qualification/family/land,2.15–2.23 formula and2.48–2.64 elections/CCA/ancillary;2.73–2.78 cross-border boundary; no fulltrust engine. Read 2026-11-14.
- [G21] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html). Read for CRA capital losses operative general/old rate/carryback/oldest/pre1986/LPP/superficial; other farming/ABIL only bounded referral. Read 2026-11-14.
- [G22] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25300-net-capital-losses-other-years.html). Read for CRA25300 whole operative prior-loss claim, oldestrate and pre1986agreement exception. Read 2026-11-14.
- [G23] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25400-capital-gains-deduction.html). Read for CRA25400 whole operative2025claim/referral/history; stale proposed and inconsistent historical values reconciled toAct/T657. Read 2026-11-14.
- [G26] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s3/5000-s3-25e.pdf). Read for actual2025 Schedule3 all4pages: flipped/PRE/disposition rows/slips/reserves/ordinary and special inclusion;page2 rendered. Read 2026-11-14.
- [G27] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1a/t1a-25e.pdf). Read for actual2025 T1A opening and completeParts5–7 capital/LPPcarryback, remaining balances/certification; other loss parts not certified. Read 2026-11-14.
- [G28] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t936/t936-25e.pdf). Read for actual2025 T936 all4pages Parts1–3 and ChartA, current/prior totals and old-loss adjustment; prior2024mapnotcertified. Read 2026-11-14.
- [G29] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t657/t657-25e.pdf). Read for actual2025 T657 pages1–5 and22–27, annual/cumulative limits/current and2024historical charts/history; not all2016–2023charts;page3rendered. Read 2026-11-14.
- [G30] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2091ind/t2091ind-25e.pdf). Read for actual2025 T2091IND all4pages same-dayCGTread reused;Section1page2 re-read/rendered;1994worksheet not separately certified. Read 2026-11-14.
- [G33] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html). Read for CRA current important-dates page complete operative2025filing/payment and death qualification; not final2026annualpackage. Read 2026-11-14.
- [G35] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/whats-new-corporations.html). Read for Currentcorporatepage opening and exact whole-text absence check for old cancellation quotation; no other corporate law audit. Read 2026-11-14.
- [G34] [Official source](https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2025/update-cra-administration-proposed-capital-gains-taxation-changes.html). Read for dated31January2025 administration statement; historicalproposal only not operative2026rate. Read 2026-11-14.
- [G36] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-69.html). Read for ITA69(1) ordinary gift/nonarmFMV and express-overrides boundary; adjacent notfullrollover. Read 2026-11-14.
- [G37] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-70.html). Read for ITA70(5)(a)–(d) ordinary death deemed disposition/acquisition, not allspouse/farm rollover engine. Read 2026-11-14.
- [G38] [Official source](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html). Read for CRA published2027business/selfemployed deadlines, ordinaryT1balance/date andtaxshelterexception. Read 2026-11-14.
- [G39] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-257.html). Read for ITA257 wholeoperative negativealgebraicformula=nil. Read 2026-11-14.
- [G40] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t5008.html). Read for actualT5008catalogue edition2026/PDFlink verified, not automatic annualreturnedition availability. Read 2026-11-14.
- [G41] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t5008/t5008-26b.pdf). Read for actual2026 T5008 firstpagefieldlabels/edition, bilingual duplicates not individually certified. Read 2026-11-14.
- [G42] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4091/t5008-guide-return-securities-transactions.html). Read for T4091 operativeboxes13–21 currency/settlementdate/quantity/security/costgrossproceeds; not alldealerfilingguide. Read 2026-11-14.
- [G43] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t5-slips/t5008-statement-securities-transactions-slip-information-individuals.html). Read for individualT5008 wholeoperativebusinesscapital andbox20ACB warning. Read 2026-11-14.
- [G44] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2017/t2017-25e.pdf). Read for actual2025 T2017 all3pages category/history/67060/caps/prior-ceiling;page3rendered. Read 2026-11-14.
- [G45] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1170/t1170-25e.pdf). Read for actual2025 T1170 all2pages eligibleadvantage/zeroordinary/flowthrough/exchange/destinations andAMThandoff. Read 2026-11-14.
- [G46] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t691/t691-25e.pdf). Read for actual2025 T691 openingpage1 purpose/exceptions and boundedcapital-gift handoff; no whole10page/2026AMTengine. Read 2026-11-14.
- [G47] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.2.html). Read for ITA38.2 wholeoperative giftadvantage/proration. Read 2026-11-14.
- [G48] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html). Read for ITA248 relevant eligible-relocation andsmall-business-corporation definitions; not entire248. Read 2026-11-14.

Not yet confirmed: the final2026 annual Schedule3/T657/T936/T2091/T1A/T2017/T1170/T691 package and its field changes. The actual2025 editions below support the explicitly dated2025 workflow, not a claim that2026 annual field numbers are final. The2026 T5008 edition is separately available. A guessedRC4268 URL returned404 and is not used as evidence. No complete QFFP eligibility, AMT, intergenerational-transfer, provincial or estate engine is provided; retain the referrals and actual unresolved inputs.
