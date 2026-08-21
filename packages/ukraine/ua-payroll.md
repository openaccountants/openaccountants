---
name: ua-payroll
description: Use this skill whenever asked about Ukrainian payroll for a sole proprietor (ФОП) or small employer who hires staff. Trigger on phrases like "Ukraine payroll", "hiring an employee in Ukraine", "payroll taxes Ukraine", "how much does it cost to employ someone in Ukraine", "ЄСВ on salary", "ПДФО on wages", "military levy on salary", "зарплата податки", "найняти працівника ФОП", "gross to net Ukraine", "employee vs ФОП contractor", or any question about wages, payroll withholding, the employer's social contribution, or the unified PIT/ЄСВ/military-levy report. Covers employer registration duties, the 18% PIT + 5% military levy withheld from the employee, the 22% ЄСВ paid by the employer on top of gross, the minimum-wage ЄСВ floor, the reduced 8.41% ЄСВ for employees with disabilities, the reporting and payment calendar, and misclassification risk when engaging another ФОП instead of hiring. ALWAYS read this skill before any Ukrainian payroll work.
version: 1.0
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Payroll

## Ukraine Payroll for Employers (Зарплата та податки на найманих працівників) — Skill v1.0

This skill covers what happens when a Ukrainian sole proprietor (**ФОП / fizychna osoba-pidpryyemets**) or small employer **hires staff under an employment contract (трудовий договір)** and must run payroll. It is distinct from the owner's own taxes: a single-tax ФОП's own single tax and personal ЄСВ are handled by `ua-single-tax` and `ua-social-contributions`. The moment that ФОП hires even one employee, it becomes a **tax agent (податковий агент)** and an **ЄСВ payer for that employee** with a separate set of obligations described below.

> **Wartime note.** Figures are pinned at their **1 January 2026** values. Ukraine is under martial law. The **military levy (військовий збір, ВЗ) is 5%** on salaries since **1 December 2024** (raised from 1.5%). Most amounts key off the statutory minimum wage (**₴8,647 from 1 Jan 2026**). Always **verify the current value** before relying on a number.

> **Two different "ФОП" roles — don't confuse them.** A ФОП can be (a) the *employer* running payroll for hired staff (this skill), and (b) a *worker* who invoices a business under a service contract instead of being on payroll (§4, misclassification).

## 1. Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Ukraine (UA) |
| Taxes on salary | **ПДФО** (personal income tax) 18% + **військовий збір** (military levy) 5% — *withheld from employee*; **ЄСВ** (unified social contribution) 22% — *paid by employer on top of gross* |
| Currency | UAH (₴) |
| Minimum wage 2026 (мінімальна зарплата) | **₴8,647 / month** (₴52 / hour) from 1 Jan 2026 |
| ЄСВ floor | Salary base must be **≥ minimum wage** → minimum ЄСВ **₴1,902.34 / month** per full-time employee |
| ЄСВ maximum base | 20 × minimum wage = **₴172,940 / month** → max ЄСВ **₴38,046.80 / month** *(verify — §3)* |
| Reduced ЄСВ | **8.41%** on salaries of **employees with a disability** (особа з інвалідністю) |
| Legislation | Tax Code of Ukraine (ПКУ) — PIT §167, military levy §16¹ subsec. 10; Law No. 2464-VI on ЄСВ; Labour Code (КЗпП); State Budget Law for 2026 (03 Dec 2025) sets the minimum wage; Law No. 4536-IX (16 Jul 2025) — 2026 reporting changes |
| Authority | **Державна податкова служба (ДПС / State Tax Service)** collects PIT, ВЗ and ЄСВ; Pension Fund (Пенсійний фонд) keeps insurance records |
| Portal | **Електронний кабінет платника** (cabinet.tax.gov.ua) |
| Withholding remittance | PIT + ВЗ paid **on/at the moment salary is paid** (within the salary-payment day); if salary accrued but unpaid, by the **30th** of the following month |
| ЄСВ remittance | By the **20th** of the month following the month of accrual |
| Unified report | **Податковий розрахунок** (combined PIT + ВЗ + ЄСВ + Form 4ДФ annex) — **quarterly** with monthly breakdown from 2026 |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Ukrainian accountant** |
| Skill version | 1.0 |

### Headline rates (1 Jan 2026)

**Headline rates (1 Jan 2026)**

