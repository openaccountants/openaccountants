---
name: bn-vat-gst
description: "Brunei VAT and GST position for 2026. Brunei Darussalam has no value-added tax, goods and services tax or general sales tax, so there is no registration threshold, no return, no reverse charge and nothing to charge on invoices. Explains what does apply to sales and purchases instead (customs import duty and excise administered by the Royal Customs and Excise Department, stamp duty on listed instruments, and withholding tax when a Brunei payer buys services from a non-resident). Use for questions like Brunei VAT rate, Brunei GST registration, sales tax in Brunei, do I charge VAT to a Brunei customer or VAT on imports into Brunei."
version: 1.1
jurisdiction: BN
category: international
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Brunei VAT and GST v1.1

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
| Stamp duty adjudication fee | BND 25 when applying for the Collector's adjudication of duty on an instrument | 2026 | same |
| Customs advance ruling on tariff classification | Free of charge. Apply before the goods arrive. Customs indicates 9 days per item and normally within 30 days. An applicable trade agreement may set a deadline | 2026 | https://www.mof.gov.bn/rced_tariff-and-classification/ |
| Withholding on technical services, management fees and royalties paid to non-residents | 10% domestic withholding on covered Brunei-source payments, subject to the payee's local activities, permanent establishment and applicable treaty | 2026 | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ |

## The base

Nothing is taxable for VAT or GST. What a business should still check on each transaction:

1. **Imports of goods.** Customs import duty, and excise on specified goods, collected by the Royal Customs and Excise Department on importation under the customs tariff. Rates depend on the tariff classification; get an advance ruling if unsure. Use the current Brunei Darussalam Tariff and Trade Classification and check any applicable origin preference, later amendment or exemption.
2. **Imports of services from a non-resident.** Brunei imposes no VAT. Withholding can apply to payments by any person for covered technical or management services, use of knowledge, royalties, rent of movable property, loan interest or directors' remuneration. Check the payment's source and the payee's Brunei trade or permanent establishment. The ordinary remittance period is 14 days ([bn-corporate-income-tax](bn-corporate-income-tax.md)).
3. **Documents.** Check Schedule 1 for chargeable instruments. Stamp domestic instruments before execution under the general rule in section 34. Section 39 ordinarily allows stamping within 14 days after first execution in Brunei without penalty. For chargeable instruments executed wholly abroad, the ordinary period is 30 days after first receipt in Brunei. Bills of exchange, cheques and promissory notes drawn abroad have a separate rule.
4. **Bookkeeping.** Record sales and purchases gross; there is no input or output tax to split out. Foreign invoices showing another country's VAT: that VAT is a cost unless recoverable in that country.

## Deadlines and filing

There are no Brunei VAT or GST filings. The ordinary withholding deadline is 14 days after payment. Check the stamping rules above for each instrument and submit customs declarations for covered imports.

## Penalties and interest

There are no Brunei VAT or GST penalties. An instrument not duly stamped is generally inadmissible in civil proceedings until duty and any applicable penalty are paid, subject to section 44. If withholding remains unpaid 14 days after the underlying payment, the penalty is 5%. If still unpaid after 30 days, an additional 1% per completed month applies, capped at 15% of the withholding tax ([bn-corporate-income-tax](bn-corporate-income-tax.md)).

## Cross-border points

- **Exporting to Brunei.** No Brunei VAT to register for or charge, whether goods or digital services. The Brunei customer may bear customs duty on goods.
- **Brunei business buying from Singapore, Malaysia and so on.** The foreign supplier's own VAT/GST rules decide whether it charges its tax; Brunei has nothing to self-account.
- **Approved exports.** The final income tax under section 8A is 1% of covered gross export proceeds. Check the statutory approval and turnover rules.

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

**Example 2 (decision). A Brunei company pays a Singapore company BND 5,000 for management services.** Assume a service fee only and that domestic withholding applies to the Brunei-source payment. There is no VAT or reverse charge. At payment, withhold the domestic 10% (BND 500), pay BND 4,500 to the supplier and remit BND 500 within 14 days. If the supplier is a Singapore treaty resident with no Brunei permanent establishment, Article 7 gives Singapore exclusive taxing rights on the service profits. Final Brunei tax after treaty relief is nil. Claim the BND 500 refund from the Revenue Division with evidence of treaty residence, the payment and the contract.

```oa-check
name: Brunei payment for management services to a non-resident
inputs:
  fee: 5000
  wht_rate: 0.10
steps:
  - vat: fee * 0
  - wht: fee * wht_rate
  - paid_to_supplier: fee - wht
  - final_brunei_tax_with_treaty_relief: fee * 0
expected:
  vat: 0.00
  wht: 500.00
  paid_to_supplier: 4500.00
  final_brunei_tax_with_treaty_relief: 0.00
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

| Stamp Act, Chapter 34 | Sections 31, 34–39 and 44 on adjudication, deadlines and admissibility, and Schedule 1 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-34-2022-ED-STAMP-ACT-ACT.pdf#page=29 | 2026-11-22 |
| Income Tax Act, Chapter 35 | Section 8A on approved exports, sections 9(5), 35 and 37–37B on withholding | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf | 2026-11-22 |
| Brunei–Singapore agreement | Articles 5 and 7 on permanent establishments and business profits | https://www.agc.gov.bn/wp-content/uploads/2026/08/S-96-2006-E.pdf#page=5 | 2026-11-22 |
| Revenue Division withholding relief | Claim process, certificate of residence and supporting documents | https://www.mof.gov.bn/div_revenue_withholdingoftax_claimofrelief/ | 2026-11-22 |
| Revenue Division withholding tax ruling | Section 19 on deduction at domestic rates and treaty refund | https://www.mof.gov.bn/wp-content/uploads/2025/10/PR_004-2017_Public_Ruling_on_Witholding_of_Tax.pdf | 2026-11-22 |
| Royal Customs and Excise Department | Current tariff classification and later notices | https://www.customs.gov.bn/ref-rced/ | 2026-11-22 |

Not yet confirmed: transaction-specific duty rates without the tariff line and origin of the goods or the Schedule 1 entry and execution dates for the instrument.
