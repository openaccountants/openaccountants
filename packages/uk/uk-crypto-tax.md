---
name: uk-crypto-tax
description: Use this skill whenever asked about UK cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax UK", "Bitcoin UK tax", "HMRC crypto", "cryptoassets UK", "crypto capital gains UK", "staking tax UK", "mining tax UK", "NFT tax UK", "DeFi tax UK", "SA108 crypto", "crypto CGT", "bed and breakfasting crypto", "S104 pool", "crypto loss UK", "Coinbase UK tax", "Binance UK tax", "Revolut crypto UK", "crypto income UK", "DAC8 UK", "CARF crypto", "crypto reporting 2026", "18% 24% crypto", "HMRC cryptoassets manual", or any question about the income tax, capital gains tax, or reporting treatment of cryptocurrency, tokens, or digital assets for UK tax residents. Covers HMRC's Cryptoassets Manual (CRYPTO10000+), S104 pooling, same-day and 30-day matching rules, DeFi lending/staking, NFTs, mining, SA108 reporting, and the Crypto Asset Reporting Framework (CARF) from 2026. ALWAYS read this skill before touching any UK crypto work.
version: 2.0
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on:
  - uk-capital-gains-sa108
category: crypto
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Crypto Tax

## UK Crypto / Digital Assets Tax Skill v2.0

Covers three UK tax years: **2024-25**, **2025-26**, and **2026-27**, including the mid-year CGT rate change on 30 October 2024 and the introduction of the Crypto Asset Reporting Framework (CARF) from April 2026.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Crypto Tax

- **Basic rate taxpayer** — 18%  _(TCGA 1992)_
- **Higher/additional rate** — 24%  _(TCGA 1992)_
- **AEA** — £3,000  _(TCGA 1992)_
- **Required method** — S104 pooling (weighted average)  _(TCGA 1992 s.104)_
- **FIFO** — NOT permitted  _(HMRC CRYPTO22200)_
- **Specific identification** — NOT permitted for crypto  _(HMRC CRYPTO22200)_
- **1st: Same-day** — Match same-day acquisitions  _(TCGA s.105(1))_
- **2nd: 30-day rule** — Match acquisitions within 30 days AFTER disposal  _(TCGA s.106A)_
- **3rd: S104 pool** — Average cost from pool  _(TCGA s.104)_
- **Mining (hobbyist)** — Miscellaneous income at FMV  _(ITTOIA s.687)_
- **Staking rewards** — Miscellaneous income at FMV  _(HMRC CRYPTO21200)_
- **Airdrop (service performed)** — Miscellaneous income at FMV  _(HMRC CRYPTO21250)_
- **Airdrop (unsolicited)** — Not income; CGT on disposal from zero cost  _(HMRC CRYPTO21250)_

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom (England, Wales, Northern Ireland; Scotland has different income tax rates) |
| Tax | Capital Gains Tax (CGT) and Income Tax on cryptoassets |
| Currency | GBP (all values must be converted to GBP at the transaction date) |
| Tax year | 6 April – 5 April |
| Primary authority | HMRC Cryptoassets Manual (CRYPTO10000+); Taxation of Chargeable Gains Act 1992 (TCGA 1992); Income Tax Act 2007 (ITA 2007); Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005); Finance Act 2024 (rate change at 30 Oct 2024) |
| Tax authority | HM Revenue & Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online / Government Gateway |
| Cost basis method | Section 104 pooling (TCGA 1992 S104), subject to same-day and 30-day matching rules |
| Anti-avoidance | 30-day bed-and-breakfasting rule (TCGA 1992 S106A) |
| Reporting form | SA108 (Capital Gains Summary) supplementary to SA100 — dedicated cryptoasset tick box from 2024-25 |
| Exchange reporting | CARF first reporting in **2027** covering **2026 calendar year** transactions; DAC8-equivalent UK rules align |
| Validated by | Verified by James Power on 2026-06-03 |
| Skill version | 2.0 |

