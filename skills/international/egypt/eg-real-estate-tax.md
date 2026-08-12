---
name: eg-real-estate-tax
description: Use this skill whenever asked about Egyptian real estate tax (ضريبة العقارات) under Law 196/2008 — annual rental value tax on owned property in Egypt. Trigger on "Egypt real estate tax", "ضريبة العقارات", "real estate levy Egypt", "annual rental value tax", or any property-tax compliance question for Egyptian owners/landlords.
version: 0.1
jurisdiction: EG
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on: - workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt Real Estate Tax (ضريبة العقارات) Skill v0.1

## Egypt Real Estate Tax (ضريبة العقارات) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction: EG` in frontmatter even when the folder path implies it. Sync to openaccountants.com skips files without a resolvable jurisdiction.

This skill covers Egyptian real estate tax (ضريبة العقارات المبنية) under **Law No. 196 of 2008** (the Unified Real Estate Tax Law), as amended by **Law No. 117 of 2014** and **Law No. 3 of 2026**. The AI must reply in the user's language (English or Arabic / Egyptian Arabic) and may use the native tax terms shown throughout.

> **Currency note:** all figures are in Egyptian Pounds (EGP / ج.م).
> **YMYL — verify before relying.** Egyptian property tax thresholds and exemptions were amended in 2014 and again in 2026 (Law 3/2026). Where this skill says "verify current value," re-confirm against the Real Estate Taxation Authority (RETA), the Egyptian Tax Authority (eta.gov.eg), PwC Worldwide Tax Summaries (taxsummaries.pwc.com/egypt), or a Big-4 alert before filing.

## What this file is

**This file is a content skill that loads on top of the universal workflow base** (`workflow-base`). It provides Egypt-specific real estate tax rates, exemptions, valuation mechanics, filing procedures, and the critical CIT non-deductibility rule.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date, and reflects the March 2026 amendments (Law 3/2026) where noted.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs any filing. The skill produces working papers and a brief, not a filing.

## Section 1 — Scope statement

This skill covers:

- The annual real estate tax (ضريبة العقارات المبنية) imposed on built property in Egypt
- Tax base: annual rental value (ARV) as determined by government assessors
- Tax rates and deduction mechanics for residential and non-residential property
- Exemptions: residential threshold, non-residential threshold, specific property types
- Filing and payment: annual declaration to RETA (not ETA e-filing portal)
- Collection: administered by municipalities via the Real Estate Taxation Authority (RETA)
- **The CIT non-deductibility rule**: real estate tax is NOT deductible for corporate income tax purposes
- March 2026 amendments (Law 3/2026): updated thresholds, digital filing, penalty waivers
- Real estate transactions tax (2.5% on property transfers) — briefly, for context
- Real estate wealth tax on rental income (10%–27.5% schedule) — briefly, for context

This skill does NOT cover:

- Corporate income tax (CIT) — see `eg-corporate-tax`
- Personal income tax on rental income — see `eg-income-tax`
- VAT — see `egypt-vat`
- Stamp duty on property registration — see `eg-stamp-duty`
- Property registration procedures (Law 114/1946) — legal, not tax
- Transfer pricing — see `eg-transfer-pricing`

## Section 2 — Legal framework

**Legal framework**  _(Law 196/2008; Law 117/2014; Law 3/2026; Law 91/2005 Art 47)_

| Item | Rule | Source |
| --- | --- | --- |
| **Primary law** | Unified Real Estate Tax Law — imposes annual tax on built real estate | Law 196/2008 |
| **Amendments** | Raised residential exemption threshold from EGP 6,000 to EGP 24,000; broadened commercial exemption | Law 117/2014 |
| **Latest amendments** | Raised exemption threshold to EGP 100,000; 25% timely-payment discount; penalty waiver; digital filing; centralized declaration submission | Law 3/2026 (March 2026) |
| **Regulatory authority** | Real Estate Taxation Authority (RETA — مصلحة الضرائب العقارية), known as "Maamouria" (المعمورة) | Law 196/2008 Art 1 |
| **Collection** | By municipalities / governorate-level RETA offices (44 offices nationwide) — NOT the ETA e-filing portal | Law 196/2008 Art 38 |
| **Related transfer tax** | 2.5% of property sale value — due on transfer | Law 196/2008 Art 40 |
| **Related wealth tax** | On rental income: 10%–27.5% progressive schedule — separate from the annual property tax | Law 91/2005 Art 47 |

> **Key distinction.** The real estate tax is an annual tax on property OWNERSHIP (not income). The real estate wealth tax is a tax on rental INCOME. They are separate levies with separate filing mechanisms. The transactions tax is a one-time tax on property TRANSFERS. This skill focuses on the annual real estate tax.

