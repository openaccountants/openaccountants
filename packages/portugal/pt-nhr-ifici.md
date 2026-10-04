---
name: pt-nhr-ifici
description: "Utilizar este skill sempre que questões envolvam o regime do Residente Não Habitual (RNH) em Portugal ou o seu sucessor, o Incentivo Fiscal à Investigação Científica e Inovação (IFICI). Acionar perante expressões como \"RNH\", \"Residente Não Habitual\", \"IFICI\", \"Incentivo Fiscal à Investigação Científica e Inovação\", \"20% taxa fixa\", \"nómadas digitais Portugal\", \"isenção rendimentos estrangeiros\", \"Modelo 3 anexo L\", \"Atividades de Elevado Valor Acrescentado\", \"AEVA\", \"Portaria 187/2024\", \"EBF artigo 58.º-A\", \"Despacho 230/2019\", \"pensões estrangeiras Portugal\", \"convenções dupla tributação Portugal\". Também acionar em pedidos formulados em inglês: \"Portugal NHR regime\", \"Portugal digital nomad tax\", \"non-habitual resident Portugal\", \"IFICI scheme Portugal\", \"20% flat rate Portugal\", \"foreign income exemption Portugal\", \"Portugal pension tax 10%\", \"Portugal tax residency\", \"NHR replacement Portugal\". Cobre o RNH legado criado pelo DL 249/2009 (fechado a novos pedidos desde 1 jan 2024 pela Lei 82/2023), o IFICI introduzido pela Portaria n.º 187/2024/1 ao abrigo do art.º 58.º-A do EBF, a taxa fixa de 20% sobre rendimentos das categorias A e B em Atividades de Elevado Valor Acrescentado, a matriz de isenção de rendimentos de fonte estrangeira por tipo de rendimento e país, o tratamento das pensões estrangeiras (incluindo a tributação a 10% introduzida pelo OE 2020), mais-valias e dividendos estrangeiros, convenções de dupla tributação aplicáveis (~80 acordos), processo de candidatura no Portal das Finanças até 31 de março do ano seguinte ao da residência, perda de estatuto por interrupção da residência, e preenchimento do Anexo L do Modelo 3. LER SEMPRE este skill antes de tratar fiscalidade RNH/IFICI em Portugal."
version: 1.0
jurisdiction: PT
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - pt-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal: the old NHR regime and its successor IFICI, for 2026

## Scope and status in 2026 ([EBF art. 58-A](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx); [NHR FAQ](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx))

This Guide covers two Portuguese personal income tax (IRS) regimes for people who move to Portugal:

- **NHR (residente não habitual, "RNH")**, created by Decree-Law 249/2009 and set out in the old wording of CIRS art. 16(8) to (12), 72(10) and (12) and 81(4) to (8). It was **revoked from 1 January 2024** by the 2024 Budget Law (Lei 82/2023). It still runs for people already registered and for a closed transitional group (art. 236 Lei 82/2023).
- **IFICI (incentivo fiscal à investigação científica e inovação, often described as the successor to NHR)**, in art. 58-A of the Tax Benefits Statute (EBF), added by Lei 82/2023. It applies to people who become tax resident **from 1 January 2024**. The procedure and the lists of professions and business codes are in **Portaria 352/2024/1 of 23 December 2024**.

