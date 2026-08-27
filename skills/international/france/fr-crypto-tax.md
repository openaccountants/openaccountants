---
name: fr-crypto-tax
description: French cryptocurrency and digital asset taxation for individuals. Trigger on phrases like "crypto France impôt", "fiscalité crypto", "bitcoin impôt France", "ethereum déclaration France", "plus-value crypto", "PAMC crypto", "prix d'acquisition moyen pondéré", "formulaire 2086", "déclaration 2086", "cession crypto-actifs", "staking impôt France", "mining fiscalité", "airdrop fiscalité", "exonération 305 euros", "crypto flat tax France", "échange crypto-to-crypto", "stablecoin fiscalité", "Koinly France", "Waltio", "déclaration crypto France", "BNC staking". Covers the PAMC method, the EUR 305 exemption threshold, PFU 31.4%, barème option, form 2086, staking/mining/airdrops, and documentation obligations.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FR Crypto Tax

## France — Crypto-Asset Taxation (Particuliers) v1.0

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing. Get this reviewed at **openaccountants.com**.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France |
| Tax | IR + prélèvements sociaux on crypto capital gains |
| Currency | EUR only |
| Tax year | Calendar year |
| Primary legislation | art. 150 VH bis CGI |
| Key forms | 2086 (per-disposal detail), 2042-C (cases 3AN/3BN) |
| Exemption threshold | EUR 305 annual gross disposals |
| Default rate | PFU **31.4%** (12.8% IR + 18.6% PS) for 2025 income |

## Section 2 — Scope: Occasional vs Professional

This skill covers the **occasional** regime for individuals. If the activity is habitual/professional, it is reclassified as **BIC** with TNS social contributions.

**Indicators of professional activity:**
- High transaction volume
- Near-daily frequency
- Use of professional tools (bots, API, automated arbitrage)
- Crypto income constitutes primary household revenue

## Section 3 — Taxable Events (Fait Générateur)

**Taxable Events (Fait Générateur)**

| Operation | Taxable? | Notes |
| --- | --- | --- |
| Buy crypto with EUR/USD | No | Acquisition only |
| **Sell crypto for EUR/USD** | **Yes** | Disposal to fiat |
| **Pay with crypto (goods/services)** | **Yes** | Disguised disposal |
| Crypto-to-crypto exchange (BTC → ETH) | **No** | Deferral (sursis, art. 150 VH bis-I-2) |
| Crypto → stablecoin (USDC, USDT) | **No** | Stablecoins treated as crypto-assets |
| **Stablecoin → EUR/USD** | **Yes** | Disposal to fiat |
| Staking / mining / airdrop | See Section 8 | Different regime (BNC or BIC) |

- **Crypto-to-crypto deferral rule** — Exchanges between crypto-assets do not trigger taxation. Only conversion to fiat currency (or use as payment) is a taxable event.  _(art. 150 VH bis-I-2 CGI)_

## Section 4 — PAMC Method (Prix d'Acquisition Moyen Pondéré en Continu)

### Official formula

- **Capital gain formula (PAMC)** — capital_gain = disposal_price − (total_portfolio_acquisition_cost × disposal_price / portfolio_value_before_disposal)  _(art. 150 VH bis-II CGI)_

### Practical consequences

- Each disposal draws from the **global** portfolio (not FIFO, not LIFO)
- Requires tracing the **complete history** from the first purchase
- If acquisition prices are undocumented → risk of reclassification as disposal at price 0 (maximum gain)

### Recommended tools

Koinly, CoinTracking, Waltio, Cryptio. Verify that the tool correctly applies the French PAMC method.

## Section 5 — Tax Rates

### Default: PFU 31.4%

**Default: PFU 31.4%**

| Component | Rate |
| --- | --- |
| IR | 12.8% |
| PS (revenus du patrimoine, L. 136-6 CSS) | **18.6%** (LFSS 2026, applicable to 2025 disposals) |
| **Total PFU** | **31.4%** |

- **Applied on net annual gain** — Applied on the **net annual gain** (after offsetting current-year losses).

