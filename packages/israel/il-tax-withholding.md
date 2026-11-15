---
name: il-tax-withholding
description: Use this skill when advising on Israeli tax withholding at source (ניכוי מס במקור, Nikui Mas BeMakor). Trigger on phrases like "withholding tax Israel", "nikui mas", "ishur nikui", "withholding certificate", "Form 856", "Form 102", "tium mas", "tax coordination", "ניכוי מס במקור", "אישור ניכוי", or any Israeli withholding tax query. Covers payments to suppliers, freelancers, landlords, and non-residents. ALWAYS read this skill before advising on Israeli withholding tax.
version: 1.2
jurisdiction: IL
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: decision
---

# Israel: withholding at source and payment reconciliation

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Scope

Prepare a 2026 payer/payee withholding decision and reconciliation for supplier, freelancer, rent, royalty, interest, dividend and non-resident payments. Establish the legal payer, recipient, source, payment category and certificate before calculating. Withholding is generally a collection mechanism, not a declaration that the recipient's final tax equals the amount withheld. Payroll tax coordination and real estate payments require their separate regimes.

| Quick reference | Rule and conditions | Official source |
|---|---|---|
| Domestic framework | s.164 requires deduction on specified income and categories designated by order at the prescribed rate/manner | ITO s.164, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Qualifying non-resident individual payment | 25% under s.170(a), only taxable income not already withheld under ss.161/164 and subject to written assessor direction/exceptions | ITO ss.170-172, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Qualifying non-resident company payment | s.170(a) refers to ss.126/127 corporate rates, rather than a universal 25% | ITO s.170(a), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| 2026 standard certificate period | New certificates 1 January 2026 to 31 March 2027; check actual current status and any shorter/special restriction | ITA 02/2026 ss.1-3, https://www.gov.il/BlobFolder/policy/inst-02-2026/he/IncomeTax_inst-02-2026.pdf |
| Annual payer returns | s.166(b) baseline 30 April following tax year, online Form 126 for employment and Form 856 for withholding-liable income; verify extensions | ITO s.166(b), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

## Ask the client first

Obtain payer status/turnover and withholding-file notices; payee legal identity and tax number/residence/entity type; invoice/contract and gross/VAT components; source and character of income; payment date/currency; current payment-category certificate and online lookup output; special transaction limits; treaty article/residence/beneficial-owner/PE evidence where relevant; prior payments and deposits; and annual reconciliation records. Unknown residence, payer duty, payment type or rate is an unresolved decision, not permission to withhold “to be safe.”

## The method, step by step

### Establish the governing obligation

