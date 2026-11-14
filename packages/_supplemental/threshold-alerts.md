---
name: threshold-alerts
description: "Intelligence skill that detects when the user is near important tax thresholds. Covers 14 threshold checks across EU and ten national jurisdictions (EU, US, UK, DE, AU, IN, ES, NL, SG, MT, CA). For each threshold: calculates proximity, determines direction of travel, and recommends specific action. Flags the crossing point where obligations change materially."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
type: cross-country-method
last_updated: 2026-11-14
depends_on:
  - workflow-base
category: intelligence
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tooling
---

# Threshold Alerts v0.2

## What this file is

**Obligation category:** INTEL (Intelligence / Cross-cutting)
**Functional role:** Threshold proximity detection, cliff warnings, proactive alerts
**Status:** Active

This is an intelligence skill that loads on top of `workflow-base`. It monitors the user's financial data against statutory thresholds where obligations change materially - registration requirements activate, deductions phase out, tax rates jump, or filing complexity increases.

**The reviewer is the customer of this output.** Threshold alerts are addressed to the credentialed reviewer, who decides whether action is needed.

> **Disclaimer.** Threshold amounts are based on publicly available statutory rules and may change with legislation. Currency conversions, timing of income recognition, and specific definitions of "turnover" or "income" vary by jurisdiction and may affect whether a threshold applies. All threshold assessments must be verified by a credentialed professional in the relevant jurisdiction. This is not legal or tax advice.

## Scope

### Section 1 - Scope statement

This skill covers:

- **Jurisdictions:** EU (cross-border), US, UK, DE, AU, IN, ES, NL, SG, MT, CA
- **Threshold types:** VAT/GST registration, income tax cliffs, deduction phase-outs, social security caps, simplified regime limits
- **Output:** Proximity report with distance, direction, and recommended action

This skill does NOT cover:

- Corporate tax thresholds or employer-side thresholds
- Full entity-level computations: still identify the actual taxpayer, associated businesses and aggregation needed for a supported threshold; do not omit an applicable legal test merely because it involves another entity
- Real-time monitoring (this runs on demand or when triggered by a computation skill)
- Full tax-return computations or automatic registrations. Section 4 ranks optional planning suggestions; it never suppresses a statutory obligation or missing-evidence alert

## The method, step by step

### Section 2 - Workflow

### Step 0 - Gather inputs

- **Gather inputs:** confirm taxpayer/entity, residence/establishment, filing status, actual tax/financial/calendar year, effective rule date and existing registrations/elections. Extract the required sales, receipts, income and associated-business records with transaction dates, currency, VAT treatment and recognition basis. Reconcile rolling turnover, calendar-year turnover, net receipts, taxable income before a deduction, adjusted net income and income for surcharge purposes separately. Obtain the threshold-specific facts, such as eligible cross-border B2C supplies, profession, cash-receipt proportion or hospital-cover days/dependants. If a required fact or source is missing, report **incomplete - data needed**; do not supply a favourable default.

### Step 1 - Run threshold checks

- **Run threshold checks:** for each applicable test, record its source/date, actual measurement period, eligibility, included/excluded receipts and comparison operator. Compute the actual measured value, statutory amount, signed headroom (limit minus value), and percentage headroom (headroom divided by a non-zero limit, multiplied by one hundred). Preserve both prior-year and current-year tests where required. Distinguish a strict **exceeds** test from **at least**, a taper, cap or election condition; equality is not a universal breach. Classify the legal result first. Then assess direction from comparable prior-year figures and dated commitments. YTD / elapsed months times twelve is a labelled planning projection only, not a substitute for a statutory forward test; guard zero/partial periods, seasonality and inconsistent recognition. No trend evidence means **direction unknown**. Record the applicable official currency-conversion rule or mark the currency comparison unresolved.

### Step 2 - Classify proximity

**Proximity classification bands**

| Proximity band | Condition | Flag |
| --- | --- | --- |
| Distant, not a legal safety conclusion | More than 20% below a supported positive limit | GREEN |
| Watch | From 10% through 20% below the limit | AMBER |
| Near boundary | Non-negative headroom below 10%; equality separately tested under the law | RED |
| Statutory boundary met/crossed | The actual operator and all eligibility conditions are met | RED - ACTION, or a clearly labelled favourable cap/taper notice |
| Not applicable / unresolved | Evidence proves exclusion, or facts/source are insufficient; distinguish these results | GREY / INCOMPLETE |

