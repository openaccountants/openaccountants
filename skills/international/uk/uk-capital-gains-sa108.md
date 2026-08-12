---
name: uk-capital-gains-sa108
description: Use this skill whenever asked about UK capital gains tax for individuals. Trigger on phrases like "SA108", "capital gains tax", "CGT UK", "annual exempt amount", "disposal", "chargeable gain", "crypto CGT UK", "share sale UK", "property disposal CGT", "PPR relief", "principal private residence", "BADR", "BADR 18%", "Business Asset Disposal Relief", "Entrepreneurs' Relief", "Investors Relief 18%", "carried interest April 2026", "CGT 18% 24%", "bed and breakfasting", "30-day rule", "Section 104 pool", "negligible value claim", "CGT losses", "60-day reporting", "residential property CGT", or any question about computing, filing, or reporting capital gains on the UK Self Assessment return. Covers SA108 form, CGT rates, reliefs, crypto as CGT asset, share matching rules, property CGT reporting, and loss treatment. ALWAYS read this skill before touching any UK CGT work.
version: 2.0
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on: - uk-income-tax-sa100
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Capital Gains Sa108

## UK Capital Gains Tax (SA108) Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Capital Gains SA108

- **Basic rate taxpayer** — 18%  _(TCGA 1992)_
- **Higher/additional rate** — 24%  _(TCGA 1992)_
- **BADR qualifying gains (2025-26)** — 14%  _(TCGA s.169H)_
- **BADR qualifying gains (2026-27)** — 18%  _(Finance Act 2025)_
- **BADR lifetime limit** — £1,000,000  _(TCGA 1992)_
- **2024-25 individuals** — £3,000  _(TCGA 1992)_
- **2024-25 individuals** — £3,000  _(TCGA 1992)_
- **2025-26 trustees** — £1,500  _(TCGA 1992)_
- **Last months always exempt** — 9 months  _(TCGA s.222-226)_
- **Letting relief cap** — £40,000  _(TCGA s.223)_
- **Garden/grounds exempt** — Up to 0.5 hectares  _(TCGA s.222)_
- **Deadline** — 60 days from completion  _(TCGA 1992)_
- **Late reporting penalty** — £100 initial  _(TMA 1970)_

## Section 1 -- Quick Reference

**Section 1 Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Tax | Capital Gains Tax (CGT) |
| Currency | GBP only |
| Tax year | 6 April to 5 April |
| Primary legislation | Taxation of Chargeable Gains Act 1992 (TCGA 1992) |
| Supporting legislation | Finance Act 2024 (rate changes from 30 Oct 2024); Finance Act 2024 BADR/IR two-step uplift; Autumn Budget 2024; TCGA ss. 1H, 1I (rates); TCGA s. 222-226 (PPR); TCGA s. 169H-169S (BADR); TCGA ss. 104, 106A, 107 (share matching) |
| Tax authority | HMRC |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline | 31 January following the tax year (SA return); 60 days for UK residential property (CGT on UK Property return) |
| SA108 form | Capital Gains Tax Summary supplementary pages to SA100 |
| HMRC crypto guidance | HMRC CG12100+ (Cryptoassets Manual) |
| Validated by | Verified by James Power on 2026-06-03 |
| Skill version | 2.0 |

### 1.1 Three-Year Headline Rate Comparison (2024-25 / 2025-26 / 2026-27)

**Three-Year Headline Rate Comparison**

| Item | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Annual Exempt Amount (individuals) | £3,000 | £3,000 | £3,000 |
| AEA (trustees) | £1,500 | £1,500 | £1,500 |
| Non-residential CGT (basic / higher) | 10% / 20% pre-30 Oct 2024; **18% / 24% from 30 Oct 2024** | **18% / 24%** | **18% / 24%** |
| Residential property CGT (basic / higher) | 18% / 24% | 18% / 24% | 18% / 24% |
| BADR rate (up to £1m lifetime) | **10%** | **14%** | **18%** |
| Investors' Relief rate | **10%** | **14%** | **18%** |
| Investors' Relief lifetime limit | £10m → £1m (dropped 30 Oct 2024) | £1m | £1m |
| Carried interest (fund managers) | 28% | **32%** (transitional from Apr 2025) | **Reclassified as trading income (income tax rates; no CGT treatment) from Apr 2026** |

