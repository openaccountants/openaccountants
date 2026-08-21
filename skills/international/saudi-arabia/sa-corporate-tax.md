---
name: sa-corporate-tax
description: "ALWAYS read this skill before touching any Saudi Arabian corporate income tax (CIT) work. Use this skill whenever asked about Saudi CIT for a resident company with non-Saudi/non-GCC shareholders, a Saudi PE of a non-resident, or a \"mixed\" entity owned partly by Saudi/GCC nationals and partly by foreigners. Trigger on phrases like \"Saudi CIT\", \"Saudi corporate income tax\", \"Saudi corporate tax\", \"ZATCA CIT 20%\", \"Saudi mixed entity\", \"Saudi PE tax\", \"Saudi Income Tax Law\", \"Royal Decree M/1\", \"Saudi non-resident tax\", \"Saudi natural gas tax\", \"Saudi hydrocarbons tax\", \"Saudi 50%/85% tax\", \"Article 21 ITL\", \"Article 12 ITL interest limitation\", \"Saudi transfer pricing\", \"Saudi Pillar Two\", \"Saudi DMTT\", \"Saudi 120 days filing\". Covers the 20% standard rate under the Income Tax Law (Royal Decree M/1 dated 15/1/1425H — 6 March 2004) and its Implementing Regulations on foreign-shareholder taxable income, the 30% natural gas rate, the tiered 50%–85% oil and other hydrocarbons rates depending on capital base, the mixed-entity Zakat/CIT split for partly Saudi/GCC-owned companies, Saudi PE attribution for non-residents, the indefinite loss carry-forward capped at 25% of annual taxable income (Article 21), the 50% of EBITDA interest deduction limitation (Article 12), the transfer-pricing Bylaws (2019) with BEPS Action 13 MF/LF/CbCR thresholds, the Pillar Two Domestic Minimum Top-up Tax track (TBC for 2025–2026 enactment), the ZATCA portal filing within 120 days of fiscal year-end, and quarterly advance CIT instalments where applicable. Out of scope: Zakat-only entities (Saudi/GCC-owned — see sa-zakat), the Real Estate Transaction Tax, withholding tax compliance detail (see sa-withholding-tax), VAT and e-invoicing (see saudi-arabia-vat and saudi-einvoice), group consolidated returns outside specific share-deal structures, special economic zones (e.g., RHQ Program 30-year exemption, ILBZ, KAEC, Ras Al-Khair, NEOM), bank/insurance specialised computational regimes beyond the rate reference, mutual funds and investment funds, and any ZATCA dispute or appellate proceedings."
jurisdiction: SA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mehran Habib
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SA Corporate Tax

## Saudi Arabia — Corporate Income Tax — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a Saudi-licensed tax professional (SOCPA member or ZATCA-recognised tax adviser) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mehran Habib** on 2026-06-06.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Corporate Tax (CIT)

