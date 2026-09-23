---
name: new-zealand-crypto-tax
description: Use this skill whenever asked about New Zealand cryptocurrency or cryptoasset taxation. Trigger on phrases like "crypto tax New Zealand", "crypto tax NZ", "Bitcoin NZ tax", "IRD crypto", "cryptoassets NZ", "cryptocurrency gains NZ", "crypto income NZ", "staking NZ", "mining income NZ", "NFT tax NZ", "DeFi NZ tax", "IR3 crypto", "purpose of disposal crypto", "intention test crypto NZ", "GST crypto NZ", or any question about the income tax or GST treatment of cryptocurrency, tokens, or digital assets for New Zealand tax residents or NZ-source crypto income. Covers IRD cryptoasset guidance, the purpose-of-disposal test under s CB 4, GST exemption, cost basis, DeFi/staking/mining, and IR3 reporting. ALWAYS read this skill before touching any New Zealand crypto work.
version: 1.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - new-zealand-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Crypto tax in New Zealand

How New Zealand taxes an individual who buys, sells, swaps, stakes, mines or receives cryptoassets, and how GST applies. Figures are for tax year 2026. In New Zealand that is the income year from 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. Inland Revenue's crypto pages print no crypto-specific rates or thresholds: crypto income is taxed at the ordinary rates. The personal rate table is headed "From 1 April 2025"; no later table exists. The rules come from Inland Revenue's cryptoasset pages (read 22 September 2026) and its technical publications: QB 21/06 on airdrops (June 2021), Tax Information Bulletin Vol 34 No 5 (June 2022) on GST, issues paper IRRUIP18 on DeFi (29 January 2026, initial views only) and technical decision summary 25/23 (October 2025, not binding). Names in brackets point to Sources.

Not covered: companies, trusts, crypto businesses, crypto paid as salary (binding rulings BR Pub 23/04 to 23/07), non-residents.

## Section 1: Quick Reference

**Section 1: Quick Reference**

| Field | Value |
| --- | --- |
| Country | New Zealand (Aotearoa) |
| Tax | Income tax on cryptoassets; GST where relevant |
| Currency | NZD. Each transaction is valued in New Zealand dollars at the time it happens |
| Tax year | 1 April to 31 March, named by the year it ends: 1 April 2026 to 31 March 2027 is the 2027 income year |
| Primary authority | Income Tax Act 2007, ss CA 1(2), CB 3, CB 4, CB 5, DB 23; Goods and Services Tax Act 1985, ss 2(1), 3, 20H |
| Tax authority | Inland Revenue (Te Tari Taake, IRD) |
| Filing portal | myIR |
| Filing deadline | IR3 by 7 July after the year ends, unless you have a tax agent or an extension of time (Section 7) |
| Capital gains tax | **No general capital gains tax.** Whether a crypto gain is taxable depends mainly on the PURPOSE of acquisition |
| Validated by | Pending. Requires sign-off by a New Zealand Chartered Accountant (CA) or tax advisor |
| Guide version | 2.0 (2026 refresh) |

### The Central Rule

**New Zealand has no general capital gains tax**, but Inland Revenue says "In most cases, the amounts you get from selling, trading or exchanging cryptoassets are taxable (this includes when you exchange one type of cryptoasset for another)" [Buying and selling]. The main test is the dominant purpose when the crypto was acquired. If it was acquired to sell or exchange at some point, the profit is income: "It does not matter how long you plan to hold onto your cryptoassets" [Acquiring to sell]. Calling it a "long-term investment" does not change that. Trading and profit-making schemes are also taxable.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown purpose at acquisition | Treat as acquired for disposal (taxable). No income stream "strongly suggests" a disposal purpose |
| Trading vs investment unclear | Taxable until the client has clear and compelling evidence of a non-disposal purpose |
| Unknown cost method | FIFO or weighted average cost, the two methods Inland Revenue names. Apply one consistently |
| Staking rewards | Income when received, and taxable again on disposal (cost = value when received) |
| DeFi transaction | "if you lose possession of your cryptoassets with a DeFi product, you have made a disposal" [Calculating income] |
| GST on crypto | Buying and selling crypto is NOT subject to GST |
| Unknown tax residency | STOP. Residents: worldwide income. Non-residents: New Zealand-source only. See `nz-tax-residency` |

