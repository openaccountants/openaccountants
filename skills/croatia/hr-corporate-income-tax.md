---
name: hr-corporate-income-tax
description: "Use this skill for Croatian profit tax (porez na dobit) in tax year 2026 under the Profit Tax Act in force from 1 January 2026 (last amended NN 151/25) and the Profit Tax Rulebook. It covers who pays and residence (art. 2 and 3), the 10% and 18% rates split at EUR 1,000,000 of revenue in the period (art. 28), the base and the main add-backs (50% of representation and of passenger car costs, fines, donations above 2%), depreciation rates and the car cap, bad debts, provisions, losses carried forward for 5 years, thin capitalisation (art. 8) and the 30% EBITDA interest limit (art. 30.a), monthly advances, the PD return due 30 April, and fines. Trigger on: Croatia corporate tax, porez na dobit 2026, PD obrazac, d.o.o. tax Croatia, predujam poreza na dobit, 10% or 18% profit tax. Out of scope: transfer pricing (hr-transfer-pricing), withholding and treaties in depth (cross-border skill), VAT (croatia-vat-return), individuals (croatia-income-tax)."
version: 0.2
jurisdiction: HR
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Croatia: profit tax (2026) v0.2

> **Source-cited draft.** No accountant has reviewed this skill yet. The law comes from the consolidated texts published by the Tax Administration (Porezna uprava) and from Narodne novine, all read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This is the corporate income tax (IT-CORP) skill for the Croatian pack. It links rather than repeats:

- Transfer pricing, related-party loan interest (art. 14, 2.65% for 2026), PD-IPO and APAs: [hr-transfer-pricing](hr-transfer-pricing.md).
- VAT: [croatia-vat-return](croatia-vat-return.md). Individuals and sole traders on income tax: [croatia-income-tax](croatia-income-tax.md). Setting up a company: [hr-company-formation](hr-company-formation.md). Overview: [hr-tax-overview](hr-tax-overview.md).

The law is the Profit Tax Act (Zakon o porezu na dobit, "ZPD", consolidated text in force from 1 January 2026, last amended by NN 151/25), the Profit Tax Rulebook (Pravilnik o porezu na dobit, "Rulebook", consolidated text last amended by NN 39/26) and the General Tax Act (Opći porezni zakon, "OPZ", in force from 1 January 2026). Currency: euro (EUR). Tax year: the calendar year 2026, unless the Tax Administration approved a different period of up to 12 months (ZPD art. 29(1) and (2)).

## Who this applies to

**Profit taxpayers (ZPD art. 2).**

- Companies and other resident legal and natural persons that carry on business independently, permanently and for profit (art. 2(1)).
- The Croatian branch (business unit) of a foreign business (art. 2(2)).
- An individual with self-employed income who elects profit tax instead of income tax (art. 2(3)). An individual must pay profit tax if total receipts in the prior period exceeded EUR 1,000,000 (art. 2(4)).
- Public bodies, the Croatian National Bank, associations, foundations, chambers, unions and similar bodies are not profit taxpayers (art. 2(5) and (6)). They become taxpayers for an economic activity whose non-taxation would give them an unfair market advantage, and must register within 8 days of starting it (art. 2(7)).
- Pension and investment funds without legal personality are exempt (art. 2(8)), unless the fund was set up to exploit a tax advantage (art. 2(9), added by NN 151/25).

**Residence (ZPD art. 3).** A person is resident if its seat is entered in a Croatian court or other register, or its place of effective management and supervision is in Croatia. A resident is taxed on profit made in Croatia and abroad. A non-resident is taxed only on profit made in Croatia (art. 5(2) and (3)).

