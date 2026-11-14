---
name: us-divorce-alimony-and-property
description: How a US divorce or separation is treated on the federal income tax return for 2026. Alimony under an instrument executed after 2018 (or a pre-2019 instrument modified to adopt the new rule) is neither deductible by the payer nor income to the recipient; alimony under an older instrument stays deductible and taxable. Property transfers between spouses or incident to divorce under section 1041 carry no gain or loss and the recipient takes the transferor's basis (1 year, or 6 years under the instrument). Filing status follows marital status on 31 December (section 7703), with the head of household route for a spouse living apart. The child dependency release on Form 8332, and retirement plan splits under a qualified domestic relations order (QDRO) with no 10% early distribution tax. Includes the decision case of filing jointly or separately in the final married year, with 2026 brackets from Rev. Proc. 2025-32. Trigger on "divorce tax", "alimony deductible", "is alimony taxable", "Form 8332", "QDRO", "section 1041", "file jointly while divorcing", "head of household separated". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# US divorce: alimony, property transfers, filing status and children, tax year 2026

> **Source-cited draft.** Built from IRS Publication 504 (2025), Form 8332 (Rev. December 2025), Rev. Proc. 2025-32 and 26 U.S.C. 72(t), 152(e), 402(e), 414(p), 1041 and 7703, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Alimony paid under a divorce or separation instrument **executed after 2018** is not deductible by the payer and not taxable to the recipient. Alimony under an instrument executed **on or before 31 December 2018** keeps the old rule (deductible and taxable) unless the instrument was later modified and the modification expressly adopts the new rule. Transfers of property between spouses, or to a former spouse incident to divorce, produce **no gain or loss**; the recipient takes over the transferor's basis. Filing status depends on marital status on **31 December 2026**: still married (no final decree) means married filing jointly or separately, unless one spouse qualifies as head of household by living apart for the last 6 months with a child. The custodial parent can release the child's credits to the other parent on **Form 8332**. A retirement plan split under a **QDRO** is taxed to the former spouse who receives it, without the 10% early distribution tax.

## Scope and who this is for

In scope: either spouse's 2026 Form 1040 in the year of a separation or divorce, and later years under the same instrument: alimony, child support, property settlements, filing status, which parent claims the children, and retirement plan and IRA splits.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Standard deduction amounts, the full return | `us-federal-income-tax-return-1040` |
| Child tax credit and earned income credit amounts and tests | `us-child-tax-credit-and-eitc` |
| Gift tax on a property settlement outside section 2516 | `us-estate-gift-706-709` |
| Home sale exclusion after divorce | `us-federal-income-tax-return-1040` (section 121) |
| Basis loss of S corporation stock moved under section 1041 | `us-1120-corporation-return-schedule-ordinary-business` |
| Innocent spouse relief (Form 8857) | `us-irs-collections-and-controversy` |
| State community property splits | the state's income tax skill |

## Ask the client first

