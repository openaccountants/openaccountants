---
name: ru-social-contributions
description: Use this skill whenever asked about insurance contributions (страховые взносы) in Russia for self-employed people — individual entrepreneurs (ИП) and the self-employed (самозанятые / НПД). Covers the ИП fixed annual contribution «за себя», the additional 1% on income over 300,000 ₽, payment deadlines, the НПД exemption, how страховые взносы reduce УСН and ОСНО tax, and employer contributions when an ИП hires staff. Trigger on phrases like "страховые взносы", "insurance contributions Russia", "ИП за себя", "fixed contributions Russia", "1% over 300000", "взносы свыше 300000", "единый тариф", "пониженный тариф МСП", "do self-employed pay social contributions in Russia".
version: 1.0
jurisdiction: RU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RU Social Contributions

## Russia — Insurance Contributions (страховые взносы) for the Self-Employed (2026)

This skill explains страховые взносы — Russia's mandatory pension (пенсионное) and medical (медицинское) insurance contributions — as they apply to self-employed individuals in 2026. The two relevant populations are very different:

- **ИП (индивидуальный предприниматель)** — sole proprietor. Pays **fixed contributions «за себя»** plus a **1% additional pension contribution** on income above 300,000 ₽, regardless of the tax regime used for income tax (УСН, ОСНО, ПСН, ЕСХН).
- **Самозанятый (НПД — налог на профессиональный доход)** — registered under the professional-income-tax regime. **Exempt** from mandatory страховые взносы; may pay voluntarily.

The administering bodies are the **ФНС** (Федеральная налоговая служба — collects via the Единый налоговый счёт / ЕНС) and the **СФР** (Социальный фонд России — pension/social records, voluntary schemes). Read alongside **ru-usn**, **ru-income-tax**, and **ru-payroll**.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Russia (RU) |
| Contribution | Страховые взносы (mandatory pension + medical insurance) |
| Fixed amount 2026 (ИП «за себя») | **57,390 ₽** for the calendar year (combined ОПС + ОМС, single non-itemised payment) |
| +1% over 300k ₽ | **1%** of annual income exceeding 300,000 ₽, pension only (ОПС) |
| Cap on the 1% part (2026) | **321,818 ₽** maximum for the 1% portion |
| Maximum total 2026 | 57,390 + 321,818 = **379,208 ₽** |
| Currency | RUB (₽) |
| Legislation | Налоговый кодекс РФ, глава 34 (ст. 419–432); fixed amount in ст. 430 |
| Authority | ФНС (collection via ЕНС/ЕНП) + СФР (records, voluntary schemes) |
| Deadlines | Fixed part: **28 December 2026**; 1% part: **1 July 2027** |
| Self-employed (НПД) | **Exempt** from mandatory contributions (voluntary pension/social only) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Russian accountant |
| Version | 1.0 |

### Conservative defaults

When information is missing, assume the position that results in the **higher** contribution or the **safer** filing, and flag the assumption:

1. **Assume registration = liability.** A registered ИП owes the full fixed amount even with **zero income** and even if the business is dormant, unless a statutory exemption period applies (see §3). Do not assume an exemption — require documentary proof.
2. **Assume the 1% is owed** whenever annual income may exceed 300,000 ₽; compute it and cap it at 321,818 ₽.
3. **Income base for the 1% varies by regime** (see §2). If the regime is unknown, ask; do not guess, because the base differs materially between УСН «доходы», УСН «доходы минус расходы», and ОСНО.
4. **Verify current-year figures before filing.** The fixed amount, the 1% cap, the единая предельная база, and МРОТ are reset annually by law. Figures here are 2026 values verified against ФНС; re-verify at nalog.gov.ru before relying on them.
5. **НПД exemption is conditional.** If the person also holds active ИП status NOT on НПД, the ИП rules apply. Confirm the exact regime.

## 2. ИП Fixed «за себя» + 1% — Computation

### 2.1 The fixed part (фиксированный платёж)

- **2026 fixed amount** — 57,390 ₽  _(ст. 430 НК РФ)_

