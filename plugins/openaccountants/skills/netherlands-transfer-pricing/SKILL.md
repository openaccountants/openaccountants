---
name: netherlands-transfer-pricing
description: "Use this skill whenever asked about Netherlands transfer pricing rules, documentation requirements, or verrekenprijzen compliance. Trigger on phrases like \"transfer pricing Netherlands\", \"Dutch TP documentation\", \"verrekenprijzen\", \"master file Netherlands\", \"local file Netherlands\", \"CbCR Netherlands\", \"APA Netherlands\", \"Article 8b DCITA\", \"DTA transfer pricing\", \"CbC fine Netherlands\", \"missing transfer pricing documentation Netherlands\", \"verrekenprijzen boete\", or any question about intercompany pricing for Dutch entities."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/netherlands-transfer-pricing"
  jurisdiction: "NL"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Netherlands transfer pricing: pricing, documentation and reporting, 2026 v1.2

Tax year 2026. The law was read as in force on 23 October 2026; the articles used were unchanged from their 1 January 2026 text. This skill covers Dutch corporate transfer pricing (verrekenprijzen): the arm's length rule, the mismatch rules, documentation, country-by-country (CbC) reporting, advance certainty, and what happens when any of it is missing. It does not produce a market price without transaction evidence. Corporate tax computation itself is in `nl-corporate-tax`.

## Who this applies to

