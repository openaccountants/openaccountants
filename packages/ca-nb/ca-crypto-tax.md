---
name: ca-crypto-tax
description: Use this skill whenever asked about Canadian cryptocurrency taxation. Trigger on phrases like "crypto tax Canada", "CRA crypto", "Bitcoin capital gains Canada", "crypto business income CRA", "adjusted cost base crypto", "ACB crypto", "mining tax Canada", "staking tax Canada", "GST HST crypto", "crypto inclusion rate Canada", or any question about how cryptocurrency is taxed by the CRA. This skill covers capital gains vs business income treatment, the 50% inclusion rate, ACB tracking, mining/staking as business income, GST/HST on crypto payments, and record-keeping requirements. ALWAYS read this skill before touching any Canadian crypto tax work.
version: "1.0"
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Edgar Lautsyus
review_status: current
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CA Crypto Tax

## Canada Crypto Tax -- Capital Gains & Business Income Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Crypto Tax (CA)

- **CRA treatment** — Commodity (not currency)  _(CRA — Cryptocurrency and your income tax obligations — canada.ca)_
- **Cost basis method** — Weighted average cost (mandatory under ITA s.47)  _(ITA s.47; CRA — Adjusted cost base (ACB) — canada.ca)_
- **First $250K of net gains** — 50% inclusion — applies to ALL net capital gains; there is no $250K breakpoint (the proposed 66.67% increase was cancelled March 21, 2025)  _(ITA s.38(a); CRA — Capital gains — canada.ca)_
- **Above $250K** — 50% inclusion — same rate as below $250K; the proposed 66.67% increase was cancelled March 21, 2025 and Budget 2025 confirmed the cancellation  _(PM Carney announcement March 21, 2025 (pmc.gc.ca); Budget 2025 (canada.ca); CRA — Cancellation of proposed capital gains inclusion rate increase — canada.ca)_
- **Corporations/trusts** — The 66.67% rate for corporations/trusts was also CANCELLED. The 50% inclusion rate applies to all capital gains for corporations and most trusts in 2025. Change to: '50% on all gains — the proposed 66.67% rate was cancelled.'  _(PM Carney announcement March 21, 2025; Budget 2025 (canada.ca); CRA capital gains cancellation notice)_
- **Sell for fiat** — YES — disposition  _(CRA — crypto guidance; ITA s.39)_
- **Crypto-to-crypto swap** — YES — barter transaction  _(CRA — crypto guidance; ITA s.39)_
- **Purchase goods/services** — YES — at FMV  _(CRA — crypto guidance)_
- **Gift crypto** — Deemed disposition at FMV — except a transfer to a spouse/common-law partner (or qualifying spousal trust), which rolls over at ACB unless the taxpayer elects out (ITA s.73)  _(ITA s.69(1)(b))_
- **Transfer between own wallets** — NO — same beneficial owner  _(CRA — crypto guidance)_
- **Death** — Deemed disposition at FMV (s.70(5)) — except a rollover to a surviving spouse/common-law partner or qualifying spousal trust, which defers the gain (s.70(6))  _(ITA s.70(5))_
- **Window** — 30 days before to 30 days after the disposition — AND you or an affiliated person must still own (or have a right to acquire) the same or identical property at the end of that period (s.54; loss denied under s.40(2)(g)(i))  _(ITA s.40(2)(g); ITA s.54 (definition of superficial loss))_
- **Effect** — Loss denied; added to ACB of repurchased property  _(ITA s.53(1)(f))_
- **Staking — active business** — T2125 business income at FMV  _(ITA s.9; CRA — crypto guidance)_
- **Staking — passive** — Commonly other income (line 13000) at FMV when received, but CRA has issued no definitive staking guidance — characterization and timing are facts-dependent and can be business income  _(ITA s.12(1)(c); CRA — crypto guidance)_
- **Mining — business scale** — Business income at FMV; expenses deductible  _(ITA s.9; CRA — crypto guidance)_
- **Mining — hobby** — $0 ACB; CGT on disposition  _(CRA — crypto guidance)_
- **Buying/selling crypto for fiat** — No GST/HST for a 'virtual payment instrument' (BTC/ETH-type; exempt financial instrument under the ETA since 2021); utility or security tokens failing the VPI definition can be taxable supplies — analyse the token type  _(ETA Schedule V Part VII (financial services); CRA — GST/HST and cryptocurrency)_
- **Using crypto to buy taxable goods** — GST/HST applies to the goods  _(ETA s.153; CRA — GST/HST and cryptocurrency)_
- **Period** — 6 years from end of tax year  _(ITA s.230(4))_

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
| Skill version | 1.0 |

### Core Principle

- **Core Principle** — The CRA treats cryptocurrency as a commodity (not currency). Dispositions result in either a capital gain or business income depending on the taxpayer's circumstances.

### Capital Gains Inclusion Rate (2025)

**Capital Gains Inclusion Rate (2025)**

