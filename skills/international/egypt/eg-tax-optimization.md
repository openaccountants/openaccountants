---
name: eg-tax-optimization
description: Use this skill whenever asked about legitimate tax optimization, tax planning, or how to legally reduce tax for self-employed people, freelancers, professionals, sole proprietors, and small businesses in Egypt. Trigger on phrases like "reduce tax Egypt", "save tax freelancer Egypt", "simplified vs general Egypt", "Egypt tax planning", "SME regime worth it Egypt", "lower my tax bill Egypt", "is the simplified regime cheaper", "تخطيط ضريبي مصر", "تقليل الضرائب مصر", "النظام المبسط أم العام", "هل النظام المبسط أوفر", "توفير ضرائب". Covers the choice between the turnover-based simplified SME regime (Law No. 6 of 2025) and the general progressive income-tax system, the break-even logic, e-invoicing as a deductibility lever, VAT threshold management, and the Law No. 5 of 2025 dispute-settlement / amnesty facilities. LEGAL planning only — never tax evasion. AI replies in the user's language (English or Arabic).
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

# EG Tax Optimization

## Egypt — Legitimate Tax Optimization for the Self-Employed

This skill helps a self-employed person, freelancer, professional (صاحب مهنة حرة), or small business owner in Egypt **legally minimise** their tax burden for tax year **2026**. The single biggest lever in Egypt today is the **choice of regime**: the turnover-based **integrated simplified system** under **Law No. 6 of 2025** versus the **general progressive income-tax system**. For many small businesses the simplified regime is dramatically cheaper because it taxes *turnover* at under 1.5% instead of taxing *profit* at rates up to 27.5%.

This is **tax optimization** (legal arrangement of affairs), not **tax evasion** (concealment, under-reporting, fake invoices). The line is non-negotiable — see **PROHIBITIONS**.

> Respond in the user's language. If the user writes in Arabic, reply in Arabic and keep native terms: رقم الأعمال (turnover), صافي الربح (net profit), النظام المبسط (simplified regime), النظام العام (general system), الفاتورة الإلكترونية (e-invoice), مصلحة الضرائب المصرية / ETA (Egyptian Tax Authority).

> **Cross-reference.** This skill assumes the mechanics are covered elsewhere: regime detail → `eg-sme-tax`; progressive computation, brackets, allowable deductions and the personal/insurance reliefs → `eg-income-tax`; bookkeeping and e-invoicing → `eg-bookkeeping`; VAT → `egypt-vat`. Load those for the actual computation; this skill is the **decision and planning layer**.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Egypt (EG) |
| Scope | **Legal tax planning / optimization only** (no evasion) |
| Currency | Egyptian Pound (EGP) |
| Key levers | (1) Simplified SME regime vs general system; (2) e-invoicing to preserve cost & input-VAT deductibility; (3) VAT threshold management; (4) legitimate deductions + insurance/pension relief; (5) Law 5/2025 amnesty / dispute settlement |
| Authority | Egyptian Tax Authority — مصلحة الضرائب المصرية (ETA), eta.gov.eg |
| Quality tier | **Research-verified — pending sign-off by an Egyptian accountant** |
| Version | 1.0 |

### Conservative defaults

- **Assume the general system unless eligibility for the simplified regime is confirmed.** Quote the simplified regime as an *option to evaluate*, not as the default.
- **Never assert a saving without numbers.** Always show the side-by-side computation (turnover × simplified rate vs profit × progressive bracket) before recommending.
- **Treat the 5-year lock-in as binding.** Electing the simplified regime under Law 6/2025 cannot be reversed for five years from the day after the request is submitted. Flag this prominently before recommending the election.
- **Flag "verify" on any figure used for a filing.** Rates, bands, thresholds and deadlines below are research-verified against Big-4 / ETA sources but must be confirmed against the live ETA position by a qualified Egyptian accountant before action.
- When two readings are possible, choose the one that keeps the taxpayer compliant and audit-safe, even if marginally more tax is paid.

