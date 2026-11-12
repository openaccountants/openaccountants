---
name: customs-duties-workflow-base
description: "Tier 1 workflow base for customs duty skills. Covers the customs declaration lifecycle from origin determination, HS classification, valuation, preference, special procedures, through to release for free circulation. Workflow architecture only — no country-specific tariff rates or detailed special procedure mechanics. MUST be loaded alongside a country/region customs content skill (EU UCC, US CBP, UK CDS post-Brexit, etc.). Assumes a licensed customs broker, AEO/CTPAT certified party, or in-house customs manager files the declaration. Does NOT cover: CBAM (see cbam-carbon-border-adjustment), import VAT (see country VAT skills), excise duties (see excise-tax-workflow-base), or anti-dumping / countervailing duty investigation procedure (only their tariff effect at point of declaration)."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Customs Duties Workflow Base

## What this file is

The Tier 1 workflow base for customs duty skills. Country content skills load on top.

## Section 1 — Audience and assumptions

- **Audience and assumptions** — This base assumes: The declarant is an importer / exporter / customs representative; The shipment has been physically moved or is being placed under a customs procedure; A licensed customs broker or in-house customs manager files the declaration; The HS Code is determined under the WCO Harmonized System and applied at the national tariff level

## Section 2 — Lifecycle runbook

### Step 1 — Document the transaction

- Commercial invoice (supplier, buyer, consignee)
- Packing list
- Bill of lading / airway bill / CMR
- Certificate of origin (preferential or non-preferential)
- Transport documents
- Sanitary / phytosanitary / safety certificates
- Licenses (dual-use, controlled goods)
- CBAM-relevant emissions data (EU imports of in-scope goods)

### Step 2 — Determine HS classification

- **HS classification levels** — [T1] Use WCO Harmonized System nomenclature at the level required by the destination country: 6 digits — WCO common level; 8 digits — typical national tariff (e.g., EU Combined Nomenclature); 10 digits — TARIC or US HTS additional precision
- **General Rules for the Interpretation (GRI 1-6)** — Apply the General Rules for the Interpretation (GRI 1-6) of the HS: 1. Headings and chapter notes 2. Incomplete / unassembled goods classify as complete 3. Mixed goods classify by essential character or last-in-numerical-order 4. Goods most akin 5. Containers / packaging 6. Comparable level subheadings

### Step 3 — Determine origin

- **Non-preferential origin** — country where last substantial transformation occurred; used for trade statistics, anti-dumping, trade remedy, marking, quota  _([T1])_
- **Preferential origin** — origin granting reduced or zero duty under a free trade agreement (FTA), generalised scheme of preferences (GSP), customs union  _([T1])_
- **Preferential origin tests** — Wholly obtained (mining, agriculture, fishing); Sufficient transformation per the FTA's specific rules (change in tariff heading, value-added percentage, specific manufacturing operation); Cumulation (bilateral / diagonal / full / regional); Direct transport / non-manipulation  _([T1])_

### Step 4 — Determine customs value

- **WTO Customs Valuation Agreement — six methods in hierarchical order** — 1. Transaction value of the imported goods (the price actually paid or payable) — primary method 2. Transaction value of identical goods — already accepted by customs 3. Transaction value of similar goods 4. Deductive value (resale price method) 5. Computed value (cost-plus method) 6. Fallback / reasonable means consistent with WTO  _([T1] WTO Customs Valuation Agreement)_

**Adjustments to transaction value (Article 8 WTO Valuation Agreement)**  _([T1] Article 8 WTO Valuation Agreement)_

| Add | Subtract |
| --- | --- |
| Commissions / brokerage paid to buyer's agent | Buying commissions |
| Container costs | Charges for construction / assembly / maintenance after importation |
| Packing | Duties and taxes payable in destination |
| Assists (free or below-cost goods/services provided by buyer to seller) | Interest paid (if separately identified) |
| Royalties / license fees related to imported goods that buyer must pay as condition of sale |  |
| Resale proceeds accruing to seller |  |
| Transport, loading, handling, insurance to the place of importation |  |

