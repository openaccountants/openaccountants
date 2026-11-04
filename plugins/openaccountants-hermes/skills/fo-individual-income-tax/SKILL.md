---
name: fo-individual-income-tax
description: "Prepare ordinary 2026 resident individual national and municipal income-tax working papers. The Faroes have their own tax rules; Danish tax bands must not be imported. Capital income, shipping regimes and treaty exceptions require separate work. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/fo-individual-income-tax"
  jurisdiction: "FO"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Faroe Islands individual income tax v0.1

> **Source-cited draft.** Professional review is pending. Figures are limited to the periods and assumptions below. This Guide prepares working papers; it is not authority to file or pay.

## Scope

Prepare ordinary 2026 resident individual national and municipal income-tax working papers. The Faroes have their own tax rules; Danish tax bands must not be imported. Capital income, shipping regimes and treaty exceptions require separate work.

Sources were accessed on 22 October 2026. A dated rate table controls its stated period; an undated guidance page does not prove that all later amendments have been incorporated.

## Scope and assessment route

TAKS distinguishes automatically withheld A-income from B-income, including self-employment and income from a non-Faroese employer. B-income requires a preliminary income estimate and instalments. The published limited-liability description uses a stay of at most 180 days without a permanent address; a stay beyond 180 days in twelve months brings full liability. Do not decide treaty residence or an earlier permanent-address case from that threshold alone. [TAKS taxation overview](https://www.taks.fo/en/individuals/tax/taxation-in-the-faroe-islands).

## National tax table, 2026

Let `I` be the established annual national-tax base in DKK:

| Base interval | Tax formula |
|---|---|
| 0–65,000 | 0 |
| Over 65,000–180,000 | 13% × (I − 65,000) |
| Over 180,000–330,000 | 14,950 + 15% × (I − 180,000) |
| Over 330,000–450,000 | 37,450 + 20% × (I − 330,000) |
| Over 450,000–600,000 | 61,450 + 25% × (I − 450,000) |
| Over 600,000 | 98,950 + 30% × (I − 600,000) |

[TAKS 2026 national table](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-landsskatt).

## Municipal and church tax

Use the exact 2026 municipality row; the first DKK 30,000 is exempt from municipal tax. Church tax applies to church members and requires the locality footnotes, not just the municipality headline. For Tórshavnar, the municipal rate is 19%; the church footnote specifies 0.85% for Tórshavn/Ternuryggur and 0.90% for Argir/Borðan/Nólsoy. Child credits have separate eligibility. [2026 municipal table and footnotes](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-kommunuskatt-kirkjuskatt-og-barnafradratt).

## Example and boundaries

Assume a full-year resident, non-church-member adult in Tórshavnar, no child credit, and a reviewer-established **DKK 300,000 base for both taxes**, after relevant base adjustments:

- National: 14,950 + (300,000 − 180,000) × 15% = **32,950**.
- Municipal: (300,000 − 30,000) × 19% = **51,300**.
- Combined income tax before any other adjustments: **84,250**.

This is not take-home pay: pensions and statutory contributions are separate. At national thresholds, the adjacent formulas must agree: 180,000 → 14,950; 330,000 → 37,450; 450,000 → 61,450; 600,000 → 98,950. Test these before applying the method.

## Filing

Check a pre-completed statement and correct errors. Ordinary individuals/self-employed filers use the 1 May deadline; companies use 1 July. Self-employed accounts and applicable property statements accompany the return. Record any separately granted extension. [TAKS tax-return guidance](https://www.taks.fo/en/individuals/tax/tax-return).

**Open scope:** detailed base deductions, child-credit eligibility, foreign-tax credits, tax caps, capital-income rules and each special worker category. Do not claim a complete personal-tax calculation from the ordinary table alone.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `fo-individual-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/fo-individual-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
