---
name: us-form-1041-trust-and-estate-income
description: Compute federal Form 1041 income tax for domestic estates and non-grantor trusts for tax years beginning in 2026. Covers filing, DNI, simple and complex distributions, retained income, the 65-day election, section 645, IRD, expenses, Schedule K-1 and estimated tax. Historical 2025 cases retain their inputs with explicit holds where facts are incomplete. Trigger on Form 1041, trust tax return, estate income tax, DNI, 65-day rule, section 645 or IRD.
version: "1.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: estate-wealth-tax
type: computation
---

# US Form 1041: estate and trust income, 2026

Compute the estate's or trust's retained taxable income and the beneficiaries' shares separately. A distribution is deductible only under the applicable DNI, character and separate-share rules; distributing cash is not itself proof of a deduction. Federal income tax is distinct from Form 706 estate tax.

## Scope

Domestic decedents' estates and domestic non-grantor trusts, including former revocable trusts after death and eligible section 645 elections, for **tax years beginning in 2026**. An irrevocable trust is not automatically non-grantor. Confirm status before computation. The 2025 Form 1041 and K-1 below provide navigation only: their line numbers are not confirmed for the 2026 editions. Form 1041-T is the published 2026 edition. [IRS instructions, Who Must File and Special Reporting Instructions](https://www.irs.gov/instructions/i1041).

The historical cases retain their 2025 years. Do not apply the 2026 tables to a fiscal year beginning in 2025. This Guide supplies written information, not professional sign-off or a filing authorization; assess the taxpayer's facts and applicable law before relying on it (Circular 230 section 10.37).

## Ask the client first

Obtain the instrument/will, amendments, domestic-status evidence, grantor powers, date of death, estate/trust EINs, year end and prior returns. Obtain income by character, basis and sale records, IRD and retirement basis, accounting-income/principal allocations, deductible-fee detail and tax-exempt allocations, every beneficiary's share/status, distributions by date (including the first 65 days after year end), estimated payments and withholding. Obtain Form 706 and its tax computation if relevant, section 642(g) waivers, Form 8855, S-stock elections and any final-year carryovers. Obtain beneficiaries' tax facts before recommending distributions. Missing facts are a hold, never an assumed allocation, tax rate or participation result.

## The method, step by step

### 1. Filing, year and identity

