---
name: ma-crypto-tax
description: Use this skill whenever asked about the taxation and legal status of cryptocurrency / crypto-assets in Morocco for a self-employed individual. Trigger on phrases like "Morocco crypto tax", "Bitcoin Maroc impôt", "cryptomonnaie Maroc légal", "crypto Morocco", "crypto-actifs Maroc", "is crypto legal in Morocco", "taxe cryptomonnaie Maroc", "Bitcoin impôt Maroc", "Office des Changes crypto", "loi 42.25 crypto", "stablecoin dirham", "الضريبة على العملات المشفرة المغرب", "العملات الرقمية المغرب". Covers the RESTRICTED / UNREGULATED status under the November 2017 Bank Al-Maghrib / AMMC / Office des Changes notice, the pending draft Law 42.25 on crypto-assets (verify 2026 status), the ABSENCE of any specific crypto tax regime, how gains MIGHT be treated if realised (profits from disposal of movable property / profits de capitaux mobiliers, or professional income / revenus professionnels if habitual, under the Impôt sur le Revenu), and the exchange-control (réglementation des changes) implications. This is HIGH-UNCERTAINTY, HIGH-RISK territory — the skill must never assert a settled regime. Reply in the user's language (English, French, or Moroccan Arabic / Darija) and keep native French terms in context.
version: 1.0
jurisdiction: MA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Crypto Tax

## Morocco — Taxation & Legal Status of Cryptocurrency (Cryptomonnaie / Crypto-actifs)

This skill explains how **cryptocurrency** (cryptomonnaie, crypto-actifs, actifs numériques) is treated in **Morocco** for a self-employed person — both its **legal status** and the **uncertain tax position** of any gains.

**Read this warning first.** As of **May 2026** Morocco has **no settled crypto tax regime** and crypto is **not freely legal**. The position rests on a **2017 prohibition notice** that is still in force and a **draft law (projet de loi n°42.25)** that has **not yet been adopted**. Anything in this skill about how gains "might" be taxed is **conjecture by analogy**, not established law. The correct posture is **honesty about the uncertainty** and **referral to a Moroccan expert-comptable** and, on exchange-control questions, to the **Office des Changes**.

The relevant authorities are **Bank Al-Maghrib (BAM)** — the central bank, the **Office des Changes** — the foreign-exchange regulator, the **Autorité Marocaine du Marché des Capitaux (AMMC)** — the capital-markets regulator, and the **Direction Générale des Impôts (DGI)** — the tax administration. This skill replies in the user's language and keeps native terms (crypto-actifs, profits de capitaux mobiliers, revenus professionnels, réglementation des changes, Impôt sur le Revenu / IR) explained in context.

## 1. Quick Reference

**Quick Reference**

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Topic | Legal status + (uncertain) tax treatment of cryptocurrency |
| Legal status | **Restricted / unregulated** — prohibited as a payment means since the **Nov 2017** notice; **not** legal tender; regulation **pending** |
| Authorities | **Bank Al-Maghrib (BAM)**, **Office des Changes**, **AMMC**, **DGI** |
| Currency | MAD (dirham marocain, DH) |
| Governing notice | Joint **Office des Changes / Bank Al-Maghrib / AMMC** communiqué, **20 November 2017** *(verify)* |
| Pending reform | **Projet de loi n°42.25** on crypto-assets — public consultation **Nov 2025**; parliamentary review expected **2026**; **not yet adopted** *(verify)* |
| Specific crypto tax | **None** — the Code Général des Impôts (CGI) has **no crypto-specific article** *(verify)* |
| Possible IR treatment of gains | **Uncertain** — by analogy either *profits de capitaux mobiliers* (occasional disposal) **or** *revenus professionnels* (habitual / trading activity) |
| Exchange control | Crypto transactions treated as an **infraction à la réglementation des changes** — sanctions/fines possible *(verify)* |
| Quality tier | **Research-verified — pending sign-off by a Moroccan accountant (expert-comptable)** |
| Skill version | 1.0 |

### Conservative defaults

When the facts are thin, default to the **safest, most honest** position:

- **Default = "not a settled regime."** Never tell a user there is a clear crypto tax rate or a clear legal pathway. There is not, as of May 2026.
- **Default to disclosure, not silence.** If a Moroccan tax resident has **realised** crypto gains, the conservative position is that worldwide income is in principle reportable under the IR even where the asset class is unregulated — but the **classification and rate are unsettled**, so route to an expert-comptable. Non-declaration is **not** advice this skill will give.
- **Default to "treat exchange-control rules as binding."** Never suggest moving funds or crypto across borders in a way that bypasses approved intermediaries (intermédiaires agréés) — the Office des Changes treats this as an infraction.
- **Default to "verify the draft law's status."** Law 42.25 was **not adopted** as of the last verification. Re-check BAM, the AMMC, the SGG (Bulletin Officiel), and the DGI before relying on any "new regime."
- **Default to referral.** This is YMYL, high-risk, and unsettled. Escalate to a Moroccan expert-comptable and, for FX questions, the Office des Changes.

## 2. Legal & Regulatory Status

### 2.1 The 2017 prohibition notice (the status quo)

- **2017 prohibition notice content** — On **20 November 2017** *(verify)* the **Office des Changes**, together with **Bank Al-Maghrib** and the **AMMC (Autorité Marocaine du Marché des Capitaux)**, issued a public communiqué warning against the use of **monnaies virtuelles** (virtual currencies). The key points, as widely reported: - Transactions carried out via virtual currencies constitute an **infraction à la réglementation des changes** (a breach of foreign-exchange regulations), **subject to the sanctions and fines** provided for by law. - Financial transactions with foreign countries must go through **approved intermediaries** (intermédiaires agréés) in **currencies quoted by Bank Al-Maghrib** — crypto is not such a currency. - Virtual currencies are described as an **unregulated, opaque, highly volatile payment system, not backed by any financial institution** and **devoid of protection** for users. - The trigger was a Moroccan company announcing it would accept Bitcoin; the authorities responded by declaring the practice **unauthorised in Morocco**. The practical effect: holding, buying, selling, or paying with crypto is **not expressly criminalised as mere possession**, but using it — especially for cross-border value transfer — is treated as a **regulatory breach**. There is **no licensing, no consumer protection, and no legal-tender status**. This is best described to the user as **"restricted / unregulated,"** not a clean "legal" or a clean "banned."  _(Joint Office des Changes / Bank Al-Maghrib / AMMC communiqué, 20 November 2017 (verify))_

> **Reality check.** Despite the prohibition, reporting suggests **millions of Moroccans** hold crypto (figures around **6 million / ~16% of the population** are cited — *verify, this is journalistic, not official*). Widespread use does **not** change the legal status. Flag this gap to the user.

### 2.2 The pending draft law (projet de loi n°42.25)

