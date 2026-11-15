---
name: jp-social-insurance
description: Use for Japanese self-employed National Health Insurance (国民健康保険, kokumin kenko hoken) and National Pension (国民年金, kokumin nenkin), fiscal-year premiums, household and municipal inputs, pension relief, mid-year changes and payment matching. Covers FY2026, with Shinjuku's actual municipal NHI schedule as a named example, not a national tariff. Route employees on employer insurance to japan-payroll.
version: 2.1
jurisdiction: JP
tax_year: 2026
tax_year_notes: "Fiscal 2026: April 2026-March 2027. Premiums and relief periods have different calendars; 2026 cash deductions use amounts actually paid."
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
status: needs_sources
domain: payroll
type: computation
---

# Japan self-employed health insurance and pension v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Self-employed people, freelancers, students and others whose actual insurance status puts them in municipal NHI and/or National Pension Category 1. NHI and pension have separate eligibility tests. National Pension Category 1 generally covers residents aged 20-59 who are neither Category 2 employees nor Category 3 dependent spouses; medical-stay and long-tourism visa exclusions must be checked. A freelancer label does not itself prove Category 1 or NHI status. Employer insurance is handled in `japan-payroll`, not charged again here.

Currency is JPY. FY2026 premiums apply April 2026-March 2027. NHI income generally refers to the preceding calendar year; it is not current-year profit. The NHI debtor can be the registered household head even when that head is insured elsewhere. The figures below are **Shinjuku's** municipal schedule; obtain the actual municipality's current assessment before any client payment instruction.

| Quick reference | Figure/condition | Official source |
| --- | --- | --- |
| National Pension Category 1 | Ages 20-59 resident, excluding Category 2/3 and stated visa exclusions | National Pension Act eligibility, JPS explanation: https://www.nenkin.go.jp/international/simplejapanese/japanese-system/nationalpension/nationalpension.html |
| FY2026 monthly pension | JPY 17,920, April 2026-March 2027, before approved relief/discount | National Pension Act art. 87 annual premium: https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryo.html |
| Full FY2026 pension | JPY 215,040, derived as 12 monthly payments without relief/advance discount | Same: https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryo.html |
| Historical FY2025 monthly pension | JPY 17,510, April 2025-March 2026 only; do not use for later months | JPS annual premium table: https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryogaku.html |
| Shinjuku NHI structure FY2026 | Medical + elderly support + long-term care where applicable + new child-support component | NHI Act art. 76; local premium schedule: https://www.city.shinjuku.lg.jp/kenkou/hoken01_002065_00003.html |

## Ask the client first

Before computing obtain: residence/visa and qualification dates; date of birth; municipality and household head; every insured household member and relevant age interval; prior-year income and tax returns for all required people; employer health/pension and dependent status; changes during the year; pension exemption/deferral decisions; childbirth/childcare relief; NHI reduction decisions; actual bills and payment records. Ask for evidence of no income rather than defaulting missing income to zero. Missing age, municipality or other-insurance status also means **hold**, not assume under-age or uninsured.

Preserved referrals:

- **R-JP-SI-1 -- Disability pension:** Eligibility/computation requires case-specific assessment; refer to a social insurance labour consultant.
- **R-JP-SI-2 -- Survivors pension:** Claims are outside this skill; refer.
- **R-JP-SI-3 -- Voluntary additional pension (Kokumin Nenkin Kikin):** Separate scheme advice; refer.
- Employer shakai hoken enrolment: STOP the duplicate NHI computation and resolve the actual coverage before continuing.

## The method, step by step

### Establish pension months and relief

Confirm the Category 1 qualification record month by month. Register becoming Category 1 with the municipal office using **国民年金被保険者関係届書（申出書）** within 14 days (JPS eligibility page). A job change, a dependent-spouse status or leaving Japan can change the record. Turning 60 requires a qualification-end check; voluntary continuation has separate conditions and is referred, not silently treated as compulsory Category 1.

For months without relief/discount multiply the actual fiscal year's premium by chargeable months. Never use the FY2026 amount for January-March 2026 or treat a fiscal premium total as calendar-year cash paid. Advance payment is available for 6 months, 1 year or 2 years and early bank debit; use the JPS amount for the actual method/start period. The old approximate percentage discounts are not a schedule. The current early monthly debit saves JPY 60, per the linked JPS table.

