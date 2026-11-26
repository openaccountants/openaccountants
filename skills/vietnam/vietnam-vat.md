---
name: vietnam-vat
description: >
  Prepare a Vietnam VAT review for 2026: establish the deduction or direct
  method, check 10%, temporary 8%, 5% and export treatment, input evidence,
  and the household revenue threshold. Use for thuế GTGT, hóa đơn điện tử,
  phương pháp khấu trừ and phương pháp trực tiếp questions.
version: 2.3
jurisdiction: VN
tax_year: 2026
tax_year_notes: "2026 supplies only. The temporary reduction runs through 31 December 2026; do not extrapolate it to 2027. Earlier supplies and retrospective corrections are referred."
last_updated: 2026-11-26
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
type: situation-rules
---

# Vietnam VAT

> **General reference only.** This Guide supports review, not an authorised return or payment. It remains a Tier 2 community contribution, pending professional review.

## Who this applies to

Organisations, households and individuals trading taxable goods or services in Vietnam, and importers (VAT Law arts 3–4). Amounts below are VND. Establish the business type and VAT method before calculating.

**Workflow hold.** This country file depends on `vat-workflow-base`. Its existing regional-layer requirement remains a stop: use this text as reference only until that requirement or an approved exception is met. Do not produce a filing instruction or workbook under that workflow meanwhile.

### Required inputs

Ask only for missing facts: business type; MST tax code; deduction or direct method; filing period and prior-year revenue; bank records; sales and purchase invoices; payment evidence; credit brought forward; taxable/exempt use; foreign buyers and consumption location; foreign suppliers and tax payment documents. A supplier name or bank transfer alone does not establish a VAT rate or credit. Do not validate an MST by an assumed length. Missing evidence stays **Needs Input**.

