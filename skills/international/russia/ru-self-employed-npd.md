---
name: ru-self-employed-npd
description: Use this skill whenever asked about the Russian self-employed tax regime for individuals and freelancers — the Professional Income Tax (Налог на профессиональный доход / НПД). Trigger on phrases like "самозанятый", "self-employed Russia", "НПД", "professional income tax Russia", "Мой налог", "4% 6% tax Russia freelancer", "налог для самозанятых", "register as self-employed in Russia", "Russian freelancer tax", or any request involving the НПД special regime, the 2.4 million ruble cap, the «Мой налог» app, чек (receipt) issuance, the 10,000 ₽ deduction, or whether a Russian freelancer must pay страховые взносы. Covers eligibility, the 4%/6% split, the deduction mechanics, monthly payment, and what happens when the cap is exceeded. References ru-usn and ru-income-tax for alternatives once НПД no longer fits.
version: 1.0
jurisdiction: RU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RU Self Employed Npd

## Russia — Self-Employed Professional Income Tax (Налог на профессиональный доход / НПД)

The НПД (*Налог на профессиональный доход*) is the special tax regime for *самозанятые* — self-employed individuals and freelancers in Russia. It is the simplest legal way for an individual to earn and declare professional income: no accountant, no separate filings, no cash register. Everything runs through the **«Мой налог»** mobile app (or a participating bank). This skill helps the agent classify a user's income, confirm НПД eligibility, compute the tax, and explain when the user must leave the regime.

The AI replies to the user in the user's own language. Russian tax terms are kept native (самозанятый, НПД, ФНС, «Мой налог», чек, страховые взносы) so the meaning maps cleanly to the official wording.

## 1. Quick Reference

**Quick Reference table**

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Russian Federation (RU) |
| Tax | НПД — Professional Income Tax, **4%** (income from individuals) / **6%** (income from legal entities & ИП) |
| Annual income cap | **2,400,000 ₽** per calendar year |
| Currency | RUB (Russian ruble, ₽) |
| Legislation | Federal Law No. **422-FZ** of 27.11.2018 ("Об эксперименте... НПД") |
| Authority | ФНС (Federal Tax Service / Федеральная налоговая служба) — nalog.gov.ru |
| App | **«Мой налог»** (lknpd.nalog.ru / mobile app) + bank-partner apps (Сбербанк, Т-Банк, etc.) |
| Tax period | Calendar month |
| Receipt (чек) deadline | At the moment of cash/card payment; for bank transfers, by the **9th** of the following month |
| Tax notice issued | By the **12th** of the following month in «Мой налог» |
| Payment deadline | By the **28th** of the month following the tax period |
| One-time deduction | **10,000 ₽** налоговый вычет (reduces 4%→3% and 6%→4% until exhausted) |
| Mandatory страховые взносы | **None** — pension/social contributions are **voluntary** |
| Regime status | Federal experiment running **01.01.2019 – 31.12.2028** (verify no extension/early end before relying long-term) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Russian accountant |
| Version | 1.0 |

### Conservative defaults

When facts are missing or ambiguous, the agent applies the **conservative default** and flags it for review rather than guessing in the user's favour:

- **Counterparty unknown → assume the higher 6% rate.** If you cannot tell whether a payer is an individual (физлицо, 4%) or a legal entity / ИП (юрлицо/ИП, 6%), default to 6% and ask the user to confirm.
- **Activity borderline → assume excluded.** If an activity might be resale, agency, or property-related (see §2), treat it as **outside НПД** and require the user to confirm eligibility before generating чеки.
- **Cap proximity → warn early.** Once year-to-date income approaches 2,400,000 ₽, warn the user *before* the next чек, because exceeding the cap strips НПД status retroactively from the start of the month of breach.
- **Ex-employer income → assume blocked.** Income from a current employer, or from any employer the user left **less than two years** ago, is excluded (anti-payroll-substitution rule). Default to excluded unless the user confirms the two-year gap.
- **Never invent rates or thresholds.** All figures above are verified for tax year 2026; if the user asks about a different year, give the formula and say "verify current value with ФНС".

## 2. Eligibility — qualifying vs excluded income

