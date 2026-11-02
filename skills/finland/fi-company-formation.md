---
name: fi-company-formation
description: >
  Prepare an ordinary Finnish private limited company formation in 2026 using
  the current PRH online routes. Distinguish guided setup from drafted-document
  filing, authority fees from share capital, and registration from tax obligations.
  Screen board composition and EEA residence, preserve the incorporation deadline,
  and prepare the ordinary audit-size and annual filing checks. Use for Oy formation,
  Finnish Trade Register registration, setup fees, directors, deputy directors,
  financial statement filing or audit thresholds. Includes statutory and authority
  sources, read dates and worked controls. Other entities, exemptions, specialist
  sectors and named Finnish accountant review remain open.
version: 0.2
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland company formation and entity screening v0.2

## Who this applies to

Use this source-cited draft to prepare an ordinary private limited company (Oy). The company becomes a separate legal person on registration. A public limited company (Oyj) has a EUR 80,000 minimum share-capital rule. A private Oy has no minimum share capital; PRH records zero share capital as EUR 0. Private-trader, partnership and cooperative routes need their own registration/liability analysis before comparing tax outcomes. A sole trader (toiminimi) has no separate legal personality and the owner is personally liable without limit; a general partnership (Ay) and a limited partnership (Ky) are governed by the Partnerships Act 389/1988, where general partners are personally liable. [Companies Act, chapter 1 sections 2–3][companies-law]; [PRH startup instructions][startup]; [Partnerships Act 389/1988][partnerships-law]

Connect entity choice to the [individual](fi-income-tax.md), [corporate](fi-corporate-income-tax.md), [YEL](fi-yel-social.md) and [payroll](fi-employer-payroll.md) skills. A registration route does not decide the tax residence, worker status or optimal entity for particular facts.

## Current PRH setup routes and fees

| Route | Authority handling fee | Eligibility/source |
|---|---:|---|
| Guided setup package | EUR 300 | No share subscription price, zero share capital, adult shareholders, Finnish identity codes for the specified people, standard articles sufficient. [PRH startup instructions][startup] |
| Start-up notification with drafted documents | EUR 400 | Use where share capital, entity shareholders, missing Finnish identity codes, tailored articles or public-company status require it. [PRH startup instructions][startup] |

PRH's 2026 instructions require online filing, in Finnish or Swedish, and permit an Oy with no share capital. Recheck route eligibility and the live authority fee before payment. Share capital is company funding, not another PRH fee. [PRH startup instructions][startup]

## Board and residence screen

The ordinary statutory board has one to five members unless the articles provide otherwise. Fewer than three members requires at least one deputy; multiple members require a chair. [Companies Act, chapter 6 section 8][companies-law]

PRH checks EEA residence separately for ordinary and deputy members: an EEA-resident ordinary director does not settle the deputy group's permit requirement. The managing director and their deputy have their own residence/permit test. Citizenship does not determine residence. Obtain the applicable permit before treating the structure as compliant. [PRH foreign-person permits][permits]; [Companies Act, chapter 6 sections 10 and 19][companies-law]

## Incorporation documents and deadline

File within **three months after the memorandum is signed** or incorporation lapses. Shares submitted for registration must be fully paid; non-cash subscription requires the statutory supporting auditor statement. Preserve the memorandum, articles, payments/declarations, officer details and registration result. [Companies Act, chapter 2 section 8][companies-law]

Use the current PRH route and monitor the submitted notification in Virre. Its registration extract establishes the recorded result; a draft saved in a service is not a completed registration. No fixed processing duration is supplied here. [PRH filing instructions][filing]

## Audit-size test: both periods must qualify

Under Auditing Act chapter 2 section 2, the ordinary size-based omission rule requires **at most one** of these conditions to be met in **each** of the concluded and immediately preceding financial periods:

| Condition | Exceedance threshold |
|---|---:|
| Balance-sheet total | Over EUR 100,000 |
| Net sales or corresponding revenue | Over EUR 200,000 |
| Average employee count | Over 3 |

Equality does not exceed a threshold. Startup entities without both periods have a separate statutory rule. Articles can require an audit, and the specified securities-holding/significant-influence case always requires an auditor. Check group and other-law requirements separately. [Auditing Act, chapter 2 section 2][audit-law]

## Annual filing and consequences

An Oy keeps double-entry books and prepares annual financial statements under the Accounting Act. [Accounting Act 1336/1997, chapter 1 sections 1–2 and chapter 3][accounting-law] Hold the ordinary general meeting within six months of period end; it adopts the accounts and decides on the use of profit. Company-law registration of the financial statements/annual report is due within two months after adoption. [Companies Act, chapter 5 section 3 and chapter 8 section 10][companies-law]

PRH's general outer timetable is eight months after period end; filing within that period is free. Earlier adoption still starts the statutory two-month clock. Tax-return timing is separate: the corporate income tax return is due four months after the end of the calendar month in which the period ends (see the [corporate skill](fi-corporate-income-tax.md)); do not wait for the meeting/PRH filing. VAT and payroll reports run on their own periods ([VAT](finland-vat-return.md), [payroll](fi-employer-payroll.md)). [PRH financial statements][statements]

