---
name: se-income-tax
description: Use this skill whenever asked about Swedish income tax for self-employed individuals (enskild firma / enskild näringsidkare). Trigger on phrases like "Swedish tax", "kommunalskatt", "statlig inkomstskatt", "jobbskatteavdrag", "grundavdrag", "NE-bilaga", "F-skatt", "expansionsfond", "räntefördelning", "Inkomstdeklaration 1", "self-employed tax Sweden", or any question about filing or computing income tax for a Swedish self-employed client. Covers kommunalskatt, statlig inkomstskatt, jobbskatteavdrag, grundavdrag, egenavgifter, F-skatt, expansionsfond, räntefördelning, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Swedish income tax work.
version: 2.0
jurisdiction: SE
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SE Income Tax

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Sweden (Konungariket Sverige) |
| Tax type | Personal income tax on business income (inkomst av näringsverksamhet) |
| Primary legislation | Inkomstskattelagen (IL, 1999:1229) |
| Supporting legislation | Skatteförfarandelagen (SFL, 2011:1244); Socialavgiftslagen (SAL, 2000:980); Bokföringslagen (BFL, 1999:1078) |
| Tax authority | Skatteverket (Swedish Tax Agency) |
| Filing portal | skatteverket.se / Mina sidor |
| Currency | SEK only |
| Return form | Inkomstdeklaration 1 with NE-bilaga (business income attachment) |
| Filing deadline (digital) | 2 May of the following year; for income year 2026 that is Monday 3 May 2027, because 2 May 2027 is a Sunday (SFL 32 kap. 1 §; Lag 1930:173, 2 §) |
| Filing deadline (via ombud) | 16 June |
| F-skatt instalments | 12th of each month |
| Kommunalskatt (municipal + regional) | 2026 average 32.38% (range 28.93% Österåker to 35.65% Dorotea) |
| Statlig inkomstskatt (state tax) | 20% on taxable earned income above SEK 643,000 (skiktgräns 2026, same at every age). Before the basic deduction this is reached at SEK 660,400 under 66 and SEK 760,500 from 66 (brytpunkt) |
| Egenavgifter (self-employment contributions) | 28.97% if born 1959 or later; 10.21% (old-age pension contribution only) if born 1938-1958; none if born 1937 or earlier (2026) |
| Grundavdrag (basic deduction) | Under 66: SEK 25,100 at low income, at most SEK 45,600, at least SEK 17,400. 66 or over at 1 January 2026: SEK 65,800 at low income, at most SEK 179,100, at least SEK 117,500 |
| Jobbskatteavdrag | Credit against kommunalskatt. Business surplus counts as work income (IL 67 kap. 6 §). Formula: IL 67 kap. 7 § (under 66) and 8 § (66 or over); worked in [se-employee-income-tax](se-employee-income-tax.md) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Swedish auktoriserad or godkänd revisor sign-off |
| Validation date | Pending |

**Read this whole section before classifying anything.**

**Key NE-bilaga fields**

| Field | Description |
| --- | --- |
| R1 | Gross revenue (intäkter) |
| R2 | Cost of goods sold |
| R3--R6 | Operating expenses (by category) |
| R7 | Depreciation (avskrivningar) |
| R8 | Other expenses |
| R9 | Net business result (överskudd/underskudd) |
| R14 | Sjukpenninggrundande inkomst (SGI -- sickness benefit base) |
| R24 | Räntefördelning (interest allocation) |
| R33--R35 | Expansionsfond (expansion fund) |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown expense category | Not deductible |
| Unknown business-use proportion (phone, car, home office) | 0% business use |
| Unknown whether capital or revenue expenditure | Capital (depreciate, do not expense) |
| Unknown moms treatment | Exclude moms from revenue and costs if momsregistrerad |
| Unknown municipality | Average kommunalskatt 32.38% for 2026 (flag as estimated) |
| Unknown F-skatt status | Assume not registered (flag immediately) |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | SEK 50,000 |
| HIGH tax-delta on a single conservative default | SEK 5,000 |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net tax position | SEK 100,000 |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — bank statement for the tax year in CSV, PDF, or pasted text. Must cover 1 January to 31 December. Acceptable from any Swedish bank: Handelsbanken, SEB, Swedbank, Nordea, Danske Bank, Länsförsäkringar, Skandiabanken, or fintech banks (Revolut, Wise, N26).
- **Recommended inputs** — sales invoices for the year, purchase invoices for any expense above SEK 10,000, municipality of residence, NE-bilaga from prior year (for loss carry-forward and räntefördelning basis).
- **Ideal inputs** — complete bookkeeping (verifikationer), balance sheet for räntefördelning/expansionsfond calculations, prior year Inkomstdeklaration 1, F-skatt registration confirmation.
- **Refusal policy if minimum is missing** — SOFT WARN. If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This NE-bilaga was produced from bank statement alone. The reviewer must verify that expense classifications are correct and that capital items have been properly identified."

### Refusal catalogue

