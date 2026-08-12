---
name: ru-income-tax
description: Use this skill whenever asked about Russian personal income tax (НДФЛ / nalog na dokhody fizicheskikh lits) for individuals or for individual entrepreneurs (ИП) on the general system (ОСНО). Trigger on phrases like "НДФЛ", "income tax Russia", "13% 15% Russia", "progressive scale Russia", "3-НДФЛ", "ИП ОСНО", "professional deduction Russia", "профессиональный вычет", "tax residency Russia 183 days", "personal income tax Russia 2026", or any request to compute, classify, or advise on Russian НДФЛ. This skill covers the progressive НДФЛ scale (13/15/18/20/22%) effective from 1 Jan 2025, tax residency, the non-resident 30% rate, ИП on ОСНО paying НДФЛ on net business profit with the professional deduction, the annual 3-НДФЛ declaration, advance payments, and the standard/social/property deduction overview. For simplified alternatives see ru-usn (УСН) and ru-self-employed-npd (НПД / самозанятые).
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

# RU Income Tax

## Russia — Personal Income Tax (НДФЛ) for Individuals and ИП on ОСНО

This skill computes and explains Russian personal income tax — **НДФЛ** (*nalog na dokhody fizicheskikh lits*) — for two populations: ordinary individuals with taxable income, and **ИП** (*individualnyy predprinimatel*, sole trader) operating on the **общая система налогообложения** / **ОСНО** (the general taxation regime). Reply to the user in their own language; embed the native Russian terms in parentheses on first use.

> **AI language rule:** Detect the user's language and answer in it. Keep Russian tax terms (НДФЛ, ИП, ОСНО, ФНС, 3-НДФЛ, профессиональный вычет, авансовый платёж) verbatim — they are proper terms the user and their accountant will recognise.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Tax | НДФЛ — personal income tax (*nalog na dokhody fizicheskikh lits*) |
| Tax year | 2026 calendar year (1 Jan – 31 Dec); НДФЛ is a calendar-year tax |
| Legislation | Налоговый кодекс РФ, часть вторая, **глава 23** (Tax Code, Part Two, Chapter 23, arts. 207–233) |
| Authority | **ФНС** — Федеральная налоговая служба (Federal Tax Service), nalog.gov.ru |
| Filing portal | **Личный кабинет налогоплательщика** (taxpayer Personal Account), lkfl2.nalog.ru |
| Resident scale (2026) | Progressive **13 / 15 / 18 / 20 / 22 %**, applied band-by-band on the excess |
| Non-resident rate | **30 %** generally (exceptions in §3) |
| Residency test | **≥ 183 days** of physical presence in Russia in any rolling 12-month period |
| ИП ОСНО base | Net business profit = доходы − профессиональный вычет (documented expenses **or** 20 % standard) |
| Annual declaration | **3-НДФЛ**, filed by **30 April** of the following year |
| Final payment | НДФЛ balance due by **15 July** of the following year |
| ИП advance payments | Quarterly, due **28 April / 28 July / 28 October** |
| ИП ОСНО + VAT | ИП on ОСНО are also **НДС** (VAT) payers — standard НДС rate **22 % from 1 Jan 2026** (Law 425-FZ); see russia-vat |
| Currency | Russian rouble (₽ / RUB) |
| Quality tier | **Research-verified — pending sign-off by a qualified Russian accountant** |
| Skill version | 1.0 |

### Progressive resident rate table (2026)

**Progressive resident rate table (2026)**  _(Налоговый кодекс гл. 23 art. 224)_

| Band | Annual taxable income (₽) | Rate | НДФЛ on a full band |
| --- | --- | --- | --- |
| 1 | up to **2 400 000** | **13 %** | up to 312 000 ₽ |
| 2 | over 2 400 000 to **5 000 000** | **15 %** | 390 000 ₽ on the 2.6M slice |
| 3 | over 5 000 000 to **20 000 000** | **18 %** | 2 700 000 ₽ on the 15M slice |
| 4 | over 20 000 000 to **50 000 000** | **20 %** | 6 000 000 ₽ on the 30M slice |
| 5 | over **50 000 000** | **22 %** | 22 % of the excess |

