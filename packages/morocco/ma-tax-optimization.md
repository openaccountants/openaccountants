---
name: ma-tax-optimization
description: Use this skill whenever asked about legitimate (legal) tax optimization for a self-employed person, freelancer, or sole trader in Morocco — that is, choosing the most efficient tax regime and using lawful levers to reduce the tax bill without evasion. Trigger on phrases like 'reduce tax Morocco', 'optimiser mes impôts Maroc', 'auto-entrepreneur vs CPU', 'tax planning Morocco freelancer', 'quel régime fiscal Maroc', 'lower my tax legally Morocco', 'best status freelance Maroc', 'كيف أقلل الضريبة'. Covers the choice between auto-entrepreneur (0.5% / 1% of turnover), the Contribution Professionnelle Unique (CPU), and the Résultat Net Simplifié / Réel (RNS / RNR, net profit on the IR scale to 37%), with break-even logic by turnover and margin; the auto-entrepreneur single-client 80,000 MAD anti-disguised-salary rule and disguised-employment risk; the cotisation minimale and new-business exemption; VAT registration threshold management; and export / Casablanca Finance City incentives. Reply in the user's language (English, French, or Moroccan Arabic / Darija). LEGAL planning only — never advise evasion. Cross-reference ma-auto-entrepreneur, ma-cpu, ma-income-tax.
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

# MA Tax Optimization

## Morocco — Legitimate Tax Optimization for the Self-Employed (Optimisation Fiscale Légale)

This skill helps a self-employed person in Morocco — a freelancer, sole trader, or independent professional (**travailleur indépendant**) — pay **the least tax the law allows**, by choosing the right regime and using lawful levers. It is **planning, not evasion**. Every technique here is grounded in the **Code Général des Impôts (CGI)** and the **Loi de Finances 2026**, administered by the **Direction Générale des Impôts (DGI)**.

The decisive idea: a self-employed person in Morocco is taxed under the **Impôt sur le Revenu (IR)**, but *how* the taxable base is built depends entirely on the **régime fiscal** chosen. The same MAD 300,000 of turnover can produce wildly different tax depending on whether it is taxed as a flat percentage of turnover (auto-entrepreneur), turnover × a profession coefficient (CPU), or actual net profit on the progressive IR scale (RNS / RNR). Optimization is mostly the art of matching the regime to the **turnover** and the **margin**.

This skill replies in the user's language. Moroccan users mix English, French, and Darija — keep the native terms (auto-entrepreneur, CPU, RNS, RNR, IR, TVA, CNSS, cotisation minimale, DGI) and explain them in the user's chosen language.

> **Cross-references.** For the mechanics of each regime, defer to the dedicated skills: **ma-auto-entrepreneur** (the 0.5% / 1% turnover status and its CNSS/AMO cover), **ma-cpu** (the Contribution Professionnelle Unique), and **ma-income-tax** (the IR scale, RNS/RNR net-profit regimes, and deductions). This skill sits *above* them and helps choose between them.

## 1. Quick Reference

**Quick Reference Table**

| Item | Value (2026) |
| --- | --- |
| **Scope** | Legal tax planning for self-employed individuals (IR taxpayers) |
| **Authority** | Direction Générale des Impôts (DGI), Ministère de l'Économie et des Finances |
| **Currency** | Moroccan Dirham (MAD / DH) |
| **Legal basis** | Code Général des Impôts (CGI); Loi de Finances 2026; Loi n° 114-13 (auto-entrepreneur) |
| **IR scale top rate** | 37% (income above MAD 180,000/year) |
| **IR exempt band** | First MAD 40,000/year taxed at 0% |
| **Auto-entrepreneur IR** | 0.5% of turnover (commerce/industry/craft); 1% (services) — liberatory |
| **Auto-entrepreneur ceilings** | MAD 500,000 (commerce/industry/craft); MAD 200,000 (services) |
| **CPU** | Turnover × profession coefficient, then 10% liberatory IR (+ supplementary droit) |
| **CPU ceilings** | MAD 2,000,000 (commerce/industry); MAD 500,000 (services) — *verify* |
| **RNS / RNR** | Actual net profit on the progressive IR scale (up to 37%) |
| **Cotisation minimale (CM)** | 0.25% standard; 4% for professions libérales — *verify rate for your activity* |
| **New-business CM exemption** | First 36 months of activity (per CGI Art. 144) |
| **Single-client AE rule** | Excess over MAD 80,000/year from one client → 30% withholding (services) |
| **Quality tier** | **Research-verified — pending sign-off by a Moroccan expert-comptable** |
| **Version** | 1.0 |