- **Standard CIT** — 20% on foreign-share taxable income  _(Income Tax Law Art. 7 (Chapter Three, Article 7(A)))_
- **Natural gas investment** — 0.2  _(Income Tax Law (Chapter Three, Article 7(B)))_
- **Oil and hydrocarbons** — 0.85  _(Income Tax Law (Chapter Three, Article 7(C)))_
- **Loss carry-forward** — Indefinite, capped at 25% of taxable income per year  _(ITL Art. 21 (Chapter Five, Article 21(A)))_
- **Interest deduction limit** — The deductible amount of interest is limited to the Lower of Actual Loan Charges (Interest expense) incurred during the tax year if related to income subject to tax OR The resultant of the following formula: Interest Income + 50% of (A - B) where A = income subject to tax other than interest income, B = expenses allowed under the Law other than interest expense.  _(ITL Art. 12)_
- **TP documentation (CbCR)** — Group revenue > SAR 3.2 billion  _(TP Guidelines ZATCA (Third Edition) 2019 bylaws)_
- **Record retention** — 10 years  _(Income Tax Law Art. 58)_
- **Annual return** — 120 days after FYE  _(ITL Chapter Twelve, Article 60(B))_
- **Late payment penalty** — 5% per month, capped at 25%  _(ITL Chapter Fourteen, Article 76(B))_

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Kingdom of Saudi Arabia (KSA) |
| Tax | Corporate Income Tax (CIT) — under the Income Tax Law |
| Currency | SAR (Saudi Riyals) |
| Tax year | Gregorian financial year of the taxpayer (most commonly 1 January – 31 December). Hijri or non-calendar fiscal years are permitted if reflected in the commercial registration and articles. |
| Primary legislation | **Income Tax Law (ITL)** — Royal Decree No. **M/1** dated **15/1/1425H (6 March 2004)** |
| Supporting rules | Implementing Regulations to the ITL; Transfer Pricing Bylaws (2019); Ministerial decisions; ZATCA circulars and guides |
| **Taxable persons** | (a) Non-Saudi/non-GCC **shareholders** in resident companies (on their share of taxable income); (b) **non-residents** earning Saudi-source income (PE or specific transactions); (c) **Saudi PEs of non-residents**. Saudi and GCC nationals are NOT subject to CIT — they pay **Zakat** (see `sa-zakat`). |
| **Standard CIT rate** | **20%** on adjusted taxable income (foreign-share portion / non-resident PE) |
| **Natural gas investment** | **30%** on taxable income from natural gas investment activities |
| **Oil and other hydrocarbons** | **Tiered 50%–85%** depending on capital base (see §4.2) |
| **Banks / insurance** | Special computational provisions exist, but the **standard 20%** rate generally applies on the non-Saudi/GCC share — sector-specific computational rules are largely out of scope (R-SA-CT-2) |
| **Mixed entities** | Foreign shares → **CIT** (proportional); Saudi/GCC shares → **Zakat** (proportional) |
| **Loss carry-forward** | **Indefinite**, capped at **25%** of taxable income each year (**Article 21 ITL**). No carry-back. |
| **Group consolidation** | Not generally available except specific share-deal structures (R-SA-CT-3) |
| **Transfer pricing** | TP Bylaws since **2019**; **OECD Master File / Local File / CbCR** required for groups > **SAR 750M** consolidated revenue (BEPS Action 13 aligned) |
| **Interest deduction limitation** | **50% of EBITDA** (**Article 12 ITL**) — excess interest non-deductible (with carry-forward) |
| **Pillar Two / DMTT** | KSA committed to OECD Pillar Two; **Domestic Minimum Top-up Tax** expected effective **2025–2026** — **TBC** (verify enactment status) |
| **Withholding tax** | See `sa-withholding-tax` for compliance detail; WHT credits feed into CIT computation |
| **Annual return** | Filed via **ZATCA portal** within **120 days** of fiscal year-end |
| **Quarterly advance CIT** | Instalments where applicable (see §6.3) |
| Tax authority | **Zakat, Tax and Customs Authority (ZATCA)** |
| Filing portal | ZATCA portal at zatca.gov.sa |
| Record retention | Minimum **10 years** (verify against current ZATCA guidance and Implementing Regulations) |
| **Penalties** | **5% per month** late payment (capped at **25%**); separate failure-to-file fines |
| Validated by | Pending — sign-off by a SOCPA member or ZATCA-recognised tax adviser |
| Skill version | 1.0 |

### 1.1 Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Shareholder nationality unclear | Treat as foreign (CIT applies) until Saudi/GCC nationality is documented |
| Resident-company sector unclear | Default to standard 20% (not 30% gas, not 50–85% oil); flag |
| Activity boundary unclear (e.g., upstream vs downstream hydrocarbons) | Default to standard 20% and flag for reviewer; do not apply the elevated rates without confirmation |
| Mixed-entity ownership percentages unverified | Use Commercial Registration / shareholder register as filed; do not assume |
| Loss carry-forward cap | Always apply the 25% annual cap under Article 21 |
| Interest deduction | Always apply the 50% of EBITDA cap under Article 12; track disallowed interest for carry-forward |
| TP documentation threshold | Apply CbCR/MF/LF requirements at SAR 750M group consolidated revenue; flag where uncertain |
| Pillar Two / DMTT | Mark **TBC**; do not commit to a number until enactment confirmed |
| Filing deadline | **120 days** from FYE — never assume an extension |
| Group consolidation | Treat companies as standalone unless a specific share-deal structure is documented |
| Penalty figures | Apply 5%/month capped at 25% as headline; defer specific cases to reviewer |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

**Minimum viable** — Full-year audited (or draft) financial statements (income statement, balance sheet, cash flow), prior-year CIT/Zakat return as filed with ZATCA, Commercial Registration (CR) showing shareholder composition with nationality breakdown, articles of association, confirmation of fiscal year-end, sector classification (standard / natural gas / hydrocarbons / banking / insurance), and any TP-relevant related-party transaction summary.

**Recommended** — General ledger, fixed-asset register with depreciation schedule, related-party transactions schedule, withholding tax credit certificates, prior-year tax-loss carry-forward schedule (with Article 21 25% cap tracking), prior-year disallowed interest carry-forward (Article 12), advance tax payment receipts, ZATCA correspondence and prior assessments.

**Ideal** — Audited statements signed by a SOCPA-registered audit firm, complete tax computation reconciling accounting profit to taxable income, Master File / Local File / CbCR where group consolidated revenue exceeds SAR 750M, shareholder register with nationality and percentages, board resolutions for material elections, and confirmation of Pillar Two / DMTT scoping if part of an in-scope MNE group.

**HARD STOP if minimum is missing.** Without financial statements, the CR with shareholder nationality breakdown, and the prior-year return, no CIT computation may be produced — the Zakat/CIT split cannot be determined.

### 2.2 Refusal Catalogue