## Section 2: Classification Rules

**Section 2: Classification Rules**

### 2.1 Legal Classification

**2.1 Legal Classification**

| Term | Definition | Authority |
| --- | --- | --- |
| Cryptoasset | "a form of property for tax purposes". Treatment depends on characteristics and use, not the name | [Cryptoassets] |
| Cryptocurrency vs NFT | An NFT is a cryptoasset but not "cryptocurrency". This matters for GST (3.4) | Tax Information Bulletin Vol 34 No 5 |
| Excepted financial arrangement | Cryptocurrency is excepted under s EW 5(3BA) unless s EW 5(3BAB) applies (economically equivalent to debt). The legacy Guide cited "s EW 5(22B)": wrong | Tax Information Bulletin Vol 34 No 5 |
| Personal property | "the tax rules that apply to personal property apply to cryptoassets" | IRRUIP18 |

### 2.2 The Purpose-of-Disposal Test (s CB 4)

The **key provision**. Technical decision summary 25/23: "Under s CB 4, an amount that a person derives from disposing of personal property is income of the person if they acquired the property for the purpose of disposing of it."

Inland Revenue on purpose [Acquiring to sell]:

- "It is your main purpose that matters."
- Purpose is tested when you acquire (buy or mine). "If that purpose changes later on, it does not matter."
- "Just saying why you got your cryptoassets is not enough." Long-term investment, inflation hedge, diversification or store of value "usually still involve a purpose of eventually selling or exchanging".
- No income stream "strongly suggests" a disposal purpose (as for gold bullion, QB 17/08).
- An income stream such as staking is a factor, but does not by itself show a non-disposal purpose.
- If you expect to earn more from selling than from passive income, "your dominant purpose will most likely be acquiring cryptoassets for disposal."

**Purpose-of-Disposal Test factors table**

| Factor | Indicates Purpose of Disposal (Taxable) | Indicates NOT Purpose of Disposal |
| --- | --- | --- |
| Stated intent at purchase | "I'll sell when it goes up" | A documented plan to live on passive income. A statement alone is not enough |
| Nature of the asset | No income stream while held | An income stream researched and forecast before buying |
| Frequency of transactions | Many trades; buying low, selling at peaks | Rare transactions |
| Holding period | Held until it "had realised its full potential" (length alone does not help) | Held and used for passive income over a long period |
| Return comparison | Sale gains larger than passive income | Passive income is the main return |
| Reason for sale | Market timing | An unexpected need, such as a bill |

Inland Revenue's examples: "Leena" held a "long-term investment" with no income stream and was taxable. "Selina" bought a stablecoin to earn staking income and sold to pay an unexpected bill: rewards were income, but not the profit on the initial stablecoin.

### 2.3 Other Income Provisions

**Other Income Provisions table**

| Provision | Description |
| --- | --- |
| s CB 3: Profit-making scheme | "a coherent plan of action (a scheme)" entered into to make a profit. "You do not need to write the plan down" [Profit-making scheme] |
| s CB 1, CB 2, CB 5: Business | A trader: many transactions, much time and effort, fairly continuous; crypto is then likely trading stock. A full-time employee is "probably not a trader" unless highly organised [Trading] |
| s CA 1(2): Ordinary income | Regular, recurrent receipts such as staking rewards (technical decision summary 25/23) |

### 2.4 Burden of Proof

- **Burden of proof.** The onus is on the taxpayer, on the balance of probabilities. In technical decision summary 25/23: "It was up to the taxpayers to prove the cryptoassets were not acquired with the dominant purpose of disposing of them." Not binding. The legacy Guide put "clear and compelling evidence" in that summary; the words come from Inland Revenue's web page: if you sell at a profit and claim no disposal purpose, "you will need clear and compelling evidence to support your claim" [Acquiring to sell].

## Section 3: Rate Tables

**Section 3: Rate Tables**

### 3.1 Individual Income Tax Rates (2027 income year: 1 April 2026 to 31 March 2027)

**Individual income tax rates, 2027 income year**