Every ИП pays a **single fixed contribution** for the year covering both обязательное пенсионное страхование (ОПС) and обязательное медицинское страхование (ОМС). Since 2023 this is one combined figure, not split into separate pension/medical line items by the payer.

- **2026 fixed amount: 57,390 ₽** (ст. 430 НК РФ).
- For reference, the figure was 49,500 ₽ (2024) and 53,658 ₽ (2025); it rises each year by law — *verify current value*.
- Payable in full even at zero income (subject to §3 exemptions).
- If the ИП is registered or deregistered part-way through the year, the fixed amount is **prorated** by the number of full months plus the part-month proportion of days.

### 2.2 The additional 1% (взнос с дохода свыше 300 000 ₽)

- **1% contribution formula** — 1% contribution = (annual income − 300,000 ₽) × 1% capped at 321,818 ₽ for 2026   (verify current value)

On top of the fixed part, an ИП pays **1% of annual income exceeding 300,000 ₽**, credited to pension insurance (ОПС) only.

The **"income"** base depends on the income-tax regime (see table). Cross-check the regime-specific base with **ru-usn** and **ru-income-tax**.

**Income base for the 1% by regime**

| Regime | Income base for the 1% |
| --- | --- |
| УСН «доходы» | Gross income (доходы) |
| УСН «доходы минус расходы» | Income **минус** expenses (доходы − расходы) — confirmed; expenses are deductible for the 1% base |
| ОСНО (НДФЛ) | Income minus professional deductions (профессиональные вычеты), i.e. the НДФЛ taxable base |
| ПСН (патент) | Potential annual income (потенциально возможный доход) per the patent, not actual receipts |
| ЕСХН | Income minus expenses |

### 2.3 Worked figure

ИП on УСН «доходы», 2026 income = 2,000,000 ₽:

```
Fixed part                = 57,390 ₽
1% part = (2,000,000 − 300,000) × 1% = 17,000 ₽   (below the 321,818 cap)
Total страховые взносы    = 57,390 + 17,000 = 74,390 ₽
```

### 2.4 Hitting the cap

- **Cap threshold formula** — 300,000 + (321,818 / 0.01) = 300,000 + 32,181,800 = 32,481,800 ₽ of income

The 1% part is capped at **321,818 ₽** (2026). The cap is reached at the formula above.

Above ~32.48 M ₽ of income, the 1% part stays fixed at 321,818 ₽, so total contributions never exceed **379,208 ₽** in 2026.

### 2.5 Deadlines (ст. 432 НК РФ)

- **Fixed part deadline** — Fixed part (57,390 ₽): by 28 December 2026. If the 28th is a weekend/holiday, the deadline rolls to the next working day — verify the calendar for the year.  _(ст. 432 НК РФ)_
- **1% part deadline** — 1% part: by 1 July of the following year (1 July 2027 for income year 2026).  _(ст. 432 НК РФ)_

Paid via the **Единый налоговый счёт (ЕНС)** as a Единый налоговый платёж (ЕНП); the ФНС allocates it. Since 2023 no separate payment notice (уведомление) is required for the fixed взносы of an ИП «за себя».

## 3. Exemptions and Non-Active Periods

### 3.1 Самозанятые (НПД) — exempt

- **НПД exemption** — Individuals on **НПД** (налог на профессиональный доход), including ИП who switched to НПД, are **exempt** from mandatory страховые взносы. Consequences: - They pay **no fixed contribution and no 1%**. - They accrue **no pension stage (страховой стаж)** and **no pension points (ИПК)** unless they pay voluntarily.
- **Voluntary pension (добровольное ОПС) minimum annual contribution** — 22% × 12 × МРОТ; with the 2026 МРОТ of 27,093 ₽ this is ≈ 71,525.52 ₽ for a full year of stage — verify current value

**New for 2026:** a voluntary social-insurance experiment for НПД payers (temporary incapacity / sickness benefit) runs **1 Jan 2026 – end 2028**. Optional; flag as a planning point, not a default.

### 3.2 Льготные периоды — exempt periods for ИП (ст. 430 п. 7 НК РФ)

