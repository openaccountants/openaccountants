---
name: ch-transfer-pricing
description: "Swiss transfer pricing for 2026. Switzerland has no transfer pricing statute: the arm's length principle works through profit tax (DBG art. 58 para. 1 let. b and c, StHG art. 24) and the 35% withholding tax on hidden profit distributions (geldwerte Leistungen, VStG art. 4 para. 1 let. b). Covers related parties, hidden profit distributions and hidden capital contributions, the ESTV safe-harbour interest rates for 2026 (CHF and foreign currency), service companies (Kreisschreiben 4), the burden of proof, rulings, APAs, MAP (StADG), country-by-country reporting (CHF 900 million), penalties, and the 35% withholding with the gross-up when it is not passed on. Trigger on: transfer pricing Switzerland, Verrechnungspreise, geldwerte Leistung, verdeckte Gewinnausschüttung, safe harbour Zinssätze, shareholder loan interest, CbCR Schweiz. Out of scope: ch-corporate-income-tax (rates, base), ch-cross-border (treaty refunds, migration), ch-cantonal-tax."
jurisdiction: CH
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Switzerland: transfer pricing (2026)

Switzerland has no transfer pricing law of its own. The ESTV says so itself: "Das schweizerische Steuerrecht sieht keine spezifische Gesetzgebung zu den Verrechnungspreisen vor" ([ESTV, Verrechnungspreise, January 2024](https://www.estv2.admin.ch/stp/ds/b-verrechnungspreise-de.pdf), section 2.2.2). Instead, a price between a company and its shareholder, or a person close to the shareholder, is tested under two taxes:

- **Profit tax.** A price that shifts profit to a shareholder or related party is a hidden profit distribution (verdeckte Gewinnausschüttung). It is added back to taxable profit under DBG art. 58 para. 1 let. b and c (federal) and StHG art. 24 para. 1 (cantons and communes). The cantons assess and adjust.
- **Withholding tax (Verrechnungssteuer).** The same benefit is a geldwerte Leistung, taxable income from shares under VStG art. 4 para. 1 let. b and VStV art. 20 para. 1. The ESTV charges 35%. This is the Swiss form of a secondary adjustment.

The OECD Transfer Pricing Guidelines are not law in Switzerland, but the ESTV and the courts use them to read the arm's length principle (ESTV publication, section 2.2.1; ESTV Kreisschreiben 4 of 19 March 2004).

Related skills, linked rather than repeated:

- Profit tax rates, the base and the participation deduction: `ch-corporate-income-tax`. Note that skill is still labelled tax year 2025 and cites secondary sources.
- Treaty refunds of the 35%, companies moving in or out, hidden reserves on exit: `ch-cross-border`.
- Cantonal and communal tax: `ch-cantonal-tax`.
- Functional analysis, method choice and benchmarking in general: `transfer-pricing-workflow-base` (foundation).

## Who this applies to

- **Swiss companies and cooperatives** (AG, GmbH, cooperative) that deal with their shareholders or with persons close to them. Size does not matter: a one-person GmbH that lends to its owner is in scope as much as a group subsidiary.
- **Related party.** Swiss domestic law does not use the treaty term "associated enterprise". It uses "shareholder" and "close person" (nahestehende Person). The Federal Supreme Court defines a close person as one with close personal ties to the shareholder or the company's officers, for example family or friendship (BGer 2C_177/2016 of 30 January 2017, E. 4.3, cited in the ESTV publication, footnote 6). Sister companies are close persons.
- **Both directions.** A Swiss company that pays too much to, or charges too little to, its shareholder or a close person makes a hidden profit distribution. A Swiss parent that pays too much to, or charges too little to, its foreign subsidiary makes a hidden capital contribution (verdeckte Kapitaleinlage); the parent's profit is corrected as an unjustified write-down (ESTV publication, section 2.3.1).
- **Swiss branches of foreign companies** are taxed on profit attributed to the branch; branch attribution is not covered here.
- **Groups with a Swiss ultimate parent** and consolidated revenue above CHF 900 million file a country-by-country report (ALBAG art. 6; ALBAV art. 3).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Federal profit tax | 8.5% of net profit (taxes are deductible, so about 7.83% of profit before tax) | 2026 | [DBG art. 68, 59](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Withholding tax on a hidden profit distribution (geldwerte Leistung) | 35% of the benefit | 2026 | [VStG art. 4, 13](https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de) |
| Withholding tax if the company does not recover it from the recipient (gross-up "ins Hundert") | 35/65 of the net benefit, about 53.85% | 2026 | [VStG art. 14](https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de); BVGer A-2782/2022 E. 4.4.2 |
| Safe-harbour minimum interest: CHF loan to a shareholder or close person, financed from equity, no interest-bearing debt | 0.75% | 2026 | [ESTV circular 2-218 of 29 Jan 2026](https://www.estv.admin.ch/dam/de/sd-web/xY4pH-Qc2lrL/2-218-DV-2026-d.pdf) |
| Safe-harbour minimum interest: CHF loan to a shareholder, financed with debt | Own cost of debt plus 0.5% (up to CHF 10 million) or 0.25% (above CHF 10 million), at least 0.75% | 2026 | [ESTV circular 2-218](https://www.estv.admin.ch/dam/de/sd-web/xY4pH-Qc2lrL/2-218-DV-2026-d.pdf) |
| Safe-harbour maximum interest: CHF operating loan from a shareholder, up to CHF 1 million | 3.5% (trading and manufacturing); 3% (holding and asset management) | 2026 | [ESTV circular 2-218](https://www.estv.admin.ch/dam/de/sd-web/xY4pH-Qc2lrL/2-218-DV-2026-d.pdf) |
| Safe-harbour maximum interest: CHF operating loan from a shareholder, from CHF 1 million | 1.5% (trading and manufacturing); 1.25% (holding and asset management) | 2026 | [ESTV circular 2-218](https://www.estv.admin.ch/dam/de/sd-web/xY4pH-Qc2lrL/2-218-DV-2026-d.pdf) |
| Safe-harbour maximum interest: CHF real estate loan from a shareholder, up to the first mortgage (2/3 of market value) | 1.25% (residential and agricultural); 1.75% (industrial and commercial) | 2026 | [ESTV circular 2-218](https://www.estv.admin.ch/dam/de/sd-web/xY4pH-Qc2lrL/2-218-DV-2026-d.pdf) |
| Safe-harbour maximum interest: CHF real estate loan, the rest | 2% (residential and agricultural); 2.5% (industrial and commercial) | 2026 | [ESTV circular 2-218](https://www.estv.admin.ch/dam/de/sd-web/xY4pH-Qc2lrL/2-218-DV-2026-d.pdf) |
| Safe-harbour interest: foreign-currency loans, examples | EUR 2.50%, USD 4.00%, GBP 4.00%, JPY 2.00%, CAD 3.25%, CNY 2.25%, SEK 2.75%, NOK 4.50%, DKK 3.25%, PLN 4.25% | 2026 | [ESTV circular 2-219 of 30 Jan 2026](https://www.estv.admin.ch/dam/de/sd-web/04KIslBDT-PZ/2-219-DV-2026-d.pdf) |
| Foreign-currency loan to a shareholder at a rate below the CHF rate | At least the CHF rate (0.75%) | 2026 | [ESTV circular 2-219](https://www.estv.admin.ch/dam/de/sd-web/04KIslBDT-PZ/2-219-DV-2026-d.pdf) |
| Foreign-currency operating loan from a shareholder: spread allowed on top of the table rate | Up to CHF 1 million equivalent: 2.75% (trading and manufacturing), 2.25% (holding); from CHF 1 million: 0.75% and 0.50% | 2026 | [ESTV circular 2-219](https://www.estv.admin.ch/dam/de/sd-web/04KIslBDT-PZ/2-219-DV-2026-d.pdf) |
| Country-by-country report threshold (consolidated revenue of the prior period) | Above CHF 900 million | 2026 | [ALBAV art. 3](https://www.fedlex.admin.ch/eli/cc/2017/646/de); [ALBAG art. 6](https://www.fedlex.admin.ch/eli/cc/2017/645/de) |
| Late payment interest on withholding tax and federal taxes | 4.0% | 2026 | [ESTV](https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI) |
| Participation reduction on profit tax | Holding of at least 10%, or a value of at least CHF 1 million | 2026 | [DBG art. 69](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Shareholder (individual, Swiss resident) taxed on a hidden distribution, federal | 70% of the benefit if the holding is at least 10% | 2026 | [DBG art. 20 para. 1 let. c and para. 1bis](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |

The interest rates are ESTV administrative practice, not law. The ESTV calls them a "safe haven": if you stay inside them, the rate is accepted without a comparison. A rate outside them raises a rebuttable presumption that the price is not at arm's length; the company may always prove that it is (circular 2-218; ESTV publication, section 2.2.2). The rates apply both to the ESTV (withholding tax) and to federal profit tax (circular 2-218, first paragraph). For loans from shareholders, the maximum allowable interest also depends on hidden equity under DBG art. 65 and [ESTV Kreisschreiben 6a of 10 October 2024](https://www.estv.admin.ch/dam/de/sd-web/37U14bg5Pqqj/dbst-ks-2024-006a-dvs-de.pdf). Interest on the part of debt treated as equity is added back to profit.

## The taxable base

**The rule in the law.** Taxable net profit includes (DBG art. 58 para. 1):

- **let. b:** amounts taken out of the result that do not cover business-justified expense, expressly including "offene und verdeckte Gewinnausschüttungen und geschäftsmässig nicht begründete Zuwendungen an Dritte" (open and hidden profit distributions, and gifts to third parties without business reason). This catches overpayments: excessive rent, salary, royalty or interest paid to a shareholder or close person.
- **let. c:** income not credited to the income statement. This catches underpayments: income the company gave up, such as interest not charged on a shareholder loan or a service charged below market.

StHG art. 24 para. 1 sets the same rule for cantonal and communal profit tax.

**When a benefit is a geldwerte Leistung.** The courts apply four conditions, and the tax authority bears the burden of proof for each (BVGer A-2977/2025 of 2 March 2026, E. 2.2 and 2.3):

1. the company makes a benefit without an equal counter-performance;
2. the benefit goes directly or indirectly to a shareholder or a close person;
3. it would not have been given to an unrelated third party on the same terms, so its reason lies in the shareholding;
4. the mismatch was recognisable to the company's officers. Where the mismatch is obvious, this is presumed, and the company must disprove it.

**Burden of proof and documentation.** Switzerland has no master file or local file requirement. The only formal transfer pricing document in law is the country-by-country report (ESTV publication, section 6). But the company must do everything needed for a complete and correct assessment and produce books and documents on request (DBG art. 126 para. 1 and 2; VStG art. 39), and keep business records for ten years (DBG art. 126 para. 3). The tax authority must prove a hidden distribution; once it shows an obvious mismatch, the company must rebut it. In practice, a Swiss company that cannot show how a price was set loses that argument. Under Kreisschreiben 4, a service company that thinks the margin applied to it is too high must prove it with documentation.

**Interest on shareholder loans.** An interest-free or under-priced loan to a shareholder or close person is a geldwerte Leistung, and so is excessive interest paid on a loan from one (circulars 2-218 and 2-219, first paragraph). The shortfall against the safe-harbour rate is added to profit and bears 35% withholding tax. A loan to a shareholder that will not be repaid can itself be a hidden distribution of the whole principal; that test is not covered here.

**Service companies (Kreisschreiben 4 of 19 March 2004).** The ESTV told the cantons that the margin of a service company must follow the arm's length principle, case by case, based on comparable uncontrolled transactions and a range of appropriate margins. Cost plus is "not, or only in rare exceptional cases" suitable for financial services or management functions. Kreisschreiben 4 does **not** set a percentage: it replaced a 1997 circular and states no fixed margin ([KS 4](https://www.estv.admin.ch/dam/de/sd-web/uTu5sU-zws3F/dbst-ks-2004-1-004-dv-de.pdf)). The ESTV's own publication points to the OECD simplified approach for low value-adding intra-group services: a 5% mark-up on cost without a benchmarking study (OECD Guidelines para. 7.61, cited in ESTV publication, section 5.3). Use 5% as the OECD figure for low value-adding support services only, not as a Swiss statutory rate.

**What happens on adjustment (ESTV publication, sections 7.3 and 7.4).**

- **Primary adjustment:** the canton adds the excess or shortfall to taxable profit. Only the cantons make primary adjustments.
- **Secondary adjustment:** the ESTV charges 35% withholding tax on the same amount as a geldwerte Leistung. The ESTV can do this whether or not the canton adjusted profit, and the reverse is also true.
- **Corresponding adjustment:** if a foreign state adjusts and Switzerland agrees, usually through a mutual agreement procedure, the canton reduces Swiss profit.

**The 35% and the gross-up.** The company owes the withholding tax (VStG art. 10) and must deduct it from the benefit, whatever any agreement says (VStG art. 14 para. 1). Where the benefit has already flowed, the company must recover the tax from the recipient. If it does not, the ESTV treats what was paid as a net amount and grosses it up "ins Hundert": the gross benefit is the amount that, less 35%, equals what the recipient actually got. So the tax is benefit x 35/65 (BVGer A-2782/2022 of 30 April 2024, E. 4.4.2, applied in E. 7.3.2 as "571'582.26 : 65 x 100"; BVGer A-3092/2023 of 21 March 2025, E. 2.2.2). The tax paid on the gross-up is a further use of profit, not a refundable withholding.

**Notification instead of payment.** Where the ESTV finds a benefit in an audit that fell due in a prior year, the company may ask to meet its duty by notification rather than payment, if every recipient would be entitled to a refund and there are no more than 20 (VStV art. 24 para. 1 let. a and para. 2). A Swiss resident shareholder who failed to declare the income may lose that refund entitlement and with it the notification route (VStG art. 23; BVGer A-2977/2025, E. 2.5).

**At the shareholder.** A Swiss resident individual is taxed on the hidden distribution as income from shares (DBG art. 20 para. 1 let. c), at 70% for federal tax if the holding is at least 10% (DBG art. 20 para. 1bis). A Swiss company shareholder may get the participation reduction (DBG art. 69 and 70). The shareholder reclaims the 35% through the tax return if they are Swiss resident and declare it (VStG art. 22 and 23).

**Hidden capital contributions.** A contribution by a shareholder to its company, including a benefit given below market, is not taxable profit of the receiving company (DBG art. 60 let. a; StHG art. 24 para. 2 let. a). At the Swiss parent that gives the benefit, the amount is added back as a non-deductible write-down (ESTV publication, section 2.3.1).

## Deadlines and filing

- **Profit tax.** No separate transfer pricing return. Prices are part of the company's annual return to its canton; deadlines are cantonal (see `ch-corporate-income-tax` and `ch-cantonal-tax`).
- **Withholding tax on a geldwerte Leistung.** The claim arises when the benefit falls due (VStG art. 12 para. 1). The company must declare it on **form 102** without being asked, and pay, within **30 days** after it falls due (VStG art. 16 para. 1 let. c and art. 38 para. 2; circular 2-218, first paragraph). Interest at 4.0% runs without reminder after that (VStG art. 16 para. 2; ESTV 2026 rate).
- **Country-by-country report.** The reporting entity registers with the ESTV no later than **90 days** after the end of the reporting fiscal year (ALBAG art. 10 para. 4) and files the report no later than **12 months** after the end of the reporting fiscal year (ALBAG art. 11 para. 1).
- **Rulings.** Profit tax rulings are given by the canton; withholding tax rulings by the ESTV. The ESTV recommends filing with both at the same time and enclosing evidence such as a transfer pricing study (ESTV publication, section 7.2.1). ESTV transfer pricing rulings: ruling.dvs@estv.admin.ch ([ESTV transfer pricing page](https://www.estv.admin.ch/de/allgemeines-verrechnungspreise)).
- **APAs.** Bilateral or multilateral advance pricing agreements are negotiated by the State Secretariat for International Finance (SIF). The request is made on a form (ESTV publication, section 7.2.2 and footnote 63).
- **Mutual agreement procedure (MAP).** Filed with the SIF, in an official language or in English, with the requests, reasons and evidence (StADG art. 3 and 5). The time limit for a request comes from the applicable treaty. No costs are charged for opening or conducting the procedure (StADG art. 8 and 17). An agreement binds Switzerland only once the taxpayer consents, and consent waives all appeals on the same matter (StADG art. 15).
- **Time limits for the authorities.** The right to assess profit tax lapses five years after the end of the tax period (DBG art. 120), extended to ten years for a supplementary assessment where facts were unknown (DBG art. 151 and 152). The withholding tax claim lapses five years after the end of the calendar year in which it arose (VStG art. 17), interrupted by any official act.

## Penalties and interest

- **Profit tax evasion:** a fine normally equal to the tax evaded, reduced to one third for slight fault or increased to three times for serious fault (DBG art. 175 para. 2). A legal person is fined directly (DBG art. 181). The evaded tax is collected with interest as a supplementary tax (DBG art. 151).
- **Procedural failures** (not filing, not answering after a reminder): fine up to CHF 1,000, or up to CHF 10,000 in serious or repeat cases (DBG art. 174).
- **Withholding tax evasion:** fine up to CHF 30,000, or up to three times the tax evaded if that is higher (VStG art. 61). This also covers failing to notify a benefit or making a false notification.
- **Late payment interest on withholding tax:** 4.0% for 2026 (VStG art. 16 para. 2; [ESTV](https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI)).
- **Gross-up:** if the company does not recover the 35% from the recipient, the tax rises to 35/65 of the benefit (see the base).
- **Country-by-country report filed late:** CHF 200 a day, up to CHF 50,000 (ALBAG art. 12). Intentionally false or incomplete information: fine up to CHF 100,000 (ALBAG art. 25). Ignoring an ESTV order in a review: up to CHF 10,000 (ALBAG art. 26).
- **MAP interest:** a taxpayer who caused the treaty-breaching taxation intentionally or without due care, or neglected the available procedures, gets no refund interest (StADG art. 22).

Cantonal profit tax penalties follow cantonal law and are broadly parallel.

## Cross-border points

- **The 35% hits foreign parents too.** A hidden distribution to a foreign parent or sister company bears 35% withholding tax like any dividend. The foreign recipient reclaims under the applicable treaty. Refund procedure and example treaty rates: `ch-cross-border`.
- **Secondary adjustment after a MAP.** The ESTV and the SIF have a practice where the MAP agreement can provide that withholding tax is charged on the confirmed primary adjustment only if the foreign company does not pay the amount back to the Swiss company (ESTV publication, section 7.4).
- **Treaty basis.** The arm's length rule between states comes from the treaty article modelled on OECD Model art. 9. The ESTV applies the version of the OECD Guidelines in force when the tax claim arose ([ESTV transfer pricing page](https://www.estv.admin.ch/de/allgemeines-verrechnungspreise)).
- **Pillar Two.** Large groups (revenue of EUR 750 million or more) also face the Swiss minimum tax; see `ch-corporate-income-tax`. Not covered here.
- **Moving functions or assets abroad** triggers tax on hidden reserves (DBG art. 61b): `ch-cross-border`.

## Worked examples

### Example 1: interest-free loan from a company to its shareholder (2026)

Facts: Alpha GmbH, Zurich, lends CHF 500,000 to its sole shareholder, a Swiss resident individual, on 1 January 2026. No interest is charged all year. Alpha has no interest-bearing debt, so the loan is financed from equity. The 2026 safe-harbour minimum is 0.75% (circular 2-218, item 1.1).

- Deemed interest: 500,000 x 0.75% = CHF 3,750. This is income Alpha gave up (DBG art. 58 para. 1 let. c) and a geldwerte Leistung (VStG art. 4 para. 1 let. b).
- Federal profit tax: Alpha's taxable profit rises by CHF 3,750. Federal tax is 8.5% of net profit after tax, so on profit before tax it is 8.5/108.5. The federal tax on the adjustment is CHF 293.78. Cantonal and communal tax comes on top, and because those taxes are also deductible the federal figure falls slightly; use the canton's calculator.
- Withholding tax, recovered from the shareholder: 35% x 3,750 = CHF 1,312.50, declared on form 102 and paid within 30 days after the benefit falls due. The shareholder, being Swiss resident, reclaims it by declaring the income.
- Withholding tax, not recovered: the benefit is grossed up to 3,750 / 0.65 = CHF 5,769.23, and the tax is CHF 2,019.23. Not passing the tax on costs Alpha CHF 706.73 more, and it is not refundable.

```oa-check
name: Interest-free shareholder loan, CHF 500,000, 2026 safe harbour 0.75%
inputs:
  loan: 500000
  safe_harbour_rate: 0.75
  federal_rate: 8.5
  vst_rate: 35
steps:
  - deemed_interest: pct(loan, safe_harbour_rate)
  - federal_profit_tax: round(deemed_interest * federal_rate / (100 + federal_rate), 2)
  - vst_recovered: pct(deemed_interest, vst_rate)
  - grossed_up_benefit: round(deemed_interest / (1 - vst_rate / 100), 2)
  - vst_not_recovered: round(grossed_up_benefit * vst_rate / 100, 2)
  - extra_cost_of_not_recovering: vst_not_recovered - vst_recovered
expected:
  deemed_interest: 3750.00
  federal_profit_tax: 293.78
  vst_recovered: 1312.50
  grossed_up_benefit: 5769.23
  vst_not_recovered: 2019.23
  extra_cost_of_not_recovering: 706.73
```

The edge case: if Alpha had a bank loan, the minimum rate would be its own interest cost plus 0.5%, never less than 0.75% (circular 2-218, item 1.2). At the shareholder, the CHF 3,750 is taxable income from shares, at 70% for federal tax since the holding is over 10% (DBG art. 20 para. 1bis).

### Example 2: service company charging below an arm's length mark-up (2026)

Facts: Beta AG, Swiss, is owned 100% by a German parent and has held that status for years. Beta provides accounting and HR support to the parent. Its 2026 costs for these services are CHF 2,000,000 and it charges cost plus 2%, CHF 2,040,000. The services are support functions with no unique intangibles and no significant risk, which fits the OECD definition of low value-adding services, for which the OECD allows a 5% mark-up without a benchmarking study (ESTV publication, section 5.3; OECD Guidelines para. 7.61). Beta has no study showing that 2% is at arm's length. Kreisschreiben 4 puts the burden on the company to document a lower margin. The canton adjusts to cost plus 5%.

- Arm's length charge: 2,000,000 x 1.05 = CHF 2,100,000. Shortfall: CHF 60,000, a hidden profit distribution to the parent (DBG art. 58 para. 1 let. c).
- Federal profit tax on the adjustment: 60,000 x 8.5 / 108.5 = CHF 4,700.46.
- Withholding tax (secondary adjustment by the ESTV): 35% x 60,000 = CHF 21,000, if recovered from the parent. If not recovered, the benefit is grossed up to CHF 92,307.69 and the tax is CHF 32,307.69.

```oa-check
name: Service company at cost plus 2%, adjusted to cost plus 5% (2026)
inputs:
  service_costs: 2000000
  markup_charged: 2
  markup_arms_length: 5
  federal_rate: 8.5
  vst_rate: 35
steps:
  - charged: service_costs + pct(service_costs, markup_charged)
  - arms_length_charge: service_costs + pct(service_costs, markup_arms_length)
  - adjustment: arms_length_charge - charged
  - federal_profit_tax: round(adjustment * federal_rate / (100 + federal_rate), 2)
  - vst_recovered: pct(adjustment, vst_rate)
  - grossed_up_benefit: round(adjustment / (1 - vst_rate / 100), 2)
  - vst_not_recovered: round(grossed_up_benefit * vst_rate / 100, 2)
expected:
  charged: 2040000.00
  arms_length_charge: 2100000.00
  adjustment: 60000.00
  federal_profit_tax: 4700.46
  vst_recovered: 21000.00
  grossed_up_benefit: 92307.69
  vst_not_recovered: 32307.69
```

The edge cases: the canton, not Beta, must first show the mismatch, and in BVGer A-2782/2022 (E. 6.2.3, pointing to E. 4.9.1) the court held that the ESTV bears the burden of proof for a geldwerte Leistung including a 5% cost mark-up it had added. A study placing 2% inside an arm's length range would defeat the adjustment. If the services were management or financial functions, Kreisschreiben 4 says cost plus is rarely the right method at all. The German parent then seeks a refund of the 35% under the treaty (`ch-cross-border`); Germany may also be asked, through a MAP, to make a corresponding adjustment.

## Ask the client first

1. Who are the counterparties? Shareholder, family member of a shareholder, sister company, foreign parent or subsidiary, and what holding percentage.
2. For each loan to or from a shareholder or close person: amount, currency, interest rate, start date, and whether the company itself has interest-bearing debt.
3. For services, goods or licences with related parties: what is charged, on what cost base, and is there any study or comparable data behind the price?
4. Has the withholding tax on any past benefit been declared on form 102, and was it recovered from the recipient?
5. Group consolidated revenue in the prior year, and where the ultimate parent sits (CbC report).
6. Is there an existing cantonal or ESTV ruling, APA, or open audit or MAP?

## Sources

| Source | URL | Read on |
|---|---|---|
| DBG, SR 642.11, version in force 2 September 2026, art. 20, 58, 59, 60, 65, 68, 69, 120, 126, 151, 152, 174, 175, 181 | https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de | 2026-10-23 |
| StHG, SR 642.14, version of 1 January 2025, art. 24 | https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/de | 2026-10-23 |
| VStG, SR 642.21, version of 1 January 2025, art. 4, 10, 12, 13, 14, 16, 17, 20, 22, 23, 38, 39, 61 | https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de | 2026-10-23 |
| VStV, SR 642.211, version of 1 January 2025, art. 20, 24 | https://www.fedlex.admin.ch/eli/cc/1966/1585_1641_1624/de | 2026-10-23 |
| ALBAG (CbC law), SR 654.1, version of 1 January 2022, art. 6, 10, 11, 12, 25, 26 | https://www.fedlex.admin.ch/eli/cc/2017/645/de | 2026-10-23 |
| ALBAV (CbC ordinance), SR 654.11, version of 1 November 2024, art. 3 | https://www.fedlex.admin.ch/eli/cc/2017/646/de | 2026-10-23 |
| StADG, SR 672.2, version of 1 January 2026, art. 3, 5, 8, 15, 17, 22 | https://www.fedlex.admin.ch/eli/cc/2021/703/de | 2026-10-23 |
| ESTV circular 2-218-DV-2026, steuerlich anerkannte Zinssätze 2026 in Schweizer Franken, 29 January 2026 | https://www.estv.admin.ch/dam/de/sd-web/xY4pH-Qc2lrL/2-218-DV-2026-d.pdf | 2026-10-23 |
| ESTV circular 2-219-DV-2026, steuerlich anerkannte Zinssätze 2026 in Fremdwährungen, 30 January 2026 | https://www.estv.admin.ch/dam/de/sd-web/04KIslBDT-PZ/2-219-DV-2026-d.pdf | 2026-10-23 |
| ESTV Kreisschreiben Nr. 4, Besteuerung von Dienstleistungsgesellschaften, 19 March 2004 | https://www.estv.admin.ch/dam/de/sd-web/uTu5sU-zws3F/dbst-ks-2004-1-004-dv-de.pdf | 2026-10-23 |
| ESTV Kreisschreiben Nr. 6a, verdecktes Eigenkapital, 10 October 2024 | https://www.estv.admin.ch/dam/de/sd-web/37U14bg5Pqqj/dbst-ks-2024-006a-dvs-de.pdf | 2026-10-23 |
| ESTV Steuerdokumentation, Verrechnungspreise (law as at 1 January 2024) | https://www.estv2.admin.ch/stp/ds/b-verrechnungspreise-de.pdf | 2026-10-23 |
| ESTV, Allgemeines zu den Verrechnungspreisen | https://www.estv.admin.ch/de/allgemeines-verrechnungspreise | 2026-10-23 |
| ESTV, Verzugs- und Vergütungszinssätze ab 2026 | https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI | 2026-10-23 |
| Bundesverwaltungsgericht A-2977/2025, 2 March 2026 (conditions and burden of proof, notification procedure) | https://bvger.weblaw.ch/pdf/A-2977-2025_2026-03-02_4b9bf11e-e7ff-4e3b-9a3b-02f4c90c0c5f.pdf | 2026-10-23 |
| Bundesverwaltungsgericht A-2782/2022, 30 April 2024 (gross-up, 5% cost mark-up, burden), copy on entscheidsuche.ch | https://entscheidsuche.ch/docs/CH_BVGer/CH_BVGE_001_A-2782-2022_2024-04-30.pdf | 2026-10-23 |
| Bundesverwaltungsgericht A-3092/2023, 21 March 2025 (gross-up "ins Hundert"), copy on entscheidsuche.ch | https://entscheidsuche.ch/docs/CH_BVGer/CH_BVGE_001_A-3092-2023_2025-03-21.pdf | 2026-10-23 |

Not yet confirmed: the Zurich cantonal and communal profit tax rate for 2026 (no single official 2026 figure found, so the examples stop at federal tax); whether the "from CHF 1 million" safe-harbour rate for operating loans applies to the whole loan or only to the part above CHF 1 million (the circular does not say); the treaty time limits for a MAP request (they differ by treaty); the conditions of the cross-border notification procedure for hidden distributions to foreign group companies (VStG art. 20 para. 2 allows it, the implementing rules were not read); whether each treaty treats a hidden distribution as a dividend for the refund; the official Federal Administrative Court copies of A-2782/2022 and A-3092/2023 (read on the entscheidsuche.ch archive); the circular 2-219 refers to the CHF circular as both 28 and 29 January 2026 (the CHF circular itself is dated 29 January 2026).
