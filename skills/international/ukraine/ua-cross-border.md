---
name: ua-cross-border
description: "Ukrainian cross-border tax for tax year 2026 under the Tax Code of Ukraine. Covers residence of individuals (home, centre of vital interests, 183 days, citizenship) and companies, how non-residents are taxed, the permanent establishment test (12-month sites, 183-day services, dependent agents, preparatory exclusions), withholding on Ukrainian-source income under art. 141.4 (15%, freight 6%, insurance 0/4/12%, Eurobond interest 5%, the gross-up), treaty relief with residence certificates and beneficial ownership (art. 103), foreign tax credits, controlled foreign companies under art. 39-2 (control tests, exemptions, the EUR 2 million threshold, the CFC report and 60-day notices), CFC profit of individuals (art. 170.13), leaving Ukraine (art. 179.3) and the fines. Trigger on: Ukraine withholding tax non-resident, податок на репатріацію, КІК, controlled foreign company Ukraine, residence certificate Ukraine, permanent establishment Ukraine. Out of scope: transfer pricing (ua-transfer-pricing), corporate tax generally (ua-corporate-income-tax), personal income tax generally (ua-income-tax)."
version: 0.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ukraine: cross-border tax (2026)

Ukraine taxes residents on worldwide income and non-residents on Ukrainian-source income (TCU art. 163.1, 163.2). Payments of Ukrainian-source income to non-residents are taxed by withholding at the payer (art. 141.4.2). Resident individuals and companies that control foreign companies are taxed on their share of the adjusted profit (art. 39-2). All article numbers are articles of the Tax Code of Ukraine (Податковий кодекс України, Law No. 2755-VI of 2 December 2010) unless another act is named. Currency: hryvnia (UAH).

This skill links rather than repeats:

- Corporate income tax, the 18% rate and returns: [ua-corporate-income-tax](ua-corporate-income-tax.md).
- Transfer pricing on deals with related non-residents and low-tax states: [ua-transfer-pricing](ua-transfer-pricing.md).
- Personal income tax for sole proprietors: [ua-income-tax](ua-income-tax.md). The country map: [ua-tax-overview](ua-tax-overview.md).

## Who this applies to

**Resident companies.** Legal persons, and their separate units, formed and operating under Ukrainian law, wherever they are located (art. 14.1.213(а)). They are taxed on income from all sources, and foreign income counts in full (art. 13.1).

**Resident individuals (art. 14.1.213(в)).** A person whose place of residence is in Ukraine. If the person also has a home abroad, the tests apply in order:

1. permanent home in Ukraine;
2. centre of vital interests, meaning closer personal or economic ties. Family living in Ukraine, or registration as an entrepreneur, is enough to place it in Ukraine;
3. at least 183 days in Ukraine in the tax year, counting the days of arrival and departure;
4. Ukrainian citizenship.

A person who chooses Ukraine as their main place of residence under the Code, or registers as self-employed, is resident. A Ukrainian citizen who unlawfully also holds another citizenship is treated as Ukrainian for this tax and gets no credit for foreign tax.

**Non-residents.** A non-resident company pays corporate income tax on business through a permanent establishment and on Ukrainian-source income (art. 133.2, see [ua-corporate-income-tax](ua-corporate-income-tax.md)). A non-resident individual pays personal income tax on Ukrainian-source income only (art. 162.1.2, 163.2).

**Payers who withhold.** Residents (including sole proprietors, independent professionals and single-tax payers) and non-residents with a Ukrainian PE that pay Ukrainian-source income to a non-resident (art. 141.4.2).

