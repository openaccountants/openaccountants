---
name: th-top-up-tax
description: "Thailand top-up tax (global minimum tax) for multinational groups, periods from 1 January 2025: the EUR 750 million two-of-four-years test, excluded entities and the August 2026 Royal Decree, the notification, GloBE Information Return and top-up tax return due 15 months after the parent's year end (18 months for the first period), foreign GIR filing, instalments and refunds, from the Emergency Decree on Top-up Tax B.E. 2567."
version: 1.0
jurisdiction: TH
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
---

# Thailand top-up tax for multinational groups

> **General reference only.** Source-cited draft, not reviewed by an accountant. Written by Ryan Duguid on his fork (ryanduguid/openaccountants) and brought to the standard here. Do not use it to file without professional review.

## Who this applies to

Thai constituent entities of multinational groups whose ultimate parent's consolidated financial statements show revenue of at least the Thai-currency equivalent of EUR 750 million in at least two of the four accounting periods immediately before the period under review (Emergency Decree on Top-up Tax B.E. 2567 (2024), ss 2 and 26). The Decree was published in the Royal Gazette on 26 December 2024 and applies to accounting periods beginning on or after 1 January 2025. Prorate the threshold for a period that is not 12 months; check the special rules for group restructurings. Ordinary corporate income tax is in [corporate income tax](th-corporate-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Group revenue test | At least €750 million in the ultimate parent's consolidated statements, in at least two of the four preceding accounting periods | 2026 | https://www.rd.go.th/fileadmin/user_upload/news/2567eng/englishnews_6_2025.pdf |
| First periods in scope | Accounting periods commencing on or after 1st January 2025 | 2026 | https://www.rd.go.th/fileadmin/user_upload/news/2567eng/englishnews_6_2025.pdf |
| Rate | The globally agreed minimum rate (GloBE) | 2026 | https://www.rd.go.th/fileadmin/user_upload/news/2567eng/englishnews_6_2025.pdf |

## The base

The top-up tax is computed under the GloBE method in the Decree and its secondary legislation. On 30 December 2025 the Cabinet approved in principle four draft instruments: restructured groups (Royal Decree), entities that are not constituent entities, UTPR allocation where no Thai entity has GloBE income, and the adjustments to income, expenses and covered taxes including the Thai domestic top-up tax (Revenue Department News No. 5/2026). Check each one's later publication before computing.

Excluded entities: s 27 lists categories subject to qualifying conditions, including government entities, pension funds and investment funds that are ultimate parents. The Royal Decree on entities that are not constituent entities under s 26, B.E. 2569 (2026), published 7 August 2026 and in force from 8 August 2026 (s 2), excludes entities owned by entities with the characteristics announced under s 27(1) to (6), but not where the owner is a pension services entity (ss 3 and 4). It applies to accounting periods beginning on or after 1 January 2025 (s 5). Check the Director-General's announced characteristics and any election.

## Deadlines and filing

1. **Notification (s 54).** Information identifying the ultimate parent and the entity filing the GloBE Information Return, among other particulars, within 15 months of the last day of the ultimate parent's accounting period. One Thai constituent entity may file for the others if it names each delegating entity and its taxpayer identification number.
2. **GloBE Information Return (s 55).** Within 15 months of the last day of the ultimate parent's accounting period, with the same delegation rule.
3. **Foreign filing (s 56).** No Thai GIR is needed if the ultimate parent or its designated filing entity has filed the GIR in its own country and a competent authority agreement with Thailand for automatic exchange of GIR information is in effect for that period. The s 54 notification is still due.
4. **Top-up tax return and payment (s 57).** A Thai constituent entity with top-up tax payable files the return and pays within 15 months of the last day of the ultimate parent's accounting period. A joint venture or joint-venture subsidiary liable under s 52 uses the period end of the joint venture (or the joint venture treated as ultimate parent). An entity liable to pay may ask to pay in instalments within three years, under criteria a Royal Decree sets (s 57, third paragraph).
5. **First period (s 58).** For the first accounting period in which the group is within the charge, the s 54, s 55 and s 57 deadlines are extended to 18 months.

The Revenue Department files these electronically (News No. 6/2025); live forms and instructions are on its top-up tax pages (https://www.rd.go.th/68020.html).

## Penalties and interest

Refund of top-up tax overpaid: claim within three years after the last day of the filing deadline (s 59). Late filing and payment penalties under the Decree were not read for this guide.

## Cross-border points

The Decree reaches both Thai groups investing abroad and foreign groups investing in Thailand (News No. 6/2025). The foreign-filing exemption in s 56 depends on an exchange agreement being in effect for the period; Ryan Duguid reports a September 2026 Revenue Department announcement of Thailand's signature of the GIR exchange agreement, but signature alone does not show an effective relationship with a given country for a given period.

## Two worked examples that recompute

**1. Group with a 31 December 2025 year end, first period in scope.** The deadline is 18 months after 31 December 2025: 30 June 2027 (derived). The worked month count: December 2025 plus 18 months lands in June 2027.

```oa-check
name: Thailand top-up first period deadline
inputs:
  year: 2025
  month: 12
  extension_months: 18
steps:
  - month_index: year * 12 + month + extension_months
  - due_year: floor((month_index - 1) / 12)
  - due_month: month_index - due_year * 12
expected:
  due_year: 2027
  due_month: 6
```

**2. Same group, second period ending 31 December 2026.** Ordinary 15 months: 31 March 2028 (derived).

```oa-check
name: Thailand top-up ordinary deadline
inputs:
  year: 2026
  month: 12
  months: 15
steps:
  - month_index: year * 12 + month + months
  - due_year: floor((month_index - 1) / 12)
  - due_month: month_index - due_year * 12
expected:
  due_year: 2028
  due_month: 3
```

## Ask the client first

- Ultimate parent, its country and its accounting period end?
- Consolidated revenue for each of the last four periods?
- Is this the group's first period in scope?
- Has the parent filed the GIR at home, and is an exchange agreement with Thailand in effect for the period?
- Any joint ventures, restructurings or excluded entities in the Thai group?

## Sources

| Source | URL | Read on |
|---|---|---|
| Emergency Decree on Top-up Tax B.E. 2567 (2024), Royal Gazette vol 141 part 82 A, 26 December 2024, rendered pages 30 and 31 (Read for ss 54 to 59: 15 months, 18 months, instalments within three years, refunds) | https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/prk2567.pdf | 2026-11-14 |
| Royal Decree on entities that are not constituent entities under s 26, B.E. 2569 (2026), Royal Gazette vol 143 part 47 A, 7 August 2026, both pages (Read for ss 2 to 5) | https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dctut.pdf | 2026-11-14 |
| Revenue Department News No. 6/2025 (Read for EUR 750 million, two of four periods, 1 January 2025 start, electronic filing) | https://www.rd.go.th/fileadmin/user_upload/news/2567eng/englishnews_6_2025.pdf | 2026-11-14 |
| Revenue Department News No. 5/2026 (Read for the four draft instruments of 30 December 2025) | https://www.rd.go.th/fileadmin/user_upload/news/2568eng/englishnews_5_2026.pdf | 2026-11-14 |

Not yet confirmed: the publication and content of the four secondary instruments approved in principle on 30 December 2025; the Royal Decree on instalments under s 57; Director-General forms and filing procedures; the s 27 list as Ryan Duguid read it (rendered page 14 not reopened here); the September 2026 signature announcement (not reopened); which countries have an exchange agreement in effect for a given period; late filing and payment penalties.
