---
name: tw-tax-overview
description: "Use this skill to orient a Taiwan tax question for tax year 2026 and route it to the right Taiwan skill. It gives the system at a glance (calendar tax year, Ministry of Finance and National Taxation Bureaus, largely territorial individual tax with overseas income in the basic tax, worldwide company tax), the headline rates (individuals 5% to 40%, enterprises 20%, business tax 5%) and the filing months. Built from the law, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tw-tax-overview"
  jurisdiction: "TW"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Taiwan tax overview and routing (tax year 2026)

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in Taiwan.

## Scope

Taiwan (Republic of China) taxes individuals mainly on Taiwan-source income (overseas income enters only the individual basic tax), and enterprises with a head office in Taiwan on worldwide income. The tax year is the calendar year; the currency is the New Taiwan dollar (NT$). The Ministry of Finance administers national taxes through the National Taxation Bureaus and the eTax portal. A value-added business tax applies to most sales of goods and services.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Individual income tax | 5% to 40% | Five bands; top band above NT$5,190,000 of net income for 2026 | https://www.ntbt.gov.tw/multiplehtml/1b82b380e1a34de9afd204d39b007db2 |
| Personal exemption | NT$101,000 per person | 2026 | https://www.mof.gov.tw/download/bb34472701e4443c910788e792dae85c |
| Individual basic tax deduction | 750萬 (7.5 million NT dollars) | Basic income above it may trigger the basic tax | same |
| Profit-seeking enterprise income tax | 20% | Taxable income above NT$120,000; half-excess cap to NT$200,000 | https://www.ntbt.gov.tw/singlehtml/0baa381b53034993a08862dfde2243b9?cntId=08f87d2104c04266a40e67c00d7c5c5a |
| Enterprise and individual returns | 1 to 31 May of the following year | For 2026: May 2027 | same |
| Business tax (VAT) | 5% | Floor of the statutory 5% to 10% range; bimonthly returns by the 15th of the next period | https://law-out.mof.gov.tw/LawContent.aspx?id=FL006082 |

## The method, step by step

1. **Name the job.** Individual income tax and freelancers: `tw-income-tax`. Company tax, provisional tax, undistributed earnings, withholding on payments abroad: `tw-corporate-income-tax`. Business tax (VAT), uniform invoices, the 401 return: `taiwan-vat`. National Health Insurance: `tw-nhi`. Setting up a company or 行號: `tw-company-formation`.
2. **Check residence or head office.** Individuals: domicile or 183 days in the year. Enterprises: head office in Taiwan or not.
3. **Pick the year.** Use 2026 amounts for income of calendar 2026 (returns in May 2027); 2025 amounts for returns filed in May 2026.
4. **Mainland China and Hong Kong** are separate systems: use the `china` and `hong-kong` packs.

### Worked case: enterprise tax headline check

A Taiwan company with taxable income of NT$2,000,000 in 2026: 20% = NT$400,000, due with the return in May 2027 (less the September 2026 provisional payment). Route: `tw-corporate-income-tax`.

```oa-check
name: TW 2026 enterprise tax headline at NT$2m
inputs:
  taxable: 2000000
steps:
  - tax: min(taxable * 0.20, (taxable - 120000) / 2)
expected:
  tax: 400000
```

## When to refuse or refer

- Mainland China-source income or Mainland investors (separate rules): refer.
- Transfer pricing, controlled foreign company rules, global minimum tax: refer to a Taiwan CPA.
- Any request to hide income or invoices: refuse.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Taipei National Taxation Bureau, applicable rates. Read for the 2026 individual bands | https://www.ntbt.gov.tw/multiplehtml/1b82b380e1a34de9afd204d39b007db2 | 2026-11-14 |
| MOF, 2026 amounts table (PDF). Read for the exemption and the basic tax deduction | https://www.mof.gov.tw/download/bb34472701e4443c910788e792dae85c | 2026-11-14 |
| Taipei National Taxation Bureau, enterprise income tax page. Read for the 20% rate, 120,000 exemption and May filing | https://www.ntbt.gov.tw/singlehtml/0baa381b53034993a08862dfde2243b9?cntId=08f87d2104c04266a40e67c00d7c5c5a | 2026-11-14 |
| VAT Act, MOF laws and regulations system. Read for arts. 10 and 35 | https://law-out.mof.gov.tw/LawContent.aspx?id=FL006082 | 2026-11-14 |

Not yet confirmed: basic tax rates (old file: individuals 20%, enterprises 12%) and any 15% global minimum tax rate for MNE groups (old file said "proposed from 2025").

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tw-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tw-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
