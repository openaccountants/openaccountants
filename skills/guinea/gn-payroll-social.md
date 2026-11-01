---
name: gn-payroll-social
description: "Guinea CNSS contribution working method for ordinary employees covered by the general social-security regime in 2026. Use it to identify registration evidence, assemble contributory remuneration, apply the monthly floor and ceiling published by CNSS, calculate employer and employee contributions, and reconcile the declaration and payment file. It distinguishes combined branch funding from employer-only costs and separates CNSS from salary income tax. The sources conflict on the remittance deadline: this Guide reports both and uses the earlier published agency date as an operational control without asserting that the decree changed. Special-category bases, partial months, multi-employer allocation and disputed assessments require separate review. Current salary-tax bands and complete payroll compliance remain unresolved."
jurisdiction: GN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
version: 1.1
---

# Guinea payroll and social contributions v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use for an ordinary employee working in Guinea under the Labour Code and the CNSS general regime, for a full monthly contribution period and a single employer. Article 4 of Law L/94/006/CTRN covers Labour Code workers regardless of nationality, contract form or remuneration, and specified non-permanent public employees outside civil-service status. It treats apprentices and other assimilated categories through special implementing rules. Do not apply the ordinary employee calculation to every trainee, permanent civil servant, self-employed person or specially assessed worker. [Social Security Code art. 4](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf).

This job produces the CNSS contribution workpaper, registration checklist and declaration/payment reconciliation. It does not calculate salary income tax, employer salary taxes, benefits entitlements or a complete net payslip. The historical salary-tax withholding topic remains an explicit hold: no progressive band or income-tax remittance date is supplied from the old Guide.

## Rates, bands and thresholds

The numeric parameters below are the current CNSS agency publication opened on 1 November 2026. The Code delegates rates and ceiling adjustments to implementing instruments; the instrument that introduced these published figures has not been obtained. Keep that source limitation with the workpaper. [Code arts. 32-34](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf).

