---
name: kw-vat-gst
description: "VAT, GST, excise and customs position in Kuwait for tax year 2026. Kuwait has no VAT or GST law in the Ministry of Finance legislation lists, so there is no registration, return, invoice or reverse charge. Use for questions such as does Kuwait have VAT, should I charge VAT to a Kuwaiti customer, can I recover VAT in Kuwait, Kuwait excise, GCC VAT agreement and Kuwait, and customs duty on imports. Lists what is unverified because the customs site could not be opened. Not signed off by an accountant."
version: 0.2
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait VAT / GST

Tax year 2026.

## Who this applies to

Anyone asking whether VAT, GST or excise applies in Kuwait. No taxpayer group is covered, because no such tax is enacted in the MOF lists read.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| VAT or GST status | Not implemented: the MOF lists of laws, decree-laws and resolutions carry no VAT law | 2026 | https://www.mof.gov.kw/MOFDesicions/mofDesicions1.aspx |
| VAT standard rate | Not applicable. Do not apply the 5% GCC framework rate | 2026 | same |
| Registration threshold | Not applicable | 2026 | same |
| Return frequency | Not applicable | 2026 | same |
| Reverse charge | Not applicable | 2026 | same |
| Excise | No excise law in the MOF lists | 2026 | same |
| Customs duty | unverified: 5% of CIF value on most goods, higher on tobacco, carried from the earlier version. customs.gov.kw did not open | 2026 | unverified |

## The base

There is no VAT base. Foreign VAT charged to a Kuwaiti business is not recoverable in Kuwait, as there is no return to claim it on.

## Deadlines and filing

No VAT filing exists. Do not register, charge or show VAT on Kuwaiti invoices.

## Penalties and interest

None, because there is no VAT.

## Cross-border points

A supplier in a GCC state with VAT applies its own state's rules to a Kuwaiti customer. Digital services into Kuwait carry no Kuwaiti VAT; income tax depends on Kuwait-source activity, see [corporate income tax](kw-corporate-income-tax.md).

## Two worked examples that recompute

**Example 1.** A Kuwaiti company invoices KWD 1,000. VAT added is zero, so the customer pays KWD 1,000.

```oa-check
name: Kuwaiti invoice, no VAT
inputs:
  net: 1000
  vat_rate: 0
steps:
  - vat: net * vat_rate
  - gross: net + vat
expected:
  vat: 0.00
  gross: 1000.00
```

**Example 2 (decision).** A foreign seller asks whether to charge 5% on a KWD 2,000 sale. Answer: no. Charging it would overcharge the customer by KWD 100 with no authority to collect it.

```oa-check
name: Overcharge if 5% is wrongly added
inputs:
  net: 2000
steps:
  - wrong_vat: net * 0.05
  - correct_vat: net * 0
expected:
  wrong_vat: 100.00
  correct_vat: 0.00
```

## Ask the client first

- Where is the seller established?
- Where is the customer established?
- Goods or services?
- Is the question about a sale in Kuwait or a purchase from a VAT state?

## Sources

| Source | URL | Read on |
|---|---|---|
| MOF list of laws, list pages read for VAT and excise titles | https://www.mof.gov.kw/MOFDesicions/mofDesicions1.aspx | 2026-11-01 |
| MOF list of decree-laws, list page read for VAT and excise titles | https://www.mof.gov.kw/MOFDesicions/mofDesicions2.aspx | 2026-11-01 |
| MOF list of resolutions, list page read for VAT and excise titles | https://www.mof.gov.kw/MOFDesicions/mofDesicions3.aspx | 2026-11-01 |

Not yet confirmed: A date for any Kuwait VAT or excise law: none found, and no official announcement was opened; customs duty rates, because the customs site did not open; the GCC VAT Framework Agreement text (2017) and GCC Excise Framework Agreement (2016), carried from the earlier version and not read.

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
