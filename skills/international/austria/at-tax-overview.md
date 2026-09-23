---
name: at-tax-overview
description: "Source-cited draft: tax overview for Austria (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austria Tax Overview

A map of the main Austrian taxes for a person or a small business: who is taxed, the headline rates, the returns and their deadlines, and which OpenAccountants Guide holds the detail. It does not compute anything; each section points to the Guide that does. Figures are for tax year 2026. The pages used are the business service portal (USP) pages of the Finance Ministry, dated 1 January 2026, and the USP VAT rate page, updated 1 July 2026.

## Austrian tax system at a glance

**The basics**

| Field | Value |
| --- | --- |
| Tax year | Calendar year. A company can have a financial year that differs from the calendar year |
| Currency | Euro |
| Tax authority | Finanzamt Österreich; the Finanzamt für Großbetriebe for large businesses (see `at-corporate-income-tax`) |
| Filing portal | FinanzOnline. Paper only where the rules allow it |
| Main laws | Einkommensteuergesetz (EStG), Körperschaftsteuergesetz (KStG), Umsatzsteuergesetz (UStG), Bundesabgabenordnung (BAO); social insurance of the self-employed under the GSVG |
| Social insurance of the self-employed | Sozialversicherungsanstalt der Selbständigen (SVS), a separate body from the tax office |

### Who is taxed in Austria

A person with a home (Wohnsitz) or habitual abode (gewöhnlicher Aufenthalt) in Austria has unlimited tax liability and is taxed on worldwide income. Citizenship is not decisive; the USP says it plays a role only in exceptional cases. After six months of stay the unlimited liability applies in any case, backdated to the start of the stay. Others are taxed only on certain Austrian income, such as a salary or pension from Austria. A company is taxed on worldwide income if its seat or its management is in Austria (see `at-corporate-income-tax`).

**Residence of individuals**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/einkommensteuerpflicht.html |
| Home or habitual abode in Austria | Unlimited liability, worldwide income | "Unbeschränkt steuerpflichtig sind Personen, die in Österreich ihren Wohnsitz oder ihren gewöhnlichen Aufenthalt haben." |
| Stay of six months | Unlimited liability in any case, backdated | "Nach sechs Monaten Aufenthalt in Österreich tritt die unbeschränkte Steuerpflicht auf jeden Fall ein" |

Treaty tie-breaker rules and moves to or from Austria are outside this overview.

### Income tax (Einkommensteuer)

Individuals pay progressive income tax. Each person is taxed alone. The bracket limits are raised every year for cold progression, so never reuse an earlier year's limits. The full 2026 tariff, the profit allowance, flat-rate expenses, tax credits and the E 1 return for the self-employed are in `at-income-tax`.

**Income tax headline figures, 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/tarifstufen.html |
| Taxable yearly income taxed at 0%: up to and including | EUR 13,539 | "13.539  und darunter 0 Prozent" |
| Top threshold, not indexed | EUR 1,000,000 | "über  104.859  bis  1.000.000 50 Prozent" |
| Rate on income above EUR 1,000,000, temporary to 2029 | 55% | "ein höherer Steuersatz von 55 Prozent zur Anwendung" |

Each rate taxes only its own slice of income. Employees have wage tax (Lohnsteuer) withheld by the employer and may file an employee assessment; this overview does not cover payroll.

### Capital income (Kapitalertragsteuer, KESt)

Most capital income of individuals is taxed at a special flat rate, withheld at source by the bank or the paying company, and that normally settles the tax. The shareholder can opt for the regular assessment instead.

**Special rates on capital income**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/kapitalertragsteueranmeldung.html |
| Interest on savings and current accounts | 25% | "mit einem besonderen Steuersatz von 25 Prozent (für Zinsen aus Sparbüchern und Girokonten)" |
| All other capital income, such as dividends | 27.5% | "einem besonderen Steuersatz von 27,5 Prozent" |

Withholding by companies, and the rates on payments to foreign recipients, are in `at-corporate-income-tax`.

### Corporate income tax (Körperschaftsteuer)

A GmbH, an AG and other legal persons pay corporate income tax at a flat rate, plus a yearly minimum tax even in a loss year. Minimum tax, prepayments, losses, group taxation, the participation exemption and withholding taxes are in `at-corporate-income-tax`.

**Corporate income tax rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick.html |
| Rate from 2024, flat | 23% | "Die Körperschaftsteuer beträgt 23 Prozent" |

A partnership (OG, KG) does not pay corporate income tax; its partners pay income tax on their share.

### VAT (Umsatzsteuer)

VAT is charged on supplies of goods and services in Austria. Since 1 July 2026 there are four rates. Businesses file advance returns (Umsatzsteuervoranmeldung, form U 30) monthly or quarterly depending on prior-year turnover, or none at all below the lower band unless ordered or claiming a refund, and an annual return (form U 1). Small businesses under the turnover limit are exempt and file no VAT returns, but get no input VAT deduction, unless they waive the exemption. Filing periods, boxes, reverse charge and the small business rules in full are in `at-vat-return`.

**VAT rates from 1 July 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/steuersaetze-und-steuerbefreiungen-der-umsatzsteuer.html |
| Standard rate | 20% | "Der Normalsteuersatz der Umsatzsteuer beträgt 20 Prozent." |
| Reduced rate, for example live animals and plants, firewood, artists, film, sports tickets | 13% | "Der 13-prozentige Steuersatz gilt z.B. für Die Lieferung von lebenden Tieren" |
| Reduced rate, for example residential letting, accommodation, books, food | 10% | "Der 10-prozentige Steuersatz gilt z.B. für: Die Vermietung zu Wohnzwecken" |
| Selected basic foods listed by customs code, deliveries only, from 1 July 2026 | 4.9% | "Der 4,9-prozentige Steuersatz gilt für ausgewählte Nahrungsmittel, wie z.B. Brot, Butter, Eier, Milch." |

