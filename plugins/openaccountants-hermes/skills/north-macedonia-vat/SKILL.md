---
name: north-macedonia-vat
description: "Use this skill whenever asked to prepare, review, or classify transactions for a North Macedonia VAT (DDV) return for any client. Trigger on phrases like \"Macedonia VAT\", \"North Macedonia VAT\", \"DDV\", \"PRO filing\", or any request involving Macedonian VAT. North Macedonia is NOT an EU member state but is an EU candidate country. ALWAYS read this skill before touching any North Macedonian DDV work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/north-macedonia-vat"
  jurisdiction: "MK"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# North Macedonia VAT

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Republic of North Macedonia |
| Tax name | DDV (Danok na Dodadena Vrednost) |
| Standard rate | 18% |
| Reduced rates | 10% (food and catering services — from 2024), 5% (basic foodstuffs, medicines, medical equipment, books, computers, solar panels, baby products, feminine hygiene, public transport, agricultural inputs) |
| Zero rate | 0% (exports; basic foodstuffs specified by government — bread, flour, cooking oil, sugar, rice — effective from government decree) |
| Exempt supplies | Financial services, insurance, medical, education, residential rental, postal universal service |
| Return form | DDV declaration |
| Filing portal | https://e-ujp.ujp.gov.mk |
| Authority | PRO/UJP (Upravata za Javni Prihodi) |
| Currency | MKD (Macedonian Denar) |
| Filing frequency | Monthly (turnover > MKD 25,000,000), quarterly (turnover <= MKD 25,000,000) |
| Deadline | 25th of month following period |
| Registration threshold | MKD 2,000,000 annual turnover |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending — requires licensed Macedonian tax practitioner |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate | 18% |
| Unknown purchase status | Not deductible |
| Unknown counterparty | Domestic North Macedonia |
| Unknown business-use | 0% |
| Unknown blocked status | Blocked |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction | MKD 200,000 |
| HIGH tax-delta | MKD 20,000 |
| MEDIUM concentration | >40% |
| MEDIUM defaults | >4 |
| LOW net position | MKD 500,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable input** — Minimum viable — bank statement. Banks: Komercijalna Banka, Stopanska Banka, NLB Banka, Halkbank, ProCredit Bank.

### Refusal catalogue

- **R-MK-1 — Below threshold** — Below mandatory DDV registration threshold. (Trigger: turnover below MKD 2,000,000)
- **R-MK-2 — Partial deduction** — Proportional deduction required. Flag for reviewer. (Trigger: mixed supplies)
- **R-MK-3 — TIDZ entity** — TIDZ entities have special DDV incentives. Escalate. (Trigger: client in a Technological Industrial Development Zone)

## Section 3 — Supplier pattern library

### 3.1 Banks

**Banks**  _(Financial service exempt)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| КОМЕРЦИЈАЛНА БАНКА, СТОПАНСКА БАНКА, NLB | EXCLUDE | Financial service exempt |

### 3.2 Government

**Government**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| УЈП, UJP, PRO | EXCLUDE | Tax payment |
| ФОНД ЗА ПЕНЗИСКО, ФОНД ЗА ЗДРАВСТВЕНО | EXCLUDE | Social security |

### 3.3 Utilities

**Utilities**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ЕВН, EVN MAKEDONIJA | Domestic 18% | Electricity |
| МАКЕДОНСКИ ТЕЛЕКОМ, А1, ONE.VIP | Domestic 18% | Telecoms |

### 3.4 SaaS non-resident

**SaaS non-resident**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | Reverse charge 18% | Self-assess |
| NOTION, ANTHROPIC, OPENAI | Reverse charge 18% |  |

### 3.5 Food and entertainment

**Food and entertainment**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ВЕРО, РАМСТОР, КАМ МАРКЕТ, ТИНЕКС | Default BLOCK | Personal |
| РЕСТОРАН | Default BLOCK | Entertainment |

### 3.6 Internal transfers

**Internal transfers**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ИНТЕРЕН ТРАНСФЕР | EXCLUDE |  |
| ПЛАТА, SALARY | EXCLUDE |  |

## Section 4 — Worked examples

### Example 1 — Non-resident reverse charge

**Input:** `NOTION LABS INC ; DEBIT ; MKD 900`
**Treatment:** Reverse charge 18%. Net zero.

### Example 2 — Standard domestic sale

**Input:** `ДООЕЛ КЛИЕНТ ; CREDIT ; MKD 118,000`
**Treatment:** Net = 100,000. DDV = 18,000.

### Example 3 — Entertainment, blocked

**Input:** `РЕСТОРАН ПЕЛИСТЕР ; DEBIT ; MKD 3,540`
**Treatment:** Blocked.

### Example 4 — Export

**Input:** `EU BUYER GMBH ; CREDIT ; MKD 300,000`
**Treatment:** Zero-rated. Full input credit.

### Example 5 — Food catering at 10%

**Input:** `КЕТЕРИНГ УСЛУГА ; CREDIT ; MKD 110,000`
**Treatment:** Catering at 10%. Net = 100,000. DDV = 10,000.

### Example 6 — Basic foodstuff at 5%/0%

**Input:** `SALE — bread, flour ; CREDIT ; MKD 52,500`
**Treatment:** Check current government decree — may be 5% or 0% for specified basics.

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 18%

### 5.2 Reduced rate 10% — food/catering services

### 5.3 Reduced rate 5% — basic foodstuffs, medicines, medical equipment, books, computers, solar, baby, feminine hygiene, transport, agricultural inputs

### 5.4 Zero rate — exports; government-decreed basic foodstuffs

### 5.5 Exempt — financial, insurance, medical, education, residential rental, postal

### 5.6 Reverse charge — services from non-residents at 18%

### 5.7 Imports — DDV at customs, deductible

### 5.8 Blocked — entertainment, personal use, vehicles (limited)

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 EU accession impact — evolving legislation

### 6.2 TIDZ incentives — flag

### 6.3 Vehicle costs — limited recovery, flag

### 6.4 Government decree rates — verify current list

## Section 7 — Excel working paper template

Standard layout.

## Section 8 — Bank statement reading guide

**Format:** Komercijalna/NLB CSV, DD.MM.YYYY, MKD. **Language:** Macedonian (Cyrillic) or Latin transliteration.

## Section 9 — Onboarding fallback

### 9.1 EDB — "What is your DDV identification number (EDB)?"

### 9.2 Filing period — monthly or quarterly?

### 9.3 Prior credit — always ask

## Section 10 — Reference material

### Sources

- **Zakon za DDV** — Zakon za DDV, Official Gazette No. 44/1999 (as amended)  _(Official Gazette No. 44/1999)_
- **PRO/UJP e-Taxes** — PRO/UJP e-Taxes — https://e-ujp.ujp.gov.mk  _(https://e-ujp.ujp.gov.mk)_

### Change log

- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.1/v1.0:** Initial skill.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `north-macedonia-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/north-macedonia-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
