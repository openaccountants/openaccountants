---
name: armenia-social-contributions
description: "Use for Armenian 2026 pension social payments, military stamp and universal health insurance. Establish participation, residence status, age, elections, income class, register entry and continuation before calculating employee or entrepreneur amounts. Covers ordinary monthly and annual pension caps, elected participants, employer-funded childcare, stamp populations and periods, health funding and separate transitional reporting/payment. Includes two conditional examples with supplementary controls preserved in the research record. Trigger on Armenia social contributions, funded pension, stamp payment, health insurance or entrepreneur contributions. Checked against the law: the health deadline wording discrepancy, separate erroneous-payment procedure, specialist exceptions, live acceptance and named accountant attestation remain open; independent source review is recorded in the country research."
version: 0.3
jurisdiction: AM
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia social payments, stamp payments and health insurance

## Who this applies to

2026 computation, checked against the law, read 24 October 2026, for employees, individual entrepreneurs/notaries and specified self-employed persons. Establish the person, income class, period, residence status, pension participation/elections and health-register entry before calculating. Read with `social-contributions-workflow-base` and [payroll](armenia-payroll.md); ordinary salary PIT is not the same legal obligation as pension, military stamp or health insurance. Fresh whole-pack review and named accountant attestation remain pending.

Do not treat bank references or an unknown employment status as proof of a statutory category. Obtain contracts, accrued salary and paid contract-income registers, birth date, residence permit, pension election/cessation/cap-waiver documents, other income sources, health-register notice and payer status, social-package status, prior returns and payment accounts.

## Rates, bands and thresholds

| Obligation | Ordinary 2026 method | Primary source |
|---|---|---|
| Pension, mandatory pre-retirement salary branch | 5% through AMD 500,000 monthly; above that, 10% less AMD 25,000, subject to cap/elections | [Pension 5–6][pension] |
| Pension ordinary monthly base ceiling | 15 × statutory monthly minimum wage; AMD 1,125,000 using AMD 75,000 | [Pension 6(6)][pension], [wage 1][wage] |
| Ordinary mandatory monthly pension ceiling | AMD 87,500 under the preceding branch, absent cap waiver/special case | [Pension 6(7)][pension] |
| Ordinary annual pension base ceiling | 180 × minimum wage on 1 January; AMD 13,500,000 for 2026 | [Pension 6(6)][pension], [wage 1][wage] |
| Ordinary mandatory annual pension ceiling | AMD 1,050,000 under the annual 10%-less-300,000 branch, subject to status and aggregate reconciliation | [Pension 6(7)–(9)][pension] |
| Pension actual-business annual income | 5% through AMD 6 million; above, 10% less AMD 300,000, with applicable caps | [Pension 2(27), 6(2)(2)][pension] |
| Pension specified turnover-tax activities | AMD 5,000 monthly, separate from the ordinary actual-income method | [Pension 6(2)(3), (5)][pension] |
| Military stamp, eligible monthly agent population | AMD 1,000 through AMD 1 million base; AMD 15,000 from AMD 1,000,001 | [Stamp 9–12][stamp] |
| Military stamp, eligible annual population | AMD 12,000 through AMD 12 million base; AMD 120,000 from AMD 12,000,001 | [Stamp 9–12][stamp] |
| Health statutory full premium | AMD 129,600 annually / AMD 10,800 monthly | [Health 13][health] |
| Health 2026 eligible employee contribution | AMD 4,800 through AMD 500,000 salary; full AMD 10,800 from AMD 500,001, after entry/status tests | [Health 45–46][health] |

## The base

### Pension participation is more than a birth-year switch

Article 5 includes employees, notaries and entrepreneurs born on/after **1 January 1974**, and pre-1974 persons who submitted the pension-fund choice application. That election cannot simply be reversed. Resident-status foreigners/stateless persons follow the general rule unless an applicable international agreement says otherwise. A person reaching pension age does not automatically disappear from payroll: cessation needs the prescribed application; salary cessation starts the following month, while the business-income cessation date is the year's 1 January under the statutory branch. [5][pension]

