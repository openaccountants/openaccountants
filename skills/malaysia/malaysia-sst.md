---
name: malaysia-sst
description: Use this skill whenever asked to prepare, review or classify transactions for a Malaysia Sales and Service Tax (SST) return SST-02 in 2026. Trigger on phrases like Malaysia SST, sales tax Malaysia, service tax Malaysia, SST-02, SST-02A, MySST, RMCD, JKDM, Kastam, imported taxable service, rental service tax, construction service tax, or any request involving Malaysian sales tax or service tax. SST has specific deductions and exemptions and no general VAT-style input credit. Covers sales tax at 5% and 10% on manufacturers, service tax at 8% with the 6% services and the RM25 card charge, the July 2025 scope expansion (rental, construction, financial, healthcare and education), registration thresholds, the separate SST-02 returns for sales and service tax, imported services, late payment penalties, bad debts and records. Calendar 2026.
version: "3.1"
jurisdiction: MY
tax_year: 2026
tax_year_notes: "Calendar 2026 taxable periods. Rates and thresholds read on the RMCD MySST site and gazetted orders through 22 November 2026."
last_updated: 2026-11-22
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

- **Sales tax** (Sales Tax Act 2018, Act 806): charged by registered manufacturers on taxable goods they make and sell, and on imports. Ordinary retail and wholesale sales are outside the manufacturer charge. Refer separate low-value goods rules for covered imported online sales.
- **Service tax** (Service Tax Act 2018, Act 807): charged by registered providers of the taxable services listed in the First Schedule of the Service Tax Regulations 2018, and accounted for by business recipients of imported taxable services.

