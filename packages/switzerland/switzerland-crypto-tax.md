---
name: switzerland-crypto-tax
description: Use this skill whenever asked about Switzerland cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax Switzerland", "Bitcoin Switzerland", "cryptocurrency gains Switzerland", "crypto income Switzerland", "staking Switzerland", "mining income Switzerland", "NFT tax Switzerland", "wealth tax crypto", "Vermögenssteuer crypto", "ESTV crypto", "Kursliste crypto", "Kreisschreiben 36", "professional trader crypto Switzerland", "gewerbsmässiger Handel", "Steuererklärung crypto", "Wertschriftenverzeichnis crypto", "canton crypto tax", "Zug crypto", "Swiss crypto valuation", "CARF Switzerland", or any question about the income tax, wealth tax, capital gains, or reporting treatment of cryptocurrency, tokens, or digital assets for Swiss tax residents. Covers tax-free capital gains for private investors, annual wealth tax, ESTV crypto valuations, Kreisschreiben Nr. 36 safe-haven criteria, professional trader classification, and cantonal variations. ALWAYS read this skill before touching any Switzerland crypto work.
version: 1.0
jurisdiction: CH
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - switzerland-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland Crypto Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Switzerland (Schweizerische Eidgenossenschaft / Confédération suisse) |
| Tax | Wealth tax (Vermögenssteuer), income tax (Einkommenssteuer) — cantonal + federal |
| Currency | CHF (all values must be converted to CHF) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Bundesgesetz über die direkte Bundessteuer (DBG); cantonal tax laws (StG) |
| Key guidance | ESTV Arbeitspapier "Kryptowährungen" (last updated Dec 2021); Kreisschreiben Nr. 36 (27 July 2012) |
| Tax authority | Eidgenössische Steuerverwaltung (ESTV) / Administration fédérale des contributions (AFC) |
| Filing portal | Cantonal e-filing portals (varies by canton) |
| Filing deadline | Varies by canton (typically 31 March; extensions common) |
| Capital gains for private investors | **TAX-FREE** (if not classified as professional trader) |
| Wealth tax | **YES** — crypto declared at FMV on 31 December; rates ~0.15%–1.0% of net wealth depending on canton |
| ESTV crypto valuations | Published annually (Kursliste) — reference date 31 December |
| Professional trader risk | Kreisschreiben Nr. 36 — five cumulative safe-haven criteria |
| CARF implementation | Switzerland committed to CARF by 2027 |
| Validated by | Pending — requires sign-off by a Swiss Steuerberater or Treuhänder |
| Skill version | 1.0 |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether private investor or professional trader | Apply Kreisschreiben 36 safe-haven test; if any criterion fails, flag for review |
| Unknown cost basis | STOP — needed for professional trader gains; not critical for wealth tax but good practice |
| Unknown crypto valuation | Use ESTV Kursliste; if not listed, use documented market value from reputable exchange |
| Unknown canton of residence | STOP — wealth tax rates vary significantly by canton |
| Mining activity | Treat as self-employment income unless clearly hobby/small-scale |
| Staking rewards | Treat as taxable income at FMV when received |

## Section 2 -- Classification Rules

### 2.1 Private Investor vs Professional Trader

- **Distinction critical** — The distinction between private investor (private Vermögensverwaltung) and professional trader (gewerbsmässiger Wertschriftenhandel) is the most critical classification in Swiss crypto taxation.

**Private Investor vs Professional Trader**

| Classification | Capital Gains | Income Tax | Wealth Tax | Social Security |
| --- | --- | --- | --- | --- |
| Private investor | **TAX-FREE** | Only on income events (staking, mining, etc.) | Yes — annual wealth tax | No (on trading gains) |
| Professional trader (selbständig Erwerbstätig) | **TAXABLE** as business income | Federal + cantonal income tax (up to ~40%) | Yes | Yes (~10% AHV/IV/EO on net earnings) |

### 2.2 Kreisschreiben Nr. 36 — Safe-Haven Criteria

- **Kreisschreiben Nr. 36 five cumulative criteria** — The ESTV's Kreisschreiben Nr. 36 (27 July 2012, originally for securities, now applied to crypto) defines five cumulative criteria. If ALL five are met, the taxpayer is conclusively a private investor.  _(Kreisschreiben Nr. 36 (27 July 2012))_