## 2. Simplified SME regime vs the general system — the core decision

### 2.1 The two regimes

- **General progressive income-tax system** — Tax is charged on **net profit** (صافي الربح) = revenue − allowable costs, after the EGP 20,000 personal exemption, using the 2025/2026 brackets (verify).  _(verify)_

**General progressive income-tax brackets (Annual taxable income, EGP)**  _(verify — full detail in eg-income-tax)_

| Annual taxable income (EGP) | Marginal rate |
| --- | --- |
| 1 – 40,000 | 0% |
| 40,000 – 55,000 | 10% |
| 55,000 – 70,000 | 15% |
| 70,000 – 200,000 | 20% |
| 200,000 – 400,000 | 22.5% |
| 400,000 – 1,200,000 | 25% |
| Over 1,200,000 | 27.5% |

(Brackets are progressive — each rate applies only to the slice of income within that band. Full detail and the bracket-collapse rules for higher incomes live in `eg-income-tax`. **Verify** the exact bands for TY2026.)

- **Simplified / integrated regime (Law No. 6 of 2025)** — Tax is charged on **turnover** (رقم الأعمال), not profit, at a flat band rate. Eligibility: annual turnover **≤ EGP 20 million**. Verified turnover bands (verify).  _(Law No. 6 of 2025 (verify))_

**Simplified regime turnover bands**  _(Law No. 6 of 2025 (verify))_

| Annual turnover (EGP) | Tax on turnover |
| --- | --- |
| Below 500,000 | **0.4%** |
| 500,000 – 2,000,000 | **0.5%** |
| 2,000,000 – 3,000,000 | **0.75%** |
| 3,000,000 – 10,000,000 | **1.0%** |
| 10,000,000 – 20,000,000 | **1.5%** |

- **Simplified regime exemptions** — Within the simplified regime the law also grants exemptions that matter for planning (verify): exemption from stamp tax (ضريبة الدمغة) and registration/documentation fees; exemption from capital gains tax on the sale of machinery, equipment and fixed assets; exemption from withholding tax on dividend distributions; exemption from the advance-payment / local withholding system; simplified compliance: quarterly (not monthly) VAT returns where VAT-registered.  _(Law No. 6 of 2025 (verify))_

> Note: the simplified rate replaces the profit-based **income tax**. It does **not** remove a separate VAT obligation if the taxpayer is over the VAT registration threshold — VAT still applies (see Section 4).

### 2.2 The break-even logic

Because the simplified regime taxes turnover and the general system taxes profit, the decision hinges on the taxpayer's **profit margin** (صافي الربح ÷ رقم الأعمال).

- **High-margin, low-cost businesses** (e.g. a freelance developer or consultant with few deductible costs) → profit ≈ turnover, so the general system taxes nearly the whole amount at rates up to 27.5%. The simplified regime at <1.5% is **dramatically cheaper**.
- **Low-margin businesses** (e.g. trading/retail reselling goods with thin margins) → a turnover tax can bite, because even a small % of a large turnover may exceed the income tax on a thin profit. Run the numbers.

- **Break-even rule of thumb** — Rough break-even rule of thumb: compare `turnover × simplified_rate` against `progressive_tax(profit)`. The simplified regime wins whenever the effective general-system rate on profit exceeds the simplified rate on turnover. For a high-margin freelancer the simplified regime almost always wins by a wide margin.

### 2.3 Decision table

**Decision table**

