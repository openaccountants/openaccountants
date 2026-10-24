---
name: cz-transfer-pricing
description: "Use this skill for Czech transfer pricing (převodní ceny) in tax year 2026. It covers the arm's length rule and the definition of related persons (spojené osoby, the 25% capital or voting test and other links) in Income Taxes Act § 23(7), the self-adjustment in § 23(3)(a)(17), the related-party transactions annex to the corporate return (Přehled transakcí se spojenými osobami, 25 5404/E) and who must file it (CZK 40 million assets, CZK 80 million turnover or 50 employees, plus a foreign related party, a tax loss or an investment incentive), documentation under Tax Code § 92 and Financial Administration guidance D-334 and GFŘ D-34, binding rulings on prices (APAs, § 38nc and § 38nd, guidance GFŘ D-32), country-by-country reporting (EUR 750 million), penalties and late payment interest. Trigger on: transfer pricing Czech Republic, převodní ceny, spojené osoby, cena obvyklá, závazné posouzení ceny, Local File Czech. Out of scope: corporate tax in general (cz-corporate-income-tax), withholding and exit tax (cz-cross-border), VAT (cz-vat-return)."
version: 0.1
jurisdiction: CZ
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Czech Republic: transfer pricing (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. The law comes from the consolidated texts on e-Sbírka (the official Collection of Laws), and the guidance and forms from financnisprava.gov.cz, all read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This is the transfer pricing (TP) skill for the Czech pack. It links rather than repeats:

- Corporate income tax, the base and the return: [cz-corporate-income-tax](cz-corporate-income-tax.md).
- Withholding on payments abroad, exit tax on moving assets out (ITA § 23g), residence and treaties: [cz-cross-border](cz-cross-border.md).
- VAT: [cz-vat-return](cz-vat-return.md). Overview: [cz-tax-overview](cz-tax-overview.md).

The law is Act No. 586/1992 Coll. on Income Taxes ("ITA", consolidated version in force from 1 August 2026) and Act No. 280/2009 Coll., the Tax Code (daňový řád, "TC"). Currency: Czech koruna (CZK).

## Who this applies to

**Any taxpayer that deals with a related person.** The rule in ITA § 23(7) applies to every income tax payer: companies and individuals, residents and non-residents. If prices agreed between related persons differ from prices that unrelated persons would agree in ordinary business on the same or similar terms, and the difference is not satisfactorily documented, the tax office adjusts the taxpayer's base by the difference (ITA § 23(7)). If no arm's length price can be found, the price set under the property valuation law applies.

**Related persons (spojené osoby), ITA § 23(7):**

- **Capital links.** One person holds, directly or indirectly, at least 25% of the registered capital or voting rights of the other. All persons held at that level by the same person are related to each other (§ 23(7)(a)). The holding is the arithmetic average of monthly holdings in the period.
- **Other links** (§ 23(7)(b)):
  - one person takes part in managing or controlling the other;
  - the same persons, or close persons, take part in managing or controlling both (sitting on the supervisory boards of both does not count);
  - controlling and controlled persons, and persons controlled by the same person;
  - close persons (osoby blízké);
  - persons who set up a legal relationship mainly to reduce the tax base or increase a tax loss.

Paid membership of a control commission or a similar audit body is not "taking part in control" (§ 23(7)).

**Exceptions.** The adjustment does not apply to a free loan of a thing (výprosa, výpůjčka). It also does not apply where interest on a loan between related persons is lower than arm's length and the lender is a non-resident, a member of the corporation who is a Czech tax resident, or an individual (§ 23(7)).

**Domestic deals count too.** The Ministry of Finance guidance on documentation applies to purely domestic related-party dealings as well as cross-border ones (Pokyn D-334, part 1).

**Permanent establishments.** A non-resident's Czech permanent establishment must not end up with a lower base than a Czech resident doing the same work on similar terms (ITA § 38nd(2); the attribution rule is ITA § 23(11)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Corporate income tax rate (applies to any TP adjustment of a company) | 21% | 2026 | https://e-sbirka.gov.cz/sb/1992/586 (§ 21(1)) |
| Capital link test for related persons | at least 25% of capital or voting rights, direct or indirect | 2026 | https://e-sbirka.gov.cz/sb/1992/586 (§ 23(7)(a)) |
| Annex size test: total assets | more than CZK 40,000,000 | periods starting 2025 (form vzor 12) | https://financnisprava.gov.cz/assets/tiskopisy/5404-E_12.pdf |
| Annex size test: annual net turnover | more than CZK 80,000,000 | periods starting 2025 (form vzor 12) | https://financnisprava.gov.cz/assets/tiskopisy/5404-E_12.pdf |
| Annex size test: average employees | more than 50 | periods starting 2025 (form vzor 12) | https://financnisprava.gov.cz/assets/tiskopisy/5404-E_12.pdf |
| Annex figures | whole CZK thousands | periods starting 2025 | https://financnisprava.gov.cz/assets/tiskopisy/5404-E_12.pdf |
| Thin capitalisation: related-party debt above which interest is not deductible | 4 times equity (6 times for banks and insurers) | 2026 | https://e-sbirka.gov.cz/sb/1992/586 (§ 25(1)(w)) |
| Fee for a binding ruling (APA) application | CZK 10,000 per transaction or set of aggregated transactions | 2026 | https://e-sbirka.gov.cz/sb/2004/634 (tariff item 1(1)(n)); https://financnisprava.gov.cz/assets/cs/prilohy/d-zakony/Pokyn_GFR_D_32.pdf |
| Binding ruling stops covering periods that start more than | 3 years after it becomes final (shorter if the tax office sets it) | 2026 | https://e-sbirka.gov.cz/sb/2009/280 (§ 133(3)) |
| Penalty on extra tax assessed by the tax office (penále) | 20% of the extra tax; 1% of a reduced tax loss | 2026 | https://e-sbirka.gov.cz/sb/2009/280 (§ 251(1)) |
| Late return penalty | 0.05% of the tax a day after 5 working days, capped at 5% and CZK 300,000 | 2026 | https://e-sbirka.gov.cz/sb/2009/280 (§ 250) |
| Penalty for a missed reporting or record-keeping duty | up to CZK 500,000 | 2026 | https://e-sbirka.gov.cz/sb/2009/280 (§ 247a(1)) |
| Late payment interest: CNB repo rate on the first day of the calendar half-year in which each day of interest falls, plus 8 points | 11.50% a year for days from 1 January to 30 June 2026; 11.75% for days from 1 July to 31 December 2026 | 2026 | https://e-sbirka.gov.cz/sb/2009/280 (§ 251a(5), § 252(4)); https://e-sbirka.gov.cz/sb/2013/351 (§ 2(1)); https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt |
| Country-by-country report: group consolidated revenue in the prior year | EUR 750,000,000 or more | 2026 | https://e-sbirka.gov.cz/sb/2013/164 (§ 13zd(2)) |
| Time limit to assess tax | 3 years from the filing deadline, extendable, 10 years at most | 2026 | https://e-sbirka.gov.cz/sb/2009/280 (§ 148(1), (5)) |

Repo rate: 3.50% from 9 May 2025 and 3.75% from 19 June 2026 (CNB repo history). The rate on 1 January 2026 was 3.50%, so 3.50 + 8 = 11.50%; on 1 July 2026 it was 3.75%, so 3.75 + 8 = 11.75%.

## The taxable base

**The adjustment.** The tax office compares the agreed price with the arm's length price and adjusts the base by the difference that the taxpayer cannot satisfactorily document (ITA § 23(7)). The adjustment is to the base, so tax follows at the normal rate: 21% for a company (§ 21(1)).

**Self-adjustment.** A taxpayer whose base was reduced because a related-party price departed from arm's length must add the difference back to its accounting result. This does not apply to the part of the difference that the related persons settled between themselves (ITA § 23(3)(a)(17)). If the error is found after filing, a supplementary return is due (see Deadlines).

**Methods and the range.** Czech law does not list methods. The Financial Administration applies the OECD Transfer Pricing Guidelines and their five methods: comparable uncontrolled price, resale price, cost plus, transactional net margin and profit split (Pokyn GFŘ D-34, parts 1.1.3 and 3). Its guidance on the arm's length range (D-34, part 2.4):

- Comparables data for 3 to 5 years is recommended.
- Where comparability is high and the data sit in a narrow band, use the full range.
- Where database comparables are less comparable and include extreme values, statistical tools such as the interquartile range may narrow the range. Values between the 25th and the 75th percentile then count as arm's length. Give the reasons for using it.
- A taxpayer outside the updated range of comparables, with no satisfactory explanation, is adjusted (D-34, part 2.3).

**Interest on related-party loans.** Besides the arm's length test, interest and related costs on loans from related persons are not deductible on the part of related-party debt above 4 times equity (6 times for banks and insurers) (ITA § 25(1)(w)). The separate limit on exceeding borrowing costs (30% of tax EBITDA) is in ITA § 23e; no skill in this pack covers it yet.

**Moving assets abroad within one entity.** A transfer of assets from the Czech Republic abroad without a change of owner is treated as a sale to itself at the arm's length price (ITA § 23g(1)). The exit tax detail is in [cz-cross-border](cz-cross-border.md).

## Deadlines and filing

**Corporate return.** Due within 3 months after the end of the tax period. The deadline extends to 4 months where the return is filed electronically after the 3-month date. It extends to 6 months where the accounts must be audited, or where a tax adviser files after the 3-month date (TC § 136(1) and (2)).

**Related-party transactions annex (Samostatná příloha k položce 12 I. oddílu, Přehled transakcí se spojenými osobami, form 25 5404/E).** It is filed with the corporate return, one annex per related person with whom the taxpayer had transactions in the period ([form vzor 12 and instructions](https://financnisprava.gov.cz/assets/tiskopisy/5404-E_12.pdf)). A taxpayer must file it if both tests are met:

1. **Size:** at least one of total assets above CZK 40 million, annual net turnover above CZK 80 million, or an average of more than 50 employees; and
2. **Trigger:** at least one of:
   - a transaction with a related person seated abroad (annex for those foreign related persons only);
   - a tax loss on line 200 and a transaction with any related person (annex for all related persons, domestic too);
   - an investment incentive taken as a tax credit under Act 72/2000 and a transaction with any related person (annex for all related persons).

Permanent establishments of non-residents do not file the annex. Banks, insurers and other bodies under § 11(2)(b) to (g) of Act 456/2011 leave out some lines.

The annex reports, in whole CZK thousands: sales and purchases of intangible, tangible and financial fixed assets and inventory; income and costs for services, royalties (including software), interest (including cash pooling), rent and other transactions; loans received and given, profit shares and other equity movements; yes or no flags for free supplies given or received, cash pooling, and financial or bank guarantees given or received; and long-term and short-term receivables and payables at the end of this period and the prior period.

**Documentation.** No Czech statute requires a taxpayer to prepare transfer pricing documentation. But the taxpayer must prove everything it states in its return, and the tax office can call on it to prove facts (TC § 92(3) and (4)). In practice this means showing that the price meets § 23(7) (Pokyn GFŘ D-34, part 4). The content the Financial Administration expects is in Pokyn D-334, which the Financial Administration lists as current:

- information on the group: structure, functions and risks, intangibles and royalty flows, the group TP policy, cost-sharing arrangements and APAs;
- information on the company: business, ownership, results and strategy;
- the transaction: what is supplied, contracts, volume, functions and risks, and for services the purpose and the expected benefit;
- other circumstances: market conditions, marketing strategies, legal specifics;
- the pricing method, why it was chosen, comparables (internal first, then external) and the comparability analysis;
- whether the file follows the EU master file and country file approach.

D-34 also describes the OECD three-tier structure: master file, local file and country-by-country report. Keep documentation at least as long as tax can be assessed (TC § 148) and as long as the Accounting Act requires (D-334, part 5).

**Binding ruling on prices (závazné posouzení ceny, the Czech APA), ITA § 38nc.**

- A taxpayer that agrees prices with a related person may ask its tax office to rule whether the way the price was set matches how independent persons would set it.
- The application must name all persons involved and describe the group structure, the business, the transaction, the periods covered, the method with documentation and forecast assumptions, and the proposed ruling (§ 38nc(2)).
- Where the persons involved fall under different tax offices, a higher office rules (§ 38nc(3)); in practice this is the General Financial Directorate (GFŘ), which also handles bilateral and multilateral APAs (Pokyn GFŘ D-32, part I.3).
- A ruling can be issued for a company not yet founded (§ 38nc(4)).
- The application can cover the period in which it is filed and later periods (D-32, part I.2). It must be in Czech (D-32, part I.1).
- The fee is CZK 10,000 per transaction or set of aggregated transactions (D-32, part I.5.1). No appeal lies against the ruling (TC § 132(3)).
- The ruling binds the tax office only while the facts match the application (TC § 133(1) and (5)). It lapses if the law changes (§ 133(2)). It does not cover periods that start more than 3 years after it became final (§ 133(3)).
- A non-resident can get a similar ruling on the base of its Czech permanent establishment (ITA § 38nd).

**Supplementary return.** A taxpayer that finds its tax should be higher, for example after a TP self-adjustment, must file a supplementary return and pay the difference by the end of the month after the month it found out. This duty lasts while tax can still be assessed (TC § 141(1)).

**Country-by-country reporting** (Act 164/2013, §§ 13za to 13zq). It applies to groups with consolidated revenue of EUR 750 million or more in the prior year (§ 13zd(2)).

- Every Czech member entity files a notice (ohlášení) by the end of the reporting year in which it became a member. The notice names the ultimate parent and says who files the report (§ 13zn(1) and (2)). Changes must be reported within 15 days (§ 13zn(4)).
- A Czech ultimate parent, or a Czech entity that files for the group, files the report (oznámení) within 12 months after the end of the reporting year (§§ 13zl, 13zm(1)).

## Penalties and interest

- **Penalty on adjusted tax (penále).** When the tax office assesses extra tax, the penalty is 20% of the extra tax, or 1% of a reduced tax loss (TC § 251(1)). There is no penalty on tax the taxpayer disclosed itself in a valid supplementary return (§ 251(4)).
- **Late payment interest.** It runs from the fourth day after the original due date until payment (TC § 252(2)). A later assessment does not move the start date: interest on a TP adjustment runs from the original due date of the return. The rate is the CNB repo rate on the first day of the calendar half-year in which each day of interest falls, plus 8 points (TC § 251a(5) and § 252(4); Government Regulation 351/2013 § 2(1)). Days from 1 January to 30 June 2026 bear 11.50% a year; days from 1 July to 31 December 2026, 11.75%. Interest is not charged if the total for one tax and one period does not exceed CZK 1,000 (TC § 251a(2)).
- **Late return.** 0.05% of the tax for each day after the first 5 working days, capped at 5% of the tax (0.01% a day on a tax loss). It is not charged under CZK 1,000 and cannot exceed CZK 300,000 (TC § 250(1), (3), (5)). The annex is part of the corporate return, not a separate filing.
- **Missed reporting or record-keeping duties.** The tax office may fine up to CZK 500,000 for a missed reporting duty or record-keeping duty set by a tax law or by the tax office (TC § 247a(1)). A taxpayer that does not cure a defect in a filing under TC § 74(1)(c) or (d) when called on pays CZK 1,000, which can rise to CZK 50,000 where this seriously hinders tax administration (§ 247a(2) and (4)).
- **Country-by-country reporting.** Fines of up to CZK 1,500,000 for an ultimate parent or a surrogate filer, and up to CZK 600,000 for other Czech member entities, for breaching the reporting duty (Act 164/2013, § 13zp).
- **Time limit.** Tax can be assessed for 3 years from the filing deadline. A tax audit restarts the period, and other acts extend it by 1 year, but never beyond 10 years (TC § 148). Where a tax loss could be carried forward, the period runs with the last year the loss could be used (ITA § 38r(2)).

## Cross-border points

- **Treaties.** Article 9 (associated enterprises) of Czech tax treaties sets the same arm's length rule. A corresponding adjustment in the other state follows Article 9(2) where the treaty has it, and the mutual agreement procedure (Article 25 of the OECD Model) (Pokyn GFŘ D-34, part 5).
- **EU disputes.** Inside the EU, double taxation from a TP adjustment can also go to the EU Arbitration Convention (90/436/EEC). D-34 says the EU dispute resolution directive (2017/1852) was to be transposed for complaints filed after 30 June 2019 about periods starting on or after 1 January 2018 (D-34, part 5).
- **The annex looks at foreign related persons first.** A company over the size test files the annex for every foreign related person. It files for domestic related persons too only when it reports a tax loss or claims an investment incentive (form 25 5404/E instructions).
- **Adjustments paid to a foreign related person become dividends.** For a non-resident, the difference found between the agreed price and the arm's length price (§ 23(7)), and interest not deductible under § 25(1)(w) (thin capitalisation) or § 25(1)(zl) (profit-participating loans), count as a profit share from a Czech source (ITA § 22(1)(g)(3)). Profit shares paid to non-residents are taxed at 15% (ITA § 36(1)(b)(1)). This does not apply where the recipient is resident in another EU or EEA state or in Switzerland (§ 22(1)(g)(3)). The withholding mechanics, the 35% rate for non-cooperative states and treaty caps are in [cz-cross-border](cz-cross-border.md).
- **Permanent establishments.** Profit attribution follows ITA § 23(11) and the treaty's Article 7, using the OECD 2010 report on attributing profits to permanent establishments (Pokyn GFŘ D-32, part III.1).

## Worked examples

### Example 1: the tax office cuts a management fee paid to a foreign parent

A Czech s.r.o. pays its German parent a management fee of CZK 6,000,000 for 2026 and deducts it in full. In a later tax audit the tax office shows that comparable independent services would have cost CZK 4,500,000. The company cannot satisfactorily document the difference.

1. The tax office adds the CZK 1,500,000 difference to the base (ITA § 23(7)).
2. Extra corporate tax at 21%: CZK 315,000 (§ 21(1)).
3. Penalty (penále) of 20% of the extra tax: CZK 63,000 (TC § 251(1)(a)).
4. Total before interest: CZK 378,000.
5. Late payment interest also runs on the CZK 315,000 from the fourth day after the original due date of the 2026 return until payment (TC § 252(2)). The rate changes each half-year (11.50% a year for days in January to June 2026, 11.75% for July to December 2026; TC § 251a(5)), so it is not computed here.
6. The parent is resident in Germany, an EU state, so the CZK 1,500,000 is not treated as a Czech-source dividend to it (ITA § 22(1)(g)(3)). Had the parent been outside the EU, the EEA and Switzerland, the difference would count as a profit share taxed at 15% (§ 36(1)(b)(1)), subject to the treaty.
7. To remove the double taxation, the group can use the mutual agreement procedure in the Czech-German tax treaty or the EU Arbitration Convention.

```oa-check
name: Management fee cut by CZK 1,500,000 on audit (2026)
inputs:
  fee_paid: 6000000
  arm_length_fee: 4500000
  cit_rate: 21
  penale_rate: 20
steps:
  - adjustment: fee_paid - arm_length_fee
  - extra_tax: adjustment * cit_rate / 100
  - penale: extra_tax * penale_rate / 100
  - total_before_interest: extra_tax + penale
expected:
  adjustment: 1500000
  extra_tax: 315000
  penale: 63000
  total_before_interest: 378000
```

### Example 2: the company corrects a royalty itself and checks the annex

A Czech a.s. pays its Dutch parent a royalty of 8% of sales of the licensed products. Those sales for 2025 were CZK 50,000,000. Its total assets are CZK 60,000,000, its total net turnover is CZK 90,000,000 and it has 40 employees. After filing the 2025 return, its benchmark (interquartile range, reasons given) shows that 5% is the highest arm's length royalty rate. The company decides to correct to 5% before any audit. The related persons did not settle the difference.

1. Annex check: the company passes the asset test (CZK 60 million is above CZK 40 million) and the turnover test (CZK 90 million is above CZK 80 million), and it has a foreign related person. So it must file the annex for the Dutch parent, reporting the royalty on line B2. Passing one size test is enough; the employee test is not needed.
2. Royalty paid: 8% of CZK 50,000,000 = CZK 4,000,000. At 5%: CZK 2,500,000. Excess: CZK 1,500,000.
3. The excess is added back to the base (ITA § 23(3)(a)(17)). The company files a supplementary return and pays the extra tax by the end of the month after the month it found the error (TC § 141(1)).
4. Extra tax at 21%: CZK 315,000.
5. No 20% penalty arises because the company disclosed the tax itself in a supplementary return (TC § 251(4)). It saves CZK 63,000 compared with an audit adjustment. Late payment interest still runs from the fourth day after the original due date of the 2025 return.

```oa-check
name: Royalty self-adjustment 8% to 5% on sales CZK 50,000,000 (2025 return, corrected 2026)
inputs:
  sales: 50000000
  royalty_paid_pct: 8
  royalty_alp_pct: 5
  cit_rate: 21
  penale_rate: 20
  assets: 60000000
  asset_test: 40000000
steps:
  - royalty_paid: sales * royalty_paid_pct / 100
  - royalty_alp: sales * royalty_alp_pct / 100
  - add_back: royalty_paid - royalty_alp
  - extra_tax: add_back * cit_rate / 100
  - penale_avoided: extra_tax * penale_rate / 100
  - assets_over_test: assets - asset_test
expected:
  royalty_paid: 4000000
  royalty_alp: 2500000
  add_back: 1500000
  extra_tax: 315000
  penale_avoided: 63000
  assets_over_test: 20000000
```

## Ask the client first

1. Who the related persons are: the ownership chain with percentages (direct and indirect, monthly averages), shared managers or controllers, and any close persons.
2. Which transactions there were with each related person in the period, by type and amount, and whether each related person is Czech or foreign.
3. The company's total assets, net turnover and average employees, whether it reports a tax loss, and whether it claims an investment incentive. These decide whether the annex is due and for which related persons.
4. How each price was set: the method, any benchmark or group TP policy, and whether a master file or local file exists.
5. Related-party loans: the balances, interest rates and the company's equity. These decide the thin capitalisation test.
6. Whether the group's consolidated revenue reached EUR 750 million, and whether any APA, treaty procedure or tax audit is open.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 586/1992 Coll., Income Taxes Act, version in force from 1 August 2026: §§ 21(1), 22(1)(g)(3), 23(3)(a)(17), 23(7), 23(11), 23g(1), 25(1)(w), 36(1)(b), 38nc, 38nd, 38r(2) | https://e-sbirka.gov.cz/sb/1992/586 | 2026-10-23 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026: §§ 74, 92, 132, 133, 136, 141, 148, 247a, 250, 251, 251a, 252 | https://e-sbirka.gov.cz/sb/2009/280 | 2026-10-23 |
| Act No. 634/2004 Coll., Administrative Fees, tariff item 1(1)(n) | https://e-sbirka.gov.cz/sb/2004/634 | 2026-10-23 |
| Act No. 164/2013 Coll., International Cooperation in Tax Administration, §§ 13zd, 13zl, 13zm, 13zn, 13zp | https://e-sbirka.gov.cz/sb/2013/164 | 2026-10-23 |
| Government Regulation No. 351/2013 Coll., § 2(1) (late payment interest: repo plus 8 points) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-10-23 |
| Finanční správa, form 25 5404/E vzor 12, Přehled transakcí se spojenými osobami, with instructions | https://financnisprava.gov.cz/assets/tiskopisy/5404-E_12.pdf | 2026-10-23 |
| Finanční správa, Pokyn D-334 (documentation scope), listed as current | https://financnisprava.gov.cz/assets/cs/prilohy/d-zakony/D-334.pdf | 2026-10-23 |
| Finanční správa, Pokyn GFŘ D-34 (arm's length principle, methods, range, documentation, adjustments) | https://financnisprava.gov.cz/assets/cs/prilohy/d-zakony/Pokyn-GFR-D-34.pdf | 2026-10-23 |
| Finanční správa, Pokyn GFŘ D-32 (binding rulings under §§ 38nc and 38nd) | https://financnisprava.gov.cz/assets/cs/prilohy/d-zakony/Pokyn_GFR_D_32.pdf | 2026-10-23 |
| Finanční správa, pokyny a sdělení 2010 (status of D-332, D-333, D-334) | https://financnisprava.gov.cz/cs/mezinarodni-spoluprace/mezinarodni-zdanovani-prime-dane/pokyny-sdeleni/2010 | 2026-10-23 |
| Finanční správa, Převodní ceny, zdaňování nadnárodních společností | https://financnisprava.gov.cz/cs/mezinarodni-spoluprace/mezinarodni-zdanovani-prime-dane/prevodni-ceny-zdanovani-nadnarodnich-spolecnosti | 2026-10-23 |
| Czech National Bank, two-week repo rate history | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-10-23 |

Not yet confirmed: the form version of the annex for tax periods starting in 2026 (vzor 12 covers periods starting in 2025 and parts of 2026 periods whose filing deadline falls by 31 December 2026; a later vzor had not been found); whether Pokyn GFŘ D-35, announced in D-34 to replace D-334, has been issued (it was not found on the Financial Administration pages read, and D-334 is listed as current); the Czech act that transposes EU directive 2017/1852 and its procedure; the day-count basis the Financial Administration uses to compute late payment interest; whether Article 9(2) appears in each Czech treaty; and the point in the range (median or nearest edge) to which the tax office adjusts a price that falls outside the arm's length range, which the guidance read does not state.

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
