---
name: ie-corporation-tax
description: "Use this skill whenever asked about Irish Corporation Tax for a resident Irish company or branch of a non-resident company carrying on a trade in Ireland. Trigger on phrases like \"Ireland CT\", \"Ireland corporation tax\", \"12.5% Ireland\", \"Irish trading rate\", \"Pillar Two Ireland\", \"Irish CT1 return\", \"Revenue Online Service CT\", \"ROS CT1\", \"Section 21 TCA\", \"Section 21A passive income\", \"Knowledge Development Box\", \"KDB\", \"R&D tax credit Ireland\", \"Section 766\", \"Section 110 SPV\", \"group relief Ireland\", \"preliminary CT\", \"iXBRL accounts\", \"QDMTT Ireland\", \"IIR Ireland\", or \"UTPR Ireland\". Covers the 12.5% trading rate (Section 21 TCA 1997), the 25% non-trading rate (Section 21A) on passive income, the Pillar Two 15% effective minimum tax for in-scope MNEs implemented via Finance (No. 2) Act 2023 (IIR, QDMTT, UTPR), the R&D tax credit at 30% under Section 766 TCA (as raised by FA 2024) refundable in three instalments, the Knowledge Development Box at 6.25% effective rate, Section 110 securitisation SPV rules, group relief at the 75% threshold, trading loss relief (one-year carry-back, indefinite carry-forward), preliminary tax (90% current year or 100% prior year), and final CT1 filing within 9 months of year-end (by the 23rd of that month for ROS users) with iXBRL-tagged financial statements via Revenue Online Service. Out of scope: personal income tax (use ie-income-tax-form11), USC (use ie-usc), PRSI Class S (use ie-prsi-class-s), VAT (use ireland-vat-return), preliminary income tax (use ie-preliminary-tax), partnerships and unincorporated businesses, foreign branch trading profits taxed under Section 25 attribution rules, banking and insurance sector specific regimes, life assurance Case I/IV computations, REIT (Section 705A) and IREF (Section 739K) specific returns, petroleum and mineral extraction profits, and Irish Collective Asset-management Vehicles (ICAVs). ALWAYS read this skill before touching any Irish Corporation Tax work."
jurisdiction: IE
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Irish Corporation Tax (CT1): 2026 rates, preliminary tax, losses, reliefs and filing

## Scope

This Guide covers Corporation Tax (CT) for an Irish-resident company, or an Irish branch of a non-resident company, that files a Form CT1. Figures are for tax year 2026, meaning accounting periods in 2026: for a calendar-year company, the 12 months to 31 December 2026. A dated section near the end covers the 2025 CT1, which most calendar-year companies had to file by 23 September 2026.

It covers the 12.5% and 25% rates, chargeable gains in CT, the Pillar Two minimum tax (scope only), close-company surcharges, preliminary tax, CT1 filing on ROS, losses and group relief, start-up relief, the R&D corporation tax credit, the Knowledge Development Box, capital allowances, interest limitation, and late filing surcharges and interest.

It does not cover: personal income tax, USC or PRSI; VAT; partnerships and sole traders; Section 110 securitisation companies; banks and insurers; REITs and IREFs; petroleum and mineral profits; tonnage tax; ICAVs and funds; the Pillar Two top-up computation itself; transfer pricing documentation; anti-hybrid rules; the outbound payments measures; or foreign currency (functional currency) computations. Those are in "When to refuse or refer".

The law is the Taxes Consolidation Act 1997 (the TCA), as amended each year by a Finance Act. Revenue's guidance is on [revenue.ie](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/index.aspx) and in its Tax and Duty Manuals (TDMs). Acts are on [irishstatutebook.ie](https://www.irishstatutebook.ie/eli/1997/act/39/enacted/en/html).

## Ask the client first

- What is the accounting period (start and end date)? It cannot be longer than 12 months, so a longer set of accounts must be split into two CT periods.
- Is the company Irish resident, or is it a non-resident company trading in Ireland through a branch?
- What does the company do? Is the income trading income, or rent, interest, dividends or other passive income? Does it carry on an "excepted trade" (for example dealing in or developing land, or working minerals or petroleum)?
- What was the CT liability for the previous accounting period? Was the previous period shorter than 12 months?
- Is this the company's first accounting period? When did it start to trade? Did it take over a trade from anyone else?
- Who owns the company? Is it controlled by five or fewer people, or by its directors (a close company)? Does it provide professional services (a service company)? What dividends were paid, and when?
- Is it in a group? Which companies own three quarters or more of it, and which companies does it own three quarters or more of? Is the wider group's consolidated revenue €750m or more?
- Any losses brought forward, losses this year, or losses from group companies to claim?
- Any R&D spending, patents or software income? Has the company claimed the R&D credit in any of its previous three accounting periods?
- Any assets bought or sold: plant, buildings, vehicles, intangibles, shares, land?
- Any interest expense? How much net interest (exceeding borrowing costs) in the year?
- Are the accounts audited, and does the company meet all three iXBRL exemption tests?
- Is any CT1 or payment outstanding or late?

## The method, step by step

