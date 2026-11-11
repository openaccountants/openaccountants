---
name: eg-real-estate-tax
description: >
  Use this skill whenever asked about Egyptian real estate taxes for tax year 2026, and keep the three
  apart. (1) The annual built real estate tax (الضريبة على العقارات المبنية) under Law 196 of 2008 as
  amended, administered by the Real Estate Tax Authority (مصلحة الضرائب العقارية) under the Ministry
  of Finance: 10% of the annual rental value after the 30% or 32% maintenance deduction, the EGP
  100,000 private residence exemption and the 2026 filing discounts. (2) The 2.5% income tax on
  disposals of built property and building land, Law 91 of 2005 art. 42, collected by the Egyptian Tax
  Authority. (3) Income tax on rents. Trigger on "Egypt real estate tax", "ضريبة العقارات", "الضريبة
  العقارية", "annual rental value tax", "property tax Egypt", "2.5% property sale tax Egypt", "ضريبة
  التصرفات العقارية", or any property tax question for Egyptian owners or landlords.
version: 0.2
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-02
depends_on:
  - workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: estate-wealth-tax
---

# Egypt Real Estate Tax (ضريبة العقارات) Skill v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers Egyptian taxes on real estate for tax year 2026 (calendar year). Reply in the user's language, English or Arabic. All amounts are in EGP. Three different taxes meet here; name the one you mean every time.

| Tax | Law | Charged on | Collected by |
|---|---|---|---|
| Built real estate tax (annual) | Law 196/2008, as amended in 2012 and 2026 | Owner or holder of the right of use, on the assessed annual rental value, whether the unit is let, used or empty | Real Estate Tax Authority (RTA, مصلحة الضرائب العقارية), Ministry of Finance (Law 196 art. 1) |
| Real estate disposal tax | Income Tax Law 91/2005 art. 42, as replaced by Law 151/2026 | Seller, on the gross value of each disposal of built property or building land | Egyptian Tax Authority (ETA) |
| Income tax on rents | Income Tax Law 91/2005, real estate income articles | Landlord, on rent received | ETA, inside the personal income tax return (`eg-income-tax`) |

## Who this applies to

