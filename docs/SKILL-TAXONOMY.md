# Skill taxonomy

This document maps the skill domains and the shape every jurisdiction's pack follows. Counts live in `python3 scripts/coverage-report.py --summary`, never here.

## How to read this document

Every freelancer and small business in every jurisdiction faces the same accounting obligations. The specifics differ, but the structure does not. This taxonomy uses that structure to make skill creation systematic and repeatable.

**Domains (the columns):**

[GOAL.md](../GOAL.md) goes deep on tax first. The seven tax domains are what the coverage report counts; a jurisdiction's pack is complete when it has one skill in the deep-tax shape for each domain that applies there.

| Code | Domain | What it answers |
|------|--------|-----------------|
| **TAX / IT-IND** | Individual income tax | "How much income tax do I owe as a person?" |
| **TAX / IT-CORP** | Corporate income tax | "How is my company taxed?" |
| **TAX / VAT** | VAT, GST or sales tax | "What do I charge, reclaim and file?" |
| **TAX / SC** | Social contributions | "What do I and my employer pay into social security?" |
| **TAX / PR** | Payroll withholding | "How do I compute wages, withholding and payslips?" |
| **TAX / TP** | Transfer pricing | "How do I document related-party transactions?" |
| **TAX / XB** | Cross-border | "Exit tax, treaties, non-residents: what applies when more than one country is involved?" |

The second milestone, **Accounting packs**, adds these. They never count as missing from a tax pack.

| Code | Domain | What it answers |
|------|--------|-----------------|
| **BK** | Bookkeeping | "How do I classify transactions and prepare my books?" |
| **EI** | E-invoicing | "Is my invoice compliant with local electronic invoicing rules?" |
| **FS** | Financial statements | "How do I prepare annual accounts and file them?" |
| **TO** | Tax optimisation | "What legal strategies reduce my tax bill?" |
| **CF** | Company formation | "What entity type should I choose and how do I register?" |
| **VT** | Industry verticals | "What is specific to my industry?" |
| **IN** | Platform integrations | "How do I read my Stripe, Xero or PayPal export?" |

**Functional roles (the rows within each skill):**

| Role | What it does | Example |
|------|-------------|---------|
| **Intake** | Collects data, runs the refusal sweep, hands off downstream | `us-ca-freelance-intake` |
| **Computation** | Applies rates, thresholds and deductions to classified data | `malta-income-tax` |
| **Return assembly** | Builds the actual form or return from computed figures | `mt-return-assembly` |
| **Workflow base** | Execution pipeline, output spec, self-checks, refusals | `bookkeeping-workflow-base` |

## Infrastructure skills

Foundation workflow bases live in `skills/foundation/` and are bundled into packages by the build: `workflow-base.md` (universal), `vat-workflow-base.md`, `us-tax-workflow-base.md`, `bookkeeping-workflow-base.md`, `einvoice-workflow-base.md`, `payroll-workflow-base.md`, `company-formation-workflow-base.md`, `financial-statements-workflow-base.md`, `transfer-pricing-workflow-base.md` and `cross-border-workflow-base.md`.

Orchestrators (`skills/orchestrator/`) are the global router plus per-country intake and return-assembly pairs. `skills/intelligence/` holds the deadline engine, threshold alerts and optimisation triggers; `skills/patterns/` holds vendor pattern libraries.

## The universal skill skeleton

Every jurisdiction can have skills in each domain. Not every jurisdiction needs every slot (US states have no VAT; the UAE has no individual income tax). The pack's `README.md` says which domains apply and which do not, with a reason. The skeleton is the same everywhere:

```
[Jurisdiction] Tax pack (milestone: Cover the world)
  ├── [Jurisdiction] Individual income tax          IT-IND
  ├── [Jurisdiction] Corporate income tax           IT-CORP
  ├── [Jurisdiction] VAT / GST / sales tax          VAT
  ├── [Jurisdiction] Social contributions           SC
  ├── [Jurisdiction] Payroll withholding            PR
  ├── [Jurisdiction] Transfer pricing               TP
  ├── [Jurisdiction] Cross-border                   XB
  └── [Jurisdiction] Guided intake + return assembly (if available)

[Jurisdiction] Accounting pack (milestone: Accounting packs)
  ├── Bookkeeping          chart of accounts, P&L, balance sheet (extends bookkeeping-workflow-base)
  ├── E-invoicing          format, mandatory fields, transmission (extends einvoice-workflow-base)
  ├── Financial statements annual accounts, reporting, audit (extends financial-statements-workflow-base)
  ├── Tax optimisation     legal strategies, deductions, timing (follows workflow-base)
  └── Company formation    entity types, registration, costs (extends company-formation-workflow-base)
```

Each tax skill follows the deep-tax shape in [skill-template.md](skill-template.md). Accounting-pack skills keep the general template.