All rates frozen across the three-year window unless explicitly shown changing.

### 1.2 CGT Rates — Year by Year

#### 2024-25 (split-year rate regime due to Autumn Budget 2024)

**6 April 2024 to 29 October 2024**

| Asset type | Basic rate | Higher / additional rate |
| --- | --- | --- |
| Residential property (non-PPR) | 18% | 24% |
| Other assets (shares, crypto, non-residential) | 10% | 20% |
| BADR qualifying gains | 10% | 10% |
| Investors' Relief qualifying gains | 10% | 10% |

**30 October 2024 to 5 April 2025**

| Asset type | Basic rate | Higher / additional rate |
| --- | --- | --- |
| All assets (residential and non-residential) | **18%** | **24%** |
| BADR qualifying gains | 10% | 10% |
| Investors' Relief qualifying gains | 10% | 10% |

#### 2025-26

**2025-26 rates**

| Asset type | Basic rate | Higher / additional rate |
| --- | --- | --- |
| All assets | 18% | 24% |
| BADR qualifying gains | **14%** | **14%** |
| Investors' Relief qualifying gains | **14%** | **14%** |
| Carried interest | 32% (transitional) | 32% (transitional) |

#### 2026-27

**2026-27 rates**

| Asset type | Basic rate | Higher / additional rate |
| --- | --- | --- |
| All assets | 18% | 24% |
| BADR qualifying gains | **18%** | **18%** |
| Investors' Relief qualifying gains | **18%** | **18%** |
| Carried interest | **Reclassified — taxed as trading income at income tax rates + Class 4 NIC. NO CGT treatment.** | — |

### 1.3 Annual Exempt Amount — Historic and Frozen Range

**AEA Historic and Frozen Range**

| Tax year | Individuals | Trustees |
| --- | --- | --- |
| 2022-23 | £12,300 | £6,150 |
| 2023-24 | £6,000 | £3,000 |
| 2024-25 | £3,000 | £1,500 |
| 2025-26 | £3,000 | £1,500 |
| 2026-27 | £3,000 | £1,500 |

The £3,000 AEA is frozen across the full three-year planning window.

### 1.4 From April 2026 — Watch List

Two structural changes apply from 6 April 2026 that materially shift planning for business owners and fund managers:

1. **BADR and Investors' Relief rates rise to 18%** (the second step of the Finance Act 2024 two-step uplift: 10% → 14% → 18%). The lifetime limit remains £1m. After this step, BADR/IR effectively offer only a 6-percentage-point discount over the standard 24% higher rate — much narrower than the historic 14-point gap (10% vs 24%). Pre-6 April 2026 disposals at 14% remain valuable; clients with imminent exits should weigh acceleration.

2. **Carried interest reclassified as trading income.** From 6 April 2026, carried interest received by private fund managers is no longer a capital gain. It is taxed as trading income — subject to income tax (up to 45%) and Class 4 NIC. The 32% CGT rate that applied transitionally in 2025-26 is withdrawn. There is no CGT treatment available from this date.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown acquisition cost | STOP — cannot compute gain |
| Unknown whether PPR applies | Do NOT apply PPR (taxable in full) |
| Unknown residency status | STOP — affects CGT liability |
| Unknown whether basic or higher rate | Compute at higher rate (conservative) |
| Unknown whether disposal is connected persons | Treat as connected (market value rule applies) |
| Unknown disposal date around 30 Oct 2024 | Use post-30 Oct rates (conservative) |
| Unknown disposal date around 6 Apr 2025 / 6 Apr 2026 BADR step | Use the LATER (higher) BADR rate |

## Section 2 -- Computation Framework

### 2.1 Basic CGT Calculation

