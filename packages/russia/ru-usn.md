---
name: ru-usn
description: Use this skill whenever asked about the Russian simplified taxation system (УСН / Упрощённая система налогообложения) for individual entrepreneurs (ИП) and small organisations — choosing between the «Доходы» (6%) and «Доходы минус расходы» (15%) objects, regional reduced rates, eligibility limits, the minimum tax, the 2025+ reform making УСН payers liable for VAT (НДС), the КУДиР ledger, quarterly advance payments, the annual declaration, and страховые взносы offset. Trigger on phrases like "УСН", "simplified tax Russia", "ИП 6%", "доходы минус расходы", "USN Russia", "ИП налоги", "упрощёнка", "минимальный налог УСН", "НДС на УСН", or any request to compute or review УСН tax for a self-employed person or small business in Russia. The AI replies in the user's own language.
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

# RU Usn

## Russia — Упрощённая система налогообложения (УСН) for ИП and Small Business

The **УСН** (*Упрощённая система налогообложения*, "simplified taxation system") is the default tax regime for most small Russian businesses. It replaces, for a single flat tax, the personal income tax on business profit (НДФЛ for ИП / налог на прибыль for organisations) and — historically — VAT (НДС). The 2025 tax reform broke that last link: from 2026 a УСН payer above a turnover threshold is **also a VAT payer**. This skill covers УСН for **individual entrepreneurs (ИП — индивидуальный предприниматель)** and small organisations.

**Related skills.** For freelancers below ~2.4M ₽/year with no employees and no resale of goods, the **НПД** regime (*налог на профессиональный доход*, the "self-employed" / самозанятый tax at 4%/6%) is usually simpler and cheaper — see **ru-self-employed-npd**. For the fixed and 1%-over-300k insurance contributions an ИП always owes, see **ru-social-contributions**.

> **YMYL notice.** Russian tax law changed substantially for 2026 (Federal Law 425-ФЗ of 28.11.2025; deflator order Минэкономразвития 734 of 06.11.2025). All figures below are research-verified against ФНС, КонсультантПлюс, Гарант and major accounting publishers as of May 2026. Where a value is annually indexed, the formula is given so you can re-verify the current value. **Always confirm against nalog.gov.ru before filing.**

## 1. Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Russian Federation (RU) |
| Tax | УСН — 6% («Доходы») / 15% («Доходы минус расходы») |
| Currency | Russian rouble (RUB, ₽) |
| Legislation | Налоговый кодекс РФ, глава 26.2 (Articles 346.11–346.25) |
| VAT-on-УСН legislation | НК РФ глава 21; Federal Law 176-ФЗ (2024), 425-ФЗ (28.11.2025) |
| Authority | ФНС (Федеральная налоговая служба) — nalog.gov.ru |
| Portal | Личный кабинет налогоплательщика (lkfl2.nalog.ru for individuals; lkul.nalog.ru for organisations); filing via certified ЭДО operators |
| Ledger | КУДиР (Книга учёта доходов и расходов) |
| Advance payments | Quarterly: Q1 by 28 Apr, H1 by 28 Jul, 9M by 28 Oct |
| Annual declaration & final tax | ИП — by 25 April (final tax by 28 April); organisations — declaration & tax by 25/30 March of the following year |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Russian accountant |
| Version | 1.0 |

### 1.1 Rates (2026)

**Rates (2026)**

| Object | Base rate | Floor (regional) | Tax base |
| --- | --- | --- | --- |
| «Доходы» (income) | **6%** | down to **1%** | gross income received (cash basis) |
| «Доходы минус расходы» (income minus expenses) | **15%** | down to **5%** | income less the closed list of deductible expenses |
| Minimum tax («Доходы минус расходы» only) | **1% of income** | — | paid if the 15% computation is below it (incl. a loss year) |

Note: the старые повышенные ставки (8% / 20%) that applied between the basic and upper turnover limits were **abolished** from 2025. There is now a single flat rate per object up to the УСН ceiling.

### 1.2 Eligibility limits (2026, deflator коэффициент-дефлятор = 1.090, order МЭР 734)

**Eligibility limits**

| Limit | 2026 value | Base × deflator |
| --- | --- | --- |
| Annual income to **stay on** УСН | **490.5M ₽** | 450M × 1.090 |
| 9-month income to **switch to** УСН (organisations) | **337.5M ₽** | 337.5M (not indexed by deflator in the standard reading — *verify current value*) |
| Headcount (average) | **≤ 130** employees | — |
| Fixed assets (остаточная стоимость ОС) | **218M ₽** | 200M × 1.090 |
| VAT (НДС) exemption ceiling — prior-year income | **20M ₽** | statutory (2027: 15M; 2028: 10M) |