**Safe-Haven Criteria**  _(Kreisschreiben Nr. 36)_

| # | Criterion | Threshold for Private Investor |
| --- | --- | --- |
| 1 | Holding period (Haltedauer) | Minimum 6 months |
| 2 | Transaction volume (Transaktionsvolumen) | Less than 5× the portfolio value at start of year |
| 3 | Capital gains as share of income (Kapitalgewinne als Einkommensanteil) | Realised capital gains < 50% of taxable income |
| 4 | Debt financing (Fremdfinanzierung) | No leverage/borrowed funds; or investment income > attributable debt interest |
| 5 | Derivatives (Derivate) | Derivatives used only to hedge existing positions |

- **Critical rules** — All five criteria must be met cumulatively — failure on even one may trigger professional classification. If safe-haven criteria are NOT met, it does not automatically mean professional trader status — a holistic assessment follows. The holistic assessment emphasises transaction volume/frequency and use of leverage (Federal Supreme Court 2C.868/2008, 23 October 2009)  _(Federal Supreme Court 2C.868/2008, 23 October 2009)_

### 2.3 Indicators of Professional Trading (Holistic Assessment)

If the safe-haven test fails, the following factors are weighted (in order of importance per Federal Supreme Court precedent):

**Indicators of Professional Trading**  _(ESTV Kreisschreiben Nr. 36; BGer 2C.868/2008; BGer 2C.766/2010; BGer 2C.385/2011)_

| Factor | Weight | Indicates Professional |
| --- | --- | --- |
| Transaction volume and short holding periods | **Primary** | High volume, day-trading, swing-trading |
| Use of substantial borrowed funds | **Primary** | Lombard loans, margin trading, leveraged positions |
| Systematic, planned approach | Secondary | Dedicated software, algorithmic trading, full-time activity |
| Specialist knowledge from professional position | Secondary | Working in finance/crypto industry |
| Income dependency | Secondary | Trading profits fund living expenses |
| Continuous, recurring losses | Contra-indicator | Suggests hobby, not professional activity |

- **Citation** — ESTV Kreisschreiben Nr. 36; BGer 2C.868/2008; BGer 2C.766/2010; BGer 2C.385/2011  _(ESTV Kreisschreiben Nr. 36; BGer 2C.868/2008; BGer 2C.766/2010; BGer 2C.385/2011)_

### 2.4 Consequences of Professional Trader Classification

**Consequences of Professional Trader Classification**

| Aspect | Treatment |
| --- | --- |
| All capital gains | Taxable as self-employment income |
| All capital losses | Deductible against other income |
| Transaction costs | Fully deductible as business expenses |
| AHV/IV/EO social contributions | ~10% of net self-employment income |
| Income tax rate | Combined federal + cantonal: up to ~40% (varies by canton and income level) |
| Accounting obligations | Proper bookkeeping required |

## Section 3 -- Rate Tables

### 3.1 Wealth Tax (Vermögenssteuer)

- **Wealth tax levied by cantons only** — Wealth tax is levied by cantons and municipalities only — there is no federal wealth tax on private individuals.

**Wealth Tax by Canton**

| Canton | Approximate Effective Rate (on net taxable wealth) | Notes |
| --- | --- | --- |
| Zug | 0.15%–0.30% | One of the lowest; crypto-friendly reputation |
| Nidwalden | 0.15%–0.25% | Very low |
| Schwyz | 0.20%–0.35% | Low |
| Zurich | 0.30%–0.60% | Moderate |
| Bern | 0.35%–0.65% | Moderate |
| Basel-Stadt | 0.40%–0.75% | Higher |
| Geneva | 0.50%–1.00% | Among the highest |
| Vaud | 0.50%–0.80% | Higher |

Rates are progressive — higher net wealth = higher marginal rate. Most cantons grant exemptions of CHF 50,000–100,000 for single taxpayers and CHF 100,000–200,000 for married couples. Smaller crypto portfolios often remain below the exemption threshold and pay no wealth tax. Wealth tax applies to the total net wealth (all assets minus liabilities), not just crypto

### 3.2 Income Tax Rates (If Professional Trader)

**Income Tax Rates**

| Level | Maximum Marginal Rate |
| --- | --- |
| Federal (direkte Bundessteuer) | 11.5% |
| Cantonal + municipal | ~15%–35% (varies widely) |
| Combined maximum | ~35%–42% (depending on canton) |

