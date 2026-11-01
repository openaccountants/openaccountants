---
name: bf-social-contributions
description: >
  Burkina Faso social contribution workpaper for the 2026 tax year, covering the ordinary CNSS employee branches, individual contribution ceiling, remuneration and benefits in kind, expense exclusions, employer and employee splits, declaration fields and the public monthly or quarterly payment instructions. Use for CNSS contribution calculations, the twenty-worker reporting boundary, company vehicles, voluntary pension contributions and separating social contributions from payroll taxes. Two executable cases test the ceiling and payment-frequency decision. The Guide identifies which statements come from signed orders and which rely on current CNSS authority guidance. Unreadable statutes, current social penalties, AMU activation and authenticated filing remain explicit source gaps.
jurisdiction: BF
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.1
---

# Burkina Faso social contributions (CNSS) v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This is a 2026 contribution workpaper for an employer/worker whose affiliation to the CNSS employee regime is established, and for a person already admitted to its voluntary pension branch. It does not decide the CNSS/CARFO boundary, a new employee group's statutory coverage or a cross-border exemption. The CNSS now identifies Loi 004-2021/AN as the relevant regime in its official forms; do not rely on the old Guide's 2006-law citation as proof of the current procedure. [CNSS official BNTS and references to Loi 004-2021 arts. 17–18](https://cnss.bf/wp-content/uploads/2024/07/1_Bordereau-Nominatif-des-Travailleurs-Salaries.pdf).

CNSS and the separate AMU/CNAMU scheme must be reconciled independently. Ministry AMU guidance has been read, but the signed AMU decree, full operative 2026 category/start-date rules and authenticated workflow have not been verified. This Guide therefore computes CNSS only and does not produce a complete payroll net-pay or employer-cost total. Salary tax and TPA belong in [payroll](bf-payroll.md).

## Rates, bands and thresholds

