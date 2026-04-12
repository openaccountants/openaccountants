---
name: ro-income-tax
description: >
  Use this skill whenever asked about Romanian income tax for self-employed individuals (PFA). Trigger on phrases like "how much tax do I pay", "Declarația Unică", "PFA tax", "norma de venit", "impozit pe venit", "CAS", "CASS", "self-employed tax Romania", or any question about filing or computing income tax for a self-employed or freelance client in Romania. ALWAYS read this skill before touching any Romanian income tax work.
version: 2.0
jurisdiction: RO
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Romania Income Tax (Declarația Unică) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Romania (România) |
| Tax type | Impozit pe venit (income tax on independent activities) |
| Primary legislation | Codul Fiscal (Legea 227/2015), Titlul IV |
| Supporting legislation | Codul de Procedură Fiscală (Legea 207/2015); OUG 168/2022; Legea 239/2025 |
| Tax authority | ANAF (Agenția Națională de Administrare Fiscală) |
| Filing portal | SPV (Spațiul Privat Virtual) / declaratii.anaf.ro |
| Currency | RON only |
| Income tax rate | 10% flat on net income |
| CAS (pension) | 25% on threshold tiers (RON 48,600 / 97,200) |
| CASS (health) | 10% on threshold tiers (RON 24,300 / 48,600 / 97,200) |
| Filing deadline | 25 May of the following year |
| Minimum wage (2025) | RON 4,050/month |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Romanian expert contabil or consultant fiscal sign-off |
| Validation date | Pending |

**Income determination methods:**

| Method | Tax base | Bookkeeping |
|---|---|---|
| Sistem real | Revenue - documented expenses | Full daňová evidence required |
| Norma de venit | Fixed deemed amount by CAEN/county | Revenue records only |

**CAS/CASS threshold tiers (2025):**

| Threshold | CAS (25%) | CASS (10%) |
|---|---|---|
| Below 6x min wage (RON 24,300) | Optional | Mandatory minimum RON 2,430 |
| 6x--12x (RON 24,300--48,600) | Optional | RON 2,430 |
| 12x--24x (RON 48,600--97,200) | RON 12,150 | RON 4,860 |
| Above 24x (RON 97,200+) | RON 24,300 | RON 9,720 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown entity type | STOP -- PFA vs SRL changes everything |
| Unknown income method | STOP -- sistem real vs norma |
| Unknown expense category | Not deductible |
| Unknown CAEN code for norma | STOP -- norma varies by code and county |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year. Acceptable from: BCR (Banca Comercială Română), BRD (Groupe Société Générale), Banca Transilvania, ING Romania, Raiffeisen Romania, CEC Bank, or fintech (Revolut, Wise).

**Recommended** -- invoices, CAEN code, county (județ), chosen income method, prior year Declarația Unică.

**Ideal** -- complete bookkeeping, norma de venit published amount, CAS/CASS payment statements.

### Refusal catalogue

**R-RO-1 -- SRL.** *Trigger:* client is a limited company. *Message:* "This skill covers PFA/II/IF only. SRL files corporate income tax (impozit pe profit) or micro-enterprise tax. Please use a separate skill."

**R-RO-2 -- International income.** *Trigger:* significant foreign income. *Message:* "International income is outside scope. Consult a consultant fiscal."

**R-RO-3 -- Crypto.** *Trigger:* crypto trading income. *Message:* "Crypto taxation is outside scope."

**R-RO-4 -- Income method unknown.** *Trigger:* not confirmed. *Message:* "I cannot compute without knowing: sistem real or norma de venit?"

---

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 Romanian banks (fees and interest)

| Pattern | Treatment | Notes |
|---|---|---|
| BCR, BANCA COMERCIALĂ ROMÂNĂ | Bank charges: deductible (sistem real) | Monthly fees |
| BRD, GROUPE SOCIÉTÉ GÉNÉRALE | Bank charges: deductible | Same |
| BANCA TRANSILVANIA, BT | Bank charges: deductible | Same |
| ING BANK ROMANIA | Bank charges: deductible | Same |
| RAIFFEISEN BANK ROMANIA | Bank charges: deductible | Same |
| CEC BANK | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| DOBÂNDĂ (interest credit) | EXCLUDE from independent activity income | Capital income |
| DOBÂNDĂ (interest debit) | Deductible if business loan | Personal: EXCLUDE |
| CREDIT, ÎMPRUMUT (principal) | EXCLUDE | Loan principal |

### 3.2 Romanian government and statutory bodies

| Pattern | Treatment | Notes |
|---|---|---|
| ANAF | EXCLUDE | Tax payment |
| IMPOZIT PE VENIT | EXCLUDE | Income tax payment |
| CAS, CASA NAȚIONALĂ DE PENSII | Deductible from gross income (sistem real) | Pension contribution |
| CASS, CASA NAȚIONALĂ DE SĂNĂTATE | Deductible from gross income (sistem real) | Health contribution |
| REGISTRUL COMERȚULUI, ONRC | Deductible | Registration fees |