### Conservative defaults

When the facts are incomplete, default to the **safer, more conservative** answer and tell the user to verify:

- **Default to the regime that survives audit, not the one with the lowest headline number.** A regime that minimizes tax but exposes the client to requalification (e.g. disguised employment) is not optimization — it is risk.
- **Treat the 80,000 MAD single-client situation as a red flag** until the relationship is shown to be genuinely independent.
- **Assume VAT applies** to services above the relevant threshold unless an exclusion or exemption is clearly established.
- **Assume the standard cotisation minimale applies** once the new-business window closes, unless a reduced rate or exemption is confirmed.
- Where a figure is marked **"verify"**, state it as provisional and tell the user to confirm with the DGI or an **expert-comptable** before relying on it.

## 2. Choosing the Regime (the Core Optimization Decision)

A self-employed Moroccan has, broadly, three families of regime. The first lever of optimization is picking the right one.

### 2.1 The three options at a glance

**The three options at a glance**

| Regime | Tax base | Headline rate | Best when | Key limit |
| --- | --- | --- | --- | --- |
| **Auto-entrepreneur (AE)** | Turnover collected | 0.5% (goods) / 1% (services), liberatory | Low costs, high margin, turnover under the ceiling | MAD 500k / 200k ceilings; single-client 80k rule |
| **CPU** (Contribution Professionnelle Unique) | Turnover × profession coefficient | 10% liberatory on the coefficiented base (+ droit complémentaire) | Modest turnover above AE ceilings, no full accounts wanted | MAD 2,000,000 / 500,000 ceilings *(verify)* |
| **RNS / RNR** (net-profit) | Actual net profit (revenue − deductible expenses) | Progressive IR scale, 0%–37% | High real costs / thin margin, or turnover above CPU ceilings | Full bookkeeping; cotisation minimale floor |

### 2.1 The three options at a glance

> RNS (**Résultat Net Simplifié**) and RNR (**Résultat Net Réel**) both tax *real net profit* on the IR scale; RNR requires fuller accounting. See **ma-income-tax**.

### 2.2 The IR scale (the engine behind CPU and RNS/RNR)

**The IR scale**  _(Loi de Finances 2026)_

| Annual taxable income (MAD) | Rate |
| --- | --- |
| 0 – 40,000 | 0% |
| 40,001 – 60,000 | 10% |
| 60,001 – 80,000 | 20% |
| 80,001 – 100,000 | 30% |
| 100,001 – 180,000 | 34% |
| above 180,000 | 37% |

### 2.2 The IR scale (the engine behind CPU and RNS/RNR)

(Loi de Finances 2026; unchanged from 2025. *Verify the bracket edges before filing.*)

### 2.3 Break-even logic — turnover and margin are everything

Two variables drive the choice: **turnover (CA)** and **net margin** (profit ÷ turnover).

**Auto-entrepreneur is unbeatable when margin is high and costs are low.** Because AE taxes *turnover* — not profit — at just 0.5% / 1%, a freelancer with almost no deductible costs (a typical service freelancer: laptop, internet, software) pays a tiny effective rate. On MAD 200,000 of services, AE IR is only **MAD 2,000** (1%). No net-profit regime can match that, because even after deductions the IR scale would tax most of that income at 30–37%.

**Net-profit (RNS/RNR) wins when margin is thin.** If a sole trader buys and resells goods at a 10% margin, AE taxes the whole turnover, ignoring the 90% that went to suppliers. Here the net-profit regime — which deducts the cost of goods — produces a far smaller base. The crossover happens when **real deductible costs are large enough that net profit × IR-scale rate < turnover × AE rate**.

**CPU sits in the middle.** It is the natural home for someone who has outgrown the AE ceilings but still has modest turnover and does not want full RNR accounting. The coefficient is meant to *approximate* a realistic margin for the profession, then 10% is applied.

**A practical decision rule:**

1. **Turnover within AE ceiling (200k services / 500k goods) AND high margin AND not dependent on a single client?** → **Auto-entrepreneur** is almost always the lowest legal tax.
2. **Turnover above the AE ceiling but within the CPU ceiling, margin roughly in line with the profession coefficient?** → **CPU**.
3. **Thin margin (high real costs), OR turnover above CPU ceilings, OR you want to deduct genuine business expenses (rent, salaries, equipment)?** → **RNS / RNR** on the IR scale.

