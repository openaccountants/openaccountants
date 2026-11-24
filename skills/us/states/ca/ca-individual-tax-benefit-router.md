---
name: ca-individual-tax-benefit-router
description: "Route California individual income tax questions about credits, deductions, exemption credits, disaster relief, penalty relief and withholding allowances for tax year 2026. Identifies the taxpayer, return, year and facts that control the route, then loads the existing California individual tax, figures, residency, estimated tax, coverage or payroll skill where one exists, or the current FTB or EDD source. Does not decide eligibility or calculate a benefit. Trigger on California tax credits, California deductions, California tax relief, California tax allowances, CalEITC, renter's credit, disaster loss deduction, penalty abatement, or DE 4 withholding allowances."
version: "0.1"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-24
category: orchestrator
type: router
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
---

# California individual tax benefits and relief router v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This is a routing skill for California personal income tax questions for tax year 2026. It does not calculate tax, decide whether a taxpayer qualifies, or replace a current-year return instruction. It helps identify which California skill or official source should handle the question.

To the extent work based on this skill concerns a federal tax matter, a practitioner preparing written advice must comply with Treasury Department Circular 230, including 31 CFR §10.37. California outputs also require review by a qualified professional with California tax competence before delivery or filing.

## Scope and who this is for

Use this skill when a person asks about a California personal income tax credit, deduction, exemption credit, disaster loss, penalty or interest relief, or the meaning of California withholding allowances. It covers intake and routing only. It does not provide a complete list of every California tax benefit.

The California pack has a Form 540 method skill focused on full-year residents with Schedule C or disregarded single-member LLC income, a separate figures card, and other topic skills for residency, estimated tax, health coverage, payroll and pass-through entity elective tax. Those skills have narrower scopes. Where no current skill fits, use the current FTB form instructions or refer the issue to a California tax professional rather than stretching a sibling skill beyond its scope.

The words "allowance" and "exemption" can refer to different things. A DE 4 withholding allowance changes wage withholding during the year; it is not a deduction or credit claimed on the annual return. A personal or dependent exemption credit is an annual return item. Confirm which one the client means.

## Ask the client first

- Which tax year is involved, and is this a current-year question or an amended return?
- Who would claim the item: an individual, spouse or registered domestic partner, dependent, estate or trust, partnership, LLC, S corporation, or C corporation?
- What California return or form is involved, and was the person a California resident for all, part, or none of the year?
- What benefit or relief is being considered, and what facts may qualify it, such as rent, dependents' ages, care costs, adoption, college support, a disaster loss, tax paid to another state, or an FTB notice?
- What income, withholding, estimated payments, prior-year elections or claims, and supporting documents affect this item?

Do not request every fact in this list automatically. Ask only for facts that change the selected route, and collect personal information only in an appropriate secure workflow.

## The method, step by step

1. **Identify the tax and claimant.** Confirm that the question is about California personal income tax. If the client means sales or use tax, business entity tax, payroll withholding, property tax, or a city or county charge, route to that topic instead.
2. **Fix the tax year and return.** Use the year the income or event belongs to, not the year the return is filed. Determine whether the person is a full-year resident, part-year resident, or nonresident, and whether the return is Form 540, Form 540NR, or another return. Do not reuse a prior year's form as if it were current.
3. **Select the route.** Use the table below. Load only the relevant skills, then read the official instructions for the tax year and form involved.

| Client's question or facts | Route and handoff |
|---|---|
| Full-year California resident with Schedule C income or a disregarded single-member LLC asks how a benefit affects Form 540 or Schedule CA | Load `ca-540-individual-return` for its stated scope. Load `ca-income-tax` for figures, but reconcile any 2026 amount to the latest FTB publication before using it. |
| Part-year California resident, nonresident, move into or out of California, or California-source income question | Load `ca-residency-leaving-california` before applying a credit or deduction. |
| Standard deduction, itemized deductions, California exemption credits, rate schedules, or a figure already covered by the figures card | Load `ca-income-tax` when it is within scope, then verify the current amount and conditions on FTB's current-year forms and instructions. For an individual who is not within the Form 540 skill's Schedule C scope, use the applicable FTB Form 540 or Form 540NR instructions. |
| Personal credit such as CalEITC, Young Child Tax Credit, Foster Youth Tax Credit, renter's credit, adoption, child and dependent care, college access, dependent parent, joint custody head of household, other-state tax, prior-year AMT, or senior head of household | Start with FTB's Personal Credits page and the Schedule P instructions for the return year. Use the FTB 3514 instructions for CalEITC, YCTC, or FYTC when applicable. Do not infer eligibility from a category name. |
| Disaster loss deduction, a disaster-related filing or payment postponement, or a disaster penalty notice | Read FTB's current Disaster Loss and Emergency Tax Postponement guidance, including the current disaster list and the instructions for the affected form. Do not assume a federal postponement automatically resolves every California filing or payment issue. |
| Penalty dispute, reasonable-cause claim, one-time penalty abatement, interest relief, or refund claim | Start with FTB's Help with Penalties and Fees and Claim for Refund pages, then follow the specific notice and form instructions. Distinguish penalty relief from interest relief and a refund claim. Do not transfer a federal first-time abatement result to California. |
| California estimated tax payment or underpayment question | Load `ca-estimated-tax-540es`; confirm current-year payment information and whether withholding affects the calculation. |
| Individual shared responsibility penalty or exemption for health coverage | Load `ca-form-3853-coverage`. |
| Employee asks about California wage withholding allowances or exempt status on DE 4 | Load `ca-payroll` for the payroll handoff and read the current EDD DE 4. Do not use federal Form W-4 allowances as California PIT allowances. |
| Pass-through entity asks about the entity-level elective tax and member credit | Load `ca-pte-elective-tax`; confirm the entity's eligibility, election and the member's return-year treatment. |
| LLC asks about its annual tax, fee or Form 568 filing | Load `ca-llc-fee-and-tax` and, for a disregarded single-member LLC's filing, `ca-smllc-form-568`. |
| C corporation or S corporation asks about a business credit, deduction, or Form 100 or 100S treatment | The current California pack does not have a dedicated Form 100 or 100S method skill. Use the current FTB business return instructions and refer the issue to a California business tax professional. Do not apply the individual Form 540 method. |
| Fiduciary, estate or trust asks about a credit or deduction on Form 541 | Use the current FTB Form 541 and Schedule P instructions. The individual Form 540 skills do not establish fiduciary eligibility. |
| Sales or use tax exemption, deduction, credit or reimbursement question | Load `california-sales-tax` if its scope fits. If not, use current CDTFA guidance and refer any unresolved classification question. |

