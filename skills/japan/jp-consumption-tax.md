---
name: jp-consumption-tax
description: Use this skill whenever asked about Japanese Consumption Tax (消費税 / JCT) for self-employed individuals. Trigger on phrases like "consumption tax", "shohizei", "JCT", "qualified invoice", "invoice system", "T-number", "simplified taxation", "簡易課税", "消費税確定申告", or any question about consumption tax filing, rates, or the qualified invoice system for sole proprietors in Japan. Covers standard rate (10%), reduced rate (8%), qualified invoice system (インボイス制度), simplified taxation (簡易課税), and registration thresholds. ALWAYS read this skill before touching any Japanese consumption tax work.
jurisdiction: JP
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
version: 1.1
type: computation
job: sole-proprietor-consumption-method
---

# Japan consumption tax: sole proprietor computation v1.1

> **General reference only.** This skill prepares AI-assisted working papers. A qualified 税理士 must review the facts, elections, computations and current forms before filing, paying or taking a tax position.

## Scope

This is the 2026 sole-proprietor eligibility and method computation skill. Use `japan-consumption-tax` for transaction classification and return working papers, `jp-etax-filing` for portal submission. Current rules are checked for 2026; final form examples remain the 2025-2026 filing cycle. Currency is JPY. Contributor: Open Accountants Community. The old confidence tiers meant deterministic / judgement / refer, not professional approval; all outputs still require review.

### Quick reference

| Item and conditions | Figure | Official source / provision |
|---|---|---|
| Standard domestic taxable supply | 10% combined, 7.8% national + 2.2% local | [NTA 6102, Consumption Tax Act art.29](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm) |
| Eligible food, excluding alcohol, dining-in and catering; qualifying subscription newspapers issued at least 2 times weekly | 8% combined, 6.24% national + 1.76% local | [NTA 6102, reduced-rate provisions](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm) |
| Sole proprietor base period | 2 calendar years before current year; 2026 uses 2024 (derived) | [NTA 6501, Act art.9](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm) |
| Base-period exemption, subject to specified-period, registration, election, succession and asset restrictions | Taxable sales <=JPY 10,000,000 (source: 1,000万円) | [NTA 6501, Act arts.9 and 9-2](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm) |
| General-method full credit, otherwise allowable business inputs only | Current annualised taxable sales <=JPY 500,000,000 (source: 5億円) AND taxable-sales ratio >=95% | [NTA 6401, Act art.30](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6401.htm) |
| Simplified taxation, effective election and no statutory restriction | Base-period taxable sales <=JPY 50,000,000 (source: 5,000万円) | [NTA 6505, Act art.37](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm) |

## Ask the client first

- Tax year, residence and base-period taxable sales; specified-period sales/wages and any succession or large-asset restrictions.
- Qualified-invoice registration date/number, taxable-person election and cancellation notices.
- Supply mix, domestic/export facts and taxable/exempt turnover by rate.
- Gross/net books, actual eligible input evidence, business use and interim payments.
- Effective simplified election, activity types and split of sales by type; 2割 eligibility.

## The method, step by step

1. Establish taxpayer, taxable period, registration effective dates, base-period taxable sales, specified-period sales and wages, election notices and asset/succession restrictions. Current turnover alone never decides exemption or simplified eligibility. For a domestic sole proprietor, specified period is January 1-June 30 of the previous year; the taxpayer may use wages paid instead of sales for the JPY 10,000,000 test. Non-resident operators cannot use the wages substitution for periods beginning on/after 2024-10-01. [Act arts.9,9-2; NTA 6501](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm).
2. Reconcile invoice sales, credit notes, accruals and bank receipts. Identify whether every amount is gross or net. Gross standard-rate sales /1.10 and gross reduced-rate sales /1.08 give net amounts; net sales multiply by the applicable rate. Never apply 10/110 to a net amount. Maintain export, exempt and outside-scope categories separately. [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm).
3. General method: compute national output by rate; accumulate eligible national input tax from retained evidence. Separate business/private use and apply full-credit or partial-exemption rules. Export sales belong in the taxable-sales numerator; exempt sales affect the denominator. Individual allocation is taxable-only inputs plus common inputs times the ratio; lump-sum proportional allocation applies the ratio to all eligible inputs and has a continuity restriction. Escalate allocation beyond this small-business computation. [Act art.30; NTA 6401](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6401.htm).
4. Compute only legally available alternatives. Simplified taxation replaces actual purchase credits; 2割特例 also replaces actual input credit. Do not add actual credits to deemed credits. The valid elected simplified method cannot simply be abandoned for a lower general-method bill; test election/termination rules. Under 2割特例, national net tax is national output after sales-return adjustments times 20%, with local tax then derived from that national balance. Compare methods on identical gross/net, rate and period assumptions. [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm), [NTA 6505](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm).
5. Preserve national and local balances separately: local tax is the net national assessment times 22/78, subject to the current return's rounding. A combined-tax estimate already includes local tax; never add 22/78 to a 10% combined amount. Deduct national and local interim payments in their respective fields and reconcile final payable/refund. Map field labels using the current method-specific form, not the old invented universal boxes. [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm).

