---
name: ua-freelance-intake
description: "ALWAYS USE THIS SKILL when a user asks for help preparing their Ukrainian taxes AND mentions freelancing, self-employment, sole proprietorship, ФОП, FOP, or being an individual entrepreneur in Ukraine. Trigger on phrases like \"help me do my Ukrainian taxes\", \"I'm a ФОП\", \"I'm a freelancer in Ukraine\", \"prepare my single-tax return\", \"I'm self-employed in Ukraine\", or any similar phrasing where the user is a Ukraine-resident self-employed individual needing tax help. This is the REQUIRED entry point for the Ukraine self-employed workflow; downstream skills (ua-single-tax, ua-income-tax, ua-social-contributions, ukraine-vat, ua-return-assembly) depend on this skill running first to produce a structured intake package. Upload-first workflow. Ukraine-resident sole proprietors only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ua-freelance-intake"
  jurisdiction: "UA"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# UA Freelance Intake

## Scope

This is the required intake entry point for Ukraine-resident self-employed individuals registered as ФОП / FOP. It produces a structured package for ua-single-tax, ua-income-tax, ua-social-contributions, ukraine-vat and ua-return-assembly. It computes no tax and does not prepare a company return.

Upload first, infer from documents, fill only gaps, then obtain one confirmation. Aim for 3-5 brief routing questions and about 30 seconds for the initial screen; these are workflow targets, not legal deadlines. Do not narrate phases or re-ask facts visible in documents. A target never justifies skipping an unresolved eligibility fact.

**Not yet confirmed:** the client's registration, system, group, VAT status, residence, permitted activities, receipt classification and any change dates until supported by documents. The former unanswered-facts fallback (FOP, simplified, Group 3, non-VAT, resident) is withdrawn: none of those statuses can be established by silence. Residence and treaty disputes, Group 4 farming, electronic residency and company taxation require a separate review. This intake supplies no filing dates, forms or final tax calculation.

## Ask the client first

Read all uploaded records before asking. Confirm only missing or conflicting facts:

- Individual entrepreneur (ФОП) or company (ТОВ)? Refer a company; do not infer FOP from the word freelancer.
- Simplified/single tax or general system, with the effective dates of any changes during the year?
- If single tax, registered Group 1, 2 or 3, registered activities and rate? Group 3 is a common route for eligible freelancers, not an automatic classification.
- For Group 3, VAT registration and effective dates? Obtain the single-tax register extract and VAT evidence separately. An EDR business-registration extract supplies identity and activity information; it does not by itself establish the tax group's current registration.
- Ukrainian tax resident for the period? Record the basis and any competing residence claim; refer nonresidents or unresolved residence instead of assuming resident status.

Request bank statements for **all accounts**, UAH and FX, for the **full year**, the EDR registration extract (виписка з ЄДР) with КВЕД codes, the single-tax register extract/current registration evidence, prior-year single-tax declaration and ЄСВ payment history if available. For general-system periods, request the prior property/income declaration and income/expense records. Obtain contracts, invoices, transfer links and loan documents where needed to explain statement entries. Record missing periods and accounts explicitly.

## The method, step by step

