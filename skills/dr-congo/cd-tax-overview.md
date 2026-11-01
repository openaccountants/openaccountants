---
name: cd-tax-overview
description: "Route a DR Congo tax engagement for 2026 to the correct source-bound country workpapers. Use this Guide when asked about Congo tax, company versus individual taxation, registering a business, employer obligations, VAT, related parties or payments abroad. It separates legal formation, company source and individual residence, identifies the evidence needed before calculation, and builds a filing and payment control register. It links the existing figure homes instead of duplicating their rates, bands or deadlines. Two recomputing cases demonstrate a supported profit bridge and a payment-allocation decision. The output is an intake and preparation plan. All seven tax domains remain partial; carried law, specialist calculations and authenticated filing must be resolved before reliance."
jurisdiction: CD
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: orchestrator
version: 1.0
tax_year_notes: "2026 research and preparation only; stated national-law, carried-law, implementation and filing holds remain."
---

# DR Congo tax overview: intake and routing method v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

**RESEARCH HOLD.** This is a 2026 intake and routing method. It does not consolidate every tax, certify an operative-law chain or prepare a return by itself. The six calculation workpapers have accepted source review within their recorded conditional scopes. Their legal, implementation and filing holds still apply. All seven tax domains remain partial. Finance Law 25/060 article 16 carries specified 2025 provisions into 2026; those provisions are not fully reconciled. [25/060 art.16](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf); [country gap register](README.md).

Start with the legal person, activity, income period, residence/source, employees and transaction types. Do not use the old overview's blanket “territorial” claim for every taxpayer: the company source rule and the individual's habitual-residence/global-income rule are different. DGI's public pages identify its IS, IRPP and VAT services; CNSS is a separate social-security institution. [23/053 arts.7,58–60](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf); [DGI services](https://dgi.gouv.cd/taxe-sur-la-valeur-ajoutee-tva/); [CNSS](https://cnss.cd/?page_id=1388).

## Ask the client first

- Is this an individual, existing company, company being formed, foreign branch or another entity, and what documents prove its form and registration?
- What income year, activity locations, residence facts, establishments and foreign income are involved?
- What goods/services, exports/imports, related-party transactions and payments to nonresidents occurred, with contracts and transaction dates?
- Are there workers, directors or expatriate/seconded staff, and who employs, pays and directs them?
- What records, prior returns, tax-office instructions, assessments, payment references and filing acknowledgements exist?

## The method, step by step

### 1. Identify the person and registration job

