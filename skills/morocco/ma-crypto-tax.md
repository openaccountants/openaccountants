---
name: ma-crypto-tax
description: Use this skill whenever asked about the taxation and legal status of cryptocurrency or crypto-assets in Morocco for a resident individual or self-employed person, tax year 2026. Trigger on phrases like "Morocco crypto tax", "Bitcoin Maroc impot", "cryptomonnaie Maroc legal", "crypto-actifs Maroc", "is crypto legal in Morocco", "Office des Changes crypto", "loi 42.25 crypto", "stablecoin dirham", "الضريبة على العملات المشفرة المغرب". Covers the restricted and unregulated status under the November 2017 Office des Changes, Bank Al-Maghrib and AMMC notice, the draft Law 42.25 (status to verify), the absence of any crypto article in the 2026 Code General des Impots, the two IR categories a gain might fall into by analogy (profits de capitaux mobiliers or revenus professionnels) with the rates each would borrow, and the exchange-control risk. High-uncertainty territory, never asserts a settled regime. Reply in the user's language (English, French or Darija) and keep the native French terms.
version: 2.0
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-14
type: situation-rules
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
---

# Morocco: crypto-assets, legal status and tax, tax year 2026

## Scope

This skill covers how cryptocurrency (cryptomonnaie, crypto-actifs, actifs numeriques) is treated in Morocco for a resident individual, including a self-employed person: its legal status, the unsettled income tax (IR) position of a realised gain, and the exchange-control risk. It covers tax year 2026 (gains realised from 1 January to 31 December 2026).

**Read this warning first.** Morocco has no settled crypto tax regime and crypto is not freely legal. The 2026 Code General des Impots (CGI), which includes Finance Law 50-25 for 2026, has no article that names crypto-assets (searched in full on 14 Nov 2026). The legal position rests on a November 2017 notice that is still treated as in force and on a draft law (projet de loi n° 42.25) whose adoption is not confirmed. Anything here about how a gain "might" be taxed is analogy, not established law. The right posture is honesty about the uncertainty and referral to a Moroccan expert-comptable and, on exchange-control questions, to the Office des Changes.

The authorities: Bank Al-Maghrib (BAM), the central bank; the Office des Changes, the foreign-exchange regulator; the Autorite Marocaine du Marche des Capitaux (AMMC), the capital-markets regulator; the Direction Generale des Impots (DGI), the tax administration.

Out of scope: companies holding crypto (IS), VAT on crypto services (see `morocco-vat`), residency and treaty questions, AML opinions.

## Ask the client first

1. Is the person a Moroccan tax resident in 2026? Any other country taxing them?
2. What happened: bought and held, sold for dirhams or foreign currency, swapped one crypto for another, paid for goods, mined or staked, received crypto as pay for work?
3. How often and how organised: a few occasional disposals, or frequent trading run like a business (tools, time, volume)?
4. Where are the assets and the proceeds: a foreign platform, a foreign bank account, a wallet? Did any dirhams leave Morocco to buy crypto?
5. What other income does the person have in 2026 (salary, CPU, auto-entrepreneur, RNS or RNR)? It decides which return the gain would sit on.
6. Has anything been declared already, or has the DGI or the Office des Changes written to them?

## The method, step by step

1. **State the legal status first.** Restricted and unregulated: not legal tender, not an authorised means of payment, no licensing or consumer protection. Do not say "legal" without that caveat, and do not say "fully banned" either.
2. **Check the draft law's status before relying on any new regime.** Law 42.25 and its decrees count only once published in the Bulletin officiel (sgg.gov.ma). Until then the 2017 position governs.
3. **Say plainly that the CGI 2026 has no crypto article and no crypto rate.** There is no published, binding DGI rate for crypto.
4. **Lay out the two analogies, side by side,** with the rate each would borrow from the CGI (table below). Do not choose between them for the user: whether activity is occasional or habitual is a facts-and-circumstances judgement for the reviewer.
5. **Default to disclosure, not silence.** A resident's worldwide income is in principle within the IR. Non-declaration is not advice this skill gives.
6. **Flag the exchange-control exposure,** which is often the sharper risk.
7. **Refer.** Every answer ends with referral to a Moroccan expert-comptable and, for cross-border flows, the Office des Changes.

