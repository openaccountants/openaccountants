---
name: li-tax-overview
description: >
  Route 2026 Liechtenstein tax questions to the right skill and give the headline
  figures. Covers the tax system at a glance: calendar tax year, Swiss franc,
  the Steuerverwaltung, who is taxed on what, individual wealth-and-income tax
  (state tax 0% up to a basic allowance, then 1% to 8%, plus a municipal surcharge of 150% to 250% of state tax, 4% deemed yield on
  wealth), corporate income tax (12.5%, CHF 1,800 minimum tax), VAT (8.1%,
  2.6%, 3.8%, common VAT territory with Switzerland), social contributions
  (AHV/IV/FAK, ALV), payroll withholding, transfer pricing, cross-border rules
  and company formation. Trigger on: Liechtenstein tax overview, taxes in
  Liechtenstein, how is Liechtenstein taxed, Steuern Liechtenstein. It gives no
  standalone liability calculation; each linked skill holds the rules, sources
  and worked examples.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.3
---

# Liechtenstein tax overview v0.3

## Start with the question

This is a router for 2026. Establish the person or entity, residence and activity countries, dates, the income, supply or payment, existing registrations and records before choosing a skill.

| Work | Read first | Key point |
|---|---|---|
| Individual income and wealth | [li-income-tax](li-income-tax.md) | Family tariff, 4% deemed yield on net wealth, the municipality's surcharge |
| Corporate profit | [li-corporate-income-tax](li-corporate-income-tax.md) | Tax adjustments, modified-equity deduction, losses, minimum tax |
| VAT | [liechtenstein-vat](liechtenstein-vat.md) | Registration, common territory with Switzerland, input tax, reporting method |
| Employee withholding and social insurance | [li-payroll-social](li-payroll-social.md) | Separate tax and contribution bases, 2026 Liechtenstein rates |
| Related parties and permanent establishments | [li-transfer-pricing](li-transfer-pricing.md) | Documentation route, arm's-length method, CbC reporting |
| Moving, foreign income and relief | [li-cross-border](li-cross-border.md) | Domestic liability first, then the treaty and the claim procedure |
| Setting up an entity | [li-company-formation](li-company-formation.md) | Legal form, capital, registration, accounts and review |

## Liechtenstein at a glance

| Item | 2026 rule | Source |
|---|---|---|
| Tax authority | Steuerverwaltung (Liechtenstein Tax Administration) | https://www.llv.li/de/landesverwaltung/steuerverwaltung |
| Currency | Swiss franc (CHF) | SteG article 19 (amounts in Franken), https://www.gesetze.li/konso/pdf/2010340000 |
| Tax year | Calendar year; a shorter liability period replaces it; a business whose accounts do not end on 31 December declares the result of the financial year that ended | SteG articles 14(5), 47(6) |
| Who is taxed on what | Individuals resident or habitually staying in Liechtenstein: worldwide income and wealth. Nonresidents: Liechtenstein property, permanent establishments and the domestic income listed in article 6(5). Companies with seat or actual management in Liechtenstein: all their profit | SteG articles 6(1), 6(2), 6(4)-(5), 44(1) |
| Taxes in the Tax Act | Wealth-and-income tax, expenditure (lump-sum) tax, property gains tax, corporate income tax, formation duty and insurance-premium duty; GloBE top-up tax under its own Act | SteG article 1 |
| Individuals: state tax | 0% up to the basic allowance (CHF 15,855 general tariff, CHF 23,783 single parents, CHF 31,710 joint spouses), then marginal rates of 1% to 8% | SteG article 19(1) |
| Individuals: wealth | Net wealth taxed as a 4% deemed yield (Sollertrag) added to income | SteG articles 5, 14(2)(l) |
| Individuals: municipal tax | A surcharge of 150% to 250% of state tax, set each year by the municipal council; none on tax withheld at source. The top combined marginal rate is therefore 20% (8% x 2.5) to 28% (8% x 3.5) | SteG articles 19(1), 75 |
| Inheritance, estate and gift tax | None in the Tax Act. Inheritances, legacies and gifts are not taxed as income, but donor, recipient and heir report them in the return | SteG articles 1, 15(2)(c), 96(1) |
| Companies | 12.5% of taxable net income; CHF 1,800 minimum tax, credited against it, not charged on a purely commercial business whose average balance-sheet total over the last three years is CHF 500,000 or less | SteG articles 61-62 |
| Withholding tax on dividends, interest, royalties | None: source tax applies only to wages, replacement income, board fees and specified pensions (and 12% on nonresident entities' board-function income) | SteG articles 24, 63a |
| VAT | 8.1% standard, 2.6% reduced, 3.8% accommodation; registration below CHF 100,000 worldwide turnover is exempt; Liechtenstein and Switzerland form one VAT territory | MWSTG articles 3, 10, 25, https://www.gesetze.li/konso/pdf/2009330000 |
| Social contributions | Employee 4.9% AHV/IV/FAK plus 0.5% ALV; employer 7.385% plus 0.5% ALV | AHV-IV-FAK bulletin 1.01, 2026, https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf |
| Late-payment interest on tax | 4% | SteV article 45, https://www.gesetze.li/konso/pdf/2010437000 |

The official entry points are the [Steuerverwaltung](https://www.llv.li/de/landesverwaltung/steuerverwaltung) and the [Liechtenstein law register](https://www.gesetze.li). Each linked skill cites the exact articles it uses.

## Sources

| Source | URL | Read on |
|---|---|---|
| Steuergesetz (SteG), consolidated 1 July 2026, articles 1, 5, 6, 14, 15, 19, 24, 44, 47, 61-63a, 75, 96 | https://www.gesetze.li/konso/pdf/2010340000 | 2026-10-30 |
| Steuerverordnung (SteV), consolidated 1 July 2026, article 45 | https://www.gesetze.li/konso/pdf/2010437000 | 2026-10-30 |
| Mehrwertsteuergesetz (MWSTG), consolidated 1 January 2026, articles 3, 10, 25 | https://www.gesetze.li/konso/pdf/2009330000 | 2026-10-30 |
| AHV-IV-FAK, bulletin 1.01 contributions, 1 January 2026 | https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf | 2026-10-30 |
| Steuerverwaltung | https://www.llv.li/de/landesverwaltung/steuerverwaltung | 2026-10-31 |

Not yet confirmed: the filing dates for 2026 individual and corporate returns; the 2026 surcharge of each municipality.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
