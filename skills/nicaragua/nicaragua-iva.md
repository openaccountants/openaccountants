---
name: nicaragua-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Nicaragua IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "Nicaragua VAT", "DGI return", "VET filing", or any request involving Nicaragua value added tax filing. This skill covers Regimen General IVA filers only. Cuota Fija (fixed-fee small taxpayer) and free-zone entities are in the refusal catalogue. ALWAYS read this skill before touching any Nicaragua IVA work.
version: 2.0
jurisdiction: NI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nicaragua IVA

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Nicaragua |
| Standard rate | 15% |
| Zero rate | Exports |
| Exempt supplies | Basic food basket, medicines, agricultural inputs, medical services, education, public transport, financial interest, insurance, residential rental, electricity/water (domestic) |
| Return form | Monthly IVA declaration |
| Filing portal | https://www.dgi.gob.ni (VET) |
| Authority | DGI (Direccion General de Ingresos) |
| Currency | NIO (Cordoba) / USD (some transactions) |
| Filing frequency | Monthly |
| Deadline | 15th of month following period |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate | 15% |
| Unknown purchase status | Not deductible |
| Unknown counterparty | Domestic Nicaragua |
| Unknown business-use | 0% |
| Unknown blocked status | Blocked |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement. Banks: BAC, Banpro, Lafise Bancentro, Banco de la Produccion (Banpro), Ficohsa.

### Refusal catalogue

- **R-NI-1 — Cuota Fija** — Cuota Fija taxpayers pay a fixed monthly amount and do not file IVA returns. (Trigger: client under fixed-fee small taxpayer regime.)
- **R-NI-2 — Free zone** — Free zone entities have IVA exemptions. Escalate. (Trigger: client in a zona franca.)
- **R-NI-3 — Cooperative special regime** — Cooperatives may have special IVA treatment. Flag. (Trigger: cooperative entity.)

## Section 3 — Supplier pattern library

### 3.1 Banks

**Banks**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BAC, BANPRO, LAFISE, FICOHSA | 15% for fees; EXCLUDE for interest |  |

### 3.2 Government

**Government**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI, INSS | EXCLUDE | Tax/social security |
| ALCALDIA | EXCLUDE | Municipal fee |

### 3.3 Utilities

**Utilities**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UNION FENOSA, DISNORTE, DISSUR | Domestic 15% (commercial) | Electricity |
| ENACAL | Exempt (domestic water) |  |
| CLARO, TIGO | Domestic 15% | Telecoms |

### 3.4 SaaS non-resident

**SaaS non-resident**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META, ZOOM | Reverse charge 15% |  |
| NOTION, ANTHROPIC, OPENAI | Reverse charge 15% |  |

### 3.5 Food and entertainment

**Food and entertainment**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| LA COLONIA, PALI, MAXI PALI | Default BLOCK | Personal |
| RESTAURANT | Default BLOCK | Entertainment |

### 3.6 Internal transfers

**Internal transfers**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA | EXCLUDE |  |
| NOMINA, SALARIO | EXCLUDE |  |

## Section 4 — Worked examples

### Example 1 — Non-resident reverse charge

**Input:** `NOTION LABS INC ; DEBIT ; NIO 500`
**Treatment:** Reverse charge 15%. Net zero.

### Example 2 — Standard domestic sale

**Input:** `EMPRESA CLIENTE SA ; CREDIT ; NIO 115,000`
**Treatment:** Net = 100,000. IVA = 15,000.

### Example 3 — Entertainment, blocked

**Input:** `RESTAURANT ; DEBIT ; NIO 1,150`
**Treatment:** Blocked. No credit.

### Example 4 — Export

**Input:** `US BUYER ; CREDIT ; NIO 500,000`
**Treatment:** Zero-rated. Full input credit.

### Example 5 — Motor vehicle, blocked

**Input:** `AUTOMOTRIZ ; DEBIT ; sedan ; NIO 400,000`
**Treatment:** Blocked.

### Example 6 — Basic food (exempt)

**Input:** `PROVEEDOR AGRICOLA ; DEBIT ; basic grains ; NIO 50,000`
**Treatment:** Exempt. No IVA. No input credit on attributable costs.

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 15% (LCT Art. 109)

- **Standard rate** — 15%

### 5.2 Exempt goods — basic food basket, medicines, agricultural inputs

- **Exempt goods** — Basic food basket, medicines, agricultural inputs

### 5.3 Exempt services — medical, education, public transport, financial interest, insurance, residential rental

- **Exempt services** — Medical, education, public transport, financial interest, insurance, residential rental

### 5.4 Exports — zero-rated with full input credit

- **Exports** — Zero-rated with full input credit

### 5.5 Reverse charge — services from non-residents

- **Reverse charge** — Services from non-residents

### 5.6 Blocked input IVA — entertainment, vehicles, personal use

- **Blocked input IVA** — Entertainment, vehicles, personal use

### 5.7 Self-supply (autoconsumo) — taxable event

- **Self-supply (autoconsumo)** — Taxable event

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Cooperative treatment — flag

- **Cooperative treatment** — Flag

### 6.2 Mixed operations — proportional method

- **Mixed operations** — Proportional method

### 6.3 Digital services from non-residents — evolving

- **Digital services from non-residents** — Evolving

## Section 7 — Excel working paper template

Standard layout.

## Section 8 — Bank statement reading guide

**Format:** BAC/Banpro CSV, DD/MM/YYYY, NIO. **Language:** Spanish.

## Section 9 — Onboarding fallback

### 9.1 RUC — "What is your RUC?"

"What is your RUC?"

### 9.2 Regime — "Regimen General or Cuota Fija?"

"Regimen General or Cuota Fija?"

### 9.3 Prior credit — always ask

always ask

## Section 10 — Reference material

### Sources

1. Ley de Concertacion Tributaria (LCT), Ley 822 (as amended by Ley 987)
2. Reglamento LCT (Decreto 01-2013)
3. DGI VET — https://www.dgi.gob.ni

### Change log

- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
