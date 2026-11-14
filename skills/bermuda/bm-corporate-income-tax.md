---
name: bm-corporate-income-tax
description: >
  Bermuda corporate income tax under the Corporate Income Tax Act 2023 for fiscal years
  beginning on or after 1 January 2025, including fiscal year 2026. Covers who is in scope
  (Bermuda constituent entities of multinational groups with EUR 750 million revenue in two
  of the four preceding years), excluded entities, the 15% charge less foreign tax credits,
  the 80% loss carryforward limit, the de minimis election, the economic transition
  adjustment, transfer pricing, instalments, CITA Online returns and civil penalties.
  Trigger phrases include Bermuda CIT, Bermuda Pillar Two, CITA, Bermuda constituent
  entity group, Bermuda 15% tax, Form S-101.
version: "1.0"
jurisdiction: BM
tax_year: 2026
tax_year_notes: "Fiscal years beginning on or after 1 January 2025; 2026 fiscal years"
last_updated: 2026-11-14
category: international
type: computation
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Bermuda corporate income tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Bermuda charges corporate income tax (CIT) only on Bermuda Constituent Entity Groups of In Scope MNE Groups. It is administered by the Corporate Income Tax Agency (CITA). Every other Bermuda company, partnership and individual pays no tax on profits, income, dividends or capital gains: that answer belongs to [bermuda-tax](bermuda-tax.md). Payroll tax on staff is separate and owned by [bm-payroll-social](bm-payroll-social.md).

The Act applies to fiscal years beginning on or after 1 January 2025. This skill covers the fiscal years that end in 2026 (years of assessment 2026) and calendar 2026. CIT liability applies even where an assurance was given under the Exempted Undertakings Tax Protection Act 1966 ([CIT Act 2023 s.4(4)](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)).

This is the full computation only at the level of the statute's charging rules. The Act follows the OECD GloBE model and its detailed income adjustments (Parts 5 and 6) run to many sections; this skill gives the order of work and the figures, and refers the detailed adjustments out.

## Ask the client first

