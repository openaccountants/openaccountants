---
name: algeria-payroll
description: "Use this skill whenever asked about Algeria payroll processing for employed persons. Trigger on phrases like 'Algeria payroll', 'IRG Traitements et Salaires', 'IRG withholding Algeria', 'retenue à la source Algérie', 'CNAS deduction', 'cotisation sociale Algérie', 'G50 declaration', 'DAS CNAS', 'bordereau CNAS', 'salaire net Algérie', 'PAYE Algeria', 'net salary Algeria', 'SNMG', 'salaire minimum Algérie', 'abattement 40% salaire', 'employer social security Algeria', 'gross to net Algeria', 'barème IRG', or any question about computing employee pay, income-tax withholding, or social-security contributions for Algeria-based employees. This skill covers IRG (income tax) withholding by the employer, CNAS social security (employee 9%, pure employer 25%, separate 0.5% social-works-fund share), the branch-by-branch contribution breakdown, the 40% salary abattement, the SNMG minimum wage, and filing obligations to the DGI (G50) and CNAS (monthly/quarterly according to headcount + annual DAS)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/algeria-payroll"
  jurisdiction: "DZ"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Algeria Payroll v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026, calendar year. Amounts are Algerian dinars (DA or DZD). The salary scale and tax abatements are in CIDTA art. 104, enacted by LF 2022 art. 31; LF 2026 art. 11 expressly leaves salary subsection II.3 unchanged. The ordinary social table is 25% employer, 9% employee and 0.5% social-works-fund share, 34.5% combined, rather than the unsupported former 26%/9%/35% headline. Read the base and source boundaries before computing.

## Who this applies to

Employers preparing monthly payroll working papers for Algeria-based employees, on top of `payroll-workflow-base`. Compute from a documented, separately confirmed social-contribution base and IRG taxable base. This skill does not establish that every gross-pay component is subject to both charges. Directors' fees, expatriate treaty cases and difficult arrears go to a local professional; non-monthly arrears still have the statutory treatment below.

The output is a payroll reconciliation and filing brief for a licensed Algerian expert-comptable, with source documents, assumptions, separate employer and worker liabilities, net pay and unresolved items. Self-employed income follows [algeria-social-contributions.md](algeria-social-contributions.md), not the employee path. The passing income-tax and VAT skills retain their own scope; an unresolved rule here is not cured by copying their unverified wording.

## Rates, bands and thresholds

Annual bands below are monthly-applied salary bands under CIDTA art. 104-II.3(a). The enacted annual table is read together with LF 2026 art. 11's unchanged salary locator; it is not a new annual assessment of salary every month.

| Annual taxable income, DA | Rate | Conditions and authority | Official URL |
|---|---|---|---|
| Up to 240,000 | 0% | CIDTA art. 104-I/II.3(a) | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| 240,001 to 480,000 | 23% | Same progressive scale; tax only the band portion | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| 480,001 to 960,000 | 27% | Same progressive scale; tax only the band portion | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| 960,001 to 1,920,000 | 30% | Same progressive scale; tax only the band portion | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| 1,920,001 to 3,840,000 | 33% | Same progressive scale; tax only the band portion | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Over 3,840,000 | 35% | Same progressive scale; tax only the excess | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |

| Item | Amount or formula | Complete conditions and authority | Official URL |
|---|---|---|---|
| Salary exemption | Monthly income not exceeding DA 30,000: no IRG | CIDTA art. 104-II.3(a); taxable-base determination must be confirmed separately | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| First abatement | 40% of tax; DA 1,000 minimum and DA 1,500 maximum monthly | Annual equivalents DA 12,000/18,000; reduction of tax, not income; CIDTA art. 104-II.3(a) | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Ordinary second abatement | IRG after first abatement × 137/51 − 27,925/8 | Income strictly greater than DA 30,000 and strictly less than DA 35,000; CIDTA art. 104-II.3(a) | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Special second abatement | IRG after first abatement × 93/61 − 81,213/41 | Income strictly greater than DA 30,000 and strictly less than DA 42,500; motor/mental disability, blind or deaf-mute workers, or general-regime retirees; cannot combine with ordinary second abatement; CIDTA art. 104-II.3(a) | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Non-monthly remuneration and related arrears | 10% | CIDTA art. 67(4) payments treated as a distinct monthly payment; art. 104-II.3(b) | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Occasional teaching/research/surveillance/assistant work | 10% final | Vacataire activity within art. 67(5), art. 104-II.3(c); not every additional employment | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Other occasional intellectual activity | 15% final | Art. 104-II.3(c); identify the actual activity before using it | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Food benefit valuation | DA 400 per meal in absence of justification | LF 2022 art. 21/CIDTA art. 71, retained by LF 2026 art. 7; statutory fallback, not an unconditional minimum | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| SNMG | DA 24,000 monthly; DA 138.46 hourly | 40 hours weekly, 173.33 monthly; decree 26-01 arts. 1–3, effective 1 January 2026; does not by itself establish every contribution-base rule | https://www.joradp.dz/FTP/jo-francais/2026/F2026001.pdf |

The Gazette's second-abatement upper limits say strictly below, while the inaccessible DGI page's indexed summary uses inclusive upper figures. Apply the statute's strict wording; refer equality cases and administrative rounding rather than invent a rounding convention. The two preserved employee cases are strictly inside their relevant bands.

| CNAS branch | Employer | Employee | Social-works fund | Total | Authority and official URL |
|---|---|---|---|---|---|
| Social insurance | 11.5% | 1.5% | None | 13% | Decree 15-236 art. 1 replacing 94-187 art. 2; https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015049.pdf |
| Work accidents/occupational disease | 1.25% | None | None | 1.25% | Decree 15-236 art. 1; https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015049.pdf |
| Retirement | 11% | 6.75% | 0.5% | 18.25% | Decree 15-236 art. 1; https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015049.pdf |
| Unemployment | 1% | 0.5% | None | 1.5% | Decree 15-236 art. 1; https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015049.pdf |
| Early retirement | 0.25% | 0.25% | None | 0.5% | Decree 15-236 art. 1; https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015049.pdf |
| Combined | 25% | 9% | 0.5% | 34.5% | Decree 15-236 art. 1; distinguish the fund share from the employer's own share; https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015049.pdf |
| CACOBATPH bad weather | 0.375% | 0.375% | None | 0.75% | Decree 97-46 art. 3, on social-contribution base for activities in 97-47 art. 2; https://www.joradp.dz/FTP/jo-francais/1997/F1997008.PDF |
| CACOBATPH paid leave | 12.21% | None | None | 12.21% | Decree 97-46 art. 2, employer-exclusive on social-contribution base; separate paid-leave activity scope under 97-48 requires confirmation; https://www.joradp.dz/FTP/jo-francais/1997/F1997008.PDF |

This branch allocation is not a determination of the complete FNPOS or social-works financing regime. Do not treat 34.5% as the complete employer cost or infer that a separate housing/social-works obligation is absent; establish those duties and their incidence separately before finalising a cost comparison. Do not call the bad-weather line the full construction leave/weather burden. Match the actual activity to the applicable statutory list; an unknown sector cannot be treated as contribution-free. The 2015 table is the actual operative table read, replacing the old secondary 2024-edition citation. Confirmation of any later branch amendments and special employer relief remains a stated boundary below.

## The base

### Inputs and computation

Obtain gross ordinary pay, benefits in kind, exempt or reimbursed components, the verified CNAS base, employee category and the separately verified IRG base. Split ordinary monthly pay from art. 67(4) non-monthly payments. Do not use a bank narrative or gross amount as proof that these bases coincide.

