---
name: eg-customs
description: "Egyptian customs tax for tax year 2026 under Customs Law No. 207 of 2020 and its executive regulations (Minister of Finance Decree 430 of 2021). Covers who pays and when, the customs value (transaction value plus costs to the Egyptian port, at the Central Bank rate on the declaration date), where to find the tariff rate, exemptions and the 5% rate for project equipment, the 1.5% monthly additional tax, declaration and release, transit, warehouses, temporary admission, temporary release, refunds, free zones and duty-free shops as far as the customs law reaches, fines, smuggling, grievance and arbitration. Trigger on: Egypt customs duty, Egyptian customs tax, الضريبة الجمركية, قانون الجمارك 207, customs value Egypt, temporary release Egypt, drawback Egypt, customs penalty Egypt. Out of scope: VAT on imports (egypt-vat), company tax (eg-corporate-tax), the tariff schedule itself."
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-21
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
category: international
type: computation
version: 1.0
---

# Egypt Customs Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Work out the Egyptian customs tax (الضريبة الجمركية) on goods brought into or taken out of Egypt in 2026, and the customs consequences of the special systems and of errors. The law is Customs Law No. 207 of 2020 (Official Gazette 45 bis (d), 11 November 2020, in force the next day under issuing art. 6), which repealed the Customs Law 66 of 1963 and the Customs Exemptions Law 186 of 1986 (issuing art. 5). Its executive regulations are Minister of Finance Decree 430 of 2021 (Al-Waqa'i' al-Misriya 193 (cont.), 31 August 2021). The Egyptian Customs Authority ("the Authority") applies both. Reply in the user's language, English or Arabic. Amounts are in EGP.

The law applies without prejudice to international agreements Egypt is party to (and agreements on electricity, petroleum and mining projects), customs exemptions in other laws, the Special Economic Zones Law 83 of 2002 and the Investment Law 72 of 2017 (issuing art. 1). Check those first where they could apply.

Out of scope: VAT on imports, which customs collects at release on the customs value plus customs tax (see `egypt-vat`); company income tax (`eg-corporate-tax`); free zone and investment incentives under the Investment Law; the tariff rates themselves, which you read from the official tariff for the HS code; import controls of other authorities (art. 58).

## Ask the client first

1. What are the goods, their HS code on the official tariff, their origin, and are they new or used?
2. The invoice and terms of sale: price paid or payable, currency, Incoterm, freight, insurance, commissions, royalties or licence fees tied to the goods, and is the seller related to the buyer (5% voting share and the other links in Regulations art. 35)?
3. Which system: final release for use, transit, customs warehouse, temporary admission for manufacture and re-export, temporary release (how long, for work or rent), or entry from a free zone or duty-free shop?
4. Does an exemption or the 5% rate apply (arts. 19 to 23), a trade agreement rate (certificate of origin), or is the importer a State entity (Law 159 of 2023)?
5. Is the importer in the Authority's customer register (art. 45), and who clears: the owner, a licensed clearing agent, or a public body's own staff (arts. 51, 55)?
6. Is there an open dispute, a short or excess quantity, a value challenge, or a notice of an offence?

## The method, step by step

### Key figures

| Item | Rate or amount | Conditions | Official URL |
|---|---|---|---|
| Additional tax on late customs tax | 1.5% of the unpaid customs tax a month | Each month or part of a month from the due date to payment (art. 1 item 22) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Reduced rate, project equipment | 5% of value, or the tariff rate if lower | Machinery, equipment, production lines and parts for setting up companies and listed projects (art. 22) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Reduced rate, tourist transport vehicles | 5% of value up to four hundred thousand Egyptian pounds a car | Private cars up to that value and vehicles for 10 or more people for licensed tourist transport companies; full tax above it (art. 23) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Temporary release, equipment for work or rent | 2% of the customs tax a month, at most 20% a year | Machinery, equipment, devices, containers, means of transport; not passenger cars or yachts (art. 34) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Temporary release, renewable energy equipment | 1% a month, at most 10% a year | New and renewable energy equipment, components and spare parts (art. 34) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Temporary release, passenger cars and yachts | Up to 5% of the tax a month | Exact figure set by the Regulations (art. 34) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Temporary admission period | One and a half years from release, plus up to one year | Re-export within the period or pay the taxes and additional tax (art. 33) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Related buyer and seller | 5% or more of voting shares | One of the links that test the transaction value (Regulations art. 35) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace474457860.pdf |
| Undervaluation fine trigger | Tax cut by more than 20% | Fine of half the customs tax at risk (art. 74) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |
| Records kept | Five years from release | Importers, exporters, agents, carriers (art. 8) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf |

### 1. Who pays and when the tax falls due [Customs Law arts. 1, 12, 50](https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf)

Goods entering Egypt bear the tax in the customs tariff plus the other taxes and duties due, unless a special text excepts them. Exports bear no customs tax unless the law says so. No goods are released before the customs procedures are finished and the customs tax and all other taxes and duties are paid, unless the law provides otherwise (art. 12). The goods owner or their clearing agent files a customs declaration for every consignment in or out, even when exempt; the signer answers for its accuracy, without prejudice to the owner's liability (art. 50). Customs tax, taxes, fees and other sums due to the treasury under the law rank ahead of all other debts except judicial costs (art. 85).

Late payment carries the additional tax: 1.5% of the unpaid customs tax for each month or part of a month from the due date to payment (art. 1 item 22).

### 2. The customs value [Customs Law art. 16; Regulations arts. 30 to 35](https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace474457860.pdf)

Subject to international agreements, the value of imported goods is their actual value plus all actual costs and expenses paid up to arrival at the port of destination in Egypt; the declaration must list the elements of value (art. 16). A value in foreign currency converts at the Central Bank of Egypt rate announced on the date the customs declaration is registered, or a rate the Minister sets by decree (art. 16). Exports are valued at price plus actual costs to the port of export on the declaration date, without other taxes and duties (art. 17).

Regulations art. 31 makes the transaction value (the contract price paid or payable) the first basis, and adds, where the buyer bears them and they are not in the price:
- commissions and brokerage, except buying commission; containers treated as one with the goods; packing, labour and materials;
- goods and services the buyer supplies free or at reduced cost for production: materials and components, tools, dies and moulds, materials consumed, and engineering, design, plans and drawings made outside Egypt;
- royalties and licence fees for patents, trademarks and copyright related to the goods that the importer must pay as a condition of sale;
- any part of the proceeds of resale or use that goes to the seller as a condition of sale;
- transport, handling, freight, insurance and unloading up to the port of arrival; if no freight or insurance document is shown, current comparable prices are used.

Additions must rest on objective, quantifiable data, and nothing else is added unless it is a condition of sale (art. 32). Left out, if shown separately: transport after import; Egyptian taxes and duties; assembly, maintenance and technical help after import; buying commission; marketing in Egypt; engineering and drawings done in Egypt; the right to reproduce the goods in Egypt; interest under a financing contract; dividends paid to the seller (art. 33).

The transaction value is accepted only if: no restriction on the buyer's use of the goods (other than restrictions set by Egyptian law or authorities, those with no effect on value, or limits on resale territory); no condition whose value cannot be measured; no undetermined share of resale proceeds to the seller; and no buyer and seller relationship that affects the price (art. 34). Persons are related if, among other links, one owns or controls 5% or more of the voting shares of the other, they are partners, employer and employee, under common control, or relatives to the fourth degree; a sole agent, distributor or franchisee is related if one of those tests is met (art. 35). Where the Authority doubts the declared value it tells the importer why and gives up to 15 days to justify it; if the reply does not satisfy it, or none comes, the customs office decides the accepted value (Regulations art. 38). If the transaction value cannot be used, the Regulations move through identical goods, similar goods, deductive value and computed value, as the WTO Customs Valuation Agreement does; read those articles before applying a fallback.

### 3. Classification and the rate [Customs Law arts. 13, 14; official tariff](https://www.customs.gov.eg/Services/Tarif)

The tariff's rules, categories and schedules are set by Presidential decree, which must go to the House of Representatives (art. 13). Read the rate for the HS code from the Authority's tariff service; do not quote a rate from memory or a third party. A new or amended tariff, or an agreement rate, applies from its entry into force to goods whose customs tax has not yet been paid (art. 13). Ad valorem tax is a percentage of the accepted customs value in the goods' condition when the tariff is applied; specific tax (per unit, number or weight) is due in full whatever the goods' condition, unless the Authority finds force majeure damage, when it may be reduced in proportion (art. 14). Disputes on type, origin or value go to grievance (step 7).

### 4. Exemptions and reduced rates [Customs Law arts. 19 to 24](https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf)

