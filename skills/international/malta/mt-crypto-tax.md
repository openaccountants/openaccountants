---
name: mt-crypto-tax
description: Use this skill whenever asked about Malta cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Malta", "Bitcoin Malta", "DLT assets", "cryptocurrency gains", "crypto income Malta", "Binance Malta tax", "staking Malta", "mining income Malta", "NFT tax Malta", "Coinbase Malta", "Revolut crypto Malta", "token tax", "distributed ledger", "MFSA crypto", "DAC8", or any question about the income tax, capital gains, or VAT treatment of cryptocurrency, tokens, or digital assets for Malta tax residents or Malta-source crypto income. Covers the CfR DLT asset guidelines, classification of coins/tokens, trading vs investment distinction, VAT treatment, and DAC8 reporting. ALWAYS read this skill before touching any Malta crypto work.
version: 1.0
jurisdiction: MT
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - malta-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta tax on crypto-assets: income tax, capital gains, VAT and duty for individuals and companies

## Scope ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

This Guide covers how Malta taxes coins, tokens and other crypto-assets (the Commissioner calls them "DLT assets") held or dealt in by **individuals** and **companies**: income tax on trading profits and other crypto receipts, capital gains on tokens that count as securities, the remittance basis for non-domiciled residents, VAT, duty on documents, and the new crypto reporting by exchanges.

- **Primary year: basis year 2026 = year of assessment 2027.** An individual's return for 2026 income is due by 30 June 2027.
- **Returns being filed now:** 2025 income (year of assessment 2026). See "Filing and payment".

**How the law is built.** The Income Tax Act has no crypto-specific rule. Crypto is taxed through the general rules: trading income under article 4(1)(a), other income under article 4(1), and capital gains only on the assets listed in article 5. The Commissioner has published guidelines on the income tax, VAT and duty treatment of DLT assets. Under article 96(2), published guidelines "shall have the same effect as the rules" as long as they do not conflict with the Act.

**What we could not check.** The guidelines sit on mtca.gov.mt, which refused our automated source checks on 25 September 2026. So this Guide sources every figure from the Laws of Malta (legislation.mt). Anything that rests only on the guidelines (the exact coin/utility/financial token definitions, the guideline dates, and the VAT and duty positions on specific crypto transactions) is marked **"check on mtca.gov.mt"**. Do not quote guideline wording from memory.

**Companion Guides.** For rate tables in full, residence rules, provisional tax, interest and penalties, use the Malta income tax Guide (malta-income-tax). For registration, returns and input tax, use the Malta VAT return Guide (malta-vat-return).

**Not covered:** licensing under the Virtual Financial Assets Act or MiCA; issuing tokens (ICOs, IEOs, STOs); funds; the special residence programmes; double tax relief; and full company refund computations. These are referred (see "When to refuse or refer").

## Ask the client first

- **Who holds the crypto?** An individual, a company, a partnership, a trust or a fund? Companies and individuals follow different rate and filing rules.
- **Residence and domicile** (individuals): resident in Malta in the year? Domiciled in Malta? Ordinarily resident? A long-term resident or permanent-residence holder? Is your spouse ordinarily resident and domiciled in Malta?
- **Which years?** Dates of every buy, sell, swap, spend, reward and transfer. 2026 income uses the Act III of 2026 tables; 2025 income uses the Act IX of 2025 tables.
- **Why did you buy?** To hold long term, or to resell at a profit? How often do you trade, how long do you hold, do you use leverage, bots or borrowed money, and do you have another job?
- **What exactly is each asset?** A coin (such as BTC or ETH), a utility token, a token giving a share of profits or a fixed return, a stablecoin, an NFT, or units in a fund? Get the white paper for anything unusual.
- **Other receipts:** mining, staking, lending interest, liquidity-pool rewards, airdrops, forks, or crypto received as pay or as payment for goods and services.
- **Records:** CSV exports from every exchange and wallet, with euro values and fees.
- **Where did the money go?** For a non-dom: which foreign income was brought into Malta, when, and how much?
- **Business side:** do you sell goods or services for crypto, run a node or mining operation for customers, or sell NFTs you created? Are you registered for VAT?
- **Share-type tokens:** did you transfer any token that is a holding of share capital in a company?