**Out of this skill.** Transfer pricing, withholding tax in depth, treaties, tonnage tax, CFC rules (ZPD art. 30.b and 30.c) and the Investment Promotion Act and Tourism Act reliefs. They are flagged, not computed. The assisted-area relief is summarised under "Tax due" but not computed.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Profit tax rate, revenue in the period up to EUR 1,000,000 | 10% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 28(1)) |
| Profit tax rate, revenue in the period above EUR 1,000,000 | 18% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 28(2)) |
| Revenue tested for the rate | PD line 1 (total revenue) less line 28 (special-circumstance support grants and written-off liabilities) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro23 (Rulebook art. 47(3), line 43) |
| Cash-basis option: prior-period revenue not above | EUR 1,000,000 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 5(7)) |
| Representation costs added back | 50% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 7(1)(3)) |
| Passenger car and other personal transport costs added back (not insurance or interest; only where no salary benefit is assessed) | 50% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 7(1)(4)) |
| Promotional items given to consumers that are not representation | up to EUR 22 each, excluding VAT | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 7(6)) |
| Deductible donations for public-benefit purposes | up to 2% of prior or current period revenue | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 7(7)) |
| Fixed asset threshold | cost above EUR 665 and life over 1 year | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(3)) |
| Depreciation, buildings and ships over 1,000 GRT | 5% (20 years) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(5)) |
| Depreciation, basic herd and passenger cars | 20% (5 years) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(5)) |
| Depreciation, intangibles, equipment, vehicles other than cars, machinery | 25% (4 years) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(5)) |
| Depreciation, computers, hardware, software, mobile phones, network equipment | 50% (2 years) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(5)) |
| Depreciation, other assets | 10% (10 years) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(5)) |
| Doubling of the depreciation rates | allowed | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(6)) |
| Car depreciation cap per vehicle (unless used only for a registered rental or transport business) | EUR 54,000 of cost | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 12(13)) |
| Bad debt write-down: days past due at period end | more than 60 days, and unpaid by the 15th day before the return is filed | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 9(1)) |
| Write-off of small time-barred debts from unrelated business debtors | up to EUR 665 per debtor per period | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 9(4)) |
| Tax loss carry-forward | 5 years, oldest first; no carry-back | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 17(2) and (4)) |
| Ownership change that can cancel losses | more than 50% in the period | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 17(7)) |
| Thin capitalisation: shareholder holding | at least 25% of shares, capital or votes | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 8(1)) |
| Thin capitalisation: loans above which interest is not deductible | 4 times the shareholder's share of capital | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 8(1) and (3)) |
| Interest limitation on exceeding borrowing costs | 30% of tax EBITDA or EUR 3,000,000, whichever is higher; excess carried forward 3 periods | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 30.a(1) and (9)) |
| Advances | prior period liability divided by its months, paid monthly by the end of the next month; the new amount is fixed on the last day of the filing deadline | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 34(1)); https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro23 (Rulebook art. 48(1)) |
| PD return and payment | 4 months after period end: 30 April 2027 for calendar 2026 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 35(1) and (2)) |
| Withholding tax: interest, royalties (to non-individuals) | 15% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 31(4) and (6)) |
| Withholding tax: dividends and profit shares; foreign performers paid through a company | 10% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 31(7) and (10)) |
| Withholding tax: payees in EU-listed non-cooperative jurisdictions with no treaty (also market research, tax and business advisory, audit) | 25% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 31(12)) |
| Fine: base not determined, tax or advance not paid on time (legal person) | EUR 260 to EUR 26,540; responsible person EUR 260 to EUR 2,650 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 38(1) and (2)) |
| Fine: return not filed on time or not filed electronically (legal person) | EUR 660 to EUR 39,810; responsible person EUR 390 to EUR 3,980 | 2026 | https://porezna-uprava.gov.hr/Propisi (OPZ art. 193(1)(9), (11) and (4)) |

The `propisi.aspx#id=pro` links are the Tax Administration's own links to its consolidated texts: pro19 is the ZPD and pro23 the Rulebook. The OPZ is in the same register at https://porezna-uprava.gov.hr/Propisi, under "Porezni postupak".

## The taxable base

**Start from accounting profit.** The base is the profit under the accounting rules (revenue less expenses before profit tax), increased and reduced as the Act says (ZPD art. 5(1)). Costs not connected with the business are not expenses (art. 5(6)). A taxpayer whose revenue in the prior period was not above EUR 1,000,000 may use the cash basis instead. A VAT payer must also be in the VAT cash-accounting scheme. The taxpayer notifies the Tax Administration within 15 days of the start of the period and keeps the method for at least 3 periods (art. 5(7), (11) to (13)).