- **Breach of limits** — Exceeding the income or asset ceiling, or the headcount limit, causes loss of УСН from the start of the quarter in which the breach occurred.

### 1.3 VAT (НДС) bands for УСН payers (2026)

**VAT bands**

| Prior-year income | VAT status / rate |
| --- | --- |
| ≤ 20M ₽ | Exempt from НДС (освобождение) |
| > 20M and ≤ 272.5M ₽ | **5%** without input-VAT deduction, **or** 22% with deduction |
| > 272.5M and ≤ 490.5M ₽ | **7%** without input-VAT deduction, **or** 22% with deduction |
| Standard rate (with deduction) | **22%** (raised from 20% by 425-ФЗ); 10% applies to socially-significant goods; 0% for exports/qualifying IT |

### 1.4 Conservative defaults

When information is missing, assume the more cautious treatment and flag it:

- **Object unknown** → do not guess; the object is chosen once a year and binds for the whole year. Ask, or model both.
- **Expense not clearly on the закрытый перечень (closed list, ст. 346.16)** → treat as **non-deductible** under «Доходы минус расходы». The list is exhaustive.
- **Expense lacks a primary document / proof of payment** → non-deductible.
- **Income timing** → cash basis: income is recognised when money (or property) is *received*, including advances/предоплата.
- **VAT status near 20M ₽** → if prior-year income is at/above the threshold, default to **VAT payer** and recommend choosing a rate; do not assume exemption.
- **Regional reduced rate claimed** → verify the specific region's law and the activity code (ОКВЭД); from 2026 regions may only reduce rates for activities the federal Government lists.
- **ИП страховые взносы offset** → apply, but cap correctly (see §5.3).

## 2. Choosing «Доходы» 6% vs «Доходы минус расходы» 15%

The two objects tax completely different bases. The choice is made for the whole calendar year and can only be changed from 1 January of the next year (notify ФНС by 31 December).

### 2.1 Break-even logic

- **Break-even formula** — 6% × Income  =  15% × (Income − Expenses) =>  Expenses / Income = 0.60   (i.e. 60%)

Ignoring regional reductions and the взносы offset, the two objects produce the **same** tax when expenses equal a fixed share of income:

- **Expenses < 60% of income** → «Доходы» (6%) is usually cheaper.
- **Expenses > 60% of income** → «Доходы минус расходы» (15%) is usually cheaper.
- **Around 60%** → other factors decide (see below).

This 60% rule is the headline heuristic. Two adjustments matter in practice:

1. **Страховые взносы offset (§5.3) tilts toward «Доходы».** On «Доходы» an ИП *reduces the tax itself* by contributions (in full if no employees, up to 50% with employees). On «Доходы минус расходы» contributions are merely a *deductible expense*, so they save only 15% of their value, not 100%. This pushes the practical break-even **above 60%** — often to roughly 65–70% of income before «Доходы минус расходы» wins, especially for low-income ИП whose tax can be wiped out entirely by the fixed взносы.

2. **The 1% minimum tax (§2.2) sets a floor on «Доходы минус расходы».** A high-cost or loss-making business on the 15% object never pays less than 1% of income.

### 2.2 The minimum tax (минимальный налог) — «Доходы минус расходы» only

- **Minimum tax formula** — Regular tax = 15% × (Income − Expenses) Minimum tax = 1%  × Income УСН due     = max(Regular tax, Minimum tax)  _(ст. 346.18)_
- **Minimum tax carry-forward** — If the minimum tax is higher (a thin-margin or loss year), you pay the minimum tax. The difference (minimum tax paid − regular tax) may be carried forward and added to expenses / loss in later years. The «Доходы» object has no minimum tax.  _(ст. 346.18)_

### 2.3 Practical decision checklist

- Low costs, services, freelancing (consulting, IT done as ИП, design) → **«Доходы» 6%**.
- Trading, manufacturing, anything reselling goods with a thin margin → **«Доходы минус расходы» 15%**, but watch the closed expense list and the 1% floor.
- Strong regional incentive for your activity (rate cut to 1% or 5%) can override the heuristic.
- If income is small enough that fixed взносы exceed the «Доходы» tax, «Доходы» effectively costs **0 ₽** of УСН for an ИП without employees — almost always the winner.

