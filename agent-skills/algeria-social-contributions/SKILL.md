---
name: algeria-social-contributions
description: "Use this skill whenever asked about Algeria social security / social insurance contributions (CNAS for salaried employees, CASNOS for self-employed/non-salaried) and the interaction with Algerian personal income tax (IRG). Trigger on phrases like 'how much CNAS do I pay', 'Algeria payroll contributions', 'employer social security Algeria', 'CNAS employee deduction', 'CASNOS self-employed contribution', 'G50 declaration', 'DAS annual salary declaration', 'IRG on salary', 'Algerian minimum wage SNMG', 'social security Algeria calculation', or any question about Algerian payroll, contribution or IRG obligations. Also trigger when classifying bank statement transactions that relate to CNAS/CASNOS debits, G50 tax payments, or DGI/Trésor payments from BNA, BEA, CPA, BADR, or other Algerian banks. This skill covers CNAS 25% employer/9% employee/0.5% social-works fund branch rates, the CASNOS 15% self-employed regime, the SNMG floor, routing to IRG computations, G50/DAS separation and verified"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/algeria-social-contributions"
  jurisdiction: "DZ"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Algeria Social Contributions (CNAS and CASNOS) v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year), current-law reading on 15 November 2026. Amounts in Algerian dinars (DA or DZD). CNAS handles salaried social contributions and CASNOS the non-salaried regime; DGI handles IRG tax. This skill produces a working paper, not an authenticated filing or a statement of arrears.

**Answer layer.** The general branch table is 25% employer + 9% employee + 0.5% social-works fund = 34.5%, not a rounded 26%/9%/35%. CASNOS is 15% of its legally determined annual base, subject to activity/year rules and the auto-entrepreneur option. First establish the regime, period, documented contribution base, number of employees, sector and existing assessments. The July 2026 amendment adds multiple-activity and third-year rules; an old minimum-only calculation is insufficient. [CNAS table,15-236 article 1](https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf); [CASNOS,26-257 article 1](https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf).

## Who this applies to

Salaried workers and employers (CNAS), including the nationality-neutral affiliation rule, and persons carrying on a non-salaried professional, industrial, commercial, agricultural, craft or liberal activity (CASNOS), even without employees. Establish actual activity and effective affiliation, rather than infer non-affiliation from low income. A salaried person with accessory self-employment must also affiliate for the non-salaried activity; separate the income streams and confirm benefit coordination. [83-14 articles 3–10](https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf); [15-289 article 19](https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015061.pdf).

Arrears, start-up/youth-employment reductions, an actual foreign posting and treaty relief need their own official decisions and sources. This skill does not establish eligibility for an incentive or particular bilateral exemption.

## Rates, bands and thresholds

| Branch or item | Employer rate | Employee rate | Social-works fund rate | Total rate and condition | Official URL |
|---|---|---|---|---|---|
| Social insurance | 11.5% | 1.5% | 0% | 13%, general salaried table | https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf |
| Work accidents and occupational diseases | 1.25% | 0% | 0% | 1.25%, general salaried table | https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf |
| Retirement | 11% | 6.75% | 0.5% | 18.25%, fund column distinct from pure employer column | https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf |
| Early retirement | 0.25% | 0.25% | 0% | 0.5%, general salaried table | https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf |
| Unemployment | 1% | 0.5% | 0% | 1.5%, general salaried table | https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf |
| General total | 25% | 9% | 0.5% | 34.5%, before separately applicable sector regimes/reductions | https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf |
| CACOBATPH weather interruption | 0.375% | 0.375% | Separate scheme | 0.75%, only covered activities; not ordinary unemployment | https://www.joradp.dz/FTP/jo-francais/1997/F1997008.PDF |
| CACOBATPH paid leave | 12.21% | 0% | Separate scheme | 12.21%, employer only, if paid-leave regime applies; sector classification needs confirmation | https://www.joradp.dz/FTP/jo-francais/1997/F1997008.PDF |

The table reproduces the enacted 15-236 allocation. It is not a determination of the complete FNPOS or social-works financing regime. Do not use 34.5% as proof of the complete employer cost or of the absence of a separate housing/social-works duty; establish its applicability and incidence separately. No later amendment changing that general allocation was found in the official-source search; it is not a claim that every special category pays the same rate. Do not add the fund column a second time when a statement already aggregates employer/fund amounts.

