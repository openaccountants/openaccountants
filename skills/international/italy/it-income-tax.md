---
name: it-income-tax
description: >
  Use this skill whenever asked about Italian income tax for self-employed individuals (lavoratori autonomi, liberi professionisti) under regime ordinario. Trigger on phrases like "Modello Redditi PF", "Quadro RE", "IRPEF", "redditi di lavoro autonomo", "imposta sul reddito Italy", "deduzioni", "detrazioni", "addizionale regionale", "addizionale comunale", "regime ordinario", "acconti IRPEF", "no tax area", "INPS Gestione Separata", "rivalsa INPS", or any question about filing or computing income tax for an Italian freelancer or professional. Also trigger when preparing or reviewing a Modello Redditi PF, computing deductions, or advising on regime ordinario tax obligations. This skill covers progressive IRPEF brackets, deduzioni, detrazioni, addizionali, acconti, Quadro RE structure, rivalsa INPS, and penalties. ALWAYS read this skill before touching any Italian income tax work. Does NOT cover regime forfettario — see it-regime-forfettario.md.
version: 2.0
---

# Italian Income Tax — Regime Ordinario (IRPEF) v2.0

## Section 1 — Quick Reference

### IRPEF Brackets 2025 (Regime Ordinario)

| Taxable Income (EUR) | Rate | Tax on Band | Cumulative Tax |
|---|---|---|---|
| 0 – 28,000 | 23% | 6,440 | 6,440 |
| 28,001 – 50,000 | 35% | 7,700 | 14,140 |
| Over 50,000 | 43% | on excess | 14,140 + 43% |

**Formula:** Tax = cumulative tax for lower bracket + (income − lower bracket threshold) × marginal rate

**No-tax area:** Detrazioni per lavoro autonomo reduce effective IRPEF to zero up to roughly EUR 4,800 net income (not a true zero-tax band — result of detrazioni calculation).

### Addizionali (Regional + Municipal Surtaxes)

| Surtax | Rate | Notes |
|---|---|---|
| Addizionale regionale | 1.23%–3.33% | Varies by region; default 1.23% if region not specified |
| Addizionale comunale | 0%–0.9% | Varies by municipality; zero in some comuni |

Apply both addizionali to the same taxable income (net income after deduzioni, before detrazioni).

### Detrazioni per Lavoro Autonomo (Work Deductions — Reduce Tax Payable)

| Net Income (EUR) | Detrazione |
|---|---|
| ≤ 5,500 | EUR 1,265 |
| 5,501 – 28,000 | EUR 500 + [1,200 × (28,000 − income) / 22,500] |
| 28,001 – 50,000 | EUR 500 × (50,000 − income) / 22,000 |
| > 50,000 | 0 |

These detrazioni reduce IRPEF payable (not taxable income). Compute after applying bracket rates.

### INPS Gestione Separata (Social Contributions)

| Contributor Type | Rate 2025 |
|---|---|
| Freelancer without pension fund (no cassa) | 26.07% |
| Freelancer with pension fund (con cassa) | 24% |
| Pensioners or those with other coverage | 24% |

Applied to: **net income** (gross receipts − deductible expenses). Cap: EUR 119,650 gross (contributions stop above this).

**Rivalsa INPS (4% surcharge on invoices):** Freelancers without a cassa previdenziale may add 4% to invoice as rivalsa INPS. The rivalsa received is taxable income; the corresponding INPS contribution paid is deductible.

### Acconti IRPEF (Advance Payments)

| Threshold | Rule |
|---|---|
| IRPEF due < EUR 51.65 | No acconto required |
| IRPEF due EUR 51.65–257.52 | One payment: 100% by 30 November |
| IRPEF due > EUR 257.52 | 40% by 30 June (with saldo); 60% by 30 November |

