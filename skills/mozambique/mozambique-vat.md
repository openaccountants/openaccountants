---
name: mozambique-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mozambique VAT (IVA) return. ISPC simplified regime for small taxpayers. Portuguese-language terminology. ALWAYS read before handling Mozambique IVA work.
version: 2.1
jurisdiction: MZ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). The governing 2026 texts could not be read: Boletim da Republica I Serie n.o 248 of 29 Dec 2025 (Leis 9/2025 ISPC, 10/2025 IVA, 11/2025 IRPS, 12/2025 IRPC) is listed on the AT site, at.gov.mz and inss.gov.mz refused both direct fetch and a real browser on 2026-11-01, and the gazette files have no archive copy. Every row below that rests on an older text says so.

## Who this applies to

Taxable persons under the Codigo do IVA (Lei 32/2007, amended by Lei 10/2025 from 1 Jan 2026). Before 2026 small businesses could opt for ISPC, which excludes IVA, IRPC and IRPS. Megaprojects with negotiated regimes are out of scope.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official source |
|---|---|---|---|
| Standard IVA rate | unverified, old skill 16% | Lei 10/2025 not read | unverified |
| Reduced rate | unverified, old skill 5% for private health and education | same | unverified |
| Exports | unverified, old skill 0% | same | unverified |
| ISPC fixed tax | MZN 75,000 a year, pre-Lei 9/2025 | pre-2026 text | https://web.archive.org/web/20260309101834/https://www.at.gov.mz/por/Processos-Fiscais/Imposto-Simplificado-para-Pequenos-Contribuintes-ISPC |
| ISPC percentage option | 3% of turnover; 50% off in the first year, pre-Lei 9/2025 | pre-2026 text | same |
| ISPC turnover ceiling | MZN 2,500,000, pre-Lei 9/2025 | pre-2026 text | same |


## The base