1. **Fix the period and the company's status.** Confirm the accounting period (12 months at most), residence, and whether the company is a close company, a service company, a group member or in Pillar Two scope.
2. **Start from the accounts profit.** Add back depreciation, business entertainment, capital expenditure and other non-deductible items. Deduct capital allowances instead of depreciation.
3. **Split the profits.** Trading income is taxed at 12.5%. Rental, investment and other non-trading income, and income of an excepted trade, are taxed at 25%. Chargeable gains (other than development land) are included in CT by grossing up the gain (see below).
4. **Apply losses and group relief** in the order the law allows: current-period and prior-period set-off, value basis, carry forward, group surrenders.
5. **Apply credits and reliefs:** start-up relief (s.486C), double tax relief, and the Knowledge Development Box deduction if claimed. Compute the R&D credit separately: it is paid in instalments, not deducted from the tax charge.
6. **Add close-company surcharges** that fall due with this period's CT (they relate to the previous period's undistributed income).
7. **Check preliminary tax.** Work out whether the company is small or large, what was due, and whether it was paid on time. The balance is due with the CT1.
8. **File the CT1 with iXBRL financial statements (if required) on ROS** and pay the balance by the return date.
9. **Check for exposure:** late filing surcharge, restriction of reliefs, and daily interest on late tax.

## Rates and key figures for 2026 accounting periods ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx))

| Item | 2026 figure | Notes |
| --- | --- | --- |
| Trading income | 12.5% | Case I and II trading profits (s.21 TCA) |
| Non-trading income and excepted trades | 25% | Rent, interest, foreign dividends taxed under Case III, other passive income; excepted trades such as land dealing (s.21A TCA) |
| Chargeable gains (not development land) | CGT rate of 33%, collected through CT | Gain grossed up so that CT at 12.5% equals CGT at 33% |
| Pillar Two minimum rate | 15% | Groups with consolidated revenue of €750m or more in two of the four preceding fiscal years |
| Small company (preliminary tax) | CT of the previous period not above €200,000 | Above €200,000 = large company |
| Close-company surcharge on estate and investment income | 20% | After a 7.5% reduction for trading companies; exempt if the excess is €2,000 or less |
| Service-company surcharge | 15% on half of undistributed trading income, plus 20% on estate and investment income | s.441 TCA |
| R&D corporation tax credit | 35% for periods ending 31 December 2026 or later; 30% for periods commencing on or after 1 January 2024 that end earlier | See the R&D section |
| Knowledge Development Box | Deduction of 20% of qualifying profits, an effective rate of 10% | From 1 October 2023; periods commencing before 1 January 2027 |
| Plant and machinery | 12.5% a year over eight years | Wear and tear |
| Late payment interest | 0.0219% per day | Cannot be appealed or reduced |
| Late filing surcharge | 5% (maximum €12,695) or 10% (maximum €63,485) | Two-month dividing line |

**The accounting period.** CT is charged on the profits of an accounting period, which cannot be longer than 12 months. If the rate changes during a period, profits are apportioned on a time basis. No rate change has been made for 2026: the 12.5% and 25% rates apply to the whole of 2026 and 2025.