| Ordinary monthly CNSS parameter | Published value and condition | Official source |
|---|---|---|
| Contribution floor | GNF 550,000 per employee month | [CNSS, assiette](https://cnss.gov.gn/cotisations-sociales-employeurs/) |
| Contribution ceiling | GNF 2,500,000 per employee month | [CNSS, assiette](https://cnss.gov.gn/cotisations-sociales-employeurs/) |
| Employer total | 18% of contributory remuneration after the floor/ceiling control | [CNSS, taux](https://cnss.gov.gn/cotisations-sociales-employeurs/) |
| Employee total | 5% of the same base | [CNSS, taux](https://cnss.gov.gn/cotisations-sociales-employeurs/) |
| Combined contribution | 23% of the same base | [CNSS, taux](https://cnss.gov.gn/cotisations-sociales-employeurs/) |
| Family-benefit branch | 6%, wholly employer funded | [CNSS, branches](https://cnss.gov.gn/cotisations-sociales-employeurs/); [Code art. 34](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf) |
| Occupational accident/disease branch | 4%, wholly employer funded; the Code permits an employer-specific risk-rate increase for prevention non-compliance | [CNSS, branches](https://cnss.gov.gn/cotisations-sociales-employeurs/); [Code arts. 33-34](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf) |
| Sickness branch | 6.5% combined funding, not an employer-only rate | [CNSS, branches](https://cnss.gov.gn/cotisations-sociales-employeurs/) |
| Old age, invalidity and death branch | 6.5% combined funding | [CNSS, branches](https://cnss.gov.gn/cotisations-sociales-employeurs/) |

Do not deduct the employer contribution from wages. Code article 34 reserves family and occupational-risk contributions to the employer, shares sickness and pension contributions under implementing rules, and limits the worker share to half the relevant branch contribution. The current page publishes total employer/worker shares but not each party's pension/sickness allocation. Do not use the historical 2.5% worker pension and 4% employer pension assertions as verified allocations. [Code art. 34](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf).

## The base

1. Confirm employee/regime coverage and obtain the employer CNSS number, employee's existing social-security number, contract, monthly payroll and attendance. The employee keeps the same number when changing employer. Apply the special-case stop below before using an ordinary full-month floor or cap. [Code art. 4](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf); [decree arts. 2-5](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf).
2. Assemble remuneration before employee contribution deduction: salary, commissions, bonuses, gratifications, overtime, relevant allowances and the taxable value of benefits in kind. The Code includes cash and in-kind advantages and excludes representative expense reimbursements and statutory family benefits; in-kind valuation follows tax rules. Obtain a separately supported in-kind valuation rather than assume cash cost is the statutory amount. [Code art. 32](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf).
3. Classify each exclusion from evidence. Decree article 36 specifically lists exclusions including foreign-paid expatriation allowances, work-accident/disease daily benefits, reimbursable maternity advances, family allowances, travel/displacement allowances, dirt/insalubrious-work premiums, medical reimbursements, dismissal indemnity beyond notice pay, and genuine expense reimbursements. Notice-pay and paid-leave compensation are included. A pay label alone does not prove a reimbursement. Irregular payments are added to the simultaneous payroll or the next payroll if paid between payrolls. [Decree art. 36](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf).
4. For an ordinary full-month, single-employer case within this scope, set the monthly base to `min(max(contributory_remuneration, 550000), 2500000)` using the published CNSS parameters. Calculate worker contribution as base × 5%, employer contribution as base × 18%, and CNSS payable as their sum. Apply the cap to each employee, not to the company's aggregate wage bill. [CNSS calculation and assiette](https://cnss.gov.gn/cotisations-sociales-employeurs/); [Code art. 32](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf).
5. Keep gross remuneration, excluded reimbursements, base before/after floor and cap, worker share, employer share and total payable in separate fields. Reconcile worker shares to payroll deductions and employer shares to employer expense. The employer pays both to CNSS and remains responsible for the whole payment; worker withholding is not proof CNSS received it. [Code art. 34](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf); [CNSS, débiteur](https://cnss.gov.gn/cotisations-sociales-employeurs/).
6. Stop for a partial month, several employers, an apprentice/special wage class, disputed in-kind valuation, a risk-rate increase or a posting exemption. Code article 34 apportions multi-employer contributions in proportion to pay; it does not itself supply all floor/cap allocation mechanics. Do not give each employer an independent full floor/cap without resolving that allocation. [Code arts. 4,32-34](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf).

Contributions attach to months with effective work, paid leave or an equivalent period with remuneration due. An employee cap does not by itself authorise treating a paid-leave month as a nil month. [Decree art. 35](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf).

## Deadlines and filing

Register the employer within eight days of opening/acquiring the enterprise or first hiring, using the earlier applicable trigger in decree article 5. CNSS's current registration page describes eight days from employing workers and also instructs employee registration within eight days after hire. Obtain the signed employer request, statutes or RCCM, signed payroll, worker identity/birth evidence, and the assigned registration notices; an APIP incorporation record alone is not proof each worker is registered. [Decree arts. 3-5](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf); [CNSS registration](https://cnss.gov.gn/immatriculation/).

Twenty or more employees triggers monthly payment. Below twenty, the decree provides quarterly payment and the current agency page also allows monthly payment at the employer's request. Keep the confirmed employer frequency and headcount evidence. [Decree arts. 38,40](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf); [CNSS periodicity](https://cnss.gov.gn/cotisations-sociales-employeurs/).

**Unresolved deadline conflict:** decree D/94/089 articles 37-40 provides the first twenty days of the following month or quarter. Both current CNSS contribution and collection pages instead instruct the first fifteen days. No amending instrument resolving this difference was found. Use the published fifteen-day window as this workflow's earlier operational submission/payment control; this does not assert that the decree was amended or that payment on days 16-20 is legally late. Obtain the governing instrument or CNSS's written position before advising on a disputed deadline or sanction. [Decree arts. 37-41](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf); [CNSS published due date](https://cnss.gov.gn/cotisations-sociales-employeurs/); [CNSS collection](https://cnss.gov.gn/recouvrement/).

Prepare the quarterly nominative declaration for every employed quarter, including employer identity/number, quarter, each employee's identity/number, total and capped pay, employment dates, duration, contributions, payments already made and remaining balance, headcount, payment references, date and signature. A nil-employed quarter still requires a declaration under article 37. At least twenty employees also requires aggregate monthly salary declarations for the first two months of each quarter under article 38. The decree rounds the quarterly contribution total up to the next franc and the monthly aggregate declaration contribution up to the next ten francs. Reconcile this declaration rounding to the underlying exact employee computation. [Decree arts. 37-38](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf).

Correct earlier periods through a supplementary declaration for each affected quarter. Article 40 specifies payment within fifteen days after drawing up the corresponding supplementary declarations. For a bank/postal transfer it requires a copy of the transfer order with the salary declaration. Retain the filed declaration, acknowledgement, transfer evidence and CNSS allocation/receipt; do not equate a draft or a bank order with credited payment. Current e-CNSS screen/field instructions and authenticated submission were not inspected. [Decree arts. 39-40](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf).

## Penalties and interest

Code article 35 specifies a 5% monthly late-payment surcharge and allows a remission/reduction request for force majeure or proven good faith. Decree article 41 starts the surcharge on the twenty-first day, while current CNSS guidance describes 5% per month or fraction after its fifteen-day deadline. Keep the amount/date in dispute unresolved until the deadline conflict and fraction-of-month treatment are settled; do not generate a live surcharge for days 16-20 from this Guide. [Code art. 35](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf); [decree art. 41](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf); [CNSS penalties](https://cnss.gov.gn/cotisations-sociales-employeurs/).

Decree article 37 sets a late quarterly declaration penalty of GNF 1,000 per worker, capped at GNF 100,000 per reference period, and GNF 1,000 for each fraudulent wage inaccuracy or employee omission. Do not transfer that cap to the separate inaccuracy/omission provision without legal support. For an assessment, obtain the notice, period, headcount, facts and governing text before computing a sanction. [Decree art. 37](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf).

## Cross-border points

Nationality alone does not exclude a Labour Code worker in Guinea. Code article 4 permits a foreign-enterprise posting to remain under the worker's normal foreign system with CNSS agreement if the expected assignment does not exceed six months. An unforeseen extension can obtain a further period up to six months with CNSS agreement. This is conditional approval, not an automatic foreign-worker exemption or evidence of a bilateral treaty. Obtain both the posting facts and CNSS agreement before omitting contributions; refer longer postings, treaties and special cases for separate review. [Code art. 4](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf).

## Two worked examples that recompute

An ordinary full-month employee has GNF 1,800,000 of validated contributory remuneration, no special risk assessment and no special-category rule. The base is inside the published floor and ceiling. Worker contribution is GNF 90,000, employer contribution GNF 324,000 and CNSS payable GNF 414,000. Salary income tax is not included.

```oa-check
name: Ordinary full-month employee below ceiling
inputs:
  contributory_pay: 1800000
  monthly_floor: 550000
  monthly_ceiling: 2500000
steps:
  - base: min(max(contributory_pay, monthly_floor), monthly_ceiling)
  - employee: base * 0.05
  - employer: base * 0.18
  - payable: employee + employer
expected:
  base: 1800000
  employee: 90000
  employer: 324000
  payable: 414000
```

The second case is a classification decision, not an election to relabel pay. An employee has GNF 2,400,000 of contributory remuneration and a further GNF 400,000 payment. If documents prove reimbursement of genuine professional expenses, the extra amount is excluded: base GNF 2,400,000 and CNSS total GNF 552,000. If it is a cash bonus, include it before the cap: base GNF 2,500,000 and total GNF 575,000. The contribution difference is GNF 23,000, split GNF 5,000 worker and GNF 18,000 employer. The cap shelters only the excess contribution base; it does not turn a bonus into a reimbursement.

```oa-check
name: Evidenced reimbursement versus cash bonus at the ceiling
inputs:
  regular_contributory_pay: 2400000
  additional_payment: 400000
  monthly_floor: 550000
  monthly_ceiling: 2500000
steps:
  - reimbursement_base: min(max(regular_contributory_pay, monthly_floor), monthly_ceiling)
  - bonus_base: min(max(regular_contributory_pay + additional_payment, monthly_floor), monthly_ceiling)
  - reimbursement_employee: reimbursement_base * 0.05
  - reimbursement_employer: reimbursement_base * 0.18
  - bonus_employee: bonus_base * 0.05
  - bonus_employer: bonus_base * 0.18
  - reimbursement_total: reimbursement_employee + reimbursement_employer
  - bonus_total: bonus_employee + bonus_employer
  - extra_employee: bonus_employee - reimbursement_employee
  - extra_employer: bonus_employer - reimbursement_employer
  - extra_total: bonus_total - reimbursement_total
expected:
  reimbursement_base: 2400000
  bonus_base: 2500000
  reimbursement_total: 552000
  bonus_total: 575000
  extra_employee: 5000
  extra_employer: 18000
  extra_total: 23000
```

## Ask the client first

- Which regime covers each worker, and is there a CNSS-approved foreign posting, apprenticeship, special assessment or risk-rate increase?
- What are the employer/worker registration numbers, hire dates, other employers and paid/unpaid periods?
- What salary, bonuses, in-kind benefits, termination items and substantiated expense reimbursements were paid, and when?
- What headcount, confirmed CNSS frequency, declarations, receipts and notices apply to the period?
- Is there a deadline, penalty, base allocation or in-kind valuation dispute requiring the governing instrument?
- Is the requested output CNSS only, or does it also need salary-tax withholding and employer taxes that this Guide does not yet compute?

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [CNSS-hosted Social Security Code, Law L/94/006/CTRN](https://cnss.gov.gn/wp-content/uploads/2023/08/CODE-CNSS-GUINEE-1994.pdf), arts. 1-5, 32-39, including coverage, contribution base, implementing powers, liability and sanctions. The reproduction itself refers readers to JO no. 5 of 10 March 1994. | 2026-11-01 |
| [CNSS-hosted decree D/94/089 of 11 October 1994](https://cnss.gov.gn/wp-content/uploads/2023/08/Texte-Reglementaire-CNSS-1994-securite-sociale-partie-regelementaire.pdf), arts. 1-6 and 35-43 with neighbouring clauses: registration, remuneration, declarations, payment and dispute steps. | 2026-11-01 |
| [CNSS current employer contribution page](https://cnss.gov.gn/cotisations-sociales-employeurs/), full contribution/base, funding, debtor, frequency, due-date and surcharge sections, read through an ordinary browser after direct HTTP 403. | 2026-11-01 |
| [CNSS current collection page](https://cnss.gov.gn/recouvrement/), full contribution/payment and registration sections, including fifteen-day instruction, read through an ordinary browser after direct HTTP 403. | 2026-11-01 |
| [CNSS current registration page](https://cnss.gov.gn/immatriculation/), employer/worker requirements and general-regime scope, read through an ordinary browser after direct HTTP 403. | 2026-11-01 |

Not yet confirmed: implementing instruments establishing the currently published floor, cap and rates; reconciliation of the decree's twenty-day window with current fifteen-day guidance and surcharge fraction/start-date treatment; separate employee/employer sickness and pension allocations; partial-month and multi-employer floor/cap mechanics; special worker categories and increased occupational-risk rates; current tax valuation of in-kind benefits; authenticated e-CNSS form/screens/receipts; current salary income-tax withholding, employer salary/apprenticeship taxes and their remittance rules. This Guide does not establish complete payroll or whole-country coverage.

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
