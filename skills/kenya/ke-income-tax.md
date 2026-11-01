---
name: ke-income-tax
description: Use this skill whenever asked about Kenyan income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "KRA", "iTax", "income tax return", "personal relief", "insurance relief", "turnover tax", "presumptive tax", "self-employed tax Kenya", or any question about filing or computing income tax for a self-employed or sole proprietor client in Kenya. ALWAYS read this skill before touching any Kenyan income tax work.
version: 2.2
jurisdiction: KE
tax_year: 2025
tax_year_notes: Rates and reliefs reviewed for the year of income 2025 only. The SHIF treatment was updated on 2026-10-31. Finance Act, 2026 changes are listed in their own section and are not yet worked into the rates or examples.
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KE Income Tax

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Kenya |
| Tax type | Income tax on business income (self-assessment) |
| Primary legislation | Income Tax Act, Chapter 470 |
| Supporting legislation | Tax Procedures Act 2015; Finance Act 2023; Finance Act 2024 |
| Tax authority | KRA (Kenya Revenue Authority) |
| Filing portal | iTax (itax.kra.go.ke) |
| Currency | KES only |
| Return form | Self-assessment return |
| Filing deadline | 30 June of the following year. Finance Act, 2026 s.18 moves individuals to the last day of the fourth month after the year of income, in force 1 January 2027: see "Finance Act, 2026" |
| Instalment tax | Quarterly (20th of 4th, 6th, 9th, 12th months) |
| Personal relief | KES 28,800/year (credit against tax) |
| Insurance relief | 15% of qualifying premiums, cap KES 60,000/year |
| Turnover tax | 1.5% on gross turnover KES 1M--25M (non-professional) |
| Presumptive tax | KES 15,000/year (turnover below KES 1M) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Kenyan CPA or registered tax agent sign-off |
| Validation date | Pending |

**Progressive tax table (resident, annual)**

| Taxable income (KES) | Rate |
| --- | --- |
| 0--288,000 | 10% |
| 288,001--388,000 | 25% |
| 388,001--6,000,000 | 30% |
| 6,000,001--9,600,000 | 32.5% |
| 9,600,001+ | 35% |

**Wear-and-tear rates (reducing balance)**

| Asset | Rate |
| --- | --- |
| Heavy/self-propelling machinery | 37.5% |
| Computer/IT equipment | 30% |
| Motor vehicles | 25% |
| Furniture and fittings | 12.5% |
| Farm machinery | 100% |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | STOP -- non-residents pay flat 30% |
| Unknown expense category | Not deductible |
| Unknown business-use proportion | 0% |
| Unknown whether turnover tax is elected | Normal tax |

**Read this whole section before classifying anything.**

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs**: bank statement for the tax year. Acceptable from: Equity Bank, KCB (Kenya Commercial Bank), Co-operative Bank, NCBA, Standard Chartered Kenya, Absa Kenya, I&M Bank, DTB, or mobile money (M-Pesa via Safaricom).
- **Recommended inputs**: invoices, insurance premium certificates, instalment tax payment records, PIN certificate, WHT certificates.
- **Ideal inputs**: complete bookkeeping, prior year return, iTax account records.

### Refusal catalogue

- **R-KE-1 -- Company/LLP**: This skill covers self-employed individuals only. Companies file corporate returns at 30%. (Trigger: client is a limited company or LLP.)
- **R-KE-2 -- Non-resident**: Non-residents pay flat 30% on Kenya-source income with no personal relief. This skill covers residents only. (Trigger: non-resident status.)
- **R-KE-3 -- Cross-border/WHT**: Cross-border WHT and treaty analysis are outside scope. Consult a tax practitioner. (Trigger: complex withholding tax or treaty questions.)
- **R-KE-4 -- Capital gains**: Capital gains tax (15%) is outside scope. (Trigger: property disposal.)

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 Kenyan banks (fees and interest)

**Kenyan banks (fees and interest)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EQUITY BANK | Bank charges: deductible | Monthly/transaction fees |
| KCB, KENYA COMMERCIAL BANK | Bank charges: deductible | Same |
| CO-OPERATIVE BANK, CO-OP | Bank charges: deductible | Same |
| NCBA | Bank charges: deductible | Same |
| STANDARD CHARTERED KENYA | Bank charges: deductible | Same |
| ABSA KENYA (formerly Barclays) | Bank charges: deductible | Same |
| I&M BANK, DTB | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| INTEREST (credit) | Taxable income | Subject to WHT at source (15%) |
| INTEREST (debit) | Deductible if business loan | Personal: NOT deductible |
| LOAN (principal) | EXCLUDE | Principal movement |

