---
name: bh-payroll-social
description: "Bahrain private-sector payroll screening for 2026, including sourced employee pension/unemployment components, work-injury base rate, wage cap, EOSB and payment penalties. Holds employer pension phase-in implementation and the new October 2026 minimum-base amount pending source confirmation."
jurisdiction: BH
tax_year: 2026
last_updated: 2026-11-01
version: 0.3
category: payroll
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Payroll and Social Insurance v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Private-sector employment covered by Social Insurance Law arts. 2 to 4. Establish coverage and nationality before calculating. Government, excluded occupations and GCC extension cases need their applicable regime. The end-of-service scheme covers non-Bahraini private-sector workers insured for employment injury, excludes protected GCC-extension workers and Social Insurance Law art. 3 categories, and applies from 1 March 2024 (Decision 109/2023, enactment art. 4 and Regulation arts. 1 to 3).

## Rates, bands and thresholds

| Item | Amount and condition | Year | Official source |
|---|---|---|---|
| Employee pension share, Social Insurance art. 33 as amended by Law 14/2022 | 7% for covered pension-insured employees; do not apply to a person outside that branch | 2026 | https://www.lloc.gov.bh/Legislation/HTM/K1422 |
| Unemployment employee share, art. 6 | 1% of insured wage for covered workers under arts. 1 to 2, including covered foreign workers; this is not work-injury insurance | 2026 | https://www.lloc.gov.bh/FullAr/L7806.docx |
| Work-injury employer share, Social Insurance arts. 47 to 49 | Base rate 3%, employer alone; authorised reductions and safety-related increases require the relevant decision | 2026 | https://www.lloc.gov.bh/FullAr/L2476.docx |
| Insurable wage ceiling, art. 17 | BHD 4,000 monthly for contributions under the Social Insurance Law; do not import it into EOSB wage definition | 2026 | same |
| EOSB, Regulation art. 5 | Employer alone: 4.2% of defined wage for first three years with that employer, 8.4% thereafter | From 1 March 2024, including 2026 | https://www.lloc.gov.bh/Legislation/HTM/RCAB10923 |
| EOSB transition, art. 13 | Service already exceeding three years before commencement: 8.4% from commencement | 2026 | same |
| Monthly payment, Social Insurance arts. 27 and 31 | Within first fifteen days of following month | 2026 | https://www.lloc.gov.bh/FullAr/L2476.docx |
| Late payment, art. 31 | 5% of contribution due per month or part, payable on written demand under the article | 2026 | same |
| Failure to insure/use real wage, art. 29 | Additional 20% of unpaid contributions or applicable end-of-service amount, payable on written demand | 2026 | same |

## The base

Social Insurance art. 17 starts with total monthly wages and its statutory ceiling. January wage can determine monthly contributions through the year; for later entrants use entry-month wage through December. Articles 18 to 26 cover daily/piece/hourly workers, minimum base, concurrent employers, interrupted pay, secondment, joining/leaving months and rounding. Do not calculate from bank net pay. Article 28 makes the employer responsible for both shares and permits deduction of the employee share when paying wages; a missed deduction cannot be recovered later.

A new art. 19 bis was added by Decree-Law 44/2026, published 8 October 2026 and effective the next day. It applies to people first satisfying registration conditions after commencement and requires a Cabinet-set minimum base for pension-covered branches. The implementing amount is held. Stop a base calculation for that group until the applicable Cabinet decision is obtained.

Unemployment art. 6 provides an employer share but expressly makes the Labour Fund bear the private-sector employers' share. Do not add it again as an employer payroll cost. The predecessor's claim that a foreign employee pays work-injury insurance and has no unemployment coverage is incorrect.

EOSB uses the contractual periodic wage plus increases and social allowance, if any (Regulation art. 1). Transfers within the same employer do not end service; secondment leaves contributions with the original employer (art. 6). Pre-commencement service remains governed by the Labour Law (art. 14). EOSB is separate from SIO pension, unemployment and work-injury contributions.

