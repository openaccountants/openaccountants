---
name: ivory-coast-payroll
description: >
  Use this skill to run payroll in Côte d'Ivoire (Ivory Coast) for 2026: salary tax withholding, employee and employer CNPS, CMU, the employer taxes on pay at 2.8% for local staff and 12% for expatriates, FDFP levies, the SMIG, monthly deadlines by taxpayer type and annual filings. It suits employers, payroll providers and accountants with staff in Abidjan or elsewhere in the country. Trigger on "payroll Ivory Coast", "bulletin de paie", "contribution employeur", "FDFP", "etat 301", "salaire net", "cost of an employee in Côte d'Ivoire". It links to the income tax and social contributions skills for the scale and the CNPS rules.
version: 0.2
jurisdiction: CI
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Côte d'Ivoire (Ivory Coast) Payroll v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it without checking the cited official source or a licensed professional.

Tax year 2026. Pay in XOF, monthly.

## Who this applies to

Employers with staff in Côte d'Ivoire. This skill runs the payslip and the employer's tax. The ITS scale and RICF are owned by [Income tax](ivory-coast-income-tax.md); CNPS rules by [Social contributions](ivory-coast-social-contributions.md). A TCE payer's tax replaces ITS and the employer contribution.

## Rates, bands and thresholds

| Item | Local | Expatriate | Conditions | Source |
|---|---|---|---|---|
| Employer contribution CE | exempt | 9.2% | Art. 146 | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf |
| Contribution nationale CN | 1.2% | 1.2% | Art. 146 | same |
| Taxe d'apprentissage | 0.4% | 0.4% | Art. 143, 146; FDFP | same |
| Continuing training tax | 1.2% | 1.2% | Art. 146; FDFP | same |
| Total on gross | 2.8% | 12% | The total already holds both FDFP taxes; never add 1.6% again | https://www.dgi.gouv.ci/assets/documents/DOCTRINE%20FISCALE%202024/IMPOTS%20DIRECTS/IMPOT%20SUR%20LES%20TRAITEMENTS,%20SALAIRES,%20PENSIONS%20ET%20RENTES%20VIAGERES/N%C2%B0%2000026%20MFB%20DGI%20DLCD%20DU%2003%20JAN%202024%20Pr%C3%A9cisions%20relatives%20aux%20am%C3%A9nagements%20...%20des%20salari%C3%A9s.pdf |
| SMIG | 75,000 XOF a month | same | Decree 2022-986, from 1 Jan 2023 | https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf |

CE base: gross taxable pay, including benefits in kind, with no 20% abatement. Exempt: first job pay for two years; disabled staff pay for five years; maternity pay from CNPS (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page35.html).

## The base

Gross taxable pay as in [Income tax](ivory-coast-income-tax.md). Canteen meals are exempt up to 30,000 XOF a month per employee with a supplier contract where outside. Apprentice pay is exempt to 100,000 a month for up to two years (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page31.html).

Order: 1. gross pay; 2. ITS from the scale; 3. RICF; 4. employee CNPS and CMU; 5. net pay; 6. employer CNPS; 7. the 2.8% or 12% charge.

## Deadlines and filing

| Task | Date | Where |
|---|---|---|
| ITS and employer taxes, real regimes | 15th of next month | Recette or e-impots |
| Same, DGE and DME | Industry, oil, mining 10th; trade 15th; services 20th | e-impots |
| Annual ITS regularisation | 15 February; DGE and DME 10, 15 or 20 February | Same |
| Summary of employer contributions | 30 April | DGI |
| Etat 301 | 30 May; 30 June if audited | DGI |
| CNPS | See [Social contributions](ivory-coast-social-contributions.md) | e-CNPS |

Monthly withholding of 1,000 XOF or less may go half-yearly by 15 July and 15 January; if a month passes 5,000, all sums fall due in the first 15 days of the next month (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page36.html).