### Three-Year Snapshot

**Three-Year Snapshot**

| Item | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| CGT rate (basic-rate) | 10% pre-30 Oct 2024 / **18%** from 30 Oct 2024 | 18% | 18% |
| CGT rate (higher/additional) | 20% pre-30 Oct 2024 / **24%** from 30 Oct 2024 | 24% | 24% |
| Annual Exempt Amount (individuals) | £3,000 | £3,000 | £3,000 |
| Annual Exempt Amount (trustees) | £1,500 | £1,500 | £1,500 |
| SA108 crypto tick box | Yes (new from 2024-25) | Yes | Yes |
| CARF reporting | Not yet | Data collection prep | **Data collection begins (calendar 2026); first reports filed 2027** |
| Personal Allowance | £12,570 | £12,570 | £12,570 (subject to confirmation) |

### HMRC Cryptoasset Classification (CRYPTO10000+)

**HMRC Cryptoasset Classification**

| Asset Type | HMRC Classification | CGT Treatment | Income Tax Treatment |
| --- | --- | --- | --- |
| Exchange tokens (BTC, ETH, LTC) | Tokens used as means of payment | Subject to CGT on disposal | Mining/staking/airdrops = income |
| Utility tokens | Tokens providing access to a service | Subject to CGT on disposal | Trading profits = income if traded |
| Security tokens | Tokens providing rights like shares/debt | Subject to CGT on disposal | May also attract income tax on returns |
| Stablecoins (USDT, USDC) | Exchange tokens pegged to fiat | Subject to CGT on disposal (gain usually negligible) | N/A |
| NFTs | Non-fungible tokens | Subject to CGT on disposal | Creator sales = trading income |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown cost basis | Zero cost basis (maximises gain) — STOP if material |
| Unknown whether trading or investment | Treat as investment (CGT) unless clear badges of trade |
| Unknown token classification | Treat as exchange token (subject to CGT) |
| Unknown FMV at receipt | Use CoinGecko/CoinMarketCap daily close in GBP |
| Unknown whether income or capital DeFi return | Income (higher rate treatment) |
| Airdrop with no clear service performed | Income at FMV on receipt |
| Disposal date straddles 30 Oct 2024 | Use **contract date of disposal** to allocate to pre- or post-30 Oct rate |

## Section 2 — Classification Rules: Capital Gains vs Income

HMRC treats cryptoassets as **CGT assets by default** for individuals. This classification applies across all three tax years covered (2024-25, 2025-26, 2026-27).

### When CGT applies (most individual crypto users)

- **Disposal definition** — HMRC treats cryptoassets as property, not currency. Each disposal triggers a CGT computation. A "disposal" includes: Selling tokens for fiat; Exchanging tokens for a different type of token (crypto-to-crypto swap); Using tokens to pay for goods or services; Giving away tokens (except to spouse/civil partner)  _(CRYPTO22100)_
- **NOT a disposal** — Transferring between own wallets; Using a mixer/tumbler where same token type returned; Gifting to spouse/civil partner (no gain, no loss — transferee inherits cost basis)

### When Income Tax applies

Crypto received as **income** (employment, mining, staking rewards, airdrops with conditions) is taxed as miscellaneous income or trading income — income tax + NIC.

**Income Tax Applicability Table**

| Activity | Tax Treatment | Authority |
| --- | --- | --- |
| Mining (hobbyist) | Miscellaneous income at FMV when received | ITTOIA 2005 S687; CRYPTO21200 |
| Mining (commercial/business) | Trading income; expenses deductible; Class 2/4 NIC | ITTOIA 2005 Part 2; CRYPTO21200 |
| Staking rewards | Miscellaneous income at FMV when received | CRYPTO21200 |
| Airdrops (for service/action) | Miscellaneous income at FMV when received | CRYPTO21250 |
| Airdrops (unsolicited, no action) | Not income on receipt; CGT on disposal from zero cost | CRYPTO21250 |
| Employer pays salary in crypto | Employment income at FMV; PAYE/NIC applies | CRYPTO21100 |
| DeFi yield (income returns) | Miscellaneous income or trading income | CRYPTO61200 |

