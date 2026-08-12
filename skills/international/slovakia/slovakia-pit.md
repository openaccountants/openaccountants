---
name: slovakia-pit
description: Use this skill whenever asked to prepare, review, or classify transactions for Slovakia Personal Income Tax (Daň z príjmov fyzickej osoby — DPFO), annual return filing, or advise on Slovak PIT deductions and credits. Trigger on phrases like "daň z príjmov", "DPFO", "Slovak income tax", "SZČO", "živnosť", "paušálne výdavky", or any Slovakia personal tax request. ALWAYS read this skill before touching any Slovakia PIT work.
version: 1.0
jurisdiction: SK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - foundation
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia Pit

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Slovenská republika (Slovak Republic) |
| Tax | Daň z príjmov fyzickej osoby (DPFO — Personal Income Tax) |
| Currency | EUR (€) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Current tax year | 2025 |
| Tax authority | Finančná správa SR (Financial Administration) |
| Return form | DPFO typ A (employment only) / DPFO typ B (all income, self-employed) |
| Filing portal | https://www.slovensko.sk |
| Filing deadline | 31 March of following year (extendable to 30 June / 30 September) |
| Source credit | `priznanie-digital/priznanie-digital` (MIT, 40 contributors) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Slovak daňový poradca |
| Skill version | 1.0 |

## Section 2 — Tax rates (Sadzby dane) — 2025

**Tax rates (Sadzby dane) — 2025**

| Taxable base (základ dane) | Rate | Notes |
| --- | --- | --- |
| Up to €100,000 | **15%** | Znížená sadzba (reduced rate) |
| €100,001 – €176,800 (92.8× životné minimum) | **19%** | Základná sadzba |
| Over €176,800 | **25%** | Zvýšená sadzba |

The 15% reduced rate applies to the first €100,000 of taxable base for all taxpayers.

## Section 3 — Key constants (2025)

**Key constants (2025)**

| Constant | Value | Slovak term |
| --- | --- | --- |
| Non-taxable amount (self) | €5,753.79 | Nezdaniteľná časť základu dane |
| Non-taxable amount (partner) max | €5,260.61 | Na manžela/manželku |
| Flat-rate expenses cap | €20,000 | Paušálne výdavky (60% of income, max €20,000) |
| Flat-rate expense percentage | 60% | — |
| Child bonus (≤15 years) | €100/month | Daňový bonus na dieťa |
| Child bonus (>15, ≤18 years) | €50/month | Daňový bonus na dieťa |
| Max child bonus age | 18 | — |
| Minimum income for child bonus | €3,876 | 6× minimum wage |
| Pension savings deduction cap | €180/year | Príspevky na doplnkové dôchodkové sporenie |
| Rental/supplementary income exemption | €500 | Oslobodenie prenájom |
| Minimum tax payable | €5 | Under €5 = no payment required |
| Životné minimum (subsistence minimum) | €268.88/month | Used for various thresholds |

## Section 4 — Non-taxable amounts (Nezdaniteľné časti)

- **Non-taxable amounts (Nezdaniteľné časti)** — Overview of non-taxable amounts on taxpayer and spouse, detailed in subsections below.

### On taxpayer (na daňovníka)

- **Annual non-taxable amount on taxpayer** — €5,753.79 EUR
- **Reduced non-taxable amount when taxable base > €25,426.27** — KONSTANTA(€48,441.43) − taxable base × 0.25
- **Non-taxable amount when taxable base > €48,441.43** — 0

### On spouse (na manžela/manželku)

- **Max non-taxable amount on spouse** — €5,260.61 per year (prorated by months)
- **Conditions** — Spouse lived with taxpayer, had own income below threshold
- **Spouse non-taxable amount calculation** — €17,370.97 − spouse's own income (max €5,260.61)
- **Reduced formula condition** — If taxpayer's base > €25,426.27 → reduced formula applies

## Section 5 — Self-employed (SZČO / Živnostník)

### Expense options

**Expense options**

| Method | Rule |
| --- | --- |
| Paušálne výdavky (flat-rate) | 60% of income, max **€20,000** + social/health insurance paid |
| Skutočné výdavky (actual) | Documented expenses per accounting records |

### Social & health insurance (Odvody)

**Social & health insurance (Odvody)**

