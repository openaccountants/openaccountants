---
name: mt-crypto-tax
description: Use this skill whenever asked about Malta cryptocurrency or digital asset taxation for basis year 2026. Trigger on phrases like crypto tax Malta, Bitcoin Malta, DLT assets, cryptocurrency gains, crypto income Malta, Binance Malta tax, staking Malta, mining income Malta, NFT tax Malta, Coinbase Malta, Revolut crypto Malta, token tax, distributed ledger, MFSA crypto, DAC8, or any question about the income tax, capital gains, VAT or duty treatment of cryptocurrency, tokens or digital assets for Malta tax residents or Malta-source crypto income. Covers the Commissioner's DLT asset guidelines (coins, financial, utility and hybrid tokens), trading versus investment, receipts such as mining and staking, the remittance basis and the EUR 5,000 minimum tax, companies at 35%, VAT, duty on share-type tokens and DAC8 reporting from 1 January 2026. Read it before any Malta crypto work.
version: "2.0"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - malta-income-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: situation-rules
---

# Malta tax on crypto-assets: income tax, capital gains, VAT and duty, basis year 2026

## Scope

This skill covers how Malta taxes coins, tokens and other crypto-assets (the Commissioner calls them "DLT assets") held or dealt in by **individuals** and **companies**: income tax on trading profits and other crypto receipts, capital gains on tokens that count as securities, the remittance basis for non-domiciled residents, VAT, duty on documents, and crypto reporting by exchanges.

- **Primary year: basis year 2026 = year of assessment 2027.** An individual's return for 2026 income is due by 30 June 2027.
- **Returns being filed now:** 2025 income (year of assessment 2026). The classification rules are the same for 2025.

**How the law is built.** The Income Tax Act, Cap. 123, has no crypto-specific rule. Crypto is taxed through the general rules: trading income under art. 4(1)(a), other income under art. 4(1), and capital gains only on the assets listed in art. 5. The Commissioner's *Guidelines on the Income Tax Treatment of transactions or arrangements involving DLT assets* (issued 1 November 2018 under art. 96(2)) set out the classification and valuation approach. The guidelines say: "Ultimately, the tax treatment of any type of DLT asset will not necessarily be determined by its categorisation, but will depend on the purpose for and context in which it is used."

**Companion skills.** Rate tables, residence rules, provisional tax and penalties: [malta-income-tax](malta-income-tax.md). VAT registration and returns: [malta-vat-return](malta-vat-return.md). Article 5 gains in general: [mt-capital-gains](mt-capital-gains.md). Non-doms: [mt-non-dom](mt-non-dom.md).

**Not covered:** licensing of crypto-asset services under MiCA and the Markets in Crypto-Assets Act, Cap. 647; issuing tokens (ICOs, IEOs, STOs); funds; the special residence programmes; double tax relief; full company refund computations. These are referred.

Built from the law: not yet approved by an accountant.

## Ask the client first

1. **Who holds the crypto, and their residence, domicile and ordinary residence?** Individual, company, partnership, trust or fund. For an individual: long-term resident or permanent-residence holder? Spouse ordinarily resident and domiciled in Malta?
2. **Why did you buy, and how do you deal?** To hold long term or to resell at a profit? Frequency, holding period, leverage, bots, borrowed money, another job?
3. **What exactly is each asset?** A coin (BTC, ETH), a utility token, a token sharing in profits or paying a return, a stablecoin, an NFT, fund units? The white paper for anything unusual.
4. **Other receipts:** mining, staking, lending interest, liquidity-pool rewards, airdrops, forks, crypto received as pay or for goods and services.
5. **Records:** CSV exports from every exchange and wallet, with euro values and fees. For a non-dom: which foreign income was brought into Malta, when, and how much.
6. **Business side:** goods or services sold for crypto, node or mining services for customers, NFTs created and sold, VAT registration; any token that is a holding of share capital.

## The method, step by step

