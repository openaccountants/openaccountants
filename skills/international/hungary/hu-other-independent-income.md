---
name: hu-other-independent-income
description: "Hungarian tax on four kinds of private-person income that sit outside sole-trader status, tax year 2026. Covers agricultural primary producers (mezőgazdasági őstermelő): the tax-free band up to half the annual minimum wage (HUF 1,936,800), flat-rate taxation with a 90% cost ratio up to HUF 38,736,000, itemised costs or the 10% cost ratio, the HUF 100,000 producer credit, the family farm, and their TB and szocho; other independent activity such as fees under a civil-law contract (megbízási díj) with the 10% flat cost, payer withholding, 18.5% TB and 13% szocho; crypto-asset gains (Szja tv. 67/C. §) at 15% with annual netting and loss offset; and private accommodation (fizetővendéglátás) under the itemised flat tax of HUF 150,000 or HUF 38,400 per room (Szja tv. 57/A. §). Triggers: őstermelő adózás, megbízási díj adója, kriptoadó, kripto veszteség, magánszálláshely tételes átalányadó, Airbnb adó Magyarország. Out of scope: hu-income-tax, hu-capital-and-rental-income, hu-social-contributions, hu-payroll, hu-cross-border."
version: 0.2
jurisdiction: HU
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary: primary producers, civil-law contract fees, crypto gains and holiday letting (2026)

> **General reference only.** A source-cited draft, not reviewed by an accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Hungary.

This skill covers four kinds of income a private individual earns without being a registered sole trader (egyéni vállalkozó). The law is the personal income tax act, 1995. évi CXVII. törvény ("Szja tv."), the social security act, 2019. évi CXXII. törvény ("Tbj."), the social contribution tax act, 2018. évi LII. törvény ("Szocho tv."), and the procedure act, 2017. évi CL. törvény ("Art."). All four were read on 2026-10-23 in the consolidated text on the Nemzeti Jogszabálytár (njt.jog.gov.hu); njt.hu refused connections. The tax authority is the Nemzeti Adó- és Vámhivatal (NAV). Amounts are in forint (HUF). The tax year is the calendar year.

Many limits are multiples of the minimum wage. For 2026 the monthly minimum wage is HUF 322,800 (426/2025. (XII. 23.) Korm. rendelet 2. § (1)). The "annual minimum wage" (éves minimálbér) is 12 times the minimum wage in force on 1 January: HUF 3,873,600 (Szja tv. 3. § 84.).

See also, in this pack: `hu-income-tax` (sole traders: átalányadó, vállalkozói szja, KATA), `hu-capital-and-rental-income` (interest, dividends, securities gains, long-term letting, real estate sales, the annual return), `hu-social-contributions` (TB and szocho for sole traders and company members), `hu-payroll` (employees and the allowances that reduce the consolidated base), `hu-cross-border` (residence, treaties, non-residents), `hungary-vat-return` (VAT). This skill does not repeat them.

## Who this applies to

