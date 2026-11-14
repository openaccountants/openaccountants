---
name: ms-investment-incentives
description: >
  Montserrat tax incentives in force in 2026: the Fiscal Incentives Act, Cap. 15.04
  (income tax holidays for approved manufacturing and processing enterprises of up to
  15 years for Group I and enclave enterprises, 12 for Group II and 10 for Group III,
  plus conditional customs relief), the Hotels Aid Act, Cap. 15.16 (duty relief or
  refund within two years on licensed hotel construction and equipment), the hotel
  income exemption for five years of assessment in Cap. 17.01 s.10, and relief for
  registered micro and small businesses under Cap. 15.05 (Form 6, by order, five years
  of income tax relief unless Cabinet approves longer). Trigger phrases include
  Montserrat tax holiday, Montserrat fiscal incentives, hotels aid Montserrat, micro and
  small business relief Montserrat.
version: 1.0
jurisdiction: MS
tax_year: 2026
tax_year_notes: "Acts current at their latest revisions: Cap. 15.04 at 1 January 2013, Cap. 15.16 and Cap. 15.05 at 1 January 2019, Cap. 17.01 at 1 January 2025."
last_updated: 2026-11-14
category: tax-optimization
type: situation-rules
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Montserrat investment incentives

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Statutory incentive regimes a Montserrat business may hold in 2026. Each depends on a grant (an order, licence or approval); this skill says what each regime can give and what the grant must show. Company tax at the ordinary 30% rate and the company-specific rate orders: [ms-corporate-income-tax](ms-corporate-income-tax.md). Import charges: [ms-customs-consumption-tax-hotels-tax](ms-customs-consumption-tax-hotels-tax.md). The international business and economic substance regimes are outside it.

## Ask the client first

