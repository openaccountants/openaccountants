---
name: india-income-tax
description: Use this skill whenever asked about Indian income tax for a resident individual with salary, interest, house property, or business or professional income, including freelancers and sole proprietors. Trigger on phrases like "how much tax do I pay in India", "India income tax", "new tax regime", "old tax regime", "section 87A rebate", "44AD", "44ADA", "presumptive taxation", "advance tax India", "Form 26AS", "AIS", "ITR-1", "ITR-3", "ITR-4", "Sugam", "Form 10-IEA", "Income-tax Act 2025", "Tax Year 2026-27" or "AY 2026-27". It covers both regimes, slabs, rebate and marginal relief, surcharge and cess, standard deduction and key deductions, presumptive income, regime choice, advance tax and interest, residence tests, TDS credits, the ITR form and the return deadlines, for Tax Year 2026-27 under the Income-tax Act, 2025 and AY 2026-27 returns under the 1961 Act. Non-residents, RNORs, capital gains beyond the ITR-1/ITR-4 limits, foreign income, firms, LLPs and companies are referred.
version: "0.4"
type: computation
jurisdiction: IN
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# India income tax for resident individuals: salary, freelancers and small businesses (Tax Year 2026-27, with AY 2026-27 returns)

## Scope

- This skill covers resident individuals (not RNOR) with salary, interest, one or two house properties, and business or professional income, including presumptive income. It covers both regimes, the rebate, surcharge and cess, advance tax, TDS credits and the return deadlines.
- **Primary year: Tax Year 2026-27** (1April 2026 to 31 March 2027). The Income-tax Act, 2025 governs it. The portal says: "The 1961 Act stands repealed on the 01.04.2026." The new Act uses "tax year" in place of "previous year" and drops "assessment year".
- **Returns being filed now: AY 2026-27** (income of FY 2025-26). These are filed and assessed entirely under the Income-tax Act, 1961, with the old ITR forms. See the dated section "AY 2026-27 returns (FY 2025-26), filed in 2026" below.
- Out of scope, refer: non-residents and RNORs, capital gains beyond the ITR-1/ITR-4 limits, foreign income or assets, firms, LLPs and companies, tax audit cases, virtual digital assets.
- Currency is Indian rupees. Amounts use Indian grouping (₹12,00,000 is INR 1,200,000).

## Ask the client first

Source for this checklist: [Salaried Individuals for AY 2026-27](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1).

- Which year is this for: Tax Year 2026-27 (new Act) or AY 2026-27 (income of FY 2025-26, old Act)? Challans and returns must name the right year.
- Residential status for the year: days in India this year and in the previous four years, citizenship or Indian origin, and income other than foreign-source income.
- Age at any time in the year (below 60,60 to below 80,80 or more). It changes the old-regime age/residence exemption; senior advance-tax relief separately requires no business/profession income.
- Regime: new (default) or old. If the client has business or professional income, did they file Form 10-IEA in an earlier year, and have they already used the one-time switch back?
- Kind of work: a profession listed for presumptive profession income (legal, medical, engineering or architectural, accountancy, technical consultancy, interior decoration, or notified), or a business. Is any income commission, brokerage or agency income?
- Gross receipts or turnover for the year, and how much was received in cash as opposed to account-payee cheque, draft, bank transfer or prescribed electronic mode.
- Salary: old-cycle Form 16/current Form 130 under rule 215, employer category (for the employer NPS limit), HRA and rent paid if old regime is being considered.
- Form 26AS and AIS downloaded? Every TDS, TCS, advance tax and self-assessment challan.
- Advance tax paid, with dates.
- Any director role, unlisted shares, foreign asset or foreign income, brought-forward loss, short-term capital gain, or long-term gain under s.112A above ₹1,25,000. Any of these rules out ITR-1 and ITR-4 ([returns and forms](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)).
- For AY 2026-27: has the return already been filed, and on what date?

## The method, step by step

Sources: [Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq) and [Salaried Individuals for AY 2026-27](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1).

1. **Fix the year and the Act.** Income earned from 1April 2026 is Tax Year 2026-27 under the Income-tax Act, 2025. Income of FY 2025-26 is AY 2026-27 under the 1961Act, even though the return is filed after 1April 2026.
2. **Fix residential status** under s.6 (same tests in both Acts; see the residence table below). If the client is non-resident or RNOR, stop and refer.
3. **Sort income by head**: salary, house property, business or profession, capital gains, other sources. From bank statements: gross up any receipt net of TDS to the invoice amount; reconcile loans and own-account transfers before excluding them; separate refund principal from interest and any recovery of previously deducted expenditure or GST/income, checking records and referring uncertain tax treatment; never exclude every receipt labelled income-tax/GST refund automatically; keep salary and interest out of business receipts.
4. **Business or profession income.** If eligible and chosen, apply the presumptive rates (44AD business, 44ADA profession; s.58 of the 2025 Act for Tax Year 2026-27). The statutory computation also uses higher actually claimed profit. Check eligibility, exclusion and cash-deeming conditions beside the figures. Declaring less, or leaving the scheme, raises books and audit questions: refer. Otherwise compute actual profit from books (ITR-3).
5. **Choose the regime.** Compute tax both ways when the client has old-regime deductions and a valid old-regime option. The new regime is the default. The old regime must be chosen on time (see "Regime choice" below).
6. **Deductions.** New regime: salary standard deduction, employer pension under current 124(1)-(2) (old-cycle 80CCD(2)), government Agniveer contribution current 125(2), and eligible let-out interest subject to the current house-loss restrictions. Old regime: standard deduction plus Chapter VI-A deductions, HRA and home-loan interest within their limits.
7. **Tax on total income** from the slab table for the chosen regime and age.
8. **Rebate** (resident individuals only): new regime up to ₹60,000 where total income does not exceed ₹12,00,000, with marginal relief just above; old regime up to ₹12,500 where total income does not exceed ₹5,00,000 ([rebate table](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)).
9. **Surcharge** above ₹50 lakh, with marginal relief. Then **Health and Education Cess at 4%** on tax plus surcharge ([surcharge and cess](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)).
10. **Credits.** Match TDS/TCS to the relevant statement and assessability year, resolve differences without fabricating credit, preserve current s.401 protection for amounts actually deducted, then subtract supported credits, then advance tax and self-assessment tax paid. Check interest under old 234A/234B/234C or current 423/424/425, retaining the current 425 constructionhold and any late fee.
11. **Pick the ITR form** and file by the due date. For the older cycle, e-verify or send signed ITR-V within 30 days under current portal guidance; do not project that deadline onto an unconfirmed TY 2026-27 utility.

### Current-year answer layer: Tax Year 2026-27

Use these enacted provisions for the current year. The older-cycle tables are retained below with their period. Amounts are INR; cumulative base taxes and example results are derived. A quoted statutory number written in words is identified on its row. Scope remains ordinarily resident individuals even where the cited provision also covers other persons.