| Component | Native term | Rate | Who pays | Reduces net pay? |
| --- | --- | --- | --- | --- |
| Personal income tax | ПДФО (податок на доходи фізичних осіб) | **18%** | Employee (withheld) | Yes |
| Military levy | військовий збір (ВЗ) | **5%** | Employee (withheld) | Yes |
| Unified social contribution | ЄСВ (єдиний соціальний внесок) | **22%** | **Employer (on top of gross)** | No |
| ЄСВ — employees with disability | ЄСВ (пільгова ставка) | **8.41%** | Employer | No |

### Conservative defaults

**Conservative defaults**

| Situation | Default assumption |
| --- | --- |
| Salary below minimum wage for a full-time post | **Not allowed.** Accrue ЄСВ on at least ₴8,647 (the minimum-wage floor) |
| Part-time / partial month | ЄСВ may be on actual (proportional) salary — but confirm; the floor applies to full normal hours |
| Worker engaged "as a ФОП" but works like staff | Treat as **disguised employment risk** → default to advising an employment contract (§4) |
| Disability status claimed but no certificate on file | Use **standard 22%**, not 8.41%, until the disability certificate is documented |
| Unsure whether a payment is "salary" | Treat as salary subject to PIT + ВЗ + ЄСВ unless clearly a non-wage item |
| Any rate/threshold | State the formula and add "**verify current value**" |

## 2. Required inputs & refusal catalogue

### Inputs needed before computing payroll

- **Inputs needed before computing payroll** — 1. **Employer status** — is the employer a ФОП or a legal entity? Is the ФОП registered as an employer / has it filed the hiring notification (повідомлення про прийняття на роботу) **before the employee starts**? 2. **Gross salary per employee** (нарахована заробітна плата) and whether full-time or part-time. 3. **Employee special status** — disability (for 8.41% ЄСВ), and any PIT social-tax-allowance (податкова соціальна пільга, ПСП) eligibility. 4. **Pay frequency** — Ukraine requires salary **at least twice a month**, intervals ≤ 16 calendar days. 5. **Tax year / month** to pin the minimum wage and caps.

### Refusal catalogue

**Refusal catalogue**

| Code | Refuse / escalate when | Why |
| --- | --- | --- |
| **R-UA-1** | User asks how to pay "salary" off the books / in cash to dodge ЄСВ | Illegal undeclared employment (зарплата в конвертах); fines up to 10× minimum wage per worker |
| **R-UA-2** | User asks to dress up an employment relationship as a ФОП service contract to avoid payroll taxes | Disguised employment; reclassification, back taxes + penalties (§4) |
| **R-UA-3** | User wants to pay below the minimum wage for full-time work | Statutory floor; ЄСВ must still be on ₴8,647 |
| **R-UA-4** | Hiring foreign nationals / work-permit, posted-worker, or special-regime payroll | Out of scope; specialist immigration + labour advice needed |
| **R-UA-5** | Diia City "гіг-спеціаліст" gig-contract payroll (5% PIT regime, 1.5% military levy via residency tax) | Different regime — cross-ref `ua-tax-optimization`; do **not** apply the standard 18%/5%/22% set without checking Diia City status |
| **R-UA-6** | Mobilised/military personnel pay, sickness/maternity benefit funded by the state social fund, or дивіденди treated as wages | Special bases/rates; verify with ДПС |
| **R-UA-7** | The figure cannot be verified against ДПС / a reputable source for the relevant month | YMYL — never guess a rate or cap |

## 3. Gross-to-net computation

### The model

- **Gross-to-net model** — For each employee, each month: ``` Employee withholdings (reduce take-home): ПДФО (PIT)          = 18% × gross salary Військовий збір (ВЗ) =  5% × gross salary Net pay             = gross − ПДФО − ВЗ Employer cost (on top of gross, NOT withheld): ЄСВ                 = 22% × base, where base = max(gross, ₴8,647 minimum-wage floor) capped at base ≤ ₴172,940 (20 × minimum wage)   [verify] 8.41% instead of 22% for employees with disability Total employer cost = gross + ЄСВ ``` Key points: - **PIT and ВЗ have no floor and no cap** — they are flat percentages of the actual gross. - **ЄСВ has a floor** (must be on ≥ minimum wage for a full normal month) **and a cap** (base ≤ 20 minimum wages = ₴172,940; max ЄСВ ≈ **₴38,046.80/month** — *verify*). - ЄСВ is the employer's expense; it is **never** deducted from the employee. - A **податкова соціальна пільга (ПСП)** can reduce the PIT base for low earners — apply only if eligibility is documented; otherwise default to no ПСП.

