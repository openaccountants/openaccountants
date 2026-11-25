---
name: sg-cpf-medisave
description: Use this skill whenever asked about Singapore CPF MediSave contributions for self-employed persons (SEPs). Trigger on phrases like "MediSave contribution", "CPF self-employed", "how much MediSave do I pay", "net trade income CPF", "voluntary CPF contributions", "BHS", "Basic Healthcare Sum", "MediShield Life", or any question about MediSave obligations for a self-employed client in Singapore. This skill covers mandatory MediSave rates by age, contribution caps, voluntary CPF contributions, tax relief, payment deadlines, penalties, and edge cases. ALWAYS read this skill before touching any Singapore CPF/MediSave-related work.
version: 3.1
jurisdiction: SG
tax_year: 2026
tax_year_notes: "Calendar 2026 MediSave work year; paid-year relief from YA 2026 onwards"
last_updated: 2026-11-22
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Singapore self-employed MediSave contributions v3.1

Calendar 2026 work-year contributions. The payment year separately determines the following YA's relief. A 2026 payment for an older notice does not adopt 2026 rates.

## Scope

Singapore citizen/PR self-employed persons with qualifying assessed net trade income. Employee payroll CPF and platform-operator computations are separate jobs. Pensioner status is a separate official classification, not simply being over 65.


