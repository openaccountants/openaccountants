---
name: my-income-tax
description: Use this skill whenever asked about Malaysia income tax for self-employed individuals, sole proprietors and partners for year of assessment 2026. Trigger on phrases like Malaysia income tax, LHDN, Lembaga Hasil Dalam Negeri, hasil.gov.my, Form B, Form BE, Form M, section 4(a), personal reliefs Malaysia, chargeable income Malaysia, tax rebate RM400, Malaysian tax return, e-Filing Malaysia, or any question about Malaysian income tax rates, reliefs, deductions, capital allowances, filing or penalties for a business individual. Covers the Schedule 1 resident scale, the 30% non-resident rate, adjusted income, capital allowances, personal reliefs under sections 46 to 49 and 46B, the section 6A rebate, Form B filing and penalties. Year of assessment 2026 is calendar 2026 income, filed in 2027.
version: "2.0"
jurisdiction: MY
tax_year: 2026
tax_year_notes: "Year of assessment 2026 (basis year = calendar 2026), return due in 2027. Figures read from the Income Tax Act 1967 as at 1 January 2026."
last_updated: 2026-11-14
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

1. **Residence for 2026.** Days in Malaysia in 2026, and in 2025 and 2027 if under 182 (section 7). Residence switches the whole computation.
2. **Type of income.** Business or profession (Form B), employment only (Form BE), or both.
3. **Structure.** Sole proprietor, partner (partnership files Form P), or a company (out of scope).
4. **Gross income and expenses** for the 2026 basis year, with the asset purchases list for capital allowances.
5. **Family and spending facts** for reliefs: spouse with or without income, children's ages and studies, EPF, life insurance, PRS, medical and lifestyle receipts.
6. **CP500 instalments paid** for YA 2026 (credits against the final tax, see `my-pcb`).

Conservative defaults when a fact is missing:

| Ambiguity | Default |
| --- | --- |
| Residence unknown | Treat as non-resident (30% flat, no reliefs) until confirmed |
| Business-use share unknown | 0% deduction |
| Expense category unknown | Not deductible |
| Relief eligibility or receipt unknown | Do not claim |

Minimum records: bank statements for 2026, business type, residence facts. Better: sales and purchase invoices, EPF, SOCSO and EIS statements, the prior Form B and assessment, SSM registration. Best: full accounts, capital allowance schedule, partnership agreement, prior tax computation.

## The method, step by step

1. **Confirm residence** under section 7(1): 182 days or more in Malaysia in 2026 makes a resident; shorter stays can still qualify when linked to 182 consecutive days spanning the year boundary, or under the 90-day and three-year tests in section 7(1)(c) and (d). If not resident, go to step 8.
2. **Gross business income.** All receipts of the business for the basis year.
3. **Adjusted income.** Deduct expenses wholly and exclusively incurred in producing the income (section 33(1)) and remove the items barred by section 39 (table under "The base").
4. **Statutory income.** Deduct capital allowances under Schedule 3. Initial allowance is one-fifth of qualifying plant expenditure (Schedule 3 para 10); annual allowances are at prescribed rates (para 15). Assets of RM2,000 or less each may be written off in full (para 19A), capped at RM20,000 a year in total.
5. **Losses.** Unabsorbed business losses are set against aggregate income and carried forward for ten consecutive years of assessment (section 44(5F)), then lapse.
6. **Chargeable income.** Total income less the personal reliefs in the table below (sections 46 to 49 and 46B). Reliefs are for residents only.
7. **Tax.** Apply the Schedule 1 resident scale. Deduct the RM400 rebate if chargeable income is RM35,000 or less (section 6A), then zakat or fitrah paid (section 6A(3)), then CP500 instalments already paid.
8. **Non-resident.** Tax at a flat 30% of chargeable income (Schedule 1 para 1A), with no personal reliefs and no rebate.

### Rates, bands and thresholds

Resident scale, YA 2026 (ITA Schedule 1 Part I para 1). LHDN's tax-rate page shows the same scale for YA 2023 to 2025; the Act as at 1 January 2026 has not changed it.

| Chargeable income (RM) | Rate | Tax on the band (RM) | Tax at top of band (RM) | Source |
| --- | --- | --- | --- | --- |
| First 5,000 | 0% | 0 | 0 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf |
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
| Rental of a non-commercial vehicle, deduction cap (s. 39(1)(k)) | RM50,000; RM100,000 if new and cost up to RM150,000 | | | same |