### Rates, bands and thresholds

These are the CGI 2026 rates the two analogies would borrow. None of them names crypto. They show what is at stake, not the rule.

| Item | Rate or amount | Conditions | Year | Source URL |
|---|---|---|---|---|
| Crypto-specific IR rate | None | The CGI 2026 contains no article on crypto-assets or virtual currencies | 2026 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Gains on listed shares and equity UCITS (profits de capitaux mobiliers) | 15% of net gain | Art. 73-II-C-1°. The occasional-disposal analogy for a listed-type asset | 2026 | same |
| Gains on bonds, unlisted shares, other securities | 20% of net gain | Art. 73-II-F-2°. Securities are defined at Art. 66-II-A; crypto is not on that list | 2026 | same |
| Foreign-source capital gains (profits de capitaux mobiliers de source etrangere) | 20% of gross profit | Art. 73-II-F-5°. Relevant if the asset is treated as foreign-source; an analogy only | 2026 | same |
| IR scale, exempt band | 0% to MAD 40,000 a year | Art. 73-I. The habitual-activity analogy (revenus professionnels, net profit) | 2026 | same |
| IR scale, top band | 37% above MAD 180,000 | Art. 73-I. Bands of 10%, 20%, 30% and 34% between | 2026 | same |
| Annual return of securities disposals | Before 1 April of the following year | Art. 84. For gains taxed as profits de capitaux mobiliers | 2026 | same |
| Global income return, professional income on RNS or RNR | Before 1 May of the following year | Art. 82-I | 2026 | same |
| Global income return, other income | Before 1 March of the following year | Art. 82-I | 2026 | same |

### The 2017 notice (the status quo)

On 20 November 2017 the Office des Changes, Bank Al-Maghrib and the AMMC issued a joint communique on monnaies virtuelles (virtual currencies). As reported, it said:

- transactions carried out through virtual currencies are an infraction a la reglementation des changes (a breach of exchange-control rules), open to the sanctions and fines the law provides;
- financial transactions with other countries must go through approved intermediaries (intermediaires agrees) in currencies quoted by Bank Al-Maghrib, and crypto is not such a currency;
- virtual currencies are an unregulated, opaque, highly volatile payment system, not backed by any financial institution and without protection for users.

The trigger was a Moroccan company announcing it would accept Bitcoin. Holding crypto is not expressly criminalised as mere possession, but using it, especially to move value across the border, is treated as a regulatory breach. Describe it to the user as "restricted and unregulated". The communique text was not reopened today (see Not yet confirmed).

Reality check: press reports cite millions of Moroccan holders. Widespread use does not change the legal status. Flag the gap.

### The draft law (projet de loi n° 42.25)

The authorities have signalled a move from prohibition to regulation. The vehicle reported is draft law 42.25 on crypto-assets, prepared by the Ministry of Economy and Finance, Bank Al-Maghrib and the AMMC, reportedly inspired by the EU MiCA regulation. Reported design: crypto-assets as a distinct financial-asset category (not legal tender, not a means of payment); exchanges and custodians licensed and supervised; the AMMC over issuers and platforms, Bank Al-Maghrib over stablecoins (including a possible dirham-backed stablecoin); a transition period (reported about 18 months) and decrees setting capital, reporting and AML thresholds. Reported timeline: public consultation in November 2025, parliamentary review in 2026. None of this is confirmed from an official text: until the law and its decrees appear in the Bulletin officiel, do not present 42.25 as in force.

### Analogy 1: occasional disposal, profits de capitaux mobiliers

