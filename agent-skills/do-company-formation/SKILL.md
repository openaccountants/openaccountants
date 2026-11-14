---
name: do-company-formation
description: "How to form a company in the Dominican Republic in 2026 and register it with DGII. Covers the SRL (two to fifty partners, capital of at least RD$100,000 in quotas of RD$100), the SA (authorised capital of at least RD$30,000,000), the SAS (authorised capital of at least RD$3,000,000, at least 10% paid), the EIRL, the 1% tax on authorised capital that still applies in 2026 and is repealed from 2027, Mercantile Registry registration at the Chamber of Commerce, and the RNC application with form RC-02 and the beneficial owner annex. Trigger on Dominican Republic company formation, SRL, SAS, EIRL, RNC, Registro Mercantil, 1% capital tax. Built from DGII and the Companies Law; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/do-company-formation"
  jurisdiction: "DO"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Dominican Republic Company Formation and Entity Choice v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders forming a commercial company in the Dominican Republic in 2026 under the General Law on Commercial Companies and Individual Limited Liability Enterprises, Law 479-08 (as amended by Law 31-11), and registering it with the Dirección General de Impuestos Internos (DGII). Amounts are Dominican pesos (RD$).

- **In:** SRL, SA, SAS and EIRL; name, bylaws, Mercantile Registry, the 1% capital tax and RNC registration.
- **Out:** free-zone and incentive-law approvals, regulated financial entities, non-profits, foreign company branches (DGII's guide lists their own requirements), and the ongoing tax returns (use `do-tax-overview`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| SRL, number of partners | Two or more, at most 50 | Over 50 must regularise or transform within two years | Law 479-08 arts. 89 and 93 (as amended by Law 31-11), SIPEN copy: https://sipen.gob.do/descarga/otras-leyes_2008_12_20200906121346.pdf |
| SRL, minimum capital | RD$100,000, in quotas of at least RD$100 | Set in the bylaws; the Ministry of Industry and Commerce may adjust the minimum every three years | same |
| SA, minimum authorised capital | RD$30,000,000, shares of at least RD$1 | Art. 160; the Ministry may adjust every three years | same |
| SAS, minimum authorised capital | RD$3,000,000 | Two or more persons; subscribed and paid capital at least 10% of authorised (art. 369-6) | same |
| Tax on company formation and capital increases | 1% of authorised share capital | Paid before RNC registration; not for EIRLs, foreign companies or non-profits; repealed from 2027 | DGII, Guide 3, incorporation of companies (2026): https://dgii.gov.do/publicacionesOficiales/bibliotecaVirtual/contribuyentes/rnc/Documents/Gu%C3%ADa%203%20-%20Incorporaci%C3%B3n%20de%20Sociedades.pdf |
| Repeal of the 1% tax | From 2027 | Law 30-26 art. 58 repeals Law 173-07 art. 10; in-kind contributions then bear the transfer taxes of the asset | same |
| Beneficial owner for RNC | Any individual with at least 20% of the capital or effective control | Annex D to form RC-02, mandatory | same |
| Start of operations declared to DGII | No later than 60 days after the RNC application | Obligations run from that date | same |

## The base

### Entity choice

| Form | Owners | Liability | Capital rule | Notes |
|---|---|---|---|---|
| SRL | 2 to 50 partners | Limited to contributions | At least RD$100,000 | Most common SME vehicle |
| SAS | 2 or more | Limited to contributions | Authorised at least RD$3,000,000, 10% paid | Flexible governance |
| SA | Shareholders | Limited | Authorised at least RD$30,000,000 | Larger companies; the paid-up share required is under Not yet confirmed |
| EIRL | One individual | Limited | Set by the founder; bank deposit certificate if contributed in cash | No 1% capital tax |

All pay corporate income tax at 27% (30% for income of RD$1,000 million or more in fiscal years 2026 to 2028) and the 1% asset tax: see `do-tax-overview`.

## Deadlines and filing

| Step | Where | What | After |
|---|---|---|---|
| 1 | ONAPI | Register the trade name (optional for the RNC, but DGII asks for the certificate if held) | Certificado de Nombre Comercial |
| 2 | Notary or private document | Bylaws (estatutos) and constituent assembly; the assembly must name the individual responsible for tax obligations, who must accept | Signed documents |
| 3 | Bank and DGII | Pay the 1% tax on authorised capital (SRL, SA, SAS in 2026) | Payment receipt |
| 4 | Cámara de Comercio y Producción | Register bylaws and assembly; obtain the Mercantile Registry certificate; all legal and financial documents must be registered and stamped by the Chamber | Certificado de Registro Mercantil |
| 5 | DGII, Oficina Virtual or office | Apply for the RNC: form RC-02 with Annex A (individual partners not yet in the RNC), B (foreign companies as partners), C (in-kind contributions), D (beneficial owner, mandatory), E (obliged subjects); IDs or passports, Mercantile Registry certificate, bylaws and assembly, 1% receipt, CIIU activity code | RNC number |
| 6 | DGII | A partner, shareholder or board member signs the registration form or the RNC registration act in person (a representative with a power may deposit it) | Acta de inscripción listing each obligation and its due dates |
| 7 | DGII | Declare the start of operations within 60 days of the RNC application; then file ITBIS, ISR, withholding and asset tax as listed in the acta | See `do-tax-overview` |

In-kind contributions of registrable assets need the contributions commissioner's report and the title or vehicle registration.

## Penalties and interest

Late payment of any tax after registration bears the 3% monthly surcharge (capped at 100%) and 1.10% monthly interest: see `do-tax-overview`. Formal breaches carry fines of 5 to 30 minimum wages.

## Cross-border points

- Foreign shareholders: passport copies; a foreign company as partner uses Annex B.
- A foreign company operating in the country registers its own RNC under the foreign company rules (not covered here).
- Dividends paid to foreign shareholders bear 10% final withholding (`do-tax-overview`).

## Two worked examples that recompute

### Example: SRL with authorised capital RD$1,000,000, formed in 2026 or in 2027

Formed in 2026, the 1% tax is RD$10,000 and its receipt is needed for the RNC. Formed in 2027 the tax is repealed and costs nothing; in-kind contributions would then bear the transfer tax of the asset instead.

```oa-check
name: DO SRL 1% capital tax, 2026 vs 2027
inputs:
  authorised_capital: 1000000
steps:
  - tax_2026: authorised_capital * 0.01
  - tax_2027: authorised_capital * 0
  - saving_by_waiting: tax_2026 - tax_2027
expected:
  tax_2026: 10000
  tax_2027: 0
  saving_by_waiting: 10000
```

## Ask the client first

1. Which form (SRL, SAS, SA, EIRL), and how many partners or shareholders, resident or foreign?
2. Authorised and paid capital, and any in-kind contributions?
3. Will incorporation finish in 2026 (1% tax due) or 2027 (repealed)?
4. Who are the beneficial owners (20% or control)?
5. Main economic activity (CIIU code) and whether any incentive law applies.
6. Who will be the individual responsible for tax obligations?

## Sources

| Source | URL | Read on |
|---|---|---|
| DGII, Guía del Contribuyente No. 3, incorporación de sociedades (2026): read in full for RNC requirements, the 1% tax and its repeal from 2027, the beneficial owner annex and the 60-day start of operations | https://dgii.gov.do/publicacionesOficiales/bibliotecaVirtual/contribuyentes/rnc/Documents/Gu%C3%ADa%203%20-%20Incorporaci%C3%B3n%20de%20Sociedades.pdf | 2026-11-14 |
| Law 479-08 on commercial companies, consolidated with Law 31-11 (copy published by SIPEN): read for arts. 89, 90, 93, 155, 160, 369-1 and 369-6 | https://sipen.gob.do/descarga/otras-leyes_2008_12_20200906121346.pdf | 2026-11-14 |
| Law 30-26 of 18 June 2026: read for art. 58 (repeal of the 1% formation tax from 2027) | https://dgii.gov.do/legislacion/leyesTributarias/Documents/Codigo%20Tributario%20y%20Leyes%20que%20lo%20modifican%20y%20complementan/30-26.pdf | 2026-11-14 |
| DGII, Aviso 10-26: read for the start date of the repeal (fiscal year 2027) | https://dgii.gov.do/publicacionesOficiales/avisosInformativos/Documents/2026/10-26.pdf | 2026-11-14 |

Not yet confirmed: whether the Ministry of Industry and Commerce has adjusted the minimum capital amounts since Law 31-11 (the SIPEN copy may not show later changes, including Law 68-19); the paid-up share required for an SA; Chamber of Commerce registration fees and the Mercantile Registry renewal cycle (the earlier version said every two years); ONAPI trade name fees; the typical one to two week timeline; the earlier version's statement that the SRL has no legal minimum capital, which the consolidated law contradicts.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `do-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/do-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
