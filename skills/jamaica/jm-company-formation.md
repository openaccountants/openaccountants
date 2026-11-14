---
name: jm-company-formation
description: >
  How to form a company or register a business name in Jamaica in 2026, at the
  Companies Office of Jamaica (COJ), and register it with Tax Administration
  Jamaica. Gives the COJ fees (J$27,500 incorporation package with the Business
  Registration Form, stamp duty and beneficial ownership form; J$2,500 sole
  trader or small partnership; expedition J$3,000 or J$6,000), the annual return
  on the anniversary of incorporation (J$5,000, late fees up to J$10,000), and the
  post-incorporation TRN, GCT, NIS, NHT and HEART registrations. Trigger on
  Jamaica company formation, incorporate in Jamaica, COJ, BRF, annual return
  Jamaica, business name Jamaica. Built from COJ and TAJ pages; not reviewed by an
  accountant.
version: 1.0
jurisdiction: JM
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
tier: 2
domain: formation
type: filing-howto
---

# Jamaica Company Formation and Entity Choice v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone setting up a business in Jamaica in 2026: a private company limited by shares (the usual vehicle), a public company, a company limited by guarantee (non-profit), a sole trader or partnership registered as a business name, or a branch of an overseas company. Registration is with the Companies Office of Jamaica (COJ), under the Companies Act and the Registration of Business Names Act. Tax registration is with Tax Administration Jamaica (TAJ). Amounts are J$.

Out of scope: regulated financial businesses (licensing by the Bank of Jamaica or Financial Services Commission), Special Economic Zone approvals, conversion to a public company with a prospectus (fees listed, process not covered).

## Rates, bands and thresholds

| Item | Fee | Conditions | Source |
|---|---|---|---|
| Incorporation package: Form 1A/1B Articles of Incorporation, BRF Business Registration Form, stamp duty, BOR-A/B (beneficial ownership) form | J$27,500 | One filing for a new company | COJ, fees: https://www.orcjamaica.com/Fees.aspx |
| Expedition of company registration, same day | J$6,000 | Optional | same |
| Expedition of company registration, next day | J$3,000 | Optional | same |
| Business name, sole trader (B.N 1 or BRF) | J$2,500 | Registration or renewal | same |
| Business name, partnership of 2 to 5 partners (B.N 2) | J$2,500 | Registration or renewal | same |
| Business name, partnership of 6 to 20 partners (B.N 2) | J$5,000 | Registration or renewal | same |
| Trade name of a corporation (B.N 3) | J$3,000 | Registration or renewal | same |
| Branch business, filed with B.N 1, 2 or 3 | J$1,000 | Each branch | same |
| Change of business name particulars (B.N 5) | J$2,500 | Notification | same |
| Closure of a business name (B.N 6) | J$600 | | same |
| Amend or adopt articles (resolution and amended articles) | J$8,000 | | same |
| Increase of share capital (notice, resolution) | J$12,000 | | same |
| Particulars of charge (Form 16A) | J$5,000 | Each charge document | same |
| Restoration to the register (Forms 28A and 28B) | J$15,000 | | same |
| Annual return, company limited by shares | J$5,000 | Forms 19A (or 19E status quo, where a 19A is on file) | COJ, filing annual returns: https://www.orcjamaica.com/FAQ/Filing%20Annual%20Returns.pdf |
| Annual return, company limited by guarantee without share capital | J$2,000 | Form 19B | same |
| Late annual return | Late fees up to a maximum of J$10,000 a return | Directors liable to proceedings; the company can be struck off | same |

## The base

### Entity choice

| Form | Liability | Tax | Notes |
|---|---|---|---|
| Sole trader or partnership (business name) | Unlimited | Owner's or partners' income tax on S04 (see `jm-income-tax`) | Partnership files IT03 for the sharing |
| Private company limited by shares | Limited | Corporate income tax on IT02 (see `jm-corporate-income-tax`) | Dividends to shareholders taxed separately |
| Company limited by guarantee | Limited | Non-profit use; may seek charity status | Annual return Form 19B |
| Branch of an overseas company | Parent liable | Jamaica-source profits | Registration with COJ as an overseas company |

Choosing between sole trader and company is a tax decision (25% company rate against 25% and 30% personal rates above the threshold, plus Education Tax, NHT and NIS on self-employed income): run both skills before advising.

## Deadlines and filing