- **R-SE-1 -- Aktiebolag (AB) instead of enskild firma** — Trigger: client operates through an AB (limited company). Message: "This skill covers enskild firma (sole proprietorship) only. AB taxation follows the corporate income tax rules (20.6% bolagsskatt) and different filing forms. Please use a separate skill or consult an auktoriserad revisor."
- **R-SE-2 -- 3:12 rules (fåmansbolag)** — Trigger: client has a closely held company and asks about dividend taxation under 3:12 rules. Message: "The 3:12 rules for fåmansbolag are outside the scope of this skill. Please consult an auktoriserad revisor."
- **R-SE-3 -- International income** — Trigger: client has significant foreign-source income or asks about tax treaty application. Message: "International income and tax treaty questions are outside this skill's scope. Please consult a qualified tax advisor."
- **R-SE-4 -- Handelsbolag / kommanditbolag** — Trigger: client operates through a partnership. Message: "Partnership taxation has specific rules for income allocation between partners. This skill covers enskild firma only."

## Section 3 -- Transaction pattern library (the lookup table)

This is the deterministic pre-classifier for income tax purposes. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific.

### 3.1 Swedish banks (fees and interest -- classify correctly)

**Swedish banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HANDELSBANKEN | Bank charges: deductible expense (R3--R6) | Monthly/annual service fees |
| SEB, SKANDINAVISKA ENSKILDA | Bank charges: deductible expense | Same |
| SWEDBANK, SPARBANKEN | Bank charges: deductible expense | Same |
| NORDEA | Bank charges: deductible expense | Same |
| DANSKE BANK | Bank charges: deductible expense | Same |
| LÄNSFÖRSÄKRINGAR | Bank charges: deductible expense; insurance premiums: deductible if business | Separate fee lines from insurance |
| REVOLUT, WISE, N26 (fee lines) | Deductible expense for transaction/maintenance fees | Check for separate subscription invoices |
| RÄNTA, INTEREST (credit) | EXCLUDE from business income | Interest income is inkomst av kapital, not näringsverksamhet |
| RÄNTA, INTEREST (debit) | Deductible if business loan interest | If personal loan interest: EXCLUDE |
| LÅN, LOAN (principal movements) | EXCLUDE | Loan principal is not income or expense |

### 3.2 Swedish government, tax authority, and statutory bodies

**Government bodies pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SKATTEVERKET, SKV | EXCLUDE | Tax payment (F-skatt, moms, arbetsgivaravgifter) -- not a deductible expense |
| SKATTEKONTO | EXCLUDE | Tax account movement |
| F-SKATT | EXCLUDE | Preliminary tax payment |
| BOLAGSVERKET | Deductible expense | Company registration fees |
| MOMS, MERVÄRDESKATT (payment to SKV) | EXCLUDE | VAT remittance |
| FÖRSÄKRINGSKASSAN | EXCLUDE | Social insurance authority -- benefits or repayments |
| KRONOFOGDEN | NOT deductible | Enforcement fees/fines -- public policy |
| ARBETSFÖRMEDLINGEN | EXCLUDE | Employment agency -- government body |

### 3.3 Swedish utilities and telecoms

**Utilities and telecoms pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VATTENFALL | Deductible if business premises electricity | If home: apportion business % |
| E.ON, FORTUM | Same as above | Electricity supplier |
| STOCKHOLMS STAD, [municipality] KOMMUN (water/waste) | Deductible if business premises | Apportion if home office |
| TELIA, TELENOR, TRE (3), HALEBOP, COMVIQ | Deductible: business phone/internet | If mixed-use: apportion business % |
| BREDBANDSBOLAGET, BAHNHOF | Deductible: business internet | If mixed-use: apportion |

### 3.4 Insurance

**Insurance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| LÄNSFÖRSÄKRINGAR, TRYGG-HANSA, IF SKADEFÖRSÄKRING | Deductible if business insurance (professional indemnity, business property) | Personal insurance: NOT deductible |
| FOLKSAM, SKANDIA | Same | Separate business from personal lines |
| PENSIONSFÖRSÄKRING, IPS | EXCLUDE from business | Pension -- separate deduction in inkomst av kapital |

### 3.5 SaaS and software -- international

**SaaS/software international pattern table**

| Pattern | Billing entity | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | Deductible expense; moms: reverse charge | Exclude moms from cost if momsregistrerad |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Deductible expense | Same |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Deductible expense | Same |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Deductible expense (marketing) | Same |
| GITHUB | GitHub Inc (US) | Deductible expense | Non-EU; reverse charge moms |
| SLACK, ATLASSIAN, ZOOM | Various IE/NL/US entities | Deductible expense | Check billing entity for moms |
| OPENAI, CHATGPT, ANTHROPIC, CLAUDE | US entities | Deductible expense | Non-EU |
| NOTION | Notion Labs Inc (US) | Deductible expense | Non-EU |
| FIGMA, CANVA | US/AU entities | Deductible expense | Non-EU |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | Deductible expense if business use | Swedish entity -- domestic moms |