### 3.2 M-Pesa and mobile money

**M-Pesa and mobile money**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MPESA, M-PESA, SAFARICOM | Transaction fees: deductible | Business M-Pesa charges |
| MPESA PAYBILL, TILL NO | Revenue if incoming; deductible if outgoing business payment | Verify nature |
| MPESA FLOAT, B2C, C2B | EXCLUDE if internal movement | Business float management |
| AIRTEL MONEY | Same as M-Pesa | Alternative mobile money |

### 3.3 Kenyan government and statutory bodies

**Kenyan government and statutory bodies**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KRA, KENYA REVENUE AUTHORITY | EXCLUDE | Tax payment |
| NSSF, NATIONAL SOCIAL SECURITY | Deductible (up to statutory limit) | Provident fund contribution |
| SHIF, SOCIAL HEALTH INSURANCE | Deductible (ITA s15(2)(ae)) | Deduction from taxable income, not insurance relief |
| NHIF (legacy) | NOT deductible | Replaced by SHIF |
| COUNTY GOVERNMENT, NAIROBI COUNTY | Deductible if business licence/permit | Business licence fees |

### 3.4 Kenyan utilities and telecoms

**Kenyan utilities and telecoms**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KENYA POWER, KPLC | Deductible if business premises | Electricity; apportion if home |
| NAIROBI WATER, ELDOWAS | Deductible if business premises | Water |
| SAFARICOM, AIRTEL, TELKOM KENYA | Deductible: business phone/internet | Mixed: apportion |
| ZUKU, FAIBA | Deductible: business internet | Mixed: apportion |

### 3.5 SaaS and software -- international

**SaaS and software -- international**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | International SaaS |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.6 Professional services (Kenya)

**Professional services (Kenya)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACCOUNTANT, CPA, AUDIT FIRM | Deductible | Accounting fees |
| ADVOCATE, LAW FIRM | Deductible if business | Legal fees |
| TAX AGENT | Deductible | Tax advisory |

### 3.7 Transport and travel

**Transport and travel**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KENYA AIRWAYS, JAMBOJET | Deductible if business travel | Flights |
| UBER, BOLT, LITTLE CAB | Deductible if business | Ride services |
| TOTAL, SHELL, RUBIS, VIVO ENERGY | Deductible: business vehicle portion | Fuel |
| SGR (Madaraka Express) | Deductible if business | Train |

### 3.8 Insurance

**Insurance**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| JUBILEE, BRITAM, CIC, UAP, APA | Deductible if business insurance | Personal life/health: insurance RELIEF (not deduction) |
| INSURANCE PREMIUM (life/health/education) | Insurance relief: 15% of premiums, cap KES 60,000 | Credit against tax |

### 3.9 Food and entertainment

**Food and entertainment**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NAIVAS, CARREFOUR KE, QUICKMART | Default: NOT deductible | Personal provisioning |
| RESTAURANT | Deductible only if wholly and exclusively business | Must prove |

### 3.10 Internal transfers and exclusions

**Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| MPESA TO BANK, BANK TO MPESA | EXCLUDE | Own account transfer |
| DRAWINGS, PERSONAL | EXCLUDE | Owner drawings |

## Section 4 -- Worked examples

### Example 1 -- Standard self-employed, mid-range

**Input:** Resident, revenue KES 3,000,000, expenses KES 1,200,000, insurance premiums KES 100,000, instalment tax KES 150,000.
**Computation:** Taxable = KES 1,800,000. Tax = 28,800 + 25,000 + 423,600 = KES 477,400. Less personal relief 28,800. Less insurance relief min(15,000, 60,000) = 15,000. Net = KES 433,600. Less instalment KES 150,000. Due = KES 283,600.

```oa-check
name: Standard self-employed, profit KES 1,800,000
inputs:
  profit: 1800000
  premiums: 100000
  instalments: 150000
steps:
  - tax: 288000 * 0.10 + 100000 * 0.25 + (profit - 388000) * 0.30
  - insurance_relief: min(premiums * 0.15, 60000)
  - net: tax - 28800 - insurance_relief
  - due: net - instalments
expected:
  tax: 477400
  net: 433600
  due: 283600
```

