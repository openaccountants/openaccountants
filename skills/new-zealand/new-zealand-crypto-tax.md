---
name: new-zealand-crypto-tax
description: Use this skill whenever asked about New Zealand cryptocurrency or cryptoasset taxation in the 2027 income year (1 April 2026 to 31 March 2027). Trigger on phrases like "crypto tax New Zealand", "crypto tax NZ", "Bitcoin NZ tax", "IRD crypto", "cryptoassets NZ", "cryptocurrency gains NZ", "crypto income NZ", "staking NZ", "mining income NZ", "NFT tax NZ", "DeFi NZ tax", "IR3 crypto", "purpose of disposal crypto", "intention test crypto NZ", "GST crypto NZ", or any question about the income tax or GST treatment of cryptocurrency, tokens, or digital assets for New Zealand tax residents or NZ-source crypto income. Covers IRD cryptoasset guidance, the purpose-of-disposal test under s CB 4, GST exemption, cost basis, DeFi, staking, mining, airdrops, CARF and IR3 reporting. ALWAYS read this skill before touching any New Zealand crypto work.
version: "2.0"
jurisdiction: NZ
tax_year: 2026
tax_year_notes: "New Zealand income year 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. Crypto income is taxed at the ordinary rates; IRD's personal rate table is headed From 1 April 2025 and no later table exists."
last_updated: 2026-11-14
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - nz-income-tax-ir3
category: crypto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: situation-rules
---

# Crypto tax in New Zealand, 2027 income year

> **Source-cited draft.** Built from Inland Revenue's cryptoasset pages, QB 21/06, technical decision summary 25/23, Tax Information Bulletin Vol 34 No 5 and the IRRUIP18 landing page, re-read on 14 November 2026. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Scope

How New Zealand taxes an individual who buys, sells, swaps, stakes, mines or receives cryptoassets, and how GST applies. The year covered is the income year from 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. Inland Revenue's crypto pages print no crypto-specific rates or thresholds: crypto income is taxed at the ordinary rates. The rules come from Inland Revenue's cryptoasset pages and its technical publications: QB 21/06 on airdrops (June 2021), Tax Information Bulletin Vol 34 No 5 (June 2022) on GST, issues paper IRRUIP18 on DeFi (29 January 2026, initial views only) and technical decision summary 25/23 (October 2025, not binding). Names in square brackets point to Sources.

Not covered: companies, trusts, crypto businesses, crypto paid as salary (binding rulings BR Pub 23/04 to 23/07), non-residents.

| Field | Value |
| --- | --- |
| Country | New Zealand (Aotearoa) |
| Tax | Income tax on cryptoassets; GST where relevant |
| Currency | NZD. Each transaction is valued in New Zealand dollars at the time it happens |
| Tax year | 1 April to 31 March, named by the year it ends: 1 April 2026 to 31 March 2027 is the 2027 income year |
| Primary authority | Income Tax Act 2007, ss CA 1(2), CB 3, CB 4, CB 5, DB 23; Goods and Services Tax Act 1985, ss 2(1), 3, 20H |
| Tax authority | Inland Revenue (Te Tari Taake, IRD) |
| Filing portal | myIR |
| Filing deadline | IR3 by 7 July after the year ends, unless you have a tax agent or an extension of time (Filing and payment) |
| Capital gains tax | **No general capital gains tax.** Whether a crypto gain is taxable depends mainly on the PURPOSE of acquisition |
| Guide version | 2.0 (world standard rewrite, November 2026) |

### The central rule

**New Zealand has no general capital gains tax**, but Inland Revenue says "In most cases, the amounts you get from selling, trading or exchanging cryptoassets are taxable (this includes when you exchange one type of cryptoasset for another)" [Buying and selling]. The main test is the dominant purpose when the crypto was acquired. If it was acquired to sell or exchange at some point, the profit is income: "It does not matter how long you plan to hold onto your cryptoassets" [Acquiring to sell]. Calling it a "long-term investment" does not change that. Trading and profit-making schemes are also taxable.

## Ask the client first

