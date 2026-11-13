---
name: ca-income-tax
description: California personal income tax figures for tax year 2026, the one home for the numbers the California resident return uses. The 2026 FTB tax rate schedules X, Y and Z (1% to 12.3%), the 1% Behavioral Health Services Tax on taxable income over $1,000,000 (top rate 13.3%), exemption credits, the standard deduction, the AGI limits that reduce exemption credits and itemized deductions, the alternative minimum tax exemptions, the California section 179 limit, the excess business loss limit, the NOL suspension, and the renter's credit, CalEITC and Young Child Tax Credit amounts. Where the FTB has not yet published a 2026 amount, the 2025 amount is given and labelled for the 2025-2026 filing cycle. Trigger on "California tax brackets", "California income tax rate", "CA tax rate 2026", "California standard deduction", "California exemption credit", "mental health tax", "Behavioral Health Services Tax", "CalEITC amount". Load ca-540-individual-return for the method.
version: "1.0"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: rates-card
---

# California personal income tax figures, tax year 2026

> **Source-cited draft.** Built from the 2026 California Tax Rate Schedules, the 2026 Form 540-ES instructions, the 2025 Form 540 and its booklet, the 2025 Schedule CA (540), Schedule P (540) and form FTB 3885A instructions, FTB Pub. 1001 (2025), the FTB renter's credit and CalEITC pages, and California Revenue and Taxation Code (R&TC) sections 17024.5, 17041 and 17043, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** California taxes a resident's whole taxable income at nine rates from 1% to 12.3%. For 2026 the 12.3% rate starts above **$768,213** for a single filer (Schedule X), **$1,536,426** for a joint return (Schedule Y) and **$1,044,771** for head of household (Schedule Z). A separate 1% Behavioral Health Services Tax applies to taxable income over **$1,000,000** for every filing status, so the top rate is 13.3%. Taxable income of $100,000 or less uses the FTB tax table instead of the schedules. The FTB has published the 2026 schedules but not yet the 2026 standard deduction, exemption credits or credit income limits: those rows carry the 2025 amount and say so.

This card holds figures only. The method (Schedule CA (540), what California does not follow, the line-by-line Form 540) is in `ca-540-individual-return`. Estimated tax is in `ca-estimated-tax-540es`, the health coverage penalty in `ca-form-3853-coverage`, and part-year and nonresident rules in `ca-residency-leaving-california`. Employee SDI on wages is in `ca-payroll`. Federal figures are not restated here.

