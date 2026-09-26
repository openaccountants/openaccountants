---
name: us-capital-gains
description: "US federal capital gains tax for residents: short-term vs long-term rates, 2025 0%/15%/20% LTCG brackets by filing status, 3.8% NIIT thresholds and Form 8960 computation, §1202 QSBS including post-OBBBA issuance-date rules, §1031 like-kind exchange, installment sales, wash sale rule, Schedule D, and state-tax caveats. Trigger on: \"US capital gains tax\", \"long-term capital gains US\", \"Schedule D\", \"LTCG rate US\", \"NIIT net investment income tax\", \"QSBS exclusion\", \"1031 exchange\", \"sell US shares tax\", \"US CGT resident\", \"capital loss carryforward US\". For non-residents see us-nonresident-cgt."
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

# US federal capital gains for resident individuals: 2026 method, with 2025 return notes

Figures are for tax year 2026 unless a line says 2025. The 2026 amounts come from Rev. Proc. 2025-32, the inflation adjustments issued after the One Big Beautiful Bill Act (P.L. 119-21). A separate section covers 2025 returns, which are due by October 15, 2026 if the taxpayer got an extension.

## Scope and who this is for

- **Covers:** US citizens and resident aliens who file Form 1040 and sell capital assets. That includes shares, funds, bonds, digital assets held as investments, collectibles, a main home and investment real estate. It covers the federal rate on the gain, the net investment income tax (NIIT), the loss limit, wash sales, the home-sale exclusion, like-kind exchanges and installment sales.
- **Does not cover:** nonresident aliens (see the `us-nonresident-cgt` Guide), estates and trusts, dealers and traders who elected mark-to-market, corporations, and the details of qualified small business stock (see the `us-section-1202-qsbs` Guide).
- **State tax is separate.** Most states have their own rules on capital gains. This Guide gives the federal answer only. Check the state's own rules before giving a combined figure.

## Ask the client first

- Which tax year was the asset sold in (2025 or 2026), and what is the filing status: single, married filing jointly, married filing separately, head of household or qualifying surviving spouse?
- What was the trade date of each purchase and sale? Was the asset bought, received as a gift, inherited, or received in a tax-free exchange?
- What is the basis? Get Forms 1099-B and 1099-DA, and ask whether the broker reported basis to the IRS. Ask for any adjustments, reinvested dividends, and gift or inheritance valuations.
- Is the asset a collectible (art, antiques, gems, metals, coins, stamps, alcoholic beverages), depreciated real property, qualified small business stock, or a digital asset?
- Were substantially identical shares bought in the 30 days before or after a loss sale? Check the client's IRA and Roth IRA, the spouse's accounts, and any corporation the client controls.
- For a home: the dates of ownership and of use as the main home in the last 5 years, any home sale in the last 2 years that used the exclusion, any rental or home-office depreciation, and any reason for an early sale (job move, health, unforeseen event).
- For real estate traded for other real estate: the transfer date, the identification date, the location of both properties, and whether a qualified intermediary held the proceeds.
- For a sale paid in installments: the payment schedule, the stated interest, whether the buyer is related, and any depreciation recapture.
- Estimate modified adjusted gross income (MAGI) and net investment income for the NIIT test. Also get any capital loss carryover from the prior-year Schedule D.

## The method, step by step

