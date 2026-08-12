---
name: ca-fed-t1135
description: Use this skill whenever asked about Canada Form T1135, Foreign Income Verification Statement, specified foreign property, foreign asset reporting, the $100,000 cost amount threshold, the $250,000 simplified-versus-detailed reporting boundary, or how to classify foreign accounts, foreign securities, foreign real estate, foreign trusts, and other foreign property for a Canadian resident taxpayer. Trigger on phrases like "T1135", "foreign income verification statement", "specified foreign property", "foreign assets over 100000", "do I need to file T1135", "foreign bank account reporting Canada", "US brokerage T1135", "foreign rental property T1135", "simplified T1135", "Part A Part B T1135", or any question about whether a Canadian resident individual, corporation, trust, or partnership must disclose foreign property. ALWAYS read this skill before touching any Canada T1135-related work.
version: 2.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Edgar Lautsyus
review_status: current
depends_on: - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CA Fed T1135

## Verified rates & thresholds (accountant-reviewed)

- **Reviewer note** — Reviewed against the cited tax authorities by Nathan Wiebe on 2026-06-21. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.

### T1135 (Foreign Property)

- **Filing threshold** — Total cost > $100,000 CAD at any time  _(ITA s.233.3; CRA — T1135 guide — canada.ca)_
- **Basis** — Cost amount, NOT fair market value  _(ITA s.233.3(1) definition of 'cost amount'; CRA — Questions and answers about T1135)_
- **Simplified (Part A)** — $100,000–$249,999 throughout the entire year  _(ITA s.233.3; CRA Form T1135 instructions)_
- **Detailed (Part B)** — $250,000+ at any time  _(ITA s.233.3; CRA Form T1135 instructions)_
- **Cat 1** — Funds held outside Canada  _(CRA Form T1135)_
- **Cat 2** — Shares of non-resident corporations  _(CRA Form T1135)_
- **Cat 3** — Indebtedness owed by non-residents  _(CRA Form T1135)_
- **Cat 4** — Interests in non-resident trusts  _(CRA Form T1135)_
- **Cat 5** — Real property outside Canada (not personal-use/active business)  _(CRA Form T1135)_
- **Cat 6** — Other property outside Canada  _(CRA Form T1135)_
- **Cat 7** — Property held with Canadian registered dealer/trust co  _(CRA Form T1135; CRA — T1135 reporting for 2015 and later years)_
- **Personal-use property** — Excluded  _(ITA s.233.3(1))_
- **Active business property** — Excluded  _(ITA s.233.3(1))_
- **Registered plans (RRSP/RRIF/TFSA/RESP/DPSP)** — Excluded  _(ITA s.233.3(1))_
- **First year of Canadian residence** — Excluded for that year  _(ITA s.233.7)_
- **Late filing — up to 100 days** — CORRECT PENALTY SCHEDULE: Late filing under ITA s.162(7) = $25/day, minimum $100, MAXIMUM $2,500 (100 days). The skill's 'up to 100 days' framing is correct but the next row is wrong. The $12,000 cap in Row 22 applies to a different penalty (s.162(10)(a) — knowing/grossly negligent failure). There is no separate '$100/day; max $12,000' penalty tier — that is a mischaracterisation.  _(ITA s.162(7) — max $2,500; ITA s.162(10)(a) — $500/month up to 24 months, max $12,000; CRA — Table of penalties (foreign reporting) — canada.ca)_
- **Knowing / grossly negligent failure to file** — $500 per MONTH, up to 24 months (max $12,000), less any s.162(7) penalty already applied. There is no "$100/day" penalty in the T1135 regime.  _(ITA s.162(10)(a); CRA — Table of penalties (foreign reporting))_
- **Knowingly non-filed > 24 months** — Additional 5% of the cost amount of the property (ITA s.162(10.1)). The separate false-statement penalty under s.163(2.4) is the greater of $24,000 and 5% of cost amount. Reassessment period is extended 3 years under s.152(4)(b.2).  _(ITA s.162(10.1); ITA s.163(2.4); ITA s.152(4)(b.2); CRA — Table of penalties)_

## Section 1 -- Quick reference

Read this whole section before classifying anything.

