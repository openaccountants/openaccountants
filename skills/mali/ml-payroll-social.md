---
name: ml-payroll-social
description: >
  Mali payroll and social-contribution research draft for 2026, using older DGI provisions, the 2010 AMO decrees and undated government guidance without certifying their complete current amendment chain. Use it to build conditional employer workpapers for branch-by-branch INPS contributions, private-sector AMO, contribution bases, headcount-dependent payment calendars, employer payroll taxes and wage-withholding controls. It distinguishes the housing tax, professional-training tax, youth-employment tax and ANPE levy, which the former Guide mixed together. It links the wage-income Guide for ITS bands rather than copying them. Two executable examples test contribution splits and the payment-calendar decision. Current legal continuity, wage floors, risk classification, declaration forms and portal procedures remain held for verification.
jurisdiction: ML
category: international
tax_year: 2026
tax_year_notes: "2026 research draft only; older DGI source baseline, operative 2026 amendment chain unproved."
version: 0.1
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mali payroll and social contributions source-reference draft v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research draft; operative 2026 law is unproved.** This is a conditional source-reference workpaper, not an approved current-law computation. The DGI online consolidation contains amendments labelled through 2017 in the provisions used here. No complete later amendment chain or enacted 2026 fiscal Annex U has been reconciled. Read every rule below as a statement of that identified source baseline, not proof it applies unchanged in 2025 or 2026. Do not calculate a client's 2026 liability or instruct a 2026 filing from this draft. The current-year metadata identifies the research job; it is not evidence of currentness or a technical retrieval/publication safeguard.

## Who this applies to

This conditional baseline concerns an ordinary private-sector employer and permanent salaried staff. Identify the contribution branch, worker category, employer registration and notified occupational-risk class first. The government's RSU INPS page describes employer registration at opening and worker registration on hiring, with a notified employer number/rates and employee hiring forms. Its undated content is not a 2026 legal consolidation. Occasional labour, household staff, voluntary/self-employed schemes and public servants need separate rules. [RSU, INPS registration and contributions sections](https://rsu.gouv.ml/portail/partenaires/inps/).

