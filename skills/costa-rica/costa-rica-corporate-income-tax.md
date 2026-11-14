---
name: costa-rica-corporate-income-tax
description: >
  Costa Rica corporate income tax (impuesto sobre las utilidades) source
  reference for ordinary domiciled companies (sociedad anónima, sociedad de
  responsabilidad limitada) for fiscal period 2026. Covers territorial scope,
  the 30% rate, the small-company scale and its gross-income cliff, the
  Mipyme reduction, the base, loss carry-forward, partial payments, the
  TRIBU-CR form 102 return, payment and penalties. Trigger on Costa Rica
  company tax, impuesto sobre las utilidades, persona jurídica, pagos
  parciales, D-101, formulario 102 or TRIBU-CR. Includes recomputing
  fictional cases and explicit source holds. This Tier 2 draft awaits
  professional review and does not establish filing readiness.
jurisdiction: CR
category: international
tax_year: 2026
tax_year_notes: "Fiscal period 1 January to 31 December 2026 (Ley 7092 art. 4); return due by 15 March 2027. Selected source reading on 2 November 2026."
tier: 2
last_updated: 2026-11-03
version: 0.1
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Costa Rica Corporate Income Tax Reference: Ordinary Domiciled Companies, 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This draft helps a Costa Rican professional reviewer apply selected impuesto sobre las utilidades rules to an ordinary domiciled sociedad anónima (SA) or sociedad de responsabilidad limitada (SRL) for fiscal period 2026. Load both declared bases before actual work; their intake, refusal messages, computation sequence, outputs and checks apply in full.

**General source reference, not an engagement calculation.** It does not establish comprehensive Costa Rican corporate coverage or filing readiness. No actual classification, computation or return may rely on a rule this file lists as held.

