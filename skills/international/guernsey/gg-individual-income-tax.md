---
name: gg-individual-income-tax
description: >
  Prepare ordinary calendar-year 2026 individual tax working papers for the Guernsey income-tax jurisdiction. Special caps, resident-only elections, trusts, pension encashments and foreign-tax relief are outside these calculations. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts.
version: 0.1
jurisdiction: GG
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guernsey individual income tax and residence v0.1

> **Source-cited draft.** Professional review is pending. Figures are limited to the periods and assumptions below. This Guide prepares working papers; it is not authority to file or pay.

## Scope

Prepare ordinary calendar-year 2026 individual tax working papers for the Guernsey income-tax jurisdiction. Special caps, resident-only elections, trusts, pension encashments and foreign-tax relief are outside these calculations.

Sources were accessed on 22 October 2026. A dated rate table controls its stated period; an undated guidance page does not prove that all later amendments have been incorporated.

## Residence and scope

Revenue Service guidance treats an individual as resident with at least 91 days in the year, or at least 35 days plus 365 days in the preceding four years. Principal residence includes 182 days, or 91 days plus 730 in the preceding four years, with an additional permanent-arrival rule. Sole residence also tests residence elsewhere. Record day counts, prior years and the subsequent-year evidence needed by the arrival rule. [Residence guidance and s3 extract](https://gov.gg/residency).

Do not treat an immigration permission or an address as the residence determination. Separately document which income enters the tax base and any treaty outcome.

## Ordinary 2026 rates

Income tax is 20%. The personal allowance is £15,200. Withdrawal starts at £85,000, at £1 for every £5 above it. Additional withdrawable reliefs follow a specified order; the protected pension amount and transfer rules require separate handling. [Rates and allowances](https://gov.gg/RStax-rates-and-allowances); [withdrawal rules](https://gov.gg/wopa).

## Computation

For a case where the reviewer has established the relevant income base, full personal-allowance entitlement, no transferred allowance, no additional relief and no special regime:

1. Set income `I` to the reviewed base, not automatically to gross cash receipts.
2. Compute withdrawal `W = max(0, (I - 85,000) / 5)`.
3. Personal allowance `A = max(0, 15,200 - W)`.
4. Preliminary tax `T = max(0, I - A) × 20%`.
5. Reconcile credits, withholding and payments separately. For additional reliefs, replace this simplified model with the published ordered withdrawal calculation.

| Assumed income | Allowance after withdrawal | Tax before credits |
|---|---:|---:|
| £50,000 | £15,200 | £6,960 |
| £85,000 | £15,200 | £13,960 |
| £100,000 | £12,200 | £17,560 |
| £161,000 | £0 | £32,200 |

At the allowance-only exhaustion boundary, £85,000 + 5 × £15,200 = £161,000. This does not establish exhaustion of additional reliefs.

## Filing and evidence

The Revenue Service states **30 November 2026 for the 2025 personal return**. Do not relabel that as the 2026-return deadline. Check the notice for the relevant year and retain confirmation of any automatic-assessment exemption. [Personal returns](https://gov.gg/revenue-service/personal-tax-returns).

Collect employment and investment statements, foreign income/tax records, residence-day evidence, pension records and each allowance's supporting documents. An unused allowance transfer must be supported by both parties' positions and consent; do not assume it remains available when the transferor's income changes. [Allowances guidance](https://gov.gg/RStax-rates-and-allowances).

## Forward changes

The tax-reform page describes personal-tax and GST changes for 2029 and corporate changes for 2027. They are not substituted into the 2026 calculation. Track enactment and commencement separately. [Tax reform timetable](https://gov.gg/taxreform).

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