1. Which grant does the business hold or want: an approved product and enterprise order, a hotels aid licence, a hotel approval under Cap. 17.01 s.10, a micro and small business relief order?
2. The dates: construction day, production day, completion of the hotel or extension.
3. The enterprise group (I, II, III or enclave) and the local-value-added figures behind it.
4. Which taxes the grant covers (income tax, customs duty, consumption tax, stamp duty).
5. Is the business registered and compliant (for micro and small business relief)?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Fiscal incentives, Group I or enclave enterprise, Schedule II | Income tax relief for up to fifteen years (in words on the page) from the production day | [Fiscal Incentives Act, Cap. 15.04, ss.7 to 12 and Schedule II](https://www.gov.ms/wp-content/uploads/2026/02/15.04-Fiscal-Incentives-Act.pdf) |
| Group II enterprise | Up to twelve years (in words on the page) | same |
| Group III enterprise | Up to ten years (in words on the page) | same |
| Hotels aid refund, Cap. 15.16 s.5 | Claim repayment of qualifying duty within two years of payment (in words on the page) | [Hotels Aid Act, Cap. 15.16, ss.2 to 8](https://www.gov.ms/wp-content/uploads/2026/02/15.16-Hotels-Aid-Act.pdf) |
| Hotel income exemption, Cap. 17.01 s.10 | Exempt in each of the five years of assessment after the year the hotel or extension is completed (in words on the page); dividends paid from it exempt; then set-off of capital expenditure in any five of the next eight years | [Income and Corporation Tax Act, Cap. 17.01, ss.10 to 12](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf) |
| Micro and small business income tax relief, Cap. 15.05 | Five years unless Cabinet approves longer (in words on the page) | [Micro and Small Business Act, Cap. 15.05, ss.14 to 17 and 20](https://www.gov.ms/wp-content/uploads/2026/02/15.05-Micro-and-Small-Business-Act.pdf) |
| Micro and small business accounts, s.17 | Financial statements and records within three months of the year end unless the Registrar allows longer (in words on the page) | same |

### Who is in and who is out

- **Fiscal incentives.** Products and enterprises are approved by published order. The group follows the statutory local-value-added calculation, or the enclave criteria. "Industry" covers manufacturing and processing and excludes agriculture and tourism. Section 12 allows complete or partial relief on profits from selling the approved product from the production day. Section 7 gives a separate import licence and conditional customs relief on qualifying goods from outside the Common Market; enclave enterprises are excluded from s.7. Sections 8 and 9: records and restrictions on disposal.
- **Hotels aid.** Licences for qualifying construction or equipping of a hotel or extension; a hotel needs six or more bedrooms. The licence lists the materials or equipment and the conditions. The regulations have separate applications for construction and initial equipping (reg.3). The licensee shows the licence to Customs for duty relief, or claims a refund within two years. Section 6: local purchase relief; ss.7 and 8: use and disposal restrictions.
- **Hotel income relief.** Needs Governor-in-Cabinet approval and a hotels aid licence; s.12 keeps return and accounts obligations. Hotels tax and consumption tax are separate.
- **Micro and small business.** A registered business applies on Form 6 for relief from customs duty and consumption tax, income tax or stamp duty. The Governor grants it by order on Cabinet advice if the socio-economic benefit test is met. Present the order by the tax or duty due date; meet the registration, compliance and disqualification rules. Section 20: revocation and recovery of relief.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Grant silent on a tax | No relief for that tax; read the order | [Cap. 15.04](https://www.gov.ms/wp-content/uploads/2026/02/15.04-Fiscal-Incentives-Act.pdf) |
| Enclave enterprise importing | No s.7 customs relief | same |
| Agriculture or tourism business | Not "industry" under Cap. 15.04; look at Hotels Aid or micro and small business relief | same |
| Micro and small business relief revoked | Relief may be recovered (s.20) | [Cap. 15.05](https://www.gov.ms/wp-content/uploads/2026/02/15.05-Micro-and-Small-Business-Act.pdf) |
| Business Progressive Fund borrower | Separate import concession (SRO 33/2026) | [ms-customs-consumption-tax-hotels-tax](ms-customs-consumption-tax-hotels-tax.md) |

## Worked cases

### Case 1: how long does a Group II holiday run?

Production day in 2026; Group II maximum twelve years. If the order grants the maximum, the last year of relief is 2037 (derived).

```oa-check
name: Montserrat Group II holiday from a 2026 production day
inputs:
  start: 2026
  years: 12
steps:
  - last_year: start + years - 1
expected:
  last_year: 2037
```

### Case 2 (decision): finish the hotel extension in December 2026 or January 2027?

The s.10 exemption runs for the five years of assessment after the year of assessment in which the work is completed. Completed in 2026: exempt 2027 to 2031. Completed in January 2027: exempt 2028 to 2032. Finishing in 2026 starts the exemption a year earlier; finishing in 2027 pushes it a year later. Which is better depends on when the hotel expects profits.

```oa-check
name: Montserrat hotel exemption, completion 2026 vs 2027
inputs:
  done_a: 2026
  done_b: 2027
steps:
  - first_a: done_a + 1
  - last_a: done_a + 5
  - first_b: done_b + 1
  - last_b: done_b + 5
expected:
  first_a: 2027
  last_a: 2031
  first_b: 2028
  last_b: 2032
```

## When to refuse or refer

- Applications and negotiation of grants.
- Group classification (the local-value-added calculation).
- International business companies and economic substance.
- Later legislation or sector-specific orders not listed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Incentives Act Cap. 15.04, revised to 1 January 2013: read for ss.2 to 12 and Schedule II (fifteen, twelve, ten and fifteen years) | https://www.gov.ms/wp-content/uploads/2026/02/15.04-Fiscal-Incentives-Act.pdf | 2026-11-14 |
| Hotels Aid Act Cap. 15.16 and Regulations, revised to 1 January 2019: read for ss.2 to 8 (licence, refund within two years) and reg.3 | https://www.gov.ms/wp-content/uploads/2026/02/15.16-Hotels-Aid-Act.pdf | 2026-11-14 |
| Income and Corporation Tax Act Cap. 17.01, revised to 1 January 2025: read for ss.10 to 12 (hotel relief) | https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf | 2026-11-14 |
| Micro and Small Business Act Cap. 15.05, revised to 1 January 2019: read for ss.14 to 17, 20 and Schedule 1 (Form 6, five years, three months) | https://www.gov.ms/wp-content/uploads/2026/02/15.05-Micro-and-Small-Business-Act.pdf | 2026-11-14 |

Not yet confirmed: amendments after each revision date; current application procedures and actual grants; sector-specific measures.
