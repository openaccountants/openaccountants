---
name: india-crypto-tax
description: Use this skill whenever asked about India cryptocurrency or virtual digital asset (VDA) taxation. Trigger on phrases like "crypto tax India", "Bitcoin India tax", "VDA tax", "Section 115BBH", "194S TDS crypto", "crypto TDS India", "virtual digital asset India", "crypto income India", "NFT tax India", "mining tax India", "staking tax India", "WazirX tax", "CoinDCX tax", "crypto loss India", "Schedule VDA", "ITR crypto", "30% crypto tax India", "1% TDS crypto", or any question about the income tax, TDS, or reporting treatment of cryptocurrency, tokens, NFTs, or virtual digital assets under Indian tax law. Covers Finance Act 2022 amendments (Sections 115BBH, 194S, 2(47A)), the no-loss-offset rule, ITR Schedule VDA, and advance tax obligations. ALWAYS read this skill before touching any India crypto work.
version: 1.0
jurisdiction: IN
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mayur Deokar
review_status: current
depends_on:
  - in-income-tax
category: crypto
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Crypto Tax

## India Crypto / Virtual Digital Assets Tax Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mayur Deokar** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Crypto (VDA)

- **Health & Education Cess** — 4% on tax  _(Finance Act)_
- **Rate (ITA 2025 replacement)** — New section as per new Income Tax Act 2025 applicable from financial year fy 2026-27 is Section 393(1). Rate remains same.  _(ITA s 194S)_
- **Threshold (general)** — ₹10,000 aggregate per FY  _(ITA s 194S)_
- **Threshold (specified persons)** — ₹50,000 (individual/HUF with turnover ≤ ₹1 Cr)  _(ITA s 194S)_
- **Form** — Form 26QE (→ Form 141 under ITA 2025)  _(CBDT)_
- **Deductible** — Purchase price only  _(ITA s 115BBH(2))_
- **Mined/staked/airdrop tokens** — Cost = ₹0  _(ITA s 115BBH)_
- **ITR form** — ITR-2 or ITR-3 with Schedule VDA  _(CBDT notification)_
- **Deadline** — 31 July (non-audit) / 31 October (audit)  _(ITA s 139)_
- **Flat rate on VDA gains** — 30% (s 115BBH)  _(ITA s 115BBH)_
- **Effective rate (before surcharge)** — 31.20%  _(Calculated)_
- **Loss offset** — NOT permitted — crypto losses cannot offset ANY income  _(ITA s 115BBH(2))_
- **Loss carry-forward** — NOT permitted  _(ITA s 115BBH)_
- **TDS on VDA Transfer (s 194S) — Rate** — 1% of consideration (rate unchanged); citation updated to Section 393(1) of the new Income Tax Act 2025, applicable from FY 2026-27  _(ITA s 194S; new Income Tax Act 2025 s 393(1))_
- **TDS Threshold (general)** — ₹10,000 aggregate per FY  _(ITA s 194S)_
- **TDS Threshold (specified persons)** — ₹50,000 (individual/HUF with turnover ≤ ₹1 Cr)  _(ITA s 194S)_
- **Form** — Form 26QE (→ Form 141 under ITA 2025)  _(CBDT)_
- **Cost of Acquisition — Deductible** — Purchase price only  _(ITA s 115BBH(2))_
- **Cost of improvement** — NOT deductible  _(ITA s 115BBH(2)(a))_
- **Transfer expenses (fees, gas)** — NOT deductible  _(ITA s 115BBH)_
- **Mined/staked/airdrop tokens cost basis** — Cost = ₹0  _(ITA s 115BBH)_
- **ITR form** — ITR-2 or ITR-3 with Schedule VDA  _(CBDT notification)_
- **Deadline** — 31 July (non-audit) / 31 October (audit)  _(ITA s 139)_

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Tax | Income Tax on Virtual Digital Assets (VDA) |
| Currency | INR (Indian Rupee) — all values in INR |
| Tax year (Assessment Year) | Financial Year 1 April – 31 March (FY 2025-26 = 1 Apr 2025 – 31 Mar 2026; AY 2026-27) |
| Primary legislation | Income Tax Act, 1961: Section 2(47A) (VDA definition), Section 115BBH (flat 30% tax), Section 194S (1% TDS); Finance Act, 2022 (amendments effective 1 April 2022 / 1 July 2022) |
| Replacement under ITA 2025 | Income-tax Act, 2025: Section 393(1) Sl. No. 8(vi) replaces Section 194S for TDS |
| Tax authority | Central Board of Direct Taxes (CBDT); Income Tax Department |
| Filing portal | incometax.gov.in (e-filing portal) |
| Tax rate on VDA gains | Flat 30% (plus 4% health & education cess = effective 31.2%) |
| Surcharge | Applicable based on total income slab (10%–37%) on the 30% |
| TDS rate | 1% on consideration for transfer of VDA (Section 194S) |
| TDS threshold | ₹10,000 (general) / ₹50,000 (specified persons — individuals/HUF with turnover ≤ ₹1 crore or profession receipts ≤ ₹50 lakh) |
| Loss offset | NOT PERMITTED — crypto losses cannot be set off against ANY income |
| Loss carry-forward | NOT PERMITTED |
| Reporting form | ITR-2 or ITR-3 with Schedule VDA |
| Filing deadline | 31 July of the assessment year (31 July 2026 for FY 2025-26); 31 October for audit cases |
| Validated by | Pending — requires sign-off by an Indian Chartered Accountant |
| Skill version | 1.0 |