**Controlling persons.** Resident individuals and companies that own or control a foreign company or foreign entity under the tests in art. 39-2.1.2.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Withholding on Ukrainian-source income of non-residents, general (art. 141.4.2) | 15% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Freight paid to non-residents (art. 141.4.4) | 6% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Insurance payments to non-residents (art. 141.4.5) | 0%, 4% or 12% by contract type | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Interest on loans funded by Eurobonds on an approved exchange (art. 141.4.11) | 5% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Discount bonds and treasury bills of non-residents (art. 141.4.3) | 18% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Gross-up where tax was not withheld or income paid in kind (art. 141.4.2) | tax = paid x 100 / (100 - rate) - paid | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Permanent establishment: building or installation site (art. 14.1.193(а)) | more than 12 months | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Permanent establishment: services through staff (art. 14.1.193(б)) | more than 183 days in any 12 months | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Individual residence, day count (art. 14.1.213) | 183 days or more in the tax year | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC control: one resident (art. 39-2.1.2) | more than 50% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC control: each resident, where residents together hold 50% or more (art. 39-2.1.2) | more than 10% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC exemption: effective tax rate (art. 39-2.4.1) | at least the 18% base rate less 5 points (13%) | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC exemption: passive income share (art. 39-2.4.1) | not more than 50% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC exemption: total income of all CFCs of one controlling person (art. 39-2.4.2.1) | not more than EUR 2,000,000 | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC profit of a company (art. 136.7) | 18% base rate | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC profit of an individual (art. 170.13.1, 167.1) | 18% personal income tax | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| CFC profit distributed before it is reported (art. 170.13.2.1, 167.5.4) | 9% (half of 18%) | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Military levy on individuals' income under art. 163 (section XX, subsection 10, point 16-1) | 5% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Personal income tax on foreign income of residents (art. 170.11.1, 167.1) | 18% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Subsistence minimum for an able-bodied person at 1 January 2026, the unit for CFC fines (State Budget Law 2026, art. 7) | UAH 3,328 | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 |
| Document retention and assessment period for art. 39-2 and 141.4 (art. 44.3.1, 102.1) | 2,555 days | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |

## The taxable base

**What income is Ukrainian-source (art. 141.4.1).** Interest and discount income; dividends paid by a resident; royalties; freight and engineering fees; operating lease or rent; proceeds from Ukrainian real estate; gains on shares of Ukrainian companies (except shares traded on a listed exchange) and on shares of foreign companies whose value, at any time in the prior 365 days, comes 50% or more from Ukrainian companies whose value comes 50% or more from Ukrainian real estate; joint activity and long-term contracts in Ukraine; fees for cultural, educational, religious, sports and entertainment activity in Ukraine; broker, commission and agency fees; insurance premiums; entertainment income; donations; rights to Ukrainian natural resources; and other income from business in Ukraine. Payment for goods, work and services supplied to a resident is not on the list (art. 141.4.1(к)).

**The withholding mechanics (art. 141.4.2).** The payer withholds at the time of payment and pays the tax to the budget then, unless a treaty in force says otherwise. Income a non-resident earns through its Ukrainian PE is taxed with the PE, not by withholding. If the income is paid in kind, or the tax was not withheld, the payer grosses it up and pays from its own funds: tax = paid amount x 100 / (100 - rate) - paid amount.

**Excess payments treated as dividends.** A resident paying a non-resident more than the arm's length amount in a way art. 14.1.49 treats as a dividend withholds 15% on the excess (art. 141.4.2). Single-tax group 4 payers are excluded from this rule.

**Sale of Ukrainian property-rich shares between non-residents.** A non-resident buyer withholds 15% of the seller's gain and must register with the tax authority by the first payment. The gain is proceeds less documented cost; without cost documents the whole proceeds are taxed (art. 141.4.2).

**Exempt interest.** Interest and gains of non-residents on Ukrainian government and local bonds, and on state- or locally-guaranteed debt, are not taxed, with an exception for some gains of residents of listed low-tax states (art. 141.4.10).

**Permanent establishment (art. 14.1.193).** A fixed place through which a non-resident carries on business in Ukraine: a place of management, branch, office, factory, workshop, mine or well, warehouse, or server. It also includes a building or installation site lasting more than 12 months; services (other than staff supply) through employees for more than 183 days in any 12-month period; and a person who habitually concludes contracts, or negotiates their essential terms, or holds stock from which goods are delivered, for one non-resident or related non-residents. Activities of related non-residents are counted together. Storage, display, purchasing, information gathering and other activity of a preparatory or auxiliary character are not a PE. An independent agent acting in the ordinary course of its business is not a PE. Being a controlling person under art. 39-2 does not make a PE. A PE is taxed on its profit as if it were an independent company (art. 141.4.7).

