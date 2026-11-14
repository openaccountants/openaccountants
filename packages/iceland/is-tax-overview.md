---
name: is-tax-overview
description: "A one-page map of the Icelandic tax system for tax year 2026, from the Income Tax Act 90/2003, the VAT Act 50/1988 and Acts 4/1995, 113/1990 and 129/1997 as consolidated on althingi.is (text 158a), Advertisement 1521/2025 and Skatturinn's 2026 pages and filing notices. Covers the income year, the authority, who is taxed on worldwide income, the 2026 withholding bands (31.49%, 37.99%, 46.29%), the personal credit, the 22% capital income tax, company tax at 20% and 37.6%, the 6.35% payroll levy, the 15.5% minimum pension contribution, VAT at 24% and 11% with the ISK 2,000,000 registration limit, and the main 2026 deadlines (company returns 31 May, professional extension to 21 September). Use for how does tax work in Iceland, Iceland tax overview, Iceland tax rates 2026. It points to the pack's domain skills for the detail, namely iceland-income-tax, is-corporate-income-tax, iceland-vat, iceland-payroll, iceland-social-contributions, is-cross-border, is-transfer-pricing, is-company-formation and iceland-tax-optimization."
jurisdiction: IS
category: international
tax_year: 2026
last_updated: 2026-11-14
version: 1.0
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: situation-rules
---

# Iceland Tax Overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This is a map, not a computation skill. Each line gives the 2026 headline figure and its source, and names the skill in this pack that carries the full rules. Where a domain skill and this overview ever differ, the domain skill wins.

## Who this applies to

Iceland taxes individuals on earned income at progressive rates (state income tax plus municipal tax, collected together), taxes capital income at a flat rate, taxes companies at a flat rate, and charges value added tax (virðisaukaskattur, VSK). The tax authority is Skatturinn (Iceland Revenue and Customs). The ordinary income year is the calendar year.