The five-band scale took effect **1 January 2025** and continues unchanged into 2026. The higher rate applies **only to the portion of income inside that band** (band-by-band / *поэтапно*), never to the whole amount. Bands below are annual taxable income of a **tax resident**.

> **Verify current values** at filing time against ФНС (nalog.gov.ru) and Налоговый кодекс гл. 23 art. 224. Bands are nominal rouble figures fixed in statute (not indexed automatically), so confirm they have not been re-set for the year you are filing.

### Special "passive income" 13 / 15 % scale [verify]

For certain income categories — **dividends (дивиденды)**, **bank deposit interest (проценты по вкладам)**, gains on **securities (ценные бумаги)** and **digital financial assets**, and **sale of property (продажа имущества)** — a separate **two-rate** scale applies to residents: **13 %** up to 2 400 000 ₽ and **15 %** above. These do **not** climb to 18/20/22 %. Treat this base separately from the main employment/business base. **Verify the exact list of qualifying income** before applying.

### Conservative defaults (apply when an input is missing or ambiguous)

- **Residency unknown → assume non-resident (30 %)** until ≥ 183 days of presence is documented. This is the cautious assumption (higher tax); flag for the reviewer to confirm and re-compute as resident if proven.
- **ИП deduction method unknown → use whichever is *lower* tax for the client only after both are computed**; if expenses cannot be documented at all, fall back to the **20 % standard** professional deduction.
- **Income classification unclear (main scale vs passive 13/15 % scale) → flag, do not guess.**
- **Foreign-source income for a resident → flag.** Residents are taxed on worldwide income; sanctions and double-tax-treaty suspension complicate this — escalate.
- Round each computation step to the kopeck, final НДФЛ to the **whole rouble** (standard ФНС rounding) — verify rounding direction at filing.

## 2. Required Inputs & Refusal Catalogue

### Required inputs

1. **Taxpayer type** — ordinary individual, or **ИП on ОСНО**. (If ИП is on УСН or НПД, stop and route to `ru-usn` / `ru-self-employed-npd`.)
2. **Residency status** — days of physical presence in Russia over the relevant rolling 12 months.
3. **ИНН** (taxpayer identification number) — 12 digits for an individual/ИП.
4. **Income by category** — employment (зарплата), business turnover (доходы от предпринимательской деятельности), dividends, interest, property sale, other.
5. **For ИП:** documented business expenses with primary documents (первичные документы), or a decision to use the 20 % standard professional deduction.
6. **Deductions claimed** — standard (стандартные), social (социальные), property (имущественные), investment (инвестиционные).
7. **Withholding already taken** — НДФЛ withheld at source by a tax agent (налоговый агент), and ИП advance payments already made in-year.

### Refusal catalogue

**Refusal catalogue table**

| Code | Refuse / escalate when… | Action |
| --- | --- | --- |
| **R-RU-1** | Taxpayer is a legal entity (ООО/АО). | НДФЛ does not apply — they pay налог на прибыль (corporate tax). Out of scope. |
| **R-RU-2** | ИП is on **УСН, ПСН, ЕСХН, or НПД**, not ОСНО. | Route to `ru-usn` / `ru-self-employed-npd` / patent skill. This skill is ОСНО only. |
| **R-RU-3** | Cross-border / foreign-source income, or a counterparty in a sanctioned relationship. | Flag [T2/T3]; treaty suspension and sanctions affect treatment. Escalate to a qualified Russian accountant. |
| **R-RU-4** | "Foreign agent" (иностранный агент) status, or other special-category taxpayer. | A punitive 30 % НДФЛ regime may apply; out of scope — escalate. |
| **R-RU-5** | Controlled foreign company (КИК) income, crypto/DFA mining, or self-employed VAT interplay beyond basics. | Out of scope — escalate. |
| **R-RU-6** | User asks to under-report income, fabricate expenses, or backdate documents. | Refuse. See PROHIBITIONS. |
| **R-RU-7** | Inputs insufficient to determine residency or income category and the user cannot supply them. | Apply conservative default, flag clearly, and recommend reviewer confirmation. |

## 3. Residency & Rates