### VDA Definition (Section 2(47A) / Income-tax Act, 2025 S. 2(57))

**VDA Definition table**

| Category | Included |
| --- | --- |
| (a) Cryptographic tokens | Any information, code, number, or token generated through cryptographic means providing a digital representation of value — includes BTC, ETH, SOL, etc. |
| (b) NFTs | Non-fungible tokens or any token of similar nature |
| (c) Central Government notified | Any other digital asset the Central Government may notify |
| Excluded | Indian currency, foreign currency, CBDCs (Digital Rupee) |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown cost of acquisition | Zero (maximises gain) — STOP if material |
| Unknown whether business or investment | Treat as transfer of VDA under 115BBH (30% flat) |
| Unknown whether mining income or business income | Treat as "income from other sources" (still taxable) |
| Unknown FMV at receipt | Use exchange price at time of transaction |
| Gift of VDA — unknown value | Obtain FMV; if ≥ ₹50,000, taxable in hands of recipient |

## Section 2 — Classification Rules

### The 115BBH Regime — No Capital vs Income Distinction

- **115BBH flat rate scope** — Unlike most jurisdictions, India does not distinguish between capital gains and income for crypto taxation. Section 115BBH applies a flat 30% tax on any income arising from the transfer of a VDA, regardless of: Holding period (no short-term vs long-term distinction); Frequency of trading; Whether taxpayer is an investor or trader; Whether gain is revenue or capital in nature

**Classification Question table**

| Classification Question | Answer |
| --- | --- |
| Is crypto a capital asset in India? | The government treats income from VDA transfer under a special regime (S.115BBH) separate from the regular capital gains provisions |
| Does holding period matter? | NO — flat 30% regardless of holding period |
| Does trader vs investor distinction matter? | NO — flat 30% in either case |
| Can crypto be treated as business income? | Only mining/staking/providing services may be classified as business income or income from other sources; the transfer gain is always 30% under 115BBH |

### What constitutes a "transfer" under 115BBH

- **transfer definition** — Sale of VDA for fiat (INR or foreign currency); Exchange of one VDA for another VDA (crypto-to-crypto swap); Use of VDA as payment for goods or services; Gift of VDA (except to specified relatives under Section 56); Any disposal or alienation of VDA

