---
name: crypto-tax-workflow-base
description: >
  Universal workflow base for cryptocurrency and digital asset taxation worldwide.
  Covers classification (capital vs income), cost basis tracking, DeFi protocols,
  NFTs, mining, staking, airdrops, hard forks, and reporting obligations.
  Loaded alongside country-specific crypto tax skills. Does not contain any
  jurisdiction-specific rates or thresholds.
version: 1.1
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-11-14
tax_year: 2026
type: cross-country-method
tier: 2
domain: crypto
---

# Crypto Tax Workflow Base v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

Universal workflow for cryptocurrency and digital asset tax compliance. Defines the classification framework, cost basis methods, transaction type taxonomy, and output format that every country-specific crypto tax skill builds on. Country tax rates and annual filing thresholds come from the country skill. The UK and Canadian sections below demonstrate why classification and matching cannot be defaulted across countries.

**Must be loaded with at least one country-specific crypto tax skill** (e.g., `uk-crypto-tax.md`, `us-crypto-tax.md`). This file alone cannot produce a tax liability or a filing. It can produce a reconciled transaction ledger and a list of the country-specific decisions still needed. Coverage is the shared method as checked on 14 November 2026, not a certification of every country's 2026 tax rules.

---

## Ask the client first

The table is the complete document request. First establish the taxpayer, residence, relevant countries, tax period, ownership/capacity and whether the activity is a business or investment. Record any change during the year. A wallet or exchange location alone does not establish residence.

### Onboarding: what to collect

Before computing anything, obtain ALL of the following:

| # | Required input | Why |
|---|----------------|-----|
| 1 | Which digital assets are held (BTC, ETH, stablecoins, NFTs, DeFi tokens, memecoins) | Determines classification rules |
| 2 | Transaction history source : exchange CSVs, on-chain wallet exports, DeFi protocol records | Raw data for computation |
| 3 | Acquisition dates and costs per lot in local fiat equivalent | Cost basis tracking |
| 4 | All disposal events : sells, swaps (crypto-to-crypto = disposal in most jurisdictions), gifts, payments | Taxable event identification |
| 5 | Mining/staking/yield farming/liquidity rewards : amounts received, FMV at receipt | Income recognition |
| 6 | Airdrops and hard forks : what received, when, whether any action was required | Classification varies by jurisdiction |
| 7 | NFT activity : minting costs, sales proceeds, royalties received, platform fees | Separate reporting in some jurisdictions |
| 8 | Cost basis method elected : FIFO, LIFO, specific ID, average cost | Country skill determines which are permitted |
| 9 | Prior year losses carried forward | Offset computation |
| 10 | Exchange accounts : domestic and foreign | FBAR/foreign reporting obligations |

If any of inputs 1-4 are missing, STOP and request them. Cannot compute without transaction history and cost basis.

---

## The method, step by step

### Step 1: Reconcile before classifying

Reconcile opening units plus acquisitions and incoming transfers minus sales, spending, outgoing transfers and fees to closing units, for every asset and wallet. Match both sides of an own-wallet transfer so it is not counted as fresh income or as two disposals. Keep original timestamps, time zone, transaction hashes, original currency, valuation evidence and all exchange statements. Missing basis or missing receipts stay unresolved rather than becoming zero.

### Step 2: Transaction type taxonomy

Record the economic components separately. One transaction can contain a disposal, acquisition, reward and fee; forcing it into a single category can omit a taxable leg or count it twice. The categories below are investigation prompts. The country rule and actual beneficial ownership decide treatment, not the protocol label.

#### Candidate disposals (capital or business treatment must be established)

| Type | Description | Taxable event? |
|------|-------------|----------------|
| **Sell for fiat** | BTC → USD/EUR/GBP | Test disposal and capital versus business treatment under the actual country rule; no universal tax charge is asserted |
| **Crypto-to-crypto swap** | BTC → ETH | Yes in most jurisdictions (check country skill) |
| **Payment for goods/services** | Using crypto to buy something | Test barter/disposal and the separate supplier-income event; UK and Canadian rules below |
| **Gift** | Transferring to another person | Varies : some jurisdictions tax donor, some recipient, some neither |
| **Lost/stolen** | Permanently inaccessible | Varies : some allow capital loss, some don't |