**Main reductions (ZPD art. 6(1)).**

- Dividends and profit shares received, where the payer is subject to profit tax or a similar tax, has a comparable corporate form and did not deduct the payment (art. 6(1)(1)).
- Unrealised gains on shares that were taxed earlier; recoveries of written-off debts that were not deducted (art. 6(1)(2) and (3)).
- Depreciation disallowed in earlier periods, up to the art. 12 amounts (art. 6(1)(4)).
- **New for 2026:** sponsorship given in Croatia for cultural, scientific, educational, health, humanitarian, sports, religious, environmental and other public-benefit purposes, to bodies the competent minister names by decision (art. 6(1)(6) and (8), added by NN 151/25; PD line 33.a).

**Main add-backs (ZPD art. 7(1); PD lines 5 to 25).**

- 50% of representation: hospitality, gifts with or without a logo, holidays, sport, recreation, renting cars, boats, aircraft and holiday homes, in dealings with business partners (point 3; PD line 6). A business partner is anyone with whom a business relationship exists or is expected (Rulebook art. 23(1)). Goods marked "not for sale", and promotional items given to consumers worth up to EUR 22 each, are not representation (art. 7(6)).
- 50% of the costs of own or hired passenger cars and other personal transport (car, boat, helicopter, aircraft) used by managers and other staff, where no salary benefit is assessed for that use (point 4; PD line 7). Insurance, interest on the purchase, road vehicle tax and compulsory registration charges are left out of the 50% (Rulebook art. 25(1)). Cars used only in a driving school, taxi, rental, roadside assistance, installation or emergency business are not caught (Rulebook art. 25(2)).
- Fines imposed by an authority (point 7; PD line 11), and costs of enforced collection of tax (point 6).
- Default interest between related persons (point 8). Interest that is not deductible under the Act, including thin capitalisation and art. 14 (point 11; PD lines 15 and 16).
- Donations above 2% of revenue, and donations that benefit the taxpayer or a related person (point 10; PD line 14).
- Hidden profit distributions and private withdrawals found in an audit, with the VAT, income tax and contributions on them (point 12).
- Shortages above the chamber of commerce limits (point 5), and all other costs not directly connected with making profit (point 13).
- Bribes and other illicit benefits are never deductible (art. 7.a).

Where income tax is paid on the item as a benefit to a person, the add-back does not apply, except for points 9 and 12 (art. 7(2)).

**Depreciation (ZPD art. 12).** Straight line on cost, asset by asset, at no more than the rates in the table; the rates may be doubled (art. 12(1), (2), (5), (6)). Depreciation starts the month after the asset is put into use (art. 12(8)). Land, forests, financial assets, cultural monuments and works of art are not depreciated (art. 12(4)). Car depreciation is allowed only on up to EUR 54,000 of cost per vehicle, unless the vehicle serves only a registered rental or transport business (art. 12(13)). Boats, aircraft, apartments and holiday homes are depreciable only by a business registered to rent them that earns revenue from them in the period of at least 7% (boats, aircraft) or 5% (apartments, holiday homes) of their cost (art. 12(16)). Otherwise the depreciation and running costs are added back (art. 12(17)). Depreciation above these limits goes on PD lines 5 and 18.

**Bad debts, stock, provisions (ZPD art. 9 to 11).**

- A write-down of trade receivables is deductible if more than 60 days passed from the due date to the period end and the debt was not paid by the 15th day before the return is filed (art. 9(1)). The taxpayer must also have taken collection steps: a lawsuit, enforcement, a claim in bankruptcy, or a settlement with an unrelated debtor (art. 9(2) and (3)). Small time-barred debts of up to EUR 665 per business debtor, or EUR 40 per individual, may be written off without those steps (art. 9(4)).
- Write-downs of stock and financial assets are deductible only when the asset is sold or used (art. 10(1)).
- Provisions are not deductible, except those required by law or contract (severance, restoring natural resources, warranties, lawsuits already started) and unused annual leave (art. 11(1), (2) and (5)).