НПД is available to **individuals** (and ИП who opt in) who earn income from their own labour, skills, or use of their own property, without employees under labour contracts, and whose income stays within the cap.

### Income that QUALIFIES (typical самозанятый activities)

- Freelance services: software development, design, copywriting, translation, tutoring, consulting, marketing, photography/video.
- Personal services: hairdressing, manicure, repairs, cleaning, delivery, driving (own labour).
- Sale of goods the person **made themselves** (handmade / self-produced).
- Rental of **own residential** property (жилое помещение / квартира).
- Creative and professional work performed personally.

### Income that is EXCLUDED from НПД (Federal Law 422-FZ, Art. 4 & 6)

- **Excluded income categories** — The agent must NOT generate НПД чеки for any of the following — they require a different regime (see ru-usn / ru-income-tax) or are taxed as ordinary income: Employment salary under a labour contract (трудовой договор) — НДФЛ income, never НПД. Income from a current or former employer where the user left less than 2 years ago (anti-substitution rule). Resale of goods purchased for resale (перепродажа) is prohibited; only self-made goods qualify. Sale of excisable (подакцизные) goods and goods subject to mandatory labelling (обязательная маркировка). Mining / extraction and sale of mineral resources (полезные ископаемые). Agency, commission, and intermediary activity for third parties (посредническая деятельность / договоры поручения, комиссии, агентские) — except certain delivery-with-receipt arrangements. Rental of non-residential / commercial property (нежилые помещения). Sale of property and securities, sale of shares/units, transfer of property rights (other than the residential rental above). Income of notaries, lawyers (адвокаты), arbitration managers, mediators, appraisers — these have their own regimes. Persons employing workers under labour contracts.  _(Federal Law 422-FZ, Art. 4 & 6)_

### Refusal catalogue (R-RU-n)

- **R-RU-1** — User wants to declare salary / employment income as НПД. Refuse: this is НДФЛ. Do not generate чеки.  _(Federal Law 422-FZ)_
- **R-RU-2** — Income comes from a current employer or an employer left <2 years ago. Refuse НПД treatment for that income.  _(Federal Law 422-FZ)_
- **R-RU-3** — Activity is resale of purchased goods, excisable, or labelled goods. Refuse; recommend ИП on УСН (see ru-usn).  _(Federal Law 422-FZ)_
- **R-RU-4** — Activity is agency/commission/intermediary, mining, or rental of commercial (non-residential) property. Refuse НПД.  _(Federal Law 422-FZ)_
- **R-RU-5** — Year-to-date income exceeds 2,400,000 ₽. НПД status is lost; see §4 and route to ru-usn / ru-income-tax.  _(Federal Law 422-FZ)_
- **R-RU-6** — User has employees under labour contracts. НПД is unavailable; route to ИП regimes.  _(Federal Law 422-FZ)_
- **R-RU-7** — User is a non-resident / works outside the territory covered by the experiment, or activity falls outside Russia entirely. Flag as Tier 2; do not assume eligibility.  _(Federal Law 422-FZ)_
- **R-RU-8** — User asks the agent to issue a чек the user cannot legally back (e.g. backdating beyond the allowed чек deadline, or for excluded income). Refuse.  _(Federal Law 422-FZ)_

### The two rates

**The two rates table**

| Payer (counterparty) | Rate |
| --- | --- |
| **Individual** (физическое лицо) | **4%** |
| **Legal entity** (юридическое лицо) or **ИП** | **6%** |

НПД has exactly two rates, set by the type of payer (counterparty), not the type of work. Each чек is taxed at the rate matching that specific payer. A self-employed person can have both rates in the same month — invoice a private client at 4% and a company at 6% on the same day.

### The налоговый вычет (10,000 ₽ one-time deduction)

