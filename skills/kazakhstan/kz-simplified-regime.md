---
name: kz-simplified-regime
description: >
  Use this skill whenever asked about Kazakhstan SPECIAL TAX REGIMES for small business and
  individual entrepreneurs (ИП / ЖК) — the simplified declaration regime, the self-employed
  regime, and registration/choice of regime under the NEW 2026 Tax Code. Trigger on phrases
  like "упрощёнка Казахстан", "упрощённая декларация", "Form 910", "Форма 910",
  "simplified declaration Kazakhstan", "ИП налог", "ИП на упрощёнке", "retail tax Kazakhstan",
  "розничный налог", "patent Kazakhstan", "патент Казахстан", "самозанятый Казахстан",
  "self-employed regime Kazakhstan", "E-Salyq Business", "какой налоговый режим выбрать",
  "СНР Казахстан 2026", "регистрация ИП", "оборот лимит ИП", or any request to choose,
  compute, classify, or advise on a Kazakhstan small-business special tax regime under the
  2026 Tax Code. This skill covers the simplified declaration (Форма 910.00, half-year
  filing, turnover ceiling, the combined 4% rate with maslikhat ±50% adjustment), the new
  self-employed regime (replaces the abolished patent / mobile-app regime), eligibility and
  ceilings (employees, turnover, prohibited activities), ИП registration, and what the 2026
  Code CHANGED — including the ABOLITION of the patent, retail tax (розничный налог) and
  fixed-deduction regimes. For business income taxed on the GENERAL regime (ОУР) use
  kz-income-tax. For VAT (НДС) use kazakhstan-vat. For social payments use
  kz-social-contributions.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Kazakhstan Special Tax Regimes for Small Business (СНР) — Self-Employed Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill computes and explains **Kazakhstan special tax regimes** (Russian: *специальные налоговые
режимы*, **СНР**; Kazakh: *арнайы салық режимдері*) for **individual entrepreneurs** (Russian
*индивидуальный предприниматель*, **ИП**; Kazakh *жеке кәсіпкер*, **ЖК**) and very small businesses —
the **simplified declaration regime** (*упрощённая декларация*, **Форма 910.00**) and the new
**self-employed regime** (*режим для самозанятых*). The prose is in English; native Russian and
Kazakh terms are kept inline because the source forms, the State Revenue Committee portal, the
**E-Salyq Business** app, and bank statements use them. **The AI must reply in the language the user
writes in** (Russian, Kazakh, or English).

> **The headline 2026 change.** A NEW Tax Code (signed 18 Jul 2025, effective **1 January 2026**)
> cut the number of special tax regimes from **seven to three**. The **patent regime (патент)**, the
> **retail tax (розничный налог, ст. 696-1)** and the **fixed-deduction regime (фиксированный
> вычет)** were **ABOLISHED**. What survives for the self-employed: (1) the **simplified declaration**
> and (2) the **self-employed regime** (plus the peasant/farm-household regime, out of scope here).
> Do not advise a client to "go on patent" or "use retail tax" for 2026 — those routes are gone.

> **Scope guard.** Special-regime taxpayers from 2026 **cannot be VAT payers** (except import VAT and
> reverse-charge VAT on non-residents). If business income is taxed on the **general established
> regime (ОУР)**, route to **kz-income-tax** (Форма 220.00). For НДС route to **kazakhstan-vat**; for
> ОПВ/ОПВР/СО/ВОСМС route to **kz-social-contributions**.

---

## 1. Quick Reference

| Item | Value |
|---|---|
| Topic | Special tax regimes for small business / ИП — СНР / арнайы салық режимдері |
| Authority | State Revenue Committee — **Комитет государственных доходов (КГД)**, under the Ministry of Finance; portal **kgd.gov.kz**, filing via **cabinet.salyk.kz** / eGov / **E-Salyq Business** app |
| Currency | Kazakhstani tenge — **KZT (₸)** |
| Legislation | **Tax Code of the Republic of Kazakhstan (2026)** — Code No. 214-VIII of 18 Jul 2025, effective **1 January 2026** |
| Tax year | Calendar year (1 Jan – 31 Dec 2026); simplified declaration period = **half-year (полугодие)** |
| Simplified return | **Форма 910.00** + appendix **910.01** (redesigned for 2026) |
| Surviving SNR (2026) | (1) Simplified declaration, (2) Self-employed regime, (3) Peasant/farm (КХ — out of scope) |
| ABOLISHED from 2026 | **Patent (патент)**, **retail tax (розничный налог, ст. 696-1)**, **fixed-deduction (фиксированный вычет)** |
| MCI / МРП (2026) | **4,325 ₸** (месячный расчётный показатель) *(verify on 1 Jan 2026 budget law)* |
| MZP / МЗП (2026) | **85,000 ₸** (minimum monthly wage, unchanged from 2025) |
| Regime-choice deadline | Notification (уведомление) by **1 March 2026**; no notice → auto-moved to ОУР |
| Quality tier | **Research-verified — pending sign-off by a Kazakhstan accountant** |
| Skill version | **1.0** |