### Example 1A -- SHIF deducted

**Input:** Resident, profit before SHIF KES 1,800,000, SHIF paid KES 49,500, no insurance premiums.
**Computation:** Taxable = KES 1,750,500. Tax = 28,800 + 25,000 + 408,750 = KES 462,550. Less personal relief 28,800. Insurance relief on SHIF is nil. Net = KES 433,750.

```oa-check
name: SHIF deducted from taxable income, no insurance relief
inputs:
  profit: 1800000
  shif: 49500
steps:
  - taxable: profit - shif
  - tax: 288000 * 0.10 + 100000 * 0.25 + (taxable - 388000) * 0.30
  - net: tax - 28800
expected:
  taxable: 1750500
  tax: 462550
  net: 433750
```

### Example 2 -- Below personal relief

**Input:** Taxable income KES 200,000.
**Computation:** Tax = 10% x 200,000 = KES 20,000. Less relief KES 28,800. Payable = KES 0.

### Example 3 -- Turnover tax

**Input:** Non-professional trader, turnover KES 8,000,000.
**Computation:** TOT = 1.5% x KES 8,000,000 = KES 120,000/year.

### Example 4 -- Presumptive vs normal

**Input:** Small trader, turnover KES 500,000, expenses KES 350,000.
**Computation:** Normal: profit KES 150,000. Tax = 15,000 - 28,800 relief = KES 0. Presumptive: KES 15,000. Normal is better.

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Progressive rates

- **Progressive rates**: 10%/25%/30%/32.5%/35%. Non-residents: flat 30%.  _(ITA Cap 470, Third Schedule.)_

### 5.2 Personal relief

- **Personal relief**: KES 28,800/year. Credit against tax, NOT deduction from income. Available to all residents.  _(ITA.)_

### 5.3 Insurance relief

- **Insurance relief**: 15% of qualifying premiums (life, health, education). Cap KES 60,000/year. Credit against tax. SHIF contributions do not qualify; they are a deduction under s15(2)(ae).  _(s31; KRA notice 8 Nov 2024.)_

### 5.4 Instalment tax

- **Instalment tax**: Quarterly: 25% each on 20th of 4th, 6th, 9th, 12th months. Based on estimated current year or prior year actual. If prior year tax < KES 40,000: not required. Under-estimation: 20% penalty.  _(s12.)_

### 5.5 Turnover tax

- **Turnover tax**: 1.5% on gross turnover KES 1M--25M. Monthly filing. Replaces income tax. No expense deductions. Excludes professional/management services.  _(s12C.)_

### 5.6 Presumptive tax

- **Presumptive tax**: KES 15,000/year for specified businesses under KES 1M turnover. Final tax.  _(s12D.)_

### 5.7 Wear-and-tear (capital deductions)

- **Wear-and-tear rates**: Reducing balance method. Heavy machinery: 37.5%. Computers: 30%. Vehicles: 25%. Furniture: 12.5%. Farm machinery: 100%.  _(Second Schedule.)_

### 5.8 NSSF/SHIF

- **NSSF/SHIF treatment**: NSSF (provident): deductible up to statutory limit. SHIF (health): deductible, from 27 December 2024. Insurance relief does not apply to SHIF.  _(ITA s15(2)(ae); KRA PAYE page; KRA notice 8 Nov 2024.)_

### 5.9 WHT credits

- **WHT credits**: Withholding tax on professional fees (5%) is a credit against final tax. Requires WHT certificates.  _(ITA.)_

### 5.10 Record keeping

- **Record keeping**: 5 years. English or Swahili. Paper or electronic.  _(Tax Procedures Act s23.)_

## Section 6 -- Tier 2 catalogue

### 6.1 Turnover tax vs normal tax

*Why:* Depends on expense level and qualification. *Default:* Present both. *Question:* "What are your total expenses? Professional services?"

### 6.2 Below KES 1M: presumptive vs normal

*Why:* Normal may be cheaper if expenses are high. *Default:* Compute both. *Question:* "Total documented expenses?"

### 6.3 Motor vehicle business portion

*Why:* Unknown split. *Default:* 0%. *Question:* "Do you maintain a logbook?"

### 6.4 Home office

