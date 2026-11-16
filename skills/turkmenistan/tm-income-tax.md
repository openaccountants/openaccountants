---
name: tm-income-tax
description: "Turkmenistan personal income tax for 2026: residence, taxable income, deductions, withholding, self-assessment and foreign-income relief, with explicit limits on unconfirmed deduction amounts and filing forms."
version: 1.1
jurisdiction: TM
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
---

# Turkmenistan personal income tax, 2026 (version 1.1)

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file without professional review.

## Scope

Compute ordinary personal income tax (PIT) and identify who withholds or files in Turkmenistan. The ordinary rate applies to a tax base after statutory exclusions and eligible deductions, rather than automatically to every receipt. Residents are within scope on worldwide income; non-residents on Turkmen-source income. The calendar year is the tax year. Tax Code arts. 5, 182-185: https://mejlis.gov.tm/single-code/10?lang=ru.

This Guide covers employment, ordinary business and professional income, interest, royalties, property receipts and securities or equity disposals. It also routes exemptions and special regimes. Pension contributions and the separate employee territorial-improvement levy belong to [payroll and social contributions](tm-payroll-social.md). A PIT result alone is not final take-home pay.

## Ask the client first

- Citizenship, permanent-residence status, days present in the tax year, transit days and any diplomatic posting or treaty-residence claim.
- Each receipt's nature, payer, source country, date, cash or non-cash value, and any registered-business or hydrocarbon-contract status.
- Main employment or other employment, joining date, cumulative income and tax already withheld by each payer.
- Documentary entitlement to exemptions, dependants and other deductions; the official current tax basic-unit value and voluntary pension or medical contributions.
- Business or professional expenses, securities acquisition costs, foreign tax paid and possible treaty refunds.
- Whether the person must self-file, is a foreign citizen leaving Turkmenistan, or needs an annual deduction correction.

## The method, step by step

### 1. Establish residence and source

A person is resident after presence totalling at least 183 calendar days in the tax year. Any part of a day counts, except presence solely in transit; foreign diplomatic, consular and international-organisation staff and their families have a posting exception. Residence is determined for each tax period. Then apply worldwide or Turkmen-source scope; nationality alone does not decide PIT residence. Tax Code art. 14(3)-(5): https://mejlis.gov.tm/single-code/10?lang=ru.

Article 184 defines local source, including employment and civil-contract remuneration paid by the specified resident entities, local establishments or individual entrepreneurs, local property rent and professional activity through a fixed place in Turkmenistan. Read the source facts before applying the rate to a foreign payer: own-account foreign-trade activity without such a fixed place, and payments by a resident entity's foreign branch, have specific exclusions in art. 184(2). Tax Code arts. 183-184: https://mejlis.gov.tm/single-code/10?lang=ru.

### 2. Classify the receipt before computing

Start with money, benefits in kind and material or social benefits, subject to the statutory exclusions. Foreign currency is translated at the Central Bank's official rate on the receipt date. Cash receipt or bank credit, transfer in kind, discharge of a debt and receipt of a benefit determine the ordinary receipt date; entrepreneurial recognition follows its separate business rule. Tax Code arts. 185-186, 190: https://mejlis.gov.tm/single-code/10?lang=ru.

Property rent is distinct from property disposal. Ordinary sales of personally owned property are excluded, except business disposals and disposals of shares, bonds, other securities or equity interests. Bank-deposit and individual deposit-certificate interest is excluded; do not label all interest taxable. Statutory pensions, qualifying insurance proceeds, gifts or inheritances from individuals and qualifying compensation also have exclusions. Unused-leave compensation does not share the employment-compensation exclusion. Read the relevant art. 187 category and its evidence before excluding a payment. Tax Code art. 187(1)(b)-(g), (l), (t): https://mejlis.gov.tm/single-code/10?lang=ru.

### 3. Compute the ordinary base and tax

| Item and condition | Amount or rule for 2026 | Official URL |
|---|---|---|
| Ordinary PIT, including taxable local-source income of non-residents; exceptions below | 10%; no ordinary progressive bands, art. 192(1) | https://mejlis.gov.tm/single-code/10?lang=ru |
| General monthly deduction, when allowable | One statutory tax basic unit per month, art. 188(1)(a); current TMT value is not confirmed here | https://mejlis.gov.tm/single-code/10?lang=ru |
| Disability caused by specified emergencies; other qualifying disability | Four or two basic units respectively, art. 188(1)(b)-(c); check the complete income exemptions first | https://mejlis.gov.tm/single-code/10?lang=ru |
| Qualifying dependants; qualifying bereaved military parent or spouse | One basic unit per dependant, or three basic units respectively, art. 188(1)(d)-(e); choose the largest entitlement among (b)-(e), do not stack those categories | https://mejlis.gov.tm/single-code/10?lang=ru |
| Voluntary pension or medical insurance | Deduct qualifying contributions, art. 188(2), with the main-employment withholding limitation below | https://mejlis.gov.tm/single-code/10?lang=ru |
| Ordinary tax rounding | Below 50 tenge is discarded; 50 tenge or more rounds up to a whole manat, art. 193(4) | https://mejlis.gov.tm/single-code/10?lang=ru |

