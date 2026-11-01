---
name: gw-vat-gst
description: "Guinea-Bissau IVA for tax year 2026: rates, FCFA 40 million threshold, simplified 5% regime, reverse charge, monthly return and credits, from Lei 4/2022."
jurisdiction: GW
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guinea-Bissau VAT (IVA) (2026)

**Status of the 2026 budget text.** The Ministry of Finance publishes a document called OGE 2026, dated December 2025 (https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195). Its law number and date are blank (`Lei n.º ____/202`), and we could not confirm a vote, promulgation or Boletim Oficial publication. Each rule below marked "2026 budget text" applies only if that law is in force. Confirm that with the DGCI before relying on it.

## Who this applies to

IVA replaced the IGV. The Código do IVA is Lei 4/2022, and Despacho 130/GMF/2024 fixed [1 January 2025](https://dgci.mef.gw/despacho-no-130-gmf-2024/) as the start date. A business falls into one of three regimes by prior-year turnover (arts 37, 38, 45). The regime is decided by the law, not chosen: simplified and small taxpayers cannot opt into normal IVA (art. 37(6)).

| Regime | Turnover, or single operation | Effect |
|---|---|---|
| Normal | FCFA 40,000,000 or more | Charge IVA, deduct input IVA, file monthly |
| Simplified | FCFA 10,000,000 up to 40,000,000 | 5% of sales, no deduction, file quarterly |
| Small taxpayer | Under FCFA 10,000,000 | Exempt from IVA; single small-taxpayer tax set by separate law |

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate (art. 18(1)(b)) | 19% | 2026 | https://kontaktu.mef.gw/legislation |
| Reduced rate, Annex I (art. 18(1)(a)) | 10% | 2026 | same |
| Exports (art. 18(1)(c)) | 0% | 2026 | same |
| Simplified regime (art. 38(2)) | 5% | 2026 | same |
| Normal regime threshold (art. 37) | FCFA 40,000,000 | 2026 | same |
| Simplified threshold (art. 38) | FCFA 10,000,000 | 2026 | same |
| Extra levy on imports by listed non-declarers (Lei 4/2022 art. 6) | 30% of customs value | 2026 | same |
| Gifts outside the rules (art. 3(4)) | FCFA 50,000 unit value | 2026 | same |
| Electricity and water, 2026 budget text | 15% | 2026 | https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195 |
| Extra levy, 2026 budget text, replaces the 30% | 7% of customs value | 2026 | same |

The 2026 budget text also rewrites Annex I. It lists cereals, rice, flour, pasta, bread, roots, meat, fish, dairy, eggs, oil, fruit and vegetables, water, honey, salt, sugar, soap, soft drinks, school items, press, farm inputs, solar and IT equipment, funeral services, passenger transport, fire equipment, some legal services for individuals, restaurants, hotels and tourism, home construction, and State construction contracts. It also exempts international air tickets (art. 13(1)(h)).

## The base

Taxable value is the consideration, plus other taxes and charged extras, excluding IVA itself (art. 16). For imports it is customs value plus duties and import costs (art. 17). To extract IVA from a tax-inclusive price, divide by 100 plus the rate, times 100 (art. 35).

Exempt without deduction (art. 13): listed medicines; medical care; education; domestic gas; financial and insurance operations with no explicit fee; housing property, excluding hotel lodging. Exports and international ship and aircraft supplies are exempt with deduction (arts 15, 20).

Input IVA needs a legal invoice and a normal-regime supplier or customs document (art. 19). Blocked: travel, hospitality and leisure; passenger vehicles and their fuel, unless that is the business; boats, helicopters, planes and motorcycles; luxury costs (art. 21). Mixed businesses deduct pro rata (art. 23).

Excess credits carry forward. After 12 months, a credit above FCFA 1,000,000 can become a tax credit note; above FCFA 25,000,000 needs prior inspection (art. 24).

## Deadlines and filing

| Step | Deadline | Basis |
|---|---|---|
| Start declaration | Before starting | art. 28 |
| Change of details | 15 days | art. 28 |
| Ceasing activity | 30 days | art. 28 |
| Invoice | When tax falls due, or by the 5th working day | art. 29 |
| Monthly return and payment, normal | 15th of next month, even if nil | arts 25, 31 |
| One-off return | End of the month of the operation | art. 32 |
| Simplified return and payment | Last working day of April, July, October, January, even if nil | art. 42 |
| Simplified records | Within 30 days of receipt | art. 40 |

How to file a monthly return: use the model approved by the DGCI at the tax office or authorised bank (art. 31). Report output IVA by rate, exempt sales, and deductible input IVA, then pay by the same date. We could not confirm the box numbers or an electronic IVA form on Kontaktu; the portal's published form is the older IGV return. Simplified invoices must read "IVA Simplificado – Não confere direito à dedução" (art. 39).

## Penalties and interest

Penalties sit in the Regime Geral das Infrações Tributárias, Lei 5/2022 (art. 47). 2026 budget text: failing to require invoices FCFA 25,000 to 750,000. If tax is assessed by the office, pay within 30 days of notice (art. 26).

## Cross-border points

A normal- or simplified-regime customer self-assesses IVA on services from a supplier with no base or fiscal representative here (art. 7(1)). A non-resident making taxable supplies must appoint a representative who is an IVA taxpayer; without one, the customer pays (art. 33). Services invoiced by entities in privileged tax regimes that produce payments from Guinea-Bissau count as local (art. 10(4)). Normal-regime buyers withhold all the IVA on invoices from simplified taxpayers and from those the DGCI names as risky (art. 7(3)).

## Two worked examples that recompute

Normal regime month: sales FCFA 10,000,000 at 19%, input IVA FCFA 800,000. Pay 1,100,000 by the 15th.

```oa-check
name: Normal regime month
inputs:
  sales: 10000000
  input_vat: 800000
steps:
  - output: sales * 0.19
  - due: output - input_vat
expected:
  due: 1100000
```

Decision: turnover FCFA 39,000,000 or 41,000,000 with FCFA 20,000,000 of purchases carrying 19%. Under simplified: 5% of 39,000,000 = 1,950,000, a cost with no recovery. Under normal at 41,000,000: charge 7,790,000, deduct 3,800,000, remit 3,990,000 but collected from customers. If customers cannot absorb IVA, the threshold matters; if they are IVA-registered, normal costs them nothing.

```oa-check
name: Simplified or normal near the threshold
inputs:
  low: 39000000
  high: 41000000
  purchases: 20000000
steps:
  - simplified: low * 0.05
  - normal: high * 0.19 - purchases * 0.19
expected:
  simplified: 1950000
  normal: 3990000
```

## Ask the client first

1. Last calendar year's turnover, and this year's forecast if new?
2. What is sold, and is it on Annex I?
3. Are customers businesses or consumers?
4. Non-resident: is there a base or representative?
5. Are there imports, and is the client on the declarers' list?
6. Any exempt sales?

## Sources

| Source | URL | Read on |
|---|---|---|
| Código do IVA, Lei 4/2022, full text (consolidated text on the DGCI Kontaktu legislation page; only the sections for this skill were read) | https://kontaktu.mef.gw/legislation | 2026-11-01 |
| Despacho 130/GMF/2024, DGCI page | https://dgci.mef.gw/despacho-no-130-gmf-2024/ | 2026-11-01 |
| OGE 2026, Lei do Orçamento, arts 6 to 17 (draft-form text, law number blank; the tax chapter only was read) | https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195 | 2026-11-01 |

Not yet confirmed: whether the 2026 budget text is in force, which decides the 15%, 7% and new Annex I; the source of the small-taxpayer tax law (art. 45) and its rate; box numbers of the IVA return and whether it runs on Kontaktu; the Annex I in force before the budget; Lei 5/2022 penalty amounts for late IVA (the law text was not on the portal page read). The old 'real estate' exemption is narrowed to housing as art. 13 says.

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
