---
name: us-cfc-gilti
description: "US anti-deferral rules for US persons owning foreign corporations: Controlled Foreign Corporation status (IRC §957/§951(b)), Subpart F income (§951/§952), GILTI (§951A) and the §250 deduction, the §962 election to be taxed at corporate rates with deemed-paid credits, the high-tax exception, and Form 5471 filing. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
version: 0.1
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
depends_on:
  - cross-border-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US CFC GILTI

## US Anti-Deferral — CFC, Subpart F & GILTI v0.1

## What this file is

This is a **topic content skill** that loads on top of `cross-border-tax-workflow-base`. It assumes the cross-border router has already run, confirmed the taxpayer is a **US person** (citizen, green-card holder, or resident alien), and established that the taxpayer holds an interest in a **foreign corporation**. If that triage has not happened, stop and run the base workflow first.

It produces two artifacts for a licensed accountant:

1. A **working paper** — the CFC determination, inclusion computations, and Form 5471 category mapping.
2. A **reviewer brief** — the elections taken or declined, the audit flash points, and the open facts a credentialed preparer must confirm.

It does **not** file anything and is **not** advice. Subpart F, GILTI, and Form 5471 are among the most complex provisions in the Code; every output below is a draft for human sign-off.

## Layer A — Reference layer

### A.1 CFC determination decision tree

- **Step 1 — foreign corporation classification** — Check the entity's default classification and any check-the-box election (Form 8832). A foreign eligible entity may be a corporation, partnership, or disregarded entity — only a *corporation* triggers CFC rules. (If it is a partnership/disregarded entity, this file does not apply.)  _(Form 8832)_
- **United States shareholder** — A US person is a United States shareholder if it owns ≥ 10% of the foreign corporation measured by vote OR value. Ownership is tested under §958.  _(§951(b))_
- **CFC ownership threshold** — more than 50% percent of vote or value (United States shareholders together, on any day of the tax year; small shareholders below 10% do not count toward the >50% test)  _(§957)_
- **Inclusion eligibility after CFC status** — Only persons who are United States shareholders and own stock directly or indirectly under §958(a) on the last day of the year the corporation is a CFC pick up Subpart F (§951(a)) and GILTI (§951A) inclusions. Constructive-only owners count for status but generally not for the inclusion amount.  _(§958(a); §951(a); §951A)_

⚑ AUDIT FLASH POINT — Constructive ownership under §958 routinely makes a corporation a CFC when no single client "feels" like a controller. Attribution runs through family, partnerships, estates, trusts, and corporations, and downward attribution rules can pull in stock held by related foreign persons. A founder who owns 9% directly but is attributed family or entity stock can cross both the 10% and >50% thresholds. Map the full §958 attribution chain before concluding "not a CFC."

### A.2 Ownership measurement (§958)

- **§958(a) — direct and indirect** — Stock owned directly, plus stock owned through foreign entities (proportionate). This is the ownership that drives the inclusion amount.  _(§958(a))_
- **§958(b) — constructive** — §318-style attribution (with modifications). This is used to determine United States shareholder and CFC status, not the dollar inclusion.  _(§958(b))_
- **Documentation requirement** — Always document both the §958(a) chain (for math) and the §958(b) chain (for status) separately.  _(§958)_

### A.3 Subpart F vs GILTI categorization

- **Foreign personal holding company income** — Passive-type: dividends, interest, rents, royalties, annuities, net gains from property producing such income, certain currency/commodity gains.  _(§952)_
- **Foreign base company sales and services income** — Certain related-party sales/services with a nexus outside the CFC's country.  _(§952)_
- **Insurance income and other categories** — Insurance income and certain other categories subject to the de minimis / full-inclusion tests and the earnings & profits limitation of §952 — confirm current thresholds.  _(§952)_
- **Subpart F taxed currently** — Subpart F income (§952) is taxed currently under §951(a).  _(§951(a); §952)_
- **GILTI computation** — GILTI = net CFC tested income less a net deemed tangible income return (10% of QBAI — qualified business asset investment — reduced by certain interest expense). Tested income excludes amounts already taxed as Subpart F, ECI, high-tax-excepted income, and related-party dividends. Confirm the current QBAI return percentage and any statutory changes for the filing year.  _(§951A)_
- **Order of operations** — Subpart F is computed and removed first; GILTI sweeps up most of what remains. Confirm current-year interaction rules.  _(§951A; §952)_

### A.4 The §250 deduction

- **§250 deduction on GILTI (historical)** — 50% percent of GILTI inclusion (historically; with a scheduled reduction and a taxable-income limitation — confirm the current-year §250 percentage, which changes by statute)  _(§250)_
- **§250 availability limitation** — The §250 deduction is available to C corporations. An individual US shareholder gets no §250 deduction on a direct GILTI inclusion unless the individual makes a §962 election.  _(§250; §962)_

