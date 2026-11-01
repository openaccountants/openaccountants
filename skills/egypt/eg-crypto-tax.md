---
name: eg-crypto-tax
description: Use this skill whenever asked about the legal status or taxation of cryptocurrency in Egypt , Bitcoin, stablecoins, tokens, NFTs, mining, staking, or trading , for individuals, freelancers, or small businesses. Trigger on phrases like "crypto tax Egypt", "is crypto legal in Egypt", "Bitcoin Egypt tax", "cryptocurrency Egypt", "ضريبة العملات المشفرة", "هل البيتكوين قانوني في مصر", "العملات الرقمية مصر", or any request to classify, compute, or explain Egyptian tax on crypto gains. ALWAYS read this skill before touching any Egypt crypto question. The AI must reply in the user's language (English or Arabic / Egyptian Arabic).
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Crypto Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers how Egyptian income tax reaches cryptocurrency gains, for individuals and small businesses, tax year 2026. Reply in the user's language, English or Arabic.

## Who this applies to

Individuals and small businesses with crypto income: trading, mining, staking, airdrops, NFTs, DeFi and P2P. Companies: `eg-corporate-tax`. Legal permission to deal in crypto is a separate question and needs an Egyptian lawyer before any tax work; the rule the old skill cited could not be opened (see Sources). State this first in every answer: "If you deal in crypto in Egypt, a lawyer must first confirm whether the activity is permitted."

## Rates, bands and thresholds

No crypto rate exists in the tax laws read. Laws 91/2005, 7/2024, 151/2026, 206/2020 and 6/2025 do not mention it. The ordinary table applies to whatever falls within a charge. The table is held in `eg-income-tax`, one home for those figures.

| Item | Rule | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Rates | `eg-income-tax` table | Individual whose gains are income under the classes below | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf |
| Charge on organised activity | Commercial profit, even from a single deal (art. 19 item 3), or the class covering income from any profession or activity not otherwise listed | Law 91 art. 19; art. 32 item 3 as replaced by Law 53/2014 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Listed-securities exemption | Does not apply | Covers securities listed on the Egyptian exchange (Law 151/2026) | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |

## The base

If activity is regular and profit-seeking, treat the year's net gain as income from activity on the normal base. If there is no crypto-specific rule, say so: no cost-basis method, FX method, loss rule or filing line is published. Keep complete records in EGP at the date of each trade and show the method chosen. Open questions the AI must state rather than fill: which class applies, whether a one-off disposal is caught at all, losses, and treatment of mining, staking, airdrops, NFTs, DeFi yield and P2P.

Do not say gains are tax-free because no rule exists. Do not give a rate as settled for crypto. Declaring may also be evidence of the activity, which is a lawyer's question.

**Carried from the earlier version, not checked against the law.** Kept so no working rule is lost. Any figure here is unverified, and where it differs from the tables above the tables win.

Crypto is **not a regulated, licensed activity in Egypt**. Under the Central Bank Law, issuing, trading, promoting, or operating a crypto platform requires a **CBE licence that has not, in general, been granted to anyone**. Dealing in crypto in Egypt therefore carries **real legal risk, including criminal penalties**. And there is **no specific crypto tax law and no clear ETA guidance**: anything said about tax below is *uncertain and provisional*. This skill is **informational only**. It is **not** encouragement to deal in crypto, and it does **not** make crypto dealing legal or safe.
⚠️ **Prominent warning (اقرأ بعناية).** In Egypt, crypto is **not a normal investment asset with a known tax rate**. The activity itself is **legally restricted and may expose the person to criminal liability** (imprisonment and large fines: see Section 2). Do **not** present a clean "buy → gain → pay X% tax" picture as if Egypt worked like a crypto-friendly jurisdiction. It does not.
1. **Legal status first, tax second.** Never discuss tax without first stating the regulatory restriction and legal risk. The legal question dominates.
2. **Do not declare crypto legal or safe.** State the restriction plainly.
3. **No definitive tax rate.** There is no settled crypto tax rate in Egypt. Refuse to assert one. Present *possibilities*, clearly flagged as uncertain.
4. **If the person already has gains and wants to be compliant**, treat any declared income on the *conservative* (higher-tax / fully-taxable) basis and route them to a credentialed Egyptian professional rather than guessing.
The decisive practical fact: **the CBE has not, in general, granted any such licence.** No crypto exchange or crypto business is known to be CBE-licensed. The result is that crypto dealing in Egypt is **effectively restricted and unlicensed**: i.e. carried on outside any legal/regulated framework.
Reported penalties under the framework include **imprisonment** and **fines**, with figures cited up to the **multi-million EGP** range (sources commonly cite fines in the hundreds of thousands up to ~EGP 10 million, plus possible imprisonment). *Exact current penalty figures must be verified against the law text and a local lawyer: do not quote a precise number as settled.*
The CBE has **repeatedly and publicly warned** the public against dealing in cryptocurrencies, citing extreme volatility, fraud risk, money-laundering / terrorist-financing exposure, and: critically: that **Egyptian law gives no recourse to recover funds lost** in crypto transactions. These warnings have been issued/renewed on multiple occasions (e.g. statements around 2018 and 2021).
Egypt's **Grand Mufti / Dar al-Ifta issued a fatwa (2018) declaring crypto haram (محرّم)**, citing speculation, uncertainty (gharar), and fraud risk. A fatwa is a **religious opinion with significant social and moral weight in Egypt: but it is not itself a statute.** Mention it for context; the binding legal restriction is Law 194/2020, not the fatwa.
- Crypto is **not** a recognised legal currency or a regulated investment asset in Egypt.
- Operating an exchange, brokering, promoting, or running a crypto platform in Egypt without a (non-existent) CBE licence is **prohibited and penalised**.
- Even an *individual* simply trading crypto operates in a **legally grey-to-prohibited zone with real downside risk** and **no legal protection** if funds are lost or stolen.
- The honest summary for any user: **"In Egypt, crypto dealing is restricted and legally risky. There is no clean, safe, taxed-and-blessed way to do it."**
**Heavy caveat (تنبيه شديد).** Everything in this section is **conjecture about how existing tax law *might* be read** in the absence of a crypto-specific law or ETA guidance. **None of it is confirmed. Do not treat any of it as the definitive rule, and do not state a definitive rate.**