## Deadlines and filing

Establish SIO registration and the correct nationality/branch; reconcile wage and service dates to the employer record; calculate each component separately; check joining/leaving rules and the minimum-base hold; compare the calculation with the SIO assessment and remit by the statutory date above. Retain the assessment, payment reference and receipt. Exact current SIO employer e-service forms, field identifiers and WPS upload/payment steps remain held, so this Guide does not authorise an unattended payroll submission.

## Penalties and interest

Use the contribution penalties in the table with their written-demand conditions. EOSB Regulation art. 5 applies Social Insurance arts. 29 and 31 to payment, and art. 12 refers offences to arts. 148 and 149. No criminal fine amount is computed here.

## Cross-border points

GCC protected workers are excluded from this EOSB scheme (Regulation art. 3). Obtain the home-state certificate, rate and extension assessment before computing. Do not substitute Bahraini rates or infer foreign tax outcomes from Bahrain's personal-tax position.

## Two worked examples that recompute

An eligible non-GCC employee in their second year has defined EOSB wage BHD 900. Employer EOSB is BHD 37.80, separate from the other payroll components.
```oa-check
name: EOSB eligible second year
inputs:
  eosb_wage: 900
steps:
  - employer_eosb: eosb_wage * 0.042
expected:
  employer_eosb: 37.8
```

Decision: can the second-year EOSB rate be kept after this worker passes three years? No. Compare the two monthly contributions on the same defined wage: the contribution rises by BHD 37.80. This is a rate-selection check, not advice to replace an employee.
```oa-check
name: EOSB service boundary comparison
inputs:
  eosb_wage: 900
steps:
  - first_period: eosb_wage * 0.042
  - later_period: eosb_wage * 0.084
  - increase: later_period - first_period
expected:
  first_period: 37.8
  later_period: 75.6
  increase: 37.8
```

## Ask the client first

- Nationality, sector, covered branches and any GCC extension certificate?
- First registration date, employment start/end dates and payroll month?
- Gross and insured wage, January/entry wage, contractual increases and social allowance?
- Any minimum-base, work-injury reduction/increase or other SIO decision?
- Any transfer, secondment, pre-commencement service or missed deduction?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Social Insurance Law, current Arabic consolidation, arts. 1 to 4, 17 to 33 and 47 to 49 read; do not use old archived English rates | https://www.lloc.gov.bh/FullAr/L2476.docx | 2026-11-01 |
| Law 14/2022, whole amendment incl. phase-in art. 4 and commencement art. 12 read | https://www.lloc.gov.bh/Legislation/HTM/K1422 | 2026-11-01 |
| Decree-Law 44/2026, whole enactment, including first-registration restriction and commencement read | https://www.lloc.gov.bh/Legislation/HTM/L4426 | 2026-11-01 |
| Unemployment Law, consolidated Arabic arts. 1 to 6 and 8(E) read | https://www.lloc.gov.bh/FullAr/L7806.docx | 2026-11-01 |
| Decision 109/2023 and whole attached Regulation arts. 1 to 15 read | https://www.lloc.gov.bh/Legislation/HTM/RCAB10923 | 2026-11-01 |

Not yet confirmed: exact 2026 employer pension phase-in implementation (therefore the inherited combined 18% employer rate is not executable); the former 17%/21% schedule; Cabinet amount for new art. 19 bis; other minimum wage/floor; current SIO online forms and WPS Resolution 68/2019 or enhanced 2026 procedure. Employee 7% pension plus 1% unemployment, employer base work injury 3%, and BHD 4,000 Social Insurance wage cap now have primary support; they are not blanket totals for every worker. Full predecessor text and exact destinations are preserved in [the country evidence](../../evidence/ledgers/bahrain-20261101/README.md). These are NON-OPERATIVE holds, never defaults or authority to compute.

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