- **Agricultural primary producers (mezőgazdasági őstermelő).** A person aged 16 or over, entered in the primary producer register kept by the agricultural chamber (Magyar Agrár-, Élelmiszergazdasági és Vidékfejlesztési Kamara, known as NAK), farming in their own holding (Szja tv. 3. § 18.; családi gazdaságokról szóló 2020. évi CXXIII. törvény ("Csgtv.") 3. § (1)-(2), 4. § (1)). The holding can be owned or rented land and equipment, provided the producer decides how production runs and what happens to the crop. An activity in the register cannot also be run as a sole trader (Csgtv. 3. § (3)). Members of an **őstermelők családi gazdasága** (family farm of related producers) are primary producers too (Szja tv. 3. § 18.). Members of a **családi mezőgazdasági társaság** (a family agricultural company) are not: that is a company (NAV information sheet 6, section 1).
- **Other independent activity (önálló tevékenység).** Any activity that brings income and is not employment (Szja tv. 16. § (1)). This skill covers the common case of a private person paid a fee under a civil-law contract: a megbízási szerződés (agency or services contract), a vállalkozási szerződés outside sole-trader status, or a felhasználási szerződés (licence of a work), plus elected local councillors and auditors (NAV information sheet 2, section 1). Letting real estate for the long term is in `hu-capital-and-rental-income`.
- **Crypto-asset holders.** Any individual who sells, spends or otherwise gives up a crypto-asset for something that is not a crypto-asset (Szja tv. 67/C. § (2)). A crypto-asset is a digital representation of value or rights that can be transferred and stored electronically using distributed ledger or similar technology (Szja tv. 3. § 102.).
- **Private accommodation hosts (fizetővendéglátó).** A person who, not as a sole trader, provides private accommodation (magánszálláshely-szolgáltatás) under the commerce act to the same guest for no more than 90 days in the tax year (Szja tv. 57/A. § (1)). A magánszálláshely is a flat, holiday home or similar with at most eight rooms and sixteen beds (NAV information sheet 10, Fizetővendéglátás).
- **Out of scope:** sole traders in any of these activities (`hu-income-tax`), employees (`hu-payroll`), long-term letting and the sale of property (`hu-capital-and-rental-income`), letting farmland (Szja tv. 17. § (4), 73. §), VAT on farm produce (the compensation surcharge regime) and EKHO.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal income tax on independent-activity income | 15% of income in the consolidated base | 2026 | Szja tv. 8. § (1), 29. §, https://njt.jog.gov.hu/jogszabaly/1995-117-00-00 |
| Monthly minimum wage | HUF 322,800 | 2026 | 426/2025. (XII. 23.) Korm. rendelet 2. § (1), https://njt.jog.gov.hu/jogszabaly/2025-426-20-22 |
| Annual minimum wage (12 x monthly at 1 January) | HUF 3,873,600 | 2026 | Szja tv. 3. § 84. |
| **Primary producer:** revenue with no income to compute and nothing to declare | Up to half the annual minimum wage, HUF 1,936,800. Above it, the whole revenue counts | 2026 | Szja tv. 23. §, 11. § (3) a); NAV information sheet 6, section 2.2 |
| Primary producer: flat-rate taxation (átalányadózás) applies by default | Revenue up to 10 x the annual minimum wage, HUF 38,736,000 | 2026 | Szja tv. 50. § (2); 8. számú melléklet 1. |
| Primary producer on flat rate: cost ratio | 90%, so income is 10% of revenue | 2026 | Szja tv. 53. § (1) d) |
| Primary producer on flat rate: tax-free income | Income up to half the annual minimum wage, HUF 1,936,800, which means revenue up to HUF 19,368,000 is tax-free | 2026 | Szja tv. 1. számú melléklet 4.26.; NAV information sheet 6, section 2.3.2 |
| Primary producer family farm: flat-rate ceiling | Members at year end x 10 x the annual minimum wage, at most 40 x (HUF 154,944,000) | 2026 | Szja tv. 6. számú melléklet 3. |
| Primary producer credit (őstermelői adókedvezmény), itemised or 10% route only | Up to HUF 100,000 off the tax on the producer income (de minimis aid) | 2026 | Szja tv. 39. § (1) |
| Primary producer: supplementary activity (kiegészítő tevékenység) | Counts as producer revenue only while it is no more than one quarter of the year's producer revenue; above that, all of it is independent-activity income | 2026 | Szja tv. 3. § 85.; Csgtv. 3. § (4) |
| Primary producer: TB contribution base | 92% of the minimum wage a month, HUF 296,976; or, if 2025 producer revenue (without subsidies) was not more than HUF 17,448,000, 15% of the 2025 revenue spread over 12 months. HUF 17,448,000 is 5 x the 2025 annual minimum wage (12 x HUF 290,800) | 2026 | Tbj. 41. § (1)-(3), https://njt.jog.gov.hu/jogszabaly/2019-122-00-00; 394/2024. (XII. 12.) Korm. rendelet 2. § (1) |
| TB contribution (társadalombiztosítási járulék) | 18.5% | 2026 | Tbj. 25. § (1) |
| Primary producer: szocho base, itemised or 10% route, insured | Producer income, at least the minimum wage a month; none if revenue is up to HUF 1,936,800 | 2026 | Szocho tv. 7. § (1), https://njt.jog.gov.hu/jogszabaly/2018-52-00-00 |
| Primary producer: szocho base, flat rate, insured | The minimum wage a month (HUF 322,800); none if revenue is up to HUF 19,368,000 | 2026 | Szocho tv. 7. § (2) |
| Social contribution tax (szocho) | 13% | 2026 | Szocho tv. 2. § (1) |
| **Civil-law contract fee:** flat cost (10 százalék költséghányad) | Income = 90% of the fee | 2026 | Szja tv. 17. § (3) b) |
| Civil-law contract: insured, so TB is due | When the month's contribution-base income reaches 30% of the minimum wage, HUF 96,840 (HUF 3,228 a day) | 2026 | Tbj. 6. § (1) f); NAV information sheet 2, section 4 |
| Civil-law contract: szocho | 13% of the income, paid by a Hungarian or foreign payer on top of the fee; by the individual if the fee is not from a payer | 2026 | Szocho tv. 1. § (1), 3. § (2) |
| Cost declared to the payer for the advance | At most 50% of the fee | 2026 | Szja tv. 47. § (2) a) aa) |
| Advance paid by the individual | 15%, quarterly by the 12th of the month after the quarter; nothing due while the year's total is HUF 10,000 or less | 2026 | Szja tv. 46. § (9) |
| Difference penalty (különbözeti bírság) | 12% of costs declared to a payer but not proved in the return; none if the difference is HUF 10,000 or less | 2026 | Szja tv. 48. § (4) a) |
| **Crypto:** tax on the net gain of the year | 15%; no szocho | 2026 | Szja tv. 8. § (1), 67/C. § (1)-(2); Szocho tv. 1. § (5) |
| Crypto small-transaction exemption | A transaction with proceeds up to 10% of the minimum wage (HUF 32,280) is ignored, if no other same-subject transaction on that day and these exempt proceeds total no more than the minimum wage (HUF 322,800) in the year | 2026 | Szja tv. 67/C. § (2) |
| Crypto loss offset (adókiegyenlítés) | A declared loss of the year or any earlier year x 15%, limited to the crypto tax declared for the year and the two years before, less credits already used | 2026 | Szja tv. 67/C. § (5)-(7) |
| **Private accommodation:** itemised flat tax (tételes átalányadó), per room a year | HUF 150,000 in a settlement with over 2 million guest nights two years earlier (for 2026: Budapest); HUF 38,400 elsewhere | 2026 | Szja tv. 57/A. § (4), (4c); NAV information sheet 10, Fizetővendéglátás section 3 and question 23 |
| Private accommodation: who may elect | At most three properties, owned or held in usufruct; not rented flats | 2026 | Szja tv. 57/A. § (2); NAV information sheet 10, question 3 |
| Private accommodation on independent-activity rules | 15% szja on income, plus 13% szocho | 2026 | Szja tv. 17. § (3); NAV information sheet 10, Fizetővendéglátás section 5 |
| Annual return and payment deadline | 20 May 2027 for tax year 2026 | 2026 | Szja tv. 12/C. § (6), 67/C. § (8); NAV information sheet 6, section 2.3.4 |
| Failure-to-file penalty (mulasztási bírság), individual | A missing return: NAV first sets a 15-day deadline, then fines HUF 50,000, then HUF 200,000 with a further 15-day deadline. Other breaches, including late filing: up to HUF 400,000 | 2026 | Art. 220. § (1), 221. § (1)-(3), https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 |
| Tax penalty (adóbírság) | 50% of the shortfall; 200% where income was hidden or records falsified | 2026 | Art. 215. § (3)-(4) |
| Late payment interest (késedelmi pótlék) | Central bank base rate plus 5 percentage points, per day /365. Base rate 5.50% (unchanged on 20 October 2026), so 10.50% a year | 2026 | Art. 209. § (1); MNB press release of 20 October 2026, https://www.mnb.hu/en/monetary-policy/the-monetary-council/press-releases/2026/press-release-on-the-monetary-council-meeting-of-20-october-2026 |

