---
name: crypto-accounting
description: "How to build a defensible cryptoasset transaction ledger for UK individual clients in tax year 2026/27, before any Capital Gains Tax or income tax computation. Covers collecting exchange and wallet data, the record HMRC expects for each transaction, stripping out transfers between the client's own wallets, crypto-to-crypto swaps as disposals, the same-day, 30-day and section 104 matching order, consistent sterling valuation, reconciling units to balances, how long to keep records, and what the Cryptoasset Reporting Framework means from 1 January 2026. The tax computation itself is in uk-crypto-tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/crypto-accounting"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Crypto Accounting in United Kingdom: Bookkeeping and Record-Keeping for Crypto Transactions, how I do it

This Guide covers what a UK-based accountant needs to build and maintain a defensible transaction record for a client's cryptoasset activity, ahead of any CGT or income tax computation, for tax year 2026/27 (6 April 2026 to 5 April 2027). Good bookkeeping here is what makes every downstream tax position defensible: HMRC's own manual is explicit that exchanges may keep records only for a short time or may stop existing, so the responsibility for the data sits with the individual, and a compliance check lives or dies on the audit trail built at this stage.

## Scope

This applies to accountants building or reviewing the underlying transaction ledger for individual clients holding, trading, or earning cryptoassets: the data layer that CGT (SA108) and income tax computations are built on top of.

It does not cover the tax computation itself (disposal gains, staking and mining income, DeFi classification), which is in `uk-crypto-tax`, nor corporate crypto accounting under UK GAAP or IFRS, which follows separate rules.

Clients whose exchange history spans defunct or unregulated offshore platforms with no exportable data, or whose wallet activity cannot be reconciled to any fiat on or off-ramp, are flagged for a specialist crypto forensic review before a normal bookkeeping build (see When to refuse or refer).

## Ask the client first

- Which exchanges, brokers and wallets have they used, going back to their very first crypto transaction, not just the ones they use now?
- Can they export full transaction history (CSV or API) from each platform, including deposits, withdrawals, trades and any staking or rewards activity, rather than a current balance snapshot?
- Do they hold assets in self-custodied (hot or cold) wallets, and can they give the public wallet addresses so activity can be cross-checked against the blockchain?
- Have they used any platform that has since closed, been hacked, or stopped serving UK customers? These are the gaps to plug first, while any trace of the data may still exist.
- Have they made any crypto-to-crypto trades, or only fiat to crypto and back? Crypto-to-crypto swaps are disposals in their own right and are the most commonly missed category in a client's own summary.
- Are they self-employed or trading in crypto, or an individual investor? It decides how long the records must be kept.

## The method, step by step

