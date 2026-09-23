---
name: it-income-tax
description: Use this skill whenever asked about Italian income tax for self-employed individuals (lavoratori autonomi, liberi professionisti) under regime ordinario. Trigger on phrases like "Modello Redditi PF", "Quadro RE", "IRPEF", "redditi di lavoro autonomo", "imposta sul reddito Italy", "deduzioni", "detrazioni", "addizionale regionale", "addizionale comunale", "regime ordinario", "acconti IRPEF", "no tax area", "INPS Gestione Separata", "rivalsa INPS", or any question about filing or computing income tax for an Italian freelancer or professional. Also trigger when preparing or reviewing a Modello Redditi PF, computing deductions, or advising on regime ordinario tax obligations. This skill covers progressive IRPEF brackets, deduzioni, detrazioni, addizionali, acconti, Quadro RE structure, rivalsa INPS, and penalties. ALWAYS read this skill before touching any Italian income tax work. Does NOT cover regime forfettario -- see it-regime-forfettario.md.
version: 2.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian income tax (IRPEF) for the self-employed: regime ordinario, with the forfettario test

How Italy taxes one self-employed professional under IRPEF: rates, surcharges, expense rules, INPS gestione separata, acconti, the return and penalties, plus the test for the forfettario (flat-rate) regime that replaces all of this when it applies. Figures are for tax year 2026. Italy's tax year is the calendar year: 2026 income is declared in 2027. For 2026 income the old TUIR (D.P.R. 917/1986) applies. The new TUIR (D.Lgs. 117/2026) applies only from 1° gennaio 2027 (art. 377), so Normattiva can show old articles as repealed; statutes here were read as in force on 30 June 2026. Two sources carry another year: the Agenzia rate page (13 January 2026) gives the 2026 change only in a note; the 730 pages are the 2026 edition, for 2025 income. The 2026 detrazioni for self-employed income are not printed here (no allowed page read proves them); the cuneo fiscale applies to employees only and is in `italy-payroll`.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Italy |
| Tax | IRPEF plus addizionale regionale and addizionale comunale |
| Currency | EUR only |
| Tax year | Calendar year |
| Primary legislation | TUIR, D.P.R. 917/1986, for 2026 income. New TUIR (D.Lgs. 117/2026) from 1 January 2027 |
| Tax authority | Agenzia delle Entrate |
| Return (professional with VAT number) | Modello Redditi PF online by 31 October of the following year. Not the 730 |
| Status | Drafted from the official pages. No accountant has reviewed it yet |

### IRPEF Brackets 2025 (Regime Ordinario) [T1]

The 2025 table is replaced. For 2026 the bracket limits are unchanged and the middle rate falls. The Agenzia table still shows the old middle rate; only its note gives the 2026 one.

**IRPEF bracket limits 2026 (TUIR art. 11)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig= |
| Top of the first bracket of taxable income | EUR 28,000 | "a) fino a 28.000 euro, 23 per cento" |
| Top of the second bracket | EUR 50,000 | "fino a 50.000 euro" |

**IRPEF rates 2026 (Agenzia delle Entrate)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef |
| First bracket | 23% | "sull’intero importo" |
| Second bracket, from 2026 income | 33% | "dal 35 al 33 per cento" |
| Old second-bracket rate, 2024 and 2025 only. Not for 2026 | 35% | "Dall’anno 2024" |
| Above the second bracket | 43% | "sul reddito eccedente i 50.000 euro" |
| Gross tax on the first EUR 50,000 at 2026 rates | EUR 13,700 | "pari a 13.700 euro" |

**High-income offset (L. 199/2025 art. 1 comma 4, TUIR D.P.R. 917/1986 art. 16-ter(5-bis))**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199 |
| Total income (reddito complessivo) above which it applies | EUR 200,000 | "reddito complessivo superiore a 200.000 euro" |
| Cut to the detrazioni for certain expenses (oneri) | EUR 440 | "pari a 440 euro" |

- **Tax formula.** Each rate applies only to income inside its bracket. Above the second limit: the Agenzia amount in the table plus the top rate on the excess. Taxable income = total income less oneri deducibili.
- **The offset** is a flat cut to the detrazioni for the oneri the law lists (mainly the 19 per cento items, not medical costs). It is not a surcharge.
- **No-tax area.** The live Guide's income level with no IRPEF comes from the detrazioni, which could not be proven for 2026. Removed.

**Cap on detrazioni for oneri (TUIR art. 16-ter, L. 207/2024 art. 1 comma 10)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207 |
| Total income above which the cap applies | EUR 75,000 | "reddito complessivo superiore a 75.000 euro" |
| Total income at which the base amount drops | EUR 100,000 | "non superiore a 100.000 euro" |
| Base amount, income above 75,000 up to 100,000 | EUR 14,000 | "a) 14.000 euro" |
| Base amount, income above 100,000 | EUR 8,000 | "b) 8.000 euro" |
| Family coefficient, no qualifying children | 0,50 | "a) 0,50, se nel nucleo familiare non sono presenti figli" |

