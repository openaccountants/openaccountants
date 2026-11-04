---
name: crypto-tax-workflow-base
description: >
  Universal workflow base for cryptocurrency and digital asset taxation worldwide.
  Covers classification (capital vs income), cost basis tracking, DeFi protocols,
  NFTs, mining, staking, airdrops, hard forks, and reporting obligations.
  Loaded alongside country-specific crypto tax skills. Does not contain any
  jurisdiction-specific rates or thresholds.
version: 1.0
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-06-12
tier: 2
domain: crypto
---

# Crypto Tax Workflow Base v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

Universal workflow for cryptocurrency and digital asset tax compliance. Defines the classification framework, cost basis methods, transaction type taxonomy, and output format that every country-specific crypto tax skill builds on. No rates, no thresholds, no country-specific rules — those come from the country skill.

**Must be loaded with at least one country-specific crypto tax skill** (e.g., `uk-crypto-tax.md`, `us-crypto-tax.md`). This file alone cannot produce any output.

---

## Step 1 — Onboarding: what to collect

Before computing anything, obtain ALL of the following:

| # | Required input | Why |
|---|----------------|-----|
| 1 | Which digital assets are held (BTC, ETH, stablecoins, NFTs, DeFi tokens, memecoins) | Determines classification rules |
| 2 | Transaction history source — exchange CSVs, on-chain wallet exports, DeFi protocol records | Raw data for computation |
| 3 | Acquisition dates and costs per lot in local fiat equivalent | Cost basis tracking |
| 4 | All disposal events — sells, swaps (crypto-to-crypto = disposal in most jurisdictions), gifts, payments | Taxable event identification |
| 5 | Mining/staking/yield farming/liquidity rewards — amounts received, FMV at receipt | Income recognition |
| 6 | Airdrops and hard forks — what received, when, whether any action was required | Classification varies by jurisdiction |
| 7 | NFT activity — minting costs, sales proceeds, royalties received, platform fees | Separate reporting in some jurisdictions |
| 8 | Cost basis method elected — FIFO, LIFO, specific ID, average cost | Country skill determines which are permitted |
| 9 | Prior year losses carried forward | Offset computation |
| 10 | Exchange accounts — domestic and foreign | FBAR/foreign reporting obligations |

If any of inputs 1-4 are missing, STOP and request them. Cannot compute without transaction history and cost basis.

---

## Step 2 — Transaction type taxonomy

Every crypto transaction maps to exactly one of these types. The country skill determines the tax treatment of each.

### Disposals (potential capital gain/loss)

| Type | Description | Taxable event? |
|------|-------------|----------------|
| **Sell for fiat** | BTC → USD/EUR/GBP | Yes — always |
| **Crypto-to-crypto swap** | BTC → ETH | Yes in most jurisdictions (check country skill) |
| **Payment for goods/services** | Using crypto to buy something | Yes — disposal at FMV |
| **Gift** | Transferring to another person | Varies — some jurisdictions tax donor, some recipient, some neither |
| **Lost/stolen** | Permanently inaccessible | Varies — some allow capital loss, some don't |

### Income events (ordinary income at FMV)

| Type | Description | When recognized |
|------|-------------|-----------------|
| **Mining** | Proof-of-work block rewards | When coins received in wallet |
| **Staking** | Proof-of-stake validation rewards | When rewards credited (jurisdiction-dependent) |
| **Yield farming** | DeFi liquidity provision returns | When tokens received |
| **Airdrops** | Free tokens distributed | At receipt if no action required; at claim if action required |
| **Hard forks** | New chain creates new tokens | Varies by jurisdiction — some at fork, some at first disposal |
| **Payment for services** | Employer/client pays in crypto | At receipt, FMV in local currency |
| **Interest** | CeFi/DeFi lending returns | When credited |
| **Referral/bounty rewards** | Platform rewards | At receipt |

### Non-taxable events (no gain/loss computed)

| Type | Description | Note |
|------|-------------|------|
| **Transfer between own wallets** | Moving from exchange to hardware wallet | Same owner — no disposal |
| **Buying with fiat** | USD → BTC purchase | Establishes cost basis only |
| **Wrapping/unwrapping** | ETH → WETH | Generally not taxable (same underlying asset) |
| **Chain migration** | Token upgrade on same protocol | Generally not taxable |

### DeFi-specific events

| Type | Tax treatment | Complexity |
|------|--------------|------------|
| **Liquidity pool deposit** | Potentially a disposal (country-dependent) | High — impermanent loss not always deductible |
| **Liquidity pool withdrawal** | Potentially an acquisition + disposal | High |
| **Borrowing against crypto** | Generally not a taxable event | Medium — but liquidation IS taxable |
| **Lending crypto** | May be a disposal or may retain ownership | High — jurisdiction-dependent |
| **Governance token rewards** | Income at FMV when received | Medium |
| **Flash loans** | Generally no tax impact if repaid in same transaction | Low |

---

## Step 3 — Cost basis methods

The country skill specifies which methods are permitted. Universal definitions:

