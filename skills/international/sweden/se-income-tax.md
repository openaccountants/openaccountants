---
name: se-income-tax
description: Use this skill whenever asked about Swedish income tax for self-employed individuals (enskild firma / enskild näringsidkare). Trigger on phrases like "Swedish tax", "kommunalskatt", "statlig inkomstskatt", "jobbskatteavdrag", "grundavdrag", "NE-bilaga", "F-skatt", "expansionsfond", "räntefördelning", "Inkomstdeklaration 1", "self-employed tax Sweden", or any question about filing or computing income tax for a Swedish self-employed client. Covers kommunalskatt, statlig inkomstskatt, jobbskatteavdrag, grundavdrag, egenavgifter, F-skatt, expansionsfond, räntefördelning, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Swedish income tax work.
version: 2.0
---

# Sweden Income Tax -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Sweden (Konungariket Sverige) |
| Tax type | Personal income tax on business income (inkomst av näringsverksamhet) |
| Primary legislation | Inkomstskattelagen (IL, 1999:1229) |
| Supporting legislation | Skatteförfarandelagen (SFL, 2011:1244); Socialavgiftslagen (SAL, 2000:980); Bokföringslagen (BFL, 1999:1078) |
| Tax authority | Skatteverket (Swedish Tax Agency) |
| Filing portal | skatteverket.se / Mina sidor |
| Currency | SEK only |
| Return form | Inkomstdeklaration 1 with NE-bilaga (business income attachment) |
| Filing deadline (digital) | 2 May of the following year |
| Filing deadline (via ombud) | 16 June |
| F-skatt instalments | 12th of each month |
| Kommunalskatt (municipal + regional) | Average 32.41% (range 28.98%--35.30%) |
| Statlig inkomstskatt (state tax) | 20% on taxable earned income above SEK 625,800 (under 66); SEK 733,200 (66+) |
| Egenavgifter (self-employment contributions) | 28.97% (full); 10.21% (age 66+) |
| Grundavdrag (basic deduction) | SEK 17,300--45,300 (under 66); up to SEK 86,500 (66+) |
| Jobbskatteavdrag | Tax credit reducing kommunalskatt; approximately SEK 44,000--46,000 for average earners |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Swedish auktoriserad or godkänd revisor sign-off |
| Validation date | Pending |

**Key NE-bilaga fields:**

| Field | Description |
|---|---|
| R1 | Gross revenue (intäkter) |
| R2 | Cost of goods sold |
| R3--R6 | Operating expenses (by category) |
| R7 | Depreciation (avskrivningar) |
| R8 | Other expenses |
| R9 | Net business result (överskudd/underskudd) |
| R14 | Sjukpenninggrundande inkomst (SGI -- sickness benefit base) |
| R24 | Räntefördelning (interest allocation) |
| R33--R35 | Expansionsfond (expansion fund) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown expense category | Not deductible |
| Unknown business-use proportion (phone, car, home office) | 0% business use |
| Unknown whether capital or revenue expenditure | Capital (depreciate, do not expense) |
| Unknown moms treatment | Exclude moms from revenue and costs if momsregistrerad |
| Unknown municipality | Average kommunalskatt 32.41% (flag as estimated) |
| Unknown F-skatt status | Assume not registered (flag immediately) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | SEK 50,000 |
| HIGH tax-delta on a single conservative default | SEK 5,000 |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net tax position | SEK 100,000 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year in CSV, PDF, or pasted text. Must cover 1 January to 31 December. Acceptable from any Swedish bank: Handelsbanken, SEB, Swedbank, Nordea, Danske Bank, Länsförsäkringar, Skandiabanken, or fintech banks (Revolut, Wise, N26).

**Recommended** -- sales invoices for the year, purchase invoices for any expense above SEK 10,000, municipality of residence, NE-bilaga from prior year (for loss carry-forward and räntefördelning basis).

