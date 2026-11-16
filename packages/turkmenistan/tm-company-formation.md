---
name: tm-company-formation
description: "Turkmenistan company formation, 2026: the seven enterprise forms (Law on Enterprises art. 24), minimum charter capital as multiples of the base value (25 sole, 50 co-operative, 100 economic company and joint venture, 200 joint-stock), half paid before registration, registration decision in three working days, documents, re-registration, joint-stock reporting, and foreign founders, under the Civil Code in force from 1 January 2026."
version: 1.1
jurisdiction: TM
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Turkmenistan company formation and entity choice

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to form a company without professional review.

## Who this applies to

Founders, Turkmen or foreign, setting up an enterprise in Turkmenistan. The new Civil Code entered into force on 1 January 2026 (commencement law No. 162-VII of 28 June 2025, arts 2 and 4, with transitional rules); it leaves creation of commercial legal entities to legislation, makes a legal entity exist on state registration, and lets a sole founder adopt a charter where one founder is allowed (arts 49 to 53). Branches and representative offices are units of the parent without legal personality (art. 56). Tax registration and the profit tax regimes are in [corporate income tax](tm-corporate-income-tax.md).

## Rates, bands and thresholds

| Form | Minimum charter capital | Tax year | Official URL |
|---|---|---|---|
| Sole (individual) enterprise | 25 times the base value for calculating taxes and fees | 2026 | https://mejlis.gov.tm/single-law/301?lang=ru |
| Co-operative enterprise | 50 times the base value | 2026 | https://mejlis.gov.tm/single-law/301?lang=ru |
| Joint venture | 100 times the base value | 2026 | https://mejlis.gov.tm/single-law/301?lang=ru |
| Enterprise of a public organisation | 100 times the base value | 2026 | https://mejlis.gov.tm/single-law/301?lang=ru |
| Economic company (hojalyk jemgyýeti) | 100 times the base value | 2026 | https://mejlis.gov.tm/single-law/301?lang=ru |
| Registration decision | Within three working days of the founders submitting the required documents (art. 16) | 2026 | https://mejlis.gov.tm/single-law/301?lang=ru |

Joint-stock companies: issued and placed shares of at least 200 times the base value (Joint-Stock Companies Law art. 12, as Ryan Duguid read it). The money value of the base value was not found in a primary source; use the multiples.

## The base

Not a tax. Forms (Law on Enterprises art. 24): state enterprise, sole enterprise, co-operative, joint venture, enterprise of a public organisation, economic company and joint-stock company; legislation may add others.

- **Sole enterprise** (art. 26): one natural person owns it, approves the charter and is fully liable with his or her property.
- **Economic company** (art. 29): at least two natural or legal persons under a founders' agreement; the general meeting is the highest body; liability either joint and several with all participants' property or limited to each contribution (art. 29(6)). This, not a generic "LLC", is the usual vehicle.
- **Joint-stock company** (Joint-Stock Companies Law arts 5 and 12): open or closed; at formation all shares go to founders; at least half the charter capital paid at registration and the rest within 12 months.
- **Contributions** (art. 47): at least half after signing the founding documents and before applying, the balance within one year of registration (joint-stock companies follow their own rule).

## Deadlines and filing

1. Sign the charter and, where required, the founders' agreement (not needed for a state enterprise or a single-founder enterprise, art. 12(2)); pay at least half the capital.
2. Apply to the Tax Directorate of the Ministry of Finance and Economy with the signed application (name, legal address, capital, founders), charter, founders' agreement and proof of the registration fee (arts 12, 15 to 17, 20). Electronic handling is allowed under a Ministry procedure (2021 amendment). The Cabinet of Ministers sets the fee.
3. The decision to register or refuse is due within three working days (art. 16); a refusal or a missed deadline can be appealed in court (art. 18).
4. Pay the balance of capital within one year.
5. Notify the registration authority within one week of amending founding documents; a change of name, owner, legal address, founders or form takes effect on re-registration (art. 21).
6. Joint-stock companies: keep accounts and file financial statements, appoint an auditor each year, have the board pre-approve the annual report at least 30 days before the AGM, publish the annual report, balance sheet and results, and keep the listed records (Joint-Stock Companies Law arts 56, 58 to 60).

## Penalties and interest

Not read for this guide.

## Cross-border points

Foreign individuals and legal entities can be founders (Law on Enterprises art. 11). Foreign investors choose the amount, composition and structure of capital within the law; check restrictions by activity and territory and any reciprocity measures (Law on Foreign Investments arts 8 and 12). Qualifying investment income, including dividends and profits, may be transferred abroad in foreign currency after taxes (art. 21); conditional customs relief (art. 9); tax relief is in the Tax Code (art. 10). Foreign-invested enterprises cannot use the SME 2% profit tax regime.

## Two worked examples that recompute

**1. Economic company with charter capital at the minimum, 100 base values.** At least 50 base values paid before applying, 50 within a year (derived).

```oa-check
name: Turkmenistan economic company capital split
inputs:
  capital_base_values: 100
steps:
  - before_registration: capital_base_values * 0.5
  - within_one_year: capital_base_values - before_registration
expected:
  before_registration: 50
  within_one_year: 50
```

**2. Joint-stock company versus sole enterprise minimums.** 200 against 25 base values: the joint-stock minimum is 8 times the sole-enterprise minimum (derived).

```oa-check
name: Turkmenistan JSC vs sole enterprise minimum
inputs:
  jsc: 200
  sole: 25
steps:
  - ratio: jsc / sole
expected:
  ratio: 8
```

## Ask the client first

- How many founders, and are any foreign?
- Which form, and what liability do the founders want?
- Planned activity and territory (restrictions, licences)?
- Intended charter capital?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on Enterprises, Russian text on the Mejlis site, arts 16, 26, 28 and 29 (Read for the capital multiples and the three-day decision) | https://mejlis.gov.tm/single-law/301?lang=ru | 2026-11-14 |
| Law on Enterprises, state-language text, arts 11, 12, 15 to 24, 26, 29, 47 (Read by Ryan Duguid) | https://mejlis.gov.tm/single-law/301?lang=tm | 2026-11-11 |
| Civil Code and its commencement law, arts 49 to 53 and 56 (Read by Ryan Duguid) | https://mejlis.gov.tm/single-code/6?lang=tm | 2026-11-11 |
| Joint-Stock Companies Law arts 5, 12, 56, 58 to 60 (Read by Ryan Duguid) | https://mejlis.gov.tm/single-law/308?lang=ru | 2026-11-11 |
| Law on Foreign Investments arts 8 to 10, 12 and 21 (Read by Ryan Duguid) | https://mejlis.gov.tm/single-law/265?lang=ru | 2026-11-11 |

Not yet confirmed: the money value of the base value; the registration fee; sector and reciprocity restrictions; joint-stock and foreign-investment text as Ryan Duguid read it (not reopened here). The old guide's figures (TMT 5,000 or USD 20,000 minimum capital, at least one director of any nationality, possible single-member LLC) came from private websites and are not in the Law on Enterprises.
