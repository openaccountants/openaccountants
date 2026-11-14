---
name: us-form-1041-trust-and-estate-income
description: Prepare Form 1041, the US income tax return for estates and non-grantor trusts, for tax year 2026. 2026 figures from Rev. Proc. 2025-32, including the compressed trust brackets (37% above USD 16,000), the 0% and 15% capital gain bands (USD 3,300 and USD 16,250), the 3.8% net investment income tax above USD 16,000, the AMT exemption of USD 31,400 and the USD 5,300 qualified disability trust exemption. Covers who must file, calendar or fiscal year, DNI under section 643(a), simple and complex trust distribution deductions (sections 651 and 661), the 65-day election under section 663(b), the section 645 election to combine a revocable trust with the estate, income in respect of a decedent and the section 691(c) deduction, the section 642(g) choice between Form 706 and Form 1041, Schedule K-1, estimated tax and ESBTs in outline. Trigger on "Form 1041", "trust tax return", "estate income tax", "DNI", "65-day rule", "section 645", "K-1 from a trust", "IRD". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: estate-wealth-tax
type: computation
---

# US Form 1041, income tax of estates and trusts, tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32 (2026 inflation amounts), the 2025 Form 1041, its 2025 instructions (the latest published; they also give the 2026 estimated tax rule) and 26 U.S.C. 642, 644, 645, 651, 661, 663, 1411, 6012, 6072 and 6654, with Public Law 119-21 section 70110 for section 67(g), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, income kept in an estate or trust is taxed at 10%, 24%, 35% and **37% above USD 16,000** of taxable income. Qualified dividends and long-term gains are taxed at 0% up to **USD 3,300**, 15% up to **USD 16,250** and 20% above. The 3.8% net investment income tax applies to the lesser of undistributed net investment income and adjusted gross income above **USD 16,000**. Income paid out to beneficiaries (up to DNI) is deducted by the trust and taxed to them on their own returns through Schedule K-1, so distribution, including within 65 days after year end under section 663(b), is the main planning lever. A calendar-year 2026 Form 1041 is due **15 April 2027**; Form 7004 extends it 5 1/2 months.

## Scope and who this is for

In scope, for tax year 2026:

- **A decedent's estate**, from the date of death until administration ends.
- **Irrevocable trusts** (lifetime or under a will) that are not grantor trusts under sections 671 to 679.
- **Revocable living trusts after the grantor's death**, when they become irrevocable.
- **Section 645 filings** combining a qualified revocable trust with the estate on one return.

Out of scope, and where it goes:

| Topic | Where it goes |
| --- | --- |
| Estate tax on the value at death (Form 706), gift tax (Form 709), GST tax, the estate side of DSUE, basis at death | `us-estate-gift-706-709` |
| Grantor trust income (taxed on the grantor's Form 1040); only the filing options are covered below | `us-form-1040-individual-return` |
| ESBT computation in detail (overview below) | Refer |
| Charitable remainder trusts (section 664, Form 5227), split-interest and section 4947(a)(1) trusts, pooled income funds | Refer; `us-charitable-giving-strategies` for planning |
| Foreign trusts (Forms 3520, 3520-A) | `us-foreign-trust-reporting` |
| Bankruptcy estates of individuals (section 1398) | Refer |
| Common trust funds (section 584) | Refer |
| QBI deduction thresholds and phase-in for 2026 | `us-qbi-deduction` |
| Net operating loss computation | `us-net-operating-loss-172` |
| Estimated tax safe harbours in detail | `us-quarterly-estimated-tax` |
| State fiduciary income tax and trust residency | The state's income tax skill |

Charitable lead trusts, QPRTs, GRATs during the grantor's life and ILITs during the insured's life are usually grantor trusts; check before preparing a 1041.

## Ask the client first

1. **What is the entity?** Estate, trust created during life, trust under a will, or a revocable trust that became irrevocable at death. Get the will or trust instrument.
2. **Date of death** (for estates and former revocable trusts), and the year end chosen or wanted.
3. **Does the instrument require all income to be paid out currently?** Does it allow charitable gifts or principal (corpus) distributions? How does it, or state principal and income law, allocate capital gains?
4. **Every distribution made in 2026 and in the first 65 days of 2027**, by date, beneficiary and amount, and each beneficiary's expected marginal rate.
5. **Income by character**: interest, ordinary and qualified dividends, tax-exempt interest, short and long-term gains, rents, royalties, business income, IRD items (unpaid wages, IRA distributions, accrued interest).
6. **Expenses**: trustee or executor fees, legal and accounting fees, investment advisory fees, taxes, and how the trustee allocates each between income and principal.
7. **Was a Form 706 filed or required?** Estate tax paid, and IRD included in the gross estate (for section 691(c)).
8. **EIN** for the estate and for the trust; Forms 1099 received under the decedent's SSN versus the new EIN.
9. **Estimated tax paid** for 2026 and whether any should be passed to beneficiaries (Form 1041-T).
10. **S corporation stock** held (QSST or ESBT election made?), foreign accounts, nonresident alien beneficiaries.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Ordinary rates, estates and trusts (Table 5): not over USD 3,300 at 10%; over USD 3,300 to USD 11,700, USD 330 plus 24%; over USD 11,700 to USD 16,000, USD 2,346 plus 35% | 10%, 24%, 35% | [Rev. Proc. 2025-32, section 3.01, Table 5](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Top rate: over USD 16,000, USD 3,851 plus 37% of the excess | 37% above USD 16,000 | [Rev. Proc. 2025-32, section 3.01, Table 5](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum zero rate amount for qualified dividends and net capital gain, estates and trusts | USD 3,300 | [Rev. Proc. 2025-32, section 3.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum 15% rate amount, estates and trusts (20% above) | USD 16,250 | [Rev. Proc. 2025-32, section 3.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Net investment income tax: 3.8% of the lesser of undistributed net investment income and AGI (section 67(e)) above the start of the top bracket (USD 16,000 for 2026) | 3.8% | [26 U.S.C. 1411(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| Exemption (section 642(b)): estate USD 600; trust required to distribute all income USD 300; other trusts USD 100 | USD 600 / 300 / 100 | [26 U.S.C. 642(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec642.htm) |
| Qualified disability trust exemption (section 642(b)(2)(C)(i)) | USD 5,300 | [Rev. Proc. 2025-32, section 3.35](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT exemption, estates and trusts (section 55(d)(1)) | USD 31,400 | [Rev. Proc. 2025-32, section 3.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT exemption phase-out, estates and trusts: begins / complete | USD 104,800 / USD 167,600 | [Rev. Proc. 2025-32, section 3.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Filing threshold: estate with gross income of USD 600 or more; trust with any taxable income or gross income of USD 600 or more; any estate or trust with a nonresident alien beneficiary | USD 600 | [26 U.S.C. 6012(a)(3) to (5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartB-sec6012.htm) |
| Due date: 15th day of the 4th month after year end (15 April 2027 for calendar 2026) | 15 April 2027 | [26 U.S.C. 6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) |
| Extension on Form 7004 (to 30 September 2027 for calendar 2026) | 5 1/2 months | [Instructions for Form 1041 (2025), Extension of Time To File](https://www.irs.gov/pub/irs-pdf/i1041.pdf) |
| 65-day election window (section 663(b)): for calendar 2026, distributions through 6 March 2027 | 65 days | [26 U.S.C. 663(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartC-sec663.htm) |
| Estimated tax required if at least USD 1,000 of tax is expected after withholding and credits; estates exempt for years ending before 2 years after death | USD 1,000 | [Instructions for Form 1041 (2025), Estimated Tax](https://www.irs.gov/pub/irs-pdf/i1041.pdf) |

### Step 1. Who files, and the year

- **Estate**: files for the year of death (a short year from the date of death) and every later year until it closes, when gross income is USD 600 or more or any beneficiary is a nonresident alien. Almost every estate holding investments for a few months must file.
- **Trust**: files when it has any taxable income, gross income of USD 600 or more, or a nonresident alien beneficiary. Two or more trusts with substantially the same grantors and beneficiaries, formed mainly to avoid tax, are treated as one (section 643(f), for contributions after 1 March 1984).
- **Closing an estate**: a facts-and-circumstances point, not an IRS event. The practical marker is the final distribution of the residue, a final 1041 marked "Final return" and final K-1s. Administration kept open only to defer tax may be treated as ended (Treas. Reg. 1.641(b)-3(a)), with income then taxed to the beneficiaries.
- **Year end**: an estate may choose a calendar year or a fiscal year ending on the last day of any month, provided the first year is no longer than 12 months; it is chosen by filing the first return, and a later change needs Form 1128 and consent (section 442). The usual choice is the month end just before the month of death, which gives the longest first year. A trust must use the calendar year (section 644), except tax-exempt and section 4947(a)(1) trusts; a former revocable trust gets a fiscal year only through the section 645 election.
- **Why fiscal years help an estate**: a beneficiary reports K-1 income in the beneficiary's year that includes the estate's year end. An estate with a year ending 31 May 2027 issues K-1s that go on the beneficiaries' 2027 returns, filed in 2028. A fiscal year also lets a large gain be timed into a beneficiary's lower-income year, and the 65-day rule runs from the fiscal year end.
- **Short years**: the first and final returns are short years. Income is not annualised; the normal rate table applies.

### Step 2. Grantor trusts: the filing options

A grantor trust's income is taxed to the grantor (sections 671 to 679). The trustee may (Treas. Reg. 1.671-4): (1) file no 1041 where the trust uses the grantor's SSN and payers report to the grantor (most revocable trusts during life); (2) file a Form 1041 with only the entity information, the "Grantor type trust" box checked and an attached grantor statement showing each item by character; or (3) use an optional method, issuing Forms 1099 in the trust's name instead of a 1041. Assignment of wages to a trust does not move the income: salaries stay on the earner's return. At the grantor's death the revocable trust becomes a non-grantor trust and files its own 1041 (or joins the estate under section 645).

### Step 3. EIN and the split at death

Every estate and non-grantor trust needs its own EIN (Form SS-4 or online); the executor or trustee is the responsible party. A trust that was a qualified revocable trust must get a new TIN after the death whether or not section 645 is elected. Give payers Form W-9 with the new number. In the year of death, income to the date of death goes on the decedent's final Form 1040 and income after it on the 1041; where a Form 1099 mixes the two, report the full amount and back out the other part as a nominee amount with a statement.

### Step 4. Distributable net income (section 643(a))

DNI caps both the trust's distribution deduction and what the beneficiaries must include, and sets the character they receive. On Schedule B:

1. Line 1: adjusted total income (page 1 line 17, with the instructions' adjustments).
2. Line 2: adjusted tax-exempt interest (tax-exempt interest less expenses allocated to it). Tax-exempt income is in DNI, but no deduction is allowed for distributing it (section 661(c)); the beneficiary keeps it tax-exempt.
3. Lines 3 to 6: capital gains. By default gains go to principal and are left out of DNI (section 643(a)(3)); they are taxed in the trust. Line 6 removes the page 1 line 4 gain (or adds back a loss).
4. The exemption is added back: it never reduces DNI.
5. Line 7: DNI. For a simple trust, extraordinary dividends and taxable stock dividends allocated to principal are also left out (section 643(a)(4)).

**When gains go into DNI** (Treas. Reg. 1.643(a)-3): when they are allocated to income under the instrument or local law; when the trustee, using a discretion given by the instrument or local law, allocates them to income reasonably, impartially and consistently; or when they are actually distributed or used by the fiduciary in deciding the amount distributed. Default: gains stay in the trust unless one of these applies and is documented.

### Step 5. Simple or complex, and the distribution deduction

**Simple trust (section 651)** for a year when all three hold: the instrument requires all income to be distributed currently; no charitable gifts are provided for; nothing beyond current income is distributed. Otherwise it is complex for that year (section 661). The test is year by year. An estate is always treated like a complex trust.

| Item | Simple trust | Complex trust or estate |
| --- | --- | --- |
| Distribution deduction | Lesser of income required to be distributed and DNI less tax-exempt income | Lesser of amounts paid, credited or required (Tier 1 plus Tier 2) and DNI less tax-exempt income |
| Exemption | USD 300 | USD 100 (trust); USD 600 (estate) |
| 65-day election | Not available | Available |
| Gains in DNI by default | No | No |
| Charitable deduction (section 642(c)) | No | Yes |

Schedule B lines 8 to 15: line 8 accounting income (complex trusts); line 9 income required to be distributed (Tier 1); line 10 other amounts paid or credited (Tier 2); line 11 total; line 12 tax-exempt part; line 13 line 11 less line 12; line 14 DNI less tax-exempt interest; line 15 the smaller of lines 13 and 14, carried to page 1 line 18.

**Tiers and character (sections 652(b) and 662(b))**: Tier 1 (required income distributions) takes DNI first; Tier 2 (discretionary and principal) takes what is left. Within each tier, each beneficiary gets a pro rata share of every class of income in DNI (interest, qualified and ordinary dividends, tax-exempt interest, rents, royalties, foreign income, and gains only if they are in DNI). The separate share rule (section 663(c)) treats substantially separate shares as separate trusts for DNI.

### Step 6. Taxable income and the tax

Page 1: total income, less deductions (fiduciary fees, legal and accounting fees, taxes, the section 691(c) deduction), less the distribution deduction (line 18), less the exemption (line 21) = taxable income (line 23). Then:

1. **Regular tax** from Table 5 on ordinary income, with qualified dividends and net capital gain taxed in the 0% band to USD 3,300, the 15% band to USD 16,250 and 20% above, stacked on top of ordinary income.
2. **Net investment income tax** (Form 8960): 3.8% of the lesser of undistributed net investment income and AGI above USD 16,000. AGI for this purpose is figured under section 67(e), after the distribution deduction and the exemption. Grantor trusts, charitable trusts and some others are not subject to it.
3. **AMT** (Schedule I): exemption USD 31,400, phased out between USD 104,800 and USD 167,600.
4. **Credits and payments**: estimated tax, Form 7004 payment, withholding.

Why it matters: an individual pays 37% only on taxable income above USD 640,600 (single, 2026, Rev. Proc. 2025-32 Table 3); a trust reaches 37% at USD 16,000. Retained investment income above USD 16,000 bears 37% plus 3.8% (40.8%); retained long-term gain above USD 16,250 bears 20% plus 3.8%. Pushing income to a beneficiary in a lower bracket usually saves tax; that is the design of subchapter J.

**Material participation by a trust** (passive loss and NIIT on business or rental income): Frank Aragona Trust v. Commissioner, 142 T.C. 165 (2014), held that a trust can materially participate through its trustees' work. Guidance is unsettled. Default: treat the trust as not participating unless the trustees do the work directly and substantially.

### Step 7. Expenses: deductible, and where

- **Section 67(e)**: costs paid because the property is held in a trust or estate and that would not otherwise have been incurred (fiduciary fees, the fiduciary's legal and return preparation costs) are deducted in arriving at AGI. Knight v. Commissioner, 552 U.S. 181 (2008): costs an individual would commonly incur (investment advice) do not qualify.
- **Section 67(g)**: miscellaneous itemized deductions are disallowed for years beginning after 2017, now with no end date (Public Law 119-21 section 70110 struck "and before January 1, 2026"). So investment advisory fees that are not unique to a trust stay non-deductible in 2026.
- **Section 691(c)** is not a miscellaneous itemized deduction (section 67(b)(7)) and stays deductible.
- **Section 642(g)**: administration expenses (executor and attorney fees, court costs, appraisal fees) and casualty or theft losses during administration may be deducted on Form 706 (section 2053 or 2054) or on Form 1041, not both. Choose item by item; each item goes wholly to one return. For the 1041, attach a statement listing the items and waiving the Form 706 deduction for them.

| Estate's position | Usually deduct on |
| --- | --- |
| No Form 706 required (estate below USD 15,000,000 for a 2026 death) | Form 1041; the 706 deduction would be wasted |
| Taxable on Form 706; most income retained in the estate | Model both; 40% estate tax often beats the income tax saving |
| Taxable on Form 706; large income at 37% plus 3.8% in the estate or flowing to high-bracket beneficiaries | Model both; the 1041 often wins because it cuts DNI and so the K-1 income |

### Step 8. The 65-day election (section 663(b))

A complex trust or an estate may elect to treat amounts paid or credited in the first 65 days of the year as paid on the last day of the year before. For a calendar 2026 return, the window is 1 January to 6 March 2027.

- **Made by** checking Question 6 under Other Information on a Form 1041 filed by the due date, including extensions. It is irrevocable and is made year by year. The amount elected cannot exceed the greater of the trust's accounting income and its DNI for the year, less amounts already paid, credited or required to be distributed in that year.
- **Not on an amended return.** A return filed on time without the election loses it. If the numbers are not ready by 15 April, extend on Form 7004, make the distributions, then file with the election.
- **Process**: draft the return without the election; compare the trust's marginal rate with each beneficiary's; distribute in January to early March; elect. Worked case 2 is this decision.

### Step 9. Section 645: combining a revocable trust with the estate

- A **qualified revocable trust** is a trust treated as owned by the decedent under section 676 at death (a typical revocable living trust).
- The trustee and the executor (or the trustee alone if there is no executor) elect on **Form 8855** by the due date, including extensions, of the estate's first Form 1041. It is irrevocable.
- **Election period**: from death to the earlier of the day the trust and estate have distributed everything, or the day before the applicable date. The applicable date is 2 years after death if no Form 706 is required; if Form 706 is required, the later of 2 years after death and 6 months after the final determination of estate tax.
- **Effect**: one return under the estate's name and EIN (the trust keeps its own TIN with payers); the estate's fiscal year; one USD 600 exemption; the estate's two-year estimated tax exemption; the estate's two-year section 469(i) treatment for rental real estate. After the period ends, the trust is treated as a new trust filing on a calendar year.

| Point | Without section 645 | With section 645 |
| --- | --- | --- |
| Returns | Two | One |
| Trust's year | Calendar | Estate's fiscal year |
| Exemption | USD 600 estate plus USD 100 trust | USD 600 only |
| Estimated tax, first 2 years | Trust exempt only if it receives the residue under the will (section 6654(l)(2)(B)) | Combined entity exempt as an estate |

Decision: estate only (no revocable trust); estate plus a separate trust on a calendar year; or one combined return under section 645, usually best. Where the revocable trust holds everything and there is no probate estate, a trust-only return may be all that is needed.

### Step 10. Income in respect of a decedent (section 691)

IRD is income the decedent had a right to before death but had not received and that was not on the final Form 1040: unpaid wages, accrued bond interest to the date of death, the remaining installments of an installment sale, traditional IRA and qualified plan balances, accrued Series EE interest, renewal commissions, crop share rents, lottery annuity payments.

- Taxed to whoever receives it (estate, trust or beneficiary), in the year received, with the character it would have had for the decedent. If distributed, it flows out through DNI with that character.
- **No step-up**: IRD gets no section 1014 basis increase.
- **Section 691(c) deduction**: where estate tax was paid and the gross estate included IRD, the recipient deducts the estate tax attributable to it: the estate tax paid minus the estate tax figured without the net IRD. It is not a miscellaneous itemized deduction (section 67(b)(7)). It flows to beneficiaries on K-1 box 11.
- **Trap**: IRD is both in the Form 706 gross estate and taxed as income. That is correct; the relief is the section 691(c) deduction, not leaving it off either return. Always compute it when Form 706 showed tax and IRD exists. With no estate tax there is no section 691(c) deduction.

### Step 11. Schedule K-1 (Form 1041) and the final year

Each beneficiary who receives DNI gets a K-1: box 1 interest; 2a and 2b ordinary and qualified dividends; 3 net short-term gain; 4a to 4c net long-term gain (28% rate gain and unrecaptured section 1250 gain shown separately); 5 other portfolio and nonbusiness income; 6 ordinary business income; 7 net rental real estate income; 8 other rental income; 9 directly apportioned deductions (depreciation, depletion, amortization); 10 estate tax deduction (section 691(c)); 11 final year deductions; 12 AMT items; 13 credits (code A estimated tax passed out); 14 other information (tax-exempt interest, foreign items, NIIT items, section 199A information). Beneficiaries report the items on their own Form 1040 (interest and dividends on Schedule B, gains on Schedule D, and the rest on Schedule E Part III), keeping the character.

- **Depreciation, depletion and amortization** are split between the trust and beneficiaries in proportion to accounting income kept and distributed. The trust may elect under section 266 to capitalise carrying charges.
- **Final year**: unused capital loss and NOL carryovers pass to the beneficiaries who receive the residue (section 642(h)(1)), and the final year's excess deductions pass out under section 642(h)(2). Under Treas. Reg. 1.642(h)-2 (T.D. 9918, 2020) excess deductions keep their character: section 67(e) costs remain deductible in arriving at AGI for the beneficiary; others may be disallowed as miscellaneous itemized deductions.
- **NOLs** stay in the trust or estate during its life and only pass out at termination; their computation belongs in `us-net-operating-loss-172`.

### Step 12. Estimated tax and Form 1041-T

- Trusts, and estates after their first 2 years, pay estimated tax on Form 1041-ES if they expect at least USD 1,000 of tax after withholding and credits (safe harbours in `us-quarterly-estimated-tax`). Quarterly dates for calendar 2026: 15 April, 15 June and 15 September 2026, and 15 January 2027.
- **Estate exemption (section 6654(l)(2))**: no estimated tax for a taxable year ending before 2 years after death, for the estate and for a trust that was wholly owned by the decedent and receives the residue under the will.
- **Section 643(g)**: a trust (or an estate, in its final year only) may treat part of its estimated payments as paid by beneficiaries. File Form 1041-T by the 65th day after year end (6 March 2027 for calendar 2026); the amount goes in K-1 box 13 code A. It pairs with the 65-day election.

### Step 13. Other topics in outline

- **ESBT (section 1361(e), section 641(c))**: a trust holding S corporation stock must be a QSST or ESBT or the S election fails. An ESBT's S portion is taxed separately at 37% (with the capital gain rates for its gains), with no distribution deduction and no exemption; the rest is taxed as a normal trust. The election is due within 2 months and 16 days after the trust acquires the stock. Full mechanics, including QBI between the portions, are referred.
- **Section 199A**: a non-grantor trust is a separate taxpayer for the QBI deduction on QBI it keeps; QBI passed out goes to beneficiaries through K-1 box 14. Trusts use the individual thresholds (not compressed ones); the 2026 amounts are in `us-qbi-deduction`. Trusts formed mainly to multiply the deduction are disregarded (Treas. Reg. 1.643(f)-1).
- **State fiduciary income tax**: most states copy the federal return with changes; trust residency can depend on the testator's state, the trustee's, the beneficiaries' or where the trust is run. Use the state skill.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Trust required to pay out all income, but trustee also pays principal this year | Complex for this year |
| Estate | Always complex; USD 600 exemption |
| Capital gain sold and proceeds not distributed, instrument silent | Gain stays in the trust, outside DNI |
| Distributions exceed DNI | Excess is a tax-free principal distribution to the beneficiary |
| Distribution made 20 March 2027 for a calendar 2026 trust | Outside the 65-day window; a 2027 distribution |
| 65-day election omitted on a timely return | Lost; cannot be added on an amended return |
| Former revocable trust, no section 645 election | Calendar year, own EIN, USD 100 (or USD 300) exemption |
| IRD received by an estate below the Form 706 threshold | Taxable income; no section 691(c) deduction |
| Investment advisory fees in 2026 | Not deductible (section 67(g)) unless unique to the trust |
| Qualified disability trust | USD 5,300 exemption |

### Defaults when a fact is missing

| Missing fact | Default | Flag |
| --- | --- | --- |
| How the instrument allocates capital gains | Gains to principal, outside DNI | Read the instrument and state law |
| Allocation of trustee fees between income and principal | Follow the trustee's accounting; deduct the full fee on the return | Allocate part to tax-exempt income |
| Whether the trust materially participates | Not participating | Frank Aragona facts needed |
| Whether a 65-day distribution is intended | Extend on Form 7004 rather than file without the election | Decision before the extended due date |
| Whether Form 706 was filed | Ask; do not compute section 691(c) without it | Estate tax paid and IRD values |
| Year end for a new estate | Ask; if undecided, the month end before the month of death | First return fixes it |

### Red flags

| Red flag | Why it matters |
| --- | --- |
| Parent died in the last 24 months, estate EIN obtained, income-producing assets, no 1041 filed | The most commonly missed return: IRS notice CP259, then section 6651 penalties (5% a month to 25% for late filing, plus late payment) |
| Forms 1099 still issued to the decedent's SSN after death | Nominee reporting and payer correction needed |
| Estate kept open with no administration left | Risk the IRS treats it as closed |
| Retained income far above USD 16,000 with discretionary beneficiaries in low brackets | Consider distribution and the 65-day election |
| IRD and a taxable Form 706 with no section 691(c) deduction | Overpaid income tax |
| Trust holds S stock with no QSST or ESBT election | S election at risk |

## Worked cases

### Case 1. Complex trust keeps its interest income, 2026

A discretionary trust (calendar year, complex) has USD 30,000 of taxable interest in 2026, pays USD 2,000 of trustee fees (deductible under section 67(e)) and distributes nothing. Exemption USD 100. Taxable income USD 27,900. Regular tax = USD 3,851 + 37% x (USD 27,900 minus USD 16,000) = USD 8,254. Net investment income kept USD 28,000 (interest less the fee); AGI over USD 16,000 is USD 11,900, the lesser, so NIIT = 3.8% x USD 11,900 = USD 452.20. Total USD 8,706.20.

```oa-check
name: Complex trust, 30,000 interest retained (2026)
inputs:
  interest: 30000
  trustee_fees: 2000
  exemption: 100
  distribution_deduction: 0
  top_start: 16000
steps:
  - taxable_income: interest - trustee_fees - distribution_deduction - exemption
  - regular_tax: 3851 + (taxable_income - top_start) * 0.37
  - undistributed_nii: interest - trustee_fees - distribution_deduction
  - niit: min(undistributed_nii, max(taxable_income - top_start, 0)) * 0.038
  - total_tax: regular_tax + niit
expected:
  taxable_income: 27900
  regular_tax: 8254.00
  undistributed_nii: 28000
  niit: 452.20
  total_tax: 8706.20
```

### Case 2. Decision: distribute by 6 March 2027 and elect under section 663(b)?

Same trust. The beneficiary is in the 24% bracket and below her own NIIT threshold. The trustee pays her USD 11,900 on 20 February 2027 and elects to treat it as paid in 2026. DNI (USD 28,000 less nothing tax-exempt) covers it. Trust taxable income falls to USD 16,000: tax USD 3,851, no NIIT. Trust saving USD 4,855.20; her extra tax 24% x USD 11,900 = USD 2,856. Family saving USD 1,999.20: **distribute and elect** on a timely Form 1041 (extend if needed).

```oa-check
name: 65-day election decision, beneficiary at 24% (2026 trust year)
inputs:
  tax_before: 8706.20
  taxable_income: 27900
  undistributed_nii: 28000
  distribution: 11900
  beneficiary_rate: 0.24
  top_start: 16000
steps:
  - ti_after: taxable_income - distribution
  - regular_after: 3851 + max(ti_after - top_start, 0) * 0.37
  - niit_after: min(undistributed_nii - distribution, max(ti_after - top_start, 0)) * 0.038
  - trust_saving: tax_before - regular_after - niit_after
  - beneficiary_tax: distribution * beneficiary_rate
  - family_saving: trust_saving - beneficiary_tax
  - elect: min(max(family_saving, 0), 1)
expected:
  ti_after: 16000
  regular_after: 3851.00
  niit_after: 0.00
  trust_saving: 4855.20
  beneficiary_tax: 2856.00
  family_saving: 1999.20
  elect: 1
```

The regular tax formula above is the top-bracket line of Table 5; it holds only at or above USD 16,000. Below that, use the lower lines. A beneficiary above her own NIIT threshold adds 3.8% to her cost; a beneficiary at 35% or 37% may make the push a loss, so compare rates per beneficiary.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-1041-ESBT | ESBT computation, S portion and QBI split | Refer to a specialist |
| R-1041-CRT | Charitable remainder trust, Form 5227, split-interest trust | Refer |
| R-1041-FOREIGN | Foreign trust, or a US trust with foreign grantor issues | `us-foreign-trust-reporting`; refer |
| R-1041-BANKR | Bankruptcy estate (section 1398) | Refer |
| R-1041-THROWBACK | Accumulation distribution from a foreign or pre-1984 trust (Schedule J throwback) | Refer |
| R-1041-PARTIC | Business or rental income where material participation by the trust decides the tax | Flag; reviewer decides on the facts |
| R-1041-GRANTOR | The trust may be a grantor trust (retained powers) | Resolve grantor status before preparing a 1041 |
| R-1041-706 | Estate tax computation or the Form 706 side of section 642(g) | `us-estate-gift-706-709` |

## Filing and payment

| Item | Calendar 2026 | Fiscal year |
| --- | --- | --- |
| Form 1041 and K-1s due | 15 April 2027 | 15th day of the 4th month after year end (year ending 31 May 2027: 15 September 2027) |
| Form 7004 extension | 5 1/2 months, to 30 September 2027 | 5 1/2 months from the original due date |
| Tax due | 15 April 2027; the extension does not extend payment | Original due date |
| Form 8855 (section 645) | Due date of the estate's first 1041, with extensions | Same |
| Form 1041-T (section 643(g)) | 6 March 2027 | 65th day after year end |
| 65-day election | On the timely 2026 return | On the timely return for that year |

Form 1041 can be e-filed through MeF (Forms 8453-FE or 8879-F for signature). If a due date falls on a weekend or legal holiday, file the next business day.

## Completion checklist

- Estate's first 1041 filed when gross income reached USD 600, even with no tax.
- EIN for the estate, and for the trust if no section 645 election; payers given W-9s; year-of-death 1099s split with nominee statements.
- Year end chosen for the estate on the first return; trust on calendar year unless section 645 applies.
- Form 8855 filed if a revocable trust exists and the election is wanted.
- DNI computed with gains outside it unless a Treas. Reg. 1.643(a)-3 exception is met and documented.
- Distribution deduction is the lesser of distributions and DNI, less tax-exempt income.
- 65-day election decided and made on a timely return; extension filed if needed.
- Section 642(g) statement attached for expenses deducted on the 1041.
- IRD identified, taxed when received, no step-up; section 691(c) computed when estate tax was paid.
- K-1s show each beneficiary's pro rata share by character.
- NIIT on Form 8960 and AMT on Schedule I checked.
- Estimated tax: trusts pay; estates exempt for their first 2 years; Form 1041-T considered.
- Final return marked "Final return"; section 642(h) carryovers and excess deductions on final K-1s.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 3.01 Table 5 (estates and trusts brackets), 3.03 (USD 3,300 and USD 16,250), 3.10 (AMT USD 31,400, USD 104,800, USD 167,600) and 3.35 (qualified disability trust USD 5,300). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Instructions for Form 1041 (2025). Read for Who Must File, the section 645 election period, When To File, the 5 1/2-month Form 7004 extension, Estimated Tax for 2026 and Form 1041-T, Question 6 (section 663(b)), e-filing. | https://www.irs.gov/pub/irs-pdf/i1041.pdf | 2026-11-13 |
| Form 1041 (2025). Read for page 1 lines 17, 18, 21 and 23 and Schedule B lines 1 to 15. | https://www.irs.gov/pub/irs-pdf/f1041.pdf | 2026-11-13 |
| Schedule K-1 (Form 1041) instructions (2025). Read for the box list (box 13 code A, box 14). | https://www.irs.gov/pub/irs-pdf/i1041sk1.pdf | 2026-11-13 |
| 26 U.S.C. 1411 (govinfo). Read for (a)(2): 3.8% of the lesser of undistributed net investment income and AGI over the start of the top section 1(e) bracket. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-13 |
| 26 U.S.C. 642 (govinfo). Read for (b): USD 600, USD 300, USD 100 and the qualified disability trust rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec642.htm | 2026-11-13 |
| 26 U.S.C. 644 (govinfo). Read for the calendar year rule and its exceptions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec644.htm | 2026-11-13 |
| 26 U.S.C. 645 (govinfo). Read for the qualified revocable trust definition and the applicable date. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec645.htm | 2026-11-13 |
| 26 U.S.C. 663 (govinfo). Read for (b) the first 65 days rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartC-sec663.htm | 2026-11-13 |
| 26 U.S.C. 6012 (govinfo). Read for (a)(3) to (5) filing thresholds. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartB-sec6012.htm | 2026-11-13 |
| 26 U.S.C. 6072 (govinfo). Read for (a) the 15th day of the 4th month. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-13 |
| 26 U.S.C. 6654 (govinfo). Read for (l)(2) the two-year exception for estates and certain trusts. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm | 2026-11-13 |
| 26 U.S.C. 67 (govinfo). Read for (e) estate and trust AGI and (g) as it stood before 2025. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partI-sec67.htm | 2026-11-13 |
| Public Law 119-21, section 70110. Read for striking ", and before January 1, 2026" from section 67(g). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |

Not yet confirmed: the 2026 Form 1041, its instructions and the 2026 K-1 were not yet published when read, so line, box and question numbers are from the 2025 editions; whether the new section 68 limit on itemized deductions (Public Law 119-21 section 70111, worded "in the case of an individual") reaches estates and trusts was not confirmed; Treas. Reg. 1.641(b)-3, 1.643(a)-3, 1.642(h)-2, 1.671-4 and 1.643(f)-1 and the two cases were not re-read today and are carried from the old file.