| Taxpayer | Inclusion Rate | Notes |
| --- | --- | --- |
| Individuals -- first $250,000 of net capital gains | 50% | Standard inclusion |
| Individuals -- gains above $250,000 | 50% | Same rate as first $250K; the proposed 66.67% increase was cancelled March 21, 2025 |
| Corporations and trusts | 50% on all gains | The proposed 66.67% rate was cancelled March 21, 2025 |

**Important:** The proposed increase to 66.67% above $250K was cancelled March 21, 2025 (confirmed in Budget 2025). The 50% inclusion rate applies to all net capital gains for individuals in 2025 — no $250K threshold distinction.

### Federal Tax Rates (2025)

**Federal Tax Rates (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 57,375 | 15% |
| 57,376 -- 114,750 | 20.5% |
| 114,751 -- 158,468 | 26% |
| 158,469 -- 220,000 | 29% |
| 220,001+ | 33% |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether capital or business income | Treat as capital gains (lower inclusion) until evidence of business activity |
| Unknown ACB | $0 (maximum gain) -- obtain records |
| Unknown acquisition date | No holding period benefit claimed |
| Unknown fair market value at acquisition | Use reputable exchange rate at date/time |

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
| Tax treatment | 50% inclusion | 100% income (fully taxable) |
| Loss treatment | Capital losses (only offset gains) | Business losses (offset all income) |

The CRA applies a holistic test. No single factor is determinative.

### 2.2 Disposition Events

A disposition occurs when:

**2.2 Disposition Events**

| Event | Disposition? |
| --- | --- |
| Sell crypto for CAD (or fiat) | Yes |
| Trade crypto for another crypto | Yes -- barter transaction |
| Use crypto to purchase goods/services | Yes -- at FMV |
| Gift crypto | Yes -- FMV (spousal transfers roll over at ACB unless elected out) |
| Donate crypto to registered charity | Yes -- but donation receipt at FMV; no capital gain if donated to qualified donee (proposed) |
| Transfer between own wallets | No -- same beneficial owner |
| Death of taxpayer | Yes -- FMV (spousal/spousal-trust rollover defers the gain, s.70(6)) |

### 2.3 Adjusted Cost Base (ACB) Tracking

- **ACB calculation method** — The ACB is calculated using the weighted average cost method (mandatory for identical properties under ITA s. 47).  _(ITA s. 47)_
- **ACB per unit** — ACB per unit = Total cost of all units acquired ÷ Total units held  _(ITA s. 47)_

**Elements included in ACB**

| Element Included in ACB | Example |
| --- | --- |
| Purchase price in CAD | Amount paid on exchange |
| Transaction/exchange fees on purchase | Coinbase fee, spread cost |
| Transfer fees (incoming) | Network/gas fees to acquire |

- **Partial disposition calculation** — When a partial disposition occurs: - Proceeds of disposition = FMV in CAD at time of sale - ACB of disposed units = (Total ACB ÷ total units) × units sold - Capital gain/loss = Proceeds − ACB of disposed units − disposition costs

### 2.4 Superficial Loss Rule (ITA s. 40(2)(g)(i))

- **Superficial loss rule** — If you sell crypto at a loss and repurchase the same crypto (or identical property) within 30 days before or after the sale (or your affiliated person acquires it), the loss is denied. The denied loss is added to the ACB of the repurchased property.  _(ITA s. 40(2)(g)(i))_

### 2.5 Staking Rewards

**2.5 Staking Rewards**

| Treatment | Detail |
| --- | --- |
| CRA position | Business income or property income (assessable when received) |
| Amount | FMV in CAD at date/time of receipt |
| ACB of received tokens | FMV at receipt (becomes cost base for future disposition) |
| If part of active business | Report on T2125 (business income) |
| If passive/property income | Report as other income (Line 13000) |

### 2.6 Mining

**2.6 Mining**

| Scenario | Treatment |
| --- | --- |
| Hobby mining (small-scale, no profit intent) | Acquired at $0 ACB; CGT on disposition |
| Business mining (significant operations) | Business income at FMV when mined; expenses deductible; GST/HST registrant obligations |

### 2.7 Airdrops and Hard Forks

**2.7 Airdrops and Hard Forks**

| Type | Treatment |
| --- | --- |
| Airdrop (no consideration given) | CRA: income at FMV if received for services or as reward; otherwise $0 ACB |
| Hard fork (new token from existing chain) | $0 ACB; taxable on disposition |
| Airdrop requiring action (governance, claim) | Income at FMV if value exists |

### 2.8 GST/HST on Crypto

**2.8 GST/HST on Crypto**

| Transaction | GST/HST Implication |
| --- | --- |
| Purchasing crypto with fiat | No GST/HST (financial instrument) |
| Selling crypto for fiat | No GST/HST |
| Using crypto to purchase taxable goods/services | GST/HST applies to the goods/services (crypto is consideration) |
| Mining/staking as business -- selling mined crypto | Exempt financial service (no GST/HST on sale of crypto itself) |
| Mining/staking as business -- input costs | ITC may be restricted (financial services supplier rules) |
| Crypto exchange services (platform fees) | Subject to GST/HST as a taxable supply |

## Section 3 -- Transaction Pattern Library

### 3.1 Common Exchange Patterns (Canadian Exchanges)

**3.1 Common Exchange Patterns (Canadian Exchanges)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NEWTON BUY / SHAKEPAY BUY | Acquisition | ACB = CAD paid + spread (no explicit fee on some platforms) |
| BITBUY PURCHASE / COINSMART BUY | Acquisition | ACB = CAD paid + any trading fee |
| KRAKEN BUY (CAD pair) | Acquisition | ACB = CAD equivalent + fee |
| WEALTHSIMPLE CRYPTO BUY | Acquisition | ACB = CAD paid + spread |
| SELL ORDER (any exchange) | Disposition | Proceeds = CAD received |
| CONVERT / SWAP / TRADE | Disposition + acquisition | Two legs: dispose of A, acquire B |
| CAD WITHDRAWAL | Not taxable | Already sold |
| CAD DEPOSIT | Not taxable | Funding account |

### 3.2 Income Events

**3.2 Income Events**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STAKING REWARD | Income (business or property) | FMV at receipt |
| MINING PAYOUT | Income (if business) or $0 ACB (if hobby) | Determine mining scale |
| REFERRAL BONUS (crypto) | Income | FMV at receipt |
| EARN / LENDING INTEREST | Income (property income) | FMV at receipt |
| CASHBACK REWARD (crypto) | Income | FMV at receipt |

### 3.3 Non-Taxable Movements

**3.3 Non-Taxable Movements**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER TO COLD WALLET | No tax event | Same beneficial owner |
| TRANSFER BETWEEN EXCHANGES | No tax event | Network fees add to ACB or deductible expense |
| FIAT DEPOSIT / WITHDRAWAL | No tax event | Cash movement |

## Section 4 -- Computation Method

### Step 1: Classify Activity

- **Step 1** — Determine if taxpayer is investor (capital gains) or trader (business income).

### Step 2: Build ACB Ledger

- **Step 2** — Track every acquisition: weighted average cost across all units of each crypto.

### Step 3: Calculate Gain/Loss per Disposition

- **Step 3** — Proceeds (CAD FMV) − ACB of disposed units − selling costs = gain or loss.

### Step 4: Check Superficial Loss Rule

- **Step 4** — Deny any loss where you or an affiliated person reacquired the same crypto within the 30-day window and still hold it at the end of that period.

### Step 5: Apply Inclusion Rate

- **Step 5** — - Capital gains: 50% on all net capital gains (individuals) — the proposed 66.67% rate above $250K was cancelled March 21, 2025 - Business income: 100% taxable

### Step 6: Report Staking/Mining/Airdrop Income

- **Step 6** — Separately from capital gains -- as business or property income.

### Step 7: File

- **Step 7** — - Capital gains: Schedule 3 - Business income: T2125 (Statement of Business Activities) - Other income: Line 13000

## Section 5 -- Record-Keeping Requirements

CRA requires:

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

- **Retention** — 6 years from the end of the tax year to which they relate.

## Section 6 -- Edge Cases

### 6.1 Crypto-to-Crypto Swaps

- **Crypto-to-Crypto Swaps** — Each swap is a barter transaction. The disposition of crypto A is at the FMV of crypto B received (or FMV of A given up, whichever is more readily determinable). Must calculate gain/loss on A and establish ACB for B.

### 6.2 DeFi Lending

- **DeFi Lending** — Lending crypto to a DeFi protocol may be a disposition (if legal ownership transfers to the protocol). Conservative treatment: disposition at FMV when deposited, reacquisition when withdrawn. Interest/yield received is property income.

### 6.3 NFTs

- **NFTs** — Treated the same as other crypto assets. Acquisition = ACB. Sale = disposition. If creating NFTs as a business, profits are business income.

### 6.4 Wrapped Tokens

- **Wrapped Tokens** — Wrapping (e.g., ETH → WETH) is a grey area. Conservative treatment: disposition of ETH, acquisition of WETH at same FMV. No gain/loss but must track separately.

### 6.5 Emigration from Canada

- **Emigration from Canada** — Deemed disposition of all crypto at FMV on departure date. Capital gains tax applies on departure.  _(ITA s. 128.1)_

### 6.6 Death

- **Death** — Deemed disposition at FMV immediately before death (s.70(5)); capital gains included in the terminal return and the beneficiary acquires at FMV as their ACB. A rollover to a surviving spouse/common-law partner or qualifying spousal trust defers the gain (s.70(6)).

## Section 7 -- Prohibitions

- **Prohibitions** — - NEVER apply a higher inclusion rate than 50% — the proposed 66.67% rate above $250K was cancelled March 21, 2025; 50% applies to all gains in 2025 - NEVER use specific identification method for identical properties -- CRA requires weighted average (ITA s. 47) - NEVER ignore the superficial loss rule for repurchases within 30 days - NEVER treat crypto-to-crypto swaps as non-events -- each swap is a disposition - NEVER claim business losses without substantiating that the activity is a business (not capital) - NEVER ignore GST/HST obligations for crypto businesses - NEVER assume airdrops are always tax-free -- determine if income character exists - NEVER omit staking/mining income -- it is taxable when received - NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