> **Margin sensitivity check.** Always recompute. AE's appeal collapses as margin falls: at a 20% net margin, 1% of turnover equals 5% of profit — cheap. At a 5% margin, 1% of turnover equals 20% of profit — and a net-profit regime that deducts real costs may now beat it. Run the actual numbers for the client's CA and margin before recommending.

## 3. The 80,000 MAD Single-Client Rule & Disguised-Employment Risk

This is the single most important compliance trap in Moroccan freelance optimization — and the one where naive "optimization" tips into illegality.

### 3.1 What the rule says

- **80,000 MAD single-client withholding rule** — For an auto-entrepreneur providing services, the portion of annual turnover billed to the same client that exceeds MAD 80,000 is no longer taxed at the favourable 1% liberatory rate. Instead, the client is required to apply a 30% withholding on the excess. The 1% rate continues to apply only up to MAD 80,000 per client.  _(Loi de Finances 2023, in force in 2026)_

### 3.2 Why it exists — the anti-disguised-salary purpose

The rule targets **disguised employment (salariat déguisé)**: companies replacing salaried staff with auto-entrepreneurs to dodge payroll tax, CNSS contributions, and Labour Code obligations. A "freelancer" who works full-time for one employer, under that employer's direction, looks like an employee. The 80,000 MAD threshold plus 30% withholding removes the tax advantage of that arrangement.

### 3.3 How to plan around it — *legitimately*

The lawful response is **not** to hide the relationship or split invoices across shell entities — that is evasion and is prohibited (see PROHIBITIONS). The legitimate options are:

- **Genuinely diversify the client base.** If the freelancer really serves several clients, no single one breaches 80,000 MAD and the rule simply does not bite. This is the cleanest path and reflects a true independent business.
- **Accept the withholding and move to the right regime.** If income from one client legitimately exceeds 80,000 MAD, the AE status may simply be the wrong tool. Re-run the break-even (Section 2): **CPU** or **RNS/RNR** may now be both lawful and more efficient than AE plus 30% withholding.
- **If the relationship is, in substance, employment, treat it as employment.** The honest answer is sometimes a salaried contract (with CNSS and the IR withholding on wages). Recommending this is good advice, not a failure.

### 3.4 The disguised-employment red flags the DGI looks for

Flag the risk to the client if the arrangement shows:

- A **single dominant client** providing most or all income.
- **Subordination**: fixed hours, the client's premises/equipment, the client's direction and supervision.
- **No real business autonomy**: no other clients, no own tools, no commercial risk, no ability to refuse work.
- **Continuity** mimicking permanent employment.

If several of these are present, **warn the client**: the DGI (and the labour authorities / CNSS) can **requalify** the relationship as employment, with back taxes, social contributions, and penalties. Optimization stops where substance says "employee".

## 4. Cotisation Minimale / New-Business / VAT Levers

Beyond regime choice, three lawful levers move the tax bill.

### 4.1 Cotisation minimale (CM) — the floor under net-profit regimes

- **Cotisation minimale standard rate** — 0.25% percent of turnover (standard rate under RNS/RNR)  _(CGI)_
- **Cotisation minimale professions libérales rate** — 4% percent of turnover (professions libérales — verify for the specific activity)  _(CGI)_

Under **RNS / RNR**, even a low- or no-profit year owes a **cotisation minimale**: a minimum tax computed on **turnover** (plus certain other income), not profit. The **standard rate is 0.25%**; **professions libérales** face a higher rate (reported at **4%** — *verify for the specific activity*). The CM matters for optimization because it sets a *floor*: a net-profit regime never costs less than the CM, so a very-low-margin business should compare AE/CPU against "RNS net-profit tax, but never below the CM".

### 4.2 The new-business exemption — a real, time-limited lever

- **New-business cotisation minimale exemption** — New taxpayers are exempt from the cotisation minimale for the first 36 months of activity.  _(CGI Art. 144)_

This is a genuine planning point: in the early, loss-making or thin-margin years, a net-profit regime can be attractive because the CM floor is switched off. Plan the regime choice with this 36-month window in mind, and note when it expires (the CM floor then re-engages).