Income-tested relief needs an application and approval. Exemption considers the applicant, spouse and household head; payment deferral generally considers applicant and spouse and covers ages 20 to under 50. Students use their separate student scheme; statutory disability/welfare exemptions and prenatal/postnatal relief have separate routes. Do not infer approval from low income.

| Pension relief, current JPS criteria | Prior-income ceiling formula/condition | FY2026 monthly payment after approval | Official source |
| --- | --- | --- | --- |
| Full exemption | (Number of dependants + 1) × JPY 350,000 + JPY 320,000, for each person whose income is tested; special personal-status rules may alter it | JPY 0 | National Pension Act relief rules, JPS criteria: https://www.nenkin.go.jp/service/kokunen/menjo/20150428.html |
| 3/4 exemption | JPY 880,000 + relevant dependant and social-insurance deductions, etc. | JPY 4,480 | Same: https://www.nenkin.go.jp/service/kokunen/menjo/20150428.html |
| 1/2 exemption | JPY 1,280,000 + relevant deductions | JPY 8,960 | Same: https://www.nenkin.go.jp/service/kokunen/menjo/20150428.html |
| 1/4 exemption | JPY 1,680,000 + relevant deductions | JPY 13,440 | Same: https://www.nenkin.go.jp/service/kokunen/menjo/20150428.html |
| Deferral | Full-exemption income formula; ages 20 to under 50; applicant/spouse test | Deferred, not an approved permanent waiver | Same: https://www.nenkin.go.jp/service/kokunen/menjo/20150428.html |
| Early monthly bank debit | FY2026 method-specific discount JPY 60; not the ordinary next-month debit | JPY 17,860 | JPS advance-payment table: https://www.nenkin.go.jp/service/kokunen/hokenryo/zenno.html |

For the current ordinary relief year July 2026-June 2027 the tested income is calendar 2025; January-June 2026 belongs to the previous relief year. Verify the correct period and special cases with the linked JPS application-period table. The old flat approximate partial-relief thresholds of JPY 930,000/1,410,000/1,890,000 are not universal legal tests.

Ordinary approved exemption can reduce the pension amount credited; deferral does not add to the old-age benefit amount until repaid, although qualifying periods can count. Partial exemption requires paying the remaining premium: otherwise the period is unpaid. Approved exempt/deferred months may be paid back within 10 years, with applicable additions. Unpaid months and approved relief are not equivalent.

**October 2026 change:** Category 1 actual/adoptive parents (including the JPS-listed foster situations), living at the same address as a child under 1, can have childcare premium exemption without an income test. Both qualifying parents can benefit; Category 3 and voluntary contributors are excluded. Only months from October 2026 qualify. Fathers/adoptive parents generally have the parenting month through the month before the first birthday, at most 12 months; birth mothers with prenatal/postnatal exemption generally receive the following 9 months, limited by commencement. These exempt months count as **fully paid** for the old-age amount, unlike ordinary income-tested relief. Already paid or otherwise relieved months may be converted, with credit/refund. Obtain the JPS notice: some confirmed birth mothers continue automatically; others file the combined **国民年金産前産後免除該当届/育児免除該当・終了届** through municipality/post/Mynaportal, with identity, parent-child and same-address evidence. Report an early loss of qualifying co-residence; expiry at the child's age limit needs no end notice (JPS childcare page).

### Compute the municipal NHI estimate

1. Verify actual NHI membership and insured months; do not equate the filing date with qualification. In Shinjuku the charge begins from qualification, and late notification can produce retrospective billing. Obtain the current revised household notice after a move or insurance change.
2. Establish each insured person's prior-calendar-year income under the municipal definition, including relevant separately taxed income. Subtract the municipality's applicable basic deduction and floor at zero, **per insured person**, then aggregate the appropriate people for each component. Shinjuku's JPY 430,000 deduction here applies when total income is at most JPY 24,000,000; higher bands must be obtained separately. This is not the national income-tax basic deduction.
3. For each component multiply the applicable aggregate income base by its municipal rate and add the per-person amount. Only applicable age groups enter the flat/long-term-care bases. Check local per-household/asset-based elements rather than assuming every municipality uses Shinjuku's shape.
4. Apply approved reductions to the eligible flat charges, not automatically to the income charge. The household income test includes the head even if insured elsewhere and may include former members in the stated elderly-transition category. Unknown household income blocks a reduction determination.
5. Cap each component separately, then sum. Apply exact municipal rounding, insured-month and birthday rules using the actual notice. The raw estimates below do not specify that final billing calculation. Do not divide an annual charge by the ordinary instalment count and call that the legally notified payment.

