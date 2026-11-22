---
name: ca-corporation-franchise-tax
description: >
  Compute and prepare the California C corporation franchise or income tax
  return for tax year 2026. Covers Form 100, corporation and LLC nexus, the
  8.84% general rate, the 10.84% bank and financial corporation rate, the
  $800 minimum franchise tax and first-year exceptions, California income
  adjustments, NOL and credit limits, multistate apportionment, combined
  reporting, deadlines, estimates, penalties, and records. Trigger on
  "California C corporation tax", "California Form 100", "California
  corporation franchise tax", "California corporate income tax", or "Form
  100 estimated tax". Use ca-smllc-form-568 for a disregarded SMLLC,
  ca-llc-fee-and-tax for an LLC taxed as a partnership or disregarded entity,
  ca-pte-elective-tax for the elective pass-through entity tax, and
  ca-payroll for payroll. Form 100S, Form 100W and transfer pricing are out
  of scope.
jurisdiction: US-CA
category: state-tax
tax_year: 2026
last_updated: 2026-11-21
version: 0.1
tier: 2
domain: corporate-tax
type: computation
---

# California C corporation franchise and income tax: Form 100 (tax year 2026) v0.1

> **General reference only.** This skill is a source-cited draft for AI-assisted tax work. It has not been reviewed for any specific corporation, election, accounting period, unitary group, or filing position. Do not file, pay, amend, or take a tax position from it without review by a qualified California tax professional.

For written federal tax advice based on this material, a practitioner must follow applicable Treasury Department Circular 230 requirements, including 31 C.F.R. §10.37.

**Answer first.** For 2026, a general corporation subject to California franchise tax computes tax at 8.84% of California net income, but usually owes at least the $800 minimum franchise tax. Banks and financial corporations use 10.84%. The first taxable year of a corporation newly incorporated or qualified with the California Secretary of State is not subject to the $800 minimum, but measured tax on net income still applies. The FTB has published 2026 corporation estimated-tax instructions, but as of 21 November 2026 its latest Form 100 return booklet is for 2025. This guide labels those form-line instructions as 2025 and requires a refresh against the 2026 Form 100 booklet before a 2026 return is filed in 2027.

## Scope

This guide covers a C corporation's 2026 California corporation franchise or income tax computation and Form 100 workflow. It includes ordinary state net income, nexus, the minimum tax, basic California adjustments, NOL and credit limits, multistate apportionment, combined reporting, estimates, deadlines and penalties.

Out of scope:

- S corporation tax and Form 100S. See the FTB's 2025 S Corporation Tax Booklet.
- Water's-edge returns and Form 100W. Water's-edge elections are complex and require a separate review.
- LLC annual tax, LLC fee and Form 568 when an LLC is taxed as a partnership or disregarded. See ca-llc-fee-and-tax and ca-smllc-form-568.
- PTE elective tax, individual owner tax, payroll, sales and use tax, local business tax, tax credits requiring a separate computation, and transfer pricing.
- Advice on Public Law 86-272, unitary status, California sourcing, or whether an entity is a corporation for federal purposes where those facts are disputed.

## Rates, bands and thresholds

Use 2026 figures where the FTB has published them. The listed nexus thresholds are specifically the FTB's 2025 values; the FTB had not published 2026 values as of 21 November 2026, so do not apply them to a 2026 nexus test.