**Small business exemption (Kleinunternehmerregelung)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html |
| Yearly turnover limit, gross, regime since 1 January 2025 | EUR 55,000 | "Kleinunternehmergrenze in Höhe von 55.000 Euro". Must not be exceeded in the previous year nor in the current year; tolerance and the rest in `at-vat-return` |

### Social insurance of the self-employed (SVS)

A trader or new self-employed person is insured with the SVS for pension, health and accident insurance, and in most cases the self-employed severance provision (Selbständigenvorsorge); some liberal professions are insured with the SVS for pension only. Contributions are a share of a monthly base worked out from income, between a minimum and a maximum base, and are charged quarterly. They are deductible for income tax. Rates, bases, the insurance threshold for new self-employed persons, the small business exemption and due dates are in `at-svs-contributions`. SVS rules are separate from tax rules: the SVS small business limits are not the VAT limit, even where the numbers look the same.

### Setting up a company

For a GmbH, the minimum share capital also sets the minimum corporate tax. Founding steps, trade licence, registrations with the tax office and the SVS are in `at-company-formation`.

**GmbH minimum capital**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/services/suchen-und-finden/lexikon/gesellschaft-mit-beschraenkter-haftung-gmbh.html |
| Minimum share capital of a GmbH | EUR 10,000 | "Das Stammkapital einer GmbH muss mindestens 10.000 Euro betragen." In principle half must be paid in cash at formation |

### Return deadlines

Income tax, corporate income tax and the annual VAT return share the same deadlines: 30 April of the following year on paper, 30 June of the following year through FinanzOnline. The tax office can extend on a reasoned request, and a taxpayer represented by a tax adviser usually has longer. Prepayments of income tax and corporate tax fall due quarterly on the dates set in the prepayment notice.

**Annual returns and deadlines**

| Return | Form | Due | Detail |
| --- | --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuererklaerung.html | |
| Income tax | E 1 (with E 1a for business income) | 30 April on paper, 30 June via FinanzOnline | `at-income-tax`. "Abgabe der Steuererklärung in Papierform 30. April des Folgejahres" |
| Corporate income tax | K 1, K 2 or K 3 | 30 April on paper, 30 June via FinanzOnline | `at-corporate-income-tax`; USP page: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuererklaerung.html |
| VAT, annual | U 1 | 30 April on paper, 30 June via FinanzOnline | `at-vat-return`; USP page: https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html |
| VAT, advance | U 30 | 15th of the second month after the period | `at-vat-return`; USP page: https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html |
| SVS contributions | Charged by the SVS | Quarterly; dates in the Guide | `at-svs-contributions` |

Who must file an income tax return at all (the income limits) is in `at-income-tax`.

## The method, step by step

1. **Decide who is taxed and where.** For a person, check home and habitual abode under the income tax liability rules; for a company, seat and management: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/einkommensteuerpflicht.html
2. **Pick the tax type and the Guide.** Self-employed profit: income tax under the EStG, `at-income-tax`. A GmbH or AG: corporate income tax under the KStG, `at-corporate-income-tax`: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick.html
3. **Check VAT status.** Normal scheme or small business exemption under the UStG, then the filing period, in `at-vat-return`: https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html
4. **Check SVS insurance** for a self-employed person under the GSVG, in `at-svs-contributions`.
5. **File each return through FinanzOnline** by the dates in the deadlines table: E 1, K 1 and U 1 each have their own USP page linked there.

## Ask the client first

- Do you live in Austria, and since when? Do you have a home here or elsewhere as well?
- Are you employed, self-employed, or do you run a company (GmbH, AG) or a partnership?
- What was your turnover last year and so far this year? This decides the VAT small business exemption and the filing period.
- Are you insured with the SVS, and as a trader (Gewerbetreibender) or a new self-employed person (Neuer Selbständiger)?
- Do you have income from abroad, or pay anyone abroad?

## When to refuse or refer

- Any computation: this overview holds no method for computing tax. Use the linked Guide.
- Moves to or from Austria, dual residence and treaty tie-breakers: refer to a Steuerberater.
- Payroll and wage tax of employees, and the employee assessment: outside this overview.
- Real estate transfer tax, municipal tax on payroll, inheritance and foundation matters: outside this overview.
- Farming, and partnerships' own filing duties: outside this overview.

## Sources

- USP, Einkommensteuerpflicht: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/einkommensteuerpflicht.html
- USP, Tarifstufen: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/tarifstufen.html
- USP, Einkommensteuererklärung: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuererklaerung.html
- USP, Kapitalertragsteuer-Anmeldung: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/kapitalertragsteueranmeldung.html
- USP, Körperschaftsteuer: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick.html
- USP, Körperschaftsteuererklärung: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuererklaerung.html
- USP, VAT rates: https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/steuersaetze-und-steuerbefreiungen-der-umsatzsteuer.html
- USP, Kleinunternehmen: https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html
- USP, UVA and annual VAT return: https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html
- USP Lexikon, GmbH: https://www.usp.gv.at/services/suchen-und-finden/lexikon/gesellschaft-mit-beschraenkter-haftung-gmbh.html

This Guide is a source-cited draft. It is not tax advice. Confirm each figure on the official page before relying on it.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