### 3.3 Romanian utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| ENEL, E-DISTRIBUȚIE, ELECTRICA | Deductible if business premises | Electricity; apportion if home |
| ENGIE, E.ON ENERGIE | Deductible if business premises | Gas |
| ORANGE RO, VODAFONE RO, DIGI, RCS & RDS | Deductible: business phone/internet | Mixed: apportion |
| TELEKOM ROMANIA | Deductible: business phone/internet | Mixed: apportion |

### 3.4 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| ALLIANZ-ȚIRIAC, EUROINS, GROUPAMA, OMNIASIG | Deductible if business insurance | Personal: NOT deductible |
| ASIGURARE AUTO (RCA/CASCO) | Deductible: business vehicle portion | Personal vehicle: NOT deductible |

### 3.5 SaaS and software -- international

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | EU reverse charge TVA |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.6 Professional services (Romania)

| Pattern | Treatment | Notes |
|---|---|---|
| CONTABIL, CONTABILITATE, EXPERT CONTABIL | Deductible | Accounting fees |
| AVOCAT, CABINET AVOCAT | Deductible if business | Legal fees |
| NOTAR, BIROU NOTARIAL | Deductible if business | Notary fees |
| CONSULTANT FISCAL | Deductible | Tax advisory |

### 3.7 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| CFR CĂLĂTORI | Deductible if business | Train |
| TAROM, WIZZAIR, RYANAIR | Deductible if business travel | Flights |
| UBER, BOLT | Deductible if business | Ride services |
| PETROM, OMV, MOL, ROMPETROL, LUKOIL | Deductible: business vehicle portion | Fuel |

### 3.8 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| KAUFLAND, LIDL, CARREFOUR, MEGA IMAGE, AUCHAN | Default: NOT deductible | Personal provisioning |
| RESTAURANT, PENSIUNE | Protocol expenses: limited to 2% of adjusted gross income | Must document business purpose |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER PROPRIU, OWN TRANSFER | EXCLUDE | Internal |
| NUMERAR, ATM | EXCLUDE (default: drawings) | Ask client |
| DEPUNERE | EXCLUDE | Owner deposit |

---

## Section 4 -- Worked examples

### Example 1 -- PFA sistem real, mid-range

**Input:** CAEN 6201, revenue RON 200,000, expenses RON 70,000 (including prior CAS/CASS).
**Computation:** Net income = RON 130,000. Tax = 10% x RON 130,000 = RON 13,000. CAS = 25% x RON 97,200 = RON 24,300 (above 24x). CASS = 10% x RON 48,600 = RON 4,860. Total = RON 42,160.

### Example 2 -- PFA norma de venit

**Input:** Taxi driver, Bucharest, norma = RON 32,000.
**Computation:** Tax = RON 3,200. CAS optional (below RON 48,600). CASS = RON 2,430 (mandatory minimum). Total (no CAS) = RON 5,630.

### Example 3 -- Low-income mandatory CASS

**Input:** Net income RON 18,000.
**Computation:** Tax = RON 1,800. CAS optional. CASS = RON 2,430 (mandatory minimum). Total = RON 4,230.

### Example 4 -- Part-year PFA

**Input:** Registered July 2025 (6 months), net income RON 30,000.
**Computation:** Tax = RON 3,000. CAS prorated: 6/12 x RON 48,600 = RON 24,300 threshold. RON 30,000 > RON 24,300, so CAS = 25% x RON 24,300 = RON 6,075. CASS prorated similarly = RON 1,215. Total = RON 10,290.

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Income tax rate
Flat 10% on net income from independent activities. No progressive bands. **Legislation:** Codul Fiscal, Art. 68-69.

### 5.2 Sistem real
Net income = gross revenue - deductible expenses. CAS/CASS paid are deductible. Expenses must be documented and incurred for business purpose. Protocol/entertainment limited to 2% of adjusted gross income. **Legislation:** Art. 68.

### 5.3 Norma de venit
Fixed deemed income by CAEN code and county. Published by ANAF by 15 February. Tax = 10% x norma. Actual revenue/expenses irrelevant. Available only for specific CAEN codes. **Legislation:** Art. 69.

### 5.4 CAS thresholds
Fixed amounts based on tier brackets, NOT percentage of actual income. Below RON 48,600: optional. RON 48,600--97,200: RON 12,150. Above RON 97,200: RON 24,300. **Legislation:** Art. 148-154.

### 5.5 CASS thresholds
Mandatory even if income is zero. Minimum RON 2,430. Tiers at RON 24,300/48,600/97,200. **Legislation:** Art. 170-174.

### 5.6 Part-year proration
CAS/CASS thresholds prorated by months of registration. **Legislation:** Codul Fiscal.

### 5.7 Record keeping
Sistem real: full accounting records. Norma: revenue records only. Retention: 5 years. **Legislation:** Codul de Procedură Fiscală.

---

## Section 6 -- Tier 2 catalogue

### 6.1 Norma vs sistem real comparison
*Why:* Depends on actual profit vs deemed amount. *Default:* Present both. *Question:* "What is the published norma for your CAEN code and county?"