- **Who is taxed.** Legally constituted personas jurídicas are contribuyentes whether or not they carry on a lucrative activity; inactive companies file only a summary information return. [S1, art. 2 a)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
- **What is taxed.** Profits from lucrative activities of Costa Rican source, meaning income generated exclusively in the national territory from services rendered, property situated, capital invested and rights used there, whatever the nationality, domicile or residence of the parties. [S1, art. 1](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
- **Exception to territoriality.** Foreign-source dividends, interest, royalties, capital gains and other capital income are taxed when received by a member of a multinational group that is not a 'qualified entity' under arts. 2 bis to 2 quinquies (Ley 10381 of 14 September 2023). This file does not qualify those tests; any such income is a hold. [S1, arts. 1 and 2 bis to 2 quinquies](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
- **Period.** 1 January to 31 December; the Administration may set other periods by branch of activity. Each period is settled independently. [S1, art. 4](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
- **Outside this file.** Non-subject entities in art. 3, including free-zone companies under Ley 7210, cooperatives and public-works trusts; financial entities supervised under Conassif; permanent establishments of non-domiciled entities (art. 2 b)); the simplified regime; transfer pricing (art. 81 bis and Decreto 37898-H, kept in force by Ley 9635 Transitorio XXI); capital income taxed under chapter XI; and remittance withholding, which [costa-rica-income-tax](costa-rica-income-tax.md) covers. [S1, arts. 2, 3](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1); [S8, Transitorio XXI](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=87720&param2=150648&param3=1)

### Source currency

S1 is the consolidated Ley 7092, version 83 of 83 on SINALEVI, read on 2 November 2026. Its 2026 small-company figures were inserted by Decreto 45333-H of 10 November 2025, which applies from 1 January 2026 and repeals the 2025 figures of Decreto 44772-H (S4, S5). The regulation, Decreto 43198-H (S7), still prints superseded figures in its art. 23 (a ₡106,000,000 threshold and a three-year 100%, 75% and 50% reduction); the law as amended by Ley 10392 and Decreto 45333-H prevails, so do not use those regulation figures.

## Ask the client first

Complete the corporate base intake first. These Costa Rican additions change the answer:

| Fact | Why it matters |
| --- | --- |
| Entity type, domicile and art. 3 status | Decides whether this file applies at all. A free-zone, cooperative, supervised financial entity or non-domiciled entity fires the refusal below. |
| Total renta bruta for the period | At or below ₡119,174,000 the small-company scale applies; above it the whole renta neta is taxed at 30%. |
| MEIC or MAG registration as a micro or small enterprise, and the year operations began | Decides whether the Mipyme reduction applies and in which year of the schedule. |
| Activity class and loss history by period | Decides the carry-forward length (3 or 5 periods) and whether each loss was booked as a deferred loss. |
| Determined tax for each of the last 3 periods, and any approved change to partial payments | Sets the 2026 partial-payment base and the balance due with the return. |
| Foreign-source passive income, group membership, net interest expense and the first period declared under Ley 9635 | Triggers the territorial exception and the art. 9 bis interest limit, both held here. |

Missing facts yield **Needs Input**, never a zero.

## The method, step by step

### [RATES] [Official source](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)

Apply the rate to renta imponible, which for a company is its renta neta. [S1, arts. 14 and 15](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)

| Item | 2026 figure | Conditions | Official source |
| --- | --- | --- | --- |
| General rate | 30% of renta neta | Personas jurídicas whose renta bruta for the period exceeds ₡119,174,000 | [S1, art. 15 a)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1) |
| Small-company eligibility | Renta bruta not above ₡119,174,000 | Fiscal periods from 1 January 2026; the test is gross income, the brackets apply to net income | [S4, art. 3](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=105834&param2=148657&param3=1) |
| Bracket 1 | 5% on the first ₡5,621,000 of annual renta neta | Eligible companies only | [S4, art. 3 b) i.](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=105834&param2=148657&param3=1) |
| Bracket 2 | 10% above ₡5,621,000 up to ₡8,433,000 | Eligible companies only | [S4, art. 3 b) ii.](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=105834&param2=148657&param3=1) |
| Bracket 3 | 15% above ₡8,433,000 up to ₡11,243,000 | Eligible companies only | [S4, art. 3 b) iii.](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=105834&param2=148657&param3=1) |
| Bracket 4 | 20% above ₡11,243,000 | Eligible companies only | [S4, art. 3 b) iv.](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=105834&param2=148657&param3=1) |
| Mipyme reduction, years 1 to 3 of business activity | 0% of the determined tax is payable | Micro or small enterprise registered with MEIC or MAG that applies the small-company scale; counted from its first year of operations | [S1, art. 15 b) as reformed by S6](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1) |
| Mipyme reduction, years 4 and 5 | 25% of the determined tax is payable | Same conditions | [S6, sole article](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=101001&param2=138742&param3=1) |
| Mipyme reduction, year 6 | 50% of the determined tax is payable | Same conditions; full tax from year 7 | [S6, sole article](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=101001&param2=138742&param3=1) |

The 2025 return (filed in 2026) uses Decreto 44772-H instead: eligibility up to ₡119,629,000 of renta bruta and brackets at ₡5,642,000, ₡8,465,000 and ₡11,286,000. [S5, arts. 3 and 7](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=103391&param2=148976&param3=1)

The scale is not elective. Once renta bruta passes the threshold, the 30% rate applies to all renta neta, so one extra colón of gross income can raise the tax by several million colones (Case 2). The Administration may correct artificial fragmentation of activities to stay under the threshold. [S1, art. 15 b)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1); [S7, art. 23 b)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=95992&param2=139872&param3=1)

### [BASE] [Official source](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)

