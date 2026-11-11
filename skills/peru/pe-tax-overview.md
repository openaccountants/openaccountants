---
name: pe-tax-overview
description: >
  Route a Peru tax question for 2026 to the correct computation and filing
  method before giving a headline rate. Use for Peru tax overview, SUNAT,
  residence, worldwide income, Peruvian-source income, personal and company
  tax, IGV, IPM, dividend withholding, financial transactions tax, ITF,
  payroll and annual return timing. Separates the income year from the year
  a return is filed, work income from rental and capital income, and company
  profit from distributions. Includes ordinary ITF classification, statutory
  rounding and same-holder transfer examples. Requires taxpayer identity,
  period, domicile, income type, transaction evidence and the requested job.
  Load the current country skill for its calculation; do not reuse an older
  year or an unconfirmed filing date.
jurisdiction: PE
category: orchestrator
domain: tax
type: router
tax_year: 2026
tax_year_notes: "2026 income and transactions; separately identified historical 2025 filing context"
last_updated: 2026-11-11
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
version: 0.1
---

# Peru Tax Overview v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** identify the taxpayer, income/transaction year, tax
domicile and job before selecting a rate. Then load the relevant current-year
method below. A bank receipt, company name or nationality does not determine
the tax. This overview owns the ordinary ITF reference. Linked skills own
their income-tax, IGV and payroll calculations, so their rates are not copied
here.

## Scope

Ordinary national tax intake in Peru for 2026: identify the workstreams,
order and evidence to pass to them. This is a router, not a substitute for
an income return, treaty determination or missing rental/capital calculation.