## The method, step by step

1. **Fix the taxpayer and the year.** For an individual, the basis year is the calendar year; add one for the year of assessment. A company uses its accounting period.
2. **Build the ledger.** Every acquisition and disposal, in euro at the date of the transaction, with fees. Take out transfers between the client's own wallets and exchanges; they are not disposals.
3. **Classify each asset.** Is it "securities" as defined in article 5 of the Act (shares and similar instruments that share in profits with a return not limited to a fixed rate, or units in a collective investment scheme)? If yes, its disposal can be a capital gain under article 5. Coins and utility tokens are not in the article 5 list. The Commissioner's coin/utility/financial/hybrid labels come from the guidelines: check on mtca.gov.mt.
4. **Decide trading or capital for each disposal.** If the client trades, or bought "for the purpose of profit-making by sale", the profit is income under article 4(1)(a). Otherwise a gain on a coin or utility token is a capital gain outside article 5, and the Act does not tax it.
5. **Tax other receipts.** Mining, staking, lending, rewards and crypto received for work are income when received, at euro market value, under article 4(1)(a) if it is a business, or otherwise the head the Commissioner applies (check).
6. **Apply residence rules.** A non-dom or not-ordinarily-resident individual is taxed on foreign income only when received in Malta, and never on foreign capital gains. Then test the €5,000 minimum tax ([ITA art. 4(1) and 56(27)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c)).
7. **Compute the tax.** Individuals: add crypto income to other chargeable income and apply the rate table. Companies: 35% of chargeable income ([ITA art. 56(6)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c)).
8. **Check VAT and duty.** Is any supply taxable (goods or services paid in crypto, NFTs, services to identified customers)? Was any share-type token transferred?
9. **File and pay.** Individuals by 30 June of the year of assessment. Companies by the later of nine months after the accounting period ends and 31 March of the year of assessment.
10. **Keep records for nine years** after the transactions.

## Figures and years ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430))

**Individual resident, single table, basis year 2026 (year of assessment 2027).** Tax = chargeable income × rate − subtraction. Act III of 2026 replaced article 56(1)(a) and (b) "applicable from the year of assessment 2027".

| Chargeable income | Rate | Subtract |
| --- | --- | --- |
| Not over €12,000 | 0% | nil |
| Over €12,000 and under €16,000 | 15% | €1,800 |
| Over €16,000 and under €60,000 | 25% | €3,400 |
| Over €60,000 | 35% | €9,400 |