| Situation | Likely better regime | Why |
| --- | --- | --- |
| Freelancer/consultant, few costs, profit margin > ~40%, turnover ≤ 20m | **Simplified** | Turnover tax <1.5% beats up to 27.5% on near-full profit |
| Low-margin trader/retailer (margin < ~10%) | **Often general** | Turnover tax can exceed income tax on a thin profit — model it |
| Turnover above EGP 20m | **General (only option)** | Above simplified eligibility ceiling |
| Heavy genuine deductible costs, modest profit | **Model both** | Deductions shrink the general-system base; compare carefully |
| Wants flexibility to change soon | **General** | Simplified locks in for **5 years** |
| Poor documentation / can't issue e-invoices | **Model both, fix docs first** | Without e-invoices, costs are disallowed on the general system, pushing toward simplified |

> **Always produce the two numbers.** Do not recommend a regime in the abstract.

## 3. e-invoicing compliance as a deductibility lever

- **E-invoice deductibility requirement** — On the general system, the value of deductions depends entirely on documentation. Since 1 July 2023, for taxpayers registered on the e-invoice system, only electronic invoices (الفاتورة الإلكترونية) count as valid evidence of deductible costs and expenses for income-tax purposes, and only e-invoices/e-receipts support input-VAT deduction or refund (verify).  _(verify — effective 1 July 2023)_

- **A cost without a valid e-invoice is effectively a non-deduction.** It raises taxable profit and the tax bill. Optimising the general system therefore *starts* with getting suppliers to issue compliant e-invoices and issuing your own.
- **Input VAT on paper invoices is lost** — non-electronic invoices are not accepted for VAT input credit or refund.
- The **simplified regime** is more forgiving on cost documentation (tax is on turnover, not profit), but e-invoicing/e-receipt integration is itself an **eligibility condition** of Law 6/2025, plus timely return filing. So e-invoicing is mandatory either way; on the general system it is also the gate to your deductions.

**Optimization actions:** register on the ETA e-invoice/e-receipt system; require e-invoices from every supplier before paying; reconcile e-invoices to the books monthly; never rely on paper or PDF invoices for a deduction.

## 4. VAT threshold management + amnesty facilities

### 4.1 VAT registration threshold

- **Standard VAT rate** — 14%  _(verify)_
- **Mandatory VAT (and e-invoicing) registration threshold** — Reduced from EGP 500,000 to EGP 250,000 of annual turnover under Resolution No. 281 of 2025 (verify). Businesses whose 2025 gross revenue exceeded EGP 250,000 must register with ETA before 31 March 2026 or face penalties (reported as an EGP 20,000 fine plus EGP 1,000/day — verify).  _(Resolution No. 281 of 2025 (verify))_
- **Turnover definition for threshold** — "Turnover" for the threshold is gross revenue before costs — a business with EGP 260,000 revenue and EGP 20,000 net profit is still in scope.

- **Do not artificially fragment or suppress turnover to stay under the threshold** — that is evasion, not planning (see PROHIBITIONS). Splitting one business into sham entities is illegal.
- Legitimate timing: a genuinely seasonal or growing business should **monitor cumulative turnover** and register on time to avoid penalties; voluntary early registration can be sensible where customers are themselves VAT-registered (your VAT is recoverable to them) and where you want input-VAT recovery on your own costs.
- On the simplified regime, VAT registrants benefit from **quarterly** filing — a real compliance-cost saving.

### 4.2 Law No. 5 of 2025 — dispute settlement / amnesty

- **Law No. 5 of 2025 facilities** — Law No. 5 of 2025 (in force from 13 February 2025) is a one-off facilitation window worth checking for any taxpayer with a backlog (verify): **Penalty/interest waiver:** up to a 100% waiver of penalties, late fees and additional tax where the principal tax is paid promptly. **Non-filers (2020 → 13 Feb 2025):** relief from penalties if outstanding or amended returns are filed within six months of 13 February 2025. **Unregistered taxpayers:** no tax obligations imposed for periods before 13 February 2025 (income tax, VAT, stamp tax, development fee) if they register within three months of that date. **Old disputes (pre-2020):** fast-track settlement — pay the principal within set windows and have delay fines / additional tax forfeited.  _(Law No. 5 of 2025 (verify))_

