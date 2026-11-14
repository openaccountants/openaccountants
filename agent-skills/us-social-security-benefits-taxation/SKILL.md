---
name: us-social-security-benefits-taxation
description: "Work out how much of a person's US Social Security (and tier 1 railroad retirement) benefits is taxable for tax year 2026 under 26 U.S.C. 86. Covers provisional income (modified AGI plus tax-exempt interest plus half the benefits), the 50% and 85% tiers, the statutory base amounts of USD 25,000 and USD 32,000 and adjusted base amounts of USD 34,000 and USD 44,000 (zero for a married person filing separately who lived with the spouse), repayments, the lump-sum election, and how the taxable amount raises AGI and so the 2025 to 2028 senior deduction phase-out. Trigger on \"is my Social Security taxable\", \"taxable Social Security\", \"provisional income\", \"combined income\", \"SSA-1099\", \"85% of benefits\", \"tax torpedo\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-social-security-benefits-taxation"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Taxable Social Security benefits, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 86 on govinfo.gov, Public Law 119-21 (section 70103), IRS Pub. 915 (2025) and the 2026 Form 8606, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Up to 85% of Social Security benefits can be taxable, never more. Add modified AGI, tax-exempt interest and half the benefits: that is provisional income. If it is no more than **USD 25,000** (single, head of household) or **USD 32,000** (joint), nothing is taxable. Between that and **USD 34,000** / **USD 44,000**, up to 50% is taxable. Above it, up to 85% is taxable. A married person filing separately who lived with the spouse at any time in the year has base amounts of zero, so up to 85% is taxable from the first dollar. These amounts are fixed in the statute and are not indexed for inflation, and Public Law 119-21 did not change section 86.

## Scope and who this is for

In scope: one individual or married couple with Social Security retirement, survivor or disability benefits (Form SSA-1099) or tier 1 railroad retirement benefits (Form RRB-1099), for tax year 2026. The result is the taxable amount on Form 1040, line 6b.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The rest of Form 1040, the standard deduction and the tax brackets | `us-federal-income-tax-return-1040` |
| The senior deduction for 2025 to 2028 (amount and phase-out) | `us-new-deductions-tips-overtime-senior-car-loan` |
| IRA distributions, Roth conversions and Form 8606 | `us-ira-and-roth-conversions-8606` |
| Required minimum distributions and qualified charitable distributions | `us-secure-2-and-retirement-updates` |
| Nonresident aliens receiving benefits | `us-form-1040-nr-nonresident-return` |
| State tax on benefits | the state's income tax skill |

## Ask the client first

