---
name: ng-return-assembly
description: Assemble Nigerian 2026 personal or company tax working papers from completed computations, including identity, income, gains, credits, VAT, PAYE and contribution reconciliations. Produce the master workbook, reviewer brief and taxpayer action list with separate federal/state filing and payment evidence. Does not submit returns, invent upstream figures or revive old rates and portal assumptions.
jurisdiction: NG
tax_year: 2026
last_updated: '2026-11-16'
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: '1.1'
type: filing-howto
category: orchestrator
---

# Nigeria return assembly v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Produce a reviewer-ready annual return package for a full-year Nigerian resident individual/sole proprietor or ordinary resident company. This is an assembly method: consume the owning computations and independently reconcile their totals without substituting another set of tax rates. A taxpayer can need a State/FCT personal return and a separate NRS VAT or employer obligation. Authority follows the tax and person; a single combined workbook is not a single combined filing. [NTAA sections3,11,13,14,22 and28](https://nass.gov.ng/documents/download/11250).

Historical provenance retained from the original: **"Reviewed against the cited tax authorities by Omolola Fasasi on 2026-06-21."** That is an old exported body statement, not approval of this rewrite. This file remains tier2 and carries no current accountant approval. The old instruction that this paragraph was generated from verified skill_facts is not a source for current law.

