---
name: mx-cross-border
description: "Mexico cross-border income reference for 2026. Covers LISR Title V taxation of non-residents with Mexican-source income: source-of-wealth rules (Arts. 153-165), flat 25% on real-property rent and gains and on independent services (Arts. 156, 158, 160), the permanent-establishment concept, the gross-up duty of the Mexican payer, and treaty interaction. Trigger on Mexico non-resident, residente en el extranjero, fuente de riqueza, establecimiento permanente, retencion 25%, Title V. Source-cited draft."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mx-cross-border"
  jurisdiction: "MX"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Mexico cross-border (non-resident income, Title V LISR)

> **Source-cited draft.** Built from the Cámara de Diputados consolidated text of the Ley del Impuesto Sobre la Renta (LISR, last reform DOF 01-04-2024), Title V, read on 2026-10-28. No accountant has reviewed it. Do not file from it without review by a qualified Mexican professional.

Tax year: the calendar year. Currency: Mexican peso (MXN). The Servicio de Administración Tributaria (SAT) administers ISR.

See also: `mx-corporate-income-tax`, `mx-payroll-withholding`, `mexico-transfer-pricing`.

## Who this applies to

Foreign residents (individuals or corporations) earning Mexican-source income without a Mexican permanent establishment (PE) are taxed under Title V (LISR Art. 153). With a PE, they pay the ordinary regimes on income attributable to it. Art. 153 also imposes arm's-length pricing on related-party operations even for Title V taxpayers (paragraph added DOF 12-11-2021). Payments that merely benefit a foreign resident, including avoided expenses, are swept into the same net (Art. 153).

## Rates, bands and thresholds

| Income type | Rate on gross | Tax year | Source |
|---|---|---|---|
| Independent services performed in Mexico | 25% | 2026 | [LISR Art. 156](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Mexican real-property rent / land-use rights | 25% | 2026 | [LISR Art. 158](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Sale of Mexican real property | 25% on gross proceeds (a seller with an Art. 174 representative in Mexico and a public deed may opt to pay the top Art. 152 tariff rate, 35%, on the gain instead) | 2026 | [LISR Art. 160](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Shares in Mexican companies (50%+ real-estate value test) | 25% | 2026 | [LISR Art. 161](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Derivatives on Mexican shares | 25% on gain | 2026 | [LISR Art. 163](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Dividends | Corporate-level 30% via the Art. 10 gross-up when not paid out of CUFIN, plus **10% withheld** on the dividend paid to the non-resident | 2026 | [LISR Arts. 10, 164 fr. I](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |

The Mexican payer is the withholding agent; if the payer is also non-resident, the foreign recipient self-pays by declaration within 15 days of receiving the income (Arts. 158, 160).

## The taxable base

Title V flat categories are on gross with no deductions ("sin deducción alguna", Arts. 156, 158, 160). Source rules are location-based for real property (Arts. 158, 160) and place-of-performance for services, with a presumption that services are wholly performed in Mexico once part is performed there, rebuttable by proving the foreign portion (Art. 156). A related-party payment presumption also applies (Art. 156).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Self-assessment by the non-resident when the payer is also non-resident | Declaration within 15 days of the income | LISR Arts. 158, 160 |
| Transfer-pricing informative returns | Master and country-by-country (Art. 76-A fr. I, III): 31 December of the following year; local (fr. II): 15 May of the following year | LISR Art. 76-A |

## Penalties and interest

Underpaid contributions discovered by the authorities draw a fine of 55% to 75% of the omitted contributions (CFF Art. 76); CFF Art. 64 (the old 45%-85% fine) is repealed in the consolidated text read 2026-10-31. Omitted amounts plus accessories are due within 30 days of the assessment notice, with inflation updating under CFF Art. 65; recargos run at the annual variable rate of CFF Art. 22.

## Cross-border points

- **Permanent establishment.** Domestic definition in LISR Art. 2 plus treaty definitions. A construction site creates one when it lasts more than 183 days, consecutive or not, in a 12-month period, and so can a dependent agent; a person acting exclusively or almost exclusively for related foreign residents is presumed not to be an independent agent (Art. 2).
- **Treaty relief** requires a residence certificate; the Art. 156 presumption survives unless treaty residence and a PE analysis are documented.
- **Holding structures.** Art. 161's 50% real-estate look-through defeats share structures for Mexican property.

## Worked examples

### Worked example 1: non-resident rent, grossed up

A US company leases MXN 50,000/month of Mexico City warehouse space to a Mexican tenant and wants to receive 50,000 net. Art. 158 taxes 25% of gross and the tenant withholds, so the rent is grossed up: 50,000 / 0.75 = MXN 66,666.67, of which MXN 16,666.67 is withheld.

```oa-check
name: gross-up of non-resident rent 25 percent rate
inputs:
  renta_neta: 50000
  tasa: 0.25
steps:
  - renta_bruta: renta_neta / (1 - tasa)
  - retencion: renta_bruta * tasa
expected:
  renta_bruta: 66666.67
  retencion: 16666.67
```

### Worked example 2: non-resident services, grossed up

A German consultant invoices a Mexican group company MXN 80,000 net for services delivered in Mexico City (Art. 156, 25% on gross, grossed up): gross fee MXN 106,666.67, withholding MXN 26,666.67.

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

1. **Does the foreign party have a PE** (site, agent, dependent contractor)?
2. **Is the payer grossing up flat-rate income, or did the contract quote net?**
3. **Is the 50% real-estate share test** (Art. 161) hit in any share sale?
4. **Are treaty residence certificates on file** before payment?
5. **Are related-party cross-border flows mapped** to the Art. 76-A informative returns?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Arts. 2, 10, 76-A, 153, 156, 158, 160, 161, 163, 164, 166, 167, 174 (still last reformed DOF 01-04-2024 in the October 2026 copy) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-29 |
| Código Fiscal de la Federación, consolidated (Cámara de Diputados, last reform DOF 09-04-2026), Arts. 22, 64, 65, 76 | https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | 2026-10-31 |

Confirmed from the consolidated LISR read: interest rates sit in Art. 166 (4.9% for the cases in fr. II, including qualifying securities and financial-system credits; the rate becomes 10% when those requirements are not met; 15% for reinsurance companies, fr. III; 21% for the cases in fr. IV; other interest is taxed at the top marginal rate of the Art. 97 tariff, fr. V); royalty, technical assistance and advertising source rules and rates are in Art. 167 (rates by category, including 5% for railway cars and containers, 25% for technical assistance, 1% for some goods; no 35% royalty rate appears in the text read); Art. 174 governs the non-resident's representative; Art. 165 covers Title III non-profit conduit income; Art. 155 covers pensions and retirement income; the 10% dividend withholding for non-residents is Art. 164 fr. I.

Not yet confirmed: the remittance date for tax withheld from non-residents (earlier drafts said with the monthly return by the 17th of the following month); a targeted exemption for foreign pension funds on Mexican real-property gains (earlier drafts cited "the Art. 155 area"; Art. 155 in the text read covers pensions and retirement income); the domestic PE rules earlier drafts cited as Arts. 8-8A, including business carried on through a Mexican related party; the payer's joint liability for tax not withheld (no such clause found in the LISR or CFF copies read); treaty-by-treaty rates and PE thresholds (DOF/SAT); the SAT residence-certificate procedure.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mx-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mx-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
