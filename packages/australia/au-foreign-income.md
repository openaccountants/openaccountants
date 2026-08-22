---
name: au-foreign-income
description: >
  Use this skill whenever asked about how Australian tax residents are taxed on foreign income -- the worldwide assessable income rule, the foreign income tax offset (FITO) and its offset limit, foreign employment income and the narrowed section 23AG exemption, foreign rental/business/investment income, foreign capital gains and Division 775 forex gains, foreign pensions (UK/US), temporary residents under Subdiv 768-R, overseas HELP debtor worldwide income reporting, return labels 20/20M/20O, currency conversion, and record keeping. Trigger on "foreign income", "overseas income", "FITO", "foreign tax credit", "double tax", "UK pension", "Wise income", "foreign rental", or any GL showing offshore receipts.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---
# Australia Foreign Income -- Resident Taxpayers Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Scope.** This skill covers FOREIGN INCOME OF AUSTRALIAN TAX RESIDENTS (individuals). It does NOT cover foreign residents' Australian-source income (see au-nonresident-cgt), companies' international tax (transfer pricing, thin capitalisation), or GST on cross-border supplies.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary legislation | ITAA 1997 ss 6-5, 6-10; Div 770 (FITO); Div 775 (forex); Subdiv 768-R (temporary residents); ITAA 1936 ss 23AF, 23AG; TAA 1953 Sch 1 (overseas HELP assessments) |
| Tax authority | Australian Taxation Office (ATO) |
| Income year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Core rule | Residents: assessable on worldwide income (s 6-5(2)) -- ordinary + statutory income from ALL sources |
| FITO cap | Australian tax payable on the foreign-taxed and other foreign income (the "offset limit", s 770-75) -- lesser of foreign tax paid or the limit; excess never refunded or carried forward |
| FITO de minimis | Foreign tax paid <= $1,000: claim the actual amount, no limit computation needed |
| s 23AG scope (2026-27) | Confined to: delivery of Australian official development assistance (ODA) by non-government employers; developing-country relief funds; public disaster relief funds; certain prescribed charitable/religious institutions; disciplined force deployment -- 91+ continuous days required; NOT available to Australian government agency employees delivering ODA |
| Temporary residents (Subdiv 768-R) | Most foreign-source income NANE; overseas employment/services income may still be assessable; CGT limited to taxable Australian property; CGT discount apportioned for post-8 May 2012 assets |
| Individual return labels | Question 20 -- foreign source income (labels incl. 20M net foreign employment income, 20O foreign income tax offset, 20P overseas assets >= $50,000 flag); foreign capital gains at question 18, not 20 |
| Medicare levy / MLS | Foreign income counts -- levy is 2% of taxable income (which includes worldwide income); FITO can reduce levy and MLS after tax payable is nil |
| HELP overseas debtors | Worldwide income reporting from 2016-17; overseas travel notification within 7 days if overseas 183+ days in 12 months; report by 31 October; 2026-27 minimum repayment threshold $69,528 (marginal system) |
| Currency conversion | RBA rates from 1 Jan 2020; transaction-date rate or average rate per the translation rules (s 960-50); functional currency rules (s 960-70) generally not for individuals |
| Contributor | Open Accountants |
| Validated by | Pending -- Australian CPA/CA sign-off required |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown residency status | Treat as Australian resident taxed on worldwide income; STOP and escalate if genuinely unclear (residency is threshold -- see au-tax-residency) |
| Foreign tax "paid" unclear (withheld vs assessed vs final) | Treat only tax actually paid (or deemed paid) and evidenced as FITO-eligible; accrued/unpaid foreign tax does NOT count |
| Unknown exchange rate evidence | Use ATO annual average rate for the income year; flag that transaction-date rates may be required (e.g. capital gains, one-off receipts) |
| Foreign employment exemption (s 23AG) claimed | Assume NOT exempt unless the facts map exactly to the confined 2026-27 categories AND 91+ continuous days |
| Overseas asset holding >= $50,000 unclear | Answer "Yes" at 20P and keep the supporting schedule |
| Temporary resident status unclear | Assume NOT a temporary resident (worldwide income assessable) until visa + Social Security Act tests confirmed |
| Foreign pension with possible UPP | Include gross; claim UPP deductible amount ONLY with an ATO determination or solid computation; escalate valuation questions |
| Foreign tax year straddles two Australian years | Apportion to the Australian income years the income aligns with; flag both years |

