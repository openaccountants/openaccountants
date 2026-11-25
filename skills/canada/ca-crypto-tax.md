---
name: ca-crypto-tax
description: Use this skill whenever asked about Canadian cryptocurrency taxation. Trigger on phrases like "crypto tax Canada", "CRA crypto", "Bitcoin capital gains Canada", "crypto business income CRA", "adjusted cost base crypto", "ACB crypto", "mining tax Canada", "staking tax Canada", "GST HST crypto", "crypto inclusion rate Canada", or any question about how cryptocurrency is taxed by the CRA. This skill covers capital gains vs business income treatment, the 50% inclusion rate, ACB tracking, mining/staking as business income, GST/HST on crypto payments, and record-keeping requirements. ALWAYS read this skill before touching any Canadian crypto tax work.
version: "1.1"
jurisdiction: CA
tax_year: 2025
tax_year_notes: Historical 2025 return workpaper and rates; later source reads do not recertify the entire skill for the current year.
last_updated: 2026-11-25
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: crypto
---

# CA Crypto Tax

## Canada Crypto Tax -- Capital Gains & Business Income Skill v1.1

This is a correction to a historical 2025 workpaper. **HOLD** blocks final use of an affected conclusion until the specified source, rights or case inputs are established. Missing evidence does not establish zero cost, capital character, a taxable receipt or no tax.

## Rates and thresholds

> Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
> That historical attribution does not approve this proposed correction. Unresolved claims and operative conditions are explicitly held below.

### Crypto Tax (CA)

