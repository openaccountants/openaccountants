---
name: mx-imss
description: "Use this Mexico reference for voluntary IMSS cover under the Ley del Seguro Social in 2026: incorporation as a persona trabajadora independiente, continuación voluntaria, called Modalidad 40 in practice, and the Seguro de Salud para la Familia. Match requests about IMSS, seguro social Mexico, regimen voluntario, incorporacion voluntaria, IMSS freelancer, aseguramiento voluntario, Modalidad 40, voluntary IMSS enrollment, contribution calculation, benefits and tax deductibility for self-employed persons in Mexico. It ties each rate to its article and year, gives the UMA and minimum wage limits, separates INFONAVIT and SAR from IMSS, and holds every claim that these payments reduce income tax. This Tier 2 draft supports source checking and reviewer questions; it does not authorise filing, payment or a tax position."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mx-imss"
  jurisdiction: "MX"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# MX Imss v2.4
> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers voluntary cover at the Instituto Mexicano del Seguro Social (IMSS) for self-employed people and former employees, in Mexican pesos (MXN only). Tax year: calendar 2026. A year is stated beside every figure that changes.

The Ley del Seguro Social (LSS) Art 6 has 2 regimes: obligatorio and voluntario. Self-employed enrolment under Art 13 is voluntary entry into the obligatory regime. The Seguro de Salud para la Familia sits in the voluntary regime. Legacy versions used the label 'IVRO', and bank narrations may too, but no text read uses it. 'Modalidad 40' is the common name for Art 218 continuation: Art 218 itself says continuación voluntaria, and no text read uses that number.

| Route | Basis | Who | Cover |
| --- | --- | --- | --- |
| Persona trabajadora independiente (PTI) | LSS Art 13 fr I, Art 5 A fr XX, Arts 222 to 231; Reglas PTI, DOF 28-05-2024 | A natural person who is not subordinate and earns income from freely exercising a profession, trade or activity, not a salary. Art 5 A fr XX also lists ejidatarios, comuneros, colonos, pequeños propietarios, patrones with insured workers, and those who pay the cuotas of voluntary incorporation, except Art 13 fr V subjects | All 5 seguros: Enfermedades y Maternidad (in-kind cover subject to waiting times), Riesgos de Trabajo, Invalidez y Vida, Retiro, Cesantía en Edad Avanzada y Vejez (CEAV), Guarderías y Prestaciones Sociales (Art 222 fr II a)) |
| Continuación voluntaria, Modalidad 40 | LSS Arts 218 to 221; RACERF Arts 64 to 66, 128; Acuerdo of DOF 21-10-2026 | An insured with at least 52 weekly contributions credited in the obligatory regime in the last 5 years, on being given baja. From 22 October 2026 IMSS's temporary measures limit new enrolment and exclude anyone in PTI: see 'The base' | Invalidez y Vida and Retiro, CEAV only. No medical cover |
| Seguro de Salud para la Familia (SSF) | LSS Arts 240 to 245; RACERF Arts 95 to 107 | Families in Mexico. RACERF Art 95: people not subject to a compulsory regime in any social security system, and the insured person must insure at least 1 person from LSS Art 84 fr III to IX, without the cohabitation, dependency or study tests, or an additional relative: a grandparent, grandchild, sibling, cousin, niece, nephew, aunt or uncle (Art 96). IMSS may admit a person with no family alone, on a sworn declaration (Art 97) | In-kind Enfermedades y Maternidad only. No pension and no cash benefit |

The 5 seguros cover: medical care, prescriptions and maternity (Enfermedades y Maternidad); disability pension and death benefits (Invalidez y Vida); old-age pension and cesantía, which is unemployment at an advanced age (Retiro, CEAV); work accidents and occupational diseases (Riesgos de Trabajo); daycare and social services (Guarderías y Prestaciones Sociales).

Art 13 fr V public administration workers and any scheme older than the Reglas PTI are outside the figures below. Insured people in modalidad 44, 43 or 35 at the reform, and in the 2021 pilot, keep their terms until that cover ends, and may extend it under the new scheme with rights already acquired recognised (Reglas PTI 14 and 15; LSS decree DOF 01-12-2023, Transitorio Segundo). ISSSTE and employer-employee obligations are out of scope.

### What this file is

This is a Tier 2 source-cited draft. It has no accountant sign-off, and no accountant has reviewed this version. Treat every working it produces as a working paper only: an estimate for a reviewer, never an exact amount. IMSS's calculator and payment line, or a qualified contador público or social security specialist, settle the amount.

Mexican statutes were read in the Cámara de Diputados consolidated text through dated Internet Archive copies, because the Cámara site refused the connection, in a real browser too. IMSS pages were mostly read the same way because imss.gob.mx blocked direct requests and a real browser. DOF instruments were read directly at SIDOF, the official DOF mirror, because www.dof.gob.mx failed its certificate check. Each row says what it rests on.

**Operational hold.** `income-tax-workflow-base` says it must always be loaded with a country income tax skill that fills its Section 6 slots, and its Step 1 confirms that companion. This file is not that skill: it has no income tax rate schedule. `mx-income-tax` carries tax year 2025, is unconverted and does not declare this base. No conformance was tested in this conversion. Use this file as a reference only. Stop before producing a return, payment instruction, filing or tax position until a conforming Mexican income tax skill exists.

### Refusals and boundaries

A refusal is a full stop: give the message and classify nothing further.

- **R-MX-1, salaried employees.** Trigger: the person's only work is salaried employment, or the question is about contributions an employer owes. Message: 'The employer handles IMSS for salaried employment. This file covers self-employed and voluntary enrolment only. Stop.' It does not fire for an independent activity held alongside a job: LSS Art 224 lets a person who is both choose to affiliate as independent, paying separately. The employment side is still not computed here.
- **R-MX-2, employer-employee IMSS disputes.** Trigger: a dispute between an employer and IMSS about contributions or registrations. Message: 'Employer-employee IMSS disputes are outside this file. Escalate to a specialist.'
- **R-MX-3, disability claims.** Trigger: a claim for an IMSS disability benefit. Message: 'IMSS disability benefit claims require medical and legal evaluation. Escalate.'
- **R-MX-4, INFONAVIT complex cases.** Trigger: a question about how an INFONAVIT credit interacts with voluntary IMSS. Message: 'INFONAVIT credit interaction with voluntary IMSS is outside this file. Escalate.'