Acconto rate: 100% of prior-year IRPEF (or 100% of current-year estimate if lower).

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Regional surtax unknown | Apply 1.23% (statutory minimum) |
| Municipal surtax unknown | Apply 0% (cannot assume) — flag for client |
| Pension fund (cassa) membership unknown | Apply 26.07% Gestione Separata rate |
| Rivalsa INPS on invoices unclear | Do NOT assume 4% added — ask client |
| Deductible vs. non-deductible expense disputed | Non-deductible — flag for reviewer |
| Payment received: unclear if taxable | Taxable — flag for reviewer |
| Invoice date vs. payment date conflict | Apply **cassa** (cash) basis for freelancers |
| Refund or reimbursement | Non-taxable if documented client reimbursement; taxable otherwise |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Gross receipts > EUR 85,000 | Was regime forfettario? — verify |
| INPS contributions < 20% of net income | Possible miscalculation — review |
| No acconto payments recorded | Check if acconti were due |
| Large cash payments > EUR 999.99 | Anti-money-laundering limit — flag |
| Expense > EUR 5,000 with no documentation | Reject — cannot deduct |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing Italian income tax, collect:

1. **Total gross receipts** (fatturato lordo) — all amounts invoiced or received, including rivalsa INPS if applied
2. **Deductible expenses** — receipts or bank evidence for each
3. **Region and municipality** — for addizionali rates
4. **Pension fund membership** — yes/no; if yes, which cassa (e.g., ENPAM, INPGI, Inarcassa) — affects INPS rate
5. **Rivalsa INPS applied on invoices** — yes/no; if yes, total rivalsa received
6. **Prior-year IRPEF** — for acconto calculation
7. **Bank statements** — 12 months for the fiscal year
8. **Advance payments made** — acconti IRPEF paid (F24 receipts)
9. **Detrazioni claimed** — family dependants (coniuge, figli) for additional detrazioni
10. **Other income sources** — employment (redditi da lavoro dipendente), rental (redditi fondiari), capital gains

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-IT-1 | Client provides only bank totals, no itemised expenses | Request itemised expense list with F24/receipts before proceeding |
| R-IT-2 | Income from both regime ordinario AND regime forfettario in same year | Stop — mixed regime not possible; verify which applies and for which period |
| R-IT-3 | Gross receipts > EUR 85,000 but client claims regime forfettario applies | Stop — forfettario threshold exceeded; regime ordinario applies automatically |
| R-IT-4 | Non-resident claiming full Italian detrazioni | Clarify residency status; non-residents have restricted access to detrazioni |
| R-IT-5 | Client requests deduction for private vehicle without usage log | Reject vehicle deduction — 20% cap applies and requires documented business use |

---

## Section 3 — Transaction Pattern Library

Map bank statement narrations to tax lines deterministically. If a narration matches a pattern, apply the mapped treatment without escalating. If no pattern matches, escalate to Tier 2.

### Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `BONIFICO DA [client name]` | Gross receipts — professional income | Standard SEPA credit transfer from client |
| I-02 | `VB DA [client name]` / `VB ENTRATA` | Gross receipts — professional income | UniCredit/BancoBPM credit notation |
| I-03 | `ACCREDITO DA [client]` | Gross receipts — professional income | Generic bank credit from client |
| I-04 | `STRIPE PAYMENTS EUROPE` / `STRIPE PAYOUT` | Gross receipts — online professional income | Gross-up to pre-fee amount; Stripe fee is deductible |
| I-05 | `PAYPAL TRANSFER` / `PAYPAL ACCREDITO` | Gross receipts — professional income | Gross-up; PayPal fee deductible |
| I-06 | `SATISPAY BUSINESS PAYOUT` | Gross receipts — professional income | Satispay payout; fee deductible |
| I-07 | `NEXI PAGAMENTI` / `NEXI POS VERSAMENTO` | Gross receipts — card payment income | Nexi merchant settlement; gross-up |
| I-08 | `SUMUP PAYOUT` / `ZETTLE PAYOUT` | Gross receipts — card payment income | Card terminal payout; gross-up |
| I-09 | `REVERSALE [client]` / `RIMESSA CLIENTI` | Gross receipts — professional income | Public administration or factoring payment |
| I-10 | `RIVALSA INPS` (portion of invoice) | Taxable — included in gross receipts | 4% rivalsa component is taxable income |
| I-11 | `INTERESSI ATTIVI` / `INTERESSI MATURATI` | Interest income — Quadro RW/RL | Not professional income; separate treatment |
| I-12 | `RIMBORSO SPESE [client]` | Non-taxable reimbursement (if documented) | Requires client reimbursement note; flag if undocumented |

### Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `AFFITTO UFFICIO` / `CANONE LOCAZIONE` / `PIGIONE` | Rent — deductible (professional share) | Home office: only dedicated professional portion |
| E-02 | `ENEL` / `ENI PLENITUDE` / `A2A ENERGIA` | Utilities — 50% deductible (mixed use assumption) | Flag if solely professional premises — 100% |
| E-03 | `TELECOM ITALIA` / `TIM FIBRA` / `FASTWEB` / `WIND3` | Internet/phone — 80% deductible (Telecomunicazioni rule) | 80% cap for all telecoms under Art. 54 TUIR |
| E-04 | `VODAFONE MOBILE` / `TIM MOBILE` / `ILIAD` | Mobile phone — 80% deductible | Same 80% telecoms cap |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software subscriptions — 100% deductible | Professional software, fully deductible |
| E-06 | `COMMERCIALISTA` / `CONSULENTE FISCALE` / `STUDIO [name]` | Professional fees — 100% deductible | Accountant/tax advisor fees |
| E-07 | `AVVOCATO` / `NOTAIO` | Legal fees — 100% deductible (if professional purpose) | Flag if personal legal matter |
| E-08 | `TRENITALIA` / `ITALO` / `FRECCIAROSSA` | Travel — 100% deductible if professional | Require destination + purpose note |
| E-09 | `RYANAIR` / `EASYJET` / `ITA AIRWAYS` / `ALITALIA` | Air travel — 100% deductible if professional | Require itinerary + purpose |
| E-10 | `HOTEL` / `AGODA` / `BOOKING.COM` | Accommodation — 75% deductible (forfait hospitality limit) | Art. 109 TUIR hospitality cap |
| E-11 | `RISTORANTE` / `PIZZERIA` / `CAFFE` | Meals — 75% deductible (hospitality limit) | Must be professional purpose; social meals = 0% |
| E-12 | `INPS F24` / `CONTRIBUTI GESTIONE SEPARATA` | INPS contributions — 100% deductible | Social contributions reduce taxable income |
| E-13 | `F24 ACCONTO IRPEF` / `F24 SALDO IRPEF` | IRPEF advance/balance — NOT deductible | Tax payments are not expenses |
| E-14 | `ASSICURAZIONE PROFESSIONALE` / `RC PROFESSIONALE` | Professional insurance — 100% deductible | Professional liability insurance |
| E-15 | `ADDIZIONALE REGIONALE` / `ADDIZIONALE COMUNALE` | NOT deductible | Surtaxes paid are not deductible from income |
| E-16 | `SPESE BANCARIE` / `COMMISSIONI BANCARIE` / `CANONE CONTO` | Bank fees — 100% deductible | Professional account fees |
| E-17 | `AMORTAMENTO` / `BENE STRUMENTALE` | Capital asset — depreciation schedule | Do not expense in full; apply ammortamento table |
| E-18 | `AUTONOLEGGIO` / `NOLEGGIO AUTO` | Car hire — 20% deductible cap | Art. 164 TUIR; full deduction only if exclusively professional |
| E-19 | `CARBURANTE` / `ENI` / `Q8` / `SHELL` | Fuel — 20% deductible cap | Same Art. 164 TUIR car expense limit |
| E-20 | `FORMAZIONE` / `CORSO` / `SEMINARIO` | Training/education — 100% deductible | Professional development |
| E-21 | `CANCELLERIA` / `MATERIALE UFFICIO` / `UNIEURO` (office) | Office supplies — 100% deductible | Minor consumables; flag large amounts |
| E-22 | `CONTRIBUTO CASSA [profession]` / `ENPAM` / `INARCASSA` | Cassa contributions — 100% deductible | Replaces Gestione Separata for applicable professions |

---

## Section 4 — Worked Examples

### Example 1 — Intesa Sanpaolo (Milan, Graphic Designer)

**Bank:** Intesa Sanpaolo CSV export (semicolon-delimited)
**Client:** Valentina Rossi, graphic designer, Milan, no pension fund