1. **Filing status for 2026**, and, if married filing separately, whether the spouses lived apart for the **whole** year. Living together for even one day sets the base amounts to zero.
2. **Form SSA-1099 and RRB-1099, box 5** (net benefits, after repayments) for each spouse.
3. **All other income** that goes into AGI: wages, pensions, IRA distributions and Roth conversions, interest, dividends, capital gains, business and rental income.
4. **Tax-exempt interest** (municipal bond interest, Form 1099-INT box 8 and 1099-DIV box 12). It counts in provisional income even though it is not taxed.
5. **Excluded foreign or U.S. possession income** (Form 2555, Puerto Rico or other possession income), student loan interest deduction, and adoption or savings bond exclusions. These are added back.
6. **Any benefits received in 2026 that relate to earlier years** (a back-payment). The lump-sum election may lower the tax.
7. **Age of each spouse at 31 December 2026**, for the senior deduction.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Base amount, single, head of household, qualifying surviving spouse, and married filing separately living apart all year | USD 25,000 | [26 U.S.C. 86(c)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| Base amount, joint return | USD 32,000 | [26 U.S.C. 86(c)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| Base amount, married filing separately and lived with the spouse at any time | zero | [26 U.S.C. 86(c)(1)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| Adjusted base amount, other than joint | USD 34,000 | [26 U.S.C. 86(c)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| Adjusted base amount, joint return | USD 44,000 | [26 U.S.C. 86(c)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| Adjusted base amount, married filing separately and lived with the spouse | zero | [26 U.S.C. 86(c)(2)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| Share of benefits counted in provisional income | 50% (one-half) | [26 U.S.C. 86(b)(1)(A)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| First tier: taxable share | 50% (one-half) | [26 U.S.C. 86(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |
| Second tier: taxable share of the excess, and the overall cap on benefits | 85% | [26 U.S.C. 86(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) |

None of these amounts is indexed. The same figures apply for 2025, 2026 and later years unless Congress changes section 86.

### Step 1: modified AGI for section 86

Start with AGI **without** the taxable benefits (section 86 itself) and without the exclusions and deductions in [26 U.S.C. 86(b)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm): add back the student loan interest deduction (221), the savings bond (135) and adoption (137) exclusions, the foreign earned income and housing exclusions (911) and the possession exclusions (931, 933). Add **tax-exempt interest** (86(b)(2)(B)).

The below-the-line deductions on Schedule 1-A (tips, overtime, senior, car loan interest) come after AGI and do not reduce modified AGI here.

### Step 2: provisional income

Provisional income = modified AGI (step 1) + one-half of the benefits (box 5 of every SSA-1099 and RRB-1099, both spouses on a joint return).

### Step 3: the taxable amount

Let B be the benefits, P the provisional income, base and adjusted base the amounts in the table.

1. If P is no more than the base amount: nothing is taxable. Stop.
2. **First tier:** T1 = the lesser of one-half of B, or one-half of (P minus the base amount). If P is no more than the adjusted base amount, T1 is the taxable amount. Stop.
3. **Second tier:** taxable amount = the lesser of
   - 85% of (P minus the adjusted base amount), plus the lesser of T1 or one-half of (adjusted base minus base) (USD 4,500 single, USD 6,000 joint); or
   - 85% of B.

One formula covers every case: taxable = min(85% x max(P minus adjusted base, 0) + min(T1, half of (adjusted base minus base)), 85% x B), with T1 = min(B / 2, max(P minus base, 0) / 2). Pub. 915 Worksheet 1 and the Form 1040 instructions worksheet do the same thing line by line.

### Step 4: where it goes and what it changes

- Form 1040 line 6a: gross benefits (box 5 total). Line 6b: the taxable amount.
- The taxable amount is part of AGI, so it raises every AGI-based limit: the **senior deduction** phase-out (modified AGI for that deduction is AGI plus excluded foreign and possession income: see `us-new-deductions-tips-overtime-senior-car-loan` for the amount and phase-out), the medical expense floor, the net investment income tax threshold and IRA deductibility (`us-ira-and-roth-conversions-8606`). For the IRA deduction test, AGI is taken **after** section 86 ([26 U.S.C. 219(g)(3)(A)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm)).
- The "tax torpedo": in the second tier every extra USD 1 of other income adds USD 1 plus USD 0.85 of benefits to taxable income, so the marginal rate is 1.85 times the bracket rate until 85% of benefits is reached.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Married filing separately, lived with the spouse at any time in 2026 | Base and adjusted base are zero: taxable = min(85% x P, 85% x B) in effect |
| Married filing separately, lived apart all year | Use the single amounts (USD 25,000 / USD 34,000) |
| Benefits repaid in 2026 (SSA-1099 box 4) | Box 5 is already net of repayments ([86(d)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm)). If box 5 is negative, none of the benefits is taxable; a repayment of benefits taxed in an earlier year may be an itemized deduction or a section 1341 credit (Pub. 915, Repayments More Than Gross Benefits) |
| Lump-sum back payment for earlier years | The client may elect under [86(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm) to compute the earlier-year portion using that year's income; it only lowers tax, it never amends the earlier return. Use the Pub. 915 lump-sum worksheets |
| Workers' compensation that reduced benefits | Treated as a benefit under 86(d)(3); it is in box 5 |
| Supplemental Security Income (SSI) | Not a section 86 benefit; not taxable |
| Medicare premiums deducted from benefits | Box 5 is before Medicare premiums; the premiums may be a medical expense on Schedule A |
| A Roth conversion or large IRA distribution in the year | Raises P; model it before converting (worked case 2) |
| Qualified Roth IRA distribution | Excluded from gross income, so not in P |
| Nonresident alien | Section 86 tiers do not apply; Pub. 915 says 85% of the benefits is subject to the nonresident tax unless a treaty applies; refer (R-SS-NRA) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether a separate filer lived with the spouse | Assume yes (base amounts zero); ask |
| Tax-exempt interest | Ask: never assume zero for a retiree with a brokerage account |
| SSA-1099 box 5 | Do not estimate from monthly benefit; ask for the form |
| Spouse's benefits on a joint return | Both spouses' box 5 go in; ask for both forms |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Provisional income within about USD 10,000 above the adjusted base | Tax torpedo zone: an extra distribution costs 1.85 times its size in taxable income |
| Box 5 negative | Repayment exceeds benefits: special treatment |
| Large back payment in box 3 for earlier years | Lump-sum election may save tax |
| Planned Roth conversion or capital gain | Raises taxable benefits and the senior deduction phase-out at once |

## Worked cases

**Case 1, single, in the 85% tier.** A single retiree has USD 30,000 of Social Security benefits (box 5), USD 40,000 of other AGI (pension and IRA) and USD 2,000 of tax-exempt municipal bond interest.

Provisional income: 40,000 + 2,000 + 15,000 = USD 57,000. That is over the USD 25,000 base, so T1 = the lesser of 15,000 or half of 32,000 (16,000) = USD 15,000. It is over the USD 34,000 adjusted base by USD 23,000: 85% of that is USD 19,550. Add the lesser of T1 or USD 4,500: USD 4,500. Total USD 24,050, below the cap of 85% x 30,000 = USD 25,500. Taxable benefits: **USD 24,050** on line 6b.

```oa-check
name: Taxable Social Security, single, 85% tier (2026)
inputs:
  benefits: 30000
  other_agi: 40000
  tax_exempt_interest: 2000
  base: 25000
  adjusted_base: 34000
steps:
  - provisional: other_agi + tax_exempt_interest + benefits / 2
  - tier1: min(benefits / 2, max(provisional - base, 0) / 2)
  - taxable: min(0.85 * max(provisional - adjusted_base, 0) + min(tier1, (adjusted_base - base) / 2), 0.85 * benefits)
expected:
  provisional: 57000.00
  tier1: 15000.00
  taxable: 24050.00
```

**Case 2, a decision: take an extra USD 10,000 from the traditional IRA or the Roth IRA?** A married couple filing jointly has USD 40,000 of benefits and USD 30,000 of other AGI. They need USD 10,000 more cash in 2026.

Without the extra withdrawal: provisional income 30,000 + 20,000 = USD 50,000, over the USD 44,000 adjusted base by USD 6,000. Taxable = 85% x 6,000 + the lesser of T1 (USD 9,000) or USD 6,000 = **USD 11,100**.

From the traditional IRA: provisional income becomes USD 60,000, USD 16,000 over the adjusted base. Taxable = 13,600 + 6,000 = **USD 19,600**, so USD 8,500 more of the benefits becomes taxable. Taxable income rises by USD 18,500 for USD 10,000 of cash.

From the Roth IRA (a qualified distribution, excluded from gross income): provisional income is unchanged and taxable benefits stay at USD 11,100. Recommend the Roth withdrawal if a qualified Roth balance exists and the couple's tax bracket now is not lower than the one they expect later; if the traditional IRA must be used, check the senior deduction phase-out on the higher AGI.

```oa-check
name: Extra withdrawal decision, joint, traditional against Roth (2026)
inputs:
  benefits: 40000
  other_agi: 30000
  extra_traditional: 10000
  base: 32000
  adjusted_base: 44000
steps:
  - p_without: other_agi + benefits / 2
  - t1_without: min(benefits / 2, max(p_without - base, 0) / 2)
  - taxable_without: min(0.85 * max(p_without - adjusted_base, 0) + min(t1_without, (adjusted_base - base) / 2), 0.85 * benefits)
  - p_with: other_agi + extra_traditional + benefits / 2
  - t1_with: min(benefits / 2, max(p_with - base, 0) / 2)
  - taxable_with: min(0.85 * max(p_with - adjusted_base, 0) + min(t1_with, (adjusted_base - base) / 2), 0.85 * benefits)
  - extra_taxable_benefits: taxable_with - taxable_without
  - added_taxable_income: extra_traditional + extra_taxable_benefits
expected:
  taxable_without: 11100.00
  taxable_with: 19600.00
  extra_taxable_benefits: 8500.00
  added_taxable_income: 18500.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-SS-NRA | Recipient is a nonresident alien (SSA-1042S) | Refer: 85% flat inclusion and treaty rules, `us-form-1040-nr-nonresident-return` |
| R-SS-1341 | Repayment exceeds benefits for the year and relates to benefits taxed in an earlier year | Refer: section 1341 claim-of-right computation |
| R-SS-LUMP | Lump-sum election across several earlier years | Compute with the Pub. 915 worksheets and earlier-year returns; a reviewer checks |
| R-SS-FOREIGN | Foreign social security (for example a UK State Pension) | Not a section 86 benefit; treaty rules decide; refer |

## Filing and payment

Report on the 2026 Form 1040 or 1040-SR, lines 6a and 6b, due **15 April 2027**; an extension to 15 October 2027 extends filing, not payment. Tax on benefits can be withheld by filing Form W-4V with the Social Security Administration, or paid by estimated tax: see `us-quarterly-estimated-tax`.

## Completion checklist

- Box 5 of every SSA-1099 and RRB-1099 for both spouses on line 6a.
- Filing status checked, and for a separate filer whether the spouses lived apart all year.
- Tax-exempt interest and the section 86(b)(2) add-backs included in modified AGI.
- Taxable amount never above 85% of benefits.
- Lump-sum election considered for back payments.
- Senior deduction and other AGI-based items rerun on the AGI that includes line 6b.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 86 (govinfo, 2024 edition). Read for (a) the 50% and 85% inclusion rules, (b) provisional income and modified AGI, (c) the base amounts (USD 25,000, USD 32,000, zero) and adjusted base amounts (USD 34,000, USD 44,000, zero), (d) repayments and workers' compensation, (e) the lump-sum election. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec86.htm | 2026-11-13 |
| Public Law 119-21 (govinfo). Read for section 70103 (the senior deduction and its modified AGI) and to confirm the Act does not amend section 86. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 219 (govinfo). Read for (g)(3)(A)(i): AGI for the IRA deduction is taken after section 86. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm | 2026-11-13 |
| IRS Pub. 915 (2025), Social Security and Equivalent Railroad Retirement Benefits. Read for Worksheet 1, tax-exempt interest in the test, the lump-sum election worksheets and repayments. | https://www.irs.gov/pub/irs-pdf/p915.pdf | 2026-11-13 |

Not yet confirmed: the 2026 edition of Pub. 915 and the 2026 Form 1040 instructions were not yet published when read, so the worksheet steps are taken from the 2025 edition; the section 86 amounts themselves are statutory and do not change.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-social-security-benefits-taxation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-social-security-benefits-taxation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