1. Are you a New Zealand tax resident, and when did you arrive or return?
2. For each holding: why did you buy it, what research did you do, and is anything written down from that time?
3. Does it give you an income stream, and how does that compare with your sale gains?
4. How often do you trade, and how much time do you spend on it?
5. Did you receive airdrops, forks, mining rewards, NFTs or crypto for work?
6. Which exchanges, wallets and protocols (including overseas), and do you have full exports?

## The method, step by step

1. **Residency.** Confirm residency and any transitional resident exemption [Tax residence]; tests in [nz-tax-residency](nz-tax-residency.md). Unknown residency: STOP. Residents are taxed on worldwide income; non-residents on New Zealand-source income only.
2. **List everything.** List every acquisition and disposal across all wallets and platforms, New Zealand and overseas, and reconcile holdings at 31 March [Calculating income]. Transfers between your own wallets are not disposals [Buying and selling].
3. **Purpose test (s CB 4).** Test the dominant purpose at acquisition (below). If it fails, test trading and a profit-making scheme under s CB 3 [Acquiring to sell].
4. **Income on receipt.** Record income when received for staking, DeFi and mining rewards, crypto for services, and airdrops in the taxable cases of QB 21/06 (Boundary table).
5. **Disposals.** Work out each taxable disposal as sale price less cost less fees, by FIFO or weighted average cost, in NZD [Calculating income].
6. **GST.** Check GST on NFT sales, mining services and crypto taken as payment [Crypto and GST].
7. **Return.** Enter net crypto income or loss in the IR3 "other income" box, attach the calculation, file by 7 July unless there is a tax agent or extension of time, and check provisional tax [Declare].

### Legal classification

| Term | Definition | Authority |
| --- | --- | --- |
| Cryptoasset | "a form of property for tax purposes". Treatment depends on characteristics and use, not the name | [Cryptoassets] |
| Cryptocurrency vs NFT | An NFT is a cryptoasset but not "cryptocurrency". This matters for GST | Tax Information Bulletin Vol 34 No 5 |
| Excepted financial arrangement | Cryptocurrency is excepted under s EW 5(3BA) unless s EW 5(3BAB) applies (economically equivalent to debt). The legacy Guide cited "s EW 5(22B)": wrong | Tax Information Bulletin Vol 34 No 5 |
| Personal property | "the tax rules that apply to personal property apply to cryptoassets" | IRRUIP18 |

### The purpose-of-disposal test (s CB 4)

The key provision. Technical decision summary 25/23: "Under s CB 4, an amount that a person derives from disposing of personal property is income of the person if they acquired the property for the purpose of disposing of it."

Inland Revenue on purpose [Acquiring to sell]:

- "It is your main purpose that matters."
- Purpose is tested when you acquire (buy or mine). "If that purpose changes later on, it does not matter."
- "Just saying why you got your cryptoassets is not enough." Long-term investment, inflation hedge, diversification or store of value "usually still involve a purpose of eventually selling or exchanging".
- No income stream "strongly suggests" a disposal purpose (as for gold bullion, QB 17/08).
- An income stream such as staking is a factor, but does not by itself show a non-disposal purpose.
- If you expect to earn more from selling than from passive income, "your dominant purpose will most likely be acquiring cryptoassets for disposal."

| Factor | Indicates purpose of disposal (taxable) | Indicates NOT purpose of disposal |
| --- | --- | --- |
| Stated intent at purchase | "I'll sell when it goes up" | A documented plan to live on passive income. A statement alone is not enough |
| Nature of the asset | No income stream while held | An income stream researched and forecast before buying |
| Frequency of transactions | Many trades; buying low, selling at peaks | Rare transactions |
| Holding period | Held until it "had realised its full potential" (length alone does not help) | Held and used for passive income over a long period |
| Return comparison | Sale gains larger than passive income | Passive income is the main return |
| Reason for sale | Market timing | An unexpected need, such as a bill |

Inland Revenue's examples: "Leena" held a "long-term investment" with no income stream and was taxable. "Selina" bought a stablecoin to earn staking income and sold to pay an unexpected bill: rewards were income, but not the profit on the initial stablecoin.

