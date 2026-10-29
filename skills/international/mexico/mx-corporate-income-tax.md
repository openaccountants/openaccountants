---
name: mx-corporate-income-tax
description: >
  Mexico corporate income tax reference for 2026. Covers the 30% LISR rate on the annual fiscal result (Art. 9), monthly provisional payments by the 17th (Art. 14), loss carryforward 10 years (Art. 57), the CUFIN/CORE dividend system with the 1.4286 gross-up and 10% additional tax (Arts. 10, 77-79), PTU deductibility, and corporate deadlines and penalties. Trigger on Mexico corporate tax, ISR personas morales, utilidad fiscal, CUFIN, perdida fiscal, pago provisional. Source-cited draft.
jurisdiction: MX
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.4
---

# Mexico corporate income tax (ISR, personas morales)

> **Source-cited draft.** Built from the Cámara de Diputados consolidated text of the Ley del Impuesto Sobre la Renta (LISR, last reform DOF 01-04-2024) and SAT pages, read on 2026-10-28. No accountant has reviewed it. Do not file from it without review by a qualified Mexican professional.

Tax year: the calendar year. Currency: Mexican peso (MXN). The Servicio de Administración Tributaria (SAT) administers ISR.

See also: `mx-cross-border` (Title V non-resident income), `mx-social-contributions` (IMSS, INFONAVIT, PTU), `mexico-transfer-pricing`.

## Who this applies to

Resident Mexican corporations (personas morales) are taxed on worldwide income (LISR Arts. 8-9). A Mexican-source rule and a permanent-establishment concept bring non-resident corporations in under Title V: see `mx-cross-border`. Mexican branches of foreign companies are taxed as resident corporations; a foreign corporation without a PE pays the Title V flat rates instead.

## Rates, bands and thresholds

| Item | Rate | Tax year | Source |
|---|---|---|---|
| Corporate ISR on the annual fiscal result | 30% | 2026 | [LISR Art. 9](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Corporate-level tax on dividends not paid out of CUFIN | 30% on the dividend grossed up by the factor 1.4286 | 2026 | [LISR Art. 10](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Additional tax on dividends paid to resident individuals | 10% | 2026 | [LISR Art. 140](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Non-resident flat rates (no PE) | 25% on rent, real-property gains and services | 2026 | LISR Arts. 156, 158, 160; see `mx-cross-border` |
| Dividends paid to non-residents | 10% withheld by the paying company | 2026 | [LISR Art. 164 fr. I](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |

No general reduced corporate rate exists in the consolidated LISR text read on 2026-10-28.

## The taxable base

**Fiscal result** (LISR Art. 9): accumulate all Title II income, subtract authorised deductions (Arts. 25-37) and PTU actually paid in the year (Art. 9 fr. I), then subtract updated prior-year loss carryforwards.

**Losses** carry forward 10 years ("los diez ejercicios siguientes", LISR Art. 57), inflation-updated, with same-line-of-business limits on mergers and control changes (Art. 57).

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

No penalty or interest figure in this domain is confirmed yet; the Código Fiscal de la Federación figures earlier drafts carried are on the "Not yet confirmed" line under Sources. IMSS contribution penalties are covered in `mx-social-contributions`.

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

The same company distributes a MXN 700,000 dividend out of post-2014 profits. The Art. 10 tax is 700,000 × 1.4286 × 30% = MXN 300,006. The 10% additional tax on the resident individual (Art. 140, second paragraph: "una tasa adicional del 10% sobre los dividendos o utilidades distribuidos", retained by the company and definitive) applies to the dividend distributed, not to the dividend plus the Art. 10 tax: 700,000 × 10% = MXN 70,000.

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
2. **Any control change or merger** that limits the loss carryforward (Art. 57)?
3. **Is every deduction backed by a CFDI** (Art. 27)?
4. **Was PTU paid in the year?** Only PTU paid reduces the base.
5. **Any payments to non-residents** that need Title V withholding before the payment date?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Arts. 8-10, 14, 25-37, 44-46, 57, 76, 76-A, 78, 140, 156, 158, 160, 164, 179-182 (still last reformed DOF 01-04-2024 in the October 2026 copy) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-29 |
| SAT, personas morales régimen general: declaraciones mensuales | http://omawww.sat.gob.mx/informacion_fiscal/obligaciones_fiscales/personas_morales/regimen_general/Paginas/declaraciones_mensuales.aspx | 2026-10-28 |

Not yet confirmed: whether CUFIN is limited to profits taxed before 2014 as earlier drafts said, and the CUFIN-non-resident account; the 35% Title V rate earlier drafts listed for some non-resident income; whether a 2025-2026 reform changed the Art. 9 rate after the DOF 01-04-2024 consolidation (the 2025-2026 rate-increase debate had not changed the text read); the annual return as a calendar date (the LISR text gives three months after year end; earlier drafts said 30 July for calendar-year taxpayers); the PTU payment deadline of 60 days after the annual return (Ley Federal del Trabajo; not read); Código Fiscal de la Federación penalties of 45%-85% for underpaid amounts (Art. 64) and 50%-150% for false returns (Art. 65), inflation updating and interest (Art. 20) and the 1.41% monthly rate (no archived copy of the CFF); treaty-by-treaty withholding rates; the 2026 UMA and minimum wage; current SAT tariff tables.

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