### Worked: ₴30,000 gross (standard full-time employee)

**Worked: ₴30,000 gross (standard full-time employee)**

| Line | Calculation | Amount (₴) |
| --- | --- | --- |
| Gross salary (нарахована ЗП) | — | 30,000.00 |
| ПДФО (PIT) | 18% × 30,000 | −5,400.00 |
| Військовий збір (ВЗ) | 5% × 30,000 | −1,500.00 |
| **Net pay to employee (на руки)** | 30,000 − 5,400 − 1,500 | **23,100.00** |
| ЄСВ (employer, on top) | 22% × 30,000 | 6,600.00 |
| **Total cost to employer** | 30,000 + 6,600 | **36,600.00** |

### Worked: ₴30,000 gross (standard full-time employee)

So a ₴30,000 salary costs the employer **₴36,600**, the employee receives **₴23,100**, and **₴13,500** goes to the budget (₴5,400 PIT + ₴1,500 ВЗ + ₴6,600 ЄСВ).

## 4. Employee vs ФОП-contractor (misclassification / disguised employment)

A common arrangement: instead of hiring an employee, a business asks the worker to register as a **single-tax ФОП (Group 3)** and invoice for "services". The worker then pays ~5% single tax + 1% military levy + their own minimum ЄСВ, and the engaging business pays **no** payroll PIT/ВЗ/ЄСВ. This can be legitimate for genuine independent work — but it is **disguised employment (приховані трудові відносини)** if the substance is an employment relationship.

### Indicators that point to *employment*, not genuine contracting

