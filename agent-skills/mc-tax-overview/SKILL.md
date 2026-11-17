---
name: mc-tax-overview
description: "Monaco tax overview for 2026 routing individual, business profits, VAT, payroll, social contribution, transfer pricing, cross border and formation questions to the detailed country Guides. Highlights the inclusive foreign turnover boundary, separate rights income scope, French national residence rules, dated October contribution changes and company reform transition limits. Use as the country entry point before preparing a working paper. Names specialist, formation implementation and professional review boundaries and avoids a general zero tax promise. Source cited draft with no named Monaco professional sign off."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mc-tax-overview"
  jurisdiction: "MC"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Monaco tax overview and routing v1.4

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** The unchanged source research and independent review of 25 October 2026 are reused after a 16 November applicability check; changed dependencies are checked separately. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Scope

This overview routes 2026 questions to the detailed Guides. It is not a complete tax computation and does not replace the [applicability and scope register](README.md). All eight Guides are tier 2 source-cited drafts. No named Monaco professional review has been obtained.

## Ask the client first

- What person or entity, nationality and residence facts are involved?
- What activity, income or transaction needs a decision, and where is it used or carried out?
- Which tax year, transaction date or contribution period applies?
- What foreign turnover, ownership, permissions and source documents are available?

## The method, step by step

1. Establish the required facts before choosing a tax.
2. Load each relevant Guide below, using the headline solely to identify the route.
3. Reconcile shared facts for mixed cases and apply the specialist Guide's confirmed method and limitations.

