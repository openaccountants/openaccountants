---
name: cbam-carbon-border-adjustment
description: "Use this skill whenever an EU importer (declarant), an indirect customs representative, or a non-EU producer asks about the EU Carbon Border Adjustment Mechanism. Trigger on phrases like \"CBAM\", \"carbon border adjustment\", \"CBAM certificates\", \"embedded emissions\", \"default values\", \"verified emissions\", \"CN code 7208\", \"CN code 28080000\", \"fertiliser CBAM\", \"cement CBAM\", \"aluminium CBAM\", \"hydrogen CBAM\", \"electricity CBAM\", \"iron and steel CBAM\", \"quarterly CBAM report\", \"CBAM declarant\", \"CBAM authorised declarant\", or any request to assess CBAM scope, compute embedded emissions, prepare the quarterly report (transitional period) or annual CBAM declaration (definitive period from 2026). Covers Regulation (EU) 2023/956, Implementing Regulation (EU) 2023/1773 (transitional period reporting), the Default Values Implementing Regulation and the Commission's 2025 sectoral guidance. Does NOT cover: emissions trading system (EU ETS), domestic carbon taxes (UK CBAM, Australia Safeguard Mechanism, California CCA), customs tariff / preference rules, or product origin determination. ALWAYS read this skill before computing CBAM exposure or preparing a CBAM report."
version: 0.1
jurisdiction: EU-27
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CBAM Carbon Border Adjustment

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It implements:

- **Regulation (EU) 2023/956** of 10 May 2023 establishing the CBAM.
- **Implementing Regulation (EU) 2023/1773** of 17 August 2023 on reporting obligations during the transitional period (1 October 2023 – 31 December 2025).
- **Definitive period rules** entering into force 1 January 2026 (financial liability via CBAM certificates plus annual CBAM declaration).
- **Default values** and verified-emissions methodologies as published by the Commission.

**Tax year coverage.** Current for **calendar 2025** (transitional reporting) and the **early definitive period 2026**, reflecting the **Omnibus simplification proposal of February 2025** which introduced a small-importer de minimis (50 tonnes/year per declarant) and clarified default-value usage.

**The reviewer is the customer of this output.** CBAM emissions data flows from production-site engineering records, customs classifications, and external verification. Every output must be reviewed by a credentialed practitioner (customs broker, EU import lawyer, or accredited verifier under Implementing Regulation (EU) 2018/2067) before submission.

## Section 1 — Scope statement

This skill covers:

- **Six initial CBAM sectors** plus the scope expansions added in 2023:
  - **Cement** — CN codes 2507 00 80, 2523 (clinker, cement, white cement, aluminous cement)
  - **Iron and steel** — CN chapter 72 (most subheadings) plus selected articles of 7301, 7302, 7303, 7304, 7305, 7306, 7307, 7308, 7311, 7318, 7326
  - **Fertilisers** — CN chapter 31 (nitrogen fertilisers, mixed fertilisers) plus 2808 00 00 (nitric acid)
  - **Aluminium** — CN chapter 76 (unwrought, semi-fabricated, articles) and selected wrought products
  - **Electricity** — CN code 2716 00 00 (only cross-border supplies)
  - **Hydrogen** — CN code 2804 10 00
- **Embedded emissions** computation: direct, indirect (where applicable), default values, verified actual values.
- **Quarterly transitional reports** (Q3 2023 → Q4 2025) and **annual CBAM declaration** (from 2026, due 31 May for prior calendar year).
- **CBAM certificates** — purchase, sale-back, surrender (definitive period).
- **Adjustment for carbon price paid in country of origin**.
- **Authorised CBAM declarant** application and obligations.

This skill does NOT cover:

- **EU ETS** stationary installations, aviation, maritime — see `eu-ets-allowances.md` (forthcoming).
- **Other carbon-pricing regimes** (UK CBAM from 2027, Canada OBPS, Australia Safeguard Mechanism, California CCA, Korea K-ETS).
- **Customs tariff and origin rules** beyond the minimum required to classify CBAM goods.
- **Preference treatment** under FTAs.
- **Indirect emissions** for sectors where they are out of scope (currently iron and steel and aluminium — confirm the latest delegated act).

