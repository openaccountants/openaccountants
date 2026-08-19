---
name: ua-tax-optimization
description: Use this skill whenever asked about legal tax optimization or tax planning for self-employed people in Ukraine. Trigger on phrases like "reduce tax Ukraine", "Diia City", "single tax vs general system", "tax planning Ukraine freelancer", "optimise FOP taxes", "should I be on єдиний податок or загальна система", "lower my tax as an IT freelancer in Ukraine", "Group 3 5% vs general system", "Diia City gig contract", "do I need to register for VAT", or any question about legitimately structuring a Ukrainian self-employed person's affairs to pay less tax. Covers choosing the right regime, the ₴1,000,000 VAT threshold lever, the Diia City IT regime, ЄСВ minimisation, expense documentation on the general system, foreign-client / FX considerations, and the red flags of fictitious-FOP misclassification. This skill is about LEGAL planning only — it never advises evasion. ALWAYS read this skill before any Ukrainian self-employed tax-planning work, and cross-read ua-single-tax, ua-income-tax, ua-payroll and ua-formation.
version: 1.0
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Tax Optimization

## Ukraine Tax Optimization & Planning (Self-Employed) — Skill v1.0

> **Scope:** Legal tax planning only. This skill helps a self-employed person in Ukraine choose and operate the most efficient *lawful* structure. It does **not** help anyone evade tax, disguise employment, or build fictitious arrangements (see PROHIBITIONS). Every output here is a starting point for a conversation with a qualified Ukrainian accountant or tax lawyer.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Ukraine (UA) |
| Scope | Legal tax planning / optimization for self-employed individuals |
| Currency | UAH (₴) |
| Taxpayer types | ФОП (фізична особа-підприємець / sole proprietor); Diia City gig-specialist; general-system entrepreneur |
| Key levers | (1) Regime choice — single tax (єдиний податок) Group 3 vs general system (загальна система); (2) ₴1,000,000 VAT threshold; (3) Diia City for IT; (4) ЄСВ at the minimum base; (5) documented expenses on the general system |
| Tax authority | Державна податкова служба (ДПС / State Tax Service) — tax.gov.ua |
| Filing portal | Електронний кабінет платника (cabinet.tax.gov.ua); Diia City portal (city.diia.gov.ua) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Ukrainian accountant |
| Skill version | 1.0 |

### Verified 2026 base figures (pin date: 1 January 2026)

**Verified 2026 base figures**

| Figure | 2026 value | Notes |
| --- | --- | --- |
| Minimum wage (мінімальна зарплата) | ₴8,647/month | Drives ЄСВ and Diia City thresholds — **verify final 2026 minimum wage** in the State Budget law |
| ЄСВ minimum (єдиний соціальний внесок) | ₴1,902.34/month (22% × ₴8,647) | Per FOP and per Diia City specialist |
| Group 3 single tax (non-VAT) | 5% of turnover |  |
| Group 3 single tax (VAT-registered) | 3% of turnover + VAT (ПДВ) |  |
| Group 3 military levy (військовий збір) | 1% of turnover | In force under martial law; **verify still 1% for Group 3** |
| Group 3 annual income cap | ₴10,091,049 (1,167 × minimum wage) | Recalculated annually |
| General system | 18% PIT + 5% military levy + 22% ЄСВ — all on **net profit** |  |
| VAT (ПДВ) registration threshold | ₴1,000,000 taxable supplies over rolling 12 months | See VAT-threshold change note below |
| Diia City gig-specialist | 5% PIT + 5% military levy + ЄСВ 22% of minimum wage | Gig income above €240,000/yr taxed at 18% |

> **Wartime note.** The military levy (військовий збір) rose to 5% for general individuals from Dec 2024 and remains in force throughout 2026 under martial law; Group 3 FOPs pay a separate fixed 1% military levy on turnover. Fixed amounts (ЄСВ, single tax) are pinned at their 1 January value for the whole year. **Verify all rates against tax.gov.ua before relying on them.**

### Conservative defaults

- **Conservative defaults** — When a planning input is missing or ambiguous, assume the higher-tax / lower-risk outcome and flag it for the reviewer. Specifically: Default to the regime the client is already on until a break-even analysis clearly favours switching. Assume an expense is non-deductible on the general system unless it is documented and business-related. Assume the client must register for VAT once the rolling 12-month figure approaches ₴1,000,000. Never assume a relationship qualifies as genuine self-employment if it looks like disguised employment — flag it (Section 7). Treat every Diia City figure and the VAT-threshold reform as "verify current value" — both are live policy areas in 2026.

