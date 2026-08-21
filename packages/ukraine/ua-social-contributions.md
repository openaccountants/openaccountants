---
name: ua-social-contributions
description: "Ukrainian Unified Social Contribution (ЄСВ / USC) for self-employed people (FOP and independent professionals): the 22% rate, minimum and maximum monthly base, quarterly payment, the obligation to pay even at zero income, exemptions, and 2026 reporting changes."
version: 1.0
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Social Contributions

## Ukraine Unified Social Contribution (Єдиний соціальний внесок / ЄСВ / USC) — Self-Employed Skill v1.0

The Unified Social Contribution (ЄСВ) is Ukraine's single mandatory social-security charge. It replaced four separate state social funds (pension, unemployment, temporary disability/sickness, and accident-at-work insurance) with one consolidated contribution. For self-employed people it is **separate from and on top of** income tax / the single tax — see the companion skill `ua-single-tax` for the simplified-system tax itself.

> **Wartime note.** Figures below are pinned at their **1 January 2026** values. Ukraine is under martial law; the temporary wartime right to skip ЄСВ that existed in 2022–2024 was **abolished from 1 January 2025**. Several values depend on the statutory minimum wage (₴8,647 from 1 Jan 2026) — always **verify the current value** before relying on a number.

## 1. Quick Reference

**Quick Reference Table**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Ukraine (UA) |
| Contribution | Єдиний соціальний внесок (ЄСВ / Unified Social Contribution / USC) |
| Rate | **22%** |
| Minimum monthly base | 1 × minimum wage = **₴8,647** → min contribution **₴1,902.34/month** |
| Maximum monthly base | 20 × minimum wage = **₴172,940** → max contribution **₴38,046.80/month** *(verify — see §3)* |
| Currency | UAH (₴) |
| Legislation | Law of Ukraine "On collection and accounting of the unified social contribution" (No. 2464-VI); State Budget Law for 2026 (03 Dec 2025) sets the year's minimum wage |
| Authority | Державна податкова служба (ДПС / State Tax Service) collects; Pension Fund of Ukraine (Пенсійний фонд) administers records |
| Portal | Електронний кабінет платника (cabinet.tax.gov.ua) |
| Payment deadlines | Quarterly — by the **20th** of the month after each calendar quarter (20 Apr, 20 Jul, 20 Oct, 20 Jan) |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Ukrainian accountant** |
| Skill version | 1.0 |

### Base and amount table (as of 1 Jan 2026; verify current minimum wage)

**Base and amount table**

| Item | Basis | Indicative value (₴) |
| --- | --- | --- |
| Minimum wage (мінімальна зарплата) | statutory, 1 Jan 2026 | 8,647 |
| ЄСВ rate | statutory | 22% |
| **Minimum** monthly contribution | 22% × 1 min. wage (₴8,647) | **1,902.34** |
| **Minimum** quarterly contribution | 1,902.34 × 3 | **5,707.02** |
| **Minimum** annual contribution | 1,902.34 × 12 | **22,828.08** |
| **Maximum** monthly base | 20 × min. wage | 172,940 *(verify)* |
| **Maximum** monthly contribution | 22% × ₴172,940 | 38,046.80 *(verify)* |
| Military/police-only cap (not for FOP) | 15 × min. wage = ₴129,705 → 22% | 28,535.10 |

### Conservative defaults

**Conservative defaults**

| Situation | Default assumption |
| --- | --- |
| Single-tax FOP (Groups 1–3) with any or no income | Owes the **minimum** ₴1,902.34/month unless a clear exemption is documented |
| FOP wants to pay below the minimum | **Not allowed** — minimum applies even at zero income |
| Income unknown for a general-system FOP | Assume profit ≥ minimum base → ₴1,902.34/month floor |
| Claimed exemption (pensioner, disability, mobilised) | Treat as **not exempt** until status and supporting documents are confirmed |
| Maximum cap multiplier in doubt | Cap at the lower (15×) base and flag for reviewer; never under-cap |
| Mid-year start/stop | Pro-rate by **months registered**, not by days |

## 2. Who Pays / Who Is Exempt

### Who pays ЄСВ "for themselves"

- **Categories of payers** — **FOP (фізична особа-підприємець / sole proprietor)** on the **simplified system** (single-tax Groups 1, 2 and 3). **FOP on the general system** (загальна система) — pays 22% of **net taxable income (profit)**, but not less than the minimum and not more than the maximum base. **Independent professionals** ("особи, які провадять незалежну професійну діяльність") — e.g. private notaries, lawyers/advocates, arbitration managers, appraisers, and others registered as self-employed professionals. **Members of farming households** in some cases (out of scope here). > **Single-tax payers owe ЄСВ even with zero income.** In 2026 a FOP on the simplified system must pay the minimum ₴1,902.34/month **regardless of whether any income or activity occurred**. The only way to avoid it is to fall into an exemption category (below) or to be officially deregistered.