Steps: 1. Log in at https://e-impots.gouv.ci. 2. Enter the month's gross pay by staff type. 3. Submit the return. 4. Pay and keep the receipt. The screens and box names were not opened; see the last line of Sources.

## Penalties and interest

Omissions in withholding carry late interest under LPF 161 (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page29.html). Not paying over salary tax extends the audit period by three years (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page99.html).

## Cross-border points

The host of staff seconded by a non-resident employer is jointly liable for the employer contribution (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page35.html). Employers abroad pay it too. An employee of a foreign employer declares ITS personally (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page33.html).

## Two worked examples that recompute

Example 1. Local employee, 500,000 XOF, 1 part, AT/MP 2%.

```oa-check
name: Local employee 500000
inputs:
  pay: 500000
  atmp: 0.02
steps:
  - its: (240000 - 75000) * 0.16 + (pay - 240000) * 0.21
  - staff_cnps: pay * 0.063
  - net: pay - its - staff_cnps - 500
  - employer_cnps: pay * 0.077 + 75000 * 0.0575 + 75000 * atmp + 500
  - employer_tax: pay * 0.028
expected:
  its: 81000
  staff_cnps: 31500
  net: 387000
  employer_cnps: 44812.50
  employer_tax: 14000
```

Example 2, a decision. Local or expatriate contract on 1,000,000 XOF: the employer tax is 28,000 or 120,000, so expatriate status costs 92,000 a month more.

```oa-check
name: Local against expatriate
inputs:
  pay: 1000000
steps:
  - local: pay * 0.028
  - expat: pay * 0.12
  - extra: expat - local
expected:
  local: 28000
  expat: 120000
  extra: 92000
```

## Working material carried from the earlier version

### 8.1 Required Inputs

Before computing, you MUST have:

1. **Gross monthly remuneration in XOF** (cash + allowances + benefits in kind).
2. **RICF parts** (or the data to derive them: marital configuration + number of dependent children).
3. **Local vs expatriate status** (contract classification per AEJ).
4. **Employer headcount** (to set CNPS periodicity: ≥20 monthly, <20 quarterly).
5. **CNPS AT/MP risk-class rate** for the employer (2%-5%).
6. **Number of CMU-covered persons** per employee (for the flat 500 XOF/person each side).

### 8.2 Refusal Catalogue, STOP and refuse if:

**Refusal Catalogue table**

| Trigger | Action |
| --- | --- |
| Remuneration given in EUR, USD, or any non-XOF currency | Refuse; request XOF figures. No FX conversion in payroll. |
| Pre-2024 "IGR + CN + IS" stack requested | Refuse the obsolete method; explain the 2024 ITS reform (Ord. 2023-719) and offer the unified ITS. |
| Asked to apply the 12% expatriate rate without contract evidence | Refuse; require AEJ contract classification. |
| Asked to skip CNPS or FDFP "to save cost" | Refuse; these are statutory employer obligations. |
| Asked to treat ITS/CNPS as final without accountant sign-off | Refuse to label as final; output is Tier 2 estimate only. |
| Net-pay calc requested with no RICF / dependant data | Proceed only on the **1-part** conservative default, clearly flagged. |
| Sub-SMIG salary (< 75,000 XOF, non-agricultural) | Flag as below statutory minimum; do not normalise it. |

Statements and payroll documents are typically in **French**. Common terms and patterns:

### 14.1 Salary credits (employee view)

**Salary credits table**

| Pattern (French) | Meaning |
| --- | --- |
| SALAIRE, PAIE, VIREMENT SALAIRE | Net salary payment |
| NET À PAYER | Net pay line on payslip |
| AVANTAGES EN NATURE | Benefits in kind (taxable) |
| PRIME, INDEMNITÉ | Bonus / allowance (check taxability) |

### 14.2 Employer debit patterns

**Employer debit patterns table**