## Section 3 — Tax base and valuation

### 3.1 — Annual Rental Value (ARV)

The tax base is the **Annual Rental Value (ARV)** of the property as determined by government assessors — NOT the market purchase price and NOT the actual rent (if leased).

**Annual Rental Value (ARV)**  _(Law 196/2008 Art 4–7; Art 8; Art 5; Art 2; Art 18; Law 3/2026)_

| Item | Rule | Source |
| --- | --- | --- |
| **Basis** | Assessed annual rental value set by RETA valuation committees | Law 196/2008 Art 4–7 |
| **Valuation cycle** | Every 5 years (revaluation of all properties) | Law 196/2008 Art 8 |
| **Factors** | Location, condition, size, usage type, associated facilities | Law 196/2008 Art 5 |
| **Vacant vs let** | Tax applies whether the property is let, owner-occupied, or vacant | Law 196/2008 Art 2 |
| **Dispute/appeal** | Owner may appeal the assessed ARV within 60 days of notification; appeals can now be filed electronically (per 2026 amendment) | Law 196/2008 Art 18; Law 3/2026 |

### 3.2 — Deductions before applying the rate

- **Deductions before applying the rate** — Before the 10% tax rate is applied, two deductions are made: 1. **Maintenance/management deduction** — a statutory allowance for maintenance and management costs: - Residential property: deduct **30%** of gross ARV - Non-residential property: deduct **32%** of gross ARV 2. **Exemption deduction** — deduct the statutory exemption amount: - EGP 24,000 (pre-2026) / EGP 100,000 (post-2026, Law 3/2026) per residential unit - EGP 1,200 for non-residential units  _(Law 3/2026)_

> **The 30%/32% deduction is automatic** — no receipts or proof of actual expenses required. It is built into the statute.

### 3.3 — Tax rate

**Tax rate**  _(Law 196/2008 Art 12)_

| Property type | Tax rate | Deduction | Statutory exemption |
| --- | --- | --- | --- |
| **Residential** | 10% of net ARV | 30% of gross ARV | EGP 24,000 (pre-2026) / EGP 100,000 (Law 3/2026) |
| **Non-residential** (commercial, industrial, administrative) | 10% of net ARV | 32% of gross ARV | EGP 1,200 |

> **Note on non-residential rate.** Law 196/2008 Art 12 sets the rate at 10% for ALL property types. Some secondary sources reference a 20% rate for non-residential — this reflects earlier draft proposals and/or the wealth tax on rental income, NOT the annual property tax. The statutory annual rate is 10% across the board.

## Section 4 — Worked examples

### Example 1: Residential property (pre-2026 threshold)

- Property: Cairo apartment
- Gross ARV: EGP 120,000/year
- Maintenance deduction (30%): EGP 36,000
- Net ARV: 120,000 – 36,000 = EGP 84,000
- Exemption deduction: EGP 24,000
- Taxable base: 84,000 – 24,000 = EGP 60,000
- Tax at 10%: **EGP 6,000/year**

### Example 2: Residential property (post-2026 threshold, Law 3/2026)

- Property: Giza apartment
- Gross ARV: EGP 120,000/year
- Maintenance deduction (30%): EGP 36,000
- Net ARV: 120,000 – 36,000 = EGP 84,000
- Exemption deduction (Law 3/2026): EGP 100,000
- Taxable base: 84,000 – 100,000 = EGP 0 (fully exempt under new threshold)
- Tax at 10%: **EGP 0/year**

### Example 3: Non-residential property

- Property: Commercial shop, downtown Cairo
- Gross ARV: EGP 200,000/year
- Maintenance deduction (32%): EGP 64,000
- Net ARV: 200,000 – 64,000 = EGP 136,000
- Exemption deduction: EGP 1,200
- Taxable base: 136,000 – 1,200 = EGP 134,800
- Tax at 10%: **EGP 13,480/year**

### Example 4: Below-threshold residential

- Property: Small residential unit
- Gross ARV: EGP 24,000/year
- Maintenance deduction (30%): EGP 7,200
- Net ARV: 24,000 – 7,200 = EGP 16,800
- Net ARV is below exemption threshold → **fully exempt, no tax due**

## Section 5 — Exemptions

### 5.1 — Threshold exemptions (annual rental value)

**Threshold exemptions (annual rental value)**  _(Law 196/2008 Art 10; Law 3/2026)_

| Property type | Exemption threshold | Source |
| --- | --- | --- |
| Residential | ARV ≤ EGP 24,000 (pre-2026) / ≤ EGP 100,000 (Law 3/2026) | Law 196/2008 Art 10; Law 3/2026 |
| Non-residential | ARV ≤ EGP 1,200 | Law 196/2008 Art 10 |