## Section 3 -- GL sweep library

Foreign income hides in bank feeds, e-wallet exports and platform statements -- never trust the client's "I have no overseas income".

| GL pattern | Likely issue | Action |
|---|---|---|
| Foreign bank interest credits (UK, US, NZ, SG accounts) | Assessable interest income | Convert at average rate; gross before foreign withholding; FITO for foreign tax withheld |
| Dividend credits from overseas brokers (IBKR, Stake, Computershare US) | Assessable dividends (no franking; NZ imputation NOT claimable) | Gross-up to pre-withholding amount; FITO for withholding; check treaty rates |
| WISE / REVOLUT / PAYONEER receipts | Mixed: own transfers vs foreign income vs client payments | Characterise per transaction -- client payments are business/employment income; own-account transfers are NOT income |
| Overseas payroll deposits (foreign employer, no PAYG) | Foreign employment income | Assessable in full; PAYG instalments flag; FITO for foreign tax; s 23AG screen |
| AIRBNB / BOOKING.COM / VRBO payouts for overseas property | Foreign rental income | Gross rent assessable; deductions at Australian rules (interest, rates, repairs, depreciation); FITO for foreign tax on net rent |
| Foreign super/pension periodic payments (UK SIPP, US 401k/IRA, NZ KiwiSaver) | Foreign pension income -- assessable | Include gross less any ATO-determined UPP deductible amount; lump sums escalate (R-AU-FI-4) |
| RSU/ESPP vesting from a foreign employer | ESS discount income (question 12) + foreign tax creditable | Not question 20 income, but FITO at 20O can include foreign tax on ESS discounts |
| Crypto exchange withdrawals to AUD (foreign exchange) | CGT events, not "foreign income" per se | Route to CGT schedule (question 18); FITO possible for foreign tax on the gain |
| Regular small foreign transfers labelled "family support" | Possible foreign income vs gifts/loans | Evidence of gift/loan or treat as income; escalate remittance structuring |
| Foreign currency account balance movements | Div 775 forex realisation events | Check $250k balance election eligibility (s 775-230); otherwise gains assessable/losses deductible |
| Journal reclassifying foreign income as "loan from relative" | Concealment risk | Refuse without documentation; escalate |

---

## Section 4 -- Worked examples

### Example 1 -- FITO cap where foreign tax exceeds Australian tax on the income (2026-27 rates)

Resident employee: Australian salary $60,000; US consulting income A$20,000 (net of nothing; gross); US tax withheld A$6,000 (30%). No deductions. Taxable income $80,000.

```
Step 1 -- Tax on $80,000 (2026-27 rates incl. 2% Medicare levy):
  Income tax: $4,020 + ($80,000 - $45,000) x 30% = $4,020 + $10,500 = $14,520
  Medicare levy: $80,000 x 2%                                          = $1,600
  Total step 1                                                          = $16,120

Step 2 -- Tax payable disregarding the foreign-taxed income ($20,000):
  Taxable income under assumptions: $60,000
  Income tax: $4,020 + ($60,000 - $45,000) x 30% = $4,020 + $4,500     = $8,520
  Medicare levy: $60,000 x 2%                                          = $1,200
  Total step 2                                                          = $9,720

Step 3 -- Offset limit = $16,120 - $9,720                              = $6,400

FITO = lesser of foreign tax paid ($6,000) and limit ($6,400)          = $6,000
```

Result: full $6,000 offsettable. Had the US tax been $7,000, the offset would cap at $6,400 and the $600 excess is lost forever -- no carry-forward, no refund, no pooling into next year.

### Example 2 -- Foreign rental property with deductions and FITO

UK flat rented all year. Gross rent GBP 12,000; UK expenses GBP 4,000; UK tax paid on net GBP 1,600 (20%). Annual average rate 0.50 GBP/AUD.

```
Gross rent:     GBP 12,000 / 0.50  = A$24,000
Deductions:     GBP  4,000 / 0.50  = A$ 8,000   (Australian deductibility rules applied)
Net foreign rent                     = A$16,000  (label 20, net foreign rent)
UK tax paid:    GBP  1,600 / 0.50  = A$ 3,200
```

