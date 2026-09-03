---
name: ring-fencing-of-assessed-losses-under-section-20a
description: From 1 March 2026 section 20A bites from the 39% marginal rate, not 45% — the threshold roughly halves and a geared residential rental becomes ring-fenced by default.
jurisdiction: ZA
last_updated: 2026-09-02
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ring-fencing of Assessed Losses under Section 20A

## South Africa — Ring-fencing of Assessed Losses, s 20A

> **What changed, and why this file exists.** For years of assessment commencing on or
> after **1 March 2026**, s 20A bites from the **39%** marginal rate, not the 45% maximum
> marginal rate. The threshold roughly halves. Ring-fencing stops being a
> high-income edge case and becomes the **default** for a geared residential rental held
> by a reasonably paid employee.

## Section 1 — Scope

This file covers **s 20A ring-fencing for natural persons**, and enough of **s 20** to
place it.

Not covered: assessed losses of trusts; the s 20(1)(a) company rules beyond the summary in
Section 6; capital losses, which are an Eighth Schedule matter and not assessed losses at
all.

## Section 2 — The two-stage test

- **Two-stage test — both stages must be met** — Ring-fencing under s 20A applies only where **both** stages are met. **Stage 1 — the income test.** The taxpayer's taxable income, *before* setting off the loss in question, equals or exceeds the amount at which the relevant marginal rate begins. **Stage 2 — the trade test.** Either - the trade is a **listed suspect trade** (Section 4), **or** - the trade has made an assessed loss in **at least three of the last five** years of assessment, counting the current year. If stage 1 fails, s 20A does not apply at all, whatever the trade. If stage 1 is met, a listed suspect trade is caught **immediately** — it never needs the three-in-five test.  _(Income Tax Act 58 of 1962 s 20A(2).)_

## Section 3 — The income threshold, by year of assessment ([SARS, Rates of Tax for Individuals](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))

