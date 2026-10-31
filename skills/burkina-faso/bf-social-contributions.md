---
name: bf-social-contributions
description: Burkina Faso Social Security (CNSS) Skill v1.0
jurisdiction: BF
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burkina Faso Social Security (CNSS)

## Burkina Faso Social Security (CNSS) Skill v1.0

AI-drafted from official sources (CNSS Burkina Faso cnssbf.org; Décret n°2023-0129 du 24 février 2023 taux d'appel; Arrêté n°2022-067 du 30 août 2022 plafond; Loi n°015-2006/AN). Pending accountant verification. Note: the separate AMU universal-health scheme (Décret 2024-0345) is NOT covered here.

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Burkina Faso |
| Currency | FCFA (XOF) |
| Authority | Caisse Nationale de Sécurité Sociale (CNSS) |
| Pension branch (assurance vieillesse) | 14% total — employer 8.5% + employee 5.5% |
| Family benefits (prestations familiales) | 6% — employer only |
| Occupational risk (risques professionnels) | 1.5% — employer only (standard rate) |
| Total employer rate | 16% |
| Total employee rate | 5.5% |
| Combined total (taux d'appel) | 21.5% |
| Contribution ceiling (plafond) | 800,000 FCFA/month (9,600,000 FCFA/year) per worker |
| Declaration — employers >= 20 employees | Monthly, within 15 days of month-end |
| Declaration — employers < 20 employees | Quarterly, within 30 days of quarter-end |
| Late contribution penalty | 2% per month (or fraction) of delay |
| Late declaration penalty | 1% per month (or fraction) of delay |
| Voluntary insured | 14% (pension branch), borne entirely by the member |
| E-services | eservices.cnss.bf (e-CNSS) |
| Primary legislation | Loi n°015-2006/AN; Décret n°2023-0129 (rates); Arrêté n°2022-067 (ceiling) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | June 2026 |

## Section 2 -- Branches, rates and split

**Branches, rates and split**  _(Décret n°2023-0129 du 24 février 2023)_

| Branch | Total | Employer | Employee |
| --- | --- | --- | --- |
| Pensions / assurance vieillesse | 14% | 8.5% | 5.5% |
| Prestations familiales | 6% | 6% | 0% |
| Risques professionnels | 1.5% | 1.5% | 0% |
| **Total** | **21.5%** | **16%** | **5.5%** |

- **Rates basis and employee-funded branch** — Rates per Décret n°2023-0129 du 24 février 2023. Only the pension branch is employee-funded. The occupational-risk 1.5% is the standard/general rate.  _(Décret n°2023-0129 du 24 février 2023)_

## Section 3 -- Ceiling, contribution base and computation

- **Monthly contribution ceiling** — 800,000 FCFA FCFA/month (Per worker; 9,600,000 FCFA/year; raised from 600,000)  _(Arrêté n°2022-067)_
- **Contribution base** — Contributions are computed on gross remuneration up to a monthly ceiling of 800,000 FCFA (9,600,000 FCFA/year), per Arrêté n°2022-067 (raised from 600,000). Salary above the ceiling is not subject to contributions.  _(Arrêté n°2022-067)_
- **Employer/employee cost at ceiling** — Employer cost on a salary at/above the ceiling = 16% × 800,000 = 128,000 FCFA/month; employee = 5.5% × 800,000 = 44,000 FCFA/month.  _(Arrêté n°2022-067)_

## Section 4 -- Declaration, payment, penalties

- **Registration and declaration requirement** — Employers must register (immatriculation) with CNSS and declare each worker's remuneration on the bordereau nominatif.  _(Loi n°015-2006/AN)_
- **Declaration frequency by employer size** — >= 20 employees: monthly, within 15 days of month-end. < 20 employees: quarterly, within 30 days of quarter-end.  _(Loi n°015-2006/AN)_
- **Late payment and late declaration penalties** — Late payment of contributions: 2% per month (or fraction); late declaration of personnel information: 1% per month (or fraction), plus legal default interest (Loi n°015-2006/AN).  _(Loi n°015-2006/AN)_

## Section 5 -- Prohibitions

- **Prohibition — ceiling exceedance** — NEVER apply contributions above the 800,000 FCFA/month ceiling.  _(Arrêté n°2022-067)_
- **Prohibition — employee charged for employer-only branches** — NEVER charge the employee for family or occupational-risk branches (employer-only).  _(Décret n°2023-0129)_
- **Prohibition — conflating CNSS with AMU** — NEVER conflate CNSS with the separate AMU universal-health scheme.  _(Décret 2024-0345)_
- **Prohibition: engine computing numbers** — NEVER compute numbers — the engine handles arithmetic.
- **Verification requirement** — Confirm rates, ceiling and deadlines against current CNSS sources before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