1. Reconcile gross pay and each allowance to contract, payslip and the payroll register. Apply the social-base exclusions below; obtain confirmation of any minimum, ceiling or special-category rule before finalising that base.
2. On an ordinary worker covered by the general table, employee CNAS is 9% of the verified contribution base. Keep employer 25% and the separate 0.5% fund liability distinct. Check any applicable sector contributions separately. Law 83-14 arts. 17–20 makes the employer responsible for remittance, requires worker-share withholding on payment and leaves its own share exclusively to the employer. [https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf](https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf)
3. Use the independently confirmed monthly IRG taxable income. The legacy approach is gross plus taxable accessories/benefits less pension withholding and worker social insurance; its full current CIDTA arts. 69–73 text was not recovered, so do not assume it resolves a disputed component or base.
4. First confirm the legally applicable input for the DA 30,000 exemption gate and each statutory interval. The disputed gross-versus-taxable gate is held under Sources: a confirmed IRG taxable base alone does not resolve it. Stop and refer if the gate or interval eligibility remains unresolved; do not compute IRG under this step. Only after that separate confirmation, income within the legally applicable DA 30,000 exemption is nil. Otherwise annualise the monthly taxable base, apply the progressive annual bands, and divide the result by 12. Reduce that tax by `clamp(tax * 0.40, 1000, 1500)`. The abatement is off tax, never off income. Apply the appropriate second formula only in its statutory interval; do not combine the two second abatements. [CIDTA art. 104-II.3(a)](https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf).
5. Compute net pay from gross less the worker's confirmed social and tax deductions and other documented lawful deductions. Employer contributions are not worker deductions. Reconcile each liability and payment separately; retain mathematical precision until the required official rounding is established.

### Social-base exclusions