| Rule | Current value and conditions | Official source |
|---|---|---|
| New-regime s.202 slabs | Up to 400,000 nil; 400,000-800,000: 5%; 800,000-1,200,000: 10%; 1,200,000-1,600,000: 15%; 1,600,000-2,000,000: 20%; 2,000,000-2,400,000: 25%; above 2,400,000: 30%. Each rate applies only to excess in its band; subtract lower-band limit and add accumulated lower-band tax | s.202(1); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Old-regime resident below 60 | Up to 250,000 nil; 250,000-500,000: 5%; 500,000-1,000,000: 20%; above 1,000,000: 30%. Derived bases 12,500 and 112,500 | Finance Act 2026 First Schedule I-B Para A; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old-regime resident 60 to below 80 | Up to 300,000 nil; 300,000-500,000: 5%; 500,000-1,000,000: 20%; above 1,000,000: 30%. Derived bases 10,000 and 110,000; age any time in year | First Schedule I-B Para A; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old-regime resident 80 or more | Up to 500,000 nil; 500,000-1,000,000: 20%; above 1,000,000: 30%; derived base 100,000; age any time in year | First Schedule I-B Para A; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Resident new-regime rebate | Income at most 1,200,000 (in words on page): lesser of slab income-tax and 60,000. Above 1,200,000, if relevant tax exceeds income above that threshold, relief is that excess; s.156(3) caps rebate to s.202 slab tax, so no automatic rebate of special-rate tax. Amounts printed in numerals on page | s.156(2)-(3); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Resident old-regime rebate | Income at most 500,000: lesser of income-tax and 12,500. No new-regime marginal-relief extension for this threshold. Amounts printed in numerals on page | s.156(1); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Surcharge/cess | Income above 5,000,000: 10%; above 10,000,000: 15%; above 20,000,000: 25%; above 50,000,000 old 37%, new 25% maximum. Test marginal relief at each applicable threshold; special capital-gain/dividend surcharge caps and exceptions require referral. Health and Education Cess 4% of tax plus surcharge after relief | FAs.3 and First Schedule I-B Para A/F; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Salary standard deduction | Lesser of salary and 75,000 under s.202; lesser of salary and 50,000 otherwise. Amounts printed in numerals on page; this is not an allowance against freelance receipts | s.19(1)Table row 2; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Family pension | Lesser of one-third family pension and 25,000 under s.202, or 15,000 otherwise. Amounts printed in numerals on page; family pension is other-source income, not salary standard deduction | s.93(1)(d); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Old-regime specified savings | s.123 combined deduction at most 150,000, only eligible Schedule XV payments and its payment/holding/other conditions. Own-pension additional s.124(3) at most 50,000, without double-counting s.123; neither is a general new-regime deduction. Limits printed in numerals on page. Exact investment eligibility remains document-specific | ss.123-124 and s.202(2); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Employer pension contribution | s.124(1): 14% salary for central/state government, 10% other employers; under s.202 the other-employer limit is also 14%. Salary includes DA if employment terms provide, excludes other allowances/perquisites. s.124(1)-(2) survive new regime; verify employer contribution, not own contribution | ss.124(1)-(2),(13), 202(2)(a)(xii); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Agniveer | s.125(1) eligible individual's own Agniveer Corpus contribution and 125(2) central-government contribution; new regime preserves ONLY 125(2), not own 125(1). Withdrawal exemption/eligibility must be separately checked, not assumed from this deduction | section 125; section 202(2)(a)(xii); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Old-regime health deduction | Separate self/spouse/dependent-child and parent pools normally 25,000 each; qualifying senior cases 50,000 each. Preventive health check-up 5,000 is an AGGREGATE sublimit within pools, not 5,000 extra per pool. Eligible senior medical expenditure requires no health-insurance payment for that person; combined pool caps apply. Insurance/medical payment noncash, preventive check-up may be cash; approved insurance and multi-year apportionment conditions apply. Amounts printed in numerals on page | s.126(1)-(11), excluded by 202(2); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Old-regime interest deduction | s.153: non-senior individual/HUF savings interest only, at most 10,000; resident senior citizen 60 or more during year: qualifying deposit interest including term deposits at most 50,000. Banking/co-operative banking/post-office conditions apply; firm/AOP/BOI deposit income does not generate personal partner/member deduction. Limits printed in numerals on page | section 2(100); section 153; section 202(2); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| House-property deductions | s.22: 30% annual value; qualifying borrowed-capital interest and preconstruction interest in 5 equal instalments from acquisition/construction year. For self-occupied property, aggregate interest generally 30,000 or 200,000 if qualifying acquisition/construction loan and completion within 5 years from end of borrowing tax year, with prescribed lender interest certificate. Limits in numerals; 5 years/instalments in words on page. Abroad-payable interest has the s.22(6) TDS/agent restriction | s.22(1)-(6); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| House loss/regime | Old regime: s.109(1)(b) cross-head house loss capped 200,000; s.110 remaining house loss only against future house income for up to 8 tax years. New regime excludes self-occupied interest and cross-head house-loss setoff; s.202(3) deems the disallowed loss/depreciation fully given effect, so do not promise later deduction of it | sections 109-110; section 202(2)-(3); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| HRA | New regime excludes Schedule III Table row 11 exemption. Old regime requires rent expenditure for occupied accommodation not owned by recipient, subject to prescribed extent. Exact city/rent/salary formula is not computed here | Schedule III Table 11 and 202(2)(a)(i); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Business presumption | s.58(2)serial 1: eligible resident individual/HUF/non-LLP firm; no Chapter VIII-C deductions, specified profession, agency, commission/brokerage or goods-carriage scheme. Limit 20,000,000, increased 30,000,000 only if cash receipts at most 5%; non-account-payee cheque/draft deemed cash. Limits in words on the page; Finance Act 2026 s.40 corrected 58(11)(a)(i) | ss.58(2),(9),(11), FA 40; https://egazette.gov.in/WriteReadData/2025/265620.pdf; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Business income | Aggregate 6% qualifying banking/online receipts during year or before 263(1)original due date plus 8% rest, or higher actually claimed profit. Unknown mode is an unresolved input, not proof of cash share | s.58(2)serial 1; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Professional presumption | s.58(2)serial 3: resident individual/non-LLP firm, profession under 62(4), receipts at most 5,000,000 or 7,500,000 (in words on the page) if cash at most 5%; deemed-cash instruments included. Income 50% receipts or higher actual claimed profit. Specified professions include information technology and company secretary as well as the older listed professions; other notified professions need their notification | ss.58(2),(9),(11)(b), 62(4); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Lower profit/lockout/assets | Lower profit AND total income above maximum not chargeable triggers 58(3)books/audit; serial 1 lockout if a nonconforming declaration occurs within succeeding 5 years, barring benefit for 5 years after that year, subject 58(7)-(8). No extra expense/allowance against presumption; WDV deemed adjusted for depreciation. Preserve asset history; audit/book exceptions referred | ss.58(3)-(8), 62-63; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Regime option | s.202(4): business/profession timely opt-out continues, withdrawal once in subsequent year, no further opt-out while business continues; cessation exception. Nonbusiness timely-return choice annually. Rule 136 puts current option/withdrawal in 263(1)return; 536(2)(f) saves only an old option in force immediately before commencement | ss.202(4), 536(2)(f); https://egazette.gov.in/WriteReadData/2025/265620.pdf; rule 136; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Advance tax | Net advance-tax liability at least 10,000; resident 60 plus exempt only with NO business/profession income. Ordinary cumulative 15%/45%/75%/100% by 15 June/15 September/15 December/15 March; 58 serial 1/3 whole by 15 March; serial 2 ordinary. Payments by 31 March count as advance tax. Current 425(2)/(3)construction remains held in in-advance-tax | sections 403-408; section 425; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Self-assessment/rounding | s.266(3) insufficient cash adjusts first fee, then interest, then tax; do not describe tax balance alone as total cash due. s.424(4) adjusts subsequent self-assessment tax for interest computation. s.516 rounds total income and payable/refundable amounts to nearest 10, ignoring paise, last digit 5 or more up, otherwise down; retain full working | ss.266(3), 424(4), 516; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Current statement/certificates | Ordinary salary Form 130, ordinary nonsalary 131, exceptions 132/133 under rule 215; Form 168 AIS under rule 245. Statement form depends on actual deduction provision/payee category; no universal 140/144 claim. Rule 203 credit follows assessability year/proportion and documented exceptions; s.401 protects tax actually deducted without fabricating missing credit | rule 203; rule 215; rule 219; rule 245; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; s.401; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Current original-return categories | s.263(1)(c) as amended: 30 November 2027 if 172 report required; 31 October 2027 company, required audit under this/other law, and specified audit-firm partner/spouse s.10 apportionment categories; 31August 2027 other business/profession and partner of a firm not required to be audited, plus spouse where s.10 apportionment applies; 31 July 2027 residual cases. Apply exact partner/spouse and category priority, not only filer form; required audit is enough | Finance Act 2026 s.66; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Current belated/revised/fees | s.263(4): within 9 months tax-year end or assessment completion earlier; 263(5): within 12 months or assessment completion earlier.428(a)late-return fee 1,000 if income at most 500,000,5,000 otherwise; 428(b)revised fee same amounts beyond 9 months tax-year end, within the applicable 263(5)revision window. Updated-return 267 eligibility/additional tax require referral; no assumption that every old case qualifies | Act 263/428 amended by FA 66/96; https://egazette.gov.in/WriteReadData/2025/265620.pdf; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Current form controls | Rule 164: ITR 1 ordinary resident individual, income at most 5,000,000 (in words on the page), permitted salary/up to 2 houses/other-source/agriculture at most 5,000/198 LTCG at most 125,000; ITR 4 qualifying resident non-RNOR individual/HUF or resident non-LLP firm with 58 income and permitted 198 LTCG; ITR 2 nonbusiness otherwise, ITR 3 business otherwise. Apply ALL following exclusions and required verification mode | rule 164 entire; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

