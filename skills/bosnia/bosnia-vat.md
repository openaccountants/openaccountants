---
name: bosnia-vat
description: "Bosnia and Herzegovina VAT (PDV, porez na dodanu vrijednost) for 2026. VAT is a single state-level tax across the Federation, Republika Srpska and Brčko District, run by the Indirect Taxation Authority (UIO, uino.gov.ba). Covers who must register (100,000 KM threshold since December 2023), the single 17% rate, exemptions and zero-rated exports, place of supply, input tax and its blocks, partial exemption, capital goods adjustment, the monthly return (boxes 11 to 80) due by the 10th, refunds, the construction scheme, services bought from foreign suppliers, the 2026 first-home refund, penalties and 0.04% daily interest. Trigger on: PDV prijava, PDV obveznik, prag za registraciju, ulazni porez, UIO, ITA, Bosnia VAT return, 17% BiH. Out of scope: excise and customs duty, entity income taxes (bosnia-income-tax, ba-corporate-income-tax)."
version: 2.1
jurisdiction: BA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina: VAT (PDV) 2026

> **Not reviewed by an accountant.** Figures come from the Zakon o porezu na dodanu vrijednost (Službeni glasnik BiH 9/05, 35/05, 100/08, 33/17, 46/23, 80/23, 20/25), the Zakon o postupku indirektnog oporezivanja (89/05, 100/13), the VAT rulebook amendment of 2026 (45/26) and the UIO return instructions (47/22), all read on uino.gov.ba on 30 October 2026. It prepares working papers; it is not authority to file or pay.

VAT is the one general tax set at state level. The same law, rate, return and authority apply in the Federation of BiH, Republika Srpska and Brčko District; Bosnia and Herzegovina is one place of supply (Law art. 14). Revenue is shared out afterwards, which is why the return asks for sales to non-registered buyers by entity (boxes 32 to 34).

Related skills: entity income and payroll taxes in [bosnia-income-tax](bosnia-income-tax.md), [bosnia-payroll](bosnia-payroll.md) and [ba-corporate-income-tax](ba-corporate-income-tax.md); the system overview in [ba-tax-overview](ba-tax-overview.md); setting up in [ba-company-formation](ba-company-formation.md).

## Who this applies to

