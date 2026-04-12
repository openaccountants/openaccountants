---
name: nl-income-tax
description: >
  Use this skill whenever asked about Netherlands income tax for self-employed individuals (zzp'ers, eenmanszaak). Trigger on phrases like "aangifte inkomstenbelasting", "income tax return Netherlands", "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "Box 1 income", "Box 3 wealth tax", "heffingskortingen", "arbeidskorting", "KIA investment deduction", "self-employed tax Netherlands", "winst uit onderneming", or any question about filing or computing income tax for a Dutch zzp'er or eenmanszaak. Also trigger when preparing or reviewing an aangifte IB, computing deductible expenses, or advising on voorlopige aanslagen. This skill covers Box 1 progressive rates, entrepreneur deductions, capital allowances, tax credits, Box 3 savings/investment income, filing deadlines, and penalties. ALWAYS read this skill before touching any Dutch income tax work.
version: 2.0
---

# Netherlands Income Tax — Zzp'er / Eenmanszaak (IB) v2.0

## Section 1 — Quick Reference

### Box 1 Rates 2025 (Inkomen uit werk en woning)

| Taxable Income (EUR) | Rate | Notes |
|---|---|---|
| 0 – 38,441 | 35.82% | Includes national insurance (volksverzekeringen) for those below AOW age |
| 38,442 – 76,817 | 37.48% | Above AOW threshold component |
| Over 76,817 | 49.50% | Top rate |

**AOW-gerechtigden (state pension age, born before 1 January 1958):** First bracket rate is lower (~19.17%) because they do not pay AOW premium. Confirm DOB before applying rates.

**Formula:** Tax = cumulative tax for lower bracket + (income − lower bracket threshold) × marginal rate

### Entrepreneur Deductions (Ondernemersaftrek)

| Deduction | Amount 2025 | Condition |
|---|---|---|
| Zelfstandigenaftrek | EUR 2,470 | Must meet urencriterium (≥ 1,225 hours/year in business) |
| Startersaftrek | EUR 2,123 (additional) | First 3 years of business; combined max EUR 4,593 for year 1–3 |
| MKB-winstvrijstelling | 13.31% of profit after other deductions | No urencriterium required — applies to ALL entrepreneurs |

**Order of computation:**
1. Winst (profit = revenue − deductible business expenses)
2. Less: Zelfstandigenaftrek (if urencriterium met)
3. Less: Startersaftrek (if eligible)
4. Less: MKB-winstvrijstelling (13.31% of result after above deductions)
5. = Belastbaar inkomen Box 1 (from business)

### Heffingskortingen (Tax Credits — Reduce Tax Payable)

| Credit | Amount 2025 | Notes |
|---|---|---|
| Algemene heffingskorting | Up to EUR 3,068 (phases out above EUR 24,813) | General tax credit; reduces to EUR 0 at ~EUR 76,817 |
| Arbeidskorting | Up to EUR 5,174 (phases out above EUR 43,071) | Employment/work credit; phases out at higher incomes |
| Inkomensafhankelijke combinatiekorting | Up to EUR 2,950 | For working parents with child < 12; urencriterium must be met |

Credits reduce the tax computed on Box 1 income. They cannot create a refund below EUR 0 (except toeslagen via Belastingdienst system).

### Zelfstandigenaftrek Phase-Out

The zelfstandigenaftrek is being phased down annually: EUR 2,470 in 2025, converging toward EUR 900 by 2027. Always use the current-year amount.

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Urencriterium status unclear | Do NOT apply zelfstandigenaftrek — flag for client to confirm hour log |
| Startersaftrek eligibility unclear | Do NOT apply — flag; client must confirm first year of business |
| Home office deduction claimed | Do NOT deduct home costs — Dutch rules restrict home office for zzp'ers in own home |
| Mixed personal/business expense | Non-deductible — flag for reviewer |
| Payment received: unclear if business income | Taxable — flag for reviewer |
| Box 3 assets unknown | Exclude — cannot estimate; flag for client |
| Foreign income present | Flag — possible bilateral treaty implications |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Hours log not maintained | Urencriterium unprovable — zelfstandigenaftrek at risk |
| Revenue > EUR 20,000 | Check VAT (BTW) registration and KOR (kleineondernemersregeling) |
| Single client > 70% of revenue | Belastingdienst "hidden employment" risk — flag |
| Large asset purchase > EUR 450 | KIA (kleinschaligheidsinvesteringsaftrek) may apply |
| Cash payments received | Document carefully; above EUR 3,000 unusual for zzp |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing Dutch income tax, collect:

1. **Total revenue** (omzet) — all amounts invoiced and received, ex-BTW
2. **Itemised business expenses** — with bank or receipt evidence
3. **Hour log** (urenstaat) — to verify urencriterium (≥ 1,225 hours)
4. **Business start date** — to determine startersaftrek eligibility
5. **Date of birth** — to apply correct first-bracket rate (AOW threshold)
6. **Bank statements** — 12 months for the fiscal year
7. **Voorlopige aanslag payments made** — advance tax payments
8. **Box 3 assets** (savings, investments, second property) as at 1 January of the tax year
9. **Partner income** — for heffingskortingen calculation (partner's credits affect allocation)
10. **KIA-eligible investments** — assets purchased (> EUR 450, not cars, land, goodwill)

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-NL-1 | No hour log available | Stop — cannot confirm urencriterium; flag zelfstandigenaftrek as at risk |
| R-NL-2 | Client is BV director (DGA), not zzp | Stop — this skill covers eenmanszaak/zzp only; BV/DGA tax is different |
| R-NL-3 | Box 3 assets > EUR 57,000 per person | Box 3 return required; do not estimate Box 3 tax without asset breakdown |
| R-NL-4 | Foreign income or foreign employer | Flag — double-tax treaty analysis required; stop income tax computation |
| R-NL-5 | Revenue reported ex-BTW vs. incl-BTW unclear | Clarify — income tax is computed on amounts ex-BTW; do not mix |

---

## Section 3 — Transaction Pattern Library

### Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `BIJSCHRIJVING [client name]` / `OVERBOEKING VAN [client]` | Business revenue (omzet) — Box 1 | Standard SEPA credit from client |
| I-02 | `CREDITERING [client]` / `INCASSO CREDIT` | Business revenue — Box 1 | iDEAL/Incasso credit from client |
| I-03 | `STRIPE PAYMENTS EUROPE` / `STRIPE PAYOUT` | Business revenue — gross-up | Stripe net payout; gross-up to pre-fee amount; fee deductible |
| I-04 | `PAYPAL TRANSFER` / `PAYPAL PAYOUT NL` | Business revenue — gross-up | PayPal net; fee deductible |
| I-05 | `MOLLIE PAYOUT` | Business revenue — gross-up | Mollie (Dutch payment provider) settlement; fee deductible |
| I-06 | `ADYEN SETTLEMENT` | Business revenue — gross-up | Adyen merchant payout; fee deductible |
| I-07 | `SUMUP PAYOUT` / `ZETTLE PAYOUT` | Business revenue — card income | Card terminal settlement; gross-up |
| I-08 | `RENTE` / `RENTE VERGOEDING` | Interest income — Box 1 (if business account) or Box 3 | Business account interest → Box 1; personal → Box 3 |
| I-09 | `TERUGGAAF BELASTINGDIENST` / `BELASTINGTERUGGAAF` | NOT income — tax refund | Tax refund is not taxable income |
| I-10 | `BORG TERUG` / `BORGSOM TERUGBETAALD` | Non-taxable deposit return | If documented as security deposit return |
| I-11 | `FACTUURBETALING [client ref]` | Business revenue — Box 1 | Payment referencing invoice number |
| I-12 | `TIKKIE ONTVANGEN` / `TIKKIE BETALING` | Revenue (if business) / personal (if private) | Flag if large amount — confirm business vs. personal |

### Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `HUUR` / `HUUR KANTOOR` / `HUURPENNING` | Office rent — 100% deductible | Home office in own home: generally NOT deductible for zzp |
| E-02 | `VATTENFALL` / `VATTENFALL ENERGIE` / `ENECO` / `NUON` / `ESSENT` | Utilities — deductible if separate business premises | NOT deductible for home office in own home |
| E-03 | `KPN` / `T-MOBILE` / `VODAFONE NL` / `ODIDO` | Phone/internet — deductible (business portion) | Mixed use: document business percentage |
| E-04 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` / `SLACK` | Software subscriptions — 100% deductible | Professional software |
| E-05 | `ACCOUNTANT` / `BOEKHOUDER` / `ADMINISTRATIEKANTOOR` | Accounting fees — 100% deductible | Tax advisor / bookkeeper fees |
| E-06 | `NS TREIN` / `NS.NL` | Train travel — deductible (business trips) | Require purpose note; commute home-work for zzp is debatable |
| E-07 | `RYANAIR` / `KLM` / `EASYJET` / `TRANSAVIA` | Air travel — deductible (business purpose) | Require itinerary + business purpose |
| E-08 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation — deductible (business travel) | Personal travel = 0%; require proof of business purpose |
| E-09 | `POSTNL` / `DHL` / `DPD` | Shipping/postage — 100% deductible | Business deliveries and mailings |
| E-10 | `LINKEDIN PREMIUM` / `EXACT ONLINE` / `TWINFIELD` | Business platform subscriptions — 100% deductible | Professional tools |
| E-11 | `KWARTAALBETALING BELASTINGDIENST` / `VOORLOPIGE AANSLAG IB` | Advance tax (voorlopige aanslag) — NOT deductible | Tax payments are not business expenses |
| E-12 | `BTW AFDRACHT` / `OB BETALING` | VAT payment — NOT deductible from IB | BTW is a separate tax; not an IB expense |
| E-13 | `VERZEKERING` / `AOV` / `ARBEIDSONGESCHIKTHEIDSVERZEKERING` | Insurance — deductible if business or AOV | AOV (disability) insurance: deductible; private health/life: via Zorgverzekeringswet |
| E-14 | `ZAKELIJK TANKSTATION` / `SHELL` / `BP` / `TOTAL` | Fuel — deductible (business vehicle portion) | Private car: document business km; lease car: see BPM/auto rules |
| E-15 | `LEASE AUTO` / `LEASEPLAN` / `ARVAL` | Vehicle lease — deductible (business %) with bijtelling | Complex auto fiscaliteit — flag for reviewer |
| E-16 | `ZAKELIJKE BANKKOSTEN` / `REKENING KOSTEN` / `RABO ZAKELIJK` | Bank charges — 100% deductible | Business account fees |
| E-17 | `CURSUS` / `OPLEIDING` / `TRAINING` | Training/education — deductible | Professional development; personal courses = 0% |
| E-18 | `KANTOORBENODIGDHEDEN` / `STAPLES` / `OFFICECENTER` | Office supplies — 100% deductible | Consumables and stationery |
| E-19 | `INVESTERING` / `AANKOOP [asset]` > EUR 450 | Capital asset — KIA eligible + depreciate | Do not fully expense in year 1; KIA deduction applies on top of depreciation |
| E-20 | `KLEINSCHALIGHEIDSINVESTERINGSAFTREK` | Not a payment — KIA deduction entry | Computed at year end (28% for EUR 2,801–69,765; scales for higher amounts) |
| E-21 | `MOLLIE KOSTEN` / `STRIPE FEES` / `ADYEN FEES` | Payment processor fees — 100% deductible | Deduct the gross-up difference |
| E-22 | `EIGEN BIJDRAGE ZORGVERZEKERING` | Health insurance own contribution — NOT IB deductible | Specific health deduction via zorgtoeslag, not IB expense |

---

## Section 4 — Worked Examples

### Example 1 — ING Business (Amsterdam, Web Developer)

**Bank:** ING Zakelijk CSV export
**Client:** Pieter van den Berg, web developer, Amsterdam

```
Datum;Naam/Omschrijving;Rekening;Tegenrekening;Bedrag
03-01-2025;BIJSCHRIJVING CLIENTCO BV;NL12INGB...; ;3500,00
15-01-2025;KOSTEN ZAKELIJKE REKENING;NL12INGB...; ;-6,00
10-02-2025;BIJSCHRIJVING STARTUP NL BV;NL12INGB...; ;4200,00
28-02-2025;KPN ZAKELIJK FACTUUR;NL12INGB...; ;-65,00
15-03-2025;STRIPE PAYMENTS EUROPE;NL12INGB...; ;1940,00
01-04-2025;ADOBE CREATIVE CLOUD;NL12INGB...; ;-59,99
20-04-2025;BIJSCHRIJVING AGENCY PLUS BV;NL12INGB...; ;5500,00
15-06-2025;VOORLOPIGE AANSLAG IB;NL12INGB...; ;-2800,00
10-07-2025;ACCOUNTANT DE VRIES;NL12INGB...; ;-750,00
10-10-2025;NS TREIN AMSTERDAM-ROTTERDAM;NL12INGB...; ;-45,00
```

**Step 1 — Revenue (ex-BTW)**

| Narration | Pattern | Amount (ex-BTW) |
|---|---|---|
| BIJSCHRIJVING CLIENTCO BV | I-01 | EUR 3,500 (confirm ex-BTW) |
| BIJSCHRIJVING STARTUP NL BV | I-01 | EUR 4,200 |
| STRIPE PAYMENTS EUROPE | I-03 | EUR 1,940 net → gross ~EUR 1,998 |
| BIJSCHRIJVING AGENCY PLUS BV | I-01 | EUR 5,500 |
| **Total revenue** | | **EUR 15,198** |

**Step 2 — Deductible Expenses**

| Narration | Pattern | Amount | Deductible |
|---|---|---|---|
| KOSTEN ZAKELIJKE REKENING | E-16 | EUR 72/yr | EUR 72 |
| KPN ZAKELIJK | E-03 | EUR 780/yr | EUR 780 (100% business) |
| ADOBE CREATIVE CLOUD | E-04 | EUR 720/yr | EUR 720 |
| ACCOUNTANT | E-05 | EUR 750 | EUR 750 |
| NS TREIN | E-06 | EUR 45 | EUR 45 |
| STRIPE FEES | E-21 | ~EUR 58 | EUR 58 |
| VOORLOPIGE AANSLAG IB | E-11 | EUR 2,800 | EUR 0 |
| **Total deductible** | | | **EUR 2,425** |

**Step 3 — Profit (Winst)**

```
Revenue:            EUR 15,198
Less expenses:      EUR  2,425
Winst:              EUR 12,773
```

**Step 4 — Entrepreneur Deductions**

```
Zelfstandigenaftrek (urencriterium assumed met): EUR 2,470
MKB-winstvrijstelling: 13.31% × (12,773 − 2,470) = 13.31% × 10,303 = EUR 1,371.33
Belastbaar inkomen Box 1: 12,773 − 2,470 − 1,371 = EUR 8,932
```

**Step 5 — IRPEF Box 1 Tax**

```
EUR 8,932 × 35.82% = EUR 3,200.87
Less: Algemene heffingskorting (income EUR 8,932 — below phase-out): ~EUR 3,068
Less: Arbeidskorting (income EUR 8,932): ~EUR 1,850 (scales with income)
Note: Credits cannot reduce tax below EUR 0; excess via toeslagen system
Box 1 net tax: EUR 3,200.87 − EUR 3,068 = EUR 132.87 (arbeidskorting already covered)
```

Practical: at this income level heffingskortingen likely reduce tax to near zero. Flag for detailed credit calculation.

---

### Example 2 — Rabobank (Utrecht, Graphic Designer)

**Bank:** Rabobank MT940/CSV export
**Client:** Lisa de Boer, graphic designer, Utrecht, 4th year of business (no startersaftrek)

Key transactions:
- OVERBOEKING VAN clients: EUR 42,000 total revenue
- MOLLIE PAYOUT: EUR 8,000 (net); gross ~EUR 8,250
- Total revenue: EUR 50,250

Expenses: accountant EUR 900, software EUR 1,200, training EUR 500, phone/internet EUR 960, bank charges EUR 84, travel EUR 300

Total expenses: EUR 3,944

Winst: EUR 50,250 − EUR 3,944 = EUR 46,306
Zelfstandigenaftrek: EUR 2,470
MKB: 13.31% × (46,306 − 2,470) = 13.31% × 43,836 = EUR 5,834.17
Belastbaar Box 1: EUR 46,306 − EUR 2,470 − EUR 5,834 = **EUR 38,002**

Box 1 tax: EUR 38,002 × 35.82% (all in first bracket) = EUR 13,614.72
Less heffingskortingen (phase-out at EUR 24,813 — income > EUR 24,813 so AHK phases out)
AHK at EUR 38,002: EUR 3,068 − [(38,002 − 24,813) × 6.095%] = EUR 3,068 − EUR 804.06 = EUR 2,263.94
Arbeidskorting at EUR 38,002: ~EUR 4,606 (check table; phases down above EUR 43,071)
Net tax: EUR 13,614.72 − EUR 2,263.94 − EUR 4,606 = **EUR 6,744.78**

---

### Example 3 — ABN AMRO (Rotterdam, Marketing Consultant)

**Bank:** ABN AMRO CSV
**Client:** Jan Smit, marketing consultant, Rotterdam, year 2 of business (startersaftrek eligible)

Revenue: EUR 65,000 (multiple BIJSCHRIJVING narrations)

Entrepreneur deductions:
- Zelfstandigenaftrek: EUR 2,470
- Startersaftrek: EUR 2,123
- MKB: 13.31% × (65,000 − 2,470 − 2,123) = 13.31% × 60,407 = EUR 8,040.17

Belastbaar: EUR 65,000 − EUR 2,470 − EUR 2,123 − EUR 8,040 = **EUR 52,367**

Box 1 tax:
EUR 38,441 × 35.82% = EUR 13,771.37
(EUR 52,367 − EUR 38,441) × 37.48% = EUR 13,926 × 37.48% = EUR 5,219.47
Total: EUR 18,990.84

AHK at EUR 52,367: phases out further; estimated ~EUR 1,200
Arbeidskorting at EUR 52,367: ~EUR 4,052 (starts phasing at EUR 43,071)
Net tax: EUR 18,990.84 − EUR 1,200 − EUR 4,052 = **EUR 13,738.84**

Flag: Confirm startersaftrek — must be within first 3 years, and urencriterium met in current year AND at least 1 of prior 5 years did NOT meet urencriterium.

---

### Example 4 — Bunq Business (Eindhoven, IT Freelancer)

**Bank:** Bunq CSV ("Export" in app)
**Client:** Sophie Willems, IT freelancer, Eindhoven, single client (>70% revenue)

Note: Single client > 70% revenue — flag potential "hidden employment" (schijnzelfstandigheid) risk. Belastingdienst enforcement on this increased from 2025.

Revenue: EUR 90,000 (single BIJSCHRIJVING from one BV)
KIA eligible: laptop EUR 2,200 + server EUR 1,800 = EUR 4,000

KIA deduction: 28% × EUR 4,000 = EUR 1,120 (investments EUR 2,801–EUR 69,765 range)

Expenses (total): EUR 12,000
Winst: EUR 90,000 − EUR 12,000 − EUR 1,120 (KIA) = EUR 76,880
Zelfstandigenaftrek: EUR 2,470
MKB: 13.31% × (76,880 − 2,470) = EUR 9,910.31
Belastbaar: EUR 76,880 − EUR 2,470 − EUR 9,910 = **EUR 64,500**

Box 1 tax:
EUR 38,441 × 35.82% + (EUR 64,500 − EUR 38,441) × 37.48%
= EUR 13,771 + EUR 9,762.91 = EUR 23,533.91

AHK: ~EUR 0 (income > EUR 76,817 phase-out threshold — actually ~EUR 0 at EUR 64,500 it's still partly there)
Net tax: approximately **EUR 18,000–19,000** (detailed credit calculation required)

Flag: Schijnzelfstandigheid risk — single client structure.

---

### Example 5 — Knab Business (Den Haag, Consultant)

**Bank:** Knab business account export (Excel format)
**Client:** Thomas Bakker, management consultant, Den Haag

Box 3 reminder: If Thomas has savings > EUR 57,000 (heffingvrij vermogen) on 1 January 2025, Box 3 wealth tax applies separately. Box 3 fictitious return rates vary by asset class (2025 rates: savings ~1.44%, investments ~5.88%, other ~5.88%). Box 3 tax rate: 36%.

This example: Box 3 flagged — Thomas has bank savings EUR 120,000. Flag for Box 3 calculation:
Excess above heffingvrij: EUR 120,000 − EUR 57,000 = EUR 63,000
Fictitious return (savings rate 1.44%): EUR 63,000 × 1.44% = EUR 907.20
Box 3 tax: EUR 907.20 × 36% = **EUR 326.59**

Note: Box 3 is additional to Box 1 IB; total tax = Box 1 + Box 3.

---

### Example 6 — SNS Bank (Groningen, Photographer)

**Bank:** SNS Bank CSV
**Client:** Emma Jansen, photographer, Groningen, first year of business

Eligibility check: First year → startersaftrek applies if urencriterium met.
Revenue: EUR 18,000 (below EUR 20,000 — check BTW KOR eligibility)

Winst: EUR 18,000 − EUR 2,800 (expenses) = EUR 15,200
Zelfstandigenaftrek: EUR 2,470
Startersaftrek: EUR 2,123
MKB: 13.31% × (15,200 − 2,470 − 2,123) = 13.31% × 10,607 = EUR 1,411.79
Belastbaar: EUR 15,200 − EUR 2,470 − EUR 2,123 − EUR 1,412 = **EUR 9,195**

Box 1 tax: EUR 9,195 × 35.82% = EUR 3,294.47
Heffingskortingen likely cover most/all at this income — net tax approximately **EUR 0–500**

BTW flag: Revenue EUR 18,000 > EUR 0 — KOR (kleineondernemersregeling) available if ≤ EUR 20,000 annually. If KOR applied, no BTW filing required. Confirm KOR registration.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-NL-1 — Revenue is always ex-BTW**
All income tax computations use revenue and expenses exclusive of BTW (VAT). Amounts including BTW must be stripped before processing. BTW is a separate tax; it is neither income nor an expense for IB purposes.

**T1-NL-2 — MKB-winstvrijstelling is mandatory**
The 13.31% MKB-winstvrijstelling applies to ALL entrepreneurs (eenmanszaak, VOF, maatschap) regardless of whether urencriterium is met. Always apply it after other entrepreneur deductions. Never omit it.

**T1-NL-3 — Voorlopige aanslag is not deductible**
Advance income tax payments (voorlopige aanslag IB) paid to Belastingdienst are tax prepayments, not business expenses. Never include F-prefix or IB payment narrations as deductible expenses.

**T1-NL-4 — BTW afdracht is not deductible**
Quarterly BTW payments (OB/BTW afdracht) are not a business expense for IB purposes. Exclude all BTW payment narrations from the expense calculation.

**T1-NL-5 — KIA deduction requires ≥ EUR 2,801 in new business assets**
Kleinschaligheidsinvesteringsaftrek applies only when total qualifying asset purchases exceed EUR 2,801 in the year. Assets < EUR 450 per item do not qualify. KIA applies in addition to normal depreciation.

**T1-NL-6 — Home office deduction: strict rules**
A zzp'er working from home cannot generally deduct a portion of home expenses (mortgage interest, rent, utilities) unless they have a separate, self-contained workspace that could be let independently. The default is: home office in own home = NOT deductible. Flag any home office claim for reviewer.

**T1-NL-7 — Urencriterium: 1,225 hours minimum**
Zelfstandigenaftrek requires the entrepreneur to have worked ≥ 1,225 hours in the business during the year. Without a contemporaneous hour log, the claim cannot be substantiated. Never assume urencriterium is met — always require the log.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-NL-1 | Single client > 70% of revenue | Schijnzelfstandigheid risk — Belastingdienst may reclassify as employment | Flag; advise client to diversify or obtain a modelovereenkomst |
| T2-NL-2 | AOW-leeftijd question (state pension age) | First bracket rate differs significantly (~19.17% vs 35.82%) | Confirm DOB; apply lower rate only if born before 1 January 1958 |
| T2-NL-3 | Box 3 wealth above heffingvrij EUR 57,000 | Box 3 rate/return contested in courts (Hoge Raad Kerst-arrest) | Compute at current statutory rates; note litigation uncertainty |
| T2-NL-4 | Company car (auto van de zaak) | Bijtelling (benefit in kind) required; complex auto fiscaliteit | Flag — bijtelling % depends on CO2 emissions and first registration date |
| T2-NL-5 | International assignment or partial-year residency | 30% ruling may apply; non-resident rules | Flag — bilateral treaty and 30%-ruling analysis required |
| T2-NL-6 | Partner's income affects krediet allocation | Heffingskortingen can be transferred between fiscal partners in some cases | Flag for fiscal partner analysis |
| T2-NL-7 | OR-eligible investment (R&D / WBSO) | WBSO subsidy reduces payable wage tax; separate S&O administration required | Flag — WBSO is claimed separately, not via IB return |

---

## Section 7 — Excel Working Paper Template

```
NETHERLANDS INCOME TAX WORKING PAPER (ZZP / EENMANSZAAK)
Taxpayer: _______________  BSN: _______________  FY: 2025

SECTION A — REVENUE (ex-BTW)
                                        EUR
Gross revenue (all clients, ex-BTW)    ___________
Less: credit notes / returns           (___________)
Net revenue                            ___________

SECTION B — DEDUCTIBLE BUSINESS EXPENSES
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
Other business expenses                ___________
Payment processor fees                 ___________
TOTAL DEDUCTIBLE EXPENSES              ___________

SECTION C — PROFIT (WINST)
Net revenue − Total expenses           ___________

SECTION D — ENTREPRENEUR DEDUCTIONS (ONDERNEMERSAFTREK)
Zelfstandigenaftrek (if uren met)      ___________
Startersaftrek (if eligible yr 1–3)    ___________
KIA — kleinschaligheidsinvesteringsaftrek ________
Subtotal after deductions              ___________
MKB-winstvrijstelling (13.31%)         (___________)
BELASTBAAR INKOMEN BOX 1               ___________

SECTION E — BOX 1 TAX COMPUTATION
Tax at bracket rates (see table)       ___________
Less: Algemene heffingskorting         (___________)
Less: Arbeidskorting                   (___________)
Less: Other kortingen                  (___________)
BOX 1 NET TAX                          ___________

SECTION F — ADVANCE PAYMENTS
Voorlopige aanslag paid                (___________)
IB balance due / (refund)              ___________

SECTION G — BOX 3 (if applicable)
Assets on 1 January (incl. bank saldo) ___________
Less: heffingvrij vermogen EUR 57,000  (___________)
Grondslag Box 3                        ___________
Fictitious return (see rates by class) ___________
Box 3 tax @ 36%                        ___________

SECTION H — REVIEWER FLAGS
[ ] Urencriterium — hour log reviewed?
[ ] Startersaftrek — year 1/2/3 confirmed?
[ ] Single client > 70%? Schijnzelfstandigheid flag
[ ] BTW stripped from all revenue/expense amounts
[ ] KIA — qualifying assets > EUR 2,801?
[ ] Box 3 assets declared on 1 January balance
[ ] AOW age check (DOB before 1 January 1958?)
```

---

## Section 8 — Bank Statement Reading Guide

### ING Zakelijk
- Export: CSV via "Downloaden" in Mijn ING Zakelijk
- Columns: `Datum;Naam/Omschrijving;Rekening;Tegenrekening;Code;Af Bij;Bedrag (EUR);Mutatiesoort;Mededelingen`
- Amount format: comma decimal, no thousands separator (e.g., `3500,00`)
- `Af Bij`: `Af` = debit, `Bij` = credit
- Date format: DD-MM-YYYY

### Rabobank
- Export: CSV from Rabo Internetbankieren ("Downloaden")
- Columns: `IBAN/BBAN;Munt;BIC;Volgnr;Datum;Rentedatum;Bedrag;Saldo na trn;Tegenrekening IBAN/BBAN;Naam tegenpartij;Naam uiteindelijke partij;Naam initierende partij;BIC tegenpartij;Code;Batch ID;Transactiereferentie;Machtigingskenmerk;Incassant ID;Betalingskenmerk;Omschrijving;Reden retour;Oorspr bedrag;Oorspr munt;Koers`
- Amount: negative = debit, positive = credit

### ABN AMRO
- Export: CSV or MT940 from "Bankieren" portal
- CSV columns: `Transactiedatum;Valutacode;CreditDebet;Bedrag;Tegenrekening IBAN;Naam tegenpartij;Omschrijving`
- `CreditDebet`: `C` = credit, `D` = debit

### Bunq
- Export: CSV from app ("Accounts" > "Export")
- Columns: `date,amount,account,counterparty_name,counterparty_iban,description`
- Amount: positive = credit, negative = debit; period decimal

### Knab Business
- Export: CSV or Excel from online portal
- Standard Dutch bank format; comma decimal amounts

### SNS Bank
- Export: CSV from "Mijn SNS"
- Columns: `Boekdatum;Naam;Rekening;Tegenrekening;Code;Debet/Credit;Bedrag;Mededelingen;Saldo`

---

## Section 9 — Onboarding Fallback

**Missing hour log:**
> "To claim the zelfstandigenaftrek (EUR 2,470), Dutch tax law requires you to have worked at least 1,225 hours in your business during 2025 and to be able to demonstrate this. Do you maintain an urenstaat (hour log)? If not, we must flag the zelfstandigenaftrek as unsubstantiated. I recommend starting a log immediately for 2026."

**Revenue includes BTW:**
> "I notice some amounts may include BTW (VAT). For income tax (IB) purposes, only the ex-BTW amounts count as revenue. Please confirm which figures are ex-BTW. If you are BTW-plichtig, your BTW return is separate from your IB return."

**Single client situation:**
> "I see that more than 70% of your 2025 revenue came from a single client. The Belastingdienst is increasingly scrutinising this pattern as possible hidden employment (schijnzelfstandigheid). This may not affect your 2025 return, but I recommend consulting your accountant about diversifying clients or obtaining a valid modelovereenkomst to protect your zzp status."

**Box 3 assets:**
> "To complete your income tax return, I also need your financial position on 1 January 2025: total savings, investments, and any second property. If these exceed EUR 57,000 (EUR 114,000 with fiscal partner), Box 3 wealth tax applies on top of your Box 1 income tax."

---

## Section 10 — Reference Material

### Key Legislation
- **Wet inkomstenbelasting 2001 (Wet IB 2001)** — primary income tax law; Box 1/2/3 framework
- **Art. 3.76 Wet IB** — zelfstandigenaftrek
- **Art. 3.78 Wet IB** — startersaftrek
- **Art. 3.79a Wet IB** — MKB-winstvrijstelling
- **Art. 3.41 Wet IB** — kleinschaligheidsinvesteringsaftrek (KIA)

### Filing Deadlines 2025 (FY 2024)
| Deadline | Event |
|---|---|
| 1 May 2025 | Standard aangifte IB 2024 deadline |
| 1 September 2025 | Extended deadline (with accountant / DigiD aanvraag) |
| 1 July each year | Voorlopige aanslag voor 2025 can be requested/revised |

### Useful Rates Summary 2025
- Box 1 first bracket: 35.82% (up to EUR 38,441)
- Box 1 second bracket: 37.48% (EUR 38,442 – EUR 76,817)
- Box 1 top rate: 49.50%
- Zelfstandigenaftrek: EUR 2,470
- MKB-winstvrijstelling: 13.31%
- Box 3 tax rate: 36%
- Box 3 heffingvrij: EUR 57,000 (EUR 114,000 for fiscal partners)

### Useful References
- Belastingdienst: belastingdienst.nl
- Ondernemersplein: ondernemersplein.kvk.nl
- KIA table: belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/investeringen_aftrekken
