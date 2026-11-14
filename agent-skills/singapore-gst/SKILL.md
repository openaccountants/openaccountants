---
name: singapore-gst
description: "Route Singapore GST registration, return, input-tax, reverse-charge, InvoiceNow, correction and penalty questions to the single detailed method sg-gst-return. This compatibility entry preserves the old singapore-gst name and contains no separate tax figures."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/singapore-gst"
  jurisdiction: "SG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Singapore GST method handoff v3.0

## Scope and who this is for

This is the compatibility entry for the former duplicate Singapore GST guide. The detailed method now lives in `sg-gst-return`; load it before answering, computing, filing or classifying a transaction. This entry is not a second set of rules or another accountant approval.

## Ask the client first

Establish Singapore jurisdiction, the client's GST registration/effective date, actual period and requested job. The detailed method supplies the remaining inputs. Keep tax residence for income tax separate from GST registration and customer belonging.

## The method, step by step

1. Load `sg-gst-return` and read its scope, required facts, rates and source/read-date boundaries.
2. For registration use its retrospective/prospective tests and evidence; do not infer registration from a bank narration or headline turnover alone.
3. For a return follow its sale/purchase classification, input conditions, blocked costs, customer belonging, reverse charge and exemption workflow, then the applicable F5 boxes and review steps.
4. For InvoiceNow, correction/F7, filing, payment, GIRO, overdue returns or penalties use the corresponding section of that same guide. Its historical examples and future phases keep their stated periods.
5. Preserve the original specialist referrals: groups/divisions, import suspension/deferment, customer accounting, margin/vehicle schemes, unresolved partial exemption, marketplace/redeliverer/OVR, uncertain international services, rate transitions, cancellation/F8, tourist refunds and suspected fraud. Never continue from a partial section when a relevant exception has not been read.
6. For token classification load `singapore-crypto-tax` as well. For an individual's income tax use `sg-income-tax`; for formation use `singapore-formation`. The GST method still controls GST answers.

The old full return-box table, every registration/input/RC/OVR/InvoiceNow/correction/penalty topic, boundary table, all eight worked cases and checklist are retained and updated in `sg-gst-return`. No tax topic was silently dropped from the detailed method.

## When to refuse or refer

If the detailed method cannot be retrieved, do not answer a figure, deadline, return box or filing procedure from this compatibility entry. Say which method is missing. Hold missing invoices, registration/period evidence, export/customer-belonging facts or unresolved source questions. Refuse false invoices, backdating, unsupported zero-rating or input claims and unauthorised filing/payment. Apply the detailed method's specialist refusals.

## Sources

| Source and scope read | Official URL | Read on |
|---|---|---|
| Read for the F5 return's box structure and why the detailed method, rather than this handoff, is necessary. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns | 2026-11-14 |
| Read for the registration tests and documentary forecast boundaries routed above; no figures reproduced here. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst | 2026-11-14 |

Not yet confirmed: a client-specific outcome remains subject to the facts and the current source gaps in `sg-gst-return`. This compatibility entry does not certify a rate, deadline, scheme approval or successful filing.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `singapore-gst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/singapore-gst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
