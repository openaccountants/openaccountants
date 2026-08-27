---
name: sa-excise-tax
description: Use this skill whenever asked about Saudi Arabia Excise Tax. Trigger on phrases like "Saudi excise tax", "ZATCA excise", "Saudi sin tax", "tobacco tax Saudi", "energy drinks Saudi excise", "soft drinks excise Saudi", "sweetened drinks Saudi", "e-cigarette tax Saudi", "vape tax KSA", "Royal Decree A/86", "GCC excise", "excise tax warehouse Saudi", "excise registration ZATCA", or any question about computing, registering, filing, or reporting Saudi excise tax obligations on tobacco, energy drinks, soft drinks, sweetened drinks, or electronic smoking devices. Scope covers the Excise Tax Law issued by Royal Decree A/86 of 27/8/1438H (2017) and the Excise Tax Bylaws, the taxable product list and rates, the tax base (higher of retail selling price or ZATCA standard price), tax warehouse regime, importer/manufacturer registration, monthly filing through the ZATCA portal, penalties, and GCC harmonisation context. ALWAYS read this skill before touching any Saudi excise tax work.
jurisdiction: SA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mehran Habib
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SA Excise Tax

## Saudi Arabia — Excise Tax — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mehran Habib** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Excise Tax

- **Tobacco and tobacco products** — 100%  _(Chapter two Article 3 Rates - Implementing Regulation of Excise Tax Law)_
- **Energy drinks** — 100%  _(Chapter two Article 3 Rates - Implementing Regulation of Excise Tax Law)_
- **Soft drinks (carbonated)** — 50%  _(Chapter two Article 3 Rates - Implementing Regulation of Excise Tax Law)_
- **Sweetened drinks + Distilled beverages (energy drinks still 100%)** — 0.5  _(Chapter two Article 3 Rates - Implementing Regulation of Excise Tax Law)_
- **E-cigarettes / vape devices** — 100%  _(Chapter two Article 3 Rates - Implementing Regulation of Excise Tax Law)_
- **E-liquids** — 100%  _(Chapter two Article 3 Rates - Implementing Regulation of Excise Tax Law)_
- **Tax base** — Higher of declared RSP or ZATCA standard price  _(Definition - Tax Base - Implementing Regulations of Excise Tax Law)_
- **Filing** — Monthly; due within 15 days of month-end  _(Article 16(1) Tax Return - Implementing Regulation of Excise Tax Law)_

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Kingdom of Saudi Arabia (KSA) |
| Tax | Excise Tax (selective tax / ضريبة انتقائية) |
| Currency | SAR (Saudi Riyal) |
| Primary legislation | Excise Tax Law — Royal Decree No. A/86 dated 27/8/1438H (corresponding to 2017) |
| Secondary legislation | Excise Tax Implementing Regulations / Bylaws (issued by ZATCA, as amended) |
| GCC framework | Common GCC Excise Tax Agreement (signed 2016) — KSA was an early adopter |
| Tax authority | Zakat, Tax and Customs Authority (ZATCA) |
| Tax base | Higher of (a) retail selling price declared by the taxpayer or (b) "standard price" published by ZATCA for the product |
| Filing frequency | Monthly excise return via ZATCA e-portal |
| Filing & payment deadline | Within 15 days of month-end (verify against current ZATCA bylaw — historically the 15th of the following month) |
| Validated by | Pending — requires sign-off by a Saudi licensed tax practitioner (SOCPA member) |
| Skill version | 1.0 |

### Taxable products and rates at a glance

**Taxable products and rates at a glance**

| Product class | Rate | Effective from | Notes |
| --- | --- | --- | --- |
| Tobacco and tobacco products | **100%** | June 2017 | Cigarettes, cigars, shisha, smokeless tobacco, heated tobacco products |
| Energy drinks | **100%** | June 2017 | Caffeinated beverages marketed for energy/stimulation |
| Soft drinks (carbonated) | **50%** | June 2017 | Carbonated drinks excluding unflavoured carbonated water |
| Sweetened drinks | **50%** | December 2019 | Added sugar or sweetener: flavoured milk, sweetened juices, sweetened iced tea, sweetened flavoured water |
| Electronic smoking devices and tools | **100%** | May/June 2019 | Vapes, e-cigarettes, heat-not-burn devices |
| Liquids used in electronic smoking devices | **100%** | May/June 2019 | Vape liquids / e-liquids, with or without nicotine |

