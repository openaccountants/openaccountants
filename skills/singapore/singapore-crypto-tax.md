---
name: singapore-crypto-tax
description: Use this skill whenever asked about Singapore cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Singapore", "Bitcoin Singapore", "digital tokens Singapore", "cryptocurrency gains Singapore", "IRAS crypto", "GST crypto Singapore", "staking Singapore", "mining income Singapore", "NFT tax Singapore", "Coinbase Singapore", "Binance Singapore", "payment tokens", "digital payment tokens", "capital gains Singapore crypto", "crypto business income Singapore", or any question about the income tax, GST, or reporting obligations for cryptocurrency, tokens, or digital assets for Singapore tax residents or Singapore-source crypto income. Covers IRAS e-Tax Guide on Digital Tokens (income tax and GST), trader vs investor distinction, badges of trade, and GST exemption for digital payment tokens. ALWAYS read this skill before touching any Singapore crypto work.
version: 2.1
jurisdiction: SG
tax_year: 2026
tax_year_notes: "2026 income belongs to YA 2027; historical YA rebates explicitly labelled"
last_updated: 2026-11-22
depends_on:
  - sg-income-tax
category: crypto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: situation-rules
---

# Singapore digital-token tax v2.1

2026 income normally belongs to YA 2027. Rates labelled from YA 2024 onwards remain applicable; historical filing dates and rebates never become current merely by changing the file date.

## Scope and who this is for