- **Exempt periods list** — A registered ИП may suspend the fixed contribution for documented periods of no business activity, including: - Military conscription service (военная служба по призыву). - Care for a child up to 1.5 years (отпуск по уходу за ребёнком до 1,5 лет). - Care for a disabled person of group I, a disabled child, or a person aged 80+. - Periods living with a military-service spouse, or abroad with a diplomatic/consular spouse, where employment was impossible. Requirements: the ИП must **carry on no business activity** during the period and must file an **application with supporting documents** to the ФНС. Income earned in the period defeats the exemption. **Conservative default:** do not apply an exemption without proof.  _(ст. 430 п. 7 НК РФ)_

### 3.3 No general "low income" or "loss" exemption

- **No loss/dormancy exemption** — A loss-making or dormant-but-registered ИП still owes the **full fixed part**. The only way to stop the обязанность is **deregistration** (снятие с учёта) or a §3.2 льготный период.

## 4. Offset Against УСН / ОСНО Tax

Страховые взносы «за себя» **reduce income tax**, which is the main reason to compute them precisely. Coordinate with **ru-usn** and **ru-income-tax**.

### 4.1 УСН «доходы» (6%)

- **Tax reduction without employees** — ИП without employees: reduce the tax / advance payments by up to 100% of the contributions «за себя» (fixed + 1%). The tax can be reduced to zero.
- **Tax reduction with employees** — ИП with employees: reduce by contributions for self and for employees, but no more than 50% of the tax.
- **2026 rule (важно)** — The reduction is taken on contributions due for the period (подлежащие уплате в данном году) — actual payment date is not required to claim the reduction. The 1% for 2025 income (due 1 July 2026) and the 1% for 2026 income (due 1 July 2027) may be claimed in the year they fall due — verify the exact current-year transitional rule with ru-usn before filing.

### 4.2 УСН «доходы минус расходы» (15%)

- **Contributions as expenses** — Contributions «за себя» (and for employees) are included in expenses (расходы), lowering the taxable base — not a direct credit against the tax. No 50% cap (it is an expense, not a tax credit).

### 4.3 ОСНО (НДФЛ)

- **Professional deductions** — Contributions «за себя» are part of professional deductions (профессиональные вычеты) under НДФЛ, reducing the taxable base for personal income tax.

### 4.4 ПСН (патент)