Primary year: **tax year 2026** (Portugal's tax year is the calendar year). The rules below are the ones in force on 25 September 2026. A short dated section covers the 2025 returns (filed in 2026) and the 2024 and 2025 arrivals.

**What applies to 2026, in one table**

| Person | Regime available for 2026 |
| --- | --- |
| Registered as NHR on 1 January 2024 | NHR keeps running until its 10-year period ends ([NHR FAQ 5149](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx)) |
| Met the residence conditions on 31 December 2023 but registered as NHR afterwards (art. 236(3)(b)) | NHR, if registered by 31 March 2024 (the old CIRS art. 16(10) deadline for 2023 residents); runs to the end of the 10th year counted from the year of residence |
| Became resident in 2024 and meets an art. 236(3)(c) condition | NHR, but only if registered. A registration filed after 31 March 2025 still works, but only from the year it is filed until the end of the 10th year counted from 2024 (FAQ 6010) |
| Became resident in 2025 or 2026 | NHR is **not** available (FAQ 5153). IFICI if the activity qualifies; otherwise the general rules |
| Became resident in 2024 or later with a qualifying activity | IFICI (EBF art. 58-A) |

Not covered: Regressar (CIRS art. 12-A), IRS Jovem (art. 12-B), visas, trusts, the Azores and Madeira regional rules, and disputes against a refusal.

## Ask the client first

- **When did you become tax resident in Portugal?** Get the first day of presence and the year. Residence follows CIRS art. 16(1): more than 183 days, consecutive or not, in any 12-month period starting or ending in the year, **or** fewer days but a home on any day of that period that suggests an intention to keep and occupy it as a habitual residence. A day of presence is any day, full or partial, that includes an overnight stay ([CIRS art. 16](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx)).
- **Were you tax resident in Portugal at any time in the five years before that year?** If yes, neither NHR nor IFICI is available. Nationality does not matter.
- **Have you ever been registered as NHR, used IFICI before, or opted for the Regressar regime (art. 12-A)?** Any of these blocks IFICI (EBF art. 58-A(10) and (12)).
- **What exactly is your work in Portugal, and under what contract?** Employment contract, company-board seat, research grant, or self-employed services. For most IFICI routes a "posto de trabalho" means an employment contract.
- **Who is the employer or client, and what do they do?** Higher-education or research body, technology and innovation centre, startup certified under Lei 21/2023, company with contractual investment benefits, company using RFAI, exporter with an eligible business code, or a company recognised by AICEP or IAPMEI.
- **Your qualifications and experience.** Some routes need a doctorate, or a degree or master's plus three years of professional experience.
- **Registration status.** For NHR: registration year shown on the Portal das Finanças. For IFICI: the date the request was filed and the status the AT shows.
- **Foreign income, by type and country.** Employment, self-employment, dividends, interest, rent, gains, pensions. Note which paying countries are on Portugal's list of privileged tax regimes.
- **For NHR pensioners: were you already tax resident in Portugal on 31 March 2020?** This decides whether a foreign pension is exempt or taxed at the NHR pension rate.
- **For 2024 NHR transitional cases:** which of the art. 236(3)(c) documents do you hold, and on what date was it signed or completed?

## The method, step by step

1. **Confirm residence and the five-year look-back.** Apply CIRS art. 16(1) and (2) for the arrival year. A person meeting the 183-day or habitual-home test becomes resident from the first day of presence, unless they were resident on any day of the previous year ([CIRS art. 16(3)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx)). Both regimes require that the person was **not resident in any of the five previous years** ([EBF art. 58-A(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx); old [CIRS art. 16(8)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs16bra_202312.aspx)).

2. **Sort the person into a regime by arrival year**, using the table under "Scope". Resident by 31 December 2023: NHR if registered (art. 236(3)(a) and (b) Lei 82/2023). 2024 arrival: NHR only under art. 236(3)(c) or (d). 2025 or later: IFICI or the general rules. A past NHR beneficiary cannot switch to IFICI or renounce NHR ([NHR FAQ 6011](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx); EBF art. 58-A(10)(a)).

3. **For the 2024 NHR transitional group, test art. 236(3)(c) exactly.** The person must become resident by 31 December 2024 **and** declare one of these ([text reproduced under CIRS art. 81](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx)):

| Document | Cut-off date |
| --- | --- |
| Employment contract or promise, or secondment agreement or promise, for work to be done in Portugal | concluded by 31 December 2023 |
| Lease or other contract giving use or possession of a property in Portugal | concluded by 10 October 2023 |
| Reservation contract or promissory contract to acquire a real right over a property in Portugal | concluded by 10 October 2023 |
| Enrolment of dependants in a school in Portugal | completed by 10 October 2023 |
| Residence visa or residence permit | valid by 31 December 2023 |
| Visa or residence-permit procedure (including a request for, or a booked, appointment) | started by 31 December 2023 |

Family-household members of a qualifying person also qualify (art. 236(3)(d)). The lease, property and school dates are **10 October 2023**, not 31 December 2023.

4. **For IFICI, match the activity to one letter of EBF art. 58-A(1)** and to the conditions in Portaria 352/2024/1 (see the activity table below). Check three things: the person's role (employment, board member, research grant, or listed profession), the entity (what it is and who recognises it), and the person's qualifications. A "posto de trabalho" (job) needs an employment contract; see the boundary table for contractors, lecturers and shareholders.

5. **Check the exclusions.** No IFICI after NHR, after an art. 12-A election, or a second time; none for pay for jobs counted under CFI art. 22(2)(c) (EBF art. 58-A(10) to (12)). From 2025, IFICI users cannot use IRS Jovem ([IFICI leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/incentivos_investigacao.pdf)).

6. **Check registration and the deadline.**

- Prerequisite for both: a Portuguese tax number (NIF) and a Portuguese tax address, so that the AT register shows the person as resident for the year. Portaria 352/2024/1 art. 2(1) addresses IFICI requests to "sujeitos passivos registados como residentes". While the register still shows the person as non-resident, the Portal will not accept an NHR request; with a retroactive address change pending, raise it through e-balcão by the 31 March deadline ([NHR FAQ 6007](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx)).
- IFICI: file on the Portal das Finanças (Cidadãos > Serviços > Benefícios Fiscais > Inscrição no IFICI) **by 15 January of the year after the year the person becomes resident** ([Portaria 352/2024/1, art. 2(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_352_2024_1.pdf)). If filed late, IFICI applies from the year of filing for the rest of the 10 years (EBF art. 58-A(7)).
- NHR (2024 transitional group): request on the Portal das Finanças by 31 March 2025. A late request, if granted, applies from the year it is filed until the end of the 10th year counted from 2024 (art. 236(5); [NHR FAQ 6008 and 6010](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx)).

7. **Tax Portuguese-source work income.** Under IFICI, net category A (employment) and B (self-employment) income from the qualifying activity may be taxed at the special flat rate; under NHR, the same applies to net A and B income from a listed high-value activity (old CIRS art. 72(10)). Everything else is taxed under the general rules. The person may instead opt to aggregate (englobamento).

8. **Treat foreign income** using the matrix under "Foreign income" below.

9. **Test each year of the 10-year period.** The person must be resident at some point in the year and, for IFICI, must still earn income from a qualifying activity. A new qualifying activity keeps the benefit if it starts within six months after the old one ends (EBF art. 58-A(3) and (4)). Years lost to non-residence are not added on at the end; the person resumes only for the years left (art. 58-A(5); old CIRS art. 16(12)).

10. **File** Modelo 3 with Annexes L and J (see "Filing and payment").

## Rates, deadlines and figures by year

### Rates ([EBF art. 58-A(2)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx); [CIRS art. 72, wording to December 2023](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs72ra_202312.aspx); [IFICI FAQ 5495](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx))

| Item | Figure | Years |
| --- | --- | --- |
| IFICI special rate on net category A and B income from the qualifying activity | 20% | 2024 onward, for 10 consecutive years from the year of registration as resident; aggregation (englobamento) can be chosen instead |
| IFICI withholding on qualifying category A or B pay, once the payer is shown proof the request was filed | 20% | 2025 onward. Withholding is only a payment on account; if IFICI is refused, the general rates apply on assessment ([IFICI leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/incentivos_investigacao.pdf)) |
| IFICI: foreign income of any category paid by an entity in a listed privileged-tax jurisdiction | 35% | 2024 onward (CIRS art. 81(5)); final withholding or autonomous taxation depending on who pays |
| NHR special rate on net category A and B income from a listed high-value activity | 20% | Whole NHR period (old CIRS art. 72(10), kept by art. 236(3)) |
| NHR rate on net foreign pensions (category H and the listed similar income) that are not Portuguese-source | 10% | People who became resident after 31 March 2020, and earlier NHRs who opted in (old CIRS art. 72(12); Lei 2/2020 art. 329) |
| General IRS rates, 2026 table | 12.50% up to 48% | 2026 ([CIRS art. 68](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx), wording of Lei 73-A/2025) |
| Additional solidarity rate on taxable income over EUR 80,000 | 2.5% up to EUR 250,000; 5% above | Unchanged ([CIRS art. 68-A](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx)) |
| Special rate on capital income and on the net balance of listed gains (general rules, not NHR/IFICI) | 28% | 2026 ([CIRS art. 72(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx)) |

The 2026 bracket table (CIRS art. 68, 2026 wording) is needed for any comparison with the general rules:

| Taxable income (EUR) | Marginal rate | Average rate on the whole band |
| --- | --- | --- |
| up to 8,342 | 12.50% | 12.500% |
| over 8,342 to 12,587 | 15.70% | 13.579% |
| over 12,587 to 17,838 | 21.20% | 15.823% |
| over 17,838 to 23,089 | 24.10% | 17.705% |
| over 23,089 to 29,397 | 31.10% | 20.579% |
| over 29,397 to 43,090 | 34.90% | 25.130% |
| over 43,090 to 46,566 | 43.10% | 26.472% |
| over 46,566 to 86,634 | 44.60% | 34.856% |
| over 86,634 | 48.00% | n/a |

Method (art. 68(2)): the part of income up to the top of the highest full band is taxed at that band's average rate; the excess is taxed at the next band's marginal rate.

### Deadlines by arrival year ([IFICI leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/incentivos_investigacao.pdf); [IFICI FAQ 5858](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx); [NHR FAQ](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx))

| Became resident in | Regime | File the request by | Entities report to the AT and companies confirm by | AT shows status by |
| --- | --- | --- | --- | --- |
| 2023 or earlier | NHR | 31 March of the following year (old CIRS art. 16(10)) | n/a | n/a |
| 2024 | NHR (art. 236 group) | 31 March 2025; later requests start from the year filed | n/a | n/a |
| 2024 | IFICI (special dates, Despacho 24/2025-XXIV) | 31 March 2025 | 30 April 2025 | 15 May 2025 |
| 2025 | IFICI | 15 January 2026 | 15 February 2026 | 31 March 2026 |
| 2026 | IFICI | 15 January 2027 | 15 February 2027 (entities); 15 March 2027 (company confirmation for letter (c)) | 31 March 2027 |

For letter (c), the company confirms the conditions on its Portal area by 15 March (Portaria art. 4(2)). The 2026-arrival row applies the general rules (Portaria art. 2(1), 4(2), 6(1), 6(3)); the AT's FAQ gave 15 February 2026 for both steps for 2025 arrivals, so **check** the Portal for the 2027 dates.

A person who became resident in 2024 and applied for IFICI **before** the Portaria was published (23 December 2024) keeps the Portaria 12/2010 list of high-value activities for their whole IFICI period, as long as they keep doing that activity (IFICI FAQ 5859; EBF art. 58-A(8)).

### IFICI activities: EBF art. 58-A(1) and Portaria 352/2024/1 ([IFICI leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/incentivos_investigacao.pdf); [IFICI FAQ 5498 to 5512](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx))

| Letter | Who qualifies | Entity where the work is done | Reviews the activity |
| --- | --- | --- | --- |
| (a) | Higher-education teaching and scientific research, including scientific employment; jobs directly involved in research or innovation; board members | Higher-education institutions and bodies in the national science and technology system; technology and innovation centres (DL 126-B/2021) | FCT |
| (b) | Qualified jobs (at least EQF/ISCED level 5) and board members | Entities with contractual investment benefits (CFI chapter II) | AICEP |
| (c)(i) | Highly qualified professions in Portaria Annex I, held by someone with a doctorate, or a degree or master's plus three years' proven experience; also directors, managers and general managers | Companies with relevant investment that benefit, or benefited in the start year or the five prior years, from RFAI (CFI chapter III) | AT |
| (c)(ii) | Same professions and qualifications | Industrial and service companies whose main business code (CAE) is in Portaria Annex II and that export at least 50% of turnover in the start year or either of the two prior years (EU sales count, FAQ 5512) | AT |
| (d) | Qualified jobs listed in IAPMEI Notice 4812/2025/2 and AICEP Notice 5309/2025/2 (at least level 5), and board members | Companies in economic activities those agencies recognise as relevant to the economy | AICEP if the company's consolidated annual turnover in the prior year was EUR 75 million or more, or the project is PIN or PII; otherwise IAPMEI (FAQ 5525) |
| (e) | R&D staff whose costs qualify for SIFIDE (CFI art. 37(1)(b)), at least national qualifications level 4, directly involved in R&D | Companies using SIFIDE | ANI |
| (f) | Jobs directly involved in research or innovation, and board members | Startups certified under Lei 21/2023 | Startup Portugal |
| (g) | Jobs or other activities of residents of the Azores and Madeira | To be defined by regional decree | Regional governments |

Annex I professions (CPP codes): 112 general and executive directors; 12 administrative and commercial directors; 13 production and specialised-services directors (except 1349); 21 physical, mathematical and engineering specialists (except 216); 2163.1 industrial product or equipment designer; 221 doctors; 231 university and higher-education teachers; 25 ICT specialists (FAQ 5504). This list is narrower than the NHR list: dentists, authors and journalists, performing artists, and intermediate-level technicians are **not** in Annex I. The letter (d) list is wider in places: it adds 14 hospitality, retail and other services directors, 241 finance and accounting specialists (except 2411), 2654 film, stage, TV and radio directors and producers, and 31 intermediate science and engineering technicians. It applies only to employees or board members of a recognised company (FAQ 5508).

The AT reviews residence and the other legal conditions for every letter (Portaria art. 3(1)(b)).

### NHR high-value activities ([NHR leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/IRS_RNH_PT.pdf))

For activities carried on up to 31 December 2019, the list is the original table in Portaria 12/2010 (codes 101 to 802, for example architects, engineers, doctors, dentists, university teachers, IT programmers and senior company executives). For activities carried on from 1 January 2020, it is the CPP-based table in Portaria 12/2010 as amended by **Portaria 230/2019 of 23 July** (the legacy text called this "Despacho 230/2019 of 4 July", which is wrong). The 2020 table covers codes 112, 12, 13, 14, 21, 221, 2261, 231, 25, 264, 265, 31, 35, 61, 62, 7 and 8, plus investors, directors and managers of companies with CFI investment contracts. The workers need at least EQF level 4 (or the ISCED equivalent) or five years of proven professional experience. People already registered, or with a request pending, on 1 January 2020, and people who applied by 31 March 2020 for 2019, keep the old table but may choose the new one (Portaria 230/2019, art. 5).

## Foreign income ([CIRS art. 81, current](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx); [CIRS art. 81, wording to December 2023](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs81ra_202312.aspx))

First decide whether the income is foreign at all. Employment income is Portuguese-source if the work is **done in Portugal**, or if the pay is owed by an entity resident in Portugal or by a Portuguese permanent establishment ([CIRS art. 18(1)(a)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs18.aspx)). A remote worker living in Lisbon and paid by a US employer therefore has Portuguese-source employment income. It is not exempt as foreign income under either regime. It gets the flat rate only if the job itself qualifies.

| Income obtained abroad | IFICI (CIRS art. 81(4) and (5)) | NHR (old art. 81(4), (5) and (7); old art. 72(12)) |
| --- | --- | --- |
| A: employment | Exempt, with progression | Exempt if **taxed** in the other state under a treaty, or, with no treaty, taxed there and not Portuguese-source under art. 18(1) |
| B: self-employment | Exempt, with progression | Exempt only for high-value services of a scientific, artistic or technical nature, intellectual or industrial property, or know-how, if it **may be taxed** in the other state under a treaty (or, with no treaty, under the OECD Model, if the state is not blacklisted and the income is not Portuguese-source under art. 18) |
| E: dividends, interest, other capital income | Exempt, with progression | Exempt if it **may be taxed** in the other state under the treaty; with no treaty, under the OECD Model as read with Portugal's reservations, if the state is not blacklisted and the income is not Portuguese-source |
| F: rental income | Exempt, with progression | Same test as E |
| G: gains | Exempt, with progression | Same test as E |
| H: pensions | **Not exempt**. General rules (aggregation, treaty credit) | Kept the pre-2020 rules under Lei 2/2020 art. 329(2) (registered as NHR, or with a request pending, when that law took effect, or resident then and applied by 31 March 2020 for 2019 or 31 March 2021 for 2020; see the note below): exempt under the pre-2020 wording, unless the person opted into the 10% rate. Everyone else, including people resident after 31 March 2020: 10% on the net pension, if not Portuguese-source and only on the part that did not create a deduction under art. 25(2). Aggregation can be chosen instead (old art. 72(13)) |
| Any category paid by an entity in a listed privileged-tax jurisdiction | 35% (art. 81(5); IFICI FAQ 5500 gives UAE dividends as an example) | Not exempt under the no-treaty OECD Model route (old art. 81(5)(b)) for B, E, F and G. Where Portugal has a treaty with that state, the treaty route in old art. 81(5)(a) applies and has **no** blacklist condition, so the income can still be exempt if the treaty lets that state tax it |

Notes on the matrix:

- **The blacklist.** CIRS art. 81(5) points to the list of privileged-tax jurisdictions approved by portaria of the Finance Minister. That list is Portaria 150/2004 as amended; **check** the current version before relying on it, because the AT pages used here do not reproduce it.

- **"Exempt with progression"** means the exempt income is added in only to find the rate on the person's other aggregated income (art. 81(4) current; old art. 81(7)). The flat-rate and special-rate items that old art. 81(7) lists are left out of that rate calculation.
- **NHR credit option.** An NHR may choose the foreign tax credit method instead of exemption. The income is then aggregated and taxed, except items that keep their special rates ([NHR leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/IRS_RNH_PT.pdf); old art. 81(8)).
- **"May be taxed" versus "taxed".** For NHR category A the test is actual taxation in the other state. For B, E, F and G, it is enough that the treaty allows that state to tax. Where a treaty gives the residence state sole taxing rights (commonly gains on shares, and royalties under the OECD Model), the NHR exemption is not met; the income is taxed in Portugal under the general rules (for example 28% on the net balance of listed gains). Read the actual treaty; do not assume the OECD Model. ([CIRS art. 72](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx))
- **Pre-2020 pension exemption** ([art. 81 wording to March 2020](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs81ra_202003.aspx)): a foreign pension was exempt, as far as it had not created a deduction under art. 25(2), if it was taxed in the other state under a treaty, or if it was not Portuguese-source under art. 18(1). Lei 2/2020 art. 329 keeps this for people registered as NHR, or with a request pending, when that law came into force, and for people resident then who applied by 31 March 2020 (for 2019) or 31 March 2021 (for 2020). They could opt into the 10% rate in their 2020 return ([Lei 2/2020 art. 329](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/artigo329_oe2020.aspx)).
- **Crypto.** Gains on crypto assets held for 365 days or more are excluded from IRS under the general rules ([CIRS art. 10](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx)); neither regime changes this. For shorter holdings, decide the source before applying any exemption.
- **Foreign tax credit (general rules).** The credit is the lower of the foreign tax paid and the share of Portuguese tax on that income. With a treaty it cannot exceed the tax the treaty allows. Unused credit can be carried forward five years (CIRS art. 81(1) to (3)).

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Resident in Portugal in any of the five prior years | Neither regime | [EBF art. 58-A(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx) |
| Already an NHR, now in a job that would qualify for IFICI | Cannot switch or renounce NHR | [NHR FAQ 6011](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx) |
| Became resident in 2025, asks for NHR for 2024 | Rejected: not resident in 2024 | NHR FAQ 5153 |
| 2024 transitional NHR request filed in 2026 | Granted if eligible, but only from 2026 to 2033 | NHR FAQ 6010 |
| IFICI request filed after 15 January of the year after arrival | Applies from the year of filing, for the rest of the 10 years | EBF art. 58-A(7) |
| Contractor (services contract) to a certified startup or AICEP/IAPMEI-recognised company | Not eligible under (d) or (f): a "posto de trabalho" needs an employment contract | [IFICI FAQ 5502](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx) |
| University lecturer on a services contract | Eligible under (a) | IFICI FAQ 5501 |
| Shareholder of a qualifying company | Not eligible as shareholder; a sole-shareholder manager can qualify as a board member | IFICI FAQ 5503 |
| Qualifying job ends | Benefit continues only if a new qualifying activity starts within six months; report the change by 15 January of the next year and file a new request if the reviewing entity or company changes. The 10 years do not restart | EBF art. 58-A(4); FAQ 5515, 5516 |
| SIFIDE project (letter e) ends | Benefit stops unless new qualifying income starts within six months | IFICI FAQ 5522 |
| Leaves Portugal mid-period | Change the tax address to non-resident within 60 days (LGT art. 19(5)). NHR status is then suspended automatically and resumes on return for the years left; it is not extended | EBF art. 58-A(5); NHR FAQ 6006 and 6012 |
| Several qualifying activities reviewed by different entities | One request per activity | IFICI leaflet |
| Regressar (art. 12-A) chosen | IFICI excluded | EBF art. 58-A(10)(b) |
| IFICI ever used (from 2025) | IRS Jovem excluded | IFICI leaflet |
| Azores or Madeira resident | Letter (g) not yet regulated; can use letters (a) to (f) if met | IFICI FAQ 5499 |

## Worked cases

Amounts are hypothetical; personal deductions, social security and treaty credits are ignored.

**Case 1: IFICI engineer, 2026** ([EBF art. 58-A](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx); [CIRS art. 68](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx)). A software engineer (CPP 25, master's degree, five years' experience) moves to Porto in February 2026, not resident in the previous five years, never NHR. She is employed under an employment contract by a startup certified under Lei 21/2023, in an innovation role. She qualifies under letter (f) and must file with Startup Portugal via the Portal by 15 January 2027. Assume net 2026 category A income from the job of EUR 80,000.
- IFICI: EUR 80,000 at 20% = EUR 16,000. ([EBF art. 58-A(2)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx))
- General rules, for comparison: EUR 46,566 at the average rate of 26.472% gives EUR 12,326.95; the excess of EUR 33,434 at 44.60% gives EUR 14,911.56. Together, from unrounded parts, that is EUR 27,238.52. There is no solidarity rate, because taxable income is not over EUR 80,000. ([CIRS art. 68](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx))
- Difference before personal deductions: EUR 11,238.52 for 2026. ([CIRS art. 68](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx))
- If she gives her employer proof that the request was filed, it may withhold at 20%. ([IFICI leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/incentivos_investigacao.pdf))

**Case 2: IFICI beneficiary with foreign dividends, 2026** ([CIRS art. 81](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx); [IFICI FAQ 5500](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx)). The engineer in Case 1 also receives EUR 5,000 of dividends from a German company and EUR 2,000 from a company in the UAE.
- German dividends: category E obtained abroad, exempt under art. 81(4). They count only to set the rate on any other aggregated income. If she has none, that has no practical effect.
- UAE dividends: the UAE is on the privileged-tax list, so art. 81(5) applies: EUR 2,000 at 35% = EUR 700. ([CIRS art. 81(5)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx))

**Case 3: 2024 NHR transitional pensioner, late registration** ([art. 236 Lei 82/2023, under CIRS art. 81](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx); [NHR FAQ 6010](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx); [CIRS art. 72, wording to December 2023](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs72ra_202312.aspx)). A retiree signs a Portuguese lease on 1 September 2023, moves in September 2024 and becomes resident in 2024. He had not lived in Portugal before. He files the NHR request on 1 February 2026.
- Condition met: a lease concluded by 10 October 2023, and residence by 31 December 2024.
- The request is after 31 March 2025, so NHR runs from 2026 to 2033: eight years, not ten. 2024 and 2025 are taxed under the general rules.
- 2026: a foreign private pension of EUR 20,000 net, not Portuguese-source, that never created an art. 25(2) deduction. He became resident after 31 March 2020, so it is taxed at 10% = EUR 2,000 unless he chooses aggregation. ([old CIRS art. 72(12)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs72ra_202312.aspx))

**Case 4: late IFICI registration** ([IFICI leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/incentivos_investigacao.pdf)). A person becomes resident in 2025 and meets every IFICI condition, but files on 10 January 2029. IFICI applies from 2029 to 2034: six years. Had she filed by 15 January 2026, it would have run from 2025 to 2034.

**Case 5: remote worker, not a qualifying activity** ([CIRS art. 18](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs18.aspx)). A US citizen arrives in Lisbon in 2026 on a digital-nomad visa and keeps working from home for her US employer. The work is done in Portugal, so the salary is Portuguese-source under art. 18(1)(a). The foreign-income exemption does not apply to it. The employer is not an eligible IFICI entity, so she cannot use IFICI through this job, and the salary is taxed at the general rates. Treaty relief against US tax is a US question; refer.

## When to refuse or refer

- **Refuse** to apply NHR to anyone who became resident in 2025 or later, or to a 2024 arrival without an art. 236(3)(c) or (d) document meeting its date.
- **Refuse** to apply the IFICI flat rate before checking the activity against a specific letter of art. 58-A(1), the entity conditions and the qualifications. Where the reviewing entity (FCT, AICEP, IAPMEI, ANI, Startup Portugal) has not yet confirmed, label the result provisional.
- **Refuse** to treat a foreign pension as exempt under IFICI, or under NHR for a person who became resident after 31 March 2020 and did not keep the pre-2020 rules.
- **Refuse** to claim the NHR "may be taxed" exemption for a gain or royalty without reading the treaty article that applies.
- **Refer** when the case involves: disputed residence or dual residence under a treaty; a refused or pending registration (administrative objection and appeal deadlines are outside this Guide); trusts, foundations or blacklisted-jurisdiction structures; stock options; Regressar or IRS Jovem interaction; Azores or Madeira regional rules; US citizens (US tax applies on citizenship); penalties for late or wrong returns (not covered here, **check** the penalty rules separately).
- **Check** points this Guide could not confirm from an AT page: the full text of Portaria 352/2024/1 annexes as later amended, and whether any 2026 Budget change touched EBF art. 58-A. The AT's art. 58-A page shows no amendment since Lei 82/2023 as of 25 September 2026.

## Filing and payment ([CIRS art. 60](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx); [NHR leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/IRS_RNH_PT.pdf))

- **Annual return:** Modelo 3, filed online from 1 April to 30 June of the year after the income year, whether or not 30 June is a working day. The 2026 return is due between 1 April and 30 June 2027.
- **Annex L** is required for both regimes. It reports flat-rate income with its activity code (NHR) or the IFICI activity, the choice between the special rate and aggregation, and the method used for foreign income. Foreign income also goes on **Annex J**. For NHR pensions, Annex L asks whether the person was resident on or before 31 March 2020 and whether they opt for the 10% rate. ([NHR leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/IRS_RNH_PT.pdf))
- **Foreign tax credit not yet known:** where the credit amount is not fixed in the source state by 30 June, the deadline moves to 31 December of that year. The taxpayer must tell the AT within the normal deadline, naming the type of income and the source state (art. 60(3) and (4)).
- **Changes:** a return must also be filed within 30 days of any fact that changes income already declared (art. 60(2)). IFICI changes go to the Portal by 15 January of the following year.
- **2025 returns (filed in 2026):** the normal window closed on 30 June 2026. The extension to 31 December 2026 applies only where it was notified in time. A late 2025 return should be treated as a refer case for penalties.
- **Records:** IFICI beneficiaries keep evidence of the activity and income for every year; the employer keeps its records for 10 years (IFICI FAQ 5524). NHRs must prove the high-value activity on request.

## Completion checklist

- [ ] Residence year confirmed under CIRS art. 16, with the day count or the home evidence on file.
- [ ] No residence in the five prior years confirmed.
- [ ] No prior NHR, prior IFICI, or art. 12-A election (for IFICI).
- [ ] Regime chosen by arrival year, with the 2024 art. 236 document and its date checked where relevant.
- [ ] IFICI letter, entity, contract type and qualifications matched, and the reviewing entity identified.
- [ ] Registration filed by 15 January (IFICI) or 31 March 2025 (2024 NHR); if late, start year and end year recomputed.
- [ ] Each year: resident at some point, and qualifying income still earned (six-month gap rule).
- [ ] Source of each item decided under CIRS art. 18 before any exemption is applied.
- [ ] Foreign income classified by category, with blacklist and pension rules applied.
- [ ] Aggregation versus flat-rate choice reviewed and entered on Annex L.
- [ ] Modelo 3 with Annexes L and J filed between 1 April and 30 June; art. 60(3) extension notified if needed.

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
