---
name: eg-crypto-tax
description: Use this skill whenever asked about the legal status or taxation of cryptocurrency in Egypt — Bitcoin, stablecoins, tokens, NFTs, mining, staking, or trading — for individuals, freelancers, or small businesses. Trigger on phrases like "crypto tax Egypt", "is crypto legal in Egypt", "Bitcoin Egypt tax", "cryptocurrency Egypt", "ضريبة العملات المشفرة", "هل البيتكوين قانوني في مصر", "العملات الرقمية مصر", or any request to classify, compute, or explain Egyptian tax on crypto gains. ALWAYS read this skill before touching any Egypt crypto question. The AI must reply in the user's language (English or Arabic / Egyptian Arabic).
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Crypto Tax

## Egypt Cryptocurrency — Legal Status & Tax (العملات المشفرة) Skill v1.0

This skill covers the **regulatory** and **possible tax** treatment of cryptocurrency (العملات المشفرة / العملات الرقمية) in Egypt for individuals and small businesses. The AI must reply in the user's language (English or Arabic / Egyptian Arabic) and may use the native terms shown throughout.

> **READ FIRST — this is the single most important point in this skill.**
> Crypto is **not a regulated, licensed activity in Egypt**. Under the Central Bank Law, issuing, trading, promoting, or operating a crypto platform requires a **CBE licence that has not, in general, been granted to anyone**. Dealing in crypto in Egypt therefore carries **real legal risk, including criminal penalties**. And there is **no specific crypto tax law and no clear ETA guidance** — anything said about tax below is *uncertain and provisional*. This skill is **informational only**. It is **not** encouragement to deal in crypto, and it does **not** make crypto dealing legal or safe.

> **YMYL — verify before relying.** Egyptian crypto law and any tax position may change. Re-confirm against the **Central Bank of Egypt (CBE — cbe.org.eg)**, the **Egyptian Tax Authority (ETA — eta.gov.eg)**, **PwC Worldwide Tax Summaries (taxsummaries.pwc.com/egypt)** or a Big-4 / local-counsel alert before acting. **Always involve a qualified Egyptian lawyer (محامٍ) for the legal-risk question — not just an accountant.**

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Egypt (جمهورية مصر العربية) |
| Topic | Legal status & taxation of cryptocurrency (العملات المشفرة) |
| Currency | EGP (Egyptian Pound — ج.م) |
| **Legal status** | **Restricted / unlicensed** — issuance, trading, promotion and platform operation prohibited without CBE approval under **Banking Law No. 194 of 2020 (Art. 206)**; no general licence granted |
| **Tax** | **No specific crypto tax regime; no clear ETA guidance** — treatment uncertain (see Section 3) |
| Regulator | Central Bank of Egypt (CBE — البنك المركزي المصري) — cbe.org.eg |
| Tax authority | Egyptian Tax Authority (ETA — مصلحة الضرائب المصرية) — eta.gov.eg |
| Religious ruling | Fatwa declaring crypto haram (the Grand Mufti / Dar al-Ifta, 2018) — moral/social weight, **not** a law |
| Contributor | Open Accountants Community |
| **Quality tier** | **Research-verified — pending sign-off by a qualified Egyptian accountant (محاسب قانوني) and lawyer (محامٍ)** |
| Skill version | 1.0 |

⚠️ **Prominent warning (اقرأ بعناية).** In Egypt, crypto is **not a normal investment asset with a known tax rate**. The activity itself is **legally restricted and may expose the person to criminal liability** (imprisonment and large fines — see Section 2). Do **not** present a clean "buy → gain → pay X% tax" picture as if Egypt worked like a crypto-friendly jurisdiction. It does not.

### Conservative defaults (مبادئ احترازية)

When the position is unclear (which is almost always for Egyptian crypto), apply these defaults:

1. **Legal status first, tax second.** Never discuss tax without first stating the regulatory restriction and legal risk. The legal question dominates.
2. **Do not declare crypto legal or safe.** State the restriction plainly.
3. **No definitive tax rate.** There is no settled crypto tax rate in Egypt. Refuse to assert one. Present *possibilities*, clearly flagged as uncertain.
4. **If the person already has gains and wants to be compliant**, treat any declared income on the *conservative* (higher-tax / fully-taxable) basis and route them to a credentialed Egyptian professional rather than guessing.
5. **Escalate to a human.** For any real situation involving money, hand off to a qualified Egyptian accountant **and** lawyer. Do not let the user rely on this skill alone.

## Section 2 — Regulatory status & legal risk (الوضع القانوني)

- **Core rule — CBE licence requirement** — Under the Central Bank and Banking Sector Law No. 194 of 2020 — Egypt's banking law — Article 206 prohibits the issuance, trading, promotion, or operation of platforms dealing in cryptocurrencies or "cryptographic units" without prior approval (a licence) from the Central Bank of Egypt (CBE).  _(Central Bank and Banking Sector Law No. 194 of 2020, Art. 206)_

### The core rule

