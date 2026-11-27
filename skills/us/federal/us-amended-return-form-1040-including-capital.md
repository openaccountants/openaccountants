---
name: us-amended-return-form-1040-including-capital
description: How to correct a filed US Form 1040 series return with Form 1040-X in 2026, including rebuilding a mis-stated capital loss deduction or capital loss carryforward year by year. Covers the refund time limits (3 years from filing or 2 years from payment, and the lookback cap), early and extended filing dates, the $3,000 ($1,500 married filing separately) loss limit under 26 U.S.C. 1211(b), how 1212(b) keeps short-term and long-term character and uses adjusted taxable income, electronic and paper filing, the excessive claim penalty and tracking. Trigger on "amend my return", "Form 1040-X", "capital loss carryover wrong", "fix last year's Schedule D", "refund claim deadline". For individuals and their preparers. Federal only.
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
category: federal
type: filing-howto
---

# Form 1040-X amended returns and capital loss carryforward corrections in the United States

Use the forms for the year being corrected and rebuild capital losses from the earliest wrong year before deciding which returns need amendment.

> **General reference only.** This Guide has not been reviewed for a particular taxpayer's documents, elections, deadlines, residency or filing status. It supports professional review before filing or taking a position.

## Scope and who this is for

This is a 2026 reference for individuals correcting filed Forms 1040, 1040-SR or 1040-NR with Form 1040-X, including amounts previously changed by the IRS. File a separate amendment for each affected year. The [continuous-use instructions](https://www.irs.gov/instructions/i1040x) cover December 2025 and later Form 1040-X revisions unless superseded; use the underlying return, schedules and tax rules for the year amended. The examples below retain their original 2025 loss years and 2026 carryovers.

The IRS may correct certain errors or accept a return without some required attachments without requiring an amendment. Amend when filing status, income, deductions, credits or tax liability changes. Use the IRS **Should I file an amended return?** tool when the need is unclear. [IRS Topic 308](https://www.irs.gov/taxtopics/tc308); [IRS amendment guidance](https://www.irs.gov/newsroom/when-and-how-to-amend-a-tax-return).

Forms 1040-SS and pre-2023 1040-PR have their own amended-return procedure: an electronic correction includes the necessary schedules but **does not attach Form 1040-X**. See the [IRS FAQ](https://www.irs.gov/filing/amended-return-frequently-asked-questions). Their detailed preparation, paper nonresident amendments and changes between resident and nonresident returns are referred below.

## Ask the client first

- Which years, original filing/receipt dates, extensions and separate payment dates are involved? Obtain filing acknowledgments and payment records.
- What returns, Forms 8949, Schedules D and carryover worksheets were filed, and what did earlier amendments, audits or notices change?
- What filing status and spouse owned each loss? Did a joint year precede separate years?
- What was taxable income before the zero floor, and was any section 151 or in-lieu deduction allowed in each loss year?
- Is this an ordinary investment sale, personal-use loss, bad debt, worthless security, carryback or disputed basis/wash-sale/holding-period issue?
- Is there disability, disaster or combat-zone relief, a foreign tax credit, a special election, a state return, or another special filing?

## The method, step by step

### Rates, bands and thresholds

| Item | Rule and operative condition | Official source |
|---|---|---|
| Ordinary refund claim deadline | For a filed return, claim within 3 years from filing or 2 years from payment, whichever period expires later. If no return was filed, the statutory rule is 2 years from payment; this Guide does not prepare an unfiled return. Special cases below are referred. | [26 USC 6511(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapB-sec6511.htm) |
| Early return or payment | A return filed before the prescribed filing date is deemed filed then, ignoring extensions. Advance tax payments are similarly dated to the prescribed payment date for the refund lookback. A return received during an extension, after the ordinary deadline but before the extended deadline, uses its actual receipt date for the 3-year clock; do not add the extension again to that clock. | [26 USC 6513(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapB-sec6513.htm); [1040-X, When To File](https://www.irs.gov/instructions/i1040x) |
| Deemed payment dates | Chapter 24 wage withholding is deemed paid on the 15th day of the fourth month after the tax year; estimated income tax on the prescribed return filing date without extensions. Do not replace these statutory dates with the date a late return is filed. | [26 USC 6513(b)(1)-(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapB-sec6513.htm) |
| Refund amount cap, separately from timeliness | A claim within the 3-year filing period recovers only tax paid within the preceding 3 years plus the filing extension. Otherwise only tax paid within the preceding 2 years. A timely claim can therefore yield no refund. Special postponements are referred below. | [26 USC 6511(b)(2)(A)-(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapB-sec6511.htm); [current IRS lookback guidance](https://www.irs.gov/instructions/i1040x) |
| Individual net capital loss deduction | Losses offset gains; the excess deductible against other income is the smaller of the net loss or USD 3,000 (USD 1,500 married filing separately). Fixed statutory amounts apply to the 2025 examples and 2026 reference. | [26 USC 1211(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1211.htm) |
| Excessive income-tax refund or credit claim | Section 6676 imposes 20% of the excess over the allowable claim unless reasonable cause is shown. A noneconomic-substance transaction under section 6662(b)(6) cannot have reasonable cause for this purpose; no section 6676 charge on a portion already subject to the penalties identified in section 6676(d). | [26 USC 6676(a)-(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6676.htm) |

### Rebuild the loss and each affected return

1. **Reconcile the starting records.** Compare the original return, IRS tax records and every later adjustment. Form 1040-X column A uses the original figures unless a previous amendment, audit or IRS notice changed them; then use the adjusted figures. The [Individual Account](https://www.irs.gov/filing/wheres-my-amended-return) provides tax records. [1040-X, Columns A Through C](https://www.irs.gov/instructions/i1040x).
2. **Recompute transactions for the original year.** Most capital transactions go through Form 8949 and then Schedule D. A loss on personal-use property, such as a home or car, is not deductible. Do not invent a loss carryover from it. For **2025**, Schedule D line 16 is the net result, line 21 limits the loss deduction, and Form 1040/1040-SR/1040-NR line 7a reports the allowed capital loss. These are not approved 2026 line mappings. [IRS Topic 409](https://www.irs.gov/taxtopics/tc409); [2025 Schedule D instructions](https://www.irs.gov/instructions/i1040sd); [2025 Schedule D, lines 16 and 21](https://www.irs.gov/pub/irs-prior/f1040sd--2025.pdf).
3. **Compute what survives.** Under [26 USC 1212(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm), short-term and long-term carryovers keep their character. Adjusted taxable income for this purpose equals taxable income, including a negative amount before the return's zero floor, plus the section 1211(b) allowed loss plus the deduction under section 151 or in lieu of it. Take the smaller of the allowed loss and adjusted taxable income, with a zero floor, as the loss absorbed. Short-term losses are used first. Do not assume section 151 is always zero: for a senior deduction or another uncertain in-lieu deduction, use the referral below. [Publication 550, Capital Losses and Worksheet 4-1](https://www.irs.gov/publications/p550).
4. **Roll forward year by year.** Apply the relevant year's Capital Loss Carryover Worksheet and feed the result into the next year. The allowable current-year deduction reduces a carryover whether or not it was claimed, or a return was filed. The **2025** worksheet tests the 2024 Schedule D lines 21/16 and negative 2024 Form 1040 line 15; it carries short-term loss to 2025 Schedule D line 6 and long-term to line 14. It does not establish 2026 line numbers. A joint-year carryover belongs only to the spouse who actually sustained that loss when filing separately. [2025 Schedule D, worksheet](https://www.irs.gov/instructions/i1040sd); [Publication 550, Capital loss carryover](https://www.irs.gov/publications/p550).
5. **Follow every dependent change.** Recompute AGI-dependent deductions, credits and other affected lines for each year. Rebuilding a carryover does not itself mean the loss year's filed return was wrong. Test the refund deadline and payment lookback for each year that needs a claim. [1040-X, Line 1](https://www.irs.gov/instructions/i1040x).

### Prepare, file and pay

1. **Complete one Form 1040-X per affected year.** Column B is the net increase or decrease for each changed line; explain every change in Part II. Column C is A plus the increase or minus the decrease. Attach forms supporting the changes. Sign and date; both spouses sign an amended joint return. A representative signing needs specific power-of-attorney authority attached. [1040-X, Columns A Through C and Sign Your Return](https://www.irs.gov/instructions/i1040x).
2. **Electronic filing.** Use participating tax software or a preparer. The current or two prior tax periods can be amended electronically; older years must use paper. A prior-year return first filed on paper during the current processing year must also be amended on paper. Up to three electronic amendments per year are accepted; after the third acceptance, subsequent electronic attempts are rejected. Multiple timely amendments are otherwise possible. Submit all necessary forms and schedules as for an original submission, including unchanged forms, plus Form 1040-X for Forms 1040/1040-SR/1040-NR. [IRS FAQ](https://www.irs.gov/filing/amended-return-frequently-asked-questions); [1040-X, When To File](https://www.irs.gov/instructions/i1040x).
3. **Paper filing for resident Forms 1040/1040-SR.** Place the completed, updated return behind Form 1040-X, followed by new or changed schedules in Attachment Sequence No. order and supporting statements last. Attach required supporting wage/withholding documents as directed in **Assembling Your Return** and use **Where To File** for the address applicable to that taxpayer and claim. Do not attach the unchanged original return unless required. Nonresident paper cases have different completion instructions and are referred below. [1040-X instructions](https://www.irs.gov/instructions/i1040x).
4. **Additional tax or refund.** If the original filing deadline has not passed, file the corrected return or Form 1040-X and pay by that deadline, ignoring a filing extension; the return supersedes the original. If it falls on a weekend or legal holiday, the next business day is timely. After that deadline, do not send another original return; leave interest and penalties off Form 1040-X and pay additional tax promptly. Interest applies to tax unpaid by its due date even with a filing extension. Pay using [IRS Direct Pay or the Individual Account](https://www.irs.gov/payments). For an electronic amendment, direct deposit can be requested for tax years 2021 and later using banking information on Form 1040-X. [Topic 308](https://www.irs.gov/taxtopics/tc308); [1040-X, Interest and Part III](https://www.irs.gov/instructions/i1040x).
5. **Retain the acknowledgment and track receipt.** Use [Where's My Amended Return?](https://www.irs.gov/filing/wheres-my-amended-return) or 866-464-2050 after three weeks; English and Spanish are available. The tools cover the current and three prior tax years. IRS general processing guidance is 8 to 12 weeks, sometimes up to 16; this is not a guaranteed completion date. Carrybacks, injured-spouse and certain specialized returns cannot be tracked there. [IRS FAQ](https://www.irs.gov/filing/amended-return-frequently-asked-questions).
6. **Check the state separately.** A federal change can affect state tax. Contact the state agency for its amendment procedure and do not attach a state return to the federal amendment. [Topic 308](https://www.irs.gov/taxtopics/tc308); [IRS amendment guidance](https://www.irs.gov/newsroom/when-and-how-to-amend-a-tax-return).

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Low/negative taxable income | Use the negative figure and the adjusted-taxable-income calculation above; the full annual deduction need not be absorbed. |
| Separate returns after a joint loss year | Trace the carryover to the spouse who actually had the loss. |
| Allegedly closed loss year | A refund deadline does not by itself decide a later year's corrected carryover. Check this point with one of our partner accountants. |
| Missing original returns, transaction evidence, IRS adjustments or payment dates | Do not provide a usable amended-return amount or deadline. Check this point with one of our partner accountants. |

## Worked cases

**Case 1: carryforward that kept the whole loss.** A single filer's **2025** Schedule D shows a net short-term loss of USD 2,000 and net long-term loss of USD 8,000, with adjusted taxable income USD 50,000. The return deducted USD 3,000 but the working paper carried all USD 10,000 into 2026. Assuming the 2025 return and deduction were otherwise correct, no 2025 amendment is needed merely to correct that working paper. Section 1212(b) treats the USD 3,000 used as short-term gain: it absorbs the USD 2,000 short-term loss and USD 1,000 long-term. Correct **2026** carryover: USD 0 short-term and USD 7,000 long-term. Use the final 2026 Schedule D when filing; if a 2026 return is subsequently filed using the incorrect carryover, amend that return and recompute dependent amounts. [26 USC 1212(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm).

```oa-check
name: Character and size of a capital loss carryforward (1212(b))
inputs:
  st_loss: 2000
  lt_loss: 8000
  limit: 3000
  adjusted_taxable_income: 50000
steps:
  - used: min(limit, adjusted_taxable_income, st_loss + lt_loss)
  - st_carryover: max(st_loss - used, 0)
  - lt_carryover: lt_loss - max(used - st_loss, 0)
  - total_carryover: st_carryover + lt_carryover
expected:
  used: 3000
  st_carryover: 0
  lt_carryover: 7000
  total_carryover: 7000
```

**Case 2: a low-income year uses less loss.** A single student's **2025** return has USD 5,000 net short-term loss and no long-term result. After the USD 3,000 capital loss and the standard deduction, taxable income before the zero floor is minus USD 2,000. For this conditional example, the supplied section 151/in-lieu deduction is **USD 0**; this is not a statement that every student's or senior's deduction is zero. Adjusted taxable income is minus USD 2,000 + USD 3,000 + USD 0 = USD 1,000. Only USD 1,000 is absorbed; **USD 4,000 short-term carries into 2026**, rather than USD 2,000. If a 2026 return is subsequently filed with USD 2,000, correct it and subsequent affected years, testing deadlines independently. No refund amount can be determined from these inputs. If a section 151 senior or in-lieu deduction applies, this example is not a usable computation for that taxpayer: Check this point with one of our partner accountants. [26 USC 1212(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm); [Publication 550, Worksheet 4-1](https://www.irs.gov/publications/p550).

```oa-check
name: Adjusted taxable income limits the loss used up (1212(b)(2))
inputs:
  st_loss: 5000
  limit: 3000
  taxable_income_if_negative: -2000
  personal_exemption: 0
steps:
  - adjusted_taxable_income: taxable_income_if_negative + limit + personal_exemption
  - used: max(min(limit, adjusted_taxable_income), 0)
  - st_carryover: st_loss - used
  - wrong_carryover: st_loss - limit
  - understated_by: st_carryover - wrong_carryover
expected:
  adjusted_taxable_income: 1000
  used: 1000
  st_carryover: 4000
  wrong_carryover: 2000
  understated_by: 2000
```

## When to refuse or refer

Each case below is outside this Guide's usable computation and deadline instructions. Do not treat the ordinary refund deadline as its answer.

- Bad debts and worthless securities, including their special refund periods and carryover effects: Check this point with one of our partner accountants.
- Financial disability and possible suspension, including whether anyone was authorized to manage the individual's finances: Check this point with one of our partner accountants.
- Loss/credit carrybacks, net operating losses, foreign tax credits and section 1256 contract loss elections: Check this point with one of our partner accountants.
- Federal or State-declared disasters, combat/contingency service, special lookback postponements and qualified wildfire payments: Check this point with one of our partner accountants.
- Domestic research expenditure/section 174A elections, their deadlines and Rev. Proc. 2025-28 procedures: Check this point with one of our partner accountants.
- Penalty/interest-only refunds (Form 843), injured spouse allocations (Form 8379), wage corrections involving W-2c/W-3c or disclosures on Form 8886: Check this point with one of our partner accountants.
- Paper nonresident amendments, residence-form conversions, Forms 1040-SS/pre-2023 1040-PR, entity/estate/trust amendments and state amendments: Check this point with one of our partner accountants.
- Capital gain rate selection (including the original historical 2025 most-individuals rate summary): Check this point with one of our partner accountants.
- Contested basis, wash sales, holding periods, debt cancellation reducing tax attributes, or a section 151/in-lieu deduction whose carryover treatment has not been established for the taxpayer: Check this point with one of our partner accountants.

## Sources

| Source and portion actually read or applicable completed read reused | URL | Read on |
|---|---|---|
| Read in 1040-X, December 2025 continuous-use instructions: scope, revision, refund limits and neighbouring exceptions, columns, AGI effects, signature, attachments, interest and deposit | https://www.irs.gov/instructions/i1040x | 2026-11-26 |
| Read in 26 USC 6511(a), (b)(2); special cases (d), (h) read to bound referrals; ordinary rules corroborated by current IRS instructions | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapB-sec6511.htm | 2026-11-26 |
| Read in 26 USC 6513(a), (b): statutory filing and payment dates | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapB-sec6513.htm | 2026-11-26 |
| Read in 26 USC 6676(a)-(d): excess definition, reasonable cause and penalty coordination | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6676.htm | 2026-11-26 |
| Read in 26 USC 1211(b): fixed individual loss limit; completed US capital-gains read reused for 2025/2026 | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1211.htm | 2026-11-26 |
| Read in 26 USC 1212(b): character and adjusted taxable income; completed US capital-gains read reused, conditions checked against both original cases | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm | 2026-11-26 |
| Read in Publication 550 (2025), Capital Losses and Worksheet 4-1: carryover, zero floor, short-term first; completed US capital-gains exact read reused | https://www.irs.gov/publications/p550 | 2026-11-26 |
| Read in 2025 Schedule D: carryover worksheet for 2024 to 2025, line mappings and joint-to-separate allocation; no 2026 line certification | https://www.irs.gov/instructions/i1040sd | 2026-11-26 |
| Read in 2025 Forms 1040 and Schedule D: capital-loss line 7a and Schedule D lines 16/21 (PDFs read in memory) | https://www.irs.gov/pub/irs-prior/f1040sd--2025.pdf; https://www.irs.gov/pub/irs-prior/f1040--2025.pdf | 2026-11-26 |
| Read in IRS Topic 409: personal-use losses, Form 8949/Schedule D and 2025 return line; completed US capital-gains read reused | https://www.irs.gov/taxtopics/tc409 | 2026-11-26 |
| Read in Amended-return FAQ: electronic years, exceptions, count, 1040-SS distinction, attachments, deposit, timing and status limitations | https://www.irs.gov/filing/amended-return-frequently-asked-questions | 2026-11-26 |
| Read in IRS Topic 308: need to amend, original/superseding return, payment, weekend, status and state effects | https://www.irs.gov/taxtopics/tc308 | 2026-11-26 |
| Read in IRS amendment guidance: Interactive Tax Assistant and state attachments | https://www.irs.gov/newsroom/when-and-how-to-amend-a-tax-return | 2026-11-26 |
| Read in Where's My Amended Return: online account records and status access | https://www.irs.gov/filing/wheres-my-amended-return | 2026-11-26 |
| Read in IRS payment options: Direct Pay and Individual Account | https://www.irs.gov/payments | 2026-11-26 |

Not yet confirmed: final 2026 form-line mappings, special cases explicitly referred above, and any individual outcome without the original returns and supporting evidence. These are non-usable holds; no 2026 line number or special deadline is supplied.
