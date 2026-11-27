---
name: es-beckham
description: Use this Guide to assess and compute Spain’s incoming-worker special tax regime under article 93 for 2026, commonly called the Beckham regime. It covers qualifying employment, remote employment, administrators, entrepreneurs, highly qualified professionals and associated family members, the prior non-residence test, election evidence, income-source and service-period rules, annual ordinary and savings scales, foreign-tax relief, withholding, Modelo 149 and Modelo 151. Trigger phrases include Ley Beckham, régimen de impatriados, trabajadores desplazados, incoming-worker tax, digital nomad tax election, 24 percent regime and Spanish special residence taxation. Obtain the move and activity dates, residence history, actual election, service-period income, source evidence and payer certificates. A visa, foreign employer or foreign bank account alone does not settle eligibility or tax treatment.
version: 1.5
jurisdiction: ES
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Spain: incoming-worker special tax regime v1.5

Calculate the 2026 article 93 regime only after documenting eligibility and election.

## Who this applies to

[LIRPF art. 93](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) lets qualifying individuals who become Spanish tax resident because of moving to Spain elect the special IRNR computation **while remaining IRPF taxpayers**. The move must meet a statutory work, administrator, entrepreneur or highly qualified professional route, and occur in the first application year or the preceding year. The individual must not have been Spanish resident during the five tax periods before the move. The professional-athlete special employment relationship is excluded.

Qualifying employment includes a Spanish employment/statutory relationship, an employer-directed posting evidenced by its letter, or employment performed remotely using the specified IT/telecommunications means. The international telework visa supports the employment route; a visa does not dispense with the remaining tax conditions. Ordinary freelance work is not automatically qualifying remote **employment**.

An administrator can qualify, but an administrator of a patrimonial entity must not hold a participation that makes them related under LIS art. 18. For the entrepreneurial route, [RIRPF art. 113.2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a113) requires an innovative activity and/or one of special economic interest to Spain with favourable ENISA assessment: obtain the article 69 residence authorisation before moving; EU/free-movement beneficiaries instead request the favourable ENISA report before moving. An existing elector starting a different entrepreneurial activity also needs the report.

For highly qualified services to qualifying emerging companies, document the article 71 qualification; its pre-move residence authorisation establishes that qualification. For training/research/development/innovation, document an article 72.1(a)–(d) activity; its pre-move authorisation establishes that circumstance. The qualifying remuneration must together exceed **40% of all business, professional and employment income**. During the regime, economic activities are confined to the entrepreneurial, emerging-company-services and specified training/research/development/innovation routes; no Spanish PE income is allowed outside the article 93.1.b.3/4 exceptions. Ordinary freelancing or managing investments alone is insufficient ([LIRPF art. 93.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93); RIRPF art. 113.2).

