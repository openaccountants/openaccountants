---
name: belgium-crypto-tax
description: Use this skill whenever asked about Belgium cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Belgium", "Bitcoin Belgium", "cryptocurrency gains Belgium", "crypto income Belgium", "staking Belgium", "mining income Belgium", "NFT tax Belgium", "goede huisvader crypto", "bon père de famille crypto", "speculative income Belgium", "miscellaneous income Belgium", "divers inkomen crypto", "revenus divers crypto", "professional income crypto Belgium", "Ruling Commission crypto", "Service des Décisions Anticipées crypto", "SDA crypto", "Belgian crypto audit", or any question about the income tax, capital gains, or reporting treatment of cryptocurrency, tokens, or digital assets for Belgian tax residents. Covers the three-tier classification system (normal management / speculative / professional), SDA ruling criteria, the 25% wealth threshold, and the upcoming 2026 capital gains regime. ALWAYS read this skill before touching any Belgium crypto work.
version: 1.0
jurisdiction: BE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - belgium-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium Crypto Tax

## Belgium Crypto / Digital Assets Tax Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Belgium (Koninkrijk België / Royaume de Belgique) |
| Tax | Personal income tax (personenbelasting / impôt des personnes physiques) on crypto |
| Currency | EUR |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Wetboek van de Inkomstenbelastingen 1992 (WIB 92) / Code des Impôts sur les Revenus 1992 (CIR 92) — Articles 23, 90, 171 |
| Tax authority | FOD Financiën / SPF Finances |
| Advance rulings body | Dienst Voorafgaande Beslissingen (DVB) / Service des Décisions Anticipées (SDA) |
| Filing portal | MyMinfin (Tax-on-web) |
| Filing deadline | Typically late June–mid July of the following year (varies; paper earlier) |
| EU reporting | DAC8 / CARF — exchanges report from 2026 |
| Three-tier system | (1) Tax-free (normal management); (2) 33% + municipal surcharge (speculative); (3) Progressive 25%–50% + social security (professional) |
| 2026 change | New 10% capital gains tax on crypto from 1 Jan 2026 for normal management gains (EUR 10,000 annual exemption) |
| Validated by | Pending — requires sign-off by a Belgian belastingconsulent / conseil fiscal |
| Skill version | 1.0 |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether normal management or speculative | Treat as speculative (taxable at 33%) |
| Unknown whether speculative or professional | Treat as professional (progressive rates) |
| Unknown cost basis | STOP — cannot compute gain without acquisition cost |
| Unknown residency status | STOP — determines worldwide taxation |
| Crypto > 25% of movable wealth | Strong indicator of speculative/abnormal management per SDA practice |
| Mining/staking activity | Treat as professional income unless clearly de minimis |

## Section 2 -- Classification Rules

### 2.1 The Three-Tier System (Income Year 2025)

Belgium applies a **facts-and-circumstances** classification to determine how crypto gains are taxed. There is no statutory bright-line test. The three tiers are:

**Three-Tier System table**  _(Art. 90, al. 1, 1° WIB 92; Art. 171, 1° WIB 92; Art. 23 §1 WIB 92)_

| Tier | Dutch | French | Tax Rate | Legal Basis |
| --- | --- | --- | --- | --- |
| 1. Normal management of private patrimony | Normaal beheer van privévermogen / goede huisvader | Gestion normale du patrimoine privé / bon père de famille | **TAX FREE** | Art. 90, al. 1, 1° WIB 92 (exclusion) |
| 2. Speculative gains | Speculatieve meerwaarden | Plus-values spéculatives | **33%** + municipal surcharge (avg. 7–8%) | Art. 90, al. 1, 1° and Art. 171, 1° WIB 92 |
| 3. Professional income | Beroepsinkomen | Revenus professionnels | **25%–50%** progressive + social security | Art. 23 §1 WIB 92 |

### 2.2 Classification Factors (SDA Ruling Practice)