PRH's 2026 notice describes a late-submission fee from EUR 150, rising to EUR 600 for more than four months' delay, with doubling for two or more consecutive periods. Actual period, delay and statutory notice/decision conditions must be checked; this draft does not compute every fee. Inactive companies still have a filing duty. [PRH 2026 late-filing notice][late]

## Cross-border and other boundaries

Foreign ownership, EEA officer residence, Finnish tax residence, immigration permission, bank onboarding and regulated-activity approval are distinct checks. The permit screen above does not resolve the others. Collect the activity, ownership and management facts and obtain the relevant authority decision before relying on a particular route. [PRH permit guidance][permits]

## Worked controls

### 1. Registration fee versus company funding

Assume an ordinary own-document Oy route with EUR 10,000 agreed cash share capital and the published EUR 400 authority fee. Cash funding is EUR 10,400, of which EUR 10,000 is company capital. This is not a tax deduction calculation or a quote for professional/bank services. The zero-capital guided route is not assumed to be available.

```oa-check
name: Finland assumed Oy capital and authority fee separation
inputs:
  agreed_cash_share_capital: 10000
  own_document_authority_fee: 400
steps:
  combined_cash_funding: agreed_cash_share_capital + own_document_authority_fee
  authority_fee_only: combined_cash_funding - agreed_cash_share_capital
expected:
  combined_cash_funding: 10400
  authority_fee_only: 400
```

### 2. Count each year's established audit triggers

Assume current balance EUR 110,000, sales EUR 190,000 and average employees 4: two exceedances. Previous figures EUR 90,000, EUR 150,000 and 2 give zero. The ordinary omission test requires no more than one in each period, so these facts do not satisfy it. The control recomputes the counts from already classified flags; it is not a complete legal decision engine.

```oa-check
name: Finland assumed separate period audit trigger counts
inputs:
  current_balance_trigger: 1
  current_sales_trigger: 0
  current_employee_trigger: 1
  previous_balance_trigger: 0
  previous_sales_trigger: 0
  previous_employee_trigger: 0
steps:
  current_trigger_count: current_balance_trigger + current_sales_trigger + current_employee_trigger
  previous_trigger_count: previous_balance_trigger + previous_sales_trigger + previous_employee_trigger
  highest_period_count: max(current_trigger_count, previous_trigger_count)
expected:
  current_trigger_count: 2
  previous_trigger_count: 0
  highest_period_count: 2
```

## Ask the client first

- Which entity, activities, ownership and tax-residence facts apply?
- Who will own shares and serve as ordinary/deputy directors or managing director, and where do they live?
- Are standard articles sufficient, and do the specified people have Finnish identity codes?
- What subscription price/capital, payment evidence and signing date apply?
- What do both financial periods, articles and group/holding-company facts show for audit?
- Which registrations, permits, meeting decisions and filing receipts already exist?

## Sources and review limits

Read 23 October 2026. PRH's startup page was directly opened. Permit, general filing, financial-statement and late-filing instructions were read as indexed official text. The listed company/auditing provisions were read directly from official Finlex HTML statutory content; retrieval hashes are in the country research record.

- [PRH startup routes][startup]; [foreign-person permits][permits]; [filing instructions][filing].
- [Companies Act 624/2006][companies-law], chapter 1 sections 2–3, chapter 2 sections 8–9, chapter 5 section 3, chapter 6 sections 8, 10 and 19, chapter 8 section 10.
- [Auditing Act 1141/2015][audit-law], chapter 2 section 2. The statutory positive omission test is used rather than ambiguous English summaries of the two-period condition.
- [PRH financial statements][statements]; [2026 late-filing notice][late].
- [Partnerships Act 389/1988][partnerships-law]; [Accounting Act 1336/1997][accounting-law], chapter 1 sections 1–2, chapter 3 (read 27 October 2026).

Not yet confirmed: complete company/accounting/Trade Register and fee-law chains; entity comparisons, share rights and non-cash subscriptions, all foreign-person exemptions, beneficial-owner specifics, group/sector audit and sustainability rules, actual late-fee cases and live filing. Named Finnish accountant review remains open; the independent source-review scope is recorded in the [country README](README.md#evidence-and-next-action). This secondary formation topic does not establish any core tax domain as complete.

[startup]: https://www.prh.fi/en/companiesandorganisations/yrityksen_perustaminen/osakeyhtio.html
[permits]: https://www.prh.fi/en/companiesandorganisations/ulkomaalaisluvat.html
[filing]: https://www.prh.fi/en/companiesandorganisations/muutokset_rekisteritietoihin/yleisohje.html
[companies-law]: https://www.finlex.fi/fi/lainsaadanto/2006/624
[audit-law]: https://www.finlex.fi/fi/lainsaadanto/2015/1141
[statements]: https://www.prh.fi/en/companiesandorganisations/financial_statements/limited_liability_companies_co-operatives_and_other_companies/digital.html
[late]: https://www.prh.fi/en/presentation_and_duties/uutislistaus/news/2026/financial-statements-submitted-late-27.5.2026.html
[partnerships-law]: https://www.finlex.fi/fi/lainsaadanto/1988/389
[accounting-law]: https://www.finlex.fi/fi/lainsaadanto/1997/1336

> Contributed by Michael Cutajar.

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
