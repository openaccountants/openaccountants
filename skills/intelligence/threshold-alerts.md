---
name: threshold-alerts
description: >
  Intelligence skill that detects when the user is near important tax thresholds. Covers 14 threshold checks across 10 jurisdictions (EU, US, UK, DE, AU, IN, ES, NL, SG, MT, CA). For each threshold: calculates proximity, determines direction of travel, and recommends specific action. Flags the crossing point where obligations change materially.
version: 0.1
category: intelligence
depends_on:
  - workflow-base
triggers:
  - threshold alert
  - am I near the VAT threshold
  - do I need to register for VAT
  - income threshold
  - tax cliff
  - am I close to
  - threshold check
---

# Threshold Alerts v0.1

## What this file is

**Obligation category:** INTEL (Intelligence / Cross-cutting)
**Functional role:** Threshold proximity detection, cliff warnings, proactive alerts
**Status:** Active

This is an intelligence skill that loads on top of `workflow-base`. It monitors the user's financial data against statutory thresholds where obligations change materially -- registration requirements activate, deductions phase out, tax rates jump, or filing complexity increases.

**The reviewer is the customer of this output.** Threshold alerts are addressed to the credentialed reviewer, who decides whether action is needed.

> **Disclaimer.** Threshold amounts are based on publicly available statutory rules and may change with legislation. Currency conversions, timing of income recognition, and specific definitions of "turnover" or "income" vary by jurisdiction and may affect whether a threshold applies. All threshold assessments must be verified by a credentialed professional in the relevant jurisdiction. This is not legal or tax advice.

---

## Section 1 -- Scope statement

This skill covers:

- **Jurisdictions:** EU (cross-border), US, UK, DE, AU, IN, ES, NL, SG, MT, CA
- **Threshold types:** VAT/GST registration, income tax cliffs, deduction phase-outs, social security caps, simplified regime limits
- **Output:** Proximity report with distance, direction, and recommended action

This skill does NOT cover:

- Corporate tax thresholds or employer-side thresholds
- Thresholds that require entity-level (partnership, corporation) analysis
- Real-time monitoring (this runs on demand or when triggered by a computation skill)
- Thresholds below a materiality floor (see Section 4)

---

## Section 2 -- Workflow

### Step 0 -- Gather inputs

From the user's data (intake, computation output, or explicit statement), extract:

1. **Jurisdiction(s)** -- where the user files
2. **Gross revenue / turnover** -- rolling 12-month and year-to-date
3. **Net income / adjusted gross income** -- current period
4. **Specific data points** -- as required by individual thresholds (e.g., cross-border B2C sales, private health insurance status)

If a required data point is missing, flag the threshold check as "incomplete -- data needed" and state what is required.

### Step 1 -- Run threshold checks

