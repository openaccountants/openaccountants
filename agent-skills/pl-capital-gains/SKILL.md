---
name: pl-capital-gains
description: "Polish tax on investment income and capital gains of individuals for tax year 2026: the 19% flat tax on interest and dividends (PIT Act art. 30a) and on gains from shares, securities, derivatives and fund units (art. 30b), 19% on crypto-asset gains with unused costs carried forward without limit (art. 30b ust. 1a), losses on securities over five years, 19% on property sold within five years of the end of the year of purchase (art. 30e) and the housing relief (art. 21 ust. 1 pkt 131), credit for foreign tax (art. 30a ust. 9, art. 30b ust. 5a and 5e), the 4% solidarity levy, and the PIT-38 and PIT-39 returns due 30 April 2027. Trigger on: Belka tax, podatek od zysków kapitałowych, PIT-38, PIT-39, PIT-8C, kryptowaluty podatek, sprzedaż mieszkania przed 5 latami, ulga mieszkaniowa. Out of scope: business income (pl-income-tax), non-residents and exit tax (pl-cross-border), companies (pl-cit-corporate-tax)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pl-capital-gains"
  jurisdiction: "PL"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Poland: capital gains and investment income of individuals (2026)

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

This skill covers the flat 19% taxes on an individual's savings, investments, crypto-assets and private property sales. It links to the other Poland skills and does not repeat them:

- [pl-income-tax](pl-income-tax.md): the scale, the flat tax on business income, ryczałt, residence basics and the solidarity levy return (DSF-1).
- [pl-cross-border](pl-cross-border.md): non-residents, withholding on payments abroad, treaty relief and the individual exit tax.
- [pl-cit-corporate-tax](pl-cit-corporate-tax.md): companies, including dividends paid by a Polish company.

**Which text of the law.** PIT Act (ustawa o podatku dochodowym od osób fizycznych), consolidated text Dz.U. 2026 poz. 592. Tax Ordinance, Dz.U. 2026 poz. 622.

## Who this applies to

- **Residents.** Individuals resident in Poland pay on worldwide investment income and gains (PIT Act art. 3 ust. 1). Residence tests are in [pl-income-tax](pl-income-tax.md).
- **Non-residents.** They pay only on Polish-source income, subject to treaties. A treaty rate or exemption needs a certificate of residence (art. 30b ust. 3). See [pl-cross-border](pl-cross-border.md).
- **Private investors only.** Gains on shares and securities made in a business are business income, not art. 30b income (art. 30b ust. 4). Property sold in a business, or by a developer, is outside art. 30e (art. 30e ust. 6).
- **Out of scope.** Individual savings accounts (IKE, IKZE, PPK), CFC income (art. 30f), the exit tax on unrealised gains (art. 30da) and inheritance and gift tax.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Interest, bond discount, deposit income, dividends, fund distributions | 19% of the revenue, no costs | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf (art. 30a ust. 1 pkt 1-5) |
| Gains on securities, derivatives, shares, cooperative shares, contributions in kind, fund units | 19% of income (revenue minus costs) | 2026 | same, art. 30b ust. 1-2 |
| Gains on crypto-assets (waluty wirtualne) | 19% of income | 2026 | same, art. 30b ust. 1a-1b |
| Private sale of property or property rights within five years from the end of the year of purchase or building | 19% of income | 2026 | same, art. 10 ust. 1 pkt 8, art. 30e ust. 1 |
| Private sale of other things (for example a car) within six months from the end of the month of purchase | taxed on the scale with other income | 2026 | same, art. 10 ust. 1 pkt 8 lit. d |
| Housing relief: time to spend the sale proceeds on own housing | the year of sale and the next three years | 2026 | same, art. 21 ust. 1 pkt 131 |
| Loss carry-forward, securities and shares | 5 years; at most 50% of the loss a year, or one deduction up to PLN 5,000,000 | 2026 | same, art. 9 ust. 3, 6 |
| Solidarity levy (danina solidarnościowa) | 4% of income above PLN 1,000,000, art. 30b income included | 2026 | same, art. 30h ust. 1-2 |
| Late payment interest | 10.50% a year from 5 March 2026; reduced 5.25% | 2026 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf; Tax Ordinance art. 56 § 1 |