SUNAT administers national internal taxes and functions assigned by law or
agreement. Municipal taxation needs its own authority and rules. [SUNAT
functions, ROF DS 040-2023-EF art. 4](https://www.sunat.gob.pe/institucional/quienessomos/funciones.html).
Amounts here are soles, written S/. Old legal texts may say Nuevo Sol: Law
30381 renamed it Sol. [SUNAT official communication](https://www.sunat.gob.pe/mensajes/diciembre/2015/aviso-ti-161215.html),
[SUNAT monetary notation](https://www.sunat.gob.pe/indicestasas/uit.html).

## Ask the client first

1. Who is the taxpayer: individual, estate, company, branch or other entity?
   Obtain identity/RUC and separate an entity's funds from its owner's funds.
2. What is the income/transaction period and requested job: classification,
   computation, withholding, registration, filing or correction?
3. What are the tax-domicile facts/effective dates, source country, payer,
   recipient and claimed treaty? Obtain residence/movement evidence.
4. What produced each receipt: employment, independent work, business, rent,
   disposal, interest, dividend or transfer of existing money? Obtain contracts,
   invoices, payroll and acquisition records.
5. For a business, what regime and registrations apply, are there staff,
   and are operations related-party, imported, exported or nonresident?
6. Which accepted returns, deductions, withholdings and payments exist?
   For bank movements also identify account holders, currency, event and
   exemption evidence. A narration alone is not an accepted filing.

## The method, step by step

### 1. Separate the tax period from the filing year

The income-tax exercise starts on 1 January and ends on 31 December. Timing
of particular receipts still depends on category; not every category follows
the bank receipt date. [LIR art. 57](https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf):
`comienza el 1 de enero de cada año`.

For a 2026 computation obtain that year's UIT from the official table, then
use the relevant skill's conversions. The old overview's 2025 UIT is
historical, not a 2026 input. [SUNAT UIT table, DS 301-2025-EF](https://www.sunat.gob.pe/indicestasas/uit.html).
Do not use today's UIT for an older period.

Check the selected skill's tax year, effective-date conditions and source
read date. If its available version is still older, do not present it as a
2026 calculation. Open its primary law and arrange the missing current-year
work. A current overview does not make every linked skill current.

### 2. Establish the jurisdictional basis

Domiciled taxpayers fall within the worldwide-income basis. Non-domiciled
persons and the specified Peruvian branches/agencies/permanent establishments
of foreign enterprises are taxed on Peruvian-source income. Do not turn the
branch's domicile label into worldwide taxation of its foreign head office.
[LIR arts. 6-7](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf):
`solo sobre las rentas gravadas de fuente peruana`.

Apply individual domicile tests and effective dates, including the departure
exception; a change during the exercise does not automatically create a
part-year split. Determine source under the applicable provision, not the
bank's location. Resolve domicile, permanent establishment and any treaty
before selecting the tax method. [LIR arts. 7-10](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf).

### 3. Classify each stream and select its method

LIR art. 22 separates rent, other capital, business, independent work and
employment/other specified work. An individual can have several categories.
[LIR art. 22](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf):
`las rentas afectas de fuente peruana se califican`.

| Trigger | Method and evidence to pass | Primary basis |
|---|---|---|
| Individual employment or independent work | Load current [Income tax](peru-income-tax.md), adding [Payroll](peru-payroll.md) for employer withholding. Pass domicile, income category, certificates/receipts, documented deductions, foreign income and prior payments. The progressive work scale is not a flat gross-receipts tax. | [LIR arts. 52-A to 54](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf) |
| Rent, disposal or investment income | Obtain a current category-specific working paper. Pass asset/use, owner, dates, cost, receipts, losses and exemption facts. A work-income method/deduction does not establish capital treatment. | [LIR arts. 22-24](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [52-A to 54](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf) |
| Business income, including sole proprietor | Load current [Corporate income tax](pe-corporate-income-tax.md) after identifying regime. Pass entity/domicile, enrolment, revenue, tax-adjusted profit, losses, advances and foreign taxes. The General Regime headline is not every business's rate. | [LIR art. 14](https://www.sunat.gob.pe/legislacion/renta/ley/capiii.pdf), [28](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [55-56](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf) |
| Sale, service, import or export | Load [IGV and IPM](peru-igv.md). Pass event/place, taxpayer, period, exemption/special-rate facts, invoices/acceptance, purchase use and credit/payment history. Its current rate composition replaces the old overview's component split. | [LIGV arts. 12-17 and Law 32387 composition note](https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf) |
| Staff/remuneration | Load [Payroll](peru-payroll.md) and [Social contributions](peru-social-contributions.md). Pass actual month, employment regime, components, domicile, pension affiliation and cumulative records. Employer cost and employee withholding are distinct. | [LIR arts. 71, 75](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf); the methods cite separate labour/health/pension laws |
| Related-party or cross-border transaction | Load [Transfer pricing](peru-transfer-pricing.md) where applicable; separately resolve source, withholding and treaty entitlement before payment. Pass ownership, transaction, jurisdictions, comparables and group/reporting facts. | [LIR art. 32-A](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [6-10](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf) |
| New company/structure | Load current [Company formation](pe-company-formation.md). Pass owners, entity, capital, representation, registry/RUC and activities. Registration does not establish every tax treatment. | [LIR art. 14](https://www.sunat.gob.pe/legislacion/renta/ley/capiii.pdf) identifies the separate taxpayer question |
| Bank movement | Apply the ITF screen below independently of income/IGV classification. Obtain both holders, currency, value, event, purpose and any exemption declaration. | [Law 28194 arts. 9-17](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf) |

Ordinary rental/capital work remains a required separate handoff when the
loaded individual skill covers work income only. Do not count its existence
as comprehensive individual-tax coverage.

### 4. Treat distributions separately from company profit

A profit calculation does not settle dividend withholding. Identify recipient
type/domicile, distribution, profit vintage, any stability arrangement and
treaty before applying the dividend provisions. Article 73-A excludes
payments to domiciled legal persons from its withholding and has a payer
payment/beneficiary reimbursement rule for distributions in kind. Pass these
facts to the corporate/distribution method and check its transition rules;
do not use the old universal dividend headline. [LIR arts. 52-A, 54(a), 56(e)](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf),
[73-A and transition references](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf):
`excepto cuando la distribución se efectúe a favor de personas jurídicas domiciliadas`.

### 5. Build one obligation schedule

Record each obligation's taxpayer/RUC, period, frequency, actual form/version,
due-date source, credits and payment evidence. Load its method for the
portal, boxes, submission and payment sequence. Keep return acceptance
separate from payment settlement.

Historical correction: RS 386-2025 expressly governs income year 2025 filed
in 2026. It contains general and separate extended calendars, Law 31940
eligibility/exclusions and RUC-specific dates. The old May-to-June statement
was not a universal company/individual window and is not a 2026-income
deadline. Apply the taxpayer's actual calendar and any relevant later
extension. [RS 386-2025 arts. 1, 3-6](https://www.sunat.gob.pe/legislacion/superin/2025/000386-2025.pdf):
`correspondiente al ejercicio gravable 2025`.

Exact 2027 annual dates and released forms for 2026 income are not confirmed
here. Do not shift an old calendar forward a year, or tell every employee
to file. First establish the filing obligation under the applicable method.

### 6. ITF: classify before multiplying

This reference covers ordinary bank credits/debits and screens the distinct
annual non-cash settlement provision. It does not prepare a bank/operator's
return or an article 9(g) annual return.

| Item | Figure and conditions | Primary source |
|---|---|---|
| Ordinary ITF | 0.005% of the taxable operation value. It is not a percentage of profit or an unconditional tax on every receipt. | [Law 28194 arts. 9-10, 12, Law 29667 amendment](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf): `cinco por ciento (0,005%)`; [SUNAT rate](https://orientacion.sunat.gob.pe/07-la-tasa-del-impuesto-itf-empresas) |
| Same-holder transfer | Art. 9(a) excludes credit, debit or transfer between the same holder's accounts, at the same or different financial enterprises. Establish legal ownership first. | [Art. 9(a)](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf): `entre cuentas de un mismo titular` |
| Rounding | Express to two decimals; discard the third decimal; adjust a second decimal below 5 to 0 or above 5 to 5. A second decimal equal to 5 stays 5. For nonnegative amounts this rounds down to a multiple of 0.05, not normally to cents. | [Art. 13, Law 29667 art. 3](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf): `debe suprimirse` / `se ajusta a cinco (5)` |
| Annual non-cash/non-means settlement | Art. 9(g) concerns a third-category taxpayer settling more than 15% of annual obligations without cash or statutory means of payment. The excess base bears double the ordinary rate. Test its insurance-settlement exceptions. This is not a normal bank transfer. | [Arts. 9(g), 12(b), 14(h), 17(c.2)](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf): `más del quince por ciento (15%)` / `el doble de la alícuota` |

For an ordinary bank movement:

1. Identify holder, event and full operation value. The obligation arises at
   credit/debit. Actual foreign currency needs its lawful conversion input,
   not a remembered FX rate. [Arts. 9(a), 12, 14(a)](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).
2. Test same-holder exclusion and the applicable Appendix exemption, not an
   account nickname. Art. 11 normally requires an identifying sworn account
   declaration, with specified identification exceptions. Salary/pension
   accounts have employer/payment/communication conditions; an existing
   habilitated account has its specified credit/debit limits. CTS has a
   separate rule. [Art. 11, Appendix (c)-(d)](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).
3. If taxable, apply the rate to that operation's full taxable value and
   statutory rounding. Do not net sales against payments or round a monthly
   aggregate as one operation. The examples assume separate nonnegative
   PEN transactions. [Arts. 10, 12-13](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).
4. Reconcile the bank's collection to its evidence. Art. 16 requires a
   document stating retained/perceived tax and return of undue/excess
   collections. Ordinary customers do not file a second return simply
   because their bank collected ITF. Identify any separate art. 17 duty
   first. [Arts. 15-17](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).

For art. 9(g), obtain whole-year obligations and each settlement method,
then determine the statutory excess and obtain the full annual filing
method. RS 386-2025 also concerns that provision for its express historical
exercise, not every customer's account tax. [Arts. 9(g), 17](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf),
[RS 386-2025 art. 3(d)](https://www.sunat.gob.pe/legislacion/superin/2025/000386-2025.pdf).

ITF and the legal obligation to use means of payment are distinct. Paying
ITF does not cure missing payment evidence for an expense. [Law 28194
arts. 3-8](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).

## Worked cases

Amounts are hypothetical PEN inputs. Neither case determines the underlying
receipt's income-tax or IGV treatment.

### Case 1: taxable credit and statutory rounding

An ordinary taxable account credit is S/ 15,780, no applicable exclusion or
exemption. ITF before rounding is 15,780 x 0.005% = S/ 0.789. Art. 13 gives
S/ 0.75, not S/ 0.79. Reconcile to the bank's ITF record. Fees are outside
this hypothetical value. [Law 28194 arts. 9(a), 10, 12-13](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).

```oa-check
name: Peru ordinary ITF, statutory rounding per operation
inputs:
  operation_value: 15780
  rate_percent: 0.005
steps:
  raw_itf: operation_value * rate_percent / 100
  truncated_cents: floor(raw_itf * 100) / 100
  payable_itf: floor(truncated_cents * 20) / 20
expected:
  raw_itf: 0.789
  truncated_cents: 0.78
  payable_itf: 0.75
```

### Case 2: ownership decides the route

Compare two S/ 20,000 movements. A transfer proved to be between the same
taxpayer's accounts is excluded under art. 9(a): no ITF on that transfer's
debit/credit. A payment between different taxpayers' ordinary accounts, both
legs taxable and no Appendix exemption, gives S/ 1.00 per leg, S/ 2.00
combined. This is classification, not permission to relabel a supplier's
account as the payer's. [Law 28194 arts. 9(a), 10, 12-13](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).

```oa-check
name: Peru ITF, own-account exclusion and two taxable holders
inputs:
  transfer_value: 20000
  rate_percent: 0.005
  own_account_taxable_legs: 0
  different_holder_taxable_legs: 2
steps:
  per_leg_itf: floor(transfer_value * rate_percent / 100 * 20) / 20
  own_account_itf: per_leg_itf * own_account_taxable_legs
  different_holder_total_itf: per_leg_itf * different_holder_taxable_legs
expected:
  per_leg_itf: 1
  own_account_itf: 0
  different_holder_total_itf: 2
```

## When to refuse or refer

- Refuse a single-rate answer without domicile, category, regime, period or
  exemption facts. Return the missing facts and applicable source.
- Refer a rental/capital calculation absent from the loaded work-income
  method, disputed domicile/PE, treaty claim or activity-specific incentive
  to its current-year method. The overview does not fill those gaps.
- Refer bank/operator returns, art. 9(g) annual filing, disputed ITF exemption
  or refund cases and foreign-currency rounding/conversion for the full
  procedure. These PEN examples do not confirm those workflows.
- Route late filing/payment or misuse of an exempt account to the applicable
  Code/relief assessment. Law 28194 art. 22 imports the Tax Code; art. 18
  separately addresses exempt-account misuse. A remembered income-tax fine
  is not necessarily the customer's ITF sanction. [Arts. 18, 22](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).
- Municipal property tax, customs classification/duties, excise, mining,
  agrarian/Amazonia or zone incentives, trusts and regulated finance require
  their own sources and assessment.

## Completion checklist

Return taxpayer/period, established domicile/source facts, categories,
selected current-year methods and primary links, registration/withholding/
filing/payment workstreams, documents checked and unresolved facts/source
gaps. Give an amount only when its method's inputs and conditions are met.
Keep income, IGV, payroll, distributions and ITF separate and reconcile their
payment evidence to the ledger.

## Sources

| Source and actual material read | URL | Read on |
|---|---|---|
| LIR chapter II: arts. 6-10 jurisdictional basis, domicile/effective dates and PE qualifications | https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf | 2026-11-11 |
| LIR chapter III: art. 14 taxpayer/entity and sole-proprietor/attribution distinctions | https://www.sunat.gob.pe/legislacion/renta/ley/capiii.pdf | 2026-11-11 |
| LIR chapter V: art. 22 categories, arts. 28, 32-A, 33-34 classification/TP routing; no full specialist computation claimed | https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf | 2026-11-11 |
| LIR chapter VII: arts. 52-A to 56, separate work/capital/corporate/nonresident/dividend regimes and transition references | https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf | 2026-11-11 |
| LIR chapter VIII: art. 57 calendar-year sentence and category timing context, 2026 amendment note | https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf | 2026-11-11 |
| LIR chapter X: arts. 71, 73-A, 75 withholding routes and dividend exceptions | https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf | 2026-11-11 |
| LIGV chapter V: arts. 12-17 base/rate structure and Law 32387 composition note | https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf | 2026-11-11 |
| SUNAT functions: national internal-tax/assigned functions, ROF DS 040-2023-EF art. 4 attribution | https://www.sunat.gob.pe/institucional/quienessomos/funciones.html | 2026-11-11 |
| SUNAT currency communication: actual Law 30381 name-change statement | https://www.sunat.gob.pe/mensajes/diciembre/2015/aviso-ti-161215.html | 2026-11-11 |
| SUNAT UIT table: distinct 2026/2025 entries/decree references and S/ notation | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 |
| Law 28194 TUO current PDF: arts. 3-18, 20, 22 and Appendix (c)-(d), ITF/exclusions/rounding/collection/exemptions | https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf | 2026-11-11 |
| SUNAT ITF rate page: actual operation-value 0.005% statement | https://orientacion.sunat.gob.pe/07-la-tasa-del-impuesto-itf-empresas | 2026-11-11 |
| RS 386-2025: all seven pages, definitions and general/extended calendars, expressly exercise 2025 filed in 2026 | https://www.sunat.gob.pe/legislacion/superin/2025/000386-2025.pdf | 2026-11-11 |

Not yet confirmed: exact 2027 annual dates/extensions and released annual forms/numbered fields for 2026 income; client-specific domicile, regime, treaty/stability/profit-vintage and foreign-credit entitlement; actual FX and the foreign-currency ITF rounding/conversion sequence; bank/operator and art. 9(g) filing screens/payment codes; current numerical penalties, interest and individual relief; specialist/municipal computations named above. Ordinary rental/capital work needs its own current computation when the work-income skill lacks it. The old blanket dividend rate and general May-to-June filing window are not valid universal instructions.
