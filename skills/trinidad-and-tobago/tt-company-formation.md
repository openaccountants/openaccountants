---
name: tt-company-formation
description: >
  How to incorporate a company in Trinidad and Tobago in 2026 through the
  Companies Registry online system and register it with the Inland Revenue
  Division. Gives the steps (Companies Registry Account, name search and
  reservation for TT$25 held 45 days, consent by directors and incorporators,
  Articles of Incorporation for TT$520, certificate collection), then the BIR
  file number, PAYE, health surcharge, VAT above TT$600,000 and NIS registrations.
  Trigger on Trinidad company formation, incorporate in Trinidad, Companies
  Registry Trinidad, CRA account, BIR number company. Built from the Registrar
  General and IRD pages; not reviewed by an accountant.
version: 1.0
jurisdiction: TT
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
tier: 2
domain: formation
type: filing-howto
---

# Trinidad and Tobago Company Formation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders incorporating a for-profit company under the Companies Act, Chap. 81:01, with the Companies Registry of the Office of the Registrar General in 2026, and registering it for tax. Amounts are TT$.

Out of scope: non-profit companies, external (foreign) companies, business name registration for sole traders and partnerships, regulated financial institutions.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Name search and reservation | TT$25 | Processing three working days; name reserved 45 days | Registrar General, Companies Registry, incorporate a company: https://legalaffairs.gov.tt/incorpcompany.php |
| Incorporation (Articles of Incorporation) | TT$520 | Filed online through the CRA; must be done within the 45-day reservation | same |
| VAT registration threshold | Commercial supplies over TT$600,000 in 12 months | See `trinidad-vat` | IRD, VAT page: https://www.ird.gov.tt/VAT |
| Business levy exemption | First twelve months after registration | See `tt-corporate-income-tax` | Corporation Tax Act, Chap. 75:02: https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.02-Corporation-Tax-Act--2024.pdf |

## The base

| Form | Liability | Tax |
|---|---|---|
| Company limited by shares | Members liable to the amount unpaid on shares | Corporation tax 30% (see `tt-corporate-income-tax`) |
| Sole trader or partnership (business name) | Unlimited | Income tax 25% and 30% or business levy (see `tt-income-tax`) |

## Deadlines and filing

| Step | Where | What | After |
|---|---|---|---|
| 1 | Companies Registry Online System | Every director, incorporator and attorney-at-law creates a Companies Registry Account (CRA): personal details, birth certificate, two photo IDs and a headshot holding one ID | CRA active |
| 2 | CROS search | Check the name is not the same as or similar to an existing business name, corporation name or trademark | Shortlist |
| 3 | CRA, Name Reservation | Apply and pay TT$25 | Approved (reserved 45 days), queried or rejected (new fee) |
| 4 | Each CRA | Directors, incorporators and statement signatories approve their inclusion using the name reservation number; companies approve through a director or secretary | Surname and Account PIN given to the applicant |
| 5 | CRA, Registration/Incorporation | File Articles of Incorporation and pay TT$520 | Emailed confirmation; Articles, Notice of Address and Notice of Directors to download |
| 6 | Companies Registry counter | Print two copies, sign with wet signatures and deliver | Certificate of Incorporation |
| 7 | IRD | BIR file number for the company; set the Established Accounting Terminal Date | BIR number |
| 8 | IRD | PAYE and health surcharge accounts if hiring; VAT registration if over TT$600,000; withholding tax account if paying abroad | See the tax skills |
| 9 | NIBTT | Register as an employer before the first payroll | See `tt-payroll-social` |

## Penalties and interest

Penalties after incorporation belong to the tax skills (late corporation tax return TT$1,000 per six months: `tt-corporate-income-tax`).

## Cross-border points

Foreign directors need the same CRA identity documents. Payments abroad need a withholding tax account (see `tt-corporate-income-tax`).

## Two worked examples that recompute

### Example: Government fees to incorporate, with one rejected name

A first name is rejected (TT$25 lost), a second is approved (TT$25), then incorporation (TT$520): TT$570.

```oa-check
name: TT 2026 incorporation fees with one rejected name
inputs:
  reservation: 25
  incorporation: 520
  attempts: 2
steps:
  - total: reservation * attempts + incorporation
expected:
  total: 570
```

## Ask the client first

1. Company name options, and has a CROS search been run?
2. Who are the directors, incorporators and the statement signatory, and do they all have CRAs?
3. Expected turnover in the first year (VAT TT$600,000)?
4. Employees from the start?
5. Payments to non-residents expected?

## Sources

| Source | URL | Read on |
|---|---|---|
| Office of the Registrar General, Companies Registry, incorporate a company: read in full for steps 1 to 6, the TT$25 and TT$520 fees and the 45-day reservation | https://legalaffairs.gov.tt/incorpcompany.php | 2026-11-14 |
| IRD, VAT page: read for the TT$600,000 threshold | https://www.ird.gov.tt/VAT | 2026-11-14 |
| IRD, corporations page: read for the BIR file number and EATD | https://www.ird.gov.tt/corporations | 2026-11-14 |
| Corporation Tax Act, Chap. 75:02: read for the s. 3A business levy exemption | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.02-Corporation-Tax-Act--2024.pdf | 2026-11-14 |

Not yet confirmed: no minimum share capital and no par value shares; the minimum number of directors and any residence requirement; the annual return filing date and fee at the Companies Registry; the 3 to 6 week timeline in the earlier version; the earlier version's 90-day name reservation, which the Registry page contradicts (45 days).