**Section 1 -- Quick reference**

| Field | Value |
| --- | --- |
| Country | Canada -- Federal |
| Jurisdiction Code | CA-FED |
| Tax | Foreign reporting -- specified foreign property |
| Currency | CAD, unless a valid functional currency election applies |
| Tax year | Calendar year for individuals; taxation year / fiscal period as applicable for other filers |
| Primary legislation | Income Tax Act (Canada), section 233.3 |
| Tax authority | Canada Revenue Agency (CRA) |
| Form | T1135 -- Foreign Income Verification Statement |
| Filing deadline | Same due date as the related income tax return or partnership information return |
| Contributor | Open Accountants Community |
| Validated by | Verified by Nathan Wiebe on 2026-06-21 |
| Validation date | Verified by Nathan Wiebe on 2026-06-21 |
| Skill version | 2.0 |
| Confidence coverage | Tier 1: threshold testing, Part A / Part B decision, category mapping, common exclusions, form-field capture. Tier 2 (Section 7 catalogue, T2-1 to T2-10): residency timing, beneficial ownership, foreign affiliate exposure, partnership/trust attribution, digital-asset situs, mixed-use real estate, pre-construction deposits, functional currency / amended returns, joint ownership, missed prior-year filings. Tier 3: foreign affiliate filings (T1134), formal voluntary disclosure execution. |

### Core thresholds (2025 form usage)

**Core thresholds (2025 form usage)**

| Item | Rule |
| --- | --- |
| Basic filing threshold | File T1135 if total cost amount of specified foreign property exceeded $100,000 CAD at any time in the year |
| Threshold basis | Cost amount, NOT fair market value |
| Simplified boundary | If total cost was more than $100,000 CAD but **less than $250,000 CAD throughout the entire year** (i.e., did not reach $250,000 CAD at any time), complete either Part A or Part B |
| Detailed boundary | If total cost reached $250,000 CAD or more at any time in the year, complete Part B |

### T1135 categories

**T1135 categories**

| Category | Description |
| --- | --- |
| 1 | Funds held outside Canada |
| 2 | Shares of non-resident corporations (other than foreign affiliates) |
| 3 | Indebtedness owed by non-residents |
| 4 | Interests in non-resident trusts |
| 5 | Real property outside Canada (other than personal-use property and real estate used in an active business) |
| 6 | Other property outside Canada |
| 7 | Property held in an account with a Canadian registered securities dealer or a Canadian trust company |

### Common exclusions

**Common exclusions**

| Item | Treatment |
| --- | --- |
| Personal-use property | Excluded |
| Property used or held exclusively in an active business | Excluded |
| Property inside registered plans (RRSP, RRIF, TFSA, RESP, DPSP) | Excluded |
| First year of Canadian tax residence for an individual (other than a trust) | Excluded under ITA s. 233.7 for that first resident year |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP -- residency required |
| Unknown cost basis | STOP -- do not use market value as final threshold test |
| Unknown first-year resident status | Ask one targeted question |
| Unknown account type | Do NOT assume registered-plan exclusion |
| Unknown property use | Do NOT assume personal-use or active-business exclusion |
| Unknown country code | Use provisional country and flag reviewer confirmation |
| Unknown ownership chain | Flag reviewer escalation |
| Unknown functional currency election | Assume CAD unless clearly documented otherwise |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Required inputs list** — Before reaching any conclusion, gather: 1. Taxpayer type -- individual, corporation, trust, or partnership 2. Canadian tax residency status for the year 3. First-year resident status if the filer is an individual 4. Taxation year / fiscal period from and to dates 5. Whether the filing is amended 6. Whether a functional currency election applies 7. Complete list of all foreign assets or accounts held at any time in the year 8. Cost amount in CAD for each reportable or potentially reportable property 9. Maximum cost amount during the year where available 10. Cost amount at year-end or fair market value at year-end where the form requires it 11. Gross income / income received and gain (loss) on disposition 12. Country code and institution / issuer / counterparty / property description 13. Whether any property was inside a registered plan 14. Whether any property was personal-use property or used exclusively in an active business 15. Whether any property was jointly owned, held through a nominee, trust, partnership, or Canadian registered securities dealer / Canadian trust company If cost amount is unavailable, STOP. Do not convert a market-value-only answer into a final filing conclusion.