| Filing control | Rule and conditions | Primary source |
| --- | --- | --- |
| Existing company annual return | Within6 months after accounting year-end | [NTAA section11(6)(a)](https://nass.gov.ng/documents/download/11250) |
| New company first return | Earlier of18 months after incorporation and6 months after its first accounting period | [NTAA section11(6)(b)](https://nass.gov.ng/documents/download/11250) |
| Company cessation | No later than6 months after cessation | [NTAA section11(7)](https://nass.gov.ng/documents/download/11250) |
| Individual annual return | JRB:31 March of assessment year, preceding income basis; PAYE/nil-tax status does not alone remove filing | [NTAA section13](https://nass.gov.ng/documents/download/11250); [JRB paragraph11](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf) |
| Employer annual return |31 January for employees in the preceding year | [NTAA section14](https://nass.gov.ng/documents/download/11250) |
| Self-assessed payment | By filing due date; approved instalments must finish by that date | [NTAA section49](https://nass.gov.ng/documents/download/11250) |
| Records | Keep required records6 years after relevant assessment year | [NTAA section31](https://nass.gov.ng/documents/download/11250) |
| Late return | NGN100,000 first month and NGN50,000 each subsequent month of failure; do not use the old CITA or PITA filing penalties for a current NTAA obligation | [NTAA section101](https://nass.gov.ng/documents/download/11250) |
| Tax clearance | Issue within2 weeks of demand or give denial reasons, where assessment fully paid/no tax due; prescribed dealings refer to preceding3 assessment years | [NTAA section72](https://nass.gov.ng/documents/download/11250) |

For illustration, an existing ordinary company with31 December2026 year-end has30 June2027 due date;2026 employee annual reporting has31 January2027 due date. A preceding-basis individual2027 assessment filing date is31 March2027 under the JRB guideline. These are derived calendar examples, subject to actual period and a sourced extension. Earlier2025 year-end/company30June2026, individual31March2026 and employer31January2026 examples are historical dates, already past at this read date; do not present them as upcoming.

## Ask the client first

Use the complete existing intake, case record, accounts and upstream outputs before asking anything again. Ask only for a missing item that changes finalisation:

1. Taxpayer legal identity/individual-company status, Tax ID, RC/BN/NIN as applicable, employer code/RSA where relevant, State/FCT and residence history, tax office, basis period and assessment year.
2. Signed/attested accounts, bookkeeping trial balance, current computation outputs, asset/loss schedules and all-source income, including gains, foreign items and employment.
3. PAYE/WHT credit evidence and schedules, advance tax, prior offsets/refunds, assessments, payment proof and filing acknowledgements; authority/period for each item.
4. Monthly VAT, payroll and social-contribution returns/remittances, employer headcount, contribution coverage and outstanding certificates/notices.
5. Related-party transactions, donations/incentives, special-sector facts, unresolved discrepancies, missing upstream work and actual filing authority/portal access delegated to the authorised filer.

## The method, step by step

### Consume the existing work and fix identity/period

Do the authorised reconciliation and prepare the package without asking whether to assemble it. Use [ng-freelance-intake](ng-freelance-intake.md), [ng-formation](ng-formation.md), [ng-personal-income-tax](ng-personal-income-tax.md), [ng-cit](ng-cit.md), [ng-cgt](ng-cgt.md), [ng-wht](ng-wht.md), [ng-payroll](ng-payroll.md), [ng-pension-nhf-social-contributions](ng-pension-nhf-social-contributions.md) and [nigeria-vat](nigeria-vat.md), subject to their own unresolved items. ng-income-tax retains the narration library. Old ng-paye/ng-statutory-deductions/ng-foundation/ng-intake names are not existing owning files. Do not edit or infer renewed approval for the held VAT files.

Make one identity sheet: legal name, person type, registration/TIN evidence, RC/BN, NIN where required, address/contact, State/LGA, employer code, RSA, authority, accounting start/end and YOA. Verify the issued Tax ID rather than demand a fictional universal10-digit or12-digit format. Keep federal and State tax/payroll codes separate. NTAA sections4 to8 require registration/use and prohibit multiple/misused Tax IDs. Do not substitute place of employment for the First Schedule residence test. [NTAA sections3 to8/First Schedule](https://nass.gov.ng/documents/download/11250).

Resolve effective-law and basis-period differences before selecting rates. ng-cit records the official NTA-copy differences; ng-personal-income-tax records current versus historical CRA, gains and basis rules. The original2026 planning notes are now current-law review topics, not permission to back-apply new thresholds. Unresolved full transition guidance remains held under Sources. State all comparison alternatives where necessary; no arbitrary higher bracket, automatic allowance cap, donor disallowance or authority selection can replace evidence.

If an upstream computation did not run or a self-check fails, name it and continue assembling the available working paper. A partial package may be useful, but it is not final or ready to file until material held positions and identity/payment issues are resolved. Do not fabricate a missing amount or treat a failed check as passed.

### Run the eight reconciliations

1. **Revenue:** anchor to books/trial balance. Bridge gross income in the tax computation to annual VAT supplies and WHT-associated receipts. Explain exempt/zero-rated/out-of-scope supplies, accrual/cash timing, credit notes, disposals, foreign receipts and intragroup elimination. WHT divided by a rate can be a diagnostic only after correct rate/base/period and gross-up are known; it is not substitute turnover.
2. **Credits:** separate PAYE, creditable recipient WHT, advance payments, foreign tax and approved prior offsets. Match each to taxpayer, period, authority, gross receipt and supporting evidence; eliminate duplicates and final-taxed dividends/passive items. Outgoing WHT remitted for suppliers is not the payer's own income-tax credit. Final dividend withholding is not ordinary CIT credit; use ng-wht and ng-cit for franked income/redistribution and excess-dividend exceptions. Do not assume a universal6-year WHT expiry; section55's refund-claim period is a different issue. A credit older than3 years is an internal verification flag, not statutory expiry.
3. **Payroll:** employee/YTD totals and employer annual return must reconcile to every monthly payroll return, salary bank payment, PAYE liability and authority receipt, including joiners/leavers, benefits, bonus and December true-up. Use actual H1/FormG labels only where the authority prescribes them.
4. **Contributions:** employee deductions plus employer accruals must reconcile to scheme coverage, monthly registers, pension/PFC/NHF/ECS/ITF/health payments and receipts; identify arrears, missing RSA allocation and penalty exposure. Do not automatically treat every certificate as a statutory TCC prerequisite.
5. **WHT agent:** contracts, expense/AP ledger, payer schedules and deductions/remittances agree by payee, nature, residence, Tax ID, tax point, authority and currency. Apply the separate receipt-credit rule; recipient credit is not always defeated by a payer's failure to remit.
6. **VAT:** sum every relevant return and reconcile output supplies, credit notes, input recovery, balances and payments. VAT is not a CIT/PIT credit. Recoverable input VAT is not also an expense/asset cost; non-recoverable VAT follows the relevant underlying treatment. A company income-tax exemption does not by itself remove VAT.
7. **Assets/gains/losses:** compare fixed-asset register, book depreciation, additions/disposals, qualifying cost, allowances, gain residue, reinvestment and loss use; prevent double deduction. Transfer current chargeable gains into income tax rather than assume every current gain needs an independent flat10% charge.
8. **Differences:** retain the original internal policy: investigate and show every difference; above NGN1,000 flag Needs Input, above NGN100,000 give it prominent reviewer attention. These are workflow priorities, not statutory tolerances or authority to write off smaller amounts. Explain and resolve differences; do not round them away.

### Individual return working paper and field map

Consume all-source employment, net trade/professional, partnership, rent, investment, digital and other income, chargeable gains, exemptions, eligible deductions, tax bands and credits from the personal-tax computation. Attach accounts, cost/asset/loss schedules, rent/insurance/pension evidence, PAYE and WHT registers and foreign-tax computation where relevant. Do not make another CRA or rate calculation inside this assembly.

[JRB Appendix2](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf) maps **A** taxpayer identity; **B** YOA/filing mode/tax office; **C** employment/business information and source selection; **D** annual employment, business ScheduleX, rent ScheduleY, investment, gains ScheduleM and other ScheduleQ; **E** eligible deductions; **F** chargeable-income computation; **G** tax; **H** credits; **I** payable/overpayment; **J** taxpayer declaration; **K** official use. Its PartF repeats deduction references including E1/E2 not clearly labelled in PartE. Reconcile to the statute and actual authority's form and deduct eligible amounts once, rather than blindly subtract the same figure twice. Mark exempt/final-taxed income and corresponding adjustments transparently; do not force exempt amounts into taxable fields merely because a form has a line.

NTAA section13 permits audited statements OR accounts attested by the individual for trade/business; do not claim every sole trader needs a statutory audit. Employer filing does not replace personal annual filing. Do not complete official-use fields or sign the taxpayer declaration for them. A legacy "FormA" label does not guarantee identical parts across States.

### Company self-assessment working paper

Bring in legal identity/period/accounts; turnover and company-size test; accounting profit; add-backs; exempt/final-taxed adjustments; assessable profit; qualifying losses; allowances and taxable profit; CIT; development levy; any ETR top-up; separate historic TET/minimum-tax/incentive schedules where legally applicable; credit register; balance due/overpayment and payment evidence. Use the owners' actual ordering and limits. CIT and levy bases differ; a levy can remain when taxable profit falls after allowances. Keep franked income, dividends and excess-dividend-tax tests visible without presuming a credit.

Attach accounts and signed principal-officer attestation, computation, fixed assets/allowances, losses, donations/beneficiary evidence, recipient WHT, foreign-tax, incentives, related-party and gain schedules. NTAA section11 allows a small company's taxpayer-attested accounts instead of audited statements; this is not a determination of CAMA corporate-audit exemption. Companies in the ETR regime have the additional prescribed return information. Related-party transactions require the arm's-length test under [NTA section191](https://nass.gov.ng/documents/download/11249); do not invent a blanket LocalFile attachment or an unverified TP threshold. Separate current development levy from repealed/continuing historical levies and preserve transition evidence. [NTAA section11](https://nass.gov.ng/documents/download/11250); [NTA sections27,56,57,59,163,191,195 to198](https://nass.gov.ng/documents/download/11249).

### Build the three deliverables

1. **`[taxpayer_slug]_[income_period]_ng_master.xlsx`**, retaining the old2025 naming convention only for an actual2025 package. Sheets: Cover, Identity, FormA or CIT Self-Assessment, Tax Computation, Capital Allowances, Loss Relief, WHT Credit Notes Register, Statutory Deductions Register, VAT Reconciliation, Employer Annual/Monthly Reconciliation, Cross-Check Summary, Payment Schedule and Compliance Certificates Tracker. Keep source documents/references, formulas and status on every schedule; recalculate and check for broken references. This skill describes the output; it does not pretend an actual workbook has already been made.
2. **`reviewer_brief.md`**: executive summary/identity/period; federal or State headline calculation; contributions; recipient/agent WHT; VAT; gains; payroll; formation/compliance identity; all eight reconciliations; attention flags; positions taken with legal sources; current-versus-historical planning and unresolved items. Include the exact tax, credits, paid amounts, remaining payable/overpayment, earliest deadline and responsible filer/body. Separate an evidenced fact, calculation, assumption and held position.
3. **`taxpayer_action_list.md`**: immediate deadlines, each payment amount/tax type/authority/period/reference/status, each separate return/attachment, missing evidence, statutory contribution steps, certificate/TCC requests, monthly calendar, record policy, and authorised post-review submission. Clearly label partial outputs if interrupted; complete and disclose what remains.

Place files in the actual writable delivery directory for the current environment and link all three. The old hardcoded `/mnt/user-data/outputs/` is not portable. Do not claim an incomplete output is final because a formatted file exists.

### Review and attestation control

Keep the original workflow's human-review gate before a filing package is released as ready. NTAA section33 permits self-representation or an accredited agent; it does not impose a universal ICAN/ANAN signature on every self-filed return. Professional review here is the package's quality control, distinct from that legal representation rule. Preserve the original ICAN/ANAN/CITN/FRC fields as optional reviewer credentials where applicable, without inventing a person's name/number or reproducing private identifiers in public material.

The brief carries an unsigned attestation with taxpayer/period/preparer, reviewer name/firm/credentials/date and checkboxes: accounts signed/attested; tax adjustments/allowances/reliefs checked; contribution/certificate status; credits verified; revenue/VAT differences explained; employer annual/monthly/payments tied; correct transition law; TP and special obligations assessed; applicable minimum-tax/ETR and dividend tests; actual payment and filing steps explained. An AI must not tick "reviewed" on behalf of a professional or fabricate a signature. An unresolved material item keeps the package in working-paper status.

## Boundary and exception table

| Trigger | Output consequence |
| --- | --- |
| Missing upstream result, identity or Tax ID | Retain placeholders, name missing item and complete available schedules; finalisation blocked where material. |
| Unverified WHT/foreign credit, donation, allowance or loss | Separate proposed amount and evidence gap; show effect/alternatives, no invented disallowance or promised refund. |
| Missing certificate or account audit question | Determine actual requirement for that body/transaction; distinguish corporate-law audit from tax-return attestation and procurement certificates from TCC. |
| Petroleum/hydrocarbon, mining, telecom/gaming, pioneer/priority incentive or NEPZA/OGFZA free zone | Specialist computation required; do not fill ordinary formulas into a special regime. |
| Non-resident/PE/SEP, treaty, mixed-residency or expatriate year | Refer with evidence; this capstone does not decide those legal positions. |
| Combined federal/State dispute, TAT, audit defence or TP audit | Refer to appropriately qualified adviser/counsel; preserve notices and dispute payment/deadline evidence. |
| Asked to upload, pay, sign or submit | This skill produces working papers and filing instructions. An authorised filer acts after the review gate; no submission or payment is authorised by this reference alone. |

## Worked cases

**Company package with separate levy base.** Upstream ng-cit supplies assessable profit20m, taxable profit12m, CIT3.6m and development levy800k for a company already determined non-small and outside ETR. Supported creditable WHT2m and advance CIT1m leave CIT600k; levy800k remains separate, so total outstanding1.4m. Supplier WHT remitted400k is a compliance liability, not another credit: using it would wrongly reduce outstanding to1m. The case checks assembly of supplied computations, not another tax-rate home. Keep the underlying owner method and actual eligibility with the package.

```oa-check
name: Nigeria company return own credits versus supplier withholding
inputs:
  upstream_cit: 3600000
  upstream_development_levy: 800000
  recipient_credit: 2000000
  advance_cit: 1000000
  supplier_wht_remitted: 400000
steps:
  - cit_balance: upstream_cit - recipient_credit - advance_cit
  - all_outstanding: cit_balance + upstream_development_levy
  - incorrect_credit_result: all_outstanding - supplier_wht_remitted
expected:
  cit_balance: 600000
  all_outstanding: 1400000
  incorrect_credit_result: 1000000
```

**Revenue decision under the internal control policy.** Books10m versus VAT-supply total9.8m gives200k difference. Evidence shows exempt supply150k and timing50k, leaving0: documented bridge passes. If only150k is supported, unexplained50k is Needs Input under the1,000 policy; it does not disappear because below the100,000 priority flag. Without any evidence the full200k requires prominent reviewer attention. These priorities do not establish tax treatment of the purported exemption/timing adjustment, which the VAT owner must confirm.

```oa-check
name: Nigeria return revenue bridge evidence decision
inputs:
  books: 10000000
  vat_supplies: 9800000
  supported_exempt: 150000
  supported_timing: 50000
steps:
  - gross_difference: books - vat_supplies
  - explained_balance: gross_difference - supported_exempt - supported_timing
  - missing_timing_balance: gross_difference - supported_exempt
  - unexplained_no_evidence: gross_difference
expected:
  gross_difference: 200000
  explained_balance: 0
  missing_timing_balance: 50000
  unexplained_no_evidence: 200000
```

## When to refuse or refer

Retain the original refusal set: missing upstream work/self-check, material reconciliation or intake gap; specialist sectors/incentives; non-resident/PE/SEP/mixed residence; federal/State litigation/audit/TP dispute; direct portal submission; and retrospective use of new rules. Keep working, naming each gap, but do not declare the final return ready, choose an unsupported conservative position, manufacture identifiers/references or imply professional approval. No automated PDF filling, TaxProMax XML/bulk upload, CbCR XML or full TP documentation is produced here.

## Filing and payment

Use the verified authority's current official service entry point. For federal accounts start at [NRS](https://www.nrs.gov.ng/); older TaxProMax links and FIRS labels in historical evidence do not establish a current screen. For Lagos start at [LIRS](https://lirs.gov.ng/) and its eTax service; for another State/FCT use that authority, not a Lagos form by default. Current authenticated fields, XML templates and payment reference formats were not inspected, so do not invent box numbers or an RRR. NRS/company and State personal/PAYE packages remain separate.

For each tax: verify entity, period, tax type and computation; prepare the return/attachments; obtain the actual assessment/payment request from the authorised official channel; have the authorised payer pay the exact remaining balance; save reference, receipt, date, bank evidence and authority allocation; have the authorised filer submit/complete the return; save the separate return acknowledgement. Reconcile assessment, payment and filing statuses independently. A Remita payment reference, where that channel is actually offered, is not a return acknowledgement; payment does not itself file. Approved instalments under section49 do not postpone the final deadline or create quarterly15April/July/October/January defaults. Late assessed-tax notices and objections have their own payment/abeyance rules. [NTAA sections11,13,49 and85](https://nass.gov.ng/documents/download/11250).

Build a monthly calendar for VAT, PAYE, WHT and each applicable scheme using owning skills and actual assessments; resolve ng-wht's disclosed State deadline conflict. Keep formation, social certificates and tax clearance distinct. Apply TCC separately through the relevant authority using the preceding3 years' assessment/payment evidence; nil liability and evidenced source deductions have statutory protections. A tax clearance certificate is not a declaration that every procurement or contribution certificate is current. [NTAA section72](https://nass.gov.ng/documents/download/11250).

An overpayment is subject to verification/set-off/refund: section55 permits a written claim within6 years of the relevant assessment year and refund within90 days of the authority's decision after audit, with a set-off option; no promise of payment90 days after filing. Late payment uses section65's10% penalty plus specified interest, distinct from withheld-tax non-remittance under section107. Resolve applicable sanctions by obligation and actual period rather than compound old penalty tables. Preserve books/returns/payment and receipt records for the statutory period; retain asset acquisition and relief histories through use and subsequent enquiry as prudent policy. [NTAA sections31,49,55,65 and107](https://nass.gov.ng/documents/download/11250).

## Completion checklist

- All identity, tax and period fields evidenced; relevant federal/State authority confirmed.
- All required upstream owners loaded; gaps and special regimes explicitly marked.
- Every revenue, credit, payroll, scheme, WHT, VAT, asset and tolerance check reconciled or held with quantified effect.
- Correct current/historical law, exemptions, levy/minimum-tax/ETR/dividend and foreign-tax treatment checked by their owners.
- Return schedules tied to accounts and actual prescribed form; no double deductions or final-taxed credits.
- Payment, filing and certificate statuses distinct; references genuine; due dates sourced and responsibility assigned.
- Three outputs recalculated, internally consistent, linked, and labelled partial or reviewer-ready honestly.
- Reviewer attestation remains unsigned until the actual reviewer acts; no material gap hidden by a passed formatting check.

## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| NTAA sections3 to8,11,13 to15,22,28,31,33,49,51,55,65,72,85,100 to107 and relevant First Schedule residence rules | https://nass.gov.ng/documents/download/11250 | 2026-11-16 |
| NTA sections20 to32,56 to59,119 to121,163,191,195 to198; owning computation scopes recorded in their source tables | https://nass.gov.ng/documents/download/11249 | 2026-11-16 |
| JRB2026 PIT Guidelines paragraphs11 to15/22 to26 and full Appendix1/2 form structure, including PartF ambiguity | https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf | 2026-11-16 |
| Government transition announcement only; full operative document unavailable | https://fmino.gov.ng/federal-government-issues-transition-guidelines-for-tax-acts-2025/ | 2026-11-16 |

Not yet confirmed: live authenticated federal/State portal fields, current TaxProMax/Remita/TSA payment sequence/reference lengths, universal VAT002/H1/FormG nomenclature and paper-filing requirements in each State; complete transition Guidelines and straddling periods; CAMA section402 audit exemption; TP LocalFile NGN300m, MasterFile NGN160b, CbCR and purported NGN12m thresholds/filing dates; universal12-month validity or TCC prerequisite for ITF/NSITF/PenCom/NHF certificates; the original6-year WHT shelf-life claim or routine quarterly advance-tax dates; historic CITA/PITA penalties and credits/EDT offsets not confirmed by the owning computation. These topics are preserved for resolution, with no guessed current instruction. The repeated old rate/threshold tables, conservative defaults and action lists are replaced by the owning methods, eight specific reconciliations and current workflow above; old2025 files/dates remain historical conventions only.
