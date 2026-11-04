---
name: ee-transfer-pricing
description: "Estonian transfer pricing (siirdehinnad) for tax year 2026: Estonian companies, permanent establishments of foreign companies and sole proprietors (FIE) dealing with associated persons. Covers who is associated under Income Tax Act § 8, the arm's length rule in § 50(4) (companies), § 14(7) (FIE) and § 53(4⁶) (permanent establishments), how an adjustment is taxed at 22/78 in the monthly TSD like a profit distribution, Minister of Finance Regulation No. 53 (methods, 5% low value-adding services mark-up, master file and local file), who must keep full files (250 staff, EUR 50m turnover or EUR 43m balance sheet with associated persons; banks, insurers, listed companies), the 60-day production deadline, fines, interest at 0.06% a day, country-by-country reporting at EUR 750m, MAP and why there is no domestic APA or binding ruling. Trigger on: siirdehind, turuväärtus, seotud isikud, master file Estonia, management fee Estonia. Out of scope: ee-corporate-income-tax (rates, distributions), est"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ee-transfer-pricing"
  jurisdiction: "EE"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Estonian transfer pricing (siirdehinnad): tax year 2026

Source-cited draft: not reviewed by an accountant, not for filing.

Estonia taxes company profit when it leaves the company, not when it is earned. Transfer pricing fits that system. If a price between associated persons is not at market value, the profit the Estonian company gave away (income it did not receive, or a cost it should not have borne) is treated like a hidden distribution. It is taxed in the month of the transaction at the corporate income tax rate on a grossed-up basis, 22/78 of the net amount, through the monthly TSD return (Income Tax Act (TuMS) §§ 8(2), 50(4), 4(1) and (1¹), 54(2) and (4)).

The rules sit in three places:
- **Income Tax Act (Tulumaksuseadus, TuMS):** § 8 (associated persons and the transfer pricing charge), § 14(7) to (9) (sole proprietors), § 50(4) to (8) (resident legal persons), § 53(4⁶) (permanent establishments). Version in force from 1 October 2026; the version in force from 1 January 2027 does not change these sections or the 22% rate.
- **Minister of Finance Regulation No. 53 of 10 November 2006**, "Seotud isikute vahel tehtud tehingute väärtuse määramise meetodid" (methods for valuing transactions between associated persons), as amended from 1 January 2022. It sets the comparability factors, the five methods, the documentation duty and the master file and local file contents.
- **Taxation Act (Maksukorralduse seadus, MKS):** interest, time limits, fines, EU dispute resolution. Country-by-country reporting is in the **Tax Information Exchange Act (Maksualase teabevahetuse seadus, MTVS)**, chapter 2².

The Estonian Tax and Customs Board (Maksu- ja Tolliamet, EMTA) published a transfer pricing guide in 2011, labelled recommended guidance. It still sits on emta.ee. Its figures (the 21/79 rate of 2011, the documentation scope before 2022) are out of date; this skill uses it only for practice that the law has not changed.

Related skills: `ee-corporate-income-tax` (the 22/78 distribution tax and the TSD), `ee-tax-overview`, `estonia-income-tax` (individuals and FIE), `estonia-payroll` and `estonia-social-contributions` (fringe benefits). This skill does not repeat them.

## Who this applies to

**The taxpayers.** Three groups, each with its own charging rule (Regulation No. 53 § 1(1)):
- A resident legal person (an OÜ, AS, partnership or other) dealing with an associated person: TuMS § 50(4).
- A sole proprietor (füüsilisest isikust ettevõtja, FIE) dealing with an associated person in the course of business: TuMS § 14(7). The adjustment is added to business income and taxed in the FIE's annual personal return, not at 22/78.
- A non-resident company's Estonian permanent establishment, for transactions made through it or at its expense with persons associated with the non-resident: TuMS § 53(4⁶), which applies § 50(4) to (8).

The rule applies to domestic transactions as well as cross-border ones. EMTA's 2011 guide says so expressly, and nothing in § 50(4) limits it to foreign counterparties.