Taxpayer's other Australian taxable income: $90,000. Taxable income total $106,000.

```
Step 1 tax on $106,000: $4,020 + 30% x $61,000 = $22,320; levy $2,120  = $24,440
Step 2 tax on $90,000:  $4,020 + 30% x $45,000 = $17,520; levy $1,800  = $19,320
Offset limit                                                           = $5,120
FITO = lesser of $3,200 and $5,120                                     = $3,200
```

Note: the UK tax was computed on UK taxable rent (GBP 8,000); if UK depreciation/reliefs differ from Australian deductions, the FITO still uses tax actually PAID, but the offset limit uses the AUSTRALIAN net income figure.

### Example 3 -- UK pension inclusion with UPP determination

UK resident-turned-Australian-resident receives UK State Pension GBP 11,500/year + a private UK pension GBP 6,000/year with an ATO-determined UPP deductible amount of A$2,000. Average rate 0.50.

```
Gross foreign pensions: GBP 17,500 / 0.50 = A$35,000  (assessable in full -- s 6-5(2))
Less UPP deductible amount (D11)          = A$ 2,000
Net foreign pension (label 20)            = A$33,000
```

No UK tax withheld (pensions paid gross under the UK/AU DTA article 17 allocation -- treaty mechanics are escalate-only beyond this note: R-AU-FI-5). The A$33,000 is taxed at Australian marginal rates and counts for Medicare levy. No FITO arises because no foreign tax was paid.

### Example 4 -- Temporary resident: foreign income exempt

Maria holds a temporary skilled visa; she and her spouse are not Australian residents under the Social Security Act 1991; she is an Australian resident for tax purposes and therefore a TEMPORARY resident. In 2026-27 she earns: Australian salary A$95,000; UK bank interest A$4,000 (UK tax A$800 withheld); dividends on US shares A$6,000 (US withholding A$900); net rent on her pre-arrival Manila condo A$10,000.

```
Australian salary        A$95,000  -> assessable, taxed at resident rates
UK interest              A$ 4,000  -> NANE under Subdiv 768-R; NOT declared
US dividends             A$ 6,000  -> NANE; NOT declared; NO FITO for the $900 US tax
Manila rent              A$10,000  -> NANE; NOT declared
```

The A$1,700 foreign tax paid is simply lost -- no FITO because the income is not assessable. Her HELP repayment income, if she had a debt, would still include A$95,000 (and any exempt foreign employment income only if the employment itself was overseas service -- not her case). CGT: a sale of the Manila condo while she is a temporary resident is outside Australian CGT (not taxable Australian property); on ceasing to be a temporary resident she is deemed to acquire non-TAP assets at market value at that date.

### Example 5 -- HELP overseas debtor: worldwide income assessment sketch

Tom has a HELP debt and moved to Canada on 1 August 2026 (overseas 183+ days). He notifies via ATO online within 7 days of leaving. He remains a foreign resident for the whole year for this sketch. Canadian employment income for the Canadian 2026 tax year: CAD 82,000; no Australian income.

```
Obligations: overseas travel notification (done); report worldwide income by 31 Oct 2027.
Assessment method chosen: overseas assessed method -- Canadian 2026 assessment income,
  converted at the applicable average rate (assume 0.90 CAD/AUD): CAD 82,000 / 0.90 = A$91,111.
Worldwide (repayment) income ~ A$91,111 -> above the 2026-27 threshold of $69,528.
Overseas levy (marginal system, 2026-27):
  ($91,111 - $69,528) x 15c = $21,583 x 0.15 = $3,237.45
```

The overseas levy is assessed by the ATO after the worldwide income report (TAA 1953 Sch 1 overseas assessment machinery). If Tom's worldwide income were below $69,528 he would lodge a non-lodgment advice instead. Voluntary repayments from overseas do NOT discharge the assessed overseas levy.

---

## Section 5 -- Numbered rules

### Rule 1 -- Residents are assessable on worldwide income (s 6-5(2), s 6-10(4))

