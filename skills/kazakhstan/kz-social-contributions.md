---
name: kz-social-contributions
description: >
  Use this skill whenever asked about Kazakhstan mandatory social payments for the
  self-employed (ИП / individual entrepreneurs) or for employers — pension contributions,
  social contributions, medical insurance, and social tax. Trigger on phrases like
  "ОПВ Казахстан", "ОПВР", "социальные отчисления", "ОСМС", "социальный налог",
  "social contributions Kazakhstan ИП", "Kazakhstan payroll contributions 2026",
  "сколько платит ИП за себя", "пенсионные взносы Казахстан", or any request to compute
  what an individual entrepreneur or employer owes to the pension fund (ЕНПФ/UAPF),
  the State Social Insurance Fund (ГФСС), or the Social Health Insurance Fund (ФСМС).
  Covers tax year 2026 under the new Tax Code effective 1 January 2026. The AI must reply
  in the user's language (Russian, Kazakh, or English). Does NOT cover individual income
  tax (ИПН), VAT (НДС), corporate tax, or the simplified declaration mechanics themselves —
  this skill only computes the social-payment layer that sits on top of any regime.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on: [social-contributions-workflow-base]
---

# Kazakhstan Mandatory Social Payments — Self-Employed (ИП) & Employers (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill computes the five mandatory social payments that Kazakhstan layers on top of
income tax: **ОПВ** (employee pension), **ОПВР** (employer pension), **СО** (social
contributions / социальные отчисления), **ОСМС** (mandatory social health insurance /
обязательное социальное медицинское страхование), and **социальный налог** (social tax).
It covers the rules for individual entrepreneurs (ИП) and for employers paying staff, for
tax year 2026 under the new Tax Code (Налоговый кодекс) effective 1 January 2026.

The AI applying this skill replies in the **user's language** — Russian, Kazakh, or
English — but keeps the native abbreviations (ОПВ, ОПВР, СО, ОСМС, СН) and the units
МЗП (minimum monthly wage) and МРП (monthly calculation index) intact, since these are the
legal terms used on filings.

## 1. Quick Reference

| Field | Value |
|---|---|
| Country | Kazakhstan (Республика Казахстан) |
| Tax year | 2026 |
| Authorities | State Revenue Committee (КГД / KGD) under the Ministry of Finance; State Social Insurance Fund (ГФСС); Social Health Insurance Fund (ФСМС); Unified Accumulative Pension Fund (ЕНПФ / UAPF) |
| Currency | KZT (Kazakhstani Tenge, ₸) only |
| МЗП (minimum monthly wage / МЗП / ең төмен жалақы) | **85,000 ₸** for 2026 (unchanged from 2025) |
| МРП (monthly calculation index / МРП / айлық есептік көрсеткіш) | **4,325 ₸** for 2026 (was 3,932 ₸ in 2025) |
| Collection portal | https://cabinet.salyk.kz (КГД); ЕНПФ for pension |
| Legal basis | New Tax Code of RK (eff. 1 Jan 2026); Law "On Compulsory Social Health Insurance"; Law "On Compulsory Social Insurance"; Social Code of RK |
| Quality tier | **Research-verified — pending sign-off by a Kazakhstan accountant** |
| Version | 1.0 |
| Companion skill | **social-contributions-workflow-base — MUST be loaded** |

**Rate table (2026):**

| Payment | Abbrev. | Rate | Base | Who pays |
|---|---|---|---|---|
| Mandatory pension contributions | ОПВ | 10% | Income (employee) or chosen income (ИП) | Employee / ИП for self |
| Employer mandatory pension contributions | ОПВР | 3.5% (2026 step) | Employee income or ИП chosen income | Employer / ИП for self |
| Social contributions | СО | 5% | Income less ОПВ (employee); chosen income (ИП) | Employer / ИП for self |
| Mandatory social health insurance | ОСМС | Employee withheld **2%**; employer **3%** | Employee income; ИП uses **1.4 МЗП** as fixed base | Employer + employee / ИП for self |
| Social tax | Социальный налог (СН) | Employer **6%** of payroll; **ИП on general regime (ОУР): 2 МРП for self + 1 МРП per employee** | Gross remuneration / fixed МРП for ИП | Employer / ИП on ОУР |