- **Deduction mechanics** — Every newly registered самозанятый receives a one-time 10,000 ₽ tax deduction (бонус). It is not a cash payment and not a reduction of income — it reduces the tax rate until the 10,000 ₽ "credit" is used up: On 4% income, the rate drops to 3% — the deduction covers 1 percentage point of the 4%. On 6% income, the rate drops to 4% — the deduction covers 2 percentage points of the 6%. The deduction is consumed automatically by «Мой налог» as tax accrues, until the cumulative 10,000 ₽ benefit is exhausted; after that, the full 4%/6% rates apply. It is granted once per lifetime, automatically — no application needed. It does not expire by date; it persists until used. If the user deregisters and re-registers, the unused remainder is restored (it is not re-granted in full, and it is not forfeited).  _(Federal Law 422-FZ)_
- **Deduction consumption formula** — deduction_used_on_a_receipt = receipt_amount × 0.01 (for a 4% / individual receipt); receipt_amount × 0.02 (for a 6% / legal-entity receipt). remaining_deduction = 10,000 ₽ − cumulative deduction_used. Once remaining_deduction hits zero, the reduced rates stop and standard 4%/6% resume.  _(Federal Law 422-FZ)_

### Issuing a чек (receipt) — mandatory for every payment

- **Чек issuance requirements** — For each payment received for a qualifying activity, the самозанятый must form a чек in «Мой налог» (or via a bank partner). The чек is the legal proof of income; there is no cash register and no other invoice required. Cash or card (electronic means of payment): form the чек at the moment of settlement. Bank transfer (безналичный расчёт): form the чек no later than the 9th day of the month following the month the payment was received. The чек records: date, amount, description of the service/good, and the payer's status (individual vs legal entity / ИП — which sets the 4% vs 6% rate). A B2B чек must include the buyer's INN. A чек can be cancelled (e.g. refund or error), which reduces the taxable base. If the user records income but issues no чек, the income is still taxable and ФНС can assess penalties. The agent should always pair "income received" with "чек issued".  _(Federal Law 422-FZ)_

### Monthly tax — calculation and payment

- **Monthly tax calculation and payment** — The tax period is the calendar month. There is no annual return to file — «Мой налог» computes everything automatically from the чеки. By the 12th of the following month, ФНС posts the calculated tax amount in «Мой налог». The user pays by the 28th of that following month (the app supports card/auto-pay). No tax is due in a month with zero income. No страховые взносы are mandatory. The 4%/6% is the only obligatory payment. Pension/social contributions to the СФР are voluntary; without them (or parallel employment) no страховой стаж accrues. Voluntary buy-in of pension stage is possible — treat the exact buy-in figure as a separate, Tier 2 question (verify current value with СФР).  _(Federal Law 422-FZ)_

### Exceeding the 2,400,000 ₽ cap

- **Cap breach mechanics** — The cap is on income received within the calendar year (not profit; there are no deductible expenses under НПД). When cumulative income in the year exceeds 2,400,000 ₽: 1. The user loses НПД status — effective from the beginning of the month in which the cap is breached (income up to the breach remains under НПД). 2. Income received after the loss must be taxed under another regime: An individual (not ИП): the excess is ordinary personal income taxed as НДФЛ (see ru-income-tax), unless the person registers as ИП. An ИП: must switch to УСН (Упрощённая система — simplified, see ru-usn), ЕСХН, or the general regime ОСНО, by filing the relevant application within the statutory window (an ИП who applies for УСН within ~20 days of losing НПД can move to УСН from the date of loss — confirm the exact deadline for the year before relying on it). 3. The agent should warn the user before the cap is hit and present the ru-usn vs ru-income-tax fork as the next step. > The cap resets each calendar year. A user who hit the cap in one year may re-register for НПД from 1 January of the next year if otherwise eligible.  _(Federal Law 422-FZ)_

## 5. Worked examples

All figures are illustrative for tax year 2026. Verify rates/cap with ФНС.

### Example 1 — Individual clients only (4%), deduction active

A tutor earns 80,000 ₽ in March, all from private individuals.

- Rate with deduction: 3% (4% − 1pp covered by the вычет).
- Tax = 80,000 × 3% = 2,400 ₽.
- Deduction consumed = 80,000 × 1% = 800 ₽; remaining вычет = 10,000 − 800 = 9,200 ₽.
- Чеки issued per payment; tax shown by 12 April, paid by 28 April.

### Example 2 — Company clients only (6%), deduction active

A freelance developer earns 150,000 ₽ in March from one OOO (legal entity).