### Missing facts

| Missing fact | Action |
| --- | --- |
| Employment status | Stop until it is known. It decides R-MX-1 and the route |
| Prior weeks or baja date | Needs Input. Absence proves neither eligibility nor ineligibility for Art 218 |
| Art 218 enrolment date and contracted period | Needs Input. They decide whether the temporary measures under 'The base' apply |
| Income or base | Needs Input. Do not estimate on 1 UMA: it is below the Art 28 floor and is no base in law |
| Geographic area | Needs Input. It sets the minimum wage floor |
| Riesgos de Trabajo class | Needs Input for PTI. IMSS's system assigns it by occupation; the calculator's default is not a finding |
| Which date an amount falls on | Needs Input where UMA changes mid-period. IMSS's calculator fixes UMA, SM and the CEAV year by request date across the whole period, so check a multi-period payment separately |
| Tier 2 question threshold | MXN 0: no row is filtered on amount, as no Mexican floor was set |

### Rules for using this file

- Do not treat a route as open until its conditions are confirmed: the 52 contributions and the 5-year request window for Art 218, and for a request from 22 October 2026 the temporary measures under 'The base'.
- Do not treat the SSF as giving pension or disability cover. It is health only.
- Use the UMA where the law uses it as a unit, and the minimum wage (SM) where the law keeps it: the Art 28 floor and the 1.0 SM CEAV row. Legacy versions said never to use SM; that was wrong.
- Do not treat PTI rates as fixed: the CEAV employer rate changes each year in the table below.
- Do not advise on Modalidad 40 as a pension strategy without flagging a qualified adviser.
- Do not classify a person's own cuotas as business expenses or personal deductions until the hold under 'Income tax treatment' is cleared.

## Rates, bands and thresholds

Every statute link below is the Cámara de Diputados file. This draft read it through the dated archive listed in Sources, consolidated to the date given there. Rates are percentages for 2026 unless a row says otherwise. Under LSS Art 228 fr II, a PTI pays the whole cuota obrero-patronal; State shares are not charged.

| Item | Figure | Applies to | Source and limit |
| --- | --- | --- | --- |
| UMA 2026 | MXN 117.31 daily, 3,566.22 monthly, 42,794.64 annual | From 1 February 2026 | [INEGI UMA 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/uma/uma2026.pdf); DOF 09-01-2026. IMSS's calculator code uses it for requests from 1 January 2026, switching on the request date, not the covered month; that conflict is listed under Sources |
| UMA 2025 | MXN 113.14 daily, 3,439.46 monthly, 41,273.52 annual | From 1 February 2025 | [INEGI UMA 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/uma/uma2025.pdf) |
| Minimum wage 2026 | MXN 315.04 daily general area; MXN 440.87 Zona Libre de la Frontera Norte | From 1 January 2026 | [CONASAMI resolution, DOF 09-12-2025](https://sidof.segob.gob.mx/notas/5775534) |
| Base floor | SM of the geographic area, daily | All routes with a salary base | [LSS Art 28](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Base ceiling | 25 UMA daily: MXN 2,932.75 from 1 February 2026 | All routes with a salary base | same. Art 28 still prints 25 SM of the Distrito Federal. The [2016 decree](https://sidof.segob.gob.mx/notas/5423663), Transitorio Tercero, reads such mentions as UMA, and IMSS's calculator uses 25 UMA |
| Enfermedades y Maternidad, in kind, fixed | 20.40% of 1 UMA per day, not of income | PTI | same LSS file, Art 106 fr I with Décimo Noveno Transitorio of the 1995 Act: 13.9% plus 0.65 point a year from 1998 to 2007. IMSS calculator agrees |
| Enfermedades y Maternidad, in kind, excess | 1.10% employer plus 0.40% worker, 1.50% in all, of max(SBC - 3 UMA, 0) | PTI | same LSS file, Art 106 fr II with Décimo Noveno Transitorio; IMSS calculator agrees |
| Enfermedades y Maternidad, cash | 0.70% plus 0.25%, 0.95% in all, of SBC. Legacy 1.00% corrected: the other 0.05% is the Government's | PTI | same LSS file, Art 107 |
| Gastos médicos pensionados | 1.05% plus 0.375%, 1.425% in all, of SBC | PTI and Art 218 | same LSS file, Art 25 second paragraph; Art 218 b) for continuation |
| Riesgos de Trabajo | Prima media by class: I 0.54355%, II 1.13065%, III 2.59840%, IV 4.65325%, V 7.58875% of SBC | PTI | same LSS file, Art 73, read as an image at page 26. Reglas PTI 5.5: IMSS's system assigns the class by occupation |
| Invalidez y Vida | 1.75% plus 0.625%, 2.375% in all, of SBC | PTI and Art 218 | same LSS file, Art 147; Art 218 b) |
| Guarderías y Prestaciones Sociales | 1.00% of SBC | PTI | same LSS file, Arts 211 and 212 |
| Retiro | 2.00% of SBC | PTI and Art 218 | same LSS file, Art 168 fr I; Art 218 a). Set in the LSS, not the SAR law |
| CEAV | Employer rate in the next table plus 1.125% worker | PTI and Art 218 | same LSS file, Art 168 fr II a) and b); Art 218 a) |
| Art 218 total at 4.01 UMA and above | 13.347% for 2025, 14.438% for 2026: 2.000 + (employer rate + 1.125) + 2.375 + 1.425, where the CEAV term is 7.547% for 2025 and 8.638% for 2026 | Art 218 | same LSS file, Art 218 and the rows above; arithmetic checked |
| INFONAVIT, optional | 5% of reported income, if chosen, paid with the cuotas. Not IMSS: the housing law governs it | PTI | [Ley del INFONAVIT Art 59 Bis](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIFNVT.pdf) allows the contribution and Reglas PTI 12.1 has IMSS compute it on reported income. Art 29 fr II fixes 5% for employers only. The 5% for a PTI rests on IMSS's FAQ and calculator, which are administrative |

Employer CEAV rate by salario base de cotización (SBC), with the 2026 column in use for this tax year:

