---
name: uk-scottish-income-tax
description: "Scottish income tax for UK resident individuals, tax year 2026/27 (6 April 2026 to 5 April 2027), with the 2025/26 bands for returns filed now. Covers who is a Scottish taxpayer (Scotland Act 1998 ss 80D to 80F: close connection, main home, midnight days count), the six Scottish rates and band limits set by the Scottish Rate Resolution 2026-27, why savings and dividends stay on UK rates and the UK basic rate limit, the Personal Allowance taper, how the SA100 computes it, Gift Aid and relief-at-source pension extensions of the Scottish limits, and PAYE S codes (S1257L, SBR, SD0 to SD3). Trigger phrases: Scottish taxpayer, Scottish income tax, intermediate rate 21%, S tax code, live in Scotland tax return, moving to Scotland tax. Out of scope: UK-wide rules and allowances (uk-income-tax-sa100), self-employment profits (uk-self-employment-sa103), National Insurance (uk-national-insurance), payroll running (uk-payroll), residence (uk-statutory-residence-test)."
version: 0.2
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Scottish income tax on the SA100 (2026/27, with 2025/26)

> **Source-cited draft.** Drafted from the Scotland Act 1998, the Income Tax Act 2007, the Finance Act 2004, the Scottish Rate Resolution 2026-27 as agreed by the Scottish Parliament, and HMRC and Scottish Government pages, all read on 2026-10-23. No accountant has reviewed it. Do not file from it without review by a qualified UK professional.

This skill adds Scottish taxpayers to the UK individual income tax method. Use it with `uk-income-tax-sa100`, which holds the UK-wide steps (who files, allowances, savings and dividend rates, Marriage Allowance, Child Benefit charge, payments on account). Where this skill is silent, the UK rule in that skill applies unchanged. Self-employed profits come from `uk-self-employment-sa103`, National Insurance from `uk-national-insurance`, PAYE mechanics from `uk-payroll`.

Tax year: 6 April to 5 April. Authority: HM Revenue and Customs (HMRC) collects Scottish income tax; the Scottish Parliament sets the rates and bands. Currency: pound sterling (GBP).

## Who this applies to

A Scottish taxpayer for a tax year is an individual who is **resident in the UK** for that year and meets condition A, B or C (Scotland Act 1998 s 80D(1)):

- **Condition A: close connection with Scotland** (s 80D(2), s 80E).
  - One place of residence in the UK: it is in Scotland and they live there for at least part of the year (s 80E(2)).
  - Two or more places of residence in the UK: their main place of residence is in Scotland for at least part of the year, for more of the year than in each other part of the UK, and they live at a place in Scotland for at least part of the year (s 80E(3)).
- **Condition B: days count** (s 80D(3), s 80F). They have no close connection with England, Wales or Northern Ireland, and they are in Scotland at the end of the day (midnight) on more days than in each of England, Wales and Northern Ireland. A day in transit (arrive as a passenger, leave the next day, nothing unrelated to the journey) does not count as a day in the UK (s 80F(2)).
- **Condition C: office.** A Member of the Scottish Parliament, or an MP for a Scottish constituency, for any part of the year (s 80D(4)).

