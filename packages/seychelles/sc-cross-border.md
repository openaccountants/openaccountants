---
name: sc-cross-border
description: "Seychelles cross-border business tax for tax year 2026 under the Business Tax Act 2009 (Cap 20) as amended. Covers residence of individuals (183 days, domicile, normal residence) and entities (incorporation, management and control), the permanent establishment test in section 2A (90-day construction and services tests, dependent agents, preparatory or auxiliary exclusions), Seychelles-source rules in section 5 including the foreign passive income and economic substance rule for members of multinational groups, the final withholding tax on dividends, interest, royalties, natural resource amounts, technical services fees and insurance premiums paid to non-residents, the 33% rate on managerial fees paid by financial institutions, the 3% tax on non-resident ships and aircraft, treaty precedence and the MLI principal purpose test. Trigger on: Seychelles withholding tax non-resident, Seychelles permanent establishment, Seychelles tax residence, Seychelles foreign passive income, Seychelles DTA. Out of scope: treaty rates."
version: 0.2
jurisdiction: SC
category: cross-border
tax_year: 2026
last_updated: 2026-11-14
tier: 2
domain: cross-border
type: situation-rules
---

# Seychelles cross-border: residence, permanent establishment, source and withholding on non-residents (2026) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The Business Tax Act 2009 (Act 28 of 2009, now Cap 20) taxes business income from sources in Seychelles. Its rates are in the First Schedule, which S.I. 27 of 2010 replaced and later instruments amended. The Business Tax (Amendment) Act 2020 (Act 2 of 2021), in force from 15 September 2021 (S.I. 78 of 2021), added the permanent establishment section 2A and the foreign-income rules for multinational group members. The Seychelles Revenue Commission (SRC) administers the tax. The tax year is the calendar year (s 2), so this skill covers 1 January to 31 December 2026. Domestic business tax rates and penalty amounts live in [Corporate income tax](sc-corporate-income-tax.md); transfer pricing lives in [Transfer pricing](sc-transfer-pricing.md); employee tax rates live in [Personal income tax](sc-personal-income-tax.md).

## Who this applies to

- **Resident individuals** (BTA s 2, "resident person" (a)). An individual is resident if they:
  - reside in Seychelles ("resides" means normally resides, or has resided at least 183 days in a tax year, or is domiciled in Seychelles);
  - are domiciled in Seychelles, unless they have a permanent place of abode outside Seychelles; or
  - are present in Seychelles for 183 days or more in aggregate in any twelve-month period that begins or ends in the tax year.
- **Resident entities** (s 2 (b)). An entity incorporated, formed, organised or otherwise established in Seychelles, or managed and controlled in Seychelles.
- **Other residents** (s 2 (c) to (e)): a trust settled or established in Seychelles or with a resident trustee; a government body; a partnership in which one partner is resident.
- **Non-residents** are everyone else. They are taxed in Seychelles:
  - on business income attributable to a permanent establishment in Seychelles (s 5(2)), at the ordinary business tax rates;
  - by a final tax on the gross amount of a dividend, interest, royalty, natural resource amount, insurance premium or technical services fee from Seychelles sources (s 8, s 9), withheld by the payer (s 66(1));
  - by a final tax on gross carriage income of ships and aircraft (s 7, s 9);
  - through the promoter's or agent's withholding from the gross remuneration or receipts of non-resident entertainers and sports persons for a performance or event in Seychelles, "at the rate specified in the First Schedule" (s 66(2)). This is not an s 8 amount, so s 9 does not make it a final tax; tax withheld that is not final is credited against business tax (s 76(2), (3)). The rate is not stated here: see "Not yet confirmed".
- **Permanent establishment** (s 2A, from 15 September 2021). A person has a permanent establishment in a territory if it has there:
  - a fixed place of business through which its business is wholly or partly carried on, including a place of management, branch, office, factory, warehouse, workshop, mine, oil or gas well, quarry or other place of extraction (s 2A(1)(a), (2));
  - a building site or construction, assembly or installation project, including supervisory activities, but only if it continues for more than ninety days (s 2A(1)(b), (3));
  - services, including consultancy, through employees or other personnel, but only for periods aggregating more than ninety days in any twelve-month period beginning or ending in the financial year (s 2A(1)(c), (4));
  - an agent who habitually concludes contracts, or habitually plays the principal role leading to contracts routinely concluded without material modification, in the person's name, for its property or for its services (s 2A(1)(d), (5)). An agent of independent status acting in the ordinary course of its business is excluded (s 2A(6)), but not one acting exclusively or almost exclusively for closely related persons (s 2A(7)).
