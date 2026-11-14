---
name: mx-corporate-income-tax
description: "Mexico corporate income tax reference for 2026. Covers the 30% LISR rate on the annual fiscal result (Art. 9), monthly provisional payments by the 17th (Art. 14), loss carryforward 10 years (Art. 57), the CUFIN/CORE dividend system with the 1.4286 gross-up and 10% additional tax (Arts. 10, 77-79), PTU deductibility, and corporate deadlines and penalties. Trigger on Mexico corporate tax, ISR personas morales, utilidad fiscal, CUFIN, perdida fiscal, pago provisional. Source-cited draft."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mx-corporate-income-tax"
  jurisdiction: "MX"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Mexico corporate income tax (ISR, personas morales)

> **Source-cited draft.** Built from the Cámara de Diputados consolidated text of the Ley del Impuesto Sobre la Renta (LISR, last reform DOF 01-04-2024) and SAT pages, read on 2026-10-28. No accountant has reviewed it. Do not file from it without review by a qualified Mexican professional.

Tax year: the calendar year. Currency: Mexican peso (MXN). The Servicio de Administración Tributaria (SAT) administers ISR.

See also: `mx-cross-border` (Title V non-resident income), `mx-social-contributions` (IMSS, INFONAVIT, PTU), `mexico-transfer-pricing`.

## Who this applies to

Resident Mexican corporations (personas morales) are taxed on all their income regardless of where the source of wealth is located (LISR Art. 1 fr. I: "Las residentes en México, respecto de todos sus ingresos, cualquiera que sea la ubicación de la fuente de riqueza de donde procedan"); Art. 8 imposes the Title III obligation on those residents and Art. 9 sets the 30% rate. A Mexican-source rule and a permanent-establishment concept bring non-resident corporations in under Title V: see `mx-cross-border`. Mexican branches of foreign companies are taxed as resident corporations; a foreign corporation without a PE pays the Title V flat rates instead.

## Rates, bands and thresholds

