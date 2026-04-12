---
name: no-income-tax
description: >
  Use this skill whenever asked about Norwegian income tax for self-employed individuals (enkeltpersonforetak). Trigger on phrases like "Norwegian tax", "trinnskatt", "alminnelig inntekt", "personfradrag", "skattemelding", "RF-1175", "naeringsoppgave", "enkeltpersonforetak", "self-employed tax Norway", or any question about filing or computing income tax for a Norwegian self-employed client. Covers alminnelig inntekt (22%), trinnskatt (5 brackets), personfradrag, naeringsinntekt computation, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Norwegian income tax work.
version: 2.0
jurisdiction: "NO"
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Norway Income Tax -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Norway (Kongeriket Norge) |
| Tax | Alminnelig inntekt (22%) + Trinnskatt (5 brackets) + Trygdeavgift (11.0% for self-employed) |
| Currency | NOK only |
| Tax year | Calendar year |
| Primary legislation | Skatteloven; Skatteforvaltningsloven |
| Supporting legislation | Folketrygdloven; Bokforingsloven |
| Tax authority | Skatteetaten |
| Filing portal | skatteetaten.no / Altinn |
| Filing deadline | 30 April of following year |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Norwegian statsautorisert or registrert revisor |
| Validation date | Pending |
| Skill version | 2.0 |

### Alminnelig Inntekt (General Income Tax)

| Item | Value |
|---|---|
| Rate | 22% flat |
| Applied to | Net income after all deductions minus personfradrag |
| Personfradrag | NOK 108,550 (class 1, 2025) |

### Trinnskatt Brackets (2025)

| Trinn | Income Range (NOK) | Rate |
|---|---|---|
| 1 | 217,401 -- 306,050 | 1.7% |
| 2 | 306,051 -- 697,150 | 4.0% |
| 3 | 697,151 -- 942,400 | 13.7% |
| 4 | 942,401 -- 1,410,750 | 16.7% |
| 5 | Above 1,410,750 | 17.7% |

Trinnskatt applies to personinntekt (NOT alminnelig inntekt).

### Trygdeavgift (National Insurance)

| Income Type | Rate |
|---|---|
| Naeringsinntekt (self-employment) | 11.0% |
| Lonnsinntekt (employment) | 7.9% |
| Pensjonsinntekt (pension) | 5.1% |

Lower threshold: ~NOK 69,650.

### Key Form

| Form | Who | Threshold |
|---|---|---|
| RF-1175 Naeringsoppgave 1 | All enkeltpersonforetak | Gross revenue > NOK 50,000 |
| Skattemelding | All taxpayers | Filed via Altinn by 30 April |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown business form | Enkeltpersonforetak |
| Unknown business-use % | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown asset useful life | Use saldogruppe rates |
| Unknown minstefradrag claim | NOT applicable to naeringsinntekt |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, confirmation of business form (enkeltpersonforetak).

**Recommended** -- all invoices, prior year skattemelding, asset register, forskuddsskatt payment records.

**Ideal** -- complete naeringsoppgave from prior year, balance sheet (for skjermingsfradrag), documented mileage log if vehicle claimed.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement = hard stop.

### Refusal Catalogue

**R-NO-1 -- Companies (AS, ASA).** "This skill covers enkeltpersonforetak only. Aksjeselskap files separate return. Out of scope."

**R-NO-2 -- International income / permanent establishment.** "Cross-border income requires specialist analysis. Escalate."

**R-NO-3 -- Complex restructuring.** "Business restructuring (omdanning) requires specialist advice. Escalate."

**R-NO-4 -- Petroleum tax.** "Petroleum taxation is out of scope."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| OVERF. [client], BETALING, HONORAR, FAKTURA | Driftsinntekter | Business income | If MVA-registered, extract net (excl. 25% MVA) |
| STRIPE PAYOUT, PAYPAL PAYOUT | Driftsinntekter | Business income | Platform payout |
| UPWORK, FIVERR, TOPTAL | Driftsinntekter | Business income | Freelance platform |
| LONN, ARBEIDSGIVER | Lonnsinntekt | NOT self-employment | Employment income |
| LEIEINNTEKT, HUSLEIE MOTTATT | Eiendomsinntekt | NOT self-employment | Rental income |
| RENTER, UTBYTTE, AVKASTNING | Kapitalinntekt | NOT self-employment | Capital income |
| SKATT TILBAKEBETALING | EXCLUDE | Not income | Tax refund |
| NAV UTBETALING | Check nature | May be taxable | Some NAV benefits are taxable |

