---
name: dominican-republic-tax-optimization
description: "Legal tax planning for small businesses and self-employed people in the Dominican Republic for fiscal year 2026. Compares trading as an individual on the 2026 scale (top rate 25%) with a company at 27% plus 10% final dividend withholding, explains the mixed territorial rule (foreign investment and financial income of a new resident taxed only from the third year), the main home exemption on the 10% real estate gain tax, the RST simplified regime, and the red lines. Trigger on reduce tax Dominican Republic, tax planning DR, RST, territorial taxation DR, DR dividends 10%, company or individual DR. Built from DGII pages and laws; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/dominican-republic-tax-optimization"
  jurisdiction: "DO"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Dominican Republic Tax Optimization v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Planning choices for resident individuals, sole-owner businesses and small companies in the Dominican Republic for fiscal year 2026, administered by DGII. Amounts are RD$. Figures here must agree with `do-tax-overview`, `dominican-republic-income-tax` and `dominican-republic-social-contributions`; where they differ, those skills and the DGII pages win. Aggressive positions are never advised.

Out of scope: free-zone and incentive regimes, cross-border structures with treaties, transfer pricing, and anything turning on fraud or concealment.

## Ask the client first

1. Is the client resident (more than 182 days in the year), and since when? (Decides when foreign investment income becomes taxable.)
2. Expected annual net profit, and how much will be taken out each year versus kept in the business?
3. Individual, sole-owner business, or company already? Partners?
4. Turnover and purchases (RST eligibility), and whether sales are only to final consumers.
5. Any real estate sale planned, and is it the main home? Will the proceeds be reinvested, and is the owner over 65?
6. Any foreign income: investments, financial gains, technical assistance services?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Individual scale 2026, exempt band | Up to RD$416,220.01 | Resident individuals | DGII, Impuesto sobre la Renta: https://dgii.gov.do/cicloContribuyente/obligacionesTributarias/principalesImpuestos/Paginas/impuestoSobreRenta.aspx |
| Individual scale 2026, top band | RD$79,776.00 plus 25% of the excess over RD$867,123.01 | Fiscal year 2026 | same |
| Corporate rate | 27% | 30% for income of RD$1,000,000,000 or more, fiscal years 2026 to 2028 | same |
| Dividends | 10%, single and final | Residents and non-residents (Tax Code art. 308) | Law 253-12: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Codigo%20Tributario%20y%20Leyes%20que%20lo%20modifican%20y%20complementan/253-12.pdf |
| Foreign-source income of a resident | Taxed only if from investments and financial gains, and for a new resident only from the third year of residence | Tax Code arts. 269, 271 | DGII, Aviso 22-25: https://dgii.gov.do/publicacionesOficiales/avisosInformativos/Documents/2025/22-25.pdf |
| Real estate gain of an individual | 10%, final, within six months | Main home fully reinvested within six months exempt (partial reinvestment, proportional); owner over 65 selling the main home exempt | Law 30-26 arts. 14 and 16: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Codigo%20Tributario%20y%20Leyes%20que%20lo%20modifican%20y%20complementan/30-26.pdf |
| 2027 individual scale | Exempt to RD$480,000; 27% above RD$4,800,000.01 | From fiscal year 2027 | DGII, Aviso 10-26: https://dgii.gov.do/publicacionesOficiales/avisosInformativos/Documents/2026/10-26.pdf |
| RST under Law 30-26 | Income mode RD$30,000,000 (companies) or RD$15,000,000 (individuals); purchases mode RD$60,000,000 | Only once the new RST regulation is issued; prior DGII approval | Law 30-26 art. 25: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Codigo%20Tributario%20y%20Leyes%20que%20lo%20modifican%20y%20complementan/30-26.pdf |

### Steps

1. **Individual or company?** For 2026 the top individual rate (25%) is below the corporate rate (27%), and a company adds 10% final withholding on what it distributes. Compute both: individual scale on the net profit, against 27% plus 10% of the distributed after-tax profit. A company only defers the 10% on profit it keeps. Non-tax reasons (limited liability, partners, investors) may still favour a company. Recheck for 2027, when the individual top rate becomes 27%.
2. **Territorial window.** A new resident's foreign investment and financial income is taxed only from the third year of residence. Confirm the source of each item and the residence start date. From Law 30-26, foreign technical assistance income of residents is also taxable (see `do-tax-overview`).
3. **Real estate sales.** Reinvest the whole proceeds of a main home sale in a new main home within six months to exempt the gain; a partial reinvestment exempts the same share.
4. **RST.** For small businesses, the simplified regime sets ISR and ITBIS on income or purchases. The Decree 265-19 limits and the 40% deemed-expense rule the earlier version gave are not confirmed for 2026, and Law 30-26's new RST waits for its regulation. Check DGII before advising entry.
5. **Timing of withholding.** Fees and rent paid to individuals from 1 July 2026 bear 15% (10% before); rent withholding is now final.

