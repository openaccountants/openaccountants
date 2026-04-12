---
name: pl-income-tax
description: Use this skill whenever asked about Polish income tax (PIT) for self-employed individuals (działalność gospodarcza / JDG). Trigger on phrases like "Polish tax", "PIT-36", "PIT-36L", "skala podatkowa", "ryczałt", "IP Box", "kwota wolna", "ZUS", "składki", "działalność gospodarcza", "self-employed tax Poland", or any question about filing or computing income tax for a Polish self-employed client. Covers skala podatkowa (12%/32%), flat tax (19%), ryczałt, IP Box (5%), kwota wolna, ZUS contributions, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Polish income tax work.
version: 2.0
---

# Poland Income Tax (PIT) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Poland (Rzeczpospolita Polska) |
| Tax type | Personal income tax (podatek dochodowy od osob fizycznych -- PIT) |
| Primary legislation | PIT Act (26 July 1991); Ryczałt Act (20 November 1998) |
| Supporting legislation | Social Insurance Act; Health Insurance Act; Tax Ordinance (Ordynacja podatkowa) |
| Tax authority | Krajowa Administracja Skarbowa (KAS -- National Revenue Administration) |
| Filing portal | e-Urzad Skarbowy (e-US) / podatki.gov.pl |
| Currency | PLN only |
| Skala podatkowa | 12% up to PLN 120,000; 32% above; kwota wolna PLN 30,000 |
| Podatek liniowy (flat tax) | 19% flat; no kwota wolna; no joint filing |
| Ryczałt rates | 2%--17% depending on activity (PKD code) |
| IP Box | 5% on qualifying IP income |
| Filing deadline | 30 April of the following year (all PIT forms) |
| Monthly advance payments | 20th of the following month |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Polish doradca podatkowy or biegły rewident sign-off |
| Validation date | Pending |

**Taxation form summary:**

| Form | Return | Kwota wolna | Joint filing | Expense deductions |
|---|---|---|---|---|
| Skala podatkowa | PIT-36 | Yes (PLN 30,000) | Yes | Yes |
| Podatek liniowy | PIT-36L | No | No | Yes |
| Ryczałt | PIT-28 | No | No | No (revenue-based) |
| IP Box | PIT-36/36L + PIT/IP | Per base form | Per base form | Yes (nexus ratio) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown taxation form | STOP -- must determine before computing |
| Unknown expense category | Not deductible |
| Unknown business-use proportion (car, phone) | 0% business use (20% if car not in asset register) |
| Unknown PKD code for ryczałt | STOP -- rate depends on PKD |
| Unknown VAT status | Assume non-deductible VAT adds to cost |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | PLN 20,000 |
| HIGH tax-delta on a single conservative default | PLN 2,000 |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net tax position | PLN 50,000 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year in CSV, PDF, or pasted text. Must cover full year. Acceptable from any Polish bank: PKO BP, mBank, ING Bank Śląski, Santander Polska, Bank Pekao, Alior Bank, or fintech (Revolut, Wise).

**Recommended** -- sales invoices (faktury), purchase invoices, chosen taxation form confirmation, PKD code(s), ZUS contribution statements (ZUS DRA).

**Ideal** -- complete KPiR (tax ledger) or ewidencja przychodów (for ryczałt), środki trwałe register (asset register), prior year PIT return.

**Refusal policy if minimum is missing -- SOFT WARN.** No bank statement = hard stop. Bank statement only = proceed with warnings.

### Refusal catalogue

**R-PL-1 -- Spółka z o.o. (sp. z o.o.) or spółka akcyjna.** *Trigger:* client operates through a limited company. *Message:* "This skill covers JDG (sole proprietorship) only. Sp. z o.o. files CIT-8 under corporate income tax at 9%/19%. Please use a separate skill."

**R-PL-2 -- International income / CFC rules.** *Trigger:* client has controlled foreign company or significant foreign income. *Message:* "International income and CFC rules are outside scope. Consult a doradca podatkowy."

**R-PL-3 -- Transfer pricing.** *Trigger:* related-party transactions. *Message:* "Transfer pricing is outside scope."

**R-PL-4 -- Taxation form unknown.** *Trigger:* client has not confirmed skala/liniowy/ryczałt. *Message:* "I cannot compute tax without knowing your chosen taxation form. Please confirm: skala podatkowa, podatek liniowy, or ryczałt."

