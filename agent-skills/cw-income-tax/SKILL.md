---
name: cw-income-tax
description: "Curacao personal income tax (inkomstenbelasting) for tax year 2026. Covers who is taxed (residents on worldwide income, non-residents on Curacao income), the 2026 six-band table from 9.75% to 46.5%, the 2026 basic credit and supplements, the 19.5% substantial-interest rate, the 4% deemed return, 65% of rent, the penshonado regime at 10% or the ANG 500,000 forfait, loss carry-forward, the online return two months after the invitation, the 36-month rule and late-filing penalties. Trigger phrases include Curacao income tax, inkomstenbelasting Curacao, belastingdienst.cw, penshonado, basiskorting, aanmerkelijk belang Curacao, CRIB."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cw-income-tax"
  jurisdiction: "CW"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Curacao personal income tax (inkomstenbelasting) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar year 2026. Authority: Belastingdienst Curacao (Inspectie der Belastingen), belastingdienst.cw. Amounts are Curacao guilders: older official pages print ANG or NAf, newer ones XCG or Cg. The Belastingdienst carries the same numbers across (the 2025 first-band limit of NAf 38,225 appears as XCG 38,225 on its Lei di Bion page).

## Who this applies to

- **Residents** (binnenlands belastingplichtig): everyone living in Curacao pays income tax on worldwide income, earned in Curacao or abroad ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
- **Non-residents** (buitenlands belastingplichtig): someone not living in Curacao but with income from Curacao files only for that Curacao income (same page).
- **Sole traders and partners in a V.O.F. or maatschap** pay income tax on their share of the profit; a B.V., N.V. or other legal person pays profit tax instead ([Tax Office Curacao, Startende ondernemers](https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/)). Profit tax is in `cw-corporate-income-tax`.
- **Out of scope here:** wage tax withholding and social premiums (`cw-payroll-social`), turnover tax (`cw-vat-gst`), inheritance tax, property tax.
- **Married couples:** the spouse with the lower personal income is taxed only on that personal income; the joint, non-personal income and deductions go to the spouse with the higher personal income, who receives the assessment ([Toelichting inkomstenbelasting, binnenlandse belastingplichtigen](https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf)).

## Rates, bands and thresholds