### 5.2 — Property-type exemptions (fully non-taxable)

- **Property-type exemptions (fully non-taxable)** — The following properties are NOT subject to the real estate tax at all: - **State-owned properties** (unless used for commercial purposes) - **Places of worship** — mosques, churches, and registered religious institutions - **Public schools, universities, and hospitals** (government and private) - **Registered charitable organisations** and nonprofit entities - **Properties owned by foreign governments** used for diplomatic purposes - **Under-construction properties** — not taxed until fully built and registered - **Agricultural land** — not subject to the built-property tax (separate agricultural land tax regime under Law 113/1939)  _(Law 113/1939)_

### 5.3 — Partial/conditional exemptions

- **Partial/conditional exemptions** — - **Newly constructed properties**: may qualify for a 5-year exemption from completion (certain conditions apply per Law 196/2008 Art 11) - **Owner-occupied sole residence**: exempt if it is the taxpayer's only property AND below the threshold (per Law 117/2014 amendments, the exemption applies to the aggregated value of all residential properties owned) - **Heritage/registered historic buildings**: may negotiate deductions during restoration - **Vacant properties**: unrented for 6+ months may qualify for partial relief (governorate discretion)  _(Law 196/2008 Art 11; Law 117/2014)_

### 5.4 — 2026 amendments to exemptions (Law 3/2026)

**2026 amendments to exemptions (Law 3/2026)**  _(Law 3/2026)_

| Item | Old rule (pre-2026) | New rule (Law 3/2026) |
| --- | --- | --- |
| Residential exemption threshold | EGP 24,000 ARV | EGP 100,000 ARV |
| Total exemption value | EGP 2,000,000 (aggregated property value) | EGP 8,000,000 (aggregated property value) |
| Declaration submission | Separate submission to each RETA office | Single submission to any RETA office |
| Late payment penalties | Accumulating | Cancelled (blanket waiver) |
| Timely-payment incentive | None | 25% discount for on-time payment |
| Appeal filing | In person at local RETA office | Electronic filing available |
| Dispute settlement | 100% of disputed tax | 70% of disputed tax |
| Tax effect date | Retroactive from property registration | From date of declaration submission |

Key changes introduced in March 2026:

## Section 6 — Filing and payment

**Filing and payment**  _(Law 196/2008; Law 3/2026)_

| Item | Rule | Source |
| --- | --- | --- |
| **Who must file** | All property owners (individuals, companies, associations, public bodies) owning built real estate in Egypt | Law 196/2008 Art 2 |
| **Filing method** | Annual declaration submitted to RETA office (Maamouria) — NOT the ETA e-filing portal | Law 196/2008 Art 25 |
| **Digital filing** | Gradually transitioning to digital platforms (per Law 3/2026) | Law 3/2026 |
| **Payment frequency** | Annual — payable in one installment or as notified by RETA | Law 196/2008 Art 30 |
| **Payment location** | RETA offices or designated banks/post offices; digital channels being introduced | Law 196/2008 Art 30 |
| **Timely-payment discount** | 25% discount on tax value for on-time payment (post-2026) | Law 3/2026 |
| **Late payment penalty** | Previously accumulating — cancelled under Law 3/2026 blanket waiver | Law 3/2026 |
| **Revaluation** | Every 5 years by RETA valuation committees | Law 196/2008 Art 8 |
| **Appeal deadline** | 60 days from notification of assessed ARV | Law 196/2008 Art 18 |

> **Filing is NOT automated.** Exemptions are not automatic — owners must proactively file a declaration and submit proof of eligibility (title deed, rental contract, valuation report, proof of eligibility for exemption category).

> **RETA ≠ ETA.** The Real Estate Taxation Authority (RETA / المعمورة) is a separate authority from the Egyptian Tax Authority (ETA). Real estate tax declarations go to RETA offices, NOT the ETA online portal. There are 44 RETA branch offices across Egypt.

## Section 7 — CIT non-deductibility (critical audit issue)

> **This is the single most important compliance point for corporate taxpayers.**

**CIT non-deductibility**  _(Law 91/2005 Art 23)_

| Item | Rule | Source |
| --- | --- | --- |
| **Deductibility for CIT** | **NOT deductible** — real estate tax is a non-business tax and is disallowed as a deduction from taxable profits | Law 91/2005 Art 23 |
| **Mechanism** | Real estate tax is added back to accounting profit in the CIT return as a non-deductible expense | Law 91/2005 Art 23 |
| **Rationale** | Art 23 disallows "taxes and duties" that are not business taxes (income tax, VAT, customs). Real estate tax is a property tax on ownership — not a cost of generating business income |  |
| **Exception** | REAL ESTATE HELD FOR RE-SALE (inventory/stock) may qualify for different treatment — verify with advisor |  |
| **Audit risk** | High — many companies incorrectly deduct real estate tax on their business premises. This is a common audit finding by ETA |  |