*Why:* Must be dedicated space. *Default:* Not deductible. *Question:* "Dedicated room for business?"

### 6.5 Capital allowances (industrial building)

*Why:* Complex rules. *Default:* Flag for reviewer. *Question:* "Do you own business premises?"

## Section 7 -- Excel working paper template

### Sheet "Transactions"

Columns: Date, Counterparty, Description, Amount (KES), Category (Revenue/Expense/Capital/Insurance/EXCLUDE), Deductible amount, Default?, Question, Notes.

### Sheet "Tax Computation"

Progressive brackets. Reliefs. Instalment tax offset. WHT credits.

## Section 8 -- Bank statement reading guide

**CSV formats.** Equity Bank exports CSV with DD/MM/YYYY. KCB uses various formats. Co-op Bank uses semicolons. Common columns: Date, Description/Narration, Debit, Credit, Balance.

**M-Pesa integration.** Many transactions flow through M-Pesa. M-Pesa statements are separate from bank statements. Request both. M-Pesa shows: transaction ID, type (paybill/till/send money), recipient, amount.

**Kenyan-specific patterns.** "PAYBILL" = payment to business. "TILL" = payment at point of sale. "B2C" = business to customer. "C2B" = customer to business. "FULIZA" = overdraft (loan -- exclude principal). "KCB MPESA" = integrated mobile banking.

**WHT deductions.** Professional fees received may have 5% withheld. Gross up the income and claim WHT credit.

**Foreign currency.** Convert to KES at CBK (Central Bank of Kenya) rate on transaction date.

## Section 9 -- Onboarding fallback

### 9.1 Residency

*Inference:* Kenyan bank + KRA PIN. *Fallback:* "Are you a Kenyan tax resident?"

### 9.2 Nature of trade

*Inference:* From counterparty mix. *Fallback:* "What is your business activity?"

### 9.3 Annual turnover

*Inference:* Sum of credits. *Fallback:* "What is your approximate annual turnover? (Determines TOT/presumptive eligibility.)"

### 9.4 Tax regime

*Inference:* If TOT monthly payments visible. *Fallback:* "Are you on turnover tax, presumptive tax, or normal self-assessment?"

### 9.5 Insurance premiums

*Inference:* Monthly insurance debits. *Fallback:* "Do you pay life, health, or education insurance premiums?"

### 9.6 Instalment tax

*Inference:* Quarterly KRA payments. *Fallback:* "What instalment tax amounts have you paid?"

### 9.7 WHT certificates

*Inference:* Not inferable from bank statement. *Fallback:* "Do you have WHT certificates from clients who withheld tax?"

## Section 10 -- Reference material

### Test suite

**Test 1 -- Mid-range.** KES 3M revenue, KES 1.2M expenses, KES 100K insurance, KES 150K instalment. Net tax KES 283,600.
**Test 2 -- Below relief.** KES 200K taxable. Tax KES 0 (below relief).
**Test 3 -- Turnover tax.** KES 8M turnover. TOT KES 120,000.
**Test 4 -- Insurance cap.** KES 600K premiums. Relief = KES 60,000.
**Test 5 -- High earner.** KES 12M taxable. Tax KES 3,718,600.
**Test 6 -- Presumptive vs normal.** KES 500K turnover, KES 350K expenses. Normal = KES 0; presumptive = KES 15,000.

### Edge case registry

**EC1 -- Personal relief as deduction.** INCORRECT -- it's a credit against tax.
**EC2 -- Insurance relief cap.** KES 60,000 maximum.
**EC3 -- TOT for professionals.** NOT eligible.
**EC4 -- Presumptive vs normal.** Compare both.
**EC5 -- WHT not credited.** Must include as credit.
**EC6 -- SHIF deductibility.** Deductible under ITA s15(2)(ae). No insurance relief on SHIF.
**EC7 -- Capital gain on business asset.** ESCALATE.
**EC8 -- Non-resident consulting.** 20% WHT (or treaty rate). ESCALATE.

### Prohibitions

- NEVER apply personal relief as deduction from income
- NEVER allow turnover tax for professional/management services
- NEVER allow insurance relief above KES 60,000
- NEVER compute non-residents with progressive rates
- NEVER allow capital expenditure as direct expense
- NEVER ignore WHT certificates
- NEVER give insurance relief on SHIF contributions
- NEVER present calculations as definitive

## Finance Act, 2026