### Difference: simplified vs general system at zero income

**Difference: simplified vs general system at zero income**

| System | No income / loss in the month |
| --- | --- |
| Simplified (Groups 1–3) | Still owes the **minimum** ₴1,902.34 |
| General system | **No ЄСВ** is due for a month with no net profit / a loss (ЄСВ = 22% of profit, minimum floor only applies in months with profit) |

### Who may legally NOT pay ЄСВ for themselves (exemptions)

- **Exemption categories** — The following FOP/self-employed categories are released from paying ЄСВ "for themselves" — but the exemption must be supported by status and, where relevant, an application/documents: 1. **Old-age (and certain length-of-service) pensioners** — FOP who already receive a pension by age are exempt; payment becomes voluntary. 2. **Persons with disabilities** who receive a pension or social assistance on the grounds of disability — exempt; payment becomes voluntary. 3. **FOP who are also employed** ("основне місце роботи") where the **employer pays ЄСВ for them at no less than the minimum** on the employment income — relief applies for the months the employer's contribution is at/above the minimum. The taxpayer should retain proof. 4. **Mobilised FOP** (called up for military service during martial law) — exempt for the period of service, on the basis of supporting documents (mobilisation order / demobilisation confirmation). The State Tax Service / Pension Fund records the period.

### Status of wartime / mobilisation reliefs in 2026

- **Wartime reliefs status** — **2022–2024 voluntary right to skip ЄСВ:** During the COVID period and then the full-scale-war period, single-tax FOP had a **temporary voluntary right not to pay ЄСВ for themselves**. This relief was **abolished from 1 January 2025.** **2026 position:** There is **no general wartime exemption** for ordinary FOP. Single-tax payers must pay the minimum even with zero income. The **mobilisation exemption** (item 4 above) for FOP actually called up to serve **remains** in force during martial law and is the main wartime relief still available.

### What ЄСВ funds

- **What ЄСВ funds** — ЄСВ is the single contribution that finances the state social-insurance system: **State pension** (Pension Fund of Ukraine) — and it is what builds the FOP's **insurance length-of-service (страховий стаж)** toward a future pension; paying only the minimum earns roughly one month of stage per month paid. **Social insurance** — temporary incapacity / sickness, maternity, work-accident / occupational-disease, and unemployment cover.

## 3. Computation — Minimum, Voluntary Higher Base, Maximum Cap

- **Core formula (per month)** — ЄСВ (month) = 22% × base where  minimum base = 1 × minimum wage  (₴8,647 in 2026) maximum base = 20 × minimum wage (₴172,940 in 2026 — verify)

### Minimum (the usual case)

- **Minimum calculation** — Almost all single-tax FOP pay on the minimum base because the law sets a **floor** of one minimum wage regardless of actual income: 22% × ₴8,647 = ₴1,902.34 / month × 3 = ₴5,707.02 / quarter × 12 = ₴22,828.08 / year

### Voluntary higher base

- **Voluntary higher base rule** — A FOP **may choose** to pay ЄСВ on a **higher self-declared base** (anywhere between one minimum wage and the maximum base). This is voluntary and is usually done to build a larger future pension. Example: choosing a base of ₴20,000 → 22% × ₴20,000 = ₴4,400/month.

### Maximum cap

- **Maximum cap** — The base is **capped**. For 2026 the operative cap is **20 × minimum wage = ₴172,940**, giving a maximum monthly contribution of **22% × ₴172,940 = ₴38,046.80**. > **Verify the maximum-base multiplier.** Sources conflict. The State Budget Law for 2026 (3 Dec 2025) and current specialist Ukrainian tax catalogues (dtkt.ua, Factor, Holovbukh) state the FOP maximum base is **20 × minimum wage (₴172,940)**. A separate **15 ×** cap (₴129,705 → ₴28,535.10) applies **only to military / police service members**, not to FOP. One international summary (PwC) described the 20× increase as "postponed," leaving 15× — this appears to be outdated for the FOP base. The cap only ever matters for a FOP paying voluntarily above the minimum, so the minimum-case figures above are unaffected. **A Ukrainian accountant must confirm the exact cap before relying on it.**

### Mid-year start / stop (pro-ration)

