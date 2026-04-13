---
name: za-income-tax
description: Use this skill whenever asked about South African income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "ITR12", "income tax return", "SARS", "tax brackets", "provisional tax", "IRP6", "rebates", "medical credits", "retirement deduction", "turnover tax", "eFiling", or any question about filing or computing income tax for a self-employed or sole proprietor client in South Africa. ALWAYS read this skill before touching any South African income tax work.
version: 2.0
---

# South Africa Income Tax -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | South Africa |
| Tax type | Income tax (normal tax) on trade income |
| Primary legislation | Income Tax Act 58 of 1962 |
| Supporting legislation | Tax Administration Act 28 of 2011; Sixth Schedule (Turnover Tax); Fourth Schedule (Provisional Tax) |
| Tax authority | SARS (South African Revenue Service) |
| Filing portal | SARS eFiling (www.sarsefiling.co.za) |
| Currency | ZAR only |
| Tax year | 1 March -- 28 February |
| Return form | ITR12 |
| Provisional tax | IRP6 (1st: 31 Aug, 2nd: last day Feb, 3rd voluntary: 30 Sep) |
| Primary rebate | R17,235 |
| Secondary rebate (65+) | R9,444 |
| Tertiary rebate (75+) | R3,145 |
| Retirement fund deduction | 27.5% of greater of remuneration/taxable income, cap R350,000 |
| Turnover tax | Available for non-professional services, turnover up to R1,000,000 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires SA registered tax practitioner sign-off |
| Validation date | Pending |

**Progressive tax table (2025/2026 year of assessment):**

| Taxable income (ZAR) | Rate |
|---|---|
| 1--237,100 | 18% |
| 237,101--370,500 | R42,678 + 26% above R237,100 |
| 370,501--512,800 | R77,362 + 31% above R370,500 |
| 512,801--673,000 | R121,475 + 36% above R512,800 |
| 673,001--857,900 | R179,147 + 39% above R673,000 |
| 857,901--1,817,000 | R251,258 + 41% above R857,900 |
| 1,817,001+ | R644,489 + 45% above R1,817,000 |

**Tax thresholds (below = no tax):**

| Age | Threshold |
|---|---|
| Below 65 | R95,750 |
| 65--74 | R148,217 |
| 75+ | R165,689 |

**Medical tax credits (s6A, 2025/2026):**

| Member | Monthly |
|---|---|
| Main member | R364 |
| First dependant | R364 |
| Each additional | R246 |

**Turnover tax table (Sixth Schedule):**

| Turnover (ZAR) | Rate |
|---|---|
| 0--335,000 | 0% |
| 335,001--500,000 | 1% above R335,000 |
| 500,001--750,000 | R1,650 + 2% above R500,000 |
| 750,001--1,000,000 | R6,650 + 3% above R750,000 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown age | STOP -- age determines rebates and threshold |
| Unknown expense category | Not deductible |
| Unknown business-use proportion | 0% |
| Unknown whether home office qualifies | Not deductible (IN 28 strict) |
| Entertainment expenses | NOT deductible (s23(m)) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year (1 March -- 28 February). Acceptable from: FNB (First National Bank), Standard Bank, Nedbank, Absa, Capitec, Investec, Discovery Bank, TymeBank, or fintech (Revolut, Wise).

**Recommended** -- invoices, IRP6 payment records, medical aid statements, RA contribution certificates, vehicle logbook.

**Ideal** -- complete bookkeeping, prior year ITR12, IT34 (assessment), asset register.

### Refusal catalogue

**R-ZA-1 -- Company/CC/Trust.** *Trigger:* client is a company, close corporation, or trust. *Message:* "This skill covers sole proprietors only. Companies file ITR14 at 27% corporate rate. Trusts file ITR12T."

**R-ZA-2 -- Foreign income.** *Trigger:* significant foreign income. *Message:* "Foreign income, s10(1)(o)(ii) exemption, and DTA analysis are outside scope. Consult a registered tax practitioner."

**R-ZA-3 -- Capital gains tax.** *Trigger:* disposal of capital assets. *Message:* "Capital gains tax is outside scope."

**R-ZA-4 -- Age unknown.** *Trigger:* age not provided. *Message:* "I cannot compute without knowing your age -- it determines rebates and tax threshold."

