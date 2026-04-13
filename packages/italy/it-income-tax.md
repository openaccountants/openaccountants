---
name: it-income-tax
description: >
  Use this skill whenever asked about Italian income tax for self-employed individuals (lavoratori autonomi, liberi professionisti) under regime ordinario. Trigger on phrases like "Modello Redditi PF", "Quadro RE", "IRPEF", "redditi di lavoro autonomo", "imposta sul reddito Italy", "deduzioni", "detrazioni", "addizionale regionale", "addizionale comunale", "regime ordinario", "acconti IRPEF", "no tax area", "INPS Gestione Separata", "rivalsa INPS", or any question about filing or computing income tax for an Italian freelancer or professional. Also trigger when preparing or reviewing a Modello Redditi PF, computing deductions, or advising on regime ordinario tax obligations. This skill covers progressive IRPEF brackets, deduzioni, detrazioni, addizionali, acconti, Quadro RE structure, rivalsa INPS, and penalties. ALWAYS read this skill before touching any Italian income tax work. Does NOT cover regime forfettario -- see it-regime-forfettario.md.
version: 2.0
jurisdiction: IT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Italian Income Tax -- Regime Ordinario (IRPEF) v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Italy (Repubblica Italiana) |
| Tax | IRPEF (Imposta sul Reddito delle Persone Fisiche) + Addizionale regionale + Addizionale comunale |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | DPR 917/1986 (TUIR -- Testo Unico delle Imposte sui Redditi) |
| Tax authority | Agenzia delle Entrate (AdE) |
| Filing portal | Fisconline / Entratel (dichiarazioni.agenziaentrate.it) |
| Filing deadline | 30 June (online Modello Redditi PF); 30 November (Modello 730 via sostituto) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a qualified Italian Commercialista |
| Skill version | 2.0 |

### IRPEF Brackets 2025 (Regime Ordinario) [T1]

| Taxable Income (EUR) | Rate | Tax on Band | Cumulative Tax |
|---|---|---|---|
| 0 -- 28,000 | 23% | 6,440 | 6,440 |
| 28,001 -- 50,000 | 35% | 7,700 | 14,140 |
| Over 50,000 | 43% | on excess | 14,140 + 43% |

**Formula:** Tax = cumulative tax for lower bracket + (income - lower bracket threshold) x marginal rate

**No-tax area:** Detrazioni per lavoro autonomo reduce effective IRPEF to zero up to roughly EUR 4,800 net income (result of detrazioni calculation, not a true zero-tax band).

### Addizionali (Regional + Municipal Surtaxes) [T1]

| Surtax | Rate | Notes |
|---|---|---|
| Addizionale regionale | 1.23%-3.33% | Varies by region; default 1.23% if region not specified |
| Addizionale comunale | 0%-0.9% | Varies by municipality; zero in some comuni |

Apply both addizionali to the same taxable income (net income after deduzioni, before detrazioni).

### Detrazioni per Lavoro Autonomo (Reduce Tax Payable) [T1]

| Net Income (EUR) | Detrazione |
|---|---|
| <= 5,500 | EUR 1,265 |
| 5,501 -- 28,000 | EUR 500 + [1,200 x (28,000 - income) / 22,500] |
| 28,001 -- 50,000 | EUR 500 x (50,000 - income) / 22,000 |
| > 50,000 | 0 |

Detrazioni reduce IRPEF payable (not taxable income). Compute after applying bracket rates.

### INPS Gestione Separata (Social Contributions) [T1]

| Contributor Type | Rate 2025 |
|---|---|
| Freelancer without pension fund (no cassa) | 26.07% |
| Freelancer with pension fund (con cassa) | 24% |
| Pensioners or those with other coverage | 24% |

Applied to net income (gross receipts - deductible expenses). Cap: EUR 119,650 gross.

**Rivalsa INPS (4% surcharge on invoices):** Freelancers without a cassa may add 4% to invoice. Rivalsa received is taxable income; corresponding INPS paid is deductible.

### Acconti IRPEF (Advance Payments) [T1]