| CASNOS item | Rate or amount | Conditions and period | Official URL |
|---|---|---|---|
| Ordinary rate | 15% of annual base | 7.5% insurance + 7.5% retirement; determine the legal base first | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |
| Annual minimum base | 288,000 DA, derived:24,000 × 12 | Arabic original article 14 expressly says annual SNMG. Apply actual affiliation, activity and auto-entrepreneur rules; the third-year mean may impose a higher contribution | https://www.joradp.dz/FTP/jo-arabe/2026/A2026053.pdf |
| Corresponding ordinary minimum contribution | 43,200 DA, derived:288,000 × 15% | Not the auto-entrepreneur option or a guaranteed final liability in every activity/year | https://www.joradp.dz/FTP/jo-arabe/2026/A2026053.pdf |
| Annual maximum base | 5,760,000 DA, derived:24,000 × 12 × 20 | Article 14 ceiling 20 times annual SNMG; multiple activities and assessments require reconciliation | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |
| Corresponding maximum contribution | 864,000 DA, derived:5,760,000 × 15% | Ordinary single-base illustration, not a statement of arrears or sector-specific liability | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |
| First year of activity | Annual SNMG base:288,000 DA; contribution 43,200 DA, derived | Actual first-year rule in the current article 14, subject to the explicit auto-entrepreneur choice | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |
| Third year onwards | Activity/wilaya prior-year mean contribution | Contribution cannot be below this mean; amount set/revised by ministerial order. No current numeric mean is supplied here | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |
| Auto-entrepreneur choice | 24,000 DA annually or contribution under ordinary rules | Confirm actual statutory auto-entrepreneur status and choice; not every sole trader | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |
| SNMG | 24,000 DA monthly;138.46 DA hourly | Decree 26-01:40 hours weekly,173.33 hours monthly; effective 1 January 2026 | https://www.joradp.dz/FTP/jo-francais/2026/F2026001.pdf |

**Language reconciliation.** The French 26-257 translation omits “annual” from the general lower-bound sentence while expressly retaining it for the upper bound and first year. The Arabic original expressly contains annual in the lower-bound sentence. Both operative versions were read; the annual-derived figures above follow that original text. This does not resolve actual transition assessments before the July amendment or supply the missing activity/wilaya mean order.

## The base

### Document the CNAS base