### Income Tax Rates (England, Wales, NI) — All Three Years

**Income Tax Rates**

| Band | Taxable Income | Rate |
| --- | --- | --- |
| Personal Allowance | Up to £12,570 | 0% |
| Basic rate | £12,571 – £50,270 | 20% |
| Higher rate | £50,271 – £125,140 | 40% |
| Additional rate | Over £125,140 | 45% |

Bands and Personal Allowance are frozen through 2027-28 under the previous Government's policy; 2026-27 figures subject to confirmation in Autumn Budget 2025. Scotland operates separate income tax bands.

## Section 3 — Capital Gains Tax Rate Table (3-Year)

This is the central rate reference for crypto disposals. Use it to determine which rate applies based on the **date of disposal**.

### CGT Rates for Cryptoassets — 3-Year View

**CGT Rates for Cryptoassets — 3-Year View**

| Tax Year | Period | Basic-rate (gains in basic band) | Higher / Additional / Trustees | Annual Exempt Amount |
| --- | --- | --- | --- | --- |
| **2024-25** | 6 Apr 2024 – **29 Oct 2024** | **10%** | **20%** | £3,000 |
| **2024-25** | **30 Oct 2024** – 5 Apr 2025 | **18%** | **24%** | (shared £3,000) |
| **2025-26** | 6 Apr 2025 – 5 Apr 2026 | **18%** | **24%** | £3,000 |
| **2026-27** | 6 Apr 2026 – 5 Apr 2027 | **18%** | **24%** | £3,000 |

Authority: Finance Act 2024 (Autumn 2024) increased the main rates from 10%/20% to 18%/24% with effect from **30 October 2024**. The 2024-25 tax year is therefore split: disposals on or before 29 October 2024 use the old rates; disposals on or after 30 October 2024 use the new rates. From 2025-26 onwards the full year uses 18%/24%.

The Annual Exempt Amount of £3,000 is a **single** annual allowance per individual — it is not split across the two halves of 2024-25. Apply it once against total chargeable gains for the year.

### CGT Computation

- **CGT Computation formula** — Disposal proceeds (GBP at date of disposal) LESS: Allowable cost (from S104 pool, same-day rule, or 30-day rule) LESS: Incidental costs of disposal (exchange fees, gas fees) = Gain or (Loss) Total gains for the year LESS: Allowable losses of the year LESS: Losses brought forward (only to reduce gains to annual exempt amount) LESS: Annual exempt amount (£3,000) = Taxable gains For 2024-25 only: allocate taxable gains between pre- and post-30 Oct disposals in proportion to gross gains in each window, then apply the applicable rate. Tax = Taxable gains × applicable rate(s) per table above

### SA108 Reporting from 2024-25

- **Cryptoasset tick box** — HMRC introduced a dedicated "crypto asset" tick box on SA108 from the 2024-25 tax year. Where any portion of the year's disposals are cryptoassets, the box must be ticked, and crypto disposals must be separately identified in the supporting computations. This obligation continues in 2025-26 and 2026-27.

## Section 4 — Cost Basis: Section 104 Pooling and Matching Rules

(Unchanged across all three years.)

HMRC requires a specific matching order for cryptoasset disposals (CRYPTO22200):

### Matching Order (mandatory priority)

**Matching Order**

| Priority | Rule | Reference |
| --- | --- | --- |
| 1st | **Same-day rule** — match against tokens of the same type acquired on the same day | TCGA 1992 S105(1) |
| 2nd | **30-day rule (bed-and-breakfasting)** — match against tokens of the same type acquired within 30 days AFTER the disposal | TCGA 1992 S106A |
| 3rd | **S104 pool** — match against the average cost of the S104 pool of that token type | TCGA 1992 S104 |