---

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 Polish banks (fees and interest)

| Pattern | Treatment | Notes |
|---|---|---|
| PKO BP, PKO BANK POLSKI | Bank charges: deductible expense (KPiR) | Monthly service fees |
| MBANK, MBANK S.A. | Bank charges: deductible expense | Same |
| ING BANK ŚLĄSKI, ING PL | Bank charges: deductible expense | Same |
| SANTANDER POLSKA, BZWBK | Bank charges: deductible expense | Same |
| BANK PEKAO, PEKAO S.A. | Bank charges: deductible expense | Same |
| ALIOR BANK | Bank charges: deductible expense | Same |
| REVOLUT, WISE, N26 (fee lines) | Deductible expense | Check for subscription invoices |
| ODSETKI, INTEREST (credit) | Revenue if business loan interest received; else EXCLUDE | Personal interest = capital income |
| ODSETKI, INTEREST (debit) | Deductible if business loan interest | Personal: EXCLUDE |
| KREDYT, POŻYCZKA (principal) | EXCLUDE | Loan principal movement |

### 3.2 Polish government and statutory bodies

| Pattern | Treatment | Notes |
|---|---|---|
| URZĄD SKARBOWY, US | EXCLUDE | Tax payment -- not deductible |
| ZUS, ZAKŁAD UBEZPIECZEŃ SPOŁECZNYCH | Social ZUS: deductible from income (or as cost); Health ZUS: depends on form | See Section 5.2 |
| CEIDG | EXCLUDE | Registration -- government act |
| GUS | EXCLUDE | Statistical office fees |
| KRS | Deductible if business registration | Court register fee |

### 3.3 Polish utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| PGE, TAURON, ENEA, ENERGA | Deductible if business premises | Home: apportion business % |
| PGNiG, INNOGY | Deductible if business premises (gas) | Apportion if home |
| ORANGE, PLAY, T-MOBILE, PLUS | Deductible: business phone/internet | Mixed-use: apportion |
| UPC, VECTRA, NETIA | Deductible: business internet | Mixed-use: apportion |
| MPWIK, WODOCIĄGI | Deductible if business premises (water) | Apportion if home |

### 3.4 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| PZU, ERGO HESTIA, WARTA, ALLIANZ, AXA | Deductible if business insurance | Personal insurance: NOT deductible from income |
| UBEZPIECZENIE OC/AC (vehicle) | Deductible: business portion of vehicle insurance | If car not in asset register: 20% of costs |

### 3.5 SaaS and software -- international

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | Deductible expense | Reverse charge VAT applies |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Deductible expense | Same |
| ADOBE | Adobe Ireland (IE) | Deductible expense | Same |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Deductible expense (marketing) | Same |
| GITHUB, OPENAI, ANTHROPIC | US entities | Deductible expense | Non-EU |
| SLACK, ATLASSIAN, ZOOM | Various IE/NL/US | Deductible expense | Check billing entity |
| SPOTIFY | Spotify AB (SE) | Deductible expense if business use | EU entity |

### 3.6 Professional services (Poland)

| Pattern | Treatment | Notes |
|---|---|---|
| BIURO RACHUNKOWE, KSIĘGOWA, ACCOUNTING | Deductible expense | Bookkeeping fees |
| KANCELARIA, ADWOKAT, RADCA PRAWNY | Deductible expense | Legal fees if business |
| NOTARIUSZ | Deductible expense | If business transaction |
| DORADCA PODATKOWY | Deductible expense | Tax advisory |

### 3.7 ZUS contributions (special treatment)

| Pattern | Treatment | Notes |
|---|---|---|
| ZUS SPOŁECZNE (emerytalna, rentowa, chorobowa, wypadkowa) | Deductible from income or as KPiR cost | Both methods allowed |
| ZUS ZDROWOTNE (health) -- skala podatkowa | NOT deductible | Non-deductible under skala |
| ZUS ZDROWOTNE (health) -- podatek liniowy | Deductible from income up to annual limit | Check current limit |
| ZUS ZDROWOTNE (health) -- ryczałt | 50% deductible from revenue | Half deductible |
| FUNDUSZ PRACY | Deductible | Labour fund contribution |

