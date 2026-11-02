---
name: na-company-formation
description: >
  Namibia company formation, 2026: Pty Ltd, Ltd, CC, section 21 and external company, BIPA steps, beneficial ownership and annual duties. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: NA
category: international
tax_year: 2026
tax_year_notes: "Individuals: year of assessment 1 March 2026 to 28 February 2027. Companies: financial year."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Namibia Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

## Who this applies to

Anyone forming a business in Namibia. Registrar: Business and Intellectual Property Authority (BIPA).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Private company members | Typically maximum 50 | 2026 | https://www.bipa.na/business-registration/companies/private/ |
| Directors | Private at least one, public at least two | 2026 | https://www.lac.org.na/laws/annoSTAT/Companies%20Act%2028%20of%202004.pdf (s.216(1)) |
| Public company memorandum | Signed by not less than seven | 2026 | https://www.lac.org.na/laws/annoSTAT/Companies%20Act%2028%20of%202004.pdf |
| Close corporation members | 1 to 10 | 2026 | https://www.lac.org.na/laws/annoSTAT/Close%20Corporations%20Act%2026%20of%201988.pdf (s.2(1)) |
| Beneficial owner test | 25% or more, or control | 2026 | https://www.bipa.na/beneficial-ownership/ |
| Beneficial ownership update | 7 working days after a change; yearly at financial year end | 2026 | https://www.bipa.na/beneficial-ownership/ |
| Fees | Set on the BIPA schedule, effective 1 January 2020 | 2020 | https://www.bipa.na/business-registration/application-fees/ |

## The base

Other forms: section 21 company not for gain, and external company for a foreign company in Namibia (Companies Act 28 of 2004). CCs have members, not shares, and an accounting officer.

## Deadlines and filing

Private or public company ([BIPA](https://www.bipa.na/business-registration/companies/private/)): 1. Reserve the name. 2. On approval, complete the memorandum and articles booklet, in triplicate (one original, two notarised). 3. Add loose forms: notice of addresses, list of directors, auditors and public officers, certified copies of directors' IDs, name approval, beneficial ownership forms. 4. Obtain the certificate of incorporation and certificate to commence business.

CC ([BIPA](https://www.bipa.na/business-registration/close-corporation/)): 1. Reserve the name. 2. Submit the founding statement in triplicate with name approval, accounting officer's consent, certified IDs, and beneficial ownership forms. Foreign passports are notarised or apostilled.

After that: annual return CM23 (company) or CC7 annual duty (CC) ([BIPA](https://www.bipa.na/annual-returns/)). If no BO change, a BO2 form may serve. Register with NamRA (https://www.namra.org.na/documents/cms/uploaded/information-brochure--how-to-register-on-itas-ce02d8af03.pdf), for VAT if over the [threshold](na-vat-gst.md), and SSC if employing. Companies appoint a public officer and auditor (Companies Act s.278).

## Penalties and interest

BIPA refuses new applications for entities without a complete BO declaration ([BIPA](https://www.bipa.na/beneficial-ownership/)).

## Cross-border points

Foreign company: register an external company, or incorporate. Foreign owners supply notarised or apostilled ID.

## Two worked examples that recompute

Example 1. Pty profit N$500,000 at 30% gives N$150,000.

```oa-check
name: Company
inputs:
  p: 500000
steps:
  - tax: p * 0.30
expected:
  tax: 150000.00
```

Example 2. A decision: sole trader or company at N$500,000. Personally N$59,000 + 28% of N$150,000 = N$101,000, N$49,000 less than the company before any salary or dividend effects.

```oa-check
name: Sole v company
inputs:
  p: 500000
steps:
  - s: 59000 + (p - 350000) * 0.28
  - d: p * 0.30 - s
expected:
  d: 49000.00
```

## Ask the client first

1. Owners, and are any foreign?
2. Need for outside investors?
3. Expected profit?
4. Not for gain?
5. Existing foreign company?

## Sources

| Source | URL | Read on |
|---|---|---|
| BIPA private companies (read: whole page) | https://www.bipa.na/business-registration/companies/private/ | 2026-11-01 |
| BIPA close corporation (read: whole page) | https://www.bipa.na/business-registration/close-corporation/ | 2026-11-01 |
| BIPA beneficial ownership (read: part) | https://www.bipa.na/beneficial-ownership/ | 2026-11-01 |
| BIPA annual returns (read: list) | https://www.bipa.na/annual-returns/ | 2026-11-01 |
| Companies Act 28 of 2004 (read: targeted) | https://www.lac.org.na/laws/annoSTAT/Companies%20Act%2028%20of%202004.pdf | 2026-11-01 |
| Close Corporations Act (read: s.2) | https://www.lac.org.na/laws/annoSTAT/Close%20Corporations%20Act%2026%20of%201988.pdf | 2026-11-01 |

Not yet confirmed: No minimum share capital; audit relief for private companies and CCs; typical timeline of days to weeks (old skill, not on pages read); annual duty amount and due date; fee amounts.

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