**Ideal** -- complete bookkeeping (verifikationer), balance sheet for räntefördelning/expansionsfond calculations, prior year Inkomstdeklaration 1, F-skatt registration confirmation.

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This NE-bilaga was produced from bank statement alone. The reviewer must verify that expense classifications are correct and that capital items have been properly identified."

### Refusal catalogue

**R-SE-1 -- Aktiebolag (AB) instead of enskild firma.** *Trigger:* client operates through an AB (limited company). *Message:* "This skill covers enskild firma (sole proprietorship) only. AB taxation follows the corporate income tax rules (22% bolagsskatt) and different filing forms. Please use a separate skill or consult an auktoriserad revisor."

**R-SE-2 -- 3:12 rules (fåmansbolag).** *Trigger:* client has a closely held company and asks about dividend taxation under 3:12 rules. *Message:* "The 3:12 rules for fåmansbolag are outside the scope of this skill. Please consult an auktoriserad revisor."

**R-SE-3 -- International income.** *Trigger:* client has significant foreign-source income or asks about tax treaty application. *Message:* "International income and tax treaty questions are outside this skill's scope. Please consult a qualified tax advisor."

**R-SE-4 -- Handelsbolag / kommanditbolag.** *Trigger:* client operates through a partnership. *Message:* "Partnership taxation has specific rules for income allocation between partners. This skill covers enskild firma only."

---

## Section 3 -- Transaction pattern library (the lookup table)

This is the deterministic pre-classifier for income tax purposes. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific.

### 3.1 Swedish banks (fees and interest -- classify correctly)

| Pattern | Treatment | Notes |
|---|---|---|
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

| Pattern | Treatment | Notes |
|---|---|---|
| SKATTEVERKET, SKV | EXCLUDE | Tax payment (F-skatt, moms, arbetsgivaravgifter) -- not a deductible expense |
| SKATTEKONTO | EXCLUDE | Tax account movement |
| F-SKATT | EXCLUDE | Preliminary tax payment |
| BOLAGSVERKET | Deductible expense | Company registration fees |
| MOMS, MERVÄRDESKATT (payment to SKV) | EXCLUDE | VAT remittance |
| FÖRSÄKRINGSKASSAN | EXCLUDE | Social insurance authority -- benefits or repayments |
| KRONOFOGDEN | NOT deductible | Enforcement fees/fines -- public policy |
| ARBETSFÖRMEDLINGEN | EXCLUDE | Employment agency -- government body |

### 3.3 Swedish utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| VATTENFALL | Deductible if business premises electricity | If home: apportion business % |
| E.ON, FORTUM | Same as above | Electricity supplier |
| STOCKHOLMS STAD, [municipality] KOMMUN (water/waste) | Deductible if business premises | Apportion if home office |
| TELIA, TELENOR, TRE (3), HALEBOP, COMVIQ | Deductible: business phone/internet | If mixed-use: apportion business % |
| BREDBANDSBOLAGET, BAHNHOF | Deductible: business internet | If mixed-use: apportion |

### 3.4 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| LÄNSFÖRSÄKRINGAR, TRYGG-HANSA, IF SKADEFÖRSÄKRING | Deductible if business insurance (professional indemnity, business property) | Personal insurance: NOT deductible |
| FOLKSAM, SKANDIA | Same | Separate business from personal lines |
| PENSIONSFÖRSÄKRING, IPS | EXCLUDE from business | Pension -- separate deduction in inkomst av kapital |

### 3.5 SaaS and software -- international

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
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

| Pattern | Treatment | Notes |
|---|---|---|
| REVISOR, REDOVISNING, BOKFÖRING, ACCOUNTING | Deductible expense (R3--R6) | Accountancy/bookkeeping fees -- always deductible |
| ADVOKAT, JURIST, LAWYER | Deductible expense | If business legal matter |
| NOTARIUS, NOTARY | Deductible expense | If business transaction |
| KONSULT (received from) | REVENUE (R1) | Client paying for consulting services |

### 3.7 Payroll and social contributions (exclude or classify)