- **CRA treatment** — Commodity (not currency)  _(CRA — Cryptocurrency and your income tax obligations — canada.ca)_
- **Cost basis method** — Average adjusted cost for identical capital properties under section 47; not a universal business-inventory method. [ITA 47](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html).
- **Ordinary capital-gains inclusion (2025)** — 50%, subject to section 38's specific exceptions; no ordinary $250,000 breakpoint. The proposed 66.67% increase was cancelled on 21 March 2025. This ordinary rule also covers corporations/trusts; do not describe every special gain as necessarily having the same inclusion. [ITA 38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html); [dated cancellation announcement](https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase).
- **Sell for fiat** — YES — disposition  _(CRA — crypto guidance; ITA s.39)_
- **Crypto-to-crypto swap** — YES — barter transaction  _(CRA — crypto guidance; ITA s.39)_
- **Purchase goods/services** — YES — at FMV  _(CRA — crypto guidance)_
- **Gift crypto** — Ordinary ownership gifts are dispositions. **HOLD the actual FMV basis and spouse/common-law/spousal-trust rollover or election result:** complete section 69/73 residency, trust and election conditions were not read in this unit. Retain those investigations; no automatic rollover is certified. [CRA dispositions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html).
- **Transfer between own wallets** — NO — same beneficial owner  _(CRA — crypto guidance)_
- **Death** — HOLD an actual section 70(5)/(6) deemed disposition, beneficiary basis or spousal/trust rollover pending the operative residency, vesting and trust conditions; these provisions were not completely read in this unit. The death and rollover topics are retained in 6.6.
- **Window** — 30 days before to 30 days after the disposition — AND you or an affiliated person must still own (or have a right to acquire) the same or identical property at the end of that period (s.54; loss denied under s.40(2)(g)(i))  _(ITA s.40(2)(g); ITA s.54 (definition of superficial loss))_
- **Effect** — A superficial loss can be denied; an ACB adjustment is usually available in the applicable acquiring-taxpayer case, not every affiliated or registered-plan arrangement. HOLD actual ownership, exclusions and ACB recovery. [CRA superficial-loss guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html).
- **Staking** — CRA now describes centralized-exchange rewards as generally income when credited to the platform wallet. HOLD other arrangements, business/property character, return line, timing and basis until actual rights and sources are bound; no universal line 13000 or receipt rule. [CRA mining/staking](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html).
- **Mining** — CRA distinguishes business and hobby; business income timing is when earned. HOLD actual character, valuation/inventory/cost, expenses and any hobby zero-basis conclusion rather than deciding from scale alone. [CRA mining](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html).
- **Buying/selling a qualifying virtual payment instrument** — The qualifying VPI supply is an exempt financial service; not all crypto/token services qualify. Enacted in 2021 with relevant amendments deemed effective 18 May 2019. HOLD actual token rights/eligibility. [CRA GST/HST](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html); [enacted amendment](https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2021_23/page-12.html).
- **Using crypto to buy taxable goods** — GST/HST applies to the goods  _(ETA s.153; CRA — GST/HST and cryptocurrency)_
- **Period** — Ordinary minimum six years from the end of the **last** tax year to which records relate, with longer unfiled-return, objection/appeal and demand rules. Acquisition evidence can remain relevant through a later disposal. [ITA 230(4)-(8)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html).

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Tax | Income Tax -- Cryptocurrency / Digital Assets |
| Currency | CAD (all gains/income reported in CAD) |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | Income Tax Act (Canada), Sections 3, 9, 38, 39, 54 |
| Supporting guidance | CRA Guide T4037 (Capital Gains); IT-479R (archived -- Transactions in Securities); CRA crypto guidance page |
| Tax authority | Canada Revenue Agency (CRA) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.1; [version in frontmatter](https://github.com/openaccountants/openaccountants/blob/4c3707f5574c8751e2738fe7b4044ff067245e0a/skills/canada/ca-crypto-tax.md#L4) |

### Core Principle

- **Core Principle** — The CRA treats cryptocurrency as a commodity (not currency). Dispositions result in either a capital gain or business income depending on the taxpayer's circumstances.

### Capital Gains Inclusion Rate (2025)

**Capital Gains Inclusion Rate (2025)**

| Taxpayer | Inclusion Rate | Notes |
| --- | --- | --- |
| Individuals -- ordinary capital gains | 50% | No $250,000 breakpoint; specific statutory exceptions remain. [ITA 38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) |
| Individuals -- ordinary gains above the former proposed $250,000 breakpoint | 50% | Same ordinary rate; proposal cancelled 21 March 2025. [official announcement](https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase) |
| Corporations and trusts -- ordinary gains | 50% | Specific section 38 exceptions remain separate. [ITA 38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) |

**Important:** The proposed 66.67% increase was cancelled on 21 March 2025; the ordinary 2025 inclusion is 50% with no $250,000 breakpoint, subject to the specific statutory exceptions. [ITA 38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html); [dated official announcement](https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase).

### Federal Tax Rates (2025)

**Federal Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| Up to 57,375 | 14.5%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 57,375 through 114,750 | 20.5%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 114,750 through 177,882 | 26%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 177,882 through 253,414 | 29%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 253,414 | 33%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether capital or business income | HOLD character and resulting inclusion; a lower-tax default is not a legal finding. Even an isolated transaction may be an adventure in trade. [CRA character guidance](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html) |
| Unknown ACB | HOLD actual gain until records and applicable cost rules are bound; zero is not an established cost |
| Unknown acquisition date | No holding period benefit claimed |
| Unknown fair market value at acquisition | Obtain support for actual token/CAD value at the applicable time; HOLD a result without a defensible valuation |

## Section 2 -- Classification Rules

### 2.1 Capital Gains vs Business Income

**2.1 Capital Gains vs Business Income**

| Factor | Capital (Investor) | Business Income (Trader) |
| --- | --- | --- |
| Frequency of transactions | Occasional | High volume, systematic |
| Holding period | Extended (weeks/months/years) | Very short (minutes/hours/days) |
| Knowledge/expertise | General interest | Deep market knowledge, technical analysis |
| Time devoted | Part-time/casual | Significant daily commitment |
| Financing | Own capital | Leveraged/borrowed funds |
| Advertising/promotion | None | May promote activity |
| Nature of assets | Long-term hold for appreciation | Quick turnover for profit |
| Tax treatment | Ordinary capital inclusion 50%, subject to specific exceptions | Net business profit after allowable costs is fully included; gross proceeds are not all profit. [CRA transactions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html) |
| Loss treatment | Capital-loss application subject to actual statutory restrictions | HOLD actual deductibility and loss restrictions; business character alone does not prove an unrestricted offset. [CRA classification](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html) |

The CRA applies a factual test; these factors are indicators, not numerical safe harbours. An isolated transaction may still be business. HOLD unresolved character. [CRA transactions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html).

### 2.2 Disposition Events

A disposition occurs when:

**2.2 Disposition Events**

| Event | Disposition? |
| --- | --- |
| Sell crypto for CAD (or fiat) | Yes |
| Trade crypto for another crypto | Yes -- barter transaction |
| Use crypto to purchase goods/services | Yes -- at FMV |
| Gift crypto | Ordinary ownership gift is a disposition; HOLD actual FMV/spousal/trust rollover conditions as stated above. [CRA transactions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html) |
| Donate crypto to registered charity | No general zero-inclusion exception for ordinary cryptocurrency merely because the recipient is a qualified donee. Apply actual property/gift conditions; HOLD receipt valuation/credit and any specific exception. [ITA 38(a)-(a.3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) |
| Transfer between own wallets | No -- same beneficial owner |
| Death of taxpayer | HOLD actual section 70(5)/(6) result and beneficiary basis until operative conditions are read and case facts bound; see 6.6 |

### 2.3 Adjusted Cost Base (ACB) Tracking

- **ACB calculation method** — The ACB is calculated using the weighted average cost method (mandatory for identical properties under ITA s. 47).  _(ITA s. 47)_
- **ACB per unit** — Remaining total **adjusted cost** of identical capital units held ÷ those units, after earlier dispositions and applicable adjustments; not lifetime gross purchase cost divided by current holdings. [ITA 47](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html).

**Potential ACB components: HOLD actual fee purpose, payment asset, adjustments and duplication. An embedded spread is not added again to an amount already including it. No universal own-transfer/network-fee rule was verified.**

**Elements included in ACB**

| Element Included in ACB | Example |
| --- | --- |
| Purchase price in CAD | Amount paid on exchange |
| Transaction/exchange fees on purchase | Coinbase fee, spread cost |
| Transfer fees (incoming) | Network/gas fees to acquire |

- **Partial disposition calculation** — When a partial disposition occurs: - Proceeds of disposition = FMV in CAD at time of sale - ACB of disposed units = (Total ACB ÷ total units) × units sold - Capital gain/loss = Proceeds − ACB of disposed units − disposition costs

### 2.4 Superficial Loss Rule (ITA s. 40(2)(g)(i))

- **Superficial loss rule** — Both the acquisition window (30 days before through 30 days after disposal) and ownership/right-to-acquire at its end matter, including applicable affiliated-person facts. HOLD actual denial/exclusions and ACB adjustment; an acquisition in the window alone is insufficient, and ACB recovery is not universal. [CRA superficial-loss passage](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html).

### 2.5 Staking Rewards

**2.5 Staking Rewards**

| Treatment | Detail |
| --- | --- |
| Centralized-exchange rewards | Generally income when credited to the platform wallet, within the CRA guidance's scope. [CRA staking](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html) |
| Other arrangements / amount / timing | HOLD actual rights, income character, recognition time and valuation; do not generalize platform guidance to every protocol |
| Basis of received tokens | HOLD applicable cost/inventory/basis adjustments; no universal equal-FMV ACB rule is certified |
| Business / passive reporting | Determine actual business/property/other character and form route; HOLD a generic line 13000 conclusion |

### 2.6 Mining

**2.6 Mining**

| Scenario | Treatment |
| --- | --- |
| Hobby mining investigation | HOLD character, cost and later-disposal treatment; no universal $0 ACB source was read. Scale alone does not settle character. [CRA mining](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html) |
| Business mining investigation | CRA uses income when earned; HOLD actual character, valuation/inventory, allowable costs and recognition. GST/HST mining regime is a separate test, not automatic registration. [CRA mining](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html); [CRA GST/HST](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html) |

### 2.7 Airdrops and Hard Forks

**2.7 Airdrops and Hard Forks**

| Type | Treatment |
| --- | --- |
| Airdrop (no consideration given) | HOLD rights, consideration, income source, timing and basis; no universal zero cost or income rule was verified |
| Hard fork (new token from existing chain) | HOLD actual rights, cost and tax treatment; no universal zero-cost acquisition rule was verified |
| Airdrop requiring action (governance, claim) | HOLD actual contractual rights, consideration and income source; action plus value does not establish a universal receipt-income rule |

### 2.8 GST/HST on Crypto

**2.8 GST/HST on Crypto**

| Transaction | GST/HST Implication |
| --- | --- |
| Purchase/sale of a qualifying VPI | Exempt financial service within the actual VPI definition, not every crypto/utility/security/NFT token. HOLD token eligibility. [CRA GST/HST](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html) |
| Using crypto for taxable goods/services | Underlying supply can remain taxable; establish its value at transaction time. [CRA GST/HST](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html) |
| Mining activity | CRA describes section 188.2's generally noncommercial regime effective 5 February 2022, with known-recipient exceptions. HOLD actual activity, recipient/conditions and credits; income-tax business status is distinct. [CRA mining regime](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html) |
| Sale of mined/staked tokens | Apply actual token/VPI and supply rules separately from the mining activity; no universal exemption |
| Input costs | HOLD commercial-activity, mining regime and credit entitlement; financial-service shorthand is insufficient |
| Platform/exchange fees | HOLD actual service, supply/financial-service and registration rules; no universal taxable-fee treatment was verified |

## Section 3 -- Transaction Pattern Library

These labels are candidate intake patterns. HOLD tax classification, beneficial ownership, gross/net values, fee purpose and contract facts; bank/exchange labels do not decide a legal outcome.

### 3.1 Common Exchange Patterns (Canadian Exchanges)

**3.1 Common Exchange Patterns (Canadian Exchanges)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NEWTON BUY / SHAKEPAY BUY | Acquisition | Bind actual acquisition cost; do not add an already-included spread twice |
| BITBUY PURCHASE / COINSMART BUY | Acquisition | ACB = CAD paid + any trading fee |
| KRAKEN BUY (CAD pair) | Acquisition | ACB = CAD equivalent + fee |
| WEALTHSIMPLE CRYPTO BUY | Acquisition | Bind actual acquisition cost and whether spread is already included |
| SELL ORDER (any exchange) | Disposition | Proceeds = CAD received |
| CONVERT / SWAP / TRADE | Disposition + acquisition | Two legs: dispose of A, acquire B |
| CAD WITHDRAWAL | Not taxable | Already sold |
| CAD DEPOSIT | Not taxable | Funding account |

### 3.2 Income Events

**3.2 Income Events**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STAKING REWARD | HOLD actual character/route | Centralized-platform crediting guidance has limited scope; see 2.5 |
| MINING PAYOUT | HOLD actual earned income/cost/character | Scale and payout label alone are insufficient; see 2.6 |
| REFERRAL BONUS (crypto) | HOLD source/contract/character | No universal receipt-income rule verified |
| EARN / LENDING INTEREST | HOLD source/contract/rights | Determine actual recognition, basis and return route |
| CASHBACK REWARD (crypto) | HOLD rebate/reward/contract treatment | A label does not establish taxable income |

### 3.3 Non-Taxable Movements

**3.3 Non-Taxable Movements**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER TO COLD WALLET | No tax event | Same beneficial owner |
| TRANSFER BETWEEN EXCHANGES | No ownership disposal only if same beneficial owner | HOLD actual fee treatment and payment asset; no universal ACB addition/deduction |
| FIAT DEPOSIT / WITHDRAWAL | No tax event | Cash movement |

## Section 4 -- Computation Method

### Step 1: Classify Activity

- **Step 1** — Determine if taxpayer is investor (capital gains) or trader (business income).

### Step 2: Build ACB Ledger

- **Step 2** — For identical capital properties, maintain remaining adjusted cost and units across wallets after acquisitions, dispositions and adjustments; HOLD business inventory and unresolved fees/basis. [ITA 47](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html).

### Step 3: Calculate Gain/Loss per Disposition

- **Step 3** — Proceeds (CAD FMV) − ACB of disposed units − selling costs = gain or loss.

### Step 4: Check Superficial Loss Rule

- **Step 4** — Deny any loss where you or an affiliated person reacquired the same crypto within the 30-day window and still hold it at the end of that period.

### Step 5: Apply Inclusion Rate

- **Step 5** — Ordinary capital gains: 50% inclusion, subject to specific section 38 exceptions, with no $250,000 breakpoint. Net business profit after allowable costs is fully included. HOLD unresolved character and adjustments. [ITA 38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html); [CRA transactions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html).

### Step 6: Report Staking/Mining/Airdrop Income

- **Step 6** — Separately investigate rewards, mining and airdrops; bind actual income source, timing, valuation, basis and reporting route. HOLD unresolved outcomes; not every labelled receipt has a universal tax treatment.

### Step 7: File

- **Step 7** — Capital reporting uses Schedule 3 and business reporting T2125 within the CRA guidance scope. HOLD actual passive/reward/lending/airdrop character and return line; do not send every non-business receipt to line 13000. [CRA reporting](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html).

## Section 5 -- Record-Keeping Requirements

CRA guidance supports these transaction and wallet/cost records. This is not a claim that each workpaper field has an identical standalone statutory-form requirement. [CRA records](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html).

**Section 5 -- Record-Keeping Requirements**

| Record | Mandatory |
| --- | --- |
| Date and time of each transaction | Yes |
| Type of transaction (buy/sell/trade/transfer) | Yes |
| Amount of crypto involved | Yes |
| FMV in CAD at time of transaction | Yes |
| Exchange or platform used | Yes |
| Wallet addresses involved | Yes |
| Running ACB calculation | Yes |
| Purpose of transaction | Yes |

- **Retention** — Ordinary minimum six years from the end of the **last** taxation year to which records relate; unfiled returns, objections/appeals and ministerial demands can require longer. Do not discard acquisition evidence six years after purchase if it supports a later disposal. HOLD destruction until actual retention conditions are established. [ITA 230(4)-(8)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html).

## Section 6 -- Edge Cases

### 6.1 Crypto-to-Crypto Swaps

- **Crypto-to-Crypto Swaps** — Each swap is a barter transaction. The disposition of crypto A is at the FMV of crypto B received (or FMV of A given up, whichever is more readily determinable). Must calculate gain/loss on A and establish ACB for B.

### 6.2 DeFi Lending

- **DeFi Lending** — HOLD deposit/withdrawal disposition, reacquisition and yield character pending actual beneficial rights, protocol terms and source treatment. A default workflow is not a legal ruling; no complete protocol-specific official source was read.

### 6.3 NFTs

- **NFTs** — HOLD actual business inventory, capital, personal-use and token-rights treatment; do not assume every NFT follows one generic crypto rule. Ordinary disposition principles do not verify exhaustive NFT treatment.

### 6.4 Wrapped Tokens

- **Wrapped Tokens** — HOLD whether the actual wrapping changes beneficial rights and constitutes a disposition. If a capital disposition is assumed, equal exchanged FMVs do **not** establish zero gain: proceeds still differ from original ACB. Conditional diagnostic: original ACB $1,000, assumed proceeds $2,000 and no selling costs give a $1,000 gain, with ordinary taxable capital gain $500. This does not decide whether any specific wrap is a disposition. [CRA capital formula](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ordinary inclusion](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html).

### 6.5 Emigration from Canada

- **Emigration from Canada** — Do not deem every crypto asset sold or payment automatically due on departure. CRA lists exclusions, including qualifying Canadian permanent-establishment business property and qualifying pre-immigration/inherited property for short-term residents. A payment-deferral election may be available subject to conditions/security. HOLD actual residency history, property status, exclusions, reporting and deferral before final use. [CRA departure rules](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html).

### 6.6 Death

- **Death** — Preserve the section 70(5) FMV-disposition/beneficiary-basis and 70(6) spousal/trust-rollover investigations. **HOLD actual result:** complete operative residency, vesting and trust conditions were not read; no blanket FMV basis or rollover is certified.

## Section 7 -- Prohibitions

- NEVER choose capital character just because its inclusion is lower; bind actual facts.
- NEVER apply the superseded 66.67% proposal to ordinary 2025 capital gains; apply section 38's actual exceptions separately.
- NEVER use specific identification instead of the applicable identical-capital-property average cost; do not generalize it to every business-inventory case.
- NEVER deny a superficial loss solely for a repurchase in the window or promise universal ACB recovery; apply all conditions.
- NEVER treat a beneficial-ownership crypto swap as a non-event merely because no fiat was received.
- NEVER claim unrestricted business losses without actual character and deduction/loss conditions.
- NEVER equate income-tax mining business with GST/HST commercial activity or universal VPI eligibility.
- NEVER assume airdrops, hobby rewards or missing ACB have universal zero cost or receipt-income treatment.
- NEVER omit a verified mining/staking income item, but use its actual earned/credited recognition and character; no universal receipt-time rule.
- NEVER present estimates or held outcomes as definitive filing results.

### Conditional arithmetic diagnostics

The baseline had no numeric case inputs to replace. These two diagnostics exercise the existing capital-formula/ACB topics. They assume identical capital property, established costs and no special adjustments; the wrap diagnostic assumes a disposition only to test its old zero-gain conclusion. Actual character, rights and tax treatment remain held. [CRA formula](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html); [ITA 47](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html).

```oa-check
name: Conditional wrapped-token disposition is not necessarily zero gain
inputs:
  original_acb: 1000
  assumed_proceeds: 2000
  selling_costs: 0
steps:
  - capital_gain: assumed_proceeds - original_acb - selling_costs
  - ordinary_taxable_capital_gain: capital_gain * 0.5
expected:
  capital_gain: 1000
  ordinary_taxable_capital_gain: 500
```

```oa-check
name: Conditional identical-capital-property average cost and partial disposal
inputs:
  first_units: 2
  first_total_cost: 1000
  second_units: 1
  second_total_cost: 800
  units_sold: 1
  assumed_proceeds: 900
  selling_costs: 0
steps:
  - total_units: first_units + second_units
  - total_adjusted_cost: first_total_cost + second_total_cost
  - average_acb: total_adjusted_cost / total_units
  - disposed_acb: average_acb * units_sold
  - capital_gain: assumed_proceeds - disposed_acb - selling_costs
  - remaining_units: total_units - units_sold
  - remaining_acb: total_adjusted_cost - disposed_acb
  - ordinary_taxable_capital_gain: capital_gain * 0.5
expected:
  total_units: 3
  total_adjusted_cost: 1800
  average_acb: 600
  disposed_acb: 600
  capital_gain: 300
  remaining_units: 2
  remaining_acb: 1200
  ordinary_taxable_capital_gain: 150
```

## Sources

Reuse the completed 21 November 2026 reads after confirming the baseline blob is unchanged. The 25 November follow-ups below are bounded quote/provenance checks for the three existing non-table defects, not a repeated whole-skill audit. No complete Budget PDF or whole Income Tax Act read is claimed.

| Primary source | Completed read scope | Read date |
| --- | --- | --- |
| [ITA 38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) | Ordinary half inclusion and specific zero-inclusion exceptions; no general ordinary-crypto donation exception. Follow-up (a)-(a.3) read; short exception excerpt: “a share, debt obligation or right listed on a designated stock exchange” | 2026-11-21; bounded follow-up 2026-11-25 |
| [Official cancellation announcement](https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase) | Dated 21 March 2025 cancellation; the superseded January deferral does not govern the ordinary rule | 2026-11-21 |
| [CRA 2025 annual rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) | Annual table and transition footnote, reused T2125 receipt: “making the tax rate 14.5% for 2025” | 2026-11-21 |
| [CRA individual dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) | Ordinary 2025 return deadlines in 2026, reused completed deadline work; actual exceptions still require binding | 2026-11-21 |
| [CRA crypto transactions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html) | Capital/business character, isolated adventures in trade, dispositions and capital/business reporting; actual individual character not certified | 2026-11-21 |
| [ITA 47](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html) | Identical capital-property average adjusted cost; not a universal inventory rule | 2026-11-21 |
| [CRA T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html) | Relevant identical-property, formula and superficial-loss passages; bounded formula follow-up: proceeds less ACB and selling costs. Input-label excerpt: “the adjusted cost base (ACB)” | 2026-11-21; bounded formula follow-up 2026-11-25 |
| [CRA mining/staking](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html) | Business/hobby and earned/centralized-platform-crediting timing. No universal protocol characterization, return line or zero-cost hobby rule | 2026-11-21 |
| [CRA crypto GST/HST](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/gst-hst-crypto-transactions.html) | Full page including qualifying VPI, underlying supplies, mining regime and known-recipient exceptions; no universal token/fee conclusion | 2026-11-21 |
| [2021 enacted VPI amendment](https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2021_23/page-12.html) | Enactment and 18 May 2019 deemed commencement read; July 2026 draft is not treated as enacted authority | 2026-11-21 |
| [ITA 230](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html) | Subsections (4)-(8), last relevant year and longer unfiled/objection/appeal/demand retention rules | 2026-11-21 |
| [CRA crypto records](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html) | Full transaction/wallet/cost-record guidance; field list is not claimed as identical standalone statutory forms | 2026-11-21 |
| [CRA departure guidance](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html) | Exclusions and deferral conditions read. Bounded follow-up deemed-disposition exclusions plus deferral deadline/security: “Some exceptions are”. Actual case remains held | 2026-11-21; bounded follow-up 2026-11-25 |

**Not yet confirmed:** full gift/spouse/death rollover conditions, actual capital/business character and loss availability, unknown/adjusted cost and fee treatment, superficial-loss/ACB exceptions, actual staking/mining/airdrop/hard-fork/rebate/lending character and basis/line, token/VPI/service and mining-regime eligibility, DeFi/wrapping beneficial rights, exhaustive NFT treatment, and actual departure exclusions/reporting/deferral. These holds prevent final use of affected conclusions. Six contradicted historical ledger groups were corrected; neither forty grouped checks nor passing arithmetic constitute a census of every fact in this skill.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
