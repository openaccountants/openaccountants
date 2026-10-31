---
name: austria-vat-return
description: "Austrian VAT (Umsatzsteuer) for tax year 2026 in the deep-tax shape: who must charge VAT, the rates under § 10 UStG 1994 (20%, 13%, 10%, the 4.9% rate on listed basic foods from 1 July 2026, 19% for Jungholz and Mittelberg), the small business exemption under § 6 Abs 1 Z 27 (EUR 55,000 with the 10% tolerance) and the EU SME scheme (EUR 100,000 EU-wide), the UVA period (monthly above EUR 100,000, quarterly, none at or below EUR 55,000), the due date on the 15th of the second following month, the annual U 1 by 30 April or 30 June, reverse charge under § 19, the recapitulative statement (ZM), the late-filing surcharge (§ 135 BAO) and late-payment surcharges (§ 217 BAO). Trigger on: Austrian VAT return, UVA, Umsatzsteuervoranmeldung, U 30, U 1, Kleinunternehmerregelung, Säumniszuschlag, Austrian reverse charge. Out of scope: the Kennzahl-by-Kennzahl bank-statement method in at-vat-return; corporate income tax in at-corporate-income-tax; non-residents and treaties in at-cross-border."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/austria-vat-return"
  jurisdiction: "AT"
  tax_year: "2026"
  last_updated: "2026-10-27"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Austria: VAT (Umsatzsteuer), the UVA and the annual return (2026)

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file or pay without review by a qualified professional in Austria (Steuerberater).

**Which text of the law.** Umsatzsteuergesetz 1994 (UStG), consolidated text on the federal legal database (RIS) as of 23 October 2026, last amended by BGBl. I Nr. 62/2026. Bundesabgabenordnung (BAO), consolidated text as of 23 October 2026. The 4.9% food rate and Anlage 3 came in by BGBl. I Nr. 37/2026 and apply to supplies made after 30 June 2026 (§ 28 Abs 69 UStG). BGBl. I Nr. 43/2026 changed only Art. 21 Abs 2 of the internal-market annex (new vehicles); nothing in this skill turns on it.

**Sibling skills.** The box-by-box method for turning a bank statement into the U 30 form, with the full Kennzahl map and supplier patterns, is in [at-vat-return](at-vat-return.md). Corporate income tax is in [at-corporate-income-tax](at-corporate-income-tax.md). Non-residents, treaties and exit rules are in [at-cross-border](at-cross-border.md). This skill does not repeat them.

## Who this applies to