If a private individual buys and later sells now and then, the closest analogy is profits de capitaux mobiliers, the category used for securities (Art. 66-II, rates at Art. 73-II-C and F). The CGI taxes gains on valeurs mobilieres and is silent on crypto, so applying it is an analogy, not a rule. Any rate would be borrowed.

### Analogy 2: habitual activity, revenus professionnels

If the activity is habitual, organised and speculative (frequent trading, mining as a business, run like a profession), the DGI could treat it as revenus professionnels taxed on net profit on the progressive scale, with the cotisation minimale and bookkeeping duties that follow. See `morocco-professional-income-tax`. Do not decide "occasional" against "habitual" mechanically.

### What this skill will and will not say

- It will explain that realised gains are in principle within the scope of income reporting for a resident, even for an unregulated asset.
- It will set out the two competing classifications and that the rate is unsettled.
- It will not quote a single "crypto tax rate" as Moroccan law.
- It will not help structure a non-declaration.
- It will not decide occasional against habitual without the facts and an expert-comptable's view.

Caution on secondary figures: some web sources cite "2022 DGI guidance treating crypto as an intangible asset taxed at 20%" and others "a planned 15% to 30% rate". Neither appears in the CGI 2026 or in Note circulaire 737 on Finance Law 2026 (both searched on 14 Nov 2026). Treat them as unconfirmed claims; never present them as the rule.

### Exchange control (Office des Changes)

Morocco runs exchange control (reglementation des changes). Under the 2017 notice, crypto transactions, especially cross-border ones, are treated as an infraction, open to administrative sanctions and fines (scale not confirmed). Lawful cross-border transactions go through intermediaires agrees in currencies quoted by Bank Al-Maghrib; crypto is neither. Sending dirhams abroad to buy crypto, bringing crypto proceeds home, or using crypto to move value across the border can all breach these rules. This skill never advises bypassing exchange control: refer to the Office des Changes and an expert-comptable.

## Boundary and exception table

| Situation | Position | What to do |
|---|---|---|
| Bought and holds, nothing sold | No realised gain; legal status still restricted | Explain status; no IR computation |
| A few disposals for dirhams | Analogy 1 most often discussed; unsettled | Show both analogies; refer |
| Frequent trading, mining or staking as a business | Analogy 2 more likely; unsettled | Route the computation to `morocco-professional-income-tax`; refer |
| Crypto swapped for another crypto | No rule on whether a swap realises a gain | Flag; refer |
| Crypto received as pay for services | Income of the activity it pays for (professional or salary), valued at receipt; no crypto rule | Treat as income of that activity; refer |
| Assets on a foreign platform, proceeds abroad | Exchange-control exposure as well as tax | Refer to the Office des Changes first |
| User asks for "the crypto tax rate" | There is none in the CGI 2026 | Say so; show the borrowed rates only as a range |
| User cites Law 42.25 as in force | Not confirmed | Ask for the Bulletin officiel reference; until then the 2017 position governs |
| Company holding crypto | Outside this skill (IS) | Refer |
| Residency, treaty or AML question | Outside this skill | Refer |

### Conservative defaults

- Default to "not a settled regime".
- Default to disclosure, not silence.
- Default to treating exchange-control rules as binding.
- Default to "verify the draft law's status" at BAM, the AMMC, the SGG (Bulletin officiel) and the DGI.
- Default to referral: this is high-risk, unsettled, and affects the user's money and legal exposure.

## Worked cases

Both cases show the range at stake under the two analogies. They are not a computation of tax due: the classification is unsettled.

**Case 1: occasional seller, net gain MAD 100,000 in 2026, no other income.** Under analogy 1 at the borrowed 20% (Art. 73-II-F-2°): MAD 20,000. Under analogy 2, the gain as the only professional income on the 2026 scale: 100,000 x 30% less 18,000 = MAD 12,000. The analogies give different answers, and the "investment" one is higher here, which is why the user must not pick the cheaper one alone.