## Section 2 — Required inputs & refusal catalogue

### Required inputs

Before computing any Saudi excise tax position, obtain:

1. **Taxpayer identity** — legal name, Commercial Registration (CR) number, ZATCA Tax Identification Number (TIN), and excise tax registration number.
2. **Role in the supply chain** — importer, local manufacturer, warehouse keeper / holder of unreleased excise goods.
3. **Product list** — for each SKU: HS code, product class (tobacco, energy drink, soft drink, sweetened drink, ESD, e-liquid), pack size, declared retail selling price (SAR), unit count per pack and per consignment.
4. **ZATCA standard price** — published "standard price" (السعر القياسي) for the product, if any.
5. **Import documentation** — bill of lading, customs declaration, country of origin, value, quantity, and customs duty paid.
6. **Manufacturing data** — production volumes, releases into consumption from a tax warehouse, internal transfers between licensed warehouses.
7. **Tax warehouse licence status** — copy of the ZATCA tax warehouse licence (if any), inventory records, opening and closing stock by SKU.
8. **Period under review** — calendar month for which the return is being prepared.
9. **Prior period adjustments** — credit notes, returns, damaged stock disposed of under ZATCA supervision.

### Refusal catalogue

STOP and do not produce a final excise tax figure where any of the following applies:

- **Taxpayer not registered for excise tax but is importing or manufacturing excise goods** — Registration is a precondition — instruct the taxpayer to register before filing; do not produce a return for an unregistered person
- **Product classification uncertain (e.g. drink that may or may not qualify as "sweetened")** — Obtain ZATCA classification ruling before computing
- **Mixed consignment containing both excise and non-excise goods with no SKU-level breakdown** — Cannot apportion the tax base reliably
- **ZATCA standard price not published for the product and no documented retail selling price** — Cannot determine the tax base
- **Tax warehouse inventory reconciliation shows unexplained variances** — Investigate before filing — variances may indicate unreported releases
- **Goods released into a GCC member state under intra-GCC transfer rules** — Cross-border GCC excise mechanics may apply — verify with ZATCA and the destination state's authority
- **Customs clearance was effected before excise registration** — Retrospective registration / penalty exposure — refer to specialist
- **Damaged or destroyed stock not disposed of under ZATCA supervision** — Conservative default: treat as released into consumption and tax
- **2024-2025 scope expansion to additional sugar-containing items** — **Verify current scope against latest ZATCA circular** before excluding any item

## Section 3 — Tier 1 — taxable products and rates

### 3.1 Statutory basis

The Excise Tax Law was issued by **Royal Decree No. A/86 dated 27/8/1438H** (corresponding to 2017) and is administered by **ZATCA** (Zakat, Tax and Customs Authority — formed in 2021 from the merger of GAZT and the General Customs Authority). The Excise Tax Bylaws / Implementing Regulations set out the procedural rules, registration mechanics, tax warehouse regime, return format and payment timing.

The KSA regime sits inside the **Common GCC Excise Tax Agreement** (2016), under which member states agreed a harmonised list of "selective goods" (tobacco, energy drinks, carbonated soft drinks) and a common framework for cross-border movement and rate alignment. Individual member states may vary rates and add products at the national level — Saudi Arabia has added sweetened drinks (2019) and electronic smoking devices (2019).

### 3.2 Taxable products and rates

The current Saudi excise list comprises six product groupings:

#### Tobacco and tobacco products — 100%

