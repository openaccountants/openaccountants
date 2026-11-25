---
name: pg-corporate-income-tax
description: >
  Compute ordinary PNG company and permanent-establishment tax for 2026, distinguish commercial-bank marginal rates, classify domestic non-resident withholding, reconcile GST, and use the new statutory filing and provisional-payment rules. Resource-project agreements, treaty relief, special funds and unresolved regulatory inputs require separate evidence.
jurisdiction: PG
category: international
tax_year: 2026
last_updated: 2026-11-22
version: 1.1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Papua New Guinea corporate income tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Compute ordinary company income tax and identify PNG permanent-establishment, bank and non-resident-payment exceptions for the 2026 tax year. The Income Tax Act 2025 commenced on the first day of that year; it and the enacted budget amendment replace reliance on repealed income-tax rate Acts. This is not a resource-project return, treaty opinion, transfer-pricing study or fund return. [Income Tax Act ss. 163-165](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### Quick reference

| Tax or condition | Current rule | Official source |
|---|---|---|
| Ordinary company | 30% of taxable income, including an ordinary non-resident company's PNG permanent establishment | [Income Tax Act s. 11, Sch. 1 Part I clause (5)(d)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Commercial bank, fiscal 2026 | 35% on taxable income under PGK 300 million and 43% on taxable income over that boundary; marginal bands, not a separate levy on all income | [Sch. 1 Part I clause (5)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Approved superannuation fund | 25%; a non-approved fund is 30%, requiring the separate fund rules | [Sch. 1 Part I clause (5)(a), (b), s. 118](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Non-resident PE repatriated profit | 15% on the statutory amount; not just a cash dividend or cash remittance | [ss. 14, 71 and Sch. 1 Part I clause (9)(f)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| International transport | 2.4% of the source-defined gross transportation income, with exclusions and special collection rules | [s. 15, ss. 139-140, Sch. 1 Part I clause (13)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Domestic capital gains tax | 15% for the defined taxable-asset regime; not a blanket tax on every sale gain | [Part V (ss. 81-84) and Sch. 1 Part I clause (21)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

The bank's upper marginal rate steps down for later fiscal years: 42% in 2027, then 1 percentage point annually until it reaches 35% in 2034. This skill's numerical bank cases are for fiscal 2026 only. Use the applicable year's schedule and approved accounting period, not a generic blended percentage. [Schedule 1 Part I clause (5)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

## Ask the client first

Obtain incorporation and management/control facts, tax accounting year and approvals, resident or non-resident status, PNG activities and PE facts, financial accounts, tax reconciliation, losses, capital allowances, GST registration, exempt and foreign income, withholding certificates, provisional payments, related-party transactions and applicable agreements. Ask whether it is a licensed commercial bank, non-profit company, fund or resource licensee before applying the ordinary rate. Record the tax agent's registration if relying on the agent-prepared company deadline.

## The method, step by step

1. **Determine residence and source.** A company incorporated, created or formed in PNG, or centrally managed and controlled there, is resident; further specified fund and trust vehicles are included by the definition. A resident includes worldwide assessable income, subject to exemptions and foreign-income rules. A non-resident includes PNG-source assessable income, with source and PE attribution tested under the Act. An invoice destination alone does not establish source. [ss. 7-10, 18(4)-(5), 23-25 and 66-70](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).
2. **Select the period and accounting basis.** A company's accounting year follows the annual balance of its financial accounts. Changing it for tax purposes requires prior written IRC approval, with transitional rules. Companies use accrual accounting. Do not assert that every company must already have a calendar financial year; the default fiscal-year convention is not an approved company balance date. [ss. 42-45](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).
3. **Build the taxable-income reconciliation.** Start from financial profit, identify assessable income, deduct source-connected allowable expenses and make explicit adjustments for exempt income, capital expenditure, depreciation versus statutory capital allowances, private spending, income tax, fines, losses and any withholding-related deduction delay. Keep GST output outside assessable income and recoverable input GST outside deductions and asset cost. An irrecoverable cost still needs the revenue-versus-capital test. [ss. 23-41 and 46](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).
4. **Check special regimes before applying a rate.** Resource projects need Part VII, ring-fencing, additional profits tax and any surviving project/fiscal-stability terms. Do not use a quoted ordinary mining rate to finalise an oil, gas or mining agreement. Approved funds, banks and non-profits have separate conditions. [s. 11, Part VII, ss. 117-119, 164 and Sch. 1](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).
5. **Compute ordinary or bank income tax.** Apply the ordinary company rate to taxable income, or the bank marginal bands. Apply credits in the statutory order and reconcile each credit to certificates and payments. Do not invent treaty relief, group loss offsets or an infrastructure credit. The enacted budget amendment changes eligible infrastructure-credit rules and creates a petroleum-levy credit, but those require their own eligibility proof. [s. 11 and Sch. 1](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf); [budget amendment ss. 1-2](https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050).
6. **For a non-resident PE, separately calculate repatriated profit.** The formula is opening net asset cost plus financial net profit minus income tax minus closing net asset cost. The opening asset value carries forward from the preceding year's closing value. Reconcile assets, liabilities and accounting profit, rather than assuming all after-tax profit was remitted. Apply the non-resident tax to that statutory base and include it in the return. [ss. 14, 71 and 135(2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).
7. **Review payments to non-residents.** Determine the legal payment type, PNG source, beneficial recipient, associate status, treaty and any PE attribution or statutory exemption. The domestic rates below are not treaty quotations. Gross-up and recharged technical-service/royalty arrangements need contract analysis. [ss. 14, 72, 154 and Sch. 1](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

| PNG-source payment to a non-resident | Domestic rate and conditions | Official source |
|---|---|---|
| Ordinary dividend | 15%; qualifying non-profit or former non-profit exempt-income distributions instead 30% | [s. 14 and Sch. 1 Part I clause (9)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Interest, technical fee, annuity or natural-resource amount | 15%; check source and exclusions first | [s. 14 and Sch. 1 Part I clause (9)(d)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Royalty to an associate | 30% | [s. 14 and Sch. 1 Part I clause (9)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Other royalty | 10% | [s. 14 and Sch. 1 Part I clause (9)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Insurance premium | 3% | [s. 14 and Sch. 1 Part I clause (9)(a)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Entertainer | 10% | [s. 14 and Sch. 1 Part I clause (9)(b)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

A PNG PE-attributable amount is not automatically taxed again at the gross non-resident rate; read the exclusions in the non-resident-tax provision. A treaty may alter a domestic outcome only after the treaty article, residence, recipient conditions and effective period are checked. No default treaty dividend or interest cap is supplied. [s. 14(4) and treaty provisions](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### Filing, payments and provisional tax

| Job | Statutory timing and conditions | Official source |
|---|---|---|
| Company return prepared by a registered tax agent | Within 9 months of tax-year end | [s. 135(1)(a)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Other company return | Within 6 months of tax-year end | [s. 135(1)(b)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Calendar-year 2026 illustrations | Derived: 30 September 2027 for agent-prepared company return; 30 June 2027 otherwise | [s. 135(1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Income tax and PE non-resident tax | Return due date for a self-assessment; the assessment notice's specified date otherwise | [s. 137](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Provisional income tax | 3 instalments, last day of the month following the third, sixth and ninth tax-year months | [s. 138](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Calendar-year 2026 instalment dates | 30 April, 31 July and 2 November 2026. The last instalment rolls forward because 31 October is a Saturday. | [s. 138](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf); [TAA s. 68](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d); [IPA business calendar](https://www.ipa.gov.pg/public/Holidays.aspx?lang=en-US) |
| Non-employment withholding return and payment | By 21st of the month after the payment month, unless the specific collection rule applies | [s. 158](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Annual withholding statement | Within 3 months of fiscal-year end | [s. 159](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

Each ordinary provisional instalment is **(A - B) / 3**. A is the most recent assessed income-tax liability, including self-assessment, reduced by the foreign tax credit allowed for that year and multiplied by the prescribed regulatory uplift factor. B is the part of A paid by withholding under Part X. Subtract B before dividing by three, not after. The uplift factor has not been read in a current Regulation and must not be assumed. For a new income taxpayer or most recent return showing a net loss, the Act instead sets each instalment at 2% of the relevant quarter's assessable income not subject to withholding. A variation election needs reasonable grounds, the approved form and timely lodgement. Payments become credits, not deductions. [s. 138](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Prepare the IRC return from the reconciliation and actual applicable form, attach accounts and supporting schedules as required, submit through the authorised IRC channel, preserve the acknowledgement and match payment to the taxpayer ledger. The live 2026 portal fields and any administrative extensions were not accessed; do not invent a form-box mapping, an extension or a submission receipt.

### Income-tax administration

The Income Tax Act's administration clause incorporates the Tax Administration Act 2017, with the cross-reference corrections in the enacted budget amendment. Keep a penalty separate from interest and from the underlying tax. A penalty requires an IRC assessment and notice; remission may be requested. Do not turn these statutory exposures into an automatic debit in a working paper. [Income Tax Act s. 133 and amendment s. 3](https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050); [TAA ss. 39, 93-101](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d).

| Default | Statutory amount and conditions | Official source |
|---|---|---|
| Late filing | Higher of 20% of tax due, or PGK 200 per month or part month for a company and PGK 100 for another person | [TAA s. 93](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Late payment penalty | 20% of unpaid tax, in addition to interest; tax for this purpose excludes penalty and interest | [TAA s. 94](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Late payment interest | Central Bank rediscount rate at the start of the relevant period plus 5 percentage points; simple interest calculated daily, not a fixed annual penalty rate | [TAA s. 39](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Tax shortfall | 100% for deliberate or reckless statements; otherwise 25%, subject to repeat-default increases, timely-disclosure reductions and statutory defences | [TAA s. 95](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Retention | 7 years after the tax period, extended for unexpired amendment periods, unused losses, audits and proceedings | [TAA s. 11](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Objection and review | Objection within 60 days of service; Tribunal review normally within 28 days of service of the reviewable decision; National Court appeal on law within 28 days of notification, with extension powers | [TAA ss. 24-27, 79](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |

Preserve the notice, service date, grounds, return, undisputed-tax payment and disputed-tax payment arrangements. An objection does not itself suspend collection. Obtain current legislation and the actual IRC decision before advising on a dispute, transition or enforcement case. The current rediscount rate and day-count denominator are not supplied here, so no numerical interest estimate is authorised.


### Exceptions

| Fact pattern | Required treatment |
|---|---|
| Branch retains assets or introduces capital | Recompute statutory repatriated profit; a blanket combined rate is not sufficient |
| Exempt or foreign income | Trace the exemption and separate foreign credits/losses before applying them |
| Related-party fees, interest or royalties | Test source, arm's-length terms, deduction limits, withholding and recharges |
| Shipping or airline income | Use the special gross-income and departure-clearance collection rules; not ordinary company turnover |
| Extractive project or fiscal stability | Obtain the actual agreement, licence and transition provisions; no generic petroleum rate |

## Worked cases

### Ordinary resident company

An ordinary resident trading company has assessed taxable income of PGK 100,000 after its completed tax reconciliation, no special regime and provisional payments of PGK 12,000. Tax is PGK 30,000 and the remaining income-tax balance is PGK 18,000. [s. 11, s. 138(9), Sch. 1 company rate](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG ordinary company with provisional credits
inputs:
  taxable_income: 100000
  provisional_paid: 12000
steps:
  - income_tax: taxable_income * 0.30
  - balance: income_tax - provisional_paid
expected:
  income_tax: 30000
  balance: 18000
```


### Non-resident PE: derived combined example

Opening and closing net asset cost are equal. Financial profit and taxable income are both PGK 100,000, with no further adjustment, treaty relief or credit. Company income tax is PGK 30,000. Statutory repatriated profit is PGK 70,000 and its non-resident tax is PGK 10,500. Combined tax is PGK 40,500 in these facts only. If closing net assets increase, the statutory base changes. [ss. 14, 71, Sch. 1](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG PE statutory repatriated profit
inputs:
  opening_net_assets: 500000
  closing_net_assets: 500000
  financial_profit: 100000
  taxable_income: 100000
steps:
  - income_tax: taxable_income * 0.30
  - repatriated_profit: opening_net_assets + financial_profit - income_tax - closing_net_assets
  - non_resident_tax: repatriated_profit * 0.15
  - combined_tax: income_tax + non_resident_tax
expected:
  income_tax: 30000
  repatriated_profit: 70000
  non_resident_tax: 10500
  combined_tax: 40500
```


### Commercial bank, fiscal 2026

On taxable income of PGK 400 million, the lower band contributes PGK 105 million and the upper band PGK 43 million. The total is PGK 148 million, not a higher levy imposed on the whole base. [Sch. 1 Part I clause (5)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG commercial bank marginal rates in fiscal 2026
inputs:
  taxable_income: 400000000
steps:
  - lower: min(taxable_income,300000000) * 0.35
  - upper: max(taxable_income - 300000000,0) * 0.43
  - tax: lower + upper
expected:
  tax: 148000000
```


## When to refuse or refer

Stop finalisation if the accounting year, residence, taxable-income reconciliation, PE net assets or payment classifications are unresolved. Refer projects, fund returns, treaty positions, unverified uplift factors and enforcement cases to a PNG-qualified practitioner. Do not remove an existing exemption, condition or loss restriction merely to produce a number.

## Sources

Original sources read on 16 November 2026. The business-day rule and calendar were checked on 23 November 2026.

| Official source and scope read | URL | Read on |
|---|---|---|
| Read for Income Tax Act 2025: residence, income/deductions, accounting and GST, PE and foreign-income rules, project boundaries, ss. 133-160 and Schedule 1 | https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf | 2026-11-16 |
| Read for Enacted Income Tax 2026 Budget amendment: ss. 1-4 and commencement | https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050 | 2026-11-16 |
| Read for Tax Administration Act 2017: ss. 11, 18, 24-27, 39, 79, 92-101, as incorporated for income tax | https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d | 2026-11-16 |
| Read for Tax Administration Act 2017: s. 68, due dates falling on weekends or public holidays | https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d#page=48 | 2026-11-23 |
| Read for the 2026 business calendar, including the business day after 31 October | https://www.ipa.gov.pg/public/Holidays.aspx?lang=en-US | 2026-11-23 |

Not yet confirmed: Current provisional-tax regulatory uplift, live 2026 IRC return fields, actual extensions, current interest-rate input and taxpayer-specific treaty/project terms. Company statutory deadlines are verified, but no administrative extension is assumed.