```oa-check
name: Occasional crypto gain 100000, the two analogies
inputs:
  gain: 100000
steps:
  - analogy_securities: gain * 0.20
  - analogy_professional: gain * 0.30 - 18000
  - spread: analogy_securities - analogy_professional
expected:
  analogy_securities: 20000
  analogy_professional: 12000
  spread: 8000
```

**Case 2, a decision on what to bring to the expert-comptable: a day trader with net trading profit of MAD 250,000 in 2026 and no other income.** The pattern (daily trades, tools, volume) points toward analogy 2. On the 2026 scale: 250,000 x 37% less 27,400 = MAD 65,100. Under analogy 1 at 20%: MAD 50,000. The MAD 15,100 gap is the money at stake in the classification, so the file goes to an expert-comptable with the trade history before anything is declared. The exchange-control question (where the funds came from and sit) goes to the Office des Changes in parallel.

```oa-check
name: Day trader profit 250000, the two analogies
inputs:
  profit: 250000
steps:
  - analogy_professional: profit * 0.37 - 27400
  - analogy_securities: profit * 0.20
  - at_stake: analogy_professional - analogy_securities
expected:
  analogy_professional: 65100
  analogy_securities: 50000
  at_stake: 15100
```

## When to refuse or refer

- Do not assert that Morocco has a settled crypto tax regime or quote a single crypto tax rate as law.
- Do not say crypto is "legal in Morocco" without the 2017 restricted and unregulated caveat; do not call it fully "banned" either.
- Do not present draft law 42.25 as in force.
- Do not repeat secondary-source rates (20%, 15% to 30%) as Moroccan law.
- Do not advise, suggest or help a breach of the reglementation des changes: refer to the Office des Changes.
- Do not advise non-declaration of realised gains or help structure concealment.
- Do not decide occasional against habitual for the user.
- Do not give residency, treaty or AML opinions here.
- Do not issue any position as final without a Moroccan expert-comptable's sign-off.

## Filing and payment

There is no crypto return. If the expert-comptable takes a position:

1. Analogy 1 (profits de capitaux mobiliers): the annual return of disposals is due before 1 April of the following year (Art. 84), so before 1 April 2027 for 2026 gains.
2. Analogy 2 (revenus professionnels on RNS or RNR): the global income return is due before 1 May of the following year (Art. 82-I), so before 1 May 2027. Bookkeeping and the cotisation minimale follow (see `morocco-professional-income-tax`, `ma-bookkeeping`).
3. Other residents filing a global income return: before 1 March of the following year (Art. 82-I).

## Completion checklist

- Legal status stated as restricted and unregulated, with the 2017 notice.
- Law 42.25 status checked in the Bulletin officiel, or flagged as unconfirmed.
- "No crypto article in the CGI 2026" stated.
- Both analogies shown with the borrowed rates and labelled as analogy.
- Exchange-control risk flagged; nothing suggests bypassing approved intermediaries.
- Disclosure, not silence, as the default.
- Referral to an expert-comptable (and the Office des Changes for cross-border flows).

## Sources

| Source | URL | Read on |
|---|---|---|
| Code Général des Impôts 2026, DGI, French edition (includes Finance Law 50-25). Read for the absence of any crypto-asset or virtual-currency article (full-text search), Art. 66-II securities definition, Art. 73-I scale, Art. 73-II-C-1° 15%, Art. 73-II-F-2° and 5° 20%, Art. 82-I and 84 return dates | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-14 |

Not yet confirmed: the text and date of the November 2017 Office des Changes, Bank Al-Maghrib and AMMC communique on virtual currencies (not reopened today; bkam.ma refuses scripts and no copy was found on oc.gov.ma); the number, content and adoption status of draft law 42.25 and its decrees (no official text found on sgg.gov.ma, ammc.ma or oc.gov.ma on 14 Nov 2026); the scale of exchange-control fines; any DGI circular or ruling on crypto.