| Method | How it works | Effect on tax |
|--------|-------------|---------------|
| **FIFO** (First In, First Out) | Oldest lots disposed first | In rising markets: higher gains (older = lower cost) |
| **LIFO** (Last In, First Out) | Newest lots disposed first | In rising markets: lower gains (newer = higher cost) |
| **Specific identification** | Taxpayer chooses which lot | Maximum flexibility — can minimize tax |
| **Average cost** | Total cost / total units | Simple but no lot-level optimization |
| **S104 pool** (UK-specific) | Weighted average pool | Required for UK shares/crypto |

**Conservative default:** FIFO unless the country skill permits and the taxpayer has elected another method.

### Cost basis tracking rules

1. **Acquisition cost** includes: purchase price + exchange fees + network gas fees + transfer fees
2. **Crypto-to-crypto swaps** create a NEW cost basis for the received asset at the FMV of the disposed asset
3. **Staking/mining income** establishes cost basis at the FMV on the date of receipt
4. **Airdrops** — if taxed as income at receipt, cost basis = FMV at receipt. If not taxed at receipt (e.g., unsolicited, zero-value), cost basis = zero
5. **Hard forks** — country-specific. Some jurisdictions assign zero basis, others use FMV at fork
6. **All values must be converted to local fiat** at the transaction date using a consistent exchange rate source (CoinGecko, CoinMarketCap, or the exchange's own reported price)

---

## Step 4 — Gain/loss computation

For each disposal:

```
Gain or Loss = Proceeds (FMV in local fiat) − Cost Basis − Allowable Fees
```

Then apply the country skill's rules for:
- **Holding period** — short-term vs long-term (thresholds vary: 1 year US/UK, 0 for some, varies by country)
- **Tax rate** — capital gains rate vs ordinary income rate
- **Exemptions** — annual exempt amount, de minimis thresholds, personal use exemptions
- **Loss offset** — which gains can losses offset? Carry-forward rules?
- **Wash sale / bed-and-breakfasting** — anti-avoidance rules on repurchasing after a loss

---

## Step 5 — Income computation

For each income event (mining, staking, airdrops, etc.):

```
Taxable Income = FMV at Receipt (in local fiat)
```

Country skill determines:
- Whether taxed as ordinary income, miscellaneous income, or a special category
- Whether business deductions apply (electricity for mining, hardware depreciation)
- Whether there's a de minimis threshold below which income is not taxable
- Self-employment tax / social contribution implications

---

## Step 6 — Reporting obligations

Country skill specifies the forms, but universal requirements include:

| Obligation | What to report |
|------------|---------------|
| Capital gains schedule | Every disposal: date acquired, date sold, proceeds, cost basis, gain/loss |
| Income schedule | Mining/staking/airdrop income with FMV at receipt |
| Foreign account reporting | Balances on foreign exchanges (FBAR, Form 8938, DAC8 equivalent) |
| Digital asset question | Whether taxpayer transacted in digital assets during the year |
| Annual crypto return | Some jurisdictions require a separate crypto-specific filing |

---

## Step 7 — Output specification

Produce these artifacts:

### 1. Crypto transaction ledger
For every transaction in the period:

| Date | Type | Asset | Amount | FMV (local) | Cost basis | Gain/Loss | Holding period | Tax treatment |
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
| Source | Amount (local fiat) | Tax treatment |
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

## Conservative defaults

| Ambiguity | Conservative default |
|-----------|---------------------|
| Unknown acquisition cost | **STOP** — cannot compute without cost basis. Ask user. |
| Unknown holding period | Short-term (higher rate) |
| Unknown whether income or capital | Income (higher rate) |
| Unknown FMV at receipt | CoinGecko/CoinMarketCap daily close in local fiat |
| Unknown cost basis method | FIFO |
| Airdrop — no clear service performed | Income at FMV on receipt |
| Staking — unclear when rewards received | At the earliest possible date (more income recognized sooner) |
| DeFi LP deposit — unclear if disposal | Treat as disposal (more conservative) |
| Lost/stolen crypto — no evidence | No loss claim (cannot substantiate) |
| Crypto-to-crypto swap | Taxable disposal (even if some jurisdictions haven't clarified) |

---

## Self-checks (run before delivering)

1. Every disposal has a computed cost basis (no blanks)
2. Crypto-to-crypto swaps are treated as taxable disposals
3. Mining/staking income is recognized at FMV on receipt date
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

## Refusals

| Trigger | Action |
|---------|--------|
| No transaction history available | STOP — cannot compute without data |
| Day trading as primary income with hundreds of trades and no CSV | STOP — manual entry impossible |
| DeFi protocol with unclear tax treatment and no country guidance | Flag for reviewer, apply conservative default, disclose uncertainty |
| Crypto earned through illegal activity | REFUSE |
| Tax evasion planning ("how do I hide my crypto") | REFUSE |

---

## Disclaimer

This workflow base and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. Cryptocurrency taxation is rapidly evolving and many jurisdictions have unclear or changing rules. All outputs must be reviewed by a qualified professional before filing.