| SBC | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.0 SM | 3.150% | 3.150% | 3.150% | 3.150% | 3.150% | 3.150% | 3.150% | 3.150% | [LSS, decree DOF 16-12-2020, Transitorio Segundo, image at page 153](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| 1.01 SM to 1.50 UMA | 3.281% | 3.413% | 3.544% | 3.676% | 3.807% | 3.939% | 4.070% | 4.202% | same |
| 1.51 to 2.00 UMA | 3.575% | 4.000% | 4.426% | 4.851% | 5.276% | 5.701% | 6.126% | 6.552% | same |
| 2.01 to 2.50 UMA | 3.751% | 4.353% | 4.954% | 5.556% | 6.157% | 6.759% | 7.360% | 7.962% | same |
| 2.51 to 3.00 UMA | 3.869% | 4.588% | 5.307% | 6.026% | 6.745% | 7.464% | 8.183% | 8.902% | same |
| 3.01 to 3.50 UMA | 3.953% | 4.756% | 5.559% | 6.361% | 7.164% | 7.967% | 8.770% | 9.573% | same |
| 3.51 to 4.00 UMA | 4.016% | 4.882% | 5.747% | 6.613% | 7.479% | 8.345% | 9.211% | 10.077% | same |
| 4.01 UMA and above | 4.241% | 5.331% | 6.422% | 7.513% | 8.603% | 9.694% | 10.784% | 11.875% | same |

From 1 January 2021 to 31 December 2022 the employer rate was 3.150% flat. The graded table applies from 1 January 2023 (Transitorio Segundo). The printed bands leave gaps, such as 1.50 to 1.51 UMA; IMSS's calculator closes them by testing below the next row's start. Since SM exceeds 1.5 UMA in 2026, only an SBC exactly at SM gets 3.150%. An SBC just above SM in the general area (2.69 UMA) falls straight into the 2.51 to 3.00 row. In the northern border zone (3.76 UMA) it falls into the 3.51 to 4.00 row.

SSF annual quota per person, from 1 March 2026:

| Age group | Annual quota, MXN | Source and limit |
| --- | --- | --- |
| 0 to 19 | 9,300 | [IMSS SSF FAQ](http://www.imss.gob.mx/faq/seguro-familia), read in an archive of 26 September 2026. LSS Art 242 lets the Consejo Técnico set quotas by age group; the DOF instrument was not found, so these are IMSS's published figures |
| 20 to 29 | 11,550 | same |
| 30 to 39 | 12,350 | same |
| 40 to 49 | 14,350 | same |
| 50 to 59 | 14,850 | same |
| 60 to 69 | 20,600 | same |
| 70 to 79 | 21,500 | same |
| 80 and over | 22,150 | same |

Legacy age bands and percentages of the annual UMA had no source and are replaced. Quotas before 1 March 2026 are held.

## The base

**PTI.** The base is income actually reported from the activity, within the Art 28 limits (LSS Art 227 fr I; Reglas PTI 7.1). It is not a freely chosen multiple of the UMA. The in-kind Enfermedades y Maternidad cuotas follow Art 106, not this base (Art 227). IMSS's calculator divides monthly income by the days in the month, rounds to 2 decimals and holds the entry between days × SM and days × 25 UMA. What happens to a person whose real income is below the floor beyond that calculator rule is held.

```text
SBC = round(monthly income / days in month, 2)
Cuota for the period = days × [ 20.40% × UMA + 1.50% × max(SBC - 3 × UMA, 0) ]
                     + days × SBC × (0.95% + 1.425% + RT prima + 2.375% + 1.00% + 2.00% + CEAV employer rate + 1.125%)
INFONAVIT, if chosen = days × SBC × IMSS's administrative 5%, shown separately
```

The formula reads the calculator's components against the rows above. It deducts nothing, because no credit or earlier voluntary payment reduces a PTI cuota in the texts read. An AFORE voluntary contribution is outside it.

**Art 218.** The person must register on the last salary at baja or higher, at their choice, up to the Art 28 ceiling (RACERF Art 65). Art 218 sets the floor and Art 28 the ceiling; Art 218 does not state 25 UMA. If a legal rise in the area's SM passes the SBC, IMSS raises the SBC to that SM of its own motion (RACERF Art 65). A cuota is SBC × days × the Art 218 total, with the CEAV row chosen by that SBC. No housing contribution appears in Art 218. Whether Ley del INFONAVIT Art 59 Bis reaches a continuation is held.

**Art 218 temporary measures.** Acuerdo ACDO.AS2.HCT.101026/302.P.DG of IMSS's Consejo Técnico (DOF 21-10-2026), in force from 22 October 2026, sets these in point Cuarto. It is an IMSS measure: it names neither LSS Arts 218 to 220 nor RACERF Arts 65 and 66, and its point Tercero leaves changes to the normative provisions to a later proposal.

- Enrolled on its start date: stay on current conditions until the contracted period ends (point Cuarto), and keep the weeks and salaries actually paid (point Séptimo).
- Period ended, or a new applicant: may join from the request, on the last SBC registered at baja from the obligatory regime or up to that amount plus 1 UMA, never below 1 SM 'para el resto del país'. New enrolments start only on the request date. On that wording, a person now above the limit falls back to it when the period ends.
- In PTI, or entering it: cannot contract continuation.
- Duration: temporary, with no end date. It runs until the financial study in point Segundo, due within 6 months of 10 October 2026, reaches the Consejo Técnico, which then decides whether it continues.

Art 218 says 'último salario o superior', and RACERF Art 65 lets the person choose a higher salary up to the ceiling. Which text governs a new request is held. Give the reviewer the cuota on each reading, as in Example 3, and state neither as settled. This file reads the added UMA as the daily figure because the SBC is daily; the Acuerdo does not say so.

**SSF.** The cost is the sum of each person's age group quota, with no base.

**Days and UMA changes.** No text read sets a day count for an Art 218 month. Examples here use 30 days and name that as an input. The 30.4 in the 2016 decree is the multiplier for the monthly UMA, not a contribution rule. For periods before 1 February 2026 the law's UMA is the 2025 figure.

### INFONAVIT and SAR

INFONAVIT is governed by the Ley del INFONAVIT, not the LSS. The SAR, the retirement savings system, is run under the Ley de los Sistemas de Ahorro para el Retiro: AFOREs operate individual accounts subject to the social security laws (Art 18 fr I). The Retiro and CEAV rates are in LSS Art 168, and the person's choice of AFORE is in LSS Art 176. Voluntary contributions to the individual account come under LSS Art 192 and are not cuotas.

### Income tax treatment

Hold: enter no deduction for these payments until a reviewer names the limb. LISR Art 151 is a list, and no fraction names IMSS cuotas. The other fractions, II funerals, III donations, IV mortgage interest, VII school transport and VIII local salary tax, do not fit any row and are not repeated.

| Payment | Fr I medical fees and hospital costs | Fr V retirement accounts | Fr VI medical insurance premiums | Business deduction, LISR Art 103 fr VI | Result |
| --- | --- | --- | --- | --- | --- |
| PTI cuotas | Not a fee to a titled provider or a hospital bill | Not paid into a listed subaccount or plan | Held: the limb is for insurance complementary to or independent of public social security | Employer cuotas only; these are the person's own | IMSS's FAQ answers 'No.' to deductibility. That is administrative, and no SAT rule was searched in full. Legacy 'Yes' corrected to Needs Input |
| Art 218 cuotas | Not a medical payment | Held: paid to IMSS, not into the listed subaccounts | Not a medical premium | As above | Needs Input. Legacy already said not confirmed |
| SSF quotas | Held: annual quota, not a fee or a hospital bill | Not retirement | Held: the quota buys IMSS's own services | Not an employer cuota | Needs Input. Legacy 'Yes' removed; the IMSS FAQ read says nothing either way |
| Employer cuotas for the client's own workers | Not applicable | Not applicable | Not applicable | Deductible under fr VI subject to the Art 105 and 147 requirements; LISR Art 28 fr I keeps employer-borne IMSS deductible | Not a personal item. Keep apart from the client's own cuotas |
| INFONAVIT voluntary contribution | Not medical | Held: the subaccount is housing, not one fr V lists | Not a premium | Not an employer contribution | Needs Input |

AFORE voluntary contributions under fr V are not IMSS payments. The cap and conditions belong to `mx-income-tax`. The Art 151 overall cap does not apply to fr V.

Receipts: LISR Art 93 fr IV exempts an IMSS pension up to a daily cap, which it prints as 15 times the SM of the taxpayer's geographic area, and taxes the excess; fr V counts all pensions together. Legacy 'taxable' was too broad. The unit is unresolved, SM as printed or UMA under the 2016 decree's Transitorio Tercero, so the cap is Needs Input: compute neither as settled. Incapacity subsidies fall under Art 93 fr VIII, social security benefits from public institutions under fr VII, and work risk indemnities under fr III. The fr VIII previsión social limit in the later paragraph of Art 93 still needs a reviewer. A refund is Needs Input: find out what it is, either cuotas paid without legal basis (LSS Art 299) or a medical reimbursement (Art 93 fr VI), and treat any actualización on it separately.

### Bank narrations

These patterns are unsourced classifier hints, not law. Bank columns are not in any text read: confirm the file's own headers. Banks seen in earlier versions were BBVA Mexico, Banorte, Citibanamex, Santander Mexico, HSBC Mexico and Scotiabank Mexico, with columns such as Fecha, Descripcion or Concepto, Cargo, Retiro or Debito, Abono, Deposito or Credito, and Saldo.

| Narration | Meaning | Treatment |
| --- | --- | --- |
| IMSS REGIMEN VOLUNTARIO, IMSS IVRO | Person's own PTI or older voluntary cuotas | Keep out of business expenses. Deduction Needs Input |
| IMSS CUOTA OBRERO PATRONAL, IMSS CUOTA, IMSS PAGO, PAGO IMSS | Could be employer cuotas or the client's own, as the Reglas call PTI cuotas that too | Needs Input: ask if the client has workers |
| IMSS MODALIDAD 40, IMSS MOD 40 | Art 218 cuotas | Keep apart from PTI. Deduction Needs Input |
| IMSS SEGURO SALUD FAMILIA, IMSS SSF, SEGURO SALUD | SSF quota | Deduction Needs Input |
| INFONAVIT, INFONAVIT PAGO, PAGO INFONAVIT | Housing | Not IMSS. Separate programme |
| IMSS PENSION, PENSION IMSS, RETIRO IMSS | Pension receipt | Art 93 fr IV and V test above |
| IMSS INCAPACIDAD, SUBSIDIO IMSS | Incapacity subsidy | Art 93 test above |
| IMSS REEMBOLSO | Refund | Needs Input |

If a client gives a bank statement but cannot answer yet: identify the IMSS debits, keep Art 218 payments apart from PTI, assume eligibility for nothing, and ask the questions in 'Ask the client first'.

## Deadlines and filing

| Item | Rule | Source |
| --- | --- | --- |
| PTI enrolment | Self-service on the IMSS portal 'Personas Trabajadoras Independientes', or at the Subdelegación for the person's home address. Enrol and pay by day 20 of the month, and insurance starts on the first day of the month after payment. Payment receipt counts as the alta | Reglas PTI 5.1, 5.2, 5.4, 7.2. RACERF Art 77 allows any working day. Legacy 'any time' is qualified by this |
| PTI payment | In advance, monthly, bimonthly, half-yearly or yearly at the insured's choice, by day 20; if day 20 is a non-working day or a Friday, the next working day. Part payments carry no actualización or recargos | LSS Art 224; Reglas PTI 6.1, 7.1, 7.2. Legacy 'monthly' corrected. RACERF Art 115 fr II still prints actualización and recargos on later instalments; reformed Art 224 says none, and this row follows the Act |
| Mexicans abroad, PTI | Day 15 of the month, or the next working day if day 15 is non-working | Reglas PTI 9.3 |
| PTI renewal | RACERF Art 80 gives 30 days before expiry and 30 days after by authorisation; otherwise the next enrolment counts as initial for all legal purposes, so waiting times restart. Reglas PTI 5.3 u) makes automatic renewal optional. IMSS's FAQ says affiliation and payment are repeated each month | RACERF Art 80; Reglas PTI 5.3; IMSS PTI FAQ. Interaction held |
| Art 218 request | In writing, within 5 years of the baja date, or the right is lost. Point Quinto of the Acuerdo tells IMSS to move enrolment to digital means only; Trámite IMSS-02-007, which carries no date, still lists the online route and a Subdelegación counter, so confirm the route | LSS Art 219; Acuerdo of DOF 21-10-2026; Trámite IMSS-02-007 |
| Art 218 start | RACERF Art 66 lets the person choose the request date or the day after baja, and either way cover any unpaid cuotas. Point Cuarto of the Acuerdo starts new enrolments only on the request date. Conflict held | RACERF Art 66; Acuerdo of DOF 21-10-2026 |
| Art 218 payment | Monthly in advance, by day 17 of the month. Trámite IMSS-02-007 repeats day 17 but carries no date, and IMSS's current payment line was not read | LSS Art 218; RACERF Art 128 |
| Art 218 end | Signed declaration, 2 months unpaid, or re-registration under Art 12. After baja for 2 consecutive unpaid months, the person may ask in writing to re-enter within 12 months, on the salary at that baja or higher up to the ceiling, covering the cuotas from that baja to re-entry. Trámite IMSS-02-007 adds recargos on retroactive cuotas. Whether the Acuerdo reaches a re-entry is held | LSS Art 220; RACERF Art 65; Trámite IMSS-02-007 |
| SSF | Any working day, at the Subdelegación or online at https://serviciosdigitales.imss.gob.mx/portal-ciudadano-web-externo/home, paying the annual quota in advance; service starts on the first day of the next month; renew within 30 days before expiry. IMSS may authorise late renewal within 45 working days only where an illness arose in the period and needs continuity. Otherwise the next enrolment counts as initial for all legal purposes, so waiting times restart | RACERF Arts 101, 103, 105; LSS Art 242; Trámite IMSS-02-014 |
| SSF and PTI waiting times | In-kind cover waits: 6 months for a benign breast tumour, 10 months for childbirth, 1 year for the listed surgeries, 2 years for orthopaedic surgery. Art 83 has the list, and PTI is subject to it. Art 85's first paragraph disapplies Arts 81 to 83 for a voluntary incorporation into the obligatory regime requested within 12 months of baja, as insured or beneficiary, from the obligatory regime or the SSF, after 52 weeks insured. Its second paragraph does the same within 12 months of leaving a Decreto Presidencial scheme. Art 99 applies Art 85 to the SSF, but whether the first paragraph reaches an SSF entrant who is not in continuation is held. For individual SSF entry, Art 105 disapplies Arts 81 to 83 within 45 working days of leaving the obligatory regime or collective SSF, and states no minimum weeks. Art 85's third paragraph applies Arts 81 to 83 to a person in continuation who seeks voluntary incorporation or the SSF, unless the first paragraph fits. Reglas PTI 11.1 observes Art 85 for a PTI 'cuando resulte procedente' but excludes Arts 81, 82 and 84, so on a move from continuation to PTI the Art 83 waits apply unless the first paragraph fits, and whether Arts 81 and 82 also apply is held | RACERF Arts 83, 85, 99, 105; LSS Art 222 fr II a); Reglas PTI 11.1 |
| Exclusions | SSF: applicants undergo the exams IMSS sets (Art 98), and Arts 82 and 84 apply (Art 99). An applicant with a listed condition is refused unless the row above lifts Art 82 for that person, and the treatments listed in Art 84 are not covered: neither Art 85 nor Art 105 names Art 84. PTI: Reglas PTI 11.1 excludes Arts 81, 82 and 84, subject to the continuation hold in the row above | RACERF Arts 82, 84, 85, 98, 99, 105; Reglas PTI 11.1 |