Use `base = max(0, taxable receipts - allowable deductions)`. Business expenses must be actual, documented and income-related, applying the corporate expense rules referenced in art. 189(1)(a). Professional or civil-contract expenses must be directly connected and documented. For the professional/civil-contract and author categories in art. 189(1)(b)-(c), art. 189(2) limits actual-expense deductions to the work- or service-related material expenses specified in art. 155, including VAT. Documentation alone does not permit deduction of every type of professional cost. For securities and equity disposals, deduct documented acquisition and disposal costs. Authors can have statutory expense allowances where documentation is absent; do not combine those allowances with actual expenses for the same calculation. The allowance classification must be separately established before use. Tax Code arts. 185(3), 189: https://mejlis.gov.tm/single-code/10?lang=ru.

The monthly general deduction is a tax basic unit, not a minimum-wage figure. **Do not use the former TMT 1,280 approximation.** Obtain the current official instrument establishing the unit before producing a manat deduction or a final assessment that depends on it. Dependants require actual maintenance and the statutory evidence; pensioners, scholarship recipients and the other state-supported categories listed in art. 188(1)(d) do not qualify merely because they are family members. Tax Code art. 188: https://mejlis.gov.tm/single-code/10?lang=ru.

### 4. Decide withholding or self-assessment

A resident entity, local foreign branch, representative office or permanent establishment, or individual entrepreneur normally acts as tax agent for the covered payments. Payments to registered individual entrepreneurs are excluded from this agent rule. Compute ordinary agent tax cumulatively from the beginning of the year, less tax withheld in earlier months. Withhold on each payment. Agents normally give no arts. 188-189 deductions; the exception is art. 188 deductions for employment at the main workplace, and even those are unavailable at withholding for the first incomplete month of work. Tax Code art. 195(1)-(4): https://mejlis.gov.tm/single-code/10?lang=ru.

Self-assess income paid by non-agent individuals, resident foreign-source income, relevant business or professional income and income on which the agent did not withhold. Credit agent tax already withheld against the calculated assessment. A person without a compulsory declaration may file to obtain an annual deduction recalculation. Tax Code arts. 188(5), 196, 197(1): https://mejlis.gov.tm/single-code/10?lang=ru.

## Boundary and exception table

| Facts | Treatment | Official URL |
|---|---|---|
| Personal property sale versus securities or business disposal | Apply the personal-property exclusion only to the eligible category; taxable disposals can use documented costs, arts. 187(1)(l), 189(1) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Disability, protected status, young graduate specialist or qualifying award | Art. 187(5) contains complete exemptions and tax reductions; establish the exact category and evidence before using the ordinary calculation | https://mejlis.gov.tm/single-code/10?lang=ru |
| Qualifying youth entrepreneur | Art. 192(1) has a conditional early-years reduction; verify classification, workforce and activity-year facts before applying it | https://mejlis.gov.tm/single-code/10?lang=ru |
| Listed small-business activity | Art. 200 uses a separate fixed-plus-gross-income regime; do not apply the ordinary net-income method without classifying the activity | https://mejlis.gov.tm/single-code/10?lang=ru |
| Gambling or employee of hydrocarbon contractor/subcontractor | Separate rules in arts. 192(2), 194; obtain the applicable operative provisions before calculating | https://mejlis.gov.tm/single-code/10?lang=ru |
| Resident with foreign tax | Art. 198(1) credit requires official foreign payment evidence and is capped at Turkmen PIT on that income; check treaty refund rights | https://mejlis.gov.tm/single-code/10?lang=ru |
| Non-resident claiming treaty relief | Art. 198(2) requires an effective treaty, residence confirmation and the prescribed application; nationality alone gives no relief | https://mejlis.gov.tm/single-code/10?lang=ru |

## Worked cases

### Case 1: first incomplete employment month