### Refusal catalogue

- **R-CA-T1135-1** — Trigger: taxpayer was not resident in Canada for the relevant year. Message: "T1135 is a Canadian-resident foreign reporting regime. Non-resident treatment is outside this skill. Escalate to a Canadian cross-border tax practitioner."
- **R-CA-T1135-2** — Trigger: immigration / emigration timing is unclear. Message: "Residency timing changes the T1135 analysis. Do not guess. Escalate to a licensed Canadian CPA."
- **R-CA-T1135-3** — Trigger: legal ownership and reporting attribution are uncertain. Message: "Legal ownership and reporting attribution are unclear. Do not guess. Escalate to a Canadian CPA with international reporting experience."
- **R-CA-T1135-4** — Trigger: only market value is available. Message: "T1135 threshold testing uses cost amount, not market value. A final conclusion cannot be made without cost basis support."
- **R-CA-T1135-5** — Trigger: crypto, offshore wallet, exchange, or token arrangement with unclear situs or characterization. Message: "Digital asset reporting classification is fact-specific and outside routine scope. Escalate before concluding."
- **R-CA-T1135-6** — Trigger: possible foreign affiliate identified. Message: "Possible foreign affiliate reporting issue identified. Do not handle within routine T1135 workflow. Escalate."

## Section 3 -- Foreign property pattern library

This is the deterministic pre-classifier for T1135 assets. Each asset gets exactly one of three outcomes: **REPORTABLE**, **EXCLUDED**, or **REVIEWER FLAG**.

### 3.1 Commonly reportable property

**3.1 Commonly reportable property**

| Pattern | Treatment | Category |
| --- | --- | --- |
| Foreign bank account | REPORTABLE | 1 |
| Shares of non-resident corporations held directly | REPORTABLE | 2 |
| Shares of non-resident corporations held with foreign broker | REPORTABLE | 2 |
| Foreign bonds, notes, loans receivable, indebtedness | REPORTABLE | 3 |
| Interests in non-resident trusts / foreign mutual fund trusts | REPORTABLE | 4 |
| Foreign rental / investment real estate | REPORTABLE | 5 |
| Other foreign investment property | REPORTABLE | 6 |
| Property held in an account with a Canadian registered securities dealer or a Canadian trust company | REPORTABLE | 7 |

### 3.2 Commonly excluded property

**3.2 Commonly excluded property**

| Pattern | Treatment | Reason |
| --- | --- | --- |
| Foreign property inside RRSP / RRIF / TFSA / RESP / DPSP | EXCLUDED | Registered-plan exclusion |
| Foreign vacation property used as personal-use property | EXCLUDED | Personal-use property exclusion |
| Property used or held exclusively in an active business | EXCLUDED | Active-business exclusion |
| Canadian mutual fund trust / Canadian mutual fund corporation | EXCLUDED | Investor holds Canadian property, not underlying foreign property |

### 3.3 Always flag for reviewer

**3.3 Always flag for reviewer**

| Pattern | Treatment | Reason |
| --- | --- | --- |
| Mixed-use foreign real estate | REVIEWER FLAG | Personal-use exclusion depends on facts |
| Joint ownership with unclear contributions | REVIEWER FLAG | Threshold depends on beneficial ownership share |
| Bare trust / nominee / beneficial ownership mismatch | REVIEWER FLAG | Attribution issue |
| Partnership interest with foreign property underneath | REVIEWER FLAG | Partner-level vs entity-level analysis |
| Possible foreign affiliate | REVIEWER FLAG | Foreign affiliate rules may displace routine T1135 handling |
| Crypto / offshore wallet / exchange arrangement | REVIEWER FLAG | Situs / property characterization issue |
| Pre-construction foreign real estate deposits | REVIEWER FLAG | Determine whether reportable property exists yet |

## Section 4 -- Threshold and filing path rules

### 4.1 Residency screen

**4.1 Residency screen**