The 2026 table: the tax on the lower limit plus the rate on the excess.

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Band 1: income 0 to under 39,094 | 9.75% | Tax at lower limit 0 | 2026 | [Schijven tarief 2026](https://belastingdienst.cw/wp-content/uploads/2026/01/Schijven-tarief-2026.pdf) |
| Band 2: 39,094 to under 52,127 | 15% on the excess over 39,094 | Tax at lower limit 3,812 | 2026 | same |
| Band 3: 52,127 to under 78,190 | 23% on the excess over 52,127 | Tax at lower limit 5,767 | 2026 | same |
| Band 4: 78,190 to under 110,769 | 30% on the excess over 78,190 | Tax at lower limit 11,761 | 2026 | same |
| Band 5: 110,769 to under 162,894 | 37.5% on the excess over 110,769 | Tax at lower limit 21,535 | 2026 | same |
| Band 6: 162,894 and over | 46.5% on the excess over 162,894 | Tax at lower limit 41,082 | 2026 | same |
| Basic credit (basiskorting) | 2,915 a year | Residents only; once per person, used by one employer only | 2026 | [Loonbelastingverklaring 2026](https://belastingdienst.cw/wp-content/uploads/2026/01/Loonbelastingverklaring-2026.pdf) |
| Sole-earner supplement (alleenverdienertoeslag) | 1,779 a year | Married all year, living in Curacao, spouse's taxable income nil or negative | 2026 | same |
| Elderly supplement (ouderentoeslag) | 1,342 a year | Resident aged 60 or over at the start of the year | 2026 | same |
| Transferred elderly supplement | 673 a year | Spouse aged 60 or over with unused supplement | 2026 | same |
| Child supplement, categories I, II, III, IV | 948, 475, 124, 96 a year | I: aged 16 to 26 studying abroad; II: 16 to 26 in MBO, HBO or university in Curacao; III: 16 to 26 in other education at home; IV: under 16 at home | 2026 | same |
| Substantial-interest income (aanmerkelijk belang) | 19.5% flat | 5% or more of issued shares, with spouse; regular benefits and disposal gains | 2026 | [Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/) |
| Deemed return (fictief rendement) | 4% of market value at 1 January | Under 5%, or no substantial interest, in an exempt company or a foreign investment company | 2026 | same |
| Rental income from real estate | 65% of the actual rent is declared | Loan interest, costs and linked premiums deductible | 2026 | same |
| Penshonado rate on foreign income | 10% (5% under the pre-1998 regime) | Conditions in "The base" | 2026 | [Tax Office Curacao, Penshonadoregeling](https://belastingdienst.cw/particulier/themas/penshonadoregeling/) |
| Penshonado forfait | ANG 500,000 (ANG 150,000 under the pre-1998 regime), taxed at the table | Chosen instead of the 10% rate; no double-tax relief under the Netherlands-Curacao arrangement | 2026 | same |
| Penshonado home value | at least ANG 450,000 | Owned for own use, not let, within 18 months of registration | 2026 | same |
| Late-filing penalty, income tax | ANG 250 (first time) to ANG 2,500 (fifth time) | After a reminder, with an ex officio assessment | 2026 | [Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/) |

The 2025 table, for 2025 returns still being filed: 9.75% to 38,225; 15% from 38,225 (tax 3,727); 23% from 50,968 (5,638); 30% from 76,452 (11,500); 37.5% from 108,306 (21,056); 46.5% from 159,273 (40,168); basic credit NAf 2,850 ([P.B. 2024 no. 143, Ministeriele regeling vaststelling bedragen inkomstenbelasting 2025](https://belastingdienst.cw/wp-content/uploads/2026/02/143.-MR-vaststelling-bedragen-IB-2025.pdf)). The Minister indexes the table and credits each year under art. 25 of the Landsverordening op de inkomstenbelasting 1943 (same source).

## The base

1. **Income** is income from work, business profit, income from movable capital, income from real estate and periodic payments ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
2. **Personal reductions** come off first: the employee AOV/AWW premium withheld from pay, AOV/AWW paid on the assessment, annuity premiums and blocked savings deposits (under conditions), and interest and costs of a study loan for your own profession (same page).
3. **Personal charges** are deductible: mortgage or other loan interest and costs for your own home, premiums of a term life policy, interest on other personal loans, and gifts to church, charitable, cultural, scientific and public-benefit bodies established in Curacao. Fire insurance and personal accident insurance are not deductible (same page).
4. **Extraordinary charges** are deductible: maintenance of children aged 27 or over, close relatives and sick or disabled children up to 26; illness, childbirth, disability and death; your own professional training; study costs of children up to 26 in further education (same page).
5. **Fixed employment-cost deduction.** The explanatory notes mention a fixed deduction of NAf 500 for professional costs, or actual costs ([Toelichting inkomstenbelasting](https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf)). The notes are not dated for 2026; confirm the amount on the 2026 return.
6. **Losses:** a negative taxable income from any of the previous five years is set off against this year's positive income ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
7. **Tax:** apply the table to taxable income, then deduct the basic credit and any supplements. Substantial-interest income is taxed separately at 19.5%. Wage tax withheld is credited on the assessment ([Toelichting inkomstenbelasting](https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf)).
8. **Non-residents** get no basic credit and no supplements ([Toelichting Loonbelastingverklaring 2026](https://belastingdienst.cw/wp-content/uploads/2026/01/Loonbelastingverklaring-2026-toelichting.docx-1.pdf)).

### Penshonado regime

All conditions apply ([Tax Office Curacao, Penshonadoregeling](https://belastingdienst.cw/particulier/themas/penshonadoregeling/)):
- aged 50 or over;
- lived outside Curacao for at least 60 consecutive months before arriving;
- request to the Inspector within 2 months of entry in the population register;
- within 18 months of registration, own a home in Curacao for own use worth at least ANG 450,000 and not let; or own a protected monument worth at least ANG 450,000, which may be let for no more than 4 months in any 12;
- neither you nor your spouse works, practises a profession or does other work in Curacao. Exception: a supervisory director, or an employee holding at least 40% (directly or indirectly) of the Curacao profit-taxpaying company, still qualifies, but that local income is taxed at the normal table.

What it covers: only foreign income, net of costs, such as foreign employment or past employment, a business run abroad through a permanent establishment, foreign real estate, foreign receivables and bank balances (not Curacao mortgages or claims on Curacao persons), profit shares and shares in foreign companies, gains on a substantial interest in a foreign company, periodic payments from a foreign debtor and interest in a foreign life-insurance payout. Other income is taxed at the normal table (same page). With only foreign income there is no right to the basic credit, supplements or personal and extraordinary charges, and the tax is at least 10% ([Toelichting inkomstenbelasting](https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf)).

The choice: 10% on actual foreign income, or a forfait of ANG 500,000 taxed at the table whatever was actually received. With the forfait there is no relief under the Netherlands-Curacao tax arrangement. Someone who chooses the 10% option can switch to the forfait only after 3 years. The right lapses for a year in which you or your spouse earn local employment or business income; two consecutive such years, or two consecutive years of late or incomplete returns, end it for good. Penshonados still pay BVZ and AVBZ premiums and, depending on age, AOV/AWW ([Tax Office Curacao, Penshonadoregeling](https://belastingdienst.cw/particulier/themas/penshonadoregeling/)).

## Deadlines and filing

- **Invitation:** the Belastingdienst sends an invitation by post; file online within two months of its date ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)). There is no fixed 31 May date.
- **Extension:** ask online before the two months run out ([Toelichting inkomstenbelasting](https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf)).
- **No invitation but income:** file of your own accord within 36 months from when the return for that year can be filed ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
- **First online return:** create a portal account first (same page). Round every amount to whole guilders, convert foreign currency to NAf at the published average rate, and upload proof of all income and expenses entered ([Toelichting inkomstenbelasting](https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf)).
- **Assessment:** the Inspector must impose the final assessment within 5 years after the tax year (longer if you had an extension), together with the final AOV/AWW, AVBZ and BVZ premium assessment. Pay within 2 months of receipt ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
- **Wage tax reduction during the year:** an employee with deductions can ask for lower withholding; see `cw-payroll-social`.

## Penalties and interest

- Not filed within 36 months, or not filed after an extension: a reminder, then an ex officio assessment and a penalty from ANG 250 the first time to ANG 2,500 the fifth time ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)). The 2026 Belastingdienst handbook gives the same range in Cg ([Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf)).
- Fault penalties for gross negligence or intent and interest on late income tax are not on the pages read: see "Not yet confirmed".

## Cross-border points

- Residents: worldwide income. Non-residents: Curacao income only, no credits ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
- A person who settles in Curacao and holds a substantial interest is taxed on a later sale only on the gain over the value at the date of settling ([Toelichting inkomstenbelasting](https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf)).
- Treaty or Kingdom-arrangement relief from wage tax needs an Inspector's statement; see `cw-payroll-social`. Treaty analysis itself is a refer item.
- The expatriate (ex-patriate) wage regime is in `cw-payroll-social`.

## Two worked examples that recompute

**Case 1: resident employee, 2026.** Unmarried, no children, taxable income 60,000. Band 3 applies: 5,767 + 23% of (60,000 less 52,127) = 5,767 + 1,810.79 = 7,577.79. Less the basic credit 2,915: income tax 4,662.79, before crediting wage tax withheld.

```oa-check
name: Curacao 2026 resident, taxable income 60000
inputs:
  taxable_income: 60000
  band3_floor: 52127
  band3_base_tax: 5767
  band3_rate: 0.23
  basic_credit: 2915
steps:
  - table_tax: band3_base_tax + (taxable_income - band3_floor) * band3_rate
  - tax_due: table_tax - basic_credit
expected:
  table_tax: 7577.79
  tax_due: 4662.79
```

**Case 2: penshonado decision, 10% or the forfait.** A retiree who qualifies has foreign pension and investment income of ANG 300,000 and no Curacao income. Option A: 10% of 300,000 = 30,000. Option B: the ANG 500,000 forfait at the 2026 table = 41,082 + 46.5% of (500,000 less 162,894) = 197,836.29. Option A is cheaper by 167,836.29. The forfait only wins once actual foreign income exceeds the break-even of 197,836.29 / 10% = 1,978,362.90; it also gives up relief under the Netherlands-Curacao arrangement. No basic credit applies, because the income is all foreign.

```oa-check
name: Penshonado 10 percent versus ANG 500000 forfait
inputs:
  foreign_income: 300000
  forfait: 500000
  penshonado_rate: 0.10
  band6_floor: 162894
  band6_base_tax: 41082
  band6_rate: 0.465
steps:
  - option_a: foreign_income * penshonado_rate
  - option_b: band6_base_tax + (forfait - band6_floor) * band6_rate
  - saving_with_a: option_b - option_a
  - break_even_income: option_b / penshonado_rate
expected:
  option_a: 30000.00
  option_b: 197836.29
  saving_with_a: 167836.29
  break_even_income: 1978362.90
```

## Ask the client first

1. Do you live in Curacao, and since when? Did you live abroad for 60 months before arriving (penshonado)?
2. Married or not, and the spouse's income for 2026?
3. Your income by type: wages (with the annual statement, jaaropgaaf), business profit, interest and dividends, rent, foreign income.
4. Do you, with your spouse, hold 5% or more of a company's shares?
5. Deductions: mortgage interest, AOV/AWW paid, annuity premiums, gifts, medical and study costs, children and their ages and schooling.
6. Have you received the invitation to file, and when? Any earlier years not filed?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Office Curacao, Schijven tarief 2026: read for the six 2026 bands, the tax at each lower limit and the rates | https://belastingdienst.cw/wp-content/uploads/2026/01/Schijven-tarief-2026.pdf | 2026-11-14 |
| Tax Office Curacao, Loonbelastingverklaring 2026: read for the 2026 basic credit, sole-earner, elderly and transferred elderly supplements and the four child categories | https://belastingdienst.cw/wp-content/uploads/2026/01/Loonbelastingverklaring-2026.pdf | 2026-11-14 |
| Tax Office Curacao, Toelichting Loonbelastingverklaring 2026: read for who gets each supplement and that non-residents get no credits | https://belastingdienst.cw/wp-content/uploads/2026/01/Loonbelastingverklaring-2026-toelichting.docx-1.pdf | 2026-11-14 |
| P.B. 2024 no. 143, Ministeriele regeling vaststelling bedragen inkomstenbelasting 2025: read for the 2025 table, the 2025 credits and the art. 25 indexation | https://belastingdienst.cw/wp-content/uploads/2026/02/143.-MR-vaststelling-bedragen-IB-2025.pdf | 2026-11-14 |
| Tax Office Curacao, Inkomstenbelasting (theme page): read for residence, income types, deductions, the 19.5% rate, the 4% deemed return, 65% of rent, loss set-off, filing, the 36-month rule, penalties and the assessment | https://belastingdienst.cw/particulier/themas/inkomstenbelasting/ | 2026-11-14 |
| Tax Office Curacao, Penshonadoregeling: read for the conditions, the 10% and 5% rates, the ANG 500,000 and 150,000 forfaits, the ANG 450,000 home and the lapse rules | https://belastingdienst.cw/particulier/themas/penshonadoregeling/ | 2026-11-14 |
| Tax Office Curacao, Toelichting inkomstenbelasting binnenlandse belastingplichtigen (undated, uploaded 2023): read for filing within two months, extensions, married couples, the NAf 500 cost deduction, the penshonado minimum of 10% and substantial-interest rules | https://belastingdienst.cw/wp-content/uploads/2023/02/Toelichting_inkomstenbelasting_binnenland_voor_website_v1.pdf | 2026-11-14 |
| Tax Office Curacao, Startende ondernemers: read for which legal forms pay income tax and which pay profit tax | https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/ | 2026-11-14 |
| Tax Office Curacao handbook "De basis van succesvol ondernemen" (2026): read for the income tax penalty range in Cg | https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf | 2026-11-14 |

Not yet confirmed: the 2026 ministerial regulation fixing the income tax amounts (the 2026 table and credits above come from the Belastingdienst's own 2026 table and the 2026 wage tax declaration, not the gazette text); whether the NAf 500 fixed cost deduction still applies for 2026; fault penalties (25%, 50%, 100%) and interest for income tax, which the pages read state only for profit tax; the official ANG to XCG conversion notice (published as an image); the expatriate regime change from 1 February 2025 said in the old file to require training of local staff (no official page found).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cw-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cw-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