**Head office and permanent establishment.** For the transfer pricing rule, a non-resident and its Estonian permanent establishment are associated, and so are an Estonian resident and its foreign permanent establishment (TuMS § 8(3); Regulation No. 53 § 1(2) and (3)). Business units inside one legal person are also treated as associated where at least one of them is taxed under the tonnage scheme in § 52¹ (TuMS § 8(4), § 50(4¹)).

**Who is associated (TuMS § 8(1)).** Persons are associated if they have a common economic interest or one has dominant influence over the other. In any event these are associated:
1. spouses, registered partners, cohabitees, and direct or collateral relatives;
2. companies in one group under § 6 of the Commercial Code;
3. a legal person and an individual holding at least 10% of its share capital, votes or profit rights;
4. a person who, together with associated persons, holds more than 50% of a legal person's share capital, votes or profit rights;
5. legal persons more than 50% of which (capital, votes or profit rights) belongs to the same person or associated persons;
6. persons who each hold more than 25% of the same legal person;
7. legal persons whose management boards (or substitute bodies) are made up of the same persons;
8. an employer and its employee, or the employee's spouse, registered partner, cohabitee or direct relative;
9. a member of a legal person's management or controlling body (§ 9), and that member's spouse, registered partner or direct relative.

The list is a floor, not a ceiling: the opening test (common economic interest or dominant influence) can catch other relationships.

**Fringe benefits go first.** If the advantage is a fringe benefit under § 48 (for example a company selling a car below market value to a board member), it is taxed as a fringe benefit, not under the transfer pricing rule (TuMS § 8(2)). See `estonia-payroll`.

**Who must keep full transfer pricing files.** Every taxpayer must be able to show its prices are at market value under the general bookkeeping rules. The extra documentation in Regulation No. 53 § 18 applies only to (§ 18(1)):
1. resident credit institutions, insurance companies and companies listed on a stock exchange;
2. any transaction where one party is in a non-cooperative jurisdiction for tax purposes;
3. resident companies that, counted together with their associated persons, had 250 or more employees, or turnover of EUR 50 million or more in the financial year before the transaction, or a balance sheet total of EUR 43 million or more;
4. non-residents operating through an Estonian permanent establishment with the same 250 employees, EUR 50 million turnover or EUR 43 million consolidated balance sheet test.

Meeting any one of the three size tests is enough. Companies below all three, and FIEs, are exempt from the master file and local file, but not from the arm's length rule.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Income tax rate | 22% | 2025 onwards, unchanged in the 2026 and 2027 versions | TuMS § 4(1): https://www.riigiteataja.ee/et/akt/109072026066 |
| Gross-up for company-level objects (distributions, § 50(4) adjustments) | Taxable amount divided by 0.78 before the rate, so tax = 22/78 of the net amount | 2025 onwards | TuMS § 4(1¹); EMTA, Tax rates (2026): https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Associated person: individual holding in a legal person | At least 10% of capital, votes or profit rights | 2026 | TuMS § 8(1) 3): https://www.riigiteataja.ee/en/akt/520102026008 |
| Associated persons: common holding in one legal person | More than 25% each | 2026 | TuMS § 8(1) 6) |
| Associated persons: common control | More than 50% held by the same person or associated persons | 2026 | TuMS § 8(1) 4) and 5) |
| Full documentation test: employees | 250 or more, counted with associated persons | 2026 | Regulation No. 53 § 18(1) 3) and 4): https://www.riigiteataja.ee/et/akt/123122021024 |
| Full documentation test: turnover | EUR 50 million or more in the preceding financial year, with associated persons | 2026 | Regulation No. 53 § 18(1) 3) and 4) |
| Full documentation test: balance sheet total | EUR 43 million or more, with associated persons (consolidated, for a permanent establishment) | 2026 | Regulation No. 53 § 18(1) 3) and 4) |
| Low value-adding intra-group services | A 5% mark-up needs no comparables to support it | From 1 January 2022 | Regulation No. 53 § 6(3) |
| Country-by-country report | Group revenue of EUR 750 million or more in the preceding financial year | 2026 | Regulation No. 53 § 18(3) 3); MTVS chapter 2²: https://www.riigiteataja.ee/et/akt/115042026002 |
| Time to hand over transfer pricing information on request | At least 60 days | 2026 | TuMS § 50(7) |
| Interest on late tax | 0.06% a day | 2026 | MKS § 117(1): https://www.riigiteataja.ee/et/akt/116102026009 |
| Fine for not submitting a document on time: legal person | Up to EUR 3,200 | 2026 | MKS § 154(2) |
| Fine for not submitting a document on time: individual | Up to 300 fine units; one fine unit is EUR 8, so up to EUR 2,400 | 2026 | MKS § 154(1); Penal Code § 47(1): https://www.riigiteataja.ee/et/akt/109072026028 |
| Fine for intentionally withholding data or giving false data that cuts tax: legal person | Up to EUR 32,000 | 2026 | MKS § 153¹(2) |
| Coercive payment (sunniraha) to force production of information | Up to EUR 640 the first time, EUR 2,000 the second, EUR 2,640 in total | 2026 | MKS § 67(3) |
| Fine for breaching a country-by-country reporting duty: legal person | Up to EUR 50,000 | From 25 April 2026 | MKS § 155³(2) |
| Time limit for EMTA to assess tax | 3 years from the TSD due date; 5 years if tax was intentionally not paid | 2026 | MKS § 98(1) |