The Article 6(3) elected/continuing-after-pension-age branch uses **5%**, rather than automatically applying the mandatory young-worker 10%-less-25,000 limb. The start dates differ by income class. Establish actual status and applications. Self-employed income has its own voluntary-payment route. The statutory definition excludes exclusively microenterprise entrepreneurs from the ordinary entrepreneur definition and includes them in the self-employed definition; do not charge them the turnover-regime monthly amount just because they have a registration. [2(2)/(9), 5–7][pension]

For the ordinary mandatory branch with eligible monthly base B and no cap waiver:

`capped_B = min(B, 15 × minimum_wage)`; `payment = 5% × capped_B` through 500,000, otherwise `10% × capped_B − 25,000`.

The law's salary definition includes specified contractual income. Monthly aggregate income includes salary/equivalents accrued by all employers and contract income paid in that month. Annual aggregate income includes the specified business/salary/contract categories. Article 6(6)–(9) provides multi-source ceilings; turnover-activity amounts enter the maximum and voluntary self-employed payments have a stated exclusion. Article 6(11) permits an election not to apply the ordinary base ceilings. Use the separate participant reconciliation below; do not reduce each employer's withholding in anticipation of the same personal refund. [2(4), 6–7][pension]

### Salary equivalents and the actual pension applications

The implementing salary list is joint **416-N/107-N/561-N**, not a rule that every taxable benefit is pensionable salary. Within employment contracts/hiring acts, it includes basic/additional pay, overtime, night/rest/holiday work, additions and bonuses regardless of frequency/funding, paid idle time including reinstatement, lawful strike pay, paid special breaks, extra workload and mandatory work-related medical-examination time. Annual paid leave, specified paid study/public-duty leave and **unused-leave compensation on termination** are included. Its wage-fund one-off-payment limb excludes statutory compensation, including statutory temporary-incapacity/maternity benefits, aid and social-needs payments. Author remuneration is included except Code 4(1)(34) royalties. Civil work/service-contract income is a separate statutory limb, not an employment benefit. Keep this pension list separate from PIT exemptions and the health salary test. [Joint list 1(1)–(3)][salarylist]; [Pension 2(1)(4)][pension]

For a **cap waiver or restoration**, use current **189-N**, paragraphs 2–20 and Forms 1–4:

| Applicant | Waiver / restoration route | Effective date |
|---|---|---|
| Ordinary employee | Signed paper request to employer; employer retains it and submits signed electronic **Form 1 / Form 3** through personalised accounting by the **last working day of receipt month** | First day of the month after submission to the tax authority |
| Entrepreneur/notary or employee of a tax-agent-exempt employer | Signed electronic **Form 2 / Form 4** through personalised accounting | Entrepreneur/notary: 1 January of submission year; employee: first day of following month |

The paper request identifies employer, applicant/full identity-document details, public-service number or alternative certificate, date and signature. Employer electronic forms identify employer/TIN, worker/identifier, date and registration number; direct forms also contain the relevant employer identity/TIN fields. Multiple employers can use any one employer. A person with employee and entrepreneur/notary income needs separate monthly/annual elections. Restoration is available to the paragraph 6 participants who applied for waiver; the paragraph 2 six-month rule runs from the **2017 commencement**, not afresh from each 2026 election. Mistaken employee submissions can be cancelled only before any following-month personalised return, including another employer's; entrepreneurs/notaries must cancel within that year and before the annual return. [189-N 2–20, Forms 1–4][capforms]