Status is for the **whole tax year**. There is no split between Scottish and other UK rates inside a year. A person who moves to Scotland pays Scottish income tax for the year if they live there for longer than anywhere else in the UK that year, and HMRC backdates the change to 6 April ([Scottish Income Tax: if you move](https://www.gov.uk/scottish-income-tax/if-you-move-to-or-from-scotland)).

**Main home.** HMRC treats the main home as usually where the person lives and spends most time, whether owned, rented or free. It may be the home where they spend less time if that is where most possessions are, where a spouse or civil partner lives, where they are registered with bank, GP or car insurance, or where they belong to clubs ([more than one home](https://www.gov.uk/scottish-income-tax/if-you-live-in-more-than-one-home)).

**Who is out:**
- Non-UK residents. They cannot be Scottish taxpayers (s 80D(1)(a)) and pay the default UK rates (ITA 2007 s 11C, listed in s 10(4)). See `uk-non-resident-sa109`.
- Welsh parliamentarians (s 80D(4A)), who are Welsh taxpayers.

## Rates, bands and thresholds

Scottish rates apply to **non-savings income only**: employment, pensions, trading profits, property income and most other income (ITA 2007 s 11A(1A)). Savings and dividend income use UK rates and the UK bands ([Scottish Income Tax](https://www.gov.uk/scottish-income-tax)).

The Scottish Rate Resolution sets limits on income **above the Personal Allowance**. The GOV.UK table restates them as total income for someone with the standard £12,570 allowance.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal Allowance (UK-wide) | £12,570 | 2026/27 | https://www.gov.uk/scottish-income-tax |
| Starter rate | 19% on taxable income up to £3,967 (total income £12,571 to £16,537) | 2026/27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Scottish basic rate | 20% above £3,967 up to £16,956 (total £16,538 to £29,526) | 2026/27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Intermediate rate | 21% above £16,956 up to £31,092 (total £29,527 to £43,662) | 2026/27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Higher rate | 42% above £31,092 up to £62,430 (total £43,663 to £75,000) | 2026/27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Advanced rate | 45% above £62,430 up to £125,140 (total £75,001 to £125,140) | 2026/27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Top rate | 48% above £125,140 | 2026/27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Starter rate, total income | £12,571 to £15,397 at 19% | 2025/26 | https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Basic rate, total income | £15,398 to £27,491 at 20% | 2025/26 | https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Intermediate rate, total income | £27,492 to £43,662 at 21% | 2025/26 | https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Higher, advanced, top, total income | £43,663 to £75,000 at 42%; £75,001 to £125,140 at 45%; over £125,140 at 48% | 2025/26 | https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Personal Allowance taper | £1 lost for every £2 of adjusted net income over £100,000; nil at £125,140 | 2026/27 | https://www.gov.uk/income-tax-rates |
| UK basic rate limit (used for savings and dividends) | £37,700 | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/10 |
| Dividend allowance; ordinary, upper, additional rates | £500; 10.75%, 35.75%, 39.35% | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/8 |
| Relief-at-source pension relief given by the scheme | Scottish basic rate, 20% | 2026/27 | https://www.legislation.gov.uk/ukpga/2004/12/section/192 |

The Scottish Parliament agreed the 2026-27 resolution (motion S6M-20844) on 19 February 2026, 93 for and 29 against. It is set under Scotland Act 1998 s 80C, applies for one tax year only (s 80C(3)), and is made "for the purposes of section 11A of the Income Tax Act 2007". The Scottish Government's own table matches the GOV.UK figures ([gov.scot rates and bands 2026 to 2027](https://www.gov.scot/publications/scottish-income-tax-rates-and-bands/pages/2026-to-2027/)).

**Personal Allowance taper.** The taper is a UK rule and applies to Scottish taxpayers in the same way. Between £100,000 and £125,140 of adjusted net income, each extra £1 of non-savings income is taxed at the 45% advanced rate and also removes 50p of allowance, which is then taxed at 45%. The marginal rate in that range is therefore 45% + 22.5% = 67.5%. The top rate starts at £125,140, which is where the allowance reaches nil.

## The taxable base

Run the `uk-income-tax-sa100` method. Change these steps only.

1. **Total income and reliefs** are the same as for any UK taxpayer. Trading profit, property profit, employment income and pensions are worked out under UK law.
2. **Personal Allowance and taper** are UK rules. Set the allowance against non-savings income first, as usual.
3. **Split taxable income** into non-savings, savings and dividends in the normal order (ITA 2007 s 16, applied by s 11A(6)).
4. **Charge non-savings income at the Scottish bands** (s 11A(1A)): 19%, 20%, 21%, 42%, 45%, 48% on the limits above.
5. **Charge savings and dividends at UK rates**, placing them in the UK bands by reference to the UK basic rate limit of £37,700 and the higher rate limit of £125,140. ITA 2007 s 13 charges dividends at the ordinary rate where they "would otherwise be charged at the basic rate", and s 13(5) reads that test for a Scottish taxpayer as income that would be charged at that rate "if the individual were not a Scottish taxpayer". The UK basic rate limit under s 10, not a Scottish limit, decides the dividend rate. So a Scottish taxpayer can pay 42% on salary and still pay the dividend ordinary rate on dividends.
6. **Extend the Scottish limits for Gift Aid.** The grossed-up gift increases the UK basic and higher rate limits and, for a Scottish taxpayer, "the upper limit for the Scottish basic rate and the limits for any Scottish rates above the Scottish basic rate" (ITA 2007 s 414(2)(b)). The gift is still treated as made after deduction of tax at the UK basic rate of 20% (s 414(2)(a)), so the charity claims at 20%.
7. **Extend the Scottish limits for relief-at-source pension contributions.** The scheme claims relief at the Scottish basic rate of 20% (FA 2004 s 192(1A)). If any income is charged at a Scottish rate above the Scottish basic rate, a claim increases the Scottish basic rate limit and every higher Scottish limit by the gross contribution (s 192(4A)). This gives the extra 1% at the intermediate rate, and 22%, 25% or 28% at the higher, advanced and top rates. A starter-rate taxpayer keeps the 20% relief; HMRC does not recover the 1% difference ([PTM044220](https://www.gov.uk/hmrc-internal-manuals/pensions-tax-manual/ptm044220)).
8. **Tax reducers, charges and tax paid** follow the UK steps. PAYE deducted under an S code counts as tax paid.

**PAYE codes.** A Scottish taxpayer's code starts with S. The standard code is S1257L. S0T means the Scottish allowance is used up or not known. SBR, SD0, SD1, SD2 and SD3 tax all pay from that job at the Scottish basic, intermediate, higher, advanced and top rate ([tax codes](https://www.gov.uk/tax-codes)). The S prefix tells the employer or pension provider to deduct tax at Scottish rates ([who pays](https://www.gov.uk/scottish-income-tax/who-pays)). The 2026/27 PAYE bands are in `uk-payroll`.

**Losses** are UK rules. A trading loss set against general income reduces total income before the Scottish bands are applied.

## Deadlines and filing

The deadlines are the UK Self Assessment deadlines in `uk-income-tax-sa100`.

| Item | Date |
|---|---|
| Register for Self Assessment, 2025/26 | 5 October 2026 |
| Paper return, 2025/26 | 31 October 2026 |
| Online return and balancing payment, 2025/26; first payment on account 2026/27 | 31 January 2027 |
| Second payment on account 2026/27 | 31 July 2027 |
| Online return and balancing payment, 2026/27 | 31 January 2028 |

Source: [Self Assessment deadlines and penalties](https://www.gov.uk/self-assessment-tax-returns/penalties) and [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account).

- **Tell HMRC on the return.** The online SA100 has a box to say the person pays Scottish Income Tax ([who pays](https://www.gov.uk/scottish-income-tax/who-pays)).
- **Tell HMRC about a move.** A person who moves to or from Scotland must tell HMRC of the new address, or tax may be taken at the wrong rate ([if you move](https://www.gov.uk/scottish-income-tax/if-you-move-to-or-from-scotland)).
- **Payments on account** are half of last year's Self Assessment liability, including Class 4 NIC. Student loan and capital gains are paid with the balancing payment, not in payments on account. See `uk-payments-on-account`.

## Penalties and interest

The UK Self Assessment regime applies unchanged ([penalties](https://www.gov.uk/self-assessment-tax-returns/penalties)).

- **Late return:** £100 at once; after 3 months, £10 a day up to £900; after 6 months, the greater of 5% of the tax due and £300; after 12 months, another 5% or £300.
- **Late payment:** 5% of the tax unpaid at 30 days, 6 months and 12 months.
- **Late payment interest:** Bank of England base rate plus 4% from 6 April 2025. The rate is 7.75% from 9 January 2026 ([HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)).
- **Failure to notify:** registering after 5 October and not paying in full by 31 January can bring a failure-to-notify penalty based on the tax unpaid.
- **Wrong status.** Filing as a rest-of-UK taxpayer when the person is Scottish (or the reverse) understates or overstates the tax. Correct it by amending the return. Inaccuracy penalties are out of scope here: refer.

## Cross-border points

- **Non-residents are never Scottish taxpayers.** Scottish status needs UK residence for the year (s 80D(1)(a)). Decide residence first with `uk-statutory-residence-test`.
- **Split year.** Scottish status still applies for the whole tax year. In a year the person becomes or stops being UK resident, split-year treatment under the statutory residence test decides how much of that year's income is charged at Scottish rates ([STTG4100](https://www.gov.uk/hmrc-internal-manuals/scottish-taxpayer-technical-guidance/sttg4100)). Refer split-year Scottish cases for review.
- **Moving within the UK.** Status is all or nothing for the year (s 80E(3)(c) and s 80F compare time or days across the whole year; HMRC's example of a mid-year move from Birmingham to Aberdeen is in [STTG4400](https://www.gov.uk/hmrc-internal-manuals/scottish-taxpayer-technical-guidance/sttg4400)). Example: a person whose only home is in Edinburgh until 30 November 2026 and in London from 1 December 2026 had a Scottish main home for more of 2026/27 than an English one, so is a Scottish taxpayer for the whole of 2026/27.
- **Treaties.** A Scottish taxpayer is a UK resident for treaty purposes. Treaty residence, withholding and foreign tax credit relief follow the UK rules in `uk-non-resident-sa109` and `uk-dividends`.
- **Offshore and mobile workers** with no fixed home use the days test: where they were at midnight ([more than one home](https://www.gov.uk/scottish-income-tax/if-you-live-in-more-than-one-home)). A night on the UK continental shelf, such as on a North Sea rig, is not a day in any part of the UK; Scottish territorial waters (to 12 nautical miles) count as Scotland ([STTG4500](https://www.gov.uk/hmrc-internal-manuals/scottish-taxpayer-technical-guidance/sttg4500)).

## Worked examples

### Example 1: Scottish employee on a salary of GBP 50,000 (2026/27)

Morag lives in Glasgow, her only home. She earns £50,000, has the standard allowance and code S1257L, and has no other income. Taxable income is £50,000 − £12,570 = £37,430, all non-savings.

- Starter: £3,967 × 19% = £753.73.
- Basic: (£16,956 − £3,967) = £12,989 × 20% = £2,597.80.
- Intermediate: (£31,092 − £16,956) = £14,136 × 21% = £2,968.56.
- Higher: (£37,430 − £31,092) = £6,338 × 42% = £2,661.96.
- Income tax: £8,982.05.

A rest-of-UK employee on the same pay would pay £37,430 × 20% = £7,486.00, so Morag pays £1,496.05 more. Employee Class 1 NIC is UK-wide: 8% of (£50,000 − £12,570) = £2,994.40 (`uk-national-insurance`). Between £43,663 and £50,270 of salary her marginal rate is 42% tax plus 8% NIC, 50%, because the Scottish higher rate starts below the UK NIC upper limit.

```oa-check
name: Scottish employee, salary GBP 50,000, 2026/27
inputs:
  salary: 50000
  pa: 12570
steps:
  - taxable: salary - pa
  - starter: min(taxable, 3967) * 0.19
  - basic: (min(taxable, 16956) - 3967) * 0.20
  - intermediate: (min(taxable, 31092) - 16956) * 0.21
  - higher: (min(taxable, 62430) - 31092) * 0.42
  - scottish_tax: starter + basic + intermediate + higher
  - ruk_tax: taxable * 0.20
  - extra_vs_ruk: scottish_tax - ruk_tax
  - employee_nic: (min(salary, 50270) - 12570) * 0.08
expected:
  taxable: 37430
  starter: 753.73
  basic: 2597.80
  intermediate: 2968.56
  higher: 2661.96
  scottish_tax: 8982.05
  ruk_tax: 7486.00
  extra_vs_ruk: 1496.05
  employee_nic: 2994.40
```

### Example 2: Scottish sole trader, profit GBP 40,000 plus GBP 5,000 dividends (2026/27)

Callum lives in Aberdeen. His 2026/27 trading profit is £40,000 and he receives £5,000 of UK dividends. No PAYE, no pension or Gift Aid.

- **Non-savings first.** The allowance is set against the profit: £40,000 − £12,570 = £27,430 taxable at Scottish rates.
  - Starter £753.73; basic £2,597.80; intermediate (£27,430 − £16,956) = £10,474 × 21% = £2,199.54.
  - Scottish tax on profit: £5,551.07.
- **Dividends at UK rates in the UK bands.** The UK basic rate band is £37,700. The profit uses £27,430 of it, leaving £10,270. All £5,000 of dividends fit in it. The first £500 is the dividend allowance at 0%; £4,500 × 10.75% = £483.75.
- **Edge case.** His total taxable income of £32,430 is above the Scottish higher rate limit of £31,092, yet none of it is taxed at 42%. The dividends sit in the UK basic rate band, and the profit alone (£27,430) stops in the intermediate band.
- **Class 4 NIC:** 6% of (£40,000 − £12,570) = £1,645.80.
- **Total Self Assessment liability:** £5,551.07 + £483.75 + £1,645.80 = £7,680.62. If he had no payments on account, he pays this by 31 January 2028, plus a first 2027/28 payment on account of £3,840.31, with a second £3,840.31 by 31 July 2028.

```oa-check
name: Scottish sole trader, profit 40,000 and dividends 5,000, 2026/27
inputs:
  profit: 40000
  dividends: 5000
  pa: 12570
steps:
  - nsi_taxable: profit - pa
  - starter: min(nsi_taxable, 3967) * 0.19
  - basic: (min(nsi_taxable, 16956) - 3967) * 0.20
  - intermediate: (min(nsi_taxable, 31092) - 16956) * 0.21
  - scottish_tax: starter + basic + intermediate
  - uk_basic_room: 37700 - nsi_taxable
  - div_in_basic: min(dividends, uk_basic_room)
  - div_tax: (div_in_basic - 500) * 0.1075
  - class4: (min(profit, 50270) - 12570) * 0.06
  - total_sa: scottish_tax + div_tax + class4
  - poa_each: total_sa / 2
expected:
  nsi_taxable: 27430
  scottish_tax: 5551.07
  uk_basic_room: 10270
  div_tax: 483.75
  class4: 1645.80
  total_sa: 7680.62
  poa_each: 3840.31
```

## Ask the client first

1. Where was your only or main home during the tax year, and did that change? Give the dates of any move.
2. Do you have homes in more than one part of the UK? Where do your partner, possessions, GP and bank registration sit?
3. If you have no fixed home (offshore, mobile or student), roughly how many midnights did you spend in Scotland and in each other part of the UK?
4. Were you UK resident for the whole year, or did you arrive or leave?
5. What does your tax code start with (S, C or neither)?
6. Did you pay into a personal pension under relief at source, or make Gift Aid donations? (They extend the Scottish bands only if you claim.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Scotland Act 1998 s 80C (Scottish rate resolution) | https://www.legislation.gov.uk/ukpga/1998/46/section/80C | 2026-10-23 |
| Scotland Act 1998 s 80D (Scottish taxpayers) | https://www.legislation.gov.uk/ukpga/1998/46/section/80D | 2026-10-23 |
| Scotland Act 1998 s 80E (close connection) | https://www.legislation.gov.uk/ukpga/1998/46/section/80E | 2026-10-23 |
| Scotland Act 1998 s 80F (days in Scotland) | https://www.legislation.gov.uk/ukpga/1998/46/section/80F | 2026-10-23 |
| Scottish Parliament, motion S6M-20844, Scottish Rate Resolution 2026-27 (agreed) | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 | 2026-10-23 |
| Scottish Government, Scottish Rate Resolution 2026 to 2027: draft motion | https://www.gov.scot/publications/scottish-rate-resolution-2026-2027-draft-motion-explanatory-note/pages/2/ | 2026-10-23 |
| Scottish Government, Scottish Income Tax rates and bands 2026 to 2027 | https://www.gov.scot/publications/scottish-income-tax-rates-and-bands/pages/2026-to-2027/ | 2026-10-23 |
| Income Tax Act 2007 s 11A (income charged at Scottish rates) | https://www.legislation.gov.uk/ukpga/2007/3/section/11A | 2026-10-23 |
| Income Tax Act 2007 s 10 (UK basic, higher, additional rates) | https://www.legislation.gov.uk/ukpga/2007/3/section/10 | 2026-10-23 |
| Income Tax Act 2007 s 13 (dividend rates; s 13(5) for Scottish taxpayers) | https://www.legislation.gov.uk/ukpga/2007/3/section/13 | 2026-10-23 |
| Income Tax Act 2007 s 8 (dividend ordinary, upper and additional rates) | https://www.legislation.gov.uk/ukpga/2007/3/section/8 | 2026-10-23 |
| GOV.UK, Scottish Income Tax: who pays (S codes, SA return box) | https://www.gov.uk/scottish-income-tax/who-pays | 2026-10-23 |
| Income Tax Act 2007 s 414 (Gift Aid relief) | https://www.legislation.gov.uk/ukpga/2007/3/section/414 | 2026-10-23 |
| Finance Act 2004 s 192 (relief at source) | https://www.legislation.gov.uk/ukpga/2004/12/section/192 | 2026-10-23 |
| HMRC Scottish Taxpayer Technical Guidance STTG4100, STTG4400, STTG4500 | https://www.gov.uk/hmrc-internal-manuals/scottish-taxpayer-technical-guidance/sttg4100 | 2026-10-23 |
| HMRC Pensions Tax Manual PTM044220 | https://www.gov.uk/hmrc-internal-manuals/pensions-tax-manual/ptm044220 | 2026-10-23 |
| GOV.UK, Scottish Income Tax (2026/27 and 2025/26 tables, who pays, main home, moving) | https://www.gov.uk/scottish-income-tax | 2026-10-23 |
| GOV.UK, Tax codes | https://www.gov.uk/tax-codes | 2026-10-23 |
| HMRC, Rates and thresholds for employers 2026 to 2027 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-10-23 |
| GOV.UK, Self Assessment penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-10-23 |
| GOV.UK, Payments on account | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-10-23 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-23 |
| GOV.UK, Income Tax rates and Personal Allowances (taper) | https://www.gov.uk/income-tax-rates | 2026-10-23 |
| Finance Act 2026 s 4 (dividend ordinary and upper rates from 2026-27) | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-10-23 |

Not yet confirmed: the SA100 and SA100 notes box wording for Scottish status (the form itself was not read); the rest of HMRC's Scottish Taxpayer Technical Guidance (only STTG4100, 4400 and 4500 were read); whether the Scottish Parliament has set separate Scottish property rates for 2027/28 under s 80C(2B).

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