An Australian resident's assessable income includes ordinary and statutory income from ALL sources, in or out of Australia. Foreign source does not matter; receipt does not matter (income held overseas for the taxpayer is still derived). Residency is the threshold question -- apply au-tax-residency before this skill. Foreign residents are taxed only on Australian-source income (s 6-5(3)) and are out of scope.

### Rule 2 -- Foreign income tax offset (Div 770): entitlement

A taxpayer is entitled to a FITO for an income year for foreign income tax PAID (or deemed paid) on an amount included in assessable income (or in NANE income under s 23AI/23AK ITAA 1936). "Paid" means actually paid -- withheld or assessed and settled. The offset is claimed in the year the foreign income is included in Australian income; if the foreign tax is paid later (different foreign tax year), amend the earlier Australian assessment -- special amendment rules allow this outside the normal s 170 windows, but ONLY for changes in foreign tax paid.

### Rule 3 -- The offset limit (s 770-75): the lesser-of cap

```
FITO = LESSER of:
  (a) foreign income tax paid that counts towards the offset, and
  (b) the offset limit = Step 1 - Step 2, where
      Step 1 = Australian income tax payable for the year
               (incl. Medicare levy + MLS, excluding penalties/interest,
               DISREGARDING all tax offsets), and
      Step 2 = the tax that would be payable on the same basis if
               assessable income excluded (i) all amounts on which
               creditable foreign tax was paid and (ii) any other
               foreign-source amounts, and deductions reasonably
               related to those amounts were disallowed
               (debt deductions only where attributable to an overseas PE;
               gifts/super/tax-agent fees are NOT reasonably related).
De minimis: foreign tax paid <= $1,000 -> claim the actual amount; no limit computation.
```

FITO applies AFTER all other non-refundable, non-transferable offsets. Unused offset is NOT refundable and CANNOT be carried forward -- there is no pooling of foreign tax credits across years. Foreign losses reduce the foreign income entering the computation (and net foreign losses quarantine as tax losses; a current-year deferred non-commercial foreign business loss is added back before step 2 -- escalate that computation).

### Rule 4 -- Foreign employment income and the s 23AG exemption

Default: foreign salary/wages of a resident are assessable in Australia (Rule 1), with FITO for foreign tax. The s 23AG ITAA 1936 exemption now applies ONLY where ALL of the following hold: (1) foreign service of 91+ continuous days; (2) the service is directly attributable to -- delivery of Australian official development assistance by the employer (NOT where the employer is an Australian government agency), a Minister-declared developing country relief fund, a public disaster relief fund for a developed country, activities of a prescribed charitable or religious institution exempt because it is located/pursuing objectives outside Australia, or deployment as a member of a disciplined force; and (3) no non-exemption condition applies (broadly, the income is taxed in the foreign country -- a treaty-driven exemption in the foreign country defeats s 23AG). s 23AF (Austrade-approved overseas projects) is a separate, narrower gate. Exempt s 23AG income is still disclosed in the return and feeds the tax-rate-on-other-income mechanics and HELP repayment income. Escalate any s 23AG claim (R-AU-FI-5).

### Rule 5 -- Foreign rental, business and investment income

Foreign rent: gross rent assessable; deductions computed under AUSTRALIAN rules (interest, council/rates, insurance, repairs, depreciation, borrowing costs); net rent at label 20; FITO for foreign tax paid (Example 2). Foreign business income of a sole trader: business schedule + label 20; non-commercial loss rules can defer foreign business losses (T2 flag). Foreign interest/dividends/royalties: gross (pre-withholding) amounts assessable; no franking on foreign dividends; New Zealand imputation credits are NEVER claimable in Australia (though Australian franking credits attached by an NZ franking company are). FITO for withholding actually suffered.

### Rule 6 -- Foreign capital gains, forex and the $250k election

Residents are subject to CGT on worldwide assets. Foreign-source gains/losses go at question 18 (NOT question 20), but foreign tax paid on the gain counts towards the FITO at 20O. Assets held when residency starts are deemed acquired at market value at that time (s 855-45). Div 775 brings realised forex gains to account as assessable income (losses deductible) on foreign-currency accounts and transactions; the s 775-230 $250,000 balance election lets taxpayers disregard forex gains/losses on qualifying transaction/credit-card accounts under the limit -- a written election kept with records. Functional currency rules (s 960-70) are for certain entities, not individuals -- flag, do not apply. From 1 July 2027 the Tax Reform No. 1 Act 2026 CGT reforms change the CGT landscape (verified today) -- re-check any multi-year position that spans that date.