| Threshold | Rule |
|---|---|
| IRPEF due < EUR 51.65 | No acconto required |
| IRPEF due EUR 51.65-257.52 | One payment: 100% by 30 November |
| IRPEF due > EUR 257.52 | 40% by 30 June (with saldo); 60% by 30 November |

Acconto rate: 100% of prior-year IRPEF (or 100% of current-year estimate if lower).

### Conservative Defaults [T1]

| Situation | Default Assumption |
|---|---|
| Regional surtax unknown | Apply 1.23% (statutory minimum) |
| Municipal surtax unknown | Apply 0% (cannot assume) -- flag for client |
| Pension fund (cassa) membership unknown | Apply 26.07% Gestione Separata rate |
| Rivalsa INPS on invoices unclear | Do NOT assume 4% added -- ask client |
| Deductible vs non-deductible expense disputed | Non-deductible -- flag for reviewer |
| Payment received: unclear if taxable | Taxable -- flag for reviewer |
| Invoice date vs payment date conflict | Apply cassa (cash) basis for freelancers |
| Refund or reimbursement | Non-taxable if documented client reimbursement; taxable otherwise |

### Red Flag Thresholds [T1]

| Flag | Threshold |
|---|---|
| Gross receipts > EUR 85,000 | Was regime forfettario? -- verify |
| INPS contributions < 20% of net income | Possible miscalculation -- review |
| No acconto payments recorded | Check if acconti were due |
| Large cash payments > EUR 999.99 | Anti-money-laundering limit -- flag |
| Expense > EUR 5,000 with no documentation | Reject -- cannot deduct |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full calendar year (January-December) in CSV, PDF, or pasted text. Confirmation of regime (ordinario vs forfettario), region, and municipality.

**Recommended:** All client invoices (fatture), F24 payment receipts (acconti IRPEF and INPS), INPS Gestione Separata / cassa contribution statements, prior year Modello Redditi.

**Ideal:** Complete books of accounts, asset register with ammortamento schedules, complete set of fatture emesse and ricevute, family situation details (dependants for detrazioni).

### Refusal Catalogue

**R-IT-1 -- Client provides only bank totals, no itemised expenses.** "Request itemised expense list with F24/receipts before proceeding."

**R-IT-2 -- Income from both regime ordinario AND regime forfettario in same year.** "Mixed regime not possible in the same year. Verify which applies and for which period."

**R-IT-3 -- Gross receipts > EUR 85,000 but client claims regime forfettario.** "Forfettario threshold exceeded. Regime ordinario applies automatically. Proceed under ordinario."

**R-IT-4 -- Non-resident claiming full Italian detrazioni.** "Non-residents have restricted access to detrazioni. Clarify residency status -- escalate."

**R-IT-5 -- Client requests deduction for private vehicle without usage log.** "Reject vehicle deduction beyond 20% cap. Art. 164 TUIR requires documented business use."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| BONIFICO DA [client name] | Gross receipts -- professional income | Revenue | Standard SEPA credit from client |
| VB DA [client name] / VB ENTRATA | Gross receipts -- professional income | Revenue | UniCredit/BancoBPM credit notation |
| ACCREDITO DA [client] | Gross receipts -- professional income | Revenue | Generic bank credit from client |
| STRIPE PAYMENTS EUROPE / STRIPE PAYOUT | Gross receipts -- online income | Revenue | Gross-up to pre-fee amount; Stripe fee deductible |
| PAYPAL TRANSFER / PAYPAL ACCREDITO | Gross receipts | Revenue | Gross-up; PayPal fee deductible |
| SATISPAY BUSINESS PAYOUT | Gross receipts | Revenue | Satispay payout; fee deductible |
| NEXI PAGAMENTI / NEXI POS VERSAMENTO | Gross receipts -- card income | Revenue | Nexi merchant settlement; gross-up |
| SUMUP PAYOUT / ZETTLE PAYOUT | Gross receipts -- card income | Revenue | Card terminal payout; gross-up |
| REVERSALE [client] / RIMESSA CLIENTI | Gross receipts | Revenue | Public administration or factoring payment |
| RIVALSA INPS (portion of invoice) | Taxable -- included in gross receipts | Revenue | 4% rivalsa component is taxable income |
| INTERESSI ATTIVI / INTERESSI MATURATI | Interest income -- Quadro RW/RL | NOT professional income | Separate treatment |
| RIMBORSO SPESE [client] | Non-taxable reimbursement (if documented) | Flag | Requires client reimbursement note |
| STIPENDIO / SALARIO [employer] | Employment income | NOT professional income | Separate head -- redditi da lavoro dipendente |