### S104 Pool Mechanics

The S104 pool is a running weighted-average cost pool for each token type. Each time you acquire tokens, the pool quantity and pool cost increase. Each time you dispose of tokens (not matched by same-day or 30-day rules), the cost of disposal is the proportionate share of the pool cost.

- **Pool cost formula** — Pool cost per token = Total pool cost ÷ Total pool quantity Cost of disposal = Tokens disposed × Pool cost per token

**Permitted Method table**

| Permitted Method | Status |
| --- | --- |
| S104 pooling (weighted average) | MANDATORY for most disposals |
| FIFO | NOT permitted |
| LIFO | NOT permitted |
| Specific identification | NOT permitted for crypto |

### What is included in cost basis

- **Included in cost basis** — Purchase price in GBP (converted at exchange rate on acquisition date); Exchange fees and commissions on acquisition; Gas/network fees on acquisition (CRYPTO22280); Note: token fees paid as gas are themselves a disposal at market value  _(CRYPTO22280)_

## Section 5 — DeFi, Staking, Mining, and Airdrops

(Substantively unchanged across the three years. Watch for outcomes of the ongoing DeFi consultation.)

### 5.1 DeFi Lending (CRYPTO61000+)

**DeFi Lending table**

| DeFi Activity | Tax Treatment | Key Question |
| --- | --- | --- |
| Lending tokens to a protocol | **Disposal** if beneficial ownership transfers; **not a disposal** if beneficial ownership retained | Does the borrower/platform have free use of the tokens? |
| Receiving LP tokens in return | Exchange of tokens = disposal of deposited tokens, acquisition of LP tokens at FMV | CRYPTO61620 |
| Interest/yield received | Miscellaneous income at FMV on receipt (NOT interest — crypto is not money) | CRYPTO61200 |
| Withdrawal from protocol | Disposal of LP tokens, reacquisition of underlying | FMV at withdrawal |
| Impermanent loss | Crystallised on withdrawal — reflected in gain/loss on LP token disposal | No separate relief |

**DeFi consultation status:** A 2022/2023 HMRC consultation proposed an elective regime to disregard DeFi lending/staking disposals for CGT until economic disposal. No legislation enacted by 2025-26; status to be re-checked for 2026-27.

### 5.2 Staking

**Staking table**

| Aspect | Treatment |
| --- | --- |
| Proof-of-stake validation rewards | Miscellaneous income at FMV when received (CRYPTO21200) |
| Cost basis of staking reward | FMV at receipt date (becomes acquisition cost for CGT) |
| Subsequent sale of staking reward | CGT on gain from FMV cost basis (rate per Section 3 table) |
| Staking-as-a-service provider | Trading income; business expenses deductible |

### 5.3 Mining

**Mining table**

| Aspect | Treatment |
| --- | --- |
| Hobby mining | Miscellaneous income at FMV when mined (CRYPTO21200) |
| Business mining | Trading income; expenses deductible (electricity, hardware depreciation, rent) |
| Cost basis of mined tokens | FMV at date mined |
| Subsequent sale of mined tokens | CGT on gain from FMV cost basis |

### 5.4 Airdrops (CRYPTO21250)

**Airdrops table**

| Scenario | Treatment |
| --- | --- |
| Airdrop received in return for a service or action | Miscellaneous income at FMV on receipt |
| Unsolicited airdrop (no action required) | NOT income on receipt; zero cost basis; full gain taxable as CGT on disposal |
| Airdrop with negligible value | Record at zero; CGT on disposal |

### 5.5 Hard Forks

**Hard Forks table**

