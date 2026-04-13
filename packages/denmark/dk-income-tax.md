---
name: dk-income-tax
description: >
  Use this skill whenever asked about Danish income tax for self-employed individuals (selvstaendig erhvervsdrivende). Trigger on phrases like "Danish tax", "AM-bidrag", "bundskat", "topskat", "kommuneskat", "virksomhedsordningen", "kapitalafkastordningen", "personfradrag", "Arsopgorelse", "Oplysningsskema", "self-employed tax Denmark", or any question about filing or computing income tax for a Danish self-employed client. Covers AM-bidrag (8%), bundskat, topskat, kommuneskat, kirkeskat, virksomhedsordningen, kapitalafkastordningen, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Danish income tax work.
version: 2.0
jurisdiction: DK
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Denmark Income Tax -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Denmark (Kongeriget Danmark) |
| Tax | AM-bidrag + Bundskat + Topskat + Kommuneskat + Kirkeskat (if applicable) |
| Currency | DKK only |
| Tax year | Calendar year |
| Primary legislation | Personskatteloven (PSL); Kildeskatteloven (KSL); Virksomhedsskatteloven (VSL) |
| Supporting legislation | Ligningsloven (LL); Afskrivningsloven (AL); Statsskatteloven (SL) |
| Tax authority | Skattestyrelsen (SKAT) |
| Filing portal | skat.dk / TastSelv |
| Filing deadline | 1 July (self-employed, extended from 1 May) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Danish statsautoriseret or registreret revisor |
| Validation date | Pending |
| Skill version | 2.0 |

### Tax Rates (2025)

| Tax | Rate | Applied To |
|---|---|---|
| AM-bidrag | 8% | Gross personal income (FIRST, before all other taxes) |
| Bundskat | 12.01% | Personal income after AM-bidrag, above personfradrag |
| Topskat | 15% | Personal income after AM-bidrag above DKK 611,800 |
| Kommuneskat | Avg 25.1% (22-27%) | Taxable income (varies by municipality) |
| Kirkeskat | Avg 0.87% (0.39-1.20%) | Only for Folkekirken members |

### Key Thresholds

| Item | DKK (2025) |
|---|---|
| Personfradrag (personal allowance) | 51,600 |
| Topskat threshold (after AM-bidrag) | 611,800 |
| Skatteloft (tax ceiling) | ~52.07% combined marginal rate |
| Straksafskrivning (immediate write-off) | 15,400 |

### VSO vs KAO vs Default

| Scheme | Key Feature | Best For |
|---|---|---|
| Virksomhedsordningen (VSO) | 22% interim tax on retained profits | Significant interest expenses; variable income |
| Kapitalafkastordningen (KAO) | 2% yield on net assets reclassified as capital income | Significant assets, limited interest |
| No scheme (default) | All profit = personal income | Simple; no income splitting |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown municipality | National average 25.1% kommuneskat (flag as estimated) |
| Unknown Folkekirken membership | No kirkeskat (0%) |
| Unknown VSO/KAO election | No scheme (default PSL) |
| Unknown business-use % | 0% deduction |
| Unknown expense category | Not deductible |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, municipality of residence, business form (selvstaendig erhvervsdrivende).

**Recommended** -- all invoices, prior year arsopgorelse, tax scheme election (VSO/KAO/none), Folkekirken membership status.

**Ideal** -- complete regnskab (accounts), asset register, B-skat payment records, VSO indskudskonto and opsparingskonto balances.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement = hard stop.

### Refusal Catalogue

**R-DK-1 -- Companies (ApS, A/S, IVS).** "This skill covers self-employed individuals only. Selskabsskat is out of scope."

**R-DK-2 -- International income / dual residency.** "Cross-border income requires specialist analysis. Escalate."

**R-DK-3 -- Complex VSO exits.** "Exiting virksomhedsordningen with significant opsparet overskud requires specialist computation. Escalate."

