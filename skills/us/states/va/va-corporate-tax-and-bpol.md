---
name: va-corporate-tax-and-bpol
description: Compute Virginia corporate income tax (Form 500) for tax year 2026 and the local BPOL gross receipts license tax. Covers the 6% rate on Virginia taxable income, the December 31, 2025 conformity date, the standard double-weighted sales apportionment formula and the single sales factor industries, separate, consolidated or combined filing, Form 500 due dates (15th day of the 4th month) with the automatic 7-month extension, Form 500ES estimated tax when tax is expected to exceed $1,000, penalties, the pass-through entity return (Form 502), 5% nonresident owner withholding, the 5.75% elective PTET (Form 502PTET), and BPOL rate caps per $100 of gross receipts ($0.16 contractors, $0.20 retail, $0.58 financial, real estate and professional, $0.36 repair, personal and business services, $0.05 per $100 of purchases for wholesalers) with the $100,000 / $50,000 thresholds and the March 1 license date. Trigger on "Virginia corporate tax", "Form 500", "Virginia apportionment", "Virginia PTET", "Form 502", "BPOL", "Virginia business license tax". Not for the US Virgin Islands (see skills/us-virgin-islands).
version: "2.1"
jurisdiction: US-VA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# Virginia corporate income tax (Form 500), PTET and local BPOL tax, tax year 2026

> **Source-cited draft.** Built from Va. Code §§ 58.1-390.3, 58.1-400, 58.1-408, 58.1-3700.1, 58.1-3703, 58.1-3703.1, 58.1-3706, 58.1-3709, 58.1-3715 and 58.1-3716, the 2025 Form 500 instructions and the 2025 Form 502 instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A corporation with Virginia income pays 6% of Virginia taxable income (Va. Code § 58.1-400). Multistate corporations apportion with property plus payroll plus twice sales, divided by four (§ 58.1-408), unless they are in an industry that must use a single sales factor (motor carriers, financial corporations, construction, railways, retailers, debt buyers, manufacturers that elect, certain data center operators). Form 500 is due the 15th day of the 4th month after year end (April 15, 2027 for calendar 2026), with an automatic 7-month extension to file if 90% of the tax is paid by the original date. A partnership or S corporation files Form 502 (or Form 502PTET if it elects the 5.75% entity-level tax, available through Taxable Year 2026). BPOL is a separate local tax on gross receipts, set by each county, city or town within state caps; licenses are generally due by March 1.

## Scope and who this is for

This skill covers: Virginia corporate income tax on Form 500 for C corporations; the pass-through entity return of income (Form 502), nonresident owner withholding and the elective pass-through entity tax (PTET, Form 502PTET) at the entity level; and the local Business, Professional and Occupational License (BPOL) tax under Va. Code Title 58.1, Chapter 37.

