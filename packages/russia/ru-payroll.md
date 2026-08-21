---
name: ru-payroll
description: Use this skill whenever asked about payroll in Russia — how an individual entrepreneur (ИП) or a company (ООО) computes, withholds, reports, and pays the taxes and contributions on employee wages in 2026. Covers НДФЛ withheld from salaries at the progressive scale, employer страховые взносы under the единый тариф (30% up to the unified base, 15.1% above), the reduced ~15% SME tariff on wages above 1.5× МРОТ for priority-sector SMEs, injury contributions (взносы на травматизм) paid to СФР, payroll reporting (РСВ, 6-НДФЛ, персонифицированные сведения, ЕФС-1), the ЕНП/ЕНС unified tax account, and pay/withholding deadlines. Trigger on phrases like "payroll Russia", "hiring an employee Russia", "страховые взносы employer", "6-НДФЛ", "зарплатные налоги", "РСВ", "сколько стоит сотрудник", "gross to net Russia", "НДФЛ с зарплаты".
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

# RU Payroll

## Russia — Payroll for an ИП or Company that Hires Staff (2026)

This skill explains Russian PAYROLL: the full set of taxes and contributions that an employer (an ИП or a company) must compute, withhold, report, and pay when it has employees on an employment contract (трудовой договор) or a civil-law contract (договор ГПХ) in 2026.

Russian payroll has **two economically distinct money flows**:

1. **НДФЛ (налог на доходы физических лиц)** — personal income tax. This is the **employee's** tax, but the employer is the **tax agent (налоговый агент)**: it must withhold НДФЛ from the gross wage and remit it. It comes OUT of the employee's gross — it does not add to employer cost.
2. **Страховые взносы (insurance contributions)** — pension + medical + social insurance under the **единый тариф**, plus **взносы на травматизм** (injury/occupational-disease insurance). These are paid by the **employer ON TOP of** the gross wage — they are a real additional cost of employment.