### 3.2 Expense Patterns (Debits) -- Fully Deductible

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| KONTORLEIE, HUSLEIE KONTOR | Lokalekostnader | Fully deductible | Dedicated premises |
| YRKESSKADEFORSIKRING, ANSVARSFORSIKRING | Forsikring | Fully deductible | Professional insurance |
| REVISOR, REGNSKAPSFORER, BOKHOLDER | Revisjonskostnader | Fully deductible | |
| ADVOKAT (business) | Advokatkostnader | Fully deductible | Business-related |
| KONTORREKVISITA, KONTORMATERIELL | Kontorkostnader | Fully deductible | |
| REKLAME, MARKEDSFORING, GOOGLE ADS | Markedsforingskostnader | Fully deductible | |
| FAGLIG OPPDATERING, KURS, SEMINAR | Utdanningskostnader | Fully deductible | Current profession ONLY |
| BRANSJEFORENING, FAGFORENING | Kontingenter | Fully deductible | |
| BANKGEBYR, KONTOGEBYR | Bankkostnader | Fully deductible | Business account |
| STRIPE FEE, PAYPAL FEE | Transaksjonskostnader | Fully deductible | |
| SOFTWARE, ABONNEMENT, LISENS | IT-kostnader | Fully deductible | |
| PORTO, POSTEN | Portokostnader | Fully deductible | |

### 3.3 Expense Patterns -- Travel

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| FLY, SAS, NORWEGIAN, WIDEROE | Reisekostnader | Fully deductible | Business travel |
| HOTELL, BOOKING.COM | Reisekostnader | Fully deductible | Business travel |
| NSB, VY, RUTER | Reisekostnader | Fully deductible | Business travel |
| TAXI, UBER, BOLT | Reisekostnader | Fully deductible | Business purpose |
| BENSIN, DIESEL, CIRCLE K, ESSO, SHELL | Bilkostnader | T2 -- business km only | Standard NOK 3.50/km or actual |
| BOMPENGER, PARKERING | Bilkostnader | T2 -- business km only | |

### 3.4 Expense Patterns -- Partially Deductible

| Pattern | Deductibility | Treatment | Notes |
|---|---|---|---|
| REPRESENTASJON, KUNDEMIDDAG | Up to NOK 559/person/event | Limited | Must document business purpose |

### 3.5 Expense Patterns -- NOT Deductible

| Pattern | Treatment | Notes |
|---|---|---|
| PRIVAT, DAGLIGVARER, KIWI, REMA, COOP | NOT deductible | Personal living costs |
| BOT, FORELEGG, GEBYR (penalty) | NOT deductible | Fines |
| SKATT, FORSKUDDSSKATT, RESTSKATT | NOT deductible | Income tax |
| TRYGDEAVGIFT | NOT deductible | Not deductible against income |
| PRIVATUTTAK | NOT deductible | Drawings |
| UTDANNING NY PROFESJON | NOT deductible | Education for NEW profession blocked |

### 3.6 Capital Items (Saldogrupper)

| Pattern | Saldogruppe | Max Rate | Notes |
|---|---|---|---|
| KONTORMASKIN, PC, LAPTOP, SKRIVER | a (office machines) | 30% | Declining balance pool |
| BIL, PERSONBIL (business) | d (passenger cars) | 20% | |
| VAREBIL, LASTEBIL | c (trucks/vans) | 24% | |
| INVENTAR, MOBLER | d (fixtures) | 20% | |
| BYGNING (commercial) | i (office buildings) | 2% | |
| BYGNING (hotel, industrial) | h (commercial) | 4% | |
| Low-value (under NOK 15,000) | Immediate | 100% | Direct expense |
| Short-life (under 3 years) | Immediate | 100% | Regardless of cost |

### 3.7 Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| INTERN OVERF., EGNE KONTI | EXCLUDE | Own-account transfer |
| LAN, AVDRAG, NEDBETALING | EXCLUDE | Loan principal |
| RENTER LAN (business) | Deductible | Business loan interest |
| MVA BETALING | EXCLUDE from P&L | MVA liability |
| FORSKUDDSSKATT | Track separately | Preliminary tax credit |

