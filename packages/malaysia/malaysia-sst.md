---
name: malaysia-sst
description: Use this skill whenever asked to prepare, review or classify transactions for a Malaysia Sales and Service Tax (SST) return SST-02 in 2026. Trigger on phrases like Malaysia SST, sales tax Malaysia, service tax Malaysia, SST-02, SST-02A, MySST, RMCD, JKDM, Kastam, imported taxable service, rental service tax, construction service tax, or any request involving Malaysian sales tax or service tax. SST is not a VAT and gives no input tax credit. Covers sales tax at 5% and 10% on manufacturers, service tax at 8% with the 6% services and the RM25 card charge, the July 2025 scope expansion (rental, construction, financial, healthcare, education, beauty), registration thresholds, the bi-monthly SST-02 return, imported services, late payment penalties, bad debts and records. Calendar 2026.
version: "3.0"
jurisdiction: MY
tax_year: 2026
tax_year_notes: "Calendar 2026 taxable periods. Rates and thresholds read on the RMCD MySST site and gazetted orders on 14 November 2026."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
depends_on:
  - vat-workflow-base
---

# Malaysia Sales and Service Tax (SST), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Malaysia.

## Scope

Malaysia has no VAT or GST (GST was repealed in 2018). It has two single-stage taxes administered by the Royal Malaysian Customs Department (RMCD, JKDM) on the MySST portal, https://mysst.customs.gov.my:

- **Sales tax** (Sales Tax Act 2018, Act 806): charged by registered manufacturers on taxable goods they make and sell, and on imports. Retailers and wholesalers do not charge it.
- **Service tax** (Service Tax Act 2018, Act 807): charged by registered providers of the taxable services listed in the First Schedule of the Service Tax Regulations 2018, and accounted for by business recipients of imported taxable services.

**There is no input tax credit.** SST paid on purchases is a cost. Manufacturers reduce sales tax on inputs through exemptions applied at purchase (Schedules A, B and C of the exemption order), not through a credit.

Out of scope: e-invoicing (`malaysia-einvoice`); income tax (`my-income-tax`); Free Zones and licensed manufacturing warehouses, petroleum specific rates, foreign digital service providers' own registration (see "When to refuse or refer").

## Ask the client first

1. **Which tax?** Registered for sales tax, service tax, or both; registration numbers.
2. **Manufacturer?** Does the business manufacture taxable goods (sales tax), or only trade them (no sales tax on output)?
3. **Which services?** Map each service to the First Schedule group and item, including the July 2025 additions (rental or leasing, construction, financial, private healthcare, education, beauty).
4. **Value of taxable sales or services** for the last 12 months and the next 12 months (registration threshold test).
5. **Exemption approvals** (Schedule A, B or C certificates) held.
6. **Taxable period**: the standard two months, or a period approved by the Director General.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Sales tax rate unknown for a taxable good | 10% (goods not in the rate order or the exemption order are at 10%) |
| Service tax rate unknown for a taxable service | 8% |
| Manufacturer or trader unknown | Trader: no sales tax on output |
| Service not mapped to the First Schedule | Not taxable, flag it |
| SST paid on inputs | Cost, no credit |
| Supplier billing entity (Malaysian or foreign) unknown | Treat as imported, account for service tax, flag it |

Flag for review any single transaction over RM50,000 or any default that moves tax by more than RM2,000.

## The method, step by step

