---
name: sd-tax-overview
description: Use this skill whenever asked for a high-level overview of the Sudanese tax system — the full structure of direct and indirect taxes, the administering authority, recent reform history, and where to start for a deeper dive. Trigger on phrases like "Sudan tax", "Sudan tax system", "Sudan taxation", "الضرائب في السودان", "taxes in Sudan", "Sudan corporate tax", or any request for a top-down summary of Sudan's tax regime. ALWAYS read this skill as the entry point before consulting any Sudan-specific tax skill.
version: 0.1
jurisdiction: SD
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sudan Tax Overview Skill v0.1

## Sudan Tax Overview Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Currency note:** All figures are in Sudanese Pounds (SDG — ج.س). Sudan has undergone multiple currency redenominations; verify current SDG values before filing.
> **YMYL — verify before relying.** Sudan's tax legislation has been subject to amendments and the political situation (post-2021 military takeover, ongoing conflict since April 2023) has disrupted tax administration. Where this skill says "verify current value," re-confirm against the Sudan Taxation Chamber (tax.gov.sd), PwC Worldwide Tax Summaries, or a qualified Sudan accountant.

## Section 1 — Quick reference

**Quick reference**  _(Section 1 — Quick reference)_

| Field | Value |
| --- | --- |
| Country | Republic of Sudan (جمهورية السودان) — note: separate from South Sudan (Republic of South Sudan) since 2011 |
| Capital | Khartoum (الخرطوم) |
| Official language | Arabic; English common in business |
| Currency | Sudanese Pound (SDG — ج.س) — multiple redenominations since 2007 |
| Fiscal year | Calendar year (1 Jan – 31 Dec); companies may use different accounting period with approval |
| Tax year | Calendar year |
| Tax authority | Sudan Taxation Chamber (Diwan Al-Daraib / ديوان الضرائب) under the Ministry of Finance and Economic Planning |
| Customs authority | Exercises and Customs General Administration (الجمارك) |
| Banking authority | Bank of Sudan (البنك المركزي السوداني) |
| Tax system type | Territorial + person principle combined; residents taxed worldwide, non-residents on Sudan-source |
| Self-assessment | Yes — required for most taxpayers |
| Default audit framework | Self-assessment system; Secretary-General issues additional assessments when needed |
| Number of DTA treaties | 17 countries and regions (as of January 2024) |
| ATAF mutual assistance | Implemented since September 2022 |
| Top personal rate | 15% (resident employee); 20% (non-resident, fringe benefits) |
| Standard corporate rate | 15% (general/industrial); 30% (banks, tobacco, petroleum) |
| Standard VAT rate | 17% (40% telecom, 30% cigarettes special rates) |
| Filed currency | SDG (foreign currency must be converted at transaction-date rate) |

## Section 2 — Tax structure map

Sudan classifies taxes into three categories:

### Category 1 — Goods and Services Taxes

**Category 1 — Goods and Services Taxes**  _(Section 2 — Tax structure map)_

| Tax | Authority | Rate | Notes |
| --- | --- | --- | --- |
| **Value Added Tax (VAT)** | Taxation Chamber | 17% standard; 40% telecom; 30% cigarettes; 5% reduced | VAT Act 2001 + 2017 Regulations — see `sd-vat-gst` |
| **Excise Duty** | Taxation Chamber | Schedule-based (subject to Ministerial amendment) | Alcohol, tobacco, luxury items |
| **Customs Duty** | Customs Administration | Schedule-based by HS code | Imports and exports |
| **Special Tax on Services** | State / Local | 3%-10% on service supply; 5%-35% on goods production | Municipal/local taxes |
| **Public Lighting Tax** | State / Local | 5% on alcohol/tobacco at first stage |  |
| **Accommodation / Hotel Tax** | State / Local | 2% on hotel accommodation |  |
| **Patent Tax** | State / Local | Fixed schedule |  |
| **Signboard Tax** | State / Local | Per decimeter-squared and height |  |

### Category 2 — Income Taxes

**Category 2 — Income Taxes**  _(Section 2 — Tax structure map)_

| Tax | Authority | Rate | Notes |
| --- | --- | --- | --- |
| **Corporate Income Tax (BPT)** | Taxation Chamber | 15% standard; 30% sector rates | Income Tax Act 1986 — see `sd-corporate-income-tax` |
| **Individual Income Tax** | Taxation Chamber | 5%-15% progressive (residents); 20% (non-residents/fringe) | Income Tax Act 1986 — see `sd-income-tax` |
| **Capital Gains Tax** | Taxation Chamber | 20% | Separate schedule |
| **Rental Income Tax** | Taxation Chamber | 10% | On real-estate lease income |
| **Tax on Salary** | Employer withholds | Progressive | PAYE system |
| **Withholding Tax** | Payer | 4%-15% (residents); 7%/15% (non-residents) | Final for non-residents |

