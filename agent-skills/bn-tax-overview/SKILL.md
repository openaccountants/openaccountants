---
name: bn-tax-overview
description: "Overview of the Brunei Darussalam tax system for 2026 (year of assessment 2026). Brunei taxes only companies on income (18.5% after a threshold, preceding-year basis), with withholding on certain payments to non-residents, stamp duty on listed documents, customs and excise on goods, and SPK retirement contributions on payroll. There is no personal income tax, no capital gains tax and no VAT or GST. Use to orient any Brunei tax question and to pick the right Brunei skill; the detailed figures live in the linked skills."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bn-tax-overview"
  jurisdiction: "BN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Brunei Tax Overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone with a Brunei question in 2026: individuals, sole proprietors, companies, foreign businesses paying or selling into Brunei, employers.

| Tax | Applies to | Skill |
|---|---|---|
| Corporate income tax and withholding tax | Companies; Brunei payers of non-residents | [bn-corporate-income-tax](bn-corporate-income-tax.md) |
| Personal income tax | Nobody: none levied | [bn-income-tax](bn-income-tax.md) |
| VAT, GST, sales tax | Nobody: none exists | [bn-vat-gst](bn-vat-gst.md) |
| SPK retirement contributions | Employers and citizen or PR employees below 60 | [bn-payroll-social](bn-payroll-social.md) |
| Company formation | Founders | [bn-company-formation](bn-company-formation.md) |
| Petroleum income tax (55%) | Oil and gas exploration and production | Not covered: refer |

Authorities: the Revenue Division, Ministry of Finance and Economy (MOFE) for income tax, withholding and stamp duty; the Royal Customs and Excise Department for import duty and excise; Tabung Amanah Pekerja (TAP) for SPK; the Registry of Companies and Business Names (ROCBN) for companies. Currency: Brunei dollar (BND).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Corporate income tax | 18.5% of chargeable income (YA 2015 onward) | YA 2026 | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ |
| Small company threshold | First BND 100,000 at 25% of the rate, next BND 150,000 at 50% (section 35(4)); new companies: first BND 100,000 exempt for 3 YAs (section 35(5)) | YA 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ |
| Oil and gas exploration and production profits | 55% (Income Tax (Petroleum) Act, Chapter 119) | YA 2026 | same |
| Personal income, business names, capital gains | No tax levied | 2026 | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ |
| Withholding on payments to non-residents | 2.5% loan interest; 10% royalties, technical services, management fees, rent of movable property, non-resident directors | 2026 | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ |
| Company return | By 30 June each year; ECI within 3 months of the accounting period end | YA 2026 | https://www.mof.gov.bn/div_revenue_paymentoftax/ |
| SPK, employee | 8.5% of wages | 2026 | https://www.tap.com.bn/spk-members-contribution |
| SPK, employer | BND 57.50 to 10.5% by salary group | 2026 | https://www.tap.com.bn/employers-responsibilities-contribution |
| Stamp duty | Ad valorem or fixed duty on Stamp Act Schedule 1 instruments | 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_stampduty/ |
| VAT or GST | None | 2026 | https://www.mof.gov.bn/div_revenue_taxresources_relevantacts/ |

## The base

- **Companies** are taxed on income accruing in, derived from or received in Brunei, under the Income Tax Act (Chapter 35), on a preceding-year basis: YA 2026 taxes the basis period ending in 2025. Dividends from Brunei-taxed companies are excluded. Capital gains are not taxed.
- **Individuals** pay no income tax on any income, and file no return.
- **Payroll** carries no PAYE, only SPK for citizens and permanent residents.
- **Goods** imported bear customs duty and, for specified goods, excise.

## Deadlines and filing

- Company: ECI within 3 months after the accounting period end; return and payment by 30 June; through OCP.
- Withholding: within 14 days of the payment to the non-resident.
- SPK: by the 15th of the following month, through e-Amanah.
- Stamp duty: before execution in Brunei, or within 30 days of first receipt if executed abroad.

## Penalties and interest