### Step 5 — Apply tariff

- **Apply tariff** — [T1] Base most-favoured-nation (MFN) rate per WTO commitments; Preferential rate where origin satisfied and certificate / declaration provided; Anti-dumping / countervailing duty if applicable; Tariff suspensions (autonomous suspensions, EU); Tariff quotas (in-quota / out-of-quota duty rates); Safeguard measures; Retaliatory duties (Section 301 US; EU retaliation lists)

### Step 6 — Apply special procedures (where applicable)

- Inward processing — duty-free import for processing and re-export
- Outward processing — re-import after processing abroad with duty only on added value
- Customs warehousing — duty deferral
- Free zones / FTZ — duty-free storage and processing
- Temporary admission / ATA Carnet — duty-free import for exhibitions, samples, professional equipment
- End-use — reduced duty for specific use
- Transit (T1 / T2 / TIR) — movement under customs control

### Step 7 — Prepare and lodge declaration

- Customs declaration in destination country's electronic system (EU AES/IES, US ACE, UK CDS, China MIPS, India ICES, etc.)
- Single Administrative Document (SAD) for EU; entry summary for US ABI
- Pre-arrival lodgement where required (24-hour rule for ocean to US, EU ICS2)

### Step 8 — Pay duty and VAT/GST

- Duty paid on release OR deferred under deferment account (with bank guarantee)
- Import VAT/GST — paid at import OR self-assessed under postponed VAT accounting (EU PVA), reverse charge

### Step 9 — Post-clearance audit and amendment

- **Post-clearance audit and amendment** — [T1] Customs authorities have 3-5 years post-clearance to audit. Maintain documentation. Voluntary amendment (corrective declaration) reduces penalties.

## Section 3 — Customs regimes by region

### 3.1 European Union

- UCC (Union Customs Code) — Regulation (EU) 952/2013 in force from 1 May 2016
- AEO (Authorised Economic Operator) — trusted-trader certification (AEO-C customs, AEO-S security, AEO-F combined)
- Centralised clearance — declaration in one MS for goods imported into another
- ICS2 (Import Control System 2) — pre-arrival risk analysis
- CBAM (Carbon Border Adjustment Mechanism) — see `cbam-carbon-border-adjustment.md`

### 3.2 United States

- CBP (Customs and Border Protection) under Title 19 USC
- ACE (Automated Commercial Environment) declaration system
- C-TPAT trusted trader program
- Section 301 tariffs (China)
- Section 232 tariffs (steel, aluminum)
- De minimis USD 800 per shipment

### 3.3 United Kingdom (post-Brexit)

- CDS (Customs Declaration Service) replaced CHIEF in 2023
- UK Global Tariff (UKGT) since 1 January 2021
- Northern Ireland Protocol / Windsor Framework — separate rules for NI imports from GB
- Inward / outward processing — UCC mechanics retained
- Postponed VAT accounting — VAT deferred to VAT return

### 3.4 Other major regimes

- Canada — CBSA with CARM system rollout 2024-2025
- Australia — Border Force with ICS
- Japan — Japan Customs with NACCS
- China — General Administration of Customs with GACC
- India — ICEGATE with Customs Act 1962
- Brazil — Receita Federal with Siscomex / Portal Único do Comércio Exterior (Pucomex)

## Section 4 — Reviewer brief

1. Shipment register
   - Commercial documents
   - HS classification with GRI rationale
   - Origin determination with supporting certificate
   - Customs value with WTO method and Article 8 adjustments

2. Tariff calculation
   - Base MFN rate
   - Preference applied
   - ADD / CVD applied
   - Tariff quotas allocated
   - Total duty

