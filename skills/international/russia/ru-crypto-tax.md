---
name: ru-crypto-tax
description: Use this skill whenever asked about the taxation of cryptocurrency or digital currency (цифровая валюта) for individuals in Russia. Trigger on phrases like "crypto tax Russia", "цифровая валюта налог", "Bitcoin tax Russia", "mining tax Russia", "майнинг налог", "налог на криптовалюту", "crypto НДФЛ", "is crypto legal in Russia", "реестр майнеров", "продажа криптовалюты налог", "crypto property Russia", or any request to compute, classify, or advise on Russian tax on disposal of digital currency, mining income, or holding crypto. Covers Federal Law No. 418-ФЗ (29 Nov 2024) which treats digital currency as PROPERTY (имущество), the two distinct НДФЛ tax bases (disposal gains capped at 15 %, mining income on the general 13–22 % scale), cost-basis deduction, the mining registry (реестр майнеров) and reporting, the ban on domestic crypto payments, the experimental legal regime (ЭПР) for foreign-trade settlements, the 3-НДФЛ declaration, and the absence of VAT (НДС) on digital currency. For ordinary income tax see ru-income-tax; for self-employed see ru-self-employed-npd.
version: 1.0
jurisdiction: RU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RU Crypto Tax

## Russia — Taxation of Cryptocurrency / Digital Currency (цифровая валюта) for Individuals

This skill computes and explains how Russia taxes **digital currency** — **цифровая валюта** (*tsifrovaya valyuta*) — for individuals: gains on **disposal** (продажа / обмен), income from **mining** (майнинг), and the legal status of holding and using crypto. Russia does **not** use a "crypto" tax category as such; since 1 January 2025 digital currency is **property** (*имущество*) under the Tax Code, and ordinary НДФЛ rules apply with a few crypto-specific tax-base rules.

Reply to the user in their own language; keep the native Russian terms in parentheses on first use.

> **AI language rule:** Detect the user's language and answer in it. Keep Russian terms verbatim (цифровая валюта, НДФЛ, ФНС, майнинг, реестр майнеров, 3-НДФЛ, ЭПР) — the user and their accountant will recognise them.

## 1. Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Russia (RU) |
| Tax | **НДФЛ** (personal income tax) on gains — digital currency taxed as **property (имущество)** |
| Disposal gains scale | Special **two-rate** scale: **13 %** up to 2.4M ₽, **15 %** above (capped at 15 %) |
| Mining income scale | **General progressive scale 13 / 15 / 18 / 20 / 22 %**, taxed at fair value **at receipt** |
| Currency | Russian rouble (₽ / RUB) — all amounts converted at **Банк России** rate on the transaction date |
| Legislation | **Федеральный закон № 418-ФЗ от 29.11.2024** (digital-currency tax), amending **НК РФ** глава 23; **№ 259-ФЗ** (digital financial assets / digital currency framework) |
| Authority | **ФНС** — Федеральная налоговая служба (Federal Tax Service), nalog.gov.ru |
| Filing | Annual **3-НДФЛ** declaration, due **30 April** of the following year; tax paid by **15 July** |
| VAT (НДС) | **None** — operations with digital currency and mining are **exempt from НДС** |
| Non-resident rate | **30 %** on Russian-source crypto income, no cost-basis structure parity (verify) |
| Quality tier | **Research-verified — pending sign-off by a qualified Russian accountant** |
| Skill version | 1.0 |

### Conservative defaults

When facts are missing, default to the position that produces the **higher** tax / the safer compliance posture, and state the assumption explicitly:

- **Assume tax residency** (≥ 183 days in Russia in the rolling 12 months) unless the user says otherwise — non-residents are taxed at 30 % with no resident-style relief, so confirm before relying on it.
- **Assume a taxable disposal occurred** on any sale, crypto-to-crypto swap, or use of crypto to settle an obligation. A swap of one token for another **is** a disposal of the first token.
- **Assume mining is taxable at receipt** at market value, even if the coins are never sold.
- **Assume zero cost basis** if the user cannot document acquisition cost — undocumented basis is generally **not** deductible. Push the user to produce exchange statements / bank records.
- **Assume the domestic payment ban applies** — never advise using crypto to pay for goods/services inside Russia.
- Treat the **foreign-trade settlement regime (ЭПР)** and the 2026 exchange/broker framework as **evolving** — verify current in-force status before advising.