### Other income provisions

| Provision | Description |
| --- | --- |
| s CB 3: Profit-making scheme | "a coherent plan of action (a scheme)" entered into to make a profit. "You do not need to write the plan down" [Profit-making scheme] |
| s CB 1, CB 2, CB 5: Business | A trader: many transactions, much time and effort, fairly continuous; crypto is then likely trading stock. A full-time employee is "probably not a trader" unless highly organised [Trading] |
| s CA 1(2): Ordinary income | Regular, recurrent receipts such as staking rewards (technical decision summary 25/23) |

### Burden of proof

The onus is on the taxpayer, on the balance of probabilities. In technical decision summary 25/23: "It was up to the taxpayers to prove the cryptoassets were not acquired with the dominant purpose of disposing of them." Not binding. The summary weighed: "Actions may speak louder than words"; years in the crypto industry; staking not available at purchase; buying low and selling at peaks; sale gains far above staking returns. The legacy Guide put "clear and compelling evidence" in that summary; the words come from Inland Revenue's web page: if you sell at a profit and claim no disposal purpose, "you will need clear and compelling evidence to support your claim" [Acquiring to sell].

### Cost basis

"To work out the cost of disposed cryptoassets you can use 1 of the following methods: first-in first-out (FIFO) weighted average cost (WAC)." [Calculating income]

| Method | Status |
| --- | --- |
| FIFO (first in, first out) | Named by Inland Revenue |
| Weighted average cost | Named by Inland Revenue |
| Specific identification | Not named. The legacy Guide said "accepted"; the Inland Revenue page names only FIFO and weighted average cost |
| LIFO | Not named. Use FIFO or weighted average cost |

- Apply one method consistently (prudent practice; not stated in those words by Inland Revenue).
- Part disposal: "calculate the cost of just that part." Unrealised gains and losses "are not taxable or deductible."
- Formula: income = sale price less purchase cost less transaction fees [Calculating income].

| Component | Included? |
| --- | --- |
| Purchase price in NZD at acquisition | Yes |
| Exchange, network and gas fees | Yes (transaction fees) |
| Fees on disposal | Yes, deducted |
| Crypto taxed on receipt (mining, staking, payment) and later sold | Cost = value when received |
| Airdropped crypto taxed only on disposal | Generally no cost apart from transaction fees (QB 21/06); IRD: "Generally no deduction is available for the cost of acquiring the cryptoassets from an airdrop or a hard fork" [Airdrops and forks] |

- **Trading stock.** Cryptoassets are excepted financial arrangements (except those economically equivalent to debt), so "if your cryptoassets are trading stock they are valued at cost at the end of the tax year" [Cryptoassets]. Mining rewards that are trading stock: cost (value on receipt) is deducted in the year the rewards are returned as income [Calculating income].
- **NZD conversion.** Value each transaction in NZD when it happens. IRRUIP18 says market value "can usually be obtained by looking up the value on a centralised exchange". The legacy "mid-market rate" rule is on no page read. Record a crypto-to-crypto exchange "as both a disposal and an acquisition" [Calculating income], at the market value of the cryptoasset received.

## Rates, bands and thresholds

| Item | Value | Conditions | Source |
| --- | --- | --- | --- |
| Individual rate, up to NZD 15,600 | 10.5% | IRD table "From 1 April 2025", no later table; no tax-free threshold | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals |
| Individual rate, NZD 15,601 to 53,500 | 17.5% | Each band rate applies only to income inside the band | same |
| Individual rate, NZD 53,501 to 78,100 | 30% | | same |
| Individual rate, NZD 78,101 to 180,000 | 33% | | same |
| Individual rate, NZD 180,001 and over | 39% | | same |
| Company rate, most companies | 28% | | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/tax-rates-for-businesses |
| Trustee rate, trust income NZD 10,000 or less | 33% | Undistributed income, from 1 April 2024 | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/trusts-and-estates/income/trustee-tax-rates |
| Trustee rate, trust income more than NZD 10,000 | 39% | Exceptions on the same page | same |
| GST compulsory registration | NZD 60,000 | "at least" this in the last 12 months or expected in the next 12; the NFT page says "more than" this of NFT sales in a 12-month period | https://www.ird.govt.nz/gst/registering-for-gst |
| GST standard rate (for example NFT sales to New Zealand buyers) | 15% | "The current rate is 15%." | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf |
| IR3 filing trigger | more than NZD 200 | Income (before tax) IRD was not told about | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3 |
| Provisional tax trigger | more than NZD 5,000 | Tax to pay at the end of the year from the last return | https://www.ird.govt.nz/income-tax/provisional-tax |
| Record retention | at least 7 years | "even if you no longer have any cryptoassets" | https://www.ird.govt.nz/cryptoassets/taxing/record-keeping |

