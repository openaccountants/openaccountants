---
name: ke-income-tax
description: Use this skill whenever asked about Kenyan income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "KRA", "iTax", "income tax return", "personal relief", "insurance relief", "turnover tax", "presumptive tax", "self-employed tax Kenya", or any question about filing or computing income tax for a self-employed or sole proprietor client in Kenya. ALWAYS read this skill before touching any Kenyan income tax work.
version: 2.0
---

# Kenya Income Tax -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Kenya |
| Tax type | Income tax on business income (self-assessment) |
| Primary legislation | Income Tax Act, Chapter 470 |
| Supporting legislation | Tax Procedures Act 2015; Finance Act 2023; Finance Act 2024 |
| Tax authority | KRA (Kenya Revenue Authority) |
| Filing portal | iTax (itax.kra.go.ke) |
| Currency | KES only |
| Return form | Self-assessment return |
| Filing deadline | 30 June of the following year |
| Instalment tax | Quarterly (20th of 4th, 6th, 9th, 12th months) |
| Personal relief | KES 28,800/year (credit against tax) |
| Insurance relief | 15% of qualifying premiums, cap KES 60,000/year |
| Turnover tax | 1.5% on gross turnover KES 1M--25M (non-professional) |
| Presumptive tax | KES 15,000/year (turnover below KES 1M) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Kenyan CPA or registered tax agent sign-off |
| Validation date | Pending |

**Progressive tax table (resident, annual):**

| Taxable income (KES) | Rate |
|---|---|
| 0--288,000 | 10% |
| 288,001--388,000 | 25% |
| 388,001--6,000,000 | 30% |
| 6,000,001--9,600,000 | 32.5% |
| 9,600,001+ | 35% |

**Wear-and-tear rates (reducing balance):**

| Asset | Rate |
|---|---|
| Heavy/self-propelling machinery | 37.5% |
| Computer/IT equipment | 30% |
| Motor vehicles | 25% |
| Furniture and fittings | 12.5% |
| Farm machinery | 100% |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown residency | STOP -- non-residents pay flat 30% |
| Unknown expense category | Not deductible |
| Unknown business-use proportion | 0% |
| Unknown whether turnover tax is elected | Normal tax |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year. Acceptable from: Equity Bank, KCB (Kenya Commercial Bank), Co-operative Bank, NCBA, Standard Chartered Kenya, Absa Kenya, I&M Bank, DTB, or mobile money (M-Pesa via Safaricom).

**Recommended** -- invoices, insurance premium certificates, instalment tax payment records, PIN certificate, WHT certificates.

**Ideal** -- complete bookkeeping, prior year return, iTax account records.

### Refusal catalogue

**R-KE-1 -- Company/LLP.** *Trigger:* client is a limited company or LLP. *Message:* "This skill covers self-employed individuals only. Companies file corporate returns at 30%."

**R-KE-2 -- Non-resident.** *Trigger:* non-resident status. *Message:* "Non-residents pay flat 30% on Kenya-source income with no personal relief. This skill covers residents only."

**R-KE-3 -- Cross-border/WHT.** *Trigger:* complex withholding tax or treaty questions. *Message:* "Cross-border WHT and treaty analysis are outside scope. Consult a tax practitioner."

**R-KE-4 -- Capital gains.** *Trigger:* property disposal. *Message:* "Capital gains tax (15%) is outside scope."

---

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 Kenyan banks (fees and interest)

| Pattern | Treatment | Notes |
|---|---|---|
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

| Pattern | Treatment | Notes |
|---|---|---|
| MPESA, M-PESA, SAFARICOM | Transaction fees: deductible | Business M-Pesa charges |
| MPESA PAYBILL, TILL NO | Revenue if incoming; deductible if outgoing business payment | Verify nature |
| MPESA FLOAT, B2C, C2B | EXCLUDE if internal movement | Business float management |
| AIRTEL MONEY | Same as M-Pesa | Alternative mobile money |

### 3.3 Kenyan government and statutory bodies

| Pattern | Treatment | Notes |
|---|---|---|
| KRA, KENYA REVENUE AUTHORITY | EXCLUDE | Tax payment |
| NSSF, NATIONAL SOCIAL SECURITY | Deductible (up to statutory limit) | Provident fund contribution |
| SHIF, SOCIAL HEALTH INSURANCE | NOT deductible for income tax | Separate health levy |
| NHIF (legacy) | NOT deductible | Replaced by SHIF |
| COUNTY GOVERNMENT, NAIROBI COUNTY | Deductible if business licence/permit | Business licence fees |

### 3.4 Kenyan utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| KENYA POWER, KPLC | Deductible if business premises | Electricity; apportion if home |
| NAIROBI WATER, ELDOWAS | Deductible if business premises | Water |
| SAFARICOM, AIRTEL, TELKOM KENYA | Deductible: business phone/internet | Mixed: apportion |
| ZUKU, FAIBA | Deductible: business internet | Mixed: apportion |

### 3.5 SaaS and software -- international

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | International SaaS |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.6 Professional services (Kenya)

| Pattern | Treatment | Notes |
|---|---|---|
| ACCOUNTANT, CPA, AUDIT FIRM | Deductible | Accounting fees |
| ADVOCATE, LAW FIRM | Deductible if business | Legal fees |
| TAX AGENT | Deductible | Tax advisory |

### 3.7 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| KENYA AIRWAYS, JAMBOJET | Deductible if business travel | Flights |
| UBER, BOLT, LITTLE CAB | Deductible if business | Ride services |
| TOTAL, SHELL, RUBIS, VIVO ENERGY | Deductible: business vehicle portion | Fuel |
| SGR (Madaraka Express) | Deductible if business | Train |

