---
name: cl-corporate-income-tax
description: "Chile first category tax (impuesto de primera categoría, IDPC) of companies for tax year 2026 (año comercial 2026, declared in April 2027, año tributario 2027) under DL 824 art. 14 and art. 20. Covers the general semi-integrated regime of art. 14 A at 27% for 2026 under Ley 21.850 (falling to 25.5%, 24% and 23% from 2027), the Régimen Pro Pyme of art. 14 D No. 3 at 12.5% for 2025 to 2027 under Ley 21.755 art. 25 (15% in 2028), its eligibility (capital up to 85,000 UF at start, average gross income up to 75,000 UF, no year above 85,000 UF, passive income up to 35%), the transparency option of art. 14 D No. 8, the savings incentive of art. 14 E, cash-basis base and instant depreciation, PPM, the 35% IDPC restitution, losses, art. 21 rejected expenses, Impuesto Adicional withholding on dividends, interest and royalties, F22 lines and penalties. Trigger on: impuesto primera categoría 2026, Pro Pyme, 14 D, 14 A, semi integrado, transparencia tributaria, PPM, Chile corporate tax. Out of scope: individuals in cl-income-tax."
version: 1.0
jurisdiction: CL
tax_year: 2026
tax_year_notes: "Año comercial 2026, año tributario 2027"
last_updated: 2026-11-11
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Chile: first category tax for companies (2026) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Chile taxes business profits with the first category tax (impuesto de primera categoría, IDPC) and then taxes the owners with the final taxes: the Impuesto Global Complementario (IGC) for resident individuals and the Impuesto Adicional (IA) for non-residents. The IDPC paid is a credit against the final tax. This skill covers the company side for the 2026 income year.

Linked skills, not repeated here:

- [cl-income-tax](cl-income-tax.md): the owner's IGC, the scale, the UTA and the dividend credit in the owner's return.
- [cl-vat-return](cl-vat-return.md): IVA, the electronic purchase and sales register (RCV) and Form F29.
- [cl-company-formation](cl-company-formation.md): forming the entity.

**Which text of the law.** DL 824, Ley sobre Impuesto a la Renta (LIR), LeyChile version of 17 October 2026. That consolidated text already shows the permanent 23% rate that Ley 21.850 (published 17 October 2026) writes into art. 20. The rate for 2026 income is set by Ley 21.850's sixth transitory article (27% for art. 14 A) and by Ley 21.755 art. 25 (12.5% for Pro Pyme). Use those transitory rates, not the headline in art. 20, for 2026.

## Who this applies to

- **First category taxpayers.** Income from capital and from companies: commerce, industry, mining, services and other activities of art. 20 No. 3 to 5, rent of property and capital income (art. 20 No. 1 and 2), whether earned by a company or an individual entrepreneur with accounts.
- **General regime, art. 14 A (semi-integrated).** Every company that is not in the Pro Pyme regime and has owners who pay final taxes. Full accounts, monetary correction (art. 41), the tax registers RAI, DDAN, REX and SAC (art. 14 A No. 2).
- **Régimen Pro Pyme, art. 14 D No. 3.** A company is a Pyme when, together (art. 14 D No. 1):
  - its effective capital at the start of activities was no more than 85,000 UF (UF of the first day of the start month);
  - its average annual gross income from its business over the three previous years is no more than 75,000 UF, and stays so while in the regime. The 75,000 UF average may be exceeded once; gross income of any single year may never exceed 85,000 UF. UF of the last day of each year; VAT excluded; income of related companies (CT art. 8 No. 17) is added;
  - passive income (rent and capital income of art. 20 No. 1 and 2, except agricultural land; shares in partnerships; holding shares or fund units) is no more than 35% of its gross business income.
  A company meeting these conditions at start of activities is in Pro Pyme by law unless it chooses otherwise; an existing company opts in by notice to SII between 1 January and 30 April of the year it joins (art. 14 D No. 5).
