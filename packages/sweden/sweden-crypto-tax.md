---
name: sweden-crypto-tax
description: Use this skill whenever asked about Sweden cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Sweden", "Bitcoin Sweden", "kryptovaluta skatt", "cryptocurrency gains Sweden", "crypto income Sweden", "staking Sweden", "mining income Sweden", "NFT tax Sweden", "K4 form crypto", "Skatteverket crypto", "genomsnittsmetoden", "average cost method Sweden", "DeFi tax Sweden", "Inkomstdeklaration crypto", "kapitalvinst krypto", or any question about the income tax, capital gains, or reporting treatment of cryptocurrency, tokens, or digital assets for Swedish tax residents. Covers Skatteverket guidance on crypto as "andra tillgångar", the mandatory average cost method, K4 reporting, mining/staking income treatment, and DAC8/CARF reporting from 2026. ALWAYS read this skill before touching any Sweden crypto work.
version: 1.0
jurisdiction: SE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - sweden-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden Crypto Tax

## Sweden Crypto / Digital Assets Tax Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Sweden (Konungariket Sverige) |
| Tax | Capital income tax on cryptocurrency (kapitalinkomstskatt) |
| Currency | SEK (all values must be converted to SEK at transaction date) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary authority | Inkomstskattelagen (1999:1229) — Income Tax Act, Chapter 44 (capital gains), Chapter 48 (other assets) |
| Administrative guidance | Skatteverket ställningstaganden on kryptovalutor (multiple, updated periodically) |
| Tax authority | Skatteverket (Swedish Tax Agency) |
| Filing portal | Skatteverket e-tjänst — Inkomstdeklaration 1 |
| Filing deadline | 2 May of the following year (e.g. 2 May 2026 for income year 2025) |
| EU reporting | DAC8 / CARF — crypto service providers report to Skatteverket from 2026 (Riksdag decision 26 November 2025) |
| Capital gains rate | 30% flat on gains |
| Loss deduction | 70% of capital losses deductible (30% lost permanently) |
| Cost basis method | Genomsnittsmetoden (average cost method) — mandatory |
| Reporting form | Bilaga K4, Avsnitt D (Övriga tillgångar) |
| Validated by | Pending — requires sign-off by a Swedish auktoriserad revisor or skattejurist |
| Skill version | 1.0 |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown whether hobby mining or business | Treat as hobby (inkomst av tjänst) unless clear business indicators |
| Unknown cost basis | STOP — cannot compute gain without omkostnadsbelopp |
| Unknown whether personal NFT or investment NFT | Treat as kapitalplacering (K4 avsnitt D — taxable at 30%) |
| Unknown residency status | STOP — affects worldwide taxation obligation |
| Crypto-to-crypto swap classification | Treat as taxable disposal (avyttring) |

## Section 2 -- Classification Rules

### 2.1 Crypto as "Andra Tillgångar" (Other Assets)

- **Crypto classification** — Skatteverket classifies all cryptocurrency (kryptovalutor/kryptotillgångar) as "andra tillgångar" (other assets) for capital gains purposes. They are not classified as currency, securities, or financial instruments under Swedish tax law.

Key legislative references:
- Inkomstskattelagen (IL) Chapter 44 — general capital gains provisions
- IL Chapter 48 — specific rules for "andra tillgångar"
- IL Chapter 41 § 1–2 — income from capital (inkomst av kapital)

### 2.2 Taxable Events

**Taxable Events table**

| Event | Taxable? | Treatment |
| --- | --- | --- |
| Selling crypto for SEK/fiat | Yes | Capital gain/loss, K4 avsnitt D |
| Crypto-to-crypto swap (e.g. BTC → ETH) | Yes | Disposal of first crypto; acquisition of second |
| Paying for goods/services with crypto | Yes | Disposal at market value in SEK at payment date |
| Receiving salary in crypto | Yes | Employment income (inkomst av tjänst) at FMV when received |
| Mining rewards | Yes | Income at FMV when received (see Section 5) |
| Staking rewards | Yes | Interest income (ränteinkomst) at FMV when received |
| Lending crypto (e.g. DeFi lending) | Yes | Transfer to lending protocol is likely a disposal |
| Receiving airdrop | Depends | Taxable if received for a service; gratuitous may not be taxable until sold |
| Transfer between own wallets | No | Not a disposal — no tax event |
| HODLing (holding without selling) | No | No tax event until disposal |