**SST has no general VAT-style input credit.** Check purchase exemptions under Schedules A, B and C. A registered manufacturer may apply to deduct specified sales tax under Act 806 s. 41A. The return provides for specific deductions where the applicable relief permits them. [Act 806, s. 41A](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf), [SST-02, item 13](https://mysst.customs.gov.my/wp-content/uploads/2026/09/Borang-SST02.pdf#page=2).

Out of scope: e-invoicing (`malaysia-einvoice`); income tax (`my-income-tax`); Free Zones and licensed manufacturing warehouses, petroleum specific rates, foreign digital service providers' own registration (see "When to refuse or refer").

## Ask the client first

1. **Which tax?** Registered for sales tax, service tax, or both; registration numbers.
2. **Manufacturer?** Does the business manufacture taxable goods (sales tax), or only trade them?
3. **Which services?** Map each service to the First Schedule group and item, including the July 2025 additions (rental or leasing, construction, financial, private healthcare and education).
4. **Value of taxable sales or services** for the last 12 months and the next 12 months (registration threshold test).
5. **Exemption approvals** (Schedule A, B or C certificates) held.
6. **Taxable period**: the standard two months, or a period approved by the Director General.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Sales tax rate unknown for a good | Establish tariff classification and exemptions before applying a rate. |
| Service tax rate unknown | Resolve the prescribed service and any exemption before applying a rate. |
| Manufacturer or trader unknown | Confirm the business activity and registration before classifying output. |
| Service not yet mapped to the First Schedule | Hold classification until the applicable item and service facts are established. |
| SST paid on inputs | Generally a cost. Check specific deductions, exemptions and refunds. |
| Supplier billing entity unknown | Hold imported-service classification until the supplier location and taxable service are established. |

For internal working-paper review, flag any single transaction over RM50,000 or unresolved classification that could move tax by more than RM2,000.

## The method, step by step

1. **Classify each sale.** Taxable goods made by the client (sales tax), a taxable service (service tax), an export of goods (verify any direct-export exemption or drawback conditions), or outside SST (salaries, dividends, loans, internal transfers, government fees).
2. **Apply the rate** to the statutory taxable value. Domestic service tax is generally due when payment is received. For payment outstanding 12 months after the service was provided, apply the statutory due point on the following day unless an authorised accounting basis applies. [Act 807 ss. 9 and 11](https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf), [Finance Act 2018 s. 87](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1695979_BI/ACT%20812.pdf).
3. **Imported taxable services.** Confirm a taxable service acquired by a person in Malaysia from a person outside Malaysia. The earlier of payment and receipt of the invoice sets the tax point. A service tax registrant accounts for it in SST-02. A business outside service tax registration declares on SST-02A and pays by the last day of the month after the trigger month. Check specific exemptions and deductions. [Finance Act 2018 ss. 87–89](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1695979_BI/ACT%20812.pdf).
4. **Adjust** for eligible credit notes. Apply to the Director General for a bad debt refund within 6 years from paying the sales or service tax. Write the relevant amount off and show reasonable recovery efforts. Repay the relevant refund when the debt is recovered. [Act 806 ss. 36–37](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf), [Act 807 ss. 35–36](https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf).
5. **File and pay** by the last day of the month after each taxable period, including nil returns when required. Use separate SST-02 returns for sales and service tax. [RMCD filing guidance](https://mysst.customs.gov.my/filing-text-returns/), [SST-02 instructions](https://mysst.customs.gov.my/wp-content/uploads/2026/09/Borang-SST02.pdf#page=1).
6. **Late payment** without prosecution adds 10% of unpaid tax in the first 30-day period, then an additional 15% in each of the next two 30-day periods, up to 40% for tax still unpaid in the third period.
7. **Records**: keep for 7 years from the latest date to which each record relates, in Malay or English, in Malaysia unless the Director General permits otherwise.

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Service tax, general rate from 1 March 2024 | 8% | https://mysst.customs.gov.my/wp-content/uploads/2025/03/PERINTAH-CUKAI-PERKHIDMATAN-KADAR-CUKAI-PINDAAN-2024.pdf |
| Food and beverage, telecommunications, parking and logistics | 6% | https://mysst.customs.gov.my/wp-content/uploads/2025/03/PERINTAH-CUKAI-PERKHIDMATAN-KADAR-CUKAI-PINDAAN-2024.pdf |
| Credit card or charge card | RM25 per principal or supplementary card on issuance and each subsequent year or part-year | https://mysst.customs.gov.my/wp-content/uploads/2025/03/PERINTAH-CUKAI-PERKHIDMATAN-KADAR-CUKAI-PINDAAN-2024.pdf |
| Prescribed construction work | 6% since 1 July 2025 | https://mysst.customs.gov.my/background/ |
| Prescribed private healthcare, traditional and complementary medicine and allied health | 6% since 1 July 2025, subject to the exclusions and Malaysian citizen relief | https://mysst.customs.gov.my/background/, https://mysst.customs.gov.my/service-tax-policy/ |
| Prescribed education | 6% since 1 July 2025. Check Group M, including school fees exceeding RM60,000 per student per academic year and the non-citizen rule for covered higher education and language centres | https://mysst.customs.gov.my/background/, https://mysst.customs.gov.my/wp-content/uploads/2025/07/Peraturan-Peraturan-CP-Pindaan-2025.pdf#page=51, https://mysst.customs.gov.my/wp-content/uploads/2025/12/STP-4-2025-Education-Amendment-No.-2.pdf |
| Taxable rental or leasing | 8% from 1 July to 31 December 2025. 6% from 1 January 2026. Check Group K exemptions | https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/3413687/P.U.%20%28A%29%20125_2026.pdf#page=3, https://pub-359af8e1f79c472292a7e44ec60f3027.r2.dev/Service%20Tax%20Policy/MS/DCP%202-2025%20%28Sewaan%20atau%20Pajakan%29%20%28Pindaan%20No.5%29%20220726.pdf#page=2 |
| Group K rental or leasing registration threshold | RM1,000,000 in 12 months | https://mysst.customs.gov.my/wp-content/uploads/2025/07/5-PUA-201.2025.pdf#page=5 |
| Group H financial services registration threshold | RM1,000,000 in 12 months for items 2 to 4. Item 1 card services has a nil threshold | https://mysst.customs.gov.my/wp-content/uploads/2025/07/5-PUA-201.2025.pdf#page=5, https://mysst.customs.gov.my/wp-content/uploads/2025/07/Peraturan-Peraturan-CP-Pindaan-2025.pdf#page=38 |
| Prescribed construction registration threshold | RM1,500,000 in 12 months. Check Group L exclusions for residential work and related public facilities | https://mysst.customs.gov.my/wp-content/uploads/2025/07/Peraturan-Peraturan-CP-Pindaan-2025.pdf#page=49 |
| Prescribed private healthcare and related services registration threshold | RM1,500,000 in 12 months | https://mysst.customs.gov.my/wp-content/uploads/2025/07/Peraturan-Peraturan-CP-Pindaan-2025.pdf#page=47 |
| Sales tax rates | 5%, 10% or specific rates under the tariff orders. Check current exemptions and schedules before applying the residual 10% | https://mysst.customs.gov.my/faq-transition-of-sales-tax-rate-changes-2025/, https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/3635172/PUA%20281%20%282026%29.pdf#page=4 |
| General manufacturer of taxable goods registration threshold | RM500,000 in 12 months, subject to activity exemptions | https://mysst.customs.gov.my/faq-sales-tax/ |
| SST-02 due date | Last day of the month after the taxable period | https://mysst.customs.gov.my/filing-text-returns/ |
| Late payment penalty | 10% for the first 30 days, 15% for the second 30 days and 15% for the third 30 days, maximum 40% | https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf, https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf |
| Apply for sales or service tax bad debt refund | 6 years from payment of the tax | https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf, https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf |
| Record keeping | 7 years from the latest date to which the record relates | https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf, https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Threshold test | Historical: this month plus the 11 before. Future: this month plus the 11 after. Registration generally follows the earlier test under which the historical total exceeds the prescribed threshold or there are reasonable grounds to expect the projected total to exceed it. Check any commencement or special category rule |
| Manufacturer supplies or exports goods for export | Verify a direct export exemption, a buyer’s exemption with required proof, or any later drawback under s. 40. Use the applicable sales-tax SST-02 field. [Act 806, s. 40](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf) |
| Subcontract processing for another manufacturer | Manufacturing or a service? Flag and ask |
| Goods and services on one invoice | Can they be separately invoiced? Flag and ask |
| SaaS or cloud bought online | Check the billing entity, taxing jurisdiction and nature of service. A foreign invoice alone does not establish an imported taxable service or additional tax payable. |
| Streaming or apps for staff from a foreign provider | The foreign digital service provider may already charge service tax; check the invoice |
| Bank fees | Check the Group H item and continuing exemptions. Specified fee-based services were in scope from 1 July 2025. Remaining covered financial fees entered from 1 October 2025, at the general 8% rate where taxable. [RMCD Policy 1/2025 (Amendment No. 5)](https://mysst.customs.gov.my/service-tax-policy/). |
| Electricity, water, telecoms, insurance, professional fees and platform commissions | Review each invoice. Domestic supplier tax is generally a cost. Apply the imported taxable services rules where relevant. |
| Salaries, EPF, SOCSO, EIS, LHDN, RMCD, SSM payments, dividends, loans, own transfers | Outside SST, exclude |
| Cash withdrawal | Ask; default exclude |
| Residential building construction | Excluded from the construction service tax |
| GST refunds from before September 2018 | Refer |

## Worked cases

Case 1, two SST-02 returns for January and February 2026. Assume both registrations are in place, the goods are correctly tariffed and sold in the period, and payment for the stated taxable services is received in the period. Goods at 10% are RM80,000 and goods at 5% are RM20,000, giving sales tax RM8,000 + RM1,000 = RM9,000. Consultancy receipts of RM30,000 at 8% and café receipts of RM5,000 at 6% give service tax RM2,400 + RM300 = RM2,700. Both payments and returns are due by 31 March 2026. At 45 days late, the 25% penalties are RM2,250 for sales tax and RM675 for service tax, RM2,925 in total. [SST-02 instructions](https://mysst.customs.gov.my/wp-content/uploads/2026/09/Borang-SST02.pdf#page=1), [Act 806 s. 26](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf), [Act 807 s. 26](https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf).

```oa-check
name: Separate sales and service tax returns paid 45 days late
inputs:
  goods_10: 80000
  goods_5: 20000
  consultancy: 30000
  cafe: 5000
steps:
  - sales_tax: goods_10 * 0.10 + goods_5 * 0.05
  - service_tax: consultancy * 0.08 + cafe * 0.06
  - total: sales_tax + service_tax
  - sales_penalty: sales_tax * (0.10 + 0.15)
  - service_penalty: service_tax * (0.10 + 0.15)
  - penalty: sales_penalty + service_penalty
expected:
  sales_tax: 9000.00
  service_tax: 2700.00
  total: 11700.00
  sales_penalty: 2250.00
  service_penalty: 675.00
  penalty: 2925.00
```

Case 2, commercial landlord. At the end of May 2026 the historical 12-month taxable rental is RM520,000 and projected taxable rental for the statutory forward window is RM480,000. Both are below the RM1,000,000 Group K threshold. If there is no registration or other obligation and the landlord remains below the threshold, it charges no service tax on the RM90,000. If it was already validly registered for Group K, payment of all RM90,000 is received in its July–August taxable period and no exemption applies, service tax is RM90,000 × 6% = RM5,400 and is due by 30 September 2026. [P.U. (A) 201/2025, reg. 3(b)](https://mysst.customs.gov.my/wp-content/uploads/2025/07/5-PUA-201.2025.pdf#page=5), [P.U. (A) 125/2026, paras 1–2](https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/3413687/P.U.%20%28A%29%20125_2026.pdf#page=3).

```oa-check
name: Rental registration test and tax if already registered
inputs:
  trailing_12: 520000
  forward_12: 480000
  threshold: 1000000
  period_rent: 90000
steps:
  - over_historical: max(trailing_12 - threshold, 0)
  - over_future: max(forward_12 - threshold, 0)
  - tax_if_registered: period_rent * 0.06
expected:
  over_historical: 0
  over_future: 0
  tax_if_registered: 5400.00
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
| Register | Apply on MySST when registration liability arises, or voluntarily if eligible. |
| Taxable period | The first period generally starts at the effective registration date and ends on the last day of the following month. Later periods are normally two months unless a different period is approved. |
| Return | File separate SST-02 forms for sales tax and service tax by the last day of the following month, including nil returns. |
| Imported services, outside service tax registration | SST-02A and payment by the last day of the month after the earlier payment or invoice-receipt month. |
| Payment | Pay electronically via MySST, or send one cheque or bank draft per return to the Customs Processing Centre using a permitted delivery method. [RMCD Public Ruling 6/2026, paras 26–33](https://pub-359af8e1f79c472292a7e44ec60f3027.r2.dev/SST%20Public%20Rulings/KETETAPAN%20UMUM%20BIL.6%202026.pdf#page=13). |
| Working paper | Per `vat-workflow-base`: sales tax by rate and exempt; service tax by rate; imported services; adjustments; net payable |

Bank statements (Maybank, CIMB, Public Bank and others, DD/MM/YYYY, MYR): exclude internal transfers and payroll; split platform settlements (Grab, Shopee) into platform fee and underlying sale.

## Completion checklist

- Each sale mapped to sales tax, service tax (with First Schedule item), export or outside scope.
- Threshold tested both ways for every service type the client provides.
- Rates checked against the table, including the 6% services and construction.
- Imported services declared on the right form.
- Specific deductions and exemptions checked where relevant.
- Due date and any late payment penalty stated.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the service tax rates (8%, 6% services, RM25 card), threshold methods, SST-02 due date, late payment penalty and records. Use the Acts for the bad debt clock | https://mysst.customs.gov.my/faq-services-tax/ | 2026-11-14 |
| Read for the initial scope in July 2025. Use later orders for 2026 rental, financial, healthcare and education services | https://mysst.customs.gov.my/faq-expansion-of-service-tax-scope-2025/ | 2026-11-14 |
| Read for the sales tax rates of 5%, 10% and specific rates from 1 July 2025 and the RM500,000 manufacturer threshold | https://mysst.customs.gov.my/faq-transition-of-sales-tax-rate-changes-2025/ | 2026-11-14 |
| Read for the Service Tax (Rate of Tax) (Amendment) Order 2024, P.U. (A) 64/2024: 8% from 1 March 2024 with 6% kept for F&B, telecoms, parking and logistics | https://mysst.customs.gov.my/wp-content/uploads/2025/03/PERINTAH-CUKAI-PERKHIDMATAN-KADAR-CUKAI-PINDAAN-2024.pdf | 2026-11-14 |
| Read for the Service Tax (Amendment) Regulations 2025, P.U. (A) 172/2025: thresholds in the First Schedule items | https://mysst.customs.gov.my/wp-content/uploads/2025/07/Peraturan-Peraturan-CP-Pindaan-2025.pdf | 2026-11-14 |
| Read for the Sales Tax (Rate of Sales Tax) (Amendment) Order 2025, P.U. (A) 199/2025, in force 1 July 2025 | https://mysst.customs.gov.my/wp-content/uploads/2025/07/2-PUA-199.2025.pdf | 2026-11-14 |
| Read for imported taxable services: registered persons declare in SST-02, others on SST-02A | https://mysst.customs.gov.my/wp-content/uploads/2025/02/Information-about-Imported-Taxable-Services.pdf | 2026-11-14 |
| Read for the list of 2026 orders, regulations and policies issued by RMCD | https://mysst.customs.gov.my/announcements/ | 2026-11-14 |
| 6% Group K rental rate from 1 January 2026, P.U. (A) 125/2026 | https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/3413687/P.U.%20%28A%29%20125_2026.pdf | 2026-11-22 |
| Corrected Group K and H thresholds, P.U. (A) 201/2025 | https://mysst.customs.gov.my/wp-content/uploads/2025/07/5-PUA-201.2025.pdf | 2026-11-22 |
| Current Customs policies, including Group K, finance and healthcare | https://mysst.customs.gov.my/service-tax-policy/ | 2026-11-22 |
| Group K rates and tenant relief, Policy 2/2025 (Amendment No. 5, Malay) | https://pub-359af8e1f79c472292a7e44ec60f3027.r2.dev/Service%20Tax%20Policy/MS/DCP%202-2025%20%28Sewaan%20atau%20Pajakan%29%20%28Pindaan%20No.5%29%20220726.pdf | 2026-11-22 |
| Withdrew service tax proposal for beauty services | https://www.mof.gov.my/portal/images/2025/06/27/Media-Release-Revisions-to-the-SST-take-into-account-public-and-industry-feedback.pdf | 2026-11-22 |
| Service tax periods, records, penalties and bad debts, Act 807 | https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf | 2026-11-22 |
| Sales tax periods, records, deductions, penalties and bad debts, Act 806 | https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1761172_BI/Act%20806%20%28MUKTAMAD%29%20AS%20AT%201.1.2023.pdf | 2026-11-22 |
| Imported services tax point and deadline, Finance Act 2018 ss. 87–89 | https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/1695979_BI/ACT%20812.pdf | 2026-11-22 |
| Current SST-02 and separate return requirement | https://mysst.customs.gov.my/wp-content/uploads/2026/09/Borang-SST02.pdf | 2026-11-22 |

Not yet confirmed: a general six-year period for credit-note adjustments or the relevant rate for a specific product without the goods classification and current tariff orders.