---

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 South African banks (fees and interest)

| Pattern | Treatment | Notes |
|---|---|---|
| FNB, FIRST NATIONAL BANK | Bank charges: deductible | Business account fees |
| STANDARD BANK, SBSA | Bank charges: deductible | Same |
| NEDBANK | Bank charges: deductible | Same |
| ABSA | Bank charges: deductible | Same |
| CAPITEC | Bank charges: deductible | Same |
| INVESTEC | Bank charges: deductible | Same |
| DISCOVERY BANK, TYMEBANK | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| INTEREST (credit) | Taxable income up to exemption (R23,800 <65; R34,500 65+); excess = taxable | Interest exemption applies |
| INTEREST (debit) | Deductible if business loan | Personal: NOT deductible |
| LOAN, HOME LOAN (principal) | EXCLUDE | Principal movement |

### 3.2 SA government and statutory bodies

| Pattern | Treatment | Notes |
|---|---|---|
| SARS | EXCLUDE | Tax payment (provisional/income) |
| UIF, UNEMPLOYMENT INSURANCE | Deductible if employer contribution | Employee-related |
| COIDA, COMPENSATION FUND | Deductible | Workers compensation |
| CIPC | Deductible | Company/IP registration |

### 3.3 SA utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| ESKOM, CITY POWER, CITY OF [JHB/CPT/DBN] | Deductible if business premises | Electricity/rates; apportion if home |
| RAND WATER | Deductible if business premises | Water |
| VODACOM, MTN, CELL C, TELKOM, RAIN | Deductible: business phone/internet | Mixed: apportion |

### 3.4 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| HOLLARD, SANTAM, OLD MUTUAL, MOMENTUM, OUTSURANCE | Deductible if business insurance | Personal: NOT deductible |
| DISCOVERY HEALTH, BONITAS, GEMS, MEDIHELP | NOT deductible from income | Medical = s6A/s6B credits (against tax, not income) |

### 3.5 SaaS and software -- international

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | Foreign SaaS |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.6 Professional services (SA)

| Pattern | Treatment | Notes |
|---|---|---|
| ACCOUNTANT, AUDIT, CA(SA) | Deductible | Accounting/audit fees |
| ATTORNEY, ADVOCATE, LAW FIRM | Deductible if business | Legal fees |
| TAX PRACTITIONER | Deductible | Tax advisory |

### 3.7 Retirement contributions

| Pattern | Treatment | Notes |
|---|---|---|
| ALLAN GRAY, CORONATION, 10X, SYGNIA, NINETY ONE | s11F deduction: 27.5% of taxable income, cap R350,000 | RA contributions |
| OLD MUTUAL RA, MOMENTUM RA, LIBERTY RA | Same | RA fund |

### 3.8 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| KULULA, FLYSAFAIR, AIRLINK, SAA | Deductible if business travel | Flights |
| UBER, BOLT | Deductible if business | Ride services |
| ENGEN, SHELL, BP, SASOL, CALTEX, TOTAL | Deductible: business vehicle portion only | Fuel; requires logbook |
| AVIS, EUROPCAR, HERTZ | Deductible if business | Rental car |
| SANRAL, E-TOLL | Deductible: business travel portion | Toll fees |

### 3.9 Office and supplies

| Pattern | Treatment | Notes |
|---|---|---|
| INCREDIBLE CONNECTION, MATRIX, TAKEALOT | Deductible or wear-and-tear depending on value | IT equipment |
| OFFICE NATIONAL, WALTONS | Deductible | Stationery |
| POSTNET, SA POST OFFICE | Deductible | Postage/courier |
| MAKRO, GAME | Deductible if business supplies | Verify business purpose |

### 3.10 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| PICK N PAY, WOOLWORTHS, CHECKERS, SPAR, SHOPRITE | Default: NOT deductible | Personal provisioning |
| RESTAURANT (any) | NOT deductible -- s23(m) | Entertainment blocked for sole proprietors |

### 3.11 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| DRAWINGS, OWNER | EXCLUDE | Personal drawings |
| DEPOSIT, OWN DEPOSIT | EXCLUDE | Capital injection |

---

## Section 4 -- Worked examples

### Example 1 -- Standard self-employed, mid-range

