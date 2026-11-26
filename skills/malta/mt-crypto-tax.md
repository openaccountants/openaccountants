---
name: mt-crypto-tax
description: Use this skill whenever asked about Malta cryptocurrency or digital asset taxation for basis year 2026. Trigger on phrases like crypto tax Malta, Bitcoin Malta, DLT assets, cryptocurrency gains, crypto income Malta, Binance Malta tax, staking Malta, mining income Malta, NFT tax Malta, Coinbase Malta, Revolut crypto Malta, token tax, distributed ledger, MFSA crypto, DAC8, or any question about the income tax, capital gains, VAT or duty treatment of cryptocurrency, tokens or digital assets for Malta tax residents or Malta-source crypto income. Covers the Commissioner's DLT asset guidelines (coins, financial, utility and hybrid tokens), trading versus investment, receipts such as mining and staking, the remittance basis and the EUR 5,000 minimum tax, companies at 35%, VAT, duty on share-type tokens and DAC8 reporting from 1 January 2026. Read it before any Malta crypto work.
version: "2.1"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
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
- Historical returns, including 2025 income, need the rules and rates for their own year; this Guide does not certify an unchanged prior-year result.

**How the law is built.** Apply the Income Tax Act, Cap. 123, and the asset’s actual rights and use: trading income under art. 4(1)(a), other income under art. 4(1), and capital gains only on the assets listed in art. 5. The Commissioner's *Guidelines on the Income Tax Treatment of transactions or arrangements involving DLT assets* (issued 1 November 2018 under art. 96(2)) set out the classification and valuation approach. The guidelines say: "Ultimately, the tax treatment of any type of DLT asset will not necessarily be determined by its categorisation, but will depend on the purpose for and context in which it is used."

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

1. **Fix the taxpayer, basis period and assessment year.** Use the applicable ordinary or permitted accounting period; this Guide’s individual examples use calendar 2026.
2. **Build the ledger.** Record every acquisition, transfer, receipt and disposal, value and fee. Use the taxpayer’s reporting currency; the individual examples here use euro. Reconcile same-owner wallet movements without assuming that wrapping, exchange custody, fees or a change in rights is tax-neutral.
3. **Classify the actual rights.** Test the full article 5 asset list, including securities and intellectual property, not just the crypto label. Genuine coins and utility tokens, as defined by the income-tax guidelines, fall outside capital-gains tax; financial tokens need the securities test. An NFT can convey additional rights: Check this point with one of our partner accountants.
4. **Trading or capital for each disposal.** A trade, or an asset bought "for the purpose of profit-making by sale", gives income under art. 4(1)(a). Otherwise a gain on a coin or utility token is capital outside art. 5 and is not taxed.
5. **Other receipts.** Find the income head and the recognition event before valuing any mining, staking, lending, reward or work payment. Crypto does not create a cash basis: the guidelines say that for businesses accepting crypto "there is no change to when revenue is recognised or the manner in which taxable profits are calculated". Unsettled receipt classes are explicitly referred below; do not fill a missing recognition rule from a token label.
6. **Residence rules.** Subject to the long-term/permanent-residence and spouse exceptions below, article 4(1) provisos distinguish foreign income received in Malta from foreign capital gains. First determine whether the item is income or capital and where it arises; then test article 56(27).
7. **Compute.** Individuals: add crypto income to chargeable income at the normal rates. Companies: the ordinary article 56(6) rate is 35%; special/elective regimes and refunds require the corporate-tax Guide.
8. **VAT and duty.** Any taxable supply paid in crypto, NFTs, services to identified customers; any share-type token transferred.
9. **File and pay** using the actual filing-year form, and apply the record-retention conditions below.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Individual crypto income | Added to chargeable income at the 2026 rates; single 25% band less EUR 3,400 from EUR 16,001 to EUR 60,000 | Rate tables owned by malta-income-tax | MTCA Tax Rates 2026: https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 |
| Company rate on chargeable income | 35% ("thirty-five cents ... on every euro") | Ordinary rate only; special/elective company regimes and shareholder refunds require separate analysis | Cap. 123 art. 56(6): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Non-dom minimum tax | EUR 5,000 a year | Ordinarily resident/non-domiciled and article 4 provisos apply; no other minimum-tax scheme; foreign income at least EUR 35,000 not fully received; joint-assessed spouses aggregate. Article 5A tax excluded; test before double-tax relief; lower worldwide liability if proved to Commissioner | Cap. 123 art. 56(27): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Interest on late income tax | 0.6% for every month or part, capped at the tax | Tax payable on or after 31 August 2022 | Cap. 372 art. 44(2A): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Record retention | Not less than nine years after completion of relevant transactions/acts/operations | Article 19 records; alternative Companies Act article 26/163(5)/324(2) retention rules can apply | Cap. 372 art. 19(5): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| VAT standard rate | 18% | Only a supply actually standard-rated in Malta by a person liable to charge it; crypto payment alone does not determine rate, place, exemption or registration | Cap. 406 art. 19(1): https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 |
| Duty on a share-type token | EUR 2 per EUR 100 or part of the higher of consideration/real value; extra EUR 3 per EUR 100 or part if article 42(2) applies | Ordinary non-foreign marketable-security document within article 42(1)(b); exemptions and indirect property-company tests require individual review | Cap. 364 art. 42(1), (2): https://legislation.mt/eli/cap/364/eng/pdf |
| DAC8 exchange of crypto data | Within nine months after the end of the calendar year | Data for periods from 1 January 2026 | S.L. 123.127: https://legislation.mt/getpdf/6a3101a4d3e9ed28acd19036 |
| Ordinary individual statutory return/settlement | 30 June 2027 for 2026 income | No 2027-specific online concession assumed | S.L. 372.16 rule 2(c)(ii): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |
| Company return date | Later of the last day of the ninth month after the accounting period and 31 March of the year of assessment | 30 September 2027 for a 31 December 2026 period; payment can follow special settlement provisions and must be checked separately | S.L. 372.16 rule 2(c)(i): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |

### Which crypto-assets fall under which rule

Article 5 taxes capital gains only on: immovable property; "securities, business, goodwill, business permits, copyright, patents, trademarks and trade-names and any other intellectual property"; a beneficial interest in a trust; an interest in a partnership. "Securities" means "shares and stocks and such like instrument that participate in any way in the profits of the company and whose return is not limited to a fixed rate of return, units in a collective investment scheme ... and units and such like instruments relating to linked long term business of insurance." An asset outside the list is taxed only if the profit is income.

The Commissioner's categories (DLT income-tax guidelines, section A):

| Category | What the guidelines say | Article 5 capital gains? | Trading profit taxable? |
|---|---|---|---|
| Coin | No characteristics of a security, no link to a project or equity, "designed to be used as a means of payment or medium of exchange, or function as a store of value" | No: not securities | Yes, art. 4(1)(a) |
| Financial token | Qualities similar to equities, debentures, collective investment scheme units or derivatives (dividends, interest, fund payments, asset-linked payments, voting or ownership rights) | Yes, if it meets the securities definition | Yes, if dealt in |
| Utility token | Use restricted solely to acquiring goods or services within the platform or a limited network; no link to equity | No | Yes |
| Hybrid | "Where a hybrid token is used in a particular case as a utility token then it is to be treated as such, while if in another occasion the same token is used as a coin, then it needs to be treated as such" | By use | Yes |

A token whose return is limited to a fixed rate fails the share-like limb, but still test the collective-investment-scheme and linked-insurance limbs; do not finalize the classification before all rights are checked; an unresolved classification is referred. Listed shares on an exchange recognised by the Commissioner (not fund units) are outside the capital gains rule (art. 5(6)(b)); whether a crypto venue qualifies for that exemption: Check this point with one of our partner accountants. Art. 5 losses "shall not be set off against other income ... but shall be carried forward and set off against capital gains" (art. 5(10)); a loss on a coin held as an investment gives no relief.

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

