---
name: ivory-coast-social-contributions
description: >
  Use this skill for Côte d'Ivoire (Ivory Coast) social contributions in 2026 under the CNPS general scheme: pension, family benefits, maternity, work injury and CMU, with the contribution floor and ceilings, the contribution base, monthly or quarterly payment and the e-CNPS steps. It is for employers, payroll staff and accountants handling salaried workers in the private sector. Trigger on "CNPS", "cotisations sociales", "retraite Côte d'Ivoire", "AT/MP", "CMU", "plafond CNPS", "e-CNPS" or questions on what an employer owes on a salary in Ivory Coast. It does not cover the self-employed RSTI scheme or public sector pensions, and it reads with the payroll skill.
version: 0.2
jurisdiction: CI
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Côte d'Ivoire (Ivory Coast) Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it without checking the cited official source or a licensed professional.

Tax year 2026. Private sector salaried scheme.

## Who this applies to

Employers and employees under the CNPS general scheme. Self-employed RSTI and public sector staff are out of scope.

## Rates, bands and thresholds

| Branch | Employee | Employer | Monthly base | Source |
|---|---|---|---|---|
| Pension | 6.3% | 7.7% | Up to 3,375,000 | https://www.cnps.ci/employeur |
| Family benefits | 0 | 5% | Up to 75,000 | same |
| Maternity | 0 | 0.75% | Up to 75,000 | same |
| Work injury AT/MP | 0 | 2% to 5%, as notified | Up to 75,000 | same |
| Floor, all branches | | | 75,000 | https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf |
| Other ceiling confirmation | | | 3,375,000 pension, 75,000 others, from 1 Jan 2023 | same |
| CMU | unverified 500 XOF a person | unverified 500 XOF a person | Flat | unverified, page shows no amount |

CNPS gives each employer's AT/MP rate with its employer number. Use that rate. Do not assume one.

## The base