For **pension-age cessation**, current joint **182-N/127-N** Annex 2 requires name/address, TIN if any, identity-document type/number, public-service number or alternative, date and signature. Ordinary employees hand the signed paper request to the employer, which communicates it through the statutory employee-registration application; it is legally submitted to the tax authority **when handed to the employer**. Entrepreneurs/notaries, self-employed persons and exempt-employer employees apply electronically. Pension 5(7) ends salary and turnover-activity payments from the following month's first day, and business-income payments from 1 January of that year. A separate application to the pension-register manager to receive a funded pension triggers SRC notice to the employer within one working day after SRC receives the register information. Retain that notice; birthday alone is insufficient. This cessation procedure and its deemed filing date differ from the cap-election forms. [Pension 5(4)–(7)][pension]; [joint 182-N/127-N, Annexes 1–3][cessation]

### Multiple sources: reconcile paid pension contributions once

For the ordinary mandatory pre-retirement participant without a cap waiver, retain each agent's salary/contract base, assessment, remittance and reporting period. Compare the person's settled monthly payments with the applicable Article 6(7) monthly maximum, including the AMD 87,500 ceiling at the ordinary maximum base. Do not substitute one agent's income for all sources or give every agent the individual's full refund. The actual return mechanism is joint **181-N/126-N**, current incorporation from 1 July 2023. [6(6)–(9)][pension]; [joint procedure 2–6][pensionrefund]

For example, two employers each accrue AMD 1 million and each withhold/remit AMD 75,000 under the ordinary branch. Total paid is AMD 150,000; the applicable aggregate maximum is AMD 87,500, leaving AMD 62,500 for the participant's refund procedure. The full period obligation must first be discharged. Accrued withholding alone is not cash available for refund. [6(2)/(6)/(7)][pension]; [joint procedure 6/11][pensionrefund]

For annual reconciliation, joint paragraph 2(2) defines the annual maximum after subtracting annual social payments paid for turnover-tax activities from the statutory annual maximum. Paragraph 3 uses the profit-tax calculation for the employee who is also an entrepreneur/notary and takes the year's monthly calculated social payments into account. Pension 6(9) excludes voluntary self-employed payments from this maximum; apply the actual status branch rather than adding every bank debit. Use the contribution card after prior monthly refunds, because joint paragraph 13 reduces the recorded paid amount when a refund is made. Do not refund the same excess again in the annual calculation. [6(6)–(9)][pension]; [joint procedure 2–3/13][pensionrefund]

In the preceding two-employer example repeated for 12 months, original paid contributions total AMD 1.8 million. Twelve monthly refunds total AMD 750,000, leaving AMD 1.05 million recorded paid. With no other sources/status changes, that already equals the ordinary annual ceiling; an additional AMD 750,000 annual refund would duplicate the monthly refunds. [6(7)][pension]; [joint procedure 13][pensionrefund]

Refund routing is to the **participant's own bank account**, not a second employer payroll credit or the pension register manager. Under current joint paragraphs 10–12, the tax authority obtains bank-account/ownership/validity information from the CBA's central bank-account register and sends Treasury a payment instruction within **two working days after receiving that information**. The participant can supply an account belonging to them under 10.1. Treasury transfers within **two working days after the instruction**. These are different event-based clocks, not a guaranteed four-day period from payroll filing. The instruction identifies the participant, public-service number or stated alternative, bridge account, bank/account, refund amount and period. A filed cap-waiver application under Pension 6(11)/(12) excludes this excess-refund route under joint paragraph 15. [Joint procedure 4–6/10–15][pensionrefund]

**Employer-funded exception:** Article 6(10) requires AMD **3,000 per month from the employer's own funds** for the specified participant on childcare leave, from the month following leave commencement through the month the child reaches two, inclusive, while the employment relationship exists. Do not repeat a universal “no employer pension payment” rule. This is distinct from ordinary employee withholding and from state co-financing. [6(10)][pension]

### Military stamp: population, base and separate periods

