---
name: sd-company-formation
description: Use this skill whenever asked about Sudanese company formation, entity types, registration procedure, capital requirements, sectoral licensing, and tax/VAT registration. Trigger on phrases like "Sudan company registration", "Sudan LLC", "Sudan share company", "Sudan branch registration", "تسجيل شركة السودان", "Sudan GAFI", "company formation Sudan", or any request to incorporate a business in Sudan. ALWAYS read this skill before touching any Sudan company formation or registration work.
version: 0.1
jurisdiction: SD
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on: - company-formation-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sudan Company Formation & Entity Choice Skill

## Sudan Company Formation & Entity Choice Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Currency note:** All figures are in Sudanese Pounds (SDG — ج.س). Sudan has undergone multiple currency redenominations; verify current SDG values before filing.
> **YMYL — verify before relying.** Sudan's company registration framework operates under disrupted conditions since the October 2021 military takeover and the conflict since April 2023. Registration timelines vary widely. Where this skill says "verify current value," re-confirm against the Sudan Taxation Chamber (tax.gov.sd), the Commercial Registrar, or a Sudan-qualified formation agent before acting.

## Section 1 — Scope statement

This skill covers:

- Common entity types under Sudanese corporate law (Companies Act — verify current year)
- Minimum shareholders, directors, and capital requirements
- Commercial (Trade) Registration procedure
- Memorandum and Articles of Association preparation
- Tax registration with the Sudan Taxation Chamber
- VAT registration (when threshold met)
- National Social Insurance Fund (NSIF) registration for employers
- Free zone registration under the Free Zones Act
- Sector-specific licensing (banking, oil, telecom)
- Annual return, audit, and renewal obligations

This skill does NOT cover:

- Computing corporate income tax or filing the return — see `sd-corporate-income-tax`
- VAT return preparation — see `sd-vat-gst`
- Computing PAYE or NSIF contributions — see `sd-payroll-social`
- Sudan tax system overview — see `sd-tax-overview`
- Personal income tax registration — see `sd-income-tax`

## Section 2 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Republic of Sudan (جمهورية السودان) |
| Governing companies law | Companies Act (verify current year — 2015 per Chandrawat; 2017 per Scribd draft — verify against gazette) |
| Registration authority | Commercial (Trade) Registrar, Ministry of Justice |
| Annual returns | Required for active companies |
| Audit requirement | Audited financial statements required for most companies |
| Common entity type | Limited Liability Company (LLC) |
| Foreign ownership | Permitted with sector-specific limitations |
| Minimum LLC members | 1 shareholder and 1 director (any nationality) — verify |
| Minimum share capital (LLC) | No fixed statutory minimum; varies by activity |
| Typical incorporation timeline | Several weeks to months in practice |
| Tax authority | Sudan Taxation Chamber (tax.gov.sd) |
| Tax ID type | Tax Registration Number (TRN) |
| VAT threshold | SDG 1,200,000 annual turnover (see `sd-vat-gst`) |
| Insurance fund | National Social Insurance Fund (NSIF / NPSIF) |
| Free zones authority | Sudan Free Zones & Investment Authority |
| Investment regime | Investment Incentive Law 2021 |

## Section 3 — Entity types, capital and incorporation

### Common entity types

**Common entity types**  _(Companies Act)_

| Entity type | Key features | Source |
| --- | --- | --- |
| **Limited Liability Company (LLC) — شركة ذات مسؤولية محدودة** | 1+ shareholder; 1+ director; any nationality; limited liability; most common for SMEs | Companies Act |
| **Public Joint-Stock Company — شركة مساهمة عامة** | Larger capital; shares publicly tradable; suitable for large enterprises | Companies Act |
| **Private Joint-Stock Company — شركة مساهمة خاصة** | Private shares; shares not publicly tradable | Companies Act |
| **Branch of a Foreign Company — فرع شركة أجنبية** | Foreign company opens a branch; representative required; subject to approval | Companies Act |
| **Partnership — شركة تضامن / شركة توصية بسيطة** | General partnerships (تضامن) with unlimited joint liability; limited partnerships (توصية) with mixed liability | Companies Act |
| **Sole Proprietorship — مؤسسة فردية** | Single owner; unlimited liability; simplest form | Commercial Registrations |