### 3.6 Professional services (Sweden)

**Professional services pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| REVISOR, REDOVISNING, BOKFÖRING, ACCOUNTING | Deductible expense (R3--R6) | Accountancy/bookkeeping fees -- always deductible |
| ADVOKAT, JURIST, LAWYER | Deductible expense | If business legal matter |
| NOTARIUS, NOTARY | Deductible expense | If business transaction |
| KONSULT (received from) | REVENUE (R1) | Client paying for consulting services |

### 3.7 Payroll and social contributions (exclude or classify)

**Payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| LÖN, SALARY, LÖNEUTBETALNING (outgoing to employees) | Deductible expense (R3--R6) | Staff salary cost |
| ARBETSGIVARAVGIFT (payment to SKV) | Deductible expense | Employer social contributions |
| EGENAVGIFTER (own social contributions) | Deductible via schablonavdrag (25%; 10% if born 1938-1958) | See Section 5.2 |
| FACKAVGIFT, UNIONEN, IF METALL | Deductible expense | Trade union dues for employees |

### 3.8 Transport and travel

**Transport and travel pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SL, VÄSTTRAFIK, SKÅNETRAFIKEN | Deductible if business travel | Public transport for business trips |
| SJ, MTRX (train) | Deductible if business travel | Document purpose |
| SAS, NORWEGIAN, RYANAIR (flights) | Deductible if business travel | Document purpose and destination |
| TAXI STOCKHOLM, TAXI KURIR, UBER, BOLT | Deductible if business travel | Document purpose |
| OKQ8, CIRCLE K, PREEM, SHELL, ST1 (fuel) | Deductible: business portion only | If private car: SEK 25.00/mil standard rate instead |
| BILPROVNING (vehicle inspection) | Deductible if business vehicle | Private car: include in km-rate |
| PARKERING, APCOA, EASYPARK | Deductible if business purpose | Document occasion |

### 3.9 Office and supplies

**Office and supplies pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STAPLES, OFFICE DEPOT, CLAS OHLSON | Deductible expense | Office supplies |
| IKEA (business furniture) | Capital if SEK 29,600 or more excluding moms and life > 3 years; else deductible expense | Half prisbasbelopp threshold, 2026 (IL 18 kap. 4 §) |
| ELGIGANTEN, MEDIAMARKT, KOMPLETT | Capital if SEK 29,600 or more excluding moms and life > 3 years; else deductible | Computer/electronics |
| POSTNORD | Deductible expense | Postage and shipping |
| WEBHALLEN, INET | Capital or expense depending on amount | IT equipment |

### 3.10 Food and entertainment

**Food and entertainment pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ICA, COOP, WILLYS, HEMKÖP, LIDL | Default: NOT deductible (personal provisioning) | Only deductible if hospitality/catering business |
| RESTAURANT, RESTAURANG (any named restaurant) | NOT deductible: external representation food | SEK 0 deduction for external meals |
| INTERN REPRESENTATION | Deductible up to SEK 300/person/event | Internal events only; enklare förtäring |

### 3.11 Rent and property

**Rent and property pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HYRA, HYRESVÄRD, [landlord name] (monthly rent) | Deductible if dedicated business premises | Home office: use proportional or SEK 2,000 standard |
| HEMFÖRSÄKRING (home insurance) | NOT deductible unless home office proportion | Apportion if home office claimed |
| BOSTADSRÄTTSFÖRENING, BRF | NOT deductible unless home office proportion | Monthly fee for housing cooperative |

### 3.12 Internal transfers and exclusions

**Internal transfers and exclusions pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EGEN ÖVERFÖRING, OWN TRANSFER, INTERNAL | EXCLUDE | Internal account movement |
| EGET UTTAG, EGNA UTTAG, DRAWINGS | EXCLUDE | Owner drawings -- not an expense |
| INSÄTTNING, OWN DEPOSIT | EXCLUDE | Owner capital injection |
| UTDELNING, DIVIDEND | EXCLUDE | Dividend (capital income, not business) |
| SPARANDE, SAVINGS | EXCLUDE | Transfer to savings |

## Section 4 -- Worked examples

These are four fully worked income tax classifications drawn from a hypothetical Swedish enskild firma IT consultant.

### Example 1 -- SaaS subscription (reverse charge moms interaction)

**Input line:**
`2026-03-15 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Workspace ; -1,200.00 SEK`

**Reasoning:**
Google Ireland Ltd is an EU entity (Section 3.5). The consultant is momsregistrerad. Reverse charge moms applies -- the consultant reports output moms and claims input moms on the momsdeklaration (net zero). For income tax purposes, the expense is deductible at the net amount (SEK 1,200). Moms is NOT included in R1 revenue or expense costs.

**Classification:** Deductible business expense, R3--R6 (software/IT). Amount: SEK 1,200.

### Example 2 -- Capital equipment above threshold

**Input line:**
`2026-06-20 ; ELGIGANTEN ; DEBIT ; MacBook Pro 14" ; -22,990.00 SEK`