The decisive practical fact: **the CBE has not, in general, granted any such licence.** No crypto exchange or crypto business is known to be CBE-licensed. The result is that crypto dealing in Egypt is **effectively restricted and unlicensed** — i.e. carried on outside any legal/regulated framework.

### Penalties

Reported penalties under the framework include **imprisonment** and **fines**, with figures cited up to the **multi-million EGP** range (sources commonly cite fines in the hundreds of thousands up to ~EGP 10 million, plus possible imprisonment). *Exact current penalty figures must be verified against the law text and a local lawyer — do not quote a precise number as settled.*

### CBE public warnings

The CBE has **repeatedly and publicly warned** the public against dealing in cryptocurrencies, citing extreme volatility, fraud risk, money-laundering / terrorist-financing exposure, and — critically — that **Egyptian law gives no recourse to recover funds lost** in crypto transactions. These warnings have been issued/renewed on multiple occasions (e.g. statements around 2018 and 2021).

### Religious ruling (fatwa)

Egypt's **Grand Mufti / Dar al-Ifta issued a fatwa (2018) declaring crypto haram (محرّم)**, citing speculation, uncertainty (gharar), and fraud risk. A fatwa is a **religious opinion with significant social and moral weight in Egypt — but it is not itself a statute.** Mention it for context; the binding legal restriction is Law 194/2020, not the fatwa.

### What this means in practice

- Crypto is **not** a recognised legal currency or a regulated investment asset in Egypt.
- Operating an exchange, brokering, promoting, or running a crypto platform in Egypt without a (non-existent) CBE licence is **prohibited and penalised**.
- Even an *individual* simply trading crypto operates in a **legally grey-to-prohibited zone with real downside risk** and **no legal protection** if funds are lost or stolen.
- The honest summary for any user: **"In Egypt, crypto dealing is restricted and legally risky. There is no clean, safe, taxed-and-blessed way to do it."**

## Section 3 — Possible income-tax treatment IF gains arise (uncertain)

> **Heavy caveat (تنبيه شديد).** Everything in this section is **conjecture about how existing tax law *might* be read** in the absence of a crypto-specific law or ETA guidance. **None of it is confirmed. Do not treat any of it as the definitive rule, and do not state a definitive rate.**

Egypt has **no specific cryptocurrency tax law** and the ETA provides **no dedicated section or guidance** for declaring crypto income. There is no established practice of filing crypto capital gains in Egypt, partly because the state does not recognise crypto as a legal asset/currency.

If a resident individual nonetheless realises gains from crypto activity and wants to be tax-compliant, the **general** Income Tax Law No. 91 of 2005 (as amended) is the only framework that *could* be reached. Possible — and competing — readings include:

1. **Commercial / industrial income (الأرباح التجارية والصناعية).** Frequent, organised, profit-seeking trading *might* be argued to be a commercial activity, taxed under the normal **progressive personal income tax brackets** (see the `eg-income-tax` skill for the current bracket table). This is the most likely "conservative" reading for an active trader.

2. **Non-commercial / professional income (إيرادات المهن غير التجارية).** Less likely, but conceivable for certain activity patterns.

3. **No clear charging provision at all.** Because crypto is not a recognised asset and the activity is itself restricted, it is genuinely unclear whether any income-tax charge cleanly attaches, and there is **no general personal capital-gains tax** on most assets in Egypt to fall back on.

There is **no settled rate, no recognised cost-basis method, no loss-relief position, and no filing line** for crypto. **Do not invent one.** Note also the uncomfortable interaction: declaring crypto income may simultaneously *evidence* participation in a restricted activity — a point only a **lawyer** can advise on.

**Practical guidance the AI should give:** route the person to a qualified Egyptian accountant **and** lawyer; if they choose to declare, the conservative default is to treat realised gains as fully taxable commercial income under the ordinary brackets and to keep complete records — while understanding the legal exposure of the underlying activity.

## Section 4 — What we DON'T know / open questions (أسئلة مفتوحة)

Be transparent with the user about every one of these:

- **No crypto-specific statute or ETA circular.** There is no published rule that says how (or whether) crypto gains are taxed.
- **Which category, if any** — commercial, non-commercial, "other" — applies is unsettled.
- **No confirmed rate** for crypto specifically.
- **Cost basis, FX conversion (USD/USDT → EGP), and timing** of any gain are undefined for tax purposes.
- **Losses** — whether deductible or carried forward — undefined.
- **Mining, staking, airdrops, NFTs, DeFi yield, P2P** — no specific treatment; arguably even more exposed on the legal side.
- **Interaction with the restriction itself** — whether and how one can declare income from a restricted activity is a legal question, not just a tax one.
- **Enforcement reality vs. the letter of the law** — these can diverge, and this skill does not assess prosecution likelihood. A lawyer must.
- **Foreign-exchange / capital-controls rules** may also bear on moving funds in and out — out of scope here; verify separately.

When asked something covered above, the correct answer is **"this is not established in Egypt — here is why, and here is who to ask,"** not a guess.

## Section 5 — Worked examples (heavily caveated)

> Every example below is **illustrative only**. They do **not** establish that the treatment shown is correct, legal, or safe. They show *how the AI should respond*, with the warnings attached.

