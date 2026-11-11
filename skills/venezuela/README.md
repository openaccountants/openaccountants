---
jurisdiction: VE
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  VAT: venezuela-iva
  TP: venezuela-transfer-pricing
  XB: venezuela-cross-border-tax
partial:
  TP: "Current filing instructions, accepted range administration and current jurisdiction lists remain unconfirmed."
  XB: "Current administrative return and withholding instructions remain unconfirmed; ordinary company calculations use the merged corporate owner."
  IT-IND: "2026 resident and specified nonresident computations covered; current UT currency value, employment-bonus interpretation and administrative instructions not yet confirmed."
  IT-CORP: "2026 ordinary statutory computation covered; current UT currency value and filing/advance instructions not yet confirmed."
  VAT: "Ordinary IVA computation is sourced; current ordinary filing deadline/form mapping and operative withholding administration remain unconfirmed from primary text."
  SC: "2026 INCES computation and IVSS/LOPCYMAT statutory framework covered; current IVSS, RPE, FAOV and pensions-protection inputs remain unconfirmed."
  PR: "Existing skill remains on tax year 2025."
---

# Venezuela: tax pack

This map is maintained with the country pack. Coverage includes only Guides on main; pending work is identified separately.

Tax years: 2025 (1 skill), 2026 (7 skills).

| Tax | Skill | Tax year | Status |
|---|---|---|---|
| Income tax | [Individual income tax](venezuela-income-tax.md) | 2026 | Partial: currency, employment interpretation and filing inputs unconfirmed |
| Company tax | [Corporate tax](venezuela-corporate-tax.md) | 2026 | Partial: UT currency value and filing instructions unconfirmed |
| VAT or sales tax | [IVA](venezuela-iva.md) | 2026 | Partial: current filing and withholding administration unconfirmed |
| Social contributions | [Social contributions](venezuela-social-contributions.md) | 2026 | Partial: current ordinary IVSS, RPE, FAOV and pension inputs unconfirmed |
| Payroll | [Payroll](venezuela-payroll.md) | 2025 | Needs updating |
| Transfer pricing | [Transfer pricing](venezuela-transfer-pricing.md) | 2026 | Partial: current filing and range administration unconfirmed |
| Cross-border | [Cross-border tax](venezuela-cross-border-tax.md) | 2026 | Partial: current filing and withholding instructions unconfirmed |

Ready means the skill is on the current tax year. It does not mean an accountant has reviewed it. Missing means we have no skill yet; nobody has checked yet that the tax applies here.

## What still needs doing

- Income tax: confirm current primary UT currency value, employment-base interpretation and filing/withholding instructions.
- Confirm the current UT currency value, filing calendar and implementing instructions for [Corporate tax](venezuela-corporate-tax.md).
- IVA: confirm the current ordinary filing deadline, portal field mapping and operative withholding administration.
- Social contributions: confirm current IVSS/RPE/FAOV and pensions-protection parameters, actual LOPCYMAT implementation/assessment, and current currency/calendar inputs.
- Payroll: bring [Payroll](venezuela-payroll.md) up to the current tax year.
- Transfer pricing: confirm current filing instructions, range administration and jurisdiction lists.
- Cross-border: confirm current return and withholding instructions before a live filing.

Tracked in [\[VE\] Complete the pack](https://github.com/openaccountants/openaccountants/issues/373).

## Other skills

- [Tax optimization](venezuela-tax-optimization.md) (2026): statutory ISLR planning decisions; current administrative, treaty, incentive, municipal, IVA and employment inputs remain explicitly unconfirmed. This does not make the country pack comprehensive.

## Pending work

[Payroll PR #1470](https://github.com/openaccountants/openaccountants/pull/1470) awaits Jose Padilla’s approval of the revised text. It is not counted as main-branch coverage. The current payroll Guide remains on 2025.

## Out of scope

Specialist financial and extractive-sector computations, sector exonerations, treaty-rate tables, low-tax-jurisdiction investment calculations, shareholder/branch distribution computations and complex reorganizations require separate primary-source work.