> **Timing caveat — verify the windows have not closed.** Today is **May 2026**. The six-month and three-month windows above ran from 13 February 2025 and have **likely expired**. Treat Law 5/2025 as relevant mainly for *already-initiated* settlements or any extension/successor facility. **Confirm current availability with ETA / a qualified accountant before relying on it.**

## 5. Worked examples

> All numbers are **illustrative** and use the verified 2026 rates above. Confirm bands and the taxpayer's facts before filing. Computations are rounded.

### Persona A — High-margin freelance developer (the classic win)

- Turnover: **EGP 1,800,000**; deductible costs ≈ EGP 200,000; net profit ≈ **EGP 1,600,000**.
- **General system:** progressive tax on EGP 1,600,000 (after EGP 20,000 exemption) lands deep in the upper brackets — effective tax broadly in the region of **EGP 380,000–400,000** (≈ 24% effective; verify with the bracket calc in `eg-income-tax`).
- **Simplified system:** turnover EGP 1,800,000 falls in the 0.5% band → **EGP 9,000**.
- **Outcome:** simplified regime saves roughly **EGP 370,000+**. Overwhelmingly favours simplified. Flag the 5-year lock-in.

### Persona B — Low-margin online trader (where it can flip)

- Turnover: **EGP 9,000,000**; cost of goods + costs ≈ EGP 8,400,000; net profit ≈ **EGP 600,000**.
- **Simplified system:** EGP 9,000,000 in the 1.0% band → **EGP 90,000**.
- **General system:** tax on EGP 600,000 profit ≈ **EGP 90,000–100,000** (verify).
- **Outcome:** roughly a wash — model carefully. If margins are thinner (say profit EGP 350,000), the **general system becomes cheaper** because 1% of EGP 9m exceeds the income tax on a small profit. Documentation (e-invoices for the EGP 8.4m of costs) is critical to make the general system viable.

### Persona C — New consultant near the VAT threshold

- Turnover: **EGP 240,000** (first year), high margin, almost no costs.
- Below the **EGP 250,000** VAT registration threshold — not yet required to register for VAT (verify), but e-invoicing/registration obligations should be checked.
- Income tax: small profit, much of it sheltered by the EGP 20,000 exemption and low brackets → modest tax either way.
- **Planning:** monitor cumulative turnover monthly; register for VAT and e-invoicing **before** crossing EGP 250,000 to avoid the late-registration penalties. If growth is expected, evaluate the simplified election early — but weigh the 5-year lock-in.

### Persona D — Established professional with a pre-2020 dispute

- Has an open ETA dispute for periods before 2020 and unfiled amended returns.
- **Planning:** check whether a Law 5/2025 settlement (or any successor facility) is **still open**; if a settlement is already in train, paying the principal promptly can forfeit delay fines and additional tax (verify the deadline has not lapsed). Going forward, evaluate simplified vs general for current years separately.

## 6. Risks & red flags

- **5-year lock-in (simplified regime)** — The Law 6/2025 election cannot be withdrawn for five years. A business expecting to scale past EGP 20m, change activity, or want profit-based treatment soon should think twice.  _(Law No. 6 of 2025 (verify))_
- **Exceeding the EGP 20m ceiling** — Going over by up to 20% keeps the 1.5% rate for one further year; exceeding the 20% buffer revokes all benefits the following year (verify). Plan growth around this.  _(verify)_
- **e-invoice non-compliance disallows costs** — On the general system, missing/paper invoices = lost deductions and lost input VAT. This is the most common, avoidable over-payment of tax.
- **Misuse of the simplified regime = audit risk** — Splitting one business into multiple sham entities to stay under EGP 20m, or to access the low rate multiple times, is abuse and exposes the taxpayer to reassessment and penalties.
- **Suppressing turnover to dodge the VAT threshold** — Suppressing turnover to dodge the VAT threshold is evasion, not planning.
- **Late VAT/e-invoice registration penalty** — Late VAT/e-invoice registration after EGP 250,000 triggers fixed and daily penalties (verify).  _(verify)_
- **Stale amnesty windows** — Law 5/2025 deadlines ran from Feb 2025 and are likely closed by May 2026 — do not promise relief without confirming it is live.