## Section 2 — Choosing the regime (single tax vs general system)

The first and biggest lever for a Ukrainian freelancer is **regime choice**. Most freelancers and IT contractors serving companies and foreign clients sit on **Group 3 of the single tax** because the arithmetic is simple and the rate is low. But the general system can win when **documented expenses are high relative to revenue**.

### The core comparison

**The core comparison**

| Lever | Group 3 single tax (non-VAT) | General system (загальна система) |
| --- | --- | --- |
| Tax base | Gross **turnover** (revenue received) | **Net profit** (revenue − documented expenses) |
| Headline tax | 5% single tax + 1% military levy = **6% of turnover** | 18% PIT + 5% military levy = **23% of net profit** |
| ЄСВ | ₴1,902.34/month minimum (fixed) | 22% of net profit, but **not less than** ₴1,902.34/month |
| Bookkeeping | Light — income ledger only | Full — income **and** expense documentation |
| Income cap | ₴10,091,049/year | None |
| Activity restrictions | Several activities barred (see ua-single-tax) | None |
| Loss / no-income month | Still owe ЄСВ; single tax/levy track turnover | If no profit, **no PIT/levy** that period (ЄСВ minimum may still apply) |

### Break-even logic

- **Break-even logic** — Compare 6% of turnover (Group 3) against 23% of net profit + ЄСВ delta (general system). Group 3's 6% effectively equals 23% of profit when profit ≈ 26% of turnover (since 0.06 ÷ 0.23 ≈ 0.26), ignoring the ЄСВ difference. Profit margin above ~26% of turnover → Group 3 (6% of turnover) is cheaper. This describes almost all software developers and freelancers selling labour with few costs — they should stay on Group 3. Profit margin below ~26% of turnover → the general system may win, because you are only taxed on the thin slice of profit, not the whole turnover. This describes resellers, agencies with large pass-through costs, or businesses with heavy documented purchases. Add the ЄСВ effect. On the general system ЄСВ is 22% of net profit (floored at the minimum), so high-profit businesses on the general system also carry a larger ЄСВ bill — this pushes the break-even slightly in Group 3's favour for high earners.

> **Rule of thumb for IT freelancers serving foreign/domestic companies:** Group 3 at 6% is almost always the optimum unless turnover is about to breach ₴10,091,049 or VAT/Diia City considerations change the picture. Run the actual numbers (Section 6) — never decide on the rule of thumb alone.

Cross-reference **ua-single-tax** for the full Group 1/2/3 rules and activity bars, and **ua-income-tax** for general-system PIT mechanics and the deductible-expense list.

## Section 3 — The ₴1,000,000 VAT (ПДВ) threshold lever

- **VAT registration threshold** — VAT registration in Ukraine becomes mandatory once taxable supplies exceed ₴1,000,000 over any rolling 12 calendar months.
- **Key points on VAT threshold** — Group 3 has two sub-rates: 5% without VAT, or 3% with VAT registration. The 3% looks cheaper but only makes sense if you can reclaim meaningful input VAT (ПДВ кредит) or your clients require VAT invoices. A pure-labour freelancer with no input VAT usually keeps the 5% non-VAT status and stays below ₴1,000,000. Foreign-client services may be outside Ukrainian VAT. Many B2B services exported to non-residents are treated as supplied outside Ukraine (place-of-supply rules) and so do not count toward the threshold and are not subject to Ukrainian VAT. Verify the place-of-supply treatment per service type — getting this wrong is a common error. See ukraine-vat. Monitor the rolling figure, not the calendar-year figure. Registration is triggered by any 12-month window.  _(see ukraine-vat)_

> **VAT-threshold reform — VERIFY.** Draft legislation in late 2025 proposed making VAT registration mandatory for single-tax payers (Groups 1–3) whose taxable operations exceed ₴1,000,000, with effect from **1 January 2027** (application by 10 January 2027 for those over the threshold in 2026). As of the latest research this was **not yet enacted** and the ₴1,000,000 general threshold remained in force for 2026, with a carve-out for single-tax payers. **This is a live policy area — verify the current enacted rule on tax.gov.ua before advising anyone, because it materially affects whether a Group 3 freelancer must register.**