#### Candidate income events (recognition and character are country-specific)

| Type | Description | When recognized |
|------|-------------|-----------------|
| **Mining** | Proof-of-work block rewards | Record when earned, controlled and received; business status and the country's recognition rule decide |
| **Staking** | Proof-of-stake validation rewards | When rewards credited (jurisdiction-dependent) |
| **Yield farming** | DeFi liquidity provision returns | Establish capital versus revenue, entitlement and the actual recognition event |
| **Airdrops** | Free tokens distributed | Establish service/conditions, business activity and entitlement; the UK does not automatically tax an unsolicited personal airdrop as income |
| **Hard forks** | New chain creates new tokens | Varies by jurisdiction : some at fork, some at first disposal |
| **Payment for services** | Employer/client pays in crypto | Establish employment versus business, when earned/received and valuation under the country rule |
| **Interest** | CeFi/DeFi lending returns | Establish the legal return and timing; a token return is not automatically legal interest or revenue |
| **Referral/bounty rewards** | Platform rewards | Inspect the service, conditions, control and country recognition rule |

#### Potential non-disposals (prove the relevant conditions)

| Type | Description | Note |
|------|-------------|------|
| **Transfer between own wallets** | Moving from exchange to hardware wallet | UK/Canada own-wallet examples below require continuing ownership; investigate fees separately |
| **Buying with fiat** | USD → BTC purchase | Record acquisition basis; any disposal of another asset or foreign currency and fees needs its own analysis |
| **Wrapping/unwrapping** | ETH → WETH | Do not assume continuing ownership or tax neutrality; inspect legal rights and the country rule |
| **Chain migration** | Token upgrade on same protocol | Inspect changed rights and the applicable reorganisation rule; no universal exemption |

### DeFi-specific events

| Type | Tax treatment | Complexity |
|------|--------------|------------|
| **Liquidity pool deposit** | Potentially a disposal (country-dependent) | High : impermanent loss not always deductible |
| **Liquidity pool withdrawal** | Potentially an acquisition + disposal | High |
| **Borrowing against crypto** | Check beneficial ownership, collateral and later liquidation separately | Medium, a loan label does not settle whether a disposal occurred |
| **Lending crypto** | May be a disposal or may retain ownership | High : jurisdiction-dependent |
| **Governance token rewards** | Establish why received, character and timing under the country rule | Medium |
| **Flash loans** | Reconcile borrowing, repayment, fees, swaps and realised profit independently; same-transaction repayment is not a tax exemption | Requires the actual protocol/country analysis |

---

## Step 3 : Cost basis methods

The country skill specifies which methods are permitted. Universal definitions:

| Method | How it works | Effect on tax |
|--------|-------------|---------------|
| **FIFO** (First In, First Out) | Oldest lots disposed first | In rising markets: higher gains (older = lower cost) |
| **LIFO** (Last In, First Out) | Newest lots disposed first | In rising markets: lower gains (newer = higher cost) |
| **Specific identification** | Taxpayer chooses which lot | Maximum flexibility : can minimize tax |
| **Average cost** | Total cost / total units | Simple but no lot-level optimization |
| **S104 pool** (UK-specific) | A separate pool for each qualifying fungible token type, after same-day and subsequent matching | Do not pool separately identifiable NFTs; apply the UK sequence below |

**No matching-method default.** FIFO, LIFO and specific identification are definitions, not elections offered by every country. Load the legally required matching or inventory method before calculating a disposal. The UK example below uses statutory matching ahead of pooling, not FIFO.

### Cost basis tracking rules

1. **Acquisition cost:** retain purchase price and each exchange, gas and transfer fee separately. Include only the costs the country permits, allocating dual-purpose fees once rather than automatically adding every charge.
2. **Crypto-to-crypto swaps:** record the outgoing asset and incoming asset separately, their transaction-date values and applicable allowable costs. Establish whether a disposal occurred and the country's new-basis rule; do not assume every protocol exchange has the same treatment.
3. **Staking/mining:** preserve the amount already brought into income and the recognition date. Establish the later disposal basis under the country rule so the same receipt is not taxed twice; do not assume the receipt date is the earning date for every business.
4. **Airdrops:** retain the service/conditions and any income already charged. Lack of an income charge does not establish a zero capital basis in every jurisdiction; obtain the actual basis rule before a later disposal.
5. **Hard forks:** obtain the country rule. The UK may split existing allowable costs between the original and new pools on a just and reasonable basis, rather than use either zero or receipt-date market value universally.
6. **Valuation and currency:** record the applicable tax currency and recognition/disposal-date value, source, trading pair, timestamp and conversion. Exchange statements and market feeds can be client valuation evidence, not tax-law authority. Do not choose a daily close where the actual transaction or country rule requires a different time/value; obtain the country's permitted method.

