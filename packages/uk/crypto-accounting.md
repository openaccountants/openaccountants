---
name: crypto-accounting
description: How to build a defensible crypto transaction ledger for UK clients exchange/wallet data collection, internal-transfer traps, and the Section 104/30-day matching sequence.
jurisdiction: GB
last_updated: 2026-09-02
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Crypto Accounting in United Kingdom: Bookkeeping & Record-Keeping for Crypto Transactions, how I do it

## Crypto Accounting in United Kingdom: Bookkeeping & Record-Keeping for Crypto Transactions, how I do it

This Guide covers what a UK-based accountant needs to build and maintain a defensible transaction record for a client's cryptoasset activity, ahead of any CGT or income tax computation. Good bookkeeping here is what makes every downstream tax position defensible HMRC's own manual is explicit that the responsibility for keeping this data sits with the individual, not the exchange, and that a compliance check lives or dies on the audit trail you built at this stage. The record-keeping regime as HMRC currently states it.

## Who this is for

This applies to accountants building or reviewing the underlying transaction ledger for individual clients holding, trading, or earning cryptoassets the data layer that CGT (SA108) and income tax computations are built on top of. It does not cover the tax computation itself (disposal gains, staking/mining income treatment, DeFi classification), which sit in their own Guides, nor corporate crypto accounting under UK GAAP/IFRS, which follows separate rules. Clients whose exchange history spans defunct or unregulated offshore platforms with no exportable data, or whose wallet activity can't be reconciled to any fiat on/off-ramp, should be flagged for a specialist crypto forensic review before you attempt a normal bookkeeping build.

## Before you start, ask the client

- Which exchanges, brokers, and wallets have they used, going back to their very first crypto transaction not just the ones they currently use.
- Can they export full transaction history (CSV or API) from each platform, including deposits, withdrawals, trades, and any staking/rewards activity, rather than relying on a current balance snapshot?
- Do they hold assets in self-custodied (hot or cold) wallets, and can they provide public wallet addresses so activity can be cross-checked against the blockchain directly?
- Have they used any platform that has since closed, been hacked, or stopped serving UK customers these are the gaps you need to plug first, while any trace of the data might still exist.
- Have they engaged in any crypto-to-crypto trades, or only fiat-to-crypto and back? Crypto-to-crypto swaps are disposals in their own right and are the single most commonly missed category in a client-provided summary.

## The method, step by step

1. Build the master transaction list first, before touching any tax classification. Pull every exportable record from every exchange and wallet the client has ever used deposits, withdrawals, trades, transfers between their own wallets, staking rewards, airdrops. Getting this list complete before you start classifying anything is what prevents a rebuild later; classifying transaction-by-transaction as you go means re-doing the whole file every time a missing exchange turns up.
2. For each transaction, record: the type of cryptoasset, the date, whether it was an acquisition or disposal, the number of units, and the sterling value at the date of the transaction. HMRC's own guidance treats this as the minimum defensible record — a wallet download or blockchain link on its own isn't enough without the sterling valuation attached at the transaction date, since that's what actually feeds the gain/loss computation.
3. Strip out internal transfers between the client's own wallets or accounts before running any computation. A transfer from one exchange to a personal cold wallet is not a disposal but it's the single most common line-item error I see, because exported CSVs often list it identically to an external trade. Tag these explicitly as "internal transfer" in the ledger so nobody downstream mistakes them for a disposal event.
4. Apply the Section 104 pooling approach to group same-type assets together as they're acquired and disposed of, subject to the same-day rule and 30-day ("bed and breakfasting") matching rule taking priority over the pool for any acquisitions within those windows. Get this sequencing wrong pooling first, matching rules second and the cost basis for near-in-time disposals comes out wrong even though the total pool value looks fine on the surface.
5. Reconcile the sterling valuation of every acquisition and disposal against a consistent, defensible pricing source (the exchange's own recorded fill price where available, or a stated third-party price index applied consistently) don't mix valuation sources transaction to transaction, since HMRC can and does query an unexplained swing in method partway through a tax year.
6. Once the ledger reconciles, total units held per asset in your records match the units actually sitting in the client's wallets and exchange balances at the reconciliation date hand it off for the CGT or income tax computation. Do not hand off a ledger with unresolved balance mismatches; that mismatch is exactly the kind of gap that turns into a much bigger problem once a return has been filed on top of it.

## The traps

- Treating an exchange's current balance snapshot as sufficient records — exchanges aren't required to retain transaction history indefinitely, and a client who only pulls data when you ask may find the platform has already purged it.
- Missing crypto-to-crypto trades because the client only reported fiat conversions in their own summary; every swap is a disposal of the asset given up.
- Recording an internal wallet-to-wallet transfer as a disposal, which manufactures a taxable event and a gain/loss that never actually happened.
- Applying the Section 104 pool without first excluding same-day and 30-day rule-matched acquisitions, corrupting the cost basis for any disposal made shortly after a new purchase.
- Letting the client's DIY spreadsheet be the only record, with no underlying export or blockchain reference to support it if HMRC opens an enquiry the spreadsheet is a summary, not the audit trail.
- Disposing of the client's own records too early. Standard practice for the self-employed and those with property or investment income is to retain records for at least five years from the 31 January filing deadline for that tax year treat crypto records the same way, and keep cost-basis-relevant records even longer if the position (the pool) carries forward into future years, since you'll need the acquisition history to compute the next disposal correctly.

## Rates, thresholds and deadlines

**Rates, thresholds and deadlines**  _(HMRC Cryptoassets Manual — https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10400)_

| What | Value | Source |
| --- | --- | --- |
| Who must keep crypto transaction records | The individual, not the exchange; exchanges may not retain data indefinitely or may cease to exist | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10400 |
| Minimum record content per transaction | Type of cryptoasset, date, acquisition/disposal, number of units, and value in sterling at the transaction date | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10400 |
| Standard record retention period (self-employed / property / investment income) | At least 5 years from the 31 January Self Assessment filing deadline for that tax year | https://www.gov.uk/self-assessment-tax-returns/keeping-your-pay-and-tax-records |
| Cost basis matching order | Same-day rule, then 30-day ("bed and breakfasting") rule, then Section 104 pooling for the remainder | TCGA 1992 s104, s105, s106A — https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200 |
| Cryptoasset Reporting Framework (CARF) | UK platforms began collecting user/transaction data on UK users from 1 January 2026; first reports due to HMRC by 31 May 2027 | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10000 |

## Rates, thresholds and deadlines

*Working paper aid only; this builds the transaction record, not the filed tax position. Have the computation built from this ledger reviewed and signed off before anything is filed.*

## Sources

- HMRC Cryptoassets Manual, CRYPTO10400 — Introduction to cryptoassets: record keeping — https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10400 - HMRC Cryptoassets Manual, CRYPTO10000 — Introduction to cryptoassets: contents — https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10000 - HMRC Cryptoassets Manual, CRYPTO22200 — Capital Gains Tax: pooling, section 104 — https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200 - Taxation of Chargeable Gains Act 1992, ss.104, 105, 106A - HMRC, Self Assessment tax returns: Keeping your pay and tax records — https://www.gov.uk/self-assessment-tax-returns/keeping-your-pay-and-tax-records

> Contributed by Nadir Khan.

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