1. **Renta bruta.** All income and benefits received or accrued in the period from Costa Rican-source activity. Foreign-currency transactions convert at the Banco Central reference selling rate; realised and period-end exchange differences on assets and liabilities are taxable gains or deductible losses. Unexplained increases in net worth are renta bruta. The return must carry a statement of assets and liabilities. [S1, art. 5](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
2. **Exclusions.** Capital contributions; asset revaluations; profits, dividends and other distributions paid or credited to art. 2 taxpayers (art. 6 c)); dividend distributions where the shareholder is another capital company domiciled in Costa Rica that carries on an economic activity and is subject to this tax (art. 6 h)); and chapter XI capital gains unless the asset is used in the activity or the activity is habitual. Gains of a commercial company on shares of any entity used in its own activity are exempt in the part matching undistributed profits. Capital income and gains from assets used in the activity are taxed here, not under chapter XI. [S1, arts. 1 and 6](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
3. **Renta neta.** Deduct costs and expenses that are useful, necessary and pertinent to produce the profit, supported by vouchers and recorded in the accounts. Expenses that produce both taxed and exempt income are deductible only in the taxed proportion. [S1, art. 7](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1) Every art. 8 deduction except donations also needs, together: an expense necessary to obtain taxable income, actual or potential; any withholding due under the law made and paid; and vouchers authorised by the Administration. The Administration may reject listed expenses, including salaries, organisation and advertising costs, that it finds excessive or not indispensable. [S1, art. 8, closing paragraphs](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
4. **Selected deductions** [S1, art. 8](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1):
   - cost of goods and services sold (a));
   - interest and financial expenses directly related to the business and taxed income, except amounts to be capitalised (d)). Not deductible: interest paid to partners of an SRL (treated as dividends), interest on which the tax was not withheld, and interest disconnected from taxable income. The company must prove the use of the loans in the documents filed with the return. Art. 9 bis then caps what remains;
   - depreciation of income-producing tangible assets at the rates or useful lives the regulation sets (f)); a disposal at a value different from tax written-down value gives a taxable gain or deductible loss;
   - employer contributions required by law (i));
   - organisation expenses, deductible when paid or over 5 consecutive periods from the start of productive activity (n));
   - qualifying donations, capped at 10% of renta neta computed before the donation (q)).
5. **Interest limit.** Net interest expense (interest expense less the period's financial income) is deductible up to 20% of UAIIDA, computed as net profit plus deductible borrowing costs, depreciation and amortisation. Any excess carries forward to later periods, each within its own cap. Outside the formula: interest already non-deductible under art. 9 k); credit formalisation commissions and exchange differences; interest on debts with the Sistema de Banca para el Desarrollo, Conassif-supervised entities or supervised foreign banks, unless the Administration finds the loan is not real or is backed by the borrower's own deposits; and interest financing a public infrastructure project of a domiciled developer that is subject to art. 23 g) withholding, whose profit and borrowing cost also leave UAIIDA. The Administration may authorise a higher limit on a prior reasoned request; hold any case that relies on one. [S1, art. 9 bis](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1) Ley 9635 Transitorio XX and regulation Transitorio III phase it in: 30% in the second period declared under Ley 9635 and the next, then 2 points less each period until 20%. The 2026 percentage therefore depends on the company's first Ley 9635 period; confirm it before applying a cap. [S8, Transitorio XX](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=87720&param2=150648&param3=1)

### [LOSSES] [Official source](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)

- A loss of a period is deductible in the **3 following periods**. Agricultural companies, and film and audiovisual companies whose activity falls within the regulation's definition, deduct over the **5 following periods**. Industrial companies that began after the law took effect may use 5 periods, then the general rule. [S1, art. 8 g)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
- The 3-period rule has covered every company since Ley 9635; Ley 10657 of 10 March 2025 re-enacted it and added the film and audiovisual rule. [S2, art. 8 g) version 9](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=3&param4=63824); [S3, art. 32(2)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=104196&param2=145503&param3=1)
- The loss is accepted only if booked as a deferred loss (pérdidas diferidas), at the Administration's judgement. Companies combining agricultural or industrial activity with commercial activity must keep separate accounts for each. [S1, art. 8 g)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
- A balance not used within the period gives no right to a refund or credit. [S1, art. 8 g)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)

There is no carry-back and no percentage cap on use within the window in the text read. The order of use when several vintages are live is not stated there; hold any case that turns on it.

### [PARTIAL PAYMENTS] [Official source](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)