| Rate or threshold | Figure | Applies when | Official source |
|---|---:|---|---|
| General corporation tax rate | 8.84% | C corporation measured tax on California net income | [2026 Form 100-ES, C](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| Bank and financial corporation tax rate | 10.84% | Corporation is classified as a bank or financial corporation | [2026 Form 100-ES, C](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| Minimum franchise tax | $800 | Corporation is subject to franchise tax, unless a statutory exception applies | [2026 Form 100-ES, E](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| Special minimum franchise tax | $25 | Qualified inactive gold or quicksilver mining corporation | [2025 Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| Doing-business sales threshold (2025 only) | $757,070 | 2025 California sales test; also compare with 25% of everywhere sales | [FTB: Doing business in California](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) |
| Doing-business property and payroll threshold (2025 only) | $75,707 | 2025 California property or payroll test; also compare with 25% of everywhere amount | [FTB: Doing business in California](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) |
| NOL suspension threshold | $1,000,000 | California taxable income at or above this amount, tax years beginning 2024 through 2026 | [2025 Form 100 instructions, W](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| General credit limitation | $5,000,000 | Tax years beginning 2024 through 2026, subject to stated exceptions | [2025 Form 100 instructions, line 23](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| Regular estimated-tax installments | 30%, 40%, 0%, 30% | Installments 1 through 4 for a regular corporation | [2026 Form 100-ES, D](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| Estimated-tax installment months | 4th, 6th, 9th, 12th | Due on the 15th day of each month, shifted for weekends and holidays | [2026 Form 100-ES, D](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| Mandatory electronic-payment threshold | Payment over $20,000 or total tax liability over $80,000 | Once met, later payments generally must be electronic | [2025 Form 100 instructions, G](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| Late-filing penalty | 5% per month; 25% maximum | Tax due after timely payments; Form 100 filed late | [2025 Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| Late-payment penalty | 5% plus 0.5% per month; 25% maximum | Unpaid tax remains unpaid after the original due date | [2025 Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| EFT noncompliance penalty | 10% | Required electronic payment not made electronically | [2025 Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| Large-corporation estimate test | $1,000,000 | California net income, without NOL, in any of the three preceding years | [2026 Form 100-ES, I](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |

## Ask the client first

- What is the entity's legal type and federal tax classification, California SOS status, and taxable year; is it in its first year or a reorganization?
- What California activity, California-source income, sales, property and payroll does it have, including pass-through shares; could Public Law 86-272 apply?
- Is it part of a unitary group, does it operate in other states, and is a water's-edge election in effect?
- What are federal taxable income, California adjustments, depreciation differences, NOLs, disaster losses, credits and estimated payments?
- Did it have at least $1 million of California net income (without NOL) in a prior year, foreign information returns, reportable transactions or an uncertain tax position statement?
- Has the corporation received an FTB or IRS notice or determination, or been suspended, forfeited, dissolved or merged?

## The method, step by step

1. **Classify and route.** Confirm C corporation treatment. Use Form 100 for the corporation franchise or income tax. If the entity is an S corporation, use Form 100S. If it has elected water's-edge treatment, use Form 100W. An LLC classified as a partnership or disregarded entity is outside this skill.
2. **Determine the tax.** Decide whether the corporation is subject to franchise tax because it is incorporated, qualified or doing business in California. If it is not doing business but has California-source income, test for corporation income tax instead.
3. **Test the minimum.** Apply the $800 minimum franchise tax, first-year relief, the 15-day short-year rule, and any narrow exception. Do not assume that inactivity, a loss, a short period or a lack of registration removes the obligation.
4. **Compute state net income.** Use the federal reconciliation method or the California computation method. Reconcile federal taxable income to California law and attach the forms and schedules the return requests.
5. **Apply California limits.** Recompute depreciation, NOLs, disaster losses, charitable contributions, credits and other California-specific items. Keep the 2026 NOL and credit limitations separate from federal rules.
6. **Source and apportion.** Separate business from nonbusiness income. Allocate nonbusiness income and apportion multistate business income using Schedule R. Determine whether the unitary group must file a combined report.
7. **Calculate tax.** Apply 8.84%, or 10.84% for banks and financial corporations, and compare the measured tax with the applicable minimum. Credits, AMT and special taxes require their own rules and schedules.
8. **File and pay.** File Form 100 by its original due date, make any estimated payments on Form 100-ES, and pay the full balance by the original return due date. An extension extends filing time only.
9. **Reconcile and retain.** Tie every return line to workpapers, federal returns, apportionment records, payments, elections and disclosures. Confirm whether any recordkeeping, foreign reporting, underpayment or large-corporate penalty rule applies.

### The 150 California rules

The numbered items below are 150 distinct operational rules and exceptions for the Form 100 workflow. The numbering makes the requested count reviewable; it does not replace the statute, regulations, current-year forms, or the facts.

| No. | Rule | Authority |
|---:|---|---|
| 001 | A corporation incorporated or organized under California law is subject to the corporation franchise tax. | [R&TC §23151](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 002 | A corporation qualified or registered with the California Secretary of State to do business is subject to the corporation franchise tax. | [R&TC §23151](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 003 | A corporation doing business in California may owe franchise tax whether or not it is incorporated, organized, qualified or registered here. | [R&TC §23151](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 004 | The measured franchise tax is based on the corporation's income for the current taxable year in which it enjoys the privilege of doing business. | [R&TC §23151](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 005 | A corporation that is inactive but remains within the franchise-tax jurisdiction is still subject to the minimum franchise tax. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 006 | A franchise-tax corporation cannot substitute a business loss for the minimum franchise tax. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 007 | A corporation deriving income from California sources but not doing business here is subject to corporation income tax rather than franchise tax, subject to the law's exceptions. | [R&TC §23501](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23501.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 008 | Use Form 100 for a C corporation subject to California corporation franchise or income tax. | [FTB Form 100 instructions](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 009 | An LLC that elects federal corporate tax treatment files the applicable California corporate forms and is treated as a corporation under the Corporation Tax Law. | [R&TC §23038](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23038.); [FTB Form 100 instructions, X](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 010 | A corporation includes certain associations and other entities treated as corporations for California tax purposes. | [R&TC §23038](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23038.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 011 | Certain business or Massachusetts trusts, REITs and other listed entities can be within Form 100's corporation filing rules. | [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 012 | An S corporation files Form 100S and uses its separate rules; do not apply this Form 100 computation to it. | [FTB 2025 Form 100S Booklet](https://www.ftb.ca.gov/forms/2025/2025-100s-booklet.html) |
| 013 | A C corporation that elects water's-edge reporting uses Form 100W rather than Form 100. | [R&TC §§25110, 25113](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25110.); [FTB Form 100 instructions](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 014 | An LLC classified as a partnership generally files Form 568, not Form 100; an LLC classified as disregarded has separate Form 568 obligations. | [FTB Form 100 instructions, X](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html); [ca-smllc-form-568](https://www.openaccountants.com/skills/ca-smllc-form-568) |
| 015 | A taxpayer is doing business if it actively engages in a California transaction for financial or pecuniary gain or profit. | [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [FTB doing-business guide](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) |
| 016 | Being organized or commercially domiciled in California is a separate doing-business test. | [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [FTB doing-business guide](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) |
| 017 | The California sales doing-business test includes sales by agents and independent contractors. | [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 018 | The property doing-business test includes California real property and tangible personal property. | [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 019 | The payroll doing-business test measures compensation paid in California. | [R&TC §§23101, 25120](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 020 | Each sales, property or payroll threshold is exceeded when the California amount is more than the lesser of the indexed amount or 25% of the everywhere amount. | [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [FTB doing-business guide](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) |
| 021 | Include the corporation's pro rata or distributive share of pass-through entity sales, property and payroll when applying the doing-business tests. | [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 022 | A corporation that is a general partner of a partnership or a member of an LLC doing business in California is treated as doing business in California under FTB instructions. | [FTB Form 100 instructions, A](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 023 | As of 21 November 2026, the FTB's doing-business table shows 2025 thresholds of $757,070 for sales and $75,707 for property and payroll; it does not yet show 2026 indexed amounts. Label these as 2025 values and refresh before applying them to 2026. | [FTB doing-business guide](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) |
| 024 | The general California corporation tax rate is 8.84% of the applicable California net income. | [R&TC §23151](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [2026 Form 100-ES instructions, C](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 025 | Banks and financial corporations use a 10.84% rate under the current FTB corporate estimated-tax instructions. | [R&TC §23186](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23186.); [2026 Form 100-ES instructions, C](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 026 | The ordinary minimum franchise tax is $800 for a corporation subject to franchise tax. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [2026 Form 100-ES instructions, E](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 027 | A combined return must include a minimum franchise tax for each group corporation that is subject to franchise tax. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C and S](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 028 | The $800 minimum generally applies even if the corporation is inactive, has a loss, or files a short-period return. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 029 | A corporation newly incorporated or qualified through the California SOS is not subject to the minimum franchise tax in its first taxable year. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 030 | First-year minimum-tax relief does not exempt a new corporation from measured tax on its California net income. | [R&TC §23151](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [FTB Form 100 instructions, C and L](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 031 | First-year minimum-tax relief applies only when the corporation is incorporated or qualified through the California SOS; an unregistered foreign corporation doing business here does not qualify for that first-year exception. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 032 | A corporation doing no business in California during a taxable year of 15 days or less is not subject to the $800 minimum franchise tax. | [R&TC §23114](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23114.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 033 | A foreign corporation's sole California activity of convention or trade-show participation for seven days or fewer is not doing business if California-reportable gross income does not exceed $10,000. | [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [2026 Form 100-ES instructions, E](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 034 | A qualified inactive gold or quicksilver mining corporation may have a $25 minimum instead of $800; confirm qualification before using the special amount. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 035 | A corporation subject only to income tax, not incorporated or qualified in California and not doing business here, has no minimum franchise tax. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [2026 Form 100-ES instructions, E](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 036 | The deployed-military minimum-tax exemption applies only to taxable years beginning on or after 1 January 2020 and before 1 January 2030. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 037 | For that exemption, the corporation must be a small business solely owned by a deployed U.S. Armed Forces member, and the owner must be deployed during the year. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 038 | The deployed-owner corporation must operate at a loss or cease operation to use the exemption. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 039 | The FTB defines a deployed small business for this exemption using California total income of $250,000 or less. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 040 | For the deployed-military minimum-tax exemption, “deployed” means called to active duty or active service while the United States is engaged in combat or homeland defense; temporary duty solely for training or processing and a permanent change of station do not qualify. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 041 | California's 2026 corporation estimated-tax instructions use the IRC as of 1 January 2025 unless a California modification applies. | [2026 Form 100-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-10…7402 tokens truncated…ges are 30% for installment one, 40% for installment two, no required installment three, and 30% for installment four. | [R&TC §§19021, 19023](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19021.); [2026 Form 100-ES instructions, D](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 125 | When the minimum franchise tax applies, pay at least the minimum by the first estimated-tax due date; a newly formed or qualified corporation is exempt from the minimum in its first year and, if required to make estimates, should compute installments from annualized current-year income under the FTB instructions. | [R&TC §19021](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19021.); [2026 Form 100-ES instructions, D and E](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 126 | When the minimum franchise tax applies and total estimated tax does not exceed that minimum, pay the full minimum by the first estimated-tax installment date; do not apply this minimum-payment rule to a first-year corporation exempt from the minimum. | [R&TC §19021](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19021.); [2026 Form 100-ES instructions, D and E](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 127 | California estimated-tax penalty exceptions use California's current-year rules; do not import the federal lesser-of-current-or-prior-year safe harbor. | [R&TC §§19142-19161](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19142.); [2026 Form 100-ES instructions, H and I](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 128 | The prior-year-tax exception generally uses the preceding year's tax for a 12-month period, prorated to installments, but has special limitations for large and newly formed corporations. | [R&TC §§19142-19161](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19142.); [2026 Form 100-ES instructions, I](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 129 | A corporation is large for this estimated-tax exception if it or a predecessor had California net income of at least $1,000,000 in any of the three preceding taxable years, computed without the NOL deduction. | [R&TC §§19142-19161](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19142.); [2026 Form 100-ES instructions, I](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 130 | A large corporation may use the prior-year-tax exception only for the first installment and must add the first-installment reduction to the second installment. | [R&TC §§19142-19161](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19142.); [2026 Form 100-ES instructions, I](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| 131 | A late Form 100 filing penalty is generally 5% of tax due after timely payments for each month late, up to 25%. | [R&TC §19131](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19131.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 132 | If Form 100 is not filed by the extended due date, the automatic extension does not apply and the late-filing penalty is computed from the original due date. | [R&TC §18604](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18604.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 133 | A late-payment penalty is generally 5% of unpaid tax plus 0.5% for each month or part of a month unpaid, capped at 25%. | [R&TC §19132](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19132.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 134 | If both late-filing and late-payment penalties apply, their combined amount may not exceed 25% of the unpaid tax. | [R&TC §§19131-19132](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19131.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 135 | A corporation must pay electronically after an estimated-tax or extension payment exceeds $20,000, or its total tax liability exceeds $80,000, subject to the first-trigger payment exception. | [R&TC §19011](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19011.); [FTB Form 100 instructions, G](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 136 | Once mandatory electronic payment applies, subsequent payments must be electronic regardless of amount, tax type or taxable year; the first payment that crosses the threshold need not be electronic. | [R&TC §19011](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19011.); [FTB Form 100 instructions, G](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 137 | Failure to make a required electronic payment may result in a penalty of 10% of the amount not paid electronically. | [R&TC §19011](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19011.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 138 | Failure to attach a required federal Form 5471 or 8975 may result in a $1,000 penalty per form per year; the 2025 Form 100 booklet describes a 90-day cure, while FTB Pub. 1024 revised 1/2026 also lists a $1,000 continuation penalty per 30 days after 90-day notice, up to $24,000. Confirm current-year treatment before calculating it. | [R&TC §19141.2](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19141.2.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html); [FTB Pub. 1024](https://www.ftb.ca.gov/forms/misc/1024.html) |
| 139 | A corporation required to attach federal Form 5472 must include it with Form 100, and may have to file it on time even when Form 100 is late. The 2025 Form 100 booklet states $10,000 per required form per year; FTB Pub. 1024 revised 1/2026 lists $25,000 and a $25,000 continuation amount per 30 days after 90-day notice. The 2026 amount is unresolved between current FTB sources; verify before calculating. | [R&TC §19141.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19141.5.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html); [FTB Pub. 1024](https://www.ftb.ca.gov/forms/misc/1024.html) |
| 140 | Failure to maintain required apportionment and combined-report records may result in a $10,000 penalty per taxable year. The 2025 Form 100 booklet describes a further $10,000 per 30 days after 90-day notice with no maximum; FTB Pub. 1024 revised 1/2026 lists the same continuation amount, capped at $50,000 for non-willful conduct. Verify the applicable cap before calculating. | [R&TC §19141.6](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19141.6.); [FTB Form 100 instructions, Records Maintenance Requirements](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html); [FTB Pub. 1024](https://www.ftb.ca.gov/forms/misc/1024.html) |
| 141 | A foreign corporation that fails to qualify or whose powers are forfeited, or a suspended domestic corporation, that is doing business in California and fails to file a return within 60 days after FTB notice and demand may incur a $2,000 penalty per taxable year under R&TC §19135. | [FTB Pub. 1024, Penalty reference chart](https://www.ftb.ca.gov/forms/misc/1024.html); [FTB Form 100 instructions, Q](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 142 | The automatic filing extension is unavailable to a business entity that is suspended on or after the original return due date. | [R&TC §18604](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18604.); [FTB Form 100 instructions, E](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 143 | A corporation protected by Public Law 86-272 and not filing a combined report may be exempt from California tax measured by net income, but remains subject to minimum franchise tax if otherwise subject to it. | [R&TC §23151](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [FTB Form 100 instructions, line 18](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 144 | A corporation claiming Public Law 86-272 protection must follow the Form 100 instructions for excluding net income from the California tax measure and identifying the claim on the return; refer disputed protection questions. | [FTB Form 100 instructions, line 18](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 145 | Reorganization solely to avoid the minimum franchise tax does not qualify a corporation for a new first-year minimum-tax exception. | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100 instructions, C](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 146 | The FTB may waive a late-payment penalty for reasonable cause; reasonable cause is presumed when 90% of the tax shown, but at least the minimum franchise tax if applicable, is paid by the original due date. | [R&TC §19132](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19132.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 147 | The large corporate understatement penalty applies when an understatement exceeds the greater of $1,000,000 or 20% of tax shown on a timely original or amended return; for a taxpayer required or authorized to file as part of a combined report, apply the threshold to the group's aggregate tax liability. | [R&TC §19138](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19138.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html); [FTB Manual of Audit Procedures, §11.12](https://www.ftb.ca.gov/tax-pros/procedures/manual-of-audit-procedures/chapter-11.pdf) |
| 148 | When it applies, the large corporate understatement penalty is 20% of the understatement; check the statutory exceptions before applying it. | [R&TC §19138](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19138.); [FTB Form 100 instructions, M](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| 149 | R&TC §19719 separately imposes a $250 to $1,000 fine on anyone who exercises the rights of a suspended or forfeited corporation, or transacts intrastate business for a foreign corporation whose rights were forfeited. | [FTB Pub. 1024, Penalty reference chart](https://www.ftb.ca.gov/forms/misc/1024.html) |
| 150 | For taxable years beginning on or after 1 January 2025, a corporation required under IRC §6011(e) or its regulations to file at least 10 returns during the calendar year ending with or within its taxable year must electronically file its California corporate return. | [FTB December 2025 Tax News, Business Electronic Filing Mandate](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/12.html) |

## Boundary and exception table

| Situation | Treatment | Authority |
|---|---|---|
| C corporation incorporated, qualified or doing business in California | Form 100 and franchise tax; apply the minimum unless an exception applies | [R&TC §§23151, 23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151.); [FTB Form 100](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| Foreign corporation with California-source income but not doing business here | Test corporation income tax; generally no minimum franchise tax | [R&TC §§23501, 23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23501.); [FTB Form 100-ES](https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html) |
| Newly incorporated or qualified corporation | First taxable year measured tax still applies; $800 minimum does not | [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.); [FTB Form 100](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |
| California activity lasts 15 days or less and corporation does no California business | No $800 minimum under the narrow short-year rule | [R&TC §23114](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23114.) |
| Multistate C corporation with business income | Schedule R generally required; classify and allocate nonbusiness income separately | [R&TC §§25120-25141](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25120.); [FTB Schedule R](https://www.ftb.ca.gov/forms/2025/2025-100r-instructions.html) |
| S corporation, water's-edge corporation, or partnership LLC | Stop and use the separate skill or return named in Scope | [FTB Form 100 instructions](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html) |

## Worked cases

### Case A: multistate C corporation using the single-sales factor

A mature general C corporation has California net income before apportionment of $500,000, a California sales factor of 70%, no California-allocated nonbusiness income, no credits, and no AMT. The California income measure is $350,000; tax at 8.84% is $30,940. This exceeds the $800 minimum.

```oa-check
name: Mature C corporation, California sales factor (2026)
inputs:
  everywhere_business_income: 500000
  california_sales_factor: 0.70
  general_corporation_rate: 0.0884
  minimum_franchise_tax: 800
steps:
  - california_business_income: everywhere_business_income * california_sales_factor
  - measured_tax: california_business_income * general_corporation_rate
  - california_tax: max(measured_tax, minimum_franchise_tax)
expected:
  california_business_income: 350000
  measured_tax: 30940
  california_tax: 30940
```

### Case B: choose the first-year rule or the ordinary minimum

A newly incorporated and SOS-registered C corporation has $5,000 of California net income in its first taxable year. Its measured tax is $442, and first-year minimum-tax relief means the tax is $442. If the same facts occur in a later year, the $800 minimum raises the liability to $800. The difference is $358.

```oa-check
name: First-year relief compared with ordinary minimum
inputs:
  california_net_income: 5000
  general_corporation_rate: 0.0884
  minimum_franchise_tax: 800
steps:
  - measured_tax: california_net_income * general_corporation_rate
  - first_year_tax: measured_tax
  - later_year_tax: max(measured_tax, minimum_franchise_tax)
  - difference: later_year_tax - first_year_tax
expected:
  measured_tax: 442
  first_year_tax: 442
  later_year_tax: 800
  difference: 358
```

## When to refuse or refer

- The corporation's legal or federal tax classification is uncertain, or an LLC election may be missing or inconsistent.
- California nexus, commercial domicile, Public Law 86-272 protection, market assignment, or unitary status is disputed.
- The filing requires a water's-edge election, combined-report position, credit assignment, tax-credit transfer, or transfer-pricing analysis.
- The corporation has a pending FTB or IRS audit, assessment, refund claim, protest, or statute-of-limitations issue.
- The corporation is suspended or forfeited, has an unfiled final return, or is in a dissolution or merger.
- A federal OBBBA change, current-year California conformity change, or not-yet-published 2026 Form 100 instruction could affect the result.
- A corporation relies on the deployed-military, convention/trade-show, exempt-organization, or inactive-mining exception.

## Filing and payment

For calendar-year 2026, most C corporations must file Form 100 by 15 April 2027 and generally receive an automatic filing extension to 15 November 2027; tax is due by 15 April 2027. Farmers' cooperative associations have a special original deadline on the 15th day of the ninth month after year-end and an extended deadline on the 15th day of the 16th month after year-end. Apply weekend, holiday and disaster postponements to the applicable deadline. The automatic extension is unavailable to a business entity suspended on or after the original due date.

Use the 2026 Form 100-ES instructions for estimates. The ordinary installment dates fall on the 15th day of months 4, 6, 9 and 12. The usual percentages are 30%, 40%, 0% and 30%. Apply the first-installment minimum franchise tax and any exception using the 2026 instructions. A corporation that meets the FTB's electronic-payment threshold must remit payments electronically; do not mail a payment voucher when the payment was made electronically.

Late filing can generally cost 5% of tax due after timely payments per month, up to 25%. Late payment can generally cost 5% plus 0.5% per month or part of a month, also capped at 25%; when both apply, the combined cap is 25% of unpaid tax. A required electronic-payment failure can add 10% of the amount not paid electronically. Check the current FTB instructions for penalty relief, interest and exceptions.

For corporations with foreign ownership or foreign subsidiaries, check whether Forms 5471, 5472 or 8975 must be attached or separately filed on time. Omission penalties can be substantial. Apportioning corporations must retain the records needed to support combined-report items, income classification and apportionment factors.

The 2025 Form 100 booklet is the latest published Form 100 return instruction as of 21 November 2026. Confirm the 2026 booklet, 2026 Schedule R, rate changes, filing deadlines and form line numbers before preparing or filing a 2026 return.

## Completion checklist

- Confirm federal classification, California SOS status, initial versus later year, and the corporation's tax year.
- Save the federal Form 1120, trial balance, California modifications, FTB 3885, NOL schedules, credit schedules and payment confirmations.
- Document the California nexus tests and the version/date of indexed thresholds used.
- Reconcile business income, nonbusiness income, Schedule R factors, group members and combined-report treatment.
- Compute measured tax, minimum tax, AMT, credits, estimates, payments and any penalty separately.
- Verify the original filing date, extension date, payment date, e-file requirement and EFT status.
- Attach all required schedules and disclosures, including FTB 4197 or federal information returns when applicable.
- Have a qualified California tax professional review every filing position and example before action.

## Sources

| Source | URL | Read on |
|---|---|---|
| California Revenue and Taxation Code, corporation tax and franchise tax, §§23038, 23101, 23114, 23151, 23153, 23186, 23501 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23151. | Not read (access blocked), attempted 2026-11-21 |
| California Revenue and Taxation Code, tax computation and filing, including §§18601, 18604, 18621.10, 19011, 23051.5, 23036.4, 23036.5, 24402, 24410, 24416.24, 24632, 19131, 19132, 19135, 19138, 19141.2, 19141.5, 19141.6, 19719 | https://leginfo.legislature.ca.gov/faces/codes.xhtml?lawCode=RTC | Not read (access blocked), attempted 2026-11-21 |
| California Revenue and Taxation Code, apportionment, §§25101, 25101.15, 25106, 25120, 25128, 25128.7, 25135, 25136 | https://leginfo.legislature.ca.gov/faces/codes.xhtml?lawCode=RTC | Not read (access blocked), attempted 2026-11-21 |
| California FTB, 2025 Instructions for Form 100 Corporation Tax Booklet | https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html | 2026-11-21; read for rates, filing, penalties, NOL, credits, reporting |
| California FTB, 2026 Instructions for Form 100-ES Corporation Estimated Tax | https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html | 2026-11-21; read for rates, estimates, installments, minimum and exceptions |
| California FTB, conformity to federal law | https://www.ftb.ca.gov/tax-pros/law/conformity.html | 2026-11-21; read for the IRC conformity date and state-law differences |
| California FTB, November 2025 tax news on SB 711 conformity | https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/11.html | 2026-11-21; read for SB 711 and post-January 2025 federal-law changes |
| California FTB, December 2025 Tax News, Business Electronic Filing Mandate | https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/12.html | 2026-11-21; read for the 10-return corporate e-file threshold effective for taxable years beginning in 2025 |
| California FTB, 2025 Instructions for Schedule R | https://www.ftb.ca.gov/forms/2025/2025-100r-instructions.html | 2026-11-21; read for apportionment, business income, market sourcing and group returns |
| California FTB, Doing business in California and indexed thresholds | https://www.ftb.ca.gov/file/business/doing-business-in-california.html | 2026-11-21; read for nexus tests and published thresholds |
| California FTB, Corporations and C corporations | https://www.ftb.ca.gov/file/business/types/corporations/c-corporations.html | 2026-11-21; read for corporate filing and tax overview |
| California FTB, business due dates | https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html | 2026-11-21; read for general Form 100 filing and extension dates |
| California FTB, e-file calendars | https://www.ftb.ca.gov/tax-pros/efile/e-file-calendars.html | 2026-11-21; read for special farmers' cooperative Form 100 original and extended return dates |
| California FTB, apportionment and allocation | https://www.ftb.ca.gov/file/business/income/apportionment-and-allocation.html | 2026-11-21; read for allocation and apportionment overview |
| California FTB, Guidelines for Corporations Filing a Combined Report (Publication 1061) | https://www.ftb.ca.gov/forms/misc/1061.html | 2026-11-21; read for combined-report overview and group-return rules |
| California FTB, Pub. 1024 Penalty reference chart | https://www.ftb.ca.gov/forms/misc/1024.html | 2026-11-21; read for demand-to-file, suspended or forfeited corporation, information-reporting and record-maintenance penalties |
| California FTB, Manual of Audit Procedures, Chapter 11 | https://www.ftb.ca.gov/tax-pros/procedures/manual-of-audit-procedures/chapter-11.pdf | 2026-11-21; read for large-corporate-understatement threshold and combined-report group treatment |
| United States Code of Federal Regulations, 31 C.F.R. §10.37 (GovInfo official edition) | https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol1/xhtml/CFR-2025-title31-vol1-subtitleA.html | 2026-11-21; read for §10.37 requirements for written tax advice |

Not yet confirmed: the direct text of the cited R&TC sections (the official LegInfo pages blocked access); final line instructions, credits, forms and any law changes in the 2026 Form 100 booklet and 2026 Schedule R (not published as of 21 November 2026); the 2026 indexed doing-business thresholds (not listed by the FTB as of that date); and the 2026 application of FTB information-reporting and records penalties because the 2025 Form 100 booklet and FTB Pub. 1024 revised 1/2026 conflict on amounts, continuation penalties or caps. The tax rules above are cross-referenced to the FTB's opened 2025 Form 100 booklet, 2026 Form 100-ES instructions, 2025 Schedule R instructions, 2026 Penalty reference chart and FTB audit manual. Use the listed 2025 nexus amounts only for the 2025 tax-year test.

> **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