The administering bodies are the **ФНС** (Федеральная налоговая служба — collects НДФЛ and the единый тариф via the Единый налоговый счёт / ЕНС) and the **СФР** (Социальный фонд России — receives взносы на травматизм и the ЕФС-1 report). Read alongside **ru-social-contributions** (an ИП's own fixed contributions «за себя», which are separate from employer payroll) and **ru-self-employed-npd** (engaging самозанятые instead of employees — see §5 for the misclassification risk).

The user may write in Russian or English. **Reply in the user's language.** Russian payroll terms (НДФЛ, страховые взносы, единый тариф, предельная база, РСВ, 6-НДФЛ, ЕФС-1, СФР, МРОТ) are kept in Russian throughout because that is how they appear on every form and in every law.

## 1. Quick Reference

**Quick Reference table**

| Field | Value (2026) |
| --- | --- |
| Country | Russia (RU) |
| МРОТ (federal minimum wage) | **27,093 ₽/month** (Law No. 429-ФЗ of 28.11.2025) — verify regional МРОТ may be higher |
| 1.5× МРОТ (SME threshold) | **40,639.50 ₽/month** per employee |
| **НДФЛ — progressive scale** (cumulative annual income) | 13% up to 2,400,000 ₽; 15% over 2.4M to 5M; 18% over 5M to 20M; 20% over 20M to 50M; 22% over 50M (each band taxed at its own rate). Resident salary income. |
| Standard employer **единый тариф** | **30%** on cumulative wage up to предельная база; **15.1%** on the excess above the база |
| Предельная база (unified, единая предельная величина) 2026 | **2,979,000 ₽** per employee per year (Government Decree; confirmed by ФНС) |
| Reduced **SME tariff** (priority sectors) | **30%** on the part of monthly wage up to 1.5× МРОТ; **15%** on the part above 1.5× МРОТ (verify eligibility — see §3.4) |
| SME manufacturing (обрабатывающее производство) tariff | **30%** up to 1.5× МРОТ; **7.6%** above 1.5× МРОТ (verify) |
| Взносы на травматизм (injury) | **0.2% – 8.5%** of wages, by ОКВЭД hazard class (Law No. 434-ФЗ of 28.11.2025) — paid to СФР |
| Currency | RUB (₽) |
| Legislation | Налоговый кодекс РФ — гл. 23 (НДФЛ), гл. 34 (страховые взносы, ст. 419–432); ст. 427 (reduced tariffs); Law No. 125-ФЗ (травматизм) |
| **Authority** | **ФНС** (НДФЛ + единый тариф via ЕНС/ЕНП) + **СФР** (травматизм + ЕФС-1) |
| **Reporting forms** | **6-НДФЛ**, **РСВ** (расчёт по страховым взносам), **персонифицированные сведения о физлицах**, **ЕФС-1** (incl. раздел 2 для травматизма and subsections for personnel events) |
| **Deadlines** (high-level) | НДФЛ: pay by 28th (for 1st–22nd) / by 5th of next month (for 23rd–end); единый тариф: pay by 28th of next month; травматизм: pay by 15th of next month; уведомления by 25th; reports by 25th — see §4 |
| Contributor | Open Accountants Community |
| **Quality tier** | **Research-verified — pending sign-off by a Russian accountant** |
| Version | 1.0 |

### Conservative defaults

When information is missing, assume the position that produces the **higher liability** or the **safer filing**, and flag the assumption:

1. **Assume the STANDARD единый тариф (30% / 15.1%), not a reduced one**, unless the user documents МСП-register inclusion, a qualifying primary ОКВЭД, and the 70%-income test (§3.4). The reduced SME tariff was narrowed for 2026 to priority sectors only — do not assume it.
2. **Assume the employee is a tax RESIDENT** taxed on the progressive scale starting at 13%, unless told otherwise. Non-residents are out of scope here (different rates apply) — refer out.
3. **Assume an employment relationship** when work looks like ongoing personal labour under the employer's direction. Do not reclassify employees as самозанятые to save tax (§5).
4. **Verify every current-year figure before filing.** МРОТ, the предельная база, the НДФЛ band thresholds, the травматизм tariff table, and the SME priority-sector list are all reset annually by law. Figures here are 2026 values verified against ФНС/СФР sources; re-verify at nalog.gov.ru and sfr.gov.ru before relying on them.
5. **Cumulative-from-year-start logic governs everything.** Both the НДФЛ band and the единый тариф база are tracked on a running year-to-date basis per employee. A figure correct in January can change mid-year once a threshold is crossed.

## 2. Required Inputs & Refusal Catalogue

### 2.1 Required inputs

- **Required inputs before computing payroll** — Before computing payroll, collect: **Employer type & status** — ИП or company; whether it is in the **реестр МСП** (SME register). **Primary ОКВЭД** and whether ≥70% of income comes from it (governs SME tariff eligibility, §3.4). **Injury hazard class / ОКВЭД** — sets the травматизм rate (0.2%–8.5%); the СФР assigns it. **Per employee:** gross monthly wage (gross, до удержания НДФЛ), tax-residency status, standard deductions claimed (e.g. вычеты на детей), and year-to-date cumulative wage and НДФЛ. **Contract type** — трудовой договор vs договор ГПХ (both attract НДФЛ + страховые взносы; ГПХ may differ on травматизм — verify the contract terms). **Region** — to check whether a regional МРОТ above the federal 27,093 ₽ applies.

### 2.2 Refusal catalogue

Refuse, or escalate to a qualified Russian accountant / payroll specialist, when:

- **R-1 Misclassification request** — The user wants to pay ongoing staff as самозанятые / ГПХ to avoid НДФЛ and страховые взносы. Explain the risk (§5) and decline to design an evasion scheme.
- **R-2 Non-resident or foreign-worker payroll** — Different НДФЛ rates, patent rules, and migration-status complications. Out of scope — refer out.
- **R-3 Special categories** — Northern/regional coefficients and надбавки, hazardous-work early pensions, государственная тайна, seasonal/vahta arrangements — refer to a specialist.
- **R-4 Reduced-tariff eligibility judgement** — Confirming whether a specific ОКВЭД is on the 2026 priority-sector list, or whether the IT/Сколково/special-economic-zone 7.6%/0% regimes apply, is a fact-specific legal determination — verify against the official list and have a professional confirm.
- **R-5 НДФЛ on non-salary income** — (dividends, material benefit, prizes, property) — different rules and rates; out of scope for this payroll skill.
- **R-6 Arrears, penalties, or ФНС/СФР disputes** — Refer to a credentialed professional.

## 3. Gross-to-Net + Employer-Cost Computation

Russian payroll is computed **per employee, cumulatively from the start of the calendar year**. The gross wage (the contractual «оклад» / зарплата до удержаний) is the starting point.

### 3.1 НДФЛ — withheld from the gross (employee's tax)

- **НДФЛ mechanics** — НДФЛ is **withheld from** the gross wage. The employee receives gross minus НДФЛ; the employer remits the НДФЛ to the ФНС. For 2026, resident salary income uses the **progressive scale on cumulative year-to-date income**, each band taxed at its own rate.

**НДФЛ progressive scale table**

| Cumulative annual income | Rate |
| --- | --- |
| up to 2,400,000 ₽ | **13%** |
| over 2.4M to 5,000,000 ₽ | **15%** |
| over 5M to 20,000,000 ₽ | **18%** |
| over 20M to 50,000,000 ₽ | **20%** |
| over 50,000,000 ₽ | **22%** |

- **Band and deduction rule** — Only the portion of income within each band is taxed at that band's rate. Standard deductions (вычеты, e.g. children) reduce the taxable base before applying the rate.
- **НДФЛ computation formula** — Taxable base   = gross wage − applicable вычеты НДФЛ (month)   = НДФЛ on cumulative YTD base − НДФЛ already withheld earlier in the year Net to employee = gross − НДФЛ (month)
- **Ordinary salary effective rate** — For most ordinary salaries (well under 2.4M ₽/year), the effective rate is a flat **13%**.

### 3.2 Страховые взносы — единый тариф (employer cost, on top of gross)

- **Единый тариф mechanics** — The employer pays the **единый тариф** ON TOP of the gross wage. The единый тариф is a single, non-itemised contribution covering pension (ОПС), medical (ОМС), and social/temporary-disability (ВНиМ) insurance. It is tracked on **cumulative YTD wage** against the предельная база.
- **Единый тариф formula** — While cumulative YTD wage ≤ 2,979,000 ₽ :  rate = 30% On the part of wage above 2,979,000 ₽   :  rate = 15.1%

### 3.3 Взносы на травматизм — injury insurance (employer cost, to СФР)

- **Травматизм rules** — Separately, the employer pays **взносы на травматизм** to the **СФР** at a rate from **0.2% to 8.5%** of wages, set by the company's occupational-hazard class (assigned by ОКВЭД). There is **no предельная база** for травматизм — it applies to the full wage all year. Use 0.2% as the default illustrative rate for a low-hazard office activity; the actual rate must come from the СФР.

### 3.4 Reduced SME tariff (priority sectors) — eligibility narrowed for 2026

- **SME tariff eligibility conditions** — For **2026**, the reduced SME tariff is **no longer available to all small businesses**. It applies only to SMEs that **simultaneously**: 1. are in the **реестр МСП** (SME register); 2. have a **primary ОКВЭД on the 2026 priority-sector list** (Government Decree No. 4125-р of 27.12.2025); and 3. earn **≥70% of income** from that primary activity.  _(Government Decree No. 4125-р of 27.12.2025)_
- **SME tariff monthly wage split formula** — On the part of monthly wage up to 1.5× МРОТ  :  30% On the part of monthly wage above 1.5× МРОТ  :  15%   (7.6% for manufacturing — verify)
- **Public catering and interaction with предельная база** — (Public catering / общепит SMEs retained the 15%-above-1.5×-МРОТ treatment; verify the current list.) Above the annual предельная база the standard 15.1% logic still interacts — for ordinary salaries this rarely binds, but **verify for high earners**. If eligibility is not documented, default to the standard 30% / 15.1% tariff (Conservative default #1).

### 3.5 Worked computation — 100,000 ₽/month gross

Single resident employee, 100,000 ₽/month gross, no deductions, low-hazard травматизм 0.2%, early in the year (well below all annual caps). НДФЛ at 13%.

**Worked computation table**

| Item | Standard tariff | SME priority tariff (15% above 1.5× МРОТ) |
| --- | --- | --- |
| Gross wage | 100,000 ₽ | 100,000 ₽ |
| НДФЛ (13%, withheld) | −13,000 ₽ | −13,000 ₽ |
| **Net to employee** | **87,000 ₽** | **87,000 ₽** |
| Единый тариф | 30% × 100,000 = **30,000 ₽** | 30% × 40,639.50 + 15% × 59,360.50 = 12,191.85 + 8,904.08 = **21,095.93 ₽** |
| Взносы на травматизм (0.2%) | 200 ₽ | 200 ₽ |
| **Employer contributions total** | **30,200 ₽** | **21,295.93 ₽** |
| **Total employer cost** (gross + contributions) | **130,200 ₽** | **121,295.93 ₽** |

- **НДФЛ vs employer cost note** — Note: НДФЛ is part of the gross and does NOT add to employer cost — it is the employee's tax, merely withheld and remitted by the employer. Total employer cash outlay = gross + страховые взносы + травматизм.

## 4. Reporting & Payment Calendar

All НДФЛ and единый-тариф money flows through the **ЕНП / ЕНС** (единый налоговый платёж / единый налоговый счёт): the employer tops up its ЕНС, files **уведомления об исчисленных суммах** so the ФНС knows how to allocate the money, and the ФНС debits the tax. Травматизм is paid separately to the **СФР** (not through ЕНС).

### 4.1 Payment deadlines

**Payment deadlines table**

| Obligation | Deadline (2026) |
| --- | --- |
| НДФЛ withheld 1st–22nd of a month | **28th** of the same month |
| НДФЛ withheld 23rd–end of month | **5th** of the next month |
| НДФЛ withheld 23–31 December | **last working day of the year** |
| **Единый тариф** (страховые взносы) | **28th** of the next month |
| **Взносы на травматизм** (to СФР) | **15th** of the next month |
| Уведомление по НДФЛ / по взносам | by the **25th** (per the relevant period) |

(From 1 September 2026, an optional consolidated уведомление covering several months at once becomes available — verify and use only if helpful.)

### 4.2 Reporting deadlines

**Reporting deadlines table**

| Report | Sent to | Period / due date (2026) |
| --- | --- | --- |
| **6-НДФЛ** | ФНС | Quarterly, by the **25th** of the month after the quarter; annual by **25 February** of the next year |
| **РСВ** (расчёт по страховым взносам) | ФНС | Quarterly — Q1 by **27 Apr**, half-year by **27 Jul**, 9 months by **26 Oct**, annual by **25 Feb 2027** (a new РСВ form applies from Q2 2026 — verify) |
| **Персонифицированные сведения о физлицах** | ФНС | Monthly, by the **25th** of the next month (the 3rd month of each quarter may be omitted — verify) |
| **ЕФС-1, раздел 2** (травматизм) | СФР | Quarterly, by the **25th** of the month after the quarter |
| **ЕФС-1** personnel subsections (подраздел 1.1 — hire/fire/transfer events) | СФР | Hire/termination: **next working day**; other personnel events: by the **25th** of the next month — verify |

- **Weekend/holiday deadline shift** — When a deadline falls on a weekend or holiday it moves to the next working day. Confirm the exact 2026 calendar dates against the ФНС/СФР production calendar before filing.

## 5. Employee vs Самозанятый (Misclassification)

A frequent question is whether to engage workers as **самозанятые (НПД)** or on a **договор ГПХ** instead of as employees, to avoid НДФЛ withholding and страховые взносы. See **ru-self-employed-npd** for the НПД regime mechanics. The payroll-side rules:

- **Genuine самозанятый supplier:** the engaging business pays NO НДФЛ and NO страховые взносы on the payment (the самозанятый pays their own 6%/4% НПД tax and issues a чек from «Мой налог»). This is legitimate ONLY for genuinely independent, project-based services.
- **Misclassification (подмена трудовых отношений):** if the relationship has the hallmarks of employment — fixed schedule, integration into the team, employer's tools/premises, a single ongoing «client», monthly fixed pay, subordination — the ФНС can **reclassify** it as employment. Consequences: assessment of unpaid **НДФЛ + страховые взносы**, plus penalties (штрафы) and interest (пени), and labour-law liability.
- **Red flags the ФНС tracks:** a former employee re-engaged as самозанятый within ~2 years; the business being the самозанятый's sole or dominant source of income; payroll-like regular monthly amounts; mass conversion of staff to НПД.

**Do not design a scheme to disguise employment as self-employment (R-1).** If the work is genuinely that of an employee, it must be run through payroll.

## 6. Worked Examples

### Example A — Ordinary salary, standard tariff

Company (not SME-priority), one employee, 60,000 ₽/month gross, resident, no deductions, травматизм 0.2%, early in the year. НДФЛ at 13%.

- НДФЛ = 13% × 60,000 = **7,800 ₽** (withheld) → **net 52,200 ₽**.
- Единый тариф = 30% × 60,000 = **18,000 ₽**.
- Травматизм = 0.2% × 60,000 = **120 ₽**.
- **Employer cost = 60,000 + 18,000 + 120 = 78,120 ₽/month.**

### Example B — SME priority-sector, same wage

Same 60,000 ₽ gross, but the employer is in the реестр МСП with a qualifying priority ОКВЭД and the 70% test met. 1.5× МРОТ = 40,639.50 ₽.

- НДФЛ unchanged = **7,800 ₽** → **net 52,200 ₽**.
- Единый тариф = 30% × 40,639.50 + 15% × (60,000 − 40,639.50) = 12,191.85 + 2,904.08 = **15,095.93 ₽**.
- Травматизм = **120 ₽**.
- **Employer cost = 60,000 + 15,095.93 + 120 = 75,215.93 ₽/month** — about 2,904 ₽/month cheaper than the standard tariff for this wage.

### Example C — Crossing the предельная база mid-year (standard tariff)

High earner, 300,000 ₽/month gross, standard tariff. Cumulative wage reaches the предельная база of 2,979,000 ₽ during month 10 (10 × 300,000 = 3,000,000 ₽; the база is hit at 2,979,000 ₽).

- For months 1–9 (cumulative 2,700,000 ₽, still ≤ база): единый тариф = 30% × 300,000 = 90,000 ₽/month.
- Month 10: of the 300,000 ₽, the part up to the база (2,979,000 − 2,700,000 = 279,000 ₽) is at 30% = 83,700 ₽; the remaining 21,000 ₽ is at 15.1% = 3,171 ₽ → **86,871 ₽** for month 10.
- Months 11–12: entire 300,000 ₽ at 15.1% = **45,300 ₽/month**.
- НДФЛ also steps up: cumulative income crosses 2,400,000 ₽ in month 8, so income above that point is taxed at **15%** (each band at its own rate). Compute cumulatively.

### Example D — Crossing the НДФЛ 2.4M threshold

Employee, 250,000 ₽/month gross, resident. By month 10 cumulative income = 2,500,000 ₽.

- Months 1–9: cumulative 2,250,000 ₽ — all within the 13% band → НДФЛ 32,500 ₽/month.
- Month 10: cumulative reaches 2,500,000 ₽. The first 150,000 ₽ of month 10 fills the band up to 2,400,000 ₽ at 13% (19,500 ₽); the remaining 100,000 ₽ is at 15% (15,000 ₽) → **34,500 ₽** НДФЛ.
- Months 11–12: entire 250,000 ₽ at 15% = **37,500 ₽/month**.
  Net to employee falls accordingly once the higher band applies.

## 7. Tier 2 Considerations, References, Test Suite

### 7.1 Tier 2 — judgement calls requiring a professional

- **Reduced-tariff eligibility** — confirming a specific ОКВЭД is on the 2026 priority list, the 70% test, and the correct tariff code (e.g. «32») on the РСВ. Verify with the official list.
- **IT / special regimes** — accredited IT companies, Сколково residents, and special-economic-zone residents may use 7.6% or 0% tariffs under separate rules. Out of this skill's default scope.
- **Деньги ГПХ contracts** — травматизм applies to a ГПХ contract only if the contract expressly provides for it; the единый тариф and НДФЛ generally still apply. Read each contract.
- **Director without salary / sole-owner-director** — reporting nuances (РСВ, ПСВ) changed for 2026; verify whether minimum-wage accruals and reports are required.
- **Deductions (вычеты)** — child, standard, social, and property deductions reduce the НДФЛ base; their correct application is fact-specific.
- **Regional МРОТ and coefficients** — some regions set a higher minimum wage; northern coefficients add to the wage and to the contribution base.

### 7.2 References (verify before relying)

- **References list** — **ФНС** — nalog.gov.ru — НДФЛ, страховые взносы, единый тариф, предельная база, РСВ, 6-НДФЛ, персонифицированные сведения, ЕНС/ЕНП. **СФР** — sfr.gov.ru — взносы на травматизм, ЕФС-1, hazard-class assignment. **Налоговый кодекс РФ** — гл. 23 (НДФЛ), гл. 34 (страховые взносы, ст. 419–432, ст. 425, ст. 427). **Law No. 429-ФЗ (28.11.2025)** — МРОТ 27,093 ₽ from 1 Jan 2026. **Law No. 434-ФЗ (28.11.2025)** — травматизм tariffs for 2026. **Government Decree No. 4125-р (27.12.2025)** — 2026 SME priority-sector list. **Предельная база 2026** — единая предельная величина 2,979,000 ₽ (Government Decree; confirmed by ФНС). Related skills: **ru-social-contributions** (ИП «за себя»), **ru-self-employed-npd** (НПД), **ru-usn**, **ru-income-tax**.  _(nalog.gov.ru; sfr.gov.ru; Налоговый кодекс РФ гл.23, гл.34; Law No. 429-ФЗ (28.11.2025); Law No. 434-ФЗ (28.11.2025); Government Decree No. 4125-р (27.12.2025))_

### 7.3 Test suite (self-check before producing output)

1. Did I treat НДФЛ as **withheld from gross** (employee's tax), not as an addition to employer cost? ✔
2. Did I apply the **единый тариф and травматизм ON TOP of** gross as employer cost? ✔
3. Did I track НДФЛ bands and the предельная база **cumulatively from the start of the year**? ✔
4. Did I **default to the standard 30%/15.1% tariff** unless SME priority eligibility was documented? ✔
5. Did I keep the **1.5× МРОТ split MONTHLY** for the SME tariff and the **предельная база ANNUAL** for the standard tariff (two different mechanics)? ✔
6. Did I name the right report for each obligation (6-НДФЛ, РСВ, перс. сведения to ФНС; ЕФС-1 to СФР)? ✔
7. Did I route НДФЛ and единый тариф through **ЕНС/ЕНП** but травматизм **separately to СФР**? ✔
8. Did I flag any figure I could not re-verify with "verify current value"? ✔
9. Did I refuse misclassification schemes (R-1) and non-resident payroll (R-2)? ✔
10. Did I tell the user that an accountant must sign off before filing? ✔

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT design or endorse misclassification.** Never structure ongoing employees as самозанятые (НПД) or договор ГПХ to dodge НДФЛ or страховые взносы (R-1). - **Do NOT assume a reduced tariff.** Never apply the 15% SME, 7.6%, or 0% tariff without documented eligibility (реестр МСП, qualifying primary ОКВЭД, 70% test, or the relevant special regime). Default to 30% / 15.1%. - **Do NOT file or submit anything.** This skill computes and explains; it does not transmit 6-НДФЛ, РСВ, ЕФС-1, уведомления, or payments to the ФНС or СФР. - **Do NOT treat НДФЛ as an employer add-on cost** or страховые взносы as withheld from the employee — they are economically opposite flows. - **Do NOT rely on a figure without checking it for the current period.** МРОТ, the предельная база, НДФЛ thresholds, the травматизм table, and the priority-sector list change by law. - **Do NOT handle non-resident, foreign-worker, hazardous-work, or northern-coefficient payroll** here — refer those to a specialist (R-2, R-3). - **Do NOT give a final position without qualified human sign-off.**

## Disclaimer

This skill is **research-verified** against ФНС (nalog.gov.ru), СФР, and reputable Russian payroll sources for tax year 2026, but it is **pending sign-off by a qualified Russian accountant**. Russian payroll, tax, and contribution rules — including МРОТ, the единая предельная база, the progressive НДФЛ thresholds, the травматизм tariff table, the SME priority-sector list, and report forms and deadlines — change frequently and by law. Always re-verify current figures at nalog.gov.ru and sfr.gov.ru, and have a credentialed Russian accountant or payroll specialist review every computation and return before it is filed or relied upon. Provided for educational purposes by openaccountants.com; not a substitute for professional advice.

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