| CNSS item and conditions | Employer | Employee | Official source |
|---|---|---|---|
| Pensions under ordinary employee CNSS affiliation | 8.5% | 5.5% | [CNSS contribution authority page, citing Décret 2023-0129](https://cnssbf.org/?p=2078) |
| Family benefits | 6% | 0% | [CNSS contribution authority page](https://cnssbf.org/?p=2078) |
| Occupational risks, ordinary rate before any notified prevention surcharge | 1.5% | 0% | [CNSS contribution authority page and Arrêté 2023-018 arts. 2–8](https://cnssbf.org/?p=2078) |
| Total ordinary employee regime | 16% | 5.5%, combined 21.5% | [CNSS contribution authority page](https://cnssbf.org/?p=2078) |
| Contribution ceiling per insured worker | XOF 800,000 monthly / 9,600,000 annually, not a pooled employer allowance | Same individual ceiling | [Arrêté 2022-067 art. 2](https://cnssbf.org/wp-content/uploads/2024/02/arrete_no_2022-067_fixation_du_plafond_des_salaires_soumis_a_cotisation_du_regime.pdf) |
| Admitted voluntary insured, pension branch only | Entire 14% borne by the member | No employer split | [CNSS contribution authority page; official voluntary form](https://cnssbf.org/?p=2078) |

The signed ceiling order takes effect on its 30 August 2022 signature (arts. 3–4). The signed base order takes effect from 30 August 2022 (art. 9). These are effective-date readings, not claims that a 2026 statute was enacted. The current CNSS authority page confirms the rates and ceiling when read on 1 November 2026. Its linked rate PDF is mislabelled and the separate ministry rate PDF could not be read; rate-decree article numbers/full text remain a source limit, not an invented citation.

## The base

1. Build each worker's remuneration base from actual payslips and benefit evidence. Arrêté 2023-017 arts. 2–3 includes base/supplementary pay, overtime, the listed housing/residence/transport/function and other allowances, seniority/performance/other listed bonuses, tips, thirteenth month, notice/paid-leave compensation, employer payment of the employee share and other employment cash benefits. An allowance's payroll label does not alone exclude it. [Arrêté 2023-017 arts. 2–3](https://cnssbf.org/wp-content/uploads/2024/02/Arrete-n%C2%B02023-017-portant-determination.pdf).
2. Add the counter-value of employment benefits in kind, including housing/accessories, domestic staff, company vehicles, school fees, local staff leave travel and any other precisely valued benefit. Where the specified housing/accessories, domesticity or vehicle element belongs to the enterprise and is made available to the worker, art. 5 uses a monthly forfait of historical cost divided by 240. Identify benefits separately in declarations. Do not import salary-tax family or professional-expense deductions into this base. [Arrêté 2023-017 arts. 4–6](https://cnssbf.org/wp-content/uploads/2024/02/Arrete-n%C2%B02023-017-portant-determination.pdf).
3. Exclude genuine expense reimbursements under art. 7, including its listed travel, milk, dirty-work, meal and tool allowances on the reimbursement character. The same article separately excludes death, negotiated departure, end-of-contract, dismissal and retirement-departure amounts; family allowance; maternity/work-accident daily benefit; annuity; pension; and damages. Classify the actual payment rather than relabelling taxable pay as reimbursement. [Arrêté 2023-017 art. 7](https://cnssbf.org/wp-content/uploads/2024/02/Arrete-n%C2%B02023-017-portant-determination.pdf).
4. Apply the per-person ceiling. The CNSS authority page also states the base cannot fall below current SMIG; the present amount and treatment of partial periods/multiple employers are not established here. Cases below use full months, one employer, and remuneration above that unverified floor. [Arrêté 2022-067 art. 2; CNSS base guidance](https://cnssbf.org/wp-content/uploads/2024/02/arrete_no_2022-067_fixation_du_plafond_des_salaires_soumis_a_cotisation_du_regime.pdf).
5. Multiply each branch base by the applicable split and reconcile the employee withholding and employer cost separately. The employer owes all CNSS contributions and withholds the worker's share at each pay, subject to the ceiling. Employer-only branches do not reduce the employee's pay. [CNSS contribution instructions, “Obligations de l’employeur”](https://cnssbf.org/?p=2078).

**Risk surcharge.** The ordinary risk rate is not unconditional. Arrêté 2023-018 requires a prevention inspection, notified findings/corrections and a revisit. Uncorrected failures trigger a 50% increase of that branch rate; the notified increase starts the first day of the month after the correction deadline and is suspended from the first day of the month after full correction. The signed recurrence clause contains inconsistent words and parenthetical percentage, so its precise repeated-breach computation is held. Obtain the actual CNSS notice; do not automatically keep the ordinary rate after it. [Arrêté 2023-018 arts. 2–9](https://cnssbf.org/wp-content/uploads/2024/02/Arrete-n%C2%B02023-018-portant-determination.pdf).

## Deadlines and filing

1. Check employer and worker registration before calculating. CNSS's public employer-registration instructions identify the CEFORE common registration channel and the ordinary company dossier: employer request, RCCM/recognition, IFU, identity evidence, company statutes and workers' registration files. Existing registration and identity values are client inputs, not information to invent. [CNSS employer registration instructions](https://cnssbf.org/immatriculation-de-lemployeur/).
2. Prepare the **Bordereau nominatif des travailleurs salariés (BNTS), Pr-RCS/Cot 01**, available official version dated 7 April 2023. The PDF has three physical pages: Cot 01 front and reverse on pages 1–2, and the Cot 02 intercalary on page 3. Its columns are: (1) enterprise worker number; (2) CNSS number; (3–4) surname/given names; (5–6) period start/end; (7) gross pay plus benefits; (8) capped CNSS base; (9) employment code; (10) income code; (11) observations. Use the form's code tables, record total headcount and sign/stamp. Its instructions require the electronic version and identify e-CNSS; the published form is source evidence, not proof that the current authenticated upload screen is unchanged. [CNSS BNTS, Cot 01 front/reverse and Cot 02 intercalary](https://cnss.bf/wp-content/uploads/2024/07/1_Bordereau-Nominatif-des-Travailleurs-Salaries.pdf).
3. Prepare the separate **Déclaration récapitulative des salaires, Pr-RCS/Cot 04**, with period, employer number, branch/category bases, branch contributions and principal total. The form marks delay/non-production surcharge and total-due fields for CNSS completion; do not prefill an unsupported sanction. Ensure the employer number accompanies payment. [CNSS recap form, both pages](https://cnss.bf/wp-content/uploads/2024/07/5_Declaration-recapitulative-des-salaires.pdf).
4. The current CNSS contribution page states monthly payment for employers with twenty or more employees, within the first fifteen days after month-end; fewer than twenty employees use quarterly payment within thirty days after quarter-end. The recap form separately requires the monthly declaration by the 15th of the following month and the quarterly declaration by the last day of the following month. Both the recap and BNTS require payment with the declaration. For a following month of 31 days, that quarterly declaration wording differs from the web page’s thirty-day payment window. The precise controlling interaction remains held because the downloaded 2021 law is malformed; do not treat the last calendar day as an approved payment extension. Do not replace them with the AMU monthly deadline or infer an unverified extension. Retain the submitted BNTS/recap, electronic counterpart, receipt and account-allocation evidence. [CNSS contribution guidance](https://cnssbf.org/?p=2078); [official BNTS instructions](https://cnss.bf/wp-content/uploads/2024/07/1_Bordereau-Nominatif-des-Travailleurs-Salaries.pdf).
5. For an admitted voluntary insured, the official subscription form limits cover to pensions, puts all contributions on the member and states payment within thirty days after the month/quarter. It explains suspension/loss of insured status after twelve months and conditions for resumption, uncredited periods and pension-entry cessation. Use that form's identity/supporting-document checklist and the member's CNSS references; do not enrol an employee as voluntary to avoid employer contributions. Full eligibility and optional-income-floor rules remain held. [CNSS voluntary subscription form, both pages](https://cnss.bf/wp-content/uploads/2024/02/SOUSCRIPTION-A-LASSURANCE-VOLONTAIRE.pdf).

No authenticated e-CNSS session, current upload template validation, acknowledgement or bank-allocation workflow was tested. The exact operative-law declaration deadline and all special-worker schedules require the source resolution stated below.

## Penalties and interest

The old Guide's CNSS late-payment and late-declaration percentages cannot be recertified from the unreadable current law and the primary texts opened. Do not compute a CNSS penalty using them. The official BNTS and recap confirm that delay/non-production brings sanctions, refer to Loi 004-2021 arts. 17–19 and allocate the relevant recap fields to CNSS. Obtain the applicable assessment and readable controlling text before calculating. [Official BNTS](https://cnss.bf/wp-content/uploads/2024/07/1_Bordereau-Nominatif-des-Travailleurs-Salaries.pdf); [official recap](https://cnss.bf/wp-content/uploads/2024/07/5_Declaration-recapitulative-des-salaires.pdf).

The ministry's AMU guidance describes a separate scheme's declaration/payment sanctions. They are not authority for CNSS sanctions. The prevention surcharge above is also distinct from late-payment penalties. [Ministry AMU payment guidance](https://www.fonction-publique.gov.bf/accueil/actualites/details?cHash=a4f5423688bb0ffe0c4ef33bc95b172a&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=2517).

## Cross-border points

A foreign posting, multiple-employer arrangement or foreign pension record does not establish CNSS exemption or a second ceiling. The applicable treaty/coordination, detached-worker and totalisation rules are not established by the sources read. Keep those facts out of an ordinary single-employer computation until the relevant coverage decision is sourced. AMU is separate; no CNSS ceiling or payment-frequency rule is automatically transferred to it.

## Two worked examples that recompute

**Full-month ceiling and benefits.** An ordinary CNSS employee has cash remuneration XOF 900,000, an enterprise-owned company vehicle with historical cost XOF 12 million, and a genuine XOF 20,000 business-expense reimbursement. The vehicle adds XOF 50,000; the reimbursement is excluded. The XOF 950,000 remuneration base is capped at XOF 800,000. Ordinary employer contributions are XOF 128,000 and employee contributions XOF 44,000. This does not compute IUTS, TPA, AMU or any risk surcharge.

```oa-check
name: CNSS benefits and individual ceiling
inputs:
  cash_pay: 900000
  vehicle_historical_cost: 12000000
  reimbursement: 20000
steps:
  vehicle_benefit: vehicle_historical_cost / 240
  remuneration_base: cash_pay + vehicle_benefit
  contribution_base: min(remuneration_base, 800000)
  employer: contribution_base * 0.16
  employee: contribution_base * 0.055
  combined: employer + employee
expected:
  vehicle_benefit: 50000
  remuneration_base: 950000
  contribution_base: 800000
  employer: 128000
  employee: 44000
  combined: 172000
```

**Decision: monthly or quarterly schedule?** Assume stable headcount throughout the period, ordinary employee coverage, no surcharge, and XOF 300,000 monthly contribution base for each worker. With twenty workers, the monthly total is XOF 1,290,000 and the authority's monthly schedule applies. With nineteen workers, the monthly accrual is XOF 1,225,500, but the three-month payment is XOF 3,676,500 under its quarterly schedule. Choose the schedule from actual headcount and CNSS status, not preferred cash timing; headcount changes require confirmation of the applicable transition procedure.

```oa-check
name: CNSS twenty-worker reporting boundary
inputs:
  monthly_base_per_worker: 300000
  monthly_staff: 20
  quarterly_staff: 19
steps:
  total_per_worker: monthly_base_per_worker * 0.215
  monthly_payment: total_per_worker * monthly_staff
  quarterly_monthly_accrual: total_per_worker * quarterly_staff
  quarterly_payment: quarterly_monthly_accrual * 3
expected:
  total_per_worker: 64500
  monthly_payment: 1290000
  quarterly_monthly_accrual: 1225500
  quarterly_payment: 3676500
```

## Ask the client first

- Which employer/worker CNSS registration and coverage category are evidenced, and is voluntary status already admitted?
- What were headcount and each worker's actual full/partial pay periods?
- What cash pay, benefits/historical costs and genuine reimbursement records exist?
- Is there a prevention notice, surcharge or contribution assessment?
- Which declarations, receipts and payroll withholdings already appear in the CNSS account?
- Are AMU, public-service coverage, multiple employers or foreign postings involved?

## Sources

| Source | Actual reading scope | Read on |
|---|---|---|
| [Signed Arrêté 2022-067](https://cnssbf.org/wp-content/uploads/2024/02/arrete_no_2022-067_fixation_du_plafond_des_salaires_soumis_a_cotisation_du_regime.pdf) | Read both scanned pages, especially ceiling art.2 and signature/effect arts.3–4. | 2026-11-01 |
| [Signed Arrêté 2023-017](https://cnssbf.org/wp-content/uploads/2024/02/Arrete-n%C2%B02023-017-portant-determination.pdf) | Read scanned substantive pages 2–5: arts.1–10, remuneration, benefits and exclusions, including signature/effect. | 2026-11-01 |
| [Signed Arrêté 2023-018](https://cnssbf.org/wp-content/uploads/2024/02/Arrete-n%C2%B02023-018-portant-determination.pdf) | Read substantive scanned pages 2–3, arts.1–11; recurrence wording/numeric inconsistency actually seen. | 2026-11-01 |
| [CNSS contribution guidance](https://cnssbf.org/?p=2078) | Read for the rate/split, voluntary rate, base/floor, employer obligations and monthly/quarterly payment sections, not a verified signed rate decree. | 2026-11-01 |
| [CNSS BNTS](https://cnss.bf/wp-content/uploads/2024/07/1_Bordereau-Nominatif-des-Travailleurs-Salaries.pdf) and [recap](https://cnss.bf/wp-content/uploads/2024/07/5_Declaration-recapitulative-des-salaires.pdf) | Read for BNTS columns 1–11 and recap branch/category fields, BNTS physical pages 1–2 (Cot 01 front/reverse) and page 3 (Cot 02 intercalary), plus both recap pages and their instructions/code tables; no authenticated portal operation. | 2026-11-01 |
| [CNSS employer registration](https://cnssbf.org/immatriculation-de-lemployeur/) | Actual CEFORE channel and ordinary company dossier, public-page lines 164–188; no special-category or live registration approval. | 2026-11-01 |
| [CNSS voluntary subscription](https://cnss.bf/wp-content/uploads/2024/02/SOUSCRIPTION-A-LASSURANCE-VOLONTAIRE.pdf) | Read both pages, pension-only cover, member funding, periods/suspension and document checklist. | 2026-11-01 |
| [Ministry AMU contribution guidance](https://www.fonction-publique.gov.bf/accueil/actualites/details?cHash=25196f1849f6833010b67cadeb5258be&tx_news_pi1%5Bnews%5D=2504) and [payment guidance](https://www.fonction-publique.gov.bf/accueil/actualites/details?cHash=a4f5423688bb0ffe0c4ef33bc95b172a&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=2517) | Actual 30 July 2025 and 6 August 2025 explanatory texts referring to Décret 2024-0345; read to distinguish AMU, not to certify its signed articles or operative 2026 activation. | 2026-11-01 |

Not yet confirmed: controlling reconciliation of quarterly declaration by the last following-month day versus payment within thirty days, including simultaneous-payment instructions;  readable full Loi 004-2021 and Décret 2023-0129 with exact controlling article checks; historical prior ceiling XOF 600,000; CNSS late-payment 2%/late-declaration 1% legacy claims and legal-interest interaction; repeated-risk-surcharge words versus printed percentage; current SMIG and part-period/multiple-employer floor/ceiling; current authenticated e-CNSS template/acknowledgement/payment allocation; full voluntary eligibility/income election; signed AMU decree and operative 2026 categories/start dates, rates/bases/ceilings, forms and remittance; foreign coverage/coordination and sanction cumulation. Independent conditional source review of this rewrite is accepted; no accountant has attested to it.

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