### 3.3 Social Security (If Professional Trader)

**Social Security**

| Contribution | Rate |
| --- | --- |
| AHV/IV/EO (self-employed) | ~10% of net self-employment income (maximum; declining scale) |
| Additional social security | Varies by canton |

### 3.4 ESTV Crypto Valuations — Kursliste 2025 (Selected)

The ESTV publishes official CHF valuations for the most common cryptocurrencies as of 31 December each year.

**ESTV Crypto Valuations**  _(ESTV Kursliste 2025; ictax.admin.ch)_

| Cryptocurrency | ESTV Value 31.12.2025 (CHF) |
| --- | --- |
| Bitcoin (BTC) | 69,571.99 |
| Ethereum (ETH) | 2,364.08 |
| Others | Published on ESTV Kursliste (ictax.admin.ch) |

- **If a token is not on the Kursliste** — Use the documented market value from a reputable exchange (e.g. Coinbase, Kraken, Binance) as of 31 December 2025. Retain evidence.  _(ESTV Kursliste 2025; ictax.admin.ch)_

## Section 4 -- Cost Basis Methods

### 4.1 Private Investors — Limited Relevance

For private investors, cost basis tracking is not strictly required for tax purposes since capital gains are tax-free. However, it is strongly recommended to:
- Prove private investor status if challenged
- Document acquisition costs for tokens that generate income (staking/mining)
- Prepare for potential future tax law changes

### 4.2 Professional Traders — Full Tracking Required

**Cost Basis Methods**

| Method | Status |
| --- | --- |
| FIFO (First In, First Out) | Accepted; commonly used |
| Average cost | Accepted |
| Specific identification | Accepted if documented |
| LIFO | Not standard practice |

### 4.3 Cost Basis Components

- **Cost basis components** — For professional traders, the acquisition cost includes: - Purchase price in CHF at date of acquisition - Exchange fees and commissions - Network/gas fees - Any costs directly attributable to the acquisition

## Section 5 -- DeFi, Staking, Mining, and Airdrop Treatment

### 5.1 Mining

**Mining**  _(StP 20 Nr. 2 (Canton TG); ESTV Arbeitspapier Kryptowährungen)_

| Scale | Classification | Tax Treatment |
| --- | --- | --- |
| Small-scale / hobby | May be treated as occasional income | Taxable as "übrige Einkünfte" (other income); amount = FMV at receipt |
| Commercial / regular | Self-employment (selbständige Erwerbstätigkeit) | Full income tax + social security; deduct equipment, electricity, and operating costs |

- **Note - Thurgau mining** — The Canton of Thurgau's Steuerpraxis explicitly states: "Mining of Bitcoin through provision of computing power and receipt of income in Bitcoin constitutes taxable income from self-employment in all cases." Other cantons are generally aligned.  _(StP 20 Nr. 2 (Canton TG); ESTV Arbeitspapier Kryptowährungen)_

### 5.2 Staking

**Staking**

| Aspect | Treatment |
| --- | --- |
| Classification | Income (Einkommen) at FMV when rewards are received |
| Tax rate | Ordinary income tax rates (federal + cantonal) |
| Tax point | When rewards are accessible to the taxpayer |
| Wealth tax | Staked tokens remain in the wealth tax base (declared at 31 Dec FMV) |
| Cost basis for future sale | FMV at receipt date (relevant only for professional traders) |

### 5.3 DeFi Lending

**DeFi Lending**

| Activity | Treatment |
| --- | --- |
| Interest/yield received | Taxable as income at FMV when received |
| Principal returned | Not an income event (return of capital) |
| Principal lost (protocol failure) | Potential deductible loss for professional traders; limited relief for private investors |

ESTV has not published comprehensive DeFi lending guidance. Conservative approach: treat all yield as taxable income.

### 5.4 Liquidity Providing

**Liquidity Providing**

| Activity | Treatment |
| --- | --- |
| Adding to LP | Uncertain — may or may not be a disposal for professional traders |
| Fees/rewards earned | Taxable as income at FMV |
| Impermanent loss | Not addressed by ESTV |

LP positions in DeFi are an evolving area.

### 5.5 Airdrops

**Airdrops**