### 3.8 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| PKP, PKP INTERCITY | Deductible if business travel (delegacja) | Document purpose |
| LOT, RYANAIR, WIZZAIR | Deductible if business travel | Document purpose and destination |
| UBER, BOLT, FREENOW | Deductible if business purpose | Document occasion |
| ORLEN, BP, SHELL, CIRCLE K (fuel) | Deductible: if car in asset register, 100% business or 75% mixed; if private car, 20% | Requires documentation |
| PARKING, APCOA, SKYCASH | Deductible if business purpose | Document occasion |

### 3.9 Office and supplies

| Pattern | Treatment | Notes |
|---|---|---|
| MEDIA EXPERT, RTV EURO AGD, KOMPUTRONIK | Capital if > PLN 10,000; else deductible | Check środki trwałe threshold |
| IKEA, LEROY MERLIN | Capital or expense depending on amount | Office furniture/equipment |
| CASTORAMA, OBI | Deductible if business premises repairs | Document purpose |
| ALLEGRO, AMAZON.PL | Deductible if business purchase | Verify nature of purchase |

### 3.10 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| BIEDRONKA, LIDL, ŻABKA, KAUFLAND, AUCHAN | Default: NOT deductible (personal provisioning) | Deductible only if hospitality/catering business |
| RESTAURANT, RESTAURACJA | Deductible if documented business purpose (representation) | Unlike Sweden, PL allows business meal deduction with documentation |

### 3.11 Rent and property

| Pattern | Treatment | Notes |
|---|---|---|
| CZYNSZ, WYNAJEM (monthly rent) | Deductible if business premises | Home office: proportional to business area |
| WSPÓLNOTA MIESZKANIOWA | NOT deductible unless home office proportion | Housing cooperative fees |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| PRZELEW WŁASNY, OWN TRANSFER | EXCLUDE | Internal movement |
| WPŁATA WŁASNA | EXCLUDE | Owner capital injection |
| WYPŁATA, DRAWINGS | EXCLUDE | Owner drawings |
| DYWIDENDA | EXCLUDE | Dividend (capital income) |
| LOKATA, SAVINGS | EXCLUDE | Savings transfer |

---

## Section 4 -- Worked examples

### Example 1 -- Skala podatkowa, standard computation

**Input:** JDG, skala podatkowa, revenue PLN 300,000, costs PLN 100,000, social ZUS PLN 18,000.
**Computation:** Dochód = PLN 200,000. Less social ZUS = PLN 182,000. Tax: 12% on PLN 120,000 = PLN 14,400; 32% on PLN 62,000 = PLN 19,840. Total = PLN 34,240. Less kwota zmniejszająca PLN 3,600. Tax = PLN 30,640.

### Example 2 -- Private car used for business (20% rule)

**Input line:**
`2025-04-15 ; ORLEN WARSZAWA ; DEBIT ; Fuel ; -350.00 PLN`

**Reasoning:** Car is NOT in the business asset register (środki trwałe). Per Art. 23 PIT Act, only 20% of total car expenses are deductible. Deductible amount = PLN 70.00.

### Example 3 -- Capital asset above PLN 10,000

**Input line:**
`2025-07-01 ; KOMPUTRONIK ; DEBIT ; Laptop ThinkPad ; -12,500.00 PLN`

**Reasoning:** Above PLN 10,000. Must enter środki trwałe register. Computer hardware: 30% straight-line depreciation. Year 1 (6 months): PLN 12,500 x 30% x 6/12 = PLN 1,875 depreciation.

### Example 4 -- Ryczałt IT services

**Input:** Revenue PLN 400,000, social ZUS PLN 18,000, health ZUS 50% deductible = PLN 6,000.
**Computation:** Base = PLN 400,000 - PLN 18,000 - PLN 6,000 = PLN 376,000. Tax at 12% = PLN 45,120. No expense deductions under ryczałt.

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Skala podatkowa rates

12% on first PLN 120,000. 32% above. Kwota zmniejszająca podatek = PLN 3,600 (= PLN 30,000 x 12%). Monthly tax-reducing amount = PLN 300. **Legislation:** PIT Act art. 27.

### 5.2 ZUS contribution deductibility

Social contributions (społeczne): fully deductible from income (all forms). Health contribution (zdrowotna): NOT deductible under skala; deductible up to limit under liniowy; 50% deductible under ryczałt. **Legislation:** PIT Act, Health Insurance Act.

### 5.3 Podatek liniowy

19% flat on net income. No kwota wolna. No joint filing. No child credit. Health contribution deductible up to annual limit. **Legislation:** PIT Act art. 30c.