### 3.8 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| JUBILEE, BRITAM, CIC, UAP, APA | Deductible if business insurance | Personal life/health: insurance RELIEF (not deduction) |
| INSURANCE PREMIUM (life/health/education) | Insurance relief: 15% of premiums, cap KES 60,000 | Credit against tax |

### 3.9 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| NAIVAS, CARREFOUR KE, QUICKMART | Default: NOT deductible | Personal provisioning |
| RESTAURANT | Deductible only if wholly and exclusively business | Must prove |

### 3.10 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| MPESA TO BANK, BANK TO MPESA | EXCLUDE | Own account transfer |
| DRAWINGS, PERSONAL | EXCLUDE | Owner drawings |

---

## Section 4 -- Worked examples

### Example 1 -- Standard self-employed, mid-range

**Input:** Resident, revenue KES 3,000,000, expenses KES 1,200,000, insurance premiums KES 100,000, instalment tax KES 150,000.
**Computation:** Taxable = KES 1,800,000. Tax = 28,800 + 25,000 + 423,600 = KES 477,400. Less personal relief 28,800. Less insurance relief min(15,000, 60,000) = 15,000. Net = KES 433,600. Less instalment KES 150,000. Due = KES 283,600.

### Example 2 -- Below personal relief

**Input:** Taxable income KES 200,000.
**Computation:** Tax = 10% x 200,000 = KES 20,000. Less relief KES 28,800. Payable = KES 0.

### Example 3 -- Turnover tax

**Input:** Non-professional trader, turnover KES 8,000,000.
**Computation:** TOT = 1.5% x KES 8,000,000 = KES 120,000/year.

### Example 4 -- Presumptive vs normal

**Input:** Small trader, turnover KES 500,000, expenses KES 350,000.
**Computation:** Normal: profit KES 150,000. Tax = 15,000 - 28,800 relief = KES 0. Presumptive: KES 15,000. Normal is better.

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Progressive rates
10%/25%/30%/32.5%/35%. Non-residents: flat 30%. **Legislation:** ITA Cap 470, Third Schedule.

### 5.2 Personal relief
KES 28,800/year. Credit against tax, NOT deduction from income. Available to all residents. **Legislation:** ITA.

### 5.3 Insurance relief
15% of qualifying premiums (life, health, education). Cap KES 60,000/year. Credit against tax. **Legislation:** s31.

### 5.4 Instalment tax
Quarterly: 25% each on 20th of 4th, 6th, 9th, 12th months. Based on estimated current year or prior year actual. If prior year tax < KES 40,000: not required. Under-estimation: 20% penalty. **Legislation:** s12.

### 5.5 Turnover tax
1.5% on gross turnover KES 1M--25M. Monthly filing. Replaces income tax. No expense deductions. Excludes professional/management services. **Legislation:** s12C.

### 5.6 Presumptive tax
KES 15,000/year for specified businesses under KES 1M turnover. Final tax. **Legislation:** s12D.

### 5.7 Wear-and-tear (capital deductions)
Reducing balance method. Heavy machinery: 37.5%. Computers: 30%. Vehicles: 25%. Furniture: 12.5%. Farm machinery: 100%. **Legislation:** Second Schedule.

### 5.8 NSSF/SHIF
NSSF (provident): deductible up to statutory limit. SHIF (health): NOT deductible for income tax. **Legislation:** Various acts.

### 5.9 WHT credits
Withholding tax on professional fees (5%) is a credit against final tax. Requires WHT certificates. **Legislation:** ITA.

### 5.10 Record keeping
5 years. English or Swahili. Paper or electronic. **Legislation:** Tax Procedures Act s23.

---

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

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"
Columns: Date, Counterparty, Description, Amount (KES), Category (Revenue/Expense/Capital/Insurance/EXCLUDE), Deductible amount, Default?, Question, Notes.

### Sheet "Tax Computation"
Progressive brackets. Reliefs. Instalment tax offset. WHT credits.

---

## Section 8 -- Bank statement reading guide

**CSV formats.** Equity Bank exports CSV with DD/MM/YYYY. KCB uses various formats. Co-op Bank uses semicolons. Common columns: Date, Description/Narration, Debit, Credit, Balance.

**M-Pesa integration.** Many transactions flow through M-Pesa. M-Pesa statements are separate from bank statements. Request both. M-Pesa shows: transaction ID, type (paybill/till/send money), recipient, amount.

**Kenyan-specific patterns.** "PAYBILL" = payment to business. "TILL" = payment at point of sale. "B2C" = business to customer. "C2B" = customer to business. "FULIZA" = overdraft (loan -- exclude principal). "KCB MPESA" = integrated mobile banking.

**WHT deductions.** Professional fees received may have 5% withheld. Gross up the income and claim WHT credit.

**Foreign currency.** Convert to KES at CBK (Central Bank of Kenya) rate on transaction date.

---

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

---

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
**EC6 -- SHIF deductibility.** NOT deductible.
**EC7 -- Capital gain on business asset.** ESCALATE.
**EC8 -- Non-resident consulting.** 20% WHT (or treaty rate). ESCALATE.

### Prohibitions

- NEVER apply personal relief as deduction from income
- NEVER allow turnover tax for professional/management services
- NEVER allow insurance relief above KES 60,000
- NEVER compute non-residents with progressive rates
- NEVER allow capital expenditure as direct expense
- NEVER ignore WHT certificates
- NEVER treat SHIF as deductible
- NEVER present calculations as definitive

### Sources

1. Income Tax Act, Chapter 470
2. Tax Procedures Act 2015
3. Finance Act 2023, Finance Act 2024
4. KRA -- https://www.kra.go.ke

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA(K), registered tax agent, or equivalent licensed practitioner in Kenya) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