**R-DK-4 -- Transfer pricing.** "Transfer pricing is out of scope."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| OVERFORSEL [client], BETALING, HONORAR | Omsaetning (revenue) | Business income | If momsregistreret, extract net (excl. 25% moms) |
| STRIPE PAYOUT, PAYPAL PAYOUT | Revenue | Business income | Platform payout |
| LON, GAGE, ARBEJDSGIVER | Lonindkomst | NOT self-employment | Employment income |
| LEJEINDTAEGT, HUSLEJE | Lejeindkomst | NOT self-employment | Rental income |
| RENTER, UDBYTTE | Kapitalindkomst | NOT self-employment | Capital income |
| SKAT TILBAGEBETALING | EXCLUDE | Not income | Tax refund |
| UPWORK, FIVERR, TOPTAL | Revenue | Business income | Freelance platform |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (Driftsomkostninger)

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| KONTORLEJE, HUSLEJE KONTOR | Lokaleomkostninger | Fully deductible | Dedicated premises |
| ERHVERVSFORSIKRING, ANSVARSFORSIKRING | Forsikring | Fully deductible | Professional insurance |
| REVISOR, BOGHOLDER, REGNSKAB | Revisorudgifter | Fully deductible | |
| ADVOKAT (business) | Advokatomkostninger | Fully deductible | Business-related |
| KONTORARTIKLER, KONTORMATERIALER | Kontorhold | Fully deductible | |
| REKLAME, MARKETING, GOOGLE ADS, META ADS | Reklameudgifter | Fully deductible | |
| UDDANNELSE, KURSUS, EFTERUDDANNELSE | Uddannelsesudgifter | Fully deductible | Related to current business |
| BRANCHEFORENING, FAGFORENING | Kontingenter | Fully deductible | |
| BANKGEBYR, KONTOGEBYR | Bankudgifter | Fully deductible | Business account |
| STRIPE FEE, PAYPAL FEE | Transaktionsgebyr | Fully deductible | |
| SOFTWARE, ABONNEMENT, LICENS | IT-udgifter | Fully deductible | |
| PORTO, POSTNORD | Porto | Fully deductible | Business correspondence |

### 3.3 Expense Patterns -- Travel

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| FLYREJSE, SAS, NORWEGIAN, RYANAIR | Rejseudgifter | Fully deductible | Business travel |
| HOTEL, BOOKING.COM | Rejseudgifter | Fully deductible | Business travel |
| DSB, REJSEKORT | Rejseudgifter | Fully deductible | Business travel |
| TAXA, DANTAXI, UBER, BOLT | Rejseudgifter | Fully deductible | Business purpose |
| BENZIN, DIESEL, SHELL, OK, Q8 | Biludgifter | T2 -- business km only | Standard rate or actual |

### 3.4 Expense Patterns -- Partially Deductible

| Pattern | Deductibility | Treatment | Notes |
|---|---|---|---|
| REPRESENTATION, KUNDEPLEJE, RESTAURANTBESOG | 25% | Partially deductible | Representation expenses |
| GAVER TIL FORRETNINGSFORBINDELSER | Limited | Per-person limit applies | Business gifts |

### 3.5 Expense Patterns -- NOT Deductible

| Pattern | Treatment | Notes |
|---|---|---|
| PRIVAT, DAGLIGVARER, SUPERMARKED, NETTO, FOTEX | NOT deductible | Personal living costs |
| BODE, STRAF | NOT deductible | Fines |
| SKAT, INDKOMSTSKAT, B-SKAT BETALING | NOT deductible | Income tax |
| PRIVATHVAEVNING | NOT deductible | Drawings |

### 3.6 Capital Items (Driftsmidler Pool)

| Pattern | Method | Rate | Notes |
|---|---|---|---|
| COMPUTER, LAPTOP, PC | Declining balance pool | Up to 25% | If over DKK 15,400 |
| MASKINE, UDSTYR, INVENTAR | Declining balance pool | Up to 25% | Pool depreciation |
| BIL, PERSONBIL (business) | Declining balance pool | Up to 25% | Business vehicle |
| SOFTWARE (purchased, over DKK 15,400) | Declining balance pool | Up to 25% | |
| Small items (under DKK 15,400) | Straksafskrivning | 100% immediate | Full deduction |
| BYGNING (business) | Straight-line | 4% | Business buildings |
| GOODWILL | Straight-line | 1/7 (~14.3%) | |

### 3.7 Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| INTERN OVERFORSEL, EGNE KONTI | EXCLUDE | Own-account transfer |
| LAN, AFDRAG | EXCLUDE | Loan principal |
| RENTER LAN (business) | Deductible | Business loan interest (important for VSO) |
| MOMS BETALING | EXCLUDE from P&L | Moms liability |
| B-SKAT BETALING | Track separately | Preliminary tax credit |