### 4.3 VAT (TVA) threshold management

Auto-entrepreneurs operate **outside the scope of VAT (hors champ de la TVA)** while within their ceilings — they charge **no TVA**, which makes them cheaper to non-recoverable clients (consumers, exempt businesses). This is a legitimate competitive and cash-flow advantage.

- **VAT standard rate** — 20% percent
- **VAT reduced rate** — 10% percent (for some services)
- **Optional VAT registration lock-in period** — The option, once taken, is binding for a minimum of 3 consecutive years.

Optimization levers:

- **Staying within the AE ceiling keeps you VAT-free.** Crossing the ceiling (or moving to CPU/RNS) generally brings you **into** VAT: you must register, charge TVA (standard **20%**, reduced **10%** for some services), file VAT returns, and keep accounts — but you also gain the **right to deduct input VAT** on purchases.
- **Optional VAT registration** can pay off when your clients are VAT-registered businesses (they reclaim the TVA you charge) and you carry significant input VAT (equipment, subcontractors). The option, once taken, is binding for a **minimum of 3 consecutive years** — so model it before opting in.
- **Do not artificially suppress turnover** to stay under a threshold (e.g. refusing real work, or pushing income off-book). Declining growth is a business choice; *concealing* turnover is evasion (see PROHIBITIONS).

### 4.4 Export & Casablanca Finance City (brief mention)

These are largely **corporate (IS)** incentives, but relevant when a freelancer considers incorporating:

- **Export activities** benefit from preferential corporate treatment (historically a full IS exemption for the first years, then a reduced rate). A self-employed exporter selling services abroad should ask whether incorporating to access these reliefs is worthwhile — *verify current 2026 terms*.
- **Casablanca Finance City (CFC)** offers strong incentives for eligible companies (a multi-year IS exemption then a reduced **20%** rate, with CM relief in the early years). This is **company-level**, not for a bare sole trader, and eligibility is restrictive. Mention it only as a "consider incorporating" prompt and route the client to a specialist. *Verify all CFC terms against the Loi de Finances 2026.*

## 5. Worked Examples (3 Personas)

> Illustrative only. Figures rounded; confirm bracket edges and rates before filing.

### 5.1 Amine — high-margin solo developer (AE wins)

- **Activity:** freelance software developer, several clients (none above 80k).
- **Turnover:** MAD 180,000 (services). **Real costs:** ~MAD 15,000 (laptop, internet, SaaS) → margin ~92%.
- **Auto-entrepreneur:** 1% × 180,000 = **MAD 1,800** IR (liberatory), no VAT, no accounts. Within the 200,000 services ceiling.
- **RNS comparison:** net profit ≈ 165,000 → IR scale tax would be in the tens of thousands of dirhams. Far worse.
- **Recommendation:** **Auto-entrepreneur.** Keep clients diversified so the 80k single-client rule never bites. Monitor the 200,000 ceiling.

### 5.2 Khadija — single-client consultant (the 80k trap)

- **Activity:** consultant invoicing **one** company MAD 240,000/year.
- **Naive AE view:** "1% = MAD 2,400." **Wrong** — only the first 80,000 enjoys 1%; the **MAD 160,000 excess from the same client** suffers **30% withholding** ≈ **MAD 48,000**. And the 240,000 turnover **exceeds the 200,000 services ceiling**, so AE is not even available beyond it.
- **Disguised-employment risk:** one client, likely subordination → high requalification risk.
- **Recommendation:** **(a)** if genuinely independent, move to **CPU or RNS** and re-run the numbers — likely cheaper than AE-plus-withholding and audit-safe; **(b)** if in substance an employee, advise a **salaried contract**. Do **not** split invoices or interpose entities to dodge the 80k rule.

### 5.3 Younes — low-margin trader (net-profit regime wins)

- **Activity:** buys and resells electronics. **Turnover:** MAD 1,200,000. **Cost of goods + costs:** MAD 1,080,000 → net profit ≈ **MAD 120,000**, margin ~10%.
- **AE:** unavailable — turnover far above the 500,000 goods ceiling.
- **CPU vs RNS:** under **RNS**, tax is on the **MAD 120,000 net profit** on the IR scale (≈ low-to-mid four figures up to the 34% band on the top slice), subject to the **cotisation minimale** floor (0.25% × 1,200,000 = **MAD 3,000**). Compare against the CPU coefficiented base.
- **New-business lever:** in his first 36 months, the **CM is waived**, improving the net-profit option in early years.
- **Recommendation:** a **net-profit regime (RNS/RNR)** that deducts the genuine cost of goods, with CPU as a fallback to model. VAT registration is required at this turnover — use input-VAT deduction on stock.