## The taxable base

1. **Find the real transaction.** The market value is set for the transaction actually carried out. A sham transaction is ignored; if it hides another transaction, the hidden one is priced (Regulation No. 53 § 11(6)). Where the parties' conduct does not match the contract, the real terms decide (§ 8(1)).
2. **Compare.** The controlled price is compared with similar transactions between unrelated persons, looking at the features of the goods or services, a functional analysis (functions, assets, risks), the contract terms, economic circumstances and business strategy (Regulation No. 53 §§ 3 to 10).
3. **Pick the method.** The five methods are comparable uncontrolled price, resale price, cost plus, profit split and transactional net margin (Regulation No. 53 §§ 11 to 16). Use the one that gives the most reliable result for the facts and the data. Another method can be used if none of the five fits, with reasons (§ 11(2) and (3)). EMTA can ask why a method was chosen, and can use another method if it shows why (§ 11(4)). The OECD Transfer Pricing Guidelines are recommended reading so far as they do not conflict with the regulation (§ 20).
4. **The range.** The range runs from the lower quartile to the upper quartile of the results from the comparables or methods used (Regulation No. 53 § 2 6)). A transfer price is at market value if it falls inside that range. If it falls outside, EMTA may correct it so the result falls inside the range. A very wide range means the analysis is repeated with better data or another method (Regulation No. 53 § 11(8)). The regulation does not say to which point in the range EMTA adjusts.
5. **Services and management fees.** A service is treated as provided only if it has, or may have, economic value for the recipient and an unrelated person would pay for it or do it itself (Regulation No. 53 § 6(2)). A service that only duplicates what the company already does or buys, or that benefits it only by chance or because it is a group member, is not a chargeable service (§ 6(4)). A provider normally expects to cover costs and make a profit. For low value-adding intra-group services (supporting services outside the group's core business that do not use or create unique or valuable intangibles and carry no significant risk for the provider, § 2 9)), a 5% mark-up does not have to be supported by comparables (§ 6(3)).
6. **Intangibles and cost contribution arrangements.** Identify who owns an intangible and who is entitled to its income (Regulation No. 53 § 5). Cost contribution arrangements need documents showing the contributions and shares are at market value, updated each year (§ 17).
7. **What is taxed (companies).** If the transfer price differs from market value, income tax is charged on the income the company would have received, or the cost it would not have borne, at market value (TuMS § 50(4)). This is a company-level object under § 1(3), so the 0.78 gross-up applies (§ 4(1¹)): tax = adjustment x 22/78. Only adjustments that reduce Estonian profit are taxed. An Estonian company paying more than market value, or charging less, is caught. There is no Estonian tax when the price favours the Estonian side.
8. **No double charge.** § 50(4) does not apply to the part of the difference on which the company has already paid income tax, or on which tax was withheld under § 41 (TuMS § 50(5)). The FIE rule has the same carve-out (§ 14(9)).
9. **Loans to shareholders and the parent.** A loan to a shareholder can itself be taxed as a hidden profit distribution if the facts point that way. For a loan to the parent, or to another subsidiary of the same parent (not the lender's own subsidiary), with a term over 48 months, the company must prove the borrower's ability and intention to repay when EMTA asks, with at least 30 days to respond (TuMS § 50²(1)). Such loans are reported quarterly (TuMS § 56⁵). The interest rate on any intra-group loan or cash pool balance must still be at market value under § 50(4); EMTA's 2011 guide treats a cash pool debit balance as a loan that must carry market interest. See `ee-corporate-income-tax`.
10. **Sole proprietors.** For an FIE, the adjustment is added to business income (TuMS § 14(7)) and taxed in the annual income tax return with the rest of business income. Social tax also follows business income. See `estonia-income-tax`.
11. **What the full files contain.** For taxpayers in scope of Regulation No. 53 § 18(1), the documents split into a master file (group information), a local file (the Estonian entity and its transactions) and, for groups of EUR 750 million or more, the country-by-country report (§ 18(3)). The master file covers 17 items, including the group's legal and ownership structure, value drivers, the supply chain of the five largest products or services and any over 5% of group turnover, intra-group services and their pricing policy, intangibles and R&D policy, intra-group financing, the consolidated accounts, and existing APAs and rulings (§ 18(5)); it can be prepared per business line. The local file covers 20 items, including management structure, business and strategy, competitors, each material controlled transaction with amounts, counterparties and contracts, the comparability and functional analysis, the method and why it was chosen, the comparables and adjustments, and the link to the annual report (§ 18(6)). The information must be current as at the transaction, plus later facts that matter (§ 18(2)). Detail must match the size and complexity of the transaction (§ 18(7)). Documents may be in a foreign language; EMTA can ask for an Estonian translation within a reasonable time (§ 18(9)).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Declare a transfer pricing adjustment (company or permanent establishment) | In the TSD for the month of the transaction, by the 10th of the following month: TSD annex 6, part Ia, code 6000 (difference between the transfer price and market value). The tax at 22/78 goes to TSD code 114 | TuMS § 54(2); Regulation No. 60 annex 7 (TSD annex 6) instructions 2 and 22: https://www.riigiteataja.ee/aktilisa/1260/6202/0024/RM_m24_lisa7.pdf |
| Pay the tax | By the 10th of the month after the month of the transaction | TuMS § 54(4) |
| FIE adjustment | In the annual personal income tax return, by 30 April of the following year | TuMS §§ 14(7) and 44(1) |
| Hand over transfer pricing information to EMTA | On request; EMTA must give at least 60 days | TuMS § 50(7) (§ 53(4⁶) for permanent establishments) |
| Prove ability and intention to repay a long loan to the parent group | On request; at least 30 days | TuMS § 50²(1) |
| Quarterly report of loans to shareholders and the parent group | By the 20th of the month after the quarter | TuMS § 56⁵ |
| Country-by-country report (Estonian reporting entity) | By 31 December of the calendar year after the reporting financial year | MTVS § 20⁵(1) |
| Country-by-country notification (which group member is the reporting entity, and where it is resident) | Within six months after the end of the group's reporting financial year | MTVS § 20⁶(2) to (4) |
| Claim to remove double taxation after an adjustment (domestic corresponding adjustment) | Within three years of the first notice of the action that causes double taxation | Regulation No. 53 § 19(2) |
| EU dispute resolution complaint | Within three years of notice of the act or action causing the dispute | MKS § 151⁴ |

There is no separate transfer pricing return or annual documentation filing. The files are kept and handed over only when EMTA asks.

## Penalties and interest

- **Tax and interest.** The adjustment is taxed at 22/78. Interest at 0.06% a day runs from the day after the TSD payment date until payment (MKS §§ 115(1) and 117(1)). There is no separate transfer pricing surcharge. For a company, the interest, fines and coercive payments are themselves non-business expenses, taxed at 22/78 in the TSD of the month they are paid (TuMS § 51(1) and (2) 1), which points to § 34 3)). An FIE cannot deduct them (§ 34 3)).
- **Late or missing documents.** Not submitting a document on time or not keeping records properly: a fine of up to EUR 3,200 for a legal person, up to 300 fine units (EUR 2,400) for an individual (MKS § 154; Penal Code § 47(1)). EMTA can also set a coercive payment, up to EUR 640 the first time and EUR 2,000 the second, EUR 2,640 in total for the same duty (MKS § 67).
- **False or withheld data.** Intentionally not submitting data, or giving false data, so that tax is reduced: up to EUR 32,000 for a legal person, up to 300 fine units for an individual (MKS § 153¹).
- **Country-by-country reporting.** Not meeting a duty under the MTVS, or obstructing information exchange: up to EUR 50,000 for a legal person (from 25 April 2026), up to 300 fine units for an individual (MKS § 155³).
- **Time limit.** EMTA can assess within three years of the TSD due date for the month concerned, five years where tax was intentionally not paid (MKS § 98(1)).
- **Burden of proof in practice.** Where a price differs from what unrelated persons would agree in similar conditions, EMTA may assess the tax using the values that unrelated independent persons apply (Regulation No. 53 § 1(4)), so a taxpayer without documents is left with EMTA's comparables. Comparable data used must be available to both EMTA and the taxpayer (§ 18(4)).