**Losses (ZPD art. 17; Rulebook art. 38).**

- A negative base is a tax loss. It is carried forward and set against the base in the next 5 years, oldest first (art. 17(1), (2), (4); Rulebook art. 38(1)). A 2021 loss can be used in 2022 to 2026; a 2020 loss lapsed after 2025. There is no carry-back.
- The right lapses if ownership changes by more than 50% in the period and the taxpayer had not been trading for the two periods before, or substantially changes its activity in the two periods after (art. 17(5) and (7); Rulebook art. 38(4)). A substantial change includes a change of section or group in the national activity classification (Rulebook art. 38(5)). Losses already used must then be added back (art. 17(6)). Saving jobs or a business rescue is an exception (art. 17(8)).

**Thin capitalisation (ZPD art. 8; Rulebook art. 32).** Interest on loans from a shareholder holding at least 25% of shares, capital or votes is not deductible on the part of the loans that at any time in the period exceeds 4 times that shareholder's share of capital (art. 8(1)). Capital means paid-in capital, retained earnings and reserves, averaged over the last day of each month (art. 8(3)). Loans from third parties guaranteed by the shareholder, and loans from related persons, count (art. 8(2)). The rule does not apply to loans from banks and other financial organisations, to interest on which income tax on capital is paid, or to interest charged by a Croatian profit taxpayer (art. 8(1); Rulebook art. 32(4) to (6)). The add-back goes on PD line 15.

**Interest limitation (ZPD art. 30.a; Rulebook art. 39.a).**

- Exceeding borrowing costs, meaning borrowing costs above taxable interest income, are deductible only up to the higher of 30% of tax EBITDA and EUR 3,000,000 (art. 30.a(1) and (2)).
- Tax EBITDA counts only taxable income: profit before tax plus tax-allowed depreciation plus total borrowing costs (art. 30.a(4)).
- A standalone taxpayer (no accounting consolidation group, no related person, no permanent establishment, no loans to or from its members) and financial undertakings are outside the rule (art. 30.a(5) and (6)).
- Amounts already added back under art. 8 or art. 14 reduce the art. 30.a add-back (art. 30.a(11)). The disallowed excess is carried forward for 3 periods (art. 30.a(9)). The add-back goes on PD line 12.

**Tax due.** The base after losses (PD line 38) times the rate (line 43) gives the liability (line 44). Reliefs for assisted areas, Vukovar and the Investment Promotion and Tourism Acts reduce it (lines 45 to 52). A taxpayer working in the City of Vukovar pays no profit tax, and one working in a local unit in development group I pays half the rate, if it employs more than 5 people on open-ended contracts and more than 50% of them live in group I areas or Vukovar; the relief counts as de minimis aid (ZPD art. 28.a(1) to (3); Rulebook art. 47(3), lines 46 and 47). The foreign tax credit (line 54; ZPD art. 30) and advances paid (line 56) come off to give the balance due or refundable (Rulebook art. 47(3)).

## Deadlines and filing

