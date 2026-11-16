---
name: ai-gst
description: "Anguilla General Services Tax (GST) for ordinary domestic taxable services in 2026, under the General Services Tax Act, 2025 (in force 1 August 2025). Covers the registration tests (XCD 300,000 actual or expected), the 13% rate, tax-exclusive and tax-inclusive invoice arithmetic (13/113), supported input credits and the s 25 apportionment, monthly returns due on the 20th, payment, records, and the IRD return lines. Use for Anguilla GST, service invoices, taxable turnover, GST registration or input tax. Separates Goods Tax from services tax and identifies imported services as a separate obligation. Later amendments and complete specialised classifications remain unresolved; requires professional review before calculating an engagement liability."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ai-gst"
  jurisdiction: "AI"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Anguilla General Services Tax: ordinary services v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Written by Ryan Duguid; imported from his fork and brought to the repository standard. Built from the law. Not yet approved by an accountant. Tax year 2026.

## Scope

Establish the applicable period law and supply classification before calculating GST. This companion supplies substantive rules for an ordinary domestic taxable service, an ordinary registration test and a supported domestic input credit. Load `workflow-base` for procedure, outputs and universal refusals. The reviewer receives working papers for professional review.

Specialised supplies, exports, exemption schedules, accommodation, mixed activities beyond the stated allocation rule, imported-service valuation, tariffs, assessments, penalties and refunds require their complete applicable provisions. Goods Tax, Social Security and Universal Social Levy are separate obligations (payroll levy: [ai-payroll](ai-payroll.md)). No general absence of income, corporate, withholding or capital gains tax is established here.

### Period coverage and source currency

