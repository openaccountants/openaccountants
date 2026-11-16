---
name: ws-tax-overview
description: "Samoa tax overview for 2026: source-cited rules, conditions, filing boundaries and recomputing cases. Not yet approved by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ws-tax-overview"
  jurisdiction: "WS"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Samoa Tax Overview v0.1

> **General reference only.** This skill supports AI-assisted working papers. It is not approval to file, pay or take a tax position for a particular person. Obtain qualified local review of the facts, applicable law and filing instructions.

## The method, step by step

Use this pack for the Independent State of Samoa (WS), not American Samoa. Work in Samoan tala: WST, also shown locally as SAT or $. The Ministry now styles its public site Ministry of Revenue; older Acts/pages use Ministry of Customs and Revenue. Tax intake/returns belong to its Inland Revenue services. The default tax year is calendar year, with approved company substituted-year rules. [Tax Due Dates and footnote](https://revenue.gov.ws/inland-revenue-services/); [section 2, tax year](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 34](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

First classify the person and income: individual or company, residence and source, ordinary taxable income versus wages, exempt amounts or final gross withholding. Residents generally bring worldwide assessable income into scope; non-residents bring Samoa-source income. Then load the owner skill below; do not combine unrelated thresholds. [section 2, resident company](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 6](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 14](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 10](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

- [Personal income tax](ws-income-tax.md) owns annual individual bands, the tax-free threshold, home/day-count residence rules and mixed wage/business computation.
- [Corporate income tax](ws-corporate-income-tax.md) owns ordinary resident/non-resident company tax, withholding classification, annual returns/payment and provisional tax.
- [VAGST](ws-vat-gst.md) owns the indirect-tax rate, taxable supplies/registration, input credits, import/export treatment, ordinary filing periods and the unresolved administrative deadline conflict.
- [Payroll](ws-payroll-social.md) owns fortnightly PAYE, SNPF/ACC splits, contribution bases and separate remittance jobs.
- [Formation](ws-company-formation.md) owns entity/registry/licence steps, foreign-investment gates and the separate international-company restrictions.

The former overview’s personal top rate/allowance, company rate, VAGST rate and annual/monthly deadline bullets are preserved in those owner skills, with their corrections and boundaries. The international-company exemption is conditional and has an enacted future change; do not answer with the domestic company rate merely because “Samoa company” appears in the question. [section 249(2), exemptions and exclusions](https://sifa.ws/wp-content/uploads/2025/01/International-Companies-Act-1988.pdf); [sections 1-2 and 6, enacted deferred commencement](https://sifa.ws/wp-content/uploads/2026/06/Miscellaneous-Removal-of-Tax-Exemption-for-International-Companies-Amendment-Act-2026-Eng.pdf).

## Worked cases

### Route business receipts to the tax base

Assume an ordinary resident sole trader with WST 52,000 business receipts and WST 12,000 proved allowable expenses, no wages or final-tax/exempt income. The amount handed to personal income tax is WST 40,000, derived, not gross receipts. That skill computes the tax. This intake step does not establish VAGST registration or assume all expenses carry input credit.

```oa-check
name: Route business receipts to the tax base
inputs:
  receipts: 52000
  allowed_expenses: 12000
steps:
  - ordinary_taxable_income: receipts - allowed_expenses
expected:
  ordinary_taxable_income: 40000
```

### Route company profit and a separate royalty payment

Assume a company reports WST 90,000 assessable trading income and WST 30,000 established allowable trading deductions, plus a separate WST 20,000 outbound royalty requiring payee/PE/treaty checks. Hand a WST 60,000 derived trading subtotal to corporate tax and hand the royalty gross amount separately to its withholding analysis. Do not subtract an untested royalty a second time or confuse the gross payment with taxable trading profit.

```oa-check
name: Route company profit and a separate royalty payment
inputs:
  trading_income: 90000
  allowed_trading_deductions: 30000
  royalty_gross: 20000
steps:
  - trading_subtotal: trading_income - allowed_trading_deductions
  - withholding_review_base: royalty_gross
expected:
  trading_subtotal: 60000
  withholding_review_base: 20000
```

## When to refuse or refer

Stop if the place is American Samoa, the year/entity/source is unclear, the requested filing needs an unavailable final-year form, the client relies on an exemption without evidence, or a VAGST/imported-service/ACC deadline boundary is unresolved. Transfer pricing and a full cross-border/treaty skill remain missing in the pack README. Do not imply that six mechanically compliant skills cover every Samoan tax or complete a filing.

## Ask the client first

- Which jurisdiction, year/balance date, legal form, residence and ownership?
- What income types, source, staff, imports/exports, taxable activity and turnover?
- What registrations, statutory notices, exemption certificates and final-year forms?
- Is the requested output an estimate, comparison, working paper or filing step?

## Sources

Read on **2026-11-15** for the stated sections. The Attorney General tax consolidations are official texts as at 31 December 2023; current Ministry guidance and the later instruments expressly identified below were checked separately. A recent upload path does not change a document’s printed date.

| Source and scope actually read | URL | Read on |
|---|---|---|
| Read for section 2, resident company; section 10; section 13; section 14; section 18; section 19; section 34; section 6; section 2, tax year | https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf | 2026-11-15 |
| Read for sections 1-2 and 6, enacted deferred commencement | https://sifa.ws/wp-content/uploads/2026/06/Miscellaneous-Removal-of-Tax-Exemption-for-International-Companies-Amendment-Act-2026-Eng.pdf | 2026-11-15 |
| Read for section 249(2), exemptions and exclusions | https://sifa.ws/wp-content/uploads/2025/01/International-Companies-Act-1988.pdf | 2026-11-15 |
| Read for Tax Due Dates and footnote | https://revenue.gov.ws/inland-revenue-services/ | 2026-11-15 |

Not yet confirmed: The subject-specific boundaries in the linked skills, including final 2026 income-tax forms, treaty/transfer-pricing coverage, VAGST deadline/instrument reconciliation and separate fund/ACC operational directions. This router does not supply missing filing evidence.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ws-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ws-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