## 2. Legal status (settled vs evolving)

- **Digital currency is property — SETTLED** — Federal Law № 418-ФЗ of 29 November 2024 amended the Tax Code so that, from 1 January 2025, цифровая валюта is recognised as property (имущество) for tax purposes. Consequently disposals and mining are taxable events under НДФЛ. The underlying civil/financial framework comes from Federal Law № 259-ФЗ "О цифровых финансовых активах, цифровой валюте..." (digital financial assets / digital currency).  _(Федеральный закон № 418-ФЗ от 29.11.2024; Федеральный закон № 259-ФЗ)_
- **Holding and investing — LEGAL** — Individuals may own, hold, buy and sell digital currency. Crypto is treated as an investment asset, not as money.
- **Domestic payment ban — SETTLED** — Digital currency may not be used as a means of payment for goods, works or services inside Russia (it is not legal tender; only the rouble is). Advising or facilitating domestic crypto payments is outside this skill's scope and exposes the user to penalties.
- **Mining registry (реестр майнеров) — SETTLED for professionals; threshold for individuals — VERIFY** — Legal entities (юрлица) and individual entrepreneurs (ИП) that mine on an industrial scale must register in the реестр майнеров maintained by ФНС. Ordinary individuals may mine without registration only if electricity consumption stays within the personal limit commonly cited as 6 000 kWh/month — verify the current in-force limit, as it is set by Government decree and may change. Self-employed on НПД (самозанятые) are prohibited from mining and from putting mining income into the НПД base; mining income goes onto the general НДФЛ scale instead.
- **Foreign-trade settlement regime (ЭПР) — EVOLVING** — Under an experimental legal regime (экспериментальный правовой режим / ЭПР) supervised by the Банк России, crypto may be used in cross-border settlements under foreign-trade contracts. This is a controlled pilot for businesses, not a general permission for individuals, and the Банк России's 2025–2026 concept for regulated exchanges, brokers and "especially qualified" investors is still being built out. Verify current in-force status before advising on any cross-border or exchange-based activity.

### What is a taxable event

**What is a taxable event**

| Event | Taxable? | Notes |
| --- | --- | --- |
| Buying crypto with roubles | No | Acquisition only; records the **cost basis** |
| Holding crypto (unrealised gain) | No | No mark-to-market for individuals |
| **Selling crypto for fiat** (₽, $) | **Yes** | Disposal; gain = proceeds − cost basis |
| **Crypto-to-crypto swap** | **Yes** | Disposal of the token given up, valued in ₽ at the swap date |
| Using crypto to settle an obligation | **Yes** (and banned domestically) | Disposal at market value |
| **Receiving mined coins** | **Yes** | See §4 — taxed at receipt at market value |
| Receiving crypto as a gift | Maybe | General НДФЛ gift rules; verify per facts |
| Transferring between own wallets | No | No change of beneficial owner |

### Gain on disposal

- **Gain formula** — Gain = Proceeds (₽, at Банк России rate on disposal date) − Documented acquisition cost (cost basis, ₽) − Documented related expenses (e.g. exchange fees), where supported
- **Cost basis documentation** — Cost basis (стоимость приобретения) is deductible only when documented (exchange statements, bank transfers, contracts). Undocumented basis ⇒ treat as zero (conservative default).
- **Mined coins later sold — cost basis** — For mined coins later sold, the cost basis is the market value already taxed at receipt (§4), so the same gain is not taxed twice.

Losses and netting across disposals follow the ordinary НДФЛ tax-base rules for property/financial assets — verify the exact netting and loss-carry treatment with a Russian accountant, as the crypto-specific tax-base rules are new.

### Rate on disposal gains — the SPECIAL two-rate scale (capped at 15 %)

**Rate on disposal gains**

| Band | Annual disposal gain (₽) | Rate |
| --- | --- | --- |
| 1 | up to **2 400 000** | **13 %** |
| 2 | over **2 400 000** | **15 %** (on the excess) |

So НДФЛ on disposal gains is capped at 15 % — it does not reach 18/20/22 %. This is the most commonly mis-stated point: the headline "up to 22 %" Russian НДФЛ scale does not apply to crypto disposal gains.