### Rule 7 -- CFC and transferor trust (attribution) -- escalation only

Interests in controlled foreign companies (Part X ITAA 1936) and transferor trusts (Div 6AAA) can attribute undistributed foreign income to Australian residents (attributed foreign income). Detection trigger: question 19 (foreign entities) answers "Yes", or the client controls/benefits from an offshore company or trust. DO NOT compute attribution here -- identify, document the holding, and escalate (R-AU-FI-1).

### Rule 8 -- Foreign pensions and annuities

For a resident, foreign pension/annuity receipts (UK State/private pensions, US 401(k)/IRA distributions, overseas government pensions) are assessable in full under s 6-5(2) -- no general exemption, whatever the foreign treatment. The only reduction is the deductible amount of undeducted purchase price (UPP) where the pension has one (personal contributions): claim at D11 only with an ATO determination of the deductible amount (or a defensible computation). Lump sums from foreign super funds are a separate regime (some taxable, some exempt) -- contact/escalate rather than compute (R-AU-FI-4). FITO applies to foreign tax withheld on pension payments.

### Rule 9 -- Return labels and disclosures

Question 20 (supplementary return): assessable foreign income by type -- net foreign employment income (label 20M), net foreign pension/annuity income (with/without UPP), net foreign rent, other net foreign income; Australian franking credits from an NZ franking company; exempt foreign employment income (s 23AG/23AF amounts are still disclosed); FITO at label 20O; label 20P "Yes" if overseas assets total >= A$50,000 (historical cost or market value, whichever greater, at 30 June exchange rate). NOT at question 20: foreign capital gains (question 18), ESS discounts (question 12), foreign ETPs (question 4), pension arrears lump sums (question 24). A schedule of additional information (per country, per income type, foreign tax per type) is required where instructed.

### Rule 10 -- Medicare levy, MLS and FITO interaction

Foreign income is inside taxable income, so it attracts the 2% Medicare levy and counts toward MLS income. FITO ordering: offset reduces income tax payable first; any residue then reduces Medicare levy; then MLS. s 23AG-exempt income does not bear levy directly but can lift the effective rate context (and counts in HELP repayment income). Temporary residents' NANE foreign income bears no levy. MLS thresholds are in au-medicare-levy -- do not restate; foreign income simply forms part of the MLS income base.

### Rule 11 -- Records and currency conversion

Keep: foreign tax receipts/assessments/withholding certificates (per country, per income type); payslips and foreign payroll summaries; exchange rate evidence (ATO/RBA daily, monthly or annual average rates as applicable); bank statements showing foreign balances; the FITO limit worksheet; any $250k forex election. Five-year retention from lodgment. Conversion: translate at the rate prevailing at the time of the transaction OR an applicable average rate per the translation rules (s 960-50); from 1 Jan 2020 ATO publishes RBA-sourced daily/monthly/annual rates; an unlisted currency may use any reasonable externally sourced rate. Capital gains and one-off receipts generally need transaction-date rates; recurring salary/pension streams suit average rates -- state the convention used in the working papers.

### Rule 12 -- Temporary residents vs part-year residents

Temporary residents (temporary visa + not Social Security Act Australian residents + spouse likewise): Subdiv 768-R makes most foreign-source income NANE; employment/services income earned overseas while a temporary resident CAN be assessable (Part A of question 20 allocates it); CGT applies only to taxable Australian property, with deemed market-value acquisition of non-TAP assets on ceasing temporary residence; the CGT discount is apportioned for foreign/temporary-resident days on assets acquired after 8 May 2012. A person who was an Australian resident after 6 April 2006 without a temporary visa can never later become a temporary resident. PART-YEAR residents are different: full worldwide income for the resident period, Australian-source only for the foreign-resident period, and a pro-rated tax-free threshold (s 6-5(3) + ITAA 1936 residency-period rules) -- do not confuse the two concessions.

### Rule 13 -- HELP and overseas debtors