### Option barème (since revenus 2023)

- **Option barème availability and advantage** — Available since LFI 2022. **Advantageous only if TMI ≤ 11%.** The barème option is **global** — applies to all capital income for the year (dividends, interest, capital gains). Arbitrage must be performed at the global level.  _(LFI 2022)_

## Section 6 — EUR 305 Exemption Threshold

**EUR 305 Exemption Threshold**

| Annual gross disposals | Treatment |
| --- | --- |
| ≤ EUR 305 | **Total exemption** — no tax, no filing of 2086 |
| > EUR 305 | **Full taxation** on the gain (not just the excess) |

- **Trap: threshold applies to gross disposal amount** — The threshold applies to the **gross disposal amount**, not the gain. Selling EUR 500 of crypto with only EUR 10 gain still triggers taxation on the EUR 10 gain.

## Section 7 — Loss Offsetting

- **Current-year crypto losses offset current-year crypto gains** — Current-year crypto losses can offset current-year crypto gains
- **Crypto losses cannot offset securities gains** — Crypto losses cannot offset standard securities capital gains (separate bucket)
- **No carryforward of crypto losses** — No carryforward of crypto losses to future years (specific rule)

## Section 8 — Staking, Mining, Airdrops

**Separate regime from capital gains** — taxed according to the nature of the activity:

**Staking, Mining, Airdrops regime table**

| Activity | Probable regime | Notes |
| --- | --- | --- |
| Occasional staking | BNC non-professionnel | Valued in EUR at each reception date |
| Mining | BIC |  |
| Professional staking/lending | BIC |  |
| Passive airdrop (no task) | Not taxable at reception | Capital gain computed at disposal |
| Active rewards (tasks required) | BNC or salary |  |

- **Occasional staking — BNC declaration at reception** — Value in EUR at each date of receipt. Declare on 2042-C-PRO case 5HQ (micro-BNC, 34% abattement) or 5HG (réel). Micro-BNC exemption if receipts ≤ EUR 305.

**Grey zone:** DGFiP doctrine is evolving. Check latest BOFiP positions.

## Section 9 — Form 2086 (Mandatory Disclosure)

- **Form 2086 mandatory filing threshold** — Mandatory for every disposal once annual gross disposals exceed EUR 305.
- **Per-disposal details required** — - Date of disposal - Portfolio value before disposal - Total portfolio acquisition cost - Disposal price - Computed gain or loss
- **Reporting on 2042-C** — Case 3AN: net annual gain (profit); Case 3BN: net annual loss

## Section 10 — Documentation Requirements

- **Retention period and required documentation** — Retain for minimum 6 years (statute of limitations): Complete transaction history (exchange exports); Proof of acquisition dates and prices; Crypto-to-crypto exchange details (even though non-taxable — prove portfolio continuity); Wallet-to-wallet transfers (prove portfolio continuity); Staking reward exports with fiat valuation at each reception date

## Section 11 — Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Activity classification unclear | Occasional (particulier regime) |
| Acquisition cost undocumented | EUR 0 (maximum gain — conservative from tax authority perspective) |
| Staking income classification unclear | BNC non-professionnel |
| PFU vs barème unclear | PFU (no global commitment) |
| Stablecoin → stablecoin | Non-taxable (crypto-to-crypto) |

## Section 12 — Key Legal References

**Key Legal References**

| Rule | Article |
| --- | --- |
| Crypto capital gains regime | art. 150 VH bis CGI |
| PAMC method | art. 150 VH bis-II CGI |
| Crypto-to-crypto deferral | art. 150 VH bis-I-2 CGI |
| Professional/habitual activity (BIC) | art. 34 CGI |
| PS (revenus du patrimoine) | art. L. 136-6 CSS |
| LFSS 2026 CSG increase | loi n° 2025-1403, art. 12 |
| BOFiP PV crypto | BOI-RPPM-PVBMC-30 |
| BOFiP BNC staking/mining | BOI-BNC-CHAMP-10-10-20-40 |

## Footer

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: **openaccountants.com** | Report errors: **github.com/openaccountants/openaccountants***

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