```
Data;Valuta;Descrizione;Dare;Avere
03/01/2025;;BONIFICO DA STUDIO GAMBA SRL;;3.500,00
15/01/2025;;SPESE BANCARIE TENUTA CONTO;4,50;
10/02/2025;;BONIFICO DA FREELANCE CORP;;2.200,00
28/02/2025;;FASTWEB INTERNET;35,90;
15/03/2025;;STRIPE PAYMENTS EUROPE;;1.850,00
31/03/2025;;ADOBE CREATIVE CLOUD;59,99;
20/04/2025;;BONIFICO DA MEDIA HOUSE SRL;;4.100,00
15/05/2025;;F24 ACCONTO IRPEF;1.200,00;
30/06/2025;;CONTRIBUTI GESTIONE SEPARATA F24;1.800,00;
15/07/2025;;COMMERCIALISTA STUDIO BIANCHI;500,00;
10/10/2025;;TRENITALIA ROMA-MILANO;89,00;
30/11/2025;;F24 ACCONTO IRPEF;1.800,00;
```

**Step 1 — Income**

| Narration | Pattern | Gross Amount |
|---|---|---|
| BONIFICO DA STUDIO GAMBA | I-01 | EUR 3,500.00 |
| BONIFICO DA FREELANCE CORP | I-01 | EUR 2,200.00 |
| STRIPE PAYMENTS EUROPE | I-04 | EUR 1,850.00 (net); gross-up: assume ~2.9%+0.30 fee → ~EUR 1,905.81 |
| BONIFICO DA MEDIA HOUSE | I-01 | EUR 4,100.00 |
| **Total gross receipts** | | **EUR 11,705.81** |

**Step 2 — Expenses**

| Narration | Pattern | Amount | Deductible |
|---|---|---|---|
| SPESE BANCARIE | E-16 | EUR 4.50 | EUR 4.50 |
| FASTWEB INTERNET | E-03 | EUR 35.90 × 12 = EUR 430.80 | EUR 344.64 (80%) |
| ADOBE CREATIVE CLOUD | E-05 | EUR 59.99 × 12 = EUR 719.88 | EUR 719.88 (100%) |
| CONTRIBUTI GESTIONE SEPARATA | E-12 | EUR 1,800.00 | EUR 1,800.00 (100%) |
| COMMERCIALISTA | E-06 | EUR 500.00 | EUR 500.00 |
| TRENITALIA | E-08 | EUR 89.00 | EUR 89.00 (professional) |
| F24 ACCONTO IRPEF | E-13 | EUR 3,000.00 | EUR 0 (not deductible) |
| **Total deductible expenses** | | | **EUR 3,458.02** |

**Step 3 — Net Income**

```
Gross receipts:          EUR 11,705.81
Less deductible expenses: EUR  3,458.02
Net income (Quadro RE):  EUR  8,247.79
```

**Step 4 — INPS Gestione Separata (final)**

```
EUR 8,247.79 × 26.07% = EUR 2,150.99
Less advance paid:       EUR 1,800.00
Balance due:             EUR   350.99
Deductible from IRPEF base: EUR 2,150.99 (adjust if advance differs from actual)
```

Note: Net income for IRPEF = EUR 8,247.79 − additional INPS adjustment if any. For simplicity here use EUR 8,247.79.

**Step 5 — IRPEF**

```
EUR 8,247.79 × 23% = EUR 1,896.99
Detrazione lavoro autonomo (income EUR 8,247.79):
  = EUR 500 + [1,200 × (28,000 − 8,247.79) / 22,500]
  = EUR 500 + [1,200 × 19,752.21 / 22,500]
  = EUR 500 + EUR 1,053.45 = EUR 1,553.45
IRPEF net = EUR 1,896.99 − EUR 1,553.45 = EUR 343.54
```

**Step 6 — Addizionali (Lombardia, Milan)**

```
Regionale (Lombardia 1.23%): EUR 8,247.79 × 1.23% = EUR 101.45
Comunale (Milan 0.80%):      EUR 8,247.79 × 0.80% = EUR  65.98
Total addizionali:            EUR 167.43
```

**Total tax:** EUR 343.54 + EUR 167.43 = **EUR 510.97**

---

### Example 2 — UniCredit (Turin, IT Consultant)

**Bank:** UniCredit PDF statement (manual parse)
**Client:** Marco Ferretti, IT consultant, Turin, Gestione Separata

Key transactions:
- BONIFICO VB DA ACCENTURE SRL: EUR 6,500/month × 10 = EUR 65,000
- MICROSOFT 365 BUSINESS: EUR 12.50/month
- SPESE BANCARIE: EUR 3.00/month
- FORMAZIONE UDEMY/COURSERA: EUR 250 total
- F24 INPS GESTIONE SEPARATA: EUR 8,500 (acconti)

