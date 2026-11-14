---
name: me-tax-overview
description: "A one-page map of the Montenegrin tax system for tax year 2026, read from the laws published in the Official Gazette and on gov.me. Covers the calendar tax year, the euro, the Tax Administration (Poreska uprava) and its IRMS portal, who is resident, personal income tax at 0%, 9% and 15% (monthly salary bands EUR 700 and 1,000; annual business bands EUR 8,400 and 12,000), 15% on most other income and 12% on gambling winnings from 21 May 2026, the municipal surtax caps, corporate profit tax at 9%, 12% and 15% (bands EUR 100,000 and 1,500,000), withholding at 15% and 30%, VAT at 21%, 15%, 7% and 0% with EUR 30,000 registration, social contribution rates, the main filing deadlines and late-payment interest. Use for how does tax work in Montenegro, Montenegro tax overview, Montenegro tax rates 2026. Detail sits in montenegro-income-tax, me-corporate-income-tax, montenegro-vat, montenegro-social-contributions, montenegro-payroll, me-cross-border, me-transfer-pricing and me-company-formation."
version: 1.0
jurisdiction: ME
category: international
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: situation-rules
---

# Montenegro Tax Overview

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Montenegro taxes salaries at 0%, 9% and 15% (monthly bands EUR 700 and 1,000), a sole trader's main business at 0%, 9% and 15% (annual bands EUR 8,400 and 12,000), company profit at 9%, 12% and 15% (bands EUR 100,000 and 1,500,000), and supplies under VAT at 21% standard. The tax year is the calendar year and the currency is the euro. This is a map: each line names the skill in the pack that carries the full rules, and the domain skill wins if the two differ.

Several laws below are read from the Ministry of Finance's consolidated texts on gov.me (wapi.gov.me). A consolidation is a working text; the official text is the one in the Official Gazette (Službeni list Crne Gore). On 2026-11-14 wapi.gov.me refused every connection from here, so those rows keep their 2026-10-30 read date and were not reopened; see Sources.

## Who this applies to