4. **Check year-specific authority.** FTB's October 2026 Tax News says the complete 2026 tax rates and exemption amounts will be available in late December 2026. Its 2026 tax-form page labels forms as drafts. As of this skill's review date, do not treat a draft form, the 2025 final booklet, or an older skill amount as final 2026 authority. Recheck FTB before preparing or amending a return.
5. **Handoff with scope stated.** Tell the client which route applies, which facts remain needed, and which part is not covered. Keep the handoff focused on the selected topic; do not turn this router into a calculation or an eligibility conclusion.

## When to refuse or refer

- The taxpayer, return year, residence period, or type of tax is unknown and changes the answer. Ask for that fact before selecting a route.
- A credit, deduction, exemption, or relief depends on facts, documentation, elections, or form instructions the router does not contain. Load the relevant current FTB source or refer to a qualified California tax professional; do not guess eligibility.
- A 2026 amount or instruction is still draft, not published, or conflicts with an older skill. Verify it on FTB's latest current-year page and use no unconfirmed figure.
- The question concerns a corporation, S corporation, fiduciary, estate, trust, partnership, or business return and no live pack skill covers the exact job. Use that return's current FTB instructions and refer the uncovered analysis to a specialist.
- The item concerns county property tax, a local tax, federal tax, an employee benefit plan, or legal eligibility outside California personal income tax. Route to the responsible authority or professional.
- The client wants tax planning, a legal opinion, a filing position, or a guarantee of a refund or penalty waiver. This router provides none of those; refer for a fact-specific professional review.

## Sources

| Source | URL | Read on |
|---|---|---|
| FTB Personal Filing Information, read for the resident/nonresident, deduction, and personal credit categories | https://www.ftb.ca.gov/file/personal/ | 2026-11-24 |
| FTB Personal Credits, read for the Schedule P handoff and credit overview | https://www.ftb.ca.gov/file/personal/credits/ | 2026-11-24 |
| FTB Deductions, read for the standard and itemized deduction handoff and federal-conformity caution | https://www.ftb.ca.gov/file/personal/deductions/ | 2026-11-24 |
| FTB Residents, read for Form 540 and Form 540 2EZ distinctions and referral to deduction and credit pages | https://www.ftb.ca.gov/file/personal/residency-status/ | 2026-11-24 |
| FTB 2026 Tax News, read for the timing of full 2026 rates and exemption amounts | https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/10.html | 2026-11-24 |
| FTB Draft Tax Forms, read for the status of 2026 draft forms and instructions | https://www.ftb.ca.gov/forms/draft-tax-forms.html | 2026-11-24 |
| FTB Disaster Loss, read for the disaster deduction and filing guidance | https://www.ftb.ca.gov/file/business/deductions/disaster-loss.html | 2026-11-24 |
| FTB Emergency Tax Postponement, read for state and federal disaster deadline relief routing | https://www.ftb.ca.gov/file/when-to-file/emergency-tax-relief.html | 2026-11-24 |
| FTB Help with Penalties and Fees, read for reasonable-cause, notice, and penalty-relief routes | https://www.ftb.ca.gov/pay/penalties-and-interest/help-with-penalties-and-fees.html | 2026-11-24 |
| FTB Claim for Refund, read for refund and penalty-relief handoffs | https://www.ftb.ca.gov/help/disagree-or-resolve-an-issue/claim-for-refund.html | 2026-11-24 |
| EDD Employee's Withholding Allowance Certificate (DE 4), read for the California wage withholding handoff | https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de4.pdf | 2026-11-24 |
| 31 CFR Part 10, §10.37, read for the Circular 230 written-advice disclosure | https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol1/xhtml/CFR-2025-title31-vol1-part10.html | 2026-11-24 |

Not yet confirmed: final 2026 Form 540, Form 540NR, Schedule CA, Schedule P and Form 3514 instructions and any remaining indexed credit amounts not yet published as of 2026-11-24. Recheck the current FTB forms page before using this router for 2026 return preparation.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