**Net income:** EUR 65,000 − EUR 250 (training) − EUR 36 (bank) − EUR 150 (Microsoft 80%) − EUR 16,945.50 (INPS 26.07%) = **EUR 47,618.50**

IRPEF: EUR 28,000 × 23% + EUR 19,618.50 × 35% = EUR 6,440 + EUR 6,866.48 = EUR 13,306.48
Detrazione: income > EUR 28,000 → EUR 500 × (50,000 − 47,618.50) / 22,000 = EUR 54.12
IRPEF net: EUR 13,306.48 − EUR 54.12 = **EUR 13,252.36**

Flag: Gross receipts EUR 65,000 — below EUR 85,000 forfettario threshold, but single client — verify no regime forfettario election was active.

---

### Example 3 — FinecoBank (Rome, Photographer)

**Bank:** FinecoBank digital statement (CSV)
**Client:** Sofia Mancini, photographer, Rome, no cassa

Key transactions:
- ACCREDITO BONIFICO clienti: EUR 28,000 total
- NEXI POS VERSAMENTO (card payments on-site): EUR 7,000 total
- AFFITTO STUDIO FOTOGRAFICO: EUR 600/month = EUR 7,200
- ENEL ENERGIA studio: EUR 120/month = EUR 1,440 (100% professional premises)
- ATTREZZATURA FOTOGRAFICA (equipment purchase > EUR 516.46): EUR 3,500 → ammortamento 25% = EUR 875 deductible year 1
- ASSICURAZIONE RC PROFESSIONALE: EUR 350

**Net income:** EUR 35,000 − EUR 7,200 − EUR 1,440 − EUR 875 − EUR 350 − EUR 9,124.50 (INPS 26.07%) = **EUR 16,010.50**

IRPEF: EUR 16,010.50 × 23% = EUR 3,682.42
Detrazione: EUR 500 + [1,200 × (28,000 − 16,010.50) / 22,500] = EUR 500 + EUR 639.40 = EUR 1,139.40
IRPEF net: EUR 3,682.42 − EUR 1,139.40 = **EUR 2,543.02**

Note: Equipment EUR 3,500 > EUR 516.46 threshold — cannot fully expense in year 1; ammortamento table applies (25% for fotocamere/attrezzatura).

---

### Example 4 — N26 Italy (Florence, Translator/Copywriter)

**Bank:** N26 app CSV (comma-delimited, EUR amounts without thousands separator)
**Client:** Luca Bianchi, translator, Florence, no pension fund

Key income: STRIPE PAYOUT EUR 22,000 (net of fees), PayPal ACCREDITO EUR 5,500 (net)

Gross-up: Stripe ~EUR 22,660 / PayPal ~EUR 5,664 = EUR 28,324 gross receipts

Key expenses: FASTWEB 80% = EUR 344, ADOBE 100% = EUR 720, INPS contributions EUR 7,378 (26.07%)

Net income: EUR 28,324 − EUR 344 − EUR 720 − EUR 7,378 = **EUR 19,882**

IRPEF net of detrazione: EUR 19,882 × 23% = EUR 4,572.86 − EUR 1,265 (threshold detrazione) = wait — income EUR 19,882 > EUR 5,500; use formula: EUR 500 + [1,200 × (28,000 − 19,882) / 22,500] = EUR 500 + EUR 432.96 = EUR 932.96

IRPEF: EUR 4,572.86 − EUR 932.96 = **EUR 3,639.90**

Note: N26 Italy CSV exports use DD/MM/YYYY date format; amounts use period decimal separator, no thousands separator.

---

### Example 5 — Hype Business (Naples, E-commerce)

**Bank:** Hype Business statement
**Client:** Anna Greco, e-commerce seller, Naples

Note: If e-commerce generates redditi d'impresa (business income), Quadro RE does NOT apply — Quadro RF (impresa) applies. Flag immediately if client is registered as impresa individuale.

Assuming **lavoro autonomo** status (occasional/consulting, not impresa):
- SUMUP PAYOUT (card sales): EUR 15,000
- Refunds issued to customers: EUR 800 → deduct from gross
- Hosting/platform fees (Shopify/WooCommerce): EUR 500 (100% deductible)