## Boundary and exception table

| Situation | Rule |
|---|---|
| RST limits exceeded | The taxpayer leaves the regime; do not plan to stay just under without real figures |
| RST and real expenses | One regime: never combine a deemed-expense method with real-expense deductions |
| Dominican-source income relabelled as foreign | Not allowed; the territorial benefit covers only genuine foreign investment and financial income |
| Stay of exactly 182 days | Not resident: the test is more than 182 days |
| Company with no substance | Structures need real substance |

## Worked cases

### Case 1: Individual or company, net profit RD$1,000,000 or RD$10,000,000, all distributed

At RD$1,000,000: individual RD$112,995.25; company 27% = RD$270,000 plus 10% of RD$730,000 = RD$343,000. At RD$10,000,000: individual RD$2,362,995.25; company RD$3,430,000 (RD$2,700,000 if nothing is distributed). For 2026 the individual route costs less at both levels.

```oa-check
name: DO 2026 individual vs company, profit 1m and 10m, full distribution
inputs:
  p_small: 1000000
  p_large: 10000000
steps:
  - ind_small: round(79776 + (p_small - 867123.01) * 0.25, 2)
  - co_small: p_small * 0.27 + p_small * 0.73 * 0.10
  - ind_large: round(79776 + (p_large - 867123.01) * 0.25, 2)
  - co_large: p_large * 0.27 + p_large * 0.73 * 0.10
  - gap_large: co_large - ind_large
expected:
  ind_small: 112995.25
  co_small: 343000
  ind_large: 2362995.25
  co_large: 3430000
  gap_large: 1067004.75
```

### Case 2: Sale of the main home with a gain of RD$3,000,000, reinvest all, 60% or nothing

Reinvesting all the proceeds in a new main home within six months exempts the gain. Reinvesting 60% exempts 60%: tax 10% of RD$1,200,000 = RD$120,000. No reinvestment: RD$300,000.

```oa-check
name: DO 2026 main home gain, reinvestment share decides
inputs:
  gain: 3000000
  share_partial: 0.6
steps:
  - tax_full: gain * (1 - 1) * 0.10
  - tax_partial: gain * (1 - share_partial) * 0.10
  - tax_none: gain * 0.10
expected:
  tax_full: 0
  tax_partial: 120000
  tax_none: 300000
```

## When to refuse or refer

- Any structure whose main purpose is to hide Dominican-source income, or that lacks substance.
- RST entry decisions until DGII confirms the current limits and regulation.
- Free-zone, tourism and other incentive regimes; treaty claims.
- Optimisation is never final advice: route to a licensed Dominican tax adviser.

## Sources

| Source | URL | Read on |
|---|---|---|
| DGII, Impuesto sobre la Renta page: read for the 2026 scale, the 27% and 30% rates and the territorial rule | https://dgii.gov.do/cicloContribuyente/obligacionesTributarias/principalesImpuestos/Paginas/impuestoSobreRenta.aspx | 2026-11-14 |
| DGII, Aviso 22-25: read in full for the mixed territorial rule and the third-year start for new residents | https://dgii.gov.do/publicacionesOficiales/avisosInformativos/Documents/2025/22-25.pdf | 2026-11-14 |
| Law 253-12: read for Tax Code art. 308 (10% dividends) | https://dgii.gov.do/legislacion/leyesTributarias/Documents/Codigo%20Tributario%20y%20Leyes%20que%20lo%20modifican%20y%20complementan/253-12.pdf | 2026-11-14 |
| Law 30-26: read for arts. 14, 16, 17 and 25 | https://dgii.gov.do/legislacion/leyesTributarias/Documents/Codigo%20Tributario%20y%20Leyes%20que%20lo%20modifican%20y%20complementan/30-26.pdf | 2026-11-14 |
| DGII, Aviso 10-26: read for the start dates (2027 scale, RST regulation) | https://dgii.gov.do/publicacionesOficiales/avisosInformativos/Documents/2026/10-26.pdf | 2026-11-14 |
| DGII, RST page: read for the regime outline under Decree 265-19 | https://dgii.gov.do/contribuyentesRegistrados/regimenesEspeciales/RST | 2026-11-14 |

Not yet confirmed: the Decree 265-19 RST limits for 2026 (earlier version: income RD$10,742,792.74, purchases RD$49,392,150.51 for 2025) and the 40% deemed-expense deduction in the income mode; the RST benefits the earlier version listed (no anticipos, no 606, 607 and 608 formats, no asset tax on activity assets); whether self-employed people are outside the TSS social security system by default; the rate DGII applies to foreign investment income of residents from the third year.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `dominican-republic-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/dominican-republic-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
