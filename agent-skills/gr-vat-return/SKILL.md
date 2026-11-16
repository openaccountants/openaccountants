---
name: gr-vat-return
description: "Routing-only pointer for Greek VAT returns in tax year 2026. Load greece-vat-return for the method, rates, island reductions, small-business and EU SME schemes, input tax, reverse charge, intra-EU, OSS, refunds, periodicity and penalties. Load greece-einvoice for myDATA. This file does not compute tax or repeat the owner's figures. Trigger phrases: Greek VAT return, ΦΠΑ, do the VAT Greece, myAADE VAT, TAXISnet VAT."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gr-vat-return"
  jurisdiction: "GR"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Greek VAT return: routing to greece-vat-return v0.3

## The method, step by step

1. Load [greece-vat-return](greece-vat-return.md). It owns Greek VAT registration, the current VAT Code, rates and island conditions, the domestic small-business exemption and EU SME scheme, input VAT and blocked costs, reverse charge, intra-EU trade, OSS, periodic returns, payment, refunds and penalties.
2. Before using its method, establish the transaction and place of supply, tax period, book category, registration/start date, any periodicity election, exemption and island conditions. The old pointer's blanket statement that all single-entry businesses file quarterly is wrong: use the owner's A.1049/2025 start-date cohorts and election rules, corrected in v2.4.

3. For invoice creation, myDATA and e-invoicing load [greece-einvoice](greece-einvoice.md). Use [gr-tax-overview](gr-tax-overview.md) to locate other Greek tax jobs.
4. Hand off the facts, selected owner/version, exact applicable section and source, unresolved questions and proposed working papers. This pointer supplies no independent tax figures, filing calendar or computation.

## When to refuse or refer

Do not use the superseded VAT Code or historical figures from this file, infer a rate from an island's name, assume an exemption without checking its conditions, or describe a prepared return as filed. If the owner's Sources identifies an unresolved question, keep it unresolved and refer the particular position for professional review.

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| Ministry of Finance VAT Code codification through Law 5313/2026: read arts. 26, 43 and 44a for the old pointer's rate, period and exemption topics; substantive application is handed to the owner | https://minfin.gov.gr/wp-content/uploads/2026/10/Κοινοποίηση-Διοικητικής-Κωδικοποίησης-του-ν.5144-2024-γι.pdf | 2026-11-16 |
| Repository base owner: read in full for routing and open questions; its separate v2.4 delta changes only A.1049/2025 periodicity, not all unchanged VAT claims | https://github.com/openaccountants/openaccountants/blob/2844c309238b4fdb63be0a3d0ad9ae99a8ea89c8/skills/greece/greece-vat-return.md | 2026-11-16 |

| AADE A.1049/2025, read arts. 1-4 for the corrected owner’s start cohorts and election conditions | https://www.aade.gr/sites/default/files/2025-04/a1049_2025fek.pdf | 2026-11-16 |

Not yet confirmed: the unresolved items in the owning greece-vat-return skill, including transaction-specific island, exemption, input-credit and filing exceptions. This pointer does not resolve or silently remove them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gr-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gr-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