**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Singapore (Republic of Singapore) |
| Tax | Income tax; separately test GST treatment |
| Currency | SGD (values must be converted to SGD at transaction date) |
| Tax year | Preceding year basis , income earned in calendar 2026 normally belongs to YA 2027; confirm the actual accounting basis period |
| Primary authority | IRAS e-Tax Guide: Income Tax Treatment of Digital Tokens (updated 30 January 2026) |
| GST authority | IRAS e-Tax Guide: GST , Digital Payment Tokens (third edition, 30 January 2026; DPT treatment effective 1 January 2020) |
| Tax authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing portal | myTax Portal (mytax.iras.gov.sg) |
| Individual filing deadline | 18 April 2027 for YA 2027 [IRAS due dates](https://www.iras.gov.sg/due-dates?dueYear=2027) |
| Corporate tax rate | Flat 17% on chargeable income [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| Top personal rate | 24% on income above S$1,000,000, from YA 2024 [IRAS](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Capital disposals | Generally outside income tax for individuals; test section 10L for foreign-asset disposal gains received in Singapore by an entity of a relevant group [IRAS](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr10L-&ValidDate=20261122&ViewType=Advance) |
| Skill version | 2.1 |

### Key Principle

Gains from disposals on capital account are generally outside Singapore income tax. Classify the disposal on its facts. Profits from a trade or business are ordinary income under section 10(1)(a) of the Income Tax Act 1947 (ITA). For an entity of a relevant group, separately test section 10L on gains received in Singapore from foreign-asset disposals on or after 1 January 2024, including the statutory exclusions.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether trading or investment | Assess against badges of trade; if unclear, treat as potentially taxable (trading) and seek IRAS ruling |
| Unknown token classification | Obtain token terms, rights and GST characteristics; hold classification |
| Unknown cost basis | STOP , cannot compute gain without acquisition cost |
| Unknown residency or income source | Check each separately before applying the applicable rates, exemptions and treaty rules |
| Unknown whether mining is hobby or business | Companies → presumed business; individuals → evaluate frequency and scale |


## Ask the client first

Confirm the income period, residence/source, individual/company, contracts and token rights, purpose at acquisition/disposal, trading organisation, every wallet/exchange transaction, cost method, fees, SGD valuation, reward entitlement and any moratorium, GST registration and customer-belonging evidence. A wallet narration cannot establish beneficial ownership or tax character.

## Rates, bands and thresholds


### 3.1 Personal Income Tax Rates (YA 2027, Resident Individuals)

**Personal Income Tax Rates (YA 2027, Resident Individuals)**  _(IRAS, Individual Income Tax rates, effective from YA 2024 onwards.)_

| Chargeable Income (S$) | Rate | Cumulative Tax (S$) |
| --- | --- | --- |
| First 20,000 | 0% | 0  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 10,000 | 2% | 200  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 10,000 | 3.5% | 550  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 40,000 | 7% | 3,350  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 40,000 | 11.5% | 7,950  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 40,000 | 15% | 13,950  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 40,000 | 18% | 21,150  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 40,000 | 19% | 28,750  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 40,000 | 19.5% | 36,550  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 40,000 | 20% | 44,550  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 180,000 | 22% | 84,150  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Next 500,000 | 23% | 199,150  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Above 1,000,000 | 24% | 199,150 on the first million  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |

Historical YA 2025 only: 60% rebate capped at S$200. It is not carried into YA 2027. No YA 2027 rebate is confirmed in this pass.

### 3.2 Corporate Income Tax Rate

**Corporate Income Tax Rate**  _(Income Tax Act 1947 (ITA), Section 43; IRAS corporate tax guide.)_

| Parameter | Value |
| --- | --- |
| Headline rate | 17%  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| PTE: first S$10,000 normal income before exemption | 75% exemption → derived effective 4.25% = 17% × 25%  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| PTE: next S$190,000 normal income before exemption | 50% exemption → derived effective 8.5% = 17% × 50%  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |

PTE applies only where the company is not claiming SUTE; SUTE requires separate first-three-YA, residence, incorporation, shareholder and activity conditions. Any YA-specific rebate is separate from these bands.

### 3.3 Non-Resident Rates

**Non-Resident Rates**

| Income Type | Rate |
| --- | --- |
| Employment income | Higher of 15% flat or progressive resident rates  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Non-resident director remuneration | 24% from YA 2024  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Non-resident professional services performed in Singapore | 15% gross or 24% net, subject to the actual category and treaty  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Non-resident trade/business income | Corporate 17%; individual 24% unless a reduced withholding/treaty category applies  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |


## The method, step by step

1. Reconcile holdings and transfers across all wallets and exchanges. Separate own-wallet movements from disposals.
2. Classify token rights for income tax, then separately apply the GST DPT tests. Currency-pegged stablecoins fail the DPT definition but may be separately exempt derivatives; NFTs are not fungible DPTs. Unknown tokens are held, not defaulted to payment tokens.
3. Establish source and capital/revenue character from the whole activity. Long holding or passive receipt alone does not decide every tax question.
4. Apply contractual accrual/valuation, the accepted cost method, business deductions and the correct resident/corporate computation. Do not double-count income on receipt and later disposal.
5. Complete the return and GST workpapers, check deadlines and retain the submission/payment confirmations. Preparation does not itself file a return.

### Classification


### 2.1 IRAS Digital Token Classification

**IRAS Digital Token Classification**  _(IRAS e-Tax Guide updated 30 January 2026)_

| Token Type | Definition | Examples | Tax Treatment on Disposal |
| --- | --- | --- | --- |
| **Payment tokens** | Tokens that function or are intended to function as a medium of exchange | Examples include BTC and ETH; classify actual rights. GST DPT is a separate, narrower definition | Apply the capital/revenue test and, for relevant group entities, the section 10L rules |
| **Utility tokens** | Tokens that provide access to a current or prospective product/service on a DLT platform | Filecoin (FIL), BAT, service access tokens | Apply the capital/revenue test and, for relevant group entities, the section 10L rules |
| **Security tokens** | Tokens that represent ownership rights (equity, debt, units in a fund) | Tokenised shares, tokenised bonds, fund tokens | Identify interest, dividend or other distribution and any non-resident withholding separately; capital/revenue test for disposal |

IRAS classifies digital tokens into three categories for tax purposes (per the e-Tax Guide, January 2026):

### 2.2 Taxable vs Non-Taxable Events

**Taxable vs Non-Taxable Events**

| Event | Taxable? | Condition |
| --- | --- | --- |
| Disposal of crypto investment (capital gain) | Generally outside income tax | Establish capital treatment on the facts and check section 10L if the seller is an entity of a relevant group |
| Disposal of crypto trading stock (revenue gain) | **Yes** | Part of a trading business; taxed as income |
| Receiving crypto as payment for goods/services | **Yes** | Taxable contractual value when income accrues; token-count versus fiat-value contract matters |
| Mining rewards (company) | **Yes, on disposal** | Mining business disposal profits, not merely successfully mining and holding a token |
| Mining rewards (individual, habitual) | **Yes** | If habitual and systematic → vocation income |
| Mining rewards (individual, hobby) | **No** | Prima facie hobby; capital gain on disposal not taxable |
| Staking or DeFi yields | Depends on the facts | Establish the character, source, entitlement date and SGD value of each reward. Refer unresolved protocol-specific treatment. |
| Airdrop with nothing expected in return | **No** | A genuine windfall on receipt; later disposal requires separate capital/revenue and cost analysis |
| Airdrop in exchange for goods or services | **Yes** | Apply the ordinary rules for accrual and valuation of the consideration |
| Crypto-to-crypto swap on capital account | Generally outside income tax | Establish capital treatment and check section 10L for relevant group entities |
| Crypto-to-crypto swap (trader) | **Yes** | Revenue transaction; gain/loss is taxable |
| Transfer between own wallets | **No** | No change in beneficial ownership |


### Cost basis


### 4.1 Accepted Methods

**Accepted Methods**

| Method | Status | Notes |
| --- | --- | --- |
| Specific identification | Not confirmed in this pass | Do not assume it replaces the methods expressly accepted in paragraph 5.7 |
| FIFO (First In, First Out) | Accepted | Paragraph 5.7 for taxable payment-token disposals |
| Weighted average cost | Acceptable | Particularly for fungible tokens traded in volume |
| LIFO | Not acceptable | Paragraph 5.7 footnote expressly rejects LIFO |

- **Consistent application** , Once a method is chosen, apply it consistently across the tax year and across years.

### 4.2 Cost Basis Components

- Purchase price in SGD (convert foreign currency at exchange rate on acquisition date)
- Exchange/trading fees and commissions on acquisition
- Network/gas fees directly attributable to the acquisition
- Any other directly incurred acquisition costs

### 4.3 For Businesses (Revenue Assets)

- Cost basis = purchase price + incidental acquisition costs
- Standard accounting principles (FRS 2 / SFRS(I) 1-2 for the inventory-method reference) apply
- Reconcile accounting valuation to tax. Paragraph 5.6 excludes unrealised fair-value gains/losses from taxable/deductible amounts; do not claim an automatic tax deduction for an accounting write-down.


### Rewards, mining and forks


### 5.1 Mining

**Mining**  _(IRAS Income Tax Treatment of Digital Tokens, Annex A, receipt D/E)_

| Scenario | Tax Treatment |
| --- | --- |
| Company mining | A mining business is taxed on profits when it disposes of its mined tokens. Deduct eligible operating costs from business commencement and consider capital allowances for equipment. |
| Individual mining (habitual, systematic) | Vocation income , profits from sale of mined tokens are taxable |
| Individual mining (hobby) | Not taxable , gains on sale are capital gains (no CGT) |

- **Key nuance** , For miners, IRAS taxes at the point of disposal, not at receipt. Do not capitalise expenses already deducted on an incurred basis and deduct them again as token cost. Mining-service fees are separately taxable. A company deducts eligible costs from business commencement, with equipment through applicable capital allowances.  _(IRAS Income Tax Treatment of Digital Tokens, Annex A, receipt D/E)_

### 5.2 Staking and DeFi

Staking rewards, DeFi lending interest, liquidity provision and yield farming remain separate questions. The official token guide read here does not settle all their receipt, source, timing and cost questions. Obtain protocol contracts, reward conditions, entitlement dates, lock-ups, services performed and business facts. Do not infer tax-free capital income merely because an individual is passive or occasional, or choose receipt/disposal timing from accounting preference. Hold unresolved tax classifications for the practitioner, with the old proposed treatments named under Not yet confirmed.

### 5.3 Airdrops and Hard Forks

**Airdrops and Hard Forks**

| Event | Tax Treatment |
| --- | --- |
| Airdrop (no consideration given) | No receipt income if no goods/services or expected service; later disposal may be trading income |
| Airdrop (in return for service, e.g. referral) | Taxable income at FMV |
| Hard fork (new coin received) | Windfall at receipt where nothing is done in return; later trading disposal can be taxable; zero cost allocation is not assumed |


### NFTs


**NFT Treatment**

| Scenario | Treatment |
| --- | --- |
| Purchase of NFT | Acquisition at cost , cost basis for future disposal |
| Sale of NFT on capital account | Generally outside income tax; check section 10L for relevant group entities |
| Sale of NFT (trader/business) | Taxable business income |
| Creation and sale of NFT (artist/creator) | Classify the actual services, vocation and transaction; occasional creation does not itself establish tax-free hobby proceeds |
| NFT → NFT swap on capital account | Generally outside income tax; check section 10L for relevant group entities |
| NFT → NFT swap (trader) | Revenue transaction , taxable |
| NFT royalties | Determine whether the payment is a royalty for use of IP or another type of income. Singapore-source royalties of an individual are taxable in the year they are due and payable. Check the applicable source and withholding rules. [IRAS royalty guidance](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/royalty) |
| GST on NFT sales | If NFT is not a digital payment token → standard GST rules may apply (9% from 1 January 2024) |


## Boundary and exception table

### Loss relief


**Loss Offset and Carry-Forward**

| Rule | Detail |
| --- | --- |
| Trading losses | Can offset against other income in the same YA (Section 37 ITA) |
| Carry-forward of unabsorbed losses | Unabsorbed trade losses: verify the taxpayer-specific carry-forward conditions; corporate shareholding and capital-allowance same-business tests are not universal individual tests |
| Carry-back | Elect to carry back up to S$100,000 in eligible current-year unabsorbed capital allowances and trade losses combined to the immediately preceding YA. The same-business test applies to capital allowances. Companies also apply the substantial-shareholding test. The three-YA enhancement applied only to YAs 2020 and 2021. [IRAS company rules](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/loss-carry-back-relief) and [individual business rules](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/business-making-losses-and-unabsorbed-capital-allowances) |
| Capital losses | Generally outside ordinary trade loss relief; test the separate foreign loss rules for an entity within section 10L |
| Investment losses (individual) | Not deductible , capital in nature |


### Anti-avoidance


**Anti-Avoidance Rules**

| Rule | Description |
| --- | --- |
| General anti-avoidance (section 33 ITA) | The Comptroller must counteract the tax advantage if the statutory purpose or effect test is met. Section 33(7) excludes bona fide commercial arrangements with no main purpose of avoiding or reducing tax. |
| Transfer pricing (Section 34D ITA) | Arm's length standard applies to related-party crypto transactions |
| Substance over form | IRAS may recharacterise transactions based on economic substance |
| Recharacterisation of capital as revenue | If IRAS determines activity is trading despite taxpayer's claim of investment, gains become taxable |
| MAS compliance | Unlicensed crypto activities may attract regulatory scrutiny and affect tax positions |


## Worked cases


### Example 1 -- Long-Term Investor (Not Taxable)

**Input:** Singapore tax resident individual. Employed full-time as a software engineer. Bought 2 BTC at S$40,000 each on 1 July 2022. Sold 2 BTC at S$75,000 each on 1 July 2026. Two transactions, investment facts documented. Used personal savings.

**Analysis:**
```
Proceeds:           2 × S$75,000 = S$150,000
Cost basis:         2 × S$40,000 = S$80,000
Gain:               S$70,000

Badges of trade assessment:
  Frequency:        Low (1 purchase and 1 sale over 4 years)
  Holding period:   Long (4 years)
  Motive:           Long-term appreciation
  Financing:        Own savings
  Organisation:     Casual, alongside employment

Classification:     INVESTMENT (capital gain)
Tax:                S$0 on this individual's capital gain
```

**Reporting:** For these assumed investment facts the disposal gain is capital; retain the classification evidence and answer any IRAS request. This does not waive the individual’s unrelated return obligation.

### Example 2 -- Active Trader (Taxable)

**Input:** Singapore tax resident individual. No other employment. Traded crypto full-time on an exchange in 2026. Made 500+ trades, average holding period 3 days. Used leverage. Total revenue: S$200,000 from cost basis of S$120,000. Net trading gain: S$80,000.

**Analysis:**
```
Revenue:            S$200,000
Cost of tokens:     S$120,000
Net gain:           S$80,000

Badges of trade assessment:
  Frequency:        Very high (500+ trades)
  Holding period:   Very short (3 days average)
  Motive:           Short-term profit
  Financing:        Used leverage
  Organisation:     Full-time, sole activity

Classification:     TRADING (business income)
Tax computation:    Chargeable income S$80,000
  First S$20,000 @ 0%    = S$0
  Next S$10,000 @ 2%     = S$200
  Next S$10,000 @ 3.5%   = S$350
  Next S$40,000 @ 7%     = S$2,800
  Total tax:              = S$3,350
  No YA 2027 rebate established:       S$0
  Gross tax before rebates or credits: S$3,350
```

**Reporting:** Declare trade income in the self-employment section of the YA 2027 return by 18 April 2027. This example assumes S$80,000 of chargeable income after allowable adjustments and reliefs. [IRAS due dates](https://www.iras.gov.sg/due-dates?dueYear=2027)

### Example 3 -- Company Mining Operation

**Input:** Singapore-incorporated company. Mines a hypothetical proof-of-work payment token using dedicated hardware. Calendar-2026 revenue: 50 tokens sold at average S$4,000 each = S$200,000. Assume S$80,000 is the total allowable electricity/hosting and qualifying capital-allowance amount after adding back accounting depreciation.

**Analysis:**
```
Revenue:            S$200,000
Expenses:           S$80,000
Chargeable income:  S$120,000

Corporate tax (17%):
  First S$10,000:   75% exempt → taxable S$2,500 @ 17% = S$425
  Next S$110,000:   → S$190,000 bracket, 50% exempt → taxable S$55,000 @ 17% = S$9,350
  Total tax:        S$9,775
```

**Reporting:** For a 31 December 2026 FYE, file ECI by 31 March 2027 unless waived. File the YA 2027 company return by 30 November 2027. The S$9,775 calculation assumes PTE eligibility and excludes any YA-specific credit or rebate. [IRAS due dates](https://www.iras.gov.sg/due-dates?dueYear=2027)


```oa-check
name: Token investor and resident trading gross tax
inputs:
  units: 2
  sale_price: 75000
  purchase_price: 40000
  revenue: 200000
  allowable_cost: 120000
steps:
  - investor_gain: units * (sale_price - purchase_price)
  - trading_chargeable_income_assumed: revenue - allowable_cost
  - trading_gross_tax: 10000 * 0.02 + 10000 * 0.035 + 40000 * 0.07
expected:
  investor_gain: 70000
  trading_chargeable_income_assumed: 80000
  trading_gross_tax: 3350
```

```oa-check
name: Mining company partial exemption before YA specific credits
inputs:
  revenue: 200000
  allowable_cost_and_ca: 80000
steps:
  - normal_income: revenue - allowable_cost_and_ca
  - first_band_taxable: min(normal_income, 10000) * 0.25
  - second_band_taxable: min(max(normal_income - 10000, 0), 190000) * 0.5
  - gross_tax: (first_band_taxable + second_band_taxable) * 0.17
expected:
  normal_income: 120000
  first_band_taxable: 2500
  second_band_taxable: 55000
  gross_tax: 9775
```

## When to refuse or refer

Hold missing cost, source, residence, token rights or beneficial ownership. Refer ambiguous capital/revenue, protocols, ICO/security-token, non-resident withholding, licensing and disputed loss relief to the relevant practitioner. Never call passive yields tax-free by default; never use LIFO. Do not submit or pay without the client’s authorised process.

## Filing and payment


### 7.1 Badges of Trade (Trader vs Investor Determination)

**Badges of Trade (Trader vs Investor Determination)**

| Badge | Indicates Trading | Indicates Investment |
| --- | --- | --- |
| Subject matter | Commodities or items typically traded | Assets typically held for long-term appreciation |
| Frequency of transactions | High volume, repeated transactions | Infrequent, isolated transactions |
| Holding period | Short (days to weeks) | Long (months to years) |
| Supplementary work | Value-added activities (market making, arbitrage) | No additional work beyond buy-and-hold |
| Circumstances of sale | Systematic selling pattern | Sold only when needed or at opportune time |
| Motive/intention | Profit from short-term price movements | Long-term capital appreciation |
| Financing | Borrowed funds to trade | Own savings |
| Organisation | Business-like structure, dedicated accounts | Casual, alongside primary employment |

IRAS applies the common law "badges of trade" to distinguish trading (taxable) from investment (not taxable):

### 7.2 Filing Forms

**Filing Forms**

| Form | Who Files | Deadline |
| --- | --- | --- |
| Form B | Self-employed individuals when this form is issued, including people with a crypto trading business | 18 April 2027 |
| Form B1 | Resident individuals when this form is issued; include applicable employment and other taxable income | 18 April 2027 |
| Form M | Non-resident individuals when this form is issued | 18 April 2027 |
| Form C-S / C-S (Lite) / Form C (companies) | Companies with crypto business income | 30 November of the relevant YA; confirm first-account and waiver facts [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies) |
| ECI (Estimated Chargeable Income) | Companies | Within 3 months of FYE unless waived; ordinary waiver requires revenue ≤S$5m and nil pre-exemption ECI [IRAS](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-%28eci%29-filing) |

### 7.3 GST Reporting

**GST Reporting**  _(IRAS e-Tax Guide: GST , Digital Payment Tokens (effective 1 January 2020))_

| Transaction | GST Treatment |
| --- | --- |
| Exchange of digital payment tokens for fiat (or vice versa) | **Exempt supply** (no GST) |
| Exchange of digital payment tokens for other digital payment tokens | **Exempt supply** |
| Use of qualifying digital payment tokens to pay for other goods/services | Disregard the token for GST. Apply the ordinary GST rules to the underlying goods or services. |
| ICO that issues qualifying digital payment tokens in exchange for currency or other qualifying digital payment tokens | Exempt supply. Apply the ordinary GST rules to token types or other consideration outside this exemption. |
| Supply of utility tokens | Depends on underlying supply , may be standard-rated (9%) or exempt  [IRAS GST guide](https://www.iras.gov.sg/docs/default-source/e-tax/e-tax-guide_gst_digital-payment-tokens.pdf) |
| Mining services to identifiable recipient for consideration | Taxable services; 9% if standard-rated, with actual zero-rating conditions tested  [IRAS GST guide](https://www.iras.gov.sg/docs/default-source/e-tax/e-tax-guide_gst_digital-payment-tokens.pdf) |
| NFT sale | Not a digital payment token , standard GST rules apply |

- **GST registration threshold** , Taxable turnover exceeding S$1 million under the calendar-year retrospective or supported next-12-month prospective test. Exempt DPT supplies do NOT count as taxable turnover. Do not use gross token-exchange proceeds as taxable turnover.  _(IRAS e-Tax Guide: GST , Digital Payment Tokens (effective 1 January 2020))_

### 7.4 No FBAR Equivalent

Do not import the US FBAR form into Singapore. The absence of one similarly named form does not establish that the client has no tax, automatic-exchange or regulatory reporting duties:
- Under the Crypto-Asset Reporting Framework, reporting Singaporean crypto-asset service providers register with IRAS and report relevant transactions annually. Check the provider and transaction definitions. [IRAS reporting framework](https://www.iras.gov.sg/taxes/international-tax/crypto-asset-reporting-framework-%28carf%29/carf-overview-and-latest-developments)
- Check the regulated service, where it is provided and where customers are located for Monetary Authority of Singapore licensing and reporting. [MAS licensing scope](https://www.mas.gov.sg/news/media-releases/2025/mas-clarifies-regulatory-regime-for-digital-token-service-providers)
- Licensed payment service providers under the Payment Services Act 2019 have AML/CFT reporting requirements


For filing steps and current individual payment notices load `sg-income-tax`; for GST boxes, due dates, input attribution and confirmation load `sg-gst-return`. ICO utility proceeds generally defer until performance; payment-token issuance and security-token capital require actual rights analysis. Founder remuneration can accrue only when a moratorium ends; this does not make all founder tokens remuneration. Keep contracts, units, transaction dates, verifiable SGD rates, invoices and expense records.

## Completion checklist


Before finalising any Singapore crypto tax computation:

- [ ] Assessed badges of trade to determine capital vs revenue nature
- [ ] Confirmed Singapore tax residency status
- [ ] Verified whether individual or corporate taxpayer
- [ ] For companies: confirmed whether mining/trading income is Singapore-sourced
- [ ] Applied correct cost basis method consistently
- [ ] GST implications assessed (digital payment token exemption vs standard supply)
- [ ] Ensured no double-counting of exempt supply in GST returns
- [ ] Trading losses properly offset or carried forward
- [ ] No historical personal or corporate rebate carried into YA 2027 without authority


## Sources

| Source and scope read | Official URL | Read for on |
|---|---|---|
| Read for paragraphs 4.4 to 12 and Annexes A/B: rights, barter, valuation, realised timing, FIFO/WAC and rejected LIFO, mining/service fees, airdrops, hard forks, ICOs and records; 30 January 2026 update. | https://www.iras.gov.sg/media/docs/default-source/e-tax/etaxguide_cit_income-tax-treatment-of-digital-tokens_091020.pdf | 2026-11-14 |
| Read for paragraphs 2 to 12: DPT characteristics and exclusions, stablecoin derivatives, token/non-token legs, turnover exclusion, mining, customer belonging, principal/agent, input-tax apportionment; third edition 30 January 2026. | https://www.iras.gov.sg/docs/default-source/e-tax/e-tax-guide_gst_digital-payment-tokens.pdf | 2026-11-14 |
| Read for current from-YA-2024 resident bands, non-resident employment, director/professional withholding distinction and historical rebates. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates | 2026-11-14 |
| Read for headline rate, PTE and SUTE conditions, current YA 2026 rebate and grant; no YA 2027 rebate was established. | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes | 2026-11-14 |
| Read for ordinary one-YA carry-back, aggregate ceiling, conditions, historic YA 2020/2021 exception and Form C election. | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-reliefs/loss-carry-back-relief | 2026-11-14 |
| Read for current DPT tests, use as consideration, exempt exchange/loan and unchanged underlying supply. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/specific-business-sectors/digital-payment-tokens | 2026-11-14 |
| Read for paper Forms B, B1 and M and the historical YA 2026 deadline of 18 April. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/filing-a-paper-income-tax-return | 2026-11-14 |
| Read for current 9% standard GST rate and historical rate periods. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates | 2026-11-14 |
| Read for ordinary three-month ECI requirement and revenue/nil-ECI waiver, independent of final return. | https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-%28eci%29-filing | 2026-11-14 |
| Read for annual 30 November corporate return and first-account/YA allocation, distinct from ECI. | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies | 2026-11-14 |
| YA 2027 individual and corporate filing and December-year-end ECI dates. | https://www.iras.gov.sg/due-dates?dueYear=2027 | 2026-11-24 |
| Section 10L and foreign asset disposal gains received in Singapore. | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr10L-&ValidDate=20261122&ViewType=Advance | 2026-11-24 |
| Same-business condition, carry-back limit and qualifying individual businesses. | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/business-making-losses-and-unabsorbed-capital-allowances | 2026-11-24 |
| Royalty income, Singapore source and due-and-payable timing. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/royalty | 2026-11-24 |
| CARF definitions and registration, reporting and exchange obligations. | https://www.iras.gov.sg/taxes/international-tax/crypto-asset-reporting-framework-%28carf%29/carf-overview-and-latest-developments | 2026-11-24 |
| June 2025 licensing clarification for providers serving offshore and local customers. | https://www.mas.gov.sg/news/media-releases/2025/mas-clarifies-regulatory-regime-for-digital-token-service-providers | 2026-11-24 |

Not yet confirmed: protocol-specific staking, DeFi lending, liquidity provision and yield-farming character, source and timing. Check the facts and authority before using specific identification or a zero allocation to airdrop or fork tokens, including incidental costs, deducting inventory write-downs or applying license, reporting or withholding rules to a particular client. IRAS publishes the YA 2027 filing due date. Check the relevant filing notice for the portal opening and verify any YA 2027 rebate before applying it.
