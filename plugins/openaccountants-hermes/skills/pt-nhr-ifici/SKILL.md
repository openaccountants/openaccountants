---
name: pt-nhr-ifici
description: "Portugal's IFICI regime (EBF art. 58-A, often called NHR 2.0) and the old non-habitual resident (NHR) regime, for tax year 2026. Covers who qualifies for IFICI (not resident in the previous five years, the seven activity routes, Portaria 352/2024/1 professions and business codes, the reviewing bodies), registration by 15 January of the year after arrival, the 20% rate on qualifying Portuguese employment and business income for 10 years, the exemption of most foreign income (not pensions, 35% on income from listed low-tax jurisdictions), the NHR transitional rules (who could still enter in 2024, the 10% pension rate, the pre-2020 pension exemption), the IRS Jovem bar, Annex L, penalties. Trigger on: IFICI, NHR, RNH, residente não habitual, 20% flat rate Portugal, Portugal pension 10%, artigo 58.º-A EBF, Portaria 352/2024. Out of scope: pt-irs-employees-investment, pt-income-tax, pt-cross-border, pt-foreign-source-treaties, portugal-crypto-tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pt-nhr-ifici"
  jurisdiction: "PT"
  tax_year: "2026"
  last_updated: "2026-10-24"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Portugal: IFICI and the old NHR regime, for 2026

This skill covers two Portuguese personal income tax (IRS) regimes for people who move to Portugal. **IFICI** (incentivo fiscal à investigação científica e inovação) is in art. 58-A of the Tax Benefits Statute (EBF), added by the 2024 Budget Law (Lei 82/2023). It is open to people who become resident from 1 January 2024. **NHR** (residente não habitual, RNH) was revoked from 1 January 2024. It still runs for people already registered and for a closed transitional group (art. 236 Lei 82/2023). Portugal's tax year is the calendar year.

Sibling skills this one links to and does not repeat:

- `pt-irs-employees-investment`: the general 2026 IRS computation for employees, pensioners, capital income, rent and gains.
- `pt-income-tax`: self-employed (Category B) income, including IRS Jovem.
- `pt-cross-border`: residence, arriving and leaving, non-residents, exit charges.
- `pt-foreign-source-treaties`: foreign income of ordinary residents and the foreign tax credit.
- `portugal-crypto-tax`: crypto gains and the exit charge.

## Who this applies to

**IFICI.** A person qualifies if all of these hold ([EBF art. 58-A(1), (10) to (12)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx)):

- They become tax resident under CIRS art. 16(1) and (2). That means more than 183 days in Portugal (consecutive or not) in any 12-month period starting or ending in the year, or fewer days but a home there that suggests an intention to keep and occupy it as a habitual residence. A day counts if it includes a night spent in Portugal ([CIRS art. 16(1) and (2)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx)).
- They were **not resident in Portugal in any of the five previous years**. Nationality does not matter.
- They carry on an activity in one letter of art. 58-A(1), listed below.
- They have never been an NHR, never opted for the Regressar regime (CIRS art. 12-A), and never used IFICI before.

The pay must not be for jobs counted under CFI art. 22(2)(c) (art. 58-A(11)).

| Letter | Activity | Entity where it is done | Reviewed by |
|---|---|---|---|
| (a) | Higher-education teaching and scientific research, including scientific employment; jobs and board members in technology and innovation centres (DL 126-B/2021) | Higher-education institutions and bodies in the national science and technology system; technology and innovation centres | FCT |
| (b) | Qualified jobs and board members | Companies with contractual investment benefits (CFI chapter II) | AICEP |
| (c)(i) | Highly qualified professions in Portaria Annex I; also directors, managers and general managers | Companies with relevant investment that use, or used in the start year or the five prior years, the RFAI investment regime (CFI chapter III) | AT |
| (c)(ii) | Highly qualified professions in Portaria Annex I | Industrial and service companies whose main business code is in Portaria Annex II and that export at least 50% of turnover in the start year or either of the two prior years | AT |
| (d) | Qualified jobs listed in IAPMEI Notice 4812/2025/2 and AICEP Notice 5309/2025/2, and board members | Companies in activities AICEP or IAPMEI recognise as relevant to the economy | AICEP if the company's consolidated turnover in the prior year was EUR 75 million or more, or the project is PIN or PII; otherwise IAPMEI |
| (e) | R&D staff whose costs qualify for SIFIDE (CFI art. 37(1)(b)) | Companies using SIFIDE | ANI |
| (f) | Jobs and board members | Startups certified under Lei 21/2023 | Startup Portugal |
| (g) | Jobs or other activities of residents of the Azores and Madeira | To be set by regional decree | Regional governments |