No periodic IMSS return is required of a PTI in the texts read: reporting income and paying the línea de captura is the process. Payment is online or at a bank (IMSS FAQ). Use IMSS's calculator and the portal's payment line for the final figure. Income tax filing sits in `mx-income-tax`.

### Working paper

```text
MEXICO IMSS SELF-EMPLOYED WORKING PAPER (working paper only)
Client: ____________  CURP: ____________  NSS: ____________  RFC (optional): ____________  Date: ________

A. Status: employment status; enrolled in IMSS now, and which regime; prior weeks
   (semanas cotizadas); baja date and last salary
B. Route: PTI / Art 218 / SSF
C. Calculation: income or last salary; SBC; days; geographic area; RT class;
   CEAV row and year; period cuota; yearly cuota
D. Cover: health; disability and life; pension; work risk; childcare
E. Income tax: limb named by the reviewer, or Needs Input

REVIEWER FLAGS
[ ] Employment status confirmed, and R-MX-1 tested
[ ] Prior weeks verified: 52 in the last 5 years at baja
[ ] Request made within 5 years of baja; base at or above last salary
[ ] Art 218 enrolment date and period known, temporary measures tested, not in PTI
[ ] UMA and SM verified for each date in the period, not only the request date
[ ] CEAV row for the right year and SBC
[ ] Own cuotas kept apart from employer cuotas; no deduction entered without a named limb
```

