---
name: uzbekistan-income-tax
description: Use this skill whenever asked about Uzbekistan personal income tax (PIT) for individuals, self-employed persons, and individual entrepreneurs. Trigger on phrases like "how much income tax in Uzbekistan", "Uzbekistan PIT", "soliq", "12% flat tax", "INPS pension", "social tax", "individual entrepreneur turnover tax", "non-resident tax Uzbekistan", "annual income declaration", "dividends tax Uzbekistan", "payroll Uzbekistan", "minimum wage UZS", "BHM/BRV base amount", or any question about computing or filing personal income tax for a resident or non-resident individual, an employee, a sole trader, or an individual entrepreneur in Uzbekistan. Also trigger when classifying UZS bank-statement lines for income tax, modelling take-home pay, or computing employer social tax. This skill covers the flat 12% PIT, the 5% dividend/interest rate, non-resident rates, the INPS 0.1% accumulative pension carve-out, employer social tax (12%/25%/7%/4.7%/1%), the calendar-year filing cycle, and the 2026 self-employed turnover-tax changes. ALWAYS read this skill before touching any Uzbekistan income tax work.
version: 0.2
jurisdiction: UZ
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Uzbekistan personal income tax

## Scope

Compute an individual's Uzbekistan PIT, reconcile withholding and take-home pay, and distinguish an individual entrepreneur (IE) from a self-employed person. Use UZS and the calendar tax year. This is the individual computation job; use the payroll and social-contributions Guides for employer administration, the corporate Guide for company profit, and the VAT Guide for supplies and entity turnover-tax returns. [Tax Code, arts. 364–368, 384](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

Law read on 14 November 2026 includes the Code's selected 21 October 2026 edition and separately operative Presidential measures. In particular, PF-100 changes the turnover ceiling from June; the older Code wording alone is insufficient. Bank classifications are evidence leads, never a substitute for the underlying contract or tax certificate. The original historical cases remain below with corrected boundaries.

## Ask the client first

- Obtain the tax year, identity/tax registration, citizenship, entry/exit calendar, home/family and treaty residence evidence, departure date, and any approved special foreign-citizen status.
- Obtain each employer's gross-pay, benefits, withholding and INPS certificates, primary/secondary workplace status and previous-employer certificate. Establish whether a bank credit is gross pay or already net.
- Obtain all domestic/foreign salary, royalties, rent, asset-sale, freelance, platform, dividend and interest records, source country, original currency/date, foreign tax proof, and the payer's legal form for dividends.
- For business receipts, obtain IE/self-employed registration, activity and location, actual annual/cumulative turnover, regime election/transition dates, turnover returns and social-tax payments. Obtain the actual current BCV/minimum-wage effective dates.
- Obtain benefit eligibility evidence, designated-area work evidence, withheld/paid tax receipts, INPS statements, foreign declarations and prior-year/carrying reconciliation. Reconcile bank accounts, e-wallets, cash, loans and own-account transfers to the income summary.

## The method, step by step

### Determine residence and source before applying a rate