## Section 2 — Timeline

**Timeline table**

| Date | Event |
| --- | --- |
| 1 October 2023 | Transitional period begins; first quarterly report due |
| 31 January 2024 | First quarterly report (Q4 2023) due |
| 31 January 2025 | Quarterly report (Q4 2024) due |
| 1 January 2026 | Definitive period begins; financial liability via certificates |
| 31 January 2026 | Final quarterly transitional report (Q4 2025) due |
| 31 May 2027 | First annual CBAM declaration (for 2026) due, with certificate surrender |
| Phased ETS free allocation phaseout | 2026: 97.5% free → reduces to 0% by 2034 (annual schedule in Article 36) |

## Section 3 — Filing requirements

### Transitional period (to 31 December 2025)

- **[T1] Reporting declarant quarterly CBAM report** — Reporting declarant (importer or indirect customs representative) submits a quarterly CBAM report within one month of quarter end via the CBAM Transitional Registry.  _(Implementing Regulation (EU) 2023/1773)_
- **Contents of quarterly CBAM report** — Total quantity of CBAM goods imported (by CN code and country of origin); Total embedded emissions (direct and where applicable indirect) in tonnes CO₂e per tonne of goods; Methodology used (verified actual data; default values from the Commission; equivalent national methodologies during a grace period); Carbon price paid in the country of production with supporting documentation.  _(Implementing Regulation (EU) 2023/1773)_
- **Transitional period flexibility** — Q3 2023 → Q3 2024: any methodology, including default values, allowed. From Q4 2024 onwards: must use actual values where available; default values only allowed within Commission-set limits.  _(Implementing Regulation (EU) 2023/1773)_

### Definitive period (from 1 January 2026)

- **[T1] Only an Authorised CBAM Declarant can import CBAM goods** — Only an Authorised CBAM Declarant can import CBAM goods. Application via the national Competent Authority of the importer's Member State. Approval requires: No serious or repeated infringements of customs, tax, or market abuse rules; Financial standing; Established in the Member State.  _(Regulation (EU) 2023/956)_
- **Annual CBAM declaration contents** — Annual CBAM declaration due 31 May for the prior calendar year, containing: Total quantity imported per CN code per country of origin; Total embedded emissions (verified by accredited verifier, except where default values used); Total CBAM certificates to be surrendered; Carbon price paid in country of origin.  _(Regulation (EU) 2023/956)_
- **Certificate purchase** — Declarant buys CBAM certificates at the weekly average price of EU ETS auctions, on the Common Central Platform managed by a designated entity (likely the European Energy Exchange).  _(Regulation (EU) 2023/956)_
- **Certificate surrender** — Certificate surrender: equal to embedded emissions × applicable factor (reflecting any ETS free allocation phasing).  _(Article 31 / Annex II)_

## Section 4 — Computing embedded emissions

### Step 1 — Classify the import

- **[T1] Match the goods to a CN code** — Match the goods to a CN (Combined Nomenclature) code. CBAM scope is determined by Annex I of Regulation (EU) 2023/956 — a list of specific 4-/6-/8-digit CN codes. If the CN code is not in Annex I, the import is out of scope (this period).  _(Annex I of Regulation (EU) 2023/956)_

### Step 2 — Determine the country of origin

- **[T1] CBAM applies to imports from third countries EXCEPT** — Use customs rules of origin. CBAM applies to imports from third countries EXCEPT: EEA states (Iceland, Liechtenstein, Norway); Switzerland; Certain territories with full EU ETS coverage (Northern Ireland for electricity, Büsingen, etc. — Annex III).  _(Annex III)_

### Step 3 — Identify the production installation

- **[T1] Embedded emissions computed at installation level** — Embedded emissions are computed at the installation level. Importer must obtain from the third-country operator: Installation identification (name, address, UNLOCODE if available, operator name); Direct emissions: Specific Direct Embedded Emissions (SDEE) per tonne of product; Indirect emissions (electricity used in production) — applicable currently for cement, fertilisers, electricity, hydrogen; not applicable for iron and steel or aluminium during the transitional period and currently in the definitive period (confirm latest delegated act); Production route (e.g., for steel: integrated route via BOF vs electric arc furnace); Carbon price paid (per Article 9).  _(Article 9)_