## Penalties and interest

A PTI who does not pay on time is treated as giving baja (Reglas PTI 5.2), and cover ends. Reglas PTI 7.3, citing RACERF Art 87's last paragraph, says no payment is returned in whole or part 'bajo ningún supuesto', apart from RACERF Art 86: if invalidity or death comes after a renewal is paid but before the new period starts, the insured or family may choose its refund or credit for the period. Art 87's own paragraph covers only early termination. LSS Art 299 returns cuotas paid without legal basis, and whether rule 7.3 cuts that back is held, so pass any such claim to the reviewer and do not refuse it on rule 7.3 alone. Art 231 ends the voluntary incorporation by signed declaration or non-payment; RACERF Art 88 gives the individual and collective detail.

General LSS rules: cuotas, actualización, recargos and fines are crédito fiscal (Art 287); an employer's late cuotas carry actualización and recargos under the Código Fiscal (Art 40 A; CFF Arts 17-A and 21). IMSS's power to fix credits lapses 5 years after the aviso or liquidación, or after IMSS learned of the generating event; nothing interrupts that term, and only a recurso de inconformidad or a juicio suspends it (Art 297). The duty to pay cuotas and capitales constitutivos prescribes 5 years after it falls due, with completion and interruption under the CFF (Art 298): CFF Art 146 interrupts the term with each notified collection step or the debtor's express or tacit acknowledgement, and caps it at 10 years from when the credit could be demanded, not counting periods of suspension under that article. Cuotas paid without legal basis are returned, updated, if claimed within 5 years of payment, except Retiro and CEAV cuotas, which follow their own rules, and for other branches IMSS may deduct the cost of benefits given (Art 299). Whether non-payment by a voluntary insured creates a debt, or only ends cover, is held. So is whether the fines in Arts 304 A and 304 B reach them: those articles address the 'patrón o sujeto obligado'. The monthly recargo rate sits in the Ley de Ingresos, which was not read.