1. **Fix the taxpayer and the year.** An individual's basis year is the calendar year; a company uses its accounting period.
2. **Build the ledger.** Every acquisition and disposal, in euro at the date, with fees. Remove transfers between the client's own wallets and exchanges.
3. **Classify each asset.** Is it "securities" under art. 5? If yes, its disposal can be an art. 5 capital gain. Coins and utility tokens are not in the art. 5 list.
4. **Trading or capital for each disposal.** A trade, or an asset bought "for the purpose of profit-making by sale", gives income under art. 4(1)(a). Otherwise a gain on a coin or utility token is capital outside art. 5 and is not taxed.
5. **Other receipts.** Find the income head and the recognition event before valuing any mining, staking, lending, reward or work payment. Crypto does not create a cash basis: the guidelines say that for businesses accepting crypto "there is no change to when revenue is recognised or the manner in which taxable profits are calculated". Unsettled receipt classes stay on hold.
6. **Residence rules.** A person not domiciled or not ordinarily resident is taxed on foreign income only when received in Malta, and never on foreign capital gains; then test the minimum tax (art. 4(1) provisos, art. 56(27)).
7. **Compute.** Individuals: add crypto income to chargeable income at the normal rates. Companies: 35% (art. 56(6)).
8. **VAT and duty.** Any taxable supply paid in crypto, NFTs, services to identified customers; any share-type token transferred.
9. **File and pay**, and keep records for nine years.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Individual crypto income | Added to chargeable income at the 2026 rates; single 25% band less EUR 3,400 from EUR 16,001 to EUR 60,000 | Rate tables owned by malta-income-tax | MTCA Tax Rates 2026: https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 |
| Company rate on chargeable income | 35% ("thirty-five cents ... on every euro") | Shareholder refunds outside this skill | Cap. 123 art. 56(6): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Non-dom minimum tax | EUR 5,000 a year | Income arising outside Malta not less than EUR 35,000 and not received, or not fully received, in Malta; art. 5A tax does not count; a lower worldwide tax applies if proved | Cap. 123 art. 56(27): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Interest on late income tax | 0.6% for every month or part, capped at the tax | Tax payable on or after 31 August 2022 | Cap. 372 art. 44(2A): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Record retention | Not less than nine years after the transactions | Anyone carrying on a trade or business | Cap. 372 art. 19(5): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| VAT standard rate | 18% | Goods or services sold for crypto | Cap. 406 art. 19(1): https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 |
| Duty on a share-type token | 2% of the higher of consideration and real value; plus 3% where 75% or more of the company's assets, excluding current assets other than immovable property, are immovable property | A holding of share capital transferred to or by a person in Malta | Cap. 364 art. 42(1), (2): https://legislation.mt/eli/cap/364/eng/pdf |
| DAC8 exchange of crypto data | Within nine months after the end of the calendar year | Data for periods from 1 January 2026 | S.L. 123.127: https://legislation.mt/getpdf/6a3101a4d3e9ed28acd19036 |
| Individual return and payment | 30 June 2027 for 2026 income | Online return by 31 July (MTCA) | S.L. 372.16 rule 2(c)(ii): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |
| Company return and payment | Later of the last day of the ninth month after the accounting period and 31 March of the year of assessment | 30 September 2027 for a 31 December 2026 year end | S.L. 372.16 rule 2(c)(i): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |

### Which crypto-assets fall under which rule

Article 5 taxes capital gains only on: immovable property; "securities, business, goodwill, business permits, copyright, patents, trademarks and trade-names and any other intellectual property"; a beneficial interest in a trust; an interest in a partnership. "Securities" means "shares and stocks and such like instrument that participate in any way in the profits of the company and whose return is not limited to a fixed rate of return, units in a collective investment scheme ... and units and such like instruments relating to linked long term business of insurance." An asset outside the list is taxed only if the profit is income.

The Commissioner's categories (DLT income-tax guidelines, section A):

| Category | What the guidelines say | Article 5 capital gains? | Trading profit taxable? |
|---|---|---|---|
| Coin | No characteristics of a security, no link to a project or equity, "designed to be used as a means of payment or medium of exchange, or function as a store of value" | No: not securities | Yes, art. 4(1)(a) |
| Financial token | Qualities similar to equities, debentures, collective investment scheme units or derivatives (dividends, interest, fund payments, asset-linked payments, voting or ownership rights) | Yes, if it meets the securities definition | Yes, if dealt in |
| Utility token | Use restricted solely to acquiring goods or services within the platform or a limited network; no link to equity | No | Yes |
| Hybrid | "Where a hybrid token is used in a particular case as a utility token then it is to be treated as such, while if in another occasion the same token is used as a coin, then it needs to be treated as such" | By use | Yes |