## Cross-border points

- **Corresponding adjustment.** When EMTA adjusts one party, the other party's profit can be corrected to remove double taxation (Regulation No. 53 § 19(1)). For two Estonian parties, EMTA refunds or offsets the excess tax under the MKS (§ 19(3)). For a foreign counterparty, EMTA starts the procedure with the other tax authority under the EU Arbitration Convention 90/436/EEC, or under a tax treaty that provides for exchange of information and a mutual agreement procedure (§ 19(4)).
- **EU dispute resolution.** MKS chapter 15¹ implements the EU directive on tax dispute resolution. A resident of an EU state files the complaint within three years (§ 151⁴). EMTA confirms receipt within two months (§ 151³), can ask for more information within three months (§ 151⁶), and decides whether to accept within six months (§ 151⁷). A non-EU resident uses the treaty's own procedure (§ 151²(2)).
- **No domestic APA or binding ruling on transfer prices.** EMTA's binding ruling procedure (siduv eelotsus, MKS §§ 91¹ to 91¹²) expressly does not apply to valuing transactions between associated persons under TuMS § 14(7) and § 50(4) (MKS § 91²(2)). No Estonian statute or regulation read for this skill sets up an advance pricing agreement procedure. Regulation No. 53 lists APAs among the items for the master file and local file (§ 18(5) 17) and § 18(6) 17)), which covers APAs the group holds elsewhere.
- **Country-by-country reports.** An Estonian ultimate parent or surrogate parent files the report; another Estonian group member files only in the cases set out in Annex III of the directive, and no Estonian member files where the parent or surrogate files in its own country (MTVS §§ 20⁴ and 20⁵). Every Estonian group member must notify EMTA whether it is the reporting entity and, if not, which entity is and where it is resident (§ 20⁶). EMTA may not use country-by-country data as the sole or main basis for a transfer pricing adjustment (MTVS § 6(1¹)).
- **Reportable arrangements (DAC6).** Three transfer pricing hallmarks are reportable without a main benefit test: unilateral safe harbours, transfers of hard-to-value intangibles, and intra-group transfers of functions, risks or assets that cut the transferor's projected EBIT by more than 50% over the next three years (EMTA, cross-border arrangements guidance, updated 8 January 2025).
- **Exit and withholding.** Moving assets to a foreign permanent establishment and withholding on payments to non-residents have their own rules (TuMS §§ 54⁵ and 41). They are outside this skill.

