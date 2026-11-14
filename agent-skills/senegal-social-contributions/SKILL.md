---
name: senegal-social-contributions
description: "Senegal social contributions for employees, tax year 2026. How IPRES pensions (general scheme and the extra cadre scheme), CSS family allowances and work injury, and IPM health cover are worked out, who bears each share, how ceilings cap the base, how the debits show on bank statements, and what to ask the employer. The rates and ceilings are not yet confirmed from an official Senegal source and must come from the employer's IPRES, CSS and IPM notices. Trigger on IPRES, CSS, IPM, cotisation sociale Senegal, Senegal employer charges, prestations familiales, accident du travail."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/senegal-social-contributions"
  jurisdiction: "SN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Senegal Social Contributions v1.0

## Scope

Compulsory social contributions on employees' pay in Senegal, tax year 2026, amounts in XOF:

| Body | Branch | Who pays |
|---|---|---|
| IPRES (Institution de Prevoyance Retraite du Senegal) | Pension, general scheme (all employees) | Employer and employee |
| IPRES | Pension, extra cadre scheme (executives only, in addition to the general scheme) | Employer and employee |
| CSS (Caisse de Securite Sociale) | Family allowances | Employer only |
| CSS | Work injury and occupational disease, rate by risk class set by the CSS | Employer only |
| IPM (Institution de Prevoyance Maladie) | Health cover through the employer's own IPM | Employer and employee |

Income tax withholding (IRPP), TRIMF and the 3% CFCE employer tax are in [senegal-payroll](senegal-payroll.md). This skill does not restate them.

**What is confirmed and what is not.** The ipres.sn and secusociale.sn sites did not open on 14 Nov 2026 and no Senegal decree setting the 2026 rates and ceilings was read, so every IPRES, CSS and IPM rate and ceiling is listed under "Not yet confirmed" and must be taken from the employer's affiliation notices or the institution's statement. The method below is sound whatever the figures are.

## Ask the client first

1. Gross monthly pay of each employee, in XOF.
2. Whether each employee is a cadre (executive or manager) under the collective agreement: decides the extra IPRES scheme.
3. The employer's IPRES, CSS and IPM affiliation notices, showing the rates and ceilings applied to it, including the CSS work-injury risk class.
4. Which IPM the employer belongs to, and that IPM's schedule (rate, base, caps).
5. Any foreign or seconded staff, and any social security agreement that may apply.
6. Any arrears or regularisation notices from the institutions.

## The method, step by step

### Rates, bands and thresholds

Only the figures confirmed on an official page are in this table. All contribution rates and ceilings are on the "Not yet confirmed" line under Sources.

| Item | Figure | Tax year | Source |
|---|---|---|---|
| Employee contributions and income tax | The 30% employment abatement (cap XOF 900,000 a year) stands in for compulsory pension contributions; employee IPRES and IPM shares are not deducted again from the IRPP base (CGI arts. 168 b, 182) | 2026 | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Family benefits and CFCE | Family benefits are left out of the CFCE base (CGI art. 266) | 2026 | same |

### Steps