| Step | Where | What | After |
|---|---|---|---|
| 1 | COJ (online or at the office) | Choose and check the name | Name approved with the filing |
| 2 | COJ | File Form 1A/1B Articles, the BRF and the BOR form, pay J$27,500 (plus expedition if wanted) | Certificate of Incorporation |
| 3 | COJ and TAJ | Obtain the company's TRN (the BRF in the package is the business registration form; check whether it covered the TRN and employer registrations, see Not yet confirmed) | TRN issued |
| 4 | TAJ | Apply for GCT registration (Form GCT-1) if supplies will reach J$15,000,000 in 12 months, or voluntarily (see `jamaica-gct`) | Certificate or Notice of Registration |
| 5 | TAJ | Register as an employer for PAYE and statutory deductions before the first payroll (see `jm-payroll-social`) | Monthly S01 by the 14th |
| 6 | COJ | Annual return (Form 19A, 19B or 19E) on each anniversary of incorporation, or the date the last return was made up to | Late fees up to J$10,000 |
| 7 | TAJ | Corporate IT02 and IT07 by 15 March each year | See `jm-corporate-income-tax` |

## Penalties and interest

- Late annual return: late fees up to J$10,000 per return; directors become liable to proceedings and the company can be removed from the register (restoration J$15,000).
- Tax penalties belong to the tax skills named above.

## Cross-border points

- A foreign company trading in Jamaica registers as an overseas company with COJ; its Jamaica-source profit is taxed under `jm-corporate-income-tax`.
- Non-resident shareholders: withholding on dividends is in the corporate and income tax skills (rates not yet confirmed there).

## Two worked examples that recompute

### Example: Incorporate a private company with same-day expedition, then file the first annual return

Incorporation package J$27,500, same-day expedition J$6,000, first annual return a year later J$5,000. Total COJ fees in the first year and a day: J$38,500. A late return could add up to J$10,000.

```oa-check
name: JM 2026 company formation, COJ fees first year
inputs:
  incorporation: 27500
  same_day: 6000
  annual_return: 5000
  late_cap: 10000
steps:
  - first_year: incorporation + same_day + annual_return
  - worst_case_late: first_year + late_cap
expected:
  first_year: 38500
  worst_case_late: 48500
```

## Ask the client first

1. Sole trader, partnership or company? How many owners, and are any non-resident?
2. Expected turnover in the first 12 months (GCT threshold J$15,000,000)?
3. Will there be employees from the start?
4. Is the business in a regulated sector (financial services, utilities) needing a licence?
5. Who are the directors, secretary and beneficial owners (for the BOR form)?
6. Is same-day or next-day registration needed?

## Sources

| Source | URL | Read on |
|---|---|---|
| COJ, fees page (first 25 of 121 entries, opened through Firecrawl because the site blocks scripts): read for the incorporation package, business name, expedition, amendment, share capital, charge, liquidation and restoration fees | https://www.orcjamaica.com/Fees.aspx | 2026-11-14 |
| COJ, "Filing annual return: what you need to know": read in full for when to file, the J$5,000 and J$2,000 fees, Forms 19A, 19B and 19E and the late fee cap | https://www.orcjamaica.com/FAQ/Filing%20Annual%20Returns.pdf | 2026-11-14 |
| TAJ, income tax and statutory contributions for self-employed individuals (updated November 2026): read for TRN registration, the business name option and the branch extension for GCT or employers | https://www.jamaicatax.gov.jm/documents/10194/20399532/4-Income+Tax+and+Self+Employed+Individuals++%28+Updated+Nov.+2026+%29.pdf/c4f3878c-7a44-0a3b-d4a2-4a8cbef3f9ef | 2026-11-14 |
| TAJ, General Consumption Tax guide: read for the J$15,000,000 registration threshold | https://www.jamaicatax.gov.jm/general-consumption-tax1 | 2026-11-14 |

Not yet confirmed: the minimum number of directors and whether a company secretary is required under the current Companies Act; the earlier version's statements that a private company has no minimum share capital and a public company about US$4,400 paid up; the 90-day name reservation period; the typical 4 working day incorporation time; the stamp duty of at least J$500 the earlier version listed separately (COJ now quotes one J$27,500 package); that the BRF itself issues NIS, NHT and HEART employer numbers (COJ's package lists the BRF; the scope of its agency registrations was not read); fees beyond the first 25 entries on the COJ list.