Before 2026, a valid invoice is in Portuguese and meticais, dated, sequentially numbered, with buyer name, NUIT and address, quantity and description, net price, rate and amount of tax, and the reason where no tax applies (CIVA art. 27; https://web.archive.org/web/20250815104300/https://www.at.gov.mz/por/Perguntas-Frequentes2/IVA). IVA on travel abroad is not deductible, with the exception for commercial travellers' lodging and meals (CIVA art. 20(b), same page). ONGs bear IVA as a cost: CIVA exempts operations, not persons (same page). Services listed in CIVA art. 6(7) for a buyer established abroad are outside IVA (art. 6(8), same page).

### Supplier pattern library
**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BCI, BANCO COMERCIAL | EXCLUDE | Exempt financial |
| MILLENNIUM BIM | EXCLUDE | Same |
| STANDARD BANK MZ | EXCLUDE | Same |
| AT, AUTORIDADE TRIBUTARIA | EXCLUDE | Tax payment |
| ALFANDEGAS, CUSTOMS | Check for import IVA |  |
| INSS | EXCLUDE | Social security |
| EDM, ELECTRICIDADE | Domestic, standard rate | Electricity |
| FIPAG | Domestic, standard rate | Water |
| VODACOM MZ, TMCEL, MOVITEL | Domestic, standard rate | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidacao | Non-resident |

### Classification rules
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

- **Standard rate classification** , 16% standard. 5% reduced (private health/education). 0% exports. Exempt: basic foodstuffs, financial, medical (public), education (public), residential rental, public transport, agricultural inputs.
- **ISPC classification** , ISPC: 3% of gross turnover for businesses below MZN 2,500,000. No IVA charged, no input recovery.

### IVA return form
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

Output: Lines 1-8 (16% sales, exempt, exports, total, IVA liquidado, autoliquidacao, adjustments, total).

Input: Lines 9-14 (local, imports, autoliquidacao input, capital goods, exclusions, total deductible).

Net: Lines 15-17 (net, credit transitado, payable/credit).

### Reverse charge (autoliquidacao)
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

- **Non-resident services reverse charge** , Non-resident services: self-assess 16%. Net zero.

### Deductibility and blocked input
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

- **Blocked input VAT** , Blocked: vehicles < 9 seats, entertainment, personal use, fuel for blocked vehicles, invoices without NUIT.
- **Prorata deduction** , Prorata deduction rule applies.

### Edge cases, test suite, and escalation
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

Autoliquidacao 16%. Net zero.

Zero-rated. Input recoverable.

Exceeds MZN 2.5M: must register for IVA.

Escalate.

Rice/bread exempt. No output, no input recovery.

MZN 1M sale. IVA MZN 160K.

MZN 500K purchase + IVA 80K. Recoverable.

SA services MZN 3M. Output 480K, input 480K. Net zero.

Export MZN 50M. Zero-rated.

Entertainment. Blocked.

ISPC quarterly MZN 400K. ISPC = MZN 12K.

Out of scope: IRPC 32%, IRPS progressive 10%-32%, INSS employer 4% + employee 3%.

#### Prohibitions

- **Prohibitions list** , - NEVER confuse IVA with ISPC - NEVER allow ISPC taxpayers to charge IVA - NEVER apply standard rules to megaprojects without verification - NEVER accept invoices without NUIT - NEVER compute numbers -- engine handles arithmetic

## Deadlines and filing

Portal: e-Declaracao, https://edeclaracao.at.gov.mz/. Frequency, form boxes and due dates after Lei 10/2025 were not read; do not state them. See the return layout kept above as the old skill's outline, unverified.

## Penalties and interest

Late filing and payment figures were not read. The old skill's MZN 5,000 to 50,000 and 2% a month are unverified.

## Cross-border points

Reported, unread: digital services by non-residents taxed where the buyer is established in Mozambique. Old-skill rule, unverified: self-assess IVA on non-resident services, net zero if fully deductible.

## Two worked examples that recompute

**ISPC percentage on turnover of MZN 2,000,000.** 3% is MZN 60,000.

```oa-check
name: ISPC percentage
inputs:
  turnover: 2000000
steps:
  - tax: turnover * 0.03
expected:
  tax: 60000.00
```

**Decision: fixed or percentage ISPC.** On MZN 2,000,000 the percentage saves MZN 15,000 against the fixed MZN 75,000. The two meet at MZN 2,500,000. Pre-Lei 9/2025 figures.

```oa-check
name: ISPC fixed against percentage
inputs:
  turnover: 2000000
steps:
  - pct: turnover * 0.03
  - saving: 75000 - pct
expected:
  saving: 15000.00
```


## Ask the client first

- Turnover in the last 12 months.
- IVA or ISPC status and registration date.
- Sales of exempt supplies.
- Exports and foreign suppliers.
- Megaproject or special regime.

## Sources

| Source | URL | Read on |
|---|---|---|
| AT, ISPC Regulation, Decreto 14/2009 (archive copy of 9 Mar 2026; arts. 1 to 9 read) | https://web.archive.org/web/20260309101834/https://www.at.gov.mz/por/Processos-Fiscais/Imposto-Simplificado-para-Pequenos-Contribuintes-ISPC | 2026-11-01 |
| AT, Perguntas Frequentes ISPC (archive copy of 19 Jan 2026; whole page read) | https://web.archive.org/web/20260119123327/https://www.at.gov.mz/por/Perguntas-Frequentes2/ISPC | 2026-11-01 |
| AT, Perguntas Frequentes IVA (archive copy of 15 Aug 2025; whole page read) | https://web.archive.org/web/20250815104300/https://www.at.gov.mz/por/Perguntas-Frequentes2/IVA | 2026-11-01 |
| AT, Legislacao Fiscal list naming BR 248 supplements (archive copy of 20 Feb 2026; list read, the gazette files were not archived) | https://web.archive.org/web/20260220064207/https://www.at.gov.mz/por/Legislacao/Legislacao-Fiscal/Leis | 2026-11-01 |

Not yet confirmed: Law 10/2025 and Law 9/2025 texts, so all of these: rates; exemptions; registration threshold; abolition of the simplified and exemption regimes; filing frequency and deadlines; return lines; blocked input tax (old skill: vehicles under 9 seats, entertainment, personal use, invoices without NUIT, arts. 20 to 22); prorata (art. 19); reverse charge (art. 23); penalties; ISPC ceiling (MZN 4,000,000 reported by secondary commentary only).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