---

## Step 4 : Gain/loss computation

For each disposal:

```
Gain or Loss = Proceeds (FMV in local fiat) − Cost Basis − Allowable Fees
```

Then apply the country skill's rules for:
- **Holding period**: test only where the country makes it relevant. Do not apply a US-style short/long-term rate distinction to the UK; UK matching is a separate issue
- **Tax rate** : capital gains rate vs ordinary income rate
- **Exemptions** : annual exempt amount, de minimis thresholds, personal use exemptions
- **Loss offset** : which gains can losses offset? Carry-forward rules?
- **Wash sale / bed-and-breakfasting** : anti-avoidance rules on repurchasing after a loss

---

## Step 5 : Income computation

For each income event (mining, staking, airdrops, etc.):

```
Candidate receipt value = units received × supported unit value in the applicable tax currency
Taxable character and recognition date = the country rule applied to the actual facts
```

Country skill determines:
- Whether taxed as ordinary income, miscellaneous income, or a special category
- Whether business deductions apply (electricity for mining, hardware depreciation)
- Whether there's a de minimis threshold below which income is not taxable
- Self-employment tax / social contribution implications

---

## Step 6 : Reporting obligations

The following are reporting checks, not universal filing obligations. Confirm whether each applies to this taxpayer, country, asset and period before putting it in the filing schedule:

| Obligation | What to report |
|------------|---------------|
| Capital gains schedule | Every disposal: date acquired, date sold, proceeds, cost basis, gain/loss |
| Income schedule | Mining/staking/airdrop income with FMV at receipt |
| Foreign account and provider reporting | Determine actual foreign-property/account tests separately from a service provider's exchange-reporting duty; an exchange address alone does not establish FBAR, Form 8938 or DAC8 applicability |
| Digital asset question | Whether taxpayer transacted in digital assets during the year |
| Annual crypto return | Some jurisdictions require a separate crypto-specific filing |

---

## Country applications

### United Kingdom

For a UK individual holding tokens as investments, HMRC includes fiat sales, token swaps and spending within disposals; an own-wallet movement without loss of beneficial ownership is different. Gifts, spouses and charity require the actual exceptions. [CRYPTO22100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100).

Match qualifying fungible tokens acquired on the same day first, then acquisitions of the same type and capacity in the following **30 days**, then the section 104 pool. NFTs are separately identifiable and not pooled. This defeats a blanket FIFO default. [CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200).

Not every exchange or gas charge is allowable. Keep income deductions and capital costs separate, and allocate a fee relating to both assets justly once. A personal airdrop without service/conditions and outside a crypto trade may have no income charge. A hard fork can require splitting existing pool costs reasonably. [Allowable costs](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150), [airdrops](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250), [forks](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300).

For DeFi inspect the actual rights and whether a return is service remuneration or capital growth. A marketing label, regular return or single factor cannot alone decide. Ordinary reward/employment receipts and later disposals also need separate records; do not apply income twice to the same previously taxed value. [Nature of DeFi returns](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61214), [receipt and later disposal](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets).

### Canada

CRA separates business profits from capital gains using all the activity's facts, including dealing frequency, holding periods, knowledge, time, finance and the profit-making venture. Its disposition examples include swaps, purchases and gifts, while a transfer between the taxpayer's own wallets does not itself dispose of the asset. Keep Canadian-dollar proceeds, adjusted cost base and disposal costs distinct; obtain current inclusion/loss rules and return lines from `ca-crypto-tax` rather than copying an annual tax table here. [CRA dispositions and character](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html).

