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
| Turnover over 20m and outside the tolerance | General is the only option |
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
- **E-invoices:** art. 3 of Law 6 makes them a condition of the turnover regime. On the general system, regular books backed by documents support costs (Law 91 arts. 22, 23).
- **Splitting:** one business split with no economic reason to stay under 20m is outside Law 6 (art. 4 item 2). Do not design it.
- **Lock-in:** form 11/1 is available only after five years.

**Carried from the earlier version, not checked against the law.** Kept so no working rule is lost. Any figure here is unverified, and where it differs from the tables above the tables win.

- **Assume the general system unless eligibility for the simplified regime is confirmed.** Quote the simplified regime as an *option to evaluate*, not as the default.
- **Never assert a saving without numbers.** Always show the side-by-side computation (turnover × simplified rate vs profit × progressive bracket) before recommending.
- **Treat the 5-year lock-in as binding.** Electing the simplified regime under Law 6/2025 cannot be reversed for five years from the day after the request is submitted. Flag this prominently before recommending the election.
- When two readings are possible, choose the one that keeps the taxpayer compliant and audit-safe, even if marginally more tax is paid.

Because the simplified regime taxes turnover and the general system taxes profit, the decision hinges on the taxpayer's **profit margin** (صافي الربح ÷ رقم الأعمال).

- **High-margin, low-cost businesses** (e.g. a freelance developer or consultant with few deductible costs) → profit ≈ turnover, so the general system taxes nearly the whole amount at rates up to 27.5%. The simplified regime at <1.5% is **dramatically cheaper**.
- **Low-margin businesses** (e.g. trading/retail reselling goods with thin margins) → a turnover tax can bite, because even a small % of a large turnover may exceed the income tax on a thin profit. Run the numbers.
**2.3 Decision table**

**Decision table**

| Situation | Likely better regime | Why |
| --- | --- | --- |
| unverified: Freelancer/consultant, few costs, profit margin > ~40%, turnover ≤ 20m | **Simplified** | Turnover tax <1.5% beats up to 27.5% on near-full profit |
| unverified: Low-margin trader/retailer (margin < ~10%) | **Often general** | Turnover tax can exceed income tax on a thin profit: model it |
| unverified: Turnover above EGP 20m | **General (only option)** | Above simplified eligibility ceiling |
| Heavy genuine deductible costs, modest profit | **Model both** | Deductions shrink the general-system base; compare carefully |
| unverified: Wants flexibility to change soon | **General** | Simplified locks in for **5 years** |
| Poor documentation / can't issue e-invoices | **Model both, fix docs first** | Without e-invoices, costs are disallowed on the general system, pushing toward simplified |

**Always produce the two numbers.** Do not recommend a regime in the abstract.
- **E-invoice deductibility requirement**: On the general system, the value of deductions depends entirely on documentation. Since 1 July 2023, for taxpayers registered on the e-invoice system, only electronic invoices (الفاتورة الإلكترونية) count as valid evidence of deductible costs and expenses for income-tax purposes, and only e-invoices/e-receipts support input-VAT deduction or refund (verify).

- **A cost without a valid e-invoice is effectively a non-deduction.** It raises taxable profit and the tax bill. Optimising the general system therefore *starts* with getting suppliers to issue compliant e-invoices and issuing your own.
- **Input VAT on paper invoices is lost**: non-electronic invoices are not accepted for VAT input credit or refund.
- The **simplified regime** is more forgiving on cost documentation (tax is on turnover, not profit), but e-invoicing/e-receipt integration is itself an **eligibility condition** of Law 6/2025, plus timely return filing. So e-invoicing is mandatory either way; on the general system it is also the gate to your deductions.

**Optimization actions:** register on the ETA e-invoice/e-receipt system; require e-invoices from every supplier before paying; reconcile e-invoices to the books monthly; never rely on paper or PDF invoices for a deduction.
- **Mandatory VAT (and e-invoicing) registration threshold**: Reduced from EGP 500,000 to EGP 250,000 of annual turnover under Resolution No. 281 of 2025 (verify). Businesses whose 2025 gross revenue exceeded EGP 250,000 must register with ETA before 31 March 2026 or face penalties (reported as an EGP 20,000 fine plus EGP 1,000/day: verify).
- **Turnover definition for threshold**: "Turnover" for the threshold is gross revenue before costs: a business with EGP 260,000 revenue and EGP 20,000 net profit is still in scope.