The figures below describe the [*General Services Tax Act, 2025*](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) as enacted, with commencement on 1 August 2025 under s 107. The [IRD General Services Tax page](https://www.ird.gov.ai/Services/Tax/GenST), read on 14 November 2026, confirms that the tax came into force on 1 August 2025 and lists the 2025 Act, the 2025 Regulations and the Goods Tax Act, 2025 as the governing texts; the [IRD document library](https://www.ird.gov.ai/MediaCenter/Documents), read the same day, lists no General Services Tax amendment Act or regulations after 2025. The figures are therefore used for tax year 2026. A complete later amendment chain has not been verified from the gazette; the editing date does not certify current 2026 liability.

Before an engagement calculation, record the requested period, operative statutory version, applicable amendments and regulations, registration notice and evidence establishing the ordinary supply classification. If those cannot be verified, fire `R-AI-GST-PERIOD`; do not produce a payable estimate from this baseline. The worked examples illustrate stated legislative assumptions and cannot establish an actual liability. Apply this source check when using any rate or computation section separately.

Version history: version 0.2 (Ryan Duguid, 12 October 2026) corrected registration pinpoints in this bounded 2025 legislative reference. Version 0.3 (14 November 2026) moved the text to the repository's method headings, made every link inline, set tax year 2026 and added the IRD return guide's line numbers, due-date roll and penalties. Complete post-2025 amendments, specialised schedules, operational rounding and calendar exceptions remain unverified.

## Ask the client first

1. Which month (tax period) is being prepared, and is the person registered (GST certificate, TIN, effective date)?
2. Actual taxable supplies in the last 12 months or fewer, and expected supplies in the next 12 months (registration tests).
3. What is the service, where are the supplier and customer, and is the price tax-exclusive or tax-inclusive?
4. Invoice, completion and payment dates (tax point).
5. Input invoices held, and whether each purchase is used for taxable, exempt or mixed supplies.
6. Any excess credit carried from earlier periods, imported services and Comptroller notices.

Establish the period, reviewer, entity and taxable-person status; actual and expected taxable supplies; special registration facts; supplier/customer location and service category; invoice, completion and consideration dates; inclusive/exclusive pricing; input invoices and taxable use; notified tax periods, opening credits and actual authority decisions. Collect facts through the base's structured form; keep required document requests in the action list. Do not request or submit bank details or actual identity documents through this guide.

## The method, step by step

### Period-specific figures

All monetary examples use Eastern Caribbean dollars, XCD, consistent with the [official GST return](https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf). Amounts in this table are the enacted 2025 Act, applied to 2026 subject to the period check above.

| Rule | Figure or period, 2026 | Primary provision |
|---|---|---|
| Ordinary positive GST rate | 13% | [Act s 8(1)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf); [IRD return guide, line 3](https://www.ird.gov.ai/Content/documents/GST%20GUIDE%20-COMPLETING%20THE%20GENERAL%20SERVICES%20TAX%20RETURN.pdf) |
| Tax fraction on a tax-inclusive price | 13/113 | [IRD return guide, line 4](https://www.ird.gov.ai/Content/documents/GST%20GUIDE%20-COMPLETING%20THE%20GENERAL%20SERVICES%20TAX%20RETURN.pdf) |
| Actual taxable-supply registration test | At least XCD 300,000 in 12 or fewer months | [Act s 10(1)(a)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Expected taxable-supply registration test | At least XCD 300,000 in an expected 12-month period | [Act s 10(1)(b)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Actual-test application | Within 15 days of the end of the tested period | [Act s 10(1)(a)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Expected-test application | Within 15 days of the beginning of the tested period | [Act s 10(1)(b)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Ordinary tax period | Calendar month as notified by the Comptroller | [Act s 30](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Return, including a nil return | Within 20 days after the tax period; the IRD guide says on or before the 20th, or the next working day if the 20th falls on a weekend or public holiday | [Act s 31](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf); [IRD return guide, 1.0](https://www.ird.gov.ai/Content/documents/GST%20GUIDE%20-COMPLETING%20THE%20GENERAL%20SERVICES%20TAX%20RETURN.pdf) |
| Ordinary period payment | By the return due date | [Act s 43(1)(a)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Imported-service return and payment | Within 20 days after import, or another time allowed by the Comptroller | [Act s 22](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| GST record retention | Seven years after the end of the relevant tax period | [Act s 61(2)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |

### Primary source library

Use the [Act](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf), [*General Services Tax Regulations, 2025*](https://www.ird.gov.ai/Content/documents/22%20-%20General%20Services%20Tax%20Regulations,%202025%20-%20G.pdf), [*Goods Tax Act, 2025*](https://www.ird.gov.ai/Content/documents/Act%209%20-%20Goods%20Tax%20Act,%202025%20-%20G.pdf) and [blank GST return](https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf). Read statutory conditions in context; a form summarises reporting and does not settle every penalty or credit entitlement. [The IRD document library](https://www.ird.gov.ai/MediaCenter/Documents) is discovery evidence, not proof of an unchanged amendment chain. `references.md` records source hashes, selected-page checks and remaining pack gaps.

### Registration

Reconcile taxable supplies for the actual and expected tests separately. Equality satisfies each XCD 300,000 test. [Act ss 9 to 11](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) also govern persons required to register, compulsory registration and effective dates. A person required to register is a taxable person even before receiving a certificate.

The actual-test ordinary effective date is the beginning of the following tax period under s 11(4)(a). The expected-test date is the beginning of the tested 12-month period under s 11(4)(b). Where a person required to register fails to apply, the Comptroller may register the person from the date determined by the Comptroller under s 11(3).

State/statutory-body, auctioneer and accommodation-provider cases have special registration treatment under ss 10(6), (7), (8). Under s 10(2), the Comptroller may have regard to related persons or persons acting in concert; s 10(3) values supplies under s 15. The cessation or capital-replacement condition in s 10(4) requires the Comptroller to be satisfied before the ordinary registration requirement is displaced. Voluntary registration has conditions under s 10(5) and the [regulations](https://www.ird.gov.ai/Content/documents/22%20-%20General%20Services%20Tax%20Regulations,%202025%20-%20G.pdf). Do not treat these as automatic exclusions from turnover. Refer a special case before applying an ordinary threshold calculation.

### Ordinary output GST

After the period and classification checks, establish the taxable person's domestic taxable service and its value under [Act ss 8, 13 to 15](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf). The tax point generally uses the earliest completion, invoice or receipt of consideration under s 13(1); periodic and other supplies have distinct rules. Supplier location alone does not settle every service: s 14 contains benefit-location and other exceptions, including professional services.

For an established positive-rate service valued excluding tax, output GST is value x 13 / 100. For a tax-inclusive consideration, contained GST is gross x 13 / 113. Do not add 13% to an already inclusive price. The [official return](https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf) confirms the inclusive fraction. Discounts, related parties, deposits, vouchers and adjustments need their applicable provisions before changing the value or tax point.

### Supported input tax and period reconciliation

[Act ss 23 to 25](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) require deductible input tax, taxable use and the applicable documentary evidence. Purchase value is not the credit. Record actual eligible GST separately from the price. A tax invoice or relevant note ordinarily must be held when filing under s 24(2). The Comptroller's exception in s 24(3) needs reasonable efforts, absence of purchaser fault and the correctly due amount; do not assume permission.

Direct taxable-use input may qualify; direct exempt-use input does not. For common input, s 25(3)(c) ordinarily allocates A x B / C. A is eligible period input tax less input directly allocated to taxable or exempt supplies; B is the value of taxable supplies made during the period; C is the value of all supplies made during the period. The special comparisons in s 25(4) are strict: a taxable share above 0.90 permits the specified full common credit; below 0.10 permits none. At exactly 0.90 or 0.10, apply the ordinary formula. Confirm all statutory categories, blocked credits and any approved alternative before using this allocation. A zero denominator needs source-supported treatment; do not divide by zero or invent an allocation.

For the bounded ordinary case, net period GST is output GST less supported deductible input GST under s 23. Reconcile adjustments, imported services and prior credits separately. An excess input amount is not an automatic cash refund; s 35 imposes carry-forward and refund conditions. The [IRD return guide, line 19](https://www.ird.gov.ai/Content/documents/GST%20GUIDE%20-COMPLETING%20THE%20GENERAL%20SERVICES%20TAX%20RETURN.pdf) describes the excess credit as carried forward to the next three tax periods, with a refund application possible if the remaining excess is EC$1,000 or more at the end of the third period; check s 35 before relying on it. An opening credit cannot be deducted twice through both current input and the prior-credit line on the [return](https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf).

The [Goods Tax Act](https://www.ird.gov.ai/Content/documents/Act%209%20-%20Goods%20Tax%20Act,%202025%20-%20G.pdf) uses the relevant Goods Tax column in the Integrated Customs Tariff for imported goods. A goods import value or Goods Tax payment is not automatically deductible General Services Tax. [Act ss 21 and 22](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) impose a distinct imported-service obligation; ordinary registration turnover does not create a universal exemption from it. Imported-service calculations are outside this companion's bounded computation.

### Returns, payment and records

Use the notified monthly period and retain nil-return obligations under [Act ss 30 and 31](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf). A filing extension under s 32 does not itself extend payment. Section 43(3) payment arrangements do not change the due date used for interest. Do not roll a nominal deadline over weekends or holidays without the applicable authority decision or law; the IRD return guide's next-working-day statement is that authority statement, so record it as the basis when used.

[Act s 61](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) requires a GST account and relevant original invoices, notes, import/export and accounting records in Anguilla, in English, for the stated retention period. Its retail point-of-sale requirement needs separate attention for a retail supplier. This guide supplies no statutory penalty, interest or refund computation; the IRD guide's stated penalties are under Filing and payment.

### Conservative defaults

These are disclosed working-paper treatments inside verified law, subject to the base's questions and refusal procedure. They do not replace statutory evidence.

| Missing fact | Treatment and disclosure | Primary condition |
|---|---|---|
| Documentary entitlement to an otherwise identified input credit | Claim zero pending evidence; disclose the potential credit and tax difference; obtain the document or actual Comptroller permission | [Act s 24(2), (3)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Business/taxable use of a purchase is unsubstantiated | Use zero deductible credit pending evidence and disclose the possible difference | [Act ss 24 and 25](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Claimed exemption or zero rating lacks its applicable classification evidence | Stop the affected engagement under R-AI-GST-SPECIAL; a foreign customer or untaxed invoice does not establish the classification | [Act ss 8, 14, 21](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |
| Rate, operative law, deadline or registration status is unresolved | Needs input and the relevant refusal; no invented higher rate, cap or date | [Act ss 8 to 11, 30 to 32, 43](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) |

### Reviewer attention and question thresholds

Every position requires professional review, regardless of amount. The cash threshold for an automatic reviewer flag and an unresolved fact question is XCD 0: disclose every nonzero tax difference. This is a companion review policy, not a statutory threshold. Flag source currency, classification, registration, unsupported credits and approaching or disputed deadlines regardless of cash difference. Apply the base's no-effect, description-answered, grouping and ten-question limits.

## Worked cases

These examples use the enacted 13% rule, an established ordinary taxable service and a verified illustrative classification. They are not current-law confirmation or an actual return. No opening credit, reverse charge or adjustment exists unless stated. Figures are exact and need no penny-rounding convention. Results are derived from the rule cited on the row.

| Position and supplied hypothetical facts | Computation and result (derived) | Rule and review consequence |
|---|---|---|
| 1. Tax-exclusive ordinary service, XCD 1,000 | 1,000 x 13 / 100 = 130 output GST; invoice total 1,130 | [Act ss 8 and 15](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf); verify ordinary classification and period before engagement use |
| 2. Tax-inclusive ordinary service, XCD 2,260 | 2,260 x 13 / 113 = 260 GST; value excluding tax 2,000 | [Act s 15](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) and [return](https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf); reconcile gross as 2,000 + 260 |
| 3. Period output XCD 650 and documented eligible domestic input GST XCD 130 | 650 - 130 = 520 net period GST | [Act ss 23 and 24](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf); input is actual eligible tax, not purchase value |
| 4. Common eligible input A = XCD 100, B = taxable supply value 4,000, C = total relevant supply value 5,000; no alternative allocation | Taxable share 4,000 / 5,000 = 0.80; credit 100 x 4,000 / 5,000 = 80; with output 520, net is 440 | [Act s 25(3)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf); verify statutory B/C composition and blocked credits |
| 5. Output XCD 650; potential XCD 130 input credit has no required invoice or Comptroller permission | Provisional input credit zero; net 650. With established entitlement, alternative net 520; difference 130 | [Act s 24(2), (3)](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf); Assumed, disclose missing invoice and the difference, obtain reviewer evidence |

For a separate registration boundary, verified ordinary taxable supplies of XCD 300,000 in the actual tested period satisfy equality; XCD 299,999 alone does not satisfy that test. The expected test or a special registration rule may still apply. [Act s 10](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf) supplies the tests, not a general below-threshold tax exemption.

### Case 1: tax-exclusive and tax-inclusive invoices (positions 1 and 2)

A registered consultant invoices XCD 1,000 plus GST to one client and quotes XCD 2,260 GST-inclusive to another. Output GST is 130 on the first (invoice total 1,130) and 260 contained in the second (value 2,000). Total output GST for the two supplies is 390.

```oa-check
name: Anguilla GST, exclusive 1,000 and inclusive 2,260 at 13%
inputs:
  exclusive_value: 1000
  inclusive_price: 2260
  rate: 0.13
steps:
  - gst_exclusive: exclusive_value * rate
  - invoice_total: exclusive_value + gst_exclusive
  - gst_inclusive: inclusive_price * 13 / 113
  - value_ex_gst: inclusive_price - gst_inclusive
  - total_output: gst_exclusive + gst_inclusive
expected:
  gst_exclusive: 130
  invoice_total: 1130
  gst_inclusive: 260
  value_ex_gst: 2000
  total_output: 390
```

### Case 2 (decision): claim the input credit now or hold it (positions 3 to 5)

Output GST for the month is XCD 650. A purchase carries XCD 130 of GST, but the tax invoice is missing. Holding the credit until the invoice arrives gives net GST of 650; with the invoice held, net GST is 520. The figure that decides is whether s 24(2) evidence exists at filing: without it, file at 650 and disclose the 130 difference. Separately, a common input of XCD 100 with taxable supplies of 4,000 out of 5,000 gives a credit of 80 (share 0.80, inside the 0.10 to 0.90 band, so the ordinary formula applies).

```oa-check
name: Anguilla GST, input credit held or claimed, and s 25 apportionment
inputs:
  output_gst: 650
  input_gst: 130
  common_input: 100
  taxable_supplies: 4000
  total_supplies: 5000
steps:
  - net_without_invoice: output_gst - 0
  - net_with_invoice: output_gst - input_gst
  - difference: net_without_invoice - net_with_invoice
  - taxable_share: taxable_supplies / total_supplies
  - common_credit: common_input * taxable_supplies / total_supplies
  - net_after_common: net_with_invoice - common_credit
expected:
  net_without_invoice: 650
  net_with_invoice: 520
  difference: 130
  taxable_share: 0.80
  common_credit: 80
  net_after_common: 440
```

## When to refuse or refer

Use these messages verbatim when their trigger applies, together with the universal catalogue in `workflow-base`.

| Code | Trigger | Output message |
|---|---|---|
| R-AI-GST-PERIOD | Applicable period law, amendments or relevant regulatory conditions cannot be verified | I cannot calculate an Anguilla GST liability until the applicable period law and required source conditions are verified. Obtain the operative legislation and professional review. |
| R-AI-GST-SPECIAL | The calculation needs an unsupported import, export, exemption, accommodation, special valuation, adjustment, penalty or refund rule | This Anguilla GST companion does not establish the rules needed for this specialised calculation. Load the applicable primary provisions and a suitable companion, or consult an Anguilla tax professional. |
| R-AI-GST-AMBIGUITY | More than ten unresolved grouped fact questions remain after the base's filtering rules | The Anguilla GST records contain more unresolved grouped questions than this workflow can handle. Obtain a reconciled fact schedule and professional review before calculation. |

## Filing and payment

The [IRD return guide (August 2025)](https://www.ird.gov.ai/Content/documents/GST%20GUIDE%20-COMPLETING%20THE%20GENERAL%20SERVICES%20TAX%20RETURN.pdf) sets out the return in the order the filer meets it:

1. Register on the IRD web portal at services.gov.ai to file and pay online, or use the paper [GST return form](https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf). Amounts are in XCD; a nil return is required for a period with no transactions.
2. Section A: TIN, taxable person, trade name, tax period (calendar month) and due date.
3. Section B, output tax: line 1 exempt supplies; line 2 zero-rated supplies; line 3 standard-rated supplies at 13% inclusive of GST; line 4 GST chargeable (line 3 x 13/113); line 5 reverse charge on imported services (amount paid x 13%); line 6 adjustments for earlier periods; lines 7 to 9 are totals (line 9 = lines 4 + 5 + 6).
4. Section C, input tax: line 10 value of domestic purchases; line 11 GST paid on domestic purchases (tax invoice or agreement required); line 12 value of imports; line 13 GST on imported services (reverse charge); line 14 = lines 11 + 13; line 15 adjustments; line 16 total input tax. Apportion lines 11, 13 and 15 for mixed supplies and exclude input tax not claimable under s 24.
5. Section D: line 17 = line 9 minus line 16; line 18 excess credit brought forward; line 19 net GST payable or excess credit.
6. File and pay on or before the 20th of the following month, or the next working day if the 20th falls on a weekend or public holiday.

Penalties stated in the IRD guide, section 3.0 (statutory provisions not separately verified here): late filing, the greater of XCD 50 per day or part day up to XCD 2,000, or 10% of tax payable for each month or part month the return is outstanding (the XCD 50 per day rule applies to a late nil or credit return); late payment, 20% of the amount due plus interest of 1% for each month or part month outstanding.

Retain all four base outputs. Add a source-currency and registration schedule, supply classification and tax-point columns, tax-exclusive value, output GST, actual input GST, allowed input, documentary reference, allocation and prior-credit reconciliation. The brief states whether source currency was verified and distinguishes a provisional working-paper amount from a payable instruction. The action list and review checklist include every source gap, assumption and refusal clearance. A refused engagement receives the base's refusal output, not a filing-ready workbook.

## Completion checklist

Verify the period law before every applied figure. Reconcile inclusive and exclusive prices, check both registration tests and equality, trace every credit to actual GST and entitlement, verify common-input boundaries, separate Goods Tax and imported services, prevent duplicate opening credits, reconcile nil returns and payment dates, and retain every source item once. Check all five example rows independently. Record every universal and topical refusal in the trace. The eighteen base checks and professional sign-off still apply.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRD, General Services Tax page: read for the 1 August 2025 commencement, the 20th-day remittance and the list of governing texts | https://www.ird.gov.ai/Services/Tax/GenST | 2026-11-14 |
| IRD document library: read for the list of GST and Goods Tax texts (no General Services Tax amendment after 2025 listed) | https://www.ird.gov.ai/MediaCenter/Documents | 2026-11-14 |
| IRD, Guide to completing the General Services Tax return (August 2025): read for lines 1 to 19, the 13% rate and 13/113 fraction, the 20th or next working day due date, excess-credit carry-forward and section 3.0 penalties | https://www.ird.gov.ai/Content/documents/GST%20GUIDE%20-COMPLETING%20THE%20GENERAL%20SERVICES%20TAX%20RETURN.pdf | 2026-11-14 |
| IRD, General Services Tax return form: read for XCD, the 13% line and 13/113 fraction, and the input and prior-credit lines | https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf | 2026-11-14 |
| General Services Tax Act, 2025 (Act 8 of 2025, scanned PDF): read on 14 November 2026 by OCR for s 8(1) (13%), s 10(1) (EC$300,000, 15 days), s 22 (20 days after import), s 31 (20 days after the period), s 43(1), s 61 (7 years) and s 107 (1 August 2025); ss 9, 11 to 15, 23 to 25, 30, 32 and 35 rest on Ryan Duguid's reading of 11 October 2026 | https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf | 2026-11-14 |
| General Services Tax Regulations, 2025: read by Ryan Duguid for conditional voluntary registration and specialised cases | https://www.ird.gov.ai/Content/documents/22%20-%20General%20Services%20Tax%20Regulations,%202025%20-%20G.pdf | 2026-10-11 |
| Goods Tax Act, 2025: read by Ryan Duguid for the separation of the tariff-based tax on imported goods | https://www.ird.gov.ai/Content/documents/Act%209%20-%20Goods%20Tax%20Act,%202025%20-%20G.pdf | 2026-10-11 |

Not yet confirmed: any amendment to the General Services Tax Act, 2025 or its Regulations after enactment (no gazette search done; the IRD library lists none); the Act is a scanned PDF with no text layer, read by OCR, so a misread digit cannot be ruled out without the page image; ss 9, 11 to 15, 23 to 25, 30, 32 and 35 were not re-read on 14 November 2026; the statutory basis of the IRD guide's penalties, interest and EC$1,000 refund floor (s 35 and the penalty sections not read in this pass); the next-working-day roll as a matter of statute; specialised schedules, exports, exemptions, accommodation and imported-service valuation; operational rounding.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ai-gst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ai-gst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
