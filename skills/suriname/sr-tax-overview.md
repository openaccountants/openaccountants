---
name: sr-tax-overview
description: "Suriname tax overview for tax year 2026, built from the Wet Inkomstenbelasting 1922, the Wet Loonbelasting, the Wet BTW 2022, the Wet AOV and the Wet Dividendbelasting 1973 as published by the Suriname Tax Administration. Use when someone asks how Suriname taxes people and companies, which taxes apply, the headline rates, who is liable, the main deadlines and penalties, and which detailed skill to open next."
jurisdiction: SR
tax_year: 2026
last_updated: 2026-11-14
version: 2.0
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Suriname tax overview (2026) v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. A qualified professional in Suriname must review the work before filing, paying or taking a tax position.

This skill is the map of Suriname's tax system for 2026. It gives the headline rules and figures and sends each question to the skill that does the work:

- [sr-income-tax](sr-income-tax.md): individuals, wage tax and the income tax return.
- [sr-corporate-income-tax](sr-corporate-income-tax.md): income tax for bodies (companies) and dividend tax.
- [sr-vat-gst](sr-vat-gst.md): BTW (VAT).
- [sr-payroll-social](sr-payroll-social.md): wage tax withholding, AOV, the general pension and basic health insurance.
- [sr-cross-border](sr-cross-border.md): non-residents, permanent establishments and treaties.
- [sr-company-formation](sr-company-formation.md): setting up an NV and registering it.

## Who this applies to

