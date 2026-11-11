---
name: fk-cross-border-tax
description: "Determine Falkland Islands cross-border income-tax exposure in 2026 for individuals, companies and payers. Covers domestic residence and source, the separate UK double-tax arrangement, ordinary business permanent establishments, short-stay employment, foreign-tax-credit limits and withholding on overseas company interest. Use for non-resident Falklands tax, overseas salary, UK treaty, branch activity, foreign tax relief and interest payments. Distinguishes ordinary cases from petroleum and offshore activities, which have overriding provisions. Includes a withholding calculation and a treaty short-stay decision case. It is not a general UK tax guide and does not apply UK treaties automatically to the Falkland Islands."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/fk-cross-border-tax"
  jurisdiction: "FK"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Falkland Islands cross-border tax 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

For an individual arriving, leaving or earning abroad, a company doing business across borders, or a local payer paying overseas. Establish domestic residence/source first, then apply the actual arrangement where available. FIGTO identifies the UK arrangement as its only double-tax agreement. Being a British territory does not make every UK treaty applicable here. [FIGTO 2026 guide §§2-4](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/General-Tax-Guide-Individuals-2026.pdf); [CT guide §3](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/CT-guide0.pdf).

Quick answer: use domestic law, check treaty entitlement and the income article, then withholding and credit. An exemption from final tax and an employer's withholding procedure are separate questions.

## Rates, bands and thresholds

