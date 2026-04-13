---
name: be-income-tax
description: >
  Use this skill whenever asked about Belgian income tax (Personenbelasting / Impot des personnes physiques) for self-employed individuals. Trigger on phrases like "personenbelasting", "IPP", "belastingaangifte", "belastingvrij minimum", "gemeentebelasting", "beroepskosten", "sociale bijdragen", "VAPZ", "PLCI", "Belgian income tax", "self-employed tax Belgium", "Tax-on-web", or any question about computing or filing income tax for a self-employed person in Belgium. This skill covers progressive brackets (25--50%), belastingvrij minimum, gemeentebelasting, beroepskosten (actual vs forfaitaire), sociale bijdragen deductibility, VAPZ/PLCI pension deduction, and Tax-on-web filing. ALWAYS read this skill before touching any Belgian income tax work.
version: 2.0
jurisdiction: BE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Belgium Income Tax (PB/IPP) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Belgium (Koninkrijk Belgie / Royaume de Belgique) |
| Tax | Personenbelasting (PB) / Impot des personnes physiques (IPP) + Gemeentebelasting |
| Currency | EUR only |
| Tax year | Calendar year (income year) / Assessment year = income year + 1 |
| Primary legislation | Wetboek van de inkomstenbelastingen 1992 (WIB 92) / CIR 92 |
| Supporting legislation | KB/WIB 92; Royal Decree No. 38 (social statute) |
| Tax authority | FOD Financien / SPF Finances |
| Filing portal | Tax-on-web (MyMinfin) |
| Filing deadline | 30 June (self-filing) / mid-October (with accountant) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by erkend boekhouder-fiscalist or bedrijfsrevisor |
| Validation date | Pending |
| Skill version | 2.0 |

### Progressive Tax Brackets (Income Year 2025 / AJ 2026)

| Taxable Income (EUR) | Marginal Rate |
|---|---|
| 0 -- 16,720 | 25% |
| 16,721 -- 29,510 | 40% |
| 29,511 -- 51,070 | 45% |
| Above 51,070 | 50% |

### Belastingvrij Minimum (Tax-Free Allowance)

| Category | EUR |
|---|---|
| Base | 10,910 |
| +1 dependant child | +1,850 |
| +2 dependant children | +4,760 |
| +3 dependant children | +10,660 |
| +4+ children | +6,180 per additional |
| Disabled dependant | +1,850 per person |

Converted to tax reduction at 25% rate: EUR 10,910 x 25% = EUR 2,727.50 base.

### Gemeentebelasting (Municipal Surcharge)

- Range: 0% to 9% of federal tax
- Average: ~7%
- **MUST know municipality to compute. STOP if unknown.**

### Key Deductions

| Item | Rule |
|---|---|
| Sociale bijdragen | Fully deductible as professional expense |
| Restaurant meals (business) | 69% deductible |
| Business gifts | 50% deductible |
| VAPZ/PLCI (gewoon) | Max ~EUR 3,965 (8.17% of reference income) |
| VAPZ/PLCI (sociaal) | Max ~EUR 4,562 (9.40% of reference income) |
| Forfaitaire beroepskosten (max) | ~EUR 5,750 |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown municipality | STOP -- cannot compute gemeentebelasting |
| Unknown expense method | Forfaitaire beroepskosten |
| Unknown business-use % | 0% deduction |
| Unknown VAPZ type | Gewoon VAPZ |
| Unknown vehicle CO2 | Minimum deductibility percentage |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, municipality of residence, marital/family status.

**Recommended** -- all invoices, sociale bijdragen statements from social fund, VAPZ/PLCI certificates, prior year aanslagbiljet.

**Ideal** -- complete accounting records, asset register, voorafbetalingen confirmations, employment income fiche 281.10.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement = hard stop. No municipality = hard stop.

### Refusal Catalogue

**R-BE-1 -- Companies (BV, NV, CV).** "This skill covers natural persons (personenbelasting) only. Vennootschapsbelasting is out of scope."

**R-BE-2 -- Non-resident.** "Non-resident taxation (BNI/INR) has different rules. Escalate."

**R-BE-3 -- International structures.** "Cross-border income and tax treaties require specialist analysis. Escalate."