- **Patent cost reduction** — The patent cost may be reduced by contributions «за себя» (and employees') on the same logic as УСН «доходы»: 100% without employees, 50% with employees, via a уведомление об уменьшении.

## 5. Employer Contributions When an ИП Hires Staff

When an ИП employs people, it becomes a **страхователь** and pays страховые взносы **on employee wages** in addition to its own «за себя» contributions. These are governed by the **единый тариф** (unified tariff) on the **единая база** (unified contribution base). See **ru-payroll** for full payroll mechanics.

### 5.1 Единый тариф and единая предельная база (2026)

**Единый тариф and единая предельная база (2026)**

| Item | 2026 value |
| --- | --- |
| Единая предельная база (per employee, per year) | **2,979,000 ₽** (*verify current value*) |
| Standard unified tariff up to the base | **30%** |
| Tariff above the base | **15.1%** |
| Coverage | ОПС + ОМС + ВНиМ (temporary incapacity & maternity) combined |

- **Combined rate structure** — The 30% / 15.1% единый тариф is a single combined rate; the payer does not split it by fund.

### 5.2 Reduced tariff for SMEs (МСП) — changed for 2026

- **Reduced tariff rate** — 15%
- **Threshold for reduced tariff applicability (2026)** — 1.5 × МРОТ = 1.5 × 27,093 ₽ = 40,639.50 ₽ per month per employee
- **Reduced tariff mechanics** — Subjects in the реестр МСП (small/medium enterprise register) may apply a reduced tariff of 15% — but the structure changed for 2026: - The reduced 15% applies only to the part of monthly wages exceeding 1.5 × МРОТ (previously 1 × МРОТ). With 2026 МРОТ = 27,093 ₽, the threshold is 1.5 × 27,093 = 40,639.50 ₽ per month per employee. Verify МРОТ and the multiplier. - Wages up to 1.5 × МРОТ are taxed at the standard 30%. - The universal SME discount was narrowed: from 2026 the reduced tariff is restricted to priority-sector МСП (per Government Decree No. 4125 of 27 Dec 2025, ~54 eligible OKVED-based sectors). Not every МСП qualifies. Conservative default: assume the standard 30% applies unless the ИП's primary OKVED is confirmed on the priority list — verify the sector list.  _(Government Decree No. 4125 of 27 Dec 2025)_

### 5.3 Injury contributions (взносы на травматизм / НСиПЗ)

- **Injury/accident contribution range** — 0.2%–8.5% depending on the industry risk class

Separate from the единый тариф, employers also pay accident-and-occupational-disease contributions to the СФР at 0.2%–8.5% depending on the industry risk class. These are not part of the единый тариф and have no предельная база. Verify the applicable class.

### 5.4 Reporting

Employer contributions require periodic reporting (РСВ — расчёт по страховым взносам; ЕФС-1 to the СФР; monthly уведомления for ЕНС allocation). See **ru-payroll**.

## 6. Worked Examples

### Example 1 — Small ИП on УСН «доходы», no employees

2026 income = 1,200,000 ₽; tax regime УСН «доходы» 6%.

```
Income tax before reduction = 1,200,000 × 6% = 72,000 ₽
Fixed part                  = 57,390 ₽
1% part = (1,200,000 − 300,000) × 1% = 9,000 ₽
Total страховые взносы      = 66,390 ₽

Tax reduction (no employees, up to 100%):
  72,000 − 66,390 = 5,610 ₽ УСН tax actually payable
Effective cash out = 66,390 (взносы) + 5,610 (УСН) = 72,000 ₽
```

### Example 2 — ИП on УСН «доходы», income below 300k

2026 income = 250,000 ₽, no employees.

```
Fixed part = 57,390 ₽  (still owed in full — registration = liability)
1% part    = 0          (income below 300,000 ₽)
УСН tax    = 250,000 × 6% = 15,000 ₽
Reduction  = up to 100% → 15,000 covered by the 57,390 ₽ fixed взносы
УСН tax payable = 0; the unused взносы do NOT carry over or refund.
```

### Example 3 — High-income ИП hitting the 1% cap

2026 income = 40,000,000 ₽ on УСН «доходы».

```
Fixed part = 57,390 ₽
1% raw     = (40,000,000 − 300,000) × 1% = 397,000 ₽
1% capped  = 321,818 ₽   (cap binds, since 397,000 > 321,818)
Total страховые взносы = 57,390 + 321,818 = 379,208 ₽  (the 2026 maximum)
```

### Example 4 — ИП with one employee, standard tariff (non-priority МСП)

Employee monthly gross = 80,000 ₽; non-priority sector, so standard единый тариф 30%.

```
Monthly employer взносы (within предельная база) = 80,000 × 30% = 24,000 ₽
Plus injury (e.g. class I, 0.2%)                 = 80,000 × 0.2% = 160 ₽
Monthly total on this employee                   ≈ 24,160 ₽

If instead the ИП were a confirmed priority-sector МСП:
  Up to 1.5 МРОТ (40,639.50 ₽): 40,639.50 × 30% = 12,191.85 ₽
  Above 1.5 МРОТ (39,360.50 ₽): 39,360.50 × 15% = 5,904.08 ₽
  Employer взносы (excl. injury) = 18,095.93 ₽
```

Employer contributions are separate from and additional to the ИП's own «за себя» contributions, and (under УСН «доходы») feed the 50% reduction limit described in §4.1.

## 7. Tier 2 Issues + References + Test Suite

### Tier 2 — escalate to a qualified Russian accountant (бухгалтер / налоговый консультант)

- Mid-year ИП registration/deregistration proration of the fixed part.
- Combining regimes (e.g. УСН + ПСН) and allocating the 1% base and the tax reduction.
- Confirming priority-sector МСП eligibility by OKVED for the 15% reduced tariff.
- Льготные (exempt) periods documentation and partial-year exemption.
- Transitional rules for *which year's* 1% reduces *which year's* УСН (2025→2026 carryover mechanics).
- НПД voluntary pension/social-insurance elections and their stage/benefit consequences.
- Foreign-resident or cross-border ИП situations (interaction with sanctions and treaties).

### References (verify before filing — figures reset annually)

- **Налоговый кодекс РФ, глава 34** (ст. 419–432) — contributions framework; **ст. 430** — fixed amount and the 1% / cap.
- **ФНС** — nalog.gov.ru (official 2026 figures: 57,390 ₽ fixed; 1% cap 321,818 ₽; единая база 2,979,000 ₽).
- **СФР** — sfr.gov.ru (voluntary ОПС for НПД/ИП; injury contributions; records).
- Government Decree **No. 4125 of 27 Dec 2025** — priority-sector list for the 15% reduced МСП tariff (~54 sectors).
- 2026 МРОТ = **27,093 ₽**; 1.5 МРОТ = **40,639.50 ₽**.
- Companion skills: **ru-usn**, **ru-income-tax**, **ru-payroll**.

### Test suite (expected behaviour)

1. *"How much does an ИП pay в 2026 за себя?"* → 57,390 ₽ fixed + 1% over 300k ₽ (cap 321,818 ₽); deadlines 28 Dec 2026 / 1 Jul 2027.
2. *"My ИП earned 0 ₽ — do I still pay?"* → Yes, full 57,390 ₽ unless a §3.2 льготный период applies.
3. *"Do самозанятые pay страховые взносы?"* → No mandatory contributions; voluntary ОПС via СФР (~71,525.52 ₽ for full 2026 stage).
4. *"Income 5,000,000 ₽ — what's the 1%?"* → (5,000,000 − 300,000) × 1% = 47,000 ₽ (below cap); total 104,390 ₽.
5. *"Can страховые взносы reduce my УСН?"* → Yes — 100% without employees, 50% with employees (УСН «доходы»); expense deduction under «доходы минус расходы».
6. *"I hired one worker — what rate?"* → Standard единый тариф 30% up to 2,979,000 ₽ base; 15% reduced only if confirmed priority-sector МСП on wages above 1.5 МРОТ.
7. *"Income 50,000,000 ₽ — total взносы?"* → Capped: 57,390 + 321,818 = 379,208 ₽.

## PROHIBITIONS

- **Do NOT** file or pay on the basis of these figures without re-verifying the current-year fixed amount, the 1% cap, the единая предельная база, and МРОТ against ФНС/nalog.gov.ru. All reset annually by law.
- **Do NOT** assume a registered ИП is exempt because income is low, zero, or the business is dormant — only deregistration or a documented §3.2 льготный период removes the fixed obligation.
- **Do NOT** apply the 15% reduced МСП tariff without confirming priority-sector eligibility (Decree No. 4125); default to 30%.
- **Do NOT** treat самозанятые (НПД) as owing mandatory contributions, and do NOT promise pension stage to a НПД payer who has not made voluntary СФР contributions.
- **Do NOT** mix up the income bases for the 1% across regimes (gross vs net vs potential income).
- **Do NOT** advise on cross-border, sanctions-affected, or multi-regime situations without escalating to a qualified Russian accountant.
- **Do NOT** present this skill's output as final advice — it requires sign-off by a qualified Russian accountant before reliance.

## Disclaimer

This skill is **research-verified** against ФНС (nalog.gov.ru), the Social Fund of Russia (СФР), and reputable secondary sources for tax year 2026, but it is **pending sign-off by a qualified Russian accountant (налоговый консультант / бухгалтер)**. Russian contribution figures (the fixed amount, the 1% cap, the единая предельная база, and МРОТ) are reset every year by federal law and must be re-verified before any filing or payment. Insurance contributions are a YMYL (Your Money or Your Life) topic; nothing here is a substitute for advice from a credentialed professional who has reviewed the taxpayer's specific facts. Part of the OpenAccountants open-source tax skills project — openaccountants.com.

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
