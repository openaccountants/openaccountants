---
name: gh-cross-border
description: >
  Use this skill for Ghana cross-border tax in tax year 2026: residence of individuals, companies, partnerships and trusts, the withholding rates on payments to residents and non-residents, final withholding, notice of non-resident contracts, foreign tax credit, the double taxation agreements Ghana lists, repatriated branch profits, 3% and 10% withholding on realisation of assets, and the monthly DT 110 return. VAT on imports of services sits in ghana-vat. Trigger on "Ghana withholding tax", "WHT Ghana", "non-resident Ghana", "double tax treaty Ghana", "dividend withholding Ghana", "service fees to foreign company Ghana". Use it for any payment crossing the Ghana border.
version: 0.1
jurisdiction: GH
category: cross-border
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Cross-Border Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Law: Income Tax Act, 2015 (Act 896) as amended. The GRA table was last edited in 2022; each rate was read there, and later statute changes are listed under Sources.

## Who this applies to

Residents paying non-residents, non-residents earning from Ghana, and residents with foreign income. Residence tests for individuals are in [ghana-pit](ghana-pit.md), for companies in [gh-corporate-income-tax](gh-corporate-income-tax.md). A partnership is resident if any partner lived in Ghana during the year. A trust is resident if established in Ghana, if a trustee is resident, or if a resident directs senior decisions ([Act 896 s.101](https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf)).

## Rates, bands and thresholds

| Payment to a non-resident | Rate | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Dividends | 8% | Final | 2026 | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ |
| Interest | 8% | Excluding individuals | 2026 | same |
| Management and technical service fees | 20% | Final unless through a Ghanaian permanent establishment | 2026 | same |
| Goods, works or any services | 20% | Contract with a non-resident | 2026 | same |
| Royalties, natural resource payments, rents | 15% | Final | 2026 | same |
| Telecommunications and transport income | 15% | Final | 2026 | same |
| Petroleum subcontractors | 15% | Final | 2026 | same |
| Repatriated branch after-tax profits | 8% | Branch | 2026 | same |
| General insurance premiums | 5% | Final | 2026 | same |
| Asset or liability realisation | 10% of consideration | Resident payer not an individual (s.116A) | 2026 | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf |

| Payment to a resident | Rate | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Dividends | 8% | Final | 2026 | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ |
| Interest | 8% | Not to individuals or resident financial institutions | 2026 | same |
| Rent, residential | 8% | | 2026 | same |
| Rent, non-residential | 15% | | 2026 | same |
| Invigilators, examiners, part-time teachers or lecturers, endorsement fees | 10% | Individuals | 2026 | same |
| Directors, managers, board members, trustees | 20% | Resident individuals | 2026 | same |
| Commission to insurance, sales, canvassing and lotto agents | 10% | Individuals | 2026 | same |
| Services | 7.5% | By an entity, above GHS 2,000 a year; general services by an individual | 2026 | same |
| Goods | 3% | Above GHS 2,000 a year | 2026 | same |
| Works | 5% | Above GHS 2,000 a year | 2026 | same |
| Unprocessed precious minerals | 3% | | 2026 | same |
| Petroleum subcontractors | 7.5% | Final | 2026 | same |
| Royalty, natural resource payments | 15% | | 2026 | same |
| Asset or liability realisation | 3% of consideration | Resident payer not an individual (s.116A) | 2026 | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf |
| Lottery winnings | 10% of gross winnings | End of each game | 2026 | same |

## The base

Withhold on the gross payment. Payments by an individual outside a business, employee pay, interest to a resident financial institution and exempt amounts are outside investment-return withholding ([GRA](https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/)).

Final payments are not taxed again: dividends by a resident company, rent by a resident individual, rent outside a letting business, payments to non-residents other than through a Ghanaian permanent establishment, petroleum subcontractor payments, and examination and endorsement fees. For anything else the payee claims a credit.