Crypto income is added to other income; tax credits and codes are in [nz-income-tax-ir3](nz-income-tax-ir3.md). For the 2025 income year (1 April 2024 to 31 March 2025) IRD prints a separate table headed "From 1 April 2024 to 31 March 2025", with composite rates in some bands; the legacy Guide printed the current bands for that year, which was wrong. Use that table only for that year's returns.

## Boundary and exception table

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown purpose at acquisition | Treat as acquired for disposal (taxable). No income stream "strongly suggests" a disposal purpose |
| Trading vs investment unclear | Taxable until the client has clear and compelling evidence of a non-disposal purpose |
| Unknown cost method | FIFO or weighted average cost, the two methods Inland Revenue names. Apply one consistently |
| Staking rewards | Income when received, and taxable again on disposal (cost = value when received) |
| DeFi transaction | "if you lose possession of your cryptoassets with a DeFi product, you have made a disposal" [Calculating income] |
| GST on crypto | Buying and selling crypto is NOT subject to GST |
| Unknown tax residency | STOP. Residents: worldwide income. Non-residents: New Zealand-source only. See [nz-tax-residency](nz-tax-residency.md) |

### GST

| Transaction | GST treatment | Authority |
| --- | --- | --- |
| Buying and selling cryptoassets | **Not subject to GST.** "Cryptoassets are excluded from GST ... you do not need to register for GST." | [Crypto and GST] |
| Brokering cryptocurrency transfers | Exempt financial service, s 3(1)(lb) GST Act | Tax Information Bulletin Vol 34 No 5 |
| Crypto received as payment | Charge GST on the goods or services as normal, on the NZD value received. No GST on a later sale of that crypto | [Crypto and GST] |
| NFT sales | **GST applies** if you are registered or must register (a taxable activity, as for "Phil"). "NFTs are classified as a service for GST." Zero-rated to buyers outside New Zealand; royalties zero-rated | [NFTs] [Crypto and GST] |
| Mining service | A supply for GST, zero-rated for a blockchain outside New Zealand; input tax claimable | [Mining] |

The definitions of "goods" and "services" in s 2(1) GST Act exclude cryptocurrency, retrospectively from 1 January 2009 (Tax Information Bulletin Vol 34 No 5). The legacy Guide named the wrong amending Act (the 2024-25 rates Act). GST returns: [nz-gst-return](nz-gst-return.md).

### Mining

| Aspect | Treatment |
| --- | --- |
| Mining rewards | "In most cases, cryptoassets you get from mining (such as transaction fees and block rewards) are taxable" [Mining] |
| Classification | Business, profit-making scheme, ordinary income, or mined for disposal. Refer hobby mining claims |
| Cost basis of mined coins | Value when received, if taxed on receipt |
| Later sale | May be taxable again; no GST |
| GST | Zero-rated supply for a blockchain outside New Zealand |

### Staking

| Aspect | Treatment |
| --- | --- |
| Staking rewards | "The reward income is taxable when it is received. Any profit made when it is sold is also income." ("Chen", rewards from lending crypto to an exchange) [Acquiring to sell] |
| Rationale | Income under ordinary concepts (technical decision summary 25/23) |
| Cost basis | "the cost is the income amount when the reward was received" |
| Dominant purpose | Staking can support a non-disposal purpose for the ORIGINAL holding only with evidence ("Selina"). It did not in "Pete" or in technical decision summary 25/23 |
| Buy, stake and sell | A profit-making scheme: rewards and all sale profits taxable ("Tai" [Profit-making scheme]; "Ariana" on the Inland Revenue mining profit-making scheme page) |

