---
name: bd-financial-statements
description: "Bangladesh 2026 distinction between sole-trader working accounts, company statutory statements and income-tax audit/certification requirements for companies, firms and other taxpayers."
version: 1.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: financial-statements
type: situation-rules
---

# Bangladesh financial statements and audit v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Triage statutory reporting and prepare a reviewable accounts package. Companies Act filing is separate from the income-tax return. A sole proprietor is not automatically a Companies Act company, but that does not exempt every individual or partnership from tax reporting/certification.

## Ask the client first

- Legal form, public-interest/regulatory status and financial year.
- Turnover, capital, long-term contracts and business activity.
- Prior statements, trial balance, audit appointments and AGM dates.
- Applicable adopted reporting standards and regulator instructions.

## The method, step by step

### Requirements card

| Taxpayer/condition | Requirement and threshold | Official source |
|---|---|---|
| Company annual statements | Balance sheet and profit/loss or income/expenditure presented at AGM; statutory audit | Companies Act section 183: https://bdlaws.minlaw.gov.bd/act-788/section-33572.html |
| Company accounts filing | Within 30 days after presentation at AGM, or last lawful AGM date if not held; attach reasons where not approved/not held | Companies Act section 190: https://bdlaws.minlaw.gov.bd/act-788/section-33579.html |
| Public-interest company | Follow FRC standards under the Financial Reporting Act; no blanket small-company IFRS-for-SMEs exemption is supplied | Companies Act section 190(1A): https://bdlaws.minlaw.gov.bd/act-788/section-33579.html |
| Company taxpayers, persons with long-term-contract income, or firms/AOP/HUF/artificial persons exceeding turnover/capital trigger | Audited/certified statements; current triggers are turnover over 100,000,000 (10 crore, in words on the page) or capital over 50,000,000 (5 crore, in words on the page) for the listed non-company entities | Income Tax Act section 73(1): https://bdlaws.minlaw.gov.bd/act-1429/section-51903.html |
| All firms/AOP/HUF/artificial-person taxpayers | Certified income computation sheet even where statement-audit trigger is not met | Income Tax Act section 73(2): https://bdlaws.minlaw.gov.bd/act-1429/section-51903.html |

1. Prepare records and a trial balance using [bookkeeping](bd-bookkeeping.md). A normal sole freelancer keeps income, costs, banks and assets for the individual return; do not demand RJSC company filings merely because they freelance. Check the long-term-contract and activity-specific provisions before stating no audit/certification is required.
2. Companies prepare the statutory accounts, arrange the qualified auditor and present them at the AGM. Section 73 defines the tax-return statement package to include comprehensive income, equity changes, cash flows, financial position and notes; the income computation sheet reconciles allowable/disallowed items (https://bdlaws.minlaw.gov.bd/act-1429/section-51903.html).
3. For partnerships and other non-company entities, test the tax audit/certification rules separately from RJSC company reporting. The old statement that partnerships merely keep accounts with no further certification test is incomplete.
4. Determine the actual financial-reporting framework and regulator/FRC adoption. BFRS/IFRS labels in old files do not establish an automatic IFRS-for-SMEs option. Obtain the applicable standard before asserting compliance.
5. Retain signed accounts, auditor report, AGM evidence, income computation, tax-return attachments and Registrar filing acknowledgement. No particular return is complete merely because a spreadsheet balances.

## Worked cases

### Company working-paper reconciliation

Illustrative opening equity 1,000,000, profit 300,000 and distributions 100,000 produce closing equity 1,200,000. This reconciliation supports the statements; it does not replace audit or tax adjustments.

```oa-check
name: Company equity bridge for the statements package
inputs:
  opening_equity: 1000000
  profit: 300000
  distributions: 100000
steps:
  - closing_equity: opening_equity + profit - distributions
expected:
  closing_equity: 1200000
```

### Edge: partnership turnover threshold

Illustrative firm turnover 101,000,000 is 1,000,000 above the section 73(1) turnover threshold, so statement audit applies on that fact even with capital below the capital trigger. A firm at the threshold does not exceed it, but still needs the section 73(2) certified income computation. No long-term-contract or other special trigger is assumed absent without checking.

```oa-check
name: Firm above the statutory turnover audit trigger
inputs:
  turnover: 101000000
  trigger: 100000000
steps:
  - excess: turnover - trigger
expected:
  excess: 1000000
```

## When to refuse or refer

Refer reporting-standard selection, public-interest/regulated entities, consolidations, long-term contracts, activity-specific certification, audit eligibility and missed AGMs. Never tell every sole proprietor or partnership that statutory tax audit/certification cannot apply.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for Companies Act section 183 statements and audit | https://bdlaws.minlaw.gov.bd/act-788/section-33572.html | 2026-11-14 |
| Read for Companies Act section 190 filing, public-interest standards and missed/not-approved AGM exceptions | https://bdlaws.minlaw.gov.bd/act-788/section-33579.html | 2026-11-14 |
| Read for Income Tax Act section 73 complete entity/activity thresholds, certification and statement definition | https://bdlaws.minlaw.gov.bd/act-1429/section-51903.html | 2026-11-14 |

Not yet confirmed: The applicable FRC/sector reporting-standard adoption and any IFRS-for-SMEs eligibility for the particular entity, detailed auditor-qualification and penalty rules, and live RJSC submission fields. No blanket SME framework is asserted.