- **Basic CGT Calculation** — Disposal proceeds (or market value if gift/connected person) Less: Allowable costs - Original acquisition cost - Incidental acquisition costs (stamp duty, legal fees, survey) - Enhancement expenditure (capital improvements) - Incidental disposal costs (estate agent, legal, advertising) = Chargeable gain (or allowable loss) Less: Annual Exempt Amount (£3,000) = Taxable gain Tax = Taxable gain × applicable rate (based on income band and disposal date)

### 2.2 Rate Band Allocation

- **Rate Band Allocation** — Unused basic rate band = £50,270 - taxable income (after personal allowance) If gain fits within unused basic rate band → basic rate CGT (18%) If gain exceeds unused basic rate band → split: 18% within band, 24% on excess

CGT rates depend on where the gain falls relative to the basic rate band:

## Section 3 -- Share Matching Rules (Section 104 Pool)

**Share Matching Rules priority order**

| Priority | Rule | Reference |
| --- | --- | --- |
| 1 | Same-day acquisitions | TCGA s. 105(1) |
| 2 | Acquisitions within 30 days AFTER disposal (bed and breakfasting rule) | TCGA s. 106A |
| 3 | Section 104 pool (average cost of all shares held) | TCGA s. 104 |

UK share disposals follow strict matching rules in this priority order:

### 3.1 Section 104 Pool

- **Section 104 pool calculation** — Pool cost = total cost of all acquisitions Pool quantity = total shares held Average cost per share = Pool cost ÷ Pool quantity
- **On disposal allowable cost** — allowable cost = number of shares sold × average cost per share

The Section 104 pool is a rolling average cost of all shares of the same class in the same company:

### 3.2 Bed and Breakfasting (30-Day Rule)

- **30-day rule** — If you sell shares and repurchase the same shares within 30 days, the disposal is matched to the repurchase — NOT the Section 104 pool. This prevents crystallising a gain/loss while retaining the same economic position. Applies to: shares, securities, crypto assets (per HMRC guidance CRYPTO22200).  _(HMRC guidance CRYPTO22200)_

## Section 4 -- Crypto Assets as CGT Assets

### 4.1 HMRC Position

- **HMRC crypto treatment** — HMRC treats cryptoassets as property for CGT purposes (not currency). Each disposal is a chargeable event.

**Crypto CGT event treatment table**

| Event | CGT Treatment |
| --- | --- |
| Selling crypto for fiat (GBP, USD, etc.) | Disposal — gain/loss computed |
| Exchanging one crypto for another | Disposal of the first crypto |
| Using crypto to pay for goods/services | Disposal at market value |
| Gifting crypto | Disposal at market value |
| Transfer between own wallets | NOT a disposal |
| Receiving airdrop (no consideration given) | Acquisition at zero cost |
| Mining/staking rewards | Income when received; acquisition cost = income value |
| DeFi lending | Depends on terms — may or may not be disposal |

### 4.2 Crypto Matching Rules

- **Crypto matching rules** — Same as share matching rules: same-day → 30-day → Section 104 pool. Each crypto token type has its own pool (e.g. separate pools for BTC, ETH, SOL).

### 4.3 Crypto Reporting on SA108

From 2024-25, SA108 includes dedicated crypto boxes:
- Box 5.9A: Cryptoasset gains included in total gains
- Box 5.10A: Cryptoasset losses included in total losses

## Section 5 -- Principal Private Residence (PPR) Relief

### 5.1 Full PPR Relief

- **Full PPR relief** — If a property has been your only or main residence throughout ownership, the entire gain is exempt from CGT.

### 5.2 Partial PPR Relief

**Partial PPR Relief table**

| Period | Treatment |
| --- | --- |
| Periods of occupation as main residence | Exempt |
| Last 9 months of ownership (regardless of occupation) | Always exempt (deemed occupation) |
| Periods of absence due to employment (up to 4 years) | Exempt if resided before and after |
| Periods of overseas employment (any length) | Exempt if resided before and after |
| Letting relief | Up to £40,000 if part of PPR was let as residential accommodation |
| Garden/grounds | Exempt up to 0.5 hectares (or larger if appropriate to the property) |