- **Employment indicators** — - Fixed working hours / a workplace / subordination to internal rules. - Single client (the engaging business is the worker's only or dominant "customer"). - Payment is a regular fixed monthly amount resembling salary, not per-deliverable. - The business supplies the tools, equipment and workplace. - Personal performance required; the ФОП cannot subcontract or substitute. - Integration into the org chart, ongoing managed work rather than a defined project. Ukraine's incoming labour-reform "**5+ indicators**" test presumes employment when **5 or more** such criteria are met (status pending the new Labour Code — *verify timing*).

### Consequences of misclassification

- **Consequences** — - **Reclassification** to an employment relationship by the labour inspectorate / court. - **Back PIT, military levy and ЄСВ** for the whole period, plus interest. - **Fines** under the Labour Code (КЗпП ст. 265) up to **10× minimum wage per worker** for undeclared employment; potential personal liability for management.  _(Labour Code of Ukraine (КЗпП) ст. 265)_

### Default guidance

If indicators point to employment, **advise an employment contract** with proper payroll (this skill). Only treat as a genuine ФОП-to-ФОП service contract when the worker is truly independent, has multiple clients, controls their own work, and bears business risk — document the reasoning. See **R-UA-2**.

> **Diia City gig specialists.** Companies in the **Diia City** regime can engage **гіг-спеціалісти (gig specialists)** under a special gig-contract that is neither an employment contract nor an ordinary ФОП arrangement, with a favourable resident-tax regime (commonly **5% PIT**). This is a separate regime — **cross-ref `ua-tax-optimization`** and do not apply the standard 18%/5%/22% set without confirming Diia City status (R-UA-5).

## 5. Reporting & payment calendar

### Registration / before the first employee starts

- **Registration before first employee starts** — - File the **повідомлення про прийняття на роботу** (notification of hiring) to ДПС **before** the employee begins work — failure is penalised. - Issue a hiring order (наказ про прийняття) and employment contract; keep a salary ledger.

### Withholding remittance (PIT + military levy)

- **Withholding remittance (PIT + military levy)** — - PIT and ВЗ are **paid at the same time salary is paid** (з виплатою зарплати). - If salary is **accrued but not paid**, PIT/ВЗ are due by the **30th** of the following month. - Advance + final salary each month (twice-monthly pay rule, ≤ 16-day interval).

### ЄСВ remittance

- **ЄСВ remittance** — - ЄСВ is due by the **20th** of the month following the accrual month (e.g., January salary → ЄСВ by 20 February).

### Unified report — Податковий розрахунок (combined PIT + ВЗ + ЄСВ)

**Unified report filing deadlines**  _(Law No. 4536-IX (16 Jul 2025))_

| Period | Filing deadline (verify; rolls to next business day if weekend/holiday) |
| --- | --- |
| Q1 2026 | by **10 May 2026** (→ 11 May 2026 in practice) |
| Q2 2026 | by **9 August 2026** |
| Q3 2026 | by **10 November 2026** |
| Q4 2026 | by **9 February 2027** |

### Unified report — Податковий розрахунок (combined PIT + ВЗ + ЄСВ)

From **1 January 2026** (Law No. 4536-IX, 16 Jul 2025) the **Податковий розрахунок** — the single report combining ЄСВ, ПДФО, the military levy and the **4ДФ** per-person annex — is filed **quarterly with a monthly breakdown** within the quarter.

> Filed via the **Електронний кабінет**. There is **no separate military-levy return** — ВЗ is reported inside the Податковий розрахунок alongside PIT and ЄСВ.

## 6. Worked examples

### Example A — Minimum-wage employee

**Example A — Minimum-wage employee**

| Line | Calc | ₴ |
| --- | --- | --- |
| Gross | — | 8,647.00 |
| ПДФО 18% | 0.18 × 8,647 | −1,556.46 |
| ВЗ 5% | 0.05 × 8,647 | −432.35 |
| **Net** |  | **6,658.19** |
| ЄСВ 22% | 0.22 × 8,647 | 1,902.34 |
| **Total cost** |  | **10,549.34** |

### Example A — Minimum-wage employee

Gross = ₴8,647 (the 2026 minimum wage), standard rates.

(ЄСВ minimum floor met exactly, since base = minimum wage.)

### Example B — Part-time below minimum wage (ЄСВ floor bites)

**Example B — Part-time below minimum wage (ЄСВ floor bites)**

| Line | Calc | ₴ |
| --- | --- | --- |
| Gross | — | 5,000.00 |
| ПДФО 18% | 0.18 × 5,000 | −900.00 |
| ВЗ 5% | 0.05 × 5,000 | −250.00 |
| **Net** |  | **3,850.00** |
| ЄСВ — *if part-time is genuine* | 22% × actual ₴5,000 | 1,100.00 |
| ЄСВ — *if treated as full normal-hours post* | 22% × ₴8,647 floor | 1,902.34 |

### Example B — Part-time below minimum wage (ЄСВ floor bites)

A part-time employee is paid **₴5,000** gross for a part-time post.

The **floor rule** matters: for a full normal-hours position ЄСВ must be on **at least ₴8,647** even if the paid salary is lower. For a genuinely part-time/partial-month post, ЄСВ may be on the actual amount — **confirm the working-time basis** before choosing.

### Example C — Employee with a disability (reduced ЄСВ)

**Example C — Employee with a disability (reduced ЄСВ)**

| Line | Calc | ₴ |
| --- | --- | --- |
| Gross | — | 30,000.00 |
| ПДФО 18% |  | −5,400.00 |
| ВЗ 5% |  | −1,500.00 |
| **Net** |  | **23,100.00** |
| ЄСВ **8.41%** (not 22%) | 0.0841 × 30,000 | 2,523.00 |
| **Total cost** |  | **32,523.00** |

### Example C — Employee with a disability (reduced ЄСВ)

Gross = ₴30,000, documented disability certificate on file → ЄСВ at **8.41%**.

Compared with Example "₴30,000 standard" (₴36,600 total cost), the disability rate saves the employer **₴4,077/month**. *(Without a certificate on file, use 22% — default.)*

### Example D — High earner hitting the ЄСВ cap

**Example D — High earner hitting the ЄСВ cap**

| Line | Calc | ₴ |
| --- | --- | --- |
| ПДФО 18% | 0.18 × 200,000 | 36,000.00 |
| ВЗ 5% | 0.05 × 200,000 | 10,000.00 |
| **Net** | 200,000 − 46,000 | **154,000.00** |
| ЄСВ base | min(200,000, **172,940** cap) | 172,940.00 |
| ЄСВ 22% | 0.22 × 172,940 | **38,046.80** *(verify cap)* |
| **Total cost** | 200,000 + 38,046.80 | **238,046.80** |

### Example D — High earner hitting the ЄСВ cap

Gross = ₴200,000.

PIT and ВЗ apply to the **full** ₴200,000 (no cap); **ЄСВ stops at the 20-minimum-wage base** of ₴172,940, so the marginal employer ЄСВ on income above the cap is **zero**.

## 7. Tier 2 — judgement calls & edge cases

- **Salary in kind / benefits** — taxable; a "natural coefficient" (натуральний коефіцієнт) grosses up non-cash benefits for PIT. Flag for accountant.
- **Vacation pay & sick leave** — included in the ЄСВ/PIT base; first 5 days of sick leave are employer-funded, the rest from the social-insurance fund (different ЄСВ treatment on the fund-paid portion). Verify.
- **ПСП (податкова соціальна пільга)** — reduces PIT base for low earners meeting the income limit; apply only with documented eligibility.
- **Дивіденди / royalties / GPC (civil-law) contract fees** — different rate/base mixes; a civil-law service contract with an individual (not a ФОП) is still subject to PIT + ВЗ and ЄСВ (often at the standard 22%). Don't conflate with employment.
- **Multiple jobs** — the minimum-wage ЄСВ floor applies at the **main** place of work; for a secondary job ЄСВ is on actual pay. Confirm which is primary.
- **Diia City** — see §4 / R-UA-5 and `ua-tax-optimization`.

## 8. References & test suite

### References (verify against primary sources before filing)

- **References** — - **Tax Code of Ukraine (ПКУ)** — §167 (PIT 18%), §16¹ subsec. 10 (military levy 5%), §168 (withholding/remittance), §176 (tax-agent reporting). - **Law No. 2464-VI** "On collection and accounting of the Unified Social Contribution" — 22% rate, minimum/maximum base, 8.41% for employees with disability. - **Labour Code of Ukraine (КЗпП)** — ст. 265 (penalties for undeclared/disguised employment), twice-monthly pay rule, hiring notification. - **State Budget Law for 2026** (adopted 03 Dec 2025) — minimum wage ₴8,647 from 1 Jan 2026. - **Law No. 4536-IX** (16 Jul 2025) — quarterly Податковий розрахунок from 1 Jan 2026. - **ДПС / State Tax Service** — tax.gov.ua / dps.gov.ua; Електронний кабінет (cabinet.tax.gov.ua). - **PwC Worldwide Tax Summaries — Ukraine** (corroboration of rates).

### Self-check / test suite

1. ₴30,000 gross → PIT ₴5,400, ВЗ ₴1,500, net ₴23,100, ЄСВ ₴6,600, total ₴36,600. ✔
2. ₴8,647 (minimum wage) → net ₴6,658.19, ЄСВ ₴1,902.34 (= ЄСВ minimum). ✔
3. Disability employee at ₴30,000 → ЄСВ 8.41% = ₴2,523 (not ₴6,600). ✔
4. ₴200,000 → ЄСВ capped at base ₴172,940 → ЄСВ ₴38,046.80; PIT/ВЗ uncapped. ✔
5. Worker with one client, fixed hours, employer's tools, monthly fixed pay → **employment** indicators ≥ 5 → advise contract (R-UA-2). ✔
6. Request to pay cash off-book to skip ЄСВ → **refuse** (R-UA-1). ✔
7. Diia City gig specialist → do not apply 18%/5%/22%; cross-ref `ua-tax-optimization` (R-UA-5). ✔
8. Q1 2026 unified report deadline → 10/11 May 2026; no separate military-levy return. ✔

## PROHIBITIONS

- **Prohibitions** — - **Do NOT** advise paying wages off the books, in cash undeclared, or "in envelopes" (зарплата в конвертах) to avoid ЄСВ/PIT/ВЗ. - **Do NOT** structure a genuine employment relationship as a ФОП service contract to dodge payroll taxes (disguised employment). - **Do NOT** accrue ЄСВ below the minimum-wage floor for a full normal-hours position. - **Do NOT** apply the 8.41% reduced ЄСВ without a documented disability certificate. - **Do NOT** treat Diia City gig specialists under the standard 18%/5%/22% set without confirming the regime. - **Do NOT** state any rate, cap or deadline as final without **verifying the current value** against ДПС / a reputable source for the relevant month. - **Do NOT** file or submit anything on the user's behalf, or move money — prepare figures for the user and their accountant to review and submit.

## Disclaimer

This skill is **research-verified** against public sources (ДПС / State Tax Service, PwC Worldwide Tax Summaries, reputable Ukrainian payroll/accounting publishers) but is **pending sign-off by a qualified Ukrainian accountant**. Ukrainian payroll rules, minimum wage, caps, the military-levy rate and reporting forms change frequently — especially under martial law — so every figure must be re-verified for the exact month of computation. This is general information, **not** legal, tax or accounting advice, and does not create a professional relationship. Always have a credentialed Ukrainian accountant review payroll before salaries are paid or reports are filed.
Part of **openaccountants.com** — open-source tax skills for the self-employed.

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