| Pattern | Treatment | Notes |
|---|---|---|
| LÖN, SALARY, LÖNEUTBETALNING (outgoing to employees) | Deductible expense (R3--R6) | Staff salary cost |
| ARBETSGIVARAVGIFT (payment to SKV) | Deductible expense | Employer social contributions |
| EGENAVGIFTER (own social contributions) | Deductible via schablonavdrag (25%) | See Section 5, Step 2 |
| FACKAVGIFT, UNIONEN, IF METALL | Deductible expense | Trade union dues for employees |

### 3.8 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| SL, VÄSTTRAFIK, SKÅNETRAFIKEN | Deductible if business travel | Public transport for business trips |
| SJ, MTRX (train) | Deductible if business travel | Document purpose |
| SAS, NORWEGIAN, RYANAIR (flights) | Deductible if business travel | Document purpose and destination |
| TAXI STOCKHOLM, TAXI KURIR, UBER, BOLT | Deductible if business travel | Document purpose |
| OKQ8, CIRCLE K, PREEM, SHELL, ST1 (fuel) | Deductible: business portion only | If private car: SEK 25.00/mil standard rate instead |
| BILPROVNING (vehicle inspection) | Deductible if business vehicle | Private car: include in km-rate |
| PARKERING, APCOA, EASYPARK | Deductible if business purpose | Document occasion |

### 3.9 Office and supplies

| Pattern | Treatment | Notes |
|---|---|---|
| STAPLES, OFFICE DEPOT, CLAS OHLSON | Deductible expense | Office supplies |
| IKEA (business furniture) | Capital if > SEK 5,000; else deductible expense | Check half prisbasbelopp threshold |
| ELGIGANTEN, MEDIAMARKT, KOMPLETT | Capital if > SEK 5,000 and life > 3 years; else deductible | Computer/electronics |
| POSTNORD | Deductible expense | Postage and shipping |
| WEBHALLEN, INET | Capital or expense depending on amount | IT equipment |

### 3.10 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| ICA, COOP, WILLYS, HEMKÖP, LIDL | Default: NOT deductible (personal provisioning) | Only deductible if hospitality/catering business |
| RESTAURANT, RESTAURANG (any named restaurant) | NOT deductible: external representation food | SEK 0 deduction for external meals |
| INTERN REPRESENTATION | Deductible up to SEK 300/person/event | Internal events only; enklare förtäring |

### 3.11 Rent and property

| Pattern | Treatment | Notes |
|---|---|---|
| HYRA, HYRESVÄRD, [landlord name] (monthly rent) | Deductible if dedicated business premises | Home office: use proportional or SEK 2,000 standard |
| HEMFÖRSÄKRING (home insurance) | NOT deductible unless home office proportion | Apportion if home office claimed |
| BOSTADSRÄTTSFÖRENING, BRF | NOT deductible unless home office proportion | Monthly fee for housing cooperative |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| EGEN ÖVERFÖRING, OWN TRANSFER, INTERNAL | EXCLUDE | Internal account movement |
| EGET UTTAG, EGNA UTTAG, DRAWINGS | EXCLUDE | Owner drawings -- not an expense |
| INSÄTTNING, OWN DEPOSIT | EXCLUDE | Owner capital injection |
| UTDELNING, DIVIDEND | EXCLUDE | Dividend (capital income, not business) |
| SPARANDE, SAVINGS | EXCLUDE | Transfer to savings |

---

## Section 4 -- Worked examples

These are four fully worked income tax classifications drawn from a hypothetical Swedish enskild firma IT consultant.

### Example 1 -- SaaS subscription (reverse charge moms interaction)

**Input line:**
`2025-03-15 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Workspace ; -1,200.00 SEK`

**Reasoning:**
Google Ireland Ltd is an EU entity (Section 3.5). The consultant is momsregistrerad. Reverse charge moms applies -- the consultant reports output moms and claims input moms on the momsdeklaration (net zero). For income tax purposes, the expense is deductible at the net amount (SEK 1,200). Moms is NOT included in R1 revenue or expense costs.