⚑ AUDIT FLASH POINT — The individual-shareholder GILTI trap: without a §962 election, an individual reports the full GILTI inclusion at ordinary rates with no §250 deduction and no deemed-paid foreign tax credit, even if the CFC paid substantial foreign tax. This can produce US tax on income that was already heavily taxed abroad. Always model the §962 alternative for individuals.

### A.5 Foreign tax credits (§960)

- **Deemed-paid FTC availability** — A corporate US shareholder (or an individual who elects §962) may claim deemed-paid foreign tax credits under §960 for foreign taxes the CFC paid on Subpart F and GILTI inclusions, subject to GILTI-basket limitations and a current-year haircut on the GILTI deemed-paid credit. Confirm the current haircut percentage.  _(§960)_

### A.6 The §962 election

- **§962 election mechanics** — §962 lets an individual (or certain trusts/estates) US shareholder elect to be taxed on Subpart F and GILTI inclusions at corporate rates and to claim §960 deemed-paid credits as if a domestic corporation. It also opens the §250 deduction to the individual for the GILTI inclusion.  _(§962)_
- **Trade-off — two layers of tax** — Under §962, when the CFC later actually distributes the previously included earnings, the distribution is taxable again to the individual to the extent it exceeds the tax actually paid under the election. The election relieves the first-layer rate but defers a second layer of tax on distribution.  _(§962)_

⚑ AUDIT FLASH POINT — §962 second layer: flag that the election is most attractive for individuals with high-foreign-tax CFCs that retain earnings; it is far less attractive where near-term distributions are expected, because the actual distribution is taxed again (generally at the dividend rate, reduced by tax already paid). Model both the inclusion-year and the distribution-year consequences before recommending or declining.

### A.7 High-tax exclusion / exception

- **High-tax exclusion/exception mechanics** — GILTI high-tax exclusion and the Subpart F high-tax exception (§954(b)(4)) can exclude tested income / Subpart F income from inclusion when the foreign effective rate on that income exceeds a threshold tied to a percentage of the highest US corporate rate. Confirm the current threshold rate and the exact effective-tax-rate computation for the filing year.  _(§954(b)(4))_
- **Consistency requirement** — These are elections / determinations made by the CFC's controlling US shareholders and must be applied consistently across CFCs as required by the regulations.  _(§954(b)(4))_

⚑ AUDIT FLASH POINT — High-tax elections are all-or-nothing and consistency-bound within the rules, and once the high-tax exclusion applies the related foreign taxes are generally not creditable. Electing out of GILTI can be the wrong answer if it strands foreign tax credits. Document the rate test and model the FTC consequence before electing.

### A.8 Form 5471 — information return

- **Form 5471 purpose** — Form 5471, Information Return of US Persons With Respect to Certain Foreign Corporations, reports ownership of and transactions with foreign corporations. Filer categories (Categories 1–5, with sub-categories) determine which schedules are required; a single person may fall in multiple categories.  _(Form 5471)_
- **Category determination facts** — Determine the category from the facts: Officers/directors and acquisition/disposition events (Category 2/3), US shareholders of a CFC (Category 5), and related categories for §965/specified foreign corporations. Confirm the current-year category definitions and required schedules (e.g., Schedules I-1, J, P, and the GILTI/Subpart F supporting schedules), as these are revised frequently.  _(Form 5471; §965)_
- **Form 5471 penalty exposure** — $10,000-per-form, per-year penalty for late, incomplete, or non-filed returns, with continuation penalties after IRS notice (capped per the statute) and a potential reduction of foreign tax credits. A late or incomplete 5471 also keeps the entire return's statute of limitations open.  _(§6501(c)(8))_

⚑ AUDIT FLASH POINT — Form 5471 carries a $10,000-per-form, per-year penalty for late, incomplete, or non-filed returns, with continuation penalties after IRS notice (capped per the statute) and a potential reduction of foreign tax credits. A late or incomplete 5471 also keeps the entire return's statute of limitations open (§6501(c)(8)). Treat the 5471 as a hard filing deadline, not a soft attachment.

## Layer B — Executable layer

Run these steps to produce the working paper. Never finalize numbers without confirming current-year rates and thresholds.

### B.1 Inputs to collect

- **Inputs list** — Each US person's ownership: % by vote and % by value, direct (§958(a)) and constructive (§958(b)). The full §958 attribution map (family, entities, trusts). CFC financials: earnings & profits, income by category (passive vs active vs related-party), tested income, QBAI, foreign income taxes paid, and any actual distributions. Filing year and the taxpayer's other US income (for §250 limitation and rate modeling).  _(§958(a); §958(b); §250)_