Use the documented contribution base, not automatically basic pay or the bank debit. Decree 96-208 articles 1–2 defines excluded family payments, expense reimbursements, exceptional indemnities and particular residence/isolation indemnities. Family categories include school/family benefits, single-salary indemnity and birth/marriage/family-event payments. Expense examples include qualifying meal/vehicle/tool/clothing, travel/transport/mission amounts. Exceptional indemnities include dismissal compensation and exceptional retirement departure amounts. Residence/isolation exclusion requires at least 2 of the listed constraints: mobile/camp accommodation, continuous multi-week rotation with unpaid rest indemnity, and a remote/difficult-access workplace. A name on a payslip alone does not establish the exclusion. [96-208, articles 1–2](https://www.joradp.dz/FTP/Jo-Francais/1996/F1996035.pdf).

The complete operative 95-01 article 1 general inclusion text and any special minimum-base/ceiling exceptions were not recovered in an ordinarily readable official original. Do not invent a general earnings ceiling, blindly floor every payroll base to monthly SNMG, or decide an unusual remuneration item from this skill. Obtain and reconcile the actual payslip/DAC base and refer an unresolved classification. The SNMG wage decree is not, by itself, a complete contribution-base rule.

### Determine the CASNOS base in order

1. Establish the assessment year, activity start/cessation, tax regime, all non-salaried activities and actual CASNOS status. A tax exemption does not by itself prove an insurance exemption.
2. The retained annual declaration duty is supported by fiscal/accounting documents, no later than 1 March. For the real tax regime,24-49 uses the closed-year ordinary pre-tax result declared during the preceding year. Record both accounting year and declaration year; do not replace that wording with an assumed one-year shortcut. [22-121 article 2/amended 14](https://www.joradp.dz/FTP/jo-francais/2022/F2022020.pdf); [24-49 article 1/amended 14](https://www.joradp.dz/FTP/jo-francais/2024/F2024004.pdf).
3. If operating income cannot be determined, notably under the forfait regime, the alternative base uses 25% of prior-year fiscal turnover for production/sale of goods or 35% for services. Those percentages produce the base, then apply 15%; they are not contribution rates and turnover is not automatically the whole base. [24-49,14](https://www.joradp.dz/FTP/jo-francais/2024/F2024004.pdf).
4. Apply the current annual SNMG lower bound and 20 annual-SNMG ceiling with the language reconciliation above. For multiple activities,26-257 aggregates previous operating income but requires the contribution for each activity, considered separately, to meet the stated minimum. Do not simply apply one shared minimum to an unanalysed mixed portfolio. [26-257,14](https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf); [Arabic original](https://www.joradp.dz/FTP/jo-arabe/2026/A2026053.pdf).
5. First-year annual base is annual SNMG. From the third year, obtain the ministerially determined prior-year mean contribution for the same activity/wilaya; the annual contribution cannot be below it. Without that amount, a final third-year liability is unavailable. The qualifying auto-entrepreneur may choose 24,000 DA annually or the ordinary amount. [26-257,14](https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf).
6. A missing declaration/undetermined income or turnover allows provisional determination on the prior year's base with a 5% uplift, definitively acquired by the agency. The provision does not say 5% for each extra month. Assessments can be reassessed using declarations or comparable same-activity bases. Obtain the assessment rather than manufacture an arrears amount. [26-257,14](https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf).

### Required inputs, refusal catalogue and practical bank controls

The earlier workflow topics remain below with corrected legal boundaries. Bank matching and working-paper controls are practical recommendations, not statutory presumptions; the sourced conditions above govern.

#### Required inputs

**Minimum viable**: employment status (salaried vs non-salaried/self-employed) and documented contribution base and pay period (CNAS) or the fiscal/accounting base, tax regime and assessment year (CASNOS). Without employment status, STOP: the two regimes are not interchangeable.

**Recommended**: the tax year, the employer's sector (construction/public works/hydraulics carries an add-on), and for IRG: residency status and any other Algeria-source income.

**Ideal**: CNAS DAC declarations, G50 declarations, DAS annual salary declaration, payslips showing the 9% employee deduction and IRG withheld, and bank statements showing CNAS/CASNOS and Trésor/DGI debits.

#### Refusal catalogue

- **R-DZ-SC-1**: Employment status unknown. Trigger: not stated whether the client is salaried (CNAS) or self-employed (CASNOS). Message: "Employment status is mandatory. The general CNAS table is 25% employer, 9% employee and 0.5% social-works fund, total 34.5%, with special categories checked separately; CASNOS is 15% of its determined base, subject to activity/year rules and the qualifying auto-entrepreneur choice. These regimes are not interchangeable. Cannot proceed without this information."
- **R-DZ-SC-2**: Contribution arrears / penalties. Trigger: client has unpaid CNAS contributions from prior periods. Message: "Late contribution payment is distinct from late salary declaration:83-14 article 24 states 5% of contributions due plus 1% of principal per additional month; article 16 separately states a 15% declaration penalty increased by 5% per month. Do not invent an uplift base or cumulative assessment without the actual notice. Public-administration exceptions and the agency statement must be checked. Do not quantify arrears without a CNAS statement. Escalate to a warranted Algerian accountant."
- **R-DZ-SC-3**: Sector add-ons and exemptions. Trigger: client is in construction, public works, hydraulics, or claims a reduced-rate scheme (e.g. ANSEJ/ANADE start-up exemptions). Message: "Covered CACOBATPH weather interruption carries 0.375% on each side; covered paid leave carries 12.21% employer-only. These are not the ordinary unemployment branch. Start-up/youth-employment relief eligibility is not established here. These require case-specific confirmation. Escalate to a warranted Algerian accountant."
- **R-DZ-SC-4**: Non-resident / expat payroll. Trigger: client is a non-resident, on a bilateral social-security agreement, or seconded into/out of Algeria. Message: "Bilateral social-security agreements and secondment relief are outside the scope of this skill. The earlier Algeria-source-only professional-income assertion is an unusable historical note here; actual nonresident IRG treatment requires a separately sourced determination. Escalate to a warranted Algerian accountant."
- **R-DZ-SC-5**: IRG/tax penalty quantification. Trigger: request to quantify statutory IRG late-payment penalties. Message: "Specific statutory IRG late-payment penalty percentages are not confirmed from a primary authority in this skill (unverified). Do not estimate. Escalate to a warranted Algerian accountant."

Use this practical pre-classifier to propose a ledger category from bank references, then reconcile the official declaration, assessment and receipt. A matching substring is not proof of regime, period, taxable base or final liability.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statements may be in French or Arabic. An identified statutory contribution/tax settlement is not a purchase invoice: do not claim input VAT from the bank debit alone. Confirm what the payment settles; this classification control does not establish the VAT treatment of a separate service invoice.

#### 3.1 CNAS salaried contribution debits

**CNAS salaried contribution debits**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: CNAS | EXCLUDE: social contribution | DAC contribution settlement: general 34.5% allocation; monthly/quarterly period depends on headcount, and debit may include adjustments |
| CAISSE NATIONALE ASSURANCES SOCIALES | EXCLUDE: social contribution | Full CNAS name |
| COTISATION CNAS, COTISATIONS SOCIALES | EXCLUDE: social contribution | "Contribution" reference |
| DAC, DECLARATION CNAS | EXCLUDE: social contribution | DAC contribution declaration/payment; establish monthly or quarterly period and receipt |
| الضمان الاجتماعي (social security) | EXCLUDE: social contribution | Arabic-language reference |

#### 3.2 CASNOS self-employed contribution debits

**CASNOS self-employed contribution debits**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: CASNOS | EXCLUDE: self-employed contribution | 15% of the legally determined annual base; check first year/third-year mean/multiple activities/auto-entrepreneur choice |
| CAISSE NON-SALARIES, NON SALARIES | EXCLUDE: self-employed contribution | Full/abbreviated CASNOS reference |
| COTISATION CASNOS | EXCLUDE: self-employed contribution | Contribution reference |

#### 3.3 IRG / income tax payments (NOT a social contribution)

**IRG / income tax payments**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: G50, G-50, G 50 | EXCLUDE: payroll tax (IRG withheld) | Tax declaration/payment cue; route current G50/G29 timing and regime to algeria-payroll rather than infer from this reference |
| IRG, IMPOT REVENU GLOBAL | EXCLUDE: income tax | Not a CNAS/CASNOS contribution |
| TRESOR, RECETTE DES IMPOTS | EXCLUDE: tax payment to the Treasury | DGI/Trésor counterparty |
| DGI, DIRECTION DES IMPOTS | EXCLUDE: tax payment | Tax authority |
| IBS, IMPOT BENEFICES SOCIETES | EXCLUDE: corporate tax | Company-level, not payroll contribution |

#### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| SALAIRE, PAIE, VIREMENT SALAIRE (outgoing) | EXCLUDE: payroll expense | Net wage transfer, not a CNAS payment |
| SALAIRE (incoming) | EXCLUDE: employment income received | Not a contribution |
| الراتب (salary) | EXCLUDE: payroll/salary | Arabic-language reference |

#### 3.5 Benefits received (not contributions paid)

**Benefits received**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| PENSION CNR, RETRAITE | EXCLUDE: pension income received | CNR pays pensions; not a contribution |
| ALLOCATION CHOMAGE, CNAC | EXCLUDE: unemployment benefit received | Inbound benefit, not a contribution |
| ALLOCATIONS FAMILIALES | EXCLUDE: family benefit received | Outside the contribution base entirely |

When bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

#### T2-1: Salaried vs self-employed boundary (mixed activity)

- **T2-1**: Trigger: Client draws a salary and also earns self-employed/professional income. Issue: Separate the general CNAS 34.5% allocation from the CASNOS 15% base rules and qualifying choice. Both regimes can apply simultaneously on different income streams. Action: Flag for reviewer. Split the income streams and confirm dual affiliation before computing.

#### T2-2: Sector-specific add-on (construction / public works / hydraulics)

- **T2-2**: Trigger: Employer operates in construction, public works, or hydraulics. Issue: Weather interruption is 0.375% employer plus 0.375% employee for covered activities, separate from ordinary unemployment; paid-leave coverage adds 12.21% employer-only. Action: confirm both coverage lists and actual classifications before adding either scheme.

#### T2-3: Rate-source reconciliation (old 26% versus 25.5%)

- **T2-3**: The official 15-236 table gives pure employer 25%, employee 9% and social-works fund 0.5%, total 34.5%. Employer/fund combined 25.5% is derived, not the table's pure employer column. The former 26%/35% headline and alternative 12.5% health/10.5% retirement split were unsubstantiated; they must not drive a payment. Reconcile the actual branch statement and separately applicable additions, rather than round the statutory table. Those rejected historical figures are retained only on the Not yet confirmed line.

#### T2-4: CNAS / CASNOS arrears and penalties

- **T2-4**: Trigger: Client has unpaid contributions from prior periods. Issue: Payment and declaration failures have different statutory rules; use the sourced Penalties and interest section, public-administration exception and actual agency statement. Principal and penalty cannot be separated without a CNAS statement. Action: Do not quantify arrears. Escalate to a warranted Algerian accountant.  _(unverified note)_

#### T2-5: Salaried IRG withholding vs annual table

- **T2-5**: Trigger: Need to compute IRG actually withheld from a salary. Issue: The salary exemption and special abatements differ from a naive application of the annual IRG bands; use the current salary computation and its strict boundaries. Action: use `algeria-payroll`.

#### T2-6: 2026 SNMG change and Finance Law 2025 floors

- **T2-6**: Trigger: Computation spans into 2026, or involves the lump-sum/minimum tax regime. Issue: SNMG is 24,000 DZD/month under Decree 26-01; the earlier 20,000 DZD wage figure is historical and is not the 2026 wage amount. Action: use the SNMG of the year being computed. For IFU floors use `algeria-income-tax`.

When producing a contribution / payroll computation, structure the working paper as follows:

```
ALGERIA CONTRIBUTION & IRG COMPUTATION: WORKING PAPER
Client: [name]
Tax Year: [year]                          Currency: DZD
Prepared: [date]

INPUT DATA
  Employment status:             [Salaried (CNAS) / Self-employed (CASNOS)]
  Sector:                        [Standard / Construction-PublicWorks-Hydraulics]
  Gross monthly salary (CNAS):   DZD [____]
  Declared annual income (CASNOS): DZD [____]
  Residency:                     [Resident / Non-resident]

CNAS COMPUTATION (salaried)
  Documented contribution base: DZD [____]   (unresolved base classification referred; no blind wage-floor substitution)
  Employer 25%:                  DZD [____]
  Employee 9%:                   DZD [____]
  Social-works fund 0.5%:        DZD [____]
  Covered weather 0.375% each:   DZD [____]
  Covered paid leave 12.21% ER:   DZD [____]
  General total 34.5%:            DZD [____] (before separately applicable schemes)

CASNOS COMPUTATION (self-employed)
  Legal annual base:            DZD [____]
  Assessment year/activity/first or third year/mean: [____]
  Multiple-activity minima and auto-entrepreneur choice: [____]
  Ordinary single-base bounds 288,000–5,760,000: reconcile conditions above
  Contribution 15%:              DZD [____]
    of which 7.5% insurance:     DZD [____]
    of which 7.5% retirement:    DZD [____]

IRG COMPUTATION (separately confirmed tax base; social base is not automatically identical)
  Gross salary (annual):         DZD [____]
  Less employee CNAS 9%:         DZD [____]
  IRG taxable base:              DZD [____]
  IRG (see algeria-payroll):     DZD [____]
  Net pay:                       DZD [____]

FILING
  G50/G29 (IRG):                 current tax-specific deadline verified separately
  CNAS payment:                 30 days after month if >=10 workers; after quarter if <10
  DAS (annual salaries):        30 days aftercalendar year end
  CASNOS declaration/payment:   current sourced deadlines and affiliation conditions

REVIEWER FLAGS
  [List any Tier 2 flags and (unverified)

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

#### Bank statement reading guide

Statements from BNA, BEA, CPA, BADR and BDL are usually in French, sometimes Arabic, in DZD.

- CNAS: "CNAS", "COTISATION CNAS", "DAC", "CAISSE NATIONALE ASSURANCES SOCIALES". Practical cue only; reconcile the monthly/quarterly assessment and general 34.5% allocation, sector items, arrears and prior credits.
- CASNOS: "CASNOS", "COTISATION CASNOS", "NON SALARIE". Annual-base assessment or qualifying choice, with the activity/year conditions above; do not infer a unique income from the debit.
- G50 and IRG: "G50", "RECETTE DES IMPOTS", "TRESOR", "IRG SALAIRES", "DGI". Counterparty DGI or Tresor, distinct from CNAS/CASNOS. Verify the actual G50/G29 tax period and current duty separately.

Tips: contribution debits are always outgoing, so inbound CNR or CNAC credits are benefits. CNAS payment can be monthly or quarterly and CASNOS ordinarily annual; observed recurrence is only a clue. "MAJORATION DE RETARD" or "REGULARISATION" signals penalties or arrears: flag for the reviewer. Family benefits are outside the base.

#### Onboarding fallback, bank statement only

1. Propose the regime from CNAS/CASNOS references, then confirm affiliation and mixed activities; a payment reference alone is insufficient.
2. List every outgoing payment that matches the patterns above.
3. Work back only as an illustration after establishing that the debit is a clean general contribution with all three shares and no adjustments: debit/0.345 suggests the contribution base, not automatically gross monthly salary. A clean ordinary CASNOS debit/0.15 suggests an assessed base, not necessarily declared income.43,200 DA is compatible with the derived ordinary minimum/first-year illustration, but does not prove the year, activity or assessment. Never divide a special-choice, arrears, instalment or mixed-period debit as if it were clean principal.
4. Keep tax apart: G50, Tresor and DGI debits are IRG, not contributions.
5. Flag for the reviewer: "Regime and base derived from bank statement amounts only. Employment status, sector and declared income have not been independently verified."

#### Prohibitions

- NEVER compute contributions before establishing salaried or self-employed status.
- NEVER assume a universal CNAS ceiling, uncapped gross base or wage floor while the applicable base/category rule remains unresolved; obtain its authority before computing.
- NEVER omit a covered weather or paid-leave scheme; confirm both activity classifications and both sides of the weather allocation.
- NEVER apply only the ordinary floor while ignoring the qualifying auto-entrepreneur choice, multiple-activity minima, first-year rule, third-year mean or actual assessment.
- NEVER conflate CNAS or CASNOS with G50 or IRG: they go to different authorities.
- NEVER quantify arrears or penalties without an official CNAS or DGI statement: escalate.
- NEVER mix tax years' SNMG figures: 20,000 DA through 2025, 24,000 DA in the 2026 tables.
- NEVER present figures as definitive: this skill awaits accountant sign-off.

#### Corporate tax (IBS), context only

IBS remains outside this skill; route to a separately sourced company-tax computation. The former context-only corporate figures are retained as unusable historical claims on the Not yet confirmed line, not contribution inputs.

## Deadlines and filing

| Obligation | Deadline or rate | Conditions | Official URL |
|---|---|---|---|
| CASNOS annual base declaration | No later than 1 March | Fiscal/accounting support; current amended 14 retains declaration paragraph | https://www.joradp.dz/FTP/jo-francais/2022/F2022020.pdf |
| CASNOS ordinary non-farm payment | Before 1 July | Due 1 January; actual affiliation/cessation conditions below | https://www.joradp.dz/FTP/jo-francais/2022/F2022020.pdf |
| CASNOS exclusively agricultural payment | Before 1 October | Only persons exclusively carrying on agriculture; other/mixed activity not automatically eligible | https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015061.pdf |
| CNAS contribution payment | First 30 days after month if more than 9 workers; after quarter if fewer than 10 | Unique payment by territorial employer; reconcile actual workforce/period | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| CNAS annual nominative salary declaration |30 days after calendar year end | Article 14 permits periodicity to be changed by regulation; do not substitute an unverified 31 January extension | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Activity declaration/employee affiliation |10 days after activity begins or worker recruitment | Distinct obligations, not the recurring contribution deadline | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |

CASNOS 15 as amended 22-121: affiliation runs from actual declared activity start to cessation. A midyear affiliation before 1 December incurs the annual contribution; if affiliation follows the ordinary due date, pay within 30 days after affiliation. On cessation, the contribution is due only if cessation is after 31 January. This is not an invented daily/monthly prorating rule. Validation of insurance years requires contributions for all liable periods. Certificate/authorisation conditions and agency procedures must be checked on the actual record. [22-121,15](https://www.joradp.dz/FTP/jo-francais/2022/F2022020.pdf).

For difficulties,16 allows a current-year schedule for persons up to date for previous years;17 permits arrears schedules conditioned on current-year payment, with the agency's schedule and certificate requirements. The amended 22 ties continued in-kind benefits to those arrangements and suspends them immediately on non-payment. Do not assume an automatic instalment entitlement or that a partial debit clears arrears. [22-121,16–17/22](https://www.joradp.dz/FTP/jo-francais/2022/F2022020.pdf).

Practical filing steps: (1) reconcile affiliation, salary/base records and assessment year; (2) identify monthly/quarterly/annual obligation and applicable due date; (3) prepare the DAC/DAS or CASNOS declaration and reconcile contributions, fund share, sector schemes, principal, penalties and prior credits; (4) use only the actual agency-authorised form/portal and obtain filing and payment receipts. The public [CNAS e-declaration portal](https://teledeclaration.cnas.dz/) visibly offers base declaration, payment, DAS and employee affiliation services. No sign-in, current authenticated fields, successful submission or payment has been tested. An office address or bank reference is not a filing receipt. G50/IRG obligations remain separate.

## Penalties and interest

| Failure | Rate or amount | Complete boundary | Official URL |
|---|---|---|---|
| CASNOS missing declaration or undetermined operating income/turnover | Provisional prior-year base with 5% uplift | Definitively acquired uplift, not 5% per extra month; actual reassessment powers remain | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |
| CNAS late contribution payment |5% of contributions due plus 1% of principal per additional month | Article 24; month runs from article 21 claim due; actual statement needed | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Late article 14 salary declaration |15% of contributions due; penalty increased 5% per month | Article 16 as amended 04-17 article 11; separate from payment failure and provisional assessment | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Missing activity declaration |5,000 DA plus 20% per month | Article 7; separate from missing worker affiliation | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Missing timely worker affiliation |1,000 DA per worker plus 20% per month | Article 13; judicial sanctions are a distinct referral | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |

**Exception before computation:**83-14 article 44 excludes public administrations/local authorities from the listed ordinary penalties, including 7,13,15(2),16,24,26,27,40–42; particular texts govern their sanctions. Articles 17–20 place the payment and worker withholding duties on the employer, with the employer share exclusively borne by it. Articles 25/25 bis and judicial enforcement make arrears more than a percentage calculation. Do not quantify an actual arrears balance, cumulative sanctions, contested period or remission without the official statement, procedure and relevant limitation/appeal rules. Tax penalties are not supplied here. [83-14,17–25 bis/40–45](https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf).

## Cross-border points

A French posted worker or treaty case needs the bilateral agreement, which is out of scope. Refer it.

## Two worked examples that recompute

**Example 1, simple.** Retained original fixture: documented ordinary contribution base 80,000 DA, employee 7,200 DA, pure employer 20,000 DA, separate social-works fund 400 DA, total 27,600 DA (derived). The original variable `fnpos` remains verbatim as a historical fixture identifier; this is not a fresh determination of the complete FNPOS financing regime. No sector scheme, reduction, arrears or base dispute is assumed. The general rates come from 15-236 article 1.

```oa-check
name: CNAS on 80,000 DA
inputs:
  gross: 80000
steps:
  - employee: gross * 0.09
  - employer: gross * 0.25
  - fnpos: gross * 0.005
expected:
  employee: 7200.00
  employer: 20000.00
  fnpos: 400.00
```

**Example 2, edge.** Retained ordinary lower-bound fixture: legally determined income/base 200,000 DA, annual SNMG 288,000 DA, contribution 43,200 DA rather than 30,000 DA (all derived). Assume a single ordinary activity with no auto-entrepreneur choice and no higher third-year/wilaya mean. For a first-year activity the actual statutory base is fixed at annual SNMG, which reaches the same 43,200 DA here; the retained generic clamp is not a substitute for that rule. For a qualifying auto-entrepreneur, the 24,000 DA option is a distinct decision. For an unconfirmed third-year mean, stop before calling 43,200 DA final liability. The original block remains verbatim.

```oa-check
name: CASNOS floor 2026
inputs:
  income: 200000
  snmg: 24000
steps:
  - base: clamp(income, snmg * 12, snmg * 12 * 20)
  - due: base * 0.15
expected:
  due: 43200.00
```

## Ask the client first

1. Salaried or self-employed?
2. Sector, for the construction add-on?
3. Declared annual income?
4. Farm or non-farm?
5. Any arrears, actual assessment, instalment schedule or period before the July 2026 amendment?
6. Activity start/cessation year, all activities/wilaya, real or forfait tax regime, and actual auto-entrepreneur status/choice?

## Sources

| Source | URL | Read on |
|---|---|---|
|15-236 article 1, full general branch allocation and article 2; Read for all CNAS branch rows and aggregate | https://www.joradp.dz/FTP/jo-francais/2015/F2015049.pdf |2026-11-15 |
|96-208 articles 1–2 and all four exclusion categories/conditions; Read for documented base exclusions | https://www.joradp.dz/FTP/Jo-Francais/1996/F1996035.pdf |2026-11-15 |
|83-14 official CNRC consolidation, articles 3–10/14–25 bis/40–45 and neighboring exceptions; Read for affiliation, payment/declaration distinction, penalties and public administration exception. Actual retained official web capture read; root direct open timed out | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |2026-11-15 |
|04-17 operative amendments to 83-14; Read for activity/affiliation, declaration penalty and employer procedures | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Dec-04-17-FR.pdf |2026-11-15 |
|15-289 original articles 13–22; Read for preserved exclusively agricultural timing and accessory mixed activity affiliation, subject to later amendments | https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015061.pdf |2026-11-15 |
|22-121 amended 14–17/22 and neighbors; Read for declaration, payment, affiliation/cessation and schedules, subject to 24-49/26-257 base changes | https://www.joradp.dz/FTP/jo-francais/2022/F2022020.pdf |2026-11-15 |
|24-49 articles 1–3; Read for real/forfait base ordering, fiscal turnover fractions, provisional uplift, auto-entrepreneur choice and commencement | https://www.joradp.dz/FTP/jo-francais/2024/F2024004.pdf |2026-11-15 |
|26-257 articles 1–2, complete amended 14 and neighbors, French translation; Read for multiple activities, rate, first year, third year mean, choice and provisional uplift | https://www.joradp.dz/FTP/jo-francais/2026/F2026053.pdf |2026-11-15 |
|26-257 Arabic original article 1/amended 14, printed 8, complete operative paragraph and neighbors; Read for expressly annual minimum and upper bound, compared with French translation. Textual reading, no visual Arabic PDF claim | https://www.joradp.dz/FTP/jo-arabe/2026/A2026053.pdf |2026-11-15 |
|26-01 articles 1–4; Read for 2026 SNMG, hours and 1 January effect | https://www.joradp.dz/FTP/jo-francais/2026/F2026001.pdf |2026-11-15 |
|97-46 articles 1–4 with 97-47 activity neighbors; Read for distinct weather and paid leave contribution rates, not full actual sector classification | https://www.joradp.dz/FTP/jo-francais/1997/F1997008.PDF |2026-11-15 |
|CNAS public e-declaration portal; Read for visible DAC/payment/DAS/employee affiliation service labels, no authenticated filing test | https://teledeclaration.cnas.dz/ |2026-11-15 |

Access record: ordinary verified local Gazette downloads frequently failed TLS EOF; the French 2026/53 PDF did download normally and its operative page was visually read. Actual ordinary official web readings and the bounded retained CNRC capture supply the stated scopes. The 1995/5 official PDF opened without readable text; its article 1 full general inclusion was not visually recovered. Direct DGI/CNAS homepage/CACOBATPH page failures are not treated as successful readings. No challenge, request disguise or TLS weakening was used. The earlier 2024 CLEISS and stale CASNOS homepage bands are not current authority for these rewritten instructions.

Not yet confirmed: complete readable 95-01 general inclusion and any special minimum/ceiling exception; a particular unusual pay item/base; current special category/reduction eligibility including ANSEJ/ANADE; exact current CACOBATPH activity classification and full paid leave/filing mechanics; the current ministerial third year activity/wilaya mean and its commencement; actual CASNOS transition assessments before 26-257 publication; multiple activity allocation/assessed maximum mechanics beyond the express paragraph; actual form fields, portal filing/payment and agency receipts; treaty/secondment entitlement; nonresident IRG outcome; tax penalties, disputed/cumulative social sanctions and remission. Rejected historical claims, unusable: rounded CNAS 26%/35%; alternate 12.5% health/10.5% retirement allocation;10%+3% monthly and 15%+2% generic late payment;5% monthly CASNOS base uplift; CNAS 10 day monthly and unverified 31 January DAS shorthand; blanket prior 2024 CASNOS 216,000/4,320,000 base band; context-only IBS 19%/23%/26%,10,000 minimum and 10% reinvested profit. Those figures are retained for traceability, never computation. Current G50/G29 timing, IRG 30,000 exemption and annual 0%–35% bands are routed to the separately rewritten payroll skill, not reverified by this social-contribution computation. Bank patterns, calendars and suggested working papers are practical controls, not legal presumptions or a return.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `algeria-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/algeria-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
