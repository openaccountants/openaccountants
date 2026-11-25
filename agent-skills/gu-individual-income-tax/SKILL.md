---
name: gu-individual-income-tax
description: "Decide where and how an individual with Guam income files for 2026 under the Guam Territorial income tax, which mirrors the US Internal Revenue Code (48 U.S.C. 1421i). Covers bona fide residence (presence, tax home and closer connection tests, Form 8898 above USD 75,000), full-year residents filing one Guam Form 1040 with the Department of Revenue and Taxation reporting worldwide income, US citizens and resident aliens who are not residents filing only with the IRS and attaching Form 5074 when AGI is USD 50,000 or more and Guam-source gross income USD 5,000 or more, the de minimis rule (90 days, USD 3,000), joint returns decided by the higher-AGI spouse, citizens of Guam, nonresident aliens, estimated tax, Form 1040-SS for self-employment tax, military and MSRRA spouses. Trigger on \"Guam tax return\", \"Guam income tax\", \"Form 5074\", \"W-2GU\", \"Guam DRT 1040\", \"mirror code Guam\", \"bona fide resident of Guam\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gu-individual-income-tax"
  jurisdiction: "US-GU"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Guam: individual income tax, tax year 2026

> **Source-cited draft.** Built from 48 U.S.C. 1421i, IRS Pub. 570 (2025), Form 5074 (2026) with its instructions, the Guam Department of Revenue and Taxation (DRT) 2025 Guam Form 1040 and the DRT tax calendar, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Guam has its own income tax, the **Guam Territorial income tax**: the US income tax law applied with "Guam" read for "United States" (the mirror code, 48 U.S.C. 1421i). Rates, brackets and deductions are the US ones. Everyone with Guam income files **one** return, to Guam or to the US, never both. A **bona fide resident of Guam** for 2026 files with the **DRT**, reports worldwide income, and counts tax withheld or paid to either government. A **US citizen or resident alien who is not a bona fide resident** files only with the **IRS**, reports worldwide income, and attaches **Form 5074** if AGI is **USD 50,000 or more** and Guam-source gross income is **USD 5,000 or more**. On a joint return the **spouse with the higher AGI** decides. Returns are due **15 April 2027**.

## Scope and who this is for

In scope: individuals (US citizens, resident aliens, citizens of Guam, and the outline of the nonresident alien route) who live in Guam or have Guam-source income, for tax year 2026: which government, which form, residence, sourcing of common items, joint returns, estimated tax, self-employment tax and where to send the return.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The return itself: brackets, standard deduction, credits for 2026 | `us-federal-income-tax-return-1040` |
| Self-employment tax computation | `us-schedule-c-and-se-computation` |
| Estimated tax amounts and safe harbours | `us-quarterly-estimated-tax` |
| Nonresident aliens of the United States (Form 1040-NR) | `us-form-1040-nr-nonresident-return` |
| Guam business privilege tax on business income | `gu-business-privilege-tax` |
| Employer withholding and Form W-2GU | `gu-payroll` |
| Corporations, partnerships, estates, trusts, Qualifying Certificate rebates | refer (see the refusal table) |
| The Northern Mariana Islands (CNMI), which also uses Form 5074 | not this skill |

## Ask the client first