## Section 3 — Rate Table

### Tax on Transfer of VDA (Section 115BBH)

**Tax on Transfer of VDA table**

| Component | Rate | Source |
| --- | --- | --- |
| Base tax on VDA transfer income | 30% | S. 115BBH(1)(a) |
| Health & Education Cess | 4% on tax | S. 136C |
| Effective rate (before surcharge) | 31.20% | — |

### Surcharge (based on total income including VDA)

**Surcharge table**

| Total Income | Surcharge Rate | Effective VDA Tax Rate |
| --- | --- | --- |
| Up to ₹50 lakh | Nil | 31.20% |
| ₹50 lakh – ₹1 crore | 10% | 34.32% |
| ₹1 crore – ₹2 crore | 15% | 35.88% |
| ₹2 crore – ₹5 crore | 25% | 39.00% |
| Above ₹5 crore | 37% | 42.74% |

Note: Marginal relief applies at surcharge thresholds.

### TDS on Transfer of VDA (Section 194S)

**TDS on Transfer of VDA table**

| Element | Detail |
| --- | --- |
| Rate | 1% of consideration |
| Threshold (general) | ₹10,000 aggregate in a financial year |
| Threshold (specified persons) | ₹50,000 aggregate (individual/HUF with business turnover ≤ ₹1 crore or profession receipts ≤ ₹50 lakh in preceding year) |
| Who deducts | Buyer of VDA / exchange platform |
| When | At time of credit or payment, whichever is earlier |
| TDS on crypto-to-crypto | Both parties may be liable (buyer of each VDA in the swap) |
| Form | Form 26QE (now Form 141 under ITA 2025) |
| Deposit deadline | Within 30 days from end of month of deduction |

## Section 4 — Cost Basis

### Permitted Deductions

**Permitted Deductions table**

| Deductible | Permitted? | Detail |
| --- | --- | --- |
| Cost of acquisition | YES | Purchase price of the VDA only |
| Cost of improvement | NO | Explicitly disallowed under S.115BBH(2)(a) |
| Transfer expenses | NO | Exchange fees, gas fees — NOT deductible |
| Any other deduction | NO | No deduction under any section of the Act |
| Depreciation | NO | Not applicable |

**This is the harshest cost basis regime globally.** Only the original purchase price can be deducted — no fees, no commissions, no gas costs.

### Cost Basis Methods

India does not prescribe FIFO/LIFO/average cost for individuals. The Act simply refers to "cost of acquisition." In practice:

**Cost Basis Methods table**

| Method | Status |
| --- | --- |
| FIFO | Commonly used by exchanges and software |
| Average cost | Acceptable in practice |
| Specific identification | Acceptable if documented |
| LIFO | Not standard; no prohibition |

The key constraint is that **only cost of acquisition** matters — method of identifying which lot was sold is secondary.

### Zero-Cost Scenarios

**Zero-Cost Scenarios table**

| Scenario | Cost of Acquisition |
| --- | --- |
| Mined tokens | ₹0 (no cost of acquisition; full value is gain) |
| Staking rewards received | ₹0 (if not purchased) |
| Airdrop tokens | ₹0 |
| Hard fork tokens | ₹0 |
| Gifted VDA (below ₹50,000) | Cost to the previous owner (for computing S.115BBH gain on subsequent transfer) |

## Section 5 — DeFi, Staking, Mining, and Airdrops

### 5.1 Mining

**Mining table**

| Aspect | Treatment |
| --- | --- |
| Receipt of mined tokens | Taxable as "income from other sources" or "business income" at applicable slab rates |
| Cost basis of mined tokens | FMV at time of mining (if taxed as income on receipt) becomes the cost of acquisition for future transfer |
| Subsequent transfer | 30% flat tax under S.115BBH on (proceeds – cost of acquisition) |