**Classification:** Deductible business expense, R3--R6 (software/IT). Amount: SEK 1,200.

### Example 2 -- Capital equipment above threshold

**Input line:**
`2025-06-20 ; ELGIGANTEN ; DEBIT ; MacBook Pro 14" ; -22,990.00 SEK`

**Reasoning:**
SEK 22,990 exceeds half prisbasbelopp (approximately SEK 5,000 in 2025) and the asset has a useful life over 3 years. Must enter the inventarier pool as a capital asset. Not directly expensed. Depreciation year 1 = 30% of SEK 22,990 = SEK 6,897 (räkenskapsenlig avskrivning).

**Classification:** Capital asset (inventarier pool). R7 depreciation = SEK 6,897. Do NOT put SEK 22,990 in R3--R6.

### Example 3 -- External restaurant meal (not deductible)

**Input line:**
`2025-09-10 ; RESTAURANG PELIKAN STOCKHOLM ; DEBIT ; Client dinner ; -2,400.00 SEK`

**Reasoning:**
External representation food costs are NOT deductible for income tax in Sweden. Only simpler refreshments (enklare förtäring) at internal events are deductible up to SEK 300/person. This is a client dinner -- zero deduction regardless of business purpose.

**Classification:** NOT deductible. Exclude from R3--R6 expenses entirely.

### Example 4 -- Home office standard deduction

**Input line:**
(No single bank line -- client claims home office)

**Reasoning:**
The client can choose either the standard deduction of SEK 2,000/year or actual costs proportional to floor area. Cannot combine both. If actual costs exceed SEK 2,000 and the client has a dedicated room, actual method may be better but requires documentation.

**Classification:** R3--R6 expense, SEK 2,000 (standard deduction). Flag for reviewer if actual costs are claimed instead.

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Kommunalskatt computation

Applied to taxable earned income (beskattningsbar förvärvsinkomst) at the municipality rate. If municipality unknown, use 32.41%. Range: 28.98% (Österåker) to 35.30% (Degerfors). **Legislation:** IL kap. 65.

### 5.2 Egenavgifter and schablonavdrag

Egenavgifter = 28.97% of net business profit (10.21% for age 66+). Since egenavgifter are calculated on the profit they reduce, apply schablonavdrag of 25% as preliminary deduction from net business profit. Actual egenavgifter reconciled on the return. **Legislation:** SAL.

**Computation:** (1) Net profit before egenavgifter = X. (2) Schablonavdrag = X x 25% = Y. (3) Taxable business income = X - Y. (4) Actual egenavgifter computed on final adjusted base.

### 5.3 Statlig inkomstskatt

20% on taxable earned income above SEK 625,800 (under 66) or SEK 733,200 (66+). Below the brytpunkt: 0% state tax. **Legislation:** IL kap. 65.

### 5.4 Grundavdrag

Income-dependent basic deduction. Minimum SEK 17,300, maximum SEK 45,300 (under 66); up to SEK 86,500 (66+). Computed automatically by Skatteverket. Reduces taxable earned income before both kommunalskatt and statlig skatt. **Legislation:** IL kap. 63.

### 5.5 Capital expenditure threshold

Assets above half prisbasbelopp (approximately SEK 5,000) with useful life over 3 years: must enter inventarier pool and depreciate. Assets below or with life under 3 years: expense immediately (direktavdrag). **Legislation:** IL kap. 18.

### 5.6 Depreciation rates

Inventarier (machinery, equipment): 30% declining balance (räkenskapsenlig avskrivning) or 20% straight-line (supplementary rule). Buildings: 2--5% straight-line. Goodwill: pooled with inventarier at 30%. **Legislation:** IL kap. 18, 19, 20.

### 5.7 Motor vehicle standard rate

SEK 25.00/mil (2025) for business travel using a private car. Alternative: actual costs with logbook apportionment. **Legislation:** IL kap. 16.

