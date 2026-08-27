---
name: mt-rental-income
description: Use this skill whenever asked about Malta rental income taxation. Trigger on phrases like "rental income Malta", "letting property Malta", "15% final withholding tax", "Article 31E", "TA24 rental", "property letting", "kiri", "rent received", "landlord tax Malta", "Airbnb Malta tax", "short-term rental Malta", "non-resident landlord Malta", "rental declaration CFR", "FWS rental", or any question about computing, filing, or optimising tax on rental income from Maltese immovable property. Covers both the Final Withholding System (15% flat) and the normal progressive system, non-resident landlords, short-term letting, VAT interaction, and property transfer tax. ALWAYS read this skill before touching any Malta rental income work.
version: 1.0
jurisdiction: MT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - malta-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MT Rental Income

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Tax | Income Tax on Rental Income (Immovable Property) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act, Chapter 123, Article 31E |
| Supporting legislation | ITA Articles 4, 5, 27; Income Tax Management Act (Chapter 372); Legal Notice 99 of 2014 (residential); Legal Notice 158 of 2017 (commercial) |
| Tax authority | Commissioner for Revenue (CFR) / MTCA |
| Filing portal | CFR e-Services (mytax.cfr.gov.mt) |
| Filing deadline (FWS) | 30 April of the year following the basis year |
| Filing deadline (normal) | 30 June of the year following the basis year (via annual tax return) |
| Validated by | Pending — requires sign-off by a Maltese warranted accountant |
| Skill version | 1.0 |

### Two Systems for Taxing Rental Income

**Two Systems for Taxing Rental Income**

| Feature | Final Withholding System (FWS) | Normal Progressive System |
| --- | --- | --- |
| Tax rate | 15% flat on gross rent | Progressive rates (0%--35%) on net rent |
| Deductions | NONE — no expenses, set-offs, or refunds | Full Werbungskosten-style deductions allowed |
| Filing form | TA24 (rental section) | Annual Income Tax Return (TA form) |
| Deadline | 30 April following year | 30 June following year |
| Availability | Residents and non-residents | Residents and non-residents |
| Entities | Individuals and bodies corporate | Individuals and bodies corporate |
| Related-party lets | NOT available | Must use this system |
| Election | Annual choice — can change each year | Default if FWS not elected |
| Mixed election | NOT allowed — all rental income must be under one system | N/A |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown system choice (FWS vs normal) | STOP — ask client which system they elect |
| Unknown whether let is to related party | Treat as related party (FWS blocked) |
| Unknown property type (residential vs commercial) | STOP — ask client |
| Unknown residency status of landlord | STOP — affects withholding obligations |
| Unknown whether furnished or unfurnished | Treat as unfurnished (no furniture premium) |
| Unknown rental period (short-term vs long-term) | STOP — VAT treatment depends on this |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- total gross rental income for the year, election for FWS or normal system, confirmation of whether the tenant is a related party.

**Recommended** -- lease agreement(s), rental income bank receipts, property purchase documentation (for normal system deductions), details of any letting agent commissions, insurance and maintenance invoices.

**Ideal** -- complete rental income schedule per property, bank statements showing rental receipts, itemised expenses with receipts (normal system only), confirmation of property type (residential/commercial), and dates of letting periods.

### Refusal Catalogue

- **R-MTR-1 -- System election unknown** — The client must confirm whether they elect the 15% Final Withholding System or the normal progressive system. This affects all calculations. Cannot proceed without this election.  _(R-MTR-1)_
- **R-MTR-2 -- Related-party letting** — Rental income from related parties (as defined in Article 31E) cannot benefit from the 15% FWS. If the letting is between related parties, the normal progressive system must be used. Confirm relationship before proceeding.  _(R-MTR-2; Article 31E)_
- **R-MTR-3 -- Property transfers / capital gains** — Property disposals and transfer tax computations are outside the scope of this skill. Escalate to a warranted accountant.  _(R-MTR-3)_
- **R-MTR-4 -- Complex non-resident structures** — Non-resident landlords with complex holding structures, trusts, or nominee arrangements require specialist advice. Escalate to a warranted accountant.  _(R-MTR-4)_
- **R-MTR-5 -- Mixed election attempted** — A taxpayer cannot elect FWS for part of their rental income and the normal system for another part. All rental income must be under one system for any given year.  _(R-MTR-5)_

## Section 3 -- Final Withholding System (FWS) -- Computation Rules

### 3.1 Core Rules (Article 31E)