- A domestic estate files if gross income is **USD 600 or more**, or a beneficiary is a nonresident alien. A domestic trust taxable under section 641 files for **any taxable income**, gross income of **USD 600 or more**, or a nonresident alien beneficiary. A qualified opportunity fund investment can independently require a return with Form 8997. Ordinarily, domestic trust status requires both the US court and US-person control tests; a grandfather election for certain trusts existing in August 1996 is a separate route, held for individual review. [IRS, Who Must File](https://www.irs.gov/instructions/i1041).
- The estate chooses its first period on its first return: at most **12 months**, ending on a month's last day; changing the period uses Form 1128. Non-grantor trusts generally use a calendar year; section 644 excepts section 501(a) and section 4947(a)(1) trusts, and section 645 supplies a separate estate-treatment route. Do not assume a short year is always exempt from annualization: a change-of-year case needs separate analysis. [IRS, Accounting Periods](https://www.irs.gov/instructions/i1041); [section 644](https://uscode.house.gov/us/usc/t26/s644/).
- Beneficiaries report the estate/trust year ending within or with their own tax year: an estate year ending 31 May 2027 enters a calendar beneficiary's 2027 return. [Sections 652(c)](https://uscode.house.gov/us/usc/t26/s652/) and [662(c)](https://uscode.house.gov/us/usc/t26/s662/).
- Establish the entity's EIN and reconcile information returns across death; the decedent's accounting method and IRD determine the income split, not simply the date on a Form 1099. All qualified revocable trusts obtain a new TIN after death **even if section 645 is elected**; notify payers using Form W-9. [IRS, EIN and Special Rule for Certain Revocable Trusts](https://www.irs.gov/instructions/i1041).
- For a wholly grantor trust using the ordinary Form 1041 method, enter entity information and report owner amounts on an attachment, not K-1. A partly grantor trust separately reports the non-grantor portion normally. Optional filing methods and ownership determinations are held below. [IRS, Grantor Type Trusts](https://www.irs.gov/instructions/i1041).
- An estate cannot prolong administration unreasonably to defer tax; termination can occur after a reasonable administration period or distribution of assets apart from a reasonable good-faith reserve. Section 645 has a special continuation rule. [Treas. Reg. 1.641(b)-3(a)](https://www.ecfr.gov/current/title-26/section-1.641(b)-3).

### Rates, bands and thresholds

For ordinary taxable income, apply the following table; excess means excess above the lower boundary. Amounts are USD. Each row is from **Rev. Proc. 2025-32 section 4**, not section 3.

| Ordinary taxable income, 2026 | Tax amount | Official source |
| --- | --- | --- |
| Not over 3,300 | 10% of taxable income | [Section 4.01, Table 5](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Over 3,300 through 11,700 | 330 + 24% of excess over 3,300 | [Section 4.01, Table 5](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Over 11,700 through 16,000 | 2,346 + 35% of excess over 11,700 | [Section 4.01, Table 5](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Over 16,000 | 3,851 + 37% of excess over 16,000 | [Section 4.01, Table 5](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

Ordinary-rate income fills the lower bands before qualified dividends and eligible net capital gains. The general preferential-rate boundaries are **USD 3,300 at 0%, USD 16,250 at 15%, then 20%**; these are total taxable-income boundaries, not fresh allowances for each class. Special capital gains need their own Schedule D computation. [Rev. Proc. 2025-32 section 4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [IRS, Schedule D Tax Worksheet (2025 mechanics)](https://www.irs.gov/instructions/i1041sd).

| Item | Amount / treatment, 2026 | Official source |
| --- | --- | --- |
| Estate personal exemption | USD 600 | [Section 642(b)(1)](https://uscode.house.gov/us/usc/t26/s642/) |
| Trust personal exemption | USD 300 if the instrument requires all income currently distributed, even if corpus distributions make the trust complex that year; otherwise USD 100, subject to the disability rule | [Section 642(b)(2)](https://uscode.house.gov/us/usc/t26/s642/) |
| Qualified disability trust exemption | USD 5,300; establish the statutory disability-trust and beneficiary disability conditions first | [Section 4.35](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [section 642(b)(2)(C)](https://uscode.house.gov/us/usc/t26/s642/) |
| AMT exemption; phaseout begins / complete | USD 31,400; USD 104,800 / USD 167,600, applied to AMT income, not ordinary taxable income | [Section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [section 55(d)](https://uscode.house.gov/us/usc/t26/s55/) |

NIIT is **3.8% of the lesser of undistributed NII and max(section 67(e) AGI minus USD 16,000, zero)**. Compute AGI separately: qualifying administration costs, the distribution deduction and personal exemption reduce it; it need not equal taxable income. NII uses properly allocable allowed deductions, not the personal exemption. Use Form 8960; do not add NIIT to every retained dollar indiscriminately. Qualified-plan/IRA distributions are excluded from NII, although they can affect AGI. [Sections 1411(a)(2), (c)(1), (c)(5)](https://uscode.house.gov/us/usc/t26/s1411/); [section 67(e)](https://uscode.house.gov/us/usc/t26/s67/); [Form 8960 instructions](https://www.irs.gov/instructions/i8960).

### 3. Expenses and DNI

Qualifying administration costs that would not have been incurred outside the estate/trust are section 67(e) deductions. A fee's label alone does not make its entire amount deductible. Ordinary investment advice is not such a cost; only qualifying incremental fiduciary advice can escape that restriction. Allocate bundled fees and tax-exempt expenses before deduction. Miscellaneous itemized deductions remain disallowed in 2026 under **section 67(h)** (former subsection (g)). [Section 67](https://uscode.house.gov/us/usc/t26/s67/); [Treas. Reg. 1.67-4](https://www.ecfr.gov/current/title-26/section-1.67-4).

Amounts allowable under sections 2053/2054 cannot also reduce income tax without the section 642(g) statement that they have not been allowed and waiver of the estate-tax deduction. An income-tax deduction must independently qualify; being below an estate-tax filing threshold does not itself prove deductibility. Model the actual returns instead of choosing by a headline marginal rate. Detailed expense splitting is held below. [Section 642(g)](https://uscode.house.gov/us/usc/t26/s642/).

Compute DNI from taxable income **without the distribution deduction or personal exemption**; if starting with adjusted total income before those deductions, do not add the exemption again. Include tax-exempt interest net of allocable expenses. For simple trusts, exclude qualifying extraordinary/taxable stock dividends allocated to corpus in good faith under the instrument and local law. [Section 643(a)(1)–(5)](https://uscode.house.gov/us/usc/t26/s643/).

Capital gains are ordinarily outside DNI. Under Treas. Reg. 1.643(a)-3(b), inclusion requires the instrument/local law or a reasonable, impartial exercise of authorized fiduciary discretion, with one of: allocation to income (including the regulation's consistency/unitrust limitations); allocation to corpus but consistent treatment on books, records and returns as part of a beneficiary distribution; or corpus gain actually distributed or used to determine the distribution. These are alternatives, not a requirement to satisfy every route. A cash distribution alone does not establish any route. Charitable gains have a separate rule. [Treas. Reg. 1.643(a)-3](https://www.ecfr.gov/current/title-26/section-1.643(a)-3).

### 4. Classification, deduction and K-1 character

A trust qualifies under section 651 for a year only if its terms require all income currently distributed, do not provide for section 642(c) amounts, and it distributes no other amounts that year. A discretionary trust does not become simple just because it distributes all income. A required-income trust paying corpus becomes complex that year, but can still have the USD 300 exemption. Estates use section 661. [Sections 651](https://uscode.house.gov/us/usc/t26/s651/), [661](https://uscode.house.gov/us/usc/t26/s661/) and [642(b)](https://uscode.house.gov/us/usc/t26/s642/).

- **Simple trust:** deduct income required currently distributed, limited to DNI computed excluding tax-exempt income and its allocable deductions. The beneficiary includes the required amount whether paid or not, subject to DNI and character rules. [Sections 651(b)](https://uscode.house.gov/us/usc/t26/s651/) and [652](https://uscode.house.gov/us/usc/t26/s652/).
- **Estate/complex trust:** first identify eligible current required income (tier 1) and other properly paid, credited or required amounts (tier 2). Apply the DNI cap, then exclude the tax-exempt portion of the capped amount. Do not simply take min(cash, taxable DNI) when cash includes tax-exempt character. Tier 1 absorbs DNI first; tier 2 uses the balance. Specific bequests, charitable amounts and amounts already used for an earlier-year deduction have section 663(a) exclusions; in-kind and accumulation distributions are held below. [Sections 661](https://uscode.house.gov/us/usc/t26/s661/), [662](https://uscode.house.gov/us/usc/t26/s662/) and [663(a)](https://uscode.house.gov/us/usc/t26/s663/).
- Income keeps its character. Absent an effective instrument allocation, apply each class's share of DNI and the applicable tier; allocate expenses under the regulations. Substantially separate independent shares require separate DNI computations, solely for the distribution provisions. Do not treat a section 645 combination as one unrestricted DNI pool. [Sections 652(b)](https://uscode.house.gov/us/usc/t26/s652/), [662(b)](https://uscode.house.gov/us/usc/t26/s662/), [663(c)](https://uscode.house.gov/us/usc/t26/s663/); [IRS, Special Rule for Certain Revocable Trusts](https://www.irs.gov/instructions/i1041).

On the **2025** form, Schedule B computes DNI on line 7 and the distribution deduction on line 15, carried to page 1 line 18. Adjusted total income is page 1 line 17; the estate-tax deduction is line 19, QBI deduction line 20, exemption line 21 and taxable income line 23. Include all applicable deductions, not just fees, distributions and exemption. [Form 1041](https://www.irs.gov/pub/irs-pdf/f1041.pdf).

K-1 navigation, **2025 edition only**: interest 1; ordinary dividends 2a (including qualified dividends separately shown in 2b); short-term gain 3; long-term/special-rate gains 4a–4c; other portfolio/business/rental income 5–8; apportioned deductions 9; **estate-tax deduction 10**, final-year deductions 11; AMT 12; credits 13; other information 14. Estimated tax allocation is 13 code A, tax-exempt interest 14 code A, NIIT adjustments 14 code H and QBI information 14 code I. [Schedule K-1](https://www.irs.gov/pub/irs-pdf/f1041sk1.pdf).

### 5. The 65-day election

A complex-trust fiduciary or estate executor can elect for designated amounts properly paid or credited within the first **65 days** after year end to count on the prior year's last day. For calendar 2026 the window ends **6 March 2027**; a payment on **20 March 2027** is outside it. The elected amount is limited to the greater of prior-year accounting income or DNI, reduced by relevant prior-year amounts already paid, credited or required; amounts already treated as a preceding-year distribution under this election are excluded from that reduction. [Section 663(b)](https://uscode.house.gov/us/usc/t26/s663/); [Treas. Reg. 1.663(b)-1(a)](https://www.ecfr.gov/current/title-26/section-1.663(b)-1).

Make the election for each desired year by the return deadline including extensions, in the appropriate return place (Other Information question 6 on the 2025 form). The regulation makes it irrevocable after the last day prescribed for making it. Do not say filing an original return automatically destroys every possible timely corrective route. Omitted/late elections, relief and no-return-required statements need individual review. A filing extension does not extend the **distribution window**. [Treas. Reg. 1.663(b)-2](https://www.ecfr.gov/current/title-26/section-1.663(b)-2); [IRS, Question 6](https://www.irs.gov/instructions/i1041).

Compare tax with and without the election using each beneficiary's income character, brackets and NIIT position, subject to the instrument and fiduciary duties. Do not assume distributing all income always saves tax.

### 6. Section 645

An eligible QRT is a trust/portion treated as owned by the decedent at death under section 676 because of a power held by the decedent, without section 672(e) attribution. The executor, if any, and trustee elect on Form 8855 by the estate's first Form 1041 deadline including extensions, even if insufficient income would otherwise excuse the return. It is irrevocable. No executor is required for a QRT to elect. [Section 645](https://uscode.house.gov/us/usc/t26/s645/); [Treas. Reg. 1.645-1(b), (c)](https://www.ecfr.gov/current/title-26/section-1.645-1).

The period starts at death and ends on the earlier of full asset distribution by the trust and related estate, or the day before the applicable date. Without a required Form 706, the applicable date is two years after death; with one, it is the later of two years after death or six months after the regulatory final determination of estate-tax liability. Do not infer that date from receipt of a closing letter alone. [Treas. Reg. 1.645-1(f)](https://www.ecfr.gov/current/title-26/section-1.645-1).

With an executor, file the combined return using the estate's name/TIN; the QRT still has its own post-death TIN with payers. With no executor, the filing trust uses its post-death TIN and may choose a fiscal year. The combined entity receives one USD 600 exemption, with separate-share DNI treatment. At election termination a continuing trust returns to calendar-year filing if required; the deemed distribution, any new TIN requirement and a later-appointed executor are held for separate review. [IRS, Special Rule for Certain Revocable Trusts](https://www.irs.gov/instructions/i1041).

### 7. IRD and termination

IRD was not properly includible on the decedent's final or earlier return and is included by the recipient when received, with the decedent's income character. Identify unpaid wages, accrued interest, installment profit, taxable retirement distributions, accrued savings-bond interest, commissions, crop-share rents and annuity receipts separately; recovery of basis is not automatically taxable IRD. IRD receives **no section 1014 basis adjustment**. [Section 691(a)](https://uscode.house.gov/us/usc/t26/s691/); [section 1014(c)](https://uscode.house.gov/us/usc/t26/s1014/); [IRS, IRD](https://www.irs.gov/instructions/i1041).

Under section 691(c), allocate the federal estate tax attributable to **net IRD value** to the IRD actually included that year, using the estate-tax value or included amount if lower. Do not deduct all attributable tax every time an installment is received. The estate/trust excludes IRD passed to beneficiaries in computing its own share; report the beneficiary share in K-1 box 10. Section 67(b)(7) excludes this deduction from miscellaneous itemized deductions. A Form 706 filing alone proves neither estate tax nor this deduction. [Section 691(c)](https://uscode.house.gov/us/usc/t26/s691/); [section 67(b)(7)](https://uscode.house.gov/us/usc/t26/s67/); [IRS, Box 10](https://www.irs.gov/instructions/i1041).

At actual termination, section 642(h) can pass unused NOL/capital-loss carryovers and last-year excess deductions (excluding personal exemption and charitable deductions) to beneficiaries succeeding to the property. Excess deductions retain their AGI/non-miscellaneous/miscellaneous character and additional limitations; do not pass every lifetime loss or deduction indiscriminately. [Section 642(h)](https://uscode.house.gov/us/usc/t26/s642/); [Treas. Reg. 1.642(h)-2](https://www.ecfr.gov/current/title-26/section-1.642(h)-2).

## Boundary and exception table

| Facts or topic | Required treatment |
| --- | --- |
| Required-income trust also distributes principal | Complex for that year; exemption still follows the instrument, not the classification label. |
| Gain retained in corpus; no documented regulatory route into DNI | Do not pass the gain out merely because cash was distributed. |
| Cash exceeds DNI | Do not label all excess tax-free: check specific bequests, accumulated income, in-kind property, gain recognition and foreign issues first. |
| Missing instrument, expense allocation, grantor status or participation facts | Stop that conclusion and obtain the evidence; no default to full deductibility or nonparticipation. |
| Form 706/709/GST, DSUE or basis other than IRD | Route to `us-estate-gift-706-709`; this Guide computes income tax only. |
| Foreign trusts/owners, nonresident beneficiaries and withholding | Route to `us-foreign-trust-reporting`; no foreign reporting or withholding clearance here. Check this point with one of our partner accountants. |
| ESBT/QSST, S-election eligibility, S-portion tax, election timing or QBI split | No computation or eligibility assurance here. Check this point with one of our partner accountants. |
| CRT, Form 5227, split-interest/section 4947 trusts, pooled income funds, common trust funds, bankruptcy estates | Separate regimes; do not use the ordinary computation as a filing answer. Check this point with one of our partner accountants. |
| Charitable lead trust, QPRT, GRAT or ILIT ownership; optional grantor filing methods; domestic-trust grandfather election | Do not infer grantor status from the label or waive filing from an SSN alone. Check this point with one of our partner accountants. |
| Material participation/passive activity, rental relief under section 469, disputed litigation positions | No participation default or legal holding supplied here. Check this point with one of our partner accountants. |
| QBI, multiple-trust anti-abuse, NOL computation, depreciation/depletion/amortization allocations, drilling costs or section 266 | Route QBI/NOL detail to `us-qbi-deduction` / `us-net-operating-loss-172`; hold the result pending that analysis. Check this point with one of our partner accountants. |
| Charitable deduction computation, extraordinary dividends, separate-share allocations, in-kind distributions, Schedule J throwback or section 663(a) specific bequests | Apply the identified statutory gateway above; complex outcome held. Check this point with one of our partner accountants. |
| Expense splitting under section 642(g), section 68 itemized limitation, change-of-year annualization, section 645 termination/later executor, omitted-election relief | No blanket result from this Guide. Check this point with one of our partner accountants. |
| State fiduciary tax/residency | Use the relevant state Guide and its year; federal classification is not state clearance. |

## Worked cases

### Case 1. Complex trust retains interest, 2026

Original facts: discretionary calendar-year trust, USD 30,000 taxable interest, USD 2,000 trustee fees deductible under section 67(e), no distribution, USD 100 exemption. Assume the fees are fully allocable to this interest and no AMT adjustment, other deductions, credits or tax applies. DNI and NII are USD 28,000; both taxable income and section 67(e) AGI are USD 27,900 **on these facts**. Regular tax is USD 3,851 + 37% × (27,900 − 16,000) = USD 8,254; NIIT is 3.8% × min(28,000, 11,900) = USD 452.20. Total federal regular tax plus NIIT: **USD 8,706.20**, before return rounding. Sources: rate table, sections 67(e), 642(b), 643(a) and 1411 above.

```oa-check
name: Complex trust retains 30000 interest in 2026
inputs:
  interest: 30000
  trustee_fees: 2000
  exemption: 100
  distribution_deduction: 0
  top_start: 16000
steps:
  - dni: interest - trustee_fees
  - agi: interest - trustee_fees - distribution_deduction - exemption
  - taxable_income: interest - trustee_fees - distribution_deduction - exemption
  - regular_tax: 3851 + (taxable_income - top_start) * 0.37
  - undistributed_nii: interest - trustee_fees - distribution_deduction
  - niit: min(undistributed_nii, max(agi - top_start, 0)) * 0.038
  - total_tax: regular_tax + niit
expected:
  dni: 28000
  agi: 27900
  taxable_income: 27900
  regular_tax: 8254.00
  undistributed_nii: 28000
  niit: 452.20
  total_tax: 8706.20
```

### Case 2. Election on a February distribution

Same 2026 trust and assumptions; beneficiary's incremental ordinary rate is 24% and she stays below her own NIIT threshold. The trustee properly pays her **USD 11,900 on 20 February 2027**, elects timely for that amount and has authority under the instrument. The USD 28,000 DNI covers it. Trust taxable income and AGI become USD 16,000, regular tax USD 3,851 and NIIT zero. Trust saving USD 4,855.20 less beneficiary tax USD 2,856 gives **USD 1,999.20 combined saving**. Elect on these assumptions; reassess if the beneficiary crosses a band, NIIT applies, or another tax/benefit changes. A filing extension cannot postpone the distribution. Sources: sections 661, 662, 663(b), 1411 and the rates above.

```oa-check
name: 65-day election at beneficiary rate 24 percent
inputs:
  tax_before: 8706.20
  taxable_income: 27900
  agi: 27900
  undistributed_nii: 28000
  distribution: 11900
  beneficiary_rate: 0.24
  top_start: 16000
steps:
  - ti_after: taxable_income - distribution
  - agi_after: agi - distribution
  - regular_after: 3851 + max(ti_after - top_start, 0) * 0.37
  - niit_after: min(undistributed_nii - distribution, max(agi_after - top_start, 0)) * 0.038
  - trust_saving: tax_before - regular_after - niit_after
  - beneficiary_tax: distribution * beneficiary_rate
  - family_saving: trust_saving - beneficiary_tax
  - elect: min(max(family_saving, 0), 1)
expected:
  ti_after: 16000
  agi_after: 16000
  regular_after: 3851.00
  niit_after: 0.00
  trust_saving: 4855.20
  beneficiary_tax: 2856.00
  family_saving: 1999.20
  elect: 1
```

These formulas use the top ordinary-bracket line and apply only at or above its lower boundary. Use all lower bands for other cases.

### Historical H1. Simple trust, 2025: outcome held

Original inputs retained: trust created in **2010**, mandatory current income to one daughter, no charitable or corpus distributions; taxable interest **USD 40,000**, qualified dividends **USD 20,000**, tax-exempt interest **USD 8,000**, corpus long-term gain **USD 30,000**, trustee fees **USD 5,000** allocated **USD 4,000 income / USD 1,000 corpus**. Accounting income is **USD 64,000**, corpus net **USD 29,000**. These are arithmetic subtotals, not the income-tax fee allocation. The old USD 63,000 DNI and USD 55,000 deduction ignored the required tax-exempt expense allocation; the old K-1 values and capital-gain tax are not usable. Qualified dividends are also ordinary dividends for box 2a, with box 2b showing the qualified subset. Preserve 2025: resolve fee allocations, DNI and gain treatment before computing the return. **Check this point with one of our partner accountants.**

### Historical H2. Estate fiscal year, 2025–26: outcome held

Original inputs retained: death **14 June 2025**, estate **USD 2.5 million**, no revocable living trust, fiscal year ends **31 May 2026**; residence sold **10 March 2026**, gain **USD 40,000**; post-death dividends **USD 32,000**, post-death interest **USD 9,500**, accrued IRD interest **USD 8,000**, unpaid consulting IRD **USD 12,000**; executor fees **USD 15,000**, attorney fees **USD 10,000**; cash **USD 90,000 on 31 March 2026**, equally to three adult children (**USD 30,000 each**), assumed rates **24% ordinary / 15% long-term gain**. Income sums to USD 101,500; subtracting the stated USD 25,000 fees gives USD 76,500 before distribution and exemption. If the fees fully qualify and the gain is outside DNI, DNI is **USD 36,500**, not USD 37,100: no exemption add-back to a starting figure that never deducted it. On those conditions, taxable income is **USD 39,400**, not USD 38,800. The fiscal-year distribution belongs in calendar beneficiaries' **2026** year, not 2025. Final tax and K-1 amounts remain **non-usable** pending expense allocation, dividend qualification, instrument/gain and estate-tax facts; USD 2.5 million alone does not establish the Form 706 filing result. **Check this point with one of our partner accountants.**

### Historical H3. Discretionary trust, 2025: outcome held

Original inputs retained: two beneficiaries, **Tom age 35 at 22% ordinary**, **Sara age 38 at 35% ordinary**, with **15% qualified-dividend rates** used in the old comparison; interest **USD 25,000**, nonqualified dividends **USD 10,000**, qualified dividends **USD 15,000**, no gain, fees **USD 4,000**, no charity. USD **5,000** distributed to Tom in 2025; proposed **USD 20,000 to Tom and USD 10,000 to Sara on 14 February 2026**. With fully deductible fees and no other adjustments, net income/DNI is **USD 46,000**, not USD 46,100; taxable income before/after a valid USD 30,000 election is USD **40,900 / 10,900**. Ordinary dividends total USD 25,000 before expenses; qualified dividends are a subset, not a new allowance underneath ordinary income. Distributions carry the properly allocated dividend character out; USD 15,000 cannot automatically stay qualified inside the trust after distribution. The original before/after taxes, K-1 amounts and family-saving conclusion are **non-usable** until fee allocation, beneficiary gain bands and NIIT facts are resolved. **Check this point with one of our partner accountants.**

## When to refuse or refer

A held point supplies no filing, deadline-relief, tax-saving or eligibility conclusion. Retain its original facts, identify the missing operative condition and use the exact partner-accountant referral in the boundary table or historical case. For the ordinary supported case, return classification, year, income/expense reconciliation, DNI, eligible deduction, taxable income, regular tax/NIIT/AMT check, K-1 character and payment/election dates. Do not use a referral to replace those core computations.

## Filing and payment

| Task | Rule and calendar 2026 result | Official source |
| --- | --- | --- |
| Form 1041 and K-1 filing | 15th day of fourth month after year end: 15 April 2027; fiscal year ending 31 May 2027: 15 September 2027 | [Section 6072(a)](https://uscode.house.gov/us/usc/t26/s6072/); [IRS, When To File](https://www.irs.gov/instructions/i1041) |
| Form 7004 | Timely application for 5½-month filing extension: calendar return to 30 September 2027; tax payment remains due on the original payment date | [IRS Form 7004 instructions](https://www.irs.gov/instructions/i7004) |
| Estimated tax, ordinary calendar case | Generally required if expected tax after withholding/credits is at least USD 1,000 and withholding/credits fall below the applicable safe harbour; installment dates 15 April, 15 June, 15 September 2026 and 15 January 2027 | [Section 6654(c), (d), (e), (l)](https://uscode.house.gov/us/usc/t26/s6654/); [IRS, Estimated Tax for 2026](https://www.irs.gov/instructions/i1041) |
| Estate/certain-trust estimated-tax exception | Taxable years ending before two years after death: estate; or wholly decedent-owned trust receiving residue under the will, or primarily liable for debts/taxes/administration if no will admitted to probate. Separate prior-year no-liability and charitable exceptions also exist | [Section 6654(e), (l)](https://uscode.house.gov/us/usc/t26/s6654/); [IRS, Exceptions](https://www.irs.gov/instructions/i1041) |
| Form 1041-T | A trust (including a continuing trust), or an estate for a taxable year reasonably expected to be its last, may elect estimated-payment allocation by the 65th day after close, next business day if weekend/holiday; calendar 2026 deadline **8 March 2027** | [2026 Form 1041-T, When To File](https://www.irs.gov/pub/irs-pdf/f1041t.pdf) |

For the ordinary case outside the stated exceptions and special farming/fishing rules, the safe harbour uses the smaller of 90% current-year tax or 100% prior-year tax (110% if prior-year AGI exceeds USD 150,000); the prior return must cover twelve months. Section 6654(l)(1) applies the section to estates and trusts, and (d)(1)(C)(iii) specifically determines their AGI under section 67(e). Special farming/fishing, fiscal/short-year and annualized-income cases need their own computation; use `us-quarterly-estimated-tax` and hold unresolved results. [Section 6654(d), (i)–(l)](https://uscode.house.gov/us/usc/t26/s6654/); [2026 Form 1041-ES, Who Must Make Estimated Tax Payments](https://www.irs.gov/pub/irs-pdf/f1041es.pdf). Check this point with one of our partner accountants.

Form 1041-T transfers **estimated payments**, not withholding. Include the elected amount as a beneficiary distribution in Schedule B line 10 and K-1 box 13 code A; it is not a free-standing credit transfer with no DNI effect. Its deadline remains independent of the Form 1041 extension and the section 663(b) election. [2026 Form 1041-T, lines 1–2](https://www.irs.gov/pub/irs-pdf/f1041t.pdf).

Electronic filing/signature methods, any paper address, late-filing/late-payment minimums, rate changes, penalty coordination, information-return penalties and relief depend on the actual return and filing date. No penalty estimate or filing-method clearance supplied here. **Check this point with one of our partner accountants.** Interest can apply despite a filing extension. [IRS, Interest and Penalties](https://www.irs.gov/instructions/i1041). For weekend/legal-holiday filing dates apply [section 7503](https://uscode.house.gov/us/usc/t26/s7503/); do not move the stated distribution cutoff by analogy to a filing deadline.

## Completion checklist

- Confirm domestic/grantor status and required return; reconcile every source document and death-date split.
- Resolve the instrument, deductible expenses and tax-exempt allocation before DNI and K-1s.
- Keep accounting income, DNI, AGI, taxable income and NII distinct; preserve separate shares and income character.
- Compare distribution/election alternatives on actual beneficiary facts and document authority.
- Confirm 2026 form mapping before filing; retain Form 8855, waivers, Form 1041-T and supporting computations where applicable.
- Identify final-year carryovers and mark final returns/K-1s when appropriate; do not treat unresolved historical cases as completed returns.

## Sources

All sources below were read **27 November 2026** for the operative passages used. Current US Code text is through Public Law 119-142 (10 November 2026); section 67 reflects Public Law 119-21's 2026 amendment. Government legal and IRS source text is public-domain material. A 2025 form citation supports its labeled navigation, not an assertion that the final 2026 form is identical.

| Source and passages | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32 sections 4.01 Table 5, 4.03, 4.10, 4.35 | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| Form 1041 instructions (2025): filing, identity, periods, expenses, distributions, K-1 and 2026 estimated tax | https://www.irs.gov/instructions/i1041 | 2026-11-27 |
| Form 1041 and Schedule K-1 (2025): labeled line/box navigation | https://www.irs.gov/pub/irs-pdf/f1041.pdf ; https://www.irs.gov/pub/irs-pdf/f1041sk1.pdf | 2026-11-27 |
| Form 1041-T (2026), instructions on page 2 | https://www.irs.gov/pub/irs-pdf/f1041t.pdf | 2026-11-27 |
| Form 1041-ES (2026), Who Must Make Estimated Tax Payments and exceptions | https://www.irs.gov/pub/irs-pdf/f1041es.pdf | 2026-11-27 |
| Form 7004, Form 8960 and Schedule D instructions | https://www.irs.gov/instructions/i7004 ; https://www.irs.gov/instructions/i8960 ; https://www.irs.gov/instructions/i1041sd | 2026-11-27 |
| Sections 55, 67, 642 and 644 | https://uscode.house.gov/us/usc/t26/s55/ ; https://uscode.house.gov/us/usc/t26/s67/ ; https://uscode.house.gov/us/usc/t26/s642/ ; https://uscode.house.gov/us/usc/t26/s644/ | 2026-11-27 |
| Section 643(a), DNI modifications | https://uscode.house.gov/us/usc/t26/s643/ | 2026-11-27 |
| Sections 645, 651, 652, 661, 662 and 663 | https://uscode.house.gov/us/usc/t26/s645/ ; https://uscode.house.gov/us/usc/t26/s651/ ; https://uscode.house.gov/us/usc/t26/s652/ ; https://uscode.house.gov/us/usc/t26/s661/ ; https://uscode.house.gov/us/usc/t26/s662/ ; https://uscode.house.gov/us/usc/t26/s663/ | 2026-11-27 |
| Sections 691, 1014 and 1411 | https://uscode.house.gov/us/usc/t26/s691/ ; https://uscode.house.gov/us/usc/t26/s1014/ ; https://uscode.house.gov/us/usc/t26/s1411/ | 2026-11-27 |
| Sections 6072, 6654 and 7503 | https://uscode.house.gov/us/usc/t26/s6072/ ; https://uscode.house.gov/us/usc/t26/s6654/ ; https://uscode.house.gov/us/usc/t26/s7503/ | 2026-11-27 |
| Treas. Reg. 1.67-4, 1.641(b)-3, 1.642(h)-2 | https://www.ecfr.gov/current/title-26/section-1.67-4 ; https://www.ecfr.gov/current/title-26/section-1.641(b)-3 ; https://www.ecfr.gov/current/title-26/section-1.642(h)-2 | 2026-11-27 |
| Treas. Reg. 1.643(a)-3, 1.645-1, 1.663(b)-1 and -2 | https://www.ecfr.gov/current/title-26/section-1.643(a)-3 ; https://www.ecfr.gov/current/title-26/section-1.645-1 ; https://www.ecfr.gov/current/title-26/section-1.663(b)-1 ; https://www.ecfr.gov/current/title-26/section-1.663(b)-2 | 2026-11-27 |

Not yet confirmed: final 2026 Form 1041/K-1 navigation and every specifically held specialist or historical outcome above are non-usable until their stated conditions are resolved. Check this point with one of our partner accountants.
