---
name: my-income-tax
description: Use this skill whenever asked about Malaysia income tax for self-employed individuals, sole proprietors and partners for year of assessment 2026. Trigger on phrases like Malaysia income tax, LHDN, Lembaga Hasil Dalam Negeri, hasil.gov.my, Form B, Form BE, Form M, section 4(a), personal reliefs Malaysia, chargeable income Malaysia, tax rebate RM400, Malaysian tax return, e-Filing Malaysia, or any question about Malaysian income tax rates, reliefs, deductions, capital allowances, filing or penalties for a business individual. Covers the Schedule 1 resident scale, the 30% non-resident rate, adjusted income, capital allowances, personal reliefs under sections 46 to 49 and 46B, the section 6A rebate, Form B filing and penalties. Year of assessment 2026 is calendar 2026 income, filed in 2027.
version: "2.1"
jurisdiction: MY
tax_year: 2026
tax_year_notes: "Year of assessment 2026 (basis year = calendar 2026), return due in 2027. Figures read from the Income Tax Act 1967 as at 1 January 2026."
last_updated: 2026-11-22
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Malaysia income tax for self-employed individuals, year of assessment 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Malaysia.

## Scope

This skill computes Malaysian income tax for an individual who carries on a business or profession (section 4(a) of the Income Tax Act 1967, the ITA), as a sole proprietor or a partner, for **year of assessment (YA) 2026**. The basis year for an individual is the calendar year, so YA 2026 taxes income of 1 January to 31 December 2026, and the return (Form B, or Form M for a non-resident) is filed in 2027.

- Tax: income tax (Cukai Pendapatan), under the Income Tax Act 1967 (Act 53), online version as at 1 January 2026.
- Authority: Lembaga Hasil Dalam Negeri Malaysia (LHDN, also IRBM); portal MyTax, https://mytax.hasil.gov.my.
- Currency: ringgit (RM). Year: YA 2026, basis year calendar 2026.

Out of scope, with the skill that owns it:

- Companies (Sdn Bhd, Berhad) and their rates: `my-corporate-income-tax`.
- Monthly tax deductions from wages (PCB/MTD) and CP500 instalments: `my-pcb`.
- EPF, SOCSO and EIS contributions: `my-epf-socso`.
- Sales tax and service tax: `malaysia-sst`. e-Invoicing: `malaysia-einvoice`.
- Real property gains tax and the capital gains tax on unlisted shares: refer (R-MY-4).

## Ask the client first

1. **Residence for 2026.** Days in Malaysia in 2026, and in adjacent years and, where relevant, the preceding 4 years for the section 7 tests. Residence switches the whole computation.
2. **Type of income.** Business or profession (Form B), employment only (Form BE), or both.
3. **Structure.** Sole proprietor, partner (partnership files Form P), or a company (out of scope).
4. **Gross income and expenses** for the 2026 basis year, with the asset purchases list for capital allowances.
5. **Family and spending facts** for reliefs: spouse with or without income, children's ages and studies, EPF, life insurance, PRS, medical and lifestyle receipts.
6. **CP500 instalments paid** for YA 2026 (credits against the final tax, see `my-pcb`).

Conservative defaults when a fact is missing:

| Ambiguity | Default |
| --- | --- |
| Residence unknown | Confirm section 7 residence before finalising the return. Show a scenario only if its residence assumption is explicit. |
| Business-use share unknown | 0% deduction |
| Expense category unknown | Not deductible |
| Relief eligibility or receipt unknown | Do not claim |

Minimum records: bank statements for 2026, business type, residence facts. Better: sales and purchase invoices, EPF, SOCSO and EIS statements, the prior Form B and assessment, SSM registration. Best: full accounts, capital allowance schedule, partnership agreement, prior tax computation.

## The method, step by step