| Taxable income | Rate on each dollar in the band | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals |
| Up to NZD 15,600 | 10.5% | Table headed "From 1 April 2025" |
| Over NZD 15,600 up to NZD 53,500 | 17.5% | Same table |
| Over NZD 53,500 up to NZD 78,100 | 30% | Same table |
| Over NZD 78,100 up to NZD 180,000 | 33% | Same table |
| From NZD 180,001 | 39% | "and over" |

- **No tax-free threshold.** The first band starts at the first dollar.
- **Crypto income aggregation.** Taxable crypto income is added to other income; each band rate applies only to income inside that band. Tax credits and codes: `nz-income-tax-ir3`.

### 3.2 Prior Year Rates (2024/25 Tax Year: 1 April 2024 to 31 March 2025)

The legacy Guide printed the current bands for this year. Wrong: the page in 3.1 prints a separate table for it, headed "From 1 April 2024 to 31 March 2025", with composite rates in some bands. Use that only for this year's returns.

### 3.3 Company Tax Rate

**Company rate**

| Entity | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/tax-rates-for-businesses |
| Most companies | 28% | "Most companies 28%" |

**Trustee rates**

| Entity | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/trusts-and-estates/income/trustee-tax-rates |
| Trust income level that switches the rate | NZD 10,000 | "If your trust earns more than" this |
| Trustee rate above that level | 39% | "you'll need to pay 39%" |
| Trustee rate at or below that level | 33% | "you'll pay at a 33% rate" |

### 3.4 GST

**GST treatment table**

| Transaction | GST Treatment | Authority |
| --- | --- | --- |
| Buying and selling cryptoassets | **Not subject to GST.** "Cryptoassets are excluded from GST ... you do not need to register for GST." | [Crypto and GST] |
| Brokering cryptocurrency transfers | Exempt financial service, s 3(1)(lb) GST Act | Tax Information Bulletin Vol 34 No 5 |
| Crypto received as payment | Charge GST on the goods or services as normal, on the NZD value received. No GST on a later sale of that crypto | [Crypto and GST] |
| NFT sales | **GST applies** if you are registered or must register (a taxable activity, as for "Phil"). "NFTs are classified as a service for GST." Zero-rated to buyers outside New Zealand; royalties zero-rated | [NFTs] [Crypto and GST] |
| Mining service | A supply for GST, zero-rated for a blockchain outside New Zealand; input tax claimable | [Mining] |

**GST registration**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst |
| Compulsory registration: turnover in the last 12 months, or expected in the next 12 | NZD 60,000 | This page says "at least" this; the NFT page says "more than" this of NFT sales "in a 12-month period" |

**GST rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf |
| Standard rate, for example on NFT sales to New Zealand buyers | 15% | "The current rate is 15%." |

- **GST amendment.** The definitions of "goods" and "services" in s 2(1) GST Act exclude cryptocurrency, retrospectively from 1 January 2009 (Tax Information Bulletin Vol 34 No 5). The legacy Guide named the wrong amending Act (the 2024-25 rates Act). See `new-zealand-gst` and `nz-gst-return`.

## Section 4: Cost Basis Methods

**Section 4: Cost Basis Methods**

### 4.1 Accepted Methods

"To work out the cost of disposed cryptoassets you can use 1 of the following methods: first-in first-out (FIFO) weighted average cost (WAC)." [Calculating income]

**Accepted Methods table**

| Method | Status |
| --- | --- |
| FIFO (First In, First Out) | Named by Inland Revenue |
| Weighted average cost | Named by Inland Revenue |
| Specific identification | Not named. The legacy Guide said "accepted"; the Inland Revenue page names only FIFO and weighted average cost |
| LIFO | Not named. Use FIFO or weighted average cost |

- **Consistency requirement.** Apply one method consistently (prudent practice; not stated in those words by Inland Revenue).
- Part disposal: "calculate the cost of just that part." Unrealised gains and losses "are not taxable or deductible."

### 4.2 Cost Basis Components

Formula: income = sale price less purchase cost less transaction fees [Calculating income].

**Cost Basis Components table**

| Component | Included? |
| --- | --- |
| Purchase price in NZD at acquisition | Yes |
| Exchange, network and gas fees | Yes (transaction fees) |
| Fees on disposal | Yes, deducted |
| Crypto taxed on receipt (mining, staking, payment) and later sold | Cost = value when received |
| Airdropped crypto taxed only on disposal | Generally no cost apart from transaction fees (QB 21/06) |

