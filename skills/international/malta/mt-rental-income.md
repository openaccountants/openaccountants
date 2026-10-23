---
name: mt-rental-income
description: 'Use this skill whenever asked about Malta rental income taxation. Trigger on phrases like "rental income Malta", "letting property Malta", "15% final withholding tax", "Article 31D", "TA24 rental", "property letting", "kiri", "rent received", "landlord tax Malta", "Airbnb Malta tax", "short-term rental Malta", "non-resident landlord Malta", "rental declaration CFR", "FWS rental", or any question about computing, filing, or optimising tax on rental income from Maltese immovable property. Covers both the Final Withholding System (15% flat) and the normal progressive system, non-resident landlords, short-term letting, VAT interaction, and property transfer tax. Basis year 2026: the 15% final tax under Article 31D, the L.N. 100 of 1993 deductions (interest, ground rent, licence fees and the 20% further deduction) under the normal system, the 2026 single rate bands, and the TA24 deadline of 30 April. ALWAYS read this skill before touching any Malta rental income work.'
version: 1.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - malta-income-tax
category: international
tier: 2
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MT Rental Income

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

Tax year: basis year 2026, return and TA24 due in 2027. Rate tables are in [malta-income-tax](malta-income-tax.md); sales of property are in [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md); [how-to-account-for-rental-income-in-malta](how-to-account-for-rental-income-in-malta.md) covers the bookkeeping side.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Tax | Income Tax on Rental Income (Immovable Property) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act, Chapter 123, Article 31D |
| Supporting legislation | ITA Article 4(1)(a) and 4(1)(e); Income Tax Management Act (Chapter 372); Deductions (Expenses in Respect of Immovable Property) Rules, L.N. 107 of 1978 as amended by L.N. 50 of 1983 and L.N. 100 of 1993 |
| Tax authority | Commissioner for Tax and Customs / Malta Tax and Customs Administration (MTCA) |
| Filing portal | MTCA online services (myTax) |
| Filing deadline (FWS) | 30 April of the year following the basis year |
| Filing deadline (normal) | 30 June of the year following the basis year (via annual tax return); MTCA's Tax Return Cycle page gives 31 July for online submission, with tax still due by 30 June |
| Review status | Source-cited draft: not reviewed by an accountant |
| Skill version | 1.1 |

### Two Systems for Taxing Rental Income

**Two Systems for Taxing Rental Income**

| Feature | Final Withholding System (FWS) | Normal Progressive System |
| --- | --- | --- |
| Tax rate | 15% flat on gross rent | Progressive rates (0%--35%) on net rent |
| Deductions | NONE: no expenses, set-offs, or refunds | Interest, ground rent, licence fees, plus a 20% further deduction that replaces all other expenses (L.N. 100 of 1993) |
| Filing form | TA24 | Annual income tax return |
| Deadline | 30 April following year | 30 June following year |
| Availability | Residents and non-residents | Residents and non-residents |
| Entities | Individuals and bodies corporate | Individuals and bodies corporate |
| Related-party lets | NOT available | Must use this system |
| Election | Annual choice: can change each year | Default if FWS not elected |
| Mixed election | NOT allowed: the option covers all qualifying rental income from all tenements for the year | N/A |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown system choice (FWS vs normal) | STOP: ask client which system they elect |
| Unknown whether the tenant is a related party (a company or other body of persons more than 25% owned or controlled by the landlord, or by the same persons) | Treat as related party (FWS blocked) |
| Unknown property type (residential vs commercial) | STOP: ask client |
| Unknown residency status of landlord | STOP: affects withholding obligations |
| Unknown whether furnished or unfurnished | Treat as unfurnished (no furniture premium) |
| Unknown rental period (short-term vs long-term) | STOP: VAT treatment depends on this |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- total gross rental income for the year, election for FWS or normal system, confirmation of whether the tenant is a related party.

**Recommended** -- lease agreement(s), rental income bank receipts, property purchase documentation (for normal system deductions), details of any letting agent commissions, insurance and maintenance invoices.