3. VAT / GST on importation
   - Base value (customs value + duty + other charges)
   - VAT rate
   - Postponed accounting status

4. Special procedure usage
   - Procedure code
   - Bond / guarantee status
   - Discharge plan

5. Risk register
   - Trade compliance flags (controlled goods, sanctioned parties, dual-use)
   - ADD / CVD investigation status
   - CBAM in-scope goods

6. Reviewer questions — [T2]/[T3] items

## Section 5 — Self-checks (15)

1. [ ] HS classification supported by GRI reasoning, binding tariff information (BTI) or equivalent if available
2. [ ] Origin determination supported by certificate or supplier declaration
3. [ ] Customs value method correctly applied per Article 8 hierarchy
4. [ ] Royalties / assists / commissions / freight added per Article 8
5. [ ] Preference verified against current FTA text and product-specific rules
6. [ ] ADD / CVD / safeguard rates current and applicable
7. [ ] Tariff quota allocation verified
8. [ ] Special procedure code correct
9. [ ] Sanctions / dual-use / controlled-goods screening completed
10. [ ] Importer-of-record identification correct
11. [ ] Pre-arrival electronic submission lodged within window
12. [ ] CBAM scope checked for EU imports
13. [ ] Postponed VAT accounting election applied where eligible
14. [ ] Bond / guarantee in place for special procedures
15. [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 6 — Global refusal catalogue

**Global refusal catalogue**

| Refusal | Trigger |
| --- | --- |
| R-CUST-1 | Sanctioned party / OFAC / EU restrictive measures match |
| R-CUST-2 | Controlled / dual-use goods without licence |
| R-CUST-3 | ADD / CVD investigation active and country uncertain |
| R-CUST-4 | HS classification ambiguous — request BTI / equivalent |
| R-CUST-5 | Preference origin contested or supplier declaration absent |
| R-CUST-6 | Customs value contested (related-party transaction, missing royalty info) |
| R-CUST-7 | Anti-circumvention investigation against country of origin |
| R-CUST-8 | CBAM in-scope without verified emissions or default-value-cap exceeded |

- **R-CUST-1** — Sanctioned party / OFAC / EU restrictive measures match
- **R-CUST-2** — Controlled / dual-use goods without licence
- **R-CUST-3** — ADD / CVD investigation active and country uncertain
- **R-CUST-4** — HS classification ambiguous — request BTI / equivalent
- **R-CUST-5** — Preference origin contested or supplier declaration absent
- **R-CUST-6** — Customs value contested (related-party transaction, missing royalty info)
- **R-CUST-7** — Anti-circumvention investigation against country of origin
- **R-CUST-8** — CBAM in-scope without verified emissions or default-value-cap exceeded

## Section 7 — Slot contract for country customs skills

[TARIFF SYSTEM]
- Nomenclature (CN, HTS, UKGT, etc.)
- Tariff portal URL
- Update frequency

[FTA PORTFOLIO]
- Active FTAs and product-specific rules portal references
- GSP/GSP+/Everything But Arms applicability

[VALUATION]
- National rules supplementing WTO Valuation Agreement
- Related-party transaction rules

[PROCEDURES]
- Special procedure codes
- AEO / trusted trader equivalent

[FILING]
- Electronic declaration system
- Pre-arrival lodgement window
- De minimis thresholds (low-value consignment)

[OVERLAYS]
- CBAM (EU)
- Section 301 / 232 (US)
- Trade remedy investigations active

[PENALTIES]
- Misclassification penalties
- Origin misstatement penalties
- Voluntary disclosure relief

## Section 8 — Disclaimer

This workflow base produces working papers for review by licensed customs practitioners. Customs declarations are legally binding; misstatements carry criminal as well as civil penalties. Every output must be reviewed and signed off by a licensed customs broker or in-house customs manager before lodgement.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).

## Section 2 — Lifecycle runbook

0. **Step 1 — Document the transaction** — Document the transaction