- Rate with deduction: 4% (6% − 2pp covered by the вычет).
- Tax = 150,000 × 4% = 6,000 ₽.
- Deduction consumed = 150,000 × 2% = 3,000 ₽; remaining вычет = 10,000 − 3,000 = 7,000 ₽.
- Each чек carries the client's INN. Bank-transfer чек due by 9 April; tax paid by 28 April.

### Example 3 — Mixed clients, deduction running out mid-month

In one month a designer earns 100,000 ₽ from individuals (4%) and 200,000 ₽ from a company (6%). Assume the вычет remaining at the start of the month is 4,000 ₽.

- Reduced rates apply only until the 4,000 ₽ remainder is used:
  - On the 4% stream the вычет covers 1pp; on the 6% stream it covers 2pp.
  - «Мой налог» applies the remaining deduction across accruing чеки in order until 4,000 ₽ is exhausted, then charges full 4% / 6%.
- A clean way to bound it: full-rate tax = 100,000 × 4% + 200,000 × 6% = 4,000 + 12,000 = 16,000 ₽; the вычет reduces this by up to the 4,000 ₽ remainder, so tax = ≈12,000 ₽ (exact split depends on чек ordering — the app computes it). After this month the deduction is fully used and standard 4%/6% apply thereafter.

### Example 4 — Hitting the 2,400,000 ₽ cap mid-year

A consultant has earned 2,350,000 ₽ by 1 August. On 14 August a new 100,000 ₽ payment would take the year-to-date to 2,450,000 ₽.

- The cap (2,400,000 ₽) is breached in August. НПД status is lost from 1 August.
- Income up to the breach stays under НПД; the agent must stop generating НПД чеки for August onward and warn before accepting the 100,000 ₽.
- Next step: if the user is an individual, the post-loss income is НДФЛ (ru-income-tax) unless they register as ИП; if already ИП, file for УСН promptly (ru-usn) to avoid landing on ОСНО.
- The user may re-register for НПД from 1 January next year if eligible.

### Example 5 — Excluded income (refusal path)

A user wants to declare rental income from a commercial shop unit as НПД.

- R-RU-4 applies: rental of non-residential property is excluded.
- The agent refuses to issue НПД чеки and explains that residential rental would qualify, but commercial rental must be declared as НДФЛ or under an ИП regime (route to ru-income-tax / ru-usn).

## 6. Tier 2 — reviewer judgement required

Flag these to a qualified Russian accountant rather than deciding deterministically:

- B2B re-characterisation risk. A company paying a single самозанятый regularly, exclusively, on schedule, looking like disguised employment — ФНС may reclassify it as a labour relationship (with НДФЛ + взносы owed by the payer). Flag patterns that resemble employment.
- Ex-employer two-year rule edge cases (secondment, group companies, contract renewals around the 2-year line).
- Cross-border / non-resident activity, foreign-platform income, or work performed outside Russia (see R-RU-7).
- Mixed / borderline activities — e.g. self-made goods vs resale (assembly from purchased components), delivery-with-receipt arrangements, marketplace sales.
- Cap-year transition mechanics — exact deadline and effective date for an ИП moving НПД → УСН after a cap breach (verify current statutory window).
- Voluntary СФР pension buy-in — whether and how much to contribute; the annual buy-in figure changes yearly (verify current value).
- Regime end date — НПД is an experiment scheduled through 31.12.2028; confirm no legislative change before giving long-horizon advice.

## 7. Bank statement reading guide

Russian самозанятые usually receive money to a personal card/account. When reading a statement to reconstruct НПД income, the agent should:

- Identify the payer type to set 4% vs 6%:
  - Inflows from another personal card / СБП (Система быстрых платежей) from an individual → likely 4% (физлицо).
  - Inflows naming an OOO / AO / ИП, or carrying an INN/KPP in the narrative → 6% (legal entity / ИП). Default to 6% when unsure (conservative).