From 2016-17, HELP/VSL/AASL debtors who are (or become) foreign residents must: notify within 7 days via an overseas travel notification if overseas 183+ days in any 12 months; and report WORLDWIDE income (repayment income + non-resident foreign-sourced income) or lodge a non-lodgment advice, by 31 October, through ATO online services or a registered tax agent. Foreign-sourced income is computed by the overseas assessed method (most recent foreign tax authority assessment covering 12 months overlapping the Australian year), the comprehensive tax-based assessment method, or the default rules in the Overseas Debtors Repayment Guidelines 2017. The ATO then assesses an overseas levy on the same marginal thresholds as domestic compulsory repayments (2026-27: nil to $69,528; 15c/$1 over $69,528 to $129,717; $9,028 + 17c/$1 over $129,717 to $186,050; 10% of total repayment income at $186,051+). s 154-19 TAA Sch 1 machinery covers the overseas assessment; deferral/amendment of the levy is possible on hardship-style grounds (R-AU-FI-6 for disputes).

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Foreign tax year mismatch

**Trigger:** foreign tax assessed on a different income year (e.g. UK 6 April year, US calendar year). **Action:** claim FITO in the Australian year the income is assessed, then amend when the foreign tax is actually paid (special amendment rules); diarise.

### T2-2 -- Deferred non-commercial foreign business loss

**Trigger:** foreign sole-trader loss deferred under the non-commercial loss rules. **Action:** add-back adjusts step 2 of the offset limit; escalate computation.

### T2-3 -- Excess foreign tax (creditable > limit)

**Trigger:** high-withholding countries (e.g. 30% US on consulting, gross-up regimes). **Action:** quantify the lost excess for the client letter; check treaty-reduced withholding was actually claimed at source (refund claim in the foreign country may be the only recovery); escalate treaty claims (R-AU-FI-5).

### T2-4 -- $250k forex balance election hygiene

**Trigger:** multiple foreign-currency transaction accounts with realised gains. **Action:** confirm account eligibility (transaction/credit-card accounts), election in writing before reliance, balance test monitoring; note CGT-on-withdrawal carve-out coverage.

### T2-5 -- 2027 CGT reform horizon

**Trigger:** any position spanning 1 July 2027 (asset disposals, deemed acquisitions, discount computations). **Issue:** Tax Reform No. 1 Act 2026 reforms CGT from 1 July 2027 (verified 20 August 2026). **Action:** flag on every foreign-asset CGT computation that crosses the date; re-verify rules before lodgment of 2027-28 returns.

### T2-6 -- Concealment/data-matching risk

**Trigger:** CRS-exchanged accounts, Wise/Revolut flows, "gifts from family" patterns. **Action:** ATO receives financial account data from participating foreign tax authorities; document source-of-funds for every material inbound foreign transfer; refuse recharacterisation without evidence.

---

## Section 7 -- Excel working paper template

```
AUSTRALIA FOREIGN INCOME -- RESIDENT WORKING PAPER
Taxpayer: [name]   Income year: 2026-27   Residency: [resident / temp resident / part-year]
Prepared: [date]

1. FOREIGN INCOME REGISTER (per country, per type)
  Country | Type (salary/rent/interest/dividend/pension/business/other)
  Gross (FCY) | Rate used (daily/avg annual, source) | Gross AUD
  Deductions AUD (Australian rules) | Net AUD
  Foreign tax paid (FCY) | Rate used | Foreign tax AUD
  Return label (20M / 20 rent / 20 other / D11 / q18)

2. FITO LIMIT WORKSHEET (skip if total foreign tax <= $1,000)
  Step 1 tax payable (incl. levy + MLS, before offsets):  A$[____]
  Step 2 tax payable disregarding foreign-taxed and other
    foreign-source income and reasonably related deductions: A$[____]
  Offset limit (Step 1 - Step 2):                          A$[____]
  FITO claimed = lesser of foreign tax paid and limit:     A$[____]  (label 20O)
  Excess foreign tax lost:                                 A$[____]

3. SCREENS
  s 23AG screen (employer type / 91 days / attribution / non-exemption): [PASS/FAIL/ESC]
  Temporary resident screen (visa + SSA tests):            [Y/N]
  Question 19 foreign entities (CFC/trust flag):           [Y/N -> ESCALATE]
  Overseas assets >= $50,000 (20P):                        [Y/N]
  Forex accounts and $250k election:                       [____]
  HELP debt + overseas 183+ days (notification/report):    [____]

REVIEWER FLAGS: [list Tier 2 flags and escalation items]
```