## 3. Eligibility Limits and Refusal Catalogue

### 3.1 Who can use УСН

- **Eligibility conditions** — An ИП or organisation may apply УСН if it stays within the limits in §1.2 and is not on the prohibited-activities list of ст. 346.12 НК РФ (banks, insurers, NPFs, professional securities dealers, pawnshops, gambling, producers of excisable goods other than certain wine/grapes, notaries and advocates in private practice, organisations with branches, organisations where another legal entity owns > 25%, etc.).  _(ст. 346.12 НК РФ)_
- **Notification to start УСН** — To start: file the notification (уведомление о переходе на УСН) within 30 days of registration, or by 31 December to apply УСН from the next year.

### 3.2 Refusal catalogue

**Refusal catalogue**

| Code | Situation | Action |
| --- | --- | --- |
| **R-RU-1** | Income exceeds 490.5M ₽ in 2026 | Loss of УСН from the start of that quarter; move to ОСНО. Out of scope — escalate. |
| **R-RU-2** | Average headcount exceeds 130 | Loss of УСН from that quarter. Escalate. |
| **R-RU-3** | Fixed-asset residual value exceeds 218M ₽ | Loss of УСН (applies to organisations; relevant for ИП too on the asset test). Escalate. |
| **R-RU-4** | Prohibited activity (banking, insurance, gambling, excisable production, etc., ст. 346.12) | УСН not available. Refuse and refer to a practitioner. |
| **R-RU-5** | Organisation has branches, or > 25% owned by another legal entity | УСН not available. Refuse. |
| **R-RU-6** | Client is actually eligible/registered under **НПД** (самозанятый) | Redirect to **ru-self-employed-npd** — usually simpler and cheaper for true freelancers. |
| **R-RU-7** | VAT (НДС) treatment for a payer above 20M ₽ — choosing 5%/7% vs 22%, input-VAT deduction, invoicing | Tier 2: flag and present options; do not auto-decide. See §4. |
| **R-RU-8** | Cross-border transactions, sanctions exposure, EAEU trade, currency control | Out of scope. Escalate — sanctions and currency-control rules dominate. |
| **R-RU-9** | Combining УСН with ПСН (patent), or splitting a business across regimes | Tier 2: anti-fragmentation (дробление бизнеса) risk. Escalate. |
| **R-RU-10** | Whether a specific expense is on the closed list (ст. 346.16) | Tier 2 if not obvious — default to non-deductible and flag. |

## 4. The 2025+ VAT-on-УСН Rules (НДС для упрощенцев)

This is the single biggest change for small business. Until 2024, УСН payers were not VAT payers. From **2025** (Law 176-ФЗ) a УСН payer whose income exceeds the threshold becomes a **НДС payer**. The threshold and rates were further changed for **2026** by **425-ФЗ (28.11.2025)**.

### 4.1 When you become a VAT payer

- **VAT payer trigger** — - Look at prior-year income. For 2026 the exemption ceiling is 20M ₽ (down from 60M ₽ in 2025; falling to 15M in 2027 and 10M in 2028 — verify). - If prior-year (2025) income ≤ 20M ₽ → exempt (освобождение) for 2026, no VAT returns, no VAT invoices. Exemption is automatic; no application is required. - If prior-year income > 20M ₽ → you are a VAT payer from 1 January 2026 and must choose a rate. If you cross 20M ₽ during the year, VAT obligations begin from the 1st of the month following the breach.  _(176-ФЗ; 425-ФЗ (28.11.2025))_

### 4.2 Choosing the rate

**VAT rate options**

| Option | Rate | Input-VAT deduction | Income band (prior year) |
| --- | --- | --- | --- |
| Reduced | **5%** | No (no вычет) | > 20M and ≤ 272.5M ₽ |
| Reduced | **7%** | No (no вычет) | > 272.5M and ≤ 490.5M ₽ |
| Standard | **22%** | Yes (full вычет of input НДС) | any band |

- **5%/7% (без вычетов)** suits businesses with few VAT-bearing purchases (services, labour-heavy work) — you charge a small VAT but cannot reclaim input VAT.
- **22% (с вычетами)** suits businesses with large VAT-bearing purchases for resale/production — the higher output rate is offset by reclaiming input VAT.

### 4.3 Lock-in period