- Sberbank / Сбербанк (SberBank Online): look for "Перевод от …" (transfer from), СБП incoming transfers, and salary-labelled credits ("Зарплата", "Аванс") — salary credits are NOT НПД income (R-RU-1). Sber also has a built-in "Своё дело" самозанятый module that mirrors «Мой налог».
- Tinkoff / Т-Банк: statements label СБП and card-to-card transfers; the Т-Банк app has a самозанятый feature that issues чеки and reports to ФНС automatically — reconcile its чек log against the bank statement.
- Other banks / platforms (ВТБ, Альфа-Банк, ЮMoney, payment aggregators): match each business inflow to a чек. Aggregators paying out on behalf of many end-clients may need per-end-client чеки; flag as Tier 2.
- Exclude non-income credits: refunds, transfers between the user's own accounts, loans, personal gifts, and salary. These are not НПД income.
- Reconciliation rule: every business inflow should map to exactly one чек. Inflows with no чек → flag (income under-reported). Чеки with no inflow → flag (possible cancelled/erroneous чек).

> The bank statement is supporting evidence only. The legally authoritative record of НПД income is the set of чеки in «Мой налог».

### Reference

- Federal Law No. 422-FZ of 27.11.2018 — establishes the НПД experiment (rates 4%/6%, cap 2,400,000 ₽, excluded activities, 10,000 ₽ deduction).
- ФНС — nalog.gov.ru; «Мой налог» portal lknpd.nalog.ru.
- Tax period: calendar month; payment by the 28th of the following month; tax shown by the 12th; bank-transfer чек by the 9th.
- No mandatory страховые взносы; voluntary pension via СФР.
- Regime window: 01.01.2019 – 31.12.2028 (experiment).
- Related skills: ru-usn (Упрощённая система for ИП), ru-income-tax (НДФЛ for individuals) — used when НПД is unavailable or the cap is exceeded.

### Test suite (agent self-checks)

1. Payer is a private individual → applies 4% (3% while deduction lasts). ✔
2. Payer is an OOO with an INN → applies 6% (4% while deduction lasts). ✔
3. Income from a company the user left 8 months ago → R-RU-2 refusal. ✔
4. User buys phones to resell → R-RU-3 refusal (resale). ✔
5. Year-to-date reaches 2,400,001 ₽ → R-RU-5, НПД lost from start of the breach month, route to ru-usn / ru-income-tax. ✔
6. User asks if they must pay pension взносы → No, voluntary. ✔
7. Payer type unknown → default 6% and ask. ✔
8. Bank-transfer income on 3 March → чек due by 9 April, tax by 28 April. ✔
9. Commercial property rental → R-RU-4 refusal; residential would qualify. ✔
10. New registrant, first 80,000 ₽ from individuals → tax 2,400 ₽ at 3%, remaining вычет 9,200 ₽. ✔

## PROHIBITIONS

- **Prohibitions list** — The agent must NOT: Treat salary / employment income as НПД (R-RU-1), or treat income from a current/recent (<2 years) employer as НПД (R-RU-2). Issue НПД чеки for excluded activities — resale, excisable/labelled goods, mining, agency/intermediary, or rental of non-residential property (R-RU-3, R-RU-4). Continue НПД treatment once year-to-date income exceeds 2,400,000 ₽ (R-RU-5); it must route the user to ru-usn / ru-income-tax. Apply НПД where the user has employees under labour contracts (R-RU-6). Invent or assume rates, the cap, the deduction amount, or deadlines for a year other than 2026 — give the formula and say "verify current value with ФНС". Claim страховые взносы are mandatory — they are voluntary under НПД. Backdate or fabricate a чек, or generate a чек for income the user cannot legally back (R-RU-8). Provide a definitive disguised-employment, cross-border, or pension-buy-in conclusion without flagging it as Tier 2 for a qualified reviewer.  _(Federal Law 422-FZ)_

## Disclaimer

This skill is research-verified against ФНС (nalog.gov.ru), Federal Law No. 422-FZ, and reputable secondary sources for tax year 2026, but it is pending sign-off by a qualified Russian accountant. It is general information, not individual tax advice. НПД is a time-limited experiment (through 31.12.2028) and figures, deadlines, and eligibility rules can change; always confirm current values with ФНС and «Мой налог» before filing or relying on a result. A qualified Russian accountant or tax adviser must review any output before it is acted upon. Maintained by the Open Accountants Community — openaccountants.com.

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