- **R-SA-CT-1** — Saudi/GCC-only-owned entities. Companies wholly owned by Saudi or GCC nationals/entities are subject to Zakat, not CIT. Out of scope — see `sa-zakat`.  _(R-SA-CT-1)_
- **R-SA-CT-2** — Specialised sector regimes. Banking and insurance carry sector-specific computational rules beyond the rate. Out of scope except for the rate reference. Investment funds, mutual funds, and similar collective vehicles — out of scope.  _(R-SA-CT-2)_
- **R-SA-CT-3** — Group consolidated returns. Saudi tax law does not generally permit group consolidation. Specific share-deal structures may produce de facto consolidation effects — out of scope for this skill; refer to a SOCPA adviser.  _(R-SA-CT-3)_
- **R-SA-CT-4** — Special Economic Zones and incentive regimes. Includes the Regional Headquarters (RHQ) Program (30-year tax incentive package), the Integrated Logistics Bonded Zone (ILBZ), King Abdullah Economic City (KAEC), Ras Al-Khair, NEOM, and other zone-specific incentives. Out of scope — escalate to a SOCPA adviser familiar with the specific zone.  _(R-SA-CT-4)_
- **R-SA-CT-5** — Hydrocarbons upstream / oil and gas concessions. The tiered 50%–85% rates are referenced for completeness only. Actual computation involves concession-specific terms, cost-recovery mechanics, and Ministry of Energy interactions. Out of scope — escalate.  _(R-SA-CT-5)_
- **R-SA-CT-6** — Active ZATCA assessment / audit / appellate proceedings. Tax Violations and Disputes Resolution Committee (TVDRC), General Secretariat of Zakat, Tax and Customs Committees, or Court of Appeal proceedings — escalate. Do not produce numbers that pre-empt the dispute.  _(R-SA-CT-6)_
- **R-SA-CT-7** — Transfer-pricing controversy. Active APA, MAP, or controversy under the TP Bylaws — out of scope.  _(R-SA-CT-7)_
- **R-SA-CT-8** — Cross-skill scope. VAT → `saudi-arabia-vat`; e-invoicing → `saudi-einvoice`; withholding tax compliance → `sa-withholding-tax`; Zakat → `sa-zakat`; Real Estate Transaction Tax — separate skill (TBD).  _(R-SA-CT-8)_
- **R-SA-CT-9** — Pillar Two ambiguity. Where the Domestic Minimum Top-up Tax (DMTT) enactment status, scope, or effective date is uncertain, flag as TBC and decline to commit to a number until the gazetted instrument is verified.  _(R-SA-CT-9)_
- **R-SA-CT-10** — Tax treaty positions and PE determinations. Treaty-based PE analysis, Article 5 thresholds, treaty residency, and tie-breakers — escalate to a SOCPA adviser for any taxpayer claiming treaty relief.  _(R-SA-CT-10)_

## Section 3 — Tier 1 — Taxable Persons, Taxable Base, 20% Standard Rate

### 3.1 Taxable Persons

- **Taxable persons** — Saudi CIT applies to: 1. Non-Saudi/non-GCC shareholders of a resident company — taxed on their share of the company's taxable income (the company computes a single taxable income, then attributes the non-Saudi/GCC share to CIT and the Saudi/GCC share to Zakat — see "mixed entity" mechanics in §3.4 and §5.2). 2. Non-residents earning Saudi-source income — through a Permanent Establishment (PE) under Article 4 ITL or via specific transactional withholding regimes (see `sa-withholding-tax`). 3. Saudi PEs of non-residents — taxed on attributable income computed under Articles 4–5 ITL and Implementing Regulations. Saudi and GCC nationals are NOT subject to CIT. Their share is subject to Zakat instead (2.5% of the Zakat base — see `sa-zakat`).  _(ITL Articles 1–4 and Implementing Regulations)_

### 3.2 Standard Rate — 20%

- **Standard CIT rate** — 20% of adjusted taxable income for: the foreign-shareholder share in a resident company; Saudi PEs of non-residents; non-resident persons earning Saudi-source business income.  _(Article 7(a) ITL)_
- **CIT standard formula** — CIT = 20% × Adjusted Taxable Income (foreign-share portion or PE attributable income)  _(Article 7(a) ITL)_
- **Scope of standard rate** — This rate applies to all sectors except (i) natural gas investment (30%), (ii) oil and other hydrocarbons (tiered 50%–85%), and (iii) any specific incentive regimes (out of scope).  _(Article 7(a) ITL)_

### 3.3 Taxable Base — Adjusted Taxable Income

- **Adjusted Taxable Income formula** — Adjusted Taxable Income = Gross Income (Article 6) − Allowable Deductions (Articles 8–17) − Tax depreciation (Articles 17, declining-balance per asset class) − Loss carry-forward (Article 21, capped at 25% of annual taxable income) ± Adjustments per Implementing Regulations  _(Articles 5–6 ITL and Implementing Regulations)_

**Key adjustments**  _(Articles 5–6 ITL and Implementing Regulations)_