### Step 4 — Methodology selection

- **[T1] Hierarchy (Annex IV)** — 1. Actual emissions data from the installation, calculated per the EU methodology equivalent to ETS Monitoring and Reporting Regulation (EU) 2018/2066, verified by an accredited verifier. 2. Default values — Commission-published per sector and country/region. Use only: During transitional period freely until end of Q3 2024; From Q4 2024: only for ≤ 20% of imported product weight per declarant per quarter; In definitive period: only where actual values cannot reasonably be obtained. 3. Other methodologies — equivalent national methodologies of the producing country may be accepted during transitional period; not generally in definitive period.  _(Annex IV)_

### Step 5 — Compute embedded emissions

- **[T1] Embedded Emissions formula** — Embedded Emissions (tCO₂e) = Quantity (t) × Specific Embedded Emissions (tCO₂e / t). Sum across all shipments for the reporting period.  _(Section 4, Step 5)_

### Step 6 — Adjustment for carbon price paid

- **[T1] Article 9 carbon price deduction conditions** — Article 9 allows a deduction for carbon price paid in country of origin on the embedded emissions of the imported goods, provided: The price was effectively paid (e.g., national ETS, carbon tax); Documentation provided (proof of payment, accreditation of the carbon-pricing regime); Not offset by subsidies or other rebates. Adjustment in EUR converted at exchange rate of payment date.  _(Article 9)_

### Step 7 — Compute certificate surrender (definitive period from 2026)

- **Certificates to surrender formula** — Certificates to surrender = Embedded Emissions − Free Allocation Factor − Carbon Price Adjustment  _(Annex II)_
- **Free Allocation Factor (Annex II)** — In 2026 = 97.5% of the free allocation share for the equivalent ETS product (i.e., importer surrenders only 2.5% × benchmark emissions); reduces annually to 0% in 2034. Each certificate represents 1 tCO₂e and is purchased at the weekly average EU ETS auction price.  _(Annex II)_

## Section 5 — Edge cases and special rules

### 5.1 Indirect emissions

- **Indirect emissions scope** — Currently in scope for: cement, fertilisers, electricity, hydrogen. Out of scope (transitional + early definitive period) for: iron and steel, aluminium. The Commission's 2025 review will reassess scope inclusion.

### 5.2 De minimis exemption (Article 2(3) and Omnibus 2025)

- **[T1] De minimis exemption** — Originally: shipments ≤ EUR 150 in value exempt. Omnibus 2025 (proposed): 50-tonne annual de minimis per importer. Confirm the as-enacted text before relying.  _(Article 2(3) and Omnibus 2025)_

### 5.3 Re-imports of EU-originating goods

- **Re-imports of EU-originating goods out of scope** — Goods of EU origin that are re-imported are out of scope.

### 5.4 Inward processing and special procedures

- **Suspensive procedures do not trigger CBAM** — Goods placed under inward processing, customs warehousing, transit, or other suspensive procedures are generally not yet released for free circulation and do not trigger CBAM. CBAM triggers on release for free circulation.

### 5.5 Precursor materials

- **Precursor materials must be included** — For complex goods (e.g., steel articles, aluminium articles), embedded emissions of CBAM-relevant precursor materials must be included. The Commission's sectoral guidance maps each CN code to its in-scope precursors.

### 5.6 Common Central Platform certificate handling

- **Certificate account handling** — Authorised CBAM Declarants maintain a certificate account. Up to 1/3 of certificates held at the end of each quarter may be sold back at original price (mitigates price volatility). Certificates not surrendered by 31 May of the year following the import year are cancelled.

### 5.7 Penalty exposure

**Penalty exposure table**

| Trigger | Penalty |
| --- | --- |
| Failure to file quarterly report (transitional period) | EUR 10 – EUR 50 per tonne of unreported emissions (Implementing Regulation (EU) 2023/1773 Article 16) |
| Failure to surrender certificates (definitive period) | 3 × the average price of certificates over preceding year × shortfall in tonnes (Article 26) |
| Unauthorised import in definitive period | Goods may be denied release; declarant penalties per Member State implementation |