### Tax residency (налоговое резидентство)

- **Tax residency definition** — A person is a **Russian tax resident (налоговый резидент РФ)** if present in Russia for **at least 183 calendar days within any rolling 12-month period**. Residency is determined per the facts of the year, not by citizenship. Short trips abroad for treatment/study (under 6 months) generally do not break the count — **verify** the specific exception list. - **Resident** → taxed on **worldwide income** at the progressive **13/15/18/20/22 %** scale (or the special 13/15 % scale for qualifying passive income). - **Non-resident** → taxed only on **Russian-source income**, generally at a flat **30 %**.  _(Налоговый кодекс art. 207)_

### Non-resident rate exceptions [verify]

The flat 30 % has carve-outs where the **progressive resident scale** (or a reduced flat rate) applies even to non-residents — confirm each before relying on it:

- **Dividends** from Russian companies to non-residents: **15 %** (verify; treaty may reduce).
- **Highly qualified specialists (ВКС)**, EAEU-country workers, patent-based migrant workers, refugees, and remote workers for Russian employers — may be taxed on the **progressive resident scale** rather than 30 %. **Verify the current list** in art. 224, as it has been amended repeatedly.

> **Verify current value:** non-resident treatment is the most volatile part of Russian НДФЛ. Always check the live text of Налоговый кодекс art. 224 and ФНС guidance for the filing year.

## 4. ИП on ОСНО — Professional Deduction & Net Profit

An **ИП on ОСНО** pays НДФЛ on the **net profit of the business**, not on gross turnover. The taxable base is:

- **НДФЛ base (ИП ОСНО)** — НДФЛ base (ИП ОСНО) = доходы (business income) − профессиональный вычет (professional deduction) − other applicable deductions (standard / social / property)

### Professional deduction (профессиональный вычет) — art. 221

- **Professional deduction methods** — The ИП chooses **one** of two methods for the year (cannot mix): 1. **Documented expenses (расходы по документам)** — actual business expenses supported by primary documents (первичные документы): purchases, rent, wages, contributions, depreciation, etc. Composition mirrors the profit-tax rules of гл. 25. 2. **20 % standard deduction (стандартный профвычет 20 %)** — if expenses cannot be documented (or are below 20 %), deduct a flat **20 % of business income** without proof. > Choose documented expenses when they exceed 20 % of income; otherwise the 20 % standard is better. Compute both and pick the lower-tax outcome. The 20 % method applies **only to business income**, not to employment or other personal income.  _(art. 221)_

### НДС (VAT) for ИП on ОСНО

- **VAT for ИП on ОСНО** — ИП on ОСНО are **also VAT payers (плательщики НДС)**. From **1 January 2026** the standard НДС rate is **22 %** (Federal Law No. 425-FZ; up from 20 %), with a preferential 10 % rate for socially significant goods. НДФЛ and НДС are **separate taxes** with separate returns — do not net them. For VAT classification, returns, and reverse charge, defer to the `russia-vat` skill.  _(Federal Law No. 425-FZ)_

### Advance payments (авансовые платежи) — art. 227

**Advance payment due dates**  _(art. 227)_

| Period | Advance due date (2026 income) |
| --- | --- |
| Q1 (Jan–Mar) | **28 April** |
| Half-year (Jan–Jun) | **28 July** |
| 9 months (Jan–Sep) | **28 October** |
| Annual balance | **15 July** of the following year (with the 3-НДФЛ) |

- **Advance for period formula** — Advance for period = (income to date − deductions to date) × rate − advances already paid  _(art. 227)_

ИП on ОСНО self-compute and pay **quarterly НДФЛ advances** based on actual income to date, less professional and other deductions, less prior advances:

Advances flow through the **ЕНС / ЕНП** (единый налоговый счёт / платёж — Single Tax Account/Payment) system; verify the current EНП mechanics, as ФНС has changed notification (уведомление) requirements recently.

### Annual declaration (3-НДФЛ)

- **3-НДФЛ filing rules** — - **Form:** 3-НДФЛ, filed via Личный кабинет, in person, or by post. - **Deadline to file:** **30 April** of the year following the tax year (e.g. 2026 income → file by 30 Apr 2027). - **Deadline to pay the balance:** **15 July** of the following year. - ИП on ОСНО must file 3-НДФЛ **even if the result is a loss or zero** (declaration is mandatory).

