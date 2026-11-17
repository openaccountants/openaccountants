---
name: south-korea-crypto-tax
description: >
  South Korea virtual asset tax reference for calendar 2026, distinguishing current
  gift, inheritance and overseas account obligations from the promulgated income
  regime scheduled for 1 January 2027. Use for Bitcoin, crypto tax, Upbit, Bithumb,
  가상자산 과세, basis, exchanges, lending, gifts, overseas accounts, staking,
  mining, DeFi and NFTs. Identify the taxpayer, activity and year before computing;
  refer unresolved reward, token and cross-border classifications. Produces a tax
  working paper, not regulatory compliance advice or complete coverage of every
  digital asset activity.
version: 1.1
jurisdiction: KR
tax_year: 2026
tax_year_notes: "Calendar 2026; separately labelled promulgated 2027 regime"
last_updated: 2026-11-16
depends_on:
  - kr-income-tax
category: crypto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
---

# South Korea Crypto Tax v1.1

> **General reference only.** This guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

The separate income category for an individual's virtual asset transfers and lending has **not commenced for calendar 2026**. The promulgated commencement is **1 January 2027**. Recheck the enacted law before using the future-year scenarios: a proposal or statement about readiness does not change commencement. The deferral does not defer gift tax, inheritance tax, overseas-account reporting or tax on another income category merely because payment is in tokens. [Income Tax Act arts. 21(1)(27), 37; Act 17757 addenda art. 1 item 2 and art. 5(1)-(2), as amended; Act 20615 addenda art. 1(2)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701).

This reference addresses Korean resident individuals' ordinary holdings and identifies separate gift and overseas-reporting work. Stop for uncertain residence, nonresident or corporate ownership, employment/service remuneration, commercial activities or securities rights. The resident individual's future deduction/rate cannot be copied to a company. The corporate-versus-individual comparison is a scope distinction, not a company exemption. [Income Tax Act arts. 1-3, 19-21](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701).

### Quick reference and required inputs