| Fund | Rate (self-employed) | Assessment base |
| --- | --- | --- |
| Social insurance (Sociálna poisťovňa) | 33.15% | 50% of taxable base (min/max caps apply) |
| Health insurance (zdravotné) | 14% | 50% of taxable base (min/max caps apply) |

- **Deductibility of insurance** — These are deductible from income before applying flat-rate or actual expenses.

## Section 6 — Computation method

- **Computation method steps** — Step 1: Total income (príjmy) per §5–§8 Step 2: − Expenses (výdavky) — flat-rate or actual Step 3: = Partial base per income type (čiastkový základ dane) Step 4: Sum all partial bases = Total base (základ dane) Step 5: − Non-taxable amount on self (§11 ods.2) Step 6: − Non-taxable amount on spouse (§11 ods.3) Step 7: − Pension savings (max €180) Step 8: = Adjusted taxable base Step 9: Apply rates: 15% on first €100,000; 19% on remainder to €176,800; 25% above Step 10: = Calculated tax (vypočítaná daň) Step 11: − Child bonus (daňový bonus na dieťa) Step 12: − Mortgage interest bonus (daňový bonus na zaplatené úroky) Step 13: − Advance payments / withholding already paid Step 14: = Tax payable or refund (daň na úhradu / preplatok)

## Section 7 — Worked example

Freelance developer (SZČO, živnosť), annual income €45,000, uses flat-rate expenses, single, no children, paid social insurance €4,200 and health insurance €1,800.

**Worked example computation**

| Step | Description | Amount (€) |
| --- | --- | --- |
| Gross income | Príjmy z podnikania §6 | 45,000 |
| − Flat-rate expenses | 60% × 45,000 = 27,000 → capped at 20,000 | (20,000) |
| − Social/health insurance | Actually paid (added to flat-rate) | (6,000) |
| **Partial base** |  | **19,000** |
| − Non-taxable (self) | Nezdaniteľná časť | (5,753.79) |
| **Taxable base** |  | **13,246.21** |
| Tax at 15% | 13,246.21 × 0.15 | **1,986.93** |

## Section 8 — Child bonus (Daňový bonus na dieťa)

**Child bonus amounts**

| Child age | Monthly amount | Annual max |
| --- | --- | --- |
| ≤ 15 years | €100 | €1,200 |
| 16–18 years | €50 | €600 |

- **Conditions for child bonus** — Taxpayer's income must be at least €3,876 (6× minimum wage); Child must live in household; For high-income taxpayers (base > €25,740): bonus may be limited

## Section 9 — Filing guidance

### Which form?

**Which form?**

| Form | Who |
| --- | --- |
| DPFO typ A | Employment income only (§5) |
| DPFO typ B | Self-employed, rental, capital gains, multiple income types |

### Key dates

**Key dates**

| Event | Deadline |
| --- | --- |
| Tax year end | 31 December |
| Standard filing deadline | 31 March |
| Extended (EU/EEA income) | 30 June |
| Extended (foreign non-EU income) | 30 September |
| Payment due | Same as filing deadline |

### Electronic filing

All DPFO typ B returns can be filed via **slovensko.sk** (requires eID with chip). The `priznanie-digital` tool generates compatible XML.

## Section 10 — Advance payments (Preddavky na daň)

**Advance payments (Preddavky na daň)**

| Last year's tax liability | Advance frequency | Amount |
| --- | --- | --- |
| < €5,000 | None required | — |
| €5,000 – €16,600 | Quarterly | 25% of last year's tax |
| > €16,600 | Monthly | 1/12 of last year's tax |

## Section 11 — Conservative defaults

**Conservative defaults**

| Situation | Conservative position |
| --- | --- |
| Expense documentation unclear | Use flat-rate (paušálne výdavky); do NOT claim actuals without proof |
| Child eligibility uncertain | Do not claim bonus; flag for reviewer |
| Partner income unknown | Do not claim non-taxable on spouse; flag |
| Foreign income | Include; flag treaty applicability |
| Crypto gains | Classify as §8 (ostatné príjmy); flag |

## Section 12 — Sources

**Sources**

| Source | URL |
| --- | --- |
| Finančná správa SR | https://www.financnasprava.sk |
| slovensko.sk (e-filing) | https://www.slovensko.sk |
| `priznanie-digital/priznanie-digital` (MIT) | https://github.com/priznanie-digital/priznanie-digital |
| Zákon č. 595/2003 Z. z. o dani z príjmov | — |

## Footer disclaimer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed by a qualified professional before filing.*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