**Trading or not.** The 12.5% rate needs a real trade. Holding investments, letting property and earning deposit interest are not trading, even inside a trading company; that income is taxed at 25%. When the split is unclear, do not default to 12.5%: gather the facts and refer borderline cases (see Revenue's TDM Part 02-02-06 on classifying activities as trading).

## Chargeable gains inside CT ([Revenue: capital gains for companies](https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx))

A company's gains on assets other than development land are taxed at the CGT rate of 33%, but the tax is collected through CT at 12.5%. So the gain is adjusted: work out the CGT at 33%, then divide that tax by 12.5%. Report the adjusted gain in the capital gains section of the CT1.

Revenue's example: a gain of €150,000 gives CGT of €49,500 (33%), and an adjusted gain of €396,000 (€49,500 divided by 12.5%). CT at 12.5% on €396,000 is €49,500.

Gains on development land stay outside CT profits. They are taxed under CGT rules, reported in the Capital Gains (Development Land) section of the CT1, and follow the CGT pay and file dates. Development land losses can be set against all gains; other losses only against gains on non-development land assets.

Disposals of shares in trading subsidiaries may be exempt under s.626B (the substantial shareholding exemption). The conditions are technical; check them against TDM Part 20-01-14 before relying on the exemption.

## Pillar Two: the 15% minimum tax ([Revenue: what is Pillar Two](https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/index.aspx))

Pillar Two (Part 4A of the Taxes Consolidation Act 1997) makes multinational and large domestic groups pay at least 15% on their profits in each jurisdiction. A group is in scope if its consolidated annual revenue is €750m or more in two of the four preceding fiscal years. The test is "or more": a group at exactly €750m is in scope.

Ireland has three top-up taxes:

- **Domestic top-up tax (Ireland's qualified domestic top-up tax, QDTT).** Collects top-up tax on Irish entities before any other country can apply its IIR or UTPR. In effect for fiscal years commencing on or after 31 December 2023 ([domestic top-up tax](https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/domestic-top-up-tax.aspx)).
- **IIR top-up tax.** Charged on a parent entity for low-taxed group entities. In effect for fiscal years commencing on or after 31 December 2023 ([IIR](https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/iir-top-up-tax.aspx)).
- **UTPR top-up tax.** The backstop where the ultimate parent is in a country that has not implemented Pillar Two. In effect for fiscal years commencing on or after 31 December 2024, with limited cases earlier ([UTPR](https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/uptr-top-up-tax.aspx)).

**Compliance** ([Revenue: key dates](https://www.revenue.ie/en/companies-and-charities/pillar-two/dates/index.aspx); [TIR](https://www.revenue.ie/en/companies-and-charities/pillar-two/top-up/index.aspx)):

- Registration on ROS within 12 months after the end of the first fiscal year in scope. Entities whose first fiscal year ended in 2024 had until 28 February 2026 (after an extension).
- Every in-scope entity must file a Top-up Tax Information Return (TIR) no later than 15 months after the end of each fiscal year, or 18 months for the first fiscal year in scope. The first TIR and the first pay and file date were 30 June 2026.
- Revenue has announced relief from local filing for some centrally filed returns, and the OECD's January 2026 "Side-by-Side" package changes some rules. Check Revenue's key dates page before advising.

This Guide only screens for scope. The top-up computation needs the full GloBE rules, deferred tax adjustments and safe-harbour tests: refer it.

## Close companies and the surcharges ([Revenue: surcharge on undistributed income](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx))

A close company is an Irish-resident company controlled by five or fewer participators, or by any number of participators who are directors ([Revenue: close companies](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/close-companies.aspx)). Most owner-managed companies are close companies.

**Estate and investment income (s.440).** A surcharge of 20% applies to the undistributed after-tax estate and investment income (rent, interest, dividends). The steps:

1. Take the estate and investment income and deduct the CT on it.
2. If the company is a trading company, deduct a further 7.5%. The result is the distributable estate and investment income.
3. Deduct distributions made for the period within 18 months after the end of the period.
4. If the excess is €2,000 or less, there is no surcharge. Otherwise the surcharge is 20% of the excess.

The surcharge is not part of the same period's CT. It is collected as part of the CT of the next accounting period and must be reported on that CT1. Two close companies can jointly elect to disregard a distribution between them; both must include the election on their CT1.

Irish dividends received by a close company are exempt from CT but still count. Revenue's example: €50,000 of Irish dividends, nothing paid out, gives a surcharge of €10,000.

**Service companies (s.441).** A close company whose main income comes from a profession, professional services or holding an office or employment (for example a doctor, dentist, architect, solicitor, accountant, actuary, actor, computer programmer or engineer) pays a surcharge of 15% on half of its undistributed trading income, and 20% on undistributed estate and investment income ([TDM Part 13-02-06](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-13/13-02-06.pdf)). Service-company rules have their own marginal relief: refer any case near the limits.

**Returns without the surcharge are incomplete.** A CT1 that leaves out a surcharge due under s.440 or s.441 is treated as an incorrect return, and can bring interest and a late filing surcharge ([TDM Part 47-06-04](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-04.pdf)).

## Deductions and capital allowances ([Revenue: capital allowances and deductions](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/capital-allowances-and-deductions.aspx))

**Deductions.** Expenses are deductible only if they are revenue (not capital) in nature and incurred wholly and exclusively for the trade. Business entertainment and capital expenditure are not deductible. Depreciation in the accounts is added back; capital allowances are claimed instead. Other points:

- Pre-trading expenses incurred in the three years before trading starts can be deducted.
- Interest, royalties and other annual payments can be deducted, subject to the interest limitation rule below.
- A donation to a Revenue-approved charity can reduce CT if it is at least €250 in a 12-month period (apportioned for a shorter period).
- CT itself, fines and penalties, and interest on late tax are not deductible.

**Capital allowances** are generally given on the net cost of the asset, as a trading expense:

| Asset | Allowance |
| --- | --- |
| Plant and machinery (wear and tear) | 12.5% a year over eight years, if the asset is in use in the trade at the end of the period |
| Most industrial buildings | 4% a year over 25 years |
| Energy-efficient equipment (including electric and alternative fuel vehicles), gas vehicles and refuelling equipment, and a creche or gym for employees | Accelerated capital allowance of 100% in the first year the asset is used |
| Building used as an employee creche or gym | 15% a year over seven years |
| Specified intangible assets (s.291A): patents, copyrights, trademarks, know-how | Amortisation and impairment charged in the accounts, or an election for 7% a year over 15 years with 2% in the final year ([Revenue: intangibles](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/capital-allowances-for-intangible-assets/index.aspx)) |

The wear and tear allowance is reduced if the accounting period is shorter than 12 months or the asset is also used for non-trade purposes. Revenue's example: a machine costing €25,000 gives an allowance of €3,125 a year.

Intangible asset allowances are ring-fenced to the "relevant trade" that uses the assets. For expenditure on or after 11 October 2017, the allowances (with related interest) cannot exceed 80% of that trade's income for the period; the excess carries forward. Finance Act 2025 extends the ring-fence and the 80% cap to balancing allowances on balancing events on or after 8 October 2025.

Cars are restricted by reference to CO2 emissions and cost: the cost limit is currently €24,000, and it also applies to lease payments ([TDM Part 11-00-01](https://www.revenue.ie/en/tax-professionals/tdm-wm/income-tax-capital-gains-tax-corporation-tax/part-11/11-00-01.pdf)). Check the emissions category before claiming.

## Losses ([Revenue: trading losses](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/trading-losses.aspx); [Notes for guidance, Part 12](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part12.pdf))

**Trading losses from a 12.5% trade (ss.396A and 396B):**

1. **Same period and the period before (s.396A).** Set the loss against other 12.5% trading income of the same accounting period, then against trading income of the immediately preceding accounting period. It is a euro-for-euro offset. It cannot be set against rent, interest or gains this way.
2. **Value basis (s.396B).** Any unused loss can reduce the CT on non-trading income and chargeable gains of the same or preceding period, but only at 12.5% of the loss. A loss of €100,000 therefore saves €12,500 of tax, however that other income is taxed.
3. **Carry forward (s.396(1)).** Unused losses carry forward without time limit against trading income of the same trade. They must be used against the first available profits of that trade.

**Losses of an excepted (25%) trade** can be set against total profits of the same period and of the immediately preceding accounting period (s.396(2)), then carried forward against the same trade.

**The preceding period rule.** Relief against the previous period only applies if the company carried on the trade in that period. It is limited to profits of the preceding period of the same length as the loss period, with apportionment where periods differ.

**Terminal loss (s.397).** A loss in the last 12 months of a trade that cannot be relieved otherwise can be carried back against income of the same trade in the three preceding years, later years first.

**Change of ownership.** Losses carried forward can be lost where there is a change in ownership combined with a major change in the activities of the trade, or where the trade is near dormant at the time of the change (s.401, aimed at "loss-buying"). Refer any such case.

**Late filing cuts loss relief.** If the CT1 is late, loss claims under ss.396(2), 396A(3) and 396B(2) are restricted (see "Filing and payment").

## Group relief ([Revenue: group relief](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/group-relief/index.aspx))

Two companies are in a group for group relief if one is a 75% subsidiary of the other, or both are 75% subsidiaries of a third company. The parent must hold at least 75% of the ordinary share capital, and be entitled to at least 75% of distributable profits and of assets on a winding up.

- **What can be surrendered:** current-year trading losses, excess charges on income, excess management expenses of investment companies, Case V excess capital allowances.
- **How it is used:** against the claimant's trading income of the corresponding period, on a value basis against its CT, or against total profits for an excepted trade.
- **Who:** generally Irish-resident companies and Irish branches of foreign companies. An Irish parent can claim, in limited cases, the losses of a 75% subsidiary resident in an EU or EEA state that has a tax treaty with Ireland.
- **Time limit and consent:** the claim must be made within two years from the end of the surrendering company's accounting period, and the surrendering company must consent in writing.
- **Consortium relief (s.412):** a separate relief for companies owned by a consortium. Refer it.
- **Restrictions:** relief is time-apportioned where accounting periods do not match or a company joins or leaves the group. It is also restricted if either company's return is filed late.

## Interest limitation ([TDM Part 35D-01-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35d/35D-01-01.pdf))

The interest limitation rule (ILR, Part 35D TCA) applies to accounting periods commencing on or after 1 January 2022. It limits a company's exceeding borrowing costs (net interest expense) to 30% of its tax-adjusted EBITDA. A higher group ratio can be elected.

- **De minimis.** The ILR applies only where the exceeding borrowing costs exceed €3,000,000 for a 12-month period. The amount is reduced proportionally for a shorter period. For an interest group, the €3,000,000 applies once to the whole group.
- **Standalone entities** are outside the ILR. A standalone entity is not part of a worldwide group, has no associated enterprises and has no permanent establishment outside Ireland. A company wholly owned by one individual is **not** a standalone entity: the individual is an associated enterprise.
- **Equity ratio exemption and legacy debt** (loans agreed before 17 June 2016) can also apply. Refer these.
- **Carry forward.** A disallowed amount is carried forward as "deemed borrowing cost" to later periods with spare capacity.

For most owner-managed companies, the practical test is the de minimis: confirm that net interest does not exceed €3,000,000.

## Start-up relief (s.486C) ([Revenue: can you claim](https://www.revenue.ie/en/starting-a-business/initiatives-startup-businesses-smes/tax-relief-for-new-startup-companies/can-you-claim-for-tax-relief-for-your-start-up-company.aspx); [how the relief is calculated](https://www.revenue.ie/en/starting-a-business/initiatives-startup-businesses-smes/tax-relief-for-new-startup-companies/how-is-the-relief-calculated.aspx))

**Who qualifies.** A company qualifies if it was incorporated on or after 14 October 2008, and it set up and began a qualifying trade between 1 January 2009 and 31 December 2026. A company that begins trading in 2027 does not qualify unless the end date is extended. Check before advising.

**Excluded trades:** a trade taken over from another person, land development, petroleum or mineral extraction, s.441 service company activities, certain primary agricultural and fishery production, and activities that would form part of an associated company's trade.

**How long.** Where the trade started on or after 1 January 2018, relief applies for five years from the date it started ([TDM Part 15-03-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-15/15-03-03.pdf)).

**How much.** Two separate limits apply:

1. **The CT band.** The company's total CT for the period, on all income and gains, decides whether relief is available:
   - €40,000 or less: full relief, up to the PRSI limit below.
   - More than €40,000 and less than €60,000: marginal relief.
   - €60,000 or more in a 12-month period: no relief.
2. **The PRSI limit.** Relief can never exceed the qualifying PRSI:
   - employer's PRSI paid, capped at €5,000 per employee;
   - from 2025, Class S PRSI paid by certain directors through PAYE on emoluments from the company, capped at €1,000 per individual;
   - an overall limit of €40,000 for all of it.

Only the CT on profits of the qualifying trade, and on gains on assets used in it, is reduced. CT on rent or investment income is not.

**Marginal relief.** The CT on the qualifying trade is reduced to the greater of two amounts:
- the marginal relief formula: 3 x (T - M) x ((A + B) / T);
- the CT on the qualifying trade less the qualifying PRSI.

In the formula, T is the total CT, M is €40,000, A is the CT on income of the qualifying trade, and B is the CT on gains of the qualifying trade.

**Unused relief.** Relief not used in the first five years, for example because of losses, can be carried forward. In a later year it is limited to the PRSI paid in that year.

**How to claim.** Claim the relief on the CT1 through ROS.

## The R&D corporation tax credit ([Revenue: R&D credit](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/research-and-development-rd-tax-credit/index.aspx); [TDM Part 29-02-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf))

**The rate depends on the period:**

| Accounting period | Credit rate | First instalment is the greater of |
| --- | --- | --- |
| Commencing on or after 1 January 2024 and ending before 31 December 2026 (for example calendar 2025) | 30% | €75,000 (or the whole credit if lower) and 50% of the credit, for periods commencing on or after 1 January 2025 |
| Specified return date on or after 23 September 2027 (in general, periods ending 31 December 2026 or later) | 35% | €87,500 (or the whole credit if lower) and 50% of the credit |

**Instalments.** The credit is paid in three annual instalments:
1. The first instalment is the amount shown in the table.
2. The second is three fifths of the balance.
3. The third is whatever remains.

The credit is not set against the CT for the period. For each instalment, the company elects either to treat it as an overpayment of tax, for offset against its liabilities, or to have it repaid. The first instalment is specified on the CT1 for the period in which the expenditure was incurred. The second is specified on the CT1 for the following period.

**Qualifying activity.** The R&D must be carried out in Ireland, the EEA or the UK, by a company within the charge to Irish CT, on spending not deductible abroad. It must be systematic, investigative or experimental work in science or technology that seeks an advance by resolving scientific or technological uncertainty ([qualifying criteria](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/research-and-development-rd-tax-credit/qualifying-criteria.aspx)). Outsourcing limits apply to subcontractors and agency staff.

**Deadlines:**
- **The claim:** within 12 months from the end of the accounting period in which the expenditure was incurred. For a calendar 2026 period, that means by 31 December 2027.
- **Pre-filing notification:** a company claiming for the first time, or one that has not claimed in any of its previous three accounting periods, must notify Revenue at least 90 days before making the claim.

## Knowledge Development Box ([Revenue: KDB](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/knowledge-development-box-kdb/index.aspx))

From 1 October 2023, a qualifying company can deduct 20% of its qualifying profits. That gives an effective rate of 10%. Up to 30 September 2023 the deduction was 50%, an effective rate of 6.25%; do not use 6.25% for 2026. The KDB is available for accounting periods commencing before 1 January 2027.

The profits must come from a qualifying asset created by qualifying R&D:
- a computer programme;
- an invention protected by a qualifying patent;
- for small companies, IP that the Controller of Patents certifies as patentable but that is not patented.

The claim is made on the CT1. The qualifying profit is restricted by the OECD nexus fraction and needs tracking and tracing of R&D spend (TDM Part 29-03-01). Refer any KDB claim.

## Foreign dividends: participation exemption ([Revenue: participation exemption](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/exemption-foreign-distributions/index.aspx))

For distributions on or after 1 January 2025, an Irish parent can claim exemption from CT on dividends from a foreign subsidiary, instead of a credit for foreign tax. The conditions are:

- **Holding:** the parent holds at least 5% of the subsidiary's ordinary share capital for a continuous 12 months that include the date of the distribution.
- **The subsidiary:** for distributions from 1 January 2026, it must have been resident throughout the preceding three years in an EU or EEA state or a treaty country (for 2025 distributions, the look-back was five years). It must not be on the EU list of non-cooperative jurisdictions, and must not be generally exempt from tax.
- **Non-treaty countries:** from 2026 these also qualify if they apply withholding tax to the distribution, paid in full and not refunded.
- **The distribution:** it must be taxable as income under Case III, not as trading income, and must not be deductible abroad.

The election is all or nothing. If it is claimed, every relevant distribution from every relevant subsidiary is exempt for that period; it cannot be made dividend by dividend. The claim is made on the CT1 (see TDM Part 35-02-11).

## Boundary and exception table ([Revenue: preliminary CT](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/preliminary-ct.aspx))

| Situation | Rule | Source |
| --- | --- | --- |
| Previous period's CT exactly €200,000 | Small company: the test is "not above €200,000", excluding surcharges and s.239 income tax | [Preliminary CT](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/preliminary-ct.aspx) |
| Previous period shorter than 12 months | Annualise its CT to test small or large, and when using the 100% prior-year basis | Same |
| First accounting period of a new company | No preliminary tax if the CT is less than €200,000 (excluding surcharge, including s.239 income tax); pay in full with the CT1. If the CT is €200,000 or more, preliminary tax is due | Same |
| Large company, accounting period of less than seven months | One instalment of 90%, not two (two instalments are for periods longer than seven months; for a period of exactly seven months, check TDM Part 41A-07-02) | [When is preliminary CT due](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/when-is-preliminary-ct-due.aspx) |
| Group consolidated revenue of exactly €750m in two of the four preceding years | In Pillar Two scope ("€750m or more") | [What is Pillar Two](https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/index.aspx) |
| Close company: excess distributable income of exactly €2,000 | No s.440 surcharge ("€2,000 or less") | [Surcharge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx) |
| Start-up with total CT of exactly €40,000 | Full relief band ("does not exceed €40,000") | [TDM Part 15-03-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-15/15-03-03.pdf) |
| Start-up with total CT of exactly €60,000 | No relief ("€60,000 or more") | Same |
| Exceeding borrowing costs of exactly €3,000,000 | Does not exceed the de minimis, so the ILR does not apply (it applies only where they exceed €3,000,000) | [TDM Part 35D-01-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35d/35D-01-01.pdf) |
| Accounting period ends on the 21st of a month or later | CT1 due on the 21st of the ninth month after the period ends; 23rd if filed and paid on ROS | [TDM Part 47-06-08](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf) |
| Accounting period ends before the 21st of a month (for example 5 December) | CT1 due on the same day of the ninth month (for example 5 September); the ROS extension to the 23rd only replaces a 21st due date | Same |
| CT1 filed exactly two months late | Within two months: 5% surcharge (maximum €12,695) | Same |
| iXBRL: company fails one of the three small tests | iXBRL required; the exclusion needs all three (assets under €4.4 million, turnover under €8.8 million, 50 or fewer employees) | [Who must submit iXBRL](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/who-submit.aspx) |
| R&D expenditure in a period ending 30 November 2026 | Its return date falls in August 2027, before 23 September 2027, so the 30% rate applies (Revenue: the 35% rate applies "in general" to periods ending 31 December 2026 or later) | [TDM Part 29-02-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf) |
| Owner-managed company with interest expense | Not a standalone entity if owned by an individual; rely on the €3,000,000 de minimis | [TDM Part 35D-01-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35d/35D-01-01.pdf) |

## Worked cases ([Revenue: when is preliminary CT due](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/when-is-preliminary-ct-due.aspx))

**Case 1: small trading company with rent, calendar 2026.** Hill Ltd is a close trading company. In 2026 it has a trading profit of €400,000 and a net rental profit of €40,000. Its CT for 2025 was €48,000.

- CT for 2026: €400,000 at 12.5% = €50,000, plus €40,000 at 25% = €10,000. Total €60,000.
- Hill Ltd is a small company because its 2025 CT of €48,000 is not above €200,000. By 23 November 2026 it must pay at least the lower of 100% of the 2025 CT (€48,000) and 90% of the 2026 CT (€54,000). It can pay €48,000 and still be on time.
- The balance of €12,000 is due with the CT1 by 23 September 2027 (ROS).
- Surcharge on the 2026 rent: €40,000 less CT of €10,000 = €30,000. Less the 7.5% trading company reduction (€2,250) = €27,750. It pays dividends of €20,000 within 18 months of 31 December 2026, leaving an excess of €7,750. That is more than €2,000, so the surcharge is 20% x €7,750 = €1,550. It is collected with the CT for 2027, not 2026.

**Case 2: large company preliminary tax, calendar 2026.** Coast Ltd's CT for 2025 was €900,000. It expects €1,200,000 for 2026.

- First instalment by 23 June 2026: either 50% of the 2025 CT (€450,000) or 45% of the 2026 CT (€540,000). Paying €450,000 meets the rule.
- Second instalment by 23 November 2026: the total must reach 90% of the 2026 CT, which is €1,080,000. The second payment is therefore €630,000.
- The balance of €120,000 is due by 23 September 2027 with the CT1.
- If the 2026 CT turns out higher than expected, the 90% test is measured against the final figure. An underpayment carries interest at 0.0219% a day.

**Case 3: trading loss against a gain, value basis.** This is Revenue's example on its [trading losses page](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/trading-losses.aspx). A company has a trading loss of €100,000 and a chargeable gain of €100,000. The tax on the gain is €33,000. The loss is worth €100,000 x 12.5% = €12,500 on a value basis, so the tax due is €20,500. Value-basis relief is not a choice: it applies only to losses left unused after the euro-for-euro offset against trading income of the same and preceding periods.

**Case 4: R&D credit, calendar 2026 compared with calendar 2025.** Lab Ltd spends €400,000 of qualifying R&D expenditure in each year.

- **2026 (35%):** credit €140,000. The first instalment is the greater of €87,500 and 50% of the credit (€70,000), so €87,500. The balance is €52,500. The second instalment is three fifths of that, €31,500, and the third is €21,000. The claim must be made by 31 December 2027.
- **2025 (30%):** credit €120,000. The first instalment is the greater of €75,000 and €60,000, so €75,000. The balance is €45,000. The second instalment is €27,000 and the third is €18,000.

**Case 5: start-up relief limited by PRSI (2025).** This is Revenue's example on its [start-up relief page](https://www.revenue.ie/en/starting-a-business/initiatives-startup-businesses-smes/tax-relief-for-new-startup-companies/how-is-the-relief-calculated.aspx). A company's CT for the year to 31 December 2025 is €25,000, which is below €40,000, so it is in the full relief band.

- Qualifying PRSI: employer's PRSI of €9,000, plus Class S PRSI of €1,500 (one director's €1,200 is capped at €1,000). Total €10,500.
- Relief is €10,500, not €25,000.
- The CT payable on the qualifying trade is €14,500.

**Case 6: late 2025 CT1.** Brook Ltd has a 31 December 2025 year end and CT for 2025 of €150,000. The CT1 was due by 23 September 2026 on ROS.

- If it files on 20 October 2026 (within two months): surcharge of 5% x €150,000 = €7,500, below the €12,695 cap. Any loss relief or group relief claim is cut by 25%, up to €31,740.
- If it files on 15 December 2026 (more than two months late): surcharge of 10% = €15,000, below the €63,485 cap. The relief restriction is 50%, up to €158,715.
- Unpaid tax also carries interest at 0.0219% a day. The surcharge itself counts as tax for interest.

**Case 7: Pillar Two scope for fiscal year 2026.** A group's consolidated revenue was €700m in 2022, €760m in 2023, €720m in 2024 and €800m in 2025. Revenue reached €750m or more in two of the four preceding fiscal years (2023 and 2025), so the group is in scope for 2026. Refer the computation.

## When to refuse or refer

Refer to a Chartered Tax Adviser or other qualified Irish tax practitioner, and do not produce a final figure, when:

- **Residence is uncertain,** or a non-resident company may be trading in Ireland without a branch. The residence and permanent establishment tests come first.
- **Special regimes apply:** Section 110 securitisation companies, banks and insurers, REITs and IREFs, funds and ICAVs, tonnage tax, petroleum or mineral profits, or development land gains beyond reporting.
- **The group is in Pillar Two scope.** The QDTT, IIR, UTPR and TIR computations need the GloBE rules, specialist software and current OECD guidance, including the January 2026 Side-by-Side package.
- **Cross-border related-party flows need screening:** transfer pricing documentation, anti-hybrid rules, the outbound payments measures, or the equity ratio or legacy debt points under the interest limitation rule.
- **The claim is technical:** KDB (nexus and tracking), R&D claims with subcontracting, grants or borderline science, intangible asset elections, or foreign currency (s.402) computations.
- **Structuring advice is sought:** loss-buying (s.401), moving IP or residence, or any arrangement that may fall within the general anti-avoidance rule (s.811C) or the mandatory disclosure regime.
- **Revenue is involved:** an audit, a compliance intervention, a qualifying disclosure, or penalties for a careless or deliberate return.
- **Close-company items go beyond the surcharge:** loans to participators, benefits for participators, or service-company marginal relief.
- **Records are missing:** there are no signed accounts, no prior-period CT figure, or no evidence of preliminary tax payments.
- **The trading or non-trading split is doubtful:** do not apply 12.5% until the facts support a trade.

## Filing and payment ([Revenue: payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx))

**Mandatory e-filing.** A company must file its return and pay its tax on the Revenue Online Service (ROS). Each period it must:
1. pay preliminary tax by the due date;
2. file a CT1 and a Form 46G (Company) by the return filing date;
3. pay any balance of tax by the return filing date.

**The return date.** The CT1 is due nine months after the end of the accounting period ([TDM Part 47-06-08](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf)):
- Period ending on or after the 21st of a month: due by the 21st of the ninth month. Filed and paid through ROS, it is due by the 23rd. For a 31 December 2026 year end that means 23 September 2027.
- Period ending before the 21st of a month: due on the same day of the ninth month. Revenue's example: a period ending 5 December 2024 was due by 5 September 2025.

**Preliminary tax, 2026 periods** ([when is preliminary CT due](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/when-is-preliminary-ct-due.aspx)):

| Company | Amount | Due (calendar 2026 period) |
| --- | --- | --- |
| Small (previous period's CT not above €200,000) | At least the lower of 100% of the previous period's CT and 90% of this period's CT, in one instalment; a top-up is possible | 31 days before the period ends, by the 23rd of that month: 23 November 2026 |
| Large, period longer than seven months | Instalment 1: 50% of the previous period's CT or 45% of this period's CT | 23rd of the sixth month: 23 June 2026 |
| | Instalment 2: brings the total to 90% of this period's CT | 23rd of the eleventh month: 23 November 2026 |
| Large, period of less than seven months | 90% in one instalment | Revenue's page does not state this date; check TDM Part 41A-07-02 |
| New company, first period, CT less than €200,000 | None | Pay the whole CT with the CT1 |

Groups can allocate preliminary tax between members (notional allocation) to reduce interest. This requires an application to Revenue's Debt Management Task Force and full payment of the CT by the return date.

**iXBRL financial statements** ([Revenue: iXBRL](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/index.aspx)):
- **Who must file:** companies managed by Large Corporates Division or High Wealth and Financial Services Division, Section 110 companies, and every other CT filer unless it meets all three small tests: total assets under €4.4 million, turnover under €8.8 million, and 50 or fewer employees on average.
- **How:** iXBRL statements are filed with the CT1 through ROS. Companies that file them skip the CT1 "Extracts from Accounts" panel, but must tag certain mandatory items.
- **More detail:** see TDM Part 41A-03-01.

**Interest on late tax.** Late or short payments carry interest at 0.0219% a day. It is charged on the amount underpaid for the number of days late. It cannot be appealed to the Tax Appeals Commission or reduced.

**Late filing surcharge (s.1084)** ([TDM Part 47-06-08](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf)):
- **Rates:** 5% of the tax, up to €12,695, if the CT1 is filed within two months of the due date; 10%, up to €63,485, if later.
- **Paid on time is not enough:** the surcharge applies even if the tax was paid in full and on time.
- **Incorrect returns:** a careless or deliberate incorrect return is treated as late, unless it is corrected before the due date.
- **Interest:** the surcharge itself carries interest.

**Restriction of reliefs (s.1085)** ([TDM Part 47-06-04](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-04.pdf)). A late CT1 also cuts these claims:
- excess capital allowances;
- loss relief under ss.396(2), 396A(3), 396B(2) and 399(2);
- group relief claims and surrenders.

| Filed late by | Restriction | Maximum restriction |
| --- | --- | --- |
| Less than two months | 25% | €31,740 |
| Two months or more | 50% | €158,715 |

**Time limit for Revenue enquiries (s.959AA)** ([TDM Part 41A-05-04](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41a/41A-05-04.pdf)). Where the company has made a full and true disclosure of all material facts, Revenue cannot make or amend an assessment later than four years after the end of the chargeable period to which the return relates. The limit does not protect a return without full and true disclosure. There is no time limit in cases of fraud or neglect, or where no return was filed.

## 2025 accounting periods: the CT1 being filed now ([TDM Part 47-06-08](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf); [TDM Part 29-02-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf))

- **Due date.** For a 31 December 2025 year end, the CT1 and balance of tax were due by 23 September 2026 on ROS. A return filed after that date is late.
  - Filed before 23 November 2026 (less than two months late): 5% surcharge and a 25% relief restriction.
  - Filed on 23 November 2026: still within two months for the surcharge (5%), but two months late for the relief restriction (50%).
  - Filed after 23 November 2026: 10% surcharge and a 50% restriction.
- **Rates.** 12.5% and 25%, as in 2026.
- **R&D.** The credit is 30% for 2025 periods. For periods commencing on or after 1 January 2025, the first instalment is the greater of €75,000 (or the credit if lower) and 50% of the credit. Claim it within 12 months of the period end: by 31 December 2026 for a calendar 2025 period.
- **KDB.** 10% effective rate.
- **Start-up relief.** 2025 is the first year Class S PRSI of up to €1,000 per director counts, within the €40,000 overall limit.
- **Participation exemption.** For 2025 distributions, the subsidiary look-back is five years, not three.
- **Pillar Two.** For a group whose first year in scope is 2025, the first TIR is due 18 months after that fiscal year ends. For a calendar 2025 year, that is 30 June 2027.

## Completion checklist ([Revenue: payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx))

- [ ] Accounting period confirmed and no longer than 12 months; residence confirmed.
- [ ] Income split into trading (12.5%), non-trading and excepted trade (25%) and chargeable gains; development land kept out of CT.
- [ ] Depreciation, entertainment and capital items added back; capital allowances computed (intangibles cap checked).
- [ ] Losses applied in the right order (s.396A, s.396B, carry forward); group relief consents and the two-year limit checked.
- [ ] Interest limitation: exceeding borrowing costs compared with the €3,000,000 de minimis; standalone status tested properly.
- [ ] Start-up relief limited to qualifying PRSI and the CT bands; the trade start date is within 2009 to 2026.
- [ ] R&D credit at the right rate (30% or 35%), claimed within 12 months, pre-filing notification checked, and the instalment election made.
- [ ] Close company: the previous period's s.440 or s.441 surcharge included on this CT1; this period's dividend plan reviewed.
- [ ] Pillar Two scope tested (€750m or more in two of four years); referred if in scope.
- [ ] Preliminary tax: small or large status, amounts and dates checked; any shortfall and interest noted.
- [ ] iXBRL requirement tested against all three conditions.
- [ ] CT1 and Form 46G filed on ROS and the balance paid by the 23rd of the ninth month (or the earlier date for periods ending before the 21st).
- [ ] Any late filing: surcharge and relief restrictions computed and explained to the client.

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