**Reasoning:**
Half prisbasbelopp for 2026 is SEK 29,600 (price base amount SEK 59,200). The consultant is momsregistrerad, so the cost is SEK 22,990 / 1.25 = SEK 18,392 excluding moms. That is below SEK 29,600, so the computer is an asset of low value and the whole cost is deducted at once (IL 18 kap. 4 §), even though it will last more than 3 years. Only an asset costing SEK 29,600 or more excluding moms, with a life over 3 years, goes into the inventarier pool (year 1 depreciation at most 30%, IL 18 kap. 13 §).

**Classification:** Deductible expense, R3--R6, SEK 18,392 (direktavdrag). Input moms of SEK 4,598 goes on the momsdeklaration, not in the NE-bilaga.

### Example 3 -- External restaurant meal (not deductible)

**Input line:**
`2026-09-10 ; RESTAURANG PELIKAN STOCKHOLM ; DEBIT ; Client dinner ; -2,400.00 SEK`

**Reasoning:**
External representation food costs are NOT deductible for income tax in Sweden. Only simpler refreshments (enklare förtäring) at internal events are deductible up to SEK 300/person. This is a client dinner -- zero deduction regardless of business purpose.

**Classification:** NOT deductible. Exclude from R3--R6 expenses entirely.

### Example 4 -- Home office standard deduction

**Input line:**
(No single bank line -- client claims home office)

**Reasoning:**
The client can choose either the standard deduction of SEK 2,000/year or actual costs proportional to floor area. Cannot combine both. If actual costs exceed SEK 2,000 and the client has a dedicated room, actual method may be better but requires documentation.

**Classification:** R3--R6 expense, SEK 2,000 (standard deduction). Flag for reviewer if actual costs are claimed instead.

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Kommunalskatt computation

- **Kommunalskatt computation** — Applied to taxable earned income (beskattningsbar förvärvsinkomst) at the rate of the municipality where the person was registered on 1 November 2025. If municipality unknown, use the 2026 average of 32.38%. Range 2026: 28.93% (Österåker) to 35.65% (Dorotea).  _(IL kap. 65; SCB, Kommunalskatter 2026)_

### 5.2 Egenavgifter and schablonavdrag

- **Egenavgifter and schablonavdrag** — The rate follows the year of birth, not the age on a given day. Born 1959 or later: full egenavgifter of 28.97% (16.35% under SAL 3 kap. 13 § plus allmän löneavgift 12.62%). Born 1938-1958: only the old-age pension contribution of 10.21% (SAL 3 kap. 15 §, which from 2026 applies to those who were 67 at the start of the year). Born 1937 or earlier: no egenavgifter (SAL transitional rule 2000:980 point 6). Someone born 1959 or later who had full old-age pension all of 2026, or full sickness or activity compensation for any part of it, also pays only 10.21% (SAL 3 kap. 16 §). Since egenavgifter are calculated on the profit they reduce, apply a schablonavdrag as a preliminary deduction from net business profit: 25% where the full rate applies, 10% where only 10.21% applies. Actual egenavgifter are reconciled the following year (IL 16 kap. 29 §).  _(SAL 3 kap.; Skatteverket, belopp och procent 2026)_
- **Schablonavdrag computation** — (1) Net profit before egenavgifter = X. (2) Schablonavdrag = X x 25% (or 10%) = Y. (3) Taxable business income = X - Y. (4) Egenavgifter computed on that base at 28.97% (or 10.21%).  _(SAL; IL 16 kap. 29 §)_

### 5.3 Statlig inkomstskatt

- **Statlig inkomstskatt** — 20% on taxable earned income (after the basic deduction) above SEK 643,000 for 2026, at every age. Measured before the basic deduction, that point (brytpunkt) is SEK 660,400 under 66 and SEK 760,500 from 66.  _(IL 65 kap. 5 §; Skatteverket, belopp och procent 2026)_

### 5.4 Grundavdrag

- **Grundavdrag** — Income-dependent basic deduction on the assessed earned income (business surplus after the schablonavdrag), rounded up to the next SEK 100. Under 66: SEK 25,100 at low income, at most SEK 45,600, at least SEK 17,400. 66 or over at 1 January 2026 (born 1959 or earlier): SEK 65,800 at low income, at most SEK 179,100, at least SEK 117,500. The band formula is in [se-employee-income-tax](se-employee-income-tax.md). Computed automatically by Skatteverket. Reduces taxable earned income before both kommunalskatt and statlig skatt.  _(IL 63 kap. 3 and 3 a §§)_

### 5.5 Capital expenditure threshold

- **Capital expenditure threshold** — Assets costing half prisbasbelopp or more (SEK 29,600 excluding moms in 2026) with useful life over 3 years: must enter inventarier pool and depreciate. Assets below that, or with life of 3 years or less: expense immediately (direktavdrag). Items bought together as one purchase are tested on their combined cost.  _(IL 18 kap. 4 §)_

### 5.6 Depreciation rates