| Item | Treatment |
| --- | --- |
| Provisions and contingent expenses | Generally non-deductible unless realised |
| Related-party expenses without arm's-length pricing | Disallowed to the extent non-arm's-length (TP Bylaws) |
| Interest expense | Deductible up to **50% of EBITDA** (Article 12); excess carried forward |
| Bad debts | Deductible when written off and Article 13 conditions are met |
| Donations / charitable contributions | Deductible only if to a public-benefit entity approved by the relevant authority (Article 13(c) and Implementing Regulations) |
| Dividends paid | Not deductible |
| Income tax / Zakat paid | Not deductible |
| Withholding tax paid by the company (gross-up scenarios) | Specific Implementing-Regulation treatment — verify |
| Foreign tax | Foreign tax credit available under Article 6(c) and Implementing Regulations |

### 3.4 Mixed-Entity Computation Mechanics

- **Mixed-entity computation** — Foreign-share portion = Total Adjusted Taxable Income × (Non-Saudi/GCC ownership %) CIT                  = 20% × Foreign-share portion Saudi/GCC-share portion = Total tax base for Zakat purposes × (Saudi/GCC ownership %) Zakat                  = 2.5% × Saudi/GCC Zakat base (see sa-zakat)
- **Ownership percentage timing** — The ownership percentages are taken from the Commercial Registration (CR) as of the last day of the fiscal year (or per the Implementing Regulations where a change occurred mid-year — verify).
- **Conservative default** — Use the CR snapshot at year-end; flag any mid-year ownership changes for reviewer to apportion correctly under the Implementing Regulations.

### 3.5 Permanent Establishment (PE) — Article 4 ITL

- **Permanent Establishment** — A non-resident has a Saudi PE where it carries on business through a fixed place of business in KSA, including: a branch, office, factory, workshop, or place of management; a building site, construction or installation project (subject to the duration threshold per the ITL / applicable treaty); the provision of services in KSA (subject to the services-PE threshold per the ITL / applicable treaty); a dependent agent habitually concluding contracts in KSA on behalf of the non-resident.  _(Article 4 ITL)_
- **Treaty override** — Treaty positions override domestic-law thresholds where a treaty applies and the taxpayer claims treaty benefits. Treaty-based PE analysis is out of scope (R-SA-CT-10).  _(R-SA-CT-10)_
- **PE CIT formula** — PE CIT = 20% × Adjusted Taxable Income attributable to the PE  _(Article 5 ITL)_
- **Attribution principle** — Attribution follows the separate-enterprise principle under Article 5 and Implementing Regulations.  _(Article 5 ITL)_

### 3.6 Loss Carry-Forward — Article 21

- **Loss carry-forward formula** — Loss carry-forward = Indefinite (no time limit) Annual offset cap  = 25% of taxable income in the offset year  _(Article 21)_
- **Loss continuity** — Losses may be carried forward indefinitely but the offset against any single year's taxable income is capped at 25% of that year's taxable income. Carry-back is not available. Loss continuity requires continuity of ownership and business activity (Implementing Regulations — verify the precise tests for material ownership changes).  _(Article 21)_

### 3.7 Interest Deduction Limitation — Article 12

- **Interest deduction cap formula** — Maximum deductible interest = 50% × EBITDA EBITDA = Earnings before interest, tax, depreciation, and amortisation (Implementing-Regulation definition)  _(Article 12)_
- **Carry-forward of disallowed interest** — Interest expense in excess of 50% of EBITDA is non-deductible in the current year and is carried forward for deduction in future years (subject to the same 50%-of-EBITDA cap in each future year). The cap applies on a per-entity basis (not consolidated) for standalone CIT computations.  _(Article 12)_
- **Conservative default** — Compute the cap each year, track the disallowed amount as a carry-forward, and never deduct prior-year disallowed interest without confirming current-year EBITDA headroom.

## Section 4 — Tier 2 — Sectoral Rates, Transfer Pricing, Pillar Two, Group Taxation

### 4.1 Natural Gas Investment — 30%

- **Natural gas investment rate** — Taxable income from natural gas investment activities is taxed at 30%. This rate covers upstream natural gas exploration, development, and production where the activity is classified as "natural gas investment" under the ITL and ZATCA guidance.  _(Article 7(b) ITL)_
- **Natural gas CIT formula** — Natural Gas CIT = 30% × Taxable income from natural gas investment activities  _(Article 7(b) ITL)_
- **Scope narrow** — Scope is narrow — verify with ZATCA / reviewer whether the activity is classified as natural gas investment or falls under standard 20% or the hydrocarbons tier. Activity boundary uncertainty defaults to 20% with a flag (do not apply elevated rates without confirmation).

### 4.2 Oil and Other Hydrocarbons — Tiered 50%–85%

**Capital Base table**  _(Article 7(c) ITL)_

| Capital Base | Indicative Rate |
| --- | --- |
| Above SAR 375 billion (largest concession holders) | **85%** |
| Mid-tier capital base | Sliding intermediate rates |
| Lower capital base (per the ITL schedule) | **50%** floor |

