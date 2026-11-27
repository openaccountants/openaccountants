---
name: us-1120-corporation-return-schedule-ordinary-business
description: Apply the four federal loss limits to a 2026 S corporation shareholder’s Schedule K-1 box 1 loss, with stock and debt basis, at-risk amounts, the seven material participation tests, excess business losses, distributions and loan repayments. Includes original worked cases and separately labelled historical corporation-filing points.
version: "2.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# S corporation ordinary business loss on Schedule K-1 (Form 1120-S), tax year 2026

Apply the shareholder’s **basis → at-risk → passive activity → excess business loss** limits in that order. A K-1 loss is not automatically deductible. For tax years beginning in 2026 the last limit uses **USD 256,000, or USD 512,000 on a joint return**. Track the amounts stopped by each limit separately. ([Form 7203 instructions](https://www.irs.gov/instructions/i7203); [Rev. Proc. 2025-32 §4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

## Scope and who this is for

For an individual shareholder of a corporation with a valid S election and a box 1 ordinary business loss. Federal rules only. Despite the filename, this is not the C corporation Form 1120 computation. Corporation filing points retained from the earlier Guide appear separately below. The 2026 loss thresholds come from the 2026 revenue procedure; procedural box and line references use the read editions identified in Sources, not an assumed 2026 revision.

## Ask the client first

Obtain the K-1 and all activity statements; beginning stock basis and all prior basis worksheets; suspended losses classified by limit and year; contributions, distributions and nondeductible expenses; each loan’s documents, principal, basis, repayments and funding source; any guarantee payments or loss protection; work by the shareholder and spouse; other businesses and filing status; stock transfers and election changes. Ask whether the corporation’s year is calendar or fiscal. Do not substitute zero basis, passive status or an unwritten loan for missing evidence. **Hold the affected result until the facts are established.**

## The method, step by step

### Rates, bands and thresholds

| Item and period | Amount or test | Official source |
|---|---|---|
| Excess business loss, tax years beginning in 2026 | USD 256,000; USD 512,000 joint | [Rev. Proc. 2025-32 §4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Historical 2025 excess business loss threshold only | USD 313,000; USD 626,000 joint; do not use for 2026 | [Form 461 instructions, Threshold amount](https://www.irs.gov/instructions/i461) |
| Open account debt at corporation year end | Aggregate outstanding principal not exceeding USD 25,000; see later-year rule below | [Reg. 1.1367-2(a)(2)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf) |

The statutory base is USD 250,000, doubled for joint returns. The 2026 inflation reset uses 2024 rather than 2017; that is why the 2026 indexed amount is lower than 2025. P.L. 119-21 §70601(b),(c)(2) applies the reset after 31 December 2025, and §70601(a),(c)(1) makes the rule permanent after 31 December 2026. The older Code page’s end date must be read with P.L. 117-2 §9041 (covering 2026), P.L. 117-169 §13903(b), and P.L. 119-21, not applied in isolation. ([§461(l)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm); [P.L. 117-2](https://www.govinfo.gov/content/pkg/PLAW-117publ2/html/PLAW-117publ2.htm); [P.L. 117-169](https://www.govinfo.gov/content/pkg/PLAW-117publ169/html/PLAW-117publ169.htm); [P.L. 119-21 §70601](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))

### 1. Basis: Form 7203

File Form 7203 if any one applies: claiming an aggregate loss deduction, including a prior basis-suspended loss; receiving a non-dividend distribution; disposing of stock, whether gain is recognized or not; or receiving a loan repayment. If both spouses receive a K-1 for jointly held stock, complete a separate form for each spouse. Maintaining it in other years helps track basis. ([Instructions, Who Must File and Name of Shareholder](https://www.irs.gov/instructions/i7203))

**Stock, Part I.** Beginning basis normally equals the prior year’s ending basis; purchased stock usually starts at cost. Record capital contributions separately from loans. For property exchanged under §351, gifts, inherited stock and multiple stock blocks, use the specific hold below rather than assuming cash cost or unrestricted fair market value. ([Instructions, lines 1–2](https://www.irs.gov/instructions/i7203))

Under §1367(a) and Reg. 1.1367-1(f), adjust in this order: income (including tax-exempt income) and excess non-oil/gas depletion; non-dividend distributions; noncapital nondeductible expenses and permitted oil/gas depletion; then losses and deductions. Basis never falls below zero. Taxable income increases basis only to the extent included on the shareholder’s return. An S corporation’s excluded discharge-of-indebtedness income does not increase shareholder basis. ([§1367](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1367.htm); [Reg. 1.1367-1(f)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-1.pdf); [Form 7203 lines 3k, 8b](https://www.irs.gov/instructions/i7203))

The Reg. 1.1367-1(g) election reverses the last two adjustments, putting losses before nondeductibles. Excess nondeductibles then carry over for basis purposes; without the election they do not carry beyond stock and debt basis. Attach the election statement to a timely original or amended return and mark Form 7203 item E; it continues for this corporation until the IRS permits revocation. Adjustments generally take effect at corporate year end, or immediately before a stock disposition; a closing-of-books election requires separate periods. ([Reg. 1.1367-1(d),(g)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-1.pdf); [Form 7203](https://www.irs.gov/instructions/i7203))

**Distributions.** Non-dividend distributions use stock basis, not debt basis. Report any excess as capital gain on Form 8949 and Schedule D without increasing basis for that gain; long-term treatment requires stock held more than one year. Form 1099-DIV dividends are not box 16 code D distributions. ([IRS basis page](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis); [Form 7203 line 6](https://www.irs.gov/instructions/i7203))

**Debt, Part II.** Only adjusted basis in bona fide corporate indebtedness running directly to the shareholder counts. A disregarded entity can be used; back-to-back loans depend on their real facts. A guarantee or co-signature alone creates no basis; an actual payment on bona fide guaranteed debt can create basis to that extent. ([Reg. 1.1366-2(a)(2), examples 1–4](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1366-2.pdf))

Losses, deductions, nondeductible expenses and oil/gas depletion exceeding stock basis reduce debt basis, never below zero. Distributions do not reduce it. Reduce debts held at corporate year end; satisfied, disposed-of or forgiven debt is excluded. If the shareholder exits during the year, test debts held immediately before exit. With several debts, allocate the reduction in proportion to their bases. ([Reg. 1.1367-2(b),(d)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf); [Form 7203](https://www.irs.gov/instructions/i7203))

**Restoration and repayment.** A later year’s net increase (income and excess depletion less all §1367(a)(2) decreases, including distributions) first restores prior debt reductions before increasing stock basis. Only debt held at the beginning of that later year qualifies, and restoration is capped at its beginning-year adjusted basis ignoring prior S corporation reductions. Restore debt repaid that year first, to the extent necessary to offset repayment gain, then allocate the remainder in proportion to outstanding unrestored reductions. Restoration generally occurs at year end, but immediately before the first repayment/disposition when that happens earlier. Repayment of debt whose basis remains reduced is a recognition event. ([Reg. 1.1367-2(c),(d)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf))

For gain character, the Form 7203 line 34 instructions prescribe capital gain on a formal note (Form 8949/Schedule D), ordinary gain on open account debt (Form 4797), and no basis increase for the gain. **An unwritten advance exceeding USD 25,000 needs a separate character determination:** the same instructions’ line 17 caution says prior-year excess debt is a formal note for gain calculation, while line 34 includes Reg. 1.1367-2(a)(2)(ii) debt in ordinary gain. Do not use either label automatically for that conflict. Check this point with one of our partner accountants. ([Instructions, lines 17 and 34](https://www.irs.gov/instructions/i7203))

Open account debt consists of unwritten advances and repayments treated as one debt; net the year’s advances/repayments and combine with the opening principal balance. If the resulting year-end principal exceeds USD 25,000, that debt is treated as written-instrument debt for basis purposes in subsequent years, separately tracked; it is not an annual reset of all unwritten advances. ([Reg. 1.1367-2(a)(2),(d)(2)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf))

**Loss, Part III.** Available basis is stock basis after the applicable preceding adjustments plus debt basis before this year’s loss reduction. Combine current losses with basis-suspended losses and allocate limited basis proportionately across the loss/deduction categories. The §1367-1(g) election changes which nondeductibles precede losses. Excess losses retain character and carry indefinitely subject to later basis. Report released prior-year amounts separately by year rather than netting them into the current K-1. ([Reg. 1.1366-2(a)(3)–(5)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1366-2.pdf); [K-1 instructions, Part III](https://www.irs.gov/instructions/i1120ssk))

A partial stock transfer ordinarily leaves the suspended basis loss with the transferor; transferring all stock permanently loses it. For qualifying §1041 transfers after 31 December 2004, the loss on transferred stock goes to the spouse/former spouse under the regulation’s allocation rule. Check a planned disposal before completing it; a contribution does not guarantee that the other limits will allow a deduction. If S status ends, the last S year’s suspended basis losses have a post-termination transition rule capped by stock basis, not debt basis, on its last day. Do not use an ordinary annual carryforward calculation for that event. ([Reg. 1.1366-2(a)(6)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1366-2.pdf); [§1366(d)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1366.htm))

### 2. At-risk: Form 6198

Compute the amount at risk for each activity independently of the basis calculation. Section 465 limits the current loss to the amount at risk at year end; amounts include money and adjusted property basis contributed and eligible borrowing. Personal liability can qualify borrowing; a pledge of property outside the activity counts only up to the net fair market value of the taxpayer’s interest, subject to §465(b)(2)’s anti-financing rule. Nonrecourse financing and loss protection generally do not qualify. Qualified nonrecourse financing of an activity holding real property is an exception; mineral property is excluded. Interested/related-party borrowing has creditor and corporate-shareholder exceptions, so a direct shareholder loan is not disqualified merely because its lender owns stock. Use the financing holds below for these exceptions. ([§465(a),(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec465.htm); [Form 6198, Amounts Not at Risk](https://www.irs.gov/instructions/i6198))

Form 6198 generally applies when an activity incurred a loss and had amounts not at risk invested during the year. Its instructions also require filing for the residual category of trade/business activities with the specified interested-party borrowing, subject to the pre-May 2004 exception. Do not reduce that to a loss-only filing test. Obtain separate corporate activity statements and apply the form’s aggregation/separation rules. Pre-1987 real-property cases need the specific exception, not a blanket exemption. ([Form 6198, Who Must File and At-Risk Activities](https://www.irs.gov/instructions/i6198))

Carry the disallowed loss to the next year under §465(a)(2). If at-risk falls below zero, §465(e) recaptures the shortfall into activity income, capped by earlier allowable losses less prior recapture; the amount recaptured is a deduction allocated to the activity in the succeeding year. ([§465(a),(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec465.htm))

### 3. Passive activity: Form 8582

For the ordinary trade/business activity here, lack of material participation makes it passive. Passive losses normally offset passive income, not wages or ordinary portfolio interest; excess carries under §469(b). Disposal of the entire activity interest to an unrelated party in a fully taxable transaction releases the activity’s losses from this limit; installment sales, gifts, death, grouping and rental exceptions need separate treatment. Becoming active alone does not release all old passive losses: §469(f) first uses them against that activity’s income and leaves the rest subject to passive rules. ([§469(b),(c),(e),(f),(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm); [Form 8582](https://www.irs.gov/instructions/i8582))

One of the seven tests can establish material participation. Apply the definitions and exclusions, not just an hours total. ([Reg. 1.469-5T](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf))

| Test | Required conditions | Official source |
|---|---|---|
| 1 | More than 500 hours in the year | [§1.469-5T(a)(1)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |
| 2 | Substantially all participation of all individuals, including non-owners | [§1.469-5T(a)(2)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |
| 3 | More than 100 hours and at least as much as any other individual, including non-owners | [§1.469-5T(a)(3)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |
| 4 | Significant participation activities total more than 500 hours; each is a trade/business with more than 100 hours and no other material-participation test met | [§1.469-5T(a)(4),(c)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |
| 5 | Material participation, determined without this test, in any 5 of the preceding 10 years | [§1.469-5T(a)(5)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |
| 6 | Personal service activity: material participation in any 3 preceding years; covered professions or another business where capital is not a material income-producing factor | [§1.469-5T(a)(6),(d)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |
| 7 | Regular, continuous, substantial participation on all facts; unavailable at 100 hours or less. Management hours do not count if another manager is compensated or another individual manages for more hours | [§1.469-5T(a)(7),(b)(2)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |

Count qualifying work by the shareholder and spouse, excluding investor work without direct day-to-day involvement and unusual owner work principally intended to avoid passive-loss rules. Use participation during the corporation’s tax year. Reasonable evidence can include calendars and narrative summaries; contemporaneous daily logs are not mandatory. ([K-1 instructions, Material participation](https://www.irs.gov/instructions/i1120ssk); [Form 8582, Proof of participation](https://www.irs.gov/instructions/i8582))

### 4. Excess business loss: Form 461

At shareholder level, aggregate all trade/business deductions and income. The excess over business income plus the applicable threshold is disallowed. Exclude employee-service income and deductions (including the owner’s W-2 wages), deductions under §§172 and 199A, and capital losses. Capital gains count only up to the lesser of business capital-gain net income and total capital-gain net income. Disallowed excess is treated as an NOL for subsequent-year carryover under §172; use Form 172 for the NOL computation rather than assuming the whole allowed business loss is itself an NOL. ([§461(l)(2)–(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm); [Form 461](https://www.irs.gov/instructions/i461); [2026 thresholds](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

**Filing hold:** exceeding the net-loss threshold is not necessarily the only Form 461 filing trigger. The read 2025 instructions also test an individual line loss. This Guide does not establish the final 2026 form’s separate filing-trigger amount or revised line numbers. Do not copy the 2025 form’s amounts into 2026. Check this point with one of our partner accountants.

## Worked cases

All amounts are invented US dollars for illustration. The only official figure used is the 2026 excess business loss threshold for a single filer (USD 256,000).

**Case 1, the four limits in order.** Ana is the sole shareholder of a calendar-year S corporation and files as single. Stock basis on 1 January 2026: 30,000. Of the cash she paid for the stock, 10,000 came from a nonrecourse loan secured only by the stock. On 1 March 2026 she lent the corporation 40,000 of her own money under a signed note. She also guaranteed a 100,000 bank loan to the corporation and has paid nothing on it. No losses are suspended from earlier years and no Reg. 1.1367-1(g) election. 2026 K-1: box 1 ordinary business loss (90,000); box 4 interest income 1,000; box 16C nondeductible expenses 2,000; box 16D non-dividend distributions 8,000. She worked 1,200 hours in the business; the corporation paid her W-2 wages. She also runs a separate sole proprietorship with a Schedule C net loss of (240,000).

| Step | USD | Running stock basis |
| --- | --- | --- |
| Stock basis 1 January 2026 | | 30,000 |
| Add interest income (box 4) | 1,000 | 31,000 |
| Less non-dividend distributions (box 16D) | (8,000) | 23,000 |
| Less nondeductible expenses (box 16C) | (2,000) | 21,000 |

The distribution of 8,000 is below the 31,000 of basis before distributions, so it is tax-free. Debt basis: 40,000 from the direct loan; the guarantee adds nothing. Section 1366(d) limit: 21,000 + 40,000 = 61,000; suspended for basis: 29,000. At-risk: the 10,000 financed by the nonrecourse loan secured only by the stock is not at risk. On these facts, the Form 6198 computation before this year’s loss is 30,000 - 10,000 + 40,000 + 1,000 - 8,000 - 2,000 = 51,000; 51,000 passes and 10,000 is carried under section 465. This is a separate at-risk calculation, not a general rule to subtract nonrecourse borrowing from whatever passes the basis limit. Passive: 1,200 hours is more than 500 hours (test 1), so the 51,000 is nonpassive. (If she had worked 80 hours, met no other test and had no passive income, all 51,000 would be suspended under section 469(b), and test 7 would not be available.) Excess business loss: 51,000 + 240,000 = 291,000 of net business loss, wages left out; over the 256,000 threshold by 35,000, which becomes a net operating loss on Form 172. Business loss allowed through these four limits in 2026: 256,000. The 1,000 portfolio interest remains separately reportable; it is not business income in this example’s Form 461 calculation. Check: 29,000 + 10,000 + 51,000 = 90,000.

```oa-check
name: S corporation K-1 loss through the four limits, single (2026)
inputs:
  beginning_stock_basis: 30000
  interest_income: 1000
  distributions: 8000
  nondeductible: 2000
  debt_basis: 40000
  k1_loss: 90000
  not_at_risk: 10000
  schedule_c_loss: 240000
  ebl_threshold: 256000
steps:
  - stock_basis_before_loss: beginning_stock_basis + interest_income - distributions - nondeductible
  - basis_limit: stock_basis_before_loss + debt_basis
  - allowed_after_basis: min(k1_loss, basis_limit)
  - suspended_basis: k1_loss - allowed_after_basis
  - allowed_after_at_risk: allowed_after_basis - not_at_risk
  - suspended_at_risk: allowed_after_basis - allowed_after_at_risk
  - net_business_loss: allowed_after_at_risk + schedule_c_loss
  - excess_business_loss: max(net_business_loss - ebl_threshold, 0)
  - deducted_2026: net_business_loss - excess_business_loss
expected:
  stock_basis_before_loss: 21000.00
  basis_limit: 61000.00
  suspended_basis: 29000.00
  allowed_after_at_risk: 51000.00
  suspended_at_risk: 10000.00
  net_business_loss: 291000.00
  excess_business_loss: 35000.00
  deducted_2026: 256000.00
```

Carryforwards into 2027:

| Carried (USD) | Limit that stopped it | What frees it |
| --- | --- | --- |
| 29,000 | Section 1366(d), basis | New stock or debt basis in a later year (Form 7203 Part III); lost if she disposes of all her stock, except a section 1041 transfer |
| 10,000 | Section 465, at-risk | An increase in her amount at risk in the activity (Form 6198) |
| 35,000 | Section 461(l), excess business loss | Used as a net operating loss under section 172 (Form 172) |

**Case 2, a distribution over basis and the repayment trap.** Same facts, but the 2026 distribution is 35,000 instead of 8,000. Basis before distributions is 31,000, so 31,000 is tax-free and 4,000 is capital gain on Form 8949; her 40,000 of debt basis does not cover any of the distribution, and stock basis is then 0. The 2,000 of nondeductible expenses comes next in the Reg. 1.1367-1(f) order and, with no stock basis left, reduces debt basis to 38,000 (Reg. 1.1367-2). That 38,000 is all the basis left for the loss, so 52,000 of the 90,000 loss is suspended. For this variant too, the full 38,000 passing basis uses all remaining debt basis, even if a later limit suspends a deduction. Then in 2027 the corporation repays 10,000 of the note and 2027 has no net increase to restore debt basis: her basis in the note is 0 and the whole 10,000 is gain, capital gain on Form 8949 and Schedule D because the debt is a formal note. She files Form 7203 for 2027 because she received a loan repayment.

```oa-check
name: Distribution over stock basis, then repayment of a zero-basis note
inputs:
  basis_before_distribution: 31000
  distribution: 35000
  debt_basis: 40000
  nondeductible: 2000
  k1_loss: 90000
  repayment_2027: 10000
  note_basis_2027: 0
steps:
  - tax_free: min(distribution, basis_before_distribution)
  - capital_gain_distribution: distribution - tax_free
  - stock_basis_after: max(basis_before_distribution - distribution, 0)
  - basis_limit: stock_basis_after + debt_basis - nondeductible
  - suspended_basis: k1_loss - min(k1_loss, basis_limit)
  - repayment_gain: repayment_2027 - min(repayment_2027, note_basis_2027)
expected:
  tax_free: 31000.00
  capital_gain_distribution: 4000.00
  basis_limit: 38000.00
  suspended_basis: 52000.00
  repayment_gain: 10000.00
```

## Filing and payment

After the limits, report nonpassive box 1 income/loss on Schedule E (Form 1040), line 28 column (i) or (k) in the read 2025 instructions; passive amounts go through Form 8582. Report K-1 items in the shareholder year in which the corporation’s tax year ends. Keep released prior-year losses separately identified and keep a schedule by year, activity and limiting rule. Attach the required loss-limitation forms, not the K-1 itself unless the backup-withholding exception applies. Final 2026 edition-specific line changes remain on the filing hold above. ([K-1 instructions, Purpose, Part III and Box 1](https://www.irs.gov/instructions/i1120ssk))

For an ordinary calendar-year individual Form 1040, the 2026 return is due **15 April 2027**; a timely automatic filing extension ordinarily gives **15 October 2027**, without extending payment. Overseas, disaster and other special deadline relief needs separate checking. ([§6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm); [IRS extension guidance](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return); [§6151(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap62-subchapA-sec6151.htm))

### Corporation filing points retained from the historical Guide

These are distinct from the shareholder’s deduction. Confirm the Form 2553 election was accepted and remains in effect; do not file for a year before it takes effect. Prepare Form 1120-S, Schedule K and each shareholder’s K-1 with the pro rata ordinary business result in box 1, separately identifying each activity. Furnish each K-1 by the return’s filing due date. ([Form 1120-S instructions, Who Must File and Schedule K-1](https://www.irs.gov/instructions/i1120s))

| Period and ordinary calendar-year deadline | Treatment | Official source |
|---|---|---|
| Historical tax year 2025 | Form 1120-S due 16 March 2026 because 15 March was Sunday | [2025 instructions, When To File](https://www.irs.gov/instructions/i1120s) |
| Tax year 2026 | Form 1120-S due 15 March 2027; fiscal years ordinarily use the 15th day of the third month after year end | [§6072(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) |

Form 7004 generally must be filed by the regular due date to request a filing extension; any corporate tax due ordinarily remains payable by the unextended due date. Dissolution, S termination and §336(e) transactions can change the return period/deadline: hold those rather than use this calendar-year row. ([Form 1120-S instructions, Extension and Tax Payments](https://www.irs.gov/instructions/i1120s))

**Historical penalty hold:** the earlier Guide’s USD 340 per incorrect/late K-1, USD 680 for intentional disregard, and 10% alternative are not a complete penalty calculation and must not be used for a 2026 return. They omit correction timing, caps, reasonable cause, and the correct furnishing-year inflation amount. No penalty liability is calculated here. Check this point with one of our partner accountants. ([2025 instructions, Failure to furnish information timely](https://www.irs.gov/instructions/i1120s))

Keep corporate records as long as needed for tax administration; the instructions’ usual period is 3 years after each shareholder return’s due date or filing date, whichever is later. Keep property-basis records as long as needed for original/replacement basis and retain filed returns; do not discard a shareholder’s continuing basis or suspended-loss evidence just because 3 years passed. ([Recordkeeping](https://www.irs.gov/instructions/i1120s); [Form 7203 record notice](https://www.irs.gov/instructions/i7203))

## When to refuse or refer

Each hold below means no usable conclusion for the affected issue. Check this point with one of our partner accountants.

| Issue from the original Guide | Destination or hold |
|---|---|
| R-K1-NOBASIS: no reliable beginning basis or records | Rebuild from records; hold loss deduction until supported |
| R-K1-DEBT / R-K1-GUAR: disputed direct debt, back-to-back/entity loans, guarantee payments, restructuring or forgiveness | Hold the debt-specific result; do not default missing loan documents to ordinary gain |
| R-K1-BASISCASES: §351 property/liabilities, gifts including below-basis value, inherited stock/IRD, multiple stock blocks or midyear transfers | Hold the acquisition/transfer computation; ordinary cash-purchase basis is not a substitute |
| R-K1-TERM: terminated election, post-termination transition period | Apply specialist transition computation; do not assume annual debt-basis relief |
| At-risk special cases: qualified nonrecourse financing, interested/related lenders, pre-1987 real property, grouping/separation or recapture | Hold the special result until the exception and activity allocation are established |
| R-K1-PASSIVE: rental boxes 2/3, grouping, real estate professional, former-passive activity or special farming tests | Hold special treatment; the ordinary box 1 tests do not decide these exceptions |
| R-K1-OTHER: partnership, reasonable compensation, QBI | `us-form-1065-partnership`, `us-s-corp-election-decision`, `us-qbi-deduction` |
| C corporation return / distribution or repayment capital gains / individual-return assembly | `us-form-1120-c-corp`, `us-capital-gains-and-losses`, `us-form-1040-individual-return` |
| R-K1-ENTITY: election validity/end, complete entity-return preparation, extensions and penalty liability beyond the limited filing points above | Hold disputed election or entity-return conclusions; extension routing: `us-corporate-extension-form-7004-and-the` |
| R-K1-STATE: state basis, conformity and NOLs | Use the relevant state Guide and hold any unproven state result |

Circular 230 §10.37: this reference does not replace a written-advice analysis of the actual facts, applicable law and reasonable assumptions. Do not use its hypothetical cases as filing advice.

## Sources

Official US government material. Read on 2026-11-27 only the operative portions listed; this is not a claim to have read each full publication. Earlier-year instructions support unchanged mechanics and clearly labelled historical facts, not unconfirmed 2026 form revisions.

| Source and portions read | URL | Read on |
|---|---|---|
| IRS stock/debt basis: loss order, responsibility, distributions and nondeductibles | https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis | 2026-11-27 |
| Form 7203 instructions (12/2022): filing triggers, Parts I–III, elections, debt gain character conflict and record notice | https://www.irs.gov/instructions/i7203 | 2026-11-27 |
| K-1 shareholder instructions (2025): loss limits, participation, Part III, Box 1 and reporting years | https://www.irs.gov/instructions/i1120ssk | 2026-11-27 |
| Form 6198 instructions (11/2025): filing triggers, excluded borrowing, exceptions and activity rules | https://www.irs.gov/instructions/i6198 | 2026-11-27 |
| Form 8582 instructions (2025): participation evidence, tests, dispositions and carryover | https://www.irs.gov/instructions/i8582 | 2026-11-27 |
| Form 461 instructions (2025): historical threshold, filing trigger, definitions and NOL | https://www.irs.gov/instructions/i461 | 2026-11-27 |
| Rev. Proc. 2025-32 §4.31: 2026 excess business loss threshold | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| §1366(a),(b),(d): allocation, character, basis and transition period | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1366.htm | 2026-11-27 |
| §1367(a),(b): basis categories, taxable income and debt restoration | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1367.htm | 2026-11-27 |
| Reg. 1.1366-2(a): direct debt, guarantees, basis limitation/proration, transfers | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1366-2.pdf | 2026-11-27 |
| Reg. 1.1367-1(b)–(g): basis, timing, default and elective order | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-1.pdf | 2026-11-27 |
| Reg. 1.1367-2(a)–(d): debt reduction, restoration and open accounts | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf | 2026-11-27 |
| §465(a),(b),(d),(e): at-risk amount, excluded borrowing and recapture | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec465.htm | 2026-11-27 |
| §469(b),(c),(e),(f),(g): passive definition, excluded income, carryover and disposition | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm | 2026-11-27 |
| Reg. 1.469-5T(a)–(d): seven participation tests and definitions | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf | 2026-11-27 |
| §461(l)(2)–(4): unchanged computational rules; end date/inflation read with amending Acts | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm | 2026-11-27 |
| P.L. 117-2 §9041: extension applicable in 2026 | https://www.govinfo.gov/content/pkg/PLAW-117publ2/html/PLAW-117publ2.htm | 2026-11-27 |
| P.L. 117-169 §13903(b): extension applicable after 2026 | https://www.govinfo.gov/content/pkg/PLAW-117publ169/html/PLAW-117publ169.htm | 2026-11-27 |
| P.L. 119-21 §70601: permanence and inflation reset, respective effective dates | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-27 |
| Form 1120-S instructions (2025): election, K-1 preparation, deadlines, payment, historical penalty and retention | https://www.irs.gov/instructions/i1120s | 2026-11-27 |
| §6072(a),(b): individual and S corporation filing deadlines | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-27 |
| §6151(a): payment without filing extension | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap62-subchapA-sec6151.htm | 2026-11-27 |
| IRS extension guidance: request by April due date, October filing, payment and relief exceptions | https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-27 |

Not yet confirmed: final 2026 form-specific line/filing-trigger changes, unwritten excess-debt gain character, historical K-1 penalty liability and the specialist case outcomes expressly held above are non-usable. Check this point with one of our partner accountants.