The Dienst Voorafgaande Beslissingen (DVB/SDA) uses a detailed questionnaire to classify crypto investors. Key factors:

**Classification Factors table**

| Factor | Normal Management (Tax-Free) | Speculative (33%) | Professional (25–50%) |
| --- | --- | --- | --- |
| Crypto as % of movable wealth | < 25% (SDA informal threshold) | > 25% | High and systematic |
| Transaction frequency | Low; buy-and-hold | High volume trading | Very high; daily trading |
| Holding period | Long (months to years) | Short (days to weeks) | Very short; day trading |
| Strategy | Passive; long-term appreciation | Active trading; momentum | Full-time activity |
| Leverage / borrowing | None | May use | Regular use |
| Automation / bots | None | Possible | Systematic use |
| Professional knowledge/background | No finance background | Some expertise | Finance/IT professional |
| Mining activity | None | Minor | Regular commercial mining |
| Forum/community participation | Minimal | Active | Influencer/educator |
| Third-party management | None | None | Manages for others |
| Income dependency | Has separate primary income | Has other income | Crypto is primary income |

### 2.3 The 25% Wealth Threshold

- **25% wealth threshold rule** — The SDA applies an informal but consistently enforced threshold: if more than 25% of a taxpayer's movable wealth is invested in cryptocurrency, the SDA quasi-automatically classifies the management as "abnormal" (speculative). This threshold is controversial but well-documented in published rulings.
- **Critical note on tracking percentage** — The percentage must be tracked from the date of first investment through each year-end. The SDA questionnaire requires a table showing this percentage at each key date.

### 2.4 Advance Rulings (DVB/SDA)

**Advance Rulings table**

| Aspect | Detail |
| --- | --- |
| Who can apply | Any Belgian tax resident (individual) |
| What it provides | Binding advance determination of tax classification |
| Validity | Typically limited to 1 year; contains reservations for legislative changes |
| Cost | Free |
| Processing time | 3–6 months |
| Questionnaire | 17+ questions covering all factors above (updated 2026 for new regime) |
| Binding effect | Binds the tax administration unless facts change or legislation is amended |

Citation: Loi du 24 décembre 2002 / Wet van 24 december 2002 (DVB/SDA organic law); DVB/SDA annual reports and published rulings

## Section 3 -- Rate Tables

### 3.1 Tax Rates by Classification (Income Year 2025)

**Tax Rates by Classification table**  _(Art. 130–145 WIB 92; Art. 171 WIB 92; FOD Financiën "Belastingtarieven — Inkomstenjaar 2025 (Aanslagjaar 2026)")_

| Classification | Federal Rate | Municipal Surcharge | Effective Rate | Social Security |
| --- | --- | --- | --- | --- |
| Normal management | 0% | N/A | **0%** | No |
| Speculative (miscellaneous income) | 33% | ~7–8% of federal tax | **~35.4–35.6%** | No |
| Professional income bracket 1 | 25% on 0–€16,320 | ~7–8% | ~26.8–27.0% | Yes (~20.5% self-employed) |
| Professional income bracket 2 | 40% on €16,320–€28,800 | ~7–8% | ~42.8–43.2% | Yes |
| Professional income bracket 3 | 45% on €28,800–€49,840 | ~7–8% | ~48.2–48.6% | Yes |
| Professional income bracket 4 | 50% on €49,840+ | ~7–8% | ~53.5–54.0% | Yes |

- **Personal tax allowance (belastingvrije som)** — EUR 10,910 EUR (income year 2025)  _(Art. 130–145 WIB 92; Art. 171 WIB 92; FOD Financiën "Belastingtarieven — Inkomstenjaar 2025 (Aanslagjaar 2026)")_

### 3.2 Staking / Passive Income Classification

- **SDA staking classification rule** — The SDA has classified staking rewards as roerend inkomen (movable income / income from movable property) under Art. 17 §1 WIB 92, analogous to interest under Art. 19, 1° WIB 92.  _(SDA ruling March 2025; Art. 17, 19, 261–269 WIB 92)_

