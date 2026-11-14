---
name: ar-corporate-tax
description: "Arkansas corporation income tax for tax year 2026: graduated rates, AR1100CT, market-based sourcing, economic nexus, estimated payments and the separate annual franchise-tax obligation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ar-corporate-tax"
  jurisdiction: "US-AR"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Arkansas corporate income and franchise tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; no accountant has reviewed this version. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** The 2026 corporation income-tax top rate remains 4.3% above $11,000 of Arkansas net taxable income. Act 2 lowers it to 4.1% only for tax years beginning on or after January 1, 2027. Income tax and annual franchise tax are separate obligations. [DFA 2025-2026 filing cycle booklet p.5](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf); [Act 2 sections 2-3](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf).

## Scope

Ordinary domestic and foreign C corporations filing Arkansas AR1100CT, plus the separate franchise-tax identification step. Federal taxable-income computations belong to `us-form-1120-c-corp` and `us-section-179-and-bonus-depreciation`. This skill computes ordinary state tax after Arkansas adjustments; it does not compute bank, insurance, cooperative, exempt-organization, consolidated-group or pass-through returns.

## Ask the client first

1. Entity legal form, tax classification, incorporation/registration dates and tax-year start/end?
2. Property, staff, agents and receipts in Arkansas in the current and preceding years?
3. Federal return, Arkansas income/deduction reconciliation, NOL vintages and credit schedules?
4. For each receipt, customer delivery/use location, product/service character and other-state taxability?
5. Assigned account ID, prior-year liability, estimated payments, extensions and notices?
6. Franchise-tax classification, par-value stock and Arkansas/total real and personal property?

## The method, step by step

### Rates, bands and thresholds

| Rule and period | Amount | Official source |
| --- | --- | --- |
| 2026 corporate net income first $3,000 | 1% | [DFA booklet p.25; section 26-51-205](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf) |
| Next $3,000, through $6,000 | 2% | [DFA booklet p.25](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf) |
| Next $5,000, through $11,000 | 3% | [DFA booklet p.25](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf) |
| 2026 net income exceeding $11,000 | $240 plus 4.3% of excess | [DFA booklet p.25](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf) |
| Top rate for tax years starting January 1, 2027 or later, not a 2026 rate | 4.1% above $11,000 | [Act 2 sections 2-3](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf) |
| No-physical-presence nonresident corporation/partnership, current or immediately preceding tax year, from 2026 | Arkansas receipts **exceeding $250,000** create statutory nexus | [Act 719 section 2, section 26-51-202(f)](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf) |
| Ordinary stock corporation franchise tax, allocated par-value base | 0.3%; $150 minimum | [Legislative handbook section 8.4; section 26-54-104](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf) |
| Corporation without authorized stock, other than special classes | $300 franchise tax | [Legislative handbook section 8.4](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf) |
| Income-tax declaration, 2025-2026 filing cycle instructions | Expected tax **over $1,000** | [DFA booklet p.11](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf) |
| Estimated quarterly tax electronic-payment threshold | $20,000 or more, subject to DFA notice | [DFA booklet p.8; section 26-19-106](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf) |