## The taxable base

### Agricultural primary producers

**Revenue.** Everything received in connection with the producer activity, under Szja tv. 2. and 4. számú melléklet: sale proceeds, advances, payments in kind, insurance payouts and damages (NAV information sheet 6, section 2.1). Subsidies paid under a law or treaty are not revenue at all and do not count towards any limit (Szja tv. 7. § (3); NAV information sheet 6, section 2.1). The sale of farm equipment or land is not producer revenue: it is taxed as the sale of movable property or real estate (Szja tv. 58.-62. §).

**The tax-free band.** If producer revenue for the year is not more than HUF 1,936,800, no income is computed and nothing is declared, whichever method applies (Szja tv. 23. §, 11. § (3) a)). One forint above it, the whole revenue is in.

**Three ways to reach income.**
1. **Flat rate (átalányadózás), the default.** A producer with revenue up to HUF 38,736,000 is on flat rate unless they opt out (Szja tv. 50. § (2)). The opt-out is made by the deadline of the previous year's return, so 20 May 2026 for 2026, and must be repeated each year (8. számú melléklet 1.; NAV information sheet 6, section 2.3.1). Income is 10% of revenue (53. § (1) d)). Income up to HUF 1,936,800 is tax-free (1. számú melléklet 4.26.). Revenue up to HUF 19,368,000 therefore bears no tax, but must still be declared once it passes HUF 1,936,800 (NAV information sheet 6, section 2.3.4). All costs, including depreciation, are deemed claimed (54. § (1)).
2. **Itemised costs (tételes költségelszámolás).** Revenue less documented costs under the 3. számú melléklet and depreciation under the 11. számú melléklet (17. § (3) a) aa)). Costs above revenue become a carried-forward loss (elhatárolt veszteség), usable against producer income of the next five years; in a year the offset is limited to 50% of producer income before it (22. § (1)-(2)). A loss can instead be carried back two years by self-revision, at 30% a year (22. § (5)).
3. **10% cost ratio.** Income is 90% of revenue (17. § (3) b)).

