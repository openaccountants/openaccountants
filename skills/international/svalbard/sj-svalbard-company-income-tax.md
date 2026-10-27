---
name: sj-svalbard-company-income-tax
description: >
  Compute ordinary Svalbard company income tax for tax year 2026 for locally managed companies and nonresident businesses operating on Svalbard. Covers the office and management residence test, continuous business duration, local property, taxable profit reconciliation, deductions, depreciation, losses and mainland allocation. Calculates the sixteen-percent ordinary rate and the higher profit slice using qualifying payroll and physical capital. Includes return and payment dates, penalties, distribution and related-party cross-references, and two reproducible examples. Use for Svalbard corporation tax, company profit, nonresident business and split mainland projects. Svalbard only; Jan Mayen and specialist regimes are outside scope. This source-cited draft awaits licensed professional review.
version: 0.2
jurisdiction: SJ
tax_year: 2026
last_updated: 2026-10-24
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Svalbard: company income tax in 2026 v0.2

> **Source-cited draft.** Tax year 2026, checked 24 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. Independent AI review does not confer accountant review.

## Who this applies to

A company with an **office on Svalbard and management exercised there** is resident and starts with liability on all income. Business income earned outside Svalbard is excluded if shown taxable under other Norwegian taxation or in a foreign state. Income from real property/installations outside Svalbard is separately excluded. A registered address alone does not establish management ([Act §§2-3, 1-3](https://lovdata.no/dokument/NL/lov/1996-11-29-68)).

A nonresident company is liable on Svalbard business income if its activity lasts **at least 30 continuous days**, and on local property income under the separate property rule regardless of duration (§§2-4, 2-2(3)). Test the company's activity separately from employees' stays. The [business guidance](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/naring-pa-svalbard/) alternates between “over 30” and “30 or more”; exactly 30 satisfies the statute. This covers Svalbard under §1-1, not Jan Mayen. Sole proprietors use the individual guide.

## Rates, bands and thresholds

| Item | 2026 amount or rate | Official source |
|---|---:|---|
| Ordinary company profit | 16% | [2026 Svalbard decision §3(c)](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780) |
| Higher profit slice | 22% | [Decision §3(b)](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780) |
| Higher slice floor | NOK 15,000,000 | [Decision §3(b)](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780) |
| Substance threshold | 10 × qualifying payroll + 20% × qualifying physical-asset tax value | [Decision §3(b)](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780) |
| Capitalisation test | Cost at least NOK 30,000 and expected life at least 3 years | [Income Tax Act §14-40](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_14) |
| Ordinary machine/furniture balance depreciation | Up to 20% | [Income Tax Act §14-43(1)(d)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_14) |
| Svalbard commercial buildings; qualifying short-life buildings | Up to 4%; up to 10% where life no more than 20 years | [Svalbard regulation §4](https://lovdata.no/dokument/SF/forskrift/1997-12-15-1305) |

## The base

Use [Act §3-2](https://lovdata.no/dokument/NL/lov/1996-11-29-68) to import the Income Tax Act with the Svalbard exclusions. Build taxable profit from revenue and taxable gains, less costs incurred to acquire, maintain or secure taxable income ([Income Tax Act §§5-1, 5-30, 6-1](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_6)). Use accrual timing, not bank receipts alone (§14-2). Reconcile accounting depreciation to tax balances, separate improvements from deductible repairs, and remove exempt/outside-scope income and associated costs. Retain invoices, asset registers and project accounts. Svalbard does not import every mainland allowance: the §3-2 exclusions include employer-association/professional-organisation subscriptions under §6-19 and the shipping-company regime.

For capital assets use §§14-40 to 14-48. Common rates under §14-43 are office machines **30%**, goodwill **20%**, qualifying commercial vehicles **24%**, machinery/furniture **20%**, and fixed building technical installations **10%**. Classify the asset first. Svalbard regulation §4 overrides the ordinary commercial-building rate. Interest starts with §6-40; §6-41 limits deductible net interest to **25% of tax EBITDA**, subject to its thresholds and exceptions: group net-interest threshold **NOK 25 million** for the Norwegian group portion, and **NOK 5 million** outside a group. Outside a group the disallowance is limited to related-party net interest. The equity-ratio exception in §6-41(8) requires the statutory comparison and evidence, not an assertion of adequate equity. Carry disallowed net interest forward for up to **ten subsequent years** under §6-41(10), subject to the statutory capacity and ordering rules; keep it separate from an ordinary trading loss.

Deduct ordinary assessed loss carryforwards under [§14-6](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_14), oldest first, subject to debt forgiveness, insolvency and anti-avoidance restrictions. At cessation, §14-7 provides carryback into the preceding **two years** for qualifying final losses. Keep Svalbard and mainland loss ledgers separate; do not use a Svalbard loss against mainland income by default (Income Tax Act §2-35(2)(c)).

**Disposals and ordinary liquidation:** under [Income Tax Act §§14-44–14-48](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_14), reconcile sale proceeds to the relevant tax balance before computing company profit. For pooled groups a/c/d/j, proceeds reduce the balance unless taken directly to income; a negative balance is brought into income at least at that group’s maximum depreciation rate (§14-46). Group e–i disposal gains/losses go through the gain/loss account unless the statute provides direct recognition; a positive account is recognised at **at least 20% a year**, a negative account at **up to 20%** (§14-45). Under §14-47, a remaining deductible balance below **NOK 30,000** can be expensed, while a negative pool/gain-account balance below **NOK 30,000** must be recognised in full, measured before that year’s recognition.

On **complete liquidation**, §14-48(1)–(2) requires settlement of negative a/c/d/j balances and positive gain/loss-account balances into income; negative gain/loss accounts and qualifying positive a/c/d/j balances whose assets have been realised are deducted. Apply the statutory continuity/prior-emigration exceptions. Section 14-48(3)–(4) separately addresses cessation of tax liability and conditional EEA continuation/security; do not turn an ordinary liquidation rule into an unsupported blanket cross-border exemption. The XB gap concerns the territorial adaptation of unrealised-asset/company emigration rules, not these confirmed ordinary disposal/liquidation mechanics.

For positive taxable profit P, qualifying withholding-taxed payroll W and year-end tax value A of physical assets **located on Svalbard**:

`threshold = max(15000000, 10*W + 0.20*A)`

`high_slice = max(0, P-threshold)`

`tax = (P-high_slice)*0.16 + high_slice*0.22`

Both higher-rate conditions must be exceeded. Payroll is qualifying cost, assets use **tax value**, and financial assets do not supply physical substance. Round income/wealth down to whole kroner under decision §4 before tax. The personal NOK 20,000 allowance does not belong to companies.

Qualifying corporate share income is screened under [Income Tax Act §2-38](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_2), including foreign low-tax/ownership exclusions, corresponding nondeductible share losses and the **3%** inclusion for qualifying dividends under §2-38(6), unless its exception applies. This is a separate test from the ordinary trading-profit computation. Ordinary AS/ASA are wealth-tax exempt under §2-36(1); do not apply individual wealth tax to them. Other taxable institutions need the annual decision §2(b) classification.

## Deadlines and filing

Identify the company with Skatteetaten, establish the organisation number/reporting access, and file an electronic return with business specification and reconciliation. For mainland/Svalbard activity, use “Fordelt beregnet næringsinntekt” and attach an explanation of taxable income and deductible costs. Project accounts and activity dates support the allocation ([business guidance](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/naring-pa-svalbard/); [Administration Act §§8-1, 8-2](https://lovdata.no/dokument/NL/lov/2016-05-27-14)).

The ordinary deadline is **31 May following the income year**, so the 2026 return is due in 2027, subject to the statutory non-working-day rule and an approved extension ([regulation §§8-2-3, 8-2-5](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/KAPITTEL_7)). Company advance-tax instalments are **15 February and 15 April following the income year**, in equal amounts, and no earlier than **three weeks** after the notice is sent. Residual company tax is due **three weeks after assessment is sent** ([Payment Act §§10-20(3), 10-21(3), 10-2](https://lovdata.no/dokument/NL/lov/2005-06-17-67); Act §5-1). Cessation does not remove the final return or payment obligation.

## Penalties and interest

Under [Svalbard Act §4-1](https://lovdata.no/dokument/NL/lov/1996-11-29-68), the Tax Administration Act applies. Missing mandatory information can trigger a daily coercive fine, ordinarily **0.5 court-fee units per day**, capped at **50 units** for the ordinary information failure ([Administration Act §14-1](https://lovdata.no/dokument/NL/lov/2016-05-27-14); [regulation §14-1-1](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/KAPITTEL_13)). The authority's notice sets the start date; this is not an automatic charge on every late return.

Incorrect or incomplete information producing a tax advantage attracts **20%** additional tax, reduced to **10%** for the specified third-party-reported information. Intentional or grossly negligent failures can attract a further **20% or 40%**. Excusable circumstances, qualifying voluntary correction and other statutory exceptions must be tested ([Administration Act §§14-3 to 14-6](https://lovdata.no/dokument/NL/lov/2016-05-27-14)). These percentages apply to the tax advantage, not turnover.

Unpaid tax bears interest from the due date under [Payment Act §§11-1 and 11-6](https://lovdata.no/dokument/NL/lov/2005-06-17-67). The [authority's 2026 interest table](https://www.skatteetaten.no/satser/forsinkelsesrenter/) gives **12% a year for 1 January–30 June 2026** and **12.25% for 1 July–31 December 2026**. Split arrears at the change date. A payment falling due in 2027 needs the rate then in force; do not extrapolate 2026 rates.

## Cross-border points

Do not allocate income merely by the customer's address: establish work, management and property locations, taxable source and the evidence for statutory exclusions. Use the residence/cross-border guide for mainland relief, foreign tax, departure and the **20%** dividend withholding rule in decision §6. Related-party prices remain subject to [Income Tax Act §13-1](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_13); the transfer-pricing guide supplies disclosure/documentation tests. Norway's income-tax treaties do not cover Svalbard ([current Skatte-ABC S-23-1.5](https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-S-23)); do not import a treaty permanent-establishment threshold or rate.

## Two worked examples that recompute

**Ordinary profit after depreciation and a carried loss.** NOK 12 million revenue less NOK 3 million current deductible expenses, NOK 400,000 tax depreciation and NOK 600,000 valid carried loss leaves NOK 8 million. This is below the higher-rate floor; tax is NOK 1,280,000. Inputs assume correct allocation and no interest limitation or exempt income.

```oa-check
name: Svalbard company ordinary profit after loss 2026
inputs:
  revenue: 12000000
  expenses: 3000000
  tax_depreciation: 400000
  carried_loss: 600000
steps:
  profit: max(0, revenue-expenses-tax_depreciation-carried_loss)
  tax: profit*0.16
expected:
  profit: 8000000
  tax: 1280000
```

**Substance threshold exceeds the floor.** Taxable profit NOK 30 million, qualifying payroll NOK 2 million and qualifying asset tax value NOK 10 million yield threshold NOK 22 million. The high slice is NOK 8 million; tax is NOK 5,280,000.

```oa-check
name: Svalbard company higher profit slice 2026
inputs:
  profit: 30000000
  payroll: 2000000
  assets: 10000000
steps:
  substance: 10*payroll+0.20*assets
  threshold: max(15000000, substance)
  high_slice: max(0, profit-threshold)
  tax: (profit-high_slice)*0.16+high_slice*0.22
expected:
  threshold: 22000000
  high_slice: 8000000
  tax: 5280000
```

## Ask the client first

- Where are the office, actual management, work and property, and how long has local business continued?
- Which revenue/costs belong to Svalbard, mainland Norway or another state, and what proves taxability elsewhere?
- What are the tax asset balances, qualifying payroll, debt, group relationship and loss histories?
- Are there dividends, share disposals, associated-party transactions or planned cessation/asset transfers?
- Which returns, advance-tax notices and payments have already been made?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Svalbard Act §§1-1 to 5-2 | https://lovdata.no/dokument/NL/lov/1996-11-29-68 | 2026-10-24 |
| Enacted 2026 decision §§2–6 | https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780 | 2026-10-24 |
| Income Tax Act §§2-35, 2-36, 2-38 | https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_2 | 2026-10-24 |
| Income Tax Act chs.5–6 | https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_6 | 2026-10-24 |
| Income Tax Act §§14-2, 14-6, 14-7, 14-40–48 | https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_14 | 2026-10-24 |
| Income Tax Act §13-1 | https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_13 | 2026-10-24 |
| Svalbard regulation §4 | https://lovdata.no/dokument/SF/forskrift/1997-12-15-1305 | 2026-10-24 |
| Business allocation and filing | https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/naring-pa-svalbard/ | 2026-10-24 |
| Administration Act chs.8,14 | https://lovdata.no/dokument/NL/lov/2016-05-27-14 | 2026-10-24 |
| Administration regulation chs.8,14 | https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/KAPITTEL_7 | 2026-10-24 |
| Coercive-fine regulation §14-1-1 | https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/KAPITTEL_13 | 2026-10-24 |
| Payment Act chs.10–11 | https://lovdata.no/dokument/NL/lov/2005-06-17-67 | 2026-10-24 |
| 2026 interest | https://www.skatteetaten.no/satser/forsinkelsesrenter/ | 2026-10-24 |
| Current authority S-23, 2026 publication dates | https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-S-23 | 2026-10-24 |

The current Skatte-ABC contains stale year labels in some rate paragraphs and numbering inconsistencies. The enacted 2026 decision and consolidated statute control all figures here.

Not yet confirmed: Specialist shipping, extractive, financial and large multinational minimum-tax regimes are excluded. Exact exit/foreign-relief administration is identified in the cross-border guide.

> Contributed by Ryan Duguid.

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
