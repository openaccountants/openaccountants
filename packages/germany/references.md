---
name: germany-references
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-14
version: 2.0
description: Where the official German tax sources are and which Germany skill does which job, tax year 2026, plus the open-source projects earlier Germany skills drew on and how far they can be trusted.
tier: 2
type: router
---

# Germany: official sources and related open-source projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This file routes. It states no rate or threshold of its own. Every figure the Germany skills use comes from an official page named in that skill.

## The method, step by step

1. **Find the job, then the skill.** Income tax for the self-employed: `de-einkommensteuer-freelancer`. Employees: `de-employee-income-tax`. Payroll: `de-payroll`, with a UK employer's first hire in `de-uk-employer-first-hire`. VAT: `germany-vat-return` and `de-vat-annual-and-special-schemes`. E-invoicing: `germany-einvoice`. Trade tax: `de-trade-tax`. Corporate tax: `de-corporate-tax`. Social contributions: `de-social-contributions`. Crypto: `de-crypto-tax`. Withholding on payments abroad: `de-treaty-withholding-rates`. Exit tax: `leaving-germany-exit-tax`. Transfer pricing: `germany-transfer-pricing`. Books, accounts and formation: `germany-bookkeeping`, `germany-financial-statements`, `germany-formation`. Planning: `germany-tax-optimization`. The whole freelancer package: `de-return-assembly`.
2. **Read the statute on gesetze-im-internet.de.** The Federal Ministry of Justice publishes the consolidated federal law: EStG, KStG, GewStG, UStG, UStDV, AO, AStG, HGB, GmbHG, SGB IV. One page per section, for example [§ 32a EStG](https://www.gesetze-im-internet.de/estg/__32a.html), which sets the 2026 tariff.
3. **Read the ministry's letters for how the law is applied.** BMF letters (BMF-Schreiben) on bundesfinanzministerium.de bind the tax offices, not the courts. Use the letter's own paragraph numbers and its date.
4. **Use the BZSt for federal procedures:** withholding refunds and exemptions, VAT ID numbers, country-by-country reports.
5. **Compute wage tax from the official flowchart, never from a copy.** The BMF publishes a Programmablaufplan each year under [§ 39b(6) EStG](https://www.gesetze-im-internet.de/estg/__39b.html), and the [BMF calculator](https://www.bmf-steuerrechner.de/) runs it. A third-party library is at best a convenient implementation of an older or newer flowchart: check its year and version against the BMF's before trusting a figure.
6. **Treat the projects below as tools, not sources.** None of them is an official source for a figure.

### Related open-source projects

OpenAccountants is AGPL-3.0. All projects below have compatible licences as stated by their repositories. Star counts are as recorded on 2026-06-12.

| Project | Licence | Language | What it does | How it was used |
| --- | --- | --- | --- | --- |
| [jenner/LstGen](https://github.com/jenner/LstGen) | MIT | Python generator; outputs Python, Java, JavaScript, Go, PHP | Generates wage-tax calculators from the BMF Programmablaufplan XML files | Structure of the flowchart, input and output parameters, Steuerklassen; adapted into `de-payroll` with attribution |
| [MarcelLehmann/Lohnsteuer](https://github.com/MarcelLehmann/Lohnsteuer) | Apache-2.0 | Java (generated from BMF PAP XML) | Wage-tax calculator for 2006 onwards with the BMF XML files and a test suite against the BMF calculator | The 2025 flowchart constants (tariff, contribution ceilings, Steuerklasse V and VI limits, solidarity surcharge exemption) were taken into `de-payroll`; for 2026 `de-payroll` must use the 2026 flowchart |
| [taxcalcs/taxjs](https://github.com/taxcalcs/taxjs) | MIT | TypeScript and JavaScript | npm library for German wage tax generated from BMF pseudo-code | Validation of `de-payroll` results |
| [horstoeko/zugferd](https://github.com/horstoeko/zugferd) | MIT | PHP | ZUGFeRD, XRechnung and Factur-X library with code lists | VAT category codes (UNTDID 5305: S, Z, E, AE, K, G, O, L, M) referenced in `germany-vat-return`; e-invoice patterns |
| [0-k/netto](https://github.com/0-k/netto) | Not checked | Python | Net income calculator for income tax and social security | Pattern reference only; URL and licence not verified |

## When to refuse or refer

- A figure found only in one of the projects above, or in any non-official page: do not use it. Find it on the official page or list it as not confirmed.
- A wage-tax result from a library whose flowchart year is not 2026: recompute with the 2026 BMF flowchart or calculator.
- A question no Germany skill covers (gift and inheritance tax, real estate transfer tax, church tax detail by state): say so and refer to a Steuerberater.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for § 32a(1) EStG, the 2026 tariff (Grundfreibetrag EUR 12,348) as an example of a statute page | https://www.gesetze-im-internet.de/estg/__32a.html | 2026-11-14 |
| Read for § 39b(6) EStG, the BMF's duty to publish the Programmablaufplan | https://www.gesetze-im-internet.de/estg/__39b.html | 2026-11-14 |
| Read for the BMF wage-tax calculator and its 2026 year option | https://www.bmf-steuerrechner.de/ | 2026-11-14 |

Not yet confirmed: the licences and star counts of the open-source projects were recorded on 2026-06-12 and not re-read; 0-k/netto's URL and licence were never verified.