### Conservative defaults

When information is missing or ambiguous, the AI applies the **safer** assumption and flags it:

- **Default rate for the simplified declaration = 4%** (the national base rate). Only apply a reduced
  rate (e.g. 2% or 3%) if the user confirms the **maslikhat** (местный представительный орган) of
  their specific district/city set one for their activity. Rates can be adjusted **±50% → 2%–6%**.
- **Assume the client is NOT on patent or retail tax for 2026** — those regimes no longer exist.
  If a client says they were "on patent," explain they were auto-migrated and must re-choose.
- **Assume turnover is measured against the annual ceiling in МРП**, converted at the МРП value in
  force **on 1 January of the year** (4,325 ₸ for 2026), not a current-month МРП.
- **Assume special-regime ИП are NOT VAT payers**; flag if turnover approaches the VAT-registration
  threshold (handled in kazakhstan-vat) — crossing it can force a move to ОУР.
- Where a figure cannot be confirmed against the 2026 Code → give the **formula** + the note
  **"verify under 2026 Tax Code"**. Never invent a maslikhat rate or a precise ceiling in ₸.

---

## 2. The regimes compared

| Feature | **Self-employed** (самозанятые) | **Simplified declaration** (упрощённая декларация) | **General regime** (ОУР) *(reference)* |
|---|---|---|---|
| Form / app | **E-Salyq Business** app (no paper return) | **Форма 910.00** (+ 910.01) | Форма 220.00 (ИП) |
| Filing frequency | Monthly self-assessment in app *(verify)* | **Half-year (semi-annual)** | Annual |
| Turnover ceiling | **300 МРП / month** (≈ **3,600 МРП / year**) | **600,000 МРП / year** | No SNR ceiling |
| Ceiling in ₸ (2026) | ≈ **1,297,500 ₸/month** (300 × 4,325) | ≈ **2,595,000,000 ₸/year** (600,000 × 4,325) | — |
| Employees | **None allowed** | **No statutory limit** (was capped under old code) *(verify)* | Unlimited |
| Tax base | Gross income | Gross turnover (доход) | Income **minus** deductions |
| Headline rate | **0% ИПН + 4% social payments** | **4%** combined (ИПН/КПН), maslikhat ±50% → 2%–6% | 10% / 15% progressive |
| Social tax (СН) | Included in the 4% bundle | **Not separately paid** by ИП on simplified (2026 change) | Paid separately |
| VAT (НДС) | No | No (except import / non-resident reverse charge) | Yes if registered |
| Activities | Restricted to a **government-approved list** | Broad, but **prohibited list** applies (see §3) | Almost all |
| Replaces | **Patent + mobile-app regime** (abolished) | Absorbed the old **retail tax** features | — |

> **Big picture.** The 2026 code pushed the old **patent** crowd down into the **self-employed**
> regime and pulled the old **retail tax** crowd up into the **simplified declaration**. There is no
> longer a "patent" or "retail tax" middle tier.

---

## 3. Eligibility & ceilings

### 3.1 Simplified declaration (упрощённая декларация)

A resident **ИП** or **ТОО** (LLP) may apply the simplified declaration if **all** hold:

- **Annual income ≤ 600,000 МРП** (≈ 2,595,000,000 ₸ for 2026). Exceeding it mid-year forces a
  switch to ОУР from the start of the next quarter/period *(verify transition timing under 2026
  Code)*.
- The activity is **not on the prohibited list**. Commonly excluded: production/sale of
  **excisable goods** (подакцизные товары — alcohol, tobacco, fuel), **lotteries/gambling**,
  certain **financial / subsoil / consultancy / accounting / legal** activities, and grain
  receipts/storage *(confirm the exact 2026 list before relying on it)*.
- The taxpayer is **not a VAT payer** under the special regime (import/non-resident VAT excepted).
- Employee headcount: the old code capped staff (e.g. ~30 for ИП); the **2026 code reportedly
  removed the explicit headcount cap** for the simplified declaration *(verify under 2026 Code)*.

