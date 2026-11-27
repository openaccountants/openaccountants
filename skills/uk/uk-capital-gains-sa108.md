---
name: uk-capital-gains-sa108
description: Use this skill whenever asked about UK capital gains tax for individuals. Trigger on phrases like "SA108", "capital gains tax", "CGT UK", "annual exempt amount", "disposal", "chargeable gain", "crypto CGT UK", "share sale UK", "property disposal CGT", "PPR relief", "principal private residence", "BADR", "BADR 18%", "Business Asset Disposal Relief", "Entrepreneurs' Relief", "Investors Relief 18%", "carried interest April 2026", "CGT 18% 24%", "bed and breakfasting", "30-day rule", "Section 104 pool", "negligible value claim", "CGT losses", "60-day reporting", "residential property CGT", or any question about computing, filing, or reporting capital gains on the UK Self Assessment return. Covers SA108 form, CGT rates, reliefs, crypto as CGT asset, share matching rules, property CGT reporting, and loss treatment. ALWAYS read this skill before touching any UK CGT work.
version: 2.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - uk-income-tax-sa100
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# UK Capital Gains Tax for individuals and the SA108 pages

## Scope and who this is for

Compute individuals’ UK CGT for 2026/27 (6 April 2026–5 April 2027), and complete **2025/26** returns on the SA108 labelled **2026**. Keep the 2024/25 split rates for amendments. This covers ordinary shares, investment cryptoassets, property, business disposals, losses and reliefs. UK residents are generally chargeable on assets wherever situated, subject to the statutory exceptions ([TCGA s.1A](https://www.legislation.gov.uk/ukpga/1992/12/section/1A)). Non-resident, split-year, temporary non-resident, FIG, remittance/TRF and foreign-tax-credit computations are non-usable here: Check this point with one of our partner accountants.

## Ask the client first

Establish residence and the relevant year; asset and beneficial owner; contract/conditions/completion dates; evidenced proceeds, costs and values; gifts and connections; spouse/separation agreements; same-day and following-30-day purchases; losses and previous relief claims; taxable income and band extensions; home occupation, absences, letting, business use and grounds; business/trading status, employment and ownership rights; and property/real-time returns already submitted. Request missing evidence before computing. Do not invent costs, connection status, dates, residence or relief entitlement; an upper-rate illustration is not a filing calculation.

## The method, step by step

### 1. Select the year, allowance and rate

| Disposal period | Individuals: ordinary gains within unused basic band / above | Residential property | Qualifying BADR / Investors’ Relief | Trustees / personal representatives, ordinary gains | Official source (read 2026-11-27) |
| --- | --- | --- | --- | --- | --- |
| 2026/27 | 18% / 24% | 18% / 24% | 18% | 24% | [TCGA s.1H](https://www.legislation.gov.uk/ukpga/1992/12/section/1H); [FA2025 ss.8–9](https://www.legislation.gov.uk/ukpga/2025/8/section/8); [s.9](https://www.legislation.gov.uk/ukpga/2025/8/section/9) |
| 2025/26 | 18% / 24% | 18% / 24% | 14% | 24% | [HMRC dated rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances); [FA2025 s.8](https://www.legislation.gov.uk/ukpga/2025/8/section/8); [s.9](https://www.legislation.gov.uk/ukpga/2025/8/section/9) |
| 30 October 2024–5 April 2025 | 18% / 24% | 18% / 24% | 10% | 24% | [HMRC dated rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |
| 6 April–29 October 2024 | 10% / 20% | 18% / 24% | 10% | 20%; residential 24% | [HMRC dated rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |

Carried interest is separate: individuals’ rates were 18%/28% in 2024/25 and 32% in 2025/26. From 6 April 2026 HMRC directs it to Income Tax and National Insurance; no SA103/employment box or effective rate is determined here. Check this point with one of our partner accountants. ([Dated rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances); [current regime](https://www.gov.uk/capital-gains-tax/rates).)

| Tax year | Individual annual exempt amount (AEA) | Most other trustees | Official source (read 2026-11-27) |
| --- | --- | --- | --- |
| 2026/27, 2025/26, 2024/25 | £3,000 each year | £1,500 each year | [TCGA s.1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K); [HMRC](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |
| 2023/24 | £6,000 | £3,000 | [HMRC](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |
| 2022/23 | £12,300 | £6,150 | [HMRC](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) |

Trustees for disabled people use the individual amounts. Personal representatives receive the full AEA for the death year and next two tax years during administration; estates/trust computations are otherwise held. An individual’s AEA is for that tax year; it is not transferable or carried forward. No AEA where a foreign gain claim, foreign income claim or foreign employment election is made for that year; old remittance-basis claims can also remove the old-year allowance. ([s.1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K); [HMRC](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances).)

For ordinary 2026/27 gains, use **£37,700**, not £50,270, less taxable income **after** the Personal Allowance/reliefs, allowing applicable band extensions. Deduct current-year allowable losses, then AEA, then eligible brought-forward losses; allocate AEA in the most beneficial way. BADR/IR gains use available basic band first; remaining ordinary gains use 18% within the remaining band and 24% above it. Taxable income already charged at a higher income-tax rate means ordinary gains at 24%. For a 2024/25 amendment/late return, separately check the main-rate adjustment for post-29 October disposals ([HMRC adjustment](https://www.gov.uk/guidance/work-out-your-capital-gains-tax-adjustment-for-the-2024-to-2025-tax-year)). ([s.1I](https://www.legislation.gov.uk/ukpga/1992/12/section/1I); [s.1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K); [HMRC examples](https://www.gov.uk/capital-gains-tax/rates).)

### 2. Establish disposal date, proceeds and costs

Use the unconditional contract date; for a conditional contract use when the condition is satisfied ([s.28](https://www.legislation.gov.uk/ukpga/1992/12/section/28)). **Rate/IR-limit anti-forestalling overrides this timing for the specified purpose**:

| Contract / transfer boundary | Operative treatment | Official source (read 2026-11-27) |
| --- | --- | --- |
| Contract before 30 October 2024; transfer on/after it | Main-rate/IR-limit changes use transfer date unless excluded contract | [FA2025 Sch.2 para.7](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2/paragraph/7) |
| BADR/IR: contract before 30 October 2024; transfer on/after 6 April 2025 | Transfer-date rate unless excluded contract | [Sch.2 para.11](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2/paragraph/11) |
| BADR/IR: contract 30 October 2024–5 April 2025; transfer on/after 6 April 2025 | Transfer-date rate unless excluded contract | [Sch.2 para.12](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2/paragraph/12) |
| BADR/IR: contract during 2025/26; transfer on/after 6 April 2026 | Transfer-date rate unless excluded contract | [Sch.2 para.13](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2/paragraph/13) |

Excluded means no purpose of obtaining an advantage from s.28 and, if connected, wholly commercial reasons. Claim with the prescribed statement unless aggregate gains under all relevant excluded contracts do not exceed **£100,000**; the BADR measure is the s.169N(2) gain. This changes the rate/limit date, not the general tax year of disposal. ([Sch.2 paras.7,14](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2); [CG10250](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg10250).) Reorganisation/exchange elections and unusual straddling contracts are non-usable here: Check this point with one of our partner accountants.

Gain = proceeds less allowable acquisition cost, incidental acquisition/disposal expenses and qualifying enhancement expenditure still reflected in the asset at disposal; no double deduction of income-tax expenses. Maintenance and home loan interest are not enhancement expenditure. Fees/SDLT/SDRT require the statutory purpose and cost test, not merely a bank-payment label. ([s.38](https://www.legislation.gov.uk/ukpga/1992/12/section/38); [s.39](https://www.legislation.gov.uk/ukpga/1992/12/section/39); [HMRC property costs](https://www.gov.uk/tax-sell-property/work-out-your-gain).)

Market value replaces consideration for non-arm’s-length gifts/bargains, subject to specific reliefs. Connected parties are treated as non-arm’s-length; a connected loss is usable only against another disposal to that same person while connected, subject to s.18(4). Connections include spouse/civil partner, siblings, ancestors/descendants and spouses of relevant relatives, relevant partners, controlled companies and settlor/trustee connections; apply the exact s.286 test. Never assume an unknown buyer is connected. ([s.17](https://www.legislation.gov.uk/ukpga/1992/12/section/17); [s.18](https://www.legislation.gov.uk/ukpga/1992/12/section/18); [s.286](https://www.legislation.gov.uk/ukpga/1992/12/section/286).)

Spouse/civil-partner transfers are no gain/no loss while living together. After separation this can continue while still married/civil partners until the earlier of the end of the third tax year following separation and the specified court order/decree; qualifying divorce agreements/orders have a separate limb. Trading-stock and deathbed-gift exclusions apply. **Separation for a whole tax year does not itself establish market-value treatment.** Divorce/agreement classification is held: Check this point with one of our partner accountants. ([s.58](https://www.legislation.gov.uk/ukpga/1992/12/section/58).)

Inherited assets generally take market value at death; death itself is not the deceased’s disposal, and a legatee normally takes the representatives’ acquisition basis. Individuals’ assets held on **31 March 1982** generally rebase to that date. Charity gifts/bargain sales, tainted donations, hold-over/rollover/incorporation relief and part-disposal computations are held rather than automatically exempt or deductible. Check this point with one of our partner accountants. ([s.62](https://www.legislation.gov.uk/ukpga/1992/12/section/62); [s.35](https://www.legislation.gov.uk/ukpga/1992/12/section/35).)

For ordinary tangible movable property, proceeds **not exceeding £6,000** exempt the gain; above this the chargeable gain is capped at five-thirds of the excess. Losses use deemed proceeds of at least £6,000. Aggregate sets sold to the same person, persons acting in concert or connected persons; partial interests, wasting/business assets, currency and terminal-market commodities need separate checks. Check this point with one of our partner accountants. ([s.262](https://www.legislation.gov.uk/ukpga/1992/12/section/262).)

### 3. Match shares and investment tokens

For ordinary shares of the same class, company, owner and capacity, match **same day → next 30 days → Section 104 pool → later unmatched acquisitions, earliest first**. The 30-day rule does not match acquisitions while non-UK-resident **or treaty non-resident**. Day 30 qualifies; day 31 does not qualify under that rule, although another matching limb may apply. Pool cost allocated = shares disposed from pool ÷ pool shares × pool cost; remove that cost and quantity. ([ss.104–105](https://www.legislation.gov.uk/ukpga/1992/12/section/105); [s.104](https://www.legislation.gov.uk/ukpga/1992/12/section/104); [s.106A](https://www.legislation.gov.uk/ukpga/1992/12/section/106A); [HS284](https://www.gov.uk/government/publications/shares-and-capital-gains-tax-hs284-self-assessment-helpsheet/hs284-shares-and-capital-gains-tax-2026).)

HMRC’s share illustration: 100 at 80 p (£80) plus 300 at £1.20 (£360) = 400 costing £440, £1.10 each; 150 pooled shares use £165 cost. Employee/EMI shares, rights/bonus issues, reorganisations, investment funds and accumulation distributions, bed-and-ISA matching and EIS/SEIS/VCT are held: Check this point with one of our partner accountants. ([Share example](https://www.gov.uk/tax-sell-shares/print).)

Investment tokens: sales, swaps, spending and gifts can be disposals; assess spouse/charity exceptions separately. No disposal where beneficial ownership is retained throughout an own-wallet transfer; a mixer returning the same type is not a disposal, but a different type is. Keep each token type in a separate pool with the same-day/30-day priority. Fees, contracts, valuations and pooled costs can qualify; mining equipment/electricity and expenses already deducted against income do not. If token value has already borne Income Tax, do not charge CGT again on that value. ([CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100); [HMRC token computation](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets).)

Keep sterling values, dates, token quantities, bank statements, pool cost/quantity before and after disposals; exchange reports are not tax calculations. Mining, staking, employment receipts, airdrops, forks, DeFi/lending/liquidity pools and trading classification are non-usable until separately established: Check this point with one of our partner accountants. Do not treat every withdrawal as a sale or every airdrop as zero-cost. For earlier unpaid tax, HMRC provides the Cryptoasset Disclosure Service. ([HMRC records](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets).)

### 4. Apply home and business reliefs

**PRR:** establish genuine only/main residence; do not infer full relief from a brief stay. Relief under s.223 covers qualifying residence periods including the final **9 months**, without double counting; ownership for this purpose excludes periods before 31 March 1982. Exclusive business use and acquisition/development with a purpose of realising a gain restrict relief. Grounds ordinarily cover **0.5 hectare including the house**, with a larger area only where required for reasonable enjoyment having regard to size/character. Full relief is possible where the relevant statutory conditions cover the entire gain. ([ss.222–224](https://www.legislation.gov.uk/ukpga/1992/12/section/222); [s.223](https://www.legislation.gov.uk/ukpga/1992/12/section/223); [s.224](https://www.legislation.gov.uk/ukpga/1992/12/section/224).)

**Letting Relief:** only the gain attributable to a period when part was the owner’s main residence and another part was let as residential accommodation; maximum is the lower of qualifying letting gain, PRR and **£40,000**. Whole-house letting without shared occupancy does not satisfy this condition. A lodger sharing living space may not restrict PRR; it is not a general exemption for all room lettings. ([s.223B](https://www.legislation.gov.uk/ukpga/1992/12/section/223B); [HS283](https://www.gov.uk/government/publications/private-residence-relief-hs283-self-assessment-helpsheet/hs283-private-residence-relief-2026).)

Absence relief, delayed occupation, disability/care-home final period, pre-2020 final periods, multiple-home nominations, married couples’ shared residence and overseas residence/day-count rules need their full conditions. No entitlement is inferred from the old short table. Check this point with one of our partner accountants.

| BADR disposal | Ordinary qualifying conditions | Official source (read 2026-11-27) |
| --- | --- | --- |
| Whole or part of a business | Owned throughout 2 years ending with disposal; an isolated asset sale from a continuing business is not itself a sale of part of the business | [s.169I(2)–(3)](https://www.legislation.gov.uk/ukpga/1992/12/section/169I) |
| Assets in use when business ceased | Business owned throughout 2 years to cessation; disposal within 3 years of cessation | [s.169I(4)](https://www.legislation.gov.uk/ukpga/1992/12/section/169I) |
| Ordinary personal-company shares/securities | Throughout 2 years to disposal: personal company, trading company/holding company of trading group, and officer/employee of company or relevant group member | [s.169I(6)](https://www.legislation.gov.uk/ukpga/1992/12/section/169I) |
| Shares after trading cessation | Those conditions throughout 2 years to relevant cessation, with disposal within 3 years | [s.169I(7)](https://www.legislation.gov.uk/ukpga/1992/12/section/169I) |

Personal company requires at least **5% ordinary share capital and voting rights**, plus at least **5% of both distributable profits and winding-up assets**, or the alternative **5% whole-company sale proceeds** test. Exactly 5% can qualify; 1 year 11 months fails the ordinary 2-year test. EMI exceptions, associated disposals/rent, goodwill to close companies, dilution elections, recent business transfers and trustee claims are held: Check this point with one of our partner accountants. ([s.169S](https://www.legislation.gov.uk/ukpga/1992/12/section/169S); [s.169I](https://www.legislation.gov.uk/ukpga/1992/12/section/169I).)

Aggregate relevant gains and losses for the qualifying disposal. BADR lifetime limit is **£1 million**, including relevant earlier individual/trust claims; excess uses normal rates. Claim by **31 January 2028** for 2025/26, **31 January 2029** for 2026/27 (first anniversary of 31 January following disposal year). Spouses’ limits are individual, subject to their own qualification. ([s.169N](https://www.legislation.gov.uk/ukpga/1992/12/section/169N); [s.169M](https://www.legislation.gov.uk/ukpga/1992/12/section/169M); [HS275](https://www.gov.uk/government/publications/entrepreneurs-relief-hs275-self-assessment-helpsheet/hs275-business-asset-disposal-relief-2026).)

**Investors’ Relief:** shares ordinary both at issue and disposal, issued on/after **17 March 2016**, subscribed in cash, fully paid at issue, for genuine commercial reasons at arm’s length without tax-advantage arrangements; none of the issuer’s shares or securities listed at issue, issuer a trading company or holding company of a trading group throughout ownership; continuously held for at least **3 years** (the statutory longer initial period applies to pre-6 April 2016 issues). No relevant employee in the investor/connected-person test. Value received can disqualify shares; mixed holdings need allocation. Officer/employee exceptions and reorganisations require separate application: Check this point with one of our partner accountants. ([s.169VB](https://www.legislation.gov.uk/ukpga/1992/12/section/169VB); [s.169VU](https://www.legislation.gov.uk/ukpga/1992/12/section/169VU); [HS308](https://www.gov.uk/government/publications/investors-relief-2020-hs308/investors-relief-2026-hs308).)

IR has its own lifetime limit: **£1 million** for disposals from **30 October 2024**, **£10 million** before then, subject to the anti-forestalling rule above. Excess uses normal rates. Claims have the same anniversary deadline as BADR. A holding of 2 years 11 months fails the ordinary 3-year condition. ([s.169VK](https://www.legislation.gov.uk/ukpga/1992/12/section/169VK); [s.169VM](https://www.legislation.gov.uk/ukpga/1992/12/section/169VM); [HS308](https://www.gov.uk/government/publications/investors-relief-2020-hs308/investors-relief-2026-hs308).)

### 5. Deduct eligible losses and compute tax

Current-year allowable losses reduce current gains before AEA; brought-forward losses are used only to the AEA level, preserving unused losses. Notify HMRC of the quantified loss, normally within **4 years after the disposal year**; pre-6 April 1996 losses have special treatment. Do not deduct a restricted connected-person loss against ordinary gains. ([s.1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K); [s.16](https://www.legislation.gov.uk/ukpga/1992/12/section/16); [TMA s.43](https://www.legislation.gov.uk/ukpga/1970/9/section/43); [HMRC losses](https://www.gov.uk/capital-gains-tax/losses).)

Negligible value requires an asset still owned which became negligible during ownership, or the qualifying no-gain/no-loss chain condition. A valid claim deems sale/reacquisition at the specified value. An earlier date requires ownership and negligible value at that date and, for CGT, cannot precede the beginning of the claim tax year by more than **2 years**. Loss/destruction/extinction is itself a disposal, subject to the Act. Dissolved-company cases, evidence of negligible value, income share-loss relief and death-year carry-back require separate review: Check this point with one of our partner accountants. ([s.24](https://www.legislation.gov.uk/ukpga/1992/12/section/24).)

## Boundary and exception table

| Boundary | Result or hold | Source (read 2026-11-27) |
| --- | --- | --- |
| Proceeds exactly £50,000; gains not above allowance | Does not meet the “more than £50,000” test; check every other reporting trigger | [2026 notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |
| Full PRR on UK-resident home sale | No CGT payment; no property return where no payment on account; no SA108 solely for that fully relieved disposal | [FA2019 Sch.2 paras.1–5](https://www.legislation.gov.uk/ukpga/2019/1/schedule/2); [2026 notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |
| Non-resident UK land disposal at a loss | Reporting can still be required, subject to excluded-disposal and ordinary-return exceptions; not a blanket “every transfer” rule | [FA2019 Sch.2 paras.1–5](https://www.legislation.gov.uk/ukpga/2019/1/schedule/2) |
| Exchange one year, completion the next | General disposal year follows s.28; property reporting runs from completion; rate/limit anti-forestalling must still be tested | [s.28](https://www.legislation.gov.uk/ukpga/1992/12/section/28); [FA2019 Sch.2](https://www.legislation.gov.uk/ukpga/2019/1/schedule/2); [FA2025 Sch.2](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2) |

## Worked cases

Each is an illustration, assuming UK residence, ordinary chargeable assets, available AEA, no other gains/losses/reliefs and no rate-band extensions unless stated. Relief conditions must be established; a form mapping below is **2025/26 only**.

**A: 2026/27 band allocation.** Taxable income £20,000; gain £12,600 − £3,000 = £9,600; total £29,600 within £37,700; CGT £1,728. With the same income and gain £52,600, taxable gain £49,600: £17,700 ×18% (£3,186) + £31,900 ×24% (£7,656) = **£10,842**. ([HMRC examples](https://www.gov.uk/capital-gains-tax/rates).)

**B: former home, 2026/27.** Gain £120,000; ownership 15 years; residence 7.5 years then whole-house letting 7.5 years. Assume no qualifying absence/additional relief, no exclusive business use and permitted grounds. Residence plus final 0.75 year = 8.25/15; PRR £66,000; gain £54,000; no shared occupancy so no Letting Relief. Higher-rate taxpayer: (£54,000 − £3,000) ×24% = **£12,240**. Report/pay within 60 days of completion, subject to the exceptions below; reconcile on the correct year’s return. ([s.223](https://www.legislation.gov.uk/ukpga/1992/12/section/223); [s.223B](https://www.legislation.gov.uk/ukpga/1992/12/section/223B).)

**C: repurchase, 2025/26.** Holding 9,500; sell 4,000 on 30 August 2025 for £6,000; acquire 500 on 11 September 2025 for £850, UK resident and not treaty non-resident; assume no same-day/other priority acquisitions. Match 500: proceeds £750 − cost £850 = **£100 loss**. The remaining 3,500 use the pool; its cost is missing, so the total gain/tax is non-usable. Check this point with one of our partner accountants. Listed-share reporting uses boxes 23–30. ([s.106A](https://www.legislation.gov.uk/ukpga/1992/12/section/106A); [2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf).)

**D: BADR limit, 2026/27.** Fully qualifying personal-company sale: unconditional contract/completion 1 June 2026; gain £400,000; prior BADR gains £700,000; income uses all basic band. Limit left £300,000 at 18% = £54,000. Excess £100,000 less £3,000 AEA at 24% = £23,280. **Total £77,280**; claim by 31 January 2029. No 2026/27 box numbers are authorised by the 2025/26 map. ([s.169N](https://www.legislation.gov.uk/ukpga/1992/12/section/169N); [s.1K](https://www.legislation.gov.uk/ukpga/1992/12/section/1K).)

**E: token pool, 2026/27.** 100 tokens at £2 (£200) then 300 at £1 (£300):400 costing £500, £1.25 each; no same-day/30-day purchase. Sell 200 for £700; cost £250; **gain £450**, remaining 200/cost £250. Only disposal; no claim/election or special reporting trigger: no tax or SA108 on these facts. ([HMRC tokens](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets); [HMRC reporting tests](https://www.gov.uk/capital-gains-tax/print); [2026 notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf), for the identified reporting tests only; do not assume the later-year form’s boxes.)

**F: connected loss.** Parent gives unlisted shares costing £40,000 to daughter at market value £30,000: **£10,000 restricted loss**, not deductible against unrelated gains. Track separately for gains on disposals to that daughter while connected; 2025/26 box 47 includes unused clogged losses. ([s.18](https://www.legislation.gov.uk/ukpga/1992/12/section/18); [2026 notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf).)

**G: 2025/26 property already reported.** UK-resident buy-to-let sale completed in 2025/26; property return filed/paid, then listed shares sold at a gain. Include property gain in box 6, its reported gain/loss in 9 and tax charged in 10; shares 23–30; property return reference 54. Reconcile whole-year CGT against property tax already charged, without double counting. Further tax ordinarily due 31 January 2027. For 2021/22 onwards, an initial overpayment is automatically offset against other Self Assessment charges; contact HMRC for allocation or repayment of a remaining overpayment, which is not automatically repaid. ([2026 form/notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf); [CG-APP18-320](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg-app18-320).)

**Historical examples preserved, with corrected conditions:**

- **H1, shares 2024/25:** sell 1,000 on 15 November 2024 for £25,000; pool £10/share; no priority purchase; unused band £5,000. Cost £10,000; gain £15,000; taxable £12,000; £5,000×18% + £7,000×24% = **£2,580**. ([Dated rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances); [s.104](https://www.legislation.gov.uk/ukpga/1992/12/section/104).)
- **H2, BTC:** sell 0.5 BTC on 1 February 2025 for £20,000; pool 2BTC at £8,000 each; no priority match. Cost £4,000; gain £16,000; taxable £13,000. Income/band absent: tax is **non-usable**, not a guessed 18%/24% result. Check this point with one of our partner accountants. ([HMRC tokens](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets).)
- **H3, former home:** ownership 10 years; residence 6 then letting 4; gain £200,000. Original occupancy/date evidence does not establish Letting Relief. If whole-house letting after departure and a 2024/25-or-later sale with no other qualifying periods, PRR=(6+0.75)/10×£200,000=£135,000; gain £65,000; **no Letting Relief; taxable £62,000**, replacing the old £40,000 relief/£22,000 taxable conclusion. Actual sale year, shared occupancy and income remain non-usable until confirmed. Check this point with one of our partner accountants. ([ss.223](https://www.legislation.gov.uk/ukpga/1992/12/section/223), [223B](https://www.legislation.gov.uk/ukpga/1992/12/section/223B).)
- **H4, same £900,000 qualifying business gain:** AEA£3,000 gives £897,000 taxable. Contract and completion assumed together on each original date:5 April 2025 at 10%=**£89,700**;5 April 2026 at 14%=**£125,580**;6 April 2026 at 18%=**£161,460**. Each step adds £35,880; total £71,760. A completion date alone cannot determine the rate. ([FA2025 s.8](https://www.legislation.gov.uk/ukpga/2025/8/section/8); [Sch.2](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2).)
- **H5, original 2024/25 BADR:** qualifying sole-trader business gain £500,000, owned>2 years, available lifetime allowance, no other gains/losses: taxable £497,000×10%=**£49,700**. For a later claim, the lifetime usage from this disposal is **£497,000**, the gain actually charged after AEA, rather than the original £500,000 entry ([CG64125](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg64125)). ([s.169N](https://www.legislation.gov.uk/ukpga/1992/12/section/169N); [HS275 amount of relief](https://www.gov.uk/government/publications/entrepreneurs-relief-hs275-self-assessment-helpsheet/hs275-business-asset-disposal-relief-2026).)

The two original £23,000-gain checks remain: the first assumes at least £20,000 unused basic band; the second assumes all ordinary gains fall above it. Neither establishes entitlement to the AEA where a disqualifying claim/election applies.

```oa-check
name: Basic rate gain GBP 23,000, annual exempt amount GBP 3,000 (2026/27)
inputs:
  gain: 23000
  aea: 3000
steps:
  - taxable: gain - aea
  - tax: pct(taxable, 18)
expected:
  taxable: 20000
  tax: 3600
```

```oa-check
name: Higher rate gain GBP 23,000, annual exempt amount GBP 3,000 (2026/27)
inputs:
  gain: 23000
  aea: 3000
steps:
  - taxable: gain - aea
  - tax: pct(taxable, 24)
expected:
  taxable: 20000
  tax: 4800
```

## When to refuse or refer

Non-usable holds remain for uncertain residence, overseas/FIG/TRF cases, non-resident tax bases/rebasing, UK branch/agency gains, property dealing versus investment, companies/trusts/estates, charity/hold-over/rollover, EIS/SEIS/VCT, liquidations/capital distributions, employee shares, funds/reorganisations, special BADR/IR cases, complex PRR, income share-loss claims, death carry-back and crypto income/DeFi. Preserve inputs and evidence and state the unresolved point: **Check this point with one of our partner accountants.** Do not turn a hold into an exemption, relief claim or estimated filing position. In particular, non-residents are not automatically exempt on every asset other than land ([s.1A](https://www.legislation.gov.uk/ukpga/1992/12/section/1A)).

## Filing and payment

**UK property:** FA2019 Sch.2 generally requires return within **60 days after completion** and payment on the return filing date. UK-resident residential disposals with no payment on account need no return under para.4. Excluded disposals include specified no-gain/no-loss transfers, certain no-premium leases, charities and pension investments. Para.5 can remove a separate return when an adequate ordinary self-assessment already delivered, or its required delivery date, falls before/on the property-return filing date. Non-resident direct/indirect UK-land disposals can require reporting even at a loss, subject to those exceptions. Joint owners report their own share. Before 27 October 2021 the post 6-April 2020 deadline was 30 days. Late filing starts at **£100**; interest/further penalties may apply. ([Sch.2 paras.1–6](https://www.legislation.gov.uk/ukpga/2019/1/schedule/2); [HMRC](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print); [dated deadlines](https://www.gov.uk/capital-gains-tax/print); [FA2009 Sch.55 para.3](https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/3).)

**SA1082026 (2025/26):** report if chargeable disposal proceeds>**£50,000**, gains before losses>**£3,000**, earlier-year gains taxable now, allowable-loss claim/CGT claim/election, remitted old foreign gains, FIG/TRF claim, or relevant non-resident/split-year UK-land disposal. Do not assume low gains remove every reporting obligation. Exclude the specified exempt disposals: private cars, qualifying low-value chattels, ISA/PEP investments, gilts/Premium Bonds and wholly PRR-covered home; notes also exclude betting/lottery winnings, relevant personal-injury/PPI compensation and personal-use foreign currency. The proceeds threshold was 4 times the allowance before 2023/24 ([HMRC year boundary](https://www.gov.uk/capital-gains-tax/print)); other old-year filing details require that year’s notes. ([2026 notes pp.1–2](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf).)

Send computations and relevant valuations/claim forms. Do not deduct AEA in disposal boxes. **2025/26 only** box map below; do not transfer box numbers to 2026/27 before checking its issued form. ([2026 form](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf); [notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf).)

| Section | Boxes / use | Source (read 2026-11-27) |
| --- | --- | --- |
| Residential / carried interest | 3–13C;6 gains before losses,7 losses;9 reported UK-property gain/loss,10 tax charged;11–12 real-time;13–13C carried-interest/FIG fields | [2026 form p.1](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) |
| Crypto | 13.1–13.8: disposal count/proceeds/costs/gains/losses/code/real-time gain/tax | [2026 form p.1](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) |
| Other assets / BADR | 14–22;17.1 non-residential land;17.2–17.4 BADR asset splits;18 unused | [2026 form p.2](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) |
| Listed shares | 23–30;26 gains,27 losses;26.1 FIG | [2026 form p.2](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) |
| Unlisted shares | 31–44;34 gains,35 losses;34.1 FIG;39–44 special employee/SEIS/income-loss entries require their own eligibility | [2026 form p.3](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) |
| Losses | 45 brought-forward losses used;46 eligible income losses against gains;47 unused losses carried;48 losses used against earlier gains | [2026 form p.3](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) |
| Reliefs | 49 IR;50 BADR;50.1 lifetime claimed to date, including current year; historical claims above current limit need notes’ exceptional adjustment treatment | [2026 notes pp.11–12](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf) |
| Adjustments / other | 51 adjustments,52 trust-related extra liability;52.1–52.5 non-resident CGT;53 estimates/valuations,54 explanations/references/claims | [2026 form p.4](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf) |

Use the notes’ applicable claim code (including PRR,LET,GHO,ROR,PRO,ESH,BAD,INV,NVC,EOT,OTH,MUL), not a code implying an unestablished entitlement. Record property/real-time references and credit the tax already charged/paid in the designated fields; reconcile the whole year. ([2026 notes](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf).)

**2025/26 deadlines:** paper 31 October 2026, online 31 January 2027; ordinary balance 31 January 2027. A late registration notice can set a 3-month filing period; payment remains due 31 January 2027. **Real-time service:** UK residents, own gains only; excludes UK residential property, overseas-property foreign-tax-credit claims and life-policy chargeable-event gains. For 2025/26 report by 31 December 2026/pay 31 January 2027; also include in Self Assessment if registered. For 2026/27 use 31 December 2027/31 January 2028. ([Self Assessment deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines); [real-time service](https://www.gov.uk/report-and-pay-your-capital-gains-tax/print).)

## Completion checklist

- Evidence, year, residence and beneficial ownership established; held conclusions excluded.
- Contract/transfer and anti-forestalling checked; costs, matching, reliefs, losses and lifetime claims supported.
- Original cases and all disposals reconciled; allowance/rates use the correct year and remaining band.
- Property and annual return obligations tested separately; right-year form and payment credits checked; computations attached.

## Sources

The cited operative provisions and guidance passages were read on **2026-11-27**. Core legislation: [TCGA1992](https://www.legislation.gov.uk/ukpga/1992/12), [FA2025 ss.8–9/Sch.2](https://www.legislation.gov.uk/ukpga/2025/8/schedule/2), [FA2019 Sch.2](https://www.legislation.gov.uk/ukpga/2019/1/schedule/2). Filing evidence: [SA1082026](https://assets.publishing.service.gov.uk/media/69bd8990cfa346b9d47049e4/SA108-2026.pdf), [notes 2026](https://assets.publishing.service.gov.uk/media/6a02e5df4fb0713aa63ea77c/SA108-Notes-2026.pdf). Rates/examples: [HMRC rates](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances), [rate-band examples](https://www.gov.uk/capital-gains-tax/rates). Held specialist topics are not proven outcomes.

Not yet confirmed: specialist outcomes expressly held above are non-usable; Check this point with one of our partner accountants.
