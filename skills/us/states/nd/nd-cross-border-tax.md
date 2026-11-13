---
name: nd-cross-border-tax
description: >-
  Use when a taxpayer or business crosses North Dakota borders (tax year 2025 figures):
  nonresident and part-year ND filing on Form ND-1, the ND-Minnesota and
  ND-Montana reciprocity agreements, military-service sourcing, the
  credit for income tax paid to another state, and the 0%/1.95%/2.50%
  bracket schedule (single: 0% to $48,475, 1.95% to $244,825, 2.50%
  above) verified from the Tax Commissioner's individual page. Trigger on
  North Dakota nonresident, ND-1 part-year, ND Minnesota reciprocity, ND
  military pay, credit for tax paid another state North Dakota.
  Source-cited draft; reciprocity and military cites need statute
  confirmation (ndlegis.nd.gov unreachable 2026-10-25).
jurisdiction: US-ND
category: cross-border
tax_year: 2025
tax_year_notes: Covers the 2025-2026 filing cycle, that is tax year 2025 figures for returns filed in 2026. North Dakota indexes its brackets and the 2026 amounts were not published when checked on 2026-11-13.
tier: 2
verified_by: pending
last_updated: 2026-11-13
version: 0.4
---

# North Dakota cross-border tax (nonresidents, reciprocity, military, credits)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

- Individuals who work in ND but live elsewhere (ND-source wages), live in ND but work elsewhere, or move in/out of ND mid-year (part-year Form ND-1).
- Residents of **Minnesota and Montana** working in ND under reciprocity agreements (exempt from ND wage withholding on employment income).
- Military personnel stationed in ND, and their spouses under federal Military Spouses Residency Relief Act (MSRRA) rules.
- Businesses with ND nexus but out-of-state owners, and part-year residents of border states (MN, MT, SD, Manitoba).

### 2. Core rules and rates

