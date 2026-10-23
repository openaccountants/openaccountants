---
name: ro-transfer-pricing
description: "Romanian transfer pricing for tax year 2026: who is an affiliated person (Fiscal Code art. 7 pt. 26, the 25% holding or effective control test), the arm's length rule and the five methods (art. 11(4)), the transfer pricing file (dosarul prețurilor de transfer) under Fiscal Procedure Code art. 108(2) and ANAF Order 442/2016, the large taxpayer thresholds (EUR 200,000 / 250,000 / 350,000) and annual preparation by the corporate tax return deadline, the on-request regime for others (EUR 50,000 / 50,000 / 100,000, 30 to 60 days to present), the interquartile range and the median adjustment, APAs and their EUR 10,000 / 20,000 fees, the RON 2,000 to 14,000 fine for not preparing or presenting the file, and country-by-country reporting. Trigger on: transfer pricing Romania, prețuri de transfer, dosarul prețurilor de transfer, persoane afiliate, OPANAF 442/2016, acord de preț în avans, CbCR Romania. Out of scope: corporate tax rates, base and filing (ro-corporate-income-tax), withholding and exit tax (ro-cross-border), VAT market value rules (ro-vat-return)."
jurisdiction: RO
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Romania: transfer pricing (prețuri de transfer) v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific company's facts, transactions or filings. Do not rely on it to file, price a transaction or take a tax position without review by a qualified professional in Romania.

Tax year: 2026, the calendar year unless the company has a modified fiscal year. Currency: leu (RON); the documentation thresholds are set in euro. Authority: ANAF (Agenția Națională de Administrare Fiscală); its transfer pricing and APA directorate (DPTAPA) runs APAs and mutual agreement cases.

