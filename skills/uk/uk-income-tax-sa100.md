---
name: uk-income-tax-sa100
description: "UK Income Tax for individuals who file the SA100 Self Assessment return, tax year 2026-27 (6 April 2026 to 5 April 2027), with 2025-26 figures for returns filed now. Covers the GBP 12,570 Personal Allowance and its taper above GBP 100,000, the frozen bands and the 20%, 40% and 45% rates, the Welsh rates, the six Scottish bands for 2026-27, the starting rate for savings and the Personal Savings Allowance, the dividend allowance and rates, Marriage Allowance, the High Income Child Benefit Charge, who must file, Tax-Free Childcare adjusted net income and pension gross-up, registration by 5 October, the 31 October and 31 January deadlines, penalties and late payment interest. Trigger on: SA100, personal allowance taper, income tax bands 2026-27, Scottish income tax, marriage allowance, child benefit charge, register for self assessment, late tax return penalty. Out of scope: uk-self-employment-sa103, uk-rental-sa105, uk-capital-gains-sa108, uk-national-insurance, uk-statutory-residence-test, uk-dividends, uk-scottish-income-tax, uk-payments-on-account."
version: 2.5
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# UK Income Tax for individuals: the SA100 Self Assessment return (2026-27)

The UK tax year runs from 6 April to 5 April. The year in force is 2026-27 (6 April 2026 to 5 April 2027). The returns being filed now are for 2025-26, due online by 31 January 2027. Where a figure differs between the two years, both are given. Do not use these computations for 2027-28 without a fresh year-specific check.

This skill sets out the income tax computation and the filing rules. It points to the other UK skills and does not repeat them:

- Sole trader profits, the trading allowance and Class 4 figures: `uk-self-employment-sa103`.
- Rental profits, finance costs and the property allowance: `uk-rental-sa105`.
- Capital gains: `uk-capital-gains-sa108`.
- National Insurance: `uk-national-insurance`.
- Residence and split years: `uk-statutory-residence-test` (and `uk-non-resident-sa109` for the SA109 pages).
- Dividend planning and director pay: `uk-dividends`.
- Scottish taxpayer status tests and S codes in depth: `uk-scottish-income-tax`.
- Payments on account in depth: `uk-payments-on-account`.

## Who this applies to

Use for a UK-resident individual after establishing Personal Allowance entitlement. For non-residence, split years, foreign income, trusts, estates or uncertain Scottish/Welsh status: Check this point with one of our partner accountants. Load `uk-statutory-residence-test`, `uk-non-resident-sa109` and, for Scottish status, `uk-scottish-income-tax`.

Scottish and Welsh status affects non-savings income; savings and dividends use UK rates. Scottish PAYE codes start with S, Welsh codes with C. Multiple homes, day-count tests and moves during the year need a status determination, not a rate inferred from today's address ([Scotland](https://www.gov.uk/scottish-income-tax/who-pays); [Wales](https://www.gov.uk/welsh-income-tax)).

For 2025-26, HMRC requires a return for a sole trader earning over GBP 1,000 before reliefs, a business partner, someone with CGT to pay, someone paying the Child Benefit charge outside PAYE, an off-payroll worker repaying a student/postgraduate loan, or anyone asked by HMRC to file. Untaxed rent, tips, interest, dividends and foreign income can also require one ([who must file](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return)). A notice to file must not be ignored; seek withdrawal from HMRC if no return is needed.