- **FWS core rules** — 1. The tax is 15% of **gross rental income received** in the basis year 2. Gross means gross — no deductions of any kind (repairs, insurance, management fees, mortgage interest, depreciation — NOTHING) 3. The tax is **final** — no refunds, no set-offs, no credits against other tax, no carry-forward of losses 4. Available to both residents and non-residents 5. Available to both individuals and bodies corporate 6. **NOT available** for rental income from related parties  _(Article 31E)_

### 3.2 Calculation

- **FWS tax calculation** — Tax = Gross rental income × 15% There is no exempt band, no personal allowance applicable, and no threshold below which FWS is unavailable.  _(Article 31E)_

### 3.3 Filing and Payment

**Filing and Payment**

| Step | Detail |
| --- | --- |
| Form | TA24 (rental income section) — paper or online via mytax.cfr.gov.mt |
| Deadline | 30 April of the following year |
| Payment | Accompanies the form; cash at MaltaPost or online |
| Late payment | Not accepted by MaltaPost branches after deadline |
| Rental income not declared in annual return | Correct — FWS income is excluded from the annual tax return |

### 3.4 FWS Historical Coverage

**FWS Historical Coverage**

| Property type | Available from |
| --- | --- |
| Residential property | Basis year 2014 (Legal Notice 99/2014) |
| Commercial property | Basis year 2017 (Legal Notice 158/2017) |

## Section 4 -- Normal Progressive System -- Computation Rules

### 4.1 Core Rules

- **Normal system core rule** — If FWS is not elected, rental income is declared in the annual tax return and taxed at progressive rates after deducting allowable expenses.

### 4.2 Allowable Deductions (Normal System Only)

**Allowable Deductions (Normal System Only)**

| Deduction | Notes |
| --- | --- |
| Mortgage interest | Interest on loan to acquire/improve the rental property |
| Repairs and maintenance | Revenue repairs only — not improvements or additions |
| Insurance | Building insurance, landlord liability insurance |
| Letting agent fees/commissions | Agency fees for finding/managing tenants |
| Condominium fees (spejjez komuni) | Ongoing maintenance charges for common parts |
| Ground rent (cens) | If applicable |
| Accountancy fees | Attributable to the rental property |
| Legal fees | Related to tenancy matters (not acquisition) |
| Advertising costs | To find tenants |
| Depreciation (wear and tear) | On furniture/fittings if furnished letting |
| Travel to property | Reasonable travel costs for property management |

### 4.3 Non-Deductible Items (Normal System)

**Non-Deductible Items (Normal System)**

| Item | Reason |
| --- | --- |
| Capital improvements (new extension, new roof) | Capital expenditure — not revenue |
| Mortgage principal repayments | Loan repayment, not expense |
| Personal living costs | Not related to letting activity |
| Periods of own occupation | Apportion if mixed use |
| Fines and penalties | Public policy |

### 4.4 Tax Rates (Normal System)

- **Tax Rates (Normal System)** — Progressive rates apply per the Income Tax Act rate tables. Rental income is added to all other income (employment, self-employment, investment) and taxed at the marginal rate. See the malta-income-tax skill for rate tables.  _(Income Tax Act rate tables)_

### 4.5 When Normal System May Be Preferable

- **High expenses relative to rent** — if deductible expenses exceed 15% of gross rent, normal system produces lower effective tax
- **Rental losses** — losses can offset other income under normal system; FWS does not allow losses
- **Low overall income** — if total income falls within the 0% band, no tax is due under normal system

## Section 5 -- Transaction Pattern Library

### 5.1 Income Patterns (Credits on Bank Statement)