- **Annual tax, who pays** (Law 196 art. 2 as replaced by Law 103/2012): the natural or legal person who has the right of ownership, use or exploitation of the built property, even under an unregistered deed. A legal person pays through its legal representative; a person without full capacity through the person who represents them.
- **What is taxed** (art. 8): every built property, whatever its material or use, permanent or not, on land or water, let or not, in any of three states: complete and occupied, complete and unoccupied, or occupied though not complete. A building that is neither complete nor occupied is not in that list. Also treated as built (art. 9): property used to run public utilities under concession or licence; vacant land attached to buildings or separate from them, walled or not; installations on roofs or facades if let or paid for.
- **Built property on agricultural land** pays the built tax, and the land under it is then not charged agricultural land tax (art. 10).
- **Outside the tax** (art. 11): state property used for a public purpose (state private property is taxed from the month after it is disposed of to individuals or legal persons); buildings for worship or religious teaching; property expropriated for public benefit, from actual taking.
- **Disposal tax, who pays** (Law 91 art. 42 as replaced by Law 151/2026, corrected by the Gazette correction of 8 Aug 2026): every disposal of built property or building land outside villages, however many disposals, by sale, will, gift or donation to anyone other than ascendants, spouses or descendants, or by granting a usufruct or a lease of more than 50 years. Heirs who sell inherited property pay it too.
- **Not here:** stamp tax on documents (`eg-stamp-duty`); a property dealer taxed as a business (Law 91 art. 19 item 7, `eg-income-tax` and `eg-corporate-tax`); VAT (`egypt-vat`).

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Built real estate tax rate | 10% of the taxable annual rental value | Law 196 art. 12 as replaced by Law 103/2012 | 2026 | https://eta.gov.eg/sites/default/files/2024-10/law-103-2012.pdf |
| Maintenance and expenses deduction | 30% of the annual rental value for residential use; 32% for non-residential use | Same article; covers every expense including maintenance, no receipts needed | 2026 | same |
| Private residence exemption | EGP 100,000 of net annual rental value | One unit used as private residence by the taxpayer and family (spouse and minor children); equal to a unit with a market value of about EGP 8 million; the claim is made in the declaration | 2026 | https://www.rta.gov.eg/news/amendments-and-facilities-real-estate-taxes |
| Non-residential deduction | EGP 1,200 of net annual rental value | Ministry of Finance explainer, 6 Oct 2026 | 2026 | https://mof.gov.eg/ar/media/learn-more/news-2 |
| Previous residence exemption | EGP 24,000 of annual rental value, one unit per owner (from 1 Jul 2013); EGP 6,000 per residential unit in the original 2008 text | Law 196 art. 18 item (d) as replaced by Law 103/2012 (original text: art. 18 item (d) of Law 196); superseded by the 2026 amendment | Before 2026 | https://eta.gov.eg/sites/default/files/2024-10/law-103-2012.pdf |
| Rental value from market value (assessment guide) | Capital value 60% of market value; annual rental value 3% of capital value | Ministry of Finance explainer; also the method of the Law 103/2012 table 1 | 2026 | https://mof.gov.eg/ar/media/learn-more/news-2 |
| Timely filing discount | 25% of the annual tax for residential units; 10% for non-residential | Declaration filed on time and correctly; continuing each year | 2026 | same |
| Advance payment discount | A further 5%, so 30% residential and 15% non-residential | Paid in advance before the committees finish the rental assessment; deducted from the 2027 tax, refunded in full if the unit turns out exempt | 2026 | same |
| Cap on rise at reassessment | Tax may not rise more than 30% (residential) or 45% (non-residential) over the tax of the previous five-year assessment | Law 196 art. 5 as replaced by Law 103/2012 | 2026 | https://eta.gov.eg/sites/default/files/2024-10/law-103-2012.pdf |
| Delay charge | Runs from 1 January after the year the tax is due, at the Central Bank credit and discount rate on the 1 January preceding that date plus 2%; part months and pounds dropped; an appeal or court case does not stop it | Law 196 art. 27. ETA circular 1/2026 gives 20.50% on 1 Jan 2026, so 2026 tax unpaid on 1 Jan 2027 runs at 22.50% a year | 2026 | https://eta.gov.eg/sites/default/files/2024-10/law-196-2008.pdf |
| Delay charge cap | Not more than the principal tax | 2026 amendment of Law 196; delay charges waived for those who paid before it took effect or within six months after, extended to 2 Apr 2027 | 2026 | https://www.rta.gov.eg/news/amendments-and-facilities-real-estate-taxes |
| Dispute settlement | Pay 70% of the disputed tax; the delay charge is waived | Disputes before appeal committees or courts; request within six months of the 2026 amendment's start (2 Oct 2026 per the MoF explainer), extended by the Minister to 2 Apr 2027. A second route, ending the dispute where the owner claims a reduction of more than 30%, was open to requests until 31 Dec 2026 (MoF explainer) | 2026 | https://www.rta.gov.eg/news/extending-period-submitting-real-estate-tax-declarations-until-end-december-2026 |
| Real estate disposal tax (income tax) | 2.5% of the gross disposal value, no deduction | Law 91 art. 42 as replaced by Law 151/2026 and corrected 8 Aug 2026; paid within 60 days of the disposal | From 29 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |

## The base

**Annual built real estate tax.**
1. The base is the annual rental value set by the survey and assessment committees in each governorate, by building standard, location and services (art. 13), not the rent actually paid and not the price. The assessment stands for five years; work on the next one starts at least one year and at most three years before the period ends (art. 4).
2. Deduct 30% (residential) or 32% (non-residential) for expenses (art. 12).
3. Deduct the exemption: EGP 100,000 for the one private residence; EGP 1,200 for a non-residential unit (RTA notice; MoF explainer). The Law 103/2012 table worked the previous EGP 24,000 the same way, as a deduction.
4. Tax is 10% of what is left. Take off the 25% or 10% timely filing discount, and the further 5% for advance payment where it applies.

**Exempt** (art. 18 as amended by Law 103/2012, which also repealed every exemption in other laws except those in issuing art. 4, and deleted item (c), the old exemption for property of political parties and professional syndicates): buildings of registered associations and labour organisations used as offices or for their purposes; non-profit educational institutions, hospitals, clinics, shelters and charitable homes; the private residence up to the exemption; cattle yards and cemetery buildings; youth and sports centres; property of foreign governments if Egypt gets the same treatment; buildings serving agricultural land; houses used for social occasions without profit. When an exemption ends, the owner must notify the RTA office within 60 days and tax runs from 1 January of the next year (arts. 18, 22).