**ОПВР phase-in schedule (employer pension, ОПВР):** 1.5% (2024) → 2.5% (2025) → **3.5% (2026)** → 4.5% (2027) → 5.0% (2028). Applies for employees born after 1 January 1975.

**Conservative defaults (apply when a fact is unknown):**

| Ambiguity | Default |
|---|---|
| ИП declared income unknown | Use the **minimum base = 1 МЗП** for ОПВ/ОПВР/СО, and 1.4 МЗП for ОСМС |
| Regime unknown (simplified vs general) | Assume the heavier path and **flag for verification** |
| Whether ИП on simplified pays social tax | Assume **no social tax on simplified** (2026 change), flag |
| Date of birth unknown (ОПВР eligibility) | Assume **born after 1 Jan 1975** → ОПВР applies |
| Income above the ceiling | Apply the **cap** (50 МЗП for ОПВ/ОПВР; 7 МЗП for СО) |
| СО base for ИП (ambiguous, see §3.3) | Use chosen income with **1 МЗП floor / 7 МЗП cap**, flag |

## 2. Who Pays What

There are three actors. The same person can wear more than one hat (an ИП who also
employs staff pays both for themselves and for each employee).

**Individual entrepreneur (ИП) paying for themselves ("за себя"):**

| Payment | Does ИП pay it? | Notes |
|---|---|---|
| ОПВ | Yes | 10% on a self-chosen income, 1 МЗП–50 МЗП |
| ОПВР | Yes | 3.5% in 2026 on the same chosen income |
| СО | Yes | 5% on chosen income, 1 МЗП–7 МЗП |
| ОСМС | Yes | Fixed: 5% of 1.4 МЗП (see §3.4) |
| Социальный налог | **Only on the general regime (ОУР)** — 2 МРП. On the **simplified regime the ИП no longer pays social tax in 2026** | Major 2026 change |

**Employee (наёмный работник) — amounts withheld from gross salary:**

| Payment | Withheld from employee? | Rate |
|---|---|---|
| ОПВ | Yes | 10% |
| ОСМС | Yes | 2% |
| ОПВР, СО, social tax | No — these are employer costs | — |

**Employer (работодатель / ТОО or ИП with staff) — paid on top of salary:**