- **Depreciation rates** — Inventarier (machinery, equipment): 30% declining balance (räkenskapsenlig avskrivning) or 20% straight-line (supplementary rule). Buildings: 2--5% straight-line. Goodwill: pooled with inventarier at 30%.  _(IL kap. 18, 19, 20)_

### 5.7 Motor vehicle standard rate

- **Motor vehicle standard rate (2026)** — SEK 25 per mil (business travel using a private car; alternative: actual costs with logbook apportionment)  _(IL kap. 16)_

### 5.8 Home office deduction

- **Home office deduction** — Standard deduction: SEK 2,000/year (no documentation required). Alternative: actual proportional costs (requires floor area calculation and dedicated room). Cannot combine both methods.  _(IL kap. 16)_

### 5.9 Representation

- **Representation** — Internal: up to SEK 300/person/event for enklare förtäring. External: food costs NOT deductible for income tax (even if limited moms deduction applies).  _(IL kap. 16)_

### 5.10 Moms interaction

- **Moms interaction** — Moms collected on sales: NOT income (exclude from R1). Input moms recovered: NOT an expense (exclude from costs). Non-deductible moms (e.g., representation): IS an expense. Non-momsregistrerad (turnover not above SEK 120,000 this year or either of the two previous years): no moms separation needed, gross = net.  _(ML 18 kap. 4 §)_

### 5.11 F-skatt

- **F-skatt** — All self-employed must register for F-skatt. Monthly instalments due 12th of each month. Without F-skatt, clients paying the individual must pay arbetsgivaravgifter.  _(SFL kap. 55)_

### 5.12 Loss carry-forward

- **Loss carry-forward** — Business losses (underskudd) carry forward to future years within the same income category (näringsverksamhet). No time limit on carry-forward.  _(IL kap. 40)_

### 5.13 Record keeping

- **Record keeping** — Minimum retention: 7 years from end of calendar year. Must follow god redovisningssed. Digital or paper permitted.  _(BFL)_

## Section 6 -- Tier 2 catalogue (reviewer judgement required)

### 6.1 Jobbskatteavdrag computation

- **Jobbskatteavdrag computation** — Compute it. The surplus of active business income counts as work income, after general deductions, rounded down to SEK 100 (IL 67 kap. 6 §). Under 66 at 1 January 2026 use IL 67 kap. 7 §; 66 or over use 67 kap. 8 §. The formula, the order of credits and a worked example are in [se-employee-income-tax](se-employee-income-tax.md); do not repeat them here. The SEK 1,500 earned income credit (IL 67 kap. 46-47 §§) also applies. Inputs needed: municipality on 1 November 2025 and year of birth. Question: "Which municipality were you registered in on 1 November 2025, and what is your year of birth?"

### 6.2 Expansionsfond allocation

- **Expansionsfond allocation** — Why ambiguous: Requires accurate kapitalunderlag using SKV 2196. 20.6% tax on allocation, deferred until reversal. Maximum limited by net business assets. Default: Do not allocate without reviewer confirmation. Question: "Do you want to allocate profit to expansionsfond? If so, provide your net business assets (kapitalunderlag) calculation."

### 6.3 Räntefördelning

- **Räntefördelning** — Why ambiguous: Positive räntefördelning reclassifies business income as capital income (30% tax). Positive räntefördelning is open when the capital base (kapitalunderlag) is above SEK 0. Rate for 2026: 8.55% (statslåneräntan 2.55% at 30 November 2025 + 6 points). Default: Do not apply without reviewer confirmation. Question: "What were your net business assets at the start of the income year?"

### 6.4 Mixed-use phone/internet

- **Mixed-use phone/internet** — Why insufficient: Business proportion unknown from bank statement alone. Default: 0% business use. Question: "Is this a dedicated business line or mixed-use? What percentage is business?"

### 6.5 Motor vehicle documentation

- **Motor vehicle documentation** — Why insufficient: Business km unknown. Default: Use standard rate SEK 25.00/mil only with documented business km. Question: "Do you have a logbook showing business vs private km?"

### 6.6 Home office -- actual vs standard

- **Home office -- actual vs standard** — Why ambiguous: Choice of method affects deduction amount. Default: SEK 2,000 standard deduction. Question: "Do you have a dedicated room exclusively for business? What is its proportion of total floor area?"

### 6.7 Negative räntefördelning

- **Negative räntefördelning** — Why ambiguous: Mandatory if the capital base (kapitalunderlag) at the start of the year is below minus SEK 500,000; 2026 rate 3.55%. Moves an amount from capital income to business income. Default: Flag for reviewer. Question: "Were the business's liabilities more than SEK 500,000 above its assets at the start of the year?"

## Section 7 -- Excel working paper template

### Sheet "Transactions"

**Sheet Transactions columns**