- **Not a permanent establishment:** a fixed place used solely for storage, display or delivery, for keeping stock for those purposes or for processing by another enterprise, for purchasing or collecting information, or for any other activity, if the activity (or the combined activity) is preparatory or auxiliary (s 2A(8)). The exclusion is lost where the person or a closely related enterprise carries on business at the same place or other places in the territory, their activities there form complementary functions of a cohesive business operation, and either one of those places is a permanent establishment of either of them or the combined activity is not preparatory or auxiliary (s 2B). "Closely related" means control, common control, or more than 50% of the beneficial interest, vote and value (s 2C). A subsidiary is not by itself a permanent establishment of its parent (s 2A(9)).

Not covered here, refer to a specialist: the rates and permanent establishment articles of each treaty; Seventh Schedule regimes; the Immovable Property Tax on non-Seychellois owners (see [Tax overview](sc-tax-overview.md)).

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official URL |
|---|---|---|---|
| Non-resident tax on a dividend, royalty, natural resource amount or technical services fee from Seychelles sources (s 8; First Schedule item 3(a)) | 15% of the gross amount, or the rate under a taxation agreement | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/SI-66-of-2012-Business-Tax-Amendment-of-Schedules-Regulations-2012.pdf |
| Non-resident tax on an insurance premium for a risk in Seychelles (item 3(b)) | 5% of the gross premium | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/SI-27-of-2010-Business-Tax-Act-2009-Business-Tax-Amendment-Schedules-Regulations.pdf |
| Technical fees, other than managerial fees, paid to a non-resident by a financial institution operating in Seychelles (First Schedule item 3(c), inserted by S.I. 92 of 2010 from 1 January 2011) | 15% | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/SI-92-of-2010-Business-Tax-Act-Business-Tax-Amendment-of-Schedules-No.-4-Regulations-2010.pdf |
| Managerial fees paid to a non-resident by a financial institution operating in Seychelles (item 3(d), same instrument); a managerial fee paid by any other payer is a technical services fee at 15% | 33% | 2026 | same |
| Interest to a non-resident (item 3(e)): current account; call deposit | 5% | 2026 | https://src.gov.sc/wp-content/uploads/2025/02/SI-107-2024-Business-Tax-Amendment-of-First-Schedule-Regulations-2024.pdf |
| Interest to a non-resident: fixed deposit (SCR or foreign currency) | 0% for individuals; 5% otherwise | 2026 | same |
| Interest to a non-resident: savings account, bank to bank, non-resident bank interest, Government Securities (bills and bonds issued by the Government and administered by the Central Bank) | 0% | 2026 | same |
| Interest to a non-resident paid by a person that is not a financial institution to a person that is not a financial institution | 15% | 2026 | same |
| Non-resident ship or aircraft operator, gross amount for carriage of passengers, livestock, mail, merchandise or goods embarked in Seychelles (s 7; First Schedule item 2) | 3% | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/SI-27-of-2010-Business-Tax-Act-2009-Business-Tax-Amendment-Schedules-Regulations.pdf |
| Permanent establishment time tests (s 2A(3), (4)) | Construction or installation: more than 90 days; services: more than 90 days in aggregate in any 12 months | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/Business-Tax-Amendment-Act-2020-Act-2-of-2021.pdf |
| Individual residence day test (s 2) | 183 days or more in any 12-month period beginning or ending in the tax year | 2026 | https://src.gov.sc/wp-content/uploads/2023/04/Business-Tax-Act-2009-1.pdf |
| Closely related enterprise (s 2C) | More than 50% of beneficial interest, or of vote and value of shares | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/Business-Tax-Amendment-Act-2020-Act-2-of-2021.pdf |
| Withholding tax payment (s 69; Revenue Administration Act s 20 as inserted by Act 27 of 2023) | By the 21st of the following month in person; by the 23rd through the SRC Tax Portal or bank transfer; Tax Portal compulsory for a large business or a payment of SCR 50,000 or more | 2026 | https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf |

No 2026 amendment to these rates was found on the SRC legislation page read on 2 November 2026, so 2026 rests on the instruments above staying in force. The SRC page still lists rates for bearer bonds and Treasury Bills and a flat 5% on fixed deposits; S.I. 107 of 2024 replaced the interest table from 1 January 2025 and the law wins. The SRC page also gives 5% for non-resident entertainers; no First Schedule item setting that rate was found (see "Not yet confirmed").

## The base

**Source (s 5).**
- **Residents, ordinary case (s 5(1), as substituted in 2021):** business income is from Seychelles sources if derived from activities conducted, goods situated or rights used in Seychelles. Income from activities abroad and passive income from abroad are not Seychelles-source, so they are outside the tax (the territorial basis the SRC describes).
- **Residents that are members of a multinational group (s 5(1A) and the Eleventh Schedule, as amended by S.I. 79 of 2021, gazetted on 16 September 2021 with no commencement date of its own; the SRC dates the change from 16 September 2021).** The Schedule applies to an enterprise that is a member of a multinational group: a group with enterprises resident in different jurisdictions, or with a permanent establishment in another jurisdiction. For such a company, Seychelles-source income also includes:
  - income from activities conducted outside Seychelles, unless attributable to a permanent establishment of the company outside Seychelles;
  - income from intellectual property held in Seychelles, other than the qualifying share of income from a patent or a right functionally equivalent to a patent (including copyrighted software), worked out on qualifying against overall expenditure (s 5(1B), (5));
  - passive income generated outside Seychelles (interest, rents, royalties, dividends, and capital gains from holding and managing shares), unless the company is a qualifying company with adequate economic substance.
- **Adequate economic substance (Eleventh Schedule para 3):** the company has met its filing duties under the Companies Act or the International Business Companies Act; has adequate human resources and premises in Seychelles for holding and managing the assets; and, unless it is a pure equity holding or real estate holding company, takes the strategic decisions, manages and bears the principal risks in Seychelles, and incurs adequate expenditure. Premises, people and risk management may be outsourced if the company shows adequate supervision and the work is done in Seychelles (para 4).
- **Non-residents (s 5(2)):** business income is from Seychelles sources to the extent attributable to a permanent establishment in Seychelles. Profits attributed to the permanent establishment must be arm's length under s 54(7), see [Transfer pricing](sc-transfer-pricing.md).
- **Always Seychelles-source (s 5(3)):** a fee for services performed in Seychelles; rent from real property in Seychelles; a dividend paid by a resident entity; interest, a royalty or a technical services fee paid by a resident (other than as an expense of its permanent establishment abroad) or by a non-resident as an expense of its Seychelles permanent establishment; a natural resource amount for resources taken in Seychelles; an insurance premium for a risk in Seychelles.

**Final tax on non-residents (s 8, s 9).** Tax under s 8 is levied on the gross amount and is a final tax: the income is left out of assessable income, nothing is deductible, no loss reduces it and no tax credit reduces the tax (s 9). It does not apply to exempt income, or to an amount attributable to the non-resident's Seychelles permanent establishment, which is taxed as business income instead (s 8(2)).
- **Technical services fee** (s 2 as substituted by Act 14 of 2012): consideration for managerial, technical or consultancy services, including services of technical or other personnel; for supplying technical, industrial, commercial or scientific knowledge, experience or skill; and for ancillary services for which royalties are received.
- **Who withholds:** the person paying the amount, from the gross, at the s 8 rate (s 66(1)), at the earlier of crediting the amount to the recipient's account and paying it (s 68). Nothing is withheld from exempt income (s 67).

**Ships and aircraft (s 7).** A non-resident operating a ship or aircraft pays 3% of the gross amount for carriage embarked in Seychelles, as a final tax (s 9). The liability is discharged when paid under s 60 or s 61.

**Branches.** A Seychelles permanent establishment of a non-resident pays business tax on its taxable income at the ordinary rates (s 6; see [Corporate income tax](sc-corporate-income-tax.md)). The Act's arrangement of sections contains no branch profits or remittance tax.