### 3.2 Expense Patterns (Debits)

| Pattern | Tax Category | Treatment | Notes |
|---|---|---|---|
| AFFITTO UFFICIO / CANONE LOCAZIONE / PIGIONE | Rent -- deductible (professional share) | Fully deductible | Home office: only dedicated professional portion |
| ENEL / ENI PLENITUDE / A2A ENERGIA | Utilities -- 50% deductible (mixed use) | 50% deductible | Flag if solely professional premises -- 100% |
| TELECOM ITALIA / TIM FIBRA / FASTWEB / WIND3 | Internet/phone -- 80% deductible | 80% deductible | Art. 54 TUIR telecoms cap |
| VODAFONE MOBILE / TIM MOBILE / ILIAD | Mobile phone -- 80% deductible | 80% deductible | Same Art. 54 TUIR cap |
| ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE | Software subscriptions -- 100% deductible | Fully deductible | Professional software |
| COMMERCIALISTA / CONSULENTE FISCALE / STUDIO [name] | Professional fees -- 100% deductible | Fully deductible | Accountant/tax advisor fees |
| AVVOCATO / NOTAIO | Legal fees -- 100% deductible (if professional) | Fully deductible | Flag if personal matter |
| TRENITALIA / ITALO / FRECCIAROSSA | Travel -- 100% deductible if professional | Fully deductible | Require destination + purpose note |
| RYANAIR / EASYJET / ITA AIRWAYS / ALITALIA | Air travel -- 100% deductible if professional | Fully deductible | Require itinerary + purpose |
| HOTEL / AGODA / BOOKING.COM | Accommodation -- 75% deductible | 75% deductible | Art. 109 TUIR hospitality cap |
| RISTORANTE / PIZZERIA / CAFFE | Meals -- 75% deductible | 75% deductible | Must be professional purpose; social = 0% |
| INPS F24 / CONTRIBUTI GESTIONE SEPARATA | INPS contributions -- 100% deductible | Fully deductible | Social contributions reduce taxable income |
| F24 ACCONTO IRPEF / F24 SALDO IRPEF | IRPEF advance/balance | NOT deductible | Tax payments are not expenses |
| ASSICURAZIONE PROFESSIONALE / RC PROFESSIONALE | Professional insurance -- 100% deductible | Fully deductible | Professional liability insurance |
| ADDIZIONALE REGIONALE / ADDIZIONALE COMUNALE | NOT deductible | EXCLUDE | Surtaxes are not deductible |
| SPESE BANCARIE / COMMISSIONI BANCARIE / CANONE CONTO | Bank fees -- 100% deductible | Fully deductible | Professional account fees |
| AMORTAMENTO / BENE STRUMENTALE | Capital asset -- depreciation schedule | Depreciate | Do not expense in full; apply ammortamento table |
| AUTONOLEGGIO / NOLEGGIO AUTO | Car hire -- 20% deductible cap | 20% deductible | Art. 164 TUIR |
| CARBURANTE / ENI / Q8 / SHELL | Fuel -- 20% deductible cap | 20% deductible | Same Art. 164 TUIR |
| FORMAZIONE / CORSO / SEMINARIO | Training/education -- 100% deductible | Fully deductible | Professional development |
| CANCELLERIA / MATERIALE UFFICIO / UNIEURO (office) | Office supplies -- 100% deductible | Fully deductible | Minor consumables |
| CONTRIBUTO CASSA [profession] / ENPAM / INARCASSA | Cassa contributions -- 100% deductible | Fully deductible | Replaces Gestione Separata |
| STRIPE FEE / PAYPAL FEE / SATISPAY FEE | Payment processor fees | Fully deductible | Deduct the gross-up difference |

---

## Section 4 -- Worked Examples

