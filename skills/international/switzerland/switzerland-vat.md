---
name: switzerland-vat
description: "Swiss VAT (MWST, TVA, IVA) for tax year 2026: who must register (worldwide turnover of CHF 100,000, CHF 250,000 for non-profit clubs, foreign businesses, electronic platforms since 2025), the 8.1%, 2.6% and 3.8% rates, the taxable base and input tax, the effective method and the net tax rate method (Saldosteuersatz, ten rates, CHF 5,024,000 / CHF 108,000), quarterly, semi-annual, monthly and the new annual reporting option (CHF 5,005,000), the 60-day filing and payment deadline, reverse charge on services from abroad (Bezugsteuer, CHF 10,000), import VAT and the deferral procedure, default interest of 4.0% for 2026 and penalties. Trigger on: Swiss VAT, MWST Abrechnung, Saldosteuersatz, Bezugsteuer, jährliche Abrechnung, Verzugszins MWST, ESTV, Einfuhrsteuer, decompte TVA. Out of scope: Swiss income and profit taxes (ch-federal-income-tax, ch-cantonal-tax, ch-corporate-income-tax), cross-border income tax (ch-cross-border), crypto (switzerland-crypto-tax)."
version: 2.1
jurisdiction: CH
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
verified_by: pending
review_status: pending_review
authored_by: OpenAccountants team
depends_on:
  - vat-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland VAT (MWST): registration, rates, returns and penalties, tax year 2026 v2.1

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Switzerland.

**What this skill does.** It covers Swiss VAT for 2026 from the Federal VAT Act (MWSTG, SR 641.20) and Ordinance (MWSTV, SR 641.201), read on Fedlex, and the Federal Tax Administration (ESTV) pages. It replaces the older `ch-vat-return` skill, which now points here. Switzerland is not in the EU: do not load `eu-vat-directive`. Load `vat-workflow-base` for the workflow.

**Sibling skills.** [ch-tax-overview](ch-tax-overview.md) for the Swiss tax system. [ch-corporate-income-tax](ch-corporate-income-tax.md) and [ch-federal-income-tax](ch-federal-income-tax.md) for income and profit taxes, where VAT-registered businesses report income net of VAT. [ch-cross-border](ch-cross-border.md) for income tax on cross-border work.

## Who this applies to

