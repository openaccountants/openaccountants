---
name: mg-company-formation
description: "Madagascar 2026 formation preparation for SARL/SARLU using official EDBM instructions, capital allocation and tax-registration handoff; limited scope."
jurisdiction: MG
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
---

# Madagascar company formation: SARL dossier and tax handoff

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Madagascar.

## Who this applies to

Use to prepare an ordinary SARL/SARLU dossier and identify the tax work needed after incorporation. The official EDBM document selector also lists SA/SAU, EI and SDET; select that actual form’s requirements rather than reuse a SARL checklist. [EDBM legal-form documents](https://orinasa.edbm.mg/documentsLegalForm/). This Guide does not give an incorporation guarantee, a complete company-law opinion or special-sector approval.

## Rates, bands and thresholds

| Formation choice | Verified rule / workflow | Official source |
|---|---|---|
| SARL capital | Freely set by contributors; no nominal example is a legal minimum | [EDBM, Créer une SARL](https://orinasa.edbm.mg/Articles_3/) |
| SARL manager | Gérant, with co-gérant where appointed | same |
| Resident presence for EDBM dossier | At least one resident dirigeant, gérant or co-gérant | same |
| Analamanga incorporation channel | Online Orinasa personal account; accepted dossier leads to appointment for payment and physical archival file | same |

The EDBM information page was updated in October 2025 and remains available when read. Its fee figures are not treated as a verified 2026 statutory tariff. Obtain a current assessment rather than quote a setup price or timing.

## The base

EDBM describes a SARL as a separate company with partners liable for social debts up to contributions. Capital is allocated from the agreed contributions; obtain valuation support for non-cash contributions and signed partner decisions. Draft statutes identifying form, name, activity/object, partners and contributions, capital and share values, registered office, duration and operation. Name the gérant in the statutes or a later act. [EDBM opening and Etape 1](https://orinasa.edbm.mg/Articles_3/). This operational statement does not settle shareholder-number limits or every liability exception; those require the company law.

## Deadlines and filing

Prepare the statutes and the form-specific supporting documents from [EDBM’s selector](https://orinasa.edbm.mg/documentsLegalForm/), including identity and tax-status evidence, premises documents and appointment act when relevant. For a foreign legal-person shareholder, the selector asks for statutes and commercial-registry extract in sworn French translation.

EDBM’s SARL instructions require a commercial lease, property/legal-status evidence, proof that premises exist, a location plan, at least one resident manager and prior authorization for a regulated activity. In Analamanga, create/log into the [Orinasa account](https://client.orinasa.edbm.mg), enter the actual dossier, attach its generated required documents, and wait for the dossier to be deemed admissible. The stated next step is an appointment for payment and submission of a physical archive file. Keep all incorporation outputs and fiscal-registration evidence. [EDBM Etapes 2–4](https://orinasa.edbm.mg/Articles_3/).

Then confirm NIF and elected/assigned regime with DGI. Route ongoing obligations to [business tax](mg-corporate-income-tax.md), [TVA](mg-vat-gst.md) and [payroll](mg-payroll-social.md). Do not assume incorporation alone proves TVA enrolment. No fixed completion time is established here.

## Penalties and interest

Formation fees, late-registration sanctions, annual company-law filing deadlines and audit obligations are outside the verified 2026 scope. Tax return/payment consequences belong to the relevant tax Guide; do not apply a tax late-payment rate to a registry filing.

## Cross-border points

A foreign company selecting a branch/SDET must use that dossier’s requirements. The SARL document selector distinguishes foreign legal-person shareholders and asks for their statutes and registry extract in sworn French translation. [EDBM documents](https://orinasa.edbm.mg/documentsLegalForm/). A resident-manager requirement does not establish the company’s tax-treaty residence. Use [cross-border triage](mg-cross-border.md) before choosing a foreign branch versus company.

## Two worked examples that recompute

Hypothetical equal-rights cash shares, no special classes or non-cash valuation dispute. These are capital-allocation workpapers, not a statutory minimum or tax computation.

```oa-check
name: Two partner capital allocation
inputs:
  partner_a: 600000
  partner_b: 400000
  share_nominal: 10000
steps:
  - capital: partner_a + partner_b
  - shares_a: partner_a / share_nominal
  - shares_b: partner_b / share_nominal
  - total_shares: shares_a + shares_b
expected:
  capital: 1000000
  shares_a: 60
  shares_b: 40
  total_shares: 100
```

```oa-check
name: Single shareholder allocation
inputs:
  contribution: 500000
  share_nominal: 5000
steps:
  - shares: contribution / share_nominal
  - capital_check: shares * share_nominal
expected:
  shares: 100
  capital_check: 500000
```

## Ask the client first

Get chosen entity/activity, all partner identities and legal forms, ownership and share rights, cash/non-cash contributions, manager and residence evidence, lease/property documents and location, regulated authorizations, foreign shareholder documents and intended regime. Ask for actual EDBM/DGI assessments before quoting charges.

## Sources

 | Source and provisions actually read | Read on |
|---|---|
| [EDBM SARL official instructions](https://orinasa.edbm.mg/Articles_3/), opening, Etapes 1–4; page labels October 2025 update | 2026-11-01 |
| [EDBM official document selector](https://orinasa.edbm.mg/documentsLegalForm/), SARL/SARLU, shareholders, premises and manager documents | 2026-11-01 |

**Not yet confirmed:** current underlying company-law articles, SARL maximum partners, SA governance/minimum capital, nationality restrictions, 2026 fee tariffs, complete NIF issuance sequence, annual registry/accounts filings and binding completion times. These old topics are preserved as gaps, not inferred from the SARL operational page.

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