### 4.3 Trading Stock Rules

- **Trading stock valuation.** Cryptoassets are excepted financial arrangements (except those economically equivalent to debt), so "if your cryptoassets are trading stock they are valued at cost at the end of the tax year" [Cryptoassets]. Mining rewards that are trading stock: cost (value on receipt) is deducted in the year the rewards are returned as income [Calculating income].

### 4.4: NZD Conversion

- **NZD conversion method.** Value each transaction in NZD when it happens. IRRUIP18 says market value "can usually be obtained by looking up the value on a centralised exchange". The legacy "mid-market rate" rule is on no page read. Record a crypto-to-crypto exchange "as both a disposal and an acquisition" [Calculating income], at the market value of the cryptoasset received.
- Include all wallets and platforms, New Zealand and overseas; reconcile holdings at 31 March [Calculating income].

## Section 5: DeFi / Staking / Mining / Airdrop Treatment

**Section 5: DeFi, Staking, Mining, Airdrop Treatment**

### 5.1 Mining

**Mining table**

| Aspect | Treatment |
| --- | --- |
| Mining rewards | "In most cases, cryptoassets you get from mining (such as transaction fees and block rewards) are taxable" [Mining] |
| Classification | Business, profit-making scheme, ordinary income, or mined for disposal. Refer hobby mining claims |
| Cost basis of mined coins | Value when received, if taxed on receipt |
| Later sale | May be taxable again; no GST |
| GST | Zero-rated supply for a blockchain outside New Zealand (3.4) |

### 5.2 Staking

**Staking table**

| Aspect | Treatment |
| --- | --- |
| Staking rewards | "The reward income is taxable when it is received. Any profit made when it is sold is also income." ("Chen", rewards from lending crypto to an exchange) [Acquiring to sell] |
| Rationale | Income under ordinary concepts (technical decision summary 25/23) |
| Cost basis | "the cost is the income amount when the reward was received" |
| Dominant purpose | Staking can support a non-disposal purpose for the ORIGINAL holding only with evidence ("Selina"). It did not in "Pete" or in technical decision summary 25/23 |
| Buy, stake and sell | A profit-making scheme: rewards and all sale profits taxable ("Tai" [Profit-making scheme]; "Ariana" on the Inland Revenue mining profit-making scheme page) |

### 5.3 Airdrops

**Airdrops table** (QB 21/06)

| Aspect | Treatment |
| --- | --- |
| Receipt taxable only if | a cryptoasset business; part of a profit-making scheme; services provided for it; or regular airdrops with "hallmarks of income". "In other cases, the receipt is not taxable." |
| Promotional airdrop (unsolicited) | Not taxable on receipt unless a case above applies. The legacy Guide said taxable: QB 21/06 disagrees |
| Airdrop you signed up or did small tasks for | Receipt usually not taxable (unless one of the four cases above applies, for example the tokens are payment for services). Signing up shows you turned your mind to acquiring them, so a later disposal is taxable if you acquired them to dispose of them ("Beth", QB 21/06) |
| Airdrop you did nothing to get (no sign-up or opt-in) | Not acquired for disposal, so a later disposal is not taxable under s CB 4 ("Beth", QB 21/06 Example 2), unless you are in business or a scheme |
| Disposal taxable if | business; scheme; services; or acquired for disposal. "In many cases, the disposal will be taxable" |
| Cost | Generally only transaction fees. If taxed on receipt AND disposal, cost = value on receipt |
| Hard forks | QB 21/07 (not read). May be taxable "on either receipt, disposal or both" [Airdrops and forks] |

- **Airdrop citation.** QB 21/06 is the current guidance. The legacy citation mixed up IRRUIP14 (December 2020) with IRRUIP18 (January 2026, DeFi).

### 5.4 DeFi

IRRUIP18 gives initial views only; issues papers "are not authoritative statements". No final statement yet.

**DeFi table (IRRUIP18 initial views, not final)**

