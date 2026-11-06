---
name: il-crypto-tax
description: "Use this skill when advising on Israeli cryptocurrency tax reporting and capital gains calculations. Trigger on phrases like \"crypto tax Israel\", \"bitcoin tax Israel\", \"מס קריפטו\", \"FIFO Israel\", \"Form 1325 crypto\", \"Form 1322\", \"capital gains crypto Israel\", \"staking tax Israel\", \"airdrop tax Israel\", \"DeFi tax Israel\", \"voluntary disclosure crypto Israel\", \"gilui mirtzon\", \"גילוי מרצון\", or any Israeli cryptocurrency tax query. ALWAYS read this skill before advising on Israeli crypto taxation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-crypto-tax"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-03"
---

# IL Crypto Tax

## Israel Cryptocurrency Tax Reporting Skill v1.1

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1: Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Israel (מדינת ישראל) |
| Scope | Cryptocurrency capital gains tax, DeFi income classification, reporting |
| Currency | NIS (Israeli New Shekel: ₪) |
| Classification | A decentralised payment instrument is an asset (Neches: נכס) under Section 88 ITO, not currency or foreign currency (https://www.gov.il/BlobFolder/policy/income-tax-professional-inst-5-2018/he/Policy_ProfessionalInstIncomeTax_hor_acc%2015.2.18.pdf, ss.2.3, 3.1.1) |
| Primary guidance | ITA Circular 2018/05 (חוזר 05/2018) |
| Cost basis method | unverified: FIFO (First In, First Out) as the default |
| Tax rate: individuals | Capital gain under Part E, at the s.91 rates (Circular 5/2018 s.3.1.2): real capital gain on an asset bought from 1/1/2012 is taxed at up to 25%; older assets are split linearly; lower starting rates from age 60 | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.48) |
| Tax rate: significant shareholder (10%+) | unverified: 30% |
| Tax rate: business/traders | If the activity amounts to a business, ordinary income at the s.121 or s.126 rates; mining is business income (Circular 5/2018 s.3.1.4) |
| Corporate rate | unverified: 23% |
| Surtax above NIS 721,560 | 3% on the part of total taxable income above NIS 721,560, plus 2% on capital-source taxable income above that amount: two bases, not a flat 5% (https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf, p.11) |
| Advance payment form | Form 1399י: virtual currency is marked with transaction symbol 77 and code 71; several sales in one month may be grouped as one with a weighted-average purchase date, with a worksheet attached (https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf, PDF p.47) |
| Advance payment deadline | unverified: within 30 days of disposal |
| Reporting forms | Forms 1322 / 1325 (attached to annual Form 1301) |
| Contributor | Open Accountants Community |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown whether activity is business or investment | Treat as investment (25% capital gains): flag for professional review if high frequency |
| Staking reward classification unclear | Treat as income at receipt (most conservative) |
| Unknown NIS exchange rate for transaction date | Use most recent Bank of Israel business day rate |
| Crypto received as gift | Use donor's carryover basis (Section 97(a)(5)) |
| Stablecoins (USDT, USDC) | Still an "asset": every conversion is a taxable disposal |

## Section 2: Legal framework

### 2.1 Core principles

- **Crypto classification as asset**: Cryptocurrency is classified as an asset (Neches) under Section 88 of the Income Tax Ordinance (Pekudat Mas Hachnasa: פקודת מס הכנסה), NOT as currency  _(Section 88 ITO)_
- **Gains taxed as capital gains**: Gains are taxed as capital gains (Revach Hon) under Chapter E of the Ordinance  _(Chapter E, Income Tax Ordinance)_
- **Primary guidance**: ITA Circular 2018/05 provides primary guidance on crypto taxation  _(ITA Circular 2018/05)_
- **Taxable event on every disposal**: Every disposal (sale, trade, conversion) is a taxable event valued in NIS
- **Crypto-to-crypto swaps taxable**: Crypto-to-crypto swaps are taxable events: unlike some jurisdictions, Israel has always treated these as disposals

### 2.2 Business vs investment classification

- **Business classification consequence**: If crypto activity constitutes a business (Esek: עסק), gains are taxed as ordinary income at marginal rates (up to 50%)
- **Classification factors**: Classification depends on: Frequency and volume of trading; Whether taxpayer holds crypto as inventory vs investment; Time and effort devoted to crypto activity; Whether the taxpayer has another profession
- **Default when in doubt**: When in doubt, treat as investment (25%) but flag for professional review

## Section 3: FIFO cost basis method

unverified: Israel mandates FIFO (First In, First Out) for calculating cost basis unless the taxpayer can demonstrate a different method was consistently applied. Circular 5/2018 does not set a cost-basis method.

