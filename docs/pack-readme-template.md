# Pack README template

Every jurisdiction pack (`skills/international/<country>/`, `skills/us-states/<xx>/`, `packages/ca-<xx>/`) has a `README.md` that says which tax domains apply there. `scripts/coverage-report.py` reads it, so a domain a jurisdiction does not have stops showing as missing, and a skill whose name does not reveal its domain is still counted. `scripts/build-index.py` skips README files, so this never changes the skill counts.

Copy this, fill the frontmatter, delete these instructions.

```markdown
---
jurisdiction: XX
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable:
  TP: no transfer pricing documentation regime; related-party rules are in the corporate skill
covered_by:
  SC: xx-national-insurance
  XB: moving-to-xx-tax-residence
partial:
  PR: employees only; no rules for directors' fees
---

# Country name: tax pack

One paragraph on the tax system a visitor should know before reading any skill: tax year, authority, currency, anything unusual (no VAT, territorial system, federal and state layers).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | xx-income-tax | source-cited draft |
| IT-CORP, corporate income tax | (missing) | |
| VAT / GST | xx-vat-return | source-cited draft |
| SC, social contributions | xx-national-insurance | source-cited draft |
| PR, payroll withholding | xx-payroll | source-cited draft |
| TP, transfer pricing | not applicable, see above | |
| XB, cross-border | moving-to-xx-tax-residence | source-cited draft |

## Official sources

The tax authority, the statutes, and the gazette pages the pack cites, each with the date last read.
```

Rules:
- `applicable` lists the domain codes from GOAL.md that exist in this jurisdiction. `not_applicable` gives a one-line reason for each domain left out; "not applicable" with no reason is not accepted.
- `covered_by` is only needed when the covering skill's slug does not contain the usual tokens (income-tax, corporate, vat, gst, sales-tax, social, payroll, withholding, transfer-pricing, exit, departure, treaty).
- `partial` names a domain whose skills exist but leave out a part of it that most clients need (for example SC covered for the self-employed only). The report counts it as missing until the gap is closed: a skill being present is not coverage. Say what is missing in one line.
- Status uses the two quality states only: `source-cited draft` or `accountant-reviewed`.
- Keep it short. The README is a map, not a guide.