### Example 1 -- Intesa Sanpaolo (Milan, Graphic Designer)

**Input line (Intesa Sanpaolo CSV, semicolon-delimited):**
`03/01/2025;;BONIFICO DA STUDIO GAMBA SRL;;3.500,00`

**Reasoning:**
Standard SEPA credit from a client SRL. Valentina is a graphic designer with no pension fund (Gestione Separata at 26.07%). This is professional income (Quadro RE). Amount EUR 3,500 is ex-IVA (confirm). Taxed on cash basis (principio di cassa).

**Classification:** Gross receipts EUR 3,500. Add to annual professional income.

### Example 2 -- UniCredit (Turin, IT Consultant)

**Input line (UniCredit PDF):**
`10/01/2025 | VB DA ACCENTURE SRL | AVERE EUR 6,500.00`

**Reasoning:**
Monthly fee from Accenture SRL. Marco receives EUR 6,500/month x 10 months = EUR 65,000 gross annual income. Single client pattern -- flag for reviewer (verify no regime forfettario election active). Gestione Separata applies.

**Classification:** Gross receipts EUR 6,500. Flag: single client concentration.

### Example 3 -- FinecoBank (Rome, Photographer)

**Input line (FinecoBank CSV):**
`15/03/2025;NEXI POS VERSAMENTO;Entrata;7.000,00`

**Reasoning:**
Nexi POS card payment settlement EUR 7,000. Sofia is a photographer. Nexi collects card payments and settles net of fees. Gross-up to total card payments received; Nexi fee is deductible. Match to Nexi merchant portal for exact split.

**Classification:** Gross receipts EUR 7,000 (or gross-up). Nexi fees deductible.

### Example 4 -- N26 Italy (Florence, Translator)

**Input line (N26 Italy CSV):**
`2025-05-20,STRIPE,,,STRIPE PAYOUT,22000.00,,,`

**Reasoning:**
Stripe payout EUR 22,000 (net of fees). Luca is a translator using Stripe for international clients. Gross-up: Stripe collected approximately EUR 22,660; fees ~EUR 660. For income tax, gross receipts = EUR 22,660. Stripe fee deductible for regime ordinario filers.

**Classification:** Gross receipts EUR 22,660. Stripe fees EUR 660 deductible.

### Example 5 -- Hype Business (Naples, E-commerce)

**Input line (Hype Business statement):**
`2025-07-15;SUMUP PAYOUT;ENTRATA;15.000,00`

**Reasoning:**
SumUp card terminal settlement EUR 15,000. Anna is an e-commerce seller. If e-commerce generates redditi d'impresa, Quadro RE does NOT apply -- Quadro RF (impresa) applies. Flag immediately to confirm lavoro autonomo vs impresa individuale.

**Classification:** Gross receipts EUR 15,000. RED FLAG: confirm lavoro autonomo vs impresa before filing Quadro RE.

### Example 6 -- BancoBPM (Bergamo, Architect -- Inarcassa Member)

**Input line (BancoBPM PDF):**
`20/04/2025 | BONIFICO DA STUDIO ARCHITETTURA XYZ | AVERE EUR 8,500.00`

**Reasoning:**
Roberto is an architect enrolled in Inarcassa. Gestione Separata does NOT apply. Inarcassa rate differs (~14.5% subjective + 4% integrative). Collect Inarcassa annual statement for exact contribution amounts. Revenue EUR 8,500 added to gross receipts.

**Classification:** Gross receipts EUR 8,500. Flag: Inarcassa member -- use cassa rates, not Gestione Separata.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Cash Basis for Freelancers

**Legislation:** Art. 54 TUIR

Italian freelancers (liberi professionisti) use the cassa (cash) principle: income is taxed when received, expenses are deductible when paid. Invoice date is irrelevant for timing.

### 5.2 INPS Gestione Separata Deductibility

All INPS Gestione Separata contributions paid in the fiscal year are 100% deductible from professional income. This reduces taxable income before applying IRPEF brackets. Apply without escalating.

### 5.3 Telecoms 80% Cap

**Legislation:** Art. 54 TUIR

