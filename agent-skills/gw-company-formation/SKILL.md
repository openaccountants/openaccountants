---
name: gw-company-formation
description: "Guinea-Bissau company formation for 2026: OHADA forms, tax registration and ongoing filings, with what we could not confirm from an official source."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gw-company-formation"
  jurisdiction: "GW"
  tax_year: "2026"
  last_updated: "2026-11-01"
---

# Guinea-Bissau Company Formation and Entity Choice (2026)

Guinea-Bissau is an OHADA member, so company law follows the OHADA Uniform Act on Commercial Companies. We could not open the Act on an official page, so every figure from it is unverified.

## Entity types

| Item | Position | Source |
|---|---|---|
| Common forms | SARL, single-member SARL (SUARL), SA | unverified, OHADA Act not opened |
| Foreign branch | Possible; conversion period | unverified |
| SARL minimum capital | unverified: old skill said no fixed minimum, often XOF 1,000,000 | unverified |
| SA minimum capital | unverified: old skill said XOF 10,000,000 | unverified |
| Annual financial statements | unverified: old skill said OHADA SYSCOHADA framework | unverified |
| One-stop shop, Centro de Formalização de Empresas | unverified: steps, 1 to 3 week timing, fees | unverified |

## Tax steps after formation

| Step | Rule | Official URL |
|---|---|---|
| Get a NIF | Needed before activity; a missing or false NIF costs FCFA 250,000 (Contribuição Industrial code arts 5, 61) | https://kontaktu.mef.gw/legislation |
| IVA start declaration | Before starting (Código do IVA art. 28) | same |
| Kontaktu access | "Autorização de Uso do Kontaktu" form | https://kontaktu.mef.gw/api/public_files/cQ07WYIBVxKCKoELcDhC.pdf |
| Accounts | Organised accounts for group A, signed by an enrolled accountant (art. 20); annual return in April with balance sheet, income statement and cash flow statement (art. 23) | https://kontaktu.mef.gw/legislation |

The DCI-SMT instructions refer to the minimum treasury system of art. 13 of the OHADA accounting Uniform Act of 15 February 2017 for smaller taxpayers.

## Ongoing filings

See [corporate tax](gw-corporate-income-tax.md), [VAT](gw-vat-gst.md) and [payroll](gw-payroll-social.md).

## Worked checks

A new company with no profit and forecast turnover of FCFA 80,000,000 still owes the 1% minimum tax: 800,000.

```oa-check
name: Minimum tax in a loss year
inputs:
  turnover: 80000000
steps:
  - ci: max(0, turnover * 0.01)
expected:
  ci: 800000
```

The same company charges IVA once the tax administration confirms the forecast, as it passes FCFA 40,000,000 (Código do IVA art. 37(3)). A month of FCFA 6,000,000 sales with FCFA 300,000 input IVA: 1,140,000 less 300,000 = 840,000.

```oa-check
name: First IVA month
inputs:
  sales: 6000000
  input_vat: 300000
steps:
  - due: sales * 0.19 - input_vat
expected:
  due: 840000
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Contribuição Industrial code and Código do IVA | https://kontaktu.mef.gw/legislation | 2026-11-01 |
| DCI-SMT instructions | https://kontaktu.mef.gw/api/public_files/cQ07WYIBVxKCKoELcDhC.pdf | 2026-11-01 |

Not yet confirmed: all OHADA figures and the order of incorporation steps (name, by-laws, capital deposit, RCCM, NIF, social security); branch conversion; CFE timing and fees. The OHADA and CFE pages tried did not give the text.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-01. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gw-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gw-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