| Column | Content |
| --- | --- |
| A | Date (YYYY-MM-DD) |
| B | Counterparty |
| C | Description |
| D | Amount (SEK, positive = income, negative = expense) |
| E | Category (R1 Revenue / R2 COGS / R3-R6 Expense / R7 Depreciation / EXCLUDE / CAPITAL) |
| F | Deductible amount (after any apportionment) |
| G | Default? (Y/N) |
| H | Question for client |
| I | Notes |

### Sheet "NE-bilaga Summary"

**NE-bilaga Summary formulas**

| Row | Field | Formula |
| --- | --- | --- |
| R1 | Gross revenue | =SUMIFS(Transactions!F:F, Transactions!E:E, "R1") |
| R2 | Cost of goods sold | =SUMIFS(Transactions!F:F, Transactions!E:E, "R2") |
| R3-R6 | Operating expenses | =SUMIFS(Transactions!F:F, Transactions!E:E, "R3-R6") |
| R7 | Depreciation | =SUMIFS(Transactions!F:F, Transactions!E:E, "R7") |
| R9 | Net result | =R1-R2-R3_R6-R7 |

### Sheet "Tax Computation"

**Tax Computation steps**

| Step | Description | Formula |
| --- | --- | --- |
| 1 | Net business profit (R9) | From NE-bilaga |
| 2 | Schablonavdrag (25%; 10% if born 1938-1958) | =Step1 * 0.25 |
| 3 | Taxable business income | =Step1 - Step2 |
| 4 | Grundavdrag | Manual entry (income-dependent) |
| 5 | Beskattningsbar förvärvsinkomst | =Step3 - Step4 |
| 6 | Kommunalskatt | =Step5 * [rate] |
| 7 | Statlig skatt | =MAX(0, (Step5 - 643000) * 0.20) |
| 8 | Jobbskatteavdrag | IL 67 kap. 7 § formula; see se-employee-income-tax |
| 9 | Estimated tax | =Step6 + Step7 - Step8 - 1500 (earned income credit) |
| 10 | Egenavgifter | =Step3 * 0.2897 (0.1021 if born 1938-1958) |

## Section 8 -- Bank statement reading guide

**CSV format conventions.** Handelsbanken exports use semicolon delimiters with YYYY-MM-DD dates. SEB exports use comma or tab delimiters. Swedbank exports typically use semicolons with DD/MM/YYYY dates -- confirm format. Common columns: Datum (Date), Text (Description), Belopp (Amount), Saldo (Balance).

**Swedish language variants.** Common descriptions: lön (salary), hyra (rent), ränta (interest), avgift (fee), köp (purchase), insättning (deposit), uttag (withdrawal), överföring (transfer), faktura (invoice), betalning (payment).

**Internal transfers and exclusions.** Own-account transfers between the client's Handelsbanken, SEB, Swedbank accounts. Labelled "egen överföring", "överföring mellan konton", "sparande". Always exclude.

**Moms interaction.** If client is momsregistrerad, bank statement amounts include moms. For income tax, expenses should be recorded net of recoverable moms. If moms is not recoverable (blocked categories), include gross amount.

**F-skatt payments.** Monthly payments to Skatteverket labelled "F-skatt" or "skattekonto". These are tax payments, NOT business expenses. Always exclude.

**Egenavgifter.** Self-employment contributions are not visible as separate bank transactions -- they are computed on the return. Do not look for them in the bank statement.

**Foreign currency.** Convert to SEK at the transaction date rate. Use Riksbanken's daily exchange rates.

**Cryptic card purchases.** Swedish bank statements often show merchant category codes or abbreviated names. If the counterparty cannot be identified, ask the client.

## Section 9 -- Onboarding fallback (only when inference fails)

### 9.1 Business form

- **Business form** — Inference: Account holder name matching a personal name = enskild firma. "AB" suffix = aktiebolag (refuse via R-SE-1). Fallback: "Are you an enskild firma (sole trader) or operating through a company?"

### 9.2 Municipality

- **Municipality** — Inference: Address on bank statement or prior correspondence. Fallback: "Which municipality do you live in? (Determines your kommunalskatt rate.)"

### 9.3 F-skatt status

- **F-skatt status** — Inference: Presence of F-skatt payments in bank statement. Fallback: "Are you registered for F-skatt?"

### 9.4 Moms registration

- **Moms registration** — Inference: Moms payments to Skatteverket in bank statement. Fallback: "Are you momsregistrerad (VAT registered)?"

### 9.5 Age

- **Age** — Inference: Not inferable from bank statement. Always ask. Fallback: "What is your year of birth?" (Born 1959 or later: full egenavgifter. Born 1938-1958: 10.21%. Born 1959 or earlier is 66 at 1 January 2026 and gets the higher grundavdrag and the jobbskatteavdrag under IL 67 kap. 8 §.)

### 9.6 Industry

- **Industry** — Inference: Counterparty mix, invoice descriptions. Fallback: "In one sentence, what does your business do?"

### 9.7 Prior year losses

- **Prior year losses** — Inference: Not inferable from single-year statement. Fallback: "Do you have any losses carried forward from prior years (underskudd)?"

### 9.8 Net business assets