## Boundary and exception table

### Invoice and method exceptions

| Rule and full conditions | Treatment | Official source |
|---|---|---|
| Ordinary qualified invoice | Issuer name/registration, transaction date, description including reduced-rate marker, rate-separated consideration and rate, tax by rate, recipient name; simplified invoices have permitted omissions | [Act arts.30,57-4; NTA 6625](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6625.htm) |
| Registration number | T +13 digits; registration is obtained by application, not mandatory for every business | [Act art.57-2; NTA 6498](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm) |
| Otherwise eligible purchases from unregistered suppliers with required books and invoice-equivalent evidence | 80% through 2026-09-30; 70% from 2026-10-01 through 2028-09-30; 50% from 2028-10-01 through 2030-09-30; 30% from 2030-10-01 through 2031-09-30; 0% thereafter | [FY 2026 invoice reform](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm) |
| Supplier-specific transitional purchase cap (gross purchase amount, excess excluded); period beginning from 2024-10-01, then from 2026-10-01 | JPY 1,000,000,000 (source: 10億円), reduced to JPY 100,000,000 (source: 1億円) for periods beginning on/after 2026-10-01; calendar 2026 retains earlier cap | [NTA 6498, amended transitional law](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm) |
| 2割特例, would otherwise be exempt but taxable because of invoice registration; no asset restriction, specified/base-period compulsory liability or shortened taxable period | National output after returns times 20%; applies to periods containing any date 2023-10-01 through 2026-09-30, including eligible calendar 2026; elect on return | [2016 Amending Act supplementary art.51-2; NTA 2割 guidance](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0023011-048_01.pdf) |
| Simplified deemed credit ratios, by actual transaction type | Type 1 wholesale 90%; type 2 retail and food-selling agriculture/forestry/fisheries 80%; type 3 other primary production, mining, construction, manufacturing/utilities 70%; type 4 other including restaurants 60%; type 5 transport, finance/insurance, services excluding restaurants 50%; type 6 real estate 40% | [Act art.37, Order art.57; NTA 6505](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm) |
| Multiple business types | Allocate output tax by type; optional single-type ratio only if that type's taxable sales are >=75% of total. For >=3 types, qualifying 2 types together >=75% allow the statutory higher/lower allocation. Unclassified portion uses lowest ratio among relevant unclassified types | [NTA 6505 calculation exceptions](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm) |
| Simplified election timing | Normally before period starts; registration-period concession and post 2割/3割 transition exceptions apply. New transition deadline is following period's return deadline if that period ends on/after 2026-10-01; earlier-ending period uses its end. Normally locked for 2 years | [NTA 6505 procedure and FY 2026 reform](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm) |

Missing supplier status does not establish entitlement to transitional credit. Check evidence and caps first. Ordinary books-only exceptions are real: do not state that absence of an invoice always bars every input credit. [NTA 6497](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6497.htm). Purchases under simplified taxation/2割 do not generate additional actual input credits. Invoice-registration cancellation and a taxable-person election are separate notices; cancellation does not automatically restore exemption. Have the reviewer confirm the effective dates and lock-ins.

### Supply boundaries and former edge cases

Food takeout can be reduced-rated; dine-in, alcohol and catering are standard-rated. A foreign payer does not prove export exemption: obtain contract, non-resident status and where the benefit is directly enjoyed. Japan property/storage, meals/lodging and similar direct domestic benefits can defeat it; domestic real-estate intermediary services have a 2026-10-01 amendment and earlier-contract exception. Export evidence retention is 7 years. [Act art.7; NTA 6551](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm).

Land and securities transactions, interest/insurance, qualifying medical/education, burial/cremation and residential rent have defined exemptions; land/residential leases under 1 month and parking facilities have exceptions. Gifts, subsidies, insurance proceeds and loan principal must be tested as non-consideration/outside scope, not automatically labelled exempt sales. [NTA 6201](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6201.htm).

