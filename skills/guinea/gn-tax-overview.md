---
name: gn-tax-overview
description: "Guinea tax routing and cross-workpaper control for 2026. Use it before combining individual salary tax, corporate IS and IMF, VAT, CNSS, property or formation results. It identifies the correct country job, the governing-source-version prerequisite, the inputs still missing and the distinction between a tax year, a payment date and a credit balance. Rates and statutory thresholds stay in the domain Guides so a summary cannot silently contradict them. Two executable cases reconcile imported, independently validated liabilities without creating a new tax-rate table. The pack remains partial: transfer pricing, complete cross-border relief, specialised personal/company/VAT methods, employer-tax base reconciliation and parts of formation/reporting remain unresolved. AI review does not provide accountant attestation."
jurisdiction: GN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: orchestrator
version: 1.1
---

# Guinea tax routing and workpaper controls v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Start here to identify the Guinea job and assemble a combined working file. Read the [pack scope](README.md) before treating any domain as complete. The enacted CGI uses categorical taxes and distinct corporate, property and VAT systems; CNSS social contributions and company registration/reporting have separate sources and authorities. This is a router and reconciliation control, not a substitute for those computations. [CGI contents and art. 1](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis contents](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx); [CNSS](https://cnss.gov.gn/cotisations-sociales-employeurs/); [OHADA Act](https://biblio.ohada.org/doc_num.php?explnum_id=2032).

Establish the operative law and administrative interpretation for each actual period. The enacted base and cited finance-law amendments plus April 2026 DGI guidance are available, but the October rectifying-law promulgation/effect is not retrieved. A current date in frontmatter is not evidence that every provision remained unchanged. If the governing version is unresolved, keep hypothetical source-version analysis separate and stop before live filing/payment or compliance conclusions.

## Rates, bands and thresholds

Rates have one home. Load the owning Guide and its exact conditions instead of copying a headline rate into this overview. The statutory references below identify each route; they do not establish an unresearched special regime.

