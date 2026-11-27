---
name: au-crypto-tax-2
description: "Australian crypto tax: reconcile holdings, classify transactions, value rewards and distinguish current ATO guidance from draft rulings."
jurisdiction: AU
last_updated: 2026-11-27
version: 1
category: crypto
tax_year: 2026
tax_year_notes: "2026 reconciliation reference; ordinary investment CGT events before 1 July 2027; drafts remain preliminary, not final law"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Ryan Duguid"
reviewed_on: 2026-11-03
tier: 1
domain: crypto
---

# Australian crypto asset tax

Reconcile the taxpayer's wallets and exchange accounts before calculating crypto income or capital gains. This is a 2026 Australian transaction-reconciliation and classification method. The ordinary investment-discount calculation below covers eligible CGT events before 1 July 2027; later events require the enacted reform and transitional rules, not automatic reuse of the old percentage. Draft ATO rulings are identified separately. [ITAA 1997, Division 115][law3]; [2026 reform, Schedule 1 item 82][reform].

## Ask the client first

Obtain the income year, entity type and residence history; purpose and nature of each activity; complete wallet/exchange exports and ownership terms; parcel acquisition dates and costs; reward/service receipts; AUD valuations and fees; available capital losses; personal-use evidence; and any missing assets, distributions or compensation. Do not infer beneficial ownership from an exchange's transaction label.

## Establish the activity and transaction history

Determine whether the taxpayer invests, carries on a trading or mining business, receives payment for services, or undertakes a separate profit-making transaction. Frequency alone does not settle business status: consider commercial purpose, profit intention, organisation, repetition and scale together. A separate profit-making transaction needs its own commercial-purpose analysis; wanting an investment to appreciate is not by itself a business classification. [ATO: crypto assets used in business][business]; [TR 97/11, paragraphs 11–16][indicators]; [TR 92/3, paragraphs 6–7 and 35–37][isolated].

Crypto held for sale or exchange in the ordinary course of a crypto business is trading stock; business receipts and allowable expenses use the revenue rules, including stock on hand, rather than the investment-discount calculation. A business may separately hold an investment on capital account. Payment for services is valued when the income is derived. Apply the trading-stock disregard or the ordinary-income/CGT anti-overlap rule where applicable, rather than taxing the same gain twice. [ITAA 1997, sections 6-5, 8-1][law1], [70-10, 70-35, 118-20 and 118-25][law3]; [ATO business guidance][business].

- **Records and reconciliation** — Collect exchange exports, wallet addresses, transaction identifiers, timestamps, token quantities, fees and Australian dollar valuations. Account for each asset separately. Match transfers between the taxpayer's own wallets; no disposal arises where beneficial ownership remains unchanged. Check exchange, lending and custody terms before accepting that conclusion. Crypto used to pay a transfer/network fee is a separate disposal to classify. Reconcile opening units plus receipts less disposals and fee units to closing units; count fee units once, not again within disposals. [ATO: keeping crypto records][records]; [ATO: crypto investments and tax][transfers]; [ITAA 1997, section 104-10][law3].

## Classify disposals and acquisitions

- **Events and timing** — Selling, swapping, giving away or spending investment crypto can trigger CGT. A swap generally disposes of the original asset and acquires the replacement; record both legs without inventing a disposal of the newly acquired asset. For an A1 disposal, the event is at contract date, or ownership change if there is no contract; a contract that falls through without ownership changing does not produce that event. [ITAA 1997, section 104-10][law3]; [ATO: crypto-to-crypto exchange or swap][swap].
- **Proceeds, cost base and fees** — Identify the parcel and event-date AUD money/property proceeds. Gifts and specified non-arm's-length cases require market-value substitution, subject to the statutory exceptions. Start with money/property paid or required to acquire the asset and include only eligible cost-base elements. Classify actual fees by the transaction: no automatic deduction or addition to every asset. Apply the statutory exclusions and adjustments for deducted or deductible costs, recoupments and net input tax credits. Use reduced cost base when testing a loss; it is not necessarily the gain cost base. Missing evidence does not prove zero cost: reconstruct it before finalising. [ITAA 1997, sections 103-30, 110-25, 110-35, 110-45, 110-55, 116-20 and 116-30][law3].
- **Capital losses and discount** — For the pre-1 July 2027 calculation, apply eligible current-year losses, then available earlier net capital losses (oldest first), before any discount. Capital losses cannot offset ordinary staking or business income. Personal-use losses are disregarded; collectable losses are restricted to collectable gains. Check loss availability and category before using a carried-forward amount. [ITAA 1997, sections 102-5, 102-10 and 102-15 as applicable before the reform][oldlaw3]; [sections 108-10 and 108-20][law3].
- **CGT discount for individuals** — For ordinary eligible investment events before 1 July 2027, an individual can generally access the **50%** discount after the required **12-month** holding period. Exclude acquisition and event days when counting. Check special acquisition histories and excluded gains; foreign or temporary residence during the ownership period can reduce or deny the percentage. Ordinary companies cannot use the general discount. This does not determine later-event or transitional calculations: Check this point with one of our partner accountants. [ITAA 1997, sections 115-10, 115-25, 115-30, 115-100 and 115-105–115-115][law3]; [ATO discount guidance][discount]; [reform application][reform].