1. **Base.** The greater of the tax determined for the immediately preceding period and the arithmetic average of the last 3 periods. With fewer than 3 returns, use those filed. A company filing its first period gives the Administration a reasoned estimate by January; otherwise the Administration sets the instalment. [S1, art. 22 a)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1) Hacienda's 2025 notice tells companies that began during the period to make the estimate and pay with the official payment receipt. [S11](https://www.hacienda.go.cr/docs/CP422025.pdf) The deadline for a company that starts after January is not stated in the text read; hold it.
2. **Amount.** 75% of the base, in 3 equal instalments. [S1, art. 22 b)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)
3. **Due dates.** By the last business day of **June, September and December**. Art. 22 b) still prints March, June and September, but the regulation sets June, September and December from 1 January 2021, and Hacienda announces those months. [S7, Transitorio I(2)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=95992&param2=139872&param3=1); [S11](https://www.hacienda.go.cr/docs/CP422025.pdf) Use Hacienda's schedule, and record the conflict in the working papers.
4. **Credit.** The instalments, and withholdings that count as payments on account, are deducted from the tax on the return; the balance is paid with the return. [S1, arts. 22 c) and 24](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1); [S7, art. 26](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=95992&param2=139872&param3=1)
5. **Changes.** Before an instalment falls due, the company may ask in writing to eliminate instalments because it expects a loss, or to reduce them because extraordinary income inflated the base. It must prove the ground. Hacienda's request form asks a loss request to attach a balance sheet and income statement to the end of the month before the request and projected to the period end, with notes and assumptions. [S1, art. 22](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1); [S13](https://www.hacienda.go.cr/docs/FormularioSolicitudElimDismPP.pdf)
6. **Exception.** Companies whose income comes exclusively from agricultural and livestock activity may pay the whole tax in one instalment with the return. [S1, art. 22 c)](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1)

Missing an instalment triggers interest under CNPT art. 57 (see Penalties).

### [FILING AND PAYMENT MECHANICS] [Official source](https://www.hacienda.go.cr/docs/CP11-2026.pdf)

- Register with the taxpayer register when activity starts; report data changes and cessation within 10 business days. [S7, art. 27](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=95992&param2=139872&param3=1)
- File the self-assessment return and pay within 2 months and 15 calendar days after the period ends, whatever the amount of gross income and even if income is exempt or not subject. The duty to file survives non-payment. [S1, arts. 20 and 21](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1); [S7, art. 28](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=95992&param2=139872&param3=1) For the 2026 period that is 15 March 2027, a Monday.
- Form: **102, Impuesto sobre las Utilidades - Persona Jurídica (ISU02)**, annual, in TRIBU-CR; Hacienda's codification maps it to form 101 of the earlier systems, which also covered individuals. [S12](https://www.hacienda.go.cr/docs/a_1NuevaCodificacionDeDeclaracionesEnTRIBU-CR-Consolidado_PP_PJ_PF.pdf)
- Where: for the 2025 return, Hacienda named the TRIBU-CR Oficina Virtual (OVi), with payment online in the OVi by entering an IBAN account or at Banco de Costa Rica or BAC branches; partial payments and withholdings appear at settlement once the return is filed. [S10](https://www.hacienda.go.cr/docs/CP11-2026.pdf) For the first 2025 partial payment (June 2025), it named a real-time debit in ATV or authorised banks, online or at their counters. [S11](https://www.hacienda.go.cr/docs/CP422025.pdf) Confirm the channels Hacienda announces for the 2026 instalments and the 2027 return; hold them until then.
- When the deadline falls on a weekend, Hacienda moved it to the next business day for the 2025 return (Monday 16 March 2026). [S10](https://www.hacienda.go.cr/docs/CP11-2026.pdf)
- Income reported in VAT returns must also be reported in the income tax return. [S10](https://www.hacienda.go.cr/docs/CP11-2026.pdf)
- On cessation of activity, file a final return with final statements within 30 days and pay then; a company that is legally extinguished but keeps trading in fact must still file. [S1, art. 20](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1); [S7, art. 29](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=95992&param2=139872&param3=1)

The box-by-box layout of TRIBU-CR form 102 was not read; map figures to its sections in the OVi itself and hold box numbers.

### [PENALTIES AND INTEREST] [Official source](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1)

| Item | Amount or rate | Conditions | Official source |
| --- | --- | --- | --- |
| Late filing | 50% of one salario base | Return not filed within the legal period | [S9, CNPT art. 79](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1) |
| Late payment of self-assessed tax | 1% per month or part month, capped at 20% of the unpaid amount | Runs from the due date to payment. Where an art. 38 deferral or instalment arrangement is granted, the article says the penalty is not applied and its computation is not interrupted; hold the effect on a given arrangement until art. 38 is read | [S9, CNPT art. 80 bis](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1) |
| Interest | Rate fixed by Administration resolution at least every 6 months: the simple average of state banks' commercial lending rates, never more than 10 points above the Banco Central basic passive rate | Applies to late payment and to partial payments not made; not waived except for Administration error | [S9, CNPT art. 57](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1) |
| Omitted or inaccurate return | 50% of the sanction base: the amount determined by the Administration for an omitted return, or the difference from the self-assessed amount for an inaccurate one; 100% if grave (concealment over 10% of the base), 150% if very grave (fraudulent means) | The 100% and 150% rates apply where the sanction base is no more than 500 salarios base; above that, and art. 81(2), were not read, so hold | [S9, CNPT art. 81](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1) |
| Late registration or change | 50% of one salario base per month or part month, capped at 3 salarios base | Registration, deregistration, or a change to relevant legal-representative or fiscal-domicile information, not filed within the regulation's period | [S9, CNPT art. 78](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1) |
| Voluntary correction | Penalty under arts. 78, 79 and 81 reduced by 75%, or 80% if self-assessed and paid on correction | Before any action by the Administration to obtain the correction; smaller reductions apply later | [S9, CNPT art. 88](https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1) |

The 2026 salario base amount and the current interest rate were not read; obtain both before computing a penalty or interest figure.

### Defaults and outputs

Use the corporate base outputs. State the period, the rate path (30% or small-company scale), any Mipyme reduction and its year, each loss vintage with its last usable period, the partial-payment base and instalments, credits, the balance due and every hold.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Renta bruta exactly ₡119,174,000 | Small-company scale ('no supere' includes equality) |
| Renta bruta above ₡119,174,000 | 30% on all renta neta; no blended computation |
| Dividend received by the company | Excluded from renta bruta under art. 6 c) when paid or credited to an art. 2 taxpayer, or under art. 6 h) when the shareholder is a domiciled capital company that carries on an economic activity and is subject to this tax; whether chapter XI capital-income tax or withholding applies is outside this file, so refer; foreign dividends of a group member stay held |
| Loss from 2022 not used by the end of 2025 | Expired (general 3-period rule); no refund or credit |
| Expected loss for 2026 | Partial payments are still due unless the Administration approves an elimination request made before the instalment date |
| Free-zone company (Ley 7210) | Not subject under art. 3 c); outside this file |
| Inactive company | Summary information return only (art. 2 a)); outside the computation |
| Foreign-source passive income of a group member | Territorial exception may apply; hold |