- **Taxable persons (art. 12).** Anyone who independently carries on an economic activity: producing, trading or providing services to earn income, including farming, forestry, exploiting natural resources and the professions, and using property or rights to earn income. Public bodies acting as authorities are outside VAT unless they compete with private firms.
- **Who pays (art. 13).** The supplier of taxable goods and services; the tax representative of a foreign supplier with no seat or permanent unit in BiH; **the business customer of services from a foreign supplier who has not appointed a tax representative**; anyone who shows VAT on an invoice when not entitled to; the importer or customs debtor; and the customer of construction work under the special scheme.
- **Registration (art. 57 as amended by 80/23).** A person whose taxable supplies and exempt-with-credit supplies (exports) in the previous year exceed, or are likely to exceed, 100,000 KM must register. Supplies of related companies under common control count together. The 100,000 KM threshold applies from 2 December 2023 (80/23, in force on the eighth day after publication on 24 November 2023).
- **Below the threshold (art. 44).** A small business under the threshold is not a VAT payer and may not charge VAT or deduct input tax, unless it registered before. It can apply to register voluntarily at any time; it then stays registered for at least 60 months. A farmer whose household's total cadastral income is below 15,000 KM is not a VAT payer.
- **Foreign suppliers (art. 60).** A business with no seat in BiH that makes supplies in BiH registers through a tax representative seated in BiH; both are jointly and severally liable.
- **Voluntary registration for letting (art. 61).** UIO may allow a landlord of non-residential premises, or a farmer, to register voluntarily for at least two calendar years.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 17% on taxable supplies and imports | 2026 | [VAT Law art. 23](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-Zakon_o_PDV-b.pdf) |
| Reduced rates | none | 2026 | VAT Law art. 23 |
| Exports and international transport | exempt with right to deduct (zero-rated) | 2026 | VAT Law arts. 27, 28 and 32(5) |
| Registration threshold | 100,000 KM of taxable and zero-rated supplies in the previous year, or likely in the current year | from 2 Dec 2023 | [VAT Law art. 57(1) as amended by 80/23](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-5-Z-o-PDV-sl-list-80-23-24-11-23.pdf) |
| Voluntary registration, minimum period | 60 months (small business); two calendar years (letting, farming) | 2026 | VAT Law arts. 44(7) and 61 |
| Farmers outside VAT | household cadastral income below 15,000 KM | 2026 | VAT Law art. 44(3) |
| Construction special scheme | works on new or existing buildings worth more than 25,000 KM | 2026 | VAT Law art. 40 |
| Capital goods adjustment | equipment costing over 10,000 KM: 5 years; buildings: 10 years; no adjustment below 5% | 2026 | VAT Law art. 36 |
| Residential letting exempt | lets of houses and flats for more than 60 days | 2026 | VAT Law art. 25(3) |
| Refund deadline | 60 days after the return deadline; 30 days after filing for a business whose main activity is exporting and that is in credit on consecutive returns | 2026 | VAT Law art. 52 |
| Unused credit | refunded after six months | 2026 | VAT Law art. 52 |
| First-home refund | citizens with BiH domicile buying a newly built first home (none owned in the last seven years): VAT on up to 40 m² plus 15 m² per household member; cap = 14.5299% of (the average flat price including VAT in the latest quarterly report of the BiH Statistics Agency before the contract date × 55 m²); claim by 30 June of the year after the sale is registered (sales registered between 20/25 taking effect and the rulebook taking effect: within six months of the rulebook) | from the eighth day after 30 Jun 2026 | [VAT Law art. 54a (20/25)](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-6-Z-o-izmj-i-dop-Z-o-PDV-sl-list-20-25-04-04-2025.pdf); [Rulebook art. 105a (45/26)](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/2_Pravilnici/B/B-1-24-P-o-izmj-i-dop-Praviln-o-primj-Z-o-PDV-sl-list-45-26-30-06-2026.pdf) |
| Currency | returns and payments in convertible marks (KM); fixed rate 1 EUR = 1.95583 KM | 2026 | [Central Bank of BiH, official exchange rate notice](https://www.cbbh.ba/press/ShowNews/321?lang=en) |
| Late payment interest | 0.04% a day | 2026 | [Procedure Law art. 10(1) as amended by 100/13](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/1_UIO/3_Zakon_o_postupku_indirektnog_oporeivanja/1_Zakon/B/B-1-1-Zakon-o-izmjenama-Zakona-o-postupku-indirektnog-oporezivanja-Sluzbeni-glasnik-BiH-broj-10013.pdf) |
| Enforcement surcharge | 5% of the debt when enforced collection starts | 2026 | Procedure Law art. 11(1) as amended by 100/13 |
| Late or missing return | 300 KM fine, except when the return shows a credit (negativna prijava) | 2026 | VAT Law art. 67(1)(4) |

## The taxable base

**What is taxed (arts. 3 to 11).** Supplies of goods and services in BiH for consideration, imports, and self-supplies: business assets taken for private use or given away, goods kept after deregistration, and services provided free for private purposes (arts. 5, 6 and 9).

**Place of supply (arts. 14 and 15).** Goods: where they are when dispatch begins, where they are installed, or where they enter the customs area. Services: where the supplier is established, except that services connected with real estate are taxed where the property is; transport where it takes place (only the BiH part of international transport); cultural, sporting, educational and similar services, and work on movable goods, where performed; and the following are taxed where the customer is established: licences and other intellectual property, advertising, consultancy, engineering, legal, audit, accounting, translation, data processing and supply of information, financial and insurance services, staff supply, telecommunications, hire of movable goods other than means of transport, and agents for these. When a BiH supplier provides those services to a customer established abroad, the supply is outside BiH VAT.

**Tax point (art. 17).** The earliest of delivery or performance, issue of the invoice, or payment (including part payment) before the invoice; for imports, when customs debt arises.

**Taxable amount (arts. 20 and 21).** Everything the supplier receives or is to receive, without VAT, including subsidies linked to the price, excise and other public charges, and incidental costs charged to the customer. Market value applies when consideration is in kind, below market value or nil. Discounts given on the invoice and disbursements recharged at cost are left out. Imports: customs value plus duties, excise and incidental costs to the first destination.

**Exempt without credit (arts. 24 and 25).** Public postal services; medical and dental care; social security; education; non-profit sport and culture; religious services; members' services of non-profit bodies; public broadcasting (non-commercial); insurance and reinsurance; sales of real estate **except the first transfer of a newly built property**; residential lets over 60 days and lets of registered farm and forest land; financial services (credit, deposits and accounts, payments, currency, shares and securities, investment funds); stamps; gambling.

**Zero-rated (arts. 27 and 28, with credit under art. 32).** Exports by or for the seller; services directly linked to imports and exports; work on goods imported for processing and re-exported for a foreign customer; supplies for humanitarian export; international air and sea transport supplies.

**Input tax (art. 32).** A registered person deducts VAT charged by other registered persons and import VAT paid on goods and services used for taxable supplies or zero-rated supplies, in the period in which the VAT arose, holding a proper invoice or import document. Not deductible:

- passenger cars, buses, motorcycles, boats and aircraft, their parts, fuel, hire and repairs, unless used **exclusively** for the business;
- business entertainment and accommodation, representation costs;
- property used as housing, child care or recreation for the owner or staff;
- payments to employees in kind;
- VAT on an invoice from someone not entitled to issue one, or charged too high, even if paid.

**Partial exemption (art. 33).** A business with both taxable and exempt supplies deducts the share of input tax that matches taxable turnover in total turnover (excluding VAT), set yearly as a whole-number percentage from the previous year's figures. Occasional financial or property transactions and equipment sales are left out of the fraction. UIO can allow a separate fraction for each activity with separate books.

**Mixed-use buildings and capital goods (arts. 34 and 36).** VAT on a building with business and other premises is deducted in proportion to construction costs (repairs by floor area). Deductions on equipment over 10,000 KM and on buildings are adjusted if their use changes, for 5 and 10 years respectively, unless the change is below 5%.

**Services from foreign suppliers (art. 13(1)(3)).** If a supplier with no seat in BiH and no tax representative provides services whose place of supply is BiH to a business, the business customer is liable for the VAT. It pays the VAT and then deducts it: UIO's return instructions put this VAT in box 41 only once the customer has paid it, and the value of the service in box 21.

**Construction scheme (arts. 40 to 42).** For building work over 25,000 KM, the main contractor pays the VAT invoiced by a subcontractor, quoting the subcontractor's VAT number; the subcontractor deducts it once it receives proof of payment. Both are jointly liable until then.

**Bad and corrected invoices (art. 55).** A credit note is issued for returns, later discounts and extra payments. VAT shown on an invoice by someone not registered, or on an exempt supply, or overstated, is payable to UIO unless corrected in the customer's favour.

## Deadlines and filing

- **Registration (art. 57).** Apply at least eight days before starting taxable business; or, once the threshold is passed, by the 20th of the month after the month in which turnover passed (or was likely to pass) 100,000 KM. UIO issues the decision within 15 days and fixes the registration date. Display the registration certificate at the business premises.
- **Tax period and return (arts. 38 and 39).** The tax period is the calendar month. Each registered person files a monthly VAT return (PDV prijava) by the 10th of the month after the period, even if nothing is due, and pays by the same day. Persons liable under chapter III (art. 13), such as customers of foreign suppliers, also pay by the 10th. Import VAT is paid under the customs rules at import.
- **Return boxes (UIO instructions, Službeni glasnik BiH 47/22).**

| Box | What goes in |
|---|---|
| 11 | value of taxable supplies, including self-supplies |
| 12 | value of exports |
| 13 | value of exempt supplies under arts. 24 and 25 |
| 21 | value of purchases (registered and non-registered suppliers, including services from abroad and capital goods), without VAT |
| 22 | value of imports (customs base) |
| 23 | net value of purchases from farmers on the flat-rate compensation |
| 32, 33, 34 | VAT charged to non-registered buyers in the FBiH, RS and Brčko |
| 41 | input VAT on purchases from registered persons, plus VAT paid by the customer on services from foreign suppliers, plus the deductible share under art. 33 |
| 42 | import VAT paid in the period |
| 43 | flat-rate compensation paid to farmers |
| 51 | output VAT on supplies and self-supplies |
| 61 | 41 + 42 + 43 |
| 71 | 51 − 61: payable if positive, credit if negative |
| 80 | X = refund requested when box 71 is negative |

- **Refunds (art. 52).** A negative box 71 can be refunded or carried forward; credit still unused after six months is refunded. Refunds are paid within 60 days of the return deadline, or within 30 days of filing for a business whose main activity is exporting and that is in credit on consecutive returns. If late, UIO pays interest from 30 days after the return was filed.
- **Deregistration (art. 62).** UIO can deregister a person whose previous-year turnover did not exceed the threshold, or who stops trading. Before deregistration, VAT is charged on goods held in stock as if taken for own use.
- **Records (art. 56).** Books with enough detail to compute the VAT for each period; keep copies of all invoices, credit notes and payment statements.

## Penalties and interest

Under VAT Law art. 67:

- No return or late return: 300 KM, except when the return shows a credit (negativna prijava).
- VAT not charged or not paid, or wrongly calculated: 50% of the amount, at least 100 KM.
- Input tax wrongly deducted: 50% of the unlawful gain.
- VAT charged or deducted by a non-registered small business: 100% of the amount, at least 100 KM.
- No invoice issued or no copy kept: 300 KM. VAT not shown properly on an invoice: 100% of the VAT, or 300 KM in other cases.
- Books not kept: 300 to 10,000 KM.
- Failure to notify UIO of start, change or end of activity (registration): 100% of the unreported liability, at least 1,000 KM.
- A first-home buyer who has to repay the refunded VAT: 5,000 to 10,000 KM (art. 67 as amended by 20/25).
- The authorised person in a legal entity is fined the same as the entity. All fines rise by 50% for repeat offenders, for obstruction, or for fraud through third parties.

Interest on late VAT is 0.04% a day (Procedure Law art. 10). When enforced collection starts, a 5% surcharge is added (art. 11).

## Cross-border points

- **Imports.** VAT at 17% on the customs value plus duties and incidental costs, collected by UIO at customs and deductible in box 42 once paid (arts. 21, 32 and 39). Some imports free of customs duty are also VAT-free (art. 26 as amended by 33/17).
- **Exports.** Zero-rated with full input tax deduction; keep the export customs declaration (art. 27; return instructions box 12).
- **Services to foreign customers.** Services listed in art. 15(2)(4) (consultancy, IT and data processing, advertising, licensing, staff supply and others) supplied to a customer established abroad are outside BiH VAT.
- **Services from foreign suppliers.** The BiH business customer pays the VAT if the supplier has no tax representative, and deducts it once paid (art. 13; box 41).
- **Foreign businesses.** A foreign business making supplies in BiH registers through a tax representative (art. 60). A foreign business with no establishment and no BiH supplies can reclaim BiH input VAT on form PDV SL 1 (art. 53).
- **Diplomats, international organisations and aid projects.** VAT paid on supplies to diplomatic and consular missions, to international organisations and their members where a treaty BiH signed provides for it, and on supplies under international aid projects that BiH has committed to keep free of VAT, is refunded (art. 29(1), point 4 added by 35/05). Supplies under projects financed from the EU pre-accession instrument (IPA) are exempt (art. 29(2), added by 100/08), with the right to deduct input tax (art. 32(5)).
- **Travellers.** Non-residents can reclaim VAT on goods taken out of BiH, except mineral oils, alcohol and tobacco (art. 54).

## Worked examples

### Example 1: monthly return for a trading company (2026)

A Sarajevo company registered for VAT sells goods in BiH for 50,000 KM net in March 2026. It buys goods from registered suppliers for 20,000 KM net plus 3,400 KM VAT, and imports goods with a customs base of 10,000 KM, paying 1,700 KM import VAT in March.

- Box 11: 50,000. Box 51: 50,000 × 17% = 8,500 KM.
- Box 21: 20,000. Box 41: 3,400 KM. Box 22: 10,000. Box 42: 1,700 KM.
- Box 61: 3,400 + 1,700 = 5,100 KM.
- Box 71: 8,500 − 5,100 = 3,400 KM, filed and paid by 10 April 2026.

```oa-check
name: BiH monthly VAT return, trading company (2026)
inputs:
  sales: 50000
  purchases: 20000
  imports: 10000
steps:
  - box_51: sales * 0.17
  - box_41: purchases * 0.17
  - box_42: imports * 0.17
  - box_61: box_41 + box_42
  - box_71: box_51 - box_61
expected:
  box_51: 8500.00
  box_61: 5100.00
  box_71: 3400.00
```

### Example 2: foreign consultancy and a blocked car cost (2026)

A Banja Luka company makes taxable sales of 30,000 KM net in May 2026. It buys goods from registered suppliers with 1,700 KM VAT. It hires a German consultant (no BiH tax representative) for 2,000 KM; consultancy is taxed where the customer is, so the company owes 17% itself. It pays that VAT on 28 May. The law allows payment up to 10 June (art. 39), but box 41 takes this VAT only in the month in which it is actually paid (UIO instructions 47/22, box 41), so paying in May puts it on the May return. It also buys fuel for a director's passenger car used privately as well, with 85 KM VAT.

- Box 51: 30,000 × 17% = 5,100 KM.
- VAT on the consultancy, paid by the company: 2,000 × 17% = 340 KM. Once paid it goes into box 41.
- Fuel VAT of 85 KM is blocked: the car is not used only for the business.
- Box 41: 1,700 + 340 = 2,040 KM. Box 71: 5,100 − 2,040 = 3,060 KM.
- Total paid to UIO: 3,060 + 340 = 3,400 KM. The 85 KM is a cost.

```oa-check
name: BiH VAT with foreign service and blocked fuel (2026)
inputs:
  sales: 30000
  domestic_input: 1700
  foreign_service: 2000
  blocked_fuel_vat: 85
steps:
  - box_51: sales * 0.17
  - reverse_vat: foreign_service * 0.17
  - box_41: domestic_input + reverse_vat
  - box_71: box_51 - box_41
  - total_paid: box_71 + reverse_vat
expected:
  box_51: 5100.00
  reverse_vat: 340.00
  box_41: 2040.00
  box_71: 3060.00
  total_paid: 3400.00
```

## Ask the client first

1. Turnover in 2025 and expected in 2026 (taxable plus exports), including related companies: is the business over 100,000 KM?
2. What does it sell, to whom (BiH businesses, consumers by entity, foreign customers), and are any supplies exempt (financial, insurance, residential lets, used property)?
3. Does it buy services from abroad, and do those suppliers have a BiH tax representative?
4. Does it import or export goods, and does it hold the customs documents?
5. Any cars, entertainment, staff housing or gifts in kind among the costs?
6. Any building work over 25,000 KM, new property sales, or equipment over 10,000 KM whose use may change?

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dodatu vrijednost, Službeni glasnik BiH 9/05 (base text), arts. 3 to 67 | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-Zakon_o_PDV-b.pdf | 2026-10-30 |
| VAT Law amendments 35/05 and 100/08 (UIO file labels are swapped; content checked) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-2-Zakon-izmjene-PDV-100-08.pdf | 2026-10-30 |
| VAT Law amendment 33/17 (art. 26 imports) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-3-Izmj-Zako-o-PDV-B-sl-glasnik-33-17.pdf | 2026-10-30 |
| VAT Law amendment 46/23 (food donations) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-4-D-Zakona-o-PDV-s-list-46-23-30-06-2023.pdf | 2026-10-30 |
| VAT Law amendment 80/23 (threshold 100,000 KM) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-5-Z-o-PDV-sl-list-80-23-24-11-23.pdf | 2026-10-30 |
| VAT Law amendment 20/25 (art. 54a first-home refund, art. 67 fine) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-6-Z-o-izmj-i-dop-Z-o-PDV-sl-list-20-25-04-04-2025.pdf | 2026-10-30 |
| Pravilnik o dopuni Pravilnika o primjeni Zakona o PDV, Službeni glasnik BiH 45/26 (art. 105a) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/2_Pravilnici/B/B-1-24-P-o-izmj-i-dop-Praviln-o-primj-Z-o-PDV-sl-list-45-26-30-06-2026.pdf | 2026-10-30 |
| Uputstvo za popunjavanje PDV prijave, Službeni glasnik BiH 47/22 | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/2_Pravilnici/B/B-1-2-Uputstvo-o-popunjavanju-PDV-prijave-Sglasnik-47-22-19-07-22.pdf | 2026-10-30 |
| Zakon o postupku indirektnog oporezivanja 89/05, arts. 9 to 11 | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/1_UIO/3_Zakon_o_postupku_indirektnog_oporeivanja/1_Zakon/B/B-1-Zakon-o-postupku-indirektnog-oporezivanja-Sluzbeni-glasnik-BiH-broj-8905.pdf | 2026-10-30 |
| Zakon o izmjenama Zakona o postupku indirektnog oporezivanja 100/13 (0.04%, 5%) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/1_UIO/3_Zakon_o_postupku_indirektnog_oporeivanja/1_Zakon/B/B-1-1-Zakon-o-izmjenama-Zakona-o-postupku-indirektnog-oporezivanja-Sluzbeni-glasnik-BiH-broj-10013.pdf | 2026-10-30 |
| Central Bank of BiH, notice on the official exchange rate (1 EUR = 1.95583 KM) | https://www.cbbh.ba/press/ShowNews/321?lang=en | 2026-10-30 |
| UIO, list of tax regulations | https://www.uino.gov.ba/portal/bs/propisi/porezi/ | 2026-10-30 |

Not yet confirmed: the consolidated VAT rulebook (93/05 to 25/25) beyond the 2026 first-home article, including invoice content and cash-register rules; the electronic supply and purchase records referred to in rulebook 45/26 (eIsporuke); the travellers' refund conditions (Instruction 48/25); the conditions for refunds to foreign businesses (PDV SL 1); the special schemes for travel agents, second-hand goods and auctions (arts. 46 to 51); the yearly farmers' flat-rate compensation; the average price per m² that sets the first-home cap; whether a later consolidated text of the VAT Law exists (the Parliament site was not read).

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