### Example 1 — "Is Bitcoin legal in Egypt and how is it taxed?"

**Correct response shape:**
- Lead with the legal status: crypto dealing is **restricted/unlicensed** under CBE Law 194/2020 (Art. 206); no general CBE licence exists; CBE has warned the public repeatedly; a fatwa deems it haram.
- State there is **no specific crypto tax law and no clear ETA guidance** — so no definitive tax answer exists.
- Flag the **legal risk** (possible imprisonment/fines) and **no legal recourse** if funds are lost.
- Recommend a qualified Egyptian **lawyer and accountant** before doing anything.
- Do **not** quote a tax rate as if settled.

### Example 2 — "I already made a profit trading on a foreign exchange. How much tax do I owe in Egypt?"

**Correct response shape:**
- Acknowledge the situation without endorsing the activity.
- Explain there is **no settled crypto tax rule**; *if* they choose to declare, the **conservative** default is to treat the realised gain as taxable commercial income under the ordinary personal income-tax brackets (point them to `eg-income-tax` for the current bracket table) — **clearly labelled as one uncertain interpretation, not the law.**
- Stress that declaring may also surface the **legal-status issue** — a lawyer must advise.
- Hand off to a credentialed Egyptian professional. **No firm number.**

### Example 3 — "Can I run a crypto exchange / OTC desk in Egypt?"

**Correct response shape:**
- Direct, unambiguous: operating a crypto platform/brokerage **without a CBE licence is prohibited** under Law 194/2020, and such licences are **not generally granted** — so this is **effectively not permitted** and carries **penalties (imprisonment and fines)**.
- This is a **legal-prohibition** answer, not a tax-planning one. Do **not** offer structuring or tax-optimisation advice for a restricted activity.
- Refer to a qualified Egyptian lawyer.

## Section 6 — Tier 2 details & references

### Tier 2 — escalate to a human professional when:

- **Escalation triggers** — - The user has real crypto gains and wants to file (accountant **+** lawyer). - The user is considering any crypto **business** in Egypt (lawyer first). - Any question of **enforcement risk, prosecution, or legality** of a specific plan (lawyer — outside this skill's competence). - Cross-border, FX, capital-controls, or AML/CTF angles arise. - The user wants certainty on a **rate, basis, or filing line** — there is none; escalate rather than fabricate.

### References (verify before relying)

- **Reference list** — - **CBE — Central Bank of Egypt** (cbe.org.eg): Banking Law No. 194 of 2020, Art. 206; public warnings against crypto dealing. - **ETA — Egyptian Tax Authority** (eta.gov.eg): Income Tax Law No. 91 of 2005 (as amended) — the general framework; **no crypto-specific guidance**. - **PwC Worldwide Tax Summaries** (taxsummaries.pwc.com/egypt) — general Egyptian tax background. - **Dar al-Ifta / Grand Mufti** — 2018 fatwa (religious opinion, not law). - Companion skills: `eg-income-tax` (brackets, filing), `eg-bookkeeping`, `egypt-vat`, `income-tax-workflow-base`.  _(CBE cbe.org.eg; ETA eta.gov.eg; PwC Worldwide Tax Summaries taxsummaries.pwc.com/egypt; Dar al-Ifta / Grand Mufti 2018 fatwa)_

## PROHIBITIONS (محظورات)

- **AI prohibitions** — The AI must **NEVER**: - **Never present crypto dealing as legal, permitted, or safe in Egypt.** It is restricted/unlicensed under CBE Law 194/2020 and carries real legal risk. - **Never assert a definitive crypto tax rate or filing treatment** for Egypt — none is settled; saying "you pay X%" is wrong and harmful. - **Never encourage** dealing in, promoting, or operating crypto in Egypt, or offer structuring/tax-optimisation advice for a restricted activity. - **Never imply the fatwa is the binding law** (the statute is) — or that the *absence* of a tax rule means crypto gains are tax-free or risk-free. - **Never let the user rely on this skill alone** for a real decision — always route to a qualified Egyptian lawyer and accountant. - **Never claim Egypt has no recourse problem solved, or that funds are protected** — the CBE warns there is no legal recourse for losses.  _(CBE Banking Law No. 194 of 2020)_

## Disclaimer (إخلاء مسؤولية)

This skill is **research-verified — pending sign-off by a qualified Egyptian accountant (محاسب قانوني) and lawyer (محامٍ)**. The legal and tax status of cryptocurrency in Egypt is **unsettled and high-risk**: dealing in crypto is restricted/unlicensed under CBE Banking Law No. 194 of 2020, and there is **no specific crypto tax law and no clear ETA guidance**. This material is **informational only** — it is **not** legal, tax, or financial advice, and it is **not** encouragement to deal in crypto. Anyone with a real situation must **consult a qualified Egyptian lawyer and accountant** before acting. Figures, penalties, and any tax position must be re-verified against the CBE, the ETA, and reputable sources at the time of use. Provided by the Open Accountants Community — **openaccountants.com**.

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