- **ND individual brackets (verified from the Tax Commissioner's individual income tax page, 2026-10-25):** single -- 0.00% to $48,475; 1.95% over $48,475 to $244,825; 2.50% over $244,825. MFJ/qualifying widow(er) -- 0% to $80,975; 1.95% to $298,075; 2.50% above. MFS -- 0% to $40,475; 1.95% to $149,025; 2.50% above. HOH -- 0% to $64,950; 1.95% to $271,450; 2.50% above. _(tax.nd.gov/individual-income-tax, 200 with text, 2026-10-25; the page presents these as the current schedule -- confirm the tax year against the Form ND-1 booklet before filing.)_
- **The 0% first bracket is the headline cross-border fact:** a nonresident whose ND-source wages fall entirely under the first bracket owes **zero ND income tax** even though a return may still be required. _(same source)_
- **Reciprocity.** ND maintains income-tax reciprocity with **Minnesota** and **Montana** (employment income taxable only in the state of residence; no ND withholding with a valid exemption certificate). _(US-ND-dr-ndwr.pdf: "North Dakota has income tax reciprocity agreements with Minnesota and Montana. If you are a resident of one of these states, the agreements provide that you do not have to pay North Dakota income tax on wages you earn for work in North Dakota.")_
- **Military.** Nonresident military personnel stationed in ND are not ND residents; military pay is sourced to the domicile state. Mobilized-employee relief exists as a **tax credit** against ND tax (Tax Commissioner page "Wages Paid to Mobilized Military Employee Tax Credit," verified 2026-10-25). MSRRA is federal and governs spousal sourcing.
- **Credit for income tax paid to another state or local jurisdiction** -- ND grants a credit (Form ND-CITP or per the Tax Commissioner page of the same name, verified live 2026-10-25) for tax lawfully paid to another state on the same income; the credit cannot exceed the ND tax attributable to that income.
- **ND has no state-level exit tax or entry tax.** _(no such levy appears in the Tax Commissioner's tax-type index, read 2026-10-25.)_

### 3. Base and adjustments

- Nonresidents: ND taxable income = ND-source income (wages for services performed in ND, ND business income, ND rental/real-property gains) allocated per the ND-1 instructions, then the bracket schedule applies to the **full** taxable income with a proration of the tax by the ND-source ratio (the exact ND-1 proration computation: see "Not yet confirmed:" in Sources).
- Reciprocity states: employment income is excluded from ND taxation; **non-employment** ND-source income (contract work, rentals, business) remains ND-taxable.
- Part-year: two short-period returns or one annual return with the residency split per the ND-1 instructions.
- The credit for tax paid to another state is claimed after the ND tax computation and is limited to the lesser of tax paid or ND tax on the same income.

### 4. Deadlines

- Form ND-1 (full-year, part-year, and nonresident): due **April 15** (same as federal); extension to October 15 by timely federal extension filing. _(existing `nd-income-tax` / `nd-return-assembly` skills; ND TAP payment mechanics verified on tax.nd.gov 2026-10-25.)_
- Withholding exemption certificate for reciprocity states: file with the employer before the first pay period of the year to stop ND withholding.
- Estimated tax (Form ND-1ES) quarterly if the expected balance due exceeds the threshold; interest applies to underpayment (US-ND-dr-nd1es2025.pdf: estimated tax not required where the balance due is under $1,000 -- "you do not have to pay estimated tax"; interest at 12% per year, US-ND-dr-nd1ut2025.pdf: "Interest of 12% per year is charged on" underpayments).

### 5. Penalties and interest

- Underpaid estimates: interest on the shortfall from the installment due date (US-ND-dr-nd1ut2025.pdf: "Interest of 12% per year is charged on" underpayments; US-ND-dr-nd1es2025.pdf: interest "of 12% per year from the installment" due date).
- Failure to file / failure to pay: Chapter 57-38 penalties; exact 2026 percentages: see "Not yet confirmed:" in Sources.
- Reciprocity error pattern: a Montana or Minnesota resident who fails to file the exemption certificate has ND withheld and must file an ND return to get it back -- a refund claim, not a penalty, but a common client complaint.

### 6. Cross-border and federal overlay

- SALT cap: ND tax paid (including by nonresidents) counts toward the federal $10,000 state-and-local deduction cap for itemizers (US-ND-dr-plaw119-21.txt, SEC. 70120 amending IRC § 164(b)(6), which carries the "$10,000 ($5,000 in the case of a married individual filing a separate return)" limitation).
- ND-Manitoba (Canada) border traffic: foreign-tax credit analysis is federal (see federal skills); ND's credit for tax paid to **another state** does not cover foreign tax.
- Treaty and MSRRA interactions are federal; ND follows the federal sourcing result.
- Employers: multi-state withholding follows the reciprocity certificate, not the employee's address.

### 7. Worked examples

**Example 1 -- Minnesota resident working in Fargo without reciprocity relief.** MN resident earns $55,000 of Fargo wages, no exemption certificate, so ND withheld; wages exceed the 0% bracket floor.

```oa-check
name: nd nonresident mn resident wages
inputs:
  wages: 55000
steps:
  - nd_taxable: wages
expected:
  nd_taxable: 55000
```

(The ND tax itself is then computed on the bracket schedule with the ND-source proration; because the reciprocity agreement makes the wages taxable only in MN, the correct fix is the exemption certificate plus a refund claim -- see §5.)

**Example 2 -- ND-source income of $100,000 for a nonresident, bracket math.** Assume the ND-1 computation applies the bracket schedule to ND taxable income.

```oa-check
name: nd bracket tax 100k single
inputs:
  ti: 100000
steps:
  - b1: (min(ti, 244825) - 48475) * 0.0195
  - tax: b1
expected:
  tax: 1004.74
```

(The 0% first $48,475 is real money for border commuters -- a $48,475-or-less commuter owes nothing.)

### 8. Ask the client first

1. Where is domicile, and did any move cross a state line mid-year?
2. Is the client a Montana or Minnesota resident working in ND? (Reciprocity certificate on file?)
3. Military: is the service member stationed in ND, and what is the claimed domicile? Does MSRRA cover the spouse's income?
4. What other states taxed the same income, and is the ND credit-for-tax-paid claim being made (or the other state's credit)?
5. Any ND real property, rentals, or business situs that keeps ND in scope even with no ND wages?

### 9. Sources

- ND Office of State Tax Commissioner -- individual income tax (bracket schedules, estimated-tax interest, ND-1ES): <https://www.tax.nd.gov/individual-income-tax> -- 200 with text, 2026-10-25.
- ND Tax Commissioner -- Credit for Income Tax Paid to Another State or Local Jurisdiction: <https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction> -- 200, 2026-10-25.
- ND Tax Commissioner -- Wages Paid to Mobilized Military Employee Tax Credit: <https://www.tax.nd.gov/wages-paid-mobilized-military-employee-tax-credit> -- 200, 2026-10-25 (linked from the site root, verified 2026-10-25).
- Existing `nd-income-tax`, `nd-payroll`, `nd-return-assembly` skills (reciprocity, filing mechanics) -- read 2026-10-25.
- Reciprocity statute cites, ND-1 nonresident proration mechanics, 2026 penalty/interest percentages: see the "Not yet confirmed:" paragraph below -- ndlegis.nd.gov DNS failure (getaddrinfo) on 2026-10-25; Justia mirror 403.

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at the OpenAccountants network.

- Use it in your AI: 
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Who this applies to

No figures stated in this section.

## Rates, bands and thresholds

No figures stated in this section.

## The taxable base

No figures stated in this section.

## Deadlines and filing

No figures stated in this section.

## Penalties and interest

No figures stated in this section.

## Cross-border points

No figures stated in this section.

## Worked examples

No figures stated in this section.

## Ask the client first

No figures stated in this section.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| US-ND-dr-nd-booklet2024.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2024-iit/2024-individual-income-tax-booklet.pdf | 2026-10-28 |
| US-ND-dr-nd-withholding-2025.pdf | https://www.tax.nd.gov/sites/www/files/documents/misc-discuss-folder/Final_2025%20Income%20Tax%20Withholding%20Rates%20%20Instructions.pdf | 2026-10-28 |
| US-ND-dr-ndwr.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf | 2026-10-28 |
| US-ND-dr-nd-walsh-county-notice-2026.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/sales-use/local-jurisdiction-rates/2026-jurisdiction/notice-to-walsh-county-permit-holders.pdf | 2026-10-28 |
| US-ND-dr-t57c51-1.pdf | https://ndlegis.gov/cencode/t57c51-1.pdf | 2026-10-28 |
| US-ND-dr-usc26-1.txt | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1&num=0&edition=prelim | 2026-10-28 |
| US-ND-dr-ndcc-57-39-2.pdf | https://ndlegis.gov/cencode/t57c39-2.pdf | 2026-10-28 |
| US-ND-tap.html | https://tap.tax.nd.gov/?Check=1 | 2026-10-28 |

Not yet confirmed: figures in this skill lack archived line-citations.
- Exact ND-1 nonresident proration mechanics (bracket schedule applied to full taxable income with tax prorated by the ND-source ratio).
- Exact 2026 Chapter 57-38 failure-to-file / failure-to-pay penalty percentages (ndlegis.nd.gov DNS failure 2026-10-25).


| Source | URL | Read on |
| --- | --- | --- |
| (see "Not yet confirmed:" paragraph) | -- | 2026-10-28 |

No figures stated in this section.

## Talk to a verified accountant

No figures stated in this section.