1. **Fix identity and periods.** Build a year timeline of FOP registration, system, group, VAT and activity changes from evidence. Do not force a mixed year into a single regime. Obtain confirmation of unresolved facts before computation.
2. **Verify the tax registration.** Use the single-tax register extract for group, rate, registered activities and effective dates. Tax Code 299.7 lists these particulars and 299.9 provides an extract. A prior return is useful evidence of history, not proof that no later change occurred. Preserve the source document and date for each inferred fact.
3. **Reconcile receipts.** Identify client revenue separately from linked own-account transfers, borrowing, repayments and other receipts. Do not exclude an unexplained deposit merely because its description says transfer or loan. Under 292.11(3), returnable financial assistance is excluded only when received and returned within 12 calendar months; credits are separately excluded. Record terms, receipt/repayment dates and evidence. Refer uncertain contributions or other receipt types for classification under the appropriate regime.
4. **Translate simplified-system FX receipts.** Under 292.5, use the official NBU rate on the income-receipt date, not the later bank sale rate. Keep original currency, amount, date, rate evidence and UAH equivalent, and avoid counting the same receipt again when transferred or sold. The example below uses a hypothetical rate; retrieve the actual official daily rate for a real receipt. For general-system FX treatment, pass all dates and amounts to ua-income-tax rather than applying this single-tax rule automatically.
5. **Screen eligibility before handoff.** Check actual activity and customers against 291.4, 291.5-291.7 and 293.3; a KVED label alone is insufficient. Group 1 is restricted to market retail and/or listed household services to the public with no employees. Group 2 covers qualifying services to single-tax payers/the public, goods production/sale and restaurant activity, with no more than 10 counted employees simultaneously. The service-customer condition does not create a blanket ban on all Group 2 goods sales to legal entities. Employee counting has maternity/childcare and mobilization exceptions under 291.4.1. Group 3 has no employee-number cap under 291.4, but still requires eligibility and registration.
6. **Flag caps and barred activities.** Pass cumulative income and suspected cap approaches to ua-single-tax; do not use a rounded cap or decide an excess consequence here. Preserve the original flags for gambling, FX exchange, excisable goods, financial services and mineral extraction, but test statutory exceptions rather than treating each label as an absolute ban. Article 291.5 also covers the other barred activities/persons, including nonresidents and tax-debt conditions. Production, supply or sale of the jewellery/household precious-metal or stone articles specified in 291.4(2) is not categorically barred: eligible FOPs use Group 3 at 5% under 293.3. Distinguish household services: 291.7(28)-(29) lists custom jewellery-making and repair, and the [official 2026 household-services explanation](https://if.tax.gov.ua/media-ark/news-ark/print-967828.html) includes these in the Group 1 list. Review the actual activity; do not classify every jewellery repair as Group 3. Refer any prohibited, unregistered, nonmonetary or mismatched activity; do not silently repair its history by choosing another group.
7. **Confirm once.** Show identity, tax year, evidence, period-by-period registration, activity/customer screen, receipts and FX reconciliation, missing documents and unresolved flags. Ask for corrections once. An unconfirmed fact remains open; no default fills it.
8. **Hand off by the verified period.** Simplified: ua-single-tax for single tax and military levy, ua-social-contributions for ЄСВ, and ukraine-vat if VAT-registered or another VAT issue is identified, then ua-return-assembly. General: ua-income-tax for business PIT and military levy, plus ua-social-contributions and VAT review where needed, then ua-return-assembly. Send all supporting records and unresolved items. Preserve the original duplicate single-tax routing instruction through this consolidated step.

### Rates used only to identify the destination

| Registration/route | Value and condition | Official source |
|---|---|---|
| Ordinary eligible Group 3 FOP | 3% of statutory income when paying VAT, or 5% when VAT is included in single tax; FOPs carrying on the specified jewellery production/supply/sale use 5%, with the household-service distinction in method6. Actual registration, activity and dates must agree. This is not a tax computation | [Tax Code 291.4,293.3](https://tax.gov.ua/nk/) |
| General-system FOP | 18% PIT on the statutory net taxable business base under 177.1-177.4, plus ordinarily 5% military levy under section XX, subsection 10,16-1. Separate exemptions and nonbusiness income are reviewed downstream | [Tax Code 167.1,177;16-1(1.2-1.4,1.7)](https://tax.gov.ua/nk/) |

A non-VAT registration does not settle every VAT obligation. Article 181.1's mandatory turnover test excludes single-tax Groups 1-3, while imports and other special obligations need separate VAT review. Do not add VAT solely because a single-tax payer's receipts exceed a general-system threshold, or assume no obligation solely because there is no VAT registration. [Tax Code 181.1-181.2](https://tax.gov.ua/nk/).

## Worked cases

These are hypothetical intake checks, not tax due.

### Case 1: reconcile FX, a linked transfer and documented borrowing

A verified eligible Group 3 FOP's statements show UAH 100,000 customer receipts, USD 3,000 customer receipts at a hypothetical NBU receipt-date rate of UAH 41.50/USD, an identified UAH 50,000 transfer between the same owner's accounts and UAH 20,000 bank credit. Assume both exclusions are documented and no other income adjustment applies. Total bank credits translated for this check are UAH 294,500; candidate single-tax receipts are **UAH 224,500**, derived. Pass the latter with the exclusions and evidence, not an unexplained net deposit total. The borrowing input is a bank credit, not a returnable-assistance claim with an unchecked 12-month condition. [Tax Code 292.1,292.5-292.6,292.11(3)](https://tax.gov.ua/nk/).

```oa-check
name: Intake receipt reconciliation, not tax due
inputs:
  customer_uah: 100000
  customer_usd: 3000
  nbu_rate: 41.50
  linked_transfer: 50000
  bank_credit: 20000
steps:
  - fx_receipts: customer_usd * nbu_rate
  - bank_credits_uah: customer_uah + fx_receipts + linked_transfer + bank_credit
  - candidate_receipts: bank_credits_uah - linked_transfer - bank_credit
expected:
  fx_receipts: 124500
  bank_credits_uah: 294500
  candidate_receipts: 224500
```

### Case 2: a Group 2 employee conflict blocks routine routing

The extract says Group 2, but the simultaneous roster shows 9 ordinary counted employees plus 2 additional ordinary counted employees, with no 291.4.1 counting exception. The total is **11**, exceeding the **10** limit by **1**, derived. Refer the mismatch to ua-single-tax/the reviewer to establish its timing and consequences; do not claim that the person automatically became Group 3, or compute a Group 2 return using the extract alone. [Tax Code 291.4(2),291.4.1](https://tax.gov.ua/nk/).

```oa-check
name: Group 2 counted-employee eligibility conflict
inputs:
  existing_counted: 9
  additional_counted: 2
  group2_limit: 10
steps:
  - counted_total: existing_counted + additional_counted
  - over_limit: max(0, counted_total - group2_limit)
expected:
  counted_total: 11
  over_limit: 1
```

## When to refuse or refer

Refer companies, nonresidents, unresolved residence, Group 4 farming, electronic residency, unexplained or barred activity, unverified registration, conflicting dates/group/VAT evidence, cap breaches and unresolved receipt exclusions. Keep collecting safe documentary facts, but stop the affected computation until the issue is resolved. General-system use is within this workflow when identity and residence are established; it is not a refusal merely because simplified eligibility fails.

## Sources

| Official source | Read for | Read date |
|---|---|---|
| [State Tax Service consolidated Tax Code](https://tax.gov.ua/nk/) | Read for full 291.1-291.8 and 292.1-292.16;293.3 and 293.4 and293.8(1)-(3) transition context;299.7-299.9 registration particulars/extract and299.10(1)-(2) cancellation context;167.1 and177.1-177.4.3 general-system base;181.1-183.4 VAT context;section XX,subsection10,16-1(1.1-1.7-1) levy rates, timing and exemptions. Header includes October2026 amendments. Operative scope was opened, not the entire 26,507-line code | 2026-11-15 |
| [State Tax Service 2026 household-services explanation](https://if.tax.gov.ua/media-ark/news-ark/print-967828.html) | Read for Group 1 eligibility and full 40-item household-service list, especially 291.7(28)-(29) custom jewellery-making/repair; actual activity must be distinguished from specified commercial jewellery production/supply/sale | 2026-11-15 |

Not yet confirmed: client-specific registration and residence, receipt exclusions, actual daily NBU rates and any period with unresolved activity or status changes. No tax calculation or filing calendar is approved by this intake.

The Parliamentary code endpoint and its older cited archive were unavailable in this session. The operative source above is the tax authority's accessible consolidated text; unavailable endpoints are not presented as read. Actual daily NBU rates and client-specific registrations remain evidence to obtain for the individual case.

## Disclaimer

This skill orchestrates intake only and computes no tax. All downstream outputs must be reviewed and signed off by a qualified Ukrainian accountant or auditor before filing. The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ua-freelance-intake` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ua-freelance-intake. If neither is available, confirm every figure against the official source pages cited above before relying on it.
