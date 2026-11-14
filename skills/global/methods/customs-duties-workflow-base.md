---
name: customs-duties-workflow-base
description: "Shared workflow base for customs duty skills. Covers the customs declaration lifecycle from origin determination, HS classification, valuation, preference, special procedures, through to release for free circulation. Workflow architecture only : no country-specific tariff rates or detailed special procedure mechanics. MUST be loaded alongside a country/region customs content skill (EU UCC, US CBP, UK CDS post-Brexit, etc.). Assumes a licensed customs broker, AEO/CTPAT certified party, or in-house customs manager files the declaration. Does NOT cover: CBAM (see cbam-carbon-border-adjustment), import VAT (see country VAT skills), excise duties (see excise-tax-workflow-base), or anti-dumping / countervailing duty investigation procedure (only their tariff effect at point of declaration)."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
type: cross-country-method
last_updated: 2026-11-14
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Customs Duties Workflow Base v0.2

## Scope

The shared workflow base for customs duty skills. Country content skills load on top. This is a 2026 preparation method, not a current worldwide tariff table. Keep the original source documents and every unresolved country/procedure question with the reviewer handoff. Internal [T1]/[T2]/[T3] tags are workflow notes, never professional approval labels.

## Ask the client first

Obtain the importer/exporter and actual owner/representative, origin and destination/customs territories, movement and acceptance dates, goods/composition/use/quantity, supplier/customer relationship, price and Incoterms, freight/insurance/royalties/assists, the proposed procedure/authorisations and actual origin evidence. Missing classification, origin, value or authorisation does not default to a plausible code or the highest rate.

## Section 1 : Audience and assumptions

- **Audience and assumptions** : This base assumes: The declarant is an importer / exporter / customs representative; The shipment has been physically moved or is being placed under a customs procedure; A licensed customs broker or in-house customs manager files the declaration; The HS Code is determined under the WCO Harmonized System and applied at the national tariff level

## The method, step by step

### Step 1 : Document the transaction

- Commercial invoice (supplier, buyer, consignee)
- Packing list
- Bill of lading / airway bill / CMR
- Certificate of origin (preferential or non-preferential)
- Transport documents
- Sanitary / phytosanitary / safety certificates
- Licenses (dual-use, controlled goods)
- CBAM-relevant emissions data (EU imports of in-scope goods)

### Step 2 : Determine HS classification