**Note:** There is ambiguity on whether mining income is taxed at slab rates (as other income) AND THEN the transfer gain is separately taxed at 30%. Conservative approach: tax as income on receipt, then 30% on disposal gain from that FMV cost basis.

### 5.2 Staking

**Staking table**

| Aspect | Treatment |
| --- | --- |
| Staking rewards received | Income from other sources at FMV on receipt — taxed at slab rates |
| Cost basis of staking rewards | FMV at receipt date |
| Subsequent transfer of staked tokens | 30% under S.115BBH |

### 5.3 Airdrops

**Airdrops table**

| Scenario | Treatment |
| --- | --- |
| Airdrop requiring action | Income at FMV on receipt; slab rates |
| Unsolicited airdrop | Potentially taxable as income under Section 56(2)(x) if value > ₹50,000 |
| Transfer of airdropped tokens | 30% under S.115BBH; cost of acquisition = ₹0 or FMV if already taxed as income |

### 5.4 DeFi Lending/Yield

**DeFi Lending/Yield table**

| Activity | Treatment |
| --- | --- |
| Interest/yield from DeFi protocols | Income from other sources; taxed at slab rates |
| LP token receipt (deposit into pool) | May constitute transfer of VDA — 30% on any gain |
| LP token withdrawal | Transfer — 30% on gain |
| Impermanent loss | No explicit relief; loss on VDA transfer cannot offset anything |

### 5.5 Hard Forks

**Hard Forks table**

| Scenario | Treatment |
| --- | --- |
| New tokens from hard fork | Cost of acquisition = ₹0 |
| Transfer of forked tokens | 30% on full proceeds (zero cost basis) |
| Original tokens | Cost basis unchanged |

## Section 6 — NFT Treatment

NFTs are explicitly included in the VDA definition under Section 2(47A)(b).

**NFT Treatment table**

| Event | Treatment |
| --- | --- |
| Purchase of NFT | Acquisition — record cost |
| Sale of NFT | Transfer of VDA — 30% flat tax on gain under S.115BBH |
| Creation and sale (artist) | If business income: slab rates; if transfer of VDA: 30% |
| Royalty on secondary sale | Income from other sources; slab rates |
| NFT-for-NFT swap | Transfer of VDA on both sides — 30% on each gain |
| Gift of NFT (value > ₹50,000) | Taxable in hands of recipient under S.56(2)(x) |
| NFT becomes worthless | Loss — cannot be offset or carried forward |

## Section 7 — Reporting Requirements

### 7.1 ITR Forms

**ITR Forms table**

| Taxpayer Type | Applicable ITR | Schedule |
| --- | --- | --- |
| Individual with salary + VDA income | ITR-2 | Schedule VDA |
| Individual/HUF with business income + VDA | ITR-3 | Schedule VDA |
| Company | ITR-6 | Schedule VDA |

### 7.2 Schedule VDA (Virtual Digital Asset)

Schedule VDA requires the following for each VDA transaction:

**Schedule VDA fields table**

| Field | Detail |
| --- | --- |
| Type of VDA | Cryptocurrency, NFT, other |
| Date of transfer | DD/MM/YYYY |
| Date of acquisition | DD/MM/YYYY |
| Head of income | Income from transfer of VDA |
| Cost of acquisition | In INR |
| Consideration received | In INR |
| Income from transfer | Gain (consideration – cost) |

### 7.3 TDS Reporting

**TDS Reporting table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Form 26QE / Form 141 | TDS on VDA transfer | Within 30 days from end of month |
| Form 26AS / AIS | Annual Information Statement — reflects TDS deducted | Available on e-filing portal |
| Form 67 | For claiming foreign tax credit (if VDA traded on foreign exchange and tax paid abroad) | Before filing ITR |

### 7.4 Key Deadlines

**Key Deadlines table**