### 5.3 PPR and Nominal Occupation

- **Nominal occupation challenge** — HMRC may challenge PPR claims where occupation was nominal (e.g. a few weeks). Must demonstrate genuine occupation as main residence — utility bills, electoral roll, correspondence address.

## Section 6 -- Business Asset Disposal Relief (BADR) and Investors' Relief

### 6.1 BADR (formerly Entrepreneurs' Relief)

**BADR feature table**

| Feature | Detail |
| --- | --- |
| Lifetime limit | £1,000,000 (unchanged across 2024-25, 2025-26, 2026-27) |
| Rate — pre-6 Apr 2025 | **10%** |
| Rate — 6 Apr 2025 to 5 Apr 2026 | **14%** |
| Rate — from 6 Apr 2026 | **18%** |
| Qualifying assets | Shares in a trading company (5% holding, 2-year ownership, officer/employee); sole trader/partnership business |
| Claim deadline | 1st anniversary of 31 January following tax year of disposal |
| Interaction with AEA | AEA used first; BADR applies to remaining gain |

- **Two-step uplift basis** — The two-step uplift (10% → 14% → 18%) is set by Finance Act 2024 following the Autumn Budget 2024.  _(Finance Act 2024)_

### 6.2 Investors' Relief (IR)

**Investors' Relief feature table**

| Feature | Detail |
| --- | --- |
| Lifetime limit | £10m before 30 Oct 2024; **£1m from 30 Oct 2024 onwards** |
| Rate — pre-6 Apr 2025 | **10%** |
| Rate — 6 Apr 2025 to 5 Apr 2026 | **14%** |
| Rate — from 6 Apr 2026 | **18%** |
| Qualifying conditions | Newly issued ordinary shares in unlisted trading company; held ≥3 years; subscriber must not be an employee/officer |

Investors' Relief tracks BADR on rates but applies to external investors (non-employees) in qualifying unlisted trading companies.

### 6.3 Carried Interest (Private Fund Managers)

**Carried interest treatment table**

| Period | Treatment |
| --- | --- |
| Pre-Apr 2025 | 28% CGT rate |
| 6 Apr 2025 onwards (transitional) | **32% CGT rate** |
| From 6 Apr 2026 | **Reclassified as trading income — taxed at income tax rates (up to 45%) plus Class 4 NIC. No CGT treatment.** |

Carried interest is out of scope for SA108 from 2026-27 — it migrates to SA103 (self-employment) / employment pages depending on structure.

## Section 7 -- 60-Day Property CGT Reporting

**60-Day Property CGT reporting feature table**

| Feature | Detail |
| --- | --- |
| Applies to | Disposals of UK residential property by UK residents (where CGT is due) and ALL disposals by non-residents |
| Deadline | 60 days from completion of the sale |
| Form | CGT on UK Property return (online HMRC service) |
| Payment | CGT due with the 60-day return (payment on account) |
| SA return | Still required — CGT on UK Property return is reported on SA108, with credit for CGT already paid |
| Penalty for late reporting | £100 (initial); further penalties accrue |
| Exemption from reporting | If no CGT due (e.g. full PPR relief applies) — reporting still recommended |

## Section 8 -- Losses

### 8.1 Loss Rules

**Loss Rules table**

| Rule | Detail |
| --- | --- |
| Current year losses | Must be set against gains of the same year (even if this wastes the AEA) |
| Brought-forward losses | Used only to reduce gains to the AEA level (not below) |
| Carry forward | Indefinite |
| Carry back | Only on death (to the 3 previous tax years) |
| Connected person losses | Can only be set against gains from disposals to the same connected person |
| Negligible value claim | Treat asset as disposed of and reacquired at negligible value — creates an allowable loss |
| Claim deadline | 4 years from end of tax year |

### 8.2 Reporting Losses

