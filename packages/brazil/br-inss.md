---
name: br-inss
description: >
  Brazil INSS individual-contributor social security for 2026. Distinguishes own-account normal20%
  contributions, eligible simplified11%, ordinary company withholding and MEI/facultative referrals.
  Covers the current floor/ceiling, same-month concurrent employment and multiple payers, monthly GPS
  and DAS identities/timing, reduced-plan benefit limits and complements, ordinary late charges and
  historic indemnity boundaries. Trigger on INSSautonomo, contribuinteindividual, GPS1007/1163/1295,
  tetoINSS, simplified plan, PJretencao11%, CLTplusautonomo and no-income months. Includes a plan-cost
  decision and company-withholding ceiling reconciliation, plus preserved edge cases and tests. Excludes
  employee payroll computation, complete benefit eligibility, treaty certificates, specialist payer/MEI
  exceptions, refunds and historic-period recognition not verified here.
version: 2.1
jurisdiction: BR
category: international
tax_year: 2026
last_updated: 2026-11-11
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: decision
domain: payroll
---

# Brazil INSS for individual contributors: classification, plans and payment, 2026 v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** First distinguish own-account work from services to a company, an eligible simplified contributor, an actual MEI and a facultative contributor. Their collection mechanisms are different. For 2026 the monthly contribution floor is BRL 1,621 and ceiling BRL 8,475.55. Own-account normal contributions are 20%; the eligible simplified plan is 11% of the minimum. Ordinary company withholding of 11% is not that simplified plan and does not automatically require an extra 9% GPS payment.

This Guide owns individual-contributor social-security classification and ordinary calculation/payment. Employee progressive contributions and employer payroll belong to [brazil-payroll](brazil-payroll.md); IRPF deductions/annual settlement belong to [br-income-tax](br-income-tax.md), with monthly personal-income payment in [br-estimated-tax](br-estimated-tax.md). MEI business eligibility, turnover and exclusion belong to [br-simples-nacional](br-simples-nacional.md). Amounts below are BRL, not a conversion into another currency. A consumption-tax reform is not authority to replace an INSS contribution with CBS or IBS; use the relevant consumption-tax Guide separately.

## Who this applies to

An individual contributor (contribuinte individual) working on their own account without a company/equivalent relationship normally pays their own contribution. The simplified option is confined to its statutory category; it is not an election every person with a PJ payer can make. Receita’s current SC Cosit 130/2019 also rejects code 1163/11% for an own-account individual concurrently employed in another activity: the normal compulsory category applies within the overall monthly ceiling. Do not offer the simplified plan merely because the independent receipts themselves came from individuals. For an ordinary company service relationship, the company collects the individual's contribution. Payer exceptions and mixed activities must be classified before using the ordinary 11% example. INSS's current contribution guidance and Lei 8.212 arts. 12,14,21,28 and30 establish these distinctions.

A facultative contributor is a separate affiliation for a person not exercising paid activity that makes them compulsorily insured. A zero-income month does not let an already compulsory situation be relabelled facultative at will. The qualified low-income facultative 5% route is distinct from MEI; it must not be offered merely because somebody is not a MEI. The current INSS page describes its no-own-income, exclusive domestic-work and low-income CadÚnico conditions. Full enrolment validation is a separate specialist check, not assumed here.

An ordinary eligible MEI pays its social component through DAS-MEI, not the normal self-employed GPS. The value in the table is only that component, not the entire DAS including the relevant business taxes. Special MEI categories, including transport/trucker cases, require their own verified rate and eligibility; do not generalise the ordinary row to them. Exceeding MEI business limits calls for the proper business exclusion/regularisation analysis, not automatic treatment of every company receipt as personal self-employed remuneration.

## Rates, bands and thresholds