Treaties: GRA lists Belgium, Czech Republic, Denmark, France, Germany, Italy, Mauritius, Morocco, Netherlands, Qatar, Singapore, South Africa, Switzerland and the United Kingdom ([GRA](https://gra.gov.gh/double-taxation-agreements/)). Read the treaty itself for the rate. A treaty rate needs the recipient to qualify.

Foreign tax credit: resident other than a partnership, separately by income source, capped at the average Ghanaian rate on that income (s.112).

## Deadlines and filing

| Obligation | Date | Official URL |
|---|---|---|
| Notice of a contract with a non-resident | Within 30 days of the contract date | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ |
| Withholding statement and payment | Within 15 days after the month end | same |
| Withholding certificate | To the payee | same |

**Monthly return:**

1. Log in at www.etax.gra.gov.gh ([ITAS](https://gra.gov.gh/itas-faqs/)).
2. Open the Withholding Tax return, DT 110, for the month.
3. Upload the DT 110 items file, giving each payee, payment and rate.
4. Submit, keep the acknowledgement, pay through Ghana.gov.
5. Give each payee a certificate. Taxpayers attach them to annual returns.

## Penalties and interest

A withholding agent who fails to withhold is liable for the tax and may recover it from the payee ([GRA](https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/)). Late return: GHS 500 plus GHS 10 a day. Late payment: 125% of the Bank of Ghana policy rate, compounded monthly ([Act 915](https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf)).

## Cross-border points

- Imported services and digital services also carry VAT: see [ghana-vat](ghana-vat.md).
- Related-party pricing: see [gh-transfer-pricing](gh-transfer-pricing.md).
- A person who stops being resident is treated as realising assets at market value on that date; a person who becomes resident takes market value as cost (Act 896 s.102(3) to (5), not for domestic assets, s.102(6)).

## Two worked examples that recompute

**Example 1: service fee abroad.** A Ghana company owes a UK consultant GHS 100,000 under no treaty relief claim. It withholds 20%, GHS 20,000, pays GHS 80,000, and remits by the 15th of the next month.

```oa-check
name: Non-resident service fee
inputs:
  fee: 100000
steps:
  - wht: fee * 0.20
  - net: fee - wht
expected:
  wht: 20000.00
  net: 80000.00
```

**Example 2: branch or subsidiary?** After-tax profit of GHS 750,000 from GHS 1,000,000 at 25%. A branch pays 8% on repatriated profit, a subsidiary pays 8% on the dividend. On full distribution each costs GHS 60,000, so withholding does not decide it; retained profit does, as a branch pays only on what it repatriates and a subsidiary only on what it distributes.

```oa-check
name: Branch against subsidiary
inputs:
  profit: 1000000
steps:
  - after_tax: profit * 0.75
  - branch: after_tax * 0.08
  - subsidiary: after_tax * 0.08
  - gap: branch - subsidiary
expected:
  branch: 60000.00
  gap: 0.00
```

## Ask the client first

1. Payer and payee residence.
2. Type of payment and contract date.
3. Treaty country, and proof the recipient qualifies.
4. Any Ghanaian permanent establishment.
5. Whether the payer is an individual outside a business.

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA, Withholding Tax page (rates table, last edited 2022), page read in full | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ | 2026-11-01 |
| Income Tax (Amendment) Act, 2023 (Act 1094), whole act | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf | 2026-11-01 |
| Income Tax Act, 2015 (Act 896), OCR of scan; ss 33, 101, 102, 112, 121, 124, 125 read | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf | 2026-11-01 |
| Revenue Administration Act, 2016 (Act 915); ss 27 to 30, 46, 47, 70 to 73 read | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf | 2026-11-01 |
| GRA, Double Taxation Agreements page (country list), page read in full | https://gra.gov.gh/double-taxation-agreements/ | 2026-11-01 |
| GRA, ITAS FAQs, page read in full | https://gra.gov.gh/itas-faqs/ | 2026-11-01 |

Not yet confirmed: (1) Treaty rates and in-force status: GRA page lists countries only, under a heading on status; treaties were not read. (2) GRA withholding table dates from 2022; changes in Acts 1066, 1071 and any later act were not read, and the Act 1178 notice mentions only individual bands and MTS. The Finance Ministry 2025 report says Act 1129 abolished a 1.5% withholding on unprocessed gold by small-scale miners; Act 1129 itself was not read, and the 3% row may be affected for that gold. (3) The DT 110 screen layout on ETAX. (4) The GRA form list shows an older Excel DT 110; the upload format may differ on ETAX.

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