- **Registration.** A company enters the register of taxpayers kept by the Tax Administration when it registers its business. A public body or association that starts a taxable activity must register within 8 days (ZPD art. 2(7)).
- **Advances.** Paid monthly, by the end of the month for the month before, at the prior period's liability divided by the number of months in that period (ZPD art. 34(1)). The advance from a return is fixed on the last day of the deadline for filing that return, 30 April for a calendar year (Rulebook art. 48(1)); until then the advance from the earlier return applies. A new business pays no advances until its first return (art. 34(3)). The Tax Administration may change the amount by decision, on request or after an audit; the decision binds until the next return (art. 34(2); Rulebook art. 48(2)). Taxpayers in bankruptcy or liquidation pay no advances (Rulebook art. 48(7)).
- **PD return (Prijava poreza na dobit).** Filed within 4 months after the period ends: by **30 April 2027** for calendar 2026 (ZPD art. 35(1)). The tax shown is due on the last day of that deadline (art. 35(2); art. 32(2) as amended by NN 151/25). Cash-basis taxpayers file form PD-NN instead (Rulebook art. 46(1)).
- **Electronic filing for everyone.** From 2026 every taxpayer must file the PD return electronically through e-Porezna. NN 151/25 deleted the words that limited this duty to large and medium-sized businesses (ZPD art. 35(3); Rulebook art. 46(3)).
- **Attachments.** The balance sheet and profit and loss account go with the return; those already filed with FINA on time count as filed (ZPD art. 35(6); Rulebook art. 46(5)). Depending on the facts, also: the related-party form PD-IPO (see [hr-transfer-pricing](hr-transfer-pricing.md)), the CFC report, the relief calculations and the art. 30.a schedule (Rulebook art. 39.a(3), art. 46(2)).
- **Overpaid advances** are refunded on request or set against the next period (ZPD art. 35(5)).
- **Short periods.** On a merger or division, or when liquidation or bankruptcy opens, the return is due within 30 days after the period ends; at the end of liquidation or on closing without liquidation, within 8 days (art. 35(7)). Moving the seat abroad, a merger or division, the end of liquidation and a closure must be announced to the Tax Administration 30 days before the formal steps (art. 29(3) and (4)).
- **No return filed.** The Tax Administration assesses the tax by estimate, using earlier periods' revenue, liabilities, assets and bank balances (art. 35(8)).

## Penalties and interest

- **Late payment interest.** Interest runs on tax paid late from the due date (OPZ art. 130(1) and (3)). Where an audit finds more tax, it runs from the day the tax should have been paid (OPZ art. 130(7)), so from the original PD due date. The rate is set by a separate law; see "Not yet confirmed".
- **Fines under the Profit Tax Act (ZPD art. 38).** EUR 260 to EUR 26,540 for the company, and EUR 260 to EUR 2,650 for the responsible person, for: not determining the base as the Act requires; not withholding or paying withholding tax; not paying the tax due on time; not paying an advance on time; not notifying a change of legal form, liquidation, bankruptcy, merger or division within 8 days. A repeat offence costs EUR 390 to EUR 39,810 and EUR 390 to EUR 3,980.
- **Fines under the General Tax Act (OPZ art. 193).** EUR 660 to EUR 39,810 for a legal person, and EUR 390 to EUR 3,980 for the responsible person, for: not filing a return on time (point 9), not attaching the required documents (point 10), not filing electronically (point 11), and not giving data on request (point 14). A repeat offence costs EUR 1,060 to EUR 53,080 and EUR 660 to EUR 6,630 (art. 193(5)).
- These are ranges set case by case. The Act sets no fixed percentage surcharge on underpaid profit tax.

## Cross-border points

- **Non-residents.** A non-resident's Croatian branch is a profit taxpayer on Croatian profit (ZPD art. 2(2), art. 5(3)). Profit attribution is in [hr-transfer-pricing](hr-transfer-pricing.md).
- **Withholding tax (ZPD art. 31), pointer only.** The Croatian payer withholds on payments to foreign persons that are not individuals: 15% on interest and royalties, 10% on dividends and profit shares, 10% on foreign performers paid through a company. Interest on trade credit for goods, on loans from foreign banks and financial institutions, and on bonds is exempt (art. 31(5)). The rate is 25% on all these payments, and also on market research, tax and business advice and audit services, where the payee is in an EU-listed non-cooperative jurisdiction with which Croatia has no treaty (art. 31(12)). EU directive exemptions and treaty rates belong to the pack's cross-border skill (XB). The previous version of this skill said 15% applied to advisory and audit services generally. The 2026 text taxes those services only at 25%, and only for listed jurisdictions.
- **Foreign tax credit (ZPD art. 30, rewritten by NN 151/25).** A resident with a foreign branch adds the branch's positive base and credits the foreign tax. The credit is capped at the Croatian rate on that base, at the Croatian liability and at the tax actually paid (art. 30(1) and (2)). Treaty withholding tax is credited the same way (art. 30(4)). Foreign tax with no treaty reduces the base instead (art. 30(5)). A certificate of the foreign tax paid, with no right to a refund, is needed (art. 30(6)).
- **Anti-abuse.** Arrangements set up mainly for a tax advantage that are not genuine lose it (ZPD art. 5.a). CFC income is added under art. 30.b and 30.c (PD line 10); not covered here.