Married (joint), parent and the new qualifying-child tables have different bands and conditions. Use the Malta income tax Guide (malta-income-tax) for them. For 2025 income, the single table in [Act IX of 2025](https://legislation.mt/getpdf/6811d803cf7b7f36a4f360f5) has the same bands and subtractions.

### Other figures ([Laws of Malta](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

| Item | Figure | Year | Source |
| --- | --- | --- | --- |
| Company rate on chargeable income | 35% ("thirty-five cents (0.35) on every euro") | 2026 and 2025 | [ITA art. 56(6)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |
| Non-dom minimum tax | €5,000 a year, only if income arising outside Malta is not less than €35,000 and is not received, or not fully received, in Malta | 2026 and 2025 | [ITA art. 56(27)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |
| Interest on late income tax | 0.6% for every month or part of a month, capped at the tax | tax due on or after 31 August 2022 | [ITMA art. 44](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b) |
| VAT standard rate | 18% | 2026 | [VAT Act art. 19(1)](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20) |
| Duty on transfer of marketable securities | 2% (two euro per hundred), plus 3% more for property-rich companies | 2026 | [Duty on Documents and Transfers Act art. 42](https://legislation.mt/getpdf/68c1374a22d5d32e6c111563) |
| Property-rich test for the extra duty | 75% or more of the company's relevant assets are immovable property | 2026 | [Duty on Documents and Transfers Act art. 42(2)](https://legislation.mt/getpdf/68c1374a22d5d32e6c111563) |
| Record retention | not less than nine years after the transactions | all years | [ITMA art. 19(5)](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b) |

## Which crypto-assets fall under which rule ([Income Tax Act art. 4 and 5](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

**The statute.** Article 5 taxes capital gains only on the listed assets: immovable property; "securities, business, goodwill, business permits, copyright, patents, trademarks and trade-names and any other intellectual property"; a beneficial interest in a trust; and an interest in a partnership. "Securities" means:

> "shares and stocks and such like instrument that participate in any way in the profits of the company and whose return is not limited to a fixed rate of return, units in a collective investment scheme as defined in article 2 of the Investment Services Act, and units and such like instruments relating to linked long term business of insurance."

A crypto-asset that is not in that list is outside article 5. Its disposal is taxed only if the profit is income, mainly trading income under article 4(1)(a).

**The Commissioner's labels** (from the DLT guidelines; the definitions and wording are to check on mtca.gov.mt):

| Label | Typical example | Article 5 capital gains? | Trading profit taxable? |
| --- | --- | --- | --- |
| Coin | BTC, ETH, LTC used as money or a store of value | No: not "securities" | Yes, under art. 4(1)(a) |
| Utility token | Gives access to a product or service on a DLT platform | No: not "securities" | Yes, under art. 4(1)(a) |
| Financial token | Shares in profits like a share, or pays a return like a bond or fund unit | Yes, if it meets the "securities" definition | Yes, under art. 4(1)(a) if dealt in |
| Hybrid token | Starts as utility, later gains profit rights | Treat by its features at the time of transfer; check | Yes, under art. 4(1)(a) |

A token that pays only a fixed return does not meet the "securities" wording ("not limited to a fixed rate of return"). Its non-trading gain is then outside article 5. Check the guideline treatment before relying on this.

**Listed shares.** Article 5(6)(b) takes out of the capital gains rule any "transfer of shares listed, or in consequence of a listing, on a stock exchange recognised by the Commissioner for the purpose of this provision not being securities in a collective investment scheme". Whether a crypto trading venue is a recognised stock exchange: check.

**Capital losses** on article 5 assets "shall not be set off against other income for the year of assessment but shall be carried forward and set off against capital gains in respect of subsequent years of assessment" (article 5(10)(b)). A loss on a coin held as an investment is outside article 5 and gives no relief.

## Trading or capital: the test that decides most cases ([Income Tax Act art. 4(1)(a)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

Article 4(1)(a) taxes "gains or profits from any trade, business, profession or vocation ... including the profit arising from the sale by any person of any property acquired by him for the purpose of profit-making by sale, or from the carrying on or carrying out of any profit-making undertaking or scheme".

So there are **two** ways crypto profit becomes income:

1. The client carries on a **trade** in crypto (frequent, organised, business-like dealing).
2. The client **bought an asset to resell it at a profit**, even once. There is no minimum number of trades.

There is no bright-line test in the Act. Weigh the facts:

| Factor | Points to trading or profit-making | Points to capital (investment) |
| --- | --- | --- |
| Frequency | Many trades a day, week or month | A few trades over years |
| Holding period | Days or weeks | Months or years |
| Intention at purchase | Profit from price moves and resale | Long-term holding |
| Methods | Leverage, derivatives, bots, arbitrage | Buy and hold, no leverage |
| Funding | Borrowed money | Own savings |
| Organisation | Systematic, business-like, dedicated time | Incidental to other work |
| Other income | None, or crypto is the main activity | Separate full-time job or business |

**Working default.** When the facts are unclear, treat the profit as taxable income and tell the client why. This is a prudent default, not a rule of law; a well-documented investment position can be defended.

**What the Act does not do.** A genuine capital gain on a coin or utility token held as an investment is not in article 5, so it is not taxed. The guidelines take the same line on coins held as investments (check on mtca.gov.mt).

## Other crypto receipts ([Income Tax Act art. 4(1)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

The Act has no specific rules for these. The treatments below follow the general heads of article 4(1). Where the head depends on the guidelines or is unsettled, it says "check".

| Receipt | Working treatment | Status |
| --- | --- | --- |
| Crypto received as salary or fees | Income at euro market value when received: employment under art. 4(1)(b), or business under art. 4(1)(a) | Statute |
| Selling goods or services for crypto | Business income at the euro value of the crypto received; later disposal of the crypto is a separate event | Statute |
| Mining as a business (organised, for profit) | Business income under art. 4(1)(a), at market value when received; costs deductible if wholly and exclusively incurred | Statute; valuation check |
| Hobby-scale mining | Income at market value when received is the prudent view | Check |
| Staking and validator rewards | Income at market value when received; art. 4(1)(a) if a business, otherwise the head the Commissioner applies | Check |
| Lending interest (DeFi or platform) | Income when received; whether it is "interest" under art. 4(1)(c) or other income | Check |
| Airdrops | Taxable if received for doing something (a service or task); a purely gratuitous airdrop may not be income | Check |
| Hard fork coins | Cost of the original coin unchanged; new coin has nil cost; disposal classified like any other | Check |
| Liquidity pools | Adding to a pool may be a disposal; LP tokens get a new cost; impermanent loss is not a recognised deduction | Check; evolving |
| NFTs bought and sold | Disposal of an asset; taxable if trading or bought to resell | Statute |
| NFTs created and sold by the artist | Business income | Statute |

Whatever is taxed on receipt becomes the cost of that crypto for any later disposal.

## Cost, ledger and records ([Income Tax Management Act art. 19](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b))

- **Cost** is the euro price at the acquisition date, plus exchange fees and commissions, plus network (gas) fees directly attributable to the acquisition. Disposal fees reduce the proceeds.
- **Matching method.** First in, first out is the common working method. Specific identification is acceptable if clearly documented. The Act prescribes no method; whether the Commissioner accepts others: check. Use one method consistently.
- **Not disposals:** transfers between the client's own wallets or exchanges. Wrapping (ETH to WETH) is generally treated as no change of ownership; check.
- **Disposals:** crypto-to-fiat, crypto-to-crypto swaps (including into a stablecoin, even if the gain is small), and spending crypto on goods or services.
- **Unknown cost: stop.** Do not compute a gain without the acquisition cost.
- **Records.** A person carrying on a trade or business must keep "proper and sufficient records of his income and expenditure" ([ITMA art. 19(1)](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b)). They must be kept "for a period of not less than nine years after the completion of the transactions" (art. 19(5)). Keep exchange CSV exports, wallet addresses, on-chain links, the matching ledger, and staking or mining logs. The burden of proving cost and classification is on the client in practice.

## Residence, domicile and the remittance basis ([Income Tax Act art. 4(1) and 56(27)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

| Client | Crypto income | Crypto capital gains (art. 5 assets only) |
| --- | --- | --- |
| Resident, ordinarily resident and domiciled in Malta | Worldwide, whether received in Malta or not | Worldwide |
| Resident but not domiciled, or not ordinarily resident | Malta-source income in full; foreign income only "on the amount received in Malta" (proviso (i)) | Malta gains only; "no tax shall be payable on capital gains arising outside Malta" (proviso (ii)) |
| Not resident | Malta-source only | Malta-source only |

- **Where income arises.** The remittance basis applies only to income "arising outside Malta". For trading profits, where the income arises depends on where the trading is carried on, not on where the exchange is based. A non-dom living in Malta and trading from a laptop in Malta should not assume the profit is foreign. Refer if material.
- **Exceptions.** Provisos (i) and (ii) do not apply to a long-term resident or to a holder of a permanent residence certificate or card (for income from the year the status is granted and later years), or to an individual "whose spouse is ordinarily resident and domiciled in Malta". These people are taxed on worldwide income.
- **Received in Malta.** Moving proceeds to a Maltese bank account is a remittance. Keep evidence of what was brought in and from which source.
- **Minimum tax (article 56(27)).** It applies only if the individual meets all of these in the basis year:
  - ordinarily resident but not domiciled in Malta, and taxed under provisos (i) and (ii);
  - not under another scheme that sets a minimum tax;
  - has income arising outside Malta, "not less than thirty five thousand euro (€35,000)", that is not received or not fully received in Malta. For a married couple taxed jointly under article 49, count both spouses' foreign income.

  The tax is then not less than €5,000 for the year. Tax paid under the Act counts towards it, except tax on article 5A property transfers. If the client proves that tax on worldwide income would be lower, the lower amount applies. If foreign income is below €35,000, or all of it is received in Malta, there is no minimum tax. The €35,000 test is on total foreign income, not only the part kept abroad: bringing part of it into Malta does not take the client out.

## Companies holding or trading crypto ([Income Tax Act art. 56(6)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Rate.** A company pays tax "at the rate of thirty-five cents (0.35) on every euro" of chargeable income: 35%.
- **Same classification.** A company's crypto profit is trading income if it trades or bought to resell. A gain on a coin or utility token held as a genuine investment is outside article 5, as for individuals. A gain on a token that meets the "securities" definition is an article 5 gain. Companies set up to deal in crypto will usually be trading. Check the guideline treatment for company investment holdings.
- **Accounting period.** Accounts are made up to 31 December ("the day immediately preceding the next following year of assessment", article 11(1)) unless the Commissioner permits another date (article 11(2)).
- **Return date.** "The last day of the ninth month following that to which the accounts for the relative financial period are made or the thirty-first of March of the relative year of assessment, whichever is the later" ([S.L. 372.16 rule 2(c)(i)](https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2)). Tax is due on the same date (rule 5(b)).
- **Shareholder refunds** on distributed profits, provisional tax and the rest of the company computation are outside this Guide. Refer them.
- **Regulation.** A company offering crypto services may need a licence (MiCA and the [Virtual Financial Assets Act, Cap. 590](https://legislation.mt/getpdf/6a6c60bcab8952298c312cae)). A licence does not change the tax classification. Do not advise on licensing.

## VAT on crypto transactions ([VAT Act, Cap. 406](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

The VAT Act has no crypto-specific rule. The Maltese exemption for money is Fifth Schedule, Part Two (exempt without credit), item 3(4): "Transactions, including negotiation, concerning currency, bank notes and coins normally used as legal tender". The view that exchanging crypto for money is exempt comes from the EU Court of Justice's Hedqvist ruling (C-264/14) on the matching Directive rule and from the MTCA VAT guideline. Neither could be captured from an allowed source: check on mtca.gov.mt.

| Transaction | Working VAT treatment | Status |
| --- | --- | --- |
| Buying or selling crypto for euro, or swapping coins, as an investor | No economic activity, so no VAT | Check |
| Exchange service for a fee or spread (crypto to fiat and back) | Exempt without credit under the currency exemption, as read in Hedqvist | Check |
| Selling goods or services and accepting crypto as payment | VAT on the goods or services at the normal rate (18% standard) on the value received; the crypto itself is not taxed | Statute for the rate; check for valuation |
| Mining with no identifiable customer (block rewards) | No supply for consideration, so outside VAT | Check |
| Mining, hosting or node services for identified customers for a fee | A supply of services; taxable at 18% unless an exemption applies | Check |
| Staking-as-a-service fees charged to others | Possibly an exempt financial service; case by case | Check |
| NFT sales | Commonly treated as electronically supplied services; for consumers, the place of supply is where the customer lives, so another EU country's VAT may apply (OSS) | Check |

- **Input tax.** Exempt-without-credit supplies give no right to recover input tax. There is one exception in article 22(4)(d)(v): transactions "concerning currency, bank notes and coins normally used as legal tender" carry a credit "when the customer is established outside the Community". Partial exemption applies to mixed businesses.
- **Registration, returns, OSS:** use the Malta VAT return Guide (malta-vat-return).

## Duty on documents and transfers ([Duty on Documents and Transfers Act, Cap. 364](https://legislation.mt/getpdf/68c1374a22d5d32e6c111563))

- **What is taxed.** Duty is charged on transfers of immovable property and of "marketable securities". A "marketable security" "shall mean a holding of share capital in any company and any document representing the same" (article 2).
- **Coins and utility tokens** are not share capital, so the Act has no charge on transferring them. Check the MTCA duty guideline.
- **Tokens that are shares.** A token that is a holding of share capital in a company is a marketable security. When it is transferred "to or by any person in Malta", article 42(1)(b) charges "two euro for every one hundred euro or part thereof" (2%) of the higher of the consideration and the real value. It rises by three euro per hundred when 75% or more of the company's assets, excluding current assets other than immovable property, are immovable property (article 42(2)).
- **Foreign marketable securities** and **exemptions** (group restructurings, some listed securities, companies determined under article 47 to have more than 90% of business interests outside Malta) have their own rules. Refer.

## Reporting by crypto exchanges (DAC8) ([S.L. 123.127](https://legislation.mt/getpdf/6a3101a4d3e9ed28acd19036))

- Malta transposed the EU crypto reporting rules (Directive 2023/2226, "DAC8") into the Cooperation with Other Jurisdictions on Tax Matters Regulations by Legal Notice 162 of 2026.
- A "Reporting Malta Crypto-Asset Service Provider" must apply the due diligence and reporting rules in Annex VI. That includes getting each user's self-certification of tax residence.
- Malta passes the data to other EU tax authorities "within nine (9) months following the end of the calendar year". The first data covers the period "as from 1 January 2026". Exchanges in other EU countries report Malta residents to MTCA the same way.
- **What this means for the client:** transactions from 2026 onward will be visible to MTCA. Reconcile the return to exchange data before filing. The date by which providers file with MTCA: check on mtca.gov.mt.

## Boundary and exception table ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

| Situation | Treatment | Why |
| --- | --- | --- |
| One purchase of a coin, bought to sell at a profit, sold months later | Taxable income under art. 4(1)(a) | "property acquired by him for the purpose of profit-making by sale"; no minimum number of trades |
| Coin bought to hold, sold years later, no trading pattern | Not taxed | Not in the art. 5 list; capital, not income |
| Loss on a coin held as an investment | No relief | Outside art. 5; art. 5(10) losses cover only art. 5 assets |
| Trading loss | Business loss rules apply (see malta-income-tax) | Art. 4(1)(a) and 14 |
| Token that shares in profits with no fixed cap on return | Art. 5 "securities": capital gain even if held as investment | Art. 5(1) definition |
| Token paying only a fixed return | Not "securities" (return "limited to a fixed rate"); non-trading gain not taxed; income it pays is taxed | Art. 5(1) definition; check guideline |
| Listed shares (not fund units) on a recognised exchange | Outside the capital gains rule | Art. 5(6)(b) |
| Non-dom, foreign crypto income kept abroad | Not taxed unless received in Malta; minimum tax test at €35,000 | Art. 4(1) proviso (i); art. 56(27) |
| Non-dom whose spouse is ordinarily resident and domiciled in Malta | Taxed on worldwide income | Art. 4(1) provisos do not apply |
| Non-dom, foreign capital gain on a financial token | Not taxed, even if remitted | Art. 4(1) proviso (ii) |
| Transfer between own wallets | Not a disposal | No change of owner |
| Crypto-to-crypto swap | Disposal of the first asset at market value | General principles; check guideline |
| Stablecoin swap | Disposal; gain usually small | General principles |
| Transfer of a coin or utility token | No duty | Not a "marketable security" |
| Transfer of a token that is a holding of share capital, to or by a person in Malta | Duty at 2%, or 5% for a property-rich company | Duty Act art. 42 |

## Worked cases ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430))

All cases are hypothetical. Individuals are resident, ordinarily resident and domiciled in Malta, single and on the single table, unless stated.

**Case 1: frequent trader (basis year 2026).** Bought one BTC for €25,000 in January 2026 and sold it for €45,000 in March 2026, with fees of €100 in total. Over 50 trades in the year. No other income.
- Trading, so income under art. 4(1)(a). Profit = €45,000 − €25,000 − €100 = €19,900.
- Band: over €16,000 and under €60,000. Tax = €19,900 × 25% − €3,400 = €4,975 − €3,400 = €1,575.
- The same facts in 2025 give the same tax: the Act IX of 2025 single table has the same bands and subtractions.

**Case 2: long-term holder (basis year 2026).** Bought 2 ETH at €1,500 each in 2021 and sold both at €3,500 each in 2026. Three trades in five years. Full-time job elsewhere; says the ETH was bought as a long-term holding.
- Gain = (€3,500 − €1,500) × 2 = €4,000.
- Coins are not art. 5 assets. If the facts support a capital holding, the gain is not taxed.
- If the client actually bought to resell at a profit, the gain is income and goes into the return. Record the evidence for the capital view (purchase notes, holding pattern, no leverage).

**Case 3: staking rewards on top of a salary (basis year 2026).** Chargeable employment income €30,000. Staking rewards worth €1,750 at the dates received.
- Treating the rewards as income when received (check the head): total €31,750.
- Tax with staking = €31,750 × 25% − €3,400 = €7,937.50 − €3,400 = €4,537.50. Without staking = €30,000 × 25% − €3,400 = €4,100. Extra tax €437.50.
- The staked coins received have a cost of €1,750 for any later disposal.

**Case 4: non-dom and the minimum tax (basis year 2026).** Ordinarily resident, not domiciled, not a long-term resident, spouse not domiciled in Malta. Income arising outside Malta of €50,000 (including lending income from a platform abroad; confirm the source), none brought into Malta. Tax on Malta income €1,200.
- Foreign income is not taxed because none was received in Malta.
- €50,000 is not less than €35,000, so the minimum tax applies: €5,000 − €1,200 = €3,800 extra, unless tax on worldwide income would be lower.
- Variant: foreign income of €30,000 (none remitted) is below €35,000, so there is no minimum tax.
- Any capital gain on coins held as an investment is untaxed anyway (not an art. 5 asset).

**Case 5: trading company (accounting period to 31 December 2026).** A Malta company deals in crypto. Chargeable income €100,000.
- Tax = €100,000 × 35% = €35,000.
- Return and tax due: the later of the last day of the ninth month after December 2026 (30 September 2027) and 31 March 2027, so 30 September 2027.
- Shareholder refunds: refer.

**Case 6: shop accepting BTC (VAT, 2026).** A VAT-registered shop sells goods priced at €1,180 including VAT and is paid in BTC worth €1,180.
- VAT is due on the goods at 18%: €1,180 × 18 / 118 = €180. The BTC received is not itself a taxable supply (check the guideline).
- If the shop later sells the BTC, that is a separate income tax event.

**Case 7: token that is a share (duty, 2026).** A token representing shares in a Malta company, not property-rich, is transferred between two persons in Malta for €10,000.
- Duty = €10,000 × 2% = €200. If 75% or more of the company's relevant assets were immovable property: €10,000 × 5% = €500.
- A transfer of BTC for €10,000 carries no duty.

## Reading exchange and bank statements ([Income Tax Act art. 4(1)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

| Line on a statement | Likely meaning | What to do |
| --- | --- | --- |
| Exchange sell, "crypto sell", payout to bank (Binance, Coinbase, Kraken, Revolut) | Disposal proceeds | Match to the acquisition cost; convert to euro at the date |
| Exchange buy, "crypto buy", card purchase of crypto | Acquisition | Record cost with fees |
| Gas, network or transaction fee | Cost of the related acquisition or disposal | Add to cost or deduct from proceeds |
| Trading fee, commission | Cost of acquisition or disposal | Same |
| Mining reward, pool payout | Receipt | Income at market value when received (see "Other crypto receipts") |
| Staking reward, validator reward, "earn" interest | Receipt | Income at market value when received; head to check |
| Airdrop, token distribution | Possible income | Taxable if received for a task or service |
| Transfer, withdrawal or deposit between the client's own accounts | Not a disposal | Exclude; keep the on-chain proof |
| P2P transfer | Sale, purchase or own transfer | Ask the client which |
| Hardware wallet purchase | Equipment | Deductible (by capital allowances) only for a trading business; not for an investor |

## When to refuse or refer

**Stop and ask** when:
- residence, domicile or ordinary residence is unknown. The remittance basis turns on them;
- there are no transaction records, or acquisition cost is unknown. A gain cannot be computed.

**Refer to a Maltese warranted accountant or tax adviser** when:
- tokens are being issued (ICO, IEO, STO): issuer income tax, VAT and licensing all arise;
- the question is whether a token is a financial token, a hybrid, or "securities", and material money depends on it;
- the client is a non-dom whose trading may arise in Malta, or whose foreign income is near €35,000 ([ITA art. 56(27)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c));
- the client is a company and shareholder refunds, group relief or participation rules matter;
- DeFi structures, DAOs, liquidity-pool governance or cross-border arrangements are involved;
- the client wants a ruling on the Commissioner's guideline position, or the amount at stake justifies one;
- the client needs licensing advice under MiCA or the Virtual Financial Assets Act (not a tax question).

**Never:**
- say all crypto gains are tax-free in Malta. Trading profit, and profit on anything bought to resell, is taxable;
- call a coin "securities" for article 5;
- apply the remittance basis without checking the exceptions (long-term resident, permanent residence, Maltese-domiciled spouse);
- say the non-dom minimum tax applies regardless of income. It needs foreign income of at least €35,000 that is not fully brought into Malta ([ITA art. 56(27)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c));
- treat transfers between the client's own wallets as disposals;
- quote the MTCA guidelines from memory. Point to them and mark the point "check";
- present an answer as final without a professional review.

## Filing and payment ([Income Tax (Statutory Dates) Rules, S.L. 372.16](https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2))

| What | When | Source |
| --- | --- | --- |
| Individual return and self-assessment, 2026 income | 30 June 2027 (rule 2(c)(ii)); tax due the same day (rule 5(b)) | S.L. 372.16 |
| Company return, accounting period ending 31 December 2026 | Later of 30 September 2027 and 31 March 2027: 30 September 2027 (rule 2(c)(i)) | S.L. 372.16 |
| Provisional tax during 2026 and 2027 | Instalment dates and percentages: see malta-income-tax | P.T. Rules |
| Late tax | Interest at 0.6% a month or part of a month, capped at the tax | [ITMA art. 44](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b) |
| Late return | Additional tax: see malta-income-tax | ITMA |
| VAT returns | See malta-vat-return | VAT Act |
| Duty on a share-type token transfer | Payable on the transfer document; timing and form: check on mtca.gov.mt | Duty Act |

- **Where crypto goes on the return.** Trading profit goes in with business income; other crypto income goes in as other income. The form layout and the online filing portal: check on mtca.gov.mt.
- **Online filing extensions:** check the MTCA notice for the year; do not assume one.

### Returns being filed now: 2025 income (year of assessment 2026) ([Act IX of 2025](https://legislation.mt/getpdf/6811d803cf7b7f36a4f360f5))

- The statutory return date was 30 June 2026. A 2025 return not filed yet is late: interest and additional tax run (see malta-income-tax). Check whether MTCA announced an online extension.
- Rate tables: Act IX of 2025. The single table has the same bands and subtractions as 2026. The qualifying-child tables do not apply to 2025 income.
- DAC8 data starts with 2026, so it does not cover 2025. That changes nothing about what must be reported.
- The classification rules above are unchanged for 2025.

## Completion checklist ([Laws of Malta](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- Taxpayer type, residence, domicile and ordinary residence confirmed, including the spouse's position.
- Full ledger in euro, own-wallet transfers removed, cost known for every disposal, one matching method used throughout.
- Each asset classified: coin, utility, share-type or fixed-return token, and whether it meets the article 5 "securities" definition.
- Each disposal classified trading or capital, with the reasons written down, including whether it was bought to resell.
- Mining, staking, lending, airdrops and crypto pay valued at receipt and taxed.
- Remittance basis applied only to income arising outside Malta and only where no exception applies; minimum tax tested against €35,000.
- Tax computed on the right table for the right year (Act III of 2026 for 2026; Act IX of 2025 for 2025), or at 35% for a company.
- VAT checked on any business supplies paid in crypto, NFT sales and services to identified customers.
- Duty checked on any token that is a holding of share capital.
- Return reconciled to exchange data; records kept for nine years.
- Every point that rests on the MTCA guidelines marked "check" and confirmed on mtca.gov.mt before filing.

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