All figures are "verify". Rates, bands and thresholds change; this is research-verified, not a substitute for an Egyptian accountant.

## 7. Reference

Research-verified against the following (accessed May 2026; **verify** against the live ETA position before any filing):

- Egyptian Tax Authority (ETA) — مصلحة الضرائب المصرية — eta.gov.eg
- **Law No. 6 of 2025** — integrated simplified tax regime for enterprises with turnover ≤ EGP 20m; turnover bands 0.4% / 0.5% / 0.75% / 1.0% / 1.5%; stamp/CGT/dividend/advance-payment exemptions; 5-year commitment; e-invoicing & timely-filing eligibility conditions. (EY Global tax alert; Andersen Egypt; Amereller; Wealth Advisory; HLUL Legal.)
- **Law No. 5 of 2025** — tax reconciliation / dispute settlement; penalty & interest waivers; non-filer and unregistered-taxpayer relief windows from 13 Feb 2025. (EY Global Tax News; Lexology/Amereller; Andersen Egypt; Orbitax.)
- **Personal income tax brackets 2025/2026** (0% to 27.5%; EGP 20,000 exemption). (PwC Worldwide Tax Summaries — Egypt, Individual.)
- **e-invoicing & deductibility** — from 1 July 2023 only e-invoices evidence deductible costs for income tax; e-invoices/e-receipts required for input-VAT credit/refund. (Bloomberg Tax; PwC; KPMG.)
- **VAT** — standard rate 14%; mandatory registration / e-invoicing threshold reduced to EGP 250,000 under Resolution No. 281 of 2025, register by 31 March 2026. (PwC; Fonoa; DataValue; VATupdate.)
- Cross-skills: `eg-sme-tax`, `eg-income-tax`, `eg-bookkeeping`, `egypt-vat`.

## PROHIBITIONS

- **Prohibited actions** — This skill performs **legal tax optimization only**. It must **never**: - Advise, design, or assist any form of **tax evasion** (التهرب الضريبي): under-reporting turnover or income, omitting sales, keeping two sets of books, or claiming costs that were not incurred. - Suggest **fake, inflated, or backdated invoices**, or any document not reflecting a real transaction. - Recommend **artificially fragmenting one business** into sham entities to stay under the EGP 20m simplified ceiling or the EGP 250,000 VAT threshold, or to multiply low-rate access. - Recommend **suppressing or splitting turnover** to avoid VAT registration. - Recommend **concealing assets, foreign income, or related-party transactions**, or misclassifying private spending as business cost. - Encourage **late or non-filing** to "wait for the next amnesty." - Present any planning as guaranteed, or substitute for a credentialed reviewer. If a user asks for any of the above, **refuse** and redirect to a legal, documented alternative (e.g. choosing the genuinely cheaper regime, improving e-invoice documentation, timely registration, or a legitimate settlement).

## Disclaimer

This skill is **research-verified, pending sign-off by a qualified Egyptian accountant or registered tax adviser**. It provides general information on **legal tax planning** for self-employed people in Egypt for tax year 2026 and is **not** tax, legal, or accounting advice. Rates, bands, thresholds, exemptions, and deadlines (all marked "verify") change frequently and must be confirmed against the current position of the Egyptian Tax Authority (مصلحة الضرائب المصرية, eta.gov.eg) before any decision or filing. Choosing a tax regime, electing the simplified system (a 5-year commitment), and any dispute settlement have lasting consequences and should be reviewed with a qualified Egyptian accountant. Part of the open-source tax skills at **openaccountants.com**.

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