| Scenario | Treatment |
| --- | --- |
| New tokens from fork (e.g. BTC → BCH) | NOT a disposal of original tokens; new tokens received at zero cost (no acquisition cost) |
| Sale of forked tokens | Full proceeds = gain (zero cost basis) |
| Apportioning original cost | HMRC does not require cost apportionment for hard forks — new token cost = £0 |

## Section 6 — NFT Treatment

(Unchanged across the three years; rate changes per Section 3 apply.)

**NFT Treatment table**

| Event | Tax Treatment |
| --- | --- |
| Purchase of NFT (collector) | Acquisition — record cost basis including gas fees |
| Sale of NFT (collector) | CGT on disposal (proceeds minus pool cost of NFT) at applicable rate |
| Creation and primary sale of NFT (artist) | Trading income if business; miscellaneous income if one-off |
| Royalty income from secondary sales | Miscellaneous income at FMV on receipt |
| NFT-for-NFT swap | Disposal of both NFTs; each at FMV |
| NFT becomes worthless | Negligible value claim possible (TCGA 1992 S24(2)) — triggers loss |
| VAT on NFT | Potentially subject to VAT at 20% if seller is VAT-registered (digitally supplied service) |

- **NFT pooling treatment** — HMRC treats NFTs the same as any other cryptoasset for CGT purposes (CRYPTO22100). Each unique NFT is its own asset — no pooling between different NFTs.  _(CRYPTO22100)_

## Section 7 — Reporting Requirements

### 7.1 Self Assessment Forms

**Self Assessment Forms table**

| Form | Purpose |
| --- | --- |
| SA100 | Main Self Assessment tax return |
| SA108 | Capital Gains Summary supplementary page — with cryptoasset tick box from 2024-25 |

### 7.2 When SA108 is required

- **SA108 filing triggers** — You must file SA108 if any of the following apply (all three years): Total disposal proceeds from all assets exceed £50,000; Chargeable gains before losses exceed £3,000 (the annual exempt amount); You wish to claim an allowable capital loss; Losses brought forward are being used; You are reporting any cryptoasset disposal (tick the dedicated cryptoasset box from 2024-25 onwards)

### 7.3 Key Deadlines

**Key Deadlines table**

| Tax Year | End of Year | Paper SA100 | Online SA100 / Payment |
| --- | --- | --- | --- |
| 2024-25 | 5 Apr 2025 | 31 Oct 2025 | 31 Jan 2026 |
| 2025-26 | 5 Apr 2026 | 31 Oct 2026 | 31 Jan 2027 |
| 2026-27 | 5 Apr 2027 | 31 Oct 2027 | 31 Jan 2028 |

- **Payments on account** — Payments on account: 31 January and 31 July each year.

### 7.4 From April 2026 — Crypto Asset Reporting Framework (CARF)

**The major change for 2026-27 and beyond.**

The UK is implementing the **OECD Crypto Asset Reporting Framework (CARF)**, the international equivalent of the EU's DAC8 regime. Key timeline and effects:

**CARF Milestone table**

| Milestone | Date | Effect |
| --- | --- | --- |
| Reporting Crypto-Asset Service Providers (RCASPs) data collection begins | **1 January 2026** | UK exchanges, custodians, brokers, and certain DeFi front-ends must collect KYC + transaction data on UK-resident users |
| First reportable period | **Calendar year 2026** | All in-scope transactions during 2026 are reportable |
| First report filed with HMRC | **2027** (deadline expected May 2027) | RCASPs send user-level data to HMRC |
| HMRC information exchange with other CARF jurisdictions | From **2027** onwards | Bilateral exchange under CARF MCAA |

**Practical implications for taxpayers (from April 2026):**

- HMRC will receive transaction-level data on UK residents from both UK and overseas crypto platforms participating in CARF.
- Non-disclosure risk increases sharply — voluntary disclosure under the Crypto Disclosure Facility is strongly recommended **before** the first CARF reports land in 2027.
- Taxpayers should ensure their on-record name, address, and National Insurance number with each exchange match Self Assessment records to avoid mismatches that trigger HMRC enquiries.
- The CARF data point set covers: identity of holder, wallet addresses (where known), fiat on/off-ramp transactions, crypto-to-crypto exchanges, transfers, and retail payments.