- **Transparency option, art. 14 D No. 8.** A Pyme whose owners all pay final taxes (including owners in the exempt IGC band) may choose to be exempt from IDPC; the owners pay IGC on the company's base, withdrawn or not.
- **Out of scope.** Art. 14 G entities with no owners subject to final taxes (foundations, state-owned companies), presumed-income regimes (art. 34), mining royalty, and the individual's IGC.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| IDPC, general regime art. 14 A, income earned or received in 2026 | 27% | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=1229250 (Ley 21.850, art. 6 transitorio a) |
| IDPC, art. 14 A, later years | 25.5% (2027), 24% (2028), 23% from 2029 | 2027-2029 | same, art. 6 transitorio b) to d); not for art. 14 G entities in 2026 and 2027 |
| IDPC, Régimen Pro Pyme art. 14 D No. 3, income of 2025, 2026 and 2027 | 12.5%, if at each year end the employer pension contribution of Ley 21.735 art. 4 transitorio is 1%, 3.5% and 4.25% respectively | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=1214890 (Ley 21.755, art. 25) |
| IDPC, Pro Pyme, income of 2028 | 15%, if that contribution is 5% at the 2028 year end | 2028 | same, art. 25 last paragraph |
| SII reading of the contribution condition | Deemed met for every year to 2028 | 2025-2028 | https://www.sii.cl/normativa_legislacion/circulares/2025/circu53.pdf (Circular 53/2025) |
| Permanent IDPC rate after the transitory periods | 23% (art. 20 as amended by Ley 21.850 art. 8 No. 3) | from 2029 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 20) |
| Pro Pyme eligibility: capital at start | Up to 85,000 UF | 2026 | same, art. 14 D No. 1 (a) |
| Pro Pyme eligibility: average gross income, 3 years | Up to 75,000 UF; may be exceeded once; any one year up to 85,000 UF | 2026 | same, art. 14 D No. 1 (b) |
| Pro Pyme eligibility: passive income | Up to 35% of gross business income | 2026 | same, art. 14 D No. 1 (c) |
| PPM, Pro Pyme (art. 14 D No. 3 (k)) | 0.25% of gross income in the first year and where prior-year income was up to 50,000 UF; 0.5% above 50,000 UF | 2026 | same, art. 14 D No. 3 (k) |
| PPM, Pro Pyme at the 12.5% rate | Halved for 2025, 2026 and 2027 | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=1214890 (Ley 21.755, art. 25, second paragraph) |
| PPM, general regime (art. 84 a) | Prior-year IDPC as % of prior-year gross income, adjusted; 1% when not determinable (first year, prior loss) | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 84 a) |
| Savings incentive, art. 14 E (14 A and 14 D No. 3; average income up to 100,000 UF) | Deduct up to 50% of the RLI kept invested, cap 5,000 UF (UF at year end) | 2026 | same, art. 14 E |
| Sole tax on rejected expenses benefiting owners or related parties (art. 21 first paragraph) | 40% | 2026 | same, art. 21 |
| Restitution of IDPC credit from 14 A companies, against IGC or IA | 35% of the credit; not for IA payers resident in a treaty country whose treaty lets the IDPC be deducted | 2026 | same, arts. 56 No. 3 and 63 |
| Restitution phase-out (Ley 21.850) | 30% for credits of AT 2028, 20% for AT 2029, then none | 2027-2029 | https://www.bcn.cl/leychile/navegar?idNorma=1229250 (art. 5 transitorio) |
| Impuesto Adicional on dividends and withdrawals to non-residents | 35%, with credit for the IDPC (art. 63) | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 58 No. 1, 2) |
| Impuesto Adicional on interest to non-residents | 35%; 4% on interest on foreign-currency deposits, loans from foreign banks or financial institutions, deferred import prices, foreign-currency bonds of Chilean companies | 2026 | same, art. 59 No. 1 |
| Impuesto Adicional on royalties | 30% (marks, patents, formulas); 15% (patents of invention, utility models, designs, plant varieties, software, author's rights); standard software exempt; 30% to a preferential regime (art. 41 H) | 2026 | same, art. 59 |

## The base

**General regime (art. 14 A).** The base is the renta líquida imponible (RLI): gross income less cost of sales, then less the expenses necessary to produce income (art. 31), with full accounts and annual monetary correction of equity, assets and liabilities by CPI (art. 41). Losses of earlier years are deducted in the next year and so on, updated by CPI; dividends received do not absorb losses, and a change of ownership plus change of business blocks pre-change losses (art. 31 No. 3). Rejected expenses that benefit owners or related parties pay the 40% sole tax of art. 21. On F22 the base is built in Recuadro N° 12 and the tax goes on line 55 (codes 1109, 1111, 1113).

**Pro Pyme (art. 14 D No. 3).** Simplified accounts may be chosen between 1 January and 30 April (art. 14 D No. 3, first paragraph). The base is cash-based: business income received less expenses paid in the year (letter f), except dealings with related 14 A companies, which go on accruals. The Pyme is freed from monetary correction (letter c), depreciates fixed assets fully in the year bought (letter d), and expenses stock and inputs bought in the year (letter e). Losses of earlier years are an expense (letter f (ii)). Dividends from 14 A or 14 D No. 3 companies are not part of the base (letter f (i)). On F22 the base is built in Recuadro N° 17 (total income code 1410, total expenses code 1430, base code 1440) and the tax goes on line 54 (codes 18, 19, 20). SII offers a proposed return from the electronic purchase and sales register between 15 and 30 April (letter a).

**Transparency (art. 14 D No. 8).** The same cash base, no IDPC; the base is allocated to the owners in proportion to their share and taxed in their IGC (art. 14 D No. 8 (a) (i)).

**Savings incentive (art. 14 E).** A 14 A or 14 D No. 3 company with average income up to 100,000 UF may deduct up to 50% of the RLI it keeps invested (RLI less art. 21 items and less amounts withdrawn or distributed in the year), capped at 5,000 UF. Recuadro N° 17 code 1432 for Pro Pyme.

**Owner credit.** When profits are withdrawn or distributed, the owner adds the IDPC credit to the amount (gross-up) and deducts it from IGC or IA (arts. 54 No. 1, 56 No. 3, 58, 63). For a 14 A company, 35% of that credit is paid back by the owner (restitution), so a resident owner keeps 65% of it; a non-resident in a treaty country with the IDPC-deduction clause keeps all of it. Credits from Pro Pyme profits carry no restitution unless they come from 14 A companies.

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| PPM on monthly gross income | Monthly, in F29 (Pro Pyme and general first category PPM, line 69, code 62) | LIR art. 84; SII F29 |
| Opt into Pro Pyme, or choose simplified accounts | 1 January to 30 April of the year | LIR art. 14 D No. 3 and No. 5 |
| SII proposal for Pyme returns | Between 15 and 30 April 2027 | LIR art. 14 D No. 3 (a) |
| Annual return F22 for 2026 and payment of the balance | During April 2027 | LIR arts. 65 No. 1, 69, 72 |
| Companies whose balance closes in June | October of the same year | LIR art. 69 No. 1 |
| Balance due is paid updated by CPI | From the month before year end to the month before the payment date | LIR art. 72 |
| Refund of excess PPM | Within 30 days after the normal filing deadline | LIR art. 97 |

**How to file.** Log in at sii.cl with the company RUT and Clave Tributaria, open Servicios Online, Declaración de Renta, and file F22 for AT 2027. Complete the base box for the regime (Recuadro N° 12 for 14 A, N° 17 for Pro Pyme, N° 22 for transparency), carry the base and tax to line 54 or 55, deduct PPM on line 85 (code 1904 for first category PPM) and other credits, and check the result in code 305. A refund lands in the bank account in codes 301, 306 and 780; a balance due is paid in code 91 by the April deadline. The company also files the sworn statements (declaraciones juradas) on withdrawals, dividends and credits that feed its owners' F22. Codes here are from the F22 for AT 2026; check the AT 2027 form.

## Penalties and interest

Under the Código Tributario (DL 830):

- **Late return that is the basis of a tax:** 10% of the tax if up to 5 months late, then 2% more per month or part, up to 30% (CT art. 97 No. 2).
- **Incomplete or wrong return** that could lower the tax, without due diligence: 5% to 20% of the difference (art. 97 No. 3).
- **Maliciously false return or accounts:** 100% to 300% of the tax evaded, and prison (art. 97 No. 4).
- **Late payment of tax withheld** (Impuesto Adicional, IUSC, boleta withholding): 10% plus 2% a month up to 30%; 20% and 60% when found in an audit (art. 97 No. 11).
- **Late payment interest:** CPI update plus penal interest at the CMF one-year rate plus 3.5%, fixed by SII each semester: 7.70% a year (0.0213888889% a day) for 1 July to 31 December 2026 (CT art. 53).

## Cross-border points

- **Withholding on payments abroad.** The Chilean payer withholds the Impuesto Adicional on dividends and withdrawals (35% with the IDPC credit, art. 74 No. 4), interest (35% or 4%) and royalties (30% or 15%) at the rates in the table. Treaties may reduce them; treaty rates are not covered here.
- **Dividends to a non-resident from a 14 A company (2026).** On a gross dividend of 100 that bore 27 of IDPC: IA 35 less credit 27 = 8 for a treaty resident whose treaty has the deduction clause; otherwise the 35% restitution of the credit (9.45) is added, 17.45 in total (arts. 58, 63).
- **Foreign tax.** Credits for tax paid abroad under art. 41 A; transfer pricing (art. 41 E) and thin capitalisation (art. 41 F) are separate topics, not covered here.

## Two worked examples that recompute

UTA December 2026 = CLP 873,624 (SII), for the owner's IGC in example 2.

### Example 1: Pro Pyme company, 12.5%, against the general regime

Andes Digital SpA is in Pro Pyme. In 2026 it received CLP 300,000,000 of business income and paid CLP 220,000,000 of expenses, including a server bought and paid in March (fully depreciated in the year, art. 14 D No. 3 (d)). Its prior-year income was under 50,000 UF, so its PPM rate is 0.25%, halved to 0.125% (Ley 21.755 art. 25), CLP 375,000 for the year.

Base (code 1440): CLP 80,000,000. IDPC at 12.5%: CLP 10,000,000 (line 54). Less PPM CLP 375,000: balance CLP 9,625,000 due by April 2027. Had the company been in the general regime, the same base would bear 27%, CLP 21,600,000, before monetary correction and accrual adjustments.

```oa-check
name: CL IDPC 2026, Pro Pyme 12.5% against 14 A 27%
inputs:
  income_received: 300000000
  expenses_paid: 220000000
  ppm_rate: 0.00125
  propyme_rate: 0.125
  general_rate: 0.27
steps:
  - base: income_received - expenses_paid
  - idpc_propyme: base * propyme_rate
  - ppm: income_received * ppm_rate
  - balance_due: idpc_propyme - ppm
  - idpc_general: base * general_rate
  - nonresident_ia_treaty: 35 - 27
  - nonresident_ia_no_treaty: 35 - 27 + 27 * 0.35
expected:
  base: 80000000
  idpc_propyme: 10000000
  ppm: 375000
  balance_due: 9625000
  idpc_general: 21600000
  nonresident_ia_treaty: 8
  nonresident_ia_no_treaty: 17.45
```

### Example 2: Pro Pyme with IDPC, or transparency? Two owners

A one-owner Pyme expects a base of CLP 40,000,000 for 2026 and will keep all of it in the company. Should it stay in art. 14 D No. 3 or choose transparency under No. 8?

- **Under No. 3:** the company pays IDPC of 12.5%, CLP 5,000,000, now. The owner pays nothing until he withdraws.
- **Under No. 8:** no IDPC; the owner is taxed on CLP 40,000,000 in his own IGC even though he takes nothing out.

The figure that decides is the owner's IGC on the extra CLP 40,000,000 against 12.5% of it (CLP 5,000,000).

- **Owner A has no other income.** CLP 40,000,000 is 45.79 UTA, the 8% band: IGC = 40,000,000 x 8% - 1.74 x 873,624 = CLP 1,679,894.24. Transparency costs CLP 3,320,105.76 less now. If he later withdraws everything under No. 3, the CLP 5,000,000 credit (no restitution) against the same IGC gives a refund of the same CLP 3,320,105.76: with everything withdrawn the two regimes come to the same total, and No. 8 simply avoids paying it early.
- **Owner B already has a base of 150 UTA (CLP 131,043,600).** His IGC rises from CLP 25,492,348.32 to CLP 39,492,348.32, so the extra profit costs CLP 14,000,000 (35% band). Staying in No. 3 and retaining costs CLP 5,000,000 now. No. 3 wins for him while profits stay in the company.

```oa-check
name: CL Pro Pyme 2026, No. 3 against No. 8 transparency, two owners
inputs:
  uta: 873624
  profit: 40000000
  owner_b_other_uta: 150
steps:
  - idpc_no3: profit * 0.125
  - owner_a_igc_no8: round(profit * 0.08 - 1.74 * uta, 2)
  - owner_a_saving_no8: idpc_no3 - owner_a_igc_no8
  - owner_b_base_before: owner_b_other_uta * uta
  - owner_b_igc_before: round(owner_b_base_before * 0.35 - 23.32 * uta, 2)
  - owner_b_igc_after: round((owner_b_base_before + profit) * 0.35 - 23.32 * uta, 2)
  - owner_b_cost_no8: owner_b_igc_after - owner_b_igc_before
expected:
  idpc_no3: 5000000
  owner_a_igc_no8: 1679894.24
  owner_a_saving_no8: 3320105.76
  owner_b_base_before: 131043600
  owner_b_igc_before: 25492348.32
  owner_b_igc_after: 39492348.32
  owner_b_cost_no8: 14000000
```

## Ask the client first

1. Which regime is the company in now (14 A, 14 D No. 3, 14 D No. 8), and when did it start activities, with what capital?
2. Gross business income for each of the last three years and for 2026, in UF at each year end, including related companies' income (85,000 UF and 75,000 UF tests), and how much is passive income (35% test)?
3. Does it keep full or simplified accounts, and which expenses and fixed assets were paid in 2026 (Pro Pyme is cash-based)?
4. Will profits be withdrawn or kept, and what are the owners' other incomes and residence (the IGC and IA side, treaty)?
5. PPM paid each month in F29, and losses carried from earlier years.
6. Payments abroad in 2026 (dividends, interest, royalties, services) and the recipient's country.

## Sources

| Source | URL | Read on |
|---|---|---|
| DL 824, LIR, LeyChile version of 17 Oct 2026 (LeyChile XML export): arts. 14 A, 14 D Nos. 1, 3, 5, 8, 14 E, 14 G, 20, 21, 31 No. 3, 41, 56 No. 3, 58, 59, 63, 65, 69, 72, 74 No. 4, 84, 97 | https://www.bcn.cl/leychile/navegar?idNorma=6368 | 2026-11-11 |
| Ley 21.850, Reconstrucción Nacional (DO 17 Oct 2026): art. 8 Nos. 1 and 3, art. 9, transitory arts. 5, 6, 7 and 9 | https://www.bcn.cl/leychile/navegar?idNorma=1229250 | 2026-11-11 |
| Ley 21.755 (2025): art. 25 (Pro Pyme 12.5% for 2025 to 2027, 15% for 2028, PPM halved) | https://www.bcn.cl/leychile/navegar?idNorma=1214890 | 2026-11-11 |
| DL 830, Código Tributario, version of 17 Oct 2026: arts. 8 No. 17, 53, 97 Nos. 2, 3, 4, 11 | https://www.bcn.cl/leychile/navegar?idNorma=6374 | 2026-11-11 |
| Read for the figures named: SII Circular 53/2025 (Pro Pyme 12.5% and 15%, contribution condition deemed met to 2028, PPM halving months) | https://www.sii.cl/normativa_legislacion/circulares/2025/circu53.pdf | 2026-11-11 |
| Read for the figures named: SII news of 19 Oct 2026 on Ley 21.850 (IDPC 25.5%, 24%, 23% for AT 2028 to 2030; restitution 30%, 20%, 0%) | https://www.sii.cl/noticias/2026/191026noti01pcr.htm | 2026-11-11 |
| Read for the figures named: SII Formulario 22 AT 2026 (lines 53 to 57, 85; Recuadros 12, 17, 22) | https://www.sii.cl/ayudas/formularios/f22_at2026.pdf | 2026-11-11 |
| Read for the figures named: SII Formulario 29 (PPM line 69, code 62) | https://www.sii.cl/formularios/imagen/F29.pdf | 2026-11-11 |
| Read for the figures named: SII UTM/UTA 2026 (UTA December 2026 CLP 873,624) | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm | 2026-11-11 |
| Read for the figures named: SII daily penal interest (7.70%, Jul to Dec 2026) | https://www.sii.cl/valores_y_fechas/otros_valores/tasa_interes_penal_diario.html | 2026-11-11 |

Not yet confirmed: the Pro Pyme PPM rate for November and December 2026, where Ley 21.850 art. 8 No. 1 replaces 0.25% with 0.23% from the month after publication while Ley 21.755 halves it (SII has not yet instructed how the two combine); the AT 2027 F22 codes and the exact April 2027 deadline days; the UF at 31 December 2026, which sets the peso value of the UF limits; whether any transitory rule limits the deduction of carried-forward losses for large companies (none found in art. 31 No. 3 as read); treaty rates.