The 2010 rate decree distinguishes private employers from the state/local authorities, pensioners and voluntary insured people. Its private-sector AMO rate already incorporates the former INPS disease-protection contribution; do not add the superseded disease branch again. [Décret 10-578 arts. 2–7](https://www.canam.ml/media/attachments/2022/02/07/dcret-n-10-578-taux-de-cotisations.pdf#page=2).

## Rates, bands and thresholds

These are source-reference figures with the source ages stated, not approved operative 2026 payroll rates.

| Item | Older statutory or undated authority baseline | Official source |
|---|---|---|
| INPS family benefits | Employer 8% | [RSU INPS, branch-rate table](https://rsu.gouv.ml/portail/partenaires/inps/) |
| INPS old-age | Employer 3.4%, employee 3.6% | [RSU INPS, branch-rate table](https://rsu.gouv.ml/portail/partenaires/inps/) |
| INPS invalidity/death | Employer 2% | [RSU INPS, branch-rate table](https://rsu.gouv.ml/portail/partenaires/inps/) |
| Occupational injury/disease | Employer 1%–4%; use notified class, not an arbitrary midpoint | [RSU INPS, branch-rate table and classification text](https://rsu.gouv.ml/portail/partenaires/inps/) |
| AMO active employee | 3.06% | [Décret 10-578 art. 3](https://www.canam.ml/media/attachments/2022/02/07/dcret-n-10-578-taux-de-cotisations.pdf#page=2) |
| AMO private employer | 3.50%, including the former 2% INPS disease branch | [Décret 10-578 art. 5](https://www.canam.ml/media/attachments/2022/02/07/dcret-n-10-578-taux-de-cotisations.pdf#page=2) |
| CFE | Individuals/companies liable to IS, IBIC or agricultural-profit tax under art.159: employer 3.5% of gross remuneration including actual benefits, base rounded down to XOF 1,000; statutory employee exemptions require separate proof | [CGI arts. 159–163](https://www.dgi.gouv.ml/CGI/) |
| Professional training tax | 2% for the IS/IBIC/agricultural-profit persons in art. 183; gross remuneration including actual benefits, base rounded down to XOF 1,000 | [CGI arts. 183–185](https://www.dgi.gouv.ml/CGI/) |
| Youth-employment tax, TEJ | 2% for the profit-tax/CFE employers in art. 185-A; gross remuneration including actual benefits, base rounded down to XOF 1,000 | [CGI arts. 185-A–185-D, Loi 2008-020](https://www.dgi.gouv.ml/CGI/) |
| Housing tax | 1% of gross payroll for public/private employers, monthly; distinct from CFE/training | [DGI appendix, Loi 85-35 art. 2 and Décret 183/PG-RM art. 14](https://www.dgi.gouv.ml/CGI/) |
| ANPE levy | Authority page describes 1% employer levy, separately from social-insurance branches; statutory enactment/amendment chain not obtained | [RSU INPS, contribution obligations](https://rsu.gouv.ml/portail/partenaires/inps/) |
| Contribution ceiling | RSU INPS page says no salary ceiling; this is an undated authority statement, not verified 2026 law | [RSU INPS, contribution base](https://rsu.gouv.ml/portail/partenaires/inps/) |

## The base

1. Reconcile payroll and identify basic pay, taxable premiums/allowances, benefits, actual expense reimbursements and family benefits separately. For AMO, the 2010 collection decree includes basic salary and taxable premiums/allowances, excluding professional expenses, reimbursement allowances and family benefits. It sets a SMIG floor and annual regularisation for fluctuating pay, but this draft supplies no current SMIG figure. Do not use the RSU page's visibly old wage-floor figure as a 2026 floor. [Décret 10-601 arts. 5–8](https://www.canam.ml/media/attachments/2022/03/17/decret-601.pdf#page=2).
2. For the INPS branches, the authority page describes all remuneration including benefits and allowances except reimbursements, with no ceiling. It also calls for the notified accident-risk rate. Do not assume every branch has the same exemption merely because the payroll amounts coincide in a simple case. The complete social-code amendment chain remains unproved. [RSU INPS, base and rate sections](https://rsu.gouv.ml/portail/partenaires/inps/).
3. Calculate each employer and employee branch on its supported base. Retain employee deductions separately from the employer cost. The AMO employer contribution remains exclusively the employer's charge and cannot be shifted by agreement. The employer must remit the withheld contributions; withholding from the payslip alone does not settle the fund liability. [Décret 10-601 arts. 28–30](https://www.canam.ml/media/attachments/2022/03/17/decret-601.pdf#page=6).
4. Calculate applicable CFE, training, TEJ, housing and ANPE amounts separately, with a tax-specific base/rounding and evidenced exclusions. The former 3.5% housing/training combination is not a valid single charge. Do not present a universal all-in employer rate, especially for exempt staff or different worker categories. [CGI arts. 159–163, 183–185-D and housing appendix](https://www.dgi.gouv.ml/CGI/); [RSU INPS](https://rsu.gouv.ml/portail/partenaires/inps/).
5. Use [wage income tax](ml-income-tax.md) for the distinct ITS annual grid, residence, deductions and family relief. Its annual examples do not establish the monthly payroll conversion method. Keep taxable wage, contribution wage and employer-tax base reconciliations distinct. [CGI arts. 5–11, 160, 184, 185-B; LPF arts. 410–418](https://www.dgi.gouv.ml/CGI/).

## Deadlines and filing

**AMO 2010 source calendar.** Article 14 requires payment within the fifteen days after the expired month for employers of at least ten staff, and after the expired quarter for employers below ten. It requires a payment quittance; its continuation on the next page allows a ministerial order to change the calendar. Articles 15–17 require a nominative declaration and the delegated manager's CANAM-approved model. Send the declaration even if contributions cannot be paid. [Décret 10-601 arts. 13–17, 21](https://www.canam.ml/media/attachments/2022/03/17/decret-601.pdf#page=3).

**INPS authority calendar.** The RSU page describes the same ten-worker split for monthly versus quarterly contribution declarations/payments and a quarterly nominative wage schedule. It describes employer registration, hiring bulletins and a contribution recap. These operational descriptions need current confirmation; they are not proof that no later order changed the calendar. [RSU INPS, registration and declaration/payment obligations](https://rsu.gouv.ml/portail/partenaires/inps/).

**Tax source calendar.** ITS is withheld at payment and normally declared/remitted by the next month's fifteenth, with the next working day if that is non-working. The source has a separate quarterly exception when monthly retention does not exceed XOF 5,000, which ends when the threshold is exceeded. CFE has its own declaration/payment rules and small-amount exception. Do not import one tax's exception into every contribution. [LPF arts. 93–98, 297–302, 410–418](https://www.dgi.gouv.ml/CGI/).

Employers' annual wage summary is due in January; payroll records must show payment/withholding details and be retained through the third following year. Employees receive the prior month's gross-pay/withholding information and an annual statement in February. [LPF arts. 29, 31–32](https://www.dgi.gouv.ml/CGI/).

Prepare branch and tax schedules, nominative records, registration/risk evidence and the separate payment calendar. Obtain each actual prescribed form and current filing route, map supported totals to its fields, then retain the filed declaration, acknowledgement and fund/tax receipt. Current form identifiers, boxes, authenticated filing/payment/confirmation steps and later calendar orders have not been inspected. No 2026 filing is authorised by this source workpaper.

## Penalties and interest

For AMO, the 2010 decree separately addresses missing wage reports, inaccurate reporting, late contributions and withheld amounts not paid over. Article 26 provides 2% per month for late/incomplete contributions and expressly permits later ministerial revision; article 27 provides notice before recovery. Further penalties and possible interaction with the AMO law remain unresolved, so do not aggregate them or transplant them to all INPS branches. [Décret 10-601 arts. 20–30](https://www.canam.ml/media/attachments/2022/03/17/decret-601.pdf#page=5).

The older tax LPF provides a fine equal to unwithheld ITS under article 419; article 420 addresses understated remittances, while article 421 charges 2% per month on late ITS, capped at 20%, counting a started month as full under its stated sixteenth-to-fifteenth convention. Articles 36–39 address declaration/information failures separately. CFE article 98 and late-payment article 302 are different sanctions. Their complete current amendment chain and cumulation are not verified. [LPF arts. 36–39, 98, 302, 419–421](https://www.dgi.gouv.ml/CGI/).

## Cross-border points

Determine domestic payroll registration, the wage-income source/residence result and any valid social-security convention before assuming an expatriate is excluded. The older LPF expressly requires self-payment of taxable wages by Mali-domiciled recipients where the employer is abroad. This draft provides no treaty contribution exemption, foreign-certificate procedure or universal expatriate rate. [LPF arts. 34, 411–412](https://www.dgi.gouv.ml/CGI/); [Décret 10-578 art. 2](https://www.canam.ml/media/attachments/2022/02/07/dcret-n-10-578-taux-de-cotisations.pdf#page=2).

## Two worked examples that recompute

Both cases test the identified older/undated sources only. Assume an employer within art.159 IS/IBIC/agricultural-profit scope and the stated other employer-tax scopes, ordinary permanent private staff, confirmed bases above the applicable wage floor, no exemptions, and no later amendments. They do not determine client 2026 payroll.

**Separate employee deductions and employer cost.** For XOF 1 million cash payroll, assume each branch base equals that amount and a notified accident rate of 2%. Employee old-age plus AMO is XOF 66,600. Employer INPS plus AMO is XOF 189,000. CFE, training, TEJ, housing and authority-described ANPE total XOF 95,000. Total employer charge is XOF 284,000 and cost including gross salary XOF 1,284,000. ITS is excluded because its employee facts and monthly algorithm have not been provided. ANPE is shown once, outside the insurance subtotal.

```oa-check
name: Older Mali payroll source test, split the charges
inputs:
  payroll: 1000000
steps:
  employee_pension: payroll * 0.036
  employee_amo: payroll * 0.0306
  employee_social: employee_pension + employee_amo
  employer_inps: payroll * (0.08 + 0.034 + 0.02 + 0.02)
  employer_amo: payroll * 0.035
  employer_social: employer_inps + employer_amo
  cfe: floor(payroll / 1000) * 1000 * 0.035
  training: floor(payroll / 1000) * 1000 * 0.02
  youth: floor(payroll / 1000) * 1000 * 0.02
  housing: payroll * 0.01
  anpe: payroll * 0.01
  fiscal_charges: cfe + training + youth + housing + anpe
  employer_charges: employer_social + fiscal_charges
  employer_cost: payroll + employer_charges
expected:
  employee_social: 66600
  employer_social: 189000
  fiscal_charges: 95000
  employer_charges: 284000
  employer_cost: 1284000
```

**Monthly or quarterly AMO payment?** Keep total eligible monthly payroll XOF 2 million constant. With nine employees the source calendar calls for quarterly payment; with ten it calls for monthly payment. Combined employee/employer AMO is XOF 131,200 per month and XOF 393,600 per quarter in either case. The headcount decision changes due-date cash flow, not the amount for the same base. Use actual per-employee records and the source calendar only after currentness verification.

```oa-check
name: AMO 2010 source calendar decision, nine or ten workers
inputs:
  monthly_payroll: 2000000
steps:
  monthly_contribution: monthly_payroll * (0.0306 + 0.035)
  nine_workers_quarterly_payment: monthly_contribution * 3
  ten_workers_monthly_payment: monthly_contribution
  ten_workers_quarter_total: ten_workers_monthly_payment * 3
  quarter_difference: nine_workers_quarterly_payment - ten_workers_quarter_total
expected:
  monthly_contribution: 131200
  nine_workers_quarterly_payment: 393600
  ten_workers_monthly_payment: 131200
  quarter_difference: 0
```

## Ask the client first

- What period, employer category, headcount and permanent/occasional/household staff classifications apply?
- What employer/employee registrations, accident-risk notification and any exemption certificates exist?
- What payroll, benefits, reimbursements, family benefits and retroactive changes support each base?
- Which amounts were withheld, declared and paid, with what acknowledgements or notices?
- Are any employees cross-border, seconded or paid from abroad, and what convention documents support treatment?
- Have the current source chain, wage floor, actual forms and authorised payment calendar been obtained?

## Sources

| Source and actual scope | URL | Read on |
|---|---|---|
| DGI, CGI and LPF online consolidation; exact articles cited above and their neighbouring provisions, older amendment labels through 2017; not a 2026 consolidation | https://www.dgi.gouv.ml/CGI/ | 2026-11-01; selected chapters read offline, not the entire code |
| Décret 10-578/P-RM, 26 October 2010; complete arts. 1–8 read, page 2 rates and inclusion visually checked | https://www.canam.ml/media/attachments/2022/02/07/dcret-n-10-578-taux-de-cotisations.pdf | 2026-11-01; original 2010 decree, not a current consolidation |
| Décret 10-601/P-RM, 18 November 2010; complete arts. 1–46 read by French OCR, arts. 5–8, 13–14 and 25–30 visually checked | https://www.canam.ml/media/attachments/2022/03/17/decret-601.pdf | 2026-11-01; original 2010 decree, no later orders reconciled |
| Government RSU, INPS; complete registration, base, branch rates and declaration/payment sections read; page undated and contains an old wage-floor figure and an unrelated injected link, neither relied upon | https://rsu.gouv.ml/portail/partenaires/inps/ | 2026-11-01; authority guidance only, not proof of 2026 law |
| CANAM homepage, complete contribution accordion; ordinary browser read after direct Python TLS-chain failure, no bypass | https://www.canam.ml/ | 2026-11-01; base and private/employee rate corroboration, not the statutory amendment chain |

Not yet confirmed: operative 2026 amendments and enacted fiscal Annex U; complete INPS legislation, current contribution ceilings and wage floor; ANPE statutory chain; current exemptions, risk classification, occasional/household rules; current forms, boxes and authenticated submission/payment; later AMO calendar/penalty orders and full sanction interaction. No continuity from old instruments, complete payroll coverage or accountant attestation is claimed.

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