A token whose return is limited to a fixed rate fails the share-like limb, but still test the collective-investment-scheme and linked-insurance limbs; hold the classification until all rights are checked. Listed shares on an exchange recognised by the Commissioner (not fund units) are outside the capital gains rule (art. 5(6)(b)); whether a crypto venue is a recognised stock exchange is not confirmed. Art. 5 losses "shall not be set off against other income ... but shall be carried forward and set off against capital gains" (art. 5(10)); a loss on a coin held as an investment gives no relief.

### Trading or capital: the test that decides most cases

Art. 4(1)(a) taxes "gains or profits from any trade, business, profession or vocation ... including the profit arising from the sale by any person of any property acquired by him for the purpose of profit-making by sale". Two routes to income: a **trade** in crypto, or a **single purchase made to resell at a profit** (no minimum number of trades). Weigh the facts:

| Factor | Points to trading or profit-making | Points to capital |
|---|---|---|
| Frequency | Many trades a day, week or month | A few trades over years |
| Holding period | Days or weeks | Months or years |
| Intention at purchase | Profit from price moves | Long-term holding |
| Methods | Leverage, derivatives, bots, arbitrage | Buy and hold |
| Funding | Borrowed money | Own savings |
| Organisation | Systematic, dedicated time | Incidental to other work |
| Other income | None, or crypto is the main activity | Separate full-time job or business |

**Working default:** when the facts are unclear, treat the profit as income and say why. This is a prudent default, not law; a documented investment position can be defended.

### Other crypto receipts

| Receipt | Working treatment | Status |
|---|---|---|
| Crypto received as salary or fees | Employment (art. 4(1)(b)) or business (art. 4(1)(a)); ordinary recognition, market value at the event | Statute; guidelines on remuneration |
| Goods or services sold for crypto | Business income at the euro value received; a later disposal of the crypto is a separate event | Statute; guidelines |
| Mining as a business | Income under art. 4(1)(a); ordinary recognition and allowable costs | Guidelines; statute |
| Hobby-scale mining | Hold: income status and recognition not confirmed | Not confirmed |
| Staking and validator rewards | Hold: classify the arrangement and the recognition event first | Not confirmed |
| Lending interest (DeFi or platform) | Hold: income head, source and recognition | Not confirmed |
| Airdrops | Taxable if received for a task or service; a purely gratuitous airdrop may not be income | Not confirmed |
| Hard fork coins | Hold; do not assign a nil cost automatically | Not confirmed |
| Liquidity pools | Hold; no categorical impermanent-loss conclusion | Not confirmed |
| NFTs bought and sold | Taxable if trading or bought to resell | Statute |
| NFTs created and sold by the artist | Business income | Statute |

**Value.** The guidelines: market value "may be determined by reference to the rate established by the relevant Maltese authority, and where such is not available by reference to the average quoted price on reputable exchanges, on the date of the relevant transaction or event".

### Cost, ledger and records

- **Cost** is the euro value at acquisition plus exchange fees, commissions and directly attributable network fees; disposal fees reduce proceeds.
- **Matching method:** no authority found for FIFO, specific identification or another method; keep transaction-level evidence and agree a supported method before finalising.
- **Not disposals:** transfers between the client's own wallets or exchanges. Wrapping (ETH to WETH): hold.
- **Disposals:** crypto to fiat, crypto to crypto (including into a stablecoin), spending crypto.
- **Unknown cost: stop.**
- **Records:** "proper and sufficient records" (ITMA art. 19(1)), kept "for a period of not less than nine years after the completion of the transactions" (art. 19(5)): exchange exports, wallet addresses, on-chain links, the matching ledger, mining and staking logs.

### Residence, domicile and the remittance basis

| Client | Crypto income | Crypto capital gains (art. 5 assets only) |
|---|---|---|
| Resident, ordinarily resident and domiciled | Worldwide | Worldwide |
| Resident but not domiciled, or not ordinarily resident | Malta-source in full; foreign income only "on the amount received in Malta" (proviso (i)) | Malta gains only; "no tax shall be payable on capital gains arising outside Malta" (proviso (ii)) |
| Not resident | Malta-source only | Malta-source only |