**Controlled foreign companies (art. 39-2).**

- **Control.** A resident owns more than 50%; or owns more than 10% where residents together own 50% or more; or, alone or with related residents, exercises actual control (art. 39-2.1.2). Trusts, partnerships, funds and listed entity forms without legal personality can count (art. 39-2.1.1). Where a Ukrainian company is itself the controlling person, its Ukrainian owners are not.
- **What is taxed.** The controlling person's share, on the last day of the period, of the CFC's adjusted profit (art. 39-2.2.2). Adjusted profit starts from profit before tax in the CFC's non-consolidated financial statements for the year (art. 39-2.3.1). Then (art. 39-2.3.2): results on securities, corporate rights and derivatives follow special rules (39-2.3.2.1); impairment of fixed and intangible assets counts only on disposal (39-2.3.2.2); interest expense counts only up to 30% of the sum of profit before tax, finance costs and depreciation (39-2.3.2.3); deals with related non-residents, residents of listed low-tax states and listed entity forms are adjusted to arm's length (39-2.3.2.4); income from another CFC of the same controlling person (39-2.3.2.5), profit earned through a Ukrainian PE (39-2.3.2.6), and dividends and participation income from Ukrainian companies (39-2.3.2.7) are taken out. Profit taxed for one controlling person is not taxed again for another (art. 39-2.2.3).
- **Exemptions (art. 39-2.4.1, 39-2.4.2).** No CFC charge if Ukraine has a tax treaty or tax information exchange agreement with the CFC's state and either the CFC's effective tax rate is at least 13% (the 18% base rate less 5 points) or passive income is not more than 50% of its income. Passive income above 50% counts as active where the CFC has real functions, risks, assets, staff and capital. Separately, no charge if the total income of all CFCs of one controlling person is not more than EUR 2,000,000, or the CFC is listed on a recognised exchange, or it is a charity that does not distribute. The controlling person may waive an exemption (art. 39-2.4.4).
- **Companies.** The CFC's adjusted profit is a separate object taxed at the 18% base rate (art. 134.1.7, 136.7). Foreign corporate tax paid by the CFC, including tax withheld from its income, reduces the Ukrainian tax in proportion to the controlling share (art. 137.9).
- **Individuals.** The share of adjusted profit goes into total annual taxable income on the annual declaration and is taxed at 18% (art. 170.13.1). Foreign corporate tax actually paid by the CFC, including withholding on its income, reduces this personal income tax, in proportion to the controlling share, if proof of payment is filed with the declaration (art. 170.13.2.4). The 5% military levy also applies: its object for individuals is the income in art. 163, which includes total annual taxable income (art. 163.1.1), and only income left out of total taxable income is exempt (section XX, subsection 10, point 16-1, sub-points 1.2, 1.3 and 1.7). The foreign tax credit in art. 170.13.2.4 reduces the personal income tax only, not the levy.
- **Distributions by a CFC to an individual (art. 170.13.2).** Distributed before the CFC report is filed: the 9% dividend rate applies to what is received. Distributed after the report but before the end of the second calendar year after the reporting year: the tax on the CFC profit is recomputed at 9% through a corrective declaration. Distributed later: no recomputation, and the amount is not taxed again.
- **Return of capital.** Amounts an individual receives from a foreign entity that are not a profit distribution under IFRS, up to the capital the individual (or family of the first and second degree) put in, are not taxable income (art. 170.13-1(2)).

**Foreign income and foreign tax credits.**