### Airdrops and hard forks (QB 21/06)

| Aspect | Treatment |
| --- | --- |
| Receipt taxable only if | a cryptoasset business; part of a profit-making scheme; services provided for it; or regular airdrops with "hallmarks of income". "In other cases, the receipt is not taxable." |
| Promotional airdrop (unsolicited) | Not taxable on receipt unless a case above applies. The legacy Guide said taxable: QB 21/06 disagrees |
| Airdrop you signed up or did small tasks for | Receipt usually not taxable (unless one of the four cases above applies, for example the tokens are payment for services). Signing up shows you turned your mind to acquiring them, so a later disposal is taxable if you acquired them to dispose of them ("Beth", QB 21/06) |
| Airdrop you did nothing to get (no sign-up or opt-in) | Not acquired for disposal, so a later disposal is not taxable under s CB 4 ("Beth", QB 21/06 Example 2), unless you are in business or a scheme |
| Disposal taxable if | business; scheme; services; or acquired for disposal. "In many cases, the disposal will be taxable" |
| Cost | Generally only transaction fees. If taxed on receipt AND disposal, cost = value on receipt |
| Hard forks | QB 21/07 (not read). May be taxable "on either receipt, disposal or both" [Airdrops and forks] |

QB 21/06 is the current airdrop guidance. The legacy citation mixed up IRRUIP14 (December 2020) with IRRUIP18 (January 2026, DeFi).

### DeFi (IRRUIP18 initial views, not final)

IRRUIP18 gives initial views only; issues papers "are not authoritative statements". No final statement yet.

| Activity | Treatment |
| --- | --- |
| General test | Disposal when crypto moves to a pool, vault or contract you do not control and another holds the private key. No disposal if locked in your own wallet or an individual vault where you keep a key |
| Lending, yield farming | Rewards "are usually taxable when received"; a deposit into a pool is likely a disposal |
| Liquidity provision | Deposit = likely disposal; LP tokens received at market value; removing liquidity disposes of LP tokens |
| Wrapping, bridging (for example ETH to WETH) | Conservative: disposal and new acquisition; close together "there may be no net tax liability" |
| Impermanent loss | Not addressed by name. A loss arises only on a disposal (for example burning LP tokens), and only if the crypto is held on revenue account. No loss while still in the pool |
| Borrowing against crypto | Depends on whether collateral leaves your control; a liquidation is a disposal (if the collateral was not already disposed of) |

### NFTs [NFTs]

| Aspect | Treatment |
| --- | --- |
| Sale at profit | Taxable if your business creates NFTs, you buy and sell to profit, or you acquired them for disposal |
| Bought for personal use and enjoyment | "there is no tax to pay on their disposal"; clear and compelling evidence of purpose needed |
| Creation and sale | Business or profit-making scheme ("Phil"); costs deductible |
| Royalties | "income at the time they receive them"; zero-rated for GST [Crypto and GST] |
| GST on NFT sales | The standard rate on sales to New Zealand buyers; zero-rated abroad; register above the threshold in the rates table |

GST "will continue to apply to supplies of non-fungible tokens (NFTs)" (Tax Information Bulletin Vol 34 No 5).

### Losses

| Rule | Detail |
| --- | --- |
| Crypto disposal losses | Claimable ONLY if a profit would have been taxable ("Sione"). "To claim a loss, you need to show that if you'd made a profit it would have been taxable." |
| Offset order | "Losses from disposals can offset other cryptoasset profits, and then other income." [Calculating income] |
| Carry-forward, company continuity, carry-back | General income tax rules, not on the crypto pages and not checked. Confirm before relying on them |
| Stolen crypto | Separate Inland Revenue pages. Refer |
| Trading stock losses | Trading stock is valued at cost at year end, so a market fall below cost is not deducted until disposal |