### B.2 CFC + United States shareholder determination

0. **Determine US shareholder and CFC status** — For each US person, test the ≥10% vote-or-value United States shareholder threshold (§951(b)) using §958 ownership. Sum United States shareholders' ownership; test the >50% vote-or-value CFC threshold (§957). Record the result and the controlling shareholders. Output: a CFC-status table with the attribution chain cited to §958.

- **Step 1 — US shareholder test** — For each US person, test the ≥10% vote-or-value United States shareholder threshold (§951(b)) using §958 ownership.  _(§951(b); §958)_
- **Step 2 — CFC test** — Sum United States shareholders' ownership; test the >50% vote-or-value CFC threshold (§957).  _(§957)_
- **Step 3 — record result** — Record the result and the controlling shareholders. Output: a CFC-status table with the attribution chain cited to §958.  _(§958)_

### B.3 Inclusion computation

- **Step 1 — Subpart F** — Subpart F (§951/§952): categorize income, apply de minimis / full-inclusion tests and the E&P limitation, allocate to each §958(a) shareholder. Confirm current thresholds.  _(§951; §952)_
- **Step 2 — GILTI** — GILTI (§951A): at the shareholder level, compute net CFC tested income, subtract the net deemed tangible income return (QBAI × current %), arrive at GILTI.  _(§951A)_
- **Step 3 — high-tax exception** — Apply the high-tax exception / exclusion (A.7) if elected and supported; recompute.  _(§954(b)(4))_
- **Step 4 — §250 deduction** — Apply §250 only for corporate shareholders or §962 electors, at the current-year percentage.  _(§250; §962)_

### B.4 §962 vs no-election comparison (individuals)

Produce a side-by-side for each individual US shareholder:

**§962 vs no-election comparison**  _(§962; §11; §250; §960)_

| Line | No election | §962 election |
| --- | --- | --- |
| Rate on inclusion | individual ordinary rates | corporate rate (§11) |
| §250 deduction on GILTI | none | available (current %) |
| §960 deemed-paid FTC | none | available (GILTI haircut applies) |
| Tax on later actual distribution | already taxed; basis adjustments per PTEP | **second layer** — taxable above tax paid |

Recommend (as a draft for review) based on foreign tax rate of the CFC and expected distribution timing. Confirm all rates for the filing year.

### B.5 Form 5471 mapping

- **Form 5471 output requirements** — For each US person, output the category(ies) of filer, the required schedules, and a penalty-exposure note ($10k per form). Flag any prior-year missed filings for a delinquent-filing / reasonable-cause discussion with the credentialed reviewer.  _(Form 5471)_

### B.6 Cross-reference

- **Foreign trust coordination** — If a foreign trust holds the CFC stock, attribution under §958 runs through the trust and the trust itself may be the §958(a) owner. Coordinate with `us-foreign-trust-reporting` (Forms 3520 / 3520-A) — the same earnings can trigger both regimes.  _(§958(a))_

0. **Coordinate with foreign trust reporting** — Coordinate with us-foreign-trust-reporting (Forms 3520 / 3520-A) — the same earnings can trigger both regimes.

## Topic self-checks

- [ ] Confirmed the taxpayer is a US person and the entity is a *foreign corporation* (not a partnership/disregarded entity).
- [ ] Built **both** the §958(a) (math) and §958(b) (status) ownership chains, including family/entity/trust attribution.
- [ ] Applied the §951(b) ≥10% and §957 >50% (vote **or** value) tests and documented the result.
- [ ] Categorized income into Subpart F (§952) vs GILTI (§951A) before computing.
- [ ] Confirmed current-year figures: GILTI QBAI return %, §250 deduction %, §960 GILTI FTC haircut %, high-tax threshold rate, corporate rate.
- [ ] For individuals, modeled **both** the no-election and **§962** outcomes, including the **second-layer** distribution tax.
- [ ] Evaluated the GILTI / Subpart F **high-tax** election and its FTC consequence.
- [ ] Determined Form 5471 **category(ies)** and required schedules; flagged $10k penalty exposure and any prior missed filings.
- [ ] Cross-referenced `us-foreign-trust-reporting` if any CFC stock is held through a trust.
- [ ] Marked every rate/threshold as "confirm current-year" where not independently verified.
- [ ] Labeled output a draft working paper for licensed-accountant sign-off; no human sign-off claimed.

## Disclaimer

Provides computational and interpretive guidance on Subpart F / GILTI / Form 5471 only. Not tax advice and not a filed return. These are among the most complex provisions in the Code and turn on ownership and entity facts. Have outputs reviewed and signed by a qualified, licensed accountant before acting. Research-verified (tier 2) pending credentialed sign-off.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
