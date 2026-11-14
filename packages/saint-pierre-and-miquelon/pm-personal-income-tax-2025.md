---
name: pm-personal-income-tax-2025
description: >
  Saint-Pierre-et-Miquelon personal income tax for 2025 income declared in the 2026 campaign, under article 95 of the local tax code. Covers who is liable, household shares, the twelve-band schedule per share from 0% to 55%, worked one-share and two-share calculations, the 2026 deadlines (31 March paper, 30 April online for residents, 15 May for non-residents), foreign income disclosure, the departure inconsistency, and the youth reduction of article 103 octies (5,000 euros per household over five years, aged 25 or under) in force from 1 January 2026. Does not use mainland French bands. Trigger phrases include impot sur le revenu Saint-Pierre-et-Miquelon, bareme IR SPM 2026, declaration revenus 2025 SPM, reduction jeunes 103 octies.
version: "1.0"
jurisdiction: PM
tax_year: 2025
tax_year_notes: "2025-26: income earned in 2025, declared and assessed in the 2026 campaign"
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Saint-Pierre-et-Miquelon: 2025 personal income and 2026 filing v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year label: 2025-26, income earned in 2025 and declared in 2026, the latest table the territory has published. Law: Code local des impots, "a jour au 31 decembre 2025", read in the copy archived on 17 July 2026 because the official link now returns 404 ([Code local des impots, archived copy](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf)). Administration: Direction des services fiscaux. Amounts in euros.

## Who this applies to

Article 2 covers individuals domiciled in the territory and nonresidents receiving local-source income. It lists principal residence, principal place of stay, local professional activity and centre of economic interests as domicile criteria. It does not establish a universal 183-day safe harbour. Nonresident income categories, exceptions and any applicable treaty require separate analysis. [Code article 2](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf).

Tax is calculated by household. Articles 88–95 apply household shares to the taxable-income calculation: article 90 gives one share for a single, divorced or widowed person without dependent children, and two for a married or PACS couple without dependent children, subject to separate-assessment rules. Children, shared custody, disability and other circumstances alter the calculation and can introduce limits. Establish those facts before applying a table. [Code articles 6 and 88–95](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf).

This Guide concerns **2025 income reported in 2026**. The [local code, article 95](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) expressly identifies that income year and assessment year. Do not reuse this table for 2026 income without checking the later legislation.

## Rates, bands and thresholds

Per share of taxable income; article 95 applies "a compter de 2026, sur les revenus percus en 2025".

