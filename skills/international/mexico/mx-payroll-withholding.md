---
name: mx-payroll-withholding
description: >
  Mexico payroll withholding reference for 2026. Covers employer ISR withholding on wages under LISR Arts. 94-99 and the SAT monthly tariff tables, the February annual adjustment, monthly payment by the 17th, aguinaldo and PTU treatment on the payroll, and gross-up duties for payments to non-residents. Trigger on Mexico payroll, retencion ISR salarios, tabuladores SAT, aguinaldo, determinacion mensual. Source-cited draft.
jurisdiction: MX
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.3
---

# Mexico payroll withholding (ISR retenciones)

> **Source-cited draft.** Built from the Cámara de Diputados consolidated text of the Ley del Impuesto Sobre la Renta (LISR, last reform DOF 01-04-2024), Title IV Chapter I, read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Mexican professional.

Tax year: the calendar year. Currency: Mexican peso (MXN). The Servicio de Administración Tributaria (SAT) administers ISR and publishes the withholding tariffs.

See also: `mx-social-contributions` (IMSS, INFONAVIT, PTU), `mx-income-tax`, `mx-cross-border`.

## Who this applies to

Any employer that pays wages withholds ISR each calendar month (LISR Art. 96) by applying the SAT monthly tariff: cuota fija plus the marginal rate on the excess over the bracket floor. The withholding is a provisional payment on account of the worker's annual ISR (Art. 96). The employer does not make the annual calculation for a worker whose wages for the year exceed MXN 400,000 (Art. 97, last paragraph, item (b)); such a worker files their own annual return (Art. 150).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Monthly wage withholding | SAT monthly tariff for 2026: 1.92% from MXN 0.01 rising to 35% over MXN 425,642.00 a month (cuota fija MXN 133,488.54 on the top band); full table in RMF 2026 Anexo 8, A.V | 2026 | [LISR Art. 96](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [RMF 2026 Anexo 8](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf) |
| Aguinaldo and other year-end bonuses paid to all staff | Exempt up to 30 days of the general minimum wage of the worker's area; the rest taxed | 2026 | LISR Art. 93 fr. XIV |
| PTU (employee profit share) | Exempt up to 15 days of the general minimum wage of the worker's area; the rest taxed | 2026 | LISR Art. 93 fr. XIV |
| Prima vacacional paid to all staff | Exempt up to 15 days of the general minimum wage of the worker's area | 2026 | LISR Art. 93 fr. XIV |
| Wages above which the employer does not make the annual calculation | MXN 400,000 a year | 2026 | LISR Art. 97, last paragraph, item (b) |
| Payment to a non-resident for services performed in Mexico | 25% of the gross, no deductions | 2026 | LISR Art. 156 |

## The taxable base

Taxable payroll includes wages, seniority premiums, aguinaldo, bonuses and cash allowances (Art. 94). Exempt items include the Art. 93 fr. XIV amounts above and savings-fund contributions within limits (Art. 93). Withholding is computed per calendar month (Art. 96).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Payment of tax withheld from wages | By the 17th of the following month | LISR Art. 96 |
| Annual calculation for employees, and payment of any difference | By February of the following year | LISR Art. 97 |
| Employee annual return (when obliged) | During April of the following year | LISR Art. 150 |

## Penalties and interest

No penalty or interest figure in this domain is confirmed yet; see the "Not yet confirmed" line under Sources.

## Cross-border points

- **Payments to non-resident individuals for personal services performed in Mexico** bear 25% on the gross, withheld by the Mexican payer. Services are presumed wholly performed in Mexico once part is performed there, and payments by a Mexican resident to a foreign related party are presumed Mexican-source (LISR Art. 156). A payer that quotes the fee net grosses it up (example 2).

## Worked examples

### Worked example 1: monthly withholding on a MXN 25,000 salary (2026 tariff)

The 2026 monthly Art. 96 tariff (RMF 2026 Anexo 8, A.V) puts MXN 25,000 in the band from MXN 17,533.65 to 35,362.83: cuota fija MXN 1,856.84 plus 21.36% on the excess. The excess is MXN 7,466.35 and the withholding MXN 3,451.65. (v0.2 used the 2025 band, floor 15,487.72 and cuota 1,640.18, giving MXN 3,672.00; that is the 2025 figure, not 2026.)

```oa-check
name: monthly ISR withholding 25000 salary 2026 tariff
inputs:
  salario: 25000
  limite_inferior: 17533.65
  cuota_fija: 1856.84
  tasa_marginal: 0.2136
steps:
  - excedente: salario - limite_inferior
  - impuesto_mensual: cuota_fija + excedente * tasa_marginal
expected:
  excedente: 7466.35
  impuesto_mensual: 3451.65
```

### Worked example 2: non-resident instructor paid net

An employer pays a non-resident instructor MXN 80,000 net for a Mexico City course (Art. 156, 25% on gross; the payer grosses up): gross fee MXN 106,666.67, withholding MXN 26,666.67.

```oa-check
name: gross-up of non-resident services 25 percent rate
inputs:
  fee_neta: 80000
  tasa: 0.25
steps:
  - fee_bruta: fee_neta / (1 - tasa)
  - retencion: fee_bruta * tasa
expected:
  fee_bruta: 106666.67
  retencion: 26666.67
```

## Ask the client first

1. **Is the current SAT tariff loaded in payroll** for the year being run?
2. **Are exempt items coded correctly** (aguinaldo up to 30 days and PTU up to 15 days of minimum wage, savings-fund contributions)?
3. **Will any employee earn more than MXN 400,000 this year?** You do not make that worker's annual calculation.
4. **Any foreign instructors or contractors paid net?** The 25% Title V withholding has to be grossed up.
5. **Is the February annual calculation calendared?**

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Arts. 93, 94, 96, 97, 150, 156 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-28 |
| SAT, Resolución Miscelánea Fiscal 2026, Anexo 8 (DOF 28-12-2025), monthly Art. 96 tariff for 2026 (A.V); read from the Internet Archive copy | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf | 2026-10-29 |
| SAT, Resolución Miscelánea Fiscal 2025, Anexo 8 (ISR tariffs for 2025) | http://omawww.sat.gob.mx/normatividad_RMF_RGCE/Paginas/documentos2025/rmf/anexos/Anexo8_RMF2025-30122024.pdf | 2026-10-28 |

Not yet confirmed: whether the minimum-wage references in LISR Art. 93 fr. XIV are read as the UMA (the law text says salario mínimo); aguinaldo of at least 15 days' wages (LFT Art. 87; no archived copy of the LFT); PTU being taxed at the annual tariff rather than through the payroll tables (earlier drafts cited LISR Art. 98); proration rules for multi-month or irregular payments (earlier drafts cited Arts. 96, 106); the worker's annual-return thresholds as they apply in 2026; earlier drafts' rule that a seconded employee becomes Mexican resident after 183 days (cited as Art. 9; the 183-day test found in the text read is the construction-PE rule in Art. 2); Código Fiscal de la Federación penalties of 45%-85% and 50%-150% (Arts. 64-65), updating and interest (Art. 20) and the employer's joint liability for ISR withheld but not paid (no archived copy of the CFF); savings-fund exemption limits for 2026.

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
