---
jurisdiction: SK
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: slovakia-pit
  IT-CORP: sk-corporate-income-tax
  VAT: slovakia-vat-return
  SC: sk-payroll-social
  PR: sk-payroll-social
  TP: sk-transfer-pricing
  XB: sk-cross-border
partial:
  VAT: "The owners retain unresolved zero-turnover annual coefficient, first control-statement breach and gross crossing-invoice boundaries."
  TP: "The owner retains unresolved APA-office identity and foreign deemed-dividend points."
  XB: "The owner has not established the operative Russia-treaty suspension boundary."
---

# Slovakia: tax pack

Start with [sk-tax-overview](sk-tax-overview.md) to identify the task, period and residence/source facts. The tax authority is the Financial Administration (Finančná správa SR); the tax owners use EUR and distinguish the tax year from any different company accounting period. Each owner carries its own law, conditions, forms and read dates. This coverage map does not repeat a second set of rates or imply that a file's existence resolves every boundary.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | [slovakia-pit](slovakia-pit.md): employment, self-employment, rent, capital/other income, allowances, bonus, expenses, advances and actual return | checked against the law |
| IT-CORP, corporate income tax | [sk-corporate-income-tax](sk-corporate-income-tax.md): revenue-based rate, minimum tax, expenses, VAT deductibility, depreciation, losses, interest limits, dividends, advances and actual return | checked against the law |
| VAT | [slovakia-vat-return](slovakia-vat-return.md): classification, input tax, reverse charge, car restrictions, periods, returns/control statements, refunds and penalties; [slovakia-vat-registration-4-7-7a](slovakia-vat-registration-4-7-7a.md): category, effective date, actual form and deregistration | checked against the law |
| SC, social contributions | [sk-payroll-social](sk-payroll-social.md): insured status, social/health bases, ceilings, employee/employer/SZČO methods, payment and reconciliation | checked against the law |
| PR, payroll withholding | [sk-payroll-social](sk-payroll-social.md): advances, allowance/child bonus, actual employer reports and reconciliation | checked against the law |
| TP, transfer pricing | [sk-transfer-pricing](sk-transfer-pricing.md): dependent persons, significance, methods, adjustments, documentation, return disclosure, penalties, CbCR and APAs | checked against the law |
| XB, cross-border | [sk-cross-border](sk-cross-border.md): residence/source, treaties, withholding, security deductions and foreign facts | checked against the law |

Formation is in [sk-company-formation](sk-company-formation.md); software provenance and evaluation are in [slovakia-references](references.md). This batch changes those files and the overview, with this coverage update; the other domain owners remain byte-identical to the baseline and are not newly reviewed by this rewrite.

## Out of scope

Apply each owner's explicit “Not yet confirmed” boundary. In particular, the VAT coefficient/control-statement and registration invoice issues, transfer-pricing APA/deemed-dividend points and cross-border treaty-suspension issue above remain unresolved. Do not convert a coverage label into an answer to those questions.

## Official sources

Follow the owner sources tables for the exact statutory provisions, official forms and actual read dates. The formation rewrite adds the current register/annex/trade-authorisation route and corrects the accounts-deposit deadline. Its source table records the provisions read on 2026-11-15. The overview links the official Financial Administration entry point; no generic electronic-filing platform replaces the relevant form's actual instructions.
