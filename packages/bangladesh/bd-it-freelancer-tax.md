---
name: bd-it-freelancer-tax
description: "Bangladesh conditional services-income exemption in 2026, including the enacted freelancing/content-creation expansion, banking conditions, return disclosure and separation from export cash incentives."
version: 1.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: income-tax
type: situation-rules
---

# Bangladesh IT and freelance income relief v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Resident individuals and non-resident Bangladeshi individuals carrying on listed services businesses. This is an income-tax relief analysis, not a licence for informal foreign exchange, a VAT exemption decision or an export-incentive calculation.

## Ask the client first

- Residence, citizenship, service description and contracts.
- Earning dates and relevant income/assessment year.
- All business receipts and statutory bank-transfer/remittance evidence, including account-to-account MFS records.
- Domestic/export split, other income, expenses, filing/payment compliance and any claimed incentive.

## The method, step by step

### Quick reference

| Rule and complete condition | Period or amount | Official source |
|---|---|---|
| Listed services business income of resident or non-resident Bangladeshi individual, Sixth Schedule part 1 paragraph 21 | 1 July 2024 to 30 June 2027 | Base paragraph and list in Income Tax Act: https://nbr.gov.bd/uploads/acts/Income_tax_act_2023.pdf |
| Current banking proviso for that business | All income must be transacted 100% through statutory bank transfer; section 2(72) includes account-to-account MFS transfers. The former all-income/expenditure/investment proviso was replaced | Act 89 section 135(a)(4) and definition: https://bdlaws.minlaw.gov.bd/act-1718/section-59129.html ; https://bdlaws.minlaw.gov.bd/act-1429/section-51794.html |
| List item expanded from IT freelancing to freelancing and content creation | Finance Act amendment effective 1 July 2026; apply the correct earning period | Finance Act section 157(b): https://bdlaws.minlaw.gov.bd/act-1725/section-59531.html |
| Entitlement also requires filing compliance; exempt-source disallowed expenses remain taxable | Section 76(5) denies exemption on failure to file in compliance with sections 166 and 171; paragraph 21 is not among its exceptions. Section 76(7) preserves section 56 tax on section 55-disallowed expenses | Current section 76: https://bdlaws.minlaw.gov.bd/act-1429/section-51906.html |

1. Match the work to the actual list: AI solutions, blockchain solutions, robotics process outsourcing, SaaS, cyber security, data analytics/data science, mobile applications, software development/customization, software testing, web development/services, IT support/maintenance, geographic information, digital animation/graphics, data entry/processing, e-learning/e-publication, freelancing/content creation as amended, call centres, document conversion/imaging/digital archiving. Do not confuse blockchain software work with permission to receive crypto.
2. Check the service and amendment dates. The earlier assertion that IT/ITES relief expired without a successor after June 2024 is wrong. The original paragraph's window continues, subject to its scope and banking condition. Do not backdate the later content-creation expansion to earlier receipts without the applicable commencement rule.
3. Reconcile every receipt to bank/MFS account statements and applicable remittance/encashment certificates. Use the statutory bank-transfer definition in section 2(72), including account-to-account MFS; an ordinary-language bank-only rule would be too narrow. The proviso tests all business income, not only foreign receipts. If any receipt/channel is unresolved, withhold the relief conclusion; do not automatically apply either exemption or normal bands to the whole business.
4. Confirm filing and payment compliance under sections 166 and 171 before certifying relief: current section 76(5) denies the exemption on the stated filing failure, and paragraph 21 is not excepted. Disclose qualifying exempt income in the return; a filing duty is a condition of this exemption, not merely an optional reporting step. Section 76(7) still taxes section 55-disallowed expenses under section 56 even for an exempt source. Section 76(6) also prevents a second exemption for the same source through a new period or restructuring, except where the Act extends the existing period. Keep those adjustments separate from exempt-source income; other taxable income goes through [PIT](bangladesh-pit.md). Do not reject a domestic listed service merely because it is domestic (https://bdlaws.minlaw.gov.bd/act-1429/section-51906.html ; https://bdlaws.minlaw.gov.bd/act-1429/section-52001.html ; https://bdlaws.minlaw.gov.bd/act-1429/section-51996.html).
5. Keep the ICT/ITES export cash-incentive question separate. Bring export proceeds through lawful banking channels and keep certificates. No incentive percentage or guaranteed award is given here. Use [VAT](bangladesh-vat.md) separately for export/sector treatment.

## Worked cases

### Qualifying service and bank-reconciliation test

Illustrative listed software business receipts 2,950,000, all matched to statutory bank transfers. Matched amount equals receipts and the unmatched balance is 0, so the channel test is met on these facts. Service, period, citizenship and section 76 filing-compliance conditions must also be met, and section 55/56 adjustments checked; this arithmetic alone does not certify exemption. The amount is an illustrative BDT receipt, not a fixed USD conversion or an incentive award.

```oa-check
name: Listed service bank channel reconciliation
inputs:
  business_receipts: 2950000
  bank_matched: 2950000
steps:
  - unmatched: business_receipts - bank_matched
  - bank_share: bank_matched / business_receipts
expected:
  unmatched: 0
  bank_share: 1
```

### Edge case: an unmatched receipt stops relief sign-off

Same receipts, but only 2,800,000 matched. The unmatched 150,000 prevents certifying the all-income banking condition. Request evidence and refer the relief conclusion; do not label the remainder taxable or grant a partial exemption without legal analysis.

```oa-check
name: Unmatched receipts prevent the all income channel conclusion
inputs:
  business_receipts: 2950000
  bank_matched: 2800000
steps:
  - unmatched: business_receipts - bank_matched
expected:
  unmatched: 150000
```

## When to refuse or refer

Refer an unidentified service, mixed activities, a receipt outside the statutory bank-transfer definition, overseas residence/PE, filing failure, disallowed-expense tax or a period that straddles an amendment. Account-to-account MFS is not excluded merely because it is not an ordinary bank account transfer. Never recommend crypto or informal remittance. Do not state that relief removes filing, promises an export incentive, or makes unrelated business income exempt.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for Sixth Schedule part 1 paragraph 21 service list, 2024-2027 window and adjacent foreign-earned-income paragraph 17 | https://nbr.gov.bd/uploads/acts/Income_tax_act_2023.pdf | 2026-11-14 |
| Read for current all-income banking proviso, Act 89 section 135 | https://bdlaws.minlaw.gov.bd/act-1718/section-59129.html | 2026-11-14 |
| Read for freelancing/content-creation substitution and neighboring relief changes, Finance Act section 157 | https://bdlaws.minlaw.gov.bd/act-1725/section-59531.html | 2026-11-14 |
| Read for exempt-income return duty and exceptions, section 166 | https://bdlaws.minlaw.gov.bd/act-1429/section-51996.html | 2026-11-14 |
| Read for complete section 76 filing-entitlement, repeated-source-exemption and disallowed-expense conditions | https://bdlaws.minlaw.gov.bd/act-1429/section-51906.html | 2026-11-14 |
| Read for current section 171 filing and payment requirements | https://bdlaws.minlaw.gov.bd/act-1429/section-52001.html | 2026-11-14 |
| Read for section 2(72) statutory bank transfer including account-to-account MFS | https://bdlaws.minlaw.gov.bd/act-1429/section-51794.html | 2026-11-14 |

Not yet confirmed: Current export cash-incentive percentage, eligible provider/certification requirements and claim deadline; cross-period application of the expanded non-IT list to earlier income; taxpayer-specific treatment where the all-income banking condition fails. No relief is certified for those unresolved facts.