*(Reviewer: confirm the precise capital-base bands and intermediate rates against the current ITL text and ZATCA implementing guidance — the schedule has been updated by Royal Decrees in recent years.)*

- **Hydrocarbons CIT formula** — Hydrocarbons CIT = (Tier rate per capital base) × Taxable income from oil/other hydrocarbons  _(Article 7(c) ITL)_
- **R-SA-CT-5 reference** — Out of scope (R-SA-CT-5) — the rate is referenced only for completeness. Actual computation involves concession terms, cost recovery, and Ministry of Energy / ZATCA interactions.  _(R-SA-CT-5)_

### 4.3 Banks and Insurance — Standard Rate with Sector Specials

- **Banks and insurance treatment** — The standard 20% rate generally applies to the foreign-share portion of banks and insurance companies, but the computational base carries sector-specific rules (provisioning, technical reserves, gross premium treatment, etc.). Sector-specific computational regimes are out of scope (R-SA-CT-2) beyond the rate reference.  _(R-SA-CT-2)_

### 4.4 Group Taxation — Not Generally Available

- **Group taxation** — Saudi tax law does not generally permit group consolidated returns. Each resident entity files separately. Specific share-deal structures (mergers, demergers, share-for-share exchanges under Articles in the ITL and Implementing Regulations) may produce rollover or deferred outcomes, but these are out of scope (R-SA-CT-3) for this skill.  _(R-SA-CT-3)_

### 4.5 Transfer Pricing — TP Bylaws (2019)

- **TP Bylaws legislation** — Transfer Pricing Bylaws issued by ZATCA (then GAZT) effective 2019, aligned with OECD BEPS Action 13.  _(Transfer Pricing Bylaws (2019))_

**Documentation requirements**

| Document | Threshold | Filing |
| --- | --- | --- |
| **Country-by-Country Report (CbCR)** | Group consolidated revenue > SAR 750M (≈ EUR 750M / BEPS Action 13 threshold) | Annual filing by the Ultimate Parent or surrogate; KSA constituent files CbCR notification |
| **Master File** | Same SAR 750M threshold | Maintained and submitted to ZATCA upon request |
| **Local File** | KSA entity with related-party transactions above the prescribed threshold | Maintained and submitted to ZATCA upon request |
| **Disclosure Form** | All taxpayers with related-party transactions | Filed with the annual CIT return |

- **Arm's-length principle** — Arm's-length principle applies to all related-party transactions. The five OECD methods are accepted (CUP, RPM, CPM, TNMM, Profit Split). Country-by-country reporting uses the same template and exchange mechanism as the OECD CbC Standard.
- **Conservative default** — For any group exceeding SAR 750M consolidated revenue, treat MF / LF / CbCR as required and flag for reviewer. For below-threshold groups, the Disclosure Form still applies — verify.

### 4.6 Pillar Two — Domestic Minimum Top-up Tax (DMTT) — **TBC**

- **DMTT status** — KSA has committed to OECD Pillar Two and is expected to implement a Domestic Minimum Top-up Tax (DMTT) effective 2025–2026. As of skill version 1.0 the precise enactment status, scope, and effective date are TBC — verify against the current ZATCA / Ministry of Finance instruments and the gazetted Royal Decree.
- **Conservative default** — For any MNE group with consolidated revenue ≥ EUR 750 million in at least two of the four preceding fiscal years (the Pillar Two scope threshold), flag DMTT applicability for reviewer. Do not compute a top-up amount until enactment is confirmed and the GloBE / DMTT rules are loaded into the workflow.

### 4.7 Withholding Tax — Cross-Skill Reference

- **WHT cross-reference** — WHT under Articles 68–69 ITL applies to certain payments from Saudi-resident payers to non-residents (e.g., royalties, technical services, management fees, dividends, interest, rent). Rates vary by category and treaty position. Detailed WHT compliance is out of scope — see `sa-withholding-tax`. WHT borne by the foreign-shareholder side of a mixed entity may interact with CIT credit mechanics — verify.  _(Articles 68–69 ITL)_

## Section 5 — Worked Examples

### 5.1 100% Foreign-Owned LLC — Standard 20%

**Facts:** GlobalTech Saudi LLC. Resident KSA company, **100% owned** by a non-Saudi, non-GCC parent. Fiscal year 1 Jan 2025 – 31 Dec 2025.
- Gross income (Article 6): SAR 80,000,000.
- Deductible expenses (Articles 8–17, excluding interest): SAR 50,000,000.
- Interest expense: SAR 8,000,000.
- EBITDA (per Implementing Regulations definition): SAR 38,000,000.
- Tax depreciation: SAR 4,000,000.
- Prior-year loss carry-forward (Article 21): SAR 6,000,000.

#### 5.1.1 Interest deduction limitation (Article 12).