| Condition | Result |
| --- | --- |
| Non-resident for the relevant year | STOP -- fire R-CA-T1135-1 |
| Individual (other than a trust) in first year of Canadian tax residence | No T1135 filing obligation for that first resident year (ITA s. 233.7) |
| Canadian-resident individual, corporation, trust, or partnership | Continue to threshold test |

### 4.2 Threshold test (Tier 1)

Aggregate the **cost amount** of all reportable specified foreign property held at any time in the year.

**4.2 Threshold test (Tier 1)**

| Condition | Result |
| --- | --- |
| Total never exceeded $100,000 CAD | T1135 generally not required |
| Total exceeded $100,000 CAD at any time | T1135 generally required |
| Cost amount missing | STOP -- fire R-CA-T1135-4 |

- **Sold assets rule** — Do NOT ignore property sold before year-end. If the threshold was met during the year, those assets still matter.

### 4.3 Part A vs Part B

**4.3 Part A vs Part B**

| Condition | Filing path |
| --- | --- |
| Total cost was more than $100,000 CAD and remained less than $250,000 CAD throughout the entire year (did not reach $250,000 CAD at any time) | Part A or Part B |
| Total cost reached $250,000 CAD or more at any time during the year | Part B (mandatory) |

### 4.4 Part A -- Simplified reporting method

- **Part A requirements** — Part A requires: type-of-property boxes; top three country codes based on maximum cost amount during the year; gross income from all specified foreign property; gain (loss) from disposition of all specified foreign property. Even if Part A is used, still build the underlying asset inventory for reviewer support.

### 4.5 Part B -- Detailed reporting method

- **Part B requirements** — Part B requires category-by-category detail for each specified foreign property held at any time in the year, unless valid Category 7 aggregation is used. Always gather: country code; institution / issuer / trust / property description; maximum cost amount during the year or other category-specific maximum field; cost amount at year-end where the form calls for it; gross income or income received; gain (loss) on disposition.

## Section 5 -- Category classification rules

### 5.1 Category 1 -- Funds held outside Canada

- **Capture fields** — Capture: country code; name of bank / other entity holding the funds; maximum funds held during the year; funds held at year-end; income received.

### 5.2 Category 2 -- Shares of non-resident corporations

- **Capture fields** — Capture: country code; name of corporation; maximum cost amount during the year; cost amount at year-end; gross income; gain (loss) on disposition.

### 5.3 Category 3 -- Indebtedness owed by non-residents

- **Capture fields** — Capture: country code; description of indebtedness; maximum cost amount during the year; cost amount at year-end; gross income; gain (loss) on disposition.

### 5.4 Category 4 -- Interests in non-resident trusts

- **Capture fields** — Capture: name of trust; country code; maximum cost amount during the year; income received; capital received; gain (loss) on disposition.

### 5.5 Category 5 -- Real property outside Canada

- **Capture fields** — Capture: description of property; country code; maximum cost amount during the year; cost amount at year-end; gross income; gain (loss) on disposition.

### 5.6 Category 6 -- Other property outside Canada

- **Capture fields** — Capture: description of property; country code; maximum cost amount during the year; cost amount at year-end; gross income; gain (loss) on disposition.

### 5.7 Category 7 -- Property held with Canadian registered securities dealer or Canadian trust company

- **Capture fields, country-by-country** — Capture, country-by-country (one aggregated line per country code): dealer / trust company name; country code; maximum fair market value during the year (aggregate across all securities of that country); fair market value at year-end (aggregate across all securities of that country); gross income (aggregate across all securities of that country); gain (loss) on disposition (aggregate across all securities of that country).
- **Category 7 aggregation rule** — Category 7 is a special aggregation rule that permits country-by-country reporting in lieu of security-by-security detail when property is held with a Canadian registered securities dealer or Canadian trust company. Do not force Categories 2 to 6 line-by-line reporting if valid Category 7 aggregation is available and chosen. Aggregation is by country of the issuer of the underlying property, not by dealer.
- **Why Category 7 uses fair market value, not cost amount** — Categories 1 to 6 use cost amount for both the threshold test and the in-form reporting fields. Category 7 is the deliberate exception: CRA permits FMV reporting because Canadian registered securities dealers and Canadian trust companies already track daily FMV (T5008 / T3 / T5 reporting infrastructure), and reconstructing cost amount across high-volume trading would impose disproportionate compliance burden. The Category 7 FMV concession is reporting-side only. The threshold test under s. 233.3 still uses cost amount -- you cannot use FMV to decide whether the $100,000 CAD threshold is crossed, even if every reportable asset will ultimately land in Category 7.  _(CRA, "Form T1135 -- Reporting for 2015 and later tax years.")_