### 5.8 Home office deduction

Standard deduction: SEK 2,000/year (no documentation required). Alternative: actual proportional costs (requires floor area calculation and dedicated room). Cannot combine both methods. **Legislation:** IL kap. 16.

### 5.9 Representation

Internal: up to SEK 300/person/event for enklare förtäring. External: food costs NOT deductible for income tax (even if limited moms deduction applies). **Legislation:** IL kap. 16.

### 5.10 Moms interaction

Moms collected on sales: NOT income (exclude from R1). Input moms recovered: NOT an expense (exclude from costs). Non-deductible moms (e.g., representation): IS an expense. Non-momsregistrerad (under SEK 80,000 turnover): no moms separation needed, gross = net. **Legislation:** ML.

### 5.11 F-skatt

All self-employed must register for F-skatt. Monthly instalments due 12th of each month. Without F-skatt, clients paying the individual must pay arbetsgivaravgifter. **Legislation:** SFL kap. 55.

### 5.12 Loss carry-forward

Business losses (underskudd) carry forward to future years within the same income category (näringsverksamhet). No time limit on carry-forward. **Legislation:** IL kap. 40.

### 5.13 Record keeping

Minimum retention: 7 years from end of calendar year. Must follow god redovisningssed. Digital or paper permitted. **Legislation:** BFL.

---

## Section 6 -- Tier 2 catalogue (reviewer judgement required)

### 6.1 Jobbskatteavdrag computation

*Why ambiguous:* Complex formula based on earned income, kommunalskatt rate, and age. *Default:* Do not compute manually -- flag for reviewer or use Skatteverket's calculator. *Question:* "What is your municipality of residence? (Required for precise jobbskatteavdrag.)"

### 6.2 Expansionsfond allocation

*Why ambiguous:* Requires accurate kapitalunderlag using SKV 2196. 20.6% tax on allocation, deferred until reversal. Maximum limited by net business assets. *Default:* Do not allocate without reviewer confirmation. *Question:* "Do you want to allocate profit to expansionsfond? If so, provide your net business assets (kapitalunderlag) calculation."

### 6.3 Räntefördelning

*Why ambiguous:* Positive räntefördelning reclassifies business income as capital income (30% tax). Requires net business assets > SEK 50,000. Rate: 2.96% (statslåneräntan + 6pp). *Default:* Do not apply without reviewer confirmation. *Question:* "What were your net business assets at the start of the income year?"

### 6.4 Mixed-use phone/internet

*Why insufficient:* Business proportion unknown from bank statement alone. *Default:* 0% business use. *Question:* "Is this a dedicated business line or mixed-use? What percentage is business?"

### 6.5 Motor vehicle documentation

*Why insufficient:* Business km unknown. *Default:* Use standard rate SEK 25.00/mil only with documented business km. *Question:* "Do you have a logbook showing business vs private km?"

### 6.6 Home office -- actual vs standard

*Why ambiguous:* Choice of method affects deduction amount. *Default:* SEK 2,000 standard deduction. *Question:* "Do you have a dedicated room exclusively for business? What is its proportion of total floor area?"

### 6.7 Negative räntefördelning

*Why ambiguous:* Mandatory if business capital deficit exceeds SEK 500,000 change during year. Reclassifies capital income as business income. *Default:* Flag for reviewer. *Question:* "Has your business capital changed by more than SEK 500,000 during the year?"

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"

| Column | Content |
|---|---|
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

| Row | Field | Formula |
|---|---|---|
| R1 | Gross revenue | =SUMIFS(Transactions!F:F, Transactions!E:E, "R1") |
| R2 | Cost of goods sold | =SUMIFS(Transactions!F:F, Transactions!E:E, "R2") |
| R3-R6 | Operating expenses | =SUMIFS(Transactions!F:F, Transactions!E:E, "R3-R6") |
| R7 | Depreciation | =SUMIFS(Transactions!F:F, Transactions!E:E, "R7") |
| R9 | Net result | =R1-R2-R3_R6-R7 |