Personal reliefs, YA 2026 (resident individuals; amounts are maximums unless fixed).

| Relief | Amount (RM) | Source |
| --- | --- | --- |
| Individual and dependent relatives (s. 46(1)(a)) | 9,000 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf |
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
| Registered child care centre or kindergarten, child aged 6 or under (s. 46(1)(r)) | 3,000 | same |
| Sports equipment, facility, competition and gym fees, additional (s. 46(1)(u)) | 1,000 | same |
| EV charging, food waste compost machine, and from YA 2026 food waste grinder and home CCTV (s. 46(1)(v) and (1A)) | 2,500 total | same |
| Housing loan interest, first home, SPA 1 Jan 2025 to 31 Dec 2027, three consecutive years, citizen (s. 46B), price up to RM500,000 | 7,000 | same |
| Same, price over RM500,000 up to RM750,000 (s. 46B) | 5,000 | same |
| Wife (or husband under s. 45A) with no income or joint assessment (s. 47(1)(a)); alimony to former wife within the same cap (s. 47(2)) | 4,000 | same |
| Disabled spouse, further (s. 47(1)(b)) | 6,000 | same |
| Each unmarried child under 18, or 18 and over in A-level, matriculation or preparatory study (s. 48(2)(a)) | 2,000 | same |
| Each unmarried child 18 and over at diploma level or higher in Malaysia, or degree level or higher abroad (s. 48(2)(b)) | 8,000 | same |
| Disabled child; a further 8,000 if 18 or over and studying at diploma level or higher (s. 48) | 8,000 | https://www.hasil.gov.my/en/individu/pelepasan-cukai/ |
| Life insurance or family takaful, and additional voluntary EPF (s. 49(1)(a)) | 3,000 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf |
| EPF or approved scheme contributions, including voluntary EPF of the self-employed (s. 49(1)(b)) | 4,000 | same |
| Education or medical insurance premiums (s. 49(1)(c)) | 4,000 | same |
| Private Retirement Scheme and deferred annuity (s. 49(1D)) | 3,000 | same |

### The base: what is deductible

| Item | Treatment |
| --- | --- |
| Cost of goods sold, staff wages and employer EPF, business rent, utilities, professional fees, marketing, business travel, business insurance | Deductible under s. 33(1) when wholly and exclusively for the business |
| Bad debts written off as irrecoverable | Deductible |
| Repairs and maintenance | Deductible if revenue in nature; improvements go to capital allowances |
| Export promotion, approved training, disabled employee costs, approved R&D | Double deduction where the specific rule allows; check it before claiming |
| Private or domestic expenses | Not deductible (s. 39(1)(a)) |
| Income tax itself | Not deductible |
| Entertainment | 50% disallowed (s. 39(1)(l)) unless an exception applies, for example staff entertainment or promotional samples linked to sales |
| Capital expenditure | Not deductible; claim capital allowances |
| Fines and penalties | Not deductible |
| Donations | Not a business expense; approved gifts are deducted from aggregate income under s. 44(6) and following |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Present fewer than 182 days but linked to 182 consecutive days with 2025 or 2027 | Resident under s. 7(1)(b); temporary absences for business, treatment or social visits up to 14 days count |
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
| CP500 instalment paid more than 30 days late (s. 107B(3)) | 10% of the instalment outstanding |
| Actual tax more than 30% above the revised estimate (s. 107B(4)) | 10% of the difference |
| Incorrect return, no prosecution (s. 113(2)) | Penalty equal to the tax undercharged |
| Incorrect return, prosecuted (s. 113(1)) | Fine RM1,000 to RM10,000 and 200% of the tax undercharged |
| Wilful evasion (s. 114(1)) | Fine RM1,000 to RM20,000, prison up to 3 years, or both, and 300% of the tax undercharged |

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

Not yet confirmed: the annual allowance rates for plant (prescribed by rules under Schedule 3 para 15, not opened; the old table showed 14% general plant, 10% office equipment, 20% motor vehicles and heavy machinery, 40% computers); the motor vehicle qualifying cost cap for capital allowances (old file RM100,000, or RM200,000 if on-the-road price up to RM150,000), also in the rules; the e-Filing grace period for YA 2026 returns (LHDN's 2027 programme is not yet published).