### 3.8 Danish Banks -- Statement Format Reference

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| Danske Bank | CSV, PDF | Dato, Tekst, Belob, Saldo | Most common; Netbank export |
| Nordea DK | CSV, PDF | Bogforingsdato, Tekst, Belob | |
| Jyske Bank | CSV, PDF | Dato, Tekst, Belob | |
| Sydbank | CSV, PDF | Dato, Tekst, Belob | |
| Spar Nord | CSV, PDF | Dato, Posteringstekst, Belob | |
| Lunar, Revolut | CSV | Date, Counterparty, Amount | Neobank format |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (Momsregistreret)

**Input line:**
`15/03/2025 ; Danske Bank Indgang ; KREATIV BUREAU APS ; Faktura 2025-003 ; +62,500.00 ; DKK`

**Reasoning:**
Client payment. If momsregistreret (25% moms), DKK 62,500 includes moms. Net = DKK 50,000 (revenue) + DKK 12,500 moms (excluded).

**Classification:** Revenue = DKK 50,000. Moms DKK 12,500 excluded.

### Example 2 -- Representation (25% Deductible)

**Input line:**
`22/04/2025 ; Nordea Visa ; RESTAURANT NOMA ; Kundepleje ; -4,000.00 ; DKK`

**Reasoning:**
Representation expenses. Only 25% deductible for tax. DKK 4,000 x 25% = DKK 1,000 deductible. DKK 3,000 not deductible.

**Classification:** Driftsomkostning = DKK 1,000. DKK 3,000 add back.

### Example 3 -- AM-bidrag Computation

**Input line:**
Gross business income: DKK 600,000.

**Reasoning:**
AM-bidrag = DKK 600,000 x 8% = DKK 48,000. Paid FIRST, before all other taxes. Remaining DKK 552,000 is the base for bundskat, topskat, kommuneskat.

**Classification:** AM-bidrag DKK 48,000. Taxable base DKK 552,000.

### Example 4 -- Equipment Over Straksafskrivning Limit

**Input line:**
`03/06/2025 ; Danske Bank Kort ; DUSTIN A/S ; SERVER ; -25,000.00 ; DKK`

**Reasoning:**
Server DKK 25,000. Over DKK 15,400 straksafskrivning limit. Must enter driftsmiddel pool. Year 1 depreciation: DKK 25,000 x 25% = DKK 6,250.

**Classification:** Add to driftsmiddel pool. Depreciation DKK 6,250. NOT direct expense.

### Example 5 -- B-skat Payment (Not Expense)

**Input line:**
`10/01/2025 ; Danske Bank ; SKAT ; B-SKAT JANUAR ; -8,000.00 ; DKK`

**Reasoning:**
Preliminary tax payment. Not a business expense. Track as credit against final tax liability.

**Classification:** EXCLUDE from expenses. Track for tax settlement.

### Example 6 -- Moms in Revenue (Exclude)

**Input line:**
Total receipts DKK 750,000 including 25% moms.

**Reasoning:**
Net revenue = DKK 600,000. Moms DKK 150,000 is liability to SKAT, not income.

**Classification:** Revenue = DKK 600,000.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 AM-bidrag

8% on gross personal income. Calculated FIRST, before all other deductions and taxes. Reduces base for bundskat, topskat, kommuneskat.

### 5.2 Bundskat and Topskat

- Bundskat: 12.01% on personal income (after AM-bidrag) above personfradrag
- Topskat: 15% on personal income (after AM-bidrag) above DKK 611,800
- Skatteloft: combined marginal rate capped at ~52.07%

### 5.3 Kommuneskat and Kirkeskat

- Kommuneskat: varies by municipality (22-27%)
- Kirkeskat: only for Folkekirken members (0.39-1.20%)

### 5.4 Personfradrag

DKK 51,600. Provides tax value = personfradrag x (bundskat + kommuneskat + kirkeskat rates). Applied as credit.

### 5.5 Driftsomkostninger (Business Expenses)

Deductible if incurred to acquire, secure, or maintain income (SL ss 6). Mixed-use must be apportioned.

### 5.6 Depreciation (Afskrivninger)