```
Cap = 50% × EBITDA = 50% × 38,000,000 = SAR 19,000,000
Interest expense (SAR 8,000,000) ≤ Cap (SAR 19,000,000)
→ Full SAR 8,000,000 deductible. No carry-forward.
```

#### 5.1.2 Taxable income (pre-loss).

```
Gross income                       SAR 80,000,000
Less: Deductible expenses         (SAR 50,000,000)
Less: Interest (within cap)        (SAR  8,000,000)
Less: Tax depreciation             (SAR  4,000,000)
                                   ───────────────
Taxable income (pre-loss)          SAR 18,000,000
```

#### 5.1.3 Loss carry-forward (Article 21 25% cap).

```
Annual offset cap = 25% × 18,000,000 = SAR 4,500,000
Loss b/f                         = SAR 6,000,000
Loss applied this year (capped)  = SAR 4,500,000
Loss remaining for c/f           = SAR 1,500,000
```

#### 5.1.4 CIT.

```
Adjusted taxable income = 18,000,000 − 4,500,000 = SAR 13,500,000
CIT @ 20%               = 20% × 13,500,000       = SAR  2,700,000
```

#### 5.1.5 Filing.

Return due via ZATCA portal within **120 days** of 31 Dec 2025 → by **30 April 2026**. Tax payable with the return; quarterly advance instalments (Section 6.3) may have already discharged part of the liability.

### 5.2 60/40 Mixed Entity (40% Foreign, 60% Saudi/GCC)

**Facts:** Riyadh Trading Co. Resident KSA company. **60% Saudi nationals, 40% non-Saudi/non-GCC** per the CR as at 31 Dec 2025. Fiscal year 1 Jan 2025 – 31 Dec 2025.
- Adjusted taxable income (per ITL): SAR 25,000,000.
- Zakat base (per Zakat regulations — see `sa-zakat`): SAR 30,000,000.

#### 5.2.1 Foreign-share CIT.

```
Foreign-share portion = 40% × 25,000,000 = SAR 10,000,000
CIT @ 20%             = 20% × 10,000,000 = SAR  2,000,000
```

#### 5.2.2 Saudi/GCC-share Zakat (reference — see sa-zakat).

```
Saudi/GCC-share Zakat base = 60% × 30,000,000 = SAR 18,000,000
Zakat @ 2.5%               = 2.5% × 18,000,000 = SAR    450,000
```

#### 5.2.3 Total ZATCA liability.

```
CIT                          SAR 2,000,000
Zakat (cross-reference)      SAR   450,000
                             ─────────────
Total                        SAR 2,450,000
```

**Filing:** Single annual return via ZATCA portal within **120 days** of 31 Dec 2025 → by **30 April 2026**. CIT and Zakat reported on the integrated return (see Section 6).

**Reviewer note:** The Zakat base and the CIT taxable income are **not the same number** — they are computed under different rules. Always compute them independently. This example assumes the Zakat base is provided; the actual Zakat computation is delegated to `sa-zakat`.

### 5.3 Saudi PE of a Non-Resident

**Facts:** ForeignCo SARL (resident in a treaty country) operates a project office in Riyadh constituting a Saudi PE under Article 4 ITL. Fiscal year 1 Jan 2025 – 31 Dec 2025.
- Saudi-source revenue attributable to the PE: SAR 40,000,000.
- Allocable head-office expenses (under Implementing Regulations and the separate-enterprise principle): SAR 5,000,000.
- Local PE expenses (rent, salaries, depreciation): SAR 28,000,000.
- Adjusted taxable income attributable to the PE: SAR 7,000,000.

#### 5.3.1 PE CIT.

```
PE CIT = 20% × 7,000,000 = SAR 1,400,000
```

#### 5.3.2 Considerations.

- **Treaty position:** If ForeignCo's home jurisdiction has a treaty with KSA, the treaty may modify the PE threshold or the attribution rules — **out of scope (R-SA-CT-10)**, escalate to reviewer.
- **WHT interaction:** Payments to the PE by Saudi customers may be subject to WHT under Articles 68–69; WHT borne is generally creditable against the PE's CIT liability subject to the Implementing Regulations — see `sa-withholding-tax`.
- **Repatriation of branch profits:** Saudi domestic law imposes a separate WHT on branch-profit remittances — verify the current rate and whether the treaty modifies it.

**Filing:** PE files a Saudi CIT return via the ZATCA portal within **120 days** of fiscal year-end. Quarterly advance CIT instalments apply where the prior-year liability exceeds the threshold (Section 6.3).

## Section 6 — Filing and Payment Mechanics

### 6.1 Annual Return — ZATCA Portal

**Form:** Integrated annual Zakat / Income Tax / WHT return — filed electronically via the **ZATCA portal** (zatca.gov.sa). Mixed entities file a single return that splits CIT and Zakat per ownership.

**Required attachments / schedules**