### Rates, bands and thresholds: Shinjuku FY2026 NHI

| Component | Income rate and flat charge | Household annual component cap | Official source |
| --- | --- | --- | --- |
| Medical | 7.51% of all members' bases + JPY 47,600 per insured person | JPY 670,000 (67万円) | Shinjuku FY2026 schedule: https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html |
| Elderly support | 2.80% of all members' bases + JPY 17,600 per insured person | JPY 260,000 (26万円) | Same: https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html |
| Long-term care | 2.43% of bases for insured ages 40-64 + JPY 17,800 per such member | JPY 170,000 (17万円) | Same: https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html |
| Child support, new FY2026 | 0.27% of all members' bases + JPY 1,873 per insured member aged at least 18; flat amount includes JPY 73 adult increment | JPY 30,000 (3万円) | Same: https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html |
| Total when all components reach cap | JPY 1,130,000, derived sum; not a per-person tariff and no care component if nobody qualifies | Derived from 4 caps above | Same: https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html |
| Income-base deduction | JPY 430,000 (43万円) per person if total income at most JPY 24,000,000 (2,400万円), negative base zero | Higher-income deduction tiers not supplied here | Same: https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html |

| Shinjuku flat-charge reduction | Relevant household prior-income ceiling | Official source |
| --- | --- | --- |
| 70% (7割) | JPY 430,000 + JPY 100,000 × max(wage/pension earner count - 1, 0) | Shinjuku reduction table: https://www.city.shinjuku.lg.jp/kenkou/hoken01_002065_00003.html |
| 50% (5割) | Above base + JPY 310,000 × relevant insured/former-member count | Same: https://www.city.shinjuku.lg.jp/kenkou/hoken01_002065_00003.html |
| 20% (2割) | Above base + JPY 570,000 × relevant insured/former-member count | Same: https://www.city.shinjuku.lg.jp/kenkou/hoken01_002065_00003.html |

Use the municipality's definitions for wage/pension earners and the relevant former-member count. All required income must be known, including the head's. Reductions are reflected through known/declared income; an income-tax filing exemption does not mean municipal declaration is unnecessary. Other disaster, involuntary-unemployment, childbirth and child flat-charge relief have their own conditions; check the municipality, not an assumed flat discount.

### Payment matching and tax deduction

| Pattern | Candidate treatment | Check before posting |
| --- | --- | --- |
| NENKIN, PENSION, 年金, 国民年金 | National Pension | Confirm insured person, premium month, paid amount and relief |
| JAPAN PENSION SERVICE, 日本年金機構 | Pension payment | Match JPS record, not just payee |
| 年金前納, ADVANCE PENSION | Advance pension | Match start period, method and discount schedule |
| NHI, 国民健康保険, 国保, KOKUMIN KENKO | NHI premium | Match municipality, household bill and actual settlement |
| 市区町村, CITY OFFICE, WARD OFFICE | Possible NHI | Could be local tax or another charge; verify |
| 口座振替 + municipal name | Possible NHI debit | Require the bill/receipt and avoid double posting |
| 介護保険, LONG-TERM CARE | Care component | Embedded in NHI for applicable ages; separate collection later |
| 健康保険, KENPO, 協会けんぽ | Employer health insurance | Stop duplicate NHI charge and resolve coverage |
| 厚生年金, KOSEI NENKIN | Employees' pension | Employer scheme, not fixed Category 1 premium |

Qualified NHI and pension contributions **actually paid** are income deductions, not a uniform extra business expense. The deduction can include a spouse/relative sharing the livelihood where the taxpayer actually bears the payment; obtain evidence. NTA No. 1130 governs documents and the new statement alternative for relevant 2026 returns filed from 2027. Do not deduct merely billed but unpaid contributions or equate a calculated fiscal total with calendar cash paid.

## Boundary and exception table