- **Pro-ration rule** — ЄСВ accrues per **month of registration**. A FOP registered on any day of a month owes the full minimum for that month; a FOP deregistered owes for each month they were registered. Pro-rate by **whole months**, not days.

## 4. Payment & Reporting Calendar

### Payment (quarterly)

- **Payment cadence** — Self-employed people pay ЄСВ **quarterly** by the **20th of the month following the end of the calendar quarter**. A FOP may also pay monthly/in advance if they prefer, but the legal deadline is quarterly.

**Payment schedule table**

| Period (2026) | Minimum amount | Pay by |
| --- | --- | --- |
| Q1 (Jan–Mar 2026) | ₴5,707.02 | **20 April 2026** |
| Q2 (Apr–Jun 2026) | ₴5,707.02 | **20 July 2026** |
| Q3 (Jul–Sep 2026) | ₴5,707.02 | **20 October 2026** |
| Q4 (Oct–Dec 2026) | ₴5,707.02 | **20 January 2027** |

### Payment (quarterly)

> If the 20th falls on a weekend/holiday the deadline is **not** automatically extended for ЄСВ — pay on or before the 20th. Verify against the current ДПС tax calendar.

### Reporting — 2026 changes

- **Reporting changes** — **The separate ЄСВ report has been abolished as a standalone form.** Self-employed FOP no longer file a separate monthly or standalone annual ЄСВ report. ЄСВ data is reported **as part of the tax return** (in the unified single-tax declaration, via the ЄСВ appendix / "Додаток" / former Form D5 content folded in). From **2026** single-tax FOP move to **quarterly tax reporting** (for personal income tax, military levy and ЄСВ where relevant); FOP **without employees** generally report ЄСВ "for themselves" **once a year** together with the annual return. Indicative annual-return deadlines (verify against ДПС for the exact form/year): Groups 1–2 by **early March** after year-end; Group 3 quarterly returns plus the year-end ЄСВ appendix. > **Reporting is mandatory even at zero income.** Missing the ЄСВ appendix is treated as failing to report for the whole year.

## 5. Worked Examples

### Example 1 — Group 3 FOP (IT freelancer), normal year

Olena is a Group-3 single-tax FOP. She earns ₴80,000 some months, ₴0 in others.

- ЄСВ is **not** based on her income — she pays the **minimum**.
- Per month: **₴1,902.34**. Per quarter: **₴5,707.02**. Per year: **₴22,828.08**.
- This is **on top of** her single tax (5%) and military levy (1%) — see `ua-single-tax`.

### Example 2 — Group 2 FOP, no income for two months

Petro had ₴0 turnover in February and March (sick, no clients).

- As a **simplified-system** payer he **still owes** the minimum for those months.
- Q1 ЄСВ = 3 × ₴1,902.34 = **₴5,707.02**, due **20 April 2026**, despite zero income.

### Example 3 — Old-age pensioner FOP (exempt)

Maria is 63, receives an old-age pension, and runs a Group-1 FOP.

- As an **old-age pensioner** she is **exempt** from ЄСВ "for herself"; payment is **voluntary**.
- Default ЄСВ due: **₴0**. If she wants more pension stage she may pay voluntarily, on a base she chooses between ₴8,647 and ₴172,940.

### Example 4 — Employed + FOP (dual status)

Andriy works full-time for an employer who pays ЄСВ on his ₴30,000 salary, and also has a Group-3 FOP on the side.

- The employer's ЄСВ (22% × ₴30,000 = ₴6,600/month) is **above the minimum**.
- For months where the employer's contribution ≥ the minimum, Andriy is **relieved** of paying ЄСВ on the FOP. He should keep proof (payslips / employer confirmation).
- Default FOP ЄСВ for those months: **₴0** (relief), but **confirm month-by-month**.

### Example 5 — Voluntary higher base for pension

Iryna (Group 3) wants a bigger future pension and elects a base of ₴25,000.

- ЄСВ = 22% × ₴25,000 = **₴5,500/month** (well below the ₴38,046.80 cap).
- She must declare the chosen higher base; it is voluntary and self-elected.

## 6. Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue table**