**DAC8 (EU-equivalent) status for UK:** The UK is implementing CARF-aligned rules rather than DAC8 directly (post-Brexit). The direction and data set are equivalent; precise UK reporting thresholds and de minimis rules are being finalised in HMRC technical guidance — TBC for full 2026-27 production cycle. Watch for the final HMRC Cryptoasset Service Provider Reporting Regulations.

### 7.5 Exchange Reporting Position by Year

**Exchange Reporting Position table**

| Tax Year | Mandatory third-party reporting? |
| --- | --- |
| 2024-25 | No mandatory CARF reporting yet; HMRC information powers only |
| 2025-26 | No mandatory CARF reporting yet; preparation period |
| 2026-27 | **Yes — CARF data collection from 1 Jan 2026, first reports to HMRC in 2027** |

### 7.6 Record-Keeping

**Record-Keeping table**

| Requirement | Detail |
| --- | --- |
| Retention period | At least 5 years after the 31 January filing deadline (effectively ~6 years from end of tax year) |
| Records to maintain | Full transaction logs from all exchanges, wallet addresses, S104 pool calculations, staking/mining logs, DeFi protocol records |
| Format | CSV exports preferred; screenshots acceptable as backup; on-chain records (block explorer links) recommended |

## Section 8 — Loss Offset and Carry-Forward Rules

(Unchanged across the three years.)

### 8.1 Capital Losses

**Capital Losses table**

| Rule | Detail | Authority |
| --- | --- | --- |
| In-year offset | Allowable losses MUST be set against gains of the same tax year first | TCGA 1992 S2 |
| Carry-forward | Unused losses can be carried forward indefinitely | TCGA 1992 S2(2) |
| Carry-forward limitation | Carried-forward losses can only reduce gains to the annual exempt amount (£3,000) | TCGA 1992 S3 |
| Carry-back | NOT permitted (except on death) | — |
| Reporting deadline | Losses MUST be reported to HMRC within **4 years** of the end of the tax year in which they arose | TCGA 1992 S16(2A) |
| Negligible value claim | For tokens that become worthless — treated as disposal and reacquisition at negligible value, crystallising a loss | TCGA 1992 S24(2) |

### 8.2 Income Losses (Mining/Trading)

- **Trading and misc income losses** — Trading losses from crypto mining/staking business may be offset against other income under ITA 2007 S64; Miscellaneous income losses can only offset miscellaneous income of the same type  _(ITA 2007 S64)_

### 8.3 Critical: 4-Year Loss Claim Window

If you do not report a capital loss within 4 years of the end of the tax year in which it arose, the loss is permanently lost.

**Loss Claim Window table**

| Loss arising in | Must be reported by |
| --- | --- |
| 2024-25 | 5 Apr 2029 |
| 2025-26 | 5 Apr 2030 |
| 2026-27 | 5 Apr 2031 |

## Section 9 — Anti-Avoidance: Bed-and-Breakfasting and Wash Sale Rules

### 9.1 The 30-Day Rule (TCGA 1992 S106A)

- **30-day rule** — Unchanged across all three years. If a taxpayer disposes of tokens and reacquires tokens of the same type within 30 days after the disposal, the disposal is matched to the reacquisition (not the S104 pool).  _(TCGA 1992 S106A)_

### 9.2 Same-Day Rule (TCGA 1992 S105)

- **Same-day rule** — If tokens are both acquired and disposed of on the same day, the disposal is matched to the same-day acquisition first.  _(TCGA 1992 S105)_

### 9.3 General Anti-Abuse Rule (GAAR)