## The taxable base

**Interest and dividends (art. 30a).** Tax is 19% of the gross amount; no costs are deducted. A Polish payer (bank, broker, company) withholds it, and the investor does nothing more. Interest, dividends and fund distributions from abroad are reported in the PIT-38, with the foreign tax credited up to 19% (art. 30a ust. 9 and 11, art. 45 ust. 3b-3c).

**Securities, shares and funds (art. 30b).** Income is the year's total revenue from disposals minus the costs of acquiring what was sold (art. 30b ust. 2, art. 22 ust. 1f, art. 23 ust. 1 pkt 38). Fees and commissions count as costs. Where the units sold cannot be identified, the earliest bought are treated as sold first (FIFO), separately for each investment account (art. 30b ust. 7-7a). This income is not added to scale or flat-tax income (art. 30b ust. 5). Losses on securities, shares, derivatives and fund units are carried forward five years under art. 9 ust. 3 and 6 against income of the same source. Polish brokers send a PIT-8C by the end of February; it lists revenue and costs but no tax is withheld.

**Crypto-assets (art. 30b ust. 1a).** Income is revenue from exchanging crypto for money, goods, services or other property rights, minus documented acquisition and disposal costs (art. 17 ust. 1f, art. 22 ust. 14). Crypto-to-crypto swaps are not a disposal and give no cost (art. 23 ust. 1 pkt 38d). Costs not used in the year (because they exceed revenue) are carried to the next year with no time limit (art. 22 ust. 16); there is no "loss" in the art. 9 sense (art. 9 ust. 3a pkt 2). Crypto income is taxed separately from other art. 30b income (art. 30b ust. 5d), but both go on the PIT-38. Costs must be reported even in a year with no crypto revenue (art. 30b ust. 6a).

**Property sold within five years (art. 30e).** The five years run from the end of the calendar year of purchase or building. Revenue is the contract price minus the costs of sale, such as agent and notary fees (art. 19 ust. 1). Costs are the documented purchase or building cost plus improvements (art. 22 ust. 6c), increased by any depreciation taken (art. 30e ust. 2). Property received by inheritance or gift has no purchase cost; inheritance and gift tax paid can count (art. 22 ust. 6d). Losses on property cannot be carried forward (art. 9 ust. 3a pkt 1).

**Housing relief (art. 21 ust. 1 pkt 131).** The exempt part of the income is income x (housing spending / revenue). Qualifying spending is made from the day of sale to the end of the third year after the year of sale on buying or building a home or land for one, renovating one's own home, or repaying a housing loan taken before the sale, in the EU, EEA or Switzerland (art. 21 ust. 25-30a). Holiday homes do not count (art. 21 ust. 28). If the money is not spent as declared, the seller files a correction and pays tax with interest (art. 30e ust. 7).

**Rounding.** The base and the tax are rounded to whole złoty, 50 grosze and above up (Tax Ordinance art. 63 § 1).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| PIT-8C from Polish brokers and other payers | to the investor by 28 February 2027 | PIT Act art. 39 ust. 3, art. 42g ust. 1 |
| PIT-38 for 2026 (securities, shares, funds, crypto, foreign dividends and interest) and payment | 15 February to 30 April 2027 | art. 45 ust. 1, 1a pkt 1, ust. 4 pkt 2 |
| PIT-39 for 2026 (property sold within five years), including a sale fully covered by the housing relief, and payment | 15 February to 30 April 2027 | art. 30e ust. 4, art. 45 ust. 1a pkt 3, ust. 4 pkt 4 |
| Solidarity levy (DSF-1) and payment | 30 April 2027 | art. 30h ust. 4 |
| Withholding on Polish interest and dividends | at payment, by the payer | art. 41 ust. 4 |

