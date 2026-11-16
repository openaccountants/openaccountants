---
name: bd-freelance-intake
description: "Bangladesh resident freelancer and sole-proprietor intake for 2026: collect documents, establish residence and activity, and route to the current tax computations without guessing relief or filing dates."
version: 0.2
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
tier: 2
domain: income-tax
type: router
---

# Bangladesh self-employed intake v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Entry point for resident individual freelancers, IT/ITES exporters and sole proprietors. Produces a confirmed fact package, not tax or a filed return. The income year and assessment year must both be recorded; downstream rules depend on the period.

## Ask the client first

- Residence and presence history, citizenship and the income/assessment periods.
- Exact services, domestic/export customers, employment versus independent business, and entity form.
- TIN, prior returns, BIN/enlistment status and turnover evidence.
- Bank/platform statements, invoices, remittance and encashment certificates, expenses, investments and withholding certificates.

## The method, step by step

1. Complete the residence and entity sweep before applying individual rules. Route non-residents, companies and permanent establishments for separate analysis using [tax overview](bd-tax-overview.md). Do not assume residence or a sole proprietorship when facts are missing.
2. Request the full-period bank and platform records first, including Upwork/Fiverr statements, direct invoices, prior return, TIN and trade licence. Separate export proceeds, domestic receipts, owner transfers and any export incentive. Confirm the resulting reconciliation with the taxpayer.
3. Route eligible services to [IT/freelancer relief](bd-it-freelancer-tax.md), other individual income and all bands/filing windows to [PIT](bangladesh-pit.md). Do not default IT/ITES income to taxable merely because the old relief period ended. The successor list and its conditions must be applied; Finance Act section 157 changes the list (https://bdlaws.minlaw.gov.bd/act-1725/section-59531.html).
4. Route registration, turnover tax and VAT to [VAT](bangladesh-vat.md); use [social contributions](bd-social-contributions.md) for pension choice and [payroll](bd-payroll.md) if there are staff.
5. Hand off the confirmed facts and unresolved documents to [return assembly](bd-return-assembly.md). Relief does not itself remove filing: check section 166's exempt-income and other filing triggers (https://bdlaws.minlaw.gov.bd/act-1429/section-51996.html).

## When to refuse or refer

Stop computation where residence, legal entity, relevant period or the nature of services is unknown. Refer non-resident and company matters. Do not invent missing amounts or recommend informal remittance channels.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for filing triggers and exceptions, Income Tax Act section 166 | https://bdlaws.minlaw.gov.bd/act-1429/section-51996.html | 2026-11-14 |
| Read for successor freelancing list, Finance Act section 157 | https://bdlaws.minlaw.gov.bd/act-1725/section-59531.html | 2026-11-14 |

Not yet confirmed: Client-specific residence, relief qualification, bank reconciliation and registration facts until documents establish them; current cash-incentive eligibility/rate is not established here and must not be promised.
