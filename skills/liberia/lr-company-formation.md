---
name: lr-company-formation
description: "Routes a 2026 Liberia business formation through the Liberia Business Registry, distinguishes sole trader, partnership, corporation and limited liability company documents, and links registration to tax and social-security compliance. Use for Liberia company incorporation, a business registration certificate, RF-001, TIN registration, name reservation, an LLC or a foreign company. The Guide relies on published regulator and investment-agency instructions, preserves discrepancies between their document lists and removes unsupported agent prices and processing promises. It is an administrative starting point, not a complete Associations Law opinion or a guarantee of approval. Capital rules, current statutory fees, foreign investment restrictions and live forms remain explicit gaps in this partial pack."
jurisdiction: LR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
version: 0.1
---

# Liberia Company Formation and Entity Choice v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Read on: 2026-11-01. Source-cited country draft; currentness gaps are listed below.

## Who this applies to

A person preparing to register and operate a domestic or foreign business in Liberia. Entity selection requires the actual owners, liability model and activity; the available administrative categories do not prove identical legal or tax treatment. LBR registration is required before business activity and is renewed annually. Obtain sector authorisations where applicable; registration alone is not a sector licence. [Business Tax Kinds, registration](https://www.lra.gov.lr/domestic-tax-profile/businesstaxkinds/) [F01]

## Rates, bands and thresholds

| Rule | Condition and result | Official source |
|---|---|---|
| F04 | NIC says a reserved name lasts 120 days. The old six-month claim is not supported. Its approximate fee is not treated as a statutory fixed fee; no 700/900 USD agent-price claim is retained. | [Starting a Business, name reservation](https://www.nic.gov.lr/pages/starting-a-business/) [F04] |
| O05 | A resident with a tax obligation must obtain one TIN, must not obtain multiple TINs, and must give it to the withholding agent. Obtaining the TIN itself is free. | [s 53(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O05] |

## The base

For LLCs the LRA list names certificate of formation and member/applicant IDs; business corporations need incorporation and subscriber/beneficial-owner IDs; partnerships need their agreement and partner IDs; sole traders need legal ID and photo. Foreign entities have additional authority/resolution/good-standing/representative documents. [entity document list](https://www.lra.gov.lr/domestic-tax-profile/businesstaxkinds/) [F02]

NIC identifies RF-001, constitutional documents and ID with Form A/B, with E/F/Q as applicable, submission at LBR, coordinated TIN/BPS, payment at bank window, receipt back to LBR, then approval/certificate. Its LLC document wording differs from the LRA list; confirm the selected entity’s live checklist. [Starting a Business, application](https://www.nic.gov.lr/pages/starting-a-business/) [F03]

Follow this order: choose the legal form and obtain its current checklist; reserve an available name; assemble constitution, owner/beneficial-owner and representative documents; submit the prescribed LBR forms; obtain the official fee assessment; pay through the designated bank; return the Government receipt and receive the approval/certificate and TIN. The NIC and LRA lists use different LLC constitutional document terms, so do not substitute corporate Articles for an LLC Certificate without Registry confirmation.

## Deadlines and filing

LBR registration is required before business activity and is renewed annually. Obtain sector authorisations where applicable; registration alone is not a sector licence. [Business Tax Kinds, registration](https://www.lra.gov.lr/domestic-tax-profile/businesstaxkinds/) [F01]

Renew the certificate annually and separately calendar income returns/advances, GST if registered, payroll withholding and NASSCORP if employing staff. Routes: [corporate](lr-corporate-income-tax.md), [GST](lr-vat-gst.md), [payroll](lr-payroll-social.md). No promise of one-to-three-day incorporation, USD 700 setup or USD 900 renewal is verified. Current fees are obtained from the Registry assessment, not a private agent estimate.

## Penalties and interest

The LRA registration page warns that unregistered or expired businesses can incur fines/penalties. The 2026 amended Revenue Code s 92 addresses knowing failure to obtain required licensing/registration, with conviction conditions. Do not turn that into an automatic administrative fee. [Business Tax Kinds, registration](https://www.lra.gov.lr/domestic-tax-profile/businesstaxkinds/) [F01] [amended ss 76,90–92](https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf) [O12]

## Cross-border points

Liberian incorporation does not by itself prove tax residence or tax exemption. The residence/limited nonresident-domestic exceptions and PE tests are explained in [Corporate](lr-corporate-income-tax.md) and [Cross-border](lr-cross-border.md). Sector approvals and foreign entity authority are separate from domestic incorporation. [s 801(a)–(e)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [C11]

## Two worked examples that recompute

### Separate a TIN charge from quoted services

Suppose a service provider quotes LRD 12,000 incorporation assistance and LRD 3,000 labelled as a government charge for issuing the TIN. The statutory TIN fee is zero, so 3,000 needs removal or clarification as separately agreed private work, not payment as tax-authority TIN fees. Verified private service cost remains 12,000; this does not establish the Registry incorporation fee. [s 53(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O05]

```oa-check
name: Separate a TIN charge from quoted services
inputs:
  assistance: 12000
  claimed_tin_fee: 3000
steps:
  - quoted_total: assistance + claimed_tin_fee
  - verified_tin_fee: 0
  - amount_to_query: claimed_tin_fee - verified_tin_fee
  - retained_private_cost: assistance
expected:
  quoted_total: 15000
  verified_tin_fee: 0
  amount_to_query: 3000
  retained_private_cost: 12000
```

### Budget two separate annual certificate renewals

Two separately registered operating businesses each have twelve-month registration validity. Assume the current Registry has actually assessed LRD 6,000 renewal per certificate. Reserve 12,000 for their two renewals, or 1,000 per month. The fee is an example assumption, not an asserted statutory amount; do not use the old USD 900 quote. [Business Tax Kinds, registration](https://www.lra.gov.lr/domestic-tax-profile/businesstaxkinds/) [F01]

```oa-check
name: Budget two separate annual certificate renewals
inputs:
  certificates: 2
  assessed_fee_each: 6000
steps:
  - annual_budget: certificates * assessed_fee_each
  - monthly_reserve: annual_budget / 12
expected:
  annual_budget: 12000
  monthly_reserve: 1000
```

## Ask the client first

- Proposed activity, sector licences, owners/beneficial owners and nationality.
- Sole trader, partnership, LLC, corporation or foreign branch, and reasons for limited liability.
- Existing TIN, entity documents, representative and tax residence.
- Staff, turnover and expected renewal/filing obligations.

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| December 2024 general amendment, approved 17 December/printed 20 December 2024, substantive pages 1–9 | https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf | 2026-11-01; read in part, specific scope in first column |
| Revenue Code 2020, selected general, income, nonresident, filing and GST provisions | https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf | 2026-11-01; read in part, specific scope in first column |
| LRA Forms and Schedules, named return/schedule links read; not a completed portal filing | https://www.lra.gov.lr/forms-and-schedules/ | 2026-11-01; read in part, specific scope in first column |
| National Investment Commission, Starting a Business, application and name reservation paragraphs read | https://www.nic.gov.lr/pages/starting-a-business/ | 2026-11-01; read in part, specific scope in first column |
| LRA Business Tax Kinds, registration, entity documents, annual renewal and payment instructions read | https://www.lra.gov.lr/domestic-tax-profile/businesstaxkinds/ | 2026-11-01; read in part, specific scope in first column |
| December 2025 amendment, approved 24 March/printed 1 April 2026, cover/preliminary/amended 63,74,76,79,90–92,803,805,806,1000,1021; excise schedule not used | https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf | 2026-11-01; read in part, specific scope in first column |

Not yet confirmed: Full Associations Law and amendments; minimum capital by entity type; live LBR document requirements, fee schedule and approval timing; foreign ownership/reserved activities; financial statements, audit and beneficial-ownership filing deadlines; binding reconciliation of NIC/LRA LLC document terminology.

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
