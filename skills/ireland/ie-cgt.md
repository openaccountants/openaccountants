---
name: ie-cgt
description: "Irish individual Capital Gains Tax for calendar 2026: disposal dates, the provisional October standard-rate reduction, costs, losses, shares, home and business reliefs, clearance, payment and filing. Includes preserved historical cases. Specialist and unproven treatments require a partner accountant."
version: 2.5
jurisdiction: IE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Ireland Capital Gains Tax (CGT) for individuals, 2026

Built by Michael Cutajar and the OpenAccountants team. Checked against the law: not signed off by an accountant.

For individual capital disposals in calendar 2026. Establish the asset, residence and ordinary residence, domicile, contract and condition dates, documented costs, ownership history, reliefs and losses before computing. An unknown date, cost, valuation or eligibility condition means stop that calculation and obtain evidence; do not invent a higher-rate or denied-relief default.

## Who this applies to

- **Resident or ordinarily resident individuals:** generally chargeable on gains wherever the asset is situated, subject to exceptions. Someone neither resident nor ordinarily resident is charged on specified Irish assets: land/buildings, minerals and related rights, continental-shelf exploration/exploitation rights, relevant unquoted shares deriving their value or the greater part of it directly or indirectly from those assets, and Irish branch/agency trade assets. Residence alone is not the whole test ([TCA s.29](https://www.irishstatutebook.ie/eli/1997/act/39/section/29/enacted/en/html)). Foreign gains of non-domiciled individuals, temporary non-residence and treaty positions are specialist holds below.
- **Disposal:** sale, gift, exchange, or certain compensation/insurance receipts. For a contract, use the date the contract is made, not completion; if genuinely conditional, the date the condition is satisfied ([s.542](https://www.irishstatutebook.ie/eli/1997/act/39/section/542/enacted/en/html)). Compulsory purchase and capital-payment timing are specialist holds.
- **Assets:** land, buildings, shares, goodwill, patents/copyright, foreign currency and trade assets can be chargeable; joint owners compute their own share ([Revenue assets](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-do-you-pay-cgt-on.aspx)). Crypto capital disposals can be within CGT; a trade of dealing in crypto has different treatment. Multi-lot crypto identification, options, debts and corporate actions are specialist holds, not automatic application of a share rule ([TDM 02-01-03, sections 1–1.3](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf)).
- **Exempt categories:** betting/lottery winnings, prize bonds, sweepstakes, National Instalments Savings Scheme bonuses, government stocks, animals and private motor cars are listed by [Revenue](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx). Life policies and pension-related payments require classification; no blanket exemption is offered here.
- **Chattels:** s.602 tests **consideration**, not gain. An individual's non-wasting tangible movable asset is exempt if consideration does not exceed EUR 2,540, subject to the set/part-interest and excluded-transaction rules. Above that, tax is capped at half the consideration excess; losses have a deemed minimum consideration. A set, part interest, loss, commodity/currency or disputed valuation requires specialist checking before use ([s.602](https://www.irishstatutebook.ie/eli/1997/act/39/section/602/enacted/en/html), euro substitution in [Finance Act 2001 Schedule 5](https://www.irishstatutebook.ie/eli/2001/act/7/schedule/5/enacted/en/html)). Do not use Revenue's summary wording about the amount of the gain to override the statute.
- **Wasting chattels:** tangible movable wasting assets are generally exempt, but capital-allowance and trade-use restrictions apply, including partial-use apportionment; do not exempt business plant automatically ([s.603](https://www.irishstatutebook.ie/eli/1997/act/39/section/603/enacted/en/html)). Check this point with one of our partner accountants.
- **Spouses/civil partners:** qualifying transfers generally produce no gain/no loss and preserve the transferor's base cost, rather than a fresh market-value cost. Trading stock, non-resident recipients outside the CGT charge, separation/divorce and court-order conditions need checking ([s.1028(5)–(7)](https://www.irishstatutebook.ie/eli/1997/act/39/section/1028/enacted/en/html), [Revenue exemptions](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx)). Check this point with one of our partner accountants.
- **Death:** no deemed disposal by the deceased; acquisition at death-date market value by the representative/legatee. A sale in administration can create CGT; CAT is a separate recipient-side tax (`ie-cat`). Estate administration is a specialist hold ([s.573](https://www.irishstatutebook.ie/eli/1997/act/39/section/573/enacted/en/html)).

## Rates, bands and thresholds

| Item and operative conditions | 2026 figure | Official source URL |
|---|---|---|
| Standard gains, disposals to 6 October 2026; 33% has applied since 6 December 2012 | 33% | https://www.irishstatutebook.ie/eli/2013/act/8/section/43/enacted/en/html |
| Standard gains, disposals from 7 October 2026; provisional resolution, not an enacted Finance Act | 31% | https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml ; https://www.revenue.ie/ros-content/ROS-Info-section-text-en.aspx |
| Development land, separate regime; detailed computation held | 33% | https://www.irishstatutebook.ie/eli/2013/act/8/section/43/enacted/en/html |
| Individual annual exemption, after allowable losses; non-transferable, also for non-residents; unavailable where s.598/599 relief is allowed | EUR 1,270 | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx ; https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html |
| Revised Entrepreneur Relief, qualifying gains from 2017; 2016 rate was 20% | 10% | https://www.irishstatutebook.ie/eli/2016/act/18/section/26/enacted/en/html |
| Entrepreneur Relief lifetime gain ceiling: 2016–2025 / from 1 January 2026; prior gains count as explained below | EUR 1,000,000 / EUR 1,500,000 | https://www.irishstatutebook.ie/2025/en/act/pub/0018/sec0051.html |
| Retirement Relief outside family, from 2025: age 55–69 / 70+; aggregated consideration, not gain | EUR 750,000 / EUR 500,000 | https://www.irishstatutebook.ie/eli/2023/act/39/section/49/enacted/en/html |
| Retirement Relief to qualifying child, from 2025: age 55–69 / 70+; aggregation rules apply | EUR 10 million / EUR 3 million | https://www.irishstatutebook.ie/eli/2023/act/39/section/50/enacted/en/html |
| Site-to-child maximum market value; area rule below | EUR 500,000 | https://www.irishstatutebook.ie/eli/2008/act/3/section/55/enacted/en/html |
| Section 980 consideration threshold, specified asset / house including apartment; applies only above threshold | EUR 500,000 / EUR 1,000,000 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf |
| Purchaser deduction without clearance on in-scope money consideration | 15% | https://www.irishstatutebook.ie/eli/1997/act/39/section/980/enacted/en/html |

**Status of the October reduction, checked 27 November 2026.** Financial Resolution No.3 substitutes 31% for 33% for disposals from 7 October and expressly declares statutory effect. A qualifying resolution has force under the Provisional Collection of Taxes Act 1927; the definition of tax includes CGT ([1927 s.2](https://www.irishstatutebook.ie/eli/1927/act/7/section/2/enacted/en/html), [Finance Act 2010 s.160](https://www.irishstatutebook.ie/eli/2010/act/5/section/160/enacted/en/html)). The [official Bill API](https://api.oireachtas.ie/v1/legislation?bill_year=2026&bill_no=98&limit=1) records Fifth Stage completed in the Dáil on 25 November, with `act: null`; it does not establish enactment. The [Bill as passed by the Dáil, section 41](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/ver_b/b98b26d.pdf) retains the same rate/date (section 36 in the initiated Bill).

The resolution ceases at the earliest applicable event: failure of the Second Stage deadline (84 days, with the statutory recess rule), rejection of the provision, commencement of the corresponding Act, or four months from the expressed effective date. Dissolution periods are disregarded under the amended rule ([Finance Act 1974 s.85](https://www.irishstatutebook.ie/eli/1974/act/27/section/85/enacted/en/html), [Appropriation Act 1991 s.2](https://www.irishstatutebook.ie/eli/1991/act/32/section/2/enacted/en/html), [Finance Act 1992 s.250](https://www.irishstatutebook.ie/eli/1992/act/9/section/250/enacted/en/html)). Second Stage is recorded on 20 October 2026. Use 31% while operative; before relying on this Guide later, recheck enactment/amendment or lapse, particularly before 7 February 2027. Do not describe the Bill as enacted or automatically assume a retrospective 33% liability if the resolution ceases; that outcome needs the final legislation and provisional-collection rules checked. Check this point with one of our partner accountants.

## The taxable base

1. Compute each capital disposal in EUR: consideration (market value where required), less allowable acquisition costs, qualifying enhancement/title expenditure, and disposal costs. Under s.552 expenses must be wholly and exclusively incurred; enhancement must remain reflected in the asset's state or nature at disposal. Professional fees, commission, stamp duty, conveyancing and relevant advertising/valuation costs can qualify. Routine repairs/revenue deductions are not additional CGT costs. Interest and insurance premiums are not ordinary individual s.552 deductions; no double deduction of expenditure allowable against income ([s.552](https://www.irishstatutebook.ie/eli/1997/act/39/section/552/enacted/en/html), [s.554](https://www.irishstatutebook.ie/eli/1997/act/39/section/554/enacted/en/html)).
2. Apply any proven relief; collect all annual gains and losses. Deduct current-year allowable capital losses, then unused brought-forward losses, before the annual exemption. Losses reduce capital gains, not ordinary income. Where more than one rate applies, losses go against higher-rate gains first, subject to special restrictions ([ss.31,546](https://www.irishstatutebook.ie/eli/1997/act/39/section/546/enacted/en/html)).
3. Deduct the individual EUR 1,270 exemption, highest-rate gains first; it is not carried to a spouse. Do not deduct it where Retirement Relief under s.598 or s.599 is allowed ([s.601(3),(5)](https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html)). Apply the rate for each disposal's date; keep pre/post-7 October gains separate.

**Market value:** non-arm's-length gifts/undervalue transactions and connected-person disposals normally use market value; qualifying spouse relief is a separate exception. Inherited assets normally use death-date value. Pre-6 April 1974 holdings require the statutory rebasing safeguards. Obtain a supported valuation ([ss.547](https://www.irishstatutebook.ie/eli/1997/act/39/section/547/enacted/en/html), [549](https://www.irishstatutebook.ie/eli/1997/act/39/section/549/enacted/en/html), [556](https://www.irishstatutebook.ie/eli/1997/act/39/section/556/enacted/en/html)).

**Indexation:** apply the statutory year-of-cost multiplier separately to eligible acquisition/enhancement costs incurred through 2002; 2003 onwards has multiplier 1.000. Do not index disposal costs. Indexation cannot create or increase a loss, nor turn a loss into a gain; pre-1974 rebasing has the s.556(4) safeguards. Development-land current-use-value rules require specialist work ([Finance Act 2003 s.65, s.556(6A) table](https://www.irishstatutebook.ie/eli/2003/act/3/section/65/enacted/en/html), [s.556(4)](https://www.irishstatutebook.ie/eli/1997/act/39/section/556/enacted/en/html)).

**Shares:** FIFO within the same class under [s.580](https://www.irishstatutebook.ie/eli/1997/act/39/section/580/enacted/en/html), subject to [s.581](https://www.irishstatutebook.ie/eli/1997/act/39/section/581/enacted/en/html). Match disposals first with same-class shares acquired by the same person in the same capacity within the preceding four weeks; normal identification applies to the excess. Do not describe this as a universal LIFO rule. A loss followed by same-class reacquisition within four weeks is restricted to gains on the reacquired shares, proportionately if only some are reacquired. Spouse/civil-partner transactions can engage the rule too. Corporate actions, rights/bonus issues and different classes need a complete cost trail and specialist checking.

**Other loss restrictions:** development-land gains accept only development-land losses; development-land losses can offset other gains. Connected-person losses are restricted to gains on other disposals to that same person while still connected. Jointly assessed spouse/civil-partner losses generally transfer automatically unless retention is requested by 1 April next year. No general carry-back; unused losses arising in the year of death can offset the deceased's gains in the preceding three years, latest first ([Revenue losses](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx), [s.549(3)](https://www.irishstatutebook.ie/eli/1997/act/39/section/549/enacted/en/html), [s.573(3)](https://www.irishstatutebook.ie/eli/1997/act/39/section/573/enacted/en/html)). If no gains arise in the loss year, Revenue permits the loss claim on the next return with gains. Do not preserve an exemption by voluntarily carrying losses past available gains.

### Principal Private Residence relief (s.604)

Full relief requires occupation as the only/main residence throughout ownership, subject to the final-period rule; gardens/grounds up to one acre **excluding the house site** can qualify. For partial occupation, exempt the qualifying proportion of the gain. Count the last 12 months once, only for a property that has been the owner's PPR. Exclusive business use is apportioned; Rent a Room Relief does not itself prevent full relief. Acquisition wholly/mainly to realise a disposal gain, or profit-seeking expenditure, can prevent relief ([s.604(2)–(6),(14)](https://www.irishstatutebook.ie/eli/1997/act/39/section/604/enacted/en/html), [Revenue PPR](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx)).

Employment absences qualify under s.604(5) only if the home was occupied as PPR **both before and after**, and there was no other residence eligible for this relief during the absence. Employment/office duties wholly outside the State can qualify; work-location or reasonably imposed employer conditions preventing residence can qualify for up to four years in total. There is no general Irish three-year absence allowance for any reason. Hospital/nursing/convalescent/fee-paying retirement-home absences, dependent-relative claims, multiple homes and development value require specialist checking; do not use a simple occupied-month fraction for them. Check this point with one of our partner accountants.

### Revised Entrepreneur Relief (s.597AA)

The reduced rate is 10% from 2017 (20% in 2016). The lifetime qualifying gain limit is EUR 1,000,000 for 2016–2025, increasing to EUR 1,500,000 from 1 January 2026. For a 2026 disposal include earlier 2026 qualifying gains and 2016–2025 qualifying gains, with the latter contribution capped at EUR 1,000,000. Excess goes at the applicable standard rate; the annual exemption goes against higher-rate gains first ([Finance Act 2016 s.26](https://www.irishstatutebook.ie/eli/2016/act/18/section/26/enacted/en/html), [Finance Act 2025 s.51](https://www.irishstatutebook.ie/2025/en/act/pub/0018/sec0051.html)).

- **Sole trade assets:** beneficial ownership for three continuous years within the five before disposal, used in a qualifying business. **Shares:** at least 5% of ordinary shares beneficially owned for three continuous years at any time before disposal; do not impose the sole-trade five-year window on that shareholding ([Finance Act 2015 s.35](https://www.irishstatutebook.ie/eli/2015/act/52/section/35/enacted/en/html), amended by [Finance Act 2020 s.24](https://www.irishstatutebook.ie/eli/2020/act/26/section/24/enacted/en/html)).
- For company shares the individual must also have served as director/employee in a managerial or technical capacity for at least 50% of working time for three continuous years in the five before disposal. The company must carry on a qualifying business, or be a holding company of a qualifying group. Investment holding, holding development land, and developing/letting land are excluded businesses. Each relevant 51% subsidiary must satisfy the qualifying-business test; a dormant/non-trading subsidiary can prevent relief. The holding-company definition requires shares in other companies all of which are its 51% subsidiaries ([2015 s.35](https://www.irishstatutebook.ie/eli/2015/act/52/section/35/enacted/en/html), [Finance Act 2023 s.48](https://www.irishstatutebook.ie/eli/2023/act/39/section/48/enacted/en/html)).
- Investment assets, development land and personally owned assets used by a separate company do not qualify as ordinary sole-trade business assets. Connected-company goodwill, shares sold to a company while remaining connected, incorporations/reorganisations and commercial-reasons exceptions need specialist checking under s.597AA(2),(6)–(8) ([Finance Act 2017 s.30](https://www.irishstatutebook.ie/eli/2017/act/41/section/30/enacted/en/html), [Revenue relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx)). Check this point with one of our partner accountants.

### Retirement Relief (ss.598–599)

No actual retirement is required. Ordinary eligibility starts at 55. Qualifying business assets generally require ten-year ownership ending at disposal; tangible movable assets have separate ownership treatment. Family-company shares require the qualifying ten-year company/shareholding and working-director conditions, with five years full time. A family company requires at least 25% voting rights personally, or at least 10% personally with at least 75% held by the individual/family. Relief on shares is limited to the chargeable-business-asset proportion. Review previous disposals and aggregate consideration; do not test the gain against the threshold ([s.598](https://www.irishstatutebook.ie/eli/1997/act/39/section/598/enacted/en/html)).

- **Outside family from 2025:** full relief up to aggregate consideration EUR 750,000 at 55–69 or EUR 500,000 at 70+. Above it, marginal relief limits CGT to 50% of the excess, subject to the lifetime aggregation/adjustment rules. The older 2014–2024 age split was 66, not 70 ([Finance Act 2023 s.49](https://www.irishstatutebook.ie/eli/2023/act/39/section/49/enacted/en/html), [Revenue retirement](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx)).
- **Qualifying child from 2025:** EUR 10 million at 55–69; EUR 3 million at 70+. Aggregation includes the statutory pre-2025 transition where applicable; it is not a fresh allowance per child/transfer. Extended child definitions include qualifying step/adopted/civil-partner/foster children and certain nieces/nephews/deceased-child descendants. Six-year disposal clawback and the separate twelve-year deferral/retention regime need specialist checking. The latter is for s.599(1)(b)(v) disposals above EUR 10 million by a parent aged 55–69, claimed on the return; it is not available merely because a transferor is over 55 ([Finance Act 2023 s.50](https://www.irishstatutebook.ie/eli/2023/act/39/section/50/enacted/en/html), [Finance Act 2024 s.55](https://www.irishstatutebook.ie/eli/2024/act/43/section/55/enacted/en/html)). Check this point with one of our partner accountants.
- Under-55 ill-health concessions, farm letting, ownership-period deeming, connected-company disposals and other special Retirement Relief cases remain non-usable holds. Check this point with one of our partner accountants.

### Site to a child (s.603A)

A qualifying parent-to-child disposal to enable construction of the child's only/main residence can be exempt where market value is at most EUR 500,000. The garden/grounds area must not exceed 0.4047 hectare **excluding the house construction site**; the original blanket one-acre total-site limit was too restrictive. Simultaneous transfers by both parents and the statutory inclusion of a child's spouse/civil partner are recognised. Check earlier site relief: relief is not simply repeatable for successive sites to the same child. The original gain can become chargeable on the child's onward disposal if the house was not built and occupied as PPR for three years; the spouse/civil-partner exception and family definitions need checking ([Finance Act 2001 s.93](https://www.irishstatutebook.ie/eli/2001/act/7/section/93/enacted/en/html), [2007 s.53](https://www.irishstatutebook.ie/eli/2007/act/11/section/53/enacted/en/html), [2008 s.55](https://www.irishstatutebook.ie/eli/2008/act/3/section/55/enacted/en/html), [2018 s.30](https://www.irishstatutebook.ie/eli/2018/act/30/section/30/enacted/en/html)). Check this point with one of our partner accountants.

## Deadlines and filing

- **Pay the actual CGT:** disposals 1 January–30 November 2026 by **15 December 2026**; December 2026 disposals by **31 January 2027**. There is no routine balance deferred to the annual return date. **File by 31 October 2027** for 2026 disposals, including disposals with no tax because of reliefs/losses ([Revenue pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)).
- **Return:** Form 11 on ROS for chargeable individuals (`ie-income-tax-form11`); paper Form 12 for PAYE taxpayers required to return; paper CG1 for those not normally returning or using online Form 12. The online eForm 12 cannot report CGT. Include asset description, consideration, reliefs, brought-forward losses, gain/loss, taxable gain/rate and tax already paid. Trust/estate Form 1 and company CT1 are outside this individual Guide (same Revenue page).
- **ROS extensions:** do not infer a 2027 filing extension from a 2026 announcement. [eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx) concerns the 2025 income-tax pay/file cycle. A ROS return extension does not move the December/January CGT payment dates. Any claimed extension for this return requires the actual applicable announcement.
- **Register/pay:** myAccount or ROS, using TRN/PPSN. If exempt from mandatory e-filing, use Revenue's payment-accounting route or Payslip A/B for the initial/later period. Registration/payment online does not turn CG1 into an online return (Revenue pay/file page).

**CG50A clearance (s.980):** specified assets include Irish land/minerals/related rights, continental-shelf rights, relevant land-rich unquoted shares and replacement shares, and goodwill of an Irish trade. Anti-avoidance applies when determining share values. Above EUR 500,000 consideration (EUR 1 million for a house/apartment), obtain clearance before the consideration passes or apply the withholding rules; splitting parts of one asset does not necessarily avoid the threshold. Gifts with no consideration are outside this deduction regime; new-house certificates and non-cash consideration have separate rules ([TDM 42-03-01, sections 1.1–1.8](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf)).

A certificate may issue if the vendor is resident, **no CGT is payable on the disposal**, or relevant CGT on this and earlier disposals of the same asset has been paid. Revenue also accepts a properly documented solicitor's undertaking in the specified circumstances. Thus a non-resident does not invariably need to prepay tax. Apply through eCG50 in ROS/myAccount; paper CG50 remains for non-enabled customers. Without clearance on an ordinary in-scope cash sale, the buyer deducts 15%, accounts/pays within 30 days and provides CG50B; the vendor claims the appropriate credit/repayment, not an automatic full refund. Non-cash consideration has a seven-day notification/payment rule. These special conveyancing cases require checking before completion (same TDM; [s.980(8) as substituted](https://www.irishstatutebook.ie/eli/2003/act/3/section/71/enacted/en/html)). Check this point with one of our partner accountants.

**Records:** retain contracts, supported valuations, broker/corporate-action notes, cost invoices, relief and loss history, occupation evidence and CG50 documents. Do not discard acquisition evidence while the asset is held. The historical blanket six-year retention statement is not a destruction instruction; the applicable statutory period for the particular records needs checking. Check this point with one of our partner accountants.

## Penalties and interest

CGT late-payment interest is **0.0219% per day or part day** on the unpaid balance for the actual delay ([s.1080, substituted by Finance Act 2005 s.145](https://www.irishstatutebook.ie/eli/2005/act/5/section/145/enacted/en/html), [2009 s.29 table](https://www.irishstatutebook.ie/eli/2009/act/12/section/29/enacted/en/html)). Do not confuse the annual-return date with the payment due date.

For a chargeable person's late return, s.1084 includes CGT: **5% capped at EUR 12,695** within two months of the applicable return deadline, **10% capped at EUR 63,485** afterwards. The base is assessed tax subject to statutory deductions/credits, not simply the unpaid balance after voluntary advance CGT payments. For an unextended 31 October 2027 deadline, the bands run to 31 December 2027 and thereafter ([s.1084](https://www.irishstatutebook.ie/eli/1997/act/39/section/1084/enacted/en/html), [euro amounts, Schedule 5](https://www.irishstatutebook.ie/eli/2001/act/7/schedule/5/enacted/en/html)). Incorrect returns, director/source-credit exceptions and overlapping tax-geared penalties need specialist checking; do not automatically add every sanction. Check this point with one of our partner accountants.

## Cross-border points

Foreign-tax credits/remittance basis and treaty scope: `ie-foreign-tax-and-withholding`, `ie-cross-border`, `ie-non-dom`; company gains/development land: `ie-corporation-tax`; gifts/inheritances to recipients: `ie-cat`. Also held: trusts/estates, partnerships, offshore funds/foreign life policies, venture funds, reorganisations/share exchanges, compensation/insurance deferrals, pre-1974 safeguards, Farm Restructuring Relief and the separate 7 December 2011–31 December 2014 property relief. None is automatically taxed/exempted at an ordinary CGT rate on the basis of this Guide. Check this point with one of our partner accountants.

## Worked examples

**Example 1. Listed shares sold in May 2026 (33%, simple).** Mr Ó Briain, Irish resident, sells 5,000 shares in an Irish listed company on 12 May 2026 for 75,000 after commission. He bought 3,000 in June 2018 for 18,000 and 2,000 in February 2021 for 22,000. No other disposals, no purchases in the four weeks before, no losses. FIFO uses the 2018 shares, then the 2021 shares; together they are the whole sale. No indexation (costs after 2002). The disposal is before 7 October 2026, so 33%. Gain 35,000, less 1,270, taxable 33,730, CGT 11,130.90. Pay by 15 December 2026; file by 31 October 2027 (Form 11 if he is a chargeable person, otherwise Form 12 or CG1). If he paid on 15 January 2027, interest for 31 days would be 11,130.90 x 0.0219% x 31.

```oa-check
name: Listed shares sold 12 May 2026, FIFO, 33% rate
inputs:
  proceeds: 75000
  cost_2018: 18000
  cost_2021: 22000
  exemption: 1270
  rate: 33
  late_days: 31
  daily_interest_bp: 219
steps:
  - gain: proceeds - cost_2018 - cost_2021
  - taxable: max(gain - exemption, 0)
  - cgt: taxable * rate / 100
  - interest_if_late: round(cgt * daily_interest_bp / 1000000 * late_days, 2)
expected:
  gain: 35000
  taxable: 33730
  cgt: 11130.90
  interest_if_late: 75.57
```

**Example 2. Founder sells her trading company on 2 November 2026 (Entrepreneur Relief over the limit, 31% on the excess).** Ms de Paor founded an Irish trading company in 2018 and has held all its ordinary shares and worked full time as a director since. The company has no subsidiaries and no Irish land. Assume it also has no Irish mineral or continental-shelf rights or replacement shares caught by s.980, and that her full-time service meets the managerial/technical working-time test. On 2 November 2026 she sells all the shares to an unrelated buyer for 2,010,000, keeps no connection, and has no earlier qualifying gains. Cost 10,000. Gain 2,000,000. The gain arises in 2026, so the lifetime limit is 1,500,000 at 10%: 150,000. The excess of 500,000 is taxed at the standard rate for the disposal date. The disposal is after 7 October 2026, so 31%. The EUR 1,270 exemption goes against the higher-rate part first (s.601(3)): 498,730 at 31% = 154,606.30. Total 304,606.30. The disposal is in the initial period, so she pays by 15 December 2026. For arithmetic comparison only, applying 33% to that excess gives 164,580.90 and total 314,580.90; this is not a conclusion about liability if the resolution ceases. The shares are unquoted but do not derive their value from Irish land, so s.980 does not apply.

```oa-check
name: Entrepreneur Relief, gain EUR 2,000,000, disposal 2 Nov 2026, excess at 31% (33% arithmetic comparison)
inputs:
  proceeds: 2010000
  cost: 10000
  er_limit: 1500000
  er_rate: 10
  exemption: 1270
  rate_new: 31
  rate_old: 33
steps:
  - gain: proceeds - cost
  - qualifying: min(gain, er_limit)
  - cgt_er: qualifying * er_rate / 100
  - excess: gain - qualifying
  - excess_taxable: max(excess - exemption, 0)
  - cgt_excess: excess_taxable * rate_new / 100
  - total_cgt: cgt_er + cgt_excess
  - total_if_33: cgt_er + excess_taxable * rate_old / 100
expected:
  gain: 2000000
  qualifying: 1500000
  cgt_er: 150000
  excess: 500000
  excess_taxable: 498730
  cgt_excess: 154606.30
  total_cgt: 304606.30
  total_if_33: 314580.90
```

### Preserved home and Retirement Relief illustrations

**2026 PPR illustration (Ms Ní Mhurchú):** bought January 2012 for EUR 300,000 including purchase costs, occupied through December 2021 (120 months), let from January 2022 by choice, contract December 2026 for EUR 520,000 less EUR 8,000 sale costs. Assume no development value, exclusive business use, other gains/losses or special absence. Ownership 180 months; qualifying 120 + 12 = 132, chargeable 48. Gain EUR 212,000; chargeable part EUR 56,533.33; after exemption EUR 55,263.33; at 31%, EUR 17,131.63. Pay 31 January 2027; return 31 October 2027. The pre-October-update version applied 33% and gave EUR 18,236.90: that is only a comparison, not the operative December 2026 rate.

**2026 Retirement Relief illustration:** age 60, qualifying assets sold at arm's length in March 2026 for EUR 900,000, cost EUR 200,000, no prior qualifying disposals, no other gains/losses or credits. Assume all s.598 conditions proved. Gain EUR 700,000. With no Retirement Relief, the ordinary calculation is (700,000 − 1,270) × 33% = EUR 230,580.90. With marginal Retirement Relief, no annual exemption is given: limit (900,000 − 750,000) × 50% = **EUR 75,000**. Pay 15 December 2026; return 31 October 2027.

### Historical cases (keep their original tax years)

- **Shares, 12 May 2025:** Mr Ó Briain's earlier case uses the same 5,000 shares, 3,000 bought June 2018 for EUR 18,000 and 2,000 February 2021 for EUR 22,000, EUR 75,000 net proceeds, no other disposals or losses. Assuming no four-week acquisitions, gain EUR 35,000, taxable EUR 33,730, 33% tax **EUR 11,130.90** (original whole-euro display EUR 11,131). Pay 15 December 2025; return 31 October 2026. It does not become a 2026 disposal merely because this Guide is updated.
- **Founder, 1 October 2025:** Ms de Paor, age 47, company founded in 2018, 100% ordinary shares, full-time director, EUR 1,400,000 proceeds, EUR 10,000 cost, no prior qualifying gains. On the stated qualifying-business assumptions, gain EUR 1,390,000; the **2025** ceiling is EUR 1,000,000, not EUR 1.5 million. EUR 100,000 at 10%, plus (390,000 − 1,270) × 33% = EUR 128,280.90; total **EUR 228,280.90** (original rounded EUR 228,281). Company asset composition was not established: the historical reference to Nigerian or other non-land assets does not prove s.980 is inapplicable. Clearance remains a non-usable hold pending actual assets. Check this point with one of our partner accountants.
- **Founder, 1 October 2026:** preserve the prior case's original date and EUR 2,010,000 proceeds/EUR 10,000 cost, 2018 foundation, entire ordinary holding, full-time director, no subsidiaries, unconnected buyer/no retained connection and no prior qualifying disposals. Gain EUR 2,000,000; EUR 1,500,000 at 10% plus EUR 498,730 at 33% = **EUR 314,580.90**. This is a separate historical case from the current 2 November disposal above; establish land-rich status for s.980.
- **Galway home, 30 November 2025: conditional arithmetic only:** Ms Ní Mhurchú bought January 2008 for EUR 280,000 plus EUR 5,000 costs; occupied through December 2018 (132 months), let January 2019–December 2023 (60 months) while working/renting in Dublin; returned January 2024–November 2025 (23 months); sold for EUR 490,000 less EUR 10,000 costs. Original total 215 months, occupation 155, proposed work absence 48, proposed qualifying 203, residual 12. The final 12 months are already within actual occupation and cannot offset earlier letting again. Gain EUR 195,000. **Only if** s.604(5)'s work-prevention and no-other-eligible-residence tests are proved, unrounded arithmetic gives taxable EUR 9,613.72093 and 33% tax EUR 3,172.53 (original rounded displays: chargeable EUR 10,884, taxable EUR 9,614, tax EUR 3,173). The facts do not establish that work prevented residence; those candidate figures are **not usable as a filing conclusion**. Check this point with one of our partner accountants.

## Ask the client first

Obtain the signed contract and conditions; residence, ordinary residence and domicile; asset classification and location; consideration, valuations and cost evidence; connected-party relationship; share/corporate-action history; gains/losses and earlier relief claims. For a home obtain exact ownership/occupation/absence/business-use dates and land/development value. For a business obtain age, voting/ordinary shareholdings, working-time and ownership evidence, group assets and prior disposals. For clearance obtain consideration type, CG50A/CG50B and any relevant tax-payment/undertaking evidence. Missing facts stop the affected calculation, not every ordinary CGT calculation.

## Sources

Primary provisions and the neighbouring conditions identified above were read on **27 November 2026**; the Bill API is a status record, not an enacted statute. Historical examples keep their stated years.

| Source / portion read | Official URL | Read on |
|---|---|---|
| s.29(1)–(7): residence and territorial scope | https://www.irishstatutebook.ie/eli/1997/act/39/section/29/enacted/en/html | 2026-11-27 |
| s.542(1)–(2): contract and condition timing | https://www.irishstatutebook.ie/eli/1997/act/39/section/542/enacted/en/html | 2026-11-27 |
| Assets, joint ownership and compensation headings | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-do-you-pay-cgt-on.aspx | 2026-11-27 |
| TDM sections 1–1.3: capital crypto versus trade | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf | 2026-11-27 |
| Exemptions, spouse exceptions and personal exemption headings | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx | 2026-11-27 |
| s.602(1)–(7): consideration test, marginal cap and limits | https://www.irishstatutebook.ie/eli/1997/act/39/section/602/enacted/en/html | 2026-11-27 |
| Schedule 5: euro rows for ss.601,602,1084 | https://www.irishstatutebook.ie/eli/2001/act/7/schedule/5/enacted/en/html | 2026-11-27 |
| s.603(1)–(4): wasting chattels and business use | https://www.irishstatutebook.ie/eli/1997/act/39/section/603/enacted/en/html | 2026-11-27 |
| s.1028(5)–(7): spouse basis carryover | https://www.irishstatutebook.ie/eli/1997/act/39/section/1028/enacted/en/html | 2026-11-27 |
| s.573(2)–(5): death basis and losses | https://www.irishstatutebook.ie/eli/1997/act/39/section/573/enacted/en/html | 2026-11-27 |
| s.43: 33% standard/development rate and start date | https://www.irishstatutebook.ie/eli/2013/act/8/section/43/enacted/en/html | 2026-11-27 |
| Financial Resolution No.3: motion, effective date and statutory declaration | https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml | 2026-11-27 |
| CGT notice: new rate, earlier disposals and unchanged development land | https://www.revenue.ie/ros-content/ROS-Info-section-text-en.aspx | 2026-11-27 |
| s.601(1)–(5): exemption and rate ordering | https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html | 2026-11-27 |
| s.26: ER 10% from 2017 | https://www.irishstatutebook.ie/eli/2016/act/18/section/26/enacted/en/html | 2026-11-27 |
| s.51: ER annual/lifetime gain aggregation from 2026 | https://www.irishstatutebook.ie/2025/en/act/pub/0018/sec0051.html | 2026-11-27 |
| s.49: post-2024 Retirement Relief age bands | https://www.irishstatutebook.ie/eli/2023/act/39/section/49/enacted/en/html | 2026-11-27 |
| s.50: child relief and transition aggregation | https://www.irishstatutebook.ie/eli/2023/act/39/section/50/enacted/en/html | 2026-11-27 |
| s.55: site value and simultaneous parents | https://www.irishstatutebook.ie/eli/2008/act/3/section/55/enacted/en/html | 2026-11-27 |
| TDM sections 1.1–1.8: scope, deductions and clearance | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf | 2026-11-27 |
| s.980(2)–(11): specified assets, deduction and clearance | https://www.irishstatutebook.ie/eli/1997/act/39/section/980/enacted/en/html | 2026-11-27 |
| s.2: statutory effect of financial resolutions | https://www.irishstatutebook.ie/eli/1927/act/7/section/2/enacted/en/html | 2026-11-27 |
| s.160: CGT within provisional tax definition | https://www.irishstatutebook.ie/eli/2010/act/5/section/160/enacted/en/html | 2026-11-27 |
| Bill status, act field and dated stages | https://api.oireachtas.ie/v1/legislation?bill_year=2026&bill_no=98&limit=1 | 2026-11-27 |
| CGT clause, section 41 | https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/ver_b/b98b26d.pdf | 2026-11-27 |
| s.85: cessation events and four-month rule | https://www.irishstatutebook.ie/eli/1974/act/27/section/85/enacted/en/html | 2026-11-27 |
| s.2: Second Stage/recess deadline and dissolution | https://www.irishstatutebook.ie/eli/1991/act/32/section/2/enacted/en/html | 2026-11-27 |
| s.250: revised dissolution exclusion | https://www.irishstatutebook.ie/eli/1992/act/9/section/250/enacted/en/html | 2026-11-27 |
| s.552(1)–(5): costs and exclusions | https://www.irishstatutebook.ie/eli/1997/act/39/section/552/enacted/en/html | 2026-11-27 |
| s.554(1)–(2): income deduction overlap | https://www.irishstatutebook.ie/eli/1997/act/39/section/554/enacted/en/html | 2026-11-27 |
| s.546(1)–(6): loss scope and rate order | https://www.irishstatutebook.ie/eli/1997/act/39/section/546/enacted/en/html | 2026-11-27 |
| s.547(1)–(4): non-arm’s-length values | https://www.irishstatutebook.ie/eli/1997/act/39/section/547/enacted/en/html | 2026-11-27 |
| s.549(1)–(9): connected persons and restricted losses | https://www.irishstatutebook.ie/eli/1997/act/39/section/549/enacted/en/html | 2026-11-27 |
| s.556(2)–(4): indexation and rebasing safeguards | https://www.irishstatutebook.ie/eli/1997/act/39/section/556/enacted/en/html | 2026-11-27 |
| s.65: frozen statutory multiplier table | https://www.irishstatutebook.ie/eli/2003/act/3/section/65/enacted/en/html | 2026-11-27 |
| s.580(1)–(6): FIFO and its scope | https://www.irishstatutebook.ie/eli/1997/act/39/section/580/enacted/en/html | 2026-11-27 |
| s.581(1)–(5): four-week matching and restricted losses | https://www.irishstatutebook.ie/eli/1997/act/39/section/581/enacted/en/html | 2026-11-27 |
| Loss restrictions, carryforward, spouse and death headings | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx | 2026-11-27 |
| s.604(2)–(14): residence, periods and exclusions | https://www.irishstatutebook.ie/eli/1997/act/39/section/604/enacted/en/html | 2026-11-27 |
| PPR occupation, absence and restriction headings | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx | 2026-11-27 |
| s.35: original ER definitions/qualifying assets | https://www.irishstatutebook.ie/eli/2015/act/52/section/35/enacted/en/html | 2026-11-27 |
| s.24: current shareholding-period test | https://www.irishstatutebook.ie/eli/2020/act/26/section/24/enacted/en/html | 2026-11-27 |
| s.48: ER holding-company definition | https://www.irishstatutebook.ie/eli/2023/act/39/section/48/enacted/en/html | 2026-11-27 |
| s.30: connected-company restrictions/exceptions | https://www.irishstatutebook.ie/eli/2017/act/41/section/30/enacted/en/html | 2026-11-27 |
| ER limits, qualifying tests and exclusions headings | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx | 2026-11-27 |
| s.598(1)–(7): eligibility, shares and aggregation | https://www.irishstatutebook.ie/eli/1997/act/39/section/598/enacted/en/html | 2026-11-27 |
| Retirement thresholds, family, deferral and marginal-relief headings | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx | 2026-11-27 |
| s.55: twelve-year deferral and commercial reasons | https://www.irishstatutebook.ie/eli/2024/act/43/section/55/enacted/en/html | 2026-11-27 |
| s.93: site relief, repeat claims and clawback | https://www.irishstatutebook.ie/eli/2001/act/7/section/93/enacted/en/html | 2026-11-27 |
| s.53: garden area excludes construction site | https://www.irishstatutebook.ie/eli/2007/act/11/section/53/enacted/en/html | 2026-11-27 |
| s.30: child’s spouse/civil partner inclusion | https://www.irishstatutebook.ie/eli/2018/act/30/section/30/enacted/en/html | 2026-11-27 |
| Payment, return, registration and return-content headings | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx | 2026-11-27 |
| 2026 ROS extension announcement: eligible return/payment years | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-11-27 |
| s.71: replacement clearance eligibility | https://www.irishstatutebook.ie/eli/2003/act/3/section/71/enacted/en/html | 2026-11-27 |
| s.145: CGT interest scope and delay | https://www.irishstatutebook.ie/eli/2005/act/5/section/145/enacted/en/html | 2026-11-27 |
| s.29: interest table, 0.0219% | https://www.irishstatutebook.ie/eli/2009/act/12/section/29/enacted/en/html | 2026-11-27 |
| s.1084(1)–(5): scope, surcharge, deductions and exceptions | https://www.irishstatutebook.ie/eli/1997/act/39/section/1084/enacted/en/html | 2026-11-27 |

Not yet confirmed: specialist holds above and the conditional 2025 Galway absence claim are not usable conclusions. Future enactment/lapse after the read date, the applicable 2027 ROS extension, and record-specific destruction dates are not assumed. Check this point with one of our partner accountants.