Decree 96-208 arts. 1–2 identifies excluded family benefits and family-event payments, representative expenses (including qualifying panier, vehicle, required tools/work clothing, travel, transport and mission costs), exceptional compensation such as dismissal and retirement-departure indemnities, and residence/isolation allowances meeting its conditions. For the last category the worker must face at least 2 listed constraints: mobile cabin/tent/itinerant camp/base accommodation; continuous multi-week shift cycles followed by unpaid-allowance rest; or a remote workplace difficult to access from an urban centre. [Actual operative text](https://www.joradp.dz/FTP/Jo-Francais/1996/F1996035.pdf). This prevents a blanket instruction to charge every gross-pay component. Tax exemptions are a separate test; the 70% tax allowance claim is held below.

### Training and apprenticeship

| Item | Rate/base/deadline | Conditions and authority | Official URL |
|---|---|---|---|
| Professional training tax | Up to 1% of half-year gross payroll | Employers established/domiciled in Algeria, except public institutions/administrations, where qualifying spend is below the statutory minimum; employers with fewer than 20 employees are exempt from this tax under art. 196 ter; arts. 196 bis/ter, LF 2026 art. 18 and LF 2022 art. 56 | https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf ; https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Apprenticeship/student placements tax | Up to 1% of half-year gross payroll | Separate qualifying apprenticeship/placement expenditure test; the fewer-than-20-employee exemption in art. 196 ter covers professional training only, not this tax; arts. 196 bis/ter | https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf ; https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf |
| Both bases | Gross remuneration paid during the semester before social, retirement or IRG deductions | Art. 196 quater, LF 2026 art. 19 | https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf |
| Each effective tax rate | 1% minus qualifying expenditure divided by semester gross payroll | Derived tax amount is the shortfall; qualifying expenditure only, not all employer spending; art. 196 quinquies, LF 2026 art. 20 | https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf |
| Declaration/payment | By day 20 of the month following the semester | Special declaration, even when neither tax is due; art. 196 sexies, LF 2026 art. 21 | https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf |

CIDTA art. 196 ter exempts employers with fewer than 20 employees from professional training tax only; it does not exempt apprenticeship tax. The 2026 amendments replace arts. 196 bis, quater, quinquies and sexies, leaving this separate exemption in place. [LF 2022 art. 56](https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf); [LF 2026 arts. 18–21](https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf).

Training expenses include training, transport, accommodation, meals and insurance for the employees concerned. Apprenticeship/placement expenses include the relevant training and placement costs, master-of-placement bonuses, qualifying instructor indemnities in public establishments for technical specialities, apprentice pre-salaries, supplies, professional clothing, tools and expenses directly or indirectly within the apprenticeship actions. Where duly justified reasons prevent reaching the apprenticeship allocation, its differential may be assigned to professional training; do not assume this transfer automatically. [Art. 196 quinquies](https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf).

### Working paper and onboarding

Use one row per employee per month: name; gross; separately documented social base and worker contribution; separately documented IRG base; annual equivalent; annual scale tax; monthly tax; first and any second abatement; final IRG; net; employer own contribution; fund share; separate sector liabilities; employer cost. The original A–N spreadsheet and all constants are preserved under Sources as a historical payload because its 26% employer cell, universal bases and incomplete construction cost must not drive a current result.

If there is no payroll register, request the last 3 months of payslips, G50 declarations and CNAS bordereaux to reconcile what was applied, not to infer that past treatment was lawful. Confirm the sector before remittance; flag unknown components. Confirm wage/minimum-base questions rather than silently accepting a sub-SNMG base. Resolve year ambiguity using the stated 2026 period and route mixed self-employed income separately. Do not silently apply the old CASNOS annual band.

### Bank-statement triage and terminology

Classify case-insensitively, longest/most-specific pattern first; these are workflow hints, not authority for taxable income or contribution bases. Salary credits: `SALAIRE`, `VIR.* SALAIRE`, `PAIE`, `VIREMENT SALAIRE` indicate net salary; `ACOMPTE`, `AVANCE SUR SALAIRE` an advance clearing against salary; `PRIME`, `INDEMNITE`, `IFSP`, `IEP` a component needing classification; `RAPPEL`, `RAPPEL SALAIRE` arrears; `REMBOURSEMENT CNAS`, `IJ CNAS` a benefit/reimbursement requiring separate treatment.

Employer debits: `IRG`, `G50`, `RETENUE SOURCE`, `VERSEMENT IRG` suggest tax-liability settlement; `CNAS`, `COTISATION CNAS`, `SECURITE SOCIALE` social-liability settlement; `CACOBATPH` sector leave/weather liabilities whose split must be checked; `DAS`, `DECLARATION ANNUELLE` an annual declaration, not proof of payment; `VIREMENT PAIE`, `SALAIRES`, `NOMINATIVE PAIE` net wages paid.

Terminology: Salaire/Paie = salary/payroll; IRG (Impôt sur le Revenu Global) = personal income tax; Traitements et Salaires = salary category; Retenue à la source = withholding; Abattement = here a tax reduction; CNAS = salaried social-insurance fund; Cotisation = contribution; G50/bordereau = tax declaration/remittance document, not a CNAS return; DAS = annual salaries/employees declaration; SNMG = guaranteed minimum wage; Prime/Indemnité = bonus/allowance; Acompte/Avance = advance; CACOBATPH = construction leave/weather fund; FNPOS = social-housing fund (the old shorthand for the separate 0.5% fund component must not recast it as an extra worker deduction); Allocation chômage = unemployment allowance; DGI = Directorate-General of Taxes.

## Deadlines and filing

### CNAS registration, returns and payment

Law 83-14 arts. 3, 6, 8 and 10 covers employers with at least one worker, regardless of legal form/duration of the relationship and remuneration amount, subject to the statutory category conditions. Activity declaration is within 10 days of starting the activity; AAPI explains the salaried-employer trigger as the first hire. Each worker's affiliation request is within 10 days of recruitment. Thus the old instruction to obtain all numbers before first payroll is an onboarding objective, not the statutory deadline itself. The competent CNAS agency supplies the employer number and portal credentials. [Consolidated law](https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf); [AAPI procedure](https://aapi.dz/regimes-sociaux/).

| Obligation | Period or deadline | Conditions and authority | Official URL |
|---|---|---|---|
| Contributions, fewer than 10 workers | First 30 days after each calendar quarter | Employer makes the single remittance; law 83-14 art. 21, amended by LF 86-15 art. 118 | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Contributions, 10 or more workers | First 30 days after each month | Same art. 21; not a universal monthly duty for smaller employers | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Annual DAS | Within 30 days after calendar-year end | Nominative wages/workers, quarterly remuneration and contributions; art. 14; do not substitute 31 January | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Voluntary transfer/cessation | Due and future contributions payable within 10 clear days | Art. 24 bis, added by law 04-17 art. 13; other cessation cases follow art. 24 ter | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Dec-04-17-FR.pdf |

Open [the actual CNAS employer portal](https://teledeclaration.cnas.dz/). The public page provides employer username/password entry, a new-employer-registration request and agency-contact guidance. Its notice requires identifier/password, an Algerian telephone number (email for persons resident abroad), confirmation and an SMS/email verification code. It advertises contribution-base declarations (DAC), online payment, DAS deposit/verification, new-worker affiliation requests and employee/declaration downloads. No authenticated account, private form fields, upload schema or payment was tested. Prepare the agency affiliation evidence, period/base reconciliation and worker list; use only fields actually displayed in the authorised account, retain submission acknowledgement and separate payment proof, and stop if private validation or the current schema cannot be established. AAPI's broader El Hanaa discussion does not establish employer-form fields.

### Tax registration and filings

LF 2026 art. 8/CIDTA art. 75(3) requires the employee's unique definitive NIN in the annual salary statement and electronic filing for taxpayers served by an office equipped with the information system. LF 2022 art. 22/CIDTA art. 75(5) gives heirs 6 months after the employer/debtor's death for the deceased's salary/pension statement. [2026 amendment](https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf); [2022 provision](https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf). The full current G50/G50 ter/G29 forms, ordinary deadlines, record-retention and penalty provisions were not recovered as opened operative text; the complete legacy workflow is retained under Sources and is not a filing instruction. Do not infer a general extension from an old notice or treat tax and CNAS remittances as the same payment.

## Penalties and interest

| Failure | Consequence | Conditions and authority | Official URL |
|---|---|---|---|
| Late contribution payment | 5% of contributions due, plus 1% of principal per additional month | Law 83-14 art. 24, amended by LF 86-15 art. 119; additional monthly period runs from art. 21 due date; distinct from DAS | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf |
| Missing salary declaration: provisional assessment | Provisional contribution plus 5% permanently acquired by the fund | Art. 15, law 04-17 art. 10; prior month/quarter/year or assessment information basis | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Dec-04-17-FR.pdf |
| Late annual salary declaration | 15% of contributions due, increased by 5% per month late | Art. 16, law 04-17 art. 11, referring to art. 14 declaration | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Dec-04-17-FR.pdf |
| Omitted worker or deliberate wage inaccuracy | DA 1,000 per worker and/or inaccuracy | Art. 16 bis, law 04-17 art. 12 | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Dec-04-17-FR.pdf |

These are different defaults, not alternative all-purpose penalties. Law 83-14 art. 44 has specific public-administration/local-authority exclusions; do not apply the private-employer penalty table to them without checking that article and their particular rules. Tax penalties and the legacy 15% plus 2% CNAS claim remain held below.

## Cross-border points

CIDTA art. 104-II.3(a) applies the same monthly withholding method to pensions/life annuities paid to persons whose tax domicile is outside Algeria. [Operative clause](https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf). Treaty relief, expatriate remuneration and directors' fees require a local professional and the actual agreement/facts. The old rule making an employee pay when the employer has no Algerian tax home has not been recovered from an opened current source and remains on hold; it is not permission to omit employee tax or social obligations. Do not mix CASNOS self-employed income into the employee calculation.

## Two worked examples that recompute

The two original payloads below are preserved exactly. For each, assume an ordinary employee, no exempt/non-monthly components, a separately confirmed social base equal to the stated gross, an IRG base confirmed as gross less the 9% employee contribution, no sector/other worker deductions and no second special category. They are conditional arithmetic before any unconfirmed administrative rounding; they do not establish the disputed exemption/interval gate or prove those base assumptions for another worker.

**Example 1, simple.** Gross 120,000 DA gives IRG 22,660 and net 86,540.

```oa-check
name: Employee, gross 120,000 DA a month
inputs:
  gross: 120000
steps:
  - cnas: gross * 0.09
  - base: gross - cnas
  - annual: base * 12
  - tax_year: (min(annual,480000)-240000)*0.23 + (min(annual,960000)-480000)*0.27 + (annual-960000)*0.30
  - before: tax_year / 12
  - abate: clamp(before * 0.40, 1000, 1500)
  - irg: before - abate
  - net: gross - cnas - irg
expected:
  irg: 22660.00
  net: 86540.00
```

**Example 2, edge.** Gross 37,000 DA falls in the second abatement band: taxable 33,670 DA; IRG 1,576.92 DA.

```oa-check
name: Employee, gross 37,000 DA a month, second abatement band
inputs:
  gross: 37000
steps:
  - cnas: gross * 0.09
  - base: gross - cnas
  - before: (base * 12 - 240000) * 0.23 / 12
  - abate: clamp(before * 0.40, 1000, 1500)
  - first: before - abate
  - irg: first * 137 / 51 - 27925 / 8
expected:
  irg: 1576.92
```

**Additional case, training spend decision.** For a private employer with at least 20 employees within art. 196 bis, semester gross payroll is DA 6,000,000. With qualifying documented training spend DA 30,000 and apprenticeship/placement spend DA 45,000, the respective shortfalls are DA 30,000 and DA 15,000. If training spend instead reaches DA 60,000, its levy is nil, while the DA 15,000 apprenticeship shortfall remains. For an otherwise comparable employer with 19 employees, art. 196 ter makes professional training tax nil, but the DA 15,000 apprenticeship shortfall remains. Assume no duly justified cross-allocation and no other relief. The special declaration remains due even when the relevant tax is nil. [LF 2026 arts. 18–21](https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf); [LF 2022 art. 56/CIDTA art. 196 ter](https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf).

```oa-check
name: Semester training expenditure decision, private employer
inputs:
  payroll: 6000000
  training: 30000
  apprenticeship: 45000
steps:
  minimum: payroll * 0.01
  training_tax: max(0, minimum - training)
  apprenticeship_tax: max(0, minimum - apprenticeship)
  combined: training_tax + apprenticeship_tax
  training_at_minimum: max(0, minimum - 60000)
  training_for_exempt_employer: 0
  combined_for_exempt_employer: training_for_exempt_employer + apprenticeship_tax
expected:
  minimum: 60000
  training_tax: 30000
  apprenticeship_tax: 15000
  combined: 45000
  training_at_minimum: 0
  training_for_exempt_employer: 0
  combined_for_exempt_employer: 15000
```

## Ask the client first

1. Monthly gross ordinary salary in DZD, benefits in kind, documented social base and confirmed IRG base? If absent, obtain the last 3 months of payslips, payroll register, G50 and CNAS bordereaux.
2. Tax/payment year, monthly or non-monthly bonuses, primes, indemnités and arrears, and their documented classification?
3. Motor/mental disability, blindness/deaf-mute status or general-regime retirement relevant to the special abatement?
4. Actual sector/activity, paid-leave/weather coverage, worker headcount, SNMG/base issues and any special employer relief, including the training-tax headcount exemption?
5. Real, IFU or simplified tax regime, tax centre, NIF, CNAS employer/worker registration details and available portal access?
6. Semester payroll and qualifying training/apprenticeship/student-placement expenditure; foreign employer/treaty facts or mixed self-employed income?

Refuse to compute without gross salary or a DZD amount/conversion basis; refuse requests to omit statutory IRG/CNAS to save money or ignore an applicable exemption; refer a disputed below-SNMG base rather than assume it valid; route non-salarié income separately; refuse a definitive exact-tax assertion pending professional sign-off. Flag every missing or ambiguous input. Do not guess a supposedly conservative rate, default an unknown sector off, or present an estimate as a filed liability. Specific component treatment, CACOBATPH applicability and employer/fund incidence remain reviewer decisions when facts or law are unresolved.

## Sources

| Source | Official URL | Read for | Read on |
|---|---|---|---|
| LF 2022, law 21-16 | https://www.joradp.dz/FTP/jo-francais/2021/F2021100.pdf | Arts. 21–22 (CIDTA 71/75), art. 31 full 104-I/II.3 and adjacent subsections/III; art. 56 full 196 bis–octies including the fewer-than-20 training exemption; operative paragraphs and neighbors | 2026-11-15 |
| LF 2026, JO 88/2025 | https://www.joradp.dz/FTP/jo-francais/2025/F2025088.pdf | Arts. 7–8 (71/75), 11 (104 unchanged salary locator), 18–21 (196 bis/quater/quinquies/sexies), with operative neighbors | 2026-11-15 |
| Presidential decree 26-01 | https://www.joradp.dz/FTP/jo-francais/2026/F2026001.pdf | Arts. 1–4, wage/hour figures, repeal and 1 January 2026 effect | 2026-11-15 |
| Decree 15-236, JO 49/2015 | https://www.joradp.dz/FTP/JO-FRANCAIS/2015/F2015049.pdf | Full art. 1 contribution table and art. 2, publication neighbors; text extraction read, not visual inspection | 2026-11-15 |
| CNRC official consolidated law 83-14 | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Loi-83-14-FR.pdf | Arts. 3–25 bis, 26–27 neighbors and art. 44 exclusions; source lists amendments 86-15/98-12/04-17 | 2026-11-15 |
| Law 04-17 actual amendment | https://cnrcinfo.cnrc.dz/wp-content/uploads/2021/02/Dec-04-17-FR.pdf | All operative arts. 1–25, particularly 6/10/11/12/13 amending activity/declaration/penalty rules | 2026-11-15 |
| Decree 96-208 | https://www.joradp.dz/FTP/Jo-Francais/1996/F1996035.pdf | All operative base-exclusion clauses and listed residence/isolation constraints, adjacent decree boundaries | 2026-11-15 |
| Decrees 97-46/97-47, JO 8/1997 | https://www.joradp.dz/FTP/jo-francais/1997/F1997008.PDF | Full 97-46 arts. 1–4 and 97-47 arts. 1–3/activity list; separate 97-48 list only partly read, not treated as fully verified | 2026-11-15 |
| AAPI, Régimes sociaux | https://aapi.dz/regimes-sociaux/ | Full official page, especially CNAS concepts/procedures/headcount periods/DAS and affiliation documents; summary distinguished from Gazette | 2026-11-15 |
| CNAS actual public employer portal | https://teledeclaration.cnas.dz/ | Read for public credentials/services and 2FA notice only; no authenticated filing or private form validation | 2026-11-15 |
| DGI current salary page and codes index | https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires | Not read as a live page: direct retrieval timed out/SSL failed; browser failed before navigation. Indexed primary content retained in research only, not substituted for an opened source | Not read; attempted 2026-11-15 |

### Historical payload and unavailable current confirmations

The previous version's primary-source read dates were 2026-11-01. Its DGI evidence was an Internet Archive salary capture of 1 September 2026, an IFU capture of 19 February 2025 (page dated 24 October 2023, subject to later laws), and an 8 October 2026 G50/training/apprenticeship extension capture. Those archive pages were not freshly read, and their dates have not been renewed. Its CLEISS 1 January 2024 edition was a secondary contribution comparison; the actual Gazette table now replaces it as authority. The old statement that mfdgi.gov.dz/cnas.dz refused direct and Chrome access on 1 November is historical, not today's access result; today's CNAS public portal was actually read.

Not yet confirmed: the complete current CIDTA consolidation and intermediate salary amendments; whether any post-2015 branch rates or special relief changes affect the general table; universal CNAS ceiling/minimum/SNMG and special-category base rules; disputed gross-versus-taxable DA 30,000 gate and administrative rounding/equality handling; part-year salary treatment and spouse/dependent reductions; full paid-leave activity matching under 97-48; the current tax form/private portal fields and the legacy tax filing/penalty/base/exemption rules listed below. These are outside usable filing/computation guidance. A source's HTTP response or indexed text is not a current legal read.

**Retained legacy base and tax-rule holds.** The old salary-base instruction was gross including benefits/accessories less pension withholding/worker social insurance; isolation/residence allowance exempt up to 70% of basic salary; promoted-zone food/lodging excluded; meal benefit not below DA 400. The actual opened law corrects the last item to DA 400 **in absence of justification**. The other component/base assertions remain unusable until current arts. 69–73/68 are opened. The old assertion that wages must be computed and paid in Algerian dinars has not been independently recovered as an operative employment-law rule; DZD remains the working-paper currency. The old universal uncapped-gross/SNMG-floor instruction and blanket refusal below that floor are also not established by the wage decree alone. Preserve professional referral for a questionable base rather than claiming the unsourced universal rule.

**Retained legacy tax workflow holds.** The old G50 real-regime route was Jibaya'tic where the tax centre uses it, otherwise paper Série G n° 50 to the head-office/main-establishment receiver; enter taxable sales/output TVA/input TVA/salary IRG; use form box numbers (never confirmed); attach the Code TCA art. 29 input-VAT supplier statement; file/pay inside the first 20 days after the month (payment could be later than filing inside that limit); retain stamped/online acknowledgement. It claimed a no-penalty electronic-payment delay up to 10 days through no fault of taxpayer or bank. These current form, VAT attachment, routing and grace-period assertions were not recovered from an opened official text and are not instructions to file or defer payment.

The old calendar was G50 monthly within the first 20 days; IFU G50 ter by 20 after the quarter; G29 with NIN by 30 April; cessation G29 within 10 days; payslip records until the fourth following year and nil wording “retenue IRG: neant”. The old tax penalties were 10% for no G50/payment, increased to 25% after one unremedied month after notice (134-2), and 5% of annual payroll for missing G29. The foreign-employer-without-Algerian-tax-home employee self-payment rule is also held. New NIN/electronic filing and heirs' 6-month rules above are separately sourced; they do not verify the unchanged ordinary deadlines/penalties. The old CNAS universal-monthly/31-January dates are corrected to the statutory headcount/30-day rules above; the old 15% plus 2% monthly CNAS penalty remains unsupported and must not replace the distinct current declaration/payment provisions.

**Retained legacy defaults and spreadsheet, not executable current instructions.** The old defaults were year 2026; unknown construction sector off/flagged; full exemption at taxable pay no more than DA 30,000; 40% tax abatement, DA 1,000/1,500 limits; social base floored at DA 24,000; uncapped gross; DZD; and 26% employer/9% worker/35% combined. Missing inputs were to use a supposedly conservative assumption. Keep the sourced tax rules above, but do not use unsupported 26%/35%, universal bases or sector-off defaults. The old onboarding CASNOS band DA 288,000–5,760,000 is not a universal usable rule: current non-salarié amendments include multi-activity, first-year/third-year conditions and auto-entrepreneur choices, handled in the social skill.

The following original A–N payload and H formula are retained verbatim for traceability only; the 26% employer cell is unsupported, C/E require verified bases, M is weather only, K omits any extra worker sector deduction and N omits the separate paid-leave levy/fund incidence. Reconcile the current working paper above instead.

| Col | Header | Formula / source |
| -- | -- | -- |
| A | Employee name | input |
| B | Gross monthly salary (DZD) | input |
| unverified: C | Employee CNAS 9% | `=B*0.09` |
| D | Salary after CNAS | `=B-C` |
| E | Monthly IRG base | `=D` |
| F | Annual IRG base | `=E*12` |
| G | Tax before abatement, monthly | `=H/12` |
| H | Tax on annual base | nested IF on F using subtract constants (55,200 / 74,400 / 103,200 / 160,800 / 237,600) |
| I | Abatement | `=MIN(MAX(G*0.40,1000),1500)` |
| J | IRG monthly (final) | `=IF(D<=30000, 0, MAX(0, G-I))`, then the second abatement formula if D is 30,001 to 35,000 |
| K | Net pay | `=B-C-J` |
| unverified: L | Employer CNAS 26% | `=B*0.26` |
| unverified: M | CACOBATPH (construction only) | `=IF(construction, B*0.375%*2, 0)` |
| unverified: N | Total employer cost | `=B+L+IF(construction, B*0.375%, 0)` |

- **IRG formula for column H**: =IF(F<=240000,0, IF(F<=480000, F*0.23-55200, IF(F<=960000, F*0.27-74400, IF(F<=1920000, F*0.30-103200, IF(F<=3840000, F*0.33-160800, F*0.35-237600)))))  _(Section 11 formulas)_

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `algeria-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/algeria-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
