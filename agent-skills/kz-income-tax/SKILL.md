---
name: kz-income-tax
description: "Kazakhstan 2026 personal income tax: residence, income-specific rates, deductions, general-regime entrepreneur profit and separate filing obligations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kz-income-tax"
  jurisdiction: "KZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Kazakhstan personal income tax v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Residents are taxed on Kazakhstan and foreign-source income; non-residents on Kazakhstan-source income, with separate permanent-establishment rules (Tax Code arts. 221–222). Establish residence before computing. The ordinary presence test is 183 days in any consecutive 12-month period ending in the tax year, including arrival and departure days (figures in words on the page). Centre of vital interests requires the cumulative citizenship/residence permission, family and available-home conditions in art. 222. The AIFC investment-resident and deemed-resident categories require separate review. Use `kz-payroll` for employer withholding, `kz-simplified-regime` for special regimes, and this file for resident annual income and general-regime ИП.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Ordinary annual taxable income, excluding separately classified income | 10% through 8,500 МРП; 15% on the excess; МРП at 1 January (art. 363(1)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| General-regime ИП annual taxable income | 10% through 230,000 МРП; 15% on the excess (art. 363(4)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Taxable resident dividends | 5% through 230,000 МРП; 15% on the excess, after any applicable exemption (art. 363(3)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Private practice | 9% (art. 363(2)); not the general ИП schedule | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Basic personal deduction | 30 МРП per calendar month, maximum 360 МРП per calendar year (art. 403) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Social-payment deductions | Actual qualifying ОПВ, ВОСМС and specified civil-contract СО; apply before the basic deduction (arts. 401–402) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Classify income before selecting a rate. For ordinary resident employment use taxable income after statutory exclusions and personal deductions. The basic deduction is available at only 1 tax agent, on the individual’s application (art. 437). Unused monthly basic deduction is not carried to later payroll months; an unused amount can be considered in self-assessment under art. 409, within the annual limit. There is no universal tax-free band independent of these deductions. Pension and medical contribution rates/bases belong to `kz-social-contributions`; do not subtract a presumed percentage from every kind of income.

For a general-regime ИП, art. 393 starts with annual business income, adjusts income and allowable documented deductions under the corporate-tax rules, then applies reductions and eligible loss carryforwards. Do not substitute turnover for profit or apply the employment deduction automatically to business income. Listed-security dividend relief requires the listing and actual-trading conditions in art. 436(13); a holding period alone does not establish exemption.

## Deadlines and filing

General-regime ИП: annual business declaration by 31 March following the reporting year (art. 420), payment within 10 calendar days after that deadline (art. 421). Other self-assessed income: determine the declaration obligation under arts. 416–417; the ordinary income-and-property declaration deadline is 15 September following the reporting year (art. 418), with payment within 10 calendar days after that deadline (art. 419). These are different jobs: do not apply the old blanket 31 March individual deadline to all residents. Employees whose only income is correctly withheld salary may fall within the art. 417 exception; foreign assets, other income and other listed conditions can still require a declaration. Use the current taxpayer-cabinet form for the applicable obligation; do not reuse an old line map. Retain submission acceptance, computation and payment reference. Statutory non-working-day adjustments must be applied.

## Penalties and interest

Late filing, late payment and under-declaration require separate assessment of the current administrative rule, tax-agent status, period and any extension. No numerical penalty is asserted here; calculate none from memory.

## Cross-border points

Art. 692 sends non-resident Kazakhstan-source income to art. 682, normally without personal deductions. Employment-type income uses the 10%/15% schedule through 8,500 МРП under art. 682(1)(8), rather than an unconditional flat 10%. Other Kazakhstan-source payments generally start at 20%, with income-specific exceptions in art. 682. Treaty relief requires the applicable treaty, beneficial recipient and residence evidence; do not assume a treaty rate or resident deduction. Foreign tax credit and permanent-establishment analysis require separate review.

## Two worked examples that recompute

Case 1: hypothetical ordinary annual taxable income is expressed in МРП after all deductions. For 9,000 МРП, tax is 850 + 75 = 925 МРП. The annual threshold is not a separate threshold at each employer.

```oa-check
name: Ordinary income crosses annual threshold
inputs:
  income_mrp: 9000
steps:
  - tax_mrp: min(income_mrp, 8500) * 0.10 + max(income_mrp - 8500, 0) * 0.15
expected:
  tax_mrp: 925
```

Case 2: a general-regime ИП has hypothetical receipts of KZT 15,000,000 and allowable costs of KZT 3,000,000, no other adjustments or losses and income below its own annual threshold. Tax on KZT 12,000,000 is KZT 1,200,000. The result differs from a turnover-based special regime; eligibility must be tested before choosing.

```oa-check
name: General-regime IP documented costs
inputs:
  income: 15000000
  costs: 3000000
steps:
  - base: income - costs
  - tax: base * 0.10
expected:
  base: 12000000
  tax: 1200000
```

## Ask the client first

- Residence, travel days, citizenship/residence permission, family and available home?
- Employment, ИП, private practice, dividends or other income, and all payers?
- Actual deductions, prior tax-agent applications and withheld tax?
- Business regime, documented costs, adjustments and carried losses?
- Foreign income/assets, treaty residence evidence and current filing obligation?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 221–222, 363, 393, 401–403, 409, 417–421, 436–441, 682 and 692 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |

Not yet confirmed: Specific treaty rates, social-category deductions not worked here, exact current electronic form fields and administrative penalty amounts. The old 2025 flat-rate/non-resident shorthand, 14-МРП deduction and blanket individual 31 March deadline are superseded, not fallback instructions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kz-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kz-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