### Practical guidance for the reviewer

When preparing or reviewing a CIT return:

1. **Check the trial balance** for real estate tax expense accounts
2. **Add back** the full amount of real estate tax in the CIT reconciliation (Form 10 —Schedule of adjustments)
3. **Document** the add-back with the RETA receipt as supporting evidence
4. If the property is held for re-sale (developer), seek specialist advice on classification
5. Real estate TRANSACTIONS tax (2.5% on purchase) is also generally NOT deductible — it is a capital cost of acquiring the asset

> **Note.** This non-deductibility is specific to the annual real estate tax. Rental INCOME taxed under the wealth tax regime (Art 47, Law 91/2005) is a separate matter — that IS the income tax itself, not a deduction question.

## Section 8 — Real estate transactions tax (context only)

**Real estate transactions tax (context only)**  _(Law 196/2008 Art 40; Art 41)_

| Item | Rule | Source |
| --- | --- | --- |
| **Rate** | 2.5% of the property's sale value | Law 196/2008 Art 40 |
| **Timing** | Due on transfer (registration) | Law 196/2008 Art 40 |
| **Exemptions** | Family transactions, inheritance transfers, some investment-related sales | Law 196/2008 Art 41 |
| **Administered by** | RETA — separate from annual property tax | Law 196/2008 |

This is a one-time transfer tax, NOT the annual property tax. See the property registration process (Law 114/1946) for the registration mechanics.

## Section 9 — Interaction with other Egypt taxes

**Interaction with other Egypt taxes**  _(eg-corporate-tax; eg-income-tax; egypt-vat; eg-stamp-duty; eg-transfer-pricing)_

| Tax | Relationship | Skill |
| --- | --- | --- |
| **CIT (corporate income tax)** | Real estate tax is NOT deductible — must add back in CIT reconciliation | `eg-corporate-tax` |
| **Personal income tax** | Real estate wealth tax on rental income (10%–27.5%) is collected via the income tax return | `eg-income-tax` |
| **VAT** | No interaction — property tax is not a VAT input | `egypt-vat` |
| **Stamp duty** | Separate levy on property registration documents | `eg-stamp-duty` |
| **Transfer pricing** | No direct interaction | `eg-transfer-pricing` |

## Section 10 — Sources and verification

**Sources and verification**  _(Law 196/2008; Law 117/2014; Law 3/2026; Law 91/2005)_

| Source | Reference | URL |
| --- | --- | --- |
| **Law 196/2008** | Unified Real Estate Tax Law (primary statute) | — |
| **Law 117/2014** | Amendments to Law 196/2008 (exemption threshold increases) | — |
| **Law 3/2026** | March 2026 amendments (exemption threshold, digital filing, penalty waiver) | — |
| **Law 91/2005 Art 23** | CIT non-deductibility of non-business taxes | — |
| **Law 91/2005 Art 47** | Real estate wealth tax on rental income | — |
| **PwC Worldwide Tax Summaries** | Egypt — property tax | taxsummaries.pwc.com/egypt |
| **Andersen Egypt** | Real Estate Tax Laws in Egypt (English law translation) | eg.andersen.com/real-estate-tax-laws |
| **RETA** | Real Estate Taxation Authority (44 offices nationwide) | — |

> **Verify before relying.** Egyptian property tax thresholds and exemption amounts change frequently. The 2026 amendments (Law 3/2026) significantly raised thresholds and introduced new facilitations. Always confirm current values against the official sources above before filing.

## Self-check

Before delivering any real estate tax computation or advisory to the reviewer:

- [ ] Did you use the ARV (assessed rental value), NOT the market value or actual rent?
- [ ] Did you apply the correct deduction (30% residential, 32% non-residential)?
- [ ] Did you apply the correct exemption threshold (EGP 24,000 or EGP 100,000 post-2026 for residential; EGP 1,200 for non-residential)?
- [ ] Did you apply the 10% rate to the NET ARV after both deductions?
- [ ] Did you check whether the property qualifies for a property-type exemption (state, religious, hospital, school, charity)?
- [ ] If the client is a company — did you flag the CIT non-deductibility add-back?
- [ ] Did you verify the current exemption threshold against the latest law (Law 3/2026)?
- [ ] Did you confirm filing is with RETA, not the ETA e-filing portal?
- [ ] Did you check whether the 25% timely-payment discount (Law 3/2026) applies?
- [ ] Where any figure was uncertain, did you mark it "verify before relying" and cite the source?

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