- **Reporting losses** — Losses must be reported to HMRC to be available for carry forward. Use SA108 or write to HMRC. Time limit: 4 years from end of the tax year in which the loss arose.

## Section 9 -- Transaction Pattern Library

### 9.1 Disposal Patterns

**Disposal patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SHARE SALE, STOCK SALE, BROKER PAYOUT | Disposal — compute gain/loss | Match using share matching rules |
| PROPERTY SALE, SOLICITOR COMPLETION FUNDS | Disposal — compute gain/loss | 60-day reporting required for residential |
| BINANCE WITHDRAWAL, COINBASE SELL, CRYPTO SALE | Disposal — compute gain/loss | Match using crypto pool rules |
| GIFT OF SHARES, GIFT OF PROPERTY | Disposal at market value | Gift = disposal at MV for CGT |
| LIQUIDATION DISTRIBUTION, COMPANY WIND-UP | Disposal — capital distribution | May qualify for BADR if trading company |
| EIS DISPOSAL, SEIS DISPOSAL | Check relief conditions | May be exempt if held ≥3 years |

### 9.2 Acquisition Cost Evidence

**Acquisition cost evidence table**

| Pattern | Classification |
| --- | --- |
| SHARE PURCHASE, BROKER BUY | Acquisition cost (add dealing fees) |
| STAMP DUTY, SDLT | Incidental acquisition cost |
| SOLICITOR FEES (acquisition) | Incidental acquisition cost |
| SURVEY, VALUATION (on purchase) | Incidental acquisition cost |
| RENOVATION (capital improvement) | Enhancement expenditure |

## Section 10 -- Worked Examples

### Example 1 -- Share Disposal (2024-25, After 30 Oct)

**Input:** Sold 1,000 shares on 15 November 2024 for £25,000. Section 104 pool average cost: £10 per share. No same-day or 30-day matching. Basic rate taxpayer with £5,000 unused basic rate band.

**Computation:**
```
Proceeds:        £25,000
Cost (1,000 × £10): £10,000
Gain:            £15,000
Less AEA:        £3,000
Taxable gain:    £12,000

Rate (post-30 Oct): 18% basic / 24% higher
Basic rate portion: £5,000 × 18% = £900
Higher rate portion: £7,000 × 24% = £1,680
Total CGT:       £2,580
```

### Example 2 -- Crypto Disposal

**Input:** Sold 0.5 BTC on 1 February 2025 for £20,000. BTC Section 104 pool: 2 BTC at average cost £8,000 per BTC. No same-day or 30-day match.

**Computation:**
```
Proceeds:         £20,000
Cost (0.5 × £8,000): £4,000
Gain:             £16,000
Less AEA:         £3,000
Taxable gain:     £13,000
Rate (post-30 Oct): 18%/24% depending on income
```

### Example 3 -- PPR with Letting Relief

**Input:** Owned house 10 years. Lived in it for 6 years, let it for 4 years. Total gain £200,000.

**Computation:**
```
Exempt (PPR): 6 years + last 9 months = 6.75 years
Total ownership: 10 years
PPR fraction: 6.75/10 = 67.5%
PPR exempt: £200,000 × 67.5% = £135,000
Chargeable: £200,000 - £135,000 = £65,000
Letting relief: lower of (a) £40,000, (b) PPR exempt amount, (c) chargeable letting gain = £40,000
Chargeable after letting relief: £65,000 - £40,000 = £25,000
Less AEA: £3,000
Taxable: £22,000
```

### Example 4 -- BADR Rate Change Across Three Years (SAME Business Sale)

**Scenario:** Sole trader sells qualifying trading business for a gain of £900,000 (all within £1m BADR lifetime limit; no other gains in year; AEA available).

The same disposal is modelled across three completion dates to show the cost of delay:

```
Gain:                          £900,000
Less AEA:                      £3,000
Taxable BADR gain:             £897,000
```

**BADR rate change table**