The former JPY 9,800,000 base /JPY 11,000,000 specified-sales case needs the wages alternative and all other liability tests. The former JPY 8,000,000 unregistered case is exempt only after those tests. A missed prior-year election normally prevents simplified taxation, but test the registration/post 2割 exceptions above. No largest-sales default is lawful for mixed types. For taxable sales <=JPY 500,000,000 with ratio <95%, partial allocation still applies. Foreign digital supplies require `japan-consumption-tax` cross-border screening.

For invoice cancellation, submit `適格請求書発行事業者の登録の取消しを求める旨の届出書` by the day 15 days before the desired next period starts. A later submission defers effect to the following period; no holiday extension applies to this cancellation deadline. Separate taxable-person-election and asset lock-ins still apply. An exempt operator registered under the transition outside the period containing 2023-10-01 remains taxable through the period containing the date 2 years after registration, even after cancellation. [NTA 6629, Act art.57-2 and notice exceptions](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6629.htm), [NTA registration lock-in FAQ](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/sinkijigyousha/faq_k08.pdf).

Goods/asset export evidence change from 2026-10-01: for a transfer or lease made as an export from Japan, if the proceeds are received in cash or by a method that does not clearly establish payment from the transaction counterparty, retain destination-country customs import permission or other proof of actual import, including electronic records, in addition to the ordinary export evidence. NTA examples include direct crypto payment without a crypto exchange and payment from a person other than the counterparty. A bank transfer/documentary-bill settlement that clearly identifies the counterparty does not trigger this extra requirement; the third-party example excludes a guarantor or another person clearly obliged to pay the transaction debt. Do not apply this goods/asset-export rule automatically to exported services. If the payment trail or required destination import proof is missing, hold export-exemption treatment for the affected transaction and refer for evidence review. [Consumption Tax Act art.7, Enforcement Order art.17, Regulations art.5; NTA 6551, cash-receipt section](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm).

## Worked cases

Case 1, general method: tax-INCLUSIVE receipts JPY 16,500,000 and wholly eligible purchases JPY 3,300,000, all standard-rated. Net sales JPY 15,000,000; national output JPY 1,170,000, input JPY 234,000, national balance JPY 936,000, local JPY 264,000, total JPY 1,200,000 before interim credits. Inputs are hypothetical, national/local method from [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm).

```oa-check
name: General method gross-to-national-and-local
inputs:
  sales_gross: 16500000
  purchases_gross: 3300000
steps:
  output: sales_gross / 1.10 * 0.078
  input_credit: purchases_gross / 1.10 * 0.078
  national: output - input_credit
  local: national * 22 / 78
  total: national + local
expected:
  national: 936000
  local: 264000
  total: 1200000
```

Case 2, method decision: eligible invoice-transition consultant, gross sales JPY 8,800,000, general-method combined eligible input JPY 200,000, valid type 5 simplified election and 2割 entitlement independently established. Output combined JPY 800,000. General-method benchmark JPY 600,000, simplified JPY 400,000,2割JPY 160,000.2割 is lower; election on the return must be documented. The general-method result is a benchmark only if a binding simplified election prevents using it for this period. These are combined-tax comparison amounts, not an extra base for local tax. [NTA 6505](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm), [2割 guidance](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0023011-048_01.pdf).

```oa-check
name: Eligible general simplified and two-wari comparison
inputs:
  sales_gross: 8800000
  actual_input_combined: 200000
steps:
  output_combined: sales_gross / 1.10 * 0.10
  general: output_combined - actual_input_combined
  simplified: output_combined * (1 - 0.50)
  two_wari: output_combined * 0.20
  saving: min(general, simplified) - two_wari
expected:
  general: 600000
  simplified: 400000
  two_wari: 160000
  saving: 240000
```

Additional retained test scenarios, gross amounts explicitly: old JPY 15,000,000 sales /JPY 3,000,000 purchases -> unrounded combined difference JPY 1,090,909.09; JPY 8,000,000 consultant sales -> unrounded simplified JPY 363,636.36; JPY 6,000,000 eligible 2割 sales -> unrounded JPY 109,090.91; food JPY 5,000,000 plus dine-in JPY 2,000,000 -> unrounded output JPY 552,188.55. These are diagnostics before statutory form rounding, not ready-to-file balances. [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm).

## When to refuse or refer

Do not file an exempt operator's return as though taxable. Do not treat invoice registration alone as 2割 eligibility. Refer partial exemption, unusual industry classification, foreign operators, asset-lock or election disputes. Never use 8% for alcohol/dine-in, claim personal/exempt inputs, invent exports, mix national/combined figures or present estimates as definitive. Do not issue qualified invoices while unregistered.