### 3.1 FIFO rules

- **FIFO calculation steps**: 1. Queue all purchases by date (oldest first) 2. For each sale, match against the oldest available purchase lots 3. Calculate gain/loss for each matched lot: (sale price − purchase price − fees) per unit 4. If a lot is partially consumed, the remainder stays in the queue 5. Sum all gains and losses for the tax year

### 3.2 Currency conversion

- **NIS conversion at BOI exchange rate**: All transactions must be converted to NIS at the Bank of Israel exchange rate (Sha'ar Yatzig: שער יציג) on the transaction date
- **Crypto-to-crypto NIS valuation**: For crypto-to-crypto trades, the NIS value of BOTH sides must be determined at the time of trade
- **Weekend/holiday rate fallback**: For weekends/holidays when BOI doesn't publish rates, use the most recent business day rate

## Section 4: DeFi and special income classification

**DeFi and special income classification table**

unverified: every row except the first two. Circular 5/2018 covers sale (capital gain), business activity, mining (business income) and payment in crypto (barter); it does not address staking, liquidity mining, airdrops, NFTs, hard forks or lending.

| Activity | Classification | Tax rate | Reporting form |
| --- | --- | --- | --- |
| Buy and hold, then sell | Capital gain | 25% | Form 1325 |
| Crypto-to-crypto swap | Capital gain (disposal + acquisition) | 25% | Form 1325 |
| Staking rewards | Income at receipt (conservative); debated | 25–50% | Form 1301 or 1325 |
| Liquidity mining / yield farming | Ordinary income | Marginal rates | Form 1301 |
| Airdrops (free tokens) | Income at receipt, capital gain on subsequent sale | Marginal + 25% | Form 1301 + 1325 |
| Mining | Business income or capital gain (depends on scale) | Variable | Form 1301 or 1325 |
| NFT sales (creator) | Business income | Marginal rates | Form 1301 |
| NFT sales (collector) | Capital gain | 25% | Form 1325 |
| Hard fork tokens | Zero cost basis, capital gain on sale | 25% | Form 1325 |
| Lending interest (CeFi/DeFi) | Interest income | 25% (passive) | Form 1301 |

### Classification notes

- **Staking guidance status**: ITA has not issued definitive guidance. Conservative approach treats rewards as income at receipt (market value), then capital gain/loss on subsequent sale
- **Airdrop treatment**: Received tokens are income at market value on receipt date. Cost basis for future sale = market value at receipt
- **Hard fork treatment**: New tokens have zero cost basis; entire sale proceeds are capital gain
- **Stablecoin treatment**: USDT, USDC, DAI are still "asset" under Section 88. Every USDT-to-USDC swap, every conversion leg of a DeFi trade, every off-ramp to fiat is a taxable disposal  _(Section 88)_

## Section 5: Loss offsetting rules

- **Crypto losses offset crypto gains**: Capital losses from crypto can offset capital gains from crypto in the same tax year
- **Losses offset other asset gains**: Capital losses can offset gains from other assets (stocks, real estate) in the same year
- **Loss carryforward**: Capital losses carry forward to offset future capital gains under Section 92 (but cannot offset ordinary income)  _(Section 92)_
- **Spousal loss offset**: Losses from one spouse can offset gains of the other spouse if filing jointly
- **No wash-sale rule**: Israel has no wash-sale rule: a taxpayer can sell in December at a loss and re-buy in January with the loss fully recognized

## Section 6: Reporting requirements

### 6.1 Annual reporting (Forms 1322 / 1325)

- **Form 1322**: Form 1322 (Nispach Gimel: נספח ג): primary capital gains schedule attached to annual return
- **Form 1325**: Form 1325 (Nispach Gimel(1): נספח ג(1)): auxiliary detail form for securities/crypto where tax was not withheld at source
- **Disposal reporting items**: For each disposal, report: 1. Asset description (e.g., "Bitcoin (BTC)") 2. Date of acquisition (FIFO-determined) 3. Date of disposal 4. Acquisition cost (NIS) 5. Disposal proceeds (NIS) 6. Capital gain or loss (NIS) 7. Holding period

### 6.2 Advance payment (Form 1399י)

- **Filing deadline**: File within 30 days of the capital gain event
- **Transaction codes**: Transaction codes: 77 (sale) and 71 (virtual currency)
- **Payment rate**: Payment: 25% of gain for individuals (30% for significant shareholders)
- **Advance payment credit**: Advance payments are credited against annual tax liability
- **Non-payment penalties**: Penalties for non-payment: interest (Ribit: ריבית) and CPI linkage (Hafreshei Hatzmada: הפרשי הצמדה)

### 6.3 Annual return obligation

- **Filing obligation for salaried individuals**: Salaried individuals with crypto disposals must file Form 1301 even if they would otherwise be exempt. Any disposal generally triggers a filing obligation.
- **Filing deadlines**: Filing deadlines (tax year 2025, filed in 2026): Online: June 30, 2026; Paper: May 29, 2026; CPA-represented: extensions available (tax year 2025)

## Section 7: Surtax on crypto gains (Mas Yesafim: מס יסף)

- **Surtax structure**: 3% on the part of total taxable income above NIS 721,560 (2026), and an additional 2% on taxable income from capital sources above that amount (2026 booklet p.11, s.121B). Work out each base separately; a crypto gain is in the 2% base only to the extent capital-source income exceeds the threshold.
- **Threshold freeze**: unverified: threshold frozen through 2027

## Section 8: Voluntary disclosure (Nohal Gilui Mirtzon: נוהל גילוי מרצון)

**Voluntary disclosure tracks table**

| Track | Eligibility | Deadline |
| --- | --- | --- |
| Green Track | unverified: annual income up to NIS 500,000 and cumulative crypto assets up to NIS 1.5M (as of 31.12.2024) | unverified: 31 August 2026 |
| Regular Track | unverified: larger cases | unverified: 31 August 2026 |

unverified: The 2025–2026 Voluntary Disclosure Procedure expressly covers digital assets and grants criminal immunity. Anonymity is no longer available: all applications filed with identifying details.

## Section 9: Special rules

### 9.1 Gifts and inheritance

- **Carryover basis for gifts/inheritance**: Under Section 97(a)(5), gifts and inheritance use carryover basis: the recipient inherits the donor's original cost basis and acquisition date. Treating inherited crypto as zero-basis or fair-market-value at inheritance is incorrect.  _(Section 97(a)(5))_

### 9.2 Lost crypto

- **Lost crypto treatment**: Crypto lost to exchange insolvency (FTX, Celsius pattern), theft, or lost private keys is recognized as a capital loss ONLY when the loss is final and documented (e.g., bankruptcy court order, police report). Do not write off frozen-but-not-bankrupt balances.

### 9.3 Inflation indexation

- **Inflation indexation split**: unverified: Section 91(b)(3) splits capital gain into a "real gain" (taxed at 25%) and an "inflation-component gain" (taxed at 0% for individuals on assets acquired after 1.1.1994). For long-held lots, a CPA should perform the manual indexation pass, which reduces effective tax. (assets acquired after 1.1.1994)  _(Section 91(b)(3))_

## Section 10: Worked examples

### Example 1: Simple buy and sell

**Scenario:** Bought 0.5 BTC in January 2025 for NIS 80,000, sold in August 2025 for NIS 120,000.

**Working:**
- Capital gain: NIS 120,000 − NIS 80,000 = NIS 40,000
- Tax (up to 25% on real gain, asset bought after 1/1/2012, rights guide PDF p.48): NIS 40,000 × 25% = NIS 10,000
- Surtax: total income below NIS 721,560 → no surtax
- Advance payment: Form 1399י within 30 days of August sale → NIS 10,000
- Annual reporting: Forms 1325/1322 with 2025 Form 1301

### Example 2: Crypto-to-crypto with FIFO

**Scenario:** Bought 2 ETH at NIS 5,000 each (March 2024), 3 ETH at NIS 7,000 each (June 2024). In October, traded 3 ETH for 0.5 BTC when ETH = NIS 9,000.

**Working:**
- FIFO: consume Lot 1 (2 ETH @ NIS 5,000) then 1 ETH from Lot 2 (@ NIS 7,000)
- Lot 1 gain: 2 × (NIS 9,000 − NIS 5,000) = NIS 8,000
- Lot 2 partial gain: 1 × (NIS 9,000 − NIS 7,000) = NIS 2,000
- Total gain: NIS 10,000 → Tax: NIS 2,500
- New BTC cost basis: NIS 27,000 (3 × NIS 9,000)
- Remaining: 2 ETH at NIS 7,000 each

### Example 3: DeFi staking rewards

**Scenario:** Staked 10 ETH, earned 0.5 ETH in rewards (ETH = NIS 8,000 at receipt). Not sold.

**Working:**
- Conservative: NIS 4,000 taxable income at receipt (0.5 × NIS 8,000)
- Rate: 25% if passive income → NIS 1,000 tax; or marginal rates if ordinary income
- Cost basis for 0.5 reward ETH established at NIS 8,000/ETH
- The 10 staked ETH have not been disposed: no capital gain event on those
- Recommend professional consultation on staking classification

## Section 11: Common errors

**Common errors table**

| Error | Consequence |
| --- | --- |
| Using US capital gains rates (15%/20%) | Israeli rate is 25% for individuals |
| Treating crypto-to-crypto as non-taxable | Always taxable in Israel |
| Using average cost or LIFO | unverified: Israel mandates FIFO |
| Ignoring stablecoin conversions | USDT/USDC are assets: every swap is a disposal |
| Treating inherited crypto as zero basis | Carryover basis applies (Section 97(a)(5)) |
| Applying US wash-sale rule | Israel has no wash-sale rule: loss harvesting is valid |
| Missing 30-day advance payment deadline | Interest and linkage penalties accrue |
| Ignoring surtax on crypto gains | 3% on total taxable income above NIS 721,560 plus 2% on capital-source income above it (2026 booklet p.11) |

## Section 12: Reference material

**Reference material table**

| Resource | Reference |
| --- | --- |
| ITA Circular 05/2018 (crypto classification) | https://www.gov.il/he/Departments/legalInfo/04-2018 |
| Tax Authority: annual return service | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals |
| Bank of Israel: exchange rates | https://www.boi.org.il/roles/markets/exchangerates/ |
| Voluntary Disclosure Procedure 2025–2026 | https://www.gov.il/he/Departments/policies/voluntary-disclosure-2025 |
| Bituach Leumi: self-employed rates | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |
| OECD CARF (Israel collection from 1 Jan 2026) | https://www.oecd.org/tax/exchange-of-tax-information/crypto-asset-reporting-framework.htm |

## Section 13: When to escalate to a professional

- Transaction volume exceeds 100 trades per year
- DeFi activities involve complex protocols (multi-chain, bridging, wrapping)
- Uncertainty whether activity constitutes business vs investment
- Total gains exceed NIS 500,000
- Tokens received from ICO, IEO, or similar offering
- Cross-border transactions with foreign tax obligations
- Voluntary disclosure consideration

## Recomputed checks (2026)

```oa-check
name: Gain NIS 40,000 at 25%
inputs:
  g: 40000
steps:
  - t: g*0.25
expected:
  t: 10000
```

```oa-check
name: Surtax when all NIS 800,000 of taxable income is capital-source (2026)
inputs:
  total: 800000
  capital: 800000
steps:
  - base3: max(total-721560, 0)*0.03
  - base2: max(capital-721560, 0)*0.02
  - s: base3+base2
expected:
  s: 3922
```

The two charges have separate bases (2026 booklet p.11). They add up to 5% only where all the income above the threshold is capital-source, as here. unverified: how the 2% base is measured when income is mixed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Israel Tax Authority, Circular 5/2018 on decentralised payment instruments ("virtual currencies"), read all six pages (ss.2.3, 3.1.1 to 3.1.5 income tax, 3.2 VAT) | https://www.gov.il/BlobFolder/policy/income-tax-professional-inst-5-2018/he/Policy_ProfessionalInstIncomeTax_hor_acc%2015.2.18.pdf | 2026-11-03 |
| Israel Tax Authority, "Know your rights and duties" guide, tax year 2025 (published July 2026), read PDF p.47 (Form 1399 for virtual currency, symbol 77 code 71, monthly grouping) and PDF p.48 (capital gains rates: up to 25% on real gain for assets bought from 1/1/2012, linear split, material shareholder in securities) | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-03 |
| Israel Tax Authority, salary-deduction booklet from January 2026 (updated April 2026), read p.11 (s.121B surtax 3% above NIS 721,560 and 2% on capital-source income) | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf | 2026-11-03 |
| Israel Tax Authority, Form 1301 service page, tax year 2025 | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals | 2026-11-01 |

Not yet confirmed: the 30% rate for a significant shareholder applied to crypto (the guide states the 30% uplift for securities held by a material shareholder) and the 23% corporate rate; how the monthly grouping on Form 1399 interacts with FIFO; FIFO as the cost-basis method; the DeFi, staking, airdrop, NFT, hard-fork and lending rows; Form 1399 and the 30-day advance; loss offsetting and carryforward; gifts and inheritance basis; the voluntary disclosure dates and tracks; the indexation rule; the threshold freeze; how the 2% surtax base is measured for mixed income.

## Disclaimer

> **חשוב:** כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional: such as a רואה חשבון (Ro'eh Cheshbon: CPA) or יועץ מס (Yo'etz Mas: tax advisor) licensed in Israel: before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-03. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-crypto-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-crypto-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
