---
jurisdiction: US-SD
applicable: [IT-CORP, VAT, SC, PR, TP, XB]
not_applicable:
  IT-IND: "No ordinary state individual income tax or wage income-tax withholding."
covered_by:
  IT-CORP: sd-bank-franchise-tax
  VAT: sd-sales-tax
  SC: sd-payroll
  PR: sd-payroll
partial:
  IT-CORP: "No ordinary corporate income tax; financial institutions have bank franchise tax. Ordinary method/rates covered, specialist sourcing, final forms and transition details incomplete."
  VAT: "Ordinary sales/use covered; exact SaaS/custom contracts, agricultural product exemptions and inherited frequency/fraud claims need confirmation."
  TP: "No dedicated state transfer-pricing skill."
  XB: "Ordinary nexus/localization boundaries only; no dedicated cross-border skill."
---

# South Dakota: 2026 tax skills

South Dakota has no ordinary individual or corporate income tax. It taxes retail products and many services through sales/use tax, with municipal additions. Financial institutions can owe bank franchise tax, and covered employers pay reemployment assistance and separate fees. No income-tax withholding does not eliminate employer payroll obligations.

| Job | covered_by | Coverage |
| --- | --- | --- |
| Individual income tax | Not applicable | Federal taxes remain separate |
| Sales/use and municipal gross receipts | `sd-sales-tax` | Ordinary 4.2% state sales/use, municipal rates, current dollar-only nexus, sourcing, EPath and preserved old topics/cases with corrections and explicit gaps |
| Corporate/franchise | `sd-bank-franchise-tax` | No ordinary corporate income tax; partial specialized financial-institution computation with current rates/minimum/base and filing framework |
| Payroll withholding and UI | `sd-payroll` | No state income-tax withholding; 2026 employer RA, wage base, new/construction and experience fees, Form 21 and payments |

All three skills are **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. Load relevant federal skills for federal income and payroll, and `us-sales-tax` before the state sales skill. Preserve each separate tax's base, code and due date.

Construction contractor excise, agricultural machinery excise, tourism/telecom, insurance, trust-special taxes, property and motor fuel remain separate regimes. Inherited construction/agricultural sales examples are retained as corrected boundaries, not expanded into full specialist computations. No separate ordinary sales skill duplicates `sd-sales-tax`.

Official sources read 2026-11-13: [DOR July 2026 sales publication](https://dor.sd.gov/media/avyep2sr/2026-7_sales-use-tax-guide.pdf), [DOR bank franchise](https://dor.sd.gov/businesses/taxes/bank-franchise-tax/), [DLR employer RA](https://dlr.sd.gov/ra/businesses/default.aspx) and the current Legislature provisions listed in each skill. Final Not yet confirmed lines identify the unresolved rules; 2026 metadata is not accountant approval.