| # | Situation | Why it needs judgement |
| --- | --- | --- |
| T2-1 | **Claimed exemption** (pensioner / disability / mobilised) | Must confirm official status, dates, and supporting documents; partial-year exemptions are common. |
| T2-2 | **Mid-year registration or deregistration** | Determine exact months owed; first/last partial month rules; deregistration paperwork timing. |
| T2-3 | **Dual status (employee + FOP)** | Relief only for months the employer's ЄСВ ≥ minimum; verify each month and the employment income level. |
| T2-4 | **General-system FOP with fluctuating profit/loss** | ЄСВ = 22% of profit with a min/max collar; loss months differ from simplified-system months. |
| T2-5 | **Maximum-base cap** (paying voluntarily above the minimum) | Cap multiplier (15× vs 20×) must be confirmed for the year before applying. |
| T2-6 | **Mobilisation period overlapping a quarter** | Apportioning exempt vs non-exempt months; documentation from the military unit. |
| T2-7 | **Independent professional vs FOP classification** | Different registration and base rules for notaries/advocates/etc. |
| T2-8 | **Backdated arrears / penalties** | Penalty and late-interest computation, voluntary disclosure. |

## 7. Reference Material + Test Suite

### Key sources (verify before reuse)

Law of Ukraine **No. 2464-VI** "On collection and accounting of the unified social contribution to compulsory state social insurance."
**State Tax Service of Ukraine** — tax.gov.ua / dps.gov.ua (ЄСВ rates, calendar, Електронний кабінет).
**Pension Fund of Ukraine** — pfu.gov.ua (FOP ЄСВ guidance, e.g. "Сплата ЄСВ для ФОП з 1 січня 2026 року").
**State Budget Law for 2026** (03 Dec 2025) — minimum wage ₴8,647 from 1 Jan 2026.
PwC Worldwide Tax Summaries — Ukraine, Individual / Other taxes (note the cap discrepancy in §3).
Specialist Ukrainian tax catalogues: dtkt.ua, Factor (factor.academy / i.factor.ua), Holovbukh (buhplatforma), taxer.ua, buh.ua.

### Self-check test suite

**Self-check test suite table**

| # | Prompt | Expected answer |
| --- | --- | --- |
| 1 | What is the ЄСВ rate? | **22%**. |
| 2 | Minimum monthly ЄСВ in 2026? | **₴1,902.34** (22% × ₴8,647). |
| 3 | Minimum quarterly ЄСВ? | **₴5,707.02**. |
| 4 | A Group-2 FOP earned ₴0 this quarter — owes? | **₴5,707.02** — single-tax payers pay even at zero income. |
| 5 | A general-system FOP had a loss this month — owes? | **₴0** for that month (ЄСВ = 22% of profit; no profit, no ЄСВ). |
| 6 | When is Q1 2026 ЄСВ due? | **20 April 2026** (20th of month after the quarter). |
| 7 | Is the old wartime "skip ЄСВ" relief available in 2026? | **No** — abolished from 1 Jan 2025; only the mobilisation exemption remains. |
| 8 | Who can legally not pay ЄСВ for themselves? | Old-age pensioners, persons with disabilities on disability pension, FOP whose employer pays ЄСВ ≥ minimum, and mobilised FOP. |
| 9 | Is there still a separate monthly ЄСВ report for FOP? | **No** — ЄСВ is reported within the tax return; the separate report is abolished. |
| 10 | What does ЄСВ fund? | State **pension** + **social insurance** (sickness, maternity, accident, unemployment). |

## PROHIBITIONS

- **Do not** tell a single-tax FOP they can skip ЄСВ in a zero-income month — they cannot (simplified system); they owe the minimum.
- **Do not** apply the 2022–2024 voluntary-non-payment relief to 2025 or 2026 — it was abolished from 1 Jan 2025.
- **Do not** assert an exemption (pensioner / disability / mobilised / dual-status) without confirmed status and supporting documents.
- **Do not** state the maximum-base cap as settled fact without a Ukrainian accountant confirming the multiplier for the year (15× vs 20×) — see §3.
- **Do not** quote ₴ figures without anchoring them to the **current minimum wage** and adding "verify current value."
- **Do not** conflate ЄСВ with the single tax or the military levy — they are separate charges (see `ua-single-tax`).
- **Do not** treat the quarterly **20th** deadline as auto-extended over weekends/holidays without checking the ДПС calendar.

## Disclaimer

This skill is **research-verified** from public sources (State Tax Service of Ukraine, Pension Fund of Ukraine, PwC Worldwide Tax Summaries, and reputable Ukrainian specialist sources) as of **May 2026** for tax year 2026. It is **not** a substitute for professional advice and **must be signed off by a qualified Ukrainian accountant / tax adviser** before being relied upon for filing or payment. Rates, the minimum wage, the maximum-base multiplier, deadlines, and exemption rules can change — especially under martial law — so always verify the current values with ДПС / the Pension Fund. Part of the Open Accountants community library at **openaccountants.com**; contributions and corrections welcome.

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