Article 11 covers the specified resident employment/contract-income populations, non-resident Armenian-source/work populations and registered entrepreneurs/notaries. It excludes the specified no-income/no-base cases and foreigners/stateless persons without Armenian residence status. If eligible civil-contract income is insufficient to withhold the stamp, 11(3.1) instead requires the agent to pay from its own funds; it is not permission to show negative net income or erase liability. Specified military-family refunds require their own application/procedure. [11][stamp]

Article 9 distinguishes monthly agent/qualifying exempt-employer populations from annual non-agent/entrepreneur/notary populations. Employee base is salary/equivalents and relevant civil-contract income. Entrepreneur stamp base is the specified **turnover or gross income** from regime reports, including mixed-regime aggregation, rather than automatically taxable business profit. Tax-agent withholding is calculated per agent under Article 14; do not apply pension aggregate-cap rules to stamp payments. [9, 12–15][stamp]

The 2026 monthly/annual rates above follow HO-477-N. Its early employee branch covers salary of AMD 200,001 or more and applies to relationships from **1 December 2025**, although published 24 December and effective the next day. The other change begins **1 January 2026**. A universal “payment on/after 25 December” switch is wrong for historical recomputation. Reconstruct earlier periods under the then-operative table. [HO-477-N 1–2][stamp-amend]

### Health insurance: entry, continuation and payer

Read the current September 2026 consolidation, not only the initial December law. Article 11 covers Armenian citizens in the enumerated groups and specified resident-status foreigners/refugee populations. Citizenship alone does not decide payment, and covered status is not necessarily the same as employee deduction. Register status, population, funding and commencement all matter. [11–12, 45–46][health]

For the ordinary employee phase:

- The initial November 2025 reported-salary test is tied to returns submitted as of 25 December 2025 and the Article 45(1)(3) conditions.
- In **January–November 2026**, salary reaching AMD **200,001 per employer** activates the Article 45(1)(4) branch from the following month's first day and applies to that following month's salary onwards. It is not automatic same-month entry merely because a pay amount crossed the threshold.
- Once the branch is triggered, the law continues calculation despite a salary reduction during the following **12 months**. Below AMD 200,001 is therefore not a universal zero-payment band for an existing participant. Later phases have their own dates; do not backdate 2027 populations.

[45][health]

For established 2026 payers, Article 46(9) sets the AMD 4,800 agent amount through 500,000 per employer and the full monthly rate from 500,001. Article 46(17) provides AMD 6,000 state financing for the specified lower-paid group **except social-package beneficiaries**. Those beneficiaries have a separate AMD 6,000 self-payment obligation under 46(18). A low or absent salary can still require the agent's AMD 4,800 under 46(20). After employment ends, 46(19) provides self-payment during the stated continuing insured period. A state-paid status/refund branch under 46(16) must be tested separately; do not assume every covered worker is automatically exempt at payroll. [46][health]

Multiple calculation bases/employers require the Article 14(7)–(8) total-premium and application/refund reconciliation, not an invented proportional deduction. Obtain the Fund record and payment evidence before recognising a refund. Employer payment of all or part is permitted under 14(9); tax treatment of a particular employer-paid benefit is a separate question. [14][health]

The specified 2025-income entrepreneur/notary phase uses the AMD **2,400,001** gross-income/turnover test in 45(1)(5). Under the April-amended transitional rule, the 2026 annual amount is the full statutory premium, payable by **20 July 2026**; covered status follows full payment as prescribed. Suspended/restarted activity and special payment arrangements have separate 46(20.1)/(20.2) provisions. This Guide does not invent a monthly employee-band election for an entrepreneur. [45–46][health]

## Deadlines and filing

Pension Article 7 makes the employer the agent, ties ordinary salary payments/reporting to the Tax Code monthly deadlines and separates annual/self-payment routes. Ordinary monthly PIT/social return and PIT payment are through the following month's **20th** under Tax Code 156/158; stamp Article 14 also uses the following month's 20th after calculation. Pension Article 8 governs personal-account recording, amended liabilities and former-worker corrections. Reconcile assessed amounts, remittance dates and allocation to each obligation. [Pension 7–8][pension], [Stamp 13–15][stamp], [Tax Code 156/158][code]