- Driftsmidler: declining balance pool, up to 25%/year
- Buildings: straight-line 4%/year
- Goodwill: straight-line 1/7/year
- Under DKK 15,400: straksafskrivning (immediate)
- Under 3-year life: immediate regardless of cost

### 5.7 Non-Deductible

| Expense | Reason |
|---|---|
| Private living expenses | SL ss 6 |
| Fines | Public policy |
| Income tax | Tax on income |
| Capital items (above DKK 15,400) | Through depreciation |
| Representation (75%) | Only 25% deductible |

### 5.8 B-skat (Preliminary Tax)

10 monthly instalments (Jan-May, Aug-Dec). Self-assessed expected income. Adjustable via TastSelv. Underpayment above DKK 22,900 attracts interest.

### 5.9 Filing Deadlines

| Item | Deadline |
|---|---|
| Oplysningsskema (self-employed) | 1 July |
| Extension (via revisor) | Typically 1 September |
| B-skat instalments | Monthly (10 payments) |

### 5.10 Penalties

| Offence | Penalty |
|---|---|
| Late filing | DKK 200/day (max ~DKK 5,000) |
| Negligent incorrect return | Up to 20% of understated amount |
| Gross negligence / fraud | Up to 100% + prosecution |

### 5.11 Moms Interaction

| Scenario | Income Tax Treatment |
|---|---|
| Moms collected (momsregistreret) | NOT income -- exclude from revenue |
| Input moms recovered | NOT expense -- exclude |
| Non-deductible moms | IS expense -- adds to cost |
| Not registered (under DKK 50,000) | No moms; gross = net |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 VSO vs KAO vs Default Election

Must model all scenarios. VSO advantageous when significant business interest expenses or variable income. KAO when significant assets. Flag for reviewer.

### 6.2 VSO -- Opsparet Overskud

Retained profits taxed at 22% interim. Withdrawals taxed as personal income (22% credited). Complete separation of business/private required.

### 6.3 Home Office

- Dedicated room, exclusively business: proportional actual costs
- Standard deduction: DKK 2,100/year (2025) as alternative
- Room must be unsuitable for private use
- Flag for reviewer

### 6.4 Vehicle Business Use

- Standard rate: DKK 3.79/km (first 20,000 km); DKK 2.23/km thereafter
- Or actual costs with logbook
- Flag for reviewer

### 6.5 Phone / Internet

Business portion only. Default 0%.

### 6.6 Personfradrag Transfer (Married)

Unused personfradrag transferable between spouses for bundskat only (not topskat). Flag for reviewer.

---

## Section 7 -- Excel Working Paper Template

```
DENMARK INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Municipality: ___________ (Kommuneskat: ___%)
Folkekirken: Yes / No (Kirkeskat: ___%)
Tax Scheme: VSO / KAO / None

A. BUSINESS INCOME
  A1. Omsætning (net of moms)                     ___________
  A2. Øvrige indtægter                             ___________
  A3. Total                                        ___________

B. DRIFTSOMKOSTNINGER
  B1. Lokaleomkostninger                           ___________
  B2. Forsikring                                   ___________
  B3. Revisor / bogholder                          ___________
  B4. IT / software                                ___________
  B5. Reklame / marketing                          ___________
  B6. Rejseudgifter                                ___________
  B7. Biludgifter (business %)                     ___________
  B8. Repræsentation (25%)                         ___________
  B9. Afskrivninger                                ___________
  B10. Bankudgifter                                ___________
  B11. Øvrige driftsomkostninger                   ___________
  B12. Total                                       ___________

C. RESULTAT (A3 - B12)                             ___________

D. TAX COMPUTATION
  D1. AM-bidrag (8% x gross)                       ___________
  D2. Personal income after AM                     ___________
  D3. Bundskat (12.01%)                            ___________
  D4. Topskat (15% on excess > DKK 611,800)        ___________
  D5. Kommuneskat                                  ___________
  D6. Kirkeskat (if applicable)                    ___________
  D7. Personfradrag credit                         ___________
  D8. Total tax                                    ___________
  D9. Less: B-skat paid                            ___________
  D10. Balance due / refund                        ___________

REVIEWER FLAGS:
  [ ] Municipality confirmed?
  [ ] Folkekirken membership confirmed?
  [ ] Tax scheme (VSO/KAO/none) confirmed?
  [ ] Vehicle method confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Representation at 25%?
  [ ] All items over DKK 15,400 in depreciation pool?
```

