---
name: lv-cross-border
description: "Hub skill for crossing the Latvian border in tax year 2026. Covers tax residence for individuals (declared home, or 183 days in any 12-month period, Law On Taxes and Fees section 14) and companies (incorporated under Latvian law); permanent establishment, including services over 30 days in any 6 months; Latvian-source income of non-residents; corporate income tax withholding on payments to non-residents (20% on management and consulting fees, 3% on real estate sales, 5% on real estate rent, 20% on all payments to low-tax or no-tax jurisdictions); treaty relief and the non-resident's net-basis refund report; foreign tax credit; the exit charge when assets leave Latvian taxing rights. Trigger on: moving to Latvia, leaving Latvia, non-resident, nerezidents, withholding tax Latvia, management fee withholding, low-tax jurisdiction, residence certificate, permanent establishment, exit tax. Out of scope: personal income tax detail (latvia-income-tax), corporate income tax (lv-corporate-income-tax), social contributions (latvia-social-contributions), payroll (latvia-payroll), VAT (latvia-vat-return)."
jurisdiction: LV
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Latvia: cross-border tax for people and companies (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure below comes from the consolidated texts of the Corporate Income Tax Law, the Law On Personal Income Tax and the Law On Taxes and Fees published on likumi.lv, in the versions in force for 2026 (including the amendments of 3 December 2025 in force from 1 January 2026). It prepares working papers; it is not authority to file or pay.

This is the hub for the Latvian cross-border (XB) domain. It summarises and links rather than repeating other skills:

- Personal income tax, rates and the annual declaration: [latvia-income-tax](latvia-income-tax.md).
- Corporate income tax on distributed profit: [lv-corporate-income-tax](lv-corporate-income-tax.md).
- Social contributions: [latvia-social-contributions](latvia-social-contributions.md). Payroll: [latvia-payroll](latvia-payroll.md).
- VAT: [latvia-vat-return](latvia-vat-return.md). Overview: [lv-tax-overview](lv-tax-overview.md). Entity choice: [lv-company-formation](lv-company-formation.md).

Those skills still carry 2025 figures. Where this skill and a 2025 skill disagree for 2026, this skill cites the 2026 law text.

The laws are the Corporate Income Tax Law (Uzņēmumu ienākuma nodokļa likums, "CIT Law"), the Law On Personal Income Tax (likums "Par iedzīvotāju ienākuma nodokli", "PIT Law") and the Law On Taxes and Fees (likums "Par nodokļiem un nodevām", "LTF"). The tax authority is the State Revenue Service (Valsts ieņēmumu dienests, VID). Currency: euro.

## Who this applies to

**Individuals.** A person is Latvian resident if any one of these is true (LTF section 14(2)):

- their declared place of residence is in Latvia; or
- they stay in Latvia for 183 days or more in any 12-month period that starts or ends in the tax year; or
- they are a Latvian citizen employed abroad by the Latvian government.

**Part year under the 183-day test** (LTF section 14(3)):

- A person who was not resident in the previous year becomes resident from the date they first arrived in Latvia.
- A person who will not be resident in the following year stops being resident from the date they left. This only applies if after that date they have closer ties with another country than with Latvia: property owned abroad, family living abroad, or social insurance paid abroad.

A resident is taxed on income from Latvia and abroad. A non-resident is taxed only on income earned in Latvia (PIT Law section 2; LTF section 14(5)). Where a treaty sets a different rule, the treaty applies (PIT Law section 24(1)).

**Companies.** A taxpayer other than an individual is resident if it was, or had to be, formed and registered under Latvian law (LTF section 14(4)). Anyone else is a non-resident (section 14(5)). The CIT Law taxes three groups (CIT Law section 2(1)):

- domestic companies;
- permanent establishments of non-residents;
- foreign companies and other persons earning income in Latvia ("non-residents").

**Permanent establishment.** A permanent establishment of a non-resident is treated as a separate domestic taxpayer for every tax law. It must register with VID (LTF section 14(6)). It exists in either of two cases.

- **Fixed place test** (section 14(7)). All three conditions are met at once: the non-resident uses a specific place of business in Latvia, it is used permanently or set up to be, and it is used for business.
- **Activity test** (section 14(8)). The non-resident does at least one of these in Latvia, whether or not there is a fixed place:
  - uses a building site, or does construction, assembly or installation work, or supervises or advises on it;
  - uses equipment, rigs or special vessels to explore or extract natural resources, or supervises or advises on that;
  - provides services, including consulting, management and technical services, through its own staff or hired personnel, for more than 30 days in total in any 6-month period;
  - uses a person who holds, and regularly uses (more than once in a tax period), authority to conclude contracts in its name.

A treaty can give a narrower definition; read the treaty article before relying on section 14(8).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Corporate income tax rate on distributed and deemed distributed profit | 20% of the base; the taxable object is first divided by 0.8 | 2026 | [CIT Law ss. 3(1), 4(9)](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Alternative rate on dividends of a company whose members are all individuals in the tax period in which the dividends are calculated (by choice) | 15%; object divided by 0.85; PIT of 6% withheld from the dividend. Covers calculated dividends only (s. 4(2)(1)(a)); deemed distributions stay at 20% after the 0.8 gross-up | 2026 (new, in force 1 January 2026) | CIT Law ss. 3(5), 4.2, 16(5); [PIT Law s. 15(5.1)](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Withholding on fees for management and consulting services paid to a non-resident | 20% of the fee | 2026 | CIT Law s. 5(1)(1), (5) |
| Withholding on payment for sale of Latvian real estate by a non-resident (includes shares in a company more than 50% of whose assets are Latvian real estate) | 3% of the payment | 2026 | CIT Law s. 5(1)(2), (2) |
| Withholding on rent or lease of Latvian real estate paid to a non-resident | 5% of the payment | 2026 | CIT Law s. 5(1)(4) |
| Withholding on all payments and dividends to persons in low-tax or no-tax jurisdictions (except goods and listed EU or EEA securities bought at market price) | 20% | 2026 | CIT Law s. 5(6) |
| Withholding on interest and on intellectual property payments to persons in low-tax or no-tax jurisdictions | 20% each | 2026 | CIT Law s. 5(8) |
| Payer that failed to withhold: its own extra CIT | base ÷ 0.8 × the withholding rate | 2026 | CIT Law s. 5(11) |
| Non-resident's optional net-basis report on management fees, real estate sale or rent | 20% on income less proven costs; report within 12 months of the transaction | 2026 | CIT Law ss. 5(4), 17(17) |
| Personal income tax rate, annual income up to the maximum social insurance contribution base | 25.5% | 2026 | PIT Law s. 15(2)(1) |
| Personal income tax rate, annual income above that base | 33% | 2026 | PIT Law s. 15(2)(2) |
| Additional rate on total annual income above EUR 200,000 | 3% | 2026 | PIT Law s. 15.1(1) |
| PIT on capital income and capital gains | 25.5% | 2026 | PIT Law s. 15(5) |
| PIT withheld from a non-resident individual's sale of Latvian real estate, where the payer withholds | 3% of the payment | 2026 | PIT Law ss. 3(3)(7.1), 15(7), 17(12) |
| PIT on a non-resident artist's, athlete's or coach's income, and on author's fees for literary, scientific or artistic works, discoveries, inventions and industrial designs | 25.5% | 2026 | PIT Law ss. 3(3)(3), (12)(a), 15(7.1) |
| PIT on other intellectual property payments to a non-resident individual | 5% | 2026 | PIT Law ss. 3(3)(12)(b), 15(8) |
| PIT withheld by individuals from payments to low-tax or no-tax jurisdictions | 25.5% | 2026 | PIT Law s. 17(17) |
| Optional rate for a foreign remote worker on a long-stay visa under Immigration Law s. 11(5), working for an employer or business registered in an OECD state | 15%, for 365 days from becoming resident | 2026 | PIT Law s. 15(19.2) |
| Permanent establishment through services | more than 30 days in any 6-month period | 2026 | [LTF s. 14(8)(3)](https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam) |
| Individual residence day count | 183 days in any 12-month period starting or ending in the tax year | 2026 | LTF s. 14(2)(2) |
| Late payment interest | 0.05% of the unpaid principal per day | 2026 | LTF s. 29(2) |
| Penalty on tax understated, found in a tax audit | 20% if the understatement is 15% or less of the tax due; 30% if more; halved if conditions in s. 32(7) are met | 2026 | LTF s. 32(4), (5), (7) |

## The taxable base

**Residents: income from Latvia and abroad.** An individual resident is taxed on worldwide income at the PIT Law rates; see [latvia-income-tax](latvia-income-tax.md). A Latvian company pays CIT only when it distributes profit or makes a deemed distribution (CIT Law section 4(2)). Profit earned abroad and kept in the company is not taxed until it is distributed.

**Non-resident individuals: income from Latvia only** (PIT Law section 3(3)). The main items:

- employment income for work in Latvia, including work for a foreign employer with no Latvian permanent establishment, and work abroad for a Latvian employer;
- professional services provided to Latvian residents or Latvian permanent establishments, in Latvia or abroad;
- income of artists, athletes and coaches from performing in Latvia, whoever receives it;
- board and council fees from a company registered in Latvia;
- income from using or selling Latvian real estate. A sale includes shares in a company where more than 50% of assets, directly or indirectly, is Latvian real estate (section 3(4));
- dividends, interest and intellectual property payments, unless exempt under section 9;
- Latvian pensions.

The payer withholds PIT from most of these items and pays it over by the 23rd of the following month (PIT Law section 17(12)). Latvian employers withhold on wages through payroll; see [latvia-payroll](latvia-payroll.md).

**Non-resident companies: income from Latvia** (CIT Law section 5(1)). Tax is withheld by Latvian residents (other than individuals) and by permanent establishments. It is withheld only where PIT has not been withheld from the same payment. Withholding applies to four groups of payment:

1. **Management and consulting fees: 20%.** These are services a non-resident provides, directly or through hired staff, to run a Latvian company or permanent establishment, or to advise it (section 5(5)).
2. **Real estate sale proceeds: 3%.** Where the buyer has no duty to withhold, the non-resident reports and pays 3% of the transaction value to VID within 30 days of the sale (section 5(3)).
3. **Real estate rent: 5%.**
4. **Payments to low-tax or no-tax jurisdictions: 20%** (section 5(6) and (8)). This applies to any payment, dividend, interest or royalty, including payments to a representative, to a third party's bank account, or by set-off. It does not apply to goods, or to listed EU or EEA securities, bought at market price. VID may allow a payer not to withhold under section 5(6) if the payer proves the payment is not made to reduce Latvian tax (section 5(9)). The list of jurisdictions is set by the Cabinet of Ministers (CIT Law section 4(10)).

Other payments to non-residents, such as ordinary dividends, interest and royalties to a company in a country not on the low-tax list, are not on the section 5(1) list. Latvia does not withhold CIT on them.

**Net-basis option.** A non-resident from an EU state or a treaty state that received a management fee, real estate proceeds or rent may file a report with VID. The report shows the costs related to that income, and tax is then charged at 20% on the net income (CIT Law section 5(4)). The report is due within 12 months of the transaction (section 17(17)). VID refunds the difference.

**Arriving.** An arriving individual is taxed at the normal rates from the date residence starts. The only special regime is the optional 15% rate for foreign remote workers on the long-stay visa under Immigration Law section 11(5). It covers income from remote work for an employer registered in another OECD state, or from a business registered in an OECD state. It applies for 365 days from becoming resident (PIT Law section 15(19.2)).

**Leaving: individuals.** The PIT Law has no exit charge on individuals. After residence ends, only Latvian-source income stays taxable. That includes Latvian rent, the sale of Latvian real estate, and the sale of shares in a real estate rich company.

**Leaving: companies (exit charge).** A transfer of assets out of Latvian taxing rights is a deemed distribution taxed at 20% after the 0.8 gross-up (CIT Law section 4(2)(2)). It covers three cases:

- **(i) Transfer to a foreign permanent establishment.** A Latvian taxpayer transfers an asset to its own permanent establishment abroad, and Latvia loses the right to tax that asset. If the book value is not the market value, market value is used (section 4(8.2)). If the asset is a fixed asset and the company keeps separate accounts for the establishment, its value enters the base gradually, as its depreciation is attributed to the establishment, and is taxed in the period in which the company distributes profit (section 4(8.2)). The company reports these assets in the return for the last month of the reporting year (section 16(4)).
- **(j) Transfer by a Latvian permanent establishment.** A non-resident's Latvian permanent establishment transfers an asset to its head office or to another permanent establishment abroad, and Latvia loses the right to tax that asset. Where the establishment moves a line of business abroad, the base is the market value of the transferred assets at the transfer date less the liabilities transferred with them (section 4(13.1)).
- **(g) Stopping CIT.** A company that stops paying Latvian CIT without being liquidated, other than in a reorganisation where the assets stay in use in Latvia, is taxed as if it had been liquidated (sections 4(8.1), 17(20)). The base is the liquidation quota: equity less what the members contributed (section 4(8)).

The (i) and (j) items go into the base of the last tax period of the reporting year (section 4(5)). Temporary transfers of up to 12 months are excluded where the assets serve as securities financing, collateral, prudential capital or liquidity management (section 4(11.1)). Neither the CIT Law nor LTF section 24 contains a five-year instalment option for the exit charge of the kind in article 5(2) of Council Directive (EU) 2016/1164 (ATAD), which the CIT Law names as a directive it transposes. The only payment relief in the text is the general one: on a reasoned written application filed no later than five working days after the due date, VID may split payment of a tax over up to one year (LTF section 24(1)(1)).

## Deadlines and filing

- **CIT withholding.** The payer withholds at the time of payment and pays the tax into the single tax account by the 23rd of the following month (CIT Law section 16(1)). It also reports the payments to non-residents and the tax withheld to VID, in the form and by the dates set by the Cabinet of Ministers (section 16(2)).
- **PIT withholding** from non-resident individuals: paid by the 23rd of the month after the payment month (PIT Law section 17(12)). The payer gives the non-resident a statement of the income and tax for the year (section 17(12.1)).
- **Real estate sold by a non-resident company to a buyer who does not withhold.** The seller reports and pays 3% within 30 days of the sale (CIT Law section 5(3)).
- **Net-basis report** by a non-resident: within 12 months of the transaction (CIT Law section 17(17)).
- **Monthly CIT return** (also for permanent establishments): by the 20th of the month after the tax period. Tax is paid by the 23rd (CIT Law section 17(1), (7)). A return for the last month of the reporting year is always required (section 17(3)).
- **Permanent establishment accounts.** Its reporting year is the calendar year. It files its balance sheet and profit and loss account within 4 months of the year end (CIT Law section 17(9)). If it stops trading, it files the return, balance sheet and profit and loss account within 20 days (section 17(10)).
- **Individual annual income declaration.** It is filed from 1 March to 1 June of the following year. If income taxed at the section 15(2) rates exceeds the maximum social insurance contribution base, the window is 1 April to 1 July (PIT Law section 19(5)).
  - A non-resident working in Latvia for a foreign employer with no Latvian permanent establishment, who stops that work and will not return before the year ends, files before leaving Latvia (section 19(5.1)).
  - A non-resident whose income taxed by annual assessment stops during the year, and who cuts economic ties with Latvia, files within 30 days after that income ends (section 19(5.2)).

## Penalties and interest

- **Late payment interest (nokavējuma nauda):** 0.05% of the unpaid principal for each day late, unless a specific tax law sets another rate (LTF section 29(2)). For taxes paid through the single tax account, it is calculated twice a month, on the 1st and the 15th. It is not charged if the late tax arrives by the last day of the month in which it fell due (section 29(2.1), (2.2)).
- **Failure to withhold.** A payer that should have withheld CIT from a non-resident and did not must pay it as its own tax. The amount is the payment ÷ 0.8 × the withholding rate (CIT Law section 5(11)). Late withholding or late reporting also makes the payer liable under the LTF (CIT Law section 19(2)).
- **Understatement found in an audit.** The tax, interest to the audit start date and a penalty (LTF section 32(1)). The penalty is 20% of the undeclared tax where the understatement is 15% or less of the tax that should have been declared, and 30% where it is more (section 32(4), (5)). It is halved where the taxpayer met filing and payment deadlines, cooperated, and this is not a repeat breach (section 32(7)). Amounts assessed in an audit are due within 30 days of the decision (section 32(8)).
- **Late returns** (LTF section 141, in fine units of EUR 5 each, Administrative Liability Law section 16(2)):
  - 3 to 10 days late: warning, or 5 to 14 units (EUR 25 to 70). No penalty for one monthly or quarterly return filed up to 5 days late in the VID electronic system within 12 months;
  - 11 to 20 days late: 15 to 30 units (EUR 75 to 150);
  - 21 to 30 days late: 31 to 56 units (EUR 155 to 280);
  - more than 30 days late, or not filed: 57 to 140 units (EUR 285 to 700).

## Cross-border points

- **Treaty overrides domestic rules.** Where a Latvian double tax treaty sets a different rule, the treaty applies (PIT Law section 24(1)). This covers the tie-breaker for dual residents and the cap or removal of withholding. Where the treaty's business profits article covers a management fee and the recipient has no Latvian permanent establishment, Latvia cannot tax the fee. Read the specific treaty to see which article covers the fee. To apply the treaty at source the payer needs the recipient's residence certificate, in the form set by Cabinet of Ministers regulation. Without one, the payer withholds the full domestic rate and the recipient claims a refund.
- **Low-tax jurisdictions override treaties in the domestic text.** The 20% under CIT Law section 5(6) and (8) applies "regardless of any provision of this law". Check the Cabinet list on the payment date, and check whether a treaty with that jurisdiction applies.
- **Foreign tax credit, individuals.** Latvian tax is reduced by the foreign tax paid, proved by documents confirmed by the foreign tax authority. The credit cannot exceed the Latvian tax on that foreign income (PIT Law section 24(3), (4)).
- **Employment abroad, individuals.** A resident's wages are exempt in Latvia if all three are true (PIT Law section 24(7)):
  - the work is done in another EU or EEA state, or a treaty state;
  - the wages are subject to income tax there;
  - the worker is not personnel leased to a Latvian resident or to a Latvian permanent establishment.

  If the employer is Latvian, it must confirm to VID in writing, before the work abroad starts, that the wages are taxed abroad (section 24(7.1)).
- **Foreign tax credit, companies.** CIT on dividends is reduced by foreign tax paid on the foreign income in those dividends, proved by confirmed foreign documents (CIT Law section 15(1)). The credit is capped at the Latvian CIT on the foreign income, worked out country by country (section 15(2), (3)). Excess credit carries forward in date order (section 15(6)). A company may also reduce dividends in the base by income received from a foreign permanent establishment that was taxed abroad. This needs separate accounts for that establishment (section 15(4), (4.1)). It does not apply to an establishment in a low-tax jurisdiction (section 15(5)).
- **Controlled foreign companies.** A Latvian taxpayer includes in its base the profit of a foreign company it controls that comes from non-genuine arrangements (CIT Law section 6.1). Detail is in [lv-corporate-income-tax](lv-corporate-income-tax.md).
- **Transfer pricing.** Transactions with persons in low-tax jurisdictions are treated as related-party transactions for deemed distributions (CIT Law section 4(10)). A tax audit may cover 3 years from the payment due date, but 5 years where VID checks transfer prices or hybrid mismatches (LTF section 23(1)).
- **Social security.** Inside the EU, EEA and Switzerland, Regulation (EC) 883/2004 decides which state's social security applies. See [latvia-social-contributions](latvia-social-contributions.md).

## Worked examples

### Example 1: a Latvian SIA pays a German consulting company without a residence certificate

A Latvian SIA pays a German GmbH a consulting fee of EUR 10,000 in March 2026. The GmbH has no Latvian permanent establishment. It does not send a residence certificate before payment. Germany is not on the low-tax list.

1. The fee is for consulting services to a Latvian company, so it falls under CIT Law section 5(1)(1) and (5).
2. The SIA withholds 20%: EUR 2,000. It pays EUR 8,000 to the GmbH and pays the EUR 2,000 to VID by 23 April 2026.
3. Had the SIA failed to withhold, its own extra CIT would be 10,000 ÷ 0.8 × 20% = EUR 2,500 (section 5(11)).
4. The GmbH is resident in an EU state. Within 12 months of the payment it files the section 5(4) report, showing EUR 6,000 of costs related to the contract. Tax on the net income at 20% is EUR 800. VID refunds the excess of EUR 1,200.
5. If the Latvia-Germany treaty treats the fee as business profit taxable only in Germany (check the treaty article), the GmbH can instead claim the full EUR 2,000 back with a residence certificate in the Cabinet form.

```oa-check
name: Consulting fee EUR 10,000 to a non-resident company (2026)
inputs:
  fee: 10000
  costs: 6000
steps:
  - withheld: fee * 0.20
  - net_paid: fee - withheld
  - payer_charge_if_not_withheld: fee / 0.8 * 0.20
  - tax_net_basis: (fee - costs) * 0.20
  - refund_net_basis: withheld - tax_net_basis
expected:
  withheld: 2000
  net_paid: 8000
  payer_charge_if_not_withheld: 2500
  tax_net_basis: 800
  refund_net_basis: 1200
```

### Example 2: a Finnish company's Riga branch moves its business line to Helsinki

A Finnish Oy has a registered permanent establishment in Riga. On 30 September 2026 it moves its whole software support line to the head office in Helsinki. The assets moved have a market value of EUR 300,000 at the transfer date. Liabilities of EUR 50,000 go with them, none of them provisions for future costs. After the move, Latvia can no longer tax those assets.

1. This is a transfer by a Latvian permanent establishment to its head office abroad, with loss of Latvian taxing rights. It is a deemed distribution (CIT Law section 4(2)(2)(j)).
2. Because a business line moves, the object is market value less the liabilities transferred: 300,000 − 50,000 = EUR 250,000 (section 4(13.1)).
3. Gross-up: 250,000 ÷ 0.8 = EUR 312,500 (section 4(9)).
4. CIT at 20%: EUR 62,500 (section 3(1)).
5. The item goes in the return for the last tax period of the reporting year, December 2026, since a permanent establishment's year is the calendar year (sections 4(5), 17(9)). That return is due by 20 January 2027 (section 17(1)). The tax falls due on 23 January 2027 (section 17(7)), a Saturday, so the payment day is the next working day, Monday 25 January 2027 (LTF section 29(3.1)). If the branch stops trading altogether, it files within 20 days of stopping (section 17(10)).

```oa-check
name: Branch moves business line abroad, market value EUR 300,000 (2026)
inputs:
  market_value: 300000
  liabilities: 50000
steps:
  - taxable_object: market_value - liabilities
  - grossed_up_base: taxable_object / 0.8
  - cit: grossed_up_base * 0.20
expected:
  taxable_object: 250000
  grossed_up_base: 312500
  cit: 62500
```

## Ask the client first

1. For a person: the declared place of residence, the exact arrival or departure date, the days in Latvia in each 12-month window, and where the family, property and social insurance are.
2. Which other country treats the person or company as resident, and which treaty applies.
3. For a payment abroad: what the payment is for (management or consulting, real estate, interest, royalty, goods), where the recipient is resident, and whether it holds a residence certificate in the Cabinet form before payment.
4. Whether the recipient or its jurisdiction is on the Cabinet low-tax list on the payment date.
5. For a foreign company: how many days its staff work in Latvia in any 6-month period, whether there is a site or office, and whether anyone signs contracts for it in Latvia.
6. For a company moving assets or a business abroad: what moves, its market value at the transfer date, the liabilities going with it, and whether Latvia keeps the right to tax it.

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Law (Uzņēmumu ienākuma nodokļa likums), consolidated text with amendments to 3 December 2025: ss. 1, 2, 3, 4, 4.2, 5, 6.1, 15, 16, 17, 19 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums | 2026-10-24 |
| Law On Personal Income Tax (Par iedzīvotāju ienākuma nodokli), consolidated text with amendments to 3 December 2025: ss. 2, 3, 15, 15.1, 17, 19, 24 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-10-24 |
| Law On Taxes and Fees (Par nodokļiem un nodevām), consolidated text: ss. 14, 23, 24, 29, 32, 141 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam | 2026-10-24 |
| Administrative Liability Law (Administratīvās atbildības likums), version in force from 1 January 2026: s. 16 | https://likumi.lv/ta/id/303007 | 2026-10-24 |

likumi.lv (the official legal acts portal of the publisher Latvijas Vēstnesis) and vid.gov.lv refused connections from our network on 23 and 24 October 2026 (direct requests and a browser both timed out). The texts were read from Internet Archive (web.archive.org) copies of the likumi.lv pages: the CIT Law captured on 4 October 2026, the LTF on 18 September 2026, the PIT Law on 1 September 2026, and the Administrative Liability Law (version from 1 January 2026) on 13 October 2025.

Not yet confirmed: the Cabinet of Ministers regulation on applying treaty relief and the residence certificate forms (Regulation No. 178 of 30 April 2001 is the one named in VID material; not read); the Cabinet list of low-tax and no-tax jurisdictions in force in 2026 (not read); whether Latvia gives the ATAD article 5(2) exit-tax instalments anywhere outside the CIT Law and LTF section 24 (none found in those texts); the 2026 maximum social insurance contribution base that sets the 33% band and the later declaration window (set under the law On State Social Insurance, not read); the Cabinet rules on reporting payments to non-residents under CIT Law section 16(2); amendments to the PIT Law adopted after 1 September 2026; individual treaty rates and tie-breakers.