### Sheet "Tax Computation"

| Step | Description | Formula |
|---|---|---|
| 1 | Net business profit (R9) | From NE-bilaga |
| 2 | Schablonavdrag (25%) | =Step1 * 0.25 |
| 3 | Taxable business income | =Step1 - Step2 |
| 4 | Grundavdrag | Manual entry (income-dependent) |
| 5 | Beskattningsbar förvärvsinkomst | =Step3 - Step4 |
| 6 | Kommunalskatt | =Step5 * [rate] |
| 7 | Statlig skatt | =MAX(0, (Step5 - 625800) * 0.20) |
| 8 | Jobbskatteavdrag | Manual entry (complex formula) |
| 9 | Estimated tax | =Step6 + Step7 - Step8 |
| 10 | Egenavgifter | =Step3 * 0.2897 |

---

## Section 8 -- Bank statement reading guide

**CSV format conventions.** Handelsbanken exports use semicolon delimiters with YYYY-MM-DD dates. SEB exports use comma or tab delimiters. Swedbank exports typically use semicolons with DD/MM/YYYY dates -- confirm format. Common columns: Datum (Date), Text (Description), Belopp (Amount), Saldo (Balance).

**Swedish language variants.** Common descriptions: lön (salary), hyra (rent), ränta (interest), avgift (fee), köp (purchase), insättning (deposit), uttag (withdrawal), överföring (transfer), faktura (invoice), betalning (payment).

**Internal transfers and exclusions.** Own-account transfers between the client's Handelsbanken, SEB, Swedbank accounts. Labelled "egen överföring", "överföring mellan konton", "sparande". Always exclude.

**Moms interaction.** If client is momsregistrerad, bank statement amounts include moms. For income tax, expenses should be recorded net of recoverable moms. If moms is not recoverable (blocked categories), include gross amount.

**F-skatt payments.** Monthly payments to Skatteverket labelled "F-skatt" or "skattekonto". These are tax payments, NOT business expenses. Always exclude.

**Egenavgifter.** Self-employment contributions are not visible as separate bank transactions -- they are computed on the return. Do not look for them in the bank statement.

**Foreign currency.** Convert to SEK at the transaction date rate. Use Riksbanken's daily exchange rates.

**Cryptic card purchases.** Swedish bank statements often show merchant category codes or abbreviated names. If the counterparty cannot be identified, ask the client.

---

## Section 9 -- Onboarding fallback (only when inference fails)

### 9.1 Business form
*Inference:* Account holder name matching a personal name = enskild firma. "AB" suffix = aktiebolag (refuse via R-SE-1). *Fallback:* "Are you an enskild firma (sole trader) or operating through a company?"

### 9.2 Municipality
*Inference:* Address on bank statement or prior correspondence. *Fallback:* "Which municipality do you live in? (Determines your kommunalskatt rate.)"

### 9.3 F-skatt status
*Inference:* Presence of F-skatt payments in bank statement. *Fallback:* "Are you registered for F-skatt?"

### 9.4 Moms registration
*Inference:* Moms payments to Skatteverket in bank statement. *Fallback:* "Are you momsregistrerad (VAT registered)?"

### 9.5 Age
*Inference:* Not inferable from bank statement. Always ask if relevant to tax computation. *Fallback:* "What is your age at the start of the income year? (Affects grundavdrag, egenavgifter rate, and brytpunkt.)"

### 9.6 Industry
*Inference:* Counterparty mix, invoice descriptions. *Fallback:* "In one sentence, what does your business do?"

### 9.7 Prior year losses
*Inference:* Not inferable from single-year statement. *Fallback:* "Do you have any losses carried forward from prior years (underskudd)?"

### 9.8 Net business assets
*Inference:* Not inferable from bank statement alone. *Fallback:* "What were your net business assets at the start of the year? (Required for räntefördelning and expansionsfond.)"

