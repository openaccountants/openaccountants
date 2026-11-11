---
name: br-regional-payroll
description: >
  Select the applicable regional wage floor for Brazilian private employment in
  calendar 2026 before computing payroll. Covers the occupation bands and effective
  dates in Paraná, Santa Catarina, São Paulo and Rio Grande do Sul, collective
  agreement precedence, remote-work territorial rules, Rio de Janeiro's conflicting
  historical tables and Supreme Court judgment, and eSocial salary-change evidence.
  Use for piso regional, salário mínimo estadual, state minimum wage, collective
  agreement wage floor, retroactive salary differences, CBO classification and
  multistate or remote employee payroll. Produces a dated salary-selection workpaper
  for the national payroll owner. It does not approve a particular collective
  agreement's validity or replace the full payroll calculation.
jurisdiction: BR
job: regional-wage-floor-selection
category: payroll
type: computation
tax_year: 2026
tier: 2
last_updated: 2026-11-11
version: 0.1
depends_on:
  - brazil-payroll
---

# Brazil: regional wage floors and collective-agreement selection v0.1

**General reference only. Built from the law. Not yet approved.** This version has no accountant approval. Select the actual employee's law, territory, occupation and period before transferring a salary to payroll.

## Who this applies to

Employers selecting the lawful basic salary for private employees in Brazil during calendar 2026, including a regional-floor check before admission, a salary adjustment, a territorial transfer or a collective-agreement update. Amounts below are monthly BRL for the stated full monthly employment assumption. An hourly, part-time, apprentice, public-service, domestic or sector-specific contract needs its own entitlement and working-time checks. The existence of a state floor is not a national tax or contribution rate.

[LC 103/2000 art. 1](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp103.htm) authorises state and Federal District floors for employees **without** a floor defined by federal law, a collective convention (CCT) or a collective agreement (ACT). It permits extension to domestic employees and excludes municipal public servants from that delegation. Do not calculate `max(national, state, CCT)` before deciding which provisions apply: the state floor may be excluded when an applicable collective instrument sets a different floor. Keep the national minimum and non-reducible rights separate ([CLT arts. 611-B IV and 620](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html)).

**Ownership:** this Guide selects the regional/collective salary and computes a basic-salary shortfall. [Brazil payroll](brazil-payroll.md) owns INSS, IRRF, employer charges, FGTS, full entitlements and payment reconciliation; check that owner's actual year and approval status. Its proposed later text does not acquire Ariane Marrocos's historical approval through this new Guide. No existing approval statement is changed here.

## Rates, bands and thresholds

Apply the eligibility, effective date and occupational band on the same row. A listed state does not mean all employees there receive its highest band.