### 3.8 Norwegian Banks -- Statement Format Reference

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| DNB | CSV, PDF | Dato, Forklaring/Tekst, Inn/Ut, Saldo | Most common; DNB Nettbank export |
| Nordea NO | CSV, PDF | Bokforingsdato, Tekst, Belop | |
| SpareBank 1 | CSV, PDF | Dato, Beskrivelse, Belop | Regional SpareBank 1 banks |
| Handelsbanken NO | CSV, PDF | Datum, Text, Belopp | Swedish parent format |
| Sbanken | CSV | Dato, Tekst, Belop | Clean CSV |
| Revolut, Wise | CSV | Date, Counterparty, Amount | Multi-currency |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (MVA-registered)

**Input line:**
`15/03/2025 ; DNB Innbetaling ; DESIGN STUDIO AS ; Faktura 2025-003 ; +125,000.00 ; NOK`

**Reasoning:**
Client payment. If MVA-registered (25%), NOK 125,000 includes MVA. Net = NOK 100,000 (revenue) + NOK 25,000 MVA (excluded).

**Classification:** Driftsinntekt = NOK 100,000. MVA NOK 25,000 excluded.

### Example 2 -- Representation (Limited)

**Input line:**
`22/04/2025 ; SpareBank 1 Kort ; RESTAURANT MAAEMO ; Kundelunsj ; -2,500.00 ; NOK`

**Reasoning:**
Representation. Deductible up to NOK 559 per person per event. If 4 persons: max NOK 559 x 4 = NOK 2,236. NOK 264 not deductible. Must document attendees and business purpose.

**Classification:** Deductible up to NOK 559/person limit. Flag for reviewer.

### Example 3 -- Equipment (Saldogruppe)

**Input line:**
`03/06/2025 ; DNB Kort ; ELKJOP ; LAPTOP ; -18,000.00 ; NOK`

**Reasoning:**
Laptop NOK 18,000. Over NOK 15,000 and life over 3 years. Saldogruppe a (office machines, 30%). Year 1: NOK 18,000 x 30% = NOK 5,400.

**Classification:** Saldogruppe a. Depreciation NOK 5,400. NOT direct expense.

### Example 4 -- Low-Value Asset (Immediate)

**Input line:**
`15/05/2025 ; Nordea Kort ; CLAS OHLSON ; KONTORSTOL ; -4,500.00 ; NOK`

**Reasoning:**
Office chair NOK 4,500. Under NOK 15,000 threshold. Immediate full deduction.

**Classification:** Driftskostnad. Fully deductible.

### Example 5 -- Minstefradrag Error

**Input line:**
Client claims minstefradrag NOK 104,450 on naeringsinntekt NOK 500,000.

**Reasoning:**
INCORRECT. Minstefradrag does NOT apply to naeringsinntekt -- only to lonnsinntekt. Self-employed must deduct actual documented expenses.

**Classification:** REJECT minstefradrag. Use actual expenses only.

### Example 6 -- Loss Carry-Forward

**Input line:**
Prior year loss NOK 150,000. Current year naeringsinntekt NOK 400,000.

**Reasoning:**
Underskudd (losses) carry forward with no time limit. Reduces alminnelig inntekt. But trinnskatt and trygdeavgift based on personinntekt (NOK 400,000) -- loss does NOT reduce personinntekt.

**Classification:** Alminnelig inntekt base = NOK 400,000 - NOK 150,000 = NOK 250,000. Trinnskatt/trygdeavgift on NOK 400,000.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Naeringsinntekt Computation

Gross revenue minus cost of sales minus operating expenses minus depreciation = naeringsinntekt. Skjermingsfradrag then reduces personinntekt (T2).

### 5.2 Alminnelig Inntekt

22% flat on net income (all sources minus all deductions minus personfradrag NOK 108,550). Applies to both personal and capital income.

### 5.3 Trinnskatt

Applies to personinntekt (gross personal income less skjermingsfradrag), NOT alminnelig inntekt. Cumulative brackets.

### 5.4 Trygdeavgift

11.0% on personinntekt from naeringsinntekt. Lower threshold ~NOK 69,650.

### 5.5 Minstefradrag -- NOT for Self-Employed

Minstefradrag applies ONLY to lonnsinntekt. Self-employed must deduct actual documented expenses.

### 5.6 Depreciation (Saldogrupper)

| Group | Assets | Max Rate |
|---|---|---|
| a | Office machines, equipment | 30% |
| b | Goodwill | 20% |
| c | Trucks, buses, vans | 24% |
| d | Passenger cars, machinery, fixtures | 20% |
| e | Ships | 14% |
| f | Aircraft | 12% |
| g | Technical installations | 10% |
| h | Commercial buildings | 4% |
| i | Office buildings | 2% |