IMSS may check that PTI status is not hiding employment (Reglas PTI 13.1). Employer penalties are out of scope.

## Cross-border points

A Mexican abroad may enrol as a PTI through IMSS's system, with the day 15 limit above, and must register a domicile in Mexico; the cover operates in Mexico (Reglas PTI 9.1 to 9.3). A foreigner in Mexico may enrol as a PTI under Reglas PTI 10, also registering a domicile in Mexico, and the IMSS FAQ asks for legal stay, CURP and NSS. Mexican workers abroad may take the SSF for relatives in Mexico and for themselves when in Mexico, paying the whole quota (LSS Art 243; RACERF Art 107).

Social security agreements with other countries were not searched, so totalisation is held rather than ruled out. Where a client works in another country, Needs Input.

## Two worked examples that recompute

All examples use 2026 figures after 1 February, 30 days, the general area and no INFONAVIT unless stated. The class I prima is an input in each PTI case, not a finding about the person. Each is an estimate.

### Example 1: PTI at the minimum base

A self-employed designer with no prior IMSS cover has real monthly income of 30 × SM = MXN 9,451.20, the lowest entry IMSS's calculator accepts. SBC is 315.04, so excess over 3 UMA (351.93) is max(315.04 - 351.93, 0) = 0, and the 1.0 SM row gives 3.150%. Fixed in-kind cuota 717.94 plus 12.56855% of income 1,187.88 gives MXN 1,905.82. The legacy MXN 1,066 used 1 UMA as a base at about 31%, and both are wrong. The legacy 'for self and family' is dropped: family members reach PTI in-kind cover only as LSS Art 84 beneficiaries, as Example 2 shows, so no family cost is priced.

```oa-check
name: PTI at the Art 28 floor, June 2026, general area, class I
inputs:
  uma: 117.31
  sm: 315.04
  days: 30
  rt: 0.0054355
  ceav_employer: 0.0315
steps:
  - income: sm * days
  - sbc: round(income / days, 2)
  - excess: max(sbc - 3 * uma, 0)
  - fixed: 0.204 * uma * days
  - excess_cuota: 0.015 * excess * days
  - rest: income * (0.0095 + 0.01425 + rt + 0.02375 + 0.01 + 0.02 + ceav_employer + 0.01125)
  - total: fixed + excess_cuota + rest
expected:
  income: 9451.20
  excess: 0
  fixed: 717.94
  rest: 1187.88
  total: 1905.82
```

### Example 2: decision, PTI or SSF

A couple aged 35 and 33, neither subject to a compulsory regime. One earns MXN 30,000 a month as a freelancer. Should they take PTI or the SSF?

PTI: SBC 1,000.00, which is 8.52 UMA, so the 4.01 UMA row gives 7.513%. Excess is max(1,000.00 - 351.93, 0) = 648.07. Fixed cuota 717.94, excess cuota 291.63 and 16.93155% of income 5,079.47 give MXN 6,089.03 for the month, about 20.3% of income. INFONAVIT, if chosen, would add MXN 1,500.00 at IMSS's administrative 5%.

SSF: 2 × 12,350 = MXN 24,700 a year, or MXN 2,058.33 a month. PTI in-kind cover reaches the spouse only as an LSS Art 84 fr III beneficiary who meets that article's dependency test, which RACERF Art 95 waives for the SSF; confirm that before comparing. The figure that decides on cost alone is the gap of MXN 4,030.70 a month.

Decide in this order. First, the cover: if either adult needs pension weeks, work risk cover or cash sickness benefit, the SSF does not provide them, so PTI is the route for that person. Second, entry to the SSF: a condition listed in RACERF Art 82 bars an applicant unless it is lifted. Art 105 lifts it on individual entry within 45 working days of leaving the obligatory regime or collective SSF, and Art 85 may too, as held under 'SSF and PTI waiting times'. So get each adult's last baja date and weeks before ruling the SSF out. Third, the spouse under PTI: Reglas PTI 11.1 excludes Art 82, but in-kind cover for the spouse still needs the LSS Art 84 test, and a spouse who fails it needs their own PTI enrolment, if eligible, at a cost not worked here. Only where both adults can enter the SSF and PTI would cover both does the SSF, for in-kind health cover alone, cost MXN 4,030.70 a month less. Neither outcome is a recommendation: flag retirement impact for a reviewer.

```oa-check
name: PTI against SSF, couple 35 and 33, income 30,000, June 2026
inputs:
  uma: 117.31
  income: 30000
  days: 30
  rt: 0.0054355
  ceav_employer: 0.07513
  ssf_quota: 12350
steps:
  - sbc: round(income / days, 2)
  - excess: max(sbc - 3 * uma, 0)
  - fixed: 0.204 * uma * days
  - excess_cuota: 0.015 * excess * days
  - rest: income * (0.0095 + 0.01425 + rt + 0.02375 + 0.01 + 0.02 + ceav_employer + 0.01125)
  - pti: fixed + excess_cuota + rest
  - ssf_month: 2 * ssf_quota / 12
  - gap: pti - ssf_month
expected:
  excess: 648.07
  excess_cuota: 291.63
  rest: 5079.47
  pti: 6089.03
  ssf_month: 2058.33
  gap: 4030.70
```

### Example 3: Modalidad 40 at 10 UMA

A former employee was given baja 2 years before enrolling, on MXN 800 a day, with 200 weeks in all, of which 60 are in the 5 years before baja. Art 218 is open, and the written request is within Art 219's 5 years. A total of 200 weeks would not be enough alone: if fewer than 52 sat in the 5-year window, the right would not arise. The client enrolled before 22 October 2026 on 10 UMA, MXN 1,173.10 a day, which is at or above the last salary and falls in the 4.01 UMA row, and elected the request date as the start under RACERF Art 66. 30 days × 1,173.10 × 14.438% = MXN 5,081.17. Electing the day after baja would have added the unpaid cuotas for those 2 years, not costed here. This buys pension and disability cover only, so the client needs separate health cover. RACERF Art 85's third paragraph applies Arts 81 to 83 to entry into the SSF unless its first paragraph fits; for PTI, see the hold under 'SSF and PTI waiting times'.

