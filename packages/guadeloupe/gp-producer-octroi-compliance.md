---
name: gp-producer-octroi-compliance
description: >
  Guadeloupe internal octroi de mer for local producers, 2026. Covers who is liable (independent production activity with prior-year production turnover of at least 550,000 euros, excluding VAT and octroi), what counts as production (manufacture, transformation with a change of SH4 tariff heading, renovation, extraction, agriculture), aggregation across the five DROM, proration for a start-up year, liability from 1 January after the threshold year, identification with customs before 31 January, and quarterly electronic returns and payment by the 24th of the following month. Product rates, local exemptions and deductions are out of scope. Trigger phrases include octroi de mer interne Guadeloupe, seuil 550 000 euros, producteur octroi de mer, declaration trimestrielle octroi de mer.
version: "1.0"
jurisdiction: GP
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
---

# Guadeloupe: producer octroi de mer threshold and compliance v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Year: 2026. Law: Loi n. 2004-639 of 2 July 2004 on octroi de mer, article 2 as amended by Loi n. 2026-103 of 19 February 2026 (art. 99), in force since 21 February 2026 ([Loi 2004-639, Legifrance](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/)). Guidance: the customs circular of 10 July 2025 ([Circulaire octroi de mer, douane.gouv.fr](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf)). Amounts in euros.

## Who this applies to

This Guide concerns **internal octroi on goods produced**, not an exemption from import octroi. Article 2 of Law 2004-639, in its version effective 21 February 2026, covers independent production activities with prior-calendar-year production turnover **at least €550,000**, regardless of legal form or treatment under other taxes. The threshold excludes VAT and octroi and is prorated for a business starting during the reference year. [Law, article 2](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/).

Production includes manufacture, transformation or renovation of movable goods, extractive activities, and agricultural activities as defined by Rural Code article L311-1 in the amended provision. Establish classification before measuring turnover. This Guide does not resolve a disputed production classification. [Law, article 2](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/).