## 6. Risks & Red Flags

- **Disguised employment (salariat déguisé).** The biggest one. Single dominant client + subordination = requalification risk. See Section 3. Flag it; never facilitate it.
- **Splitting / fragmenting turnover** across several auto-entrepreneurs or fake entities to stay under ceilings or under the 80k rule — **abusive and illegal.**
- **Under-declaring turnover** or keeping income off-book to stay VAT-free or below a ceiling — **evasion**, not optimization.
- **Ceiling breach by stealth.** Exceeding the AE ceilings for **two consecutive years** triggers automatic transition to a higher regime from 1 January of the next year. Plan the transition; do not pretend it isn't happening.
- **Mismatched coefficient (CPU).** Choosing CPU when the real margin is far below the profession coefficient can *cost* tax — CPU is not automatically cheaper.
- **Forgetting the cotisation minimale floor** when modelling a net-profit regime.
- **Optional VAT lock-in.** The 3-year minimum commitment means a bad VAT election is sticky — model it first.
- **Treating "verify" figures as settled.** Bracket edges, ceilings, and reduced CM rates must be confirmed against the **Loi de Finances 2026** and the DGI.

## 7. Reference

**Primary sources (verify before relying):**

- **Code Général des Impôts (CGI)** — IR scale and regimes (Art. 73, 144 cotisation minimale, 40 CPU coefficients, 42 bis–44 auto-entrepreneur), VAT (Art. 88+).
- **Loi de Finances 2026**, Ministère de l'Économie et des Finances.
- **Loi n° 114-13** — auto-entrepreneur status.
- **Direction Générale des Impôts (DGI)** — official guides and the auto-entrepreneur portal (ae.gov.ma); CNSS for social cover.

**Key figures used (2026 — confirm before filing):**

- IR scale: 0% to 40,000; 10%; 20%; 30%; 34%; **37%** above 180,000.
- AE: **0.5%** goods / **1%** services; ceilings **500,000 / 200,000** MAD.
- AE single-client: **30%** withholding on the excess over **80,000** MAD (services).
- CPU: **10%** liberatory on turnover × profession coefficient; ceilings **2,000,000 / 500,000** MAD *(verify)*.
- Cotisation minimale: **0.25%** standard; **4%** professions libérales *(verify)*; **36-month** new-business exemption (CGI Art. 144).
- VAT: standard **20%**, reduced **10%**; optional registration binds **3 years**.

**Cross-references:** ma-auto-entrepreneur · ma-cpu · ma-income-tax

## PROHIBITIONS

- **Prohibited activities** — This skill provides **legal tax optimization only**. It must **never**: - Advise, design, or facilitate **tax evasion** — under-declaring or concealing turnover/income, keeping cash off-book, or falsifying records. - Help structure or disguise an **employment relationship** as freelancing to dodge payroll tax, CNSS, or Labour Code duties (**salariat déguisé**). Where the substance is employment, say so. - Suggest **fragmenting turnover** across multiple auto-entrepreneurs, relatives, or sham entities to stay under ceilings or under the 80,000 MAD single-client rule. - Recommend **artificial invoice-splitting**, backdating, or fictitious deductions. - Present any **abusive arrangement** that fails a substance/economic-reality test as "optimization". - State unverified figures as certain. Mark estimates **"verify"** and route the user to the DGI or an expert-comptable. When a request crosses into evasion or disguised employment, **decline the unlawful part, explain why, and offer the lawful alternative.**

## Disclaimer

This skill is **research-verified** against public DGI guidance, the Loi de Finances 2026, and reputable professional commentary, but is **pending sign-off by a Moroccan expert-comptable** (chartered accountant). It is general information for legitimate tax planning, **not** personalised tax advice. Tax rates, thresholds, coefficients, and rules change and may have exceptions specific to your activity or region. Before acting, confirm the current position with the **Direction Générale des Impôts (DGI)** or a qualified Moroccan **expert-comptable**. Figures marked "verify" are provisional.

Part of **OpenAccountants** — open-source tax skills for the self-employed. openaccountants.com

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