Section 164 lists employment and other specified income and permits designated categories under orders; it does not impose one service rate or one turnover threshold on every payer. Check the applicable order/regulations and payer conditions before using a default. The 2026 booklet's summary lists services/assets at 30% and a NIS 5,520 one-off exemption amount, but this alone does not establish the detailed 20%/30% conditions, payer scope, aggregation or VAT base. Those operative regulations remain unconfirmed here. A payroll Form 102 obligation does not by itself prove the same payer's supplier-payment duty ([ITO s.164](https://www.btl.gov.il/Laws1/00_0103_000000.pdf); [2026 booklet, other amounts/non-salary summary](https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf)).

Do not use the old blanket domestic table as a rate instruction. Rent has a separate certificate category, and residential/commercial use does not establish a universal 30%/35% withholding rate. Royalties, interest and dividends require their own income/source and withholding provisions; the final dividend rates in [il-corporate-tax](il-corporate-tax.md) are not a substitute for that analysis. Real estate purchase tax (Mas Rechisha), land-gain advances and income-tax withholding are distinct regimes.

### Verify the actual certificate near payment

ITA 02/2026 requires a payer subject to withholding to refresh certificate eligibility near the supplier payment. Match legal identity/entity number, payment category, approved rate, validity dates, payer and any transaction/amount limitation. The online payer lookup output must be produced and signed by the payer, addressed to it, retained for audit and is not transferable to another payer. Use the authority's official linked certificate service, including gmishurim where currently routed, rather than treating an old saved PDF as current proof ([ITA 02/2026 ss.1,6.3-6.4](https://www.gov.il/BlobFolder/policy/inst-02-2026/he/IncomeTax_inst-02-2026.pdf)).

The standard new period runs to **31 March 2027**, correcting the old universal January-December/31 December expiry rule. Special/short certificates can differ. The directive also distinguishes ordinary cash-payment certificates from barter/in-kind cases; do not apply a cash certificate automatically to noncash consideration. A one-off certificate can be limited to a described transaction, specific payer withholding file and amount. Under s.12.1 the general one-off approval is issued at the assessor office for 3 months and is not valid for a stock-exchange member's capital-market withholding. The special employer provident-fund refund approval can run up to 6 months under its separate conditions; refer that exception before applying the general period. Rent appears as a separate payment type, so a services/assets approval is not automatically rent approval ([ITA 02/2026 ss.2,4.7,12.1,12.3](https://www.gov.il/BlobFolder/policy/inst-02-2026/he/IncomeTax_inst-02-2026.pdf)).

Tax coordination (Ishur Tium Mas) for multiple employers/payers is a separate individual payroll process. A public-body bookkeeping certificate is also distinct from a withholding exemption/reduction. For an unavailable/expired certificate, establish the governing legal default; do not assume the payee's final tax rate or invent a punitive 47%.

### Obtain or amend an approval through the proper route

The directive describes centralized/ongoing eligibility checks and assessor handling of defects. To request a changed rate, send a detailed supported written application through the authorized assessor/representative channel; s.10 describes consideration and a written decision/challenge route. Use the actual identity, returns/accounts and supporting facts requested for that case; do not promise automatic annual approval from a universal document checklist. Do not contact the authority or submit here without the relevant authority ([ITA 02/2026 ss.3,10](https://www.gov.il/BlobFolder/policy/inst-02-2026/he/IncomeTax_inst-02-2026.pdf)).

### Compute the payment without inventing the base

Record separately: contractual amount, VAT, **legally established withholding base**, approved/default rate and source, tax withheld, cash paid to recipient and deposit owed to the authority. Net recipient cash = invoice payable minus withholding; payer total cash = recipient cash plus tax remitted. A withheld amount does not reduce output VAT or become a supplier discount. Whether the statutory base includes VAT must be settled for the governing regime, not assumed from the old pre-VAT example. Gross-up clauses require their own contract and tax analysis.

### Non-residents: source and written relief first

Section 170(a) concerns **taxable income** paid to a non-resident, excluding income already withheld under ss.161/164. For an individual it states 25% (25 agorot per lira in the older statutory wording); for a body corporate it refers to ss.126/127. The assessor may set another rate in writing or permit no deduction where tax has been/will be paid another way. Financial institutions transmitting the payment are included unless holding the specified exemption. Section 170(b) excludes a payer itself responsible under ss.108-115; REIT transfers have a separate s.170(c) rule. A foreign bank destination does not prove a non-resident taxable payment ([ITO s.170](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

Treaty residence, source/article, beneficial ownership, permanent establishment, limitations and required approval need actual documentation before treaty relief. Retain the old US-Israel, UK-Israel, Germany-Israel and France-Israel treaty topics as routes to the actual treaty, not invented reduced rates. Section 171's baseline is payment/report within **7 days** of withholding, naming/addressing the recipient; check actual applicable procedural relief before scheduling. Section 172 credits the deduction against recipient tax, while s.173 permits assessment for failure/incorrect reporting ([ITO ss.170-173](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

### Deduction risk: distinguish the legal tests

Current s.32A(a) denies relevant expense deduction/advance reduction unless required tax is withheld and remitted and the ss.166/171 report accurately identifies the recipient. Section 32A(b) permits exceptions where the assessor is satisfied that the recipient reported and paid the tax, tax was withheld/remitted under an assessor approval, or no withholding duty applies. Preserve those exceptions; a missing certificate alone is not the entire test ([ITO s.32A](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

The old Circular 3/2026 statement also combined withholding failures, cash-law breaches and input-VAT disallowance as though identical. Treat them as separate reviews: current s.32(18) concerns an expense linked to input VAT disallowed for the missing allocation number under VAT Law s.38(a1); cash-law tax consequences have their own conditions. The full circular and cash-limit rules could not be reopened, so the old NIS 6,000 threshold and automatic loss of both deductions are not usable conclusions here ([ITO ss.32(18),32A](https://www.btl.gov.il/Laws1/00_0103_000000.pdf); [israel-vat](israel-vat.md)).

## Worked cases

### Approved rate and an independently established base

Retain the freelancer's consulting net NIS 10,000 and VAT NIS 1,800, invoice payable NIS 11,800. **Assume** professional review of the applicable regulation establishes a VAT-inclusive withholding base of NIS 11,800 and the live certificate validly approves 2% for this payment. Tax withheld is NIS 236, recipient cash NIS 11,564 and remittance NIS 236; total payer outlay remains NIS 11,800. This assumption illustrates the correct reconciliation and does not establish a universal VAT-inclusive base.

```oa-check
name: Confirmed payment base and certificate reconcile payer cash
inputs:
  net_fee: 10000
  vat: 1800
  confirmed_base: 11800
  approved_rate: 0.02
steps:
  - invoice: net_fee+vat
  - withholding: confirmed_base*approved_rate
  - recipient_cash: invoice-withholding
  - payer_total: recipient_cash+withholding
expected:
  invoice: 11800
  withholding: 236
  recipient_cash: 11564
  payer_total: 11800
```

### Qualifying non-resident income and entity distinction

Assume NIS 100,000 is Israeli-taxable income to which s.170(a) applies, no ss.161/164 prior withholding, treaty/assessor reduction, gross-up or exception. An individual at 25% has NIS 25,000 withheld, NIS 75,000 net. An ordinary company to which the 23% s.126 rate applies has NIS 23,000 withheld, NIS 77,000 net. Confirm all source/entity and timing conditions rather than imposing 25% on both.

```oa-check
name: Section 170 individual versus ordinary company
inputs:
  confirmed_income: 100000
steps:
  - individual_tax: confirmed_income*0.25
  - individual_net: confirmed_income-individual_tax
  - company_tax: confirmed_income*0.23
  - company_net: confirmed_income-company_tax
expected:
  individual_tax: 25000
  individual_net: 75000
  company_tax: 23000
  company_net: 77000
```

## When to refuse or refer

Refer missing payer-duty/base/rate evidence, expired or mismatched approvals, noncash consideration, uncertain residence/source/treaty/PE status, royalties, rent and property purchases, gross-ups, retrospective rate changes, missed deposits and deduction-risk cases. Do not apply an arbitrary rate to preserve a payment deadline. An assessor's explicit transaction approval is different from an assumed exemption.

## Filing and payment

Use the actual withholding-file notice for periodic reporting/payment, often using Form 102; its exact monthly/bimonthly cycle and deposit date are not proved by business size alone. For ss.170/171 cases retain the separate statutory baseline above and obtain case-specific procedural confirmation. Late reporting or payment can involve penalties, interest and indexation; establish the applicable provision and current calculation rather than importing an unverified rate or calendar. Keep per-payee legal ID/name/address, payment category, gross/VAT/base, withholding and authority deposits.

Reconcile annual Form 856 payee totals to periodic deposits and the books; employment Form 126 is distinct. Section 166(b)'s statutory baseline is 30 April following the tax year, but live filing/confirmation requirements and extensions must be checked. Form 856 is the **payer's** obligation, not the payee's own return. The Form 806 service requires the annual recipient certificate to show payments, VAT and tax withheld and applies to obligated payers even where no tax was deducted ([ITO s.166](https://www.btl.gov.il/Laws1/00_0103_000000.pdf); [Form 806 service](https://www.gov.il/he/service/itc806)). Retain submission/payment acknowledgment and resolve differences before treating withheld tax as paid.

## Completion checklist

Establish payer obligation and payment category; document residence/source/base; refresh and retain the correct certificate; compute cash plus remittance; apply actual deposit/report route; reconcile periodic/annual returns and recipient certificates; screen deduction risks/exceptions; obtain professional review and keep acknowledgment.

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated Income Tax Ordinance; Read for ss.32(18)/32A deduction conditions/exceptions, 164-167 domestic deduction/report/assessment, 170-173 non-resident scope/rate/exception/deposit/credit/assessment, 126 ordinary company reference | https://www.btl.gov.il/Laws1/00_0103_000000.pdf | 2026-11-14 |
| ITA Interpretation01/2025; Read for introduction giving standard18% on transactions/imports with tax point from1January2025; actual invoice/base conditions remain separate | https://www.gov.il/BlobFolder/policy/vat_11/he/vat_represent-info-051224-2.pdf | 2026-11-14 |
| ITA execution instruction 02/2026; Read for ss.1-4 certificate period/class, 6 online payer lookup/evidence, 10 changed-rate application, 12 transaction/rent limitations; indexed heading retains stale 2021 text but body explicitly gives 2026/2027 dates | https://www.gov.il/BlobFolder/policy/inst-02-2026/he/IncomeTax_inst-02-2026.pdf | 2026-11-14 |
| ITA 2026 deduction booklet; Read for p.15 NIS 5,520 one-off figure and non-salary summary 30% services/assets; detailed regime not established by summary alone | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf | 2026-11-14 |
| ITA Form 806 service; Read for annual certificate content, obligated payer including no-deduction cases, and delivery to recipient | https://www.gov.il/he/service/itc806 | 2026-11-14 |

Not yet confirmed: operative domestic services/assets regulations and payer thresholds, 20% versus30% conditions/47% claim, VAT base and NIS5,520 one-off aggregation/eligibility; domestic rent30%/35%, royalty23%, interest25%, dividend25%-30% withholding defaults; actual treaty relief for each country; periodic102dates and live126/856extensions/confirmation; full Circular3/2026 and cash-law NIS6,000 rule. The circular official PDF returned403; no failed fetch is recorded as read. Old examples assuming a pre-VAT NIS10,000 base give NIS3,000 withholding/NIS8,800 paid at an **unproved30%** default, or NIS200/NIS11,600 paid at an assumed2% approval: these remain conditional historical arithmetic, not approved base/rate instructions. The old universal certificate expiry31December and residence-unknown=>25% defaults are corrected; nocertificate does not prove every payer must withhold.
