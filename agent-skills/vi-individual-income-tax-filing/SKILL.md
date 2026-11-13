---
name: vi-individual-income-tax-filing
description: "Decide where and how an individual with US Virgin Islands income files for 2026 under the mirror code and section 932. Covers full-year bona fide residents (one return to the VI Bureau of Internal Revenue reporting worldwide income, with Form 1040INFO for non-VI income), US citizens and resident aliens who are not bona fide residents (original return to the IRS, identical signed copy to the BIR, Form 8689 allocation by VI AGI over worldwide AGI, credit only for tax actually paid), joint returns decided by the higher-AGI spouse, extensions, Form 1040-SS for self-employment tax, and the nonresident alien route. Trigger on \"USVI tax return\", \"Virgin Islands income tax\", \"Form 8689\", \"Form 1040INFO\", \"BIR St. Thomas\", \"mirror code\", \"section 932\", \"working in St. Croix\". Not the British Virgin Islands."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vi-individual-income-tax-filing"
  jurisdiction: "VI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US Virgin Islands: individual income tax filing, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 932, IRS Pub. 570 (2025), Form 8689 (2026) with its instructions, Virgin Islands Bureau of Internal Revenue (BIR) Form 1040INFO (2025) and the BIR forms directory, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** The USVI has its own income tax, built on the same law and rates as the US (the "mirror code"). Who files where depends on bona fide residence for the whole year (see `vi-bona-fide-residence`). A **full-year bona fide resident** files one return with the BIR reporting worldwide income, identifies the source of each item, attaches BIR Form 1040INFO for non-USVI income, pays the USVI in full, and generally files nothing with the IRS. A **US citizen or resident alien who is not a bona fide resident** but has USVI-source income files the original Form 1040 with the IRS and an identical signed copy with the BIR, uses **Form 8689** to pay the USVI its share (USVI AGI over worldwide AGI, ratio not above 1.000) and credits only what was actually paid. On a **joint return**, the spouse with the **higher AGI** decides the route.

## Scope and who this is for

In scope: individuals (US citizens, resident aliens, and the outline of the nonresident alien route) with income from the USVI or who live there, for tax year 2026.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether the person is a bona fide resident, and Form 8898 | `vi-bona-fide-residence` |
| USVI gross receipts tax on business receipts | `vi-gross-receipts-tax` |
| The US return itself: brackets, deductions, credits | `us-federal-income-tax-return-1040` |
| Self-employment tax computation | `us-schedule-c-and-se-computation` |
| Nonresident aliens of the United States (Form 1040-NR) | `us-form-1040-nr-nonresident-return` |
| Economic Development Commission (EDC) incentives, estates and trusts, corporations | refer (see the refusal table) |
| The British Virgin Islands (VG) | not this skill |

## Ask the client first