**Relief (رفع الضريبة)** (art. 19): when the property becomes exempt, is wholly or partly demolished or ruined so it cannot be used, or vacant land becomes non-independent. The 2026 amendment adds inability to use the property after demolition or damage, and emergencies or force majeure (RTA notice). Under art. 20 relief ran from the first day of the month in which the request was filed until the reason ends; the RTA notice says the 2026 amendment counts it from the date the event occurred instead. No request is accepted unless the owner has paid the last instalment due and deposited EGP 50, refunded if the request is accepted (art. 20). The 2026 amendment also lets committees set up by the Minister write off tax debts and delay charges that cannot be collected in the cases the new text lists (RTA notice).

**Interaction with income tax.** Under Law 91 arts. 39 and 45 as replaced by Law 196 issuing art. 3: rent from a let built property is taxed on the actual rent less 50% for all costs; the built real estate tax paid is credited against the income tax due on that property, up to that tax; the 50% rule does not apply to property in the assets of a business or company (art. 46). For a business or company, Law 91 art. 23 item 3 (2005 text) lists as deductible the fees and taxes the business bears other than income tax, which on its words covers the annual built real estate tax on its premises.

**Disposal tax (income tax, ETA).** 2.5% of the value in the disposal contract; ETA bears the burden of proof if it disputes that value. Out: forced sales by administrative or court order; expropriation for public benefit or for improvement; gifts to the government, local units, public legal persons or public-interest projects; contributing the property in kind to a joint stock company if the shares are not sold for five years. Not treated as trading unless ETA proves a profit-making trade (art. 19 item 7), in which case the 2.5% paid is credited against the tax due.

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Five-yearly declaration | Every owner files a declaration for all properties owned, in the second half of the year before the new assessment | Law 196 art. 14(a); MoF explainer |
| Annual declaration | By end December each year: new properties, additions, changes in parts or use that affect the value, and properties whose exemption ended | Law 196 art. 14(b) |
| 2026 filing window | Declarations for the new facilities and discounts accepted until end December 2026 | RTA notice, 11 Oct 2026 |
| Exempt units | Must still be declared, with the exemption claim in the declaration; tenants do not file | MoF explainer |
| Owners with units in several offices | One declaration to any one of the offices; gradual move to electronic declarations | RTA notice, 10 Mar 2026 |
| Unregistered units | Taxed from the date the declaration is filed, not earlier | RTA notice, 10 Mar 2026 |
| Assessment notice and appeal | The assessment is published and notified; appeal within 60 days of notification to the RTA directorate, with an EGP 50 deposit; the appeal committee decides within 30 days and its decision is final (arts. 15 to 17). The RTA's own right to appeal assessments was removed in 2026 and appeals may be filed online | Law 196 arts. 15 to 17; RTA notice |
| Payment | Due 1 January; payable in two equal instalments, by end June and end December, or in full with the first; payable at the real estate tax directorates in the governorates and their offices, and electronically | Law 196 arts. 3, 6, 23; MoF explainer |
| Tenants | Jointly liable up to the rent owed, once notified by registered letter; their receipts count as payment | Law 196 art. 24 |
| Disposal tax | Seller pays within 60 days of the disposal; delay charge under Law 91 art. 110 from the next day | Law 91 art. 42 as replaced by Law 151/2026 |