- **The cap.** Above the first limit, oneri and expenses giving a detrazione count only up to the base amount times a family coefficient (TUIR art. 16-ter(3): see the table for no qualifying children; higher with children). Some items are left out (art. 16-ter(4)). The offset above applies after this cap.

### Addizionali (Regional + Municipal Surtaxes) [T1]

**Addizionale regionale (D.Lgs. 68/2011 art. 6)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-06-30 |
| Base rate | 1.23% | "pari a 1,23 per cento" |

- **The region sets its own rate.** An ordinary-statute region may raise or lower the base rate by law; from 2015 the rise may not exceed 2.1 percentage points ("a 2,1 punti percentuali a decorrere dall'anno 2015"). Many regions use bands. Special-statute regions have their own rules.
- **Addizionale comunale.** Each comune decides; the variation may not exceed 0.8 percentage points in total, and the comune may set an exemption threshold (D.Lgs. 360/1998 art. 1). The live Guide's upper figure for comuni was not proven and is removed.
- **Base.** Both apply to taxable income (after oneri deducibili, before detrazioni), and the comunale is due only if net IRPEF is due for the same year (D.Lgs. 360/1998 art. 1(4)); treat the regionale the same way and confirm. Forfettario income is not subject to them.

### Detrazioni per Lavoro Autonomo (Reduce Tax Payable) [T1]

**No allowed page read prints the 2026 detrazioni amounts**, so none are given. The Agenzia IRPEF page (link above) says detrazioni are subtracted from gross tax, not income, capped at tax due, with no refund; non-residents get only some unless "Schumacker" conditions are met. Take the 2026 amounts from TUIR art. 13 and the 2027 Redditi instructions.

### INPS Gestione Separata (Social Contributions) [T1]

**INPS gestione separata 2026 (Circolare n. 8 of 3 February 2026)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf |
| Professionals with a VAT number and no other compulsory cover | 26.07% | "Soggetti non assicurati presso altra forma" |
| Pensioners, or insured with another compulsory scheme | 24% | "l’aliquota è confermata" |
| Maximum income on which contributions are due | EUR 122,295 | "è pari a 122.295,00 euro" |
| Income needed for a fully credited year (not a minimum payment) | EUR 18,808 | "è pari a 18.808,00 euro" |
| Contribution at the full rate for a fully credited year | EUR 4,903.25 | "4.903,25 euro" |

- **Which rate.** A member of a profession's own fund (cassa: Inarcassa, ENPAM and others) pays that fund, not the gestione separata. The live Guide wrongly used the lower rate for cassa members.
- Contributions are due on net professional income up to the cap in the table (the live Guide used the 2025 cap).
- **Rivalsa INPS.** A professional without a cassa may charge the client a rivalsa (L. 662/1996 art. 1 comma 212). The Agenzia withholding page treats this charge as part of the fee, subject to withholding; a cassa contribution charged to the client is not income (Section 5.1). The page is undated; confirm after D.Lgs. 192/2024. More: `it-inps-contributions`.

### Acconti IRPEF (Advance Payments) [T1]

**Payments on account (Agenzia, "Come si paga l'Irpef", 12 March 2026)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef |
| No acconto unless the tax declared, after detrazioni, credits and withholdings, is above | EUR 51.65 | "superiore a 51,65 euro" |
| Acconto as a share of last year's tax (or of the lower tax expected) | 100% | "dell’imposta dichiarata nell’anno" |
| Below this: one payment by 30 November | EUR 257.52 | "se l’acconto è inferiore a 257,52 euro" |
| First instalment, 30 June, with last year's balance | 40% | "entro il 30 giugno" |
| Second instalment, 30 November | 60% | "entro il 30 novembre" |
| ISA and forfettario taxpayers: one payment by 30 November if the total is not above | EUR 206 | "non supera 206 euro" |
| Surcharge for paying balance and first acconto in the 30 days after 30 June | 0.40% | "pagando una maggiorazione" |

ISA and forfettario taxpayers otherwise pay two EQUAL instalments on the same dates. Check whether the professional's activity is subject to ISA before using this rule. Payments go by F24.

### Forfettario or ordinario: which regime applies [T1]

Decide this first. A forfettario taxpayer pays one substitute tax instead of IRPEF and the surcharges, and the rest of this Guide does not apply.