For formation, legal form, subscribed/paid capital, governance, registered office, RCCM and post-formation registration evidence, use [company formation](cd-company-formation.md). A corporate registration is a legal fact, not proof that every tax or employer registration is complete. OHADA articles 97–98 connect company legal personality to RCCM registration, subject to the Act's exceptions. The cited 2026 Procedures Law replacement separately requires a tax-number request and location plan after activities begin. Keep the [formation Guide's registration schedule](cd-company-formation.md#deadlines-and-filing) as the home of that deadline. [AUSCGIE arts.97–98](https://biblio.ohada.org/doc_num.php?explnum_id=2032); [25/060 art.17](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf).

### 2. Select the income-tax workpaper

| Intake condition | Workpaper and what to carry into it | Primary source for the routing rule |
|---|---|---|
| Company or other entity whose form/activity is within IS | [Corporate income tax](cd-corporate-income-tax.md): form, territory, exemptions, accounting result, supported adjustments, losses, minimum comparison and payment schedule | [23/053 arts.3–9](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf) |
| Individual with habitual residence or Congolese-source income | [Individual income tax](cd-income-tax.md): residence/source, each net category, supported deductions, family facts and withholding; salary is not the only category | [23/053 arts.58–60,67](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf) |
| Foreign company, branch or cross-border individual facts | Establish the applicable company source/PE or individual residence rule, then treaty and specialist work. The payment Guide does not replace a complete PE, residence or foreign-credit analysis | [23/053 arts.7–8,58–62](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf) |

The corporate Guide owns its profit rate, turnover minimum, tax period and annual declaration date. The individual Guide owns its annual bands, ceiling, family/minimum interactions and individual-return date. Use those current, hash-bound versions and their holds, rather than copying numbers into a second table. In particular, distinguish the individual return from the separate employer salary report. [23/053 arts.12,118–125](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf); [25/060 arts.18,20,22](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf).

### Rates, bands and thresholds

This routing table names the figure homes. It deliberately carries no duplicate rate, band or threshold values.

| Figure family | Owning workpaper and required scope check | Official source |
|---|---|---|
| Company rate and minimum | [Corporate Guide](cd-corporate-income-tax.md#rates-bands-and-thresholds), after entity, period and ordinary/special-regime classification | [23/053 arts.3–9,56–57](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf) |
| Individual scale, ceiling and family/minimum interaction | [Individual Guide](cd-income-tax.md#rates-bands-and-thresholds), after residence, category and family facts | [23/053 arts.58–60,118–125](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf) |
| VAT rate/version and registration threshold | [VAT Guide](cd-vat-gst.md#rates-bands-and-thresholds), after period, product/service, option and implementation evidence | [25/060 art.46](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf); [26/032 art.13](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lfr_2026/lfr_2026_recettes.pdf) |
| Employer and worker contributions/levies | [Payroll Guide](cd-payroll-social.md#rates-bands-and-thresholds), after branch, remuneration and special-worker facts | [18/041 arts.2–6](https://cnss.cd/wp-content/uploads/2024/04/Recueil-de-textes-legal-reglementaires-et-mesures-dexecution-de-la-loi-16-009-du-15-juillet-2016-1.pdf); [23/053 arts.145–149](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf) |

### 3. Add transaction and employer workstreams

| Trigger to investigate | Route | Evidence and boundary |
|---|---|---|
| Taxable supplies, turnover/profession status, self-supplies, exports or imports | [VAT](cd-vat-gst.md) | Invoice, tax point, tariff/description, option/registration and deduction evidence. Original and August rate versions must be distinguished; the VAT Guide owns all figures | [25/060 arts.45–50](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf); [26/032 arts.12–13,49–51](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lfr_2026/lfr_2026_recettes.pdf) |
| Employment or employer-borne expatriate charge | [Payroll and social contributions](cd-payroll-social.md) | Worker status, pay components, CNSS branch/base, withholding, employer levy and separate return evidence. Do not treat employer charges as an employee income-tax credit | [23/053 arts.119,145–149](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf); [16/009 art.19; Regulation 146 arts.17–31](https://cnss.cd/wp-content/uploads/2024/04/Recueil-de-textes-legal-reglementaires-et-mesures-dexecution-de-la-loi-16-009-du-15-juillet-2016-1.pdf) |
| Linked enterprises or controlled transactions | [Transfer pricing](cd-transfer-pricing.md) | Relationship, transaction delineation, pricing support and group/local reporting tests. Do not infer absence of documentation from own turnover alone | [23/053 art.53](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf); [25/060 arts.25–27](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf) |
| Foreign service provider or passive-income recipient | [Cross-border payments](cd-cross-border.md) | Recipient residence, contract, service/rights/passive classification, payment/availability date and treaty/sector evidence; income-tax withholding and VAT are separate jobs | [23/053 arts.142–144](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf); [26/032 arts.14–19](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lfr_2026/lfr_2026_recettes.pdf) |

A trigger opens a workstream; it does not by itself prove liability, an exemption or a filing duty for that person. Keep unresolved source, treaty and category questions on the engagement's hold list. No property, customs, excise, provincial or specialist-sector completeness is claimed by this map.

### 4. Build the working-paper and deadline register

Keep one row per obligation with the legal person, income/transaction period, governing article/version, competent office, prescribed form, evidence, base/calculation link, due-date source, paid amount, submission reference and acceptance receipt. Consult the owning Guide for the actual date and current holds. Do not let the old overview's personal “recapitulative” date drive either the individual or employer calendar. The enacted 2026 provisions distinguish those obligations. [25/060 arts.18,20,22](https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf).

Use Congolese-franc accounting where required by the cited company-accounting rule, and establish conversion evidence separately for foreign-currency documents. A CFA-denominated OHADA capital rule is not a CDF exchange rate. Calendar-year language in the corporate Guide also carries first-period and cessation exceptions; do not impose a universal year-end from a headline. [23/053 arts.12,141](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf); [formation capital notes](cd-company-formation.md).

### 5. Reconcile and hand over

Reconcile the accounting data, category/source schedules and bank payments to their owning workpapers. Keep deductions, withholding credits, instalments and employer contributions separate. The examples below show that reconciliation arithmetic; they do not decide tax rates or the legal eligibility of an assumed adjustment. An amount in a bank statement cannot prove that it was allocated to the correct person, period or tax. Annual IRPP withholding-credit treatment has its own source and conditions. [23/053 arts.9,67,121](https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf).

## Worked cases

### 1. A company result is ready for the corporate workpaper, not a tax bill

Assume a company's supported period schedule shows CDF 120,000,000 revenue and CDF 90,000,000 accounting costs. A separate, completed source analysis has established CDF 2,000,000 of add-backs and CDF 500,000 of allowable downward adjustments. Accounting profit is CDF 30,000,000; the draft adjusted-profit input is CDF 31,500,000. Send that bridge, the independently established turnover and every adjustment source to the corporate Guide. Do not apply a tax rate here or approve the adjustments from their labels. Its minimum, rounding, instalment and legal-chain checks remain necessary.

```oa-check
name: Supported company profit bridge passed to the owning workpaper
inputs:
  revenue: 120000000
  accounting_costs: 90000000
  independently_established_addbacks: 2000000
  independently_established_downward_adjustments: 500000
steps:
  accounting_profit: revenue - accounting_costs
  draft_adjusted_profit: accounting_profit + independently_established_addbacks - independently_established_downward_adjustments
expected:
  accounting_profit: 30000000
  draft_adjusted_profit: 31500000
```

### 2. Decision: reconcile the bank debit before claiming a payment credit

Assume CDF 6,000,000 left a company's bank account. Official references independently allocate CDF 2,000,000 to company tax, CDF 1,500,000 to VAT, CDF 1,000,000 to employer payroll/social obligations, and CDF 500,000 to an individual's withholding. The references explain CDF 5,000,000; CDF 1,000,000 remains unallocated. Route each supported amount to its own workpaper and investigate the balance. Claiming the whole debit in the company-tax reconciliation would over-allocate CDF 4,000,000 to that job. This case assumes the listed allocations are established, not that payment alone creates a tax credit or proves return acceptance.

```oa-check
name: Payment allocation decision prevents cross-tax over-credit
inputs:
  bank_debit: 6000000
  company_tax_reference: 2000000
  vat_reference: 1500000
  employer_reference: 1000000
  individual_withholding_reference: 500000
steps:
  supported_allocations: company_tax_reference + vat_reference + employer_reference + individual_withholding_reference
  unallocated_balance: bank_debit - supported_allocations
  company_overallocation_if_whole_debit_used: bank_debit - company_tax_reference
expected:
  supported_allocations: 5000000
  unallocated_balance: 1000000
  company_overallocation_if_whole_debit_used: 4000000
```

## When to refuse or refer

Stop before final computation or filing where the relevant law chain, residence/PE, treaty, sector rule, category-net amount, adjustment eligibility, current form or authenticated acceptance is unresolved. Route formation and regulated activities for the required legal/licensing work. Preserve the six accepted Guides and their review evidence; a local calculation or a 2026 label does not expand their accepted scope. A source gap is not proof that a tax does not exist.

## Filing and payment

Use the [corporate](cd-corporate-income-tax.md#deadlines-and-filing), [individual](cd-income-tax.md#deadlines-and-filing), [VAT](cd-vat-gst.md#deadlines-and-filing), [payroll](cd-payroll-social.md#deadlines-and-filing), [pricing](cd-transfer-pricing.md#deadlines-and-filing) and [nonresident-payment](cd-cross-border.md#deadlines-and-filing) schedules. Resolve each stated form/currentness hold. Public portal links are entry points, not a verified submission sequence. Keep both the actual return acknowledgement and payment/credit evidence before reporting completion.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| 23/053 arts.3–9,12,56–62,67,118–126,141–149; company versus individual scope, profit/category distinction and payer obligations. Other-category computations are not reconstructed | https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf | 2026-11-01 |
| 25/060 arts.16–22,25–27,45–50,88; carried-law hold, registration/return distinctions and route triggers, not all carried 2025 provisions or annexes | https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf | 2026-11-01 |
| 26/032 arts.12–19,49–51; VAT/nonresident version changes and commencement, no full-country consolidation | https://www.budget.gouv.cd/wp-content/uploads/budget2026/lfr_2026/lfr_2026_recettes.pdf | 2026-11-01 |
| AUSCGIE arts.97–98; legal personality is distinct from tax registrations | https://biblio.ohada.org/doc_num.php?explnum_id=2032 | 2026-11-01 |
| CNSS collection, 16/009 art.19 and Regulation 146 arts.17–31; employer liability, base and declaration distinctions | https://cnss.cd/wp-content/uploads/2024/04/Recueil-de-textes-legal-reglementaires-et-mesures-dexecution-de-la-loi-16-009-du-15-juillet-2016-1.pdf | 2026-11-01 |
| CNSS institutional Presentation §1, institutional legal personality, public status and supervision | https://cnss.cd/?page_id=1388 | 2026-11-01 |
| DGI public page/navigation in the cached VAT page, identifying IS/IRPP/VAT services; no authenticated filing | https://dgi.gouv.cd/taxe-sur-la-valeur-ajoutee-tva/ | 2026-11-01 |

Not yet confirmed: the full carried 2025/current-law and implementing-order chains, all specialist sectors/provincial and other taxes, complete residence/PE/foreign-credit/exit methods, all exceptions and category calculations, current form/portal mandates and authenticated filing/credit allocation. The seven partial-domain entries and all owning-Guide holds remain in force. This router creates no new comprehensive coverage or accountant attestation.


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
