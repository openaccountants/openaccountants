---
name: bf-tax-optimization
description: AI-drafted from official sources (DGI Burkina Faso CGI — régimes d'imposition, CGA reductions, MFP exemption). Pending accountant verification. LEGAL optimization only. Confirm thresholds and reductions against the current consolidated CGI.
jurisdiction: BF
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burkina Faso Tax Optimization

## Burkina Faso Tax Optimization Skill v1.0

> AI-drafted from official sources (DGI Burkina Faso CGI — régimes d'imposition, CGA reductions, MFP exemption). Pending accountant verification. LEGAL optimization only. Confirm thresholds and reductions against the current consolidated CGI.

## Section 1 -- Quick reference

**Quick reference table**  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_

| Field | Value |
| --- | --- |
| Country | Burkina Faso |
| Currency | FCFA (XOF) |
| Regime CME | Turnover < 15,000,000 FCFA — flat lump sum, no TVA, simplest |
| Regime RSI | 15,000,000 to < 50,000,000 FCFA — simplified accounting, cannot invoice TVA |
| Regime RNI | >= 50,000,000 FCFA — full accounting, must/may invoice TVA |
| CGA reduction — IBICA/IBNC | 30% reduction of the impôt sur les bénéfices |
| CGA reduction — MFP | 50% reduction of the minimum tax |
| CGA reduction — CME | 25% reduction of the contribution |
| CGA reduction — TPA base | 20% abatement |
| New-business MFP exemption | Exempt from MFP for the first financial year (CGI Art. 27) |
| Regime-option deadline | Before 1 February; irrevocable for 3 years |
| TVA invoicing | Only RNI may charge/recover TVA |
| Authority | Direction Générale des Impôts (DGI) |
| Primary legislation | CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | June 2026 |

## Section 2 -- Regime choice by turnover

**Regime choice by turnover**  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_

| Turnover HT | Regime | Tax basis | TVA |
| --- | --- | --- | --- |
| < 15,000,000 FCFA | CME | Flat lump sum (class × zone) | No |
| 15,000,000 to < 50,000,000 | RSI | Net profit, brackets 10/20/27.5%; MFP floor 300,000 | No |
| >= 50,000,000 | RNI | Net profit, brackets 10/20/27.5%; MFP floor 1,000,000 | Yes |

- **CME for smallest businesses** — CME for the smallest businesses is usually the lowest-admin, lowest-cost option below 15M FCFA — but it cannot recover input TVA or invoice TVA (a disadvantage when selling to TVA-registered customers who want recoverable input).  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_
- **Crossing 50M FCFA threshold** — Crossing 50M FCFA brings TVA obligations — model the cash-flow and pricing impact before growing past the threshold.  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_
- **Regime change timing** — A taxpayer only drops to a lower regime after staying below the threshold for 3 consecutive years; opting up is by election before 1 February, irrevocable 3 years.  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_

## Section 3 -- Centre de Gestion Agréé (CGA)

- **CGA reductions** — Joining an approved management centre yields statutory reductions: 30% off IBICA/IBNC, 50% off the MFP, 25% off the CME, and a 20% abatement on the TPA base. For profitable RNI/RSI businesses the 30% bénéfices reduction is typically the single largest legal lever.  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_

## Section 4 -- New-business and other levers

- **New-business MFP exemption** — New-business MFP exemption for the first financial year (CGI Art. 27) — time start-up investment accordingly.  _(CGI Art. 27)_
- **TVA-registration management** — TVA-registration management: only RNI invoices TVA; staying RSI/CME avoids TVA admin but blocks input recovery — choose based on customer mix (B2B TVA-registered vs B2C).  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_
- **Profession libérale regime** — Profession libérale → IBNC under RSI/RNI (excluded from CME).  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_

## Section 5 -- Prohibitions

- **No evasion advice** — NEVER advise evasion, under-declaration, or artificial turnover-splitting to stay under a threshold.  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_
- **No blind CME assumption** — NEVER assume CME is best without checking input-TVA recovery and customer mix.  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_
- **Prohibition: engine computing numbers** — NEVER compute numbers — the engine handles arithmetic.
- **Confirm current sources** — Confirm thresholds, reductions and option deadlines against current DGI sources.  _(CGI (Loi 058-2017/AN) Art. 13–27, 197, 527–538)_

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