| Old scenario | Correct handling | Official source |
| --- | --- | --- |
| Mid-year arrival, including September example | Charge from actual qualification, check prior income rather than assume zero; Shinjuku first-year household can owe a lump sum if head was not resident in Japan on 1 January | Shinjuku qualification/billing: https://www.city.shinjuku.lg.jp/hoken/file02_03_00001.html |
| Freelance plus part-time job | Check actual employer scheme/dependent status first; if legitimately NHI, include all income in municipal base | JPS category explanation: https://www.nenkin.go.jp/international/simplejapanese/japanese-system/nationalpension/nationalpension.html |
| Turns 40 in October | Care component starts in the legal age-attainment month; birthday is attained the preceding day, so a birthday on the first day can change the month | Shinjuku age rules: https://www.city.shinjuku.lg.jp/hoken/file02_03_00001.html |
| Turns 60 in March | Resolve pension qualification-end month and any voluntary election from JPS record; do not apply a full year automatically | JPS categories/voluntary scheme: https://www.nenkin.go.jp/international/simplejapanese/japanese-system/nationalpension/nationalpension.html |
| High income, including JPY 10,000,000 scenario | Compute and cap components separately using the actual municipality and age groups; old total JPY 1,060,000 is not a 2026 Shinjuku ceiling | Shinjuku current schedule: https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html |
| Non-payment, including old 12-month arrears case | Refer promptly for collection/relief; Shinjuku warns of demands, interest and asset seizure. Do not promise the old short-validity insurance-card process | Shinjuku collection section: https://www.city.shinjuku.lg.jp/kenkou/hoken01_002065_00003.html |

## Worked cases

Estimates, not final bills. These retain the old ordinary/low-income/high-income/mid-year cases using current named municipal inputs. Assume full-year coverage, known household income, no special relief unless stated and no other household member. NHI examples show raw component arithmetic before municipal final billing rounding.

### Age 35, prior income JPY 5,000,000, Shinjuku

```oa-check
name: Shinjuku FY2026 ordinary freelancer under 40
inputs:
  income: 5000000
  deduction: 430000
  pension_monthly: 17920
steps:
  - base: max(income - deduction, 0)
  - medical: min(base * 0.0751 + 47600, 670000)
  - support: min(base * 0.028 + 17600, 260000)
  - child_support: min(base * 0.0027 + 1873, 30000)
  - nhi: medical + support + child_support
  - pension: pension_monthly * 12
  - combined: nhi + pension
expected:
  base: 4570000
  medical: 390807
  support: 145560
  child_support: 14212
  nhi: 550579
  pension: 215040
  combined: 765619
```

### Age 45, prior income JPY 20,000,000, Shinjuku caps

```oa-check
name: Shinjuku FY2026 all four component caps
inputs:
  income: 20000000
  deduction: 430000
steps:
  - base: max(income - deduction, 0)
  - medical: min(base * 0.0751 + 47600, 670000)
  - support: min(base * 0.028 + 17600, 260000)
  - care: min(base * 0.0243 + 17800, 170000)
  - child_support: min(base * 0.0027 + 1873, 30000)
  - nhi: medical + support + care + child_support
  - pension: 17920 * 12
  - combined: nhi + pension
expected:
  nhi: 1130000
  combined: 1345040
```

### Low income and mid-year pension

Age 28, prior income JPY 300,000, confirmed 70% flat-charge reduction and no other head/household income: base is zero; raw flat charge is `(47,600 + 17,600 + 1,873) × 30% = JPY 20,121.90` before billing rounding. Pension full exemption is only a possible application until approved; do not automatically subtract it.

Age 30 with exactly 9 confirmed chargeable FY2026 pension months and no relief pays `17,920 × 9 = JPY 161,280`, derived. The old July-arrival NHI case requires the actual revised household bill and qualification months; a blanket annual × 9/12 or division into 10 equal payments is not confirmed here.

## When to refuse or refer

Keep the disability, survivors and voluntary-additional-pension referrals. Never assume municipal NHI rates are uniform, omit an applicable care/child-support component, duplicate employer coverage, call mandatory Category 1 optional, use current income instead of the required preceding year, or reduce the income-based NHI component using the flat-charge reduction. Never default unknown income/age/insurance to a low charge. Missing inputs hold the calculation; uncertain reductions, mid-year allocation, pension age transitions and foreign/social-security agreements require review. Give a social insurance labour consultant the facts, ambiguity, available options and missing evidence, labelled REVIEWER FLAG. Out-of-scope benefits use ESCALATION REQUIRED, no computation.

## Filing and payment

Pension: ordinary monthly payment is due by the end of the following month, moving to the next financial-institution business day for the specified holidays. Use JPS slip at the permitted bank/post/convenience counter, registered bank/card method, smartphone app or Nenkin Net/Pay-easy. Municipality and pension-office counters generally do not receive pension premiums. Retain settlement and deduction certificate; approved relief/refunds must reconcile.

