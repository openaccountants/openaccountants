---
name: bd-return-assembly
description: "Assemble the 2026 Bangladesh resident individual filing package from reviewed income, VAT, pension and withholding working papers; keep filing, payment and export-incentive claims separate."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bd-return-assembly"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bangladesh self-employed return assembly v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Capstone for resident freelancers and sole proprietors. It assembles working papers and a submission checklist; it does not calculate tax or submit through the taxpayer portal.

## Ask the client first

- Confirmed intake, periods and legal entity.
- Reviewed exempt/taxable income schedules, investments, withholding certificates and payments.
- BIN/enlistment status, VAT working papers and prior credit.
- Remittance/encashment certificates and any separately evidenced incentive claim.

## The method, step by step

1. Load [intake](bd-freelance-intake.md), [freelancer relief](bd-it-freelancer-tax.md) and [PIT](bangladesh-pit.md). Apply relief to qualifying income and disclose it in the return. Never treat the old assumed expiry as a charging rule.
2. Reconcile invoices/platform statements to remittance certificates and banks. Keep domestic business receipts separate. Match each withholding credit to its certificate; unresolved amounts remain on the reviewer exception list.
3. Bring in [VAT](bangladesh-vat.md) if registered/enlisted or potentially liable, and [social contributions](bd-social-contributions.md). A solo trader's drawings are not employee payroll. Apply the investment-rebate restrictions in the PIT working paper before assembly.
4. Select the filing window and any timing adjustment from PIT using current section 170 (https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html). Do not substitute the old Tax Day deadline or location-based minimum tax. Apply filing obligations under section 166 (https://bdlaws.minlaw.gov.bd/act-1429/section-51996.html) even if qualifying freelance income is exempt.
5. Present the individual return at https://etaxnbr.gov.bd, with the income, exempt-income, assets/liabilities, expenditure, tax/rebate and payment schedules applicable to that person. Validate identity, period and balances before submission; retain the final return, payment challan/reference and acknowledgement after the taxpayer or authorized practitioner files.
6. Track VAT submission separately from income tax. Track any export cash-incentive application through the bank as a separate claim; do not net an unapproved incentive against tax.

Completion checklist: export receipts matched; domestic profit supported; relief eligibility documented; investments checked; source credits reconciled; statutory minimum tax considered in PIT; VAT obligations handled; current filing window selected; payment and acknowledgement retained.

## When to refuse or refer

Do not mark a return filed until the acknowledgement exists. Do not claim a missing credit, automatic investment rebate, refund or incentive. Refer unresolved residence, overseas structures, sector incentives and disputed bank deductions.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for return filing obligations and exceptions, section 166 | https://bdlaws.minlaw.gov.bd/act-1429/section-51996.html | 2026-11-14 |
| Read for current filing windows, special first-filer/overseas cases, corporate deadline and holiday rule, section 170 | https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html | 2026-11-14 |
| Read for investment-rebate formula and excluded income, section 78 | https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html | 2026-11-14 |

Not yet confirmed: Live portal field labels and the taxpayer-specific submission/payment confirmation have not been tested here; bank export-incentive rate and claim deadline require the applicable current circular.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bd-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bd-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