1. **Bona fide residence for the full 2026 year**, settled with `vi-bona-fide-residence`, including any year-of-move exception.
2. **Citizenship or immigration status**: US citizen, resident alien, or nonresident alien of the United States.
3. **Income by source**: wages (where the work was done), business income, interest (payer's location), dividends (where the paying company is organised), rents and gains on real property (where it is), other items.
4. **Spouse**: filing jointly or separately, and each spouse's AGI and residence.
5. **Payments already made**: USVI withholding (Form W-2VI box 2), estimated tax paid to the BIR or the IRS, and any extension payment.
6. **Self-employment income** in the USVI, and any EDC or other incentive certificate.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule, 2026 | Source |
| --- | --- | --- |
| USVI income tax rates and law | Same as the US (mirror code); use the US rates for the year | [IRS Pub. 570 (2025), chapter 3, The U.S. Virgin Islands](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Form 8689 ratio: USVI AGI divided by worldwide AGI, rounded to at least | 3 decimal places | [Form 8689 (2026), line 35](https://www.irs.gov/pub/irs-pdf/f8689.pdf) |
| Form 8689 ratio cap | 1.000 | [Form 8689 (2026), line 35](https://www.irs.gov/pub/irs-pdf/f8689.pdf) |
| De minimis exception: services performed temporarily in the USVI for no more than | 90 days | [Form 8689 (2026) instructions, De minimis exception](https://www.irs.gov/pub/irs-pdf/f8689.pdf) |
| De minimis exception: earnings from those services no more than | USD 3,000 | [Form 8689 (2026) instructions, De minimis exception](https://www.irs.gov/pub/irs-pdf/f8689.pdf) |
| Penalty for each failure to file a required Form 8898 | USD 1,000 | [Form 8689 (2026) instructions](https://www.irs.gov/pub/irs-pdf/f8689.pdf) |
| Due date (same as Form 1040) | 15 April 2027 | [IRS Pub. 570 (2025), chapter 3](https://www.irs.gov/pub/irs-pdf/p570.pdf) |

The US brackets and the standard deduction for 2026 are in `us-federal-income-tax-return-1040`; they are not restated here.

### Step 1: choose the route

| Situation | Route | Source |
| --- | --- | --- |
| Full-year bona fide resident of the USVI (citizen, resident alien or nonresident alien) | One return to the BIR reporting worldwide income; Form 1040INFO for non-USVI income; generally no IRS income tax return | [Pub. 570, Bona Fide Resident of the U.S. Virgin Islands](https://www.irs.gov/pub/irs-pdf/p570.pdf); [26 U.S.C. 932(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec932.htm) |
| US citizen or resident alien, not a full-year bona fide resident, with USVI-source or USVI effectively connected income | Original Form 1040 to the IRS, identical signed copy to the BIR, Form 8689 attached to both | [26 U.S.C. 932(a) and (b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec932.htm); [Form 8689 (2026) instructions](https://www.irs.gov/pub/irs-pdf/f8689.pdf) |
| Nonresident alien of the US, not a bona fide USVI resident | A USVI return for USVI-source income only, and Form 1040-NR to the IRS for US-source income | [Pub. 570, Nonresident Alien (Other Than a Bona Fide Resident)](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| US citizen or resident with no USVI income | US return only | [Pub. 570](https://www.irs.gov/pub/irs-pdf/p570.pdf) |

Do not pick the route from a mailing address. A person treated as a full-year resident under the year-of-move rules does not use Form 8689.

### Step 2, full-year bona fide resident

1. Report **worldwide income** on the USVI return, identify the source of each item, and attach BIR **Form 1040INFO** (Non-Virgin Islands Source Income of Virgin Islands Residents). Source: [BIR Form 1040INFO](https://bir.vi.gov/content/form/ee6facb3-7d15-4066-86db-c965152411d2/index.pdf).
2. **Payments** include all income tax withheld by, or paid to, either the USVI or the US, overpayment credits from either, and estimated tax paid to either. Pay the balance with the return.
3. The US exclusion under section 932(c)(4) holds only if the person reports income from all sources, identifies its source, and **pays the USVI tax in full**. A residence claim alone is not enough. Filing with the USVI generally also starts the statute of limitations for US income tax.
4. Worldwide reporting does not make every item USVI-source for an incentive or allocation.
5. Self-employment income: Form 1040-SS goes to the IRS for self-employment tax, even with no US income tax filing.

### Step 3, US citizen or resident alien who is not a bona fide resident (Form 8689)

6. Complete the US Form 1040 as usual.
7. **Parts I and II of Form 8689:** USVI-source income (lines 1 to 16) less the deductions that belong to it (lines 17 to 29), giving **USVI AGI on line 30**. Wages are sourced where the work was done; the de minimis exception removes up to USD 3,000 earned in 90 days or less of temporary work for a non-USVI employer. Self-employment, IRA and similar deductions are apportioned by the USVI share of the related income.
8. **Part III:** line 31 total US tax, less the line 32 items (for example earned income credit, additional child tax credit, the refundable American opportunity credit, self-employment tax and household employment tax), gives line 33. **Line 35** = line 30 divided by worldwide AGI (line 34), at least 3 decimals, not above 1.000. **Line 36** = line 33 times line 35: the tax allocated to the USVI. Source: [26 U.S.C. 932(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec932.htm) and [Form 8689 (2026)](https://www.irs.gov/pub/irs-pdf/f8689.pdf).
9. **Part IV:** line 37 USVI withholding (Form W-2VI box 2; never also on the US withholding lines), line 38 estimated payments to the USVI, line 39 extension payment; line 40 total. Line 41 is the smaller of line 36 or 40. Line 45 is the amount still owed to the USVI; line 46 is the part of it paid when filing.
10. **Credit on the US return:** lines 41 plus 46, on Schedule 3 "Other refundable credits", only for USVI tax actually paid. Overpayments to one government are not applied to the other. Source: [Form 8689 (2026) instructions, Credit for U.S. tax paid to the USVI](https://www.irs.gov/pub/irs-pdf/f8689.pdf).
11. **Where to file:** the original return to the IRS (Austin, or the Charlotte payment address if a check is enclosed, per Pub. 570), and a signed copy with all attachments to the BIR, 6115 Estate Smith Bay, Suite 225, St. Thomas, VI 00802, which processes it as an original.

### Step 4, joint returns

12. File where the spouse with the **greater AGI** would file if filing separately, ignoring community property laws. If that spouse is a full-year bona fide resident, file the joint return with the USVI; if not, file with the US, and use Form 8689 for any USVI income. Source: [26 U.S.C. 932(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec932.htm) and [Pub. 570, Joint return](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Extensions

13. A full-year bona fide resident files a **paper Form 4868 with the BIR**. A non-resident files extension requests with both the IRS and the BIR and pays each; the BIR honours a timely request filed with the IRS. Source: [Pub. 570, Extension of time to file](https://www.irs.gov/pub/irs-pdf/p570.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Joint filers with exactly equal AGI | Not settled by the rule; refer |
| Joint filers, only the lower-AGI spouse is a bona fide resident | File with the US, both spouses' income on the US return; no USVI-resident treatment |
| Non-resident worked 20 days in St. Thomas for a US employer and earned USD 2,500 | De minimis: not USVI-source; no Form 8689 for that wage |
| Ratio on line 35 works out above 1.000 | Enter 1.000 |
| Zero or negative worldwide AGI | The ratio cannot be computed; refer |
| Bona fide resident with no US income tax filing but USVI business profit | Form 1040-SS to the IRS for self-employment tax |
| Military member stationed in the USVI who is not a bona fide resident | Military pay is not USVI-source (SCRA); see Pub. 570 |
| Civilian military spouse in the USVI under MSRRA | Wages and self-employment income not USVI-source if the conditions are met |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Bona fide residence for the full year | Do not choose a route; settle it first with `vi-bona-fide-residence` |
| Days worked in the USVI | Ask; wages are sourced by where the work was done |
| Whether the USVI balance will be paid when filing | Credit only line 41 plus the amount actually paid |
| Spouse's AGI | Ask; it can decide the whole route |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Claimed full-year residence with a home, family or business still on the mainland | Residence may fail; the US exclusion then fails and the IRS can assess |
| USVI tax shown but not paid | No US credit, and section 932(c)(4) fails for a resident |
| W-2VI withholding entered on the US withholding line | Double counting; it belongs on Form 8689 line 37 |
| Residence began or ended in 2026 with worldwide gross income over USD 75,000 | Form 8898 is likely due (`vi-bona-fide-residence`) |

## Worked cases

**Case 1, a decision: which government gets the joint return?** Spouse A is a full-year bona fide USVI resident with AGI of USD 60,000. Spouse B lives and works on the mainland with AGI of USD 45,000. They want to file jointly. The higher-AGI spouse is A, a bona fide resident, so the joint return of USD 105,000 goes to the BIR as a USVI resident return reporting worldwide income, with Form 1040INFO for B's US-source wages. If B's AGI had been USD 61,000 instead, B would be the higher-AGI spouse and the joint return would go to the IRS with Form 8689 for A's USVI income. Recommend confirming both AGIs on the final figures before choosing; a small change flips the route.

```oa-check
name: Joint return route by the higher-AGI spouse (2026)
inputs:
  agi_resident_spouse: 60000
  agi_mainland_spouse: 45000
steps:
  - joint_agi: agi_resident_spouse + agi_mainland_spouse
  - resident_lead: agi_resident_spouse - agi_mainland_spouse
  - higher_agi: max(agi_resident_spouse, agi_mainland_spouse)
expected:
  joint_agi: 105000
  resident_lead: 15000
  higher_agi: 60000
```

**Case 2, Form 8689 allocation and the credit.** A US citizen who is not a bona fide resident has worldwide AGI of USD 100,000 (line 34), USVI AGI of USD 40,000 (line 30), and line 33 tax of USD 20,000. Line 35 is 0.400. Line 36, tax allocated to the USVI, is USD 8,000. USVI withholding on Form W-2VI was USD 3,000 (line 37), so line 41 is USD 3,000 and line 45 is USD 5,000 owed to the USVI. If it is paid with the return (line 46 = USD 5,000), the US credit on Schedule 3 is USD 3,000 plus USD 5,000 = USD 8,000. If it is not paid, the credit is USD 3,000 only.

```oa-check
name: Form 8689 allocation and credit (2026)
inputs:
  usvi_agi: 40000
  worldwide_agi: 100000
  line_33_tax: 20000
  usvi_payments: 3000
  paid_with_return: 5000
steps:
  - ratio: min(round(usvi_agi / worldwide_agi, 3), 1)
  - allocated: line_33_tax * ratio
  - line_41: min(allocated, usvi_payments)
  - line_45: max(allocated - usvi_payments, 0)
  - us_credit: line_41 + min(paid_with_return, line_45)
expected:
  ratio: 0.400
  allocated: 8000.00
  line_45: 5000.00
  us_credit: 8000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-VI-EDC | EDC beneficiary, or any USVI tax incentive or reduction | Refer: incentive rules and source limits apply |
| R-VI-NRA | Nonresident alien of the US with USVI income | Refer for the two-return route |
| R-VI-ENTITY | Corporations, partnerships, estates or trusts | Refer |
| R-VI-AGI | Zero or negative worldwide AGI, or equal spouse AGIs | Refer |
| R-VI-SOURCE | Gains on personal property, inventory sales or other source questions beyond the general rules | Refer: sections 861 to 865 and 937 and Regulations section 1.937-2 |

## Filing and payment

Returns for 2026 are due **15 April 2027**. Residents file and pay with the BIR. Non-residents with USVI income file with the IRS and send a signed copy, including Form 8689, to the BIR, 6115 Estate Smith Bay, Suite 225, St. Thomas, VI 00802, paying the USVI share when filing. Amended returns go to both. The BIR forms directory lists the IRS Form 1040 and Form 8689 for use with the BIR, and its own Form 1040INFO.

## Completion checklist

- Full-year residence settled before choosing a route.
- Joint return route set by the higher-AGI spouse.
- Residents: worldwide income, sources identified, Form 1040INFO attached, USVI tax paid in full.
- Non-residents: Form 8689 on both returns, ratio at 3 decimals and not above 1.000, W-2VI withholding only on line 37, credit only for tax paid.
- Form 1040-SS considered for USVI self-employment income; Form 8898 considered for a move.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 932 (govinfo, 2024 edition). Read for (a) and (b) non-residents and the AGI allocation, (c) bona fide residents and (c)(4) the conditions, (d) joint returns. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec932.htm | 2026-11-13 |
| IRS Pub. 570 (2025), chapter 3, The U.S. Virgin Islands. Read for the mirror code, Which Return To File, Form 1040INFO, addresses, joint return rule, Form 1040-SS, extensions. | https://www.irs.gov/pub/irs-pdf/p570.pdf | 2026-11-13 |
| Form 8689 (2026) with instructions. Read for lines 30 to 46, the 1.000 cap and 3-decimal rounding, de minimis exception (90 days, USD 3,000), line 37 W-2VI, credit of lines 41 plus 46 on Schedule 3, the BIR filing address, the USD 1,000 Form 8898 penalty. | https://www.irs.gov/pub/irs-pdf/f8689.pdf | 2026-11-13 |
| BIR Form 1040INFO (2025), Non-Virgin Islands Source Income of Virgin Islands Residents. Read for its purpose under section 932. | https://bir.vi.gov/content/form/ee6facb3-7d15-4066-86db-c965152411d2/index.pdf | 2026-11-13 |
| BIR forms directory. Read for the forms the BIR lists for individuals (Form 1040, Form 8689, Form 4868, Form 1040INFO). | https://bir.vi.gov/form | 2026-11-13 |

Not yet confirmed: Pub. 570 for 2026 was not yet published (the 2025 edition was read, and its Form 8689 references, lines 40 and 45 and Form 1040 line 33, conflict with the 2026 Form 8689, which says lines 41 and 46 on Schedule 3; this skill follows the 2026 form). The BIR Form 1040INFO for 2026 was not yet posted.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vi-individual-income-tax-filing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vi-individual-income-tax-filing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