1. **Confirm residence** under section 7(1): 182 days or more in Malaysia in 2026 makes a resident; shorter stays can still qualify when linked to 182 consecutive days spanning the year boundary, or under section 7(1)(c) if the individual is in Malaysia for at least 90 days in 2026 and 3 of the 4 preceding years meet the residence or 90-day test. Section 7(1)(d) applies if the individual is resident in all 3 preceding years and in the following year. If not resident, go to step 8.
2. **Gross business income.** Apply sections 22 to 24 to business income for the basis period. Include qualifying sale or service debts when they arise and applicable advance payments when received.
3. **Adjusted income.** Deduct expenses wholly and exclusively incurred in producing the income (section 33(1)) and remove the items barred by section 39 (table under "The base").
4. **Statutory income.** Deduct capital allowances under Schedule 3. The standard initial allowance is 20% of qualifying plant expenditure (Schedule 3 para 10). Annual allowances depend on the asset category under para 15. A qualifying asset of RM 2,000 or less can use the para 19A allowance in place of the ordinary allowances. The combined special allowance for a sole proprietor is capped at RM 20,000 per YA.
5. **Losses.** Deduct current-year adjusted business losses against aggregate income under section 44(2). Carry forward the unused amount for the 10 consecutive YAs immediately after the loss year. Section 43(2) restricts those carried losses to aggregate statutory business income. Any balance then lapses under section 44(5F).
6. **Chargeable income.** Total income less the personal reliefs in the table below (sections 46 to 49 and 46B). Reliefs are for residents only.
7. **Tax.** Apply the Schedule 1 resident scale. Apply the RM 400 personal rebate at chargeable income of RM 35,000 or less and check the additional RM 400 spouse rebate where the statutory conditions apply. Deduct qualifying zakat or fitrah paid to an authorised religious authority, capped with other rebates at the tax charged (section 6A). Credit CP500 instalments paid against the balance.
8. **Non-resident.** Tax at a flat 30% of chargeable income (Schedule 1 para 1A), with no personal reliefs and no rebate.

### Rates, bands and thresholds

Resident scale, YA 2026 (ITA Schedule 1 Part I para 1). LHDN's tax-rate page shows the same scale for YA 2023 to 2025; the Act as at 1 January 2026 has not changed it.

| Chargeable income (RM) | Rate | Tax on the band (RM) | Tax at top of band (RM) | Source |
| --- | --- | --- | --- | --- |
| First 5,000 | 0% | 0 | 0 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf ; LHDN rate page (same scale, YA 2023 to 2025): https://www.hasil.gov.my/en/individu/kadar-cukai/ |
| 5,001 to 20,000 | 1% | 150 | 150 | same |
| 20,001 to 35,000 | 3% | 450 | 600 | same |
| 35,001 to 50,000 | 6% | 900 | 1,500 | same |
| 50,001 to 70,000 | 11% | 2,200 | 3,700 | same |
| 70,001 to 100,000 | 19% | 5,700 | 9,400 | same |
| 100,001 to 400,000 | 25% | 75,000 | 84,400 | same |
| 400,001 to 600,000 | 26% | 52,000 | 136,400 | same |
| 600,001 to 2,000,000 | 28% | 392,000 | 528,400 | same |
| Above 2,000,000 | 30% | | | same |
| Non-resident individual, every ringgit (Sch. 1 para 1A) | 30% | | | same |
| Rebate, chargeable income RM35,000 or less (s. 6A(2)) | RM400 | | | same |
| Residence test, days in Malaysia in the basis year (s. 7(1)(a)) | 182 | | | same |
| Loss carry-forward limit (s. 44(5F)) | 10 YAs | | | same |
| Initial allowance on plant (Sch. 3 para 10) | 20% | | | same |
| Small value asset, each (Sch. 3 para 19A) | RM2,000 | | | same |
| Small value assets, total a year (Sch. 3 para 19A proviso) | RM20,000 | | | same |
| Entertainment, share disallowed unless an exception applies (s. 39(1)(l)) | 50% | | | same |
| Rental of a vehicle without a commercial passenger or goods licence, aggregate deduction cap over all YAs (s. 39(1)(k)) | RM 50,000 per vehicle, or RM 100,000 if unused before rental and total cost is at most RM 150,000 | | | same |

Personal reliefs, YA 2026 (resident individuals; amounts are maximums unless fixed).