1. **Residence for 2026**: days in Guam (and in the US) in 2026 and in 2024 and 2025, where the tax home (main place of work) is, and where home, family, car, bank, voter registration and driver's licence are. Did residence start or end in 2026?
2. **Citizenship or immigration status**: US citizen, resident alien, citizen of Guam only, or nonresident alien.
3. **Income by source**: wages (where the work was done), business income, interest (payer's location), dividends (where the company is organised), rents and gains on real property (where it is), pensions.
4. **Spouse**: filing jointly or separately, and each spouse's AGI and residence.
5. **Payments already made**: Guam tax withheld (Form W-2GU box 2), US tax withheld, estimated tax paid to either government.
6. **Self-employment income** and any military service or MSRRA claim.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule, 2026 | Source |
| --- | --- | --- |
| Guam income tax law and rates | US income tax law applied as the Guam Territorial income tax | [48 U.S.C. 1421i(a), (b), (d), (e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title48/html/USCODE-2024-title48-chap8A-subchapI-sec1421i.htm) |
| Self-employment tax (IRC chapter 2) in the Guam mirror | Excluded: paid to the US on Form 1040-SS | [48 U.S.C. 1421i(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title48/html/USCODE-2024-title48-chap8A-subchapI-sec1421i.htm); [IRS Pub. 570 (2025), Guam, Self-employment tax](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Form 5074 required when AGI is | USD 50,000 or more | [Form 5074 (2026) instructions, Who must file](https://www.irs.gov/pub/irs-pdf/f5074.pdf) |
| and Guam-source gross income is | USD 5,000 or more | [Form 5074 (2026) instructions, Who must file](https://www.irs.gov/pub/irs-pdf/f5074.pdf) |
| De minimis rule: temporary services in Guam not Guam-source if no more than | 90 days | [Form 5074 (2026) instructions, De minimis exception](https://www.irs.gov/pub/irs-pdf/f5074.pdf) |
| and earnings no more than | USD 3,000 | [Form 5074 (2026) instructions, De minimis exception](https://www.irs.gov/pub/irs-pdf/f5074.pdf) |
| Presence test: days in Guam in the year, at least | 183 | [IRS Pub. 570 (2025), chapter 1, Presence Test](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| or days in the 3 years ending with 2026, at least (and at least 60 in each year) | 549 | [IRS Pub. 570 (2025), chapter 1, Presence Test](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Form 8898 when residence starts or ends and worldwide gross income is more than | USD 75,000 | [IRS Pub. 570 (2025), chapter 1, Form 8898](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Penalty for each failure to file a required Form 8898 | USD 1,000 | [Form 5074 (2026) instructions, Penalty for Failure To Furnish Information](https://www.irs.gov/pub/irs-pdf/f5074.pdf) |
| Return due | 15 April 2027 | [DRT tax calendar](https://www.guamtax.com/info/calendar.html) |

The 2026 brackets, standard deduction and credits are in `us-federal-income-tax-return-1040`; they are not restated here. Guam uses them because its law is the same code.

### Step 1: settle bona fide residence

1. A US citizen or resident alien is a bona fide resident of Guam for 2026 only if all three tests are met for the year: the **presence test** (183 days in Guam, or 549 days over 2024 to 2026 with at least 60 each year, or the other Pub. 570 routes), the **tax home test** (main place of work in Guam) and the **closer connection test** (closer to Guam than to the US or a foreign country). Source: [Pub. 570, chapter 1](https://www.irs.gov/pub/irs-pdf/p570.pdf).
2. Year of a move: Pub. 570 has special rules for the year residence starts or ends; if worldwide gross income is more than USD 75,000, file Form 8898.
3. Military: active duty presence in Guam under orders does not make a person a bona fide resident; a resident who leaves under orders keeps residence. Source: [Pub. 570, Guam, U.S. Armed Forces](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 2: choose the route

| Situation | Route | Source |
| --- | --- | --- |
| Bona fide resident of Guam for 2026 (citizen, resident alien or nonresident alien) | One Guam Form 1040 to the DRT, worldwide income, all tax withheld or paid to either government counted; generally nothing to the IRS | [Pub. 570, Bona Fide Resident of Guam](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| US citizen or resident alien, not a bona fide resident, with Guam income | Form 1040 to the IRS only, worldwide income; Form 5074 if the two thresholds are met; nothing to Guam | [Pub. 570](https://www.irs.gov/pub/irs-pdf/p570.pdf); [Form 5074 (2026)](https://www.irs.gov/pub/irs-pdf/f5074.pdf) |
| Citizen of Guam (born or naturalised in Guam) but not otherwise a US citizen or resident | Guam return, worldwide income, withholding by both counted | [Pub. 570, Citizen of Guam](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Nonresident alien of the US, not a bona fide resident of Guam | Guam return for Guam-source income only, and Form 1040-NR to the IRS for US-source income | [Pub. 570, Nonresident Alien](https://www.irs.gov/pub/irs-pdf/p570.pdf) |

### Step 3, the resident's Guam return

4. Use the **Guam Form 1040** published by the DRT (same lines as the US form; line 1a takes Form W-2 and W-2GU wages). Report worldwide income. Payments include Guam and US withholding, overpayment credits and estimated tax paid to either.
5. If the return is properly filed with, and the tax fully paid to, Guam, the person generally has no US income tax return or payment (Pub. 570).
6. **Self-employed**: file **Form 1040-SS** with the IRS for self-employment tax even though income tax goes to Guam (`us-schedule-c-and-se-computation` for the figure). Additional Medicare Tax may also be due to the IRS.

### Step 4, the non-resident's US return and Form 5074

7. Report worldwide income on Form 1040, counting tax withheld and paid to either government.
8. **Form 5074** is required if AGI is USD 50,000 or more **and** at least USD 5,000 of gross income is from Guam. Part I lists Guam-source income, Part II the adjustments that belong to it (self-employment deductions and IRA deductions are apportioned by the Guam share of the related income), line 30 Guam AGI, Part III Guam payments (estimated tax, withholding on lines 31 to 34). The US and Guam use the form to divide the tax between them; the taxpayer does not file a separate Guam return.
9. **Sourcing**: wages where the work was done, but the **de minimis rule** removes pay for temporary work in Guam of 90 days or less and USD 3,000 or less for an employer not doing business in Guam; interest where the payer is; dividends where the company is organised; gains on real property where it is; personal property gains generally the seller's residence. Source: [Form 5074 (2026) instructions](https://www.irs.gov/pub/irs-pdf/f5074.pdf).
10. **MSRRA spouse**: a civilian spouse of a servicemember who keeps a state residence is taxed by the US on worldwide income; wages and self-employment income from Guam are not Guam income. Other Guam-source income may need Form 5074.

### Step 5, joint returns

11. File where the spouse with the **greater AGI** would file if filing separately, ignoring community property laws. If that spouse is a bona fide resident of Guam, file the joint return with Guam; if not, with the US, reporting both spouses' income. Form 5074 is filed only when the higher-AGI spouse is not a bona fide resident. Source: [Pub. 570, Joint return](https://www.irs.gov/pub/irs-pdf/p570.pdf) and [Form 5074 (2026) instructions](https://www.irs.gov/pub/irs-pdf/f5074.pdf).

### Step 6, estimated tax

12. Pay estimated tax to the government that would get the return if the year ended on the first instalment due date, and keep paying there; payments to either are treated as paid to the one with which the return is filed. A joint payment follows the spouse with the greater estimated AGI. Source: [Pub. 570, Guam, Estimated tax payments](https://www.irs.gov/pub/irs-pdf/p570.pdf). Amounts: `us-quarterly-estimated-tax`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Non-resident, AGI USD 49,000, Guam wages USD 20,000 | Form 1040 to the IRS; Form 5074 not required (AGI under USD 50,000) |
| Non-resident, AGI USD 120,000, Guam interest USD 4,000 only | No Form 5074 (Guam income under USD 5,000) |
| Engineer from Hawaii works 30 days in Guam for a Hawaii firm, paid USD 2,800 | De minimis: not Guam-source |
| Same, paid USD 3,500 | Guam-source wages |
| Joint filers with exactly equal AGI | Not settled by the rule; refer |
| Guam resident with a W-2 from a mainland employer showing US withholding | Count it as a payment on the Guam return |
| Guam resident sells a home in Guam | Gain is Guam-source; reported on the Guam return |
| Servicemember stationed in Guam, resident of a state | Military pay not Guam-source; US return |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Days in Guam, tax home, closer connection | Do not pick a route; settle residence first |
| Spouse's AGI | Ask; it can decide where the joint return goes |
| Where the work was done | Ask; wages are sourced by place of work |
| Whether residence started or ended in 2026 | Ask; Form 8898 may be due |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Return filed with both Guam and the IRS | Only one is the right place; the other has to be withdrawn or refunds sorted |
| Resident claiming Guam residence while the main job is on the mainland | Fails the tax home test |
| Self-employed Guam resident with no Form 1040-SS | Self-employment tax is owed to the US |
| Non-resident with Guam AGI and no Form 5074 | Guam's share is not allocated |
| W-2GU box 2 treated as US withholding on a resident return | It is Guam withholding; both count as payments, but must not be double entered |

## Worked cases

**Case 1, a decision: which government gets the joint return?** (adapted from the Pub. 570 example). Spouse A, a US citizen living in the US, earned USD 45,000. Spouse B, a bona fide resident of Guam, earned USD 15,000. A has the greater AGI and is not a Guam resident, so the joint return of USD 60,000 goes to the **IRS**, and Form 5074 is needed because AGI is at least USD 50,000 and Guam-source income (B's USD 15,000 wages) is at least USD 5,000. If B had earned USD 50,000 instead, B would be the higher-AGI spouse and the joint return would go to **Guam**, with no Form 5074. Recommend confirming both AGIs on the final figures before choosing; a small change can flip the route.

```oa-check
name: Guam joint return route and Form 5074 test (2026)
inputs:
  agi_us_spouse: 45000
  agi_guam_spouse: 15000
steps:
  - joint_agi: agi_us_spouse + agi_guam_spouse
  - us_spouse_lead: agi_us_spouse - agi_guam_spouse
  - agi_test: min(floor(joint_agi / 50000), 1)
  - guam_income_test: min(floor(agi_guam_spouse / 5000), 1)
  - form_5074_needed: min(agi_test, guam_income_test)
expected:
  joint_agi: 60000
  us_spouse_lead: 30000
  form_5074_needed: 1
```

**Case 2, de minimis and the Form 5074 threshold.** A single US citizen living in California with AGI of USD 95,000 spent 40 days in Guam on a job for a California firm and earned USD 2,900 there; she also has USD 4,500 of interest from a bank in Guam. The USD 2,900 is not Guam-source (90 days or less, USD 3,000 or less). Guam-source gross income is USD 4,500, under USD 5,000, so no Form 5074. If the job had paid USD 3,100, the de minimis rule would fail, Guam income would be USD 7,600, and Form 5074 would be required.

```oa-check
name: De minimis wages and the USD 5,000 Guam-income test (2026)
inputs:
  guam_wages: 2900
  days_in_guam: 40
  guam_interest: 4500
  agi: 95000
steps:
  - wage_is_guam_source: 1 - min(min(floor(90 / days_in_guam), 1), min(floor(3000 / guam_wages), 1))
  - guam_gross: guam_interest + guam_wages * wage_is_guam_source
  - form_5074_needed: min(min(floor(agi / 50000), 1), min(floor(guam_gross / 5000), 1))
  - guam_gross_if_3100: guam_interest + 3100
expected:
  wage_is_guam_source: 0
  guam_gross: 4500
  form_5074_needed: 0
  guam_gross_if_3100: 7600
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GU-QC | Qualifying Certificate holder or any Guam income tax rebate | Refer: rebate rules |
| R-GU-NRA | Nonresident alien of the US with Guam income | Refer for the two-return route |
| R-GU-ENTITY | Corporations, partnerships, estates or trusts | Refer |
| R-GU-AGI | Equal spouse AGIs, or a residence claim that fails one test | Refer |
| R-GU-SOURCE | Personal property, inventory or other source questions beyond the general rules | Refer: sections 861 to 865, 937 and Regulations section 1.937-2 |
| R-GU-DOUBLE | Double taxation between the US and Guam | Refer: mutual agreement procedure (Pub. 570) |

## Filing and payment

Returns for 2026 are due **15 April 2027** (DRT calendar; a weekend or holiday moves it to the next working day). Residents send the Guam Form 1040 and payment to the Department of Revenue and Taxation, Taxpayer Services Division, P.O. Box 23607, GMF, Guam 96921; the DRT calendar also shows a **15 June** date for individuals off-island. Non-residents send the US return with Form 5074 to the IRS, Austin, TX 73301-0215 (or P.O. Box 1303, Charlotte, NC 28201-1303 if a check is enclosed). Form 1040-SS goes to the IRS.

## Completion checklist

- Residence settled on all three tests before choosing a route; Form 8898 considered for a move.
- Joint return route set by the higher-AGI spouse.
- Residents: Guam Form 1040, worldwide income, withholding and payments to both governments counted.
- Non-residents: US return only; Form 5074 tested on both thresholds; de minimis applied.
- Form 1040-SS for a self-employed Guam resident.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 48 U.S.C. 1421i (govinfo, 2024 edition). Read for (a) US income tax laws in force in Guam, (b) the Guam Territorial income tax, (d)(1) the code provisions included (chapter 2 self-employment tax excluded; chapters 24 and 25 withholding included), (e) "Guam" read for "United States". | https://www.govinfo.gov/content/pkg/USCODE-2024-title48/html/USCODE-2024-title48-chap8A-subchapI-sec1421i.htm | 2026-11-14 |
| IRS Pub. 570 (2025). Read for chapter 1 (presence test 183 and 549 days, Form 8898 above USD 75,000) and chapter 3, Guam (one return, Which Return To File, Form 5074 thresholds, citizen of Guam, nonresident alien, joint return rule and example, armed forces, MSRRA, Form 1040-SS, estimated tax, addresses). | https://www.irs.gov/pub/irs-pdf/p570.pdf | 2026-11-14 |
| Form 5074 (2026) with instructions. Read for who must file (AGI USD 50,000, Guam income USD 5,000), the de minimis exception (90 days, USD 3,000), sourcing rules, lines 1 to 35, the USD 1,000 Form 8898 penalty. | https://www.irs.gov/pub/irs-pdf/f5074.pdf | 2026-11-14 |
| DRT 2025 Guam Form 1040. Read for the Guam form and line 1a (W-2 and W-2GU). | https://www.guamtax.com/forms/2025GUAM1040TaxForm.pdf | 2026-11-14 |
| DRT tax calendar. Read for 15 April individual returns, 15 June off-island, quarterly estimated tax dates and the weekend rule. | https://www.guamtax.com/info/calendar.html | 2026-11-14 |

Not yet confirmed: Pub. 570 for 2026 is not yet published (2025 edition read); the DRT's 2026 Guam Form 1040 is not yet posted; the DRT calendar shows the second estimated tax instalment on 15 July, while the mirror code date is 15 June (pay by 15 June and confirm with DRT); whether Guam levies the separate surtax of up to 10% that 1421i(a) allows (none was found).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gu-individual-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gu-individual-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