Late company tax: 5%, then 1% per completed month up to an additional 12%. Late withholding: 5%, then 1% a month up to 15%. Failure to file a company return: BND 10,000 fine. Detail in [bn-corporate-income-tax](bn-corporate-income-tax.md).

## Cross-border points

Brunei has avoidance of double taxation agreements with 19 jurisdictions listed by the Revenue Division (including Singapore, Malaysia, Indonesia, China, Japan, the United Kingdom, Hong Kong and Cambodia). A company is non-resident if its control and management is not exercised in Brunei. Treaty use and withholding: [bn-corporate-income-tax](bn-corporate-income-tax.md).

## Two worked examples that recompute

**Example 1. Existing company, chargeable income BND 180,000.** BND 100,000 x 18.5% x 25% = BND 4,625; BND 80,000 x 18.5% x 50% = BND 7,400. Tax BND 12,025.

```oa-check
name: Brunei company, CI BND 180,000
inputs:
  ci: 180000
  rate: 0.185
steps:
  - band1: min(ci, 100000) * 0.25 * rate
  - band2: clamp(ci - 100000, 0, 150000) * 0.5 * rate
  - band3: max(ci - 250000, 0) * rate
  - tax: band1 + band2 + band3
expected:
  tax: 12025.00
```

**Example 2 (decision). A Singapore consultant asks whether to invoice a Brunei client through a Brunei sole proprietorship or directly from Singapore, fee BND 50,000 for technical services.** Through a Brunei business name: no Brunei income tax and no VAT. Directly from Singapore: the Brunei client, if a company, withholds 10% (BND 5,000) as a payment to a non-resident for technical services, subject to the Brunei and Singapore agreement. The figure that decides is the BND 5,000 withheld at source, against the cost of a Brunei registration (a sole proprietorship is open to citizens and residents; a foreigner would need a company, taxed at 18.5% after the threshold).

```oa-check
name: Brunei technical fee to a non-resident vs local business name
inputs:
  fee: 50000
steps:
  - wht_direct: fee * 0.10
  - tax_local_business_name: fee * 0
  - difference: wht_direct - tax_local_business_name
expected:
  wht_direct: 5000.00
  difference: 5000.00
```

## Ask the client first

1. Individual, sole proprietor, company or foreign business?
2. What is the transaction: profit, salary, payment abroad, import, property or share transfer?
3. Is the payee or payer resident in Brunei?
4. Is the business in oil and gas?
5. Are staff Brunei citizens or permanent residents?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Revenue Division, FAQ corporate tax | Read for the 18.5% rate, the 30 June return and the absence of tax on individuals, business names and capital gains | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ | 2026-11-14 |
| Revenue Division, types of taxes: income tax | Read for the section 35 thresholds, the 55% petroleum rate, preceding-year basis and dividend exclusion | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, withholding tax rates | Read for the withholding rates | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ | 2026-11-14 |
| Revenue Division, payment of tax | Read for ECI and return dates and penalties | https://www.mof.gov.bn/div_revenue_paymentoftax/ | 2026-11-14 |
| Revenue Division, relevant Acts | Read for the Acts administered (no VAT or GST Act) | https://www.mof.gov.bn/div_revenue_taxresources_relevantacts/ | 2026-11-14 |
| Revenue Division, stamp duty | Read for the scope and timing of stamp duty | https://www.mof.gov.bn/div_revenue_typesoftaxes_stampduty/ | 2026-11-14 |
| Revenue Division, double taxation agreements | Read for the list of 19 treaty partners | https://www.mof.gov.bn/div_revenue_internationaltaxation_adta/ | 2026-11-14 |
| TAP, SPK members' contribution and employer rates | Read for 8.5% and the employer table | https://www.tap.com.bn/employers-responsibilities-contribution | 2026-11-14 |

Not yet confirmed: customs and excise rates; stamp duty schedule rates; whether a foreign national may register a sole proprietorship (business name) in Brunei, which the decision in Example 2 assumes not; the currency peg with the Singapore dollar named in the old file (the Currency Interchangeability Agreement page was not opened).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bn-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bn-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
