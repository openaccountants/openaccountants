---
name: gi-payroll-social-insurance
description: "Prepare ordinary monthly payroll controls using the social-insurance schedule effective 1 July 2026. Special contribution classes, partial periods, employment-law entitlements and cross-border coverage require their own determination. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gi-payroll-social-insurance"
  jurisdiction: "GI"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Gibraltar payroll and social insurance v0.1

> **Source-cited draft.** Professional review is pending. Figures are limited to the periods and assumptions below. This Guide prepares working papers; it is not authority to file or pay.

## Scope

Prepare ordinary monthly payroll controls using the social-insurance schedule effective 1 July 2026. Special contribution classes, partial periods, employment-law entitlements and cross-border coverage require their own determination.

Sources were accessed on 22 October 2026. A dated rate table controls its stated period; an undated guidance page does not prove that all later amendments have been incorporated.

## Registration and reporting

Register each employee and obtain the ITO code. Remit deducted tax and social insurance by the 15th of each month. Annual P8, P10/P10A and P12 reporting is due by 31 July. Give a leaver P7A and an annual P7 certificate. Retain submission and payment receipts. [ITO employers, obligations section](https://www.gibraltar.gov.gi/income-tax-office/employers-and-trusts/employers).

## Monthly ordinary contribution table

For the ordinary earnings-related class, the published schedule effective **1 July 2026** gives:

| Contributor | Rate | Monthly minimum | Monthly maximum |
|---|---:|---:|---:|
| Employee | 10% | £62.11 | £176.76 |
| Employer | 18% | £138.55 | £243.65 |
| Self-employed, separate SE class | 20% | £131.95 | £232.05 |

[ITO 2026/27 contribution-class schedule](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Self-Employed/Social%20Insurance%20Contributions%20Class%202026-2027x.pdf). The schedule contains separate pensioner, married-woman, trainee and exemption classes. Do not assign them from age or job title without confirming the issued class and eligibility.

## Computation

1. Confirm class, pay frequency, full/partial period, and earnings base before selecting a schedule.
2. For a confirmed full-month ordinary class, compute employee `min(176.76, max(62.11, earnings × 10%))` and employer `min(243.65, max(138.55, earnings × 18%))`.
3. Use the employee's tax code and correct-year official tax tables for PAYE. Contribution rates are not income-tax rates.
4. Reconcile gross wages, PAYE, employee contributions, other deductions, net wages and employer cost separately.
5. Reconcile payroll totals to remittances and the annual return. Never multiply a rounded monthly cap to substitute for an official annual table.

**Examples:** full-month ordinary gross earnings £3,000 give employee SI **£176.76**, employer SI **£243.65** and gross-plus-employer-SI **£3,243.65**, before other employer costs. At £1,000, the respective amounts are **£100** and **£180**. A person with an exemption code must not be put through this formula.

## Evidence and exclusions

A detached-worker exemption needs the relevant coverage evidence. A pensioner, trainee, second job or self-employed worker needs the appropriate class. Refer to the complete schedule and the ITO's [social-insurance explanation](https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/social-insurance).

This draft does not calculate minimum wages, leave, redundancy, pension contributions or benefit-in-kind valuation. Preserve those as separate review lines rather than representing gross-plus-SI as total employer cost.

## Self-checks and output

- Retain the relevant source version, the applicable period and the facts establishing scope.
- Reconcile every input to the client's records; keep estimates separate from actual amounts.
- Recompute the example and boundary cases before applying the method.
- Record exclusions and unresolved points explicitly. Do not convert a missing source into an exemption.
- Deliver a calculation, evidence list, filing calendar and reviewer questions. Record the exact revision reviewed.

## Disclaimer

General tax and accounting reference material only. These drafts have not been professionally attested. A qualified professional in the relevant jurisdiction must check the facts, current law, elections and deadlines before anyone files, pays or acts on an output.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gi-payroll-social-insurance` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gi-payroll-social-insurance. If neither is available, confirm every figure against the official source pages cited above before relying on it.