On the itemised and 10% routes the producer credit takes up to HUF 100,000 off the tax on producer income. The tax on that income is computed as the consolidated-base tax with and without it. The return must show the producer's customer ID in the farm subsidy register (Szja tv. 39. § (1)).

**Producer income joins the consolidated base** with wages and other independent income and is taxed at 15% (Szja tv. 29. §). Allowances such as the family allowance reduce it (see `hu-payroll`).

**Family farm (őstermelők családi gazdasága).** At least two producers linked by a chain of family relationships farm together under a written contract; the family farm comes into being when NAK registers it (Csgtv. 6. § (1), 7. § (1)-(2)). All members use the same method; the representative notifies NAV (6. számú melléklet 1.). Revenue and costs are split by the contract's profit share, or equally (6. számú melléklet 2.). Each member files separately; one set of records is enough (6. számú melléklet 4.).

**TB and szocho for producers.** A producer is insured (biztosított) unless a minor family farm member, insured under another title other than a civil-law contract, or a pensioner (Tbj. 6. § (1) h); NAV information sheet 6, section 3.1). An insured producer pays 18.5% TB on 92% of the minimum wage, HUF 296,976 a month, or on 15% of the previous year's revenue if that revenue was small (Tbj. 41. § (1)-(3)). Szocho: on the itemised or 10% route, 13% of producer income, at least the minimum wage a month, nothing if revenue is up to HUF 1,936,800 (Szocho tv. 7. § (1)). On flat rate, 13% of the minimum wage a month, nothing if revenue is up to HUF 19,368,000 (Szocho tv. 7. § (2)). A producer who is not insured (for example, an employee) pays szocho only on producer income, with the same two revenue thresholds (Szocho tv. 7. § (3)). A pensioner's producer income bears no szocho (Szocho tv. 5. § (1) j)). Details of the TB return and family contribution credit are in NAV information sheet 6, sections 3.2-3.4.

### Civil-law contract fees and other independent activity

**Revenue** is the fee plus any cost reimbursement received for the work (Szja tv. 17. § (1)-(2)). **Income** is reached in one of two ways (17. § (3)):
1. **10% flat cost:** income is 90% of revenue, with no receipts. A cost reimbursement is also taxed at 90% (NAV information sheet 2, section 2.2). Using the flat cost for the advances does not lock it in: the return can itemise instead, provided the flat cost is used for none of the year's independent-activity revenue (Szja tv. 47. § (3)).
2. **Itemised costs:** documented costs under the 3. számú melléklet, up to the revenue. Assets under HUF 200,000 used only for the activity are expensed at once; dearer assets get a flat 1% of revenue, at most 50% of their value, once (NAV information sheet 2, section 2.3). A loss of one activity cannot offset another (17. § (3)).

The method chosen applies to all independent-activity income of the year (18. § (2)). The income joins the consolidated base at 15%.

**The 89% rule does not apply here.** Szja tv. 29. § and 47. § (5) count only 89% of income where the individual pays the szocho on it and cannot deduct it as a cost. For a fee from a payer, the payer pays the szocho (Szocho tv. 3. § (2)), so the full income is taxed. Where the individual pays szocho, for example on a fee from a private person, it is a recognised cost (3. számú melléklet I. 5.), so the exception in 29. § applies and the full income is taxed whichever cost method is used. NAV applies the 89% rule to independent activity only for the sale of property or movables as an economic activity (NAV information sheet 2, sections 2.4 and 3.2).

**TB.** A person working under a civil-law contract (other than a "tartós megbízás", a long-term contract the payer registers as such) is insured in a month when their contribution-base income from that payer reaches HUF 96,840, or HUF 3,228 per calendar day of the contract (Tbj. 6. § (1) f)). The base is the income counted for the advance; the 10% flat cost is not part of it (Tbj. 27. § (1) a); NAV information sheet 2, section 4). The payer withholds 18.5% (Tbj. 25. § (1)). A working pensioner is a supplementary-activity person and is not insured (NAV information sheet 2, section 4). Under a licence contract, only the pay for personal work is a contribution base, not the royalty (same section). A private person who engages an insured contractor is a foglalkoztató and carries the registration, withholding and reporting duties (Tbj. 1. § (4), 4. § 4.1.).