### Separate health payment and register workflow

Health 46(14) says the specified employee premiums are **not reflected in the 2026 monthly income-tax calculations**. Under 46(13), salary in those returns supplies the calculation basis, but **salary reductions in amended returns are disregarded** for this calculation. Do not insert a health column, reverse an entered payer merely because payroll was reduced, or net a pension refund against health. Current 46(11) expressly requires the specified December 2025/2026 employee payments by the **20th inclusive of the month of obtaining payer status**. Apply this current statutory transition to its stated population. General 14(3) and the older Ministry leaflet do not replace it; reconcile the Fund status/payment notice for the particular month. The older wording is recorded as historical evidence, not a missing statutory deadline. Entrepreneur/notary 2026 full-year payment instead follows 46(12)'s **20 July 2026** deadline. [14–15/46(11)–(15)][health]; [1986-N 16–17][healthnotice]

The Fund's current Armenian payment instructions distinguish these routes. Recheck the published details before an actual transfer; these are separate from PIT, pension and stamp accounts. [Fund payment instructions][healthaccounts]

| Payment population | Published account | Required allocation details |
|---|---|---|
| Employee, entrepreneur/notary and exempt-employer employee premiums to the state budget | **900005003703** | TIN and relevant persons' public-service identifiers |
| Insured person who must self-pay during the continuing 12-month period, including after employment ends | **900018010380** | Person's name, surname and public-service identifier |
| Social-package beneficiary's partial premium | **900018010471** | Employer TIN and person's public-service identifier |

All three instructions specify purpose **«Առողջության համընդհանուր ապահովագրավճար»**. Payment evidence must retain payer, person, period and amount, not only a total bank debit. [Fund payment instructions][healthaccounts]

Under current **1987-N 3/5–7**, SRC supplies each month's 2026 data by the following month's 25th and the relevant paid-person list within **three working days following full payment**. The ordinary employer list depends on the whole premium amount for its payer employees being transferred. SRC's instruction to Finance follows full settlement/list preparation within two working days; Finance transfers within one working day after receipt. Those are inter-authority settlement clocks, not a guarantee that a salary bank debit creates immediate insured status. Annex 4/8 begin **1 January 2027**, so they are not 2026 authority for the future population/exchange branches. Retain the Fund register/status notice alongside the SRC report and treasury allocation. [1987-N 2, Annex 3–10/15–16, Forms 1–2][healthsettlement]

The Fund register is accessible through the electronic-health system/mobile application. Its individual account records calculated/paid premium, difference, group and payer/insured-status dates. Current **25-N 3–4/7/11** provides monthly source-data updates. Current **1986-N**, amended 26 September 2026, provides status/payment/late-payment notices normally within three working days after the relevant ground; the notice includes legal basis, date, amount, deadline/method and consequences. A wrong recipient/content notice is cancelled by an additional notice within one working day after discovery. This is a notice correction, not permission to reduce a statutory premium. [25-N][healthregister]; [1986-N 4–17][healthnotice]

### Health refunds: participant excess is not an erroneous treasury transfer

For several bases/employers, Health 14(7)–(8) and the Fund board's **5 February 2026 decision 1, Annex 6** govern the actual excess-premium application. Settlement and register completion must exist; paragraph 5 permits the monthly application from the first day of the following month after the register information is entered. Paragraph 6 states the corresponding annual route. A one-time application supports later monthly/annual excess refunds. Form 2 identifies name/full name, public-service number, monthly/annual selection, bank/account or the stated no-account identity route, date, signature, consent and obligation to update changed details. The adopted paragraph 8 route is **info@uhif.am**; the Fund also publishes its online form with own-account confirmation, contact details, identifier/alternative and monthly/annual selection. No application has been submitted for a real person here. [Health 14(7)–(8)][health]; [board Annex 6, paragraphs 4–14/Form 2][healthrefund]; [published online form][healthrefundonline]