- **12-quarter lock-in** — Once you choose a reduced rate (5% or 7%) or move to 22%, you must apply it for 12 consecutive quarters (3 years) before changing — unless your income falls back below 20M ₽ (exemption) or rises into the next band (5%→7%), which happen automatically. Exception: a payer who chooses a reduced rate for the first time in 2026 may abandon it for 22% within the first 4 quarters of applying it.

### 4.4 Compliance obligations once you are a VAT payer

- **VAT compliance obligations** — - Issue счета-фактуры (VAT invoices) and keep the книга продаж / книга покупок. - File a quarterly VAT declaration electronically by the 25th of the month after the quarter. - Pay VAT in three equal monthly instalments after each quarter. - ФНС published Методические рекомендации по НДС для УСН (2026) — the primary practical reference. Tag all non-trivial VAT-on-УСН questions R-RU-7 (Tier 2) and confirm with a practitioner; see also the russia-vat skill.  _(ФНС Методические рекомендации по НДС для УСН (2026))_

## 5. КУДиР, Advance Payments, and Страховые взносы Offset

### 5.1 КУДиР (Книга учёта доходов и расходов)

- **КУДиР requirements** — Every УСН payer keeps a КУДиР — the tax ledger that supports the declaration. - «Доходы» payers record income only (and, in a separate section, the contributions/payments that reduce the tax). - «Доходы минус расходы» payers record both income and the closed-list expenses, each with a primary document and proof of payment. - It may be kept electronically and is not filed routinely, but ФНС can demand it on audit. - Cash basis throughout: income on receipt (including advances), expenses when both incurred and paid.

### 5.2 Advance payments and the annual declaration

- **Advance payment cadence** — УСН is paid in quarterly advance payments computed on a cumulative (year-to-date) basis, then trued up at year end.

**Advance payment schedule**

| Period | Pay advance by | Уведомление (notification) by |
| --- | --- | --- |
| Q1 (Jan–Mar) | 28 April | 25 April* |
| H1 (Jan–Jun) | 28 July | 25 July* |
| 9M (Jan–Sep) | 28 October | 25 October* |
| Year — ИП | final tax 28 April; **declaration by 25 April** | — |
| Year — organisations | tax & **declaration by 25 March** (commonly cited 30 March) | — |

- **ЕНП/ЕНС notification mechanic** — *Because УСН is paid through the ЕНП / ЕНС (единый налоговый платёж / счёт, the single tax account), a уведомление об исчисленных суммах must be filed by the 25th before each advance so ФНС allocates the money. When the 25th/28th falls on a weekend it shifts to the next working day (e.g. several 2026 dates land on 27/28 of the month — verify the exact calendar).

### 5.3 Страховые взносы offset (the big lever for ИП)

- **Insurance contributions overview** — An ИП always pays fixed insurance contributions за себя plus 1% on income over 300,000 ₽ (see ru-social-contributions for the mechanics). 2026 figures: - Fixed contribution (full year): 57,390 ₽ — verify current value. - Additional contribution: 1% × (income − 300,000 ₽), capped at 321,818 ₽ for 2026. - Combined maximum: 379,208 ₽ (57,390 + 321,818) — verify. - Deadlines: fixed part by 28 December 2026; the 1% part by 1 July 2027.

**How contributions reduce УСН**

| Object | Effect of страховые взносы |
| --- | --- |
| **«Доходы»** — ИП **without** employees | Reduce the УСН tax itself **by up to 100%** (tax can go to 0). From 2023 the fixed взносы reduce the tax for the year they relate to even if not yet paid (подлежащие уплате). |
| **«Доходы»** — ИП **with** employees / organisation | Reduce the УСН tax by **no more than 50%**. |
| **«Доходы минус расходы»** | Contributions are a **deductible expense**, not a tax credit — they cut the base, saving only 15% of their value. |

## 6. Worked Examples

### Example 1 — «Доходы» 6%, ИП, no employees (the взносы wipeout)

IT freelancer ИП, 2026 income 2,000,000 ₽, no employees.

- УСН before offset: 6% × 2,000,000 = 120,000 ₽.
- Fixed взносы 57,390 ₽ + 1% over 300k = 1% × (2,000,000 − 300,000) = 17,000 ₽ → total contributions 74,390 ₽.
- «Доходы» ИП without employees reduces the tax by contributions in full: 120,000 − 74,390 = 45,610 ₽ УСН for the year.
- Compare НПД (ru-self-employed-npd): at 6% on B2B income this would be ~120,000 ₽ tax but with no separate insurance contributions — for some clients НПД is still cheaper. Model both.