- **GAAR** — The GAAR (Finance Act 2013 Part 5) may apply to artificial crypto tax avoidance arrangements.  _(Finance Act 2013 Part 5)_

### 9.4 Date-of-Disposal Manipulation Around 30 Oct 2024

- **Date manipulation scrutiny** — For 2024-25, HMRC will scrutinise late-October 2024 disposal dates given the rate increase from 30 Oct 2024. The contract date of disposal (not settlement date) governs which rate applies. Backdating risks penalty exposure and potential GAAR application.

## Section 10 — Worked Examples

### Example 1 — Same Disposal Under Three Rate Regimes (Key 3-Year Example)

**Facts:** UK higher-rate taxpayer. S104 pool: 1 BTC at £20,000 cost. Disposes of the 1 BTC for £45,000 proceeds, £75 disposal fees. Other gains for the year: nil. We compute the CGT under four scenarios: pre- and post-30 Oct 2024 within 2024-25, then 2025-26, then 2026-27.

**Common computation up to taxable gain:**

```
Proceeds                : £45,000
Less disposal fees      : £75
Net proceeds            : £44,925
Less S104 pool cost     : £20,000
Gain                    : £24,925
Less annual exempt amt  : £3,000
Taxable gain            : £21,925
```

**Scenario A — Disposal on 15 October 2024 (2024-25, pre-30 Oct rates):**
```
Rate (higher-rate)      : 20%
CGT                     : £21,925 × 20% = £4,385.00
```

**Scenario B — Disposal on 1 December 2024 (2024-25, post-30 Oct rates):**
```
Rate (higher-rate)      : 24%
CGT                     : £21,925 × 24% = £5,262.00
Extra tax vs Scenario A : £877.00 (a ~20% increase in CGT for the same gain)
```

**Scenario C — Disposal on 1 December 2025 (2025-26):**
```
Rate (higher-rate)      : 24%
CGT                     : £21,925 × 24% = £5,262.00
(Same as Scenario B — the rate is now 24% for the whole year)
```

**Scenario D — Disposal on 1 December 2026 (2026-27):**
```
Rate (higher-rate)      : 24%
CGT                     : £21,925 × 24% = £5,262.00
(Rates unchanged from 2025-26; CARF reporting now applies to the exchange)
```

**Key takeaway:** Within 2024-25 the **date of disposal matters** — a 6-week shift from pre-30 Oct to post-30 Oct increased the tax bill on the same economic transaction by £877 (4 percentage points on £21,925). From 2025-26 onwards the rate is stable at 18%/24%.

### Example 2 — 2024-25 Year Straddling Both Rate Regimes

**Facts:** UK higher-rate taxpayer with two BTC disposals in 2024-25:
- 1 BTC sold 15 Oct 2024 (pre-rate-change) — gain £10,000
- 1 BTC sold 15 Nov 2024 (post-rate-change) — gain £15,000
- Total gross gain £25,000. AEA £3,000.

**Computation:**
```
Gross gains              : £25,000
Less AEA (£3,000) allocated pro-rata to each window
  Pre-30 Oct share       : £3,000 × (£10,000 / £25,000) = £1,200
  Post-30 Oct share      : £3,000 × (£15,000 / £25,000) = £1,800

Pre-30 Oct taxable gain  : £10,000 − £1,200 = £8,800 × 20% = £1,760
Post-30 Oct taxable gain : £15,000 − £1,800 = £13,200 × 24% = £3,168

Total CGT for 2024-25    : £4,928
```