### Deductions overview (вычеты) — individuals and ИП alike

- **Стандартные (standard)** — per-child allowances, allowances for certain categories. Verify current per-child amounts and income caps.
- **Социальные (social)** — medical treatment, education, pension/insurance contributions, charity, fitness. Subject to an annual aggregate cap — **verify the current cap** (it was raised in recent years).
- **Имущественные (property)** — deduction on purchase of housing (capped on cost and on mortgage interest) and reliefs on sale of property held over the minimum holding period. Verify caps and holding periods.
- **Инвестиционные (investment)** — ИИС (individual investment account) and long-term securities reliefs.

> Deductions reduce the base taxed at **13 %** first; verify how each interacts with the higher bands.

## 5. Transaction Pattern Library

**Transaction Pattern Library table**

| Pattern (Russian → English) | Likely category | НДФЛ treatment | Tier |
| --- | --- | --- | --- |
| `ЗАРПЛАТА` / `Заработная плата` (salary) | Employment income | Main scale; usually withheld by tax agent | T1 |
| `АВАНС` (salary advance) | Employment income | Main scale (part of salary) | T1 |
| `ОПЛАТА ПО ДОГОВОРУ` / `За услуги` (payment for services) | ИП business income | Goes into ИП доходы; main scale after проф. вычет | T1 |
| `ОПЛАТА ПО СЧЁТУ № …` (invoice payment) | ИП business income | Business income | T1 |
| `ДИВИДЕНДЫ` (dividends) | Passive income | Special 13/15 % scale; often withheld by payer | T2 |
| `ПРОЦЕНТЫ ПО ВКЛАДУ` (deposit interest) | Passive income | Special scale; threshold exemption — verify | T2 |
| `ПРОДАЖА КВАРТИРЫ` / `Продажа имущества` (property sale) | Capital | Special scale; check holding period & vychet | T2 |
| `ВОЗВРАТ` / `Возврат средств` (refund) | Not income | Exclude (return of own money) | T1 |
| `ПЕРЕВОД МЕЖДУ СВОИМИ СЧЕТАМИ` (transfer between own accounts) | Internal | Exclude | T1 |
| `АРЕНДА` / `Арендная плата` (rent received) | Other income | Main scale (rental income) | T2 |
| `ВЗНОСЫ` / `Страховые взносы` (insurance contributions paid) | ИП expense | Deductible expense / проф. вычет | T2 |
| `НАЛОГ` / `НДФЛ` / `ЕНП` (tax paid) | Tax payment | Not income; reconcile against liability | T1 |
| `ГОНОРАР` (fee/royalty), `ROYALTY` | Business/other income | Income; check проф. вычет eligibility | T2 |
| `CARD2CARD` / `Перевод СБП` (peer transfer) | Ambiguous | Flag — could be gift, repayment, or income | T2 |

Map bank-statement memos to НДФЛ treatment. Russian keyword first, English/translit equivalents after.

> Peer-to-peer transfers (`СБП`, card-to-card) are **not automatically income** but are a frequent ФНС audit trigger for ИП. Flag and ask the client to characterise them.

## 6. Worked Examples

All examples use the 2026 resident scale unless stated. **Figures are illustrative; verify rates and bands.**

### Example 1 — Resident salary below the first threshold

Income: 1 800 000 ₽ salary, resident, no deductions.
- Entirely in Band 1 → 1 800 000 × 13 % = **234 000 ₽**.
- Usually withheld monthly by the employer (tax agent); no 3-НДФЛ needed if that is the only income.

### Example 2 — Resident income spanning three bands (band-by-band)

Income: 8 000 000 ₽, resident, no deductions.
- Band 1: 2 400 000 × 13 % = 312 000
- Band 2: (5 000 000 − 2 400 000) = 2 600 000 × 15 % = 390 000
- Band 3: (8 000 000 − 5 000 000) = 3 000 000 × 18 % = 540 000
- **Total НДФЛ = 312 000 + 390 000 + 540 000 = 1 242 000 ₽** (effective rate 15.5 %).
- Note: the 18 % rate hits **only** the 3M slice above 5M, never the whole 8M.