A mining business includes reward value when earned; centrally staked exchange rewards are generally income when credited to the platform wallet. Equipment and non-resident Canadian operations have separate questions. This is why neither a universal receipt-date rule nor an automatic capital label is safe. [CRA mining and staking](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html).

### Other countries

Load the current country's crypto method and primary law before selecting classification, matching, income recognition, fees, loss relief, exchange reporting or forms. The examples above do not export UK or Canadian rules to another country. If no readable current authority covers the actual protocol/right, preserve the ledger and refer that specific question.

## Worked cases

**UK pool, after the matching checks.** A UK individual holds four identical investment tokens with pooled allowable cost GBP 4,000 and sells one for GBP 1,500, paying an allowable disposal fee GBP 20. There are no same-day or following-30-day acquisitions, no business treatment and no other special rule. Pooled cost allocated is GBP 1,000; gain is GBP 480; remaining pool is three units costing GBP 3,000. This computes the gain, not the tax liability or an annual exemption. [Matching](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200); [costs](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150).

```oa-check
name: UK section 104 pool after matching, one disposal
inputs:
  opening_units: 4
  opening_cost: 4000
  disposed_units: 1
  proceeds: 1500
  allowable_disposal_fee: 20
steps:
  - allocated_cost: opening_cost * disposed_units / opening_units
  - gain: proceeds - allocated_cost - allowable_disposal_fee
  - closing_units: opening_units - disposed_units
  - closing_pool_cost: opening_cost - allocated_cost
expected:
  allocated_cost: 1000
  gain: 480
  closing_units: 3
  closing_pool_cost: 3000
```

**One event, income and a later disposal.** Assume the UK country analysis establishes GBP 600 of taxable reward income and the corresponding GBP 600 value against a later disposal. The same tokens later sell for GBP 750 with GBP 10 allowable disposal costs and no matching, business or other adjustments. The later gain is GBP 140, not GBP 740; total income and gain before any allowances is GBP 740, not GBP 1,340. These are invented facts demonstrating the reconciliation, not an election to recognise every DeFi return as income. [HMRC receipt and later disposal](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets).

```oa-check
name: Reward income and later gain do not double count receipt value
inputs:
  recognised_income: 600
  later_proceeds: 750
  allowable_disposal_fee: 10
steps:
  - later_gain: later_proceeds - recognised_income - allowable_disposal_fee
  - total_before_allowances: recognised_income + later_gain
  - incorrect_zero_basis_gain: later_proceeds - allowable_disposal_fee
  - overstatement_if_zero_basis: incorrect_zero_basis_gain - later_gain
expected:
  later_gain: 140
  total_before_allowances: 740
  overstatement_if_zero_basis: 600
```

## Step 7 : Output specification

Produce these artifacts:

### 1. Crypto transaction ledger
For every transaction in the period:

| Date | Type | Asset | Units | FMV (local) | Cost basis | Gain/Loss | Holding period | Tax treatment |
|------|------|-------|--------|-------------|-----------|-----------|----------------|---------------|

### 2. Capital gains summary
| Category | Short-term gains | Short-term losses | Long-term gains | Long-term losses | Net |
|----------|-----------------|-------------------|-----------------|------------------|-----|
| Crypto-to-fiat | | | | | |
| Crypto-to-crypto | | | | | |
| NFT sales | | | | | |
| DeFi disposals | | | | | |
| **Total** | | | | | |

### 3. Income summary
| Source | Recorded local-fiat receipt | Tax treatment |
|--------|-------------------|---------------|
| Mining rewards | | |
| Staking rewards | | |
| Airdrops | | |
| DeFi yield | | |
| Payment for services | | |
| **Total crypto income** | | |

### 4. Reviewer brief
- Cost basis method used and justification
- Assumptions made (with conservative default disclosed)
- FMV source used for valuations
- Foreign exchange reporting obligations triggered
- Any wash sale / anti-avoidance flags
- Items requiring professional judgment

---

## Boundary and exception table

Do not settle a legal ambiguity by choosing the treatment that appears to collect more tax. Continue supported reconciliation, put unresolved amounts in a separate schedule and withhold the affected tax conclusion.

### Facts that must remain unresolved