**Residents paying abroad.** The deduction a resident may claim for royalties and technical services fees paid to a non-resident is limited as prescribed in the Ninth Schedule (s 14(3)(a), inserted by Act 14 of 2012). The Ninth Schedule itself was not read.

**Relief for foreign tax.** The Act's arrangement of sections has no foreign tax credit section; s 76 credits Seychelles tax withheld only. Foreign income outside s 5 is simply not taxed. Relief beyond that comes from a taxation agreement (s 79).

**Employees.** A person is deemed employed in Seychelles if paid by a resident, by a person carrying on business or having its place of effective management or control in Seychelles, by someone on that person's behalf, or from a Seychelles source (Income and Non-Monetary Benefits Tax Act s 3(1)). A person performing services in Seychelles for a non-resident is deemed employed by the person who benefits in Seychelles, who must withhold and remit (s 3(3)). Rates for citizens and non-citizens are in [Personal income tax](sc-personal-income-tax.md).

**Treaties (s 79).** A taxation agreement entered into by the Minister has effect for business tax once declared by regulation, and its terms take precedence over the Act (s 79(1), (3), (4)). Agreements are listed in the Sixth Schedule (s 79(5)). The SRC lists 29 double taxation agreements in force: Bahrain, Barbados, Belgium, Bermuda, Botswana, China, Cyprus, Ethiopia, Guernsey, Indonesia, Isle of Man, Jersey, Kenya, Kuwait, Luxembourg, Malaysia, Mauritius, Monaco, Oman, Qatar, San Marino, Singapore, South Africa, Sri Lanka, Swaziland, Thailand, United Arab Emirates, Vietnam and Zambia.
- **Anti-treaty-shopping:** Seychelles deposited its instrument of ratification of the MLI on 14 December 2021 and the MLI entered into force for Seychelles on 1 April 2022; each treaty's MLI provisions take effect on their own dates (for South Africa, withholding taxes from 1 January 2023). In the SRC's synthesised text of the South Africa agreement, the MLI principal purpose test (Article 7(1)) applies: a treaty benefit is denied where obtaining it was one of the principal purposes of an arrangement, unless granting it accords with the object and purpose of the provisions.
- **Domestic anti-avoidance:** the Act has a general anti-avoidance rule (s 55) and transfer pricing (s 54); s 55 was not read.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Payer remits tax withheld from a non-resident (dividend, interest, royalty, technical services fee, natural resource amount, insurance premium, entertainers) | Within 21 days after the end of the month of withholding (s 69); monthly tax and returns by the 21st in person or the 23rd through the Tax Portal or bank transfer (Revenue Administration Act ss 3(1), 20) | BTA s 69; Act 27 of 2023 ss 3, 4 |
| Withholding tax remittance form | Lodged within the period and in the form prescribed (s 73, as substituted by Act 27 of 2023); the SRC page tells payers to remit with the Business Activity Statement | Act 27 of 2023 s 7; SRC Tax System page |
| Non-resident ship | Before departure, the master or local agent files a return of gross carriage revenue; SRC assesses and notifies; SRC may allow the return within 30 days after departure if payment is arranged; customs withholds port clearance until paid or arranged | BTA s 60 |
| Non-resident aircraft | Quarterly return within 21 days after the end of each quarter, with payment by that date; unpaid after three months, SRC may ask the Civil Aviation Authority to refuse clearance | BTA s 61, as amended by Act 25 of 2010 |
| Permanent establishment of a non-resident | Annual business tax return and payment by 31 March after the tax year, as for any business; see [Corporate income tax](sc-corporate-income-tax.md) | BTA ss 57, 59 |