- **Businesses (Unternehmer) making taxable supplies in Austria.** Sole traders, partnerships and companies that supply goods or services in Austria for consideration owe VAT on those supplies (§ 1 Abs 1 Z 1 UStG). The tax is owed by the supplier (§ 19 Abs 1 UStG), except where it passes to the customer (reverse charge, below).
- **Small businesses (Kleinunternehmer).** A business run in Austria or another member state whose turnover under § 1 Abs 1 Z 1 and 2 did not exceed EUR 55,000 in the previous calendar year and has not yet exceeded it in the current year is exempt (§ 6 Abs 1 Z 27 UStG). It charges no VAT and deducts no input VAT. It can waive the exemption in writing until the assessment is final; the waiver runs from the start of a calendar year and binds for at least five calendar years (§ 6 Abs 3 UStG).
- **Businesses established in another member state.** They can use the Austrian exemption only through the EU SME scheme: EU-wide turnover not above EUR 100,000 in the previous and current year, and an application in their home state (Art. 6a procedure). The exemption starts from the day Austria is notified of their small-business identification number (§ 6 Abs 1 Z 27 UStG).
- **Customers who owe the tax.** A business (or a public body that is not a business) receiving services or work supplies from a supplier with no Austrian establishment owes the VAT itself (§ 19 Abs 1 second sentence UStG). Construction services passed down a chain, and some goods (mobile phones and chips from EUR 5,000 per invoice, scrap, emission allowances, gas and electricity from abroad) are also reverse-charged (§ 19 Abs 1a to 1e UStG).
- **Out:** private individuals, and businesses making only exempt supplies without credit (for example doctors, insurers) for those supplies.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate (§ 10 Abs 1) | 20% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Basic foods listed in Anlage 3, as goods supplied or imported (not restaurant or catering services), from 1 July 2026 (§ 10 Abs 1a, § 28 Abs 69). Anlage 3 has 12 items: milk, yoghurt, butter, fresh hen eggs, fresh or chilled vegetables, frozen vegetables, apples, pears and stone fruit (CN 0808 and 0809), rice, wheat flour and semolina, uncooked pasta, bread, table salt, each only within its listed CN code | 4.9% | 2026 (from 1 July) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Reduced rate: goods in Anlage 1 (food not in Anlage 3, books), restaurant food, residential letting, hotel accommodation, passenger transport, waste collection, repairs of bicycles, shoes, clothing (§ 10 Abs 2) | 10% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Reduced rate: goods in Anlage 2 (live animals, plants), artists, swimming pools, theatre, concerts, museums, film, circus, domestic flights, farm wine, sports event tickets (§ 10 Abs 3) | 13% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Jungholz and Mittelberg (§ 10 Abs 4) | 19% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Small business limit, previous and current year, gross (§ 6 Abs 1 Z 27) | EUR 55,000 | 2025 onward | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Tolerance in the year the limit is crossed (§ 6 Abs 1 Z 27) | 10% (to EUR 60,500) | 2025 onward | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| EU SME scheme: EU-wide annual turnover limit (§ 6 Abs 1 Z 27) | EUR 100,000 | 2025 onward | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Monthly UVA if prior-year turnover exceeded (§ 21 Abs 2) | EUR 100,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| No UVA to file (internal return only) if prior-year turnover did not exceed, and the payment is made in full on time (UVA-Verordnung § 1) | EUR 55,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005119 |
| No annual return for a small business with turnover not above this and no tax to pay (§ 21 Abs 6) | EUR 55,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Reverse charge on mobile phones and chips if invoiced consideration is at least (§ 19 Abs 1e lit b) | EUR 5,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| ZM period follows the UVA period: quarterly if prior-year turnover did not exceed this and no monthly UVA was chosen, otherwise monthly | EUR 100,000 | 2026 | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html |

## The taxable base