## Filing and payment

### Filing and interim calendar

| Obligation and conditions | Deadline or amount | Official source |
|---|---|---|
| Calendar 2026 individual final JCT return/payment | 2027-03-31; established automatic transfer 2027-04-30 | [NTA annual calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Latest final 2025 individual JCT return/payment,2025-2026 filing cycle | 2026-03-31; established automatic transfer 2026-04-30 | [NTA annual calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Corporation, ordinary final return | Within 2 months after period end; approved corporate extension can add 1 month for the year-end period | [Act arts.45,45-2; NTA 6601](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6601.htm) |
| Optional monthly/quarterly shortened periods | Generally within 2 months after period end; individual period containing December 31 is due March 31 | [Act arts.19,45; NTA 6601](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6601.htm) |
| Prior annual NATIONAL tax, local excluded, <=JPY 480,000 (source: 48万円) | No mandatory interim return; optional system exists | [Act arts.42-44; NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |
| Prior annual national tax >JPY 480,000 (source: 48万円) to JPY 4,000,000 inclusive | 1 interim, prior tax times 6/12 plus local 22/78 | [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |
| Prior annual national tax >JPY 4,000,000 to JPY 48,000,000 inclusive | 3 interims, each prior tax times 3/12 plus local 22/78 | [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |
| Prior annual national tax >JPY 48,000,000 | 11 interims, each prior tax times 1/12 plus local 22/78; special initial-month timing | [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |

Interims generally fall due within 2 months after the covered period; individual monthly January-March amounts have special May-end timing. Short prior periods, corporate extension and deemed interim returns need the actual NTA notice. Interim provisional-account returns cannot produce a refund. [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm). Do not confuse shortened taxable periods with interim periods. A taxable operator with no taxable supplies/specified purchases and no tax due may have no filing duty but can claim an eligible input/interim refund. [NTA 6605](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6605.htm).

Use e-Tax or current paper `消費税及び地方消費税の確定申告書`, with method-specific付表. Enter base-period sales, tax classification/method, output by rate, credit schedules and separate national/local interim payments. Save return, receipt, invoices and election evidence. Submission does not pay the tax.

## Completion checklist

Confirm status and period, method eligibility, rate split, invoice/exception evidence, transition dates/caps,95% condition, gross/net consistency, national/local reconciliation, interim credits, deadlines and reviewer signoff. Penalties/interest are fact/date dependent; do not reuse a stale penalty table.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTA 6102: Read for rate splits and reduced-rate exclusions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm | 2026-11-14 |
| NTA 6501: Read for base/specified-period exemption and exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm | 2026-11-14 |
| NTA 6351: Read for national computation and gross/net methods | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm | 2026-11-14 |
| NTA 6401: Read for full versus partial input credit | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6401.htm | 2026-11-14 |
| NTA 6505: Read for eligibility, ratios, mixed types, election exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm | 2026-11-14 |
| NTA 6497: Read for books/invoice requirements and exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6497.htm | 2026-11-14 |
| NTA 6498: Read for registration and transitional cap | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm | 2026-11-14 |
| NTA 6625: Read for invoice fields | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6625.htm | 2026-11-14 |
| NTA reform: Read for 2026 credit timeline and election transition | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm | 2026-11-14 |
| NTA two: Read for 2割 period and exclusions | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0023011-048_01.pdf | 2026-11-14 |
| NTA 6551: Read for export boundaries, 2026-10-01 cash/unclear-payer destination import evidence and exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm | 2026-11-14 |
| NTA 6201: Read for exempt supplies and exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6201.htm | 2026-11-14 |
| NTA 6601: Read for final/shortened-period filing | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6601.htm | 2026-11-14 |
| NTA 6605: Read for nil activity refund boundary | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6605.htm | 2026-11-14 |
| NTA 6609: Read for national-only interim boundaries and timing | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm | 2026-11-14 |
| NTA 6629: Read for invoice cancellation deadline, no-holiday rule and election exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6629.htm | 2026-11-14 |
| NTA registration lock-in FAQ: Read for cancellation versus 2-year taxable status and first-period exception | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/sinkijigyousha/faq_k08.pdf | 2026-11-14 |
| NTA dates: Read for 2025 and 2026 individual calendar | https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm | 2026-11-14 |

Not yet confirmed: Final 2026 method-specific forms and box numbering are not yet checked; use the latest 2025-2026 filing cycle only for form orientation. Specific penalty/interest assessment is outside this computation. No unsupported rate is authorised by this line.