| Schedule | Content |
| --- | --- |
| Main return | Computation of adjusted taxable income; CIT payable; Zakat payable for mixed entities |
| Audited financial statements | Attached |
| Schedule of related-party transactions / TP Disclosure Form | Required for all taxpayers with RPTs |
| Master File / Local File | If group consolidated revenue > SAR 750M (submitted on request) |
| CbCR notification / CbCR | If group consolidated revenue > SAR 750M |
| Schedule of loss carry-forward | Article 21 tracking with 25% annual cap applied |
| Schedule of interest carry-forward | Article 12 disallowed interest tracking |
| Schedule of WHT credits | Linked to `sa-withholding-tax` |
| Shareholder register snapshot | Nationality and ownership percentages for mixed-entity allocation |

### 6.2 Filing Deadlines

**Filing Deadlines table**

| Item | Deadline |
| --- | --- |
| Annual CIT return | **Within 120 days of fiscal year-end** (e.g., FYE 31 Dec 2025 → due 30 Apr 2026) |
| Annual tax payable balance | Due with the annual return |
| Quarterly advance CIT instalment 1 | End of 6th month of the current fiscal year (verify per Implementing Regulations) |
| Quarterly advance CIT instalment 2 | End of 9th month |
| Quarterly advance CIT instalment 3 | End of 12th month |
| CbCR / Notification | Per ZATCA TP Bylaws schedule (typically aligned to BEPS Action 13 timing) |
| Extension request | Application to ZATCA; not automatic — must be filed before the deadline with justification |

*(Reviewer: confirm the advance-instalment due-date schedule against the current Implementing Regulations — historically advance instalments are tied to the 6th, 9th, and 12th months of the fiscal year, but verify.)*

### 6.3 Advance CIT Instalments

- **Advance instalments rule** — Taxpayers whose prior-year tax liability exceeded a prescribed threshold must pay three advance instalments during the current fiscal year, each generally 25% of the prior-year liability (less specified credits), with the balance due on the annual return.  _(Article 60 ITL and Implementing Regulations)_
- **Advance instalment formula** — Per-instalment amount ≈ 25% × Prior-year CIT (less applicable credits per Implementing Regulations) Balance with annual return = Current-year CIT − advance instalments − WHT credits  _(Article 60 ITL and Implementing Regulations)_
- **Reduction and conservative default** — If the taxpayer reasonably estimates that the current-year liability will be materially lower, it may apply to ZATCA to reduce the instalments — subject to default surcharge if the year-end liability exceeds the reduced basis. Conservative default: Pay on the prior-year basis unless a formal reduction is approved by ZATCA.

### 6.4 Penalties

**Penalties table**

| Infraction | Sanction |
| --- | --- |
| Late payment of tax | **5% per month** of the unpaid tax, **capped at 25%** of the unpaid amount |
| Failure to file the annual return on time | Tiered fine per ZATCA schedule (verify current amounts) |
| Failure to maintain records | Per ZATCA schedule |
| Tax evasion (intentional) | Up to **25% of the evaded tax** plus criminal exposure under the ITL penal provisions |
| Failure to file CbCR / MF / LF where required | Per TP Bylaws penalty schedule |
| Late or short advance instalment | Default surcharge per the Implementing Regulations |

- **Conservative default** — Apply 5%/month capped at 25% for late-payment scenarios and flag any other penalty interaction for reviewer to confirm against the current ZATCA penalty schedule.

### 6.5 Audit, Assessment, and Statute of Limitations

- **Audit and limitations** — - Self-assessment — the return as filed forms the basis of assessment unless ZATCA selects for audit. - Audit selection — ZATCA may select on a risk basis or by sector campaign. - Statute of limitations — generally 5 years from the filing of the return, extendable in cases of suspected concealment or fraud (verify against the current ITL / ZATCA guidance). - Disputes — Tax Violations and Disputes Resolution Committee (TVDRC) → General Secretariat of Zakat, Tax and Customs Committees → Court of Appeal. Out of scope (R-SA-CT-6) — escalate.

### 6.6 Record Retention

- **Record retention** — Retain books, records, and supporting documentation for at least 10 years from the end of the fiscal year (verify against the current ZATCA guidance and Implementing Regulations — retention may differ for specific document classes).

## Section 7 — Conservative Defaults Summary

**Conservative Defaults Summary table**

| Item | Default |
| --- | --- |
| Shareholder nationality unverified | Treat as foreign (CIT applies) |
| Sector unclear | Standard 20% (not 30% gas, not 50–85% oil) |
| Activity boundary unclear | Default 20%, flag — do not apply elevated rates |
| Mixed-entity ownership | Use CR snapshot at FYE; flag mid-year changes |
| Loss carry-forward | Indefinite, **always cap offset at 25% of annual taxable income** (Article 21) |
| Interest deduction | **Always cap at 50% of EBITDA** (Article 12); track disallowed interest c/f |
| TP documentation | Apply MF / LF / CbCR at SAR 750M consolidated revenue threshold |
| Pillar Two / DMTT | Mark **TBC**; do not compute top-up until enactment confirmed |
| Advance instalments | Pay on prior-year basis unless formal ZATCA-approved reduction |
| Filing deadline | **120 days from FYE — never assume extension** |
| Group consolidation | Standalone unless documented share-deal structure |
| Penalty headline | 5%/month, capped at 25% |
| Record retention | 10 years from FYE (verify) |
| Treaty positions / PE | Escalate; do not apply treaty relief without reviewer sign-off |
| FA / Royal-Decree change uncertain | Mark **TBC** and flag for reviewer |