- **Net business assets** — Inference: Not inferable from bank statement alone. Fallback: "What were your net business assets at the start of the year? (Required for räntefördelning and expansionsfond.)"

### 9.9 Other income

- **Other income** — Inference: Employment income visible as salary credits. Fallback: "Do you have other income sources -- employment, rental, capital gains?"

### 9.10 Expansionsfond / räntefördelning elections

- **Expansionsfond / räntefördelning elections** — Inference: Not inferable. Fallback: "Do you want to allocate to expansionsfond or apply räntefördelning? (Requires separate computation.)"

## Section 10 -- Reference material

### Test suite

All figures are for income year 2026: price base amount SEK 59,200, skiktgräns SEK 643,000, Stockholm total municipal rate 30.55%, average 32.38%.

Input: Enskild firma, Stockholm (kommunalskatt 30.55% for 2026), born 1985, gross revenue SEK 800,000, allowable expenses SEK 200,000, no expansionsfond or räntefördelning, no other income.
Expected: Net profit = SEK 600,000. Schablonavdrag 25% = SEK 150,000. Taxable business income (assessed earned income) = SEK 450,000. Grundavdrag: 450,000 is between 3.11 and 7.88 price base amounts, so 0.77 × 59,200 − 10% × (450,000 − 184,112) = 18,995.20, rounded up to SEK 19,000. Beskattningsbar förvärvsinkomst = SEK 431,000. Below SEK 643,000: no statlig skatt. Kommunalskatt = SEK 131,670.50. Jobbskatteavdrag (IL 67 kap. 7 §, work income 450,000 between 3.24 and 8.08 price base amounts) = (1.813 × 59,200 + 25.1% × (450,000 − 191,808) − 19,000) × 30.55% = SEK 46,782. Earned income credit SEK 1,500. Income tax before burial and church fees = SEK 83,388.50. General pension contribution 7% × 450,000 = SEK 31,500, credited in full if paid on time. Egenavgifter 28.97% × 450,000 = SEK 130,365.

```oa-check
name: Sole trader born 1985, Stockholm, net profit SEK 600,000 (2026)
inputs:
  net_profit: 600000
  pbb: 59200
  municipal_rate: 0.3055
  skiktgrans: 643000
steps:
  - schablonavdrag: net_profit * 0.25
  - earned_income: net_profit - schablonavdrag
  - basic_deduction: ceil((0.77 * pbb - 0.10 * (earned_income - 3.11 * pbb)) / 100) * 100
  - taxable_earned: earned_income - basic_deduction
  - municipal_tax: taxable_earned * municipal_rate
  - state_tax: max(taxable_earned - skiktgrans, 0) * 0.20
  - work_income: floor(earned_income / 100) * 100
  - job_credit: floor((1.813 * pbb + 0.251 * (work_income - 3.24 * pbb) - basic_deduction) * municipal_rate)
  - earned_income_credit: 1500
  - income_tax: municipal_tax + state_tax - job_credit - earned_income_credit
  - pension_contribution: earned_income * 0.07
  - egenavgifter: earned_income * 0.2897
expected:
  schablonavdrag: 150000.00
  earned_income: 450000.00
  basic_deduction: 19000.00
  taxable_earned: 431000.00
  municipal_tax: 131670.50
  state_tax: 0.00
  job_credit: 46782.00
  income_tax: 83388.50
  pension_contribution: 31500.00
  egenavgifter: 130365.00
```

Input: Kommunalskatt 32.38% (2026 average), born 1980, net business profit SEK 900,000 before schablonavdrag, no other income.
Expected: Schablonavdrag SEK 225,000. Assessed earned income SEK 675,000, above 7.88 price base amounts, so grundavdrag SEK 17,400. Taxable earned income SEK 657,600, which exceeds SEK 643,000: statlig skatt 20% × 14,600 = SEK 2,920. Kommunalskatt SEK 212,930.88. Jobbskatteavdrag (above 8.08 price base amounts) = (3.027 × 59,200 − 17,400) × 32.38% = SEK 52,390. Earned income credit SEK 1,500. Income tax SEK 161,960.88.

```oa-check
name: Sole trader born 1980, average rate, net profit SEK 900,000 (2026)
inputs:
  net_profit: 900000
  pbb: 59200
  municipal_rate: 0.3238
  skiktgrans: 643000
steps:
  - schablonavdrag: net_profit * 0.25
  - earned_income: net_profit - schablonavdrag
  - basic_deduction: ceil(0.293 * pbb / 100) * 100
  - taxable_earned: earned_income - basic_deduction
  - municipal_tax: taxable_earned * municipal_rate
  - state_tax: max(taxable_earned - skiktgrans, 0) * 0.20
  - job_credit: floor((3.027 * pbb - basic_deduction) * municipal_rate)
  - income_tax: municipal_tax + state_tax - job_credit - 1500
expected:
  earned_income: 675000.00
  basic_deduction: 17400.00
  taxable_earned: 657600.00
  state_tax: 2920.00
  municipal_tax: 212930.88
  job_credit: 52390.00
  income_tax: 161960.88
```