Declining balance on pool. Low-value under NOK 15,000 or life under 3 years: immediate.

### 5.7 Non-Deductible

| Expense | Reason |
|---|---|
| Private living expenses | Not connected to income |
| Fines | Public policy |
| Income tax, trygdeavgift | Not deductible |
| Capital items (above NOK 15,000, life 3+ years) | Through saldogrupper |
| Education for new profession | Blocked |
| Minstefradrag on naeringsinntekt | Blocked |

### 5.8 Forskuddsskatt (Preliminary Tax)

4 quarterly instalments: 15 March, 15 June, 15 September, 15 December. Based on expected income. Adjustable via skatteetaten.no.

### 5.9 Filing Deadlines and Penalties

| Item | Detail |
|---|---|
| Skattemelding deadline | 30 April |
| RF-1175 | Filed with skattemelding |
| Late filing | Tvangsmulkt NOK 641/day (max ~NOK 64,100) |
| Incorrect (negligence) | 20% tilleggsskatt |
| Incorrect (gross) | 40% tilleggsskatt |
| Fraud | 60% + prosecution |

### 5.10 MVA Interaction

| Scenario | Income Tax Treatment |
|---|---|
| MVA collected (registered) | NOT income -- exclude from revenue |
| Input MVA recovered | NOT expense -- exclude |
| Non-deductible MVA | IS expense |
| Not registered (under NOK 50,000) | Gross = net |

### 5.11 RF-1175 Threshold

Gross revenue over NOK 50,000: must file naeringsoppgave. At or below: exempt.

### 5.12 Loss Carry-Forward

Underskudd carries forward with no time limit. Reduces alminnelig inntekt but NOT personinntekt.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Skjermingsfradrag (Shielding Deduction)

Shields risk-free return on business capital from trinnskatt/trygdeavgift. Net positive business assets x skjermingsrente. Reduces personinntekt. Flag for reviewer -- requires accurate balance sheet.

### 6.2 Home Office

- Dedicated room exclusively for business: proportional actual costs
- Standard deduction: NOK 2,050/year (2025) as alternative
- Dual-use room: standard deduction only
- Flag for reviewer

### 6.3 Vehicle Business Use

- Standard rate: NOK 3.50/km for business trips
- Or actual costs with logbook
- Flag for reviewer

### 6.4 Phone / Internet

Business portion only. Default 0%.

### 6.5 First Year Forskuddsskatt

New self-employed must estimate and register via skatteetaten.no. If not registered, SKAT sets at NOK 0 -- underpayment interest applies.

---

## Section 7 -- Excel Working Paper Template

```
NORWAY INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Business Form: Enkeltpersonforetak

A. DRIFTSINNTEKTER (net of MVA)
  A1. Omsetning                                    ___________
  A2. Andre inntekter                              ___________
  A3. Total                                        ___________

B. DRIFTSKOSTNADER
  B1. Lokalekostnader                              ___________
  B2. Forsikring                                   ___________
  B3. Revisor / regnskapsfører                     ___________
  B4. IT / software                                ___________
  B5. Markedsføring                                ___________
  B6. Reisekostnader                               ___________
  B7. Bilkostnader (business %)                    ___________
  B8. Representasjon (NOK 559/person limit)        ___________
  B9. Avskrivninger (saldogrupper)                 ___________
  B10. Bankkostnader                               ___________
  B11. Øvrige kostnader                            ___________
  B12. Total                                       ___________

C. NÆRINGSINNTEKT (A3 - B12)                       ___________

D. TAX COMPUTATION
  D1. Alminnelig inntekt (C - personfradrag)       ___________
  D2. x 22%                                        ___________
  D3. Trinnskatt (on personinntekt)                ___________
  D4. Trygdeavgift (11.0% on personinntekt)       ___________
  D5. Total tax                                    ___________
  D6. Less: Forskuddsskatt paid                    ___________
  D7. Restskatt / tilgode                          ___________

E. RF-1175 REQUIRED? (gross > NOK 50,000)          Yes / No

REVIEWER FLAGS:
  [ ] Business form confirmed?
  [ ] Minstefradrag NOT applied to næringsinntekt?
  [ ] Trinnskatt on personinntekt (not alminnelig)?
  [ ] Trygdeavgift at 11.0% (not 7.9%)?
  [ ] Vehicle method confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Items over NOK 15,000 in saldogrupper?
  [ ] Loss carry-forward correctly applied?
```