## Worked cases

All cases are fictional, in colones, for the 2026 period of an ordinary domiciled SA with no withholding credits unless stated.

### Case 1: ordinary company, partial payments and balance due

Renta bruta is ₡500,000,000, above the threshold, and renta neta is ₡80,000,000. Tax = 30% × 80,000,000 = **₡24,000,000**. Determined tax was ₡18,000,000 for 2025, ₡15,000,000 for 2024 and ₡12,000,000 for 2023; the 3-period average is ₡15,000,000, so the base is the greater figure, **₡18,000,000**. Instalments total 75% × 18,000,000 = **₡13,500,000**, paid as **₡4,500,000** by the last business day of June, September and December 2026. The balance due with form 102 by 15 March 2027 is 24,000,000 - 13,500,000 = **₡10,500,000**. Sources: S1 arts. 15, 22 and 24; S7 Transitorio I(2).

```oa-check
name: Case 1; 30% rate, partial-payment base and balance due
inputs:
  net_income: 80000000
  tax_2025: 18000000
  tax_2024: 15000000
  tax_2023: 12000000
steps:
  - tax: net_income * 0.30
  - average: (tax_2025 + tax_2024 + tax_2023) / 3
  - base: max(tax_2025, average)
  - instalments_total: base * 0.75
  - each_instalment: instalments_total / 3
  - balance_due: tax - instalments_total
expected:
  tax: 24000000
  average: 15000000
  base: 18000000
  instalments_total: 13500000
  each_instalment: 4500000
  balance_due: 10500000
```

### Case 2: decision, accept an order that crosses the gross-income threshold

A company not eligible for the Mipyme reduction expects renta bruta of ₡118,000,000 and renta neta of ₡15,000,000 for 2026. A customer offers a genuine extra order in 2026 worth ₡2,000,000 of gross income and ₡500,000 of net profit. Should it accept?