**R-BE-4 -- Fiscale procedures / bezwaar.** "Objections and appeals require specialist advice. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| OVERSCHRIJVING [client], BETALING, HONORARIUM | Beroepsinkomsten | Business income | Net of BTW if BTW-registered |
| STRIPE PAYOUT, PAYPAL PAYOUT | Beroepsinkomsten | Business income | Platform payout |
| LOON, WEDDE, WERKGEVER | Bezoldiging | NOT self-employment | Employment income |
| HUUR ONTVANGEN, HUUROPBRENGST | Onroerend inkomen | NOT self-employment | Rental income |
| INTERESTEN, DIVIDEND | Roerend inkomen | NOT self-employment | Capital income (RV 30% withheld) |
| FOD FINANCIEN TERUGBETALING | EXCLUDE | Not income | Tax refund |

### 3.2 Expense Patterns (Debits) -- Fully Deductible

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| KANTOORHUUR, HUUR KANTOOR, OFFICE RENT | Huurkosten | Fully deductible | Dedicated premises |
| BEROEPSAANSPRAKELIJKHEID, BA VERZEKERING | Verzekering | Fully deductible | Professional insurance |
| BOEKHOUDER, ACCOUNTANT, FISCALIST | Erelonen | Fully deductible | |
| ADVOCAAT, NOTARIS (business) | Erelonen | Fully deductible | Business-related |
| KANTOORMATERIAAL, BUREELBENODIGDHEDEN | Kantoorkosten | Fully deductible | |
| RECLAME, MARKETING, GOOGLE ADS | Reclamekosten | Fully deductible | |
| OPLEIDING, VORMING, BIJSCHOLING | Opleidingskosten | Fully deductible | Current profession |
| LIDMAATSCHAP, BEROEPSVERENIGING | Bijdragen | Fully deductible | |
| BANKREKENINGKOSTEN, BANKKOSTEN | Financiele kosten | Fully deductible | Business account |
| STRIPE FEE, PAYPAL FEE | Transactiekosten | Fully deductible | |
| SOFTWARE, LICENTIE, ABONNEMENT | IT-kosten | Fully deductible | |

### 3.3 Expense Patterns -- Sociale Bijdragen

| Pattern | Treatment | Notes |
|---|---|---|
| ACERTA, LIANTIS, XERIUS, GROUP S, PARTENA | Fully deductible | Social insurance fund contributions |
| SOCIALE BIJDRAGEN, COTISATIONS SOCIALES | Fully deductible | Quarterly social contributions |
| VAPZ, PLCI, AANVULLEND PENSIOEN | Deductible (within limits) | See Section 6 for caps |

### 3.4 Expense Patterns -- Partially Deductible

| Pattern | Deductibility | Treatment | Notes |
|---|---|---|---|
| RESTAURANT, ETENTJE, ZAKENLUNCH | 69% | Partially deductible | Business purpose restaurant meals |
| GESCHENK, CADEAU, RELATIEGESCHENK | 50% | Partially deductible | Business gifts |
| BRANDSTOF, BENZINE, DIESEL, TOTAL, Q8 | CO2-based % | T2 | Vehicle fuel -- see CO2 rules |
| ONDERHOUD AUTO, GARAGE | CO2-based % | T2 | Vehicle maintenance |

### 3.5 Expense Patterns -- NOT Deductible

| Pattern | Treatment | Notes |
|---|---|---|
| PRIVE, BOODSCHAPPEN, SUPERMARKT, COLRUYT, DELHAIZE | NOT deductible | Personal living costs |
| BOETE, GELDBOETE | NOT deductible | Fines |
| PERSONENBELASTING, PB BETALING | NOT deductible | Income tax |
| PRIVEOPNAME | NOT deductible | Drawings |

### 3.6 Capital Items

| Pattern | Useful Life | Annual Rate | Notes |
|---|---|---|---|
| COMPUTER, LAPTOP, PC | 3 years | 33.3% | |
| PRINTER, SCANNER | 5 years | 20% | |
| KANTOORMEUBILAIR, BUREAU | 10 years | 10% | |
| AUTO, WAGEN (business) | 5 years | 20% | CO2 deductibility limits apply |
| GEBOUW (commercial) | 33 years | 3% | |

