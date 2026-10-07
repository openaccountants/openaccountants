---
name: ca-capital-gains
description: "Canada capital gains tax: inclusion rate (50% / 2/3 above $250k from 2024), lifetime capital gains exemption (LCGE), principal residence exemption, adjusted cost base. Trigger on: \"Canada capital gains tax\", \"CRA capital gains\", \"inclusion rate Canada\", \"sell shares Canada\", \"T5008\", \"adjusted cost base Canada\", \"LCGE Canada\", \"principal residence exemption Canada\", \"capital gains inclusion rate 2/3\", \"sell small business shares Canada\". For non-residents see ca-nonresident-cgt."
version: 1.0
jurisdiction: CA
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada: capital gains for individuals (inclusion rate, ACB, principal residence, lifetime exemption, losses, Schedule 3)

## Scope and who this is for ([CRA Guide T4037, Capital Gains](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html))

This Guide covers **federal** income tax on capital gains and capital losses of an **individual resident in Canada** who sells, or is considered to have sold, capital property: shares and fund units, real estate, a home or cottage, personal-use property and qualifying small business or farm and fishing property.

Primary year: **tax year 2026** (calendar year, 1 January to 31 December 2026). A short section near the end covers the **2025** returns that were due in 2026. Where a rule is unchanged between 2025 and 2026 the Guide says so.

It covers:

- the inclusion rate (the share of a gain that is taxed) and the status of the cancelled increase;
- proceeds, adjusted cost base (ACB), outlays and expenses, and average cost for identical shares;
- the principal residence exemption, the designation, the "plus 1" year and reporting on Form T2091(IND);
- the residential property flipping rule (homes held for less than 365 days);
- the lifetime capital gains exemption (LCGE) for qualified small business corporation shares and qualified farm or fishing property, claimed as the capital gains deduction;
- capital losses, net capital losses, superficial losses, personal-use and listed personal property;
- the capital gains reserve;
- reporting on Schedule 3, line 12700, line 25300 and line 25400, and the filing dates.

**Not covered here:** non-residents selling Canadian property (see the **ca-nonresident-cgt** Guide), departure tax on leaving Canada and residency questions (see **ca-tax-residency**), corporations and trusts, provincial and territorial tax rates, Quebec's separate provincial return, and whether a sale is business income rather than a capital gain outside the flipping rule. Provincial and territorial tax also applies to the same taxable capital gain, but the rates are outside this Guide.

Law: the *Income Tax Act* (ITA), mainly [s.38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) (taxable capital gain), [s.40](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) (gains, losses, reserve, principal residence formula), [s.54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) (definitions), [s.110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html) (capital gains deduction) and [s.111](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html) (loss carryovers). The Justice Laws copies used were current to 3 September 2026.

## Ask the client first

- **Were you resident in Canada for the whole year of sale?** The LCGE needs residence throughout the year (CRA also accepts residence for part of the year plus the whole of the year before or after). A non-resident needs a different Guide.
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

1. **Confirm it is a capital disposition.** A sale, a gift, or a deemed sale all count. Check the flipping rule first for any Canadian housing unit held for less than 365 days; if it applies, the gain is business income and this Guide stops for that property.
2. **Find the year.** Report the disposition in the calendar year you sold or were considered to have sold the property, even if your business has a different fiscal year end.
3. **Work out proceeds, ACB and outlays in Canadian dollars.** Capital gain or loss = proceeds − (ACB + outlays and expenses).
4. **Apply special rules to the gain or loss:** principal residence exemption, personal-use property floor, listed personal property, superficial loss, and the reserve if you are paid over time.
5. **Apply the inclusion rate.** For 2026 (and 2025), the taxable capital gain or allowable capital loss is one-half of the capital gain or loss (ITA s.38(a)).
6. **Net the year.** Allowable capital losses of the year offset taxable capital gains of the year. A positive balance goes on **line 12700**. A negative balance becomes part of the net capital loss: keep it for later years or carry it back on Form T1A.
7. **Apply losses from other years** on **line 25300**, only against taxable capital gains, oldest loss first.
8. **Claim the capital gains deduction** on **line 25400** for eligible QSBC shares or qualified farm or fishing property, using Form T657 (and Form T936 for the cumulative net investment loss, CNIL).
9. **Report** on Schedule 3 (and Form T2091(IND) for a home), file by the deadline and pay any balance by 30 April of the next year.