## Staking rewards and airdrops

- **Staking rewards** — Ordinary staking rewards are income at their AUD money value when received, including amounts applied on the recipient's behalf. Record that value as the reward tokens' cost base and calculate their later investment disposal separately. Do not treat all subsequent sale proceeds as a second receipt of the original reward income. [ITAA 1997, section 6-5][law1]; [ATO: staking rewards and airdrops][rewards].
- **Airdrop classification** — An airdrop is not automatically ordinary income. Establish whether it was received in a crypto trading business, for goods or services, through another income-producing activity, or as a hobby receipt, gift or windfall. Current ATO guidance distinguishes these circumstances. A non-income receipt can still be a separate CGT asset whose later disposal must be considered. Establish its acquisition cost base under the applicable rules, including section 112-20's conditions and exceptions; lack of a price feed does not prove nil value. [ATO rewards guidance, updated 19 August 2026][rewards]; [ITAA 1997, section 112-20][law3].
- **TR 2026/D1 — draft only** — This is the Commissioner's preliminary view on airdrops for Australian resident taxpayers. It excludes paid crypto acquisitions, liquidity rewards, non-arm's-length airdrops and rebasing tokens; it does not address GST. Its proposed retrospective application has an exception: initial-allocation airdrops (first distribution before any trading) would be covered only after the final ruling's issue date. Do not apply a draft as final law. Hold an unresolved excluded receipt, valuation or GST outcome: Check this point with one of our partner accountants. [TR 2026/D1, paragraphs 1, 7, 9, 20 and 66][airdraft]; [ATO development status][status].

## DeFi, wrapping and NFTs

- **DeFi mechanics** — Read protocol terms and actual operation. Liquidity deposits, replacement tokens, lending, borrowing, wrapping and unwrapping may change or end rights despite unchanged economic exposure. Record assets and rights before and after; A1, C2, E2 or H2 may be relevant, depending on the arrangement. Choose the applicable statutory event, not all four: section 102-25 governs priority and H2 is residual. Do not finalise an unresolved ownership, trust or event-specific calculation: Check this point with one of our partner accountants. [ATO: decentralised finance and wrapping crypto][defi]; [ITAA 1997, sections 102-25, 104-10, 104-25, 104-60 and 104-155][law3].
- **TD 2026/D2 — draft only** — The specified smart-contract wrapping/unwrapping proposal uses C2 treatment; it is not a rule for every bridge or custodial transfer. It excludes custodial counterparties, transactions in the ordinary course of business and isolated commercial profit-making transactions. Its proposed date of effect is before and after final issue; that proposal is not finalisation. Preserve the arrangement and interpretation used. For an unresolved wrapping outcome: Check this point with one of our partner accountants. [TD 2026/D2, paragraphs 3, 5, 9, 17 and 22][wrapdraft]; [ATO development status][status].
- **NFT treatment** — Examine what the token represents and the rights actually acquired, purpose and use. Business receipts, investment disposals, personal-use assets and collectables need separate analysis. The NFT label alone does not establish collectable status or determine the result. [ATO: non-fungible tokens][nft]; [ITAA 1997, sections 108-10 and 108-20][law3].

## Personal use and missing assets

- **Personal-use exemption** — Under section 108-20, the relevant CGT asset (other than a collectable) must be used or kept mainly for personal use or enjoyment of the taxpayer or an associate. Section 118-10(3) disregards a gain where the first cost-base element (or first cost element for a depreciating asset) is **AUD $10,000 or less**, including exactly $10,000. This tests acquisition cost, not disposal proceeds; spending an investment on personal goods does not automatically convert it into a personal-use asset. Personal-use capital losses are disregarded regardless of this gain threshold. The statute's inclusive boundary controls over the crypto summary's “less than” wording. [ITAA 1997, sections 108-20 and 118-10(3)][law3]; [ATO: personal-use crypto][personal].
- **Lost access, theft and administration** — Obtain ownership, loss and recoverability evidence and identify the asset or enforceable right still held. C1 applies to an asset actually lost/destroyed: timing is first compensation, or discovery of loss / occurrence of destruction if there is no compensation. C2 requires the relevant intangible asset/right to end. A suspended withdrawal or administration announcement alone does not establish a deductible loss; determine the event, timing, compensation/distributions and reduced cost base. Hold an unresolved event or amount: Check this point with one of our partner accountants. Keep it on the reconciliation exceptions list and resolve it before finalising the return; this is not permission to omit taxable transactions. [ITAA 1997, sections 104-20 and 104-25][law3]; [ATO: lost/theft evidence][lost]; [ATO: platforms under administration][administration].