**Forfettario rules (Agenzia delle Entrate, 21 July 2026)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |
| Entry: PREVIOUS-year revenue or fees, annualised, all ATECO codes together, not above | EUR 85,000 | "ragguagliati ad anno, non superiori a 85.000 euro" |
| Exit in the SAME year once revenue or fees go over | EUR 100,000 | "dallo stesso anno" |
| Entry: previous-year gross spending on staff and collaborators not above | EUR 20,000 | "20.000 euro lordi" |
| Exclusion: previous-year employment income above (standing rule) | EUR 30,000 | "superiore a 30.000 euro" |
| The same limit for the years 2025 and 2026 | EUR 35,000 | "elevato a 35.000 euro" |
| Substitute tax (replaces IRPEF and both surcharges) | 15% | "sostitutiva" |
| Start-up rate, first five years, if conditions are met | 5% | "per i primi cinque anni" |
| EU or EEA non-resident: share of total income that must arise in Italy | 75% | "producono in Italia almeno" |

**Profitability coefficients (L. 145/2018 allegato 2, Agenzia copy)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/241208/allegato+4.pdf/d69be7fc-b18a-3c73-bd2e-b0f3c1970218 |
| Professional, scientific, technical, health, education, financial services | 78% | Allegato 2 |
| Other activities (includes IT services) | 67% | Allegato 2 |

- **Two limits, not one.** Over the entry limit, the regime ends the FOLLOWING year; over the higher limit, it ends the SAME year, with VAT due from the crossing sale.
- **Employment income** is tested on the previous year, unless that job ended then. The raised limit is "for the years 2025 and 2026"; for the regime in 2027 the standing limit returns unless extended by law.
- **Other exclusions** (same page) include a related partnership stake or S.r.l. control, and working mainly for a current or recent employer.
- **Taxable income** = revenue times coefficient, less compulsory contributions. No actual costs. Forfettari are not subject to the fee withholding (Section 5.9).

### Conservative Defaults [T1]

| Situation | Default Assumption |
| --- | --- |
| Regional surtax unknown | Base rate from the regional table, flagged. It is not a minimum |
| Municipal surtax unknown | None, flagged for the client |
| Cassa membership unknown | Full gestione separata rate from the INPS table, flagged |
| Rivalsa INPS on invoices unclear | Do NOT assume one was added. Ask |
| Deductible or not disputed | Non-deductible. Flag |
| Payment received: unclear if taxable | Taxable. Flag |
| Invoice date vs payment date | Cash basis (Section 5.1) |
| Refund or reimbursement | Not income if charged analytically to the client (TUIR art. 54(2)(b)); otherwise taxable |

### Red Flag Thresholds [T1]

**Cash limit (D.Lgs. 231/2007 art. 49)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art49!vig=2026-06-30 |
| Cash transfers between different persons prohibited at or above, from 1 January 2023 | EUR 5,000 | "alla cifra di ((5.000 euro))" |

| Flag | Threshold |
| --- | --- |
| Previous-year receipts at or below EUR 85,000 | Forfettario? Check before using this Guide |
| INPS contributions far below the INPS table rate on net income | Possible error. Review |
| No acconto payments recorded | Check whether acconti were due |
| Cash payments at or above EUR 5,000 | Cash limit. Flag |
| Any expense with no documentation | Reject |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable.** Full-year bank statement (CSV, PDF or text). Regime (ordinario or forfettario), region and comune.
- **Recommended.** Invoices issued, F24 receipts (acconti IRPEF and INPS), gestione separata or cassa statements, last year's Modello Redditi.
- **Ideal.** Complete books, asset register with depreciation, invoices received, family details (for detrazioni).

### Refusal Catalogue

- **R-IT-1.** Only bank totals, no itemised expenses. "Request an itemised expense list with F24 forms and receipts first."
- **R-IT-2.** Both regimes in one year. Happens only if forfettario receipts cross the same-year exit limit in the forfettario table. Otherwise "Verify which regime applies and for which period."
- **R-IT-3.** Previous-year receipts above the forfettario entry limit, but the client claims the regime this year. "The regime ended from this year. Proceed under regime ordinario." Crossing it this year ends the regime next year, unless the same-year limit was also crossed.
- **R-IT-4.** Non-resident claiming full detrazioni. "Restricted for non-residents. Clarify residency and escalate."
- **R-IT-5.** Private vehicle without a usage log. "Nothing beyond the capped share in art. 164 TUIR."

## Section 3: Transaction Pattern Library