## Key figures, with the year each applies to

| Item | Tax year 2026 | Tax year 2025 | Source |
| --- | --- | --- | --- |
| Inclusion rate (individuals) | one-half of the gain (ITA s.38(a), text current to 3 Sep 2026) | 50% ("The inclusion rate for 2025 is 50%") | [ITA s.38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html); [CRA capital losses](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| LCGE (QSBC shares, qualified farm or fishing property) | $1,275,000 of gains | $1,250,000 of gains | [CRA indexation table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| Capital gains deduction limit (half the LCGE, line 25400) | $637,500 | $625,000 | same CRA table |
| Personal-use property: minimum ACB and minimum proceeds | $1,000 | $1,000 | [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html) |
| Flipping rule holding period | less than 365 consecutive days | same | [ITA s.12(13)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html) |
| Superficial loss window | 30 days before to 30 days after the sale | same | [ITA s.54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) |
| Net capital loss carryback / carryforward | 3 years back, no limit forward | same | [CRA capital losses](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Listed personal property loss | 3 years back, 7 years forward, LPP gains only | same | same |
| Reserve (proceeds paid over time) | gain spread over up to 5 years; up to 10 years for certain transfers to a child | same | [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA s.40(1.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) |
| Late principal residence designation penalty | lesser of $8,000 and $100 per complete month late | same | [ITA s.220(3.5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html) |

### The inclusion rate: one-half, and the increase that did not happen ([ITA s.38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html))

- The enacted rule is ITA s.38(a): a taxable capital gain "is ½ of the taxpayer’s capital gain". The Justice Laws text used is current to 3 September 2026, so this is the rule for 2026 dispositions.
- Budget 2024 proposed raising the rate to two-thirds for an individual's gains above $250,000 a year. On 31 January 2025 the start was deferred to 1 January 2026, and CRA "reverted to administering the currently enacted capital gains inclusion rate of one-half" ([CRA, January 2025](https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2025/update-cra-administration-proposed-capital-gains-taxation-changes.html)).
- CRA now records that "It was later announced that this proposed increase was cancelled" ([CRA, What's new for corporations](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/whats-new-corporations.html)).
- So: no two-thirds rate, no annual threshold, and no split-period calculation for 2024, 2025 or 2026. Any older working paper or software note that splits 2024 into periods for the inclusion rate is out of date. (The LCGE did change part way through 2024; see the 2025 section.)
- Older net capital losses were incurred at other rates (for example 3/4 from 1990 to 1999). When you apply them to a year taxed at one-half, you adjust them using the CRA worksheet charts for line 25300.

## Proceeds, ACB and outlays ([T4037, Chapter 1 and Chapter 3](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html))

- **Proceeds of disposition** are usually the sale price; they can also be compensation for property destroyed, expropriated or stolen.
- **Adjusted cost base (ACB)** is usually the cost of the property plus expenses to acquire it (commissions, legal fees) and capital expenditures such as additions and improvements. Current expenses such as maintenance and repairs are **not** added.
- **Outlays and expenses** are the costs of selling: fixing-up expenses, finders' fees, commissions, brokers' fees, surveyors' fees, legal fees, transfer taxes and advertising. They reduce the gain only; they cannot be deducted from other income.
- **Capital gain = proceeds − ACB − outlays and expenses.** A negative result is a capital loss.
- **Identical properties** (shares of the same class of one company, units of one mutual fund trust): use the **average cost**. Recalculate the average after each purchase by dividing the total cost of the identical properties bought (including acquisition costs) by the number held. A sale does not change the average cost of the units left.
- **Mutual fund trust units:** T3 box 42 changes the ACB. A negative box 42 amount is added to the ACB; a positive amount is subtracted. If the ACB goes below zero, the negative amount is a capital gain in that year.
- **Stock splits and consolidations** do not change the total ACB; they change the ACB per share.
- **Foreign currency:** convert proceeds at the exchange rate at the time of sale, the ACB at the rate when the property was acquired, and each expense at the rate when it was incurred.
- **Gifted property:** you are generally considered to have acquired it at its fair market value (FMV) on the date you received it. **Inherited property:** your cost is generally the deceased person's deemed proceeds, usually the FMV right before death; property from a deceased spouse or common-law partner, and farm property or a woodlot passing to a child, may be treated differently.
- **Records:** keep purchase and sale records, and a record of the FMV on the date you inherit property, receive it as a gift, or change its use.
- **Slips:** brokers issue a T5008 slip or an account statement for securities sold. Rebuild the ACB from the client's own purchase records rather than relying on a slip alone.

## Principal residence exemption ([CRA: Principal residence](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/principal-residence-other-real-estate.html); [Folio S1-F3-C2](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html))

**What can qualify.** A house, cottage, condominium, apartment, duplex unit, trailer, mobile home or houseboat, a leasehold interest in one, or a co-operative housing share bought only to get the right to live in a unit. It qualifies for a year only if **all** of these hold:

- you own it, alone or jointly;
- you, your current or former spouse or common-law partner, or one of your children **ordinarily inhabited** it at some time in the year;
- you **designate** it as your principal residence for that year.

**Land.** The land under and around the home can be included, usually up to **half a hectare**. More land counts only if you can show it is needed for the use and enjoyment of the home (for example, a municipal minimum lot size).

**One home per family unit per year (1982 and later).** For 1993 and later years the family unit is: you; a person who was your spouse or common-law partner throughout the year (unless you were separated all year under a court order or written agreement); and your children, other than a child who had a spouse or common-law partner during the year or was 18 or older during the year. If you had no spouse or partner and were under 18 all year, your parents and unmarried siblings under 18 are also in the unit. So a couple with a house and a cottage can shelter only one of them for any given year.

**The exemption formula (ITA s.40(2)(b)).** Exempt part of the gain = gain × (1 + number of years after the acquisition date for which the property was designated and you were resident in Canada) ÷ (number of years after the acquisition date that you owned it). The formula counts tax years ending after the acquisition date, so the year of purchase is counted in ownership years.

- The **"plus 1"** lets you treat both the old and the new home as sheltered in the year you sell one and buy the other, even though only one can be designated for that year.
- The "plus 1" is **only available if you were resident in Canada in the year you acquired the home.** If you were non-resident throughout that year, you do not get the extra year.
- The exemption is also limited to years you were **resident in Canada**. If the client was non-resident for any part of the ownership, refer or see the ca-nonresident-cgt Guide.

**You must report the sale.** For 2016 and later years, CRA only allows the principal residence exemption if you **report the disposition and the designation** on your return.

- Report on **Schedule 3** (Part 1, line 17900 designation box) and **Form T2091(IND)**, *Designation of a Property as a Principal Residence by an Individual (Other Than a Personal Trust)*.
- Complete only **page 1** of T2091(IND) if the home was your principal residence for every year you owned it, or every year except one. Otherwise complete the full form and report the part of the gain for the years not designated.
- Sold more than one former home in the same year: a separate T2091(IND) for each.
- **Forgot to designate?** Ask CRA to amend the return. CRA can accept a late designation, but a principal residence designation is treated as an election (ITA s.220(3.21)(a.1)), and the late-election penalty is the **lesser of $8,000 and $100 for each complete month** from the original due date to the date the request is made (ITA s.220(3.5)).

**A loss on a home is not deductible.** A home is personal-use property, so a loss on its sale cannot be claimed.

**Partly used to earn income.** If only part of the home qualifies, split the selling price and ACB between the home part and the income part on a reasonable basis (square metres or number of rooms), and report the gain on the income part. The whole property keeps its principal residence status if the income use is ancillary to the home use, there is no structural change, and no capital cost allowance is claimed (for example, a home day care).

**Change of use.** Converting a home fully to a rental is a deemed sale at fair market value (ITA s.45(1)(a)). You can instead elect under **s.45(2)** (a signed letter filed with the return for the year of the change) to be treated as not having changed use; the property can then stay designated for **up to four tax years** while rented, as long as you are resident in Canada and no capital cost allowance is claimed. A **s.45(3)** election works the other way (rental turned into a home), again for up to four earlier years, and is not available if CCA was claimed after 1984. The four-year limit can be lifted in some employer-relocation cases (s.54.1). Refer if the client already claimed CCA or has mixed-use years.

## Flipped homes: the 365-day rule ([ITA s.12(12)-(13)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html))

- A **housing unit in Canada** (including a rental property), or a right to acquire one, that you owned or held for **less than 365 consecutive days** before selling it is a **flipped property**. The gain is **business income**, not a capital gain. It is fully taxed, the principal residence exemption does not apply, and a business loss on a flipped property is **deemed nil**.
- The rule applies to residential properties sold on or after 1 January 2023 (Folio S1-F3-C2, ¶2.6.1). It does not apply to property that is already inventory (that is business income anyway).
- **Exception: life events.** The rule does not apply if the sale can reasonably be considered to occur because of, or in anticipation of:
  - the death of the taxpayer or a related person;
  - a related person joining the household, or the taxpayer joining a related person's household (marriage or partnership, birth, adoption, care of an elderly parent);
  - breakdown of a marriage or common-law partnership, where the couple had lived separate and apart for **at least 90 days** before the sale;
  - a threat to the personal safety of the taxpayer or a related person;
  - a serious disability or illness of the taxpayer or a related person;
  - an eligible relocation where the new home is **at least 40 kilometres** closer to the new work or school location;
  - involuntary termination of employment of the taxpayer or spouse or common-law partner;
  - insolvency of the taxpayer;
  - destruction or expropriation of the property.
- If the home is **not** a flipped property, it can still be business income on general principles (for example, a pattern of buying to resell). If treated as business income, report on Form T2125; if a capital gain, on Schedule 3. That judgment is outside this Guide: refer when facts point to trading.

## Lifetime capital gains exemption and the capital gains deduction ([CRA line 25400](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25400-capital-gains-deduction.html); [ITA s.110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html))

The LCGE is a limit on **gains**; the deduction on line 25400 is the matching limit on **taxable** gains (half, because only half of a gain is taxable).

| Year | LCGE (gains) | Deduction limit (line 25400) |
| --- | --- | --- |
| 2026 | $1,275,000 | $637,500 |
| 2025 | $1,250,000 | $625,000 |

- **2026 is the first indexed year** after the increase: CRA's indexation table shows the 2026 exemption limit of $1,275,000 and a deduction limit of $637,500. The Act (s.110.6(2) and (2.1), text current to 3 September 2026) states the deduction as $625,000; CRA's table gives the indexed 2026 figure.
- The same limit covers **qualified small business corporation (QSBC) shares** and **qualified farm or fishing property (QFFP)**. It is one **cumulative lifetime** limit shared across both: deductions already claimed in earlier years reduce what is left.

**Who can claim.** An individual (not a trust) who:

- was **resident in Canada throughout the year** of the claim (CRA also treats you as resident throughout the year if you were resident for part of it and throughout the year before or the year after; factual and deemed residents count);
- has gains that qualify; and
- has deduction room left.

**What gains qualify.** Taxable capital gains from dispositions of QSBC shares or QFFP; a reserve brought into income from such a disposition; and such gains allocated and designated to you by a trust.

**QSBC share: all three tests** ([T4037, Definitions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)):

1. **At the time of sale** it is a share of a **small business corporation**: a Canadian-controlled private corporation (CCPC) where **all or most (90% or more)** of the fair market value of the assets are used mainly in an active business carried on primarily in Canada (by it or a related corporation), or are shares or debts of connected small business corporations, or a mix.
2. **Holding period:** throughout the **24 months** immediately before the sale, no one owned the share other than you, a partnership of which you were a member, or a person related to you. Shares issued from treasury after 13 June 1988 are treated as if an unrelated person owned them just before issue, so newly issued shares can fail this test.
3. **Asset test over the 24 months:** throughout that period, while owned by you, your partnership or a related person, it was a share of a CCPC with **more than 50%** of the fair market value of its assets used mainly in an active business carried on primarily in Canada, or in qualifying shares or debts of connected corporations, or a mix.

**How to claim.**

- Complete **Form T657**, *Calculation of Capital Gains Deduction*, and claim on **line 25400**. You may claim any amount up to the maximum you calculate.
- If you had investment income or investment expenses in any year from 1988 on, complete **Form T936** for the **cumulative net investment loss (CNIL)**. A CNIL balance reduces the deduction available in the year.
- **Allowable business investment losses** and **net capital losses of other years deducted on line 25300** reduce the "annual gains limit" in s.110.6(1), and through it the "cumulative gains limit", so they reduce the deduction available.
- Report QSBC share dispositions on **line 1** of Part 3 of Schedule 3 and QFFP on **line 2**.
- A reserve brought into income later uses the deduction rules for the year of the original disposition.
- Large gains and deductions can trigger the **alternative minimum tax**; CRA notes the AMT calculation changed for 2024 and later years under proposed changes. Run Form T691 and refer if AMT applies.

Related reliefs **not** covered here, refer instead: the capital gains deduction for a qualifying business transfer to an employee ownership trust (line 25395), qualifying cooperative conversions, intergenerational business transfers (Form T2066), and the capital gains deferral for eligible small business investments.

## Capital losses ([CRA: Capital losses](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html); [line 25300](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25300-net-capital-losses-other-years.html))

- An **allowable capital loss** is the capital loss × the inclusion rate (one-half).
- Allowable capital losses of the year **must** first be applied against taxable capital gains of the same year. They **cannot** reduce other income (except the special pre-1986 balance and business investment losses, below).
- Any excess becomes part of the **net capital loss** for the year. It can be carried **back to any of the three previous years** or **forward to any future year**, but only against taxable capital gains.
- **Carryback:** complete Part 5 of **Form T1A**, *Request for Loss Carryback*, with the current return. Do **not** file an amended return for the earlier year. A 2026 net capital loss can go back to 2023, 2024 and 2025. A carryback can reduce a capital gains deduction claimed in that year or a later year.
- **Carryforward:** claim on **line 25300**. Apply older losses before newer ones and keep separate balances by year. Losses from years with a different inclusion rate must be adjusted to the current rate (CRA worksheet charts).
- Applying a net capital loss reduces **taxable income**, not **net income**, so income-tested credits and benefits do not change.
- **Pre-1986 losses** (incurred before 23 May 1985) can, after offsetting gains, reduce other income by up to the least of the excess, $2,000 and the pre-1986 balance.
- **Business investment loss:** a loss on an arm's length disposition of a share or debt of a small business corporation can instead be an **allowable business investment loss** deductible from other income on line 21700 (gross amount on line 21699). Refer for the reduction rules and the effect on the LCGE.

### Superficial loss ([ITA s.54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html); [s.40(2)(g)(i)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html))

A loss is **superficial**, and is **denied**, when **both** of these hold:

1. you, or a person **affiliated** with you, buys (or gets a right to buy) the same or an **identical** property during the period that starts **30 days before** and ends **30 days after** the sale; and
2. at the **end** of that period, you or the affiliated person still owns (or has a right to buy) that substituted property.

- Affiliated persons include you and your spouse or common-law partner; you and a corporation controlled by you or your spouse or partner; a partnership and its majority-interest partner; a trust and its majority-interest beneficiary.
- **The loss is not lost if you are the buyer:** add the denied loss to the ACB of the substituted property. It reduces the gain, or increases the loss, when that property is later sold. If an affiliated person (your spouse or partner, or your corporation) bought the substituted property, refer: the adjustment is not simply added to your own ACB.
- **Common exceptions** (not superficial): deemed sales on becoming or ceasing to be resident, on a change of use, or on death; the expiry of an option; property appropriated by a shareholder on a winding-up; becoming or ceasing to be tax-exempt within 30 days after the sale.
- Buying back inside the taxpayer's RRSP, TFSA or other registered plan: refer.

### Personal-use and listed personal property ([T4037, lines 9 and 10](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html))

- **Personal-use property** (car, boat, furniture, a cottage used by the family): if the ACB is under $1,000, use $1,000; if the proceeds are under $1,000, use $1,000. If both are $1,000 or less, there is no gain or loss and nothing to report. **Losses on personal-use property are not deductible** (other than listed personal property).
- **Listed personal property (LPP)** is personal-use property that usually rises in value: prints, etchings, drawings, paintings, sculptures or similar works of art, jewellery, rare folios, manuscripts or books, stamps and coins (including interests in them). LPP losses offset only LPP gains, in the year or the **three years before or seven years after**. Carry back on Form T1A.

## Capital gains reserve: paid over several years ([T4037, Claiming a reserve](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA s.40(1)(a)(iii), (1.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html))

- If part of the sale price is payable after the end of the year, you may deduct a **reserve** so the gain is taxed as the money comes in. Calculate the full gain first, then deduct the reserve.
- The reserve is limited: you must bring in at least one-fifth of the gain each year, so the whole gain is taxed over **five years** (four years of reserve). For transfers to your **child** of family farm or fishing property or QSBC shares (and for qualifying business transfers and intergenerational business transfers), the period is **ten years** (nine years of reserve); in the statute the fractions become one-tenth and nine.
- Claim on **Form T2017**, *Summary of Reserves on Dispositions of Capital Property*, each year.
- **No reserve** if at the end of the year, or at any time in the next year, you were **not resident in Canada** or were exempt from tax, or if you sold the property to a corporation that you control in any way.
- For QSBC shares or QFFP, a reserve brought back into income uses the capital gains deduction rules of the year of the original sale.

## Boundaries and exceptions ([T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html))

| Situation | Treatment | Source |
| --- | --- | --- |
| Home owned less than 365 consecutive days, no listed life event | Business income, fully taxed; no principal residence exemption; loss deemed nil | ITA s.12(12)-(13) |
| Home owned 365 days or more, or life event applies | Normal capital gain rules; principal residence exemption available | CRA principal residence page |
| Home was principal residence every year owned (resident throughout) | Gain fully sheltered, but sale must still be reported (Schedule 3 and T2091(IND) page 1) | CRA principal residence page |
| Two homes in the family unit | Only one can be designated per year for the whole family unit; choose the years per property | ITA s.54 "principal residence" (c) |
| Owner not resident in Canada in the year the home was bought | No "plus 1" year | ITA s.40(2)(b), variable B |
| Loss on a home, car, boat or other personal-use property | Not deductible | T4037 |
| Personal-use item with ACB and proceeds both $1,000 or less | No gain or loss; do not report | T4037 |
| Loss on shares, same shares bought back within 30 days before or after and still held 30 days after | Superficial loss denied; add to ACB of the new shares | ITA s.54; CRA capital losses |
| Same, but repurchase is 31 or more days after the sale and not in the 30 days before | Loss allowed | ITA s.54 |
| Loss sale then repurchase by spouse or own corporation | Superficial loss (affiliated person); refer for the ACB adjustment | ITA s.54 |
| Gift of listed shares or mutual fund units to a qualified donee | Inclusion rate of zero; report on Form T1170 | ITA s.38(a.1); T4037 |
| QSBC shares held less than 24 months by you or related persons (including new treasury shares) | Generally fails the holding-period test; no LCGE | T4037 definition |
| CCPC with less than 90% active business assets at the time of sale | Not a small business corporation share at sale; no LCGE unless assets are purified first (refer) | T4037 definition |
| Seller not resident in Canada throughout the year | No capital gains deduction (subject to CRA's part-year rule); no reserve | CRA line 25400; T4037 |
| Net capital loss vs employment or business income | Cannot be used (other than the pre-1986 balance up to $2,000 or an ABIL) | CRA capital losses |
| Sale proceeds received over time | Reserve over up to five years (ten for certain transfers to a child) | T4037; ITA s.40 |

## Worked cases ([T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA s.38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html))

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
- If instead the client had waited and bought back on 15 April 2026 (more than 30 days after, and nothing bought in the 30 days before), the loss would be allowed: allowable capital loss $1,000.

**C3. Cottage and city home in one family (principal residence formula).**
A couple owns a city home (bought 2008) and a cottage the husband bought in 2017 for $300,000. The cottage is sold in 2026 for $700,000 with $20,000 of selling costs. Both were ordinarily inhabited by the family every year; both spouses were resident in Canada throughout. They decide to designate the cottage for 4 years (2023 to 2026) and keep the other years for the city home.
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
- Check alternative minimum tax on Form T691 before finalising; a large deduction can trigger it.

**C5. Condo sold after nine months (flipping rule).**
Bought 1 February 2026 for $500,000, sold 1 November 2026 for $560,000, selling costs $10,000. No listed life event.
- Owned less than 365 consecutive days, so it is a flipped property.
- Profit $50,000 is **business income** (Form T2125), fully included; no inclusion rate, no principal residence exemption.
- If the sale was because of a job move where the new home is at least 40 km closer to the new workplace, the flipping rule does not apply and the normal rules (capital gain, possible principal residence exemption) are used instead, subject to the general business-income question.

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

- the client was **not resident in Canada** for the whole year, arrived or left in the year, or was non-resident while owning a home (departure tax, part-year rules, no "plus 1");
- a home was **rented, used for business, or had CCA claimed**, or a s.45(2) or s.45(3) election is in play or was missed;
- a home sale may be **business income** on general principles (repeat buying and selling, building to sell), even if held 365 days or more;
- an **LCGE claim** on private company shares or farm or fishing property: the 24-month and asset tests, purification, CNIL, ABIL history, and **alternative minimum tax** all need a full calculation;
- a **qualifying business transfer**, **intergenerational business transfer**, cooperative conversion or small business investment deferral is proposed (several are described by CRA as "proposed changes");
- a **superficial loss** involving a spouse, corporation, trust or registered plan;
- **trusts, estates, partnerships** or corporations are the seller, or a sale or rollover to a related or controlled corporation;
- **crypto-assets**, options, short sales or frequent trading where the income may be business income;
- a **late principal residence designation** or amended return is needed and the penalty may apply;
- a sale by a **non-resident** of Canadian property: use the ca-nonresident-cgt Guide.

Refuse to give a figure when the purchase cost, dates or ownership history cannot be established; ask for the records instead of estimating.

## Returns being filed now: tax year 2025 (dated section) ([CRA line 25400](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25400-capital-gains-deduction.html))

- 2025 returns were due **30 April 2026**, or **15 June 2026** if the individual or their spouse or common-law partner was self-employed; any balance was payable by **30 April 2026** in both cases ([CRA important dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html)). Late 2025 returns and adjustments still use these rules.
- Inclusion rate for 2025: one-half ("The inclusion rate for 2025 is 50%").
- LCGE for 2025: $1,250,000, deduction limit $625,000 (not indexed for 2025). For 2024 the limit changed mid-year (a lower limit before 25 June 2024 and $1,250,000 from 25 June 2024); Form T657 has separate charts. Refer if a 2024 reserve, partnership or trust allocation straddles that date.
- A 2025 net capital loss can be carried back to 2022, 2023 and 2024 on Form T1A.
- CRA's 2025 pages still describe the LCGE increase and some related measures as "proposed changes"; the Justice Laws text of s.110.6 (current to 3 September 2026) now contains the $625,000 deduction figure.

## Filing and payment

- **Report every disposition in the calendar year of sale** on **Schedule 3**, *Capital Gains or Losses*, attached to the T1 return, even if no tax is payable. The taxable capital gain goes on **line 12700**.
- Home sales: **Schedule 3** designation (line 17900) and **Form T2091(IND)**.
- Capital gains deduction: **Form T657**, **Form T936**, **line 25400**.
- Net capital losses of other years: **line 25300**. Carryback: **Form T1A**.
- Reserve: **Form T2017**. Gifts of securities: **Form T1170**.
- **2026 return:** due **30 April 2027**, or **15 June 2027** if the individual carried on a business in 2026 or their cohabiting spouse or common-law partner did ([ITA s.150(1)(d)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html): "the following April 30", "the following June 15"); the balance owing is still due **30 April 2027**, as CRA states for 2025. Confirm on CRA's important dates page when it updates for 2026.

## Completion checklist

- [ ] Residence in Canada confirmed for the whole year (and for the LCGE test and the "plus 1" year).
- [ ] Each disposition: date, proceeds, ACB (rebuilt from records, average cost for identical property), outlays, currency conversion.
- [ ] Flipping rule checked for every Canadian housing unit held less than 365 days; life event documented if relied on.
- [ ] Principal residence: years owned, years designated, family unit's other homes, Schedule 3 designation box and T2091(IND) completed.
- [ ] Superficial loss window (30 days before and after) checked for every loss, including spouse and own corporation.
- [ ] Personal-use property floor and LPP rules applied; no personal-use losses claimed.
- [ ] Inclusion rate of one-half applied; no two-thirds or split-period calculation.
- [ ] LCGE: QSBC or QFFP tests documented; prior deductions, CNIL (T936), ABIL and line 25300 claims taken into account; 2026 limit used; AMT checked (T691).
- [ ] Net capital loss balances by year updated; carryback on T1A if chosen.
- [ ] Reserve on T2017 if proceeds are paid over time.
- [ ] Return filed and balance paid by the dates above.

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