## Section 8 — Sources

**Primary Legislation**

- **Income Tax Law (ITL)** — Royal Decree No. **M/1** dated **15/1/1425H (6 March 2004)**.
  - Article 1–4 — taxable persons, residency, permanent establishment.
  - Article 5 — separate-enterprise principle for PEs.
  - Article 6 — gross income.
  - Article 7 — rates (a) 20% standard, (b) 30% natural gas, (c) 50%–85% oil and other hydrocarbons.
  - Articles 8–17 — allowable deductions.
  - Article 12 — interest deduction limitation (50% of EBITDA).
  - Article 13 — bad debts, donations, and specific deduction conditions.
  - Article 17 — depreciation (declining-balance per asset class).
  - Article 21 — loss carry-forward (indefinite, capped at 25% of annual taxable income).
  - Article 60 — advance tax instalments.
  - Articles 68–69 — withholding tax on payments to non-residents.
- **Implementing Regulations to the ITL** — detailed procedural and computational rules issued by ministerial decision.
- **Subsequent Royal Decrees and Ministerial Decisions** amending the ITL and Implementing Regulations (verify the current consolidated text).

**Subordinate Legislation and ZATCA Instruments**

- **Transfer Pricing Bylaws (2019)** — BEPS Action 13 aligned; MF / LF / CbCR thresholds at SAR 750M.
- **ZATCA Circulars and Guides** — including TP guide, withholding-tax guide, and sectoral guides.
- **Pillar Two / Domestic Minimum Top-up Tax instruments** — **TBC** for 2025–2026 enactment; verify the gazetted Royal Decree and ZATCA implementing rules.

**Authority and Platform**

- **Zakat, Tax and Customs Authority (ZATCA)** — zatca.gov.sa.
- **ZATCA portal** — annual return filing, advance instalments, WHT filings, TP disclosure.
- **General Secretariat of Zakat, Tax and Customs Committees** — disputes and appeals (out of scope).

**International Instruments**

- **OECD Model Tax Convention** and **KSA bilateral tax treaties** — for treaty-based PE and WHT analysis (escalate per R-SA-CT-10).
- **OECD BEPS Action 13** — Master File / Local File / Country-by-Country Reporting standard.
- **OECD Pillar Two GloBE Rules** — informing the KSA DMTT track (TBC).

## PROHIBITIONS

- NEVER apply Saudi CIT to Saudi or GCC nationals' share — that share is subject to **Zakat** (see `sa-zakat`).
- NEVER apply the standard 20% rate to taxable income from **natural gas investment** (30%) or **oil and other hydrocarbons** (tiered 50%–85%) — but equally, **do not apply elevated rates without confirmation of activity classification** (default to 20% with a flag).
- NEVER omit the **Article 21 25% annual cap** on loss carry-forward offset — losses are indefinite but cannot eliminate more than 25% of any year's taxable income.
- NEVER deduct interest in excess of **50% of EBITDA** under Article 12 — track the disallowed amount as a carry-forward.
- NEVER produce a Saudi consolidated/group return — Saudi tax law does not generally permit it (R-SA-CT-3).
- NEVER apply a Regional Headquarters (RHQ), ILBZ, NEOM, KAEC, or other zone incentive without specialist verification (R-SA-CT-4).
- NEVER assume a tax treaty modifies the PE or WHT outcome without reviewer sign-off (R-SA-CT-10).
- NEVER compute Pillar Two / DMTT amounts until the gazetted KSA instrument is verified — mark **TBC** in all interim outputs.
- NEVER apply CbCR / MF / LF thresholds inconsistently — the SAR 750M consolidated-revenue threshold is the trigger.
- NEVER advise late filing — the **120-day** deadline is strict and the penalty is **5% per month capped at 25%**.
- NEVER advise skipping or reducing advance instalments without formal ZATCA approval — default surcharge applies.
- NEVER conflate the **CIT taxable income** and the **Zakat base** in a mixed entity — they are computed under different rules.
- NEVER ignore the Commercial Registration nationality breakdown — it drives the CIT/Zakat split in a mixed entity.
- NEVER produce figures as definitive — always label as estimates pending reviewer sign-off by a SOCPA-licensed tax professional.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Saudi tax professional (SOCPA member or ZATCA-recognised tax adviser) before filing or acting upon. Pillar Two / DMTT specifics flagged as **TBC** must be verified against the gazetted Royal Decree and ZATCA implementing instruments before reliance. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## OpenAccountants footer

*OpenAccountants — open-source accounting skills for AI*

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
