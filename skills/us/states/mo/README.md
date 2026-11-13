---
jurisdiction: US-MO
applicable: [IT-IND, IT-CORP, VAT, SC, PR, XB]
not_applicable:
  TP: "No separate state documentation pack; corporate nexus, groups and related-party issues route to the corporate skill."
covered_by:
  IT-IND: mo-income-tax
  IT-CORP: mo-corporate-tax
  VAT: mo-sales-tax
  SC: mo-payroll
  PR: mo-payroll
  XB: mo-income-tax
partial:
  IT-IND: "Published 2026 rates and estimates; final annual forms and full pension, property/other credits, military and nonresident calculations pending."
  IT-CORP: "Core MO-1120, federal liability deduction, receipts apportionment and 2026 estimates; final annual forms, full PTE/owner/composite and special group/industry cases pending."
  VAT: "Core sales/use, food/software rules and nexus; actual local rates, accelerated filings, exact 2,000 consumer-use boundary and specialized transactions pending."
  SC: "2026 UI base/new rates, coverage, registration and quarterly CW reporting; detailed exemptions/reimbursement/successor cases, continuing delinquency and actual UI interest pending."
  PR: "2026 withholding, MO-941, statements and core wage administration; current city filings/refunds, full special cases, 1099 specifications and detailed labour rules pending."
  XB: "Resident credit/nonresident routing and remote-work boundaries; complete multistate, military, transport, city and international cases pending."
---

# Missouri: 2026 state tax pack

Missouri imposes individual income tax, corporate income tax, sales/use tax with local additions, employer income-tax withholding and unemployment insurance. Ordinary corporation franchise tax was phased out from 2016; this does not exempt banks, insurance or local business taxes. Kansas City and St. Louis city earnings/profits tax work is a separate, explicitly partial scope.

| Job | One owning skill | Status |
| --- | --- | --- |
| Individual income tax | `mo-income-tax` | Writer source checks complete; partial above |
| Corporate income / ordinary franchise tax status | `mo-corporate-tax` | New core owner; partial above |
| Sales and use tax | `mo-sales-tax` | Writer source checks complete; partial above |
| Payroll withholding and UI | `mo-payroll` | Writer source checks complete; partial above |

Published 2026 employer formulas, individual/corporate estimates, UI rates and current law are used. Annual return mechanics retained from final 2025 forms are labelled **2025-2026 filing cycle**; unpublished 2026 annual line mappings are not guessed. Currency: USD. Federal figures remain with their federal skills.

Official sources read 2026-11-13: [DOR](https://dor.mo.gov/), [DES](https://labor.mo.gov/des/employers/tax-rates), [DOLIR](https://labor.mo.gov/dls/minimum-wage), [Revisor](https://revisor.mo.gov/main/OneSection.aspx?section=143.121). Each skill records exact source scope and unconfirmed items. Independent review remains pending.

The pack does not compute estate/inheritance tax, county property tax, full MO-PTS/MO-PTC credits, elected PTE/partnership/S corporation owner returns, specialist sector taxes or complete city earnings/profits returns. The former blanket assertion that corporate income tax was missing is resolved by the new corporate skill; existing slugs and licence strings are preserved. No person attribution is changed.