**AUDIT FLASH POINT:** Source uncertain between Companies Act 2015 (per chandrawatpartners) and Companies Act 2017 (per Scribd reference). Verify against the **official Commercial Registrar / gazette publication** before incorporation.

## Section 4 — Registration procedure

### Incorporation steps (typical LLC)

1. **Reserve company name** at the Commercial (Trade) Registrar — verify availability
2. **Prepare Memorandum of Association (MOA)** — includes objectives, capital, members
3. **Prepare Articles of Association (AOA)** — internal governance rules
4. **Submit documents to the Commercial Registrar:**
   - Memorandum of Association
   - Articles of Association
   - Proof of registered address (utility bill or tenancy agreement)
   - Identification documents (passport or national ID) of shareholders and directors
   - Application form
5. **Obtain Commercial Registration certificate**
6. **Register with Sudan Taxation Chamber** for tax purposes and obtain TRN
7. **Register for VAT** if turnover at/above SDG 1,200,000 threshold (or if importing/exporting)
8. **Register with NSIF** if hiring employees for social insurance
9. **Sectoral licensing** where required (banking, oil, telecom — see Section 7)

### Typical timeline

**Typical timeline**

| Step | Typical duration |
| --- | --- |
| Name reservation | 1-3 business days |
| MOA/AOA preparation | 3-7 days |
| Commercial Registrar filing | 1-4 weeks (varies significantly) |
| Tax registration with Taxation Chamber | 1-2 weeks |
| VAT registration (if applicable) | 1-2 weeks |
| NSIF registration | 3 stages (employer, employee enrollment) |
| Sectoral licensing | Varies — banking and petroleum can take 3-6 months |

**Total: typically 4-12 weeks** for a straightforward LLC; significantly longer for sector-licensed industries.

## Section 5 — Capital requirements

**Capital requirements**

| Entity type | Minimum capital | Source |
| --- | --- | --- |
| **LLC** | No fixed statutory minimum; capital varies by activity | Companies Act |
| **Public Joint-Stock Company** | Higher minimum — verify (commonly higher) | Companies Act |
| **Private Joint-Stock Company** | Mid-range minimum — verify | Companies Act |
| **Branch of foreign company** | No separate capital — relies on parent | Companies Act |
| **Free zone company** | Investment minimum defined by Free Zones Authority per sector | Free Zones Act |

**AUDIT FLASH POINT:** The "no fixed statutory minimum" for LLC is widely reported but must be cross-checked against any current Ministerial decree or sector-specific requirement. Capital adequacy is fundamental for banking and petroleum applications.

### Initial depreciation and investment incentives

- **Newly purchased machinery and equipment initial depreciation** — 20% initial depreciation of purchase price after being put into production %  _(Investment Incentive Law 2021)_
- **Qualifying investment projects CIT exemption** — Corporate income tax exemption starting from commercial production date, period not exceeding 5 years (see `sd-corporate-income-tax`)  _(Investment Incentive Law 2021)_

## Section 6 — Tax registrations

### Income tax registration (Tax Authority)

- Every company must register with the Sudan Taxation Chamber
- Tax Registration Number (TRN) is assigned
- Self-assessment system applies — return filed and tax paid at time of submission

### VAT registration (if applicable)

- Required when:
  - Industrial producer, trader, or service provider with turnover ≥ SDG 1,200,000
  - Importer or exporter (regardless of turnover)
  - Voluntary registration available (subject to 2-year minimum commitment)
- Requires filing Form 1 with the local tax office
- Registration Certificate issued (Form 2) — must be displayed at all branches
- See `sd-vat-gst` for full VAT mechanics

- **VAT registration turnover threshold** — SDG 1,200,000 SDG (Industrial producer, trader, or service provider with turnover ≥ SDG 1,200,000; importers/exporters regardless of turnover)

### Social insurance registration (NSIF / NHIF)

**Social insurance registration (NSIF / NHIF)**

| Item | Authority | Mandatory for |
| --- | --- | --- |
| National Pensions and Social Insurance Fund (NSIF) | Ministry of Insurance and Social Development | All employers with employees |
| National Health Insurance Fund (NHIF) | Federal Ministry of Health | All employers with employees |

See `sd-payroll-social` for full contribution mechanics.

## Section 7 — Sectoral licensing

Different sectors require specific pre-registration approvals:

**Sectoral licensing**

