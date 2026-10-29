---
name: mx-social-contributions
description: >
  Mexico social contributions (IMSS) reference for 2026. Covers employer and worker quotas under the Ley del Seguro Social (Arts. 28, 38, 39, 73, 147, 168, 211), the five occupational-risk classes, the SBC base and its 25x minimum-wage ceiling, INFONAVIT 5%, the retirement branch, state payroll taxes, monthly cedula payment by the 17th, and PTU. Trigger on Mexico IMSS, cuotas obrero patronales, salario base de cotizacion, INFONAVIT, PTU, prima de riesgo. Source-cited draft.
jurisdiction: MX
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.3
---

# Mexico social contributions (IMSS, INFONAVIT, PTU)

> **Source-cited draft.** Built from the Cámara de Diputados consolidated texts of the Ley del Seguro Social (LSS) and the Ley del Instituto del Fondo Nacional de la Vivienda para los Trabajadores (LIFNVT), and the INFONAVIT employer help pages, read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Mexican professional.

Tax year: the calendar year. Currency: Mexican peso (MXN). The Instituto Mexicano del Seguro Social (IMSS) collects social security quotas; INFONAVIT receives the housing contribution.

See also: `mx-payroll-withholding` (ISR on wages), `mx-corporate-income-tax` (PTU deduction).

## Who this applies to

Every employer (patrón) with workers in Mexico registers with IMSS, withholds the worker quotas from wages (LSS Art. 38) and pays the combined obrero-patronal quotas. Cooperatives pay the employer quota and their members pay as workers (Art. 19). Independent workers can affiliate voluntarily.

## Rates, bands and thresholds

Quotas are on the salario base de cotización (SBC). LSS Art. 28 sets the ceiling at 25 times the general minimum wage of the Distrito Federal and the floor at the general minimum wage of the area (whether the ceiling is read as 25 UMA is on the Not yet confirmed line).