**No invented classification.** Record the trade/profit-making indicators and evidence; they are prompts, not a mechanical score or statutory safe harbour. Where they do not settle the transaction: Check this point with one of our partner accountants. Never turn uncertainty into taxable income by default.

### Other crypto receipts

| Receipt | Working treatment | Status |
|---|---|---|
| Crypto received as salary or fees | Employment (art. 4(1)(b)) or business (art. 4(1)(a)); ordinary recognition, market value at the event | Statute; guidelines on remuneration |
| Goods or services sold for crypto | Business income at the euro value received; a later disposal of the crypto is a separate event | Statute; guidelines |
| Mining as a business | Income under art. 4(1)(a); ordinary recognition and allowable costs | Guidelines; statute |
| Hobby-scale mining | Check this point with one of our partner accountants. | Referred |
| Staking and validator rewards | Check this point with one of our partner accountants. | Referred |
| Lending interest (DeFi or platform) | Check this point with one of our partner accountants. | Referred |
| Airdrops, whether gratuitous or linked to a task | Check this point with one of our partner accountants. | Referred |
| Hard fork coins | Do not assign a nil cost automatically. Check this point with one of our partner accountants. | Referred |
| Liquidity pools | No categorical impermanent-loss conclusion. Check this point with one of our partner accountants. | Referred |
| NFTs bought and sold | Test actual rights and trading/profit-making purpose; no blanket capital exemption from the NFT label | Article 4(1)(a), article 5; doubtful rights referred |
| NFTs created and sold by an artist | Establish the activity, rights transferred and income head. Check this point with one of our partner accountants. | Referred |

**Value.** The guidelines: market value "may be determined by reference to the rate established by the relevant Maltese authority, and where such is not available by reference to the average quoted price on reputable exchanges, on the date of the relevant transaction or event".

### Cost, ledger and records

- **Cost and fees:** record acquisition consideration, exchange fees, commissions, network charges and proceeds separately. Do not automatically add every fee to tax cost or deduct it from proceeds; establish the applicable income/capital rule. Check this point with one of our partner accountants.
- **Matching method:** keep transaction-level evidence. FIFO, specific identification and any other proposed method: Check this point with one of our partner accountants.
- **Same-owner movements:** reconcile the beneficial ownership and rights before excluding a wallet movement from sale proceeds; assess fees separately. Custody changes or wrapping ETH to WETH: Check this point with one of our partner accountants.
- **Exchange/spending events:** record crypto to fiat, crypto to crypto (including a stablecoin), and spending. Determine the tax character and valuation of each; a ledger label alone does not establish taxable disposal.
- **Unknown cost: stop.**
- **Records:** "proper and sufficient records" (ITMA art. 19(1)), kept for at least nine years after completion of the relevant transactions, acts or operations, subject to the alternative Companies Act article 26/163(5)/324(2) cases (article 19(5)): exchange exports, wallet addresses, on-chain links, the matching ledger, mining and staking logs.

### Residence, domicile and the remittance basis

| Client | Crypto income | Crypto capital gains (art. 5 assets only) |
|---|---|---|
| Resident, ordinarily resident and domiciled | Worldwide | Worldwide |
| Resident but not domiciled, or not ordinarily resident | Malta-source in full; foreign income only "on the amount received in Malta" (proviso (i)) | Malta gains only; "no tax shall be payable on capital gains arising outside Malta" (proviso (ii)) |
| Not resident | Malta-source only | Malta-source only |

