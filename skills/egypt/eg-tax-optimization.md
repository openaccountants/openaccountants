---
name: eg-tax-optimization
description: Use this skill whenever asked about legitimate tax optimization, tax planning, or how to legally reduce tax for self-employed people, freelancers, professionals, sole proprietors, and small businesses in Egypt. Trigger on phrases like "reduce tax Egypt", "save tax freelancer Egypt", "simplified vs general Egypt", "Egypt tax planning", "SME regime worth it Egypt", "lower my tax bill Egypt", "is the simplified regime cheaper", "تخطيط ضريبي مصر", "تقليل الضرائب مصر", "النظام المبسط أم العام", "هل النظام المبسط أوفر", "توفير ضرائب". Covers the choice between the turnover-based simplified SME regime (Law No. 6 of 2025) and the general progressive income-tax system, the break-even logic, e-invoicing as a deductibility lever, VAT threshold management, and the Law No. 5 of 2025 dispute-settlement / amnesty facilities. LEGAL planning only , never tax evasion. AI replies in the user's language (English or Arabic).
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Tax Optimization v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. What this file is

The decision layer for lawful tax planning by self-employed people and small businesses in Egypt, tax year 2026. It loads on `income-tax-workflow-base` and produces a side-by-side computation for a reviewer. Reply in the user's language, English or Arabic. Planning only: never concealment, fake invoices or sham entities.

## 2. Scope statement

Covers: regime choice, e-invoicing, VAT registration timing, reliefs, settlement windows. Mechanics sit elsewhere: `eg-sme-tax`, `eg-income-tax`, `egypt-vat`, `eg-bookkeeping`.

## 3. Filing requirements

Choosing the turnover regime: form 10/1 طلبات, five-year lock-in. Annual return dates are in `eg-income-tax` and `eg-sme-tax`.

## 4. Rates and thresholds

Band tables live in `eg-income-tax` and `eg-sme-tax`. Figures owned here:

| Item | Amount | Conditions | Official URL |
|---|---|---|---|
| Dispute committees | Open to 31 December 2026 | Law 152/2026 renews Law 79/2016 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.152.of_.2026.pdf |
| Dispute application | Form to ETA, or free on its portal | MoF decision 450/2026 | https://eta.gov.eg/sites/default/files/2026-08/mof.qarar_.no_.450.of_.2026.pdf |
| Past-period settlement | Turnover under 10,000,000 | Law 151/2026 art. 4, from 1 Jan 2023 as corrected; table in `eg-sme-tax` | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf |
| Ceiling on delay charge | 100% of principal | Law 7/2025 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |

## 5. Computation rules

1. Get turnover, profit, documentation state, plans for five years.
2. Compute general tax on profit with the row table.
3. Compute turnover × band rate. Check art. 3 conditions and art. 4 exclusions.
4. Add the non-rate effects: dividends, asset gains, stamp duty, withholding, audit timing, quarterly VAT.
5. Show both numbers, then recommend. Never recommend in the abstract.

| Situation | Direction |
|---|---|
| Few costs, turnover up to 20m | Turnover regime, if not 90% consulting for one or two clients |
| Thin margin, heavy documented costs | Compute: the general system often wins |
| Losses expected | General: turnover tax is due on a loss, losses carry five years |
| Plans to pass 24m, or a second breach | General, or model the exit |
| Needs freedom to change within five years | General |
| Poor cost documents | Fix documents, then compare |

Worked side by side:

**Persona A. Developer, turnover 1,800,000, costs 200,000, profit 1,600,000.** General: 25% on 1,200,000 + 27.5% on 400,000 = 410,000. Turnover: 0.5% = 9,000. Saving 401,000.

```oa-check
name: Developer regime decision
inputs:
  turnover: 1800000
  profit: 1600000
steps:
  - general: 1200000 * 0.25 + (profit - 1200000) * 0.275
  - simplified: turnover * 0.005
  - saving: general - simplified
expected:
  general: 410000.00
  simplified: 9000.00
  saving: 401000.00
```

**Persona B. Trader, turnover 9,000,000, profit 350,000.** Turnover: 90,000. General: 1,500 + 2,250 + 26,000 + 33,750 = 63,500. The general system saves 26,500 if every cost is documented.

```oa-check
name: Thin-margin trader decision
inputs:
  turnover: 9000000
  profit: 350000
steps:
  - simplified: turnover * 0.01
  - general: 1500 + 2250 + 26000 + (profit - 200000) * 0.225
  - general_saves: simplified - general
expected:
  simplified: 90000.00
  general: 63500.00
  general_saves: 26500.00
```

**Persona C. New consultant, turnover 240,000.** Compare the two, and check the VAT threshold in `egypt-vat` before crossing it.
**Persona D. Old dispute.** Law 5/2025 windows have closed; use the committees to 31 December 2026 or the Law 151 art. 4 settlement if eligible.

## 6. Edge cases and special rules

- **Row steps:** income just over 600,000, 700,000, 800,000, 900,000 or 1,200,000 loses a band. A legitimate timing of a real receipt or a real expense can matter; invented timing cannot.
- **Law 5/2025 windows are closed.** Non-filers had six months from 13 Feb 2025 (art. 3). Unregistered taxpayers and dispute applicants had three months, extended three more from 13 May 2025 by MoF decision 167/2025. All ended by mid August 2025. Payment and installment rules of those cases stay with cases already running.
- **Listed shares:** gains exempt from 29 Jul 2026, losses lost (`eg-income-tax`).
- **E-invoices:** art. 3 of Law 6 makes them a condition of the turnover regime. On the general system, regular books backed by documents support costs (Law 91 art. 28).
- **Lock-in:** form 11/1 is available only after five years.

## 7. Self-checks

Inputs trace to documents; rates match 2026; both systems computed; row chosen on total income; exclusions checked; no figure repeated from a sibling without its link; nothing here needs concealment.

## 8. Sources

| Source | URL | Read on |
|---|---|---|
| Law 5 of 2025, whole text (OCR) | https://eta.gov.eg/sites/default/files/2025-02/law_no.5.of_.2025.pdf | 2026-11-01 |
| Law 7 of 2025, whole text (OCR) | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-01 |
| Law 152 of 2026, whole text (OCR) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.152.of_.2026.pdf | 2026-11-01 |
| MoF decision 450 of 2026, arts. 1 and 2 (OCR) | https://eta.gov.eg/sites/default/files/2026-08/mof.qarar_.no_.450.of_.2026.pdf | 2026-11-01 |
| Correction notice, page image of the Law 151 table | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-01 |
| ETA Services Guide, 2nd edition, section 18 | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-01 |

Not yet confirmed: the rule that only e-invoices prove costs and input VAT from 1 July 2023. VAT registration threshold changes, Resolution 281 of 2025 and its fine: left to `egypt-vat`. Whether Law 5 relief has a successor beyond Laws 151 and 152 of 2026. The insurance and pension relief cap (see `eg-income-tax`).

## 9. Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

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