### Example 2 — break-even, «Доходы» vs «Доходы минус расходы»

Trader, income 10,000,000 ₽, expenses 6,500,000 ₽ (65% of income), no employees.

- «Доходы»: 6% × 10,000,000 = 600,000 ₽; less взносы (57,390 + 1%×9,700,000 = 97,000 → 154,390 ₽) → 445,610 ₽.
- «Доходы минус расходы»: 15% × (10,000,000 − 6,500,000) = 15% × 3,500,000 = 525,000 ₽ (contributions already in the 6.5M expenses). Check minimum tax: 1% × 10,000,000 = 100,000 ₽ < 525,000 → regular tax stands.
- Despite expenses being above the 60% rule, «Доходы» wins here once the взносы offset is applied — illustrating why the practical break-even sits higher than 60%.

### Example 3 — minimum tax (loss year), «Доходы минус расходы»

Manufacturer, income 8,000,000 ₽, expenses 7,800,000 ₽.

- Regular tax: 15% × (8,000,000 − 7,800,000) = 15% × 200,000 = 30,000 ₽.
- Minimum tax: 1% × 8,000,000 = 80,000 ₽.
- Pay max(30,000, 80,000) = 80,000 ₽. The difference 80,000 − 30,000 = 50,000 ₽ is carried forward into next year's expenses/loss.

### Example 4 — crossing the VAT threshold

ИП on «Доходы», 2025 income 35,000,000 ₽ (above 20M ₽), continues УСН in 2026.

- Because prior-year income > 20M ₽, the ИП is a VAT payer from 1 Jan 2026.
- Income is in the 20M–272.5M band → choose 5% without deduction or 22% with deduction.
- A services business with few VAT-bearing inputs would normally pick 5%, charge 5% НДС to customers, file quarterly VAT returns, and lock in for 12 quarters. Flag R-RU-7 (Tier 2) and confirm with a practitioner.

### Example 5 — regional reduced rate