The law:
- Legea 227/2015, the Fiscal Code ("CF"): art. 7 pt. 26 (affiliated persons), art. 7 pt. 33 (arm's length principle), art. 11(4) (adjustment and methods).
- Legea 207/2015, the Fiscal Procedure Code ("CPF"): art. 52 (APAs), art. 108(2) (the file), art. 283 (domestic corresponding adjustment), art. 291^3 and annex 3 (CbCR), art. 336 (fines).
- ANAF President's Order 442/2016 ("the Order"): thresholds, deadlines, content, and the adjustment and estimation procedure.

Both codes were read on 23 October 2026 in ANAF's consolidated texts, shown as last updated by Legea 170/2026. ANAF notes these are not an official republication. The Order was read in ANAF's copy of the text published in Monitorul Oficial nr. 74 of 2 February 2016.

See also: ro-corporate-income-tax (rate, base, interest limitation, return and payment), ro-cross-border (residence, withholding on outbound payments, exit tax, and the general penalty rules), ro-vat-return.

## Who this applies to

- **Any taxpayer that deals with an affiliated person.** Transactions between affiliated persons must follow the market value (arm's length) principle (CF art. 11(4); for companies also art. 19(6)). This covers companies, permanent establishments of foreign companies, and individuals. It applies to cross-border and to purely domestic transactions (ANAF transfer pricing guide, section 1).
- **Affiliated persons** (CF art. 7 pt. 26). A person is affiliated with another in at least one of these cases:
  - two individuals who are spouses or relatives up to the third degree;
  - an individual and a legal person, where the individual holds, directly or indirectly, including holdings of the individual's affiliated persons, at least 25% of the value or number of shares or voting rights, or effectively controls it;
  - two legal persons, where one holds at least 25% in the other on the same basis, or effectively controls it;
  - two legal persons, where a third person holds at least 25% in both on the same basis, or effectively controls both.
- **Who must prepare the file, and when.** The Order splits taxpayers into three groups:

  | Group | Duty | Rule |
  |---|---|---|
  | Large taxpayers (designated by ANAF order) at or above any large-taxpayer threshold | Prepare the file every year | Order art. 2(1) |
  | Large taxpayers below those thresholds, and small and medium taxpayers, at or above any lower threshold | Prepare and present the file only when requested in a tax inspection | Order art. 2(4) |
  | Taxpayers below the lower thresholds | No file. Arm's length is shown under the general accounting and tax rules in an inspection | Order art. 2(5) |

- **How the threshold is measured.** The total annual value of each type of transaction with all affiliated persons together, excluding VAT, converted at the National Bank of Romania rate for the last day of the fiscal year (Order art. 2(1) and (4)). Meeting any one threshold triggers the duty.
- **Fiscal groups.** Each member of a corporate tax fiscal group prepares its own file, covering transactions with other members and with affiliates outside the group. The responsible legal person presents the files (CF art. 42^6).
- **No file needed** for transactions and periods covered by an ANAF APA, or for transactions already covered by an adjustment/estimation decision under CPF art. 283 (Order art. 6).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Affiliation holding test | 25% of shares or voting rights, direct or indirect, or effective control | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Large taxpayer annual file: interest on financial services, received or paid | EUR 200,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf |
| Large taxpayer annual file: services received or provided | EUR 250,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf |
| Large taxpayer annual file: purchases or sales of tangible or intangible goods | EUR 350,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf |
| File on request (other taxpayers): interest on financial services | EUR 50,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf |
| File on request: services received or provided | EUR 50,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf |
| File on request: purchases or sales of tangible or intangible goods | EUR 100,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf |
| Adjustment point | median of the interquartile range; arithmetic mean if at most three comparables | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf |
| Corporate income tax rate on an upward adjustment | 16% | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| APA issue fee, large taxpayers (or transactions over EUR 4,000,000) | EUR 20,000; modification EUR 15,000 | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| APA issue fee, other taxpayers | EUR 10,000; modification EUR 6,000 | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Fine for not preparing or not presenting the file: medium and large taxpayers | RON 12,000 to 14,000 | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Same fine: other legal persons and individuals | RON 2,000 to 3,500 | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| CbCR group revenue threshold | EUR 750,000,000 consolidated revenue in the prior year | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| CbCR fine: late, incorrect or incomplete report | RON 30,000 to 50,000 | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| CbCR fine: report not filed | RON 70,000 to 100,000 | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |

The thresholds are those of the Order as published in 2016. ANAF's transfer pricing guide, updated November 2025, gives the same six figures.

## The taxable base

**The arm's length principle.** Where conditions between two affiliated persons differ from those that would exist between independent persons, the profit that would have arisen without those conditions can be added to that person's profit and taxed (CF art. 7 pt. 33).

**Adjustment and estimation** (CF art. 11(4)). ANAF can:
- **adjust** the income or expense of either affiliated party where arm's length is not respected; or
- **estimate** it where the taxpayer does not give ANAF the data needed to test the transfer prices.

In both cases the figure is set at the central tendency of the market.

**Methods.** The most appropriate of these applies (CF art. 11(4)):
- (a) comparable uncontrolled price;
- (b) cost plus;
- (c) resale price;
- (d) transactional net margin;
- (e) profit split;
- (f) any other method recognised in the OECD Transfer Pricing Guidelines.

The OECD Guidelines, as amended, apply in using art. 11(4). The Order is completed by them and by the EU Code of Conduct on transfer pricing documentation (Order art. 10).

**The range and the median** (Order art. 8 and 9):
1. Comparables are searched in this order: national, EU, pan-European, international (art. 8 pt. 1).
2. The data must have been reasonably available when the prices were set or documented (art. 8 pt. 2).
3. The full set of comparable results (the comparison margin) is split into 4 segments. The top and bottom segments are extreme results and are dropped. What is left is the comparison interval, the interquartile range (art. 8 pt. 4).
4. A controlled transaction is arm's length if its price, margin or result falls inside that interval (art. 8, opening words).
5. If it falls outside, ANAF adjusts or estimates to the central tendency of the market, which is the median of the interval (art. 9(1) and (2)). Extreme results are never used in the calculation (art. 8 pt. 5).
6. If the median cannot be identified, it is the arithmetic mean of the two middle values (art. 8 pt. 6).
7. If at most three comparables can be found, ANAF uses their arithmetic mean (art. 9(2)).
8. Comparables are taken from data that both ANAF and the taxpayer can access (art. 9(3)).

**When the file is missing or incomplete** (Order art. 7):
- Not presenting the file on time in an inspection lets ANAF treat the transactions as undocumented (art. 7(2)).
- An incomplete file counts as missing the data needed to test the prices (art. 7(3)).
- In both cases ANAF estimates the transfer prices, only for the undocumented transactions, at the central tendency of the market (art. 7(4)).

**Domestic corresponding adjustment** (CPF art. 283):
- Where ANAF adjusts one of two Romanian affiliated persons, the adjustment binds the tax office of the other one too (art. 283(2)).
- Once the assessment is final, ANAF issues an adjustment/estimation decision to the other party (art. 283(3) and (4)).
- That party can correct its return for the period of the transaction (art. 283(5)).
- Inside a corporate tax fiscal group, ANAF adjusts the other member by the same amount in the same inspection (art. 283(2^1)).

**What the file contains** (Order annex 3). It follows the OECD BEPS Action 13 and EU master file / local file structure:
- **Group information (A, 11 points):** structure, business and strategy, group transfer pricing policy, intangibles, intra-group financing, restructurings, R&D, and APAs not issued by ANAF.
- **Taxpayer information (B, 16 points):** the affiliated persons and the transactions with each of them, including flows, invoiced values and payments; the functional and comparability analysis; the benchmarking search, with accepted and rejected comparables and the reasons for rejecting them; the method and the tested party; and any other relevant information.

Formalities (Order art. 5(4) and (5)):
- Pages must be filed in order, numbered and indexed.
- Foreign-language documents need a Romanian translation.
- Annexes available electronically are handed over in an editable format.

## Deadlines and filing

- **Large taxpayers at or above the thresholds: annual file.** It must be ready by the legal deadline for the annual corporate income tax return for that year (Order art. 2(1)). That return is due by 25 June of the next year (CF art. 42(1)). For 2026: **25 June 2027**. A modified fiscal year files by the 25th of the sixth month after the year closes (CF art. 42(2)). The file is not filed with the return. It is kept and presented on request:
  - ANAF can ask for it in an inspection (Order art. 2(2)) or outside one (art. 2(3); CPF art. 58 and 64).
  - Time to present: at most 10 calendar days from the request, but not earlier than 10 days after the preparation deadline (Order art. 4(1)).
- **Other taxpayers at or above the lower thresholds: file on request.** It is prepared and presented only when requested in a tax inspection (Order art. 2(4)):
  - The inspector sets the deadline in the request, between 30 and 60 calendar days.
  - The deadline can be extended once, on written request, by at most 30 calendar days.
  - The inspection can be suspended until then (Order art. 4(2); CPF art. 127(1)(b)).
- **More information.** On written request, the taxpayer must give extra information to complete the file (Order art. 5(1)).
- **APA annual report.** An APA holder files a yearly report on how it met the terms of the APA. It is due by the deadline for the annual financial statements (CPF art. 52(13)).
- **CbCR.** The Romanian ultimate parent, or another reporting entity, files the country-by-country report within 12 months of the end of the group's reporting year (CPF art. 291^3(1)). For a calendar 2026 group year that is by 31 December 2027.
- **CbCR notification.** Each Romanian constituent entity must notify ANAF whether it is the reporting entity, or else name the reporting entity and its residence. The deadline is the last day of the group's reporting year, and no later than the deadline for the entity's tax return for the previous year (CPF annex 3, section II, pt. 7 and 8).
- **Time limit for adjustments.** ANAF can assess within 5 years. The period starts on 1 July of the year after the year the tax is due for (CPF art. 110(1) and (2)). It is 10 years where the tax results from a criminal offence (art. 110(3)).

## Penalties and interest

- **File not prepared or not presented** (CPF art. 336(1)(e) and (2)(c)). It is a contravention to breach the duty to prepare the file under the conditions and deadlines of the Order, or to fail to present it when ANAF asks under art. 108(2). The fine is:
  - RON 12,000 to 14,000 for legal persons that are medium or large taxpayers;
  - RON 2,000 to 3,500 for other legal persons and for individuals.
- **Estimation and extra tax.** On top of the fine, ANAF estimates the transfer prices at the median, or at the mean of at most three comparables (Order art. 7(4) and 9(2)). The extra profit is taxed at 16% (CF art. 17).
- **Interest and penalties on the extra tax** (CPF art. 174, 176, 181). The general rules are in ro-cross-border. In short:
  - interest of 0.02% a day from the day after the original due date;
  - a non-declaration penalty of 0.08% a day on tax assessed by ANAF. It falls by 75% if the assessed tax is paid or set off by the deadline in CPF art. 156(1), and it cannot exceed the tax it is charged on;
  - the 0.01% a day late payment penalty does not apply where the non-declaration penalty applies (art. 176(4)).
- **CbCR fines** (CPF art. 336(1)(u) and (v), (2)(l) and (m)):
  - late filing, or incorrect or incomplete information: RON 30,000 to 50,000;
  - not filing: RON 70,000 to 100,000.

## Cross-border points

- **Mutual agreement and arbitration** (ANAF transfer pricing guide, section 9). An upward adjustment in Romania can be taken to:
  - the mutual agreement procedure under a Romanian tax treaty;
  - the EU Arbitration Convention;
  - the EU Dispute Resolution Directive (2017/1852), transposed in CPF art. 283^1 onward.
  The negotiating mandate considers all the art. 11(4) methods and the OECD Guidelines (CPF art. 282(11)).
- **APAs** (CPF art. 52):
  - **Types.** An APA sets, for a fixed period, how transfer prices for transactions with affiliated persons will be set. It can also cover the profit attributable to a permanent establishment (art. 52(2)). It can be unilateral, bilateral or multilateral; bilateral and multilateral APAs are only for counterparties in treaty states (art. 52(15)).
  - **Rollback.** On request, an APA can be extended back to up to five closed fiscal years before the year of the request, where the past transactions were on similar terms (art. 52(2^1)).
  - **Fees.** EUR 20,000 for large taxpayers, or where the consolidated value of the covered transactions exceeds EUR 4,000,000 or the taxpayer becomes a large taxpayer during the APA; EUR 10,000 for others. A modification costs EUR 15,000 or EUR 6,000. The fees are paid at the NBR rate on the day of payment (art. 52(17)). The fee is refunded if ANAF rejects the request (art. 52(19)).
  - **Time to decide.** 12 months for a unilateral APA and 18 months for a bilateral or multilateral one (art. 52(12)).
  - **Binding effect.** The APA binds ANAF only while the taxpayer meets its terms (art. 52(11)). A taxpayer that disagrees with the APA issued can notify ANAF within 30 days, and the APA then has no effect (art. 52(9)).
  - **Changes.** A request to extend, widen or revise the APA must be filed at least 30 days before it expires (art. 52(14)).
  - **Length.** ANAF's guide says an APA runs for up to 5 years, longer for long-term contracts. The procedure is in ANAF Order 3735/2015 (guide, section 10).
- **CbCR** (CPF art. 291^3 and annex 3):
  - The report covers groups with consolidated revenue of at least EUR 750,000,000 in the year before the reporting year (annex 3, section I, pt. 4).
  - A Romanian entity that is not the ultimate parent files in Romania only in the fallback cases in annex 3, section II, pt. 1, for example where the parent's state does not require the report or does not exchange it.
  - The form is set by ANAF Order 3049/2017.
  - A receiving state cannot base a transfer pricing adjustment on CbCR data alone (CPF art. 299(7)).
- **Outbound payments.** Withholding on interest, royalties and service fees paid to affiliates abroad, and the company exit tax, are in ro-cross-border. The interest limitation rule (CF art. 40^2), including its EUR 500,000 ceiling for affiliated-party costs that do not fund assets, is in ro-corporate-income-tax.

## Worked examples

### Example 1: services charged below the interquartile range

A Romanian SRL, a medium taxpayer, provides software development services only to its German parent. In 2026 its operating costs are RON 10,000,000. It charges cost plus 2%. The services are well above EUR 50,000, so the SRL must prepare a file when ANAF asks in an inspection (Order art. 2(4)). It is not a large taxpayer, so there is no annual duty.

In the inspection, ANAF benchmarks the net cost plus markup of eight independent companies, sorted from low to high: 2%, 3%, 4%, 5%, 6%, 7%, 9%, 12%.

1. Split the eight results into 4 segments of two. Drop the bottom two (2%, 3%) and the top two (9%, 12%) as extreme results (Order art. 8 pt. 4).
2. Comparison interval: 4% to 7%.
3. The 2% markup is below 4%, so the price is not arm's length.
4. The interval has four values, so there is no single middle value. The median is the mean of the two middle values: (5% + 6%) / 2 = 5.5% (art. 8 pt. 6).
5. Arm's length charge: 10,000,000 x 1.055 = RON 10,550,000. Actual charge: 10,000,000 x 1.02 = RON 10,200,000.
6. Upward adjustment to income: RON 350,000.
7. Extra corporate income tax at 16%: RON 56,000. Interest and the non-declaration penalty run on it from the original due date (see Penalties and interest).
8. Relief in Germany is sought under the Romania-Germany treaty mutual agreement article or the EU Arbitration Convention.

```oa-check
name: RO SRL, services at cost plus 2% vs interquartile range 4%-7%, median 5.5%, costs RON 10m (2026)
inputs:
  costs: 10000000
  markup_charged: 0.02
  c3: 0.04
  c4: 0.05
  c5: 0.06
  c6: 0.07
  cit_rate: 0.16
steps:
  - range_low: c3
  - range_high: c6
  - median: (c4 + c5) / 2
  - arm_charge: costs * (1 + median)
  - actual_charge: costs * (1 + markup_charged)
  - adjustment: arm_charge - actual_charge
  - extra_tax: adjustment * cit_rate
expected:
  range_low: 0.04
  range_high: 0.07
  median: 0.055
  arm_charge: 10550000
  actual_charge: 10200000
  adjustment: 350000
  extra_tax: 56000
```

### Example 2: large taxpayer does not present the file, estimate from three comparables

A Romanian manufacturer is a large taxpayer. In 2026 it sells goods to an affiliated distributor abroad for RON 50,000,000, at an operating margin of 1% of sales. The sales are far above EUR 350,000, so the file had to be ready by 25 June 2027 (Order art. 2(1); CF art. 42(1)).

In an inspection in late 2027, ANAF asks for the file with 10 calendar days to present it (Order art. 4(1)). The company presents nothing. ANAF fines it at the minimum and estimates the price. It finds only three comparable companies, with operating margins of 3%, 4% and 5%. The company pays the extra tax, interest and penalty 365 days after the original due date, and within the payment deadline of the assessment (CPF art. 156(1)).

1. Fine: RON 12,000, the bottom of the RON 12,000 to 14,000 range for large taxpayers (CPF art. 336(2)(c)).
2. At most three comparables, so ANAF uses the arithmetic mean: (3% + 4% + 5%) / 3 = 4% (Order art. 9(2)).
3. Estimated arm's length profit: 50,000,000 x 4% = RON 2,000,000. Reported profit: 50,000,000 x 1% = RON 500,000.
4. Upward adjustment: RON 1,500,000. Extra corporate income tax at 16%: RON 240,000.
5. Interest: 240,000 x 0.02% x 365 = RON 17,520 (CPF art. 174(5)).
6. Non-declaration penalty, full: 240,000 x 0.08% x 365 = RON 70,080 (art. 181(1)). It is paid by the assessment deadline, so it falls by 75% to RON 17,520 (art. 181(2)). The 0.01% late payment penalty does not apply (art. 176(4)).
7. Total cost: 240,000 + 17,520 + 17,520 + 12,000 = RON 287,040.

```oa-check
name: RO large taxpayer, no TP file, mean of three comparables 4% vs 1%, sales RON 50m, paid after 365 days (2026)
inputs:
  sales: 50000000
  margin_reported: 0.01
  comp1: 0.03
  comp2: 0.04
  comp3: 0.05
  cit_rate: 0.16
  interest_rate_day: 0.0002
  nondecl_rate_day: 0.0008
  nondecl_reduction: 0.75
  days: 365
  fine: 12000
steps:
  - mean_margin: (comp1 + comp2 + comp3) / 3
  - arm_profit: sales * mean_margin
  - reported_profit: sales * margin_reported
  - adjustment: arm_profit - reported_profit
  - extra_tax: adjustment * cit_rate
  - interest: extra_tax * interest_rate_day * days
  - nondecl_full: extra_tax * nondecl_rate_day * days
  - nondecl_reduced: nondecl_full * (1 - nondecl_reduction)
  - total_cost: extra_tax + interest + nondecl_reduced + fine
expected:
  mean_margin: 0.04
  arm_profit: 2000000
  reported_profit: 500000
  adjustment: 1500000
  extra_tax: 240000
  interest: 17520
  nondecl_full: 70080
  nondecl_reduced: 17520
  total_cost: 287040
```

## Ask the client first

1. Is the company on ANAF's list of large taxpayers for 2026? Is it a medium or a small taxpayer? This sets the file duty and the fine band.
2. Who are its affiliated persons under the 25% or effective control test, counting indirect holdings and family members of individual owners?
3. What is the 2026 value of each transaction type with all affiliates together (interest, services, goods), excluding VAT, at the NBR rate on the last day of the year?
4. Does a file already exist? Which method and tested party does it use, and does it include a benchmark showing the full range and the comparables rejected?
5. Is there an APA with ANAF, or an earlier adjustment decision, that covers some of these transactions?
6. Is the group's consolidated revenue at least EUR 750 million, and has the Romanian entity sent its CbCR notification?

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code (Legea 227/2015), ANAF consolidated text, last update Legea 170/2026: art. 7 pt. 26 and 33, art. 11(4), art. 19(6), art. 17, art. 42, art. 42^6 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-10-23 |
| Fiscal Procedure Code (Legea 207/2015), ANAF consolidated text, last update Legea 170/2026: art. 52, 108(2), 110, 127, 156, 174, 176, 181, 282, 283, 291^3, 299, 336, annex 3 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-10-23 |
| ANAF President's Order 442/2016 (MO nr. 74 of 2 February 2016), ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_442_2016.pdf | 2026-10-23 |
| ANAF, Ghid al prețurilor de transfer (updated November 2025) | https://static.anaf.ro/static/10/Anaf/Prezentare_R/Ghid%20Preturi%20de%20Transfer%20(1).pdf | 2026-10-23 |

Not yet confirmed: (1) Whether Order 442/2016 has been amended since 2016. The Portal Legislativ record (https://legislatie.just.ro/Public/DetaliiDocument/175458) could not be loaded on 23 October 2026, so the consolidated text was not read. ANAF's copy is the 2016 text, and ANAF's November 2025 guide quotes the same thresholds and deadlines. The ANAF consolidated Procedure Code cites the order as "446/2016" in several places, which appears to be a typing error for 442/2016. (2) How the Order's "4 segments" split works when the number of comparables is not divisible by four. The Order gives no rule, and Example 1 uses eight comparables so the split is exact. (3) Whether a reduced fine for paying half the minimum within 15 days applies under the general contraventions law (OG 2/2001), which was not read. (4) The treatment of secondary adjustments, such as whether an excess paid to a foreign parent becomes a dividend, was not researched. (5) ANAF Order 3735/2015 (APA procedure) and Order 3049/2017 (CbCR form) were not read; the APA length of up to 5 years comes from ANAF's guide only. (6) Whether the CbCR report and notification for calendar 2026 move when a deadline falls on a non-working day was not checked.