- **Standard tax year.** Companies: the tax period is the financial year, which "je kalendarska godina", except on liquidation, a status change or a start of business during the year _(Corporate Profit Tax Law, art. 39(1)-(2))_. Individuals: income is taxed by calendar year, and the annual return covers "prethodnu godinu" _(PIT Law, art. 43(2))_. Detail: [me-corporate-income-tax](me-corporate-income-tax.md), [montenegro-income-tax](montenegro-income-tax.md).
- **Currency.** Euro (EUR). The tax laws state their amounts in euros; for example the first corporate band is "do 100.000,00 eura" _(Corporate Profit Tax Law, art. 28(2))_.
- **Tax authority.** The Tax Administration (Poreska uprava). Since 12 January 2026 returns are filed in its IRMS portal (https://irms.tax.gov.me/); the old CRPS and TAXIS portals closed on 31 December 2025 _(Tax Administration IRMS notice, 30 December 2025)_. The same authority keeps the business register (CRPS) and the register of beneficial owners: see [me-company-formation](me-company-formation.md).
- **Resident individuals.** A person with a domicile or a centre of business and vital interests in Montenegro, or who stays in Montenegro more than 183 days in the tax year. A person sent abroad to work for a Montenegrin resident or for an international organisation is also resident _(PIT Law, art. 3)_.
- **Resident companies.** A legal person incorporated in Montenegro, or with its seat of actual management and control in Montenegro _(Corporate Profit Tax Law, art. 3(1))_. A non-resident is taxed through a permanent establishment _(art. 3(2))_.
- **Basis of taxation.** Residents are taxed on income earned "u Crnoj Gori i izvan Crne Gore" (in and outside Montenegro); non-residents only on income earned in Montenegro _(PIT Law, art. 4; Corporate Profit Tax Law, art. 4(1)-(2))_.
- **Out of scope:** the lump-sum scale, property tax, excise, real estate transfer tax and treaty rates by country.

### Which skill to use

| Question | Skill |
|---|---|
| A resident's or non-resident's income tax, business profit, rent, capital income, gambling, the GPP-FL return | [montenegro-income-tax](montenegro-income-tax.md) |
| Company profit tax, depreciation, losses, incentives, the PD return | [me-corporate-income-tax](me-corporate-income-tax.md) |
| VAT rates, registration, the monthly return, reverse charge, refunds | [montenegro-vat](montenegro-vat.md) |
| Pension and unemployment contributions, entrepreneurs, the annual ceiling | [montenegro-social-contributions](montenegro-social-contributions.md) |
| Gross to net, surtax, Chamber dues, the IOPPD report | [montenegro-payroll](montenegro-payroll.md) |
| Withholding on payments abroad, permanent establishments, treaties, foreign tax credit | [me-cross-border](me-cross-border.md) |
| Related-party prices and documentation | [me-transfer-pricing](me-transfer-pricing.md) |
| d.o.o. or a.d., share capital, CRPS registration, annual accounts | [me-company-formation](me-company-formation.md) |
| Lawful ways to lower the tax bill | [montenegro-tax-optimization](montenegro-tax-optimization.md) |

## Rates, bands and thresholds

| Item | Figure (2026) | Conditions | Source |
|---|---|---|---|
| PIT on salary | 0% to EUR 700; 9% EUR 700.01 to 1,000; 15% above EUR 1,000 | Monthly taxable income (PIT Law art. 10(1)(1)) | PIT Law consolidation through 160/25: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 |
| PIT on a principal independent activity | 0% to EUR 8,400; 9% EUR 8,400.01 to 12,000; 15% above EUR 12,000 | Annual (art. 10(1)(2)) | same |
| PIT on other income | 15% | Supplementary self-employment, property, property rights, capital income, capital gains and the other classes in art. 12(2) points 3 to 9 (art. 10(1)(3)) | same |
| PIT on gambling winnings from 21 May 2026 | 12% flat | Replaces the 0% / 10% / 15% scale that applied to 20 May 2026 (art. 10(1)(4); Official Gazette 70/26, arts. 1 and 3) | Official Gazette 70/26: https://www.sluzbenilist.me/propisi/394390/download |
| Municipal surtax (prirez), cap | Up to 13% of the tax; up to 15% in Podgorica and Cetinje | Each municipality sets its own rate (Local Self-Government Financing Law arts. 8, 9) | Local Self-Government Financing Law through 149/25: https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 |
| Corporate profit tax | 9% to EUR 100,000; EUR 9,000 + 12% of the excess to EUR 1,500,000; EUR 177,000 + 15% of the excess above | Taxable profit (Corporate Profit Tax Law art. 28); the 104/26 amendments apply from 1 January 2027 | Corporate Profit Tax Law consolidation through 88/24: https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0 |
| Withholding on payments to non-residents | 15% of the gross amount | Dividends, interest, royalties, capital gains, rent, consulting, market research and audit fees (art. 29(1), (4)) | same |
| Withholding, listed low-tax territories | 30% | Recipient from a listed territory (art. 29(5)-(7)); a treaty rate only with proof of treaty residence and beneficial ownership (art. 29a(1)) | same |
| VAT, standard rate | 21% | VAT Law art. 24 | VAT Law consolidation through 12/26: https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0 |
| VAT, reduced rates | 7% and 15% | Listed goods and services (art. 24a(1)-(2)) | same |
| VAT, zero rate | 0% | Exports and the other supplies in art. 25(1) | same |
| VAT registration threshold | EUR 30,000 | Supplies in the last 12 months or a shorter period; apply by the 20th of the following month (art. 55(1)) | same |
| Pension and disability contribution | Employee 10%; employer 0% | Contributions Law art. 15(1) | Contributions Law through 160/25: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 |
| Unemployment insurance | Employee 0.5%; employer 0.5% | Art. 18(1); no health insurance contribution is listed (art. 2) | same |
| Labour Fund | Employer 0.2% | Ministry of Finance payroll Instruction, art. 5 | Payroll Instruction: https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0 |
| Late-payment interest, 1 January to 17 July 2026 | 0.03% a day | Tax Administration Law art. 95(1), text before 104/26 | Tax Administration Law before 104/26: https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0 |
| Late-payment interest, 18 July to 31 December 2026 | 5.4% a year | Art. 95 as changed by 104/26; Tax Administration decision of 24 July 2026 | Decision of 24 July 2026: https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 |

## The base

- **Individuals.** Income is grouped by class (art. 12(2) of the PIT Law): employment, independent activity, property, property rights, capital income, capital gains, gambling and the others. Salary is taxed monthly through the employer; a principal independent activity is taxed on annual profit; other classes at 15%. A small sole trader may instead pay an annual lump sum: see [montenegro-tax-optimization](montenegro-tax-optimization.md).
- **Companies.** Taxable profit is the accounting profit adjusted under the Corporate Profit Tax Law. Depreciation, losses and incentives are in [me-corporate-income-tax](me-corporate-income-tax.md).
- **VAT.** Supplies of goods and services in Montenegro and imports. Exemptions, reverse charge and refunds are in [montenegro-vat](montenegro-vat.md).
- **Contributions.** Charged on gross salary; for entrepreneurs on a base set by turnover. See [montenegro-social-contributions](montenegro-social-contributions.md).

## Deadlines and filing

| Return | Deadline | Source |
|---|---|---|
| Corporate profit tax return (PD) and payment | Within three months after the end of the tax period: 31 March 2027 for 2026; balance sheet and income statement go with it (Corporate Profit Tax Law art. 40(3)-(4)) | Corporate Profit Tax Law |
| Annual personal income tax return (GPP-FL) | End of April for the previous year: 30 April 2027 for 2026 (PIT Law art. 43(2)) | PIT Law |
| VAT return | Monthly, electronically, by the 15th of the month after the period, even with no VAT due (VAT Law art. 35(1)-(3)); payment by the 15th (art. 36(1)) | VAT Law |
| Payroll report (IOPPD) | By the 15th of the current month for the previous month (PIT Law art. 47(3)) | PIT Law |
| Annual financial statements | By 31 March for the previous year: see [me-company-formation](me-company-formation.md) | Accounting Law |

## Penalties and interest

- **Late payment.** Interest at 0.03% a day ran from 1 January to 17 July 2026 (Tax Administration Law art. 95(1), text before 104/26). Official Gazette 104/26 changed art. 95 and the Tax Administration set the rate at 5.4% a year for 18 July to 31 December 2026 (decision of 24 July 2026). Split a 2026 late period at 17/18 July.
- **Fines.** Late or false business registration, late annual accounts and late beneficial owner entries carry fixed fines: see [me-company-formation](me-company-formation.md). Tax misdemeanour fines under the Tax Administration Law are not restated here.

## Cross-border points

- Non-residents are taxed only on Montenegrin income (PIT Law art. 4; Corporate Profit Tax Law art. 4(2)).
- Payments abroad: 15% withholding, 30% to listed low-tax territories, treaty rates only with proof of residence and beneficial ownership (art. 29, 29a). Detail: [me-cross-border](me-cross-border.md).
- Related-party prices: [me-transfer-pricing](me-transfer-pricing.md).

## Two worked examples that recompute

**Example 1: salary of EUR 1,500 a month (taxable).** The first EUR 700 is at 0%, the next EUR 300 at 9% (EUR 27) and the EUR 500 above EUR 1,000 at 15% (EUR 75): PIT of EUR 102 a month, before the municipal surtax. In Podgorica, at the 15% cap, the surtax would add 15% of EUR 102 (EUR 15.30), but use the municipality's actual rate.

```oa-check
name: Montenegro 2026 monthly salary PIT on EUR 1,500
inputs:
  taxable: 1500
steps:
  - band_9: (min(taxable, 1000) - 700) * 0.09
  - band_15: max(0, taxable - 1000) * 0.15
  - pit: band_9 + band_15
  - surtax_at_cap_15: pit * 0.15
expected:
  band_9: 27.00
  band_15: 75.00
  pit: 102.00
  surtax_at_cap_15: 15.30
```

**Example 2: company profit of EUR 2,000,000.** The fixed amount for the top band is EUR 177,000 (9% of 100,000 plus 12% of 1,400,000), plus 15% of the EUR 500,000 above EUR 1,500,000 (EUR 75,000): corporate tax of EUR 252,000, an effective 12.6%.

```oa-check
name: Montenegro 2026 corporate profit tax on EUR 2,000,000
inputs:
  profit: 2000000
steps:
  - fixed_top: 100000 * 0.09 + 1400000 * 0.12
  - tax: fixed_top + (profit - 1500000) * 0.15
  - effective_pct: tax / profit * 100
expected:
  fixed_top: 177000.00
  tax: 252000.00
  effective_pct: 12.60
```

## Ask the client first

1. Individual or company? For an individual: resident (domicile, vital interests, more than 183 days)?
2. Which income: salary, a principal or supplementary independent activity, rent, capital income, gambling?
3. Which municipality (for the surtax rate)?
4. Supplies in the last 12 months (VAT registration at EUR 30,000)?
5. Any payment to a non-resident, and from which country?

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Tax Law, Ministry of Finance consolidation through 160/25: read for arts. 3, 4, 10, 12, 43 and 47 (not reopened: wapi.gov.me refused connections on 2026-11-14) | https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 | 2026-10-30 |
| Law amending the Personal Income Tax Law, Official Gazette 70/26: read for arts. 1 and 3 (12% on gambling winnings, in force 21 May 2026) | https://www.sluzbenilist.me/propisi/394390/download | 2026-11-14 |
| Corporate Profit Tax Law, consolidation through 88/24: read for arts. 3, 4, 28, 29, 29a, 39 and 40 (not reopened, as above) | https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0 | 2026-10-30 |
| Law amending the Corporate Profit Tax Law, Official Gazette 104/26: read for its application from 1 January 2027 (not reopened, as above) | https://wapi.gov.me/download/8951908b-625c-4219-aefe-0c86501ddaf8?version=1.0 | 2026-10-30 |
| VAT Law, consolidation through 12/26: read for arts. 24, 24a, 25, 35, 36 and 55 (not reopened, as above) | https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0 | 2026-10-30 |
| Law on Compulsory Social Insurance Contributions through 160/25: read for arts. 2, 15 and 18 (not reopened, as above) | https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 | 2026-10-30 |
| Ministry of Finance payroll Instruction: read for art. 5 (Labour Fund 0.2%) (not reopened, as above) | https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0 | 2026-10-30 |
| Local Self-Government Financing Law through 149/25: read for arts. 8 and 9 (surtax caps) (not reopened, as above) | https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 | 2026-10-30 |
| Tax Administration Law, text before 104/26: read for art. 95 (0.03% a day) (not reopened, as above) | https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0 | 2026-10-30 |
| Law amending the Tax Administration Law, Official Gazette 104/26: read for arts. 20 and 26 (not reopened, as above) | https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0 | 2026-10-30 |
| Tax Administration decision of 24 July 2026 on the late-payment interest rate: read for 5.4% a year from 18 July to 31 December 2026 (not reopened, as above) | https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 | 2026-10-30 |
| Tax Administration notice on the start of IRMS, 30 December 2025: read for the 12 January 2026 start and the closing of CRPS and TAXIS portals (not reopened: gov.me refused connections on 2026-11-14) | https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms | 2026-10-30 |

Not yet confirmed: every figure on a wapi.gov.me or gov.me row was read on 2026-10-30 and could not be reopened on 2026-11-14 (the server refused connections from curl, and no 2026 web.archive.org copy exists), so re-read them in a browser before relying on them; each municipality's 2026 surtax rate (only the 13% and 15% caps are confirmed); the art. 49 lump-sum scale for small entrepreneurs; the 2026 annual pension contribution ceiling; treaty withholding rates by country.