1. **Classify each sale.** Taxable goods made by the client (sales tax), a taxable service (service tax), an export of goods (exempt from sales tax), or outside SST (salaries, dividends, loans, internal transfers, government fees).
2. **Apply the rate** from the table below to the sale value (sales tax on the sale value of the goods; service tax on the price, value, premium or takaful contribution under section 9 of Act 807).
3. **Imported taxable services.** A registered person accounts for service tax on services bought from outside Malaysia in its SST-02 for the taxable period; a business that is not registered declares on SST-02A through MySST. The tax is a cost.
4. **Adjust** for credit notes, and claim bad debt relief within 6 years of the sale where the Director General's conditions are met; repay it if the debt is later recovered.
5. **File SST-02** for each taxable period by the last day of the month after the period ends, even if no tax is due, and pay by the same date by FPX.
6. **Late payment** adds 10% for the first 30 days, a further 15% for each of the next two 30-day periods, up to 40% after 90 days.
7. **Records**: keep for 7 years, in Malay or English, in Malaysia unless the Director General permits otherwise.

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Service tax, general rate (from 1 March 2024) | 8% | https://mysst.customs.gov.my/faq-services-tax/ |
| Service tax on food and beverage, telecommunications, parking and logistics | 6% | same |
| Service tax on credit card or charge card | RM25 a card | same |
| Service tax on construction work services (from 1 July 2025) | 6% | https://mysst.customs.gov.my/faq-expansion-of-service-tax-scope-2025/ |
| Service tax on private healthcare, traditional and complementary medicine and allied health services (from 1 July 2025) | 6% | same |
| Service tax on rental or leasing services (from 1 July 2025) | 8% | same |
| Service tax on beauty treatment services | 8% | same |
| Registration threshold, rental or leasing | RM500,000 in 12 months | same |
| Registration threshold, financial services | RM500,000 in 12 months | same |
| Registration threshold, beauty treatment | RM500,000 in 12 months | same |
| Registration threshold, construction work (excluding residential buildings) | RM1,500,000 in 12 months | same |
| Registration threshold, private healthcare and related services | RM1,500,000 in 12 months | same |
| Sales tax rates (from 1 July 2025) | 5%, 10%, or specific rates; goods not listed in the rate or exemption orders at 10% | https://mysst.customs.gov.my/faq-transition-of-sales-tax-rate-changes-2025/ |
| Registration threshold, manufacturer of taxable goods | RM500,000 in 12 months | same |
| SST-02 due date | Last day of the month after the taxable period | https://mysst.customs.gov.my/faq-services-tax/ |
| Late payment penalty | 10% first 30 days; 15% second; 15% third; maximum 40% | same |
| Bad debt relief window | 6 years from the sale | same |
| Record keeping | 7 years | same |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Threshold test | Historical: this month plus the 11 before. Future: this month plus the 11 after. Either reaching the threshold triggers registration |
| Manufacturer sells goods for export | Exempt from sales tax; report as exempt in SST-02 |
| Subcontract processing for another manufacturer | Manufacturing or a service? Flag and ask |
| Goods and services on one invoice | Can they be separately invoiced? Flag and ask |
| SaaS or cloud bought online | Check the billing entity: a Malaysian entity charging service tax is a cost; a foreign entity means an imported taxable service |
| Streaming or apps for staff from a foreign provider | The foreign digital service provider may already charge service tax; check the invoice |
| Bank fees | Fee-based financial services became taxable at 8% from 1 July 2025 unless excluded; for the client it is a cost either way, never a credit |
| Electricity, water, telecoms, insurance, professional fees, platform commissions (Shopee, Lazada, Grab, Foodpanda) | Cost, with any service tax embedded; nothing goes into the client's return |
| Salaries, EPF, SOCSO, EIS, LHDN, RMCD, SSM payments, dividends, loans, own transfers | Outside SST, exclude |
| Cash withdrawal | Ask; default exclude |
| Residential building construction | Excluded from the construction service tax |
| GST refunds from before September 2018 | Refer |

## Worked cases

Case 1, SST-02 for January and February 2026, filed late. A registered manufacturer that also provides consultancy and runs a cafe has, for the period: goods at 10% RM80,000; goods at 5% RM20,000; consultancy RM30,000 (8%); cafe sales RM5,000 (6%). Sales tax RM8,000 + RM1,000 = RM9,000. Service tax RM2,400 + RM300 = RM2,700. Total due RM11,700 by 31 March 2026. Paid 45 days late: 10% + 15% = 25% penalty, RM2,925.

```oa-check
name: SST-02 Jan to Feb 2026, paid 45 days late
inputs:
  goods_10: 80000
  goods_5: 20000
  consultancy: 30000
  cafe: 5000
steps:
  - sales_tax: goods_10 * 0.10 + goods_5 * 0.05
  - service_tax: consultancy * 0.08 + cafe * 0.06
  - total: sales_tax + service_tax
  - penalty: total * (0.10 + 0.15)
expected:
  sales_tax: 9000.00
  service_tax: 2700.00
  total: 11700.00
  penalty: 2925.00
```

Case 2, decision: must a landlord register for service tax now? A company letting commercial units had rental income of RM520,000 in the 12 months to the end of May 2026 (historical method) and expects RM480,000 in the next 12 months. The historical test alone is over the RM500,000 rental threshold, so it must register even though the future test is under. Once registered, rent of RM90,000 for July and August 2026 carries 8% service tax, RM7,200, due by 30 September 2026. Had the trailing 12 months been RM499,000, and the next 12 months also under RM500,000, it would not have to register and would charge nothing.

```oa-check
name: Rental service tax registration test and first period
inputs:
  trailing_12: 520000
  forward_12: 480000
  threshold: 500000
  period_rent: 90000
steps:
  - over_historical: max(trailing_12 - threshold, 0)
  - over_future: max(forward_12 - threshold, 0)
  - service_tax: period_rent * 0.08
expected:
  over_historical: 20000
  over_future: 0
  service_tax: 7200.00
```