All telephone and internet expenses -- mobile, fixed, broadband -- are subject to a statutory 80% deductibility cap. Apply 80% to all telecom narrations without exception.

### 5.4 Vehicles 20% Cap

**Legislation:** Art. 164 TUIR

Car purchase, hire, lease, fuel, and maintenance are capped at 20% deductibility for professionals. Exception: vehicles exclusively assigned to employees (100%) -- flag for reviewer.

### 5.5 Equipment Threshold (Beni Strumentali)

Assets costing <= EUR 516.46 (unit cost) may be fully expensed in year of purchase. Assets > EUR 516.46 must be depreciated over their useful life using the Ministerial ammortamento table (DM 31/12/1988). Never fully expense assets > EUR 516.46 in year 1.

### 5.6 IVA (VAT) Not Included in Income or Expenses

Amounts subject to IVA: strip IVA before computing professional income. Gross receipts = invoiced amount ex-IVA. Deductible expenses = cost ex-IVA. Do not double-count IVA.

### 5.7 F24 Tax Payments Are Not Deductible

IRPEF (saldo and acconti), addizionali, and IVA paid via F24 are tax payments, not business expenses. Never include F24 tax payments as deductible expenses.

### 5.8 Hospitality (Meals/Accommodation) 75% Cap

**Legislation:** Art. 109 TUIR

Restaurant, hotel, and entertainment expenses incurred for professional purposes are capped at 75% deductibility. Strictly social meals are 0% deductible.

### 5.9 Tax Computation Flow

```
Gross professional receipts (ex-IVA, cash basis)
Less: Deductible expenses (including INPS Gestione Separata / cassa)
= Net professional income (Quadro RE, line RE23)
Apply IRPEF bracket rates
= IRPEF gross
Less: Detrazione per lavoro autonomo
Less: Ritenute d'acconto (withheld by clients)
Less: Acconti IRPEF paid (F24)
= IRPEF balance due / (refund)
Plus: Addizionale regionale (% x net income)
Plus: Addizionale comunale (% x net income)
= Total tax
```

### 5.10 Filing Deadlines

| Item | Deadline |
|---|---|
| Modello Redditi PF (online) | 30 June of following year |
| IRPEF saldo + 1st acconto (40%) | 30 June |
| 2nd acconto IRPEF (60%) | 30 November |
| Modello 730 (via sostituto) | 30 November |

### 5.11 Penalties

| Offence | Penalty |
|---|---|
| Late filing (within 90 days) | EUR 250 reduced sanction |
| Late filing (> 90 days) | 120%-240% of tax due |
| Under-reporting (infedele dichiarazione) | 90%-180% of additional tax |
| Late payment | 30% of unpaid amount (reduced if paid within 30 days: 15%) |
| Failure to issue invoice | 90%-180% of IVA evaded |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

Portion of rent/utilities attributable to professional use requires documented floor area calculation. Accept only dedicated professional space; estimate pro-rata if client provides layout.

### 6.2 Mixed-Use Vehicle (Auto ad Uso Promiscuo)

20% cap applies unless vehicle is exclusively professional or employee-assigned. Default to 20%; upgrade only with written assignment evidence.

### 6.3 Regime Ordinario vs Regime Forfettario Comparison

Client approaching EUR 85,000 threshold or asking which is better. Present both calculations; do not recommend -- flag for commercialista.

### 6.4 Cassa Previdenziale Contributions (Inarcassa, ENPAM, etc.)

Rates differ by profession and year. Not standard Gestione Separata. Collect annual cassa statement; do not estimate.

### 6.5 Rappresentanza (Entertainment/Promotional) Expenses

Deductible at 75% if < 1% of revenues. Above 1% may be disallowed. Flag if total entertainment > 1% of gross.

### 6.6 Foreign Client Compensation

Withholding tax may apply. Foreign tax credit possible. Requires double-tax treaty analysis. Flag and escalate.

### 6.7 Crypto Income or NFT Sales

Italian treatment evolving -- imposta sostitutiva 26% on gains. Separate from professional income. Flag -- do not include in Quadro RE; separate Quadro RT/RW treatment.

### 6.8 Occasional Work (Lavoro Autonomo Occasionale)