1. Group consolidated revenue in each of the four fiscal years before the year in question (EUR 750 million test).
2. Which entities are Bermuda tax resident entities or Bermuda permanent establishments, and whether any is an excluded entity (governmental, international organisation, non-profit, pension fund, investment fund or real estate vehicle that is the ultimate parent, and 95% or 85% owned subsidiaries of these).
3. Fiscal year end (sets the instalment and return dates).
4. Aggregate Bermuda revenue and net taxable income or loss for the current and two preceding years (de minimis test).
5. Opening tax loss carryforward and creditable foreign taxes allocated to the Bermuda entities.
6. Whether any intercompany transaction with another jurisdiction is not at arm's length, and whether international shipping income is claimed as excluded.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure and conditions | Official source |
|---|---|---|
| CIT rate | 15% of the net taxable income of the Bermuda Constituent Entity Group, less foreign tax credits | [CIT Act 2023 s.4(2)](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| In Scope MNE Group | Annual revenue of EUR 750 million or more in the consolidated financial statements of the ultimate parent in at least two of the four fiscal years immediately before the fiscal year; merger and demerger rules in s.11(2) to (6) | [CIT Act 2023 s.11](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| Tax loss carryforward deduction cap | 80% of the positive amount of taxable income less taxable losses for the year, unless otherwise prescribed | [CIT Act 2023 s.6(1)(a)](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| De minimis election, revenue test | Average revenue of all Bermuda Constituent Entities of the group, current and two preceding fiscal years, less than EUR 10 million | [CIT Act 2023 s.7](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| De minimis election, income test | Average net taxable income a loss or less than EUR 1 million; if both tests are met and elected, tax is deemed zero for the year | same |
| Economic transition adjustment, intangibles | 10% a year, for the first ten fiscal years beginning on or after 1 January 2025, of the 30 September 2023 fair value less carrying value of identifiable intangibles | [CIT Act 2023 s.33(3)](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| Penalty, failure to register | Up to USD 10,000 | [CIT Act 2023 s.46C](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| Penalty, late return, months 1 to 5 | Greater of USD 3,000 a month or 5% a month of the tax due at the due date | [CIT Act 2023 s.46D(2)](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| Penalty, late return, month 6 onward | USD 3,000 a month | same |
| Penalty, late information or documentation (not a return) | USD 3,000 a month | same |
| Penalty, understatement from negligence, disregard or substantial understatement | Up to 20% of the understatement; substantial means more than the lesser of 20% of the correct tax or USD 10,000,000 | [CIT Act 2023 s.46E](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| Penalty, failure to pay tax when due | 0.5% of the tax due at the date of the failure, for each month it continues, recalculated after part payments | [CIT Act 2023 s.46F](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| Fiscal year ending 31 December 2026: instalments, return and final payment | Instalment 1 due 31 August 2026; instalment 2 due 15 December 2026; return and final payment due 1 November 2027 | [CITA filing and payment deadlines, 5 June 2026](https://www.cita.bm/assets/images/files/Filing%20%26%20Payment%20Deadlines%2005.06.2026.pdf) |
| Fiscal year ending 31 March 2026 | Instalment 1 due 1 December 2025; instalment 2 due 16 March 2026; return and final payment due 1 February 2027 | same |
| Fiscal year ending 30 June 2026 | Instalment 1 due 2 March 2026; instalment 2 due 16 June 2026; return and final payment due 30 April 2027 | same |
| Fiscal year ending 30 September 2026 | Instalment 1 due 1 June 2026; instalment 2 due 15 September 2026; return and final payment due 2 August 2027 | same |
| Fiscal year ending 31 December 2025 (first year) | Return and final payment due 2 November 2026 | same |

### Steps

1. **Scope.** Test the EUR 750 million revenue threshold on the ultimate parent's consolidated statements for two of the four preceding years (s.11). Excluded entities' consolidated revenue counts towards the threshold even though they are not taxed (s.11(7)).
2. **Identify the Bermuda Constituent Entities** and group them into Bermuda Constituent Entity Groups (ss.8 and 9). Remove excluded entities (s.10); an otherwise excluded entity may elect into tax, a five-year election.
3. **Taxable income or loss per entity.** Start from financial accounting net income or loss (s.21) and make the Act's adjustments, including the economic transition adjustment for entities in the group in their first fiscal year beginning on or after 1 January 2025 (s.33), the transfer pricing adjustments (s.37) and, where its conditions are met, the international shipping exclusion (strategic or commercial management of the ships effectively carried on from or within Bermuda).
4. **Net taxable income of the group** (s.5): add taxable income and subtract taxable losses of all entities in the group, then subtract the tax loss carryforward deduction, capped at 80% of that positive amount (s.6(1)(a)). The filing entity may elect to use less of the carryforward.
5. **Gross tax:** 15% of net taxable income (s.4(2)(a)).
6. **Foreign tax credits:** subtract the allocated creditable foreign taxes; the credit cannot exceed the gross tax or be less than zero (s.16).
7. **De minimis:** if the s.7 tests are met, the filing entity may elect, each year, to treat the tax as zero. The election must be made for every Bermuda Constituent Entity Group in the same MNE group (except groups made up only of stateless entities or investment entities).
8. **Joint liability:** every Bermuda Constituent Entity of the In Scope MNE Group is jointly and severally liable for the tax of any Bermuda Constituent Entity Group in the same MNE group (s.4(3)).
9. **Pay instalments and file** (see Filing and payment). Tax is converted into US dollars under s.47.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Bermuda company whose group revenue is under EUR 750 million | No CIT; no tax on profits | [CIT Act 2023 s.11](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) |
| Investment fund or real estate investment vehicle that is the ultimate parent | Excluded entity | CIT Act 2023 s.10(1) |
| Subsidiary at least 95% owned by excluded entities that only holds assets or invests for them, or carries on ancillary activities | Excluded entity (not a pension services entity owner) | CIT Act 2023 s.10(2)(a) |
| Subsidiary at least 85% owned by excluded entities with substantially all income being excluded dividends or equity gains | Excluded entity | CIT Act 2023 s.10(2)(b) |
| Transaction with a group entity in another jurisdiction not at arm's length | Adjust to arm's length; two group entities recording different amounts must be aligned | CIT Act 2023 s.37 |
| Branch of a Bermuda entity abroad | A branch exemption election is available under the Act; conditions not set out here | CIT Act 2023 s.2 definition |
| Old statements that Bermuda guarantees no tax until 2035 | Wrong for in-scope groups: CIT applies notwithstanding any assurance under the Exempted Undertakings Tax Protection Act 1966 | CIT Act 2023 s.4(4) |
| Tax Credits Act 2025 benefits | Reduce adjusted tax payments; the return for tax credit benefits is due on the CIT return date | [CITA filing and payment deadlines](https://www.cita.bm/assets/images/files/Filing%20%26%20Payment%20Deadlines%2005.06.2026.pdf) |

## Worked cases

### Case 1: group with losses brought forward and foreign tax credits

A Bermuda Constituent Entity Group has taxable income less taxable losses of USD 100,000,000 for fiscal 2026, a loss carryforward of 30,000,000 and allocated creditable foreign taxes of 2,000,000. The cap is 80% of 100,000,000 = 80,000,000, so the full 30,000,000 is deductible. Net taxable income 70,000,000; tax at 15% 10,500,000; less credits 2,000,000; CIT 8,500,000.

```oa-check
name: Bermuda CIT with loss carryforward and foreign tax credit, fiscal 2026
inputs:
  positive_amount: 100000000
  loss_carryforward: 30000000
  foreign_tax_credit: 2000000
steps:
  - cap: positive_amount * 0.80
  - loss_deduction: min(loss_carryforward, cap)
  - net_taxable_income: positive_amount - loss_deduction
  - gross_tax: net_taxable_income * 0.15
  - credit_used: clamp(foreign_tax_credit, 0, gross_tax)
  - cit: gross_tax - credit_used
expected:
  cap: 80000000
  net_taxable_income: 70000000
  gross_tax: 10500000
  cit: 8500000
```

### Case 2 (decision): make the de minimis election or not

The Bermuda entities of an in-scope group had revenue of EUR 8, 9 and 10 million and net taxable income of EUR 0.7, 1.1 and 0.9 million over the two preceding and the current fiscal year. Averages are EUR 9 million (below 10) and EUR 0.9 million (below 1). Both tests pass, so the election deems tax of EUR 135,000 (15% of 0.9 million) to be zero. If current-year revenue had been EUR 13 million, average revenue would be 10 million, not less than 10 million, and no election would be available.

```oa-check
name: Bermuda CIT de minimis test, three-year averages
inputs:
  rev_2: 8000000
  rev_1: 9000000
  rev_0: 10000000
  nti_2: 700000
  nti_1: 1100000
  nti_0: 900000
  rev_0_alt: 13000000
steps:
  - avg_revenue: (rev_2 + rev_1 + rev_0) / 3
  - avg_nti: (nti_2 + nti_1 + nti_0) / 3
  - revenue_headroom: 10000000 - avg_revenue
  - income_headroom: 1000000 - avg_nti
  - tax_without_election: nti_0 * 0.15
  - avg_revenue_alt: (rev_2 + rev_1 + rev_0_alt) / 3
  - alt_headroom: 10000000 - avg_revenue_alt
expected:
  avg_revenue: 9000000
  avg_nti: 900000
  revenue_headroom: 1000000
  income_headroom: 100000
  tax_without_election: 135000
  alt_headroom: 0
```

A headroom above zero on both tests means the election is open; zero or below means it is not.

## When to refuse or refer

- The detailed adjustments in Parts 5 and 6 (financial accounting income adjustments, stateless entities, insurance, investment entities, the shipping exclusion), the branch exemption election and the opening tax loss carryforward schedules: refer to a Bermuda CIT adviser with the Form I-101 and I-103 instructions.
- Tax Credits Act 2025 benefit computations: not covered.
- Whether the group's Bermuda CIT is a qualified domestic minimum top-up tax for another country's Pillar Two rules: refer; this skill does not cover foreign GloBE rules.
- A company outside an in-scope group asking how much CIT it owes: none; do not compute.

## Filing and payment

1. **Register** each Bermuda Constituent Entity for tax as the Act and the CIT Agency Act require; failure without reasonable excuse carries a penalty up to USD 10,000 (s.46C). At incorporation, companies already tell the Registrar whether they will be a Bermuda Constituent Entity (Companies Act s.5B) ([Limited companies](https://www.gov.bm/limited-companies)).
2. **Instalments:** two a year, with Form 001 (2025 only, a web form) or the instalment form in CITA Online for fiscal 2026 onward. Dates follow the fiscal year end (table above). Interest is charged on underpaid or unpaid instalments under regulations (s.46A).
3. **Return:** file the CIT Online Return (Form 100) in CITA Online at online.cita.bm, and upload the Standard CIT Return Schedules (Form S-101, instructions I-101) or, where the de minimis election is made and the group qualifies, the Simplified Schedules (Form S-102, instructions I-102). Add Form S-103 for opening tax loss carryforward and S-104 for creditable foreign tax allocation where relevant ([CITA, CIT return](https://www.cita.bm/corporate-income-tax-return1)).
4. **Final payment** is due with the return. Late filing and late payment penalties and interest may be applied in CITA Online after the 2 November 2026 deadline for fiscal 2025.
5. Help: support@cita.bm, +1 441 543 8660.

## Completion checklist

- Revenue threshold tested on four preceding years, with merger or demerger adjustments.
- Excluded entities removed; elections into tax recorded.
- Economic transition adjustment applied for entities present on 30 September 2023.
- Loss carryforward capped at 80%.
- Foreign tax credit limited to gross tax.
- De minimis election tested and, if used, made for all groups in the MNE.
- Instalment dates for the fiscal year end diarised; return and schedules uploaded.

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Act 2023 as amended to 2026 (CITA copy): read ss.4 to 7, 10, 11, 16, 33, 37 and 46A to 46F for the charge, rate, threshold, losses, de minimis, excluded entities, credits, transition adjustment, transfer pricing and penalties | https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf | 2026-11-14 |
| CITA, filing and payment deadlines (PDF, last published 5 June 2026): read for instalment, return and final payment dates by fiscal year end | https://www.cita.bm/assets/images/files/Filing%20%26%20Payment%20Deadlines%2005.06.2026.pdf | 2026-11-14 |
| CITA, corporate income tax return page: read for Form 100, S-101 to S-104, guidance notes and the penalty reminder | https://www.cita.bm/corporate-income-tax-return1 | 2026-11-14 |
| Government of Bermuda, corporate income tax page: read for the 1 January 2025 start and the move of CIT content to cita.bm | https://www.gov.bm/articles/cit | 2026-11-14 |
| Government of Bermuda, limited companies: read for the s.5B declaration on incorporation | https://www.gov.bm/limited-companies | 2026-11-14 |

Not yet confirmed: the interest rate on late tax and instalments (set by regulations under s.52, not opened); the instalment amounts (set by the administrative regulations, not opened); the conditions of the branch exemption election; the old file's statement that entities less than 80% owned by the ultimate parent are out of scope (no section found that says so; removed).
