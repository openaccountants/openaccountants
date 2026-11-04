---
name: gl-mandatory-pension
description: "Calculate a bounded 2026 Greenland mandatory pension minimum using the 2025 consolidation together with the May 2026 amendment."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gl-mandatory-pension"
  jurisdiction: "GL"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Greenland mandatory pension: 2026 amendment

**Source-cited draft. Independent review pending.** Sources accessed 22 October 2026. This is a bounded working-paper Guide, not complete Greenland coverage or authority to file.

## Read the amendment with the consolidation

The 2025 consolidation still prints a rise to **10% in 2026**. The enacted May 2026 amendment replaces that sentence with an increase ending at **9% in 2025**, effective for 2026 onward. Read the two instruments together: the ordinary rate remains **9% for 2026**. The amendment also changes the civil-servant exclusion and suspends specified tax-card/tax-bill collection mechanisms for 2026–27. Suspension of that collection mechanism does not repeal the savings obligation. [Act no.19 of 29 May 2026, sections 1–2](https://nalunaarutit.gl/groenlandsk-lovgivning/2026/inatsisartutlov-nr-19-af-29_05_2026?sc_lang=da).

## Bounded calculation rules

The Act covers fully taxable adults, with start/stop age rules in section 1. The savings base combines A/B income and specified additions, less statutory exclusions. For an ordinary base of DKK 175,000 or more, use the full applicable rate. Between DKK 125,000 and 175,000, the rate increases linearly from zero to the full rate. Qualifying self-employment profits use a separate **6%** rule. The annual obligation ceases once contributions reach **DKK 200,000**. Contributions taxed on payment or non-deductible contributions require a pre-tax conversion. [Consolidation no.67, ss1–5, read with the amendment](https://nalunaarutit.gl/groenlandsk-lovgivning/2025/selvstyrets-lovbekendtgoerelse-nr-67-af-25_09_2025?sc_lang=da).

## Worked ordinary-income cases

Assume an eligible adult, an already established ordinary savings base, no self-employment component, no conversion adjustment and no contributions yet credited:

| Base (DKK) | Rate calculation | Minimum (DKK) |
|---|---|---:|
| 125,000 | 0% | 0 |
| 150,000 | 9% × (150,000 − 125,000) / 50,000 = 4.5% | 6,750 |
| 175,000 | 9% | 15,750 |
| 300,000 | 9% | 27,000 |

The taper changes the percentage applied to the base. It is not simply 9% of the amount above DKK 125,000. These examples are our arithmetic application of section 3 as amended, subject to independent legal review.

If the DKK 300,000 case already has DKK 20,000 of qualifying contributions measured on the required basis, the remaining minimum is DKK 7,000. Do not subtract a bank payment until its eligibility and required conversion have been established.

## Working paper and unresolved cases

Record age, full-tax-liability dates, income categories, excluded income, scheme jurisdiction, employer contributions, personal contributions and conversion adjustments. Reconcile those values to income records and pension statements. Keep contractual pension obligations separate from this statutory minimum.

Foreign-scheme permissions, mixed employment/self-employment income, precise start/stop-age application, civil-service benefits and the treatment of historical shortfalls need individual review. Do not infer from a tax card without an extra collection percentage that no pension saving is required. The 2026 amendment is essential evidence; a copy of the older consolidation alone is insufficient.

## Review output

Retain the applicable source version, calculation inputs, reconciliations and unresolved classifications. A qualified local reviewer must check the actual facts and current law before filing or payment. No professional attestation is claimed.

> Contributed by Ryan Duguid.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gl-mandatory-pension` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gl-mandatory-pension. If neither is available, confirm every figure against the official source pages cited above before relying on it.