### 5.8 Country code rules

- **Country code rules** — Capture country code in form-ready format wherever the form requires it. For Part A, identify the top three countries based on maximum cost amount during the year. For shares of non-resident corporations, generally use the country of residence of the corporation. For interests in non-resident trusts, generally use the country of residence of the trust. If country coding is uncertain, flag reviewer confirmation.

### 5.9 Income and gain rules

- **Income and gain rules** — Use gross income where the form calls for gross income. Use gain (loss) as the form label, not taxable capital gain / allowable capital loss. Do NOT net unrelated gains and losses across assets unless the form presentation explicitly aggregates them.

## Section 6 -- Exclusions and special cases

### 6.1 Registered plans

- **Registered plans exclusion** — Foreign property inside RRSP, RRIF, TFSA, RESP, and DPSP is excluded from T1135. Do not include those assets in the threshold calculation.

### 6.2 Personal-use property

- **Personal-use property exclusion** — Personal-use property is excluded. Do NOT assume foreign real estate qualifies if it also has rental or investment use.

### 6.3 Active-business property

- **Active-business property exclusion** — Property used or held exclusively in an active business is excluded. Do NOT assume a day trader or active investor automatically qualifies.

### 6.4 Joint ownership

- **Joint ownership rule** — If foreign property is jointly owned, determine beneficial ownership and contribution proportions before reaching the threshold conclusion. Do not assume 50/50 without support.

### 6.5 Mixed-use foreign real estate

- **Mixed-use rule** — Vacation use plus rental activity is fact-sensitive. Ask for personal-use days, rental days, and business purpose. Flag for reviewer.

### 6.6 Late or missed filings

- **Late or missed filings guidance** — If prior-year T1135 filings were missed: flag possible penalties and extended reassessment exposure; build the asset inventory year by year; discuss voluntary disclosure only as a reviewer issue; do NOT promise relief.

#### 6.6.1 Late-filing and false-statement penalty schedule

**6.6.1 Late-filing and false-statement penalty schedule**  _(CRA, "Table of penalties -- Foreign reporting.")_

| Penalty | Statute | Amount |
| --- | --- | --- |
| Late filing of T1135 | ITA s. 162(7) | $25 per day, minimum $100, maximum $2,500 (100 days). Applied automatically; due-diligence defence available but narrow. |
| Knowing or grossly negligent failure to file | ITA s. 162(10)(a) | $500 per month, up to 24 months. Maximum $12,000, less penalties already levied under s. 162(7). |
| Failure to file after CRA demand (knowing or gross negligence) | ITA s. 162(10)(b) | $1,000 per month, up to 24 months. Maximum $24,000, less penalties already levied. |
| Continuing failure beyond 24 months | ITA s. 162(10.1) | 5% of the cost amount of the specified foreign property, less any penalty already levied under s. 162(7) and s. 162(10). |
| False statement or omission on T1135 | ITA s. 163(2.4) | Greater of $24,000 and 5% of the greatest cost amount of the specified foreign property to which the false statement or omission relates. CRA bears burden of proving knowledge or gross negligence. |
| Extended reassessment exposure | ITA s. 152(4)(b.2) | The normal reassessment period is extended by three years for unreported income from specified foreign property where T1135 was not filed, was filed late, or contained a misrepresentation. |

Penalty references: CRA, "Table of penalties -- Foreign reporting." Late filing under s. 162(7) applies even where no tax is owing.

#### 6.6.2 Voluntary Disclosures Program

