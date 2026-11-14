---
name: us-crypto-tax
description: Work out a US individual's 2026 federal tax on cryptocurrency and other digital assets, and report it. Covers property treatment under Notice 2014-21, the taxable events (sales, crypto-to-crypto swaps, spending), income on receipt at fair market value for mining, staking (Rev. Rul. 2023-14), airdrops and hard forks (Rev. Rul. 2019-24), DeFi yield and rewards, basis by wallet under Rev. Proc. 2024-28 with specific identification or FIFO, Form 8949 digital asset boxes G to L, 2026 Form 1099-DA broker reporting (gross proceeds for all sales, basis for covered assets acquired after 2025 in a custodial account, the USD 10,000 stablecoin and USD 600 NFT and payment de minimis rules, no staking rewards on the form), the repealed DeFi broker rule, Form 8300 relief, FBAR and Form 8938, gifts, donations with a qualified appraisal above USD 5,000, theft and lost keys, and records. Trigger on "crypto tax", "bitcoin", "ethereum", "staking", "mining", "airdrop", "DeFi", "Form 1099-DA", "Form 8949 digital asset", "Coinbase taxes", "crypto cost basis", "crypto wash sale". Federal only.
version: "2.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: computation
---

# US tax on cryptocurrency and digital assets: income, gains, basis and Form 1099-DA, tax year 2026

> **Source-cited draft.** Built from Notice 2014-21, Rev. Rul. 2019-24, Rev. Rul. 2023-14, Rev. Proc. 2024-28, Announcement 2024-4, CCA 202302012, the 2026 Instructions for Form 1099-DA, the 2025 Form 1040 and Instructions for Form 8949, Public Law 119-21 (sections 70109 and 70433), 26 U.S.C. 1091 and 1411, FinCEN Notice 2020-2 and the IRS digital asset pages, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For US tax, crypto is **property**, not currency. Every sale for dollars, every swap of one token for another, and every purchase paid in crypto is a taxable disposition: gain or loss is proceeds minus basis, short-term if held one year or less, long-term if more, at the rates in `us-capital-gains`. Crypto **received** (mining, staking, airdrops, pay, rewards) is ordinary income at its fair market value when the person gains dominion and control, and that value becomes its basis. Basis is tracked **wallet by wallet** (since 1 January 2025), by specific identification or, by default, first in first out; averaging is not allowed. For 2026, US brokers report **gross proceeds of every sale** on Form 1099-DA and, for the first time, **basis** for assets bought after 2025 and kept in the same custodial account. The wash sale rule does not apply to crypto that is not a security.

## Scope and who this is for

In scope: US citizens and resident aliens filing a 2026 Form 1040 who buy, sell, swap, spend, mine, stake, lend or receive cryptocurrency and other fungible digital assets (including stablecoins), and the reporting that follows.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Capital gain rates, the 3.8% net investment income tax, the USD 3,000 loss limit, Form 8949 and Schedule D mechanics in general | `us-capital-gains` |
| NFTs: collectible status, creators and royalties | `us-nft-tax` |
| Mining or validating as a business: Schedule C and self-employment tax | `us-schedule-c-and-se-computation` |
| Mining equipment: section 179 and bonus depreciation | `us-section-179-and-bonus-depreciation` |
| FBAR and Form 8938 thresholds and filing | `us-fbar-and-fatca-8938` |
| Gift tax returns and the lifetime exemption | `us-estate-gift-706-709` |
| Charitable deduction limits | `us-charitable-giving-strategies` |
| Paying tax during the year | `us-quarterly-estimated-tax` |
| Nonresident aliens | `us-nonresident-cgt` |
| Businesses that accept crypto, brokers' own filing duties, state tax | Refer (see When to refuse or refer) |

## Ask the client first

