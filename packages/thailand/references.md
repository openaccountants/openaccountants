---
name: thailand-references
jurisdiction: TH
last_updated: 2026-11-16
version: 1.1
description: "Thailand software-discovery catalogue for PIT, VAT, withholding and refund workflows, with official filing routes and explicit separation of historical project descriptions from verified tax law and licence clearance."
tier: 2
tax_year: 2026
type: router
category: integration
---

# Thailand primary-source and software reference catalogue v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## The method, step by step

**2026 answer layer:** use this catalogue to find a software project to inspect, never to establish a Thai tax figure. The Revenue Department is the primary tax source. This repository has separate software and content licences; the old claim that all listed projects have compatible licences was not established. Read the applicable licence before copying code or content.

1. Identify the actual job: PIT computation, VAT and withholding documents, ERP integration, or refund-status enquiry.
2. Load [PIT](thailand-pit.md), [VAT](thailand-vat.md), [payroll](th-payroll-social.md), [company tax](th-corporate-income-tax.md), or [formation](th-company-formation.md) for the substantive country method. Use [top-up tax](th-top-up-tax.md) for that separate multinational job.
3. Open the Revenue Department's [filing-service index](https://www.rd.go.th/rdeservice/63813.html) to select the official form and portal. A project's form name or API does not establish current filing acceptance.
4. If evaluating third-party code, pin its actual revision, inspect its licence and dependencies, compare its rules with the relevant country skill, and recompute its outputs before use. Do not send taxpayer credentials, bank statements or identity data to a project merely because it is listed here.

### ThaiTaxCalculator

- Repository: [ratanon97/ThaiTaxCalculator](https://github.com/ratanon97/ThaiTaxCalculator).
- Legacy catalogue description: Thai-language Next.js PIT calculator with rule-driven JSON configuration and retirement-investment optimisation. The prior PIT skill credited `ratanon97/ThaiTaxCalculator` and its `TH-2567.json` configuration; retain that provenance without using it as law or as a current-year rate source.
- Integration lead: bracket logic and configurable rules can be compared against independent arithmetic. Licence, current features and maintenance have not been reopened for this update.

### laravel-thai-tax

- Repository: [anurat/laravel-thai-tax](https://github.com/anurat/laravel-thai-tax).
- Legacy catalogue description: English/Thai Laravel PIT package; example API `ThaiTax::netIncome(500000)->incomeTax()` is retained as a historical software example, not a verified current API or a tax result.
- The old catalogue and PIT skill described an MIT licence. That exact-revision licence and attribution requirements remain to be inspected before integration. Do not infer legal accuracy from a licence.

### thai_tax (ERPNext)

- Repository: [kittiu/thai_tax](https://github.com/kittiu/thai_tax).
- Legacy catalogue description: ERPNext module covering sales tax, purchase tax, withholding tax, PND3/PND53 and withholding certificates. Preserve those integration leads; current functions and licence are unconfirmed.
- Compare the actual invoice, certificate and return fields against the official forms before connecting it to a working paper.

### thai-tax-refund

- Repository: [kittinan/thai-tax-refund](https://github.com/kittinan/thai-tax-refund).
- Legacy catalogue description: Thai-language Python refund-status tool for the Revenue Department. Current API, licence and permitted authentication workflow have not been inspected.
- Use the official authenticated service for a real taxpayer; this catalogue does not authorise automated access or disclosure.

## When to refuse or refer

Refuse to treat third-party rate JSON, screenshots, package tests or a source-code licence as tax authority. Do not port rules from an older Thai tax year without checking effective dates. Do not call an uninspected API with taxpayer data. Return a comparison report with the pinned revision, rules checked, arithmetic and unresolved licence/API points, rather than a filing-ready output.

## Sources

| Source and actual reading scope | URL | Read on |
|---|---|---|
| Revenue Department filing-service index (Read for the PIT, company-tax, VAT and withholding forms and portal links) | https://www.rd.go.th/rdeservice/63813.html | 2026-11-16 |
| Revenue Department annual-form index, 2026 (Read for the listed half-year forms and absence of annual PND.90/91 on the opened index) | https://www.rd.go.th/english/68443.html | 2026-11-16 |

Not yet confirmed: current source, features, licences and API permissions of all four retained third-party projects; any claim that all licences are compatible. The project links above are historical discovery leads, not tax citations.