Returns are filed through e-Urząd Skarbowy (Twój e-PIT). Spouses cannot file PIT-38 or PIT-39 jointly; each files their own share (art. 6 ust. 1; joint filing in art. 6 ust. 2 covers scale income only, and art. 30b ust. 5 and art. 30e ust. 5 keep this income separate).

## Penalties and interest

- **Late payment interest.** 10.50% a year from 5 March 2026, when the NBP lombard rate fell to 4.25% (M.P. 2026 poz. 269; Tax Ordinance art. 56 § 1). Reduced to 5.25% if a correction is filed within 6 months of the deadline and the tax paid within 7 days (art. 56a).
- **Housing relief not used.** Tax on the part that was claimed exempt, plus interest from the day after the original payment deadline (art. 30e ust. 7).
- **Fiscal Penal Code.** Not filing a PIT-38 or PIT-39, or filing a false one, is a fiscal offence or petty offence depending on the amount (Fiscal Penal Code art. 54, 56). A valid correction (art. 16a) or voluntary disclosure (art. 16) made before the authority acts removes liability.

## Cross-border points

- **Foreign gains.** Gains through a foreign broker are added to Polish gains; foreign tax is credited up to the Polish tax on that part (art. 30b ust. 5a-5b; for crypto ust. 5e-5f). Most treaties leave gains on shares to the country of residence, so foreign tax on them is rare.
- **Foreign dividends and interest.** Polish tax is 19% of the gross amount, less foreign tax paid, capped at 19% (art. 30a ust. 9). Where the foreign country withheld more than the treaty rate, the excess is claimed back there, not in Poland.
- **Foreign property.** Gains on property abroad sold within five years are taxed in Poland unless a treaty exempts them; foreign tax is credited proportionally (art. 30e ust. 8-9).
- **Currency.** Revenue and costs in foreign currency are converted at the NBP average rate of the last working day before the day of revenue or cost (art. 11a ust. 1-2).
- **Moving abroad.** Unrealised gains may be taxed under the individual exit tax; see [pl-cross-border](pl-cross-border.md).

## Worked examples

### Example 1: shares, a carried loss and a US dividend

Piotr, a Polish resident, sold shares in 2026 for PLN 120,000. They cost PLN 90,000 including fees. He has a PLN 10,000 loss on shares from 2024 that he has not used yet. As the loss is under PLN 5,000,000 he deducts all of it in one go (art. 9 ust. 3 pkt 2). He also received a US dividend of PLN 2,000 gross through a foreign broker; the US withheld 15%, PLN 300.

Income on shares: 120,000 - 90,000 - 10,000 = PLN 20,000. Tax at 19%: PLN 3,800. On the dividend, Polish tax is 19% of 2,000 = PLN 380, less the US tax of PLN 300: PLN 80 more. Piotr pays PLN 3,880 with his PIT-38 by 30 April 2027.

```oa-check
name: Piotr, PIT-38 2026, shares with carried loss and US dividend
inputs:
  revenue: 120000
  costs: 90000
  loss_2024: 10000
  dividend: 2000
  us_tax: 300
steps:
  - income: revenue - costs
  - loss_used: min(loss_2024, 5000000, income)
  - base: round(income - loss_used, 0)
  - tax_shares: round(base * 0.19, 0)
  - pl_div_tax: dividend * 0.19
  - div_extra: pl_div_tax - min(us_tax, pl_div_tax)
  - total: tax_shares + div_extra
expected:
  base: 20000
  tax_shares: 3800
  div_extra: 80
  total: 3880
```

### Example 2: crypto with carried costs, and a flat sold within five years

Anna bought crypto in 2025 for PLN 8,000 and sold nothing that year, so she reported PLN 8,000 of unused costs. In 2026 she buys more for PLN 20,000 and sells crypto for PLN 50,000. Income: 50,000 - 20,000 - 8,000 = PLN 22,000, tax PLN 4,180 on her PIT-38.