Allocate the AEA in proportion to gains in each window (HMRC's approach in the Finance Act 2024 transitional rules — confirm against final HMRC guidance for borderline cases).

### Example 3 — Simple S104 Pool, 2025-26

**Facts:** UK basic-rate taxpayer. Bought 2 BTC at £20,000 each in January 2024. Sold 1 BTC at £45,000 in August 2025. Exchange fees: £50 acquisition, £75 disposal.

```
S104 pool:
  2 BTC at £20,000 each = £40,000 + £50 fees = £40,050
  Pool cost per BTC = £20,025

Disposal of 1 BTC:
  Net proceeds    : £45,000 − £75 = £44,925
  S104 cost       : £20,025
  Gain            : £24,900
  Less AEA        : £3,000
  Taxable gain    : £21,900
  CGT @ 18%       : £3,942
```

### Example 4 — 30-Day Rule Blocks Loss (2025-26)

**Facts:** UK tax resident. S104 pool: 5 ETH, total cost £10,000 (£2,000 per ETH). Sells 5 ETH at £1,500 each (£7,500) on 1 November 2025. Rebuys 5 ETH at £1,600 each (£8,000) on 20 November 2025.

```
With 30-day rule (mandatory):
  Disposal matched to reacquisition
  Proceeds        : £7,500
  Matched cost    : £8,000
  Loss            : (£500)
  Deferred loss   : £2,000 stays in the (now-replenished) S104 pool
```

### Example 5 — Staking Income + Subsequent CGT (2026-27)

**Facts:** UK higher-rate taxpayer. Received 0.5 ETH staking rewards during 2026-27; FMV at each receipt totalled £1,800. Sold 0.5 ETH in March 2027 at £2,200. Exchange is a CARF-reporting RCASP — HMRC will receive matching data in 2028.

```
Income tax on staking:
  £1,800 × 40% = £720

CGT on disposal:
  Proceeds   : £2,200
  Cost basis : £1,800
  Gain       : £400 (within £3,000 AEA — no CGT)

Total tax  : £720
Disclosure : Tick the cryptoasset box on SA108; expect CARF data match in 2028.
```

## Self-Checks

- [ ] Have all disposals been identified (sells, swaps, crypto-to-crypto, payments for goods/services)?
- [ ] For 2024-25 disposals, is the contract date confirmed and the correct pre- or post-30 Oct rate applied?
- [ ] Have same-day and 30-day matching rules been applied before the S104 pool?
- [ ] Is the S104 pool maintained separately for each token type?
- [ ] Have mining/staking/airdrop receipts been included as income?
- [ ] Has the £3,000 annual exempt amount been applied correctly (pro-rated across windows for 2024-25 if relevant)?
- [ ] Have losses been reported within the 4-year window?
- [ ] Is the correct CGT rate applied (10/20 or 18/24) based on disposal date and taxpayer band?
- [ ] Are all values converted to GBP at the transaction date?
- [ ] Has SA108 been completed and the cryptoasset tick box selected (2024-25 onwards)?
- [ ] For 2026-27: has the client been advised about CARF reporting and KYC consistency across exchanges?
- [ ] Have DeFi transactions been analysed for beneficial ownership transfer?

## PROHIBITIONS

- NEVER assume crypto is tax-free in the UK — disposals are subject to CGT
- NEVER apply FIFO, LIFO, or specific identification — the UK REQUIRES S104 pooling with same-day and 30-day matching
- NEVER treat crypto-to-crypto swaps as non-taxable — they ARE disposals (CRYPTO22100)
- NEVER treat staking/mining income as capital gains — it is income (CRYPTO21200)
- NEVER ignore the 30-day bed-and-breakfasting rule when matching disposals
- NEVER forget to convert all values to GBP at the transaction-date exchange rate
- NEVER allow losses to go unreported beyond the 4-year claim window
- NEVER treat transfers between own wallets as disposals
- NEVER classify DeFi returns as "interest" — crypto is not money (CRYPTO61200)
- NEVER apply the 18/24% rates to disposals before 30 October 2024 — use 10/20% pre-change
- NEVER apply the 10/20% rates to disposals on or after 30 October 2024
- NEVER assume CARF reporting is in force before 1 January 2026 — but ALWAYS warn clients about the 2027 first-report data match
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a UK chartered accountant, chartered tax adviser, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
