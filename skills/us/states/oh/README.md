---
jurisdiction: US-OH
applicable: [IT-IND, IT-CORP, VAT, SC, PR]
not_applicable:
  TP: no Ohio transfer pricing documentation regime; related-party rules sit in the federal skills
  XB: residency, contact periods and the reciprocity states are in oh-income-tax
covered_by:
  SC: oh-payroll
  PR: oh-payroll
partial:
  IT-CORP: "Commercial Activity Tax skills (oh-cat-tax, oh-cat) are being rewritten for 2026 in a separate change"
  VAT: "sales and use tax skills (oh-sales-tax, ohio-sales-tax) are being rewritten for 2026 in a separate change"
  IT-IND: "2026 IT 1040 instructions not yet published: per-person exemption amounts and credit limits not yet confirmed"
---

# Ohio (US-OH): tax pack

Calendar tax year for individuals. Authorities: the Ohio Department of Taxation (tax.ohio.gov) for income tax, withholding, sales tax and the Commercial Activity Tax, and the Ohio Department of Job and Family Services (jfs.ohio.gov) for unemployment insurance. Currency: US dollars. From tax year 2026 Ohio taxes nonbusiness income at a single rate: nothing up to $26,050, then $332.00 plus 2.75% of the excess (R.C. 5747.02(A)(3)(c), HB 96); business income gets a $250,000 deduction and a flat 3% rate on the rest. Ohio has no corporate income tax: businesses pay the Commercial Activity Tax (CAT) on gross receipts instead. A US state: federal income tax, FICA and FUTA sit on top of every domain here.

**Local income taxes.** Most Ohio cities and villages levy their own municipal income tax (R.C. Chapter 718), and some school districts levy a school district income tax. Municipal tax is not computed in this pack: a cross-state local income tax skill covers it. School district tax is pointed to, not computed, in `oh-income-tax` and `oh-payroll`.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | oh-income-tax | sourced from the law (2026 rate from R.C. 5747.02; partial) |
| IT-CORP, Commercial Activity Tax (gross receipts) | oh-cat-tax, oh-cat | being rewritten in a separate change |
| VAT / sales and use tax | oh-sales-tax, ohio-sales-tax | being rewritten in a separate change |
| SC, social contributions (unemployment insurance) | oh-payroll | sourced from ODJFS 2026 rates |
| PR, payroll withholding | oh-payroll | sourced from the Department's 2025 and 2026 withholding tables |
| TP, transfer pricing | not applicable, see above | |
| XB, cross-border | not applicable as a separate skill, see above | |

Out of scope for this pack: municipal income tax (see above); property tax (county level); the pass-through entity tax and composite returns (IT 4738, IT 4708); workers' compensation (Ohio Bureau of Workers' Compensation).

## Official sources

- R.C. 5747.02 (individual rates, 2025 and 2026): https://codes.ohio.gov/ohio-revised-code/section-5747.02 (read 2026-11-13)
- R.C. 5747.025 (personal exemptions, $500,000 cut-off from 2026): https://codes.ohio.gov/ohio-revised-code/section-5747.025 (read 2026-11-13)
- 2026 Ohio IT 1040ES worksheet and instructions: https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf (read 2026-11-13)
- 2025 Ohio IT 1040 instructions: https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf (read 2026-11-13)
- Department of Taxation, employer withholding: https://tax.ohio.gov/business/employer-withholding (read 2026-11-13)
- ODJFS, contribution rates 2023 to 2026: https://jfs.ohio.gov/page/CAJM.hl56rs7cilxWeGzd (read 2026-11-13)
- ODJFS, 2026 Rate Details: https://dam.assets.ohio.gov/image/upload/jfs.ohio.gov/ouio/uctax/2026RateDetails.pdf (read 2026-11-13)
