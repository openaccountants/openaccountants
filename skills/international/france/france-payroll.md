---
name: france-payroll
description: Use this skill whenever asked about French payroll processing for employees. Trigger on phrases like "French payroll", "bulletin de paie", "fiche de paie", "prélèvement à la source", "PAS", "URSSAF cotisations", "cotisations sociales France", "CSG CRDS", "SMIC", "AGIRC-ARRCO", "retraite complémentaire", "DSN", "net imposable", "net à payer", "salaire brut net France", "charges patronales", "charges salariales", "PMSS", "plafond sécurité sociale", "minimum wage France", "congés payés", "13ème mois", "mutuelle obligatoire", or any question about computing employee pay, income tax withholding, or social contributions in France. This skill covers prélèvement à la source (PAS), URSSAF contributions, AGIRC-ARRCO, CSG/CRDS, mandatory benefits, payslip (bulletin de paie) requirements, DSN filing, and employer cost analysis. ALWAYS read this skill before processing any French employee payroll.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France Payroll

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Currency | EUR only |
| Standard pay frequency | Monthly (mensuel) -- almost universal |
| Tax year | Calendar year (1 January -- 31 December) |
| Income tax withholding | Prélèvement à la Source (PAS) -- rate communicated by DGFiP to employer |
| Social contribution authority | URSSAF (collects contributions for all social security branches) |
| Supplementary pension | AGIRC-ARRCO (single unified scheme since 2019) |
| Tax authority | Direction Générale des Finances Publiques (DGFiP) |
| Key legislation | Code de la Sécurité sociale; Code du Travail; Code Général des Impôts (Art. 204 A--M for PAS) |
| Social Security Ceiling (PMSS, 2026) | EUR 4,005/month (EUR 48,060/year) |
| Electronic declaration | DSN (Déclaration Sociale Nominative) via net-entreprises.fr |
| Validated by | Pending -- requires sign-off by a French expert-comptable |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (Prélèvement à la Source)

Since 1 January 2019, France operates a PAYE system where the employer withholds income tax from the employee's **net imposable** (net taxable salary) each month.

### How PAS Works

**How PAS Works**

| Step | Detail |
| --- | --- |
| Rate source | DGFiP transmits the employee's personalised PAS rate to the employer via the DSN feedback loop |
| Default rate | If no personalised rate is available, a statutory "taux neutre" (barème par défaut) applies, based on monthly net imposable |
| Calculation | PAS = Net imposable x PAS rate |
| Deducted from | Net salary (after social contributions, before payment) |
| Remittance | Monthly via DSN + URSSAF collection |

### Income Tax Brackets (2026, progressive scale for annual declaration)

**Income Tax Brackets (2026, progressive scale for annual declaration)**

| Taxable Income (EUR, per part) | Rate |
| --- | --- |
| 0 -- 11,600 | 0% |
| 11,601 -- 29,579 | 11% |
| 29,580 -- 84,577 | 30% |
| 84,578 -- 181,917 | 41% |
| 181,918+ | 45% |

The PAS rate already accounts for the quotient familial (family coefficient) system when personalised. The employer does NOT compute tax brackets -- they simply apply the rate received from DGFiP.

### Taux Neutre (Default Rate Grid, 2026 -- Metropolitan France)

Used when no personalised rate is available. Based on monthly net imposable. Progressive grid from 0% (low income) to 43% (high income). Consult the CGI Article 204 H barème for exact thresholds.

## Section 3 -- Social Security -- Employee Deductions (2026)

### URSSAF Contributions (Employee Share)

**URSSAF Contributions (Employee Share)**

| Contribution | Employee Rate | Base |
| --- | --- | --- |
| Maladie, maternité, invalidité, décès | 0% | Total gross |
| Vieillesse plafonnée (old-age, capped) | 6.90% | Up to 1 PMSS (EUR 4,005/month) |
| Vieillesse déplafonnée (old-age, uncapped) | 0.40% | Total gross |
| CSG déductible | 6.80% | 98.25% of gross |
| CSG non-déductible | 2.40% | 98.25% of gross |
| CRDS | 0.50% | 98.25% of gross |

- **98.25% abattement threshold** — The 98.25% abattement (1.75% deduction for professional expenses) applies only up to 4 PMSS (EUR 192,240/year in 2026). Above that threshold, CSG/CRDS apply on 100% of gross.

### AGIRC-ARRCO (Supplementary Pension -- Employee Share)

**AGIRC-ARRCO (Supplementary Pension -- Employee Share)**