- *Resident companies.* Foreign corporate income tax paid is credited, up to the Ukrainian tax for the period. Taxes on capital or property, gains, postal, sales and other indirect taxes are not credited. A written confirmation from the foreign tax authority and a tax treaty in force are needed (art. 141.4.9).
- *Resident individuals.* Foreign income goes into total annual taxable income at 18% (art. 13.3, 170.11.1). Dividends from non-residents are taxed at 9% (art. 167.5.4). Foreign tax is credited where a treaty allows, on the annual declaration (art. 170.11.2), with a certificate from the foreign tax authority on the tax paid and the base, legalised unless a treaty says otherwise (art. 13.5).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Withholding on payments to non-residents | Paid to the budget at the time of payment | art. 141.4.2 |
| Report on income paid to non-residents and tax withheld | Each quarter in which such payments were made, on the form and deadline set by the Ministry of Finance | art. 103.9 |
| Residence certificate | Given to the payer before the treaty rate or exemption is applied. A certificate for the prior year may be used in the current year if the current one follows after year end | art. 103.4, 103.8 |
| Refund of tax withheld above the treaty rate | Application to the tax office of the payer, with documents | art. 103.11 |
| Non-resident buyer of property-rich shares | Registers with the tax authority by the first payment | art. 141.4.2, 64.5 |
| Corporate income tax return of a controlling company, with the CFC report | Within 60 calendar days after the year end for annual filers | art. 49.18.3, 39-2.5.2 |
| Annual declaration of a controlling individual, with the CFC report | By 1 May of the next year. For 2026, 1 May 2027 is a Saturday, so the deadline moves to the next operational day (art. 49.20). Tax paid by 1 August | art. 49.18.4, 39-2.5.2, 179.7 |
| CFC financial statements | Certified copies attached to the CFC report. If the foreign deadline for the statements is later, they go with the next year's declaration or return | art. 39-2.5.2 |
| Notice of acquiring or disposing of a CFC, or starting or ending actual control | Within 60 days of the event | art. 39-2.5.5 |
| Reply to a tax authority request on a CFC | Within two months | art. 39-2.6.2 |
| Resident leaving Ukraine for permanent residence abroad | Declaration no later than 60 calendar days before departure | art. 179.3 |

**Martial law.** A taxpayer that cannot file or pay on time because of martial law, including under art. 39-2, is released from liability, but must meet the obligation within six months after martial law ends (section XX, subsection 10, point 69.1).

**Martial law, CFC fines (section XX, subsection 10, point 72).** For breaches committed from 1 January 2022 to the last day of the month in which martial law ends, the art. 120.7 fines for a CFC report not filed, filed late or incomplete, and for a missing 60-day notice, are not charged, if the controlling person meets its art. 39-2 duties within six months after martial law ends. No administrative or criminal liability applies to art. 39-2 breaches in that period. The limitation period for assessing tax on information in a CFC report runs from the day the report is filed. Point 72 waives these fines only, not the tax.

## Penalties and interest

Fines in multiples are multiples of the subsistence minimum for an able-bodied person set by law on 1 January of the tax year: UAH 3,328 for 2026 (State Budget Law 2026, art. 7).

| Breach | Fine | Source |
|---|---|---|
| Withholding on a non-resident payment not charged, withheld or paid | 10% of the tax; 25% if intentional; 50% if an intentional breach is repeated within 1,095 days; 75% the third time or more within 1,095 days | art. 125-1.1 to 125-1.4 |
| CFC report not filed | 100 times (UAH 332,800) | art. 120.7 |
| CFC report filed late | 1 time (UAH 3,328) a day, capped at 50 times (UAH 166,400) | art. 120.7 |
| CFC left out of the report, or required details missing | the higher of 3% of the CFC's income and 25% of its adjusted profit, capped at 1,000 times (UAH 3,328,000) per CFC | art. 120.7 |
| No 60-day notice of acquiring or disposing of a foreign company or control | 300 times (UAH 998,400) for each event | art. 120.7 |
| Documents on a CFC not provided on request | 3% of the CFC's income, capped at 1,000 times | art. 120.7 |
| CFC report still not filed 30 days after the deadline to pay the fine | 5 times (UAH 16,640) a day, capped at 300 times | art. 120.7 |
| Extra tax assessed after an audit | 10% of the assessed tax; 25% if intentional | art. 123.1, 123.2 |
| Penalty interest on tax paid late | 120% a year of the NBU discount rate, for each day late | art. 129.4 |