1. **Classify each employee**: cadre or not. A non-cadre pays the IPRES general scheme only; a cadre pays the general scheme and the cadre scheme on top.
2. **Cap the base, not the contribution.** For each scheme take the base = min(gross monthly pay, that scheme's monthly ceiling). A high salary never raises the contribution above the capped base.
3. **Apply each share's rate** from the employer's notices: IPRES employer and employee shares; CSS family allowances and work injury, both employer only; IPM employer and employee shares from the IPM's own schedule.
4. **Split the cost.** Employee shares come off net pay (with IRPP and TRIMF from [senegal-payroll](senegal-payroll.md)). Employer shares add to the cost of employment, with the CFCE.
5. **Pay each body.** IPRES, CSS and IPM contributions go to the institutions, not to the DGID. IRPP, TRIMF and CFCE go to the DGID and Tresor.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Cadre status unclear (senior technician, team lead) | Flag; confirm against the collective agreement and the IPRES registration. Misclassification over- or under-states IPRES |
| Work-injury rate not on the CSS certificate | Do not assume a class; get the CSS registration. If a figure is needed meanwhile, show the range the employer gives and flag it |
| IPM fund unknown | Do not compute a definitive IPM amount; each IPM sets its own rate, base and caps |
| Expatriate or seconded staff | Flag; residence and any social security agreement may change which schemes apply |
| Arrears or late regularisation | Do not estimate surcharges: the CGI late-payment interest (art. 665) covers taxes, not social contributions. Get the institution's statement and refer to an expert-comptable |
| Pension received from IPRES | A benefit received, not a contribution paid |

### Defaults when a fact is missing

| Unknown | Default |
|---|---|
| Cadre or not | Non-cadre (general scheme only); flag for review |
| Gross above a ceiling | Use the ceiling as the base for that scheme |
| IPM schedule | Flag as a gap; no number |
| A DGID or Tresor debit that may bundle tax items | Treat as a tax payment (IRPP, TRIMF, CFCE); ask for the payroll journal to split |

### Bank statement patterns

These are statutory payroll payments: leave them out of any VAT return and never treat them as a business supply.

| Pattern (case-insensitive) | Treatment |
|---|---|
| `IPRES`, `INST PREVOYANCE RETRAITE`, `RETRAITE`, `COTISATION RETRAITE`, `REGIME GENERAL`, `REGIME CADRES` | IPRES pension contribution (general and cadre may be one payment) |
| `CSS`, `CAISSE DE SECURITE SOCIALE`, `PRESTATIONS FAMILIALES`, `ALLOC FAMILIALES`, `ACCIDENT TRAVAIL` | CSS contribution, employer cost |
| `IPM`, `INST PREVOYANCE MALADIE`, `MALADIE`, `COTISATION MALADIE` | IPM health contribution |
| `CFCE`, `CONTRIBUTION FORFAITAIRE` | Employer payroll tax: see [senegal-payroll](senegal-payroll.md) |
| `TRIMF`, `IRPP`, `RETENUE A LA SOURCE`, `RAS`, `DGID`, `IMPOTS`, `TRESOR PUBLIC` | Tax withheld and paid to the DGID, not a social contribution; flag to split if CFCE is bundled |
| `TVA`, `TAXE VALEUR AJOUTEE` | VAT, a separate obligation |
| `SALAIRE`, `PAIE`, `NET A PAYER` (outgoing) | Net wage paid out |
| `PENSION IPRES`, `PENSION RETRAITE` (incoming) | Pension received |
| `REGULARISATION`, `ARRIERE` | Possible arrears with surcharges; flag |

Banks seen with these references: CBAO (Attijariwafa), SGBS, Ecobank, BICIS, UBA, Bank of Africa. References are usually in French; payments are outgoing debits, usually monthly around mid-month for the previous month's payroll.

### Working from a bank statement only

1. Find the outgoing debits that match the patterns above.
2. Group them by body: IPRES, CSS, IPM, DGID.
3. Reverse-check each base: debit divided by the rate on the employer's notice gives the implied capped base. Only the CFCE (to the DGID) scales with the full payroll.
4. Flag that cadre status, the work-injury class, the IPM schedule and family parts are not verified, and that a reviewer must confirm before any return is filed.

### Working paper columns (per employee, monthly, XOF)

Gross; cadre yes or no; IPRES general base `MIN(gross, ceiling)`; IPRES general employee and employer; IPRES cadre base and shares (cadres only); CSS base `MIN(gross, CSS ceiling)`; CSS family allowances and work injury (employer); IPM base and shares (from the IPM schedule); total employee shares; total employer shares. Rates and ceilings in one input row taken from the notices, so they can be changed in one place.

## Worked cases

The rates and ceilings below are **illustrative inputs only, not Senegal's rates**: the real ones come from the employer's notices.

**Case 1, the ceiling caps the base.** A non-cadre earns 500,000 a month. Suppose the employer's IPRES notice gives a monthly ceiling of 400,000, an employer share of 8% and an employee share of 5%. The base is 400,000, not 500,000: employer 32,000, employee 20,000, total 52,000.

```oa-check
name: Contribution on a capped base (illustrative rates)
inputs:
  gross: 500000
  ceiling: 400000
  employer_rate: 0.08
  employee_rate: 0.05
steps:
  - base: min(gross, ceiling)
  - employer: base * employer_rate
  - employee: base * employee_rate
  - total: employer + employee
expected:
  base: 400000.00
  total: 52000.00
```

**Case 2, a decision: cadre or not?** The same 500,000 employee is promoted to a role the collective agreement treats as cadre. Suppose the cadre scheme notice gives a ceiling of 1,200,000 and a combined rate of 6%. Not cadre: general scheme only, 52,000. Cadre: 52,000 plus 6% of min(500,000, 1,200,000) = 30,000, so 82,000. The cadre status is the fact that decides; confirm it before the first payroll.

```oa-check
name: Cadre or not (illustrative rates)
inputs:
  gross: 500000
  general_total: 52000
  cadre_ceiling: 1200000
  cadre_rate: 0.06
steps:
  - cadre_extra: min(gross, cadre_ceiling) * cadre_rate
  - not_cadre: general_total
  - cadre: general_total + cadre_extra
expected:
  cadre_extra: 30000.00
  cadre: 82000.00
```

## When to refuse or refer

- No gross pay: stop.
- A request for definitive IPRES, CSS or IPM figures without the employer's notices: refuse; the rates are not confirmed here.
- Arrears, penalties or surcharges on contributions: refer to a Senegal expert-comptable with the institution's statement.
- Secondees and social security agreements: refer.
- Any output to be filed as final: refuse; estimate only, for review.

Never apply the cadre scheme to a non-cadre or leave it out for a confirmed cadre; never deduct CSS from the employee; never apply a rate to pay above the capped base; never treat an "RAS IRPP" debit as a social contribution.

## Filing and payment

- IPRES, CSS and IPM: paid to each institution under its own schedule; the dates were not read on an official page (see Not yet confirmed).
- Salary tax items (IRPP, TRIMF, CFCE): first 15 days of the next month, or quarterly for real simplified and CGU employers; the annual salary statement in January. See [senegal-payroll](senegal-payroll.md).

## Completion checklist

- Cadre status of each employee confirmed.
- Rates and ceilings taken from the employer's IPRES, CSS and IPM notices, with the notice dates recorded.
- Each base capped before the rate is applied.
- Employer-only branches (CSS) included in employer cost, not deducted from pay.
- Tax items left to the payroll skill.
- Output labelled as an estimate for review.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): read arts. 168, 182 (the abatement stands in for compulsory pension contributions) and 263 to 269 (CFCE base excludes family benefits) in the PDF text | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-14 |

Not yet confirmed: all IPRES, CSS and IPM rates, ceilings and payment dates for 2026. The figures in the old version (IPRES general 8.4% employer and 5.6% employee on a monthly ceiling of 432,000; IPRES cadre 3.6% and 2.4% on 1,296,000, with the cadre base possibly between 432,000 and 1,296,000; CSS family allowances 7% and work injury 1%, 3% or 5% on 63,000; IPM 3% and 3% on a base of 60,000 to 250,000, or 2% to 7.5% with a 2% AMO levy) rested on a firm's tax summary and a foreign liaison body, because ipres.sn and secusociale.sn did not open and no Senegal decree was read. SMIG (XOF 371 an hour since 1 July 2023) and the rule that CSS contributions are never on less than the SMIG: decree not read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `senegal-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/senegal-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