1. **Identify filing obligation.** Domestic/registered corporations and corporations with Arkansas-source income file AR1100CT. For 2026, test Act 719 economic nexus even without physical presence, and separately assess federal P.L. 86-272 protection using `us-pl-86-272-income-tax-nexus`. Do not confuse the corporate $250,000 receipts test with sales-tax nexus. S corporations use AR1100S, outside this computation. [DFA pp.4,10](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf); [Act 719 section 2](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf).
2. **Build Arkansas income and deductions.** The 2025-2026 filing cycle AR1100CT has separate state income/deduction lines. Reconcile federal amounts to state treatment; do not simply multiply federal taxable income by a state rate. Line 27 is income before NOL, line 28 allowed NOL (not above income), and line 29 net taxable income or Schedule A Part C result. Keep state depreciation and NOL-vintage schedules. [DFA pp.13-15](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf). Final 2026 line mapping must be checked when issued.
3. **Source and apportion multistate income.** Act 719 replaces cost-of-performance sourcing with market sourcing from tax years beginning January 1, 2026. Ordinary apportionable income uses Arkansas receipts divided by everywhere receipts (section 26-51-709). Service receipts follow where delivered; leased/licensed intangibles follow use. Nonapportionable income is allocated separately. If assignment cannot be determined, reasonably approximate; Act 719 also has denominator exclusions and special elections. Keep the sourcing workpaper. [Act 719 sections 3-6](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf).
4. **Apply the 2026 graduated rates** to Arkansas net taxable income, subtract allowed Arkansas credits and payments, and compute any AR2220 underpayment amount. Do not apply the future 2027 rate early. [DFA p.25](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf); [Act 2](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf).
5. **File and pay.** Use [ATAP](https://atap.arkansas.gov) for corporation account management, return/XML upload and payments, or the state's approved e-file channel. Select corporation income tax and the tax period; enter the Arkansas schedules, attach the federal return and reconciliation, obtain officer approval/signature, submit and retain acceptance/payment references. AR1100CTV accompanies a mailed balance payment. [DFA pp.2,7,9-12](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf).
6. **Address franchise tax separately.** Identify the Secretary of State annual franchise-tax report, legal entity class and allocated stock base. For an ordinary stock corporation, allocate par value by Arkansas real/personal property divided by everywhere property; multiply by 0.3%, subject to $150 minimum. Newly formed corporations first report in the calendar year after incorporation. The income-tax loss or S election does not itself remove franchise tax. [Legislative handbook section 8.4](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf). LLCs formed under the Uniform Limited Liability Company Act pay the $150 minimum under section 26-54-104(a)(8). The annual report describes the preceding calendar-year end and report/payment are due May 1 of the reporting year; an authorized individual signs the statutory declaration. [Act 459 sections 4-7](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2023R%2FPublic%2FACT459.pdf). Franchise portal steps remain a gap below; do not mark the entity complete without that report.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Service or intangible receipts in several states | 2026 market sourcing, reasonable approximation and denominator exclusions; refer if facts cannot locate the market. |
| Arkansas shipment to a purchaser in a state where corporation is not taxable | Throwback is phased out; the 2026 Arkansas inclusion is 57.13%, elsewhere 42.87%, for this defined shipment category. Do not apply this split to all sales. [Act 719 section 6, section 26-51-716(b)](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf). |
| Principally telecom/internet/cable/satellite provider | Act 719 allows a separate sourcing election for tax years beginning January 1, 2026 but before December 31, 2035, made on first eligible return and requiring written permission to change; refer. |
| Consolidated, bank, insurance, exempt organization, cooperative or pass-through | Separate return/rate/apportionment rules; outside ordinary C-corporation calculation. |
| NOLs, incentive credits, bonus depreciation or federal law change | Verify Arkansas law by loss/property year; never import federal current amounts. |
| Liquidation or special franchise class | Handbook has a different base or fixed amount; do not use the ordinary stock formula automatically. |

## Worked cases

**Case 1: ordinary 2026 corporation.** Invented Arkansas-only corporation has $100,000 state net taxable income after all state adjustments and no credits. First $3,000 x 1% = $30; next $3,000 x 2% = $60; next $5,000 x 3% = $150; remaining $89,000 x 4.3% = $3,827. Total $4,067. Applying the 2027 rate early would understate the liability by $178.

```oa-check
name: AR corporate 2026 versus future rate
inputs:
  taxable: 100000
steps:
  - first: min(taxable, 3000) * 0.01
  - second: min(max(taxable - 3000, 0), 3000) * 0.02
  - third: min(max(taxable - 6000, 0), 5000) * 0.03
  - tax_2026: first + second + third + max(taxable - 11000, 0) * 0.043
  - future_tax: first + second + third + max(taxable - 11000, 0) * 0.041
  - understatement: tax_2026 - future_tax
expected:
  tax_2026: 4067
  future_tax: 3889
  understatement: 178
```

**Case 2: franchise minimum decision.** Invented ordinary stock corporation has $100,000 par-value outstanding stock, $20,000 Arkansas property and $200,000 everywhere property. Allocated stock is $10,000, producing $30 at 0.3%. The $150 minimum wins. This is separate from income tax, including in a loss year.

```oa-check
name: AR ordinary stock franchise minimum
inputs:
  par_stock: 100000
  ar_property: 20000
  everywhere_property: 200000
steps:
  - allocated_stock: par_stock * ar_property / everywhere_property
  - proportional: allocated_stock * 0.003
  - franchise: max(proportional, 150)
expected:
  allocated_stock: 10000
  proportional: 30
  franchise: 150
```

## When to refuse or refer

Refer uncertain P.L. 86-272, alternative apportionment, special industry/group filings, credit qualification, NOL/depreciation reconciliation, special franchise classifications and unresolved federal-conformity questions. A 2026 metadata tag does not establish that final 2026 forms or every branch is covered.

## Filing and payment

Ordinary AR1100CT is due the 15th day of the fourth month after year end; tax is payable by the original date even when filing is extended. The 2025-2026 filing cycle instructions accept the automatic federal extension until 30 days after the federal extended due date and describe AR1155 state-extension alternatives. Ordinary estimates are due the 15th of months 4, 6, 9 and 12 using AR1100ESCT or ATAP. [DFA pp.10-12](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf).

The booklet lists late filing and remittance penalties of 5% per month up to 35%, and 10% annual interest; AR2220 determines underestimate penalties and exceptions. These are dated 2025-2026 filing cycle instructions, not a replacement for final 2026 penalty instructions. [DFA p.12](https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf).

For franchise tax, report the preceding calendar-year condition and remit on or before May 1 under section 26-54-105(c); this is separate from the corporation income-tax due date. [Act 459 section 6](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2023R%2FPublic%2FACT459.pdf).

## Completion checklist

- Arkansas source/physical/economic nexus and federal protection separately documented.
- State income, NOL, sourcing and credits reconcile to federal schedules.
- 2026 rates used; future reduction excluded.
- Return acceptance, tax payment and separate franchise obligation documented.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DFA 2025 corporation instructions. Read for pp.4-15 and p.25 ordinary corporation coverage, 2026 Act 719 announcement, current statutory rate, state-base lines, estimates, due dates, extensions and penalties; 2025-2026 filing cycle. | https://www.dfa.arkansas.gov/wp-content/uploads/CorporationIncomeTaxInstructions_2025.pdf | 2026-11-13 |
| Act 2, 2026 special session. Read for sections 2-3 corporate rate reduction and explicit January 1 2027 start, with individual-rate neighbours. | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2FACT2.pdf | 2026-11-13 |
| Act 719 of 2025. Read for entire act for receipts definitions, nexus, allocation, single receipts factor, market sourcing, phased throwback, special election and effective date. | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT719.pdf | 2026-11-13 |
| Legislative Tax Handbook, October 2026. Read for section 8.4 ordinary stock/no-stock franchise bases, minimum, formation-year exception and special classes; section 2.1 flags future corporate top rate, which Act 2 dates to 2027. | https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf | 2026-11-13 |

| Act 459 of 2023. Read for sections 4-7 corporation/LLC definition, complete rate/base/minimum, preceding-calendar-year report and May 1 payment, authorized signature; neighbouring revocation rules read as boundaries. | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2023R%2FPublic%2FACT459.pdf | 2026-11-13 |

Not yet confirmed: final 2026 AR1100CT and instructions, 2026 state NOL/depreciation conformity and credit qualification; current franchise submission/payment fields from permitted primary hosts. Franchise filing and these base adjustments remain partial; no missing amount is extrapolated.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ar-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ar-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