## Cross-border points

- **Treaty relief at source (art. 103.2).** The payer may itself apply a treaty exemption or reduced rate at the time of payment, if the non-resident is resident in the treaty state and, where the treaty requires, is the beneficial owner. It needs the residence certificate under art. 103.4. A treaty benefit is refused where the main or predominant purpose of the transaction was to obtain it, unless that benefit matches the object and purpose of the treaty.
- **Residence certificate (art. 103.4, 103.5).** Issued by the competent authority named in the treaty, on that country's form, legalised and translated as Ukrainian law requires. A notarised copy is accepted. Interest to a foreign bank needs no certificate if the bank appears in the SWIFT bank identifier directory (art. 103.7). Without a certificate, Ukrainian rates apply (art. 103.10).
- **Beneficial owner (art. 103.3).** An agent, nominee or conduit is not the beneficial owner. Signs include passing the income on to another person without substantial functions, assets or risks, or lacking staff and resources. Where the direct recipient is a conduit, the treaty with the beneficial owner's state may be applied, with statements from both.
- **Refunds (art. 103.11 to 103.14).** A non-resident that suffered tax above the treaty rate applies to the tax office of the payer. On approval, the payer pays the difference back to the non-resident.
- **Treaty rates.** Rates under each treaty are not listed here. Read the treaty itself.
- **Transfer pricing.** Deals with related non-residents and listed low-tax states above the thresholds are controlled: [ua-transfer-pricing](ua-transfer-pricing.md).
- **30% add-back.** 30% of the cost of goods, services and fixed assets bought from non-residents in states on the Cabinet of Ministers list is added back, unless the deal is a controlled transaction (art. 140.5.4; see [ua-corporate-income-tax](ua-corporate-income-tax.md)).

## Worked examples

**Example 1. A company pays a foreign licensor and a foreign shipper.** A Ukrainian company pays a royalty of UAH 2,000,000 to a non-resident licensor that has not given a residence certificate, and freight of UAH 1,000,000 to a non-resident carrier. It withholds 15% of the royalty, UAH 300,000 (art. 141.4.2), and 6% of the freight, UAH 60,000 (art. 141.4.4). It also paid UAH 850,000 for engineering services to a third non-resident and forgot to withhold. It must pay the tax from its own funds, grossed up: 850,000 x 100 / 85 - 850,000 = UAH 150,000 (art. 141.4.2). If the tax authority finds this, the fine is 10%, UAH 15,000 (art. 125-1.1), plus penalty interest. Total tax to the budget: UAH 510,000.

```oa-check
name: Ukraine withholding on royalty, freight and a missed payment with gross-up
inputs:
  royalty: 2000000
  freight: 1000000
  engineering_paid_net: 850000
steps:
  - royalty_wht: royalty * 0.15
  - freight_wht: freight * 0.06
  - grossed_up_tax: engineering_paid_net * 100 / (100 - 15) - engineering_paid_net
  - fine_125_1: grossed_up_tax * 0.10
  - total_tax: royalty_wht + freight_wht + grossed_up_tax
expected:
  royalty_wht: 300000
  freight_wht: 60000
  grossed_up_tax: 150000
  fine_125_1: 15000
  total_tax: 510000
```

**Example 2. An individual with a low-taxed passive CFC (edge case: every exemption fails).** A Ukrainian resident owns 100% of a foreign company in a state with which Ukraine has a tax treaty. In 2026 the company's income is the equivalent of EUR 3,000,000, 80% of it passive. Its profit before tax is UAH 10,000,000 and it paid UAH 500,000 of corporate tax, an effective rate of 5%. The rate is below 13% (18% less 5 points) and passive income is above 50%, so art. 39-2.4.1 does not exempt it. Income is above EUR 2,000,000, so art. 39-2.4.2.1 does not either. No profit is distributed before the report. The owner reports UAH 10,000,000 on the 2026 declaration, due on the first operational day after Saturday 1 May 2027 (art. 49.18.4, 49.20). Personal income tax at 18% is UAH 1,800,000, less the UAH 500,000 foreign tax credit (art. 170.13.2.4): UAH 1,300,000. The 5% military levy is UAH 500,000. Total due by 1 August 2027: UAH 1,800,000.