> **Verify** the exact band and threshold (2.4M ₽) and the cap against ФНС (nalog.gov.ru) and НК РФ глава 23 at filing time.

## 4. Mining taxation (майнинг)

- **Two stages of mining tax** — Mining is taxed in two stages: Stage 1 — receipt (доход в натуральной форме). When mined coins are received, the market value in roubles at the date of receipt is income and is taxable immediately, whether or not the coins are sold. Value at Банк России-referenced market rates on the receipt date. Stage 2 — later disposal. When the mined coins are sold/swapped, the gain is proceeds − the value already taxed at receipt (that value becomes the cost basis), taxed under the §3 disposal rules.

### Rate on mining income — the GENERAL progressive scale (13–22 %)

**Rate on mining income**

| Band | Annual income (₽) | Rate |
| --- | --- | --- |
| 1 | up to 2 400 000 | 13 % |
| 2 | 2 400 000 – 5 000 000 | 15 % |
| 3 | 5 000 000 – 20 000 000 | 18 % |
| 4 | 20 000 000 – 50 000 000 | 20 % |
| 5 | over 50 000 000 | 22 % |

Unlike disposal gains, mining income uses the full general НДФЛ progressive scale. Applied band-by-band on the excess, not to the whole amount.

### Mining compliance

- **Registration requirement** — Register in the реестр майнеров (ФНС) if mining as a legal entity / ИП, or as an individual above the personal electricity limit (commonly cited 6 000 kWh/month — verify current limit).
- **Deductible expenses** — Documented expenses (electricity, equipment depreciation, pool fees) may reduce the mining tax base — verify the deductible categories for individuals vs ИП.
- **Самозанятые prohibition** — Самозанятые (НПД) cannot mine within the НПД regime.
- **Informational reporting** — Miners are required to report mined-coin data to ФНС (volume received, wallet/pool identifiers). One widely cited rule is reporting by the 20th of the month following receipt — verify this monthly informational filing separately from the annual 3-НДФЛ declaration, as the two are distinct obligations.

## 5. Worked examples

Illustrative only; rates/thresholds must be re-verified at filing time. All values in roubles (₽).

### Example 1 — simple disposal below the 2.4M threshold

Bought 0.5 BTC for 1 000 000 ₽ (documented), sold for 1 800 000 ₽.

- Gain = 1 800 000 − 1 000 000 = 800 000 ₽
- 800 000 < 2.4M ⇒ entire gain at 13 %
- НДФЛ = 800 000 × 13 % = 104 000 ₽

### Example 2 — disposal crossing the 2.4M threshold (two-rate cap)

Gain on the year's disposals = 3 000 000 ₽.

- First 2 400 000 × 13 % = 312 000 ₽
- Remaining 600 000 × 15 % = 90 000 ₽
- НДФЛ = 402 000 ₽ (note: 15 % is the cap — never 18 %+ on disposal gains)

### Example 3 — undocumented cost basis

Sold crypto for 900 000 ₽ but cannot document acquisition cost.

- Cost basis = 0 (conservative default)
- Gain = 900 000 ₽, all at 13 % ⇒ НДФЛ = 117 000 ₽
- Lesson: locate exchange/bank records to substantiate basis before filing.

### Example 4 — mining received, then sold (no double tax)

Mined coins received with market value 500 000 ₽; later sold for 700 000 ₽.

- At receipt: income 500 000 ₽ on the general scale (within band 1) ⇒ 500 000 × 13 % = 65 000 ₽
- At sale: gain = 700 000 − 500 000 (basis = value already taxed) = 200 000 ₽ at 13 % = 26 000 ₽
- Total НДФЛ = 91 000 ₽; the 500 000 ₽ is not taxed twice.

### Example 5 — mining income high enough to reach an upper band

Annual mining income (value at receipt) = 6 000 000 ₽, no other income.

- 2 400 000 × 13 % = 312 000
- (5 000 000 − 2 400 000) = 2 600 000 × 15 % = 390 000
- (6 000 000 − 5 000 000) = 1 000 000 × 18 % = 180 000
- НДФЛ = 882 000 ₽ — mining can reach 18 % (and beyond), unlike disposal gains.