All pay including benefits in kind and allowances, except expense reimbursements (Code de Prévoyance Sociale art. 23). Never below the SMIG. Allowances excluded within limits: meal 3 times the hourly SMIG, dirt 13 times, work clothes 7 times, tools 10 times a month; transport up to the tax exempt amount. Apprentices with a contract use half the SMIG (https://www.cnps.ci/employeur).

## Deadlines and filing

Monthly with 20 or more staff, quarterly below 20. Pay within the first 15 days after the period (https://www.cnps.ci/employeur).

Steps: 1. Register at the CNPS agency for the head office with CIE and SODECI bills, trade register copy, tax existence declaration and the director's ID. 2. Receive the employer number and AT/MP rate. 3. Activate the account on the e-CNPS portal. 4. Each period take the CNPS and CMU contribution call online and pay online there. 5. File the annual regularisation; it lets CNPS apply the annual ceiling.

## Penalties and interest

Payment after the 15 days exposes the employer to penalties. Art. 29 of the Code sets criminal penalties (https://www.cnps.ci/employeur). Amounts: see the last line of Sources.

## Cross-border points

Seconded staff and treaty cover are not addressed here; ask for the certificate from the home scheme and refer.

## Two worked examples that recompute

Example 1. At the SMIG, AT/MP 2%.

```oa-check
name: SMIG employee
inputs:
  pay: 75000
steps:
  - staff: pay * 0.063
  - employer: pay * 0.077 + pay * 0.0575 + pay * 0.02
expected:
  staff: 4725
  employer: 11587.50
```

Example 2, a decision. Eighteen staff on 5,000,000 each at AT/MP 5%: a hire to 20 moves payment from quarterly to monthly. Each person costs the same a month; the pension base stops at 3,375,000.

```oa-check
name: Above the ceiling
inputs:
  pay: 5000000
steps:
  - base: min(pay, 3375000)
  - staff: base * 0.063
  - employer: base * 0.077 + 75000 * 0.0575 + 75000 * 0.05
  - quarter_18: employer * 3 * 18
expected:
  staff: 212625
  employer: 267937.50
  quarter_18: 14468625
```

## Working material carried from the earlier version

This is the deterministic pre-classifier for bank-statement and payroll transactions related to CNPS social contributions. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the statement. CNPS contribution payments always EXCLUDE from any VAT/TVA return, they are statutory social charges, not taxable supplies. Employer contributions are a deductible payroll cost; the employee share is withheld from gross pay.

### 3.1 CNPS contribution débits

**3.1 CNPS contribution débits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNPS, PREVOYANCE SOCIALE | EXCLUDE, CNPS contribution | Monthly/quarterly appel de cotisations |
| COTISATION SOCIALE, COTISATIONS CNPS | EXCLUDE, CNPS contribution | Same |
| RETRAITE CNPS, ASSURANCE VIEILLESSE | EXCLUDE, pension branch | Pension portion |
| PRESTATIONS FAMILIALES, ALLOC FAMILIALES | EXCLUDE, family-benefits branch | Employer-only |
| ACCIDENT TRAVAIL, AT/MP | EXCLUDE, work-injury branch | Employer-only |
| APPEL DE COTISATIONS | EXCLUDE, CNPS contribution | The CNPS billing reference |

### 3.2 CMU (health) débits

**3.2 CMU (health) débits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CMU, COUVERTURE MALADIE UNIVERSELLE | EXCLUDE, CMU health contribution | Flat XOF 500 + 500 per person/month |
| CNAM | EXCLUDE, CMU health | Caisse Nationale d'Assurance Maladie (CMU manager) |

### 3.3 CNPS débits appearing on specific Ivorian banks

**3.3 CNPS débits appearing on specific Ivorian banks**

| Bank | Typical débit description | Treatment |
| --- | --- | --- |
| SGCI (Société Générale CI) | "CNPS COTISATIONS" or "PREVOYANCE SOCIALE" | EXCLUDE, CNPS |
| BICICI | "CNPS" or "COTIS SOCIALES" | EXCLUDE, CNPS |
| Ecobank CI | "CNPS COTISATION" or "PREVOYANCE" | EXCLUDE, CNPS |
| NSIA Banque | "CNPS" or "COTISATION SOCIALE" | EXCLUDE, CNPS |
| Coris Bank | "CNPS" or "APPEL COTISATIONS" | EXCLUDE, CNPS |

### 3.4 Tax payments (NOT social contributions, do not confuse)

**3.4 Tax payments (NOT social contributions, do not confuse)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI, DIRECTION GENERALE DES IMPOTS | EXCLUDE, tax, not CNPS | Income/payroll tax (ITS, etc.), not social security |
| ITS, IMPOT SUR SALAIRES | EXCLUDE, payroll tax | Not a CNPS contribution |
| TVA | EXCLUDE, VAT | Not a CNPS contribution |

### 3.5 Salary and benefit payments (exclude from CNPS classification)

**3.5 Salary and benefit payments (exclude from CNPS classification)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, VIREMENT SALAIRE (outgoing) | EXCLUDE, payroll expense | Not a contribution payment |
| PENSION CNPS, RENTE (incoming/received) | EXCLUDE, benefit received | Not a contribution paid |

### How CNPS débits appear on Ivorian bank statements

**SGCI (Société Générale Côte d'Ivoire):**
- Description: "CNPS COTISATIONS" or "PREVOYANCE SOCIALE"
- Timing: Within 15 days after month-end (≥20 staff) or quarter-end (<20 staff)
- Amount: Sum of all branches across declared employees

**BICICI / Ecobank CI / NSIA / Coris:**
- Description: "CNPS", "COTISATION SOCIALE", "APPEL COTISATIONS", or "PREVOYANCE"
- Timing: Same monthly/quarterly cycle
- Amount: Matches the CNPS appel de cotisations

**CMU débits:**
- Description: "CMU", "COUVERTURE MALADIE UNIVERSELLE", or "CNAM"
- Amount: XOF 1,000 × number of covered persons (500 EE + 500 ER)

**Key identification tips:**
1. CNPS contribution débits are always outgoing, never credits (an incoming "PENSION CNPS" is a benefit received, not a contribution).
2. They recur monthly or quarterly with amounts tied to the appel de cotisations.
3. Do not confuse with DGI/ITS débits (payroll tax) or TVA (VAT), those are tax, not social security.
4. Régularisation lump sums may bundle principal with the 10% penalty + majorations, flag for breakdown.


## Ask the client first

1. Staff count?
2. Notified AT/MP rate?
3. Each person's pay and benefits?
4. Covered dependants for CMU?
5. Any seconded staff?

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

Not yet confirmed: CMU amounts (kept from the earlier version; no CNPS or CMU amount page opened); DISA and DASC due by 31 March; late penalty (the earlier versions gave 10% and also 5% plus 1% a month; Code articles not opened); the Code de Prévoyance Sociale text itself; employee pension base at the SMIG after 2023; CNPS guide for employers not read.

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