## Worked examples

### Example 1: small d.o.o. at 10% with add-backs and a loss

A Croatian d.o.o. has 2026 revenue of EUR 600,000 and accounting profit of EUR 80,000. Its books show EUR 4,000 of representation (client lunches and gifts), EUR 6,000 of fuel, servicing and depreciation on the director's car with no salary benefit assessed, and a EUR 500 traffic fine. It has a EUR 10,000 tax loss from 2023. Its 2024 and 2025 returns each showed tax of EUR 6,000, so every 2026 advance was EUR 500 (ZPD art. 34(1); Rulebook art. 48(1)).

1. Representation add-back: 50% of EUR 4,000 = EUR 2,000 (ZPD art. 7(1)(3); PD line 6).
2. Car add-back: 50% of EUR 6,000 = EUR 3,000 (art. 7(1)(4); line 7). No insurance or interest is in the EUR 6,000.
3. Fine: EUR 500 in full (art. 7(1)(7); line 11).
4. Base before losses: EUR 80,000 + 2,000 + 3,000 + 500 = EUR 85,500. Less the 2023 loss, still inside 5 years: EUR 75,500 (art. 17(2)).
5. Revenue is up to EUR 1,000,000, so the rate is 10% (art. 28). Tax: EUR 7,550.
6. Advances paid: 12 x EUR 500 = EUR 6,000. Balance due by 30 April 2027: EUR 1,550 (art. 35(2) and (4)).
7. New monthly advance from the 2026 return: EUR 7,550 / 12 = EUR 629.17 (art. 34(1); PD line 59), fixed on 30 April 2027 (Rulebook art. 48(1)).

```oa-check
name: Croatian d.o.o., revenue EUR 600,000, profit EUR 80,000, 2023 loss EUR 10,000 (2026, 10% rate)
inputs:
  profit: 80000
  representation: 4000
  car_costs: 6000
  fine: 500
  loss_bf: 10000
  monthly_advance: 500
steps:
  - add_representation: representation * 50 / 100
  - add_car: car_costs * 50 / 100
  - base_before_loss: profit + add_representation + add_car + fine
  - base: base_before_loss - loss_bf
  - tax: base * 10 / 100
  - advances_paid: monthly_advance * 12
  - balance_due: tax - advances_paid
  - new_monthly_advance: round(tax / 12, 2)
expected:
  add_representation: 2000
  add_car: 3000
  base_before_loss: 85500
  base: 75500
  tax: 7550
  advances_paid: 6000
  balance_due: 1550
  new_monthly_advance: 629.17
```

### Example 2: 18% company with a thin-capitalised loan from a foreign parent

A Croatian d.o.o. with 2026 revenue of EUR 5,000,000 and accounting profit of EUR 400,000 is wholly owned by an Austrian parent. The parent lent it EUR 2,000,000, outstanding all year at 2.65%, so interest is EUR 53,000. That rate equals the published related-party rate, so art. 14 adds nothing (see [hr-transfer-pricing](hr-transfer-pricing.md)). The company's capital, retained earnings and reserves are EUR 300,000 at each month end. It also booked EUR 10,000 of representation.

1. The parent holds 100%, at least 25%, so art. 8 applies. The lender is foreign, so Rulebook art. 32(6) does not exclude it.
2. Allowed loan: 4 x EUR 300,000 = EUR 1,200,000. Excess loan: EUR 800,000 (art. 8(1) and (3)).
3. Interest on the excess: EUR 53,000 x 800,000 / 2,000,000 = EUR 21,200, added on PD line 15.
4. Art. 30.a: the company is in a group, so the rule applies. Its exceeding borrowing costs (EUR 53,000) are far below EUR 3,000,000, so nothing more is added. The EUR 21,200 would in any case reduce an art. 30.a add-back (art. 30.a(1) and (11)).
5. Representation: 50% of EUR 10,000 = EUR 5,000.
6. Base: EUR 400,000 + 21,200 + 5,000 = EUR 426,200. Revenue is above EUR 1,000,000, so the rate is 18%. Tax: EUR 76,716.
7. Withholding: interest to a foreign company that is not a bank bears 15% (ZPD art. 31(4) to (6)), EUR 7,950 before any EU directive or treaty relief. Check that relief in the cross-border skill before withholding.