Sources for the table: [EBF art. 58-A(1) and (6)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx); [Portaria 352/2024/1, art. 2(2) and 7](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_352_2024_1.pdf); [IFICI FAQ 5498 and 5525](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx).

- **Annex I professions** (Portuguese Classification of Occupations codes): 112 general and executive directors; 12 administrative and commercial directors; 13 production and specialised-services directors (except 1349); 21 physical, mathematical and engineering specialists (except 216); 2163.1 industrial product or equipment designer; 221 doctors; 231 university and higher-education teachers; 25 ICT specialists. The person needs a doctorate (EQF or ISCED level 8), or a degree (level 6) plus three years' proven experience. Regulated professions must also meet their own rules (Portaria art. 7(1), (2) and (4)).
- **Annex II business codes:** mining, divisions 05 to 09; manufacturing, divisions 10 to 33; information and communication, divisions 58 to 63; R&D in physical and natural sciences, group 721; higher education, subclass 85420; human health, subclasses 86100 to 86904 (Portaria art. 8). EU sales count towards the 50% export test (IFICI FAQ 5512).
- **Letter (d) jobs** are wider than Annex I: they add 14 hospitality, retail and other services directors, 241 finance and accounting specialists (except 2411), 2654 film, stage, TV and radio directors and producers, and 31 intermediate science and engineering technicians, plus company directors, managers and general managers; codes 13 and 21 carry no 1349 or 216 exclusion here. The person needs at least a post-secondary non-higher qualification (IFICI FAQ 5508 and 5498).
- **"Posto de trabalho" means an employment contract.** A contractor to a certified startup or a recognised company does not qualify under (a), (b), (d), (f) or (g) (IFICI FAQ 5502). A university lecturer on a services contract does qualify under (a) (FAQ 5501). A shareholder does not qualify as such; a sole-shareholder manager can, as a board member (FAQ 5503).
- **Azores and Madeira residents** can use letters (a) to (f) while letter (g) has no regional decree (FAQ 5499).
- **Early 2024 applicants.** A person who became resident in 2024 and applied before the Portaria was published (23 December 2024) keeps the Portaria 12/2010 list of activities for the whole period, while doing that activity (EBF art. 58-A(8); IFICI FAQ 5859).

**NHR, who is still in it in 2026.** The old rules (CIRS art. 16(8) to (12), 22, 72(10) and (12), 81(4) to (8), 99(8) and 101(1)(d), in their December 2023 wording) keep running to the end of the 10-year period for a person who ([art. 236(3) Lei 82/2023, reproduced under CIRS art. 81](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx)):

- (a) was registered as NHR on 1 January 2024; or
- (b) met the residence conditions on 31 December 2023; or
- (c) became resident by 31 December 2024 and declares one of the documents below; or
- (d) is a household member of a person in (a) to (c).

| Document for art. 236(3)(c) | Cut-off |
|---|---|
| Employment contract or promise, or secondment agreement or promise, for work in Portugal | concluded by 31 December 2023 |
| Lease or other contract giving use or possession of a property in Portugal | concluded by 10 October 2023 |
| Reservation or promissory contract to acquire a real right over a property in Portugal | concluded by 10 October 2023 |
| Enrolment of dependants in a school in Portugal | completed by 10 October 2023 |
| Residence visa or residence permit | valid by 31 December 2023 |
| Visa or residence-permit procedure, including a requested or booked appointment | started by 31 December 2023 |

A person who became resident in 2025 or later cannot enter NHR (NHR FAQ 5153). An NHR cannot renounce the status to switch to IFICI or IRS Jovem ([NHR FAQ 6011](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx)).