Egypt has **no specific cryptocurrency tax law** and the ETA provides **no dedicated section or guidance** for declaring crypto income. There is no established practice of filing crypto capital gains in Egypt, partly because the state does not recognise crypto as a legal asset/currency.

If a resident individual nonetheless realises gains from crypto activity and wants to be tax-compliant, the **general** Income Tax Law No. 91 of 2005 (as amended) is the only framework that *could* be reached. Possible: and competing: readings include:

1. **Commercial / industrial income (الأرباح التجارية والصناعية).** Frequent, organised, profit-seeking trading *might* be argued to be a commercial activity, taxed under the normal **progressive personal income tax brackets** (see the `eg-income-tax` skill for the current bracket table). This is the most likely "conservative" reading for an active trader.

2. **Non-commercial / professional income (إيرادات المهن غير التجارية).** Less likely, but conceivable for certain activity patterns.

3. **No clear charging provision at all.** Because crypto is not a recognised asset and the activity is itself restricted, it is genuinely unclear whether any income-tax charge cleanly attaches, and there is **no general personal capital-gains tax** on most assets in Egypt to fall back on.

There is **no settled rate, no recognised cost-basis method, no loss-relief position, and no filing line** for crypto. **Do not invent one.** Note also the uncomfortable interaction: declaring crypto income may simultaneously *evidence* participation in a restricted activity: a point only a **lawyer** can advise on.