Net receipts: EUR 15,000 − EUR 800 = EUR 14,200
Net income: EUR 14,200 − EUR 500 − EUR 3,701.94 (INPS) = **EUR 9,998.06**

Flag: E-commerce structure — confirm lavoro autonomo vs. impresa individuale before filing Quadro RE.

---

### Example 6 — BancoBPM (Bergamo, Architect)

**Bank:** BancoBPM PDF (tabular format, Dare/Avere columns)
**Client:** Roberto Villa, architect, Bergamo, Inarcassa member

Key note: Architects are Inarcassa members → Gestione Separata does NOT apply. Inarcassa rate: ~14.5% subjective contribution + integrative 4%. Verify current Inarcassa rates separately.

Income: EUR 85,000 gross (below EUR 85,000 threshold — wait: EUR 85,000 equals threshold — forfettario cap is EUR 85,000; amounts > EUR 85,000 preclude forfettario. At exactly EUR 85,000 forfettario still eligible. Verify with client.)

For regime ordinario calculation:
IRPEF: EUR 28,000 × 23% + EUR 22,000 × 35% + EUR 35,000 × 43% = EUR 6,440 + EUR 7,700 + EUR 15,050 = EUR 29,190
Detrazione: income > EUR 50,000 → EUR 0
IRPEF net: **EUR 29,190**

Flag: Inarcassa contributions deductible from income — collect Inarcassa annual statement for exact amounts. High-income flag (> EUR 85,000 gross).

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-IT-1 — Cash basis for freelancers**
Italian freelancers (liberi professionisti) use the **cassa** (cash) principle: income is taxed when received, expenses are deductible when paid. Invoice date is irrelevant for timing.

**T1-IT-2 — INPS Gestione Separata deductibility**
All INPS Gestione Separata contributions paid in the fiscal year are 100% deductible from professional income. This reduces taxable income before applying IRPEF brackets. Apply without escalating.

**T1-IT-3 — Telecoms 80% cap**
All telephone and internet expenses — mobile, fixed, broadband — are subject to a statutory 80% deductibility cap under Art. 54 TUIR. Apply 80% to all telecom narrations without exception.

**T1-IT-4 — Vehicles 20% cap**
Car purchase, hire, lease, fuel, and maintenance are capped at 20% deductibility under Art. 164 TUIR for professionals. Exception: vehicles exclusively assigned to employees (100%) — flag for reviewer, do not apply automatically.

**T1-IT-5 — Equipment threshold (beni strumentali)**
Assets costing ≤ EUR 516.46 (unit cost) may be fully expensed in year of purchase. Assets > EUR 516.46 must be depreciated over their useful life using the Ministerial ammortamento table. Never fully expense assets > EUR 516.46 in year 1.

**T1-IT-6 — IVA (VAT) not included in income or expenses**
Amounts subject to IVA: strip IVA before computing professional income. Gross receipts = invoiced amount ex-IVA. Deductible expenses = cost ex-IVA (IVA is separately recovered via IVA return or disallowed if pro-rated). Do not double-count IVA.

**T1-IT-7 — F24 tax payments are not deductible**
IRPEF (saldo and acconti), addizionali, and IVA paid via F24 are tax payments, not business expenses. Never include F24 tax payments as deductible expenses.

**T1-IT-8 — Hospitality (meals/accommodation) 75% cap**
Restaurant, hotel, and entertainment expenses incurred for professional purposes are capped at 75% deductibility. Strictly social meals are 0% deductible.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-IT-1 | Home office deduction claimed | Portion of rent/utilities attributable to professional use requires documented floor area calculation | Accept only dedicated professional space; estimate pro-rata if client provides layout |
| T2-IT-2 | Mixed-use vehicle (auto ad uso promiscuo) | 20% cap applies unless vehicle is exclusively professional or employee-assigned | Default to 20%; upgrade to higher only with written assignment evidence |
| T2-IT-3 | Regime ordinario vs. regime forfettario comparison | Client approaching EUR 85,000 threshold or asking which is better | Present both calculations; do not recommend — flag for accountant |
| T2-IT-4 | Cassa previdenziale contributions (Inarcassa, ENPAM, etc.) | Rates differ by profession and year; not standard Gestione Separata | Collect annual Inarcassa/cassa statement; do not estimate |
| T2-IT-5 | Rappresentanza (entertainment/promotional) expenses | Deductible at 75% if < 1% of revenues; above 1% may be disallowed | Flag if total entertainment > 1% of gross |
| T2-IT-6 | Compensation received from foreign clients (non-resident payor) | Withholding tax may apply; foreign tax credit possible | Flag — requires double-tax treaty analysis |
| T2-IT-7 | Crypto income or NFT sales | Italian treatment evolving — imposta sostitutiva 26% on gains; separate from professional income | Flag — do not include in Quadro RE; separate Quadro RT/RW treatment |
| T2-IT-8 | Occasional work (lavoro autonomo occasionale) vs. habitual | Occasional work < EUR 5,000/year: no INPS obligation, different withholding rules | Confirm habitual/occasional status before applying INPS |

