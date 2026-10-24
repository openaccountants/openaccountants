---
name: be-vat-return
description: "Use this skill whenever asked to prepare, review, or classify transactions for a Belgian VAT return (déclaration périodique TVA / periodieke BTW-aangifte) for a self-employed individual or small business in Belgium. Trigger on phrases like \"prepare Belgian VAT return\", \"Belgian BTW\", \"déclaration TVA Belgique\", \"BTW-aangifte\", \"classify transactions for Belgian VAT\", or any request involving Belgium VAT filing. This skill covers Belgium only, standard regime (normal/normal simplifié). Régime forfaitaire, partial exemption, margin scheme, and VAT units are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Belgian VAT work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/be-vat-return"
  jurisdiction: "BE"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

This skill is superseded by [belgium-vat-return](belgium-vat-return.md), which now holds the 2026 Belgian VAT rules: rates, the small-business exemption, return frequency and deadlines, refunds, structured e-invoicing and penalties. Use that file instead. Built by Michael Cutajar and the OpenAccountants team. Source-cited draft: not reviewed by an accountant.

> Contributed by Michael Cutajar.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `be-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/be-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