### 5.4 Ryczałt rates

Tax on gross revenue, not profit. No expense deductions. Rates: 17% (liberal professions), 15% (consulting), 12% (IT services), 8.5% (general services), 5.5% (construction), 3% (trade). Rate depends on PKD code. Revenue limit: PLN 8,569,200. **Legislation:** Ryczałt Act.

### 5.5 Capital asset threshold

Assets above PLN 10,000: must enter środki trwałe register and depreciate. Below PLN 10,000: may expense immediately. Car depreciation cap: PLN 150,000 (combustion) / PLN 225,000 (electric). **Legislation:** PIT Act art. 22a--22o.

### 5.6 Depreciation rates

Computer hardware: 30%. Software: 50%. Passenger cars: 20%. Office furniture: 20%. Buildings: 2.5%. Depreciation starts month after asset placed in service. **Legislation:** PIT Act art. 22a--22o.

### 5.7 Private car expenses

Car NOT in asset register: only 20% deductible. Car IN register: 100% if exclusively business; 75% if mixed use. **Legislation:** PIT Act art. 23.

### 5.8 VAT interaction

VAT collected: NOT income. Input VAT recovered: NOT expense. Non-deductible VAT (e.g., 50% on passenger cars): IS expense. VAT-exempt (under PLN 200,000): gross = net. **Legislation:** VAT Act.

### 5.9 Record keeping

KPiR required for skala/liniowy. Ewidencja przychodów for ryczałt. Retention: 5 years from end of year return was filed. JPK reporting for digital books. **Legislation:** PIT Act, Tax Ordinance.

### 5.10 Czynny żal (voluntary disclosure)

Filing voluntary correction before audit initiation provides immunity from fiscal penalties. Critical safety valve. **Legislation:** Kodeks karny skarbowy.

---

## Section 6 -- Tier 2 catalogue (reviewer judgement required)

### 6.1 Ryczałt rate classification

*Why ambiguous:* Rate depends on specific PKD code and nature of services. Many IT activities could be 12% or 15%. *Default:* STOP -- do not guess rate. *Question:* "What is your PKD code? What specific services do you provide?"

### 6.2 IP Box eligibility

*Why ambiguous:* Requires R&D documentation, separate IP income ledger, nexus ratio. Incorrect application carries significant penalty risk. *Default:* Do not apply without reviewer confirmation. *Question:* "Do you have R&D cost documentation and a separate IP income ledger?"

### 6.3 Mixed-use vehicle

*Why insufficient:* Business vs private use proportion unknown. *Default:* 20% of expenses (car not in register). *Question:* "Is your car in the business asset register (środki trwałe)? If so, is it exclusively or mixed business use?"

### 6.4 Home office proportion

*Why insufficient:* Business area unknown. *Default:* 0% deduction. *Question:* "Do you have a dedicated room for business? What proportion of total floor area?"

### 6.5 ZUS optimization (ulga na start / preferencyjne)

*Why ambiguous:* ZUS basis depends on business duration and elections. *Default:* Use amounts actually paid per ZUS DRA. *Question:* "Are you in the ulga na start period, preferencyjne ZUS, or standard ZUS?"

### 6.6 Switching between lump-sum and real expenses

*Why complex:* Transition adjustment required for receivables and payables. *Default:* Flag for reviewer. *Question:* "Did you switch expense methods this year? If so, provide year-end receivables/payables from prior year."

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"

| Column | Content |
|---|---|
| A | Date |
| B | Counterparty |
| C | Description |
| D | Amount (PLN) |
| E | Category (Revenue / KPiR Cost / Depreciation / ZUS Social / ZUS Health / EXCLUDE) |
| F | Deductible amount |
| G | Default? (Y/N) |
| H | Question for client |
| I | Notes |

### Sheet "Tax Computation"

Branches by taxation form: skala podatkowa, liniowy, or ryczałt. Each with step-by-step formulas per Section 5.

---

## Section 8 -- Bank statement reading guide

**CSV format conventions.** PKO BP exports use semicolons with DD.MM.YYYY dates. mBank exports use CSV with comma delimiters. ING PL uses semicolons. Common columns: Data (Date), Opis (Description), Kwota (Amount), Saldo (Balance).

**Polish language variants.** Common: przelew (transfer), wpłata (deposit), wypłata (withdrawal), prowizja (commission/fee), odsetki (interest), faktura (invoice), opłata (charge), czynsz (rent).