Pre-classifier: apply the treatment when a bank line matches, else use Section 5, whose tables give the percentages.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| BONIFICO DA [client name] | Professional receipts | Revenue | SEPA credit from client |
| VB DA [client name] / VB ENTRATA | Professional receipts | Revenue | UniCredit/BancoBPM notation |
| ACCREDITO DA [client] | Professional receipts | Revenue | Generic credit |
| STRIPE PAYMENTS EUROPE / STRIPE PAYOUT | Receipts, online | Revenue | Gross up; fee deductible |
| PAYPAL TRANSFER / PAYPAL ACCREDITO | Receipts | Revenue | Gross up; fee deductible |
| SATISPAY BUSINESS PAYOUT | Receipts | Revenue | Fee deductible |
| NEXI PAGAMENTI / NEXI POS VERSAMENTO | Receipts, card | Revenue | Gross up |
| SUMUP PAYOUT / ZETTLE PAYOUT | Receipts, card | Revenue | Gross up |
| REVERSALE [client] / RIMESSA CLIENTI | Receipts | Revenue | Public body or factoring |
| RIVALSA INPS (portion of invoice) | In receipts | Revenue | Legacy treatment; see Section 1, INPS |
| INTERESSI ATTIVI / INTERESSI MATURATI | Capital income | NOT professional | TUIR art. 54(3-bis) |
| RIMBORSO SPESE [client] | Not income if charged analytically | Flag | Section 5.1 |
| STIPENDIO / SALARIO [employer] | Employment income | NOT professional | Separate head |

### 3.2 Expense Patterns (Debits)

| Pattern | Tax Category | Treatment | Notes |
| --- | --- | --- | --- |
| AFFITTO UFFICIO / CANONE LOCAZIONE / PIGIONE | Rent | Full if used only for work | Home also lived in: 50%, only with no other office in the comune |
| ENEL / ENI PLENITUDE / A2A ENERGIA | Utilities, premises used both ways | 50% | Full only for work-only premises |
| TELECOM ITALIA / TIM FIBRA / FASTWEB / WIND3 | Telecoms | 80% | Art. 54-quinquies(4) |
| VODAFONE MOBILE / TIM MOBILE / ILIAD | Mobile | 80% | Same |
| ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE | Software | Full | |
| COMMERCIALISTA / CONSULENTE FISCALE / STUDIO [name] | Professional fees | Full | |
| AVVOCATO / NOTAIO | Legal fees | Full if professional | Flag personal matters |
| TRENITALIA / ITALO / FRECCIAROSSA | Travel | Full if professional | In Italy, traceable payment only |
| RYANAIR / EASYJET / ITA AIRWAYS / ALITALIA | Air travel | Full if professional | Itinerary and purpose |
| HOTEL / AGODA / BOOKING.COM | Accommodation | 75%, within fee cap | Art. 54-septies(1) |
| RISTORANTE / PIZZERIA / CAFFE | Meals | 75%, within fee cap | Social meals: none |
| INPS F24 / CONTRIBUTI GESTIONE SEPARATA | Social contributions | Deduct from total income | Oneri deducibili, not a work cost |
| F24 ACCONTO IRPEF / F24 SALDO IRPEF | Tax | NOT deductible | |
| ASSICURAZIONE PROFESSIONALE / RC PROFESSIONALE | Insurance | Full | |
| ADDIZIONALE REGIONALE / ADDIZIONALE COMUNALE | Tax | EXCLUDE | |
| SPESE BANCARIE / COMMISSIONI BANCARIE / CANONE CONTO | Bank fees | Full | |
| AMORTAMENTO / BENE STRUMENTALE | Asset | Depreciate | Section 5.5 |
| AUTONOLEGGIO / NOLEGGIO AUTO | Car hire | 20% | Art. 164, one vehicle |
| CARBURANTE / ENI / Q8 / SHELL | Fuel | 20% | Traceable payment |
| FORMAZIONE / CORSO / SEMINARIO | Training | Full up to yearly cap | Art. 54-septies(3) |
| CANCELLERIA / MATERIALE UFFICIO / UNIEURO (office) | Supplies | Full | |
| CONTRIBUTO CASSA [profession] / ENPAM / INARCASSA | Cassa contributions | Deduct from total income | Replaces gestione separata |
| STRIPE FEE / PAYPAL FEE / SATISPAY FEE | Processor fees | Full | |

## Section 4: Worked Examples

Bank amounts are sample data in the bank's own format.

### Example 1: Intesa Sanpaolo (Milan, Graphic Designer)

`03/01/2026;;BONIFICO DA STUDIO GAMBA SRL;;3.500,00`

Client credit. No cassa: full gestione separata rate. Quadro RE, cash basis, net of IVA. **Classification:** professional receipt.

### Example 2: UniCredit (Turin, IT Consultant)

`10/01/2026 | VB DA ACCENTURE SRL | AVERE | 6.500,00`

Monthly fee from one client. Check it is not a recent employer and no forfettario applies. **Classification:** professional receipt; flag single-client concentration.

### Example 3: FinecoBank (Rome, Photographer)

`15/03/2026;NEXI POS VERSAMENTO;Entrata;7.000,00`

Net of fees: gross up from the portal; fee deductible. **Classification:** receipt at the gross amount.

### Example 4: N26 Italy (Florence, Translator)

`2026-05-20,STRIPE,,,STRIPE PAYOUT,22000.00,,,`

Net of fees: the receipt is the gross in the Stripe report; fee deductible. **Classification:** receipt at the gross amount.

### Example 5: Hype Business (Naples, E-commerce)