- **Draft law 42.25 status** — Since around **late 2024**, the authorities have signalled a **change of doctrine** toward **regulating** rather than simply prohibiting crypto. The vehicle is the **projet de loi n°42.25** on crypto-assets *(verify number and status)*: - Developed jointly by the **Ministère de l'Économie et des Finances**, **Bank Al-Maghrib**, and the **AMMC**, reportedly **inspired by the EU's MiCA** regulation and aligned with FATF / BIS / IMF recommendations *(verify)*. - Reportedly opened for **public consultation in November 2025**, with **parliamentary review expected in 2026** and **possible adoption around mid-2026** *(verify — adoption was NOT confirmed at last check)*. - Reported design: crypto-assets treated as a **distinct financial-asset category** (not legal tender, not a payment means); **service providers** (exchanges, custodians) would be **licensed and supervised**, with the **AMMC** overseeing issuers/platforms and **Bank Al-Maghrib** overseeing **stablecoins** (including a possible **dirham-backed stablecoin**) *(verify)*. - A **transition period** (reported ~18 months) and **application decrees** (décrets d'application) would set capital, reporting, and AML thresholds *(verify)*. **Until this law is adopted and its décrets published in the Bulletin Officiel, the 2017 prohibition remains the governing position.** Do not present 42.25 as if it were in force.  _(Projet de loi n°42.25 (verify))_

## 3. Possible Tax Treatment of Gains (UNCERTAIN)

> **This entire section is conjecture by analogy.** The **Code Général des Impôts (CGI)** contains **no crypto-specific provision** as of May 2026 *(verify)*. There is **no published, binding DGI rate for crypto**. Do not state a rate as settled. Route to an expert-comptable.

If a **Moroccan tax resident** has **realised** a gain (sold crypto for fiat, swapped one crypto for another, or paid for goods with crypto), the question is which existing IR category, if any, the DGI would apply. The two analogies most often discussed:

### 3.1 Occasional disposal → *profits de capitaux mobiliers*

- **Occasional disposal analogy** — If the activity looks like **occasional investment** (a private individual buys and later sells), the closest analogy is **profits de capitaux mobiliers** (profits from the disposal of movable capital / movable property) under the IR — the category used for securities and shares. Commentators note the CGI taxes gains on **valeurs mobilières** but is **silent on crypto**, so applying this category to crypto is **an analogy, not a rule**. Any rate (e.g., the securities-type rates) would be **borrowed**, not crypto-specific — **verify; do not assert**.  _(unsure - no official CGI citation given)_

### 3.2 Habitual activity → *revenus professionnels*

- **Habitual activity analogy** — If the activity is **habitual, organised, and speculative** (frequent trading, mining as a business, running it like a profession), the DGI could instead treat it as **revenus professionnels** (business / professional income) taxed on **net profit** through the **progressive IR scale**, with the **cotisation minimale** and bookkeeping obligations that implies. For how professional income is computed, see **`ma-income-tax`**. Whether a given pattern crosses into "habitual" is a **facts-and-circumstances** judgement for the reviewer — do not decide it mechanically.  _(see ma-income-tax)_

### 3.3 What this skill will and will not say

- It **will** explain that **realised gains are, in principle, within the scope of income reporting** for a resident, even for an unregulated asset.
- It **will** lay out the **two competing classifications** and that the **rate is unsettled**.
- It will **not** quote a single "crypto tax rate" as Moroccan law.
- It will **not** help structure a non-declaration.
- It will **not** opine on whether the activity is "occasional" vs "habitual" without the user's facts and an expert-comptable's confirmation.

> **Caution on aggregator figures.** Some web sources cite a "2022 DGI guidance treating crypto as an intangible asset taxed at 20%," and others a "planned 15–30% rate." These are **not reliably confirmed against the CGI or an official DGI circular** and must be treated as **unverified**. Do **not** present them as the rule. List them only as claims to verify.

## 4. Exchange-Control Implications (Office des Changes)

- **Exchange control implications** — Morocco operates a **regime of exchange control** (réglementation des changes). This is often the **sharper** legal risk than tax: - Under the **2017 notice**, crypto transactions — especially **cross-border** ones — are treated as an **infraction à la réglementation des changes**, exposing the user to **administrative sanctions and fines** *(verify scale)*. - Lawful cross-border financial transactions must use **intermédiaires agréés** (approved banks/intermediaries) and **currencies quoted by Bank Al-Maghrib**. Crypto is neither. - Sending dirhams abroad to buy crypto, repatriating crypto proceeds, or using crypto to move value across the border can all fall foul of these rules. - The Office des Changes has reportedly **increased scrutiny** of crypto flows as usage has grown *(verify)*. **This skill never advises a user to bypass exchange controls.** If the user asks how to move crypto in or out of Morocco outside approved channels, decline and refer them to the **Office des Changes** and an expert-comptable.  _(2017 notice (Office des Changes / BAM / AMMC))_

## 5. Risk Flags

Surface these **prominently** in any answer — do not bury them:

- **Unsettled regime.** No crypto-specific tax law and no clean legal status. Any tax treatment is **analogy**, not rule.
- **Active prohibition.** The **2017 notice is still in force**. Crypto is **not** authorised as a payment means and is **not** legal tender.
- **Exchange-control exposure.** Cross-border crypto activity may be an **infraction à la réglementation des changes** with **fines/sanctions**.
- **Moving target.** **Law 42.25** could change everything — or could stall. **Verify its current status** (BAM, AMMC, DGI, Bulletin Officiel) before relying on anything. Décrets d'application will carry the operative detail.
- **Unreliable secondary figures.** Rates floating around the web (20%, 15–30%) are **unverified**. Do not repeat them as fact.
- **Residency & double-tax not covered here.** Treaty/residency questions are out of scope — refer out.
- **YMYL + high risk.** This affects the user's money and legal exposure. **Always route to a Moroccan expert-comptable** and, for FX, the **Office des Changes**.

## 6. Reference

Verify **every** figure, date, and classification before use. Primary > secondary.

- **Office des Changes** — oc.gov.ma — the 2017 communiqué on monnaies virtuelles and any updated warnings; exchange-control rules and sanctions.
- **Bank Al-Maghrib (BAM)** — bkam.ma — joint 2017 warning; statements on the crypto-asset framework and stablecoins; status of the reform.
- **AMMC (Autorité Marocaine du Marché des Capitaux)** — ammc.ma — supervisory role under the draft framework.
- **Direction Générale des Impôts (DGI)** — tax.gov.ma — the **Code Général des Impôts (CGI)**; confirm there is (or is not) any crypto-specific provision or circular; categories *profits de capitaux mobiliers* and *revenus professionnels*.
- **Secrétariat Général du Gouvernement (SGG)** / **Bulletin Officiel** — to confirm whether **projet de loi n°42.25** and its **décrets d'application** have been **adopted and published**.
- **PwC Worldwide Tax Summaries — Morocco** — for the general IR framework and any note on crypto *(verify whether PwC has yet added a crypto section)*.
- **Companion skills:** `ma-income-tax` (professional income / IR computation), `morocco-vat` (TVA), `ma-bookkeeping` (records).

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT** assert that Morocco has a **settled crypto tax regime** or quote a single crypto tax **rate** as law — there is **none** confirmed as of May 2026. - **Do NOT** state that crypto is **"legal in Morocco"** without the **2017 prohibition / unregulated** caveat; equally do not say it is fully "banned" — describe it as **restricted / unregulated**. - **Do NOT** present **projet de loi n°42.25** as if it were **in force** — it was **not adopted** at last verification; always flag "verify status." - **Do NOT** repeat secondary-source **rates (e.g., 20%, 15–30%)** as established Moroccan law — flag them as **unverified**. - **Do NOT** advise, suggest, or help a user **breach the réglementation des changes** (e.g., moving crypto/funds across the border outside approved intermediaries) — refer to the **Office des Changes**. - **Do NOT** advise **non-declaration** of realised gains or help structure concealment. - **Do NOT** decide whether the activity is **"occasional" vs "habitual"** for the user — that is a reviewer judgement on the user's facts. - **Do NOT** give **residency, treaty, or AML** opinions under this skill — route out. - **Do NOT** issue any position as final without **Moroccan expert-comptable** sign-off.

## Disclaimer

This skill is **research-verified** against public sources — the **Office des Changes** (oc.gov.ma), **Bank Al-Maghrib** (bkam.ma), the **AMMC**, the **DGI** (tax.gov.ma) and **PwC Worldwide Tax Summaries (Morocco)**, plus 2025–2026 reporting on **projet de loi n°42.25** — as of **May 2026**. It is **YMYL, high-risk** content covering an **unsettled area of law** and is **pending sign-off by a Moroccan accountant (expert-comptable)**. There is **no settled crypto tax regime** in Morocco; everything about how gains might be taxed is **analogy, not established law**, and the legal status rests on a **2017 prohibition notice** with a **draft law still pending**. Dates, the status of Law 42.25, classifications, and any rate must be **re-verified** against the official authorities before use. Nothing here is a substitute for advice from a licensed Moroccan expert-comptable, the DGI, or the Office des Changes. Part of **openaccountants.com** — open-source tax skills for the self-employed.

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