Dividends over GBP 10,000 require Self Assessment. Up to and including GBP 10,000, someone already filing reports dividends on the return; someone not filing who owes dividend tax tells HMRC after 5 April and before 5 October, by requesting a tax-code change or contacting HMRC. Do not assume exactly GBP 10,000 requires a return for this reason alone ([report dividends](https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal Allowance (ITA 2007 s.35(1); FA 2021 s.5 as amended by FA 2026 s.10) | GBP 12,570, frozen to 2030-31 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/10 |
| Personal Allowance taper (ITA 2007 s.35(2)) | Reduced by half the adjusted net income over GBP 100,000; nil at GBP 125,140 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/35 ; https://www.gov.uk/income-tax-rates |
| Basic rate limit (ITA 2007 s.10(5); FA 2021 s.5 as amended by FA 2026 s.10) | GBP 37,700, frozen to 2030-31 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/10 |
| Higher rate limit (ITA 2007 s.10(5A)) | GBP 125,140 (computed: 2 x 12,570 + 100,000) | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/10 ; https://www.gov.uk/income-tax-rates |
| Main rates, England and NI: basic, higher, additional (FA 2026 s.2) | 20%, 40%, 45% | 2026-27 (same in 2025-26) | https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| Bands with the standard allowance, England, Wales and NI | 0% to 12,570; 20% 12,571 to 50,270; 40% 50,271 to 125,140; 45% over 125,140 | 2025-26 and 2026-27 | https://www.gov.uk/income-tax-rates |
| Welsh rates, 2026-27 (Government of Wales Act 2006 s.116D; Welsh rate resolution NDM9117, agreed 27 January 2026) | Welsh rate 10p in each band, so the same bands and rates as England (20%, 40%, 45%) | 2026-27 | https://record.senedd.wales/Motion/9117 ; https://www.gov.uk/welsh-income-tax |
| Scottish starter rate (ITA 2007 s.11A; Scottish Rate Resolution S6M-20844, agreed 19 February 2026: 19% on the first GBP 3,967 above the allowance) | 19% on GBP 12,571 to 16,537 (2025-26: 12,571 to 15,397) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 ; https://www.gov.uk/scottish-income-tax ; https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Scottish basic rate (S6M-20844: above GBP 3,967 up to 16,956 above the allowance) | 20% on GBP 16,538 to 29,526 (2025-26: 15,398 to 27,491) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 ; https://www.gov.uk/scottish-income-tax ; https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Scottish intermediate rate (S6M-20844: above GBP 16,956 up to 31,092) | 21% on GBP 29,527 to 43,662 (2025-26: 27,492 to 43,662) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 ; https://www.gov.uk/scottish-income-tax ; https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Scottish higher rate (S6M-20844: above GBP 31,092 up to 62,430) | 42% on GBP 43,663 to 75,000 (same in 2025-26) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 ; https://www.gov.uk/scottish-income-tax ; https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Scottish advanced rate (S6M-20844: above GBP 62,430 up to 125,140) | 45% on GBP 75,001 to 125,140 (same in 2025-26) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 ; https://www.gov.uk/scottish-income-tax ; https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Scottish top rate (S6M-20844) | 48% over GBP 125,140 (same in 2025-26) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 ; https://www.gov.uk/scottish-income-tax ; https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year |
| Savings rates (FA 2026 s.3(2)) | 20%, 40%, 45% | 2026-27 (same in 2025-26) | https://www.legislation.gov.uk/ukpga/2026/11/section/3 |
| Starting rate limit for savings (ITA 2007 s.12(3); FA 2026 s.9) | GBP 5,000 at 0%, frozen 2026-27 to 2030-31 | 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/9 |
| Starting rate entry point | With the standard allowance, other income excluding savings/dividends under GBP 17,570; each GBP 1 over the Personal Allowance cuts the GBP 5,000 by GBP 1 | 2026-27 | https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free |
| Personal Savings Allowance (ITA 2007 s.12B) | GBP 1,000 basic rate; GBP 500 higher rate; nil additional rate | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/12B |
| Dividend allowance (dividend nil rate band, ITA 2007 s.13A) | GBP 500 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/13A |
| Dividend ordinary, upper, additional rates (ITA 2007 s.8 as amended by FA 2026 s.4) | 10.75%, 35.75%, 39.35% (2025-26: 8.75%, 33.75%, 39.35%) | 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/4 ; https://www.legislation.gov.uk/ukpga/2007/3/section/8 |
| Marriage Allowance transferable amount (ITA 2007 s.55B(4)-(5)) | 10% of the Personal Allowance rounded up to GBP 10: GBP 1,260; tax cut up to GBP 252 | 2025-26 and 2026-27 | https://www.gov.uk/marriage-allowance |
| High Income Child Benefit Charge (ITEPA 2003 s.681C) | 1% of Child Benefit per GBP 200 of adjusted net income over GBP 60,000; 100% at GBP 80,000 (computed: 60,000 + 100 x 200) | 2024-25 onwards | https://www.legislation.gov.uk/ukpga/2003/1/section/681C |

The resolution limits are amounts of income above the Personal Allowance; with the standard GBP 12,570 allowance they give the bands in the table, which match HMRC's [Scottish Income Tax](https://www.gov.uk/scottish-income-tax) page. The 2025-26 main bands come from GOV.UK's previous tax years page, which states the 2025-26 Personal Allowance was GBP 12,570 and the higher rate started on income over GBP 50,270 ([Income Tax rates: previous tax years](https://www.gov.uk/income-tax-rates/previous-tax-years)).


These whole-pound income ranges are a quick reference with the standard allowance. Apply taper and band extensions in the computation. Scottish/Welsh pension relief and allowance allocation: Check this point with one of our partner accountants.

## The taxable base

**Step 1: total income, split into three kinds.** Employment, pensions, trade and property profits are non-savings income; interest is savings income; dividends are separate. Compute profits with `uk-self-employment-sa103` and `uk-rental-sa105`. ISA interest and dividends are not taxable. HMRC splits joint-account interest equally; contact HMRC if a different split is appropriate ([interest](https://www.gov.uk/apply-tax-free-interest-on-savings); [dividends](https://www.gov.uk/tax-on-dividends)).

**Step 2: reliefs deducted from income.** Deduct only reliefs to which the individual is entitled, such as eligible trading losses or pension payments made gross without prior relief. Do not deduct net-pay pension contributions twice. Eligibility, limits, loss ordering and unusual allowance allocation: Check this point with one of our partner accountants.

**Step 3: adjusted net income (ITA 2007 s.58).** Take total taxable income less those reliefs, then also deduct grossed-up Gift Aid and grossed-up relief-at-source pension contributions. Add back any relief for trade-union or police-organisation superannuation, life-insurance or funeral-benefit payments deducted in arriving at net income. Include taxable savings and dividends even where a nil rate applies. Foreign income and FIG claims need specialist treatment ([adjusted net income](https://www.gov.uk/guidance/adjusted-net-income); [s.58](https://www.legislation.gov.uk/ukpga/2007/3/section/58)).

**Relief-at-source gross-up.** With relief at the basic 20% rate, gross contribution = net payment / 0.8; net payment = gross contribution x 0.8. An eligible GBP 8,000 net payment therefore gives GBP 10,000 gross. Use the gross figure for ANI and band extension, not a second deduction from taxable salary. Net-pay and salary-sacrifice arrangements are different. Pension eligibility, annual/money-purchase/tapered allowances, carry-forward, contribution timing and any pension charge: Check this point with one of our partner accountants ([HMRC pension relief](https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief); [FA 2004 s.192](https://www.legislation.gov.uk/ukpga/2004/12/section/192)). Grossed-up qualifying Gift Aid likewise equals the net donation x 1.25; Gift Aid qualification, sufficient tax and carry-back elections: Check this point with one of our partner accountants.

**Step 4: the Personal Allowance.** GBP 12,570, reduced by half of the adjusted net income over GBP 100,000. A result that is not a whole pound rounds up (ITA 2007 s.35(2)-(3)). The allowance is nil at GBP 125,140 or more. The general formula is max(0, ceil(12570 - max(0, ANI - 100000) / 2)); round the remaining allowance up, not the reduction ([s.35](https://www.legislation.gov.uk/ukpga/2007/3/section/35)).

**Step 5: extend the bands.** Grossed-up relief-at-source pension contributions and Gift Aid extend the basic rate limit (and the higher rate limit) by the gross amount. This assumes eligible contributions/donations and any required higher-rate-relief claim. Scottish limits have distinct rules: Check this point with one of our partner accountants ([FA 2004 s.192](https://www.legislation.gov.uk/ukpga/2004/12/section/192); [ITA 2007 s.414](https://www.legislation.gov.uk/ukpga/2007/3/section/414)).

**Step 6: tax the income in order.** Non-savings first, savings next, dividends last ([ITA 2007 s.16](https://www.legislation.gov.uk/ukpga/2007/3/section/16)). Relief and allowance allocation must respect the operative year's restrictions; mixed-income optimisation, special highest-slice income and Scottish relief: Check this point with one of our partner accountants.

- Savings may use unused Personal Allowance. The starting rate for savings is 0% on up to GBP 5,000 of savings otherwise charged at basic/default basic rate. Other income above the Personal Allowance reduces that band pound for pound; GBP 17,570 is the cut-off only with the standard GBP 12,570 allowance. Dividends are not that other income. Then apply the Personal Savings Allowance. Its basic/higher/additional classification includes interest and uses the UK-equivalent test for Scottish/Welsh taxpayers, rather than the Scottish marginal rate. Nil-rated interest still occupies tax bands ([savings allowances](https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free); [s.12](https://www.legislation.gov.uk/ukpga/2007/3/section/12); [s.12B](https://www.legislation.gov.uk/ukpga/2007/3/section/12B)).
- Dividends may use unused Personal Allowance. The dividend nil rate applies to the next GBP 500, using basic-band dividends first, then upper-band and additional-band dividends. This occupies bands; it is not a deduction. Use the year's dividend rates ([s.13A](https://www.legislation.gov.uk/ukpga/2007/3/section/13A)). The GOV.UK 2026-27 example has wages GBP 29,570 and dividends GBP 3,000: GBP 17,000 wages at 20% = GBP 3,400; GBP 500 dividends at nil and GBP 2,500 at 10.75% = GBP 268.75 ([dividends](https://www.gov.uk/tax-on-dividends)).

**Step 7: Marriage Allowance.** The transferor gives up GBP 1,260; the recipient gets a tax reduction up to GBP 252. For the ordinary UK-resident route, there must be a valid election by a person entitled to Personal Allowance, married/in a civil partnership with the recipient for all or part of the relevant year and when electing (death cases need separate treatment). Neither can be liable above the permitted basic-rate categories, or above intermediate in Scotland, testing the transferor after reducing their allowance. Test dividend nil-rate income as if that nil rate did not apply: a nil dividend tax bill does not by itself establish eligibility. Neither can claim Married Couple's Allowance. Compare the couple's tax after any extra tax on the transferor ([s.55B](https://www.legislation.gov.uk/ukpga/2007/3/section/55B); [s.55C](https://www.legislation.gov.uk/ukpga/2007/3/section/55C)).

Backdating is limited to four years after the relevant tax year; on 26 November 2026 the earliest year is 2022-23 (6 April 2022). A current-year election continues only while conditions remain met and no withdrawal/cessation rule applies; an election made after year-end or after a death applies only to the specified year. Death, non-residence and cancellation timing: Check this point with one of our partner accountants ([s.55D](https://www.legislation.gov.uk/ukpga/2007/3/section/55D); [Marriage Allowance](https://www.gov.uk/marriage-allowance)).

**Step 8: High Income Child Benefit Charge.** From 2024-25, including 2025-26 and 2026-27, ANI must exceed GBP 60,000. For each relevant week, the recipient is charged if no partner throughout that week has higher annual ANI; a partner is charged instead if their ANI is higher than the recipient's. Equal ANI leaves the recipient liable. Partner means spouse, civil partner or someone living together as if married/civil partners, excluding permanent separation. Changes during the year, someone else receiving benefit for a child living with the taxpayer, or unclear entitlement: Check this point with one of our partner accountants ([s.681B](https://www.legislation.gov.uk/ukpga/2003/1/section/681B); [HMRC overview](https://www.gov.uk/child-benefit-tax-charge)).

The percentage is min(100, floor((ANI - 60000) / 200)) when liable; round the relevant benefit total and resulting charge down to whole pounds as required by s.681C. At GBP 80,000 ANI the charge reaches 100%. Use benefit for the relevant weeks, not automatically the full family annual award ([s.681C](https://www.legislation.gov.uk/ukpga/2003/1/section/681C)).

PAYE is an option for the current/previous year if no return is required for another reason and registration is on or before 31 January after the relevant year: for 2025-26, 31 January 2027. Otherwise use Self Assessment. A person previously filing only for this charge must contact HMRC to leave Self Assessment and register for PAYE ([PAYE conditions](https://www.gov.uk/child-benefit-tax-charge/pay-tax-charge-paye)). Opting out of benefit payments avoids the charge for those payments while remaining registered preserves NI credits subject to the credit conditions; historic payments still need reconciliation ([HMRC overview](https://www.gov.uk/child-benefit-tax-charge)).

**Tax-Free Childcare is a separate ANI test.** At each declaration/reconfirmation, a UK-resident parent must not expect their own ANI, including foreign income, to exceed GBP 100,000 in the tax year containing that declaration. The same limit applies separately to their partner, not to their combined income. Exactly GBP 100,000 passes this upper-income test; either person over it fails. This is not a taper ([eligibility reg.15](https://www.legislation.gov.uk/uksi/2015/448/regulation/15); [HMRC TFC11050](https://www.gov.uk/hmrc-internal-manuals/tax-free-childcare-technical-manual/tfc11050)).

Meeting that income test alone does not establish entitlement. Establish the child's age/disability and living arrangements, both adults' work and minimum-earnings tests and any exceptions, immigration/NI-number conditions, approved childcare provider, conflicting support (including Universal Credit, vouchers and childcare grants/bursaries), and ongoing reconfirmation. Details must be reconfirmed every three months. For the full eligibility decision, exceptions or cross-border circumstances: Check this point with one of our partner accountants ([all eligibility tests](https://www.gov.uk/tax-free-childcare/check-if-youre-eligible); [reconfirmation](https://www.gov.uk/tax-free-childcare)).

For the reported 2026-27 question, salary GBP 110,000 with no other income/ANI adjustments would require GBP 10,000 gross = GBP 8,000 net of eligible relief-at-source contributions to bring ANI to GBP 100,000. This is conditional arithmetic, not a promise of Childcare eligibility or pension relief. Include benefits, interest, dividends, partner income and other ANI adjustments before deciding; contribution eligibility/timing and the other Childcare gates remain on hold.

**Step 9: take off tax already paid.** Reconcile PAYE, any creditable tax deducted and payments on account to the calculated bill. Keep NIC, CGT, student loans and other charges separate until their own rules have been checked. Losses route to `uk-self-employment-sa103`, `uk-rental-sa105` and `uk-capital-gains-sa108`.

## Deadlines and filing

These are ordinary individual-return deadlines, subject to the late-notice rules below. HMRC must receive the return/payment; unknown final profit does not remove the filing duty ([HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)).

| Event | 2025-26 | 2026-27 | Source |
|---|---|---|---|
| Notify liability if required under TMA s.7 | 5 October 2026 | 5 October 2027 | https://www.legislation.gov.uk/ukpga/1970/9/section/7 |
| Paper return | 31 October 2026 | 31 October 2027 | https://www.legislation.gov.uk/ukpga/1970/9/section/8 |
| Online return | 31 January 2027 | 31 January 2028 | https://www.legislation.gov.uk/ukpga/1970/9/section/8 |
| Balance and first next-year payment on account, where due | 31 January 2027 | 31 January 2028 | https://www.gov.uk/understand-self-assessment-bill/payments-on-account |
| Second next-year payment on account, where due | 31 July 2027 | 31 July 2028 | https://www.gov.uk/understand-self-assessment-bill/payments-on-account |

For 2025-26, tell HMRC by 5 October 2026 if a return is needed and either no return has been sent before, or registration existed but no 2024-25 return was needed. For later years establish the actual notification duty; do not reuse the 2024-25 reactivation test indefinitely ([HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)).

A notice after 31 July but on/before 31 October gives three months for paper filing, while online stays 31 January. A notice after 31 October gives three months for either method. The balance moves to three months after notice only where the required s.7 notification was within six months after year-end and the s.8/8A notice arrived after 31 October; otherwise the ordinary balance date remains ([TMA s.8](https://www.legislation.gov.uk/ukpga/1970/9/section/8); [s.59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B)).

For tax-code collection, the ordinary online cut-off is 30 December 2026 for 2025-26 (30 December 2027 for 2026-27). Amount limits, sufficient PAYE income and collection capacity must also be established: Check this point with one of our partner accountants ([HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)).

Payments on account are normally half the preceding relevant bill each, excluding tax already paid outside Self Assessment. They are not required if that bill is under GBP 1,000 or more than 80% of the tax was paid outside Self Assessment. Exactly 80% is not the exemption. NIC, exclusions and reduction claims need `uk-payments-on-account`; do not treat total SA cash due as the relevant base automatically ([HMRC](https://www.gov.uk/understand-self-assessment-bill/payments-on-account); [TMA s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A)).

Online filing uses HMRC services or commercial software. Year-specific form entries, registration/reactivation, MTD digital records, quarterly updates, exemptions and software routing: Check this point with one of our partner accountants. See `uk-self-employment-sa103` and `uk-bookkeeping`.

## Penalties and interest

For an ordinary 2025-26 return under the existing annual-return regime:

| Failure | Ordinary penalty, subject to notices/defences and applicable regime | Source |
|---|---|---|
| Return late | Initial GBP 100, even if no tax due | https://www.gov.uk/self-assessment-tax-returns/penalties |
| Failure continues after three months | GBP 10/day for up to 90 days, only if HMRC decides and gives notice specifying the start date | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/4 |
| Failure continues after six months | Greater of 5% of liability that would be shown in the return and GBP 300 | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/5 |
| Failure continues after twelve months, not deliberate withholding | Further greater of 5% of liability that would be shown and GBP 300 | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/6 |
| Tax paid late under ordinary regime | 5% at 30 days, six months and twelve months on the relevant unpaid tax | https://www.gov.uk/self-assessment-tax-returns/penalties |
| Ordinary late-payment interest | 8.00% from 24 November 2026; use actual period-specific rates | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

Failure-to-notify penalties, deliberate/concealed withholding, partnership returns, reasonable excuse, special reduction, payment arrangements, appeals and notice/payment deadlines: Check this point with one of our partner accountants. Do not calculate a penalty from elapsed time alone.

For MTD taxpayers, establish which year and penalty regime applies before using this table. MTD points, quarterly-update treatment, first-year grace, late-payment percentages, payments-on-account exclusions and repayment-interest calculations: Check this point with one of our partner accountants ([MTD penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax)). Current interest is not a rate promised for the future January filing/payment date.

## Cross-border points

For non-residents, split years, treaty/foreign-tax-credit relief, foreign income/FIG, Personal Allowance or Marriage Allowance residence conditions, or Scottish/Welsh multi-home/moving status: Check this point with one of our partner accountants. Use `uk-statutory-residence-test`, `uk-non-resident-sa109`, `uk-foreign-tax-and-withholding`, `uk-non-dom` and `uk-scottish-income-tax`. Exit-planning routes remain `uk-to-uae-relocation-tax` and `uk-to-italy-flat-tax-relocation`.

Trust/estate and partnership income, pension charges, Winter Fuel Payment recovery, termination/redundancy pay and non-cash benefits need separate treatment: Check this point with one of our partner accountants. For 2027-28 savings/property rates and allowance order, use a fresh year-specific source read; do not apply later rules to these 2025-26/2026-27 cases.

## Worked examples

### Example 1: employee with side business and dividends, England, 2026-27

Assume full Personal Allowance entitlement, no other income, losses, Gift Aid, special charges or prior payments on account. Trade profit is already correctly computed. Sarah lives in England. In 2026-27 she earns a salary of GBP 40,000 (PAYE deducted GBP 5,486), makes a sole trader profit of GBP 20,000 and receives UK dividends of GBP 5,000. Her adjusted net income is GBP 65,000, under GBP 100,000, so she keeps the full GBP 12,570 allowance.

Non-savings income is GBP 60,000. After the allowance, GBP 47,430 is taxable. The first GBP 37,700 is taxed at 20% (GBP 7,540) and the remaining GBP 9,730 at 40% (GBP 3,892). Her dividends sit on top, wholly in the higher rate band. The first GBP 500 is at the dividend nil rate. The other GBP 4,500 is taxed at 35.75%: GBP 1,608.75. Total income tax is GBP 13,040.75. After PAYE, GBP 7,554.75 is due through Self Assessment. In 2025-26 the same dividends would have cost GBP 1,518.75 at 33.75%, so the rise costs her GBP 90. The same 2025-26 inputs give total income tax GBP 12,950.75 and GBP 7,464.75 after PAYE. Class 4 National Insurance on the profit is extra: see `uk-national-insurance`.

```oa-check
name: GB 2026-27, England, salary 40000, profit 20000, dividends 5000
inputs:
  salary: 40000
  profit: 20000
  dividends: 5000
  paye: 5486
steps:
  - non_savings: salary + profit
  - taxable_ns: non_savings - 12570
  - basic: min(taxable_ns, 37700) * 0.20
  - higher: (taxable_ns - 37700) * 0.40
  - div_taxed: dividends - 500
  - div_tax: div_taxed * 0.3575
  - total_tax: basic + higher + div_tax
  - due_sa: total_tax - paye
  - div_tax_2025_26: div_taxed * 0.3375
  - rise: div_tax - div_tax_2025_26
expected:
  taxable_ns: 47430
  basic: 7540
  higher: 3892
  div_tax: 1608.75
  total_tax: 13040.75
  due_sa: 7554.75
  rise: 90
```

### Example 2: Personal Allowance taper and the Child Benefit charge, England, 2026-27

Assume full-year UK residence, an eligible relievable pension payment made in the year, the necessary claim, no other income/adjustments or pension charge, and the same lower-income partner throughout every benefit week. Tom lives in England and earns GBP 112,000 of salary in 2026-27. He pays GBP 4,000 into a personal pension under relief at source, so the gross contribution is GBP 5,000. His partner earns less. The family received GBP 1,406 of Child Benefit in the year (take the figure from the award, not an estimate).

Adjusted net income is GBP 112,000 minus GBP 5,000 = GBP 107,000. That is GBP 7,000 over GBP 100,000, so the allowance falls by GBP 3,500 to GBP 9,070. The gross contribution extends his basic rate band to GBP 42,700. Taxable income is GBP 102,930. GBP 42,700 at 20% is GBP 8,540. The other GBP 60,230 at 40% is GBP 24,092. Income tax is GBP 32,632.

His adjusted net income is GBP 47,000 over GBP 60,000. That gives 235%, capped at 100%, so the Child Benefit charge is the full GBP 1,406. Total is GBP 34,038 before PAYE. Subject to relief eligibility and timing, a further gross pension contribution of GBP 7,000 would bring adjusted net income to GBP 100,000 and restore the full allowance; the charge would stay at 100% while adjusted net income is GBP 80,000 or more.

```oa-check
name: GB 2026-27, England, PA taper with relief-at-source pension and HICBC
inputs:
  salary: 112000
  pension_net: 4000
  child_benefit: 1406
steps:
  - pension_gross: pension_net / 0.8
  - ani: salary - pension_gross
  - pa: max(0, ceil(12570 - max(0, ani - 100000) / 2))
  - brb: 37700 + pension_gross
  - taxable: salary - pa
  - basic: min(taxable, brb) * 0.20
  - higher: (taxable - brb) * 0.40
  - income_tax: basic + higher
  - pct: min(100, floor(max(0, ani - 60000) / 200))
  - hicbc: floor(child_benefit * pct / 100)
  - total: income_tax + hicbc
expected:
  pension_gross: 5000
  ani: 107000
  pa: 9070
  taxable: 102930
  income_tax: 32632
  pct: 100
  hicbc: 1406
  total: 34038
```

### Earlier worked cases retained with their original inputs

These compact cases retain the earlier Guide's numbers and years. Assume ordinary full-allowance eligibility and no unstated adjustments; where facts are missing the outcome remains conditional.

- **Case A, England, 2026-27 and 2025-26:** salary GBP 35,000, PAYE GBP 4,486, no other income. GBP 35,000 - GBP 12,570 = GBP 22,430; x 20% = GBP 4,486; balance zero. This alone does not cancel a notice to file.
- **Case B:** the original GBP 40,000 salary, GBP 5,486 PAYE, GBP 20,000 profit and GBP 5,000 dividends are Example 1, including both 2025-26 and 2026-27 results.
- **Case C, 2026-27:** non-savings income GBP 115,000, eligible pension net GBP 8,000 = gross GBP 10,000. ANI GBP 105,000; taper GBP 2,500; allowance GBP 10,070; basic band GBP 47,700; higher-rate entry GBP 57,770. Without that payment, allowance GBP 5,070.
- **Case D, 2026-27:** ANI GBP 70,000, partner lower throughout, relevant benefit GBP 1,800: GBP 10,000 / GBP 200 = 50%; charge GBP 900. At ANI GBP 67,600 the percentage is 38%.
- **Case E, ordinary eligible Marriage Allowance couple:** income GBP 11,500 and GBP 20,000. Before transfer, tax on GBP 7,430 = GBP 1,486. Transfer GBP 1,260: allowance GBP 11,310 for transferor, taxable GBP 190, tax GBP 38; recipient's tax GBP 1,486 - GBP 252 = GBP 1,234 (equivalent to 20% of GBP 6,170). Combined GBP 1,272, equivalent taxable GBP 6,360; saving GBP 214.
- **Case F, 2026-27:** wages GBP 16,000 and interest GBP 200: wages above allowance GBP 3,430; remaining starting band GBP 1,570, so interest tax nil. Separately, a taxpayer eligible for the GBP 1,000 PSA with GBP 1,300 interest taxed wholly within basic band pays GBP 300 x 20% = GBP 60. Do not use a 2027-28 rate here.
- **Case G, 2025-26 first-time filer:** stipulated relevant income-tax bill GBP 13,000 and PAYE GBP 5,000; no exclusions, other credits or previous payments. Balance GBP 8,000; each 2026-27 payment on account GBP 4,000. GBP 12,000 due 31 January 2027, GBP 4,000 on 31 July 2027; any 2026-27 balance normally 31 January 2028.
- **Case H, 2025-26 return:** filing on 20 August 2027, GBP 4,000 liability already paid 31 January 2027. Assume the ordinary 31 January filing deadline, a valid HMRC daily-penalty notice covering all 90 days and no defence/reduction. GBP 100 + GBP 900 + max(GBP 200, GBP 300) = GBP 1,300. Paying the tax on time does not remove the tax-based filing penalty. If those notice/defence facts are unknown: Check this point with one of our partner accountants.

## Ask the client first

- Which tax year: the 2025-26 return being filed now, or 2026-27? The dividend rates differ.
- Where was your main home in the year: England or NI, Wales, or Scotland? Did you move during the year, or spend time outside the UK?
- Have you filed a return before, and did you file for 2024-25? This decides the 5 October registration duty.
- All income by kind: P60 and P11D, self-employment and rental income before expenses, interest outside ISAs, dividends outside ISAs, pensions, foreign income.
- Pension contributions (relief at source or net pay) and Gift Aid. They change adjusted net income, the taper and the Child Benefit charge.
- Married or in a civil partnership, and both partners' incomes? Child Benefit entitlement and payment weeks, relationship changes and each partner's ANI? For Tax-Free Childcare, expected current-year ANI for each adult plus the child, work/earnings, status and other-support facts?

## Sources

| Source and purpose | URL | Read on |
|---|---|---|
| FA 2026 ss.2-4: current main, savings and dividend rates | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-11-26 |
| FA 2026 s.9: starting savings band freeze | https://www.legislation.gov.uk/ukpga/2026/11/section/9 | 2026-11-26 |
| FA 2026 s.10: allowance/basic-limit freeze | https://www.legislation.gov.uk/ukpga/2026/11/section/10 | 2026-11-26 |
| ITA 2007 s.10: limits | https://www.legislation.gov.uk/ukpga/2007/3/section/10 | 2026-11-26 |
| ITA 2007 ss.12,12A,12B: savings nil rates/allowance | https://www.legislation.gov.uk/ukpga/2007/3/section/12B | 2026-11-26 |
| ITA 2007 s.13A: dividend nil rate | https://www.legislation.gov.uk/ukpga/2007/3/section/13A | 2026-11-26 |
| ITA 2007 s.16: income order | https://www.legislation.gov.uk/ukpga/2007/3/section/16 | 2026-11-26 |
| ITA 2007 s.35: allowance and rounding | https://www.legislation.gov.uk/ukpga/2007/3/section/35 | 2026-11-26 |
| ITA 2007 ss.55B-55D: Marriage Allowance | https://www.legislation.gov.uk/ukpga/2007/3/section/55D | 2026-11-26 |
| ITA 2007 s.58: ANI | https://www.legislation.gov.uk/ukpga/2007/3/section/58 | 2026-11-26 |
| FA 2004 s.192 and ITA s.414: band extension | https://www.legislation.gov.uk/ukpga/2004/12/section/192 | 2026-11-26 |
| HMRC ANI method and Gift Aid gross-up | https://www.gov.uk/guidance/adjusted-net-income | 2026-11-26 |
| HMRC current income tax rates | https://www.gov.uk/income-tax-rates | 2026-11-26 |
| HMRC previous-year bands | https://www.gov.uk/income-tax-rates/previous-tax-years | 2026-11-26 |
| Scottish Rate Resolution 2026-27; exact limits checked | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 | 2026-11-26 |
| Welsh 2026-27 resolution; completed independent vote review reused | https://record.senedd.wales/Motion/9117 | 2026-11-26 |
| HMRC Scottish current and previous-year bands | https://www.gov.uk/scottish-income-tax | 2026-11-26 |
| HMRC Scottish 2025-26 bands | https://www.gov.uk/scottish-income-tax/2025-to-2026-tax-year | 2026-11-26 |
| HMRC Welsh rates/status | https://www.gov.uk/welsh-income-tax | 2026-11-26 |
| HMRC interest treatment | https://www.gov.uk/apply-tax-free-interest-on-savings | 2026-11-26 |
| HMRC savings allowances | https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free | 2026-11-26 |
| HMRC dividend rates and example | https://www.gov.uk/tax-on-dividends | 2026-11-26 |
| HMRC dividend reporting | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends | 2026-11-26 |
| HMRC Marriage Allowance | https://www.gov.uk/marriage-allowance | 2026-11-26 |
| ITEPA 2003 ss.681B-681C: benefit liability and rounding | https://www.legislation.gov.uk/ukpga/2003/1/section/681C | 2026-11-26 |
| HMRC Child Benefit and PAYE conditions | https://www.gov.uk/child-benefit-tax-charge/pay-tax-charge-paye | 2026-11-26 |
| HMRC Child Benefit overview/opt-out | https://www.gov.uk/child-benefit-tax-charge | 2026-11-26 |
| Childcare Eligibility reg.15: upper income test | https://www.legislation.gov.uk/uksi/2015/448/regulation/15 | 2026-11-26 |
| HMRC TFC11050: declaration-year ANI | https://www.gov.uk/hmrc-internal-manuals/tax-free-childcare-technical-manual/tfc11050 | 2026-11-26 |
| HMRC Childcare eligibility tests | https://www.gov.uk/tax-free-childcare/check-if-youre-eligible | 2026-11-26 |
| HMRC Childcare reconfirmation | https://www.gov.uk/tax-free-childcare | 2026-11-26 |
| HMRC pension relief and gross-up conditions | https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief | 2026-11-26 |
| HMRC return requirement | https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return | 2026-11-26 |
| HMRC filing deadlines | https://www.gov.uk/self-assessment-tax-returns/deadlines | 2026-11-26 |
| TMA s.7: notification; completed SA103 read reused | https://www.legislation.gov.uk/ukpga/1970/9/section/7 | 2026-11-26 |
| TMA s.8: ordinary/late-notice filing; completed SA103 read reused | https://www.legislation.gov.uk/ukpga/1970/9/section/8 | 2026-11-26 |
| TMA s.59B: balance/late notice; completed SA103 read reused | https://www.legislation.gov.uk/ukpga/1970/9/section/59B | 2026-11-26 |
| TMA s.59A: payments on account | https://www.legislation.gov.uk/ukpga/1970/9/section/59A | 2026-11-26 |
| HMRC payments on account | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-11-26 |
| HMRC ordinary penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-11-26 |
| FA 2009 Sch.55 paras.4-6: notices/liability base | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/4 | 2026-11-26 |
| HMRC interest: completed UKVAT/SA103 exact announced sentence reused; effective-date applicability confirmed 26 November | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-22 |

Not yet confirmed: none within the conditional computations above. Referred specialist outcomes are not usable determinations.