No bank statement is a workflow stop. More than 10 questions after grouping is also a workflow stop. These are workflow policies, not legal thresholds. Direct-method businesses do not use the deduction working paper; the household example below is explanatory only.

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
| --- | --- | --- |
| Standard rate: 10% | Taxable supplies outside the 0% and 5% lists; apply the temporary reduction only where eligible. | [VAT Law art 9.3](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) |
| Temporary rate: 8% | Deduction-method supplies otherwise at 10%, from 1 July 2025 through 31 December 2026. Excludes telecoms; finance, banking, securities, insurance; real-estate business; metal products; mining products except coal; and special-consumption-tax goods/services except petrol. Check Annexes I–II against the actual supply. Exempt and 5% supplies retain their treatment. | [Decree 174 arts 1–2](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf) |
| Clean water: 5% | Water for production/domestic use; excludes bottled/jarred drinking water and other soft drinks. | [VAT Law art 9.2(a)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) |
| Household threshold: VND 1,000,000,000 (in words on the page: “01 tỷ đồng”) | In 2026, household/individual annual business revenue at or below this is not subject to VAT. Above it, direct-method VAT applies to all taxable revenue, not only the excess. It is not a company VAT exemption. | [Decree 141 arts 1, 3](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf); [Decree 68 art 3](https://xdcs.cdnchinhphu.vn/446259493575335936/2026/3/6/68-2026-nd-cp-05032026-signed-17727673940151875228819.pdf); [tax authority explanation](https://chinhsachonline.chinhphu.vn/sang-tao-noi-dung-so-doanh-thu-bao-nhieu-phai-nop-thue-90014.htm) |
| Deduction-method entry: VND 1,000,000,000 (in words on the page: “01 tỷ đồng”) | Full accounting, invoices and documents required. Businesses with annual sales revenue from this amount use deduction, excluding households/individuals; eligible businesses below it may elect deduction. | [VAT Law art 11.2](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) |
| Direct percentages: 1%, 5%, 3%, 2% | Respectively: goods distribution; services/construction without materials; production/transport/services with goods/construction with materials; other business. These are percentages of revenue, not invoice VAT rates. Gold/silver/gemstones have a separate value-added method. | [VAT Law art 12](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) |
| Direct-method reduction: 20% | Only eligible supplies during Decree 174's period, when invoiced as prescribed. The four percentages become 0.8%, 4%, 2.4%, 1.6% (computed); the sales invoice records the reduction. | [Decree 174 art 1.2(b), 1.3(b)](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf) |

Other reduced-rate or exempt classifications need the specific product and operative conditions. For agriculture and feed, salt, housing and land, insurance and financial services, medical/veterinary/funeral services, education, publications, public transport, technology/IP/software, handicrafts, fishing/agricultural equipment, medical/teaching equipment, traditional arts, toys/books, science services and social housing: Check this point with one of our partner accountants.

## The base

**Deduction calculation.** Output VAT is taxable price × rate; VAT payable is output less deductible input. For VAT-inclusive prices, net = gross ÷ (1 + rate), and VAT = gross − net (VAT Law arts 7.1(k), 11). Unused deductible input carries forward (art 14.1(đ)). For the simple example below, payable = max(output − deductible input − credit brought forward, 0); carryforward = max(credit brought forward + deductible input − output, 0). Special adjustments/refunds require separate review.

**Tax point.** Goods: transfer of ownership/use or invoice; services: completion or invoice, regardless of payment (art 8). The July example assumes both completion and invoice in July. If those dates differ, or a prepayment, staged delivery or sector-specific timing rule is involved: Check this point with one of our partner accountants.

**Input evidence.** Deduction requires taxable business use and a VAT invoice, import VAT payment document, or document of VAT paid for a foreign party (art 14). Purchases from VND 5,000,000 including VAT require non-cash payment evidence; cash paid into the seller's bank account is insufficient. Aggregate purchases from one taxpayer on the same day for this limit (Decree 181 art 26). Offsets, third-party/employee payments, gifts/samples and deferred instalments have special conditions: Check this point with one of our partner accountants.

**Taxable price and special supplies.** For surcharges, discounts, financial receipts, compensation, exchange/internal use, gifts and promotions: Check this point with one of our partner accountants.

**Mixed use and exceptional input.** Separate taxable from exempt use; do not assume all input is deductible. For shared-cost ratios, investment adjustments, cars, staff assets, losses, promotions, capital contributions, excluded assets, timing of corrections and income-tax cost treatment: Check this point with one of our partner accountants.

**Invoices.** For eligible deduction supplies the VAT invoice states 8%; mixed-rate invoices identify each item's rate. If invoiced at an unreduced rate, seller and buyer correct the invoice under invoice law and adjust VAT from the corrected invoice. File Decree 174 Annex III Form 01 with the return (Decree 174 art 1.3–1.6). For coded/uncoded/cash-register invoices, issuance timing, required fields, replacements, discounts, returns and cancellation: Check this point with one of our partner accountants.

**Supplier discovery.** Use bank, utility, telecom, transport/courier, supermarket/retail, hotel/restaurant, fuel, office/coworking, insurance, local software/cloud and payment-processor names only to request the invoice and product description. Do not assign a rate by name. For internal transfers, loan principal, wages, dividends, taxes/social-insurance payments, deposits and ATM withdrawals, reconcile the underlying transaction before deciding whether any supply or VAT document exists. For classification beyond the rules above: Check this point with one of our partner accountants.

Bank exports: inspect the actual headers, date convention, debit/credit signs, currency and balance. `Nhận chuyển khoản` means incoming transfer, `Thanh toán` payment, `Nhận ngoại tệ` foreign-currency receipt, `Lãi tiền gửi` deposit interest, `Phí dịch vụ` fee, `Số dư` balance and `Nội dung` narrative. These are reading aids, not tax classifications or verified bank layouts.

## Deadlines and filing

Before any return, confirm the period, current portal/form, ordinary deadline and any taxpayer-specific payment extension. For monthly/quarterly elections, new businesses, per-transaction/foreign-supplier filings, no-return cases, prior-period forms, payment extensions (including Decree 245), supplementary returns and non-working-day dates: Check this point with one of our partner accountants.

Do not map 8% sales to a 10% return line by inference. For Forms 01/GTGT through 05/GTGT, household forms, allocation annexes and every field mapping: Check this point with one of our partner accountants.

For refund eligibility, floors/caps, export or investment/5%-supply refunds, dissolution, travellers, aid, diplomats/treaties, refund documents and processing times: Check this point with one of our partner accountants.

## Penalties and interest

For late filing/payment, incorrect returns, evasion, illegal/missing/late invoices, organisation versus individual fines, mitigating/aggravating factors, combining breaches, limitation periods and criminal consequences: Check this point with one of our partner accountants.

## Cross-border points

**Ordinary export consulting.** A service supplied directly to a foreign organisation and consumed outside Vietnam can be zero-rated; hold its contract and non-cash payment evidence. Confirm it is outside Decree 181 art 17.4 exclusions, including services supplied in Vietnam (sports, arts, culture, entertainment, conferences, hotels, training, advertising, tours, services tied to domestic distribution/consumption, and non-cash payment services), and the statutory exclusions for technology/IP transfers, reinsurance, credit, capital transfers, derivatives and postal/telecom services (VAT Law art 9.1; Decree 181 arts 17–18).

A qualifying export service that fails the non-cash-payment condition has no output VAT and loses the related input deduction (Decree 181 art 28.9). A service consumed in Vietnam is not that export case: establish its domestic classification and rate.

For real estate and construction transactions, foreign individuals, non-tariff zones, goods/customs failures, on-the-spot exports, international transport/aviation/maritime services, digital content, export entrustment and special payment alternatives: Check this point with one of our partner accountants.

For international purchases, foreign contractor VAT/income tax, platform withholding, supplier registration, any reduced rate and import tax points: Check this point with one of our partner accountants. Do not claim input from a foreign bank charge alone.

## Worked cases

## Two worked examples that recompute

### Example 1: July 2026 deduction month

Hypothetical Ho Chi Minh City IT consultancy, deduction method, monthly period; VND 3,000,000 credit brought forward. All purchases serve taxable business exclusively, have compliant VAT invoices, and satisfy payment conditions except the cash printer. Each 8% item is ordinary taxable consulting/courier/printing equipment, not software, a metal product or any other Annex I–II exclusion. Recheck the actual supply before using these assumed classifications. The overseas service is completed and invoiced in July. Rounded to the dong for illustration, not as a statutory rounding instruction.

| Item | Gross VND | Example treatment | VAT VND | Official source |
| --- | --- | --- | --- | --- |
| Domestic IT consulting sale | 108,000,000 | Eligible 8%; net 100,000,000 | 8,000,000 output | [Decree 174 art 1](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf) |
| Clean water | 2,100,000 | 5%; net 2,000,000 | 100,000 input | [VAT Law art 9.2(a)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) |
| Courier | 10,800,000 | Eligible 8%; net 10,000,000 | 800,000 input | [Decree 174 art 1](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf) |
| Telecoms | 2,200,000 | 10%; net 2,000,000 | 200,000 input | [Decree 174 art 1.1(a)](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf) |
| Subcontractor for overseas job, paid by transfer | 54,000,000 | Eligible 8%; net 50,000,000 | 4,000,000 input except case D | [Decree 174 art 1](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf) |
| Printer paid in cash | 6,480,000 | Eligible 8%; net 6,000,000; ordinary cash purchase over evidence floor | 480,000 barred | [Decree 181 art 26](https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/4/03signed-17726133860331013983973.pdf) |
| US consulting fee | 125,000,000 | USD 5,000 converted at the example's supplied VND amount; not an asserted exchange rate | Cases below | [VAT Law art 9](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) |

Ordinary input totals VND 5,100,000. For case D, only VND 1,100,000 unrelated input remains deductible.

| Case | Additional fee output VND | Output less deductible input VND | Payable after brought credit VND | Carryforward VND | Conditions/source |
| --- | --- | --- | --- | --- | --- |
| A | 0 | 2,900,000 | 0 | 100,000 | Ordinary consulting directly to foreign company, consumed abroad, contract, non-cash evidence, no excluded service: [Decree 181 arts 17–18](https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/4/03signed-17726133860331013983973.pdf) |
| B | 10,000,000 | 12,900,000 | 9,900,000 | 0 | Consumed in Vietnam, fee excludes VAT, eligible 8%: [Decree 174 art 1](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf) |
| C | 9,259,259 | 12,159,259 | 9,159,259 | 0 | Same domestic supply, fee includes VAT: [VAT Law art 11.1(b)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) |
| D | 0 | 6,900,000 | 3,900,000 | 0 | Otherwise qualifying export consulting paid in cash; related 4,000,000 input barred: [Decree 181 art 28.9](https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/4/03signed-17726133860331013983973.pdf) |

```oa-check
name: VN deduction month with four overseas fee cases
inputs:
  domestic_gross: 108000000
  fee: 125000000
  water_gross: 2100000
  courier_gross: 10800000
  telecom_gross: 2200000
  subcontract_gross: 54000000
  printer_gross: 6480000
  credit_brought: 3000000
steps:
  - output_domestic: domestic_gross - round(domestic_gross / 1.08, 0)
  - water_input: water_gross - round(water_gross / 1.05, 0)
  - courier_input: courier_gross - round(courier_gross / 1.08, 0)
  - telecom_input: telecom_gross - round(telecom_gross / 1.10, 0)
  - subcontract_input: subcontract_gross - round(subcontract_gross / 1.08, 0)
  - printer_barred: printer_gross - round(printer_gross / 1.08, 0)
  - general_input: water_input + courier_input + telecom_input
  - input_total: general_input + subcontract_input
  - a: output_domestic - input_total
  - b: a + round(fee * 0.08, 0)
  - c: a + round(fee / 1.08 * 0.08, 0)
  - d: output_domestic - general_input
  - paid_a: max(a - credit_brought, 0)
  - carried_a: max(credit_brought - a, 0)
  - paid_b: max(b - credit_brought, 0)
  - paid_c: max(c - credit_brought, 0)
  - paid_d: max(d - credit_brought, 0)
expected:
  output_domestic: 8000000
  water_input: 100000
  courier_input: 800000
  telecom_input: 200000
  subcontract_input: 4000000
  printer_barred: 480000
  general_input: 1100000
  input_total: 5100000
  a: 2900000
  b: 12900000
  c: 12159259
  d: 6900000
  paid_a: 0
  carried_a: 100000
  paid_b: 9900000
  paid_c: 9159259
  paid_d: 3900000
```

### Example 2: household crosses the 2026 threshold

Hypothetical services business without materials; taxable revenue Q1 VND 300,000,000 and Q2 VND 350,000,000. Q3 alternatives are VND 340,000,000 (cumulative 990,000,000) or VND 400,000,000 (cumulative 1,050,000,000). Case A remains below the threshold through Q3, with no VAT triggered then; the final annual revenue still matters.

In case B, file from the crossing quarter and include earlier taxable revenue in that return. At the 5% services percentage, all VND 1,050,000,000 gives VND 52,500,000. If all sales satisfy Decree 174's reduction and invoice requirements, 4% gives VND 42,000,000. If only Q3 qualifies, Q1–Q2 give VND 32,500,000 and Q3 VND 16,000,000, total VND 48,500,000. Charging only Q3 would omit VND 26,000,000 under the all-reduced assumptions. These are alternative invoice facts, not a taxpayer choice. Sources: [VAT Law art 12.2](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf), [Decree 174 art 1](https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf), [tax authority on cumulative declaration](https://xaydungchinhsach.chinhphu.vn/giai-phap-giup-ho-kinh-doanh-ke-khai-thue-dung-an-tam-tuan-thu-phat-trien-ben-vung-119260312114316524.htm) (its former threshold is replaced by Decree 141).

A newly exceeding household not already voluntarily registered must register for qualifying e-invoices within 30 days after the last day of the period in which cumulative revenue exceeds VND 1 billion ([Decree 141 art 1.2](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf)). For the actual Q3 filing date, annual revenue notice, non-working-day adjustment and any payment extension: Check this point with one of our partner accountants.

```oa-check
name: VN household threshold and whole taxable revenue
inputs:
  q1: 300000000
  q2: 350000000
  q3_low: 340000000
  q3_high: 400000000
  threshold: 1000000000
  percentage: 5
  cut_percent: 20
steps:
  - total_low: q1 + q2 + q3_low
  - total_high: q1 + q2 + q3_high
  - over_low: min(floor(total_low / (threshold + 1)), 1)
  - over_high: min(floor(total_high / (threshold + 1)), 1)
  - reduced: percentage * (100 - cut_percent) / 100
  - tax_low: over_low * total_low * percentage / 100
  - tax_standard: over_high * total_high * percentage / 100
  - tax_reduced: over_high * total_high * reduced / 100
  - tax_mixed: ((q1 + q2) * percentage + q3_high * reduced) / 100
  - omitted: (q1 + q2) * reduced / 100
expected:
  total_low: 990000000
  total_high: 1050000000
  over_low: 0
  over_high: 1
  reduced: 4
  tax_low: 0
  tax_standard: 52500000
  tax_reduced: 42000000
  tax_mixed: 48500000
  omitted: 26000000
```

### Remaining original case inputs

The six July bank cases are retained as inputs: 15/07 domestic consulting +108,000,000; 22/07 US consulting +USD 5,000 (supplied VND 125,000,000); 30/07 clean water −2,100,000; 31/07 courier −10,800,000; 31/07 deposit interest +250,000; 05/07 Google Workspace −3,300,000. The first four use Example 1 only after checking its facts. For deposit-interest return/ratio treatment and the Google supplier's registration, withholding and input document: Check this point with one of our partner accountants.

The original mixed-investment case supplied VND 1,000,000,000 input, planned taxable use 80% and a later three-year 70% ratio. Pure arithmetic gives 800,000,000 and 700,000,000, a 100,000,000 difference. These are not confirmed entitlement or adjustment-period instructions: Check this point with one of our partner accountants.

The original form test supplied import value 100,000,000/VAT 10,000,000; domestic purchase 50,000,000/VAT 4,000,000; sale 200,000,000/VAT 20,000,000; and an exclusion value 5,000,000. Purchases add to 150,000,000 and VAT 14,000,000; subtracting the supplied exclusion from the sale gives 195,000,000. No current form-field mapping or tax entitlement follows from this arithmetic: Check this point with one of our partner accountants.

## Ask the client first

Resolve method, supply, date, location of consumption, invoice, payment and business use before any calculation. Keep unresolved facts visible; never substitute an assumed 10% rate, domestic buyer or full input deduction. Obtain professional review before any filing or payment.

## Sources

Read 26 November 2026. Working English translations; Vietnamese law controls. Exact operative quotations and old-topic destinations are in the private claims ledger. This shortened Guide retains no assertion of a completed prior source read merely because the old file listed a URL.

| Source and passages used | Official URL | Read on |
| --- | --- | --- |
| VAT Law 48/2024 consolidated through Law 149/2025: arts 3–4, 7–9, 11–12, 14 | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf | 2026-11-26 |
| Decree 174: arts 1–2: reduction, exclusion categories and invoice requirements; product codes require case checking | https://bcp.cdnchinhphu.vn/334894974524682240/2025/7/1/174-2025-nd-cp-1751372683836267987993.pdf | 2026-11-26 |
| Decree 181 consolidated through Decree 359: arts 17–18, 25–28; apply later amendments only where relevant | https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/4/03signed-17726133860331013983973.pdf | 2026-11-26 |
| Decree 144: amendments checked for applicability to retained clauses | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/144-ndcp.signed.pdf | 2026-11-26 |
| Decree 68: household VAT and crossing declaration, read with Decree 141 | https://xdcs.cdnchinhphu.vn/446259493575335936/2026/3/6/68-2026-nd-cp-05032026-signed-17727673940151875228819.pdf | 2026-11-26 |
| Law 09: art 2 delegates the household amount to Government, art 5.2 applies it from 1 January 2026; supersedes the consolidation’s former amount | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/09-qh.signed.pdf | 2026-11-26 |
| Decree 141: art 1 threshold/invoices, art 3 effective date | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf | 2026-11-26 |
| Tax authority explanation of whole taxable revenue, read with amended threshold | https://chinhsachonline.chinhphu.vn/sang-tao-noi-dung-so-doanh-thu-bao-nhieu-phai-nop-thue-90014.htm | 2026-11-26 |
| Tax Department cumulative declaration explanation; former amount superseded, cumulative principle retained | https://xaydungchinhsach.chinhphu.vn/giai-phap-giup-ho-kinh-doanh-ke-khai-thue-dung-an-tam-tuan-thu-phat-trien-ben-vung-119260312114316524.htm | 2026-11-26 |

Not yet confirmed: the regional workflow clearance and the specialist classifications, filing/field mappings, extensions, refunds and sanctions expressly referred above. Do not use those passages as a tax position.

### When to refuse or refer

Earlier-period supplies/corrections, 2027 rates, regional workflow clearance, and the specialist cases identified above: Check this point with one of our partner accountants.