| Type | Treatment |
| --- | --- |
| Gratuitous airdrop (no action required) | Add to wealth tax portfolio at FMV; acquisition cost = CHF 0 |
| Airdrop for services | Taxable as income at FMV when received |

### 5.6 Hard Forks

**Hard Forks**

| Aspect | Treatment |
| --- | --- |
| Original coin | Cost basis unchanged; continue to declare for wealth tax |
| New forked coin | Acquisition cost = CHF 0; add to wealth tax portfolio at FMV on 31 Dec |
| Private investor sale | Tax-free capital gain |
| Professional trader sale | Fully taxable |

### 5.7 ICO/Token Participation

**ICO/Token Participation**  _(ESTV Arbeitspapier "Kryptowährungen und Initial Coin/Token Offerings (ICOs/ITOs)")_

| Aspect | Treatment |
| --- | --- |
| Investment in ICO/ITO | Acquisition cost = amount invested in CHF |
| Token received | Declare for wealth tax at FMV (or cost if no market price available) |
| Subsequent sale (private) | Tax-free capital gain |
| Subsequent sale (professional) | Taxable income |

## Section 6 -- NFT Treatment

### 6.1 General Classification

NFTs are treated similarly to other crypto-assets under Swiss tax law:

**NFT General Classification**

| Aspect | Private Investor | Professional Trader |
| --- | --- | --- |
| Purchase | Acquisition cost recorded | Business expense |
| Holding | Wealth tax at 31 Dec FMV (may be difficult to value) | Wealth tax + balance sheet item |
| Sale gain | Tax-free | Taxable as business income |
| Sale loss | Not deductible | Deductible business loss |
| Creation and sale | If occasional, tax-free; if regular, self-employment income | Business income |

### 6.2 Valuation Challenges

- **NFT valuation challenges** — NFTs are generally NOT on the ESTV Kursliste. Valuation for wealth tax: - Use last sale price on a recognised marketplace (OpenSea, etc.) - If no recent sale, use acquisition cost or a reasonable estimate - If the NFT has no market value, declare at CHF 0 with a note

### 6.3 NFT Royalties

- **NFT royalties** — Secondary sale royalties received by NFT creators are treated as income (self-employment if regular, other income if occasional).

## Section 7 -- Reporting Requirements

### 7.1 Tax Return Filing

**Tax Return Filing**

| Element | Where to Report |
| --- | --- |
| Crypto holdings (wealth tax) | Wertschriftenverzeichnis (securities schedule) / État des titres — list each crypto with quantity and CHF value at 31 Dec |
| Staking/mining income | Einkommen / Revenu — declare as other income |
| Professional trading income | Einkommen aus selbständiger Erwerbstätigkeit — with profit & loss statement |
| Capital gains (private) | No reporting required (tax-free) |

### 7.2 Wertschriftenverzeichnis — How to Declare Crypto

For each cryptocurrency held on 31 December:

**Wertschriftenverzeichnis Fields**

| Field | What to Enter |
| --- | --- |
| Description | Name of cryptocurrency (e.g. "Bitcoin (BTC)") |
| Quantity | Number of units held |
| Valuation | ESTV Kursliste value per unit in CHF; or documented market value |
| Total value | Quantity × per-unit value |
| Location/custodian | Exchange name or "private wallet" |

### 7.3 Filing Deadlines (Vary by Canton)

**Filing Deadlines**

| Canton | Standard Deadline | Extension Available |
| --- | --- | --- |
| Zurich | 31 March | Yes (up to 30 September) |
| Bern | 15 March | Yes |
| Zug | 30 April | Yes |
| Geneva | 31 March | Yes |
| Others | Typically 31 March | Varies |

### 7.4 ESTV Kursliste Access