It does not cover: the owner's Form 760 (see `va-income-tax`, which also covers the PTET credit an owner claims), sales and use tax (`va-sales-tax`), payroll (`va-payroll`), the bank franchise tax, insurance premiums tax, public service corporations, telecommunications (Form 500T), electric cooperatives, local real estate, personal property and machinery and tools taxes, and each locality's actual BPOL rates (set by local ordinance; ask the locality's Commissioner of the Revenue). Virginia (US-VA) is not the US Virgin Islands (`skills/us-virgin-islands`).

## Ask the client first

1. **Entity type and federal classification** (C corporation, S corporation, partnership, LLC and how it is taxed, disregarded entity). This picks Form 500, Form 502 or Form 502PTET, or nothing at entity level.
2. **Tax year** (calendar or fiscal) and whether the entity is a nonprofit (different due dates and extension).
3. **Where the business operates**: Virginia only, or several states; property, payroll and sales in and out of Virginia; the industry (for the single sales factor rule).
4. **Affiliated corporations** with Virginia income, and the filing method used in past years (separate, consolidated or combined).
5. **For a pass-through: owners' residence** (nonresident owners trigger 5% withholding) and whether the PTET election is wanted for 2026.
6. **For BPOL: each county, city or town where the business has a definite place of business**, its gross receipts by locality and by activity (contracting, retail, professional, repair and services, wholesale).

## The method, step by step

1. **Who files.** Every Virginia corporation, every foreign corporation registered with the State Corporation Commission, and every corporation with income from Virginia sources files Form 500 through the Federal/State e-File program, unless an exception applies. S corporations (not taxed under § 58.1-400) file Form 502.
2. **Start from federal taxable income** and make the Virginia additions and subtractions (Schedule 500ADJ), including the fixed-date conformity adjustments: Virginia conforms to the Internal Revenue Code as of December 31, 2025 but decouples from immediate expensing of domestic research and experimental expenditures, immediate expensing of qualified production property and the increased section 179 limits from P.L. 119-21 (2025 Form 500 instructions; Tax Bulletin 26-1), and continues to decouple from federal bonus depreciation. The individual-side detail is in `va-income-tax`.
3. **Apportion multistate income** on Schedule 500A. Standard formula: (property factor + payroll factor + 2 x sales factor) / 4. If there is no sales factor, divide by the number of factors that exist; if the sales factor exists but payroll or property does not, divide by the existing factors plus one (§ 58.1-408 A). Industries in §§ 58.1-417 to 58.1-420 and 58.1-422 to 58.1-422.3 use a single sales factor. A corporation with all its business in Virginia does not apportion.
4. **Compute the tax**: Virginia taxable income (Form 500 Line 7, or apportioned income on Line 8(a)) x 6% = Line 9. Subtract nonrefundable credits from Schedule 500CR (Line 10).
5. **Estimated tax**: a calendar-year corporation whose Virginia tax can reasonably be expected to exceed $1,000 pays 25% by April 15, June 15, September 15 and December 15 (Form 500ES, electronically). Fiscal-year filers use the 15th day of the 4th, 6th, 9th and 12th months. Underpayments: addition to tax at the underpayment interest rate under Va. Code § 58.1-504, on Form 500C.
6. **File and pay** electronically by the 15th day of the 4th month (15th day of the 6th month for nonprofits). Form 500EZ on eForms is available only to small all-Virginia corporations meeting every listed condition (including federal taxable income of $40,000 or less).
7. **Pass-through entities** file Form 502 by the 15th day of the 4th month, withhold 5% of each nonresident owner's Virginia-source share (paid by the original due date; the extension does not cover it), or elect PTET on a timely filed Form 502PTET (including extensions) and pay 5.75% on eligible owners' shares.
8. **BPOL**, separately, in each locality: classify each line of business, apply the locality's rate per $100 to the gross receipts (wholesalers: purchases) of the preceding year for a renewing business, check the locality's threshold, and file and pay by March 1 (or the later date the locality has adopted, up to May 1).

### Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| Corporate income tax rate | six percent of Virginia taxable income | Every Virginia corporation and every foreign corporation with Virginia-source income | [Va. Code § 58.1-400](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-400/) |
| Standard apportionment | (Property + payroll + 2 x sales) / 4 | Unless a single sales factor industry; denominator adjusts when a factor is missing | [Va. Code § 58.1-408](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-408/); [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Single sales factor | Required for motor carriers, financial corporations, construction corporations, railways, retail companies, debt buyers, manufacturers electing the modified method, certain enterprise data center operations | §§ 58.1-417 to 58.1-420 and 58.1-422 to 58.1-422.3 | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Conformity date | Internal Revenue Code as of December 31, 2025 | Decoupled: R&E expensing, qualified production property expensing, increased section 179 limits | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Form 500 due date | 15th day of the 4th month after year end; nonprofits 15th day of the 6th month | Weekend or holiday moves to the next business day | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Automatic extension | 7 months (6 months for nonprofits and entities other than C corporations) | Extends filing, not payment; at least 90% of tax due by the original date | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Extension penalty | 2% a month or part month, up to 14% (12% for nonprofits and non-C corporations) | When filed within the extension but under 90% paid by the original date | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Late filing penalty | 30% of the balance due; minimum $100 | Return filed after the extended due date; the $100 minimum applies even with no tax due | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Late payment penalty | 6% a month from filing to payment, up to 30% | Return filed within the extension without full payment | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Interest | IRC § 6621 underpayment rate plus 2% | From the due date until paid | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Estimated tax trigger | Tax expected to exceed $1,000 | 25% installments, April 15, June 15, September 15, December 15 (calendar year) | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Form 500EZ | Federal taxable income $40,000 or less, 100% Virginia business, additions and subtractions each $1,000 or less, plus the other listed conditions | eForms | [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf) |
| Nonresident owner withholding (Form 502) | 5% of each nonresident owner's Virginia-source share | Due by the original Form 502 due date; exceptions include owners on a composite return (Form 765), PTE owners, exempt entities and non-captive REITs | [2025 Form 502 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-502-instructions.pdf) |
| Form 502 very late | Greater of 30% of the tax due or $1,200 | Filed more than 6 months after the due date or more than 30 days after the federal extended due date, whichever is later | [2025 Form 502 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-502-instructions.pdf) |
| PTET rate | 5.75% of Virginia taxable income attributable to eligible owners | Annual election on a timely filed Form 502PTET, including extensions; Taxable Years 2021-2026 per the instructions; nonresident owners' shares limited to Virginia-source income | [Va. Code § 58.1-390.3](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-390.3/); [2025 Form 502 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-502-instructions.pdf) |
| BPOL cap, contracting and building for own account for sale | sixteen cents per $100 of gross receipts | Above the threshold; a higher rate in force on January 1, 1978 may be kept | [Va. Code § 58.1-3706](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/) |
| BPOL cap, retail sales | twenty cents per $100 of gross receipts | Short-term rental businesses are classed as retail | [Va. Code § 58.1-3706](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/) |
| BPOL cap, financial, real estate and professional services | fifty-eight cents per $100 of gross receipts | Same grandfather rule | [Va. Code § 58.1-3706](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/) |
| BPOL cap, repair, personal and business services and all others | thirty-six cents per $100 of gross receipts | Same grandfather rule | [Va. Code § 58.1-3706](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/) |
| BPOL cap, wholesale merchants | 5 cents per $100 of purchases | Unless the locality's January 1, 1964 rate was higher | [Va. Code § 58.1-3716](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3716/) |
| BPOL threshold | No tax below $100,000 of gross receipts (locality over 50,000 people) or $50,000 (25,000 to 50,000 people) | The locality may charge only the license fee below it | [Va. Code § 58.1-3706](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/) |
| BPOL license fee | Up to $50 (over 50,000 people, after the required reduction), $50 (25,000 to 50,000), $30 (under 25,000) | No tax on the gross receipts the fee covers | [Va. Code § 58.1-3703](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3703/) |
| BPOL license date | March 1 for a renewing business (a locality may adopt a later date up to May 1); a new business applies before it begins | Penalty up to 10% of the tax for late application or payment, plus interest | [Va. Code § 58.1-3703.1](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3703.1/) |
| Contractor working in another locality | That locality may require a license once business there exceeds $25,000 in a year | Receipts taxed there may be deducted at the home office locality | [Va. Code § 58.1-3715](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3715/) |

### Filing methods for affiliated corporations

An affiliated group may file separate returns, a consolidated return or a combined return. A request to change method must reach the Department before the due date of the first return using the new method; after a group elects consolidated or combined filing, later returns follow that method. Worldwide consolidation including controlled foreign corporations is prohibited (Va. Code § 58.1-443). Virginia does not require unitary combined reporting. ([2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf))

### BPOL definitions that decide the answer

- **Definite place of business**: an office or location with a regular and continuous course of dealing for 30 consecutive days or more; a person's residence counts if there is no other definite place of business ([Va. Code § 58.1-3700.1](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3700.1/)).
- **A place of business straddling a boundary** is licensed in each locality, with receipts split by floor area used ([Va. Code § 58.1-3709](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3709/)).
- **Software**: a locality may exempt the creation of computer software for lease, sale or license by ordinance ([Va. Code § 58.1-3703](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3703/) B).
- **Federal research contracts**: prime contractors on identifiable federal R&D appropriations in the listed fields are capped at $0.03 per $100 of those receipts ([Va. Code § 58.1-3706](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/) D).
- **Not licensable by localities**: public service corporations and certain carriers, sellers of farm, domestic and nursery products, and the other § 58.1-3703 C exclusions.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Corporation does all its business in Virginia | No apportionment; tax 6% of Virginia taxable income |
| Multistate retailer | Single sales factor, not the double-weighted formula |
| Manufacturer | Double-weighted formula unless it elects the modified (single sales factor) method under § 58.1-422 |
| No property factor | Denominator is the existing factors plus one (sales counted twice) |
| No sales factor | Denominator is the number of existing factors |
| Tax expected to be exactly $1,000 | No estimated tax required ("exceed $1,000") |
| 89% of tax paid by the original due date, return filed within the extension | Extension penalty 2% a month on the balance, up to 14% |
| Return filed after the 7-month extension | 30% late filing penalty, at least $100 |
| S corporation | Not taxed under § 58.1-400; files Form 502 (or 502PTET) |
| Single-member LLC disregarded for federal tax | Not a pass-through entity for PTET; its owner reports on their own return |
| PTE elects PTET | Files Form 502PTET instead of Form 502; eligible owners claim a refundable credit and add back the entity's state tax deduction |
| Nonresident owner included on a composite return (Form 765) | No 5% withholding for that owner |
| Business with $90,000 gross receipts in a county of 120,000 people | No BPOL tax; at most the license fee |
| Business with $250,000 gross receipts in that county | Tax at the local rate on gross receipts above what the fee covers (see Case 3) |
| Contractor from another locality doing $20,000 of work in a county | That county may not require a license; above $25,000 it may |
| Locality rate above the § 58.1-3706 cap | Possible only if it was in force on January 1, 1978 (grandfather rule) |

### Red flags to raise with the client

| Flag | Why |
| --- | --- |
| Federal return used bonus depreciation, section 179 above the old limit or immediate R&E expensing | Virginia additions this year and subtractions in later years |
| Group switched filing method without a timely request | The Department may refuse the change |
| Nonresident owners and no 5% withholding paid by the original date | Penalties; the extension does not cover the payment |
| Consulting or IT firm classed as "business services" by one locality and "professional" by another | BPOL classification is the most common local dispute; ask the locality |

## Worked cases

**Case 1, double-weighted apportionment.** A Virginia manufacturer that has not elected the single sales factor has Virginia taxable income before apportionment of USD 5,200,000. Property: USD 20,000,000 in Virginia of USD 30,000,000. Payroll: USD 8,000,000 of USD 12,000,000. Sales: USD 10,000,000 of USD 50,000,000. Factor = (66.67% + 66.67% + 2 x 20%) / 4 = 43.33%. Virginia income USD 2,253,333.33, tax at 6% USD 135,200. Had it elected the single sales factor, the factor would be 20% and the tax USD 62,400: an election worth testing each year.

```oa-check
name: VA 2026 corporate tax, double-weighted sales apportionment
inputs:
  income: 5200000
  property_va: 20000000
  property_all: 30000000
  payroll_va: 8000000
  payroll_all: 12000000
  sales_va: 10000000
  sales_all: 50000000
steps:
  - factor: (property_va / property_all + payroll_va / payroll_all + 2 * sales_va / sales_all) / 4
  - va_income: income * factor
  - tax: va_income * 0.06
  - tax_single_sales: income * sales_va / sales_all * 0.06
expected:
  va_income: 2253333.33
  tax: 135200.00
  tax_single_sales: 62400.00
```

**Case 2, a decision: elect PTET for 2026?** A Virginia S corporation has two equal resident shareholders and USD 400,000 of Virginia taxable income. Electing on Form 502PTET costs USD 23,000 (5.75%) at entity level; each owner claims a USD 11,500 refundable credit and adds back their share of the entity's deduction, so Virginia tax is roughly unchanged. The election pays where the owners could not deduct Virginia income tax federally because of the federal SALT cap: at a 35% federal marginal rate the entity-level deduction saves USD 8,050. If the owners' own SALT deductions are already under the federal cap (see the federal skills for the 2026 cap), the saving shrinks toward zero and the election only adds work. Elect when the saving exceeds the extra compliance cost and the owners' home states give credit.

```oa-check
name: VA 2026 PTET election, entity tax and federal deduction value
inputs:
  va_income: 400000
  owners: 2
  federal_rate: 0.35
steps:
  - ptet: va_income * 0.0575
  - credit_per_owner: ptet / owners
  - federal_saving_if_capped: ptet * federal_rate
expected:
  ptet: 23000.00
  credit_per_owner: 11500.00
  federal_saving_if_capped: 8050.00
```

**Case 3, BPOL at the state cap.** A professional services firm has USD 500,000 of prior-year gross receipts at its only office, in a county of over 50,000 people whose ordinance taxes professional services at the USD 0.58 cap with no tax under USD 100,000. BPOL = USD 500,000 / 100 x USD 0.58 = USD 2,900, due by March 1 (or the locality's later date). A locality at a lower rate charges less; the ordinance governs, and whether the first USD 100,000 is excluded or only a threshold depends on it.

```oa-check
name: VA 2026 BPOL, professional services at the 0.58 cap
inputs:
  gross_receipts: 500000
  rate_per_100: 0.58
steps:
  - bpol: gross_receipts / 100 * rate_per_100
expected:
  bpol: 2900.00
```

## When to refuse or refer

- Banks (bank franchise tax), insurance companies, public service corporations, telecommunications (Form 500T), electric cooperatives (Schedule 500EL), home service contract providers (Form 500HS).
- Alternative or special apportionment petitions, nonapportionable investment income claims (Allied Signal) and the single sales factor industry formulas in detail.
- Consolidated or combined group computations, and any change of filing method.
- Net operating loss carryovers, partnership-level federal audit adjustments (Form 502FED-1) and amended returns after a federal change.
- Tax credits on Schedule 500CR beyond the headline.
- A locality's actual BPOL rate, classification ruling, appeal or audit: refer to that locality's Commissioner of the Revenue; the Department of Taxation hears BPOL appeals after a local determination.
- Owners' home-state credit for the Virginia PTET: depends on the other state's law.

## Filing and payment

| Return | Due | How |
| --- | --- | --- |
| Form 500 (calendar 2026) | April 15, 2027; extended to November 15, 2027 by the automatic 7-month extension, if 90% paid by April 15 | Federal/State e-File; Form 500EZ, 500V, 500CP, 500ES via eForms or Business Online Services |
| Form 500ES (calendar 2026) | April 15, June 15, September 15 and December 15, 2026, 25% each | Electronically |
| Form 502 / Form 502PTET (calendar 2026) | April 15, 2027; automatic 6-month extension to file | e-File; withholding payment on Form 502W by April 15, 2027 |
| BPOL (license year 2026) | March 1, 2026 for renewals (or the locality's later date, up to May 1); new businesses before beginning | The locality's Commissioner of the Revenue or finance office |

Sources: [2025 Form 500 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf); [2025 Form 502 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-502-instructions.pdf); [Va. Code § 58.1-3703.1](https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3703.1/).

## Completion checklist

- [ ] Right return chosen: Form 500, 502 or 502PTET.
- [ ] Federal taxable income adjusted for the December 31, 2025 conformity date and the decouplings.
- [ ] Apportionment formula matches the industry; factors tie to the books.
- [ ] Filing method for affiliates unchanged, or a change requested in time.
- [ ] Estimated payments tested against the $1,000 trigger.
- [ ] At least 90% of tax paid by the original due date if extending.
- [ ] Nonresident owner withholding paid by the original Form 502 due date, or the PTET election made.
- [ ] BPOL: each locality with a definite place of business identified, receipts classified, threshold and local rate checked, license renewed by March 1 (or the local date).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Va. Code § 58.1-400. Read for the 6% rate. | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-400/ | 2026-11-13 |
| Va. Code § 58.1-408. Read for the double-weighted sales formula, the missing-factor rules and the excluded industries. | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-408/ | 2026-11-13 |
| Va. Code § 58.1-390.3. Read for the PTET election, the 5.75% rate, nonresident owners and the owner credit with add-back. | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-390.3/ | 2026-11-13 |
| 2025 Form 500 instructions. Read for who files, due dates, the 7-month extension, penalties, interest, estimated tax, Form 500EZ, filing methods, apportionment and the conformity update. | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf | 2026-11-13 |
| 2025 Form 502 instructions. Read for the PTET (Taxable Years 2021-2026), 5% nonresident withholding, its exceptions and the Form 502 penalties. | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-502-instructions.pdf | 2026-11-13 |
| Va. Code § 58.1-3700.1. Read for "definite place of business". | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3700.1/ | 2026-11-13 |
| Va. Code § 58.1-3703. Read for license fee limits, the software exemption option and the excluded businesses. | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3703/ | 2026-11-13 |
| Va. Code § 58.1-3703.1. Read for the March 1 date, the later local date up to May 1, the 10% penalty and interest. | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3703.1/ | 2026-11-13 |
| Va. Code § 58.1-3706. Read for the rate caps, the $100,000 / $50,000 thresholds, the 1978 grandfather rule, short-term rentals and federal R&D contracts. | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/ | 2026-11-13 |
| Va. Code § 58.1-3709. Read for businesses straddling a boundary. | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3709/ | 2026-11-13 |
| Va. Code § 58.1-3715. Read for contractors and the $25,000 rule. | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3715/ | 2026-11-13 |
| Va. Code § 58.1-3716. Read for the wholesale cap. | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3716/ | 2026-11-13 |

Not yet confirmed: the 2026 Form 500 and Form 502 instructions were not yet published when read (2025 editions used; the 2026 estimated tax dates follow the same rule); whether the PTET continues after Taxable Year 2026 (the 2025 instructions say 2021-2026; the 2026 amendment, 2026 c. 7, was not read); each locality's BPOL rates, thresholds and dates (set by ordinance, not a state source); the 2026 statutory interest rate.