**Legitimate planning, not avoidance:** managing the threshold means timing genuine business and choosing the right sub-rate — *not* splitting one real business across multiple FOPs to stay under the limit. Artificial fragmentation is a red flag (Section 7).

## Section 4 — Diia City for IT (eligibility, taxation, trade-offs)

**Diia City** (Дія.Сіті) is a special legal/tax regime for the IT sector. It is not a structure an individual joins directly — it is a **regime that a resident company joins**, after which the company can engage specialists as **gig-contract** specialists (ґіг-контракт) or employees with preferential taxation. It is relevant to a self-employed developer mainly as an **alternative to the FOP model** when working with (or founding) a Ukrainian IT company.

### Taxation of a Diia City gig-specialist (2026)

**Taxation of a Diia City gig-specialist (2026)**

| Component | Rate / base |
| --- | --- |
| Personal income tax (PIT) | **5%** on gig remuneration (vs 18% standard) |
| Military levy (військовий збір) | 5% — applies from the month after the company gains resident status; **verify current rate** |
| ЄСВ | 22% of the **minimum wage** (≈ ₴1,902.34/month), paid by the resident company |
| Gig income cap | Up to **€240,000/year** at the 5% rate; any excess taxed at **18%** (FX rate fixed at 1 January) |

### Resident-company side (the entity, not the individual)

- **Resident company tax choices** — A Diia City resident company chooses between: Corporate income tax (18%) on net profit, or Exit-capital tax (податок на виведений капітал) at 9% — paid only when profit is distributed (e.g. dividends); reinvested profit is effectively taxed at 0%. This makes Diia City attractive for founders who reinvest, and for teams who value the 5% PIT and the legally-defined gig contract over the FOP model.

### Eligibility (resident company must satisfy all)

- **Eligibility criteria** — 1. ≥ 90% of income from qualified IT activities. 2. ≥ 9 specialists on average (employees and/or gig-specialists). 3. Average monthly remuneration ≥ €1,200 equivalent per specialist. (There are also additional formal requirements and a clean-history test — confirm on city.diia.gov.ua.)

### Trade-offs vs the FOP / Group 3 model

**Trade-offs vs the FOP / Group 3 model**

|  | Group 3 FOP | Diia City gig-specialist |
| --- | --- | --- |
| Effective tax on labour income | ~6% of turnover (+ fixed ЄСВ) | 5% PIT + 5% levy + ЄSV — usually **higher** than 6% all-in for the individual |
| Who you are | Independent entrepreneur | Engaged by a resident company under a gig contract |
| Income cap | ₴10,091,049 | €240,000 gig (excess at 18%) |
| Setup | Register a FOP | Requires a qualifying resident company |
| Disguised-employment risk | Present if working like an employee for one client | **Lower** — the gig contract is a recognised legal form designed for this |
| Best for | Solo freelancers, multiple clients, low costs | IT teams/companies; founders reinvesting profit; reducing misclassification risk on a single-client relationship |

> **Planning insight.** For a *solo* freelancer with several clients, Group 3 at ~6% is usually cheaper than Diia City for the individual. Diia City wins when (a) you are building or joining a team/company, (b) you want to convert a single-client FOP relationship into a legally clean form to kill misclassification risk, or (c) you reinvest profit and want the 9% exit-capital regime at the company level. Compare the **total** burden, not just the headline PIT rate. Cross-read **ua-payroll** for the gig/employment payroll mechanics and **ua-formation** for setting up the resident company.

### ЄСВ (єдиний соціальний внесок) at the minimum base

- **ЄСВ minimum-base rules** — A Group 3 FOP pays ЄСВ at the minimum — 22% of the minimum wage, ≈ ₴1,902.34/month in 2026 — regardless of how much they earn. This is already the optimum: there is no legitimate way to pay less while remaining covered, and voluntarily paying more only raises future pension entitlement. Do not over-pay ЄСВ unless the client specifically wants higher social/pension cover. Certain exemptions exist (e.g. some pensioners, persons with disabilities, FOPs who are also employed and have ЄСВ paid by an employer at/above the minimum). Verify eligibility — see ua-social-contributions. On the general system, ЄСВ is 22% of net profit but floored at the minimum and capped at the maximum base — another reason high-profit businesses often prefer Group 3's fixed ЄСВ.  _(see ua-social-contributions)_

