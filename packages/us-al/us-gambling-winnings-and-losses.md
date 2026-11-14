---
name: us-gambling-winnings-and-losses
description: Report US gambling winnings and deduct gambling losses for tax year 2026. Covers Form W-2G reporting (the 2026 minimum threshold of $2,000, the 300 times the wager test), 24% regular gambling withholding above $5,000 and 24% backup withholding, winnings on Schedule 1, losses as an itemized deduction on Schedule A, and the One Big Beautiful Bill Act rule from 2026 that only 90 percent of wagering losses is deductible and only up to wagering gains (section 165(d) as amended by Public Law 119-21 section 70114), including for professional gamblers on Schedule C. Trigger on "gambling winnings", "W-2G", "casino jackpot tax", "sports betting tax", "gambling losses deduction", "professional gambler", "lottery win tax", "90% gambling loss rule". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US gambling winnings and losses, tax year 2026

> **Source-cited draft.** Built from Public Law 119-21 section 70114, 26 U.S.C. 165, the Instructions for Forms W-2G and 5754 (Rev. January 2026), Pub. 1099 (2026) and Pub. 529, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** All gambling winnings are taxable income, whether or not a Form W-2G was issued. From tax year 2026, losses from wagering transactions are deductible at **90 percent** of the losses, and only up to the gains from wagering for the year. A casual gambler deducts them only by itemizing on Schedule A. Someone who breaks even therefore pays tax on 10 percent of their losses. Payers issue Form W-2G from a minimum threshold of **$2,000** in 2026 and withhold **24%** in the cases listed below.

## Scope and who this is for

In scope: a US citizen or resident individual with gambling winnings (casino, slot machines, table games, poker, lotteries, sweepstakes, raffles, horse and dog racing, sports betting, online wagering) in tax year 2026: what is income, what the payer reports and withholds, and how losses are deducted, for casual and professional gamblers.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether to itemize at all, the standard deduction, the rate schedules | `us-federal-income-tax-return-1040` |
| Nonresident aliens (30% withholding, Form 1042-S, treaty exemptions) | `us-form-1040-nr-nonresident-return`, `us-tax-treaty-claims-8833` |
| Self-employment tax mechanics for a professional gambler | `us-schedule-c-and-se-computation` |
| Paying tax on a large win during the year | `us-quarterly-estimated-tax` |
| Prediction markets and crypto wagering platforms where the character of the contract is unclear | Refer (R-GAM-CONTRACT) |
| State tax on winnings | the state's income tax skill |

## Ask the client first