**Staking / Passive Income table**  _(SDA ruling March 2025; Art. 17, 19, 261–269 WIB 92)_

| Income Type | Rate | Withholding |
| --- | --- | --- |
| Staking rewards (interest analogy) | 30% (précompte mobilier / roerende voorheffing) | Self-assessed if no Belgian intermediary |

### 3.3 Upcoming 2026 Regime (Important Context for 2025 Planning)

From 1 January 2026, a new capital gains tax applies:

**2026 Regime table**  _(Programme law (Programmawet) 2025; Art. 90, al. 1, 9°, c) WIB 92 (new))_

| Aspect | Detail |
| --- | --- |
| Rate on "normal management" gains | 10% (replaces tax-free treatment) |
| Annual exemption | EUR 10,000 per taxpayer |
| Historical gains exempt | Gains accrued up to 31 December 2025 are exempt if documented |
| Speculative gains | Still taxed at 33% |
| Professional gains | Still taxed at progressive rates |
| Carry-forward of unused exemption | Up to EUR 1,000/year for max 5 years |

## Section 4 -- Cost Basis Methods

### 4.1 Accepted Methods

Belgium does not prescribe a specific cost basis method for crypto. In practice:

**Accepted Methods table**

| Method | Status |
| --- | --- |
| FIFO (First In, First Out) | Accepted; most commonly used |
| Average cost | Accepted |
| LIFO (Last In, First Out) | Not standard; may be challenged |
| Specific identification | Accepted if well documented |

### 4.2 Cost Basis Components

- **Acquisition cost (aanschaffingswaarde) components** — Purchase price in EUR at the date of acquisition; Exchange fees and commissions; Network/gas fees directly attributable to the purchase; Bank transfer fees for deposits to exchanges

### 4.3 No Expense Deduction for Speculative Income

- **No expense deduction for speculative income** — Critical rule: For gains taxed as miscellaneous income (33%), no deduction is permitted for expenses — only the acquisition cost can offset the sale proceeds.  _(Art. 97 WIB 92)_

For professional income, normal business expense deductions apply.

## Section 5 -- DeFi, Staking, Mining, and Airdrop Treatment

### 5.1 Mining

**Mining table**

| Scale | Classification | Tax Treatment |
| --- | --- | --- |
| Occasional/small scale | Likely miscellaneous income (speculative) | 33% + municipal surcharge |
| Regular/commercial | Professional income | Progressive rates 25%–50% + social security |

The SDA and OATR (Opsporingsdienst) tend to quickly classify mining as professional activity due to its regular, organised nature.

### 5.2 Staking

**Staking table**

| Aspect | Treatment |
| --- | --- |
| SDA classification (March 2025 ruling) | Movable income (roerend inkomen) — interest analogy |
| Tax rate | 30% (roerende voorheffing rate) |
| Tax point | When rewards are received/accessible |
| Reporting | Separate obligation from capital gains; Part 2 of tax return (roerende inkomsten) |
| Cost basis for future sale | FMV at receipt date |

### 5.3 DeFi Lending

**DeFi Lending table**

| Activity | Treatment |
| --- | --- |
| Depositing crypto into lending protocol | Uncertain — may constitute a disposal or may be treated as a loan |
| Interest received | Likely movable income at 30% (interest analogy) |
| Withdrawing from lending protocol | Uncertain |

Warning: There is no specific Belgian guidance on DeFi lending. The SDA has not published rulings on LP positions, yield farming, or DeFi protocols. Conservative approach: treat deposits as disposals.

### 5.4 Liquidity Providing

- **Liquidity Providing conservative treatment** — No specific guidance. Conservative treatment: Deposit into LP = disposal of underlying crypto (capital gain/loss triggered); LP tokens = new acquisition at FMV; Withdrawal from LP = disposal of LP tokens

### 5.5 Airdrops

**Airdrops table**