### 6.2 SRL micro vs PFA comparison
*Why:* Total cost differs significantly including dividend extraction tax. Threshold drops to EUR 100,000 in 2026. *Default:* Flag for reviewer. *Question:* "Are you considering SRL structure? Revenue level?"

### 6.3 Multiple CAEN codes
*Why:* Norma applies only to qualifying activities; others must use sistem real. *Default:* Flag for reviewer. *Question:* "Do you have multiple CAEN codes? Which have published norma?"

### 6.4 Minimum wage increase impact
*Why:* CAS/CASS thresholds tied to minimum wage. *Default:* Use RON 4,050 (2025). *Question:* "Confirm current minimum wage if mid-year change occurred."

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"
Columns: Date, Counterparty, Description, Amount (RON), Category (Revenue/Expense/CAS/CASS/EXCLUDE), Deductible amount, Default?, Question, Notes.

### Sheet "Tax Computation"
Branches by method: sistem real or norma de venit. Includes CAS/CASS tier determination.

---

## Section 8 -- Bank statement reading guide

**CSV formats.** BCR exports use semicolons with DD.MM.YYYY. BRD uses CSV with comma delimiters. Banca Transilvania offers various formats. Common columns: Data (Date), Beneficiar/Ordonator (Counterparty), Suma (Amount), Sold (Balance).

**Romanian language variants.** Common: transfer (transfer), depunere (deposit), retragere (withdrawal), comision (commission), dobândă (interest), factură (invoice), plată (payment), chirie (rent).

**CAS/CASS payments.** Payments to ANAF labelled "CAS" or "CASS". These are deductible from gross income under sistem real.

**Tax payments.** Impozit pe venit payments to ANAF: EXCLUDE (not deductible).

**Foreign currency.** Convert to RON at BNR (National Bank) rate on transaction date.

---

## Section 9 -- Onboarding fallback

### 9.1 Entity type
*Inference:* PFA from bank account name. *Fallback:* "Are you a PFA, II, IF, or SRL?"

### 9.2 Income method
*Inference:* Not inferable. Always ask. *Fallback:* "Sistem real or norma de venit?"

### 9.3 CAEN code
*Inference:* From counterparty mix. *Fallback:* "What is your CAEN activity code?"

### 9.4 County (județ)
*Inference:* From bank branch or address. *Fallback:* "Which county (județ) are you registered in? (Affects norma de venit.)"

### 9.5 VAT status
*Inference:* TVA payments in statement. *Fallback:* "Are you TVA registered?"

### 9.6 Other income
*Inference:* Salary credits. *Fallback:* "Do you have employment income? (Affects CAS/CASS.)"

---

## Section 10 -- Reference material

### Test suite

**Test 1 -- Sistem real, mid-range.** Revenue RON 200,000, expenses RON 70,000. Tax RON 13,000 + CAS RON 24,300 + CASS RON 4,860 = RON 42,160.
**Test 2 -- Norma de venit taxi.** Norma RON 32,000. Tax RON 3,200 + CASS RON 2,430 = RON 5,630.
**Test 3 -- Low income, mandatory CASS.** RON 18,000 net. Tax RON 1,800 + CASS RON 2,430 = RON 4,230.
**Test 4 -- High income, all caps.** RON 500,000 net. Tax RON 50,000 + CAS RON 24,300 + CASS RON 9,720 = RON 84,020.
**Test 5 -- Part-year.** 6 months, RON 30,000. Tax RON 3,000 + prorated CAS/CASS.

### Edge case registry

**EC1 -- CAS between thresholds.** Fixed at tier amount, not percentage of actual income.
**EC2 -- Low income, CASS still mandatory.** Minimum RON 2,430 even if income is zero.
**EC3 -- Norma vs sistem real.** Compare both.
**EC4 -- SRL micro vs PFA.** Include dividend extraction cost.
**EC5 -- Multiple CAEN codes.** Separate norma and sistem real activities.
**EC6 -- CAS/CASS deductibility timing.** Deductible in year paid.
**EC7 -- Micro threshold exceeded.** Exit to impozit pe profit.
**EC8 -- Part-year proration.** CAS/CASS thresholds prorated.
**EC9 -- PFA with employment.** Separate CAS/CASS calculations.
**EC10 -- Minimum wage change.** Verify threshold basis.

### Prohibitions

- NEVER apply progressive rates -- Romania uses flat 10%
- NEVER ignore mandatory CASS minimum
- NEVER confuse CAS thresholds with percentage of actual income
- NEVER apply norma to CAEN codes without published norma
- NEVER use micro-enterprise rules for PFA
- NEVER forget to prorate for part-year
- NEVER advise on crypto, international income, or transfer pricing
- NEVER present calculations as definitive
- NEVER assume micro EUR 250,000 threshold is stable (drops to EUR 100,000 in 2026)

### Sources

1. Codul Fiscal (Legea 227/2015)
2. Codul de Procedură Fiscală (Legea 207/2015)
3. OUG 168/2022
4. Legea 239/2025
5. ANAF -- https://www.anaf.ro

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert contabil or consultant fiscal in Romania) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