| Question | Starting point | Guide and official source |
|---|---|---|
| Resident personal income tax | Government describes absence within genuine residence/activity scope; French convention and other states remain material | [Individual income tax](mc-income-tax.md), [Government fiscal paragraphs](https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco) |
| Business profits tax | Industrial/commercial enterprises of any form meet the ordinary foreign-turnover gate at **at least 25%**; a separate rights-income limb applies | [ISB](mc-corporate-income-tax.md), [Arts. 1–4](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Ordinary ISB rate | 25% from 1 January 2022 | [ISB](mc-corporate-income-tax.md), [Art. 21](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Ordinary VAT | Standard 20%; Monaco Code and Monaco DSF procedures | [VAT](monaco-vat.md), [Arts. 51, 70, A-139, A-144](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Employees and contributions | Separate component ceilings; October 2026 changes apply only from their stated dates | [Payroll/social](mc-payroll-social.md), [Dated tables](https://www.caisses-sociales.mc/accueil/employeur/employeur/employeur-a-titre-professionnel/cotisations) |
| Foreign commercial/financial terms | Normal-conditions adjustment, broader first limb than ownership-only related-party tests | [Transfer pricing](mc-transfer-pricing.md), [Art. 14](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Foreign tax, residence and departure | Evidenced same-income credit, French treaty screening and cessation rules require separate decisions | [Cross-border](mc-cross-border.md), [Arts. 22–23, 29](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Incorporation | Current Code plus 2025 and October 2026 reform/transition rules | [Formation](mc-company-formation.md), [Arts. 35-1–35-3](https://legimonaco.mc/code/code-commerce/), [Arts. 93–103](https://legimonaco.mc/tnc/loi/2026/10-09-1.596/) |

## Worked cases

An illustrative industrial/commercial enterprise has EUR 400,000 relevant turnover, including EUR 100,000 foreign operations classified under article 3. The foreign share is exactly 25%, so it meets article 1(1)(a)'s inclusive turnover gate. Separately assume that the specialist computation has established EUR 100,000 taxable profit, without a relief or credit: the ordinary 25% rate gives EUR 25,000 ISB. The turnover gate does not make foreign turnover the taxable-profit base. The separate rights-income limb must still be considered where relevant ([Ordinance 3.152 arts. 1-4, 21](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152)).

```oa-check
name: Monaco inclusive foreign-turnover gate and separately established profit
inputs:
  total_relevant_turnover: 400000
  foreign_operations_turnover: 100000
  scope_fraction: 0.25
  assumed_taxable_profit: 100000
  ordinary_rate: 0.25
steps:
  - foreign_fraction: foreign_operations_turnover / total_relevant_turnover
  - turnover_at_boundary: total_relevant_turnover * scope_fraction
  - ordinary_isb: assumed_taxable_profit * ordinary_rate
expected:
  foreign_fraction: 0.25
  turnover_at_boundary: 100000
  ordinary_isb: 25000
```

## When to refuse or refer

Classify the person, activity, country, dates and transaction before choosing a tax. No Monaco personal income tax does not mean no ISB for a sole trader, no VAT, no social contributions, no estate/transaction duties or no foreign liability. Foreign turnover is an ISB scope gate; foreign-operation base exclusions are a separate statutory test. A residence card and a tax certificate are also separate. [Arts. 1–4](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152); [Arts. 1–4](https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/); [Government scope](https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco).

The new-activity exemption is conditional and period-specific; there is no general promise of two tax-free years for every new company. The ordinary VAT franchise requires prior/current national turnover, activity, exclusions and start-date checks. Do not classify purchases, exemptions or deduction from a bank name. [Arts. 1–3](https://legimonaco.mc/tnc/ordonnance/1991/10-17-10.324); [Arts. 42, 87–91](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

### Dates and evidence

Law, government guidance and retrieval are distinct evidence. The ISB statute says at least 25%, despite the government summary's stricter wording. The 16 November consolidation also identifies Ordinance 12.211 of 23 October 2026 on period/advance and penalty provisions; the scope/rate and other overview pinpoints were checked separately and remain applicable. Do not use an older ISB penalty or period method without the current specialist text. At the 25 October source read, the employer PDF URL said October 2025 while serving October 2026. Dated archived 2025 employer/independent letters and native annual instruments establish the earlier 2026 periods; do not backdate the October rates. The full-year tables and effective-date changes are in the payroll/social Guide. The minimum-tax page is a project record; proposed dates do not establish operative law. The [preserved completion research](../../evidence/research/monaco-2026/completion-research.md) records the expanded source reading, calculations and fresh review. The earlier public [research report](../../docs/research/2026-10-24-monaco-research.md) and [retrieval register](../../docs/research/2026-10-24-monaco-sources.json) preserve those distinctions. [Art. 1](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152); [Actual employer letter](https://www.caisses-sociales.mc/content/download/3439/file/Lettre_information_aux_employeurs_octobre_2025.pdf); [Project 1.129](https://legimonaco.mc/projet/1.129).

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Government fiscal paragraphs, genuine establishment/activity, French convention and foreign-law limits; original browser read reused, same scope paragraphs re-read on 2026-11-16 | https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco | 2026-10-25 |
| Ordinance 3.152, arts. 1–4, 14, 21–23, 29; these pinpoints checked for unchanged text on 2026-11-16 after the consolidation changed elsewhere; original source read/review reused | https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152 | 2026-10-25 |
| Ordinance 10.324, arts. 1–3; unchanged official visible text checked on 2026-11-16, original review reused | https://legimonaco.mc/tnc/ordonnance/1991/10-17-10.324 | 2026-10-25 |
| Code, arts. 42, 51, 70, 87–91; annex A-139, A-144; unchanged official visible text checked on 2026-11-16, original review reused | https://legimonaco.mc/code/code-taxes-chiffre-affaires | 2026-10-25 |
| Caisses Sociales, dated contribution tables | https://www.caisses-sociales.mc/accueil/employeur/employeur/employeur-a-titre-professionnel/cotisations | 2026-10-25 |
| October 2026 employer letter, filename discrepancy | https://www.caisses-sociales.mc/content/download/3439/file/Lettre_information_aux_employeurs_octobre_2025.pdf | 2026-10-25 |
| Ordinance 8.566, arts. 1–4; unchanged official visible text checked on 2026-11-16, original review reused | https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/ | 2026-10-25 |
| Code de commerce, arts. 35-1–35-3; unchanged official visible text checked on 2026-11-16, original review reused | https://legimonaco.mc/code/code-commerce/ | 2026-10-25 |
| Law 1.596, arts. 93–103; unchanged official visible text checked on 2026-11-16, original review reused | https://legimonaco.mc/tnc/loi/2026/10-09-1.596/ | 2026-10-25 |
| Project 1.129, project status only | https://legimonaco.mc/projet/1.129 | 2026-10-25 |

The earlier government personal-tax retrieval and failed recheck remain in the historical register. Its substantive fiscal paragraphs were freshly read in a normal browser on 25 October, as were the government ISB filing and e-TVA onboarding steps. A browser read does not imply that the linked form PDFs or a taxpayer portal were submitted.

| Ordinance 12.211 of 23 October 2026, affected period/advance and penalty provisions and art. 4 commencement read; outside the overview calculation | https://legimonaco.mc/tnc/ordonnance/2026/10-23-12.211/ | 2026-11-16 |

**Not yet confirmed:** the specialist schemes listed in the README, complete formation/accounts/audit implementation, operative multinational minimum-tax calculations and named professional sign-off. Ordinary filing procedures are documented; no taxpayer return was filed or account accessed. Arithmetic checks establish arithmetic only.

> Contributed by Michael Cutajar.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mc-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mc-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