Key principle: no loss if the profit would have been untaxed.

### Anti-avoidance

Section BG 1 of the Income Tax Act 2007 lets the Commissioner void a tax avoidance arrangement, including structures built to get around the purpose test. (Legacy statement; the statute is on a host that refused script access, see Not yet confirmed.)

### Residents, non-residents and transitional residents [Tax residence] [New residents]

| Status | Treatment |
| --- | --- |
| New Zealand tax resident | Worldwide crypto income taxable, including through an overseas exchange |
| Non-resident | "usually not subject to New Zealand tax" on crypto income, unless it has a New Zealand source |
| Transitional resident (new, or returning after 10 years) | "4-year temporary tax exemption on most types of foreign income", which "generally includes any tax on the sale of your cryptoassets" |
| Not exempt | New Zealand-source income (trading on a New Zealand exchange) and crypto paid for work done overseas |
| After the exemption | "You do not revalue your cryptoassets at the end of your exemption period." |

Transitional resident citation: section HR 8 Income Tax Act 2007; technical decision summary 24/22 (December 2024). Residence tests: [nz-tax-residency](nz-tax-residency.md).

### Information sharing

| Measure | Detail |
| --- | --- |
| CRS (Common Reporting Standard) | New Zealand participates |
| CARF | **Adopted** (legacy: "expected to adopt"). From 1 April 2026 reporting crypto-asset service providers with a New Zealand nexus collect user and residency details; the first reporting period covers 1 April 2026 to 31 March 2027, with the first report due by 30 June 2027; data also comes from other countries [CARF] |
| Penalties for users | Possible if users withhold or falsify identifying information |

### Prohibitions

- NEVER say New Zealand has a capital gains tax
- NEVER treat crypto profits as tax-free because the client calls it a long-term investment
- NEVER charge GST on buying or selling crypto
- NEVER ignore staking rewards: income when received
- NEVER allow a loss whose matching profit would be untaxed
- NEVER value crypto trading stock at market value at year end
- NEVER treat transfers between the client's own wallets as disposals
- NEVER ignore the transitional resident exemption
- NEVER present a purpose-test answer as final

## Worked cases

The legacy examples used made-up amounts; the amounts below are illustrative, the rates are IRD's.

**Case 1: Ether bought to sell, taxed or not? (decision).** A resident on a NZD 70,000 salary bought Ether in July 2026 planning to "sell at a target price" and sold in January 2027 at a NZD 12,000 profit (sale price less cost less fees). Bought to sell, so taxable under s CB 4. The first NZD 8,100 of profit is in the 30% band, the rest in the 33% band. Had the client proved, with clear and compelling evidence, a non-disposal purpose, the tax on the profit would be nil. Return: "other income" box of the IR3, due 7 July 2027.

```oa-check
name: Crypto profit on top of salary, 2027 income year
inputs:
  salary: 70000
  profit: 12000
  bought_to_sell: 1
steps:
  - taxable_profit: profit * bought_to_sell
  - in_30: min(salary + taxable_profit, 78100) - salary
  - in_33: taxable_profit - in_30
  - tax: in_30 * 0.30 + in_33 * 0.33
expected:
  taxable_profit: 12000
  in_30: 8100
  tax: 3717.00
```

**Case 2: staking rewards taxed on receipt and on sale.** A resident bought a staking coin in May 2026 after forecasting staking income against sale gains, and sold some rewards in February 2027. Rewards worth NZD 1,000 when received were later sold for NZD 1,300, in the 33% band. Income is NZD 1,000 on receipt plus a NZD 300 gain on sale. The original coins are not sold; if sold later, the client may argue a passive income purpose ("Selina"); the onus is on the client.

```oa-check
name: Staking rewards taxed on receipt and on sale
inputs:
  received: 1000
  proceeds: 1300
  rate: 0.33
steps:
  - gain: proceeds - received
  - tax: (received + gain) * rate
expected:
  gain: 300.00
  tax: 429.00
```

