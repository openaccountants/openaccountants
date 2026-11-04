---
name: ch-vat-return
description: "Preparing and filing the Swiss VAT return (MWST-Abrechnung, decompte TVA) for tax year 2026. Covers who files (CHF 100,000 worldwide turnover test, foreign businesses, electronic platforms since 1 January 2025), the 8.1%, 2.6% and 3.8% rates, output tax, reverse charge on services from abroad (Bezugsteuer) and input tax, the effective method, the net tax rate method (Saldosteuersatz, CHF 5,024,000 and CHF 108,000 caps) and the flat tax rate method (Pauschalsteuersatz), quarterly, half-yearly, monthly and the new annual settlement with ESTV instalments, the 60-day filing and payment deadline, corrections, default interest of 4.0% and penalties. Trigger on: Swiss VAT return, MWST Abrechnung, Saldosteuersatz, Pauschalsteuersatz, jährliche Abrechnung, Bezugsteuer, Verzugszins MWST. Out of scope: wider VAT topics in switzerland-vat; income and profit taxes (ch-federal-income-tax, ch-cantonal-tax, ch-corporate-income-tax); ch-cross-border; switzerland-crypto-tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ch-vat-return"
  jurisdiction: "CH"
  tax_year: "2026"
  last_updated: "2026-10-26"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Swiss VAT return (MWST-Abrechnung), tax year 2026 v2.2

> **Source-cited draft: not reviewed by an accountant.** General tax reference for AI-assisted work. Do not file, pay or take a position on it without review by a qualified professional in Switzerland.

**What this skill does.** It walks through the periodic Swiss VAT return for 2026: who files, which method and period apply, how the amounts are built, when they are due, and what late or wrong returns cost. Law: the Federal VAT Act (MWSTG, SR 641.20, consolidated version of 31 March 2025, which carries the revision in force since 1 January 2025) and the VAT Ordinance (MWSTV, SR 641.201, version of 1 January 2025), read on Fedlex. Switzerland is not in the EU: do not load `eu-vat-directive`.

**Sibling skills.** [switzerland-vat](switzerland-vat.md) for the full VAT picture (place of supply, exemptions, imports, business transfers). [ch-tax-overview](ch-tax-overview.md), [ch-corporate-income-tax](ch-corporate-income-tax.md), [ch-federal-income-tax](ch-federal-income-tax.md), [ch-cross-border](ch-cross-border.md).

## Who this applies to