Input: Sole trader born 1955, net business profit SEK 300,000 before schablonavdrag.
Expected: Born 1938-1958, so only the old-age pension contribution of 10.21% and a 10% schablonavdrag. Schablonavdrag SEK 30,000. Taxable business income SEK 270,000. Egenavgifter 10.21% × 270,000 = SEK 27,567. Grundavdrag and jobbskatteavdrag follow the 66-or-over rules (IL 63 kap. 3 a § and 67 kap. 8 §).

Input: Net business income SEK 500,000, client allocates SEK 200,000 to expansionsfond.
Expected: Expansionsfondsskatt = SEK 200,000 x 20.6% = SEK 41,200. Taxable business income reduced to SEK 300,000.

Input: Client buys office furniture for SEK 20,000 excluding moms, deducts full amount.
Expected: Correct. SEK 20,000 is below half prisbasbelopp (SEK 29,600 for 2026), so the whole cost is deducted at once (IL 18 kap. 4 §), unless it is part of a larger purchase of linked items that together reach SEK 29,600.

Input: Momsregistrerad client reports SEK 1,250,000 gross receipts including 25% moms.
Expected: NE R1 = SEK 1,000,000. Exclude SEK 250,000 moms.

Input: Net business assets (kapitalunderlag) SEK 500,000. Business income SEK 400,000.
Expected: Räntefördelningsbelopp = SEK 42,750 (500,000 x 8.55%, the 2026 rate). Reclassified to capital income (30% tax). Taxable business income = SEK 357,250.

### Edge case registry

EC1 -- Statlig skatt below the skiktgräns. Never apply 20% state tax on taxable earned income up to SEK 643,000 (2026).
EC2 -- Egenavgifter not deducted. Always apply the schablonavdrag: 25%, or 10% if born 1938-1958. Egenavgifter are deductible.
EC3 -- Capital expenditure expensed directly. Assets above half prisbasbelopp with life > 3 years must be depreciated.
EC4 -- Moms included in revenue. For momsregistrerade, R1 = net of moms.
EC5 -- Expansionsfond reversed without taxation. Must be reversed and taxed on cessation.
EC6 -- Jobbskatteavdrag on capital income. Only applies to earned income.
EC7 -- F-skatt not registered. Must register immediately.
EC8 -- Home office: standard + actual combined. Cannot combine -- choose one.
EC9 -- Representation food deducted. External representation food: NOT deductible.
EC10 -- Negative räntefördelning ignored. Mandatory when thresholds exceeded.

### Prohibitions

- NEVER apply statlig inkomstskatt below the brytpunkt
- NEVER forget egenavgifter schablonavdrag deduction
- NEVER include moms in NE-bilaga revenue for momsregistrerade clients
- NEVER expense capital items above half prisbasbelopp with life > 3 years
- NEVER allow external representation food deductions
- NEVER combine standard and actual home office deductions
- NEVER ignore mandatory negative räntefördelning
- NEVER apply jobbskatteavdrag to capital income
- NEVER present calculations as definitive -- always label as estimated
- NEVER advise on international income, 3:12 rules, or complex restructuring -- escalate

### Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), as amended to SFS 2026:1393: 16 kap. 29 §; 18 kap. 4 and 13 §§; 63 kap. 3-3 a §§; 65 kap. 3-5 §§; 67 kap. 6-8, 46-47 §§ | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-23 |
| Socialavgiftslag (2000:980), as amended to SFS 2026:493: 3 kap. 13, 15 and 16 §§; transitional rules 2000:980 point 6, 2022:889 and 2025:1362 | https://data.riksdagen.se/dokument/sfs-2000-980.text | 2026-10-23 |
| Skatteförfarandelag (2011:1244): 32 kap. 1 §; 48 kap. 6-7 §§ | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-23 |
| Mervärdesskattelag (2023:200): 18 kap. 4 § | https://data.riksdagen.se/dokument/sfs-2023-200.text | 2026-10-23 |
| Bokföringslag (1999:1078) | https://data.riksdagen.se/dokument/sfs-1999-1078.text | not re-read |
| Skatteverket, belopp och procent inkomstår 2026 (egenavgifter, schablonavdrag, grundavdrag, skiktgräns, brytpunkt, räntefördelning, expansionsfond, milersättning) | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-23 |
| SCB, kommunala skattesatser 2026 (table OE0101, Kommunalskatter2000) | https://www.statistikdatabasen.scb.se/goto/sv/ssd/Kommunalskatter2000 | 2026-10-23 |

Not yet confirmed: the 66-or-over grundavdrag band table (IL 63 kap. 3 a §) was not worked here, so the born-1955 test stops at egenavgifter; the general 7.5% reduction of egenavgifter is not covered in this skill; the home office standard amounts, representation limits and the ombud filing date in this skill were not re-read for 2026.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an auktoriserad revisor, godkänd revisor, or equivalent licensed practitioner in Sweden) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