| Completion date | Tax year | BADR rate | CGT |
| --- | --- | --- | --- |
| 5 April 2025 | 2024-25 | **10%** | **£89,700** |
| 5 April 2026 | 2025-26 | **14%** | **£125,580** |
| 6 April 2026 | 2026-27 | **18%** | **£161,460** |

**Real cost of delay:**
- 2024-25 → 2025-26 step: extra **£35,880** CGT (≈40% increase)
- 2025-26 → 2026-27 step: extra **£35,880** CGT
- 2024-25 → 2026-27 total: extra **£71,760** CGT (an 80% increase on the original BADR bill)

Planning implication: where a sale is commercially imminent and BADR-qualifying, completing before 6 April of the relevant rate-step year materially reduces tax. Conversely, where the deal is dependent on commercial readiness, the cost of slipping a tax year should be quantified for the client before completion is timed.

### Example 5 -- BADR Disposal in 2024-25 (Original Example)

**Input:** Sole trader sells business for £500,000 gain. Owned >2 years. Claims BADR. Disposes before 6 April 2025.

**Computation:**
```
Gain: £500,000
Less AEA: £3,000
Taxable: £497,000
BADR rate: 10% (pre-6 Apr 2025)
CGT: £49,700
```
Within £1M lifetime limit. Deduct £500,000 from remaining lifetime allowance.

## Section 11 -- Edge Cases

### 11.1 Non-Residents

- **Non-resident CGT liability** — From April 2015, non-UK residents are liable to CGT on disposals of UK residential property. From April 2019, extended to all UK land and property (including commercial). Non-residents get the same AEA as UK residents.

### 11.2 Bed and ISA

- **Bed and ISA rule** — Selling shares and immediately repurchasing within an ISA wrapper: the 30-day rule does NOT apply to ISA acquisitions. The disposal is matched to the Section 104 pool, and the ISA acquisition starts with a fresh cost base.

### 11.3 Spouse Transfers

- **Spouse transfer rule** — Transfers between spouses/civil partners are at no gain/no loss. The receiving spouse inherits the original cost base. This can be used to utilise both AEAs.

### 11.4 Death

- **Death and CGT** — No CGT on death. Assets pass to the estate at market value at date of death (probate value). This effectively wipes out any accrued gain.

### 11.5 BADR/IR Disposals Straddling a Rate Step

- **Rate determination by disposal date** — The rate is set by the date of disposal (generally the date of unconditional contract under TCGA s. 28), not the completion date. Conditional contracts crystallise on the date the last condition is satisfied. Where a contract is exchanged shortly before a rate-step date, evidence of the contract date should be retained for HMRC.  _(TCGA s. 28)_

### 11.6 Carried Interest Crossing 6 April 2026

- **Carried interest transition rule** — Carry receipts arising on or after 6 April 2026 fall fully within the trading income regime, regardless of when the underlying fund or carry vehicle was set up. Pre-6 April 2026 receipts use the 32% transitional CGT rate.

## PROHIBITIONS

- NEVER compute CGT without knowing the acquisition cost — STOP and request evidence
- NEVER apply PPR relief without confirming genuine occupation
- NEVER ignore the 30-day bed and breakfasting rule for shares and crypto
- NEVER forget the 60-day reporting requirement for UK residential property disposals
- NEVER apply pre-30 October 2024 rates (10%/20%) to non-residential disposals after 30 October 2024
- NEVER apply the 10% BADR rate to disposals on or after 6 April 2025 (use 14% for 2025-26 and 18% from 6 April 2026)
- NEVER apply the 14% BADR rate to disposals on or after 6 April 2026 (use 18%)
- NEVER apply CGT treatment to carried interest received on or after 6 April 2026 — it is trading income
- NEVER exceed the £1M BADR lifetime limit
- NEVER apply the £10m Investors' Relief lifetime limit to disposals on or after 30 October 2024 (limit is £1m)
- NEVER treat transfers between own crypto wallets as disposals
- NEVER carry back losses (except on death)
- NEVER waste the AEA by offsetting brought-forward losses below £3,000
- NEVER present CGT computations as definitive — always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
