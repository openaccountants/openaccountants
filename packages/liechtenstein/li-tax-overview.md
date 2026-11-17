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
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.4
tier: 2
type: router
---

# Liechtenstein tax overview v0.4

> **General reference only.** This Guide selects the next tax workpaper. A qualified Liechtenstein professional must review the actual facts, documents and filing position before action.

## Ask the client first

- Is this an individual or entity, and what is its legal form and tax residence?
- Where are the home, seat, actual management, work, assets and supplies located?
- Which tax year and transaction dates apply, and are any periods shorter than a year?
- What income, wealth, turnover, wages or payments and existing registrations are involved?
- For an individual, what family category and municipality apply?
- Is there foreign tax, a treaty claim, a related party, a regulated activity or a special regime?

## The method, step by step

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

### Rates, bands and thresholds

| Item | 2026 rule | Source |
|---|---|---|
| Tax authority | Steuerverwaltung (Liechtenstein Tax Administration) | https://www.llv.li/de/landesverwaltung/steuerverwaltung |
| Currency | Swiss franc (CHF) | SteG article 19 (amounts in Franken), https://www.gesetze.li/konso/pdf/2010340000 |
| Tax year | Calendar year; a shorter liability period replaces it; a business whose accounts do not end on 31 December declares the result of the financial year that ended | [SteG articles 14(5), 47(6)](https://www.gesetze.li/konso/pdf/2010340000) |
| Who is taxed on what | Individuals resident or habitually staying in Liechtenstein: worldwide income and wealth. Nonresidents: Liechtenstein property, permanent establishments and the domestic income listed in article 6(5). Companies with seat or actual management in Liechtenstein: all their profit | [SteG articles 6(1), 6(2), 6(4)-(5), 44(1)](https://www.gesetze.li/konso/pdf/2010340000); domestic and treaty exemptions still require the linked workpaper |
| Taxes in the Tax Act | Wealth-and-income tax, expenditure (lump-sum) tax, property gains tax, corporate income tax, formation duty and insurance-premium duty; GloBE top-up tax under its own Act | [SteG article 1](https://www.gesetze.li/konso/pdf/2010340000) |
| Individuals: state tax | 0% up to the basic allowance (CHF 15,855 general tariff, CHF 23,783 single parents, CHF 31,710 joint spouses), then marginal rates of 1% to 8% | [SteG article 19(1)](https://www.gesetze.li/konso/pdf/2010340000); first test the separate subsistence exemption in article 15(2)(i), using li-income-tax |
| Individuals: wealth | Net wealth taxed as a 4% deemed yield (Sollertrag) added to income | [SteG articles 5, 14(2)(l), 15(1)](https://www.gesetze.li/konso/pdf/2010340000); avoid adding the same taxed wealth's actual yield again |
| Individuals: municipal tax | A surcharge of 150% to 250% of state tax, set each year by the municipal council; none on tax withheld at source. The top combined marginal rate is therefore 20% (8% x 2.5) to 28% (8% x 3.5) | [SteG articles 19(1), 75](https://www.gesetze.li/konso/pdf/2010340000); combined endpoint percentages are derived, not a current municipality list |
| Inheritance, estate and gift tax | None in the Tax Act. Inheritances, legacies and gifts are not taxed as income, but gift donors/recipients and inheritance or legacy recipients report amounts from CHF 10,000 in the return | [SteG articles 1, 15(2)(c), 96](https://www.gesetze.li/konso/pdf/2010340000); [SteV article 43](https://www.gesetze.li/konso/pdf/2010437000) |
| Companies | 12.5% of taxable net income; CHF 1,800 minimum tax, credited against it, not charged on a purely commercial business whose average balance-sheet total over the last three years is CHF 500,000 or less | [SteG articles 61-62](https://www.gesetze.li/konso/pdf/2010340000); minimum-tax scope and short-period conditions require li-corporate-income-tax |
| Withholding tax on dividends, interest, royalties | No general source withholding under these Tax Act provisions on those payment categories: source tax applies to wages, replacement income, board fees and specified pensions (and 12% on nonresident entities' board-function income) | [SteG articles 24, 63a](https://www.gesetze.li/konso/pdf/2010340000); foreign withholding and payment classification require li-cross-border |
| VAT | 8.1% standard, 2.6% reduced, 3.8% accommodation; ordinary business exemption below CHF 100,000 worldwide qualifying turnover, excluding article 21(2) exempt supplies; other article 10 exemptions and optional registration apply; Liechtenstein and Switzerland form one VAT territory | [MWSTG articles 3, 10-11, 25](https://www.gesetze.li/konso/pdf/2009330000); [authority common-territory explanation](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer) |
| Social contributions | Employee 4.9% AHV/IV/FAK plus 0.5% ALV; employer 7.385% covering AHV/IV/FAK and administration (VK), plus 0.5% ALV; ALV applies only to the capped base, ordinarily CHF 126,000 per employment annually with part-year adjustment; other insurance costs remain separate | AHV-IV-FAK bulletin 1.01, 2026, https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf |
| Late-payment interest on tax | 4% | SteV article 45, https://www.gesetze.li/konso/pdf/2010437000 |

The official entry points are the [Steuerverwaltung](https://www.llv.li/de/landesverwaltung/steuerverwaltung) and the [Liechtenstein law register](https://www.gesetze.li). Each linked skill cites the exact articles it uses.

## Worked cases

### Municipal surcharge endpoints are an arithmetic screen

Assume the ordinary top state marginal rate applies and no special regime changes it. A municipal surcharge of 150% of state tax makes the combined marginal rate 8% × (1 + 1.5) = 20%; a 250% surcharge makes it 28%. The difference is 8 percentage points. These statutory endpoints do not establish an actual municipality's annual rate or a person's average/effective tax rate. Route the facts and subsistence screen to li-income-tax before calculating liability. [SteG articles 19 and 75](https://www.gesetze.li/konso/pdf/2010340000).

```oa-check
name: Liechtenstein municipal surcharge endpoints
inputs:
  top_state_rate: 0.08
  lower_municipal_surcharge: 1.5
  upper_municipal_surcharge: 2.5
steps:
  lower_combined_rate: top_state_rate * (1 + lower_municipal_surcharge)
  upper_combined_rate: top_state_rate * (1 + upper_municipal_surcharge)
  difference_percentage_points: (upper_combined_rate - lower_combined_rate) * 100
expected:
  lower_combined_rate: 0.20
  upper_combined_rate: 0.28
  difference_percentage_points: 8
```

## When to refuse or refer

Do not calculate liability from this headline table. Load the topic Guide and obtain the required facts. Refer disputed residence, PVS, GloBE, foundations, treaty entitlement, special VAT supplies and filing calendars to the appropriate workpaper and a qualified professional. Registration or an entity's name alone proves no exemption.

## Sources

| Source | URL | Read on |
|---|---|---|
| Steuergesetz (SteG), consolidated 1 July 2026, selected provisions read: articles 1, 5, 6, 14(2), 14(5), 15, 19, 24, 44, 47, 61-62, 63a, 75, 96 | https://www.gesetze.li/konso/pdf/2010340000 | 2026-11-16 |
| Steuerverordnung (SteV), consolidated 1 July 2026, selected provisions read: articles 43 and 45 | https://www.gesetze.li/konso/pdf/2010437000 | 2026-11-16 |
| Mehrwertsteuergesetz (MWSTG), consolidated 1 January 2026, selected provisions read: articles 3, 10-11, 25, including registration exceptions and restaurant/accommodation conditions | https://www.gesetze.li/konso/pdf/2009330000 | 2026-11-16 |
| AHV-IV-FAK, bulletin 1.01 contributions, effective 1 January 2026, sections 2-6: age/status, employee and employer rate table, VK, annual and part-year ALV cap | https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf | 2026-11-16 |
| Steuerverwaltung, substantive responsibilities paragraph and navigation to topic services | https://www.llv.li/de/landesverwaltung/steuerverwaltung | 2026-11-16 |
| Steuerverwaltung, Mehrwertsteuer, substantive common-territory paragraph | https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer | 2026-11-16 |

Not yet confirmed: the filing dates for 2026 individual and corporate returns; the 2026 surcharge of each municipality.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