- **Full exemption without inspection** (art. 19): imports of the Ministry of Defence and the military, intelligence and interior bodies for armament, defence or security; and official-use goods of the Presidency, the Ministry of Foreign Affairs, the National Defence Council, the National Security Council and the Administrative Control Authority.
- **Full exemption with inspection** (art. 20), on Regulations conditions: grant-funded gifts, samples and goods of government bodies; passengers' personal effects; non-commercial personal items such as medals and awards; goods of Egyptian residents temporarily exported and brought back; free replacements of defective goods, up to the tax paid; goods exported and re-imported unchanged; supplies for ships and aircraft on foreign voyages; effects of returning scholarship holders and of Egyptian diplomats; foreign forces on reciprocity; imports of government and university hospitals named by ministerial decree; items and bodies exempted by Prime Minister decree.
- **Diplomatic** (art. 21): on reciprocity, for non-honorary diplomats and missions, with set car numbers.
- **5% of value, or the tariff rate if lower** (art. 22): machinery, equipment, devices, production lines and their parts needed to set up projects of joint stock, partnership limited by shares, limited liability and one-person companies, projects in new urban communities, and desert reclamation projects; construction machinery for reconstruction projects under Law 62 of 1974 (not passenger cars); equipment for hotel projects under Law 1 of 1973.
- **5% of value with inspection** (art. 23): private passenger cars up to EGP 400,000 and vehicles for ten or more people, needed to set up or expand licensed tourist transport companies; full tax on the value above EGP 400,000.
- **Conditions on every exemption** (art. 24): exempt or reduced-rate items may not be sold, transferred or used for another purpose for five years from release without the Authority's approval and payment of the customs tax and other taxes; all tax is recovered if the items are not used for the exempt purpose, unless force majeure stops the use; exempt tobacco and alcohol need the exemption mark; "means of transport" excludes passenger cars unless stated; exempt bodies keep books open to the Authority. Art. 24 does not apply to art. 20 items 1 to 10.
- **State entities:** customs tax exemptions given to State entities no longer cover their economic or investment activities (Law 159 of 2023; PM Decree 242 of 2024 art. 1 names customs tax). See `eg-corporate-tax` for who counts and what stays exempt.

### 5. Declaration, inspection and release [Customs Law arts. 39, 45 to 47, 50 to 53, 59 to 61](https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf)