| Activity | Treatment |
| --- | --- |
| General test | Disposal when crypto moves to a pool, vault or contract you do not control and another holds the private key. No disposal if locked in your own wallet or an individual vault where you keep a key |
| Lending, yield farming | Rewards "are usually taxable when received"; a deposit into a pool is likely a disposal |
| Liquidity provision | Deposit = likely disposal; LP tokens received at market value; removing liquidity disposes of LP tokens |
| Wrapping, bridging (for example ETH to WETH) | Conservative: disposal and new acquisition; close together "there may be no net tax liability" |
| Impermanent loss | Not addressed by name. A loss arises only on a disposal (for example burning LP tokens), and only if the crypto is held on revenue account (8.1). No loss while still in the pool |
| Borrowing against crypto | Depends on whether collateral leaves your control; a liquidation is a disposal (if the collateral was not already disposed of) |

## Section 6: NFT Treatment

**NFT Treatment table** [NFTs]

| Aspect | Treatment |
| --- | --- |
| Sale at profit | Taxable if your business creates NFTs, you buy and sell to profit, or you acquired them for disposal |
| Bought for personal use and enjoyment | "there is no tax to pay on their disposal"; clear and compelling evidence of purpose needed |
| Creation and sale | Business or profit-making scheme ("Phil"); costs deductible |
| Royalties | "income at the time they receive them"; zero-rated for GST [Crypto and GST] |
| GST on NFT sales | The rate in 3.4 on sales to New Zealand buyers; zero-rated abroad; register above the 3.4 threshold |

- **NFT GST exemption note.** GST "will continue to apply to supplies of non-fungible tokens (NFTs)" (Tax Information Bulletin Vol 34 No 5).

## Section 7: Reporting Requirements

**Section 7: Reporting Requirements**

### 7.1 Individual Filing

**Individual Filing table**

| Requirement | Detail |
| --- | --- |
| Return type | IR3, Individual income tax return |
| Filing deadline | By 7 July "unless you have a tax agent or an extension of time" [IR3]. For the 2027 income year: 7 July 2027 |
| Extended deadline (tax agent) | The legacy "31 March of the following year" is on no page read: confirm with the agent (`nz-income-tax-ir3`) |
| Crypto section | No crypto schedule. If it fits no other box, net crypto income or loss goes in the "other income" box; attach the calculation [Declare] |
| Loss to claim | "To claim a loss, you need to show that if you'd made a profit it would have been taxable." |

### 7.2 When Must You File an IR3?

**IR3 filing trigger**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3 |
| File if you received more than this (before tax) in income Inland Revenue was not told about | NZD 200 | "more than" this "(before tax)" |

"You need to file an income tax return - IR3 when you have taxable income from a cryptoasset activity" [Taxing].

### 7.3 Provisional Tax

**Provisional Tax table**

| Who | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax |
| Applies if the tax to pay at the end of the year from the last return was more than this | NZD 5,000 | "more than" this "tax at the end of the year" |

Dates and options: `nz-provisional-tax`. A large crypto gain can bring the client into provisional tax the next year.

### 7.4 Record-Keeping

**Record-Keeping table** [Records]

| Requirement | Detail |
| --- | --- |
| Retention period | "at least 7 years, even if you no longer have any cryptoassets" |
| Records | Type of cryptoasset, date, type of transaction, units, NZD value, units held at start and end of year, exchange records and bank statements, wallet addresses |
| Purpose evidence | Research and forecasts made at acquisition (2.2). Not on the list, but the purpose test turns on it |

## Section 8: Loss Offset and Carry-Forward

**Section 8: Loss Offset and Carry-Forward**

### 8.1 Loss Offset Rules

**Loss Offset Rules table**

| Rule | Detail |
| --- | --- |
| Crypto disposal losses | Claimable ONLY if a profit would have been taxable ("Sione") |
| Offset order | "Losses from disposals can offset other cryptoasset profits, and then other income." [Calculating income] |
| Carry-forward, company continuity, carry-back | General income tax rules, not on the crypto pages and not checked. Confirm before relying on them |
| Stolen crypto | Separate Inland Revenue pages. Refer |

### 8.2 Key Principle

- **Key principle for claiming loss.** No loss if the profit would have been untaxed.

### 8.3 Trading Stock Losses

- **Trading stock losses.** Trading stock is valued at cost at year end (4.3), so a market fall below cost is not deducted until disposal.