How to pay: log in to the SRC Tax Portal at [tms.src.gov.sc](https://tms.src.gov.sc/) or lodge at SRC, complete the withholding tax remittance form or Business Activity Statement for the month, and pay. Bank details and the cheque limits are in [Corporate income tax](sc-corporate-income-tax.md). Form box numbers were not read.

## Penalties and interest

- **Failure to withhold or pay over:** a payer that fails to withhold, or withholds and fails to pay by the s 69 date, is personally liable for the tax (s 70(1)). The amount is treated as revenue under Part V of the Revenue Administration Act (s 70(2)). A payer liable because it did not withhold may recover the tax from the recipient (s 70(3)); SRC may also recover it from the recipient, up to the tax that should have been withheld (s 71(1)).
- **Late filing, late payment and interest:** the amounts are set under the Revenue Administration Act and are in [Corporate income tax](sc-corporate-income-tax.md).
- **Ships and aircraft:** port clearance (s 60(5)) or airport clearance (s 61(5)) can be refused until the tax is paid.
- **Transfer pricing:** an arm's length adjustment can also raise withholding tax on interest or royalties (s 54(4)(b)(iv), (10)(d)); see [Transfer pricing](sc-transfer-pricing.md).

## Cross-border points

This whole skill is about cross-border points. In short:
- residence follows the s 2 tests (183 days, domicile, normal residence; incorporation or management and control);
- a non-resident with a s 2A permanent establishment pays ordinary business tax on attributable profit;
- without one, Seychelles-source dividends, royalties, natural resource amounts and technical services fees bear a 15% final tax, insurance premiums 5%, financial institutions' managerial fees 33%, and interest the S.I. 107 of 2024 rates, all subject to a treaty in force;
- residents are taxed on Seychelles-source income only, except multinational group members on foreign passive income without economic substance;
- treaties take precedence (s 79), subject in covered treaties to the MLI principal purpose test.

## Two worked examples that recompute

### Example 1: a non-resident consultant, permanent establishment or not (decision)

Atoll Advisory Ltd (resident in a country with no treaty with Seychelles) is hired by a Seychelles hotel company for a 2026 project. Fee SCR 2,000,000; Atoll's own costs on the project SCR 1,200,000. The question is whether its staff stay more than 90 days.

- **No permanent establishment (staff in Seychelles 80 days):** the fee is a technical services fee for services performed in Seychelles (s 5(3)(a)). The hotel withholds 15% of the gross: **SCR 300,000**, a final tax. Costs are not deductible (s 9).
- **Permanent establishment (staff in Seychelles 120 days, s 2A(4)):** s 8 does not apply (s 8(2)(b)). Atoll files a return on the profit of SCR 800,000 at the entity rates of 15% on the first SCR 1,000,000 ([Corporate income tax](sc-corporate-income-tax.md)): **SCR 120,000**.
- **Deciding figure:** with a permanent establishment the tax is SCR 180,000 lower here, but it brings a return, registration and record keeping. Both rates are 15%, one on the gross fee and one on profit, so the gap equals 15% of the deductible costs while profit stays within SCR 1,000,000; above that the 25% band narrows it. Whether there is a permanent establishment follows the facts (the days on site), not a choice.

```oa-check
name: Seychelles non-resident services, 15% final WHT against PE profit at 15% (2026)
inputs:
  fee: 2000000
  costs: 1200000
  wht_rate: 0.15
  band_limit: 1000000
  low_rate: 0.15
  high_rate: 0.25
steps:
  - wht_no_pe: fee * wht_rate
  - pe_profit: fee - costs
  - pe_tax: min(pe_profit, band_limit) * low_rate + max(pe_profit - band_limit, 0) * high_rate
  - saving_with_pe: wht_no_pe - pe_tax
expected:
  wht_no_pe: 300000.00
  pe_profit: 800000.00
  pe_tax: 120000.00
  saving_with_pe: 180000.00
```

### Example 2: a Seychelles bank paying several non-residents (edge case)

In March 2026 a bank operating in Seychelles pays, with no treaty relief:
- its non-resident parent, a managerial fee of SCR 500,000 (33%, S.I. 92 of 2010);
- a non-resident IT firm, a technical fee of SCR 300,000 (15%);
- a non-resident insurer, a premium of SCR 400,000 to insure the bank's premises in Seychelles (a Seychelles risk, 5%);
- a non-resident individual, interest of SCR 50,000 on a fixed deposit (0% for individuals, S.I. 107 of 2024).

- **Tax withheld:** 165,000 + 45,000 + 20,000 + 0 = **SCR 230,000**.
- **Due:** BTA s 69 sets 21 days after the end of March, so 21 April 2026; RAA s 20(1)(b) allows the 23rd for payment through the Tax Portal, which is compulsory here because the payment is SCR 50,000 or more (RAA s 20(2)). Paying by 21 April meets both.
- **Trap:** the 33% applies only to managerial fees paid by a financial institution. The same fee paid by a non-financial company is a technical services fee at 15%.

```oa-check
name: Seychelles bank, WHT on managerial fee, technical fee, premium and fixed deposit interest (2026)
inputs:
  managerial_fee: 500000
  technical_fee: 300000
  premium: 400000
  fd_interest_individual: 50000
steps:
  - wht_managerial: managerial_fee * 0.33
  - wht_technical: technical_fee * 0.15
  - wht_premium: premium * 0.05
  - wht_interest: fd_interest_individual * 0
  - total_wht: wht_managerial + wht_technical + wht_premium + wht_interest
expected:
  wht_managerial: 165000.00
  wht_technical: 45000.00
  wht_premium: 20000.00
  wht_interest: 0.00
  total_wht: 230000.00
```

## Ask the client first

1. For individuals: days in Seychelles in each 12-month period touching 2026, domicile, and any permanent place of abode abroad.
2. For entities: place of incorporation, and where management and control is exercised.
3. What the non-resident does in Seychelles: premises, projects, staff on site, agents concluding contracts, and the number of days.
4. Each payment to a non-resident by type (dividend, interest by account type, royalty, technical or managerial fee, insurance premium, entertainment, carriage), the amount, and whether the payer is a financial institution.
5. The recipient's country, whether a treaty in force is claimed, and the commercial purpose behind the structure.
6. For a resident company with foreign income: whether it belongs to a multinational group, and its people, premises, decisions and spending in Seychelles.

## Sources

| Source | URL | Read on |
|---|---|---|
| Business Tax Act 2009 (Act 28 of 2009), gazette scan, read for the arrangement of sections, s 2 (resident person, resides, royalty, technical services fee, tax year), s 5, ss 6 to 9, ss 57, 59, 60, 61, 63, 66 to 71, 76, 79 and the original First Schedule (items 3, 4 and 9) | https://src.gov.sc/wp-content/uploads/2023/04/Business-Tax-Act-2009-1.pdf | 2026-11-02 |
| Business Tax (Amendment) Act 2020 (Act 2 of 2021), read for ss 2A, 2B, 2C, the new s 5(1), (1A), (1B), (5) and the Eleventh Schedule | https://src.gov.sc/wp-content/uploads/2022/12/Business-Tax-Amendment-Act-2020-Act-2-of-2021.pdf | 2026-11-02 |
| S.I. 78 of 2021, commencement notice, read for the 15 September 2021 date | https://src.gov.sc/wp-content/uploads/2022/12/SI-78-of-2021-Business-Tax-Amendment-Act-2020.pdf | 2026-11-02 |
| S.I. 79 of 2021, Amendment of Eleventh Schedule, read for paras 1, 6 and 7 (multinational group, passive income) | https://src.gov.sc/wp-content/uploads/2022/12/SI-79-of-2021-Business-Tax-Act-2020.pdf | 2026-11-02 |
| S.I. 27 of 2010, replacement First Schedule, read for items 2, 3 and 5 | https://src.gov.sc/wp-content/uploads/2022/12/SI-27-of-2010-Business-Tax-Act-2009-Business-Tax-Amendment-Schedules-Regulations.pdf | 2026-11-02 |
| S.I. 92 of 2010, read for First Schedule item 3(c) and (d) (financial institutions' technical and managerial fees) | https://src.gov.sc/wp-content/uploads/2022/12/SI-92-of-2010-Business-Tax-Act-Business-Tax-Amendment-of-Schedules-No.-4-Regulations-2010.pdf | 2026-11-02 |
| S.I. 66 of 2012, read for reg 2(e) (item 3(a): 15% or the treaty rate) and the Sixth Schedule additions | https://src.gov.sc/wp-content/uploads/2022/12/SI-66-of-2012-Business-Tax-Amendment-of-Schedules-Regulations-2012.pdf | 2026-11-02 |
| S.I. 6 of 2010, S.I. 7 of 2011 and S.I. 47 of 2018, read in full for any First Schedule rate under s 66(2) (none found) | https://src.gov.sc/wp-content/uploads/2022/12/SI-6-of-2010-Business-Tax-Act-2009-ACT-Business-Tax-Amendment-of-Schedules-Regulations.pdf ; https://src.gov.sc/wp-content/uploads/2022/12/SI-7-of-2011-Business-Tax-Act-Business-Tax-Amendment-of-First-Schedule-Regulations-2011.pdf ; https://src.gov.sc/wp-content/uploads/2022/12/SI-47-of-2018-Business-Tax-Amendment-of-First-Schedule-No.-2-Regulations-2018.pdf | 2026-11-02 |
| S.I. 107 of 2024, read in full (item 3(e) non-resident interest table, item 3(f)) | https://src.gov.sc/wp-content/uploads/2025/02/SI-107-2024-Business-Tax-Amendment-of-First-Schedule-Regulations-2024.pdf | 2026-11-02 |
| Business Tax (Amendment) Act 2012 (Act 14 of 2012), read for the technical services fee definition, s 8(2), s 14(3) and s 65 repeal | https://src.gov.sc/wp-content/uploads/2022/12/Business-Tax-Amendment-Act-2012-Act-14-of-2012.pdf | 2026-11-02 |
| Business Tax (Amendment) Act 2010 (Act 25 of 2010), read for the s 61(1) change to 21 days | https://src.gov.sc/wp-content/uploads/2022/12/Business-Tax-Amendment-Act-2010.pdf | 2026-11-02 |
| Business Tax (Amendment) Act 2022 (Act 31 of 2022), read for s 2 definitions and s 54(1), (4), (6), (7), (10), (31) | https://src.gov.sc/wp-content/uploads/2023/01/Act-31-2022-Business-Tax-Amendment-Act-2022.pdf | 2026-11-02 |
| Revenue Law (Amendment) Act 2023 (Act 27 of 2023), read in full (RAA ss 2, 3, 20; BTA s 73) | https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf | 2026-11-02 |
| Income and Non-Monetary Benefits Tax Act 2010, read for s 3 (source of emoluments) | https://src.gov.sc/wp-content/uploads/2022/12/Income-and-Non-Monetary-Benefits-Tax-Act-2010.pdf | 2026-11-02 |
| SRC, Seychelles Tax System page, read for the territorial basis, the withholding tax table and remittance | https://src.gov.sc/seychelles-tax-system/ | 2026-11-02 |
| SRC, Agreements page, read for the list of DTAAs and TIEAs in force | https://src.gov.sc/agreements/ | 2026-11-02 |
| SRC, synthesised text of the Seychelles and South Africa agreement as modified by the MLI, read for the ratification and entry into force dates and Article 7(1) | https://src.gov.sc/wp-content/uploads/2025/04/Legal-IntA-DTA-MLI-2025-08-Seychelles-SA-synthesised-text-MLI.pdf | 2026-11-02 |
| SRC, legislation page, read for the list of Business Tax amending instruments | https://src.gov.sc/legislation/ | 2026-11-02 |

Not yet confirmed:
- A consolidated text of the Business Tax Act; this skill reads the 2009 Act with the amending instruments listed above, and an amendment not on the SRC legislation page could change a figure.
- The rate of withholding on non-resident entertainers and sports persons under s 66(2). The SRC Tax System page gives 5%, but s 66(2) points to the First Schedule and no item sets it: the original 2009 Schedule (item 9 covers only s 8 amounts), the S.I. 27 of 2010 replacement (items 1 to 6) and the amending S.I.s on the SRC legislation page that were read (6 of 2010, 92 of 2010, 7 of 2011, 66 of 2012, 47 of 2018, 108 of 2021, 107 of 2024) have none. Whether the non-resident then files a return to claim the s 76(2) credit was not confirmed.
- The content of the Ninth Schedule limit on deducting royalties and technical services fees paid to non-residents (s 14(3)(a)).
- The general anti-avoidance rule in s 55.
- Which of the 29 treaties are covered tax agreements under the MLI, and the rates and permanent establishment articles of each treaty.
- Whether a multinational group member taxed on foreign passive income under s 5(1A) gets any credit for foreign tax outside a treaty.
- The qualifying income formula in s 5(1B), which did not reproduce in the gazette text.
- Whether s 5(4), referred to by Act 2 of 2021, was inserted by an amending Act not read.