Current rule 164(6) exclusions, not merely headline income limits: foreign asset/signing authority/income; s.10 income apportionment; s.93 deduction other than its permitted family-pension deduction; directorship; unlisted equity; income above 5,000,000; more than 2 chargeable houses; brought-forward or carryforward loss; tax deducted on income assessable to another person; the defective treaty-relief/deduction cross-reference in 164(6)(l); agriculture above 5,000; deferred ESOP tax; income under Part A of Chapter XIII special rates. The last item interacts with expressly allowed 198 gains in 164(5); both that interaction and 164(6)(l) remain held, not silently repaired. ITR 1 additionally bars current other-source loss under 164(2)(c), cash-withdrawal TDSunder 393(3)Table 5 under 164(3)(l), and relief 159/deduction 160 under 164(3)(i). Its expressly permitted 198 LTCG 164(2)(d)also conflicts with 164(3)(n)Part AChapter XIIIbar, so that gain interaction is held for ITR 1 as well as ITR 4. Required electronic/digital verification, audit and filing mode depend on 164(12) and actual category; no assumed current portal field names. [rule 164](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

Current return categories also give 31August 2027 to partner of a firm not required to be audited and corresponding spouse where s.10 apportionment applies; these do not fall into residual 31 Julymerely because their own income is nonbusiness. The31October2027category applies to a partner of a firm required to be audited and spouse where s.10apportionment applies;30November2027applies where the corresponding firm requires s.172report. Audit-report 63(3)/rule 47 prescribed report timing is separate; do not narrow the category to an audit actually completed. [263 as amended](https://egazette.gov.in/WriteReadData/2026/271439.pdf); [rule 47](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

### Older-cycle figures by year ([Salaried Individuals for AY 2026-27: tax slabs](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1))

**Confirmed current law, separately from the older filing cycle.** The rates table below retains the official AY 2026-27 figures for the 2025-2026 filing cycle. Current TY 2026-27 rates have now been read in s.202 and Finance Act 2026; the separate current-year answer layer supplies operative provisions rather than projecting an old portal page. Derived base-tax amounts in slab rows are cumulative arithmetic, not extra allowances. [s.202](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Finance Act 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf).

### New tax regime (default), all ages, resident or non-resident ([source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1))

| Total income | Tax |
| --- | --- |
| Up to ₹4,00,000 | Nil; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| ₹4,00,001 to ₹8,00,000 | 5% above ₹4,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| ₹8,00,001 to ₹12,00,000 | ₹20,000 + 10% above ₹8,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| ₹12,00,001 to ₹16,00,000 | ₹60,000 + 15% above ₹12,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| ₹16,00,001 to ₹20,00,000 | ₹1,20,000 + 20% above ₹16,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| ₹20,00,001 to ₹24,00,000 | ₹2,00,000 + 25% above ₹20,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| Above ₹24,00,000 | ₹3,00,000 + 30% above ₹24,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |

### Old tax regime ([source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1))

| Age at any time in the year | Nil band | Then |
| --- | --- | --- |
| Below 60 | Up to ₹2,50,000 | 5% to ₹5,00,000; ₹12,500 + 20% above ₹5,00,000; ₹1,12,500 + 30% above ₹10,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| 60 or more but below 80 | Up to ₹3,00,000 | 5% to ₹5,00,000; ₹10,000 + 20% above ₹5,00,000; ₹1,10,000 + 30% above ₹10,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| 80 or more | Up to ₹5,00,000 | 20% to ₹10,00,000; ₹1,00,000 + 30% above ₹10,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |

### Rebate under old s.87A for AY 2026-27; current equivalent s.156 confirmed ([source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1))

| Regime | Maximum rebate | Condition |
| --- | --- | --- |
| New | ₹60,000 | Resident individual; taxable income does not exceed ₹12,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| Old | ₹12,500 | Resident individual; taxable income does not exceed ₹5,00,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |

- The rebate is "up to 100% of income tax subject to a maximum limit", so at ₹12,00,000 the new-regime tax of ₹60,000 is fully rebated and tax is nil. With the ₹75,000 standard deduction, a salaried resident with no other income pays nil up to a gross salary of ₹12,75,000.
- **Marginal relief just above ₹12,00,000 (new regime).** Where pre-rebate income tax exceeds the excess of total income over ₹12,00,000, apply the relief under s.87A, subject to the slab-tax cap, then calculate cess. For income taxed entirely at slab rates, the unrounded break-even is about ₹12,70,588. The ₹12,70,590 amount in the AY 2026-27 [ITR-1 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf) is a portal validation figure. [Finance Act 2025, s.20](https://egazette.gov.in/WriteReadData/2025/262125.pdf#page=23).
- The rebate is for residents only. The current s.156(3) and old 87A proviso inserted by Finance Act 2025 s.20 cap new-regime rebate to slab-rate tax. Specific capital-gain/special-rate computations remain referred; the income threshold alone does not rebate every type of tax. [current Act](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [oldamendment](https://egazette.gov.in/WriteReadData/2025/262125.pdf).

### Surcharge, cess and marginal relief ([source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1))

| Total income | New regime | Old regime |
| --- | --- | --- |
| Up to ₹50 lakh | Nil | Nil; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| Above ₹50 lakh to ₹1 crore | 10% | 10%; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| Above ₹1 crore to ₹2 crores | 15% | 15%; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| Above ₹2 crores to ₹5 crores | 25% | 25%; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| Above ₹5 crores | 25% | 37%; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |

- Surcharge on income under sections 111A, 112,112A and dividends is capped at 15%, except where taxed under 115 A, 115 AB, 115 AC, 115 ACA or 115 E.
- Marginal relief: income tax plus surcharge cannot exceed the income tax and any surcharge applicable at the relevant threshold by more than the excess income. Test the ₹50 lakh, ₹1 crore and ₹2 crore thresholds and, for the old regime, ₹5 crore. Calculate cess after the relief.
- Health and Education Cess of 4% is paid on income tax plus surcharge, in both regimes.

### Standard deduction and key deductions (AY 2026-27 rules) ([ITR-1 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf))

| Item | New regime | Old regime |
| --- | --- | --- |
| Standard deduction on salary, s.16(ia) | Up to ₹75,000 | Up to ₹50,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| Family pension deduction, s.57(iia) | 1/3 rd, maximum ₹25,000 | Lower of 1/3 rd or ₹15,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf |
| Employer NPS contribution, 80CCD(2) | Up to 14% of salary | 10% of salary (PSU or other employer); 14% (central or state government); https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| House property standard deduction | 30% of annual value | 30% of annual value; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |

Old regime only ([Salaried Individuals page, deductions](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)):

- 80C, 80CCC and 80CCD(1) together: ₹1,50,000. 80CCD(1 B), own NPS: ₹50,000 more.
- 80D health insurance: ₹25,000 for self, spouse and dependent children (₹50,000 if any of them is a senior citizen), and a separate parent pool with the applicable cap; preventive check-up ₹5,000 is aggregate within these limits, not extra for each pool. Obtain eligible payment and insurance/medical evidence; current-year complete conditions are above.
- 80TTA savings interest (non-senior): ₹10,000. 80TTB deposit interest (resident senior citizen): ₹50,000.
- Home-loan interest on self-occupied property, s.24(b): aggregate deduction capped at ₹2,00,000 for qualifying acquisition or construction borrowing from 1 April 1999, completed within 5 years from the end of the borrowing financial year, with a lender's interest certificate. The ordinary aggregate cap is ₹30,000. [Section 24](https://wm.incometaxindia.gov.in/w/section-24-64). Let-out property loss set off against other heads: ₹2,00,000, balance carried forward up to 8 assessment years against house-property income.
- HRA exemption under old 10(13A)is old-regime only: ITR 1 validation 165 requires new-regime allowance to be 0. [validation 165](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf).
- New regime keeps: 80CCD(2), 80CCH(2) government contribution only (not own 80CCH(1)); [ITR 2 validation rule 350](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT__e-Filing_ITR%202_Validation%20Rules_AY%202026-27_V1.0.pdf), and interest on a let-out property (but a house property loss cannot be set off or carried forward).

### Presumptive income: 44AD and 44ADA (AY 2026-27), s.58 (Tax Year 2026-27) ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

| Scheme | Who | Deemed profit | Turnover or receipts limit |
| --- | --- | --- | --- |
| 44AD business | Resident individual, resident HUF, resident firm (not LLP), in an eligible business | At least 6% of turnover received by account-payee cheque or draft, bank electronic clearing or prescribed electronic mode received during the year or before the s.139(1) due date for the older cycle (s.263(1) for current Tax Year); at least 8% of the rest | ₹3 crore if cash receipts do not exceed 5% of total gross receipts; ₹2 crores otherwise; https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| 44ADA profession | Resident individual or firm (not LLP) in a specified profession | At least 50% of gross receipts | ₹75 lakh if cash receipts do not exceed 5% of total gross receipts; ₹50 lakh otherwise; https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |

- The 6% and 8% rates, and the 50% rate, are minimums: the ITR-4 validation rules check that declared income is "more than or equal to" them ([ITR-4 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%204_Validation%20Rules_AY%202026-27.pdf)). Mixed receipts: 6% of the qualifying part plus 8% of the rest.
- The 6% receipt window is confirmed from old 44AD and current 58: qualifying receipt during the year or before the applicable original-return due date, not an unspecified date. Original conservative treatment of an unknown mode as 8% may be shown only as an estimate; do not invent a cash share or higher-limit eligibility. Obtain evidence before final classification. [old 44AD](https://www.incometaxindia.gov.in/documents/20117/11892059/Section%2B-%2B44AB_en_8cf1cc.pdf/2d0c4085-9682-5576-ee00-23985588b899?t=1765997029192&version=1.0); [current 58](https://egazette.gov.in/WriteReadData/2025/265620.pdf).
- 44AD does not cover: goods carriages (44AE), agency business, commission or brokerage income, or "a person who is required to maintain books of accounts as referred to in Section 44AA(1)" (the professions list).
- Specified professions for 44ADA: legal, medical, engineering or architectural, accountancy, technical consultancy, interior decoration, and any other profession notified by CBDT. 44ADA does not apply to a business.
- Once presumptive income is declared, no further business expenses are deductible; Chapter VI-A deductions still are (old regime).
- **Clients on actual profit (ITR-3) as well:** advance tax and self-assessment tax are a way of paying the tax, not a cost of the business. The return claims them as "Total Taxes Paid" (advance tax, TDS, TCS and self-assessment tax) against the tax ([ITR-3 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/CBDT_e-filing_ITR-3_Validation%20Rules_V1.0_AY%2026-27.pdf)); self-assessment tax "is merely a mode of discharging the tax liability" ([Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)). Record them as tax credits, never as expenses.
- Life insurance premium and provident fund (80C) and health insurance premium (80D) appear on the portal as Chapter VI-A deductions under "Tax deductions available to a taxpayer opting for the Old Tax Regime" ([Salaried Individuals page](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)). Treat them as old-regime deductions, not business expenses, in ITR-3 and ITR-4 alike; under the new regime they give no deduction.
- The old ITR 4 FAQ says an eligible 44ADAprofessional declaring at least 50% need not keep 44AAbooks; retain that as an older-cycle FAQ statement, subject to the profession and statutory books conditions, not a current blanket waiver. Current 58/62/63 must be applied independently.
- **Tax Year 2026-27:** s.58 consolidates the schemes; current rates/limits and full conditions are confirmed in the answer layer above. No fresh assumption based solely on older 44AD/44ADAfigures is needed.

### Regime choice ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

- No business or professional income: choose the regime each year in the return itself (ITR-1 or ITR-2, no form), but only in a return filed on or before the due date under s.139(1). The validation rules say: "Old Tax Regime cannot be selected after the due date of filing of return" ([ITR-1 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf)). A belated return is therefore taxed under the new regime.
- Older-cycle business/professional income: timely Form 10-IEA on or before s.139(1) due date opts out; a valid continuing earlier option does not require annual refiling. Withdrawal is once in a subsequent year; after withdrawal no new opt-out while business/profession income continues, with the cessation exception. Same-year revision/withdrawal of the form is barred. [Form 10-IEAFAQQ 7,12-21](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form10-iea).
- An employee must tell the employer the intended regime for TDS. Telling the employer is not the same as opting out; that is done in the return.
- **Tax Year 2026-27:** only a prior option in force immediately before commencement is saved under s.536(2)(f); current s.202(4)/rule 136 puts an option/withdrawal in the timely return, not an assumed replacement standalone form. The FAQ summarizes carryover ([objective and scope FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq), s.536(2)(f)). Rule 136 has now been read; final current-year utility fields remain unconfirmed. [rule 136](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

### Advance tax and interest ([Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq))

| Instalment (normal case) | Cumulative amount due | By |
| --- | --- | --- |
| First | 15% of tax liability | 15 June; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Second | 45% of tax liability, less advance tax already paid | 15 September; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Third | 75% of tax liability, less advance tax already paid | 15 December; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Fourth | 100% of tax liability, less advance tax already paid | 15 March; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- Source for the instalments: [ITR-1 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ).
- **Threshold:** under s.404 of the 2025 Act, advance tax is payable if tax for the year is "Rs. 10,000 or more", unchanged from the old Act. (The ITR-1 FAQ says "more than ₹ 10,000"; follow the statute wording quoted in the Tax Payments FAQ.) Estimate tax net of TDS.
- **Presumptive (old 44AD/44ADA; current 58(2)serial 1 or 3 only):** the whole advance tax is due in one instalment on or before 15 March (s.408(2)). Anything paid by 31 March counts as advance tax for that year. There is no such concession for 44AE.
- **Interest (Tax Year 2026-27, rates unchanged from the old Act):** s.424 (old 234B) 1% per month or part of a month where advance tax is not paid or is less than 90% of assessed tax; s.425 (old 234C) "1% or 3% for the specified period" for deferring instalments. s.405 gives a formula for the advance tax liability.
- **AY 2026-27 shortfalls** keep 234B and 234C of the 1961Act, even if the interest is levied after 1April 2026.
- Old 234A late-return interest remains a separate period-specific computation/referral; current 423 expressly uses 1% with its statutory base and month count. Ordinary current 425(2)/(3)construction remains held in `in-advance-tax`, so no final ordinary 425 amount is supplied here.
- Tax Year 2026-27 advance tax is paid under the 2025 Act: choose "Tax Year 2026-27" on the challan. Self-assessment tax for FY 2025-26 income is paid under the 1961Act selecting AY 2026-27 ([General Questions FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/General%20Questions-faqs)).

### Residence tests (same in both Acts) ([Non Resident FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq))

| Test | Rule |
| --- | --- |
| Basic | Resident if in India 182 days or more in the year, or 60 days or more in the year and 365 days or more in the four preceding years; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Citizen leaving for employment abroad or as crew of an Indian ship | For citizen employment/Indian-ship-crew departure the alternative 60 day limb is disabled; 182 day test remains, but separately test citizen deemed residence; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Visiting Indian citizen or person of Indian origin | 182 days inclusive meets the basic test. Visiting citizen/PIO alternative limb is disabled unless qualifying income strictly exceeds INR 1,500,000 (in words on the page), then 120 current AND 365 prior 4; actual foreign-source definition required; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Deemed resident | Citizen with income other than foreign-source income over₹15 lakh and not liable to tax in any OTHER country/territory by domicile,residence or similar criteria; current 6(8)disables this deeming if already resident under 6(2)-(6) (old 6(1A); current 6(7)-(8)); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Not ordinarily resident | Resident then RNOR if 9 of 10 prior NR OR 729 orlessprior 7; also qualifying 120-181 dayvisitor and citizen deemedresident routes (current 6(13)); historic lookbacks not reset; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- Residence is tested year by year. FY 2025-26 counts days to 31 March 2026 under the 1961Act; Tax Year 2026-27 uses the 2025 Act, with earlier years' days used for the look-back tests.
- The official FAQ visitor wording "more than182days" conflicts with inclusive enacted s.6. The statute controls: exactly 182 meets the basic residence limb. Confirm deemed-residence and RNOR separately, including for a citizen departing for employment. [s.6](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

### TDS, Form 26AS and AIS ([Tax Credit Mismatch FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/Tax%20Credit%20Mismatch%20-FAQ))

- Report the gross income and claim the TDS as a credit. The older portal says credit is restricted to 26AS, but this operational statement does not authorize charging the same tax again where it was actually deducted: current 401 protection and rule 203 evidence/assessability controls remain relevant. Refer missing credit with deduction proof; never invent a 26ASentry.
- Download AIS and Form 26AS before filing and match every TDS, TCS and challan. If TDS is missing, the deductor must file a revised TDS return. If a challan is missing, check the challan number and PAN; after filing, use a revised return only if legally available within the applicable 139(5)/263(5)revision window, or the applicable rectification remedy after intimation; 143(1)status alone does not extend a revision deadline.
- AIS shows more than TDS: SFT information, tax payments, demand and refund, and other information. Give feedback in AIS where a figure is wrong ([AIS FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ais%20-%20annual%20information%20statement-faqs)). AIS may not hold everything; the client must still report all income.
- **Tax Year 2026-27:** TDS on salary is under s.392 at payment. For s.393 provisions triggered by the earlier of credit or payment, a March 2026 credit followed by April payment remains under the 1961 Act. If the trigger is on or after 1 April 2026, use the current provisions. TCS is under s.394. AIS continues to AY 2026-27 and is replaced by Form No. 168 from Tax Year 2026-27. [Income-tax Act 2025, s.392](https://egazette.gov.in/WriteReadData/2025/265620.pdf#page=396).
- A nongovernment ordinary deductor generally deposits by 7 days after month-end, March by 30 April, but government/no-challan, special transaction forms and authorized quarterly payment exceptions require rule 218. Use in-tds-freelance rather than treating this as universal. [rule 218](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf). Interest: 1% per month or part for failure to deduct, 1.5% per month or part for failure to deposit (s.398(3)(a)). TDS rates and thresholds are in the s.393 tables; this skill does not restate them (check the table item before advising).

### Which ITR form (AY 2026-27) ([Salaried Individuals for AY 2026-27: returns and forms](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1))

| Form | Use when |
| --- | --- |
| ITR-1 (Sahaj) | Resident (not RNOR) individual; total income up to ₹50 lakh from salary or pension, up to two house properties, other sources, agricultural income up to ₹5,000, LTCG under s.112A up to ₹1,25,000; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1; https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ |
| ITR-4 (Sugam) | Resident (not RNOR) individual, HUF or firm (not LLP); total income up to ₹50 lakh with presumptive income under 44AD/44ADA/44AE plus the ITR-1 kinds of income. Optional; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1; https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| ITR-2 | Individual or HUF with no business or profession income who cannot use ITR-1; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |
| ITR-3 | Individual or HUF with business or profession income who cannot use ITR-1, ITR-2 or ITR-4; https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 |

- ITR-1 and ITR-4 are barred for a company director, anyone with short-term capital gains, s.112A gains above ₹1,25,000, unlisted shares held in the year, foreign assets, foreign signing authority or foreign income, deferred tax on start-up ESOPs, or any brought-forward loss or loss to carry forward. ITR-1 is also barred where TDS was deducted under s.194 N.
- From AY 2026-27, ITR-1 and ITR-4 accept up to two house properties ([ITR-1 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ)).
- Current rule 164 is notified and confirms ITReligibility, all exclusions and verification modes. Final utility fields remain unconfirmed. The defective 164(6)(l)cross-reference and 164(2)(d)/164(3)(n)ITR 1 and 164(5)/164(6)(o)ITR 4 gainpermission/special-rate interactions require resolution before applying ITR1orITR4to the affected gain cases. [rule 164](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

### Boundary and exception table ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

| Boundary | Inside | Outside |
| --- | --- | --- |
| New-regime rebate | Total income does not exceed ₹12,00,000: rebate up to ₹60,000, subject to the slab-tax cap | Above: apply the statutory marginal relief test using total income and the slab-tax cap; https://egazette.gov.in/WriteReadData/2025/262125.pdf#page=23 |
| Old-regime rebate | Total income does not exceed ₹5,00,000 | Above: no rebate; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| 44AD limit | Turnover up to ₹3 crore if cash receipts are 5% or less of gross receipts | Otherwise ₹2 crores; above the limit, 44AD is not available; https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| 44ADA limit | Receipts up to ₹75 lakh if cash receipts are 5% or less of gross receipts | Otherwise ₹50 lakh; above, compute actual profit (ITR-3); https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Advance tax | Advance tax payable of ₹10,000 or more after statutory reductions, subject to the resident senior exemption | Below: no advance tax; https://egazette.gov.in/WriteReadData/2025/265620.pdf#page=432 |
| ITR-1 / ITR-4 | Total income up to ₹50 lakh | Above: ITR-2 or ITR-3; https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Residence, basic test | 182 days or more | 181 days or fewer (then the 60/365 limb); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Visiting citizen or PIO | 182 days inclusive, or qualifying 120/365 limb | Below 182 doesnotsettle NRwithoutalternative/deemedtests; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Late fee (s.234F; s.428 from Tax Year 2026-27) | ₹1,000 if total income does not exceed ₹5 lakh | ₹5,000 in any other case; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Revised return fee (old 234-I, AY 2026-27) | HOLD: portal says after 31 December 2026 | Enacted wording instead says beyond 9 months/before 12 months from ASSESSMENT-year end; 1,000/5,000 income-based amounts are confirmed, operative date conflict unresolved; no filing calculation from portal date; https://egazette.gov.in/WriteReadData/2026/271439.pdf; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/CBDT_e-filing_ITR-3_Validation%20Rules_V1.0_AY%2026-27.pdf |
| Old regime in older-cycle return | Nonbusiness timely 139(1)return; business valid continuing earlier option or timely Form 10-IEA | Do not invalidate a continuing business option just because current return is late; nonbusiness late return cannot newly opt out; https://egazette.gov.in/WriteReadData/2025/265620.pdf; https://www.incometax.gov.in/iec/foportal/newformpage/forms/form10-iea |
| Losses | Apply relevant timely-loss-return provision | Ordinary business/capital-loss carryforward may be lost; house-property and unabsorbed-depreciation rules are separate; no blanket forfeiture; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### AY 2026-27 returns (FY 2025-26), filed in 2026 ([Income Tax Returns FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq))

As at 22 November 2026, these returns use the Income-tax Act, 1961 and the AY 2026-27 forms. Select AY 2026-27 on the portal and use the older-cycle rates above.

| Return | Due date or time limit |
| --- | --- |
| Original return, non-audit | "31st July, 2026 or 31st August for non-audit cases, etc." ITR-4: 31August 2026 ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)). Finance Act 2026 s.5 nowconfirms full categories: business/profession no required audit 31August; partner of non-audit firm and corresponding spouse where old 5 Aapportionment applies also 31August; other ordinary nonbusiness 31 July; earlier company/required-audit/partner/spouse/TP categories control; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Tax audit report, serial 2 cases | 21 October 2026 under CBDT Circular 07/2026, extended from 30 September 2026; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-09/Circular-7-2026.pdf |
| Original return, serial 2 audit and related cases | 21 November 2026 under CBDT Circular 07/2026, extended from 31 October 2026. For the covered taxpayers, apply the extended date when assessing whether the original return is belated; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-09/Circular-7-2026.pdf |
| Transfer pricing case | 30 November 2026 (report by 31 October 2026); https://egazette.gov.in/WriteReadData/2026/271439.pdf; https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq |
| Belated return, s.139(4) | By 31 December 2026, or before assessment is complete if earlier; fee under s.234F; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Revised return, s.139(5) | By the end of 31 March 2027, or before assessment is complete if earlier; old 234-I fee date held for the enacted/portal conflict below; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Updated return (ITR-U), s.139(8 A) | Within the s.139(8 A) time limits, even after 1April 2026; additional tax applies; https://egazette.gov.in/WriteReadData/2026/271439.pdf |

- On 22 November 2026, the general July and August deadlines and the extended serial 2 deadline have passed. For a taxpayer whose own deadline has passed, check belated filing, the section 234F fee and any section 234A interest. Check any continuing valid business regime option, the timely-return rules for business or capital losses, and the separate rules for house-property loss and unabsorbed depreciation.
- Portal validation for AY 2026-27: if the original return was belated, a revised return cannot choose the old regime; and the regime cannot be changed in a revised return filed after the original due date ([ITR-1 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf); [ITR-3 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/CBDT_e-filing_ITR-3_Validation%20Rules_V1.0_AY%2026-27.pdf)).
- The ordinary belated/revised window for AY 2025-26 andearlier has expired. Updated-return eligibility/additional tax, notice responses and possible condonation require review; do not promise ITR-Uas the only universal remedy.
- 234B/234C interest for FY 2025-26 advance tax stays under the 1961Act.
- **Tax Year 2026-27 time limits under s.263 of the 2025 Act:** belated return within 9 months from the end of the tax year; revised return within 12 months from the end of the tax year, and updated return within 48 months from the end of the financial year after the tax year (now confirmed by enacted Finance Act 2026, not a proposed Bill). Additional tax on an updated return is under s.267. The enacted current 263(1)(c)table gives 31 July/31August/31 October/30 November 2027 by category, with fullrequired-audit/partner/spouse/s.172 conditions, not a universal Julydeadline. [Finance Act 2026 s.66](https://egazette.gov.in/WriteReadData/2026/271439.pdf).

**Unresolved old 234-I date conflict, with arithmetic.** Finance Act 2026 s.16 says revised return beyond 9 months but before 12 months from the end of the relevant **assessment year**. AY 2026-27 ends 31 March 2027; literal 9/12 month dates are 31 December 2027/31 March 2028 (derived). The actual ITR 3 validation rules 990-991 instead say after 31 December 2026, whereas amended 139(5)ordinary revision ends 31 March 2027 or earlier completed assessment. These cannot be reconciled by silently changing assessment year to financial year. Official Gazette and relevant FAQ were opened and a search for official corrective text did not establish a correction. Preserve the old portal date only as a disputed statement; exact old 234-I fee timing is **Not yet confirmed**, so hold this fee calculation. Current 428(b) expressly measures from tax-year end and has no such wording conflict. [Finance Act 2026 ss.5,16,96](https://egazette.gov.in/WriteReadData/2026/271439.pdf); [ITR 3 validation 990-991](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/CBDT_e-filing_ITR-3_Validation%20Rules_V1.0_AY%2026-27.pdf);[Returns FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq).

## Worked cases

All cases: resident individual below 60, AY 2026-27 slab figures, no other income unless stated. Current s.202 confirms the same slab inputs; keep these 6 originalcases labelled older-cycle, with current rules independently stated above.

1. **Salaried, new regime, zero tax.** Gross salary ₹12,75,000. Standard deduction ₹75,000. Total income ₹12,00,000. Tax: ₹20,000 + 10% of ₹4,00,000 = ₹60,000. Rebate ₹60,000. Tax payable nil. Cess nil.
2. **Salaried, new regime, above the rebate.** Gross salary ₹16,75,000. Total income ₹16,00,000. Tax: ₹60,000 + 15% of ₹4,00,000 = ₹1,20,000. No rebate. Cess at 4% ₹4,800. Total ₹1,24,800, less TDS in Form 26AS.
3. **Marginal relief.** Freelancer, total income ₹12,10,000, new regime. Slab tax: ₹60,000 + 15% of ₹10,000 = ₹61,500. Income above ₹12,00,000 is ₹10,000, so tax is limited to ₹10,000 and the rebate is ₹51,500. Cess ₹400. Total ₹10,400.
4. **44ADA consultant.** Receipts ₹40,00,000, all by bank transfer, so cash is below 5% and the ₹75 lakh limit applies. Deemed profit at 50%: ₹20,00,000. New regime tax: ₹1,20,000 + 20% of ₹4,00,000 = ₹2,00,000. Cess ₹8,000. Total ₹2,08,000. Advance tax: all of it by 15 March, net of any TDS.
5. **44AD trader with cash.** Turnover ₹1,00,00,000: ₹90,00,000 received electronically during the year or before the s.139(1) due date for the older cycle (s.263(1) for current Tax Year), ₹10,00,000 in cash. Cash is 10% of receipts, more than 5%, so the limit is ₹2 crores; the trader is inside it. Deemed profit: 6% of ₹90,00,000 = ₹5,40,000, plus 8% of ₹10,00,000 = ₹80,000, total ₹6,20,000. New regime tax: 5% of ₹2,20,000 = ₹11,000. Rebate ₹11,000. Tax nil. Had turnover been ₹2,50,00,000 with the same cash share, 44AD would not be available.
6. **Late AY 2026-27 return.** Salaried client, total income ₹9,00,000, never filed, files ITR-1 on 1 October 2026. The return is belated (s.139(4)); it must use the new regime; late fee ₹5,000 because total income exceeds ₹5 lakh. New regime tax: ₹20,000 + 10% of ₹1,00,000 = ₹30,000, fully rebated. Fee ₹5,000 is still payable.

### Recomputing checks for the six preserved cases

All example inputs are hypothetical; outputs are derived. These cases have no special-rate income or surcharge. Case 2 adds a documented eligible 80C deduction and assumes timely valid old-regime choice solely for the comparison: new 124,800 versus old 265,200, so new saves 140,400. It does not assume every client has that deduction. Case 4 assumes no TDS/othercredits for its advance figure. Case 6 assumes a required return, no applicable extension, and no qualifying timely old-regime choice. Sources for all slab/rebate/fee inputs are the older tables and the actually opened current counterparts above; current 425 interest is not finalized by these examples.

#### Check 1

```oa-check
name: India preserved income-tax case 1
inputs:
  salary: 1275000
  deduction: 75000
  zero: 400000
  width: 400000
  r1: 0.05
  r2: 0.1
  rebate_cap: 60000
  cess: 0.04
steps:
  income: salary-deduction
  tax: width*r1+(income-zero-width)*r2
  rebate: min(tax,rebate_cap)
  after: tax-rebate
  total: after*(1+cess)
expected:
  income: 1200000
  tax: 60000
  rebate: 60000
  total: 0
```

#### Check 2

```oa-check
name: India preserved income-tax case 2
inputs:
  salary: 1675000
  new_ded: 75000
  old_ded: 50000
  eligible_80c: 150000
  new_base: 60000
  new_start: 1200000
  new_rate: 0.15
  old_base: 112500
  old_start: 1000000
  old_rate: 0.3
  cess: 0.04
steps:
  new_income: salary-new_ded
  new_tax: new_base+(new_income-new_start)*new_rate
  new_total: new_tax*(1+cess)
  old_income: salary-old_ded-eligible_80c
  old_tax: old_base+(old_income-old_start)*old_rate
  old_total: old_tax*(1+cess)
  saving: old_total-new_total
expected:
  new_income: 1600000
  new_total: 124800
  old_income: 1475000
  old_total: 265200
  saving: 140400
```

#### Check 3

```oa-check
name: India preserved income-tax case 3
inputs:
  income: 1210000
  threshold: 1200000
  base: 60000
  rate: 0.15
  cess: 0.04
steps:
  tax: base+(income-threshold)*rate
  excess: income-threshold
  relief: max(0,tax-excess)
  after: tax-relief
  total: after*(1+cess)
expected:
  tax: 61500
  relief: 51500
  after: 10000
  total: 10400
```

#### Check 4

```oa-check
name: India preserved income-tax case 4
inputs:
  receipts: 4000000
  profit_rate: 0.5
  start: 1600000
  base: 120000
  rate: 0.2
  cess: 0.04
  tds: 0
steps:
  profit: receipts*profit_rate
  tax: base+(profit-start)*rate
  total: tax*(1+cess)
  advance: total-tds
expected:
  profit: 2000000
  tax: 200000
  total: 208000
  advance: 208000
```

#### Check 5

```oa-check
name: India preserved income-tax case 5
inputs:
  bank: 9000000
  cash: 1000000
  bank_rate: 0.06
  cash_rate: 0.08
  zero: 400000
  rate: 0.05
  rebate_cap: 60000
steps:
  turnover: bank+cash
  cash_percent: cash/turnover*100
  profit: bank*bank_rate+cash*cash_rate
  tax: (profit-zero)*rate
  rebate: min(tax,rebate_cap)
  total: tax-rebate
expected:
  turnover: 10000000
  cash_percent: 10
  profit: 620000
  tax: 11000
  rebate: 11000
  total: 0
```

#### Check 6

```oa-check
name: India preserved income-tax case 6
inputs:
  income: 900000
  base: 20000
  start: 800000
  rate: 0.1
  rebate_cap: 60000
  late_fee: 5000
steps:
  tax: base+(income-start)*rate
  rebate: min(tax,rebate_cap)
  cash: tax-rebate+late_fee
expected:
  tax: 30000
  rebate: 30000
  cash: 5000
```

## When to refuse or refer

Sources: [Non Resident FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq) and [objective and scope FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq).

- Non-resident, RNOR or deemed-resident client, or a year where the day count is close to 182 or 120: refer.
- Capital gains other than s.112A gains within the ITR-1/ITR-4 limit, virtual digital assets, lottery or special-rate income: refer.
- Foreign income/assets/treaty relief: refer to `in-cross-border-india-dual-resident-treaty`. Older Form 67 deadline was amended by Notification 100/2022 to AYend for 139(1)/(4)returns and byfilingdate forupdatedreturnincludedincome; current Form 44/rule 76 has a separate deadline. Do not repeat the superseded original 139(1)deadline.
- Turnover or receipts above the presumptive limits, profit declared below the presumptive rate, or a client who has moved in and out of 44AD: refer for books, audit and re-entry rules not covered here.
- Any tax audit case, transfer pricing, firm, LLP, company or trust: refer.
- Money or assets passed to a spouse or minor child, or a spouse or minor child earning from the client's business or assets: refer. Whether that income is added to the client's own (clubbing) is not covered here.
- Pending notice, scrutiny, reassessment or search: refer. Proceedings for AY 2026-27 and earlier stay under the 1961Act (s.536(2)(c)).
- Income above ₹50 lakh: compute surcharge and marginal relief carefully and have it checked ([surcharge table](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)).
- Never present an unsupported or held computation as final. Current core rates/limits are confirmed from enacted law; exact portal fields/extensions/specialcase computations remain referrals.

## Filing and payment

- Pay by e-Pay Tax on the portal: net banking, debit card, payment gateway (including credit card and UPI), NEFT/RTGS mandate, or over the counter where allowed ([General Questions FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/General%20Questions-faqs)). A generated challan generally expires 15 days after the CRN is created. For advance tax, observe the earlier of that date and the 31 March cut-off. Instalment due dates still apply. [Know your Payment Status FAQ, question 3](https://www.incometax.gov.in/iec/foportal/help/know-payment-status-faq).
- Choose the Act and year on the challan: AY 2026-27 (1961Act) for FY 2025-26 self-assessment tax; Tax Year 2026-27 (2025 Act) for current advance tax. A wrong year means the credit lands in the wrong year.
- Self-assessment tax for AY 2026-27 is under s.140 A of the 1961Act: pay it, enter the challan in the return, then file.
- Older-cycle returns: file on the e-Filing portal; use the applicable permitted route such as Aadhaar OTP, EVC/net banking or digital signature, or send signed ITR-V by speed post to CPC Bengaluru within30days as ITR1FAQ Q7describes for the postal route. E-VerifyFAQ Q2lists the electronic modes; Q16limits DSCto immediate verification rather than Verify Later. [e-VerifyFAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-verify). Confirm the applicable permitted mode and current official postal address before sending. Current-year verification is category-dependent under rule 164, not universally paper-permitted. No documents are attached; keep them for any enquiry.
- Late fee: s.234F for AY 2026-27 (₹1,000 or ₹5,000); s.428 of the 2025 Act from Tax Year 2026-27, same amounts.
- Keep FY 2025-26 and FY 2026-27 records, TDS and challans separate. Reconcile AY 2026-27 with Form 26AS and use the applicable current statements, including Form 168, for Tax Year 2026-27.

## Completion checklist

- [ ] Year and Act fixed: Tax Year 2026-27 (2025 Act) or AY 2026-27 (1961Act).
- [ ] Residential status tested with day counts; resident and not RNOR.
- [ ] All receipts reconciled to source evidence; gross TDS income supported; loans/transfers distinguished; refund principal separated from interest/recoveries and uncertain treatment referred.
- [ ] Presumptive eligibility checked: business type, limit, cash share of 5% or less for the higher limit, 6%/8% split by mode and date, 50% for professions.
- [ ] Regime compared; correct period-specific timely option or valid saved/continuing business option, with one-time withdrawal/cessation conditions checked.
- [ ] Standard deduction applied (₹75,000 new, ₹50,000 old).
- [ ] Rebate checked for residents, including marginal relief above ₹12,00,000.
- [ ] Surcharge and marginal relief checked above ₹50 lakh; cess at 4% on tax plus surcharge.
- [ ] TDS/TCSmatched to statement and correct income year; missing deduction substantiated/referred, s.401 protection preserved, no fabricated credit.
- [ ] Advance tax and period-specific interest checked; current 425 construction held where unresolved, not marked finalized. Only eligible presumptive serial 1/3 clients use 15 March whole-payment schedule.
- [ ] Correct ITR form; due date and any late fee checked; return e-verified.
- [ ] Every held item resolved by applicable official guidance or referred before filing; no unsupported current utility/extension/old 234-I fee date used.

## Sources

| Official source | Read for | Actual read date |
|---|---|---|
| https://egazette.gov.in/WriteReadData/2025/265620.pdf | Read for ss.1,3,5-6; salary 19(1)Table; 22 whole; 58 whole; 62(4)/63; 93(1)(d); 109-110; 123-126; 153/156/202 whole; 263(1),(4)-(6)/266(1)-(3); 393(1)serial 6/8 Notes and 393(4)-(11), 395-402 relevant TDS sections; 403-410/423-425 whole; 428; 516 whole; 536(2)(c)/(f); Schedule III Table 11. Schedule XV investment rows not individually confirmed here | 2026-11-14 |
| https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read for individual tax/surcharge/cess s.3(1)-(5),(15), First Schedule I-B Para A/F; ss.5,16 whole(old 139/234-I date conflict), 40,56,66-67,84-90,93-96,111. Not all corporate/nonresident tables | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | Read for rules 47,136,164 whole; 203,213,215,218,219,245 whole; 75-76 FTC. Current final utility fields not inferred | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 | Read for age/slab/rebate/surcharge/relief tables and relevant salary/pension/NPS/80C/D/TTA/TTB/HRA/house-property deductions, forms and exclusions; older 2025-2026 filing cycle, not every unrelated deduction | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs | Read for Q 1-18/22: old 44AD/ADAeligibility/exclusions, limits/rates/books, regime, advance and due date | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf | Read for rules 1-17/23-29,54(oldfamily15,000),151(late old-regime selection),165(new-regime HRAzero),189-192,214-216 andneighbors: olddeductions/fee/credit, late-regime restriction, 1,270,590 rebate limit, family pension/salary/NPS. Not all utility rules | 2026-11-15 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT__e-Filing_ITR%202_Validation%20Rules_AY%202026-27_V1.0.pdf | Read for rule 350 andneighbors: own 80CCH(1)excluded from new regime, employer NPS limits/combineddeductions; not all 51 pages | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%204_Validation%20Rules_AY%202026-27.pdf | Read for rules 5-17 presumptive minima/exclusions, oldercycle | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/CBDT_e-filing_ITR-3_Validation%20Rules_V1.0_AY%2026-27.pdf | Read for rules 36(regime revision),971(taxes-paid sum),990-991(disputed 234-I date), and neighboring 962-1002 tax/credit/fee controls; reread 15 November 2026; older cycle, not entire 73 page document | 2026-11-15 |
| https://www.incometaxindia.gov.in/documents/20117/11892059/Section%2B-%2B44AB_en_8cf1cc.pdf/2d0c4085-9682-5576-ee00-23985588b899?t=1765997029192&version=1.0 | Read for 44AB p 1/44ADA p 4/44AD p 5 whole: cash thresholds/eligible groups/receipt window/exclusions/lockout/books; older Act | 2026-11-14 |
| https://www.incometaxindia.gov.in/documents/20117/6507196/Circular03_2017.pdf/a8f0575d-1a05-5bb9-6842-b893a95ac1eb?t=1762868214545 | Read for paras 51.1-51.3 andneighbor 50.3-50.4/52: old 24 completion period 5 years, qualifying loan date/purpose and effective AY 2017-18 onward; not full 79 pages | 2026-11-14 |
| https://egazette.gov.in/WriteReadData/2025/262125.pdf | Read for Finance Act 2025 s.20 old 87Aslab-tax cap and amended rebate, not every provision | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/newformpage/forms/form10-iea | Read for Q 7-8/12-21: continuing option/noannualrefile/withdrawal/cessation/same-year restriction | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq | Read for Q 3-6/14-23: yeartransition/threshold/schedules/credits/168 | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/General%20Questions-faqs | Read for Q 1-17: Act/year, CRNexpiry 15 days, modes/paymentreceipt and visibility | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq | Read for Q 1-25 residence/deemed/RNOR/source-scope/FTC overview. Visitor greater-than 182 wording corrected by inclusive statute | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/Tax%20Credit%20Mismatch%20-FAQ | Read for all 4 questions: 26AS/challan PAN/deductorcorrection/rectification; operational 26AS statement qualified by current 401 | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ais%20-%20annual%20information%20statement-faqs | Read for Q 2-14: AIS/TIS/26ASscope/feedback/download/ack and incompleteness | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ | Read for Q 5-15/18-19: forms/twohouses/grossincome/30 dayverification/regimes/revision; oldercycle | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq | Read for Q 7-12/24-27: returns/fees/periods; old 234-I portal date disputed, proposed Bill language superseded by enacted Gazette | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq | Read for Q 2/21-26: repeal, year, regime and savings; not a substitute for operative law | 2026-11-14 |
| https://egazette.gov.in/WriteReadData/2022/238191.pdf | Read for entire English Notification 100/2022 p 2: Form 67 amended deadlines effective 1April 2022 | 2026-11-14 |

| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-verify | Read for Q1-16including electronic modes/prevalidated EVC/mobile prerequisites,30day verification/condonation and immediate-only DSC; actual older-Act portal guidance, not a blanket current164mode permission | 2026-11-15 |

| Notified Rules 2026, targeted reread | Read for rule 164(1)-(12), including fifty-lakh wording, and rules 203, 215, 219 and 245 in full: identifiers are separate rule references, not an amount | 2026-11-16; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| ITR 1 AY 2026-27 validation, targeted reread | Read for rules 189-192 and adjacent regime-selection controls. Rule 191 contains a ₹12,70,590 portal validation figure. Apply section 87A for the statutory calculation | 2026-11-24; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%201_Validation%20Rules_AY%202026-27.pdf |

| Income-tax Act 2025 Gazette, targeted reread | Read for section 6 in full and section 58 in full, especially the fifteen-lakh visitor limit and the two/three-crore and fifty/seventy-five-lakh presumptive limits printed in words; no exception or eligibility change | 2026-11-16; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-09/Circular-7-2026.pdf | AY 2026-27 extension for section 139(1) Explanation 2, serial 2 returns and associated audit reports | 2026-11-24 |
| https://wm.incometaxindia.gov.in/w/section-24-64 | Section 24(b), old-cycle home-loan interest caps, qualifying loan and completion dates and lender certificate | 2026-11-24 |
| https://www.incometax.gov.in/iec/foportal/help/know-payment-status-faq | Question 3, challan validity and advance-tax year-end cut-off | 2026-11-24 |

**Not yet confirmed:** old 234-I assessment-year/portal date conflict and any authoritative correction; current rule 164(6)(l)defective cross-reference, ITR 1(2)(d)/(3)(n)and ITR 4(5)/(6)(o)gain interactions; final TY 2026-27 ITR utility fields and verification screens; actual extensions applicable to a filing; ordinary current 425(2)/(3)construction held in in-advance-tax; case-specific older 24 certificate/other eligibility and Schedule XV investment conditions; exact notified professions beyond 62(4), special-rate tax, audit/lockout/loss exceptions and prior option validity, missing-credit procedure and inoperative PAN consequences. Keep these out of final filing instructions until resolved or professionally reviewed. Older forms/validation and all 6 old cases explicitly remain the 2025-2026 filing cycle. No current rate is inferred solely from an older portal table.