| Payment | Employer pays? | Rate |
|---|---|---|
| ОПВР | Yes | 3.5% (2026) |
| СО | Yes | 5% |
| ОСМС (employer share) | Yes | 3% |
| Социальный налог | Yes | 6% of payroll (general); 1 МРП per employee for ИП on ОУР |
| ОПВ, ОСМС employee share | Withheld and remitted (employee's money) | 10% / 2% |

## 3. Each Payment — Base, Rate, Minimum, Ceiling

### 3.1 ОПВ — Mandatory Pension Contributions (обязательные пенсионные взносы)

- **Rate:** 10%.
- **Employee base:** gross income.
- **ИП base:** a **self-declared income** that the ИП chooses, bounded below by **1 МЗП**
  and above by **50 МЗП**.
- **Minimum (ИП, monthly):** 1 МЗП × 10% = 85,000 × 10% = **8,500 ₸**.
- **Ceiling (monthly):** 50 МЗП × 10% = 4,250,000 × 10% = **425,000 ₸**.
- Remitted to ЕНПФ (UAPF).

### 3.2 ОПВР — Employer Mandatory Pension Contributions (обязательные пенсионные взносы работодателя)

- **Rate (2026):** **3.5%** (phase-in: 1.5→2.5→3.5→4.5→5.0%).
- **Base:** employee income (employer) or ИП chosen income, **1 МЗП–50 МЗП**.
- **Applies to:** persons **born after 1 January 1975**. Not paid for older workers.
- **Minimum (ИП, monthly):** 1 МЗП × 3.5% = **2,975 ₸**.
- **Ceiling (monthly):** 50 МЗП × 3.5% = **148,750 ₸**.
- Paid from the employer's / ИП's own funds; **not** deducted from the worker. Remitted to ЕНПФ.

### 3.3 СО — Social Contributions (социальные отчисления)

- **Rate:** **5%**.
- **Employee base:** income **less ОПВ** (i.e. gross − 10% ОПВ), bounded 1 МЗП–7 МЗП.
- **ИП base:** a chosen income, floor **1 МЗП**, **cap 7 МЗП**.
- **Minimum (monthly):** 1 МЗП × 5% = **4,250 ₸**.
- **Ceiling (monthly):** 7 МЗП × 5% = 595,000 × 5% = **29,750 ₸**.
- Paid to the State Social Insurance Fund (ГФСС). **Social-tax interaction changed in 2026:**
  social tax is **no longer reduced by СО** (the old СН − СО offset is abolished — see §3.5).
- **Ambiguity (verify):** the exact СО base for ИП under the new Tax Code — specifically
  whether ОПВ is subtracted before applying 5% — is reported as unsettled in 2026 practice.
  Default to chosen income with the 1 МЗП floor and flag for the reviewer.
- A reduced **1% СО rate** applies to self-employed persons using the special "единый платёж /
  СНР для самозанятых" regime; do not apply this unless the user confirms that regime.

### 3.4 ОСМС — Mandatory Social Health Insurance (обязательное социальное медицинское страхование)

- **Employee withholding:** **2%** of income (cap 20 МЗП monthly base).
- **Employer contribution:** **3%** of employee income in 2026 (income cap 10 МЗП per
  employee → max base 850,000 ₸; PwC also notes a 3,400,000 ₸ income cap reference).
- **ИП for themselves:** a **fixed** contribution of **5% of 1.4 МЗП**.
  - 1.4 × 85,000 = 119,000 ₸ base × 5% = **5,950 ₸ per month**.
- Remitted to the Social Health Insurance Fund (ФСМС).

### 3.5 Социальный налог — Social Tax (социальный налог / СН)

- **Employer (general regime / ОУР):** **6%** of gross employee remuneration.
- **ИП on the general regime (ОУР):** a **fixed** social tax of **2 МРП for the ИП themselves**
  plus **1 МРП per employee**, per month.
  - 2 МРП = 2 × 4,325 = **8,650 ₸** for self.
  - 1 МРП = **4,325 ₸** per employee.
- **ИП on the simplified regime (упрощёнка):** **does not pay social tax in 2026** (change
  under the new Tax Code). Verify the user's regime before applying.
- **2026 change:** social tax is **no longer reduced by social contributions (СО)**. The
  previous СН − СО offset is abolished, which raises the effective burden.

## 4. Computation & Worked Examples

All examples use 2026 values: **МЗП = 85,000 ₸**, **МРП = 4,325 ₸**.

### Example 1 — ИП on the simplified regime, paying the minimum for themselves only

The ИП declares the minimum base (1 МЗП) and has no employees. On the simplified regime,
no social tax is due in 2026.

| Payment | Computation | Monthly amount |
|---|---|---|
| ОПВ | 85,000 × 10% | 8,500 ₸ |
| ОПВР | 85,000 × 3.5% | 2,975 ₸ |
| СО | 85,000 × 5% | 4,250 ₸ |
| ОСМС | 1.4 × 85,000 × 5% | 5,950 ₸ |
| Социальный налог | none (simplified) | 0 ₸ |
| **Total social payments** | | **21,675 ₸ / month** |

These social payments sit **on top of** the simplified-regime income tax (ИПН + social tax
component of the simplified declaration), which this skill does not compute.

### Example 2 — ИП on the general regime (ОУР), one employee, ИP declares 3 МЗП for self

ИП chosen income for self = 3 МЗП = 255,000 ₸. Employee gross salary = 300,000 ₸/month
(born after 1975).

**ИП for themselves:**

| Payment | Computation | Amount |
|---|---|---|
| ОПВ | 255,000 × 10% | 25,500 ₸ |
| ОПВР | 255,000 × 3.5% | 8,925 ₸ |
| СО | 255,000 × 5% (within 7 МЗП cap) | 12,750 ₸ |
| ОСМС | 1.4 × 85,000 × 5% (fixed) | 5,950 ₸ |
| Социальный налог (self) | 2 МРП | 8,650 ₸ |
| **Subtotal (self)** | | **61,775 ₸** |

**For the employee (salary 300,000 ₸):**

| Payment | Who | Computation | Amount |
|---|---|---|---|
| ОПВ | withheld | 300,000 × 10% | 30,000 ₸ |
| ОСМС (employee) | withheld | 300,000 × 2% | 6,000 ₸ |
| ОПВР | employer | 300,000 × 3.5% | 10,500 ₸ |
| СО | employer | (300,000 − 30,000 ОПВ) × 5% | 13,500 ₸ |
| ОСМС (employer) | employer | 300,000 × 3% | 9,000 ₸ |
| Социальный налог | employer | 1 МРП per employee | 4,325 ₸ |

Employer's own cost for this employee (ОПВР + СО + ОСМС-employer + СН) = **37,325 ₸**.
Withheld from the employee (ОПВ + ОСМС) = 36,000 ₸ (the employee's money, remitted by the ИП).

### Example 3 — High earner hitting the ceilings (ИП declaring 60 МЗП)

The ИП wants to contribute on 60 МЗП = 5,100,000 ₸, but the ceilings cap each payment.

| Payment | Cap applied | Capped base | Amount |
|---|---|---|---|
| ОПВ | 50 МЗП | 4,250,000 ₸ | 425,000 ₸ |
| ОПВР | 50 МЗП | 4,250,000 ₸ | 148,750 ₸ |
| СО | 7 МЗП | 595,000 ₸ | 29,750 ₸ |
| ОСМС | fixed 1.4 МЗП | 119,000 ₸ | 5,950 ₸ |

Note how СО caps far earlier (7 МЗП) than the pension payments (50 МЗП), and ОСМС is a
flat fixed amount that does not scale with declared income at all.

## 5. Payment Calendar

| Payment | Due date |
|---|---|
| ОПВ, ОПВР | By the **25th** of the month following the reporting month (to ЕНПФ) |
| СО | By the **25th** of the following month (to ГФСС via the State Corporation) |
| ОСМС | By the **25th** of the following month (to ФСМС) |
| Социальный налог | Declared and paid by the **25th** of the following month |
| ИП "за себя" social payments | Commonly remitted monthly; some ИП settle quarterly or by year end — **verify the client's schedule** |
| Reporting form | Form **200.00** (quarterly) reconciles individual income tax and social payments for employers; ИП-only payments may flow through the relevant declaration. Verify form for the client's regime. |

All payments use a single State Corporation "Government for Citizens" channel for СО/ОСМС
and ЕНПФ for pension. Always confirm the current 2026 deadlines against КГД before filing.

## 6. Tier 2 — Ambiguities and Escalation

Escalate to a Kazakhstan accountant (do not auto-decide) when:

1. **СО base for ИП** — whether ОПВ is deducted before the 5% (see §3.3). Unsettled in 2026.
2. **Regime classification** — whether the client is truly on simplified (упрощёнка), general
   (ОУР), retail tax, or the self-employed единый платёж. Social-tax liability turns on this.
3. **ОПВР eligibility** — date-of-birth cutoff (after 1 Jan 1975) and any exempt categories.
4. **Special categories** — pensioners, persons with disabilities, recipients of certain
   benefits, and foreign/EAEU workers have modified or exempt treatment. Out of scope here.
5. **Caps interaction across multiple income sources** — an individual with both employment
   and ИП income must aggregate against the ceilings; coordination rules need a human.
6. **Mid-year rate or МЗП/МРП changes** — if the budget law is amended mid-2026, recompute.

## 7. Reference + Test Suite

**Reference figures (2026):** МЗП = 85,000 ₸; МРП = 4,325 ₸. Ceilings: ОПВ/ОПВР = 50 МЗП;
СО = 7 МЗП; ОСМС employee = 20 МЗП cap, employer = 10 МЗП cap; ИП ОСМС fixed base = 1.4 МЗП.

**Authorities to cross-check before sign-off:** КГД (kgd.gov.kz / cabinet.salyk.kz),
ГФСС (State Social Insurance Fund), ФСМС (fms.kz), ЕНПФ (enpf.kz), and Big-4 2026 notes
(PwC Kazakhstan "Individual — Other taxes").

**Test suite (the AI must reproduce these):**

| # | Scenario | Expected |
|---|---|---|
| T1 | ИП, simplified, minimum, no staff | 21,675 ₸/month total; social tax = 0 |
| T2 | ИП ОПВ minimum | 8,500 ₸ |
| T3 | ИП ОПВР minimum | 2,975 ₸ |
| T4 | ИП СО minimum | 4,250 ₸ |
| T5 | ИП ОСМС fixed | 5,950 ₸ |
| T6 | ИП social tax for self (ОУР) | 2 МРП = 8,650 ₸ |
| T7 | Social tax per employee (ИП ОУР) | 1 МРП = 4,325 ₸ |
| T8 | СО cap | 7 МЗП × 5% = 29,750 ₸ |
| T9 | ОПВ cap | 50 МЗП × 10% = 425,000 ₸ |
| T10 | Employee ОПВ + ОСМС withheld on 300,000 ₸ | 30,000 + 6,000 = 36,000 ₸ |
| T11 | Reply language | AI answers in the user's language, keeps ОПВ/ОПВР/СО/ОСМС/СН and МЗП/МРП verbatim |

## PROHIBITIONS

- Do **not** compute individual income tax (ИПН), VAT (НДС), corporate income tax (КПН),
  or the simplified-declaration tax itself — this skill is only the social-payment layer.
- Do **not** advise on pension fund **withdrawals**, voluntary pension contributions, or
  investment returns in ЕНПФ.
- Do **not** handle special categories (pensioners, persons with disabilities, foreign/EAEU
  workers, civil servants, military) — escalate.
- Do **not** assert a rate as final if any 2026 figure is unverified; present the **formula**
  and write "verify against КГД/ГФСС/ФСМС/ЕНПФ".
- Do **not** file or submit on the client's behalf. Output is for a human accountant to review.
- Do **not** apply the 1% special-regime СО rate or the simplified "no social tax" rule
  without confirming the client's exact regime.

## Disclaimer

This skill is **research-verified** against public 2026 sources (КГД, ЕНПФ, PwC Kazakhstan,
and Kazakh accounting press) but is **pending sign-off by a qualified Kazakhstan accountant**.
The new Tax Code took effect 1 January 2026 and rates/bases (especially the ОПВР phase-in,
ОСМС shares, and the СО base for ИП) are subject to amendment and differing interpretations.
All figures must be confirmed against the State Revenue Committee (kgd.gov.kz), the State
Social Insurance Fund (ГФСС), the Social Health Insurance Fund (ФСМС), and ЕНПФ before use on
a real filing. No liability is accepted for reliance on unverified figures. Provided as part
of the open-source tax skills project at openaccountants.com.