- **Do not artificially fragment or suppress turnover to stay under the threshold**: that is evasion, not planning (see PROHIBITIONS). Splitting one business into sham entities is illegal.
- Legitimate timing: a genuinely seasonal or growing business should **monitor cumulative turnover** and register on time to avoid penalties; voluntary early registration can be sensible where customers are themselves VAT-registered (your VAT is recoverable to them) and where you want input-VAT recovery on your own costs.
- On the simplified regime, VAT registrants benefit from **quarterly** filing: a real compliance-cost saving.
- **Law No. 5 of 2025 facilities**: Law No. 5 of 2025 (in force from 13 February 2025) is a one-off facilitation window worth checking for any taxpayer with a backlog (verify): **Penalty/interest waiver:** up to a 100% waiver of penalties, late fees and additional tax where the principal tax is paid promptly. **Non-filers (2020 → 13 Feb 2025):** relief from penalties if outstanding or amended returns are filed within six months of 13 February 2025. **Unregistered taxpayers:** no tax obligations imposed for periods before 13 February 2025 (income tax, VAT, stamp tax, development fee) if they register within three months of that date. **Old disputes (pre-2020):** fast-track settlement: pay the principal within set windows and have delay fines / additional tax forfeited.

**Timing caveat: verify the windows have not closed.** Today is **May 2026**. The six-month and three-month windows above ran from 13 February 2025 and have **likely expired**. Treat Law 5/2025 as relevant mainly for *already-initiated* settlements or any extension/successor facility. **Confirm current availability with ETA / a qualified accountant before relying on it.**
- Turnover: **EGP 1,800,000**; deductible costs ≈ EGP 200,000; net profit ≈ **EGP 1,600,000**.
- **Simplified system:** turnover EGP 1,800,000 falls in the 0.5% band → **EGP 9,000**.
- Turnover: **EGP 9,000,000**; cost of goods + costs ≈ EGP 8,400,000; net profit ≈ **EGP 600,000**.
- **Simplified system:** EGP 9,000,000 in the 1.0% band → **EGP 90,000**.
- **Outcome:** roughly a wash: model carefully. If margins are thinner (say profit EGP 350,000), the **general system becomes cheaper** because 1% of EGP 9m exceeds the income tax on a small profit. Documentation (e-invoices for the EGP 8.4m of costs) is critical to make the general system viable.
- Turnover: **EGP 240,000** (first year), high margin, almost no costs.
- Below the **EGP 250,000** VAT registration threshold: not yet required to register for VAT (verify), but e-invoicing/registration obligations should be checked.
- **Planning:** monitor cumulative turnover monthly; register for VAT and e-invoicing **before** crossing EGP 250,000 to avoid the late-registration penalties. If growth is expected, evaluate the simplified election early: but weigh the 5-year lock-in.
- Has an open ETA dispute for periods before 2020 and unfiled amended returns.
- **Planning:** check whether a Law 5/2025 settlement (or any successor facility) is **still open**; if a settlement is already in train, paying the principal promptly can forfeit delay fines and additional tax (verify the deadline has not lapsed). Going forward, evaluate simplified vs general for current years separately.
- **5-year lock-in (simplified regime)**: The Law 6/2025 election cannot be withdrawn for five years. A business expecting to scale past EGP 20m, change activity, or want profit-based treatment soon should think twice.
- **Exceeding the EGP 20m ceiling**: Going over by up to 20% keeps the 1.5% rate for one further year; exceeding the 20% buffer revokes all benefits the following year (verify). Plan growth around this.
- **e-invoice non-compliance disallows costs**: On the general system, missing/paper invoices = lost deductions and lost input VAT. This is the most common, avoidable over-payment of tax.
- **Misuse of the simplified regime = audit risk**: Splitting one business into multiple sham entities to stay under EGP 20m, or to access the low rate multiple times, is abuse and exposes the taxpayer to reassessment and penalties.
- **Suppressing turnover to dodge the VAT threshold**: Suppressing turnover to dodge the VAT threshold is evasion, not planning.
- **Late VAT/e-invoice registration penalty**: Late VAT/e-invoice registration after EGP 250,000 triggers fixed and daily penalties (verify).
- **Stale amnesty windows**: Law 5/2025 deadlines ran from Feb 2025 and are likely closed by May 2026: do not promise relief without confirming it is live.
- **Prohibited actions**: This skill performs **legal tax optimization only**. It must **never**: - Advise, design, or assist any form of **tax evasion** (التهرب الضريبي): under-reporting turnover or income, omitting sales, keeping two sets of books, or claiming costs that were not incurred. - Suggest **fake, inflated, or backdated invoices**, or any document not reflecting a real transaction. - Recommend **artificially fragmenting one business** into sham entities to stay under the EGP 20m simplified ceiling or the EGP 250,000 VAT threshold, or to multiply low-rate access. - Recommend **suppressing or splitting turnover** to avoid VAT registration. - Recommend **concealing assets, foreign income, or related-party transactions**, or misclassifying private spending as business cost. - Encourage **late or non-filing** to "wait for the next amnesty." - Present any planning as guaranteed, or substitute for a credentialed reviewer. If a user asks for any of the above, **refuse** and redirect to a legal, documented alternative (e.g. choosing the genuinely cheaper regime, improving e-invoice documentation, timely registration, or a legitimate settlement).

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

Not yet confirmed: the rule that only e-invoices prove costs and input VAT from 1 July 2023. VAT registration threshold changes, Resolution 281 of 2025 and its fine: left to `egypt-vat`. Whether Law 5 relief has a successor beyond Laws 151 and 152 of 2026.

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