- **Decline:** renta bruta stays at ₡118,000,000, so the scale applies: 5% × 5,621,000 = 281,050; 10% × 2,812,000 = 281,200; 15% × 2,810,000 = 421,500; 20% × 3,757,000 = 751,400. Tax = **₡1,735,150**; profit after tax = **₡13,264,850**.
- **Accept:** renta bruta becomes ₡120,000,000, above ₡119,174,000, so 30% applies to all renta neta of ₡15,500,000. Tax = **₡4,650,000**; profit after tax = **₡10,850,000**.

Accepting costs **₡2,414,850** of after-tax profit. The deciding figure is the threshold: the order would have to add enough net profit to cover the jump from the scale to 30%, which this order does not. Recognition still follows the accrual rule; this decides whether to take new business, not when to book income already earned. Sources: S1 art. 15; S4 art. 3.

```oa-check
name: Case 2; small-company scale against 30% across the gross threshold
inputs:
  net_decline: 15000000
  net_accept: 15500000
steps:
  - band_5: min(net_decline, 5621000) * 0.05
  - band_10: max(min(net_decline, 8433000) - 5621000, 0) * 0.10
  - band_15: max(min(net_decline, 11243000) - 8433000, 0) * 0.15
  - band_20: max(net_decline - 11243000, 0) * 0.20
  - tax_decline: band_5 + band_10 + band_15 + band_20
  - after_tax_decline: net_decline - tax_decline
  - tax_accept: net_accept * 0.30
  - after_tax_accept: net_accept - tax_accept
  - cost_of_accepting: after_tax_decline - after_tax_accept
expected:
  band_5: 281050
  band_10: 281200
  band_15: 421500
  band_20: 751400
  tax_decline: 1735150
  after_tax_decline: 13264850
  tax_accept: 4650000
  after_tax_accept: 10850000
  cost_of_accepting: 2414850
```

### Case 3: one loss vintage expired, one usable

A commercial company with renta bruta of ₡300,000,000 has renta neta before loss relief of ₡14,000,000 in 2026. It holds an unused 2022 loss of ₡3,000,000, which was usable only in 2023 to 2025 and has expired, and a 2025 loss of ₡10,000,000 booked as a deferred loss, usable in 2026 to 2028. Assume the Administration accepts the 2025 loss as determined; an actual claim stays subject to its judgement under art. 8 g). Loss used = **₡10,000,000**; renta imponible = 14,000,000 - 10,000,000 = **₡4,000,000**; tax at 30% = **₡1,200,000**. The expired ₡3,000,000 cannot reduce the remaining ₡4,000,000 and gives no refund. Sources: S1 arts. 8 g) and 15.

```oa-check
name: Case 3; 3-period loss window, expired vintage excluded
inputs:
  income_before_losses: 14000000
  live_loss_2025: 10000000
  expired_loss_2022: 3000000
steps:
  - used: min(income_before_losses, live_loss_2025)
  - taxable: income_before_losses - used
  - closing_live_loss: live_loss_2025 - used
  - tax: taxable * 0.30
expected:
  used: 10000000
  taxable: 4000000
  closing_live_loss: 0
  tax: 1200000
```

## When to refuse or refer

- Art. 3 entity, free-zone company, supervised financial entity, cooperative or public entity: refuse this file and refer.
- Non-domiciled entity, permanent establishment, or foreign-source passive income of a group member: hold until the art. 2 b) and arts. 2 bis to 2 quinquies tests are qualified.
- Related-party transactions: refer for transfer pricing under art. 81 bis and Decreto 37898-H.
- Net interest expense that may exceed the art. 9 bis cap: hold until the company's first Ley 9635 period and its 2026 percentage are confirmed.
- Mipyme reduction claimed: confirm MEIC or MAG registration and how the years of business activity are counted for the company before applying it.
- Several live loss vintages, or a loss not booked as a deferred loss: refer.
- Any case needing the 2026 salario base, the current interest rate or form 102 box numbers: hold until read.

## Filing and payment

| Step | When | Where |
| --- | --- | --- |
| Partial payments 1 to 3 | Last business day of June, September and December 2026 | Channel Hacienda announces for 2026 (held) |
| Request to reduce or eliminate partial payments | Before the instalment falls due | Written request to the Dirección General de Tributación (S13) |
| Return and payment, period 2026 | By 15 March 2027 | Form 102 in the TRIBU-CR OVi; payment channels as Hacienda announces for 2027 (held) |

