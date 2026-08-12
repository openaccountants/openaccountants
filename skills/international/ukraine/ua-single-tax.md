---
name: ua-single-tax
description: "Ukrainian single tax (єдиний податок) simplified regime for sole proprietors (ФОП): the three FOP groups, income limits, rates, the 1% military levy on Group 3, ЄСВ due on top, employee limits, and barred activities."
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

# UA Single Tax

## Section 1 — Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ukraine |
| Regime | Спрощена система оподаткування (Simplified system) — Єдиний податок |
| Taxpayer | ФОП (фізична особа-підприємець) — sole proprietor / individual entrepreneur |
| Currency | UAH (₴) |
| Tax year | Calendar year |
| Primary legislation | Tax Code of Ukraine (Податковий кодекс), Chapter 1 of Section XIV (єдиний податок) |
| Social contribution | Єдиний соціальний внесок (ЄСВ / USC) — see ua-social-contributions |
| Tax authority | Державна податкова служба (ДПС / State Tax Service) |
| Filing portal | Електронний кабінет платника (cabinet.tax.gov.ua) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Ukrainian accountant/auditor |
| Skill version | 1.0 |

> **Wartime note:** A 1% → 5% increase to the military levy (військовий збір) took effect 1 Dec 2024 and is in force throughout 2026 under martial law. Figures below are as of **1 January 2026**. Fixed amounts are pinned at their 1 Jan value for the whole year and do **not** change mid-year even if the minimum/living wage rises.

### The three FOP groups (2026)

**The three FOP groups (2026)**

|  | Group 1 | Group 2 | Group 3 |
| --- | --- | --- | --- |
| **Who** | Retail trade at markets / personal services to individuals | Services, restaurant, production/sale of goods | Almost any activity; freelancers, IT, consultants |
| **Customers** | Individuals only | Individuals + other single-tax payers | Anyone (incl. companies, foreign clients) |
| **Employees** | 0 | ≤ 10 | Unlimited |
| **Annual income cap** | 167 × min. wage | 834 × min. wage | 1,167 × min. wage |
| **Annual cap (indicative ₴, min wage ₴8,647)** | ≈ ₴1.44 m | ≈ ₴7.21 m | ≈ ₴10.09 m |
| **Single tax** | up to 10% of living wage / month (fixed) | up to 20% of min. wage / month (fixed) | 5% of income (non-VAT) **or** 3% of income (VAT-registered) |
| **Military levy** | 10% of min. wage / month (fixed) | 10% of min. wage / month (fixed) | 1% of income |
| **VAT** | No | No | Optional (3% rate path) |

### Indicative monthly fixed amounts (as of 1 Jan 2026; verify current min/living wage)

**Indicative monthly fixed amounts**

| Item | Basis | Indicative ₴/month |
| --- | --- | --- |
| Living wage (прожитковий мінімум) | — | ₴3,328 |
| Minimum wage (мінімальна зарплата) | — | ₴8,647 |
| Group 1 single tax | 10% × living wage | ≈ ₴332.80 |
| Group 2 single tax | 20% × min. wage | ≈ ₴1,729.40 |
| Groups 1 & 2 military levy | 10% × min. wage | ≈ ₴864.70 |
| ЄСВ (USC), min | 22% × min. wage | ≈ ₴1,902.34 |

**Worked monthly cost, Group 2 (any income up to the cap):** ₴1,729.40 (single tax) + ₴864.70 (military levy) + ₴1,902.34 (ЄСВ) ≈ **₴4,496/month, fixed**, regardless of how much is earned up to the annual cap.

**Worked cost, Group 3 non-VAT:** 5% of turnover (single tax) + 1% of turnover (military levy) + ₴1,902.34/month ЄСВ. On ₴100,000 revenue in a month: ₴5,000 + ₴1,000 + ₴1,902.34 = **₴7,902.34**.

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Group not stated | Group 3, non-VAT (5%) — the freelancer default |
| VAT status unknown (Group 3) | Non-VAT (5% rate) |
| Whether ЄСВ applies | Assume YES — single-tax payers owe ЄСВ even with zero income in 2026 |
| Foreign-currency income date | Date of receipt at NBU rate |
| Activity eligibility unknown | Flag for review — see Section 3 prohibitions |

## Section 2 — Required Inputs and Refusal Catalogue

### Required inputs

- **Minimum:** FOP group, VAT status (Group 3), and full-year bank/turnover records (UAH and any FX accounts).
- **Recommended:** registration extract (виписка з ЄДР) showing КВЕД activity codes, prior-year declaration, ЄСВ payment history.
- **Ideal:** Книга обліку доходів (income ledger), all FX receipts with NBU conversion dates.

### Refusal catalogue

- **R-UA-1** — Income over the group cap. Exceeding the cap triggers a 15% single-tax penalty on the excess and forced transfer to the general system. Escalate.  _(R-UA-1)_
- **R-UA-2** — Barred activities. Single tax is not available for, e.g., excisable goods (except retail fuel within limits), gambling, currency exchange, financial intermediation, mineral extraction, trade in jewellery. Flag and route to general system.  _(R-UA-2)_
- **R-UA-3** — Company (ТОВ). This skill is FOP (individual) only. A ТОВ on single tax (Group 3) is different. Escalate.  _(R-UA-3)_
- **R-UA-4** — Non-resident. Single tax is for Ukrainian-resident FOPs. Escalate.  _(R-UA-4)_

