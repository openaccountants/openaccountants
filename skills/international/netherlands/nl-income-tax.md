---
name: nl-income-tax
description: >
  Use this skill whenever asked about Netherlands income tax for self-employed individuals (zzp'ers, eenmanszaak). Trigger on phrases like "aangifte inkomstenbelasting", "income tax return Netherlands", "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "Box 1 income", "Box 3 wealth tax", "heffingskortingen", "arbeidskorting", "KIA investment deduction", "self-employed tax Netherlands", "winst uit onderneming", or any question about filing or computing income tax for a Dutch zzp'er or eenmanszaak. Also trigger when preparing or reviewing an aangifte IB, computing deductible expenses, or advising on voorlopige aanslagen. This skill covers Box 1 progressive rates, entrepreneur deductions, capital allowances, tax credits, Box 3 savings/investment income, filing deadlines, and penalties. ALWAYS read this skill before touching any Dutch income tax work.
version: 2.0
jurisdiction: NL
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Netherlands Income Tax -- Zzp'er / Eenmanszaak (IB) v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Tax | Inkomstenbelasting (IB) -- Box 1 (work/income), Box 2 (substantial interest), Box 3 (savings/investments) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Wet inkomstenbelasting 2001 (Wet IB 2001) |
| Tax authority | Belastingdienst |
| Filing portal | Mijn Belastingdienst (belastingdienst.nl) via DigiD |
| Filing deadline | 1 May of the following year (standard); 1 September with accountant extension |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a qualified Dutch belastingadviseur or AA/RA accountant |
| Skill version | 2.0 |

### Box 1 Rates 2025 (Inkomen uit werk en woning) [T1]

| Taxable Income (EUR) | Rate | Notes |
|---|---|---|
| 0 -- 38,441 | 35.82% | Includes national insurance (volksverzekeringen) for those below AOW age |
| 38,442 -- 76,817 | 37.48% | Above AOW threshold component |
| Over 76,817 | 49.50% | Top rate |

**AOW-gerechtigden (state pension age, born before 1 January 1958):** First bracket rate is lower (~19.17%) because they do not pay AOW premium. Confirm DOB before applying rates.

**Formula:** Tax = cumulative tax for lower bracket + (income - lower bracket threshold) x marginal rate

### Entrepreneur Deductions (Ondernemersaftrek) [T1]

| Deduction | Amount 2025 | Condition |
|---|---|---|
| Zelfstandigenaftrek | EUR 2,470 | Must meet urencriterium (>=1,225 hours/year in business) |
| Startersaftrek | EUR 2,123 (additional) | First 3 years of business; combined max EUR 4,593 for year 1-3 |
| MKB-winstvrijstelling | 12.7% of profit after other deductions | No urencriterium required -- applies to ALL entrepreneurs |

**Order of computation:**
1. Winst (profit = revenue - deductible business expenses)
2. Less: Zelfstandigenaftrek (if urencriterium met)
3. Less: Startersaftrek (if eligible)
4. Less: MKB-winstvrijstelling (12.7% of result after above deductions)
5. = Belastbaar inkomen Box 1 (from business)

### Heffingskortingen (Tax Credits -- Reduce Tax Payable) [T1]

| Credit | Amount 2025 | Notes |
|---|---|---|
| Algemene heffingskorting | Up to EUR 3,068 (phases out above EUR 24,813) | General tax credit; reduces to EUR 0 at ~EUR 76,817 |
| Arbeidskorting | Up to EUR 5,174 (phases out above EUR 43,071) | Employment/work credit; phases out at higher incomes |
| Inkomensafhankelijke combinatiekorting | Up to EUR 2,950 | For working parents with child < 12; urencriterium must be met |

Credits reduce the tax computed on Box 1 income. They cannot create a refund below EUR 0 (except toeslagen via Belastingdienst system).

### Zelfstandigenaftrek Phase-Out [T1]

The zelfstandigenaftrek is being phased down annually: EUR 2,470 in 2025, converging toward EUR 900 by 2027. Always use the current-year amount.

### Conservative Defaults [T1]

| Situation | Default Assumption |
|---|---|
| Urencriterium status unclear | Do NOT apply zelfstandigenaftrek -- flag for client to confirm hour log |
| Startersaftrek eligibility unclear | Do NOT apply -- flag; client must confirm first year of business |
| Home office deduction claimed | Do NOT deduct home costs -- Dutch rules restrict home office for zzp'ers in own home |
| Mixed personal/business expense | Non-deductible -- flag for reviewer |
| Payment received: unclear if business income | Taxable -- flag for reviewer |
| Box 3 assets unknown | Exclude -- cannot estimate; flag for client |
| Foreign income present | Flag -- possible bilateral treaty implications |

### Red Flag Thresholds [T1]

| Flag | Threshold |
|---|---|
| Hours log not maintained | Urencriterium unprovable -- zelfstandigenaftrek at risk |
| Revenue > EUR 20,000 | Check VAT (BTW) registration and KOR (kleineondernemersregeling) |
| Single client > 70% of revenue | Belastingdienst "hidden employment" risk -- flag |
| Large asset purchase > EUR 450 | KIA (kleinschaligheidsinvesteringsaftrek) may apply |
| Cash payments received | Document carefully; above EUR 3,000 unusual for zzp |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full calendar year (January-December) in CSV, PDF, or pasted text. Confirmation of whether urencriterium is met and whether startersaftrek applies.

**Recommended:** Hour log (urenstaat), all client invoices (ex-BTW), voorlopige aanslag payment receipts, Box 3 asset balances as at 1 January.

**Ideal:** Complete bookkeeping, KIA-eligible asset register, partner income details, prior year aangifte IB, BTW returns for the year.

### Refusal Catalogue

**R-NL-1 -- No hour log available.** "Cannot confirm urencriterium. Zelfstandigenaftrek is at risk without a contemporaneous hour log. Proceed without zelfstandigenaftrek and flag for client to provide evidence."

**R-NL-2 -- Client is BV director (DGA), not zzp.** "This skill covers eenmanszaak/zzp only. BV/DGA tax is fundamentally different -- escalate to a belastingadviseur."

**R-NL-3 -- Box 3 assets > EUR 57,000 per person.** "Box 3 return required. Do not estimate Box 3 tax without a full asset breakdown -- escalate."

**R-NL-4 -- Foreign income or foreign employer.** "Double-tax treaty analysis required. Stop income tax computation and escalate."

**R-NL-5 -- Revenue ex-BTW vs incl-BTW unclear.** "Income tax is computed on amounts ex-BTW. Do not mix inclusive and exclusive figures. Clarify before proceeding."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| BIJSCHRIJVING [client name] / OVERBOEKING VAN [client] | Business revenue (omzet) -- Box 1 | Gross revenue | Standard SEPA credit from client |
| CREDITERING [client] / INCASSO CREDIT | Business revenue -- Box 1 | Revenue | iDEAL/Incasso credit from client |
| FACTUURBETALING [client ref] | Business revenue -- Box 1 | Revenue | Payment referencing invoice number |
| STRIPE PAYMENTS EUROPE / STRIPE PAYOUT | Business revenue -- gross-up | Revenue | Stripe net payout; gross-up to pre-fee amount; fee deductible |
| PAYPAL TRANSFER / PAYPAL PAYOUT NL | Business revenue -- gross-up | Revenue | PayPal net; fee deductible |
| MOLLIE PAYOUT | Business revenue -- gross-up | Revenue | Mollie (Dutch payment provider) settlement; fee deductible |
| ADYEN SETTLEMENT | Business revenue -- gross-up | Revenue | Adyen merchant payout; fee deductible |
| SUMUP PAYOUT / ZETTLE PAYOUT | Business revenue -- card income | Revenue | Card terminal settlement; gross-up |
| TIKKIE ONTVANGEN / TIKKIE BETALING | Revenue (if business) / personal (if private) | Flag | Flag if large amount -- confirm business vs personal |
| RENTE / RENTE VERGOEDING | Interest income -- Box 1 (if business account) or Box 3 | NOT business revenue | Business account interest = Box 1; personal = Box 3 |
| TERUGGAAF BELASTINGDIENST / BELASTINGTERUGGAAF | EXCLUDE | Not income | Tax refund is not taxable income |
| BORG TERUG / BORGSOM TERUGBETAALD | EXCLUDE | Not income | Security deposit return |

### 3.2 Expense Patterns (Debits)

| Pattern | Tax Category | Treatment | Notes |
|---|---|---|---|
| HUUR / HUUR KANTOOR / HUURPENNING | Office rent -- 100% deductible | Fully deductible | Home office in own home: generally NOT deductible for zzp |
| VATTENFALL / VATTENFALL ENERGIE / ENECO / NUON / ESSENT | Utilities | Business portion if separate premises | NOT deductible for home office in own home |
| KPN / T-MOBILE / VODAFONE NL / ODIDO | Phone/internet -- business portion | Deductible | Mixed use: document business percentage |
| ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE / SLACK | Software subscriptions -- 100% deductible | Fully deductible | Professional software |
| ACCOUNTANT / BOEKHOUDER / ADMINISTRATIEKANTOOR | Accounting fees -- 100% deductible | Fully deductible | Tax advisor / bookkeeper fees |
| NS TREIN / NS.NL | Train travel -- deductible (business trips) | Deductible | Require purpose note; commute is debatable |
| RYANAIR / KLM / EASYJET / TRANSAVIA | Air travel -- deductible (business) | Deductible | Require itinerary + business purpose |
| HOTEL / BOOKING.COM / AIRBNB | Accommodation -- deductible (business travel) | Deductible | Personal travel = 0%; require proof |
| POSTNL / DHL / DPD | Shipping/postage -- 100% deductible | Fully deductible | Business deliveries |
| LINKEDIN PREMIUM / EXACT ONLINE / TWINFIELD | Business platform subscriptions | Fully deductible | Professional tools |
| KWARTAALBETALING BELASTINGDIENST / VOORLOPIGE AANSLAG IB | Advance tax (voorlopige aanslag) | NOT deductible | Tax payments are not business expenses |
| BTW AFDRACHT / OB BETALING | VAT payment | NOT deductible from IB | BTW is a separate tax |
| VERZEKERING / AOV / ARBEIDSONGESCHIKTHEIDSVERZEKERING | Insurance -- deductible if business or AOV | Deductible | AOV (disability) insurance: deductible |
| ZAKELIJK TANKSTATION / SHELL / BP / TOTAL | Fuel -- deductible (business vehicle portion) | Business portion | Private car: document business km |
| LEASE AUTO / LEASEPLAN / ARVAL | Vehicle lease -- deductible (business %) with bijtelling | Flag for reviewer | Complex auto fiscaliteit |
| ZAKELIJKE BANKKOSTEN / REKENING KOSTEN / RABO ZAKELIJK | Bank charges -- 100% deductible | Fully deductible | Business account fees |
| CURSUS / OPLEIDING / TRAINING | Training/education -- deductible | Fully deductible | Professional development |
| KANTOORBENODIGDHEDEN / STAPLES / OFFICECENTER | Office supplies -- 100% deductible | Fully deductible | Consumables and stationery |
| INVESTERING / AANKOOP [asset] > EUR 450 | Capital asset -- KIA eligible + depreciate | Depreciate | Do not fully expense in year 1; KIA deduction applies on top |
| MOLLIE KOSTEN / STRIPE FEES / ADYEN FEES | Payment processor fees -- 100% deductible | Fully deductible | Deduct the gross-up difference |
| EIGEN BIJDRAGE ZORGVERZEKERING | Health insurance own contribution | NOT IB deductible | Specific health deduction via zorgtoeslag |

---

## Section 4 -- Worked Examples

### Example 1 -- ING Business (Amsterdam, Web Developer)

**Input line (ING Zakelijk CSV):**
`03-01-2025;BIJSCHRIJVING CLIENTCO BV;NL12INGB...;;3500,00`

**Reasoning:**
Standard SEPA credit from a business client (BV entity). This is business revenue (omzet) for Box 1. Confirm the amount is ex-BTW. If the zzp'er invoiced EUR 3,500 + 21% BTW = EUR 4,235 total, the bank shows EUR 4,235 but IB revenue is EUR 3,500 (ex-BTW).

**Classification:** Business revenue EUR 3,500 (ex-BTW). Add to annual omzet.

### Example 2 -- Rabobank (Utrecht, Graphic Designer)

**Input line (Rabobank CSV):**
`2025-03-15;OVERBOEKING VAN STUDIO PLUS BV;NL45RABO...;+4200,00`

**Reasoning:**
Transfer from a design client. Revenue for Box 1. Lisa de Boer, graphic designer, 4th year of business (no startersaftrek). Revenue ex-BTW to be confirmed.

**Classification:** Business revenue EUR 4,200 (confirm ex-BTW).

### Example 3 -- Stripe Payout with Fee Gross-Up

**Input line (ING Zakelijk CSV):**
`15-03-2025;STRIPE PAYMENTS EUROPE;NL12INGB...;;1940,00`

**Reasoning:**
Stripe net payout EUR 1,940. Stripe collected approximately EUR 1,998 from clients and deducted ~EUR 58 in fees. Gross revenue = EUR 1,998 (ex-BTW). Stripe fee EUR 58 is a deductible business expense. Match to Stripe dashboard for exact figures.

**Classification:** Gross revenue EUR 1,998. Stripe fees EUR 58 deductible.

### Example 4 -- Voorlopige Aanslag (NOT Deductible)

**Input line (ING Zakelijk CSV):**
`15-06-2025;VOORLOPIGE AANSLAG IB;NL12INGB...;2800,00;`

**Reasoning:**
Advance income tax payment (voorlopige aanslag) EUR 2,800 to Belastingdienst. This is NOT a business expense -- it is a tax prepayment. Record as advance tax paid (credit against final IB liability). Never include in deductible expenses.

**Classification:** EXCLUDE from expenses. Record: voorlopige aanslag paid EUR 2,800.

### Example 5 -- ABN AMRO (Rotterdam, Marketing Consultant with Startersaftrek)

**Input line (ABN AMRO CSV):**
`2025-04-20;BIJSCHRIJVING MARKETINGBUREAU BV;C;5500,00`

**Reasoning:**
Credit from marketing client. Jan Smit is in year 2 of business -- startersaftrek eligible (EUR 2,123 additional deduction on top of zelfstandigenaftrek EUR 2,470). Revenue EUR 5,500 (confirm ex-BTW).

**Classification:** Business revenue EUR 5,500. Flag: startersaftrek year 2 -- confirm eligibility.

### Example 6 -- Bunq Business (Eindhoven, IT Freelancer -- Single Client Flag)

**Input line (Bunq CSV):**
`2025-05-01,90000.00,NL88BUNQ...,TECHBV EINDHOVEN,NL12INGB...,MAANDELIJKSE FACTUUR`

**Reasoning:**
Large single credit from one BV entity. Revenue EUR 90,000. Single client > 70% of revenue triggers schijnzelfstandigheid (hidden employment) risk. Belastingdienst enforcement increased from 2025. Flag for reviewer.

**Classification:** Business revenue EUR 90,000 (ex-BTW). RED FLAG: single client > 70% -- schijnzelfstandigheid risk.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Revenue Is Always Ex-BTW

All income tax computations use revenue and expenses exclusive of BTW (VAT). Amounts including BTW must be stripped before processing. BTW is a separate tax; it is neither income nor an expense for IB purposes.

### 5.2 MKB-Winstvrijstelling Is Mandatory

**Legislation:** Art. 3.79a Wet IB 2001

The 12.7% MKB-winstvrijstelling applies to ALL entrepreneurs (eenmanszaak, VOF, maatschap) regardless of whether urencriterium is met. Always apply it after other entrepreneur deductions. Never omit it.

### 5.3 Voorlopige Aanslag Is Not Deductible

Advance income tax payments (voorlopige aanslag IB) paid to Belastingdienst are tax prepayments, not business expenses. Never include IB payment narrations as deductible expenses.

### 5.4 BTW Afdracht Is Not Deductible

Quarterly BTW payments (OB/BTW afdracht) are not a business expense for IB purposes. Exclude all BTW payment narrations from the expense calculation.

### 5.5 KIA Deduction Requires >= EUR 2,801 in New Business Assets

**Legislation:** Art. 3.41 Wet IB 2001

Kleinschaligheidsinvesteringsaftrek applies only when total qualifying asset purchases exceed EUR 2,801 in the year. Assets < EUR 450 per item do not qualify. KIA is 28% for investments EUR 2,801-69,765. KIA applies in addition to normal depreciation.

### 5.6 Home Office Deduction: Strict Rules

A zzp'er working from home cannot generally deduct a portion of home expenses (mortgage interest, rent, utilities) unless they have a separate, self-contained workspace that could be let independently. The default is: home office in own home = NOT deductible. Flag any home office claim for reviewer.

### 5.7 Urencriterium: 1,225 Hours Minimum

**Legislation:** Art. 3.76 Wet IB 2001

Zelfstandigenaftrek requires the entrepreneur to have worked >= 1,225 hours in the business during the year. Without a contemporaneous hour log, the claim cannot be substantiated. Never assume urencriterium is met -- always require the log.

### 5.8 Tax Computation Flow

```
Revenue (omzet, ex-BTW)
Less: Deductible business expenses
= Winst (profit)
Less: Zelfstandigenaftrek (if urencriterium met)
Less: Startersaftrek (if eligible, years 1-3)
Less: KIA (if qualifying investments >= EUR 2,801)
= Subtotal
Less: MKB-winstvrijstelling (12.7% of subtotal)
= Belastbaar inkomen Box 1
Apply bracket rates
= Box 1 tax
Less: Algemene heffingskorting
Less: Arbeidskorting
Less: Other kortingen
= Net Box 1 tax
Less: Voorlopige aanslag paid
= Balance due / (refund)
```

### 5.9 Filing Deadlines

| Item | Deadline |
|---|---|
| Standard aangifte IB | 1 May of the following year |
| Extended deadline (with accountant) | 1 September |
| Voorlopige aanslag request/revision | 1 July each year |

### 5.10 Penalties

| Offence | Penalty |
|---|---|
| Late filing | EUR 385 verzuimboete (standard) |
| Failure to file after reminder | Up to EUR 5,514 |
| Under-reporting (vergrijpboete) | 25%-100% of additional tax |
| Deliberate fraud | Up to 300% of tax evaded |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Single Client > 70% of Revenue (Schijnzelfstandigheid)

Belastingdienst may reclassify the arrangement as employment. Flag and advise client to diversify or obtain a modelovereenkomst.

### 6.2 AOW-Leeftijd (State Pension Age)

First bracket rate differs significantly (~19.17% vs 35.82%). Confirm DOB; apply lower rate only if born before 1 January 1958.

### 6.3 Box 3 Wealth Tax

Box 3 rate/return computation is contested in courts (Hoge Raad Kerst-arrest). Compute at current statutory rates: savings ~1.44%, investments ~5.88%, Box 3 tax rate 36%. Heffingvrij vermogen EUR 57,000 per person (EUR 114,000 for fiscal partners). Note litigation uncertainty.

### 6.4 Company Car (Auto van de Zaak)

Bijtelling (benefit in kind) required. Complex auto fiscaliteit -- bijtelling % depends on CO2 emissions and first registration date. Flag for reviewer.

### 6.5 International Assignment or Partial-Year Residency

30% ruling may apply. Non-resident rules require bilateral treaty analysis. Flag and escalate.

### 6.6 Fiscal Partner Income

Heffingskortingen can be transferred between fiscal partners in some cases. Flag for fiscal partner analysis.

### 6.7 WBSO (R&D Subsidy)

WBSO subsidy reduces payable wage tax. Separate S&O administration required. Flag -- WBSO is claimed separately, not via IB return.

---

## Section 7 -- Excel Working Paper Template

```
NETHERLANDS INCOME TAX WORKING PAPER (ZZP / EENMANSZAAK)
Taxpayer: _______________  BSN: _______________  FY: 2025

SECTION A -- REVENUE (ex-BTW)
                                        EUR
Gross revenue (all clients, ex-BTW)    ___________
Less: credit notes / returns           (___________)
Net revenue                            ___________

SECTION B -- DEDUCTIBLE BUSINESS EXPENSES
Rent / workspace (business only)       ___________
Utilities (business premises only)     ___________
Phone / internet (business %)          ___________
Software subscriptions                 ___________
Accountant / bookkeeper                ___________
Legal fees                             ___________
Training / CPD                         ___________
Travel (business trips)                ___________
Accommodation (business travel)        ___________
Business insurance (AOV, liability)    ___________
Business bank charges                  ___________
Depreciation (afschrijving)            ___________
Payment processor fees                 ___________
Other business expenses                ___________
TOTAL DEDUCTIBLE EXPENSES              ___________

SECTION C -- PROFIT (WINST)
Net revenue - Total expenses           ___________

SECTION D -- ENTREPRENEUR DEDUCTIONS (ONDERNEMERSAFTREK)
Zelfstandigenaftrek (if uren met)      ___________
Startersaftrek (if eligible yr 1-3)    ___________
KIA (kleinschaligheidsinvesteringsaftrek) ________
Subtotal after deductions              ___________
MKB-winstvrijstelling (12.7%)         (___________)
BELASTBAAR INKOMEN BOX 1               ___________

SECTION E -- BOX 1 TAX COMPUTATION
Tax at bracket rates (see table)       ___________
Less: Algemene heffingskorting         (___________)
Less: Arbeidskorting                   (___________)
Less: Other kortingen                  (___________)
BOX 1 NET TAX                          ___________

SECTION F -- ADVANCE PAYMENTS
Voorlopige aanslag paid                (___________)
IB balance due / (refund)              ___________

SECTION G -- BOX 3 (if applicable)
Assets on 1 January (incl. bank saldo) ___________
Less: heffingvrij vermogen EUR 57,000  (___________)
Grondslag Box 3                        ___________
Fictitious return (see rates by class) ___________
Box 3 tax @ 36%                        ___________

SECTION H -- REVIEWER FLAGS
[ ] Urencriterium -- hour log reviewed?
[ ] Startersaftrek -- year 1/2/3 confirmed?
[ ] Single client > 70%? Schijnzelfstandigheid flag
[ ] BTW stripped from all revenue/expense amounts
[ ] KIA -- qualifying assets > EUR 2,801?
[ ] Box 3 assets declared on 1 January balance
[ ] AOW age check (DOB before 1 January 1958?)
```

---

## Section 8 -- Bank Statement Reading Guide

### Dutch Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| ING Zakelijk | CSV | Datum;Naam/Omschrijving;Rekening;Tegenrekening;Code;Af Bij;Bedrag (EUR);Mutatiesoort;Mededelingen |
| Rabobank | CSV | IBAN;Munt;BIC;Volgnr;Datum;Rentedatum;Bedrag;Saldo na trn;Tegenrekening;Naam tegenpartij;Omschrijving |
| ABN AMRO | CSV / MT940 | Transactiedatum;Valutacode;CreditDebet;Bedrag;Tegenrekening IBAN;Naam tegenpartij;Omschrijving |
| Bunq | CSV (app export) | date,amount,account,counterparty_name,counterparty_iban,description |
| Knab Business | CSV / Excel | Standard Dutch format; comma decimal amounts |
| SNS Bank | CSV | Boekdatum;Naam;Rekening;Tegenrekening;Code;Debet/Credit;Bedrag;Mededelingen;Saldo |

### Key Dutch Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| BIJSCHRIJVING [name] | Credit transfer in | Potential business income |
| OVERBOEKING VAN [name] | Transfer from | Potential business income |
| INCASSO | Direct debit | Recurring expense |
| BETAALAUTOMAAT / PIN | Card payment | Identify payee |
| GELDAUTOMAAT / ATM | Cash withdrawal | Personal -- investigate |
| VOORLOPIGE AANSLAG | Advance tax payment | Tax prepayment -- exclude |
| BTW AFDRACHT / OB BETALING | VAT payment | Separate tax -- exclude |
| RENTE | Interest | Other income (Box 1 or 3) |
| ZORGTOESLAG / HUURTOESLAG | Government benefit | Not taxable income |

### Amount Format Notes

- ING: `Af Bij` column = `Af` (debit) or `Bij` (credit); Bedrag is always positive
- Rabobank: negative = debit, positive = credit
- ABN AMRO: `CreditDebet` = `C` (credit) or `D` (debit)
- Bunq: positive = credit, negative = debit; period decimal
- Date formats: DD-MM-YYYY (most Dutch banks)

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all BIJSCHRIJVING/OVERBOEKING credits from BV/VOF entities as potential business revenue
2. Apply conservative defaults: no zelfstandigenaftrek (urencriterium unproven), no startersaftrek
3. Exclude all VOORLOPIGE AANSLAG and BTW AFDRACHT debits from expenses
4. Mark all Stripe/PayPal/Mollie for gross-up
5. Flag any single client > 70% of credits
6. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- NETHERLANDS INCOME TAX (IB)
1. Do you maintain an urenstaat (hour log) showing >= 1,225 hours?
2. Is this your first, second, or third year in business? (Startersaftrek eligibility)
3. Are all invoice amounts ex-BTW or incl-BTW?
4. Are you BTW-plichtig? If so, are you in the KOR scheme (< EUR 20,000)?
5. Date of birth? (For AOW-age bracket rate check)
6. Did you pay a voorlopige aanslag this year? If so, how much?
7. Box 3: what were your total savings/investments on 1 January 2025?
8. Do you have a fiscal partner? If so, their income?
9. Did you purchase any business assets > EUR 450 this year? (KIA eligibility)
10. Do you have a dedicated, independently lettable workspace at home?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Income tax (general) | Wet inkomstenbelasting 2001 (Wet IB 2001) |
| Zelfstandigenaftrek | Art. 3.76 Wet IB |
| Startersaftrek | Art. 3.78 Wet IB |
| MKB-winstvrijstelling | Art. 3.79a Wet IB |
| KIA (investment deduction) | Art. 3.41 Wet IB |
| Urencriterium | Art. 3.76(1) Wet IB |
| Box 3 wealth tax | Art. 5.1-5.3 Wet IB |
| Heffingskortingen | Art. 8.10 et seq. Wet IB |

### Known Gaps / Out of Scope

- BV/DGA taxation (separate regime)
- International income and bilateral treaties
- 30% ruling
- Box 2 (substantial interest in BV)
- Complex auto fiscaliteit (bijtelling calculations)
- WBSO R&D subsidy administration

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Dutch bank formats (ING, Rabobank, ABN AMRO, Bunq); transaction pattern library; Mollie/Adyen patterns; worked examples; PROHIBITIONS and disclaimer added |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] All amounts ex-BTW?
- [ ] Urencriterium confirmed before applying zelfstandigenaftrek?
- [ ] MKB-winstvrijstelling (12.7%) applied after all other deductions?
- [ ] Voorlopige aanslag excluded from expenses?
- [ ] BTW payments excluded from expenses?
- [ ] KIA threshold (EUR 2,801 minimum) checked?
- [ ] Home office deduction: independently lettable workspace confirmed?
- [ ] AOW age checked for first bracket rate?
- [ ] Single client concentration flagged if > 70%?

---

## PROHIBITIONS

- NEVER apply zelfstandigenaftrek without a confirmed urenstaat showing >= 1,225 hours
- NEVER omit MKB-winstvrijstelling -- it applies to ALL entrepreneurs regardless of urencriterium
- NEVER include voorlopige aanslag (IB advance payments) as a deductible business expense
- NEVER include BTW afdracht as an IB expense -- BTW is a separate tax
- NEVER deduct home office costs for a zzp'er without confirming an independently lettable workspace
- NEVER include BTW-inclusive amounts in revenue or expense calculations -- always strip BTW first
- NEVER fully expense assets > EUR 450 in year one -- apply depreciation schedule and KIA separately
- NEVER ignore the schijnzelfstandigheid risk when a single client exceeds 70% of revenue
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their belastingadviseur for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a belastingadviseur, AA, RA, or equivalent licensed practitioner in the Netherlands) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