**Szocho** is 13% of the same income. A payer pays it on top of the fee; there is no cap (Szocho tv. 1. § (1), 2. § (1), 3. § (2)). If the payer is not a "kifizető" (for example a private person), the individual pays it with the szja (Szocho tv. 3. § (2)). Szocho is due even when TB is not, for example on a fee too small to make the person insured (NAV information sheet 2, section 4.1).

**Small amounts.** The 2026 Szja tv. has no general exemption for small civil-law fees. The only floor is for advances the individual pays: none is due while the year's total stays at or below HUF 10,000 (46. § (9)).

### Crypto-asset gains (Szja tv. 67/C. §)

- **Taxable event:** giving up a crypto-asset, by transfer or by exercising the right it carries, for value that is not a crypto-asset: fiat money, goods, services (67/C. § (2)). Exchanging one crypto-asset for another is not a taxable event. Putting crypto into a trust (bizalmi vagyonkezelés) or a private foundation is a taxable transaction, at the value the recipient books (67/C. § (3), as amended by 2026. évi XXXV. törvény).
- **Revenue:** the market value of the crypto-asset at the time of the transaction (67/C. § (3)).
- **Costs of the year:** the documented cost of crypto acquired in the tax year, fees and commissions, and documented costs of holding crypto (67/C. § (2), (4)). Mined or validated crypto: the documented costs of mining. Crypto received for work or services: its market value when received (67/C. § (4) e)).
- **Annual netting:** all of the year's transactions together. A gain is revenue less costs; a loss is costs less revenue, even with no sales (67/C. § (2)).
- **Small transactions:** a transaction with proceeds of at most HUF 32,280 is left out, if no other same-subject transaction gave proceeds that day and these left-out proceeds total no more than HUF 322,800 in the year (67/C. § (2)).
- **Tax:** 15% of the net gain, self-assessed in the return (67/C. § (8)). Crypto income is separately taxed; it is not in the consolidated base and allowances do not reduce it. It is not listed in Szocho tv. 1. § (5), so no szocho.
- **Losses:** a loss declared in the return for the year it arose gives a credit of loss x 15%, set against the crypto tax declared for the current year and the two years before, less credits already used (67/C. § (5)-(7)). The credit is treated as tax paid in the return. The individual keeps a record of unused losses and shows the total as information in each return (67/C. § (7a)).

### Private accommodation (Szja tv. 57/A. §)

**Who qualifies.** A private person, not a sole trader, who offers a magánszálláshely registered with the local notary (jegyző), with no guest staying more than 90 days in the year (57/A. § (1)). To use the itemised flat tax, the activity must be in at most three properties that the person owns or holds in usufruct (57/A. § (2)). A rented flat does not qualify (NAV information sheet 10, question 3).

**The itemised flat tax (tételes átalányadó).** Instead of tax on income, a fixed annual amount per room: HUF 150,000 in Budapest, HUF 38,400 elsewhere in 2026 (57/A. § (4); NAV information sheet 10, question 23). A room is any habitable room with space for at least one bed, whatever its size. At least one room per property is charged, even if guests come only a few months of the year (57/A. § (4b); NAV information sheet 10, section 3). The amount is paid in four equal instalments by the 12th of the month after each quarter (57/A. § (4a); 8. számú melléklet 9.). It is chosen for the whole year by a declaration attached to the previous year's return, or when registering for a new activity (8. számú melléklet 1.-2.; NAV information sheet 10, question 4). Revenue is not declared. No szocho is due under this method: the itemised flat tax computes no income, and Szocho tv. 1. § (1)-(5) taxes only the incomes it lists (NAV information sheet 10, section 5).

**If a condition fails.** From the first day of the quarter in which a condition stops being met, independent-activity rules apply; the flat tax is paid pro rata for the earlier quarters (57/A. § (5)). If the person could never have elected it, independent-activity rules apply to the whole year (57/A. § (6)).

**Independent-activity rules instead.** The host can always choose them. Income is 90% of revenue, or revenue less itemised costs, including depreciation of the property and renovation costs (17. § (3) a) ab); NAV information sheet 10, section 4). Tax is 15% plus 13% szocho, because the host is not insured under the Tbj. (NAV information sheet 10, section 5). Szocho tv. 5. § (2) h) exempts income from letting real estate, but NAV treats private accommodation as outside that exemption.