| Field | Value |
| --- | --- |
| Jurisdiction | California (US-CA) |
| Tax authority | [Franchise Tax Board (FTB)](https://www.ftb.ca.gov/) |
| Legislation | Revenue and Taxation Code, Part 10 (from section 17001) |
| Primary form | Form 540 (residents); Form 540NR (part-year and nonresidents) |
| Filing deadline | April 15, 2027 for tax year 2026, with an automatic extension to file to October 15, 2027 |

## Rates, bands and thresholds

### 2026 tax rate schedules (taxable income over $100,000; Form 540 line 19 to line 31)

**Schedule X: single or married/RDP filing separately (2026)**

| Over | But not over | Tax | Source |
| --- | --- | --- | --- |
| $0 | $11,456 | 1.00% | [2026 California Tax Rate Schedules](https://www.ftb.ca.gov/forms/2026/2026-540-tax-rate-schedules.pdf) |
| $11,456 | $27,157 | $114.56 + 2.00% of the excess over $11,456 | same |
| $27,157 | $42,861 | $428.58 + 4.00% of the excess over $27,157 | same |
| $42,861 | $59,498 | $1,056.74 + 6.00% of the excess over $42,861 | same |
| $59,498 | $75,197 | $2,054.96 + 8.00% of the excess over $59,498 | same |
| $75,197 | $384,109 | $3,310.88 + 9.30% of the excess over $75,197 | same |
| $384,109 | $460,927 | $32,039.70 + 10.30% of the excess over $384,109 | same |
| $460,927 | $768,213 | $39,951.95 + 11.30% of the excess over $460,927 | same |
| $768,213 | and over | $74,675.27 + 12.30% of the excess over $768,213 | same |

**Schedule Y: married/RDP filing jointly or qualifying surviving spouse/RDP (2026)**

| Over | But not over | Tax | Source |
| --- | --- | --- | --- |
| $0 | $22,912 | 1.00% | [2026 California Tax Rate Schedules](https://www.ftb.ca.gov/forms/2026/2026-540-tax-rate-schedules.pdf) |
| $22,912 | $54,314 | $229.12 + 2.00% of the excess over $22,912 | same |
| $54,314 | $85,722 | $857.16 + 4.00% of the excess over $54,314 | same |
| $85,722 | $118,996 | $2,113.48 + 6.00% of the excess over $85,722 | same |
| $118,996 | $150,394 | $4,109.92 + 8.00% of the excess over $118,996 | same |
| $150,394 | $768,218 | $6,621.76 + 9.30% of the excess over $150,394 | same |
| $768,218 | $921,854 | $64,079.39 + 10.30% of the excess over $768,218 | same |
| $921,854 | $1,536,426 | $79,903.90 + 11.30% of the excess over $921,854 | same |
| $1,536,426 | and over | $149,350.54 + 12.30% of the excess over $1,536,426 | same |

**Schedule Z: head of household (2026)**

| Over | But not over | Tax | Source |
| --- | --- | --- | --- |
| $0 | $22,927 | 1.00% | [2026 California Tax Rate Schedules](https://www.ftb.ca.gov/forms/2026/2026-540-tax-rate-schedules.pdf) |
| $22,927 | $54,316 | $229.27 + 2.00% of the excess over $22,927 | same |
| $54,316 | $70,018 | $857.05 + 4.00% of the excess over $54,316 | same |
| $70,018 | $86,654 | $1,485.13 + 6.00% of the excess over $70,018 | same |
| $86,654 | $102,356 | $2,483.29 + 8.00% of the excess over $86,654 | same |
| $102,356 | $522,385 | $3,739.45 + 9.30% of the excess over $102,356 | same |
| $522,385 | $626,864 | $42,802.15 + 10.30% of the excess over $522,385 | same |
| $626,864 | $1,044,771 | $53,563.49 + 11.30% of the excess over $626,864 | same |
| $1,044,771 | and over | $100,786.98 + 12.30% of the excess over $1,044,771 | same |

The schedules say: use them only when Form 540 line 19 is more than $100,000; at $100,000 or less use the tax table. Round the result to two decimals, then enter whole dollars on line 31. The FTB recomputes the brackets each year from the June-to-June California Consumer Price Index ([R&TC 17041(h)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17041)).

### Behavioral Health Services Tax (formerly the Mental Health Services Tax)

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Rate and threshold | 1% of taxable income in excess of $1,000,000 | Same $1,000,000 for every filing status: not doubled on a joint return. Credits cannot reduce it. Form 540 line 62 | [R&TC 17043](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043) |
| Estimated tax worksheet line | Worksheet line A minus $1,000,000, times 1%, carried to line 17 | Taxable income or nonresident California-source taxable income over $1,000,000 | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |

### Standard deduction and exemption credits (2025-2026 filing cycle: 2026 amounts not yet published)

| Item | Amount | Conditions | Source |
| --- | --- | --- | --- |
| Standard deduction, single or married/RDP filing separately (2025-2026 filing cycle) | $5,706 | Also the figure the 2026 Form 540-ES worksheet prints | [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf); [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Standard deduction, joint, head of household or qualifying surviving spouse/RDP (2025-2026 filing cycle) | $11,412 | Same | same |
| Personal, blind and senior exemption credit, each (2025-2026 filing cycle) | $153 | One personal credit for single, separate or head of household; two for joint or surviving spouse; one more for each blind or 65-or-older person | [2025 Form 540](https://www.ftb.ca.gov/forms/2025/2025-540.pdf) |
| Dependent exemption credit, each (2025-2026 filing cycle) | $475 | Each dependent listed | same |
| AGI above which exemption credits shrink (2025-2026 filing cycle) | $252,203 single or separate; $504,411 joint or surviving spouse; $378,310 head of household | Federal AGI (Form 540 line 13). Divide the excess by $2,500 ($1,250 separate), round up, multiply by $6, and take that off each credit | [2025 Form 540 booklet, line 32](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| Itemized deduction limitation (2025-2026 filing cycle) | Same AGI levels as the exemption credit row | Reduce itemized deductions by the smaller of 6% of the excess AGI or 80% of the deductions subject to the limit | [2025 Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |

### Business and loss limits

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| California section 179 limit | $25,000, reduced dollar for dollar once section 179 property placed in service costs more than $200,000 | Figured on form FTB 3885A; limit applies to all qualifying assets as a group | [2025 FTB 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html) |
| Excess business loss (2025-2026 filing cycle) | Net losses from all trades or businesses over $313,000 ($626,000 joint) | California's own limit, form FTB 3461; the excess carries over as an excess business loss | [FTB Pub. 1001 (2025)](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf) |
| NOL carryover suspension | Suspended for taxable years beginning in 2024, 2025 and 2026 | Does not apply below $1,000,000 of net business income or modified AGI, or to disaster loss carryovers; an NOL is still computed and carried forward | [2025 Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html) |
| Business credit limit | Business credits cannot reduce net tax by more than $5,000,000 | Taxable years beginning in 2024, 2025 and 2026 | same |

### Alternative minimum tax (2025-2026 filing cycle)

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| AMT exemption | $92,749 single or head of household; $123,667 joint or surviving spouse; $61,830 separate | Schedule P (540) | [2025 Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html) |
| Exemption phase-out starts | AMTI over $347,808 single or head of household; $463,745 joint or surviving spouse; $231,868 separate | Exemption reduced by 25% of the excess | same |
| Small-business exclusion | Aggregate gross receipts of less than $1,000,000 from all trades or businesses | Business income, adjustments and preferences are left out of AMTI | [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |

### Personal credits (2025-2026 filing cycle)

| Credit | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Nonrefundable renter's credit, income limit | California AGI $53,994 or less (single or separate); $107,987 or less (joint, head of household, surviving spouse) per the FTB page; the 2025 booklet record prints $107,988 | Rent paid on a California principal residence for at least half the year; property not tax exempt; not living with someone who can claim you as a dependent | [FTB renter's credit](https://www.ftb.ca.gov/file/personal/credits/nonrefundable-renters-credit.html); [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| Nonrefundable renter's credit, amount | $60 single or married/RDP filing separately; $120 joint, head of household or surviving spouse | Form 540 line 46. Separate filers living in the same rental may put the full $120 on one return or $60 on each | [2025 Form 540 booklet, renter's credit record question 11](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| CalEITC earned income range | At least $1 and not more than $32,900 | 18 or older or a qualifying child; valid SSN or ITIN; lived in California more than half the year | [FTB CalEITC eligibility](https://www.ftb.ca.gov/file/personal/credits/caleitc/eligibility-and-credit-information.html) |
| CalEITC maximum | $302 (no child); $2,016 (1); $3,339 (2); $3,756 (3 or more) | Form FTB 3514 | same |
| CalEITC investment income limit | No credit if investment income is more than $4,814 | FTB 3514 worksheet | [2025 FTB 3514 booklet](https://www.ftb.ca.gov/forms/2025/2025-3514-booklet.html) |
| Young Child Tax Credit | Up to $1,189; phases out above $27,425 of earned income and is gone at $32,901 | Allowed CalEITC and a qualifying child under 6 at year end; zero or negative earned income still qualifies if net losses and wages are each not over $35,640 | same |
| Foster Youth Tax Credit | Up to $1,189 per qualifying taxpayer; same phase-out | Aged 18 to 25, allowed CalEITC, in California foster care at 13 or older | [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |

### Conformity date

| Item | Rule | Source |
| --- | --- | --- |
| Internal Revenue Code date | For taxable years beginning on or after January 1, 2025, California follows the IRC as enacted on January 1, 2025, with California's own modifications (SB 1435, Stats. 2026, Ch. 236) | [R&TC 17024.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17024.5) |
| One Big Beautiful Bill Act (July 2025) | "In general, California R&TC does not conform to the OBBBA" | [2025 Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |

## Worked example

### Single filer, 2026 taxable income $150,000

Schedule X, the $75,197 to $384,109 band: $3,310.88 plus 9.30% of $74,803 is $10,267.56. Less one personal exemption credit of $153 (the 2025 amount, pending the 2026 figure), tax before other credits is $10,114.56. Federal AGI is below $252,203, so the credit is not reduced, and taxable income is under $1,000,000, so there is no Behavioral Health Services Tax.

```oa-check
name: CA 2026 Schedule X, single, taxable income 150,000
inputs:
  ti: 150000
  exemption_credit: 153
steps:
  - tax: 3310.88 + (ti - 75197) * 0.093
  - net: tax - exemption_credit
  - bhst: max(ti - 1000000, 0) * 0.01
expected:
  tax: 10267.56
  net: 10114.56
  bhst: 0
```

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 California Tax Rate Schedules (FTB). Read for Schedules X, Y and Z and the $100,000 tax-table rule. | https://www.ftb.ca.gov/forms/2026/2026-540-tax-rate-schedules.pdf | 2026-11-13 |
| 2026 Instructions for Form 540-ES. Read for the Behavioral Health Services Tax worksheet and worksheet line 2b standard deduction. | https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf | 2026-11-13 |
| 2025 Form 540. Read for lines 7 to 10 exemption credit amounts ($153, $475). | https://www.ftb.ca.gov/forms/2025/2025-540.pdf | 2026-11-13 |
| 2025 California 540 Personal Income Tax Booklet. Read for line 18 standard deduction, line 32 AGI limitation worksheet, the renter's credit record, the YCTC and FYTC notes and the AMT gross receipts test. | https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf | 2026-11-13 |
| 2025 Schedule CA (540) instructions. Read for the IRC date (January 1, 2025), the OBBBA statement and the itemized deduction limitation. | https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html | 2026-11-13 |
| 2025 Schedule P (540) instructions. Read for the AMT exemption and phase-out amounts, the NOL suspension and the $5,000,000 business credit limit. | https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html | 2026-11-13 |
| 2025 FTB 3885A instructions. Read for the $25,000 section 179 limit and $200,000 threshold. | https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html | 2026-11-13 |
| FTB Pub. 1001 (2025). Read for the excess business loss amounts ($313,000 and $626,000) and the bonus depreciation and section 174 statements. | https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf | 2026-11-13 |
| FTB nonrefundable renter's credit page. Read for the income limits and conditions. | https://www.ftb.ca.gov/file/personal/credits/nonrefundable-renters-credit.html | 2026-11-13 |
| FTB CalEITC eligibility and credit information. Read for the $32,900 limit and the maximum credit table. | https://www.ftb.ca.gov/file/personal/credits/caleitc/eligibility-and-credit-information.html | 2026-11-13 |
| 2025 FTB 3514 booklet. Read for the $4,814 investment income test and the YCTC amounts. | https://www.ftb.ca.gov/forms/2025/2025-3514-booklet.html | 2026-11-13 |
| R&TC 17041 (California Legislative Information, through Firecrawl). Read for subdivision (h) bracket indexing. | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17041 | 2026-11-13 |
| R&TC 17043. Read for the 1% tax on taxable income over $1,000,000 and the exclusions in (c). | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043 | 2026-11-13 |
| R&TC 17024.5. Read for (a)(1)(Q), the January 1, 2025 specified date, and the SB 1435 history note. | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17024.5 | 2026-11-13 |

Not yet confirmed: the 2026 standard deduction, exemption credits, exemption-credit and itemized-limitation AGI levels, AMT exemptions and phase-out levels, excess business loss limit, renter's credit amounts and income limits, and the CalEITC, YCTC and FYTC amounts. The FTB had not published them on 2026-11-13; the 2025 amounts are shown for the 2025-2026 filing cycle. The renter's credit joint limit differs between the FTB page ($107,987) and the 2025 booklet record ($107,988). The 2026 Schedule CA (540) instructions, which will list California's response to any 2026 federal change, were not yet published.