---

## Section 7 — Excel Working Paper Template

```
ITALIAN INCOME TAX WORKING PAPER (REGIME ORDINARIO)
Taxpayer: _______________  CF: _______________  FY: 2025  Region: _______________

SECTION A — INCOME (Quadro RE)
                                        EUR
Gross professional receipts             ___________
Less: returned amounts/refunds          (__________)
Net receipts                            ___________

SECTION B — DEDUCTIBLE EXPENSES
Rent (professional portion)             ___________
Utilities (professional portion)        ___________
Telecoms (80% of total)                ___________
Software subscriptions                  ___________
Professional fees (commercialista etc.) ___________
Legal fees                              ___________
Training / CPD                          ___________
Travel (trains, flights — professional) ___________
Accommodation & meals (75%)            ___________
Professional insurance                  ___________
Bank charges                            ___________
Capital allowances (ammortamento)       ___________
Other deductible expenses               ___________
INPS Gestione Separata / Cassa         ___________
TOTAL DEDUCTIBLE EXPENSES               ___________

SECTION C — NET INCOME (Quadro RE, line RE23)
Net professional income (A − B)         ___________

SECTION D — IRPEF COMPUTATION
IRPEF gross (bracket calculation)       ___________
Less: Detrazione lavoro autonomo        (___________)
IRPEF net                               ___________
Less: ritenute d'acconto withheld       (___________)
Less: acconti paid (F24)               (___________)
IRPEF balance due / (refund)            ___________

SECTION E — ADDIZIONALI
Addizionale regionale (___%)           ___________
Addizionale comunale (___%)            ___________
Total addizionali                       ___________

SECTION F — INPS GESTIONE SEPARATA
Net income × 26.07% (or cassa rate)    ___________
Less: advance contributions paid        (___________)
INPS balance due                        ___________

SECTION G — REVIEWER FLAGS
[ ] Regime forfettario threshold check (< EUR 85,000?)
[ ] Vehicle deduction — 20% cap applied?
[ ] Equipment > EUR 516.46 — depreciation schedule used?
[ ] Telecoms — 80% cap applied?
[ ] Home office — documented floor area?
[ ] Acconto payments verified against F24 receipts
[ ] IVA stripped from all amounts
```

---

## Section 8 — Bank Statement Reading Guide

### Intesa Sanpaolo
- Export: CSV via online banking ("Scarica Movimenti") — semicolon-delimited
- Columns: `Data movimento; Valuta; Descrizione; Dare (debit); Avere (credit)`
- Amount format: thousands separator = `.`, decimal = `,` (e.g., `1.234,56`)
- Date format: DD/MM/YYYY
- Credit narrations: `BONIFICO DA [sender]`, `ACCREDITO BONIFICO SEPA`
- Debit narrations: `BONIFICO A FAVORE`, `ADDEBITO`, `PAGAMENTO F24`

### UniCredit
- Export: CSV or PDF ("Estratto conto")
- Columns: `Data; Descrizione operazione; Dare; Avere; Saldo`
- Credit narrations often prefixed: `VB DA [sender]` or `ACCREDITO BONIF. DA`
- UniCredit uses `VB` (versamento bancario) prefix in many narrations

### BancoBPM
- Export: PDF or Excel from online portal
- Columns: `Data; Causale; Importo Dare; Importo Avere`
- Uses standard ABI causale codes alongside description text

### FinecoBank
- Export: CSV ("Scarica CSV") from "Conto" > "Movimenti"
- Columns: `Data; Entrata; Uscita; Descrizione; Tipo`
- Amount format: no thousands separator, comma decimal (e.g., `1234,56`)
- Date format: DD/MM/YYYY
- All electronic transfers show as `BONIFICO` with IBAN of counterpart

