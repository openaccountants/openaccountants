---
name: romania-references
jurisdiction: RO
last_updated: 2026-11-15
version: 1.1
description: "Use this skill to assess software references for Romanian tax workflows in 2026: start with the official ANAF form, validator and schema for the reporting period; reconcile computations with the Fiscal Code; distinguish technical validation from legal correctness; retain the older third-party project catalogue as unconfirmed research leads. Covers declaration tools, PFA calculators and VAT-register integrations. It does not install software, certify third-party licenses, query a taxpayer or file a return."
tier: 2
tax_year: 2026
type: filing-howto
---

# Romania: official technical references and software research leads

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Use the official ANAF resource for the reporting period before evaluating a library, calculator or declaration wrapper. A project's popularity or claimed license does not establish its tax-year coverage, permitted reuse or correctness. The legacy catalogue is preserved below as unconfirmed leads; it is not the source of a current tax rule.

## Scope

Developers and accountants assessing declaration generation, PFA computations, VAT status checks or ANAF validation tooling for Romania. This is a reference-selection and reconciliation workflow. It does not authorize downloading or executing a repository, accessing a taxpayer account, transmitting tax data or filing anything.

The relevant detailed skills are ro-income-tax, ro-cas-cass, ro-payroll-social, ro-employee-income-tax, ro-vat-return and romania-einvoice. A sibling's structural pass does not establish that every rule remains current. In particular, the e-TVA notice procedures in ro-vat-return require the separately recorded [OUG 13/2026 art. IV point 1 repeal](https://static.anaf.ro/static/10/Anaf/legislatie/OUG_13_2026.pdf) correction; do not import those old notice thresholds into an integration.

## Ask the client first

Establish the job, taxpayer category, income source, reporting period, tax registration and accounting basis. Obtain the exact package/version/commit being considered, its actual license files and the output requiring reconciliation. For a declaration, identify the ANAF form and reporting period, schema and validator version, and whether the task is calculation, file generation, validation or submission. For a register integration, identify which status and effective date are required; a current response and historical transaction date can answer different questions.

Keep credentials and personal data out of a software-source comparison. A software recommendation is not permission to execute or submit.

## The method, step by step