### Legitimate expense documentation (general system)

- **Deductible expense requirements** — Expenses only reduce tax on the general system (Group 3 is taxed on turnover, so expenses are irrelevant there). To be deductible, an expense must be: 1. Business-related (directly connected to the activity that earns the income). 2. Documented — primary documents (первинні документи): invoices, acts of acceptance (акти виконаних робіт), payment confirmations, contracts. 3. Recorded in the FOP's income-and-expense ledger. Common legitimate deductions: goods/materials for resale, subcontractor and service costs, rent of business premises, depreciation of business fixed assets, bank fees, software/licences used for the business. Personal expenses are never deductible. Keep all primary documents — the burden of proof is on the taxpayer at audit. See ua-income-tax for the deductible-expense catalogue.  _(see ua-income-tax)_

## Section 6 — Worked examples

> Illustrative only, using verified 2026 figures. Round numbers; ignore minor timing. Always reproduce with the client's real data and have a Ukrainian accountant confirm.

### Example A — Solo IT freelancer, foreign clients, low costs (Group 3 wins clearly)

Annual revenue: ₴3,000,000. Documented business expenses: ₴150,000 (≈5% of revenue). Group 3 (non-VAT): 6% × ₴3,000,000 = ₴180,000 + ЄСВ ₴22,828 = ≈ ₴202,828/year. General system: profit = ₴2,850,000; 23% × ₴2,850,000 = ₴655,500 + ЄСВ 22% × ₴2,850,000 (above min) = ₴627,000 → ≈ ₴1,282,500/year. Conclusion: Group 3 saves ~₴1.08m. Profit margin ~95% → far above the ~26% break-even. Stay on Group 3.

### Example B — Reseller / agency, heavy documented costs (general system can win)

Annual revenue: ₴2,000,000. Documented business expenses: ₴1,700,000 (85% of revenue). Profit margin 15%. Group 3 (non-VAT): 6% × ₴2,000,000 = ₴120,000 + ЄСВ ₴22,828 = ≈ ₴142,828/year. General system: profit = ₴300,000; 23% × ₴300,000 = ₴69,000 + ЄСВ 22% × ₴300,000 = ₴66,000 → ≈ ₴135,000/year. Conclusion: roughly break-even (margin 15% < ~26%); the general system edges ahead and gives no income cap. Decide on the trustworthiness of the expense documentation and audit risk.

### Example C — Approaching the Group 3 income cap

Run-rate revenue: ₴11,000,000/year — above the ₴10,091,049 Group 3 cap. Issue: exceeding the cap triggers a penalty rate and forced transition off Group 3 (see ua-single-tax). Legitimate options: (a) move to the general system (no cap); (b) defer/decline genuine work to stay under the cap if commercially sensible; (c) consider a Diia City company structure if this is an IT team. Not legitimate: splitting one real business across several FOPs to multiply the cap (Section 7).

### Example D — IT founder choosing Diia City vs Group 3

Developer earning ~₴3,000,000/year and building a small team. As a solo Group 3 FOP: ~6% (≈ ₴202,828 incl. ЄСВ) — cheapest for the individual. As a Diia City gig-specialist: 5% PIT + 5% military levy on remuneration + ЄСВ — all-in usually higher than 6% for the individual, but the company benefits from the 9% exit-capital regime on reinvested profit and the relationship is legally clean (no misclassification risk). Conclusion: choose Diia City for the company/team and risk reasons, not to cut the individual's headline rate.

## Section 7 — Risks & red flags (anti-avoidance)