Before electing, check **RIRPF article 116.3**: a taxpayer who has used the special incoming-worker employment-withholding procedure in **article 89.B cannot exercise this special-regime option**. Article 89.B concerns an employee anticipating ordinary Spanish IRPF withholding on a move to Spain; AEAT identifies that communication as **Modelo 147**. It is a different procedure from the Modelo 149 special-regime election. Retain the actual prior communication, AEAT accreditation and payer implementation evidence rather than assuming that a timely 149 overrides the bar. [RIRPF arts.89.B/116.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a116); [AEAT general incoming-worker procedure/Modelo147](https://sede.agenciatributaria.gob.es/Sede/irpf/tengo-que-presentar-declaracion/regimen-fiscal-aplicable-trabajadores-desplazados.html).

For example, an employee otherwise meets the article 93 residence-history, move and employment conditions and remains within the six-month election deadline, but has already used article 89.B's special withholding procedure. Article 116.3 bars the election on those facts. Absence of that prior procedure only clears this additional gate; every other eligibility/election condition still applies. The article89.A passive-benefit withholding procedure is a separately named procedure, so do not broaden the specific89.B bar by analogy.

The principal's spouse and children under 25 (any age if disabled), or, where there is no marriage, the other parent of those children, may elect individually under art. 93.3. Each must acquire Spanish tax residence, meet the five-period non-residence and prohibited-PE tests, and move by the end of the principal's first regime year. Earlier arrival is permitted only without acquiring Spanish tax residence before that first year ([RIRPF art. 113.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a113)). Each year, the **combined associated liquidable bases must be strictly below the principal's liquidable base**. Relationship, age and disability are tested at election ([art. 116.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a116)).

## Rates, bands and thresholds

| Item | 2026 amount/rule | Official source |
|---|---|---|
| Regime duration | First residence period plus five following periods; first year is the first calendar year with more than 183 days in Spain after moving; associated people cannot outlast principal, subject to renunciation/exclusion | [LIRPF art. 93.1/3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93), [RIRPF art. 115](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a115) |
| Pre-move non-residence | Five preceding tax periods | [LIRPF art. 93.1.a](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| Ordinary special-regime base, first 600,000 | 24% | [Art. 93.2.e.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| Same base above 600,000 | 47% on excess | [Art. 93.2.e.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| Spanish-source savings-category base 0–6,000 | 19%, opening quota 0 | [Art. 93.2.e.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| >6,000–50,000 | 21%, opening quota 1,140 | [Art. 93.2.e.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| >50,000–200,000 | 23%, opening quota 10,380 | [Art. 93.2.e.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| >200,000–300,000 | 27%, opening quota 44,880 | [Art. 93.2.e.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| >300,000 | **30%**, opening quota 71,880 | [Art. 93.2.e.2, current since 2025](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| Employment withholding | Each payer: 24%, with 47% on that payer's annual remuneration above 600,000 | [Art. 93.2.f](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93) |
| Foreign-work/qualifying foreign-entrepreneur tax credit | Art. 80 credit plus overall 30% limit on the quota attributable to all such work/entrepreneur income | [RIRPF art. 114.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a114) |

## The base

### Identify Spanish-source income correctly

Under [LIRPF art. 93.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93), **all employment income and income from a qualifying entrepreneurial activity obtained during the regime is deemed Spanish-source**. Foreign work, employer, payroll or bank account does not by itself exclude it. [RIRPF art. 114.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a114) excludes from that deeming rule income attributable to activity **before the move** or **after the notified end of the posting**, without removing any independently Spanish-source income under IRNR rules. Allocate a bonus/award by the underlying service period and keep the evidence.

For other income, apply [TRLIRNR art. 13](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a13). A genuinely foreign-source passive dividend, interest receipt, property rent or gain is not automatically brought into this special Spanish base. A foreign account can hold Spanish-source income, so its location is not the source test. Conversely, Spanish-property rent and other Spanish-source ordinary income enter the non-savings category unless the statute puts them in art. 25.1.f's savings category. Spanish-source dividends, interest and transfer gains use that separate savings-category scale.

Apply the IRNR base rules as modified by art. 93: ordinary employment is gross income, without automatically importing the annual resident employee-expense deduction or personal/family minimum. Art. 93.2.a disapplies the enumerated IRNR provisions, including general art. 14 exemptions except the specified exempt in-kind employment. Do not add ordinary IRPF exemptions/reliefs merely because the individual remains an IRPF taxpayer ([LIRPF art. 93.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93); [TRLIRNR art. 24](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a24)).

### Annual tax and credit

1. Build a source/service-period register for each income item. Classify ordinary base O and Spanish-source art. 25.1.f savings base S. The year's subject income is accumulated **without compensation between income items**; do not offset a loss against salary or a separate positive gain under an ordinary resident-loss assumption.
2. Compute `ordinary_tax = 0.24 ×min(O, 600,000) +0.47 ×max(O −600,000, 0)`.
3. Compute savings tax progressively using the table, including **30% above 300,000**. The regime has two annual categories, not a 24% tax on everything and not the old 28% top savings rate.
4. Determine permitted donation/payment-on-account deductions under [TRLIRNR art. 26](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a26) and [RIRPF art. 114.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a114). Include the specified IRNR tax already paid on account where applicable.
5. For foreign employment/qualifying entrepreneurial income, calculate the [LIRPF art. 80](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a80) credit for identical/analogous foreign income tax actually paid, limited to the effective-rate tax on the foreign-taxed base, then enforce the additional **30% of work/entrepreneur quota** cap in RIRPF art. 114.2.b. Exclude savings base and quota from the effective rate. Express it to two decimal places: `effective_percentage = round(100 × ordinary_tax / O, 2)`. In a salary-only ordinary category, credit is `min(qualifying_foreign_tax, foreign_work_income × effective_percentage / 100, 0.30 ×ordinary_tax)`. A mixed ordinary-category credit calculation is held pending individual allocation: **Check this point with one of our partner accountants.**
6. Subtract supported withholdings/payments on account to obtain the return balance. Multiple employers each below the payer withholding threshold can leave a material annual top-rate balance. Reconcile final annual tax with actual payer certificates rather than assuming the 24% deducted was final.

For economic activity, [RIRPF art. 114.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a114) subjects only professional activity income to withholding and requires the applicable rate on invoices. Its IRNR-model reporting provision specifically covers the resident entity/PE withholding under article 76.2.a; identify the actual payer obligation before selecting a form. Spanish-property transfers carry [TRLIRNR art. 25.2](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a25) purchaser retention through RIRPF art. 114.5, including its exception for contributions on formation/capital increases of Spanish-resident companies.

### Regime and other taxes

The election sets wealth-tax **real-obligation** treatment ([LIRPF art. 93.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93)); an individual wealth-tax calculation is held. **Check this point with one of our partner accountants.** Social-security coverage and case-specific treaty entitlement/certificates are also held separately from this computation. **Check this point with one of our partner accountants.**

## Deadlines and filing

| Action | Deadline/mechanism | Official source |
|---|---|---|
| Principal election, Modelo 149 | Maximum six months from documented activity start in Spanish SS registration, retained-origin SS documentation or, where no SS registration is mandatory, activity-start evidence | [RIRPF art. 116.1.a](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a116) |
| Prior incoming-worker withholding procedure | Article116.3 bars election if the taxpayer has used article89.B; inspect Modelo147/accreditation/payer evidence before treating149as available | [RIRPF art.116.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a116) |
| Associated person's individual election | Six months from entry, or principal's election deadline if later | [Art. 116.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a116) |
| Evidence and accreditation | Route-specific documents under art. 119; provide regime accreditation to withholders; disability application may precede certification but regime requires recognition | [Art. 119](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a119) |
| Annual return, Modelo 151 | Electronic; same annual window approved for general IRPF, with separate direct-debit cut-off | [Order HFP/1338/2023 arts. 3–4](https://www.boe.es/buscar/doc.php?id=BOE-A-2023-25416) |
| Voluntary renunciation | November/December before the year it takes effect; worker communication to payer and 149, no re-election | [RIRPF art. 117](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a117) |
| Exclusion | Effective in breach year; notify within one month; no re-election | [Art. 118](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a118) |
| Posting ends while still resident that year | Notify within one month, relevant to later service-period income | [Art. 119.5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a119) |

An NIE alone does not satisfy the election. For electronic Modelo 149, first join the tax census if necessary, submit supporting documents through the designated prior-document procedure and include its registration number; the principal elects before associated people ([Order HFP/1338/2023 arts. 7/8/10](https://www.boe.es/buscar/doc.php?id=BOE-A-2023-25416)). Retain the actual qualifying activity date, filed election and accreditation. A missed-election remedy is held pending the filed record: **Check this point with one of our partner accountants.** For 2026 income filed in 2027, the approved campaign window is required; no permanent 30 June date is assumed.

For associated people, loss of the combined-base condition or the principal's renunciation/exclusion excludes the associated group in the effective year; other individual eligibility failures exclude the affected member. Divorce/nullity is not itself a failure. Associated people need not repeat an exclusion notice already communicated through the principal's renunciation/exclusion. On exclusion, switch withholding to ordinary IRPF from the breach, except employment withholding switches on notice to the payer ([RIRPF art. 118](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a118)).

## Penalties and interest

Late Modelo 151, under-declaration, communication penalties, interest and collection-stage calculations are held for classification under [LGT arts. 26–28/191/198/199](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186). **Check this point with one of our partner accountants.** Do not calculate a filing surcharge or treat payment as curing a missing election from this Guide.

## Cross-border points

Keep foreign assessments and service-period/source evidence for the computation above. Complex multi-period equity allocation and departure/exit-tax calculations under [LIRPF art. 95 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a95bis) are held: **Check this point with one of our partner accountants.**

Historical visa assertions about a **20% Spanish-client income limit** are not tax-eligibility rules supplied by this Guide. Immigration eligibility is held separately: **Check this point with one of our partner accountants.** Apply the employment/qualifying-activity tax tests above.

## Two worked examples that recompute

### 1. Employment abroad remains included, foreign passive dividend does not automatically enter

A hypothetical valid elector has **110,000 gross employment income for services performed during the 2026 regime**, including 20,000 for work physically abroad. No qualifying foreign tax was paid. A Spanish-source dividend is 4,000; a separate 5,000 dividend is established to be genuinely foreign-source under art. 13. Include the whole 110,000 employment, ordinary tax **26,400**, plus Spanish-dividend tax **760**, total **27,160** before supported payments on account. The foreign dividend is outside this special Spanish source base; the foreign-work salary is included. No ordinary employee-expense or personal-minimum deduction is assumed ([LIRPF art. 93](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93); [RIRPF art. 114](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a114)).

```oa-check
name: Spain 2026 impatriate employment-source deeming and passive source
inputs:
  spanish_work_salary: 90000
  foreign_work_salary: 20000
  spanish_dividend: 4000
  foreign_source_dividend: 5000
steps:
  employment_base: spanish_work_salary + foreign_work_salary
  ordinary_tax: min(employment_base, 600000) * 0.24 + max(employment_base - 600000, 0) * 0.47
  savings_tax: spanish_dividend * 0.19
  excluded_foreign_passive: foreign_source_dividend
  total_gross_tax: ordinary_tax + savings_tax
expected:
  employment_base: 110000
  ordinary_tax: 26400
  savings_tax: 760
  excluded_foreign_passive: 5000
  total_gross_tax: 27160
```

### 2. Two employers, top savings band and foreign-credit cap

A hypothetical valid full-year elector receives **650,000 employment**, half from each of two payers, all for services during the regime. Of it, 300,000 relates to work abroad with 80,000 qualifying foreign tax. Spanish-source dividends are 310,000, with no loss or donation deduction. Ordinary tax is **167,500**; savings tax **74,880**. The salary-only effective percentage is **25.77%**, expressed to two decimal places under LIRPF art. 80.2, giving a foreign-income limit of **77,310**, but the extra 30%-of-employment-quota limit restricts credit to **50,250**. Tax after credit is **192,130**. Each salary payer paid only 325,000 and withheld 24%, total 156,000; dividend withholding at the IRNR 19% rate is 58,900. With supported credits of 214,900, the return balance is **−22,770**, a refund. The result tests annual aggregation, payer-specific withholding and the additional credit cap ([LIRPF art. 93.2.e/f](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93); [RIRPF art. 114.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a114); [TRLIRNR art. 25.1.f](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a25)).

```oa-check
name: Spain 2026 impatriate annual bands and foreign-credit ceiling
inputs:
  salary: 650000
  foreign_work_salary: 300000
  foreign_tax: 80000
  spanish_dividend: 310000
steps:
  employment_tax: min(salary, 600000) * 0.24 + max(salary - 600000, 0) * 0.47
  savings_tax: 71880 + (spanish_dividend - 300000) * 0.30
  foreign_effective_percentage: round(100 * employment_tax / salary, 2)
  foreign_income_limit: foreign_work_salary * foreign_effective_percentage / 100
  special_credit_limit: employment_tax * 0.30
  foreign_credit: min(foreign_tax, min(foreign_income_limit, special_credit_limit))
  tax_after_credit: employment_tax + savings_tax - foreign_credit
  salary_withholding: salary * 0.24
  dividend_withholding: spanish_dividend * 0.19
  return_balance: tax_after_credit - salary_withholding - dividend_withholding
expected:
  employment_tax: 167500
  savings_tax: 74880
  foreign_effective_percentage: 25.77
  foreign_income_limit: 77310
  special_credit_limit: 50250
  foreign_credit: 50250
  tax_after_credit: 192130
  salary_withholding: 156000
  dividend_withholding: 58900
  return_balance: -22770
```

## Ask the client first

1. What move, residence, qualifying work/activity and documented social-security/origin-coverage dates establish eligibility and the election deadline?
2. What residence history, prior article89.B/Modelo147 procedure and actual149election/accreditation support each principal/associated person?
3. Which income relates to pre-move, regime-period or post-notified-posting services, and what establishes each other item's Spanish/foreign source?
4. What entrepreneur/emerging-company/qualification/administrator ownership and PE evidence satisfies the selected route?
5. What foreign tax, service allocation and payer withholding certificates support the credit and annual balance?
6. What associated-person bases and events require continued eligibility, notification, renunciation or exclusion?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [LIRPF, Ley 35/2006, arts. 80/93/95 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Arts. 80/93 read: eligibility, source deeming, 2026 scales, payer threshold, family and credit; art. 95 bis departure calculation held | 2026-11-27 |
| [RIRPF, RD 439/2007, arts. 89/113–120](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 89/113–119 read: prior withholding procedure, route evidence/timing, activity restriction, base, credit ceiling, election, family, duration, notification and exclusion; treaty case held | 2026-11-27 |
| [TRLIRNR, RDL 5/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527) | Arts. 13/24–26/31 read: sources, gross base, savings classification, property retention, payments and dividend withholding | 2026-11-27 |
| [Orden HFP/1338/2023](https://www.boe.es/buscar/doc.php?id=BOE-A-2023-25416) | Arts. 3/4/7/8/10 read: electronic 149/151, election sequence/documents, annual campaign/direct-debit windows | 2026-11-27 |
| [AEAT general incoming-worker procedure](https://sede.agenciatributaria.gob.es/Sede/irpf/tengo-que-presentar-declaracion/regimen-fiscal-aplicable-trabajadores-desplazados.html) | General-regime paragraph read: Modelo 147 distinguished from 149; specific bar read in RIRPF art. 116.3 | 2026-11-27 |

**Not yet confirmed:** complex equity/mixed-credit allocations; individual treaty, social-security, wealth, immigration, departure/exit-tax, late-filing/penalty and missed-election outcomes. These are explicit non-usable holds with partner-accountant referral above; no conclusion on them is supplied. Other activity/PE or family boundary facts that do not establish the stated conditions are held too: **Check this point with one of our partner accountants.**