1. **Every win in 2026**, not just the ones with a Form W-2G: casino win/loss statements, online sportsbook and casino annual statements, lottery and raffle prizes, the fair market value of any non-cash prize.
2. **Losses and the records behind them:** a diary (date, place, game, amount won and lost), losing tickets, sportsbook account history, casino player-card statements. Without records the deduction is at risk.
3. **Withholding:** box 4 of each Form W-2G (federal tax withheld), and any state withholding.
4. **Other itemized deductions** (state and local taxes, mortgage interest, charity, medical). Losses only help if the total beats the standard deduction.
5. **Is gambling a trade or business?** Hours per week, whether it is the main source of income, records kept like a business, history of profits. This decides Schedule A or Schedule C.
6. **Filing status and residency.** A nonresident alien is outside this skill.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Share of wagering losses that is deductible, taxable years beginning after 31 December 2025 | 90 percent | [Public Law 119-21, section 70114 (amending 26 U.S.C. 165(d))](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Ceiling on the deduction | the gains from wagering transactions in the same year | [Public Law 119-21, section 70114](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Minimum Form W-2G reporting threshold, payments made in calendar year 2026 | USD 2,000 | [Instructions for Forms W-2G and 5754 (Rev. January 2026), What's New](https://www.irs.gov/pub/irs-pdf/iw2g.pdf) |
| Ratio test for parimutuel, sweepstakes, lotteries, sports wagering and similar winnings | at least 300 times the wager | [Instructions for Forms W-2G and 5754 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/iw2g.pdf) |
| Regular gambling withholding applies when winnings minus the wager are more than | USD 5,000 | [Instructions for Forms W-2G and 5754 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/iw2g.pdf) |
| Regular gambling withholding rate | 24% | [Instructions for Forms W-2G and 5754 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/iw2g.pdf) |
| Regular gambling withholding rate on certain non-cash prizes when the payer pays the tax | 31.58% | [Instructions for Forms W-2G and 5754 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/iw2g.pdf) |
| Backup withholding rate (no taxpayer identification number given) | 24% | [Instructions for Forms W-2G and 5754 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/iw2g.pdf) |
| Withholding on gambling winnings paid to a foreign person (generally) | 30% | [Instructions for Forms W-2G and 5754 (Rev. January 2026), Foreign Persons](https://www.irs.gov/pub/irs-pdf/iw2g.pdf) |

The W-2G threshold is adjusted for inflation every year from 2026 (Pub. 1099 (2026), footnote to the W-2G row). The standard deduction is in `us-federal-income-tax-return-1040`; the 2026 SALT cap and the 2/37 limit on itemized deductions for top-bracket taxpayers are in the federal library (`us.obbba.salt.cap-2026`, `us.obbba.itemized.2-37`).

### Step 1: add up winnings, gross

1. Total every gambling win for 2026 at its full amount: cash, and the fair market value of non-cash prizes (a car, a trip). Do not net losses against winnings. Source: [Pub. 529](https://www.irs.gov/pub/irs-pdf/p529.pdf) ("You can't reduce your gambling winnings by your gambling losses and report the difference").
2. Winnings are reportable even with no Form W-2G. A W-2G is only the payer's information return; the amounts on it must be in the total.
3. A casual gambler reports the total as other income on Schedule 1 (Form 1040) ("gambling winnings" line). A professional gambler reports it as gross receipts on Schedule C (Step 4).

### Step 2: check what the payer reported and withheld

4. **When a Form W-2G is issued.** For 2026 payments the minimum threshold is USD 2,000. For horse racing, dog racing, jai alai, sweepstakes, wagering pools, lotteries and sports wagering the winnings must also be at least 300 times the wager. For bingo, keno and slot machines the payer may report all of a day's wins on one form (aggregate method, "gaming day"). For a poker tournament the threshold is applied to the winnings minus the buy-in, tournament by tournament. Source: [Instructions for Forms W-2G and 5754](https://www.irs.gov/pub/irs-pdf/iw2g.pdf).
5. **Regular gambling withholding, 24%:** on winnings minus the wager of more than USD 5,000 from sweepstakes, wagering pools, lotteries, parimutuel pools (if at least 300 times the wager), and sports wagering and other wagering (if at least 300 times the wager). It is figured on the whole amount, not just the excess over USD 5,000. It does not apply to bingo, keno, slot machines or poker tournaments.
6. **Backup withholding, 24%:** if the winner gives no correct taxpayer identification number, regular withholding did not apply, and the winnings reach the reporting threshold (and the 300 times test where it applies).
7. Box 4 withholding on each W-2G goes on Form 1040 as federal income tax withheld. Withholding at 24% may be less than the tax due on a large win in a higher bracket: check estimated tax (`us-quarterly-estimated-tax`).

### Step 3: casual gambler, losses on Schedule A

8. **Losses that count:** the cost of losing wagers, tickets and bets during 2026, and (from 2026) any other deduction incurred in carrying on a wagering transaction, such as travel to and from a casino. Source: [Public Law 119-21, section 70114](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) (new 165(d)(2)); [Pub. 529](https://www.irs.gov/pub/irs-pdf/p529.pdf).
9. **Allowed deduction** = the smaller of (a) 90 percent of the losses and (b) the winnings for the year. Formula: `min(losses x 0.90, winnings)`.
10. Claim it on Schedule A as an other itemized deduction. It helps only if total itemized deductions beat the standard deduction; otherwise the loss is worth nothing and the full winnings are taxed. Compare both, as in Case 1.
11. Unused losses do not carry forward or back to another year.

### Step 4: professional gambler, Schedule C

12. A person whose gambling is a trade or business (pursued full time, for profit, in a businesslike way) reports winnings and losses on Schedule C instead of Schedule 1 and Schedule A. Business expenses (travel, subscriptions, data) count as losses from wagering transactions under new 165(d)(2), so the same 90 percent and gains ceiling applies to wagers and expenses together. Formula: `min((losing wagers + expenses) x 0.90, winnings)`.
13. The result can never be a Schedule C loss from gambling; it can be a net profit even when the gambler lost money in the year (Case 2).
14. A professional gambler's Schedule C net profit is self-employment income: run Schedule SE (`us-schedule-c-and-se-computation`).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Break-even year (winnings equal losses) | Taxable income of 10 percent of the losses remains, if itemizing; the full winnings if not |
| Losses larger than winnings | Deduction capped at winnings (after the 90 percent cut); no carryover |
| Taxpayer takes the standard deduction | No loss deduction at all; full winnings taxed |
| Win of a car or other non-cash prize | Income at fair market value; payer may pay the withholding at 31.58% and gross it up on the W-2G |
| Win shared with others | Payer issues W-2Gs to each winner using Form 5754 |
| No W-2G received | Still income; Form W-2G thresholds govern the payer, not the taxpayer |
| State lottery win paid in instalments | Each instalment is income when paid; withholding applies by instalment |
| Professional gambler with a net economic loss | Schedule C can still show a profit (90 percent rule); self-employment tax on that profit |
| Nonresident alien | Outside this skill: 30% withholding, Form 1042-S, possible treaty exemption |
| Winnings in tax years before 2026 | 100 percent of losses up to winnings applied; this skill's 90 percent rule starts with tax years beginning after 31 December 2025 |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Total winnings | Sum of W-2G box 1 amounts plus any statement totals; ask for all sportsbook and casino annual statements |
| Losses with no records | Do not claim; ask for a diary, tickets and account statements |
| Professional status | Casual gambler (Schedule A) unless the facts show a trade or business |
| Other itemized deductions | Ask; do not assume itemizing |
| Federal withholding | W-2G box 4 only |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| W-2G amounts larger than winnings reported | IRS matching notice |
| Large losses claimed with only a W-2G total as evidence | Losses are disallowed without records |
| A single large win taxed above the 24% withheld | Underpayment and possible estimated tax penalty |
| Client calls themselves professional but has another full-time job | Schedule C status is likely to be challenged |
| Online accounts in several states | State sourcing and nonresident state returns may apply |

## Worked cases

**Case 1, a decision: itemize to use the losses, or take the standard deduction?** A single filer in 2026 won USD 30,000 (two slot jackpots with Forms W-2G and online sportsbook wins) and has records of USD 28,000 of losses. Other itemized deductions are USD 8,000 of state and local taxes. The 2026 single standard deduction is USD 16,100 (`us.std.single`; see `us-federal-income-tax-return-1040`).

Allowed loss: the smaller of 90% x USD 28,000 = USD 25,200 and USD 30,000, so USD 25,200. Itemized total: USD 25,200 + USD 8,000 = USD 33,200, which is USD 17,100 more than the standard deduction. Itemize. After the loss deduction, USD 4,800 of the winnings stays in taxable income even though the client's net gambling gain was only USD 2,000. If the client took the standard deduction instead, all USD 30,000 would be taxed with no loss deduction.

```oa-check
name: Gambling losses, itemize or standard deduction (single, 2026)
inputs:
  winnings: 30000
  losses: 28000
  other_itemized: 8000
  standard_deduction: 16100
steps:
  - allowed_loss: min(losses * 0.90, winnings)
  - itemized: allowed_loss + other_itemized
  - better_deduction: max(itemized, standard_deduction)
  - itemizing_gain: itemized - standard_deduction
  - winnings_left_taxed: winnings - allowed_loss
expected:
  allowed_loss: 25200.00
  itemized: 33200.00
  better_deduction: 33200.00
  itemizing_gain: 17100.00
  winnings_left_taxed: 4800.00
```

**Case 2, professional gambler with an economic loss.** A full-time professional poker and sports bettor had USD 100,000 of winnings, USD 95,000 of losing wagers and USD 10,000 of business expenses (travel, data subscriptions) in 2026. Economically the year lost USD 5,000.

Losses from wagering transactions include the expenses: USD 105,000. Allowed: the smaller of 90% x USD 105,000 = USD 94,500 and USD 100,000, so USD 94,500. Schedule C net profit: USD 100,000 - USD 94,500 = USD 5,500. Self-employment tax: USD 5,500 x 92.35% = USD 5,079.25 of net earnings, times 15.3% = USD 777.13 (the rates are in `us-schedule-c-and-se-computation`; no wages assumed).

```oa-check
name: Professional gambler, 90 percent limit on Schedule C (2026)
inputs:
  winnings: 100000
  losing_wagers: 95000
  expenses: 10000
steps:
  - wagering_losses: losing_wagers + expenses
  - allowed: min(wagering_losses * 0.90, winnings)
  - net_profit: winnings - allowed
  - net_earnings: net_profit * 0.9235
  - se_tax: net_earnings * 0.153
  - economic_result: winnings - wagering_losses
expected:
  wagering_losses: 105000.00
  allowed: 94500.00
  net_profit: 5500.00
  net_earnings: 5079.25
  se_tax: 777.13
  economic_result: -5000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GAM-NRA | Winner is a nonresident alien | Refer to `us-form-1040-nr-nonresident-return`; treaty claims in `us-tax-treaty-claims-8833` |
| R-GAM-PRO | Professional status is disputed or the client has an IRS examination of it | Refer: facts-and-circumstances test for a reviewer |
| R-GAM-CONTRACT | Event contracts on prediction markets, crypto wagering, fantasy sports structured as contests | Refer: whether section 165(d) or other rules apply is not settled here |
| R-GAM-RECORDS | Large losses with no contemporaneous records | Flag: do not claim without records |
| R-GAM-PRIOR | Amending a 2025 or earlier return | Pre-2026 rules apply (losses at 100 percent up to winnings); outside this 2026 skill |

## Filing and payment

Winnings and losses go on the 2026 Form 1040 (Schedule 1 and Schedule A, or Schedule C and Schedule SE), due **15 April 2027**; an extension to 15 October 2027 extends filing, not payment. Payers must furnish Form W-2G to winners by 31 January 2027 for 2026 payments (Pub. 1099 (2026)). Tax on a large win during 2026 not covered by withholding should be paid through estimated tax: see `us-quarterly-estimated-tax`.

## Completion checklist

- Every win included gross, including those with no W-2G, and the W-2G totals reconcile.
- Losses backed by records; allowed deduction = min(90% of losses, winnings).
- Itemized against standard deduction compared; the loss only helps when itemizing.
- Professional gambler: expenses included in wagering losses, 90 percent applied, Schedule SE run.
- W-2G box 4 withholding claimed; estimated tax checked for large wins.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Law 119-21, section 70114. Read for new 165(d)(1): deduction "equal to 90 percent of the amount of such losses" and allowed "only to the extent of the gains"; 165(d)(2): losses include any deduction incurred in carrying on a wagering transaction; effective for taxable years beginning after 31 December 2025. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 165 (govinfo, 2024 edition). Read for the structure of section 165; its (d) text predates Public Law 119-21 and is superseded for 2026. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec165.htm | 2026-11-13 |
| Instructions for Forms W-2G and 5754 (Rev. January 2026). Read for What's New ($2,000 minimum threshold for 2026), regular gambling withholding (24%, more than $5,000, 300 times the wager), 31.58% for non-cash prizes, backup withholding (24%), poker tournaments, aggregate reporting for bingo, keno and slots, and foreign persons (30%). | https://www.irs.gov/pub/irs-pdf/iw2g.pdf | 2026-11-13 |
| Pub. 1099 (2026). Read for the W-2G row ("Generally, $2,000 or more"), the inflation-adjustment footnote and the 31 January furnishing date. | https://www.irs.gov/pub/irs-pdf/p1099.pdf | 2026-11-13 |
| Pub. 529 (Rev. December 2020). Read for gambling losses up to winnings on Schedule A, no netting, and the diary and record requirements. | https://www.irs.gov/pub/irs-pdf/p529.pdf | 2026-11-13 |

Not yet confirmed: the 2026 game-by-game W-2G thresholds above the USD 2,000 minimum (the IRS points to IRS.gov/InflationAdjustment and the figures were not on that page when read), and the 2026 Schedule 1, Schedule A and Schedule C line numbers and instructions for the 90 percent rule, which were not yet published when read. Pub. 529 has not been updated since December 2020 and predates the 90 percent rule.
