---
name: bd-corporate-income-tax
description: "Bangladesh corporate income tax for assessment year 2026-2027: enacted company classifications and banking conditions, resident/non-resident bases, selected withholding and current filing/advance-tax rules."
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.1
type: computation
category: international
---

# Bangladesh corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Ordinary Bangladesh corporate income tax, assessment year 2026-2027. The cited enacted rate schedule also covers later years, but do not apply a future period without checking amendments. Specific sectors, exemptions, minimum/final tax, losses and cross-border relief require their own provisions.

## Ask the client first

- Income/assessment period, residence and company/sector status.
- Listing, paid-up capital and share transfer method/percentage.
- Complete banking evidence, audited accounts and tax-adjustment schedule.
- Payment/recipient categories, residency, treaty certificates, source tax and instalments.

## The method, step by step

### Rates, bands and thresholds

| Class and complete condition | Rate | Official source |
|---|---|---|
| Ordinary non-listed/other company under section 2(31), excluding special classes | 27.5%; 25% if all types of transactions in the income year occur through bank transfer | Finance Act schedule 2 part 1 D(1)(a)(iii): https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf |
| Publicly traded company with at least 10% paid-up shares transferred by IPO, direct listing, rights issue or RPO | 22.5%; 20% if all types of transactions in the income year occur through bank transfer | Schedule 2 D(1)(a)(i): https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf |
| Other publicly traded company below that share-transfer threshold | 25%; 22.5% on the same all-transactions banking condition | Schedule 2 D(1)(a)(ii): https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf |
| Publicly traded bank, insurance or finance company, excluding merchant bank | 37.5% | Schedule 2 D(1)(b): https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf |
| Non-publicly traded bank, insurance or finance company | 40% | same |
| Company manufacturing the specified tobacco products | 45%, plus surcharge of 2.5% of the relevant business income | Schedule 2 D(1)(c) and part 2 B: https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf |
| Mobile operator | 45%; qualifying public conversion with 10% share transfer and no more than 5% pre-IPO placement gives 40%; additional qualifying IPO transfer rebate requires separate testing | Schedule 2 D(1)(d): https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf |

1. Establish residence under section 2 and source/exemption scope under section 26. Resident companies generally include worldwide income, non-residents Bangladesh-source income; do not ignore a specific exemption or PE/treaty rule (https://bdlaws.minlaw.gov.bd/act-1429/section-51794.html; https://bdlaws.minlaw.gov.bd/act-1429/section-51818.html). Identify the correct company/sector class before applying a rate.
2. Start with audited accounts, reconcile income and allowable/disallowed expenses and applicable depreciation under the Act. Section 73 governs certified statements and tax computation (https://bdlaws.minlaw.gov.bd/act-1429/section-51903.html). Do not apply a tax rate directly to cash receipts or assume accounting profit equals taxable income.
3. Test the full banking condition against the enacted schedule. Use statutory bank transfer under section 2(72), including qualifying account-to-account MFS and government challan payments, rather than an ordinary-bank-only test (https://bdlaws.minlaw.gov.bd/act-1429/section-51794.html). The old IPO distinction used strictly greater than 10%; the enacted schedule includes exactly 10% and specified non-IPO transfer methods. The old receipt/payment-threshold shorthand does not replace the schedule's all-transactions test.
4. Compare normal liability with applicable minimum/final-tax regimes and add surcharge where required. Loss carry-forward, sector relief, special income and gross-receipt minimum tax are not computed here; obtain the relevant provision before finalizing.

### Withholding and cross-border conditions

| Payment/recipient condition | Current selected rule | Official source |
|---|---|---|
| Resident dividend to an individual | 15%; do not use old TIN-based 10%/15% split | Income Tax Act section 117: https://bdlaws.minlaw.gov.bd/act-1429/act-part-print-542.html |
| Resident dividend to other person | 20%; exception for exempt redistributed taxed dividends under Sixth Schedule paragraph 32 | same |
| Resident deposit interest/profit | 20% to trust/AOP/company, 10% otherwise; exemption/reduced-rate certificate conditions apply | Section 102: https://bdlaws.minlaw.gov.bd/act-1429/act-part-print-542.html |
| Specified payer's loan interest to resident recipient other than bank/finance company | 10%, subject to qualifying reduced/no-deduction certificate | Section 104: https://bdlaws.minlaw.gov.bd/act-1429/act-part-print-542.html |
| Resident royalty/intangible-property payment within section 91 | 10% of the base value | Section 91: https://bdlaws.minlaw.gov.bd/act-1429/act-part-print-542.html |
| Non-resident taxable payment | Apply the prescribed payment-specific rate under section 119, up to 30%; treaty/no-tax reduction needs the statutory certificate, not an assumed uniform 20% | Section 119: https://bdlaws.minlaw.gov.bd/act-1429/act-part-print-542.html |

Check the current withholding rules for each non-resident dividend, interest, royalty or technical-service category before deduction. The section 119 ceiling is not the rate for every payment. Do not promise treaty relief without checking the instrument, beneficial recipient/PE facts and certificate procedure. Income tax deducted from salary is covered in [payroll](bd-payroll.md).

### Filing and payment

Section 170(2) sets the company/other non-individual deadline at the 15th day of the 9th month after income-year end, or the following 15 September where that calculated date would be earlier. The old 7th-month rule is not current. Early filing at least 2 months before that deadline can earn the lower of 5% of section 173(2) payable or BDT 25,000; after the deadline within the remaining assessment year the additional tax is the higher of 2% or BDT 25,000. Apply holiday and current notice rules (https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html).

Advance tax requires the section 154 trigger and exclusions, then the section 155 computation and dates: 15 September, 15 December, 15 March and 15 June. Do not infer that all businesses owe equal instalments without the statutory income base and prior credits (https://bdlaws.minlaw.gov.bd/act-1429/section-51984.html; https://bdlaws.minlaw.gov.bd/act-1429/section-51985.html). Pay return tax/surcharge with the return after supported source/advance tax credits under section 173. Retain certified accounts, computation, challans, return and acknowledgement.

## Worked cases

### Ordinary company: banking-condition decision

Illustrative adjusted taxable income 1,000,000, no minimum tax, sector surcharge or special income. Complete evidence meets the all-transactions bank condition: tax 250,000. If it does not, ordinary rate gives 275,000. Difference 25,000, derived. These are alternative fact cases, not an election to disregard the actual condition.

```oa-check
name: Ordinary company banking condition
inputs:
  taxable_income: 1000000
steps:
  - qualifying_tax: taxable_income * 0.25
  - ordinary_tax: taxable_income * 0.275
  - difference: ordinary_tax - qualifying_tax
expected:
  qualifying_tax: 250000
  ordinary_tax: 275000
  difference: 25000
```

### Tobacco surcharge is on business income

Illustrative qualifying tobacco-manufacturer taxable business income 1,000,000: company tax 450,000 plus income-based surcharge 25,000, total 475,000 before other applicable tax and credits. Do not compute the surcharge as a percentage of the corporate tax.

```oa-check
name: Tobacco manufacturer income based surcharge
inputs:
  business_income: 1000000
steps:
  - company_tax: business_income * 0.45
  - surcharge: business_income * 0.025
  - combined: company_tax + surcharge
expected:
  company_tax: 450000
  surcharge: 25000
  combined: 475000
```

## When to refuse or refer

Refer unconfirmed banking qualification, merchant banks, mobile IPO rebates, losses, special minimum/final tax, sector exemptions, treaty/PE and associated-enterprise pricing. No old approximate rate or deadline is an acceptable fallback.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for enacted company classes, banking conditions, mobile-operator exceptions and tobacco surcharge, Finance Act schedule 2 | https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf | 2026-11-14 |
| Read for residence and company definition | https://bdlaws.minlaw.gov.bd/act-1429/section-51794.html | 2026-11-14 |
| Read for income scope section 26 | https://bdlaws.minlaw.gov.bd/act-1429/section-51818.html | 2026-11-14 |
| Read for certified accounts and computation section 73 | https://bdlaws.minlaw.gov.bd/act-1429/section-51903.html | 2026-11-14 |
| Read for current resident withholding sections 91/102/104/117 and non-resident section 119, including exceptions | https://bdlaws.minlaw.gov.bd/act-1429/act-part-print-542.html | 2026-11-14 |
| Read for company filing and timing adjustments section 170 | https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html | 2026-11-14 |
| Read for advance-tax trigger and exclusions section 154 | https://bdlaws.minlaw.gov.bd/act-1429/section-51984.html | 2026-11-14 |
| Read for advance-tax computation and dates section 155 | https://bdlaws.minlaw.gov.bd/act-1429/section-51985.html | 2026-11-14 |
| Read for return payment and source/advance credits section 173 | https://bdlaws.minlaw.gov.bd/act-1429/section-52003.html | 2026-11-14 |

Not yet confirmed: Payment-specific non-resident withholding rates under current rules, detailed minimum/final-tax computations, loss and sector regimes, treaty eligibility, mobile IPO rebate entitlement and live corporate return fields. Do not retain the old approximate non-resident rates as instructions.