### 5.8 Verification requirements (definitive period)

- **[T1] Verification requirements** — Actual emissions data must be verified by an accredited verifier under Implementing Regulation (EU) 2018/2067. Default values do not require verification. The verifier must be accredited in an EU Member State; non-EU verifiers may operate through mutual recognition where established.  _(Implementing Regulation (EU) 2018/2067)_

### 5.9 Interaction with UK CBAM (from 2027)

The UK announced a domestic CBAM effective 1 January 2027 covering aluminium, cement, ceramics, fertilisers, glass, hydrogen, iron and steel (not electricity). Scope and methodology align broadly with EU CBAM. Goods that pass through the UK before importation to the EU may face double pricing in some scenarios — review preference treatment and customs sequencing.

## Section 6 — Output specification

The reviewer brief must include:

1. **Goods inventory** — every CBAM-relevant import: CN code, quantity, country of origin, installation, declarant of record.
2. **CBAM in-scope determination** — confirmation that CN code is in Annex I and country of origin is not exempt.
3. **Authorised CBAM Declarant status** — application date, approval date, or pending.
4. **Embedded emissions table** — direct and (where applicable) indirect, per shipment, with methodology source.
5. **Default-value usage tracking** — percentage of weight using default values per quarter to confirm ≤ 20% cap (Q4 2024 onwards).
6. **Carbon price adjustment computation** — per shipment with supporting documentation.
7. **Certificate surrender schedule** (definitive period) — total certificates due, free allocation factor applied, current certificate inventory.
8. **Quarterly transitional reports** — XML payload per quarter through Q4 2025.
9. **Annual CBAM declaration** draft (definitive period) — verified emissions, certificates to surrender, supporting documentation.
10. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 7 — Self-checks

Before delivering output, verify:

- [ ] CN code matched to Annex I CBAM scope list (8-digit precision where required).
- [ ] Country of origin not on Annex III exemption list.
- [ ] Authorised CBAM Declarant status confirmed for definitive-period imports.
- [ ] Installation identification documented with operator-provided data.
- [ ] Embedded emissions methodology hierarchy applied (verified actual → defaults within cap).
- [ ] Default-value usage tracked at ≤ 20% of weight per declarant per quarter from Q4 2024.
- [ ] Indirect emissions included only for sectors in scope.
- [ ] Carbon price adjustment supported by proof of payment, not subsidy-offset.
- [ ] Free allocation factor matches Annex II for the reporting year.
- [ ] Verification by accredited verifier for actual emissions in definitive period.
- [ ] Certificate inventory reconciled to surrender obligation.
- [ ] Quarterly reports filed within one month of quarter end.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 8 — Prohibitions

- **Prohibition: CN codes not in Annex I** — Do not apply CBAM to CN codes not in Annex I, even if commercially related (CBAM is enumerated, not analogous).  _(Annex I)_
- **Prohibition: default values beyond Q4 2024 limit** — Do not use default values beyond the transitional Q4 2024 limit without documenting the exception under Implementing Regulation (EU) 2023/1773 Article 4.  _(Implementing Regulation (EU) 2023/1773 Article 4)_
- **Prohibition: carbon price deduction without proof** — Do not deduct carbon price paid without proof of effective payment and a copy of the underlying regime certification.
- **Prohibition: indirect emissions for iron, steel, aluminium** — Do not treat indirect emissions as in scope for iron, steel, or aluminium during the transitional period and current definitive period (verify the latest delegated act).
- **Prohibition: advising on circumvention** — Do not advise on structuring imports to circumvent CBAM (e.g., processing in a third country to change CN code) without explicit escalation — anti-circumvention rules apply under Article 27.  _(Article 27)_

## Section 9 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. CBAM scope, methodology, and pricing are evolving rapidly with Commission delegated acts and the 2025 Omnibus simplification. Every output must be reviewed and signed off by a credentialed customs / CBAM specialist before submission of a quarterly report or annual declaration.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