---

## Section 8 -- Bank Statement Reading Guide

### Danish Bank Statement Formats

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| Danske Bank | CSV, PDF | Dato, Tekst, Beløb, Saldo | Netbank CSV export |
| Nordea DK | CSV, PDF | Bogføringsdato, Tekst, Beløb | |
| Jyske Bank | CSV, PDF | Dato, Tekst, Beløb | |
| Sydbank | CSV, PDF | Dato, Tekst, Beløb | |
| Spar Nord | CSV, PDF | Dato, Posteringstekst, Beløb | |
| Lunar | CSV | Date, Counterparty, Amount | Neobank |

### Key Danish Banking Terms

| Term | English | Hint |
|---|---|---|
| Indbetaling | Deposit/credit | Potential income |
| Udbetaling | Withdrawal/debit | Potential expense |
| Overførsel | Transfer | Check direction |
| Betalingsservice (BS) | Direct debit | Regular expense |
| Dankort | Debit card | Expense |
| Hævning | Withdrawal | Cash -- ask purpose |
| Gebyr | Fee/charge | Bank charge |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- DENMARK INCOME TAX
1. Business form: selvstændig erhvervsdrivende?
2. Tax scheme: Virksomhedsordningen, Kapitalafkastordningen, or none?
3. Municipality of residence?
4. Member of Folkekirken?
5. Home office: dedicated room or shared?
6. Vehicle: standard km rate or actual costs?
7. Phone/internet: business use %?
8. Prior year årsopgørelse available?
9. B-skat paid in the year? Monthly amounts?
10. Other income (employment, capital, share)?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Personal income tax | Personskatteloven (PSL) |
| AM-bidrag | Arbejdsmarkedsbidragsloven |
| VSO | Virksomhedsskatteloven (VSL) |
| KAO | Kapitalafkastordningen |
| Deductibility | Statsskatteloven ss 6; Ligningsloven |
| Depreciation | Afskrivningsloven (AL) |
| Filing | Skattekontrolloven |
| B-skat | Kildeskatteloven (KSL) |
| Bookkeeping | Bogføringsloven (5 years) |

### Test Suite

**Test 1 -- Mid-range, Copenhagen.**
Input: Copenhagen (kommuneskat 23.8%), not Folkekirken, gross DKK 600,000, expenses DKK 150,000, no VSO.
Expected: AM-bidrag DKK 48,000. Net DKK 402,000. Below topskat. Total ~DKK 173,479.

**Test 2 -- High income, topskat.**
Input: Aarhus (24.6%), Folkekirken (0.71%), gross DKK 1,000,000, expenses DKK 200,000.
Expected: AM DKK 80,000. Topskat on DKK 920,000 - DKK 611,800 = DKK 308,200 x 15%.

**Test 3 -- VSO retained profit.**
Input: Net DKK 500,000, retain DKK 300,000 in VSO.
Expected: DKK 300,000 x 22% = DKK 66,000 interim. Rest at personal rates.

**Test 4 -- Equipment over limit.**
Input: DKK 20,000 computer.
Expected: Pool depreciation 25% = DKK 5,000. NOT direct expense.

**Test 5 -- Representation overclaimed.**
Input: DKK 8,000 at 100%.
Expected: 25% = DKK 2,000 deductible. DKK 6,000 add back.

**Test 6 -- Moms in revenue.**
Input: DKK 750,000 gross including 25% moms.
Expected: Revenue DKK 600,000.

---

## PROHIBITIONS

- NEVER compute AM-bidrag on net income -- always 8% on GROSS
- NEVER apply topskat below DKK 611,800
- NEVER charge kirkeskat without Folkekirken confirmation
- NEVER include moms in taxable revenue
- NEVER allow capital items over DKK 15,400 as direct expense
- NEVER advise on VSO/KAO without modelling scenarios -- flag for reviewer
- NEVER allow 100% representation deduction -- maximum 25%
- NEVER treat VSO opsparet overskud withdrawals as tax-free
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a statsautoriseret revisor, registreret revisor, or equivalent licensed practitioner in Denmark) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