- Trading profit arises where the trading is carried on: a non-dom trading from a laptop in Malta should not assume the profit is foreign. Refer if material.
- Provisos (i) and (ii) do not apply to a long-term resident, a permanent residence certificate or card holder (from the year granted), or an individual "whose spouse is ordinarily resident and domiciled in Malta".
- Moving proceeds to a Maltese account is a remittance; keep evidence of source.
- **Minimum tax (art. 56(27)):** ordinarily resident but not domiciled, taxed under the provisos, not under another minimum-tax scheme, with foreign income "not less than thirty five thousand euro (€35,000)" not received or not fully received in Malta (both spouses' income counts under joint assessment). Tax is then not less than EUR 5,000. The EUR 35,000 test is on total foreign income, not only the part kept abroad.

### Companies

- 35% on chargeable income. Same classification as individuals; a company set up to deal in crypto will usually be trading.
- Accounts to 31 December unless the Commissioner permits another date (art. 11). Return and tax: the later of nine months after the period end and 31 March of the year of assessment.
- Regulation: crypto-asset services need MiCA authorisation (Regulation (EU) 2023/1114, Article 63), with the MFSA as competent authority under Cap. 647. Licences under the Virtual Financial Assets Act, Cap. 590, were "automatically ... cancelled on 2 July 2026 or upon the granting or refusal of an authorisation pursuant to Article 63 of the MiCA Regulation ... whichever comes first" (art. 66(2)). A licence does not change the tax classification.

### VAT on crypto transactions

The VAT Act has no crypto-specific rule. The money exemption is Fifth Schedule Part Two item 3(4): "Transactions, including negotiation, concerning currency, bank notes and coins normally used as legal tender". The view that exchanging crypto for money is exempt rests on the EU Court of Justice's Hedqvist ruling (C-264/14) and MTCA's VAT guideline, not re-read today.

| Transaction | Working VAT treatment | Status |
|---|---|---|
| Investor buying or selling crypto, or swapping | No economic activity, no VAT | Not confirmed |
| Exchange service for a fee or spread | Exempt without credit under the currency exemption, as read in Hedqvist | Not confirmed |
| Goods or services sold for crypto | VAT on the supply at the normal rate on the value received | Rate statute; valuation not confirmed |
| Mining with no identifiable customer | Outside VAT | Not confirmed |
| Mining, hosting or node services for a fee | Taxable at 18% unless exempt | Not confirmed |
| Staking-as-a-service fees | Possibly exempt financial service | Not confirmed |
| NFT sales | Commonly electronically supplied services; consumer place of supply where the customer lives (OSS) | Not confirmed |

Exempt-without-credit supplies give no input tax right, except currency transactions with a customer established outside the Community (art. 22(4)(d)(v)). Registration, returns and OSS: [malta-vat-return](malta-vat-return.md).

### Duty on documents and transfers

A "marketable security" "shall mean a holding of share capital in any company and any document representing the same" (Cap. 364 art. 2). Coins and utility tokens are not share capital, so no duty. A token that is a holding of share capital, transferred to or by a person in Malta, pays 2%, or 5% for a property company (art. 42). Foreign marketable securities and the exemptions (group restructurings, art. 47 determinations): refer.

### Reporting by crypto exchanges (DAC8)

Malta transposed Directive 2023/2226 (DAC8) into the Cooperation with Other Jurisdictions on Tax Matters Regulations, S.L. 123.127. A Reporting Malta Crypto-Asset Service Provider applies the due diligence and reporting rules, including users' self-certification of tax residence. Malta exchanges the data "within nine (9) months following the end of the calendar year", for periods "as from 1 January 2026". Transactions from 2026 will be visible to MTCA: reconcile the return to exchange data before filing.

## Boundary and exception table

| Situation | Treatment | Why |
|---|---|---|
| One coin bought to sell at a profit, sold months later | Income under art. 4(1)(a) | Bought "for the purpose of profit-making by sale" |
| Coin bought to hold, sold years later, no trading pattern | Not taxed | Not in the art. 5 list; capital |
| Loss on a coin held as an investment | No relief | Outside art. 5 |
| Trading loss | Business loss rules (see malta-income-tax) | Art. 4(1)(a), 14 |
| Token sharing in profits with no fixed cap | Art. 5 securities: capital gain even if held as investment | Art. 5(1) definition |
| Token paying a fixed return | Hold until the scheme and insurance limbs are checked | Art. 5(1) |
| Non-dom, foreign crypto income kept abroad | Not taxed unless received; minimum tax test at EUR 35,000 | Art. 4(1) proviso (i); 56(27) |
| Non-dom whose spouse is ordinarily resident and domiciled in Malta | Worldwide | Provisos do not apply |
| Non-dom, foreign gain on a financial token | Not taxed, even if remitted | Art. 4(1) proviso (ii) |
| Own-wallet transfer | Not a disposal | No change of owner |
| Crypto-to-crypto or stablecoin swap | Disposal at market value | General principles; guidelines on value |
| Transfer of a coin or utility token | No duty | Not a marketable security |
| Transfer of a share-type token in Malta | 2%, or 5% for a property company | Cap. 364 art. 42 |

### Reading exchange and bank statements

| Line | Likely meaning | Action |
|---|---|---|
| Exchange sell, payout to bank (Binance, Coinbase, Kraken, Revolut) | Disposal proceeds | Match to cost; euro at the date |
| Exchange buy, card purchase of crypto | Acquisition | Record cost with fees |
| Gas, network, trading fee, commission | Cost of the related acquisition or disposal | Add to cost or deduct from proceeds |
| Mining reward, pool payout, staking or "earn" reward | Receipt | Hold until classified |
| Airdrop | Possible income | Taxable if for a task or service |
| Transfer between own accounts | Not a disposal | Exclude; keep on-chain proof |
| P2P transfer | Sale, purchase or own transfer | Ask |
| Hardware wallet purchase | Equipment | Capital allowances only for a trading business |

## Worked cases

Individuals are resident, ordinarily resident and domiciled, on the 2026 single table, unless stated. All are invented.

### Case 1: frequent trader

Bought one BTC for EUR 25,000 in January 2026, sold for EUR 45,000 in March 2026, fees EUR 100; over 50 trades in the year; no other income. Trading income: EUR 19,900. Tax: EUR 19,900 x 25% less EUR 3,400 = EUR 1,575.

```oa-check
name: Resident single 2026, crypto trading profit EUR 19,900
inputs:
  proceeds: 45000
  cost: 25000
  fees: 100
steps:
  - profit: proceeds - cost - fees
  - tax: profit * 0.25 - 3400
expected:
  profit: 19900
  tax: 1575
```

### Case 2: long-term holder or trader (a decision)

Bought 2 ETH at EUR 1,500 each in 2021, sold both at EUR 3,500 each in 2026; three trades in five years; salary of EUR 30,000 chargeable income. Gain EUR 4,000. If the facts support a capital holding, coins are not art. 5 assets and the gain is not taxed: nil. If the ETH was bought to resell at a profit, the gain is income: extra tax EUR 1,000 at 25%. The intention at purchase, evidenced by the holding pattern and no leverage, decides EUR 1,000.

```oa-check
name: ETH gain EUR 4,000 on a EUR 30,000 salary, capital versus trading (2026)
inputs:
  salary: 30000
  units: 2
  buy: 1500
  sell: 3500
steps:
  - gain: (sell - buy) * units
  - tax_capital: 0
  - tax_trading: (salary + gain) * 0.25 - 3400 - (salary * 0.25 - 3400)
  - cost_of_trading_view: tax_trading - tax_capital
expected:
  gain: 4000
  tax_capital: 0
  tax_trading: 1000.00
  cost_of_trading_view: 1000.00
```

### Further cases (prose)

- **Staking on top of a salary.** Salary EUR 30,000; staking rewards EUR 1,750, only if properly classified and recognised as 2026 income: extra tax EUR 437.50 (EUR 4,537.50 against EUR 4,100). The coins received then have a cost of EUR 1,750.
- **Non-dom and the minimum tax.** Foreign income EUR 50,000, none brought in; tax on Malta income EUR 1,200: minimum tax adds EUR 3,800, unless worldwide tax would be lower. With foreign income of EUR 30,000, no minimum tax.
- **Trading company.** Chargeable income EUR 100,000 to 31 December 2026: EUR 35,000, due 30 September 2027.
- **Shop accepting BTC.** Goods at EUR 1,180 including VAT, paid in BTC: VAT EUR 180 (18/118). A later sale of the BTC is a separate income tax event.
- **Share-type token.** EUR 10,000 transfer in Malta: duty EUR 200, or EUR 500 for a property company. BTC for EUR 10,000: no duty.

## When to refuse or refer

**Stop and ask** when residence, domicile or ordinary residence is unknown, or there are no records or no acquisition cost.

**Refer** when: tokens are being issued; financial, hybrid or securities status decides material money; a non-dom's trading may arise in Malta, or foreign income is near EUR 35,000; company refunds, group relief or participation rules matter; DeFi, DAOs or cross-border structures are involved; a ruling is warranted; licensing advice under MiCA and Cap. 647 is wanted.

**Never:** say all crypto gains are tax-free in Malta; call a coin "securities"; apply the remittance basis without checking the exceptions; apply the minimum tax without the EUR 35,000 test; treat own-wallet transfers as disposals; quote a guideline from memory or stretch the income-tax guidelines to VAT or DeFi facts; present an answer as final without review.

## Filing and payment

| What | When | Source |
|---|---|---|
| Individual return and self-assessment, 2026 income | 30 June 2027, tax due the same day; online by 31 July 2027 | S.L. 372.16 rule 2(c)(ii); MTCA Tax Return Cycle |
| Company return, period to 31 December 2026 | 30 September 2027 | S.L. 372.16 rule 2(c)(i) |
| Provisional tax | Instalment dates: see [mt-estimated-tax](mt-estimated-tax.md) | ITMA |
| Late tax | 0.6% a month or part, capped at the tax | ITMA art. 44(2A) |
| VAT returns | See [malta-vat-return](malta-vat-return.md) | Cap. 406 |
| Duty on a share-type token | With the share transfer notification: see [selling-a-company-in-malta](selling-a-company-in-malta.md) | Cap. 364 |

Trading profit goes in the return with business income; other crypto income as other income. Online filing on [myTax](https://mytax.mtca.gov.mt/) with e-ID.

## Completion checklist

- [ ] Taxpayer type, residence, domicile and ordinary residence confirmed, including the spouse.
- [ ] Ledger in euro, own-wallet transfers removed, cost known for every disposal, one matching method.
- [ ] Each asset classified (coin, utility, financial, hybrid) and tested against the securities definition.
- [ ] Each disposal classified trading or capital, with reasons.
- [ ] Each receipt classified with its recognition event; held branches not taxed automatically.
- [ ] Remittance basis and minimum tax tested.
- [ ] VAT and duty checked.
- [ ] Return reconciled to exchange data; records kept nine years.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for MTCA Guidelines on the Income Tax Treatment of DLT assets (1 November 2018), sections A and B (categories, purpose and context, market value, revenue recognition, remuneration) | https://mtca.gov.mt/docs/default-source/documents/guidelines--dlts-income-tax.pdf?sfvrsn=c74e28fc_1 | 2026-11-14 |
| Read for Cap. 123 arts 4(1)(a) and provisos, 5(1), 5(6)(b), 5(10), 11, 56(6), 56(27) | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-14 |
| Read for Cap. 372 arts 19(1), 19(5) and 44(2A) | https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b | 2026-11-14 |
| Read for S.L. 372.16 rule 2(c) (return dates) | https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 | 2026-11-14 |
| Read for Cap. 406 art. 19(1) (18%) and Fifth Schedule Part Two item 3 (currency exemption) | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-14 |
| Read for Cap. 364 arts 2 and 42 (marketable security, 2%, property-company increase) | https://legislation.mt/eli/cap/364/eng/pdf | 2026-11-14 |
| Read for S.L. 123.127 (DAC8: nine months, periods from 1 January 2026) | https://legislation.mt/getpdf/6a3101a4d3e9ed28acd19036 | 2026-11-14 |
| Read for Cap. 590 art. 66 (VFA licences cancelled 2 July 2026 or on MiCA decision) | https://legislation.mt/eli/cap/590/eng/pdf | 2026-11-14 |
| Read for MTCA Tax Rates 2026, single table (25% band used in the cases) | https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 | 2026-11-14 |
| Read for MTCA Tax Return Cycle (31 July online return) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-11-14 |

Not yet confirmed: MTCA's DLT VAT and duty guidelines (not re-read); the VAT treatment of exchange services, mining, staking services and NFTs; the income treatment and timing of staking, lending, hobby mining, airdrops, forks, wrapping and liquidity pools; an accepted matching method; whether any crypto venue is a recognised stock exchange; the date by which crypto-asset service providers report to MTCA under S.L. 123.127; whether MTCA extends the 2027 return date.
