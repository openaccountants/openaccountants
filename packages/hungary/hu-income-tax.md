---
name: hu-income-tax
description: >
  Use this skill whenever asked about Hungarian income tax for self-employed individuals (egyéni vállalkozó). Trigger on phrases like "how much tax do I pay", "SZJA", "personal income tax Hungary", "KATA", "átalányadózás", "flat-rate taxation", "egyéni vállalkozó", "self-employed tax Hungary", "SZOCHO", "TB járulék", or any question about filing or computing income tax for a self-employed or freelance client in Hungary. ALWAYS read this skill before touching any Hungarian income tax work.
version: 2.0
jurisdiction: HU
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Hungary Income Tax (SZJA) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Hungary (Magyarország) |
| Tax type | Személyi jövedelemadó (SZJA -- personal income tax) |
| Primary legislation | 1995. évi CXVII. törvény (SZJA Act) |
| Supporting legislation | 2022. évi XIII. törvény (KATA); 2019. évi CXXII. törvény (SZOCHO/TB) |
| Tax authority | Nemzeti Adó- és Vámhivatal (NAV) |
| Filing portal | NAV Online / eSZJA |
| Currency | HUF only |
| SZJA rate | 15% flat on all personal income |
| Vállalkozói jövedelemadó | 9% on entrepreneurial profit (standard regime) |
| KATA | HUF 50,000/month (B2C only, no employees) |
| SZOCHO | 13% social contribution tax |
| TB | 18.5% social insurance contribution |
| Filing deadline | 20 May of the following year |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Hungarian adótanácsadó sign-off |
| Validation date | Pending |

**Tax regime summary:**

| Regime | Tax on | Rate | Best for |
|---|---|---|---|
| KATA | Fixed monthly | HUF 50,000/mo | B2C services, low admin |
| Átalányadózás | Deemed income | 15% SZJA | Services with low real expenses |
| Standard (vállalkozói) | Actual profit | 9% + 15% on withdrawal | High-expense businesses |

**Átalányadó cost ratios:**

| Activity | Cost ratio |
|---|---|
| Retail (non-food) | 90% |
| Listed activities (hair, repair, taxi) | 80% |
| All other activities | 40% |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown tax regime | STOP -- must determine |
| Unknown expense category | Not deductible |
| Unknown ÖVTJ code for átalányadó | STOP -- ratio depends on code |
| Unknown client type for KATA | Assume company (disqualifies KATA) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year. Acceptable from: OTP Bank, K&H Bank, Erste Bank Hungary, CIB Bank, Raiffeisen HU, MBH Bank, or fintech (Revolut, Wise).

**Recommended** -- invoices, chosen regime confirmation, ÖVTJ code(s), NAV correspondence.

**Ideal** -- complete bookkeeping, prior year SZJA return, contribution statements.

### Refusal catalogue

**R-HU-1 -- Kft./Zrt.** *Trigger:* client is a limited company. *Message:* "This skill covers egyéni vállalkozó only. Kft. files corporate income tax (TAO). Please use a separate skill."

**R-HU-2 -- International income.** *Trigger:* significant foreign income. *Message:* "International income is outside scope. Consult an adótanácsadó."

**R-HU-3 -- Regime unknown.** *Trigger:* client has not confirmed KATA/átalányadó/standard. *Message:* "I cannot compute without knowing your chosen tax regime."

---

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 Hungarian banks (fees and interest)

| Pattern | Treatment | Notes |
|---|---|---|
| OTP BANK, OTP | Bank charges: deductible (standard regime) | Monthly fees |
| K&H BANK | Bank charges: deductible | Same |
| ERSTE BANK | Bank charges: deductible | Same |
| CIB BANK | Bank charges: deductible | Same |
| RAIFFEISEN | Bank charges: deductible | Same |
| MBH BANK, BUDAPEST BANK, TAKARÉKBANK | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| KAMAT (interest credit) | EXCLUDE from business income | Capital income (kamatjövedelem) |
| KAMAT (interest debit) | Deductible if business loan | Personal: EXCLUDE |
| HITEL, KÖLCSÖN (loan principal) | EXCLUDE | Principal movement |

### 3.2 Hungarian government and statutory bodies

| Pattern | Treatment | Notes |
|---|---|---|
| NAV, NEMZETI ADÓ | EXCLUDE | Tax payment |
| KATA BEFIZETÉS | EXCLUDE (if on KATA: this IS the tax) | KATA monthly payment |
| SZOCHO, TB JÁRULÉK | Deductible under standard regime | Social contributions |
| ÖNKORMÁNYZAT (municipality) | Deductible if IPA (local business tax) | IPA is deductible under standard |
| IPARŰZÉSI ADÓ, IPA | Deductible under standard regime | Local business tax |