## Worked examples

### Example 1: management fee to a foreign parent above market value, 2026

Alpha OÜ, an Estonian distributor, is wholly owned by a parent company in another country, so they are associated (TuMS § 8(1) 2) and 4)). In March 2026 the parent charges Alpha EUR 300,000 for group services for the year. On review, only accounting, payroll and IT support pass the benefit test (Regulation No. 53 § 6(2) and (4)). They cost the parent EUR 200,000 and are low value-adding services, so cost plus 5% is accepted without comparables (§ 6(3)): 200,000 x 1.05 = EUR 210,000. The excess of EUR 90,000 is a cost Alpha would not have borne at market value (TuMS § 50(4)).

The tax is 90,000 x 22/78 = EUR 25,384.62 (TuMS § 4(1) and (1¹)). It belonged in the March TSD, due 10 April 2026. If EMTA assesses it later and the tax is paid 400 days late, interest is 25,384.62 x 0.06% x 400 = EUR 6,092.31 (MKS §§ 115 and 117). Had Alpha declared the difference itself in the March TSD (annex 6, code 6000), there would be no interest.

```oa-check
name: Alpha OU, excess management fee to foreign parent, 2026
inputs:
  fee_charged: 300000
  parent_cost_of_qualifying_services: 200000
  lvais_markup_pct: 5
  cit_rate_pct: 22
  interest_rate_per_day_pct: 0.06
  days_late: 400
steps:
  - market_value_fee: parent_cost_of_qualifying_services * (1 + lvais_markup_pct / 100)
  - adjustment: fee_charged - market_value_fee
  - grossed_up_base: adjustment / (1 - cit_rate_pct / 100)
  - income_tax: grossed_up_base * cit_rate_pct / 100
  - interest: income_tax * interest_rate_per_day_pct / 100 * days_late
  - total_cost: income_tax + interest
expected:
  market_value_fee: 210000
  adjustment: 90000
  grossed_up_base: 115384.62
  income_tax: 25384.62
  interest: 6092.31
  total_cost: 31476.92
```