### 2.3 No Trading vs Investment Distinction

- **No trading vs investment distinction** — Unlike Malta and some other jurisdictions, Sweden does not distinguish between trading and investment for crypto taxation purposes. All crypto capital gains are taxed at the flat 30% rate regardless of holding period or trading frequency. There is no "investor exemption" for long-term holders.

## Section 3 -- Rate Tables

### 3.1 Capital Income Tax (Inkomst av Kapital)

**Capital Income Tax table**

| Type | Rate | Citation |
| --- | --- | --- |
| Capital gains on crypto | 30% flat | IL Chapter 65 § 7 |
| Loss deduction on crypto | 70% of loss deductible | IL Chapter 48 § 24, Chapter 44 |
| Interest income (staking/lending) | 30% flat | IL Chapter 42 |

### 3.2 Capital Loss Offset Rules

**Capital Loss Offset Rules table**  _(IL Chapter 67 § 10; Skatteverket "Belopp och procent — inkomstår 2025")_

| Scenario | Deduction Rate |
| --- | --- |
| Crypto loss against crypto gain (same category — andra tillgångar) | 100% offset within category |
| Net loss in andra tillgångar against other capital income | 70% deductible |
| Net capital income deficit ≤ SEK 100,000 | 30% skattereduktion (tax credit against municipal tax) |
| Net capital income deficit > SEK 100,000 | 30% on first SEK 100,000 + 21% on excess |

### 3.3 Earned Income Tax (Mining/Business Activity)

If mining or other crypto activity is classified as earned income (inkomst av tjänst or inkomst av näringsverksamhet):

**Earned Income Tax table**  _(Skatteverket "Belopp och procent — inkomstår 2025"; SCB kommunalskatter 2025)_

| Component | Rate (Income Year 2025) |
| --- | --- |
| Municipal tax (kommunalskatt) | Average 32.41% (varies 28.98%–35.30% by municipality) |
| State income tax (statlig inkomstskatt) | 20% on taxable income above SEK 625,800 |
| Maximum marginal rate | ~52.41% (32.41% + 20%) |
| General pension contribution (allmän pensionsavgift) | 7% on earned income (capped; offset by tax credit) |

## Section 4 -- Cost Basis Methods

### 4.1 Genomsnittsmetoden (Average Cost Method) — MANDATORY

- **Mandatory method** — Skatteverket requires the average cost method for cryptocurrency. FIFO and specific identification are not permitted for crypto. How it works: 1. Add up all acquisition costs (inkl. fees) for the same cryptocurrency 2. Divide by total number of coins/units purchased 3. This gives the average omkostnadsbelopp (cost basis) per unit 4. On each disposal, the cost basis per unit × number sold = deductible amount Critical rules: - Calculated separately for each type of cryptocurrency (BTC separate from ETH separate from SOL, etc.) - All acquisitions across all exchanges and wallets are pooled together for the same cryptocurrency - Mining/staking rewards enter the pool at FMV on the date received - Exchange fees and transaction fees are included in the acquisition cost

### 4.2 Cost Basis Formula

- **Cost Basis Formula** — Total omkostnadsbelopp = Σ (acquisition cost per purchase + fees) Average cost per unit  = Total omkostnadsbelopp ÷ Total units acquired Gain/Loss per disposal = Sale proceeds − (Average cost per unit × Units sold)

### 4.3 Example: Average Cost Calculation

Purchase 1:  2.0 BTC at SEK 250,000 each = SEK 500,000 + SEK 1,000 fee
Purchase 2:  1.0 BTC at SEK 400,000      = SEK 400,000 + SEK 500 fee
Staking:     0.1 BTC received, FMV        = SEK 35,000

Total cost:  SEK 500,000 + 1,000 + 400,000 + 500 + 35,000 = SEK 936,500
Total units: 2.0 + 1.0 + 0.1 = 3.1 BTC
Average:     SEK 936,500 ÷ 3.1 = SEK 302,096.77 per BTC

Sale of 1.5 BTC at SEK 450,000 each:
  Proceeds: 1.5 × SEK 450,000 = SEK 675,000
  Cost:     1.5 × SEK 302,096.77 = SEK 453,145.16
  Gain:     SEK 221,854.84
  Tax:      SEK 221,854.84 × 30% = SEK 66,556.45

## Section 5 -- DeFi, Staking, Mining, and Airdrop Treatment

### 5.1 Mining

**Mining table**