### 3.7 Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| EIGEN REKENING, INTERNE OVERSCHRIJVING | EXCLUDE | Own-account transfer |
| LENING, AFLOSSING | EXCLUDE | Loan principal |
| LENINGSINTERESTEN (business) | Deductible | Business loan interest |
| BTW BETALING | EXCLUDE from P&L | BTW liability payment |
| VOORAFBETALING BELASTING | Track separately | Credit against tax due |

### 3.8 Belgian Banks -- Statement Format Reference

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| BNP Paribas Fortis | CSV, PDF | Datum, Omschrijving, Bedrag | Most common; CODA format available |
| KBC | CSV, PDF | Boekingsdatum, Omschrijving, Bedrag | KBC Touch export |
| Belfius | CSV, PDF | Datum, Mededeling, Bedrag | |
| ING Belgium | CSV, PDF | Datum, Naam tegenpartij, Bedrag | |
| Argenta | CSV, PDF | Datum, Verrichting, Bedrag | |
| N26, Revolut | CSV | Date, Counterparty, Amount | Neobank format |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (BTW-registered)

**Input line:**
`15/03/2025 ; BNP Fortis Credit ; DESIGN STUDIO BVBA ; Factuur 2025-012 ; +3,025.00 ; EUR`

**Reasoning:**
Client payment. If BTW-registered (21%), EUR 3,025 includes BTW. Net = EUR 2,500 (beroepsinkomsten) + EUR 525 BTW.

**Classification:** Beroepsinkomsten = EUR 2,500.

### Example 2 -- Restaurant Meal (69% Deductible)

**Input line:**
`22/04/2025 ; KBC Visa ; RESTAURANT COMME CHEZ SOI ; Zakenlunch ; -95.00 ; EUR`

**Reasoning:**
Business restaurant meal. 69% deductible. EUR 95 x 69% = EUR 65.55 deductible. EUR 29.45 not deductible.

**Classification:** Beroepskosten = EUR 65.55.

### Example 3 -- Sociale Bijdragen

**Input line:**
`15/01/2025 ; Belfius DD ; ACERTA ; Sociale bijdragen Q4 2024 ; -1,850.00 ; EUR`

**Reasoning:**
Social contributions. Fully deductible as beroepskosten.

**Classification:** Beroepskosten -- fully deductible.

### Example 4 -- VAPZ Contribution

**Input line:**
`30/06/2025 ; KBC DD ; ACERTA VAPZ ; Gewoon VAPZ 2025 ; -3,965.00 ; EUR`

**Reasoning:**
Gewoon VAPZ at maximum (EUR 3,965 for 2025). Deductible as social contribution.

**Classification:** Deductible within VAPZ cap.

### Example 5 -- Vehicle Fuel (CO2-dependent)

**Input line:**
`10/05/2025 ; BNP Fortis Card ; TOTAL ENERGIES ; Diesel ; -75.00 ; EUR`

**Reasoning:**
Vehicle fuel. Fuel is max 75% deductible regardless of CO2. Other vehicle costs follow the CO2-based formula. Business % required.

**Classification:** T2 -- 75% cap on fuel, business % required, CO2 deductibility for other costs.

### Example 6 -- Personal Groceries (Exclude)

**Input line:**
`08/03/2025 ; Belfius Card ; COLRUYT ; Boodschappen ; -85.00 ; EUR`

**Reasoning:**
Personal groceries. Not business-related.

**Classification:** NOT deductible. Exclude.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Beroepsinkomsten

All business income is beroepsinkomsten. For BTW-registered, report net of BTW.

### 5.2 Beroepskosten

Two methods (choose one):
- **Werkelijke (actual):** All documented business expenses meeting the test
- **Forfaitaire (flat-rate):** Graduated scale, max ~EUR 5,750

Cannot combine both. Sociale bijdragen deductible under either method.

### 5.3 Forfaitaire Beroepskosten Scale

| Income Bracket (EUR) | Rate |
|---|---|
| 0 -- 19,620 | 30% |
| 19,621 -- 38,900 | 11% |
| 38,901 -- 64,770 | 3% |
| Above 64,770 | 0% |

### 5.4 Non-Deductible Expenses