1. **The date the divorce or separation instrument was executed**, and every later modification: does any modification expressly say the alimony is not deductible or not includible?
2. **Status on 31 December 2026:** final decree of divorce or separate maintenance obtained by then? An interlocutory decree is not final.
3. **Living arrangements:** did the spouses live apart for the whole last 6 months of 2026? Who paid more than half the cost of the home? Which children lived with whom, and for how many nights?
4. **Payments:** amounts paid, how the instrument labels them (alimony, child support, property), and whether any amount drops when a child reaches an age or leaves home (treated as child support).
5. **Property moved:** what, when, the transferor's basis and holding period, and whether the recipient is a nonresident alien.
6. **Retirement assets:** plan names, whether a QDRO was signed and accepted by the plan, and any IRA transfers under the decree.
7. **Has a Form 8332 been signed**, for which years, and has it been revoked?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Standard deduction, married filing jointly | USD 32,200 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, single and married filing separately | USD 16,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, head of household | USD 24,150 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Married filing jointly: top of the 12% band (tax at that point USD 11,600) | USD 100,800 | [Rev. Proc. 2025-32, Table 2](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Married filing jointly: top of the 22% band | USD 211,400 | [Rev. Proc. 2025-32, Table 2](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Married filing separately: top of the 10% band | USD 12,400 | [Rev. Proc. 2025-32, Table 4](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Married filing separately: top of the 22% band (tax at that point USD 17,966) | USD 105,700 | [Rev. Proc. 2025-32, Table 4](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Married filing separately: top of the 24% band | USD 201,775 | [Rev. Proc. 2025-32, Table 4](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Alimony cut-off: instruments executed after | 31 December 2018 | [IRS Pub. 504 (2025), Alimony](https://www.irs.gov/pub/irs-pdf/p504.pdf) |
| Section 1041: transfer incident to divorce if within this period after the marriage ends | 1 year | [26 U.S.C. 1041(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1041.htm) |
| Section 1041: transfer under the instrument presumed related to the end of the marriage if within | 6 years | [IRS Pub. 504 (2025), Property Settlements](https://www.irs.gov/pub/irs-pdf/p504.pdf) |
| Head of household while married: spouse not in the household during the last | 6 months of the year | [26 U.S.C. 7703(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7703.htm) |
| Capital loss deduction limit, married filing separately | USD 1,500 | [IRS Pub. 504 (2025), Married Filing Separately](https://www.irs.gov/pub/irs-pdf/p504.pdf) |

### Step 1: filing status for 2026

1. **Final decree of divorce or separate maintenance by 31 December 2026:** unmarried for the whole year. File single, or head of household if a qualifying person lives with the taxpayer for more than half the year and the taxpayer pays more than half the cost of the home. Source: [26 U.S.C. 7703(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7703.htm).
2. **No final decree by 31 December 2026:** married for the whole year, even if separated. File jointly or separately.
3. **Married but "considered unmarried":** a spouse who files separately can use head of household if, for 2026, the spouse did not live in the home during the last 6 months, the taxpayer paid more than half the cost of the home, and the home was the main home of the taxpayer's child for more than half the year. Source: [26 U.S.C. 7703(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7703.htm).
4. **Joint return consequences.** Both spouses are jointly and individually liable for the whole tax, interest and penalties on a joint return, even if the decree later says otherwise. Relief exists (innocent spouse, separation of liability, equitable relief on Form 8857). Source: [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).
5. **Separate return consequences** (Pub. 504's list): generally higher rates; no education credits and no student loan interest deduction; no earned income credit unless there is a qualifying child; the child and dependent care credit is generally unavailable unless legally separated or living apart; capital loss limit USD 1,500; and if one spouse itemizes, the other cannot take the standard deduction. A separate return can be changed to a joint one later, generally within 3 years of the due date. Source: [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).

### Step 2: alimony

6. **Instrument executed after 31 December 2018:** payments are not deductible (no Schedule 1 line 19a entry) and not income (no Schedule 1 line 2a entry). Source: [IRS Pub. 504 (2025), Alimony](https://www.irs.gov/pub/irs-pdf/p504.pdf).
7. **Instrument executed on or before 31 December 2018, not modified to adopt the new rule:** the old rules apply. Payer deducts on Schedule 1 line 19a and gives the recipient's SSN; recipient includes on line 2a and may count it as compensation for IRA contributions. To be alimony the payment must be cash, under the instrument, not designated as non-alimony, the parties not living in the same household once divorced or legally separated, no liability after the recipient's death, and not child support. Source: [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).
8. **Recapture (old instruments only):** if payments fall by more than USD 15,000 in the second or third year, part of the earlier deduction is recaptured in the third year (Pub. 504 Worksheet 1). Source: [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).
9. **Child support** is never deductible or taxable, under any instrument. A payment that falls on a child-related event (age, leaving school, marriage) is child support to that extent. If less than the full amount is paid, it applies first to child support. Source: [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).
10. **A separation agreement signed before 2019 and a decree after 2018:** the instrument that governs the payment decides. Pub. 504 examples show payments under the earlier written separation agreement keep the old rule only while that agreement governs; once the later decree governs, the new rule applies.

### Step 3: property transfers (section 1041)

11. **No gain or loss** on a transfer to a spouse, or to a former spouse if incident to the divorce, even if paid for with cash, release of marital rights or assumed debt. The property is treated as a gift and the recipient takes the transferor's **adjusted basis** (and holding period). Source: [26 U.S.C. 1041(a), (b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1041.htm).
12. **Incident to divorce** = within 1 year after the marriage ends, or related to the end of the marriage (under the instrument and within 6 years; later transfers are presumed unrelated unless shown otherwise). Source: [26 U.S.C. 1041(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1041.htm), [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).
13. **Exceptions:** recipient is a nonresident alien (section 1041(d)); transfers in trust where liabilities exceed basis (gain on the excess); an installment obligation transferred in trust. Source: [26 U.S.C. 1041(d), (e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1041.htm).
14. **Tell the recipient:** assets with the same market value are not worth the same after tax. Low-basis stock or a rental with depreciation carries a built-in tax the recipient will pay; cash carries none.

### Step 4: retirement plans and IRAs

15. **QDRO.** A qualified domestic relations order splits an employer plan. Payments to the spouse or former spouse alternate payee are taxed to that spouse, not the participant; payments to a child are taxed to the participant. Source: [26 U.S.C. 402(e)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec402.htm), [26 U.S.C. 414(p)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartB-sec414.htm).
16. **No 10% early distribution tax** on a distribution to an alternate payee under a QDRO, at any age. The alternate payee may instead roll an eligible distribution to an IRA. Source: [26 U.S.C. 72(t)(2)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec72.htm), [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).
17. **IRAs do not use a QDRO.** A transfer of an IRA interest under a decree or a written instrument incident to it is not taxable; from the transfer date it is the recipient's IRA. A withdrawal by the owner, paid over to the spouse, is taxed to the owner (and the 10% tax can apply). The QDRO 10% exception does not cover IRAs. Source: [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf).

### Step 5: children (Form 8332)

18. **The custodial parent** is the one the child lived with for more nights in 2026 (equal nights: the parent with the higher AGI). By default the custodial parent claims the child.
19. **Release.** The custodial parent can release the claim with Form 8332 (or a statement with the same information) for one year, specified years or all future years; the noncustodial parent attaches it every year claimed. The release passes only the child tax credit, additional child tax credit and credit for other dependents. It never passes head of household status, the earned income credit or the dependent care credit, which stay with the custodial parent. Revocation is Part III of Form 8332, effective no earlier than the year after the noncustodial parent is notified. Sources: [Form 8332](https://www.irs.gov/pub/irs-pdf/f8332.pdf), [26 U.S.C. 152(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partV-sec152.htm), [IRS Pub. 504 (2025)](https://www.irs.gov/pub/irs-pdf/p504.pdf). For the credit amounts see `us-child-tax-credit-and-eitc`.
20. **Attaching the decree instead.** Pub. 504 allows pages of the decree or agreement to be attached instead of Form 8332 only where it went into effect after 1984 and before 2009 and states the three conditions Pub. 504 lists. For any later decree, use Form 8332 or a statement with the same information.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Divorce final 30 December 2026 | Unmarried for all of 2026: single or head of household, no joint return |
| Separated since March 2026, no final decree | Married for 2026: joint or separate; head of household possible if the 7703(b) tests are met |
| Pre-2019 decree modified in 2026 to change the amount only | Old rule continues: deductible and taxable |
| Pre-2019 decree modified in 2026 and the modification says the new rule applies | New rule from then: not deductible, not taxable |
| Alimony paid to the former spouse's landlord under the instrument | Can be alimony (old instruments) if it otherwise qualifies |
| House transferred to the former spouse 2 years after divorce under the decree | Section 1041 applies: no gain, carryover basis |
| Stock transferred to a nonresident alien spouse | Section 1041 does not apply: gain or loss recognized |
| 401(k) split under a QDRO, former spouse aged 40 takes cash | Taxable to the former spouse, no 10% additional tax |
| IRA owner withdraws cash to pay the former spouse | Taxable to the owner; 10% tax may apply; no QDRO exception |
| Noncustodial parent has signed Form 8332 | May claim the child tax credit; cannot claim head of household or earned income credit for that child |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Execution date of the instrument | Treat alimony as not deductible and not taxable until the instrument is seen |
| Whether a decree is final at 31 December | Married; ask for the decree |
| Transferor's basis in property received | Unknown basis; ask the former spouse's records, do not use market value |
| Signed Form 8332 | Custodial parent claims the child |
| Whether a plan split used a QDRO | Treat as the participant's distribution until the order is seen |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Both parents claim the same child | IRS tie-breaker and a notice to one parent |
| Payer deducts alimony under a post-2018 decree | Disallowed deduction, penalties |
| Recipient of pre-2019 alimony not reporting it | IRS matches the payer's deduction to the recipient's SSN |
| Joint return with a spouse whose income or deductions are unclear | Joint and several liability |
| Low-basis assets offered in the settlement | Built-in tax on later sale |

## Worked cases

**Case 1, a decision: file jointly or separately in the final married year?** Ana and Ben separated in 2026 but the divorce will not be final until 2027, so both are married at 31 December 2026. They have no children and take the standard deduction. Ana's wages are USD 150,000; Ben's are USD 20,000.

Jointly: USD 170,000 less USD 32,200 = USD 137,800 taxable; tax = USD 11,600 plus 22% of the USD 37,000 over USD 100,800 = USD 19,740. Separately: Ana USD 150,000 less USD 16,100 = USD 133,900; tax = USD 17,966 plus 24% of the USD 28,200 over USD 105,700 = USD 24,734. Ben USD 20,000 less USD 16,100 = USD 3,900 at 10% = USD 390. Separate total USD 25,124. The joint return saves USD 5,384. File jointly if both trust the other's figures and agree in writing how to share the tax and any refund; file separately (and pay the USD 5,384) if either spouse doubts the other's reporting, because the joint return makes each liable for all of it. If they file separately now, they can still amend to joint later, generally within 3 years; going from joint back to separate after the due date is not possible.

```oa-check
name: Final married year, joint against separate (2026)
inputs:
  wages_a: 150000
  wages_b: 20000
  std_mfj: 32200
  std_mfs: 16100
steps:
  - mfj_taxable: wages_a + wages_b - std_mfj
  - mfj_tax: 11600 + (mfj_taxable - 100800) * 0.22
  - a_taxable: wages_a - std_mfs
  - a_tax: 17966 + (a_taxable - 105700) * 0.24
  - b_taxable: wages_b - std_mfs
  - b_tax: b_taxable * 0.10
  - mfs_total: a_tax + b_tax
  - joint_saving: mfs_total - mfj_tax
expected:
  mfj_taxable: 137800.00
  mfj_tax: 19740.00
  a_tax: 24734.00
  b_tax: 390.00
  mfs_total: 25124.00
  joint_saving: 5384.00
```

**Case 2, old and new alimony rules, and a section 1041 transfer.** Under a decree, Carl pays Dana USD 2,000 a month (USD 24,000 a year). Carl's top rate is 24% and Dana's is 12%. If the decree was executed in 2017 and never modified to adopt the new rule, Carl deducts USD 24,000 (saving USD 5,760) and Dana reports USD 24,000 (costing USD 2,880): the couple is USD 2,880 better off in total. If the decree was executed in 2019, neither entry is made: Carl saves nothing and Dana owes nothing on it. In the same decree Dana receives shares worth USD 100,000 that Carl bought for USD 30,000: no gain for Carl, and Dana's basis is USD 30,000, so USD 70,000 of gain waits for her when she sells.

```oa-check
name: Alimony old against new rule, and carryover basis
inputs:
  alimony: 24000
  payer_rate: 0.24
  recipient_rate: 0.12
  shares_value: 100000
  carl_basis: 30000
steps:
  - payer_saving_old: alimony * payer_rate
  - recipient_cost_old: alimony * recipient_rate
  - net_saving_old: payer_saving_old - recipient_cost_old
  - net_saving_new: alimony * 0
  - gain_on_transfer: 0
  - dana_basis: carl_basis
  - built_in_gain: shares_value - dana_basis
expected:
  payer_saving_old: 5760.00
  recipient_cost_old: 2880.00
  net_saving_old: 2880.00
  net_saving_new: 0.00
  dana_basis: 30000.00
  built_in_gain: 70000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-DV-COMMUNITY | Community property state, separate returns | Refer: income splits follow state law (Pub. 555) |
| R-DV-INNOCENT | A spouse wants relief from a joint liability | Refer: Form 8857 (`us-irs-collections-and-controversy`) |
| R-DV-REDEMPTION | Closely held stock redeemed by the company as part of the divorce | Refer: Reg. 1.1041-2 decides who is taxed |
| R-DV-NRA | Transfer to a nonresident alien spouse | Refer: gain recognized, possible withholding |
| R-DV-RECAPTURE | Old-instrument alimony that fell by more than USD 15,000 | Compute Pub. 504 Worksheet 1; refer if disputed |
| R-DV-PENSION | Defined benefit plan split, or a government or military pension | Refer: plan-specific rules |

## Filing and payment

The 2026 Form 1040 (either status) is due 15 April 2027. Old-rule alimony: payer on Schedule 1 line 19a with the recipient's SSN and the date of the instrument; recipient on Schedule 1 line 2a. Form 8332 is attached to the noncustodial parent's return each year it is used. QDRO distributions are reported on Form 1099-R in the alternate payee's name. Line numbers are those of the 2025 Schedule 1; check the 2026 Schedule 1 when filing.

## Completion checklist

- Decree or separation instrument read: execution date, every modification, the alimony and child support wording.
- Filing status fixed by status on 31 December 2026; head of household tests checked for a separated spouse.
- Joint and separate both computed in the final married year (Case 1), with the liability point explained.
- Each property received: transferor's basis and holding period on file.
- Plan splits: QDRO seen; IRA transfers made trustee to trustee under the decree.
- Form 8332 signed for the right years, or the custodial parent claims the child.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Publication 504 (2025), Divorced or Separated Individuals. Read for marital status at the last day of the year, joint liability, separate-return rules (USD 1,500 capital loss), considered unmarried, custodial parent and Form 8332, alimony before and after 2018, recapture (USD 15,000), QDRO, IRA transfers and property settlements (1 year, 6 years). | https://www.irs.gov/pub/irs-pdf/p504.pdf | 2026-11-13 |
| Form 8332 (Rev. December 2025). Read for release for one, specified or all future years and Part III revocation. | https://www.irs.gov/pub/irs-pdf/f8332.pdf | 2026-11-13 |
| Rev. Proc. 2025-32. Read for 2026 standard deductions (USD 32,200, USD 16,100, USD 24,150) and Tables 2 and 4 (joint and separate brackets). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 1041 (govinfo). Read for (a) no gain or loss, (b) gift treatment and carryover basis, (c) 1 year or related to cessation, (d) nonresident alien, (e) trusts. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1041.htm | 2026-11-13 |
| 26 U.S.C. 7703 (govinfo). Read for (a) status at the close of the year and (b) married individuals living apart, last 6 months. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7703.htm | 2026-11-13 |
| 26 U.S.C. 152 (govinfo). Read for (e) children of divorced or separated parents and the written declaration. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partV-sec152.htm | 2026-11-13 |
| 26 U.S.C. 414 (govinfo). Read for (p) qualified domestic relations order defined. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartB-sec414.htm | 2026-11-13 |
| 26 U.S.C. 402 (govinfo). Read for (e)(1)(A) alternate payee spouse treated as distributee. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec402.htm | 2026-11-13 |
| 26 U.S.C. 72 (govinfo). Read for (t)(2)(C) payments to alternate payees under a QDRO. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec72.htm | 2026-11-13 |

Not yet confirmed: Publication 504 for 2026 and the 2026 Schedule 1 were not published when read, so the rules are taken from the 2025 edition (none of them is indexed or changed by Public Law 119-21) and the Schedule 1 line numbers (2a, 19a) are the 2025 ones.