The example keeps the loan and capital constant all year. With changing balances, test each month end (art. 8(1); Rulebook art. 32(2) and (3)).

```oa-check
name: 18% company, EUR 2,000,000 loan from 100% foreign parent, capital EUR 300,000 (2026)
inputs:
  profit: 400000
  loan: 2000000
  rate_pct: 2.65
  capital: 300000
  representation: 10000
steps:
  - interest: loan * rate_pct / 100
  - allowed_loan: capital * 4
  - excess_loan: max(loan - allowed_loan, 0)
  - thin_cap_addback: interest * excess_loan / loan
  - add_representation: representation * 50 / 100
  - base: profit + thin_cap_addback + add_representation
  - tax: base * 18 / 100
  - wht_before_relief: interest * 15 / 100
expected:
  interest: 53000
  allowed_loan: 1200000
  excess_loan: 800000
  thin_cap_addback: 21200
  add_representation: 5000
  base: 426200
  tax: 76716
  wht_before_relief: 7950
```

## Ask the client first

1. Total revenue for 2026 as on PD line 1, and any special-circumstance support grants in it. This sets 10% or 18%.
2. Whether the company is on the cash basis (form PD-NN) or the accrual basis, and its 2025 revenue.
3. Losses carried forward by year, and any change of more than 50% in ownership or change of activity in 2026.
4. Representation, car and transport costs (and whether a salary benefit is assessed for private use), fines, donations and provisions in the 2026 books.
5. Loans from shareholders holding 25% or more, or guaranteed by them, with monthly balances, rates and the company's monthly capital, retained earnings and reserves; and whether the company belongs to a group (art. 30.a).
6. Payments abroad of interest, royalties, dividends or advisory fees, and any reliefs claimed (assisted areas, Investment Promotion Act, Tourism Act).

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dobit, consolidated text in force from 1 January 2026 (NN 177/04 to 151/25), arts. 2, 3, 5, 5.a, 6, 7, 7.a, 8, 9, 10, 11, 12, 17, 28, 29, 30, 30.a, 31, 32, 34, 35, 38 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 | 2026-10-23 |
| Zakon o izmjenama i dopunama Zakona o porezu na dobit, NN 151/2025 (2026 changes: funds, sponsorship, art. 30, art. 32, e-filing for all) | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_151_2261.html | 2026-10-23 |
| Pravilnik o porezu na dobit, consolidated text in force from 16 April 2026 (NN 95/05 to 39/26), arts. 23, 25, 32, 38, 39.a, 46, 47, 48 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro23 | 2026-10-23 |
| Opći porezni zakon, consolidated text in force from 1 January 2026 (NN 115/16 to 151/25), arts. 130, 193 | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Zakon o kamatama (NN 94/04) and Uredba o visini stope zatezne kamate (NN 153/04), in the Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-24 |

Not yet confirmed: the late payment interest rate on tax debts for 2026. OPZ art. 130(1) points to a separate law; the register lists the Interest Act (NN 94/04), whose rate decree (NN 153/04, 15%) predates the Obligations Act art. 29 formula, and no Tax Administration text naming the 2026 rate was found. The Croatian National Bank lists the Obligations Act art. 29 non-commercial default rate at 5.40% for 1 July to 31 December 2026 (https://www.hnb.hr/documents/d/guest/h-tablica_max-nks-eks-1), but no official text was found saying that rate applies to tax debts. Also not confirmed: whether the advance for March or for April is the first one paid at the new amount (Rulebook art. 48(1) fixes it on 30 April); the list of bodies named for the new sponsorship deduction (the art. 6(8) decision was not read); EU directive and treaty relief from withholding (left to the cross-border skill); and the content of the Investment Promotion Act and Tourism Act reliefs, which this skill only flags.

> Contributed by Michael Cutajar.

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