| Expense | Reason |
|---|---|
| Personal living expenses | Not business-related |
| Fines (boetes) | Public policy |
| Income tax (personenbelasting) | Tax on income |
| Capital expenditure | Through afschrijvingen |

### 5.5 Partially Deductible

| Item | % Deductible |
|---|---|
| Restaurant meals (business) | 69% |
| Business gifts | 50% |
| Vehicle costs (fuel) | Max 75% |
| Vehicle costs (other) | CO2-based formula |

### 5.6 Voorafbetalingen (Advance Payments)

| Quarter | Deadline | Benefit % |
|---|---|---|
| VA1 | 10 April | 12% |
| VA2 | 10 July | 10% |
| VA3 | 10 October | 8% |
| VA4 | 20 December | 6% |

Vermeerdering (~9% of tax) for insufficient advance payments. Making VA earns bonification to offset.

### 5.7 Filing Deadlines

| Item | Deadline |
|---|---|
| Tax-on-web (self) | 30 June |
| With accountant | Mid-October |
| Paper filing | End of June |

### 5.8 Penalties

| Offence | Penalty |
|---|---|
| Late filing (first) | EUR 50/month |
| Late payment interest | 4% per year (2025) |
| Non-filing / serious | EUR 50-1,250 + tax increase 10%-200% |

### 5.9 Afschrijvingen (Depreciation)

| Asset | Life | Rate |
|---|---|---|
| Computer | 3 years | 33.3% |
| Software | 3 years | 33.3% |
| Furniture | 10 years | 10% |
| Vehicles | 5 years | 20% |
| Buildings | 33 years | 3% |

Straight-line or declining balance (degressief) permitted.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Werkelijke vs Forfaitaire Comparison

Compare actual expenses (including sociale bijdragen) against forfaitaire scale. Flag for reviewer.

### 6.2 Motor Vehicle CO2 Deductibility

From 2025, formula: 120% - (0.5% x coefficient x CO2 g/km). High-emission vehicles significantly limited. Flag for reviewer to compute using exact CO2 and fuel type.

### 6.3 VAPZ/PLCI Limits

- Gewoon: 8.17% of reference income (max ~EUR 3,965)
- Sociaal: 9.40% of reference income (max ~EUR 4,562)
- Reference income = net professional income from 3 years prior
- Flag for reviewer to confirm limit

### 6.4 Home Office

Dedicated workspace required. Proportional by floor area. Dual-use does not qualify.

### 6.5 Phone / Internet Mixed Use

Business portion only. Default 0%.

### 6.6 Sociale Bijdragen in First 3 Years

Provisional contributions on minimum basis. Regularisation later. Adjustment in year of payment/receipt.

---

## Section 7 -- Excel Working Paper Template

```
BELGIUM INCOME TAX -- PB/IPP WORKING PAPER
Tax Year: 2025 (AJ 2026)
Client: ___________________________
Municipality: ___________ (Rate: ___%)
Status: Single / Married / Cohabitant
Dependants: ___

A. BEROEPSINKOMSTEN (net of BTW if registered)    ___________

B. BEROEPSKOSTEN
  Method: [ ] Werkelijk  [ ] Forfaitair
  B1. Sociale bijdragen                            ___________
  B2. Kantoorkosten                                ___________
  B3. Verzekeringen                                ___________
  B4. Erelonen (boekhouder, advocaat)              ___________
  B5. IT / software                                ___________
  B6. Reclame / marketing                          ___________
  B7. Reiskosten                                   ___________
  B8. Restaurantkosten (69%)                       ___________
  B9. Autokosten (CO2-based %)                     ___________
  B10. Afschrijvingen                              ___________
  B11. Overige beroepskosten                       ___________
  B12. TOTAL                                       ___________

C. NETTO BEROEPSINKOMEN (A - B12)                  ___________

D. BELASTING
  D1. Federale belasting (brackets)                ___________
  D2. Less: Belastingvrij minimum reductie         ___________
  D3. Less: Other reductions                       ___________
  D4. Federale belasting verschuldigd              ___________
  D5. Gemeentebelasting (D4 x rate)               ___________
  D6. TOTAL                                        ___________
  D7. Less: Voorafbetalingen                       ___________
  D8. SALDO                                        ___________

REVIEWER FLAGS:
  [ ] Municipality and rate confirmed?
  [ ] Expense method confirmed (actual/forfait)?
  [ ] Vehicle CO2 deductibility computed?
  [ ] Restaurant meals at 69%?
  [ ] VAPZ within limits?
  [ ] Vermeerdering for missing VA?
```