| Type | Treatment |
| --- | --- |
| Gratuitous airdrop | Cost basis EUR 0; taxable event at disposal only |
| Airdrop for service/action | Income at FMV when received; classification depends on overall investor profile |

### 5.6 Hard Forks

- **Hard Forks conservative treatment** — No specific guidance. Conservative treatment: Cost basis of forked coin = EUR 0; Gain = full proceeds on disposal; Classification follows normal three-tier analysis

## Section 6 -- NFT Treatment

### 6.1 General NFT Classification

Belgium applies the same three-tier classification to NFTs as to other crypto assets:

**General NFT Classification table**

| Scenario | Likely Classification |
| --- | --- |
| Buy and hold NFT art long-term | Normal management (tax-free in 2025) |
| Frequent NFT trading (flipping) | Speculative (33%) |
| NFT creation and sale as regular activity | Professional income (25–50%) |

### 6.2 NFT-Specific Considerations

**NFT-Specific Considerations table**

| Aspect | Treatment |
| --- | --- |
| NFT purchased with crypto | Two transactions: disposal of crypto + acquisition of NFT |
| NFT sold for crypto | Disposal of NFT + acquisition of crypto |
| NFT creation (artist) | If regular → professional income |
| NFT royalties | Likely movable income or professional income depending on regularity |

### 6.3 TOB (Tax on Stock Exchange Transactions)

- **TOB does not apply to crypto/NFTs** — The Taks op de Beursverrichtingen (TOB) / Taxe sur les Opérations de Bourse does NOT apply to cryptocurrency or NFT transactions. The TOB is limited to transactions in financial instruments executed through a Belgian intermediary on a regulated market.  _(Art. 120–123 of the Code of Miscellaneous Taxes and Duties (Wetboek Diverse Rechten en Taksen))_

## Section 7 -- Reporting Requirements

### 7.1 Tax Return Filing

**Tax Return Filing table**

| Classification | Where to Report |
| --- | --- |
| Normal management (tax-free) | No reporting obligation for gains; but crypto accounts must be declared to CAP (see below) |
| Speculative / miscellaneous income | Part 2 of tax return, Section XV — Diverse inkomsten / Revenus divers (Code 1440/2440) |
| Professional income | Part 1 of tax return — Beroepsinkomsten / Revenus professionnels |
| Staking rewards (movable income) | Part 2 — Roerende inkomsten / Revenus mobiliers |

### 7.2 Centraal Aanspreekpunt (CAP) — Foreign Account Declaration

**CAP table**

| Requirement | Detail |
| --- | --- |
| What must be declared | Foreign crypto exchange accounts (Binance, Coinbase, Kraken, etc.) |
| To whom | National Bank of Belgium — Centraal Aanspreekpunt (CAP) |
| Deadline | Before filing the tax return |
| Penalty for non-declaration | Fines and potential criminal prosecution |
| Belgian exchanges | Not required (domestic accounts) |

### 7.3 Filing Deadlines (Income Year 2025)

**Filing Deadlines table**

| Method | Deadline |
| --- | --- |
| Paper filing | Late June 2026 (exact date published annually) |
| Tax-on-web (e-filing) | Mid-July 2026 (exact date published annually) |
| Via tax advisor (mandataris) | Late October 2026 |

### 7.4 Record-Keeping

**Record-Keeping table**

| Requirement | Detail |
| --- | --- |
| Retention period | 7 years from the assessment year |
| Records to maintain | Full transaction logs, cost basis calculations, portfolio value at each year-end, documentation of crypto-to-movable-wealth ratio |
| SDA ruling documentation | Keep the SDA questionnaire responses and ruling decision indefinitely |
| Burden of proof | On taxpayer for normal management claim; on administration for professional reclassification |

### 7.5 DAC8 / CARF (From 2026)

- **DAC8/CARF reporting** — Crypto service providers report Belgian user transaction data to FOD Financiën; Increased audit risk for undeclared crypto gains; Belgian tax authorities have been increasingly auditing crypto holders since 2023

