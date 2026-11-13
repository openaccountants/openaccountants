---
jurisdiction: US-NH
applicable: [IT-CORP, SC, PR]
not_applicable:
  IT-IND: "No broad personal wage tax; Interest & Dividends Tax repealed for taxable periods beginning after December 31, 2024. Private-investment capital gains have no separate personal state tax; business-asset gains can enter BPT."
  VAT: "No general sales tax; selective meals/rentals and other excises remain separate jobs."
  TP: "No separate state transfer-pricing documentation skill; related/unitary entity issues remain in the business-tax analysis."
  XB: "No standalone cross-border skill in this pack; business apportionment and interstate payroll boundaries are in their owner skills."
covered_by:
  IT-CORP: nh-bpt-bet
  SC: nh-payroll
  PR: nh-payroll
partial:
  IT-CORP: "2026 statutory rates and filing tests verified; published form mappings remain the 2025-2026 filing cycle. Full NOL percentage limits and special group/credit computations are not established."
  PR: "Ordinary UI and absence of NH wage withholding covered; current bulk-upload specification and 2026-specific confirmation of handbook online-filing grace remain unconfirmed."
---

# New Hampshire: 2026 tax pack

New Hampshire has no general personal wage tax or general sales tax. Its Interest & Dividends Tax was repealed for periods **beginning** after December 31, 2024; a fiscal period beginning before repeal is not exempt merely because it ended in 2025. The personal repeal does not exempt business income, sole proprietors or federal disregarded LLCs from the separate BPT/BET tests. Business-asset gains can enter BPT even though private-investment capital gains do not create a separate personal capital-gains return.

Currency is USD. DRA administers business taxes through Granite Tax Connect; NH Employment Security administers employer UI through its employer registration and WebTax systems. This pack preserves every existing slug. No accountant has approved these skills.

## Domains

| Job | Owner skill | Status |
|---|---|---|
| Individual income tax / repeal routing | `nh-interest-dividends-note` | checked against the law; personal wage tax absent and I&D repealed |
| General sales/use tax | Not applicable | DRA identifies no general sales tax; selective taxes outside this pack |
| Corporate and other business income / enterprise tax | `nh-bpt-bet` | checked against the law; partial items disclosed above |
| State wage withholding and employer UI | `nh-payroll` | checked against the law; no NH wage withholding, UI still applies |

The BPT/BET skill covers proprietors, partnerships, S/C corporations and separate SMLLCs. It corrects the old README's statement that sole proprietors have no business tax and its obsolete BPT figure. Federal payroll and corporate figures stay in `us-form-941-940-payroll` and `us-form-1120-c-corp`.

Out of scope: selective meals/rentals, real estate transfer, communications, tobacco/beer/fuel/electricity and utility-property taxes, municipal property tax, detailed special-entity elections and foreign/group calculations. These are exclusions from this pack's jobs, not claims that the taxes do not exist.

## Official sources

| Source | What was read | Read on |
|---|---|---|
| [RSA chapter 77](https://gc.nh.gov/rsa/html/V/77/77-mrg.htm) and [DRA I&D FAQs](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) | Read for repeal beginning-date rule and historical return boundary | 2026-11-13 |
| [DRA Business Taxes](https://www.revenue.nh.gov/taxes-glance/business-taxes) and [RSA 77-A:1](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm) | Read for business filing tests, separate entities and business-asset gains | 2026-11-13 |
| [NHES employer taxes](https://www.nhes.nh.gov/employers/employer-claims-taxes) and [2026 rate chart](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-chart) | Read for UI base, quarterly adjustments and new-account computation | 2026-11-13 |

The DRA no-general-sales-tax FAQ is [here](https://www.revenue.nh.gov/faq/does-new-hampshire-have-sales-tax). Direct and ordinary browser retrieval of that page was blocked in this pass; the classification is retained from the existing pack and is not labelled as a new full-page verification. All rates and computations used in the skills have separately read sources.