**Case 3: long-term holder (legacy said not taxable).** A resident bought Bitcoin in 2019 as a documented "store of value" and sold in 2026 after a medical emergency. A store of value "usually still" involves eventual disposal, and Bitcoin gives no income stream ("Leena"). Result: LIKELY TAXABLE. The legacy Guide said "likely not taxable". A forced sale is one factor Inland Revenue looks at, but it does not change the purpose at ACQUISITION. Only clear and compelling evidence could support a nil position: refer.

## When to refuse or refer

- A firm "not taxable" answer for a claimed long-term investment.
- Crypto businesses, trading stock, companies and trusts.
- Salary, bonuses or share schemes paid in crypto.
- Complex DeFi, hard forks, stolen or lost crypto, scams.
- Non-residents with New Zealand-source income, treaty cases, transitional resident edge cases.
- Undeclared past income (voluntary disclosure), and clients with no usable records.

## Filing and payment

| Requirement | Detail |
| --- | --- |
| Return type | IR3, Individual income tax return. "You need to file an income tax return - IR3 when you have taxable income from a cryptoasset activity" [Taxing] |
| When an IR3 is needed | More than NZD 200 (before tax) of income IRD was not told about (rates table) |
| Filing deadline | By 7 July "unless you have a tax agent or an extension of time" [IR3]. For the 2027 income year: 7 July 2027 |
| Extended deadline (tax agent) | The legacy "31 March of the following year" is on no page read: confirm with the agent ([nz-income-tax-ir3](nz-income-tax-ir3.md)) |
| Crypto section | No crypto schedule. If it fits no other box, net crypto income or loss goes in the "other income" box; attach the calculation [Declare] |
| Provisional tax | Applies if the tax to pay at the end of the year from the last return was more than NZD 5,000. A large crypto gain can bring the client into provisional tax the next year. Dates and options: [nz-provisional-tax](nz-provisional-tax.md) |
| Records | Keep for at least 7 years: type of cryptoasset, date, type of transaction, units, NZD value, units held at start and end of year, exchange records and bank statements, wallet addresses [Records]. Also keep the research and forecasts made at acquisition: not on IRD's list, but the purpose test turns on it |

## Completion checklist

