---
name: bf-corporate-tax
description: Burkina Faso Corporate Tax (IS) Skill v1.0
jurisdiction: BF
domain: corporate-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# bf-corporate-tax

## Burkina Faso Corporate Tax (IS) Skill v1.0

> AI-drafted from official sources (DGI Burkina Faso consolidated CGI; servicepublic.gov.bf IS/IRVM fiches; Lois de Finances 2024–2025). Pending accountant verification. The CGI was renumbered across editions — article numbers are the weakest link; the rates/amounts are high-confidence. Confirm articles against the current consolidated CGI.

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Burkina Faso |
| Currency | FCFA (XOF) |
| Standard IS rate | 27.5% |
| Taxable-profit rounding | Fraction below 1,000 FCFA disregarded |
| Minimum tax (MFP) rate | 0.5% of turnover HT (rounded down to nearest 100,000 FCFA) |
| MFP floor — réel normal | 1,000,000 FCFA |
| MFP floor — réel simplifié | 300,000 FCFA |
| Subject to IS by right | SA, SARL (incl. single-member SAU), sociétés coopératives, non-resident companies with a BF permanent establishment |
| Subject to IS by option | SNC, SCS, sociétés en participation, sociétés de fait, GIE (else partners taxed at IR/IBICA) |
| Annual return / financial statements | By 30 April (insurance/reinsurance: 31 May) |
| Advance instalments (acomptes) | 3 instalments — 20 July, 20 October, 20 January; based on 75% of prior-year IS |
| Balance (solde) | Paid by the 30 April declaration deadline |
| IRCM/IRVM on dividends | 12.5% (6.25% for new companies, first 3 years) |
| IRCM/IRVM on bond interest | 6% |
| Late filing penalty | 10% of duties (25% on repeat); taxation d'office +100% after formal notice |
| Authority | Direction Générale des Impôts (DGI) |
| Primary legislation | CGI (Loi 058-2017/AN), as amended; Lois de Finances 2024–2025 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | June 2026 |

## Section 2 -- Rate, scope and minimum tax

- **Standard IS rate** — 27.5%
- **IS is greater of computed IS or MFP** — IS is the greater of computed IS (27.5% × profit) and the MFP (0.5% of turnover HT; floor 1,000,000 FCFA RNI / 300,000 FCFA RSI). New companies are exempt from MFP for the first year.
- **Entities subject to IS by right and by option** — Subject to IS by right: SA, SARL/SAU, cooperatives, other profit-making legal persons, and non-resident companies with a BF permanent establishment. SNC/SCS/sociétés de fait/GIE are taxed at IR on partners unless they elect IS (election by all partners within 3 months of the fiscal-year start; irrevocable).

## Section 3 -- Taxable base and key non-deductibles

- **Taxable base and deductibility of charges** — Assessed on profits from enterprises operated in Burkina Faso (plus treaty-attributed profits). Charges deductible if booked in the period, in the direct interest of the business, real and supported by documentation (CGI Art. 53).  _(CGI Art. 53)_
- **Non-deductible items and donation limit** — Non-deductible: fines/penalties/confiscations; excessive or fictitious remuneration to managing partners (excess reclassified as a distribution); non-qualifying provisions. Donations to recognised public-interest bodies deductible only within 3‰ of net turnover (gifts to the State deductible without limit if justified).
- **Donation deductibility limit** — 3‰ per mille of net turnover (Donations to recognised public-interest bodies deductible only within this limit; gifts to the State deductible without limit if justified)

## Section 4 -- Advance instalments and filing

- **Advance instalments schedule** — Three advance instalments (acomptes provisionnels) due 20 July (year N), 20 October (year N), 20 January (year N+1), computed from 75% of the prior closed year's IS (annualised if that year was not 12 months). The balance is paid by the 30 April declaration deadline.
- **Annual return filing deadline** — Annual return / états financiers filed by 30 April (insurance/reinsurance 31 May).

## Section 5 -- Withholding on distributions (IRCM / IRVM)

- **IRCM/IRVM on dividends and distributions** — 12.5% (reduced to 6.25% for newly created companies during their first 3 fiscal years)
- **IRCM/IRVM on bond interest** — 6%
- **Scope of IRCM/IRVM** — Scope includes dividends, interest, capital reimbursements, and directors' tantièmes/jetons de présence.

## Section 6 -- Prohibitions

- **Prohibition: IS on non-electing sole proprietor/SNC/SCS/GIE** — NEVER apply IS to a sole proprietor or to an SNC/SCS/GIE that has not elected IS — those use IR/IBICA (see bf-income-tax).
- **Prohibition: IS below MFP floor** — NEVER report IS below the MFP floor.
- **Prohibition: skipping acomptes** — NEVER skip the three acomptes (20 July / 20 Oct / 20 Jan).
- **Prohibition: engine computing numbers** — NEVER compute numbers — the engine handles arithmetic.
- **Confirmation requirement** — Confirm every article number and the acompte dates against the current consolidated CGI before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