### Example 3 — Very high earner reaching the top band

Income: 60 000 000 ₽, resident.
- Band 1: 312 000; Band 2: 390 000; Band 3: 15 000 000 × 18 % = 2 700 000; Band 4: 30 000 000 × 20 % = 6 000 000; Band 5: (60 000 000 − 50 000 000) = 10 000 000 × 22 % = 2 200 000.
- **Total = 312 000 + 390 000 + 2 700 000 + 6 000 000 + 2 200 000 = 11 602 000 ₽** (effective 19.3 %).

### Example 4 — ИП on ОСНО, documented expenses

Business income 5 000 000 ₽; documented expenses 3 200 000 ₽ (> 20 % of income).
- Use documented method → base = 5 000 000 − 3 200 000 = 1 800 000 ₽.
- All in Band 1 → 1 800 000 × 13 % = **234 000 ₽** annual НДФЛ.
- Paid as quarterly advances (28 Apr / 28 Jul / 28 Oct) with the balance by 15 Jul; 3-НДФЛ by 30 Apr.
- Separately, the ИП charges/declares **НДС at 22 %** on taxable supplies (see russia-vat).

### Example 5 — ИП on ОСНО, 20 % standard professional deduction

Business income 3 000 000 ₽; expenses cannot be documented.
- 20 % standard вычет = 600 000 ₽ → base = 2 400 000 ₽.
- Band 1: 2 400 000 × 13 % = **312 000 ₽** (sits exactly at the band-1 ceiling).
- If documented expenses had been only 400 000 ₽ (< 20 %), the 20 % method is better — choose it.

### Example 6 — Non-resident, Russian-source income

Non-resident (present < 183 days) earns 3 000 000 ₽ of Russian-source consulting income, no special status.
- Flat **30 %** → 3 000 000 × 30 % = **900 000 ₽**. The progressive scale does **not** apply.
- If the person later qualifies as resident for the year, recompute on the progressive scale and reconcile.

## 7. Rules

### Tier 1 — deterministic (apply as written; cite Налоговый кодекс гл. 23)

- **T1-1** — Residency = ≥ 183 days in 12 months → progressive resident scale; else 30 % flat.  _(art. 207, 224)_
- **T1-2** — Resident main scale is **13/15/18/20/22 %** applied **band-by-band on the excess**, never flat on the whole.  _(art. 224)_
- **T1-3** — Bands (2026): 2.4M / 5M / 20M / 50M ₽ boundaries — **verify**.  _(art. 224)_
- **T1-4** — ИП on ОСНО taxable base = business income − professional deduction − other deductions.  _(art. 221, 227)_
- **T1-5** — Professional deduction = documented expenses **or** 20 % standard; one method only.  _(art. 221)_
- **T1-6** — 3-НДФЛ filed by **30 April**; balance paid by **15 July**; ИП advances by **28 Apr / 28 Jul / 28 Oct**.  _(art. 227, 229)_
- **T1-7** — ИП on ОСНО are НДС payers; standard НДС **22 %** from 1 Jan 2026 (Law 425-FZ). НДФЛ and НДС are separate — never net them.  _(Law 425-FZ)_
- **T1-8** — Internal transfers and refunds are not income.

### Tier 2 — reviewer judgement (flag and present options)

- **T2-1** — Choosing between documented vs 20 % professional deduction when close to the break-even.
- **T2-2** — Classifying income into the main scale vs the special 13/15 % passive scale.
- **T2-3** — Non-resident exceptions (ВКС, EAEU, dividends, remote workers) — confirm against current art. 224.  _(art. 224)_
- **T2-4** — Property-sale exemptions and minimum holding periods; имущественный вычет caps.
- **T2-5** — Social/standard/investment deduction caps and their interaction with higher bands.
- **T2-6** — Treatment of СБП / card-to-card receipts for an ИП (audit-sensitive).
- **T2-7** — Worldwide-income reporting for residents with foreign assets/accounts (КИК, treaty suspension).