**Refer, do not compute:** disputed or dual residence under a treaty; a refused or pending registration (appeal deadlines are outside this skill); trusts, foundations and structures in listed low-tax jurisdictions; stock options; Regressar (art. 12-A); US citizens (the US taxes on citizenship).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| IFICI rate on net Category A and B income from the qualifying activity | 20%, or aggregation (englobamento) by choice | 2024 onward, 10 consecutive years from the year of registration as resident | EBF art. 58-A(2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx |
| IFICI withholding on qualifying monthly Category A pay | 20% | 2026 | CIRS art. 99(8): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99.aspx |
| IFICI withholding on qualifying Category B income | 20% | 2026 | CIRS art. 101(1)(d): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx |
| IFICI: foreign income of any category paid by an entity in a listed low-tax jurisdiction | 35% (final withholding where a Portuguese payer or agent is involved, otherwise autonomous rate) | 2026 | CIRS art. 81(5), 71(17)(b) and (c), 72(18): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx |
| Gap allowed between two qualifying activities | 6 months | 2026 | EBF art. 58-A(4) |
| Annex I qualification | Doctorate (level 8), or degree (level 6) plus 3 years' experience | 2026 | Portaria 352/2024/1, art. 7(2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_352_2024_1.pdf |
| Export test, letter (c)(ii) | at least 50% of turnover | 2026 | EBF art. 58-A(1)(c)(ii) |
| AICEP instead of IAPMEI, letter (d) | prior-year consolidated turnover EUR 75 million or more | 2026 | IFICI FAQ 5525: https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx |
| NHR rate on net Category A and B income from a listed high-value activity | 20% | Whole NHR period | Old CIRS art. 72(10): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs72ra_202312.aspx |
| NHR rate on net foreign pensions | 10%, or aggregation by choice | Whole NHR period, for NHRs not kept on the pre-2020 rules | Old CIRS art. 72(12) and (13): same URL |
| NHR withholding on high-value Category A and B income | 20% | Whole NHR period | Old CIRS art. 99(8) and 101(1)(d), kept by art. 236(3); NHR leaflet: https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/IRS_RNH_PT.pdf |
| General IRS bands, for comparison | 12.50% to 48.00% in nine bands (table below) | 2026 | CIRS art. 68(1), Lei 73-A/2025: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx |
| Solidarity surcharge | 2.5% on taxable income over EUR 80,000 to 250,000; 5% above | 2026 | CIRS art. 68-A: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx |
| Category A specific deduction | 8.54 x IAS = EUR 4,587.09, or compulsory social security if higher | 2026 | CIRS art. 25(1)(a) and (2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx |
| Category H (pension) specific deduction | Same EUR 4,587.09 per pensioner | 2026 | CIRS art. 53(1) and (2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs53.aspx |
| IAS | EUR 537.13 | 2026 | Portaria 480-A/2025/1: https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222 |

The 2026 general bands (CIRS art. 68(1)), needed for any comparison:

| Taxable income (EUR) | Marginal rate | Average rate on the whole band |
|---|---|---|
| up to 8,342 | 12.50% | 12.500% |
| over 8,342 to 12,587 | 15.70% | 13.579% |
| over 12,587 to 17,838 | 21.20% | 15.823% |
| over 17,838 to 23,089 | 24.10% | 17.705% |
| over 23,089 to 29,397 | 31.10% | 20.579% |
| over 29,397 to 43,090 | 34.90% | 25.130% |
| over 43,090 to 46,566 | 43.10% | 26.472% |
| over 46,566 to 86,634 | 44.60% | 34.856% |
| over 86,634 | 48.00% | n/a |

Income up to the top of the highest full band is taxed at that band's average rate; the excess at the next band's marginal rate (art. 68(2)). Lei 64-B/2026 of 22 October 2026 authorises the Government to cut the first six marginal rates for 2026 by decree-law; no decree had been published on 24 October 2026 (see Sources).

## The taxable base

**Portuguese-source income.** Under IFICI, only net Category A (employment) and B (self-employment) income from the qualifying activity gets the 20% rate. Under NHR the same applies to income from a listed high-value activity. Every other category (Portuguese rent, interest, gains, pensions) follows the general rules ([IFICI FAQ 5495](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx)). Net means after the category's specific deductions, for example employee social security or the EUR 4,587.09 minimum (CIRS art. 22(1) and 25). The person may aggregate instead, which only helps on low income.

**Source first.** Employment income is Portuguese-source if the work is done in Portugal, or if the pay is owed by a Portuguese resident or a Portuguese permanent establishment ([CIRS art. 18(1)(a)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs18.aspx)). A remote worker living in Lisbon and paid by a US employer has Portuguese-source salary. It is not foreign income under either regime. It gets 20% only if the job itself qualifies, and a foreign employer that is not an eligible entity does not qualify, so the salary is taxed at the general rates.

**Foreign income.**

| Income obtained abroad | IFICI ([CIRS art. 81(4) and (5)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx)) | NHR ([old art. 81(4), (5), (7)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs81ra_202312.aspx); old art. 72(12)) |
|---|---|---|
| A: employment | Exempt, with progression | Exempt if taxed in the other state under a treaty; with no treaty, if taxed there and not Portuguese-source under art. 18(1) |
| B: self-employment | Exempt, with progression | Exempt only for high-value scientific, artistic or technical services, intellectual or industrial property, or know-how, if the income **may be taxed** in the other state under a treaty; with no treaty, under the OECD Model as read with Portugal's reservations, if the state is not on the low-tax list and the income is not Portuguese-source |
| E: dividends, interest | Exempt, with progression | Same "may be taxed" test as B |
| F: rent | Exempt, with progression | Same test |
| G: gains | Exempt, with progression | Same test |
| H: pensions | **Not exempt**: general rules, with the treaty credit | 10% on the net pension, if not Portuguese-source and only the part that did not create an art. 25(2) deduction; aggregation by choice. Pre-2020 exemption for those kept on it (below) |
| Any category paid by an entity in a listed low-tax jurisdiction | 35% (art. 81(5)); IFICI FAQ 5500 gives UAE dividends as an example | For B, E, F and G the no-treaty route is closed for listed states; the treaty route has no list condition |

- **Progression.** Exempt income is added only to set the rate on the person's other aggregated income (art. 81(4); old art. 81(7)). Items taxed at special rates are left out of that calculation.
- **"May be taxed" versus "taxed".** For NHR Category A the test is actual tax in the other state. For B, E, F and G it is enough that the treaty lets that state tax. Where a treaty gives only the residence state the right to tax (often gains on shares), the NHR exemption fails and the general rules apply, for example 28% on the net balance of gains ([CIRS art. 72(1)(c)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx)). Read the treaty article that applies.
- **NHR credit option.** An NHR may choose the foreign tax credit instead of exemption. The income is then aggregated, except items that keep their special rates (old art. 81(8); NHR leaflet).
- **Pre-2020 NHR pension exemption.** Lei 2/2020 art. 329(2) keeps the old wording for people registered as NHR, or with a request pending, when that law came into force, and for people then resident who applied by 31 March 2020 (for 2019) or 31 March 2021 (for 2020). For them a foreign pension is exempt, to the extent it did not create an art. 25(2) deduction, if it is taxed in the other state under a treaty or is not Portuguese-source ([art. 81(6), wording to March 2020](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs81ra_202003.aspx)). They could opt into the new rules in their 2020 return (art. 329(3) to (5)).
- **General foreign tax credit.** The lower of the foreign tax and the share of Portuguese tax on that income, capped at the treaty rate; unused credit carries forward five years only where the year's tax was too small (CIRS art. 81(1) to (3)).
- **Crypto.** Gains on crypto held 365 days or more are excluded from IRS under the general rules ([CIRS art. 10](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx)); neither regime changes this. See `portugal-crypto-tax`.

**IRS Jovem.** A person who uses or has used IFICI or NHR, or opted for art. 12-A, cannot use IRS Jovem (CIRS art. 12-B(9)(a) to (c), wording of Lei 45-A/2024, from 2025) ([CIRS art. 12-B](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx); IFICI leaflet, note 6). For a young arrival the choice is one or the other. IRS Jovem is in `pt-income-tax`.

**The 10-year period.** Each year the person must be resident at some point and, for IFICI, still earn income from a qualifying activity. A new activity keeps the benefit if it starts within six months of the old one ending. Years lost to non-residence are not added at the end: the person resumes for the years left ([EBF art. 58-A(3) to (5)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx); old CIRS art. 16(11) and (12)). IFICI FAQ 5513: status from 2024, used to 2028, abroad in 2029, back in 2030: IFICI runs 2030 to 2033. A SIFIDE project that ends stops the benefit unless new qualifying income starts within six months (FAQ 5522).

**NHR activity lists.** For activities up to 31 December 2019, the original table in Portaria 12/2010 (codes 101 to 802). From 1 January 2020, the table in Portaria 12/2010 as amended by Portaria 230/2019 of 23 July: codes 112, 12, 13, 14, 21, 221, 2261, 231, 25, 264, 265, 31, 35, 61, 62, 7 and 8, with at least EQF level 4 or five years' proven experience, plus directors and managers of companies with CFI investment contracts. People registered, or with a request pending, on 1 January 2020, or who applied by 31 March 2020 for 2019, keep the old table but may choose the new one ([NHR leaflet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/IRS_RNH_PT.pdf)).

## Deadlines and filing

**Before registering.** The person needs a Portuguese tax number (NIF) and must be registered as resident; the IFICI request is addressed to "taxpayers registered as resident" ([Portaria 352/2024/1, art. 2(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_352_2024_1.pdf)).

| Became resident in | Regime | File the request by | Entities report to AT; letter (c) company confirms | AT shows status by |
|---|---|---|---|---|
| 2024 | IFICI | 31 March 2025 (Despacho 24/2025-XXIV, per the IFICI leaflet; the Portaria's own art. 12(1)(a) date was 15 March 2025) | 30 April 2025 (Portaria art. 12(1)(b): 15 April 2025) | 15 May 2025 (Portaria art. 12(1)(c): 30 April 2025) |
| 2024 | NHR (art. 236 group) | 31 March 2025; a later request runs from the year filed to the end of the 10th year from 2024 | n/a | n/a |
| 2025 | IFICI | 15 January 2026 | 15 February 2026 (IFICI FAQ 5858) | 31 March 2026 |
| 2026 | IFICI | **15 January 2027** | Entities: 15 February 2027 (art. 6(1)); company confirmation for letter (c): 15 March 2027 (art. 4(2)) | 31 March 2027 (art. 6(3)) |

- **Where.** On the Portal das Finanças, addressed to the reviewing body for the letter (Portaria art. 2(2) and 4(4)). One request per activity where different bodies review them. Documents: employment contract, commercial register certificate for a board member, research grant contract, proof of qualifications, the employer's statement for letters (b) to (e), and anything else asked for (art. 4(1) and 10(2)).
- **Late IFICI request.** IFICI then applies from the year of filing for the rest of the 10 years (EBF art. 58-A(7)). IFICI FAQ 5857: resident in 2025, filed 10 January 2029, IFICI runs 2029 to 2034.
- **Late NHR request (2024 group).** Granted from the year filed to the end of the 10th year from 2024 (art. 236(5); NHR FAQ 6008 and 6010: filed 1 February 2026, runs 2026 to 2033). While the register still shows the person as non-resident, the Portal will not accept an NHR request; raise it on e-balcão by 31 March (NHR FAQ 6007).
- **Changes.** Tell the reviewing body by 15 January of the following year when a condition stops being met or the details change, with the end date of the old activity; file a new request if the reviewing body or the company changes. The 10 years do not restart (Portaria art. 2(3) and 5; IFICI FAQ 5515 and 5516).
- **Withholding.** Give the payer proof that the request was filed to get 20% withholding. It is only a payment on account: if IFICI is refused, the general rates apply on assessment (IFICI FAQ 5517; IFICI leaflet).
- **Annual return.** Modelo 3, online, 1 April to 30 June of the following year, so 1 April to 30 June 2027 for 2026 ([CIRS art. 60(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx)). IFICI and NHR income goes on **Annex L** with the choice of rate or aggregation; foreign income also goes on Annex J (IFICI leaflet; NHR leaflet). For NHR pensions, Annex L records the pension option. Where a foreign tax credit is not yet fixed by 30 June, the deadline moves to 31 December; tell AT within the normal deadline (art. 60(3) and (4)). A return is also due within 30 days of a fact that changes income already declared (art. 60(2)).
- **Payment.** The balance is due by 31 August 2027 when AT assesses in the normal period ([CIRS art. 97(1)(a)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx)).
- **Records.** Keep proof of the activity and the income for every year and show it when AT asks (Portaria art. 10(3); CIRS art. 128). The employer keeps its records for 10 years (IFICI FAQ 5524).
- **Leaving.** Change the tax address to non-resident within 60 days (LGT art. 19(5)). NHR status is then suspended automatically and resumes on return for the years left (NHR FAQ 6006 and 6012).

## Penalties and interest

- **Late or missing return:** fine of EUR 150 to EUR 3,750 ([RGIT art. 116(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx)). No fine is imposed if, in the five previous years, the person had no final conviction for a tax offence and no waived or reduced fine; nor where there was no actual loss of revenue and the failure is put right ([RGIT art. 29](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit29.aspx)).
- **Missing or late documents, communications or information** that the law or AT requires: fine of EUR 150 to EUR 3,750 ([RGIT art. 117(1)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx)). Late or missing declarations of the end or change of the conditions for a tax benefit: EUR 300 to EUR 7,500 (RGIT art. 117(2)).
- **Withholding not handed over** by a payer: fine between the amount and twice the amount; if negligent, 15% to half the tax ([RGIT art. 114(1) and (2)](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx)).
- **Losing the regime.** A late IFICI request does not lose the regime, but loses the years before the year of filing (EBF art. 58-A(7)). A year without qualifying income (beyond the six-month gap) is a year without the 20% rate (art. 58-A(3)).
- **Compensatory interest (juros compensatórios):** where the taxpayer's fault delays the assessment, at the legal interest rate (LGT art. 35(10); Civil Code art. 559(1)), set at 4% a year by [Portaria 291/2003](https://diariodarepublica.pt/dr/detalhe/portaria/291-2003-223663) ([LGT art. 35](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx)).
- **Late payment interest (juros de mora):** from the payment deadline at the rate the IGCP sets each year: 7.221% from 1 January 2026 ([Aviso 18/2026/2](https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668); [LGT art. 44](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx)). A 2026 balance falls due in 2027, so the 2027 rate applies.

## Cross-border points

- **Arrival year.** A person becomes resident from the first day of presence, unless resident on any day of the previous year (CIRS art. 16(3)). The split year and the one-return-per-status rule are in `pt-cross-border`.
- **Listed low-tax jurisdictions.** The list in CIRS art. 81(5) is Portaria 150/2004 as amended, last by [Portaria 292/2025/1](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_292_2025_1.pdf), which removed Hong Kong, Liechtenstein and Uruguay with effect from 1 January 2026. For 2026, income from those three is not taxed at 35%; it falls under the normal IFICI exemption. The UAE stays on the list (IFICI FAQ 5500).
- **Treaties.** Under IFICI, exemption of A, B, E, F and G does not depend on a treaty. Under NHR it does (except the no-treaty OECD-Model route). For pensions under IFICI, use the general treaty credit in `pt-foreign-source-treaties`.
- **Foreign tax already withheld** on exempt IFICI income (for example German withholding on dividends) is not credited in Portugal, because the exemption method applies, not the credit method (CIRS art. 81(4)).
- **Leaving mid-period.** See "Leaving" above; the exit charges for leavers are in `pt-cross-border` and `portugal-crypto-tax`.
- **US citizens** stay taxable in the US on citizenship; Portuguese relief does not settle the US position. Refer.

## Worked examples

### Example 1: IFICI startup engineer with foreign dividends, 2026

Ana is a software engineer (Annex I code 25, master's degree, five years' experience). She moves to Porto in February 2026. She was not resident in Portugal in 2021 to 2025 and has never been NHR. She works under an employment contract for a startup certified under Lei 21/2023, in an innovation role, so she qualifies under letter (f), reviewed by Startup Portugal. She files on the Portal by 15 January 2027. Her 2026 gross salary is EUR 85,000. Her employee social security at 11% is EUR 9,350. She also receives EUR 5,000 of dividends from a German company and EUR 2,000 from a company in the UAE, paid to her directly with no Portuguese intermediary.

1. **Net Category A income.** Social security of EUR 9,350 is more than EUR 4,587.09, so the deduction is EUR 9,350 (art. 25(2)). Net = 85,000 - 9,350 = EUR 75,650.
2. **IFICI tax:** 20% x 75,650 = EUR 15,130.00 (EBF art. 58-A(2)). Net income is below EUR 80,000, so the solidarity surcharge question does not arise.
3. **German dividends:** Category E obtained abroad, exempt under art. 81(4). They count only to set the rate on other aggregated income; she has none.
4. **UAE dividends:** the UAE is a listed low-tax jurisdiction (IFICI FAQ 5500), so 35% x 2,000 = EUR 700.00 (art. 81(5) and 72(18)).
5. **Total IRS before personal deductions:** 15,130 + 700 = EUR 15,830.00.
6. **General rates, for comparison:** 46,566 x 26.472% + (75,650 - 46,566) x 44.60% = 12,326.95 + 12,971.46 = EUR 25,298.42. IFICI saves EUR 10,168.42 on the salary.

```oa-check
name: PT IFICI startup engineer, 20% vs 2026 bands, UAE dividends at 35%
inputs:
  gross_salary: 85000
  ss_rate: 0.11
  min_deduction: 4587.09
  ifici_rate: 0.20
  de_dividends: 5000
  uae_dividends: 2000
  listed_rate: 0.35
  band7_top: 46566
  band7_avg: 0.26472
  band8_rate: 0.446
steps:
  - ss: gross_salary * ss_rate
  - deduction: max(ss, min_deduction)
  - net_a: gross_salary - deduction
  - ifici_tax: net_a * ifici_rate
  - de_tax: de_dividends * 0
  - uae_tax: uae_dividends * listed_rate
  - total_ifici: ifici_tax + de_tax + uae_tax
  - general_salary_tax: round(band7_top * band7_avg + (net_a - band7_top) * band8_rate, 2)
  - saving: general_salary_tax - ifici_tax
expected:
  net_a: 75650
  ifici_tax: 15130.00
  uae_tax: 700.00
  total_ifici: 15830.00
  general_salary_tax: 25298.42
  saving: 10168.42
tolerance: 0.01
```

### Example 2: 2024 NHR pensioner who registered late

Peter signed a lease on a flat in the Algarve on 1 September 2023. He moved in September 2024 and became resident in 2024. He had never lived in Portugal before. He filed his NHR request on 1 February 2026. In 2026 he receives a private pension of EUR 25,000 from a foreign scheme. It is not Portuguese-source and never created an art. 25(2) deduction. He has no other income.

1. **Entry test.** A lease concluded by 10 October 2023, and residence by 31 December 2024: art. 236(3)(c)(ii) is met.
2. **Period.** The request came after 31 March 2025, so NHR runs from 2026, the year filed, to 2033, the 10th year from 2024: 8 years (art. 236(5); NHR FAQ 6010). 2024 and 2025 are taxed under the general rules.
3. **Pension regime.** He became resident long after Lei 2/2020, so the pre-2020 exemption is not available. The 10% rate applies (old art. 72(12)).
4. **Net pension:** 25,000 - 4,587.09 = EUR 20,412.91 (art. 53(2)).
5. **NHR tax:** 10% x 20,412.91 = EUR 2,041.29.
6. **Aggregation, for comparison:** 17,838 x 15.823% + (20,412.91 - 17,838) x 24.10% = 2,822.51 + 620.55 = EUR 3,443.06. He keeps the 10% rate, saving EUR 1,401.77. The tax deductions under art. 78 are left out of the comparison.

```oa-check
name: PT 2024 NHR transitional pensioner, late request, 10% vs 2026 bands
inputs:
  start_year: 2026
  end_year: 2033
  gross_pension: 25000
  pension_deduction: 4587.09
  nhr_pension_rate: 0.10
  band4_top: 17838
  band4_avg: 0.15823
  band5_rate: 0.241
steps:
  - years: end_year - start_year + 1
  - net_pension: gross_pension - pension_deduction
  - nhr_tax: round(net_pension * nhr_pension_rate, 2)
  - general_tax: round(band4_top * band4_avg + (net_pension - band4_top) * band5_rate, 2)
  - saving: general_tax - nhr_tax
expected:
  years: 8
  net_pension: 20412.91
  nhr_tax: 2041.29
  general_tax: 3443.06
  saving: 1401.77
tolerance: 0.01
```

## Ask the client first

1. **When did you become tax resident in Portugal, and were you resident at any time in the five years before?** The arrival year decides the regime; any residence in the look-back year rules both out.
2. **Have you ever been NHR, used IFICI, or opted for Regressar (art. 12-A)?** Any of these blocks IFICI; NHR or IFICI blocks IRS Jovem.
3. **What is your work in Portugal, under what contract, and who is the employer or client?** Employment contract, board seat, research grant or services contract; and what the entity is (university, certified startup, SIFIDE company, exporter with an Annex II code, AICEP or IAPMEI-recognised company). Bring your qualifications and years of experience.
4. **Have you filed the IFICI or NHR request, and when?** The filing date sets the first year; ask for the status shown on the Portal.
5. **What foreign income do you have, by type and paying country?** Pensions are taxed under IFICI; income from listed low-tax jurisdictions pays 35%.
6. **For NHR pensioners: were you registered, pending, or resident and applied in time when Lei 2/2020 came into force?** This decides exemption or 10%. For the 2024 group, which art. 236(3)(c) document do you hold, and its date.

## Sources

| Source | URL | Read on |
|---|---|---|
| EBF art. 58-A (IFICI), as added by Lei 82/2023; no later amendment shown | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx | 2026-10-24 |
| Portaria 352/2024/1 of 23 December 2024, as amended by Portaria 52-A/2025/1 (AT consolidated copy) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_352_2024_1.pdf | 2026-10-24 |
| AT FAQ, IFICI (5494 to 5526, 5857 to 5859) | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/pages/faqs-01018.aspx | 2026-10-24 |
| AT leaflet, IFICI (March 2025), incl. Despacho 24/2025-XXIV dates and the IRS Jovem note | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/incentivos_investigacao.pdf | 2026-10-24 |
| AT FAQ, NHR (5148, 5149, 5153, 6005 to 6012) | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/questoes_frequentes/Pages/faqs-00309.aspx | 2026-10-24 |
| AT leaflet, NHR and Annex L | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/Folhetos_informativos/Documents/IRS_RNH_PT.pdf | 2026-10-24 |
| CIRS art. 16 (residence), current and December 2023 wording | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx and https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs16bra_202312.aspx | 2026-10-24 |
| CIRS art. 81, current (incl. art. 236 Lei 82/2023), December 2023 and March 2020 wording | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs81ra_202312.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs81ra_202003.aspx | 2026-10-24 |
| CIRS art. 72, current (incl. Lei 2/2020 art. 329) and December 2023 wording | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx and https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs72ra_202312.aspx | 2026-10-24 |
| CIRS art. 71(17) (35% final withholding) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx | 2026-10-24 |
| CIRS art. 68 (2026 bands, Lei 73-A/2025) and 68-A | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx and https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx | 2026-10-24 |
| CIRS art. 10, 12-B, 18, 22, 25, 53, 60, 97, 99, 101 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx (same path for irs10, irs18, irs22, irs25, irs53, irs60, irs97, irs99, irs101) | 2026-10-24 |
| Portaria 480-A/2025/1, IAS 2026 EUR 537.13 | https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222 | 2026-10-24 |
| RGIT art. 29, 114, 116, 117 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx (same path for rgit29, rgit114, rgit117) | 2026-10-24 |
| LGT art. 35 and 44 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx and https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx | 2026-10-24 |
| Portaria 291/2003, legal interest 4% | https://diariodarepublica.pt/dr/detalhe/portaria/291-2003-223663 | 2026-10-24 |
| Aviso 18/2026/2 (IGCP), late payment interest 7.221% from 1 January 2026 | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-24 |
| Portaria 292/2025/1 of 5 September 2025, amending the low-tax list in Portaria 150/2004 (Hong Kong, Liechtenstein, Uruguay removed from 1 January 2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_292_2025_1.pdf | 2026-10-24 |
| Lei 64-B/2026 of 22 October 2026, authorisation to cut the first six 2026 IRS rates | https://diariodarepublica.pt/dr/detalhe/lei/64-b-2026-1184484177 | 2026-10-24 |

Not yet confirmed: the decree-law under Lei 64-B/2026 that would lower the 2026 bands used in the comparisons (none published by 24 October 2026); an official consolidated copy of the full low-tax list (Portaria 150/2004 with all amendments to Portaria 292/2025/1); whether the solidarity surcharge reaches income taxed at the IFICI 20% rate (art. 68-A charges "rendimento coletável", which art. 22(1) defines as aggregated income, and art. 22(3)(b) leaves out income taxed under arts. 71 and 72, but the IFICI rate sits in EBF art. 58-A and no AT guidance on the point was found); the original text of Despacho 24/2025-XXIV (taken from the AT leaflet); whether AT will publish different 2027 dates for 2026 arrivals than the Portaria's general dates; the exact day Lei 2/2020 came into force for the pre-2020 pension test; which RGIT fine AT applies to a missed IFICI change notice under Portaria art. 5; any regional decree for letter (g) in the Azores or Madeira.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pt-nhr-ifici` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pt-nhr-ifici. If neither is available, confirm every figure against the official source pages cited above before relying on it.