**Input:** Age 35, revenue R600,000, expenses R180,000, RA R80,000, medical R3,500/mo (main + 1 dependant), provisional paid R40,000.
**Computation:** Net profit R420,000. s11F = 27.5% x R420,000 = R115,500. Taxable = R304,500. Tax = R42,678 + 26% x R67,400 = R60,202. Less rebate R17,235. Less medical credit R8,736 (R364 x 2 x 12). Net = R34,231. Less provisional R40,000. Refund R5,769.

### Example 2 -- Turnover tax

**Input:** Non-professional sole proprietor, turnover R650,000.
**Computation:** Tax = R1,650 + 2% x R150,000 = R4,650 total.

### Example 3 -- Entertainment disallowed

**Input:** Client claims R15,000 client entertainment dinners.
**Result:** NOT deductible. s23(m) denies for sole proprietors. Remove.

### Example 4 -- Retirement cap exceeded

**Input:** Taxable income R2,000,000, RA R600,000.
**Computation:** 27.5% x R2,000,000 = R550,000 but cap R350,000. Deduction = R350,000. Excess R250,000 carries forward.

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Progressive rates
Apply rate table to taxable income. One table for all individuals regardless of marital status. **Legislation:** Income Tax Act, rates schedule.

### 5.2 Rebates
Primary R17,235 (all). Secondary R9,444 (65+). Tertiary R3,145 (75+). Credits against tax, not deductions from income. **Legislation:** s6.

### 5.3 Interest exemption
R23,800 (under 65). R34,500 (65+). Excess is taxable. **Legislation:** s10(1)(i).

### 5.4 s11F retirement deduction
27.5% of greater of remuneration or taxable income (before deduction). Cap R350,000. Excess carries forward or adds to tax-free retirement lump sum (R550,000). **Legislation:** s11F.

### 5.5 Medical tax credits (s6A)
Main + first dependant: R364/mo each. Additional: R246/mo. Credit against tax. NOT a deduction from income. **Legislation:** s6A.

### 5.6 Provisional tax (IRP6)
Based on estimated current year. 1st: 31 Aug (50%). 2nd: last day Feb (top-up to 100%). 3rd voluntary: 30 Sep. Under-estimation: 20% penalty if < 90% of actual (income < R1M) or 80% (> R1M). **Legislation:** Fourth Schedule.

### 5.7 Turnover tax
Non-professional services, turnover up to R1M. Replaces income tax, CGT, dividends tax, VAT. Cannot claim normal deductions. **Legislation:** Sixth Schedule.

### 5.8 Wear-and-tear (s11(e))
Based on SARS IN 47 useful life tables. Not straight-line -- based on write-off period. **Legislation:** s11(e).

### 5.9 Entertainment
NOT deductible for sole proprietors. s23(m) expressly disallows. **Legislation:** s23(m).

### 5.10 Home office
Dedicated room, regularly and exclusively for trade. IN 28 is strict. Dual-use rooms: NO deduction. Proportion = room area / total home. **Legislation:** s11(a), IN 28.

### 5.11 Record keeping
5 years from submission. Invoices, receipts, bank statements, logbooks, asset register. **Legislation:** TAA s29-32.

---

## Section 6 -- Tier 2 catalogue

### 6.1 Home office qualification
*Why:* IN 28 requires regular and exclusive use. *Default:* NOT deductible. *Question:* "Is there a dedicated room used only for business?"

### 6.2 Motor vehicle logbook
*Why:* Business km unknown. *Default:* 0% business use. *Question:* "Do you have a logbook with date, destination, km, and purpose for each trip?"

### 6.3 Turnover tax vs normal tax
*Why:* Depends on expense level and qualification. *Default:* Present both. *Question:* "What are your total business expenses? Are you providing professional services?"

### 6.4 s6B additional medical expenses
*Why:* Complex, depends on age/disability. *Default:* Do not claim without reviewer. *Question:* "Age 65+? Disability? Out-of-pocket medical expenses?"

### 6.5 Bad debts
*Why:* Must prove irrecoverable. *Default:* Do not claim. *Question:* "Was this debt previously included in income? Is it truly irrecoverable?"

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"
Columns: Date, Counterparty, Description, Amount (ZAR), Category (Revenue/Expense/Wear-and-tear/RA/Medical/EXCLUDE), Deductible amount, Default?, Question, Notes.