For each applicable threshold (matched to user's jurisdiction), compute:

1. **Current value** -- the user's figure that is compared against the threshold
2. **Threshold amount** -- the statutory limit
3. **Distance** -- absolute difference (threshold minus current value)
4. **Distance as percentage** -- (distance / threshold) x 100
5. **Direction of travel** -- is the user approaching or moving away from the threshold? Based on:
   - Year-over-year trend (if prior-year data available)
   - YTD annualised projection (current YTD / months elapsed x 12)
   - If no trend data, state "direction unknown"

### Step 2 -- Classify proximity

| Proximity band | Condition | Flag |
|---|---|---|
| Safe | > 20% below threshold | GREEN |
| Watch | 10--20% below threshold | AMBER |
| Danger zone | < 10% below threshold | RED |
| Exceeded | At or above threshold | RED -- EXCEEDED |
| Not applicable | Threshold does not apply to this user | GREY |

### Step 3 -- Generate action recommendations

For each threshold in AMBER or RED, produce:

1. **What is happening** -- one-sentence plain-language explanation
2. **What changes if exceeded** -- concrete obligation that activates or benefit that is lost
3. **Recommended action** -- what the reviewer should consider
4. **Timing** -- when action must be taken (e.g., "register within 30 days of exceeding")

### Step 4 -- Produce output

Format per Section 5.

---

## Section 3 -- Master Threshold Table

### 3.1 EU -- VAT One Stop Shop (OSS)

| Field | Value |
|---|---|
| **Jurisdiction** | EU (all member states) |
| **Threshold name** | VAT OSS / distance-selling threshold |
| **Amount** | EUR 10,000 in B2C cross-border sales to other EU member states (aggregate, all states combined) |
| **What happens if exceeded** | Must register for OSS in home country OR register for VAT in each destination country. Must charge destination-country VAT rates instead of home-country rate. |
| **What happens if below** | May charge home-country VAT rate on all B2C cross-border sales. No OSS obligation. |
| **Measurement period** | Current calendar year OR prior calendar year (if exceeded in prior year, obligation continues) |
| **Action if approaching** | Prepare OSS registration in home country. Review pricing to absorb rate differences. Implement VAT rate lookup by customer country. |
| **Primary source** | Council Directive 2006/112/EC, Art. 59c (as amended by Directive 2017/2455) |

### 3.2 US -- QBI Deduction Phase-out

| Field | Value |
|---|---|
| **Jurisdiction** | US (federal) |
| **Threshold name** | Qualified Business Income deduction income cliff |
| **Amount** | $197,300 (single) / $394,600 (MFJ) taxable income before QBI deduction (2025, indexed) |
| **What happens if exceeded** | For specified service trades or businesses (SSTBs): QBI deduction phases out over next $50,000 (single) / $100,000 (MFJ) and reaches zero. Can cost thousands in additional tax. |
| **What happens if below** | Full 20% QBI deduction on qualified business income, regardless of business type. |
| **Measurement period** | Tax year |
| **Action if approaching** | Maximise above-the-line deductions (retirement contributions, HSA, SE health insurance) to stay below. Consider timing of income/deductions. Review whether business is an SSTB. |
| **Primary source** | IRC section 199A(d)(3); Rev. Proc. 2024-40 (inflation adjustment) |

### 3.3 US -- Social Security Tax Cap (OASDI)

| Field | Value |
|---|---|
| **Jurisdiction** | US (federal) |
| **Threshold name** | OASDI wage base / SE tax cap |
| **Amount** | $176,100 (2025) |
| **What happens if exceeded** | Stop paying the 12.4% OASDI portion of SE tax on earnings above the cap. Only 2.9% Medicare tax (+ 0.9% Additional Medicare Tax above $200K/$250K) applies. Effective SE tax rate drops significantly. |
| **What happens if below** | Full 15.3% SE tax rate applies (12.4% OASDI + 2.9% Medicare). |
| **Measurement period** | Tax year (calendar year for SE tax) |
| **Action if approaching** | This is informational -- no action required. Useful for cash flow planning: SE tax burden decreases once cap is reached. |
| **Primary source** | IRC section 1401; SSA wage base announcement |

### 3.4 UK -- VAT Registration Threshold

| Field | Value |
|---|---|
| **Jurisdiction** | GB |
| **Threshold name** | Compulsory VAT registration |
| **Amount** | GBP 90,000 taxable turnover (from 1 April 2024) |
| **What happens if exceeded** | Must register for VAT within 30 days. Must charge VAT on taxable supplies. Must file VAT returns (quarterly under MTD). Can recover input VAT. |
| **What happens if below** | No obligation to register. May register voluntarily. Cannot charge VAT (unless voluntarily registered). |
| **Measurement period** | Rolling 12 months (backward-looking) OR expected turnover in next 30 days alone |
| **Action if approaching** | Consider voluntary registration if significant input VAT to recover. Review pricing strategy. Prepare MTD-compatible software. Registration effective from date threshold exceeded, not date of application. |
| **Primary source** | VAT Act 1994, Schedule 1, para. 1; SI 2024/309 |

### 3.5 UK -- Personal Allowance Taper

| Field | Value |
|---|---|
| **Jurisdiction** | GB |
| **Threshold name** | Personal allowance income taper |
| **Amount** | GBP 100,000 adjusted net income |
| **What happens if exceeded** | Lose GBP 1 of personal allowance for every GBP 2 of income above GBP 100,000. PA fully lost at GBP 125,140. Creates an effective 60% marginal tax rate in the GBP 100,000--125,140 band. |
| **What happens if below** | Full GBP 12,570 personal allowance. |
| **Measurement period** | Tax year (6 Apr -- 5 Apr) |
| **Action if approaching** | Maximise pension contributions (relief at source reduces adjusted net income). Consider charitable donations under Gift Aid. Timing of income recognition. |
| **Primary source** | ITA 2007, s. 35; Income Tax (Earnings and Pensions) Act 2003 |

### 3.6 DE -- Kleinunternehmer (Small Business VAT Exemption)

| Field | Value |
|---|---|
| **Jurisdiction** | DE |
| **Threshold name** | Kleinunternehmerregelung (small entrepreneur scheme) |
| **Amount** | EUR 25,000 gross revenue in current calendar year (revised from EUR 22,000 effective 2025 under JStG 2024) |
| **What happens if exceeded** | Must charge VAT (Umsatzsteuer) on all supplies from the following year. Must file UStVA monthly or quarterly. Can recover input VAT. |
| **What happens if below** | No obligation to charge VAT. Cannot recover input VAT. Invoices must state Kleinunternehmer exemption. |
| **Measurement period** | Current calendar year gross revenue. Also: prior-year threshold of EUR 25,000 gross and current-year expected revenue of EUR 100,000. |
| **Action if approaching** | Evaluate whether input VAT recovery would exceed the administrative burden. Consider voluntary opt-in (Regelbesteuerung) if significant B2B sales. 5-year binding period if opting in. |
| **Primary source** | UStG section 19(1); Jahressteuergesetz 2024 |

### 3.7 AU -- GST Registration Threshold

| Field | Value |
|---|---|
| **Jurisdiction** | AU |
| **Threshold name** | Compulsory GST registration |
| **Amount** | AUD 75,000 annual turnover (GST turnover) |
| **What happens if exceeded** | Must register for GST within 21 days. Must charge 10% GST on taxable supplies. Must lodge BAS. Can claim input tax credits. |
| **What happens if below** | No obligation to register. May register voluntarily. |
| **Measurement period** | Current month's turnover + prior 11 months, OR projected turnover for current month + next 11 months |
| **Action if approaching** | Consider voluntary registration for input tax credits. Review contracts -- GST-inclusive or exclusive pricing. Register before exceeding to avoid retrospective obligations. |
| **Primary source** | A New Tax System (Goods and Services Tax) Act 1999, s. 23-15 |

### 3.8 AU -- Medicare Levy Surcharge (MLS)

| Field | Value |
|---|---|
| **Jurisdiction** | AU |
| **Threshold name** | Medicare Levy Surcharge (no private health insurance) |
| **Amount** | AUD 97,000 income for MLS purposes (single, 2024-25) |
| **What happens if exceeded** | 1.0% surcharge on taxable income (Tier 1: $97,001--$113,000); 1.25% (Tier 2: $113,001--$151,000); 1.5% (Tier 3: $151,001+). Applies if no complying private hospital insurance. |
| **What happens if below** | No MLS regardless of private health insurance status. |
| **Measurement period** | Financial year (1 Jul -- 30 Jun) |
| **Action if approaching** | Compare cost of basic private hospital cover vs MLS. Hospital-only policies from ~AUD 1,200/year may be cheaper than the surcharge (1% of $97,000 = $970). Break-even analysis required. |
| **Primary source** | A New Tax System (Medicare Levy Surcharge--Fringe Benefits) Act 1999 |

### 3.9 IN -- Presumptive Taxation Threshold (44ADA)

| Field | Value |
|---|---|
| **Jurisdiction** | IN |
| **Threshold name** | Presumptive taxation for professionals (section 44ADA) |
| **Amount** | INR 75 lakh gross receipts (if >95% digital receipts); INR 50 lakh (otherwise) |
| **What happens if exceeded** | Must maintain full books of accounts. Must get tax audit under section 44AB. Filing deadline moves from Jul 31 to Oct 31. Actual profit taxed (no presumptive benefit). Significant compliance burden increase. |
| **What happens if below** | Can declare 50% of gross receipts as deemed profit. No books of accounts required. Simplified ITR-4 filing. No audit. |
| **Measurement period** | Financial year (1 Apr -- 31 Mar) |
| **Action if approaching** | Track gross receipts monthly. If close, consider deferring invoicing to next FY (if commercially acceptable). Ensure >95% digital receipts to use the higher INR 75L threshold. |
| **Primary source** | Income Tax Act 1961, s. 44ADA; Finance Act 2023 (raised threshold) |

### 3.10 ES -- Estimacion Directa Simplificada Limit

| Field | Value |
|---|---|
| **Jurisdiction** | ES |
| **Threshold name** | Simplified direct estimation method (estimacion directa simplificada) |
| **Amount** | EUR 600,000 net revenue in prior year |
| **What happens if exceeded** | Must use estimacion directa normal (full accounting method). Lose the 5% general deduction (dificulmente justificables) capped at EUR 2,000. Full bookkeeping requirements. |
| **What happens if below** | Can use simplified method: 5% flat deduction for hard-to-justify expenses (max EUR 2,000/year). Simplified record-keeping. |
| **Measurement period** | Prior calendar year net revenue |
| **Action if approaching** | Prepare for full bookkeeping. The actual difference may be modest (max EUR 2,000 deduction lost = max ~EUR 900 tax at 45% marginal rate). Focus on ensuring full records are maintained. |
| **Primary source** | LIRPF art. 28, 30; RIRPF art. 28--30 |

### 3.11 NL -- Kleineondernemersregeling (KOR)

| Field | Value |
|---|---|
| **Jurisdiction** | NL |
| **Threshold name** | Small entrepreneurs scheme (KOR) |
| **Amount** | EUR 20,000 annual turnover |
| **What happens if exceeded** | Must deregister from KOR. Must charge BTW on all taxable supplies. Must file quarterly BTW returns. Can recover input BTW (voorbelasting). |
| **What happens if below** | VAT exempt under KOR. No BTW on invoices. No BTW returns. Cannot recover input BTW. 3-year minimum registration period. |
| **Measurement period** | Calendar year |
| **Action if approaching** | Evaluate input BTW recovery vs. pricing advantage of no BTW. KOR exit is automatic -- must notify Belastingdienst. New KOR registration has 3-year lock-in. |
| **Primary source** | Wet op de omzetbelasting 1968, art. 25 (as amended 1 Jan 2020) |

### 3.12 SG -- GST Registration Threshold

| Field | Value |
|---|---|
| **Jurisdiction** | SG |
| **Threshold name** | Compulsory GST registration |
| **Amount** | SGD 1,000,000 annual taxable turnover |
| **What happens if exceeded** | Must register for GST within 30 days. Must charge 9% GST (from 1 Jan 2024). Must file quarterly GST returns (GST F5). Can claim input tax. |
| **What happens if below** | No obligation to register. May register voluntarily (2-year commitment). |
| **Measurement period** | Retrospective: past 4 quarters exceed SGD 1M. Prospective: reasonable expectation next 12 months will exceed SGD 1M. |
| **Action if approaching** | High threshold -- most sole proprietors will not reach it. If approaching, prepare pricing strategy and accounting systems for GST. Voluntary registration possible if significant zero-rated exports. |
| **Primary source** | Goods and Services Tax Act 1993, s. 8, Third Schedule |

### 3.13 MT -- Article 11 VAT Exemption Threshold

| Field | Value |
|---|---|
| **Jurisdiction** | MT |
| **Threshold name** | Article 11 VAT exemption (small undertaking) |
| **Amount** | EUR 35,000 annual turnover from economic activity (+ EUR 14,000 rental income if applicable) |
| **What happens if exceeded** | Must register under Article 10 (standard VAT). Must charge 18% VAT on taxable supplies. Must file VAT3 returns. Can recover input VAT. |
| **What happens if below** | Exempt from charging VAT under Article 11. No VAT returns required. Cannot recover input VAT. Annual declaration only. |
| **Measurement period** | Rolling 12 months, or expected turnover in next 12 months |
| **Action if approaching** | Compare input VAT recovery benefit vs. pricing simplicity. Article 10 registration is advantageous if selling primarily B2B (customers recover VAT). Consider timing of invoicing. |
| **Primary source** | VAT Act (Cap. 406), Article 11; Legal Notice 272/2024 |

### 3.14 CA -- Small Supplier Threshold (GST/HST)

| Field | Value |
|---|---|
| **Jurisdiction** | CA |
| **Threshold name** | Small supplier exemption from GST/HST |
| **Amount** | CAD 30,000 in total taxable supplies over the last 4 consecutive calendar quarters or in a single calendar quarter |
| **What happens if exceeded** | Must register for GST/HST. Must charge 5% GST (or applicable HST rate). Must file GST/HST returns. Can claim input tax credits (ITCs). |
| **What happens if below** | No obligation to register. May register voluntarily. |
| **Measurement period** | 4 consecutive calendar quarters (backward) or single calendar quarter |
| **Action if approaching** | Consider voluntary registration for ITC recovery. Review pricing. Registration effective date is the day the CAD 30,000 is exceeded in a single quarter, or the first day of the next quarter if exceeded over 4 quarters. |
| **Primary source** | Excise Tax Act, s. 148(1); CRA IT-400 |

---

## Section 4 -- Materiality and filtering

### Materiality threshold

Do not surface a threshold alert if the potential tax impact of crossing the threshold is below the following materiality floors:

| Currency | Floor |
|---|---|
| EUR | 100 |
| USD | 100 |
| GBP | 100 |
| AUD | 150 |
| CAD | 150 |
| INR | 10,000 |
| SGD | 150 |

If the annualised impact of crossing a threshold is below the materiality floor, suppress the alert unless the user explicitly asks about it.

### Filtering logic

1. Only run checks for jurisdictions the user operates in.
2. If the user has no revenue data, skip revenue-based thresholds and note "insufficient data."
3. If the user is already registered (e.g., already VAT registered), skip the registration threshold and note "already registered -- threshold not applicable."

---

## Section 5 -- Output format

### Part A -- Threshold proximity dashboard

```
| # | Jurisdiction | Threshold | Your figure | Limit | Distance | % to limit | Direction | Flag |
|---|---|---|---|---|---|---|---|---|
| 1 | UK | VAT registration | GBP 82,000 | GBP 90,000 | GBP 8,000 | 8.9% | Approaching (+15% YoY) | RED |
| 2 | UK | PA taper | GBP 94,000 | GBP 100,000 | GBP 6,000 | 6.0% | Approaching | RED |
| 3 | US | QBI cliff | $145,000 | $197,300 | $52,300 | 26.5% | Stable | GREEN |
```

### Part B -- Action items (AMBER and RED only)

For each flagged threshold:

```
### [Threshold name] -- [Jurisdiction] -- [FLAG]

**Current position:** [Your figure] of [Limit] ([percentage]%)
**Direction:** [Approaching / Stable / Moving away] -- [basis for assessment]
**What changes:** [Plain-language explanation of what happens if exceeded]
**Recommended action:** [Specific steps for the reviewer to consider]
**Timing:** [When action must be taken]
**Tax impact:** [Estimated annual cost/saving of crossing the threshold]
```

### Part C -- Reviewer notes

- Data gaps that prevented checks
- Thresholds suppressed due to materiality
- Assumptions made (e.g., exchange rates, annualisation method)

---

## Section 6 -- Self-checks

Before delivering output, verify:

- [ ] User's jurisdiction is confirmed, not assumed
- [ ] Threshold amounts match current legislation (check tax year)
- [ ] "Your figure" traces to user-provided data, not fabricated
- [ ] Distance and percentage calculations are arithmetically correct
- [ ] Direction of travel is based on actual data or clearly marked "unknown"
- [ ] Materiality filter applied -- sub-threshold alerts suppressed
- [ ] Already-registered thresholds excluded
- [ ] Action recommendations are addressed to the reviewer, not the taxpayer
- [ ] All threshold amounts cite a primary source
- [ ] Output uses the format from Section 5
