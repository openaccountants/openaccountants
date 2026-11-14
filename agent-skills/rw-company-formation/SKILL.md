---
name: rw-company-formation
description: "Rwanda company formation for 2026: online RDB registration, free and within six working hours, shareholders, registered address, TIN, and tax obligations after incorporation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/rw-company-formation"
  jurisdiction: "RW"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Rwanda Company Formation and Entity Choice

## Who this applies to

Founders of a company, individual enterprise or branch. Register with the Registrar General within 7 days of starting (https://www.rra.gov.rw/en/domestic-tax-services/registration-de-registration/default-title).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Registration fee | Free, 100% online | 2026 | https://org.rdb.rw/business-registration/ |
| Time | Six working hours | 2026 | same |
| Foreign ownership | 100% non-local shareholding allowed | 2026 | same |
| Registered address | Local physical address required | 2026 | same |
| Share capital | Unlimited registered capital, can be increased any time; unverified: no minimum (old file) | 2026 | same |

## The base

Categories: individual enterprise, limited company, foreign branch. Public companies, partnerships and representative offices: unverified from the old file. Cooperatives register with RCA at cmis.rca.gov.rw (https://www.rra.gov.rw/en/domestic-tax-services/registration-de-registration/default-title). Limited company shareholders: unverified old limit of 100; RDB says as many as you wish.

## Deadlines and filing

1. Prepare email, ID or passport; for corporate shareholders, the incorporation certificate and articles (https://org.rdb.rw/business-registration/).
2. Register at businessprocedures.rdb.rw; name must be approved.
3. Receive the certificate; RDB and RRA systems issue one TIN (https://www.rra.gov.rw/en/domestic-tax-services/registration-de-registration/default-title).
4. Sign up at https://etax.rra.gov.rw.
5. Register for VAT if thresholds are met, PAYE and RSSB when hiring.

Ongoing: see overview. Annual return to the Registrar: unverified.

## Penalties and interest

Failure to register: art 81 fine, see [rw-corporate-income-tax](rw-corporate-income-tax.md).

## Cross-border points

A foreign company branch needs a shareholder or board resolution and a branch representative (https://org.rdb.rw/business-registration/).

## Two worked examples that recompute

```oa-check
name: Registration cost
inputs:
  fee: 0
steps:
  - cost: fee
expected:
  cost: 0.00
```

**Decision: company or individual enterprise.** Compare 28% on FRW 10,000,000 profit with personal tax of 288,000 plus 30% above 2,400,000.

```oa-check
name: Company or individual on FRW 10,000,000
inputs:
  profit: 10000000
steps:
  - company: profit * 0.28
  - personal: 288000 + (profit - 2400000) * 0.30
  - gap: personal - company
expected:
  gap: -232000.00
```

## Ask the client first

1. Shareholders, local or foreign?
2. Activities?
3. Local address?
4. Expected turnover?

## Sources

| Source | URL | Read on |
|---|---|---|
| RDB, business registration page (whole page) | https://org.rdb.rw/business-registration/ | 2026-11-01 |
| RRA, Register your business page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/registration-de-registration/default-title | 2026-11-01 |

Not yet confirmed: no minimum capital; TIN doubling as RSSB number; the annual return to the Registrar General; the 100 shareholder limit; entity list beyond the RDB page.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `rw-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/rw-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
