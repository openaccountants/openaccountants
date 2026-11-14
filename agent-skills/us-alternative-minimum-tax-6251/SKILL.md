---
name: us-alternative-minimum-tax-6251
description: "Work out the 2026 US individual alternative minimum tax on Form 6251. Covers alternative minimum taxable income (the standard deduction or state and local taxes added back, incentive stock option exercises, private activity bond interest and other adjustments), the 2026 exemptions of USD 90,100 single, USD 140,200 joint and USD 70,100 separate, the phase-out from USD 500,000 and USD 1,000,000 at the new 50% rate under the One Big Beautiful Bill Act, the 26% and 28% rates with the USD 244,500 breakpoint, capital gains kept at their own rates, and the minimum tax credit on Form 8801. Trigger on \"AMT\", \"alternative minimum tax\", \"Form 6251\", \"ISO exercise AMT\", \"incentive stock options tax\", \"AMT exemption 2026\", \"Form 8801\", \"AMT credit\". Federal only, individuals only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-alternative-minimum-tax-6251"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US alternative minimum tax for individuals (Form 6251), tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32, Public Law 119-21 (the One Big Beautiful Bill Act) section 70107, 26 U.S.C. 55, 56 and 422, the 2025 Form 6251 and its instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** AMT is owed when the tentative minimum tax is more than the regular tax. For 2026 the exemption is **USD 90,100** (single and head of household), **USD 140,200** (joint) and **USD 70,100** (separate). It shrinks by **50 cents for each dollar** of alternative minimum taxable income above **USD 500,000** (single and separate) or **USD 1,000,000** (joint). The One Big Beautiful Bill Act lowered those thresholds and doubled the phase-out rate from 25%, so more high earners lose the exemption faster. The rate is 26% on the first **USD 244,500** of income above the exemption (USD 122,250 separate) and 28% above it. The most common trigger in practice is exercising incentive stock options and holding the shares.

## Scope and who this is for

In scope: an individual's 2026 Form 6251, the adjustments most clients meet (standard deduction or taxes, incentive stock options, private activity bond interest, depreciation differences in summary), and the minimum tax credit carried to later years on Form 8801.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Regular tax: brackets, standard deduction, filing status | `us-federal-income-tax-return-1040` |
| Capital gains rates and the 0% / 15% / 20% breakpoints | `us-capital-gains` |
| Restricted stock units, NSOs and the ISO disqualifying disposition in detail | `us-equity-compensation-restricted-stock-units-and` |
| Qualified small business stock exclusion | `us-section-1202-qsbs` |
| Foreign tax credit, including the AMT foreign tax credit | `us-foreign-tax-credit-1116` |
| Estates and trusts (Schedule I, Form 1041) | refer (see the refusal table) |
| State AMT (for example California) | the state's income tax skill |

## Ask the client first