1. **Build the master transaction list first, before any tax classification.** Pull every exportable record from every exchange and wallet the client has ever used: deposits, withdrawals, trades, transfers between their own wallets, staking rewards, airdrops. Getting this list complete before classifying anything prevents a rebuild later; classifying as you go means redoing the file every time a missing exchange turns up.
2. **Record, for each transaction, what HMRC lists:** the type of cryptoasset, the date, whether it was bought or sold, the number of units, the value in pound sterling at the date of the transaction, and the cumulative total of the investment units held, plus bank statements and wallet addresses. A wallet download or blockchain link on its own is not enough without the sterling value at the transaction date, since that is what feeds the gain or loss computation.
3. **Strip out internal transfers** between the client's own wallets or accounts before running any computation. Moving tokens between addresses the client beneficially controls is not a disposal, but it is the most common line-item error I see, because exported CSVs often list it the same way as an external trade. Tag these explicitly as "internal transfer" in the ledger so nobody downstream mistakes them for a disposal.
4. **Mark every disposal.** A disposal includes selling tokens for money, exchanging tokens for a different type of token, using tokens to pay for goods or services, and giving tokens away (except to a spouse or civil partner). Every swap is a disposal of the asset given up.
5. **Apply the matching order:** first the same-day rule (acquisitions and disposals of the same token type on the same day), then the 30-day rule (tokens of the same type acquired within the next 30 days), and only then the section 104 pool for the rest (TCGA 1992 ss.104, 105, 106A). Get this sequence wrong (pool first, matching second) and the cost basis for near-in-time disposals comes out wrong even though the total pool value looks fine.
6. **Value consistently.** Reconcile the sterling value of every acquisition and disposal against one defensible pricing source (the exchange's recorded fill price where available, or a stated third-party price index applied consistently). Do not mix valuation sources from transaction to transaction: HMRC can query an unexplained change of method partway through a tax year.
7. **Reconcile units to balances.** Total units held per asset in the ledger must match the units actually in the client's wallets and exchange balances at the reconciliation date. Only then hand the ledger off for the CGT or income tax computation in `uk-crypto-tax`. Do not hand off a ledger with unresolved balance mismatches.
8. **Keep the records for the right period** (rates table below), and keep cost-basis records for as long as a section 104 pool carries forward, since the acquisition history is needed for every later disposal.

### Rates, bands and thresholds

Tax year 2026/27 unless stated.

| Item | Rule or figure | Applies | Official source |
| --- | --- | --- | --- |
| Who must keep crypto records | The individual: exchanges may keep records only for a short period, or may no longer exist | All individuals with cryptoassets | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10400 |
| Record content per transaction | Type of cryptoasset; date; bought or sold; number of units; value in pound sterling at the transaction date; cumulative total held | Each transaction | same |
| What is a disposal | Selling for money; exchanging for a different token; paying for goods or services; giving away (not to a spouse or civil partner). Moving tokens between the individual's own addresses is not a disposal | CGT | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100 |
| Matching order | Same-day rule first, then acquisitions within the next 30 days, then the section 104 pool | CGT on tokens of the same type | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200 |
| Record retention, individuals (not self-employed) | At least 22 months after the end of the tax year if the return was sent on time; at least 15 months after sending if it was late | Investors, savings, capital gains | https://www.gov.uk/keeping-your-pay-tax-records/how-long-to-keep-your-records |
| Record retention, self-employed | At least 5 years after the 31 January submission deadline of the relevant tax year | Crypto traded as a business | https://www.gov.uk/self-employed-records/how-long-to-keep-your-records |
| Cryptoasset Reporting Framework | From 1 January 2026, exchanges and other cryptoasset service providers must collect and record customer details (name, address, tax residence, tax identification number) | Service providers with UK customers | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10410 |
| CGT rates used in the worked cases | 18% within the unused basic rate band, 24% above; annual exempt amount GBP 3,000 for 2026/27 | Individuals, gains from 6 April 2026 | https://www.gov.uk/capital-gains-tax/rates |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Transfer from an exchange to the client's own cold wallet | Not a disposal; tag "internal transfer"; units stay in the same pool |
| Mixer or tumbler returning the same type of token | Not a disposal (CRYPTO22100); a different token back is a disposal |
| Crypto-to-crypto swap | Disposal of the token given up, at its sterling value; acquisition of the new token at the same value |
| Gift to a spouse or civil partner | Not a disposal at a gain or loss; record it with the date and units |
| Disposal and reacquisition within 30 days | Match to the later acquisition, not the pool |
| Exchange that has closed or purged history | Rebuild from bank statements, wallet addresses and the blockchain; if it cannot be rebuilt, refer |

### The traps

- Treating an exchange's current balance snapshot as sufficient records: exchanges are not required to keep transaction history indefinitely, and a client who only pulls data when asked may find the platform has already purged it.
- Missing crypto-to-crypto trades because the client only reported fiat conversions in their own summary.
- Recording an internal wallet-to-wallet transfer as a disposal, which manufactures a taxable event and a gain or loss that never happened.
- Applying the section 104 pool without first taking out same-day and 30-day matched acquisitions, corrupting the cost basis for any disposal made shortly after a new purchase.
- Letting the client's DIY spreadsheet be the only record, with no underlying export or blockchain reference to support it if HMRC opens an enquiry: the spreadsheet is a summary, not the audit trail.
- Disposing of the client's records too early. The period depends on whether the client is self-employed (rates table), and cost-basis records are needed for as long as the pool carries forward.

## Worked cases

All amounts are illustrations, not client data.

**Case 1: the matching order.** A client holds a section 104 pool of 10 BTC. On 1 June 2026 she buys 2 BTC for GBP 110,000 and later that day sells 3 BTC for GBP 165,000. On 15 June 2026 she buys 1 BTC for GBP 52,000. Same-day rule first: 2 of the 3 BTC sold are matched with the 2 bought that day, proceeds 2/3 of GBP 165,000 = GBP 110,000, cost GBP 110,000, gain nil. The third BTC is matched with the 15 June purchase under the 30-day rule: proceeds GBP 55,000, cost GBP 52,000, gain GBP 3,000. The 10 BTC pool is untouched.

```oa-check
name: Same-day then 30-day matching, 3 BTC sold on 1 June 2026
inputs:
  proceeds_total: 165000
  units_sold: 3
  same_day_units: 2
  same_day_cost: 110000
  thirty_day_cost: 52000
steps:
  - proceeds_per_unit: proceeds_total / units_sold
  - same_day_gain: proceeds_per_unit * same_day_units - same_day_cost
  - thirty_day_gain: proceeds_per_unit * (units_sold - same_day_units) - thirty_day_cost
  - total_gain: same_day_gain + thirty_day_gain
expected:
  same_day_gain: 0.00
  thirty_day_gain: 3000.00
  total_gain: 3000.00
```

**Case 2 (decision): internal transfer or disposal?** The client's exchange CSV shows a "send" of 0.5 BTC worth GBP 27,500 on the day. Her section 104 pool cost averages GBP 20,000 per BTC. The receiving address is her own cold wallet (she gives the public address and it matches). Recorded wrongly as a disposal, it would show a gain of GBP 27,500 less GBP 10,000 = GBP 17,500 and, for a higher rate taxpayer with the annual exempt amount already used, CGT of GBP 4,200 at 24%. Recorded correctly as an internal transfer, there is no disposal and no tax. Decide by the address, not the CSV label: if the address is hers, it is an internal transfer; if it is a third party's, it is a disposal (a sale, payment or gift).

```oa-check
name: Mislabelled internal transfer, tax overstated if booked as a disposal
inputs:
  units: 0.5
  value_on_day: 27500
  pool_cost_per_unit: 20000
  cgt_higher_rate: 0.24
steps:
  - allowable_cost: units * pool_cost_per_unit
  - wrong_gain: value_on_day - allowable_cost
  - wrong_tax: wrong_gain * cgt_higher_rate
  - correct_tax: 0
  - overstatement: wrong_tax - correct_tax
expected:
  allowable_cost: 10000.00
  wrong_gain: 17500.00
  wrong_tax: 4200.00
  overstatement: 4200.00
```

## When to refuse or refer

- Exchange history on defunct or unregulated offshore platforms with no exportable data, or wallet activity that cannot be reconciled to any fiat on or off-ramp: refer for a specialist crypto forensic review before a normal bookkeeping build.
- A ledger whose units do not reconcile to wallet and exchange balances: do not hand it off for computation.
- Staking, mining, lending, DeFi or NFT classification, and the gain or income computation: hand to `uk-crypto-tax`.
- Company-held cryptoassets and UK GAAP or IFRS accounting: out of scope.
- An HMRC compliance check or a "nudge" letter about crypto: refer to the reviewing accountant.

## Filing and payment

This Guide files nothing. The ledger feeds the SA108 capital gains pages and any income entries on the client's Self Assessment return, prepared with `uk-crypto-tax`. Deadlines, payment and penalties for that return are in `uk-income-tax-sa100` and `uk-capital-gains-sa108`.

## Completion checklist

- Every platform and wallet the client has used is listed, with a full export or a recorded reason it is missing.
- Each transaction carries type, date, bought or sold, units and sterling value at the date.
- Internal transfers are tagged and excluded from disposals.
- Crypto-to-crypto swaps are recorded as disposals.
- Same-day and 30-day matches are made before the section 104 pool.
- One pricing source is used throughout, and named.
- Units in the ledger agree to wallet and exchange balances at the reconciliation date.
- The retention period that applies to this client is noted.

*Working paper aid only; this builds the transaction record, not the filed tax position. Have the computation built from this ledger reviewed and signed off before anything is filed.*

## Sources

| Source | What was read | URL | Read on |
| --- | --- | --- | --- |
| HMRC Cryptoassets Manual, CRYPTO10400 record keeping | Read for who keeps records and the record content per transaction | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10400 | 2026-11-14 |
| HMRC Cryptoassets Manual, CRYPTO10000 contents | Read for the manual structure and the CARF page reference | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10000 | 2026-11-14 |
| HMRC Cryptoassets Manual, CRYPTO10410 Cryptoasset Reporting Framework | Read for collection from 1 January 2026 and the customer details | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10410 | 2026-11-14 |
| HMRC Cryptoassets Manual, CRYPTO22100 what is a disposal | Read for the disposal list and transfers between own addresses | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22100 | 2026-11-14 |
| HMRC Cryptoassets Manual, CRYPTO22200 pooling | Read for the same-day rule, the 30-day rule (TCGA 1992 s.106A) and the section 104 pool | https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200 | 2026-11-14 |
| GOV.UK, How long to keep your records | Read for 22 months after the tax year, or 15 months after a late return | https://www.gov.uk/keeping-your-pay-tax-records/how-long-to-keep-your-records | 2026-11-14 |
| GOV.UK, Self-employed records: how long to keep them | Read for at least 5 years after the 31 January submission deadline | https://www.gov.uk/self-employed-records/how-long-to-keep-your-records | 2026-11-14 |
| GOV.UK, Capital Gains Tax rates | Read for 18% and 24% from 6 April 2026 and the GBP 3,000 allowance for 2026/27 | https://www.gov.uk/capital-gains-tax/rates | 2026-11-14 |

Not yet confirmed: the date by which UK reporting cryptoasset service providers send their first CARF report to HMRC (the old file said 31 May 2027; CRYPTO10410 read today does not state it, and the HMRC service provider guidance page tried today returned 404).

> Contributed by Nadir Khan.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `crypto-accounting` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/crypto-accounting. If neither is available, confirm every figure against the official source pages cited above before relying on it.