**Other charges.** Private accommodation is a VAT-able service at 5%; the VAT small-business exemption can apply (NAV information sheet 10, section 6; see `hungary-vat-return`). The host collects the local tourism tax (idegenforgalmi adó) set by the municipality (NAV information sheet 10, section 5). The host needs a tax number (adószám) from NAV on form T101 (NAV information sheet 10, section 1).

## Deadlines and filing

- **Registration.** A primary producer registers with NAK, then reports the activity to NAV on form T101 (NAV information sheet 6, section 1.1). A private accommodation host registers with the notary and requests a tax number on T101 (NAV information sheet 10, section 1). A civil-law contractor who is not VAT-registered can use their tax ID (adóazonosító jel) without a tax number (NAV information sheet 2, section 6).
- **Payer withholding on fees.** The payer (kifizető) withholds the 15% advance and 18.5% TB, pays its 13% szocho, and pays all by the 12th of the month after payment (Szja tv. 46. § (3), (8)). The individual declares at payment whether they use the 10% flat cost or itemised costs; without a declaration, the payer uses 90% (47. § (2) a) aa)).
- **Payments to producers.** A buyer does not withhold an advance from producer revenue if the producer proves their status at payment, for example with the NÉBIH register entry (46. § (4) a); NAV information sheet 6, section 2.9).
- **Quarterly advances.** A producer, and a contractor paid by a private person, pays a 15% advance by 12 April, 12 July, 12 October and 12 January (46. § (9)). A producer pays no advance until cumulative revenue passes HUF 1,936,800; a flat-rate producer then pays only on the advance base above HUF 1,936,800 (47. § (4) a)-b)). The producer credit reduces the advance (46. § (9)).
- **Producer TB and szocho.** An insured producer files the TB return on form 2658 and pays by the 12th of the month after each quarter (NAV information sheet 6, section 3.4). Szocho advances on the minimum-wage base start in the quarter in which revenue first passes the threshold (Szocho tv. 22. § (1)); the balance is settled in the annual return (22. § (2)).
- **Private accommodation flat tax.** Equal quarterly instalments by the 12th of the month after each quarter; on stopping the activity, within 15 days after that quarter (57/A. § (4a)).
- **Annual return (26SZJA for 2026).** Due 20 May 2027; NAV's return proposal (bevallási tervezet) is in eSZJA from 15 March 2027 (Szja tv. 12/C. § (1), (6)). A primary producer with taxable revenue must actively file: the proposal does not become their return by default (12/C. § (7)). Crypto gains and the crypto tax are self-assessed and paid by 20 May 2027 (67/C. § (8)); NAV has no payer data on them.
- **Records.** A producer keeps one of the basic records; a flat-rate producer can keep a simple revenue record or a sales sheet (értékesítési betétlap) (Szja tv. 5. számú melléklet; NAV information sheet 6, section 2.3.5). A contractor paid only by payers and using the 10% flat cost keeps just the payer certificates (NAV information sheet 2, section 6.1).

## Penalties and interest

- **Missing return:** NAV calls on the individual to file within 15 days; if they do not, mulasztási bírság of HUF 50,000 and a second call, then HUF 200,000 and a third call (Art. 221. § (1)-(3)).
- **Late return or other breach:** mulasztási bírság up to HUF 400,000 for an individual (Art. 220. § (1)).
- **Tax shortfall found by NAV:** 50% of the shortfall, 200% where income was hidden or records falsified (Art. 215. § (3)-(4)). Undeclared crypto gains and unregistered holiday letting fall here.
- **Late payment:** késedelmi pótlék at the base rate plus 5 percentage points a year, per day (Art. 209. § (1)); 10.50% a year at the 5.50% base rate set on 20 October 2026.
- **Costs declared to a payer but not proved:** 12% különbözeti bírság on the difference, in the return; none if it is HUF 10,000 or less (Szja tv. 48. § (4) a)).
- **Flat-rate election made wrongly:** if the producer or host was not entitled to the flat method, tax is recomputed under the general rules for the whole period (Szja tv. 56. § (2), 57/A. § (6)), with the penalties above on any shortfall.
- Self-revision surcharges and the other procedure rules are as in `hu-capital-and-rental-income`.

## Cross-border points