### 3.3 Hungarian utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| MVM, ELMŰ-ÉMÁSZ, E.ON HU | Deductible if business premises | Electricity; apportion if home |
| FŐGÁZ, TIGÁZ | Deductible if business premises | Gas |
| TELEKOM (MAGYAR TELEKOM), TELENOR, VODAFONE HU, YETTEL | Deductible: business phone/internet | Mixed: apportion |
| DIGI, INVITEL | Deductible: business internet | Mixed: apportion |

### 3.4 SaaS and software -- international

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | EU reverse charge ÁFA |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.5 Professional services (Hungary)

| Pattern | Treatment | Notes |
|---|---|---|
| KÖNYVELŐ, KÖNYVELÉS | Deductible | Accounting fees |
| ÜGYVÉD | Deductible if business | Legal fees |
| KÖZJEGYZŐ | Deductible if business | Notary |
| ADÓTANÁCSADÓ | Deductible | Tax advisory |

### 3.6 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| MÁV, MÁVINFORM | Deductible if business | Train |
| BKK, BKV | Deductible if business | Budapest public transport |
| MOL, OMV, SHELL HU | Deductible: business portion | Fuel |
| WIZZAIR, RYANAIR | Deductible if business travel | Flights |
| BOLT, UBER | Deductible if business | Ride services |

### 3.7 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| TESCO, ALDI, LIDL HU, SPAR, PENNY | Default: NOT deductible | Personal provisioning |
| ÉTTEREM, RESTAURANT | Deductible if documented business | Representation with documentation |

### 3.8 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SAJÁT ÁTUTALÁS, OWN TRANSFER | EXCLUDE | Internal |
| KÉSZPÉNZFELVÉTEL, ATM | EXCLUDE (default: drawings) | Ask client |
| BEFIZETÉS | EXCLUDE | Owner deposit |

---

## Section 4 -- Worked examples

### Example 1 -- Átalányadó IT consultant

**Input:** Revenue HUF 18,000,000, 40% cost ratio, single.
**Computation:** Deemed costs = HUF 7,200,000. Taxable = HUF 10,800,000. SZJA = 15% = HUF 1,620,000. SZOCHO = 13% = HUF 1,404,000. TB = 18.5% = HUF 1,998,000.

### Example 2 -- KATA disqualification

**Input:** KATA freelancer invoices HUF 500,000 to a Kft. in March.
**Result:** Immediate KATA loss for entire year. Must re-file under standard or átalányadó. All income re-taxed.

### Example 3 -- Standard regime, two-layer

**Input:** Revenue HUF 30,000,000, expenses HUF 12,000,000, withdraws HUF 10,000,000.
**Computation:** Profit = HUF 18,000,000. Vállalkozói adó = 9% = HUF 1,620,000. SZJA on withdrawal = 15% x HUF 10,000,000 = HUF 1,500,000. SZOCHO on withdrawal = HUF 1,300,000. TB = HUF 1,850,000.

### Example 4 -- Minimum contribution trap

**Input:** Revenue HUF 1,500,000/year.
**Computation:** Monthly income HUF 125,000. Minimum base HUF 290,800. SZOCHO = HUF 37,804/mo. TB = HUF 53,798/mo. Annual contributions = HUF 1,099,224. This is 73% of revenue -- flag as potentially unviable.

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 SZJA rate
Flat 15% on all personal income. No progressive bands. **Legislation:** SZJA tv. § 8.

### 5.2 KATA rules (post-2022 reform)
B2C only -- ANY invoice to a legal entity disqualifies for the entire year. HUF 50,000/month (main) or HUF 25,000/month (auxiliary). Covers income tax + social contributions. Does NOT cover ÁFA or IPA. Revenue above HUF 12,000,000: must register for ÁFA. **Legislation:** 2022. évi XIII. törvény.

### 5.3 Átalányadózás
Revenue limit: HUF 24,000,000 (HUF 36,000,000 for listed retail). Max 1 employee. Cost ratios: 90%/80%/40%. Taxable = revenue x (1 - ratio). **Legislation:** SZJA tv. § 50-56.

### 5.4 Standard regime
Two-layer: 9% vállalkozói jövedelemadó on profit + 15% SZJA on withdrawn amounts. **Legislation:** SZJA tv. § 44-49.

### 5.5 Social contributions
SZOCHO: 13%. TB: 18.5% (pension 10%, health 4%, labour 3%, accident 1.5%). Minimum base: HUF 290,800 (no qualification) or HUF 348,800 (qualification required). Mandatory regardless of income. **Legislation:** 2019. évi CXXII. tv.

### 5.6 Local business tax (IPA)
Up to 2% of net revenue. Set by municipality. Applies to all regimes including KATA. Deductible from standard regime income. **Legislation:** 1990. évi C. tv.