### Category 3 — Property and Transaction Taxes

**Category 3 — Property and Transaction Taxes**  _(Section 2 — Tax structure map)_

| Tax | Authority | Rate | Notes |
| --- | --- | --- | --- |
| **Stamp Duty** | Taxation Chamber | Schedule (260+ instruments) | Stamp Duty Law 2019 |
| **Real Estate Tax** | State / Local | 0.1% on immovable property |  |
| **Vehicle Tax** | State / Local | Schedule based on type |  |
| **Zakat** | Zakat Chamber | Religious obligation (Islamic tax) | Zakat Act 2001 — separate from Income Tax |
| **Registration/Transfer Tax** | State / Local | 4% on ownership transfer of movable/immovable property |  |
| **Unused Land Tax** | State / Local | 2% on unused land |  |
| **Tax on Means of Transportation** | State / Local | Schedule based on vehicle type/cylinder/seats |  |

### Category 4 — Sector-specific and contractual

**Category 4 — Sector-specific and contractual**  _(Section 2 — Tax structure map)_

| Regime | Authority | Detail |
| --- | --- | --- |
| **Petroleum PSA (Production Sharing Agreement)** | Ministry of Petroleum | BPT 30% statutory, but actual fiscal regime governed by individual concession agreements |
| **Mining / minerals** | Ministry of Minerals | Special mineral production sharing regimes |
| **Free Zones** | Sudan Free Zones Authority | Free Zones Act 2001; corporate tax exemption up to 5 years; VAT exemption on capital equipment |
| **Investment Incentives** | Ministry of Investment and International Cooperation | Investment Incentive Law 2021 — 5-year CIT exemption for qualifying projects |
| **Sukuk (Islamic Finance)** | Central Bank of Sudan (Bank of Sudan) | Subject to regular corporate taxation unless specifically exempt |

## Section 3 — Tax administration architecture

### Sudan Taxation Chamber (مصلحة الضرائب السودانية)

- **Affiliated with:** Ministry of Finance and Economic Planning (وزارة المالية والتخطيط الاقتصادي)
- **Responsibilities:** Tax collection, registration, assessment, inspection, audit for resident and non-resident taxpayers
- **Contact:** Phone 183: 7200555 / 0155771641 — Email executive.tax@tax.gov.sd
- **Address:** Sudan, Khartoum, P.O. Box 2488
- **Portal:** tax.gov.sd

### Related fiscal agencies

**Related fiscal agencies**  _(Section 3 — Tax administration architecture)_

| Agency | Role |
| --- | --- |
| **Exercises and Customs General Administration** | Customs duty, customs VAT at import |
| **General Administration of Finance and Budget** | Government budget oversight |
| **Bank of Sudan** | Central bank, currency policy, Sukuk regulation |
| **National Social Insurance Fund (NPSIF / NSIF)** | Old-age, disability, survivor, work injury contributions |
| **National Health Insurance Fund (NHIF)** | Health insurance contributions |
| **Free Zones Authority** | Free zone licensing and supervision |
| **Ministry of Investment and International Cooperation** | Investment incentives, capital equipment VAT exemption approval |
| **Zakat Chamber** | Religious Zakat collection (Islamic tax) |

## Section 4 — Sudan vs. South Sudan

**Sudan vs. South Sudan comparison**  _(Section 4 — Sudan vs. South Sudan)_

| Aspect | Sudan (Khartoum) | South Sudan (Juba) |
| --- | --- | --- |
| Independence | Pre-2011 (older jurisdiction) | July 9, 2011 |
| Currency | Sudanese Pound (SDG) | South Sudanese Pound (SSP) |
| Tax year | Calendar year | Calendar year |
| Standard corporate rate | 15% | 25% (legal persons) — verify current |
| Personal rate range | 5%-15% resident | 0%-20% progressive (flat-rate scheme) |
| DTA network | 17 countries | Limited — verify |
| Tax authority | Taxation Chamber | National Revenue Authority (NRA) |

## Section 4 — Sudan vs. South Sudan

**Critical:** These are separate jurisdictions since South Sudan's independence in 2011.

