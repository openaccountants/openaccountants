---
name: cf-company-formation
description: >
  Use this Central African Republic formation Guide for 2026 research on SARL and SA capital, subscription, payment, registration and ordinary annual reporting. It separates OHADA uniform-act defaults from national formalities, and maps the published GUFE dossier route without promising a statutory processing time. Search triggers include RCCM, NIU, NIF, SARL capital, SA capital, incorporation, share subscription and annual accounts. Tax filing and fiscal visa obligations are routed to their own Guide. The national capital-override check, exact fees, local supporting forms and current filing channels remain unresolved. This is a source-based partial draft, not registration advice for an identified company.
jurisdiction: CF
category: formation
tax_year: 2026
tax_year_notes: "2026 research draft; conditional code baseline and named enacted amendments, not full operative coverage"
tier: 2
last_updated: 2026-11-01
version: 0.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Central African Republic company formation and annual reporting v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status:** People choosing a SARL or SA and preparing formation/annual-reporting working papers. Other entity forms, regulated businesses and public offerings require separate law. Independent pack review is pending. Do not treat this draft as an accountant sign-off or permission to file.

## Who this applies to

The OHADA SARL limits members’ debt exposure to their contributions and can have one individual/legal-person member or several. The SA similarly limits shareholder debt exposure and may have one shareholder. This is not a guarantee against personal guarantees or manager liability. [AUSCGIE arts. 309, 385](https://biblio.ohada.org/doc_num.php?explnum_id=2032) (ledger F01).

## Rates, bands and thresholds

| Item and conditions | Tax year / source |
|---|---|
| SARL default capital is XAF 1,000,000, divided into equal shares with at least XAF 5,000 nominal value, expressly subject to contrary national provisions. A live CAR national override check remains necessary; the default is not presented as an authenticated local floor. | 2026 research scope; AUSCGIE art. 311 [official text](https://biblio.ohada.org/doc_num.php?explnum_id=2032); ledger F02 |
| SARL capital is fully subscribed; in-kind contributions are fully paid. Cash shares require at least half nominal value on subscription, with the remainder within two years of RCCM registration under the statutes. The old “all cash fully paid at incorporation” assertion is not the uniform-act default. | 2026 research scope; AUSCGIE art. 311-1 [official text](https://biblio.ohada.org/doc_num.php?explnum_id=2032); ledger F03 |
| SA minimum capital is XAF 10,000,000 and fully subscribed before signing statutes. Cash shares require at least one quarter nominal value at subscription; remainder within three years of RCCM registration. The SARL cash fraction does not apply to an SA. | 2026 research scope; AUSCGIE arts. 387–389 [official text](https://biblio.ohada.org/doc_num.php?explnum_id=2032); ledger F04 |

## The base

SARL cash funds are deposited immediately against receipt in an approved bank, credit/microfinance institution or a notary’s office in the forming company’s name. Statutes record payment/deposit, and funds become available to the manager on RCCM registration. National deposit/subscription formalities require separate verification. [AUSCGIE arts. 313–314](https://biblio.ohada.org/doc_num.php?explnum_id=2032) (ledger F05).

Except a société en participation, companies require RCCM registration; legal personality begins on registration unless the Act provides otherwise. Signing statutes establishes formation but does not generally make pre-registration existence opposable to third parties. [AUSCGIE arts. 97–101](https://biblio.ohada.org/doc_num.php?explnum_id=2032) (ledger F06).

Choose the entity against actual governance, liability, tax and financing needs. Verify national rules before using uniform-act defaults. Separate subscribed capital from cash payable now and in-kind value. Prepare statutes and deposit evidence, then submit the appropriate local dossier. Retain RCCM proof before treating the company as a legal person. Identify the annual accounts, approval and tax/visa obligations separately.

## Deadlines and filing

Managers establish annual financial statements and management report. In the article 140 companies the annual statements/report go to statutory auditors at least 45 days before the ordinary meeting, which must be within six months after year-end. Determine whether an auditor is required before applying that delivery duty. [AUSCGIE arts. 137–140](https://biblio.ohada.org/doc_num.php?explnum_id=2032) (ledger F07).

GUFE’s published local route is: obtain form/checklist for entity; assemble identity, criminal-record, seat, statutes and capital-deposit evidence as applicable; submit complete dossier and pay at the counter; collect RCCM/tax/affiliation outputs and complete connected tax/social and sector-permit formalities. Its “48 working hours” is a published service statement, not a guaranteed statutory deadline established by this reading. [GUFE, Procédure de création, steps 1–3](https://gufe-rca.org/creer-mon-entreprise/procedure-de-creation/) (ledger F08).

Follow the GUFE dossier route in the cited row and obtain the current form/checklist directly before filing. Do not treat a general webpage as the current tariff or a guaranteed approval. Company tax/DSF is in [corporate income tax](cf-corporate-income-tax.md), tax registration in [tax overview](cf-tax-overview.md), and employee obligations in [payroll](cf-payroll-social.md).

## Penalties and interest

National company-law criminal penalties and current registry late-filing sanctions were not fetched. Do not invent an automatic fine for incomplete or late registration; escalate with the actual notice and statute.

## Cross-border points

Foreign founders need the local identity/residence documents and permissions applicable to their facts. A foreign member does not itself settle tax residence, treaty eligibility or business licensing.

## Two worked examples that recompute

All amounts below are XAF. Inputs are fictional. Code-baseline cases are conditional on confirming the cited provisions remain applicable to the actual 2026 case. Arithmetic checks do not verify current law.

### 1. Compare SARL and SA cash at default minimum capital

Assume no national override, all contributions in cash, ordinary uniform-act minima and no stricter statutes. SARL minimum subscribed capital of 1,000,000 requires 500,000 at subscription. SA minimum subscribed capital of 10,000,000 requires 2,500,000 then. The immediate cash difference is 2,000,000, but tax/governance can determine the entity choice.

```oa-check
name: Compare SARL and SA cash at default minimum capital
inputs:
  sarl_capital: 1000000
  sa_capital: 10000000
steps:
  - sarl_now: sarl_capital*0.5
  - sa_now: sa_capital*0.25
  - difference: sa_now-sarl_now
expected:
  sarl_now: 500000
  sa_now: 2500000
  difference: 2000000
```

### 2. SARL mixed contributions

Assume XAF 2,000,000 subscribed SARL capital, made of XAF 800,000 cash and XAF 1,200,000 in-kind. The minimum initial cash is 400,000, all 1,200,000 in-kind must be paid, so initial paid value is 1,600,000 and cash remaining is 400,000. This is subject to the separate valuation and national-formality checks.

```oa-check
name: SARL mixed contributions
inputs:
  cash: 800000
  kind: 1200000
steps:
  - cash_now: cash*0.5
  - initial_paid: cash_now+kind
  - cash_remaining: cash-cash_now
expected:
  cash_now: 400000
  initial_paid: 1600000
  cash_remaining: 400000
```

## Ask the client first

- SARL, SA or another form and actual business/regulated sector?
- Members, cash and in-kind contributions, and funding now/later?
- Seat, local representative and foreign identity/authorisation evidence?
- Current national capital rules, local forms and official fee schedule?
- Year-end, governance body, auditor requirement and annual filing route?

## Sources

| Source | URL | Read on / scope |
|---|---|---|
| OHADA AUSCGIE signed 2014 text | https://biblio.ohada.org/doc_num.php?explnum_id=2032 | 2026-11-01; Read arts.97–104,137–143,309–314,385–389 with surrounding text; numeric cash provisions visually checked pp.77 and95. Not whole Act. |
| GUFE published creation procedure, steps and local dossier | https://gufe-rca.org/creer-mon-entreprise/procedure-de-creation/ | 2026-11-01; Read procedure/dossier/collection sections; live forms, fee tariff and applicable national override not opened. |

Not yet confirmed: Current national capital overrides, full in-kind valuation and foreign-founder conditions, exact GUFE fees/forms, notarisation exceptions and authorised deposit process; registration timeline as a statutory right; all registry/accounting filings and national penalties; an authenticated current SYSCOHADA reporting package. No universal “several weeks” timeline is retained.

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