- **Base.** The consideration net of VAT for each taxable supply (§ 4 UStG), plus own use (Eigenverbrauch) of business goods and services. Down payments are taxed when received. Price changes, discounts and bad debts are corrected in the period they happen (§ 16 UStG).
- **When the tax arises.** On the accrual basis (Soll), at the end of the month of supply, moved by at most one month if the invoice is issued later. On the cash basis (Ist), at the end of the month of payment (§ 19 Abs 2 UStG). [at-vat-return](at-vat-return.md) sets out who uses which basis.
- **Exempt with credit.** Exports (§ 7), intra-EU supplies of goods to a business with a valid VAT number (Art. 6 Abs 1 of the annex), and cross-border transport. Input VAT on related costs stays deductible.
- **Exempt without credit.** Banking, insurance, medical care, most education, letting of business premises unless the landlord opts to tax, and the small business exemption (§ 6 Abs 1 UStG). Input VAT on related costs is lost; a business with both kinds of supply apportions (§ 12 Abs 4 to 6 UStG).
- **Input VAT.** Deductible on a proper invoice for supplies made to the business (§ 12 UStG). No deduction for ordinary cars and motorcycles and their running costs, and for business meals except where the advertising purpose far outweighs everything else. Zero-emission cars are an exception within the reasonableness cap. A cash-basis business deducts only once it has paid.
- **Reverse charge.** The customer enters the tax as output VAT and, if entitled, deducts the same amount as input VAT in the same return, so a fully taxable business pays nothing net.
- **Change of use of a capital asset.** If the facts that decided the input VAT deduction on a fixed asset change in the four calendar years after the year of first use, the deduction is corrected for each year of change, one fifth of the asset's input VAT a year. For land (including capitalised costs and major repairs) the period is nineteen years and the correction is one twentieth a year. On a sale, the rest of the period is corrected at the latest in the last UVA of that year (§ 12 Abs 10 and 11 UStG, RIS consolidated text read 26 October 2026).
- **The small business limit is counted gross.** The limit test uses the agreed consideration, not a base computed as if VAT applied (§ 6 Abs 1 Z 27 last sentence). Ancillary sales, the sale of the business, and most exempt supplies are left out.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| UVA (form U 30), monthly or quarterly, and payment | 15th day of the second calendar month after the period (§ 21 Abs 1 UStG). Q1: 15 May; Q2: 15 August; Q3: 15 November; Q4: 15 February | RIS, UStG § 21 |
| Weekend or holiday | Moves to the next day that is not a Saturday, Sunday, public holiday, Good Friday or 24 December (§ 108 Abs 3 BAO). 15 August 2026 is a Saturday and a holiday; 15 November 2026 is a Sunday | RIS, BAO § 108 |
| Choice of monthly UVA by a quarterly filer | File the January UVA on time; binds for the whole year (§ 21 Abs 2 UStG) | RIS, UStG § 21 |
| UVA at or below EUR 55,000 prior-year turnover | No UVA to file if the payment is made in full on time or there is none (UVA-Verordnung § 1); still prepare an internal return (§ 21 Abs 1 UStG). File one when there is a refund or a late or short payment, or when the tax office asks (UVA-Verordnung § 2) | RIS, UVA-Verordnung; USP, Umsatzsteuervoranmeldung |
| Recapitulative statement (ZM, form U 13) | By the end of the calendar month after the reporting period, through FinanzOnline | USP, ZM page |
| Annual return (U 1) | 30 April of the following year on paper, 30 June if filed electronically (§ 134 Abs 1 BAO). Electronic filing is the rule (§ 21 Abs 4 UStG). Paper is allowed only for a self-filer without internet access, or one not required to file UVAs because prior-year turnover did not exceed EUR 55,000 (FinanzOnline-Erklärungsverordnung § 2 with UVA-Verordnung § 1). 2026 return: 30 June 2027 | RIS, BAO § 134; RIS, FOnErklV § 2 |

