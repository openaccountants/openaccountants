---
name: bd-formation
description: "Bangladesh 2026 business setup and entity-choice routing: TIN, local trade licence, banking evidence, VAT registration and online-selling/partnership referrals, distinct from company incorporation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bd-formation"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bangladesh sole-trader and business registrations v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For a person starting freelancing or a small business. This file organizes registrations; bd-company-formation owns company incorporation. Do not infer that a solo operator is incorporated or that every online activity has identical licensing requirements.

## Ask the client first

- Activity, owners, customers and location/local licensing authority.
- Legal form, residence/NID and existing TIN.
- Expected and actual turnover, imports/exports and bank arrangements.
- Staff, regulated activities, online selling and any foreign owners.

## The method, step by step

1. Compare sole proprietorship (individual owner and personal liability), partnership (deed/partners and separate firm tax reporting), and company (incorporation, governance and accounts/audit). Partnership Act sections 4-6 require an agreement to share business profits with all or any acting for all; status or profit-sharing alone does not establish partnership (https://bdlaws.minlaw.gov.bd/act-157/act-chapter-print-411.html). Do not choose solely on a headline tax rate. Route company setup to [company formation](bd-company-formation.md); the Companies Act defines the separate legal forms (https://bdlaws.minlaw.gov.bd/act-788/section-32006.html, https://bdlaws.minlaw.gov.bd/act-788/section-32025.html).
2. Obtain taxpayer registration/TIN through the NBR's official e-TIN service linked from https://nbr.gov.bd; use the actual entity identity and documents. The individual e-Return at https://etaxnbr.gov.bd is a filing service, not a substitute for incorporation. Keep the certificate and login under the taxpayer's control.
3. Obtain the applicable trade licence from the city corporation, paurashava or union parishad. The official investment FAQ describes OSS services for participating city corporations, or the local form, supporting documents/NOC, enquiry and assessed fee route elsewhere. Collect the issued licence and track renewals; no universal fee is asserted (https://investbangladesh.gov.bd/faq).
4. Open the appropriate business banking arrangement and retain remittance/encashment certificates for export receipts. An account does not by itself prove tax exemption or an incentive award.
5. Apply [VAT](bangladesh-vat.md) to registration/enlistment, including turnover-independent activity triggers and voluntary registration. Do not use the old turnover amounts or assume every unregistered freelancer is outside all obligations. Preserve the certificate/BIN and effective date. Sections 2 and 4 test actual preceding and expected following 12-month turnover, excluding specified amounts: ordinary registration is over BDT 5,000,000 (50 lakh, in words on the page), while section 4 also lists activities requiring registration regardless of turnover (https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42295.html; https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42297.html). Section 8 applies the same VAT duties to voluntary registration and bars an application to cancel until at least 1 year has elapsed (https://bdlaws.minlaw.gov.bd/act-1106/section-42301.html).
6. Online selling needs a separate check of the currently applicable DBID/e-commerce and sector rules. Do not assume that a trade licence replaces every activity permission. Keep this unresolved check in the setup checklist rather than inventing a DBID mandate for all freelancers.
7. File applicable annual income-tax returns and retain proof of filing using [PIT](bangladesh-pit.md) or corporate tax, as appropriate. TIN, trade licence, VAT and income-tax return are separate obligations.

## Worked cases

### Expected turnover triggers registration work

An ordinary taxable domestic business expects BDT 450,000 each month for the following 12 months, all within statutory turnover, with no exempt/excluded value. Expected turnover is 5,400,000, exceeding the 5,000,000 registration threshold by 400,000. Register under section 4 and follow the current Rule 4 application route in [VAT](bangladesh-vat.md); waiting for profit or the first full year would miss the expected-turnover test. Activity-independent triggers must also be tested even below this amount.

```oa-check
name: Expected taxable turnover exceeds registration threshold
inputs:
  monthly_turnover: 450000
  months: 12
  registration_threshold: 5000000
steps:
  - expected_turnover: monthly_turnover * months
  - excess: expected_turnover - registration_threshold
expected:
  expected_turnover: 5400000
  excess: 400000
```

### Edge: voluntary registration cannot be cancelled early

A voluntarily registered business has completed 8 calendar months since registration. Section 8(3)'s minimum 1 year has not elapsed: 4 calendar months remain before it may apply for cancellation. Track the actual registration anniversary, not a guessed day count; reaching that anniversary permits an application and does not automatically cancel the registration or waive the remaining conditions.

```oa-check
name: Voluntary registration minimum period before cancellation application
inputs:
  minimum_calendar_months: 12
  completed_calendar_months: 8
steps:
  - remaining_calendar_months: minimum_calendar_months - completed_calendar_months
expected:
  remaining_calendar_months: 4
```

## When to refuse or refer

Refer partnership deed/registration specifics, online-seller DBID scope, foreign ownership, regulated sectors and unclear local licence conditions. Never omit a confirmed licence or BIN duty, use a guessed threshold, or assume a legal form without the documents.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for official incorporation/post-incorporation and trade-licence process, authorities and documents | https://investbangladesh.gov.bd/faq | 2026-11-14 |
| Read for separate company forms and membership definition | https://bdlaws.minlaw.gov.bd/act-788/section-32006.html | 2026-11-14 |
| Read for company formation | https://bdlaws.minlaw.gov.bd/act-788/section-32025.html | 2026-11-14 |
| Read for NBR official service links including e-TIN/e-Return | https://nbr.gov.bd/regulations/acts/finance-acts/eng/contents/eng | 2026-11-14 |

| Read for Partnership Act sections 4-6 contractual relationship, profit sharing and agency conditions | https://bdlaws.minlaw.gov.bd/act-157/act-chapter-print-411.html | 2026-11-14 |
| Read for VAT Act section 2 registration threshold and statutory turnover exclusions | https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42295.html | 2026-11-14 |
| Read for VAT Act section 4 actual/expected rolling turnover and independent activity triggers | https://bdlaws.minlaw.gov.bd/act-print-1106/section-print-42297.html | 2026-11-14 |
| Read for VAT Act section 8 voluntary duties and minimum year before cancellation application | https://bdlaws.minlaw.gov.bd/act-1106/section-42301.html | 2026-11-14 |

Not yet confirmed: Activity-specific DBID/e-commerce duty, local licence fees/renewals, partnership registration details and live registration fields for the individual; these are checks to resolve, not a universal exemption or mandate.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bd-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bd-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