Illustrative inputs: an ordinary employee receives TMT 5,000 for the first incomplete month at the main workplace, with no exemption or reduction and no earlier tax in the year. At withholding the agent cannot grant art. 188 deductions for that incomplete month. PIT is TMT 5,000 × 10% = TMT 500. This is the payment withholding result; an eligible annual deduction correction is a separate step. Tax Code arts. 192(1), 195(3): https://mejlis.gov.tm/single-code/10?lang=ru.

```oa-check
name: First incomplete month, agent PIT
inputs:
  salary: 5000
steps:
  pit: salary * 0.10
expected:
  pit: 500
```

### Case 2: personal property or securities disposal

Illustrative inputs: sale proceeds TMT 10,000 and documented acquisition and disposal costs TMT 7,000. An ordinary personal-property sale outside business is excluded, so its PIT is nil. A securities disposal falls outside that exclusion: the gain component before any separate art. 188 annual deductions is TMT 3,000 and the ordinary PIT attributable to that component is TMT 300. This comparison does not invent a current basic-unit value or represent a final annual assessment. Tax Code arts. 187(1)(l), 189(1), 192(1): https://mejlis.gov.tm/single-code/10?lang=ru.

```oa-check
name: Personal property versus securities gain component
inputs:
  proceeds: 10000
  documented_costs: 7000
steps:
  personal_property_pit: proceeds * 0
  taxable_gain: max(0, proceeds - documented_costs)
  securities_component_pit: taxable_gain * 0.10
expected:
  personal_property_pit: 0
  taxable_gain: 3000
  securities_component_pit: 300
```

## When to refuse or refer

Do not give a final deductible amount without an official current basic-unit value, or an exemption or treaty result without the required evidence. Refer unresolved special-business, gambling, hydrocarbon, occupational or protected-status classifications to a local practitioner with the operative instruments. Do not invent a portal, return identifier or box number. Explain which component can be computed and which remains on hold.

## Filing and payment

| Obligation and condition | Statutory timing | Official URL |
|---|---|---|
| Agent remittance on bank-funded cash or bank transfer | No later than bank cash withdrawal for the payment or the income transfer day, art. 195(5) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Agent remittance on income in kind | No later than the day following receipt, art. 195(5) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Annual agent income and tax information | By 20 January following the tax year, art. 195(9) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Ordinary self-filer other than foreign citizen | Return by the 25th of the month after the reporting period; payment by the 10th of the second month, arts. 196(3), 197(1) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Foreign citizen required to self-file | Return by 1 April and payment by 15 April after the tax year, arts. 196(3), 197(1) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Foreign citizen ceasing activity and departing | Return at least one month before departure; additional assessed tax within 15 days of filing, art. 197(2) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Agent refund of excess withholding after taxpayer application | Within 30 days of the application, art. 195(8) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Treaty application | Before payment or within three years after the tax period ends, with prescribed documentation, art. 198(2) | https://mejlis.gov.tm/single-code/10?lang=ru |

Article 191 defines the reporting periods as the first half-year and the tax year where an in-year declaration is required. Do not turn every employee into a self-filer or invent a universal monthly PIT return. File at the relevant tax registration office, report receipts, sources, deductions, tax withheld and paid, and the balance due or refundable. Obtain the current Ministry-approved declaration and income certificate; their current form, electronic route and box mapping have not been confirmed here. Tax Code arts. 30(1), 191, 195(6)-(9), 197(3): https://mejlis.gov.tm/single-code/10?lang=ru.

Late-payment interest is generally 0.03% per calendar day, including payment day, subject to art. 70's limitation and exceptions, including specified bank-processing time and official calculation errors. Do not compute a penalty total without the tax due date, notices and the complete arrears facts. Tax Code art. 70: https://mejlis.gov.tm/single-code/10?lang=ru.

## Completion checklist

Confirm residence and source, apply exclusions, document deductions and their current unit, compute cumulative or self-assessed tax and rounding, credit prior tax, select the correct citizenship-dependent filing route, and retain the payment and withholding certificates. Report any uncomputed component explicitly.

## Sources

| Official source and actual scope read | URL | Read on |
|---|---|---|
| Mejlis, official consolidated Tax Code in Russian: arts. 3-6, 14 and 30(1); arts. 70, 182-200 covering source, exclusions, deductions, computation, agent and individual filing, treaty procedure and special regimes; neighboring exemption and expense conditions read | https://mejlis.gov.tm/single-code/10?lang=ru | 2026-11-16 |

Not yet confirmed: the current TMT value and operative instrument for the tax basic unit; current Ministry-approved return/certificate/application forms, electronic portal and box mapping; applicable special-regime instruments or treaty text for a specific claimant. These are not usable assumptions. The ordinary statutory rules above were read on the official consolidation; this is not a claim that every specialist regime has been verified.