From 21 February 2026 article 2 also defines a transformation: the transformed good falls under a different tariff heading at the four-digit "SH 4" level of the Combined Nomenclature than the goods used to make it ([Loi 2004-639, art. 2](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/)).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Producer threshold | prior calendar year production turnover of 550,000 euros or more | Excluding VAT and octroi; equality counts | 2026 | [Loi 2004-639, art. 2](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/) |
| Start-up proration | threshold x months of activity / 12 | Business that started during the reference year | 2026 | same |
| Liability start | 1 January following the year the threshold is reached | Aggregate production across the five DROM | 2026 | [Circulaire 10 July 2025, paras. 16 to 19](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |
| Identification with customs | before 31 January of the following year | Previous year's production turnover with a commodity-code breakdown | 2026 | [Circulaire 10 July 2025, paras. 102 to 103](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |
| Quarterly return and payment | by the 24th of the month after each calendar quarter | Electronic from 1 July 2024; Q4 return reports annual production turnover | 2026 | [Circulaire 10 July 2025, decree 2015-1077 art. 7](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |

## The base

Prepare a reconciliation of production sales, resale and services. Customs paragraphs 16–19 distinguish production turnover from overall turnover and aggregate production sold across the five DROM, including principal and secondary establishments. They describe liability beginning on **1 January following the year the threshold is reached**. Do not allocate the threshold separately to each establishment. [July 2025 circular, printed pages 12–13](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

Checks before deciding:

- Test equality, not only amounts above €550,000.
- Separate the threshold decision from the applicable Guadeloupe product rate, exemption and deduction decisions.
- Distinguish ordinary resale from the taxpayer's own production.
- Do not treat absence of sales as automatic permission to omit a quarterly return.
- Use the [Martinique–Guadeloupe movement Guide](../martinique/mq-antilles-goods-movements.md) for qualifying inter-island movements, which have separate reporting rules.

## Deadlines and filing

The circular directs identification evidence to customs **before 31 January of the following year**, although liability starts on 1 January. It requires the previous year's production turnover and its commodity-code breakdown, with separate identification rules for establishments in different DROM. [Circular paragraphs 102–103, pages 44–45](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

Decree 2015-1077 article 7, reproduced in the circular's legislative annex, requires a **quarterly electronic return by the 24th of the following month**, with payment sent concurrently to the regional customs collection office; the final-quarter return reports annual production turnover. The electronic obligation applies from 1 July 2024. The circular requires a return even in a quarter without sales. [Decree article 7 and circular paragraphs 104–106](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

Operationally, reconcile the sales ledger to the return, separating product codes, rates and exports. Retain the accepted submission and payment evidence. Check the current customs portal and any specific extension before filing; this Guide does not specify an unverified filing-screen workflow.

For 2026 quarters the deadlines are 24 April, 24 July and 24 October 2026 and 24 January 2027, subject to any extension customs announces.

## Penalties and interest

Penalties for late identification or returns are not covered here: see "Not yet confirmed".

## Cross-border points

- Martinique and Guadeloupe form the single "marche unique antillais" for octroi (art. 1 II of the law); movements between them are in `mq-antilles-goods-movements` ([Loi 2004-639, art. 1](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/)).
- Production in all five DROM is aggregated for the threshold (circular paragraphs 16 to 19).
- Import octroi is a separate charge, not covered here.

## Two worked examples that recompute

For a full reference year, after classification and aggregation:

| Production turnover | Other business turnover | Threshold result |
|---|---:|---|
| €549,999 | €300,000 services | Below threshold; adding unrelated services would be incorrect |
| €550,000 | None | Threshold reached; equality counts |
| €600,000 | €50,000 resale | Threshold exceeded |

For a six-month start-up reference period, the circular's method gives €550,000 × 6/12 = **€275,000**. Production sales of €280,000 exceed that prorated threshold. These examples illustrate eligibility only; they do not calculate tax payable or establish an exemption. [Article 2](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/); [circular paragraph 19](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

**Case 1: equality counts.** Production turnover of exactly 550,000 euros in 2025, plus 300,000 of services: the business is liable from 1 January 2026, identifies before 31 January 2026 and files quarterly. Production of 549,999 with the same services is below the threshold; the services are not added.

```oa-check
name: Guadeloupe octroi producer threshold
inputs:
  threshold: 550000
  production_a: 550000
  production_b: 549999
  services: 300000
steps:
  - margin_a: production_a - threshold
  - margin_b: production_b - threshold
  - wrong_total_b: production_b + services - threshold
expected:
  margin_a: 0
  margin_b: -1
  wrong_total_b: 299999
```

**Case 2: decision for a business that started on 1 July of the reference year.** Prorated threshold 550,000 x 6/12 = 275,000. Production of 280,000 exceeds it by 5,000, so the business is liable from 1 January of the next year; with 270,000 it would not be.

```oa-check
name: Guadeloupe octroi prorated threshold, six months
inputs:
  months: 6
  production: 280000
steps:
  - prorated_threshold: 550000 * months / 12
  - excess: production - prorated_threshold
expected:
  prorated_threshold: 275000.00
  excess: 5000.00
```

## Ask the client first

1. What does the business do: production (manufacture, transformation with a heading change, renovation, extraction, agriculture), resale or services?
2. Production turnover for the previous calendar year, excluding VAT and octroi, across all DROM establishments.
3. When did activity start (proration)?
4. Is the business already identified with customs?
5. Which products and commodity codes, and any exports?

## Sources

| Source | URL | Read on |
|---|---|---|
| Loi n. 2004-639 du 2 juillet 2004 relative a l'octroi de mer, Legifrance, version in force on 14 November 2026: read for art. 1 II (single Antilles market) and art. 2 (550,000 euro threshold, production, transformation, proration; amended by Loi 2026-103) | https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/ | 2026-11-14 |
| Direction generale des douanes, circulaire octroi de mer of 10 July 2025: read for paras. 16 to 19, 102 to 106 and the decree 2015-1077 art. 7 annex (aggregation, 1 January start, 31 January identification, quarterly returns by the 24th, electronic filing) | https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf | 2026-11-14 |

Not yet confirmed: Guadeloupe product rates, exemptions and deductions; penalties; whether the July 2025 circular has been updated for the February 2026 amendment; the current customs filing portal steps.