The same client asking from 22 October 2026 meets the temporary measures: a base of up to 800 + 117.31 = MXN 917.31 a day, still in the 4.01 UMA row, and a start on the request date. 30 days × 917.31 × 14.438% = MXN 3,973.24. Art 218 and RACERF Art 65 would still allow 10 UMA. Which governs is held, so show the reviewer both.

```oa-check
name: Art 218 at 10 UMA, June 2026
inputs:
  uma: 117.31
  multiple: 10
  days: 30
  rate: 0.14438
  last_salary: 800
steps:
  - daily: uma * multiple
  - cuota: daily * days * rate
  - acuerdo_limit: last_salary + uma
  - acuerdo_cuota: acuerdo_limit * days * rate
expected:
  daily: 1173.10
  cuota: 5081.17
  acuerdo_limit: 917.31
  acuerdo_cuota: 3973.24
```

### Example 4: Modalidad 40 at the ceiling

A client with 500 weeks, at least 52 of them in the 5 years before a baja less than 5 years before the request, enrolled before 22 October 2026 on 25 UMA, MXN 2,932.75 a day. Over 30 days, 30 × 2,932.75 × 14.438% = MXN 12,702.91. This is a maximum pension strategy, so flag a reviewer for long-term pension impact. Under the temporary measures a request from 22 October 2026 reaches 25 UMA only with a last SBC at baja of at least 24 UMA, MXN 2,815.44; that limit is held as in Example 3.

```oa-check
name: Art 218 at the 25 UMA ceiling, June 2026
inputs:
  uma: 117.31
  multiple: 25
  days: 30
  rate: 0.14438
steps:
  - daily: uma * multiple
  - cuota: daily * days * rate
  - last_needed: daily - uma
expected:
  daily: 2932.75
  cuota: 12702.91
  last_needed: 2815.44
```

### Example 5: SSF for a family of 4

Adults aged 35 and 33 and children aged 8 and 5, none subject to a compulsory regime in any social security system, enrolling after 1 March 2026. 2 × 12,350 + 2 × 9,300 = MXN 43,300 a year, paid in advance. Health only: no pension.

```oa-check
name: SSF family of 4, after 1 March 2026
inputs:
  adults: 2
  children: 2
  quota_30_39: 12350
  quota_0_19: 9300
steps:
  - total: adults * quota_30_39 + children * quota_0_19
expected:
  total: 43300
```

## Ask the client first

1. Are you only self-employed, also employed part-time, or only employed? Do you have workers of your own? Are you enrolled in any IMSS regime now, and which?
2. What are your CURP, NSS and, optionally, RFC, and in which municipality do you live (general area or northern border zone)?
3. For Modalidad 40: how many weeks have you contributed, how many fall in the 5 years before your baja, when was your baja, what was your last salary, and are you already enrolled, since when and for what period?
4. What is your real monthly income from the activity, your occupation, and which period will you pay for?
5. Which family members do you want to cover (spouse, children, parents), with their ages? Does any of them depend on you financially, have a condition in RACERF Art 82, or fall under a compulsory regime in any social security system? When did each adult last leave IMSS cover, in which regime and with how many weeks?
6. Do you want health cover, pension cover or both, do you want INFONAVIT contributions, and do you hold an INFONAVIT credit or work in another country?

Also useful, not required: a full IMSS contribution statement, the prior year ISR return and INFONAVIT status.