**Practical guidance the AI should give:** route the person to a qualified Egyptian accountant **and** lawyer; if they choose to declare, the conservative default is to treat realised gains as fully taxable commercial income under the ordinary brackets and to keep complete records: while understanding the legal exposure of the underlying activity.
- **Which category, if any**: commercial, non-commercial, "other": applies is unsettled.
- **No confirmed rate** for crypto specifically.
- **Cost basis, FX conversion (USD/USDT → EGP), and timing** of any gain are undefined for tax purposes.
- **Losses**: whether deductible or carried forward: undefined.
- **Mining, staking, airdrops, NFTs, DeFi yield, P2P**: no specific treatment; arguably even more exposed on the legal side.
- **Interaction with the restriction itself**: whether and how one can declare income from a restricted activity is a legal question, not just a tax one.
- **Enforcement reality vs. the letter of the law**: these can diverge, and this skill does not assess prosecution likelihood. A lawyer must.
**Correct response shape:**
- Lead with the legal status: crypto dealing is **restricted/unlicensed** under CBE Law 194/2020 (Art. 206); no general CBE licence exists; CBE has warned the public repeatedly; a fatwa deems it haram.
- State there is **no specific crypto tax law and no clear ETA guidance**: so no definitive tax answer exists.
- Flag the **legal risk** (possible imprisonment/fines) and **no legal recourse** if funds are lost.
- Recommend a qualified Egyptian **lawyer and accountant** before doing anything.
- Do **not** quote a tax rate as if settled.
**Correct response shape:**
- Acknowledge the situation without endorsing the activity.
- Explain there is **no settled crypto tax rule**; *if* they choose to declare, the **conservative** default is to treat the realised gain as taxable commercial income under the ordinary personal income-tax brackets (point them to `eg-income-tax` for the current bracket table): **clearly labelled as one uncertain interpretation, not the law.**
- Stress that declaring may also surface the **legal-status issue**: a lawyer must advise.
- Hand off to a credentialed Egyptian professional. **No firm number.**
**Correct response shape:**
- Direct, unambiguous: operating a crypto platform/brokerage **without a CBE licence is prohibited** under Law 194/2020, and such licences are **not generally granted**: so this is **effectively not permitted** and carries **penalties (imprisonment and fines)**.
- This is a **legal-prohibition** answer, not a tax-planning one. Do **not** offer structuring or tax-optimisation advice for a restricted activity.
- Refer to a qualified Egyptian lawyer.
- **Escalation triggers**: - The user has real crypto gains and wants to file (accountant **+** lawyer). - The user is considering any crypto **business** in Egypt (lawyer first). - Any question of **enforcement risk, prosecution, or legality** of a specific plan (lawyer: outside this skill's competence). - Cross-border, FX, capital-controls, or AML/CTF angles arise. - The user wants certainty on a **rate, basis, or filing line**: there is none; escalate rather than fabricate.
- **AI prohibitions**: The AI must **NEVER**: - **Never present crypto dealing as legal, permitted, or safe in Egypt.** It is restricted/unlicensed under CBE Law 194/2020 and carries real legal risk. - **Never assert a definitive crypto tax rate or filing treatment** for Egypt: none is settled; saying "you pay X%" is wrong and harmful. - **Never encourage** dealing in, promoting, or operating crypto in Egypt, or offer structuring/tax-optimisation advice for a restricted activity. - **Never imply the fatwa is the binding law** (the statute is): or that the *absence* of a tax rule means crypto gains are tax-free or risk-free. - **Never let the user rely on this skill alone** for a real decision: always route to a qualified Egyptian lawyer and accountant. - **Never claim Egypt has no recourse problem solved, or that funds are protected**: the CBE warns there is no legal recourse for losses.

## Deadlines and filing

Individuals file the annual return before 1 April of the following year, and the steps are in `eg-income-tax`. No crypto line exists on any form read. A person starting an activity notifies ETA within 30 days.

## Penalties and interest

Fines and the delay charge are in `eg-income-tax`. Penalties under banking law are not stated here; see Sources.

## Cross-border points

A foreign exchange does not take income out of the charge. Under Law 91 art. 6 and art. 32 item 3 (Law 53/2014) a resident pays on income realised abroad if Egypt is the centre of the activity. Art. 3 defines Egyptian-source income. Foreign-exchange and capital-control rules are out of scope. Moving funds across the border goes to the lawyer.

## Two worked examples that recompute

**Case 1. Trader treated as active, net gain EGP 300,000.** 1,500 + 2,250 + 26,000 + 22.5% on 100,000 = 52,250, after the legal check.

```oa-check
name: Active trader, net gain 300,000
inputs:
  gain: 300000
steps:
  - tax: 1500 + 2250 + 26000 + (gain - 200000) * 0.225
expected:
  tax: 52250.00
```

**Case 2. Decision: which table row.** Gains of 600,000 keep the 0% band and pay 124,750. Gains of 610,000 lose it and pay 131,250. So 10,000 more gain costs 6,500 more tax. Treatment of each row is the ordinary table, not a crypto rule.

```oa-check
name: Row step at 600,000
inputs:
  low: 600000
  high: 610000
steps:
  - tax_low: 1500 + 2250 + 26000 + 45000 + (low - 400000) * 0.25
  - tax_high: 5500 + 2250 + 26000 + 45000 + (high - 400000) * 0.25
  - step_cost: tax_high - tax_low
expected:
  tax_low: 124750.00
  tax_high: 131250.00
  step_cost: 6500.00
```

Responses by question:
- "Is Bitcoin legal, how is it taxed?" Lawyer first; no crypto tax rule published; ordinary table if the income is caught.
- "I profited on a foreign exchange." One reading, labelled as such, then accountant and lawyer. No firm figure without records.
- "Can I run an exchange?" Lawyer only. No structuring or tax planning for it.

## Ask the client first

1. Resident? 2. What activity, how often, through which platform? 3. Realised gains in EGP for 2026. 4. Records of cost? 5. Other income, to pick the table row. 6. Has a lawyer advised on permission?

Hand over to a lawyer and an accountant for any real filing. Never encourage crypto dealing and never say funds are protected.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 91 of 2005: arts. 3, 6, 19, 32 (OCR) | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-01 |
| Law 53 of 2014, arts. 6 and 32 as replaced | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf | 2026-11-01 |
| Law 7 of 2024 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf | 2026-11-01 |
| Law 151 of 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-01 |
| Central Bank of Egypt banking-laws index (lists Law 194 of 2020; the PDF refused both fetch and archive, text unread) | https://www.cbe.org.eg/ar/laws-regulations/laws/banking-laws | 2026-11-01 |

Not yet confirmed: Law 194 of 2020 art. 206 (prior Central Bank approval for issuing, trading, promoting or running crypto platforms), its penalties, whether any licence was ever granted, and the Central Bank's public warnings: all in the old skill, none opened today. The 2018 Dar al-Ifta fatwa (a religious opinion, not a statute). Any ETA statement on crypto. The grep of tax laws used OCR text, so a spelling variant could escape it.

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