Every return is filed through FinanzOnline (https://finanzonline.bmf.gv.at). A business represented by a tax adviser usually has longer for the annual return; the tax office can extend a deadline on a reasoned request (§ 134 Abs 2 BAO).

## Penalties and interest

| What | Figure | Source |
|---|---|---|
| First late-payment surcharge (Säumniszuschlag) | 2% of the tax not paid by the due date (§ 217 Abs 2 BAO) | RIS, BAO |
| Grace for the first surcharge | None if no more than five days late (weekends and holidays not counted) and everything due in the previous six months was paid on time (§ 217 Abs 5 BAO) | RIS, BAO |
| Second and third surcharges | 1% each, if still unpaid three months after enforceability, then three months after that (§ 217 Abs 3 BAO) | RIS, BAO |
| Minimum surcharge set | Surcharges below EUR 50 are not set (§ 217 Abs 10 BAO) | RIS, BAO |
| Late-filing surcharge (Verspätungszuschlag) | Up to 10% of the tax, if the delay is not excusable; not set below EUR 50 (§ 135 BAO) | RIS, BAO |
| Late ZM | Surcharge up to 1% of the amounts to be reported, at most EUR 2,200; coercive penalty up to EUR 5,000 | BMF, U 13a instructions |

Interest on assessed differences (Anspruchszinsen, § 205 BAO) applies only to income tax and corporate income tax, not to VAT. A UVA paid too low after its due date can be a fiscal offence; a self-disclosure (§ 29 FinStrG) needs the tax paid within one month. Refer that to a Steuerberater.

## Cross-border points

- **Services to EU businesses (general rule).** Taxed where the customer is (§ 3a Abs 6 UStG). The Austrian supplier charges no Austrian VAT, notes the reverse charge and both VAT numbers on the invoice, leaves the amount out of the taxable boxes and reports it in the ZM.
- **Services bought from abroad.** The Austrian business customer owes the tax (§ 19 Abs 1 UStG) and deducts it if entitled. Federal road tolls, event services under § 3a Abs 11a and letting of land are excluded: there the foreign supplier charges Austrian VAT.
- **Goods to and from the EU.** An intra-EU supply to a business with a valid VAT number is exempt only if the ZM is filed on time or a failure is justified and corrected (USP, ZM page). An intra-EU acquisition is taxed in Austria at the Austrian rate and deducted in the same UVA.
- **Foreign businesses with Austrian supplies.** They register and file UVAs like an Austrian business unless every Austrian supply is reverse-charged to the customer. A business that owes only reverse-charge tax with full deduction is assessed only on written request (§ 21 Abs 4 UStG). Input VAT refunds for businesses without Austrian supplies go through the refund procedure (§ 21 Abs 9 UStG).
- **EU SME scheme.** An Austrian small business that wants the exemption in another member state notifies in advance through FinanzOnline; it must stay within that state's limit and the EUR 100,000 EU-wide limit, with no tolerance on the EU-wide limit.
- Treaty questions, non-resident income and exit taxation: [at-cross-border](at-cross-border.md).

## Worked examples

### Example 1: Quarterly filer, Q3 2026, with the new food rate and a reverse charge

A grocery and catering business in Graz had 2025 turnover of EUR 80,000, so it files quarterly UVAs. For July to September 2026 its net sales are: EUR 30,000 at 20% (catering services and other goods), EUR 8,000 at 4.9% (listed basic foods sold over the counter, all after 30 June 2026), and EUR 5,000 at 10% (other food). It bought online advertising for EUR 1,000 net from an Irish company, which is reverse-charged at 20%. Domestic input VAT on proper invoices is EUR 4,200.

Output VAT is 6,000 + 392 + 500 = EUR 6,892. The reverse charge adds EUR 200 output and EUR 200 input. Input VAT is 4,200 + 200 = EUR 4,400. The UVA shows a payment of EUR 2,692. The due date, 15 November 2026, is a Sunday, so the UVA and payment are due Monday 16 November 2026 (§ 108 Abs 3 BAO). If the business pays three weeks late and the five-day grace does not apply, the first late-payment surcharge is 2% of EUR 2,692, EUR 53.84; it is set because it is not below EUR 50.

```oa-check
name: Austria quarterly UVA Q3 2026 with 4.9% food rate and reverse charge
inputs:
  sales_20: 30000
  sales_food: 8000
  sales_10: 5000
  rc_service: 1000
  domestic_input_vat: 4200
steps:
  - out_20: sales_20 * 0.20
  - out_food: sales_food * 0.049
  - out_10: sales_10 * 0.10
  - rc_vat: rc_service * 0.20
  - output_total: out_20 + out_food + out_10 + rc_vat
  - input_total: domestic_input_vat + rc_vat
  - payable: output_total - input_total
  - first_surcharge: payable * 0.02
expected:
  out_food: 392
  output_total: 7092
  input_total: 4400
  payable: 2692
  first_surcharge: 53.84
```

### Example 2: Small business crosses the limit, inside and then outside the tolerance

A sole trader in Vienna had 2025 turnover of EUR 48,000 and is exempt in 2026. Sales to 31 October 2026 are EUR 54,500. A EUR 4,000 job on 12 November takes the year to EUR 58,500. That is over EUR 55,000 but within the 10% tolerance (EUR 60,500), so the November job stays exempt and the exemption could run to 31 December; from 1 January 2027 the business is taxable because 2026 exceeded the limit.

On 14 December a further EUR 3,000 sale takes the year to EUR 61,500, above the tolerance by EUR 1,000. The exemption ends from that point (§ 6 Abs 1 Z 27 UStG), so this sale is taxable at 20%. The limit is counted gross, and the client billed EUR 3,000 with no VAT, so the VAT is inside the price: 3,000 x 20 / 120 = EUR 500. From that sale the business charges VAT. Its 2025 turnover did not exceed EUR 100,000, so its period is the quarter, and the EUR 500 is due by 15 February 2027 (a Monday). Because 2025 turnover did not exceed EUR 55,000, it files no UVA if it pays in full by then (UVA-Verordnung § 1); it files one if it pays late or short.

```oa-check
name: Austria small business limit, tolerance and crossing sale (2026)
inputs:
  sales_to_october: 54500
  november_job: 4000
  december_sale: 3000
  limit: 55000
  tolerance_pct: 10
steps:
  - tolerance_ceiling: limit + pct(limit, tolerance_pct)
  - after_november: sales_to_october + november_job
  - november_headroom: tolerance_ceiling - after_november
  - after_december: after_november + december_sale
  - excess_over_ceiling: after_december - tolerance_ceiling
  - vat_in_december_sale: december_sale * 20 / 120
expected:
  tolerance_ceiling: 60500
  after_november: 58500
  november_headroom: 2000
  after_december: 61500
  excess_over_ceiling: 1000
  vat_in_december_sale: 500
```

## Ask the client first

1. What was your turnover in 2025, and so far in 2026? It decides the exemption, and whether you file monthly, quarterly or no UVA.
2. Are you on the small business exemption, or did you waive it (and from which year)?
3. Do you sell any foods listed in Anlage 3 since 1 July 2026, or restaurant and catering services? The rate differs.
4. Who are your foreign suppliers and customers, and do you hold your EU customers' valid VAT numbers?
5. Are you on the cash basis or the accrual basis?
6. Does a tax adviser file for you? It changes the annual deadline.

## Sources

| Source | URL | Read on |
|---|---|---|
| Umsatzsteuergesetz 1994, RIS consolidated text as of 23.10.2026 (§ 6 Abs 1 Z 27 and Abs 3, § 10, § 19, § 21, § 28 Abs 69 and 70) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 | 2026-10-23 |
| Bundesabgabenordnung, RIS consolidated text as of 23.10.2026 (§ 108, § 134, § 135, § 205, § 217) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 | 2026-10-23 |
| Budgetmaßnahmengesetz 2026, BGBl. I Nr. 43/2026 (Art. 2, UStG change) | https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2026_I_43/BGBLA_2026_I_43.html | 2026-10-23 |
| Änderung des Umsatzsteuergesetzes 1994, BGBl. I Nr. 37/2026 (4.9% rate, Anlage 3) | https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2026_I_37/BGBLA_2026_I_37.html | 2026-10-23 |
| Verordnung betreffend die Abstandnahme von der Verpflichtung zur Abgabe von Voranmeldungen (UVA-Verordnung), BGBl. II Nr. 206/1998 as amended by BGBl. II Nr. 401/2024, RIS consolidated text (§§ 1, 2) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005119 | 2026-10-23 |
| FinanzOnline-Erklärungsverordnung (FOnErklV), RIS consolidated text (§ 2, when paper filing is allowed) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20005197 | 2026-10-23 |
| USP, Umsatzsteuervoranmeldung (UVA thresholds and the EUR 55,000 filing relief) | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html | 2026-10-23 |
| USP, Zusammenfassende Meldung (deadline, period table, exemption condition) | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html | 2026-10-23 |
| BMF, U 13a instructions for the ZM (late surcharge and coercive penalty) | https://formulare.bmf.gv.at/service/formulare/inter-steuern/pdfd/9999/u13a.pdf | 2026-10-23 |

Not yet confirmed: the reasonableness cap for input VAT on zero-emission cars was not read for 2026.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `austria-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/austria-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