1. **Select the official period-specific material.** The [ANAF D300 page](https://static.anaf.ro/static/10/Anaf/Declaratii_R/300.html) links the return assistance, Java assistance, validation annex and schema. Its current entry identifies Order 174/2026 for obligations starting in January 2026. Older entries remain on the same page: select by the obligation's reporting period, not by the first familiar filename.
2. **Distinguish the jobs and forms.** The [D112 page](https://static.anaf.ro/static/10/Anaf/Declaratii_R/112.html) covers social contributions, income tax and insured-person details; it has separate January and July 2026 reporting versions. The [D212 page](https://static.anaf.ro/static/10/Anaf/Declaratii_R/declaratie_unica.html) points to the current public annual-individual-return application. Its 2026 label includes the current filing cycle and CASS opt-ins, not proof that the eventual form for every item of 2026 income filed in 2027 has been issued. Keep that future form and its fields unconfirmed until actually published and read.
3. **Read the official technical constraints.** Match period, schema namespace, required fields, calculation checks and error messages against the authority's own linked documents. The D300 page says its Java assistance is for taxpayers generating their own XML. Do not infer that a community PDF generator implements the same version. This research has not run either an official or a third-party validator; no validation success is claimed.
4. **Recompute the law separately.** Technical acceptance can check a file's structure and internal arithmetic without establishing the transaction's actual facts, the correct tax base, an exemption or an election. Use the Fiscal Code and the relevant detailed skill. For example, the ordinary VAT rates are 21% and 11% only for supplies within their statutory categories; exemptions, reverse charge, transitional supplies and adjustments need their own analysis (art. 291). The default individual income-tax rate is 10% of the appropriate taxable base, subject to expressly different category rates (arts. 64 and 123). The examples below test the rate and base separately.
5. **Select a register by the actual question.** The [official ANAF web-service index](https://www.anaf.ro/anaf/internet/ANAF/servicii_online/servicii_web_anaf/) identifies the VAT registration, cash-accounting, split-payment and inactive/reactivated registers, among other services. Follow its actual technical documentation before asserting an endpoint, payload, authentication requirement or historical-date capability. No live taxpayer lookup was performed for this skill. An HTTP response or a package name alone is not proof of active registration or deduction entitlement.
6. **Assess the proposed dependency.** Read that exact version's license and dependency notices before deciding whether and how to reuse code. Retain the version and review record. The old catalogue's blanket compatibility claim, star counts, activity dates and license labels below have not been reconfirmed; they cannot authorize incorporation. A library can be useful for comparison while its calculations or licensing remain unresolved.
7. **Reconcile and stop on a mismatch.** Retain the legal inputs, independent expected result, package result and difference, the official form/schema/validator identity, and any actual validation message. Correct the calculation or explicitly hold the unsupported output before using it. Do not solve a legal mismatch by changing an example's facts to make a calculator agree. No installation, account access or filing follows automatically from this selection workflow.

### Legal anchors for computation checks

| Check | Rate and conditions | Source |
|---|---|---|
| Ordinary taxable VAT supply, no exemption or reduced-rate category | 21% of the statutory VAT base; CF art. 291(1) | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Supply established to fall within a reduced-rate category | 11% of its statutory base; CF art. 291(2); do not assume every good or service qualifies | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Ordinary annual self-employed income, taxable base already correctly established | 10%; CF arts. 64 and 123(1), with the separate social-contribution and deduction analysis completed first | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |

The old catalogue's 2024 calculator figures are historical leads, not an alternative source for these 2026 checks. CAS and CASS have different bases, thresholds and exemptions; use ro-cas-cass. In particular, the old claim that “CASS always applies” must not be used as a universal rule: art. 156 applies the rate only where the law imposes the contribution.

## Worked cases

### VAT adapter: detect a stale rate table

A test dataset contains an ordinary standard-rated supply with a RON 1,000 taxable base and a separately established reduced-rated supply with a RON 500 base. Assume the correct taxable event, no transitional rate, no exemption, no reverse charge and no adjustments. Current output tax is 1,000 × 21% + 500 × 11% = RON 265, derived. A legacy adapter configured to 19% and 9% returns RON 235 on those same facts, an understatement of RON 30, derived. Those legacy percentages are test configuration inputs, not current rates. Structural acceptance alone would not repair that configuration.

```oa-check
name: VAT adapter detects stale rate configuration
inputs:
  standard_base: 1000
  reduced_base: 500
  standard_rate: 0.21
  reduced_rate: 0.11
  legacy_standard_rate: 0.19
  legacy_reduced_rate: 0.09
steps:
  - expected_vat: standard_base * standard_rate + reduced_base * reduced_rate
  - adapter_vat: standard_base * legacy_standard_rate + reduced_base * legacy_reduced_rate
  - understatement: expected_vat - adapter_vat
expected:
  expected_vat: 265
  adapter_vat: 235
  understatement: 30
```

### PFA adapter: detect the wrong base despite the right percentage

The independently established annual taxable income for an ordinary real-system PFA case is RON 18,000, after the legally applicable deductions and contributions. This supplied taxable base is an input; this case does not decide CAS/CASS liability, thresholds or exemptions. The package mistakenly taxes RON 20,000, the net-income figure before those adjustments. At 10%, expected income tax is RON 1,800 and the package returns RON 2,000: overstatement RON 200, all derived. Using the right percentage has not made its base correct. The current annual-return form and its fields still need separate period-specific confirmation.

```oa-check
name: PFA adapter detects incorrect taxable base
inputs:
  verified_taxable_income: 18000
  adapter_base: 20000
  income_tax_rate: 0.1
steps:
  - expected_income_tax: verified_taxable_income * income_tax_rate
  - adapter_income_tax: adapter_base * income_tax_rate
  - overstatement: adapter_income_tax - expected_income_tax
expected:
  expected_income_tax: 1800
  adapter_income_tax: 2000
  overstatement: 200
```

## When to refuse or refer

Stop if the relevant reporting-period law, form, schema, actual license or transaction facts cannot be established, or if output disagrees with the independent computation. Do not present an unrun validator, an unreadable page, a development wrapper, a repository label or a historical popularity count as official certification. Route unresolved tax treatment to the relevant current-law skill and professional review; retain unavailable source details under the boundary below.

## Preserved legacy project catalogue: unconfirmed leads

The following catalogue records what the prior version said. Repository identities, all project topics and the earlier figures are retained for no-loss research history. None of its licenses, popularity/activity claims or functional coverage was reconfirmed in this official-source pass; none is an adoption recommendation or a current tax instruction. The quoted tax simplifications remain held where they conflict with the law or omit conditions.


**Historical assertions below are unconfirmed and unusable as current instructions.** The exact old catalogue is quoted for topic preservation; the workflow above governs any actual assessment.

> OpenAccountants is AGPL-3.0. MIT, Apache-2.0, GPL-3.0, and AGPL-3.0 content can all be incorporated with attribution. Projects below are license-compatible unless noted otherwise.
>
> ## Declarații ANAF
>
> - Repository: [IncrementalCommunity/declaratii-anaf](https://github.com/IncrementalCommunity/declaratii-anaf)
> - License: AGPL-3.0
> - Stars: 14
> - Language: Romanian
> - Scope: ANAF declaration validation and PDF generation for key Romanian tax forms including D100 (impozit pe venit), D106 (contribuții sociale), D112 (declarație privind obligațiile de plată), D390 (declarație recapitulativă TVA), and D394 (declarație informativă TVA).
> - Why it matters: AGPL-3.0 licensed with direct coverage of the most important ANAF declaration forms. Validation logic ensures compliance with ANAF's submission requirements.
> - Integration approach:
>   - AGPL-3.0 is the same license family as OpenAccountants. Content can be incorporated with attribution.
>   - Use as a reference for ANAF declaration XML/PDF structure, field validation rules, and form-specific computation logic.
>
> ## PFASimplu
>
> - Repository: [ClimenteA/PFASimplu](https://github.com/ClimenteA/PFASimplu)
> - License: verify before reuse
> - Stars: 35
> - Language: Romanian
> - Scope: Simplified accounting application for Romanian PFA (Persoană Fizică Autorizată) and II (Întreprindere Individuală) entities.
> - Why it matters: Addresses the most common small-business/freelancer entity types in Romania (PFA and II). The 35 stars suggest meaningful adoption in the Romanian developer community.
> - Integration approach:
>   - Reference for PFA/II bookkeeping workflows, norma de venit vs sistem real (lump-sum vs actual income), and ANAF reporting requirements for sole traders.
>   - Treat as reference-only until the license is confirmed.
>
> ## Taxe PFA
>
> - Repository: [taxepfa/taxepfa.github.io](https://github.com/taxepfa/taxepfa.github.io)
> - License: MIT
> - Stars: 38
> - Contributors: Active (last update March 2026)
> - Language: TypeScript / Romanian
> - Scope: Complete PFA (sole trader) tax calculator implementing 2024 rates: CAS (pension) 25%, CASS (health) 10%, income tax 10%. Handles tiered CAS thresholds (12× vs 24× minimum wage), CASS calculation, deductible expenses, multi-currency support (EUR/USD/GBP→RON via BNR rates), and VAT threshold tracking.
> - Why it matters: MIT-licensed, 38 stars, very actively maintained. Implements the exact PFA tax logic Romanian freelancers need: the CAS threshold system (no CAS under 12× min wage, 12× base between 12–24× min wage, 24× base above), CASS always applies, and 10% flat income tax after deductions.
> - Integration approach:
>   - MIT is fully compatible. Tax rate constants (CAS 25%, CASS 10%, income tax 10%), threshold logic, and deductible expense handling directly usable.
>   - Reference for Romanian PFA net income computation and VAT registration threshold tracking.
>
> ## ANAF VAT Verification
>
> - Repository: [itrack/anaf](https://github.com/itrack/anaf)
> - License: MIT
> - Stars: 151
> - Language: Romanian / English (PHP)
> - Scope: PHP library for the ANAF VAT verification REST API, implementing Art. 316 Cod Fiscal (TVA la încasare status, split TVA, inactive taxpayer checks).
> - Why it matters: MIT-licensed with strong adoption (151 stars). Provides programmatic access to ANAF's taxpayer verification service, which is essential for Romanian B2B invoicing compliance.
> - Integration approach:
>   - MIT is fully compatible. API integration patterns and Art. 316 verification logic directly usable.
>   - Reference for ANAF REST API endpoints, TVA status checks, and Romanian fiscal code validation.
>
> ## DUKIntegrator
>
> - Repository: [mihaikelemen/DUKIntegrator](https://github.com/mihaikelemen/DUKIntegrator)
> - License: MIT
> - Language: Romanian / English
> - Scope: Dockerised ANAF DUKIntegrator for declaration validation. Wraps ANAF's official Java-based validation tool in a container for automated validation workflows.
> - Why it matters: MIT-licensed containerised version of ANAF's official declaration validator. Useful for automated testing and CI/CD validation of generated declarations.
> - Integration approach:
>   - MIT is fully compatible. Docker setup and validation workflow patterns directly usable.
>   - Reference for ANAF declaration validation requirements, error codes, and submission pre-checks.

## Sources

| Source | Official URL | Read for / actual read date |
|---|---|---|
| ANAF D300 technical resources | https://static.anaf.ro/static/10/Anaf/Declaratii_R/300.html | 2026-11-15. Read for period-specific assistance, validator/schema links and the Java-assistance scope note. No software was run. |
| ANAF D112 technical resources | https://static.anaf.ro/static/10/Anaf/Declaratii_R/112.html | 2026-11-15. Read for distinct 2026 reporting-period entries and update dates. |
| ANAF D212 technical resources and public application | https://static.anaf.ro/static/10/Anaf/Declaratii_R/declaratie_unica.html | 2026-11-15. Read for current application routing and filing-cycle/CASS opt-in description; future 2026-income final form not assumed. |
| ANAF web-service index | https://www.anaf.ro/anaf/internet/ANAF/servicii_online/servicii_web_anaf/ | 2026-11-15. Read for the named register/service groups; endpoint contracts and live taxpayer responses not tested. |
| OUG 13/2026, e-TVA repeal | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_13_2026.pdf | 2026-11-15. Read for art. IV point 1 and neighboring provisions including VII; the latter delays other named provisions, not this repeal. |
| Fiscal Code, ANAF consolidation | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-11-15. Read for arts. 64, 123, 156 and 291, with neighboring conditions; the consolidation is not an official republication. |

Not yet confirmed: every third-party project license, dependency permission, popularity/activity figure, implementation/version and functional-coverage claim in the preserved legacy catalogue; the eventual final annual-return form for 2026 income filed in 2027; exact current software payload/field constraints beyond the official entries actually read; unperformed official or third-party validation and taxpayer-register requests. The passing VAT sibling contains obsolete e-TVA notice rules separately identified during this work; do not use those instructions until corrected. No source unreadable or unrun step is represented as verified.