| Scale | Classification | Tax Treatment | Citation |
| --- | --- | --- | --- |
| Private/hobby scale | Inkomst av tjänst (hobby) | Taxed at FMV when mined; municipal + state income tax rates | Skatteverket guidance on mining (kryptovalutor) |
| Commercial/business scale | Inkomst av näringsverksamhet | Business income; deduct hardware, electricity, and operating costs; social contributions apply | IL Chapter 13 |

- **Determining hobby vs business** — Determining hobby vs business: Skatteverket considers continuity, scale, profit motive, and organisation. Most individual miners are classified as hobby.
- **Cost basis of mined coins** — Cost basis of mined coins: The amount declared as income becomes the cost basis (omkostnadsbelopp) for future capital gains calculations.

### 5.2 Staking

Skatteverket treats staking rewards as ränteinkomst (interest income) within inkomst av kapital, taxed at 30% when received.

**Staking table**

| Aspect | Treatment |
| --- | --- |
| Tax point | When rewards are received/accessible |
| Valuation | FMV in SEK at receipt date |
| Tax rate | 30% (capital income) |
| Cost basis for future sale | FMV at receipt date |
| Reporting | Inkomstdeklaration 1, punkt 7.2 (Ränteinkomster) |

### 5.3 DeFi Lending

**DeFi Lending table**

| Activity | Treatment |
| --- | --- |
| Depositing crypto into lending protocol | Likely a **disposal** (avyttring) — capital gain/loss triggered |
| Interest received from lending | Interest income (ränteinkomst) at 30% |
| Withdrawing from lending protocol | New acquisition at FMV |

Warning: Skatteverket's position is that transferring crypto to a lending platform (e.g. Celsius, Aave) where the lender receives the right to use/lend the crypto constitutes a disposal. This was confirmed in guidance related to the Celsius bankruptcy (2025).

### 5.4 Liquidity Providing (LP)

**Liquidity Providing table**

| Activity | Treatment |
| --- | --- |
| Adding crypto to LP | Likely disposal of underlying assets; LP tokens acquired at FMV |
| LP token received | New asset — cost basis = FMV of assets deposited |
| Withdrawing from LP | Disposal of LP tokens; reacquired underlying assets at FMV |
| Impermanent loss | Not separately deductible — reflected in gain/loss on LP token disposal |

Flag for reviewer: LP treatment remains uncertain. Skatteverket has not issued comprehensive LP-specific guidance.

### 5.5 Airdrops

**Airdrops table**

| Type | Treatment |
| --- | --- |
| Gratuitous airdrop (no action required) | Cost basis = SEK 0; taxed as capital gain only when sold |
| Airdrop received for a service/action (e.g. testnet participation, governance vote) | Income at FMV when received; cost basis = income amount declared |

### 5.6 Hard Forks

**Hard Forks table**

| Aspect | Treatment |
| --- | --- |
| Original coin | Cost basis unchanged |
| New forked coin | Cost basis = SEK 0 |
| Sale of forked coin | Full proceeds = capital gain |

## Section 6 -- NFT Treatment

Skatteverket has published specific NFT guidance (Beskattning av NFT, Non fungible token). Two possible classifications:

### 6.1 NFT as Capital Placement (Kapitalplacering)

Applies when the NFT is purchased as a speculative investment.

**NFT Capital Placement table**

| Aspect | Treatment |
| --- | --- |
| Reporting | K4 avsnitt D (samma som kryptovalutor) |
| Gain | Taxed at 30% |
| Loss | 70% deductible |
| Cost basis | Acquisition price in SEK + fees |

### 6.2 NFT as Personal Property (Personlig tillgång)

Applies when the NFT is purchased for personal enjoyment (e.g. profile picture, digital art for personal use).

**NFT Personal Property table**  _(Skatteverket — "Beskattning av NFT, Non fungible token" (SKV guidance))_

| Aspect | Treatment |
| --- | --- |
| Reporting | Punkt 7.5 in Inkomstdeklaration, using hjälpblankett SKV 2192 |
| Gain exemption | First SEK 50,000 of aggregate personal property gains per year is tax-free |
| Loss | NOT deductible |
| Alternative cost basis | 25% of sale price (schablonavdrag) may be used |

### 6.3 NFT Creation and Sale

- **NFT creation and sale** — If the taxpayer creates and sells NFTs as a regular activity, income may be classified as inkomst av näringsverksamhet (business income) subject to full marginal rates and social contributions.