### 3.2 Self-employed regime (самозанятые)

A natural person may use the self-employed regime if **all** hold:

- **Monthly income ≤ 300 МРП** (≈ 1,297,500 ₸ for 2026; ≈ 3,600 МРП per year).
- The activity is on the **government-approved list** of permitted self-employed activities
  *(verify the 2026 list — typically personal services, crafts, tutoring, small trade, etc.)*.
- **No hired employees** (труд работников не используется).
- Cannot simultaneously be a registered ИП for the same activity *(verify)*.
- Tax and social payments are self-assessed through the **E-Salyq Business** mobile app.

> This regime **replaced the patent (патент)** and the "**mobile transfers / E-Salyq**" special
> arrangement. Former patent holders were **auto-migrated to self-employed on 1 Jan 2026**; they
> may de-register or actively choose a different regime instead.

### 3.3 Choosing / switching — the 1 March 2026 trap

To apply a special regime, file a **notification (уведомление о применяемом режиме)** via
cabinet.salyk.kz, E-Salyq Business, a bank app (e.g. Kaspi), or a КГД office. **Deadline:
1 March 2026.** A taxpayer who files no notification is **automatically placed on the general
regime (ОУР)** for the year. Newly registered ИП elect their regime at registration.

---

## 4. Rates & computation (with the 2026 changes)

### 4.1 Simplified declaration — the core formula

Historically (pre-2026) the simplified rate was **3% of turnover**, conceptually split into **~1.5%
individual income tax (ИПН) + ~1.5% social tax (СН)**, declared on the half-year Форма 910.00.

**From 2026 this changed.** The rate is a **single combined 4% of turnover (доход)**, treated as
**ИПН (for ИП) / КПН (for ТОО)**. Critically:

- **Social tax (СН) is no longer paid separately** by ИП on the simplified declaration — it is
  folded into / replaced by the single rate. *(Verify the exact ИПН-vs-СН labelling on the 2026
  Форма 910.00.)*
- **Maslikhats (местные представительные органы)** may move the rate **±50%**, i.e. anywhere from
  **2% to 6%**, by activity and region. Many districts set **2% or 3%** for 2026. Always confirm the
  local rate before computing.

```
Simplified tax = Turnover (полугодовой доход) × applicable rate
applicable rate = 4%  (default)  OR  the maslikhat rate (2%–6%) if confirmed
```

**Separate from the tax above**, the ИП still owes its **own** social/pension payments
(ОПВ, ОПВР, СО, ВОСМС) on its declared income, and — **if it has employees** — payroll obligations
(ИПН, ОПВ, ОПВР, СО, ОСМС, ВОСМС) on wages. Note that simplified-regime employers are reported as
**exempt from social tax on employees** under the 2026 design *(verify)*. For all contribution rates
and bases use **kz-social-contributions**.

### 4.2 Self-employed — the core formula

```
Self-employed payment = Income × 4%   (this 4% is SOCIAL PAYMENTS only)
ИПН = 0%
```

The **4% is a bundle of social payments only** (commonly described as ОПВ / ОПВР / СО / ВОСМС at
~1% each → 4% total) with **ИПН at 0%**. *(Verify the exact split of the 4% under the 2026 Code.)*

### 4.3 What the 2026 Tax Code changed — summary

| Item | Pre-2026 | 2026 Tax Code |
|---|---|---|
| Number of SNR | **7** | **3** (simplified, self-employed, peasant/farm) |
| Patent (патент) | Available | **ABOLISHED** → holders auto-moved to self-employed |
| Retail tax (розничный налог, ст. 696-1) | 4% (some activities) | **ABOLISHED** → features merged into simplified |
| Fixed-deduction regime | Available | **ABOLISHED** |
| Simplified rate | ~3% (≈1.5% ИПН + ≈1.5% СН) | **4% combined**, СН not separate; maslikhat **±50% → 2%–6%** |
| Simplified turnover ceiling | ~24,038 МРП per half-year *(old)* | **600,000 МРП per year** |
| Simplified employee cap | ~30 *(ИП)* | Reportedly **removed** *(verify)* |
| Self-employed ceiling | n/a (patent-based) | **300 МРП/month (≈3,600 МРП/year)**, 0% ИПН + 4% social |
| Special-regime VAT | possible in some cases | **Not VAT payers** (import/non-resident excepted) |

---

## 5. Filing & payment calendar (2026)

