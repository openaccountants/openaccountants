---
name: nepal-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Nepal VAT return for any client. Trigger on phrases like "Nepal VAT", "IRD filing", "PAN registration", or any request involving Nepal VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Nepal VAT work.
version: 3.0
jurisdiction: NP
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
tax_year_notes: "Calendar 2026 includes FY 2082/83 (2025/26) and FY 2083/84 (2026/27); apply the labelled period."
---

# Nepal VAT return preparation

## Scope

Prepare a Nepal VAT working paper for practitioner review, using `vat-workflow-base` v0.1 or later alongside this skill. Cover ordinary domestic supplies, exports, purchases and imported services. Calendar 2026 spans FY 2082/83 and FY 2083/84; identify the tax point before selecting the rule. The Finance Act 2083 is enacted: its electricity and ride-sharing provisions commence Shrawan 1, 2083. Most other VAT amendments commence immediately under its commencement clause. [Finance Act §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=1).

Historical credit retained from the earlier version only; it does not approve the present rewrite:

**Validated by** - Verified by Ashish Bista (ICAN: 1765) on 2026-06-06

This version is a source-cited draft and has no new accountant approval. The frontmatter remains tier 2.

## Ask the client first

- PAN and actual VAT registration, legal entity and any IRD registration/filing notice; bank statements alone are intake material.
- Nepali month, fiscal year, invoice/supply/payment dates and the applicable tax period.
- Business activities, rolling taxable turnover and any special registration trigger; identify exports, SEZ, hydropower or infrastructure concessions.
- Sales and purchase invoices, customs declarations, credit notes and actual business/taxable use; identify separately charged VAT and foreign-supplier VAT registration.
- Prior submitted return, carried-forward credit, payments, adjustments and refund claims, reconciled to the ledger.
- Electricity customer/use/consumption, ride-sharing role, and any special exemption, rate or refund evidence.

No unknown location is assumed to be Nepal; no unknown sale is automatically assigned the standard rate. Hold an unsupported input claim pending evidence, rather than declaring it legally non-deductible.

## The method, step by step

### 1. Establish registration and time of supply

