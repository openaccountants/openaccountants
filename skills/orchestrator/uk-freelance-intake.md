---
name: uk-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their UK tax returns AND mentions freelancing, self-employment, sole trading, contracting, or side hustle income. Trigger on phrases like "help me do my UK taxes", "prepare my self-assessment", "I'm self-employed in the UK", "I'm a sole trader", "do my SA100", "prepare my tax return", or any similar phrasing where the user is a UK-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the UK self-employed tax workflow -- every other skill in the stack (uk-vat-return, uk-self-employment-sa103, uk-income-tax-sa100, uk-national-insurance, uk-student-loan-repayment, uk-payments-on-account, uk-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. UK full-year residents only; sole traders.
version: 0.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK sole trader tax intake (Self Assessment)

The intake an assistant runs before any UK Self Assessment work for a self-employed person: the scope questions, the document checklist, what to read out of each document, the gap questions, and the hand-off to the other UK Guides. It is for sole traders who were UK resident for the whole tax year. This Guide computes no tax. The few figures it carries are limits that decide a route: whether a return is needed, which VAT regime applies, whether Making Tax Digital for Income Tax has started, and which expense method the client is on. Figures are for tax year 2026. In the UK that means 6 April 2026 to 5 April 2027, which HMRC writes "2026 to 2027" and this Guide writes 2026-27. The Making Tax Digital table tests earlier years, and each row names its year. For an earlier return the workflow is the same, but read the year beside each number on the linked page: several figures changed on 6 April 2026.

## What this file is

The intake orchestrator for UK-resident sole traders. Every downstream UK Guide (`uk-vat-return`, `uk-self-employment-sa103`, `uk-income-tax-sa100`, `uk-national-insurance`, `uk-student-loan-repayment`, `uk-payments-on-account`) and the assembly orchestrator (`uk-return-assembly`) depends on this Guide running first. It collects the facts, parses the documents, confirms them with the user, and hands a clean package to `uk-return-assembly`.

## Design principles

v0.1 follows the upload-first, inference-then-confirm pattern of `mt-freelance-intake` v0.1:

1. **Compact refusal sweep** using `ask_user_input_v0`: 3 to 5 questions, about 30 seconds.
2. **Upload-first**: after the refusal check, the user dumps everything they have.
3. **Inference pass**: parse every document and extract what you can.
4. **Gap-filling only**: ask ONLY about what is missing, ambiguous, or needs confirming.
5. **Single confirmation pass**: show the picture, let the user correct it, hand off.

Target: about 10 minutes for a prepared user, 15 to 25 for one who has to fetch documents.

## Critical operating principles

- **Do not narrate the workflow.** No "Phase 1" or "Now I'll ask about deductions." Just do the work.
- **Do not ask what has been answered**, and do not ask about what the documents show. If the bank statement shows quarterly VAT payments to HMRC, confirm registration rather than asking for it.
- **Use `ask_user_input_v0` for any multiple-choice question.** With no such tool, ask the same questions as one numbered list in one message, 3 at a time.
- **Be terse but complete.** No hedging, no "let me know if you have questions."
- **Blocking decisions stand alone.** If one question decides scope, ask it by itself.
- **Do not decide what only HMRC or a tribunal can decide.** Employment status, trade or hobby, and residence are recorded as stated, tested against Section 2, and flagged. Never settled silently.

## Section 1: The opening

One message: a one-line greeting, a one-line summary of the flow (scope check, upload, gaps, hand-off), a one-line reviewer reminder, and the tax year being prepared. Then call `ask_user_input_v0` with the refusal questions.

Let's get your UK Self Assessment return ready. Which tax year are you preparing? The UK tax year runs 6 April to 5 April, so "2026-27" means 6 April 2026 to 5 April 2027. Quick scope check, then you upload, then I fill the gaps. Target: 10 minutes.

Reminder: everything I produce must be reviewed and signed off by a chartered accountant or licensed tax adviser before you file anything with HMRC. I'm not a substitute for professional review.

**Do NOT** write a welcome paragraph, explain the phases, ask "are you ready to start", list documents in advance, or add any disclaimer beyond the one reviewer line.

## Section 2: Refusal sweep (compact)

One `ask_user_input_v0` call with 4 single-select questions.

| Question | Options |
| --- | --- |
| Q1: "UK resident for the whole tax year you are preparing?" | ["Full year UK resident", "Part year: I arrived or left", "Non-resident", "Not sure"] |
| Q2: "Business structure?" | ["Sole trader", "Limited company (Ltd)", "LLP or partnership", "Not sure"] |
| Q3: "VAT registered?" | ["Yes, standard", "Yes, Flat Rate Scheme", "Not registered", "Not sure"] |
| Q4: "Employees?" | ["No employees", "1 to 5 employees", "More than 5 employees"] |

**Evaluation logic.**

- Q1. Full year: continue. Part year or non-resident: stop (refusal below). Not sure: walk through the residence tests below, record the answer as stated, set `classification.residence_tested` to `false` and flag it.
- Q2. Sole trader: continue. Ltd, LLP or partnership: stop. Not sure: "Invoice in your own name and report the income on your personal return? Sole trader. Registered at Companies House? Ltd. Sharing profits with partners? Partnership." A partner running a separate sole trade stays in scope for it, with a flag: the partnership files its own return.
- Q3. Standard: continue. Flat Rate Scheme: continue with a flag; the sector rate and goods costs are needed for the limited cost test below. Not registered: continue with a flag, and test turnover against the registration limit once documents are in. Not sure: "Invoices show VAT and a VAT number?" If unsettled, set `taxpayer.vat_status` to `unsettled`, ask for turnover in Section 6, and flag it.
- Q4. None: continue. 1 to 5: continue with a flag; PAYE is out of scope, route payroll to `uk-payroll`. More than 5: stop.

**Refusals.**

- **Part year or non-resident.** I'm set up for full-year UK residents only. Part-year and non-residents have split-year treatment or different sourcing rules. You need a chartered accountant who handles non-resident returns.
- **Limited company.** I don't cover corporate returns. Limited companies file CT600 returns with separate rules for directors' salaries and dividends. You need a chartered accountant.
- **LLP or partnership.** Partnerships file SA800 returns with profit-sharing arrangements. You need a chartered accountant familiar with partnership returns.
- **More than 5 employees.** I'm set up for sole operators. Above 5 employees the PAYE and employment law work needs a dedicated accountant.

### Residence is recorded, then tested

Residence follows the statutory residence test, not where the client feels they live. A person is UK resident if they meet one or more of the automatic UK tests or the sufficient ties test, and none of the automatic overseas tests. The automatic UK tests include 183 or more days in the UK in the tax year; an only home in the UK for 91 days or more in a row, visited or stayed in for at least 30 days of the tax year; and full-time work in the UK for any period of 365 days where at least one day of that period falls in the tax year being checked. The overseas tests include fewer than 16 days in the UK, or 46 days if not UK resident for the 3 previous tax years: https://www.gov.uk/tax-foreign-income/residence. Route real doubt to `uk-statutory-residence-test`. Someone who moved in or out is usually split into a non-resident part and a resident part. That is out of scope.

### Employee or self-employed: what HMRC looks at

HMRC may regard someone as self-employed for tax even if employment law says otherwise, so ask about the work, not the job title. Someone is probably self-employed if most of these are true: they bid or quote for work; they are not under direct supervision; they invoice for work done; they pay their own National Insurance and tax; they get no holiday or sick pay; and their contract uses terms like self-employed, consultant or independent contractor. Someone can be employed and self-employed at the same time: https://www.gov.uk/employment-status/selfemployed-contractor. If the answers point the other way (one client, set hours, supervised work, equipment supplied, holiday pay), record it, set `classification.employment_status_tested` to `false` and flag it. Do not reclassify the income. Construction work may fall inside the Construction Industry Scheme: see Section 4.

### Trade or hobby: the badges of trade

An activity that may not be a trade is tested against the badges of trade: profit-seeking motive; number of transactions; nature of the asset; existence of similar trading transactions or interests; changes to the asset; the way the sale was carried out; source of finance; interval of time between purchase and sale; and method of acquisition. The courts decide "on the basis of the overall impression gained from a review of all the badges": https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim20205. Record the client's description, which badges point which way, and a flag. Do not rule on it here.

### Does the client need a Self Assessment return at all

| Test | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return |
| Sole trader income above which a return must be sent, before expenses | GBP 1,000 | "you were self-employed as a ‘sole trader’ and earned more than £1,000" |

A client who has never sent a return, or registered before but did not need to send one, must tell HMRC by 5 October after the end of the tax year (same page).

| Allowance | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income |
| Trading allowance: gross trading income that can be received tax free, each tax year | GBP 1,000 | "You can get up to £1,000 each tax year in tax-free allowances" |
| Property allowance, separate from the trading allowance | GBP 1,000 | "If you have both types of income, you’ll get a £1,000 allowance for each." |

The trading allowance is an allowance, not a cliff. Above it, the allowance may be deducted INSTEAD of actual expenses, never as well, so record gross income and actual expenses both and let `uk-self-employment-sa103` choose. Route property income to `uk-rental-sa105`. Neither allowance can be used in a tax year if the client has any trade or property income from a company they or a connected person owns or controls, from a partnership where they or a connected person are partners, or from their own employer or the employer of their spouse or civil partner. The trading allowance also does not apply to trading income from a partnership: https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income.

### VAT: which regime, and the limits that decide it

| Limit | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/how-vat-works/vat-thresholds |
| Registration: taxable turnover above this makes registration compulsory | GBP 90,000 | "Total taxable turnover More than £90,000 Register for VAT" |
| Deregistration: a registered business may cancel below this | GBP 88,000 | "Less than £88,000 Cancel VAT registration" |
| Flat Rate Scheme: turnover at or below this to join | GBP 150,000 | "Flat Rate Scheme £150,000 or less" |
| Flat Rate Scheme: above this the business must leave | GBP 230,000 | "£150,000 or less More than £230,000" |

Registration is compulsory if EITHER test is met: taxable turnover for the last 12 months goes over the limit, or the client expects taxable turnover to go over it in the next 30 days on its own. The 12 month test is rolling, not the tax year: https://www.gov.uk/register-for-vat. The Flat Rate Scheme joining and leaving limits differ, so a business above the joining limit can still be in the scheme. They are also measured differently: the joining limit is turnover excluding VAT, the leaving limit is total business income including VAT. Deregistration is optional. The intake records turnover and dates; `uk-vat-return` decides the return.

A Flat Rate Scheme "limited cost business" pays one fixed rate whatever its trade.

| Test | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay |
| Flat rate for a limited cost business, whatever the sector | 16.5% | "This means you pay a higher rate of 16.5%." |
| Limited cost test: goods cost less than this share of turnover | 2% | "if your goods cost less than either: 2% of your turnover" |
| Limited cost test: or goods cost less than this in a year | GBP 1,000 | "£1,000 a year (if your costs are more than 2%)" |
| Reduction of the sector rate in the first year of VAT registration | 1% | "You get a 1% discount if you’re in your first year" |

The page joins the two tests with "either", so meeting one is enough. Goods are counted including VAT and must be used exclusively for the business. They do not include capital goods of any value, vehicle costs including fuel outside the transport sector, food or drink for the client or their staff, or goods bought for resale where that is not the main activity. For a return period shorter than a year the yearly limb is the matching proportion: VAT Notice 733 paragraph 4.4, https://www.gov.uk/government/publications/vat-notice-733-flat-rate-scheme-for-small-businesses/vat-notice-733-flat-rate-scheme-for-small-businesses. Ask a Flat Rate Scheme client for the cost of goods (not services) in the period and the date of first VAT registration.

### Making Tax Digital for Income Tax: who must join, and when

Settle this at intake, because it changes what the client must keep. Qualifying income is total self-employment and property income before expenses (turnover), based on the return submitted in the previous tax year. Employment income, a partnership profit share, dividends, the State Pension and private pensions do not count: https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax.

| Qualifying income over, in the year tested | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax |
| 2024 to 2025: should have started from 6 April 2026 | GBP 50,000 | "£50,000 for the 2024 to 2025 tax year, you should’ve started" |
| 2025 to 2026: start 6 April 2027 | GBP 30,000 | "£30,000 for the 2025 to 2026 tax year, you will need to use it from 6 April 2027" |
| 2026 to 2027: start 6 April 2028 | GBP 20,000 | "£20,000 for the 2026 to 2027 tax year, you will need to use it from 6 April 2028" |

Each row is tested on an EARLIER tax year than the one it starts in. The test is on gross income, so a client with a small profit can be caught. For a sole trader who traded for only part of the tested year HMRC annualises the figure, so a first part year of trading can carry a client over: https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax. It applies to a sole trader or landlord registered for Self Assessment; partnerships will join later, on a timeline not yet set. Inside it, the client keeps digital records and sends quarterly updates through software: https://www.gov.uk/guidance/using-making-tax-digital-for-income-tax. A Self Assessment return is still due for the tax year before the client starts, and inside the regime the yearly return is completed and submitted through the same software: https://www.gov.uk/guidance/using-making-tax-digital-for-income-tax. Some people are exempt, for example if digitally excluded. HMRC writes to those above the threshold; test it from the return anyway.

## Section 3: The dump

Once the sweep passes, ask for the documents. Single message. No preamble.

Scope is good. Now upload everything you have for the tax year you are preparing (6 April to the following 5 April). Drop it all in at once:

- Business bank statements for the full tax year (CSV or PDF)
- Sales invoices issued in the tax year
- Purchase invoices and receipts for business expenses
- Prior year SA302 (tax calculation) or the prior year return
- P60 or payslips (if you also have employment income)
- Student loan statement (if applicable)
- VAT returns filed during the tax year (if VAT registered)
- HMRC letters and payment statements, including any Making Tax Digital letter
- Receipts for equipment, computers and vehicles
- Anything else tax-related

Don't worry about labels. I'll work out what each file is.

Then wait. Ask nothing else. If the user says "that's what I have", move to inference and ask for specific missing items during gap-filling. If the user says "I don't know what I have", point them to: the business bank; email (search "invoice", "HMRC", "tax return", "P60", "student loan"); their HMRC online account; last year's accountant; cloud folders of saved invoices; and the Student Loans Company portal.

### Records the client must keep

A sole trader keeps records of business income and expenses, and of personal income too: https://www.gov.uk/self-employed-records. From the 2024 to 2025 tax year cash basis is the default, and traditional accounting needs an opt-out (same page).

Records are kept for at least 5 years after the 31 January submission deadline of the relevant tax year: https://www.gov.uk/self-employed-records/how-long-to-keep-your-records. If records were lost, stolen or destroyed, the client must still give figures and tell HMRC on the return which are estimated or provisional. Flag it.

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/1970/9/section/12B |
| Maximum penalty for failing to keep or preserve the required records. A maximum, not a fixed charge | GBP 3,000 | "shall be liable to a penalty not exceeding £3,000." |

## Section 4: The inference pass

Parse each document, extract the facts, and build an internal inference object. Do not show it raw. Turn it into the Section 5 summary.

- **Bank statements**: total deposits (candidate gross turnover); recurring inflows by client; HMRC payments for Self Assessment and VAT, dated; supplier outflows by category; equipment purchases; drawings; rent; software; memberships; insurance; telephone/broadband; motor costs.
- **Sales invoices**: client names and amounts; VAT charged or not; turnover reconciled to deposits; non-UK clients (reverse charge or outside UK VAT scope); Construction Industry Scheme deductions, already-suffered tax that goes into the return.
- **Purchase invoices and receipts**: category (revenue, capital, disallowable); VAT on each; capital items; disallowable items such as entertainment.
- **Prior year SA302 or return**: total liability; net self-employment income; GROSS self-employment and property income for the MTD test; capital allowances schedule; payments on account made; balancing payment or refund; tax collected outside Self Assessment.
- **P60 and payslips**: gross pay; PAYE tax; Class 1 NI; tax code; student loan deductions.
- **Student loan statement**: plan type (Plan 1, 2, 4, 5 or Postgraduate); balance; PAYE repayments. Thresholds belong to `uk-student-loan-repayment`.
- **VAT returns**: turnover and output tax per period; input tax claimed; flat rate percentage used; amount owed or refunded.

### Payments on account: the two tests that switch them off

| Test | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/understand-self-assessment-bill/payments-on-account |
| None due if last year's tax owed was below this. A cliff | GBP 1,000 | "the amount of tax you owed last year was less than £1,000" |
| None due if more than this share of last year's tax was paid outside Self Assessment, for example through a tax code | 80% | "you paid more than 80% of the tax you owed outside of Self Assessment" |
| Size of each instalment | half of the previous year's tax | "Each payment is half of the tax you owed last year." |

Either test switches the instalments off. They are due by 31 January and 31 July. Read both inputs from the prior year documents; `uk-payments-on-account` does the calculation.

## Section 5: The confirmation

Present one compact summary and invite corrections. Fill every line from the documents. Write "not found" where no document carried it. Never invent a figure, and never copy an amount from this Guide into a client summary.

Here's what I pulled from your documents. Skim and tell me what's wrong.

- **Identity:** name, marital status; residence as stated and whether tested; the trade; VAT regime and number.
- **Turnover:** gross turnover excluding VAT; one line per client; VAT collected; non-UK income separately; Construction Industry Scheme deductions suffered.
- **Expenses:** one line per category; each mixed item marked "need business use share"; each capital item with date and cost; input VAT.
- **Employment income (P60):** gross pay, PAYE tax, Class 1 National Insurance.
- **Student loan:** plan type and the amount repaid through PAYE.
- **Payments on account:** each instalment with its date, and the total.
- **Prior year (SA302):** total liability, net profit, and gross self-employment and property income.
- **VAT returns:** periods filed and periods outstanding.
- **Making Tax Digital:** already in, must join (from when), or below the test.

**Flags I already see:** numbered. Typical: a mixed cost with no business share; a vehicle with no chosen method; a capital item; an outstanding VAT period; employment income needing the employment pages; a classification recorded but not settled.

**Is any of this wrong? Reply "looks good" or tell me what to fix.**

## Section 6: Gap filling

After the user confirms, ask only what the documents cannot show, with `ask_user_input_v0` where possible: Scottish taxpayer status; simplified expenses for vehicles, home or premises; accounting basis; student loan plan type; capital allowances brought forward; Marriage Allowance; pension contributions; and the earlier year's gross income for Making Tax Digital if the prior return is missing.

**Scottish taxpayer.** Q: "Scottish taxpayer?" Options: ["Yes, I live in Scotland", "No, England, Wales or Northern Ireland", "Not sure"]. Scottish Income Tax applies to wages, pension and most other taxable income; dividends and savings interest are taxed as in the rest of the UK: https://www.gov.uk/scottish-income-tax. You pay it if you live in Scotland; a mover, someone with homes in and outside Scotland, or with no home, needs https://www.gov.uk/scottish-income-tax/who-pays. Record the answer; `uk-income-tax-sa100` applies the rates.

**Motor vehicle method.** Q: "Motor vehicle expenses method?" Options: ["Simplified expenses, a flat rate per mile", "Actual costs, with a business use share", "No vehicle used for business"]. Simplified: ask vehicle type and business miles. Actual: ask total miles, business miles and total costs, and record the share the client states.

| Vehicle | Flat rate per mile | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles |
| Cars and goods vehicles, first 10,000 business miles | 55p per mile | "first 10,000 miles 55p" |
| Cars and goods vehicles, after 10,000 miles | 25p per mile | "after 10,000 miles 25p" |
| Motorcycles | 24p per mile | "Motorcycles 24p" |

The first rate ROSE for 2026-27; the page shows the lower rate for before 6 April 2026. Once the flat rate is used for a vehicle it must be used for as long as that vehicle is used in the business. These are the self-employed rates. Simplified expenses cover cars, goods vehicles such as vans, and motorcycles, but not a car designed for commercial use such as a black cab, a hackney carriage or a dual control driving instructor's car, and not a vehicle already claimed as capital allowances or already put through as an expense. The mileage allowance an employer pays an employee is a different rule with the same numbers; do not mix them.

**Use of home.** Q: "Use of home for business?" Options: ["Simplified flat rate by hours worked at home", "Actual costs apportionment", "Separate business premises", "No home office claim"]. Simplified: ask average hours a month. Actual: ask household costs and the share the client states.

| Hours of business use per month | Flat rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home |
| 25 to 50 | GBP 10 a month | "25 to 50 £10" |
| 51 to 100 | GBP 18 a month | "51 to 100 £18" |
| 101 and more | GBP 26 a month | "101 and more £26" |

Below 25 hours a month the flat rate cannot be used. Telephone and internet are not included; claim the business share of those on actual cost.

**Accounting basis.** Q: "Accounting basis?" Options: ["Cash basis: income when received, expenses when paid", "Traditional accounting: income when invoiced, expenses when billed"]. Cash basis is the standard way for a sole trader or a partnership without corporate partners. A limited company, a limited liability partnership and a partnership with one or more corporate partners cannot use it. Nor can a Lloyd's underwriter, a farming business with a current herd basis election, a farming or creative business with a fluctuating profit averaging claim, a business that has claimed business premises renovation allowance within the previous 7 years, a business carrying on a mineral extraction trade, or a business that has ever claimed research and development allowance: https://www.gov.uk/simpler-income-tax-cash-basis/who-can-use-cash-basis. Ask about the averaging claim and the research and development allowance, because a client will not volunteer them. The page sets no turnover limit, so do not apply one.

**Marriage Allowance.** Ask whether the client is married or in a civil partnership, and whether either partner has applied.

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/marriage-allowance |
| Slice of Personal Allowance transferable to a spouse or civil partner | GBP 1,260 | "Marriage Allowance lets you transfer £1,260 of your Personal Allowance" |

**Private-use shares.** Flag every private-use share the client states. The reviewer confirms it is reasonable and documented. The intake records the client's figure and never chooses one.

## Section 7: The final handoff

Produce the handoff message, then invoke `uk-return-assembly` with the package.

Intake complete. I'm now going to run the full UK return preparation:
1. VAT return for any outstanding period, if you are registered
2. Self-employment pages for the trading income
3. The main return and the tax computation
4. Class 4 National Insurance, and voluntary Class 2 if your profits are low and you choose to pay it
5. Student loan repayment, if applicable
6. Payments on account for the following year

You'll get back a working paper, a reviewer brief with positions, citations and flags for your accountant, and a filing calendar.

Deadlines for the calendar, from https://www.gov.uk/self-assessment-tax-returns/deadlines: tell HMRC by 5 October if the client has never sent a return; a paper return by 31 October after the year end; an online return and the balancing payment by 31 January after the year end; the second payment on account by the following 31 July; and an online return by 30 December after the year end to have the balance collected through a tax code. The page prints calendar dates for the return that is open now, which is the year ended 5 April 2026, so read the year beside each date before copying it into a 2026-27 calendar. Class 2 is voluntary below the small profits threshold on https://www.gov.uk/self-employed-national-insurance-rates.

## Section 8: Structured intake package (internal format)

`uk-return-assembly` consumes this JSON. It is internal and not shown unless asked. `tax_year` is written as the two years it spans.

**`null` means NOT YET KNOWN and zero means a real zero.** Zero says the assistant looked and found nothing; `null` says nobody has looked or the client did not answer. `false` is an answer, `null` is not. `scottish_taxpayer`, `accounting_basis`, `vat_status`, `plan_type`, every `_pct` field and everything in `classification` stay `null` until the client or a document settles them. A pipe list such as `"cash | accruals | null"` is the set of allowed values: replace it with one.

~~~json
{
  "jurisdiction": "UK",
  "tax_year": "2026-27",
  "taxpayer": {
    "name": null, "birth_year": null,
    "marital_status": "single | married | civil_partner",
    "residency": "full_year", "scottish_taxpayer": null,
    "utr": null, "ni_number": null, "vat_number": null,
    "vat_status": "standard | flat_rate_scheme | unregistered | unsettled",
    "flat_rate_pct": null, "entity_type": "sole_trader", "industry": null,
    "accounting_basis": "cash | accruals | null"
  },
  "classification": {
    "residence_as_stated": "full_year | part_year | non_resident | unsure",
    "residence_tested": null,
    "employment_status_as_stated": "self_employed | employed | both | unsure",
    "employment_status_tested": null,
    "trade_or_hobby_as_stated": "trade | hobby | unsure",
    "badges_pointing_to_trade": [], "badges_pointing_away": [], "unsettled": []
  },
  "income": {
    "gross_turnover_ex_vat": null, "vat_collected": null, "outside_scope_income": null,
    "cis_deductions_suffered": null, "employment_income": null, "paye_tax_deducted": null,
    "class1_nic_deducted": null, "other_income": null, "client_breakdown": []
  },
  "expenses": { "fully_deductible": [], "mixed_use": [], "disallowable": [], "capital_items": [] },
  "vat": {
    "quarterly_returns_filed": [], "input_vat_reclaimable": null, "flat_rate_scheme": null,
    "flat_rate_pct": null, "limited_cost_goods_cost": null, "first_registered_date": null,
    "rolling_12m_taxable_turnover": null, "expects_to_exceed_in_next_30_days": null
  },
  "mtd_itsa": { "qualifying_income_prior_year": null, "already_using": null, "must_start_from": null, "exempt": null },
  "student_loan": {
    "has_loan": null,
    "plan_type": "plan_1 | plan_2 | plan_4 | plan_5 | postgraduate | null",
    "repaid_via_paye": null, "outstanding_balance": null
  },
  "payments_on_account": {
    "prior_year_sa_liability": null, "prior_year_tax_paid_outside_sa": null,
    "first_poa_paid": null, "second_poa_paid": null, "total_paid": null
  },
  "prior_year": {
    "total_sa_liability": null, "net_self_employment_profit": null,
    "gross_self_employment_and_property_income": null, "capital_allowances_pool": null
  },
  "home_office": {
    "method": "simplified | actual | none | null",
    "hours_per_month": null, "actual_costs": null, "business_pct": null, "annual_amount": null
  },
  "private_use": {
    "motor_vehicle_method": "simplified | actual | none | null",
    "vehicle_type": "car_or_goods_vehicle | motorcycle | null",
    "business_miles": null, "motor_vehicle_business_pct": null,
    "phone_business_pct": null, "broadband_business_pct": null
  },
  "pension": { "personal_contributions": null, "relief_method": "relief_at_source | net_pay | null" },
  "marriage_allowance": { "transfer_to_spouse": null, "transfer_from_spouse": null },
  "open_flags": [], "refusals_triggered": [], "documents_received": []
}
~~~

## Section 9: Refusal handling

Refusals fire from the sweep (Section 2) or during inference, e.g. a limited company found in the documents. When one fires: stop; state the reason in one sentence; name the practitioner to see; offer partial help only if the out-of-scope item is cleanly separable, which is rare. Do not apologise at length, work around the refusal, hint a different answer would fit, or continue silently.

Stop. You have a registered limited company. I'm set up for sole traders only. Limited companies file CT600 returns with separate rules for corporation tax, directors' pay and dividends. You need a chartered accountant familiar with Ltd returns. I can't help with this one.

## Section 10: Self-checks

- **IN1**: No one-question-at-a-time prose in the sweep; `ask_user_input_v0` or one batched list was used.
- **IN2**: Upload-first honoured: documents were asked for before any content question, and parsed before gap questions.
- **IN3**: Gap-filling asked only what the documents do not show.
- **IN4**: Anything ambiguous or risky is in `open_flags`.
- **IN5**: The handoff was explicit and `uk-return-assembly` was invoked with the package.
- **IN6**: The reviewer step was stated upfront and again before handoff.
- **IN7**: Refusals were clean. Stop means stop. No meta-commentary about phases.
- **IN8**: 8 turns or fewer for a prepared user; more than 12 is a failure.
- **IN9**: VAT status was set before inference; for a Flat Rate Scheme client, goods cost and first registration date were asked.
- **IN10**: Scottish status was set, or recorded as unsettled and flagged.
- **IN11**: Making Tax Digital was settled in `mtd_itsa` on GROSS income, not profit.
- **IN12**: Residence, employment status and trade or hobby each appear in `classification` with what the client said, whether tested, and a flag where unsettled.
- **IN13**: No figure from this Guide was copied into a client summary as the client's own.

## Section 11: Performance targets

- **Prepared user**: sweep 30 seconds (1 to 2 turns); upload 2 minutes (1 turn); inference and confirmation 1 turn; gap filling 2 to 3 turns; handoff immediate. About 10 minutes.
- **Unprepared user**: document discovery 10 to 20 minutes offline, the rest the same. 15 to 25 minutes.

## Section 12: Cross-Guide references

Inputs: user documents and answers. Output: the intake package for `uk-return-assembly`, which triggers `uk-vat-return` (if registered), `uk-self-employment-sa103`, `uk-income-tax-sa100`, `uk-national-insurance` (Class 4, voluntary Class 2), `uk-student-loan-repayment` (if applicable) and `uk-payments-on-account`.

Routed straight from the intake when documents show them: `uk-rental-sa105`, `uk-dividends`, `uk-capital-gains-sa108`, `uk-crypto-tax`, `uk-payroll` where there are employees, `uk-bookkeeping` where records will not support a return, `uk-statutory-residence-test` or `uk-non-dom` where residence or domicile is in doubt.

### Change log

- **v0.1 (April 2026):** Initial draft, modelled on `mt-freelance-intake` v0.1.
- **Refresh (September 2026):** Figures re-read on the official pages for tax year 2026 and moved into sourced tables. Making Tax Digital added. Residence, employment status and trade or hobby turned into recorded-and-tested questions. Cash basis turnover limit removed, mileage rate corrected, Class 2 marked voluntary, unknowns changed to `null`.

## The method, step by step

1. Fix the tax year and test residence: https://www.gov.uk/tax-foreign-income/residence
2. Settle the structure. Sole trader stays; Ltd, LLP or partnership is referred (Sections 2, 9).
3. Test whether a return is needed, against the filing trigger and trading allowance: https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return, https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income
4. Settle the VAT regime first, since it decides whether amounts are read net or gross: https://www.gov.uk/how-vat-works/vat-thresholds
5. Settle Making Tax Digital on the earlier year's GROSS self-employment and property income: https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax
6. Record and test employment status and trade or hobby (Section 2). Settle neither.
7. Collect and parse the documents (Sections 3, 4); check the records rule: https://www.gov.uk/self-employed-records/how-long-to-keep-your-records
8. Read the prior year calculation for both payments on account tests: https://www.gov.uk/understand-self-assessment-bill/payments-on-account
9. Confirm the summary and fill the gaps, choosing expense methods with the client (Section 6).
10. Write every unsettled point into `open_flags` and hand the package to `uk-return-assembly`, with the deadlines from https://www.gov.uk/self-assessment-tax-returns/deadlines

## Ask the client first

- Tax year; full-year UK resident, or arrived/left during it?
- Invoice in your own name or through a company? Share profits with anyone?
- 12 month turnover, VAT on invoices, and on the Flat Rate Scheme, cost of goods (not services) and first registration date?
- GROSS earlier-year self-employment and property takings? Any HMRC letter about Making Tax Digital?
- Live in Scotland? Vehicle or home room used for the business, flat rate used before?
- Other income: job, rent, dividends, savings, crypto, a disposal, a partnership share? Student loan plan?

## When to refuse or refer

- Part-year residents, non-residents, split-year treatment: refer to an accountant handling non-resident returns; read `uk-statutory-residence-test` first if unclear.
- Limited companies, LLPs and partnerships as the business itself. A partner with a separate sole trade stays in scope, with a flag.
- More than 5 employees. Payroll at any size routes to `uk-payroll`.
- Employment status the facts contradict (one client, set hours, supervised, no invoices): record, flag, say HMRC can reclassify. Do not decide it.
- An activity that may not be a trade: record the badges both ways and flag it.
- Records that will not support a return: route to `uk-bookkeeping` first.
- Domicile, remittances, foreign income and gains: route to `uk-non-dom`.
- Over the VAT registration limit and not registered: route to `uk-vat-return`, registration is compulsory.
- Inside Making Tax Digital with no digital records: a records problem first.

## Sources

- https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return
- https://www.gov.uk/self-assessment-tax-returns/deadlines
- https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income
- https://www.gov.uk/understand-self-assessment-bill/payments-on-account
- https://www.gov.uk/how-vat-works/vat-thresholds
- https://www.gov.uk/register-for-vat
- https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay
- https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax
- https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax
- https://www.gov.uk/guidance/using-making-tax-digital-for-income-tax
- https://www.gov.uk/self-employed-records
- https://www.gov.uk/self-employed-records/how-long-to-keep-your-records
- https://www.gov.uk/simpler-income-tax-cash-basis
- https://www.gov.uk/simpler-income-tax-cash-basis/who-can-use-cash-basis
- https://www.gov.uk/government/publications/vat-notice-733-flat-rate-scheme-for-small-businesses/vat-notice-733-flat-rate-scheme-for-small-businesses
- https://www.legislation.gov.uk/ukpga/1970/9/section/12B
- https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles
- https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home
- https://www.gov.uk/marriage-allowance
- https://www.gov.uk/scottish-income-tax
- https://www.gov.uk/scottish-income-tax/who-pays
- https://www.gov.uk/self-employed-national-insurance-rates
- https://www.gov.uk/tax-foreign-income/residence
- https://www.gov.uk/employment-status/selfemployed-contractor
- https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim20205

## End of Intake Guide v0.1

End of the intake Guide, version 0.1, refreshed for tax year 2026.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant, ACCA member, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