**Income Patterns (Credits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KIRI, RENT RECEIVED, RENTAL PAYMENT | Rental income | Gross amount = FWS base; net of expenses under normal system |
| LETTING AGENT, PROPERTY MANAGER + DEPOSIT | Rental income | Agent collects on behalf — full gross is landlord's income |
| AIRBNB PAYOUT, BOOKING.COM PAYOUT | Rental income | Platform rental — verify if short-term (VAT implications) |
| SECURITY DEPOSIT, DEPOSIT RECEIVED | EXCLUDE if refundable | Not income unless forfeited |
| TENANT REIMBURSEMENT, UTILITY REFUND | EXCLUDE or reduce expense | Reimbursement of costs, not rental income |

### 5.2 Expense Patterns (Normal System Only -- Debits)

**Expense Patterns (Normal System Only -- Debits)**

| Pattern | Category | Treatment |
| --- | --- | --- |
| MORTGAGE INTEREST, LOAN INTEREST, BOV LOAN | Interest expense | Deductible under normal system; NOT under FWS |
| INSURANCE, GasanMamo, MAPFRE MIDDLESEA | Property insurance | Deductible under normal system |
| PLUMBER, ELECTRICIAN, HANDYMAN, REPAIRS | Repairs & maintenance | Deductible if revenue repair; capital improvement = not deductible |
| LETTING AGENT COMMISSION, MANAGEMENT FEE | Agent fees | Deductible under normal system |
| CONDOMINIUM, SPEJJEZ KOMUNI, COMMON PARTS | Common area charges | Deductible under normal system |
| GROUND RENT, CENS | Ground rent | Deductible under normal system |
| FURNITURE, APPLIANCE (replacement) | Wear and tear | Deductible under normal system for furnished lets |

### 5.3 Exclusions

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MORTGAGE REPAYMENT, LOAN PRINCIPAL | EXCLUDE | Capital repayment, not expense |
| PROPERTY PURCHASE, NOTARY (acquisition) | EXCLUDE | Capital cost — relevant only to transfer tax or CGT |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Not rental transaction |
| STAMP DUTY, PROPERTY TRANSFER TAX | EXCLUDE | Capital cost at acquisition |

## Section 6 -- Special Topics

### 6.1 Non-Resident Landlord Rules

- **Non-Resident Landlord Rules** — - Non-residents can elect FWS (15% on gross) just like residents - Non-residents can alternatively use the normal progressive system - Non-domiciled, non-resident landlords: Malta rental income is Malta-source and always taxable in Malta regardless of domicile or remittance - Double tax treaty relief may apply — landlord should check treaty with country of residence (Article 6 OECD Model typically gives primary taxing rights to the country where the property is situated)  _(Article 6 OECD Model)_

### 6.2 Short-Term Rental / Airbnb Treatment

- **Short-Term Rental / Airbnb Treatment** — - Short-term tourist accommodation (less than 30 days per booking) requires a Malta Tourism Authority (MTA) licence - Income from short-term lets is still rental income and can be taxed under FWS (15%) or normal system - **VAT treatment**: short-term tourist accommodation is subject to VAT at 7% (reduced rate for accommodation services) — this is separate from income tax - If the landlord is VAT-registered for short-term letting: VAT collected is NOT income; net of VAT is the rental income for FWS/normal system - Platform fees (Airbnb service fee, Booking.com commission) are deducted by the platform before payout — the gross rental income for tax purposes is the amount **before** platform deductions

### 6.3 Property Transfer Tax (on Disposal)

**Property Transfer Tax (on Disposal)**

| Scenario | Final WHT Rate |
| --- | --- |
| General property transfer | 8% of transfer value |
| Property acquired before 1 January 2004 | 10% of transfer value |
| Property in Urban Conservation Area (specific conditions) | 5% of transfer value |
| Sole residential property sold within 3 years | 2% of transfer value |
| Residential property owned and occupied ≥3 consecutive years | Exempt |

### 6.4 Furnished vs Unfurnished

- **Furnished vs Unfurnished** — - FWS: no distinction — 15% on gross regardless - Normal system: furnished lets may claim wear and tear deductions on furniture and appliances (replacement basis — not initial furnishing cost) - Furnished premium (if charged): included in gross rental income

### 6.5 VAT and Rental Income

**VAT and Rental Income**

| Scenario | VAT Treatment |
| --- | --- |
| Long-term residential letting (>30 days) | Exempt from VAT (no VAT charged, no input VAT recovery) |
| Long-term commercial letting | Exempt from VAT (with option to tax in certain circumstances) |
| Short-term tourist accommodation (<30 days) | 7% VAT (reduced rate) — requires VAT registration |
| Garage letting (standalone, not ancillary) | Standard 18% VAT |

### 6.6 Former EUR 1,200 Exemption

The EUR 1,200 ground rent exemption for resident individuals was applicable under older rules but has been superseded by the current FWS regime. Under the current system (from 2014 for residential, 2017 for commercial), no exempt band applies within the FWS — the full gross amount is subject to 15%. Under the normal progressive system, the standard 0% income tax band applies as part of the overall rate table.

## Section 7 -- Worked Examples

### Example 1 -- FWS, Single Residential Property

**Input:** Resident individual receives EUR 12,000 gross rent in 2025 from one apartment. Elects FWS. Expenses: EUR 2,500 (insurance, repairs, agent fees).

**Computation:**
```
Tax = EUR 12,000 × 15% = EUR 1,800
```
Expenses are irrelevant under FWS. Tax due = EUR 1,800. File TA24 by 30 April 2026.

### Example 2 -- Normal System, High Expenses

**Input:** Same landlord, EUR 12,000 rent. Does NOT elect FWS. Single, no other income. Expenses: EUR 5,000 (mortgage interest EUR 3,000, repairs EUR 1,200, insurance EUR 500, agent EUR 300).

**Computation:**
```
Net rental income = EUR 12,000 - EUR 5,000 = EUR 7,000
Tax (single rates): EUR 7,000 falls within 0% band (0--9,100) = EUR 0
```
Normal system produces zero tax. FWS would have cost EUR 1,800. Normal system is clearly preferable here.

### Example 3 -- FWS, Non-Resident Landlord

**Input:** UK-resident individual owns apartment in Sliema. Gross rent EUR 18,000. No deductions claimed.

**Computation:**
```
Tax = EUR 18,000 × 15% = EUR 2,700
```
Non-resident can elect FWS. Filed via TA24 by 30 April. The UK-Malta double tax treaty (Article 6) gives Malta primary taxing rights on immovable property income. The landlord claims credit for Malta tax paid against UK tax liability.

### Example 4 -- Short-Term Airbnb with VAT

**Input:** MTA-licensed host. Total Airbnb payouts received: EUR 20,000 (net of Airbnb's 3% host service fee). Actual gross bookings: EUR 20,619. VAT at 7% is charged on the gross accommodation charge.

**Computation:**
```
Gross income before platform fee = EUR 20,619
VAT component (7/107 × EUR 20,619) = EUR 1,349
Net income for tax = EUR 20,619 - EUR 1,349 = EUR 19,270
FWS tax = EUR 19,270 × 15% = EUR 2,891
```
Platform fees are NOT deducted from the FWS base — the landlord's income for FWS is the gross before platform commission, net of VAT.

### Example 5 -- Related-Party Let (FWS Blocked)

**Input:** Father lets apartment to son at EUR 500/month (EUR 6,000/year).

**Computation:** FWS is NOT available. Must declare under normal progressive system. If father has other income pushing him to 25% marginal rate and no deductions:
```
Additional tax = EUR 6,000 × 25% = EUR 1,500
```

## Section 8 -- Decision Flowchart: FWS vs Normal System

```
1. Is the tenant a RELATED PARTY?
   YES → Normal system only (FWS blocked)
   NO → Continue

2. Are total allowable expenses MORE than 15% of gross rent?
   YES → Normal system likely better (do full computation to confirm)
   NO → Continue

3. Does the landlord have other income that pushes them above the 0% band?
   YES → Continue to step 4
   NO → Normal system likely better (may pay zero tax)

4. Is the landlord's marginal rate above 15%?
   YES → FWS is likely better (15% flat < marginal rate)
   NO → Normal system likely better

ALWAYS compute both options and present to reviewer for confirmation.
```

## Section 9 -- Filing Checklist

### FWS Filing

- [ ] Confirm all rental income is from non-related parties
- [ ] Calculate total gross rental income for the basis year
- [ ] Compute 15% tax
- [ ] Complete TA24 (rental section) — paper or online
- [ ] Submit TA24 with payment by 30 April
- [ ] Do NOT include FWS rental income in annual tax return

### Normal System Filing

- [ ] Gather all rental income evidence (lease, bank receipts)
- [ ] Gather all expense receipts (repairs, insurance, interest, agent fees)
- [ ] Classify expenses as allowable revenue vs blocked capital
- [ ] Compute net rental income
- [ ] Include in annual tax return under rental income section
- [ ] File by 30 June

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Final Withholding System | ITA Article 31E |
| Residential property FWS | Legal Notice 99 of 2014 |
| Commercial property FWS | Legal Notice 158 of 2017 |
| Allowable deductions | ITA Article 14 |
| Property transfer tax | ITA Article 5A |
| Tax rates | ITA Rate Schedules |
| Filing deadlines | ITMA Chapter 372 |
| VAT on accommodation | VAT Act, 8th Schedule (Item 10) — 7% reduced rate |

## PROHIBITIONS

- NEVER apply FWS to related-party lettings
- NEVER deduct expenses under the FWS — the 15% rate applies to GROSS income with zero deductions
- NEVER allow a mixed election (part FWS, part normal) in the same basis year
- NEVER treat a refundable security deposit as rental income
- NEVER ignore VAT on short-term tourist accommodation
- NEVER present the FWS/normal system comparison as definitive without running both computations
- NEVER file FWS rental income in the annual tax return — it is declared separately on TA24
- NEVER compute property transfer tax in this skill — escalate to warranted accountant

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