Occasional work < EUR 5,000/year: no INPS obligation, different withholding rules. Confirm habitual/occasional status before applying INPS.

---

## Section 7 -- Excel Working Paper Template

```
ITALIAN INCOME TAX WORKING PAPER (REGIME ORDINARIO)
Taxpayer: _______________  CF: _______________  FY: 2025  Region: _______________

SECTION A -- INCOME (Quadro RE)
                                        EUR
Gross professional receipts             ___________
Less: returned amounts/refunds          (__________)
Net receipts                            ___________

SECTION B -- DEDUCTIBLE EXPENSES
Rent (professional portion)             ___________
Utilities (professional portion)        ___________
Telecoms (80% of total)                ___________
Software subscriptions                  ___________
Professional fees (commercialista etc.) ___________
Legal fees                              ___________
Training / CPD                          ___________
Travel (trains, flights -- professional) ___________
Accommodation & meals (75%)            ___________
Professional insurance                  ___________
Bank charges                            ___________
Capital allowances (ammortamento)       ___________
INPS Gestione Separata / Cassa         ___________
Payment processor fees                  ___________
Other deductible expenses               ___________
TOTAL DEDUCTIBLE EXPENSES               ___________

SECTION C -- NET INCOME (Quadro RE, line RE23)
Net professional income (A - B)         ___________

SECTION D -- IRPEF COMPUTATION
IRPEF gross (bracket calculation)       ___________
Less: Detrazione lavoro autonomo        (___________)
IRPEF net                               ___________
Less: ritenute d'acconto withheld       (___________)
Less: acconti paid (F24)               (___________)
IRPEF balance due / (refund)            ___________

SECTION E -- ADDIZIONALI
Addizionale regionale (___%)           ___________
Addizionale comunale (___%)            ___________
Total addizionali                       ___________

SECTION F -- INPS GESTIONE SEPARATA
Net income x 26.07% (or cassa rate)    ___________
Less: advance contributions paid        (___________)
INPS balance due                        ___________

SECTION G -- REVIEWER FLAGS
[ ] Regime forfettario threshold check (< EUR 85,000?)
[ ] Vehicle deduction -- 20% cap applied?
[ ] Equipment > EUR 516.46 -- depreciation schedule used?
[ ] Telecoms -- 80% cap applied?
[ ] Hospitality -- 75% cap applied?
[ ] Home office -- documented floor area?
[ ] Acconto payments verified against F24 receipts
[ ] IVA stripped from all amounts
[ ] Cassa previdenziale or Gestione Separata confirmed?
```

---

## Section 8 -- Bank Statement Reading Guide

### Italian Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| Intesa Sanpaolo | CSV (semicolon) | Data movimento; Valuta; Descrizione; Dare (debit); Avere (credit) |
| UniCredit | CSV / PDF | Data; Descrizione operazione; Dare; Avere; Saldo |
| BancoBPM | PDF / Excel | Data; Causale; Importo Dare; Importo Avere |
| FinecoBank | CSV | Data; Entrata; Uscita; Descrizione; Tipo |
| N26 Italy | CSV (app export) | Date,Payee,Account number,Transaction type,Payment reference,Amount (EUR) |
| Hype Business | CSV | Data;Descrizione;Importo;Tipo (ENTRATA/USCITA) |
| Revolut Italy | CSV | Type,Product,Started Date,Completed Date,Description,Amount,Fee,Currency,State |

### Key Italian Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| BONIFICO DA [sender] | Wire transfer credit | Professional income |
| ACCREDITO BONIFICO SEPA | SEPA credit transfer | Income |
| VB DA [sender] | UniCredit credit notation | Income |
| BONIFICO A FAVORE [payee] | Wire transfer debit | Expense |
| ADDEBITO | Direct debit | Recurring expense |
| PAGAMENTO F24 | Tax payment | Exclude (tax payment) |
| NEXI PAGAMENTI | Card terminal settlement | Income (merchant) |
| INTERESSI ATTIVI | Interest earned | Other income |
| CANONE CONTO | Account maintenance fee | Bank charges (deductible) |

### Amount Format Notes

