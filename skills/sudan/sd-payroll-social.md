---
name: sd-payroll-social
description: >
  Prepare Sudan employer payroll workpapers for 2026 intake while separating verified source wording from unresolved current payroll operation. Covers employee data, taxable remuneration links, social contribution guidance, contradictory health insurance bases, employment leave and termination evidence. Match Sudan payroll, PAYE, social insurance, NSIF, health insurance, maternity, sick pay and severance questions. The official ministry describes contribution splits but the full current 2016 statute and implementing limits were not obtained. The opened Labour Act supplies a historical employment baseline, with later law interactions still held. Use the two calculations to expose the effect of base and termination facts, and stop before net pay, filing or remittance approval.
version: 0.2
jurisdiction: SD
tax_year: 2026
last_updated: 2026-11-01
authored_by: Ahmed Hassan
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
---

# Sudan payroll and employment contribution intake v 0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Employers and workers preparing remuneration and contribution records. [Personal income tax](sd-income-tax.md) owns employment tax bands, benefit inclusion and deductions. This Guide owns the distinct contribution-base conflict and historical labour-law calculations. It does not certify that a 1997 clause or undated agency page remained operative unchanged in 2026.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| Social contribution guidance | Official ministry describes 25% of CONTRIBUTION WAGE, employer 17% and worker 8%; self-employed 25% of declared contribution income. Full current law, coverage, floors and ceilings unresolved. | [About insurance, paragraphs on2016 law/contributions](https://hrsw.gov.sd/?page_id=1360) |
| Health guidance, basic-pay page | 10% of BASIC salary, worker 4% and employer 6%, on the opened undated ministry page. | [Financing paragraph](https://hrsw.gov.sd/?page_id=482) |
| Health registration page | Same split but TOTAL wage base, conflicting with the basic-pay page. Do not approve a base or net payroll from these pages. | [registration steps](https://hrsw.gov.sd/?page_id=239) |
| Maternity historical baseline | After 6 months employment,8 weeks full pay,4+4 or 2+6 before/after, with medical and job-protection conditions. | [s.46](https://moj.gov.sd/sudanlaws/epub/EPUB/xhtml/s8zkcj.html) |
| Sickness historical baseline | After 3 months continuous service with qualifying medical evidence:3 months full,3 half,3 quarter pay; annual leave and medical-board conditions apply. | [s.47](https://moj.gov.sd/sudanlaws/epub/EPUB/xhtml/s8zkcj.html) |
| Severance historical baseline | Minimum 3 years; first 10 years 1 monthly basic/year,next 5 years 1.5,above 15 years 1.75; cap 36 months. Social-insurance/better-rights and resignation rules apply. | [ss.60–61](https://moj.gov.sd/sudanlaws/epub/EPUB/xhtml/s8zkcj.html) |

## The base

1. Obtain contracts, employment dates, attendance, basic/contribution/total remuneration, benefits, medical certificates, leave and termination reason. Do not treat those three pay bases as interchangeable.
2. Compute personal-income tax only through the dedicated [income-tax Guide](sd-income-tax.md), after its source-period and regulation gates clear. The legacy flat fringe-benefit charge and age-based exemption are not defaults.
3. Build separate social and health contribution schedules. The social ministry guidance uses contribution wage, not an automatic gross-pay base. The health pages conflict on basic versus total wage. Hold the base choice, statutory coverage, exemptions and cap/floor until the actual 2016 law and current directions are obtained.
4. The opened Labour Act s.46 maternity and s.47 sickness provisions have service, medical and other conditions. Keep full/partial-pay leave separate from tax deductions and the entitlement decision.
5. For eligible non-resignation termination under s.60, calculate each service tranche, last monthly basic pay or the specific production-worker average, and the cap. Apply s.61 resignation reductions only after the exact service/termination facts and current law interaction are resolved. A Labour Act formula is not proof that social benefits are payable in addition.
6. Obtain the actual fund registration/coverage decision, employer and worker identifiers, current payroll return and due-date directions before any final payslip, deduction or remittance approval.

## Deadlines and filing

The health-registration ministry page requests a joining letter, representative authorisation, establishment form, employee forms and latest wage statement. That is an opened procedure aid, not proof of a current filing portal. The social ministry page identifies the contribution scheme but does not establish current forms, codes or due dates. The principal Income Tax Act s.41 employer annual list is separate from monthly PAYE; payment dates are governed through regulations. Current PAYE, fund and health filing/remittance routes, contribution month, payment reference and confirmation workflow remain unconfirmed. Stop before submission and retain the eventual fund decision, employee schedules, acknowledgement and receipt.

## Penalties and interest

No current social/health late-registration fine, surcharge, minimum collection or enforcement timetable was obtained. Income-tax sanctions are distinct. Do not apply a universal payroll penalty from another law or from an undated summary.

## Cross-border points

The social ministry guidance refers to private-sector workers including foreigners with specified exclusions, but foreign-worker coverage, bilateral social agreements and expatriate pension interaction require the actual current law. The public legal library also contains older expatriate insurance law; it was acquired as a locator, not read as current coverage authority. Immigration permission and company registration do not decide contribution liability.

## Two worked examples that recompute

### Health base conflict, two outcomes

For basic pay 100,000 and total pay 140,000, the basic-pay page implies worker 4,000/employer 6,000; the total-wage page implies 5,600/8,400. Difference 4,000 overall. This is a sensitivity workpaper showing why the legal base must be settled, not a choice offered to the employer.

```oa-check
name: Health basic versus total wage conflict
inputs:
  basic: 100000
  total: 140000
steps:
  - worker_basic: basic*0.04
  - employer_basic: basic*0.06
  - worker_total: total*0.04
  - employer_total: total*0.06
  - combined_difference: worker_total+employer_total-worker_basic-employer_basic
expected:
  worker_basic: 4000
  employer_basic: 6000
  worker_total: 5600
  employer_total: 8400
  combined_difference: 4000
```

### Historical non-resignation severance

Assume an eligible12year worker, last monthly basic20,000, no resignation reduction, no better contractual right and no social-insurance offset issue. Section60 historical tranches give10months +3months =13months, or260,000, below the36month cap. A resignation or overlapping statutory benefit requires a new legal calculation.

```oa-check
name: Labour section60 twelve year tranches
inputs:
  years: 12
  monthly_basic: 20000
steps:
  - months: min(years,10)+min(max(years-10,0),5)*1.5+max(years-15,0)*1.75
  - capped_months: min(months,36)
  - amount: capped_months*monthly_basic
expected:
  months: 13
  amount: 260000
```

## Ask the client first

- Worker identity, nationality, employment status and fund registration evidence.
- Contract, actual start date, employer category and basic/contribution/total wage components.
- Tax residence and benefit/reimbursement evidence for the income-tax calculation.
- Leave balances, medical certificates, termination reason and better contractual terms.
- Current fund/health law, cap/floor, forms, due-date directions and prior payments.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| social; selected About insurance, paragraphs on 2016 law/contributions read; not a full current consolidation | https://hrsw.gov.sd/?page_id=1360 | 2026-11-01 |
| health-basic; selected Financing paragraph read; not a full current consolidation | https://hrsw.gov.sd/?page_id=482 | 2026-11-01 |
| health-total; selected registration steps read; not a full current consolidation | https://hrsw.gov.sd/?page_id=239 | 2026-11-01 |
| labour-1997; selected s.46; s.47; ss.60–61 read; not a full current consolidation | https://moj.gov.sd/sudanlaws/epub/EPUB/xhtml/s8zkcj.html | 2026-11-01 |
| income-en; selected s.41; PDF 66–67; s.62(1),(6); PDF 90–91; s.63; PDF 92 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-payroll-social.md](../../evidence/ledgers/sd-payroll-social.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Legacy-topic controls below refer to the exact original material and line-independent destination records in [the complete old-topic map](../../evidence/ledgers/sd-old-topic-map.md). Each control retains its original rules, figures, groups, procedures and exceptions for source reconciliation. Supported content is replaced above with citations; any remaining original claim under that control is explicitly unconfirmed, not a usable default.

- SD-OLD-077: Section 1 - Scope statement. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-078: Regulatory framework. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-079: Coverage. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-080: Old Age, Disability, and Survivors (pension). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-081: Contribution wage base. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-082: Sickness and Maternity. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-083: Work Injury. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-084: Employment income tax (PAYE). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-085: Employer monthly payroll obligations. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-086: NSIF contribution remittance. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-087: Old-age pension. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-088: Disability pension. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-089: Survivor pension. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-090: Death grant. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-091: Sickness benefit (employer liability). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-092: Maternity benefit (employer liability). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-093: Severance pay (unemployment, labor code 1997). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-094: Example 1 - Standard employee payroll. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-095: Example 2 - NSIF contribution with wage cap. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-096: Example 3 - Self-employed social insurance. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-097: Example 4 - Severance calculation. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-098: Employer record requirements. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-099: Registration requirements. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-100: Penalties for non-compliance. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-101: Section 8 - Audit flash points. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-102: Section 9 - Self-checks. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-103: Section 10 - Reference material. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-104: PROHIBITIONS. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.

Not yet confirmed: Full current 2016 pensions/social-insurance statute and amendments, benefit eligibility and any insured wage floor/ceiling; current health statutory base, coverage, exclusions and mandatory employer size; current monthly contribution/PAYE due dates and online routes; expatriate/diplomatic, self-employed, agricultural, domestic and informal-worker coverage. Legacy pensions 1/50 peryear,80%maximum, early-pension 20 years, invalidity 1/50 with 15 yearminimum, injury 80%, disability/lump-sum percentages, survivor shares, funeral/severance benefit formulas and no-ceiling claims remain held. Labour 1997 amendment/2016 interaction, resignation percentages, maternity/sickness currentness and resignation/retirement/death treatment need completion. No final net-pay approval follows from this draft. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.

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