**Ideal** -- complete rental income schedule per property, bank statements showing rental receipts, itemised expenses with receipts (normal system only), confirmation of property type (residential/commercial), and dates of letting periods.

### Refusal Catalogue

- **R-MTR-1 -- System election unknown**: The client must confirm whether they elect the 15% Final Withholding System or the normal progressive system. This affects all calculations. Cannot proceed without this election.  _(R-MTR-1)_
- **R-MTR-2 -- Related-party letting**: Rent from related parties cannot benefit from the 15% final tax. Under Article 31D(8)(a)(ii), as quoted by MTCA, a body of persons is related to an individual if that individual owns or controls more than 25% of it, directly or indirectly; two bodies of persons are related if the same persons own or control more than 25% of each. If the letting is between related parties, the normal system must be used. Confirm the relationship before proceeding.  _(R-MTR-2; Article 31D)_
- **R-MTR-3 -- Property transfers / capital gains**: Property disposals and transfer tax computations are outside the scope of this skill. Escalate to a warranted accountant.  _(R-MTR-3)_
- **R-MTR-4 -- Complex non-resident structures**: Non-resident landlords with complex holding structures, trusts, or nominee arrangements require specialist advice. Escalate to a warranted accountant.  _(R-MTR-4)_
- **R-MTR-5 -- Mixed election attempted**: A taxpayer cannot elect FWS for part of their rental income and the normal system for another part. All rental income must be under one system for any given year.  _(R-MTR-5)_

## Section 3 -- Final Withholding System (FWS) -- Computation Rules

### 3.1 Core Rules (Article 31D)

- **FWS core rules**: 1. The tax is 15% of **gross rental income received** in the basis year 2. Gross means gross: no deductions of any kind (repairs, insurance, management fees, mortgage interest, depreciation: NOTHING) 3. The tax is **final**: no refunds, no set-offs, no credits against other tax, no carry-forward of losses 4. Available to both residents and non-residents 5. Available to both individuals and companies; a Malta company allocates the profits to its final tax account 6. **NOT available** for rent from related parties 7. Rent includes ground rent from an emphyteutical concession; "tenement" covers all immovable property, including land and roof tops; recharges of common costs are not rent for Article 31D (MTCA guidance note)  _(Article 31D)_

### 3.2 Calculation

- **FWS tax calculation**: Tax = Gross rental income × 15% There is no exempt band, no personal allowance applicable, and no threshold below which FWS is unavailable.  _(Article 31D)_

### 3.3 Filing and Payment

**Filing and Payment**

| Step | Detail |
| --- | --- |
| Form | TA24, online through MTCA (residents and non-residents/companies have separate entry points) or manually |
| Deadline | 30 April of the following year |
| Payment | Accompanies the form |
| Rental income not declared in annual return | Correct for individuals: FWS rent is not declared in the tax return |

### 3.4 FWS Historical Coverage

**FWS Historical Coverage**

| Property type | Available from |
| --- | --- |
| Residential property | 1 January 2014 |
| Commercial property | 1 January 2016 |

## Section 4 -- Normal Progressive System -- Computation Rules

### 4.1 Core Rules

- **Normal system core rule**: If FWS is not elected, rental income is declared in the annual tax return and taxed at progressive rates after deducting allowable expenses.

### 4.2 Allowable Deductions (Normal System Only)

For rent from property held as an investment (Article 4(1)(e) ITA), L.N. 100 of 1993 limits the deductions to:

| Deduction | Notes |
| --- | --- |
| (a) Interest | Only on a loan that relates to the property producing the rent |
| (b) Rent, ground rent or similar burden | Paid by the landlord on the property |
| (c) Licence fees | Paid under the Guest Houses and Holiday Furnished Premises Act |
| (d) Further deduction | 20% of the gross rent less (b) and (c). Not allowed on income from emphyteusis |

The 20% further deduction replaces every other expense. Repairs, insurance, agent fees, condominium fees, accountancy and similar costs are NOT deducted on top of it. Round deductions up to the nearest euro. (Version 1.0 of this skill listed those costs as deductible; that was wrong.)