### Example 2: interest-free loan to a sister company, and whether full files are needed (2026)

Beta AS, an Estonian manufacturer, lends EUR 1,200,000 to a sister company in another EU state on 1 January 2026, interest free, repayable in 24 months. The two companies have the same parent, so they are associated (TuMS § 8(1) 2) and 5)). The term is under 48 months, so the special burden of proof in § 50² does not apply, but the interest rate must still be at market value (TuMS § 50(4)). A benchmarking study puts the market rate for this borrower at 6% a year. The income Beta would have received is 1,200,000 x 6% = EUR 72,000 for 2026, or EUR 6,000 a month.

The TSD is monthly, so Beta declares the forgone interest month by month (TuMS § 54(2)): 6,000 x 22/78 = EUR 1,692.31 each month, EUR 20,307.69 for the year.

Does Beta need a master file and local file? It has 180 employees. In 2025, counted with its associated persons, the group had 230 employees, turnover of EUR 38 million and a balance sheet total of EUR 45 million. Employees (230) and turnover (EUR 38 million) are under the limits, but the balance sheet total is over EUR 43 million, and one test is enough (Regulation No. 53 § 18(1) 3)). So Beta must be able to produce a local file and master file for the loan within the deadline EMTA sets (at least 60 days, TuMS § 50(7)). If the group balance sheet had been EUR 42.9 million, Beta would need only the general documentation, but the 22/78 charge on the forgone interest would be the same.

```oa-check
name: Beta AS, interest-free loan to sister company and documentation test, 2026
inputs:
  loan: 1200000
  market_rate_pct: 6
  months: 12
  cit_rate_pct: 22
  group_employees: 230
  group_turnover: 38000000
  group_balance_sheet: 45000000
  employee_limit: 250
  turnover_limit: 50000000
  balance_sheet_limit: 43000000
steps:
  - forgone_interest_year: loan * market_rate_pct / 100
  - forgone_interest_month: forgone_interest_year / months
  - tax_per_month: forgone_interest_month / (1 - cit_rate_pct / 100) * cit_rate_pct / 100
  - tax_year: tax_per_month * months
  - employee_test: min(1, floor(group_employees / employee_limit))
  - turnover_test: min(1, floor(group_turnover / turnover_limit))
  - balance_sheet_test: min(1, floor(group_balance_sheet / balance_sheet_limit))
  - full_files_required: max(employee_test, turnover_test, balance_sheet_test)
expected:
  forgone_interest_year: 72000
  forgone_interest_month: 6000
  tax_per_month: 1692.31
  tax_year: 20307.69
  employee_test: 0
  turnover_test: 0
  balance_sheet_test: 1
  full_files_required: 1
```