Read this whole section before computing anything.

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Singapore |
| Jurisdiction Code | SG |
| Primary legislation | [Central Provident Fund Act 1953, section 9A](https://sso.agc.gov.sg/Act/CPFA1953?ProvIds=pr9A-) and [Central Provident Fund (Self-Employed Persons) Regulations 1992](https://sso.agc.gov.sg/SL/CPFA1953-RG25) |
| Supporting legislation | [Income Tax Act 1947, section 39](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr39-) and [MediShield Life Scheme Act 2015, section 4](https://sso.agc.gov.sg/Act/MLSA2015?ProvIds=pr4-) |
| Tax Authority | Central Provident Fund Board (CPFB); Inland Revenue Authority of Singapore (IRAS) |
| Tax Year | 2026 work year; paid-in-2026 relief considered in YA 2027  [Official source](https://www.cpf.gov.sg/member/growing-your-savings/cpf-contributions/saving-as-a-self-employed-person) |
| Currency | SGD only |
| MediSave Trigger Threshold | NTI > S$6,000  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| CPF Annual Limit | S$37,740, voluntary-contribution/relief limit, not an automatic mandatory MediSave cap  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| Basic Healthcare Sum (BHS) | S$79,000 for members below 65 or turning 65 in 2026; older cohorts retain their fixed BHS  [Official source](https://www.moh.gov.sg/newsroom/cpf-interest-rates-from-1-january-to-31-march-2026-and-basic-healthcare-sum-for-2026/) |
| Contributor | Open Accountants |
| Validation Date | Pending |
| Skill Version | 3.1 |
| Coverage boundary | Ordinary SEP computation; actual concurrent-work limitation, hardship, refunds and cross-border facts require their own evidence |


## Ask the client first




Before computing any MediSave figure, you MUST know:

1. Age as at 1 January of the contribution year -- determines the MediSave contribution rate band
2. Net Trade Income (NTI) for the year from the IRAS assessment. Check trade income reported on the applicable Form B or B1.
3. Is the person a Singapore Citizen or Permanent Resident? -- only SC/PR are obligated
4. Is NTI above S$6,000? -- mandatory MediSave only triggers above this threshold
5. Is the person also an employee with employer CPF contributions? -- affects CPF Annual Limit headroom
6. Has the CPF Board contribution notice been issued? -- MediSave is due 30 days after that notice, not the IRAS NOA

If NTI is unknown or the CPF Board contribution notice has not been issued, note that MediSave cannot be finalised. Provide estimates only.


7. Pensioner/non-pensioner category, actual notice work year and all compulsory/voluntary payment dates, separate from trade-income year.

## Rates, bands and thresholds

**MediSave rates by age (NTI > S$18,000, full rate)**

| Age as at 1 Jan | MediSave Rate  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| --- | --- |
| Below 35 | 8.00% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| 35 to below 45 | 9.00% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| 45 to below 50 | 10.00% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| 50 and above | 10.50% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |

**MediSave rates by age (NTI > S$6,000 to S$12,000, lower rate)**

| Age as at 1 Jan | MediSave Rate  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| --- | --- |
| Below 35 | 4.00% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| 35 to below 45 | 4.50% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| 45 to below 50 | 5.00% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| 50 and above | 5.25% of NTI  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |

- For the graduated band, use NTI above S$12,000 and up to and including S$18,000. Apply the [First Schedule, item 23](https://sso.agc.gov.sg/SL/CPFA1953-RG25?ProvIds=Sc1-&ViewType=Advance) and apply regulation 14 rounding to the resulting statutory contribution.

## The method, step by step

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown age or pensioner class | Ask; hold the affected computation |
| Unknown NTI tier | Obtain assessed NTI; do not assume full rate |
| Unknown CPF headroom | Obtain employment/platform and contribution records; do not assume nil |
| Unknown BHS status | Obtain the actual cohort and account position; no exemption from mandatory contribution is inferred |



### Official phase-in, age maxima and pensioner boundary

For non-pensioners with NTI above 12,000 through 18,000, contribution by the four age bands is 480+16%×(NTI−12,000);540+18%×(NTI−12,000);600+20%×(NTI−12,000);630+21%×(NTI−12,000). These simplify the exact effective-percentage formulas in Table 1, not a guessed interpolation. Above 18,000 the respective maxima are 7,680/8,640/9,600/10,080. [2026 Table 1](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV).

For a confirmed pensioner, CPF Board Table 2 gives the same lower-band age rates. The phase-in formulas are 480 + 10% × excess, 540 + 9% × excess, 600 + 8% × excess and 630 + 7.5% × excess. Above S$18,000 the rate is 6%, capped at S$5,760 for each age band. Confirm the classification with CPF Board and apply the public-officer conditions where relevant. [Table 2](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) and [regulations 2 and 4](https://sso.agc.gov.sg/SL/CPFA1953-RG25?ProvIds=pr2-,pr4-).

### 4.1 Determine obligation 

- **Legislation.** Apply the Central Provident Fund Act 1953, section 9A, and the Central Provident Fund (Self-Employed Persons) Regulations 1992. Check any approved reduction or statutory exemption before confirming the balance due.

**Obligation condition table**

| Condition | Obligation |
| --- | --- |
| SEP, SC/PR, NTI > S$6,000 | Mandatory MediSave contribution  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| SEP, NTI <= S$6,000 | No mandatory MediSave (voluntary allowed)  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |
| SEP who is also an employee | Mandatory MediSave on NTI still applies; concurrent-income limitation requires CPFB assessment |

- **SEP** , A person who earns trade, business, profession, or vocation income and is not an employee in respect of that income. Includes sole proprietors, freelancers, commission agents, taxi drivers, hawkers, and professionals.
- **Platform workers exclusion** , Platform workers (from work year 2025): net earnings from platform work are excluded from NTI for MediSave computation and subject to separate CPF rules. Flag if client has platform work income.
- Reconcile any Contribute As You Earn (CAYE) amounts under [regulation 8A](https://sso.agc.gov.sg/SL/CPFA1953-RG25?ProvIds=pr8A-&ViewType=Advance). Reduce the computed liability by the qualifying estimated contributions payable under section 9B. The section 9A balance is nil if they meet or exceed that liability.

### 4.2 NTI computation 

- **Net Trade Income formula.** Gross trade income less allowable business expenses, capital allowances and trade losses, as assessed by IRAS.
- **NTI source.** Use the IRAS assessment and reconcile the trade income reported on [Form B/B1](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29). Use estimates until the assessment or CPF Board computation is available.

### 4.3 Rate application 

- Apply the lower rate above S$6,000 through S$12,000, the exact phase-in above S$12,000 through S$18,000 or the applicable full rate and cap above S$18,000. Use regulation 14 to disregard any fraction of a dollar in the calculated statutory contribution. Reconcile to the [CPF Board calculator and notice guidance](https://www.cpf.gov.sg/member/growing-your-savings/cpf-contributions/saving-as-a-self-employed-person). [Regulation 14](https://sso.agc.gov.sg/SL/CPFA1953-RG25?ProvIds=pr14-).

### 4.4 Contribution caps 

- **CPF Annual Limit** , S$37,740 SGD (Limit relevant to voluntary CPF and relief; do not automatically subtract employment CPF to reduce mandatory SEP payable)
- **Concurrent work.** The CPF Board's 2026 eligibility screen compares employment income excluding Additional Wages and platform work income with S$96,000. Regulation 9A provides a written application for an eligible SEP with CPF contributions made on employment wages or platform remuneration. The approved reduction caps the relevant aggregate contributions, excluding contributions on Additional Wages, at the age-specific Third Schedule amount. Obtain the CPF Board decision. [Regulation 9A and Third Schedule](https://sso.agc.gov.sg/SL/CPFA1953-RG25?ProvIds=pr9A-,Sc3-) and [CPF Board eligibility](https://www.cpf.gov.sg/service/article/what-are-the-conditions-for-applying-to-limit-my-medisave-payable-as-a-self-employed-person).
- **BHS cap** , S$79,000 SGD for members below 65 or turning 65 in 2026; older cohorts keep their own fixed BHS (Caps the MediSave Account balance. Once MA reaches BHS, overflow goes to SA or RA depending on age and retirement conditions, then OA after the applicable retirement sum. The SEP does not get an exemption from contributing -- the contribution is still computed, but overflow is redirected.)


### 6.1 Voluntary contributions 

- **Voluntary contribution rules** , SEPs may make voluntary contributions to OA + SA + MA in addition to mandatory MediSave. Voluntary contributions are allocated under the actual contribution route and the member’s age-based accounts; do not assume an SA exists for a member whose SA has closed. Detailed allocation proportions are not confirmed in this pass.

### Tax relief, from YA 2026 onwards

Mandatory MediSave paid in the preceding calendar year qualifies for full compulsory relief without the old NTI/annual capping restriction, including where current assessed NTI is zero. Voluntary CPF relief remains the lowest of actual eligible voluntary contributions, 37% of assessed NTI less compulsory MediSave relief, and annual-limit headroom after the applicable compulsory contributions, floored at zero. For a concurrent employee, subtract employer and employee compulsory CPF in the annual-limit limb too. Do not apply the old blanket “zero NTI means no compulsory relief” rule.

Identify the actual voluntary contribution/top-up route and age-based account allocation. It is not automatically a deductible OA/SA/MA payment, and no cost can be claimed twice. The overall personal-relief cap is owned by `sg-income-tax`. Relief is automatically prefilled only where eligible and uses actual payment dates: paid by 31 December 2026 means YA 2027, not YA 2026 merely because the liability relates to an older work year. Reconcile CPFB data with receipts. [IRAS current table and examples 1 to 5](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed).

### 6.3 MediShield Life interaction 

- Keep premium statements separate from contribution receipts. The MediShield Life premium is payable from MediSave under section 4(2). For a private Integrated Shield Plan, check the Additional Withdrawal Limit for the private insurance component using the insured person's age and policy. [MediShield Life Scheme Act 2015](https://sso.agc.gov.sg/Act/MLSA2015?ProvIds=pr4-) and [CPF Board withdrawal limits](https://www.cpf.gov.sg/service/article/what-are-additional-withdrawal-limits-awls-for-integrated-shield-plan-ip-premiums).


This is the deterministic pre-classifier for bank statement entries related to CPF/MediSave. Match by case-insensitive substring on the counterparty name or transaction description.

### 3.1 CPF Board payments (mandatory MediSave)

**CPF Board payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CPFB, CPF BOARD, CENTRAL PROVIDENT FUND | MEDISAVE PAYMENT | Mandatory MediSave contribution -- verify against the CPF Board contribution notice |
| GIRO CPF, GIRO-CPF | MEDISAVE PAYMENT (GIRO) | Auto-debit for MediSave contribution |
| CPF VOLUNTARY, CPF TOP-UP | VOLUNTARY CPF CONTRIBUTION | Actual CPF allocation/top-up route and relief must be checked; not automatically tax-deductible |

### 3.2 IRAS-related (triggers MediSave obligation)

**IRAS-related pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRAS, INLAND REVENUE | INCOME TAX PAYMENT | Separate from MediSave; obtain the separate CPF Board contribution notice |
| IRAS NOA, NOTICE OF ASSESSMENT | OBTAIN SEPARATE CPF NOTICE | Income-tax notice is not the MediSave deadline trigger; obtain the CPF Board notice |

### 3.3 MediShield Life premium deductions

**MediShield Life pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MEDISHIELD, MEDISHIELD LIFE | EXCLUDE from MediSave computation | Premium deducted from MediSave Account balance, not a separate contribution |
| INTEGRATED SHIELD, AIA HEALTHSHIELD, PRUDENTIAL PRUSHIELD | EXCLUDE | Private insurance; verify the permitted MA premium funding and withdrawal limit separately |

### 3.4 Platform worker CPF (separate from traditional MediSave)

**Platform worker pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GRAB, DELIVEROO, GOJEK, FOODPANDA | FLAG FOR REVIEW | From work year 2025, platform worker income excluded from NTI for MediSave; separate CPF rules apply  [Official source](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV) |


## Boundary and exception table


### EC 1 -- SEP with NTI exactly S$6,000 

- **EC 1** , Situation: Client's assessed NTI is exactly S$6,000. Resolution: No mandatory MediSave contribution. Threshold is "more than S$6,000", not "S$6,000 or more". Voluntary contributions are still permitted.

### EC 2 -- SEP who is also an employee 

- **EC 2** , Situation: Client works part-time as an employee and also has self-employment income. Resolution: Mandatory MediSave on NTI still applies. Do not automatically cap mandatory payable at the voluntary annual limit. Verify qualifying income, all contribution records and any CPFB limitation outcome.

### EC 3 -- NTI in graduated band (above S$12,000 to S$18,000)

- **EC 3** , Situation: Client's NTI falls in the graduated rate band. Resolution: Use the CPFB Self-Employed MediSave Contribution Calculator. Do not guess or interpolate a percentage.

### EC 4 -- MediSave Account already at BHS 

- **EC 4** , Situation: Client's MediSave Account balance has reached the BHS. Resolution: Mandatory MediSave contributions are still computed on NTI, but contributions in excess of BHS flow to SA or RA depending on age and retirement conditions, then OA after the applicable retirement sum. The SEP does not get an exemption.

### EC 5 -- First year of self-employment, NOA not yet issued 

- **EC 5** , Situation: Client started self-employment mid-year and has not yet received an NOA. Resolution: IRAS assessment normally precedes CPFB assessment, but the actual payment clock runs from the CPF Board contribution notice. Budget from the actual facts. CPFB permits advance contributions through its designated route; missing notice does not establish a permanent waiver.

### EC 6 -- SEP turning 55 during the year 

- **EC 6** , Situation: Client turns 55 during the contribution year. Resolution: Age for MediSave rate purposes is measured as at 1 January. The rate does not change mid-year. Voluntary CPF allocation ratios may shift. Flag for reviewer.

### EC 7 -- Foreign-sourced self-employment income 

- **EC 7.** If the client has overseas self-employment income, check whether it forms part of assessable trade income under regulation 2 and reconcile to the IRAS assessment. Flag cross-border cases for review.

### EC 8 -- Platform worker with mixed income 

- **EC 8** , Situation: Client earns from both platform work and traditional self-employment. Resolution: From work year 2025, net platform work earnings excluded from NTI for MediSave. Only traditional self-employment income triggers mandatory MediSave. Flag for reviewer.


When a Tier 2 situation is identified:

```
REVIEWER FLAG
Tier: T 2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed Singapore practitioner must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T 3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed practitioner. Document gap.
```


## Worked cases


### Test 1 -- Standard SEP, age 30, NTI above S$18,000

Input: Age 30 (as at 1 Jan 2026), NTI = S$50,000.
Expected output: Rate = 8.00%. MediSave = S$4,000.00. Below the applicable 2026 age-specific SEP maximum; no mandatory cap binds.

### Test 2 -- SEP, age 40, NTI above S$18,000

Input: Age 40 (as at 1 Jan 2026), NTI = S$80,000.
Expected output: Rate = 9.00%. MediSave = S$7,200.00. Below the applicable 2026 age-specific SEP maximum; no mandatory cap binds.

### Test 3 -- SEP, age 48, NTI above S$18,000

Input: Age 48 (as at 1 Jan 2026), NTI = S$60,000.
Expected output: Rate = 10.00%. MediSave = S$6,000.00. Below the applicable 2026 age-specific SEP maximum; no mandatory cap binds.

### Test 4 -- SEP, age 55, NTI above S$18,000

Input: Age 55 (as at 1 Jan 2026), NTI = S$40,000.
Expected output: Rate = 10.50%. MediSave = S$4,200.00. Below the applicable 2026 age-specific SEP maximum; no mandatory cap binds.

### Test 5 -- NTI exactly S$6,000

Input: Age 30, NTI = S$6,000.
Expected output: No mandatory MediSave. Threshold is "more than S$6,000".

### Test 6 -- NTI in the lower band (above S$6,000 to S$12,000)

Input: Age 30, NTI = S$10,000.
Expected output: Rate = 4.00%. MediSave = S$400.00.

### Test 7 -- NTI in graduated band

Input: Age 30, NTI = S$15,000.
Expected output: Non-pensioner contribution = 480 + 16% × (15,000 − 12,000) = S$960, an effective 6.4%. Reconcile the exact official formula with the CPF Board calculator and eventual notice; do not substitute a guessed interpolation.

### Test 8, voluntary payment versus relief headroom

Age 35, 2026 assessed NTI 100,000, no employment CPF and a proposed voluntary 30,000. The mandatory 2026 figure is min(100,000×9%,8,640)=8,640. Assume all 8,640 paid in 2026. Annual contribution headroom is 37,740−8,640=29,100, so the 30,000 proposal exceeds it by 900. If only 29,100 is accepted and paid through the eligible route, voluntary relief is 28,360 because 37%×100,000−8,640 is tighter. Total SEP relief is 37,000 before the overall personal-relief cap, not 37,740. The 740 difference between accepted voluntary payment and voluntary relief does not itself earn more relief. Show both amounts before the client decides to top up. [2026 table](https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV); [IRAS relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed).

```oa-check
name: Ordinary2026 and official phase-in contribution
inputs:
  full_nti: 50000
  phase_nti: 15000
  fractional_phase_nti: 12009
steps:
  - ordinary: min(full_nti * 0.08, 7680)
  - graduated: 480 + 0.16 * (phase_nti - 12000)
  - effective_percentage: graduated * 100 / phase_nti
  - fractional_graduated_payable: floor(480 + 0.16 * (fractional_phase_nti - 12000))
expected:
  ordinary: 4000
  graduated: 960
  effective_percentage: 6.4
  fractional_graduated_payable: 481
```

```oa-check
name: Voluntary contribution versus relief and zero NTI exception
inputs:
  nti: 100000
  compulsory_paid: 8640
  proposed_voluntary: 30000
  prior_compulsory_paid: 4200
steps:
  - annual_headroom: max(0, 37740 - compulsory_paid)
  - accepted_voluntary: min(proposed_voluntary, annual_headroom)
  - proposal_excess: proposed_voluntary - accepted_voluntary
  - voluntary_relief: min(accepted_voluntary, max(0, nti * 0.37 - compulsory_paid), annual_headroom)
  - total_sep_relief: compulsory_paid + voluntary_relief
  - without_extra_relief: accepted_voluntary - voluntary_relief
  - zero_nti_voluntary_relief: min(2440, max(0, 0 * 0.37 - prior_compulsory_paid))
  - zero_nti_total_relief: prior_compulsory_paid + zero_nti_voluntary_relief
expected:
  annual_headroom: 29100
  accepted_voluntary: 29100
  proposal_excess: 900
  voluntary_relief: 28360
  total_sep_relief: 37000
  without_extra_relief: 740
  zero_nti_total_relief: 4200
```

The last output preserves IRAS's YA 2026 example of 4,200 compulsory payment made in 2025 despite zero 2025 assessed NTI. The model must not infer zero compulsory relief from zero trade income.

## When to refuse or refer



- **R-SG-CPF-1 -- Hardship appeal** , Trigger: client asks about reducing or waiving MediSave contributions due to financial hardship. Message: "MediSave contribution hardship appeals are handled directly by CPFB. This skill cannot advise on appeal procedures. Please contact CPFB at the contact route on its current official website."
- **R-SG-CPF-2 -- Contribution refund** , Trigger: client asks about refunding MediSave contributions already paid. Message: "MediSave contribution refunds are governed by CPFB policy and outside this skill's scope. Please escalate to a licensed Singapore practitioner."
- **R-SG-CPF-3 -- Cross-border employment** , Trigger: client asks about CPF obligations while working across Singapore and another jurisdiction simultaneously. Message: "Cross-border CPF obligations require case-specific analysis. Please escalate to a licensed Singapore practitioner."



### Actions that require actual evidence

- NEVER compute MediSave without knowing the client's age as at 1 January of the contribution year
- NEVER use estimated income for final MediSave computation -- MediSave is based on IRAS-assessed NTI
- Confirm nil contributions for ordinary NTI of S$6,000 or below or under an applicable statutory exemption. For a balance after credits or reduction, obtain the CPF Board's determination.
- Above S$12,000 through S$18,000, use the official graduated formula and the CPF Board calculator.
- Above S$6,000 of qualifying NTI, determine the ordinary statutory liability and check any applicable exemption, reduction or credit.
- NEVER ignore the CPF Annual Limit when computing total CPF contributions
- NEVER conflate BHS (MediSave Account balance cap) with CPF Annual Limit (contribution cap)
- NEVER include platform worker income in NTI for MediSave from work year 2025 onward without review
- NEVER present MediSave figures as definitive -- always label as estimated and direct client to their CPFB contribution notice
- NEVER advise on MediSave penalties without escalating to a licensed practitioner

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Filing and payment


### 5.1 Payment deadline 

**Payment deadline table**

| Item | Detail |
| --- | --- |
| Trigger | CPF Board issues its Notice of CPF Contributions for Self-employed Persons |
| Deadline | 30 days from issue of the CPF Board contribution notice, or the end of any extended period the Board specifies. Payment remains due despite an assessment objection or appeal unless the Board extends the deadline. [Regulations 7A and 16](https://sso.agc.gov.sg/SL/CPFA1953-RG25?ProvIds=pr7A-,pr16-) |
| Payment methods | PayNow and the Manage your MediSave payable form; use the actual approved GIRO/instalment arrangement |
| Instalment plan | Request CPFB approval; the approved schedule determines dates, with no universal 12-month promise  [Official source](https://www.cpf.gov.sg/member/growing-your-savings/cpf-contributions/saving-as-a-self-employed-person) |

- **Deadline alignment** , The MediSave clock is separate from the income-tax payment clock. Obtain the CPF Board notice and any approved instalment schedule.

### 5.2 Penalties for non-contribution 

After reminders, the CPF Board may offer composition and issue a Notice to Attend Court if the case remains unresolved. On conviction for an applicable offence, the general maxima are S$5,000, 6 months' imprisonment or both. A repeat conviction for the same offence can carry S$10,000, 12 months or both. Section 9(2) provides daily interest on overdue self-employed contributions at the prescribed rate and start date, subject to the Board's remission power. Verify the applicable rate and date before calculating interest. [CPF Act sections 9, 58 and 61](https://sso.agc.gov.sg/Act/CPFA1953?ProvIds=pr9-,pr58-,pr61-) and [CPF Board SEP enforcement](https://www.cpf.gov.sg/service/article/what-if-self-employed-persons-do-not-respond-to-the-notice-of-cpf-contributions-for-self-employed-persons).



## Completion checklist

- Work year, age on 1 January, pensioner class and SC/PR established.
- Assessed NTI reconciled, platform earnings excluded once, concurrent-income application checked.
- Correct table, age maximum and notice rounding used; BHS kept separate.
- Actual payment year, eligible contribution route and compulsory/voluntary relief reconciled.
- CPF Board notice, due date/instalment approval, CAYE credits and settlement receipt retained. Preparation is not filing or payment.

## Sources

| Source and scope read | Official URL | Read on |
|---|---|---|
| Read for complete 2026 Tables 1/2, age/income bands, phase-in formulas, annual maxima and platform footnote. | https://www.cpf.gov.sg/service/sfc/servlet.shepherd/document/download/069IW00000G4S1QYAV |2026-11-14 |
| Read for SEP/NTI definition, tax-authority declarations, CPFB notice, 30-day payment, PayNow, GIRO/licence interaction, CAYE and advance contributions. | https://www.cpf.gov.sg/member/growing-your-savings/cpf-contributions/saving-as-a-self-employed-person |2026-11-14 |
| Read for pre/from-YA 2026 distinction, full compulsory relief at zero NTI, voluntary limits, concurrent employment and examples 1 to 5, actual paid-year timing. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed |2026-11-14 |
| Read for 2026 amount 79,000, age 65 fixation and older cohort table. | https://www.cpf.gov.sg/service/article/what-is-the-basic-healthcare-sum |2026-11-14 |
| Read targeted regulations 2, 2A, 3, 4, 7A, 8A, 9A, 13–16, 17AB and 25 and First and Third Schedules for threshold, age, rounding, deadlines, reduced contributions and exemption. | https://sso.agc.gov.sg/SL/CPFA1953-RG25?ProvIds=pr3-,pr7A-,pr8A-,pr9A-,pr14-,pr16-,pr25-,Sc1-,Sc3- | 2026-11-24 |
| Read sections 9, 9A, 58 and 61 for contributions, late interest authority and general offence penalties. | https://sso.agc.gov.sg/Act/CPFA1953?ProvIds=pr9-,pr9A-,pr58-,pr61- | 2026-11-24 |
| Read the amended compulsory and voluntary relief in section 39 for YA 2026 onwards. | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr39- | 2026-11-24 |
| Read section 4 for premium payment and CPF Board guidance for the private component. | https://sso.agc.gov.sg/Act/MLSA2015?ProvIds=pr4- | 2026-11-24 |
| Read for continuing contribution liability and SA/RA then OA overflow conditions. | https://www.cpf.gov.sg/service/article/do-i-still-have-to-contribute-to-medisave-as-a-self-employed-person-even-though-my-medisave-balance-has-reached-the-basic-healthcare-sum-bhs |2026-11-14 |
| Read for maximum qualifying annual income 96,000 from 2026, Additional Wages exclusion, platform timing and CPFB application. | https://www.cpf.gov.sg/service/article/what-are-the-conditions-for-applying-to-limit-my-medisave-payable-as-a-self-employed-person |2026-11-14 |
| Read for SEP demand/composition/NTA and first/repeat fine/imprisonment maxima. | https://www.cpf.gov.sg/service/article/what-if-self-employed-persons-do-not-respond-to-the-notice-of-cpf-contributions-for-self-employed-persons |2026-11-14 |
| Read for flexible instalment handling and court as last resort, no promised waiver. | https://www.cpf.gov.sg/service/article/why-does-cpf-board-take-self-employed-persons-to-court-for-not-contributing-to-their-medisave |2026-11-14 |
| Read for 2026 BHS of 79,000 below age65 and fixed turn65 cohort; older cohorts unchanged. | https://www.moh.gov.sg/newsroom/cpf-interest-rates-from-1-january-to-31-march-2026-and-basic-healthcare-sum-for-2026/ | 2026-11-14 |

Not yet confirmed: the applicable prescribed SEP late-interest rate and start date, any travel restriction, a universal maximum instalment term, AXS or other alternative payment channels for this liability, and a client's actual pensioner status, notices, approved reductions, voluntary allocation or refund facts.