## Worked reconciliation and investment case

Illustration only, in AUD: an Australian individual resident throughout ownership holds 10 investment tokens bought on 1 June 2024 for $100 each. On 15 May 2026 the individual receives 2 ordinary staking-reward tokens worth $100 each, and on 1 June 2026 sells 3 specifically identified original tokens for $450. No fees, adjustments, other gains/losses, excluded-event or special-residency rules apply. The reward tokens remain held. Closing units are 9; ordinary reward income and reward-token basis are $200. The sale gain is $150 and the eligible 50% discounted net capital gain is $75; total assessable crypto amounts are $275, not the tax payable. [ATO reward rules][rewards]; [ITAA 1997, sections 104-10, 110-25 and Division 115][law3]; [pre-reform section 102-5][oldlaw3].

```oa-check
name: 2026 investment parcel and unsold staking receipts
inputs:
  opening_units: 10
  reward_units: 2
  reward_unit_value: 100
  sold_original_units: 3
  original_unit_cost: 100
  proceeds: 450
  discount_rate: 0.5
steps:
  - closing_units: opening_units + reward_units - sold_original_units
  - ordinary_income: reward_units * reward_unit_value
  - reward_basis: reward_units * reward_unit_value
  - disposed_basis: sold_original_units * original_unit_cost
  - gross_gain: proceeds - disposed_basis
  - net_capital_gain: gross_gain * (1 - discount_rate)
  - assessable_crypto: ordinary_income + net_capital_gain
expected:
  closing_units: 9
  ordinary_income: 200
  reward_basis: 200
  disposed_basis: 300
  gross_gain: 150
  net_capital_gain: 75
  assessable_crypto: 275
```

### Illustration: exact personal-use boundary

Assume two separate qualifying personal-use crypto assets (not collectables or revenue assets), each with a first cost-base element of $10,000 and no other cost adjustments. One is sold for $12,000; its $2,000 gain is disregarded because exactly $10,000 passes the statutory amount test. The other is sold for $8,000; its $2,000 personal-use loss is disregarded, so it cannot reduce other capital gains. Qualifying use is stipulated, not established merely by spending the proceeds privately. [ITAA 1997, sections 108-20 and 118-10(3)][law3].

```oa-check
name: Personal-use assets at the inclusive AUD 10000 boundary
inputs:
  first_element: 10000
  gain_asset_proceeds: 12000
  loss_asset_proceeds: 8000
steps:
  - gain: gain_asset_proceeds - first_element
  - disregarded_gain: gain
  - taxable_gain: gain - disregarded_gain
  - loss: first_element - loss_asset_proceeds
  - disregarded_loss: loss
  - available_loss: loss - disregarded_loss
expected:
  gain: 2000
  disregarded_gain: 2000
  taxable_gain: 0
  loss: 2000
  disregarded_loss: 2000
  available_loss: 0
```

> Contributed by Ryan Duguid.

## Sources

Official passages read below; prior completed Australian evidence reused for unchanged rules. Direct ATO requests returned 403; the relevant substantive indexed official texts were read, not the access-denial pages. Drafts prove only their stated proposals/status. No personal tax outcome is inferred from the illustration.