- **Who pays on worldwide income.** People domiciled in Iceland, and resident companies, pay income tax on all their income wherever it is earned _(Income Tax Act, Articles 1 and 2)_. A person who stays in Iceland for more than 183 days in total in any 12-month period, counting normal absence for holidays, is taxed the same way _(Article 1(1)(3))_. Others are taxed only on the Icelandic income listed in Article 3, such as pay for work done in Iceland _(Article 3)_. Detail: `is-cross-border`.
- **Tax authority.** Skatturinn (Iceland Revenue and Customs) assesses and collects income tax, VAT and the payroll levy. Companies are registered in its company register (fyrirtækjaskrá) _(Skatturinn, private limited companies page; [skatturinn.is](https://www.skatturinn.is/english/))_.
- **Currency.** Icelandic króna (ISK). The tax acts and the 2026 advertisement state every amount in krónur _(Advertisement 1521/2025)_.

### Which skill to use

| Question | Skill |
|---|---|
| An individual's return, bands, credit, capital income, sole traders | `iceland-income-tax` |
| Company tax at 20% or 37.6%, losses, depreciation, filing and payment | `is-corporate-income-tax` |
| VAT returns, rates, registration, VOES | `iceland-vat` |
| Payroll levy and pension contributions | `iceland-social-contributions` |
| Gross to net, withholding, benefits in kind | `iceland-payroll` |
| Residence, non-residents, withholding on payments abroad, treaties | `is-cross-border` |
| Related-party prices and documentation | `is-transfer-pricing` |
| ehf., hf., partnership or sole trade: forming and running one | `is-company-formation` |
| Lawful ways to lower the tax bill | `iceland-tax-optimization` |


## Rates, bands and thresholds

| Item, 2026 | Figure | Detail skill | Source |
| --- | --- | --- | --- |
| Withholding band 1, monthly income up to ISK 498,122 (state plus average municipal) | 31.49% | `iceland-income-tax` | https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/ |
| Withholding band 2, ISK 498,123 to ISK 1,398,450 | 37.99% | `iceland-income-tax` | same |
| Withholding band 3, above ISK 1,398,450 | 46.29% | `iceland-income-tax` | same |
| Annual state bands: up to ISK 5,977,470; to ISK 16,781,397; above | 16.55%, 23.05%, 31.35% | `iceland-income-tax` | https://island.is/stjornartidindi/nr/34903c0c-a215-46e9-878c-b1ecff73af7d |
| Average municipal rate built into withholding | 14.94% | `iceland-income-tax` | same |
| Personal tax credit | ISK 869,898 a year, ISK 72,492 a month | `iceland-income-tax` | https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/ |
| Children born 2011 or later, income above ISK 300,000 a year | 6% | `iceland-income-tax` | https://www.skatturinn.is/einstaklingar/helstutolur/2026/ |
| Capital income tax, individuals (interest, dividends, gains, rent) | 22%; allowance ISK 300,000 a person, ISK 600,000 a married couple | `iceland-income-tax` | https://www.skatturinn.is/einstaklingar/helstutolur/2026/ |
| Company tax, hf., ehf. and other Article 2(1)(1) and (2) entities | 20% | `is-corporate-income-tax` | https://www.skatturinn.is/einstaklingar/helstutolur/2026/ |
| Other taxable entities (separately taxed partnerships, estates) | 37.6% | `is-corporate-income-tax` | https://www.skatturinn.is/einstaklingar/helstutolur/2026/ |
| Payroll levy (tryggingagjald) in withholding: 4.90% general, 1.35% employment insurance, 0.05% wage guarantee, 0.05% market fee | 6.35% | `iceland-social-contributions` | https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf |
| Employer pension default in the employer return, against 4% from the employee | 11.5% | `iceland-payroll` | https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf |
| VAT standard and reduced rate | 24% and 11% | `iceland-vat` | https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/ |
| VAT registration limit, taxable sales in each 12-month period | ISK 2,000,000 | `iceland-vat` | https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/almennt-um-vsk/ |
| VAT annual settlement, taxable sales in a calendar year under | ISK 4,000,000 | `iceland-vat` | https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/almennt-um-vsk/ |
| Transfer pricing documentation, operating revenue or total assets above | ISK 1,000,000,000 | `is-transfer-pricing` | https://www.skatturinn.is/atvinnurekstur/skattskylda/milliverdlagning/ |

The minimum pension contribution is 15.5% of the contribution base _(Act 129/1997, Article 2)_, and each municipality sets its own rate between 12.44% and 14.97% _(Act 4/1995 on Municipal Revenue, Article 23)_, so the final bill uses the rate of the municipality of domicile. Both rest on the Alþingi text, which could not be reopened on 14 Nov 2026; they are on the "Not yet confirmed:" line.

## The base

- **Income year.** Tax is based on the income of the calendar year before the assessment, so the 2026 return reports 2025 income and 2026 income is assessed in 2027. Skatturinn can allow a different accounting year where that is normal in the trade or the taxpayer shows it keeps one _(Income Tax Act 90/2003, Article 59)_. Detail: `is-corporate-income-tax`.
- **Earned income** (wages, calculated remuneration, business profit, pensions) is taxed on the progressive bands after the deductible pension contributions (4% mandatory, up to 4% supplementary), less the personal credit. Detail: `iceland-income-tax`.
- **Capital income** is taxed separately at 22%; for 2026 the personal credit no longer reduces it. Detail: `iceland-income-tax`.
- **Companies** are taxed on accounting profit adjusted to the tax base. Detail: `is-corporate-income-tax`.
- **Pension contributions.** Skatturinn's employer return calculates 11.5% from the employer against 4% from the employee _(Skatturinn, employer notice 1/2026)_. Detail: `iceland-payroll`.
- **Transfer pricing.** Prices between related parties must match what unrelated parties would agree. A legal entity whose operating revenue or total assets pass ISK 1 billion must document its transactions with related legal entities from the next financial year _(Income Tax Act, Article 57)_. Detail: `is-transfer-pricing`.

## Deadlines and filing

- **Withholding (staðgreiðsla) due dates.** Withholding for a wage month falls due on the 1st of the next month; the final due date is the 15th _(Skatturinn, employer register)_. Detail: `iceland-payroll`.
- **VAT periods and due date.** Two-month periods (January and February, March and April, and so on) _(VAT Act, Article 24)_. Return and payment are due on the 5th day of the second month after the period ends, which is one month and five days, moving to the next working day after a weekend or holiday _(Skatturinn, VAT general page and guide to VAT registration)_. A business with taxable sales under ISK 4,000,000 in a whole calendar year can ask to settle once a year _(VAT Act, Article 24; Skatturinn, VAT general page)_. Detail: `iceland-vat`.
- **Individual returns.** The 2026 return (2025 income) was due on 13 March 2026 _(Skatturinn, filing a tax return)_. Detail: `iceland-income-tax`.
- **Company returns.** For the 2026 return (2025 income) the general deadline was 31 May 2026. Professional preparers (auditors and bookkeepers) could get an extension up to 21 September 2026. The extension is not automatic _(Skatturinn, notice of 30 January 2026; Income Tax Act, Article 93)_. Detail: `is-corporate-income-tax`.
- **Annual accounts.** Companies file annual accounts with the Register of Annual Accounts no later than one month after approval, and no later than eight months after the year end _(Annual Accounts Act 3/2006, Article 109)_. Detail: `is-company-formation`.

## Penalties and interest

- **Late returns.** Where no return is filed on time, Skatturinn estimates the tax bases and may add a surcharge of up to 15% to them _(Income Tax Act, Article 108)_. Detail: `iceland-income-tax`.
- **Late payment of withholding and levies.** A surcharge of 1% for each day after the due date, at most 10%, and penalty interest from the due date if not paid within a month _([Skatturinn, all taxes and charges](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/))_. Detail: `iceland-payroll`.

## Cross-border points

Non-residents are taxed on the Icelandic income in Income Tax Act Article 3, mostly through withholding at source; residence turns on domicile or a stay of more than 183 days in a 12-month period. Treaty relief, permanent establishments, the resident-like treatment for EEA residents and exit rules are in `is-cross-border`; related-party pricing in `is-transfer-pricing`.

## Two worked examples that recompute

### Example 1: an employee's monthly withholding, January 2026

Gross salary ISK 800,000 a month, one employer, 4% mandatory pension, full personal credit. Base after pension: ISK 768,000. Withholding: 31.49% of ISK 498,122 plus 37.99% of ISK 269,878, less ISK 72,492 credit: ISK 186,893.27 (rounded in practice to whole krónur, ISK 186,893).

```oa-check
name: IS 2026 monthly withholding, salary 800,000
inputs:
  gross: 800000
steps:
  - base: gross * 0.96
  - tax: round(min(base, 498122) * 0.3149 + (base - 498122) * 0.3799 - 72492, 2)
expected:
  base: 768000
  tax: 186893.27
```

### Example 2 (decision): must a new sole trader register for VAT, and may she settle once a year?

A new sole trader expects taxable sales of ISK 3,500,000 (before VAT) in her first 12 months, all in calendar 2026. That is above the ISK 2,000,000 limit, so she must register and charge VAT; at the standard rate her output VAT is ISK 840,000. Because her sales in the whole calendar year are under ISK 4,000,000 she can ask to settle once a year instead of every two months. At ISK 1,800,000 neither question arises: she need not register (she may still apply).

```oa-check
name: IS 2026 VAT registration and annual settlement test
inputs:
  sales: 3500000
steps:
  - must_register: min(max(sales - 2000000, 0), 1)
  - annual_allowed: min(max(4000000 - sales, 0), 1)
  - output_vat: sales * 0.24
expected:
  must_register: 1
  annual_allowed: 1
  output_vat: 840000
```

## Ask the client first

- Is the person domiciled in Iceland, or how many days did they stay in any 12-month period?
- Employee, sole trader, or owner of an ehf. or hf.?
- Which municipality of domicile (for the final municipal rate)?
- Expected taxable sales in the next 12 months and in the calendar year (VAT tests)?
- Any foreign income, foreign payer or related-party transactions?

## Sources

Pages dated 2026-11-14 were opened again today and the figures named were found on them. Alþingi's law pages returned HTTP 403 on 14 Nov 2026 and keep their earlier read date.

| Source | URL | Read on |
|---|---|---|
| Read for Income Tax Act 90/2003, consolidated text 158a of 1 October 2026, Articles 1, 2, 3, 57, 59, 67, 71, 93, 108; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/2003090.html | 2026-10-30 |
| Read for VAT Act 50/1988, Articles 4, 14, 24; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1988050.html | 2026-10-30 |
| Read for Act 4/1995 on Municipal Revenue, Article 23; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1995004.html | 2026-10-30 |
| Read for Act 113/1990 on the Payroll Levy, Article 2; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1990113.html | 2026-10-30 |
| Read for Act 129/1997 on Pension Funds, Article 2 (15.5%); not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1997129.html | 2026-10-30 |
| Read for Annual Accounts Act 3/2006, Article 109; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/2006003.html | 2026-10-30 |
| Read for Advertisement 1521/2025: 2026 annual bands, rates, 14.94% and the personal credit | https://island.is/stjornartidindi/nr/34903c0c-a215-46e9-878c-b1ecff73af7d | 2026-11-14 |
| Read for Skatturinn (English), key rates and amounts 2026: monthly bands, credit, VAT 24% and 11% | https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/ | 2026-11-14 |
| Read for Skatturinn, key figures and rates 2026: child rate, capital income tax and allowances, company rates 20% and 37.6% | https://www.skatturinn.is/einstaklingar/helstutolur/2026/ | 2026-11-14 |
| Read for Skatturinn, capital income tax: 22% and the listed-share condition | https://www.skatturinn.is/einstaklingar/skattar-og-gjold/fjarmagnstekjuskattur/ | 2026-11-14 |
| Read for Skatturinn, notice of 30 January 2026: legal-entity returns 2026, deadline 31 May, extension to 21 September | https://www.skatturinn.is/um-rsk/frettir-og-tilkynningar/opnad-fyrir-skil-a-skattframtali-logadila-2026 | 2026-11-14 |
| Read for Skatturinn, filing a tax return (individuals, 2026 deadline 13 March) | https://www.skatturinn.is/english/individuals/filing-a-tax-return/ | 2026-11-14 |
| Read for Skatturinn, payroll levy (tryggingagjald): 2026 components 4.90%, 1.35%, 0.05%, 0.05% | https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald | 2026-11-14 |
| Read for Skatturinn, employer register: withholding due 1st, final due 15th | https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/ | 2026-11-14 |
| Read for Skatturinn, employer notice 1/2026 (RSK 6.01): levy 6.35% and parts, 11.5% employer pension default | https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf | 2026-11-14 |
| Read for Skatturinn, VAT general page: ISK 2,000,000, two-month periods, ISK 4,000,000 annual settlement | https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/almennt-um-vsk/ | 2026-11-14 |
| Read for Skatturinn, guide to VAT registration: due date one month and five days after the period | https://www.skatturinn.is/media/baeklingar/VSK_Skraning_a_vsk_skra.pdf | 2026-11-14 |
| Read for Skatturinn, transfer pricing (milliverðlagning): ISK 1 billion documentation line | https://www.skatturinn.is/atvinnurekstur/skattskylda/milliverdlagning/ | 2026-11-14 |
| Read for Skatturinn, all taxes and charges: 1% a day surcharge, cap 10% | https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/ | 2026-11-14 |
| Read for Skatturinn, private limited companies (company register) | https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/ | 2026-11-14 |

Not yet confirmed: the Alþingi texts as at 14 Nov 2026 (403 today), so the 15.5% minimum pension contribution, the 12.44% to 14.97% municipal range and the Article 108 15% estimate surcharge rest on the 30 Oct 2026 reading; the 2027 filing deadlines for 2026 income (Skatturinn has not yet published them); the 2026 reduced payroll-levy rate for workers with an A1 certificate (Skatturinn's levy page gives rates up to wage year 2025 only; see `iceland-social-contributions`).