## When to refuse or refer

| Code | Trigger | Message |
| --- | --- | --- |
| R-MY-1 | Client in a Free Zone or licensed manufacturing warehouse | "Free Zone and LMW operations have special SST treatment. Please escalate to a licensed tax agent." |
| R-MY-2 | Petroleum or other specific-rate sales tax | "Specific sales tax rates need specialist analysis. Please escalate." |
| R-MY-3 | Foreign entity supplying digital services to Malaysian consumers | "Foreign digital service provider registration has its own rules. Please escalate." |
| R-MY-4 | Unclaimed GST input credits from before September 2018 | "GST transitional provisions have largely expired. Please escalate for any remaining claim." |
| R-MY-5 | Designated areas (Labuan, Langkawi, Tioman) or special areas | "Designated and special areas have their own orders. Please escalate." |

## Filing and payment

| Step | Detail |
| --- | --- |
| Register | MySST, once a threshold is reached (or voluntarily where allowed) |
| Taxable period | Two months, or a period approved by the Director General (for example aligned to the financial year) |
| Return | SST-02 on MySST, by the last day of the month after the period, including nil returns |
| Imported services, not registered | SST-02A on MySST |
| Payment | FPX on MySST, or cheque to the Customs Processing Centre |
| Working paper | Per `vat-workflow-base`: sales tax by rate and exempt; service tax by rate; imported services; adjustments; net payable |

Bank statements (Maybank, CIMB, Public Bank and others, DD/MM/YYYY, MYR): exclude internal transfers and payroll; split platform settlements (Grab, Shopee) into platform fee and underlying sale.

## Completion checklist

- Each sale mapped to sales tax, service tax (with First Schedule item), export or outside scope.
- Threshold tested both ways for every service type the client provides.
- Rates checked against the table, including the 6% services and construction.
- Imported services declared on the right form.
- No input credit claimed.
- Due date and any late payment penalty stated.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the service tax rates (8%, 6% services, RM25 card), threshold methods, SST-02 due date, late payment penalty steps, records and bad debts | https://mysst.customs.gov.my/faq-services-tax/ | 2026-11-14 |
| Read for the July 2025 expansion: rental 8% and RM500,000, construction 6% and RM1,500,000, healthcare 6% and RM1,500,000, financial services RM500,000, beauty 8% and RM500,000 | https://mysst.customs.gov.my/faq-expansion-of-service-tax-scope-2025/ | 2026-11-14 |
| Read for the sales tax rates of 5%, 10% and specific rates from 1 July 2025 and the RM500,000 manufacturer threshold | https://mysst.customs.gov.my/faq-transition-of-sales-tax-rate-changes-2025/ | 2026-11-14 |
| Read for the Service Tax (Rate of Tax) (Amendment) Order 2024, P.U. (A) 64/2024: 8% from 1 March 2024 with 6% kept for F&B, telecoms, parking and logistics | https://mysst.customs.gov.my/wp-content/uploads/2025/03/PERINTAH-CUKAI-PERKHIDMATAN-KADAR-CUKAI-PINDAAN-2024.pdf | 2026-11-14 |
| Read for the Service Tax (Amendment) Regulations 2025, P.U. (A) 172/2025: thresholds in the First Schedule items | https://mysst.customs.gov.my/wp-content/uploads/2025/07/Peraturan-Peraturan-CP-Pindaan-2025.pdf | 2026-11-14 |
| Read for the Sales Tax (Rate of Sales Tax) (Amendment) Order 2025, P.U. (A) 199/2025, in force 1 July 2025 | https://mysst.customs.gov.my/wp-content/uploads/2025/07/2-PUA-199.2025.pdf | 2026-11-14 |
| Read for imported taxable services: registered persons declare in SST-02, others on SST-02A | https://mysst.customs.gov.my/wp-content/uploads/2025/02/Information-about-Imported-Taxable-Services.pdf | 2026-11-14 |
| Read for the list of 2026 orders, regulations and policies issued by RMCD | https://mysst.customs.gov.my/announcements/ | 2026-11-14 |

Not yet confirmed: whether a Budget 2026 change altered the rental or leasing threshold after the July 2025 FAQ (the 2026 orders listed on MySST, such as the Service Tax (Rate of Tax) (Amendment) Order 2026 of 17 March 2026, were not opened); the general RM500,000 service tax threshold and the RM1,500,000 F&B threshold in the old file (in the Service Tax Regulations First Schedule, not checked item by item); the SST-02 box labels (A1 to C5 in the old file) against the current SST-02 guideline; the 30-day payment period for imported services in the old file; the 6-year limit for credit note adjustments in the old file.