- Italian banks: thousands separator = `.`, decimal = `,` (e.g., `1.234,56`)
- N26 Italy: period decimal, no thousands separator (e.g., `1234.56`) -- opposite of Italian banks
- FinecoBank: comma decimal, no thousands separator
- Date format: DD/MM/YYYY (Italian banks); YYYY-MM-DD (N26)
- Revolut: filter `State = COMPLETED` only

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all BONIFICO DA / VB DA credits from SRL/SPA entities as potential professional income
2. Identify all F24 payments -- these are tax payments, NOT expenses
3. Identify all INPS contributions -- these ARE deductible
4. Apply conservative defaults: Gestione Separata 26.07%, regional addizionale 1.23%, municipal 0%
5. Flag all telecom expenses at 80%, hospitality at 75%, vehicles at 20%
6. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- ITALY INCOME TAX (IRPEF REGIME ORDINARIO)
1. Regime fiscale: regime ordinario or forfettario? (Gross receipts in 2024?)
2. Regione e comune di residenza fiscale al 31 dicembre 2025?
3. Iscritto a una cassa previdenziale (ENPAM, Inarcassa, etc.) o Gestione Separata INPS?
4. Rivalsa INPS 4% applicata nelle fatture?
5. Totale fatturato lordo 2025 (ex-IVA)?
6. Acconti IRPEF versati con F24 nel 2025?
7. Contributi INPS versati nel 2025?
8. Familiari a carico (coniuge, figli) per detrazioni?
9. Auto utilizzata per lavoro? Se si, quale percentuale di utilizzo professionale?
10. Ufficio dedicato a casa o locale professionale esterno?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Professional income (lavoro autonomo) | TUIR Art. 53 |
| Deductible expenses | TUIR Art. 54 |
| Telecoms 80% cap | TUIR Art. 54(3-bis) |
| Vehicle expenses 20% cap | TUIR Art. 164 |
| Hospitality 75% cap | TUIR Art. 109(5) |
| IRPEF brackets | TUIR Art. 11 |
| Detrazioni per lavoro autonomo | TUIR Art. 13 |
| Addizionale regionale | D.Lgs. 446/1997 Art. 50 |
| Ammortamento table | DM 31/12/1988 |

### Known Gaps / Out of Scope

- Regime forfettario (separate skill)
- Corporate taxation (IRES/IRAP)
- Non-resident Italian-source income
- Capital gains (plusvalenze)
- Crypto / NFT taxation
- Redditi fondiari (rental income)

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Italian bank formats (Intesa, UniCredit, FinecoBank, N26, Hype); transaction pattern library; Nexi/Satispay patterns; worked examples; PROHIBITIONS and disclaimer added |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Cash basis (principio di cassa) applied -- income taxed when received?
- [ ] Telecoms capped at 80%?
- [ ] Vehicles capped at 20%?
- [ ] Hospitality (meals/accommodation) capped at 75%?
- [ ] Equipment > EUR 516.46 depreciated, not expensed?
- [ ] IVA stripped from all amounts?
- [ ] INPS contributions deducted from income before IRPEF?
- [ ] F24 tax payments excluded from expenses?
- [ ] Addizionali computed on correct taxable base?
- [ ] Detrazioni computed as tax credits (not income deductions)?

---

## PROHIBITIONS

- NEVER apply regime forfettario rules in this skill -- this skill covers regime ordinario only
- NEVER deduct more than 80% of telecom expenses (Art. 54 TUIR hard cap)
- NEVER deduct more than 20% of vehicle expenses for professionals (Art. 164 TUIR)
- NEVER deduct more than 75% of hospitality expenses (meals, accommodation)
- NEVER fully expense assets > EUR 516.46 -- apply ammortamento depreciation schedule
- NEVER include F24 tax payments (IRPEF, addizionali, IVA) as deductible expenses
- NEVER include IVA in income or expense figures -- always strip IVA first
- NEVER apply income-basis (competenza) for freelancers -- Italy uses cash basis (cassa)
- NEVER assume Gestione Separata for professionals enrolled in a cassa previdenziale
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Commercialista for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Commercialista, Consulente del Lavoro, or equivalent licensed practitioner in Italy) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