1. **Register.** The importer or exporter must be in the Authority's customer register before procedures or release (art. 45); personal imports are outside it. Carriers may not ship goods (other than personal items) for importers not in the register (art. 46).
2. **Advance registration.** The importer sends the shipping documents to the Authority before shipment to get a preliminary customs registration number, which must appear on the shipping documents; goods arriving without it are re-shipped out unloaded at the carrier's cost (art. 39). The importer may clear in advance and pay estimated taxes before arrival, with a final settlement at the tariff in force at release (art. 39).
3. **Manifest.** The carrier files the cargo information and manifest at least 48 hours before arrival (art. 47).
4. **Declaration.** The owner or a licensed clearing agent files the declaration (art. 50). Clearing for third parties needs a two-year renewable licence (art. 51). A clearing office deposits EGP 50,000 cash security, a licensed legal person EGP 100,000 (art. 53). Public bodies, companies, embassies and consulates may clear their own goods through trained staff with written authority (art. 55). The Authority may accept an incomplete declaration with a guarantee before release (art. 50).
5. **Inspection.** The Authority inspects all or part of the goods at the customs office (outside it at the owner's request and cost) and may re-inspect until final release (art. 59). Samples may be analysed at the owner's cost, with a repeat analysis on objection (art. 61).
6. **Pay and release.** Pay the customs tax, VAT and other charges; then release (art. 12). Machinery, equipment, production lines and parts for production projects, with no exemption or reduction, may pay the customs tax by instalments over up to one year with the additional tax for each month or part; State national or infrastructure projects named by Prime Minister decree are spared the additional tax (art. 15).
7. **Keep records** for five years from release (art. 8). The Authority may audit after clearance at the trader's premises (art. 9) and recompute taxes where they rested on fraud.

### 6. Special customs systems [Customs Law arts. 25 to 38](https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf)

| System | Rule | Article |
|---|---|---|
| Transit | Foreign goods move under guarantee; tax is computed on the date the guarantee is lodged; the carrier answers for loss, shortage or broken seals | 25 |
| Customs warehouse | Licensed by the Minister; tax paid on final release, on quantities at deposit; licensee pays on unexplained shortage, not on natural loss or force majeure | 26, 27 |
| Temporary storage | Goods stay in licensed port storage until procedures end | 28 |
| Free zones | Licensed by GAFI after consulting the Authority (15 working days' silence is consent); the Authority may inventory and reconcile balances. Free zone tax rules sit in the Investment Law, not here | 29 |
| Special economic zones | The zone body notifies the Authority; activity starts after a ministerial decree treating the area as a customs office | 30 |
| Duty-free shops (الأسواق الحرة) | Licensed by the Minister; goods released from them into Egypt pay customs tax and other taxes under the rules in force on the date of sale | 31, 32 |
| Temporary admission | Raw materials, intermediate goods and components for manufacture, packing for exports, and goods for repair or completion, then re-export, are suspended against a guarantee equal to the taxes; re-export within one and a half years from release, extendable by up to one year; after that the taxes and the additional tax are due. Guarantees are released pro rata for exports, sales to free zones or SEZs, or sales to fully exempt bodies | 33 |
| Temporary release | Payment suspended against a guarantee. Machinery, equipment, devices, containers and means of transport (not passenger cars or yachts) for work or rent in Egypt: 2% of the customs tax due on the temporary release date for each month or part, capped at 20% a year, until re-export or final release. New and renewable energy equipment and spare parts: 1% a month, capped at 10% a year. Passenger cars and yachts: up to 5% a month, set by the Regulations. On final release, the percentage paid for the month of final release is deducted from the customs tax | 34 |
| Rate on special systems | Goods under temporary admission or release bear the tax in force on the date the declaration is registered; final release only after import rules are met | 35 |
| Refund (drawback) | Customs tax and other taxes paid on imported materials used to make local products that are exported, sent to a free zone or SEZ, or sold to fully exempt bodies within one and a half years from release (extendable one year) are refunded; partial refunds for sales to partly exempt bodies | 36 |
| Re-export refunds | Tax on imported foreign goods with no local equivalent, re-exported unchanged within one year of payment, and on goods wholly rejected and re-exported within one year, is refunded | 37 |
| Re-import of exports | Customs tax paid on exported local goods is refunded if they come back unchanged or are withdrawn from a free zone or SEZ | 38 |

### 7. Grievance, arbitration and time limits [Customs Law arts. 57, 63 to 65](https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf)

A dispute on the type, origin or value of goods goes first to a grievance committee of the Authority. It decides within seven working days with reasons; if the trader accepts within seven days of notice, a record is made and the Authority must carry it out (art. 63). If the dispute continues, the trader may ask for arbitration and, with the Minister's approval, a three-member board (chaired by a judge of at least counsellor rank or a listed law professor) gives a final, binding decision, open to challenge only as the Arbitration Law 27 of 1994 allows (art. 64). The goods stay under customs control during grievance or arbitration, except as the Regulations allow (art. 65). A clearing agent may appeal a disciplinary decision within 30 days of learning of it; the supreme grievance committee decides within 15 days (art. 57).

### 8. Offences, fines and smuggling [Customs Law arts. 71 to 82](https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf)

| Offence | Fine | Article |
|---|---|---|
| Carrier: manifest not filed or late, wrong or missing entries, unauthorised docking, landing or departure, unloading outside set places | EGP 30,000 | 71 |
| Wrong data in the declaration with no tax at risk; clearing agent breaches; seals not kept without loss; obstructing officers; breach of rules with tax at risk up to EGP 30,000 | EGP 10,000 | 72 |
| Unjustified shortage against the manifest by negligence | Half the customs tax at risk, plus the taxes due | 73 |
| Unjustified excess, or excess found on inventory of storage, warehouses, free zones, SEZs or duty-free shops | Half the customs tax on the excess | 73 |
| Wrong data on type or origin; breach of the rules of transit, warehouses, free zones, SEZs, duty-free shops, temporary admission, temporary release or exemptions | Equal to the customs tax at risk | 74 |
| Declared value that cuts the customs tax by more than 20% | Half the customs tax at risk (the Authority applies the Valuation Agreement) | 74 |
| Breach of record keeping (art. 8) or of exemption conditions (art. 24 items 2 and 5), or refusing documents | Equal to the customs tax | 75 |
| Blocking a post-clearance audit | EGP 20,000 each refusal, unless excused | 75 |

Fines are imposed by criminal order on the Authority's written request; a legal person is jointly liable where the offence was in its name. The Authority may settle arts. 71 to 75 offences for half the fine before referral to the Public Prosecution, or the full fine after referral and before a final order; settlement ends the case (art. 76).

Smuggling is bringing goods in or out by unlawful means without paying all or part of the customs tax, or against the rules on prohibited goods (art. 1 item 33). Art. 77 lists acts treated as smuggling, among them false or forged documents or invoices, removing marks, unexplained loss of transit or warehoused goods, selling goods released under a special system or exemption without approval and payment, fictitious exports to obtain refunds, and any other act aimed at evading customs tax. Penalties (art. 78): imprisonment and a fine of EGP 10,000 to 100,000, or either; for trade, imprisonment of three to five years and a fine of EGP 25,000 to 250,000, or either; in every case joint compensation of twice the customs tax evaded; for prohibited goods two to five years and compensation of twice the value or twice the tax, whichever is more, with confiscation; compensation doubles on a repeat within five years. The same applies to refunds obtained by fraud, with compensation of twice the amount (art. 79). A smuggling case needs the Minister's written request; the Minister may settle up to 60 days after a final judgment for the full compensation, which ends the case (art. 81).

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Goods from abroad into a free zone | Customs control and inventory only under the Customs Law; tax and duty status under the Investment Law | Customs Law issuing art. 1, art. 29 |
| Goods from a free zone into Egypt | Treated as an import: customs tax and VAT on release | Customs Law art. 12; `egypt-vat` |
| VAT on imports | Base is the customs value plus customs tax and other charges; collected at customs before final release | `egypt-vat` (VAT Law arts. 10(7), 31) |
| Equipment brought in for a contract and taken out again | Temporary release at 2% a month capped at 20% a year, or temporary admission if it is processed and re-exported | Arts. 33, 34 |
| Undervaluation of more than 20% | Fine of half the tax at risk, plus the tax; if documents were false, smuggling | Arts. 74, 77 |
| Exempt item sold within five years | Needs approval and payment of all taxes; otherwise smuggling | Arts. 24, 77 item 9 |
| State-owned company importing for a commercial activity | No State-entity exemption; normal tax | Law 159 of 2023; Decree 242 of 2024 |
| Goods left in storage past the permitted time | Sold by the Authority; the balance after costs, taxes and charges is held five years for the owner | Arts. 66, 69 |

## Worked cases

All amounts are hypothetical inputs. The tariff rate and the exchange rate below are assumptions for the arithmetic, not 2026 figures: read the rate from the tariff and the rate of exchange from the Central Bank on the declaration date.

### Case 1: import, customs value and late payment

A company imports machinery parts: price USD 50,000 FOB, freight USD 3,000, insurance USD 500, buying commission USD 1,000 paid to its own agent. Assumed exchange rate EGP 50.00 per USD on the declaration date and an assumed tariff rate of 10%. Buying commission stays out of the value (Regulations art. 33); freight and insurance to the Egyptian port go in (art. 31). Customs value is USD 53,500, so EGP 2,675,000; customs tax EGP 267,500. The tax is paid 2 months and 10 days late: three months or parts of a month, so the additional tax is 1.5% x 3 = 4.5%, EGP 12,037.50.

```oa-check
name: Customs value and additional tax for late payment
inputs:
  price_usd: 50000
  freight_usd: 3000
  insurance_usd: 500
  buying_commission_usd: 1000
  fx: 50
  tariff_rate: 0.10
  months_late: 3
steps:
  value_usd: price_usd + freight_usd + insurance_usd
  customs_value: value_usd * fx
  customs_tax: customs_value * tariff_rate
  additional_tax: customs_tax * 0.015 * months_late
expected:
  value_usd: 53500
  customs_value: 2675000
  customs_tax: 267500
  additional_tax: 12037.50
```

### Case 2: decision, temporary release or final release for rented equipment

A contractor brings in construction equipment to rent out in Egypt. The customs tax due on the temporary release date is EGP 800,000 (assumed). Under temporary release it pays 2% a month (art. 34). If the equipment leaves after 8 months, the cost is 16%, EGP 128,000. If it stays 14 months, the first year is capped at 20% (EGP 160,000) and months 13 and 14 add 4% (EGP 32,000): EGP 192,000. If after 8 months the contractor decides to keep it, final release costs the full EGP 800,000 less the 2% paid for the month of final release (EGP 16,000), so EGP 784,000, on top of the EGP 128,000 already paid: EGP 912,000, which is EGP 112,000 more than paying EGP 800,000 on final release at the start. The figure that decides is the expected stay: short and certain, temporary release; likely to stay, final release up front.

```oa-check
name: Temporary release cost against final release
inputs:
  customs_tax: 800000
  monthly: 0.02
  annual_cap: 0.20
steps:
  eight_months: customs_tax * monthly * 8
  first_year: customs_tax * min(monthly * 12, annual_cap)
  fourteen_months: first_year + customs_tax * monthly * 2
  final_after_eight: customs_tax - customs_tax * monthly
  total_if_kept: eight_months + final_after_eight
  extra_cost_of_waiting: total_if_kept - customs_tax
expected:
  eight_months: 128000
  first_year: 160000
  fourteen_months: 192000
  final_after_eight: 784000
  total_if_kept: 912000
  extra_cost_of_waiting: 112000
```

## When to refuse or refer

- Refer to a licensed clearing agent or customs lawyer: classification disputes, a value challenge beyond the 15-day reply, grievance and arbitration (arts. 63, 64), and any notice of smuggling (arts. 77 to 81), which can lead to prison.
- Do not help undervalue goods, split invoices, misdescribe goods or origin, or move exempt goods to a new use without approval: these are offences under arts. 74 and 77.
- Do not quote a tariff rate without reading the official tariff for the HS code on the date of release.
- Free zone, special economic zone and Investment Law project incentives: refer to those laws; this skill covers only the customs law side.
- Rules from the executive regulations other than arts. 30 to 35 and 38 were not read for this version: say so and check the Regulations before applying procedure detail.

## Sources

| Source | URL | Read on |
|---|---|---|
| Customs Law No. 207 of 2020, consolidated Arabic text "with all amendments", October 2024 compilation published by the Egyptian Customs Authority, Gazette 45 bis (d), 11 Nov 2020 (OCR of all pages; page images of arts. 21, 22, 34, 53, 72, 74 to 76 read) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace159396001.pdf | 2026-11-21 |
| Customs Law No. 207 of 2020, English translation published by the Egyptian Customs Authority (arts. 1 to 92 read; checked against the Arabic for every figure used) | https://www.customs.gov.eg/Upload/ECAAdminace/62f62698-1dd6-4320-a68b-75433f639fb4.pdf | 2026-11-21 |
| Executive Regulations, Minister of Finance Decree 430 of 2021, consolidated Arabic text published by the Authority, Al-Waqa'i' al-Misriya 193 (cont.), 31 Aug 2021: arts. 30 to 35 and 38 (page images and OCR of pp. 20 to 25 read) | https://www.customs.gov.eg/Upload/ECAAdminace/ECAAdminace474457860.pdf | 2026-11-21 |
| Executive Regulations, English translation of the draft of 25 May 2021 published by the Authority (used only to locate articles; the Arabic decree text governs) | https://www.customs.gov.eg/Upload/ECAAdminace/2c2777f7-499b-4ce9-8171-78deb005de42.pdf | 2026-11-21 |
| Egyptian Customs Authority tariff service (read for the import and export tariff search by chapter) | https://www.customs.gov.eg/Services/Tarif | 2026-11-21 |
| Egyptian Customs Authority laws and regulations lists (read for the links to the texts above) | https://www.customs.gov.eg/Legislations/Manshorat?categoryId=2 | 2026-11-21 |
| PM Decree 242 of 2024, executive regulations of Law 159 of 2023, art. 1 (customs tax among the taxes concerned). manshurat.org (private legal database; official gazette copy not reachable) | https://manshurat.org/sites/default/files/ldd_5_mkrr_-_mwmn-swr-2.pdf | 2026-11-21 |

Not yet confirmed: whether Law 207 of 2020 was amended after the October 2024 compilation (no amending law was found on the Authority's list; the compilation shows only instructions and decrees as notes). The executive regulation articles other than 30 to 35 and 38, including the fallback valuation methods, temporary admission and release guarantees and periods, drawback procedure, warehouse and storage periods, instalment conditions and the clearing agent rules; the English regulations are a draft of 25 May 2021 and its numbering after art. 38 was not checked against the decree. The limitation period for customs tax claims and refund claims (none was found in Law 207 of 2020). The current tariff decree number and the 2026 rates. The service charges schedule (art. 18 caps each charge at EGP 10,000; the schedule in the Regulations was not read). Treatment of e-commerce consignments and postal parcels beyond arts. 44 and 87.