## Ask the client first

1. Who owns the company, directly and through associated persons, and who sits on its management board? Does anyone hold 10%, 25% or 50% of the counterparties too? (TuMS § 8(1).)
2. Which transactions are with associated persons, in each direction (goods, services and management fees, royalties, loans, cash pool, guarantees, asset sales), and is any counterparty an employee or board member, which makes it a fringe benefit instead?
3. For the financial year before each transaction: how many employees, what turnover and what balance sheet total, counted together with associated persons? Is the company a bank, insurer or listed company, or is a counterparty in a non-cooperative jurisdiction?
4. For each charge received: what exactly was done, by whom, at what cost, and does any of it duplicate what the company does itself?
5. Has any adjustment already been declared in a TSD, or has tax been withheld on it? Has a foreign tax authority adjusted the other side?
6. Is the group's consolidated revenue EUR 750 million or more, and which entity files the country-by-country report?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tulumaksuseadus (TuMS), consolidated version in force 1 October to 31 December 2026, §§ 1, 4, 8, 14, 34, 44, 50, 50², 51, 53, 54, 56⁵ | https://www.riigiteataja.ee/et/akt/109072026066 | 2026-10-23 |
| TuMS, consolidated version in force from 1 January 2027 (compared: no change to §§ 4(1), 8, 14(7), 50 or 53) | https://www.riigiteataja.ee/et/akt/109072026067 | 2026-10-23 |
| Income Tax Act, English translation of the version in force from 1 October 2026 (§§ 8 and 50) | https://www.riigiteataja.ee/en/akt/520102026008 | 2026-10-23 |
| Rahandusministri 10.11.2006 määrus nr 53, "Seotud isikute vahel tehtud tehingute väärtuse määramise meetodid", consolidated from 1 January 2022 | https://www.riigiteataja.ee/et/akt/123122021024 | 2026-10-23 |
| Maksukorralduse seadus (MKS), consolidated version in force from 17 October 2026, §§ 67, 91¹ to 91¹², 98, 115, 117, 151¹ to 151⁷, 153¹, 154, 155³ (also compared: versions in force from 26 October 2026, 1 November 2026, 1 January 2027 and 1 January 2028, ids 116102026010 to 116102026013, no change to these sections) | https://www.riigiteataja.ee/et/akt/116102026009 | 2026-10-24 |
| Maksualase teabevahetuse seadus (MTVS), consolidated version in force from 25 April 2026, §§ 6, 20³ to 20⁷ | https://www.riigiteataja.ee/et/akt/115042026002 | 2026-10-23 |
| Karistusseadustik (Penal Code), § 47(1) (fine unit EUR 8) | https://www.riigiteataja.ee/et/akt/109072026028 | 2026-10-23 |
| Rahandusministri 29.11.2010 määrus nr 60, annex 7 (TSD annex 6) and instructions, as worded by regulation nr 24 of 22.06.2020 | https://www.riigiteataja.ee/aktilisa/1260/6202/0024/RM_m24_lisa7.pdf | 2026-10-23 |
| EMTA, Tax rates (2026: corporate income tax 22/78) | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates | 2026-10-23 |
| EMTA, Siirdehinna turuväärtuse määramise juhend (2011, recommended guidance) | https://www.emta.ee/sites/default/files/documents/2021-04/siirdehinna-maaramise-juhend.pdf | 2026-10-23 |
| EMTA, transfer pricing hallmarks for cross-border arrangements (updated 8 January 2025) | https://emta.ee/node/382/chapter/23768/pdf | 2026-10-23 |

Not yet confirmed: that the TSD annex 6 layout and code 6000 as worded by regulation nr 24 of 22 June 2020 are unchanged for 2026 periods; whether EMTA accepts or runs bilateral APAs through the treaty mutual agreement procedure (no emta.ee page on APAs was found, and no statute sets one up); which point inside the interquartile range EMTA adjusts to (Regulation No. 53 § 11(8) says only that the result must fall inside the range); whether a 2026 English EMTA page on transfer pricing replaces the 2011 guide.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ee-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ee-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