| Relief | Amount (RM) | Source |
| --- | --- | --- |
| Individual and dependent relatives (s. 46(1)(a)) | 9,000 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf ; LHDN reliefs page (YA 2025 list, same amounts): https://www.hasil.gov.my/en/individu/pelepasan-cukai/ |
| Parents' or grandparents' medical, dental, special needs and carer costs; complete medical examination within it up to 1,000 (s. 46(1)(c)) | 8,000 | same |
| Basic supporting equipment for a disabled self, spouse, child or parent (s. 46(1)(d)) | 6,000 | same |
| Disabled individual, further (s. 46(1)(e)) | 7,000 | same |
| Education fees, self: listed fields, Masters or Doctorate; upskilling courses within it up to 2,000 (s. 46(1)(f)) | 7,000 | same |
| Medical: serious disease, fertility, vaccination (within it up to 1,000), dental (within it up to 1,000) (s. 46(1)(g)) | 10,000 | same |
| Complete medical examination, self-test devices, mental health consultation, inside the s. 46(1)(g) cap (s. 46(1)(h)) | 1,000 | same |
| Child aged 18 or under: learning disability diagnosis and early intervention, inside the s. 46(1)(g) cap (s. 46(1)(ha)) | 10,000 overall cap | same |
| SSPN net deposit (s. 46(1)(k)) | 8,000 | same |
| SOCSO and EIS contributions (s. 46(1)(n)) | 350 | same |
| Lifestyle: books, computer, smartphone, tablet, internet, skills courses (s. 46(1)(p)) | 2,500 | same |
| Breastfeeding equipment, child aged 2 or under, once every two YAs (s. 46(1)(q)) | 1,000 | same |
| Registered childcare centre or kindergarten for a child aged 6 or under, or registered care centre for a child aged 12 or under (s. 46(1)(r)) | 3,000 total | [Act 874](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/3276537_BI/Act%20874%20-%20FINANCE%20ACT%202025.pdf) |
| Qualifying Malaysian tourist attraction or cultural or arts programme entrance fees, YA 2026 (s. 46(1)(sa)) | 1,000 | [Act 874](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/3276537_BI/Act%20874%20-%20FINANCE%20ACT%202025.pdf) |
| Sports equipment, facility, competition and gym fees, additional (s. 46(1)(u)) | 1,000 | same |
| Personal EV charging and qualifying household food waste compost machines, grinders and CCTV (s. 46(1)(v) and (1A)) | 2,500 total | same |
| Housing loan interest, first home, SPA 1 Jan 2025 to 31 Dec 2027, three consecutive years, citizen (s. 46B), price up to RM500,000 | 7,000 | same |
| Same, price over RM500,000 up to RM750,000 (s. 46B) | 5,000 | same |
| Wife (or husband under s. 45A) with no income or joint assessment (s. 47(1)(a)); alimony to former wife within the same cap (s. 47(2)) | 4,000 | same |
| Disabled spouse, further (s. 47(1)(b)) | 6,000 | same |
| Each qualifying unmarried child under 18, or older child in qualifying full-time study or under articles or indentures (s. 48(1)(a) to (c) and (2)(a)) | 2,000 | same |
| Each qualifying older unmarried child in approved full-time diploma or higher study in Malaysia, degree or equivalent study overseas, or qualifying articles or indentures in Malaysia (s. 48(3)(a)(i)) | 8,000 | same |
| Qualifying unmarried disabled child. Add RM 8,000 for an older child meeting the approved higher education or qualifying training conditions under s. 48(3) | 8,000 base | [Public Ruling 5/2026](https://www.hasil.gov.my/wp-content/uploads/20261104-PR-5_Taxation-Of-A-Resident-Individualpart-I-Gifts-Or-Contributions-And-Allowable-Deductions.pdf) |
| Life insurance or family takaful, and additional voluntary EPF (s. 49(1)(a)) | 3,000 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf ; https://www.hasil.gov.my/en/individu/pelepasan-cukai/ |
| EPF or approved scheme contributions, including voluntary EPF of the self-employed (s. 49(1)(b)) | 4,000 | same |
| Education or medical insurance premiums (s. 49(1B)) | 4,000 | same |
| Private Retirement Scheme and deferred annuity (s. 49(1D)) | 3,000 | same |

Apply the eligibility and receipt rules in [Public Ruling 5/2026](https://www.hasil.gov.my/wp-content/uploads/20261104-PR-5_Taxation-Of-A-Resident-Individualpart-I-Gifts-Or-Contributions-And-Allowable-Deductions.pdf). Childcare relief is per claimant across eligible children, with one claim between spouses living together. Section 48 child claims require maintenance and a check of the child's income and any claim by another eligible person. For first-home interest, count 3 YAs from the first interest payment and exclude a home used to earn income. Under section 46(1A), claim the compost machine once in 2025–27 and the grinder and CCTV once in 2026–27. For YA 2026, section 49(3A) extends qualifying life insurance and family takaful to children within section 48(9).

### The base: what is deductible

| Item | Treatment |
| --- | --- |
| Cost of goods sold, staff wages and employer EPF, business rent, utilities, professional fees, marketing, business travel, business insurance | Deductible under s. 33(1) when wholly and exclusively for the business |
| Irrecoverable trade debts | Deduct the qualifying amount under s. 34(2)–(3) when the debt was included in gross income and reasonable recovery steps support the write-off. Include recoveries in gross income. [Public Ruling 4/2019](https://www.hasil.gov.my/wp-content/uploads/PR_04_2019.pdf) |
| Repairs and maintenance | Deductible if revenue in nature; improvements go to capital allowances |
| Export promotion, approved training, disabled employee costs, approved R&D | Double deduction where the specific rule allows; check it before claiming |
| Private or domestic expenses | Not deductible (s. 39(1)(a)) |
| Income tax itself | Not deductible |
| Entertainment | 50% disallowed (s. 39(1)(l)) unless an exception applies, for example staff entertainment or promotional samples linked to sales |
| Capital expenditure | Not deductible; claim capital allowances |
| Fines and penalties | Not deductible |
| Donations | Not a business expense; approved gifts are deducted from aggregate income under s. 44(6) and following |

For a vehicle without a commercial passenger or goods licence, the separate purchase-cost limit for capital allowances is RM 50,000. Schedule 3 para 2(2) raises it to RM 100,000 if the vehicle was unused and total cost does not exceed RM 150,000. This caps qualifying plant expenditure rather than the rental deduction.

IRBM lists ordinary annual allowances of 20% for motor vehicles and heavy machinery, 14% for general plant and machinery and 10% for office equipment, furniture, fixtures and other assets. Under P.U. (A) 328/2024, qualifying scheduled ICT equipment can instead receive 40% initial and 20% annual allowance. Check the specific conditions and exclusions. Compare the distinct eligible e-invoicing relief, which uses a 20% initial and 40% annual allowance under P.U. (A) 162/2026 or 163/2026 as applicable.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Present fewer than 182 days but linked to at least 182 consecutive days with 2025 or 2027 | Apply s. 7(1)(b). Qualifying absence for Malaysian service, illness or social visits totalling at most 14 days can count under the statutory conditions. The individual must be in Malaysia immediately before and after the absence. The 14-day limit applies to social visits. |
| Non-resident with business income | Form M, 30% flat, no reliefs, no rebate (a non-resident consultant with RM200,000 Malaysian income pays RM60,000) |
| Chargeable income exactly RM35,000 | Rebate RM400 applies (s. 6A: "does not exceed") |
| Husband and wife both with income | Separate assessment by default; joint assessment by election (s. 45); spouse relief only where one has no income or they elect joint |
| CP500 instalments | A credit against final tax, never an expense |
| Partnership income | The partnership files Form P; each partner reports their share on Form B |
| Foreign-source income received in Malaysia | Refer (R-MY-3): the exemption for individuals has conditions and end dates |
| Asset used privately and for the business | Restrict to the business share; default 0% if unknown |

## Worked cases

Case 1, resident freelance designer. Gross revenue RM150,000, allowable expenses RM45,000, capital allowances RM5,000. Single. Voluntary EPF RM7,000 (RM4,000 under s. 49(1)(b) and RM3,000 additional voluntary under s. 49(1)(a)) and lifestyle spending RM2,500. Statutory income RM100,000. Reliefs RM9,000 + RM7,000 + RM2,500 = RM18,500. Chargeable income RM81,500. Tax RM3,700 on the first RM70,000 plus 19% of RM11,500 = RM5,885. No rebate.

```oa-check
name: Resident freelancer, YA 2026, chargeable income RM81,500
inputs:
  revenue: 150000
  expenses: 45000
  capital_allowances: 5000
  reliefs: 18500
steps:
  - statutory: revenue - expenses - capital_allowances
  - chargeable: statutory - reliefs
  - tax: 3700 + (chargeable - 70000) * 0.19
expected:
  statutory: 100000
  chargeable: 81500
  tax: 5885.00
```

Case 2, decision: top up a PRS contribution to reach the rebate? A resident part-time consultant has statutory income RM48,000 and reliefs of RM9,000 (individual) and RM2,500 (lifestyle). Chargeable income is RM36,500 and tax is RM600 + 6% of RM1,500 = RM690. If she pays RM1,500 into a Private Retirement Scheme in 2026 (relief up to RM3,000), chargeable income falls to RM35,000: tax RM600 less the RM400 rebate = RM200. The RM1,500 contribution saves RM490 of tax this year. Without it she pays RM690. The figure that decides it is whether chargeable income can be brought to RM35,000 or below.

```oa-check
name: PRS top-up to reach the section 6A rebate, YA 2026
inputs:
  statutory: 48000
  reliefs: 11500
  prs: 1500
steps:
  - chargeable_without: statutory - reliefs
  - tax_without: 600 + (chargeable_without - 35000) * 0.06
  - chargeable_with: statutory - reliefs - prs
  - tax_with: max(600 - 400, 0)
  - saving: tax_without - tax_with
expected:
  chargeable_without: 36500
  tax_without: 690.00
  chargeable_with: 35000
  tax_with: 200
  saving: 490.00
```

## When to refuse or refer

| Code | Trigger | Message |
| --- | --- | --- |
| R-MY-1 | Residence unknown | "Resident and non-resident individuals are taxed very differently. I cannot proceed until residence for 2026 is confirmed." |
| R-MY-2 | Client is a company (Sdn Bhd, Berhad) or LLP | "This skill covers individuals only. Companies file Form C; use my-corporate-income-tax and a tax agent." |
| R-MY-3 | Foreign-source income received in Malaysia | "Foreign-source income received in Malaysia may be exempt or taxable depending on conditions. Refer to a specialist." |
| R-MY-4 | Gains on real property, on shares in a real property company, or on unlisted shares | "Real property gains tax and capital gains tax are separate regimes. Out of scope." |
| R-MY-5 | Tax incentive, pioneer status or investment tax allowance | "Incentive claims need the approval letter and a specialist. Out of scope." |

Never: apply resident rates without confirming residence; give reliefs to a non-resident; deduct entertainment in full without an exception; deduct capital expenditure as revenue; treat CP500 instalments as expenses; present the result as final rather than an estimate.

## Filing and payment

| Form | Who | Due (statute, s. 77) | e-Filing grace (LHDN 2026 programme, YA 2025 returns) |
| --- | --- | --- | --- |
| BE | Resident with no business income | 30 April | 15 days (to 15 May) |
| B | Resident with business income | 30 June | 15 days (to 15 July) |
| P | Partnership | 30 June | 15 days |
| M | Non-resident individual | 30 April (no business) or 30 June (business) | 15 days |

For YA 2026 the returns fall due on 30 April 2027 (Form BE) and 30 June 2027 (Form B). Steps: register on MyTax and get a tax identification number; complete e-B with the business income, reliefs and computation; submit; pay the balance of tax (after CP500 instalments) by the same due date.

Penalties (LHDN offences page and ITA):

| Offence | Penalty |
| --- | --- |
| Not furnishing a return (s. 112(1)) | Fine RM200 to RM20,000, prison up to 6 months, or both; or a penalty under s. 112(3) instead of prosecution |
| Late payment of the balance (s. 103(3)) | Increase of 10% of the tax unpaid (the further 5% under old s. 103(4) was deleted) |
| CP500 instalment unpaid more than 30 days after its due date (s. 107B(3)) | 10% of the amount then unpaid, subject to any applicable concession |
| Shortfall after an approved CP500 variation (s. 107B(4)) | If assessed tax less instalments payable exceeds 30% of assessed tax, charge 10% on the part of the shortfall above that 30% |
| Incorrect return, no prosecution (s. 113(2)) | Penalty equal to the tax undercharged |
| Incorrect return, prosecuted (s. 113(1)) | Fine RM1,000 to RM10,000 and 200% of the tax undercharged |
| Wilful evasion (s. 114(1)) | Fine RM1,000 to RM20,000, prison up to 3 years, or both, and 300% of the tax undercharged |

[IRBM's 5 January 2026 notice](https://www.hasil.gov.my/wp-content/uploads/20260105-kenyataan-media-hasil-konsesi-pengenaan-penalti-cp500-bg-individu-yg-menerima-pendapatan-penggajian.pdf) gives a YA 2026 CP500 non-payment penalty concession to individuals with both employment and non-employment income. Check the taxpayer's income sources and use the assessed balance for final payment.

## Completion checklist

- Residence decided and recorded with the day count.
- Every expense tested against s. 33 and s. 39; entertainment split.
- Capital allowance schedule ties to the asset list.
- Each relief has a receipt and is within its cap.
- Rebate tested at RM35,000.
- CP500 paid deducted as a credit; balance and due date stated.
- Output labelled as an estimate for review.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Schedule 1 rates (resident scale and non-resident 30%), s. 6A rebate, s. 7 residence, s. 39 disallowances, s. 44(5F) losses, s. 46, 46B, 47, 48 and 49 reliefs, s. 103 and s. 113, Schedule 3 paras 10, 15 and 19A: Income Tax Act 1967, online version as at 1 January 2026 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf | 2026-11-14 |
| Read for LHDN's resident scale table for YA 2023 to 2025 | https://www.hasil.gov.my/en/individu/kadar-cukai/ | 2026-11-14 |
| Read for LHDN's YA 2025 relief list and the disabled-child further relief | https://www.hasil.gov.my/en/individu/pelepasan-cukai/ | 2026-11-14 |
| Read for the fines and penalties table (s. 112 to 120, s. 103(3), s. 107B) | https://www.hasil.gov.my/en/perundangan/kesalahan-denda-dan-penalti/ | 2026-11-14 |
| Read for the 2026 return filing programme: Forms BE, B, P, M due dates and the 15-day e-Filing grace | https://www.hasil.gov.my/wp-content/uploads/rf-filing-programme-for-2026.pdf | 2026-11-14 |
| Finance Act 2025, Act 874, YA 2026 relief amendments. | https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/3276537_BI/Act%20874%20-%20FINANCE%20ACT%202025.pdf | 2026-11-22 |
| Public Ruling 5/2026, resident deductions and conditions. | https://www.hasil.gov.my/wp-content/uploads/20261104-PR-5_Taxation-Of-A-Resident-Individualpart-I-Gifts-Or-Contributions-And-Allowable-Deductions.pdf | 2026-11-22 |
| Public Ruling 4/2026, small-value assets. | https://www.hasil.gov.my/wp-content/uploads/PR-No.4_2026-Special-Allowances-For-Small-Value-Assets.pdf | 2026-11-22 |
| Public Ruling 4/2019, trade debt deduction and recovery. | https://www.hasil.gov.my/wp-content/uploads/PR_04_2019.pdf | 2026-11-22 |
| IRBM general annual allowances for plant, equipment and vehicles. | https://www.hasil.gov.my/syarikat/perniagaan-digital/ | 2026-11-22 |
| P.U. (A) 328/2024, eligible ICT equipment. | https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/2460510/PUA%20328%20%282024%29.pdf | 2026-11-22 |
| IRBM FAQ on the specified e-invoicing accelerated allowance. | https://www.hasil.gov.my/wp-content/uploads/lhdnm-e-invoice-general-faqs.pdf | 2026-11-22 |
| IRBM CP500 January 2026 penalty concession for mixed income. | https://www.hasil.gov.my/wp-content/uploads/20260105-kenyataan-media-hasil-konsesi-pengenaan-penalti-cp500-bg-individu-yg-menerima-pendapatan-penggajian.pdf | 2026-11-22 |

Not yet confirmed: the e-Filing and payment grace period for YA 2026 individual returns. Use the statutory dates until IRBM publishes the 2027 programme. Asset-specific accelerated allowances require the asset, acquisition and use dates and the applicable legal instrument.