Reviewer questions: PTI or SSF, as in Example 2. A higher reported income costs more but raises benefits, and the base must still be real income. Art 218 at a high base needs a qualified pension projection. The Acuerdo of DOF 21-10-2026 bars continuation for anyone in PTI or entering it, so do not plan the 2 together while that hold stands. If a former employee left over 5 years ago without contributions, the Art 218 right is lost (Art 219), but PTI and the SSF remain open, not PTI alone as the legacy file said. Recognition of old weeks on re-entry is under LSS Art 151 and sits with that projection, which needs actuarial analysis.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Ley del Seguro Social, Cámara consolidated text, última reforma DOF 15-01-2026. Archived copy of 16 October 2026; Cámara site refused the connection. Read: Arts 5 A, 6, 11, 13, 25, 28, 39, 40 A, 71 to 73, 84, 106, 107, 147, 150, 151, 154, 162, 167, 168, 174, 176, 192, 211, 212, 218 to 231, 240 to 245, 251 fr XIV, 287, 297 to 299, 304 A to 304 C and the 1995, 2020 and 2023 transitorios | https://web.archive.org/web/20261016034936id_/https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf | 2026-11-05 |
| Cámara reform list for the LSS, archived 19 October 2026, last entries read: DOF 15-01-2026 is the latest | https://web.archive.org/web/20261019192221id_/http://www.diputados.gob.mx/LeyesBiblio/ref/lss.htm | 2026-11-05 |
| Ley del Impuesto sobre la Renta, Cámara text, DOF 01-04-2024. Archived copy of 24 October 2026. Read: Arts 28 fr I, 93 fr I to X with the previsión social limit paragraph, 103, 151 and the opening of 105 and 147 | https://web.archive.org/web/20261024180718id_/https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-11-05 |
| Ley del INFONAVIT, Cámara text, DOF 21-02-2025. Archived copy of 5 January 2026. Read: Arts 29 fr II, 59, 59 Bis | https://web.archive.org/web/20260105062809id_/https://www.diputados.gob.mx/LeyesBiblio/pdf/LIFNVT.pdf | 2026-11-05 |
| Ley de los Sistemas de Ahorro para el Retiro, Cámara text, DOF 14-11-2025. Archived copy of 14 October 2026. Read: Art 18 fr I only | https://web.archive.org/web/20261014104312id_/https://www.diputados.gob.mx/LeyesBiblio/pdf/LSAR.pdf | 2026-11-05 |
| Reglamento de la LSS en materia de Afiliación, Clasificación de Empresas, Recaudación y Fiscalización (RACERF), Cámara text, DOF 15-07-2005. Archived copy of 2 August 2025, no 2026 capture used. Read: Arts 64 to 66, 75 to 88, 95 to 107, 115, 128 | https://web.archive.org/web/20250802160347id_/https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LSS_MACERF.pdf | 2026-11-05 |
| Cámara list of federal regulations, header date 24 September 2026, archived 7 October 2026. RACERF row read: last reform DOF 15/07/2005 | https://web.archive.org/web/20261007092326id_/https://www.diputados.gob.mx/LeyesBiblio/regla.htm | 2026-11-05 |
| Código Fiscal de la Federación, Cámara text, DOF 09-04-2026. Archived copy of 6 October 2026. Read: Arts 17-A and 21, opening paragraphs, and 146 | https://web.archive.org/web/20261006134049id_/https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | 2026-11-05 |
| Reglas PTI, Acuerdo ACDO.AS2.HCT.300424/82.P.DIR, DOF 28-05-2024, read in full | https://sidof.segob.gob.mx/notas/5728817 | 2026-11-05 |
| Acuerdo ACDO.AS2.HCT.101026/302.P.DG, temporary measures for continuación voluntaria, DOF 21-10-2026, read in full | https://sidof.segob.gob.mx/notas/5801708 | 2026-11-05 |
| DOF daily indexes at SIDOF, 25 September to 4 November 2026, titles only, the URL shown being 1 of the 29 days: no later title names continuation, the LSS or RACERF | https://sidof.segob.gob.mx/welcome/21-10-2026 | 2026-11-05 |
| Decree on the desindexación of the minimum wage, DOF 27-01-2016, transitorios read | https://sidof.segob.gob.mx/notas/5423663 | 2026-11-05 |
| UMA 2026 notice, DOF 09-01-2026, read in full | https://sidof.segob.gob.mx/notas/5778072 | 2026-11-05 |
| CONASAMI 2026 minimum wage resolution, DOF 09-12-2025, operative figures read | https://sidof.segob.gob.mx/notas/5775534 | 2026-11-05 |
| INEGI UMA 2026 bulletin, Comunicado 1/26, read in full | https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/uma/uma2026.pdf | 2026-11-05 |
| INEGI UMA 2025 bulletin, read in full | https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/uma/uma2025.pdf | 2026-11-05 |
| IMSS PTI calculator script, archived 11 October 2026, cuota functions and date logic read, not run. Administrative, not law | https://web.archive.org/web/20261011193110id_/https://www.imss.gob.mx/sites/all/statics/trabajadores-independientes/calculadoraPTI-0326.js | 2026-11-05 |
| IMSS PTI calculator page, archived 11 October 2026, read for the input limits. Administrative, not law | https://web.archive.org/web/20261011193044id_/https://www.imss.gob.mx/personas-trabajadoras-independientes/calculadora | 2026-11-05 |
| IMSS PTI landing page, archived 13 October 2026, read for the portal name | https://web.archive.org/web/20261013024325id_/https://www.imss.gob.mx/personas-trabajadoras-independientes | 2026-11-05 |
| IMSS PTI FAQ, archived 18 June 2026, read in full. Administrative, not law; it mentions the retired INSABI | https://web.archive.org/web/20260618141145id_/https://www.imss.gob.mx/personas-trabajadoras-independientes/preguntas | 2026-11-05 |
| IMSS SSF FAQ, archived 26 September 2026, read in full. Administrative, not law | https://web.archive.org/web/20260926145202id_/http://www.imss.gob.mx/faq/seguro-familia | 2026-11-05 |
| IMSS Trámite IMSS-02-014, SSF incorporation, archived 19 October 2026, read in part | https://web.archive.org/web/20261019161221id_/http://www.imss.gob.mx/tramites/imss02014 | 2026-11-05 |
| Trámite IMSS-02-007, continuation enrolment, federal trámite catalogue, live page with no date, read in full. It still prints the RACERF Art 66 choice, so it does not show practice under the Acuerdo. Administrative, not law | https://www.gob.mx/public/tramites/detalleTramite.xhtml?homoclave=IMSS-02-007 | 2026-11-05 |

Not yet confirmed: the DOF instrument for the current SSF quotas and any earlier SSF quota; the IMSS calculator, which switches UMA, SM and CEAV year on the request date from 1 January, not the covered month, against the February UMA start in law, read in the script and not run; an LSS or RACERF reform that the Cámara lists and the DOF title scan would miss; which text governs a new Art 218 request, the Acuerdo of DOF 21-10-2026 or LSS Art 218 with RACERF Arts 65 and 66; how IMSS's system applies that Acuerdo, what 'periodo contratado' means, whether its added UMA is the daily figure, how its 'resto del país' SM floor works in the border zone, whether it reaches an Art 220 re-entry and when it ends; whether a court has ruled on it; whether IMSS's current payment line uses day 17; the Art 218 day count; what follows for a PTI whose real income is below the floor; whether RACERF Art 85's third paragraph or Reglas PTI 11.1 governs Arts 81 and 82 on a move from continuation to PTI; whether Art 85's first paragraph reaches an SSF entrant who is not in continuation; whether Reglas PTI 7.3 cuts back a claim under LSS Art 299; whether the Art 93 fr IV cap reads as SM or UMA; the fr VIII previsión social limit; any SAT rule on deducting PTI cuotas, Art 218 cuotas, SSF quotas or INFONAVIT voluntary contributions; the 5% INFONAVIT rate for a PTI in a legal text; whether Art 59 Bis reaches Art 218; whether Arts 304 A and 304 B or a debt reach a voluntary insured; PTI renewal under RACERF Art 80 against the Reglas and the IMSS FAQ; social security agreements with other countries; the monthly recargo rate; the name Modalidad 40 in any IMSS text read here; the Ley UMA itself, whose DOF body failed to download, so the UMA rule was read in the 2016 decree and the DOF and INEGI notices instead; `mx-income-tax`, which treats voluntary IMSS as a personal deduction, against the hold here; `mx-estimated-tax`, which excludes IMSS cuotas, and `mexico-iva`, which excludes IMSS and INFONAVIT, although employer cuotas for a client's own workers are deductible under LISR Art 103 fr VI, the VAT exclusion itself not being tested.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | 2026-11-05 | Converted to the upstream template for 2026. Corrected the PTI rates, base and example, the deduction claims, the SSF quotas, the Art 218 tests and the minimum wage rule. Added the RACERF rules for Art 218 and held the temporary measures of DOF 21-10-2026. |
| 2.1 | 2026-11-01 | Legacy version for 2025. |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; bank statement patterns; worked examples. |
| 1.0 | 2025 | Initial version. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador público, social security specialist, or equivalent licensed practitioner in Mexico) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mx-imss` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mx-imss. If neither is available, confirm every figure against the official source pages cited above before relying on it.