## Section 9: Anti-Avoidance Rules

**Section 9: Anti-Avoidance Rules**

### 9.1 General Anti-Avoidance (s BG 1)

- **General anti-avoidance rule.** Section BG 1 of the Income Tax Act 2007 lets the Commissioner void a tax avoidance arrangement, including structures built to get around the purpose test. (Legacy statement; the statute is on a blocked host.)

### 9.2 Aggressive Position: "Clear and Compelling Evidence"

See 2.4. Technical decision summary 25/23 weighed: "Actions may speak louder than words"; years in the crypto industry; staking not available at purchase; buying low and selling at peaks; sale gains far above staking returns.

### 9.3 Transitional Residents

**Transitional Residents table** [Tax residence] [New residents]

| Status | Treatment |
| --- | --- |
| New Zealand tax resident | Worldwide crypto income taxable, including through an overseas exchange |
| Non-resident | "usually not subject to New Zealand tax" on crypto income, unless it has a New Zealand source |
| Transitional resident (new, or returning after 10 years) | "4-year temporary tax exemption on most types of foreign income", which "generally includes any tax on the sale of your cryptoassets" |
| Not exempt | New Zealand-source income (trading on a New Zealand exchange) and crypto paid for work done overseas |
| After the exemption | "You do not revalue your cryptoassets at the end of your exemption period." |

- **Transitional resident citation.** Section HR 8 Income Tax Act 2007; technical decision summary 24/22 (December 2024). Residence tests: `nz-tax-residency`.

### 9.4 Information Sharing

**Information Sharing table**

| Measure | Detail |
| --- | --- |
| CRS (Common Reporting Standard) | New Zealand participates |
| CARF | **Adopted** (legacy: "expected to adopt"). From 1 April 2026 New Zealand crypto-asset service providers collect user and residency details; first report due by 30 June 2027; data also comes from other countries [CARF] |
| Penalties for users | Possible if users withhold or falsify identifying information |

## Section 10: Worked Examples

The legacy examples used made-up amounts; they are now in words.

### Example 1: Crypto Acquired for Purpose of Disposal (Taxable)

A resident on a salary bought Ether in July 2026 planning to "sell at a target price" and sold in January 2027 at a profit.

~~~
Income:    sale price less purchase cost less transaction fees
Purpose:   bought to sell, so TAXABLE (s CB 4)
Rate:      added to salary; each dollar taxed at its band rate (3.1)
Return:    "other income" box of the IR3, due 7 July 2027
~~~

### Example 2: Staking Rewards with Non-Disposal Purpose on Underlying

A resident bought a staking coin in May 2026 after forecasting staking income against sale gains, and sold some rewards in February 2027.

~~~
Rewards:          income at NZD value when received
Rewards sold:     gain = proceeds less value taxed on receipt
Original coins:   not sold. If sold later, the client may argue a passive
                  income purpose ("Selina"); the onus is on the client.
~~~

### Example 3: Long-Term Holder (legacy said NOT Taxable)

A resident bought Bitcoin in 2019 as a documented "store of value" and sold in 2026 after a medical emergency.

~~~
Purpose:  a store of value "usually still" involves eventual disposal, and
          Bitcoin gives no income stream ("Leena").
Result:   LIKELY TAXABLE. The legacy Guide said "likely not taxable". A
          forced sale is one factor Inland Revenue looks at, but it does not
          change the purpose at ACQUISITION.
Refer:    only clear and compelling evidence could support a nil position.
~~~

## Self-Checks

- [ ] Residency and transitional resident status confirmed?
- [ ] Dominant purpose at acquisition, with evidence beyond the client's word?
- [ ] One cost method (FIFO or weighted average cost) applied consistently?
- [ ] Staking, mining and taxable airdrop receipts included as income?
- [ ] GST: none on crypto trades; NFT sales to New Zealand buyers carry GST if the seller is registered or must register?
- [ ] Loss claim: would a profit have been taxable?

## PROHIBITIONS