## Section 7 -- Reporting Requirements

### 7.1 Forms and Filing

**Forms and Filing table**

| Form | Purpose | Section |
| --- | --- | --- |
| Inkomstdeklaration 1 | Main personal tax return | Filed annually |
| Bilaga K4 — Avsnitt D | Cryptocurrency gains/losses (övriga tillgångar) | Aggregate gains and losses per crypto type |
| Punkt 7.2 | Interest income (staking/lending income) | In main declaration |
| Bilaga T2 | Hobby income (mining as hobby) | If mining income declared |
| Bilaga NE | Business income (commercial mining) | If mining classified as business |

### 7.2 K4 Avsnitt D Filing Details

- **K4 Avsnitt D filing details** — - Report total gain and total loss separately per cryptocurrency type - Not necessary to report each individual trade — aggregate allowed - Each cryptocurrency (e.g. Bitcoin, Ethereum) must be reported on a separate line - E-filing via Skatteverket's e-tjänst automatically calculates totals

### 7.3 Filing Deadlines

**Filing Deadlines table**

| Deadline | Description |
| --- | --- |
| 2 May 2026 | E-filing deadline for income year 2025 |
| March 2026 | Paper filing deadline (earlier than e-filing) |
| 30 June 2026 | Extended deadline if granted anstånd (extension) |

### 7.4 DAC8 / CARF Reporting (From 2026)

- **DAC8/CARF reporting** — The Swedish Riksdag adopted DAC8/CARF implementation on 26 November 2025: - Crypto service providers report user transaction data to Skatteverket - Applies to reporting periods beginning after 31 December 2025 - Does not change how crypto is taxed — only enhances information exchange - Skatteverket will cross-reference reported data with individual declarations

### 7.5 Record-Keeping

**Record-Keeping table**

| Requirement | Detail |
| --- | --- |
| Retention period | 7 years from end of relevant tax year |
| Records to maintain | Full transaction logs, cost basis calculations, exchange CSVs, wallet addresses, staking/mining logs |
| Format | CSV exports preferred; on-chain records (block explorer links) recommended |
| Burden of proof | On taxpayer — Skatteverket can request full documentation |

## Section 8 -- Loss Offset and Carry-Forward

### 8.1 Loss Offset Rules

**Loss Offset Rules table**

| Rule | Detail |
| --- | --- |
| Loss within andra tillgångar | 100% offset against gains in same category |
| Net loss from andra tillgångar | 70% deductible against other capital income (e.g. dividends, interest) |
| Net capital deficit (all capital income) | Skattereduktion: 30% of deficit up to SEK 100,000; 21% on excess |
| Carry-forward of capital losses | **NOT permitted** — losses must be used in the year they arise |

### 8.2 Stolen or Lost Crypto

**Stolen or Lost Crypto table**

| Scenario | Treatment |
| --- | --- |
| Crypto stolen (hacked exchange/wallet) | Generally **not** deductible — Skatteverket requires a genuine avyttring (disposal) |
| Exchange bankruptcy (e.g. FTX) | May qualify as avyttring if a court-approved restructuring plan converts holdings to a claim (as in FTX — Skatteverket guidance 2025) |
| Lost private keys | Not deductible — no avyttring has occurred |

## Section 9 -- Anti-Avoidance Rules

### 9.1 General Anti-Avoidance

- **General anti-avoidance rule** — Sweden has a general anti-avoidance rule (skatteflyktslagen, 1995:575) that can be invoked to disregard artificial tax-driven arrangements.  _(skatteflyktslagen, 1995:575)_

### 9.2 Wash Sales

- **Wash sales** — Sweden does not have a specific wash-sale rule for crypto. A taxpayer could theoretically sell at a loss and immediately repurchase to harvest the loss. However: - The new purchase resets the average cost basis (genomsnittsmetoden) - Skatteverket may challenge if the arrangement lacks business substance under the general anti-avoidance rule

### 9.3 Controlled Foreign Company (CFC) Rules

- **CFC rules** — If crypto is held through a foreign entity in a low-tax jurisdiction, Swedish CFC rules (IL Chapter 39a) may attribute income to the Swedish resident shareholder.  _(IL Chapter 39a)_

### 9.4 Exit Taxation