---

## Section 8 -- Reading guide

1. Residency first. Worldwide taxation follows from s 6-5(2); nothing else in this skill matters until residency (and temporary-residency) is settled.
2. Gross, then convert, then offset. Always bring in the gross foreign amount at the correct rate; never net off foreign tax before assessing.
3. The offset limit is a lesser-of test. Foreign tax above the Australian tax on that income is permanently lost -- compute the limit before promising relief.
4. Labels matter: foreign capital gains at question 18, employment income at 20M, FITO at 20O, asset disclosure at 20P.
5. s 23AG is now a narrow gate -- employer type and foreign taxability decide it, not the fact of working overseas.
6. Medicare levy and HELP follow the income, not the offset: foreign income feeds both bases.

---

## Section 9 -- Onboarding fallback

If the client provides only bank/e-wallet statements:

1. Sweep all accounts per Section 3; build the foreign income register with exchange-rate assumptions listed per line.
2. Characterise every foreign-currency inflow (income vs transfer vs gift vs loan) -- undocumented items default to income.
3. Compute FITO at the actual foreign tax evidenced, with the limit worksheet; flag missing foreign tax receipts.
4. Run the s 23AG, temporary resident, question 19, 20P and HELP screens and record PASS/FAIL/UNKNOWN.
5. **Flag:** "Register built from bank/e-wallet data only. Foreign tax receipts, residency facts, visa status, foreign assessments and treaty positions not sighted. Reviewer must confirm before any position is taken."

---

## Section 10 -- Reference material

### Key figures

| Item | Value (2026-27) |
|---|---|
| Resident rates | 0% to $18,200; 15% $18,201-$45,000; $4,020 + 30% $45,001-$135,000; $31,020 + 37% $135,001-$190,000; $51,370 + 45% over $190,000 |
| Medicare levy | 2% of taxable income (worldwide for residents) |
| FITO de minimis | $1,000 |
| Overseas assets disclosure (20P) | A$50,000 |
| Forex balance election | $250,000 (s 775-230) |
| HELP 2026-27 thresholds | Nil to $69,528; 15c/$1 to $129,717; $9,028 + 17c/$1 to $186,050; 10% of total repayment income above |
| s 23AG continuous service | 91+ days |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Worldwide assessable income | ITAA 1997 ss 6-5(2), 6-10(4); ato.gov.au -- Australian resident foreign and worldwide income (QC72091, updated 15 June 2026) |
| FITO entitlement and limit | ITAA 1997 Div 770 (s 770-75); ato.gov.au -- Claiming a FITO (QC72205, 8 June 2026); Guide to foreign income tax offset rules 2026, "Calculate your FITO or offset limit" (QC101688) |
| s 23AG scope | ITAA 1936 s 23AG; ato.gov.au -- Exempt income from foreign service / Exemption under 23AG (8 June 2026); TR 2013/7 |
| Return labels | Individual supplementary tax return instructions 2025, question 20 (QC104266) and 2026 instructions (D11 UPP) |
| Foreign pensions / UPP | ato.gov.au -- UPP of a foreign pension or annuity; myTax 2026 foreign pensions and annuities |
| Temporary residents | ITAA 1997 Subdiv 768-R; ato.gov.au -- Foreign and temporary resident income (QC72093, 8 June 2026); Foreign and temporary residents (residency) |
| Forex | ITAA 1997 Div 775; ato.gov.au -- Forex elections ($250,000 balance election, s 775-230) |
| Conversion | ITAA 1997 s 960-50 (translation), s 960-70 (functional currency); ato.gov.au -- Foreign exchange rates (RBA rates from 1 Jan 2020) |
| HELP overseas | TAA 1953 Sch 1 (incl. s 154-19 overseas assessments); ato.gov.au -- Overseas obligations when repaying loans (QC47358, 30 June 2026); repayment thresholds (QC16176, 30 June 2026); Overseas Debtors Repayment Guidelines 2017 |
| Rates | ato.gov.au -- Tax rates Australian resident (QC73320, 13 August 2026); new tax cuts measure page (13 May 2026) |
| Treaties | ato.gov.au -- Income tax treaties (DTA list); Treasury treaty texts |
| CGT horizon | Tax Reform No. 1 Act 2026 (CGT reform from 1 July 2027); FRCGW rate 15% (au-nonresident-cgt) |

