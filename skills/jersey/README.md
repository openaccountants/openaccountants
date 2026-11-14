---
jurisdiction: JE
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: je-income-tax
  IT-CORP: je-corporate-income-tax
  VAT: je-gst
  SC: je-social-contributions
  PR: je-payroll
  XB: je-cross-border-withholding
partial:
  IT-IND: "2026 standard and marginal calculations, thresholds and pension deduction supplied; special residence regimes, compensatory allowance computation, non-resident relief formula, assessment rounding and the personal instalment formula are not covered"
  IT-CORP: "residence, sector and retail rates, deductions, capital allowances, losses, group relief and payments supplied; complete distribution allocation, foreign-tax credits, anti-avoidance and specialist transfers are not covered"
  VAT: "classification, input tax, partial exemption, bad debts and imports supplied; partial-exemption rounding conflict, operational special schemes, GST penalties and customs tariff and excise are not covered"
  SC: "Class 1 monthly rates, earnings rules and Class 2 branches supplied; monetary rounding, non-monthly conversion, credits, penalties and standalone long-term care assessment are not covered"
  PR: "ITIS notices, defaults, returns and records supplied; minimum wage, overtime, benefits, pensions, termination and net-pay rounding are not covered"
  TP: "no transfer pricing skill yet; related-party and arm's length rules are not covered"
  XB: "individual non-resident exemptions, landlord collection and treaty relief steps supplied; treaty-specific rates, dividend deduction mechanics and corporate cross-border rules are not covered"
---

# Jersey: tax pack

**Built from the law. Not yet approved. Written by Ryan Duguid (imported from his fork). Not reviewed by an accountant.** Jersey is a Crown Dependency with its own tax system, run by Revenue Jersey. The year of assessment is the calendar year; currency is pounds sterling (GBP). Individuals pay the lower of 20% of income and 26% above an exemption threshold; companies pay 0% unless they are financial services (10%), utilities, property income or large retailers (up to 20%). GST is 5%. There is no capital gains tax or inheritance tax; property transfers carry land transaction tax or stamp duty, and land carries annual parish rates. Large multinational groups pay the 15% Multinational Corporate Income Tax.

## Domains

| Tax | Skill | Tax year | Status |
|---|---|---|---|
| IT-IND, individual income tax | [je-income-tax](je-income-tax.md), with [je-pension-contributions](je-pension-contributions.md) | 2026 | checked against the law (partial) |
| IT-CORP, company tax | [je-corporate-income-tax](je-corporate-income-tax.md), with [je-pillar-two](je-pillar-two.md) for MCIT and IIR | 2026 | checked against the law (partial) |
| VAT / GST | [je-gst](je-gst.md) | 2026 | checked against the law (partial) |
| SC, social contributions | [je-social-contributions](je-social-contributions.md), with [je-class2-contributions](je-class2-contributions.md) for the self-employed | 2026 | checked against the law (partial) |
| PR, payroll withholding (ITIS) | [je-payroll](je-payroll.md) | 2026 | checked against the law (partial) |
| TP, transfer pricing | (missing) | | |
| XB, cross-border | [je-cross-border-withholding](je-cross-border-withholding.md) | 2026 | checked against the law (partial) |
| Returns, penalties and appeals | [je-income-tax-compliance](je-income-tax-compliance.md) | 2026 | checked against the law |
| Property transactions and probate | [je-property-transactions](je-property-transactions.md) | 2026 | checked against the law |
| Annual parish rates | [je-parish-rates](je-parish-rates.md) | 2026 | checked against the law |
| Company formation and reporting | [je-company-formation](je-company-formation.md) | 2026 | checked against the law |
| Cryptocurrency | [je-crypto-tax](je-crypto-tax.md) | 2026 | checked against the law |

"Checked against the law" means the skill is on the 2026 tax year and cites the law and Revenue Jersey pages it relies on. It does not mean an accountant has reviewed it.

## Official sources

| Source | URL |
|---|---|
| Revenue Jersey | https://www.gov.je/TaxesMoney |
| Jersey Legal Information Board (laws as in force) | https://www.jerseylaw.je/laws/current |
| Jersey Financial Services Commission, Registry | https://www.jerseyfsc.org/registry/ |
| Comité des Connétables (parish rates) | https://comite.je/about-rates/ |

The full source register, with capture hashes and the coverage gaps, is in [references.md](references.md).

## What still needs doing

- Write a transfer pricing skill.
- Close the partial items above, starting with the personal instalment formula, treaty-specific rates and monetary rounding rules.
- Have a Jersey accountant review and approve each skill through their own GitHub PR.