- **Tax year.** The calendar year; a body may use a book year (IB art. 43(1) and the bodies' rules in sr-corporate-income-tax).
- **Authority.** The Belastingdienst Suriname (Tax Administration) runs income tax, wage tax, dividend tax and BTW; returns are filed in its online portal.
- **Individuals.** Residents are taxed on their worldwide income; non-residents only on the Surinamese income listed in IB art. 27(2) (see sr-cross-border).
- **Bodies.** NVs, cooperatives and the other bodies of IB arts. 1 to 3 pay income tax on their profit at one rate (IB art. 36(1)).
- **Employers** withhold wage tax (Wet Loonbelasting) and AOV premium and pay the general pension and basic health premiums (sr-payroll-social).
- **Businesses** with taxable turnover above SRD 1,000,000 in a calendar year must register for BTW (Wet BTW art. 21).
- **Out of scope here.** Customs and excise duties, the petroleum and gold-mining regimes, property taxes and municipal levies. Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Individual income tax, tax-free part of zuiver inkomen (IB art. 34(1)) | First SRD 108,000 nil | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Inkomstenbelasting.pdf |
| Individual bands above SRD 108,000 (IB art. 34(1)) | 8% to SRD 150,000; 18% to SRD 192,000; 28% to SRD 234,000; 38% above | 2026 | same |
| Income tax for bodies (IB art. 36(1)) | 36% of the belastbaar bedrag | 2026 | same |
| Late payment interest on income tax (IB art. 73(1), rate set by S.B. 1995 no. 98 as footnoted in the published text) | 45% a year | 2026 | same |
| Wage tax, same tax-free amount and bands applied by pay period (LB arts. 13, 14) | See sr-income-tax | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf |
| AOV premium, residents under 60 (Wet AOV art. 20(2)) | 4% of the base | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-AOV.pdf |
| Dividend tax on distributions by a body established in Suriname (Wet Dividendbelasting art. 5) | 25% of the distribution | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Dividendbelasting.pdf |
| BTW general rate (Wet BTW art. 4(1)) | 10% | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-121-WET-BTW-2022.pdf |
| BTW registration threshold, taxable turnover excluding BTW in a calendar year (art. 21) | More than SRD 1,000,000 | 2026 | same |
| BTW late-filing penalty per return (art. 37; S.B. 2025 no. 140), from 1 January 2026 | SRD 2,500 for 1 month late, 5,000 for 2, 7,500 for 3, 10,000 from 4 | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2025-no.-140-BESCHIKKING-boetebeleid-verzuim-boeten.pdf |

The reduced, increased and zero rates of BTW are in sr-vat-gst; the general pension and basic health premiums are in sr-payroll-social. The Wet BTW 2022 has applied since 1 January 2023, with art. 21 from 15 October 2022 (art. 70).

## The base

- **Individuals** pay on zuiver inkomen: income from business, work, assets (including dividends and interest) and periodic receipts, less the deductions of IB art. 18 (for example pension premiums and own-home mortgage interest). The bands of art. 34 apply to the part above SRD 108,000.
- **Wage tax and dividend tax are prepayments.** Both are credited against the income tax assessment on the same income (IB art. 52e(1)); a resident shareholder includes the dividend in income and credits the 25% withheld.
- **Bodies** pay on profit computed under IB arts. 19 to 25, with loss carry-forward (start-up losses of the first three years without a time limit, other losses seven years, IB art. 20(3)) and a participation exemption for qualifying foreign dividends (art. 25). The tax is computed on whole SRD (art. 36(3)).
- **BTW** is charged on supplies of goods and services and on imports (Wet BTW art. 4); input BTW is deducted in the monthly return (sr-vat-gst).
- **AOV** is levied on zuiver loon where wage tax is due, otherwise on zuiver inkomen (Wet AOV art. 20(1)).

## Deadlines and filing

| What | When in 2026 | Law or source |
|---|---|---|
| Provisional income tax return, calendar year | By 15 April 2026 | IB art. 42a |
| Provisional tax instalments | 15 April, 15 July, 15 October and 31 December 2026 | IB art. 42b(2) |
| Definitive return, individuals, for 2025 | Within four months after the year end: by 30 April 2026 | IB art. 43(1) |
| Definitive return, bodies, for 2025 | By 30 June 2026, online only | Tax Administration news of 15 May 2026 |
| BTW monthly return and payment | Before the 16th day of the following month | Wet BTW art. 13(2) |
| Dividend tax withheld | File and pay within one month after the dividend is made available | Wet Dividendbelasting art. 6(4) |

Income tax returns are filed in the Tax Administration's online portal; returns for 2024 and earlier stay on paper (Tax Administration income tax page). The detailed steps are in sr-income-tax and sr-corporate-income-tax.

## Penalties and interest

- **Income tax:** an assessment with a 100% increase where a return is not filed or the tax not paid, 10% where there is no intent or gross negligence (IB art. 51); simple interest at 45% a year on late payment (art. 73(1)). See sr-income-tax.
- **BTW:** a fixed late-filing penalty of SRD 2,500 a month late, up to SRD 10,000 per return (S.B. 2025 no. 140), plus the late-payment penalty and interest in sr-vat-gst.
- **Dividend tax:** tax not withheld or paid is collected by a top-up assessment increased by 100%, or 10% without intent or gross negligence (Wet Dividendbelasting art. 11; see sr-corporate-income-tax).

## Cross-border points

- Non-residents are taxed only on the Surinamese income listed in IB art. 27(2), including profit of a permanent establishment; a non-resident employee has no tax-free amount for wage tax.
- Dividend tax at 25% applies to dividends paid to non-resident shareholders too; a treaty may lower it.
- Suriname's treaties include the Netherlands (1975) and Indonesia; the rates and conditions are in sr-cross-border.

## Two worked examples that recompute

### Example 1: resident employee with SRD 250,000 zuiver inkomen

A resident aged 40 has zuiver inkomen of SRD 250,000 for 2026 and no other income.

- First SRD 108,000: nil.
- SRD 108,000 to 150,000: 42,000 x 8% = SRD 3,360.
- SRD 150,000 to 192,000: 42,000 x 18% = SRD 7,560.
- SRD 192,000 to 234,000: 42,000 x 28% = SRD 11,760.
- Above SRD 234,000: 16,000 x 38% = SRD 6,080.
- Income tax: SRD 28,760, less the wage tax already withheld (IB art. 52e). AOV at 4% on the same income: SRD 10,000.

```oa-check
name: SR 2026 individual income tax on SRD 250,000 zuiver inkomen, with AOV
inputs:
  income: 250000
steps:
  - band1: 42000 * 0.08
  - band2: 42000 * 0.18
  - band3: 42000 * 0.28
  - band4: (income - 234000) * 0.38
  - tax: band1 + band2 + band3 + band4
  - aov: income * 0.04
expected:
  band1: 3360
  band2: 7560
  band3: 11760
  band4: 6080
  tax: 28760
  aov: 10000
```

### Example 2: NV profit of SRD 1,000,000, all distributed

An NV has a belastbaar bedrag of SRD 1,000,000 for 2026 and distributes everything left after tax.

- Income tax for bodies: 1,000,000 x 36% = SRD 360,000.
- Distribution: SRD 640,000. Dividend tax withheld: 640,000 x 25% = SRD 160,000. The shareholder receives SRD 480,000.
- A resident individual shareholder reports the SRD 640,000 dividend and credits the SRD 160,000 against income tax (IB art. 52e).

```oa-check
name: SR 2026 NV profit, income tax for bodies and dividend tax
inputs:
  profit: 1000000
steps:
  - cit: profit * 0.36
  - dividend: profit - cit
  - dividend_tax: dividend * 0.25
  - net_to_shareholder: dividend - dividend_tax
expected:
  cit: 360000
  dividend: 640000
  dividend_tax: 160000
  net_to_shareholder: 480000
```

## Ask the client first

1. Are you resident in Suriname, and since when? Is your income from Suriname only, or from abroad too?
2. Are you employed, self-employed, or do you own an NV or other body? Which book year does it use?
3. Is your taxable turnover above SRD 1,000,000 a year, so that BTW registration applies?
4. Do you employ staff (wage tax, AOV, pension and health premiums)?
5. Do you pay or receive dividends, interest or royalties across borders (dividend tax, treaties)?

**Refer, do not compute here:** the petroleum and gold-mining regimes, customs and excise, property and municipal taxes, and any position resting on a ruling or an agreement with the State.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet Inkomstenbelasting 1922, text published by the Tax Administration: read for arts. 34(1) (bands and SRD 108,000), 36(1) (36% for bodies), 42a, 42b, 43(1), 51, 52e (dividend and wage tax as prepayment) and 73 with its 45% footnote | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Inkomstenbelasting.pdf | 2026-11-14 |
| Wet Loonbelasting, text published by the Tax Administration: read for arts. 13 and 14 (tax-free amount and bands) | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf | 2026-11-14 |
| Wet AOV, text published by the Tax Administration: read for art. 20 (4% premium and its base) | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-AOV.pdf | 2026-11-14 |
| Wet Dividendbelasting 1973, text published by the Tax Administration: read for art. 5 (25%), art. 6(4) and art. 11 (100% or 10% increase) | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Dividendbelasting.pdf | 2026-11-14 |
| Wet BTW 2022 (S.B. 2022 no. 121) as published by the Tax Administration: read for arts. 4(1) (10%), 13(2), 21 (SRD 1,000,000) and 70 (commencement 1 January 2023) | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-121-WET-BTW-2022.pdf | 2026-11-14 |
| S.B. 2025 no. 140, BTW penalty policy: read for the late-filing penalty table (SRD 2,500 to 10,000) | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2025-no.-140-BESCHIKKING-boetebeleid-verzuim-boeten.pdf | 2026-11-14 |
| Tax Administration, Inkomstenbelasting page: read for online filing from January 2025 and paper returns for 2024 and earlier | https://belastingdienst.sr/belastingen/inkomstenbelasting/ | 2026-11-14 |
| Tax Administration news of 15 May 2026: read for the bodies' definitive return 2025 due 30 June 2026, online only | https://belastingdienst.sr/belastingdienst-stapt-volledig-over-op-digitale-aangifte-inkomstenbelasting-voor-lichamen/ | 2026-11-14 |

Not yet confirmed: whether any 2025 or 2026 staatsbesluit or act changed the bands, the SRD 108,000 tax-free amount or the 36% rate after the published texts (the Staatsblad is not online; nothing newer was found on the Tax Administration site on 14 Nov 2026); the definitive return date for bodies for tax year 2026 (only the 2025 date of 30 June 2026 was read).