ИП in a region that set a 1% «Доходы» rate for IT activity (valid ОКВЭД, federal Government's permitted-activity list).

- Income 4,000,000 ₽ → УСН = 1% × 4,000,000 = 40,000 ₽ before offset.
- Fixed + 1% взносы (57,390 + 37,000 = 94,390 ₽) exceed the tax → УСН = 0 ₽ (ИП without employees). Verify the regional law and that the activity is on the permitted list, since from 2026 regions may only reduce rates for federally-listed activities.

## 7. Tier 2 — Issues Requiring Reviewer Judgement

Flag and escalate (do not auto-decide) when any of these arise:

- **VAT-on-УСН choice** (5% / 7% / 22%, input-VAT deduction, transitional contracts, advances across the rate change) — R-RU-7. Heavy reliance on ФНС Методические рекомендации 2026.
- **Loss of УСН mid-year** from breaching income/headcount/asset limits — recomputation under ОСНО from the start of the breach quarter — R-RU-1/2/3.
- **Closed-list expense disputes** (ст. 346.16) — whether a specific cost is deductible at all.
- **Дробление бизнеса** (business fragmentation / splitting to stay under limits) — major audit and criminal-liability risk — R-RU-9.
- **Combining УСН with ПСН** (patent) and apportioning income, headcount and assets.
- **Switching object** «Доходы» ↔ «Доходы минус расходы» and the timing/notification.
- **Cross-border, EAEU, currency control, sanctions** — R-RU-8, out of scope.
- **First-year and short-period** returns; transition in/out of НПД.

Always require sign-off by a qualified Russian accountant before filing.

## 8. Bank Statement Reading Guide (Russian banks) + Reference + Test Suite

### 8.1 Reading Russian bank statements (выписка по счёту)

- **Bank statement reading guidance** — УСН is cash basis, so the расчётный счёт (current account) statement is the primary source for income. Major banks: Сбербанк, Тинькофф (Т-Банк), Альфа-Банк, ВТБ, Точка, Модульбанк. Statement columns to expect: - Дата операции — transaction date (income recognised here, on receipt). - Назначение платежа — narrative; the key field for classification. Look for "оплата по договору", "за услуги", "аванс/предоплата" (advances are income on receipt), "возврат" (a refund — reverses income, not income). - Сумма with Дебет / Кредит — кредит (incoming) is income; дебет (outgoing) may be a deductible expense (15% object only) or a non-business transfer. - В том числе НДС — whether the line includes VAT; relevant once the ИП is a VAT payer. - Контрагент / ИНН — counterparty and its ИНН. Classification cautions: - Own-funds top-ups ("пополнение счёта", "внесение собственных средств") are not income. - Loans received / returned are not income / not expense. - Transfers between the ИП's own accounts are not income. - Refunds to customers (возврат) reduce income. - Personal card spending by an ИП is generally not a business expense unless it is a closed-list business cost with documents — default non-deductible and flag. - Acquiring/эквайринг settlements: income is the gross sale, with the bank's commission as a separate (deductible, 15% object) expense — do not net them.

### 8.2 Reference (research-verified, May 2026)

- НК РФ, глава 26.2 «Упрощённая система налогообложения» (ст. 346.11–346.25).
- НК РФ, глава 21 «Налог на добавленную стоимость» (VAT-on-УСН).
- Federal Law 176-ФЗ (2024) and 425-ФЗ of 28.11.2025 (VAT rate to 22%, УСН VAT thresholds).
- Приказ Минэкономразвития от 06.11.2025 № 734 (коэффициент-дефлятор 1.090 for 2026).
- ФНС России — nalog.gov.ru; Методические рекомендации по НДС для УСН 2026.
- ФНС "Налоги 2026" hub; КонсультантПлюс, Гарант, Главбух, Контур.Экстерн (cross-checks).

Фигуры flagged "verify current value": the 9-month transition limit (337.5M ₽), the 2026 fixed страховые взносы (57,390 ₽) and the 1% cap (321,818 ₽) / combined max (379,208 ₽), the 2027/2028 step-downs of the VAT exemption ceiling, and the exact weekend-shifted 2026 advance dates. These move annually or by sub-regulation — re-verify on nalog.gov.ru before relying.

### 8.3 Test suite (sanity checks)

**Test suite**

| # | Input | Expected |
| --- | --- | --- |
| T1 | «Доходы», income 1,000,000 ₽, no expenses, no employees, взносы 67,390 ₽ | УСН 60,000 − 67,390 → **0 ₽** (offset capped at the tax) |
| T2 | «Доходы минус расходы», income 5,000,000 ₽, expenses 4,950,000 ₽ | Regular 7,500 ₽ vs minimum 50,000 ₽ → **pay 50,000 ₽**, carry 42,500 ₽ |
| T3 | Expenses = 60% of income, no взносы | 6% and 15% objects give the **same** tax (break-even) |
| T4 | 2025 income 25,000,000 ₽, continues УСН 2026 | **VAT payer** from 1 Jan 2026; choose 5% or 22%; flag R-RU-7 |
| T5 | Income 600,000,000 ₽ in 2026 | **R-RU-1** — exceeds 490.5M ₽, loses УСН; escalate |
| T6 | Bank line "внесение собственных средств 200,000 ₽" | **Not income** — exclude |
| T7 | True freelancer, 1.5M ₽, no employees, no goods resale | Suggest **НПД** (ru-self-employed-npd) as likely cheaper; model both |

## PROHIBITIONS

- Do not file or submit any УСН or НДС declaration, уведомление, or payment to ФНС on the taxpayer's behalf. Prepare figures only; the taxpayer/practitioner files.
- Do not decide the VAT rate (5% / 7% / 22%) automatically — it is a 3-year lock-in; present options and require practitioner sign-off (R-RU-7).
- Do not treat an expense as deductible under «Доходы минус расходы» unless it is on the closed list of ст. 346.16 and has a primary document and proof of payment.
- Do not advise splitting a business across ИП/regimes to stay under limits — дробление бизнеса carries audit and criminal risk (R-RU-9).
- Do not opine on cross-border, EAEU, currency-control, or sanctions matters (R-RU-8) — out of scope.
- Do not present any annually-indexed figure as final without re-verifying against nalog.gov.ru for the current period.
- Do not assume VAT exemption for a payer whose prior-year income is at or above 20M ₽.

## Disclaimer

This skill is research-verified against ФНС (nalog.gov.ru), Federal Laws 176-ФЗ and 425-ФЗ, the 2026 deflator order, and reputable Russian tax publishers, as of May 2026. It is pending sign-off by a qualified Russian accountant (бухгалтер / налоговый консультант) and is not a substitute for professional advice. Russian tax law — especially the 2025–2028 VAT-on-УСН reform — changes frequently and figures are indexed annually; always confirm current values and your specific facts with a credentialed Russian practitioner before filing. Provided by the Open Accountants Community — openaccountants.com.

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