## Completion checklist

- [ ] Entity is an ordinary domiciled SA or SRL, not an art. 3 entity.
- [ ] Renta bruta compared with ₡119,174,000 and the rate path recorded.
- [ ] Mipyme registration and year of activity confirmed, or the reduction not applied.
- [ ] Every loss vintage dated, booked as deferred, and within its window.
- [ ] Partial-payment base recomputed from the last 3 determined taxes; instalments and credits reconciled.
- [ ] Interest-limit, territorial-exception and transfer-pricing screens cleared or held.
- [ ] Return and payment dates set for form 102 in TRIBU-CR.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| S1. Ley 7092, Ley del Impuesto sobre la Renta, consolidated version 83 of 83 (SINALEVI): arts. 1 to 9 bis, 14, 15, 20 to 24 and 26 read in full | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1 | 2026-11-02 |
| S2. Ley 7092 art. 8, article version 9 of 11 (before Ley 10657): inciso g) read | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=144103&param3=3&param4=63824 | 2026-11-02 |
| S3. Ley 10657, Ley de Cinematografía y Audiovisual: art. 32 read | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=104196&param2=145503&param3=1 | 2026-11-02 |
| S4. Decreto Ejecutivo 45333-H, 2026 bracket update: arts. 1 to 7 read in full | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=105834&param2=148657&param3=1 | 2026-11-02 |
| S5. Decreto Ejecutivo 44772-H, 2025 bracket update: arts. 3, 6 and 7 read | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=103391&param2=148976&param3=1 | 2026-11-02 |
| S6. Ley 10392, Mipyme reduction: sole article and commencement clause read | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=101001&param2=138742&param3=1 | 2026-11-02 |
| S7. Decreto Ejecutivo 43198-H, income tax regulation, version 5 of 5: arts. 23 and 26 to 29 and Transitorios I and III read | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=95992&param2=139872&param3=1 | 2026-11-02 |
| S8. Ley 9635, Fortalecimiento de las Finanzas Públicas: Transitorios XIX, XX and XXI read | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=87720&param2=150648&param3=1 | 2026-11-02 |
| S9. Ley 4755, Código de Normas y Procedimientos Tributarios, version 22 of 22: arts. 57, 78, 79, 80, 80 bis, 81(1) and (3) and 88 read in the browser | https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=6530&param2=148766&param3=1 | 2026-11-02 |
| S10. Hacienda press release CP-11-2026 on the return deadline: read in full | https://www.hacienda.go.cr/docs/CP11-2026.pdf | 2026-11-02 |
| S11. Hacienda press release CP-42-2025 on the first partial payment: read in full | https://www.hacienda.go.cr/docs/CP422025.pdf | 2026-11-02 |
| S12. Hacienda, Nueva codificación de declaraciones en TRIBU-CR: income tax rows read | https://www.hacienda.go.cr/docs/a_1NuevaCodificacionDeDeclaracionesEnTRIBU-CR-Consolidado_PP_PJ_PF.pdf | 2026-11-02 |
| S13. Hacienda form, Solicitud de disminución o eliminación de pagos parciales: part 1 read | https://www.hacienda.go.cr/docs/FormularioSolicitudElimDismPP.pdf | 2026-11-02 |

Not yet confirmed: the publication date and commencement of Ley 10392, and how its years of business activity apply to companies that began before it took effect; the order of use of several live loss vintages; the regulation's depreciation rates; the 2026 interest-limit percentage for a given company; arts. 2 bis to 2 quinquies and art. 2 b) tests; the art. 9 non-deductible items, which this file does not list; withholding rates creditable under art. 23 and CNPT art. 103 d); the 2026 salario base; the interest rate currently fixed under CNPT art. 57; CNPT arts. 38 and 81(2) and penalties on bases above 500 salarios base; the first-period estimate deadline for a company that starts after January; Hacienda's payment channels for the 2026 instalments and the 2027 return; TRIBU-CR form 102 box numbers; and whether Hacienda will move a weekend deadline in later years.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