---

## Section 8 -- Bank Statement Reading Guide

### Belgian Bank Statement Formats

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| BNP Paribas Fortis | CSV, PDF, CODA | Datum, Omschrijving/Mededeling, Bedrag | CODA format = structured |
| KBC | CSV, PDF | Boekingsdatum, Omschrijving, Bedrag | KBC Touch/Business |
| Belfius | CSV, PDF | Datum, Mededeling, Bedrag | |
| ING Belgium | CSV, PDF | Datum, Naam tegenpartij, Mededeling, Bedrag | |
| Argenta | CSV, PDF | Datum, Verrichting, Bedrag | |

### Key Belgian Banking Terms

| Term | English | Hint |
|---|---|---|
| Overschrijving | Transfer | Check direction |
| Domiciliering | Direct debit | Regular expense |
| Storting | Deposit | Potential income |
| Betaalkaart / Visa | Card payment | Expense |
| Bancontact | Debit card payment | Expense |
| Rekeningkosten | Account charges | Deductible |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- BELGIUM INCOME TAX
1. Municipality of residence? (Required for gemeentebelasting)
2. Family status: single, married/cohabitant, dependants?
3. Expense method: actual (werkelijk) or flat-rate (forfaitair)?
4. Sociale bijdragen: total paid in the year? Which fund?
5. VAPZ/PLCI contributions? Gewoon or sociaal?
6. Vehicle: CO2 emissions? Fuel type? Business %?
7. Home office: dedicated room? Floor area %?
8. Phone/internet: business %?
9. Other income (employment, rental, investment)?
10. Voorafbetalingen made? Amounts and dates?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Tax brackets | WIB 92, Art. 130+ |
| Belastingvrij minimum | WIB 92, Art. 131-145 |
| Beroepskosten | WIB 92, Art. 49-66 |
| Forfaitaire kosten | WIB 92, Art. 51 |
| Gemeentebelasting | WIB 92, Art. 466-470 |
| Sociale bijdragen | Royal Decree No. 38 |
| VAPZ | Programmawet 24 Dec 2002 |
| Afschrijvingen | WIB 92, Art. 61-65 |
| Voorafbetalingen | WIB 92, Art. 157-168 |
| Restaurant meals | 69% rule |
| Record keeping | 7 years |

### Test Suite

**Test 1 -- Single, Antwerp (8.4%), mid-range.**
Input: Turnover EUR 50,000, actual expenses EUR 10,000 (incl. sociale bijdragen EUR 5,500).
Expected: Net EUR 40,000. Federal tax ~EUR 14,016. Less belastingvrij EUR 2,728 = EUR 11,289. Gemeente EUR 948.

**Test 2 -- Forfaitaire comparison.**
Input: Turnover EUR 30,000, actual EUR 2,000.
Expected: Forfaitaire ~EUR 7,028. Forfaitaire is better.

**Test 3 -- Restaurant meals.**
Input: EUR 3,000 restaurant at 100%.
Expected: 69% = EUR 2,070 deductible. Remove EUR 930.

**Test 4 -- VAPZ cap.**
Input: EUR 5,000 gewoon VAPZ. Max EUR 3,965.
Expected: EUR 1,035 excess not deductible.

**Test 5 -- Gemeentebelasting.**
Input: Federal tax EUR 8,000, rate 7%.
Expected: Gemeente EUR 560. Total EUR 8,560.

**Test 6 -- Vermeerdering.**
Input: Tax EUR 10,000, no VA.
Expected: Vermeerdering ~EUR 900. Total EUR 10,900.

---

## PROHIBITIONS

- NEVER compute gemeentebelasting without municipality and actual rate
- NEVER allow both werkelijke and forfaitaire beroepskosten
- NEVER deduct restaurant meals at 100% -- maximum 69%
- NEVER allow income tax as a deduction
- NEVER allow fines as deductions
- NEVER allow VAPZ above maximum
- NEVER ignore vermeerdering for missing advance payments
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an erkend boekhouder-fiscalist or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