| Ambiguity | Conservative default |
|-----------|---------------------|
| Unknown acquisition cost | **STOP** : cannot compute without cost basis. Ask user. |
| Unknown holding period | Keep holding period unknown; identify the country rule and obtain acquisition evidence |
| Unknown whether income or capital | Keep character unresolved; investigate business/investment and the actual receipt |
| Unknown FMV at receipt | Obtain dated valuation evidence and the country's permitted conversion method |
| Unknown cost basis method | Apply no method until the country's mandatory matching/inventory rules are established |
| Airdrop, no clear service performed | Obtain actual conditions and country rule; no automatic income classification |
| Staking : unclear when rewards received | Determine when earned, credited, controlled and taxable under the actual rule; no invented early date |
| DeFi LP deposit : unclear if disposal | Inspect the contract/beneficial ownership and refer the unresolved tax treatment |
| Lost/stolen crypto : no evidence | No loss claim (cannot substantiate) |
| Crypto-to-crypto swap | Record both legs and withhold the affected tax conclusion where the country treatment is unresolved |

---

## Self-checks (run before delivering)

1. Every disposal has a computed cost basis (no blanks)
2. Crypto-to-crypto swaps have both legs recorded and the actual country disposal rule applied
3. Mining/staking character, recognition date and value follow the actual country rule, with income and later basis reconciled
4. FMV source is consistent across all transactions
5. Cost basis method is the same for all disposals of the same asset (no cherry-picking without specific ID election)
6. Foreign exchange reporting threshold checked
7. Annual crypto/digital asset question answered correctly
8. Wash sale / anti-avoidance rules applied where applicable
9. Prior year loss carryforward applied if available
10. All amounts in local fiat currency
11. Gas fees allocated to correct transaction (disposal fee vs acquisition cost)
12. NFTs treated correctly (collectibles rate if applicable)

---

## When to refuse or refer

| Trigger | Action |
|---------|--------|
| No transaction history available | STOP : cannot compute without data |
| Day trading as primary income with hundreds of trades and no CSV | STOP : manual entry impossible |
| DeFi protocol with unclear tax treatment and no country guidance | Flag the unresolved legal question for a reviewer; do not invent a taxable event or present a final tax figure |
| Crypto earned through illegal activity | REFUSE |
| Tax evasion planning ("how do I hide my crypto") | REFUSE |

---

## Disclaimer

This workflow base and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. Cryptocurrency taxation is rapidly evolving and many jurisdictions have unclear or changing rules. All outputs must be reviewed by a qualified professional before filing.


## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| HMRC CRYPTO22100. Read for disposal categories, continuing beneficial ownership and previously income-taxed amounts | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100 | 2026-11-14 |
| HMRC CRYPTO22200. Read for same-day and following-30-day matching, pools by token type and NFT exclusion | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200 | 2026-11-14 |
| HMRC CRYPTO22150. Read for permitted costs, income/capital duplication and fair allocation of swap fees | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22150 | 2026-11-14 |
| HMRC CRYPTO21250. Read for personal airdrops with no service/conditions versus trading/service rewards | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250 | 2026-11-14 |
| HMRC CRYPTO22300. Read for new hard-fork pools and just-and-reasonable allocation of original costs | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22300 | 2026-11-14 |
| HMRC CRYPTO61214. Read for capital/revenue factors and the warning that no single factor determines the return | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto61214 | 2026-11-14 |
| HMRC receipt guidance. Read for ordinary reward/employment receipts, records and capital gains on later appreciation | https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-receive-cryptoassets | 2026-11-14 |
| CRA income from crypto transactions. Read through official web view for dispositions, own-wallet movements, business/capital factors and gain computation; direct download timed out | https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html | 2026-11-14 |
| CRA mining and staking. Read through official web view for earned mining-business income, centrally staked credit timing, equipment and non-resident questions; direct download timed out | https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-mining-staking-activities.html | 2026-11-14 |

Not yet confirmed: current country-specific tax rates, exemptions, loss relief, foreign-account/provider-reporting scope and actual 2026 return editions are intentionally not certified by this shared method and must come from the relevant country skill and current authority. For any actual wrapping, chain migration, LP entry/exit, borrowing/liquidation, flash loan, governance/referral reward, NFT royalty or lost/stolen asset, establish the applicable country's legal rights, basis and recognition rule before a tax conclusion. No unresolved transaction is automatically taxed or exempted by a default here.