**Steps for an owner (annual tax):**
1. Log in on the RTA declaration and payment service (https://services.rta.gov.eg/tax-declaration/list-data) or use the RTA mobile application.
2. Declare every unit, mark the one private residence and claim the exemption, and mark use (residential or not).
3. Submit by end December 2026 to keep the 25% or 10% discount; pay in advance for the extra 5% if the assessment is not finished.
4. Watch for the assessment notice; appeal within 60 days if the rental value is wrong. The RTA "Building laws" and "Real Estate Tax" pages refused the connection when read; see "Not yet confirmed".

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| No declaration, or a declaration with wrong data affecting not more than 10% of the tax | Fine EGP 200 to 2,000; doubled on a repeat within three years | Law 196 art. 30 |
| Evasion: false or forged papers to the committees, false papers to get an exemption, not declaring the end of an exemption, false papers to get relief | Fine EGP 1,000 to 5,000 plus compensation equal to the tax not paid | Law 196 art. 31 |
| Settlement of a crime | Before or after a final judgment, on paying the tax, the delay charge and the compensation; ends the criminal case | Law 196 art. 33 |
| Late payment | Delay charge as in the rates table, capped at the principal from 2026 | Law 196 art. 27; RTA notice |
| Late disposal tax | Delay charge under Law 91 art. 110 | Law 91 art. 42 |

Criminal proceedings need a written request from the Minister of Finance or delegate (art. 32).

## Cross-border points

- The annual tax follows the property, not residence: a non-resident owner pays it the same way. The RTA publishes an English declaration form for foreigners.
- Foreign governments' property is exempt only on reciprocity (art. 18).
- A non-resident who sells built property in Egypt pays the 2.5% disposal tax within 60 days. Income tax on rents of a non-resident landlord and treaty questions go to `eg-income-tax` and `eg-withholding-tax`.

## Two worked examples that recompute

**Case 1. Private residence, assessed annual rental value EGP 180,000, filed on time.** Less 30% = 126,000. Less exemption 100,000 = 26,000. Tax 10% = 2,600. Less 25% timely filing discount = 1,950.

```oa-check
name: Private residence, rental value EGP 180,000, 2026
inputs:
  arv: 180000
steps:
  - net: arv * 0.70
  - taxable: max(net - 100000, 0)
  - tax: taxable * 0.10
  - after_discount: tax * 0.75
expected:
  net: 126000.00
  taxable: 26000.00
  tax: 2600.00
  after_discount: 1950.00
```

**Case 2. Decision: shop owner, file on time and prepay, or not.** Assessed rental value EGP 200,000, non-residential. Less 32% = 136,000; less 1,200 = 134,800; tax 13,480. Filing late: 13,480. Filing on time: 10% off = 12,132. Filing on time and paying in advance before the assessment ends: 15% off = 11,458. Filing on time and prepaying saves 2,022 a year against filing late.

```oa-check
name: Shop, rental value EGP 200,000, filing choices
inputs:
  arv: 200000
steps:
  - taxable: arv * 0.68 - 1200
  - full: taxable * 0.10
  - on_time: full * 0.90
  - on_time_prepaid: full * 0.85
  - saving: full - on_time_prepaid
expected:
  taxable: 134800.00
  full: 13480.00
  on_time: 12132.00
  on_time_prepaid: 11458.00
  saving: 2022.00
```

The exemption in market terms: 100,000 / 0.70 / 0.03 / 0.60 is about EGP 7.94 million, which is why the RTA describes it as about EGP 8 million of market value. A sale of the same flat for EGP 3,000,000 is a different tax: 2.5% disposal tax, EGP 75,000, to ETA within 60 days.

## Ask the client first

1. Which tax: the annual built property tax, the 2.5% tax on a sale or other disposal, or income tax on rent?
2. For the annual tax: how many units, where (which RTA offices), residential or not, which one is the private residence, and the assessed rental value on the notice.
3. Has the 2026 declaration been filed, and when; any advance payment?
4. Any arrears, delay charges or open appeal (settlement and waiver window to 2 Apr 2027)?
5. For a disposal: date, contract value, who the buyer is (relative, government, company in-kind contribution), and is the seller a property dealer?
6. Is the owner an individual or a company (company rent and property in business assets do not use the 50% rule)?

Do not present output as a filed declaration or a professional sign-off.

## Sources

| Source | URL | Read on |
|---|---|---|
| Built Real Estate Tax Law 196 of 2008 with issuing law, Gazette 25 bis (c), 23 Jun 2008: issuing arts. 1 to 9, law arts. 1 to 35 (page images of the ETA text copy read) | https://eta.gov.eg/sites/default/files/2024-10/law-196-2008.pdf | 2026-11-02 |
| Same law, Gazette scan uploaded by ETA in March 2026: page 1 read to confirm the Gazette issue; the rest not relied on | https://eta.gov.eg/sites/default/files/2026-03/law.no_.196.of_.2008.pdf | 2026-11-02 |
| Law 103 of 2012 amending Law 196: arts. 1 to 6 and table 1 (arts. 2, 5, 12, 13, 15, 18, 28; start 1 Jul 2013); page images read | https://eta.gov.eg/sites/default/files/2024-10/law-103-2012.pdf | 2026-11-02 |
| RTA notice "Amendments and facilities for real estate taxes", 10 Mar 2026 (read for the EGP 100,000 exemption, discounts, delay charge cap, appeals, 70% settlement, relief) | https://www.rta.gov.eg/news/amendments-and-facilities-real-estate-taxes | 2026-11-02 |
| RTA notice, 11 Oct 2026, declarations extended to end December 2026, settlement and waiver to 2 Apr 2027 (read in full) | https://www.rta.gov.eg/news/extending-period-submitting-real-estate-tax-declarations-until-end-december-2026 | 2026-11-02 |
| Ministry of Finance explainer on the real estate tax, 6 Oct 2026 (read for the deductions, 1,200, 60% and 3% valuation, discounts, filing, payment, 60-day appeal) | https://mof.gov.eg/ar/media/learn-more/news-2 | 2026-11-02 |
| RTA home page (read for the links to the declaration and payment service and the English declaration form for foreigners) | https://www.rta.gov.eg/ | 2026-11-02 |
| RTA "Building laws" and "Real Estate Tax" pages | https://www.rta.gov.eg/building-laws | refused the connection (request rejected) on 2026-11-02, not read |
| Law 151 of 2026, arts. 1, 6, 7 (Law 91 art. 42 text, repeals, start date); Gazette 30 bis (a), 28 Jul 2026; text layer read | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-02 |
| Correction notice to Laws 149, 150, 151 of 2026, Gazette 32 bis, 8 Aug 2026: page 2 read (art. 42 not 43, "built" property) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-02 |
| Income Tax Law 91 of 2005, Gazette 23 (cont.), 9 Jun 2005: Gazette pp. 17 and 18 (arts. 22 to 24) read as page images | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-02 |
| ETA circular 1 of 2026, Central Bank credit and discount rates 2021 to 2026 (page image read; 20.50% on 1 Jan 2026) | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | 2026-11-02 |

Not yet confirmed: the number, Gazette date and article text of the 2026 amending law (press reports call it Law 3 of 2026; no official copy was found on eta.gov.eg or rta.gov.eg, and the RTA laws page refused the connection), so every 2026 figure above rests on RTA and MoF pages, not the law text. Whether residential units other than the one private residence get any deduction beyond the 30%, and whether the old aggregate EGP 2,000,000 market value test survives (the old version said it rose to EGP 8,000,000 in aggregate; the RTA gives about EGP 8 million per unit). Law 117 of 2014 and Law 23 of 2020 amending Law 196 (not on the ETA site), including the origin of the EGP 1,200 non-residential deduction. Which five-year assessment cycle is current (the old version mentioned none; a 2022 cycle is reported but not confirmed). Whether Law 91 arts. 39, 45 and 46 still read as Law 196 issuing art. 3 replaced them (later income tax amendments were not checked for these articles). Whether Law 91 art. 23 item 3 was amended after 2005 (later amending laws not checked for it); the old version's statement that the annual tax is not deductible for corporate income tax under art. 23, and its "common audit finding", are contrary to the 2005 text and were not carried. The old version's other items, not found in Law 196 or its 2012 amendment: a five-year exemption for new buildings (it cited art. 11, which lists state, worship and expropriated property), relief for units empty six months, heritage building relief, a flat "no tax on buildings under construction" (art. 8 does tax an incomplete building once it is occupied), payment at designated banks and post offices, the proof the old version said must go with an exemption claim (title deed, rental contract, valuation report), a different corporate tax treatment for real estate held for resale, the RTA nickname "Maamouria" and 44 offices, the transfer tax being RTA's under Law 196 art. 40 (it is ETA's, under Law 91 art. 42), and a "wealth tax on rental income at 10% to 27.5% under Law 91 art. 47" (rent is income tax on actual rent less 50%, at the progressive rates in `eg-income-tax`). Whether the 2.5% disposal tax is deductible or capitalised for income tax (the old version called it a capital cost, not deductible). The text of Law 91 art. 42 before Law 151/2026 (1 Jan to 28 Jul 2026), so the disposal tax rules before 29 Jul 2026 were not checked. The agricultural land tax under Law 113/1939 (not read). The executive regulations of Law 196 and the form numbers of the declaration.

> Contributed by Ahmed Hassan.