| Taxable income per share (euros) | Marginal rate | Conditions | Tax year | Source |
|---|---|---|---|---|
| Up to 10,140 | 0% | Per share | 2025-26 | [Code local des impots, art. 95 (archived)](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| 10,141 to 11,140 | 5% | same | 2025-26 | same |
| 11,141 to 12,110 | 10% | same | 2025-26 | same |
| 12,111 to 13,660 | 15% | same | 2025-26 | same |
| 13,661 to 16,960 | 20% | same | 2025-26 | same |
| 16,961 to 20,100 | 25% | same | 2025-26 | same |
| 20,101 to 23,400 | 30% | same | 2025-26 | same |
| 23,401 to 27,500 | 35% | same | 2025-26 | same |
| 27,501 to 40,500 | 40% | same | 2025-26 | same |
| 40,501 to 54,600 | 45% | same | 2025-26 | same |
| 54,601 to 68,300 | 50% | same | 2025-26 | same |
| Over 68,300 | 55% | same | 2025-26 | same |
| Youth reduction (art. 103 octies) | up to 5,000 euros per household over the first declaration year and the next four | Domiciled, aged 25 or under at 31 December; from 1 January 2026 | 2025-26 | [Deliberation 228/2025](https://www.services-fiscaux975.fr/files/file/DELIB/D%C3%A9lib%202025/DELIB2025-0228-%20article%20103%20octies-RI%20jeunes.pdf) |
| Paper return, residents | 31 March 2026 | | 2025-26 | [Notice IR 2025](https://www.services-fiscaux975.fr/files/file/Documentation/2026/Notice%20IR%202025-1.pdf) |
| Online return, residents | 30 April 2026 | | 2025-26 | same |
| Non-residents, paper or online | 15 May 2026 | Taxable local income | 2025-26 | same |

## The base

Apply each rate only to the slice in that band, not to the entire income. The schedule above is for taxable income per share after the applicable income-category rules and deductions; gross salary is not an interchangeable input. [Code articles 88–95](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf).

The notice expresses continuous band boundaries ([Notice IR 2025, page 4](https://www.services-fiscaux975.fr/files/file/Documentation/2026/Notice%20IR%202025-1.pdf)); the code prints whole-euro starts (10,141, 11,141 and so on). Treat the bands as continuous; do not create 1 euro gaps.

For one share and **EUR 30,000 taxable income**, the ordinary schedule produces:

`1,000 × 5% + 970 × 10% + 1,550 × 15% + 3,300 × 20% + 3,140 × 25% + 3,300 × 30% + 4,100 × 35% + 2,500 × 40% = EUR 5,249.50`.

That is the schedule calculation before any relevant reduction, credit or final assessment rounding. For an eligible two-share household with EUR 60,000 taxable income, the corresponding ordinary calculation is twice that amount, **EUR 10,499**, before those adjustments. These examples do not determine a particular taxpayer's final bill. Article 95 also contains a low-liability reduction and family-benefit limits with indexation; their printed historical amounts are not certified here as current operational thresholds. [Code articles 88–95](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf).

### Youth reduction

[Deliberation 228/2025](https://www.services-fiscaux975.fr/files/file/DELIB/D%C3%A9lib%202025/DELIB2025-0228-%20article%20103%20octies-RI%20jeunes.pdf), published 19 December 2025, inserted article 103 octies with effect from **1 January 2026**. It provides a **EUR 5,000 multi-year ceiling per household**, usable in the first declaration year and the next four years, for a locally domiciled taxpayer aged **25 or younger at 31 December of the taxation year**. It does not say EUR 5,000 per year or per person.

The administration's [2025 return notice, page 4](https://www.services-fiscaux975.fr/files/file/Documentation/2026/Notice%20IR%202025-1.pdf) applies this to the 2026 campaign for 2025 income and describes automatic application. Its example uses EUR 1,000 against 2025 income tax, leaving EUR 4,000 across 2026–2029 income years. This is the published administrative application of the January 2026 commencement, not a statement that the legislation commenced in January 2025.

The short enacted provision does not settle all cases involving an earlier first declaration, a change of household or ageing out during the five-year window. Those cases require clarification; do not infer a fresh five-year allowance whenever a taxpayer moves or forms a new household. [Deliberation 228/2025](https://www.services-fiscaux975.fr/files/file/DELIB/D%C3%A9lib%202025/DELIB2025-0228-%20article%20103%20octies-RI%20jeunes.pdf).

## Deadlines and filing

For the ordinary 2026 campaign:

| Return | Deadline |
|---|---|
| Resident, paper | 31 March 2026 |
| Resident, electronic | 30 April 2026 |
| Nonresident with taxable local income, paper or electronic | 15 May 2026 |

These dates are in [code article 81](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) and the [official notice, page 3](https://www.services-fiscaux975.fr/files/file/Documentation/2026/Notice%20IR%202025-1.pdf). They concern submission, not a promise that payment is due on the same day. For foreign income, article 81 also requires disclosure of specified exempt income taken into account in calculating tax on other income. A treaty exemption does not by itself remove every reporting obligation. [Code article 81](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf).

**Departure inconsistency:** the notice's departure section on page 7 refers to paper filing before 1 April, whereas article 81 and its page 3 table give nonresidents until 15 May for either channel. A departure-year filing should be checked with the authority against the specific facts and article 104; this Guide does not silently substitute one deadline for the other. [Code articles 81 and 104](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf); [notice pages 3 and 7](https://www.services-fiscaux975.fr/files/file/Documentation/2026/Notice%20IR%202025-1.pdf).

The Direction des services fiscaux calendar gives the same 30 April 2026 online date for residents and 15 May 2026 ([Calendrier fiscal](https://www.services-fiscaux975.fr/fr/2-calendrier-fiscal.html)).

## Penalties and interest

Late-filing penalties and interest are not covered by this skill: see "Not yet confirmed".

## Cross-border points

- Non-residents with local-source income file by 15 May 2026; treaty relief needs separate analysis ([Code local des impots, arts. 2 and 81 (archived)](https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf)).
- Specified exempt foreign income must still be disclosed when it is used to compute tax on other income (art. 81).

## Two worked examples that recompute

**Case 1: one share, taxable income 30,000 euros.** Band by band: 50 + 97 + 232.50 + 660 + 785 + 990 + 1,435 + 1,000 = 5,249.50, before reductions.

```oa-check
name: SPM 2025 income, one share, 30000
inputs:
  income: 30000
steps:
  - b5: (min(income, 11140) - 10140) * 0.05
  - b10: (min(income, 12110) - 11140) * 0.10
  - b15: (min(income, 13660) - 12110) * 0.15
  - b20: (min(income, 16960) - 13660) * 0.20
  - b25: (min(income, 20100) - 16960) * 0.25
  - b30: (min(income, 23400) - 20100) * 0.30
  - b35: (min(income, 27500) - 23400) * 0.35
  - b40: (min(income, 40500) - 27500) * 0.40
  - tax: b5 + b10 + b15 + b20 + b25 + b30 + b35 + b40
expected:
  tax: 5249.50
```

**Case 2: decision, the youth reduction across years.** A taxpayer aged 24 owes 1,000 euros on 2025 income (the notice's example). The reduction cancels it and leaves 4,000 of the 5,000 household ceiling for the next four income years; for a two-share household with 60,000 the schedule gives 2 x 5,249.50 = 10,499 before reductions.

```oa-check
name: SPM youth reduction and two shares
inputs:
  tax_2025: 1000
  ceiling: 5000
  one_share_tax: 5249.50
steps:
  - used: min(tax_2025, ceiling)
  - remaining: ceiling - used
  - two_share_tax: one_share_tax * 2
expected:
  used: 1000
  remaining: 4000
  two_share_tax: 10499.00
```

## Ask the client first

1. Domicile in the territory in 2025 (home, main stay, work, economic interests)?
2. Household: married or PACS, children and custody, disability (shares).
3. Taxable income by category after deductions, not gross salary.
4. Ages of the taxpayers (youth reduction) and first year of declaration.
5. Foreign income or a departure in 2025?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code local des impots de Saint-Pierre-et-Miquelon, updated to 31 December 2025, copy archived 17 July 2026 (the official link now returns 404): read for arts. 2, 6, 81, 88 to 95 and 104 | https://web.archive.org/web/20260717081247/https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf | 2026-11-14 |
| Direction des services fiscaux, Notice IR 2025 (2026 campaign): read for the deadlines on page 3, the schedule on page 4, the youth reduction example and the departure section on page 7 | https://www.services-fiscaux975.fr/files/file/Documentation/2026/Notice%20IR%202025-1.pdf | 2026-11-14 |
| Deliberation 228/2025 inserting art. 103 octies: read for the 5,000 euro household ceiling, the age test and the 1 January 2026 start | https://www.services-fiscaux975.fr/files/file/DELIB/D%C3%A9lib%202025/DELIB2025-0228-%20article%20103%20octies-RI%20jeunes.pdf | 2026-11-14 |
| Direction des services fiscaux, Calendrier fiscal: read for the 30 April and 15 May 2026 dates | https://www.services-fiscaux975.fr/fr/2-calendrier-fiscal.html | 2026-11-14 |

Not yet confirmed: the schedule for income earned in 2026 (not yet published; this skill carries the 2025-26 schedule); the current official link to the code; the indexed low-liability reduction and family-benefit limits; the departure-year deadline (page 7 of the notice says before 1 April on paper, article 81 gives non-residents 15 May); late-filing penalties; youth-reduction cases with a change of household.