`2026-07-15;SUMUP PAYOUT;ENTRATA;15.000,00`

Selling goods online is business income (reddito d'impresa): Quadro RF or RG, not RE. **Classification:** RED FLAG, confirm lavoro autonomo or impresa before filing.

### Example 6: BancoBPM (Bergamo, Architect: Inarcassa Member)

`20/04/2026 | BONIFICO DA STUDIO ARCHITETTURA XYZ | AVERE | 8.500,00`

Inarcassa member: no gestione separata. Inarcassa's rates are on no allowed page; use his fund statement. **Classification:** professional receipt; flag cassa.

## Section 5: Tier 1 Rules (When Data Is Clear)

Expense rules are TUIR art. 54 to 54-octies as rewritten by D.Lgs. 192/2024, read as in force on 30 June 2026.

**Expense limits (TUIR art. 54-quinquies)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30 |
| Unit cost up to which an asset is deducted in full in the year bought | EUR 516.40 | "euro 516,40" |
| Goods (not vehicles) and premises used both for work and privately | 50% | "nella misura del 50 per cento" |
| Telecom terminal equipment and its use | 80% | "dell'80 per cento" |

**Other limits (TUIR art. 54-septies)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54septies!vig=2026-06-30 |
| Hotel and meals: deductible share | 75% | "del 75 per cento" |
| Hotel and meals: overall cap, share of fees received in the year | 2% | "al 2 per cento" |
| Rappresentanza: cap, share of fees received | 1% | "dell'1 per cento" |
| Training, masters, conferences, with travel and stay: yearly cap | EUR 10,000 | "10.000 euro" |

**Vehicles (TUIR art. 164)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30 |
| Individual professional: one vehicle only | 20% | "un solo veicolo" |
| Sales agents and representatives | 80% | "attività di agenzia" |
| Vehicles given to employees for mixed use most of the year | 70% | "uso promiscuo" |

### 5.1 Cash Basis for Freelancers

- Income = everything received in the year for the profession, less costs paid that year (TUIR art. 54(1)). A fee from a withholding agent received in the next year counts in the year the agent had to withhold.
- **Not income** (art. 54(2)): contributions that the law itself puts on the client, such as the cassa contributo integrativo; job expenses charged analytically to the client; recharges of shared office costs. The optional gestione separata rivalsa is part of the fee, subject to withholding (Section 1, INPS).
- **Traceable payment.** Meals, lodging, travel and taxis in Italy are deductible only if paid by bank, post or another traceable method (art. 54-septies(6-bis)); a reimbursement of such costs paid otherwise is income (art. 54(2-bis)).

### 5.2 INPS Gestione Separata Deductibility

- Compulsory gestione separata or cassa contributions paid in the year are oneri deducibili, deducted from total income before the brackets (Agenzia IRPEF page).

### 5.3 Telecoms 80% Cap

- Telecom equipment and its running costs: the art. 54-quinquies(4) share (the live Guide cited art. 54).

### 5.4 Vehicles 20% Cap

- Individual professional: the art. 164 share, ONE vehicle. The cost cap is printed only in lire ("lire 35 milioni"). Fuel needs traceable payment.

### 5.5 Equipment Threshold (Beni Strumentali)

- An asset with unit cost not above EUR 516.40 is deducted in full in the year bought; above it, depreciate at no more than the ministerial coefficients, halved in year one (art. 54-quinquies(1)). The coefficient table (D.M. 31 December 1988) was not read.
- Mixed-use goods (not vehicles), and the rent and running costs of premises used both ways, are deducted at 50%; premises only if there is no other office in the same comune.

### 5.6 IVA (VAT) Not Included in Income or Expenses

- Strip IVA: receipts net of IVA, costs net of deductible IVA. See `italy-vat-return`.

### 5.7 F24 Tax Payments Are Not Deductible

- IRPEF (balance and acconti), surcharges and IVA paid by F24 are taxes, not costs.

### 5.8 Hospitality (Meals/Accommodation) 75% Cap

- The art. 54-septies(1) share, within the fee-linked cap; traceable payment in Italy; social meals none. The live Guide cited art. 109, the business rule.

### 5.9 Tax Computation Flow

**Withholding on fees (D.P.R. 600/1973 art. 25)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/aliquote-f24_rit_red_lav_aut |
| Withholding on account on fees paid to resident professionals | 20% | "la ritenuta, effettuata a titolo d’acconto, è pari al 20%" |

- **Flow.** Receipts less costs = net professional income (Quadro RE). Plus other income, less oneri deducibili (INPS or cassa) = taxable income. Brackets, less detrazioni = net IRPEF. Less withholdings and acconti = balance. Surcharges on taxable income.
- Normattiva's text of D.P.R. 600/1973 art. 25 still prints the original 1973 rate; later laws raised it, shown only in its notes. Use the rate in the table. Forfettari are not subject to this withholding.

### 5.10 Filing Deadlines

| Item | Deadline |
| --- | --- |
| Modello Redditi PF, online | 15 April to 31 October of the following year (D.P.R. 322/1998 art. 2(1)) |
| Modello Redditi PF on paper, post office (only where allowed) | 15 April to 30 June of the following year |
| IRPEF balance + first acconto | 30 June, or the next 30 days with the surcharge in the acconti table |
| Second or single acconto | 30 November |
| Modello 730 | Not for income needing a VAT number. The 2026 edition was due 30 September 2026 |

- A return filed within ninety days of the deadline is valid, but late penalties apply; later, it counts as not filed (art. 2(7)).
- The 730 covers employment and pension income and self-employed income needing no VAT number, such as occasional work. Pages: see Sources.

### 5.11 Penalties

**D.Lgs. 471/1997 art. 1, violations from 1 September 2024**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-06-30 |
| Return not filed: centoventi per cento (one hundred and twenty per cent) of the tax due, minimum | EUR 250 | "minimo di euro 250" |
| Return not filed, no tax due: from the minimum above up to (may be doubled for those who must keep accounts) | EUR 1,000 | "da euro 250 a euro 1.000" |
| Understated return (infedele): settanta per cento (seventy per cent) of the extra tax, minimum | EUR 150 | "minimo di euro 150" |

- **Late payment** (art. 13): venticinque per cento (twenty-five per cent) of each unpaid amount, halved up to ninety days late, less again up to fifteen days.
- The statute prints these rates only in words. The start date is in note 40 of art. 1. The live Guide's rates were pre-September 2024; invoice penalties are in `italy-vat-return`.

## Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- Home used also for work: the art. 54-quinquies share of rent (or rendita if owned) and running costs, only with no other office in the comune. Work-only premises: full.

### 6.2 Mixed-Use Vehicle (Auto ad Uso Promiscuo)

- Individual professional: the art. 164 share, one vehicle. Higher shares only for agents and employee cars, with evidence.

### 6.3 Regime Ordinario vs Regime Forfettario Comparison

- Near the forfettario limits: show both computations, do not recommend, flag.

### 6.4 Cassa Previdenziale Contributions (Inarcassa, ENPAM, etc.)

- Each fund sets its own rates, on no allowed page. Use the yearly statement; do not estimate.

### 6.5 Rappresentanza (Entertainment/Promotional) Expenses

- Deductible within the fee-linked cap in the art. 54-septies table, only if paid traceably. Gifts of goods and art objects count. Flag near the cap.

### 6.6 Foreign Client Compensation

- Foreign withholding and credit may apply; needs treaty analysis. Escalate. See `italy-transfer-pricing` for related-party pricing.

### 6.7 Crypto Income or NFT Sales

**Crypto (L. 199/2025)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199 |
| Substitute tax on crypto gains, 2026 | 33% | "ordinaria del 33 per cento" |
| Rate kept for euro e-money tokens | 26% | "del 26 per cento" |

- Taxed apart from professional income, never in Quadro RE. The live Guide's single rate is the pre-2026 one. See `italy-crypto-tax`.

### 6.8 Occasional Work (Lavoro Autonomo Occasionale)

**Occasional work and INPS (D.L. 269/2003 art. 44)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=2026-06-30 |
| Enrolment in the gestione separata only if yearly income from it is above | EUR 5,000 | "superiore ad euro 5.000" |

- An INPS threshold, not a tax exemption. Occasional work needs no VAT number and can go on the 730.

## Section 7: Excel Working Paper Template

~~~
ITALIAN INCOME TAX WORKING PAPER (REGIME ORDINARIO)
Taxpayer: ____ CF: ____ FY: 2026 Region: ____

A: INCOME (Quadro RE)
Gross professional receipts (net of IVA) ____

B: DEDUCTIBLE COSTS
Rent / utilities (professional portion) ____
Telecoms (80% of total) ____
Software, professional and legal fees ____
Training (within yearly cap) ____
Travel (professional) ____
Hotel and meals (75%, fee cap) ____
Insurance, bank charges, processor fees ____
Depreciation (ammortamento) ____
TOTAL COSTS ____

C: NET PROFESSIONAL INCOME (A less B) ____

D: IRPEF
Other income ____
Less: INPS gestione separata / cassa (____)
Taxable income ____
Gross IRPEF (brackets) ____
Less: detrazioni (____)
Less: ritenute d'acconto, acconti (F24) (____)
IRPEF balance / (refund) ____

E: ADDIZIONALI
Regionale (___%) + Comunale (___%) ____

F: INPS GESTIONE SEPARATA
Net income x 26.07% (or cassa rate) ____
Less: contributions already paid (____)

G: REVIEWER FLAGS
[ ] Forfettario test (previous year at or below EUR 85,000?)
[ ] Vehicle: 20% share, one vehicle?
[ ] Assets above EUR 516.40 depreciated?
[ ] Telecoms 80%, hotel and meals 75% and fee cap?
[ ] Travel and meals in Italy paid traceably?
[ ] Home office: no other office in the comune?
[ ] Acconti checked against F24; IVA stripped; cassa or gestione separata confirmed?
~~~

## Section 8: Bank Statement Reading Guide

### Italian Bank Statement Formats

| Bank | Format | Key Fields |
| --- | --- | --- |
| Intesa Sanpaolo | CSV (semicolon) | Data movimento; Valuta; Descrizione; Dare; Avere |
| UniCredit | CSV / PDF | Data; Descrizione operazione; Dare; Avere; Saldo |
| BancoBPM | PDF / Excel | Data; Causale; Importo Dare; Importo Avere |
| FinecoBank | CSV | Data; Entrata; Uscita; Descrizione; Tipo |
| N26 Italy | CSV (app export) | Date,Payee,Account number,Transaction type,Payment reference,Amount (EUR) |
| Hype Business | CSV | Data;Descrizione;Importo;Tipo (ENTRATA/USCITA) |
| Revolut Italy | CSV | Type,Product,Started Date,Completed Date,Description,Amount,Fee,Currency,State |

### Key Italian Banking Narrations

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| BONIFICO DA [sender] | Transfer in | Professional income |
| ACCREDITO BONIFICO SEPA | SEPA credit | Income |
| VB DA [sender] | UniCredit credit | Income |
| BONIFICO A FAVORE [payee] | Transfer out | Expense |
| ADDEBITO | Direct debit | Recurring expense |
| PAGAMENTO F24 | Tax payment | Exclude |
| NEXI PAGAMENTI | Card settlement | Income |
| INTERESSI ATTIVI | Interest | Capital income |
| CANONE CONTO | Account fee | Bank charges |

### Amount Format Notes

- Italian banks `1.234,56`; N26 `1234.56`; FinecoBank comma decimal, no thousands separator.
- Dates: DD/MM/YYYY (Italian banks); YYYY-MM-DD (N26). Revolut: keep `State = COMPLETED` rows only.

## Section 9: Onboarding Fallback

If the client cannot answer at once:

1. Treat credits from S.r.l. and S.p.A. clients as possible professional income.
2. F24 payments are taxes, NOT expenses; INPS contributions ARE deductible from total income.
3. Apply the conservative defaults (Section 1) and the Section 5 shares.
4. Produce the working paper with PENDING flags, and ask:

~~~
ONBOARDING QUESTIONS: ITALY IRPEF, REGIME ORDINARIO
1. Regime: ordinario o forfettario? Ricavi o compensi del 2025?
2. Regione e comune di residenza fiscale?
3. Cassa previdenziale o Gestione separata INPS? Gia pensionato?
4. Rivalsa INPS in fattura?
5. Compensi incassati nel 2026, al netto dell'IVA?
6. Acconti IRPEF e contributi INPS versati nel 2026?
7. Familiari a carico?
8. Auto usata per lavoro? Una sola?
9. Studio in casa? Altro studio nello stesso comune?
~~~

## Section 10: Reference Material

### Key Legislation

| Topic | Reference |
| --- | --- |
| Professional income | TUIR art. 53; art. 54 to 54-octies (D.Lgs. 192/2024) |
| Assets, mixed use, telecoms | TUIR art. 54-quinquies |
| Hotel, meals, rappresentanza, training | TUIR art. 54-septies |
| Vehicles | TUIR art. 164 |
| Brackets; high-income offset | TUIR art. 11 and art. 16-ter(5-bis), L. 199/2025 art. 1 commi 3-4 |
| Detrazioni | TUIR art. 13 |
| Surcharges | D.Lgs. 68/2011 art. 6; D.Lgs. 360/1998 art. 1 |
| Returns; withholding | D.P.R. 322/1998 art. 2; D.P.R. 600/1973 art. 25 |
| Penalties | D.Lgs. 471/1997 art. 1 and 13 |
| Depreciation coefficients | D.M. 31 December 1988 (not read) |
| New TUIR from 2027 | D.Lgs. 117/2026 art. 377 |

### Known Gaps / Out of Scope

- Forfettario beyond the test in Section 1; IRES and IRAP (`it-irap`); non-residents; capital gains; crypto (`italy-crypto-tax`); rental income; impatriati (`it-impatriati`); the 2026 detrazioni for self-employed income (not proven); employee payroll and the cuneo fiscale (`italy-payroll`)

### Changelog

| Version | Date | Change |
| --- | --- | --- |
| 3.0 | September 2026 | Tax year 2026 refresh against official pages; detrazioni table removed as unproven |
| 2.0 | April 2026 | Full rewrite: bank formats, pattern library, worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Forfettario ruled out first?
- [ ] Cash basis; IVA stripped; F24 taxes excluded?
- [ ] Telecom, vehicle (one), hotel and meal shares and the fee cap applied?
- [ ] Travel and meals in Italy paid traceably?
- [ ] Assets above the small-asset limit depreciated?
- [ ] Contributions deducted from total income before the brackets?
- [ ] 2026 middle rate, not the 2025 one?
- [ ] Surcharges at the region's and comune's own rates?
- [ ] Detrazioni treated as tax credits?

## The method, step by step

1. Test the forfettario conditions on the Agenzia forfettario page: previous-year figures for entry, this year's receipts for the same-year exit. If it applies, stop. (See Sources.)
2. Confirm professional income (TUIR art. 53) and find it on the cash basis under art. 54, applying art. 54-quinquies, 54-septies and the vehicle rule of art. 164.
3. Work out gestione separata from INPS Circolare n. 8/2026 (or use the cassa statement); deduct contributions paid from total income.
4. Apply TUIR art. 11 with the middle rate changed by L. 199/2025, then the detrazioni of art. 13, cut under art. 16-ter(5-bis) above its income limit.
5. Add the regional surcharge (base in D.Lgs. 68/2011 art. 6) and the municipal one at the local rates.
6. Subtract withholdings and acconti; set the new acconti; pay by F24 on 30 June and 30 November.
7. File the Modello Redditi PF online by 31 October of the following year (D.P.R. 322/1998 art. 2).

## Ask the client first

- Revenue or fees last year, and so far this year? (Forfettario entry and exit.)
- Employment or pension income last year, how much, and did the job end?
- Enrolled in a cassa, or only in the INPS gestione separata? Already a pensioner?
- Region and comune of tax residence?
- Total income likely above EUR 75,000 or EUR 200,000?
- Work from home, another office in the same comune, one car for work?

## When to refuse or refer

- Forfettario applies, or the same-year exit limit was crossed: refer for the forfettario return and the VAT.
- Business income (goods, e-commerce, trade), not a profession: Quadro RF or RG, outside this Guide.
- The 2026 detrazioni for self-employed income are needed: not carried here. Refer. Employee income and the cuneo fiscale: see `italy-payroll`.
- Non-residents, "Schumacker" claims, impatriati (`it-impatriati`), foreign income, treaties.
- Cassa rates, rivalsa disputes, penalties and ravvedimento.
- Anything to be filed: every computation here is an estimate for a commercialista to confirm.

## Sources

- Agenzia, amounts subject to withholding: https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/importi-su-cui-si-applica-la-ritenuta-f24_rit_red_lav_aut
- TUIR art. 11: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig=
- TUIR art. 54: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54!vig=2026-06-30
- TUIR art. 54-quinquies: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30
- TUIR art. 54-septies: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54septies!vig=2026-06-30
- TUIR art. 164: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30
- L. 199/2025: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199
- D.Lgs. 117/2026 art. 377: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117:1~art377
- D.Lgs. 68/2011 art. 6: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-06-30
- D.Lgs. 360/1998 art. 1: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-06-30
- D.P.R. 322/1998 art. 2: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30
- D.P.R. 600/1973 art. 25: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art25!vig=
- D.Lgs. 471/1997 art. 1: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-06-30
- D.Lgs. 471/1997 art. 13: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30
- D.L. 269/2003 art. 44: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=2026-06-30
- D.Lgs. 231/2007 art. 49: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art49!vig=2026-06-30
- Agenzia, IRPEF rates: https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef
- Agenzia, paying IRPEF: https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef
- Agenzia, forfettario: https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-
- Agenzia, forfettario coefficients: https://www.agenziaentrate.gov.it/portale/documents/20143/241208/allegato+4.pdf/d69be7fc-b18a-3c73-bd2e-b0f3c1970218
- Agenzia, 730/2026: https://www.agenziaentrate.gov.it/portale/730-2026/chi-puo-presentare-il-730 and https://www.agenziaentrate.gov.it/portale/quando-e-come-presentare-il-730-2026
- INPS Circolare n. 8/2026: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf

## PROHIBITIONS

- NEVER compute forfettario tax with this Guide; it gives only the test
- NEVER use the 2025 middle IRPEF rate for 2026, or the rate printed in the body of D.P.R. 600/1973 art. 25 as the withholding rate
- NEVER exceed the telecom, vehicle (one vehicle) or hotel and meal shares, or the fee-linked cap
- NEVER fully expense an asset above the small-asset limit
- NEVER deduct F24 tax payments, or include IVA in income or costs
- NEVER use the accruals basis for professionals
- NEVER assume gestione separata for a cassa member
- NEVER present a computation as final: label it an estimate for a commercialista

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Commercialista, Consulente del Lavoro, or equivalent licensed practitioner in Italy) before filing or acting upon.

> Contributed by OpenAccountants.

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