- **VDP overview** — If prior-year T1135 filings were missed and the omission has not been the subject of CRA enforcement action, the Voluntary Disclosures Program (VDP) may provide penalty relief and protection from prosecution. Conditions are set out in CRA Information Circular IC00-1R6, Voluntary Disclosures Program (effective 1 March 2018). The five validity conditions are: voluntary, complete, involves application or potential application of a penalty, includes information that is at least one year past due, and includes payment of estimated tax owing.  _(CRA Information Circular IC00-1R6, Voluntary Disclosures Program (effective 1 March 2018))_
- **VDP outcome caution** — VDP outcomes are streamed (General Program vs Limited Program) at CRA's discretion. Do NOT promise a specific stream or relief outcome. Flag VDP eligibility for reviewer; do not file the application within routine workflow.

## Section 7 -- Tier 2 reviewer catalogue

Tier 1 (Section 4) handles deterministic threshold and category mapping. Tier 2 covers fact-sensitive issues that require a licensed Canadian CPA or cross-border practitioner to sign off before filing. Routine workflow MUST stop and escalate if any Tier 2 issue is present.

**Tier 2 reviewer catalogue**

| # | Tier 2 issue | Why it escalates |
| --- | --- | --- |
| T2-1 | Immigration / emigration timing | First-year resident exception and part-year residency change the filing obligation. |
| T2-2 | Beneficial ownership / nominee chain | Reporting attribution may differ from registered title. |
| T2-3 | Possible foreign affiliate | T1134 may apply; T1135 routine handling is displaced. |
| T2-4 | Partnership or trust attribution | Partner-level vs entity-level filing obligation depends on facts. |
| T2-5 | Digital asset situs / characterization | Crypto, exchange wallets, token arrangements -- situs and property classification fact-sensitive. |
| T2-6 | Mixed-use foreign real estate | Personal-use vs investment-use split needs documentary support. |
| T2-7 | Pre-construction foreign deposits | Whether reportable property exists yet depends on contract terms. |
| T2-8 | Functional currency election or amended return | Prior elections and amendments change cost amount and category mapping. |
| T2-9 | Joint ownership with unclear contributions | Beneficial-share allocation needed before threshold conclusion. |
| T2-10 | Missed prior-year T1135 filings | Penalty exposure under s. 162(7), s. 162(10), s. 163(2.4); VDP analysis required. |

When escalating, provide: taxpayer type; residency facts; threshold computation to date; asset inventory; missing facts; proposed category mapping; reason for escalation.

## Section 8 -- Form assembly protocol

Use this section only after classification is complete.

### 8.1 Header fields

- **Header fields to capture** — Capture exactly: amended return status; functional currency code, if any; filer type; identification number; reporting entity name; address; taxation year from date; taxation year to date.

### 8.2 Part A output block

- **Part A output fields** — Capture exactly: applicable type-of-property boxes; top three country codes; gross income from all specified foreign property; gain (loss) from disposition of all specified foreign property.

### 8.3 Part B output block

- **Part B output fields** — For each category used, capture the exact form fields listed in Section 5.

### 8.4 Working paper template

```text
CANADA T1135 -- WORKING PAPER (2025)

A. HEADER
  A1. Amended return?                                        YES / NO
  A2. Functional currency election?                          YES / NO
  A3. Functional currency code                               ___________
  A4. Filer type                                             ___________
  A5. Identification number                                  ___________
  A6. Taxation year from                                     ___________
  A7. Taxation year to                                       ___________

B. THRESHOLD SUMMARY
  B1. Aggregate cost amount of reportable specified foreign property   ___________
  B2. Exceeded $100,000 CAD at any time?                              YES / NO
  B3. Reached $250,000 CAD at any time?                               YES / NO
  B4. Filing path                                                     NONE / PART A / PART B

C. ASSET INVENTORY
| # | Asset description | Category | Country code | Max cost / FMV | Year-end cost / FMV | Income / capital received | Gain (loss) | Outcome | Notes |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | | | | | | | | REPORTABLE / EXCLUDED / REVIEWER FLAG | |

D. EXCLUSIONS APPLIED
| Asset | Exclusion reason | Support |
|---|---|---|

E. REVIEWER FLAGS
| Issue | Reason | Action |
|---|---|---|
```

### 8.5 Certification and preparer fields

Do not finalize the form package without all of the following. Capture in this template block:

```text
CANADA T1135 -- CERTIFICATION AND PREPARER BLOCK (2025)

F. CERTIFICATION
  F1. Certification statement reproduced verbatim from form        YES / NO
  F2. Signer name                                                  ___________
  F3. Position or title (if filer is a corporation, trust,         ___________
      or partnership)
  F4. Signature                                                    ___________
  F5. Date of signature                                            YYYY-MM-DD

G. PAID PREPARER (if applicable)
  G1. Paid preparer name                                           ___________
  G2. Paid preparer address                                        ___________
  G3. Postal code                                                  ___________
  G4. Telephone                                                    ___________
  G5. EFILE number (if applicable)                                 ___________
```

If the filer is an individual, F3 is omitted. If no paid preparer is involved, leave block G blank but record `N/A` against G1 to make the omission deliberate.

## Section 9 -- Test suite

Use these as minimum validation scenarios.

### Test 1 -- Below threshold

Input: Canadian-resident individual with foreign bank account cost amount $42,000 and U.S. shares cost amount $31,000. No other specified foreign property.

Expected result:
- Aggregate cost amount = $73,000
- T1135 not required

### Test 2 -- Over threshold, below detailed boundary

Input: Canadian-resident individual with foreign bank account cost amount $18,000 and U.S. shares cost amount $108,000, later sold before year-end.

Expected result:
- Threshold exceeded during year
- T1135 required
- Part A or Part B available if total stayed below $250,000 throughout the year

### Test 3 -- Detailed reporting required

Input: Canadian-resident corporation with foreign securities cost amount $310,000 at peak during the year.

Expected result:
- T1135 required
- Part B required

### Test 4 -- Registered-plan exclusion

Input: RRSP with U.S. ETF cost amount $150,000 and TFSA with foreign stock cost amount $35,000; no non-registered foreign property.

Expected result:
- Excluded property only
- T1135 not required

### Test 5 -- Mixed-use condo

Input: Foreign condo used personally for 6 weeks and rented for the rest of the year.

Expected result:
- Do not auto-exclude
- Reviewer flag required

### Test 6 -- Category 7

Input: Foreign securities held in an account with a Canadian registered securities dealer.

Expected result:
- T1135 may be reportable through Category 7 aggregation if the facts support that method
- Aggregation is country-by-country, not security-by-security

### Test 7 -- First-year Canadian resident

Input: Individual immigrated to Canada and became a Canadian tax resident on 14 March of the year. Held foreign bank account cost $180,000 CAD and foreign rental property cost $420,000 CAD throughout the entire year.

Expected result:
- ITA s. 233.7 first-year exception applies for an individual (other than a trust) who first became resident in Canada in the year
- T1135 NOT required for that first resident year
- Filing obligation begins for the FOLLOWING tax year
- Reviewer flag: confirm immigration date and that taxpayer is an individual; the s. 233.7 exception does NOT apply to corporations or trusts

### Test 8 -- Missed prior-year filings

Input: Canadian-resident individual with foreign brokerage holdings cost $310,000 CAD for the past four years. Never filed T1135. CRA has not contacted the taxpayer.

Expected result:
- T1135 required for each year cost amount exceeded $100,000 CAD
- Penalty exposure: s. 162(7) ($25/day, max $2,500 per year) at minimum; s. 162(10)(a) up to $12,000 per year (at $500/month, up to 24 months, less any s. 162(7) penalty already applied) if knowing or grossly negligent; s. 162(10.1) 5% of cost amount after 24 months; s. 163(2.4) greater of $24,000 or 5% if false statement / omission
- Extended reassessment exposure under s. 152(4)(b.2) (additional three years for unreported foreign income)
- Reviewer flag: assess Voluntary Disclosures Program eligibility under IC00-1R6 -- voluntary, complete, penalty applies, at least one year overdue, payment of estimated tax owing
- Do NOT promise General Program vs Limited Program outcome; CRA's discretion
- Do NOT file VDP application within routine workflow; escalate to Tier 2 (T2-10)

## Section 10 -- Onboarding fallback