| Obligation | Period | File by | Pay by |
|---|---|---|---|
| **Notification of regime** (уведомление) | Year 2026 | **1 Mar 2026** | — |
| **Форма 910.00 — 1st half-year** (Jan–Jun) | H1 2026 | **15 Aug 2026** | **25 Aug 2026** |
| **Форма 910.00 — 2nd half-year** (Jul–Dec) | H2 2026 | **15 Feb 2027** | **25 Feb 2027** |
| **Self-employed** payments (E-Salyq Business) | Monthly | in-app | by the **25th** of the next month *(verify)* |
| **ОПВ/ОПВР/СО/ВОСМС** (own + payroll) | Monthly | — | by the **25th** of the next month |
| **Форма 200.00** (if employees / withholding) | Quarterly | 15th of 2nd month after quarter *(verify)* | 25th |

> The simplified declaration is filed **twice a year (полугодие)** on Форма 910.00; payroll/
> withholding (Форма 200.00) stays **quarterly**. Always re-confirm the exact 2026 due dates on
> cabinet.salyk.kz — half-year deadlines that fall on a weekend roll to the next business day.

---

## 6. Worked examples

> Figures use **МРП 2026 = 4,325 ₸**. Verify the МРП value and any maslikhat rate before relying on
> a result. All examples assume the activity is permitted and turnover stays within ceiling.

### Example 1 — Simplified declaration, default 4%, no employees

Aigerim is an ИП (web design) on the simplified declaration. H1 2026 turnover = **9,000,000 ₸**.
Her district kept the **default 4%**.

```
Simplified tax (H1) = 9,000,000 × 4% = 360,000 ₸
```

She files **Форма 910.00 by 15 Aug 2026** and pays **360,000 ₸ by 25 Aug 2026**. No separate social
tax. She still pays her own ОПВ/ОПВР/СО/ВОСМС monthly (see kz-social-contributions).

### Example 2 — Simplified declaration with a reduced maslikhat rate

Same Aigerim, but her city's **maslikhat set 2%** for IT activity (a −50% reduction).

```
Simplified tax (H1) = 9,000,000 × 2% = 180,000 ₸
```

The reduced rate must be **confirmed for her specific district and activity code (ОКЭД)** — the AI
should not assume it.

### Example 3 — Self-employed regime (replaces patent)

Daniyar tutors privately, was "on patent" in 2025, auto-moved to **self-employed** on 1 Jan 2026.
Monthly income = **400,000 ₸** (≈ 92 МРП, within the 300-МРП ceiling).

```
ИПН            = 0
Social payments = 400,000 × 4% = 16,000 ₸ per month
```

He self-assesses in **E-Salyq Business** and pays ~**16,000 ₸** monthly. If his monthly income ever
exceeds **300 МРП (≈ 1,297,500 ₸)**, he must register as an **ИП** and move to the simplified
declaration (or ОУР).

### Example 4 — Approaching the simplified ceiling

Marat (ИП, retail of non-excisable goods) had H1 turnover of **1,400,000,000 ₸** and projects H2 of
**1,300,000,000 ₸** → full-year ≈ **2,700,000,000 ₸**.

```
Annual ceiling = 600,000 МРП × 4,325 = 2,595,000,000 ₸
Projected 2,700,000,000 ₸  >  2,595,000,000 ₸  → ceiling BREACHED
```

He must move to the **general regime (ОУР)** and review **VAT registration** (kazakhstan-vat). Flag
this early — crossing the ceiling mid-year has transition consequences *(verify exact timing)*.

---

## 7. Tier 2 — refer to a Kazakhstan accountant / КГД

Escalate (do **not** self-resolve) when the matter involves:

- **ТОО (LLP) on the simplified declaration** beyond the basic rate — corporate (КПН) interactions,
  dividends, and accounting thresholds (e.g. the ~135,000 МРП bookkeeping-exemption line) *(verify)*.
- **Mid-year ceiling breach or forced VAT registration** and the precise effective date of the move
  to ОУР.
- **Peasant/farm-household regime (КХ)** — out of scope of this skill.
- **Maslikhat rates** — the exact reduced rate for a specific district + ОКЭД activity code.
- **Prohibited-activity classification** (whether a borderline activity is excluded from a regime).
- **Transition from the abolished patent/retail-tax regimes** including any carry-over balances,
  inventory, or de-registration mechanics.
- **Non-residents, branches, or cross-border** elements.
- Anything requiring the **exact 2026 Форма 910.00 line mapping** or a binding filing position.

---

## 8. Reference (Tax Code) + test suite

### 8.1 Legal & official references