- [ ] Residency and transitional resident status confirmed?
- [ ] Dominant purpose at acquisition, with evidence beyond the client's word?
- [ ] One cost method (FIFO or weighted average cost) applied consistently?
- [ ] Staking, mining and taxable airdrop receipts included as income?
- [ ] GST: none on crypto trades; NFT sales to New Zealand buyers carry GST if the seller is registered or must register?
- [ ] Loss claim: would a profit have been taxable?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| [Cryptoassets] IRD cryptoassets hub: read for "a form of property for tax purposes" and trading stock at cost | https://www.ird.govt.nz/cryptoassets | 2026-11-14 |
| [Buying and selling] IRD: read for the general rule that selling, trading or exchanging is usually taxable, and own-wallet transfers | https://www.ird.govt.nz/cryptoassets/individual/buying-selling | 2026-11-14 |
| [Acquiring to sell] IRD: read for the dominant purpose test, "clear and compelling evidence", Leena, Selina, Chen and Pete | https://www.ird.govt.nz/cryptoassets/individual/buying-selling/acquiring-sell-exchange | 2026-11-14 |
| [Profit-making scheme] IRD: read for s CB 3 and Tai | https://www.ird.govt.nz/cryptoassets/individual/buying-selling/profit-making-scheme | 2026-11-14 |
| [Trading] IRD: read for when a person is a trader | https://www.ird.govt.nz/cryptoassets/individual/buying-selling/trading | 2026-11-14 |
| [Mining] IRD: read for mining rewards and GST on mining services | https://www.ird.govt.nz/cryptoassets/individual/mining | 2026-11-14 |
| [Airdrops and forks] IRD: read for "taxable on either receipt, disposal or both" and no deduction for cost (section landing page only) | https://www.ird.govt.nz/cryptoassets/individual/airdrops-and-hard-forks | 2026-11-14 |
| [Tax residence] IRD: read for residents and non-residents | https://www.ird.govt.nz/cryptoassets/individual/tax-residence | 2026-11-14 |
| [New residents] IRD: read for the transitional exemption and no revaluation at its end | https://www.ird.govt.nz/cryptoassets/individual/tax-residence/new-returning | 2026-11-14 |
| [Taxing] IRD: read for when an IR3 is needed for crypto | https://www.ird.govt.nz/cryptoassets/taxing | 2026-11-14 |
| [Calculating income] IRD: read for FIFO and WAC, the income formula, DeFi possession, exchanges and loss offset | https://www.ird.govt.nz/cryptoassets/taxing/income-expenses/calculating-cryptoasset-income | 2026-11-14 |
| [Crypto and GST] IRD: read for GST exclusion, crypto as payment, NFT royalties | https://www.ird.govt.nz/cryptoassets/taxing/cryptoassets-and-gst | 2026-11-14 |
| [Declare] IRD: read for the "other income" box and attaching the calculation | https://www.ird.govt.nz/cryptoassets/taxing/declare-cryptoasset-income-or-loss | 2026-11-14 |
| [Records] IRD: read for the 7-year retention and the records list | https://www.ird.govt.nz/cryptoassets/taxing/record-keeping | 2026-11-14 |
| [NFTs] IRD: read for NFT income, GST as a service, the NZD 60,000 "more than" wording and Phil | https://www.ird.govt.nz/cryptoassets/non-fungible-tokens | 2026-11-14 |
| [CARF] IRD CARF overview: read for the 1 April 2026 start and the 30 June 2027 first report | https://www.ird.govt.nz/international-tax/exchange-of-information/crypto-asset-reporting-framework/crypto-asset-reporting-framework-overview | 2026-11-14 |
| [IR3] IRD Individual income tax return IR3: read for the NZD 200 trigger and 7 July deadline | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3 | 2026-11-14 |
| IRD Tax rates for individuals: read for the "From 1 April 2025" table and the 2024-25 composite table | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals | 2026-11-14 |
| IRD Tax rates for businesses: read for "Most companies 28%" | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/tax-rates-for-businesses | 2026-11-14 |
| IRD Trustee tax rates: read for the NZD 10,000 switch and 33% / 39% | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/trusts-and-estates/income/trustee-tax-rates | 2026-11-14 |
| IRD Registering for GST: read for the NZD 60,000 "at least" threshold | https://www.ird.govt.nz/gst/registering-for-gst | 2026-11-14 |
| IRD guide IR295 (April 2026): read for "The current rate is 15%" | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf | 2026-11-14 |
| IRD Provisional tax: read for the NZD 5,000 trigger | https://www.ird.govt.nz/income-tax/provisional-tax | 2026-11-14 |
| QB 21/06 (June 2021): read for when airdrops are taxable on receipt and disposal, and Beth | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/questions-we-ve-been-asked/2021/qb-21-06.pdf | 2026-11-14 |
| Technical decision summary 25/23 (October 2025): read for the s CB 4 quote, onus of proof and the staking facts | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/tds/2025/tds-25-23.pdf?modified=20251006020051 | 2026-11-14 |
| IRRUIP18 (29 January 2026): read for the landing page and status as initial views; the paper itself was not opened | https://www.taxtechnical.ird.govt.nz/consultations/2026/irruip18 | 2026-11-14 |
| Tax Information Bulletin Vol 34 No 5 (June 2022): read for the GST exclusion of cryptocurrency from 1 January 2009, s EW 5(3BA) and NFTs | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/tib/volume-34---2022/tib-vol-34-no5.pdf?modified=20220803034927&modified=20220803034927 | 2026-11-14 |

Not yet confirmed: the IRRUIP18 DeFi views as read in the paper itself (only the landing page was opened; the DeFi table rests on the earlier reading and stays labelled initial views); QB 21/07 on hard forks (not read); the statutory text of ss BG 1, CB 4 and HR 8 (legislation.govt.nz refused script access on 14 November 2026); loss carry-forward rules; the tax agent extended filing date.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant (CA), tax advisor, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.