| Place and period | Monthly floor or selection rule | Conditions and primary source |
|---|---|---|
| National baseline, from 1 January 2026 | BRL 1,621.00 monthly; BRL 54.04 daily; BRL 7.37 hourly | Decree 12.797/2025 arts. 1-2. The stated daily and hourly figures are enacted amounts, not a licence to divide every state's monthly floor by an assumed divisor. https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12797.htm |
| SP, 1 January to 31 May 2026 | BRL 1,804.00 for each of the two listed groups | Lei 18.153/2025 art. 1, carried into the start of 2026 before the next amendment. Match the listed occupation and Lei 12.640 art. 2 exclusions. https://www.al.sp.gov.br/repositorio/legislacao/lei/2025/lei-18153-02.06.2025.html |
| SP, from 1 June 2026 | BRL 1,874.36 for each of the two listed groups | Lei 18.471/2026 arts. 1-2, published 28 May ([official publication record](https://dgui.cps.sp.gov.br/dgui_atos_normativos/18-471/)); first day of the following month. Includes listed domestic workers, office assistants, cleaners and occupations described below. This is not the separate public-servant abono law. https://www.al.sp.gov.br/repositorio/legislacao/lei/2026/lei-18471-27.05.2026.html |
| PR, from 1 January 2026, Group I | BRL 2,105.34; enacted hour BRL 9.57 | Agricultural, forestry and fishing workers in CBO major group 6; Decree 13.182 art. 1 I, with art. 3 exclusions. https://www.trabalho.pr.gov.br/sites/default/arquivos_restritos/files/documento/2026-04/decreto_13182_-_piso_minimo_regional_parana_2026.pdf |
| PR, same period, Group II | BRL 2,181.63; enacted hour BRL 9.92 | Administrative/service/retail/repair and maintenance occupations in CBO major groups 4, 5 and 9; art. 1 II.https://www.trabalho.pr.gov.br/sites/default/arquivos_restritos/files/documento/2026-04/decreto_13182_-_piso_minimo_regional_parana_2026.pdf |
| PR, same period, Group III | BRL 2,250.04; enacted hour BRL 10.23 | Industrial goods/services production, CBO major groups 7 and 8; art. 1 III.https://www.trabalho.pr.gov.br/sites/default/arquivos_restritos/files/documento/2026-04/decreto_13182_-_piso_minimo_regional_parana_2026.pdf |
| PR, same period, Group IV | BRL 2,407.90; enacted hour BRL 10.94 | Mid-level technical workers, CBO major group 3. Civil registrars are also expressly addressed for the statutory fee purpose; do not classify every office employee as a technician. Art. 1 IV and sole paragraph.https://www.trabalho.pr.gov.br/sites/default/arquivos_restritos/files/documento/2026-04/decreto_13182_-_piso_minimo_regional_parana_2026.pdf |
| SC, from 1 January 2026, band I | BRL 1,842.00 | LC 895/2026 arts. 1-2 plus LC 459/2009 art. 1 I. Listed agriculture, extraction/beneficiation, fishing/aquaculture, domestic work, construction, musical instruments/toys, equestrian establishments and specified motorcycle/general transport workers excluding drivers. https://leis.alesc.sc.gov.br/ato-normativo/53941 ; https://leis.alesc.sc.gov.br/ato-normativo/16847 |
| SC, same period, band II | BRL 1,908.00 | Listed clothing/footwear, textiles, leather, paper/cardboard/cork, press distribution and newspaper-company administration, communications/telemarketing and furniture industries. The old healthcare entry in band II was repealed. LC 459 art. 1 II as amended; LC 895.https://leis.alesc.sc.gov.br/ato-normativo/53941 ; https://leis.alesc.sc.gov.br/ato-normativo/16847 |
| SC, same period, band III | BRL 2,022.00 | Listed chemical/pharmaceutical, cinema and food industries, general commerce and autonomous commercial agents' employees. LC 459 art. 1 III; LC 895.https://leis.alesc.sc.gov.br/ato-normativo/53941 ; https://leis.alesc.sc.gov.br/ato-normativo/16847 |
| SC, same period, band IV | BRL 2,106.00 | Listed metal/mechanical/electrical, printing, glass/ceramics, rubber, insurance, buildings/condominiums, tourism/hospitality, jewellery, school administration, culture, data processing, transport drivers and healthcare establishments. Read the exact subparagraph and exclusions. LC 459 art. 1 IV; LC 895.https://leis.alesc.sc.gov.br/ato-normativo/53941 ; https://leis.alesc.sc.gov.br/ato-normativo/16847 |
| RS, 1 January to 20 May 2026, bands I-V respectively | BRL 1,789.04 / 1,830.23 / 1,871.75 / 1,945.67 / 2,267.21 | Lei 16.311/2025 art. 1, before the next law takes effect. Category lists, federal/collective exclusions and the period must be matched. https://diariooficial.rs.gov.br/materia?id=1277058 |
| RS, from 21 May 2026, bands I-V respectively | BRL 1,884.75 / 1,928.15 / 1,971.89 / 2,049.76 / 2,388.50 | Lei 16.514/2026 arts. 1-4 and 7. The data-base is 1 May but the law expressly applies the amounts from publication, 21 May. Do not backdate the new amount to 1 May from the data-base alone. https://www.diariooficial.rs.gov.br/materia?id=1428596 |
| RJ, historical Lei 8.315/2019 table | No operative 2026 salary selected from that table | STF ADI 6244 declared that law unconstitutional in its entirety. Examine any separate surviving/successor rule and the actual CCT/ACT; no 2019 nominal amount is certified here for current private payroll. https://portal.stf.jus.br/processos/downloadPeca.asp?id=15343610761&ext=.pdf |
| Other states and DF | Select the national baseline plus the actual applicable federal/category/collective/contractual provisions | LC 103 grants authority; it is not evidence that a particular state exercised it, or that no local provision exists. This Guide does not certify the absence of floors in the remaining jurisdictions. https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp103.htm |

### Occupational mapping and the date that matters

**SP:** Lei 18.471 art. 1 I contains the long occupation list, including domestic workers, caregivers, general office assistants, cleaners, non-specialised workers in commerce/industry/administration, listed trades, telemarketing and production supervisors. Inciso II lists agricultural/forestry managers, hygiene/health workers, transport/communications chiefs, purchasing/sales supervisors, technical sales/commercial representatives and specified broadcasting/audio/cinema-equipment operators. Both groups now have the same amount. Obtain the actual duties; a business's tax CNAE alone does not establish the employee's occupation. Lei 12.640 art. 2 excludes workers with a federal/CCT/ACT floor, state/municipal public servants and apprenticeship contracts ([current base law, art. 2](https://www.al.sp.gov.br/repositorio/legislacao/lei/2007/lei-12640-11.07.2007.html)).

**PR:** use the CBO major groups expressly enumerated on the rates rows. The decree was signed on 1 April and its art. 4 addresses publication, while art. 1 expressly adjusts the amounts from 1 January 2026. Separate the instrument date from the remuneration effect. Art. 2 requires a CETER deliberation if the national minimum changes again in 2026; it does not authorise the employer to invent an automatic percentage increase. Art. 3 excludes employees with a federal/CCT/ACT floor and public servants ([whole decree](https://www.trabalho.pr.gov.br/sites/default/arquivos_restritos/files/documento/2026-04/decreto_13182_-_piso_minimo_regional_parana_2026.pdf)).

**SC:** LC 895 was published on 26 March but expressly produces effects from 1 January 2026. Read the current occupational subparagraphs of LC 459, not an old headline or a compilation that opens a different law. Tourism/hospitality belongs to IV f after LC 551/2011; healthcare establishments belong to IV l after LC 624/2014, with the previous II g repealed. LC 459 art. 3 limits the regional floors to employees without a federal/CCT/ACT floor. Its art. 2 says the floors do not replace the constitutional national minimum and addresses the permitted/employer-established workload ([LC 459 arts. 1-3 and amendment links](https://leis.alesc.sc.gov.br/ato-normativo/16847)).

**RS:** under Lei 16.514 art. 1, band I includes listed agriculture, extraction, fishing, domestic work, tourism/hospitality, construction, toys/instruments, equestrian work, motoboys and parking. Band II includes clothing/footwear, textiles/leather/paper, newspaper distribution/administration, healthcare, cleaning, telecom/call-centre and hotel/restaurant/bar workers. Band III includes furniture, chemical/pharmaceutical/cinema/food industries, general commerce, autonomous agents, cinema exhibition/distribution, goods movement and warehouse work. Band IV includes the listed metal/electrical/printing/glass/ceramics/rubber/insurance/building/jewellery/school/cultural/social-assistance, navigation and security occupations. Band V covers mid-level technical qualifications in the stated integrated/subsequent/concurrent courses. Match the exact statutory category when descriptions overlap. Art. 1 §2 additionally addresses workers without an organised category or floor; art. 4 excludes a federal/CCT/ACT floor and municipal public servants ([Lei 16.514 arts. 1-4](https://www.diariooficial.rs.gov.br/materia?id=1428596)).

### Rio de Janeiro: resolve authority and scope before an amount

**AUDIT FLASH POINT.** A historical regional-floor table does not establish an operative private-sector entitlement. The STF's ADI 6244 judgment, pp. 2-3, declares the whole Lei 8.315/2019 unconstitutional and also specified parts of Lei 7.898/2018. Its docket records unsuccessful clarification proceedings and finality on 25 September 2020. The decision did not invalidate every provision of the earlier law. Do not treat a six-band 2019 list as a current universal RJ floor, and do not infer that the national minimum disposes of every surviving regional or professional entitlement. Preserve the conflict in the workpaper; establish the current surviving/successor provision and actual instrument before certifying an RJ basic salary ([judgment](https://portal.stf.jus.br/processos/downloadPeca.asp?id=15343610761&ext=.pdf); [docket](https://portal.stf.jus.br/processos/detalhe.asp?incidente=5803460)).

## The base

### Select the rule before comparing salary amounts

1. Record the employee's establishment of assignment, actual work location, duties/CBO, employment type, remuneration period and contractual hours. Identify transfers, remote work and any differentiated professional category. For telework, CLT art. 75-B §7 applies the local legislation and collective instruments relating to the territorial base of the **establishment of assignment**. The employee's home postcode alone does not select another state's floor ([CLT art. 75-B §§7-8](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html)).
2. Establish any applicable federal professional floor and its working-time/judicial conditions. Locate the CCT, ACT and amendments covering the actual employer, employee category, territory and period. A document for one municipality or one employer is not automatically statewide. CLT art. 611 defines the representation boundary; art. 620 gives ACT conditions precedence over CCT conditions. Do not turn this into permission to reduce the national minimum, which art. 611-B IV protects ([CLT arts. 611, 611-B and 620](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html)).
3. Open the registered text in [MTE Mediador](https://www.gov.br/pt-br/servicos/registrar-instrumentos-coletivos-de-trabalho), using its consultation step. Retain registration/request numbers, signatories, dates, scope, floor and adjustment clauses, any admission/training period, offsets, retroactive-difference deadline and amendments. Registration is evidence of the instrument's text, not a court ruling on every clause. CLT art. 614 §3 caps duration at two years and forbids automatic continued effect after expiry; a new instrument and individual contractual rights still need separate examination ([CLT art. 614](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html)).
4. Where the regional statute's exclusion applies, use the applicable federal/CCT/ACT route. A CCT may itself incorporate the state floor or an adjustment if that floor rises; read the clause. Otherwise do not import the excluded state rate merely because it is higher. If the regional law applies, select its precise occupation and dated band. Then preserve any higher individually protected salary and other applicable rights. CLT art. 468 prohibits detrimental contractual changes merely because a different minimum could now be selected ([LC 103 art. 1](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp103.htm); [CLT art. 468](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html)).
5. For a full monthly fixed-salary comparison on the same hours and component basis, compute `basic shortfall = max(0, applicable basic salary - comparable basic salary already paid)`. Sum by competence. Separate ordinary basic pay from expenses, benefits, variable commissions, premiums and overtime. Whether a particular component can satisfy a professional floor depends on its own law/instrument. Do not offset unrelated benefits or an employer's contribution against the employee's basic shortfall.
6. Transfer the selected salary, effective periods, shortfalls and instrument evidence to [payroll](brazil-payroll.md). Recompute affected entitlements, contribution bases and withholding through that owner. A correct basic-salary difference is not a complete net-pay adjustment or a declaration that every earlier return should be reopened.

### A concrete collective exception, not a countrywide rate

[Mediador RS003311/2026, request MR051304/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR051304%2F2026) covers the specified clothing-industry parties and the **17 municipalities listed in clause 2**, including Montenegro and São Sebastião do Caí. Clause 1 states 1 August 2026 to 31 July 2027. Clause 3 sets BRL 1,727.00 monthly (BRL 7.85/hour) at admission and BRL 1,848.00 (BRL 8.40/hour) after 90 days; clause 3.3 expressly disclaims automatic linkage to the state floor. Those conditions are why the state's clothing band II amount does not automatically replace this CCT's amounts. Check the actual employer/category, competing ACT, admission date, workload and higher existing salary before applying it. This example certifies neither every clause nor all clothing workers in RS.

### Required workpaper output

For each employee and period retain: employer and assigned establishment; UF/municipality and territorial conclusion; occupation/CBO and facts supporting it; category/instrument identity and exact scope; law/act/article and official URL; publication/celebration date separately from remuneration-effect date; monthly/hourly basis and contractual hours; applicable floor; higher protected individual salary; comparable amount paid; monthly difference; source excerpt and read date; eSocial event references/receipts and remaining issues. Group employees only after proving those facts match. A multistate company can have several valid salary selections in the same payroll month.

## Deadlines and filing

This is a salary-selection supplement, not a separate regional payroll return. Determine the salary due for each competence and pass that result to the existing national payroll workflow. CLT art. 459 §1 provides the ordinary monthly-salary payment limit of the fifth working day of the following month; a retroactive award or collective difference can have its own expressly applicable payment clause. Domestic and other special employment routes require their own rule ([CLT art. 459](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html)).

For an employer using the corporate eSocial workflow, the [MOS S-1.3, consolidation through NO 08/2026, S-2206 pp. 229-233](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-08-2026.pdf) distinguishes an actual contract change from a mistake in the original admission:

1. An actual salary change uses **S-2206**, after the original S-2200. A salary that was wrong when the admission was sent calls for correction of the original event, not a fictional later change. Identify the worker by CPF and employment registration and retain the accepted receipt.
2. Set `{vrSalFx}` to the applicable fixed salary and the correct salary unit. Keep the true `{dtAlteracao}` and, for a retroactive law/CCT/ACT, `{dtEf}`. The manual distinguishes publication/celebration from the earlier date on which remuneration became due. A new signed instrument is not authority to overwrite the employee's entire previous history.
3. Under the cited MOS, send S-2206 by the stated following-month day 15 limit or before the monthly remuneration events where the alteration affects totalisers, with the manual's fiscal-working-day extension. The specific fixed-term extension rule is separate. Apply the earlier applicable event-sequence obligation, rather than treating day 15 as universal permission to wait.
4. MOS section 3 permits eligible law/collective retroactive differences through S-1200 `[InfoPerAnt]` in the instrument's month, identifying the original remuneration periods. Preserve intervening salary changes; use separate effective histories where needed. Do not assume this route applies to every historical error, court award, domestic employer or pension/tax incidence.
5. The corporate Web Geral manual's **Empregado > Gestão de Empregados > Alterar Dados Contratuais** route identifies “Data da Alteração” and “Data do Efeito da Alteração”. It is an older UI reference, not confirmation of every 2026 screen or XML field. Check the current published layout and the selected employer's supported software, then retain accepted event receipts, remuneration-period reconciliation and payment evidence ([Web Geral, S-2206 subsection](https://www.gov.br/esocial/pt-br/empresas/manual-web-geral)).

The regional-floor law itself does not establish a new INSS/IRRF/FGTS rate or a separate state DAS payment. Do not file or transmit merely because this selection workpaper is complete.

## Penalties and interest

A basic-wage shortfall is not a statutory penalty. Separate unpaid pay and resulting entitlement/charge adjustments from an ACT/CCT penalty, administrative labour assessment or judicial award. Read the actual governing instrument and notice before quantifying an additional liability. Lei 16.514's procurement/public-reference provisions do not establish a universal private-employer fine. No generic state wage-floor penalty percentage, labour-court update index or eSocial late-charge amount is certified by this Guide. Transfer any supported contribution/payment adjustment to its owning workflow.

## Cross-border points

Location of the employer's customer, sales invoice or bank account does not establish the employee's labour territory. For domestic multistate telework, apply CLT art. 75-B §7's assigned-establishment test and examine the actual contract. For an employee admitted in Brazil who chooses telework abroad, §8 has a specific Brazilian-law rule and an express contractual exception; it does not settle every foreign mandatory employment, immigration, social-security or tax obligation ([CLT art. 75-B §§7-8](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html)). Coordinate with [cross-border tax](brazil-cross-border-tax.md) and payroll without assuming that a tax-residence conclusion decides the labour-law floor.

## Two worked examples that recompute

### 1. São Paulo: apply the new law from the correct month

Hypothetical full-month cleaner within the statutory list, no federal/CCT/ACT floor, no other higher salary entitlement. Basic salary paid in May and June was BRL 1,804.00 each month. The May amount meets the applicable regional floor; June requires BRL 1,874.36. The June basic-pay difference is BRL 70.36. This does not include related payroll adjustments ([Lei 18.153 art. 1](https://www.al.sp.gov.br/repositorio/legislacao/lei/2025/lei-18153-02.06.2025.html); [Lei 18.471 arts. 1-2](https://www.al.sp.gov.br/repositorio/legislacao/lei/2026/lei-18471-27.05.2026.html)).

```oa-check
name: SP May and June 2026 basic salary only
inputs:
  paid_may: 1804
  floor_may: 1804
  paid_june: 1804
  floor_june: 1874.36
steps:
  may_shortfall: max(0, floor_may - paid_may)
  june_shortfall: max(0, floor_june - paid_june)
  basic_arrears: may_shortfall + june_shortfall
expected:
  may_shortfall: 0
  june_shortfall: 70.36
  basic_arrears: 70.36
```

### 2. Santa Catarina: the promulgation date is not the remuneration-effect date

Hypothetical band I construction employee, full monthly employment, no excluded federal/CCT/ACT floor or higher individual salary. The employer paid BRL 1,730.00 for each full January, February and March competence. LC 895 fixes BRL 1,842.00 with effects from 1 January 2026. The monthly basic difference is BRL 112.00 and the three-month difference is BRL 336.00. This example stipulates the amount paid; it does not use the old 2025 floor as a current rule. Refer the related payroll incidence and any intervening changes to the payroll owner ([LC 895 arts. 1-2](https://leis.alesc.sc.gov.br/ato-normativo/53941); [LC 459 art. 1 I f and art. 3](https://leis.alesc.sc.gov.br/ato-normativo/16847)).

```oa-check
name: SC retroactive 2026 band I basic differences
inputs:
  paid_per_month: 1730
  applicable_floor: 1842
  full_months: 3
steps:
  monthly_basic_difference: max(0, applicable_floor - paid_per_month)
  basic_arrears: monthly_basic_difference * full_months
expected:
  monthly_basic_difference: 112
  basic_arrears: 336
```

### 3. Rio Grande do Sul: choose the applicable branch before taking a maximum

Hypothetical November clothing-industry employee in Montenegro, full monthly employment, within both parties' representation in RS003311/2026, no overriding ACT, no federal professional floor and no higher protected salary. At admission the CCT floor is BRL 1,727.00, not the state's BRL 1,928.15 clothing band. If the applicable CCT did not cover the employment and all state-floor conditions were instead met, the same BRL 1,727.00 payment would fall BRL 201.15 short of the regional band. The factual applicability decision changes the answer. For the CCT branch, after the stipulated 90 days the floor becomes BRL 1,848.00; a continuing BRL 1,727.00 payment would then be BRL 121.00 short. These are separate scenarios, not permission to reduce an employee's established wage ([CCT clauses 1-3](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR051304%2F2026); [Lei 16.514 arts. 1 II and 4](https://www.diariooficial.rs.gov.br/materia?id=1428596)).

```oa-check
name: RS collective and residual state branches
inputs:
  paid: 1727
  admission_cct_floor: 1727
  post_90_day_cct_floor: 1848
  residual_state_floor: 1928.15
steps:
  covered_cct_admission_shortfall: max(0, admission_cct_floor - paid)
  uncovered_state_branch_shortfall: max(0, residual_state_floor - paid)
  covered_cct_post_90_day_shortfall: max(0, post_90_day_cct_floor - paid)
expected:
  covered_cct_admission_shortfall: 0
  uncovered_state_branch_shortfall: 201.15
  covered_cct_post_90_day_shortfall: 121
```

## Ask the client first

1. Which assigned establishment, UF/municipality and actual work locations apply, and did a transfer or telework arrangement change them?
2. What are the actual duties/CBO, professional category, employment type, admission date and contractual monthly/hourly workload?
3. Which federal professional law, CCT, ACT, amendment or court order covers this employer and employee, with what territory and validity/effect dates?
4. What basic salary and relevant components were contractually due and actually paid for each competence, including intervening promotions or protected increases?
5. Which original admission, salary-change and remuneration events/receipts exist, and are we correcting an original error or implementing a new retroactive instrument?
6. Is the requested output only salary selection, or also a supported payroll recalculation, payment, correction or dispute response through the relevant owner?

## Sources

Only the portions described below were checked. Browser reads cured direct-fetch blocks for LC 103, Decree 12.797, RS gazette text and the specific Mediador instrument. A current-year government document still needs a legal scope and judicial-status check.

| Source and portion actually read | Official URL | Read on |
|---|---|---|
| Read for LC 103/2000, whole act: residual floor delegation, collective/federal exclusions, municipal-public and domestic conditions | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp103.htm | 2026-11-11 |
| Read for Decree 12.797/2025, whole act: national monthly/day/hour amounts and commencement | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12797.htm | 2026-11-11 |
| Read for SP Lei 18.153/2025 arts. 1-2, preceding occupation amounts/effective-month rule | https://www.al.sp.gov.br/repositorio/legislacao/lei/2025/lei-18153-02.06.2025.html | 2026-11-11 |
| Read for SP Lei 18.471/2026, whole act: both occupation lists, amounts and next-month commencement | https://www.al.sp.gov.br/repositorio/legislacao/lei/2026/lei-18471-27.05.2026.html | 2026-11-11 |
| Read for SP Centro Paula Souza legislation record, publication metadata: 28 May 2026 | https://dgui.cps.sp.gov.br/dgui_atos_normativos/18-471/ | 2026-11-11 |
| Read for SP Lei 12.640/2007 current art. 1 amendment annotations and art. 2, distinguishing replaced text and current exclusions | https://www.al.sp.gov.br/repositorio/legislacao/lei/2007/lei-12640-11.07.2007.html | 2026-11-11 |
| Read for PR Decree 13.182/2026, all three PDF pages: four CBO groups/hourly amounts, retroactive date and exclusions | https://www.trabalho.pr.gov.br/sites/default/arquivos_restritos/files/documento/2026-04/decreto_13182_-_piso_minimo_regional_parana_2026.pdf | 2026-11-11 |
| Read for SC LC 895/2026, whole act: four amounts and January remuneration effects | https://leis.alesc.sc.gov.br/ato-normativo/53941 | 2026-11-11 |
| Read for SC LC 459/2009 arts. 1-3 with amendment annotations, including moved tourism/health categories and collective exclusions | https://leis.alesc.sc.gov.br/ato-normativo/16847 | 2026-11-11 |
| Read for RS Lei 16.311/2025 arts. 1-4 and commencement, preceding bands/category lists | https://diariooficial.rs.gov.br/materia?id=1277058 | 2026-11-11 |
| Read for RS Lei 16.514/2026, whole gazette text: categories, amounts, publication date, data-base and exclusions | https://www.diariooficial.rs.gov.br/materia?id=1428596 | 2026-11-11 |
| Read for STF ADI 6244 merits judgment pp. 1-3; clarification judgment pp. 1-2; docket outcome/clarification/finality entries | https://portal.stf.jus.br/processos/downloadPeca.asp?id=15343610761&ext=.pdf ; https://portal.stf.jus.br/processos/downloadPeca.asp?id=15344415365&ext=.pdf ; https://portal.stf.jus.br/processos/detalhe.asp?incidente=5803460 | 2026-11-11 |
| Read for CLT arts. 75-B §§7-8, 459, 468, 611, 611-B IV, 614 §3 and 620; territorial/contractual and collective-rule context | https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html | 2026-11-11 |
| Read for MTE registration/consultation service, consultation step and official Mediador route | https://www.gov.br/pt-br/servicos/registrar-instrumentos-coletivos-de-trabalho | 2026-11-11 |
| Read for Registered RS003311/2026, identity and clauses 1-4, especially territory, admission/90-day floors, independence from regional floor and difference-payment clause | https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR051304%2F2026 | 2026-11-11 |
| Read for eSocial MOS S-1.3 consolidated through NO 08/2026, S-2206 pp. 229-233: change vs correction, sequence, fields and retroactive salary examples | https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-08-2026.pdf | 2026-11-11 |
| Read for Web Geral manual, S-2206 subsection: older interface route and date labels only; no claim of a complete 2026 UI test | https://www.gov.br/esocial/pt-br/empresas/manual-web-geral | 2026-11-11 |

Not yet confirmed: a complete operative 2026 RJ regional-floor consolidation after the invalidity of Lei 8.315/2019, including surviving/successor rules and their judicial effects; exhaustive absence/presence checks for regional floors in the other states/DF; the actual client's federal professional floor and CCT/ACT validity or litigation; partial-month/hours divisors, commissions/top-ups and overlapping occupational-category disputes; every current eSocial XML validation and employer-specific 2026 screen, domestic retroactive procedure and payroll incidence; specific labour penalties, interest and court-award update computations. These do not invalidate supported full-month regional selections above, but a dependent unresolved selection cannot be labelled complete.
