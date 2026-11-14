---
name: bd-company-formation
description: "Bangladesh 2026 company incorporation workflow, private-company member/director conditions, foreign capital evidence, statutory reporting and separate branch/liaison-office referral."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bd-company-formation"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bangladesh company incorporation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Ordinary company incorporation through RJSC/OSS. This is distinct from the sole-trader registrations in bd-formation. Public companies, one-person companies and foreign branch/liaison offices require their own conditions.

## Ask the client first

- Proposed business, ownership/nationalities and local/foreign capital.
- Entity form, intended members/directors and any public-company parent.
- Registered address, memorandum/articles and funding evidence.
- Activity licences, staff, tax registrations and foreign work-permit needs.

## The method, step by step

### Conditions card

| Condition | Requirement | Official source |
|---|---|---|
| Ordinary private company, not the separate one-person regime | At least 2 subscribers; private-company definition generally limits members to 50 excluding employees, joint holders count as one | Companies Act sections 5 and 2(1)(t): https://bdlaws.minlaw.gov.bd/act-788/section-32025.html; https://bdlaws.minlaw.gov.bd/act-788/section-32006.html |
| Private company other than a public company's subsidiary | At least 2 natural-person directors | Section 90: https://bdlaws.minlaw.gov.bd/act-788/section-32914.html |
| Public company or its private subsidiary | At least 3 directors; public formation requires at least 7 subscribers | Sections 90 and 5: https://bdlaws.minlaw.gov.bd/act-788/section-32914.html; https://bdlaws.minlaw.gov.bd/act-788/section-32025.html |

1. Choose the legal form and verify activity-specific approvals. Do not treat a foreign branch/liaison office as a local company or automatically impose its capital/remittance requirements on a local company. A one-person company is separately defined; do not apply the ordinary subscriber minimum to it without its special provisions.
2. Use the official OSS route linked in the investment authority FAQ (https://investbangladesh.gov.bd/faq) to apply for name clearance. Local company name validation and foreign name-clearance procedures differ. No universal name-validity period is asserted.
3. For foreign share capital, open the appropriate temporary bank account, remit capital matching the shareholding and collect the encashment certificate. Confirm the bank's documents and restrictions. The old USD 50,000 practical rule is not a statutory floor for every foreign-owned company.
4. Prepare the registered address, memorandum/articles, Form IX, Form I and subscription page identified in the official incorporation instructions. Submit through OSS, inspect the actual fee/stamp-duty assessment and pay the assessed amounts. Do not quote an assumed incorporation cost or completion time.
5. After approval retain incorporation certificate, memorandum/articles and Form XII. Obtain entity TIN, local trade licence and applicable BIN/VAT registration; import/export activities also require the relevant registration certificates. Use [VAT](bangladesh-vat.md) for the legal registration test.
6. Set the AGM, annual-return, accounts/audit and income-tax calendar using [financial statements](bd-financial-statements.md) and [corporate tax](bd-corporate-income-tax.md). Incorporation alone does not complete continuing compliance.

## Worked cases

### Paid versus unpaid subscribed shares

Illustrative 2 subscribers each subscribe 100,000 and together remit 150,000. Subscribed capital is 200,000, unpaid balance 50,000. Record these separately; the example is not a statutory minimum capital claim.

```oa-check
name: Subscription and remittance reconciliation
inputs:
  subscribers: 2
  each_subscription: 100000
  remitted: 150000
steps:
  - subscribed: subscribers * each_subscription
  - unpaid: subscribed - remitted
expected:
  subscribed: 200000
  unpaid: 50000
```

### Edge: public-company subsidiary director shortfall

An ordinary private company becomes a public company's subsidiary and has 2 directors. Against the statutory 3-director condition, the shortfall is 1. Assess the appointment before treating the entity as compliant.

```oa-check
name: Private subsidiary director condition
inputs:
  required_directors: 3
  existing_directors: 2
steps:
  - shortfall: max(required_directors - existing_directors, 0)
expected:
  shortfall: 1
```

## When to refuse or refer

Refer one-person/public companies, regulated sectors, foreign branch/liaison/work-permit matters, disputed name clearance and special capital rules. Never guarantee approval, processing time or a universal foreign-capital floor.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for company definition, private membership exceptions and one-person company definition | https://bdlaws.minlaw.gov.bd/act-788/section-32006.html | 2026-11-14 |
| Read for ordinary formation subscribers and limited-liability forms | https://bdlaws.minlaw.gov.bd/act-788/section-32025.html | 2026-11-14 |
| Read for director counts, public-parent exception and natural-person condition | https://bdlaws.minlaw.gov.bd/act-788/section-32914.html | 2026-11-14 |
| Read for incorporation, bank/encashment documents, post-incorporation registrations and separate branch process | https://investbangladesh.gov.bd/faq | 2026-11-14 |

Not yet confirmed: Current RJSC fee assessment, name-clearance expiry, processing duration, a universal minimum paid-up capital, foreign work-permit capital thresholds, and detailed one-person-company conditions. The old BDT 1 minimum, universal USD 50,000 floor, 30-day name-validity and 1-3 week promise are not usable instructions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bd-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bd-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