## 8. Bank Statement Reading Guide

### Russian banks — statement quirks

- **Sberbank / Сбербанк (СберБизнес)** — memos often truncated; `ОПЛАТА ПО ДОГОВОРУ` plus counterparty ИНН.
- **Tinkoff / Т-Банк (Т-Бизнес)** — clean CSV/JSON export; `Назначение платежа` field carries the memo.
- **Alfa-Bank / Альфа-Банк** — `Назначение платежа` field; СБП transfers tagged `Перевод СБП`.
- **VTB / ВТБ**, **Точка**, **Modulbank / Модульбанк** — popular with ИП; exports include ИНН/КПП of payer.

Always reconcile the **назначение платежа** (payment purpose) field plus the counterparty ИНН against the ИП's contracts. Business income for an ИП may legitimately land on a **personal** card — split personal vs business carefully and flag mixed-use accounts.

### Reference checklist

- [ ] Confirm taxpayer type (individual vs ИП on ОСНО) and that ОСНО — not УСН/НПД/ПСН — applies.
- [ ] Establish residency (day count) → choose progressive scale vs 30 %.
- [ ] Separate income into main-scale base and special 13/15 % base.
- [ ] For ИП: compute both deduction methods, choose the better; verify primary documents exist.
- [ ] Apply bands band-by-band; do not flat-rate the whole income.
- [ ] Net off withholding (tax agent) and ИП advances already paid.
- [ ] Confirm 3-НДФЛ filing (30 Apr) and balance payment (15 Jul) dates for the right year.
- [ ] Remind ИП of separate НДС obligations (22 % from 2026) — defer to russia-vat.
- [ ] Mark every figure that requires reviewer/accountant sign-off.

### Test suite (self-check before delivering)

1. Income exactly 2 400 000 ₽ resident → НДФЛ = 312 000 ₽ (all Band 1). ✔
2. Income 5 000 000 ₽ resident → 312 000 + 390 000 = 702 000 ₽. ✔
3. Income 20 000 000 ₽ resident → 312 000 + 390 000 + 2 700 000 = 3 402 000 ₽. ✔
4. ИП income 1 000 000 ₽, no docs → 20 % вычет 200 000 → base 800 000 × 13 % = 104 000 ₽. ✔
5. Non-resident, 1 000 000 ₽ Russian-source, no special status → 300 000 ₽ (30 %). ✔
6. Did you flag residency-unknown as non-resident default? Did you keep НДФЛ and НДС separate? ✔

## PROHIBITIONS

- **Do NOT** apply a single flat rate to the whole income for a resident — the scale is **band-by-band**.
- **Do NOT** assume the bands are indexed; **verify** the current rouble thresholds each filing year.
- **Do NOT** treat an ИП's gross turnover as the НДФЛ base — deduct the professional deduction first.
- **Do NOT** mix the documented-expense and 20 % methods, or apply the 20 % deduction to non-business income.
- **Do NOT** net НДФЛ against НДС; they are separate taxes with separate returns.
- **Do NOT** default an unverified taxpayer to resident — default to **non-resident (30 %)** and flag.
- **Do NOT** advise on under-reporting income, fabricating expenses, backdating primary documents, or disguising business receipts as personal transfers. Refuse such requests.
- **Do NOT** opine on sanctions, foreign-agent status, КИК, or cross-border treaty positions — escalate.
- **Do NOT** file or finalise any 3-НДФЛ without sign-off by a qualified Russian accountant.

## Disclaimer

This skill is **research-verified** against ФНС (nalog.gov.ru), PwC Worldwide Tax Summaries (Russian Federation), and reputable secondary sources, and is current to **tax year 2026** as understood in **May 2026**. It is **not a substitute for professional advice**. Russian tax law — especially non-resident rules, deduction caps, and the НДС rate — changes frequently and is affected by sanctions and treaty suspensions. Every output **must be reviewed and signed off by a qualified Russian accountant** before it is relied upon or submitted to the ФНС. Figures marked "verify current value" must be confirmed against the live Налоговый кодекс гл. 23 and ФНС guidance for the applicable year.

Part of **openaccountants.com** — open-source tax skills for self-employed people.

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