**AUDIT FLASH POINT:** Sources may congregate Sudan and South Sudan data. Verify all rates apply to **Sudan (Khartoum)**, not South Sudan (Juba), when researching this skill.

## Section 5 — Tax residence and basis

### Territorial + person hybrid

- **Territorial + person hybrid** — Sudan combines the territoriality and person principles: - Residents taxed on income arising in Sudan AND any place outside Sudan (worldwide for residents) - Non-residents taxed on Sudan-source income only  _(Income Tax Act 1986)_

### Residency tests

- **Residency tests** — For an **individual**: - Present in Sudan for 183 days or more in the period, OR - Present in Sudan in the period and both preceding periods for 12 months or more, OR - Has taken Sudan as their place of residence and shown intention to settle For a **non-individual (company)**: - Control and management are exercised directly in Sudan in the period *(Income Tax Act 1986, terminology section)*  _(Income Tax Act 1986, terminology section)_

## Section 6 — Reform history and recent changes

### Reform timeline

**Reform timeline**  _(Section 6 — Reform history and recent changes)_

| Date | Event | Detail |
| --- | --- | --- |
| **1974** | Social insurance law (consolidating 1919 pensions) | First modern social insurance |
| **1986** | Income Tax Act | Current primary direct tax law |
| **1999/2001** | VAT Act | Replaced earlier sales tax (Sales Tax Act 2000) |
| **2001** | Zakat Act | Separate Islamic-religious tax regime |
| **2001** | Free Zones Act | Special zones for export/manufacturing |
| **2004** | Investment Act | Investment promotion framework |
| **2017** | Companies Act | (Verify — Britacom cited 2015) — corporate registration |
| **2019** | Stamp Duty Law | Modernization of stamp duty framework |
| **2019** | Power transition (post-Bashir regime) | Civilian-Led Transitional Government under Juba Peace Agreement |
| **2021** | Investment Incentive Law | 5-year CIT exemption for qualifying investment projects |
| **October 25, 2021** | Military takeover | Government dissolved; reform momentum paused |
| **September 2022** | ATAF mutual assistance | Cross-border tax cooperation framework |
| **April 2023** | Conflict escalation | Ongoing war between SAF and RSF; government functions disrupted |

### Current status (as of 2026-07)

Sudan's tax administration continues to function in nominal terms but operates under disrupted conditions:
- Taxation Chamber portal (tax.gov.sd) remains online
- Currency has undergone multiple redenominations since the original SDG
- Filing deadlines continue to be observed on paper for many non-digital returns
- IFRS-equivalent accounting (Sudan Accounting Standards) follows IFRS with limited modifications
- Sector-specific taxes (telecom 40%, cigarettes 30%) are commonly challenged by industry

**AUDIT FLASH POINT:** Always verify current thresholds against the Sudan Taxation Chamber (tax.gov.sd) before relying on any rate for compliance purposes. Do not use stale historical SDG figures for filings.

## Section 7 — Currency and denomination considerations

**Currency history**  _(Section 7 — Currency and denomination considerations)_

| Year/Event | Currency note |
| --- | --- |
| Pre-2007 | Sudanese dinar (SDD) — used historically |
| 2007 | Trade currency in USD/EUR permitted in many contexts |
| 2011 | South Sudan independence; shared currency briefly legal tender |
| 2018-Present | Multiple redenominations of the Sudanese Pound (SDG) |
| 2024-2026 | Highly volatile exchange rate; chronic shortage of banknotes drives partial informal dollarisation |

## Section 7 — Currency and denomination considerations

Sudan's currency history is complex:

**Practical implications:**
- Tax computed in SDG but conversion to USD/EUR informally common in business
- Bank transactions on paper records may use multiple currencies over the base period
- Per Income Tax Act 1986, Art 39(3-5): invoices in other currencies must be converted at the **exchange rate at the time of the transaction**, with the rate used stated
- The SDG 3,000 personal exemption was set in pre-redenomination currency; verify current value

**AUDIT FLASH POINT:** When reviewing a client's books, ensure consistent transaction-date conversion methodology. Mixed-presentation across filings is a common audit finding.

## Section 8 — Audit flash points summary