### 4.3 Per-Property Rule and Losses

Each property is a separate source. If deductions exceed the rent on one property, that property gives NIL income. A loss on one property cannot be set against another property, against other income, or carried forward.

Rent that forms part of a trade (Article 4(1)(a)) is computed as business income; that is outside this section.

### 4.4 Tax Rates (Normal System)

- **Tax Rates (Normal System)**: Progressive rates apply per the Income Tax Act rate tables. Net rental income is added to all other income and taxed at the marginal rate. For 2026 the single rates are 0% to EUR 12,000, 15% to EUR 16,000, 25% to EUR 60,000 and 35% above (MTCA, Tax Rates 2026). See [malta-income-tax](malta-income-tax.md) for the married and parent tables. Non-residents who opt for the normal system are taxed at the non-resident rates.  _(Income Tax Act rate tables)_

### 4.5 When Normal System May Be Preferable

- **Large loan interest or ground rent**: these come off before tax, on top of the 20% further deduction
- **Low marginal rate**: at 0% or 15%, the tax on net rent is usually below 15% of gross rent
- **Losses**: the normal system gives NIL income on a loss-making property, but the loss cannot be used elsewhere

## Section 5 -- Transaction Pattern Library

### 5.1 Income Patterns (Credits on Bank Statement)

**Income Patterns (Credits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KIRI, RENT RECEIVED, RENTAL PAYMENT | Rental income | Gross amount = FWS base; normal system deducts interest, ground rent, licence fees and the 20% |
| LETTING AGENT, PROPERTY MANAGER + DEPOSIT | Rental income | Agent collects on behalf: full gross is landlord's income |
| AIRBNB PAYOUT, BOOKING.COM PAYOUT | Rental income | Platform rental: verify if short-term (VAT implications) |
| SECURITY DEPOSIT, DEPOSIT RECEIVED | EXCLUDE if refundable | Not income unless forfeited |
| TENANT REIMBURSEMENT, UTILITY REFUND, COMMON COSTS RECHARGE | EXCLUDE | Recharges of common costs are not rent for Article 31D |

### 5.2 Expense Patterns (Normal System Only -- Debits)

| Pattern | Category | Treatment |
| --- | --- | --- |
| MORTGAGE INTEREST, LOAN INTEREST, BOV LOAN | Interest expense | Deductible under normal system if the loan relates to the let property; NOT under FWS |
| GROUND RENT, CENS | Ground rent | Deductible under normal system |
| MTA LICENCE, LICENCE FEE | Licence fee | Deductible under normal system |
| INSURANCE, REPAIRS, AGENT COMMISSION, CONDOMINIUM, FURNITURE | Other costs | Covered by the 20% further deduction; not deducted separately |

### 5.3 Exclusions

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MORTGAGE REPAYMENT, LOAN PRINCIPAL | EXCLUDE | Capital repayment, not expense |
| PROPERTY PURCHASE, NOTARY (acquisition) | EXCLUDE | Capital cost: relevant only to transfer tax or CGT |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Not rental transaction |
| STAMP DUTY, PROPERTY TRANSFER TAX | EXCLUDE | Capital cost at acquisition |

## Section 6 -- Special Topics

### 6.1 Non-Resident Landlord Rules

- **Non-Resident Landlord Rules**: - Non-residents can elect FWS (15% on gross) just like residents - Non-residents can alternatively declare the rent in a return, take the L.N. 100 of 1993 deductions and pay at the non-resident rates - Non-domiciled, non-resident landlords: Malta rental income is Malta-source and always taxable in Malta regardless of domicile or remittance - Double tax treaty relief may apply: landlord should check treaty with country of residence (Article 6 OECD Model typically gives primary taxing rights to the country where the property is situated)  _(Article 6 OECD Model)_

### 6.2 Short-Term Rental / Airbnb Treatment

- **Short-Term Rental / Airbnb Treatment**: - Short-term tourist accommodation (less than 30 days per booking) requires a Malta Tourism Authority (MTA) licence - Income from short-term lets is still rental income and can be taxed under FWS (15%) or normal system - **VAT treatment**: letting that needs a licence under the Malta Travel and Tourism Services Act is outside the VAT exemption; an Article 10 registered landlord charges 7% (8th Schedule VAT Act). This is separate from income tax - If the landlord is VAT-registered for short-term letting: VAT collected is NOT income; net of VAT is the rental income for FWS/normal system - Platform fees (Airbnb service fee, Booking.com commission) are deducted by the platform before payout: the gross rental income for tax purposes is the amount **before** platform deductions (method carried from version 1.0; not re-checked against an MTCA source)

### 6.3 Property Transfer Tax (on Disposal)

**Property Transfer Tax (on Disposal)**

Out of scope here; see [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md). Headline rates from the MTCA FAQ for orientation only:

| Scenario | Final WHT Rate |
| --- | --- |
| General property transfer | 8% of transfer value |
| Property acquired before 1 January 2004 | 10% of transfer value |
| Property not part of a project, transferred within 5 years of acquisition (conditions apply) | 5% of transfer value |
| Property in Urban Conservation Area, restored under a permit applied for on or after 1 January 2015 | 5% of transfer value |
| Sole ordinary residence declared on acquisition, sold within 3 years, no other residential property owned | 2% of transfer value |
| Own residence owned and occupied for at least 3 consecutive years, sold within 12 months of vacating | Exempt |

### 6.4 Furnished vs Unfurnished

- **Furnished vs Unfurnished**: - FWS: no distinction, 15% on gross regardless - Normal system (Article 4(1)(e)): no separate deduction for furniture; the 20% further deduction covers it - A person who would have claimed wear and tear and opts for the 15% is deemed to have claimed it for any later balancing charge (MTCA guidance note) - Furnished premium (if charged): included in gross rental income

### 6.5 VAT and Rental Income

**VAT and Rental Income**

| Scenario | VAT Treatment |
| --- | --- |
| Letting of immovable property generally | Exempt without credit (5th Schedule, Part Two, VAT Act) |
| Accommodation that needs a Malta Travel and Tourism Services Act licence | Taxable; 7% where the landlord is Article 10 registered |
| Letting by a limited liability company to an Article 10 registered person for its economic activity | Taxable at 18% |
| Letting for 30 days or less in the course of an economic activity (with the listed exceptions) | Taxable at 18% |
| Parking sites, garages, stores, installed equipment and machinery, safes | Taxable at 18% |

### 6.6 Records and Interest

Records of rent must be kept for 10 years. Interest of 0.6% for every month on tax paid late (MTCA manual on rental income). Provisional tax applies to rent declared in the return; see [mt-estimated-tax](mt-estimated-tax.md). Undeclared rent found on investigation is taxed at 35% of gross rent, plus interest and additional tax, whichever system would have applied (MTCA FAQ 11).

Version 1.0 had a section on a "former EUR 1,200 exemption". No MTCA source for it was found, so it is removed.

## Section 7 -- Worked Examples

### Example 1 -- FWS, Single Residential Property

**Input:** Resident individual receives EUR 12,000 gross rent in 2026 from one apartment let to an unrelated tenant. Elects the 15% final tax. Costs: EUR 2,500 (insurance, repairs, agent fees).

The costs do not matter under the final tax. Tax is 15% of EUR 12,000, so EUR 1,800, paid with the TA24 by 30 April 2027. The rent is not declared in the return.

```oa-check
name: Article 31D 15% on gross rent EUR 12,000 (2026)
inputs:
  gross_rent: 12000
steps:
  - tax: pct(gross_rent, 15)
expected:
  tax: 1800.00
```

### Example 2 -- Normal System, Single, With a Salary

**Input:** Same landlord, EUR 12,000 rent, no ground rent or licence fee, EUR 3,000 interest on the loan that bought the flat. Single, salary EUR 30,000 (chargeable income after the salary's own deductions). Repairs and insurance EUR 1,700.

Under L.N. 100 of 1993 the interest comes off, plus a further 20% of gross rent (no ground rent or licence to subtract first), so EUR 2,400. Repairs and insurance are covered by the 20% and are not deducted again. Net rent is EUR 6,600. Total chargeable income is EUR 36,600, in the 25% band of the 2026 single table (rate times income, less EUR 3,400). Tax with the rent is EUR 5,750; without it, EUR 4,100. The rent adds EUR 1,650, which is EUR 150 less than the EUR 1,800 final tax. The normal system is cheaper here, before the cost of the extra compliance.

```oa-check
name: Normal system, single, salary EUR 30,000, rent EUR 12,000, interest EUR 3,000 (2026)
inputs:
  salary: 30000
  gross_rent: 12000
  interest: 3000
  ground_rent: 0
steps:
  - further_deduction: pct(gross_rent - ground_rent, 20)
  - net_rent: max(0, gross_rent - interest - ground_rent - further_deduction)
  - total_income: salary + net_rent
  - tax_with_rent: total_income * 0.25 - 3400
  - tax_without_rent: salary * 0.25 - 3400
  - extra_tax_normal: tax_with_rent - tax_without_rent
  - tax_fws: pct(gross_rent, 15)
  - saving_normal: tax_fws - extra_tax_normal
expected:
  further_deduction: 2400.00
  net_rent: 6600.00
  total_income: 36600.00
  tax_with_rent: 5750.00
  tax_without_rent: 4100.00
  extra_tax_normal: 1650.00
  tax_fws: 1800.00
  saving_normal: 150.00
```

### Example 3 -- FWS, Non-Resident Landlord

**Input:** UK-resident individual owns apartment in Sliema. Gross rent EUR 18,000.

**Computation:**
```
Tax = EUR 18,000 × 15% = EUR 2,700
```
Non-residents can elect the 15% final tax. Filed via TA24 by 30 April. Rent from Malta property is taxable in Malta. The treaty article and the UK credit are for the landlord's UK adviser to confirm.

### Example 4 -- Short-Term Letting with VAT

**Input:** Landlord holds a Malta Travel and Tourism Services Act licence and is Article 10 VAT registered. Total platform payouts received: EUR 20,000 (net of a 3% host service fee). Gross bookings: EUR 20,619. VAT at 7% is included in the gross accommodation charge.

**Computation:**
```
Gross income before platform fee = EUR 20,619
VAT component (7/107 × EUR 20,619) = EUR 1,349
Net income for tax = EUR 20,619 - EUR 1,349 = EUR 19,270
FWS tax = EUR 19,270 × 15% = EUR 2,891
```
Platform fees are not deducted from the FWS base.

### Example 5 -- Related-Party Let (FWS Blocked)

**Input:** An individual lets an office to a company in which she holds 60% of the shares, for EUR 6,000 a year. No loan, no ground rent.

**Computation:** The company is more than 25% owned by her, so it is a related party under Article 31D and the 15% is not available. Under the normal system the 20% further deduction is EUR 1,200 and net rent is EUR 4,800. If her other income keeps her in the 25% band:
```
Additional tax = EUR 4,800 × 25% = EUR 1,200
```
A let between two individuals in the same family is not caught by the body-of-persons test that MTCA quotes; see "Not yet confirmed" in Sources.

## Section 8 -- Decision Flowchart: FWS vs Normal System

```
1. Is the tenant a RELATED PARTY (a body of persons more than 25% owned or
   controlled by the landlord, or by the same persons)?
   YES → Normal system only (FWS blocked)
   NO → Continue

2. Compute net rent under the normal system:
   gross rent - interest - ground rent - licence fees - 20% of (gross - ground rent - licence fees)

3. Compute the extra tax that net rent causes at the landlord's marginal rate
   (resident or non-resident table).

4. Compare with 15% of gross rent. Choose the lower, for ALL qualifying rent in the year.

ALWAYS compute both options and present to reviewer for confirmation.
```

## Section 9 -- Filing Checklist

### FWS Filing

- [ ] Confirm no rent is from a related party (body of persons more than 25% owned or controlled)
- [ ] Calculate total gross rental income for the basis year
- [ ] Compute 15% tax
- [ ] Complete TA24, online or manually
- [ ] Submit TA24 with payment by 30 April
- [ ] Do NOT include FWS rental income in annual tax return

### Normal System Filing

- [ ] Gather all rental income evidence (lease, bank receipts)
- [ ] Gather loan interest statements, ground rent and licence fee receipts
- [ ] Apply the 20% further deduction per property
- [ ] Compute net rental income per property; a loss is NIL and is not carried anywhere
- [ ] Include in annual tax return under rental income section
- [ ] File by 30 June

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Final Withholding System | ITA Article 31D |
| Residential property FWS | From 1 January 2014 |
| Commercial property FWS | From 1 January 2016 |
| Allowable deductions | Deductions (Expenses in Respect of Immovable Property) Rules, L.N. 107 of 1978 as amended by L.N. 100 of 1993 |
| Property transfer tax | ITA Article 5A |
| Tax rates | ITA Rate Schedules |
| Filing deadlines | ITMA Chapter 372 |
| VAT on letting | VAT Act, 5th Schedule Part Two (exemption) and 8th Schedule (7% on licensed accommodation) |

## PROHIBITIONS

- NEVER apply FWS to related-party lettings
- NEVER deduct expenses under the FWS: the 15% rate applies to GROSS income with zero deductions
- NEVER deduct repairs, insurance or agent fees on top of the 20% further deduction under the normal system
- NEVER set a rental loss against other income or carry it forward
- NEVER allow a mixed election (part FWS, part normal) in the same basis year
- NEVER treat a refundable security deposit as rental income
- NEVER ignore VAT on short-term tourist accommodation
- NEVER present the FWS/normal system comparison as definitive without running both computations
- NEVER file FWS rental income in the annual tax return of an individual: it is declared separately on TA24
- NEVER compute property transfer tax in this skill: use mt-property-transfer-tax-the-sale-immovable

## Ask the Client First

- Is any tenant a company or other body of persons that the landlord (or the same owners) holds more than 25% of?
- Gross rent received in 2026 per property, and whether any of it is ground rent from emphyteusis.
- Interest on loans for each let property, ground rent paid, and any MTA licence fees.
- The landlord's other income and marital or parent status, to find the marginal rate (resident or non-resident).
- Whether any letting needs a tourism licence or is short-term or a garage, for VAT.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| MTCA, Rental Income Taxed at 15%, Article 31D FAQs | https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/rental-income-taxed-at-15----article-31d-of-the-income-tax-act | 2026-10-23 |
| MTCA, Manual on the Taxation of Rental Income (Article 31D and L.N. 100 of 1993) | https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf | 2026-10-23 |
| MTCA, Guidance Note on Article 31D | https://mtca.gov.mt/docs/default-source/documents/mtca-guidance-note-art31d.pdf | 2026-10-23 |
| MTCA, Tax on Rental Income (TA24) | https://mtca.gov.mt/personal-tax/individual/tax-on-rental-income-(ta24) | 2026-10-23 |
| MTCA, Tax Rates for Individuals 2026 | https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 | 2026-10-23 |
| MTCA, Tax Return Cycle | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-10-23 |
| MTCA, New Property Tax System FAQ | https://mtca.gov.mt/personal-tax/property-taxes/faqs/new-property-tax-system---faq | 2026-10-23 |
| MTCA, Budget Measures Implementation Act 2026 overview (no change to rental income tax) | https://mtca.gov.mt/business-tax/legislative-developments/2026 | 2026-10-23 |
| Income Tax Act, Cap. 123 | https://legislation.mt/eli/cap/123/eng | Site unavailable on 2026-10-23 |

Not yet confirmed: the full statutory text of Article 31D(8) (legislation.mt was unavailable), so whether any related-party limb reaches lets between individuals; the MTCA manual's line that gross rent under the 15% is "declared by end of June", which sits against FAQ 5 saying individuals do not declare it in the return; the 31 July online return date for the 2026 basis year; treating platform fees as not deductible from the 15% base; the UK treaty position in Example 3.

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