1. **Filing status** and the regular-tax figures for 2026: taxable income (Form 1040 line 15), regular tax, and whether they itemize.
2. **If itemizing:** state and local taxes on Schedule A line 7 (all added back for AMT).
3. **Incentive stock options exercised in 2026:** grant, exercise date, shares, strike price and fair market value on exercise, and whether any shares were sold in the same calendar year.
4. **Prior-year Form 8801** or a prior AMT payment, which may give a credit.
5. **Tax-exempt interest from private activity bonds** (Form 1099-INT box 9).
6. **Business or rental depreciation, passive activities, or K-1s** with AMT items (box 17 code A of Schedule K-1 (Form 1065), box 15 of Schedule K-1 (Form 1120-S)).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Exemption, married filing jointly and surviving spouses | USD 140,200 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Exemption, unmarried individuals (other than surviving spouses) | USD 90,100 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Exemption, married filing separately | USD 70,100 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out threshold, joint returns and surviving spouses (exemption gone at USD 1,280,400) | USD 1,000,000 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out threshold, unmarried individuals (exemption gone at USD 680,200) | USD 500,000 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out threshold, married filing separately (exemption gone at USD 640,200) | USD 500,000 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out rate (from 2026; 25% before) | 50% | [Public Law 119-21, section 70107(c)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Lower AMT rate | 26% | [26 U.S.C. 55(b)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec55.htm) |
| Higher AMT rate | 28% | [26 U.S.C. 55(b)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec55.htm) |
| Excess above which 28% applies, all other taxpayers | USD 244,500 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess above which 28% applies, married filing separately | USD 122,250 | [Rev. Proc. 2025-32, section 4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Exemption cap for a child subject to the kiddie tax: earned income plus | USD 9,750 | [Rev. Proc. 2025-32, section 4.11](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

The 28% shortcut used on Form 6251 line 7 (base times 28% minus 2% of the breakpoint) is USD 4,890 for 2026 (2% of USD 244,500), or USD 2,445 separate; this is arithmetic on the figures above, not a separate published amount.

### Part I: alternative minimum taxable income (AMTI)

1. **Line 1.** Start from taxable income on Form 1040 line 15, as the 2025 Form 6251 lines 1a and 1b direct (they also back out the Schedule 1-A deductions created by the One Big Beautiful Bill Act).
2. **Line 2a.** Add back the standard deduction if the client did not itemize, or the state and local taxes on Schedule A line 7 if they did. Source: [26 U.S.C. 56(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec56.htm).
3. **Line 2b.** Subtract a state tax refund included in income.
4. **Line 2g.** Add interest on specified private activity bonds that is exempt from regular tax.
5. **Line 2i, incentive stock options.** For shares acquired by exercising an ISO and not sold in the same calendar year, add the fair market value at exercise minus the price paid (the "bargain element"). The regular tax ignores it; AMT does not. The shares then have a higher AMT basis, which matters on sale. If the shares are sold in the same year in a disqualifying disposition, the gain is ordinary income for regular tax and there is no AMT adjustment. Source: [26 U.S.C. 56(b)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec56.htm) and [26 U.S.C. 422](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partII-sec422.htm).
6. **Lines 2c to 3.** Other adjustments (depreciation, passive activities, net operating loss, K-1 items). Take them from the source workpapers; this skill does not compute them.
7. **Line 4, AMTI** = the total.

### Part II: exemption and tentative minimum tax

8. **Line 5, exemption.** Exemption for the filing status, minus 50% of AMTI above the phase-out threshold, not below zero.
9. **Line 6** = AMTI minus the exemption. If zero or less, there is no AMT.
10. **Line 7.** If there are no qualified dividends or net capital gain: 26% of line 6 up to USD 244,500 (USD 122,250 separate), plus 28% of the rest. If there are, use Part III: qualified dividends and net capital gain keep their regular 0%, 15% and 20% rates inside AMT (see `us-capital-gains` for the breakpoints), and only the rest is taxed at 26% and 28%.
11. **Line 8,** AMT foreign tax credit (see `us-foreign-tax-credit-1116`). **Line 9,** tentative minimum tax = line 7 minus line 8.
12. **Line 10.** Regular tax (Form 1040 line 16 plus Schedule 2 line 1z items as the form directs, minus the regular foreign tax credit). **Line 11, AMT** = line 9 minus line 10, if more than zero. It goes to Schedule 2 line 1.

### The minimum tax credit (Form 8801)

13. AMT caused by "deferral" items, mainly ISO exercises and depreciation, creates a credit carried forward with no time limit. It can be used in a later year when regular tax exceeds the tentative minimum tax. AMT from "exclusion" items (the standard deduction and state taxes added back, private activity bond interest) does not. Keep the AMT basis of ISO shares; selling them in a later year produces a negative adjustment that releases the credit.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| ISO shares exercised and sold in the same calendar year | No AMT adjustment; the spread is ordinary income for regular tax |
| ISO shares exercised in 2026, sold in 2027 | 2026 adjustment on line 2i; in 2027 the AMT gain is smaller (higher AMT basis) and part of the AMT may come back as a Form 8801 credit |
| AMTI between USD 1,000,000 and USD 1,280,400 (joint) | Exemption partly phased out at 50 cents per dollar: each extra dollar adds USD 1.50 to the AMT base |
| AMTI at or above USD 1,280,400 (joint) or USD 680,200 (single) | No exemption at all |
| Child subject to the kiddie tax | Exemption capped at earned income plus USD 9,750 |
| Married filing separately with AMTI above USD 640,200 | The form adds a further amount to line 4 (see the Form 6251 instructions); refer if it applies |
| Itemized deductions other than taxes (mortgage interest, charity) | Allowed for AMT as for regular tax; only taxes are added back |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Fair market value at ISO exercise | Stop: the employer's Form 3921 gives it; do not estimate |
| Whether ISO shares were sold in the same year | Treat as held (AMT adjustment applies) and confirm |
| Prior-year Form 8801 | Assume no credit and ask for the 2025 return |
| K-1 AMT items | Assume none; ask for the full K-1 package |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| ISO exercise late in the year with shares still held | Large AMT with no cash from the shares; a same-year sale may remove it |
| Joint AMTI near or above USD 1,000,000 | The 50% phase-out raises the effective AMT rate to 39% or 42% in the band |
| Share price fell after an ISO exercise | AMT is still owed on the value at exercise; selling in the same year is the main fix |
| Large private activity bond holdings | Tax-exempt for regular tax, taxable for AMT |

## Worked cases

**Case 1, a decision: how many ISOs can be exercised in 2026 without AMT?** A single employee has wages of USD 180,000, takes the standard deduction of USD 16,100 (from `us-federal-income-tax-return-1040`), and has taxable income of USD 163,900. Regular tax on that from the 2026 single brackets in the same sibling skill is USD 31,934 (USD 17,966 plus 24% of USD 58,200). She is considering exercising ISOs with a USD 100,000 spread and holding the shares.

AMTI if she exercises everything: USD 163,900 + USD 16,100 + USD 100,000 = USD 280,000. Exemption USD 90,100 (no phase-out). Base USD 189,900, all at 26%: tentative minimum tax USD 49,374. AMT is USD 49,374 minus USD 31,934 = USD 17,440. The spread she can take with no AMT is the amount that makes 26% of (USD 89,900 plus the spread) equal the regular tax: USD 31,934 divided by 26%, minus USD 89,900 = USD 32,923.08. Recommend exercising options with a spread of about USD 32,900 in 2026 and the rest in later years (or selling those shares in the same year), unless she accepts paying AMT now for a credit later.

```oa-check
name: ISO exercise and the AMT break-even spread, single (2026)
inputs:
  taxable_income: 163900
  standard_deduction: 16100
  iso_spread: 100000
  exemption: 90100
  regular_tax: 31934
steps:
  - amti: taxable_income + standard_deduction + iso_spread
  - base: max(amti - exemption, 0)
  - tmt: min(base, 244500) * 0.26 + max(base - 244500, 0) * 0.28
  - amt: max(tmt - regular_tax, 0)
  - breakeven_spread: regular_tax / 0.26 - (taxable_income + standard_deduction - exemption)
expected:
  amti: 280000
  tmt: 49374.00
  amt: 17440.00
  breakeven_spread: 32923.08
```

**Case 2, phase-out and the 28% band, joint.** A married couple filing jointly have AMTI of USD 1,100,000, all ordinary income. The exemption is USD 140,200 minus 50% of (USD 1,100,000 minus USD 1,000,000) = USD 90,200. The base is USD 1,009,800. Tentative minimum tax: 26% of USD 244,500 = USD 63,570, plus 28% of USD 765,300 = USD 214,284, total USD 277,854 (the line 7 shortcut gives the same: USD 1,009,800 times 28% minus USD 4,890). AMT is that figure minus their regular tax, if positive.

```oa-check
name: Joint AMTI 1,100,000 with exemption phase-out (2026)
inputs:
  amti: 1100000
  exemption_full: 140200
  phaseout_start: 1000000
steps:
  - exemption: max(exemption_full - 0.5 * max(amti - phaseout_start, 0), 0)
  - base: amti - exemption
  - tmt: min(base, 244500) * 0.26 + max(base - 244500, 0) * 0.28
  - shortcut: base * 0.28 - 4890
expected:
  exemption: 90200.00
  base: 1009800.00
  tmt: 277854.00
  shortcut: 277854.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-AMT-TRUST | Estate or trust AMT (Form 1041 Schedule I) | Refer |
| R-AMT-NOL | Alternative tax net operating loss deduction | Refer: separate computation |
| R-AMT-DEPR | Large AMT depreciation or passive activity differences with no workpapers | Refer: the figures must come from the fixed asset system |
| R-AMT-FTC | AMT foreign tax credit with more than one category | Use `us-foreign-tax-credit-1116` or refer |
| R-AMT-MFS | Married filing separately with AMTI above USD 640,200 | Refer: extra line 4 amount |

## Filing and payment

Form 6251 is attached to the 2026 Form 1040 due **15 April 2027** whenever AMT is owed or the form's filing triggers apply (see the Form 6251 instructions, "Who Must File"). AMT is part of the tax for estimated tax: an ISO exercise early in the year may need a larger payment (see `us-quarterly-estimated-tax`). Form 8801 is filed in the later year to claim the credit.

## Completion checklist

- 2026 exemption, phase-out at 50%, and the USD 244,500 breakpoint used (not the 2025 figures or the 25% rate).
- Standard deduction or Schedule A taxes added back; state refund subtracted.
- Every 2026 ISO exercise checked against Form 3921 and against same-year sales.
- Capital gains and qualified dividends run through Part III, not taxed at 26% or 28%.
- AMT basis of ISO shares recorded; Form 8801 credit carryforward recorded.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.10 (exemptions USD 140,200 / 90,100 / 70,100; 28% breakpoints USD 244,500 / 122,250; phase-out thresholds USD 1,000,000 / 500,000 / 500,000 and complete phase-outs) and section 4.11 (child: earned income plus USD 9,750). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21 (One Big Beautiful Bill Act). Read for section 70107: increased exemptions made permanent, the USD 1,000,000 amount re-based to 2025, and "50 percent" substituted for "25 percent" in the phase-out, for years after 2025. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 55 (govinfo, 2024 edition). Read for (b)(1) the 26% and 28% rates and the structure of the exemption phase-out. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec55.htm | 2026-11-13 |
| 26 U.S.C. 56 (govinfo, 2024 edition). Read for (b)(1) taxes and standard deduction not allowed, (b)(3) incentive stock options. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec56.htm | 2026-11-13 |
| 26 U.S.C. 422 (govinfo, 2024 edition). Read for the ISO holding periods and disqualifying dispositions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partII-sec422.htm | 2026-11-13 |
| Form 6251 (2025) and its instructions. Read for the line order (1a, 1b, 2a, 2g, 2i, 4 to 11) and Part III. | https://www.irs.gov/pub/irs-pdf/f6251.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form 6251 and its instructions were not yet published when read; line numbers are those of the 2025 form, and the 2026 figures come from Rev. Proc. 2025-32 and the statute.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-alternative-minimum-tax-6251` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-alternative-minimum-tax-6251. If neither is available, confirm every figure against the official source pages cited above before relying on it.