1. **Confirm it is a capital asset and a taxable disposition.** Losses on personal-use property, such as a car or a main home, are not deductible.
2. **Classify each sale as short-term or long-term.** Long-term means held more than 1 year; short-term means held 1 year or less. For listed securities, the holding period starts the day after the trade date of the purchase and ends on the trade date of the sale. Settlement dates do not count. Inherited property is always long-term. For a gift where the donor's basis carries over, the donor's holding period is added to the recipient's.
3. **Compute gain or loss for each lot:** the amount realized minus the adjusted basis. Apply the wash-sale rule before you net anything (see the table below).
4. **Net within each class, then across classes.** Short-term gains and losses net together, and so do long-term gains and losses. A net loss in one class then offsets a net gain in the other. A carried-over loss keeps its short-term or long-term character.
5. **Split the long-term gain into rate groups ([Pub. 550](https://www.irs.gov/publications/p550)):** 28% rate gain (collectibles, and the taxable part of §1202 gain), unrecaptured §1250 gain (25% group), and all other gain (0%/15%/20%). Qualified dividends go in the 0%/15%/20% group.
6. **Stack.** Ordinary taxable income fills the brackets first, and the preferential gain sits on top of it. The 0% and 15% ceilings are measured against total taxable income, not against the gain alone. Use the Qualified Dividends and Capital Gain Tax Worksheet. Use the Schedule D Tax Worksheet if there is 28% rate gain or unrecaptured §1250 gain ([Schedule D instructions](https://www.irs.gov/instructions/i1040sd)).
7. **If there is a net loss,** deduct up to the annual limit. The carryforward is the net loss minus the *lesser of* the allowable deduction or taxable income after the deduction increased by it (zero if negative; see the capital loss section). Short-term losses are used first.
8. **Test the NIIT separately** on Form 8960. The tax is 3.8% of the smaller of (a) net investment income or (b) MAGI above the threshold ([IRS NIIT page](https://www.irs.gov/individuals/net-investment-income-tax)).
9. **Report:** Form 8949 (unless an exception applies), then Schedule D, then Form 1040. Check whether estimated tax payments are needed.

## Rates and thresholds for 2026 ([Rev. Proc. 2025-32 §4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

Long-term gain and qualified dividends in the "other gain" group. The tax rate on the gain depends on where it sits within total taxable income:

| Filing status (2026) | 0% up to taxable income of | 15% up to taxable income of | 20% above |
| --- | --- | --- | --- |
| Single | $49,450 | $545,500 | $545,500 |
| Married filing jointly / surviving spouse | $98,900 | $613,700 | $613,700 |
| Married filing separately | $49,450 | $306,850 | $306,850 |
| Head of household | $66,200 | $579,600 | $579,600 |

- The table figures are the "maximum zero rate amount" and "maximum 15 percent rate amount" set for 2026 under §1(j)(5)(B) ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)).
- Net short-term gain has no special rate. It is taxed as ordinary income at the regular bracket rates.

### Groups taxed above 20% ([Pub. 550 Table 4-4](https://www.irs.gov/publications/p550))

- **Collectibles gain** held more than 1 year (a work of art, rug, antique, metal such as gold or silver bullion, gem, stamp, coin or alcoholic beverage): maximum rate 28%.
- **Taxable part of §1202 gain** (the eligible gain minus the §1202 exclusion): maximum rate 28%.
- **Unrecaptured §1250 gain:** the part of the gain on depreciated real property that comes from depreciation. It cannot exceed the net §1231 gain, and it is reduced by any net loss in the 28% group. Maximum rate 25%.
- These are *maximum* rates. If the taxpayer's ordinary bracket is lower, the lower rate applies. The Schedule D Tax Worksheet does this sum.
- **Digital-art NFTs:** Notice 2023-27 says the IRS *intends* to treat an NFT as a collectible when its associated right or asset is a collectible (a "look-through" test), until it issues guidance ([Notice 2023-27](https://www.irs.gov/pub/irs-drop/n-23-27.pdf)). This is interim guidance. Flag it as uncertain rather than stating it as settled law.

### Net investment income tax ([IRS NIIT page](https://www.irs.gov/individuals/net-investment-income-tax); [NIIT Q&A](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax))

| Filing status | MAGI threshold (same for 2025 and 2026) |
| --- | --- |
| Married filing jointly / qualifying surviving spouse | $250,000 |
| Married filing separately | $125,000 |
| Single / head of household | $200,000 |

- Rate: 3.8% of the smaller of net investment income or MAGI above the threshold ([IRS NIIT page](https://www.irs.gov/individuals/net-investment-income-tax)).
- The IRS says "these threshold amounts are not indexed for inflation". The statute sets them at a fixed $250,000 and $200,000, and the married-filing-separately figure is half the joint figure ([26 U.S.C. §1411(b)](https://www.law.cornell.edu/uscode/text/26/1411)).
- Net investment income includes capital gains, interest, dividends, rents, royalties, non-qualified annuities, and income from businesses that are passive activities for the taxpayer or that trade financial instruments or commodities ([NIIT Q&A](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax)). It excludes wages and most self-employment income. Home-sale gain excluded under §121 is also excluded from the NIIT.
- Nonresident aliens are not subject to the NIIT. A dual-status individual pays it only for the resident part of the year, and the threshold is not prorated ([NIIT Q&A](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax)).
- The NIIT counts for estimated tax. Underpaying it can trigger the estimated tax penalty.

### Capital loss limit ([26 U.S.C. §1211(b)](https://www.law.cornell.edu/uscode/text/26/1211); [Pub. 550](https://www.irs.gov/publications/p550))

- A net capital loss offsets ordinary income up to the lower of $3,000 ($1,500 if married filing separately) or the net loss. This amount is set by statute and is not indexed, so it is the same for 2025 and 2026.
- The unused loss carries forward with no time limit, until it is used up. It keeps its short-term or long-term character. A long-term carryover reduces long-term gains first.
- **Carryover amount:** the total net loss minus the *lesser of* (1) the allowable capital loss deduction for the year, or (2) taxable income (Form 1040 line 15, after the capital loss deduction; negative if so) increased by the allowable deduction. If that sum is zero or less, use zero (Pub. 550 Worksheet 4-1, lines 1-4). So when taxable income is low or negative, more of the loss carries forward, and it can be the whole loss.
- **Ordering:** when you work out the carryover, use short-term losses first, even if they came after a long-term loss. Then use long-term losses up to the limit.
- Count the current year's allowable deduction as used, even if the taxpayer did not claim it or file a return.
- If spouses filed a joint return and now file separately, a carryover from the joint year can be used only by the spouse who actually had the loss. A decedent's loss can be used only on the final return. The estate cannot carry it over.

## Boundaries and exceptions

| Rule | Condition that decides it | Source |
| --- | --- | --- |
| Long-term vs short-term | Held **more than** 1 year is long-term. Held exactly 1 year or less is short-term. The count starts the day after the trade date. | [26 U.S.C. §1222](https://www.law.cornell.edu/uscode/text/26/1222); [Pub. 550](https://www.irs.gov/publications/p550) |
| 0% / 15% ceiling | The 0% band applies up to and including the ceiling, measured on taxable income (after deductions), not on AGI and not on the gain alone | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Wash sale (§1091) | A loss on stock or securities is disallowed if substantially identical stock or securities are bought, acquired in a fully taxable trade, or covered by a contract or option within 30 days **before or after** the sale. Buying through the taxpayer's IRA or Roth IRA counts, as does a purchase by the spouse or a controlled corporation. | [Pub. 550](https://www.irs.gov/publications/p550); [26 U.S.C. §1091](https://www.law.cornell.edu/uscode/text/26/1091) |
| Wash-sale basis | The disallowed loss is added to the basis of the new shares, and the old holding period carries over. **Exception:** when the IRA or Roth IRA made the purchase, the loss is not added to basis. | [Pub. 550](https://www.irs.gov/publications/p550) |
| Wash sale and digital assets | §1091 is written for "stock or securities". Do not apply it, or rule it out, for a digital asset without first checking whether that asset is a security | [26 U.S.C. §1091](https://www.law.cornell.edu/uscode/text/26/1091) |
| Home sale (§121) full exclusion | Up to $250,000, or $500,000 on a joint return. Required: owned **and** used as the main home for at least 24 months within the 5 years ending on the sale date. The two periods need not be the same 24 months. On a joint return, either spouse can meet ownership, but **both** must meet use, and **neither** spouse can be barred by the 2-year rule. If a joint return fails these conditions, the limit is the sum of the limits each spouse would have separately. The 2-year rule: no other home sale using the exclusion in the 2 years ending on the sale date. | [Topic 701](https://www.irs.gov/taxtopics/tc701); [26 U.S.C. §121](https://www.law.cornell.edu/uscode/text/26/121) |
| Home sale partial exclusion | If the 24-month tests are not met but the main reason for the sale was a change in workplace, health, or an unforeseeable event, the limit is prorated. The factor is the shorter of the qualifying ownership-and-use period or the time since the last excluded sale, divided by 2 years. One example of a qualifying work move is a new job at least 50 miles farther from the home than the old work location. Pub. 523 lists others: for example, a first job at least 50 miles from the home, or the same events happening to the spouse, a co-owner or another resident of the home. | [26 U.S.C. §121(c)](https://www.law.cornell.edu/uscode/text/26/121); [Pub. 523](https://www.irs.gov/publications/p523) |
| Home sale: depreciation and nonqualified use | Gain equal to depreciation allowed or allowable after May 6, 1997 (rental or home office) cannot be excluded. Gain allocated to periods of nonqualified use (for example, rental or a second home after 2008, before the property became the main home) is not excluded. | [Pub. 523](https://www.irs.gov/publications/p523); [26 U.S.C. §121(b)(5)](https://www.law.cornell.edu/uscode/text/26/121) |
| Surviving spouse | The $500,000 limit can still apply only if the survivor is **unmarried (has not remarried) on the date of sale**, the sale is no later than 2 years after the spouse's death, and the joint-return conditions were met just before the death. Pub. 523 adds that neither spouse can have used the exclusion on another home sold less than 2 years before this sale. | [26 U.S.C. §121(b)(4)](https://www.law.cornell.edu/uscode/text/26/121); [Pub. 523](https://www.irs.gov/publications/p523) |
| Like-kind exchange (§1031) | Real property only, held for business use or investment, exchanged for like-kind real property held for business use or investment. Real property held primarily for sale does not qualify. Shares, securities and other personal property do not qualify. | [26 U.S.C. §1031(a)](https://www.law.cornell.edu/uscode/text/26/1031) |
| §1031 deadlines | Identify the replacement property on or before day 45 after transferring the old property. Receive it by the **earlier** of day 180 or the due date of the return for that year, including extensions. File on time, or extend, when the 180-day window runs past April. | [26 U.S.C. §1031(a)(3)](https://www.law.cornell.edu/uscode/text/26/1031); [Pub. 550](https://www.irs.gov/publications/p550) |
| §1031 US and foreign property | US real property and foreign real property are **not** like kind to each other. Foreign-for-foreign is not barred by this rule. | [26 U.S.C. §1031(h)](https://www.law.cornell.edu/uscode/text/26/1031) |
| Installment sale (§453) | Required when at least one payment falls in a later year, unless the taxpayer elects out by the return due date (including extensions) for the year of sale. Not available for losses, inventory, or stock and securities traded on an established market. Depreciation recapture is taxed in the year of sale. | [Topic 705](https://www.irs.gov/taxtopics/tc705) |
| Installment interest | Interest is ordinary income. If the contract does not state adequate interest, part of the principal is recharacterized using the applicable federal rate. | [Topic 705](https://www.irs.gov/taxtopics/tc705) |
| Installment: related buyer resells | If a related buyer resells before paying in full and within 2 years of the first sale, the seller may be treated as receiving the resale amount. For marketable securities the 2-year limit does not apply, so the rule has no time limit for them. | [Pub. 537](https://www.irs.gov/publications/p537) |
| Installment: interest on deferred tax | Applies to an obligation when its sales price is over $150,000 and the total of all nondealer installment obligations that arose **during** the tax year and are still outstanding at its close is more than $5 million. Interest then continues in later years while those obligations remain outstanding. | [Pub. 537](https://www.irs.gov/publications/p537) |

## Worked cases

The amounts in these cases are made up for illustration. The thresholds and rates come from the sources linked in each heading.

### Case 1: 2026 single filer, gain straddles the 0% ceiling ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

- Taxable income $70,000, of which $40,000 is long-term gain. Ordinary taxable income is $70,000 - $40,000 = $30,000.
- 0% room: $49,450 - $30,000 = $19,450 of the gain is taxed at 0%.
- The rest, $40,000 - $19,450 = $20,550, is taxed at 15%: $20,550 × 15% = $3,082.50.
- MAGI is assumed to be below $200,000, so there is no NIIT.

### Case 2: 2026 joint filers, NIIT ([IRS NIIT page](https://www.irs.gov/individuals/net-investment-income-tax))

- MAGI $300,000, and net investment income $80,000.
- MAGI over the threshold: $300,000 - $250,000 = $50,000. That is smaller than the $80,000 of net investment income.
- NIIT: $50,000 × 3.8% = $1,900, on Form 8960.

### Case 3: married filing separately, net capital loss ([26 U.S.C. §1211(b)](https://www.law.cornell.edu/uscode/text/26/1211))

- Net capital loss for the year is $10,000. Taxable income before the loss deduction is well above the deduction.
- Deduction: $1,500, not $3,000, because of the separate-return limit.
- Carryforward: $10,000 - $1,500 = $8,500. It keeps its character.

### Case 4: main home, full exclusion ([Topic 701](https://www.irs.gov/taxtopics/tc701))

- A single filer owned the home and lived in it for 3 of the last 5 years. No depreciation, no nonqualified use, and no excluded sale in the prior 2 years. The gain is $300,000.
- Excluded: $250,000. Taxable long-term gain: $300,000 - $250,000 = $50,000. Report it on Form 8949 and Schedule D. The excluded part is also outside the NIIT.

### Case 5: main home, partial exclusion after a job move ([26 U.S.C. §121(c)](https://www.law.cornell.edu/uscode/text/26/121))

- A single filer owned the home and used it as the main home for 12 months. They then took a new job whose location is 60 miles farther from the home than the old one. There was no earlier excluded sale.
- The limit is prorated: $250,000 × 12 ÷ 24 = $125,000. Gain above that limit is taxable.

### Case 6: wash sale ([Pub. 550](https://www.irs.gov/publications/p550))

- Bought 100 shares for $1,000 and sold them for $750. Within 30 days, bought 100 shares of the same stock for $800.
- The $250 loss is disallowed. The new basis is $800 + $250 = $1,050, and the holding period of the old shares carries over.

### Case 7: 2025 return, joint filers, gain straddles the 0% ceiling ([Rev. Proc. 2024-40 §2.03](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf))

- 2025 taxable income $120,000, of which $30,000 is long-term gain and qualified dividends. Ordinary taxable income: $120,000 - $30,000 = $90,000.
- 0% room: $96,700 - $90,000 = $6,700. The rest, $30,000 - $6,700 = $23,300, is taxed at 15%: $23,300 × 15% = $3,495.

## 2025 returns: tax year 2025, extended deadline October 15, 2026 ([Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf))

Use the 2025 amounts from [Rev. Proc. 2024-40 §2.03](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) and the 2025 forms. The NIIT thresholds, the 3.8% rate and the $3,000 / $1,500 loss limit are the same as for 2026.

| Filing status (2025) | 0% up to taxable income of | 15% up to taxable income of | 20% above |
| --- | --- | --- | --- |
| Single | $48,350 | $533,400 | $533,400 |
| Married filing jointly / surviving spouse | $96,700 | $600,050 | $600,050 |
| Married filing separately | $48,350 | $300,000 | $300,000 |
| Head of household | $64,750 | $566,700 | $566,700 |

- **New for 2025 forms** ([2025 Schedule D instructions](https://www.irs.gov/instructions/i1040sd)): Form 8949 and Schedule D have new codes G through L for digital-asset transactions reported on Form 1099-DA.
- The extension moves the **filing** date only. Tax was due by the April filing date, so interest and any late-payment penalty run from then ([IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).

## When to refuse or refer

- **Refer** qualified small business stock (§1202), including the tiered exclusion for stock issued after July 4, 2025, to the `us-section-1202-qsbs` Guide. Check the issuance date and holding period there before you promise any exclusion.
- **Refer** nonresident aliens and dual-status years to the `us-nonresident-cgt` Guide. The NIIT and the rates here assume US residence for the year.
- **Refer** anything involving depreciation recapture on business property, partnership interests (including carried interests), or §1231 netting across several business assets. Use Pub. 544 and Form 4797, and review with an accountant.
- **Refer** like-kind exchanges with boot, related parties, reverse or build-to-suit structures, or a missed 45-day or 180-day deadline. These need a qualified intermediary and professional review.
- **Refuse to state as settled:** the collectible status of an NFT, whether §1091 applies to a particular digital asset, and any state's tax on the gain. Say what is uncertain and name the official source to check.
- **Refer** mark-to-market traders, straddles, short sales against the box, options and §1256 contracts. Special rules in Pub. 550 apply.

## Filing and payment

- **Forms:** report each sale on Form 8949 and total it on Schedule D. **Exception:** transactions with basis reported to the IRS on Form 1099-B or 1099-DA, with no adjustments and no ordinary, QOF or collectibles items, can go straight on Schedule D line 1a (short-term) or 8a (long-term) ([Schedule D instructions](https://www.irs.gov/instructions/i1040sd)).
- A home sale must be reported if the taxpayer received Form 1099-S, or if not all the gain can be excluded ([Topic 701](https://www.irs.gov/taxtopics/tc701)).
- Installment sales: Form 6252 in the year of sale and in each later year with payments ([Topic 705](https://www.irs.gov/taxtopics/tc705)). Like-kind exchanges: Form 8824. NIIT: Form 8960, attached to Form 1040.
- **Deadlines:** the return and payment are due by the April filing due date after year-end. An extension moves only the filing date, to October 15 ([IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)). For 2026 returns, confirm the April 2027 date in the 2026 Form 1040 instructions once they are published.
- **Estimated tax:** a large gain, or NIIT, can require quarterly estimated payments or more withholding to avoid the estimated tax penalty ([NIIT Q&A](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax)).

## Completion checklist

- Filing status and tax year are confirmed. The 2026 table is used for 2026 and the 2025 table for 2025.
- Every lot has a trade-date holding period and a basis that ties to the 1099-B or 1099-DA, or to records.
- Wash sales in the 30 days either side of each loss sale are checked, including IRA, Roth IRA and spouse accounts.
- Gains are split into the 28%, 25% and 0/15/20 groups ([Pub. 550](https://www.irs.gov/publications/p550)), and the correct worksheet is used.
- Any net loss is limited to $3,000 ($1,500 MFS). The carryforward uses the lesser-of taxable-income rule and the short-term-first ordering, and it is recorded by character ([26 U.S.C. §1211(b)](https://www.law.cornell.edu/uscode/text/26/1211)).
- The NIIT is tested against the fixed thresholds, and Form 8960 is attached if tax is due.
- For a home sale, ownership, use, the 2-year lookback, depreciation after May 6, 1997, nonqualified use and partial exclusion are all checked.
- For §1031, the 45-day and 180-day or return-due-date limits are met and US and foreign property are not mixed.
- The installment election-out decision has been made by the due date, and recapture is taxed in the year of sale.
- State treatment has been checked separately, and the §1202 and nonresident points have been referred.

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