- **Tobacco and tobacco products** — Covers all forms of tobacco prepared for consumption: cigarettes, cigars, cigarillos, shisha (mu'assel / hookah tobacco), smokeless tobacco (chewing, snuff), pipe tobacco, and heated tobacco products (HTPs, including the heat sticks used in IQOS-style devices). The 100% rate applies to the tax base (see §3.3).

#### Energy drinks — 100%

- **Energy drinks** — A beverage marketed or sold as an energy drink, generally containing stimulant compounds (caffeine, taurine, ginseng, guarana). Classification follows the labelling and marketing of the product, not merely the caffeine content — a coffee-style RTD is not automatically an energy drink. Refer to ZATCA's published guidance on classification borderline cases.

#### Soft drinks (carbonated) — 50%

- **Soft drinks (carbonated)** — Any **carbonated** drink excluding unflavoured carbonated water (sparkling water without added flavour or sweetener). This includes traditional colas, lemon-lime, ginger sodas, tonic water, and carbonated fruit-flavoured drinks. Concentrates, powders, and extracts intended to be reconstituted into a carbonated drink are also caught.

#### Sweetened drinks — 50% (added December 2019)

- **Sweetened drinks** — Any beverage to which **sugar or any sweetener** (including artificial sweeteners and natural sweeteners such as honey or fruit concentrate added beyond what is required as a natural component) has been added. Catches: - Flavoured milk and milk-substitute drinks. - Sweetened juice drinks and nectars (typically those below the 100% pure juice threshold). - Sweetened iced teas and coffee-based RTDs. - Sweetened flavoured water. - Concentrates, powders, gels, and extracts used to prepare a sweetened drink. The 100% pure unsweetened juice and unsweetened milk are typically **out of scope**, but borderline cases (e.g. juices labelled "no added sugar" that contain concentrated juice as sweetener) need ZATCA guidance.

#### Electronic smoking devices and tools — 100% (since 2019)

- **Electronic smoking devices and tools** — E-cigarettes, vapes, vape pens, pods, atomisers, batteries sold as part of a smoking device, and other tools designed for electronic smoking. Devices that are not designed for nicotine or tobacco consumption (e.g. nebulisers for medical use) are out of scope.

#### Liquids used in electronic smoking devices — 100% (since 2019)

- **Liquids used in electronic smoking devices** — E-liquids (with or without nicotine), pods pre-filled with e-liquid, and refill bottles.

### 3.3 Tax base — higher of retail selling price or ZATCA standard price

- **Excise tax payable formula** — Excise tax payable = max(RSP, ZATCA standard price) × rate
- **Tax base definition** — The tax base for each taxable product is the higher of: (1) the retail selling price (RSP) declared by the importer / manufacturer — the price at which the product is offered for sale to the final consumer in KSA, inclusive of all taxes other than excise tax but exclusive of VAT; or (2) the standard price (السعر القياسي) published by ZATCA for that product or product category. The standard price exists to prevent under-declaration of the RSP. Where ZATCA has not published a standard price, the declared RSP applies, but the taxpayer must be able to substantiate it.

### 3.4 Persons liable to tax

- **Persons liable to tax** — Excise tax is payable by: - **Importers** — on importation of excise goods into KSA, at the point of customs release. - **Local manufacturers** — on release of excise goods from the production facility into consumption. - **Holders of excise goods in a tax warehouse** — on release from the warehouse into consumption (intra-warehouse transfers and exports do not trigger the tax). - **Persons who acquire excise goods on which tax has not been paid** — secondary liability where the primary taxpayer has failed to discharge the tax.

### 3.5 Tax point (chargeability)

- **Tax point (chargeability)** — Tax becomes chargeable at the earliest of: - Import into KSA (customs release date). - Release from a tax warehouse into consumption. - Production within KSA outside a tax warehouse (i.e. by an unlicensed manufacturer — also a registration breach). - Discovery of excise goods in free circulation on which tax has not been paid.

## Section 4 — Tier 2 — registration, tax warehouses, scope expansions

### 4.1 Registration

- **Registration** — Any person who imports, produces, holds in a tax warehouse, or otherwise deals in excise goods in the course of business must register with ZATCA for excise tax before undertaking any such activity. Registration is effected through the ZATCA e-portal. Required information includes: - Commercial Registration certificate. - TIN / VAT registration number (if separately VAT-registered). - Description of business activity and the excise product classes handled. - Customs importer code (for importers). - Tax warehouse licence (if applying simultaneously for a tax warehouse — see §4.2). - Financial guarantee / bank guarantee where required by ZATCA (typically for tax warehouse keepers). Failure to register before commencing taxable activity is a separate infringement and triggers penalties in addition to the tax on the underlying goods.

### 4.2 Tax warehouse regime

- **Tax warehouse regime** — A tax warehouse (مستودع ضريبي) is a place licensed by ZATCA where excise goods may be produced, processed, held, received, or dispatched under suspension of excise tax. The tax warehouse regime is the principal mechanism by which importers and manufacturers manage cash-flow on excise stock. Key features: - **Suspension of tax** — excise goods held in a licensed tax warehouse are not yet chargeable; tax becomes due only on release into consumption. - **Intra-warehouse movements** — movements between two licensed tax warehouses (whether of the same operator or between different licensees) are under suspension provided documented controls are met. - **Exports** — goods exported from a tax warehouse out of KSA are not subject to excise tax. Documentary evidence of export is required. - **Inventory controls** — the warehouse keeper must maintain real-time inventory records by SKU, reconcile physical to book stock at month-end, and report movements to ZATCA in the form prescribed by the Bylaws. - **Financial guarantee** — ZATCA may require a bank guarantee covering a multiple of the average monthly excise tax liability of the warehouse. - **Licence conditions** — the warehouse keeper must be a registered excise taxpayer in good standing, hold a Saudi CR, and meet physical security and record-keeping requirements set by ZATCA. Operating a place as a tax warehouse without a licence is an offence; goods may be seized and penalties applied.

### 4.3 Electronic smoking devices and e-liquids (2019 expansion)

- **Electronic smoking devices and e-liquids (2019 expansion)** — In May/June 2019, KSA extended excise tax to: - **Electronic smoking devices** (vapes, e-cigarettes, heat-not-burn devices) — **100%**. - **Liquids used in electronic smoking devices** (e-liquids, with or without nicotine) — **100%**. This brought vaping products into line with combustible tobacco (also 100%). Importers and manufacturers of these products needed to register and observe the standard excise mechanics from the effective date. Standard prices for e-liquids and devices are published by ZATCA.

### 4.4 Sweetened drinks (December 2019 expansion)

- **Sweetened drinks (December 2019 expansion)** — Effective 1 December 2019, KSA extended excise tax to sweetened drinks at 50%. Sweetened drinks are defined to include any beverage (other than 100% pure unsweetened juice and unsweetened milk) to which sugar or any other sweetener has been added, plus concentrates, powders, gels, and extracts intended to make a sweetened drink. This expanded the tax base significantly: flavoured milks, sweetened iced teas, sweetened juice drinks, sweetened flavoured waters, and many RTD coffee products were brought into charge for the first time.

### 4.5 2024-2025 — possible further scope expansions

In 2024-2025 there has been public-policy discussion of expanding excise tax to additional sugar-containing food items (not just drinks) and of revisiting the rates. As of the date of this skill, no statutory expansion beyond the six product classes above has taken effect, but practitioners should verify the current ZATCA product list and rates against the latest ZATCA circular and Royal Decree amendments before producing a final excise return — particularly where the engagement involves a confectionery, dairy, or composite food product that might be brought into scope by a 2025 or 2026 amendment.

### 4.6 GCC harmonisation context

Saudi rates are aligned with the GCC Excise Tax Agreement of 2016, but individual GCC member states have implemented at different speeds and with national variations:

- UAE introduced excise in October 2017 with the same headline rates (100%/100%/50%).
- Bahrain followed in December 2017.
- Oman in 2019.
- Qatar in 2019.
- Kuwait — not yet implemented as at skill publication.

For cross-border movements within the GCC, taxpayers should observe both the KSA Excise Tax Law and the destination state's regime; intra-GCC mechanics are not standardised in practice and may require case-by-case ZATCA confirmation.

## Section 5 — Worked examples

### Example A — Tobacco importer (cigarettes)

A KSA-resident company, "Riyadh Tobacco Imports LLC", imports a consignment of 1,000,000 cigarettes (50,000 packs of 20 cigarettes each) in October 2025. The declared retail selling price per pack is SAR 25. ZATCA's published standard price for the brand is SAR 24 per pack. The company is registered for excise tax and holds a tax warehouse licence; the goods are placed into the licensed warehouse on arrival and released into consumption progressively over the month.

**Step 1 — Determine the tax base per pack**

| Element | Amount (SAR) |
| --- | --- |
| Declared RSP per pack | 25.00 |
| ZATCA standard price per pack | 24.00 |
| Tax base (higher of the two) | **25.00** |

**Step 2 — Compute excise per pack**

| Element | Amount (SAR) |
| --- | --- |
| Tax base | 25.00 |
| Rate | 100% |
| Excise per pack | **25.00** |

Assume 40,000 packs released into consumption (the remaining 10,000 packs remain in the tax warehouse at month-end).

**Step 3 — Apply to releases into consumption during October 2025**

| Element | Amount (SAR) |
| --- | --- |
| Packs released | 40,000 |
| Excise per pack | 25.00 |
| **Excise tax liability — October 2025** | **1,000,000** |

The remaining 10,000 packs in the warehouse are not yet chargeable. They will be taxed when released into consumption in a future period (or zero-rated if exported).

The October return is filed via ZATCA within 15 days of month-end (verify against the current Bylaw); payment is due at the same time.

### Example B — Soft drink manufacturer (carbonated cola)

"Jeddah Beverages Co." manufactures a carbonated cola in 330ml cans. RSP is SAR 2.00 per can; ZATCA standard price is SAR 1.80 per can. In November 2025 the manufacturer releases 5,000,000 cans into consumption from its licensed production facility (which is also a tax warehouse).

**Step 1 — Tax base per can**

| Element | Amount (SAR) |
| --- | --- |
| Declared RSP per can | 2.00 |
| ZATCA standard price per can | 1.80 |
| Tax base (higher) | **2.00** |

**Step 2 — Excise per can**

| Element | Amount (SAR) |
| --- | --- |
| Tax base | 2.00 |
| Rate (carbonated soft drink) | 50% |
| Excise per can | **1.00** |

**Step 3 — November 2025 liability**

| Element | Amount (SAR) |
| --- | --- |
| Cans released | 5,000,000 |
| Excise per can | 1.00 |
| **Excise tax liability — November 2025** | **5,000,000** |

VAT at 15% is then chargeable on a base that includes the excise tax (excise feeds into the VAT base) when the goods are sold downstream — this is handled by the VAT skill, not here.

### Example C — Sweetened drink (flavoured milk)

"Dammam Dairy" produces a 250ml chocolate-flavoured milk drink. Sugar is added during production. RSP is SAR 3.00; ZATCA has not yet published a standard price for this exact SKU. In December 2025 the company releases 2,000,000 units into consumption.

The drink contains added sugar and is not 100% pure unsweetened milk → falls within the sweetened drinks category → 50% rate.

Since no standard price is published, the declared RSP applies; the taxpayer must be able to substantiate the SAR 3.00 RSP from price lists, retail invoices, or commercial agreements.

**Step 2 table**

| Element | Amount (SAR) |
| --- | --- |
| RSP per unit | 3.00 |
| Rate | 50% |
| Excise per unit | **1.50** |

**Step 3 — December 2025 liability**

| Element | Amount (SAR) |
| --- | --- |
| Units released | 2,000,000 |
| Excise per unit | 1.50 |
| **Excise tax liability — December 2025** | **3,000,000** |

If ZATCA later publishes a standard price for this SKU that is higher than SAR 3.00, the higher figure becomes the tax base from the effective date of publication.

## Section 6 — Filing & payment

### 6.1 Monthly excise return via ZATCA portal

- **Monthly excise return via ZATCA portal** — Excise tax is filed monthly through the ZATCA e-portal. The return covers all releases into consumption during the calendar month, by product class and SKU, and reports: - Opening stock in each tax warehouse, by SKU. - Production (for manufacturers) and imports (for importers) during the month. - Movements under suspension between licensed warehouses. - Releases into consumption (the taxable event). - Exports (zero-rated). - Damaged / destroyed stock disposed of under ZATCA supervision (zero-rated). - Closing stock in each tax warehouse, by SKU. - Excise tax payable, by product class.

### 6.2 Filing & payment deadline

- **Filing & payment deadline** — The return and payment are due within 15 days of the end of the month to which they relate (historically the 15th of the following month). Verify against the current ZATCA Bylaw / circular before relying on a specific date — ZATCA has from time to time amended administrative timing.

### 6.3 Payment channels

- **Payment channels** — Payment is made through the ZATCA portal using the SADAD payment system or via authorised banks. The payment reference is the excise return reference generated by the portal.

### 6.4 Penalties

**Penalties**

| Infringement | Penalty (indicative — verify against current ZATCA bylaw) |
| --- | --- |
| Late filing of an excise return | Administrative penalty + late-filing surcharge |
| Late payment of excise tax | **5% of unpaid tax for each month or part-month** of delay |
| Failure to register | Fine + back tax + penalty on the underlying goods |
| Tax evasion (false declaration, undervaluation, unreported releases) | Up to **3× the evaded tax** + possible criminal referral |
| Operating a tax warehouse without a licence | Seizure of goods + administrative penalty |
| Failure to maintain prescribed records | Administrative penalty per Bylaw |

Penalty amounts are subject to ZATCA's published schedule and may be amended by ministerial decision; confirm the current figures before advising a client.

### 6.5 Records & retention

- **Records & retention** — - Retain all import documents, customs declarations, production records, warehouse inventory, release notes, sales invoices and ZATCA correspondence for at least 6 years from the end of the tax period (general ZATCA retention rule — verify against the current Bylaw, which may specify longer for excise). - Where a financial guarantee has been provided to ZATCA for a tax warehouse, retain the guarantee documentation for the life of the warehouse licence plus the general retention period.

## Section 7 — Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Taxpayer not yet registered for excise but already importing | STOP — register first; do not file until ZATCA registration number issued |
| Product borderline between energy drink and ordinary RTD | Treat as energy drink (100%) pending ZATCA classification ruling |
| Drink borderline between sweetened and unsweetened | Treat as sweetened (50%) until composition documentation confirms otherwise |
| RSP not documented and no ZATCA standard price published | STOP — cannot determine tax base |
| RSP documented but appears to be below market | Use higher of RSP and ZATCA standard price; if standard price unavailable, escalate to ZATCA for ruling |
| Damaged / destroyed stock not disposed of under ZATCA supervision | Treat as released into consumption (taxable) |
| Intra-warehouse movement to a warehouse whose licence cannot be confirmed | Treat as a release into consumption (taxable) |
| Export documentation incomplete | Treat as a release into consumption (taxable) |
| 2024-2025 scope expansion potentially affecting a borderline product | **Verify current ZATCA scope and rates against latest circular before excluding** |
| Filing deadline ambiguity (15-day rule vs amended bylaw) | File and pay by the **15th of the following month** unless ZATCA has published a later date for the specific period |
| Cross-border movement to another GCC state | STOP — verify intra-GCC mechanics with ZATCA and destination authority |

## Section 8 — Sources

1. **Excise Tax Law — Royal Decree No. A/86 dated 27/8/1438H** (corresponding to 2017) — primary excise tax statute for KSA.
2. **Excise Tax Implementing Regulations / Bylaws** — issued by ZATCA (formerly GAZT) under the Excise Tax Law and amended from time to time. Cover registration, tax warehouses, return mechanics, and penalty schedule.
3. **Common GCC Excise Tax Agreement (2016)** — supranational framework for excise tax across the GCC member states; establishes the core product list and harmonisation principles.
4. **ZATCA Ministerial / Board Decisions** extending the excise list:
   - 2019 extension to **electronic smoking devices and e-liquids** at 100%.
   - 2019 extension to **sweetened drinks** at 50% (effective 1 December 2019).
5. **ZATCA Excise Tax Guides** — published guidance on classification, the tax warehouse regime, standard prices, registration, and return preparation, available on the ZATCA portal.
6. **ZATCA Standard Prices Lists** (السعر القياسي) — periodically published reference prices for excise products; the tax base is the higher of RSP or the ZATCA standard price.
7. **ZATCA Penalty Schedule** — administrative penalties and late-payment surcharges, as periodically updated.
8. **VAT Implementing Regulations (KSA)** — relevant only for the interaction between excise tax and VAT (excise feeds into the VAT base when goods are sold downstream); not the subject of this skill but flagged for completeness.
9. **SOCPA practitioner guidance** — Saudi Organisation for Chartered and Professional Accountants commentary on excise tax compliance.

## End of Skill — Saudi Arabia Excise Tax v1.0

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