- **Exit taxation** — Sweden imposes a 10-year trailing tax on capital gains for individuals who emigrate. If an individual was resident in Sweden for at least 10 of the 15 years preceding emigration, capital gains on certain assets (including securities) may still be taxable in Sweden. Crypto's classification as "andra tillgångar" (not securities) means it may not fall within the exit tax scope — flag for specialist review.

## Section 10 -- Worked Examples

### Example 1 -- Simple Buy and Sell

Input: Swedish resident. Bought 0.5 BTC on 15 January 2025 at SEK 500,000 per BTC (total SEK 250,000). Exchange fee SEK 500. Sold 0.5 BTC on 20 October 2025 at SEK 700,000 per BTC (total SEK 350,000). Exchange fee SEK 700.

Computation:
Acquisition cost:      0.5 × SEK 500,000 + SEK 500 fee = SEK 250,500
Disposal proceeds:     0.5 × SEK 700,000 = SEK 350,000
Disposal costs:        SEK 700
Net proceeds:          SEK 350,000 - SEK 700 = SEK 349,300
Gain:                  SEK 349,300 - SEK 250,500 = SEK 98,800
Tax (30%):             SEK 98,800 × 0.30 = SEK 29,640

Reporting: K4 avsnitt D — Bitcoin — Gain SEK 98,800

### Example 2 -- Loss Scenario with 70% Deduction

Input: Swedish resident. Bought 10 ETH at average cost of SEK 30,000 each. Sold all 10 ETH at SEK 15,000 each. No other capital income in 2025.

Computation:
Acquisition cost:      10 × SEK 30,000 = SEK 300,000
Disposal proceeds:     10 × SEK 15,000 = SEK 150,000
Loss:                  SEK 150,000 - SEK 300,000 = SEK -150,000

Deductible loss (70%): SEK 150,000 × 0.70 = SEK 105,000
Capital deficit:       SEK 105,000
Skattereduktion:
  On first SEK 100,000: SEK 100,000 × 30% = SEK 30,000
  On excess SEK 5,000:  SEK 5,000 × 21%   = SEK 1,050
  Total tax credit:     SEK 31,050

Reporting: K4 avsnitt D — Ethereum — Loss SEK 150,000
The SEK 31,050 skattereduktion reduces municipal/state tax owed.

### Example 3 -- Mining Hobby Income + Subsequent Sale

Input: Swedish resident. Mined 0.2 BTC throughout 2025 (hobby scale). FMV at time of each mining reward totalled SEK 120,000. Later sold 0.2 BTC for SEK 140,000.

Computation:
Step 1 — Mining income:
  Income of hobby (inkomst av tjänst): SEK 120,000
  Taxed at marginal earned income rates (municipal + possibly state tax)
  Reporting: Bilaga T2

Step 2 — Sale of mined BTC:
  Cost basis: SEK 120,000 (= income declared)
  Proceeds: SEK 140,000
  Gain: SEK 20,000
  Tax (30%): SEK 6,000
  Reporting: K4 avsnitt D

## Self-Checks

Before finalising any Sweden crypto computation, verify:

- [ ] All amounts converted to SEK at the exchange rate on the transaction date
- [ ] Genomsnittsmetoden (average cost) used — NOT FIFO or specific identification
- [ ] Average cost calculated separately per cryptocurrency type
- [ ] All exchanges and wallets pooled together for the same cryptocurrency
- [ ] Mining/staking income declared separately from capital gains
- [ ] Staking reported as ränteinkomst (punkt 7.2) at 30%
- [ ] Mining reported as hobby income (T2) or business income (NE)
- [ ] Losses reported at 70% deduction rate in K4 avsnitt D
- [ ] Crypto-to-crypto swaps treated as disposals
- [ ] NFTs classified correctly (kapitalplacering vs personlig tillgång)
- [ ] Filing deadline: 2 May of following year for e-filing
- [ ] Record retention: 7 years

## PROHIBITIONS

- **Prohibitions list** — - NEVER use FIFO or specific identification for crypto cost basis — genomsnittsmetoden is mandatory in Sweden - NEVER treat crypto-to-crypto swaps as non-taxable events - NEVER ignore the 70% limitation on capital loss deductions - NEVER assume losses can be carried forward — they cannot - NEVER classify all mining as business income — most individuals are classified as hobby - NEVER treat transfers between own wallets as disposals - NEVER compute gains without verified cost basis and average cost calculations - NEVER ignore DeFi lending as a potential disposal event - NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an auktoriserad revisor, skattejurist, or equivalent licensed practitioner in Sweden) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
