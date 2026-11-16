---
name: cbam-carbon-border-adjustment
description: "Use this skill whenever an EU importer (declarant), an indirect customs representative, or a non-EU producer asks about the EU Carbon Border Adjustment Mechanism. Trigger on phrases like \"CBAM\", \"carbon border adjustment\", \"CBAM certificates\", \"embedded emissions\", \"default values\", \"verified emissions\", \"CN code 7208\", \"CN code 28080000\", \"fertiliser CBAM\", \"cement CBAM\", \"aluminium CBAM\", \"hydrogen CBAM\", \"electricity CBAM\", \"iron and steel CBAM\", \"quarterly CBAM report\", \"CBAM declarant\", \"CBAM authorised declarant\", or any request to assess CBAM scope, compute embedded emissions, prepare the quarterly report (transitional period) or annual CBAM declaration (definitive period from 2026). Covers Regulation (EU) 2023/956, Implementing Regulation (EU) 2023/1773 (transitional period reporting), the Default Values Implementing Regulation and the definitive-period implementing rules as read on 15 November 2026. Does NOT cover: emissions trading system (EU ETS), domestic carbon taxes (UK CBAM, Australia Safeguard Mechanism, California CCA), customs tariff / preference rules, or product origin determination. ALWAYS read this skill before computing CBAM exposure or preparing a CBAM report."
version: 1.0
jurisdiction: EU-27
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - cross-border-workflow-base
type: computation
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# CBAM Carbon Border Adjustment

## Scope