| Deadline | Date (FY 2025-26 / AY 2026-27) |
| --- | --- |
| Advance tax — 1st instalment | 15 June 2025 (15% of total estimated tax) |
| Advance tax — 2nd instalment | 15 September 2025 (45% cumulative) |
| Advance tax — 3rd instalment | 15 December 2025 (75% cumulative) |
| Advance tax — 4th instalment | 15 March 2026 (100%) |
| ITR filing deadline (non-audit) | 31 July 2026 |
| ITR filing deadline (audit cases) | 31 October 2026 |
| Belated return | 31 December 2026 |

## Section 8 — Loss Offset and Carry-Forward Rules

### The absolute prohibition on loss utilisation

**Loss prohibition table**

| Rule | Detail | Authority |
| --- | --- | --- |
| Loss offset against other income | **NOT PERMITTED** | S. 115BBH(2)(b) |
| Loss offset against other VDA gains | **NOT PERMITTED** — loss from one VDA cannot offset gain from another VDA | S. 115BBH(2)(b) |
| Loss carry-forward | **NOT PERMITTED** | S. 115BBH(2)(b) |
| Loss from other heads against VDA income | **NOT PERMITTED** — losses from any other head cannot reduce VDA income | S. 115BBH(1)(a) read with S.115BBH(2) |
| Infrastructure/business expenses | **NOT DEDUCTIBLE** against VDA transfer income | S. 115BBH(2)(a) |

**This is the most restrictive loss regime in any major jurisdiction.** If you lose ₹5 lakh on BTC and gain ₹5 lakh on ETH in the same year, you pay 30% on ₹5 lakh (the ETH gain) with no offset for the BTC loss.

### Example of the no-offset rule

```
BTC: Bought ₹10,00,000, Sold ₹5,00,000 → Loss: (₹5,00,000) — CANNOT USE
ETH: Bought ₹3,00,000, Sold ₹8,00,000 → Gain: ₹5,00,000

Tax = 30% × ₹5,00,000 = ₹1,50,000 + 4% cess = ₹1,56,000
The ₹5,00,000 BTC loss is permanently lost.
```

## Section 9 — Anti-Avoidance Rules

### 9.1 No Wash Sale Rule (but irrelevant)

- **wash sale irrelevance** — India has no specific wash sale rule for crypto. However, this is irrelevant because: Losses cannot be offset against anything anyway (S.115BBH(2)(b)); There is no benefit to crystallising a loss since it cannot be used  _(S.115BBH(2)(b))_

### 9.2 Anti-Avoidance Provisions

**Anti-Avoidance Provisions table**

| Provision | Effect |
| --- | --- |
| General Anti-Avoidance Rule (GAAR) — Chapter X-A | Applies to impermissible avoidance arrangements; can recharacterise VDA transactions |
| Section 56(2)(x) — Gift taxation | VDA received without consideration or for inadequate consideration (>₹50,000) is taxable as income of the recipient |
| Benami Transactions | Holding VDA in another person's name is covered under the Benami Transactions (Prohibition) Act |
| Transfer pricing | Applicable to international VDA transactions between related parties |

### 9.3 TDS as Anti-Avoidance

- **TDS dual purpose** — The 1% TDS under Section 194S serves a dual purpose: Revenue collection at source; Creating an audit trail — every VDA transfer is tracked via Form 26AS/AIS

## Section 10 — Worked Examples

### Example 1 — Simple BTC Sale

**Input:** Indian resident individual. Bought 1 BTC at ₹20,00,000 in January 2025. Sold 1 BTC at ₹50,00,000 in September 2025. Exchange fee: ₹5,000 (NOT deductible). Total other income: ₹8,00,000.