### Test suite

**Test 1:** Resident, $80,000 taxable incl. $20,000 US income, US tax $6,000. -> FITO $6,000 (limit $6,400, Example 1 arithmetic).

**Test 2:** Foreign tax paid $8,000; offset limit computed at $6,500. -> FITO $6,500; $1,500 lost, no carry-forward.

**Test 3:** UK net rent A$16,000, UK tax A$3,200, limit $5,120. -> FITO $3,200.

**Test 4:** Temporary resident with UK interest A$4,000 and UK tax A$800. -> Income NANE; no FITO.

**Test 5:** Australian government employee posted overseas delivering ODA, 190 days. -> NOT s 23AG exempt (government agency exclusion); assessable with FITO.

**Test 6:** Private-company employee contracted by DFAT delivering ODA, 180 continuous days. -> s 23AG gate passed subject to non-exemption conditions; escalate claim.

**Test 7:** Foreign pension GBP 17,500 at 0.50 avg, UPP deductible A$2,000. -> Assessable A$35,000 less A$2,000 = A$33,000 net.

**Test 8:** Foreign capital gain taxed overseas. -> Gain at question 18; foreign tax counts toward FITO at 20O.

**Test 9:** HELP debtor overseas 200 days, worldwide income A$91,111. -> Overseas levy ($91,111 - $69,528) x 15% = $3,237.45.

**Test 10:** Foreign-currency transaction account, balance always < $250k, written election made. -> Disregard FRE2 gains/losses on the account while eligible.

### Prohibitions

- NEVER net foreign tax off foreign income before computing assessable income -- assess gross, offset separately
- NEVER claim FITO for foreign tax accrued but not paid, or for NZ imputation credits
- NEVER carry forward or pool excess foreign tax into a later year
- NEVER treat s 23AG as a general "worked overseas" exemption -- verify employer type, 91 days, and foreign taxability, and escalate claims
- NEVER put foreign capital gains at question 20 (question 18) or skip 20O for foreign tax on gains/ESS discounts
- NEVER apply the functional currency rules (s 960-70) to individuals
- NEVER compute CFC/transferor trust attribution -- identify and escalate
- NEVER ignore the Medicare levy / HELP consequences of foreign income
- NEVER present figures as definitive; all outputs need professional sign-off

---

## Refusal catalogue

- **R-AU-FI-1 -- CFC / FIF / transferor trust attribution** -- Attribution regime computations (Part X, Div 6AAA, former FIF). Identify the holding, complete question 19 disclosure, and escalate to an international tax specialist.
- **R-AU-FI-2 -- Expatriate structuring** -- Advice on structuring remuneration, entities or residency to minimise cross-border tax (income splitting, offshore companies, second residency). Refuse; compute compliance positions only.
- **R-AU-FI-3 -- DTA tie-breaker disputes** -- Dual-residency tie-breakers (permanent home, centre of vital interests, habitual abode). Refuse the determination; document facts; escalate.
- **R-AU-FI-4 -- Foreign pension valuations and lump sums** -- Valuing foreign pension interests, computing UPP without an ATO determination, or characterising foreign super lump sums. Escalate (ATO determination process or specialist).
- **R-AU-FI-5 -- Treaty exemption claims beyond the mechanical** -- s 23AG claims, treaty article applications (employment income, pensions, entertainers), foreign-country refund claims for excess withholding. Mechanical withholding-rate lookups are fine; entitlement analysis escalates.
- **R-AU-FI-6 -- Foreign trust distributions** -- Distributions from foreign (non-resident) trusts, including s 99B and corpus/income characterisation. Escalate.
- **R-AU-FI-7 -- Overseas HELP levy disputes** -- Challenges to overseas levy assessments, deferrals on hardship grounds, foreign assessment method disputes. Escalate.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