- NEVER say New Zealand has a capital gains tax
- NEVER treat crypto profits as tax-free because the client calls it a long-term investment
- NEVER charge GST on buying or selling crypto
- NEVER ignore staking rewards: income when received
- NEVER allow a loss whose matching profit would be untaxed
- NEVER value crypto trading stock at market value at year end
- NEVER treat transfers between the client's own wallets as disposals
- NEVER ignore the transitional resident exemption
- NEVER present a purpose-test answer as final

## The method, step by step

1. Confirm residency and any transitional resident exemption. https://www.ird.govt.nz/cryptoassets/individual/tax-residence
2. List every acquisition and disposal across all wallets and platforms. Transfers between your own wallets are not disposals. https://www.ird.govt.nz/cryptoassets/individual/buying-selling
3. Test the dominant purpose at acquisition under s CB 4 of the Income Tax Act 2007; if it fails, test trading and a profit-making scheme under s CB 3. https://www.ird.govt.nz/cryptoassets/individual/buying-selling/acquiring-sell-exchange
4. Record income on receipt (staking, DeFi and mining rewards, crypto for services, airdrops in the taxable cases of QB 21/06). https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/questions-we-ve-been-asked/2021/qb-21-06.pdf
5. Work out each taxable disposal as sale price less cost less fees, by FIFO or weighted average cost, in NZD. https://www.ird.govt.nz/cryptoassets/taxing/income-expenses/calculating-cryptoasset-income
6. Check GST on NFT sales, mining services and crypto taken as payment. https://www.ird.govt.nz/cryptoassets/taxing/cryptoassets-and-gst
7. Enter net crypto income or loss in the IR3 "other income" box, attach the calculation, file by 7 July unless there is a tax agent or extension of time, and check provisional tax. https://www.ird.govt.nz/cryptoassets/taxing/declare-cryptoasset-income-or-loss

## Ask the client first

- Are you a New Zealand tax resident, and when did you arrive or return?
- For each holding: why did you buy it, what research did you do, and is anything written down from that time?
- Does it give you an income stream, and how does that compare with your sale gains?
- How often do you trade, and how much time do you spend on it?
- Did you receive airdrops, forks, mining rewards, NFTs or crypto for work?
- Which exchanges, wallets and protocols (including overseas), and do you have full exports?

## When to refuse or refer

- A firm "not taxable" answer for a claimed long-term investment.
- Crypto businesses, trading stock, companies and trusts.
- Salary, bonuses or share schemes paid in crypto.
- Complex DeFi, hard forks, stolen or lost crypto, scams.
- Non-residents with New Zealand-source income, treaty cases, transitional resident edge cases.
- Undeclared past income (voluntary disclosure), and clients with no usable records.

## Sources

- [Cryptoassets] https://www.ird.govt.nz/cryptoassets
- [Profit-making scheme] https://www.ird.govt.nz/cryptoassets/individual/buying-selling/profit-making-scheme
- [Trading] https://www.ird.govt.nz/cryptoassets/individual/buying-selling/trading
- [Mining] https://www.ird.govt.nz/cryptoassets/individual/mining
- [Airdrops and forks] https://www.ird.govt.nz/cryptoassets/individual/airdrops-and-hard-forks
- [New residents] https://www.ird.govt.nz/cryptoassets/individual/tax-residence/new-returning
- [Taxing] https://www.ird.govt.nz/cryptoassets/taxing
- [Records] https://www.ird.govt.nz/cryptoassets/taxing/record-keeping
- [NFTs] https://www.ird.govt.nz/cryptoassets/non-fungible-tokens
- [CARF] https://www.ird.govt.nz/international-tax/exchange-of-information/crypto-asset-reporting-framework/crypto-asset-reporting-framework-overview
- [IR3] https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3
- Linked in the method steps: [Buying and selling], [Acquiring to sell], [Tax residence], [Calculating income], [Crypto and GST], [Declare], QB 21/06
- Rate, GST, IR3 and provisional tax pages: linked in their tables
- Technical decision summary 25/23: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/tds/2025/tds-25-23.pdf?modified=20251006020051
- IRRUIP18: https://www.taxtechnical.ird.govt.nz/consultations/2026/irruip18
- Tax Information Bulletin Vol 34 No 5: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/tib/volume-34---2022/tib-vol-34-no5.pdf?modified=20220803034927&modified=20220803034927

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant (CA), tax advisor, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

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