Use this skill with `cross-border-workflow-base` for an EU importer, indirect customs representative or non-EU operator assessing CBAM scope, collecting installation data, reconstructing transitional reports or preparing the definitive-period declaration. Coverage is calendar 2026, with historical reporting for 1 October 2023 to 31 December 2025 and the expressly dated first compliance events in 2027. The financial obligation relates to 2026 imports even though certificate sales start later. [Regulation 2023/956 arts 1–2, 20, 32, 36](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

The February 2025 Omnibus proposal is no longer the operative simplification text: Regulation 2025/2083 amended Regulation 2023/956. Use the consolidated provisions and the definitive methods, default values, free-allocation, verification and accreditation acts identified under Sources. The default-value consolidation incorporates a July 2026 correction that applies from 1 January 2026; its consolidation date alone does not reveal that later correction. [Regulation 2023/956 consolidated header and arts 2a, 36](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2026/1740 arts 1–2](https://publications.europa.eu/resource/celex/32026R1740).

The reviewer receives an evidence-backed draft, not an emissions verification opinion. Engineering records, customs classification and origin, the verifier's actual accreditation scope and the applicable implementing rules must support the submission. A customs broker or import lawyer can review legal/customs issues; only an appropriately accredited verifier supplies the required actual-emissions verification. This skill does not provide professional sign-off.

### Quick reference

| Item | Rule, threshold and conditions | Official basis |
|---|---|---|
| Mass exemption | At most 50 tonnes net mass in a calendar year, aggregated across covered mass-based CN codes per importer. Electricity and hydrogen do not get this exemption. If the threshold is exceeded, obligations cover all relevant goods and emissions in that year, including the earlier imports, rather than only the excess. Declare use of the exemption in the customs declaration. | [Regulation 2023/956 art 2a, Annex VII(1)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| Definitive period | Applies to relevant imports from 1 January 2026. Import means release for free circulation; the special inward-processing and offshore rules still need testing. | [Regulation 2023/956 arts 2, 3(4), 6(3), 36(2)(b)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| First annual declaration and surrender | By 30 September 2027 for calendar 2026; then by 30 September for the preceding calendar year. The old 31 May date is superseded. | [Regulation 2023/956 arts 6(1), 22(1)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| Certificate sales and price | Sales begin 1 February 2027. For 2026 embedded emissions, use the average auction closing prices for the quarter of import; the general rule is a calendar-week average. Do not substitute a spot price or assume a platform vendor. | [Regulation 2023/956 arts 20(1)–(4), 21(1)–(1a)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| In-year certificate holding | From 2027, end-of-quarter holding of at least 50% of year-to-date embedded emissions using the specified unmarked-up defaults or qualifying preceding-year method, with free-allocation adjustment. A threshold crosser complies by the end of the following quarter. This is not a holding duty during 2026. | [Regulation 2023/956 arts 22(2)–(2a), 36(2)(c)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| Transitional reports | Q4 2023 through Q4 2025; each due within 1 month after quarter end (in words on the page). First due 31 January 2024 and last due 31 January 2026. The first reporting quarter was not Q3 2023. | [Regulation 2023/956 arts 32, 35(1)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2023/1773 recital 3, art 8](https://publications.europa.eu/resource/celex/32023R1773) |
| Transitional estimates | Up to 20% of total embedded emissions of complex goods may use operator estimates. This is an emissions test, not a percentage of import weight or a per-declarant quarterly weight allowance. | [Implementing Regulation 2023/1773 art 5](https://publications.europa.eu/resource/celex/32023R1773) |
| Actual-emissions records | Keep calculation records and the verifier's report through the end of the 4th year after the year the declaration was or should have been submitted (in words on the page). Carbon-price evidence has the corresponding retention rule. | [Regulation 2023/956 arts 7(5)–(6), 9(2)–(3), Annex V](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |

## Ask the client first

Collect the importer's establishment and EORI, representative's mandate and agreement, authorisation/application dates and status, customs entries and procedure, import dates, exact CN/TARIC description, net mass or electricity MWh, non-preferential origin, and the calendar-year aggregation across customs brokers. Ask whether the importer expects further imports that cross the threshold. Do not infer the importer from a delivery address or count each broker separately. [Regulation 2023/956 arts 2a, 3(4), 3(15)–(20), 5, 17](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

Obtain installation and operator identity, address, location/UN/LOCODE and relevant steel-mill identification, production route, reporting period, functional units and composition, direct/indirect data, precursors, source records and applicable monitoring plan. Obtain the actual/default choice, the correct current country/product default and mark-up where used, verifier and verification reports for actual data, free-allocation worksheet, carbon-price payment/rebate evidence and certificate account movements. Transitional data requirements and definitive data requirements are separate. [Implementing Regulation 2023/1773 arts 3–7](https://publications.europa.eu/resource/celex/32023R1773); [Implementing Regulation 2025/2547 arts 3–10, 13–15](https://publications.europa.eu/resource/celex/32025R2547); [Regulation 2023/956 arts 6–9, Annexes V–VI](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

## The method, step by step

### 1. Scope: classify the goods before calculating

CBAM covers the enumerated goods and greenhouse gases in Annex I, not whole commercial sectors or every item in a tariff chapter. Use the actual description and all exclusions; the summaries below are an index, not substitute classifications. The relevant gases include CO2 and, for specified goods, nitrous oxide or perfluorocarbons. [Regulation 2023/956 art 2(1), Annex I](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

| Sector | Annex I classification boundary | Official basis |
|---|---|---|
| Cement | ex 2507 00 80 excludes non-calcined kaolinic clays; 2523 10 00, 2523 21 00, 2523 29 00, 2523 30 00 and 2523 90 00. Preserve the actual product/TARIC distinction where the default table requires it. | [Regulation 2023/956 Annex I, Cement](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2026/1740 recitals 5–6, Annex I](https://publications.europa.eu/resource/celex/32026R1740) |
| Iron and steel | Chapter 72 with its express ferro-alloy and scrap exclusions; 2601 12 00; 7301–7302, 7303 00, 7304–7308, 7309 00, 7310, 7311 00, 7318 and 7326. Do not omit the ore or tank headings from the earlier short list. | [Regulation 2023/956 Annex I, Iron and steel](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| Fertilisers | 2808 00 00, 2814, 2834 21 00, 3102 and 3105 except 3105 60 00. It is not the whole of chapter 31. | [Regulation 2023/956 Annex I, Fertilisers](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| Aluminium | 7601, 7603–7608, 7609 00 00, 7610, 7611 00 00, 7612, 7613 00 00, 7614 and 7616. It is not the whole of chapter 76. | [Regulation 2023/956 Annex I, Aluminium](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| Electricity | 2716 00 00; apply the electricity-specific importer, measurement, origin/exemption and actual-emissions rules. | [Regulation 2023/956 arts 2, 5(4), 7(3), Annexes I, IV(5)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |
| Hydrogen | 2804 10 00; no mass exemption and direct-only definitive treatment under Annex II. | [Regulation 2023/956 art 2a(4), Annexes I–II](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |

For chapter 72, the excluded entries are 7202 2, 7202 30 00, 7202 50 00, 7202 70 00, 7202 80 00, 7202 91 00, 7202 92 00, 7202 93 00, 7202 99 (including its listed subheadings) and 7204. Resolve the actual classification rather than treating a commercial label such as scrap, alloy or finished steel as conclusive. [Regulation 2023/956 Annex I, Iron and steel](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

Scope normally requires third-country origin determined under non-preferential customs rules, not the shipping country or FTA preferential treatment. Annex III(1) excludes goods originating in Iceland, Liechtenstein, Norway, Switzerland, Büsingen, Heligoland, Livigno, Ceuta and Melilla. Military-use goods and the specified offshore electricity/hydrogen exclusions have distinct conditions. An electricity market-coupling exemption requires the statutory assessment/listing conditions; do not invent a general exemption from geographic proximity. [Regulation 2023/956 art 2(3)–(11), Annex III](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

The mass exemption is per importer and calendar year across covered mass-based goods, with electricity and hydrogen excluded from that exemption. If imports are expected to exceed 50 tonnes, apply for authorisation before that crossing rather than waiting for the annual declaration. Artificially splitting imports through non-genuine arrangements is not a lawful threshold strategy. The representative's own authorisation requirements are not eliminated merely because its client's goods qualify for the exemption. [Regulation 2023/956 arts 2a, 5(1a)–(2a), 25a, 27, Annex VII](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

Outside this skill's computational scope are domestic EU ETS liabilities for stationary installations, aviation and maritime, Canada OBPS, Australia Safeguard Mechanism, California CCA, Korea K-ETS, UK CBAM calculations, customs tariffs, full origin determinations and FTA preference claims. The former forthcoming `eu-ets-allowances.md` reference is not a claim that such a file exists. Refer each issue to the appropriate specialist or actual available skill. Do not reuse EU CBAM formulae for another regime.

### 2. Filing and authorisation

For definitive-period imports that are not exempt, obtain authorised CBAM declarant status and use the CBAM registry. An EU-established importer applies in its establishment state; an agreeing appointed indirect representative acts under art 5(1a), and a non-EU importer requires the indirect-representative route in art 5(2). Apply the electricity capacity-allocation rule separately. Delegating declaration submission leaves the authorised declarant responsible. [Regulation 2023/956 arts 4–5, 17](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

The authority tests the infringement/criminal-history condition, financial and operational capacity, establishment and EORI. Keep the application data, tax-debt certification, declaration of honour, estimated quantities, financial evidence and any required guarantee. The guarantee for an applicant not established throughout the preceding 2 financial years is based on the statutory anticipated certificate obligation; do not invent a fixed deposit. A timely application submitted by 31 March 2026 permits provisional importation until the authority's decision under art 17(7a); this is not a continuing permission to make a late application now. Record refusal/revocation and appeal rights rather than assuming pending status is approval. [Regulation 2023/956 arts 5(5)–(7), 17(1)–(9)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

The annual declaration covers quantities, emissions and certificates after the legally determined carbon-price and free-allocation adjustments, and applicable verification reports. Quantities include earlier imports below the threshold where the importer crosses it. Use the registry and current applicable declaration schema; no particular XML field or vendor is established by this skill. The first deadline is 30 September 2027 for 2026. [Regulation 2023/956 art 6(1)–(2), (6)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

Keep transitional reporting separate: the reporting declarant submits quarterly to the CBAM Transitional Registry, with CN/origin/installation/route, quantity, direct and indirect data, methodology and carbon-price-due information required by arts 3–8. A verified-actual-only rule did not apply to every transitional report. Use the actual amendment/correction route under art 9 and any authority instruction for a historical correction; do not assume an ordinary original filing is still timely. The Q4 2024 report was due 31 January 2025 (derived from the quarter-end rule). [Implementing Regulation 2023/1773 arts 2–9](https://publications.europa.eu/resource/celex/32023R1773).

### 3. Select the correct emissions method and period

During the transitional period, art 4(1) supplies calculation-based or continuous-measurement methods. Until 31 December 2024, the specified carbon-pricing, compulsory-monitoring or installation-monitoring methods could be used if they gave similar coverage and accuracy. The broader fallback for missing operator information, including defaults, ran until 31 July 2024 and required the method to be identified and referenced. The separate operator-estimation limit is up to 20% of total embedded emissions of complex goods under art 5. There was no general Q3 2023–Q3 2024 permission for any methodology and no Q4 2024 import-weight cap. [Implementing Regulation 2023/1773 arts 3(4), 4–5](https://publications.europa.eu/resource/celex/32023R1773).

For 2026 goods other than electricity, art 7(2) permits actual emissions or the prescribed defaults. It does not require proof that actual data was impossible before defaults may be used. Actual data follows the definitive methods and verification rules; electricity normally uses defaults unless every actual-emissions condition is established. Indirect emissions normally use the prescribed defaults unless the applicable actual-data conditions are met. [Regulation 2023/956 arts 7–8, Annex IV(4)–(6)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2025/2547 arts 2–12](https://publications.europa.eu/resource/celex/32025R2547).

For actual data, define the installation, system boundaries, production processes, monitoring plan and attribution before multiplying imports by intensity. The usual functional unit is tonnes of goods under the same CN code, but electricity, specified fertilisers and cement have the different units/composition rules in art 4(3)–(5). Record the conversion to the declaration's quantity/emissions units. For goods imported in 2026, the actual-data reporting period is 2026; later imports have the statutory year-of-import presumption and evidence-based production-period alternative. Electricity uses the year of import. [Implementing Regulation 2025/2547 arts 3–7](https://publications.europa.eu/resource/celex/32025R2547).

Do not reuse a transitional default sheet for 2026. Regulation 2025/2621 Annex I provides goods/precursor defaults, Annex II indirect defaults, Annex III electricity direct defaults and Annex IV unidentified-origin precursor defaults. Use the corrected Annex I/IV after Regulation 2026/1740, with product/TARIC, country, production-route and other required distinctions. An absent country or blank/dash value uses the specified other-countries table, not zero. The corrected total-emissions column is used for certificate calculations; its direct/indirect component columns are informational. [Implementing Regulation 2025/2621 art 1, Annex I opening rules](https://publications.europa.eu/resource/cellar/c606a88b-a0ac-11f1-b25c-01aa75ed71a1.0004.02/DOC_1); [Implementing Regulation 2026/1740 recitals 5–13, arts 1–2](https://publications.europa.eu/resource/celex/32026R1740).

| Default mark-up | Conditions | Official basis |
|---|---|---|
| Cement, iron/steel, aluminium, hydrogen | Increase the applicable total-emissions default by 10% for 2026, 20% for 2027 and 30% from 2028. The correctly selected base default and matching production-route benchmark remain necessary. | [Implementing Regulation 2025/2621 corrected Annex I opening rules](https://publications.europa.eu/resource/cellar/c606a88b-a0ac-11f1-b25c-01aa75ed71a1.0004.02/DOC_1) |
| Fertilisers | Increase the applicable total-emissions default by 1% from 2026. Do not apply the other sectors' mark-up. | [Implementing Regulation 2025/2621 corrected Annex I opening rules](https://publications.europa.eu/resource/cellar/c606a88b-a0ac-11f1-b25c-01aa75ed71a1.0004.02/DOC_1) |

This file publishes no country/product default intensity. The preparer must attach the exact operative row and version selected for the goods before a default-based exposure is usable. An alternative regional/electricity default needs the statutory evidence and conditions, rather than a self-selected lower figure. [Implementing Regulation 2025/2547 arts 11–12, Annex V](https://publications.europa.eu/resource/celex/32025R2547).

## Calculation steps

1. **Classify and determine the trigger.** Match Annex I, its exclusions, origin, exemption, importer and procedure. Test the calendar-year net-mass total and the special electricity/hydrogen rules before calculating financial exposure. Imports released from inward processing can bring the relevant original CBAM inputs into the declaration even when the processed output is not itself Annex I. [Regulation 2023/956 arts 2–6](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).
2. **Collect installation data and select the method.** Establish the actual/default basis for the relevant period, production route and functional unit, with documentary evidence. Retain the names/addresses, UN/LOCODE where applicable, sources and verification trail; do not accept a supplier's unexplained intensity. [Implementing Regulation 2023/1773 art 3](https://publications.europa.eu/resource/celex/32023R1773); [Implementing Regulation 2025/2547 arts 3–10](https://publications.europa.eu/resource/celex/32025R2547).
3. **Determine specific embedded emissions.** For simple goods, specific emissions equal attributed emissions divided by production activity. For complex goods, add the relevant precursors' embedded emissions to attributed process emissions before division. Sum each precursor's consumed mass times its specific emissions. Apply the statutory attribution, units and system boundaries; do not double-count a precursor covered by a joint process. [Regulation 2023/956 Annex IV(1)–(3)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2025/2547 arts 3–6, 13–15, Annexes II–III](https://publications.europa.eu/resource/celex/32025R2547).
4. **Compute the import's gross embedded emissions.** For a valid intensity expressed per tonne, multiply imported tonnes by tCO2e/tonne, then sum the relevant imports. Electricity uses its appropriate energy unit/intensity conversion. This is gross emissions, not automatically certificates due. [Regulation 2023/956 art 6(2)(a)–(b), Annex IV](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).
5. **Apply free allocation through the actual method.** Regulation 2025/2620 uses the goods' specific embedded free allocation times imported mass; process-level free allocation depends on the CBAM factor, cross-sectoral correction factor and relevant benchmark, with precursor rules for complex goods. Actual-emissions and default-emissions routes have corresponding free-allocation rules. Electricity's free-allocation adjustment is zero. Never subtract a bare percentage from tonnes or assume every import pays only the phased-in percentage of its actual emissions. [Regulation 2023/956 art 31](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2025/2620 arts 1–4, Annex points 2–5](https://publications.europa.eu/resource/celex/32025R2620).
6. **Establish the carbon-price reduction.** Actual-emissions claims need the effectively paid third-country carbon price, available rebates/compensation, payment evidence and independently certified documentation. The statute also provides a conditional yearly default-carbon-price route; for default emissions, only that route may be used. Do not deduct a nominal carbon tax, a claimed subsidy, a UK charge or an unsupported invoice automatically. Art 9(5) calls for yearly-average foreign-currency conversion, not the exchange rate on the payment date. This file does not establish the implementing conversion formula or a published default carbon price. Hold that component until the applicable operative rule and data are attached. [Regulation 2023/956 art 9](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).
7. **Reconcile certificates and cost separately.** The declaration/surrender number reflects embedded emissions after the legally calculated free-allocation adjustment and carbon-price reduction. One certificate represents 1 tonne CO2e. Apply the 2026 import-quarter price rule to the required certificates for those imports, not a generic weekly or current spot price. Reconcile purchases, surrender, lawful repurchase, cancellation and pending disputes. [Regulation 2023/956 arts 3(24), 6(2)(c), 20–24, 31](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

### Free-allocation factor is not the importer's effective tax rate

| Production year | CBAM factor reducing EU ETS free allocation; use only within the statutory benchmark calculation | Official basis |
|---|---|---|
| 2026 | 97.5% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| 2027 | 95% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| 2028 | 90% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| 2029 | 77.5% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| 2030 | 51.5% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| 2031 | 39% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| 2032 | 26.5% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| 2033 | 14% | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| From 2034 | No CBAM factor applies: free allocation for the relevant goods ends, rather than the import itself becoming exempt. | [Directive 2003/87/EC art 10a(1a)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |

The factor schedule is in the ETS Directive, not CBAM art 36 or Annex II. The actual certificate adjustment uses Regulation 2025/2620 and the relevant production year, benchmark, correction factor and precursor data. A 97.5% factor does not prove that certificates equal 2.5% of the import's gross actual emissions. [Implementing Regulation 2025/2620 Annex points 2–4](https://publications.europa.eu/resource/celex/32025R2620).

## Exceptions and edge cases

### 1. Indirect emissions differ by period and exact goods

Transitional reports collect direct and indirect emissions under the transitional methods; the old blanket exclusion for iron/steel and aluminium during that period was wrong. For definitive liability, only the goods listed in Annex II use direct emissions alone: its listed iron/steel goods, aluminium, hydrogen and electricity. Cement, fertilisers and the Annex I agglomerated iron ore entry 2601 12 00 require the applicable indirect-emissions treatment. Do not replace the Annex II list with a whole-sector label. [Regulation 2023/956 arts 7(1), 35(2), Annexes I–II](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2023/1773 art 3(2)–(3)](https://publications.europa.eu/resource/celex/32023R1773); [Implementing Regulation 2026/1740 recital 8](https://publications.europa.eu/resource/celex/32026R1740).

### 2. Small imports and the historical low-value rule

Use enacted art 2a and Annex VII for 2026, not the old per-consignment low-value exemption or the description of a pending Omnibus proposal. The original Regulation art 2(3)(a)–(b) linked goods/traveller relief to Regulation 1186/2009 art 23; the current text removes that general low-value route. The exact historical EUR 150 statement is reserved under Sources until its linked customs provision is separately read. It is not a 2026 exemption. [Original Regulation 2023/956 art 2(3)](https://publications.europa.eu/resource/celex/32023R0956); [current Regulation 2023/956 arts 2(3), 2a, Annex VII](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

### 3. Returned goods and processing

Do not use an unexplained EU-origin/re-import label as universal relief. Definitive returned goods qualifying under UCC art 203 are reported separately with zero embedded emissions under CBAM art 6(5). Inward-processed outputs use the original relevant inputs' emissions even when the output CN is outside Annex I, including the specified returned processed products. Outward-processed Annex I goods use the outside-EU processing emissions only. Transit, warehousing or inward processing before free circulation does not by itself equal the ordinary import trigger, but later release and special offshore rules must still be tested. Historical transitional art 34 excludes the specified outward-processed and returned goods and has its own inward-processing reporting rule. [Regulation 2023/956 arts 2, 3(4), 6(3)–(5), 34](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2023/1773 art 6](https://publications.europa.eu/resource/celex/32023R1773).

### 4. Precursors and production routes

Include the relevant Annex I precursors from non-exempt origins in complex-goods emissions. Apply the sector system boundaries and actual production route rather than a commercial finished-goods label. For definitive actual calculations, multiple precursor periods/installations ordinarily require the prescribed weighted average; the evidence-supported single-installation/subset exception and combined actual-process/default-precursor route remain available. A joint production process may avoid a separate precursor calculation where its legal conditions are met; it does not justify double counting or omission. [Regulation 2023/956 Annex IV(3)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2025/2547 arts 4(6)–(9), 13–15](https://publications.europa.eu/resource/celex/32025R2547).

### 5. Certificate holding, repurchase and cancellation

The current repurchase cap is the number the declarant had an obligation to purchase under art 22(2) during the calendar year of purchase, not 1/3 of certificates held at each quarter end. Request repurchase by 31 October in the year certificates were surrendered; the repurchase price is the original purchase price. Where expected imports never cross the threshold, art 23(2) provides the all-certificates repurchase route. Certificates bought in 2027 for 2026 emissions may only be repurchased in 2027. [Regulation 2023/956 art 23](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

On 1 November each year the Commission cancels remaining certificates bought in the year before the preceding calendar year without compensation. The special cancellation for certificates bought for 2026 emissions is 1 November 2027. Cancellation is suspended to the extent of a pending disputed surrender amount notified by the competent authority. Do not describe unsurrendered certificates as automatically cancelled on the following 31 May. [Regulation 2023/956 art 24](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

### 6. Penalties are not a multiple of the auction price

| Failure | Rule and conditions | Official basis |
|---|---|---|
| Transitional reporting | EUR 10–50 per tonne of unreported emissions, increased with the European consumer-price index; applies to the specified failure to take necessary submission/correction steps. Authority factors matter. Higher penalties apply for more than 2 consecutive incomplete/incorrect reports or a reporting failure exceeding 6 months. | [Implementing Regulation 2023/1773 art 16](https://publications.europa.eu/resource/celex/32023R1773) |
| Authorised declarant surrender shortfall | Per missing certificate, the ETS excess-emissions penalty applicable in the import year: statutory base EUR 100 per tonne, with the art 16(4) index increase. Do not quote an unindexed base as the payable 2026 amount. A conditional reduction can apply for incorrect third-party information; payment ordinarily does not discharge surrender. | [Regulation 2023/956 art 26(1), (1a), (3)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Directive 2003/87/EC art 16(3)–(4)](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) |
| Unauthorised non-compliant import | Normally 3–5 times that penalty for each missing certificate, subject to the statutory factors. For an unauthorised importer crossing the mass threshold, all the year's covered emissions count; the limited reduction for a crossing no more than 10% above the threshold or art 17(7a) cases cannot go below the ordinary shortfall penalty. The special payment/discharge rule is in art 26(2a), not the authorised-declarant rule. | [Regulation 2023/956 art 26(2)–(4a)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) |

Apply the authority's current indexed amount and national enforcement/appeal procedure before producing a payable penalty. The old formula using 3 times the preceding year's average certificate price is withdrawn. Authorisation and customs release remain a separate compliance issue. [Regulation 2023/956 arts 4, 17, 25–26](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

### 7. Verification and accreditation

Actual embedded emissions must be verified under art 8 and Annex VI. Use Implementing Regulation 2025/2546 for verification and Delegated Regulation 2025/2551 for accreditation; EU ETS accreditation under 2018/2067 is relevant to an application/extension but is not automatic CBAM accreditation. Defaults themselves do not require an art 8 actual-emissions verification opinion; actual portions of a combined calculation still do. Check the legal person's accreditation for the relevant CBAM activity group and validity when the report is issued. [Regulation 2023/956 arts 8, 18, Annex VI](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Delegated Regulation 2025/2551 arts 1–4](https://publications.europa.eu/resource/celex/32025R2551).

A verifier established outside the EU may apply to a member state's national accreditation body under art 3(2). Do not replace this with an assumed recognition of any non-EU certificate. The distinct mutual-recognition rules concern accepted national accreditation bodies and the conditions in arts 23–24. Verification follows the required physical-visit rule unless the actual virtual-visit/waiver or extraordinary-circumstance conditions are met; reasonable assurance is not an unconditional guarantee. Use the current registry report template and retain the verifier's report. [Delegated Regulation 2025/2551 arts 1(9), 3, 23–24](https://publications.europa.eu/resource/celex/32025R2551); [Implementing Regulation 2025/2546 arts 2–6, Annex](https://publications.europa.eu/resource/celex/32025R2546).

### 8. UK CBAM comparison: separate regime from 2027

The UK policy summary, read on 15 November 2026, states commencement on 1 January 2027 and specified goods in 5 sectors: aluminium, cement, fertiliser, hydrogen, iron and steel. The earlier list including ceramics and glass is superseded; electricity is not in that current sector list. This does not establish identical EU/UK methodologies or automatic mutual credit. For goods moving through the UK, map each import trigger, origin, processing and separately available carbon-price relief; potential double pricing requires a documented specialist assessment. This skill does not compute the UK charge or FTA preference. [HMRC policy summary sections 1–4](https://www.gov.uk/government/publications/carbon-border-adjustment-mechanism-cbam-policy-summary/carbon-border-adjustment-mechanism-cbam-policy-summary); [EU Regulation 2023/956 arts 2, 6, 9](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

## Worked cases

### 1. Decide whether another shipment changes the annual exemption

Hypothetical EU-established importer in 2026, acting in its own name: all goods are properly classified Annex I steel/aluminium from non-exempt origins, there are no other imports or artificial arrangements, and no electricity/hydrogen. The importer has 40 tonnes steel and 10 tonnes aluminium: 50 tonnes total, so the art 2a mass exemption still applies. An additional 0.1 tonne aluminium takes the total to 50.1 tonnes, so the alternative crosses the threshold and brings the whole year's covered imports into the obligations. The importer must arrange authorisation before the expected crossing; the example is not a permission to import first and apply later. If valid verified definitive direct intensities are supplied as hypothetical inputs of 2, 0.5 and 1 tCO2e/tonne for those batches, whole-year gross emissions on the crossing alternative are 80 + 5 + 0.1 = 85.1 tCO2e, not merely the last batch's 0.1. These are derived example amounts, not published default intensities or certificates payable. [Regulation 2023/956 arts 2a, 5(1b), 6(2), Annexes II, VII](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

```oa-check
name: CBAM annual mass boundary and whole year emissions
inputs:
  steel_mass: 40
  aluminium_mass: 10
  extra_aluminium: 0.1
  threshold: 50
  steel_intensity: 2
  aluminium_intensity: 0.5
  extra_intensity: 1
steps:
  - first_total: steel_mass + aluminium_mass
  - first_margin: threshold - first_total
  - second_total: first_total + extra_aluminium
  - second_excess: second_total - threshold
  - steel_emissions: steel_mass * steel_intensity
  - aluminium_emissions: aluminium_mass * aluminium_intensity
  - extra_emissions: extra_aluminium * extra_intensity
  - whole_year_emissions: steel_emissions + aluminium_emissions + extra_emissions
expected:
  first_total: 50
  first_margin: 0
  second_total: 50.1
  second_excess: 0.1
  whole_year_emissions: 85.1
```

### 2. Recompute a complex good before asking for certificates

Hypothetical 2026 Annex I steel article: the importer has 60 tonnes and is not mass-exempt. Proper installation/system-boundary and attribution work, including verification, supplies 200 tCO2e attributed direct process emissions, 1,000 tCO2e relevant precursor emissions and production activity of 500 tonnes of that good. The precursor is in Annex I from a non-exempt origin; its emissions are not already included in the process figure. The specific embedded emissions are (200 + 1,000) / 500 = 2.4 tCO2e/tonne and gross emissions for the import are 60 × 2.4 = 144 tCO2e (derived). This Annex II steel good uses direct emissions for the definitive computation. The next step requires the actual corresponding free-allocation and any carbon-price-reduction worksheet. Gross 144 is not itself the surrender number; multiplying it by the phase-in percentage is not a valid substitute for that missing work. No statutory benchmark, default intensity, foreign credit or certificate price is invented in this example. [Regulation 2023/956 arts 6–9, 31, Annexes II, IV(3)](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation 2025/2620 Annex points 2–4](https://publications.europa.eu/resource/celex/32025R2620).

```oa-check
name: CBAM complex good specific and imported emissions
inputs:
  attributed_process_emissions: 200
  relevant_precursor_emissions: 1000
  production_activity: 500
  imported_mass: 60
steps:
  - total_production_emissions: attributed_process_emissions + relevant_precursor_emissions
  - specific_embedded_emissions: total_production_emissions / production_activity
  - imported_embedded_emissions: imported_mass * specific_embedded_emissions
expected:
  total_production_emissions: 1200
  specific_embedded_emissions: 2.4
  imported_embedded_emissions: 144
```

## Output specification

The reviewer brief must preserve these deliverables:

1. Goods inventory: every relevant import's CN/TARIC, quantity, origin, procedure, installation and importer/declarant of record.
2. Scope determination: Annex I match/exclusions, origin exemption and calendar-year threshold calculation, including electricity/hydrogen and special procedures.
3. Authorisation evidence: application/approval/pending/refusal dates, representative mandate, establishment, EORI and any provisional-import basis.
4. Emissions table: direct/indirect treatment for the correct period and exact goods, source installation, production route, methodology, units and per-shipment totals.
5. Default/estimate evidence: actual selected definitive row/version/mark-up where used; for transitional complex-goods estimates, the emissions-based art 5 test. Do not report an invented quarterly weight cap.
6. Carbon-price worksheet and documentation: actual payment, rebates, independent certification, legal conversion basis and any unresolved default-credit route.
7. Certificate schedule: legally computed free-allocation adjustment and credit, required surrender, import-quarter price basis for 2026, account inventory and movements.
8. Historical quarterly report package through Q4 2025, including registry payload/export if available, correction status and submission evidence; do not invent a current XML schema.
9. Annual declaration draft for the definitive period, applicable verification reports, quantities, adjusted certificates and supporting records.
10. Reviewer questions: every unresolved fact, legal rule and document flagged as [T2] or [T3], with the affected result held open.

## Self-checks

- [ ] CN/TARIC and description matched to Annex I and its exact exclusions.
- [ ] Non-preferential origin and Annex III/military/offshore exception tested.
- [ ] Calendar-year mass aggregation and representative-specific duties tested; electricity/hydrogen not mass-exempted.
- [ ] Authorisation/application and any provisional route evidenced for the relevant import dates.
- [ ] Installation/operator and production data documented, including the relevant precursors.
- [ ] Method, functional unit, reporting period and actual/default route correct for transitional or definitive rules.
- [ ] Historical estimates tested against emissions of complex goods; no weight cap assumed.
- [ ] Direct/indirect treatment follows the precise period and Annex II goods list.
- [ ] Carbon-price claim has actual legal and payment/rebate/certification support, or remains uncomputed.
- [ ] Free-allocation adjustment uses the applicable benchmark method and production year, not a bare percentage of actual emissions.
- [ ] Actual emissions verified by a properly scoped accredited CBAM verifier; records retained.
- [ ] Certificate inventory, purchases, holding, surrender, repurchase, cancellation and disputes reconciled for the correct dates.
- [ ] Historical quarter-end filing/correction and definitive annual deadlines checked separately.
- [ ] Every [T2]/[T3] item and missing source is visible to the reviewer and excluded from approved computations.

## When to refuse or refer

1. Do not extend CBAM by analogy to a CN code outside Annex I. Still test the express inward-processing-input rule before declaring an output outside the obligations. Refer disputed classifications and origin to a qualified customs specialist.
2. Do not use historical defaults beyond the actual transitional method/estimation conditions, or a current default without its exact operative row and required mark-up. No 20%-of-weight rule exists in the cited transitional provision.
3. Do not deduct a carbon price without the applicable art 9 route and evidence. Hold the reduction where the conversion/default-price rule is not established; never replace effective payment with a nominal rate.
4. Do not exclude transitional indirect emissions for steel/aluminium. For definitive goods, do not include indirect emissions for Annex II items or omit them for other covered goods merely because of a broad sector label.
5. Do not design circumvention, artificial splitting or cosmetic code changes. Art 27 addresses changes lacking sufficient economic justification; modifications that genuinely alter essential characteristics are a separate legal classification question, not advance clearance for avoidance. Escalate genuine commercial restructurings and specialist uncertainties without recommending evasion. [Regulation 2023/956 art 27](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1).

## Sources

Written by Codex. Not reviewed by an accountant. The source check below records the writer's actual reading on 15 November 2026; it is not accountant attestation. The legal documents' original/adoption years are not the tax year of this skill. Official English legal texts were opened through the Publications Office resolver; consolidated texts are documentation tools and their authentic amending acts remain the legal instruments.

| Source | Actual scope read | Read date |
|---|---|---|
| Direct official DOC_1 representations of Regulations 2023/956 and 2025/2621, and Directive 2003/87/EC linked below | Read for: On 16 November, representation identity was confirmed against the prior complete-review bodies. Article 22(1)–(3) and 23, the corrected Annex I opening with arts 1–2, and art 10a(1a) with neighboring allocation context were reread. The original 15 November scopes and dates below are retained; no new complete annex review is claimed. | 2026-11-16 |
| [Regulation 2023/956, consolidated 20 October 2025, incorporating 2025/2083](https://publications.europa.eu/resource/cellar/a61c0d38-bf6a-11f0-a612-01aa75ed71a1.0007.02/DOC_1) | Read for arts 1–9; 17–24; 26–27; 31–36; Annexes I–VI and Annex VII threshold. Relevant neighboring definitions/exceptions and Annex IV equation images read. | 2026-11-15 |
| [Implementing Regulation 2023/1773, transitional rules](https://publications.europa.eu/resource/celex/32023R1773) | Read for recitals 1–13; arts 1–9, 13–17. Operator/installation information, indirect reporting, alternative methods, estimation and penalties; no claim of reading every technical annex. | 2026-11-15 |
| [Implementing Regulation 2025/2547, definitive methods](https://publications.europa.eu/resource/celex/32025R2547) | Read for arts 2–16: system boundaries, functional units, monitoring/attribution, periods, electricity/indirect proof, defaults and precursor combinations. Technical annexes are a required job-specific handoff, not wholly researched here. | 2026-11-15 |
| [Implementing Regulation 2025/2621, consolidated default rules](https://publications.europa.eu/resource/cellar/c606a88b-a0ac-11f1-b25c-01aa75ed71a1.0004.02/DOC_1) | Read for art 1–2 and corrected Annex I opening selection/mark-up/route rules. No complete country/product numeric table read or published in this skill. | 2026-11-15 |
| [Implementing Regulation 2026/1740, correcting defaults](https://publications.europa.eu/resource/celex/32026R1740) | Read for recitals 1–15, arts 1–2 and Annex I opening rules; retroactive application and corrected total/default distinctions. No claim of reading every replacement table. | 2026-11-15 |
| [Implementing Regulation 2025/2620, free allocation](https://publications.europa.eu/resource/celex/32025R2620) | Read for recitals 1–20, arts 1–5, Annex points 1–4 and 5.1; equation images 1–6, actual/default and precursor principles. Product benchmark values and specialist classifications not approved here. | 2026-11-15 |
| [Directive 2003/87/EC, consolidation 1 March 2024](https://publications.europa.eu/resource/cellar/1c8a1afb-f104-11ee-8e14-01aa75ed71a1.0006.02/DOC_1) | Read for art 10a(1a), surrounding free-allocation context and art 16(1)–(4): factor schedule and indexed excess-emissions penalty. Cross-checked against the current CBAM cross-references; no domestic ETS computation. | 2026-11-15 |
| [Implementing Regulation 2025/2546, verification](https://publications.europa.eu/resource/celex/32025R2546) | Read for recitals 1–12, arts 1–7 and Annex identification/report elements: site-visit exceptions, materiality and report template. | 2026-11-15 |
| [Delegated Regulation 2025/2551, accreditation](https://publications.europa.eu/resource/celex/32025R2551) | Read for recitals, arts 1–4 and 23–26; EU/non-EU applicants, scope extension and mutual recognition/peer-evaluation conditions. | 2026-11-15 |
| [Original Regulation 2023/956](https://publications.europa.eu/resource/celex/32023R0956) | Read for original arts 1–2, including historical low-value linkage; not used as current definitive law. | 2026-11-15 |
| [Commission definitive-regime page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-definitive-regime_en) | Read for definitive commencement, threshold summary, quarterly/weekly pricing, sectors and corrected-defaults routing. Statutory exceptions govern. | 2026-11-15 |
| [HMRC CBAM policy summary](https://www.gov.uk/government/publications/carbon-border-adjustment-mechanism-cbam-policy-summary/carbon-border-adjustment-mechanism-cbam-policy-summary) | Read for sections 1–4 and adjacent product/special-procedure context: commencement and five-sector scope only; no UK tax/filing computation approved. | 2026-11-15 |

**Not yet confirmed:** the original specific EUR 150 historical low-value figure requires a separate read of Regulation 1186/2009 art 23; its direct EUR-Lex fetch returned a robot-check page. The original Northern Ireland electricity exception has not been independently established from its separate applicable instruments and must not be inferred from Annex III. The original generic “Commission's 2025 sectoral guidance” is not an identified/read operative document and cannot approve a production-route method. The original platform-vendor speculation is unconfirmed and must not be used. A current country's product-specific default, benchmark/correction-factor worksheet, foreign-carbon-price conversion/default-price rule, exact indexed payable penalty, declaration XML schema, and any specialist installation-specific monitoring/verification exception must be attached and read for the actual engagement before the affected computation or filing is usable. The Commission certificate-price announcement fetch returned HTTP 429; no actual quarterly price is supplied here. None of those open items is resolved by the illustrative examples.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. CBAM scope, methodology, and pricing are evolving rapidly with Commission delegated acts and the 2025 Omnibus simplification. Every output must be reviewed and signed off by a credentialed customs / CBAM specialist before submission of a quarterly report or annual declaration.