---

## Section 8 -- Bank Statement Reading Guide

### Norwegian Bank Statement Formats

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| DNB | CSV, PDF | Dato, Forklaring, Inn, Ut, Saldo | DNB Nettbank CSV export |
| Nordea NO | CSV, PDF | Bokføringsdato, Tekst, Beløp | |
| SpareBank 1 | CSV, PDF | Dato, Beskrivelse, Beløp | Regional banks (SR-Bank, SMN, etc.) |
| Handelsbanken | CSV, PDF | Datum, Text, Belopp | Swedish parent format |
| Sbanken | CSV | Dato, Tekst, Beløp | Clean CSV export |
| Revolut, Wise | CSV | Date, Counterparty, Amount | Multi-currency |

### Key Norwegian Banking Terms

| Term | English | Hint |
|---|---|---|
| Innbetaling | Deposit/credit | Potential income |
| Utbetaling | Withdrawal/debit | Potential expense |
| Overføring | Transfer | Check direction |
| AvtaleGiro | Direct debit | Regular expense |
| Varekjøp / Kort | Card purchase | Expense |
| Kontantuttak | Cash withdrawal | Ask purpose |
| Gebyr | Fee/charge | Bank charge |
| Nettgiro | Online payment | Expense |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- NORWAY INCOME TAX
1. Business form: enkeltpersonforetak?
2. Gross revenue (for RF-1175 threshold)?
3. Home office: dedicated room or shared? Standard deduction or actual?
4. Vehicle: standard NOK 3.50/km or actual costs?
5. Phone/internet: business use %?
6. Capital assets purchased during year? Cost and type?
7. Forskuddsskatt paid? Amounts per quarter?
8. Other income (employment, capital, rental)?
9. Prior year losses (underskudd) to carry forward?
10. Prior year skattemelding available?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| General income tax | Skatteloven |
| Alminnelig inntekt | Skatteloven ss 15-2 |
| Trinnskatt | Stortingsvedtak om skatt |
| Trygdeavgift | Folketrygdloven ss 23-3 |
| Deductibility | Skatteloven ss 6-1 |
| Depreciation | Skatteloven ss 14-40 to 14-48 |
| RF-1175 | Revenue guidance (NOK 50,000 threshold) |
| Skjermingsfradrag | Skatteloven (shields business return) |
| Filing | Skatteforvaltningsloven (30 April) |
| Penalties | Skatteforvaltningsloven kap. 14 |
| Bookkeeping | Bokføringsloven (5 years, digital) |

### Test Suite

**Test 1 -- Mid-range income.**
Input: Enkeltpersonforetak, gross NOK 800,000, expenses NOK 200,000.
Expected: Næringsinntekt NOK 600,000. Alminnelig = (600,000 - 108,550) x 22%. Trinnskatt spans Trinn 1-2. Trygdeavgift 11.0%.

**Test 2 -- High income, upper trinnskatt.**
Input: Næringsinntekt NOK 1,200,000.
Expected: Trinnskatt through Trinn 4.

**Test 3 -- Below trinnskatt threshold.**
Input: Næringsinntekt NOK 200,000.
Expected: No trinnskatt. Only alminnelig + trygdeavgift.

**Test 4 -- Minstefradrag rejected.**
Input: Client claims minstefradrag on næringsinntekt.
Expected: REJECT. Actual expenses only.

**Test 5 -- Capital item in saldogruppe.**
Input: Laptop NOK 25,000.
Expected: Saldogruppe a, 30% = NOK 7,500.

**Test 6 -- Loss carry-forward.**
Input: Prior loss NOK 150,000, current NOK 400,000.
Expected: Alminnelig base NOK 250,000. Trinnskatt/trygdeavgift on NOK 400,000.

---

## PROHIBITIONS

- NEVER apply minstefradrag to naeringsinntekt
- NEVER apply trinnskatt to alminnelig inntekt -- it applies to personinntekt
- NEVER use 7.9% trygdeavgift for naeringsinntekt -- correct rate is 11.0%
- NEVER include MVA in taxable revenue
- NEVER allow capital items over NOK 15,000 (life 3+ years) as direct expense
- NEVER deduct income tax or trygdeavgift as business expense
- NEVER allow education for new profession as deduction
- NEVER ignore personfradrag NOK 108,550
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a statsautorisert revisor, registrert revisor, or equivalent licensed practitioner in Norway) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