- A wallet or exchange being abroad does not establish foreign-source income. Source, trading carried on from Malta and the remittance character of proceeds: Check this point with one of our partner accountants.
- Provisos (i) and (ii) do not apply to a long-term resident, a permanent residence certificate or card holder (from the year granted), or an individual "whose spouse is ordinarily resident and domiciled in Malta".
- Trace income, capital and disposal proceeds separately. Do not classify every bank transfer as taxable remitted income or every token gain as foreign. Check this point with one of our partner accountants.
- **Minimum tax (art. 56(27)):** ordinarily resident but not domiciled, taxed under the provisos, not under another minimum-tax scheme, with foreign income "not less than thirty five thousand euro (€35,000)" not received or not fully received in Malta (both spouses' income counts under joint assessment). The minimum is tested before relief under articles 76–89; tax paid by withholding or otherwise on income counts, excluding article 5A tax. A lower worldwide tax liability applies only if proved to the Commissioner. The EUR 35,000 threshold tests total relevant foreign income, not just the unremitted portion.

### Companies

- The ordinary article 56(6) rate is 35% on chargeable income. Determine actual transaction character; company incorporation alone does not prove trading. Special/elective regimes and refunds: Check this point with one of our partner accountants.
- Use the company’s actual permitted accounting period. The ordinary return date follows S.L. 372.16 rule 2(c)(i); do not assume the tax payment date is identical where special settlement provisions apply. Check this point with one of our partner accountants.
- Regulation is not decided here. Under Cap. 590 article 66(2), VFA licences were "automatically ... cancelled on 2 July 2026 or upon the granting or refusal of an authorisation pursuant to Article 63 of the MiCA Regulation ... whichever comes first" (art. 66(2)). The tax classification still follows the actual rights and transaction. MiCA authorisation or an alternative regulatory route: Check this point with one of our partner accountants.

### VAT on crypto transactions

Apply the VAT Act and the actual supply, parties, place and consideration. The [MTCA DLT VAT guidelines](https://mtca.gov.mt/docs/default-source/documents/distributed-ledger-technology-%28dlt%29-assets.pdf) apply the currency exemption to genuine coins serving solely as an alternative means of payment, and to their exchange for fiat or other cryptocurrencies where there is a supply for consideration. This does not make every crypto service exempt. The guidance follows [Hedqvist (C-264/14), operative ruling](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62014CJ0264); the exemption concerns qualifying currency exchange, not all tokens or NFTs.

| Transaction | VAT treatment and boundary | Status |
|---|---|---|
| Investor buys, sells or swaps | Establish economic activity and actual coin/token rights before deciding VAT. Check this point with one of our partner accountants. | Referred |
| Qualifying currency exchange for consideration | Exempt under Fifth Schedule Part Two item 3(4), where the coins serve solely as an alternative means of payment | MTCA VAT guidance, Coins |
| Goods or services paid for in crypto | Apply the actual underlying supply’s VAT place, rate, registration and exemption; payment medium does not prescribe 18% | General supply analysis |
| Mining with newly minted coins and no identified recipient/direct reciprocal link | Normally outside VAT in the circumstances described by the guidance | MTCA VAT guidance, Mining |
| Mining/hosting/node services for a specified customer’s fee | Test direct link, consideration, place, status and any exemption. Check this point with one of our partner accountants. | Referred |
| Digital-wallet service | Currency/payment/security transaction can qualify for exemption; a mere technological service is taxable, subject to actual place/status | MTCA VAT guidance, Digital Wallets |
| Staking-as-a-service | Check this point with one of our partner accountants. | Referred |
| NFT sales and electronically supplied services/OSS | No categorical electronic-service or consumer-location conclusion. Check this point with one of our partner accountants. | Referred |

Input VAT is a separate test. Article 22(4)(d)(v) includes specified financial operations where the customer is outside the Community **or** the operations are directly linked to goods exported outside it; article 22(5) and the Tenth Schedule still impose evidence, attribution and other conditions. Do not infer full deduction merely because a customer is abroad. Registration, returns and OSS: [malta-vat-return](malta-vat-return.md).

### Duty on documents and transfers

A marketable security is a holding of share capital in a company and a document representing it (Cap. 364 article 2). The [MTCA DLT duty guidelines](https://mtca.gov.mt/docs/default-source/documents/guidelines---dlts-duty-on-docs.pdf) put genuine coins and utility tokens without share/security characteristics outside duty; substance prevails over the token label.

For a non-foreign marketable-security transfer document within article 42(1)(b), ordinary duty is EUR 2 for every EUR 100 **or part** of the higher of consideration and real value. Article 42(2)(a) adds EUR 3 per EUR 100 or part where at least 75% of the specified company assets (excluding current assets other than immovable property) consists of immovable property or rights over it. Indirect property-company holdings have the separate aggregate test in article 42(2)(b). Do not substitute a casual property-company label for either test. Foreign securities, exemptions, restructuring, indirect holdings, valuation or filing: Check this point with one of our partner accountants.

### Reporting by crypto exchanges (DAC8)

Malta transposed Directive 2023/2226 (DAC8) into the Cooperation with Other Jurisdictions on Tax Matters Regulations, S.L. 123.127. A Reporting Malta Crypto-Asset Service Provider applies the due diligence and reporting rules, including users' self-certification of tax residence. Malta exchanges the data "within nine (9) months following the end of the calendar year", for periods "as from 1 January 2026". This is the authority-to-authority exchange period, not a nine-month provider filing deadline. Annex VII section II(D) requires annual provider reporting in the following calendar year, first for periods from 1 January 2026; section III requires residence self-certification and reasonableness checks. Whether a provider, user or transaction is reportable and its operational deadline: Check this point with one of our partner accountants. Reconcile the return to actual exchange records rather than assuming every transaction is reported.

## Boundary and exception table

| Situation | Treatment | Why |
|---|---|---|
| One coin bought to sell at a profit, sold months later | Income under art. 4(1)(a) | Bought "for the purpose of profit-making by sale" |
| Coin bought to hold, sold years later, no trading pattern | Not taxed | Not in the art. 5 list; capital |
| Loss on a coin held as an investment | No relief | Outside art. 5 |
| Trading loss | Business loss rules (see malta-income-tax) | Art. 4(1)(a), 14 |
| Token sharing in profits with no fixed cap | Test full securities definition, actual rights and any exemption; not automatic tax from the label | Article 5(1), (6) |
| Token paying a fixed return | Hold until the scheme and insurance limbs are checked | Art. 5(1) |
| Non-dom, foreign crypto income kept abroad | Subject to the residence/spouse exceptions, unremitted foreign income is outside ordinary charge; test all minimum-tax conditions | Art. 4(1) proviso (i); 56(27) |
| Non-dom whose spouse is ordinarily resident and domiciled in Malta | Worldwide | Provisos do not apply |
| Non-dom, foreign gain on a financial token | Only if a genuine foreign capital gain and the article 4 exceptions do not disapply relief; do not use for trading income | Art. 4(1) proviso (ii) |
| Own-wallet movement | Reconcile unchanged beneficial ownership/rights; do not classify fees or wrapping automatically | Individual uncertainty referred |
| Crypto-to-crypto or stablecoin swap | Record value and rights exchanged; determine actual tax character, not a blanket label | MTCA market-value approach; doubtful arrangements referred |
| Transfer of a coin or utility token | No duty | Not a marketable security |
| Transfer of a share-type token in Malta | Ordinary EUR 2 per EUR 100 or part; extra EUR 3 only when article 42(2) conditions apply; subject to exemptions | Cap. 364 art. 42 |

### Reading exchange and bank statements

| Line | Likely meaning | Action |
|---|---|---|
| Exchange sell, payout to bank (Binance, Coinbase, Kraken, Revolut) | Disposal proceeds | Match to cost; euro at the date |
| Exchange buy, card purchase of crypto | Acquisition | Record cost with fees |
| Gas, network, trading fee, commission | Separate expense record | Determine tax cost/deductibility; do not post automatically |
| Mining reward, pool payout, staking or "earn" reward | Receipt | Hold until classified |
| Airdrop | Unclassified receipt | Check this point with one of our partner accountants. |
| Transfer between own accounts | Candidate same-owner movement | Check beneficial rights, fees and on-chain evidence |
| P2P transfer | Sale, purchase or own transfer | Ask |
| Hardware wallet purchase | Equipment candidate | Deduction/capital allowance eligibility: Check this point with one of our partner accountants. |

## Worked cases

Individuals are resident, ordinarily resident and domiciled, on the 2026 single table, unless stated. All are invented.

### Case 1: frequent trader

Bought one BTC for EUR 25,000 in January 2026, sold for EUR 45,000 in March 2026, fees EUR 100; over 50 trades in the year; no other income. Assuming trading and the EUR 100 fee is allowable, income is EUR 19,900. Tax: EUR 19,900 x 25% less EUR 3,400 = EUR 1,575.

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

Bought 2 ETH at EUR 1,500 each in 2021, sold both at EUR 3,500 each in 2026; three trades in five years; salary of EUR 30,000 chargeable income. Gain EUR 4,000. If the facts support a capital holding, coins are not art. 5 assets and the gain is not taxed: nil. If the ETH was bought to resell at a profit, the gain is income: extra tax EUR 1,000 at 25%. Intention and the full facts decide the classification; three trades, holding length or no leverage alone is not a safe harbour. The conditional difference is EUR 1,000.

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

- **Staking on top of a salary.** Salary EUR 30,000; staking rewards EUR 1,750, only if properly classified and recognised as 2026 income: extra tax EUR 437.50 (EUR 4,537.50 against EUR 4,100). The later tax cost of the coins is not established by this arithmetic: Check this point with one of our partner accountants.
- **Non-dom and the minimum tax.** Foreign income EUR 50,000, none brought in; tax on Malta income EUR 1,200: if every article 56(27) condition is met, the pre-relief top-up is EUR 3,800, subject to proof of a lower worldwide liability and the tax-credit rules. At EUR 30,000 total relevant foreign income, the EUR 35,000 threshold is not met; this does not exempt Malta-source or remitted income.
- **Trading company.** Chargeable income EUR 100,000 to 31 December 2026 under the ordinary 35% regime: EUR 35,000 before other adjustments. Ordinary return date 30 September 2027; applicable settlement date/special regime must be determined separately: Check this point with one of our partner accountants.
- **Shop accepting BTC.** Assume an underlying Malta supply properly standard-rated at 18%, gross EUR 1,180 paid in BTC: conditional VAT EUR 180 (18/118). The later BTC movement needs its own income/capital analysis; payment in BTC alone establishes neither the rate nor trading.
- **Share-type token.** EUR 10,000 is assumed to be the higher of consideration/real value in an ordinary chargeable article 42(1)(b) transfer: EUR 200; EUR 500 only if article 42(2) increase applies. A genuine BTC coin for EUR 10,000 falls outside duty under the DLT guidance. Token rights, exemptions and property tests must be established, not assumed.

## When to refuse or refer

**Stop and ask** when residence, domicile or ordinary residence is unknown, or there are no records or no acquisition cost.

**Check this point with one of our partner accountants** when: tokens are being issued; financial, hybrid or securities status decides material money; a non-dom's trading may arise in Malta, or foreign income is near EUR 35,000; company refunds, group relief or participation rules matter; DeFi, DAOs or cross-border structures are involved; a ruling is warranted; licensing advice under MiCA and Cap. 647 is wanted.

**Never:** say all crypto gains are tax-free in Malta; call a coin "securities"; apply the remittance basis without checking the exceptions; apply the minimum tax without the EUR 35,000 test; treat own-wallet transfers as disposals; quote a guideline from memory or stretch the income-tax guidelines to VAT or DeFi facts; present an answer as final without review.

## Filing and payment

| What | When | Source |
|---|---|---|
| Ordinary individual return and self-assessment, 2026 income | Statutory return/settlement 30 June 2027; no 2027-specific online concession assumed | S.L. 372.16 rule 2(c)(ii); MTCA Tax Return Cycle |
| Company return, period to 31 December 2026 | 30 September 2027 | S.L. 372.16 rule 2(c)(i) |
| Provisional tax | Instalment dates: see [mt-estimated-tax](mt-estimated-tax.md) | ITMA |
| Late tax | 0.6% a month or part, capped at the tax | ITMA art. 44(2A) |
| VAT returns | See [malta-vat-return](malta-vat-return.md) | Cap. 406 |
| Duty on a share-type token | With the share transfer notification: see [selling-a-company-in-malta](selling-a-company-in-malta.md) | Cap. 364 |

Classify the income head before choosing a return section; not every non-trading receipt belongs in an “other income” box. The general MTCA cycle page identifies [myTax](https://mytax.mtca.gov.mt/) with e-ID and a 31 July online deadline, but does not establish a 2027-specific concession. Actual form fields, provider reporting deadlines or future online concessions: Check this point with one of our partner accountants.

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
| Read for MTCA Guidelines on the Income Tax Treatment of DLT assets (1 November 2018), sections A and B (categories, purpose and context, market value, revenue recognition, remuneration) | https://mtca.gov.mt/docs/default-source/documents/guidelines--dlts-income-tax.pdf?sfvrsn=c74e28fc_1 | 2026-11-26 |
| Read for Cap. 123 arts 4(1)(a) and provisos, 5(1), 5(6)(b), 5(10), 56(6), 56(27) | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-26 |
| Read for Cap. 372 arts 19(1), 19(5) and 44(2A) | https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b | 2026-11-26 |
| Read for S.L. 372.16 rule 2(c) (return dates) | https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 | 2026-11-26 |
| Read Cap.406 article19(1),22(3)–(5) and FifthSchedulePartTwoitem3: standard rate, input attribution and currency exemption | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-26 |
| Read for Cap. 364 arts 2 and 42 (marketable security, 2%, property-company increase) | https://legislation.mt/eli/cap/364/eng/pdf | 2026-11-26 |
| Read S.L.123.127 regulation13(8)(g), AnnexVII sectionII(D), sectionIII: authority exchange, provider annual reporting and residence self-certification | https://legislation.mt/getpdf/6a3101a4d3e9ed28acd19036 | 2026-11-26 |
| Read for Cap. 590 art. 66 (VFA licences cancelled 2 July 2026 or on MiCA decision) | https://legislation.mt/eli/cap/590/eng/pdf | 2026-11-26 |
| Read for MTCA Tax Rates 2026, single table (25% band used in the cases) | https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 | 2026-11-26 |
| Read for MTCA Tax Return Cycle (31 July online return) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-11-26 |
| MTCA DLT VAT guidelines, Coins, Digital Wallets, Mining and general place/supply approach actually read | https://mtca.gov.mt/docs/default-source/documents/distributed-ledger-technology-%28dlt%29-assets.pdf | 2026-11-26 |
| MTCA DLT duty guidelines, categories and substance/marketable-security approach actually read | https://mtca.gov.mt/docs/default-source/documents/guidelines---dlts-duty-on-docs.pdf | 2026-11-26 |

| Hedqvist C-264/14, paragraphs27/53–57 and operative ruling actually read; qualifying bitcoin/fiat exchange for spread | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62014CJ0264 | 2026-11-26 |

Not yet confirmed: no unsupported crypto classification remains usable. DeFi/hobby mining/staking/lending/airdrops/forks/wrapping/liquidity pools, NFT rights/receipts/VAT, cost/matching/fees, source/remittance tracing, special company regimes/payment dates, indirect property/exemption duty cases, provider operational reporting and 2027 form/online details are explicitly referred above. Recognised crypto-venue status is referred; no 2025 classification certification is made.
