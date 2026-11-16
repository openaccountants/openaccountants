---
jurisdiction: BQ
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: bq-income-tax
  IT-CORP: bq-corporate-tax
  VAT: bq-abb
  SC: bq-social-contributions
  PR: bq-payroll
  XB: bq-double-tax-relief
partial:
  IT-CORP: "BES entities pay distribution tax (opbrengstbelasting), covered; minimum-tax computations, noncash distributions and foreign relief for entities are held"
  XB: "covers the BRN with the European Netherlands and the unilateral decree; other bilateral instruments for BES are not established"
---

# Caribbean Netherlands (BQ): tax pack

**Built from the law. Not yet approved.** Written by Ryan Duguid and imported from his fork on 14 November 2026; conformed to the standard by Claude. Not reviewed by an accountant.

Bonaire, Sint Eustatius and Saba (the BES islands) are public bodies of the Netherlands with their own tax system, the Belastingwet BES, run by the Belastingdienst Caribisch Nederland (belastingdienst-cn.nl). Law is published on wetten.overheid.nl. The currency is the US dollar. The tax year is the calendar year; this pack is for 2026. The three islands share the national taxes but not every rate: ABB and excise differ by island, and island taxes (Bonaire ground tax, Sint Eustatius tourist tax, Bonaire property-tax opcenten) come from each island's own ordinance. There is no VAT: the general expenditure tax (ABB) takes its place. Entities resident in BES pay distribution tax on what they distribute, not a profit tax. Start with `bq-tax-system`.

| Tax | Skill | Tax year | Status |
|---|---|---|---|
| Which tax applies (router) | [Tax system](bq-tax-system.md) | 2026 | Ready |
| Income tax (individuals) | [Income tax](bq-income-tax.md) | 2026 | Ready |
| Company tax | [Corporate and distribution tax](bq-corporate-tax.md) | 2026 | Partial: minimum tax and noncash distributions held |
| VAT or sales tax | [ABB](bq-abb.md) | 2026 | Ready: ABB does this job |
| Social contributions | [Contributions](bq-social-contributions.md) | 2026 | Ready |
| Payroll | [Payroll](bq-payroll.md) | 2026 | Ready (elderly reduction held) |
| Transfer pricing | | | Missing |
| Cross-border | [Double-tax relief](bq-double-tax-relief.md) | 2026 | Partial: BRN and unilateral decree only |
| Property tax (national) | [Property tax](bq-property-tax.md) | 2026 | Ready |
| Bonaire ground tax | [Ground tax](bq-bonaire-ground-tax.md) | 2026 | Ready |
| Transfer tax | [Transfer tax](bq-transfer-tax.md) | 2026 | Ready |
| Inheritance and gifts | [Inheritance and gifts](bq-inheritance-gifts.md) | 2026 | Scope only: no BES charge; European Netherlands connections |
| Gambling tax | [Gambling tax](bq-gambling-tax.md) | 2026 | Ready |
| Sint Eustatius tourist tax | [Tourist tax](bq-statia-tourist-tax.md) | 2026 | Ready |
| Excise | [Excise](bq-excise.md) | 2026 | Ready |
| Customs valuation | [Customs valuation](bq-customs-valuation.md) | 2026 | Ready |
| Customs clearance | [Customs clearance](bq-customs-clearance.md) | 2026 | Ready |
| Customs debt and remedies | [Customs debt](bq-customs-debt-remedies.md) | 2026 | Ready |
| Personal import relief | [Personal import relief](bq-personal-import-relief.md) | 2026 | Ready |
| Warehouses and HDE | [Warehouses and HDE](bq-warehouses-hde.md) | 2026 | Ready |
| Procedure | [Tax compliance](bq-tax-compliance.md) | 2026 | Ready |
| Penalties | [Penalties and corrections](bq-penalties-corrections.md) | 2026 | Ready |
| Company formation | [Formation](bq-formation.md) | 2026 | Ready |
| Annual accounts | [Financial statements](bq-financial-statements.md) | 2026 | Ready |

Ready means the skill is on the current tax year. It does not mean an accountant has reviewed it. Each skill lists what is still not confirmed at the end of its Sources section.

## What still needs doing

- Write a transfer pricing skill (arm's length rules for BES entities and the distribution tax).
- Add island ordinances not yet covered: Saba and Sint Eustatius local taxes other than the Sint Eustatius tourist tax, and the Bonaire and Saba tourist taxes.
- Confirm the bilateral instruments in force for BES beyond the BRN.