- **Onboarding fallback procedure** — When a client first asks about T1135 and the required-input list in Section 2 is incomplete, do NOT guess and do NOT refuse. Run this onboarding fallback: 1. Confirm the two screening facts before anything else: (a) Canadian tax residency status for the year, and (b) whether the client is an individual in their first year of Canadian residence. Without these, no further analysis is reliable. 2. If residency is unclear -- fire R-CA-T1135-2 and stop. 3. If residency is confirmed and the first-year exception does not apply, ask one targeted question per missing input, in this priority order: 1. Cost amount (CAD) of each foreign property at any time in the year 2. Whether any property is inside a registered plan (RRSP, RRIF, TFSA, RESP, DPSP) 3. Whether any property is personal-use or used exclusively in an active business 4. Country code and institution / issuer for each property 5. Whether property is held with a Canadian registered securities dealer or Canadian trust company (Category 7 path) 6. Joint ownership, nominee, trust, or partnership structure 4. If cost amount is genuinely unobtainable (e.g., inherited foreign asset with no stepped-up basis records) -- fire R-CA-T1135-4 and recommend cost-basis reconstruction with a Canadian CPA. 5. Produce a partial working paper (Section 8.4 template) with all confirmed facts and explicit MISSING markers. Do NOT produce a final filing conclusion until the asset inventory and threshold test are complete. 6. Maintain the conservative defaults table from Section 1 throughout. Never substitute fair market value for cost amount in the threshold test. The onboarding fallback is the entry path for any first-touch T1135 query. It is NOT a substitute for the Tier 1 rules in Section 4 or the Tier 2 reviewer catalogue in Section 7.

## Section 11 -- Reference material

- **Income Tax Act (Canada), s. 233.3** — Reporting obligation for specified foreign property.  _(https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.3.html)_
- **Income Tax Act (Canada), s. 233.7** — First-year resident exemption for individuals (other than trusts) from sections 233.2, 233.3, 233.4, and 233.6.  _(https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.7.html)_
- **Income Tax Act (Canada), s. 162(7)** — Late-filing penalty for information returns.  _(https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html)_
- **Income Tax Act (Canada), s. 162(10) and 162(10.1)** — Knowing or grossly negligent failure to file; continuing failure beyond 24 months.
- **Income Tax Act (Canada), s. 163(2.4)** — False statement or omission penalty.  _(https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html)_
- **Income Tax Act (Canada), s. 152(4)(b.2)** — Extended reassessment period for unreported foreign income.
- **CRA Form T1135 -- Foreign Income Verification Statement (form and instructions)** — Form and instructions.  _(https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1135.html)_
- **CRA -- Form T1135 reporting for 2015 and later tax years** — Category 7 country-by-country aggregation rule.  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/form-t1135-reporting-2015-later-tax-years.html)_
- **CRA -- Questions and answers about Form T1135** — Q&A: cost amount, threshold, registered-plan exclusion, joint ownership, partnerships.  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html)_
- **CRA -- Foreign Income Verification Statement (overview)** — Overview page.  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/foreign-income-verification-statement.html)_
- **CRA -- Table of penalties (foreign reporting)** — Table of penalties.  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/table-penalties.html)_
- **CRA -- Questions and answers about penalties (foreign reporting)** — Q&A about penalties.  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-penalties.html)_
- **CRA Information Circular IC00-1R6, Voluntary Disclosures Program** — Effective 1 March 2018.  _(https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic00-1/ic00-1r6-voluntary-disclosures-program.html)_

Versioning note: the CRA replaced IC00-1R5 with IC00-1R6 effective 1 March 2018 for income-tax VDP applications. Confirm the current version of any CRA publication before relying on it; CRA periodically reissues these documents under new revision suffixes (e.g., IC00-1R7).

### Prohibitions

- NEVER use fair market value as the threshold test when cost amount is required.
- NEVER assume a Canadian broker removes T1135 exposure.
- NEVER assume no filing because the year-end balance fell below $100,000 CAD.
- NEVER ignore sold-before-year-end assets if the threshold was met during the year.
- NEVER assume personal-use or active-business exclusion without facts.
- NEVER ignore the first-year resident exception.
- NEVER skip amended-return, functional-currency, certification, or paid-preparer fields when assembling the form.
- NEVER present a speculative answer as definitive.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon them. The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