| Item | Answer and conditions | Official source |
| --- | --- | --- |
| Period and currency | Calendar 2026; KRW working papers. Preserve original currency, dates and conversion evidence. | [Income Tax Act arts. 5, 24](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Scheduled individual regime | Transfers/lending from 1 January 2027; other income under separate taxation. | [Income Tax Act arts. 14(3)(8)(da), 21(1)(27); Act 17757 addenda](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Combined scheduled rate (computed) | 22%; the separate statutory rates and annual deduction are in the table below. | [Income Tax Act art. 64-3(2)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202); [Local Tax Act art. 93(18)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&efYd=20260701&chrClsCd=010202) |
| Future acquisition valuation | Total average per resident, replacing the old exchange moving-average/P2P FIFO split. | [Promulgated Income Tax Decree arts. 88(1), 92(2)(4)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280865&efYd=20260102&chrClsCd=010202) |
| Existing holdings | Higher of actual cost and statutory 31 December 2026 market value; prescribed price observation at 00:00 on 1 January 2027. | [Income Tax Act art. 37(5)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202); [Decree art. 88(2)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280865&efYd=20260102&chrClsCd=010202) |
| Overseas-account trigger now | Aggregate overseas financial accounts, including overseas crypto-provider accounts: more than KRW 500,000,000 on any **month-end**, subject to filer exemptions. An intramonth peak alone is insufficient. | [NTS overseas accounts, International Tax Coordination Act arts. 52-57](https://s.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7819&mi=2513) |

The combined rate is arithmetic: national 20% + local 2% = 22% on the same positive annual amount after the deduction. The two statutory rates, deduction and their conditions remain separately stated and sourced below.

Obtain ownership/residence, year/activity, full transactions and balances, cost/fee evidence, gift history/relationship and overseas month ends before computing. Do not fill missing inputs with an assumed basis method, FMV or reward classification.

## Rates, bands and thresholds

### Scheduled individual virtual asset income from 2027

| Item | Amount and condition | Official source |
| --- | --- | --- |
| Annual deduction / non-taxation threshold | KRW 2,500,000 per resident per year, not per asset, wallet or exchange. Annual virtual asset income at or below this amount is not charged. | [Income Tax Act arts. 64-3(2), 84(3)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| National rate | 20% on annual virtual asset income less the deduction. | [Income Tax Act art. 64-3(2)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Local rate | 2% on that same net amount, with a separate local filing/payment obligation. | [Local Tax Act arts. 93(18), 95](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&efYd=20260701&chrClsCd=010202) |
| Missing-cost alternative | 50% of all same-type asset disposal proceeds only for qualifying verification difficulty on assets acquired from 1 January 2027; no extra incidental costs. | [Income Tax Act art. 37(6)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202); [Decree art. 88(4)-(5)](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280865&efYd=20260102&chrClsCd=010202) |

### Gift tax already applies

Gift tax is not limited to gifts between relatives. Recipient residence and the gift's territorial facts control; relationship affects allowances. [Inheritance and Gift Tax Act arts. 2, 4, 4-2](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=276123&efYd=20260102).

| Taxable gift base, KRW | Rate | Progressive deduction, KRW | Official source |
| --- | --- | --- | --- |
| Up to 100,000,000 | 10% | 0 | [Inheritance and Gift Tax Act arts. 26, 56; NTS table](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7728&mi=2338) |
| Over 100,000,000 to 500,000,000 | 20% | 10,000,000 | [Same](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7728&mi=2338) |
| Over 500,000,000 to 1,000,000,000 | 30% | 60,000,000 | [Same](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7728&mi=2338) |
| Over 1,000,000,000 to 3,000,000,000 | 40% | 160,000,000 | [Same](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7728&mi=2338) |
| Over 3,000,000,000 | 50% | 460,000,000 | [Same](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7728&mi=2338) |

| Donor relationship to resident recipient | Ordinary allowance over the statutory preceding 10-year aggregation period | Official source |
| --- | --- | --- |
| Spouse | KRW 600,000,000 | [Inheritance and Gift Tax Act art. 53(1)](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017648003) |
| Lineal ascendant | KRW 50,000,000; KRW 20,000,000 where recipient is a minor | [Art. 53(2)](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017648003) |
| Lineal descendant | KRW 50,000,000 | [Art. 53(3)](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017648003) |
| Other qualifying relative | KRW 10,000,000; blood relatives within fourth degree and relatives by marriage within third degree | [Art. 53(4)](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017648003) |

**Warning about superseded gift allowances:** The earlier spouse allowance of KRW 50,000,000 was wrong: the ordinary allowance for a resident recipient is KRW 600,000,000 over the statutory preceding 10-year aggregation period, not a lifetime allowance. The earlier KRW 20,000,000 allowance for other relatives was also wrong: their ordinary allowance is KRW 10,000,000, limited to blood relatives within the fourth degree and relatives by marriage within the third degree. KRW 20,000,000 instead applies where a minor recipient receives a gift from a lineal ascendant; the ordinary adult ascendant-gift allowance is KRW 50,000,000. These amounts remain subject to the prior-deduction aggregation conditions, not an automatic allowance for every gift. [Inheritance and Gift Tax Act art. 53](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017648003).

Check earlier gifts and deduction use. Article 47(2) aggregates qualifying earlier gifts from the same donor, including the donor's spouse where the donor is a lineal ascendant. Article 53-2's separate marriage/childbirth relief is conditional; obtain event/prior-use facts before applying it. The example assumes no additional relief. [Inheritance and Gift Tax Act arts. 47, 53, 53-2](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=276123&efYd=20260102).

### Progressive income rates: classification handoff

These national comprehensive-income rates are in the operative 2026 Income Tax Act. They do not establish that mining, staking, airdrops or NFT creation belong in a particular income category. Local comprehensive-income tax is computed separately under Local Tax Act arts. 91-93; do not assume every final liability/credit is a national-tax surcharge.

| Comprehensive taxable base, KRW | Statutory national marginal rate | Official source |
| --- | --- | --- |
| Up to 14,000,000 | 6% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Over 14,000,000 to 50,000,000 | 15% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Over 50,000,000 to 88,000,000 | 24% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Over 88,000,000 to 150,000,000 | 35% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Over 150,000,000 to 300,000,000 | 38% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Over 300,000,000 to 500,000,000 | 40% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Over 500,000,000 to 1,000,000,000 | 42% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Over 1,000,000,000 | 45% | [Income Tax Act art. 55(1), article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |

The following cumulative bases and quick deductions are computed arithmetic from the statutory boundaries and marginal rates in the preceding table. They are not additional statutory deductions or different rates. Starting with cumulative tax A = 0 at lower boundary L = 0, each next cumulative base is the previous A plus the width of the completed band multiplied by that band's marginal rate. For taxable base x within a band, national tax is A + (x − L) × r. Rewriting this as x × r − (L × r − A) gives the equivalent quick deduction L × r − A.

| Band in preceding statutory table | Cumulative tax A, KRW | Equivalent quick deduction, KRW | Derivation inputs |
| --- | --- | --- | --- |
| First (computed) | 0 | 0 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Second (computed) | 840,000 | 1,260,000 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Third (computed) | 6,240,000 | 5,760,000 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Fourth (computed) | 15,360,000 | 15,440,000 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Fifth (computed) | 37,060,000 | 19,940,000 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Sixth (computed) | 94,060,000 | 25,940,000 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Seventh (computed) | 174,060,000 | 35,940,000 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |
| Eighth (computed) | 384,060,000 | 65,940,000 | [Statutory boundaries and rates above](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) |

The calculations preserve each original quick-deduction equation and show how its cumulative input is obtained:

- First: cumulative base 0; quick deduction 0.
- Second: cumulative base 0 + (14,000,000 − 0) × 6% = 840,000; quick deduction 14,000,000 × 15% − 840,000 = 1,260,000.
- Third: cumulative base 840,000 + (50,000,000 − 14,000,000) × 15% = 6,240,000; quick deduction 50,000,000 × 24% − 6,240,000 = 5,760,000.
- Fourth: cumulative base 6,240,000 + (88,000,000 − 50,000,000) × 24% = 15,360,000; quick deduction 88,000,000 × 35% − 15,360,000 = 15,440,000.
- Fifth: cumulative base 15,360,000 + (150,000,000 − 88,000,000) × 35% = 37,060,000; quick deduction 150,000,000 × 38% − 37,060,000 = 19,940,000.
- Sixth: cumulative base 37,060,000 + (300,000,000 − 150,000,000) × 38% = 94,060,000; quick deduction 300,000,000 × 40% − 94,060,000 = 25,940,000.
- Seventh: cumulative base 94,060,000 + (500,000,000 − 300,000,000) × 40% = 174,060,000; quick deduction 500,000,000 × 42% − 174,060,000 = 35,940,000.
- Eighth: cumulative base 174,060,000 + (1,000,000,000 − 500,000,000) × 42% = 384,060,000; quick deduction 1,000,000,000 × 45% − 384,060,000 = 65,940,000.

The [same-edition statutory article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) supplies the boundaries and marginal rates. The [official table image](https://www.law.go.kr/LSW/flDownload.do?flSeq=123278409) is additional read evidence for the cumulative amounts, including the final cumulative base absent from the HTML alternative text. The statutory band/rate rows above remain separate from these computed outputs.

## The base

### Scheduled transfer/lending method

1. Identify an asset within the definition imported by Income Tax Act art. 21(1)(27) from Virtual Asset User Protection Act art. 2(1). Exclusions cover specified nonexchangeable limited-use tokens, game results, prepaid payment means/e-money, electronically registered shares, electronic bills, electronic bills of lading, central-bank electronic currency and prescribed exclusions. An exchange label is not the legal classification. [NTS definition section](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=238935&mi=40370).
2. Build the ledger across providers and wallets. Match own-wallet movements without double-counting acquisitions/disposals; establish unchanged beneficial ownership. Another person's wallet, a loan or a pool transaction needs separate classification. The statutory category is income from transfer/lending, not every blockchain movement. [Income Tax Act art. 21(1)(27)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701).
3. Identify fiat sales, exchanges and lending consideration. For crypto exchanges, apply the base asset's value and exchange ratio: simultaneous fiat exchange value for a designated-provider base asset, or statutory basic/arbitrated FX rate for a foreign-currency-linked base asset. Payment for goods/services needs a transfer-for-consideration analysis and separate classification of the underlying receipt. [Decree art. 88(3)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280865&efYd=20260102).
4. Deduct acquisition cost and evidenced incidental acquisition, transfer or lending costs. Use **total average per resident** under the promulgated Decree, with art. 92's total-average definition. The old exchange moving-average versus P2P/DeFi/OTC FIFO split and its consistency instruction are superseded. Do not reset the cost pool at each exchange. [Income Tax Act art. 37(1)(3)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701); [Decree arts. 88(1), 92](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280865&efYd=20260102).
5. For pre-commencement holdings, use the higher actual cost/statutory transitional market value. For designated-provider assets, average the designated providers' published prices at 00:00 on 1 January 2027; otherwise use the prescribed other provider's published price at that time. An arbitrary exchange closing price does not automatically qualify. [Income Tax Act art. 37(5)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701); [Decree art. 88(2)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280865&efYd=20260102).
6. For unverifiable actual cost of assets acquired from 1 January 2027, test the statutory alternative. Decree art. 88(4) covers acquisition outside a provider where books/evidence cannot establish actual cost and other NTS-designated cases. Paragraph (5) prescribes 50% of all same-type disposal proceeds under art. 37(6), without extra incidental expenses. This is not an unrestricted estimate or an addition to actual basis. [Income Tax Act art. 37(6)-(7)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701); [Decree art. 88(4)-(6)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280865&efYd=20260102).
7. Net annual qualifying crypto gains/losses, including different assets; apply the annual deduction once; compute national/local amounts separately. Do not offset a negative separate-income result against salary/business income. The enacted calculation provides no crypto loss carry-forward/carry-back; art. 45's carry-forward concerns qualifying business losses. Retain losses in the annual schedule without inventing a later-year deduction. [Income Tax Act arts. 14, 21(3), 45, 64-3, 84](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701).

Purchase/sale fees meet the statutory incidental-cost test where evidenced. Gas/network costs require a link to acquisition, transfer or lending. The old categorical answers for wallet-transfer fees and hardware-wallet costs are held below. Preserve transaction IDs, quantities, timestamps, exchange exports, addresses, ownership matches, fee invoices, basis calculations and lending contracts. [Income Tax Act arts. 37, 70(4)(2)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701).

### Gift, inheritance and NFT boundaries

Crypto at death requires a separate inheritance calculation. For gift/inheritance assets traded by an NTS-designated provider, valuation averages that provider's **daily average values** during each one-month period before and after the valuation date, not daily closing prices. Other crypto uses reasonably recognized value, including other providers' transaction-day daily average or end-time quote. Establish the provider before applying the two-month window. [Inheritance and Gift Tax Act art. 65(2)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=276123&efYd=20260102); [its Decree art. 60(2)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=290845&efYd=20261001).

The protection Act's [19 July 2024 commencement](https://law.go.kr/lsInfoP.do?efYd=20240719&lsiSeq=252731), discussed in the FSC's 10 June 2024 guidance, is distinct from the income-tax commencement. For NFTs, examine securities rights first, then virtual asset status. Collectible purpose/limited transferability differ from mass issuance, divisibility, payment use or crypto exchangeability. Mere secondary trading does not classify every NFT as crypto. The FSC guidance is regulatory guidance, not a ruling that creators receive business income or collectible art is tax-free. Game NFTs need the actual game-result exclusion. Refer securities, creator/service receipts and uncertain tokens for classification. [FSC guidance sections 1 and 3](https://www.fsc.go.kr/po010101/82418).

## Deadlines and filing

| Obligation | Timing and route | Official source |
| --- | --- | --- |
| Scheduled resident return | Following year's comprehensive-income return period, 1-31 May, as separately taxed other income. First scheduled income year 2027, regular filing period May 2028. Recheck law/form before filing. | [Income Tax Act art. 70(1)-(2); NTS filing section](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=238935&mi=40370) |
| National/local payment | National payment within final return period; local filing/payment is separate, due by the corresponding deadline. | [Income Tax Act art. 76](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202); [Local Tax Act art. 95](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&efYd=20260701&chrClsCd=010202) |
| Ordinary gift return/payment | Within 3 months after the end of the gift month; payment by that filing deadline. | [Inheritance and Gift Tax Act arts. 68, 70](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=276123&efYd=20260102) |
| Overseas-account report | 1-30 June after holding year; Form 45, HomeTax/SonTax or jurisdictional tax office. Thus 2026 holdings are reported in June 2027 if required. | [NTS filing instructions](https://s.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7819&mi=2513) |
| Scheduled provider submissions | Art. 164-4: end of second month following relevant quarter/year; Decree names transaction-detail/aggregate statements. Not a January annual deadline. | [Income Tax Act art. 164-4; Act 20615 addenda arts. 1, 12](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202); [Decree art. 216-4](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280865&efYd=20260102&chrClsCd=010202) |

Prepare annual national/local schedules and support; use [HomeTax](https://www.hometax.go.kr/) for the applicable return and retain submission/payment evidence. This is not a tested 2028 screen-by-screen filing guide. Future form boxes, provider schemas and provisional-payment workflow remain held below. Exchange reporting is not the individual's completed return.

For overseas accounts, prepare Form 45 holder/address, account/provider/country, month-end balances, highest aggregate month-end date and joint/nominee/beneficial-owner details. Enter the appropriate year, retain valuation work and submission confirmation. The tax office can receive a report if electronic access is unavailable. [NTS Form 45 instructions](https://s.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7819&mi=2513).

## Penalties and interest

Current NTS overseas-account guidance states a non/underreporting administrative fine of **10% of the omitted amount, capped at KRW 1 billion**, correcting the old blanket “up to 20%”. Failure to explain source of funds can attract an additional 10% fine. Omissions over KRW 5 billion can trigger disclosure/criminal sanctions, including up to two years' imprisonment or a fine of 13-20% of the omission; these differ from the ordinary administrative fine. Correction/late filing before fine imposition can reduce the administrative fine according to timing. [NTS sanctions/corrections, International Tax Coordination Act arts. 56, 90](https://s.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7819&mi=2513).

The income-category deferral gives no immunity for gift omissions, other taxable receipts, false evidence or overseas-reporting failures. Exact income/gift late-filing, underreporting, interest and limitation calculations are not supplied: obtain the tax, conduct, dates and applicable provision before computing. The old universal ten-year assessment assertion is held below.

## Cross-border points

Aggregate all relevant overseas financial accounts, not one exchange or just gains. NTS exemptions include qualifying short-term foreign residents (not more than five years' domestic residence/domicile in the preceding ten years), qualifying overseas Korean nationals, specified institutions, accounts fully disclosed by another related filer, qualifying overseas-trust disclosures and treaty-partner residents. Confirm the actual exemption; nationality alone is insufficient. Distinguish an overseas provider account from self-custody: not every wallet is an overseas financial account. [NTS scope/exemptions](https://s.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7819&mi=2513).

For nonresident/foreign-corporate cases, do not reuse resident deductions: identify source, transfer/lending/withdrawal, provider withholding and treaty status through the separate [NTS nonresident overview](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=238936&mi=40371). CARF exchange/self-certification needs operative authority; an anticipated exchange year gives no filing exemption or enforcement safe harbour. Unsupported Korea/US timing claims are held in Sources.

## Two worked examples that recompute

### Example 1: original BTC trading case, scheduled 2027 regime

Korean resident buys **1 BTC on Upbit for KRW 40,000,000 in February 2027**, sells for **KRW 55,000,000 in August 2027**, and pays **KRW 150,000 total evidenced purchase/sale fees**. Assume the only holding/transaction pool, with no other income/losses. Total-average cost equals the single purchase; this does not endorse moving-average treatment. Expenses KRW 40,150,000; gain KRW 14,850,000; taxable amount KRW 12,350,000; national KRW 2,470,000 plus local KRW 247,000 = **KRW 2,717,000**. Scheduled filing: May 2028. [Income Tax Act arts. 37, 64-3, 70](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701); [Local Tax Act art. 93(18)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=282559&efYd=20260701).

```oa-check
name: Original BTC case under scheduled 2027 regime
inputs:
  btc: 1
  purchase_per_btc: 40000000
  sale_per_btc: 55000000
  fees: 150000
  deduction: 2500000
steps:
  - expenses: btc * purchase_per_btc + fees
  - gain: btc * sale_per_btc - expenses
  - taxable: max(0, gain - deduction)
  - national: taxable * 0.20
  - local: taxable * 0.02
  - total: national + local
expected:
  expenses: 40150000
  gain: 14850000
  taxable: 12350000
  national: 2470000
  local: 247000
  total: 2717000
```

### Example 2: original ETH transitional case

Korean resident bought **10 ETH at KRW 500,000 each in 2021**, actual **KRW 5,000,000**. Original case's **31 December 2026 price KRW 4,000,000 per ETH**, total **KRW 40,000,000**, is assumed to satisfy the prescribed midnight-price rule. All **10 ETH sell at KRW 5,000,000 each in March 2027**, proceeds **KRW 50,000,000**; no other transactions/fees. Deemed cost KRW 40,000,000; gain KRW 10,000,000; taxable KRW 7,500,000; combined tax **KRW 1,650,000**. Basis substitution excludes **KRW 35,000,000** of pre-commencement appreciation from measured gain. [Income Tax Act art. 37(5)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701); [Decree art. 88(2)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280865&efYd=20260102).

```oa-check
name: Original 10 ETH transitional cost case
inputs:
  eth: 10
  actual_unit_cost: 500000
  statutory_unit_value: 4000000
  sale_unit_value: 5000000
  deduction: 2500000
steps:
  - actual: eth * actual_unit_cost
  - statutory: eth * statutory_unit_value
  - deemed: max(actual, statutory)
  - proceeds: eth * sale_unit_value
  - gain: proceeds - deemed
  - taxable: max(0, gain - deduction)
  - tax: taxable * 0.22
  - basis_uplift: deemed - actual
expected:
  actual: 5000000
  statutory: 40000000
  deemed: 40000000
  proceeds: 50000000
  gain: 10000000
  taxable: 7500000
  tax: 1650000
  basis_uplift: 35000000
```

### Example 3: original 2025 gift case, current ordinary rules distinguished

Parent gives **2 BTC to adult child**, supplied statutory two-month-window average **KRW 50,000,000 each**, gift **KRW 100,000,000**. Preserve original **2025** date as historical; these ordinary allowance/rate rules were read for 2026. Assume resident recipient, designated-provider valuation, no earlier gifts/deduction use, no marriage/childbirth relief, debt or generation-skipping surcharge. Allowance **KRW 50,000,000** leaves taxable **KRW 50,000,000**, **gross gift tax KRW 5,000,000**. Correct timely filing, with no other adjustments, permits a 3% filing credit, payment **KRW 4,850,000**. This obligation is separate from deferred income tax. [Inheritance and Gift Tax Act arts. 26, 53, 56, 68-70](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=276123&efYd=20260102).

```oa-check
name: Original parent to adult child BTC gift with filing credit distinguished
inputs:
  btc: 2
  statutory_price: 50000000
  ordinary_allowance: 50000000
steps:
  - gift: btc * statutory_price
  - taxable: max(0, gift - ordinary_allowance)
  - gross_tax: taxable * 0.10
  - filing_credit: gross_tax * 0.03
  - payment: gross_tax - filing_credit
expected:
  gift: 100000000
  taxable: 50000000
  gross_tax: 5000000
  filing_credit: 150000
  payment: 4850000
```

### Preserved loss illustration

Original **KRW 4,400,000 loss in 2027 / KRW 4,400,000 gain in 2028**: under the enacted scheduled calculation, the loss is not carried forward. Next year's taxable **KRW 1,900,000**, after deduction, produces **KRW 418,000**. Recheck future law before use. [Income Tax Act arts. 45, 64-3](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701).

```oa-check
name: Original two-year loss and gain illustration
inputs:
  first_year_loss: 4400000
  second_year_gain: 4400000
  deduction: 2500000
steps:
  - first_year_tax: max(0, 0 - first_year_loss - deduction) * 0.22
  - second_year_taxable: max(0, second_year_gain - deduction)
  - second_year_tax: second_year_taxable * 0.22
expected:
  first_year_tax: 0
  second_year_taxable: 1900000
  second_year_tax: 418000
```

## Ask the client first

- Who owns the assets beneficially; what are residence history, treaty residence and entity type?
- Which calendar year and activity: sale, exchange, loan, work payment, reward, gift or inheritance?
- What are all quantities, dates, consideration, fees, counterparties, providers, wallets and KRW/FX evidence?
- Which holdings predate commencement; what proves statutory transitional price and total-average pool?
- For gifts, what are relationship, recipient age, earlier gifts/allowance use and marriage/childbirth facts?
- What are all overseas month-end accounts/balances, ownership details and reporting exemptions?

Before completion: reconcile opening/acquired/disposed/closing quantities, match own-wallet transfers, recompute the resident pool, distinguish current and scheduled obligations, net annually, apply one deduction, retain gift valuation/history, test overseas month ends, and supply the reviewer national/local schedules and unresolved classifications. Never treat missing inputs as zero, speculative DeFi treatments as law, a loss as a future deduction or a CARF gap as immunity. Do not certify regulatory compliance from this tax guide.

## Sources

| Official source | Exact scope actually read | Read date |
| --- | --- | --- |
| [Income Tax Act, July 2026 consolidation, Act 21221](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280405&efYd=20260701); [actual article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&efYd=20260701&chrClsCd=010202) | Read for this guide: arts. 1-5, 14, 19-21, 24, 37, 45, 55 table ([actual statutory image](https://www.law.go.kr/LSW/flDownload.do?flSeq=123278409)), 64-3, 70, 76, 84, 164-4; Act 17757 addenda arts. 1, 2 and 5 and Act 20615 addenda arts. 1, 6, 12. Future provisions and commencement distinguished from present operation. | 2026-11-16 |
| [Income Tax Decree, promulgated consolidation including future provisions](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=280865&efYd=20260102); [actual article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280865&efYd=20260102&chrClsCd=010202) | Read for this guide: future arts. 88(1)-(6), 92(2), 216-4; total average, exchange value, transitional price, missing-cost conditions and 50% ratio. | 2026-11-16 |
| [Income Tax Decree, October 2026 operative text](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=290841&efYd=20261001); [actual article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290841&efYd=20261001&chrClsCd=010202) | Read for this guide: current art. 88 remains deleted pending future commencement; Decree 35121 addenda art. 1(3)-(4) preserves promulgated 2027 commencement. Read with future-text row, not applied in 2026. | 2026-11-16 |
| [NTS resident virtual asset overview](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=238935&mi=40370) | Read for this guide: commencement, definition/exclusions, basis, transitional value, exchanges and filing sections. Residual reference to 2024 missing-cost proposal supplemented with promulgated Decree, not treated as law itself. | 2026-11-16 |
| [Local Tax Act, July 2026](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=282559&efYd=20260701); [actual article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&efYd=20260701&chrClsCd=010202) | Read for this guide: arts. 91-95, especially 93(18)'s formula and 95's separate filing/payment. | 2026-11-16 |
| [Inheritance and Gift Tax Act, 2026](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=276123&efYd=20260102); [actual article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276123&efYd=20260102&chrClsCd=010202) | Read for this guide: arts. 2-4-2, 26 table, 47, 53, 53-2, 56-57, 65, 68-70; scope, rates, aggregation, valuation, filing/credit. | 2026-11-16 |
| [Article 53 and neighbours](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017648003) | Read for this guide: complete arts. 53 and 53-2: ordinary 10-year allowances/relationships and conditional marriage/childbirth relief. | 2026-11-16 |
| [Inheritance and Gift Tax Decree, October 2026](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=290845&efYd=20261001); [actual article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290845&efYd=20261001&chrClsCd=010202) | Read for this guide: art. 60(2), designated-provider daily-average window and other-asset valuation. | 2026-11-16 |
| [NTS gift computation](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7728&mi=2338) | Read for this guide: ordinary gift computation, rate bands/deductions and earlier gifts, excluding exceptional share schemes. | 2026-11-16 |
| [NTS overseas accounts](https://s.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7819&mi=2513) | Read for this guide: current scope/exemptions, month-end trigger, Form 45, filing, sanctions/corrections; obsolete commented-out fine table excluded. | 2026-11-16 |
| [NTS nonresident overview](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=238936&mi=40371) | Read for this guide: body overview of domestic-source transfer/lending/withdrawal, provider withholding and treaty application; referral only, no nonresident computation supplied. | 2026-11-16 |
| [Protection Act, current consolidation](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=290735&efYd=20261002); [actual article body](https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290735&efYd=20261002&chrClsCd=010202) | Read for this guide: original Act 19563 addenda art. 1, commencement one year after promulgation, including the separate 2025 commencement exception for addenda art. 2(6); not a regulatory compliance review. | 2026-11-16 |
| [Protection Act, original enacted version](https://law.go.kr/lsInfoP.do?efYd=20240719&lsiSeq=252731) | Read for this guide by the independent reviewer: original Act 19563 register heading and 19 July 2024 commencement, supplementing the FSC announcement; not a regulatory compliance review. | 2026-11-16 |
| [FSC NFT guidance](https://www.fsc.go.kr/po010101/82418) | Read for this guide: body sections 1 and 3, securities-first/substance classification and collectible/fungibility/payment factors; not a tax ruling. | 2026-11-16 |

**Not yet confirmed:** These old topics are held, not usable default positions. The preservation ledger records original items and destinations.

- Mining: hobby/commercial category, receipt timing, FMV valuation and reward basis. Staking: receipt taxation/basis, staking-as-a-service always being lending and slashing deductibility. Airdrops/forks: zero basis, promotional receipt tax and service-linked classification. No “likely taxable” default is supplied.
- DeFi: protocol lending interest, LP deposit/withdrawal disposal, LP-token basis, yield-farming receipt and impermanent-loss deduction. The statutory transfer/lending category does not settle every protocol's legal substance.
- NFTs: categorical creator/business-income treatment, collectible-art tax exclusion and gaming-token conclusions beyond statutory/FSC classification criteria. Securities/creator/service receipts need separate analysis.
- Fee edges: categorical treatment of own-wallet transfer fees/hardware-wallet costs and allocation of gas/network fees without transaction evidence.
- Provider operations: old January 2028 deadline, five-exchange CARF self-certification from 1 January 2026, future individual form boxes/screens, provider schemas and blanket no-provisional-payments rule. Statutory submission timing is corrected above; operational implementation is not certified.
- CARF/enforcement: alleged Korean receipt of all exchange data in 2027, US accession in 2029, US enforcement gap in 2027-2028, universal ten-year assessment period and NTS hidden-wallet statements. No disclosure decision may rely on them.
- Records: universal five-years-from-filing-deadline rule and blanket burden-of-proof assertion for every taxpayer/activity. Retain the evidence listed above pending the applicable statutory retention/assessment analysis.
- Avoidance: absence of a specific crypto wash-sale rule, application of particular general anti-avoidance rules to a round trip, and claims of active gift-evasion investigations. Establish authority/facts rather than inferring a safe harbour.
- Historical policy: earlier postponement chronology, claimed May 2026 ministerial guarantee against another deferral, five-exchange (Upbit/Dunamu, Bithumb, Coinone, Korbit, Gopax) coordination, stock-market analogy for loss relief and corporate/individual fairness rationale. None establishes a current tax position.

- Currency conversion: the old approximate USD 1,800 equivalent of the KRW 2,500,000 deduction has no dated FX evidence. Use the statutory KRW amount, not that approximate dollar threshold.

This guide remains tier 2 with no accountant approval. A qualified Korean tax professional must review actual classification and filing work before use.