| Sector | Approving body | Notes |
| --- | --- | --- |
| **Banking and Finance** | Central Bank of Sudan (Bank of Sudan) | Banking license; capital adequacy requirements; subject to specific contribution rates under Central Bank supervision |
| **Oil and Gas / Petroleum** | Ministry of Petroleum and Gas | Production Sharing Agreement (PSA); BPT 30% statutory; specific PSA terms per concession |
| **Telecommunications** | National Telecommunications Commission | Special VAT rate (40%) applies |
| **Insurance** | Ministry of Insurance and Social Development / Insurance Supervisory Authority | Insurance Supervisory Board approval |
| **Manufacturing / Industrial** | Ministry of Industry and Trade | Industrial license |
| **Agriculture** | Ministry of Agriculture | Agricultural land use approval |
| **Mining / Minerals** | Ministry of Minerals | Special mineral production sharing regimes |
| **Pharmaceuticals / Healthcare** | Federal Ministry of Health, National Medicines and Poisons Board | Medical professional licensing |
| **Education / Professional services** | Relevant ministry | Professional licensing per specialty |
| **Free Zones** | Sudan Free Zones Authority | Free Zones Act 2001 |
| **Charitable / NGO** | Humanitarian Affairs Commission | Registration for tax-exempt charitable bodies |

**AUDIT FLASH POINT:** Sectoral licensing often precedes Commercial Registrartion for foreign-owned entities. Application timelines for banking and petroleum sectors commonly take 3-6 months.

## Section 8 — Free Zones

### Free Zones Act / framework

- Free zones established under the Free Zones Authority / Investment Incentive Law 2021
- Free Trade Zones and Industrial Free Zones are the two main categories
- Multiple zones operational in Sudan (Port Sudan, several inland sites)

### Key incentives

- **Customs exemptions** on imports of capital equipment, raw materials for export production
- **Corporate income tax exemption** up to 5 years from commercial production date
- **VAT exemption** on capital equipment (list approved by Ministry of Investment and International Cooperation)
- Streamlined administrative procedures
- Cap on land allocation for projects

**AUDIT FLASH POINT:** Exemption is time-limited. Track the commercial production start date — the cap applies from there, not from registration.

See `sd-corporate-income-tax` for full free zone tax treatment.

## Section 9 — Annual obligations

### Annual return and renewal

**Annual return and renewal**

| Obligation | Frequency | Source |
| --- | --- | --- |
| Commercial Registry renewal | Annual | Companies Act / Commercial Registration Law |
| Tax return filing | Annual (BPT, capital gains, etc.) | Income Tax Act 1986, Art 38 |
| VAT return filing | Monthly (Form 3) | VAT Regulations 2017 |
| PAYE remittance | Monthly | Income Tax Act 1986 |
| NSIF contribution remittance | Monthly | Social Insurance Act 2016 |
| Audited financial statements | Annual | Companies Act; required for "most companies" |
| Books and records retention | 6 years minimum | Income Tax Act 1986, Art 39(3-5) |

### Audit requirement

Most companies must have financial statements audited by a licensed Sudanese chartered accountant. Audit and submit with the annual return within the prescribed period.

*(Income Tax Act 1986, Art 38/39)*

### Charter requirements

A chartered accountant for tax purposes must be:
- Authorized in writing by the Minister to act as a chartered accountant for the Income Tax law
- Persons leaving Taxation Chamber positions may engage in consulting after 15+ years of service and a university degree *(Income Tax Act 1986)*

## Section 10 — Refusal catalogue

For the formation agent / accountant reviewing the engagement:

- **R-SD-FORM-1** — Do not advise on formation for any sanctioned industry or restricted activity without first confirming it is permitted in Sudan.
- **R-SD-FORM-2** — Do not promise specific timelines for sector-licensed industries (banking, petroleum, telecom).
- **R-SD-FORM-3** — Do not recommend a particular entity type without considering both sector and ownership structure (foreign vs local).
- **R-SD-FORM-4** — Do not assume the SDG 1,200,000 VAT threshold applies to current-period filings without currency-redenomination verification.
- **R-SD-FORM-5** — Do not prepare documents (MOA, AOA) without signed engagement and receipt of all shareholder ID documentation.
- **R-SD-FORM-6** — Do not assume LLC "no minimum capital" applies in practice — some banks require minimum paid-in capital for opening corporate accounts.