The ordinary primary residence test is **more than 183 calendar days** in any consecutive **12-month** period beginning or ending in the tax year. A separate rule covers presence **less than 183 days** where Uzbekistan presence exceeds presence in any other state. Exactly 183 days is not automatically covered by either literal test: refer for the remaining statutory/treaty analysis. Early recognition can follow an application supported by a long-term employment contract or other evidence. Short treatment/study absences of **less than 6 months** do not interrupt the counted period; diplomatic/consular, international-organization and specified family exceptions, and government/military service abroad, require the neighboring rules. Border records and other evidence determine the facts; dual residence requires the applicable treaty and centre-of-vital-interests analysis. [Code, art. 30](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

Residents generally bring worldwide income into the computation; nonresidents bring Uzbekistan-source income. Separate differently taxed bases. Convert foreign-currency income at the Central Bank rate on the statutory actual-receipt date; a platform payout or foreign payer alone does not settle the source, business regime or gross income. Ordinary personal bank charges and loan principal are not general income deductions. Specific reliefs and the documented expense rules for the statutory declaration categories require their own eligibility test. [Code, arts. 366–368, 378–380, 394–395](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

| Income/condition | PIT treatment | Official source |
| --- | --- | --- |
| Ordinary resident taxable employment, rent, royalties, taxable gains and other general income | 12%; no progressive bands or universal personal tax-free allowance; statutory exemptions/deductions remain possible | [Code, arts. 378–381](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Resident taxable dividends and interest | 5%, subject to the exemptions below | [Code, art. 381](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Nonresident Uzbekistan-source employment/civil-contract and other taxable income | 12%; classify the actual income before using the residual category | [Code, art. 382](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Nonresident taxable dividends and interest | 10%, subject to treaty/express exemption | [Code, art. 382](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Nonresident international transportation/freight income | 6%; ordinary domestic freight is not automatically in this category | [Code, art. 382](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Dividends on qualifying joint-stock-company shares, resident or nonresident individual | Exempt from 1 April 2022 through 31 December 2028; an LLC dividend does not acquire this exemption | [Code, art. 483](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Qualifying bank-deposit interest, savings-certificate and government-security income | Apply the specific exemption rather than automatically charging the general interest rate | [Code, art. 378(13)](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Qualifying school, college or technical-school student, age not older than 30, employed while learning a profession | Temporary 1% PIT on qualifying income from the business entity during that vocational learning, from 1 September 2024 until before 1 September 2027; verify student/employment evidence | [Code, art. 483](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Employment performed in the specifically listed Sokh district, Chungara mahalla of Rishtan district, Shahimardan/Yordan villages and Tashtepa-2 street of Khosilot mahalla in Fergana district | 1% only on the qualifying employment income; residence or a bank narration alone is insufficient | [Code, arts. 480¹–480²](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |

Do not invent a deduction of one BCV. Category-specific monthly relief under article 380 is generally **1.41 times the minimum wage**, while the specified disability category uses **3 times** that minimum; document the exact category and eligibility period. Grants/subsidies are not automatically excluded because called “capital”: article 378(14) has grantor/purpose and authorized-opinion conditions. Capital gains, residential-property holding-period exceptions, rent relief and other exemptions require their actual statutory facts. [Code, arts. 378–380](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

### Reconcile gross income, tax and its allocations

Compute eligible employment withholding cumulatively from the start of the year, deducting tax already withheld. Bring the previous employer's certificate into the new primary workplace computation. Secondary-workplace treatment excludes the specified material-assistance and article 380 benefits; it is not a reason to deny every article 378 exemption. Annual-declaration obligations depend on the actual untaxed/foreign and other statutory income categories. [Code, arts. 388, 393](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

| Allocation | Treatment | Official source |
| --- | --- | --- |
| Mandatory INPS for an eligible employee | 0.1% of taxable income, redirected from PIT; do not add it to the employee's PIT burden | [PQ-4086, para. 5](https://lex.uz/docs/-4131684); [Code, art. 385](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| State Social Insurance Fund from 1 January 2026 | 0.2 percentage points of PIT, with the decree's annual rental-declaration and source-withheld dividend/interest exceptions; this is an allocation within PIT | [PQ-388, para. 5](https://lex.uz/docs/-7959569) |
| Ordinary eligible 2026 salary at 12%, including both allocations above | Remaining budget share 11.7% (derived: 12% − 0.1% − 0.2%); net pay still gross less total PIT | [PQ-4086, para. 5](https://lex.uz/docs/-4131684); [PQ-388, para. 5](https://lex.uz/docs/-7959569) |

Employer social tax is an employer cost, not an employee deduction. Rates below are eligibility references for the employer-cost column, not permission to select a relief from salary alone.

| Employer/wages | Social tax | Official source |
| --- | --- | --- |
| Ordinary taxpayer; budget organization; named “SOS Children's Villages of Uzbekistan” association | 12%; 25%; 7%, respectively | [Code, art. 405](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Labor of persons with disabilities in specialized workshops, sections and enterprises | 4.7%; not every employer with a disabled employee | [Code, art. 405](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Qualifying member of a poor/low-income family paid at least 1.5 times the minimum wage | 1% on that employee's wages from 1 January 2025 until before 1 January 2028; family status and inclusive salary test both matter | [Code, art. 483](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |

Other temporary/student/location social-tax reliefs require the social-contributions Guide. Do not impose a general contribution ceiling without authority. [Code, arts. 404–405, 480¹–483](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

### Separate IE/self-employed turnover tax and social tax

From **1 January 2026**, IE and self-employed turnover taxpayers use **1%** on the turnover-tax base; PQ-247 expressly abolishes the ordinary fixed-amount IE PIT system and the self-employed turnover-tax exemption for sales income not exceeding **UZS 100,000,000**. [PQ-247, para. 5(a)(i–ii)](https://lex.uz/docs/-7681520). Their qualifying turnover-tax business receipts are excluded from the PIT object, rather than taxed a second time as ordinary freelance income. The default company turnover rate is **4%**, with activity/location exceptions; it is not the IE rate. [Code, arts. 365, 385, 461, 467](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

The older **UZS 1,000,000,000** ceiling is relevant to the pre-June regime. From **1 June 2026**, PF-100 sets the transition ceiling at **12,000 times BCV** and removes mandatory VAT status merely because of goods imports. Derived ceiling values are **UZS 4,944,000,000** while BCV is **412,000**, and **UZS 5,280,000,000** from the **1 September 2026** BCV of **440,000**. Test actual dates, remaining statutory activity exclusions, transition notices and existing general-regime status; an existing VAT payer cannot simply return to turnover tax midyear because the ceiling rose. The Tax Committee confirms the following-year route with notice at least **10 days** before that next tax period. [PF-100, paras. 2, 9, 13](https://lex.uz/docs/-8236831); [PF-91, para. 3](https://lex.uz/docs/-7553322); [PF-115, para. 3](https://lex.uz/docs/-8283656); [Tax Committee, 23 June 2026, question I](https://gov.uz/oz/soliq/news/view/183078).

| Base amount and effective period | UZS | Official source |
| --- | --- | --- |
| BCV/BHM/BRV, 1 January–31 August 2026; from 1 September 2026 | 412,000; 440,000 | [PF-91, para. 3](https://lex.uz/docs/-7553322); [PF-115, para. 3(b)](https://lex.uz/docs/-8283656) |
| Minimum wage, 1 January–31 August 2026; from 1 September 2026 | 1,271,000; 1,360,000 | [PF-91, para. 3](https://lex.uz/docs/-7553322); [PF-115, para. 3(b)](https://lex.uz/docs/-8283656) |
| Pension calculation base, until 30 June 2026; from 1 July 2026 | 471,000; 504,000; distinct from BCV and minimum wage | [PF-91, para. 3](https://lex.uz/docs/-7553322); [PF-115, para. 3(a)](https://lex.uz/docs/-8283656) |

An ordinary IE owes at least **1 BCV per active month**, regardless of working days, subject to specific pension/disability, Hunarmand, location, registration and suspension rules. New-registration liability begins in the following month; effective suspension requires the tax authority's statutory information. Self-employed persons instead have a **voluntary annual** social-tax payment of at least **1 BCV** for pension service credit, due by **31 December**, valued at the payment-date BCV. Do not charge them the IE monthly minimum. The ordinary monthly IE payment is due by the **15th of the active month**. [Code, art. 408](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

### Classify bank records and build the workpaper

The following preserved bank-language patterns are search hints. Confirm payer, contract, gross/net, source, regime and withholding; do not automatically charge every bank credit or deduct every debit.

| Pattern | Evidence-led classification |
| --- | --- |
| ISH HAQI, OYLIK, ZARPLATA, SALARY, named employer | Employment; obtain gross-pay and withholding certificate |
| GONORAR, HONORARIUM, KONSULTATSIYA, CONSULTANCY, FEES | Royalty/service/business income; establish legal category and regime |
| DIVIDEND, DIVIDENDLAR | Establish JSC/LLC legal form, residence and source |
| FOIZ, PROTSENT, INTEREST | Test deposit/security exemption before taxable interest |
| IJARA, ARENDA, RENT RECEIVED | Rent; establish property, contract, statutory relief and withholding |
| FRAHT, FREIGHT, TRANSPORT | Verify international transport and nonresident/source facts |
| UPWORK, FIVERR, STRIPE, PAYPAL, WISE PAYOUT | Reconcile gross platform earnings, fees and payout; platform name does not set PIT |
| SOLIQ QAYTARISH, TAX REFUND | Reconcile refunded tax to liability/receivable; not new service revenue |
| GRANT, SUBSIDIYA | Establish grantor, purpose and statutory exemption evidence |
| PIT, JISMONIY SHAXS SOLIG'I, NDFL | Tax paid/withheld to reconcile as credit, not expense |
| INPS, JAMG'ARMA PENSIYA, PENSION ACCOUNT | PIT allocation; reconcile without double counting |
| IJTIMOIY SOLIQ, SOCIAL TAX, ST | Employer/IE liability according to actual status |
| OBOROT SOLIG'I, TURNOVER TAX; IE SOCIAL TAX, IP IJTIMOIY SOLIQ | Business-regime tax/social payment; not ordinary personal deduction |
| PATENT | Historical regime/payment evidence; do not continue an abolished fixed system |
| O'Z HISOBIM, OWN ACCOUNT, INTERNAL TRANSFER | Exclude only a matched own-account transfer |
| KREDIT, QARZ, LOAN REPAYMENT | Exclude established principal; separate interest or disguised income |
| BANK KOMISSIYASI, BANK FEE (personal) | Personal charge; no general PIT deduction |

Preserved statement-reading specimens, **not verified current bank export specifications**: NBU PDF/CSV, Latin/Cyrillic, `Sana / Tavsif / Debet / Kredit / Qoldiq`, patterns `O'TKAZMA / ISH HAQI / KOMISSIYA`; Kapitalbank Russian/Uzbek, `Дата / Описание / Сумма`, `PEREVOD / ZARPLATA / OPLATA`; Hamkorbank Latin PDF, `O'TKAZMA / IJARA / DIVIDEND`; Ipoteka Bank / Ipak Yo'li mixed PDF/CSV, `PEREVOD / NALOG / PENSIYA`; Payme / Click e-wallet CSV, `Date / Type / Amount / Reference`, `TO'LOV / PAYMENT`. Read the supplied headers and balance/sign convention. General terms: `daromad` income, `soliq` tax, `pensiya` pension, `o'tkazma / perevod` transfer, `komissiya` commission, `to'lov / oplata` payment. Unmatched transfers stay unresolved.

Workpaper tabs/sections: **A** gross income by employment, rent, taxable gains, royalties, dividends, interest, foreign income, IE/platform income and other income, retaining exempt/outside-object items separately; **B** residence/source/category/rate and relief evidence; **C** INPS and other PIT allocations; **D** employer social tax, never deducted from net employee pay; **E** IE/self-employed turnover base, regime and monthly/annual social liability; **F** liability, withheld/paid/foreign credits, refunds, net payable and take-home reconciliation. Attach each bank line, certificate and rule to its row. Review flags include unknown residence, JSC evidence, foreign-source credit, designated-area proof, INPS double counting, gross/net uncertainty, business-regime dates and special foreign-citizen approval.

## Boundary and exception table

| Boundary | Action |
| --- | --- |
| Residence, source or gross/net amount unproved | Hold the affected computation; do not default unknown residence to nonresident or every credit to general PIT |
| JSC exemption not established | Present the conditional taxable alternative and obtain legal-form/share evidence; do not assert either final result |
| Foreign-source resident income | Include subject to actual relief; foreign credit follows arts. 399/342, taxable-income and treaty conditions, payment proof/translation and Uzbekistan tax cap; no automatic unlimited credit |
| Special foreign-citizen regime | PF-180 introduces foreign-source PIT exemption from 1 January 2026 for approved qualifying foreign citizens, with USD 50,000 fee (source: “50 ming”, in words on the page), specified authorized bank account/crypto wallet and special residence of more than 30 days in a consecutive 12-month period beginning/ending the tax year plus owned/rented Uzbekistan housing; USD 10,000 (source: “10 ming”, in words on the page) for each adult close relative. Commission/application and implementing conditions apply. Do not claim relief just from nationality, salary, fee intention or a bank receipt. [PF-180, paras. 1–7](https://lex.uz/docs/-7755309) |
| Designated-area or temporary relief | Use its exact employment/location/category/period conditions; missing evidence triggers R3 |
| IE/self-employed vs company or VAT | Separate taxpayer and tax object; threshold changes do not erase import/tax-agent obligations or other exclusions |
| Refund, over-withholding, residence change | Reconcile documents and use the statutory adjustment/refund procedure; do not deduct a tax refund from income blindly. [Code, art. 391](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |

### Not yet confirmed - unusable legacy assertions

Article 397 language conflict: the original's before-1-February exit exception cannot be treated as an automatic exemption for a departing resident. The Uzbek original says a nonresident foreign individual in that sentence; the Russian parallel says resident. The resident departure-filing obligation in the preceding sentence and its 15-day payment rule remain relevant. Obtain a dated practitioner resolution before omitting a return on this basis. [Code, art. 397, Uzbek original](https://lex.uz/docs/4674902?ONDATE=21.10.2026); [Russian parallel](https://lex.uz/ru/docs/4674893?ONDATE=21.10.2026).

The original's automatic general PIT treatment of all unknown credits, residence default, blanket grant exclusion and blanket secondary-job benefit denial are rejected by the conditions above. The old “no formal individual audits” statement is unusable: tax-control powers and limitation exceptions remain. Its generic **3-year** limitation summary is only the starting rule under article 88, not immunity from an assessment. [Code, arts. 88, 136–140](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

Legacy base values **BCV 375,000**, **minimum wage 1,155,000**, **pension base 428,000**, and the original attribution of all subsequent bases to **1 August 2025** are retained as historical source-record claims only, not current payroll inputs. The confirmed successor dates/amounts are in the method above. Likewise, the original claim that remote registration universally starts **1 November 2025** with biometric plus SMS verification is not certified here: obtain the applicable platform/registration implementation and evidence before using that procedure. The special foreign-citizen regime's actual applicant approval, authorized provider and current implementing requirements must be established before any exemption is posted; the former unknown minimum-salary claim supplies no eligibility test.

## Worked cases

All figures below are UZS unless USD is expressly stated. Historical bank lines preserve the original date, sign, counterparty placeholder and amount; a credit line alone cannot prove gross taxable income. Cases assume the stated gross amount is independently verified. These are the original fixtures, not current bank statements. [Original case record](https://github.com/openaccountants/openaccountants/blob/264a22625593d55de372f43cfb8f697f8c4a2589/skills/uzbekistan/uzbekistan-income-tax.md).

### Resident monthly salary and historical allocation

`31/03/2025 ; NBU ; ISH HAQI MART ; [employer] ; +5,000,000.00 ; UZS`

The historical ordinary resident salary fixture has gross **5,000,000**, PIT **600,000**, INPS **5,000**, remaining budget **595,000**, net **4,400,000**, and separate standard employer social tax **600,000**. Those historical amounts are preserved. For an otherwise identical ordinary eligible **2026** salary, PIT/net/employer social remain unchanged but the insurance allocation is **10,000** and remaining budget **585,000**, derived under the allocation rules above; do not carry the historical budget split into 2026.

```oa-check
name: Ordinary 2026 salary allocations versus net pay
inputs:
  gross: 5000000
steps:
  pit: gross * 0.12
  inps: gross * 0.001
  insurance: gross * 0.002
  budget: pit - inps - insurance
  net: gross - pit
  employer_social: gross * 0.12
expected:
  pit: 600000
  inps: 5000
  insurance: 10000
  budget: 585000
  net: 4400000
  employer_social: 600000
```

### Cumulative withholding

Original same-employee salary: **5,000,000** in each of January, February and March. Jan–March income **15,000,000**, total PIT **1,800,000**; Jan–February income **10,000,000**, PIT **1,200,000**; March withholding **600,000**. Assume ordinary taxable pay, unchanged residence/benefits and accurate prior withholding.

```oa-check
name: March cumulative withholding
inputs:
  monthly: 5000000
steps:
  cumulative: monthly * 3 * 0.12
  previously_withheld: monthly * 2 * 0.12
  march: cumulative - previously_withheld
expected:
  cumulative: 1800000
  previously_withheld: 1200000
  march: 600000
```

### Resident LLC dividend versus JSC exemption

`15/05/2025 ; Kapitalbank ; DIVIDEND ; OOO [company] ; +10,000,000.00 ; UZS`

For a verified **gross 10,000,000** resident LLC dividend, PIT is **500,000**, net **9,500,000**. If documentation instead proves qualifying JSC-share dividends within the exemption period, PIT is **0**, net **10,000,000**. The decisive fact is the legal instrument/payer form, not `DIVIDEND` narration.

```oa-check
name: Dividend legal-form decision
inputs:
  dividend: 10000000
steps:
  llc_pit: dividend * 0.05
  llc_net: dividend - llc_pit
  qualifying_jsc_pit: 0
  qualifying_jsc_net: dividend - qualifying_jsc_pit
expected:
  llc_pit: 500000
  llc_net: 9500000
  qualifying_jsc_pit: 0
  qualifying_jsc_net: 10000000
```

### Nonresident freight

`20/06/2025 ; Hamkorbank ; FREIGHT SERVICES ; [non-resident carrier] ; +50,000,000.00 ; UZS`

The original **50,000,000** freight amount gives **3,000,000** PIT only when the nonresident individual, Uzbekistan-source **international** transport category is established, absent overriding treaty relief. The narration alone does not establish that classification; otherwise hold and analyze the applicable rate.

### Original IE fixture, corrected full-year bases

Original input: an IE with **800,000,000** annual turnover in **2026**, described as within the old **1 billion** ceiling. Original recorded arithmetic: turnover tax **8,000,000**, social tax **412,000 × 12 = 4,944,000**, total **12,944,000**, and a rejected old sub-**100,000,000** exemption. Preserve these as the source record; the year-round **412,000** social base is unusable for the actual full year.

Assume an ordinary IE active throughout all months, no pension/disability/location/Hunarmand relief, no suspension and no registration-month exception, eligible for turnover tax throughout. Correct minimum social tax is **8 × 412,000 + 4 × 440,000 = 5,056,000**; turnover tax remains **8,000,000**; combined **13,056,000** (derived). A self-employed person's annual voluntary social payment cannot be substituted with this IE monthly computation.

```oa-check
name: Full-year ordinary IE with September base change
inputs:
  turnover: 800000000
steps:
  turnover_tax: turnover * 0.01
  social: 8 * 412000 + 4 * 440000
  combined: turnover_tax + social
expected:
  turnover_tax: 8000000
  social: 5056000
  combined: 13056000
```

### Annual salary reconciliation

Original resident annual gross salary **60,000,000**: PIT **7,200,000**, INPS **60,000**, net **52,800,000**, separate standard employer social **7,200,000**. The historical budget split would be **7,140,000**, derived from PIT less INPS; that split was not separately printed in the original test. For otherwise identical ordinary eligible **2026** pay, insurance allocation is **120,000**, remaining budget **7,020,000**, derived; total employee PIT stays **7,200,000**.

### Distinct original test: nonresident LLC dividend

A nonresident individual's **10,000,000** gross LLC dividend gives **1,000,000** PIT and **9,000,000** net absent treaty relief. A qualifying JSC-share dividend in the statutory exemption period is exempt instead. This is distinct from the resident dividend case.

```oa-check
name: Nonresident LLC dividend
inputs:
  gross: 10000000
steps:
  pit: gross * 0.10
  net: gross - pit
expected:
  pit: 1000000
  net: 9000000
```

## When to refuse or refer

**R1:** stop a final PIT calculation if residence, income nature/source or gross/net basis is unresolved; obtain documents rather than guessing. **R2:** refer company corporate income to the corporate Guide. **R3:** hold designated-area/special-rate application pending the exact work/location/category evidence. **R4:** refer the foreign-citizen special regime for current implementation, Commission approval and provider eligibility; never equate it with ordinary foreign employment. **R5:** refer penalties, late filings, limitation disputes and audits for a dated liability analysis. **R6:** route VAT/entity turnover returns to their own Guide while retaining the individual regime reconciliation here.

Prohibitions retained: do not invent progressive bands, deduct INPS twice, deduct employer social tax from employee pay, apply JSC relief without evidence, silently exempt foreign-source income, continue abolished IE fixed taxation, assume the personal and company regimes match, or file without qualified professional review. The original bank-format examples, remote-registration mechanics and unsupported historical values cannot establish current legal treatment.

## Filing and payment

For tax filing, payment and notice deadlines expressed in days, count working days unless the provision expressly says calendar days; apply the next-working-day rule when the final date is nonworking. [Code, art. 5](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

| Obligation | Deadline/procedure | Official source |
| --- | --- | --- |
| Ordinary agent PIT report | Monthly by the following month's 15th; annual report by 15 February following the year | [Code, art. 389](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Agent withholding payment | With income payment, no later than the report deadline; in-kind income has the statutory following-month 5-day rule | [Code, art. 390](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Foreign individual resident, or becoming resident by current-year 1 April | Annual aggregate-income declaration is mandatory independently of the ordinary source-withholding exceptions; do not omit a return merely because salary was fully withheld | [Code, arts. 393, 397](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Individual annual declaration and balance | Declaration by 1 April, payment by 1 June of the following year; 2026 income therefore normally falls in the 2027 filing cycle | [Code, arts. 397–398](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Foreign resident ceases the relevant income-generating activity during the year and leaves Uzbekistan | Declaration at least 1 month before departure; exit-declaration tax within 15 days after submission. Do not automatically apply the legacy before-1-February exception: the Uzbek original says nonresident in that sentence while the Russian parallel says resident; refer that conflict for the actual departure facts | [Code, art. 397](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Untaxed rent | Preliminary declaration within 5 days after the first rental month, except the registered-contract route; monthly payment by following month's 15th | [Code, arts. 397–398](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| Other statutory preliminary declarations | Applicable categories by 1 February; newly registered category by registration-month end; confirm the exact category before applying | [Code, art. 397](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |
| IE/self-employed turnover report/payment | Monthly by following month's 15th, annual by 15 February; reconcile any statutory platform tax-agent reporting to avoid duplicates | [Code, art. 470](https://lex.uz/docs/4674902?ONDATE=21.10.2026) |

Prepare the annual aggregate-income declaration and relevant agent calculation from the workpaper. The taxpayer cabinet is [my.soliq.uz](https://my.soliq.uz); its authenticated current screens/form field identifiers were not inspected, so do not invent boxes. Match the currently displayed period/form, identity, domestic/foreign income, exemptions, withholding, foreign credit and net liability; have a qualified Uzbekistan practitioner resolve screen differences, submit only after review, and retain signed return, acknowledgement and matching payment receipt. Corrections and over-withholding use articles 391/396, not an unexplained workpaper overwrite.

Late-payment interest is computed by calendar day using **1/300 of the then-current Central Bank refinancing rate**, subject to article 110's exceptions. It is not a fixed daily percentage. Late reporting, hidden bases and incorrect underpayment have distinct consequences; no generic historical penalty shortcut is authorized here. [Code, arts. 110, 220, 223–224](https://lex.uz/docs/4674902?ONDATE=21.10.2026).

## Completion checklist

- Residence/source, taxpayer identity and business regime are evidenced; missing facts remain explicitly unresolved.
- Every income line reconciles gross/net, exempt/outside-object treatment, rate, supporting document and withholding credit.
- INPS and social-insurance allocations reconcile inside PIT; employer social tax stays separate; IE monthly and self-employed annual rules are distinguished.
- Current base dates, threshold changes, JSC/student/location relief and special approvals were checked for the actual period.
- Annual/agent/turnover forms, correction needs and deadlines reconcile to the workpaper; submission acknowledgement and payment evidence are retained after professional review.

## Sources

Official sources opened/read on **14 November 2026**: [Tax Code, selected 21 October 2026 edition](https://lex.uz/docs/4674902?ONDATE=21.10.2026), especially arts. 5, 30, 88, 110, 364–399, 404–408, 461–470, 480¹–483; [Russian parallel text](https://lex.uz/ru/docs/4674893?ONDATE=21.10.2026) used alongside the Uzbek original; [PQ-4086, para. 5, INPS](https://lex.uz/docs/-4131684); [PQ-388, para. 5, 2026 insurance allocation](https://lex.uz/docs/-7959569); [PF-91, base amounts](https://lex.uz/docs/-7553322); [PF-115, 2026 base changes](https://lex.uz/docs/-8283656); [PF-100, current turnover/VAT regime](https://lex.uz/docs/-8236831); [Tax Committee June FAQ](https://gov.uz/oz/soliq/news/view/183078); [PF-180, approved foreign-citizen regime](https://lex.uz/docs/-7755309). Earlier PwC, EY, LegalAct, WageIndicator and Goldenpages references supplied research leads only; the operative rules above rely on opened primary sources. The live authenticated 2027 declaration form has not been certified.


| Additional primary source | Operative provision | Read date |
| --- | --- | --- |
| [PQ-247, 12 August 2025](https://lex.uz/docs/-7681520) | Paragraph 5(a)(i–ii) expressly repeals fixed-amount IE PIT and the self-employed exemption for sales income not exceeding UZS 100,000,000 from 1 January 2026; paragraphs 5(b)–(g) and 8 supply neighboring turnover/digital-regime conditions | 2026-11-14 |

Not yet confirmed: authenticated current declaration fields; actual special-regime approval/provider implementation and remote-registration mechanics; legacy base claims and bank specifications held above are unusable pending evidence.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