## Section 8 -- Loss Offset and Carry-Forward

### 8.1 Loss Rules by Classification

**Loss Rules by Classification table**

| Classification | Loss Offset | Carry-Forward |
| --- | --- | --- |
| Normal management | N/A (gains are tax-free, so losses are irrelevant) | No |
| Speculative (miscellaneous income) | Losses can **only** offset gains within the **same category** (miscellaneous/speculative crypto gains) in the **same tax year** | **No carry-forward** |
| Professional income | Losses deductible as business losses; can offset other professional income | Carry-forward possible under normal business loss rules |

### 8.2 Critical Limitation — Speculative Losses

- **Speculative losses ring-fencing** — Speculative crypto losses CANNOT offset: Employment income; Rental income; Movable income (dividends, interest); Other types of miscellaneous income not in the same sub-category. This is one of the harshest aspects of Belgian crypto taxation.  _(Art. 90 and Art. 103 WIB 92)_

### 8.3 2026 Regime — Loss Rules

- **2026 loss rules** — Under the new 10% capital gains tax from 2026: Losses are deductible only against gains in the same sub-category of financial assets; Crypto losses cannot offset, e.g., share gains; No carry-forward of losses

## Section 9 -- Anti-Avoidance Rules

### 9.1 General Anti-Abuse Provision

- **General anti-abuse provision** — Belgium has a general anti-abuse provision that allows the tax administration to recharacterise transactions lacking genuine economic substance. This includes artificial structures designed to avoid crypto taxation.  _(Art. 344, §1 WIB 92)_

### 9.2 Substance Over Form

- **Substance over form analysis** — The SDA and courts apply a substance-over-form analysis. Even if a taxpayer formally holds crypto long-term, the overall pattern of behaviour determines classification. Key case law precedents include the Court of Cassation rulings of 1968/1969 defining professional vs private activities.

### 9.3 Increased Audit Activity

Belgian tax authorities have significantly increased crypto-related audits since 2023. Common triggers: Large bank deposits from crypto exchange withdrawals; Inconsistencies between declared income and lifestyle; Information received from foreign tax authorities; DAC8/CARF reports (from 2026); Undeclared CAP accounts

### 9.4 Penalties

**Penalties table**

| Offence | Penalty |
| --- | --- |
| Late filing | Administrative fines (EUR 50–1,250) |
| Undeclared crypto income | Tax surcharge of 10%–200% of unpaid tax |
| Undeclared foreign accounts (CAP) | Separate fines; potential criminal prosecution |
| Fraud | Criminal penalties; tax surcharge up to 200% |

## Section 10 -- Worked Examples

### Example 1 -- Normal Management (Tax-Free in 2025)

**Input:** Belgian resident, employed engineer. Bought 2 BTC in January 2023 at EUR 20,000 each. Sold 2 BTC in November 2025 at EUR 55,000 each. Total 3 trades in 3 years. Crypto represents 15% of movable wealth. No leverage, no bots, no mining.

**Classification analysis:**
```
Factors:
  - Low frequency: 1 buy + 1 sell in 3 years                → Normal management
  - Long holding period: ~34 months                          → Normal management
  - Crypto < 25% of movable wealth (15%)                    → Normal management
  - No leverage, no automation                               → Normal management
  - Employed separately; crypto not primary income            → Normal management
  - Passive buy-and-hold strategy                            → Normal management

Classification: Normal management of private patrimony

Gain:  2 × (EUR 55,000 - EUR 20,000) = EUR 70,000
Tax:   EUR 0 (tax-free under normal management)
```

**Recommendation:** Obtain an SDA ruling to confirm classification, especially given the significant gain amount.

### Example 2 -- Speculative Gains (33%)

**Input:** Belgian resident. Made 150+ trades in 2025 across 4 exchanges. Mix of short-term and medium-term positions. Crypto represents 40% of movable wealth. Net gain of EUR 25,000 after costs. No leverage but uses portfolio tracking tools actively.

