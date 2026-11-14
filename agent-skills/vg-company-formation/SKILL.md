---
name: vg-company-formation
description: "How to form and keep a BVI business company in good standing in 2026 under the BVI Business Companies Act (Revised Edition 2020). Covers the registered agent route, memorandum and articles, the register of beneficial ownership and its 2025 fees, the annual financial return filed with the registered agent on the new form from 2 November 2026, economic substance reporting, and what the territory does not tax. Annual fee amounts are not confirmed in this version. Trigger phrases include incorporate in the BVI, BVI business company, BVI annual financial return, BVI beneficial ownership, registered agent BVI."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vg-company-formation"
  jurisdiction: "VG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# BVI business company formation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Forming a BVI business company (BC) under the BVI Business Companies Act, Revised Edition 2020, and its yearly filings, in 2026. Limited partnerships, segregated portfolio companies, restricted purpose companies and trusts are named, not walked through. A BVI company pays no income tax; employment taxes are in [vg-payroll-social](vg-payroll-social.md) and the tax overview in [bvi-tax](bvi-tax.md).

## Ask the client first

1. What will the company do, and will it carry on a relevant activity for economic substance?
2. Who are the beneficial owners, and does any claim an exemption from disclosure?
3. How many shares will it be authorised to issue (this drives the government fee band)?
4. Financial year end (sets the financial return date).
5. Will it employ anyone in the territory (payroll tax and social security registration)?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure and conditions | Official source |
|---|---|---|
| Request to inspect or receive a copy of an entry in the Register of Beneficial Ownership, one legal entity (s.230(3A)(c)(viii)) | USD 75 | [SI 62 of 2025](https://laws.gov.vg/sites/default/files/2025-10/SI%20No%2062%20of%202025-BVI%20Business%20Companies%20%28Amendment%20of%20Schedule%201%29%20Order%202025.pdf) |
| Notice of objection; application opposing disclosure; notice of intent to appeal | USD 0 each | same |
| Application for exemption from disclosure of beneficial ownership information, or its renewal | USD 50 each | same |
| Certified copy of an entry in the Register of Beneficial Ownership (s.233) | USD 75 | same |
| Annual financial return form | Substituted Schedule in force from 2 November 2026 (balance sheet categories in US dollars) | [SI 71 of 2026](https://laws.gov.vg/sites/default/files/2026-11/SI%20No%2071%20of%202026%20--%20BVI%20Business%20Companies%20%28Financial%20Return%29%20%28Amendment%29%20Order%2C%202026%20%28signed%29.pdf) |

### Steps

1. **Appoint a licensed registered agent** in the territory; the agent files on the company's behalf and holds its records.
2. **Prepare the memorandum and articles** and the agent's due diligence on owners and directors.
3. **File for incorporation** with the Registry of Corporate Affairs through the agent and pay the government fee under Schedule 1 of the Act (amount not confirmed here).
4. **Beneficial ownership:** give the agent the beneficial ownership information for the Register of Beneficial Ownership. An owner who qualifies may apply for exemption from disclosure (USD 50) and renew it (USD 50).
5. **Each year:** pay the annual government fee; prepare the annual financial return on the form in the 2026 Schedule (from 2 November 2026) and give it to the registered agent; make the economic substance report where required.
6. **If it employs staff:** register for payroll tax on eTax (efiling.gov.vg) and with the Social Security Board before the first payroll.

## Worked cases

### Case 1: beneficial ownership fees for a two-owner company

Both owners apply for exemption from disclosure (2 x 50 = 100) and the company later orders one certified copy of an entry (75). Fees total 175.

```oa-check
name: BVI beneficial ownership register fees, 2026
inputs:
  exemption_fee: 50
  owners: 2
  certified_copy: 75
steps:
  - exemption_total: exemption_fee * owners
  - total: exemption_total + certified_copy
expected:
  exemption_total: 100
  total: 175
```

## When to refuse or refer

- Regulated businesses (banking, insurance, funds, virtual assets, trust business): licensing by the Financial Services Commission; refer.
- Economic substance tests: refer to an adviser and the Act's guidance.
- Fee amounts for incorporation and annual fees: confirm with the registered agent or Schedule 1 of the Act before quoting.

## Filing and payment

All filings go through the registered agent to the Registry of Corporate Affairs. The annual financial return is completed by the company on the 2026 form and lodged with the agent ([SI 71 of 2026](https://laws.gov.vg/sites/default/files/2026-11/SI%20No%2071%20of%202026%20--%20BVI%20Business%20Companies%20%28Financial%20Return%29%20%28Amendment%29%20Order%2C%202026%20%28signed%29.pdf)).

## Completion checklist

- Registered agent appointed; memorandum and articles filed.
- Beneficial ownership filed; exemptions applied for where due.
- Annual fee paid; financial return on the November 2026 form; economic substance report.
- Payroll and social security registration if staff.

## Sources

| Source | URL | Read on |
|---|---|---|
| SI 62 of 2025, BVI Business Companies (Amendment of Schedule 1) Order (PDF): read for the beneficial ownership fees | https://laws.gov.vg/sites/default/files/2025-10/SI%20No%2062%20of%202025-BVI%20Business%20Companies%20%28Amendment%20of%20Schedule%201%29%20Order%202025.pdf | 2026-11-14 |
| SI 71 of 2026, BVI Business Companies (Financial Return) (Amendment) Order (PDF): read for the commencement on 2 November 2026 and the substituted return form | https://laws.gov.vg/sites/default/files/2026-11/SI%20No%2071%20of%202026%20--%20BVI%20Business%20Companies%20%28Financial%20Return%29%20%28Amendment%29%20Order%2C%202026%20%28signed%29.pdf | 2026-11-14 |

Not yet confirmed: the incorporation and annual government fees (old files: USD 550 up to 50,000 shares and USD 1,350 above, one file also said 450 and 1,200); the annual fee due dates (old: 31 May or 30 November by incorporation half-year); the 9-month deadline for the financial return and the USD 5,000 maximum fine; the 6-month economic substance reporting deadline; the minimums of one director and one shareholder and the absence of a minimum capital; the 1 to 3 business day timeline. Schedule 1 of the Act (Revised Edition 2020) and the Financial Services Commission's company fee page could not be opened (the Commission's site refused direct fetches).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vg-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vg-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