| Job | Owning method and rate/threshold source | Official source |
|---|---|---|
| Individual income and salary | [Individual](gn-income-tax.md): residence, categorical routing, monthly ITS; full non-employment/pension/foreign methods remain partial | [CGI 1,4,15,51-80](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Corporate profits and IMF | [Corporate](gn-corporate-income-tax.md): regime classification, profit bridge, ordinary loss, IMF and distinct payment-credit buckets | [CGI 219-246](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §1.2](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx) |
| VAT | [VAT](gn-vat-gst.md): registration, rate boundaries, timing, input limitations, return and credit/refund controls; [invoice fields](gn-vat-invoice-control.md) | [CGI 358-388](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [LFI 2025](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf) |
| Payroll social contributions | [CNSS](gn-payroll-social.md): ordinary contribution base and shares, registrations and source-conflict control; salary ITS is owned by the individual Guide | [CNSS contribution guidance](https://cnss.gov.gn/cotisations-sociales-employeurs/) |
| Property | [CFU](gn-property-tax.md): liability, ordinary valuation and rent-withholding routes under its governing-version prerequisites | [CGI 257-274](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §4.1](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx) |
| Formation and registry reporting | [Formation](gn-company-formation.md): entity choice, capital, APIP route evidence and annual company-law control | [AUSCGIE](https://biblio.ohada.org/doc_num.php?explnum_id=2032) |
| Transfer pricing and complete cross-border relief | Unresolved dedicated methods; scope/withholding pointers in sibling Guides do not replace documentation, treaty and relief analysis | [DGI précis §1.2.3.5 and cross-border sections](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx) |

## The base

1. Identify the taxpayer, legal form, income/supply category, residence/establishment, staff and property. Route each job separately before combining outputs. Residence and worldwide/source taxation must follow the relevant categorical/business rules; the old unqualified worldwide-income summary is not a complete method. [CGI 1,4,15-15 ter](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
2. Record legal period and payment window separately. The ordinary business accounting/tax year is the calendar year with first-period exceptions; salary and VAT use monthly calculations/returns. A filing date in the following year does not change which year's tax or credit it belongs to. [CGI 63,91,236,246,373 sexies](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
3. Use GNF for local-law figures and preserve the original currency/unit/date on foreign evidence. Obtain the applicable exchange-rate rule and official rate before converting; this router supplies no exchange-rate number. The Code's monetary figures are denominated in Guinean francs. [CGI 63,229,244](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
4. Import only domain workpapers whose assumptions, governing version, evidence and unresolved items have been reviewed for the actual facts. Label inputs as validated, hypothetical or unresolved. A hypothetical arithmetic agreement is not a validated filing conclusion.
5. Keep gross salary, employee deductions, employer expense, tax withheld, tax paid and refundable/carried/non-transferable credits separate. The employer pays both employee and employer CNSS shares; the employee share is already inside gross salary, while the employer share is additional employer cost. [Social Security Code art. 34 and CNSS debtor guidance](https://cnss.gov.gn/cotisations-sociales-employeurs/).
6. Keep prior-year IS settlement, current-year IMF and actual cash instalments in separate tax-year buckets. Load the corporate method before offsetting anything: its same-year IMF rule does not let a January payment settle an unrelated prior-year balance. [CGI 236,246](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
7. Produce a job list with inputs, legal source/version, computed amount, period, due date, preparer/reviewer, filing/payment status and unresolved actions. Record who performed any actual filing and retain its receipt. Neither this document nor an AI review creates a licensed accountant's attestation.

## Deadlines and filing

There is no general country-wide annual return date to apply to every taxpayer and tax. Use each domain's sourced calendar. The historical overview's general individual-return date and old VAT date are replaced by the actual salary, corporate and VAT methods linked above. Keep CNSS's decree/agency deadline conflict visible rather than copy the salary-tax deadline into social security. [CGI 72,76,108,241,246](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [LFI 2025](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf); [CNSS](https://cnss.gov.gn/cotisations-sociales-employeurs/).

The DGI is the tax administration identified on its current official précis; CNSS administers the general social-security regime. Formation and registry evidence comes from APIP/RCCM procedures and company law. Use the correct authority and verified process for each job; this router does not submit a form or authenticate a portal session. [DGI official précis](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx); [CNSS](https://cnss.gov.gn/cotisations-sociales-employeurs/); [APIP](https://apip.gov.gn/comment-creer-mon-entreprise/).

## Penalties and interest

Load the penalty rule for the actual tax, period and procedure. Do not transfer a CNSS surcharge into VAT/ITS or assume a deadline dispute has already been resolved. Keep notices, principal, due dates, payment dates and the applicable appeal/relief process with the domain file. Full country dispute and sanction coverage remains a gap.

## Cross-border points

Separate tax residence, salary work location, company permanent establishment, VAT territory/recipient liability, withholding recipient status and social posting approval. One does not establish the others. Treaty relief and foreign credits require an actual applicable instrument and facts; the pack's partial source-based pointers are not a complete cross-border method. [CGI 4,15-15 ter,51,187-198,231-232,361 ter-duodecies](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Two worked examples that recompute

The first case checks period allocation, using imported validated workpaper amounts. Prior-year IS settlement GNF 15,000,000 is due in the current cash window. Current-year IMF paid is GNF 40,000,000 and the current-year June gross instalment is GNF 30,000,000, with no other credits. Applying current-year IMF to that current-year instalment leaves no June cash for it and GNF 10,000,000 IMF for the same year's later IS. The separate prior-year GNF 15,000,000 remains payable. The corporate Guide owns the legal credit rule; these hypothetical inputs create no new rate.

```oa-check
name: Keep tax-year buckets separate when allocating IMF
inputs:
  prior_year_settlement: 15000000
  current_year_imf_paid: 40000000
  current_year_gross_instalment: 30000000
steps:
  - current_imf_used: min(current_year_imf_paid, current_year_gross_instalment)
  - current_instalment_cash: current_year_gross_instalment - current_imf_used
  - current_imf_remaining: current_year_imf_paid - current_imf_used
  - cash_due_in_window: prior_year_settlement + current_instalment_cash
expected:
  current_instalment_cash: 0
  current_imf_remaining: 10000000
  cash_due_in_window: 15000000
```

The second case reconciles an imported payroll/payment file. Gross cash wages are GNF 10,000,000, employee CNSS GNF 125,000, ITS GNF 747,500, employer CNSS GNF 450,000 and separately validated VAT payable GNF 2,000,000. Assume all these remittances actually fall in the selected cash window. Cash to the worker is GNF 9,127,500; CNSS receives GNF 575,000; ITS receives GNF 747,500. Including VAT gives total outflow GNF 12,450,000, equal to gross wages plus employer CNSS plus VAT. Adding employee deductions again to gross wages would double count them. Other employer taxes/costs are outside these assumed validated inputs and must be added only after their own workpaper is complete.

```oa-check
name: Reconcile payroll cash without adding employee deductions twice
inputs:
  gross_wages: 10000000
  validated_employee_cnss: 125000
  validated_its: 747500
  validated_employer_cnss: 450000
  validated_vat_payable: 2000000
steps:
  - worker_cash: gross_wages - validated_employee_cnss - validated_its
  - cnss_payment: validated_employee_cnss + validated_employer_cnss
  - total_outflow: worker_cash + cnss_payment + validated_its + validated_vat_payable
  - independent_cost_check: gross_wages + validated_employer_cnss + validated_vat_payable
  - reconciliation_difference: total_outflow - independent_cost_check
expected:
  worker_cash: 9127500
  cnss_payment: 575000
  total_outflow: 12450000
  reconciliation_difference: 0
```

## Ask the client first

- What person/entity, activity, residence/establishment, income/supply, staff and property facts define the jobs?
- Which exact tax periods and cash/filing windows are being assembled?
- Which domain computations, source versions, elections/approvals and independent evidence have been validated?
- What returns, payments, withholding certificates and credit balances already exist, by tax and year?
- Which notices, missing facts, source failures or unresolved methods prevent a live conclusion?

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [DGI enacted CGI base](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf), cover/contents and the domain clauses identified in the linked Guides, including arts. 1,4,15,63,91,236,246 and separate VAT/property routes. This router does not assert a current consolidated Code. | 2026-11-01 |
| [DGI Précis fiscal 2026, version 10 April](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx), cover/contents and relevant categorical/corporate/property/VAT explanations read for the sibling methods. | 2026-11-01 |
| [LFI 2025](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf), cited electronic/filing amendments; the sibling methods preserve exact article and source hierarchy. | 2026-11-01 |
| [CNSS current contribution page](https://cnss.gov.gn/cotisations-sociales-employeurs/), entire operative contribution, debtor and due-date sections through an ordinary browser capture; Social Security Code art. 34 is read in the payroll method. | 2026-11-01 |
| [OHADA company Act](https://biblio.ohada.org/doc_num.php?explnum_id=2032), arts. 137-140 and 269 with neighbours; [APIP formation procedure](https://apip.gov.gn/comment-creer-mon-entreprise/), current route and output controls. Full detailed accounting standards remain a separate gap. | 2026-11-01 |

Not yet confirmed: the pack's actual-period source-version and October promulgation/effect gaps; complete non-salary personal, specialised corporate/VAT and employer-tax base methods; dedicated TP and full cross-border/treaty/foreign-credit methods; detailed accounting/reporting/audit and formation exceptions; all sanctions/appeals and authenticated portal processes. The [README](README.md) names the domain-level partial coverage. This router does not make those gaps disappear.

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