- **Residents** are taxed on worldwide income, including crypto gains on foreign exchanges and fees from foreign clients. A fee from a foreign payer: the individual pays the advance quarterly, and the szocho too if the fee is not a Hungarian contribution base (Szocho tv. 3. § (2)). No advance is due on income from a state without a tax treaty; the tax is settled in the return (Szja tv. 46. § (2) e)).
- **Insured abroad.** A person insured in another EU state under the coordination regulations, proved by an A1 or similar certificate, pays no szocho (Szocho tv. 5. § (4)). TB then follows the other state's rules; see `hu-social-contributions`.
- **Non-residents.** A Hungarian payer still withholds on a fee for work done in Hungary, subject to the treaty; see `hu-cross-border` for source and treaty relief. Holiday letting of Hungarian property is taxed in Hungary whoever the owner is, under the same choices as for a resident (NAV information sheet 10, question 7).
- **Crypto and moving.** Crypto gains are separately taxed income of a resident. Whether a treaty gives the gain to the state of residence, and how acquisition cost is set on arrival, is in `hu-cross-border`; Szja tv. 67/C. § has no special rule for arrivals.

## Worked examples

**Example 1: a civil-law contract fee of HUF 500,000 with the 10% flat cost.** Dóra, a Hungarian resident employee, signs a one-month megbízási szerződés with a Hungarian Kft. to write a market study. The fee is HUF 500,000, paid in October 2026. She declares the 10% flat cost to the Kft. She is not a pensioner and the contract is not registered as a long-term contract.

Income is 90% of the fee: HUF 450,000. The Kft. withholds the 15% advance, HUF 67,500. HUF 450,000 is above the HUF 96,840 monthly threshold, so she is insured for the month and the Kft. withholds 18.5% TB, HUF 83,250. Dóra receives HUF 349,250. On top of the fee, the Kft. pays 13% szocho on HUF 450,000: HUF 58,500. Its total cost is HUF 558,500. The 89% rule does not apply because Dóra does not pay the szocho. NAV's return proposal will carry the fee, the advance and the TB from the Kft.'s monthly return; she checks it and accepts it by 20 May 2027.

Edge case: if Dóra itemised and declared HUF 250,000 of costs (the 50% maximum) to the Kft., but could prove only HUF 100,000 in her return, she would owe the extra szja plus a 12% különbözeti bírság on the HUF 150,000 difference, HUF 18,000 (Szja tv. 48. § (4) a)).

```oa-check
name: HU civil-law contract fee 2026, HUF 500,000 with the 10% flat cost
inputs:
  fee: 500000
  flat_cost_pct: 10
  szja_pct: 15
  tb_pct: 18.5
  szocho_pct: 13
  minimum_wage: 322800
  declared_cost: 250000
  proved_cost: 100000
  penalty_pct: 12
steps:
  - income: fee - pct(fee, flat_cost_pct)
  - insurance_threshold: pct(minimum_wage, 30)
  - szja_advance: pct(income, szja_pct)
  - tb: pct(income, tb_pct)
  - net_to_contractor: fee - szja_advance - tb
  - payer_szocho: pct(income, szocho_pct)
  - payer_total_cost: fee + payer_szocho
  - difference_penalty: pct(declared_cost - proved_cost, penalty_pct)
expected:
  income: 450000
  insurance_threshold: 96840
  szja_advance: 67500
  tb: 83250
  net_to_contractor: 349250
  payer_szocho: 58500
  payer_total_cost: 558500
  difference_penalty: 18000
```

**Example 2: crypto gains of HUF 3,000,000 and losses of HUF 1,000,000 in 2026.** Gábor, a Hungarian resident, sells crypto for forint several times in 2026. On the sales that made money, proceeds exceed their cost by HUF 3,000,000. On the others, cost exceeds proceeds by HUF 1,000,000. Fees are already in these figures. He had no crypto transactions before 2026.

Netting is annual, across all transactions, so his 2026 crypto income is HUF 2,000,000. The tax is 15%: HUF 300,000. There is no szocho. No one withholds it: he self-assesses it in his 2026 return and pays it by 20 May 2027.

Edge case: in 2027 he makes a net crypto loss of HUF 2,500,000 and declares it in his 2027 return. The credit is 15% of the loss, HUF 375,000. It is limited to the crypto tax declared for 2027, 2026 and 2025: HUF 300,000. He gets HUF 300,000 back as tax treated as paid. The unused HUF 75,000 of credit (HUF 500,000 of loss) stays on his loss record for later years, within the same rolling limit (Szja tv. 67/C. § (5)-(7a)).

```oa-check
name: HU crypto 2026, gains HUF 3,000,000 and losses HUF 1,000,000, then a 2027 loss
inputs:
  gains: 3000000
  losses: 1000000
  szja_pct: 15
  loss_2027: 2500000
steps:
  - net_income_2026: gains - losses
  - tax_2026: pct(net_income_2026, szja_pct)
  - credit_before_cap: pct(loss_2027, szja_pct)
  - credit_used_2027: min(credit_before_cap, tax_2026)
  - credit_carried: credit_before_cap - credit_used_2027
  - loss_carried: credit_carried / (szja_pct / 100)
expected:
  net_income_2026: 2000000
  tax_2026: 300000
  credit_before_cap: 375000
  credit_used_2027: 300000
  credit_carried: 75000
  loss_carried: 500000
```