```oa-check
name: Ukraine individual CFC with all exemptions failing
inputs:
  cfc_profit: 10000000
  foreign_tax_paid: 500000
  passive_share_pct: 80
  cfc_income_eur: 3000000
steps:
  - effective_rate_pct: foreign_tax_paid / cfc_profit * 100
  - etr_threshold_pct: 18 - 5
  - etr_shortfall_pct: etr_threshold_pct - effective_rate_pct
  - passive_over_limit_pct: passive_share_pct - 50
  - income_over_eur_limit: cfc_income_eur - 2000000
  - pit_gross: cfc_profit * 0.18
  - pit_due: pit_gross - min(foreign_tax_paid, pit_gross)
  - military_levy: cfc_profit * 0.05
  - total_due: pit_due + military_levy
expected:
  effective_rate_pct: 5
  etr_threshold_pct: 13
  etr_shortfall_pct: 8
  passive_over_limit_pct: 30
  income_over_eur_limit: 1000000
  pit_gross: 1800000
  pit_due: 1300000
  military_levy: 500000
  total_due: 1800000
```

## Ask the client first

1. Where does the person live, where is the family, how many days were spent in Ukraine in 2026, and what citizenships do they hold? This settles residence.
2. What does the company pay to non-residents (interest, dividends, royalties, freight, services, rent), to whom, in which country, and does each payee have a current residence certificate and real substance?
3. Does the non-resident have staff, an office, a server, a construction site or an agent in Ukraine, and for how long?
4. Does the client own 10% or more of any foreign company, trust, fund or partnership, alone or with other Ukrainian residents? For each: country, tax actually paid, share of passive income, total income in EUR, and dates of acquisition or disposal.
5. Has any foreign company distributed profit to the client, and when, relative to the CFC report?
6. Is the client planning to leave Ukraine permanently, and when?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Ukraine (Податковий кодекс України), Law No. 2755-VI, consolidated text with amendments up to Law No. 4967-IX of 3 Sep 2026: arts. 13, 14.1.193, 14.1.213, 39-2, 44.3.1, 49.18.3, 49.18.4, 64.5, 102.1, 103, 120.7, 123.1, 123.2, 125-1, 129.4, 133.2, 134.1.7, 136.7, 137.9, 140.5.4, 141.4, 49.20, 162.1.2, 163, 164.1, 167.1, 167.5.4, 170.11, 170.13, 170.13-1, 179.3, 179.7; section XX subsection 10 points 16-1, 69.1, 72 | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (zakon.rada.gov.ua timed out from our network; official text read via the web.archive.org capture of 12 Oct 2026, https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print) |
| Law of Ukraine "On the State Budget of Ukraine for 2026", No. 4695-IX of 3 Dec 2025, art. 7 | https://zakon.rada.gov.ua/laws/show/4695-20 | 2026-10-30 (read via the web.archive.org capture of 4 Jan 2026, https://web.archive.org/web/20260104102448/https://zakon.rada.gov.ua/laws/show/4695-20/print) |
| State Tax Service of Ukraine | https://tax.gov.ua | 2026-10-30 (refused automated access with HTTP 403; not read) |

Not yet confirmed: treaty withholding rates and which treaties are in force; the form and deadline of the quarterly report under art. 103.9; the CFC report form and the detailed rules inside art. 39-2.3.2.1 and 39-2.3.2.4; the Cabinet list of recognised exchanges for art. 39-2.4.2.2 and 141.4.1; the states on the Cabinet low-tax list; whether the Tax Code charges any exit tax on unrealised gains (none found in sections III and IV); the NBU discount rate in 2026; any amendment after the 12 October 2026 archive capture.