| Pattern (French) | Meaning |
| --- | --- |
| DGI ITS, IMPÔT SUR SALAIRES, e-IMPÔTS | ITS remittance to the DGI |
| CNPS, COTISATION CNPS, e-CNPS | CNPS contribution remittance |
| CMU | Universal health coverage flat contribution |
| FDFP, TAXE APPRENTISSAGE, FPC | FDFP training levies |
| CONTRIBUTION EMPLOYEUR, TAXE SUR SALAIRES | Employer payroll tax (2.8% / 12%) |

### 14.3 Glossary

**Glossary table**

| French | English |
| --- | --- |
| Impôt sur les Traitements et Salaires (ITS) | Salary income tax |
| Réduction pour Charges de Famille (RICF) | Family-charge reduction |
| Masse salariale | Total payroll |
| Caisse Nationale de Prévoyance Sociale (CNPS) | National social-security fund |
| Prestations familiales | Family allowances |
| Assurance vieillesse | Old-age / retirement insurance |
| Accident du travail / maladie professionnelle (AT/MP) | Work injury / occupational disease |
| DISA | Annual individual salary declaration |
| SMIG / SMAG | Minimum wage (general / agricultural) |


## Ask the client first

1. Number of staff, and local or expatriate contracts?
2. Each employee's parts?
3. AT/MP rate on the CNPS notice?
4. First job or disabled hires?
5. Tax office, DGE or DME, and sector?
6. Benefits in kind?

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Annexe fiscale 2026 (loi n° 2025-987), note de service and arts. 1 to 41 headings; articles quoted here read in full | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page2.html | 2026-11-01 |
| DGI, Le système fiscal ivoirien (undated e-book, predates the 2026 annex; the annex wins where they differ), pp. 3-51 read | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page3.html | 2026-11-01 |
| DGI, Impôts et taxes en Côte d'Ivoire, édition 2025 (art. 146 table, regimes, IRVM, VAT sections read) | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf | 2026-11-01 |
| DGI, Calendrier des obligations fiscales (VAT and BIC parts read) | https://www.dgi.gouv.ci/assets/documents/CALENDRIER.pdf | 2026-11-01 |
| DGI note n° 00026 of 3 Jan 2024, employer contribution part read | https://www.dgi.gouv.ci/assets/documents/DOCTRINE%20FISCALE%202024/IMPOTS%20DIRECTS/IMPOT%20SUR%20LES%20TRAITEMENTS,%20SALAIRES,%20PENSIONS%20ET%20RENTES%20VIAGERES/N%C2%B0%2000026%20MFB%20DGI%20DLCD%20DU%2003%20JAN%202024%20Pr%C3%A9cisions%20relatives%20aux%20am%C3%A9nagements%20...%20des%20salari%C3%A9s.pdf | 2026-11-01 |
| DGI note n° 01248 on VAT credit refunds, opening part read | https://www.dgi.gouv.ci/assets/documents/PROCEDURE_DE_REMBOURSEMENT_DE_CREDIT_TVA.pdf | 2026-11-01 |
| CNPS, communiqué on ceilings from 1 Jan 2023 (whole notice read) | https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf | 2026-11-01 |
| CNPS, employer page (paying contributions read; its SMIG and pension ceiling are out of date, the communiqué wins) | https://www.cnps.ci/employeur | 2026-11-01 |

Not yet confirmed: the full consolidated Code général des Impôts and Livre de Procédures fiscales 2026 (DGI lists them in its paid kiosk; the text was not opened), so article numbers come from the DGI documents above; the SMIG after 2023 (no later decree found on gouv.ci; a search is not proof of none); SMAG 39,960 (no official page opened); the definition of expatriate through an AEJ approved contract; e-impots screens and boxes; the ITS late surcharge of 25% plus 2% a month in the earlier version; benefits in kind tables; complementary pension exemption (one tenth of pay and 320,000, shown in the 2025 DGI table, not checked further).

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