### 9.9 Other income
*Inference:* Employment income visible as salary credits. *Fallback:* "Do you have other income sources -- employment, rental, capital gains?"

### 9.10 Expansionsfond / räntefördelning elections
*Inference:* Not inferable. *Fallback:* "Do you want to allocate to expansionsfond or apply räntefördelning? (Requires separate computation.)"

---

## Section 10 -- Reference material

### Test suite

**Test 1 -- Standard self-employed, mid-range income.**
*Input:* Enskild firma, Stockholm (kommunalskatt 30.44%), born 1985, gross revenue SEK 800,000, allowable expenses SEK 200,000, no expansionsfond or räntefördelning.
*Expected:* Net profit = SEK 600,000. Schablonavdrag = SEK 150,000. Taxable business income = SEK 450,000. Grundavdrag ~SEK 17,300. Beskattningsbar = SEK 432,700. Below brytpunkt: no statlig skatt. Kommunalskatt = ~SEK 131,714. Less jobbskatteavdrag. Plus egenavgifter (28.97% on adjusted base).

**Test 2 -- High income, statlig skatt applies.**
*Input:* Kommunalskatt 32.41%, born 1980, net business income SEK 900,000.
*Expected:* After schablonavdrag and grundavdrag, taxable earned income exceeds SEK 625,800. Statlig skatt at 20% on the excess.

**Test 3 -- Expansionsfond allocation.**
*Input:* Net business income SEK 500,000, client allocates SEK 200,000 to expansionsfond.
*Expected:* Expansionsfondsskatt = SEK 200,000 x 20.6% = SEK 41,200. Taxable business income reduced to SEK 300,000.

**Test 4 -- Capital item expensed incorrectly.**
*Input:* Client buys office furniture for SEK 20,000, deducts full amount.
*Expected:* Above threshold, life > 3 years. Inventarier pool. Depreciation = SEK 6,000 year 1. Correct: remove SEK 20,000 from expenses, add SEK 6,000 depreciation.

**Test 5 -- Moms included in revenue.**
*Input:* Momsregistrerad client reports SEK 1,250,000 gross receipts including 25% moms.
*Expected:* NE R1 = SEK 1,000,000. Exclude SEK 250,000 moms.

**Test 6 -- Räntefördelning.**
*Input:* Net business assets SEK 500,000. Business income SEK 400,000.
*Expected:* Räntefördelningsbelopp = SEK 14,800 (500,000 x 2.96%). Reclassified to capital income (30% tax). Taxable business income = SEK 385,200.

### Edge case registry

**EC1 -- Statlig skatt below brytpunkt.** Never apply 20% state tax on income below SEK 625,800.
**EC2 -- Egenavgifter not deducted.** Always apply 25% schablonavdrag. Egenavgifter are deductible.
**EC3 -- Capital expenditure expensed directly.** Assets above half prisbasbelopp with life > 3 years must be depreciated.
**EC4 -- Moms included in revenue.** For momsregistrerade, R1 = net of moms.
**EC5 -- Expansionsfond reversed without taxation.** Must be reversed and taxed on cessation.
**EC6 -- Jobbskatteavdrag on capital income.** Only applies to earned income.
**EC7 -- F-skatt not registered.** Must register immediately.
**EC8 -- Home office: standard + actual combined.** Cannot combine -- choose one.
**EC9 -- Representation food deducted.** External representation food: NOT deductible.
**EC10 -- Negative räntefördelning ignored.** Mandatory when thresholds exceeded.

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

1. Inkomstskattelagen (IL, 1999:1229) -- https://www.riksdagen.se
2. Skatteförfarandelagen (SFL, 2011:1244)
3. Socialavgiftslagen (SAL, 2000:980)
4. Bokföringslagen (BFL, 1999:1078)
5. Skatteverket guidance -- https://www.skatteverket.se

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an auktoriserad revisor, godkänd revisor, or equivalent licensed practitioner in Sweden) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