- **Who must file.** Anyone who runs a business, whatever its legal form or aim, and supplies in Switzerland or has its seat, residence or a permanent establishment there (MWSTG Art. 10 (1)).
- **Small-business exemption.** Exempt if worldwide (Swiss and foreign) turnover from supplies not excluded under Art. 21 (2) is under CHF 100,000 in a year (Art. 10 (2) a). Non-profit, volunteer-run sports and cultural clubs and charities: CHF 250,000 (Art. 10 (2) c). An exempt business may opt in (Art. 11).
- **Foreign businesses.** Exempt whatever their turnover if they supply in Switzerland only exempt services, services where the Swiss customer pays reverse charge, or energy to registered customers; telecom and electronic services to non-registered customers do not qualify (Art. 10 (2) b). A foreign registrant needs a Swiss representative unless the ESTV waives it (Art. 67).
- **Electronic platforms, from 1 January 2025.** A platform that brings sellers and buyers together to a contract for a supply of goods is treated as the supplier to the buyer, with a supply both from the seller to the platform and from the platform to the buyer (Art. 20a (1)). It is not the supplier if, for example, it takes no part in the order, earns nothing tied to the deal, or only processes payment, lists ads or advertises (Art. 20a (2)). The platform reports these sales in its own return.
- **Reverse charge only.** A business not registered for VAT that buys more than CHF 10,000 a year of services from abroad pays reverse charge (Art. 45 (2) b); it registers in writing with the ESTV and declares those services within 60 days after the calendar year (Art. 66 (3)).
- **Registration.** Within 30 days after liability begins (Art. 66 (1)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 8.1% | 2026 | MWSTG Art. 25 (1), https://www.fedlex.admin.ch/eli/cc/2009/615/de ; https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz |
| Reduced rate (water in pipes, food except alcohol and restaurant service, books, newspapers, medicines and other items in Art. 25 (2)) | 2.6% | 2026 | MWSTG Art. 25 (2), (3), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Special rate for accommodation, valid at the latest to 31 December 2027 | 3.8% | 2026 | MWSTG Art. 25 (4), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Registration threshold, worldwide turnover | CHF 100,000 | 2026 | MWSTG Art. 10 (2) a, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Threshold for non-profit clubs and charities | CHF 250,000 | 2026 | MWSTG Art. 10 (2) c, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Reverse charge for a person not registered: services from abroad above | CHF 10,000 a calendar year | 2026 | MWSTG Art. 45 (2) b, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Annual settlement option: taxable turnover up to | CHF 5,005,000 a year | 2026 | MWSTG Art. 35 (1bis) b, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Net tax rate method: taxable turnover up to | CHF 5,024,000 a year | 2026 | MWSTG Art. 37 (1), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Net tax rate method: tax at the net rate up to | CHF 108,000 a year | 2026 | MWSTG Art. 37 (1), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Turnover cap at a single net rate of 0.1% to 2.1% / 3.0% / 3.7% / 4.5% / 5.3% / 6.2% / 6.8% | CHF 5.024m / 3.60m / 2.92m / 2.40m / 2.04m / 1.74m / 1.59m | 2026 | ESTV, https://www.estv.admin.ch/de/mwst-saldosteuersaetze-pauschalsteuersaetze |
| Filing and payment deadline | 60 days after the end of the reporting period | 2026 | MWSTG Art. 71 (1), 86 (1), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Default interest and refund interest | 4.0% a year (4.5% in 2025) | 2026 | Zinssatzverordnung EFD, SR 631.014, Annex 2, https://www.fedlex.admin.ch/eli/cc/2025/564/de |
| Interest not charged or paid below | CHF 100 | 2026 | SR 631.014 Art. 3 (1), https://www.fedlex.admin.ch/eli/cc/2025/564/de |

## The taxable base

The return reports, for the period, the tax due on domestic supplies, the reverse charge, and (on the effective method) the input tax.

- **Effective method (default).** Tax payable = domestic output tax + reverse charge + import tax declared under the deferral procedure, minus input tax (Art. 36). Input tax is deductible on costs used for taxable business activity (Art. 28), cut in proportion for mixed use with exempt or private activity (Art. 30), with a correction for own use (Art. 31).
- **Output tax.** Agreed or received consideration, net of VAT, times the rate for each supply. Food served in a restaurant is at 8.1%; take-away food is at 2.6% if the business separates the two (Art. 25 (3)).
- **Reverse charge (Bezugsteuer).** Services whose place is in Switzerland under Art. 8 (1), bought from foreign businesses not registered in Switzerland, at the Swiss rate (Art. 45 (1) a). A registered business owes it from the first franc (Art. 45 (2) a) and deducts it as input tax if the service is used for taxable activity.
- **Net tax rate method (Saldosteuersatz).** Tax = all taxable receipts in the period, including VAT, times the ESTV-approved net rate (Art. 37 (2)). No input tax is claimed. Invoices still show 8.1%, 2.6% or 3.8%. Reverse charge is still owed at the statutory rate in the same period (MWSTV Art. 91). A new registrant applies within 60 days of receiving the VAT number; the ESTV approves it if expected turnover and tax for the first 12 months stay within the caps (MWSTV Art. 78 (1), (2)). If it misses the 60 days, it stays on the effective method for at least three full tax periods (MWSTV Art. 78 (3)). A switch from the effective method must be notified within 60 days of the start of the tax period (MWSTV Art. 79 (1)). It is kept for at least one tax period; after leaving it, the business waits three years (Art. 37 (4)). It is closed to, among others, VAT groups, users of the import deferral procedure, mail-order sellers under Art. 7 (3), platforms treated as suppliers under Art. 20a, businesses with their seat abroad, and businesses making over half their turnover with related effective-method businesses (MWSTV Art. 77 (2)).
- **Flat tax rate method (Pauschalsteuersatz).** For public bodies and related institutions such as private schools and hospitals, care homes, public transport, clubs and foundations (Art. 37 (5); MWSTV Art. 97 (1)). Tax = taxable receipts including VAT times the ESTV-approved flat rate (MWSTV Art. 99 (1)). Every activity is reported at its own flat rate whatever its size, or, by choice, the whole taxable turnover at the highest approved flat rate (MWSTV Art. 99 (3)). An activity with no flat rate uses the net tax rate for it (MWSTV Art. 99 (2)). Kept for at least one full tax period; switches start with a tax period and are notified within 60 days of its start (MWSTV Art. 98 (2), (4)).
- **Exempt supplies** (Art. 21, for example healthcare, education, finance, insurance, letting real estate) are reported but carry no tax and no input tax. **Exports** (Art. 23) are exempt with input tax.

## Deadlines and filing

| Item | Rule | Source |
|---|---|---|
| Tax period | Calendar year | MWSTG Art. 34 (2) |
| Effective and flat tax rate methods | Quarterly returns | Art. 35 (1) |
| Net tax rate method | Half-yearly returns | Art. 35 (1) |
| Monthly, on request | Where input tax regularly exceeds output tax | Art. 35 (1bis) a |
| Annual settlement, on request (since 1 January 2025) | Taxable turnover up to CHF 5,005,000. Kept for at least one full tax period; after leaving, three tax periods before returning; switches only at the start of a tax period. The ESTV may refuse or withdraw it for a business that does not file or pay | Art. 35 (1bis) b, 35a |
| Instalments under annual settlement | ESTV sets and invoices them from last year's tax (estimated if unknown; expected tax for a new registrant). Effective and flat tax rate methods: three of one quarter each, due 150, 240 and 330 days after the start of the period. Net tax rate method: one of one half, due 240 days after the start. Paid instalments are credited against the annual return | Art. 86a (1)-(3), (6), (7) |
| Filing | Within 60 days after the reporting period ends, without a reminder. If liability ends, the 60 days run from that date | Art. 71 (1), (2) |
| Payment | Within 60 days after the reporting period ends | Art. 86 (1) |
| Refund of a credit | Paid out; refund interest (4.0% in 2026) runs if paid more than 60 days after the return arrives | Art. 88; SR 631.014 Annex 2 |
| Year-end corrections | Errors found when closing the accounts are corrected at the latest in the return for the period containing the 180th day after the financial year-end | Art. 72 (1) |
| Earlier years | Known errors in earlier returns must be corrected while those years are open and not time-barred | Art. 72 (2) |

In 2026 the 60th day after 31 March is 30 May, after 30 June is 29 August, after 30 September is 29 November, and after 31 December 2026 is 1 March 2027.

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Default interest | Due without reminder on late payment (Art. 87 (1)) and on late or short annual-settlement instalments (Art. 87 (1bis)). 4.0% a year in 2026. Not due on a reassessment of an error that would have cost the Confederation nothing if handled correctly (Art. 87 (2)) | MWSTG Art. 87; SR 631.014 Annex 2 |
| Small amounts | Default and refund interest under CHF 100 is not charged or paid | SR 631.014 Art. 3 (1) |
| Non-payment or no return | ESTV sets a provisional amount, by estimate if needed, and enforces it by debt collection after a reminder | Art. 86 (2) |
| Tax evasion (under-declared receipts, over-claimed input tax, wrongful refund) | Fine up to CHF 400,000; up to CHF 800,000 if the evaded tax was passed on in a deductible form | Art. 96 (1), (2) |
| Correctly declared facts, wrongly treated | Fine up to CHF 200,000 where the business knowingly misapplies clear law, ESTV orders or published ESTV practice without telling the ESTV in writing beforehand; up to CHF 20,000 if negligent | Art. 96 (3) |
| Errors in a return | Punishable as evasion only once the Art. 72 (1) correction window has passed | Art. 96 (6) |
| Procedural breaches (not registering, not filing, poor records) | A fine; the Act gives no fixed amount | Art. 98 |
| Voluntary disclosure | No prosecution if reported before the authority knows; an Art. 72 (2) correction counts | Art. 102 |

## Cross-border points

- **Services from abroad.** Declare reverse charge in the return for the period the service is received; registered businesses from CHF 1, others above CHF 10,000 a year (Art. 45 (2)).
- **Imports.** The Federal Office for Customs and Border Security collects import tax at the border; it is reclaimed as input tax in the return. Qualifying registered importers on the effective method, and registered platforms, may use the deferral procedure and declare import tax in the return instead (Art. 63).
- **Foreign businesses** file the same return through their Swiss representative (Art. 67) and cannot use the net tax rate method if their seat is abroad (MWSTV Art. 77 (2) h).
- **Exports and services to foreign customers** are reported as exempt or as supplies abroad (Art. 23, 8 (1)).

## Worked examples

**Example 1: annual settlement, effective method.** A Zurich GmbH chose annual settlement for 2026. Its 2025 tax was CHF 40,000, so the ESTV invoices three instalments of 40,000 × 1/4 = 10,000, due 150, 240 and 330 days after 1 January 2026. In 2026 it sells CHF 600,000 net at 8.1% and buys CHF 150,000 net of domestic costs at 8.1%. It also buys a CHF 20,000 service from a US firm not registered in Switzerland. Output tax is 48,600. Reverse charge is 1,620, owed and deducted in full. Input tax is 12,150 + 1,620. Tax for the year is 36,450. After 30,000 of instalments the balance is 6,450, due with the annual return by 1 March 2027.

```oa-check
name: Zurich GmbH, annual settlement 2026, effective method
inputs:
  prior_year_tax: 40000
  sales_net: 600000
  domestic_costs_net: 150000
  foreign_service: 20000
steps:
  - instalment: prior_year_tax / 4
  - instalments_paid: instalment * 3
  - output_tax: sales_net * 0.081
  - reverse_charge: foreign_service * 0.081
  - input_tax: domestic_costs_net * 0.081 + reverse_charge
  - annual_tax: output_tax + reverse_charge - input_tax
  - balance_due: annual_tax - instalments_paid
expected:
  instalment: 10000
  output_tax: 48600
  reverse_charge: 1620
  annual_tax: 36450
  balance_due: 6450
```

**Example 2: net tax rate method with a foreign service.** A sole trader reports half-yearly at an ESTV-approved net rate of 4.5%. In July to December 2026 it receives CHF 250,000 including VAT. Net-rate tax is 11,250. It also buys a CHF 15,000 software service from a foreign supplier not registered in Switzerland. On the net method it must pay reverse charge at the statutory 8.1% in the same return (MWSTV Art. 91) and claims no input tax, so it adds 1,215. Total due is 12,465, by 1 March 2027. Edge check: on a full year of CHF 480,000 the turnover is inside the CHF 2.40 million cap for 4.5%, and the yearly tax at 4.5% is 21,600, under CHF 108,000.

```oa-check
name: Net tax rate 4.5%, H2 2026, reverse charge on foreign software
inputs:
  receipts_incl_vat: 250000
  foreign_service: 15000
  annual_receipts: 480000
steps:
  - net_rate_tax: receipts_incl_vat * 0.045
  - reverse_charge: foreign_service * 0.081
  - total_due: net_rate_tax + reverse_charge
  - annual_net_tax: annual_receipts * 0.045
  - headroom_to_cap: 108000 - annual_net_tax
expected:
  net_rate_tax: 11250
  reverse_charge: 1215
  total_due: 12465
  annual_net_tax: 21600
  headroom_to_cap: 86400
```

## Ask the client first

- Which method are you on (effective, net tax rate, flat tax rate), and which rate did the ESTV approve? (Changes the whole computation.)
- Do you file quarterly, half-yearly, monthly or annually, and what were last year's tax and taxable turnover? (Sets deadlines, instalments and whether annual settlement or the net method is open.)
- Did you buy services from foreign suppliers not registered in Switzerland, and for how much? (Reverse charge.)
- Do you make exempt supplies or use costs privately? (Input tax cuts on the effective method.)
- Do you sell through, or run, an online platform, or import goods? (Platform rule and import tax.)
- Did you find errors in earlier returns when closing the accounts? (Art. 72 corrections and the 180-day window.)

## Sources

| Source | URL | Read on |
|---|---|---|
| MWSTG, Federal VAT Act, SR 641.20 (consolidated version of 31 March 2025) | https://www.fedlex.admin.ch/eli/cc/2009/615/de | 2026-10-26 |
| MWSTV, VAT Ordinance, SR 641.201 (version of 1 January 2025) | https://www.fedlex.admin.ch/eli/cc/2009/828/de | 2026-10-26 |
| Zinssatzverordnung EFD, SR 631.014 (in force 1 January 2026) | https://www.fedlex.admin.ch/eli/cc/2025/564/de | 2026-10-26 |
| ESTV, VAT rates | https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz | 2026-10-26 |
| ESTV, net tax rates and flat tax rates | https://www.estv.admin.ch/de/mwst-saldosteuersaetze-pauschalsteuersaetze | 2026-10-26 |
| ESTV, paying VAT | https://www.estv.admin.ch/de/mwst-bezahlen | 2026-10-26 |

Not yet confirmed: the box (Ziffer) numbers of the ESTV return form, so amounts are not mapped to boxes; the list of industries per net tax rate and the individual flat tax rates; the fine amount under Art. 98; the day-count basis for default interest; the changes in the MWSTV version in force from 1 January 2027 (not read; this skill uses the 2025 version for 2026); Liechtenstein treatment.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-26. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ch-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ch-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