| Branch | Employer | Worker | Tax year | Source |
|---|---|---|---|---|
| Disability and life (invalidez y vida) | 1.75% | 0.625% | 2026 | [LSS Art. 147](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Retirement (retiro, SAR) | 2% | none | 2026 | [LSS Art. 168 fr. I](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Old age and severance (cesantía en edad avanzada y vejez) | By SBC band, rising with pay; the LSS table shows the final schedule (3.150% at 1 minimum wage to 11.875% at 4.01 UMA and above); the 2026 transitional rates are on the Not yet confirmed line | 1.125% | 2026 | [LSS Art. 168 fr. II](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Illness and maternity, cash benefits (prestaciones en dinero) | 0.70% (70% of a 1% quota) | 0.25% (25% of the 1% quota) | 2026 | [LSS Art. 107](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Daycare and social benefits (guarderías y prestaciones sociales) | 1% | none | 2026 | [LSS Art. 211](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Housing (INFONAVIT) | 5% of wages | none | 2026 | [LIFNVT Art. 29 fr. II](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIFNVT.pdf); [INFONAVIT employer FAQ](https://portalmx.infonavit.org.mx/wps/portal/infonavitmx/mx2/patrones/centro_ayuda/preguntas_frecuentes/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zizTxdDAwtnA2MLA0NDAzM_J193ZxMTQ09w0z1C7IdFQHkqnMl/) |
| Occupational risk, average premium on first registration or change of activity | 0.54355% (class I), 1.13065% (II), 2.59840% (III), 4.65325% (IV), 7.58875% (V) | none | 2026 | [LSS Art. 73](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |

## The taxable base

**SBC** is built from fixed pay plus, where pay has variable elements, the average of variable pay over the prior two months (LSS Art. 30). Cash plus in-kind payments and the proportional aguinaldo and seniority premium form part of it.

**Accrual.** Quotas accrue by months in arrears (Art. 39).

**PTU.** PTU paid is deductible for ISR (LISR Art. 9 fr. I). The PTU computation itself is on the "Not yet confirmed" line under Sources.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| IMSS cédula de determinación plus payment | By the 17th of the following month | LSS Art. 39 |
| Worker quota withholding by employer | Each payroll; if not withheld on time, the employer may recover at most four accumulated weekly quotas from the worker | LSS Art. 38 |

## Penalties and interest

Quotas or capitales constitutivos not paid on time bear inflation updating and surcharges (recargos) under the Código Fiscal de la Federación from the date they became due, without prejudice to fines (LSS Art. 40 A). Article 304 A lists the employer acts and omissions that are infractions. IMSS can assess capitales constitutivos for individual claims; they are definitive on notification (Art. 39).

## Cross-border points

- **Foreign employers.** A foreign employer with Mexican staff must register through a PE or a Mexican representative.
- Totalisation agreements and the coverage of seconded staff are on the "Not yet confirmed" line under Sources.

## Worked examples

Both examples use only the percentage-of-SBC quotas confirmed in the table above. They leave out the illness-and-maternity benefits-in-kind quotas (a fixed quota per worker plus a quota on SBC above three times the reference wage) and the employer cesantía y vejez quota, whose 2026 rates are not yet confirmed, so they are **partial** costs, not a payroll total.

### Example 1: employer quotas on a MXN 30,000 monthly SBC, class I (confirmed branches only)

Disability and life 1.75%, retirement 2%, daycare 1%, INFONAVIT 5%, class I risk premium 0.54355% and illness-and-maternity cash benefits 0.70%: together 10.99355% of SBC, MXN 3,298.07 a month.

```oa-check
name: employer quotas on 30000 SBC, confirmed branches, class I
inputs:
  sbc: 30000
  invalidez_vida: 0.0175
  retiro: 0.02
  guarderias: 0.01
  vivienda: 0.05
  prima_riesgo: 0.0054355
  dinero_patron: 0.007
steps:
  - total_patron: sbc * (invalidez_vida + retiro + guarderias + vivienda + prima_riesgo + dinero_patron)
expected:
  total_patron: 3298.07
```

### Example 2: worker quotas withheld on the same SBC (confirmed branches only)

The employer withholds disability and life 0.625%, cesantía y vejez 1.125% and cash benefits 0.25%: 2.0% of SBC, MXN 600 a month (LSS Arts. 147, 168 fr. II, 107). If the employer fails to withhold on time it may later recover at most four accumulated weekly quotas from the worker; the rest is its own cost (LSS Art. 38).

```oa-check
name: worker quotas on 30000 SBC, confirmed branches
inputs:
  sbc: 30000
  invalidez_vida: 0.00625
  cesantia_vejez: 0.01125
  dinero_obrero: 0.0025
steps:
  - total_obrero: sbc * (invalidez_vida + cesantia_vejez + dinero_obrero)
expected:
  total_obrero: 600.00
```

## Ask the client first

1. **Which risk class is registered, and does it match the actual activities** (Art. 73)?
2. **Is the SBC complete** (aguinaldo, premiums, allowances, variable pay)?
3. **Any foreign nationals or seconded staff** who may need a coverage certificate?
4. **PTU exposure:** what is the modified fiscal result, and which cap applies?
5. **In which states does the employer have staff?** State payroll tax follows the state.

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley del Seguro Social, consolidated (Cámara de Diputados), Arts. 19, 28, 30, 38, 39, 40 A, 73, 106, 107, 147, 168, 211, 304 A (last reform DOF 15-01-2026) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf | 2026-10-29 |
| Ley del Instituto del Fondo Nacional de la Vivienda para los Trabajadores, consolidated (Cámara de Diputados), Art. 29 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIFNVT.pdf | 2026-10-28 |
| INFONAVIT, employer help centre: frequently asked questions | https://portalmx.infonavit.org.mx/wps/portal/infonavitmx/mx2/patrones/centro_ayuda/preguntas_frecuentes/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zizTxdDAwtnA2MLA0NDAzM_J193ZxMTQ09w0z1C7IdFQHkqnMl/ | 2026-10-28 |
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Art. 9 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-28 |

Not yet confirmed: the 2026 illness-and-maternity benefits-in-kind quotas (Art. 106 in the consolidated text still shows the original 13.9% fixed quota and 6% / 2% excess quotas, which the 1995 law's transitional articles changed; v0.2 carried "20.6% employer and 3.0% worker" of SBC, which matches neither and overstated cost when applied to the whole SBC); the 2026 transitional employer cesantía y vejez rates under the DOF 16-12-2020 decree; whether the Art. 28 ceiling of 25 times the minimum wage is applied as 25 UMA; a "retirement, disability, survivors" employer rate of 2.375% (earlier drafts cited Art. 134; the text read puts the employer cesantía y vejez quota in Art. 168 fr. II); a daycare/INSH upper rate of 1.75% (earlier drafts cited Art. 201; Art. 211 sets 1%); the resulting employer total of roughly 20.6% plus a fixed 11.125% plus risk premium, about 31.5% at the top class; the 2026 minimum wage and SBC ceiling in pesos (DOF annual decree); INFONAVIT payment timing (earlier drafts said monthly with the IMSS cédula) and earlier drafts' citation of "INFONAVIT Art. 45"; state payroll tax (impuesto sobre nómina) rates, including the CDMX rate (v0.2 used 3% in a worked example; the CDMX Fiscal Code was not read and the example is removed); a 10% surcharge on unpaid quotas under "LSS Art. 14-A"; PTU of 10% of the modified fiscal result, half split equally and half by wages, capped per worker at the lower of 20 times the local minimum wage or three times the average wage, with directors and non-resident workers excluded (LFT Arts. 123-127), and payment within 60 days of the annual ISR return (no archived copy of the LFT); the list of totalisation agreements and the coverage of seconded staff under the Mexico-US agreement; IMSS circulars (imss.gob.mx refused scripted access).

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