- Available at: [ictax.admin.ch](https://ictax.admin.ch)
- Published annually after year-end
- Covers major cryptocurrencies (BTC, ETH, and many others)
- Updated annually; check for the relevant tax year

### 7.5 Record-Keeping

**Record-Keeping**

| Requirement | Detail |
| --- | --- |
| Retention period | 10 years (Obligationenrecht Art. 958f) for professional traders; recommended 10 years for private investors |
| Records to maintain | Transaction logs, wallet addresses, exchange statements, ESTV Kursliste screenshots, staking/mining logs |
| Format | Electronic acceptable; exchanges' CSV exports plus on-chain evidence |

### 7.6 CARF (Crypto-Asset Reporting Framework)

- **CARF implementation** — Switzerland has committed to implementing CARF by 2027. This will require Swiss crypto service providers to report user transaction data to the ESTV for automatic exchange with other jurisdictions.

## Section 8 -- Loss Offset and Carry-Forward

### 8.1 Private Investors

**Private Investors Losses**

| Scenario | Treatment |
| --- | --- |
| Capital loss on crypto sale | **NOT deductible** — capital gains are tax-free, so capital losses are tax-irrelevant |
| Wealth tax on depreciating assets | Wealth tax still applies on 31 Dec FMV (but lower value = lower wealth tax) |

### 8.2 Professional Traders

**Professional Traders Losses**  _(DBG Art. 211)_

| Scenario | Treatment |
| --- | --- |
| Trading losses | Deductible against all other income (employment, self-employment, etc.) |
| Net operating loss | Can be carried forward for 7 years (DBG Art. 211; cantonal laws vary) |
| Transaction costs | Fully deductible |
| Social security impact | Losses reduce the base for AHV/IV/EO contributions |

### 8.3 Stolen/Lost Crypto

**Stolen/Lost Crypto**

| Scenario | Private Investor | Professional Trader |
| --- | --- | --- |
| Hacked exchange | Remove from wealth tax (no longer held on 31 Dec) | Deductible loss |
| Lost private keys | May argue removal from wealth tax if permanently inaccessible | Deductible if documented |
| Exchange bankruptcy | Remove from wealth tax once definitively lost | Deductible loss |

## Section 9 -- Anti-Avoidance Rules

### 9.1 Professional Trader Reclassification

- **Reclassification risk** — The primary anti-avoidance mechanism is the ESTV's power to reclassify a private investor as a professional trader, thereby subjecting all gains to income tax. This is the most significant risk for active Swiss crypto investors.

### 9.2 Economic Substance

- **Substance over form** — Swiss tax authorities apply substance-over-form principles. Structures lacking economic substance (e.g. crypto held through shell companies in low-tax cantons purely for wealth tax reduction) may be challenged.

### 9.3 Cantonal Tax Competition

- **Cantonal competition** — While cantonal tax competition is legal and encouraged in Switzerland, moving cantonal domicile purely for wealth tax reduction is legitimate. However, the move must be genuine — a sham relocation may be challenged.

### 9.4 Intercantonal Double Taxation

- **Intercantonal allocation** — If a taxpayer has tax obligations in multiple cantons (e.g. property in one, domicile in another), allocation rules apply. Crypto is generally allocated to the canton of domicile.

### 9.5 International Exchange of Information

- **International exchange participation** — Switzerland participates in: - AEOI (Automatic Exchange of Information) — operational since 2018 - CARF (Crypto-Asset Reporting Framework) — by 2027 - Bilateral tax treaties with 100+ countries

## Section 10 -- Worked Examples

### Example 1 -- Private Investor, Tax-Free Gains + Wealth Tax

**Input:** Swiss resident in Canton of Zurich. Holds 5 BTC purchased in 2022 at CHF 25,000 each. Sold 2 BTC in June 2025 at CHF 65,000 each. Still holds 3 BTC on 31 December 2025. No leverage, no derivatives, holds > 6 months, no other trading. Total other taxable income: CHF 120,000.

**Safe-haven test (Kreisschreiben Nr. 36):**
```
1. Holding period ≥ 6 months:          YES (held since 2022)
2. Transaction volume < 5× start value: YES (2 sales vs portfolio of 5 BTC)
3. Capital gains < 50% of income:       CHF 80,000 gain vs CHF 120,000 income
                                         → 80,000 / (120,000 + 80,000) = 40% → YES
4. No leverage/borrowed funds:           YES
5. Derivatives for hedging only:         No derivatives used → YES

All 5 criteria met → PRIVATE INVESTOR
```

**Tax computation:**
```
Capital gains: 2 × (CHF 65,000 - CHF 25,000) = CHF 80,000
Capital gains tax: CHF 0 (tax-free for private investors)

Wealth tax:
  3 BTC held on 31.12.2025
  ESTV Kursliste value: CHF 69,571.99 per BTC
  Crypto wealth: 3 × CHF 69,571.99 = CHF 208,715.97
  (Added to other wealth for total net wealth calculation)
  Zurich wealth tax on CHF 208,716 portion: ~CHF 600–1,200 (depends on total net wealth and municipality)
```

### Example 2 -- Professional Trader Classification

**Input:** Swiss resident in Canton of Zug. Made 500+ trades in 2025. Average holding period 2 weeks. Uses margin trading. Crypto gains = CHF 200,000. Other income: CHF 50,000 (part-time employment).

**Safe-haven test:**
```
1. Holding period ≥ 6 months:          NO (average 2 weeks)
2. Transaction volume < 5× start:      Likely NO (500+ trades)
3. Capital gains < 50% of income:       200,000 / 250,000 = 80% → NO
4. No leverage:                         NO (margin trading)
5. Derivatives for hedging only:         N/A

Multiple criteria FAILED → Safe haven NOT available
```

**Holistic assessment strongly indicates professional trader:**
```
- High volume (500+ trades): YES
- Short holding periods: YES
- Substantial leverage: YES
→ Classification: Professional trader (gewerbsmässiger Händler)

Tax computation:
  Taxable self-employment income: CHF 200,000
  Federal income tax: ~CHF 20,000 (11.5% marginal)
  Cantonal/municipal tax (Zug): ~CHF 16,000 (low-tax canton)
  AHV/IV/EO: ~CHF 20,000 (10%)
  Total tax burden: ~CHF 56,000 (~28%)

  Note: Can deduct all trading fees, exchange costs, and losses.
  Wealth tax also applies on remaining holdings at 31 Dec.
```

### Example 3 -- Staking Income + Wealth Tax Only

**Input:** Swiss resident in Canton of Geneva. Holds 100 ETH, staked via Lido. Received 5 ETH in staking rewards during 2025 (FMV at receipt dates totalling CHF 12,500). No sales. Private investor (safe-haven met).

**Tax computation:**
```
Capital gains: None (no sales)
Capital gains tax: CHF 0

Staking income:
  5 ETH received, total FMV: CHF 12,500
  Taxable as ordinary income
  Combined federal + cantonal tax (Geneva, ~35%): ~CHF 4,375

Wealth tax:
  105 ETH held on 31.12.2025
  ESTV value: CHF 2,364.08 per ETH
  Crypto wealth: 105 × CHF 2,364.08 = CHF 248,228.40
  Geneva wealth tax (higher bracket canton): ~CHF 1,500–2,500

Total tax: ~CHF 5,875–6,875
```

## Self-Checks

Before finalising any Switzerland crypto computation, verify:

- [ ] Kreisschreiben Nr. 36 safe-haven analysis completed (all 5 criteria)
- [ ] If safe-haven fails, holistic assessment documented
- [ ] ESTV Kursliste values used for 31 Dec wealth tax (check ictax.admin.ch)
- [ ] Tokens not on Kursliste valued from documented exchange rates
- [ ] Canton of residence identified (critical for wealth tax rates)
- [ ] Mining/staking income declared as ordinary income at FMV
- [ ] Wealth tax calculated on total crypto holdings at 31 Dec
- [ ] All values in CHF at applicable exchange rates
- [ ] Wertschriftenverzeichnis (securities schedule) completed with all crypto positions
- [ ] Professional trader consequences assessed (income tax + social security)
- [ ] Record retention of 10 years for professional; recommended same for private
- [ ] CARF reporting awareness (2027 implementation)

## PROHIBITIONS

- NEVER assume all Swiss crypto is completely tax-free — wealth tax applies and income events (staking, mining) are taxable
- NEVER ignore the Kreisschreiben Nr. 36 safe-haven test — failure triggers professional trader risk
- NEVER use outdated ESTV Kursliste values — verify for the correct tax year
- NEVER ignore cantonal differences — wealth tax rates vary by 5–7× between cantons
- NEVER classify staking/mining income as tax-free capital gains — these are income events
- NEVER forget AHV/IV/EO social security contributions for professional traders (~10%)
- NEVER assume professional trader status is always disadvantageous — losses and costs become deductible
- NEVER omit crypto from the Wertschriftenverzeichnis — all holdings must be declared for wealth tax
- NEVER treat wallet-to-wallet transfers as disposals
- NEVER compute professional trader gains without tracking cost basis
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a dipl. Steuerexperte, Treuhänder, or equivalent licensed practitioner in Switzerland) before filing or acting upon.

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