| Source | Passages read / applicability | Date read |
|---|---|---|
| [ITAA 1997 volume 1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | Sections 6-5, 8-1: income/derivation and deduction exclusions | 2026-11-27 |
| [ITAA 1997 volume 3](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) | Trading stock, CGT events/priority, bases, substitution, personal use, discounts; unchanged completed CGT evidence reused; prospective reform application checked separately | 2026-11-27 |
| [ITAA 1997 pre-application text](https://www.legislation.gov.au/C2004A05138/2026-06-27/2026-06-27/text/original/pdf/3) | Sections 102-5, 102-10, 102-15: original loss/discount order; completed Australian CGT read reused | 2026-11-27 |
| [2026 reform Act](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/1/epub/OEBPS/document_1/document_1.html) | Schedule 1 item 82 and existing-holding transition: completed Australian CGT read reused | 2026-11-27 |
| [ATO crypto assets used in business](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-assets-used-in-business) | Trading stock/investment, business indicators, services receipts | 2026-11-27 |
| [TR 97/11](https://www.ato.gov.au/law/view/document?DocID=TXR%2FTR9711%2FNAT%2FATO%2F00001&PiT=99991231235958) | Paragraphs 11–16: indicators considered together, general applicability | 2026-11-27 |
| [TR 92/3](https://www.ato.gov.au/law/view/document?DocID=TXR%2FTR923%2FNAT%2FATO%2F00001&PiT=99991231235958) | Paragraphs 6–7, 35–37: commercial profit-making versus mere realisation | 2026-11-27 |
| [ATO keeping crypto records](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records) | Transaction records, separate assets and reconstructing records | 2026-11-27 |
| [ATO crypto investments and tax](https://www.ato.gov.au/other-languages/information-in-other-languages/investing/crypto-asset-investments-and-tax) | Own-wallet transfers and crypto fee disposals | 2026-11-27 |
| [ATO crypto-to-crypto exchange or swap](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-to-crypto-exchange-or-swap) | Disposal/acquisition and AUD valuation | 2026-11-27 |
| [ATO CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount) | Holding-period day exclusions; completed Australian CGT read reused | 2026-11-27 |
| [ATO staking rewards and airdrops](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops) | Receipt income/basis, non-income receipts, later CGT, valuation; page update 19 August 2026 | 2026-11-27 |
| [TR 2026/D1](https://www.ato.gov.au/law/view/document?docid=DTR/TR2026D1/NAT/ATO/00001) | Draft status; paragraphs 1, 7, 9, 16–21, 66, 85–87 | 2026-11-27 |
| [TD 2026/D2](https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D2/NAT/ATO/00001) | Draft status; paragraphs 3, 5, 9–19, 22; no final-law conclusion | 2026-11-27 |
| [ATO advice under development](https://www.ato.gov.au/about-ato/ato-advice-and-guidance/advice-under-development-program/advice-under-development-capital-gains-tax-and-trust-specific-issues?anchor=BK_3965) | Airdrop and wrapping entries: final completion to be advised | 2026-11-27 |
| [ATO decentralised finance and wrapping crypto](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto) | Rights, protocol terms/operation and candidate CGT events | 2026-11-27 |
| [ATO non-fungible tokens](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/non-fungible-tokens) | Circumstances, use, purpose and rights; no automatic collectable status | 2026-11-27 |
| [ATO personal-use crypto](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-asset-as-a-personal-use-asset) | Completed 21 November reading reused for use/purpose; strict less-than threshold overridden by statute | 2026-11-21 |
| [ATO loss or theft of crypto assets](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/loss-or-theft-of-crypto-assets) | Ownership/loss evidence and recoverability | 2026-11-27 |
| [ATO platforms under administration](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-exchanges-and-platforms-under-administration) | Actual CGT event required; administration/distributions not automatic loss | 2026-11-27 |

Not yet confirmed: taxpayer-specific excluded airdrop/GST, DeFi/wrapping, later-event reform/transitional, valuation and lost-asset outcomes are non-usable holds above until resolved; draft proposals are not final law.

[law1]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[law3]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[oldlaw3]: https://www.legislation.gov.au/C2004A05138/2026-06-27/2026-06-27/text/original/pdf/3
[reform]: https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/1/epub/OEBPS/document_1/document_1.html
[business]: https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-assets-used-in-business
[indicators]: https://www.ato.gov.au/law/view/document?DocID=TXR%2FTR9711%2FNAT%2FATO%2F00001&PiT=99991231235958
[isolated]: https://www.ato.gov.au/law/view/document?DocID=TXR%2FTR923%2FNAT%2FATO%2F00001&PiT=99991231235958
[records]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records
[transfers]: https://www.ato.gov.au/other-languages/information-in-other-languages/investing/crypto-asset-investments-and-tax
[swap]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-to-crypto-exchange-or-swap
[discount]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount
[rewards]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops
[airdraft]: https://www.ato.gov.au/law/view/document?docid=DTR/TR2026D1/NAT/ATO/00001
[wrapdraft]: https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D2/NAT/ATO/00001
[status]: https://www.ato.gov.au/about-ato/ato-advice-and-guidance/advice-under-development-program/advice-under-development-capital-gains-tax-and-trust-specific-issues?anchor=BK_3965
[defi]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto
[nft]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/non-fungible-tokens
[personal]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-asset-as-a-personal-use-asset
[lost]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/loss-or-theft-of-crypto-assets
[administration]: https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-exchanges-and-platforms-under-administration