## Ask the client first

1. Are you a registered sole trader for any of this activity? If so, `hu-income-tax` applies instead.
2. Producers: are you in the NAK register, alone or in a family farm, what was your producer revenue (without subsidies) in 2025 and what will it be in 2026, and did you opt out of the flat rate by 20 May 2026? These set the tax-free band, the method and the TB base.
3. Fees: who pays you (a Hungarian company, a foreign company, a private person), how much per month, are you a pensioner or insured in another EU state (A1), and which cost method did you declare? This decides TB, who pays the szocho and whether you pay advances.
4. Crypto: what did you sell or spend for fiat or goods in the year, at what value and cost, and do you have losses from earlier years that you declared? Crypto-to-crypto swaps alone are not taxed.
5. Private accommodation: how many properties and rooms, do you own them or hold usufruct, in which settlement, does any guest stay more than 90 days, and did you elect the flat tax in your 2025 return?

## Sources

| Source | URL | Read on |
|---|---|---|
| 1995. évi CXVII. törvény a személyi jövedelemadóról (Szja tv.), consolidated text: 3. § 18., 84., 85., 102.; 8. §; 11. §; 12/C. §; 16.-23. §; 29. §; 39. §; 46.-48. §; 50.-56. §; 57/A. §; 67/C. §; 1. számú melléklet 4.26.; 6. és 8. számú melléklet (annexes read via the njtGetBlock service) | https://njt.jog.gov.hu/jogszabaly/1995-117-00-00 | 2026-10-23 |
| 2019. évi CXXII. törvény (Tbj.): 1. § (4); 4. § 4.1.; 6. § (1) f), h); 25. § (1); 27. § (1); 41. § | https://njt.jog.gov.hu/jogszabaly/2019-122-00-00 | 2026-10-23 |
| 2018. évi LII. törvény a szociális hozzájárulási adóról (Szocho tv.): 1.-3. §, 5. §, 7. §, 22. § | https://njt.jog.gov.hu/jogszabaly/2018-52-00-00 | 2026-10-23 |
| 2017. évi CL. törvény az adózás rendjéről (Art.): 209. §, 215. §, 220.-221. § | https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 | 2026-10-23 |
| 426/2025. (XII. 23.) Korm. rendelet, 2026 minimum wage, 2. § (1) | https://njt.jog.gov.hu/jogszabaly/2025-426-20-22 | 2026-10-23 |
| 394/2024. (XII. 12.) Korm. rendelet, 2025 minimum wage (HUF 290,800), 2. § (1) | https://njt.jog.gov.hu/jogszabaly/2024-394-20-22 | 2026-10-23 |
| 2020. évi CXXIII. törvény a családi gazdaságokról (Csgtv.): 3. §, 4. § (1), 6. § (1), 7. § | https://njt.jog.gov.hu/jogszabaly/2020-123-00-00 | 2026-10-23 |
| NAV information sheet 2, Az önálló tevékenységből származó jövedelem és adózása (published 2026-01-09) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/02.-az-onallo-tevekenysegbol-szarmazo-jovedelem-es-adozasa-2026.-01.-09 | 2026-10-23 |
| NAV information sheet 6, A mezőgazdasági őstermelő adózása (published 2026-05-12) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/06.-a-mezogazdasagi-ostermelo-adozasa-2026-05-12 | 2026-10-23 |
| NAV information sheet 10, Ingatlan bérbeadásának és egyéb hasznosításának adózása, part on fizetővendéglátás (published 2026-02-03) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/10.-Ingatlan-berbeadasanak-es-egyeb-hasznositasanak-adozasa-2026.02.03 | 2026-10-23 |
| Magyar Nemzeti Bank, press release on the Monetary Council meeting of 20 October 2026 (base rate 5.50%) | https://www.mnb.hu/en/monetary-policy/the-monetary-council/press-releases/2026/press-release-on-the-monetary-council-meeting-of-20-october-2026 | 2026-10-23 |

Not yet confirmed: that private accommodation is outside the Szocho tv. 5. § (2) h) exemption for income from letting real estate rests on NAV information sheet 10, section 5; the Szja tv. treats the two activities separately (17. § (3) a) ab)), but the Szocho tv. does not define letting. NAV publishes no 2026 information sheet on crypto; the crypto section rests on the act alone.

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
