---
name: bn-vat-gst
description: "Brunei VAT and GST position for 2026. Brunei Darussalam has no value-added tax, goods and services tax or general sales tax, so there is no registration threshold, no return, no reverse charge and nothing to charge on invoices. Explains what does apply to sales and purchases instead (customs import duty and excise administered by the Royal Customs and Excise Department, stamp duty on listed instruments, and withholding tax when a Brunei payer buys services from a non-resident). Use for questions like Brunei VAT rate, Brunei GST registration, sales tax in Brunei, do I charge VAT to a Brunei customer or VAT on imports into Brunei."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bn-vat-gst"
  jurisdiction: "BN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Brunei VAT and GST v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Any business or individual asking whether VAT, GST or sales tax applies to supplies in, into or out of Brunei Darussalam in 2026.

**The rule.** Brunei has no VAT, GST or general sales tax. The Revenue Division of the Ministry of Finance and Economy administers income tax (on companies), withholding tax and stamp duty, and lists only the Income Tax Act (Chapter 35), the Income Tax (Petroleum) Act (Chapter 119) and the Stamp Act (Chapter 34) with their subsidiary orders as the Acts it administers. No VAT or GST Act appears there. Import duty and excise are customs matters for the Royal Customs and Excise Department.

So:

- No VAT/GST registration, no threshold, no tax number for VAT.
- No VAT/GST on invoices to Brunei customers, and no VAT/GST return.
- No reverse charge on imported services.
- A foreign seller supplying Brunei customers charges no Brunei VAT (its own country's rules on exports still apply).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| VAT, GST or general sales tax | None: not among the Acts the Revenue Division administers (income tax, petroleum income tax, stamp duty) | 2026 | https://www.mof.gov.bn/div_revenue_taxresources_relevantacts/ |
| Taxes the Revenue Division administers | Income tax, withholding of tax and stamp duty | 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ |
| Stamp duty | Ad valorem or fixed duty on instruments in Schedule 1 of the Stamp Act (Chapter 34): transfers of property and shares, leases, bonds, contract notes; Memorandum and Articles and share certificates on incorporation no longer stamped (from 4 May 2017) | 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_stampduty/ |
| Stamp duty adjudication fee | BND 25 per instrument | 2026 | same |
| Customs advance ruling on tariff classification | Free of charge; about 9 days per item, normally within 30 days | 2026 | https://www.mof.gov.bn/rced_tariff-and-classification/ |
| Withholding on technical services, management fees and royalties paid to non-residents | 10% (income tax, not VAT; rates owned by bn-corporate-income-tax) | 2026 | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ |

## The base

Nothing is taxable for VAT or GST. What a business should still check on each transaction:

1. **Imports of goods.** Customs import duty, and excise on specified goods, collected by the Royal Customs and Excise Department on importation under the customs tariff. Rates depend on the tariff classification; get an advance ruling if unsure. Rates are not given here (see Not yet confirmed).
2. **Imports of services from a non-resident.** No VAT. But if the Brunei payer is a company or permanent establishment and the payment is for technical services, use of knowledge, management, royalties, rent of movable property, loan interest or directors' fees, income tax must be withheld and paid within 14 days ([bn-corporate-income-tax](bn-corporate-income-tax.md)).
3. **Documents.** Leases, property and share transfers and loan instruments need stamping before signing if executed in Brunei, or within 30 days of first receipt in Brunei if executed abroad.
4. **Bookkeeping.** Record sales and purchases gross; there is no input or output tax to split out. Foreign invoices showing another country's VAT: that VAT is a cost unless recoverable in that country.

## Deadlines and filing

None for VAT or GST. Related deadlines: withholding tax within 14 days of payment; stamp duty before execution (Brunei) or within 30 days of receipt (abroad); customs declarations on importation.

## Penalties and interest

None for VAT or GST. An instrument not duly stamped is not admissible as evidence in civil proceedings and attracts a stamp duty penalty; late withholding tax attracts 5% plus 1% a month up to 15% ([bn-corporate-income-tax](bn-corporate-income-tax.md)).

## Cross-border points

- **Exporting to Brunei.** No Brunei VAT to register for or charge, whether goods or digital services. The Brunei customer may bear customs duty on goods.
- **Brunei business buying from Singapore, Malaysia and so on.** The foreign supplier's own VAT/GST rules decide whether it charges its tax; Brunei has nothing to self-account.
- **Approved exporters** may be taxed at a flat 1% income tax on approved exports (income tax, not VAT).

## Two worked examples that recompute

**Example 1. Brunei company invoices a local client BND 10,000 for consulting.** VAT nil. The invoice total is BND 10,000, all of it revenue for corporate income tax.

```oa-check
name: Brunei local sale, no VAT
inputs:
  fee: 10000
steps:
  - vat: fee * 0
  - invoice_total: fee + vat
  - revenue: invoice_total
expected:
  vat: 0.00
  invoice_total: 10000.00
  revenue: 10000.00
```

**Example 2 (decision). A Brunei company pays a Singapore company BND 5,000 for management services: VAT or withholding?** No VAT and no reverse charge. Management fees to a non-resident carry 10% withholding under section 9(5)(c) and 37A: withhold BND 500, pay the non-resident BND 4,500 and pay BND 500 to the Collector within 14 days, unless the Brunei and Singapore agreement reduces it and a certificate of residence is held. The figure that decides is the nature of the payment, not any VAT rule.

```oa-check
name: Brunei payment for management services to a non-resident
inputs:
  fee: 5000
  wht_rate: 0.10
steps:
  - vat: fee * 0
  - wht: fee * wht_rate
  - paid_to_supplier: fee - wht
expected:
  vat: 0.00
  wht: 500.00
  paid_to_supplier: 4500.00
```

## Ask the client first

1. Is the question about goods or services?
2. Who is the supplier and who is the customer, and where is each resident?
3. For services bought from abroad, what exactly is being paid for (management, technical, royalty, interest)?
4. Are goods being imported into Brunei (customs and excise)?
5. Does the deal involve a lease, a property or share transfer, or a loan document (stamp duty)?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Revenue Division, relevant Acts | Read for the full list of Acts the Revenue Division administers (income tax, petroleum income tax, stamp duty, incentives, accounting); no VAT or GST Act listed | https://www.mof.gov.bn/div_revenue_taxresources_relevantacts/ | 2026-11-14 |
| Revenue Division, types of taxes: income tax | Read for the taxes administered and the 1% export tax | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, types of taxes: stamp duty | Read for the scope of stamp duty, the 2017 incorporation change, the BND 25 adjudication fee and the time of stamping | https://www.mof.gov.bn/div_revenue_typesoftaxes_stampduty/ | 2026-11-14 |
| Royal Customs and Excise Department, tariff and classification | Read for advance rulings, timing and the nil fee | https://www.mof.gov.bn/rced_tariff-and-classification/ | 2026-11-14 |
| Revenue Division, withholding tax rates | Read for the 10% management fee rate in Example 2 | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ | 2026-11-14 |

Not yet confirmed: customs import duty and excise rates by tariff line (the customs tariff was not opened); the stamp duty schedule rates and penalty amounts (the Stamp Act Schedule 1 was not opened); any announcement after 14 November 2026 of a future VAT or GST.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bn-vat-gst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bn-vat-gst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