| Contribution | Employee Rate | Base |
| --- | --- | --- |
| Retraite complémentaire Tranche 1 (T1) | 3.15% | Up to 1 PMSS |
| Retraite complémentaire Tranche 2 (T2) | 8.64% | From 1 to 8 PMSS (EUR 4,005 -- EUR 32,040) |
| CEG (Contribution d'Équilibre Général) T1 | 0.86% | Up to 1 PMSS |
| CEG T2 | 1.08% | From 1 to 8 PMSS |
| CET (Contribution d'Équilibre Technique) | 0.14% | From 1 to 8 PMSS (cadres/non-cadres above PMSS) |

- **Appelés rates** — AGIRC-ARRCO rates shown are appelés (call rates = 127% of contractual rates). Pension points are calculated on the contractual rate (e.g., T1 contractual = 6.20% total).

### Chômage (Unemployment -- Employee Share)

**Chômage (Unemployment -- Employee Share)**

| Contribution | Employee Rate | Base |
| --- | --- | --- |
| Assurance chômage | 0% | Up to 4 PMSS |

- **Employee unemployment contribution abolished** — Employee unemployment contribution was abolished in October 2018. Only the employer pays.

### Total Employee Deductions (Approximate)

- **Total employee deductions at PMSS** — For a salary at the PMSS (EUR 4,005/month): employee social contributions total approximately 21--23% of gross, plus PAS income tax.

## Section 4 -- Social Security -- Employer Contributions (2026)

### URSSAF Contributions (Employer Share)

**URSSAF Contributions (Employer Share)**

| Contribution | Employer Rate | Base |
| --- | --- | --- |
| Maladie, maternité, invalidité, décès | 13.00% | Total gross |
| Vieillesse plafonnée | 8.55% | Up to 1 PMSS |
| Vieillesse déplafonnée | 2.11% | Total gross |
| Allocations familiales | 5.25% | Total gross |
| Accidents du travail (AT/MP) | Variable (0.5%--7%+) | Total gross |
| Contribution Solidarité Autonomie (CSA) | 0.30% | Total gross |
| FNAL (Fonds National d'Aide au Logement) | 0.10% (< 50 employees) or 0.50% (≥ 50) | Up to 1 PMSS or total gross |
| Contribution au dialogue social | 0.016% | Total gross |

### AGIRC-ARRCO (Employer Share)

**AGIRC-ARRCO (Employer Share)**

| Contribution | Employer Rate | Base |
| --- | --- | --- |
| Retraite complémentaire T1 | 4.72% | Up to 1 PMSS |
| Retraite complémentaire T2 | 12.95% | From 1 to 8 PMSS |
| CEG T1 | 1.29% | Up to 1 PMSS |
| CEG T2 | 1.62% | From 1 to 8 PMSS |
| CET | 0.21% | From 1 to 8 PMSS |
| APEC (cadres only) | 0.036% | Up to 4 PMSS |

### Unemployment and Other Employer-Only

**Unemployment and Other Employer-Only**

| Contribution | Employer Rate | Base |
| --- | --- | --- |
| Assurance chômage | 4.05% | Up to 4 PMSS (EUR 16,020/month) |
| AGS (Association pour la Gestion du régime d'assurance des créances des Salariés) | 0.25% | Up to 4 PMSS |
| Prévoyance cadres (minimum) | 1.50% | Up to 1 PMSS (Convention collective nationale des cadres) |

### Total Employer Cost (Approximate)

- **Total employer cost approximate** — Total employer contributions typically amount to 45--55% on top of gross salary, depending on industry (AT/MP rate), company size, and whether the employee is cadre or non-cadre.

## Section 5 -- Minimum Wage and Overtime

### SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026)

**SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026)**

| Item | Value |
| --- | --- |
| Gross hourly (from 1 June 2026) | EUR 12.31 |
| Gross monthly (35 hrs/week) | EUR 1,867.02 |
| Net monthly (approximate) | EUR 1,477.93 |
| Prior rate (1 Jan -- 31 May 2026) | EUR 12.02/hour (EUR 1,823.03/month gross) |

- **SMIC revalorisation rule** — The SMIC is revalorised automatically when CPI rises 2%+ since the last revaluation, and annually on 1 January.

### Working Hours and Overtime

**Working Hours and Overtime**

| Rule | Detail |
| --- | --- |
| Legal weekly hours (durée légale) | 35 hours |
| Maximum daily hours | 10 hours (extendable to 12 by agreement) |
| Maximum weekly hours | 48 hours absolute; 44 hours average over 12 weeks |
| Overtime: 36th--43rd hour | +25% of hourly rate |
| Overtime: 44th hour and above | +50% of hourly rate |
| Annual overtime contingent | 220 hours default (modifiable by collective agreement) |
| Alternative to payment | Repos compensateur (compensatory time off) per agreement |

- **Collective agreements may adjust rates** — Collective agreements (conventions collectives) may adjust these rates and thresholds.

## Section 6 -- Mandatory Benefits

### Congés Payés (Paid Annual Leave)

**Congés Payés (Paid Annual Leave)**

| Entitlement | Detail |
| --- | --- |
| Statutory | 2.5 working days per month worked = 30 working days (5 weeks) per year |
| Accrual period | 1 June -- 31 May (reference period, unless otherwise agreed) |
| Main leave | Minimum 2 consecutive weeks between 1 May and 31 October |
| Fractionnement bonus | 1--2 extra days if leave is split outside the main period |

### Sick Leave (Arrêt Maladie)

**Sick Leave (Arrêt Maladie)**

| Entitlement | Detail |
| --- | --- |
| Social security daily allowance (IJSS) | 50% of daily base salary (capped at 1/720 of 3x PASS); 3-day waiting period |
| Employer top-up (maintien de salaire) | Per Code du Travail L1226-1: after 1 year seniority, employer pays 90% of gross for 30 days, then 66.66% for 30 days (periods increase with seniority) |
| Medical certificate | Required; sent to CPAM within 48 hours |

### Maternity Leave (Congé de Maternité)

**Maternity Leave (Congé de Maternité)**

| Entitlement | Detail |
| --- | --- |
| Duration (1st/2nd child) | 16 weeks (6 pre-natal + 10 post-natal) |
| Duration (3rd+ child) | 26 weeks (8 + 18) |
| Twins | 34 weeks; triplets+ 46 weeks |
| Pay | IJSS maternité (daily allowance from Sécurité sociale, capped at PMSS net equivalent) |
| Employer top-up | Many collective agreements provide 100% maintien de salaire |

### Paternity Leave (Congé de Paternité)

**Paternity Leave (Congé de Paternité)**

| Entitlement | Detail |
| --- | --- |
| Duration | 25 calendar days (32 for multiple births) + 3 days congé de naissance |
| Pay | IJSS from Sécurité sociale; employer top-up per agreement |

### 13th Month (Treizième Mois)

No statutory obligation. Very common per collective agreements or company policy. Where contractual, it is subject to all cotisations and PAS.

### Mutuelle Obligatoire (Compulsory Health Insurance)

**Mutuelle Obligatoire (Compulsory Health Insurance)**

| Item | Detail |
| --- | --- |
| Requirement | Employer must offer a complémentaire santé to all employees (since 2016, ANI) |
| Minimum employer contribution | 50% of the premium |
| Minimum coverage | Panier de soins (basket of care): optician, dental, hospital |

## Section 7 -- Payslip Requirements

The bulletin de paie is governed by Code du Travail Articles L3243-1 to L3243-4 and R3243-1.

### Mandatory Payslip Fields (Simplified Format since 2018)

**Mandatory Payslip Fields (Simplified Format since 2018)**

| Section | Required Fields |
| --- | --- |
| Header | Employer name, SIRET, APE/NAF code, convention collective applicable |
| Employee | Name, position, classification, date of entry |
| Period | Pay period, hours worked (normal + overtime + supplementary) |
| Gross pay | Base salary, overtime, bonuses, premiums, in-kind benefits |
| Social contributions | Grouped by risk: Santé, Accidents du travail, Retraite, Famille, Chômage, CSG/CRDS -- showing base, employee rate, employer rate, employee amount, employer amount |
| Net imposable | Gross minus deductible social contributions |
| PAS | PAS rate, PAS base, PAS amount withheld |
| Net à payer avant PAS | Net after all social contributions, before income tax |
| Net à payer | Final amount paid to employee (after PAS) |
| Cumuls annuels | Year-to-date totals: gross, net imposable, PAS withheld, hours worked |
| Footer | Payment date, leave balance, mention "conserver le bulletin de paie sans limitation de durée" |

### Delivery

- Paper or electronic (with employee consent or company agreement for digital)
- Employer must retain a copy for 5 years minimum
- Simplified format groups contributions by risk category rather than line-by-line

## Section 8 -- Filing Obligations

### Monthly -- DSN (Déclaration Sociale Nominative)

**Monthly -- DSN (Déclaration Sociale Nominative)**

| Obligation | Deadline | Notes |
| --- | --- | --- |
| DSN (≥ 50 employees) | 5th of the month following the pay period | Single electronic declaration to all social bodies |
| DSN (< 50 employees) | 15th of the month following the pay period | Same format, later deadline |
| DSN signalement d'événement | Within 5 days of event | Arrêt maladie, accident du travail, fin de contrat |
| PAS payment | With DSN transmission | Collected by URSSAF on behalf of DGFiP |
| Social contribution payment | With DSN transmission | URSSAF debits after DSN acceptance |

- **DSN replaces declarations** — The DSN replaced 25+ separate declarations and is the single channel for URSSAF, AGIRC-ARRCO, France Travail, CPAM, and DGFiP.

### Annual

**Annual**

| Obligation | Deadline | Notes |
| --- | --- | --- |
| DADS (replaced by DSN) | N/A -- fully replaced since 2019 | Historical reference only |
| Bilan social | Varies | Companies ≥ 300 employees |
| Index égalité professionnelle | 1 March | Companies ≥ 50 employees; gender pay gap index |

### Employee Obligations

**Employee Obligations**

| Item | Detail |
| --- | --- |
| Déclaration de revenus | Annual (April--June); pre-filled with PAS data |
| Adjustment | If PAS rate was incorrect, balance settled via avis d'imposition |

## Section 9 -- Common Payroll Patterns

### Typical Bank Statement Descriptions (Salary Credits)

**Typical Bank Statement Descriptions (Salary Credits)**

| Pattern | Classification |
| --- | --- |
| VIREMENT SALAIRE, VIR SALAIRE | Net salary payment |
| SALAIRE [EMPLOYER NAME] | Net salary payment |
| INDEMNITE CONGES PAYES | Holiday pay (if paid separately) |
| PRIME 13EME MOIS | 13th month bonus |
| PRIME PARTICIPATION, INTERESSEMENT | Profit-sharing (separate tax/social rules) |
| IJSS, CPAM INDEMNITE | Sickness/maternity daily allowance from Sécurité sociale |

### Typical Employer Debit Patterns

**Typical Employer Debit Patterns**

| Pattern | Classification |
| --- | --- |
| URSSAF COTISATIONS | Monthly social contribution payment |
| AGIRC-ARRCO COTISATIONS | Supplementary pension contributions |
| DGFIP PAS, PRELEVEMENT SOURCE | PAS income tax remittance |
| MUTUELLE [NAME] | Compulsory health insurance premium |
| PREVOYANCE [NAME] | Provident insurance premium |

## Section 10 -- Interaction with Other Skills

**Section 10 -- Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (cotisations + PAS) | **This skill (france-payroll.md)** |
| Self-employed income tax | france-income-tax.md |
| Auto-entrepreneur / micro-enterprise | france-micro-enterprise.md |
| TVA (French VAT) | france-vat-return.md |
| Bookkeeping | france-bookkeeping.md |
| E-invoicing (Factur-X / Chorus Pro) | france-einvoice.md |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages + employer charges are P&L expenses. Employee deductions (cotisations + PAS) are liabilities (comptes 43x) until DSN payment. Employer cotisations are booked to 645xxx.
- **Payroll → Income Tax:** The PAS system means employees' income tax is largely settled in real time. Year-end déclaration may result in adjustments. The net imposable on the bulletin de paie is the reference figure.
- **Payroll → DSN:** All payroll data feeds directly into DSN. Accurate bulletins de paie = accurate DSN. Errors in DSN trigger anomaly reports from net-entreprises.fr.

## PROHIBITIONS

- **Prohibitions list** — - NEVER compute income tax brackets manually for withholding -- use the PAS rate provided by DGFiP - NEVER forget to apply the 98.25% abattement on gross for CSG/CRDS (and 100% above 4 PMSS) - NEVER confuse Tranche 1 (up to 1 PMSS) and Tranche 2 (1--8 PMSS) ceilings for AGIRC-ARRCO - NEVER omit the mutuelle obligatoire (compulsory health insurance) from employer cost calculations - NEVER apply employee chômage contributions -- they were abolished in 2018 - NEVER issue a bulletin de paie missing any mandatory field under Code du Travail - NEVER miss a DSN deadline -- penalties of EUR 7.50 per employee per month of delay - NEVER forget that SMIC changed mid-year (1 June 2026) -- verify which rate applies - NEVER present payroll computations as definitive -- direct to expert-comptable for sign-off

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable in France) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