| Rule and condition | Amount or timing | Official provision |
|---|---|---|
| Small-business registration exemption, goods, freight-vehicle hire or freight services; taxable turnover in the preceding 12 months, subject to compulsory registration triggers | Up to NPR 5,000,000 | [Rule 6(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=3) |
| Services or mixed goods/services, subject to compulsory triggers | Up to NPR 3,000,000 over the preceding 12 months | [Rule 6(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=3) |
| Threshold unexpectedly exceeded | Apply within 30 days; where exceeding it is foreseeable, apply under Rule 7(1) without waiting for actual crossing | [Rule 7(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=4); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=5) |
| Non-resident taxable electronic/offline air services supplied in Nepal | Registration where the preceding 12 months exceed NPR 3,000,000; follow the IRD-prescribed non-resident procedure | [Act §10ख1](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=11) |
| Tax point, subject to the specific continuous-supply and instalment exceptions | Earliest of invoice, delivery/receipt of goods, service performance or consideration; continuous public services use invoice timing | [§6](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=7) |

The thresholds do not excuse an already registered person from returns. Review VAT Act §§9-10 and Rules 6-7 for voluntary registration, imports and compulsory cases before using a threshold. Registration is required on taxable imports above the special Rule 6 limit except the stated own-use exempt-business case; do not treat a turnover threshold as a universal import exemption. [§9 and §10](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=9); [Rule 6(1) proviso](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=3).

### 2. Classify each supply

| Category and condition | Rate or treatment | Official provision |
|---|---|---|
| Ordinary taxable supply or import, with no exemption, zero rate or specific reduced rate | 13%; not a default for an unknown transaction | [§7(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=8) |
| Exported goods with proof of export; qualifying exports of services must meet Schedule 2 recipient/place conditions | 0% | [§7(2), Schedule 2 items 1-2](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=94) |
| Raw materials and manufactured goods sold to an industry operating in a legally established SEZ | 0%, subject to Schedule 2 item 5; not every SEZ transaction | [Schedule 2 item 5](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=94) |
| Electricity supplied to final consumers, to the extent taxable; from Shrawan 1, 2083 | 5% | [§55(1), new VAT §7(1ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=19); [commencement §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=1) |
| Electricity resold by one electricity trader to another; household consumption up to 50 units per customer per month | Exempt under the current Schedule 1; do not charge the reduced rate to an exempt supply | [§55(10), Schedule 1 group 2, HS 2716](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=33) |
| Resident ride-sharing operator's platform transactions with affiliated passenger/freight providers; from Shrawan 1, 2083 | Operator assesses and collects 5% on the statutory taxable value; do not apply to every transport business | [§55(1)-(2), VAT §§7(1ख),8(2ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=19) |
| Exempt listed basic agricultural goods | Exempt only within the Schedule/HS description; hotel/restaurant and similar supplies have exceptions | [current Schedule 1 group 1](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=22); [group 1 notes](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=33) |
| School/university teaching, specified government-owned vocational training and institution-run ancillary services within group 6 | Exempt, subject to the listed provider and use conditions | [Schedule 1 group 6](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=55) |
| Health services within the Schedule | Exempt; do not extend to every product bought from a health provider | [Schedule 1 group 5 note (1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=52) |
| Public passenger transport within group 9 | Exempt excluding air transport, cable cars and platform ride-sharing passenger/freight services | [Schedule 1 group 9](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=56) |
| Financial services and listed digital financial-service fees | Exempt within Schedule 1 group 11(आ)(4); a bank or wallet name alone does not make every sale exempt | [Schedule 1 group 11(आ)(4)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=85) |
| Drinking water supplied openly by tap or tanker | Exempt; identify the actual supply rather than applying a standard rate to the utility's name | [Schedule 1 group 2 note 1](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=33) |

Exemption and zero-rating are different: VAT Act §5(3) bars deduction/refund of tax on purchases for exempt supplies, while taxable zero-rated supplies remain within the credit framework. [§5(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=6); [§17](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=17). General telecom supplies remain ordinary taxable supplies unless a specific exemption applies; assess the invoice, not the NTC/NCELL brand.

### 3. Determine the base and input credit

For VAT-inclusive ordinary consideration, net = gross / 1.13 and VAT = gross - net. For taxable value quoted exclusive of VAT, VAT = value × 13%. These are derived formulas, not separate statutory rates. Reduced-rate inclusive consideration uses its own rate; never divide every receipt by 1.13.

Imports use the statutory import value including freight, insurance and agent commissions, import/customs duties, equalisation levy and other import taxes, excluding VAT itself; reconcile to the customs assessment. "CIF plus duty" omitted other statutory components. [§12(5), continued](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=13); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=14).

Credit requires VAT registration, taxable business use and prescribed supporting documents. Valid supplier tax invoices/PAN and customs import evidence must be matched to the taxpayer and period; a bank debit is not sufficient. Use direct attribution where possible, then the statutory proportion for shared taxable/exempt activities. Unknown business-use percentages remain on hold for evidence. [§17(1)-(6)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=17); [§17(5ख),(6)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=18); [Rule 40(3)-(5)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=23).

Rule 41 blocks beverages, alcohol, vehicle petrol and entertainment, with the exception for a person whose principal business is supplying those items. Passenger automobiles are subject to a partial-credit rule, not the old blanket total block: Rule 41(2)(ख) states 40% (in numerals on the page) and defines covered road passenger vehicles with at least 3 wheels. Because the text and public FAQ describe this as a proportion of purchase value, this skill does not turn it into an executable tax-credit formula without the detailed IRD directive. Hold automobile credit for that confirmation; ordinary business-use and invoice conditions still apply. [Rule 41(1)-(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=23); [supplier exception](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf#page=24).

### 4. Imported services and digital suppliers

VAT Act §8(2) covers services received from a person outside Nepal by a registered or unregistered recipient; assess at payment or receipt of the service, whichever is earlier. For an ordinary taxable service, apply the ordinary rate. Credit for a registered taxable-business recipient is permitted by §17(5ख), subject to restrictions and documents; an unregistered or exempt-use recipient has no automatic matching credit. [§8(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=8); [§17(5ख),(6)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=18).

For Google, Microsoft, Meta, AWS, Zoom, Slack or Canva, identify the actual contracting entity, supply, Nepal/non-resident VAT registration and whether Nepal VAT has already been charged. Do not mechanically reverse-charge twice. The interaction between supplier-charged non-resident VAT and recipient accounting must be resolved from the current invoice and IRD procedure before finalising a live case. The old universal "Output + Input" instruction was conditional.

### 5. Read bank patterns as clues

The following preserves the original pattern catalogue. These are intake/classification cues; the statutory conditions above decide VAT.

| Pattern | Working-paper route |
|---|---|
| NABIL, NABIL BANK; NIC ASIA, NIC ASIA BANK; NEPAL BANK, RASTRIYA BANIJYA; HIMALAYAN BANK, EVEREST BANK; STANDARD CHARTERED NP | Identify bank charges; qualifying financial-service fees are exempt. Do not infer exemption for unrelated sales. |
| INTEREST, LOAN, REPAYMENT | Separate interest/financial services from principal; principal is not consideration for a supply merely because it crosses the bank. |
| IRD, INLAND REVENUE; CUSTOMS, NEPAL CUSTOMS | Separate tax/duty remittances from purchases; customs VAT may support an import-credit claim with the customs evidence. |
| SSF, SOCIAL SECURITY FUND; COMPANY REGISTRAR, OCR | Social-security remittances and registration charges; do not invent an input VAT invoice. |
| NEA, NEPAL ELECTRICITY | Check customer, consumption, invoice date, exemption and the current electricity rate; never blanket ordinary-rate treatment. |
| KUKL, KATHMANDU WATER | Identify open tap/tanker drinking-water exemption and any separate taxable supply. |
| NTC, NEPAL TELECOM, NCELL | Read the actual taxable telecom invoice and separately identified charges. |
| ESEWA, KHALTI, IME PAY; FONEPAY | Distinguish exempt financial-service fees, merchant sales and settlement transfers. A settlement is not a new sale. |
| GOOGLE, MICROSOFT, META, AWS; ZOOM, SLACK, CANVA | Apply the imported-services decision above with supplier/invoice evidence. |
| SALARY, WAGES, TLAB | Employment payroll, outside the ordinary VAT sales/purchase ledger. |
| OWN TRANSFER, INTERNAL | Reconcile both accounts and exclude the transfer itself from turnover. |
| CASH WITHDRAWAL | Unclassified movement until receipts/purpose establish spending; do not claim credit or treat it as an expense automatically. |

Nabil and NIC Asia CSV exports, NPR records and Devanagari or transliterated narrations are acceptable intake formats. Preserve dates, debit/credit signs, reference and balances; do not infer a fiscal period or supplier status from formatting. Record original foreign-currency values and conversion evidence; the exact statutory conversion rule and applicable Nepal Rastra Bank reference require confirmation before an NPR return value is finalised.

### 6. Billing, consumer incentives and one-off relief

Registered suppliers issue prescribed invoices under §14. New §14A permits IRD standards for electronic invoices and allows notice-designated taxpayers to be required to connect to CBMS or use the department's billing system. Do not assert all taxpayers must use one approved software product. Check the notice applying to this taxpayer. [§14](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=14); [§55(3), new §14A](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=19); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=20).

For IRD-notified goods/services and prescribed electronic payment, §25(1ख) provides a consumer incentive equal to 10% of VAT paid (in words on the page), under IRD's prescribed procedure. Finance Act §55(6) changes the wording from immediate refund to immediate discount. This is a conditional consumer mechanism, not a business input-credit uplift or 10% off the whole invoice. Actual covered supplies and implementation must be confirmed. The legacy claim that every VAT bill automatically becomes a lottery ticket is not established by the enacted text read; do not promise eligibility or winnings. [§25(1ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=27); [§55(6)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=20).

One-off relief is not an unrestricted "principal plus 1% settles every case" rule. The Finance Act gives the following distinct routes; determine eligibility and reconcile the account before calculating relief:

| Route and full boundary | Amount/deadline | Official source |
|---|---|---|
| §41: VAT-registered persons with past taxable transactions where VAT was not collected/deposited, or collected but returns not submitted; file returns through Chaitra 2082 | Relevant VAT plus 1% additional amount, and required returns, by Poush-end 2083; specified interest/additional charges/penalties waived | [§41(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=14) |
| §44: returns already filed but VAT/income tax/excise unpaid as at Jestha 15, 2083 | Outstanding declared tax plus 1% by Poush-end 2083; specified charges/interest waived | [§44](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=15) |
| §45: assessments/amended assessments issued by IRD/offices by Jestha 15, 2083, still unpaid | Assessed principal plus 1% by Poush-end 2083; stated charges and remaining interest waived; telecom businesses excluded | [§45(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=15) |
| §46: qualifying disputed assessments by that cutoff, pending review/court proceedings | Separate withdrawal/application and payment conditions; telecom businesses excluded. Refer the full case before a relief claim | [§46](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=15); [continuation and exceptions](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=16) |

Do not withdraw a dispute or make a relief election without practitioner instructions. These temporary provisions do not waive unrelated current liabilities.

## Boundary and exception table

| Original boundary | Required treatment |
|---|---|
| R-NP-1: SEZ entity | Refer special SEZ status/transaction treatment; ordinary exports guidance does not settle an SEZ entity's full return. |
| R-NP-2: Hydropower/infrastructure with government concession | Refer the concession, project approvals and specific exemption/zero-rate recommendation; do not infer a blanket exemption. |
| Vehicle costs | Identify fuel, automobile type, business use and Rule 41; unresolved partial-credit formula remains on hold. |
| Entertainment | Statutory block, except the principal-supply business exception where applicable. |
| SaaS entity or location unknown | Hold, establish supplier and VAT invoicing; no assumed domestic location or automatic double reverse-charge. |
| Cash withdrawal | Hold until matched to evidence; withdrawal itself is not a VAT-bearing purchase. |
| Mixed use | Direct attribution/apportionment with evidence; no invented business-use percentage. |

## Worked cases

The original dated cases remain FY 2082/83 examples; they do not apply the later electricity/ride-sharing change retroactively. All amounts are hypothetical transaction inputs. Classifications assume invoices and conditions stated here.

### 1. Ordinary domestic sale

Retained input: `05.04.2026 ; KATHMANDU TRADING ; +113,000 ; NPR`. It is VAT-inclusive consideration for an ordinary taxable sale: NPR 113,000 / 1.13 = NPR 100,000 net; VAT NPR 13,000. Record output VAT, not input VAT.

```oa-check
name: Ordinary domestic VAT-inclusive sale
inputs:
  gross: 113000
steps:
  - net: gross / 1.13
  - vat: gross - net
expected:
  net: 100000
  vat: 13000
```

### 2. Export

Retained input: `15.04.2026 ; INDIAN BUYER LTD ; +500,000 ; NPR`. For a proved export of handicrafts with customs/export evidence, taxable consideration is NPR 500,000 and output VAT NPR 0. A foreign buyer's name alone does not prove export; if the goods remain a domestic ordinary taxable supply, the zero rate fails and the contract must establish whether its price includes VAT.

```oa-check
name: Proved goods export versus ordinary domestic exclusive value
inputs:
  value: 500000
steps:
  - export_vat: value * 0
  - domestic_exclusive_vat: value * 0.13
expected:
  export_vat: 0
  domestic_exclusive_vat: 65000
```

### 3. Imported digital service

Retained input: `18.04.2026 ; GOOGLE ; -23,000 ; NPR`. Assume NPR 23,000 is the exclusive value of an ordinary taxable imported service, no Nepal VAT was already charged, section 8(2) applies, and the registered recipient has fully evidenced taxable business use with no input restriction. Self-assessed VAT is NPR 2,990; eligible credit is NPR 2,990, net VAT effect NPR 0. If the recipient is unregistered or uses the service for exempt/private purposes, do not grant that matching credit. Supplier-charged non-resident VAT needs the separate reconciliation above.

```oa-check
name: Imported service conditional credit
inputs:
  base: 23000
steps:
  - output_vat: base * 0.13
  - eligible_input: output_vat
  - taxable_business_net: output_vat - eligible_input
  - no_credit_net: output_vat - 0
expected:
  output_vat: 2990
  eligible_input: 2990
  taxable_business_net: 0
  no_credit_net: 2990
```

### 4. Bank fee

Retained input: `30.04.2026 ; NABIL BANK ; -500 ; NPR`. If this is an exempt financial-service fee, the NPR 500 is an exempt purchase cost and no VAT input credit arises. Do not assign ordinary VAT solely from a debit or the bank's name.

```oa-check
name: Exempt financial-service fee
inputs:
  fee: 500
steps:
  - vat_input_credit: fee * 0
expected:
  vat_input_credit: 0
```

## When to refuse or refer

Apply both named Nepal refusals and the unresolved-input holds above. A bank statement is sufficient to begin classification, never to certify a VAT return without invoices and registration/period evidence. Do not treat an uncertain rate, location, vehicle credit, carried-forward credit or amnesty claim as settled. Obtain practitioner review before filing.

## Filing and payment

Ordinarily self-assess and submit the return, including a nil-transaction month, within 25 days after the Nepali month ends, and pay within the same period. IRD may prescribe shorter/longer periods for specified taxpayers. For taxpayers in districts without an internal revenue office, the current local-body/Treasury alternative has its own earlier delivery and onward-transfer rules; do not apply the ordinary deadline to that route without checking §18(1क). [§18(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=18); [§19(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf#page=19); [current §18(1क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=20).

Use the [IRD Taxpayer Portal](https://ird.gov.np/). Select the taxpayer and VAT period; prepare the prescribed VAT return using output by rate, zero-rated and exempt supplies, domestic/import inputs, reverse-charge amounts, adjustments and opening credit. Reconcile to invoices, customs and the prior accepted return. Save the submission reference, obtain the verification/acceptance required by the account, generate and pay the correct voucher, and retain both return acknowledgement and payment evidence. Exact current screen/box names are not confirmed; do not invent them or call a saved draft filed.

The Excel working paper follows `vat-workflow-base`: date, narration/counterparty, original currency/value, NPR conversion, gross, net, applicable output-rate bucket, zero-rated/exempt classification, domestic/import/reverse-charge input, recoverable portion, evidence, adjustments, opening credit and net VAT. Include the reduced-rate bucket when the current rule applies; reconcile bank movements separately from tax points.

For late payment, statutory additional charges and interest are separate from the temporary relief routes. Obtain an IRD account reconciliation before quoting a total; this skill does not turn an amnesty provision into an automatic penalty waiver.

## Completion checklist

Confirm PAN/registration and the correct month; answer the industry/export/SEZ/infrastructure questions; obtain opening credit and invoice/customs evidence; resolve tax points and every applicable rate; document input restrictions and imported services; recompute the return; match acknowledgement and payment; send unresolved items for practitioner review.

## Sources

| Source and actual material read | Official URL | Read on |
|---|---|---|
| Read for Finance Act 2083 commencement; VAT amendments, current exemption descriptions and distinct relief routes; not the unrelated customs/excise schedules; PDF pages 1,14-16,19-22,33,52,55-56,85-86 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf) | 2026-11-15 |
| Read for VAT Act §§5-10,12,14,17-19,25 and Schedule 2, supplemented by the enacted 2083 amendments; PDF pages 6-9,11-14,17-19,27,94 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A8%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ty8cysa.pdf) | 2026-11-15 |
| Read for VAT Rules 6-7,40-41; registration thresholds/triggers and input restrictions; PDF pages 3-5,23-24 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%AE%E0%A5%82%E0%A4%B2%E0%A5%8D%E0%A4%AF%20%E0%A4%85%E0%A4%AD%E0%A4%BF%E0%A4%B5%E0%A5%83%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%BF%20%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%A9%20(%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_ayoqqdv.pdf) | 2026-11-15 |

Not yet confirmed: actual consumer-discount implementation/notified supplies and the alleged automatic VAT-bill lottery; detailed IRD automobile-credit directive/formula (the linked older directive returned 404 and the web reader timed out); exact foreign-currency conversion rule/NRB reference; supplier-charged non-resident VAT reconciliation procedure; current authenticated VAT form screen/box names; taxpayer-specific notices, SEZ/project concessions, and eligibility for any relief election. These are excluded from automatic calculations.

Version history retained: the earlier v2.0 described an April 2026 rewrite; the prior change log called its June 2026 threshold update v2.1 despite frontmatter v2.0. This v3.0 reconciles the enacted 2083 amendments and retains the dated examples and historical credit without claiming a new approval.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