| Item | Amount/rate and condition | Period | Official source |
|---|---|---|---|
| Monthly individual contribution base floor and ceiling | BRL 1,621 to BRL 8,475.55; aggregate same-month covered remuneration before testing the ceiling | From January 2026 | [Portaria MPS/MF 13/2026 art. 2](https://www.gov.br/previdencia/pt-br/assuntos/rpps/documentos/PortariaInterministerialMPSMF13de9dejaneirode2026.pdf) |
| Own-account normal plan | 20% of the applicable contribution base; ordinary full-month minimum BRL 324.20 and maximum BRL 1,695.11, rounded to cents | 2026 | [Lei 8.212 art. 21](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html); [Portaria 13 art. 2](https://www.gov.br/previdencia/pt-br/assuntos/rpps/documentos/PortariaInterministerialMPSMF13de9dejaneirode2026.pdf) |
| Eligible simplified own-account plan | 11% of the minimum, BRL 178.31. Own-account work without company/equivalent service and not the concurrent employment case in SC Cosit 130; reduced-plan restrictions and complement rules apply | 2026 | [Lei 8.212 art. 21 §2 I](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html); [INSS simplified plan](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/plano-simplificado) |
| Ordinary MEI social component | 5% of minimum = BRL 81.05, only ordinary eligible MEI; not the whole DAS or every special MEI category | 2026 | [INSS contribution guidance, MEI portion](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/contribuicao-dos-segurados-facultativo-e-contribuinte-individual); [Lei 8.212 art. 21 §2 II](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html) |
| Ordinary individual service to companies | 11% of remuneration within the combined ceiling, ordinarily maximum BRL 932.31 for that category; not an employee-progressive maximum or the simplified plan | 2026 | [MPS contribution explanation](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/arquivos/aeps-2024/secao-v-contribuintes/apresentacao-contribuintes); [INSS company-payment responsibility](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/contribuicao-dos-segurados-facultativo-e-contribuinte-individual) |
| Ordinary company-paid remuneration below the minimum | A missing contribution base may require complement at 20% of the difference to the minimum, subject to total concurrent remuneration and the actual category; not 9% on every company receipt | 2026 | [MPS contribution explanation, below-minimum paragraph](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/arquivos/aeps-2024/secao-v-contribuintes/apresentacao-contribuintes) |
| Simplified-to-normal complement | Additional 9% of the applicable historic minimum plus legal interest; for eligible reduced-plan periods requiring time/CTC treatment. Not an automatic ordinary-company top-up | Relevant historic competence | [INSS simplified plan, complement paragraph](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/plano-simplificado); [Lei 8.212 art. 21 §3](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html) |

The prior file's BRL 1,630 minimum and its remaining 2025 floor/ceiling calculations are superseded. Employee contribution rates use progressive bands under Portaria art. 7/Annex II, whereas the individual rows above use their own categories. Do not add contributions by comparing two categories' cash maxima. It is the contribution remuneration/base and actual same-month allocation that must be reconciled.

## The base

For a simple full-month own-account normal case with no concurrent covered employment or company withholding, identify qualifying remuneration, restrict it to the ceiling and apply the minimum-base requirement: `base = min(max(remuneration,1621),8475.55)`; contribution is `round(base × 20%,2)`. This formula assumes actual remunerated activity and the ordinary full-month category. It does not create an obligatory contribution for somebody who did no qualifying paid work, override MEI, or solve partial/concurrent/benefit months.

For eligible simplified work, calculate 11% × BRL 1,621 = BRL 178.31. Confirm eligibility before comparing cost. The INSS plan page includes age pension, sickness/incapacity, disability, death pension, maternity and imprisonment-related support subject to each benefit's conditions. “Only age pension” was an incorrect description of all benefits. The reduced contribution does not by itself count for the excluded contribution-time pension/CTC purpose without the prescribed complement; the normal plan likewise does not guarantee every benefit without age, qualifying-period, insured-status and applicable transition conditions.

For ordinary services to a company, reconcile the actual company's 11% withholding and its reported remuneration. BRL 6,000 × 11% = BRL 660 ordinarily withheld; do not generate an additional BRL 540 merely by subtracting 11% from the normal 20% rate. A shortfall to the statutory minimum is a different complement. Special exempt/charitable payers, other equivalents and mixed own-account/PJ income need their actual classification; their complete exception mechanics are not confirmed in this ordinary algorithm.

For concurrent CLT and own-account work, SC Cosit 130 requires the normal individual contribution category, not a simplified 1163 election. Collect the remuneration/base already subject to contribution in the same competence and documentary proof given to later payers. If covered employment has already used the entire BRL 8,475.55 monthly ceiling, no additional same-month base remains for ordinary individual activity. If it used less, allocate only the remaining ceiling under the actual category rules; do not subtract an employee's progressive cash contribution from the normal-plan cash maximum. Multiple companies need evidence to prevent each independently using the full ceiling. An apparent excess is a refund/adjustment investigation, not permission to silently net a refund against an unrelated month.

Official social-security contributions actually borne and paid/withheld may enter legal IRPF deductions under RIR arts. 67,75-76 and its related provisions. The annual simplified income-tax deduction replaces legal deductions; do not deduct INSS again in that branch. Monthly personal deductions must not be duplicated against salary and Carnê-Leão. This contribution Guide supplies payment evidence and classification to the income-tax owner; it does not claim every DAS component is personal INSS or deductible on the same basis.

## Deadlines and filing

| Route/code | Meaning and timing | Official source |
|---|---|---|
| GPS 1007 | Ordinary urban individual normal monthly contribution; own GPS due the 15th of the following month, postponed to the first bank business day if banks are closed | [INSS contribution guidance](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/contribuicao-dos-segurados-facultativo-e-contribuinte-individual); [official code table](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-codigos-de-pagamento-de-contribuicao-previdenciaria) |
| GPS 1163 | Eligible urban individual simplified monthly contribution; same ordinary own-GPS timing | [INSS simplified plan and code](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/plano-simplificado) |
| GPS 1104 / 1180 | Normal / simplified urban individual quarterly code identities, respectively. They are not company-withholding codes. Quarterly eligibility and its specific calendar must be verified before choosing this route | [INSS official code table](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-codigos-de-pagamento-de-contribuicao-previdenciaria) |
| GPS 1295 / 1198 | Individual simplified-plan complement, monthly / quarterly identity; 9% of the relevant minimum plus required accruals. Not the routine contribution for a company payment | [INSS official complement-code table](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-codigos-de-pagamento-de-contribuicao-previdenciaria) |
| GPS 1406 / 1473 | Facultative normal / simplified monthly identities; separate eligibility from a compulsory individual contributor | [INSS official code table](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-codigos-de-pagamento-de-contribuicao-previdenciaria) |
| Ordinary DAS-MEI | Social component paid through PGMEI/DAS-MEI; due the 20th next month, postponed if no bank business day. No-turnover alone does not cancel the registered MEI monthly obligation | [INSS MEI payment paragraph](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/contribuicao-dos-segurados-facultativo-e-contribuinte-individual); [Simples owner](br-simples-nacional.md) |
| Ordinary company collection | Responsibility lies with the company; reconcile the reported/withheld contribution rather than pay an individual GPS again by default | [INSS company-service paragraph](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/contribuicao-dos-segurados-facultativo-e-contribuinte-individual) |

Before generating a payment, reconcile the existing registration and CNIS/CPF/NIT/PIS/PASEP identifiers, competence, category, actual remuneration and prior payments. Registration/duplicate-record correction requires the current official INSS workflow; no extra registration number should be invented to force a calculation through. The simplified-plan page identifies Receita Federal's SAL, the INSS payment booklet and convened-bank applications as generation/payment routes. Confirm the actual supported channel; this Guide does not guarantee acceptance by every bank or lottery outlet. Preserve the generated guide, payment receipt and later contribution record, since generation is not proof of payment or benefit credit.

## Penalties and interest

Lei 8.212 art. 35 refers ordinary arrears to Lei 9.430 art. 61. The daily late fine is 0.33%, capped at 20%, counted from the first day after maturity through payment. Interest uses the statutory monthly SELIC accumulation from the month following maturity through the month before payment, plus 1% in the payment month; no interest is due when paid in the maturity month. It is not “daily SELIC”. Use the actual SAL/official calculation and competence/payment date, not a guessed current index.

Do not apply that ordinary late-charge formula indiscriminately to every historic complement or indemnity. Lei 8.212 art. 45-A expressly addresses remunerated activity reached by decadence that the individual wishes counted: an INSS indemnity may be required. Tax-credit limitation, proof of old work, qualifying contribution/carência and benefit recognition are distinct. The former blanket “retroactive at most five years” and “unpaid periods never count” statements were not a valid complete rule. Obtain the official activity/period assessment and calculation; this Guide does not calculate the historic indemnity or determine benefit entitlement.

## Cross-border points

A foreign coverage agreement/certificate can change an individual's applicable social-security position, but nationality or an overseas customer alone establishes no exemption. Obtain the actual treaty, worker category, assignment and certificate conditions through [brazil-cross-border-tax](brazil-cross-border-tax.md) and an appropriate social-security specialist. Bilateral totalisation, posted-worker periods, treaty exemptions and foreign-record validation are not confirmed here. Record the unresolved issue and source needed before producing a contribution instruction.

## Two worked examples that recompute

### Example 1: eligible own-account plan decision

Assume an urban own-account worker with BRL 4,000 remuneration, no company/equivalent services and no concurrent covered base. Normal contribution is BRL 800. If the simplified conditions are met, its current payment is BRL 178.31, BRL 621.69 less. If applicable contribution-time/CTC recognition is required, the reduced plan alone is insufficient: choose the normal route or obtain the prescribed assessment/complement for the relevant periods, rather than select the lower amount as an equivalent benefit package. A complement of a 2026 simplified minimum would have principal BRL 145.89 before any legal interest; that complements the minimum base, not necessarily the worker's full remuneration history. Eligibility and benefit objective decide the route, not price alone.

```oa-check
name: BR 2026 own-account normal versus eligible simplified contribution
inputs:
  remuneration: 4000
  minimum: 1621
  ceiling: 8475.55
steps:
  - normal_base: min(max(remuneration, minimum), ceiling)
  - normal_payment: round(normal_base * 0.20, 2)
  - simplified_payment: round(minimum * 0.11, 2)
  - current_difference: normal_payment - simplified_payment
  - complement_principal: round(minimum * 0.09, 2)
expected:
  normal_payment: 800
  simplified_payment: 178.31
  current_difference: 621.69
  complement_principal: 145.89
```

### Example 2: ordinary company withholding and multiple-payer ceiling

A single ordinary company payment of BRL 6,000 ordinarily produces BRL 660 withheld, with no automatic BRL 540 extra GPS. Now assume instead two ordinary company payers each pay BRL 5,000 in one month, no other covered income. Combined remuneration is BRL 10,000, but the combined covered base is capped at BRL 8,475.55. Total ordinary individual withholding should be BRL 932.31, subject to actual payer allocation/rounding. If both took BRL 550 with no shared evidence, BRL 1,100 was withheld and the apparent BRL 167.69 excess needs documented correction/refund review. Do not carry this 11% cash maximum over to employee progressive contributions.

```oa-check
name: BR 2026 ordinary company withholding and ceiling reconciliation
inputs:
  single_payer_remuneration: 6000
  payer_a: 5000
  payer_b: 5000
  ceiling: 8475.55
steps:
  - single_withholding: round(min(single_payer_remuneration, ceiling) * 0.11, 2)
  - combined_base: min(payer_a + payer_b, ceiling)
  - correct_combined: round(combined_base * 0.11, 2)
  - assumed_actual: round(payer_a * 0.11, 2) + round(payer_b * 0.11, 2)
  - apparent_excess: assumed_actual - correct_combined
expected:
  single_withholding: 660
  correct_combined: 932.31
  assumed_actual: 1100
  apparent_excess: 167.69
```

### Preserved edge-case and regression checklist

| Earlier case | Correct 2026 treatment / result |
|---|---|
| EC1, reduced plan needs contribution-time/CTC recognition | Qualified complement or normal route with pension-rule review; 1295 is a simplified complement, not ordinary company withholding |
| EC2, CLT at ceiling plus own-account income | BRL 8,475.55 covered employment base uses the ceiling, leaving no further ordinary same-month base; the former BRL 8,157.41 is not the current ceiling |
| EC3, BRL 6,000 company payment | BRL 660 ordinary withholding; no default BRL 540 GPS |
| EC4, BRL 800 own-account remuneration | Ordinary full-month normal floor BRL 324.20; eligible simplified BRL 178.31; establish category rather than charge an employee's unrelated formula |
| EC5, several companies and excess | Aggregate base and evidence, ordinary 11% maximum BRL 932.31; investigate actual excess/refund route |
| EC6, no paid work in a month | No automatic new own-account minimum; facultative status needs eligibility; MEI monthly DAS and existing mandatory status must be checked separately |
| Test1, own-account BRL 4,000 normal | BRL 800, ordinary monthly code 1007 |
| Test2, own-account BRL 12,000 normal | Capped base BRL 8,475.55; BRL 1,695.11 |
| Test3, eligible simplified with BRL 5,000 receipts | BRL 178.31 on the minimum, code 1163, if category conditions are met |
| Test4, BRL 6,000 ordinary company | BRL 660 withheld, not automatic BRL 540 extra |
| Test5, concurrent CLT at actual 2026 ceiling | No remaining ordinary same-month base; retain remuneration/withholding proof |
| Test6, no remunerated activity | Classify mandatory/facultative/MEI status; no blanket automatic compulsory payment |
| Test7, BRL 800 ordinary full-month own-account normal | Minimum base BRL 1,621; contribution BRL 324.20 |

## Ask the client first

1. Contribution competence/month, actual activity and payer: own account, ordinary company, equivalent/special payer, employee, MEI or no paid work?
2. All same-month remuneration and contribution bases, including concurrent CLT employment and services to several companies, with actual withholding evidence.
3. Existing CPF and NIT/PIS/PASEP registration/CNIS record, plan/payment codes, and any missing or duplicate periods.
4. Whether the reduced-plan conditions are actually met and whether contribution-time/CTC recognition is required under the person's applicable pension rules.
5. Paid/withheld amounts, payment dates, old periods, notices and benefit history; distinguish current contribution, late complement and historic indemnity.
6. Any foreign coverage agreement/certificate, special occupation, charitable/special payer or contested employment classification.

## When to refuse or refer

Stop a payment instruction when worker/payer classification, a foreign certificate, reduced-plan eligibility, concurrent evidence or actual competence is missing. Refer special payer exceptions, quarterly eligibility/calendar, MEI trucker/other special categories, low-income facultative validation, mixed-plan/base adjustments, refunds, historic indemnity, benefit carência/transition and contested employment. No current interest or historic complement calculation should be produced from an absent SELIC series or a single flat percentage.

The review handoff should contain competence, activity/payer classification, remuneration and contribution evidence, rule/source, possible routes, amount if supported, unresolved benefit purpose and the action requiring professional determination. An uncertain in-scope issue and an out-of-scope specialist issue both retain their facts and open question; neither should be assigned a fabricated approval tier or a “most likely” conclusion without evidence.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Lei 8.212 current Câmara text, arts. 12,14,21,28,30,35,45-A, contribution categories/base, reduced plan, collection and historic indemnity | https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html | 2026-11-11 |
| Portaria MPS/MF 13/2026, all four scanned pages visually read, especially art. 2 floor/ceiling and art. 7/Annex II employee distinction; published 12 January | https://www.gov.br/previdencia/pt-br/assuntos/rpps/documentos/PortariaInterministerialMPSMF13de9dejaneirode2026.pdf | 2026-11-11 |
| INSS current contribution guidance, own-account, MEI, facultative and company-service sections, payment dates and responsibility | https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/contribuicao-dos-segurados-facultativo-e-contribuinte-individual | 2026-11-11 |
| INSS simplified plan, eligibility, benefits, normal/simplified election and complement paragraphs | https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/plano-simplificado | 2026-11-11 |
| INSS code table, urban individual normal/simplified/quarterly and complement rows plus facultative identities; old domestic rows not reused as current rates | https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-codigos-de-pagamento-de-contribuicao-previdenciaria | 2026-11-11 |
| SC Cosit 130/2019, current official ementa read in normal browser, concurrent own-account/employment exclusion from code1163 and combined ceiling; attached full PDF not read | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/99870 | 2026-11-11 |
| MPS contribution explanation, individual own-account/company-paid distinction and below-minimum 20% complement paragraph; statistical tables not used for current monetary limits | https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/arquivos/aeps-2024/secao-v-contribuintes/apresentacao-contribuintes | 2026-11-11 |
| Lei 9.430 art. 61 and neighboring paragraphs, ordinary late fine, monthly SELIC and payment-month rule | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm | 2026-11-11 |
| LC 123 current Senate text, art. 18-A caput only, fixed monthly MEI payment independent of monthly revenue; no deferred turnover limit copied | https://legis.senado.gov.br/norma/572878/publicacao/34621013 | 2026-11-11 |
| RIR/2018 current Câmara text, arts. 67,75-77 and121, legal personal deductions, simplified replacement and no duplicate monthly deductions | https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html | 2026-11-11 |

Not yet confirmed: complete special-payer/charitable and mixed own-account/company allocation procedures; quarterly eligibility and exact calendar; MEI special/trucker rates and exclusion details; low-income facultative enrolment validation; current registration/duplicate-record/individual refund procedures; historic activity proof, carência and late-payment/indemnity recognition; post-2019 pension-transition outcomes; bilateral coverage/certificates; complete benefit conditions and case-specific interest. The prior universal five-year retroactivity cap, age-only benefit claim, company 9% top-up and unverified lottery-payment guarantee are not used.
