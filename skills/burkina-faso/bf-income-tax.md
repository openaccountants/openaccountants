---
name: bf-income-tax
description: Burkina Faso Income Tax (IBICA / IBNC) Skill v1.0
jurisdiction: BF
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burkina Faso Income Tax (IBICA / IBNC)

## Burkina Faso Income Tax (IBICA / IBNC) Skill v1.0

> AI-drafted from official sources (DGI Burkina Faso consolidated CGI 2023, Loi 058-2017/AN as amended by Loi 029-2022/ALT and Loi 035-2020/AN; Lois de Finances 2024–2025). Pending accountant verification. Confirm article numbers against the current consolidated CGI.

## Section 1 -- Quick reference

**Quick reference table**  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 13, 24-27, 39, 527, 529-536; Loi de finances 2025 checked for no identified changes to these articles](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_

| Field | Value |
| --- | --- |
| Country | Burkina Faso |
| Currency | FCFA (XOF) |
| Self-employed (commercial/industrial) tax | IBICA — Impôt sur les bénéfices industriels, commerciaux et agricoles |
| Freelancer / liberal profession tax | IBNC — Impôt sur les bénéfices des professions non commerciales |
| Bracket 1 | 10% on net profit 0 to 500,000 FCFA (CGI Art. 13) |
| Bracket 2 | 20% on 501,000 to 1,000,000 FCFA (CGI Art. 13) |
| Bracket 3 | 27.5% on profit over 1,000,000 FCFA (CGI Art. 13) |
| Profit rounding | Taxable profit rounded down to nearest 1,000 FCFA before brackets |
| Bracket method | Apply rates progressively by tranche/slice; do not apply the top rate to the whole profit |
| IBNC brackets | Identical 10% / 20% / 27.5% (CGI Art. 39) |
| CGA reduction | 30% reduction of the impôt sur les bénéfices for approved management-centre (centre de gestion agréé) members (Art. 14 / Art. 39-2) |
| Regime RNI | Turnover HT >= 50,000,000 FCFA (CGI Art. 527) |
| Regime RSI | Turnover HT 15,000,000 to < 50,000,000 FCFA (CGI Art. 529) |
| Regime CME | Turnover < 15,000,000 FCFA (CGI Art. 532–533) |
| Minimum tax (MFP) rate | 0.5% of turnover HT (CGI Art. 24) |
| MFP floor — RNI | 1,000,000 FCFA (CGI Art. 24) |
| MFP floor — RSI | 300,000 FCFA (CGI Art. 24) |
| MFP new-business exemption | Exempt from MFP for the first financial year (CGI Art. 27) |
| Annual return deadline (IBICA) | 30 April of the following year (CGI Art. 17) |
| IBNC payment deadline | Last day of February each year (CGI Art. 39-3, 40) |
| Late payment penalty | 10% of duties + interest 1% per month (CGI Art. 756) |
| Authority | Direction Générale des Impôts (DGI) |
| Primary legislation | CGI (Loi 058-2017/AN) Art. 5–84, 527–538; Lois de Finances 2024–2025 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | June 2026 |

## Section 2 -- Tax regimes (by annual turnover HT)

**Tax regimes table**  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 527, 529, 532-535](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_

| Regime | Turnover HT | Notes |
| --- | --- | --- |
| Réel Normal (RNI) | >= 50,000,000 FCFA | Full accounting; only RNI may invoice TVA |
| Réel Simplifié (RSI) | 15,000,000 to < 50,000,000 FCFA | Simplified accounting |
| CME (micro-entreprises) | < 15,000,000 FCFA | Lump-sum contribution; replaces IBICA/IS, MFP, TPA and patente |

- **Regime downgrade timing** — A taxpayer only moves down a regime after turnover stays below the threshold for 3 consecutive years  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 527 and 529](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **Regime upgrade election** — Election to opt up (CME→RSI→RNI) is made before 1 February, irrevocable for 3 years  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 530 and 535](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **Professions libérales excluded from CME** — Professions libérales are excluded from CME  _([DGI Burkina Faso, Code général des impôts 2023, Art. 534](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_

See [bf-tax-optimization](bf-tax-optimization).

## Section 3 -- Brackets and minimum tax

**Progressive brackets on net business profit (per-tranche method)**  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 13 and 39](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_

| Net profit (FCFA) | Rate |
| --- | --- |
| 0 to 500,000 | 10% |
| 501,000 to 1,000,000 | 20% |
| Over 1,000,000 | 27.5% |

- **Minimum Forfaitaire de Perception (MFP)** — 0.5% of turnover HT (rounded down to nearest 100,000 FCFA), never below 1,000,000 FCFA (RNI) or 300,000 FCFA (RSI)  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 23-24](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **MFP as floor** — The MFP is the floor — tax due is the greater of computed tax and MFP.  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 16 and 24](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **New enterprise MFP exemption** — New enterprises are exempt for their first year  _([DGI Burkina Faso, Code général des impôts 2023, Art. 27](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **CGA member MFP reduction** — CGA members get a 50% MFP reduction  _([DGI Burkina Faso, Code général des impôts 2023, Art. 25(2)](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **MFP payment instalments** — MFP paid in monthly (RNI) or quarterly (RSI) instalments  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 25-26](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_

## Section 4 -- CME (Contribution des Micro-Entreprises)

- **CME structure** — The CME is a flat annual lump sum (not a % of turnover) determined by class (turnover band) × geographic zone (A = Ouagadougou/Bobo-Dioulasso; B/C/D smaller localities)  _([DGI Burkina Faso, Code général des impôts 2023, Art. 536](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **CME replaces other taxes** — It replaces IBICA/IS, MFP, TPA and the patente  _([DGI Burkina Faso, Code général des impôts 2023, Art. 532](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_

Example top of grid (Zone A): Class 1 (turnover 13–15M) = 200,000 FCFA/yr; example bottom (Zone D): Class 8 (turnover <= 1.5M) = 2,000 FCFA/yr.

- **CME sub-regimes** — forfait (turnover < 5,000,000 FCFA) and déclaratif (5,000,000 to < 15,000,000 FCFA)  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 533-1 and 533-2](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **CGA member CME reduction** — CGA members get a 25% CME reduction  _([DGI Burkina Faso, Code général des impôts 2023, Art. 197](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_

## Section 5 -- Deductions and filing

- **Deductible charges conditions** — Charges deductible if booked in the period, incurred in the direct interest of the business, real and supported by sufficient documentation  _(CGI Art. 53)_
- **Head-office/technical-assistance fee deduction limit** — Head-office/technical-assistance fees deductible within 10% of overheads  _(Art. 62)_
- **IBICA annual return and payment deadline** — 30 April of the following year  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 15 and 17](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **IBNC deadline** — last day of February  _([DGI Burkina Faso, Code général des impôts 2023, Arts. 39(3) and 40](https://dgi.bf/wp-content/uploads/2023/10/CODE-GENERAL-DES-IMPOTS-2023-A-JOUR-AVEC-LA-LOI-DE-FINANCE-2023.pdf))_
- **Late/insufficient payment penalty** — 10% of duties + 1% per month interest  _(Art. 756)_
- **Late MFP obligations penalty** — 25% / 50%  _(Art. 758)_

## Section 6 -- Prohibitions

- **No personal/family allowances on business income** — NEVER apply personal/family allowances to business income — the brackets apply directly to net profit.
- **CME eligibility check** — NEVER place a taxpayer in CME if turnover >= 15,000,000 FCFA or if they are a profession libérale.
- **No TVA for RSI/CME** — NEVER let an RSI/CME taxpayer charge TVA.
- **No manual computation** — NEVER compute numbers — the engine handles arithmetic.
- **Confirm article numbers** — Confirm every article number against the current consolidated CGI before filing.

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