| Item | Rule with conditions | Official source |
|---|---|---|
| Individual residence | At least 183 days' physical presence in the income year; ordinary residence is a separate continuing test | [2026 guide §3](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/General-Tax-Guide-Individuals-2026.pdf) |
| Company interest withholding | 10% of gross paid or credited by a payer company to an overseas payee company within §34A; exclusions and Commissioner notice may apply | [§34A(1)-(6)](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf#page=35) |
| Interest return and payment | Within 30 days after the end of the payment/credit month | [§34A(6)-(7)](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf#page=36) |
| UK short-stay employment | Not exceeding 183 days in any twelve-month period commencing or ending in the fiscal year, plus non-local employer and no local PE/fixed-base cost bearing; other articles may override | [Arrangement ¶15(2)](https://legislation.gov.fk/download/pdf/c871204a-34a4-4b9d-bd91-ff44c386edc3/9789caf0-20f5-446e-a321-5ecf4c734db7/fisl-1996-37_2024-10-10.pdf#page=12) |
| UK construction PE | Site/project/supervision lasting more than six months; ordinary fixed-place and dependent-agent tests remain | [Arrangement ¶5](https://legislation.gov.fk/download/pdf/c871204a-34a4-4b9d-bd91-ff44c386edc3/9789caf0-20f5-446e-a321-5ecf4c734db7/fisl-1996-37_2024-10-10.pdf#page=5) |
| Foreign credit claim | Normally no later than two years after the relevant chargeable period; adjustment exception under §166(7) | [§166(6)-(7)](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf#page=172) |

Use [fk-income-tax, exemptions](fk-income-tax.md#the-base) for the separate domestic short-visit exemption; it does not depend on UK treaty status. Count arrival/departure days under §200(3). The calendar-year domestic residence test is different from the rolling treaty short-stay test. Do not equate them.

## The base

Individuals resident or ordinarily resident here normally include worldwide income. Neither-resident-nor-ordinarily-resident people exclude foreign-source income under §13, but duties performed in the Islands are local-source even if paid from abroad. Mixed duties require proper allocation; merely incidental foreign duties can remain part of a local employment. [§§8, 13](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf).

Companies are resident if incorporated or centrally managed and controlled here. Resident worldwide profits and non-resident local profits follow §§23-25 and 34. Qualifying UK business profits use ¶7 and the ¶5 permanent-establishment definition. A fixed place can be rented or shared; the construction time limit does not protect an existing office or an agent habitually exercising contract authority. [FIGTO CT guide §§2-3](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/CT-guide0.pdf); [Arrangement ¶¶4-7](https://legislation.gov.fk/download/pdf/c871204a-34a4-4b9d-bd91-ff44c386edc3/9789caf0-20f5-446e-a321-5ecf4c734db7/fisl-1996-37_2024-10-10.pdf).

For interest withholding, §34A also covers a non-resident payer carrying on a local branch/agency to which the interest relates. An overseas payee is not simply any foreign bank account: check residence, local branch attribution and the statutory definitions. The Schedule A1 territory exception requires the specified territory connection, beneficial ownership, taxation there and absence of a tax-advantage arrangement. A territory name alone is insufficient. Retain payment/credit date, gross amount, recipient identity/residence and relief evidence. [§34A and Sch A1](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf#page=35).

Treaty credit under §166(3) requires residence in the Islands for the chargeable period and a claim, with limits under §§166-168. For an individual the limit is the difference between tax on total income and tax excluding the relevant foreign income, subject also to total tax; company credit is limited to attributable corporation tax. §169 grants unilateral credit to resident or ordinarily resident people for qualifying foreign-source income and overseas tax outside an arrangement, incorporating §§166-168 for calculation, capped at the lower eligible foreign tax and Falkland tax. Employment actually performed here is excluded from §169's foreign-source definition. Do not deduct foreign tax and also claim full credit on an inconsistent base. [§§166-169](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf#page=171).

## Deadlines and filing

Use the ordinary return, accounts and tax computation in [fk-income-tax](fk-income-tax.md) or [fk-corporate-income-tax](fk-corporate-income-tax.md). Provide foreign income gross, foreign assessments and payment evidence, currency reconciliation, residence support and a credit calculation. Record any refund entitlement and subsequent adjustment so no credit exceeds final foreign tax. [FIGTO 2026 guide §2](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/General-Tax-Guide-Individuals-2026.pdf).

A §34A payer withholds from gross interest and submits its return and payment within the deadline above; §34A(7) specifies gross amount, date, payee identity/address, payment account where paid, and tax deducted. Certify the return correct and send its copy to the overseas payee within one month of payment/credit. That payee-copy clock differs from the 30-days-after-month-end return/payment clock. Obtain FIGTO's current return format rather than invent a box. Tax-treaty relief must be supported before relying on it; resolve payroll operation with FIGTO rather than silently switching POAT off. [§34A](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf); [Employer guide](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/2026-Employers-Guide.pdf).

## Penalties and interest

Ordinary assessment, late return and payment rules continue, including §§11, 12A and 33. Withholding compliance is a separate payer responsibility. Specific §34A offence/penalty provisions and Part IX can apply; no universal treaty late-claim extension is assumed. See the underlying income/company Guide for the ordinary quantified sanctions. [Ordinance](https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf).

## Cross-border points

| Boundary | Result |
|---|---|
| Short UK visit, but Falkland employer or salary borne by local PE | ¶15(2) exemption fails even below the day limit |
| Pension | ¶18 has residence/subject-to-tax conditions; government service uses ¶19 |
| Offshore resource activity | ¶21 overrides other articles and has its own PE and employment rules; do not use ordinary ¶15 short-stay relief |
| Oil-connected company payment | Schedule 6 withholding is a separate regime; FIGTO identifies 3% with scope and exemption conditions, not a general foreign-payment levy |
| Related-party charge | Test [fk-transfer-pricing](fk-transfer-pricing.md), deductibility and withholding separately |

[Arrangement ¶¶15, 18-21](https://legislation.gov.fk/download/pdf/c871204a-34a4-4b9d-bd91-ff44c386edc3/9789caf0-20f5-446e-a321-5ecf4c734db7/fisl-1996-37_2024-10-10.pdf); [FIGTO CT guide §15](https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/CT-guide0.pdf). Detailed petroleum and Schedule 6 administration are out of scope; refer those cases before payment.

## Two worked examples that recompute

**Interest.** Assume gross GBP 20,000 credited to a qualifying overseas payee and no Schedule A1 exception, treaty reduction or Commissioner exclusion. §34A withholding is GBP 2,000 and net payment GBP 18,000. Crediting can trigger the obligation before cash moves.

```oa-check
name: Overseas company interest withholding
inputs:
  gross_interest: 20000
steps:
  withholding: gross_interest*0.10
  net: gross_interest-withholding
expected:
  withholding: 2000
  net: 18000
```

**Short-stay decision.** Assume a UK treaty resident employed for GBP 10,000 for ordinary duties here for 100 days, with all rolling-period presence counted, no other relevant article, a UK employer and no local PE/fixed base bearing the cost. All ¶15(2) conditions are assumed proved, so treaty-taxable local remuneration is zero. If a local PE bears the same entire cost, exemption fails and GBP 10,000 is potentially taxable locally under ¶15(1); annual allowance, deductions and POAT determine final tax separately. This case computes the allocation, not a fictitious final flat tax.

```oa-check
name: Short-stay exemption versus local cost bearing
inputs:
  remuneration: 10000
steps:
  exempt_local_base: remuneration*0
  local_cost_borne_base: remuneration
expected:
  exempt_local_base: 0
  local_cost_borne_base: 10000
```

## Ask the client first

- Domestic and treaty residence, ordinary-residence history and day-by-day presence.
- Actual location of duties, business premises and contract authority.
- Employer residence and who economically bears salary costs.
- Income type, payer/payee status, ownership, payment and credit dates.
- Foreign assessments, tax paid, refund rights and previous credits.
- Offshore/resource activity, defence exemption and related-party arrangements.

## Sources

| Source and text actually read | URL | Read on |
|---|---|---|
| Taxes Ordinance June 2026 consolidation, §§2, 8, 13, 23-34A, 57(1)(r), 165-169 and 200 and Sch A1, including interest exception conditions. §34A: “10% of the amount of the payment”; §169: “whichever is the less” | https://legislation.gov.fk/download/pdf/05a29220-06c3-4560-867c-99d6c5200d0d/15f327cc-37ae-4304-a080-e3d54a80bd43/fiord-1997-14_2026-06-12.pdf | 2026-11-11 |
| UK arrangement, consolidated October 2024; ¶¶1-7, 15, 18-21, including neighbouring exceptions. ¶15: “not exceeding in the aggregate 183 days in any twelve month period” | https://legislation.gov.fk/download/pdf/c871204a-34a4-4b9d-bd91-ff44c386edc3/9789caf0-20f5-446e-a321-5ecf4c734db7/fisl-1996-37_2024-10-10.pdf | 2026-11-11 |
| FIGTO 2026 individual guide, §§2-6, worldwide income and credit evidence | https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/General-Tax-Guide-Individuals-2026.pdf | 2026-11-11 |
| FIGTO corporation guide, §§2-3 and 10, 14-15, treaty scope and special withholding boundaries | https://www.gov.fk/taxation/wp-content/uploads/sites/25/2026/02/CT-guide0.pdf | 2026-11-11 |

Not yet confirmed: live treaty relief/interest-return form field numbering and full Schedule 6 exemption/return procedure. Specialist petroleum computations and foreign-jurisdiction consequences are out of scope, not assumed exempt.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `fk-cross-border-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/fk-cross-border-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