1. **Sudan vs South Sudan** — verify every figure applies to Khartoum jurisdiction.
2. **Currency redenomination** — the SDG figures (3,000 personal allowance, 1,200,000 VAT threshold, 1,500-20,000 NSIF wage base) are from older ordinances. Verify current value before filing.
3. **Sector rates** — 30% applies to banks, tobacco, and petroleum; do not apply 15% standard rate to these sectors.
4. **Telecom 40% and cigarettes 30% VAT** — special VAT rates override the 17% standard.
5. **Self-assessment 2x penalty** — Income Tax Act 1986, Art 38(2) imposes additional tax up to 2x the understated amount; aggressive positions are penalized.
6. **Records retention 6 years minimum** — Arabic or English permitted.
7. **PAYE 15th of following month** — strict monthly remittance deadline.
8. **NSIF vs NHIF** — pension and health contributions go to different funds.
9. **Free zone 5-year clock** — exemption expires from commercial production date.
10. **PSA confidentiality** — petroleum concession terms are confidential; never rely on statutory 30% without checking the agreement.

## Section 9 — Reference material

**Reference material**  _(Section 9 — Reference material)_

| Resource | Reference |
| --- | --- |
| Sudan Taxation Chamber | https://tax.gov.sd/ |
| Income Tax page | https://tax.gov.sd/en/income-tax-2/ |
| Value Added Tax page | https://tax.gov.sd/en/value-added-tax-vat |
| Capital Gains Tax page | https://tax.gov.sd/en/capital-gains-tax |
| Stamp Duty page | https://tax.gov.sd/en/stamp-duty-tax |
| PwC Worldwide Tax Summaries — Sudan | https://taxsummaries.pwc.com/sudan |
| Britacom tax profile — Sudan | https://www.britacom.org/zt/BRPolicies/Sudan/ |
| US State Department Investment Climate Statement | https://www.state.gov/reports/2022-investment-climate-statements/sudan/ |
| ILO Social Protection — Sudan | https://www.social-protection.org/gimi/ShowCountryProfile.action?iso=SD |
| SSA Social Security Worldwide — Sudan | https://www.ssa.gov/policy/docs/progdesc/ssptw/2018-2019/africa/sudan.html |

## Section 10 — Risk-classified treatment summary

**Risk-classified treatment summary**  _(Section 10 — Risk-classified treatment summary)_

| Tax area | Complexity | Common audit finding | Recommended verification |
| --- | --- | --- | --- |
| Standard BPT 15% | Low | Less common — supportability of expenses | Confirm sector eligibility |
| Bank BPT 30% | Medium | Investment incentive misapplication | Confirm not in free zone |
| Petroleum BPT (PSA) | High | PSA terms vs statutory rate discrepancy | Review specific concession agreement |
| Personal income tax (resident) | Medium | Personal allowance applied incorrectly | Verify current SDG 3,000 figure |
| Personal income tax (non-resident) | Low | 20% flat rate application | Confirm residency |
| Rental income 10% | Medium | Net vs gross treatment | Confirm tax base |
| VAT standard 17% | Medium | Reconciliation with invoices | Maintain 5 registers |
| VAT telecom 40% | Medium | Misapplied to non-telecom services | Verify customer category |
| VAT cigarettes 30% | Low | Industry-specific | Usually unambiguous |
| NSIF contributions | Medium | Wage base misapplication (incl/excl allowances) | Confirm gross salary definition |
| Stamp duty | High | 260+ instrument types | Consult Schedule directly |
| Free zones | High | Expiry date miscalculation | Track from commercial production date |
| Cross-border (DTA treaty) | High | Wrong WHT rate applied | Verify specific treaty in force |

## PROHIBITIONS

- Do NOT confuse the Republic of Sudan (Khartoum) with the Republic of South Sudan (Juba) — different tax jurisdictions since 2011.
- Do NOT present current-year rates as final without flagging "verify current value" against the Sudan Taxation Chamber.
- Do NOT apply the SDG 3,000 personal allowance, SDG 1,200,000 VAT threshold, or SDG 1,500/20,000 NSIF wage base without currency-redenomination verification.
- Do NOT use sector rate (30%) for petroleum operations without reviewing the specific PSA / concession agreement.
- Do NOT present Zakat as identical to income tax — Zakat is a religious obligation under the Zakat Act 2001, not part of the Income Tax Act 1986.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in Sudan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

**Sources:** Sudan Taxation Chamber (tax.gov.sd); Income Tax Act 1986; VAT Act 2001 / 2017 Regulations; Stamp Duty Tax Law 2019; Zakat Act 2001; Free Zones Act 2001; Companies Act; Investment Incentive Law 2021; PwC Worldwide Tax Summaries — Sudan; Britacom tax profile; US State Department Investment Climate Statement 2022; ILO Social Protection; SSA Social Security Worldwide.

> Contributed by Ahmed Hassan.

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
