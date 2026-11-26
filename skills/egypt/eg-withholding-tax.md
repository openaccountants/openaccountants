---
name: eg-withholding-tax
description: Use this skill whenever asked about Egyptian withholding tax for tax year 2026, both on payments abroad to non-residents (interest, royalties, services, athletes and artists, dividends) and on payments to Egyptian residents under the deduction at source system of Law 91 art. 59 (commissions, brokerage, purchases, supplies, contracting, services) with quarterly form 41, plus the advance payment alternative. Trigger on phrases like "Egypt WHT", "Egypt withholding tax", "ضريبة الخصم تحت حساب الضريبة", "الخصم والتحصيل", "نموذج 41", "نموذج 11 مستقطعة", "dividends to non-resident Egypt", "royalty WHT Egypt", "technical services fee Egypt", "dividend tax Egypt", or any payment by an Egyptian payer that may need tax withheld. ALWAYS read this skill before touching any Egypt withholding work.
version: 0.5
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# Egyptian withholding tax — 2026

Use this Guide to classify Egyptian withholding before calculating it. Distinguish non-resident withholding, dividend tax and resident deductions on account of income tax. Amounts below are EGP. The figures are domestic rules; establish any treaty or statutory exemption first.

## Who this applies to

- Article 56 covers payments to non-residents by sole proprietors, Egyptian resident legal persons and non-resident bodies with an Egyptian permanent establishment (PE). The withholding obligation includes the specified special-economic-zone companies, establishments and branches and free-zone projects.
- Article 56 bis covers distributions by capital companies and partnerships, including special-economic-zone companies, to non-resident individuals and resident or non-resident legal persons. Civil companies count as partnerships. Resident individual dividend tax is a separate topic in `eg-income-tax`.
- For resident deductions, establish that the payer is within Article 59. Its list includes government/public bodies, companies, investment/free-zone businesses, foreign branches, partnerships with capital **over EGP 50,000**, pharmaceutical warehouses, import offices, cooperatives, press and educational institutions, professional offices and the other listed bodies or bodies designated by ministerial decision. Consult the complete Article 59 list before treating an unlisted payer as liable. [Law 91, art. 59](https://www.wipo.int/wipolex/ar/legislation/details/20194).
- An accepted advance-payment taxpayer with regular records is exempt from the Article 59 deduction system (art. 60). For a project established as subject to Law 6/2025, Article 11 excludes the income-tax deduction-on-account and advance-payment systems; this is **not a blanket exemption from every withholding category**. Establish regime eligibility under `eg-sme-tax` first. [Law 6, art. 11](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf).
- State ownership alone does not establish exemption. Law 159/2023 cancels the specified State-entity tax/fee exemptions for economic or investment activity, subject to international agreements, military/defence/national-security and basic-public-utility exceptions. Contracts concluded before commencement keep their prior legal treatment until completely performed. [Law 159, arts. 1–2](https://eta.gov.eg/sites/default/files/2024-12/law_no._159_for_2023.pdf). State-specific application is held below.

## Rates, bands and thresholds

| Payment or rule | Amount / boundary | Conditions and period | Official source |
|---|---|---|---|
| Non-resident interest, royalties and athlete/artist fees | 20% of gross, no costs | Article 56; athlete/artist payment direct or through another body; establish exemptions and treaty position first. The former industry-design/know-how royalty exception is absent from the replacement royalty clause. 2026 | https://www.wipo.int/wipolex/ar/legislation/details/20194 ; https://eta.gov.eg/sites/default/files/2024-03/law_no.101-2012.pdf |
| Non-resident service fees | 20% of gross, no costs | Article 56; first classify the service, including Regulations arts. 72–73 exclusions/treaty treatment; specialist classification is held below. Qualifying PE head-office costs are treated separately below. 2026 | https://www.wipo.int/wipolex/ar/legislation/details/20194 ; https://www.wipo.int/wipolex/ar/legislation/details/19951 |
| Qualifying PE share of foreign head-office administrative, control and supervision costs | Outside service-fee category; cap 10% of PE net taxable profit | No royalties, interest, commissions or direct wages within the allocated amount; certified and authenticated head-office auditor certificate required. Article 56(3), Law 101/2012; Regulations art. 74 replaced by Decision 172/2015. 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.101-2012.pdf ; https://eta.gov.eg/sites/default/files/2024-03/law_no.172-2015.pdf |
| Dividends within Article 56 bis | 10%; 5% for securities listed on the Egyptian Exchange | Gross, no costs; bonus shares excluded. Non-resident individuals and resident/non-resident legal persons; resident-company exclusions held below. Same rates in both periods: 1 Jan–28 Jul under Law 30/2023; from 29 Jul under Law 151/2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf ; https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Non-resident legal person's Egyptian PE profits | 10%; deemed distributed **within** 60 days of financial year end | Article 56 bis; determine distribution timing/base for the actual PE, not an automatic distribution exactly on day 60. Both 2026 periods above | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf ; https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Commission/brokerage paid to an individual, unconnected with carrying on their profession | 20% without costs | Article 57; sole-proprietor or legal-person payer. 2026 | https://www.wipo.int/wipolex/ar/legislation/details/20194 |
| Treasury-bill interest | 20% without costs | Article 58(2), also covering specified creditor balances in the Treasury single account. 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| Article 59 resident deduction on account | Payment **over EGP 300**; ministerial percentage capped at 5% | Commission, brokerage, purchases, supplies, contracting or services to a private-sector person; insurance premiums excepted. Capital-company dividends are included by statute regardless of amount, but apply the separate dividend rules. The ceiling is **not an activity rate to apply**: actual decree classification/rate is held below. 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf ; https://www.wipo.int/wipolex/ar/legislation/details/20194 |
| Advance-payment alternative | 60% of last declared tax | Use estimated tax for the intended year if no previous return or previous return shows a loss. ETA acceptance and regular records required for relief from Article 59 deduction. 2026 | https://www.wipo.int/wipolex/ar/legislation/details/20194 |

## The base

1. Establish payer/payee identity, residence, PE, payment category, date, gross/net contract terms and applicable exemption/treaty position. **Do not apply the service rate before classification.** The regulatory exclusions include transport/freight, shipping, insurance, training, exhibitions/conferences, international-exchange registration, direct advertising/promotion, religious services, accommodation and the specified Tourism Ministry charter-flight incentive payments (Regulations art. 72). Application to mixed services: **Check this point with one of our partner accountants.**
2. For a taxable Article 56 amount, multiply gross by the rate. If the contract gives a tax-free net amount and the payer bears a 20% withholding, the conditional arithmetic is gross = net / 0.80; tax = gross − net. Confirm contractual and legal classification first.
3. Use the Article 56 bis dividend rates only within their scope. Resident-company dividend exclusions, costs, pass-through distributions and period allocation: **Check this point with one of our partner accountants.**
4. Keep resident deductions as a separate tax credit process. The annual income-tax payment is net of tax deducted/collected and advances, with any applicable yield, under Unified Tax Procedures Law art. 32; this is not proof that every non-resident withholding is creditable. [Law 206, art. 32](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf).

## Deadlines and filing

| Category | Form / action | Deadline and scope | Official source |
|---|---|---|---|
| Article 56 | Form 11 مستقطعة; remittance to the withholding collection department of the central international-agreements administration | **First working day following withholding**, including the specified special-zone/free-zone payers. Statute as amended by Law 101/2012 controls; do not use the former following-month deadline or former free-zone Form 12 | https://eta.gov.eg/sites/default/files/2024-03/law_no.101-2012.pdf ; https://eta.gov.eg/sites/default/files/2024-03/law_no.172-2015.pdf |
| Article 56 bis dividends | Withhold by the body executing the transaction; prescribed dividend form | Within five working days from the beginning of the month following collection; central deduction/collection administration. Same deadline in both 2026 periods | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf ; https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Article 57 commission/brokerage | Remit to payer's competent tax office; Form 14 under Regulations art. 79 | First 15 days of the month following payment | https://www.wipo.int/wipolex/ar/legislation/details/20194 ; https://www.wipo.int/wipolex/ar/legislation/details/19951 |
| Treasury-bill interest | Payer collects and remits to competent tax office | Day following deduction, Article 58(2) | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| Article 59 ordinary resident deductions, **excluding capital-company dividends** | Form 41 خصم وتحصيل; retain transactions/payee/tax records | End of April, July, October and January; Regulations art. 82 as replaced in 2015 | https://eta.gov.eg/sites/default/files/2024-03/law_no.172-2015.pdf |
| Elect advance payments | Request before intended period; await ETA decision | At least 60 days before period begins; ETA has 60 days to answer; silence means refusal (art. 62) | https://www.wipo.int/wipolex/ar/legislation/details/20194 |
| Accepted advance payments | Three equal instalments | By 30 June, 30 September and 31 December (art. 63); after second payment, notify ETA to reduce/omit third if full-year profit will be below prior-year estimated profit. Short periods, forms, yield and cancellation held below | https://www.wipo.int/wipolex/ar/legislation/details/20194 |

Use the [ETA withholding forms page](https://www.eta.gov.eg/ar/content/nmadhj-aqrarat-alkhsm-walthsyl) for current templates. Retain transaction details, computation, remittance evidence and the payee certificate. Current upload/office/payment-channel instructions: **Check this point with one of our partner accountants.**

## Penalties and interest

| Rule | Consequence / boundary | Official source |
|---|---|---|
| Failure to apply withholding/deduction/collection/remittance within legal deadlines | Article 135 surviving third paragraph: fine of 25% of unpaid amounts. It survives Law 206/2020 issuing art. 4. This does not extinguish principal or delay charge | https://www.wipo.int/wipolex/ar/legislation/details/20194 ; https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Settlement of that offence | Minister or delegate **may** settle under art. 75 bis 1 for 12.5% of amounts not withheld/deducted/collected or withheld/deducted/collected but not remitted, **plus principal and delay charge**. Payment alone does not establish settlement approval | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |
| Delay on unremitted withholding | Starts day after remittance deadline; statutory rate is relevant preceding 1 January CBE credit/discount rate + 2 percentage points, excluding fractions of a month and pound. Where the applicable reference is 1 Jan 2026: 20.50% + 2% = 22.50% annually. Do not select a rate merely from the income's tax year | https://www.wipo.int/wipolex/ar/legislation/details/20194 ; https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf |
| Delay-charge ceiling | 100% of the principal tax on which delay/additional tax is due, Law 206 art. 45 bis | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |

Other return/form offences, repeat offences, evasion and manager liability: **Check this point with one of our partner accountants.**

## Cross-border points

Each line is a hold, not a usable tax conclusion:

| Topic | Action |
|---|---|
| Treaty country rates, residence/beneficial-owner/PE tests, relief at source versus refund, documents, refund limits and processing time | Check this point with one of our partner accountants. |
| Government foreign borrowing, legacy company loans before Law 30/2023 and national-infrastructure loan relief under Law 151/2026 and its Gazette erratum; maturity, lender relationship, project designation, investment share and expiry | Check this point with one of our partner accountants. |
| Rents to non-residents, software/know-how classification, Egyptian-source analysis, mixed services, timing of deduction on payment/credit/invoice | Check this point with one of our partner accountants. |
| Non-resident listed/unlisted share or company-interest gains, treasury-bill gains, seller payment and buyer obligations | Check this point with one of our partner accountants. |
| Resident Article 59 activity rates and current threshold application; exempt payees and reporting under arts. 59 bis–59 bis 2, designated goods/activities/rents and quarterly data requirements | Check this point with one of our partner accountants. |
| State payees/payers: Law 159 scope, PM Decree 242/2024, ETA circular 6/2024, exemption/non-liability or advance-payment certificates, separate activity accounts, indirect ownership, basic-utility list, pre-existing contracts/renewals/increases and special-law/NOSI exemptions | Check this point with one of our partner accountants. |
| Advance-payment forms/certificates, short/non-calendar periods, yield, return to deduction after losses/legal-form change/estimate differences; record retention and annual reconciliation | Check this point with one of our partner accountants. |

Salary/non-original-employer withholding: `eg-payroll`; company profit tax: `eg-corporate-tax`; imported-service VAT: `egypt-vat`; related cross-border analysis: `eg-cross-border`. These are separate computations, not additional amounts computed here.

## Two worked examples that recompute

**Case 1 — royalty and dividend to a foreign parent.** An Egyptian unlisted company pays a **gross royalty of EGP 1,000,000** and a **gross dividend of EGP 5,000,000** to its non-resident parent in **March 2026**, with no treaty claim. Conditional on taxable royalty classification and no applicable exemption: royalty tax = 1,000,000 × 20% = **200,000**, net royalty **800,000**; dividend tax = 5,000,000 × 10% = **500,000**, net dividend **4,500,000**; total net **5,300,000**. The royalty is remitted on Form 11 on the first working day following withholding; the dividend within five working days from the beginning of April. Payment/withholding date and holiday calendar are needed to name an exact due date. If the securities were listed on the Egyptian Exchange, dividend tax would be **250,000**. This March case uses Law 30/2023, not the later Law 151 resident-dividend exclusions.

```oa-check
name: Royalty and dividend to non-resident parent 2026
inputs:
  royalty: 1000000
  dividend: 5000000
steps:
  - royalty_tax: royalty * 0.20
  - dividend_tax: dividend * 0.10
  - net_paid: royalty + dividend - royalty_tax - dividend_tax
  - dividend_tax_listed: dividend * 0.05
expected:
  royalty_tax: 200000.00
  dividend_tax: 500000.00
  net_paid: 5300000.00
  dividend_tax_listed: 250000.00
```

**Case 2 — approved settlement versus the statutory fine.** Preserve the original company/service-payment scenario: **EGP 200,000 withheld in January 2026**, unremitted, with **five whole months of chargeable delay** after the statutory deadline, all within 2026. Exact dates are needed to establish that count; no later-year rate is assumed. At the applicable 22.50% annual rate, charge = 200,000 × 22.5% × 5/12 = **18,750**, below the cap. **If the Minister/delegate approves settlement** and no other amounts apply, compensation = 200,000 × 12.5% = **25,000**, total **243,750**. The Article 135 fine comparison is 200,000 × 25% = **50,000**, total **268,750** on the same principal/delay assumptions. Difference **25,000**. This compares amounts; it does not promise settlement, extinguish prosecution automatically or suggest that waiting is permissible.

```oa-check
name: Missed remittance, settlement against fine
inputs:
  withheld: 200000
  months: 5
steps:
  - delay: withheld * 0.225 * months / 12
  - settle_total: withheld + delay + withheld * 0.125
  - fine_total: withheld + delay + withheld * 0.25
  - saving: fine_total - settle_total
expected:
  delay: 18750.00
  settle_total: 243750.00
  fine_total: 268750.00
  saving: 25000.00
```

## Ask the client first

1. Payer and payee identity, legal form, residence, Egyptian PE and State ownership?
2. Payment category, gross amount, payment/withholding dates and contract gross-up clause?
3. Dividend recipient type, securities listing, relevant period and any resident-company exclusion?
4. Statutory exemption/certificate, accepted advance-payment status or established Law 6/2025 eligibility?
5. Treaty, residence certificate, beneficial owner and connection to an Egyptian PE?
6. For an unpaid remittance: exact due/payment dates, principal, prior payments and formal settlement status?

Do not present a computation as a filed form or accountant approval.

## Sources

Read/reuse scope is explicit: the existing 2 November primary-source reads and independent review were reused where applicable; the missing operative amendments were read on 26 November. Held topics above make no usable tax assertion.

| Source and scope | Official URL | Read / applicability checked |
|---|---|---|
| Income Tax Law 91, relevant arts. 56–63, 86, 110, 135; WIPO Arabic consolidated text through 2020, with later amendments applied separately | https://www.wipo.int/wipolex/ar/legislation/details/20194 | 2026-11-26 — relevant operative sentences read |
| Law 53/2014 replacement art. 59 first paragraph: payment threshold, activity/recipient scope, ceiling and insurance-premium exception | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf | 2026-11-26 — Gazette PDF p. 3 image read to resolve consolidated-text transcription |
| Law 101/2012 art. 1 replacements: royalty clause, head-office expenses and next-working-day remittance; Gazette PDF p. 6 | https://eta.gov.eg/sites/default/files/2024-03/law_no.101-2012.pdf | 2026-11-26 — page image read |
| Decision 172/2015: replacement Regulations arts. 74, 76, 82; Gazette PDF pp. 8–9 | https://eta.gov.eg/sites/default/files/2024-03/law_no.172-2015.pdf | 2026-11-26 — page images read |
| Regulations 991/2005, WIPO amended Arabic text: arts. 71–79 and 82 service exclusions/forms | https://www.wipo.int/wipolex/ar/legislation/details/19951 | 2026-11-26 — relevant clauses read |
| Law 30/2023 arts. 56 bis and 58(2), dividend scope/rates/deadline and treasury-bill interest | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | 2026-11-26 — operative clauses read; prior review reused |
| Law 151/2026 arts. 56 bis and issuing art. 7, dividends/PE scope, rates, deadline and commencement | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-26 — operative clauses read; prior review reused |
| Law 6/2025 art. 11 limited exclusion; eligibility remains subject to its own conditions | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-26 — completed bookkeeping/SME source row reused; applicability checked |
| Law 159/2023 arts. 1–2, economic-activity cancellation, exceptions and existing contracts | https://eta.gov.eg/sites/default/files/2024-12/law_no._159_for_2023.pdf | 2026-11-26 — completed corporate/stamp-duty source rows reused; applicability checked |
| Law 206/2020 issuing art. 4 saves art. 135 third paragraph; art. 32 annual credit/payment rule | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-26 — issuing art. 4 page image read; completed corporate art. 32 row reused |
| Law 7/2025 arts. 45 bis and 75 bis 1, cap and discretionary settlement | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-26 — operative text read |
| ETA circular 1/2026, rate reference and 2026 CBE row | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | 2026-11-26 — page image read |

Not yet confirmed: the specialist applications listed under Cross-border points and the other express referrals above. Check this point with one of our partner accountants.

> Originally contributed by Ahmed Hassan; rebuilt against the law by the OpenAccountants team.