NHI: follow the municipality's notice. In Shinjuku ordinary collection is 10 instalments June-March, month-end/next business day. The non-resident-at-1-January household-head rule can instead require the first-year amount at the first due date. Confirmed pension special collection has a different schedule. Bank debit, municipal/bank/post/convenience payment and supported mobile/Pay-easy methods are not interchangeable without the actual bill. Changes in household, income or age can lead to a revised bill; use the latest.

## Completion checklist

- Actual NHI/pension categories, qualification months and household members confirmed.
- Municipality, prior income, correct basic deduction and age bases documented.
- All FY2026 components, separate caps and applicable relief considered.
- No assumptions of zero income, under-age or absence of employer insurance.
- Pension relief approved, ordinary and childbirth/childcare credit consequences distinguished.
- Actual bill, instalment calendar, bank payment and calendar-year deduction reconciled.
- Every output estimated, not reviewed; missing items and referrals explicit.

## Sources

| Source | Official URL | Read on | Operative material read |
| --- | --- | --- | --- |
| Shinjuku FY2026 NHI calculation | https://www.city.shinjuku.lg.jp/hoken/hoken01_001028.html | 2026-11-14 | Read for all 4 component rows, age bases, flat charges, caps, income deduction and child-support footnote; FY2025/2024 contrasts not used as current |
| Shinjuku premium, reductions and collection | https://www.city.shinjuku.lg.jp/kenkou/hoken01_002065_00003.html | 2026-11-14 | Read for entire calculation/reduction sections and neighboring household-income, arrival, childbirth and collection exceptions; ordinary/lump-sum payment |
| Shinjuku qualification and age changes | https://www.city.shinjuku.lg.jp/hoken/file02_03_00001.html | 2026-11-14 | Read for qualification month, debtor, notices, collection, age 40/65/75 and day-before-birthday rule |
| JPS National Pension overview | https://www.nenkin.go.jp/international/simplejapanese/japanese-system/nationalpension/nationalpension.html | 2026-11-14 | Read for Category 1/2/3, visa exclusions, registration, voluntary routing, current premium, relief and payment |
| JPS ordinary premium and payment | https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryo.html | 2026-11-14 | Read for current monthly premium, due-date holiday rule, payment methods, deduction and non-payment |
| JPS annual premium table | https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryogaku.html | 2026-11-14 | Read for FY2025 and FY2026 amount rows and annual adjustment explanation |
| JPS advance payment | https://www.nenkin.go.jp/service/kokunen/hokenryo/zenno.html | 2026-11-14 | Read for methods, period-specific table and early monthly debit discount; old approximate percentage discounts not used |
| JPS income-tested exemption and deferral | https://www.nenkin.go.jp/service/kokunen/menjo/20150428.html | 2026-11-14 | Read for all current income criteria, partial payments, qualifying persons, effect on benefits, applications and special cases |
| JPS relief-year application periods | https://www.nenkin.go.jp/service/kokunen/menjo/20150402-01.html | 2026-11-14 | Read for current July-June relief-year and corresponding prior-income table |
| JPS childcare exemption | https://www.nenkin.go.jp/service/kokunen/menjo/ikujimenjo.html | 2026-11-14 | Read for entire eligibility, periods/transitions, fully paid credit, application/automatic cases, evidence and end notices, effective October 2026 |
| NTA No. 1130 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1130.htm | 2026-11-14 | Read for actual-paid deduction, family payer conditions, contribution types and required documents including 2026-return statement alternative |

Not yet confirmed: rates/caps and household/asset elements outside the named Shinjuku schedule; high-income NHI deduction tiers; exact municipal final rounding and part-year premium allocation; actual pension qualification-end month on a particular birthday; a specific social-security agreement, relief decision or client bill; current NHI consequences corresponding to the old short-validity insurance-card/qualification-certificate claim. The old generic NHI rate ranges (5-12%, JPY 20,000-60,000/person and JPY 0-30,000/household), Tokyo approximations (7.17%/2.42%/2.14%, JPY 42,100/14,400/15,600), caps JPY 650,000/240,000/170,000 and total JPY 1,060,000, pension discount estimates 1%/2%/4%, and flat partial-relief income thresholds JPY 930,000/1,410,000/1,890,000 are superseded or unsupported, not usable current instructions. Exact advice on disability/survivors benefits and voluntary additional pensions remains outside scope.