The Fund matches SRC payment information against its register and checks the actual excess. Paragraph 10 gives one working day after application for its conclusion, paragraph 12 two working days for transfer after that conclusion, subject to entitlement. The statutory three-working-day rule depends on settlement/register completion and an application; it is not an unconditional three days from salary withholding. No excess means rejection; only the existing excess is refundable, with written reasons under paragraphs 15–17 within five working days of application. The separate 46(16) state-paid-population refund has its own **five-working-day clock after SRC informs the Fund** and one-time electronic application. Do not apply the three-day rule to every refund. [Health 14(7)–(8)/46(16)][health]; [board Annex 6, paragraphs 3/5–17][healthrefund]

Health 14(12)'s **mistaken payment without liability / transfer above assessed liability** is a different Government-procedure branch. Its commencement is expressly conditional on that implementing act. The board participant-excess form does not establish that separate procedure or authorize cancelling the next employer payment. The current implementing act and its operative date have not been established in this research. [14(12) commencement note][health]

The Fund also publishes an actual **mistaken-transfer application**, a separate one-page DOCX listed on its official documents page. It asks the Fund to verify a transfer mistakenly made **to the Fund's account**, gives the reason/amount and claimant's own bank/account, and requires identity/contact details, company/entrepreneur registration evidence where applicable, representative authority and payment proof, with signature/date. This is useful evidence for that Fund-transfer case. Its text contains no Government enactment, general Treasury procedure or commencement clause; it does not establish the distinct Health 14(12) state-budget branch. [Fund document listing](https://www.uhif.am/am/documents); [actual mistaken-transfer form](https://vnxctzddivqjdrwwspgw.supabase.co/storage/v1/object/public/documents/official_docs/1788347293816_1775200508371_document.docx), read visually and structurally 26 October 2026.

## Penalties and interest

Do not apply one arrears formula to all lines. Health Article 16’s import of tax-law late-payment terms takes effect **1 January 2027**, under Health Article 45(1)(8); it is not a current 2026 basis for charging the Tax Code interest rate. Tax Code 401 prescribes 0.075% daily with its 730-day limit for its own tax branch. Establish any other operative 2026 health collection/sanction basis separately before assigning an amount; no general 2026 health-interest exemption is inferred. Stamp Article **13(4) explicitly excludes tax-law late-payment interest**, although recovery/enforcement remains. Pension corrections, penalties and debt require their own legal/account reconciliation. No stamp interest is computed merely by analogy with PIT. [Health 16, 45(1)(8)][health], [Stamp 13][stamp], [Tax Code 401–403][code]

## Cross-border points

Pension and stamp residence-status tests differ from PIT residence/source. Check permits, employer/agent identity, contract versus employment, place of work and actual international social-security agreement before excluding a posted worker or foreign citizen. No treaty coverage certificate or agreement-based relief is verified here. Health resident-foreigner eligibility is expressly addressed in Article 11, subject to group/phase/status. [Pension 5][pension], [Stamp 9/11][stamp], [Health 11/45][health]

## Two worked examples that recompute

Hypothetical AMD inputs. Status, eligible base and operative month are assumed established. No control proves refund, return acceptance, health entry or final net pay.

### 1. Ordinary mandatory pension limbs

Pre-retirement mandatory participant, no cap waiver or other sources: 300,000 gives 15,000; 600,000 gives 35,000. [6(2)][pension]

```oa-check
name: Armenia ordinary mandatory pension two limbs
inputs:
  lower_base: 300000
  upper_base: 600000
steps:
  - lower_payment: lower_base * 0.05
  - upper_payment: upper_base * 0.10 - 25000
expected:
  lower_payment: 15000
  upper_payment: 35000
```

### 7. Existing health payer after salary drops

Entered payer still within continuation period, ordinary non-social-package lower-paid branch, current salary 150,000: agent amount 4,800 plus state financing 6,000 = full 10,800. The drop below 200,001 does not itself set the contribution to zero. [45(1)(4), 46(9)/(17)][health]

```oa-check
name: Armenia continuing health payer lower salary funding
inputs:
  established_agent_amount: 4800
  established_state_financing: 6000
steps:
  - full_monthly_funding: established_agent_amount + established_state_financing
expected:
  full_monthly_funding: 10800
```

## Ask the client first

- Which period and each income class, earned/paid dates, employers and other sources apply?
- What birth date, Armenian residence status, pension participation/election/cessation/cap waiver and childcare leave dates are documented?
- Which business regime and annual income/turnover returns establish each distinct base?
- What health-register group, entry month, continuation period, social-package/state-paid status, multiple-source funding and termination date apply?
- Which declarations, assessments, treasury allocations, refunds and arrears exist?

## Sources

| Official source and actual read scope | URL | Read on |
|---|---|---|
| [Funded Pensions law, consolidation 224823][pension], targeted Articles 2, 5–8, metadata applicable from 18 May 2026; read 24 October 2026. Historical consolidation 91100 was discovery only. | https://www.arlis.am/hy/acts/224823 | 2026-10-24 |
| [Minimum Monthly Wage law][wage], Articles 1–4 and metadata; read 24 October 2026. Its 75,000 statutory amount is used where Pension Article 6 expressly cross-refers; it is not a universal gross salary or every statutory calculation base. | https://www.arlis.am/hy/acts/172160 | 2026-10-24 |
| [Current military compensation/stamp law, consolidation 230046][stamp], Articles 9–15 and September 2026 metadata; read 24 October 2026. | https://www.arlis.am/hy/acts/230046 | 2026-10-24 |
| [HO-477-N][stamp-amend], actual amendment and commencement; read 24 October 2026. | https://www.arlis.am/hy/acts/218648 | 2026-10-24 |
| [Universal Health Insurance law, consolidation 230432][health], targeted Articles 11–16 and 45–46, September 2026 metadata; read 24 October 2026. Earlier April consolidation 224417 was compared for those provisions: September change in targeted transition text is the ministry-name update, not a new salary formula. Full medical-benefit rules not implemented. | https://www.arlis.am/hy/acts/230432 | 2026-10-24 |
| [Current Armenian Tax Code][code], targeted Articles 142, 147, 150–158, 401–403; read/reused 24 October 2026. PIT methods are in the companion Guides. | https://www.arlis.am/hy/acts/215611/latest | 2026-10-24 |
| Current native Pension 6(6)–(9): monthly/annual aggregate, maximum, turnover and voluntary self-employed distinctions | https://www.arlis.am/hy/acts/224823/latest | 2026-10-25 |
| Joint 181-N/126-N current full ordinary multiple-source refund procedure, Annex paragraphs 1–15, incorporating 2023 changes | https://www.arlis.am/hy/acts/179268/latest | 2026-10-25 |

| Joint 416-N/107-N/561-N: complete pension salary-equivalent list 1(1)–(3), including benefits/leave/royalty distinctions and current metadata | https://www.arlis.am/hy/acts/126230/latest | 2026-10-26 |
| 189-N: full procedure 2–20 and actual Forms 1–4, current status; historical commencement waiting period distinguished | https://www.arlis.am/hy/acts/114736/latest | 2026-10-26 |
| Joint 182-N/127-N: complete ordinary cessation Annexes 1–3, actual Annex 2 form and register-to-employer notice | https://www.arlis.am/hy/acts/121967/latest | 2026-10-26 |
| Fund current native payment instructions: all three account populations, identification and purpose; English page compared | https://www.uhif.am/am/requisites | 2026-10-26 |
| 1987-N: commencement and complete ordinary Annex 3–10/15–16, Forms 1–2; Annex 4/8 explicitly 2027 | https://www.arlis.am/hy/acts/219163/latest | 2026-10-26 |
| Current 25-N: targeted Annex 3–4/7/8/11 and 2 October 2026 incorporation metadata; individual account/access/update fields | https://www.arlis.am/hy/acts/219364/latest | 2026-10-26 |
| Current 1986-N: all Annex 1–17 and 26 September 2026 incorporation metadata; corrected notice is distinct from liability adjustment | https://www.arlis.am/hy/acts/219155/latest | 2026-10-26 |
| Actual Fund board 5 February 2026 decision 1 Annex 6: all 5 PDFpages rendered/read, paragraphs 1–17 and Forms 1–2; discovered via Fund documents UI | https://vnxctzddivqjdrwwspgw.supabase.co/storage/v1/object/public/documents/official_docs/1771924519311_document.pdf | 2026-10-26 |
| Current published blank online refund form, monthly/annual selection, identity/account/update fields; no application submitted | https://www.uhif.am/am/refund | 2026-10-26 |
| Fresh current native Pension 5/8 and Health 14–15/46: cessation, amended liability, excess-refund conditions, transitional payment/reporting and correction rules | https://www.arlis.am/hy/acts/224823/latest ; https://www.arlis.am/hy/acts/230432/latest | 2026-10-26 |
| Fund official listing and actual mistaken-transfer DOCX, complete one-page visual/structural reading; scope distinct from Government Treasury procedure | https://www.uhif.am/am/documents ; https://vnxctzddivqjdrwwspgw.supabase.co/storage/v1/object/public/documents/official_docs/1788347293816_1775200508371_document.docx | 2026-10-26 |

[pension]: https://www.arlis.am/hy/acts/224823
[wage]: https://www.arlis.am/hy/acts/172160
[stamp]: https://www.arlis.am/hy/acts/230046
[stamp-amend]: https://www.arlis.am/hy/acts/218648
[health]: https://www.arlis.am/hy/acts/230432
[code]: https://www.arlis.am/hy/acts/215611/latest
[pensionrefund]: https://www.arlis.am/hy/acts/179268/latest

[salarylist]: https://www.arlis.am/hy/acts/126230/latest
[capforms]: https://www.arlis.am/hy/acts/114736/latest
[cessation]: https://www.arlis.am/hy/acts/121967/latest
[healthaccounts]: https://www.uhif.am/am/requisites
[healthsettlement]: https://www.arlis.am/hy/acts/219163/latest
[healthregister]: https://www.arlis.am/hy/acts/219364/latest
[healthnotice]: https://www.arlis.am/hy/acts/219155/latest
[healthrefund]: https://vnxctzddivqjdrwwspgw.supabase.co/storage/v1/object/public/documents/official_docs/1771924519311_document.pdf
[healthrefundonline]: https://www.uhif.am/am/refund

Targeted commencement recheck, **25 October 2026**: [current Health Law arts. 16 and 45(1)(8)](https://www.arlis.am/hy/acts/230432/latest) expressly defer article 16 until 1 January 2027. Other source read dates remain as recorded.

**Not yet confirmed:** operative Government procedure/commencement forHealth 14(12) mistaken/no-liability payments and specified suspended/age 65 entrepreneur refunds. Specialist populations, agreements, related-person coverage, all state-paid priority exceptions and historic stamp-family refunds remain separate boundaries. No live participant refund, accepted return, fresh independent country review or named accountant attestation is represented as obtained. The current statutory transitional deadline and ordinary contribution/participant-excess methods are supplied. The unresolved mistake/suspension/age-65 refund implementation is a conditional recovery boundary, not a universal refund entitlement or a missing ordinary contribution computation.

> Contributed by Michael Cutajar.

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
