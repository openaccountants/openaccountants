---
name: bf-vat
description: Burkina Faso VAT (TVA) Return Skill v1.0
jurisdiction: BF
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burkina Faso VAT (TVA)

## Burkina Faso VAT (TVA) Return Skill v1.0

AI-drafted from official sources (DGI Burkina Faso, Code Général des Impôts — Loi 058-2017/AN, Lois de Finances 2024–2026). Pending accountant verification. Article numbers vary across CGI editions — treat citations as indicative and confirm against the current consolidated CGI.

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Burkina Faso |
| Currency | FCFA (XOF) |
| Standard rate | 18% |
| Reduced rate | 10% on domestic air transport (transport aérien national), from 1 Jan 2025 |
| Exports | Exempt with right to deduct input TVA (zero-rated in effect) |
| Exempt supplies (without deduction) | Medicines/medical equipment; agricultural & livestock equipment; solar energy equipment; books, newspapers, periodicals; international air transport; medical consultations; approved education; water/electricity at social tariff (CGI Art. 307, 308) |
| Who may charge TVA | Only Régime du Réel Normal (RNI) taxpayers — annual turnover HT >= 50,000,000 FCFA |
| RSI / CME taxpayers | NOT authorised to invoice TVA (turnover < 50,000,000 FCFA) |
| Filing frequency | Monthly |
| Deadline | 15th of the month following the period |
| Return form | Déclaration de la Taxe sur la Valeur Ajoutée (DGI); e-filing via eSINTAX |
| Retenue à la source (VAT withholding) | 30% of the TVA (raised from 20%, effective 1 Jan 2026); withheld by DGE large enterprises, public accountants, exporters; creditable for the supplier |
| E-commerce | Platforms selling to BF residents liable to collect TVA (from 2025) |
| Late/insufficient payment penalty | 10% of TVA due + interest 1% per month of delay (CGI Art. 778) |
| Failure to file penalty | 25% of TVA due, minimum 50,000 FCFA (CGI Art. 777) |
| Authority | Direction Générale des Impôts (DGI) |
| Primary legislation | CGI (Loi 058-2017/AN) Art. 299–392; Lois de Finances 2024–2026 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | June 2026 |

## Section 2 -- Rates and scope

- **Standard rate scope** — 18% standard on taxable supplies of goods and services in Burkina Faso  _(CGI Art. 317)_
- **Reduced rate on domestic air transport** — 10% percent (Domestic air transport only (transport aérien national))  _(CGI Art. 317, 319-6; Loi de Finances 2025)_
- **Exports treatment** — Exempt with right to deduct (recover) input TVA — functions like zero-rating  _(CGI Art. 318)_
- **2026 rate change status** — The standard 18% / reduced 10% rates were unchanged by the 2026 Loi de Finances.

## Section 3 -- Exemptions (exonérations)

- **Exempt without deduction list** — Medicines and pharmaceutical/medical equipment; agricultural and livestock equipment; solar energy equipment; school/scientific publications, newsprint, newspapers and periodicals; purebred breeding animals; domestic poultry; international air transport; medical consultations; education in approved institutions; non-profit association services; water and electricity at the social (domestic) tariff.  _(CGI Art. 307, 308)_
- **Recent exemption additions** — Locally-produced frozen meat; aviation fuel/jet fuel; cement produced for export; certified electronic invoicing systems (2025); cattle/goats/sheep, shea & cashew nuts sold to local processors, fertile incubation eggs (2026).  _(Lois de Finances 2025–2026)_

## Section 4 -- Registration and tax regimes

TVA status follows the income-tax regime (turnover HT, all activities):

**Registration and tax regimes table**

| Regime | Turnover HT | TVA |
| --- | --- | --- |
| Réel Normal (RNI) | >= 50,000,000 FCFA | Charges & recovers TVA |
| Réel Simplifié (RSI) | 15,000,000 to < 50,000,000 FCFA | Cannot invoice TVA |
| Contribution des Micro-Entreprises (CME) | < 15,000,000 FCFA | Cannot invoice TVA |

Only RNI taxpayers are habilités to invoice TVA. See [bf-income-tax](bf-income-tax) and [bf-tax-optimization](bf-tax-optimization).

## Section 5 -- Retenue à la source (VAT withholding)

- **VAT withholding rate** — 30% percent (Withheld on TVA of supplier invoices by DGE large enterprises, public-order payers (comptables publics), and eligible exporters; raised from 20% effective 1 Jan 2026; withheld amount is an advance creditable on the supplier's own TVA return; does not change the 18%/10% rate itself)  _(CGI Art. 334 §4)_

## Section 6 -- Filing, deadlines, penalties

- **Filing frequency and deadline** — Monthly declaration and payment, no later than the 15th of the following month; e-filing via eSINTAX  _(CGI Art. 334)_
- **Late/insufficient/non-payment penalty** — 10% of TVA due plus interest 1% per month of delay  _(CGI Art. 778)_
- **Failure to file penalty** — 25% of TVA due, minimum 50,000 FCFA  _(CGI Art. 777)_

## Section 7 -- Prohibitions

- **Prohibition - RSI/CME charging TVA** — NEVER let an RSI or CME taxpayer (turnover < 50,000,000 FCFA) charge or recover TVA.
- **Prohibition - incorrect rate application** — NEVER apply any rate other than 18% (standard) or 10% (domestic air transport).
- **Prohibition - exempt supplies input recovery** — NEVER treat exempt-without-deduction supplies as recovering input TVA.
- **Prohibition: engine computing numbers** — NEVER compute numbers — the engine handles arithmetic.
- **Article confirmation requirement** — Confirm every article number against the current consolidated CGI before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