- **Registration.** Anyone who runs a business is liable to VAT if they supply in Switzerland, or have their seat, residence or a permanent establishment in Switzerland (MWSTG Art. 10 (1)). Liechtenstein forms one VAT area with Switzerland under a treaty (not re-read today; see Sources).
- **Small-business exemption.** A business is exempt if its worldwide turnover (Swiss and foreign) from supplies not excluded under Art. 21 (2) is under CHF 100,000 in a year (Art. 10 (2) a). The test counts agreed consideration net of VAT (Art. 10 (2bis)). A non-profit, volunteer-run sports or cultural club or charity has a limit of CHF 250,000 (Art. 10 (2) c).
- **Voluntary registration.** An exempt business may waive the exemption, for at least one tax period (Art. 11).
- **Foreign businesses.** A foreign business with no Swiss seat or establishment is exempt, whatever its turnover, if in Switzerland it supplies only exempt services, services taxed at the customer's seat (where the Swiss customer pays reverse charge), or electricity, gas and district heating to registered customers. This does not apply to telecom or electronic services to non-registered customers (Art. 10 (2) b). A foreign business that registers must appoint a Swiss representative, unless the ESTV waives this (Art. 67).
- **Mail-order sellers.** A foreign seller that ships low-value goods (exempt from import VAT because the tax is negligible) and makes at least CHF 100,000 a year from them supplies in Switzerland and must register (Art. 7 (3) b).
- **Electronic platforms, from 1 January 2025.** A platform that brings sellers and buyers together for a supply of goods is treated as the supplier to the buyer, and as buying from the seller (Art. 20a (1)). It is not the supplier if it is not involved in the order, earns nothing from the deal, or only processes payments, lists ads, advertises or redirects (Art. 20a (2)).
- **Registration deadline.** 30 days after liability begins (Art. 66 (1)). A person liable only for reverse charge on services from abroad registers within 60 days after the calendar year and declares the services at the same time (Art. 66 (3)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 8.1% | 2026 | MWSTG Art. 25 (1), https://www.fedlex.admin.ch/eli/cc/2009/615/de ; ESTV, https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz |
| Reduced rate (water in pipes, food except alcohol, livestock, cereals, seeds and plants, medicines, books and newspapers, and other items in Art. 25 (2)) | 2.6% | 2026 | MWSTG Art. 25 (2), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Special rate for accommodation (room with breakfast), valid to 31 December 2027 | 3.8% | 2026 | MWSTG Art. 25 (4), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Registration threshold, worldwide turnover | CHF 100,000 | 2026 | MWSTG Art. 10 (2) a, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Threshold for non-profit sports and cultural clubs and charities | CHF 250,000 | 2026 | MWSTG Art. 10 (2) c, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Foreign mail-order of low-value goods: registration at | CHF 100,000 a year | 2026 | MWSTG Art. 7 (3) b, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Reverse charge on services from abroad for a person not registered: above | CHF 10,000 a year | 2026 | MWSTG Art. 45 (2) b, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Annual reporting option: taxable turnover up to | CHF 5,005,000 | 2026 | MWSTG Art. 35 (1bis) b, https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Net tax rate method: taxable turnover (incl. VAT) up to | CHF 5,024,000 | 2026 | MWSTG Art. 37 (1); ESTV, https://www.estv.admin.ch/de/mwst-saldosteuersaetze-pauschalsteuersaetze |
| Net tax rate method: tax at the net rate up to | CHF 108,000 a year | 2026 | MWSTG Art. 37 (1), https://www.fedlex.admin.ch/eli/cc/2009/615/de |
| Net tax rates (Saldosteuersätze) | 0.1%, 0.6%, 1.3%, 2.1%, 3.0%, 3.7%, 4.5%, 5.3%, 6.2%, 6.8% | 2026 | ESTV, https://www.estv.admin.ch/de/mwst-saldosteuersaetze-pauschalsteuersaetze |
| Turnover cap at a single net rate of 3.0% / 3.7% / 4.5% / 5.3% / 6.2% / 6.8% (from the CHF 108,000 tax cap) | CHF 3.60m / 2.92m / 2.40m / 2.04m / 1.74m / 1.59m | 2026 | ESTV, https://www.estv.admin.ch/de/mwst-saldosteuersaetze-pauschalsteuersaetze |
| Filing and payment deadline | 60 days after the end of the reporting period | 2026 | MWSTG Art. 71 (1), 86 (1); ESTV, https://www.estv.admin.ch/de/mwst-bezahlen |
| Default interest (Verzugszins) | 4.0% a year (4.5% in 2025) | 2026 | Zinssatzverordnung EFD, SR 631.014, Annex 2, https://www.fedlex.admin.ch/eli/cc/2025/564/de |
| Interest refund rate (Vergütungszins on refunds) | 4.0% a year | 2026 | SR 631.014, Annex 2, https://www.fedlex.admin.ch/eli/cc/2025/564/de |
| Interest not charged or paid below | CHF 100 | 2026 | SR 631.014, Art. 3 (1), https://www.fedlex.admin.ch/eli/cc/2025/564/de |
| Notification procedure required when tax on a transfer of assets exceeds | CHF 10,000 | 2026 | MWSTG Art. 38 (1), https://www.fedlex.admin.ch/eli/cc/2009/615/de |

## The taxable base

- **What is taxed.** Supplies in Switzerland for consideration (domestic tax), services bought from foreign businesses (reverse charge, Bezugsteuer) and imports of goods (import tax) (Art. 1 (2)).
- **Place of services.** As a rule, where the customer has its seat or establishment, or lives (Art. 8 (1)). Exceptions apply, for example, to services usually given to people physically present, which are taxed where the provider is (Art. 8 (2)).
- **Exempt without input tax (Art. 21).** For example healthcare, education, financial services, insurance, letting and sale of real estate, and some cultural and sporting services. No input tax on costs used for them (Art. 29 (1)), unless the business opts to tax under Art. 22.
- **Exempt with input tax (Art. 23).** For example exports of goods, with customs evidence, and international transport. There is no "zero rate" as such.
- **Input tax (effective method).** Deductible on purchases used for taxable business activity, including reverse charge on services and import tax (Art. 28). Where a cost serves both taxable and exempt or private use, the input tax is cut in proportion (Art. 30). Taking goods or services out of the business for private use or exempt use triggers a correction (own use, Art. 31).
- **Net tax rate method.** The business multiplies all taxable receipts, including VAT, by its ESTV-approved net rate. It does not claim input tax. Invoices still show the statutory 8.1%, 2.6% or 3.8% (Art. 37 (2); ESTV page). It must be applied for: new registrants within 60 days of receiving the VAT number; others switching from the effective method within 60 days of the start of a tax period (MWSTV Art. 78 (1), 79 (1)). It is kept for at least one tax period, and a business that leaves it waits three years to return (Art. 37 (4)). It cannot be used with group taxation or the import deferral procedure (MWSTV Art. 77 (2)).
- **Transfers of a business.** Transfers of a business or part of it inside restructurings use the notification procedure, not tax and input tax, where the tax would exceed CHF 10,000 or the buyer is closely related (Art. 38).

## Deadlines and filing

| Item | Rule | Source |
|---|---|---|
| Tax period | Calendar year | MWSTG Art. 34 (2) |
| Standard reporting period | Quarterly | Art. 35 (1) |
| Net tax rate method | Half-yearly | Art. 35 (1) |
| Monthly, on request | Where input tax regularly exceeds output tax | Art. 35 (1bis) a |
| Annual, on request (since 2025) | Taxable turnover up to CHF 5,005,000. Keep it for at least a full tax period; after leaving it, wait three tax periods to return; switches only from the start of a period. The ESTV may refuse or withdraw it for late filers or payers | Art. 35 (1bis) b, 35a |
| Instalments under annual reporting | ESTV invoices provisional instalments. Effective method: each one quarter of the last year's tax, due 150, 240 and 330 days after the start of the period. Net tax rate method: half of the last year's tax, due 240 days after the start | Art. 86a (1), (3), (6) |
| Filing | Within 60 days after the reporting period ends, without being asked | Art. 71 (1) |
| Payment | Within 60 days after the reporting period ends, for every reporting period type | Art. 86 (1), (10) |
| Refund of a credit balance | Paid out 60 days after the return reaches the ESTV | ESTV, mwst-bezahlen page |
| Corrections found when closing the accounts | At the latest in the return for the period that contains the 180th day after the financial year-end | Art. 72 (1) |
| Corrections of earlier years | Must be made while those years are open and not time-barred | Art. 72 (2) |

For a calendar quarter, the 60th day after 31 March is 30 May, after 30 June is 29 August, after 30 September is 29 November, and after 31 December is 1 March.

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Default interest | Due without reminder on late payment, and on late or short instalments under annual reporting. 4.0% a year in 2026. Not due on a reassessment that would have caused no loss to the Confederation if handled correctly | MWSTG Art. 87; SR 631.014 Annex 2 |
| Small amounts | Default and refund interest below CHF 100 is not charged or paid | SR 631.014 Art. 3 (1) |
| Tax evasion | Fine up to CHF 400,000; up to CHF 800,000 where the evaded tax was passed on in a form that allows input tax deduction | Art. 96 (1), (2) |
| Wrong tax treatment of correctly declared facts | Fine up to CHF 200,000 if intentional; up to CHF 20,000 if negligent | Art. 96 (3) |
| Evasion on import or false answers in an audit | Fine up to CHF 800,000 | Art. 96 (4) |
| Errors in a return | Punishable as evasion only once the Art. 72 (1) correction window has passed without correction | Art. 96 (6) |
| Procedural breaches (not registering, not filing after a reminder, poor records, showing VAT not owed) | A fine; the MWSTG gives no amount | Art. 98 |
| Voluntary disclosure | No prosecution if the business reports before the authority knows and helps settle the tax. A correction under Art. 72 (2) counts as a disclosure | Art. 102 |
| Non-payment | The ESTV sets a provisional amount and enforces it through debt collection after a reminder | Art. 86 (2) |

## Cross-border points

- **Services bought from abroad (Bezugsteuer).** A Swiss business registered for VAT pays reverse charge on services from foreign businesses not registered in Switzerland whenever the service is taxable in Switzerland, at the Swiss rate, and deducts it as input tax if used for taxable activity. A person not registered pays it only above CHF 10,000 a year (Art. 45 (1) a, (2)). Telecom and electronic services to non-registered customers are taxed on the foreign supplier, which must register.
- **Imports of goods.** All goods from abroad, including from the EU, are imports. The Federal Office for Customs and Border Security (BAZG) collects import tax at the same rates (Art. 50 ff.). The import tax is deductible as input tax.
- **Import deferral (Verlagerungsverfahren).** Registered importers on the effective method who regularly import and export and have regular input tax surpluses, and registered platforms under Art. 20a, may declare import tax in their VAT return instead of paying it at the border (Art. 63 (1)).
- **Exports and foreign customers.** Exports of goods with customs evidence are exempt with input tax (Art. 23). Services to a foreign customer under the general rule are taxed abroad (Art. 8 (1)).
- **Foreign businesses** registering in Switzerland need a Swiss representative unless the ESTV waives it (Art. 67). Their turnover test is worldwide (Art. 10 (2) a).

## Worked examples

**Example 1: effective method, Q1 2026.** A Zurich GmbH reports quarterly on the effective method. In January to March 2026 it sells CHF 150,000 net at 8.1% and CHF 40,000 net of food at 2.6%. It buys a CHF 12,000 software subscription from a US company not registered in Switzerland, and CHF 40,000 net of domestic costs at 8.1%. Output tax is 12,150 + 1,040 = 13,190. Reverse charge on the software is 12,000 × 8.1% = 972; as a registered business it owes this from the first franc. Input tax is 3,240 on domestic costs plus 972 on the reverse charge. Tax payable is 13,190 + 972 − 3,240 − 972 = 9,950. The return and payment are due within 60 days of 31 March, by 30 May 2026.

```oa-check
name: Zurich GmbH, effective method, Q1 2026 with reverse charge on a US subscription
inputs:
  sales_standard_net: 150000
  sales_reduced_net: 40000
  foreign_service: 12000
  domestic_costs_net: 40000
steps:
  - output_standard: sales_standard_net * 0.081
  - output_reduced: sales_reduced_net * 0.026
  - reverse_charge: foreign_service * 0.081
  - input_domestic: domestic_costs_net * 0.081
  - input_reverse_charge: reverse_charge
  - payable: output_standard + output_reduced + reverse_charge - input_domestic - input_reverse_charge
expected:
  output_standard: 12150
  output_reduced: 1040
  reverse_charge: 972
  input_domestic: 3240
  payable: 9950
```

**Example 2: net tax rate method, late payment.** An architect reports half-yearly at an ESTV-approved net rate of 6.2%, the rate in the ESTV's own example. In January to June 2026 the firm receives CHF 400,000 including VAT. Tax due is 400,000 × 6.2% = 24,800, with no input tax calculation. The deadline is 60 days after 30 June, 29 August 2026. The firm pays 30 days late. Default interest at 4.0% is about 24,800 × 4.0% × 30 / 365 = 81.53. That is below CHF 100, so the ESTV does not charge it (SR 631.014 Art. 3 (1)). The day-count basis does not change the result: on a 360-day basis it is 82.67, still under CHF 100. The firm's turnover is well inside the CHF 1.74 million cap for the 6.2% rate.

```oa-check
name: Architect on the 6.2% net tax rate, H1 2026, paid 30 days late
inputs:
  receipts_incl_vat: 400000
  days_late: 30
steps:
  - tax_due: receipts_incl_vat * 0.062
  - interest: tax_due * 0.04 * days_late / 365
  - interest_charged: floor(min(interest, 100) / 100) * interest
expected:
  tax_due: 24800
  interest: 81.53
  interest_charged: 0
```

## Ask the client first

- What was your worldwide turnover in the last 12 months, and are you based in Switzerland? (Decides registration under the CHF 100,000 test or the foreign-business rules.)
- Are you on the effective method or a net tax rate, and which rate did the ESTV approve? (Decides the computation and whether input tax is claimed.)
- Do you report quarterly, half-yearly, monthly or annually, and is your taxable turnover under CHF 5,005,000? (Decides deadlines and whether the annual option is open.)
- Do you buy services from foreign suppliers not registered in Switzerland, and how much a year? (Decides reverse charge.)
- Do you make exempt supplies, such as letting, financial or medical services, or use costs privately? (Decides input tax cuts.)
- Do you import goods, sell to consumers from abroad, or sell through an online platform? (Decides import tax, mail-order registration and the platform rule.)

## Sources

| Source | URL | Read on |
|---|---|---|
| MWSTG, Federal VAT Act, SR 641.20 (consolidated version of 31 March 2025) | https://www.fedlex.admin.ch/eli/cc/2009/615/de | 2026-10-23 |
| MWSTV, VAT Ordinance, SR 641.201 (consolidated version of 1 January 2025) | https://www.fedlex.admin.ch/eli/cc/2009/828/de | 2026-10-23 |
| Zinssatzverordnung EFD, SR 631.014 (in force 1 January 2026) | https://www.fedlex.admin.ch/eli/cc/2025/564/de | 2026-10-23 |
| ESTV, VAT rates in Switzerland | https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz | 2026-10-23 |
| ESTV, net tax rates and flat tax rates | https://www.estv.admin.ch/de/mwst-saldosteuersaetze-pauschalsteuersaetze | 2026-10-23 |
| ESTV, paying VAT (deadlines, refunds, default interest) | https://www.estv.admin.ch/de/mwst-bezahlen | 2026-10-23 |

Not yet confirmed: the box (Ziffer) numbers of the ESTV return form were not re-read today, so this skill does not map amounts to boxes; the full list of industries per net tax rate (ESTV ordinance SR 641.202.62) was not read; the amount of the fine for procedural breaches under Art. 98; the day-count basis the ESTV uses for default interest; the Liechtenstein treaty text; ESTV practice on private use of company cars and gifts.