**Classification analysis:**
```
Factors:
  - High frequency: 150+ trades                             → Speculative
  - Crypto > 25% threshold (40%)                            → Speculative (SDA quasi-automatic)
  - Mix of holding periods                                   → Speculative
  - Active management with tools                             → Speculative
  - Not full-time; has other employment                      → Not professional

Classification: Speculative — miscellaneous income (Art. 90, 1° WIB 92)

Gain:           EUR 25,000
Federal tax:    EUR 25,000 × 33% = EUR 8,250
Municipal surcharge (assume 7.5%): EUR 8,250 × 7.5% = EUR 618.75
Total tax:      EUR 8,868.75

Reporting: Part 2, Section XV — Diverse inkomsten (Code 1440)
```

### Example 3 -- Professional Income

**Input:** Belgian resident, no other employment. Full-time crypto trader. 1,000+ trades in 2025. Uses leverage and automated bots. Manages a small fund for friends. Net income EUR 80,000.

**Classification analysis:**
```
Factors:
  - Very high frequency: 1,000+ trades                      → Professional
  - Full-time activity; primary income source                → Professional
  - Leverage and automation                                  → Professional
  - Manages for third parties                                → Professional

Classification: Professional income (Art. 23, §1 WIB 92)

Taxable income: EUR 80,000
Personal allowance: EUR 10,910 (tax-free)
Remaining: EUR 69,090

Tax computation:
  EUR 16,320 × 25%              = EUR 4,080.00
  (EUR 28,800 - EUR 16,320) × 40% = EUR 4,992.00
  (EUR 49,840 - EUR 28,800) × 45% = EUR 9,468.00
  (EUR 69,090 - EUR 49,840) × 50% = EUR 9,625.00
  Subtotal:                        EUR 28,165.00
  Less personal allowance credit:  EUR 10,910 × 25% = EUR -2,727.50
  Federal tax:                     EUR 25,437.50
  Municipal surcharge (7.5%):      EUR 1,907.81
  Total income tax:                EUR 27,345.31
  Social security (~20.5%):        EUR 80,000 × 20.5% = EUR 16,400.00
  TOTAL TAX BURDEN:                EUR 43,745.31 (~54.7%)

Reporting: Part 1 — Beroepsinkomsten / Revenus professionnels
```

## Self-Checks

Before finalising any Belgium crypto computation, verify:

- [ ] Three-tier classification analysis completed with documented factors
- [ ] Crypto-to-movable-wealth ratio calculated (25% threshold)
- [ ] All amounts in EUR at transaction date exchange rates
- [ ] Cost basis method consistently applied (FIFO or average — document choice)
- [ ] Speculative losses NOT offset against other income types
- [ ] Staking rewards reported separately as movable income (30%)
- [ ] Foreign exchange accounts declared to CAP (National Bank)
- [ ] Municipal surcharge added to federal tax
- [ ] Social security calculated for professional classification
- [ ] Record of SDA ruling (if obtained) retained
- [ ] Planning for 2026 regime change considered (10% tax on normal management gains)

## PROHIBITIONS

- NEVER assume all crypto gains are tax-free in Belgium — only "normal management" gains are exempt (and only for 2025; 10% from 2026)
- NEVER rely solely on holding period to determine classification — the SDA considers multiple factors holistically
- NEVER ignore the 25% movable wealth threshold — it is the most heavily weighted factor in SDA practice
- NEVER offset speculative crypto losses against employment or other income — they are ring-fenced
- NEVER forget to declare foreign exchange accounts to the CAP (National Bank)
- NEVER treat mining as normal management — the SDA/OATR considers mining inherently professional or speculative
- NEVER ignore municipal surcharges when computing tax — they add ~7–8% to the federal rate
- NEVER present a single ruling as universally applicable — each SDA ruling is specific to the taxpayer's facts
- NEVER compute gains without verified cost basis records
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a belastingconsulent, conseil fiscal, or equivalent licensed practitioner in Belgium) before filing or acting upon.

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