### N26 Italy
- Export: CSV from app ("Scarica estratto conto")
- Columns: `Date,Payee,Account number,Transaction type,Payment reference,Amount (EUR),Amount (Foreign Currency),Type Foreign Currency,Exchange Rate`
- Amount format: no thousands separator, period decimal (e.g., `1234.56`) — note: opposite of Italian banks
- Date format: YYYY-MM-DD
- Stripe payouts appear as: `Stripe` in Payee column

### Hype Business
- Export: CSV from Hype app
- Simple format: `Data;Descrizione;Importo;Tipo`
- Tipo: `ENTRATA` (credit) or `USCITA` (debit)
- NEXI/card settlements appear as `NEXI PAGAMENTI`

### Revolut Italy
- Export: CSV ("Statements" in app)
- Columns: `Type,Product,Started Date,Completed Date,Description,Amount,Fee,Currency,State`
- Amounts in EUR with period decimal; filter `State = COMPLETED` only

---

## Section 9 — Onboarding Fallback

If the client cannot provide all required inputs, use this script:

**Missing bank statements:**
> "To compute your IRPEF accurately I need your full 2025 bank statements (January–December). Please download from your bank's online portal: Intesa Sanpaolo → 'Scarica Movimenti'; UniCredit → 'Estratto conto'; FinecoBank → 'Scarica CSV'. If unavailable, your commercialista can request them directly from the bank."

**Unknown region/municipality:**
> "Your addizionale regionale and comunale rates depend on your tax residence (residenza fiscale) as of 31 December 2025. Please confirm your comune of residence on that date. If unsure, check your last Modello Redditi or identity documents."

**Cassa previdenziale unknown:**
> "To apply the correct social contribution rate I need to know if you are enrolled in a cassa previdenziale (e.g., ENPAM for doctors, Inarcassa for architects). If you receive a quarterly statement from a cassa, you are enrolled there and Gestione Separata does NOT apply. If you have no cassa, INPS Gestione Separata applies at 26.07%."

**Expense receipts missing:**
> "Italian tax law requires documentary evidence (ricevuta, fattura, or bank payment) for all deductions. I cannot include expenses for which you have no evidence. Please retrieve receipts from suppliers or, where unavailable, note the expense as unsubstantiated — it will be excluded from deductions."

**Regime ordinario vs. forfettario unclear:**
> "Before proceeding under regime ordinario, confirm: (1) Did your gross receipts in 2024 exceed EUR 85,000? (2) Do you have any employment income simultaneously? If gross receipts stayed below EUR 85,000 and you have no employment income, regime forfettario may be available and more beneficial. This skill covers only regime ordinario — see it-regime-forfettario.md for forfettario analysis."

---

## Section 10 — Reference Material

### Key Legislation
- **DPR 917/1986 (TUIR)** — Testo Unico delle Imposte sui Redditi; Art. 53 (lavoro autonomo), Art. 54 (deductions), Art. 164 (vehicles)
- **Legge di Bilancio 2025** — annual budget law adjusting brackets and detrazioni
- **DPR 633/1972** — IVA; relevant for VAT treatment of receipts/expenses

### Filing Deadlines 2025 (FY 2024 return)
| Deadline | Event |
|---|---|
| 30 June 2025 | Modello Redditi PF filing deadline (online) |
| 30 June 2025 | IRPEF saldo + 1st acconto (40%) payment |
| 30 November 2025 | 2nd acconto (60%) payment |

### INPS Gestione Separata 2025 Rates
- No other coverage: 26.07%
- Pensioners / those with other mandatory coverage: 24%
- Contribution ceiling: EUR 119,650

### IRPEF Acconti Computation
- Method 1 (storico): 100% of prior-year tax liability
- Method 2 (previsionale): 100% of estimated current-year liability
- Use whichever is lower (legal option)

### Useful References
- Agenzia delle Entrate: agenziaentrate.gov.it
- INPS Gestione Separata: inps.it/rubrica-del-sito/gestione-separata
- Modello Redditi PF instructions: published annually by AdE (typically April)
- Ammortamento table: DM 31/12/1988 (ministerial decree on depreciation rates)