## Section 11 — Worked examples

### Example 1 — Standard domestic LLC

**Scenario:** Three Sudanese shareholders want to form a trading company in Khartoum.

- Entity: LLC
- Activities: General trading
- Shareholders: 3 (Sudanese nationals)
- Directors: 3
- Capital: SDG 100,000 (no statutory minimum, but adequate for the activity)
- Timeline: approximately 6-8 weeks

**Documents required:**
1. MOA and AOA
2. Identification for 3 shareholders and directors (passport/national ID)
3. Proof of registered address
4. Commercial Registration form
5. Tax registration with Taxation Chamber
6. VAT registration (when turnover hits threshold)
7. NSIF registration (when employees hired)

### Example 2 — Foreign-owned branch

**Scenario:** Foreign company wants to open a Sudan branch.

- Entity: Branch of Foreign Company
- Approval: Investment Authority + Commercial Registrar
- Capital: No separate capital — based on parent
- Local representative: Required
- Timeline: 3-6 months
- Sectoral licensing: Often required (consulting, contracting, oil services)

**Additional documents:**
- Parent company board resolution approving branch establishment
- Parent company's articles of association and certificate of incorporation
- Power of attorney for branch representative
- Translation to Arabic (certified)

### Example 3 — Free zone manufacturing

**Scenario:** Foreign manufacturing investor establishes a company in a Sudanese free zone.

- Entity: LLC in Free Zone
- Approval: Free Zones Authority + Commercial Registrar
- Tax treatment: 5-year CIT exemption from commercial production date
- VAT treatment: Exemption on capital equipment (per Ministry-approved list)
- Timeline: 8-12 weeks (excluding investment authority approval)

## Section 12 — Self-checks

Before delivering incorporation guidance, verify:

- [ ] Entity type matches goals (LLC, joint-stock, branch, partnership, sole proprietorship)
- [ ] Owners and directors have confirmed identity and nationality status
- [ ] Sector-specific licensing requirements identified (banking, oil, telecom, etc.)
- [ ] Tax registration with Taxation Chamber confirmed
- [ ] VAT registration required (threshold check, importer status, volatility)
- [ ] NSIF and NHIF registration plan for first employee hire
- [ ] Free zone eligibility confirmed if applicable
- [ ] Currency-redenomination caveat added to all SDG figures
- [ ] Banks confirmed they require the formed-entity's certificate before account opening
- [ ] Audit and annual filing obligation explained to client
- [ ] 6-year books retention obligation communicated

## Section 13 — Reference material

**Reference material**

| Resource | Reference |
| --- | --- |
| Sudan Taxation Chamber | https://tax.gov.sd/ |
| Income Tax Act 1986 | https://tax.gov.sd/en/income-tax-2/ |
| VAT Act 2001 / 2017 Regulations | https://tax.gov.sd/en/value-added-tax-vat |
| Investment Authority | https://mof.gov.sd/ |
| Britacom — Sudan tax profile | https://www.britacom.org/zt/BRPolicies/Sudan/ |
| US State Dept Investment Climate Statement | https://www.state.gov/reports/2022-investment-climate-statements/sudan/ |
| Chandrawat Partners — incorporate LLC Sudan | https://chandrawatpartners.com/how-to-incorporate-an-llc-in-sudan-insights-compliances-much-more/ |
| MaxisHR — Company Registration in Sudan | https://maxishr.com/en/sudan/company-registration |

## PROHIBITIONS

- Do NOT advise forming a company for a sanctioned or restricted activity without clear regulatory confirmation.
- Do NOT promise specific timelines for sector-licensed industries.
- Do NOT apply the SDG 1,200,000 VAT threshold without currency-redenomination verification.
- Do NOT prepare MOA/AOA without receiving all signed shareholder documents.
- Do NOT confuse the Republic of Sudan's Commercial Registrar with South Sudon's Corporate Registrar.
- Do NOT present filed registration as a final step — annual renewal and audit obligations continue.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Sudan-licensed formation agent, company secretary, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed formation agent in Sudan, and track updates as company law changes.

**Sources:** Companies Act (Sudan); Income Tax Act 1986; VAT Act 2001 / 2017 Regulations; Free Zones Act 2001; Investment Incentive Law 2021; Britacom; US State Department Investment Climate Statement 2022; Chandrawat Partners; MaxisHR.

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
