---
name: pk-financial-statements
description: Use for pakistan financial statements and reporting route. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: financial-statements
type: situation-rules
---

# Pakistan financial statements and reporting route v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For Pakistan freelancers/sole proprietors, AOPs and companies in 2026. Prepare accounts and identify reporting, audit and filing obligations separately. An individual does not file SECP company accounts merely because they freelance; retain tax accounts and the applicable return/wealth statement. An AOP's tax accounts and partnership obligations differ from SECP company reporting. Company accounts require the applicable financial-reporting framework, with audit and filing tested independently. [ITO ss.114,116,174](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf); [SECP reporting FAQ](https://www.secp.gov.pk/company-formation/faqs-on-company-regulation-2024/).

## Ask the client first

Obtain legal form, company/public-interest/listed/subsidiary status, reporting period, paid-up capital, turnover, monthly employee counts, prior audited statements, classification history, applicable framework/election, audit appointment and current filing requirements. Do not use tax-law small-company status as the accounting classification.

## The method, step by step

1. For an individual freelancer, prepare supported business accounts and resident-individual wealth reconciliation for the applicable IRIS return; keep the expense/asset/bank records under `pk-bookkeeping`. Do not issue a blanket statement that no other professional/sectoral accounting law can apply. [ITO ss.114,116,174](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
2. For an AOP, prepare accounts for its own tax return and partnership requirements. Some member-share relief depends on audited financial statements where the statutory turnover condition applies; do not promise that AOPs never need audit. [ITO s.92](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
3. For a company, classify under the Companies Act Third Schedule before selecting IFRS, IFRS for SMEs or revised AFRS for SSEs. Check public-interest status and the full schedule rather than assuming all private entities use full IFRS. [Third Schedule](https://www.secp.gov.pk/document/updated-3rd-schedule-to-the-companies-act-2017-29-12-2025/?refresh=6991a886b4e621771153542&wpdmdl=63339).
4. Test audit and registrar filing separately, using the sourced boundaries below; obtain professional confirmation of any applicable notified change or special status. Audit exemption does not mean no accounts. Do not revive an unaudited-filing duty from an old checklist citing s.234: the official consolidation marks that section omitted by the 2021 amendment. [Act s.234 and footnote 51](https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422).
5. Prepare the accounts and supporting tax reconciliation; obtain required approval/authentication and audit before the relevant submission. Use the relevant SECP annual-accounts process and retain acknowledgement; tax-return completion is separate.

## Rates, bands and thresholds

| Test, with conditions | Published boundary | Official source |
|---|---|---|
| Ordinary private-company small accounting classification: all 3 criteria, subject to full schedule/public-interest rules | Paid-up capital at most PKR 10,000,000; turnover at most PKR 150,000,000; employees at most 250 | [Third Schedule SSC row](https://www.secp.gov.pk/document/updated-3rd-schedule-to-the-companies-act-2017-29-12-2025/?refresh=6991a886b4e621771153542&wpdmdl=63339) |
| Accounting classification timing | Prior year's audited statements; change after 2 consecutive years outside previous criteria; employees are monthly-average persons employed | [Third Schedule notes 1-3](https://www.secp.gov.pk/document/updated-3rd-schedule-to-the-companies-act-2017-29-12-2025/?refresh=6991a886b4e621771153542&wpdmdl=63339) |
| Audit exemption boundary described in SECP FAQ; check notified higher amount/special status | Private-company paid-up capital not exceeding PKR 1,000,000 (in words on the page) | [FAQ part 3.1, s.223](https://www.secp.gov.pk/company-formation/faqs-on-company-regulation-2024/) |
| Annual audited-account filing boundary described in SECP FAQ | Every public company and private company with paid-up capital exceeding PKR 10,000,000 (in words on the page); listed quarterly reporting separately | [FAQ part 2.8, s.233](https://www.secp.gov.pk/company-formation/faqs-on-company-regulation-2024/) |

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Solo freelancer | Tax accounts/return and resident wealth statement; no SECP company filing solely from freelance status |
| AOP/partnership | AOP tax return and agreement/other applicable law; check s.92 audited-account condition rather than assuming no audit ever |
| Private company | Full Schedule classification, audit and filing are distinct tests; no automatic full-IFRS assumption |
| Public/listed, public-interest, regulated, foreign or listed-company subsidiary | Use the specific schedule and Companies Act provisions; obtain specialist reporting/audit/filing analysis |
| Higher framework choice | The Third Schedule permits specified medium/small companies to opt for a higher framework; document the applicable option |

## Worked cases

Both cases assume an ordinary private company without an overriding public-interest/regulated/subsidiary condition. Results measure threshold distances and do not replace the complete legal classification.

```oa-check
name: Small reporting class does not itself give audit exemption
inputs:
  paid_up: 5000000
  turnover: 100000000
  employees: 100
steps:
  - capital_room: 10000000 - paid_up
  - turnover_room: 150000000 - turnover
  - employee_room: 250 - employees
  - above_published_audit_boundary: paid_up - 1000000
expected:
  capital_room: 5000000
  turnover_room: 50000000
  employee_room: 150
  above_published_audit_boundary: 4000000
```

The company fits the stated small reporting limits but exceeds the published audit-exemption capital boundary. It does not follow that audited accounts must also be filed under the private-company capital test; that is separate.

```oa-check
name: Private-company registrar filing capital threshold
inputs:
  paid_up: 12000000
  published_filing_boundary: 10000000
steps:
  - capital_above_boundary: paid_up - published_filing_boundary
expected:
  capital_above_boundary: 2000000
```

The second company exceeds the published filing boundary. Confirm the applicable accounts, audit and due date before submission.

## When to refuse or refer

Never instruct every freelancer to file SECP company statements, assume full IFRS for a small company, treat audit exemption as no accounting requirement, or apply unverified size thresholds. Refer listed/regulated/foreign/group/NPO reporting, framework transitions, special audit requirements, late filing and disputed classifications. A tax return does not replace registrar obligations.

## Filing and payment

Use the applicable SECP annual-accounts process in eZfile and retain its acknowledgement. Tax accounts accompany the applicable IRIS workflow separately. Obtain the actual statutory date, approvals and current process before filing; preserve both acknowledgements. This skill does not prescribe an unverified universal accounts-filing deadline.

## Completion checklist

Legal form established; accounting framework/classification supported; audit tested separately; registrar filing tested separately; tax reconciliation prepared; approvals/acknowledgements retained; unresolved period/status requirements visible.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for SECP Third Schedule small/medium/large/public-interest classifications and notes, including higher-framework options | https://www.secp.gov.pk/document/updated-3rd-schedule-to-the-companies-act-2017-29-12-2025/?refresh=6991a886b4e621771153542&wpdmdl=63339 | 2026-11-14 |
| Read for Companies Act ss.223(5),233(1),(3) and s.234 omission/footnote 51; separate audit and filing tests, with the omitted unaudited-filing duty distinguished from old guidance | https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422 | 2026-11-15 |
| Read for SECP FAQ parts 2.8 and 3.1, annual accounts route, separate audit and filing capital boundaries | https://www.secp.gov.pk/company-formation/faqs-on-company-regulation-2024/ | 2026-11-14 |
| Read for ITO ss.92,114,116,174, AOP/member audit condition and individual tax accounts/wealth context | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |

Not yet confirmed: taxpayer's full classification/history and notified special thresholds, detailed recognition/measurement under its selected standard, all special/group/foreign/NPO reporting rules, filing dates and current screen details. The original blanket AOP/no-audit and all-companies-file statements are replaced by separate conditional tests above.