## Section 3 — Eligibility & Activity Rules (Tier 1)

- **Group 3 is the default for freelancers/IT/consultants** because it allows company and foreign clients, has no employee cap, and is turnover-based (no tax in a zero-revenue month except ЄСВ).
- **Barred from the simplified system entirely:** excisable goods production/sale (limited fuel/retail exceptions), gambling/lotteries, FX exchange, financial services and intermediation, extraction/sale of minerals (except certain local), trade in antiques/art via auction, technical testing, and management of enterprises. Such activity in any month forces transfer to the general system.
- **Foreign income:** permitted for Group 3. Convert to UAH at the NBU rate on the date funds arrive in the FOP account. Currency must generally be sold per NBU rules; the UAH proceeds are the single-tax base.

## Section 4 — Rates, Base & Computation (Tier 1)

### Group 3 (turnover-based)

- **Base** — gross income received (cash basis — money in the account / cash received), not profit. Expenses are not deducted under the single tax.  _(Section 4 — Rates, Base & Computation (Tier 1))_
- **Single tax** — 5% (non-VAT) or 3% (VAT-registered, with separate VAT obligations)  _(Section 4 — Rates, Base & Computation (Tier 1))_
- **Military levy** — 1% of the same income base (since 1 Jan 2025 for Group 3)  _(Section 4 — Rates, Base & Computation (Tier 1))_
- **Returns/refunds** — Returns/refunds to customers reduce the base.  _(Section 4 — Rates, Base & Computation (Tier 1))_

### Groups 1 & 2 (fixed)

- **Fixed payment rule** — Pay a fixed monthly single tax (set by the local council up to the statutory cap) plus a fixed monthly military levy, regardless of income, up to the annual cap.  _(Section 4 — Rates, Base & Computation (Tier 1))_

### ЄСВ on top (all groups)

- **ЄСВ minimum** — minimum 22% of the minimum wage per month (≈ ₴1,902.34), payable quarterly. Owed even in months with no income (2026). See ua-social-contributions.  _(Section 4 — Rates, Base & Computation (Tier 1))_

## Section 5 — Filing & Payment Calendar (Tier 1)

**Filing & Payment Calendar**

| Group | Single-tax return | Single-tax payment | Military levy | ЄСВ |
| --- | --- | --- | --- | --- |
| 1 & 2 | Annual (within 60 days of year-end) | Monthly, by 20th | Monthly, by 20th | Quarterly, by 19th of month after quarter |
| 3 | Quarterly (within 40 days of quarter-end) | Quarterly, within 50 days of quarter-end | With the single tax (quarterly) | Quarterly, by 19th of month after quarter |

> From 1 Jan 2026 the separate **monthly** ЄСВ/PIT/military-levy report for sole proprietors is abolished; obligations are reported within the single-tax return / annual cycle. Confirm current ДПС guidance.

## Section 6 — Worked Examples

Receives USD 3,000 from a US client; NBU rate on receipt 41.50 → ₴124,500 income.
Single tax 5% = ₴6,225; military levy 1% = ₴1,245; plus the fixed monthly ЄСВ ₴1,902.34. No expense deduction.

Earns ₴5,000 in the month. Still pays the **fixed** Group 2 single tax (≈₴1,729.40) + military levy (≈₴864.70) + ЄСВ (₴1,902.34) ≈ ₴4,496, because Group 2 is a fixed regime.

A Group 3 FOP hits ₴10.09 m of income in November. Any income above the 1,167 × min-wage cap is taxed at **15%** single tax and the FOP must move to the general system from the next quarter. Flag well before the cap.

## Section 10 — Prohibitions

- **Prohibition — expense deduction** — NEVER deduct business expenses against the single-tax base — it is turnover-based, not profit-based.  _(Section 10 — Prohibitions)_
- **Prohibition — ЄСВ omission** — NEVER omit ЄСВ — it is due on top of the single tax, even in zero-income months (2026).  _(Section 10 — Prohibitions)_
- **Prohibition — military levy omission** — NEVER omit the military levy (1% for Group 3; fixed monthly for Groups 1–2) — it is in force under martial law.  _(Section 10 — Prohibitions)_
- **Prohibition — Group 1/2 misapplication** — NEVER apply Group 1/2 fixed amounts to a freelancer serving companies or foreign clients — that requires Group 3.  _(Section 10 — Prohibitions)_
- **Prohibition — cap excess rate** — NEVER treat income over the group cap as still 5% — the excess is 15% and forces a regime change.  _(Section 10 — Prohibitions)_
- **Prohibition — definitive computation** — NEVER compute a final figure as definitive — direct the client to a Ukrainian accountant/auditor.  _(Section 10 — Prohibitions)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Rates, wage-linked amounts, and martial-law measures change frequently — confirm the current minimum wage, living wage, and military-levy status with the Державна податкова служба before relying on any figure. All outputs must be reviewed and signed off by a qualified professional (a Ukrainian accountant or auditor) before filing.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