- **HS classification and national precision:** obtain the actual goods description, composition, function and destination tariff. A supplier's short HS code is not proof of the complete declaration code or its additional measures. Apply the required national subdivisions and any binding classification decision. [EC classification guidance](https://taxation-customs.ec.europa.eu/customs/common-customs-tariff-cct/tariff-classification-goods_en).
- **General Rules for Interpretation:** establish the applicable headings, legal notes and rules for incomplete/unassembled goods, mixtures/composites, goods most akin, containers/packaging and comparable subheadings. Do not jump from a mixed product directly to essential character or last-in-order without the preceding applicable rules. The full current legal wording was not readable in this run, so an actual disputed classification must obtain it or a binding ruling before a final code is supplied. [EC classification route](https://taxation-customs.ec.europa.eu/customs/common-customs-tariff-cct/tariff-classification-goods_en).

### Step 3 : Determine origin

- **Non-preferential origin:** determine wholly obtained status or the applicable last substantial transformation test, including minimal-operation and anti-circumvention restrictions. It is not simply the country of dispatch. In the EU, product-specific binding rules and other guidance have different legal status; non-preferential certificates are not universally required. [EC origin guidance](https://taxation-customs.ec.europa.eu/customs/rules-origin-goods/non-preferential-rules-origin_en).
- **Preferential origin:** test the actual arrangement, product rule, origin and valid evidence before claiming a reduced or zero rate. A supplier declaration is not necessarily the proof presented by the importer. Depending on the agreement, proof may be a government certificate, authorised/registered exporter statement or importer's knowledge. [EC proof of origin](https://taxation-customs.ec.europa.eu/customs/rules-origin-goods/preferential-rules-origin/proof-origin_en).
- **Preferential origin tests** : Wholly obtained (mining, agriculture, fishing); Sufficient transformation per the FTA's specific rules (change in tariff heading, value-added percentage, specific manufacturing operation); Cumulation (bilateral / diagonal / full / regional); Direct transport / non-manipulation  _([T1])_

### Step 4 : Determine customs value

- **Valuation order:** try transaction value subject to its conditions, then identical goods, similar goods, deductive value, computed value and permitted fallback. The importer may request reversal of deductive and computed value, subject to the applicable implementation. Related parties do not automatically disqualify transaction value, but price influence and statutory tests matter. Never use an invented minimum or the higher of arbitrary alternatives. [WTO Agreement arts. 1 to 7](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm).

**Adjustments to transaction value (Article 8 WTO Valuation Agreement)**  _([T1] Article 8 WTO Valuation Agreement)_

| Potential addition, subject to conditions | Potential exclusion, subject to conditions | Official basis |
| --- | --- | --- |
| Relevant selling commission or brokerage incurred by the buyer, not already in the price, excluding a genuine buying commission | A separately identified genuine buying commission is excluded, not added merely because the buyer pays it | [WTO art. 8 and notes to art. 1](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm), [interpretative notes](https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm) |
| Container costs | Charges for construction / assembly / maintenance after importation | [WTO art. 8 and notes to art. 1](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm), [interpretative notes](https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm) |
| Packing | Duties and taxes payable in destination | [WTO art. 8 and notes to art. 1](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm), [interpretative notes](https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm) |
| Qualifying art. 8 assists supplied by the buyer free/below cost, apportioned as appropriate and not already in the price | Separately identified financing interest only where the destination's actual conditions permit | [WTO art. 8 and notes to art. 1](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm), [interpretative notes](https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm) |
| Royalties / license fees related to imported goods that buyer must pay as condition of sale |  | [WTO art. 8 and notes to art. 1](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm), [interpretative notes](https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm) |
| Resale proceeds accruing to seller |  | [WTO art. 8 and notes to art. 1](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm), [interpretative notes](https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm) |
| Transport, loading, handling and insurance only to the extent included by the destination's law, without double counting an invoice-inclusive amount | Separately distinguishable post-import transport where the applicable law permits | [WTO art. 8 and notes to art. 1](https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm), [interpretative notes](https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm) |
### Step 5 : Apply tariff

- **Apply tariff** : [T1] Base most-favoured-nation (MFN) rate per WTO commitments; Preferential rate where origin satisfied and certificate / declaration provided; Anti-dumping / countervailing duty if applicable; Tariff suspensions (autonomous suspensions, EU); Tariff quotas (in-quota / out-of-quota duty rates); Safeguard measures; Retaliatory duties (Section 301 US; EU retaliation lists)

### Step 6 : Apply special procedures (where applicable)

- Inward processing: obtain authorisation and the discharge terms; identify whether products are re-exported, warehoused or released into free circulation and what duty then arises
- Outward processing: establish authorisation, exported and re-imported goods, processing value and the actual conditional relief calculation; do not assume every re-import is taxed only on added value
- Customs warehousing : duty deferral
- Free zones / FTZ: establish the actual authorised storage/processing and release rules; location in a zone does not create an unconditional exemption
- Temporary admission / ATA Carnet: establish qualifying use, identity, re-export/discharge and whether relief is total or partial, rather than assume every admission is duty-free
- End-use : reduced duty for specific use
- Transit (T1 / T2 / TIR) : movement under customs control

### Step 7 : Prepare and lodge declaration

- Use the actual destination declaration system and procedure. Identify the importer/declarant, representation, authorisation, procedure code, goods lines, origin, valuation and tariff measures from current instructions, not an assumed worldwide screen.
- In the EU, declarations are normally electronic, with alternative/oral/conduct routes only where allowed. Obtain the current national data requirements rather than assume a paper SAD is universal. In the US, establish the correct ACE formal/informal entry and current filing instructions.
- Establish the current pre-arrival security declaration, responsible carrier/operator, mode-specific deadline and the separate import declaration. A security filing is not itself customs release; no single worldwide hours limit is supplied here.

### Step 8 : Pay duty and VAT/GST

- Duty paid on release OR deferred under deferment account (with bank guarantee)
- Import VAT/GST : paid at import OR self-assessed under postponed VAT accounting (EU PVA), reverse charge

### Step 9 : Post-clearance audit and amendment

- **Post-clearance audit and amendment:** obtain the jurisdiction's actual record-retention, debt-notification, amendment and disclosure provisions, including fraud/criminal exceptions. Preserve declarations, decisions, origin and valuation evidence. Do not assume a worldwide audit period or that a voluntary correction necessarily reduces penalties.

## Section 3 : Customs regimes by region

### 3.1 European Union

- UCC framework: load the current EU customs skill and operative law for the actual procedure. The EC pages read here explain declaration, valuation, origin and conditional special procedures; they are not a complete article-by-article legal verification.
- AEO/trusted-trader status: inspect actual customs-simplification/security authorisations and their scope; do not infer approval from a broker's name or the obsolete shorthand for a combined certificate
- Centralised clearance : declaration in one MS for goods imported into another
- ICS2 (Import Control System 2) : pre-arrival risk analysis
- CBAM (Carbon Border Adjustment Mechanism) : see `cbam-carbon-border-adjustment.md`

### 3.2 United States

- CBP (Customs and Border Protection) under Title 19 USC
- ACE (Automated Commercial Environment) declaration system
- C-TPAT trusted trader program
- Section 301 tariffs (China)
- Section 232 tariffs (steel, aluminum)
- Do not apply the old blanket USD 800 duty-free shipment statement. CBP's official bulletin suspended the ordinary de minimis clearance route from 29 August 2025, subject to its stated exceptions. Obtain current 2026 implementation for the actual postal/non-postal entry before costing it. [CBP bulletin](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/3f01456).

### 3.3 United Kingdom (post-Brexit)

- CDS migration was phased; HMRC says no declarations have been made on CHIEF since July 2024. The old blanket 2023 replacement date is wrong. [HMRC VEXP40100](https://www.gov.uk/hmrc-internal-manuals/vat-exports-of-goods-from-the-uk/vexp40100).
- UK Global Tariff: obtain the current commodity code, origin, measures and event date from the UK tariff; no historical rate is assumed current
- Northern Ireland Protocol / Windsor Framework : separate rules for NI imports from GB
- Inward/outward processing: apply current UK law and authorisation, not an assumption that every EU UCC condition was retained unchanged
- Postponed VAT accounting: test eligibility and the actual import statement/return treatment through the UK VAT skill; it is not a deferral of customs duty

### 3.4 Other major regimes

- Canada: CARM became the commercial-import accounting and duty/tax system of record on 21 October 2024, confirmed by CBSA's October 2026 update. It is not itself proof that release, accounting and payment are the same event. [CBSA update](https://www.canada.ca/en/border-services-agency/news/2026/10/the-cbsa-provides-an-update-on-its-new-assessment-and-revenue-management-system.html).
- Australia : Border Force with ICS
- Japan : Japan Customs with NACCS
- China : General Administration of Customs with GACC
- India : ICEGATE with Customs Act 1962
- Brazil : Receita Federal with Siscomex / Portal Único do Comércio Exterior (Pucomex)

### Country applications and boundaries

**European Union:** establish classification, origin and value separately, then the actual declaration/procedure and import-debt event. A supplier's origin statement is evidence to test, not a universal preference entitlement. A special procedure needs the relevant authorisation, guarantee and discharge, and later free circulation may create duty. [Duty factors](https://taxation-customs.ec.europa.eu/customs/common-customs-tariff-cct/calculation-customs-duties_en), [declarations](https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/customs-operation/customs-declaration_en), [special-procedure overview](https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/importation_en).

**United Kingdom:** HMRC's Method 1 guidance includes qualifying border freight and excludes genuine separately identified buying commission. Review the agent's actual role, not its invoice label, and do not add freight already in the supplier's inclusive price. Use CDS and the current UK law/commodity measures. [HMRC Method 1, additions/deductions, transport and commissions](https://www.gov.uk/guidance/customs-valuation/method-1-transaction-value).

**Canada and other routes:** use the Canadian method for the current CAD/CARM fields, security, accounting and payment; obtain the actual local method for Australia/ICS, Japan/NACCS, China/GACC, India/ICEGATE/ICES or Brazil/Siscomex/Portal Único. These names are routing clues, not independently confirmed 2026 filing screens or relief entitlements. Keep the original country route in the workpaper when a local source is still missing.

## Worked cases

**UK invoice and additions, no rate assumption.** Assume an acceptable Method 1 sale priced GBP 10,000 with no border freight included. Separate records establish freight/insurance to the UK border GBP 500, qualifying packing GBP 100 and a genuine separately shown buying commission GBP 200 outside the goods price. No other additions or deductions arise. Customs value is GBP 10,600, not GBP 10,800. This computes the conditional base only; classification, origin and the current tariff are needed before duty. If the 500 freight was already in the 10,000 price, value is 10,100, so adding it again would overstate the base by 500. [HMRC Method 1](https://www.gov.uk/guidance/customs-valuation/method-1-transaction-value).

```oa-check
name: UK customs value excludes buying commission and avoids duplicate freight
inputs:
  goods_price_excluding_border_freight: 10000
  border_freight_insurance: 500
  qualifying_packing: 100
  genuine_buying_commission: 200
steps:
  - customs_value: goods_price_excluding_border_freight + border_freight_insurance + qualifying_packing
  - wrong_value_adding_buying_commission: customs_value + genuine_buying_commission
  - overstatement: wrong_value_adding_buying_commission - customs_value
  - inclusive_price_case: goods_price_excluding_border_freight + qualifying_packing
expected:
  customs_value: 10600
  overstatement: 200
  inclusive_price_case: 10100
```

## Section 4 : Reviewer brief

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

6. Reviewer questions : [T2]/[T3] items

## Section 5 : Self-checks (15)

1. [ ] HS classification supported by GRI reasoning, binding tariff information (BTI) or equivalent if available
2. [ ] Origin determination supported by certificate or supplier declaration
3. [ ] Customs value method correctly applied under the actual sequential rules; Article 8 governs additions, not the valuation-method hierarchy
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

## When to refuse or refer

**Global refusal catalogue**

These are workpaper escalation triggers, not automatic legal prohibitions in every country. Preserve supported preparation, but withhold the affected declaration or tax conclusion until the specific issue is resolved.

| Refusal | Trigger |
| --- | --- |
| R-CUST-1 | Sanctioned party / OFAC / EU restrictive measures match |
| R-CUST-2 | Controlled / dual-use goods without licence |
| R-CUST-3 | ADD / CVD investigation active and country uncertain |
| R-CUST-4 | HS classification ambiguous : request BTI / equivalent |
| R-CUST-5 | Preference origin contested or supplier declaration absent |
| R-CUST-6 | Customs value contested (related-party transaction, missing royalty info) |
| R-CUST-7 | Anti-circumvention investigation against country of origin |
| R-CUST-8 | CBAM in-scope with missing emissions evidence or unresolved eligibility to use an applicable default; obtain the actual current CBAM rule |

- **R-CUST-1** : Sanctioned party / OFAC / EU restrictive measures match
- **R-CUST-2** : Controlled / dual-use goods without licence
- **R-CUST-3** : ADD / CVD investigation active and country uncertain
- **R-CUST-4** : HS classification ambiguous : request BTI / equivalent
- **R-CUST-5** : Preference origin contested or supplier declaration absent
- **R-CUST-6** : Customs value contested (related-party transaction, missing royalty info)
- **R-CUST-7** : Anti-circumvention investigation against country of origin
- **R-CUST-8** : CBAM in-scope with missing emissions evidence or unresolved eligibility to use an applicable default; obtain the actual current CBAM rule

## Section 7 : Slot contract for country customs skills

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

## Section 8 : Disclaimer

This workflow base produces working papers for review by licensed customs practitioners. Customs declarations are legally binding; misstatements carry criminal as well as civil penalties. Every output must be reviewed and signed off by a licensed customs broker or in-house customs manager before lodgement.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).

## Shipment-document recap

0. **Step 1 : Document the transaction** : Document the transaction


## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| WTO Valuation Agreement. Read arts. 1 to 9 for admissible transaction value, alternatives, importer reversal option, additions and currency rules | https://www.wto.org/english/docs_e/legal_e/20-val_01_e.htm | 2026-11-14 |
| WTO interpretative notes. Read the general sequential-method note and note to art. 1 for separately distinguished post-import costs/taxes | https://www.wto.org/english/docs_e/legal_e/20-val_02_e.htm | 2026-11-14 |
| HMRC Method 1. Read the opening transaction-value/sale conditions and the additions/deductions, transport and commissions sections, not every later example | https://www.gov.uk/guidance/customs-valuation/method-1-transaction-value | 2026-11-14 |
| HMRC VEXP40100. Read for phased CHIEF migration and current CDS export declaration route | https://www.gov.uk/hmrc-internal-manuals/vat-exports-of-goods-from-the-uk/vexp40100 | 2026-11-14 |
| EC duty calculation. Read for classification, value and origin as separate factors and the six valuation methods | https://taxation-customs.ec.europa.eu/customs/common-customs-tariff-cct/calculation-customs-duties_en | 2026-11-14 |
| EC tariff classification. Read for CN classification and distinction from national tax/measure determination | https://taxation-customs.ec.europa.eu/customs/common-customs-tariff-cct/tariff-classification-goods_en | 2026-11-14 |
| EC non-preferential origin. Read for wholly obtained/last transformation, binding versus non-binding product rules and certificate exceptions | https://taxation-customs.ec.europa.eu/customs/rules-origin-goods/non-preferential-rules-origin_en | 2026-11-14 |
| EC preferential proof. Read for certificate, exporter-statement/supplier-declaration and importer-knowledge routes; no universal proof format inferred | https://taxation-customs.ec.europa.eu/customs/rules-origin-goods/preferential-rules-origin/proof-origin_en | 2026-11-14 |
| EC customs declaration. Read for responsible declarants, electronic filing and procedure routing | https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/customs-operation/customs-declaration_en | 2026-11-14 |
| EC importation. Read free-circulation and special-procedure sections for conditional authorisation/discharge; no generic ENS hours rule adopted | https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/importation_en | 2026-11-14 |
| CBP CSMS 66065494, agency bulletin hosted by its delivery service. Read for the 29 August 2025 ordinary de minimis suspension and entry-route exceptions; not a certification of every 2026 implementing change | https://content.govdelivery.com/accounts/USDHSCBP/bulletins/3f01456 | 2026-11-14 |
| CBSA 29 October 2026 update. Read for CARM's actual 21 October 2024 launch and separation of accounting/payment from release | https://www.canada.ca/en/border-services-agency/news/2026/10/the-cbsa-provides-an-update-on-its-new-assessment-and-revenue-management-system.html | 2026-11-14 |

Not yet confirmed: the full current UCC and 2026 Combined Nomenclature/GRI originals returned empty responses or a verification screen, so their complete wording, code precision, audit/debt/retention periods and any disputed classification must be obtained before use. Current tariff rates/quotas, remedy/retaliatory measures, each FTA product rule, pre-arrival deadline, special-procedure relief, payment/VAT postponement, guarantee and amendment/penalty relief remain country/job inputs, not worldwide defaults. Actual 2026 US postal/non-postal de minimis implementation and the named Asian/Australian/Brazilian portal screens are not certified here. CBAM scope/emissions/default eligibility goes to its current owner. These bounded gaps do not prevent document collection and supported valuation reconciliation.