She also sells a flat bought in 2023 for PLN 500,000. The five years end on 31 December 2028, so the 2026 sale is taxed. The price is PLN 720,000; agent and notary fees are PLN 20,000, so revenue is PLN 700,000 and income PLN 200,000. By 2029 she spends PLN 420,000 on a new home. The exempt part is 200,000 x 420,000 / 700,000 = PLN 120,000. The taxable PLN 80,000 bears PLN 15,200 at 19%, due with her PIT-39 by 30 April 2027.

```oa-check
name: Anna, 2026, crypto with carried costs and a flat with housing relief
inputs:
  crypto_revenue: 50000
  crypto_costs_2026: 20000
  crypto_costs_carried: 8000
  price: 720000
  sale_costs: 20000
  purchase_cost: 500000
  housing_spend: 420000
steps:
  - crypto_income: crypto_revenue - crypto_costs_2026 - crypto_costs_carried
  - crypto_tax: round(crypto_income * 0.19, 0)
  - property_revenue: price - sale_costs
  - property_income: property_revenue - purchase_cost
  - exempt: property_income * min(housing_spend, property_revenue) / property_revenue
  - taxable: round(property_income - exempt, 0)
  - property_tax: round(taxable * 0.19, 0)
expected:
  crypto_income: 22000
  crypto_tax: 4180
  exempt: 120000
  taxable: 80000
  property_tax: 15200
```

## Ask the client first

1. Were they resident in Poland for all of 2026? Any foreign brokers, exchanges or bank accounts?
2. The PIT-8C forms received, and for foreign accounts a list of every disposal with dates, proceeds, costs and currency.
3. Losses on securities from 2021-2025 already used, and crypto costs carried from 2025.
4. For property: the year of purchase or building (or of inheritance), the price, sale costs and improvements; was it used in a business?
5. Do they plan to spend the proceeds on a home, or repay a housing loan, by the end of 2029?
6. Total 2026 income above PLN 1,000,000 across scale, flat-tax and capital income (solidarity levy)?

## Sources

| Source | URL | Read on |
|---|---|---|
| PIT Act, consolidated text Dz.U. 2026 poz. 592 (art. 3, 9, 10, 11a, 17, 19, 21 ust. 1 pkt 131 and ust. 25-30a, 22, 23, 30a, 30b, 30e, 30h, 39, 41, 42g, 45) | https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf | 2026-10-23 |
| Tax Ordinance, Dz.U. 2026 poz. 622 (art. 56, 56a, 63) | https://api.sejm.gov.pl/eli/acts/DU/2026/622/text.pdf | 2026-10-23 |
| Minister of Finance notice on late payment interest, M.P. 2026 poz. 269 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf | 2026-10-23 |
| Fiscal Penal Code, Dz.U. 2025 poz. 633 (art. 16, 16a, 54, 56) | https://api.sejm.gov.pl/eli/acts/DU/2025/633/text.pdf | 2026-10-23 |
| NBP base rates archive (lombard rate 4.25% from 5 March 2026) | https://static.nbp.pl/dane/stopy/stopy_procentowe_archiwum.xml | 2026-10-23 |
| PIT Act amendments after poz. 592: Dz.U. 2026 poz. 779, 846, 1079 (none touches art. 9, 21 ust. 1 pkt 131, 22 ust. 14-16, 30a, 30b, 30e or 45) | https://api.sejm.gov.pl/eli/acts/DU/2026/592/references | 2026-10-23 |
| Ministry of Finance, PIT forms (PIT-38, PIT-39) | https://www.podatki.gov.pl/podatki-osobiste/pit/formularze-pit | 2026-10-23 |

Not yet confirmed: treaty treatment of gains is described in general terms; check the specific treaty.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pl-capital-gains` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pl-capital-gains. If neither is available, confirm every figure against the official source pages cited above before relying on it.