| Item | Rate | Tax year | Source |
|---|---|---|---|
| Corporate ISR on the annual fiscal result | 30% | 2026 | [LISR Art. 9, DOF 11-12-2013 (text: "aplicando al resultado fiscal obtenido en el ejercicio la tasa del 30%")](https://dof.gob.mx/nota_detalle.php?codigo=5325371&fecha=11/12/2013) |
| Corporate-level tax on dividends not paid out of CUFIN | 30% on the dividend grossed up by the factor 1.4286 | 2026 | [LISR Art. 10, DOF 11-12-2013](https://dof.gob.mx/nota_detalle.php?codigo=5325371&fecha=11/12/2013) |
| Additional tax on dividends paid to resident individuals | 10%, withheld by the paying company | 2026 | [LISR Art. 140, DOF 11-12-2013 ("tasa adicional del 10%")](https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013) |
| Non-resident flat rates (no PE) | 25% of the gross income, no deductions, on independent services (Art. 156), real property rent (Art. 158) and real property disposals (Art. 160, or the elective rate on the gain); see `mx-cross-border` | 2026 | [LISR Arts. 156, 158, 160, DOF 11-12-2013 ("la tasa del 25% sobre el total del ingreso obtenido")](https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013) |
| Dividends paid to non-residents | 10% withheld by the paying company | 2026 | [LISR Art. 164 fr. I, DOF 11-12-2013 ("la tasa del 10% sobre dichos dividendos")](https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013) |

No general reduced corporate rate exists in the consolidated LISR text read on 2026-10-28.

## The taxable base

**Fiscal result** (LISR Art. 9): accumulate all Title II income, subtract authorised deductions (Arts. 25-37) and PTU actually paid in the year (Art. 9 fr. I), then subtract updated prior-year loss carryforwards.

**Losses** carry forward 10 years ("los diez ejercicios siguientes", LISR Art. 57), inflation-updated. Same-line-of-business limits apply on mergers (fusión) and on a change of controlling shareholders (Art. 58); Art. 57 itself limits losses in spin-offs (escisión).

**Timing.** Accrual basis; inflation adjustment applies to certain items (Arts. 44-46). Deductions require CFDI invoice compliance (Art. 27).

**Dividends.** The Art. 10 tax does not apply when the dividend comes out of the Cuenta de Utilidad Fiscal Neta (CUFIN). Otherwise the paying company grosses the dividend up by the factor 1.4286 and pays 30% (Art. 10). Capital reductions are recharacterised through the CUFIN waterfall (Art. 78).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Monthly provisional ISR payments | By the 17th of the following month, on the prior year's utilidad/ingresos coefficient | LISR Art. 14; [SAT, declaraciones mensuales](http://omawww.sat.gob.mx/informacion_fiscal/obligaciones_fiscales/personas_morales/regimen_general/Paginas/declaraciones_mensuales.aspx) |
| Annual ISR return | Within three months of year end ("dentro de los tres meses siguientes a la fecha en que termine dicho ejercicio") | LISR Art. 76 fr. V |
| Related-party operations informative return | By 15 May of the following year | LISR Art. 76 fr. X |
| Transfer-pricing informative returns (Art. 76-A) | Fractions I and III (master and country-by-country): by 31 December of the following year; fraction II (local): by 15 May of the following year | LISR Art. 76-A, final paragraphs |

## Penalties and interest

CFF Art. 64 (the old 45%-85% fine for underpaid amounts) is repealed ("Artículo 64.- (Se deroga).") in the consolidated CFF read 2026-10-31. Underpaid contributions discovered by the tax authorities now draw a fine of 55% to 75% of the omitted contributions (CFF Art. 76); declaring a fiscal loss larger than the real one draws 30% to 40% of the difference (Art. 76, later paragraphs). Omitted contributions plus accessories are due within 30 days of the assessment notice (Art. 65), which also governs inflation updating. Recargos (CFF Art. 22) are an annual variable-rate charge on fiscal credits, not a fixed 1.41% monthly figure. IMSS contribution penalties are covered in `mx-social-contributions`.

## Cross-border points

- **Payments to non-residents without a PE** trigger Title V withholding: rent and real-property gains 25% flat (LISR Arts. 158, 160), services 25% flat (Art. 156). They are usually grossed up because the Mexican payer owes the tax as retentor. See `mx-cross-border`.
- **Treaty relief** requires the beneficiary to prove residence.
- **Transfer pricing** runs through Arts. 76 fr. XII, 179-182 and the master/local informative returns (Art. 76-A). See `mexico-transfer-pricing`.

## Worked examples

### Worked example 1: corporate tax with a loss carryforward

A Mexican S.A. de C.V. has MXN 12,000,000 acumulable income, MXN 8,500,000 authorised deductions, pays PTU of MXN 400,000, and has an updated loss carryforward of MXN 2,000,000 from two years ago. Utilidad fiscal is MXN 3,100,000; after the loss the resultado fiscal is MXN 1,100,000, and ISR at 30% is MXN 330,000.

```oa-check
name: corporate tax with loss carryforward
inputs:
  ingresos: 12000000
  deducciones: 8500000
  ptu_pagada: 400000
  perdida_cf: 2000000
  tasa: 0.3
steps:
  - utilidad_fiscal: ingresos - deducciones - ptu_pagada
  - resultado_fiscal: utilidad_fiscal - perdida_cf
  - impuesto: resultado_fiscal * tasa
expected:
  utilidad_fiscal: 3100000.00
  resultado_fiscal: 1100000.00
  impuesto: 330000.00
```

### Worked example 2: dividend not paid out of CUFIN

The same company distributes a MXN 700,000 dividend out of post-2014 profits. The Art. 10 tax is 700,000 × 1.4286 × 30% = MXN 300,006 (the statute itself prescribes the gross-up: "éstos se deberán multiplicar por el factor de 1.4286 y al resultado se le aplicará la tasa del artículo 9 de esta Ley"). The 10% additional tax on the resident individual (Art. 140, second paragraph: "una tasa adicional del 10% sobre los dividendos o utilidades distribuidos", retained by the company and definitive) applies to the dividend distributed, not to the dividend plus the Art. 10 tax: 700,000 × 10% = MXN 70,000.

```oa-check
name: dividend gross-up and 10 percent additional tax
inputs:
  dividendo: 700000
  factor: 1.4286
  tasa: 0.3
  adicional: 0.1
steps:
  - impuesto_dividendo: dividendo * factor * tasa
  - impuesto_adicional: dividendo * adicional
expected:
  impuesto_dividendo: 300006.00
  impuesto_adicional: 70000.00
```

## Ask the client first

1. **Is the CUFIN balance enough for planned distributions?** A dividend outside CUFIN bears the Art. 10 tax.
2. **Any control change or merger** that limits the loss carryforward (Art. 58)?
3. **Is every deduction backed by a CFDI** (Art. 27)?
4. **Was PTU paid in the year?** Only PTU paid reduces the base.
5. **Any payments to non-residents** that need Title V withholding before the payment date?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Arts. 8-10, 14, 25-37, 44-46, 57, 76, 76-A, 78, 140, 156, 158, 160, 164, 179-182 (still last reformed DOF 01-04-2024 in the October 2026 copy) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-29 |
| SAT, personas morales régimen general: declaraciones mensuales | http://omawww.sat.gob.mx/informacion_fiscal/obligaciones_fiscales/personas_morales/regimen_general/Paginas/declaraciones_mensuales.aspx | 2026-10-28 |
| DOF 11-12-2013, decree issuing the Ley del Impuesto Sobre la Renta, first part (Arts. 1 to 75), read for Art. 9 (30%) and Art. 10 (1.4286 gross-up) | https://dof.gob.mx/nota_detalle.php?codigo=5325371&fecha=11/12/2013 | 2026-11-14 |
| DOF 11-12-2013, same decree, second part (Arts. 76 onward), read for Art. 140 (additional 10%), Arts. 156, 158 and 160 (25%) and Art. 164 (10% dividends to non-residents) | https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013 | 2026-11-14 |
| Código Fiscal de la Federación, consolidated (Cámara de Diputados, last reform DOF 09-04-2026), Arts. 22, 64, 65, 75, 76 | https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | 2026-10-31 |

Not yet confirmed: how the 10% additional dividend tax (Art. 140, second paragraph) applies to non-resident shareholders; whether CUFIN is limited to profits taxed before 2014 as earlier drafts said, and the CUFIN-non-resident account; whether a 2025-2026 reform changed the Art. 9 rate after the DOF 01-04-2024 consolidation (the 2025-2026 rate-increase debate had not changed the text read; the consolidated copy read on 2026-10-29 still shows 30%); the annual return as a calendar date (the LISR text gives three months after year end; earlier drafts said 30 July for calendar-year taxpayers); the PTU payment deadline of 60 days after the annual return (Ley Federal del Trabajo; not read); treaty-by-treaty withholding rates; the 2026 minimum wage; current SAT tariff tables. The consolidated LISR read contains no 35% rate anywhere in Title V (the 25% rates in Arts. 156, 158, 160 and the interest tiers in Art. 166 are the flat rates), so the "35% Title V rate" earlier drafts listed is not carried.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mx-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mx-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