**The income threshold, by year of assessment**  _([Income Tax Act 58 of 1962 s 20A(2)(a), as amended with effect for years of assessment commencing on or after 1 March 2026; SARS Rates of Tax for Individuals for the bracket floors.](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Year of assessment | Rate the threshold keys off | Taxable income threshold |
| --- | --- | --- |
| 2023 (2022/23) | 45% — maximum marginal rate | R1,731,600 |
| 2024 (2023/24) | 45% — maximum marginal rate | R1,817,000 |
| 2025 (2024/25) | 45% — maximum marginal rate | R1,817,000 |
| 2026 (2025/26) | 45% — maximum marginal rate | R1,817,000 |
| **2027 (2026/27)** | **39%** | **R695,800** |

## Section 3 — The income threshold, by year of assessment ([SARS, Rates of Tax for Individuals](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))

- **Threshold is not a fixed rand amount; common error of R673,000** — The threshold is **not a fixed rand amount**. It is defined by reference to a marginal rate, so it moves every year with the bracket table. **Do not hard-code the rand figure.** Read it off the bracket table for the year in question as the floor of the band carrying the relevant rate. See `za-income-tax-tables`. ⚠️ **A common error in commentary written during 2025** quotes the new threshold as **R673,000**. That was the 39% bracket floor for the *2026* year of assessment, current when the amendment was proposed. Because the amendment only takes effect for years of assessment commencing on or after 1 March 2026, the first year it applies is 2027, whose 39% floor is **R695,800**. Using R673,000 for 2027 is wrong.  _(Income Tax Act 58 of 1962 s 20A(2)(a), as amended with effect for years of assessment commencing on or after 1 March 2026; SARS Rates of Tax for Individuals for the bracket floors.)_

## Section 4 — The listed suspect trades

- **Listed suspect trades caught on the income test alone** — Under s 20A(2)(b), these are caught on the income test alone: - Any sport practised by the taxpayer or a relative - Any dealing in collectibles - **The rental of residential accommodation**, unless the letting exception in Section 5 applies - The rental of vehicles, aircraft or boats - Animal showing by the taxpayer or a relative - Farming or animal breeding, unless carried on on a full-time basis - Any form of performing or creative arts - Any form of gambling or betting - Any trade in respect of which a tax benefit scheme applies  _(Income Tax Act 58 of 1962 s 20A(2)(b).)_

## Section 5 — The escapes

- **The escapes — letting exception and reasonable prospect of profit** — A trade that is otherwise caught is **not** ring-fenced where one of these applies. **The letting exception — s 20A(2)(b)(iii).** Residential accommodation is not a suspect trade where **at least 80%** of the accommodation is used by persons who are **not relatives** of the taxpayer for **at least half** the year of assessment. Note both limbs: the 80% is about who occupies it, and the half-year is about duration. **Reasonable prospect of profit — s 20A(3).** The trade escapes if it constitutes a business with a reasonable prospect of deriving taxable income within a reasonable period, having regard to the s 20A(3) factors — among them the proportion of gross income to allowable deductions, the commercial manner in which the trade is carried on, the number of years of losses, the business plan, and whether assets are available for private use. This is a facts-and-evidence test, not an assertion. A business plan, arm's length pricing, separate banking and a credible route to profitability are what carry it.  _(Income Tax Act 58 of 1962 s 20A(2)(b)(iii), s 20A(3).)_

## Section 6 — Section 20, for context

- **Section 20 underlying carry-forward rules and company 80% cap** — Ring-fencing modifies an ordinary carry-forward. The underlying rules: - An assessed loss carries forward and may be set off against income from **any** trade, subject to s 20(2A), which requires the taxpayer to have carried on a trade in the year of set-off. - **Companies** are separately limited: for years of assessment commencing on or after 1 April 2022, the balance of assessed loss that may be set off is capped at the **greater of R1,000,000 and 80%** of taxable income before the set-off. **This 80% cap does not apply to natural persons.**  _(Income Tax Act 58 of 1962 s 20, s 20(2A).)_

## Section 7 — What ring-fencing actually does

- **Effect of ring-fencing** — A ring-fenced loss is **not disallowed**. It is quarantined: it may only be set off against income from **that same trade** in future years, not against salary, not against other trades. So the cash effect is a deferral, sometimes indefinite. A rental that never turns a taxable profit carries a ring-fenced loss forward permanently without ever relieving anything.

## Section 8 — Edge cases

- **Test the income threshold before anything else.** Below it, s 20A is irrelevant and no amount of suspect-trade analysis matters.
- **"Taxable income before the set-off"** is the measure — not gross income, not remuneration, and not taxable income after the loss.
- **A geared residential rental is now the standard case, not an exotic one.** A salaried taxpayer over the 39% threshold with a bonded rental producing an interest-driven loss is ring-fenced by default from 2026/27 unless the letting exception or s 20A(3) applies. Practitioners who learned this section when it began at 45% will misjudge it.
- **Relatives occupying the property** count against the 80% limb of the letting exception. Letting to a child at market rent still fails it.
- **Farming is caught only where it is not full-time.** Full-time farming falls outside the list, and has its own regime in the First Schedule.
- **The election is not annual.** Once ring-fenced, the loss stays ring-fenced to that trade until it is absorbed by profits of that trade.

## The method, step by step

1. **Compute taxable income before the loss set-off, and test it against the threshold for that year.** If it is below, s 20A does not apply and nothing else in this file matters. Doing the trade analysis first wastes the work.
2. **Use the threshold for the right year, read off that year's bracket table.** 45% for years of assessment up to 2026; 39% from 2027. It is not a fixed rand amount.
3. **Ask whether the trade is on the suspect list.** If it is, it is caught immediately — do not run the three-in-five test, which will give you a false negative.
4. **Only if it is not listed, apply the three-in-five test** across the current year and the four before it.
5. **Then test the escapes.** For residential letting, both limbs of the letting exception — 80% non-relative occupation and at least half the year. Otherwise s 20A(3), which is a facts-and-evidence test needing a business plan and a credible route to profit, not an assertion.
6. **Where the loss is ring-fenced, carry it forward against that trade.** It is quarantined, not disallowed. Writing it off loses relief the taxpayer is still entitled to.

**What breaks when the order is wrong.** Running the three-in-five test on a listed suspect trade concludes it is safe when it is caught. Testing the trade before the income threshold wastes effort on taxpayers the section never reaches. And treating a ring-fenced loss as forfeited throws away relief that survives indefinitely.

## Section 9 — Self-checks

1. **Threshold from the right year's bracket table.** Confirm the taxable income threshold is the floor of the band carrying the relevant rate for that year of assessment — not a figure carried over from a prior year, and not R673,000 for YoA 2027.
2. **Right rate for the right year.** 45% for years of assessment up to 2026; 39% from 2027. Applying 39% to a 2026 return, or 45% to a 2027 return, both give the wrong answer.
3. **Suspect trade first, three-in-five second.** If the trade is listed, the three-in-five test is irrelevant. Running it anyway produces a false negative.
4. **Both limbs of the letting exception.** 80% non-relative occupation **and** at least half the year. One without the other fails.
5. **Ring-fenced, not lost.** Confirm the loss is carried forward against that trade and not written off.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

## Sources

Income Tax Act 58 of 1962 s 20, s 20(2A), s 20A (s 20A(2), s 20A(2)(a), s 20A(2)(b), s 20A(2)(b)(iii), s 20A(3)), as amended with effect for years of assessment commencing on or after 1 March 2026. Threshold amounts are the bracket floors in SARS, Rates of Tax for Individuals — https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/

> Contributed by Brandon Iverach, SAIPA 18504 / SARS PR0025122.

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