### Sheet "ITR12 Computation"
Step-by-step per Section 5: gross income, deductions, taxable income, tax, rebates, medical credits, provisional tax offset.

---

## Section 8 -- Bank statement reading guide

**CSV formats.** FNB exports use comma CSV with DD/MM/YYYY. Standard Bank uses semicolons. Nedbank and Absa offer various formats. Common columns: Date, Description, Amount, Balance.

**SA-specific patterns.** "DEBICHECK" = authenticated debit order. "MAGTAPE" = batch payment. "SASWITCH" = ATM network. "PREPAID" = likely personal (airtime top-up). "MUNICIPALITY" = rates and taxes.

**Provisional tax.** Two/three payments per year to SARS. These are tax payments, not expenses. EXCLUDE.

**Medical aid.** Monthly debits to Discovery/Bonitas/etc. These are NOT deductible from income -- they generate s6A credits against tax.

**RA contributions.** Monthly debits to Allan Gray/Coronation/etc. Deductible under s11F with cap.

---

## Section 9 -- Onboarding fallback

### 9.1 Age
*Inference:* Not inferable. Always ask. *Fallback:* "What is your age at 28 February 2026?"

### 9.2 Residency
*Inference:* SA bank accounts suggest resident. *Fallback:* "Are you a South African tax resident?"

### 9.3 Business type
*Inference:* From counterparty patterns. *Fallback:* "What is your trade/profession?"

### 9.4 Turnover tax election
*Inference:* Not inferable. *Fallback:* "Have you elected turnover tax?"

### 9.5 Medical aid
*Inference:* Monthly medical aid debits. *Fallback:* "Are you on medical aid? How many dependants?"

### 9.6 RA contributions
*Inference:* Monthly RA debits. *Fallback:* "Do you contribute to a retirement annuity?"

### 9.7 Provisional tax paid
*Inference:* SARS payments in statement. *Fallback:* "What IRP6 amounts have you paid?"

---

## Section 10 -- Reference material

### Test suite

**Test 1 -- Mid-range.** Age 35, R600K revenue, R180K expenses, R80K RA, medical R3,500/mo. Net tax R34,231.
**Test 2 -- Senior.** Age 68, R200K revenue, R50K expenses, R30K RA. Below threshold. R0 tax.
**Test 3 -- Turnover tax.** R650K turnover. Tax R4,650.
**Test 4 -- RA cap.** R2M taxable, R600K RA. Deduction R350,000. Excess carries forward.
**Test 5 -- Medical credits.** 6 members. R20,544/year credit.
**Test 6 -- Under-estimation penalty.** R200K estimated, R450K actual. Penalty R12,406.

### Edge case registry

**EC1 -- Interest exemption.** R23,800 <65 / R34,500 65+. Excess taxable.
**EC2 -- Turnover tax + professional.** NOT eligible.
**EC3 -- RA exceeds cap.** Excess carries forward.
**EC4 -- Home office dual use.** NOT deductible.
**EC5 -- Provisional under-estimation.** 20% penalty.
**EC6 -- Medical credits large family.** Compute per-member.
**EC7 -- Foreign income.** ESCALATE.
**EC8 -- Turnover tax exit mid-year.** Transition rules apply.
**EC9 -- Entertainment.** s23(m) blocks for sole proprietors.
**EC10 -- Assessed loss.** Carry forward under s20; SARS may query.

### Prohibitions

- NEVER compute without knowing age
- NEVER apply tax below age-threshold
- NEVER allow entertainment deductions for sole proprietors
- NEVER deduct RA above R350,000 cap
- NEVER allow turnover tax for professional services
- NEVER use prior year income for provisional tax (SA uses estimated current year)
- NEVER treat medical credits as income deductions
- NEVER allow home office for dual-use rooms
- NEVER allow income tax as a deduction
- NEVER present calculations as definitive

### Sources

1. Income Tax Act 58 of 1962
2. Tax Administration Act 28 of 2011
3. SARS Interpretation Notes (IN 28, IN 47, IN 14)
4. SARS eFiling -- https://www.sarsefiling.co.za

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CA(SA), or equivalent licensed practitioner in South Africa) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