### 5.7 Regime switching
Must notify NAV by 31 December of prior year. Cannot switch mid-year. **Legislation:** SZJA tv.

---

## Section 6 -- Tier 2 catalogue

### 6.1 Choosing between regimes
*Why:* Total burden (tax + contributions) varies significantly. *Default:* Present comparison. *Question:* "What are your actual expenses? Do you invoice businesses or individuals only?"

### 6.2 Mixed-activity cost ratios
*Why:* If multiple ÖVTJ codes, different ratios may apply. *Default:* Use 40% (conservative). *Question:* "What are your ÖVTJ activity codes?"

### 6.3 Dual KATA + employment
*Why:* Hours threshold (36/week) and B2C-only requirement. *Default:* Verify eligibility. *Question:* "How many hours/week are you employed? Are all KATA clients individuals?"

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"
Columns: Date, Counterparty, Description, Amount (HUF), Category, Deductible amount, Default?, Question, Notes.

### Sheet "Tax Computation"
Branches by regime: KATA, átalányadó, or standard.

---

## Section 8 -- Bank statement reading guide

**CSV formats.** OTP Bank exports semicolons with YYYY.MM.DD. K&H uses comma CSV. Erste uses semicolons. Common columns: Dátum (Date), Partner (Counterparty), Összeg (Amount), Egyenleg (Balance).

**Hungarian language variants.** Common: átutalás (transfer), befizetés (deposit), kifizetés (payment), díj (fee), kamat (interest), számla (invoice/account), bérleti díj (rent).

**KATA payments.** Monthly HUF 50,000 to NAV. If visible, confirms KATA status.

**IPA payments.** Twice yearly (March 15, September 15) to local municipality (önkormányzat).

---

## Section 9 -- Onboarding fallback

### 9.1 Entity type
*Inference:* Egyéni vállalkozó from bank account type. *Fallback:* "Are you an egyéni vállalkozó or Kft.?"

### 9.2 Tax regime
*Inference:* KATA payments = KATA. Átalányadó from NAV correspondence. *Fallback:* "Which tax regime: KATA, átalányadózás, or standard?"

### 9.3 Client base
*Inference:* Incoming from company names vs individuals. *Fallback:* "Do you invoice companies (Kft., Zrt.) or only individuals?"

### 9.4 ÖVTJ code
*Inference:* From trade licence or activity description. *Fallback:* "What is your ÖVTJ activity code?"

### 9.5 Employees
*Inference:* Salary outflows. *Fallback:* "Do you have employees?"

---

## Section 10 -- Reference material

### Test suite

**Test 1 -- Átalányadó IT, 40%.** Revenue HUF 18M. SZJA HUF 1,620,000. SZOCHO HUF 1,404,000. TB HUF 1,998,000.
**Test 2 -- KATA hairdresser.** B2C, HUF 8M. Annual KATA HUF 600,000. No SZJA return.
**Test 3 -- KATA disqualification.** Invoice to Kft. = full year re-tax.
**Test 4 -- Standard two-layer.** HUF 30M revenue, HUF 12M expenses, HUF 10M withdrawn. Vállalkozói 9% + SZJA 15% on withdrawal.
**Test 5 -- Minimum contribution trap.** HUF 1.5M/year. Contributions exceed 73% of revenue.

### Edge case registry

**EC1 -- KATA invoicing companies.** Immediate disqualification.
**EC2 -- Átalányadó revenue exceeded.** Lost for following year.
**EC3 -- Regime comparison.** Must include all contributions.
**EC4 -- Minimum contribution base.** Mandatory even if income is lower.
**EC5 -- KATA + employment hours.** Must be under 36/week.
**EC6 -- IPA deductibility.** Only under standard regime.
**EC7 -- ÁFA threshold with KATA.** HUF 12M triggers ÁFA registration but not KATA loss.
**EC8 -- Year-end regime switch.** Notify NAV by 31 December.

### Prohibitions

- NEVER allow KATA for taxpayers invoicing legal entities
- NEVER apply progressive rates -- Hungary uses flat 15% SZJA
- NEVER ignore minimum contribution base
- NEVER combine KATA with separate SZOCHO/TB
- NEVER allow mid-year regime switch
- NEVER forget IPA -- applies to all regimes
- NEVER deduct actual expenses under átalányadó
- NEVER confuse 9% vállalkozói adó with 15% SZJA
- NEVER present calculations as definitive
- NEVER advise on international structures or crypto

### Sources

1. 1995. évi CXVII. törvény (SZJA Act)
2. 2022. évi XIII. törvény (KATA)
3. 2019. évi CXXII. törvény (SZOCHO/TB)
4. 1990. évi C. törvény (Local taxes)
5. NAV -- https://nav.gov.hu

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an adótanácsadó or equivalent licensed practitioner in Hungary) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
