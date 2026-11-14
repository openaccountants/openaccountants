---
jurisdiction: US-AK
applicable: [IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  IT-CORP: ak-corporate-tax
  VAT: ak-sales-tax
  SC: ak-payroll
  PR: ak-payroll
not_applicable:
  IT-IND: "No Alaska individual income tax; federal income tax remains separate."
partial:
  TP: "No dedicated state transfer-pricing skill; specialized related-party analysis remains separate."
  XB: "Ordinary nexus and wage-localization boundaries only; no dedicated cross-border skill."
  VAT: "Local only. Remote sellers through ARSSTC are covered from the Uniform Code and the 11/1/2026 rate sheet; physical-presence sellers and non-member codes need the municipality's own code."
  IT-CORP: "Ordinary computation covered using current program plus explicitly labelled 2025-2026 filing-cycle instructions; final 2026 forms/later law unconfirmed."
  PR: "Ordinary 2026 UI covered; employer's notice and special coverage/elections need case facts. Income-tax wage withholding is not applicable."
---

# Alaska tax skills, 2026

**Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant.

Alaska has no individual income tax or income-tax employee withholding. It has corporate income tax and state unemployment contributions, including an employee share. Sales/use tax is **local only**, with no statewide sales tax. [DOR individual tax](https://tax.alaska.gov/programs/programs/index.aspx?10001); [DOR corporate overview](https://tax.alaska.gov/programs/programs/reports/Historical.aspx?60380); [DCRA local sales/use explanation](https://www.commerce.alaska.gov/web/dcra/localgovernmentresourcedesk/taxationassessment/salestax.aspx).

| Job | Owner | Coverage and limits |
| --- | --- | --- |
| Individual income tax | Not applicable | No Alaska individual return; use relevant federal skills for federal income and PFD questions |
| Sales/use tax | `ak-sales-tax.md` | 2026 local-only sales tax: ARSSTC USD 100,000 remote-seller test, sourcing, member rates, seasonal rates and caps (11/1/2026 sheet, Juneau cap change of October 2026), filing and penalties; physical-presence sellers and non-member codes are partial |
| Corporate income tax | `ak-corporate-tax.md` | Ordinary graduated tax, state base/group/factor method and filing/payment workflow; final 2026 forms and later law are unconfirmed; 2025 instructions expressly labelled 2025-2026 filing cycle |
| Payroll withholding and UI | `ak-payroll.md` | No income-tax withholding; 2026 employee/employer UI, coverage, wage base and TQ01; actual employer notice and special coverage must be established |

Load only the relevant skills and their stated dependencies. `ak-sales-tax` requires `us-sales-tax`. Federal wages, self-employment and corporate computations remain with the relevant federal skills, including `us-form-941-940-payroll` and `us-form-1120-c-corp`.

The local-sales skill was rewritten on 2026-11-14 from the ARSSTC Uniform Code, the ARSSTC seller pages, the ARSSTC rate sheet as of 11/1/2026 and the Juneau code. DCRA corroborates the local-only structure; it does not publish local rates.

Not yet confirmed: every municipality's current rate, caps, use-tax and remote-seller details; final 2026 corporate forms/conformity and specialized additional corporate taxes; each employer's rate notice and special UI coverage. Oil/gas production, fishing/mining license, property, workers' compensation and specialized industry computations are outside this ordinary pack. Sales and corporate coverage are partial, not complete statewide filing approval.