**Computation:**
```
Consideration:            ₹50,00,000
Cost of acquisition:      ₹20,00,000
Income from VDA transfer: ₹30,00,000

Tax on VDA: 30% × ₹30,00,000 = ₹9,00,000
Cess: 4% × ₹9,00,000       = ₹36,000
Total VDA tax:                ₹9,36,000

Surcharge: Total income = ₹8,00,000 + ₹30,00,000 = ₹38,00,000
  Below ₹50 lakh → Nil surcharge

TDS already deducted by exchange: 1% × ₹50,00,000 = ₹50,000
  (creditable against total tax liability)

Net VDA tax payable: ₹9,36,000 – ₹50,000 = ₹8,86,000
Exchange fee of ₹5,000 is NOT deductible.
```

### Example 2 — Multiple VDAs, No Loss Offset

**Input:** Indian resident. FY 2025-26 transactions:
- Sold SOL: Cost ₹2,00,000, Proceeds ₹5,00,000, Gain ₹3,00,000
- Sold DOGE: Cost ₹4,00,000, Proceeds ₹1,00,000, Loss (₹3,00,000)
- Received 0.1 ETH staking reward: FMV ₹25,000

**Computation:**
```
SOL gain: ₹3,00,000 → Tax: 30% = ₹90,000
DOGE loss: (₹3,00,000) → CANNOT offset against SOL gain
Staking income: ₹25,000 → Taxed at applicable slab rate (not 30%)

VDA transfer tax: ₹90,000 + 4% cess = ₹93,600
Staking income tax: at slab rate on ₹25,000

Total: ₹93,600 + slab tax on ₹25,000
The DOGE loss of ₹3,00,000 is permanently lost.
```

### Example 3 — Gift of VDA

**Input:** A receives 0.5 BTC as gift from a friend (non-relative). FMV at time of gift: ₹15,00,000. A later sells for ₹20,00,000.

**Computation:**
```
Gift taxation (S. 56(2)(x)):
  FMV of gift: ₹15,00,000 (exceeds ₹50,000)
  Taxable as income from other sources: ₹15,00,000
  Tax: at applicable slab rate

On subsequent transfer (S. 115BBH):
  Proceeds: ₹20,00,000
  Cost of acquisition: ₹0 (cost to previous owner for gifts from
    non-relatives — or FMV if S.49 applies)
  Gain: ₹20,00,000
  Tax: 30% × ₹20,00,000 = ₹6,00,000 + cess

Note: There is potential double taxation on the FMV amount.
Escalate gift of VDA cases to a Chartered Accountant.
```

## Self-Checks

- [ ] Has the 30% flat rate (plus cess and surcharge) been applied to ALL VDA transfer income?
- [ ] Have losses been correctly excluded from any offset (no inter-VDA, no inter-head offset)?
- [ ] Is only the cost of acquisition deducted — no fees, commissions, or improvement costs?
- [ ] Has 1% TDS been accounted for (either by exchange or buyer in P2P)?
- [ ] Is Schedule VDA completed for every VDA transaction?
- [ ] Has staking/mining income been separately classified under "income from other sources"?
- [ ] Have advance tax obligations been considered (15 June, 15 Sep, 15 Dec, 15 Mar)?
- [ ] Is the correct ITR form used (ITR-2 or ITR-3)?
- [ ] Have gifts of VDA been checked against the ₹50,000 threshold under S.56(2)(x)?
- [ ] Has TDS credit been verified in Form 26AS / AIS?

## PROHIBITIONS

- NEVER offset crypto losses against any income — it is explicitly prohibited under S.115BBH(2)(b)
- NEVER deduct exchange fees, gas fees, or any cost other than cost of acquisition
- NEVER apply capital gains exemptions (like S.54, S.54F) to VDA income
- NEVER treat VDA differently based on holding period — there is no LTCG/STCG distinction for VDA
- NEVER ignore the 1% TDS obligation on VDA transfers
- NEVER assume mining/staking income falls under the 30% regime — it is typically "income from other sources" at slab rates
- NEVER apply loss carry-forward for VDA — it does not exist
- NEVER ignore advance tax obligations for VDA income
- NEVER treat transfers between own wallets as taxable transfers
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

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