- **Related bodies.** Article 8b applies where one body takes part, directly or indirectly, in the management, supervision or capital of another, or the same person takes part in both. Profit is set as if arm's length terms had been agreed. Domestic as well as cross-border dealings are in scope. [Wet Vpb art. 8b(1)-(2)](https://wetten.overheid.nl/BWBR0002672).
- **Every such body keeps article 8b records.** There is no turnover floor. [Wet Vpb art. 8b(3)](https://wetten.overheid.nl/BWBR0002672).
- **Master file and local file.** A Dutch-taxable group entity of a multinational group with consolidated group revenue of at least EUR 50,000,000 in the reporting year before the return year. [Wet Vpb art. 29g(4)](https://wetten.overheid.nl/BWBR0002672).
- **CbC report.** A multinational group with at least EUR 750,000,000 consolidated revenue in the preceding reporting year. A Dutch ultimate parent reports. A Dutch non-parent reports only where the parent has no filing duty, there is no exchange agreement in force, or the inspector has notified a systematic failure, unless a surrogate parent files. [Wet Vpb art. 29b-29c](https://wetten.overheid.nl/BWBR0002672).
- **CbC notification.** Every Dutch-resident group entity of an in-scope group. [Wet Vpb art. 29d](https://wetten.overheid.nl/BWBR0002672).
- **Out:** unrelated parties; minimum tax, interest limits, innovation box, withholding tax, fiscal unity, VAT and customs, which use the same facts but need their own skills.

## Rates, bands and thresholds

| Item | Amount | Tax year | Source URL |
|---|---|---|---|
| Master and local file threshold (preceding reporting year group revenue) | at least EUR 50,000,000 | 2026 | https://wetten.overheid.nl/BWBR0002672 (art. 29g(4)) |
| Confidential CbC report threshold (preceding reporting year group revenue) | at least EUR 750,000,000 | 2026 | https://wetten.overheid.nl/BWBR0002672 (art. 29c(5)) |
| Public CbC report threshold (Dutch ultimate parent or standalone company) | more than EUR 750,000,000 on two consecutive balance-sheet dates | financial years from 22 June 2024 | https://wetten.overheid.nl/BWBR0049420 (art. 2) |
| Low-value intra-group services, optional markup | 5% of the relevant costs | 2026 | https://www.officielebekendmakingen.nl/stcrt-2022-16685.html (section 6.3) |
| Corporate tax rate, taxable amount up to EUR 200,000 | 19% | 2026 | https://wetten.overheid.nl/BWBR0002672 (art. 22) |
| Corporate tax rate, above EUR 200,000 | 25.8% | 2026 | https://wetten.overheid.nl/BWBR0002672 (art. 22) |
| CbC fine (vergrijpboete), maximum | sixth category: EUR 1,100,000 | from 1 Jan 2026 | https://wetten.overheid.nl/BWBR0002672 (art. 29h(1)); https://zoek.officielebekendmakingen.nl/stb-2025-401.html |
| Criminal fine, third category (AWR art. 68) | EUR 11,000 | from 1 Jan 2026 | https://zoek.officielebekendmakingen.nl/stb-2025-401.html |
| Criminal fine, fourth category (AWR art. 69(1)) | EUR 27,500 | from 1 Jan 2026 | https://zoek.officielebekendmakingen.nl/stb-2025-401.html |
| Criminal fine, fifth category (next category up for a company, Sr art. 23(7)) | EUR 110,000 | from 1 Jan 2026 | https://zoek.officielebekendmakingen.nl/stb-2025-401.html |
| Vergrijpboete on too little corporate tax, legal maximum | 100% of the tax not levied | 2026 | https://wetten.overheid.nl/BWBR0002320 (art. 67d, 67e) |
| Vergrijpboete, policy rate | 25% gross negligence, 50% intent | 2026 | https://wetten.overheid.nl/BWBR0038145 (§ 25(2)-(3)) |
| Tax interest (belastingrente) on corporate tax | 5% | from 1 Jan 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente |

Revenue thresholds are tested on the preceding reporting year. A lower current-year revenue does not undo them.

## The taxable base

**1. Delineate the actual transaction.** Describe contract terms, functions, assets and risks, the goods or services, economic circumstances and business strategy. Compare the contract with actual conduct. A risk return goes to the party that controls the risk and can bear it, not to the party the contract names. An IP return does not follow legal ownership alone. [2022 TP decree, sections 2 and 5](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).

**2. Choose a method and support it.** The recognised methods are CUP, resale price, cost plus, TNMM and profit split. The decree requires a justified method that gives an arm's length result. It does not require testing every method. Reconcile the tested figures to the accounts. Do not pick a margin to reach a preferred Dutch result. [Decree sections 2-3](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html); [OECD Guidelines 2022, chapter II](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf).

**3. Specific transactions.**
- Services: show a benefit to the recipient and strip out shareholder costs and duplication. Low-value supportive services that meet the decree's conditions can be charged at cost plus 5% with a simplified benefit test and no benchmark. Core activities (manufacturing, valuable product development, sales, financing) do not qualify, however small the invoice. [Decree section 6.3](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).
- Loans: establish that it is debt, then price it on credit risk, terms and both parties' options. There is no fixed Dutch interest rate. Guarantees and cash pools need their own analysis. [Decree section 9](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).
- IP transfers and restructurings: valuation and functional analysis, not a routine markup. [Decree section 5](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).

**4. Mismatch rules: a Dutch benefit needs foreign inclusion.**
- Article 8bb: a downward adjustment (higher costs or lower income than agreed) is allowed only to the extent the taxpayer makes plausible that the related body includes a corresponding upward adjustment in a profit tax.
- Article 8bc: on acquiring a non-debt asset from a related body, a step-up from the agreed price to the arm's length price counts only to the extent the seller includes the higher price in a profit tax. Acquired debts have a parallel rule.
- Article 8bd: on a non-debt asset received by capital contribution, distribution, capital repayment or liquidation, the Dutch starting value is the value the transferor included in a profit tax, if fair market value is higher.
Keep the agreed amount, the arm's length amount and the foreign inclusion evidence separately. Refer transparent entities, debts, mergers and old-year transitions. [Wet Vpb art. 8ba-8bd](https://wetten.overheid.nl/BWBR0002672).

**5. Documentation content.**
- Article 8b records: the five comparability factors, why the method was chosen, and how the price and terms were set. This covers domestic and cross-border transactions. Meeting the article 29g content also meets article 8b(3) for cross-border transactions. Below EUR 50,000,000 keep proportionate article 8b support; a missing database study does not by itself make it inadequate, and a copied group study is not enough unless the Dutch facts fit. [Decree section 10.2](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).
- Master file: the group's business, overall TP policy, and global allocation of income and activity. Local file: the Dutch entity's transactions with foreign group entities, the analysis supporting article 8b, and permanent establishment profit allocation. Dutch or English. Use the model items in the ministerial regulation, annexes C-F. [Wet Vpb art. 29g(1)-(3)](https://wetten.overheid.nl/BWBR0002672); [Regeling aanvullende documentatieverplichtingen verrekenprijzen](https://wetten.overheid.nl/BWBR0037475).
- Benchmarks: no automatic Dutch three-year safe harbour. OECD paragraph 5.38 allows a search refresh every three years if operating conditions are unchanged, with financial data updated each year. A changed function or risk profile needs a new analysis now. [OECD Guidelines 2022, paragraphs 5.37-5.38](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf).

The CbC report is a risk-assessment tool. The inspector may not base a transfer pricing adjustment on it. [Wet Vpb art. 29f](https://wetten.overheid.nl/BWBR0002672).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Article 8b records | Part of the administration throughout; no grace period in the law | [Wet Vpb art. 8b(3)](https://wetten.overheid.nl/BWBR0002672) |
| Master and local file | In the administration by the corporate return deadline for that year | [Wet Vpb art. 29g(1)](https://wetten.overheid.nl/BWBR0002672) |
| CbC notification (who reports, and where) | By the last day of the group's reporting year | [Wet Vpb art. 29d(1)-(2)](https://wetten.overheid.nl/BWBR0002672) |
| CbC report | Within twelve months after the last day of the reporting year | [Wet Vpb art. 29c(1)-(2)](https://wetten.overheid.nl/BWBR0002672) |
| Corporate return, calendar year | Before 1 June of the next year; online extension to 1 November if asked for before 1 June; longer or non-calendar extensions by form | [Belastingdienst, filing dates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen/); [extensions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/uitstel_aangifte_vennootschapsbelasting/) |
| Corporate return, broken year | Within 5 months after the year end | [Belastingdienst, filing dates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen/) |
| Public CbC report | Published within twelve months after the financial year; online for at least five years | [Public-report decree](https://wetten.overheid.nl/BWBR0049420) |

The master and local file deadline moves with the actual return deadline, so record the extension actually granted. CbC notification and report go through the Belastingdienst portal with eHerkenning; keep the completion confirmation and the list of covered entities, because a submission is not complete until confirmed. [CbC FAQ](https://gegevensportaal.belastingdienst.nl/cbc/faq/nl/). For a calendar 2026 reporting year, the notification is due by 31 December 2026 and the report by 31 December 2027.

## Penalties and interest

A missing CbC report, a missing master or local file and missing article 8b records are three different failures. None changes the arm's length price. They change who must prove it and what fine can follow.

| Failure | Consequence | Amount (2026) | Source |
|---|---|---|---|
| CbC report (art. 29c) or notification (art. 29d) not made, late, incomplete or wrong, through intent or gross negligence | Vergrijpboete on the reporting entity, or on the group entity that had to notify. Set case by case with the formal-law coordinator; no policy percentage. Time limit: five years after the end of the calendar year the obligation arose | Up to EUR 1,100,000 | [Wet Vpb art. 29h(1)-(2)](https://wetten.overheid.nl/BWBR0002672); [Sr art. 23(4)](https://wetten.overheid.nl/BWBR0001854); [Stb. 2025, 401](https://zoek.officielebekendmakingen.nl/stb-2025-401.html); [BBBB § 28h](https://wetten.overheid.nl/BWBR0038145) |
| Same CbC failure as a criminal offence | AWR chapter IX applies, without the usual condition that too little tax was levied | Up to 6 months' detention or EUR 11,000 (art. 68(1)); intentional: up to 4 years' imprisonment or EUR 27,500 (art. 69(1)). For a company the court can go one category higher if the fine is not adequate (EUR 27,500 or EUR 110,000) | [Wet Vpb art. 29h(3)](https://wetten.overheid.nl/BWBR0002672); [AWR art. 68-69](https://wetten.overheid.nl/BWBR0002320); [Sr art. 23(7)](https://wetten.overheid.nl/BWBR0001854); [Kamerstukken II 34305, nr. 3](https://zoek.officielebekendmakingen.nl/kst-34305-3.html) |
| Article 8b(3) records missing or clearly inadequate | Burden of proof shifts: the taxpayer must make plausible (aannemelijk maken) that its prices are arm's length, by any means. No administrative fine for the gap itself; not keeping the required administration is a criminal offence | Criminal: AWR art. 68(1)(d) amounts above | [Wet Vpb art. 8b(3)](https://wetten.overheid.nl/BWBR0002672); [Kamerstukken II 28034, nr. 3](https://zoek.officielebekendmakingen.nl/kst-28034-3.html); [AWR art. 68](https://wetten.overheid.nl/BWBR0002320) |
| Master or local file (art. 29g) not in the administration by the return deadline | The files belong to the administration, so the ordinary records offences apply and the inspector can issue an information decision. For the intentional offence (art. 69) the too-little-tax condition still applies | AWR art. 68 / 69 amounts above | [Wet Vpb art. 29g](https://wetten.overheid.nl/BWBR0002672); [AWR art. 52(3), 52a, 68-69](https://wetten.overheid.nl/BWBR0002320); [Kamerstukken II 34305, nr. 3](https://zoek.officielebekendmakingen.nl/kst-34305-3.html) |
| Information decision (informatiebeschikking) for a failure under AWR art. 41, 47, 47a, 49 or 52 becomes final, or no return was filed | Reversed and heavier burden of proof: the assessment stands in objection and appeal unless the taxpayer shows (doen blijken) that and how far it is wrong. Not for a vergrijpboete | None fixed | [AWR art. 52a, 25(3), 27e](https://wetten.overheid.nl/BWBR0002320) |
| Return incorrect through intent (primary assessment) | Vergrijpboete with the assessment. Gross negligence alone is not enough here | Up to 100%; policy 50% | [AWR art. 67d](https://wetten.overheid.nl/BWBR0002320); [BBBB § 25-26](https://wetten.overheid.nl/BWBR0038145) |
| Assessment too low through gross negligence or intent (additional assessment, navorderingsaanslag) | Vergrijpboete with the additional assessment, on the tax caused by that conduct, also where the tax was set under a reversed burden of proof | Up to 100%; policy 25% gross negligence, 50% intent | [AWR art. 67e](https://wetten.overheid.nl/BWBR0002320); [BBBB § 25(2), (3), (5), (6) and § 27](https://wetten.overheid.nl/BWBR0038145) |
| Assessment set more than 6 months after the year end | Tax interest on the amount payable, from 6 months after the year end until the assessment is collectable | 5% a year from 1 Jan 2026 | [AWR art. 30fc](https://wetten.overheid.nl/BWBR0002320); [Belastingdienst, rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente) |

How to use the table:

- Corporate tax is levied by assessment, so the fines for self-assessed taxes paid late (AWR art. 67c and 67f) do not apply to it. [Wet Vpb art. 24](https://wetten.overheid.nl/BWBR0002672).
- Fines are not automatic. Departing from the 2022 decree does not by itself lead to a fine. [Decree, note 4](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).
- A TP correction is a tax adjustment first. The fine needs gross negligence or intent on top, and the reversed burden of proof never reaches the fine. [AWR art. 25(3), 27e(3)](https://wetten.overheid.nl/BWBR0002320).
- Missing 8b records shift the burden of proof; they do not reverse it. Reversal needs a final information decision or an unfiled return.
- An information decision can be objected to. Act within the deadline it states. If the inspector sets the assessment before the information decision is final, the information decision lapses. [AWR art. 52a(3)](https://wetten.overheid.nl/BWBR0002320).

## Cross-border points

- **APA (advance pricing agreement).** Agrees an arm's length method or remuneration for cross-border related-party transactions or permanent establishment profit allocation. Screen the ruling policy first: economic nexus with relevant Dutch staff, no tax-avoidance main motive, and the low-tax and sanctions exclusions. Normal term up to five financial years; exceptionally ten with a mid-term evaluation. Bilateral and multilateral requests go through the MAP team; a unilateral Dutch APA does not bind the other country. [Besluit fiscale rulingpraktijk, sections 2-8](https://wetten.overheid.nl/BWBR0042342); [Belastingdienst, ruling](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/ruling/).
- **ICAP.** A voluntary multilateral risk assessment in which the Netherlands takes part. It gives risk assurance, not the legal certainty of an APA. [OECD ICAP handbook](https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/02/international-compliance-assurance-programme_adf0be32/a44d51e2-en.pdf).
- **Disputes.** Keep the assessment, its reasoning and the objection deadline. Treaty MAP and EU dispute routes run on their own deadlines; starting talks does not stop them. [Decree section 11](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).
- **Amount B** is not a Dutch domestic safe harbour for distributors. The Dutch decree only accepts its correct application in covered foreign jurisdictions, under treaty and local-implementation conditions. [Amount B decree, sections 2-3](https://wetten.overheid.nl/BWBR0050664).
- **Public CbC** is a separate deliverable with its own two-year test. Groups whose companies and branches are all in the Netherlands are out, and banks publishing under the capital-requirements rules are out. [Public-report decree, art. 2](https://wetten.overheid.nl/BWBR0049420).

## Worked examples

### Example 1: low-value services recharge

A Dutch shared-service company provides payroll processing and IT helpdesk support to group companies. After stripping out shareholder costs, the eligible direct and indirect costs and overhead allocated to one recipient are EUR 200,000. All the decree's low-value conditions are met. The 5% markup is EUR 10,000, so the charge is EUR 210,000, with no benchmark study needed. The allocation key must still reflect expected benefit. If the service were core manufacturing or product development, the simplification would fail and this arithmetic would prove nothing. [Decree section 6.3](https://www.officielebekendmakingen.nl/stcrt-2022-16685.html).

```oa-check
name: NL low-value services, cost base EUR 200,000 at 5% markup (2026)
inputs:
  eligible_costs: 200000
steps:
  - markup: eligible_costs * 0.05
  - charge: eligible_costs + markup
expected:
  markup: 10000.00
  charge: 210000.00
```

### Example 2: TP correction under a reversed burden of proof, then a fine

Calendar year 2026. A Dutch distributor in a group with EUR 80,000,000 of preceding-year revenue reported a taxable amount of EUR 1,000,000. It had no local file in its administration by the return deadline and did not answer the inspector's information request. The information decision became final. The inspector then raises an additional assessment correcting the intra-group purchase prices by EUR 300,000. Because the decision is final, the assessment stands unless the company shows that and how far it is wrong (AWR art. 25(3), 27e).

Tax before the correction is 19% of EUR 200,000 plus 25.8% of EUR 800,000, which is EUR 244,400. The taxable amount is above EUR 200,000 before and after, so the whole correction is taxed at 25.8%: EUR 77,400 extra. If the inspector proves gross negligence, the policy fine is 25% (EUR 19,350); for intent, 50% (EUR 38,700); the legal maximum is 100% (EUR 77,400). The reversed burden of proof does not apply to the fine. Tax interest at 5% runs on the extra tax from 1 July 2027 until the assessment is collectable. If the group also had EUR 750,000,000 of revenue and its Dutch parent filed no CbC report through intent or gross negligence, a separate fine of up to EUR 1,100,000 could follow. [Wet Vpb art. 22, 29g, 29h](https://wetten.overheid.nl/BWBR0002672); [AWR art. 25, 27e, 30fc, 52a, 67e](https://wetten.overheid.nl/BWBR0002320); [BBBB § 25](https://wetten.overheid.nl/BWBR0038145); [Stb. 2025, 401](https://zoek.officielebekendmakingen.nl/stb-2025-401.html).

```oa-check
name: NL TP correction of EUR 300,000 and vergrijpboete (2026)
inputs:
  taxable_before: 1000000
  correction: 300000
steps:
  - tax_before: min(taxable_before, 200000) * 0.19 + max(taxable_before - 200000, 0) * 0.258
  - taxable_after: taxable_before + correction
  - tax_after: min(taxable_after, 200000) * 0.19 + max(taxable_after - 200000, 0) * 0.258
  - extra_tax: tax_after - tax_before
  - fine_gross_negligence: extra_tax * 0.25
  - fine_intent: extra_tax * 0.50
  - fine_legal_max: extra_tax * 1.00
expected:
  tax_before: 244400.00
  extra_tax: 77400.00
  fine_gross_negligence: 19350.00
  fine_intent: 38700.00
  fine_legal_max: 77400.00
```

Other checks in short, all from the articles above: revenue of exactly EUR 50,000,000 in the preceding year meets the 29g test (at least). A step-up from an agreed EUR 100,000 to an arm's length EUR 140,000 is denied under article 8bc if the seller includes only EUR 100,000. A proposed EUR 20,000 extra deduction is allowed under article 8bb only to the EUR 12,000 the counterpart is shown to include, leaving EUR 8,000 denied. Exactly EUR 750,000,000 meets the confidential CbC test (at least) but not the public CbC test (more than).

## Ask the client first

- Which Dutch entity or permanent establishment, which corporate tax year and which group reporting year? The ownership chart and every related party, domestic ones included.
- Consolidated group revenue for the preceding reporting year, the ultimate parent and its residence, and who files the CbC report.
- The intra-group transactions by type (goods, services, IP, loans, guarantees, restructurings, asset transfers), with agreements and ledger totals.
- For any downward adjustment or step-up: evidence of what the foreign counterpart includes in its profit tax.
- The existing files: article 8b records, master and local file, CbC notifications and confirmations, APAs or rulings, the actual return deadline and extension.
- Any letter from the inspector: an information request, an information decision, an assessment or a fine notice, with its date.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet op de vennootschapsbelasting 1969, art. 8b, 8ba-8bd, 22, 24, 29b-29h | https://wetten.overheid.nl/BWBR0002672 | 2026-10-23 |
| Algemene wet inzake rijksbelastingen, art. 25, 27e, 30fc, 52, 52a, 67d-67f, 68, 69 | https://wetten.overheid.nl/BWBR0002320 | 2026-10-23 |
| Wetboek van Strafrecht, art. 23(4) and (7) | https://wetten.overheid.nl/BWBR0001854 | 2026-10-23 |
| Besluit van 26 november 2025, Stb. 2025, 401 (fine categories from 1 January 2026) | https://zoek.officielebekendmakingen.nl/stb-2025-401.html | 2026-10-23 |
| Besluit Bestuurlijke Boeten Belastingdienst, § 25-27 and § 28h | https://wetten.overheid.nl/BWBR0038145 | 2026-10-23 |
| Verrekenprijsbesluit 2022, Stcrt. 2022, 16685 | https://www.officielebekendmakingen.nl/stcrt-2022-16685.html | 2026-10-23 |
| Memorie van toelichting art. 8b, Kamerstukken II 2001/02, 28034, nr. 3 | https://zoek.officielebekendmakingen.nl/kst-28034-3.html | 2026-10-23 |
| Memorie van toelichting art. 29b-29h, Kamerstukken II 2015/16, 34305, nr. 3 | https://zoek.officielebekendmakingen.nl/kst-34305-3.html | 2026-10-23 |
| Regeling aanvullende documentatieverplichtingen verrekenprijzen | https://wetten.overheid.nl/BWBR0037475 | 2026-10-23 |
| Implementatiebesluit Richtlijn openbaarmaking winstbelasting (public CbC) | https://wetten.overheid.nl/BWBR0049420 | 2026-10-23 |
| Besluit fiscale rulingpraktijk | https://wetten.overheid.nl/BWBR0042342 | 2026-10-23 |
| Bedrag B besluit 2025 (Amount B) | https://wetten.overheid.nl/BWBR0050664 | 2026-10-23 |
| Belastingdienst, corporate return filing dates | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen/ | 2026-10-23 |
| Belastingdienst, corporate return extension | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/uitstel_aangifte_vennootschapsbelasting/ | 2026-10-23 |
| Belastingdienst, tax interest rates | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-10-23 |
| Belastingdienst, ruling and APA | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/ruling/ | 2026-09-28 |
| Belastingdienst, CbC notification FAQ | https://gegevensportaal.belastingdienst.nl/cbc/faq/nl/ | 2026-09-28 |
| OECD Transfer Pricing Guidelines 2022 | https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf | 2026-09-28 |
| OECD ICAP handbook | https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/02/international-compliance-assurance-programme_adf0be32/a44d51e2-en.pdf | 2026-09-28 |

No later decree amending the Verrekenprijsbesluit 2022 was found in a search of officielebekendmakingen.nl on 23 October 2026.

Not yet confirmed: how the Belastingdienst sets the amount of an article 29h fine in practice (BBBB § 28h leaves it to the formal-law coordinator and publishes no percentage); whether the Beleidsbesluit toepassing internationaal belastingrecht in de winstsfeer 2026 (6 August 2026) changes permanent establishment profit allocation used in the local file.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `netherlands-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/netherlands-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