1. **Every platform and wallet** used in 2026 and earlier: exchanges (US and foreign), hosted wallets, self-custody wallets (hardware, browser), DeFi protocols, and the chains used.
2. **Full transaction histories** (CSV or API exports) from each exchange, and wallet addresses for on-chain activity; every Form 1099-DA, 1099-MISC, 1099-NEC and 1099-K received.
3. **What happened:** purchases, sales, swaps, spending, transfers between own wallets, staking, mining, lending, liquidity pools, airdrops, forks, bridges, wrapping, gifts given or received, donations, theft or lost access.
4. **Basis records:** how basis was assigned to each wallet on 1 January 2025 (Rev. Proc. 2024-28), and whether the client uses specific identification (with standing orders at a broker) or FIFO.
5. **Business or not:** does the client mine or run validators with regularity and a profit motive, or receive crypto for services as a contractor or employee?
6. **Other income and filing status**, to place gains in the rate bands and test the net investment income tax.
7. **Foreign platforms:** balances by month, and whether each account held only crypto or also fiat or securities.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Net investment income tax on investment gains and income | 3.8% | [26 U.S.C. 1411](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, single and head of household (modified AGI) | USD 200,000 | [26 U.S.C. 1411(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, married filing jointly | USD 250,000 | [26 U.S.C. 1411(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| Form 1099-DA: basis reported for assets acquired after this year in a custodial account | 2025 | [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf) |
| Form 1099-DA: qualifying stablecoin sales not reported under the optional method if a customer's yearly gross proceeds do not exceed | USD 10,000 | [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf) |
| Form 1099-DA: specified NFT sales not reported under the optional method if yearly gross proceeds do not exceed | USD 600 | [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf) |
| Form 1099-DA: payment processor sales not reported if a customer's yearly total is not more than | USD 600 | [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf) |
| Form 1099-MISC threshold for payments (for example staking or reward payments from a platform) after 2025 | USD 2,000 | [Public Law 119-21, section 70433](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Gift tax annual exclusion, per donee | USD 19,000 | [Rev. Proc. 2025-32, section 4.42](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Donation of crypto: qualified appraisal required above | USD 5,000 | [CCA 202302012](https://www.irs.gov/pub/irs-wd/202302012.pdf) |
| Form 8300 for a business receiving more than USD 10,000: digital assets counted | Not yet (relief) | [Announcement 2024-4](https://www.irs.gov/pub/irs-drop/a-24-04.pdf) |

The capital gain rate bands, the 28% collectibles rate and the USD 3,000 loss limit are owned by `us-capital-gains`; the self-employment tax figures by `us-schedule-c-and-se-computation`.

### Step 1: crypto is property

1. Convertible virtual currency is treated as **property**; general property tax principles apply, and it does not give foreign currency gain or loss. Source: [Notice 2014-21](https://www.irs.gov/pub/irs-drop/n-14-21.pdf). The Form 8949 instructions use the term **digital asset**: any digital representation of value recorded on a cryptographically secured distributed ledger. Source: [Instructions for Form 8949](https://www.irs.gov/pub/irs-pdf/i8949.pdf).
2. Like-kind exchange treatment under section 1031 is limited to real property, so swaps of tokens are never tax-deferred.
3. **Form 1040 question:** every return asks whether, during the year, the person (a) received a digital asset as a reward, award or payment for property or services, or (b) sold, exchanged or otherwise disposed of a digital asset or a financial interest in one. It must be answered. "No" is right if the only activity was holding, transferring between the person's own wallets or accounts, or buying with real currency. Source: [Form 1040 (2025)](https://www.irs.gov/pub/irs-pdf/f1040.pdf); [IRS, Determine how to answer the digital asset question](https://www.irs.gov/filing/determine-how-to-answer-the-digital-asset-question).

### Step 2: income on receipt (ordinary income at fair market value)

4. **The rule:** crypto received without paying for it is gross income equal to its US dollar fair market value when the person gains **dominion and control** (the ability to sell, exchange or otherwise dispose of it). Fair market value uses the exchange rate set by the market, converted in a reasonable manner consistently applied. Basis in the units equals the amount included, and the holding period starts the day after receipt. Source: [Notice 2014-21](https://www.irs.gov/pub/irs-drop/n-14-21.pdf).

| Event | Treatment | Authority |
| --- | --- | --- |
| Mining rewards | Income at fair market value on receipt; if mining is a trade or business (not as an employee), net earnings are self-employment income | Notice 2014-21, Q&A 8 and 9 |
| Staking rewards (directly or through an exchange) | Income at fair market value when the person gains dominion and control, including the ability to sell; locked rewards count when they become transferable | [Rev. Rul. 2023-14](https://www.irs.gov/pub/irs-drop/rr-23-14.pdf) |
| Hard fork with no new units received | No income | [Rev. Rul. 2019-24](https://www.irs.gov/pub/irs-drop/rr-19-24.pdf), Situation 1 |
| Airdrop of new units after a fork, or any other airdrop | Ordinary income at fair market value when recorded on the ledger and the person can dispose of it; deferred if, for example, the exchange does not yet support the new coin | [Rev. Rul. 2019-24](https://www.irs.gov/pub/irs-drop/rr-19-24.pdf), Situation 2 |
| Unsolicited airdrop | Still income once the person has dominion and control and the token has a value | Rev. Rul. 2019-24 |
| Pay for work, as an employee | Wages at fair market value, on Form W-2 with withholding | Notice 2014-21 |
| Pay for work, as a contractor | Schedule C income at fair market value, subject to self-employment tax | Notice 2014-21 |
| Lending or DeFi yield, earn-account interest | Ordinary income when received (no crypto-specific ruling; general section 61 principle); report as other income, not Schedule B interest | General principles |
| Liquidity-mining and governance reward tokens | Ordinary income when received, by analogy to staking | General principles |
| Referral, learn-and-earn and play-to-earn rewards | Ordinary income when received; a reward tied to a purchase may instead reduce basis; play-to-earn at business scale is self-employment income | General principles |

5. **Where it goes:** outside a business, Schedule 1 (2025 form, line 8v for digital assets received as a reward, award or payment, or line 8z), with no self-employment tax but inside net investment income where it is investment income. In a business, Schedule C and Schedule SE. Mining equipment, power and hosting are deductible only for a business; a hobby's income is taxable and its expenses are not deductible (the suspension of miscellaneous itemized deductions is permanent from 2026 under Public Law 119-21, section 70110). Source: [IRS, Frequently asked questions on digital asset transactions](https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-digital-asset-transactions).
6. **Staking and litigation:** taxpayers have argued that newly created staking tokens are not income until sold. The first refund suit (Jarrett v. United States, 6th Cir. No. 22-6023, 2023) ended as moot after the IRS refunded the tax, and a second suit was filed in 2024. The IRS position in Rev. Rul. 2023-14 stands; follow it, and flag any client who wants the other position (R-CRYPTO-STAKE).
7. **No ascertainable value:** if an airdropped token has no market at receipt, some practitioners report nil income and nil basis. That is aggressive; use any available price (DEX pools, OTC quotes) and flag the position for the reviewer.

### Step 3: dispositions and gain

8. **Taxable dispositions:** sale for dollars or other currency; exchange of one crypto for another (BTC for ETH disposes of the BTC, at the fair market value of the ETH received); paying for goods or services with crypto; liquidating a DeFi position; a collateral liquidation. **Not dispositions:** buying with dollars, holding, moving between the person's own wallets, pledging collateral, and borrowing against crypto (loan proceeds are not income). Interest paid on a crypto loan used for investment may be investment interest under section 163(d).
9. **Gain or loss** = amount realized (fair market value of what is received, less selling costs) minus adjusted basis (cost plus acquisition fees, or the income amount for received units). Held more than one year: long-term; otherwise short-term. Rates, NIIT and the loss limit: `us-capital-gains`.
10. **Unsettled areas** (no IRS guidance; flag each for the reviewer, and apply one position consistently): depositing tokens into a liquidity pool for LP tokens (conservative: a taxable exchange; aggressive: open transaction until withdrawal); withdrawing from a pool (a disposition of the LP position); impermanent loss (not separately deductible; it shows up when the position is closed); wrapping (ETH to wETH) and bridging (conservative: taxable; aggressive: no change in substance).
11. **Small purchases:** there is no de minimis exemption; a coffee bought with bitcoin is a disposition. Proposals for an exemption have not been enacted.

### Step 4: basis, by wallet

12. **Wallet by wallet from 1 January 2025.** Basis must be identified separately for each wallet or account. Rev. Proc. 2024-28 gave a safe harbour to allocate unused basis to the units held in each wallet or account as of 1 January 2025 (by specific allocation or a rule-based method, fixed by that date and documented). Source: [Rev. Proc. 2024-28](https://www.irs.gov/pub/irs-drop/rp-24-28.pdf).
13. **Specific identification:** the person identifies the units sold at the time of the sale, with records of each unit's acquisition date and time, basis and the sale details; for assets held at a broker, through the broker's records or a standing order. This permits choosing the highest-basis lots (HIFO is a form of specific identification). **Without adequate identification, FIFO applies** within that wallet or account.
14. **Averaging is not allowed** for crypto held as property. Average basis applies only to mutual fund and dividend reinvestment plan shares, and the Form 1099-DA instructions allow it for **tokenized securities**, which are securities. A taxpayer who averaged in earlier years should be told that amended returns may be needed.
15. **Received units:** basis is the income amount (Step 2). **Gifts received:** the donor's basis carries over (fair market value at the gift date if lower, for losses), and the holding period tacks on the carryover basis. **Inherited:** fair market value at death.

### Step 5: wash sales, futures and other special rules

16. **Wash sales:** section 1091 applies to "stock or securities". Crypto held as property is neither, so a loss on crypto sold and bought back at once is allowed. It **does** apply to tokenized securities and to crypto exposure held as a security (for example shares of an exchange-traded fund). Proposals to extend it to digital assets have not been enacted. Source: [26 U.S.C. 1091](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm).
17. **Futures:** regulated futures on a qualified board or exchange (for example CME bitcoin futures) are section 1256 contracts: marked to market, 60% long-term and 40% short-term, on Form 6781. Perpetual futures on offshore platforms are generally not section 1256 contracts; refer a disputed classification (R-CRYPTO-1256).
18. **Theft, scams and lost keys:** a personal theft or casualty loss is deductible only if it comes from a federally declared disaster or, from 2026, a state declared disaster; Public Law 119-21, section 70109, made the limit permanent. A theft from a profit-seeking transaction may still be deductible under section 165(c)(2); refer that analysis. A worthless token gives a capital loss in the year it becomes wholly worthless; lost keys give no deduction until the loss is shown to be permanent. Source: [Public Law 119-21, section 70109](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
19. **Gifts given:** no income tax for the donor; Form 709 if gifts to one donee in 2026 exceed **USD 19,000** (`us-estate-gift-706-709`).
20. **Donations:** held more than one year, deduct fair market value with no gain; held one year or less, the lower of basis and value. Form 8283 above USD 500 of noncash gifts (Section B above USD 5,000). For a claim above **USD 5,000** a **qualified appraisal** is required: the IRS position is that crypto is not exempt as a readily valued security, and an exchange price is not a substitute. Source: [CCA 202302012](https://www.irs.gov/pub/irs-wd/202302012.pdf).

### Step 6: Form 8949 and Schedule D

21. Each disposition goes on Form 8949, column (a) with the asset's name or symbol, the exact units, and the transaction ID if available. Digital assets use **boxes G, H and I** (short-term: 1099-DA with basis reported; 1099-DA without basis; no 1099-DA) and **J, K and L** (long-term), never boxes C or F. Totals go to Schedule D. Source: [Instructions for Form 8949](https://www.irs.gov/pub/irs-pdf/i8949.pdf).
22. **Correcting a 1099-DA:** if the broker's basis is wrong, report on box G or J with the broker's basis in column (e) and the correction in column (g) with code B; if basis was not reported, report on box H or K with the correct basis in column (e). Fees not netted by the broker are adjustments. Summary lines are allowed where the instructions permit.

### Step 7: Form 1099-DA for 2026

23. **Who files:** a US digital asset broker: a custodial trading platform, a hosted wallet provider that effects sales, a kiosk operator, a payment processor (with knowledge), or an issuer that regularly redeems its own tokens. Not brokers: pure validators, and sellers of hardware or software that only lets users control their own keys. Source: [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf).
24. **What is reported for 2026 sales:** **gross proceeds for every sale**, and **basis** for **covered securities**: digital assets acquired after 2025 in an account where the broker provided custody, and held there until sold. Assets acquired before 2026, or transferred in from elsewhere, are **noncovered**: the broker may leave basis blank (box 9 checked). Expect 2026 forms to show basis only for 2026 purchases.
25. **Optional and de minimis rules:** qualifying stablecoin sales need not be reported where the customer's total does not exceed USD 10,000 for the year; specified NFT sales where they do not exceed USD 600; payment processor sales where they are not more than USD 600. **Rewards and staking payments are not reported on Form 1099-DA** (look for a Form 1099-MISC, now above USD 2,000, or nothing). Source: [Instructions for Form 1099-DA (2026)](https://www.irs.gov/pub/irs-pdf/i1099da.pdf).
26. **DeFi front ends are not brokers.** The rule that would have made non-custodial DeFi platforms report (T.D. 10021) was disapproved under the Congressional Review Act (Public Law 119-5, 10 April 2025) and the regulation was removed. Self-custody wallets, peer-to-peer trades and DeFi protocols produce no Form 1099-DA, so the client's own records are the only source.
27. **No form is not no tax.** Every disposition is reported whether or not a Form 1099-DA arrives; the IRS matches the forms it does receive against Form 8949.

### Step 8: other reporting

28. **Form 8300:** a business receiving more than USD 10,000 in cash must file Form 8300; the 2021 law added digital assets to "cash", but under Announcement 2024-4 digital assets need not be counted until final regulations are issued. Source: [Announcement 2024-4](https://www.irs.gov/pub/irs-drop/a-24-04.pdf).
29. **FBAR:** "at this time, a foreign account holding virtual currency is not reportable on the FBAR (unless it is a reportable account ... because it holds reportable assets besides virtual currency)". A foreign exchange account that also holds fiat or securities counts in full. Source: [FinCEN Notice 2020-2](https://www.fincen.gov/sites/default/files/shared/Notice-Virtual%20Currency%20Reporting%20on%20the%20FBAR%20123020.pdf). Thresholds and filing: `us-fbar-and-fatca-8938`.
30. **Form 8938:** whether crypto on a foreign platform is a specified foreign financial asset has no final IRS answer; many preparers report it. Thresholds: `us-fbar-and-fatca-8938`. Accounts at US exchanges are not foreign accounts for either form.

### Step 9: records

31. Keep, for every transaction: date and time, units, US dollar fair market value and its source, purpose, counterparty if known, wallet addresses, transaction hashes, and exchange records. Source: [IRS, Frequently asked questions on digital asset transactions](https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-digital-asset-transactions). Valuation: the exchange where the trade happened is the best evidence; widely used price aggregators and timestamped exchange data are acceptable if used consistently. The assessment period is normally 3 years from filing (6 years if income is understated by more than 25%, unlimited with no return or fraud), but basis records are needed for as long as the units are held: keep them indefinitely.

### Step 10: reconcile the exchange exports

32. Download the complete history from each platform; trace every deposit (bought there, transferred in, received as pay) and every withdrawal (to own wallet, paid out, sold); match transfers between the client's own platforms so they are not counted as sales; assign basis per wallet; produce Form 8949 lines; split short-term and long-term; then reconcile to each Form 1099-DA. Typical exports: Coinbase (timestamp, transaction type, asset, quantity, spot price, subtotal, total including fees); Kraken ledgers (txid, refid, time, type, asset, amount, fee, balance; staking rewards itemised); Gemini and Binance.US (date, type, symbol or pair, quantity, price, fee, trade ID). Self-custody wallets such as Coinbase Wallet are not reported by the exchange.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Transfer between two wallets the client owns | Not a disposition; answer "No" to the Form 1040 question if that was the only activity |
| Swap of ETH for USDC | Disposition of the ETH at the dollar value of the USDC received |
| Hard fork, client's exchange does not support the new chain | No income until the client can access and dispose of the new coins |
| Staking rewards locked in an unbonding period | Income when the rewards become transferable |
| Sold at a loss and bought back the same day | Loss allowed (no wash sale rule), unless the asset is a tokenized security or fund share |
| Units bought in 2025, sold on the same exchange in 2026 | Noncovered: 1099-DA shows proceeds; basis may be blank (box H or K) |
| Units bought in 2026 on the exchange where they are sold | Covered: 1099-DA shows basis (box G or J) |
| Units transferred in from a hardware wallet and sold | Noncovered: client supplies basis |
| Coins stolen in a phishing scam, personal account | No casualty deduction outside a declared disaster; a profit-motive theft claim needs referral |
| Donated bitcoin worth USD 8,000 with no appraisal | Deduction at risk: a qualified appraisal is required above USD 5,000 |
| Foreign exchange account holding only crypto | Not an FBAR account under Notice 2020-2; check Form 8938 |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Basis of units transferred in | Do not use zero without telling the client; trace the source wallet first (R-CRYPTO-1 if impossible) |
| Lot identification at the time of sale | FIFO within the wallet or account |
| Whether staking or mining is a business | Treat as non-business (no self-employment tax) and ask about scale, regularity and effort |
| Fair market value at receipt | Price on the platform where received, at that time; record the source |
| Liquidity pool or wrapping position | The conservative taxable treatment, flagged |
| Whether a foreign account holds fiat | Assume it does and count it for the FBAR |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Form 1099-DA proceeds with no matching Form 8949 lines | IRS matching notice |
| Average cost used in earlier years | Not allowed: amended returns may be needed |
| Many DeFi positions and no records | Reconstruction needed before any figure (R-CRYPTO-3) |
| Material balances on foreign platforms and no FBARs | Possible past non-filing (R-CRYPTO-2) |
| Staking or mining with significant equipment and time | Possibly a business: Schedule C and self-employment tax |
| A donation claimed at exchange value above USD 5,000 | Qualified appraisal needed |

## Worked cases

Amounts are invented; the 2026 rates come from `us-capital-gains` and 26 U.S.C. 1411.

**Case 1, a decision: which lot to sell.** A single filer has other 2026 income of USD 150,000 (modified AGI, all ordinary, so any long-term gain falls in the 15% band). In one exchange account she holds 1 BTC bought in 2023 for USD 30,000 and 1 BTC bought in March 2026 for USD 95,000. In November 2026 she sells 1 BTC for USD 90,000.

FIFO (the default): long-term gain USD 60,000, tax 15% = USD 9,000, plus NIIT 3.8% on the smaller of USD 60,000 and the USD 10,000 by which modified AGI (USD 210,000) passes USD 200,000 = USD 380; total USD 9,380. Specific identification of the 2026 lot, made at the time of sale with the broker: short-term loss USD 5,000, of which USD 3,000 offsets ordinary income taxed at 24% (USD 720 saved) and USD 2,000 carries forward. The low-basis 2023 coin remains, with its gain deferred. Recommend specific identification, set up as a standing order with the broker before the sale.

```oa-check
name: Lot selection, FIFO against specific identification (2026)
inputs:
  other_magi: 150000
  proceeds: 90000
  old_lot_basis: 30000
  new_lot_basis: 95000
  niit_threshold: 200000
steps:
  - fifo_gain: proceeds - old_lot_basis
  - fifo_tax: fifo_gain * 0.15
  - fifo_niit: min(fifo_gain, max(other_magi + fifo_gain - niit_threshold, 0)) * 0.038
  - fifo_total: fifo_tax + fifo_niit
  - specific_id_loss: proceeds - new_lot_basis
  - specific_id_saving: min(abs(specific_id_loss), 3000) * 0.24
  - carryforward: abs(specific_id_loss) - min(abs(specific_id_loss), 3000)
expected:
  fifo_gain: 60000.00
  fifo_tax: 9000.00
  fifo_niit: 380.00
  fifo_total: 9380.00
  specific_id_loss: -5000.00
  specific_id_saving: 720.00
  carryforward: 2000.00
```

**Case 2: staking income, then a sale reported on Form 1099-DA.** A client stakes ETH through a US exchange (not a business) and receives 1.2 ETH of rewards during 2026 at an average value of USD 3,500 when each reward became transferable (the actual computation uses each reward's value). Income on Schedule 1: USD 4,200; basis in the 1.2 ETH: USD 4,200. No Form 1099-DA reports the rewards. In December 2026 the client sells the 1.2 ETH for USD 5,000. The Form 1099-DA shows proceeds of USD 5,000; if the exchange leaves basis blank, report on Form 8949 box H with basis USD 4,200: short-term gain USD 800. Total 2026 income from the ETH: USD 5,000, taxed as ordinary income.

```oa-check
name: Staking rewards and a later sale (2026)
inputs:
  units: 1.2
  value_at_receipt: 3500
  sale_proceeds: 5000
steps:
  - staking_income: units * value_at_receipt
  - basis: staking_income
  - short_term_gain: sale_proceeds - basis
  - total_income: staking_income + short_term_gain
expected:
  staking_income: 4200.00
  basis: 4200.00
  short_term_gain: 800.00
  total_income: 5000.00
```

**Other quick results.** An airdrop of 1,000 tokens worth USD 1.15 each when the client can dispose of them: USD 1,150 of ordinary income and USD 1,150 basis; sold later at USD 2.00 each, gain USD 850. A swap of 10 ETH (basis USD 25,000, held under a year) for 50,000 USDC: short-term gain USD 25,000, on box I if no Form 1099-DA is received.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-CRYPTO-1 | No transaction history or wallet records for material positions | Refuse to prepare Form 8949; refer to a crypto tax specialist with blockchain reconstruction tools |
| R-CRYPTO-2 | Material foreign platform holdings and past FBARs or Forms 8938 not filed | Refer to a practitioner experienced in streamlined filing or voluntary disclosure |
| R-CRYPTO-3 | Dozens of DeFi positions with no records | Refuse to estimate; reconstruction first |
| R-CRYPTO-1256 | Disputed section 1256 classification of crypto futures | Refer for sign-off |
| R-CRYPTO-STAKE | Client wants the "no income until sold" position on staking | Refer; disclose the position against Rev. Rul. 2023-14 |
| R-CRYPTO-THEFT | Theft loss from a transaction entered into for profit | Refer: section 165(c)(2) facts and timing |
| R-CRYPTO-BIZ | A business that accepts crypto, or a client that is itself a broker | Refer: Form 8300, Form 1099-DA filing and business accounting |
| R-CRYPTO-STATE | State tax | The state skill |

## Filing and payment

- Report on the **2026 Form 1040**, due **15 April 2027** (extension to 15 October 2027 for filing only): the digital asset question, Form 8949 and Schedule D, Schedule 1 or Schedule C (with Schedule SE) for income, Form 6781 for section 1256 contracts, Form 8283 for donations.
- Brokers furnish 2026 Forms 1099-DA in early 2027; reconcile them before filing.
- Crypto income and gains usually have no withholding: pay through 2026 estimated tax (`us-quarterly-estimated-tax`).
- FBAR and Form 8938: `us-fbar-and-fatca-8938`. Form 709 for gifts above USD 19,000 to one person: due 15 April 2027.

## Completion checklist

- [ ] Every platform and wallet listed and its export obtained.
- [ ] Transfers between own wallets matched and excluded.
- [ ] Every disposition (including swaps and spending) on Form 8949, boxes G to L.
- [ ] All income events (staking, mining, airdrops, rewards, DeFi yield) included at fair market value when control arose.
- [ ] Basis per wallet, with the 1 January 2025 allocation documented; specific identification or FIFO applied consistently; no averaging.
- [ ] Each Form 1099-DA reconciled, corrections shown in columns (f) and (g).
- [ ] NIIT tested; business activity on Schedule C with self-employment tax.
- [ ] Foreign platforms reviewed for FBAR and Form 8938.
- [ ] Unsettled positions (pools, wrapping, no-value airdrops) flagged for the reviewer.
- [ ] The Form 1040 digital asset question answered.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Notice 2014-21. Read for property treatment, receipt at fair market value, mining (Q&A 8) and self-employment (Q&A 9). | https://www.irs.gov/pub/irs-drop/n-14-21.pdf | 2026-11-13 |
| Rev. Rul. 2019-24. Read for hard forks (Situation 1) and airdrops (Situation 2). | https://www.irs.gov/pub/irs-drop/rr-19-24.pdf | 2026-11-13 |
| Rev. Rul. 2023-14. Read for staking rewards and dominion and control. | https://www.irs.gov/pub/irs-drop/rr-23-14.pdf | 2026-11-13 |
| Rev. Proc. 2024-28. Read for wallet-by-wallet basis and the safe harbour as of January 1, 2025. | https://www.irs.gov/pub/irs-drop/rp-24-28.pdf | 2026-11-13 |
| Instructions for Form 1099-DA (2026). Read for covered securities (acquired after 2025, custodial), noncovered securities, the $10,000 stablecoin and $600 NFT and PDAP rules, and "Do not report rewards and staking payments on Form 1099-DA". | https://www.irs.gov/pub/irs-pdf/i1099da.pdf | 2026-11-13 |
| Instructions for Form 8949 (2025). Read for boxes G to L and "Do not use box C". | https://www.irs.gov/pub/irs-pdf/i8949.pdf | 2026-11-13 |
| Form 1040 (2025). Read for the digital asset question wording. | https://www.irs.gov/pub/irs-pdf/f1040.pdf | 2026-11-13 |
| IRS, Determine how to answer the digital asset question. Read for the Yes and No cases. | https://www.irs.gov/filing/determine-how-to-answer-the-digital-asset-question | 2026-11-13 |
| IRS, Frequently asked questions on digital asset transactions. Read for reporting lines and records. | https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-digital-asset-transactions | 2026-11-13 |
| Announcement 2024-4. Read for digital assets not yet counted for Form 8300. | https://www.irs.gov/pub/irs-drop/a-24-04.pdf | 2026-11-13 |
| CCA 202302012. Read for the qualified appraisal requirement for donated cryptocurrency. | https://www.irs.gov/pub/irs-wd/202302012.pdf | 2026-11-13 |
| Public Law 119-21. Read for section 70109 (casualty loss limit permanent, state declared disasters), 70110 (miscellaneous itemized deductions) and 70433 ($2,000 information reporting threshold after 2025). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the 2026 gift annual exclusion ($19,000). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 1091 (govinfo). Read for "stock or securities". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partVII-sec1091.htm | 2026-11-13 |
| 26 U.S.C. 1411 (govinfo). Read for 3.8% and the $250,000 and $200,000 thresholds. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-13 |
| FinCEN Notice 2020-2. Read for crypto-only foreign accounts not reportable on the FBAR "at this time". | https://www.fincen.gov/sites/default/files/shared/Notice-Virtual%20Currency%20Reporting%20on%20the%20FBAR%20123020.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form 1040, Schedule 1 and Instructions for Form 8949 were not published when read, so the digital asset question wording, the Schedule 1 line (8v on the 2025 form) and the box letters are taken from the 2025 editions; the 2026 recipient statement due date for Form 1099-DA is not quoted; the status of the second Jarrett suit was not checked.