**ZUS payments.** Monthly payments to ZUS appear as "ZUS" or "ZAKŁAD UBEZPIECZEŃ SPOŁECZNYCH". Separate social from health contributions using payment details or ZUS DRA statements.

**Tax payments.** Payments to Urząd Skarbowy for PIT advances: EXCLUDE (not deductible).

**Foreign currency.** Convert to PLN at NBP average rate for the business day before the transaction.

---

## Section 9 -- Onboarding fallback (only when inference fails)

### 9.1 Business form
*Inference:* JDG identifiable from CEIDG registration or account type. *Fallback:* "Are you a JDG (sole proprietorship) or operating through a spółka?"

### 9.2 Taxation form
*Inference:* Not inferable from bank statement. Always ask. *Fallback:* "Which taxation form have you chosen: skala podatkowa, podatek liniowy, or ryczałt?"

### 9.3 PKD code
*Inference:* Inferable from counterparty mix and invoice descriptions. *Fallback:* "What is your PKD code? (Required for ryczałt rate determination.)"

### 9.4 ZUS basis
*Inference:* ZUS payment amounts may indicate ulga na start vs standard. *Fallback:* "Are you in ulga na start, preferencyjne, or standard ZUS?"

### 9.5 VAT status
*Inference:* VAT payments in bank statement. *Fallback:* "Are you a czynny podatnik VAT (active VAT payer)?"

### 9.6 Prior year losses
*Inference:* Not inferable. *Fallback:* "Do you have losses carried forward from prior years?"

---

## Section 10 -- Reference material

### Test suite

**Test 1 -- Skala podatkowa, mid-range.**
PLN 300,000 revenue, PLN 100,000 costs, PLN 18,000 social ZUS. Tax = PLN 30,640.

**Test 2 -- Podatek liniowy, high income.**
PLN 500,000 dochód, PLN 18,000 social ZUS, PLN 12,000 health deductible. Tax = PLN 89,300.

**Test 3 -- Ryczałt IT 12%.**
PLN 400,000 revenue, PLN 18,000 social ZUS, PLN 6,000 health (50%). Tax = PLN 45,120.

**Test 4 -- Kwota wolna on flat tax.**
Client on PIT-36L claims PLN 30,000 tax-free. REJECT -- kwota wolna does not apply to liniowy.

**Test 5 -- Car depreciation cap.**
Car PLN 200,000. Deductible depreciation = PLN 150,000 x 20% = PLN 30,000. Excess non-deductible.

### Edge case registry

**EC1 -- Kwota wolna claimed under liniowy.** INCORRECT.
**EC2 -- Ryczałt rate misclassified.** Flag for reviewer -- PKD code determines rate.
**EC3 -- Business expenses under ryczałt.** INCORRECT -- ryczałt taxes revenue.
**EC4 -- Health contribution deducted under skala.** INCORRECT.
**EC5 -- IP Box without documentation.** Revert to base form.
**EC6 -- Private car 100% expenses.** Cap at 20% if not in asset register.
**EC7 -- Joint filing with liniowy.** NOT available.
**EC8 -- Czynny żal after audit.** TOO LATE.
**EC9 -- Ulga dla klasy średniej.** Abolished since July 2022.
**EC10 -- Car depreciation above cap.** PLN 150,000 combustion / PLN 225,000 electric.

### Prohibitions

- NEVER apply kwota wolna to podatek liniowy or ryczałt
- NEVER deduct business expenses under ryczałt
- NEVER deduct health contribution under skala podatkowa
- NEVER allow joint filing for podatek liniowy
- NEVER apply ulga dla klasy średniej (abolished 2022)
- NEVER apply IP Box without R&D documentation
- NEVER allow 100% car expenses for private cars not in asset register
- NEVER exceed car depreciation caps
- NEVER present calculations as definitive
- NEVER advise on international income, CFC rules, or transfer pricing

### Sources

1. Ustawa o podatku dochodowym od osob fizycznych (PIT Act, 26 July 1991)
2. Ustawa o zryczaltowanym podatku dochodowym (Ryczałt Act, 20 November 1998)
3. Ustawa o systemie ubezpieczeń społecznych (Social Insurance Act)
4. Ordynacja podatkowa (Tax Ordinance)
5. podatki.gov.pl

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a doradca podatkowy, biegły rewident, or equivalent licensed practitioner in Poland) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