- **Tax Code of the Republic of Kazakhstan (2026)** — Code No. 214-VIII of 18 Jul 2025, effective
  **1 Jan 2026** (special tax regimes chapter; simplified declaration & self-employed regime
  articles — *cite exact article numbers after verifying against the published 2026 Code*).
- **Repealed:** retail tax — former **ст. 696-1** (lost force 1 Jan 2026); patent regime; fixed-
  deduction regime.
- **State Revenue Committee (КГД)** — kgd.gov.kz; filing portal **cabinet.salyk.kz**; **E-Salyq
  Business** app; eGov (egov.kz).
- **PwC Worldwide Tax Summaries** — taxsummaries.pwc.com/kazakhstan (significant developments,
  other taxes) — for cross-checking rates.
- **МРП / МЗП 2026** — annual republican budget law: МРП **4,325 ₸**, МЗП **85,000 ₸** *(verify)*.

### 8.2 Self-check / test suite

The AI should pass all of these before giving a final answer:

1. **Patent request.** User: "Put me on patent for 2026." → Explain patent is **abolished**; offer
   self-employed or simplified instead. ✅
2. **Retail tax request.** User: "I'll use retail tax (розничный налог)." → Explain it is **repealed
   (ст. 696-1)**; features folded into simplified. ✅
3. **Rate default.** Simplified, no local rate confirmed → use **4%**, not 3%, and note maslikhat
   ±50%. ✅
4. **Social tax double-count.** Simplified ИП → do **not** add a separate social tax on top of the
   4% (2026 change). ✅
5. **Self-employed ceiling.** Income 1,500,000 ₸/month → exceeds **300 МРП**; must register ИП /
   move to simplified. ✅
6. **Simplified ceiling.** Annual turnover > **600,000 МРП** → move to ОУР + check VAT. ✅
7. **Deadlines.** H1 Форма 910.00 → file **15 Aug**, pay **25 Aug**; H2 → file **15 Feb**, pay
   **25 Feb** (next year). ✅
8. **Regime-choice trap.** No notification by **1 March** → auto **ОУР**. ✅
9. **VAT.** Special-regime ИП is **not** a VAT payer (import/non-resident excepted). ✅
10. **Language mirroring.** Reply in the user's language (RU/KK/EN) with native terms inline. ✅
11. **МРП conversion.** Convert ceilings using **4,325 ₸** (2026), flagged "verify". ✅
12. **Unverified figure.** Asked for an exact reduced district rate → give the **range 2%–6%** and
    say "confirm with the local maslikhat / КГД". ✅

---

## PROHIBITIONS

The AI must **NOT**:

- **Advise using the patent, retail tax, or fixed-deduction regime for 2026 or later** — all three
  were abolished by the 2026 Tax Code. Treating them as available is a hard error.
- **State a precise reduced (maslikhat) rate as fact** without the user confirming their district +
  activity. Default to 4% and present 2%–6% as the adjustable range.
- **Add a separate social tax (СН) on top of the 4%** for an ИП on the simplified declaration (the
  2026 code folded it in).
- **Confirm exact ₸ ceilings, article numbers, prohibited-activity lists, or due dates as settled
  law** without the "verify under 2026 Tax Code" caveat — the Code is new (in force only since
  1 Jan 2026) and subordinate acts/forms are still settling.
- **Handle VAT, the general regime (ОУР), peasant/farm regimes, ТОО corporate tax, non-residents,
  or social-contribution rates** here — route to the dedicated skills (kazakhstan-vat,
  kz-income-tax, kz-social-contributions) or to Tier 2.
- **File, sign, or submit** anything to КГД, or present output as a final filing position. This
  skill produces **draft computations and guidance only**.

## Disclaimer

This skill is **research-verified** against public 2026 sources (КГД / kgd.gov.kz, PwC Worldwide Tax
Summaries, and Big-4 / professional 2026 reform notes) but is **pending sign-off by a qualified
Kazakhstan accountant or tax adviser**. The 2026 Tax Code (No. 214-VIII) took effect only on
**1 January 2026**; rates, ceilings, МРП/МЗП values, forms (Форма 910.00), prohibited-activity
lists, maslikhat rates, and deadlines may change or be clarified by subordinate regulation. Figures
marked *"verify"* are not yet independently confirmed against the enacted Code. Nothing here is
legal or tax advice for a specific person. Always confirm with the **State Revenue Committee (КГД)**
or a licensed Kazakhstan practitioner before filing or making decisions. Provided by
**openaccountants.com** under its open-source tax-skills project.