Published in Kenya Gazette Supplement No. 157 (Acts No. 19), 26 June 2026. Commencement (s.1): ss.17, 18 and 24 on 1 January 2027; s.43 on 1 September 2026; all other sections on 1 July 2026. Income Tax Act amendments that reach individuals and small businesses:

| Section | Change | In force |
|---|---|---|
| s.2 | "Management or professional fee" includes interchange and merchant service fees on card payments. "Royalty" is redefined to include software, proprietary or off-the-shelf, whether licence, development, training, maintenance or support fees | 1 July 2026 |
| s.3 | Gratuity contribution added to s.5(4): contract of at least three years, amount not above 31% of emoluments for the contract period | 1 July 2026 |
| s.4 | New s.6B: non-resident rental income tax, a final tax. Return and payment by the 20th of the month after the month rent is paid, unless a resident receiving the rent deducts under s.35(1)(c). See `non-resident-rental-income-tax-on-kenyan-property` | 1 July 2026 |
| s.5 | Income Tax Act s.8(5A) deleted | 1 July 2026 |
| s.7, s.16, s.21 | Scrap metal and winnings added to s.10 and s.35. Withholding: 1.5% of the gross amount on scrap metal, 20% on winnings | 1 July 2026 |
| s.8 | Trust income is deemed income of the trustee, executor or administrator. A beneficiary is not liable on income on which that person paid tax | 1 July 2026 |
| s.9 | s.12(1)(a) replaced: covers a person with no income chargeable for the year other than emoluments | 1 July 2026 |
| s.10 | Bad debts of money lenders, banks and licensed financial institutions include principal, interest and related amounts. Deficit carry-forward proviso for investors of at least KES 10 billion before 1 July 2025 | 1 July 2026 |
| s.15 | Income Tax Act s.23 repealed | 1 July 2026 |
| s.17 | s.52(1): notice to furnish a return now runs to the last day of the fourth month after the year of income | 1 January 2027 |
| s.18 | s.52B(1): individuals file with self-assessment by the last day of the fourth month after the year of income; others by the last day of the sixth month after the accounting period | 1 January 2027 |
| s.19 | First Schedule: benefits arising due to death added to paragraph 53 proviso; capital gains on transfer of property to a registered real estate investment trust exempt (paragraph 76) | 1 July 2026 |
| s.20 | Second Schedule: 100% first-year allowance on item (iv) where investment is over KES 10 billion; item (a)(viii) 10% is per year in equal instalments | 1 July 2026 |

If a client's year of income ends on 31 December, the s.18 date is 30 April. The Act does not say in s.1 which year of income is the first one caught; check KRA guidance before quoting 30 April for the 2026 return.

The rest of the Act (other Income Tax amendments, VAT, excise, Tax Procedures, fees and levies, housing levy, stamp duty, road maintenance) is held in `evidence/research/kenya-2026/finance-act-2026-extract.md`.

> Finance Act, 2026 extract contributed by CPA Julian Njoroge Maina, 25241.

## Sources

1. Income Tax Act, Chapter 470 (not re-read in this update; read date unverified)
2. Tax Procedures Act 2015 (not re-read in this update; read date unverified)
3. Finance Act 2023, Finance Act 2024 (not re-read in this update; read date unverified)
4. KRA, read 2026-10-31 -- https://www.kra.go.ke
5. Income Tax Act, s15(2)(ae) (section text not re-read in this update; read date unverified)
6. KRA PAYE page, read 2026-10-31 -- https://www.kra.go.ke/individual/filing-paying/types-of-taxes/paye
7. KRA public notice on insurance relief and SHIF, 8 November 2024, read 2026-10-31 -- https://www.kra.go.ke/news-center/public-notices/2152-applicability-of-insurance-relief-to-contributions-made-to-the-social-health-insurance-fund-shif
8. Finance Act, 2026, Kenya Gazette Supplement No. 157 (Acts No. 19), 26 June 2026, text as held in evidence/research/kenya-2026/finance-act-2026-extract.md, read 2026-11-01
9. EY Global Tax Alert 2026-1445, read 2026-11-01 (secondary, confirms assent and the 1 January 2027 filing date) -- https://taxnews.ey.com/news/2026-1445-kenya-enacts-finance-act-2026

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA(K), registered tax agent, or equivalent licensed practitioner in Kenya) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