### Step 3 - Generate action recommendations

- **Generate action recommendations:** for AMBER/RED, every activated obligation and every unresolved required test, explain what is happening, the actual legal change, the proposed action, its evidence and owner, application deadline, effective date and first affected transaction. Do not use a generic number of days after crossing. A social-security cap may reduce one charge without eliminating another. Compare lawful options using actual quoted fees and eligible relief conditions; do not fabricate insurance prices, marginal tax savings or authority approval. Deferring an invoice alone does not establish lawful deferral of revenue recognition. Produce proposals for the reviewer; do not file, register, buy cover or alter records.

### Step 4 - Produce output

- **Produce output** , Format per Section 5.

## Section 3 - Master Threshold Table

### 3.1 EU - VAT One Stop Shop (OSS)

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Eligible intra-Community distance sales and B2C TBE place-of-supply threshold | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| **Jurisdiction** | EU; check establishment and origin of transport, not every B2C sale | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| **Amount** | EUR 10,000 exclusive of VAT, combined eligible TBE services and intra-Community distance sales; not separate allowances | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| **What happens if exceeded** | Once exceeded, apply destination place-of-supply rules for the relevant supplies. OSS is an optional reporting route, not itself a universal mandatory registration; establish actual VAT liability/exemption and national registrations | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| **What happens if below** | Origin place-of-supply treatment only if the single-Member-State establishment/transport and both-year conditions hold; a destination election binds for two calendar years | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| **Measurement period** | Current and preceding calendar years; no threshold for other B2C services or imported distance sales | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| **Action if approaching** | Prepare actual destination tax treatment, pricing and eligible OSS or national route before the crossing supply; check any separately applicable SME exemption | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| **Primary source** | European Commission OSS guide, place-of-supply threshold and optional schemes | [Official source](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |

### 3.2 US - QBI Deduction Phase-out

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | QBI limitation phase-in, not one automatic deduction cliff | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |
| **Jurisdiction** | US federal, actual filing status and eligible non-C-corporate business | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |
| **Amount** | 2026 taxable income before QBI deduction: MFJ USD 403,500 to USD 553,500; MFS USD 201,775 to USD 276,775; other returns USD 201,750 to USD 276,750 | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |
| **What happens if exceeded** | Apply actual SSTB exclusion and wage/property limitations through the relevant range; not every business loses its whole deduction at the start | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |
| **What happens if below** | Potential deduction remains subject to qualified income, taxable-income/net-capital-gain and other eligibility limits; not a guaranteed full twenty percent of every profit | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |
| **Measurement period** | Tax years beginning in 2026; do not substitute the old 2025 table | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |
| **Action if approaching** | Confirm SSTB classification and actual allowable retirement/HSA/health-insurance deductions, contribution limits and lawful timing with the country computation; do not invent deductible contributions to hit the limit | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |
| **Primary source** | IRS Rev. Proc. 2025-32 section .26, all three filing-status rows; IRS QBI overview for eligibility/limitations | [Official source](https://www.irs.gov/irb/2025-45_IRB) / [related source](https://www.irs.gov/newsroom/qualified-business-income-deduction) |

### 3.3 US - Social Security Tax Cap (OASDI)

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Combined OASDI base and continuing Medicare obligations | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |
| **Jurisdiction** | US federal; reconcile wages/tips and actual Schedule SE net earnings | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |
| **Amount** | 2026 combined Social Security base USD 184,500; SE components 12.4% OASDI and 2.9% Medicare | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |
| **What happens if exceeded** | OASDI applies only up to the remaining combined base; Medicare continues. Separate 0.9% Additional Medicare test: MFJ USD 250,000, MFS USD 125,000, other listed statuses USD 200,000 | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |
| **What happens if below** | Do not multiply raw business profit by the combined rate without the actual Schedule SE earnings computation and wage coordination | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |
| **Measurement period** | Applicable tax year; confirm non-calendar-year instructions where relevant | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |
| **Action if approaching** | Reforecast cash payments without treating reaching the cap as exemption from Medicare or a filing/payment obligation | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |
| **Primary source** | SSA contribution/base history for 2026; IRS self-employment tax rate and filing-status table | [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) / [related source](https://www.ssa.gov/oact/cola/cbb.html) |

### 3.4 UK - VAT Registration Threshold

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | UK compulsory VAT registration, two distinct timing tests | [Official source](https://www.gov.uk/register-for-vat) |
| **Jurisdiction** | UK ordinary taxable-turnover test; non-established suppliers and special acquisition/takeover rules need separate assessment | [Official source](https://www.gov.uk/register-for-vat) |
| **Amount** | Over GBP 90,000 taxable turnover, not at equality | [Official source](https://www.gov.uk/register-for-vat) |
| **What happens if exceeded** | Past test: apply within thirty days of the end of the crossing month; effective first day of the second month after crossing. Forward test: apply by the end of the thirty-day period; effective when the expectation was realised | [Official source](https://www.gov.uk/register-for-vat) |
| **What happens if below** | Below this ordinary threshold does not exclude non-established/special liabilities; voluntary registration may be available, and only exempt/out-of-scope supplies do not create ordinary taxable turnover | [Official source](https://www.gov.uk/register-for-vat) |
| **Measurement period** | Past twelve months, or expected taxable turnover over the limit in the next thirty days alone, with required inclusions such as zero-rated sales | [Official source](https://www.gov.uk/register-for-vat) |
| **Action if approaching** | Prepare pricing and actual VAT reporting/software obligations, verify input VAT eligibility, and assess any approved temporary-exceedance exception; do not make VAT effective automatically on the crossing day | [Official source](https://www.gov.uk/register-for-vat) |
| **Primary source** | HMRC registration, calculation, retrospective/prospective timing, late registration and special situations | [Official source](https://www.gov.uk/register-for-vat) |

### 3.5 UK - Personal Allowance Taper

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | UK adjusted-net-income Personal Allowance taper | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |
| **Jurisdiction** | UK; entitlement, income category and Scottish status matter | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |
| **Amount** | 2026-27 standard allowance GBP 12,570; adjusted net income over GBP 100,000 reduces it by GBP 1 per GBP 2, to zero at GBP 125,140 | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |
| **What happens if exceeded** | Apply the allowance reduction to the actual computation; a universal sixty-percent marginal rate is not a rule for every income/region | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |
| **What happens if below** | Full standard allowance only if otherwise entitled; other allowances and reliefs remain separate | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |
| **Measurement period** | UK tax year, sixth April through fifth April; compare adjusted net income, not gross receipts | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |
| **Action if approaching** | Assess actual qualifying pension or Gift Aid treatment and limits before changing adjusted net income; use lawful recognition, not arbitrary invoice shifting | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |
| **Primary source** | HMRC current 2026-27 rates and adjusted-net-income taper | [Official source](https://www.gov.uk/income-tax-rates/income-over-100000) |

### 3.6 DE - Kleinunternehmer (Small Business VAT Exemption)

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | German small-business VAT exemption, prior/current tests | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Jurisdiction** | DE domestic business; other-EU establishment has additional conditions under subsection four | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Amount** | Prior calendar-year Gesamtumsatz not above EUR 25,000 and current-year not above EUR 100,000; actual receipts-based statutory turnover excludes specified exempt/ancillary and capital-asset disposals | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **What happens if exceeded** | Do not wait automatically until next year: the current-year exemption condition fails once the current limit is exceeded. Determine the affected supply, filing and input-tax consequences from the German implementation | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **What happens if below** | Eligible domestic supplies are exempt under the actual scheme, not an unrestricted exemption for every cross-border transaction | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Measurement period** | Prior and current calendar years, not a forecast replacing actual current-year receipts | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Action if approaching** | Compare lawful election/input-tax effects; a waiver binds at least five calendar years. Startup and exact crossing-supply implementation require the country rule, not an invented universal forecast test | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Primary source** | UStG section 19 paragraphs one to six | [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |

### 3.7 AU - GST Registration Threshold

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Australian GST registration with statutory turnover measure | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |
| **Jurisdiction** | AU ordinary enterprise; not-for-profit and taxi/ride-sourcing rules differ | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |
| **Amount** | GST turnover AUD 75,000 or more; not-for-profit AUD 150,000 or more. Taxi/ride-sourcing regardless of turnover; fuel-credit claims also require registration | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |
| **What happens if exceeded** | ATO instructs registration within twenty-one days when the registration criterion is reached/expected; establish effective date and actual taxable-supply/BAS/input-credit rules rather than tax every receipt | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |
| **What happens if below** | Voluntary registration can be available, bringing actual GST/BAS duties; a below-limit ordinary business may still meet another registration trigger | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |
| **Measurement period** | Act section 188-10: projected turnover at least the limit, or current turnover at least the limit unless Commissioner satisfied projected turnover is below. Current month plus prior eleven, and current plus next eleven, apply the actual exclusions/grouping | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |
| **Action if approaching** | Monitor monthly; review GST-inclusive/exclusive contracts and eligible credits. Do not substitute total accounting sales or ignore projected-turnover exclusions for capital assets/cessation | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |
| **Primary source** | ATO education registration guidance; current GST Act sections 188-10 to 188-25 | [Official source](https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register) / [related source](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) |

### 3.8 AU - Medicare Levy Surcharge (MLS)

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Australian Medicare Levy Surcharge tiers and cover | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |
| **Jurisdiction** | AU actual single/family status, dependants, MLS income and uninsured days | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |
| **Amount** | 2026-27 single tiers: no surcharge through AUD 105,000; 1% from AUD 105,001 to AUD 123,000; 1.25% from AUD 123,001 to AUD 164,000; 1.5% from AUD 164,001 | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |
| **What happens if exceeded** | The relevant surcharge can apply for uncovered days, subject to exemptions and the actual surcharge base; it is distinct from the ordinary Medicare levy | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |
| **What happens if below** | At/below the applicable base tier no MLS; families use the corresponding family thresholds, with the specified dependent-child adjustment | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |
| **Measurement period** | First July to thirtieth June. The preceding 2025-26 single boundaries are AUD 101,000, AUD 118,000 and AUD 158,000; never apply the later year retrospectively | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |
| **Action if approaching** | Compare actual eligible hospital-cover quote, covered family members and days against the supported MLS computation. Extras-only, overseas/student or non-registered cover is not a substitute. No assumed policy market price | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |
| **Primary source** | Commonwealth privatehealth.gov.au MLS page, both financial-year tables, rates, dependants, cover and partial-year rules | [Official source](https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm) |

### 3.9 IN - Presumptive Taxation Threshold (44ADA)

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Indian professional presumptive method, latest verified filing cycle | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |
| **Jurisdiction** | IN resident individual or partnership other than LLP, specified profession; ITR-4 eligibility is a separate additional test | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |
| **Amount** | FY 2025-26 / AY 2026-27: gross receipts up to INR 75 lakh where cash receipts do not exceed 5% of total; otherwise up to INR 50 lakh | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |
| **What happens if exceeded** | Outside the applicable receipts/eligibility limit, assess actual books, audit and return requirements under the governing provisions; no universal automatic audit or July-to-October filing-date switch | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |
| **What happens if below** | Qualifying election generally uses fifty percent professional receipts and its books rules; separate ITR-4 income/exclusion conditions still apply | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |
| **Measurement period** | Latest verified 2025-2026 filing cycle only; do not relabel section 44ADA as the confirmed successor for FY 2026-27 | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |
| **Action if approaching** | Track actual receipts and cash proportion including equality at five percent; keep records proving eligibility. A deferred invoice does not establish deferred recognition. Confirm current law/year before advising the next cycle | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |
| **Primary source** | Income Tax Department AY 2026-27 ITR-4 FAQs, especially questions one/two, ten, thirteen through sixteen | [Official source](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online) |

### 3.10 ES - Estimacion Directa Simplificada Limit

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Spanish simplified direct-estimation eligibility and benefit | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **Jurisdiction** | ES individual economic activities; aggregate all activities and incompatible methods/elections | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **Amount** | Prior-year aggregate net turnover not above EUR 600,000; annualise the preceding startup year where required | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **What happens if exceeded** | Assess normal direct estimation and actual transition records; the allowance is not a tax credit or a fixed tax saving | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **What happens if below** | If otherwise eligible/no renunciation, general allowance 5% of positive net result before these provisions/expenses, capped EUR 2,000; Ceuta rate 10% in 2026, and incompatible reduction conditions apply | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **Measurement period** | Prior calendar year for turnover eligibility; current actual eligible positive result for the expense allowance | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **Action if approaching** | Prepare complete records and actual method transition. Compare actual marginal liability, not an assumed forty-five-percent rate or automatic EUR nine-hundred saving | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **Primary source** | AEAT simplified direct-estimation page, updated September 2026, eligibility and calculation including Ceuta exception | [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |

### 3.11 NL - Kleineondernemersregeling (KOR)

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Dutch KOR participation and crossing | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |
| **Jurisdiction** | NL established eligible participant; EU-KOR is a separate cross-border scheme | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |
| **Amount** | Calendar-year turnover not more than EUR 20,000 for ordinary KOR participation | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |
| **What happens if exceeded** | On exceeding the limit, notify immediately; the entire crossing supply is outside the KOR exemption, not just the excess | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |
| **What happens if below** | KOR requires participation, not automatic exemption for every small business. No ordinary charged VAT/input recovery under the scheme; cross-border facts can still require incidental returns | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |
| **Measurement period** | Calendar year. Voluntary exit can start at the first day of a return period with at least four weeks notice; no old three-year lock-in | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |
| **Action if approaching** | Compare actual input-VAT/pricing consequences, notify through the authority route, and check final termination date. Re-entry excluded for the remaining exit calendar year and the following year | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |
| **Primary source** | Belastingdienst KOR overview and current exit/re-entry page | [Official source](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) / [related source](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling) |

### 3.12 SG - GST Registration Threshold

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Singapore GST registration with separate effective dates | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| **Jurisdiction** | SG actual taxable supplies; reverse-charge/overseas-vendor regimes and exceptions separately assessed | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| **Amount** | More than SGD 1 million taxable turnover; include standard/zero-rated supplies, exclude relevant exempt/out-of-scope and capital-asset sales | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| **What happens if exceeded** | Retrospective: apply first to thirtieth January next year, effective first March. Prospective liability arising from first July 2025: apply within thirty days of supported forecast, effective two months from forecast | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| **What happens if below** | Ordinary test may not require compulsory registration, but other regimes can; voluntary registration and any commitment require their own conditions | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| **Measurement period** | Retrospective calendar year, not past four rolling quarters. Prospective next twelve months with objective evidence, not merely a business sales target | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| **Action if approaching** | Prepare pricing and accounting without assuming most sole traders are below the threshold. Verify supported registration exception, effective date, actual rates/returns/credits and any voluntary commitment | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| **Primary source** | IRAS compulsory registration, taxable-turnover definition, dated prospective change, examples and exceptions | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |

### 3.13 MT - Article 11 VAT Exemption Threshold

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Malta Article 11 domestic small-enterprise scheme | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **Jurisdiction** | MT established taxable person; related-person aggregation for non-physical persons and Article 12 obligations remain relevant | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **Amount** | Domestic calendar-year turnover EUR 35,000 exclusive of VAT under Sixth Schedule definitions; no separate rental-income add-on | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **What happens if exceeded** | Qualification ceases on exceeding the domestic threshold. Article 11(5)(b) requires cancellation application within fifteen days; (7) provides following-month cancellation on that application, while (8) permits Commissioner cancellation from the actual loss date. Determine Article 10 liability/date from the law, not a generic crossing-day promise | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **What happens if below** | Actual Article 11 exemption/annual declaration requirements apply, not automatic ordinary registration relief for every small activity. Some transactions still require Article 12 registration | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **Measurement period** | Preceding calendar year for application; current calendar year for continued qualification, with statutory turnover inclusions/exclusions. Not rolling twelve months | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **Action if approaching** | Reconcile turnover and eligibility, related parties, input-credit/pricing effect and actual registration dates before crossing. Apply actual Article 10/12 rules rather than inferring all supplies bear one standard rate | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **Primary source** | VAT Act Cap. 406 Article 11 and Sixth Schedule definitions/Part One, current downloaded consolidated law | [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |

### 3.14 CA - Small Supplier Threshold (GST/HST)

| Field | Value | Source |
| --- | --- | --- |
| **Threshold name** | Canadian GST/HST ordinary small-supplier timing | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| **Jurisdiction** | CA ordinary business; worldwide taxable supplies of all businesses and relevant associates, not only Canadian receipts | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| **Amount** | CAD 30,000 over four consecutive calendar quarters or within one quarter; include zero-rated taxable supplies, exclude financial services, capital-property sales and business-sale goodwill | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| **What happens if exceeded** | Single-quarter excess: charge the entire crossing supply; effective registration no later than that day. Multi-quarter-only excess: small-supplier status ends at the end of the following month; effective no later than first supply after that. Apply within twenty-nine days of effective date | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| **What happens if below** | Ordinary small supplier may register voluntarily, subject to actual taxable-supply eligibility. Charity/public-body and taxi/ride-sharing/special regimes need their own tests | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| **Measurement period** | Calendar quarters; distinguish within-quarter crossing from aggregate crossing and the following-month grace period | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| **Action if approaching** | Prepare pricing, actual tax/place/rate and credit eligibility; do not make multi-quarter registration effective automatically on the next quarter's first day | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| **Primary source** | CRA registration page, most-business table/examples and worldwide-associated-supply footnotes | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |

## Section 4 - Materiality and filtering

### Materiality threshold

**Materiality threshold floors**

| Currency | Floor |
| --- | --- |
| EUR | 100 |
| USD | 100 |
| GBP | 100 |
| AUD | 150 |
| CAD | 150 |
| INR | 10,000 |
| SGD | 150 |

### Materiality threshold

- **Rank optional planning suggestions only:** these currency floors are an internal presentation policy, not law or statutory thresholds. They may group minor optional planning items in reviewer notes when an evidenced impact estimate is available. Never suppress a registration, filing, payment, lost-exemption, deadline or missing-evidence warning because its immediate tax estimate is low, unknown or zero. Do not aggregate across currencies without a supported conversion. Keep grouped items discoverable, and surface them on request.

### Filtering logic

- **Filtering logic:** run jurisdictions established by actual residence, supply, employment or business facts. Missing revenue produces an incomplete check, not evidence of no liability. Existing registration can make a new-registration task redundant, but still assess effective date, continuing exemption, exit/re-entry, associated turnover and any distinct regime; record the precise reason for not repeating a task. Corporate/employer full computations remain outside this method, with a referral where their facts affect a supported threshold.

## Section 5 - Output format

### Part A - Threshold proximity dashboard

**Threshold proximity dashboard example:** amounts and direction are assumed case facts, not a live client report; GREEN only describes headroom under the chosen test. The statutory thresholds are sourced in Section 3.

| # | Jurisdiction | Threshold | Your figure | Limit | Distance | % to limit | Direction | Flag | Source for limit, all other figures are assumed/computed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | UK | VAT registration | GBP 82,000 | GBP 90,000 | GBP 8,000 | 8.9% | Approaching (+15% YoY) | RED | Computed example, [limit](https://www.gov.uk/register-for-vat) |
| 2 | UK | PA taper | GBP 94,000 | GBP 100,000 | GBP 6,000 | 6.0% | Approaching | RED | Computed example, [limit](https://www.gov.uk/income-tax-rates/income-over-100000) |
| 3 | US | 2026 QBI other-return threshold | USD 145,000 | USD 201,750 | USD 56,750 | 28.1% | Stable, if evidenced | GREEN | Computed example, [limit](https://www.irs.gov/irb/2025-45_IRB) |

### Part B - Action items (AMBER/RED, activated obligations and unresolved required tests)

For each flagged threshold:

```
### [Threshold name] - [Jurisdiction] - [FLAG]

**Current position:** [Your figure] of [Limit] ([percentage]%)
**Direction:** [Approaching / Stable / Moving away] - [basis for assessment]
**What changes:** [Plain-language explanation of what happens if exceeded]
**Recommended action:** [Specific steps for the reviewer to consider]
**Timing:** [Crossing/forecast date, application deadline, effective date and first affected transaction, with source]
**Tax impact:** [Supported conditional estimate with assumptions, or not yet computable; do not hide a legal action]
```

### Part C - Reviewer notes

- Data gaps that prevented checks
- Optional planning suggestions grouped under the internal presentation floors, with reason and amount; no suppressed legal obligations
- Assumptions made (e.g., exchange rates, annualisation method)

## Section 6 - Self-checks

Before delivering output, verify:

- [ ] User's jurisdiction is confirmed, not assumed
- [ ] Threshold amounts match current legislation (check tax year)
- [ ] "Your figure" traces to user-provided data, not fabricated
- [ ] Distance and percentage calculations are arithmetically correct
- [ ] Direction of travel is based on actual data or clearly marked "unknown"
- [ ] Internal presentation floors have not suppressed any legal obligation, deadline or unresolved required check
- [ ] Existing registrations/elections assessed for actual scope, effective date, continuing obligations and exit/re-entry rather than blanket exclusion
- [ ] Action recommendations are addressed to the reviewer, not the taxpayer
- [ ] All threshold amounts cite a primary source
- [ ] Output uses the format from Section 5

## Worked cases

### UK VAT past-turnover test versus allowance taper

Assume an ordinary established UK trader with no special registration trigger or approved exception has supported rolling taxable turnover GBP 82,000. Headroom is GBP 8,000, or 8.8889%, so this internal dashboard marks RED proximity; it is not evidence of registration already due. Equality at GBP 90,000 does not exceed this ordinary test. A separately established crossing in July requires application by thirty August and ordinary effective registration first September, not the crossing day. For a different taxpayer otherwise entitled to the standard allowance, adjusted net income GBP 110,000 reduces GBP 12,570 by GBP 5,000, leaving GBP 7,570; this does not itself compute marginal tax. [VAT registration](https://www.gov.uk/register-for-vat), [Personal Allowance](https://www.gov.uk/income-tax-rates/income-over-100000).

```oa-check
name: Threshold headroom and adjusted net income taper are different tests
inputs:
  taxable_turnover: 82000
  vat_limit: 90000
  adjusted_net_income: 110000
  taper_start: 100000
  standard_allowance: 12570
steps:
  - headroom: vat_limit - taxable_turnover
  - headroom_percentage: headroom / vat_limit * 100
  - allowance_reduction: min(standard_allowance, max(adjusted_net_income - taper_start, 0) / 2)
  - remaining_allowance: standard_allowance - allowance_reduction
expected:
  headroom: 8000
  headroom_percentage: 8.88888888888889
  allowance_reduction: 5000
  remaining_allowance: 7570
```

### Dutch KOR crossing transaction is not taxed only on its excess

Assume an eligible KOR participant with calendar-year qualifying turnover EUR 19,750 receives a fully qualifying EUR 500 advance. Turnover becomes EUR 20,250 and exceeds the EUR 20,000 boundary by EUR 250. The whole EUR 500 crossing transaction loses KOR exemption, not merely EUR 250. The applicable VAT rate, tax-inclusive/exclusive contract and actual VAT amount require the country computation. Immediate notification is not suppressed because a possible tax estimate is below an internal currency floor. This follows the authority's described example; it is not a registration actually submitted. [Belastingdienst exit example](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor).

```oa-check
name: KOR crossing tests turnover but affects the whole crossing supply
inputs:
  preceding_turnover: 19750
  crossing_advance: 500
  kor_limit: 20000
steps:
  - turnover_after: preceding_turnover + crossing_advance
  - excess: max(turnover_after - kor_limit, 0)
  - crossing_supply_outside_kor: crossing_advance
  - understatement_if_only_excess_used: crossing_supply_outside_kor - excess
expected:
  turnover_after: 20250
  excess: 250
  crossing_supply_outside_kor: 500
  understatement_if_only_excess_used: 250
```

## When to refuse or refer

Do not certify a completed legal test when the measurement period, entity/associated turnover, registration status, required data, operative law or source conflicts remain unresolved. Continue the evidenced proximity calculation and list the exact missing facts; refer the affected country determination rather than invent a threshold, effective date, insurance price or tax rate. Do not execute registrations or change invoicing/recognition merely on a planning recommendation.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| Read for OSS optional schemes and complete place-of-supply threshold conditions | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en | 2026-11-14 |
| Read for Rev. Proc. 2025-32 section .26, all three 2026 filing-status amounts | https://www.irs.gov/irb/2025-45_IRB | 2026-11-14 |
| Read for QBI eligibility, components, income limit and post-2025 minimum-deduction context; not all linked instructions | https://www.irs.gov/newsroom/qualified-business-income-deduction | 2026-11-14 |
| Read for OASDI/Medicare distinction and base-history rows 2025 to 2027; only 2026 adopted | https://www.ssa.gov/oact/cola/cbb.html | 2026-11-14 |
| Read for SE rate, 2026 combined base and Additional Medicare filing-status table; raw profit is not established net earnings | https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes | 2026-11-14 |
| Read for Registration triggers, taxable-turnover inclusions, both timing tests and special situations | https://www.gov.uk/register-for-vat | 2026-11-14 |
| Read for Current 2026-27 allowance, adjusted-net-income taper and Scottish-rate distinction | https://www.gov.uk/income-tax-rates/income-over-100000 | 2026-11-14 |
| Read for UStG section 19 complete paragraphs one to six; not the whole administrative implementation | https://www.gesetze-im-internet.de/ustg_1980/__19.html | 2026-11-14 |
| Read for Australian government Taxsuperandyou education page compulsory/voluntary registration and application timing | https://smallbusiness.taxsuperandyou.gov.au/goods-and-services-tax/do-i-need-to-register | 2026-11-14 |
| Read for Compilation 96 dated January 2026, volume two: sections 188-10, 188-15, 188-20 and 188-25 turnover definitions/exclusions; not the whole Act | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html | 2026-11-14 |
| Read for Both 2025-26 and 2026-27 tables plus rates, dependent adjustment, acceptable cover and partial-year coverage sections | https://privatehealth.gov.au/health_insurance/surcharges_incentives/medicare_levy.htm | 2026-11-14 |
| Read for AY 2026-27 ITR-4 FAQs one/two, nine/ten and thirteen through sixteen; latest 2025-2026 filing cycle only | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/file-itr-4-sugam-online | 2026-11-14 |
| Read for Current September 2026 eligibility and calculation sections, including Ceuta 2026 exception and incompatible reduction | https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html | 2026-11-14 |
| Read for KOR eligibility/effects and incidental cross-border filing/EU-KOR distinction | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling | 2026-11-14 |
| Read for Full operative exit, crossing-supply example, voluntary notice and re-entry sections | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor | 2026-11-14 |
| Read for Compulsory tests, turnover definition, retrospective timing, dated prospective change/examples and exceptions; July 2025 change supersedes the legacy thirty-first-day opening sentence | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst | 2026-11-14 |
| Read for Downloaded consolidated Cap. 406 Article 11 and Sixth Schedule definitions and Part One, pages eleven to thirteen and ninety-eight to one-hundred-one; not all VAT law | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-14 |
| Read for Most-business registration table/examples and associated worldwide-taxable-supply footnotes; charity/public-body headings identify separate tests | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html | 2026-11-14 |

Not yet confirmed: full successor Indian FY 2026-27 law and section numbering, current audit conditions/deadlines and every ITR-4 exclusion; German startup/current-crossing-supply administrative implementation and actual filing periods; full EU SME exemption interaction and country place/rate/registration details; every country's voluntary-registration commitment, input-credit adjustment and exceptional registration treatment; current applicable GST/VAT rates and actual filing periods where not established above; complete Schedule SE earnings computation and QBI minimum-deduction/other limitation calculation; actual pension/Gift Aid eligibility/limits and adjusted-net-income calculation; Australian family/part-year MLS tax-base computation and actual cover quote; Maltese Article 10 liability dates in every Article 11 cancellation scenario and Article 12 transaction-specific thresholds; full Canadian special-regime/charity/public-body rules. These topics remain required checks, not confirmed numbers or permission to use the former generic shortcuts.