The following are risks to flag, not techniques to recommend. If a client's situation matches any of these, surface it plainly and recommend professional advice — do not design around it. Fictitious / disguised-employment FOP (RISK). The single most scrutinised arrangement: a company pays a worker as a Group 3 FOP to avoid 18% PIT + 5% levy + ~22% ЄСВ payroll cost, while the worker in substance functions as an employee (fixed hours, single client, employer's premises/equipment, subordination, paid leave). Ukrainian authorities can reclassify this, with back taxes, ЄСВ arrears, fines and penalties for both sides. Flag, never advise. The legitimate alternatives are genuine multi-client freelancing, employment, or a Diia City gig contract (which exists precisely to give a clean legal form for this kind of engagement). Artificial business splitting (RISK). Dividing one real business across multiple FOPs or family members to stay under the Group 3 income cap or the ₴1,000,000 VAT threshold. Treated as abusive. Sham expenses (RISK). Deducting personal or fabricated costs on the general system. The taxpayer bears the burden of proof; undocumented or non-business expenses are disallowed at audit. Mischaracterising VATable supplies (RISK). Wrongly treating Ukrainian-source supplies as out-of-scope to dodge the ₴1,000,000 threshold. Verify place-of-supply per service (ukraine-vat). Ignoring the FX/currency rules (RISK). Foreign-currency proceeds must be received and converted per National Bank of Ukraine (НБУ) currency-control rules; single-tax income is generally recognised on the date funds hit the account at the NBU rate. Late or off-channel receipt of foreign earnings creates currency-control and tax-timing problems. Verify current НБУ rules. Missing the Diia City eligibility tests (RISK). Falling below the 90%-qualified-income, 9-specialist, or €1,200-average thresholds can cost the resident status and the preferential rates.

### FX / foreign-client considerations (legitimate)

- **FX considerations** — Foreign-client revenue is fine on Group 3 — it counts toward the ₴10,091,049 annual cap at the NBU rate on the date received. Many exported B2B services fall outside Ukrainian VAT (place of supply), so they may not push you toward the ₴1,000,000 VAT threshold — verify per service type. Use proper FOP currency accounts and observe NBU currency-control and mandatory-sale rules where they apply. Document every inbound payment.

## Section 8 — Reference

Tax Code of Ukraine (Податковий кодекс) — single tax (Chapter 1, Section XIV), PIT (Section IV), military levy, VAT (Section V). State Tax Service of Ukraine (ДПС) — tax.gov.ua; taxpayer cabinet cabinet.tax.gov.ua. Diia City — city.diia.gov.ua; the Diia City law and the Tax Code provisions on residents and gig contracts. National Bank of Ukraine (НБУ) — currency-control rules for foreign-currency receipts. Big-4 / professional guidance — PwC Worldwide Tax Summaries (Ukraine), EY, BDO and similar for Diia City and general-system mechanics. Companion skills — ua-single-tax, ua-income-tax, ua-payroll, ua-formation, ua-social-contributions, ukraine-vat.

> **Verify-before-advising checklist:** (1) 2026 minimum wage and the resulting ЄСВ figure; (2) whether the ₴1,000,000 VAT-threshold reform for single-tax payers has been enacted; (3) current military-levy rates for Group 3 and for Diia City specialists; (4) the Group 3 annual income cap; (5) Diia City eligibility thresholds and the €240,000 gig cap. All flagged "verify" above.

## PROHIBITIONS

- **Prohibitions list** — This skill must never: 1. Advise, design, or facilitate tax evasion of any kind, or any arrangement that conceals income, falsifies documents, or misrepresents facts to the ДПС. 2. Recommend or help structure a fictitious / disguised-employment FOP relationship, or any sham contractor arrangement intended to dodge payroll taxes. Such situations are flagged as RISK only. 3. Recommend artificial business splitting across multiple FOPs or persons to defeat the income cap or the VAT threshold. 4. Suggest deducting personal or fabricated expenses, or backdating/fabricating primary documents. 5. Advise mischaracterising VATable supplies, mishandling foreign-currency receipts outside NBU rules, or any breach of currency control. 6. Present any figure as final without the "verify against tax.gov.ua / city.diia.gov.ua" caveat where this skill has flagged it. 7. Substitute for a qualified Ukrainian accountant or tax lawyer. Every plan requires professional sign-off before action.

## Disclaimer

This skill is research-verified content produced by the Open Accountants Community for tax year 2026 and is pending sign-off by a qualified Ukrainian accountant/auditor. It addresses legal tax planning only. Rates, thresholds, and especially the VAT-threshold reform and Diia City rules are live policy areas — always verify the current position against the State Tax Service (tax.gov.ua) and the Diia City portal (city.diia.gov.ua) before relying on any figure. Tax optimisation in Ukraine requires the judgement of a qualified Ukrainian accountant or tax lawyer who can review the client's specific facts. Nothing here is legal or tax advice. Learn more at openaccountants.com.

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