## 6. Tier 2 — reviewer judgement, references, test suite

### Reviewer judgement (escalate to a qualified Russian accountant)

- Two-base interaction. Whether mining-then-sale, multiple disposals, losses, and other НДФЛ income net correctly across the disposal base vs the general base — the crypto-specific tax-base rules are new (effective 2025) and practice is still settling. Verify.
- Mining deductible expenses for individuals vs ИП; whether equipment is depreciable.
- Residency edge cases (relocation mid-year, 30 % non-resident exposure).
- ЭПР / cross-border activity and any 2026 regulated-exchange framework — confirm in-force status.
- Self-employment overlap — НПД prohibits mining; ИП on ОСНО/УСН have different rules (УСН generally not available for mining). Route to ru-self-employed-npd / ru-usn / ru-income-tax as needed.
- Penalties / criminal thresholds for non-reporting — confirm current figures before advising.

### References (verify current in-force status; YMYL)

- Федеральный закон № 418-ФЗ от 29.11.2024 — digital-currency taxation (crypto = property; amends НК РФ гл. 23)
- Федеральный закон № 259-ФЗ — digital financial assets and digital currency framework
- Налоговый кодекс РФ, глава 23 (НДФЛ) — rates, tax base, 3-НДФЛ
- ФНС — nalog.gov.ru; mining portal nalog.gov.ru/mining/
- Банк России — cbr.ru, experimental legal regime (ЭПР) for foreign-trade settlements
- Secondary: PwC Tax Summaries (Russia), Kontur, reputable Russian tax-law firms

### Test suite (expected behaviour)

1. "What's the crypto tax rate in Russia?" → НДФЛ; disposal gains 13 %/15 % capped at 15 %; mining on 13–22 %; clarify which.
2. "Is Bitcoin taxed at 22 % in Russia?" → Only mining income can reach 22 %; disposal gains cap at 15 %.
3. "Do I pay tax if I just hold crypto?" → No tax on holding; tax on disposal/mining.
4. "Is a crypto-to-crypto swap taxable?" → Yes — disposal of the token given up, valued in ₽.
5. "Can I pay for coffee with Bitcoin in Russia?" → No — domestic payment ban; not legal tender.
6. "Is there VAT on crypto?" → No НДС on digital currency / mining.
7. "I mined coins but didn't sell — do I owe tax?" → Yes, at market value at receipt.
8. "How do I declare?" → Annual 3-НДФЛ by 30 April, pay by 15 July.
9. "Can a самозанятый mine?" → No — mining excluded from НПД.
10. "Can I use crypto to pay an overseas supplier?" → Only via the ЭПР (business pilot); verify status.

## PROHIBITIONS

- Do NOT advise using digital currency to pay for goods, works or services inside Russia — it is banned; crypto is not legal tender.
- Do NOT state that crypto disposal gains are taxed up to 18/20/22 % — the disposal base is capped at 15 %. Only mining income reaches the upper bands.
- Do NOT treat holding or unrealised gains as taxable.
- Do NOT allow undocumented cost basis to be deducted — default to zero basis.
- Do NOT advise самозанятые (НПД) that they may mine within their regime.
- Do NOT treat the ЭПР cross-border regime or the 2026 exchange/broker framework as settled — flag as evolving and tell the user to verify current in-force status.
- Do NOT apply VAT (НДС) to digital-currency operations or mining.
- Do NOT advise on sanctions-evasion or circumvention of currency controls.
- Do NOT give a final filing position without sign-off by a qualified Russian accountant.

## Disclaimer

This skill is research-verified against ФНС (nalog.gov.ru), the Банк России, PwC and reputable Russian crypto-tax / legal sources, but has not been signed off by a credentialed Russian accountant. Russian digital-currency rules are new (effective 1 January 2025) and parts — especially the experimental legal regime (ЭПР) for cross-border settlements, the 2026 regulated-exchange framework, and some mining thresholds — are still evolving. Figures, rates and in-force status must be re-verified at the time of filing. This is general information, not tax advice. Every output must be reviewed and signed off by a qualified Russian accountant before it reaches the taxpayer or the ФНС.

Part of openaccountants.com — open-source tax skills for the self-employed.

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
